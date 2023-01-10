from time_app import create_app
import datetime
from time import sleep
from bs4 import BeautifulSoup


def test_date():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        moscow_timezone = datetime.timezone(datetime.timedelta(hours=3))
        datetime_now = datetime.datetime.\
            now(moscow_timezone).replace(tzinfo=None)
        sleep(1)
        response = client.get('/')
        bsh = BeautifulSoup(response.data, 'html.parser')
        time_retrieved = bsh.find('h1').text
        assert isinstance(response.data, bytes)
        response_datetime = \
            datetime.datetime.fromisoformat(str(time_retrieved))
        assert response_datetime > datetime_now
