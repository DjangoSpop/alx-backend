#!/usr/bin/env python3
"""module to get the locale lanaguge"""
from flask import Flask, request
from flask_babel import Babel
import babel
app = Flask(__name__)

@babel.localeselector
def get_locale():
    """Determine the match with our suppoeter"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])
