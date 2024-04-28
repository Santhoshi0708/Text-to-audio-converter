import streamlit as st
from gtts import gTTS

def text_to_audio(text,audio_file):
    tts = gTTS(text)
    tts.save(audio_file)

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
