# PDF to Compressed Image Converter
This Python script converts each page of a PDF file into a high-quality JPEG image, while ensuring the output images 
stay within a specified file size limit. It's built using PyMuPDF (fitz).

🚀 Features
- Converts every page of a PDF into a .jpg image
- Automatically compresses images to stay under a user-defined size (in KB)
- Adjustable DPI and JPEG quality settings
- Saves output images to a dedicated folder

🛠️ Requirements
- Python 3.x
- PyMuPDF


📦 Usage
Update the following variables in the 'main' script:
- pdf_path = r"D:\input_pdf.pdf"       # Path to your PDF file
- output_folder = 'output_images'      # Folder to save images
- max_size_kb = 1000                   # Max image size in KB

📁 Output
- Images are named as page_1.jpg, page_2.jpg, etc.
- Compression is applied dynamically to meet the size constraint
- Terminal output shows final size and quality used for each image

🧠 Notes
- Higher DPI improves image quality but increases file size
- Compression loop reduces quality in steps until the image meets the size limit
- Minimum JPEG quality is capped at 10 to avoid excessive degradation
