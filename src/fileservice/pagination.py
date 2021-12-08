from rest_framework.pagination import PageNumberPagination

from src.fileservice.constants import PAGE_SIZE, MAX_PAGE_SIZE


class FilesPagination(PageNumberPagination):
    page_size = PAGE_SIZE
    max_page_size = MAX_PAGE_SIZE
