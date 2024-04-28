import streamlit as st
import pyttsx3

def text_to_audio(text,audio_file):
    speech=pyttsx3.init()
    speech.save_to_file(text,audio_file)
    speech.runAndWait()

# Main function
def main():
    # Title of the web app
    st.title('Text to Audio Converter')

    # File uploader widget
    uploaded_file = st.text_area("Upload a text")

    if uploaded_file is not None:
        if st.button("Preview"):
            audio_file = "Output.mp3"
            text_to_audio(uploaded_file,audio_file)
           # Offer download link for converted audio
            st.audio(audio_file, format='audio/mp3')

# Run the main function
if __name__ == "__main__":
    main()
