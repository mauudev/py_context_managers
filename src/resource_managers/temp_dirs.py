import shutil
import tempfile


class TempDirectory:
    def __enter__(self):
        self.temp_dir = tempfile.mkdtemp()
        return self.temp_dir  # This value will be assigned to the variable after 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.temp_dir)
