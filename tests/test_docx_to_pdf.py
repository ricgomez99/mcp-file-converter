import tempfile
from pathlib import Path
import shutil
import pytest

from helpers import docx_to_pdf

@pytest.fixture
def source_file():
    return Path(__file__).parent / 'test_file.docx'

def test_docx_to_pdf(source_file):
    with tempfile.TemporaryDirectory() as temp_dir_path:
        temp_path = Path(temp_dir_path)
        input_file = temp_path / source_file.name

        shutil.copy(source_file, input_file)
        output_file = temp_path / 'test_file.pdf'

        result = docx_to_pdf(str(input_file), str(output_file))

        assert output_file.exists()
        assert output_file.stat().st_size > 0
        assert result.returncode == 0
