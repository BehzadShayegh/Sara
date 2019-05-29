class bcolors:
# text style
    HEADER = '95'
    OKBLUE = '94'
    OKGREEN = '92'
    WARNING = '93'
    FAIL = '91'
    Noeffect = '0'
    Bold = '1'
    Underline = '2'
    Negative1 = '3'
    Negative2 = '5'
# text color
    Black = '30'
    Red = '31'
    Green = '32'
    Yellow = '33'
    Blue = '34'
    Purple = '35'
    Cyan = '36'
    White = '37'
# background color
    backBlack = '40'
    backRed = '41'
    backGreen = '42'
    backYellow = '43'
    backBlue = '44'
    backPurple = '45'
    backCyan = '46'
    backWhite = '47'

    def makeEffect(effects) :
        key = '\033['
        for effect in effects :
            key += effect + ';'
        return key[:-1]+'m'

class HandWriting :
    def saraSaid(self, text) :
        print(bcolors.makeEffect([bcolors.Green]) + text + bcolors.makeEffect([bcolors.Noeffect]))

    def clientSaid(self, text) :
        print(bcolors.makeEffect([bcolors.Red]) + text + bcolors.makeEffect([bcolors.Noeffect]))

    def specialLog(self, text) :
        print(bcolors.makeEffect([bcolors.Bold, bcolors.Underline, bcolors.OKGREEN]) + text + bcolors.makeEffect(bcolors.Noeffect))

    def normalLog(self, text) :
        print(text)

    def wating(self) :
        print('@', end = None)