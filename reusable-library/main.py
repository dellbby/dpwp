'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

import webapp2
from pages import Page #from package import class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page() #instance of page
        page_head = p.head
        page_form = p.form
        page_close = p.close
        page_result = p.result

        if self.request.GET:
            #stores info we got from form/information input
            fname = self.request.GET['fname'] #firstname input
            lname = self.request.GET['lname'] #lastname input
            email = self.request.GET['email'] #email
             #below code is what prints out
            self.response.write(page_head + page_result + '<h2> Hi ' + fname + ' ' + lname + ",</h2> " + page_close)
        else:
            self.response.write(page_head + page_form + page_close)
            #print our info on page

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
