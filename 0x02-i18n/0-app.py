#!/usr/bin/env python3
"""Module that renders an index.html."""
import flask

app = flask.Flask(__name__)

@app.route('/')   
def website():
    """Render the website.

    Returns:
        str: Rendered template as a string.
    """    
    return flask.render_template('index.html')
