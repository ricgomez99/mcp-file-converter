from pdf2docx import Converter

def pdf_to_docx(input_files: str, output_file: str) :
    file_path = Converter(input_files)
    convert_file = file_path.convert(output_file, start=0, end=None)
    file_path.close()
    print('file: ', convert_file)
    return convert_file