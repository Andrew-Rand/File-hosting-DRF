import pathlib
from typing import Union

from django.core.files.uploadedfile import UploadedFile
import magic

JPG = 'image/jpeg'
PNG = 'image/png'
GIF = 'image/gif'
TIF = 'image/tiff'
SVG = 'image/svg+xml'
PDF = 'application/pdf'
DOC = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
XML = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
TXT = 'text/plain'

ALLOWED_FILETYPES = {JPG, PNG, GIF, PDF, SVG, TIF, TXT, DOC, XML}


def is_file_type_supported(file: Union[UploadedFile, pathlib.Path]) -> bool:
    if isinstance(file, UploadedFile):
        file = file.read(2048)
        file_type = magic.from_buffer(file, mime=True)
    elif isinstance(file, pathlib.Path):
        file_type = magic.from_file(file, mime=True)
    else:
        raise TypeError
    return file_type in ALLOWED_FILETYPES
