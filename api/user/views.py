from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.user.models import User
from api.user.serializers import UserEntryRetrieveSerializer


class UserEntryRetrieveAPIView(ListAPIView, GenericViewSet):
    """
    A view to retrieve a list of users.

    This view retrieves a list of all users with their last entry in the system.

    ### Authentication:
    - No authentication is required to access this endpoint.

    ### Response format:
    - The response is a JSON object containing information about users.

    ### Response schema:
    - username: The username of the user.
    - last_entry: The subject and message of the user's last entry.
    - message_count: The number of entry of the user.

    ### Example response:
    ```
    {
        "users": [
            {
                "username": "example_user",
                "last_entry": "Example Subject | Example Message",
                "message_count": 1
            }
        ]
    }
    ```

    ### Errors:
    - None.

    ### Permissions:
    - This endpoint is public and does not require any specific permissions.

    ### Path:
    - GET /api/v1/users
    """

    queryset = User.objects.all()
    serializer_class = UserEntryRetrieveSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response_data = {"users": data}
        return Response(response_data)
