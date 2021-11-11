from src.fileservice.utils import make_chunk_dir_path, make_chunk_paths, get_chunk_name

from tests.constants import TEST_CHUNK_TEMP_STORAGE_PATH, TEST_CHUNK_USER_ID, TEST_CHUNK_DATA,\
    MAKE_CHUNK_PATHS_RESULT, CHUNK_NAME_RESULT


class TestChunksUtils:

    def test_make_chunk_dir_path(self) -> None:
        assert make_chunk_dir_path(temp_storage_path=TEST_CHUNK_TEMP_STORAGE_PATH,
                                   user_id=TEST_CHUNK_USER_ID,
                                   data=TEST_CHUNK_DATA) == f'{TEST_CHUNK_TEMP_STORAGE_PATH}/{TEST_CHUNK_USER_ID}/' \
                                                            f'{TEST_CHUNK_DATA.get("identifier")}'

    def test_make_chunk_paths(self) -> None:
        assert make_chunk_paths(chunks_dir_path=TEST_CHUNK_TEMP_STORAGE_PATH,
                                data=TEST_CHUNK_DATA) == MAKE_CHUNK_PATHS_RESULT

    def test_get_chunk_name(self) -> None:
        assert get_chunk_name(uploaded_filename=TEST_CHUNK_DATA.get('filename'),
                              chunk_number=TEST_CHUNK_DATA.get('total_chunk')) == CHUNK_NAME_RESULT
