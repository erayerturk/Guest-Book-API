from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.user.views import UserEntryRetrieveAPIView

user_router = DefaultRouter()
user_router.register(r"", UserEntryRetrieveAPIView, basename="user-entry-retrieve")

urlpatterns = [path("", include(user_router.urls))]
