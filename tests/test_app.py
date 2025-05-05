import app

def test_homepage():
    tester = app.app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, this is a CI/CD demo!" in response.data
