ARCHIVE_TYPE = 'zip'

NGINX_TEMP_STORAGE_PATH = 'media/temp/'
NGINX_PERMANENT_STORAGE_PATH = 'media/permanent/'

FILE_TEMPLATE_URL_NAME = 'api_file_upload'
FILE_CHUNK_UPLOAD_URL_NAME = 'chunk_upload'
FILE_BUILD_URL_NAME = 'file_build'
FILE_UPLOAD_URL_NAME = 'file_upload'
FILE_DOWNLOAD_URL_NAME = 'file_download'
FILE_DOWNLOAD_ALL_URL_NAME = 'download_all_file_as_zip'
FILE_ALL_USER_FILES_URL_NAME = 'all_user_files'
FILE_DETAIL_URL_NAME = 'file_detail'

PAGE_SIZE = 5
MAX_PAGE_SIZE = 1000
ORDERING_FILED = ('date_modified', 'name')

LARGE_FILE_LIMIT_SIZE = 128 * 1024 * 1024
LARGE_HASH_PART_1 = 100 * 1024 * 1024
LARGE_HASH_PART_2 = -2 * 1024 * 1024

STD_TUMBS = {
    'application/pdf': 'src/fileservice/std_tumbs/pdf.png',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'src/fileservice/std_tumbs/doc.png',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'src/fileservice/std_tumbs/excel.png',
    'text/plain': 'src/fileservice/std_tumbs/txt.png'
}
ERROR_THUMB = 'src/fileservice/std_tumbs/error.png'
