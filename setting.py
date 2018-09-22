import os

# try:
#     if os.environ['APP_ENVIRONMENT'] == 'production':
#         SECRET_KEY = os.environ['SECRET_KEY']
#         DATABASE = os.environ['DATABASE_URL']
# except:
#     SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'
#     DATABASE = 'mysql://b292b90b1818e0:4346c8fc@us-cdbr-iron-east-01.cleardb.net/heroku_ae66112c0cf1b10'

try:
    if os.environ['SECRET_KEY']:
        SECRET_KEY = os.environ['SECRET_KEY']
except:
    SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'
