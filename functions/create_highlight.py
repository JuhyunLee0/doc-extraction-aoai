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

    
# Function to highlight text in IMG with a red box
def highlight_img(file_path, highlight_coords):
    # Open the PNG image
    image = Image.open(file_path)
    
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # Iterate over the highlight coordinates
    for highlight in highlight_coords:
        polygon = highlight['polygon']
        
        # Convert polygon to rectangle
        x0, y0, x1, y1 = polygon[0], polygon[1], polygon[4], polygon[5]
        
        # Draw a rectangle with a semi-transparent fill
        draw.rectangle([x0, y0, x1, y1], outline="red", width=4)
    
    # get file type from the file path
    file_type = file_path.split(".")[-1]

    output_png_path = os.path.join(os.getcwd(), "documents", f"temp.{file_type}")
    image.save(output_png_path)
    return output_png_path
