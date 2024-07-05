# Amazing QR Code Generator

Welcome to the **Amazing QR Code Generator**! This web application allows you to create customized QR codes with ease. You can generate either colored QR codes or QR codes with an image background. 

## Features

- **Colored QR Code**: Create QR codes with your choice of colors for both the foreground and background.
- **Image QR Code**: Generate QR codes with a custom image background.
- **Download**: Download the generated QR code as a PNG file.

## How to Use

1. **Enter URL**: Provide the URL for which you want to generate the QR code.
2. **Choose QR Code Style**: Select between "Colored QR Code" and "Image QR Code".
    - **Colored QR Code**: Input the colors for the foreground and background.
    - **Image QR Code**: Upload an image to be used as the background.
3. **Generate QR Code**: Click the "Generate QR Code" button to create the QR code.
4. **View and Download**: The generated QR code will be displayed on the screen. You can download it by clicking the "Download QR Code" button.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/amazing-qrcode-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd amazing-qrcode-generator
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    streamlit run qrCodeApp.py
    ```

## Dependencies

- **streamlit**: For the web interface
- **segno**: For generating QR codes
- **Pillow (PIL)**: For image processing

Make sure to install the dependencies by running:
```bash
pip install streamlit segno pillow
```

## Credits

This project is made by **Vishu Vaishnav**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to fork this repository and customize it as per your needs. Contributions are welcome!

---


Enjoy generating amazing QR codes!

---

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![Made by Vishu Vaishnav](https://img.shields.io/badge/Made%20by-Vishu%20Vaishnav-blue?style=flat-square)](https://github.com/vishuvaishnav)
