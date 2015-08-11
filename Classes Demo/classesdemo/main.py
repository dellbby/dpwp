
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact US"
        contact_button.show_label()

class Button(object):
    def __init__(self): #constructor method
        #print "constructor method of button ran"
        self.label = "" #public attribute
        self.__size = 60 #private attribute - two underscores
        self._color = "0x0000" #protected attribute - 1 underscore
        #self.on_roll_over("Hello!!")


    def click(self): #click method
        print "I've been clicked"

    def on_roll_over(self, message): #onRollover method
        print "You've rolled over my button " + message

    def show_label(self):
        print "MY label is " + self.label

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
