'''
Delia Akbari
Dynamic Site
August 26, 2015
'''

import webapp2
from page import Everything
from data import Clothing, Data


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #instances
        p = Everything()
        c = Clothing()
        i = Data()

        if self.request.GET:
            style = self.request.GET['style']
            if style == '':
                c = i.pieces[0]
            if style == '':
                c = i.pieces[1]
            if style == '':
                c = i.pieces[2]
            if style == '':
                c = i.pieces[3]
            if style == '':
                c = i.pieces[4]
        else:
            c = i.pieces[0]

        p.name = c.name
        p.price = c.price
        p.size = c.size
        p.make = c.make
        p.color = c.color
        p.style = c.style
        p.image = c.image

        self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
