"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project. It provides three routes:

1. '/' - Renders the index.html template with data obtained from the backend Ateneo_Counter endpoint.
2. '/publicVSprivate' - Renders the publicVSprivate.html template with data obtained fro the backend Public_Private endpoint.
3. '/compare/<param1>/<param">' - Accepts GET and POST requests. GET request renders the compare.html template. POST request fetches data from the backend Ateneo_Comp endpoint based on user-selected universities and renders the compare.html template with comparison results.

Dependencies:
- Flask: Web framework for Python.
- requests: HTTP library for making requests to backend services.

Usage:
- Run this module to start the Flask application on host '0.0.0.0' and port 80. The application interacts with backend servuces to fetch and display data absed on user requests.
"""

from flask import Flask, render_template, request
import requests  # Import the requests library to make HTTP requests

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders the index.html template with data obtained from the backend Ateneo_Counter endpoint.

    Returns:
    - Rendered HMTL template with 'risultato' variable containing JSON data from backend.
    """
    backend_url = 'http://backend/Ateneo_Counter'

    response = requests.get(backend_url)
    response.raise_for_status()

    risultato = response.json()

    return render_template('index.html', risultato=risultato)


@app.route('/publicVSprivate')
def publicVSprivate():
    """
    Renders the publicVSprivatee.html template with data obtained from the backend Public_Private endpoint.

    Returns:
    - Rendered HTML template with 'risultato' variable containing JSON data from backend.
    """
    backend_url = 'http://backend/Public_Private'

    response = requests.get(backend_url)
    response.raise_for_status()

    risultato = response.json()

    return render_template('publicVSprivate.html', risultato=risultato)


@app.route('/compare/<param1>/<param2>', methods=['GET', 'POST'])
def Compare(param1, param2):
    """
    Handles GET and POST requests to '/compare/<param1>/<param2>'.
    GET request: Renders the compare.html template.
    POST request: Fetches data from the backend Ateneo_Comp endpoint based on user-selected universities and renders the compare.html template with comparison results.

    Args:
    - param1 (str): First university parameter.
    - param2 (str): Second university parameter.

    Returns:
    - GET request: Rendered compare.html template
    - POST request: Rendered compare.htl template with 'risultato' variable containg JSON data from backend.
    """
    if request.method == 'POST':
        param1 = request.form.get('param1', 'default_value_1')
        param2 = request.form.get('param2', 'default_value_2')

        backend_url = f'http://backend/Ateneo_Comp/{param1}/{param2}'

        response = requests.get(backend_url)
        response.raise_for_status()

        risultato = response.json()

        return render_template('compare.html', risultato=risultato)
    else:
        return render_template('compare.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
