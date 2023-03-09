import faker
import pytest

from fixtures.client import Client

fake = faker.Faker()


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    # Todo: Add logger
    return Client(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://petstore.swagger.io/v2"
    )
