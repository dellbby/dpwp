
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit']]
        self.response.write(p.print_out())

class Page(object):# borrowing stuff from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE>
<HTML>
    <HEAD>
        <TITLE> </title>
    </head>
    <body>'''
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
        self.__inputs = []
        self._form_inputs = ''
        #<label> First Name: </label><input type = "text" value="" name="" /> ['first_name' , 'text', 'First Name'] placeholder, type, value
        #<label> Last Name: </label><input type = "text" value="" name="first_name" />
        #<input type="text" value="" name="last_name" />
        #<input type="submit" value="Submit" />

    @property
    def inputs(self):
        pass
    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        #sort through mega array and create HTML inputs based on the info there
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a 3rd item, add it in..
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            #otherwise.. end the tag
            except:
                self._form_inputs += '" />'

        print self._form_inputs


    #POLYMORPHISM ALERT! - METHOD OVERRIDING
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
