import sys, os
from flask import (
    Blueprint, render_template, request, url_for, send_from_directory, redirect
)
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

from api.db import db_query
from api.util import config

bp = Blueprint('portfolio', __name__, url_prefix="/portfolio")

# @bp.route('/')
# def index():
#     ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

#     db_query(
#         f""" 
#         INSERT INTO "visits" (ip, count) 
#         VALUES('{ip}', {1})  
#         ON CONFLICT (ip) DO
#             UPDATE SET count=visits.count+1 WHERE visits.ip='{ip}' 
#         """
#     )

    # return render_template('index.html')
    # return render_template('index.html')

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
CARDS = [
    {
        'img': 'TODO', 
        'title': 'Cloud API & IoT', 
        'text': 'TODO Screenshot', 
        'description': 'A Flask/React/Bootstrap application that serves my portfolio and exposes API endpoints for IoT devices. Hosted on AWS'
    },
    {
        'img': 'sitestall.png', 
        'title': 'Sitestall', 
        'text': 'Sitestall Screenshot', 
        'description': 'A Firefox extension that improves concentration. A modern implementation of Dr. Richard Patterson\'s ideal "commitment device".'
    },
    {
        'img': 'icelandVis.png', 
        'title': 'GeoSpatial Visualization', 
        'text': 'GeoSpatial Visualization Screenshot', 
        'description': 'A geospatial visualization of Iceland. Rendered with VisIt, automated with Python, video processed with ffmpeg. Available on Youtube.'
    },
    {
        'img': 'discoverdaily.png', 
        'title': 'Discover Daily', 
        'text': 'Discover Daily Spotify Screenshot', 
        'description': 'A Spotify Recommender System. Trains a Classifier on your musical tastes and recommends songs daily. Uses the Spotify API and scikit-learn for machine learning.'
    },
    {
        'img': 'pricedrop.png', 
        'title': 'Pricedrop', 
        'text': 'Pricedrop Screenshot', 
        'description': 'Compares current deals for an amazon product to historic prices and notifies you in case of a good deal. Uses BeautifulSoup, SQLite, and SMTPlib for email notifications.'
    },
    {
        'img': 'sankey.png', 
        'title': 'BudgetVis', 
        'text': 'BudgetVis Screenshot', 
        'description': 'A tool for visualizing your budget. Written in JavaScript with JQuery and Ajax. Graphed with D3.js.'
    },
    {
        'img': 'blue.png', 
        'title': 'Blue', 
        'text': 'Blue Synthesizer Screenshot', 
        'description': 'A polyphonic, MIDI capable audio synthesizer. Written with the JUCE audio framework.'
    },

]

@bp.route('/cards')
@cross_origin()
def get_cards():
    global CARDS
    response = {
        'success': True,
        'cards': CARDS,
    }, 200, {'Content-Type': 'application/json', 'access-control-expose-headers': '*'}
    
    return response

# @app.route('/images/<filename>')
# def get_image(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/up', methods=['POST'])
def upload_file():
    print(request.__dict__)
    # check if the post request has the file part
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)

    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        print('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        # return redirect(url_for('uploaded_file',
        #                         filename=filename))
        return {"message": "good"}

    return {"message": "bad"}

        
