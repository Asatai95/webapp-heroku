import webapp2
from models.user import User

webapp2_config = {
    'webapp2_extras.auth': {
        'cookie_name': 'webapp2',
        'user_model': User,
    },
    'webapp2_extras.sessions': {
        'secret_key' : 'webapp2_test',
        'session_max_age' : 60*60*24*30,
    }
}
app = webapp2.WSGIApplication([
    webapp2.Route('/test', TestHandler),
    webapp2.Route('/delete', DeleteHandler),
], debug=True, config=webapp2_config)
