import collections
import random

def pick2outof6(six): # this actually also works if len(six) is e.g. 4
    random.shuffle(six)
    two = []
    two.append(six[0])
    two.append(six[1])
    return two

def checktwo(tw):
    mt1 = tw[0][1]
    mt2 = tw[1][1]
    if mt1 == 'm1' or mt1 == 'm2' or mt1 == 'm3':
        t1 = 'nice'
    else:
        t1 = 'scary'
    if mt2 == 'm1' or mt2 == 'm2' or mt2 == 'm3':
        t2 = 'nice'
    else:
        t2 = 'scary'
    if t1 == t2:
        return 0
    else:
        return 1

def generateverbtrials():
    lst = []
    random.shuffle(FCtest)
    lst.append(FCtest.pop(0))
    i = 0
    while i < 5:
        maybe = FCtest.pop(0)
        tvc = tempcounter(maybe, lst,3)
        if tvc[0][1] > 1:
            i += 1
            FCtest.append(maybe)
            continue
        tlc = tempcounter(maybe, lst,4)
        if tlc[0][1] > 1:
            i += 1
            FCtest.append(maybe)
            continue
        else:
            lst.append(maybe)
            i += 1
    checkverbtrials(lst)
    return lst

def checkverbtrials(lstt):
    if len(lstt) < 3:
        for k in range(len(lstt)):
            FCtest.append(lstt.pop(0))

def tempcounter(trial, lst, nr):
    counter = collections.Counter()
    counter[trial[nr]] += 1
    for tr in lst:
        counter[tr[nr]] += 1
    return counter.most_common()

def checkpatterns(blocklst, f = 0):
    if len(blocklst) == 6:
        tpc2 = collections.Counter()
        for i in range(1,5):
            pat = 'p' + str(i)
            tpc2[pat] = 0
        for tr in blocklst:
            tpc2[tr[2]] += 1
        tpc2mc = tpc2.most_common()
        if len(tpc2mc) > 4:
            for j in range(6):
                if blocklst[0][0] != 'c0':
                    unusedtriallist[j][f].append(blocklst.pop(0))
                else:
                    blocklst.pop(0)
        else:
            if tpc2mc[-1][1] == 0:
                for j in range(6):
                    unusedtriallist[j][f].append(blocklst.pop(0))
    elif len(blocklst) < 6:
        print ('ik ben niet vol', len(blocklst), 'dit zou NOOIT moeten gebeuren....')
        for k in range(len(blocklst)):
            unusedtriallist[k][f].append(blocklst.pop(0))

def generateblock(v=0): # v = 0 for probable, v == 1 for improbable
    blocklist = []
    random.shuffle(unusedtriallist)
    for i in range(6):
        random.shuffle(unusedtriallist[i][v])
        trycounter = 0
        #while trycounter < len(triallist[i][1]):
        while trycounter < 74:
            #if trycounter == 0: 
            #    print 'dit is nu aan het begin de blocklist', blocklist
            if trycounter == 73:                
                blocklist.append(['c0', 'm0', 'p0', 'v0', 'l0', 'n0'])
            maybetrial = unusedtriallist[i][v].pop(0)
            tpc = tempcounter(maybetrial, blocklist, 2)
            if tpc[0][1] > 2: 
                trycounter += 1
                unusedtriallist[i][v].append(maybetrial)
                continue
            tcc = tempcounter(maybetrial, blocklist, 0)
            if tcc[0][1] > 3:
                trycounter += 1
                unusedtriallist[i][v].append(maybetrial)
                continue
            tnc = tempcounter(maybetrial, blocklist, 5)
            if tnc[0][1] > 3:
                trycounter += 1
                unusedtriallist[i][v].append(maybetrial)
                continue
            tlc = tempcounter(maybetrial, blocklist, 4)
            if tlc[0][1] > 2:
                trycounter += 1
                unusedtriallist[i][v].append(maybetrial)
                continue
            tvc = tempcounter(maybetrial, blocklist, 3)
            if tvc[0][1] > 2:
                trycounter += 1
                unusedtriallist[i][v].append(maybetrial)
                continue
            else:
                blocklist.append(maybetrial)
                break
    checkpatterns(blocklist, f = v)
    return blocklist



