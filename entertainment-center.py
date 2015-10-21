import fresh_tomatoes
import media

# List of movies with their information
avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to\
                        the moon Pandora on a unique mission becomes\
                        torn between following his orders and protecting\
                        the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "18 December 2009",
                     "James Cameron",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver")

iron_man = media.Movie("Iron Man",
                       "After being held captive in an Afghan cave,\
                        an industrialist creates a unique weaponized suit\
                        of armor to fight evil.",
                       "http://ia.media-imdb.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX214_AL_.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY",
                       "2 May 2008",
                       "Jon Favreau",
                       "Robert Downey Jr., Gwyneth Paltrow, Terrence Howard")

schindlers_list = media.Movie("Schindler's List",
                              "In Poland during World War II, Oskar Schindler\
                                gradually becomes concerned for his Jewish\
                                workforce after witnessing their persecution\
                                by the Nazis.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/3/38/Schindler%27s_List_movie.jpg/220px-Schindler%27s_List_movie.jpg",
                              "https://www.youtube.com/watch?v=JdRGC-w9syA",
                              "4 February 1994",
                              "Steven Spielberg",
                              "Liam Neeson, Ralph Fiennes, Ben Kingsley")

moneyball = media.Movie("Moneyball",
                        "Oakland A's general manager Billy Beane's successful\
                            attempt to assemble a baseball team on a\
                            lean budget by employing computer-generated\
                            analysis to acquire new players.",
                        "http://ia.media-imdb.com/images/M/MV5BMjAxOTU3Mzc1M15BMl5BanBnXkFtZTcwMzk1ODUzNg@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=AiAHlZVgXjk",
                        "23 September 2011",
                        "Bennett Miller",
                        "Brad Pitt, Robin Wright, Jonah Hill")

grown_ups = media.Movie("Grown Ups",
                        "After their high school basketball coach passes away,\
                            five good friends and former teammates reunite for\
                            a Fourth of July holiday weekend.",
                        "http://ia.media-imdb.com/images/M/MV5BMjA0ODYwNzU5Nl5BMl5BanBnXkFtZTcwNTI1MTgxMw@@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=cjfuK5QJyEQ",
                        "25 June 2010",
                        "Dennis Dugan",
                        "Adam Sandler, Salma Hayek, Kevin James")

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc and\
                                chaos on the people of Gotham, the caped\
                                crusader must come to terms with one of the\
                                greatest psychological tests of his ability to fight\
                                injustice.",
                              "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                              "https://www.youtube.com/watch?v=yrJL5JxEYIw",
                              "18 July 2008",
                              "Christopher Nolan",
                              "Christian Bale, Heath Ledger, Aaron Eckhart")

shutter_island = media.Movie("Shutter Island",
                             "A U.S Marshal investigates the disappearance\
                                of a murderess who escaped from a hospital\
                                for the criminally insane.",
                             "http://ia.media-imdb.com/images/M/MV5BMTMxMTIyNzMxMV5BMl5BanBnXkFtZTcwOTc4OTI3Mg@@._V1_SX214_AL_.jpg",
                             "https://www.youtube.com/watch?v=5iaYLCiq5RM",
                             "19 February 2010",
                             "Martin Scorsese",
                             "Leonardo DiCaprio, Emily Mortimer, Mark Ruffalo")

the_hurt_locker = media.Movie("The Hurt Locker",
                              "During the Iraq War, a Sergeant recently assigned to an army\
                                bomb squad is put at odds with his squad mates\
                                due to his maverick way of handling his work.",
                              "http://ia.media-imdb.com/images/M/MV5BNzEwNzQ1NjczM15BMl5BanBnXkFtZTcwNTk3MTE1Mg@@._V1_SX214_AL_.jpg",
                              "https://www.youtube.com/watch?v=2GxSDZc8etg",
                              "31 July 2009",
                              "Kathryn Bigelow",
                              "Jeremy Renner, Anthony Mackie, Brian Geraghty")

movies = [schindlers_list, moneyball, avatar, the_dark_knight, shutter_island,
          the_hurt_locker, iron_man, grown_ups]

# Opens list of movies in webbrowser
fresh_tomatoes.open_movies_page(movies)
