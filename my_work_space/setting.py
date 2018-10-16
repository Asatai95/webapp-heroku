# import os
#
# try:
#     if os.environ['SECRET_KEY']:
#         SECRET_KEY = os.environ['SECRET_KEY']
# except:
try:
    if os.environ['SECRET_KEY']:
        SECRET_KEY = os.environ['SECRET_KEY']
except:
    SECRET_KEY = '2fsKgOLaAHbJUbi6kJsyboVLPchUjL88iZ7sM3A1'
