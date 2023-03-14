import faker
import pytest

from fixtures.app import StoreApp
from fixtures.user.model import CreateUser

fake = faker.Faker()


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    # Todo: Add logger
    return StoreApp(url)


@pytest.fixture()
def auth(app):
    data = CreateUser.random()
    res = app.user.create_user(data)
    return res


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://petstore.swagger.io/v2"
    )
