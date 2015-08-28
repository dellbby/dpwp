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
                <li><a href="?style=shirt">Aztec Crop Top</a></li>
                <li><a href="?style=top>Chanel Drip Top </a></li>
                <li><a href="?style=legging">Striped Leggings </a></li>
                <li><a href="?style=overlay">Mauve Top </a></li>
                <li><a href="?style=suit">White Plunge One Piece Suit </a></li>
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
        self.title = ''
        self.name = ''
        self.price = ''
        self.size = ''
        self.color = ''
        self._image = ''

        @property
        def image(self):
            pass

        @image.setter
        def image(self, new_image):
            self._image = new_image

        self.make = ''
        self.style = ''

    def print_out(self):
        return self._head + self._body + '''<h1> ''' + self.name + '''</h1>''' + '<br><b>Price:</b>' + self.price + '<br><b>Size(s) available</b>' + self.size + '<br><b>Make</b>' + self.make + '<br><b>Color:</b>' + self.color + '<br><b>Style:</b>' + self.style + '<img src="' + self._image + '" />' + self._close