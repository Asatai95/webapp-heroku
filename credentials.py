from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http


scopes = ['https://www.googleapis.com/auth/admin.directory.user, https://www.googleapis.com/auth/admin.directory.orgunit']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/tmp/googleapi/serviceaccount.json', scopes=scopes)
delegated_credentials = credentials.create_delegated('defense433@gmail.com')  # 権限を委任
http_auth = credentials.authorize(Http())
