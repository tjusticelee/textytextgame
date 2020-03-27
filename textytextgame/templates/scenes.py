from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort

bp = Blueprint('scenes', __name__)

@bp.route('/')
def index():
    return render_template('base.html')

@bp.route('/home', methods=('GET', 'POST'))
def home():

    scene = {
    """Your alarm wakes you up. You lay in bed and decide
    whether or not to skip class. \n
    1. Stay in and sleep
    \n
    2. Get ready for class"""
    }

    if request.method == 'POST':
        choice = request.form['action']

        if choice == "1":
            return redirect(url_for('scenes.bus'))

        if choice == "2":
            return redirect(url_for('scenes.walk'))

@bp.route('/bus', methods('GET', 'POST'))
def bus():

    scene = {
    """You lay in bed and close your eyes. Your mom comes through
    your air vent and yells at you to get up you yell at her
    \"You don't understand me mom!\" She dropkicks you
    into the bus from your room. \n
    \n
    You land in the driver's seat of the bus and realize you have to drive
    the bus. do you?
    \n
    1. Drift dat boi
    \n
    2. Drive like a civilized person"""
    }
