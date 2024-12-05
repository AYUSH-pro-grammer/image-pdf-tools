import streamlit as st
from PIL import Image
from fpdf import FPDF
import io
import os
from streamlit_cropper import st_cropper  # Import the st_cropper function

# Function to convert images to PDF
def images_to_pdf(images, orientations):
    pdf = FPDF()

    # Temporary folder to store images
    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)

    for i, (img, orientation) in enumerate(zip(images, orientations)):
        pdf.add_page(orientation=orientation)
        temp_image_path = os.path.join(temp_dir, f"temp_image_{i}.png")
        img.save(temp_image_path, format='PNG')  # Save image in PNG format
        pdf.image(temp_image_path, x=10, y=10, w=190)  # Adjust x, y, w to your needs

    # Save the PDF to a temporary file
    temp_pdf_path = "temp_output.pdf"
    pdf.output(temp_pdf_path)  # Save the PDF to a file

    # Read the generated PDF into memory
    with open(temp_pdf_path, "rb") as pdf_file:
        pdf_data = pdf_file.read()

    # Clean up the temporary directory and file
    for file_name in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, file_name)
        os.remove(file_path)
    os.rmdir(temp_dir)
    os.remove(temp_pdf_path)  # Remove the generated PDF file

    # Return the PDF data as a byte stream
    return io.BytesIO(pdf_data)

# Image to PDF Converter Tool
def image_to_pdf_converter():
    st.title("Image to PDF Converter")

    # Upload one or more images
    uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png", "webp", "bmp", "gif", "tiff", "ico", "svg", "heif"], accept_multiple_files=True)

    if uploaded_files:
        st.write(f"{len(uploaded_files)} files uploaded")

        cropped_images = []
        orientations = []

        # Display thumbnails of uploaded images
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            width, height = img.size

            # Determine orientation
            if width > height:
                orientation = 'L'
            else:
                orientation = 'P'
            orientations.append(orientation)

            # Display image with cropping option
            st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)
            if st.checkbox(f"Crop {uploaded_file.name}"):
                cropped_img = st_cropper(img, realtime_update=True, box_color='#0000FF')
                cropped_images.append(cropped_img)
            else:
                cropped_images.append(img)

        if st.button("Convert to PDF"):
            with st.spinner("Converting images to PDF..."):
                pdf_data = images_to_pdf(cropped_images, orientations)

                # Provide a download button for the PDF
                st.download_button(
                    label="Download PDF",
                    data=pdf_data.getvalue(),  # Use getvalue() to get the bytes data
                    file_name="converted_images.pdf",
                    mime="application/pdf"
                )

# Streamlit App
def app():
    image_to_pdf_converter()

if __name__ == "__main__":
    app()
