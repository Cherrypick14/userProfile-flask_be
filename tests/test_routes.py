import json
from unicodedata import name
from urllib import response
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


def test_update_user(client, init_database):
    path ="/api/v1/3/update"
    response =client.post(path,
     json ={
         "id":5,
         "name":"hunter",
         "email":"hunterfields@gmail.com",
     },
    )
    assert response.status_code == 200

def test_delete_user(client, init_database):
    path= "/api/v1/5/delete"
    response= client.post(path)

    assert response.status_code == 200