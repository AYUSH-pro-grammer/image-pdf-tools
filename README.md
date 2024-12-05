# Currently under Development
# Image and PDF Tools

This project provides a little set of tools for working with images and PDFs. The tools are built using Streamlit and include functionalities for converting images to PDF, merging multiple PDFs, and converting image formats.

URL:https://ayush-pro-grammer-image-pdf-tools-app-tioims.streamlit.app/

## Features

- **Image to PDF Converter**: Convert multiple images to a single PDF file with options to crop images and adjust their orientation.
- **Merge PDFs**: Merge multiple PDF files into a single PDF file.
- **Image Format Converter**: Convert images to different formats and download them as a zip file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AYUSH-pro-grammer/image-pdf-tools.git
    cd image-pdf-tools
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```
    or you can also use
   ```sh
    python -m streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` to access the tools.

## Tools

### Image to PDF Converter

- **Upload Images**: Upload one or more images in various formats (jpg, jpeg, png, webp, bmp, gif, tiff, ico, svg, heif).
- **Crop Images**: Optionally crop the images before converting them to PDF.
- **Convert to PDF**: Convert the uploaded (and optionally cropped) images to a single PDF file.
- **Download PDF**: Download the generated PDF file.

### Merge PDFs

- **Upload PDFs**: Upload multiple PDF files.
- **Merge PDFs**: Merge the uploaded PDF files into a single PDF file.
- **Download Merged PDF**: Download the merged PDF file.

### Image Format Converter

- **Upload Images**: Upload multiple images in various formats.
- **Select Output Format**: Choose the desired output format for the images.
- **Convert Images**: Convert the uploaded images to the selected format.
- **Download Converted Images**: Download the converted images as a zip file.

## File Structure

- `app.py`: Main entry point for the Streamlit app.
- `pages/`: Directory containing the individual tool pages.
  - `image_to_pdf.py`: Code for the Image to PDF Converter tool.
  - `merge_page.py`: Code for the Merge PDFs tool.
  - `image_formatter.py`: Code for the Image Format Converter tool.
- `requirements.txt`: List of required Python packages.

## Dependencies

- Streamlit
- Pillow
- fpdf
- PyPDF2
- streamlit-cropper

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pillow](https://python-pillow.org/)
- [fpdf](http://www.fpdf.org/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- [streamlit-cropper](https://github.com/turner-anderson/streamlit-cropper)
