import flask



app = flask.Flask(__name__)
@app.route('/')
    
def website():
    """_summary_

    Returns:
        _type_: _description_
    """    
    return flask.render_template('index.html')
  