import os

# try:
#     if os.environ['APP_ENVIRONMENT'] == 'production':
#         SECRET_KEY = os.environ['SECRET_KEY']
#         DATABASE = os.environ['DATABASE_URL']
# except:
#     SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'
#     DATABASE = 'ローカル環境かく'

try:
    if os.environ['SECRET_KEY']:
        SECRET_KEY = os.environ['SECRET_KEY']
    if os.environ['HOST_PASSWORD']:
        HOST_PASSWORD = os.environ['HOST_PASSWORD']
    if os.environ['HOST_SMTP']:
        HOST_SMTP = os.environ['HOST_SMTP']
except:
    # for development
    SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'

HOST_EMAIL = 'official@webapp2.com'
