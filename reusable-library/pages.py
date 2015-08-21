class Page(object):
    def __init__(self):
        self.__title = "Calculate your GPA"
        self.css = "css/style.css"
        self.__head = """
<!DOCTYPE HTML>
<HTML>
        <HEAD>
                <TITLE>What is your GPA?</Title>
                <link href="css/style.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
        """
        self.body = ""
        self.__error = ''
        self.__close = """
        </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all
