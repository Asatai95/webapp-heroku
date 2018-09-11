import webbrowser
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage


# 利用するAPIのスコープを指定
SCOPE = 'https://www.googleapis.com/auth/bigquery.readonly'
# 認証フローを作成
flow = flow_from_clientsecrets(
    # API有効化時に取得したOAuth用のJSONファイルを指定
    '.credential/client_secret.json',
    # スコープを指定
    scope=SCOPE,
    # ユーザーの認証後の、トークン受け取り方法を指定（後述）
    redirect_uri='http://localhost:8080')

# 認証用URLを発行して、ブラウザで表示する
auth_uri = flow.step1_get_authorize_url()
webbrowser.open(auth_uri)

# トークンをユーザーが入力するまで、処理を待つ
token = input("Input your code > ")
