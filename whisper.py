def dowload_youtube_video(url):
    from pytube import YouTube
    yt = YouTube(url)
    global audio_stream
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    audio_stream.download()
    return 'download successfully'


def transcribe_audio():
    import openai
    from openai import OpenAI
    import os
    client = OpenAI(api_key=os.environ['openai_api_key']) 
    file = open(audio_stream.default_filename, "rb")
    transcription = client.audio.transcriptions.create(model="whisper-1", file=file, response_format='text', language='ur')
    
    return transcription