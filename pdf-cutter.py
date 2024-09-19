import pypdf
import os

def extract_first_two_pages(input_pdf_path, output_pdf_path):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = pypdf.PdfReader(input_pdf_file)
        
        # Create a PDF writer object
        writer = pypdf.PdfWriter()
        
        # Add the first two pages to the writer object
        for page_num in range(min(2, len(reader.pages))):
            writer.add_page(reader.pages[page_num])
        
        # Write the output PDF file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

# Example usage
input_pdf_path = os.path.join(os.getcwd(), "documents", "Zurich-Quote-Teachers.pdf")
output_pdf_path = os.path.join(os.getcwd(), "documents", "Zurich-Quote-Teachers page 1-2.pdf")
extract_first_two_pages(input_pdf_path, output_pdf_path)