from django.db import transaction
from rest_framework import serializers

from api.entry.models import Entry
from api.user.models import User


class EntrySerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=80)
    created_date = serializers.DateTimeField(
        format="%d/%m/%Y - %H:%M:%S", read_only=True
    )

    class Meta:
        model = Entry
        fields = ["user", "subject", "message", "created_date"]

    def create(self, validated_data):
        username = validated_data.pop("user")
        with transaction.atomic():
            user, _ = User.objects.get_or_create(name=username)
            entry = Entry.objects.create(user=user, **validated_data)
        return entry
