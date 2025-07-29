from helpers import FilesList, docx_to_pdf


class ConvertToPdf(FilesList):

    def convert_to_pdf(self):
        output_file_name = ''
        head = self.head

        while head is not None:
            output_file_name = head.data.replace('.pdf', '.docx')
            docx_to_pdf(head.data, output_file_name)

            head = head.next