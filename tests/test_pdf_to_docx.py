from helpers import pdf_to_docx
import tempfile
from pathlib import Path
import shutil

def test_pdf_to_docx() :
    with tempfile.TemporaryDirectory() as temp_dir_path :
        temp_dir = Path(temp_dir_path)
        source_docx_fixture = Path(__file__).parent / 'test_document.pdf'
        input_temp_file = temp_dir / source_docx_fixture.name
      
        shutil.copy(source_docx_fixture, input_temp_file)
        output_file = temp_dir / 'converted_document.docx'

        result = pdf_to_docx(str(input_temp_file), str(output_file))

        assert output_file.exists()
        assert output_file.stat().st_size > 0
        assert result == None



    