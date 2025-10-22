# tests/conftest.py# tests/conftest.py
import pytest
from app import app, db, User

@pytest.fixture
def client():
    # Configurar la app para testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        db.create_all()

        # Crear usuario de prueba
        test_user = User()
        test_user.username = "testuser"
        test_user.email = "test@example.com"
        test_user.set_password("password123")
        db.session.add(test_user)
        db.session.commit()

    with app.test_client() as client:
        yield client