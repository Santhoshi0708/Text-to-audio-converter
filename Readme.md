# Text-to-Audio Converter

Convert text to audio with ease using this simple web application built with Streamlit.

![Text-to-Audio Converter Demo](demo.gif)

## Features

- **Input Text**: Enter the text you want to convert to audio.
- **Language Selection**: Choose the language for the synthesized speech.
- **Convert to Audio**: Click the button to generate the audio from the input text.
- **Audio Player**: Listen to the generated audio directly in the browser.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Santhoshi0708/Text-to-audio-conveter
    ```

2. Install the streamlit libray:

    ```bash
    pip install streamlit
    ```
3. Install the library:
   
   ```bash
   pip install pyttsx3
   ```
4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```
5. Access the application in your browser at [http://localhost:8506/](http://localhost:8506/).

## Usage

1. Enter the text you want to convert to audio in the text area provided.
2. (Optional) Select the desired language for the synthesized speech from the dropdown menu.
3. Click the "Preview" button to generate the audio.
4. Listen to the synthesized audio using the audio player displayed below.

## Technologies Used

- [Streamlit](https://streamlit.io/): For building the interactive web application.
- [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/index.html): For text-to-speech synthesis.
- [Python](https://www.python.org/): Programming language used for development.

## Credits

This project utilizes the `pyttsx3` library for text-to-speech conversion. Special thanks to the developers and contributors of `pyttsx3` for their work.


