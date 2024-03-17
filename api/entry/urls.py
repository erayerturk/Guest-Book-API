from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.entry.views import EntryListCreateAPIView

entry_router = DefaultRouter()
entry_router.register(r"", EntryListCreateAPIView, basename="entry")

urlpatterns = [path("", include(entry_router.urls))]
