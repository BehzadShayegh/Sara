import csv

CommandLabels = 'CommandLabels.csv'
possibleCommands = [\
    ['label', 'command', 'lastPart'],\
    ['finish', 'پایان', 'یان'],\
    ['finish', 'هیچی', 'چی'],\
    ['finish', 'کافی', 'فیه'],\
    ['finish', 'بس است', 'بسه'],\
    ['finish', 'بی خیال', 'خیال'],\
    ['add', 'جدید', 'دید'],\
    ]

with open(CommandLabels, 'w') as commandsCsv:
    for command in possibleCommands:
        commandsCsv.write("%s,%s,%s\n"%(command[0],command[1],command[2]))