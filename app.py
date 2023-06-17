import streamlit as st
import openai
from gtts import gTTS
from io import BytesIO
import tempfile

behave_like = "You are a medical and healthcare expert that specializes in medicines and disease diagnostic."
MODEL = "gpt-3.5-turbo"
openai.api_key = <API-KEY>


st.markdown("<h1 style='text-align: center; color: blue;'>Healthcare Pro</h1>", unsafe_allow_html=True)

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_file = tempfile.NamedTemporaryFile(delete=False)
    tts.save(audio_file.name)
    with open(audio_file.name, 'rb') as f:
        audio = BytesIO(f.read())
    return audio

def CustomChatGPT(user_input):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": behave_like},
            {"role": "user", "content": user_input},
        ],
        temperature=0,
    )
    disease = response['choices'][0]['message']['content']
    return disease

def main():
    user_input = st.text_input("Enter your message")
    if st.button("Submit"):
        disease = CustomChatGPT(user_input)
        st.write("Response:", disease)
        audio = text_to_speech(disease)
        st.audio(audio.read(), format='audio/mp3', start_time=0)
        
    gif_url = "doc.jpg"  # Replace with your GIF URL
    st.image(gif_url, use_column_width=True)


if __name__ == "__main__":
    main()