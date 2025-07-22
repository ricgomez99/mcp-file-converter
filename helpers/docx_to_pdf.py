import pypandoc


def docx_to_pdf(input_file: str, output_file: str):
   return pypandoc.convert_file(input_file, 'pdf', outputfile=output_file)