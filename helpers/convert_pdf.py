from helpers import FilesList, pdf_to_docx

class ConvertPdf(FilesList):

    def convert(self):
        output_file_name = ''
        head = self.head

        while head is not None:
            output_file_name = head.data.replace('.pdf', '.docx')
            pdf_to_docx(head.data, output_file_name)

            head = head.next

