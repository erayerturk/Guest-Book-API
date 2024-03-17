from api.project.pagination import CustomPaginationSerializer


class PaginationMixin:
    pagination_class = CustomPaginationSerializer
    pagination_class.page_size = 3
