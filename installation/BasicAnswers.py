from gtts import gTTS
import os

tts = gTTS(text='I can not undestand sir!', lang='en')
tts.save("./Voices/ICanNotUnderstandSir.mp3")

tts = gTTS(text='I didn\'t hear any thing sir!', lang='en')
tts.save("./Voices/IDidntHearAnyThingSir.mp3")

tts = gTTS(text='Yes sir!', lang='en')
tts.save("./Voices/YesSir.mp3")

tts = gTTS(text='Okay sir!', lang='en')
tts.save("./Voices/OkaySir.mp3")

tts = gTTS(text='Welcome your highness.', lang='en')
tts.save("./Voices/WelcomeYourHighness.mp3")

tts = gTTS(text='Have fun your highness... shut down!', lang='en-US')
tts.save("./Voices/ShutDown.mp3")

tts = gTTS(text='Good bye Mr!', lang='en-US')
tts.save("./Voices/GoodByeMr.mp3")

tts = gTTS(text='Are you sure Mr. Shayegh?', lang='en-US')
tts.save("./Voices/GetPassword.mp3")

tts = gTTS(text='Job done sir.', lang='en-US')
tts.save("./Voices/JobDoneSir.mp3")

tts = gTTS(text='write your linux bash command', lang='en')
tts.save("./Voices/WriteLinuxBashCommand.mp3")

tts = gTTS(text='write a english label for that', lang='en')
tts.save("./Voices/WriteEnglishLabel.mp3")

tts = gTTS(text='write your persian key word \
    and last part of that in new line after that', lang='en')
tts.save("./Voices/WritePersianKeyWord.mp3")

tts = gTTS(text='I am listening sir.', lang='en')
tts.save("./Voices/ImListeningSir.mp3")

os.system("cp ./installation/Ready ./Voices/Ready.mp3")
os.system("cp ./installation/Capture ./Voices/Capture.mp3")

tts = gTTS(text='Welcome your highness. My name is sara. Call me whenever you need. I\'m listening for a command!', lang='en')
tts.save("./Voices/introduction.mp3")