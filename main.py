
from typing import Any
from mcp.server.fastmcp import FastMCP
from tools import pdf_to_docx_tool

# Initialize Server
mcp = FastMCP('file_converter')

@mcp.tool()
def convert_to_docx(file_path: str, files: list[str]):
    """Tool that converts any pdf files into docx format"""
    pdf_to_docx_tool(file_path, files)

# Run server
if __name__ == "__main__":
    mcp.run(transport='stdio')
