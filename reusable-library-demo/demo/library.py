class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        #to do: have array to hold movie info
        #have way to add to array
        #generate list of movies at end
        #function to do calculation/time span between movies
    def add_movie(self, m):
        self.__movie_list.append(m)
        #print m.title
        #<movie data object>

    def compile_list(self):
        output = ''
        for movie in self.__movie_list: #for each movie in movie array
            output += 'Title: ' + movie.title + ' (' + str(movie.year) + ')' 'Directed by ' + movie.director + '<br>'
        return output

    def calc_time_span(self):
        '''
        calculate the time in between movies
        '''
        #years
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)


        #sort years from low to high
        years.sort()

        #subtract the low year from the high year
        num = len(years) -1
        span = years [num] - years[0] #last number - first number
        #return the span of time
        return 'The span between films is ' + str(span)


class MovieData(object):  #data object
    def __init__(self):   #3 attributes below
        self.title = ''
        self.__year = 0   #check for valid year
        self.director = ''

    @property #return info
    def year(self):
        return self.__year

    @year.setter #recieve info
    def year(self, y):
        if y > 2014: #if date isnt vaild
            print "Error, invaild date!"
            self.__year = 2014
        else:
            self.__year = y