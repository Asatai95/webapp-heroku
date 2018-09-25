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
except:
    # for development
    SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'
