import streamlit as st
import segno
import os
import io
from PIL import Image

def qrCodeGenerator(url, choice, color1 = "#fafafa", color2 = "#080808"):
    qrcode = segno.make_qr(url)
    img_buffer = io.BytesIO()
    
    if choice == 'Colored QR Code':
        qrcode.save(
            img_buffer,
            kind='png',
            scale=5,
            light=color1,
            dark=color2,
            #data_dark="#19255c",
        ) 
    else:
        qrcode.to_artistic(
            background=background_image,
            target=img_buffer,
            scale=8,
            dark="black",
            kind='png',
        )   
    img_buffer.seek(0)
    return img_buffer

if __name__ == "__main__":

    st.title("Amazing QR Code Generator")
    url = st.text_input("Enter URL")
    choice = st.selectbox("Choose QR Code Style", ["Colored QR Code", "Image QR Code"])
    
    background_image = None
    if choice == "Image QR Code":
        background_image = st.file_uploader("Upload an image for the background", type=["jpg", "jpeg", "png"])
    else:
        color1 = st.text_input("Enter color1")
        color2 = st.text_input("Enter color2")
    if st.button("Generate QR Code"):
        if url and background_image:
            img_buffer = qrCodeGenerator(url, choice)        
            image = Image.open(img_buffer)
            st.image(image, caption=f'QR Code for {url}')
            st.download_button(
                label="Download QR Code",
                data=img_buffer,
                file_name=f"{choice.replace(' ', '_').lower()}_qr_code.png",
                mime="image/png"
            )
        elif url:
            img_buffer = qrCodeGenerator(url, choice, color1, color2)
            image = Image.open(img_buffer)
            st.image(image, caption=f'Your QR-Code for {url}')
            st.download_button(
                label="Download QR-Code",
                data=img_buffer,
                file_name=f"{choice.replace(' ', '_').lower()}_qr_code.png",
                mime="image/png"
            )
        else:
            st.error("Please enter both URL and file name.")
