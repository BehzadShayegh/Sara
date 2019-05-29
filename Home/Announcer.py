from gtts import gTTS
import os
from Home.Writer import HandWriting

handwriting = HandWriting()
MEDIA_PLAYER = 'mpg123'

class Lips :
    ready = './Voices/Ready.mp3'
    capture = './Voices/Capture.mp3'
    welcome = './Voices/WelcomeYourHighness.mp3'
    yes = './Voices/YesSir.mp3'
    ok = './Voices/OkaySir.mp3'
    jobDone = './Voices/JobDoneSir.mp3'
    notUnderStand = './Voices/ICanNotUnderstandSir.mp3'
    didntHear = './Voices/IDidntHearAnyThingSir.mp3'
    listenning = './Voices/ImListeningSir.mp3'
    getPass = './Voices/GetPassword.mp3'
    writeLinuxCom = './Voices/WriteLinuxBashCommand.mp3'
    writeEnLabel = './Voices/WriteEnglishLabel.mp3'
    writePesianKey = './Voices/WritePersianKeyWord.mp3'
    lastWord = './Voices/last_word.mp3'
    shutdown = './Voices/ShutDown.mp3'
    goodbye = './Voices/GoodByeMr.mp3'

    def ready_(self) :
        os.system(MEDIA_PLAYER+' '+self.ready)
    def capture_(self) :
        os.system(MEDIA_PLAYER+' '+self.capture)
    def welcome_(self) :
        os.system(MEDIA_PLAYER+' '+self.welcome)
        handwriting.saraSaid('Welcome your highness.')
    def yes_(self) :
        os.system(MEDIA_PLAYER+' '+self.yes)
        handwriting.saraSaid('Yes sir.')
    def ok_(self) :
        os.system(MEDIA_PLAYER+' '+self.ok)
        handwriting.saraSaid('Okay sir.')
    def jobDone_(self) :
        os.system(MEDIA_PLAYER+' '+self.jobDone)
        handwriting.saraSaid('Job done sir.')
    def notUnderStand_(self) :
        os.system(MEDIA_PLAYER+' '+self.notUnderStand)
        handwriting.saraSaid('I can not understand sir.')
    def goodbye_(self) :
        os.system(MEDIA_PLAYER+' '+self.goodbye)

    def makeSound(self, message) :
        tts = gTTS(text=message, lang='en')
        tts.save("./Voices/last_word.mp3")

    def removeLastWord(self) :
        os.system("rm "+self.lastWord)

    def say(self, message) :
        print(message[-4:])
        if message[-4:] == '.mp3' :
            os.system(MEDIA_PLAYER+' '+message)
            handwriting.saraSaid(message[9:-4])
        else :
            self.makeSound(message)
            self.say(self.lastWord)
            handwriting.saraSaid(message)
            self.removeLastWord()