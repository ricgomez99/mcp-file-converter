from helpers import ConvertToPdf

def docx_to_pdf_tool(path: str, files: list[str]):
    converter = ConvertToPdf()
    elements = []
    message = ''

    if not path:
        raise ValueError('Unable to process files convertion')
    
    if not len(files):
        raise ValueError('Please select the files to convert')
    
    for item in files:
        converter.insert(item)

    converter.convert_to_pdf()
    elements = converter.print_items()
    message = "Converted the following files: " + ",".join(elements)

    return message