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
        page_head = p.head
        page_form = p.form
        page_close = p.close
        page_result = p.result




        if self.request.GET:
            #stores info we got from form
            fname = self.request.GET['fname']
            lname = self.request.GET ['lname']
            number = self.request.GET ['number']
            self.response.write(page_head + page_result + ' ' + fname +  + lname + number + page_close )
        else:
            self.response.write(page_head + page_form + page_close)
            #print our info on page


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
