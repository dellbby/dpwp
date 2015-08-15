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
        p = Page() #instance of page - converting page and self
        page_head = p.head #self.head
        page_form = p.form #self.form
        page_close = p.close #self.close
        page_result = p.result #self.result




        if self.request.GET:
            #stores info we got from form/information input
            fname = self.request.GET['fname'] #firstname input
            lname = self.request.GET['lname'] #lastname input
            number = self.request.GET['number'] #phone number input
            city = self.request.GET['city'] #city input
            state = self.request.GET['state'] #state input
            zipcode = self.request.GET['zipcode'] #zipcode input
            email = self.request.GET['email'] #email input
            contact = self.request.GET['contact'] #contact input
            reason = self.request.GET['reason'] #reason input
            #below code is what prints out
            self.response.write(page_head + page_result + 'Name: ' + fname + '<BR> Last name:' + lname + '<br> Phone Number: ' + number + ' <BR> City:' + city + '<BR> State: ' + state + '<br>Zip Code: ' + zipcode + '<BR> Email: ' + email + '<BR> Contact: ' + contact + '<BR> Reason: ' + reason + ''+ page_close)
        else:
            self.response.write(page_head + page_form + page_close)
            #print our info on page

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
