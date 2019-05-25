import pyjokes
from gtts import gTTS

def tellJoke() :
    text = pyjokes.get_joke()
    tts = gTTS(text=text, lang='en-US')
    tts.save("./Voices/joke.mp3")
    os.system("mpg123 ./Voices/joke.mp3")
    print("\n\n\n:DD :DD :DD :DD :DD :DD :DD :DD :DD")
    print(text)
    print(":DD :DD :DD :DD :DD :DD :DD :DD :DD\n\n\n")
    os.system("rm ./Voices/joke.mp3")