from time_app import create_app
import datetime


def test_date():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        moscow_timezone = datetime.timezone(datetime.timedelta(hours=3))
        datetime_now = datetime.datetime.now(moscow_timezone)

        response = client.get('/')
        assert type(response.data) == type(b'a')
        response_datetime = datetime.datetime.fromisoformat(response.data.decode('utf-8'))
        assert response_datetime > datetime_now