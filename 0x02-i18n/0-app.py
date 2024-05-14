#!/usr/bin/env python3
"""Module that renders an index.html."""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')   
def website():
    """Render the website.

    Returns:
        str: Rendered template as a string.
    """    
    return render_template('index.html')
