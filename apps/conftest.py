import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.users.tests import factories as use_factories

register(use_factories.UserFactory)


@pytest.fixture(scope="session")
def django_db_setup():
    # Allow session-level database usage
    pass


@pytest.fixture
def jwt_token():
    user, _ = User.objects.get_or_create(emal="testuser@gmail.com")
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@pytest.fixture
def request_factory():
    return APIRequestFactory()


@pytest.fixture
def authenticated_request_factory():
    user, _ = User.objects.get_or_create(emal="testuser@gmail.com")
    refresh = RefreshToken.for_user(user)
    factory = APIRequestFactory(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return factory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_api_client():
    user, _ = User.objects.get_or_create(emal="testuser@gmail.com")
    refresh = RefreshToken.for_user(user)
    api_client = APIClient()
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client
