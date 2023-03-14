import faker
import pytest

from fixtures.app import StoreApp
from fixtures.user.model import CreateUser, LoginUser

fake = faker.Faker()


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    # Todo: Add logger
    return StoreApp(url)


@pytest.fixture()
def create(app):
    data = CreateUser.random()
    res = app.user.create_user(data)
    return res


@pytest.fixture()
def login(app):
    data = LoginUser.random()
    res = app.user.login_user(data)
    return res


@pytest.fixture()
def logout(app):
    res = app.user.logout_user()
    return res


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://petstore.swagger.io/v2"
    )
