import os

from flask import Flask, render_template

def create_app(test_config=None):
    '''Create the app and configure it'''
    app = Flask(__name__, instance_relative_config=True)


    @app.route('/')
    def index():
        return render_template('index.html')
