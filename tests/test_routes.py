from api.models import User


def test_new_user(client, init_database):
    """
    GIVEN the User model
    WHEN a new user is created
    THEN check that the name & email fields are defined correctly
    """
    user = User(name='Cheryl', email="kiddo@gmail.com", password="12345")
    assert user.name == 'Cheryl'
    assert user.email == 'kiddo@gmail.com'


def test_fetch_user(client, init_database):

    path = "/api/v1/2"
    response = client.get(path)
    assert response.status_code == 200


def test_fetch_users(client, init_database):

    path = "api/v1/users"
    response = client.get(path)
    assert response.status_code == 200
