
import webapp2
from library import MovieData
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()

        #movie title
        #year movie was made
        #director of the film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989 #actually calling a function
        md1.director = "Rob Reiner"

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986 #actually calling a function
        md2.director = "David Lynch"

        self.response.write(p.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
