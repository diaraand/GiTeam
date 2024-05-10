"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template, request 
import requests  # Import the requests library to make HTTP requests

app = Flask(__name__)

def index ():
    backend_url = 'http://backend/Ateneo_Counter'
    
    response = requests.get(backend_url)
    response.raise_for_status()
    
    risultato = response.json()
    


@app.route('/publicVSPrivate')
def publicVSPrivate():
   backend_url = 'http://backend/Public_Private'
   
   response = requests.get(backend_url)
   response.raise_for_status()
   
   risultato = response.json()
   
   return render_template('publicVSPrivate.html', risultato=risultato)
   
   
@app.route('/compare/<param1>/<param2>', methods= ['GET', 'POST'])   
def Compare (param1, param2):
    if request.method== 'POST': 
    param1= request.form.get ('param1', 'default_value_1')
    param2= request.form.get ('param2', 'default_value_2')
    
    backend_url = f'http://backend/Ateneo_Comp/{param1}/{param2}'
    
    response = requests.get(backend_url)
    response.raise_for_status()
    
    risultato = response.json()
    
    return render_template ('compare.html', risultato=risultato)
else:
    return render_template('compare.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)