colorcounter = collections.Counter()
monstercounter = collections.Counter()
patterncounter = collections.Counter()
verbcounter = collections.Counter()
landscapecounter = collections.Counter()
numbercounter = collections.Counter()
cmcounter = collections.Counter()
cvcounter = collections.Counter()
mvcounter = collections.Counter()
# pv
clcounter = collections.Counter()
mlcounter = collections.Counter()
#pl
vlcounter = collections.Counter()
cncounter = collections.Counter()
mncounter = collections.Counter()
#pn
vncounter = collections.Counter()
lncounter = collections.Counter()
triallist = []
m6list = []
m1list = []
m2list = []
m3list = []
m4list = []
m5list = []
for i in range(0,4):
    if i == 0:
        mrange = range(1,4)
        prange = range(1,3)
    elif i == 3:
        mrange = range(1,4)
        prange = range(3,5)
    if i == 2:
        mrange = range(4,7)
        prange = range(1,3)
    elif i == 1:
        mrange = range(4,7)
        prange = range(3,5)
    for m in mrange:
        mproblist = []
        mimproblist = []
        monster = 'm' + str(m)
        monstercounter[monster] = 0
        for c in range(1,3):
            color = 'c' + str(c)
            colorcounter[color] = 0
            cm = color + monster
            cmcounter[cm] = 0 
            for p in prange:
                pattern = 'p' + str(p)
                patterncounter[pattern] = 0
                cp = color + pattern
                mp = monster + pattern
                # cp, mp
                for v in range(1,4):
                    verb = 'v' + str(v)
                    verbcounter[verb] = 0
                    cv = color + verb
                    mv = monster + verb
                    pv = pattern + verb
                    cvcounter[cv] = 0
                    mvcounter[mv] = 0
                    #pv
                    for l in range(1,4):
                        landscape = 'l' + str(l)
                        landscapecounter[landscape] = 0
                        cl = color +  landscape
                        ml = monster + landscape
                        pl = pattern + landscape
                        vl = verb + landscape
                        clcounter[cl] = 0
                        mlcounter[ml] = 0
                        #pl
                        vlcounter[vl] = 0
                        for n in range(1,3):
                            number = 'n' + str(n)
                            numbercounter[number] = 0
                            cn = color + number
                            mn = monster + number
                            pn = pattern + number
                            vn = verb + number
                            ln = landscape + number
                            cncounter[cn] = 0
                            mncounter[mn] = 0
                            #pn
                            vncounter[vn] = 0
                            lncounter[ln] = 0
                            #trial = [color, monster, pattern, verb, landscape, number, cm,cp, mp, cv, mv, pv, cl, ml, pl, vl, cn, mn, pn, vn, ln]
                            trial = [color, monster, pattern, verb, landscape, number]
                            if i < 2:
                                mproblist.append(trial)
                            elif i > 1:
                                mimproblist.append(trial)
        if i < 2:
            if m == 1:
                m1list.append(mproblist)
            elif m == 2:
                m2list.append(mproblist)
            elif m == 3:
                m3list.append(mproblist)
            elif m == 4:
                m4list.append(mproblist)
            elif m == 5:
                m5list.append(mproblist)
            elif m == 6:
                m6list.append(mproblist)
        if i > 1:
            if m == 1:
                m1list.append(mimproblist)
            elif m == 2:
                m2list.append(mimproblist)
            elif m == 3:
                m3list.append(mimproblist)
            elif m == 4:
                m4list.append(mimproblist)
            elif m == 5:
                m5list.append(mimproblist)
            elif m == 6:
                m6list.append(mimproblist)
triallist.append(m1list)
triallist.append(m2list)
triallist.append(m3list)
triallist.append(m4list)
triallist.append(m5list)
triallist.append(m6list)

