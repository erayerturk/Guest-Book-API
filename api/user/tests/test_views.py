import pytest
from django.urls import reverse
from rest_framework import status

from api.entry.tests.factories import EntryFactory
from api.project.fixtures import api_client
from api.user.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_retrieve_api_view(api_client):
    EntryFactory.create(user=UserFactory.create(name="user1"))
    EntryFactory.create(user=UserFactory.create(name="user2"))

    url = reverse("user-entry-retrieve-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["users"]) == 2
