from time_app import create_app
import datetime
from time import sleep


def test_date():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        moscow_timezone = datetime.timezone(datetime.timedelta(hours=3))
        datetime_now = datetime.datetime.now(moscow_timezone)
        sleep(1)
        response = client.get('/')
        assert isinstance(response.data, bytes)
        response_datetime = \
            datetime.datetime.fromisoformat(response.data.decode('utf-8'))
        assert response_datetime > datetime_now
