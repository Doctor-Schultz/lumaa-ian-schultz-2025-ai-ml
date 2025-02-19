# Written by Ian Schultz. For any questions please contact: ischultz@asu.edu or 6023776290

import textwrap
import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# hyperparameters
tfidf_vectorizer = TfidfVectorizer()
rows = 1500
nRecommendations = 5
userDescription = ""

def vectorizeData(moviesDF):
    """Converts paragraphs of text in to vectors using sklearn's tfidf_vectorizer and returns a matrix. 
       We can only vectorize the user's description in the context of the other movie descriptions,
       so it must be included in the dataset.
    """
    
    moviesDF.loc[-1] = ['User Description', userDescription]
    moviesDF.index = moviesDF.index + 1
    moviesDF.sort_index(inplace=True) 

    return tfidf_vectorizer.fit_transform(moviesDF['overview'])

def findSimilarity(vectorizedMovies):
    """Computes the cosine similarity score between a dataframe of vectors, returns  a column vector of these scores."""

    # While this does compute similarity between user description and itself, 
    # keeping arrays the same size prevents the code from getting ugly in my opinion:
    cosSimilarities = cosine_similarity(vectorizedMovies[0], vectorizedMovies)
    cosSimilarities = cosSimilarities.transpose() # make vertical so it can be a column in moviesDF
    return cosSimilarities

def printRecommendations(moviesDF):
    """Sorts a moviesDF by cosine similarity score, then prints the top n results."""

    moviesDF = moviesDF.sort_values(by='similarity', ascending=False)
    top_n_similar_movies = moviesDF.head(nRecommendations)

    # Printing the actual results:
    print("\n======================================\n")
    print("Your recommended movies, in descending order:\n")
    for index, row in top_n_similar_movies.iterrows():
        print(f"Title: {row['title']}")
        print(f"Cos Similarity: {row['similarity']}")
        tmpDesc = f"Description: {row['overview']}"
        # Since this is a terminal application, the text will be annoying to read if it is on one huge line
        wrapped_text = textwrap.fill(tmpDesc, width=120)
        print(wrapped_text)
        print("\n")

def main(moviesDF):
    """Coordinates: vectorization of movie descriptions, computation of cosine scores, and printing of top results."""
    # STEP 2 - convert movie descriptions to vectors so we may compute cos of their angles (this corresponds to their similarity)
    vectorizedMovies = vectorizeData(moviesDF)

    # STEP 3 - compute cosine similarity for user description and each entry in database
    moviesDF['similarity'] = findSimilarity(vectorizedMovies)

    # STEP 4 - finally, recommend movies to the user by highest cos similarity
    moviesDF = moviesDF[moviesDF['title'] != 'User Description'] # We don't need the user description in here anymore
    printRecommendations(moviesDF)
  
if __name__ == "__main__":
    # EXAMPLE USAGE:
    # python3 movieRecommender.py numRows numRecommendations
    # python3 movieRecommender.py 2000 5

    try:
        rows = int(sys.argv[1])
        nRecommendations = int(sys.argv[2])
    except IndexError:
        print("ERROR: Improper arguments. Must follow the format: python3 movieRecommender.py numRows numRecommendations")
        exit(1)

    if rows > 14300:
        print("ERROR: Number of requested rows is too high")
        exit(1)
    elif nRecommendations > rows:
        print("ERROR: Requesting more recommendations than number of rows used")
        exit(1)

    while(True):
        userDescription = input("Type 1 to exit, or enter a brief description of what type of movie you like:\n")
        if userDescription == "1":
            exit(0)
        
        # STEP 1 - load database (must reload when performing a new search)
        moviesDF = pd.read_csv("movies_dataset.csv", nrows=rows)
        moviesDF = moviesDF.dropna() # some of the 'overview' entries are empty
        moviesDF = moviesDF[['title', 'overview']] # The only features we care about
        
        main(moviesDF)