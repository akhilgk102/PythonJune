movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {   
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

# Q1 Total number of movies
# print("Total number of movies:",len(movies))

# # Q2 Movies with genre Drama
# drama=[movie.get("title") for movie in movies if "Drama" in movie.get("genres")]
# print(drama)

# # Q3 Latest movie
# def movie(lat):
#     return lat.get("year")
# latest_movie=max(movies,key=movie)
# all_latest=[m.get("title")for m in movies if m.get("year")==latest_movie.get("year")]
# print(all_latest)

# # Q4 print(topest_movie)
# def top_movie(movie):
#     return movie.get("rating")
# topest_movie=max(movies,key=top_movie)
# all_topest_movies=[m.get("title")for m in movies if m.get("rating")==topest_movie.get("rating")]
# print(all_topest_movies)

# # Q5 All malayalm movies
# malayalam_movie=[m.get("title")for m in movies if m.get("language")=="Malayalam"]
# print(malayalam_movie)

# # Q6 movies after year 2016
# after2016=[m.get("title") for m in movies if m.get("year")>2016]
# print(after2016)

# # Q7 movie with lowest rating
# def lowest_movie(movie):
#     return movie.get("rating")
# lowest_rated=min(movies,key=lowest_movie)
# all_lowest=[m.get("title")for m in movies if m.get("rating")==lowest_rated.get("rating")]
# print(all_lowest)

# # Q8 Tamil movies with genre action
# tamil_action=[m.get("title") for m in movies if m.get("language")=="Tamil" and "Action" in m.get("genres")]
# print(tamil_action)

# # Q9 Movies released in same years
# movie_dictinonary={}
# for m in movies:
#     release_year=m.get("year")
#     if release_year in movie_dictinonary:
#         movie_dictinonary.get(release_year).append(m.get("title"))
#     else:
#         movie_dictinonary[release_year]=[m.get("title")]
# print(movie_dictinonary)

# # Q10 Oldest movie
# def oldest_movie(movie):
#     return movie.get("year")
# oldest_movie_data=min(movies,key=oldest_movie)
# oldest_movies=[m.get("title")for m in movies if m.get("year")==oldest_movie_data.get("year")]
# print(oldest_movies)

# # Q11 Movie name with generes either Drama or Comedy
# drama_or_comedy=[m.get("title")for m in movies if "Drama" in m.get("genres") or "Comedy" in m.get("genres")]
# print(drama_or_comedy)

# #Q12 Number of movies in year
# years=[m.get("year")for m in movies]
# years_count={y:years.count(y) for y in years}
# print(years_count)

#Q13 Number of genres
# genres={g for m in movies for g in m.get("genres")}
# print(genres)

#Q14 number of genres count
# all_genres=[g for m in movies for g in m.get("genres")]
# genre_count={g:all_genres.count(g) for g in all_genres}
# print(genre_count)

#Q15

sorted_movies=sorted(movies,key=lambda mov:mov.get("title"))
sorted_movie_tiles=[m.get("title")for m in sorted_movies]
print(sorted_movie_tiles)