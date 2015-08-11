'''
Delia Akbari
Date
Class
Assignment
'''

import webapp2 # use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):
    #function that starts everything. Initializing function, catalyst, starts reaction

        self.response.write('Hello world!')
        #code goes here

    def additonal_function(self):
        pass
        #code goes here


#never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
