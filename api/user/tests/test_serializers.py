import pytest

from api.user.serializers import UserEntryRetrieveSerializer
from api.user.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_entry_retrieve_serializer():
    user = UserFactory.create(name="test_user")
    user.entry_set.create(subject="Subject1", message="Message1")
    user.entry_set.create(subject="Subject2", message="Message2")

    serializer = UserEntryRetrieveSerializer(instance=user)

    assert serializer.data["username"] == "test_user"
    assert serializer.data["message_count"] == 2
    assert serializer.data["last_entry"] == "Subject2 | Message2"
