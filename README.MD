# SteganographyApp

SteganographyApp is a simple application built using Tkinter and Python that allows users to hide and reveal messages in images using steganography techniques.

## Features

- Select an image file (PNG or JPG) to work with.
- Display the selected image.
- Enter a message to hide within the image.
- Encode the message into the image using LSB steganography.
- Save the modified image with the hidden message.
- Decode and reveal the hidden message from a previously encoded image.

## Prerequisites

- Python 3.6 or higher
- Tkinter library
- PIL (Python Imaging Library) library
- stegano library

## Installation

1. Clone the repository:

   git clone https://github.com/chamuidtha00/SteganographyApp.git

2. install the required dependencies

    pip install -r

3. Run the application

    python main.py

## Usage
   * Select an image file by clicking the "Select Image" button.

   * Enter the message to be hidden in the text box.

   * Click the "Encode" button to hide the message within the image.

   * Optionally, click the "Save Image" button to save the modified image with the hidden message.

   * To reveal the hidden message, click the "Decode" button.

   * The revealed message will be displayed in the text box.

