from typing import Any
import magic

ALLOWED_FILETYPES = ('image/jpeg', 'image/png', 'application/pdf', 'text/plain', 'video/webm', )


def validate_typefile(value: Any) -> bool:
    file = value.read(2048)
    file_type = magic.from_buffer(file, mime=True)
    print(file_type)
    return file_type in ALLOWED_FILETYPES
