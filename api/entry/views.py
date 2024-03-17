from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import GenericViewSet

from api.entry.models import Entry
from api.entry.serializers import EntrySerializer
from api.project.mixins import PaginationMixin


class EntryListCreateAPIView(PaginationMixin, ListCreateAPIView, GenericViewSet):
    """
    A view to list and create entries.

    This view allows users to list existing entries and create new entries.

    ### Authentication:
    - Authentication is required to access this endpoint.

    ### Response format:
    - The response format is JSON.

    ### Request data format:
    - The request data should be in JSON format.

    ### Response schema:
    - user: The username of the user who created the entry.
    - subject: The subject of the entry.
    - message: The message of the entry.
    - created_date: The date and time when the entry was created.

    ### Example response:
    ```
    {
        "user": "example_user",
        "subject": "Example Subject",
        "message": "Example Message",
        "created_date": "2022-03-15T12:00:00Z"
    }
    ```

    ### Errors:
    - If the request data is invalid, a 400 Bad Request error is returned.
    - If there is a server error during entry creation, a 500 Internal Server Error is returned.

    ### Permissions:
    - These endpoints are public and does not require any specific permissions.

    ### Path:
    - GET /api/v1/entries/ : List existing entries
    - POST /api/v1/entries/ : Create a new entry
    """

    queryset = Entry.objects.select_related("user")
    serializer_class = EntrySerializer
