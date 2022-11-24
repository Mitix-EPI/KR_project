import random
from semantics import return_correct_thumbnail, return_movies, get_description_of_the_movie
import numpy as np

movies = return_movies()

def guess_movie_title_by_img(movie):
    try:
        url = return_correct_thumbnail(movie['image']['value'])
        movie_title = movie['titleMovie']['value']
        question = "What is the movie through this image ?"
        answer = movie_title

        return url, question, answer
    except:
        return "Error guess_movie_title_by_img", "Error guess_movie_title_by_img", "Error guess_movie_title_by_img"

def guess_movie_title_by_description(movie):
    try:
        url = return_correct_thumbnail(movie['image']['value'])
        movie_title = movie['titleMovie']['value']
        movie_description = get_description_of_the_movie(movie_title)
        movie_description = movie_description.replace(movie_title, "[The name of the movie]")
        question = "Description : " +  movie_description + " What is the name of the movie ?"
        answer = movie_title

        return url, question, answer
    except:
        return "Error guess_movie_title_by_description", "Error guess_movie_title_by_description", "Error guess_movie_title_by_description"

def guess_one_actor_movie_by_title(movie):
    try:
        url = return_correct_thumbnail(movie['image']['value'])
        movie_title = movie['titleMovie']['value']
        actors = movie['actors']['value'].replace("http://dbpedia.org/resource/", "").replace("_", " ").replace(" (actor)", "").split(' / ')
        question = "Type one actor acting in the movie '" + movie_title + "'."
        answer = actors

        return url, question, answer
    except:
        return "Error guess_one_actor_movie_by_title", "Error guess_one_actor_movie_by_title", "Error guess_one_actor_movie_by_title"

def guess_country_movie_by_title(movie):
    try:
        url = return_correct_thumbnail(movie['image']['value'])
        movie_title = movie['titleMovie']['value']
        country = movie['country']['value'].replace("http://dbpedia.org/resource/", "")
        question = "What country is the movie '" + movie_title + "' from ?"
        answer = country

        return url, question, answer
    except:
        return "Error guess_country_movie_by_title", "Error guess_country_movie_by_title", "Error guess_country_movie_by_title"

questions = {
    '1': guess_movie_title_by_img,
    '2': guess_movie_title_by_description,
    '3': guess_one_actor_movie_by_title,
    '4': guess_country_movie_by_title,
}

def get_random_question():
    
    while 1:
        random_nbr = str(random.randint(1, 4))
        url, question, answer = questions[random_nbr](np.random.choice(movies))
        if answer != '':
            return url, question, answer


