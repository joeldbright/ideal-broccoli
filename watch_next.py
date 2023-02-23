
# Start

import spacy

# load the language model for spacy
nlp = spacy.load("en_core_web_md")

def recommend_movie(movie_description):
    """ This function takes a movie description and returns the title of the most similar movie from a list of movies.
    """
    # convert the movie into a spacy object
    compare_movie = nlp(movie_description)

    # empty variables to be initialized
    most_similar = 0
    recommended_movie = ""

    # open and read the movies file
    with open("movies.txt", "r") as open_movies:
        read_movies = open_movies.readlines()
        # loop through each movie
        for line in read_movies:
            title, description = line.split(":")
            # calculate each movies similarity
            similarity = nlp(description).similarity(compare_movie)

            # find the movie with the highest similarity
            if similarity > most_similar:
                most_similar = similarity
                recommended_movie = title
    
    return print(f"Since you watched: {movie_title[0:-1]}, we recommend: {recommended_movie}")

# title and description of movie to compare
movie_to_compare = "Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
movie_title, movie_description = movie_to_compare.split(":")

recommend_movie(movie_description)

# Stop