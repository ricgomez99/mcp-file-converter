from helpers import Files_List

def main():
    print("Hello from mcp-file-converter!")
    list = Files_List()
    print(list.insert('file.pdf'))
    print(list.search_item('file.pdf'))


if __name__ == "__main__":
    main()
