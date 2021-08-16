from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def moscow_time():
    offset = datetime.timezone(datetime.timedelta(hours=3))
    return str(datetime.datetime.now(offset))