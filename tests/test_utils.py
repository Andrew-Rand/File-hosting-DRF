from src.fileservice.utils import make_chunk_dir_path, make_chunk_paths, get_chunk_name


class TestChunksUtils:

    TEST_CHUNK_TEMP_STORAGE_PATH = 'tes_storage'
    TEST_CHUNK_USER_ID = '1111111111111'
    TEST_CHUNK_DATA = {
        'identifier': 'test111',
        'filename': 'test_file',
        'total_chunk': 5}
    CHUNK_PATHS_RESULT = [
        'tes_storage/test_file_part_1',
        'tes_storage/test_file_part_2',
        'tes_storage/test_file_part_3',
        'tes_storage/test_file_part_4',
        'tes_storage/test_file_part_5']
    NAME_RESULT = f'{TEST_CHUNK_DATA.get("filename")}_part_{TEST_CHUNK_DATA.get("total_chunk")}'

    total_chunk = 5

    def test_make_chunk_dir_path(self) -> None:
        assert make_chunk_dir_path(
            temp_storage_path=self.TEST_CHUNK_TEMP_STORAGE_PATH,
            user_id=self.TEST_CHUNK_USER_ID,
            data=self.TEST_CHUNK_DATA) == f'{self.TEST_CHUNK_TEMP_STORAGE_PATH}/{self.TEST_CHUNK_USER_ID}/{self.TEST_CHUNK_DATA.get("identifier")}'

    def test_make_chunk_paths(self) -> None:
        assert make_chunk_paths(
            chunks_dir_path=self.TEST_CHUNK_TEMP_STORAGE_PATH,
            data=self.TEST_CHUNK_DATA) == self.CHUNK_PATHS_RESULT

    def test_get_chunk_name(self) -> None:
        assert get_chunk_name(
            uploaded_filename=str(self.TEST_CHUNK_DATA.get('filename')),
            chunk_number=self.total_chunk) == self.NAME_RESULT
