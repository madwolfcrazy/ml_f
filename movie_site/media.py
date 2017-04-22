#!/bin/python
#coding=utf-8
import webbrowser
class Movie():
    """ A movie object story movie title,storyline,movie's year movie's poster, and movie trailer"""
    def __init__(self, movie_title, movie_storyline,  movie_year, poster_image, trailer_youtube):
        """
            init movie object 
            Args:
                 movie_title => string, movie's title
                 movie_storyline => string, movie's story 
                 movie_year => integer, movie's year
                 poster_image => string, the url of movie's poster
                 trailer_youtube => string, the url of movie's trailer on the youtube 

        """
        self.title   = movie_title
        self.storyline = movie_storyline
        self.year = movie_year 
        self.poster_image_url   =  poster_image
        self.trailer_youtube_url  =  trailer_youtube
    def show_trailer(self):
        """
            show the movie's trailer
        """
        webbrowser.open(self.trailer_youtube_url)

