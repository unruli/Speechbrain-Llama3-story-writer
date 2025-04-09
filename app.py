import ollama
import streamlit as st
from audiorecorder import audiorecorder
from speechbrain.inference import EncoderDecoderASR

st.title('SpeechBrain - Speech to Text')


def generateStoryFrom(question):
    response = ollama.chat(model="llama3", messages=[
        {
            'role': 'system',
            'content': 'You are best story writer and you can write a brief story from the question given by user.'
        },
        {
            'role': 'user',
            'content': question
        }
    ])

    return response['message']['content']


def convertSpeechToText():
    asr_model = EncoderDecoderASR.from_hparams(
        source="speechbrain/asr-conformer-transformerlm-librispeech", savedir="pretrained_models/asr-transformer-transformerlm-librispeech")
    text = asr_model.transcribe_file("audio.wav")
    return text


audio = audiorecorder("Record")

if len(audio) > 0:
    st.audio(audio.export().read(), autoplay=True)
    audio.export("audio.wav", format="wav")
    transcript = convertSpeechToText()
    st.markdown(transcript)
    story = generateStoryFrom(transcript)
    st.markdown(story)
