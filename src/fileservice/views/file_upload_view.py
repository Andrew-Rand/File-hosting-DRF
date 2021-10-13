from typing import Any

from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from src.basecore.responses import OkResponse


class FileUploadView(generics.GenericAPIView):
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # response_data = {"Do you see any files?": "I also don`t see, but files are here!"}
        # return OkResponse(data=response_data)
        return Response(template_name="index.html")
