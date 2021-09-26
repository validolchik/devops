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

    if not os.path.exists("media/visits.txt"):
        os.makedirs("media/")
        f = open("media/visits.txt", 'x')
        f.close()

    @app.route('/')
    def moscow_time():
        """
            Generate index page
            returns current time in moscow
        """
        time_str = str(datetime.datetime.now(offset))
        with open("media/visits.txt", "a") as f:
            f.write(time_str + "\n")
        return time_str

    @app.route('/visits')
    def print_visits():
        """
            Outputs all visits
        """
        with open("media/visits.txt") as f:
            visits = f.read()
        return visits

    return app
