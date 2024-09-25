import os
import fitz  # PyMuPDF
from PIL import Image, ImageDraw

# Function to highlight text in PDF with a red box
def highlight_pdf(file_path, target_text):
    doc = fitz.open(file_path)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_instances = page.search_for(target_text)
        
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)
            highlight.set_colors(stroke=(1, 0, 0))  # Red color
            highlight.update()
    
    output_path = os.path.splitext(file_path)[0] + "_highlighted.pdf"
    doc.save(output_path)
    doc.close()
    return output_path
