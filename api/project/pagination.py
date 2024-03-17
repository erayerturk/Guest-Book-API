from rest_framework import pagination
from rest_framework.response import Response


class CustomPaginationSerializer(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "page_size": self.page.paginator.per_page,
                "total_pages": self.page.paginator.num_pages,
                "current_page_number": self.page.number,
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "entries": data,
            }
        )
