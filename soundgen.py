import sys
import wave
import os
import shutil
from psychopy import sound, core



def soundrename(old, new):
    """copy and rename a sound"""
    shutil.copy(old,new)


def soundcombine(sound1,sound2, newsound):
    """grabs two sounds and pastes them together"""
    outfile = newsound
    infiles = [sound1,sound2]
    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()

def soundtriplet(s1,s2,s3,s4):
    """combine 3 sounds"""
    soundcombine(s1,s2,"temp.wav")
    soundcombine("temp.wav", s3, s4)


def sound4(s1,s2,s3,s4,s5):
    """combine 4 sounds"""
    soundtriplet(s1,s2,s3,"t.wav")
    soundcombine("t.wav", s4, s5)


def sound5(s1,s2,s3,s4,s5,s6):
    """ combine 5 sounds"""
    soundtriplet(s1,s2,s3,"t1.wav")
    soundcombine(s4,s5, "t2.wav")
    soundcombine("t1.wav", "t2.wav",s6)


def sound6(s1,s2,s3,s4,s5,s6,s7):
    """ combine 6 sounds"""
    soundtriplet(s1,s2,s3,"tt1.wav")
    soundtriplet(s4,s5,s6, "tt2.wav")
    soundcombine("tt1.wav", "tt2.wav",s7)

def getdur(s):
    sound_file = sound.Sound(s)
    dur = sound_file.getDuration()
    return dur

def getdurs(file):
    for d in listofdurs:
        if d[0] == file:
            return d
    

listofdurs = []
    
    

# make all nouns + all nouns w determiners + all determiners
for i in range(1,7): # noun 1-6
    for j in range(1,3): # sem 1,2
        for k in range(1,3): # n 1,2
            s1 = "t1w1s" + str(j) + "n" +str(k) +".wav"
            s2 = "t3w" + str(i) + "s" + str(j) + "n" +str(k) +".wav"
            #print s1, getdur(s1)
            #print s2, getdur(s2)
            sout = "combined/10100001" + str(j) + str(k) + "000" + str(i) + str(j) + str(k) +"000000.wav"
            soundcombine(s1,s2,sout) # noun + determiner
            listofdurs.append([sout, getdur(sout), getdur(s1), 0, getdur(s2), 0,0,0,0])
            #print sout, getdur(sout)
            snew = "combined/0010000000000" + str(i) + str(j) + str(k) +"000000.wav"
            soundrename(s2,snew) # rename noun file
            listofdurs.append([snew, getdur(snew), 0,0,getdur(s2), 0,0,0,0])
            sdet = "combined/10000001"+ str(j) + str(k) + "000000000000.wav"
            soundrename(s1, sdet)
            listofdurs.append([sdet, getdur(sdet), getdur(s1), 0,0,0,0,0,0])


# make all colours w and w/o suffixes
for l in range(1,3): # color 1-6
    sold = "t2w" + str(l) + ".wav"
    #print sold, getdur(sold)
    snew = "combined/0100000000" + str(l) + "00000000000.wav"
    soundrename(sold, snew) # rename color roots
    listofdurs.append([snew, getdur(snew), 0, getdur(sold), 0,0,0,0,0])
    for j in range(1,3): # sem 1,2
        for k in range(1,3): # n 1,2
            s1 = "t2w" + str(l) + "s" + str(j) + "n" +str(k) +".wav"
            #print s1, getdur(s1)
            s2 = "combined/0100000000"+ str(l) + str(j) + str(k) + "000000000.wav"
            soundrename(s1,s2)
            listofdurs.append([s2, getdur(s2), 0, getdur(s1), 0,0,0,0,0])


# make marking words w and w/o 'ot'
for q in range(1,5): # markings
    old = "t4w" + str(q) + ".wav"
    #print old, getdur(old)
    new = "combined/0001000000000000" + str(q) + "00000.wav"
    soundrename(old,new)
    listofdurs.append([new, getdur(new), 0,0,0,getdur(old),0,0,0])
    ot = "t5w1.wav"
    ot2 = "combined/0000100000000000010000.wav"
    soundrename(ot,ot2)
    listofdurs.append([ot2, getdur(ot2), 0,0,0,0,getdur(ot),0,0])
    #print ot, getdur(ot)
    new2 = "combined/0001100000000000" + str(q) + "10000.wav"
    soundcombine(old, ot, new2)
    listofdurs.append([new2, getdur(new2), 0,0,0,getdur(old),getdur(ot),0,0])
    #print new2, getdur(new2)

# make verbs with and w/o agreement
for z in range(1,4): # verbs
    old = "t6w" + str(z) + ".wav"
    #print old, getdur(old)
    new = "combined/000001000000000000" + str(z) + "000.wav"
    soundrename(old, new)
    listofdurs.append([new, getdur(new),0,0,0,0,0,getdur(old), 0])
    for b in range(1,3): # v sem
        for c in range(1,3): # v n
            o = "t6w" + str(z) + "s" + str(b) + "n" + str(c) + ".wav"
            n = "combined/000001000000000000" + str(z) + str(b) + str(c) + "0.wav"
            #print o, getdur(o)
            soundrename(o,n)
            listofdurs.append([n, getdur(n),0,0,0,0,0,getdur(o), 0])



