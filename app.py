"""
Amazing app to help you find nearest MBTA station using Flask
"""

from flask import Flask, request, render_template, redirect, url_for, session
from mbta_helper import find_stop_near

app = Flask(__name__)

# Set secret key
app.secret_key = 'super secret key'

@app.route('/')
def home():
    '''
    Display homepage using index.html. 
    The page will be a form allowing the user to input a place name or address.
    '''
    return render_template('index.html')


@app.route('/nearest', methods=['POST'])
def data():
    '''
    Get the input: place name or address. 
    Check if search work or not by calling find_stop_near() function.
    If works, redirect page to process() fuction at the route /nearest_mbta, using POST method at the route /nearest
    If not work, display error page using error.html
    '''
    place_name = request.form['text']
    session['place_name'] = place_name
    try:
        find_stop_near(place_name)
        return redirect(url_for('process'))
    except:
        return render_template('error.html')


@app.route('/nearest_mbta', methods=['GET', 'POST'])
def process():
    '''
    Get place name or address using GET method at the route /nearest_mbta
    Search for nearest station name and wheelchair accessibility information
    Return those search result through page mbta_station.html
    '''
    if request.method == 'GET':
        place_name = session.get('place_name', None)
        stop, wheelchair = find_stop_near(place_name)
        return render_template('mbta_station.html', nearest_station = stop, wheelchair_accessibility = wheelchair)
