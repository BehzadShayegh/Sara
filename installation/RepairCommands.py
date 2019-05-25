import csv

possibleCommands = [\
    ['sara', 'سارا', 'ارا'],\
    ['label', 'command', 'lastPart'],\
    ['finish', 'پایان', 'یان'],\
    ['finish', 'هیچی', 'چی'],\
    ['finish', 'کافی', 'فیه'],\
    ['finish', 'بس است', 'بسه'],\
    ['finish', 'بی خیال', 'خیال'],\
    ['shutdown', 'لپتاپ', 'تاپ'],\
    ['shutdown', 'خاموش', 'موش'],\
    ['joke', 'جوک', 'جوک'],\
    ['joke', 'لطیفه', 'تیف'],\
    ['add command', 'جدید', 'دید'],\
    ]

CommandLabels = './Memorry/CommandLabels.csv'
with open(CommandLabels, 'w') as commandsCsv:
    for command in possibleCommands:
        commandsCsv.write("%s,%s,%s\n"%(command[0],command[1],command[2]))

PersonalCommands = './Memorry/PersonalCommands.csv'
with open(PersonalCommands, 'w') as CommandsCsv:
    CommandsCsv.write("%s,%s\n"%('label','command'))

# update github,به روز رسانی شو,روز
# VS Code,برنامه نویسی,نویس

# update github,./LinuxCommand/Shells/updateGithub.sh
# VS Code,code ~/Desktop/GitHub/