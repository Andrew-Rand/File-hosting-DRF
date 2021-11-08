MIME_TYPE__JPG = 'image/jpeg'
MIME_TYPE__PNG = 'image/png'
MIME_TYPE__GIF = 'image/gif'
MIME_TYPE__TIF = 'image/tiff'
MIME_TYPE__SVG = 'image/svg+xml'
MIME_TYPE__PDF = 'application/pdf'
MIME_TYPE__DOC = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
MIME_TYPE__XML = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
MIME_TYPE__TXT = 'text/plain'

ALLOWED_FILETYPES = set(v for k, v in globals().items() if isinstance(v, str))
