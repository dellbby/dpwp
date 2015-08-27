'''
Delia Akbari
Dynamic Site
August 26, 2015
'''

import webapp2
from page import

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #instances
        p = Content()
        c = Clothing()
        i = Info()







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
