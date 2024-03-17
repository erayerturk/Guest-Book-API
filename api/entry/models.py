from django.db import models

from api.project.base_models import BaseModel
from api.user.models import User


class Entry(BaseModel):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.subject
