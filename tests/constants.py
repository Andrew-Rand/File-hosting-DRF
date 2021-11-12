# Test user register

TEST_USERNAME = 'test_username'
TEST_EMAIL = 'test_email@gmail.com'
TEST_PASSWORD = 'test_password'

TEST_USER_REGISTER_DATA = {'first_name': 'test_first_name',
                           'last_name': 'test_last_name',
                           'email': TEST_EMAIL,
                           'password': TEST_PASSWORD,
                           'username': TEST_USERNAME,
                           }

# test_with_filecreate

TEST_FILE_NAME = 'test_file'
TEST_FILE_TYPE = '.txt'
TEST_STORAGE_PATH = 'storage/permanent'
TEST_FILE_DATA = {'filename': TEST_FILE_NAME + TEST_FILE_TYPE,
                  'type': TEST_FILE_TYPE,
                  'total_size': 48
                  }

# test for chunks

TEST_CHUNK_PATH = 'storage/temp'
TEST_CHUNK_DIR = '148-test_chunktxt'
TEST_CHUNK_NAME = 'test_chunk.txt_part_1'
TEST_QUERYSET_FOR_BUILD = '?resumableChunkNumber=1&resumableChunkSize=52428800&resumableCurrentChunkSize=148&' \
                          'resumableTotalSize=148&resumableType=text%2Fplain&resumableIdentifier=148-test_chunktxt&' \
                          'resumableFilename=test_chunk.txt&resumableRelativePath=test_chunk.txt&resumableTotalChunks=1'


#  ===================FILE_UTILS_TESTS==================================================================================

# TestMakeChunksUtils:

TEST_CHUNK_TEMP_STORAGE_PATH = 'tes_storage'
TEST_CHUNK_USER_ID = '1111111111111'
TEST_CHUNK_DATA = {'identifier': 'test111',
                   'filename': 'test_file',
                   'total_chunk': 5}

MAKE_CHUNK_PATHS_RESULT = ['tes_storage/test_file_part_1',
                           'tes_storage/test_file_part_2',
                           'tes_storage/test_file_part_3',
                           'tes_storage/test_file_part_4',
                           'tes_storage/test_file_part_5']

CHUNK_NAME_RESULT = f'{TEST_CHUNK_DATA.get("filename")}_part_{TEST_CHUNK_DATA.get("total_chunk")}'

#  ===================SERIALIZER_TESTS======================================================================

TEST_NEW_PASSWORD = 'new_password'

TEST_CHANGE_PASSWORD_SERIALIZER_DATA_VALID = {
    'password': TEST_PASSWORD,
    'new_password': TEST_NEW_PASSWORD,
    'new_password_repeated': TEST_NEW_PASSWORD,
}

# ===================TEST_USER_CHANGE_VIEW=====================================================================

TEST_NEW_USER_DATA = {
    'email': 'new@mail.ru',
    'age': 50,
    'first_name': 'new_name',
    'last_name': 'new_l_name'
}
