import streamlit as st

def home():
    st.title("Welcome to Image and PDF Tools")
    
    # Display as cards
    st.write("### Tools:")
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Image Format Converter"):
            st.session_state.page = "image-formatter"

    with col2:
        if st.button("Image to PDF"):
            st.session_state.page = "image-to-pdf"

if __name__ == "__main__":
    home()
