'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

import webapp2
from pages import Page,
from library import Grade

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
            g1 = self.request.GET['g1'] #grade1
            g2 = self.request.GET['g2'] #grade2
            g3 = self.request.GET['g3'] #grade3
            g4 = self.request.GET['g4'] #grade4

             #below code is what prints out
            self.response.write(page_head + page_result + '<h2> Hi ' + name + ",</h2><br> <h3>Here are the grades you entered:<BR> " + "<b>Grade 1:</b> " +g1 + "<BR> <b>Grade 2:</b>" + g2 + "<BR><b> Grade 3:</b>" + g3 + "<BR><b>Grade 4:</b> " + g4 + page_close)
        else:
            self.response.write(page_head + page_form + page_close)
            #print our info on page

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
