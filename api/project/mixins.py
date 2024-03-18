from django.conf import settings

from api.project.pagination import CustomPaginationSerializer


class PaginationMixin:
    pagination_class = CustomPaginationSerializer
    pagination_class.page_size = settings.PAGINATION_PAGE_SIZE