# make landscapes
for t in range(1,4): # landscapes
    old = "t7w" + str(t) + ".wav"
    new = "combined/000000100000000000000" + str(t) + ".wav"
    soundrename(old,new)
    listofdurs.append([new, getdur(new),0,0,0,0,0,0,getdur(old)])

    #print old, getdur(old)

for i in range(1,7): # noun 1-6
    for d in range(1,3): # s 
        for e in range(1,3): # n 
            for l in range(1,3): # color 1-2
                #ws = 3-d
                #wn = 3-e
                det = "t1w1s" + str(d) + "n" +str(e) +".wav"
                col = "t2w" + str(l) + "s" + str(d) + "n" +str(e) +".wav"
                mon = "t3w" + str(i) + "s" + str(d) + "n" +str(e) +".wav"
                #monws = "t3w" + str(i) + "s" + str(ws) + "n" +str(e) +".wav"
                #monwn = "t3w" + str(i) + "s" + str(d) + "n" +str(wn) +".wav"
                dcm = "combined/11100001" + str(d) + str(e) + str(l) + str(d) + str(e) + str(i) + str(d) + str(e) + "000000.wav"
                soundtriplet(det,col,mon,dcm)
                listofdurs.append([dcm, getdur(dcm), getdur(det), getdur(col), getdur(mon), 0,0,0,0])
                for q in range(1,5): # markings
                    mar = "combined/0001100000000000" + str(q) + "10000.wav"
                    mardur = getdurs(mar)[5]
                    otdur = getdurs(mar)[6]
                    dcmm = "combined/11111001" + str(d) + str(e) + str(l) + str(d) + str(e) + str(i) + str(d) + str(e) + str(q) + "10000.wav"
                    sound4(det, col, mon, mar, dcmm)
                    listofdurs.append([dcmm, getdur(dcmm), getdur(det), getdur(col), getdur(mon), mardur,otdur,0,0])
                    for z in range(1,4): # verbs
                        ver = "combined/000001000000000000" + str(z) + str(d) + str(e) + "0.wav"
                        #verws = "000001000000000000" + str(z) + str(ws) + str(e) + "0.wav"
                        #verwn = "000001000000000000" + str(z) + str(d) + str(wn) + "0.wav"
                        for t in range(1,4): # landscapes
                            lan = "combined/000000100000000000000" + str(t) + ".wav"
                            dcmmvl = "combined/11111111"+ str(d) + str(e) + str(l) + str(d) + str(e) + str(i) + str(d) + str(e) + str(q) + '1' + str(z) + str(d) + str(e) + str(t) + ".wav"
                            #dcmwsmvl = "1111111"+ str(d) + str(e) + str(l) + str(d) + str(e) + str(i) + str(ws) + str(e) + str(q) + str(z) + str(d) + str(e) + str(t) + ".wav"
                            #dcmwnmvl = "1111111"+ str(d) + str(e) + str(l) + str(d) + str(e) + str(i) + str(d) + str(wn) + str(q) + str(z) + str(d) + str(e) + str(t) + ".wav"
                            #dcmmvwsl = "1111111"+ str(d) + str(e) + str(l) + str(d) + str(e) + str(i) + str(d) + str(e) + str(q) + str(z) + str(ws) + str(e) + str(t) + ".wav"
                            #dcmmvwnl = "1111111"+ str(d) + str(e) + str(l) + str(d) + str(e) + str(i) + str(d) + str(e) + str(q) + str(z) + str(d) + str(wn) + str(t) + ".wav"
                            sound6(det, col, mon, mar, ver, lan,dcmmvl)
                            listofdurs.append([dcmmvl, getdur(dcmmvl), getdur(det), getdur(col), getdur(mon), mardur,otdur, getdur(ver), getdur(lan)])
                            #sound6(det, col, monws, mar, ver, lan,dcmwsmvl)
                            #sound6(det, col, monwn, mar, ver, lan,dcmwnmvl)
                            #sound6(det, col, mon, mar, verws, lan,dcmmvwsl)
                            #sound6(det, col, mon, mar, verwn, lan,dcmmvwnl)
# Updated for python 3 print syntax                        
print (len(listofdurs))
# generate a new one w/o duplicates
listofdur = []
for i in listofdurs:
       if i not in listofdur:
          listofdur.append(i)

# Updated for python 3 print syntax   
print (len(listofdur))

title = 'listofsounddurations.txt'
f=open(title, 'w')
for it in listofdur:
    f.write(it[0] + "\t" + str(it[1]) + "\t" + str(it[2]) + "\t" + str(it[3]) + "\t" + str(it[4]) + "\t" + str(it[5]) + "\t" + str(it[6]) + "\t" + str(it[7]) + "\t" + str(it[8]) +"\n")

