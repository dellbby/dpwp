'''
Delia Akbari
Dynamic Site
August 26, 2015
'''

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<HTML>
    <HEAD>
        <TITLE>WELCOME TO CALICLOSET.COM</TITLE>
    </HEAD>

    <BODY>'''
        self._body = '''
        <div id="container">
            <ul id ="navi">
                <li><a href=></li>
            </ul>'''

        self._close = '''
            <footer><HR>  Copyright 2015 - Cali Closet. </footer>
        </div>
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class Everything(Page):
    def __init__(self):
        super(Everything, self).__init__()

    def print_out(self):
        return self._head + self._body + '''<h1> ''' + self.name + '''</h1>''' + '<br><b>Price:</b>' + self.price + '<br><b>Size(s) available</b>' + self.size + '<br><b>Make</b>' + self.make + '<br><b>Color:</b>' + self.color + '<br><b>Style:</b>' + self.style +  '<img src="' + self._image + '" />' + self._close