from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from api.entry.models import Entry
from api.user.tests.factories import UserFactory


class EntryFactory(DjangoModelFactory):
    subject = Faker("sentence")
    message = Faker("paragraph")
    user = SubFactory(UserFactory)

    class Meta:
        model = Entry
