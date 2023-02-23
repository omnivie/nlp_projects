import spacy

# Loading advanced language model
nlp = spacy.load('en_core_web_md')


# Defining a function to find out the most semantically similar movie.
def next_best(model_movie):
    """Return the the most similar movie to watch from the file compared to model movie"""
# Declaring a dictionary and then reading the file and using for loop and  split and strip methods
# adding keys and values to the dictionary.
    movies = {}
    with open('movies.txt', 'r') as mov:
        mov_list = mov.readlines()

        for line in mov_list:
            s = line.split(':')
            movies[s[0]] = s[1].strip('\n')

# Using for loop to find out the movie with the largest semantic similarity to the model movie
    largest_sim = 0
    model_movie = nlp(model_movie)
    for key, value in movies.items():
        similarity = nlp(value).similarity(model_movie)
        if similarity > largest_sim:
            largest_sim = similarity

# Using for loop and if statement to print the movie with the largest semantic similarity for a user
    for key, value in movies.items():
        similarity = nlp(value).similarity(model_movie)
        if similarity == largest_sim:
            print(f' We recommend you to watch movie {key} because it has the largest similarity of {round(largest_sim, 3)} '
                  f'to your original movie')

# Declaring a model movie and running a function to recommend a movie to watch
planet_hulk_brief = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

next_best(planet_hulk_brief)


