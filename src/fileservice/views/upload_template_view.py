from typing import Any

from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response


class UploadTemplateView(generics.GenericAPIView):
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response(template_name="index.html")
