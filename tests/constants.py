TEST_USERNAME = 'test_username'
TEST_EMAIL = 'test_email@gmail.com'
TEST_PASSWORD = 'test_password'

TEST_USER_REGISTER_DATA = {'first_name': 'test_first_name',
                           'last_name': 'test_last_name',
                           'email': TEST_EMAIL,
                           'password': TEST_PASSWORD,
                           'username': TEST_USERNAME,
                           }

TEST_FILE_NAME = 'test_file'
TEST_FILE_TYPE = '.txt'
TEST_STORAGE_PATH = 'storage/permanent'
TEST_FILE_DATA = {'filename': TEST_FILE_NAME + TEST_FILE_TYPE,
                  'type': TEST_FILE_TYPE,
                  'total_size': 48
                  }

TEST_CHUNK_PATH = 'storage/temp'
TEST_CHUNK_DIR = '148-test_chunktxt'
TEST_CHUNK_NAME = 'test_chunk.txt_part_1'
TEST_QUERYSET_FOR_BUILD = '?resumableChunkNumber=1&resumableChunkSize=52428800&resumableCurrentChunkSize=148&' \
                          'resumableTotalSize=148&resumableType=text%2Fplain&resumableIdentifier=148-test_chunktxt&' \
                          'resumableFilename=test_chunk.txt&resumableRelativePath=test_chunk.txt&resumableTotalChunks=1'
