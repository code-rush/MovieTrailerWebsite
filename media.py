class Movie():
    '''This class provides a way to store movie related information'''

    # Method initialises the object and stores the information of movies
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date, movie_director, movie_stars):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.movie_stars = movie_stars
        self.movie_director = movie_director

    # Additional information about the movies
    def get_movie_details(self):
        print("Storyline: "+self.storyline)
        print("Release Date: "+self.release_date)
        print("Movie Stars: "+self.movie_stars)
        print("Director: "+self.movie_director)
