#!/usr/bin/env python
import argparse, csv

parser = argparse.ArgumentParser(description='Convert midi files to beep tunes')
parser.add_argument('-f', type=str, help='a filepath to the midi you want played')
parser.add_argument('-l', type=str, help='the length of the midi you would like translated to beep')
# Need an arguement to supress beep
# Need an arguement to print to console
args = parser.parse_args()
speedAdjust = 1
tempoMultiplier = 1
tempo = 571429
track = 2

def getDuration(row, noteStart):
    global tempoMultiplier
    d = int((int(row[1].strip()) - noteStart)*tempoMultiplier * speedAdjust/40)
    if d == 0: d = 1
    return str(d)

def getSleep(row, pauseStart):
    global tempoMultiplier
    return int((int(row[1].strip()) - pauseStart)* tempoMultiplier * speedAdjust/40)

def getFreq(row):
    #return str(midiNumToFreq(int(row[4].strip())))
    return row[4].strip()

def midiNumToFreq(midiNumber):
    return 440 * pow(2, (midiNumber-69)/float(12))

def buildBeep():
    csvFile = csv.reader(open(args.f, 'r', encoding='utf-8', errors='ignore'))
    beepOut = ''
    noteStart = 0
    pauseStart = 0
    noteison = 0
    for row in csvFile:
        if 'Note_on_c' in row[2] or 'Note_off_c' in row[2]:
            if (0 == int(row[5].strip()) or noteison == 1)and int(row[0].strip()) == track:
                noteison=0
                pauseStart = int(row[1].strip())
                beepOut += '\'B\',  ' + getFreq(row) + ', ' + getDuration(row, noteStart) + ', '
            elif int(row[0].strip()) == track:
                noteison=1
                noteStart = int(row[1].strip())
                if getSleep(row, pauseStart) >= 1:
                    beepOut += '\'S\', ' + str(getSleep(row, pauseStart)) + ', '
        if 'Tempo' in row[2]:
            global tempoMultiplier
            tempo = int(row[3].strip())
            tempoMultiplier = tempo /480/1000
    outputFile = open('beep.h', 'w')
    outputFile.write('unsigned char code beeptable[] = {')
    outputFile.write(beepOut)
    outputFile.write('\'T\'};')
    outputFile.close()
    return

if not args.f:
    parser.print_help()
else:
    buildBeep()
