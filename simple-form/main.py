'''
Delia Akbari
August 13, 2015
DPWP
Simple-Form Assignment
'''

import webapp2
from pages import Page #from package import class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page() #instance of page

        self.response.write(p.print_out()) #prints out to browser



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
