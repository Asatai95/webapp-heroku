import os
from bottle import  (
    route, run, template, static_file, url, get, post,
    request, response, redirect, hook,
)

# database
from app_setting import session
from models.user import User
from models.social import Social
from models.plan import Plan

# library
from library import *

# setting
import app_setting

#api
import requests

# stripe
import stripe
stripe.api_key = app_setting.STRIPE_SECRET

from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl

# 各ルートのメソッドの実行前に実行される
@hook('before_request')
def before_action():
        global current_user
        current_user = get_current_user()

# 各ルートのメソッドreturnの後に実行される
@hook('after_request')
def after_action():
        session.close()

@route('/test')
def test():

    get_twitter_access_token()

@route('/twitter/login')
def test_login():

    twitter = OAuth1Session(app_setting.CONSUMER_KEY, app_setting.CONSUMER_SECRET)

    response = twitter.post(
        'https://api.twitter.com/request_token',
        params={'oauth_callback': 'http://www.webapp2.com/twitter/callback'}
    )

    request_token = dict(parse_qsl(response.content.decode("utf-8")))

    authenticate_url = "https://api.twitter.com/oauth/authenticate"
    authenticate_endpoint = '%s?oauth_token=%s' \
        % (authenticate_url, request_token['oauth_token'])

    print(authenticate_endpoint)

    redirect(authenticate_endpoint)

@route('/')
def index():

    return template('templates/index',url=url, current_user=current_user)

@route('/charge', method='POST')
def index_pay():

    return template('templates/charge', url=url, current_user=current_user)


@route('/mypage')
def mypage():

    if current_user.email is None:
        redirect('/mypage/edit')

    socials = get_socials_info(current_user)
    plan = session.query(Plan).get(current_user.plan_id) if current_user.plan_id else None
    return template('templates/users/mypage',
                    url=url,
                    current_user=current_user,
                    socials=socials,
                    plan=plan,
                    publish_key=app_setting.STRIPE_PUBLISHABLE)

@route('/mypage/edit', method='GET')
def mypage_edit_get():
    return template('templates/users/edit',url=url, current_user=current_user, duplicate_error=None)

@route('/mypage/edit', method='POST')
def mypage_edit_post():
    if is_duplicate_email(request.POST.getunicode('email')):
            duplicate_error = '既に登録されているメールアドレスです'
            return template('templates/users/edit', url=url, current_user=current_user, duplicate_error=duplicate_error)

    update_user(current_user, request.POST)
    redirect('/mypage')

@route('/mypage/edit_password', method='GET')
def mypage_password_edit_get():
    return template('templates/users/edit_password',url=url, current_user=current_user)

@route('/mypage/create_card', method='POST')
def mypage_create_card():

    customer = stripe.Customer.create(
        email = request.POST.getunicode('stripeEmail'),
        source = request.POST.getunicode('stripeToken')
    )

    set_stripe_id(current_user, customer.id)

    return template('templates/users/create_card',
                    url=url,
                    current_user=current_user)

@route('/mypage/edit_card', method='POST')
def mypage_edit_card():

    customer = stripe.Customer.retrieve(current_user.stripe_id)
    customer.source = request.POST.getunicode('stripeToken')
    customer.save()

    redirect('/mypage')

@route('/products/<product_id:int>')
def products_detail(product_id):
    return template('templates/products',
                    url=url,
                    current_user=current_user,
                    product_id=product_id,
                    publish_key=app_setting.STRIPE_PUBLISHABLE)

@route('/products/charge', method='POST')
def products_charge():

    if current_user.stripe_id is None:
        redirect('/mypage')

    charge = stripe.Charge.create(
        customer = current_user.stripe_id,
        amount = request.POST.getunicode('amount'),
        currency = 'jpy',
        description = request.POST.getunicode('description')
    )

    return template('templates/charge',
                    url=url,
                    current_user=current_user)

@route('/mypage/edit_password', method='POST')
def mypage_password_edit_post():
    update_password(current_user, request.POST)
    redirect('/mypage')

@route('/plans')
def plans():

    plans = session.query(Plan).all()
    return template('templates/plan',
                    url=url,
                    current_user=current_user,
                    plans=plans)

