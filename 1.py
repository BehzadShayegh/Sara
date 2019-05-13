import speech_recognition as sr

r = sr.Recognizer()
choice = len(sr.Microphone.list_microphone_names()) - 1
mic = sr.Microphone(device_index = choice)

with mic as source:
    audio = r.listen(source)

r.recognize_google(audio)