for p in range(1,400):
    fulltriallistname = 'data/s' + str(p) + '/fulltriallist.txt'
    file = open('exposure.txt', 'r')
    exposure = []
    for line in file:
        trial = line.split("\t")
        trial.pop(-1)
        exposure.append(trial)
    exposure.pop(0)

    unusedtriallist = []
    for m in triallist:
        newm = []
        for l in m:
            newl = [x for x in l if x not in exposure]
            newm.append(newl)
        unusedtriallist.append(newm)

    j = 0
    while j < 40:
        FCtest = generateblock()
        j += 1
        if len(FCtest) == 6:
            break



    l = 0
    while l < 40:
        FCverbtrials = generateverbtrials()
        l += 1
        if len(FCverbtrials) == 3:
            break

    # program now picks out 6 trials for FC, and figures out what 3 can test verbs and what 3 can test landscapes

    EMimprobtrials = []

    b = 0
    while b < 80:
        emib = generateblock(v=1)
        v += 1
        if len(emib) == 6:
            EMimprobtrials.append(emib)
        if len(EMimprobtrials) == 4:
            break

    fourthblock = EMimprobtrials[3]
    q = 0
    while q < 30:
        boileddown = pick2outof6(fourthblock)
        ch = checktwo(boileddown)
        q += 1
        if ch == 1:
            EMimprobtrials[3] = boileddown
            break

    EMnadjtrials = []

    e = 0
    while e < 80:
        eb = generateblock()
        e += 1
        if len(eb) == 6:
            EMnadjtrials.append(eb)
        if len(EMnadjtrials) == 2:
            break

    EMsadjtrials = []

    f = 0
    while f < 80:
        fb = generateblock()
        f += 1
        if len(fb) == 6:
            EMsadjtrials.append(fb)
        if len(EMsadjtrials) == 2:
            break


    EMnnadjtrials = []

    g = 0
    while g < 80:
        gb = generateblock()
        g += 1
        if len(gb) == 6:
            EMnnadjtrials.append(gb)
        if len(EMnnadjtrials) == 2:
            break


    EMsnadjtrials = []

    h = 0
    while h < 80:
        hb = generateblock()
        h += 1
        if len(hb) == 6:
            EMsnadjtrials.append(hb)
        if len(EMsnadjtrials) == 2:
            break


    EMprobabletrials = []

    k = 0
    while k < 200:
        kb = generateblock()
        k += 1
        if len(kb) == 6:
            EMprobabletrials.append(kb)
        if len(EMprobabletrials) == 4:
            break
            


    EMswitchtrials = []

    s = 0
    while s < 80:
        sb = generateblock()
        s += 1
        if len(sb) == 6:
            EMswitchtrials.append(sb)
        if len(EMswitchtrials) == 6:
            break

    extra1 = EMswitchtrials.pop(0)
    extra2 = EMswitchtrials.pop(0)

    u = 0
    while u < 30:
        boild = pick2outof6(extra1)
        chb = checktwo(boild)
        u += 1
        if chb == 1:
            EMswitchtrials.append(boild)
            extra3 = [x for x in extra1 if x not in boild]
            break

    v = 0
    while v < 30:
        boi = pick2outof6(extra3)
        chn = checktwo(boi)
        v += 1
        if chn == 1:
            EMswitchtrials.append(boi)
            extra4 = [x for x in extra3 if x not in boi]
            EMswitchtrials.append(extra4)
            break


    r = 0
    while r < 30:
        boileddown = pick2outof6(extra2)
        ch = checktwo(boileddown)
        r += 1
        if ch == 1:
            EMswitchtrials.append(boileddown)
            break

    EMSwitch1 = []
    EMSwitch1.append(EMswitchtrials[0])
    EMSwitch1.append(EMswitchtrials[4])

    EMSwitch2 = []
    EMSwitch2.append(EMswitchtrials[1])
    EMSwitch2.append(EMswitchtrials[5])

    EMSwitch3 = []
    EMSwitch3.append(EMswitchtrials[2])
    EMSwitch3.append(EMswitchtrials[6])

    EMSwitch4 = []
    EMSwitch4.append(EMswitchtrials[3])
    EMSwitch4.append(EMswitchtrials[7])



    counter = 1
    
    f = open(fulltriallistname, 'w')
    f.write("trialnr\tcolor\tmonster\tpattern\tverb\tlandscape\tnumber\n")
    for tr in exposure:
        type = 'exposure'
        f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
        counter += 1

    for tr in FCverbtrials:
        type = 'FCverb'
        f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
        counter += 1

    for tr in FCtest:
        type = 'FClandscape'
        f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
        counter += 1

    for block in EMimprobtrials:
        for tr in block:
            type = 'EMimprob'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1       

    for block in EMnadjtrials:
        for tr in block:
            type = 'EMnadj'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1      

    for block in EMnadjtrials:
        for tr in block:
            type = 'EMsadj'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1 

    for block in EMnnadjtrials:
        for tr in block:
            type = 'EMnnadj'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1 

    for block in EMsnadjtrials:
        for tr in block:
            type = 'EMsnadj'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1 

    for block in EMprobabletrials:
        for tr in block:
            type = 'EMprob'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1 



    for block in EMSwitch1:
        for tr in block:
            type = 'EMswitch1'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1 

    for block in EMSwitch2:
        for tr in block:
            type = 'EMswitch2'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1 
            
    for block in EMSwitch3:
        for tr in block:
            type = 'EMswitch3'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1 

    for block in EMSwitch4:
        for tr in block:
            type = 'EMswitch4'
            f.write(str(counter) + "\t" + tr[0] + "\t" + tr[1] + "\t" + tr[2] + "\t" + tr[3] + "\t" + tr[4] + "\t" + tr[5] + "\t"+ type + "\n")
            counter += 1 




