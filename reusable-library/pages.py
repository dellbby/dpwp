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
            <h1>What is your Grade Point Average?</h1>
        </header>
        <div class="form"><form method="GET" action="">
        <h2>Fill out the form below to find out</h2>
        <label>First Name: </label><input type="text" name="fname" /><br>
        <label>Last Name: </label><input type="text" name="lname" /><br>
        <label></label><input type="submit" class="button" value="submit" /></div>
        """

        self.result = """
        <link href = "css/styles.css" rel="stylesheet" type="text/css"/>
        """

        self.close = """
        <HR>

        </body>
</html>
        """