import pytest
from django.urls import reverse

from api.entry.models import Entry
from api.entry.tests.factories import EntryFactory
from api.project.fixtures import api_client


@pytest.mark.django_db
def test_entry_creation(api_client):
    entry_data = {
        "subject": "Test Subject",
        "message": "Test Message",
        "user": "Test User",
    }
    url = reverse("entry-list")
    response = api_client.post(url, entry_data, format="json")

    assert response.status_code == 201
    assert Entry.objects.count() == 1
    assert Entry.objects.get().subject == "Test Subject"


@pytest.mark.django_db
def test_entry_list(api_client):
    EntryFactory.create_batch(5)
    url = reverse("entry-list")
    response = api_client.get(url, format="json")

    assert response.status_code == 200
    assert response.data.get("count") == 5
