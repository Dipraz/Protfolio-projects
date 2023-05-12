from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    movies = search_movie(query)
    return render_template('results.html', movies=movies)

def search_movie(query):
    # API endpoint for movie search
    url = 'https://api.themoviedb.org/3/search/movie'
    api_key = '20030169f16f77d738141a427d86ed91'

    # Parameters for the API request
    params = {
        'api_key': api_key,
        'query': query
    }

    try:
        # Send GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status() # Raise an exception if the status code is not 200

        # Parse the response
        data = response.json()

        # Extract relevant movie details
        movies = data['results']

        if movies:
            return movies
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

if __name__ == '__main__':
    app.run()
<!DOCTYPE html>
<html>
<head>
    <title>Movie Finder App</title>
</head>
<body>
    <h1>Movie Finder App</h1>
    <form action="/search" method="POST">
        <input type="text" name="query" placeholder="Describe a movie">
        <input type="submit" value="Search">
    </form>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
    <title>Movie Finder Results</title>
</head>
<body>
    <h1>Movie Finder Results</h1>
    {% if movies %}
        {% for movie in movies %}
            <h2>{{ movie.title }}</h2>
            <p>Release Date: {{ movie.release_date }}</p>
            <p>Overview: {{ movie.overview }}</p>
            <hr>
        {% endfor %}
    {% else %}
        <p>No movies found.</p>
    {% endif %}
</body>
</html>
