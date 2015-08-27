
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

class Page(object):# borrowing stuff from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE>
<HTML>
    <HEAD>
        <TITLE> </title>
    </head>
    <body>

    '''

        self._body ='Filler'
        self._close = '''
    </body>
</html>'''
    def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page): #inheriting class Page - superclass for formpage,
    def __init__(self): #constructor function
        #constructor function for the super class / calling function
        super(FormPage, self).__init__() #Page.__init__() both will work
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        #<label> First Name: </label><input type = "text" value="" name="" /> ['first_name' , 'text', 'First Name'] placeholder, type, value
        #<label> Last Name: </label><input type = "text" value="" name="first_name" />
        #<input type="text" value="" name="last_name" />
        #<input type="submit" value="Submit" />


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
