'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

import webapp2
from library import Grade, GetGrades
from pages import FormPage, ResultsPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #to do list
        #enter in name
        #enter in grade 1
        #enter in grade 2
        #enter in grade 3
        #enter in grade 4
        gg = GetGrades()
        g = Grade()
        p = ResultsPage()
        f = FormPage()

        #page_head = p.head
        #page_form = p.form
        #page_close = p.close
        #page_result = p.result

        if self.request.GET:
            #stores info we got from form/information input
            g.name = self.request.GET['name']  #name
            g.age = self.request.GET['age'] #age
            g.g1 = self.request.GET['g1'] #grade1
            g.g2 = self.request.GET['g2'] #grade2
            g.g3 = self.request.GET['g3'] #grade3
            g.g4 = self.request.GET['g4'] #grade4
            avg = gg.calc_gpa(g)
            p.body = """<div class="form"><h1><p>Hello,<b> """ +g.name + """</b> Here is what you entered:
            <br>
            Grade 1:<b> """ +g.g1 + """</b><BR> Grade 2: <b>""" + g.g2 + """</b> <BR>Grade 3:<b> """ +g.g3 + """</b> <BR> Grade 4: <b>"""  + g.g4 + """ <BR></b>We calculated that your GPA is<b> """+ str(avg) + """</b></b></p></div>"""

            self.response.write(p.print_out())
            #p.body = gg.calc_gpa() + gg.get_grades()
             #below code is what prints out
            #self.response.write(p.print_out())
            #self.response.write(page_head + page_result + '<h2> Hi ' + g.name + ",</h2><br> <h3>Here are the grades you entered:<BR> " + "<b>Age</b>" + g.age + "<b>Grade 1:</b> " +g.g1 + "<BR> <b>Grade 2:</b>" + g.g2 + "<BR><b> Grade 3:</b>" + g.g3 + "<BR><b>Grade 4:</b> " + g.g4 + page_close)
        else:
            self.response.write(f.print_out())
            #self.response.write(page_head + page_form + page_close) - ??
            #print our info on page

#do not touch
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
