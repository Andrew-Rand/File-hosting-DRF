JPG = 'image/jpeg'
PNG = 'image/png'
GIF = 'image/gif'
TIF = 'image/tiff'
SVG = 'image/svg+xml'
PDF = 'application/pdf'
DOC = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
XML = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
TXT = 'text/plain'

ALLOWED_FILETYPES = set(v for k, v in globals().items() if isinstance(v, str))
