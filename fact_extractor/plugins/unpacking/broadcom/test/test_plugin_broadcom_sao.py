import os

from test.unit.unpacker.test_unpacker import TestUnpackerBase

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

class TestBroadcomSAOUnpacker(TestUnpackerBase):

    def test_unpacker_selection_generic(self):
        self.check_unpacker_selection('firmware/broadcom-sao', 'Broadcom SAO')

    def test_extraction(self):
        test_file_path = os.path.join(TEST_DATA_DIR, 'broadcom-sao.bin')
        extracted_files, meta_data = self.unpacker.extract_files_from_file(test_file_path, self.tmp_dir.name)

        assert meta_data['plugin_used'] == 'Broadcom SAO', 'wrong plugin applied'

        assert len(extracted_files) == 4, 'not all files extracted'
        assert all(element in ['META', 'DTBB', 'KRNL', 'RTFS'] for element in extracted_files), 'not all files extracted'
