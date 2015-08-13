
import webapp2
from pages import Page #from package import class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page() #instance of page
        p.body = "Miss Piggy Likes Kermit De Frog!"
        self.response.write(p.print_out()) #prints out to browser




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
