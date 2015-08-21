'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
