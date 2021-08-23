"""
    An app that displays current time in Moscow on main page
"""
from flask import Flask
import datetime

app = Flask(__name__)

# generate offset for Moscow time zone
offset = datetime.timezone(datetime.timedelta(hours=3))

@app.route('/')
def moscow_time():
    """
        Generate index page
        returns current time in moscow 
    """
    return str(datetime.datetime.now(offset))
