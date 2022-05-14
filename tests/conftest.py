# Create a test client using the Flask application configured for testing
import pytest
import config
from api.app import create_app, db
from api.routes import app
from api.models import User


@pytest.fixture
def client():
    # app = create_app()
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture()
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert test data
    test_user = User(name='Test', email="test@gmail.com", password="12345")
    db.session.add(test_user)
    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!
    db.session.remove()  # looks like db.session.close() would work as well
    db.drop_all()
