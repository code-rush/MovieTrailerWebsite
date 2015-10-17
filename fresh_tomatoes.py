import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Favorite Movies!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        span{
            font-weight: bold;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .back {
            padding: 10px;
        }
        /* movie card container */
        .movie-tile {
            margin: 20px 5px 10px 5px;
            padding: 40px;
            height: 400px;
            width: 250px;
        }
        /* movie card front side */
        .movie-tile > .front {
            position: absolute;
            -webkit-transform: perspective(1000px) rotateY(0deg);
            transform: perspective(1000px) rotateY(0deg);
            background: #FFFFFF;
            height: 400px;
            width: 250px;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            transition: transform .5s linear 0s;
        }
        /* movie card back side */
        .movie-tile > .back {
            position: absolute;
            -webkit-transform: perspective(1000px) rotateY(180deg);
            transform: perspective(1000px) rotateY(180deg);
            background: #F5F5F5;
            height: 400px;
            width: 250px;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            transition: transform .5s linear 0s;
        }
        .movie-tile:hover > .front{
            -webkit-transform: perspective(1000px) rotateY(-180deg);
            transform: perspective(1000px) rotateY(-180deg);
        }
        .movie-tile:hover > .back{
            -webkit-transform: perspective(1000px) rotateY(0deg);
            transform: perspective(1000px) rotateY(0deg);
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.btn-primary', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0,

              //Allow full screen video playing
              'allowFullScreen': true
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">My Favorite Movie Cards</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-3 col-lg-4 col-sm-6 movie-tile text-center">
    <div class="front">
        <img src="{poster_image_url}" height="342" width="220">
        <h2>{movie_title}</h2>
    </div>

    <div class="back">
        <div><h3>{movie_title}</h3></div>
        <hr>
        <div class="text-left">
            <p><span>Storyline:  </span>{movie_description}</p>
            <p><span>Release Date: </span>{movie_release_date}</p>
            <p><span>Stars: </span>{movie_stars}</p>
            <p><span>Director: </span>{movie_director}</p>

            <!-- Button to trigger movie trailer modal -->

            <div class="text-center">
                <button type="button" class="btn btn-primary btn-sm" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">Watch Trailer</button> 
            </div>
        </div>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            #Adding details of the movie
            movie_description=movie.storyline,
            movie_release_date=movie.release_date,
            movie_director=movie.movie_director,
            movie_stars=movie.movie_stars
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('my_movies.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
