from pdf2docx import Converter

def pdf_to_docx(input_files: str, output_file: str) :
    file_path = Converter(input_files)
    convert_file = file_path.convert(output_file, start=0)
    file_path.close()
    
    return convert_file