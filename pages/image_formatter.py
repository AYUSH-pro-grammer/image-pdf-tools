import streamlit as st
from PIL import Image
import io
import zipfile
import os

# Function to convert a single image
def convert_image(image, output_format):
    img = Image.open(image)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format=output_format)
    img_byte_arr.seek(0)
    return img_byte_arr

# Function to convert multiple images and save them in a zip file
def convert_images_bulk(uploaded_files, output_format):
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format=output_format)
            img_byte_arr.seek(0)
            
            # Add each converted image to the zip file
            file_name = os.path.splitext(uploaded_file.name)[0] + f".{output_format.lower()}"
            zip_file.writestr(file_name, img_byte_arr.read())
    
    zip_buffer.seek(0)
    return zip_buffer

# Image Format Converter Tool (with Bulk Upload)
def image_format_converter():
    st.title("Image Format Converter (Bulk)")

    # Upload multiple images
    uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png", "webp", "bmp", "gif", "tiff", "ico", "svg", "heif"], accept_multiple_files=True)

    if uploaded_files:
        st.write(f"{len(uploaded_files)} files uploaded")
        # Display thumbnails of uploaded images
        for uploaded_file in uploaded_files:
            st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)

        # Dropdown for output format selection
        st.write("### Choose the output format")
        output_format = st.selectbox(
            "Select Output Format", ["JPEG", "PNG", "WEBP", "BMP", "GIF", "TIFF", "ICO", "SVG", "HEIF"]
        )

        # Convert button
        if st.button("Convert Images"):
            with st.spinner("Converting images..."):
                converted_zip = convert_images_bulk(uploaded_files, output_format)
                # Allow user to download the converted images as a zip
                st.download_button(
                    label=f"Download All {output_format} images",
                    data=converted_zip,
                    file_name=f"converted_images.{output_format.lower()}.zip",
                    mime="application/zip"
                )

# Streamlit App
def app():
    image_format_converter()

if __name__ == "__main__":
    app()
