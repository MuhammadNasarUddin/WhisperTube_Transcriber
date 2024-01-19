import streamlit as st
from whisper import dowload_youtube_video, transcribe_audio
import os



st.title("Youtube Video + OpenAI Whisper")
if st.text_input('Please Enter the access code') == os.environ['password']:
    print(os.environ['password'])

    user_input = st.text_input('Enter Your YouTube URL')

    with st.spinner('Sit back and relax. It takes a minute.'):
        if st.button('Transcribe'):
            if user_input:
                download_audio = dowload_youtube_video(user_input)
                st.write(transcribe_audio())
