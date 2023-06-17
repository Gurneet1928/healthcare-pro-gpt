import streamlit as st
import openai
from gtts import gTTS
from io import BytesIO
import tempfile

behave_like = "You are a medical and healthcare expert that specializes in medicines and disease diagnostic."
MODEL = "gpt-3.5-turbo"


st.markdown("<h1 style='text-align: center; color: cream;'> >> Healthcare Pro << </h1> <br> <h3 style='text-align:center;color:cream;'> >> By Team Tru << </h3>", unsafe_allow_html=True)

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_file = tempfile.NamedTemporaryFile(delete=False)
    tts.save(audio_file.name)
    with open(audio_file.name, 'rb') as f:
        audio = BytesIO(f.read())
    return audio

def CustomChatGPT(user_input,days_since_feeling):
    input_values = [user_input+"Feeling since " + str(days_since_feeling) + "What is the possible disease ? [A few possible names only]" ,
                    user_input+"Feeling since " + str(days_since_feeling) + "What are some possible instant medications ? [A few medications list only] ",
                   user_input+"Feeling since " + str(days_since_feeling) + "What are some other symptoms ? 6 possible symptoms"]
    response_disease = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": behave_like},
            {"role": "user", "content": input_values[0]},
            ],
            temperature=0.5,
            max_tokens = 50
        )
    
    response_medic = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": behave_like},
            {"role": "user", "content": input_values[1]},
            ],
            temperature=0.5,
            max_tokens = 150
        )
    response_symp = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": behave_like},
            {"role": "user", "content": input_values[2]},
            ],
            temperature=0.5,
            max_tokens = 50
        )
    disease = response_disease['choices'][0]['message']['content']
    medics = response_medic['choices'][0]['message']['content']
    symps = response_symp['choices'][0]['message']['content']
    return disease,medics,symps

def main():
    user_input = st.text_input("Enter your condition")
    days_since_feeling = st.slider("How many days since you are feeling ?",0,10,1)
    if st.button("Submit"):
        disease,medics,symps = CustomChatGPT(user_input,days_since_feeling)
        st.write("Possible Disease: ")
        st.write(disease)
        st.write("Possible Medications: ")
        st.write(medics)
        st.write("Other symptoms: ")
        st.write(symps)
        audio = text_to_speech(disease)
        st.audio(audio.read(), format='audio/mp3', start_time=0)
        
    gif_url = "doc.jpeg"  # Replace with your GIF URL
    st.image(gif_url, width=300)


if __name__ == "__main__":
    main()