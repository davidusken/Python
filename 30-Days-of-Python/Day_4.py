# Day 4: Basic Python Collections

# Exercises

# Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
movies = [ ("Drive", "Nicolas Winding Refn", 2011, 15000000), ]

# Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
movietitle = input("Enter movie title: ")
directorname = input("Enter director's name: ")
releaseyear = input("Enter release year: ")
moviebudget = input("Enter budget: ")

# Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
secondmovie = [ (movietitle, directorname, releaseyear, moviebudget), ]

# Add the new movie tuple to the movies collection using append.
movies.append(secondmovie)

# Print both movies in the movies collection.
print(movies)

# Remove the first movie from movies. Use any method you like.
movies.clear()
movies = secondmovie
print(movies)