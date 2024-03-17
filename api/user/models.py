from django.db import models

from api.project.base_models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=80, unique=True, db_index=True)

    def __str__(self):
        return self.name
