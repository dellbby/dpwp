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
        p = Page() #instance of page
        page_head = p.head
        page_form = p.form
        page_close = p.close
        page_result = p.result


        if self.request.GET:
            #stores info we got from form/information input
            name = self.request.GET['name']  #name
            grade1 = self.request.GET['grade1'] #grade1
            grade2 = self.request.GET['grade2'] #grade2
            grade3 = self.request.GET['grade3'] #grade3
            grade4 = self.request.GET['grade4'] #grade4

             #below code is what prints out
            self.response.write(page_head + page_result + '<h2> Hi ' + name + ",</h2><br> <h3>Here are the grades you entered:<BR> " + "<b>Grade 1:</b> " +grade1 + "<BR> <b>Grade 2:</b>" +grade2+ "<BR><b> Grade 3:</b>" + grade3 + "<BR><b>Grade 4:</b> " + grade4 + page_close)
        else:
            self.response.write(page_head + page_form + page_close)
            #print our info on page

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
