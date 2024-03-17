from rest_framework import serializers

from api.user.models import User


class UserEntryRetrieveSerializer(serializers.ModelSerializer):
    last_entry = serializers.SerializerMethodField()
    message_count = serializers.SerializerMethodField()
    username = serializers.CharField(source="name")

    @staticmethod
    def get_last_entry(user):
        last_entry = user.entry_set.order_by("-created_date").first()
        return f"{last_entry.subject} | {last_entry.message}" if last_entry else ""

    @staticmethod
    def get_message_count(user):
        return user.entry_set.count()

    class Meta:
        model = User
        fields = ["username", "last_entry", "message_count"]
