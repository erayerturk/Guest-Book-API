from factory import Faker
from factory.django import DjangoModelFactory

from api.entry.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = Faker("name")
