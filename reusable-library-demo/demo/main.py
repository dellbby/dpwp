

import webapp2
from library import MovieData, FavoriteMovies
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        lib = FavoriteMovies()

        #movie title
        #year movie was made
        #director of the film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989 #actually calling a function
        md1.director = "Rob Reiner"
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986 #actually calling a function
        md2.director = "David Lynch"
        lib.add_movie(md2)

        md2 = MovieData()
        md2.title = "Star wars"
        md2.year = 1977 #actually calling a function
        md2.director = "George Lucas"
        lib.add_movie(md2)

        p.body = lib.compile_list() + lib.calc_time_span()
        self.response.write(p.print_out())

        def main(name, GPA):
        print "The GPA for", name,"is",GPA
        return 0

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
