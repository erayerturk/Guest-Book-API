import pytest

from api.entry.serializers import EntrySerializer
from api.entry.tests.factories import EntryFactory


@pytest.mark.django_db
@pytest.mark.parametrize(
    "entry_data, expected_error",
    [
        (
            {"subject": "Test Subject", "message": "", "user": "Test User"},
            "This field may not be blank.",
        ),
        (
            {"subject": "Test Subject", "user": "Test User"},
            "This field is required.",
        ),
    ],
)
def test_entry_serializer_validations(entry_data, expected_error):
    serializer = EntrySerializer(data=entry_data)
    assert not serializer.is_valid()
    assert expected_error == str(serializer.errors["message"][0])


@pytest.mark.django_db
def test_entry_serializer_created_date_read_only():
    entry = EntryFactory.create()
    serializer = EntrySerializer(instance=entry)
    assert "created_date" in serializer.data
    assert serializer.data["created_date"] == entry.created_date.strftime(
        "%d/%m/%Y - %H:%M:%S"
    )
