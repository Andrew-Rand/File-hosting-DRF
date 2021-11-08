from rest_framework.pagination import PageNumberPagination

from src.fileservice.constants import PAGINATION_NUMBER, MAX_PAGE_SIZE


class FilesPagination(PageNumberPagination):
    page_size = PAGINATION_NUMBER
    max_page_size = MAX_PAGE_SIZE
