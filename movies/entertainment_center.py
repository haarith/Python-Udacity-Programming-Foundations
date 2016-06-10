import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=uZNHIU3uHT4")
#print(avatar.storyline)
#avatar.show_trailer()

unforgettable = media.Movie("Unforgettable", "Korean Movie 순정 (Unforgettable, 2016) 예고편", "poster_image_url", "https://www.youtube.com/watch?v=uWO7qWAWpGY")
print(unforgettable.storyline)
unforgettable.show_trailer()
