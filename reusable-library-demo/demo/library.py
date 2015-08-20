class FavoriteMovies(object):
    def __init__(self):
        pass
        #to do: have array to hold movie info
        #have way to add to array
        #generate list of movies at end
        #function to do calculation/time span between movies


class MovieData(object):  #data object
    def __init__(self):   #3 attributes below
        self.title = ''
        self.__year = 0   #check for valid year
        self.director = ''

    @property #return info
    def year(self):
        pass

    @year.setter #recieve info
    def year(self, y):
        if y > 2014: #if date isnt vaild
            print "Error, invaild date!"
            self.__year = 2014
        else:
            self.__year = y