'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

class Page(object):
    def __init__(self):
        #start Doctype html code - header, form,result,etc.
    	self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>What is your GPA?</title>
        <link href = "css/styles.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        """

        self.form = """
        <header>
            <h1>What is your High School Grade Point Average?</h1>
        </header>
        <div class="form"><form method="GET" action="">
        <h2>Fill out the form below to find out</h2>
        <label>Name: </label><input type="text" name="name" /><br>
        <label>Grade 1</label><input type="text" name="grade1" /><br>
        <label>Grade 2</label><input type="text" name="grade2" /><br>
        <label>Grade 3:</label><input type="text" name="grade3" /><br>
        <label>Grade 4:</label><input type="text" name="grade4" /><br>

        <label></label><input type="submit" class="button" value="submit" /></div>
        """

        self.result = """
        <link href = "css/styles.css" rel="stylesheet" type="text/css"/>
        """

        self.close = """


        </body>
</html>
        """