import gettext
from flask import Flask, render_template, request
from flask_babel import Babel
from flask import Flask


app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Function to determine the user's preferred language based on the
    languages provided in the request's Accept-Language header.

    Returns:
        str: The language code of the best match language.
    """
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/')
def home():
    """
    Route handler for the home page.

    Returns:
        str: The rendered HTML template with translated title and header.
    """
    return render_template('3-index.html',
                           title=gettext('home_title'),
                           header=gettext('home_header'))

if __name__ == '__main__':
    app.run()
    