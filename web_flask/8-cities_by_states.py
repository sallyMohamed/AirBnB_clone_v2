#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  29 3:24:23 2024
@author: Sally Mohamed
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """fetching data from the storage engine
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def state_info():
    """tag BODY"""
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
