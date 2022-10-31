import IMDbPY
rating = open("data_hw5/ratings.list", 'r')
rating.close()

film = IMDbPY.IMDb()

search = film.get_top250_movies()

for i in range(250):
    print(search[i]['title'])

def movies(*args):
    for i in args:
        movies = open(f"data_hw5/{i}", 'w')
        movies.close()

movies('top250_movies.txt', 'ratings.txt', 'years.txt')