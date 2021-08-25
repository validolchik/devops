"""
    An app that displays current time in Moscow on main page
"""
from flask import Flask
import datetime
import os

def create_app(test_config=None):
    app = Flask(__name__)

    # generate offset for Moscow time zone
    offset = datetime.timezone(datetime.timedelta(hours=3))

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

        # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def moscow_time():
        """
            Generate index page
            returns current time in moscow
        """
        return str(datetime.datetime.now(offset))

    return app
