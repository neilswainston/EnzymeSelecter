'''
(c) University of Liverpool 2019

All rights reserved.

@author: neilswainston
'''
import os
import uuid

from flask import Flask, render_template


# Configuration:
SECRET_KEY = str(uuid.uuid4())

# Create application:
_STATIC_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              'static')

APP = Flask(__name__, static_folder=_STATIC_FOLDER)
APP.config.from_object(__name__)


DEBUG = False
TESTING = False


@APP.route('/')
def home():
    '''Renders homepage.'''
    return render_template('index.html')
