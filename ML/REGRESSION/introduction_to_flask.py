# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 19:54:31 2025

@author: Supravata
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run(host='127.0.0.1', port=5000)
