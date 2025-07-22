from helpers import ConvertPdf


def pdf_to_docx_tool(path: str, files: list[str]):
    converter = ConvertPdf()
    elements = []
    message = ''

    if not path:
        raise ValueError('Unable to process files convertion')
    
    if not len(files):
        raise ValueError('Please select the files to convert')
    
    for item in files:
        converter.insert(item)

    converter.convert()
    elements = converter.print_items()
    message = "Converted the following files: " + ",".join(elements)

    return message