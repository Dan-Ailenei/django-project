import pytest
from {{ cookiecutter.app_name }}.models import {{ cookiecutter.project_name|replace('_', ' ')|title|replace(' ', '') }}User as User


@pytest.fixture
def user(request, db):
    user = User.objects.create(username='test_user', email='test_email@test.com')
    user.set_password('test_password')
    user.save()
    return user


def test_login(client, user):
    assert client.get('/login').status_code == 200
    resp = client.post('/login', {'username': 'test_user', 'password': 'test_password'})
    assert resp.status_code == 302