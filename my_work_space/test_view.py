import os
import pprint

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

pp = pprint.PrettyPrinter(indent=2)

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_id.json"

# This access scope grants read-only access to the authenticated user's Drive
# account.
SCOPES = ['https://www.googleapis.com/auth/plus.me']
API_SERVICE_NAME = 'plus'
API_VERSION = 'v1'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def list_drive_files(service, **kwargs):
  results = service.files().list(
    **kwargs
  ).execute()

  pp.pprint(results)

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  list_drive_files(service,
                   orderBy='modifiedByMeTime desc',
                   pageSize=5)





-----------------test------------------------

def google_token():

    SCOPE = "https://www.googleapis.com/auth/plus.me"

    # credentials = "4/cwBlEwPmFR80S0p4lr1bLnN8HzWA173HaB6VSgDCQ8vRcxGl_kiMzBY"
    # # #
    flow = flow_from_clientsecrets(
    # API有効化時に取得したOAuth用のJSONファイルを指定
    'client_id.json' ,
    # スコープを指定
    scope=SCOPE,
    # ユーザーの認証後の、トークン受け取り方法を指定（後述）
    redirect_uri='urn:ietf:wg:oauth:2.0:oob',
    )

    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open(auth_uri)

    token = input("Input your code > " )

    url = 'https://www.googleapis.com/plus/v1/people/me?access_token=%s'%(token)

    print(url)
    return url
    #



    #
    # test = flow.step2_exchange(token)
#     # Storage(CREDENTIALS_FILE).put(test)
#     flow = flow_from_clientsecrets( './google/client_secret_test.json' ,
#                                 scope=SCOPE,
#                                 redirect_uri='urn:ietf:wg:oauth:2.0:oob')
#     url_l = flow.step1_get_authorize_url()
#     code = '4/dABUOMbzknp2JB4GJFTcI4GhFAE8hHJgJIvfOo_LLESbNIXWi0vVQKE'
#     cre = flow.step2_exchange(code)
#     http = cre.authorize(httplib2.Http())
#     service = build('oauth2','v2',http=http)
#     project_id = "webapp2-heroku"
#     result = service.userinfo().list(userId='me', collection='public').execute()
#     tasks = result.get('id', [])
#     for task in tasks:
#        print(task)
#
#
#     # credentials = Storage(CREDENTIALS_FILE).get()
#     # http_auth = credentials.authorize(httplib2.Http())
#     # service = build('oauth2', 'v2', http=http_auth)
#
#
#     # result = service.userinfo().get().execute()
#
#
#     # people_resource = service.people()
#     # people_document = people_resource.get(userId='me').execute()
#     #
#     # print "ID: " + people_document['id']
#     # print "Display name: " + people_document['displayName']
#     # print "Image URL: " + people_document['image']['url']
#     # print "Profile URL: " + people_document['url']
#
# USER_ID = '103742640349868179233'
# DEVELOPER_KEY = "AIzaSyCIX4ugoPiD68JtA3Bq2UZfgAknR_NqGmU"