@route('/plans/<namespace>')
def plans_detail(namespace):

    plan = session.query(Plan).filter(Plan.namespace==namespace).first()
    if plan is None:
        redirect('/plans')

    return template('templates/plans_detail',
                    url=url,
                    current_user=current_user,
                    plan=plan)

@route('/plans/<namespace>/charge', method='POST')
def plans_charge(namespace):

    if current_user is None:
        redirect('/users/login')
    if current_user.stripe_id is None:
        redirect('/mypage')

    plan = session.query(Plan).filter(Plan.namespace==namespace).first()

    if plan is None:
        redirect('/plans')

    if current_user.plan_id is None:
        subscription = stripe.Subscription.create(
                 customer = current_user.stripe_id,
                 items = [{
                     'plan': plan.stripe_plan_id,
                 }]
        )

        current_user.plan_id = plan.id
        current_user.stripe_subscription_id = subscription.id
        session.commit()

    return template('templates/charge',
                    url=url,
                    current_user=current_user,
                    plan=plan)

@route('/users/sign_up', method="GET")
def users_new():
        is_logged_in_redirect(current_user)
        duplicate_error = None
        return template('templates/users/new',url=url, current_user=current_user, user=User(), duplicate_error=duplicate_error)

@route('/users/sign_up_confirm', method="POST")
def users_new_confirm():
        is_logged_in_redirect(current_user)
        user = User(
                email=request.POST.getunicode("email"),
                password=request.POST.getunicode("password1"),
                name=request.POST.getunicode("name"),
                age=request.POST.getunicode("age"),
        )

        if is_duplicate_email(user.email):
                duplicate_error = '既に登録されているメールアドレスです'
                return template('templates/users/new', url=url, current_user=current_user, user=user, duplicate_error=duplicate_error)

        return template('templates/users/new_confirm', url=url, current_user=current_user, user=user )

@route('/users/sign_up', method="POST")
def users_create():
        is_logged_in_redirect(current_user)

        user = create_user(request.POST)
        send_mail(user.email, 'create')
        return template('templates/users/create', url=url, user=user, current_user=current_user)

@route('/users/login', method='GET')
def login_get():
        is_logged_in_redirect(current_user)
        return template('templates/users/login', url=url, current_user=current_user)

@route('/users/login', method='POST')
def login_post():
        is_logged_in_redirect(current_user)

        if authenticate(request.POST):
            redirect('/')
        else:
            return template('templates/users/login', url=url, current_user=current_user)

"""
passはスルー
"""

@route('/facebook/login')
def facebook_login():

    url = 'https://www.facebook.com/dialog/oauth'
    params = {
        'response_type': 'code',
        'redirect_uri': app_setting.FACEBOOK_CALLBACK_URL,
        'client_id': app_setting.FACEBOOK_ID
    }

    redirect_url = requests.get(url, params=params).url
    print(redirect_url)
    # print('r.url:', r.url)
    # print('r: ', vars(r))
    # return r.url
    # redirect_url = r.url

    redirect(redirect_url)

@route('/facebook/callback')
def facebook_callback():
    try: # 予期せぬエラーがでたらログイン画面にリダイレクトする
        if request.GET.getunicode('code'):
            access_token = get_facebook_access_token(request.GET.getunicode('code'))
            data = check_facebook_access_tokn(access_token)
            if data['is_valid']:
                data = get_facebook_user_info(access_token, data['user_id'])
                if check_socials(data, 'facebook'):
                    login_user(user.id)
                    redirect('/')
                else:
                    user = create_facebook_user(data)
                    create_socials(user, data, 'facebook')
                    login_user(user.id)
                    redirect('/')
            else:
        		# アクセストークンが不正なものだったらログイン画面にリダイレクトする
                redirect('/users/login')

    except:
        redirect('/users/login')


@route('/users/logout')
def logout():
        logout_user()
        return template('templates/users/logout', url=url, current_user=None)


@route('/static/<filepath:path>', name='static_file')
def server_static(filepath):
        return static_file(filepath, root='static')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
