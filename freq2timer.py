clock=12000000
def midiNumToFreq(midiNumber):
    return 440 * pow(2, (midiNumber-69)/float(12))*2
def freqToTimer(freq):
    t = freq
    tk = (65536-clock/12/t)
    if tk < 0:
        return 0
    return tk
f = open('.\\tone.h', "w")
f.write("unsigned int code tonetofreq[] = {")
for i in range(120):
    print(i)
    f.write(str(int(freqToTimer(midiNumToFreq(i)))))
    f.write(', ')
f.write('};')
f.close()