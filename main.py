import fitz  # PyMuPDF
import os

pdf_path = r"D:\input_pdf.pdf"
output_folder = 'output_images'
max_size_kb = 1000  # Maximum file size in KB

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the PDF
doc = fitz.open(pdf_path)

# Loop through each page
for i, page in enumerate(doc):
    # Render page to image
    pix = page.get_pixmap(dpi=200)  # Higher DPI = better quality

    # Initial save
    output_path = os.path.join(output_folder, f'page_{i+1}.jpg')
    pix.save(output_path, jpg_quality=95)

    # Compress if needed
    quality = 95
    while os.path.getsize(output_path) > max_size_kb * 1024 and quality > 10:
        quality -= 5
        pix.save(output_path, jpg_quality=quality)

    #  Status update
    final_size = os.path.getsize(output_path) // 1024
    print(f"Saved: {output_path} ({final_size} KB, quality={quality})")

print(" Conversion complete!")
