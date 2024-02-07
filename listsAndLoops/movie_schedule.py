current_movies = {'The Grinch': '11:00',
                 'Rudolph': '13:00',
                 'Frosty the Snowman': '15:00',
                 'Christmas Vacation': '17:00'}

# afficher tous les films disponibles
print("Voici la liste des films du moment:")
for film in current_movies:
   print(film)

selected_movie = input("Saisissez le film pour lequel vous souhaitez afficher l'horaire\n")

movie_time = current_movies.get(selected_movie)

if movie_time:
   print("Votre film est prévu à ", movie_time, "h", sep='')
else:
   print("Ce film n'existe pas dans le programme")

