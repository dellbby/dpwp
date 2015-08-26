'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

class FormPage(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/style.css"
        #start Doctype html code - header, form,result,etc.
    	self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>What is your GPA?</title>
        <link href = "css/styles.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        """

        self.body = """
        <header>
            <h1>What is your High School Grade Point Average?</h1>
        </header>
        <div class="form"><form method="GET" action="">
        <h2>Fill out the form below to find out</h2>
        <label>Name: </label><input type="text" name="name" /><br>
        <label> Age: </label><input type="text" name="age" /><br>
        <label>Grade 1</label><input type="text" name="g1" /><br>
        <label>Grade 2</label><input type="text" name="g2" /><br>
        <label>Grade 3:</label><input type="text" name="g3" /><br>
        <label>Grade 4:</label><input type="text" name="g4" /><br>

        <label></label><input type="submit" class="button" value="submit" /></div>
        """

        self.result = """
        <link href = "css/styles.css" rel="stylesheet" type="text/css"/>
        """

        self.close = """


        </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.result + self.close
        return all



class ResultsPage(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/style.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Your Results are in!</title>
        <link href = "css/styles.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>

        <h1> Here are your Results!</h1>
                """
        self.body = ""
        self.close = """
    </body>
    </html>
    """

    def print_out(self):
        all = self.__head + self.body + self.close
        return all
