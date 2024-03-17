import pytest
from django.urls import reverse
from rest_framework import status

from api.entry.models import Entry
from api.project.fixtures import api_client


@pytest.mark.django_db
def test_end_to_end_flow(api_client):
    # Create an entry
    entry_data = {
        "subject": "Test Subject",
        "message": "Test Message",
        "user": "Test User",
    }
    entry_url = reverse("entry-list")
    create_entry_response = api_client.post(entry_url, entry_data, format="json")

    assert create_entry_response.status_code == status.HTTP_201_CREATED
    assert Entry.objects.count() == 1
    assert Entry.objects.first().subject == "Test Subject"

    # List entries
    list_entry_response = api_client.get(entry_url, format="json")

    assert list_entry_response.status_code == status.HTTP_200_OK
    assert list_entry_response.data.get("count") == 1

    # Check user endpoint
    user_entry_url = reverse("user-entry-retrieve-list")
    user_entry_response = api_client.get(user_entry_url)

    assert user_entry_response.status_code == status.HTTP_200_OK
    assert len(user_entry_response.data["users"]) == 1
    assert (
        user_entry_response.data["users"][0].get("last_entry")
        == f"{entry_data['subject']} | {entry_data['message']}"
    )
