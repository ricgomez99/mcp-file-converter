
from typing import Any
from mcp.server.fastmcp import FastMCP
from helpers import ConvertPdf

# Initialize Server
mcp = FastMCP('file_converter')

@mcp.tool()
def convert_to_docx(file_path: str, files: list[str]):
    """Tool that converts any pdf files into docx format"""
    if not file_path:
        raise ValueError('Unable to process files convertion')
    
    if not len(files):
        raise ValueError('Please select the files to convert')
    
    converter = ConvertPdf()
    for item in files:
        converter.insert(item)

    converter.convert()
    elements = converter.print_items()

    return "Converted the following files: " + ",".join(elements)

# Run server
if __name__ == "__main__":
    mcp.run(transport='stdio')
