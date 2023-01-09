"""
    An app that displays current time in Moscow on main page
"""
from flask import Flask, render_template
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
        time_now = datetime.datetime.now(offset).strftime("%Y-%m-%d %H:%M:%S")
        with open("media/visits.txt", "a") as f:
            f.write(str(time_now) + "\n")
        return render_template('main.html', utc_dt=time_now)

    @app.route('/visits')
    def print_visits():
        """
            Outputs all visits
        """
        with open("media/visits.txt") as f:
            visits = f.readlines()
        return "<br>".join(visits)

    return app
