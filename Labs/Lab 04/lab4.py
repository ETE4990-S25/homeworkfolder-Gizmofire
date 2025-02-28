import json

# Load the JSON data from the file
# with open('movies.json', 'r') as file:
#     movies = json.load(file)


# Ensure the file is read with the correct encoding - used chatgpt here to solve why the file isnt opening due to an encoding error issue
with open('movies.json', 'r', encoding='utf-8') as file:
    movies = json.load(file)



r_movies = []
for movie in movies: 
    if movie["Major Genre"] == "Romantic Comedy":
        # print(movie["Title"])
        r_movies.append(movie)

print(r_movies)

r_movies1 = []
y = float(input("Enter the minimum IMBD rating out of 10: "))
for movie in r_movies:

    if movie["IMDB Rating"] == None:
        break

    if movie["IMDB Rating"] > y:
        r_movies1.append(movie)
    

print("The movies that meet the criteria are: ")
print(r_movies1)

r_movies2 = []
y = int(input("Enter the minimum votes: "))
for movie in r_movies1:
    


    if movie["IMDB Votes"] == None:
        break

    if movie["IMDB Votes"] > y:
        r_movies2.append(movie)
    


print("The movies that meet the criteria are: ")
print(r_movies2)        

r_movies3 = []
y = int(input("Enter the minimum box office dollar amount: "))
for movie in r_movies2:
    
    if movie["US Gross"] == None:
        break   

    if movie["US Gross"] > y:
        r_movies3.append(movie)
    

print("The movies that meet the criteria are: ")
print(r_movies3)

r_movies4 = []
y = int(input("Enter the minimum Rotten Tomatoes Rating out of 100: "))
for movie in r_movies3:
 
    if movie["Rotten Tomatoes Rating"] == None:
        break

 
    if movie["Rotten Tomatoes Rating"] > y:
        r_movies4.append(movie)


    

print("The movies that meet the criteria are: ")
print(r_movies4)


print("\n\n The movies titles that meet the criteria are: ")
for movie in r_movies4:
    print(movie["Title"])

# making of a fun filter engine - removed because i got lazy
# state = True
# while state:

#     filters = ["1) IMDB Rating", "2) IMDB Votes", "3) BoxOffice", "4) Running Time min", "5) Exit"] 

#     applied_filters = [0]
#     filtered_set = []
#     x = input("Enter the filter you want to apply: ")
#     if x in applied_filters:
#         print("Filter already applied")
#         continue
#     else:
#         applied_filters.append(x)
#         for x in applied_filters:
#             print(x)

#         if x == 1:
#             y = float(input("Enter the minimum rating: "))
#             for movie in r_movies:
#                 if movie["IMDB Rating"] > y:
#                     filtered_set.append(movie)

#         elif x == 2:
#             y = int(input("Enter the minimum votes: "))
#             for movie in r_movies:
#                 if movie["IMDB Votes"] > y:
#                     filtered_set.append(movie)

#         elif x == 3:
#             y = int(input("Enter the minimum box office dollar amount: "))
#             for movie in r_movies:
#                 if movie["BoxOffice"] > y:
#                     filtered_set.append(movie)

#         elif x == 4:
#             y = int(input("Enter the minimum running time: "))
#             for movie in r_movies:
#                 if movie["Running Time min"] > y:
#                     filtered_set.append(movie)


#         elif x == 5:
#             state = False











# Search for romance moviesRunning Time min"
# romance_movies = [movie for movie in movies if movie.get("Major Genre") == "Romantic Comedy"]

# Print the titles of the romance movies
# for movie in romance_movies:
#     # print(movie["Title"])
#     print(movie)