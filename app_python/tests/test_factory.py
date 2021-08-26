from time_app import create_app


def test_creation():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing