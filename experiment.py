############################################
## written by Elise Hopman
## at University of Wisconsin - Madison
## spring/summer 2016
############################################

"""
This program runs an artificial language learning experiment
"""

import sys
from psychopy import visual, core, event
import numpy as num
import random
from psychopy import gui, sound, microphone
import webbrowser
import wave
import time

# functions for interaction with subject
def getsubjectnumber():
    myDlg = gui.Dlg(title="Subject", pos=(200,400))
    myDlg.addText('              ')
    myDlg.addField('Subject number:',)
    myDlg.addText('              ')
    myDlg.show()
    if myDlg.OK:
        info = myDlg.data #this will be a list of data returned from each field added in order
        subnr = int(info[0])
    else: sys.exit()  # if you press cancel the program will just stop. 
    return subnr
def getconditionnumber():
    myDlg = gui.Dlg(title="Experimentinfo", pos=(200,400))
    myDlg.addText('              ')
    myDlg.addField('Condition:',)
    myDlg.addText('              ')
    myDlg.show()
    if myDlg.OK:
        info = myDlg.data #this will be a list of data returned from each field added in order
        condnr = int(info[0])
    else: sys.exit()  # if you press cancel the program will just stop. 
    return condnr
def showmessage(window, whatyouwannasay):
    """ first makes the screen blank for half a second, then displays a message untill a key is pressed."""
    blankscreen(window, .05) # THIS SHOULD BE 0.5 JUST HAVE IT LIKE THIS FOR TESTING ## CHANGE BACK
    message = visual.TextStim(window,pos = [0,0], text=whatyouwannasay, color = 'black')
    message.draw()
    window.flip()
    waitforkey()
def blankscreen(window, time):
    """ This function makes the screen blank for a specified time by drawing a white square as big as my laptop screen"""
    square = visual.GratingStim(window ,tex="none",mask="none",color="white",size=[1440,900], pos = [0,0])
    square.draw()
    window.flip()
    core.wait(time)
def waitforkey():
    """ This function waits for a key"""
    # this function records time till keypress and when key is pressed returns the time.
    waitforkey = True
    timer = core.Clock()
    timer.reset()
    while waitforkey == True:
        if len(event.waitKeys())>0:
            return timer.getTime()
            waitforkey = False
def playsound(name):
    """ plays a sound and returns its duration """
    sound_file = sound.Sound(name)
    dur = sound_file.getDuration()
    sound_file.play()
    return dur
    #core.wait(dur)
def showimage(window, time, picture,pl = '1', sizeofpic = 'no', issigns = False, feedback = 'none', mic = False, green = False):
    """ Shows an image in a certain position for a time, picture = path to pic (including .jpg or whatever)"""
    p1 = visual.ImageStim(window, image = picture, pos = [0,0])
    if pl == '2':
        p1 = visual.ImageStim(window, image = picture, pos = [-200,0])
        p2 = visual.ImageStim(window, image = picture, pos = [200,0])
        if sizeofpic != 'no':
            p2.setSize(sizeofpic)
        p2.draw()
    if sizeofpic != 'no':
        p1.setSize(sizeofpic)
    p1.draw()
    if issigns == True:
        issign = visual.ImageStim(window, image = "pictures/is.png", pos = [500,-400], size = [75,45])
        issign.draw()
        isnot = visual.ImageStim(window, image = "pictures/isnot.png", pos = [-500,-400], size = [90,75])        
        isnot.draw()
    if feedback == 'wrong':
        feedb = visual.ImageStim(window, image = "pictures/rcross.png", pos = [0,-400], size = [75,75])
        feedb.draw()
    elif feedback == 'right':
        feedb = visual.ImageStim(window, image = "pictures/gcheck.png", pos = [0,-400], size = [75,75])
        feedb.draw()
    if mic == True:
        mic = visual. ImageStim(window, image = "pictures/mic.png", pos = [0, -400], size = [64,64])
        mic.draw()
    if green == True:
        left = visual.Rect(win,lineColor="green",fillColor="green", pos = [-500, 0] ,size=[10,1610])
        left.draw()
        right = visual.Rect(win,lineColor="green",fillColor="green", pos = [500, 0] ,size=[10,1610])
        right.draw()
        up = visual.Rect(win,lineColor="green",fillColor="green", pos = [0, 400] ,size=[2010,10])
        up.draw()
        down = visual.Rect(win,lineColor="green",fillColor="green", pos = [0, -400] ,size=[2010,10])
        down.draw()
    window.flip()
    core.wait(time)
def forcedchoiceimage(window, time, picture1, picture2, pl = '1', vid = 'no', keys = 'no', si = [360,270]):
    """shows 2 or 4 images for forced choice"""
    multiple = si
    if pl == '1':
        p1 = visual.ImageStim(window, image = picture1, pos = [-480,0], size = multiple)
        p2 = visual.ImageStim(window, image = picture2, pos = [480,0], size = multiple)
    elif pl == '2':
        p1 = visual.ImageStim(window, image = picture1, pos = [-650,0], size = multiple)
        p2 = visual.ImageStim(window, image = picture2, pos = [650,0], size = multiple)       
        p3 = visual.ImageStim(window, image = picture1, pos = [-310,0], size = multiple)
        p4 = visual.ImageStim(window, image = picture2, pos = [310,0], size = multiple) 
        p3.draw()
        p4.draw()
    elif pl == '3': # two pics on left one on right 
        p1 = visual.ImageStim(window, image = picture1, pos = [-650,0], size = multiple)
        p2 = visual.ImageStim(window, image = picture2, pos = [480,0], size = multiple)       
        p3 = visual.ImageStim(window, image = picture1, pos = [-310,0], size = multiple)     
        p3.draw()
    elif pl == '4': # two pics on right one on left
        p1 = visual.ImageStim(window, image = picture1, pos = [-650,0], size = multiple)
        p2 = visual.ImageStim(window, image = picture2, pos = [650,0], size = multiple)       
        p3 = visual.ImageStim(window, image = picture2, pos = [310,0], size = multiple)     
        p3.draw()
    p1.draw()
    p2.draw()
    showkeys = 'no'
    if keys == 'yes':
        showkeys = 'yes'
        key1 = visual.TextStim(window, pos = [-480,-400], text='x', color = 'black')
        key1.draw()
        key2 = visual.TextStim(window, pos = [480, -400], text = 'm', color = 'black')
        key2.draw()
    window.flip()
    core.wait(time)
    if vid == 'yes':
        twomovies(window, picture1, picture2, keys = showkeys)
def showfixation(window,t, position):
    """ This function shows a fixation cross for a specified time t at a specified position in a specified window"""
    cross = visual.TextStim(window,pos = position, text='+', color = 'black', height = 80)
    cross.draw()
    window.flip()
    core.wait(t)
def passivetrial(window, picpath, soundpath, pl = '1', vid = 'no'):
    """ Shows an image and plays the sound that goes with it twice. """
    # show all pics in the middle of the screen for now
    M = [0,0]
    single = [480, 360] # sizeofpic trying out
    if vid == 'yes':
        single = [900,675]
    # trial starts with a fixation cross for 500 ms
    showfixation(window, 0.5, M)
    # put the picture on the screen for 500 ms
    endpic = picpath
    showimage(window, .5, picpath, pl, sizeofpic = single, green = True)
    if vid == 'yes':
        endpic = movie(window, picpath, sizeofpic = single, green = True)
    # play the sound (while freezing the screen for as long as that takes)
    core.wait(playsound(soundpath))
    # show the picture for 1.5 s
    showimage(window, 1.5, endpic, pl, sizeofpic = single, green = True)
    # quick blank screen
    blankscreen(window, 0.5)
    # and then show the picture for 500 ms
    showimage(window, 0.5, picpath, pl, sizeofpic = single, green = True)
    if vid == 'yes':
        movie(window, picpath, sizeofpic = single, green = True)
    # play the sound (while freezing the screen for as long as that takes)
    core.wait(playsound(soundpath))
    # and then show the picture for 1.5 s
    showimage(window, 1, endpic, pl, sizeofpic = single, green = True)    
def activecomptrial(window, picpath1, picpath2, soundpath, pl = '1', vid = 'no'):
    """Shows an image and plays a sound and has the participant indicate whether these match and gives them feedback"""
    # show all pics in the middle of the screen for now
    M = [0,0]
    single = [480, 360]
    if vid == 'yes':
        single = [900,675]
    endpic = picpath1
    # trial starts with a fixation cross for 500 ms
    showfixation(window, 0.5, M)
    # put the picture on the screen for 500 ms
    showimage(window, .5, picpath1, pl, sizeofpic = single)
    if vid == 'yes':
        endpic = movie(window, picpath1, sizeofpic = single)
    # play the sound (while freezing the screen for as long as that takes)
    core.wait(playsound(soundpath))
    timer2 = core.MonotonicClock() # RT starts right as the sound is done till they hit the key
    # show the picture with check and crossmarks
    showimage(window, .01, endpic, pl, sizeofpic = single, issigns = True)
    response=event.waitKeys(keyList=['f','l'])[0]
    reaction = timer2.getTime()
    # right now it gives you feedback as to which one you chose, not as to whether that was the correct option. 
    if response=="f":
        if picpath1 != picpath2:
            showimage(window, 1, endpic, pl, sizeofpic = single, feedback = 'right')
            blankscreen(window, .5)
        else:
            showimage(window, 1, endpic, pl, sizeofpic = single, feedback = 'wrong')
    elif response == "l":
        if picpath1 != picpath2:
            showimage(window, 1, endpic, pl, sizeofpic = single, feedback = 'wrong')
            blankscreen(window, .5)
        else:
            showimage(window, 1, endpic, pl, sizeofpic = single, feedback = 'right')
    # only if the picture changes because the 1st pic wasn't the correct one, there's a whitescreen in between
    showimage(window, .5, picpath2, pl, sizeofpic = single, green = True)
    endpic = picpath2
    if vid == 'yes':
        endpic = movie(window, picpath2, sizeofpic = single, green = True)
    core.wait(playsound(soundpath))
    showimage(window, 2, endpic, pl, sizeofpic = single, green = True)    
    inf = [response, reaction]
    return inf
def activeprodtrial(window, picpath, soundpath, pl = '1', vid = 'no'):
    """This function shows a picture, records with a mic, then plays the sound"""
    # show all pics in the middle of the screen for now
    M = [0,0]
    single = [480, 360]
    if vid == 'yes':
        single = [900,675]
    # trial starts with a fixation cross for 500 ms
    showfixation(window, 0.5, M)
    mic = microphone.AudioCapture()
    recname = 'data/s'+str(subjectnr) + '/recordings/recordingtrial'+ str(trialnr) + '.wav'
    mic.record(360, recname, block = False)
    reaction = 9990
    # put the picture on the screen for 500 ms
    timer2 = core.MonotonicClock() # so for these trials, RT includes .5 sec to see the pic + viddurations if applicable
    showimage(window, .5, picpath, pl, sizeofpic = single, mic = True)
    endpic = picpath
    event.clearEvents()
    if vid == 'yes':
        endpic = movie(window, picpath, sizeofpic = single, mic = True)
    while mic.recorder.running:
        if 'return' in event.getKeys():
            reaction = timer2.getTime()
            core.wait(1)
            mic.stop()
    showimage(window, .5, picpath, pl, sizeofpic = single, green = True)
    if vid == 'yes':
        movie(window, picpath, sizeofpic = single, green = True)
    core.wait(playsound(soundpath))
    showimage(window, 1, endpic, pl, sizeofpic = single, green = True)
    return reaction
def forcedchoicetesttrial(window, picpath1, picpath2, soundpath, pl = '1', vid = 'no'): 
    """Shows two pictures, plays a sound, has participant choose between the two pictures. """
    M = [0,0]
    # trial starts with a fixation cross for 500 ms
    showfixation(window, 0.5, M)
    showkey = 'yes'
    siz = [360,270]
    if vid == 'yes':
        siz = [900,675]
    forcedchoiceimage(window, .5, picpath1, picpath2, pl, vid, keys = showkey, si = siz)
    # we time how long a trial takes them.
    timer2 = core.MonotonicClock()
    sound_file = sound.Sound(soundpath)
    dur = sound_file.getDuration()
    sound_file.play()
    response=event.waitKeys(keyList=['x','m'])[0]
    reaction = timer2.getTime()
    if reaction < dur:
        sound_file.stop()
    out = [response, reaction]
    return out
def errormonitoringtesttrial(window, soundpath):
    """play a sound, have participant indicate right or wrong, record time"""
    # show all pics in the middle of the screen for now
    M = [0,0]
    # trial starts with a fixation cross for 500 ms
    showfixation(window, 0.5, M)
    showimage(window, .001, "pictures/empty.png", issigns = True)
    timer2 = core.MonotonicClock()
    sound_file = sound.Sound(soundpath)
    dur = sound_file.getDuration()
    sound_file.play()
    response=event.waitKeys(keyList=['f','l'])[0]
    reaction = timer2.getTime()
    if reaction < dur:
        sound_file.stop()
    out = [response, reaction]
    return out
def movie(window, name, sizeofpic = 'no', green = False, mic = False):
    """plays a movie frame by frame"""
    lngth = len(name)
    nam = name[0:lngth-5]
    for i in range(10):
        j = i+1
        frame = nam + '%d.png' %j
        showimage(window, .025, frame, sizeofpic = sizeofpic, green = green, mic = mic)
    return frame
def twomovies(window, name1, name2, keys = 'no'):
    """plays two movies side by side for a forced choice trial"""
    lngth1 = len(name1)
    shwk = 'no'
    if keys == 'yes':
        shwk = 'yes'
    nam1 = name1[0:lngth1-5]
    lngth2 = len(name2)
    nam2 = name2[0:lngth2-5]   
    for i in range(10):
        j = i+1
        frame1 = nam1 + '%d.png' %j
        frame2 = nam2 + '%d.png' %j
        forcedchoiceimage(window, 0.025, frame1, frame2, keys = shwk, si = [900,675])
def activecompblock(trials, trlnr, ittype, pl = '1'):
    random.shuffle(trials)
    picknonmatch = range(len(trials))
    random.shuffle(picknonmatch) # random shuffle to pick which half of the trials get to be mismatch
    alts = genalt(trials)
    tcrct = 0
    for t in range(len(trials)):
        trial = trials[t]
        snd = trial[1]
        ckey = 'none'
        if trial[2]=='m': # if monster vocab trials
            if pl == '2':
                snd = trial[4] # plural sound
        if picknonmatch[t] < len(trials)/2:# match
            info = activecomptrial(win, trial[0],trial[0], snd, pl)
            key = info[0]
            if key == 'l':
                tcrct = tcrct + 1
                ckey = '1'
            elif key == 'f':
                ckey = '0'
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trlnr + "AC\t" + ittype + "\t"+ str(ckey) + "\t" + key + "\tyesmatch\t" + str(info[1]) + "\t" + snd + "\t" + trial[0] + "\t" + trial[0] + "\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
        else: # mismatch
            info = activecomptrial(win,alts[t][0], trial[0], snd, pl)
            key = info[0]
            if key == 'f':
                tcrct = tcrct + 1
                ckey = '1'
            elif key == 'l':
                ckey = '0'            
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trlnr + "AC\t" + ittype + "\t"+ str(ckey) + "\t" + key + "\tmismatch\t" + str(info[1]) + "\t" + snd + "\t" + trial[0] + "\t" + alts[t][0] + "\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
        trlnr = trlnr + 1
    activecompcorrect.append([tcrct, ittype])
    return trlnr
# functions for generating the experiment
def getdurs(s):
    "for a sound file 's' it gets you a list with the duration of the total file as well as each of the individual words that form the phrase (so that might be 0 for some parts of some phrases)"
    for d in sounddurlist:
        if d[0] == s:
            return d
def getdur(s):
    sound_file = sound.Sound(s)
    dur = sound_file.getDuration()
    return dur
def genalt(lst):
    """this function shuffles the lst so that no element stays in its old place"""
    gelukt = False
    while gelukt == False:
        new = list(lst)
        random.shuffle(new)
        cntr = 0
        for i in range(len(lst)):
            if new[i] == lst[i]:
                cntr = cntr + 1
        if cntr == 0:
            gelukt = True
    return new
def attachalt(lst, trials):
    """attach an alternative pic from a different trial to each trial in 'trials' and output to 'list' these new trials"""
    talts = genalt(trials) # create derangement
    for t in range(len(trials)): # all of them will get an alternative assigned
        trl = list(trials[t])
        alt = talts[t][0] # grab foil the pic from the derangement selected trial
        trl.append(alt)
        lst.append(trl)
def assignlanguage(wlist):
    """This function grabs a list, randomizes it and logs it"""
    random.shuffle(wlist[0])
    random.shuffle(wlist[1])
    f.write("\n\n" + wlist[2])
    for i in range(len(wlist[0])):
        f.write('\n%d\t%d' %(wlist[0][i], wlist[1][i]))
def trialgenm(triallist, listofelements, sffxes, n = 0):
    """generate a list of all monstr noun trials""" 
    for j in range(len(listofelements[0])): # list of the visual monsters that is shuffled. 
        vismon = listofelements[0][j]
        if vismon < 4:
            vissem = 1
            audsem = sffxes[1][0]
        elif vismon >  4:
            vissem = 2
            audsem = sffxes[1][1]
        audmon = listofelements[1][j]
        visual = "pictures/PNG/1110007" + str(vismon) + str(vissem) + '000.png'
        sound1 = "sounds/combined/10100001" + str(audsem) +"1000" + str(audmon) + str(audsem) +"1000000.wav" # sgl sound
        sound2 = "sounds/combined/10100001"+ str(audsem) + "2000" + str(audmon) + str(audsem)+ "2000000.wav" # pl sound
        triallist.append([visual, sound1, listofelements[3], listofelements[4], sound2, vissem])
def trialgenc(triallist, listofelements):
    """generate a list of all color noun trials""" 
    # random shuffle to get alternative
    for i in range(len(listofelements[0])): # go through all words of that type
        viscol = listofelements[0][i]
        audcol = listofelements[1][i]
        visual = "pictures/PNG/100000" + str(viscol) + "00000.png"
        sound = "sounds/combined/0100000000"  + str(audcol) + "00000000000.wav"
        triallist.append([visual, sound, listofelements[3], listofelements[4]])
def trialgenp(triallist, listofelements):
    """generate a list of all pattern noun trials""" 
    # random shuffle to get alternative
    for i in range(len(listofelements[0])): # go through all words of that type
        vispat = listofelements[0][i]
        audpat = listofelements[1][i]
        visual = "pictures/PNG/000100000" + str(vispat) + "00.png"
        sound = "sounds/combined/0001000000000000"  + str(audpat) + "00000.wav"
        triallist.append([visual, sound, listofelements[3], listofelements[4]])
def trialgenv(triallist, listofelements):
    """generate a list of all verb noun trials""" 
    # random shuffle to get alternative
    for i in range(len(listofelements[0])): # go through all words of that type
        visverb = listofelements[0][i]
        audverb = listofelements[1][i]
        visual = "verbvocab/verb" + str(visverb) + "slide1.png"
        sound = "sounds/combined/000001000000000000"  + str(audverb) + "000.wav"
        triallist.append([visual, sound, listofelements[3], listofelements[4]])
def trialgenl(triallist, listofelements):
    """generate a list of all landscape noun trials""" 
    # random shuffle to get alternative
    for i in range(len(listofelements[0])): # go through all words of that type
        vislan = listofelements[0][i]
        audlan = listofelements[1][i]
        visual = "pictures/PNG/00000100000" + str(vislan) + ".png"
        sound = "sounds/combined/000000100000000000000"  + str(audlan) + ".wav"
        triallist.append([visual, sound, listofelements[3], listofelements[4]])
def trialgenCM(tlist, clrs, mnstrs,sfxs):
    """generate det col monster trials"""
    yellowdummy = list(range(6)) # shuffle to pick out which monsters are yellow in the first block
    pldummy = list(range(6)) # shuffle to pick out which monsters are plural in the first block
    random.shuffle(yellowdummy)
    random.shuffle(pldummy)
    for round in range(2):
        roundlist = []
        mdummy = list(range(6))
        monsterfoil = genalt(mnstrs[0])
        fdummy = list(range(6))
        random.shuffle(fdummy)
        for i in range(6): # through all monsters
            if round == 0: # which ones are sg/pl in the first round
                if pldummy[i] < 3:
                    n = 1
                elif pldummy[i] > 2:
                    n = 2
                if yellowdummy[i] < 3:
                    cs = clrs[1][0]
                    cp = clrs[0][0]
                    cff = clrs[0][1]
                elif yellowdummy[i]>2:
                    cs = clrs[1][1]
                    cp = clrs[0][1]
                    cff = clrs[0][0]
            elif round == 1: # and those are pl/sg in the second round
                if pldummy[i] < 3:
                    n = 2
                elif pldummy[i] > 2:
                    n = 1            
                if yellowdummy[i] >2:
                    cs = clrs[1][0]
                    cp = clrs[0][0]
                    cff = clrs[0][1]
                elif yellowdummy[i]<3:
                    cs = clrs[1][1]
                    cp = clrs[0][1]
                    cff = clrs[0][0]
            vismon = mnstrs[0][i]
            if vismon < 4:
                vissem = 1
                audsem = sfxs[1][0]
            elif vismon >3: 
                vissem = 2
                audsem = sfxs[1][1]
            vismonf = monsterfoil[i] 
            if vismonf < 4:
                vissemf = 1
            elif vismonf > 3:
                vissemf = 2
            audmon = mnstrs[1][i]
            sound = "sounds/combined/11100001" + str(audsem) + str(n) + str(cs) + str(audsem) + str(n) + str(audmon) + str(audsem) + str(n) + "000000.wav"
            pic = "pictures/PNG/111000" + str(cp) + str(vismon) + str(vissem) + "000.png"
            cf = cp
            if fdummy[i] == 1: # color foil
                cf = cff 
                vismonf = vismon # set monster to be the old one
                vissemf = vissem
            elif fdummy[i] == 2: # both foil
                cf = cff
            elif fdummy[i] > 2:
                vismonf = vismon # set monster to be the old one
                vissemf = vissem
            fpic = "pictures/PNG/111000" + str(cf) + str(vismonf) + str(vissemf) + "000.png" # generate the foil pic, which is the same pic if fdummy was > 2
            roundlist.append([i, pic, vismon, cp, sound, audmon, cs, vissem, n , fpic])
        tlist.append(roundlist)  
def trialgenNP(tlist, clrs, nmnstrs, smnstrs, nptrns, sptrns, sfx):
    """generate 24 trials with full NPs"""
    pat = [[[3,1,2],[4,3,4]], [[1,2,1],[2,4,3]], [[2,4,1],[3,4,3]],[[2,1,2],[3,1,4]]] # patterns in each round, sorted by those for nice and scary groups
    random.shuffle(pat)
    random.shuffle(nmnstrs)
    random.shuffle(smnstrs)
    for r in range(4): # four rounds
        roundlist = []
        nicefoil = genalt(nmnstrs)
        scaryfoil = genalt(smnstrs)
        pldummy = list(range(6))
        random.shuffle(pldummy)
        colourdummy = list(range(6))
        random.shuffle(colourdummy)
        fdummy = list(range(6))
        random.shuffle(fdummy)
        for i in range(6): # six trials per round
            if i < 3:
                vissem = 1
                audsem = sfx[1][0]
                vismon = nmnstrs[i][0]
                audmon = nmnstrs[i][1]
                vismonf = nicefoil[i][0]
                whichpattern = pat[r][0][i]
                if whichpattern < 3: # a prob pattern
                    h = whichpattern - 1
                    u = 1 - h
                    vispat = nptrns[h][0]
                    vispatf = nptrns[u][0]
                    audpat = nptrns[h][1]
                elif whichpattern > 2: # the improb pattern this round
                    h = whichpattern - 3
                    u = 1-h
                    vispat = sptrns[h][0]
                    vispatf = sptrns[u][0]
                    audpat = sptrns[h][1]
            elif i > 2:
                j = i-3
                vissem = 2
                audsem = sfx[1][1]
                vismon = smnstrs[j][0]
                audmon = smnstrs[j][1]
                vismonf = scaryfoil[j][0]
                whichpattern = pat[r][1][j]
                if whichpattern > 2: # a prob pattern
                    h = whichpattern - 3 # so h is 0 or 1
                    u = 1 - h # so u is 1 or 0 (the other one that h)
                    vispat = sptrns[h][0]
                    vispatf = sptrns[u][0]
                    audpat = sptrns[h][1]
                elif whichpattern < 3: # the improb pattern this round
                    h = whichpattern - 1
                    u = 1-h
                    vispat = nptrns[h][0]
                    vispatf = nptrns[u][0]
                    audpat = nptrns[h][1]
            if pldummy[i] < 3:
                n = 1
            elif pldummy[i] > 2:
                n = 2
            if colourdummy[i] < 3:    
                cp = clrs[0][0]
                cs = clrs[1][0]
            elif colourdummy[i]>2:
                cp = clrs[0][1]
                cs = clrs[1][1]
            sound = "sounds/combined/11111001" + str(audsem) + str(n) + str(cs) + str(audsem) + str(n) + str(audmon) + str(audsem) + str(n) + str(audpat) +"10000.wav"
            pic = "pictures/PNG/111100" + str(cp) + str(vismon) + str(vissem) + str(vispat) +"00.png"
            fcp = cp
            fmp = vismon
            fpat = vispat
            if fdummy[i] == 0:
                fcp = 3 - cp # so the other colour
            elif fdummy[i] == 1:
                fmp = vismonf
            elif fdummy[i] == 2:
                fpat = vispatf
            fpic = "pictures/PNG/111100" + str(fcp) + str(fmp) + str(vissem) + str(fpat) +"00.png"
            roundlist.append([pic, vismon, cp, vispat, sound, audmon, cs, vissem, n, fpic])
        tlist.append(roundlist)    
def trialgenfull(clrs, nmnstrs, smnstrs, nptrns, sptrns, vrbs, plnts, sfx, exposure):
    """generates a list of full sentence trials"""
    unroundlist = []
    activeroundlist = []
    passiveroundlist = []
    for item in exposure: # exposure is a list of 72 trials in groups of 6 that form a block. 
        cgen = item[8]
        cp = clrs[0][cgen]
        cs = clrs[1][cgen]
        mgen = item[10]
        if item[9] == 'nice':
            vismon = nmnstrs[mgen][0]
            audmon = nmnstrs[mgen][1]
            vissem = 1
            audsem = sfx[1][0]
        elif item[9] == 'scary':
            vismon = smnstrs[mgen][0]
            audmon = smnstrs[mgen][1]
            vissem = 2
            audsem = sfx[1][1]
        pgen = item[12]
        if item[11] == 'nice':
            vispat = nptrns[pgen][0]
            audpat = nptrns[pgen][1]
        elif item[11] == 'scary':
            vispat = sptrns[pgen][0]
            audpat = sptrns[pgen][1]
        vgen = item[13]
        visverb = vrbs[0][vgen]
        audverb = vrbs[1][vgen]
        lgen = item[14]
        vislan = plnts[0][lgen]
        audlan = plnts[1][lgen]
        nr = item[15]
        pic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(vispat) + str(visverb) + str(vislan)+ 'n' + str(nr) + 'f1.png'
        sound = "sounds/combined/11111111" + str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + str(audpat)+ '1' + str(audverb) + str(audsem) + str(nr) + str(audlan) + ".wav"
        unroundlist.append([pic, sound, cp, mgen, vissem, vispat, vgen, lgen, nr, vismon, visverb, vislan])
    tnr = 0
    planetlist = list(range(3))
    verblist = list(range(3))
    fdummy = list(range(6))
    for r in range(6):
        passiveblock = []
        for i in range(6):
            passivetrial = unroundlist[tnr]
            passiveblock.append([passivetrial[0], passivetrial[1]])
            tnr += 1
        passiveroundlist.append(passiveblock)
    for r in range(6):
        activeblock = []
        nmfoils = genalt(nmnstrs)
        smfoils = genalt(smnstrs)
        vfoils = genalt(verblist)
        lfoils = genalt(planetlist)
        random.shuffle(fdummy)
        for i in range(6):
            activetrial = unroundlist[tnr]
            cp = activetrial[2]
            cfc = 3-cp # 3 - colorpic is either 1 or 2 but the other one than the cp
            vissem = activetrial[4]
            mgen = activetrial[3]
            if vissem == 1: # vissem nice
                cmf = nmfoils[mgen][0] # mgen
            elif vissem == 2: # vissem scary
                cmf = smfoils[mgen][0] # mgen
            vispat = activetrial[5]
            if vispat < 3: #vispat nice pattern
                cpf = 3 - vispat # the other nice pattern
            elif vispat > 2: # vispat scary pattern
                cpf = 7 - vispat
            vgen = activetrial[6]
            lgen = activetrial[7]
            cvf = vrbs[0][vfoils[vgen]] # vgen picks out which vfoil it will be
            clf = plnts[0][lfoils[lgen]] # lgen picks out which foil it will be
            # so now i've generated a candidate foil for each aspect of each pic. now let's see who gets what foil
            fpic = activetrial[0]
            nr = activetrial[8]
            vismon = activetrial[9]
            visverb = activetrial[10]
            vislan = activetrial[11]
            if r % 3 == 0:
                if fdummy[i] == 0: # verbfoil
                    fpic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(vispat) + str(cvf) + str(vislan) + 'n' + str(nr) + 'f1.png'
                elif fdummy[i] == 1: # planetfoil
                    fpic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(vispat) + str(visverb) + str(clf) + 'n' + str(nr) + 'f1.png'
            elif r % 3 == 1:
                if fdummy[i] == 0: # planetfoil
                    fpic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(vispat) + str(visverb) + str(clf) + 'n' + str(nr) + 'f1.png'
                elif fdummy[i] == 1: # patternfoil
                    fpic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(cpf) + str(visverb) + str(vislan) + 'n' + str(nr) + 'f1.png'
            elif r % 3 == 2:
                if fdummy[i] == 0: # patternfoil
                    fpic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(cpf) + str(visverb) + str(vislan) + 'n' + str(nr) + 'f1.png'
                elif fdummy[i] == 1: # verbfoil
                    fpic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(vispat) + str(cvf) + str(vislan) + 'n' + str(nr) + 'f1.png'
            if r % 2 == 0:
                if fdummy[i] == 2: # monsterfoil
                    fpic = "slides/v111111"+str(cp) + str(cmf) + str(vissem) + str(vispat) + str(visverb) + str(vislan) + 'n' + str(nr) + 'f1.png'
            elif r % 2 == 1:
                if fdummy[i] == 2: # colourfoil
                    fpic = "slides/v111111"+str(cfc) + str(vismon) + str(vissem) + str(vispat) + str(visverb) + str(vislan) + 'n' + str(nr) + 'f1.png'
            activeblock.append([activetrial[0], activetrial[1], fpic])
            tnr += 1
        activeroundlist.append(activeblock)
    random.shuffle(activeroundlist)
    random.shuffle(passiveroundlist)
    return [passiveroundlist, activeroundlist]
def FCimprob(tlist, clrs, nmnstrs, smnstrs, nptrns,sptrns, sfxs):
    """generates a list of NP trials with improbable monster-pattern combinations (and probable foil pics)"""
    improbclnr = [[[1,1],[2,2]],[[1,2],[2,1]], [[2,1],[1,2]],[[2,1],[1,2]],[[2,2],[1,1]],[[1,1],[2,2]]] # colour and number for the improbable noun phrases
    foilpat = [[0,1],[1,0],[0,1],[0,1],[1,0],[0,1]]
    random.shuffle(nmnstrs)
    random.shuffle(smnstrs)
    random.shuffle(nptrns)
    random.shuffle(sptrns)
    colourlist = list(range(2))
    random.shuffle(colourlist)
    nrdummy = ['1','2']
    random.shuffle(nrdummy)
    for m in range(6): # 6 monsters
        for p in range(2): # 2 patterns
            if m < 3:
                vismon = nmnstrs[m][0] # monster pic
                audmon = nmnstrs[m][1]
                vissem = 1
                vispat = sptrns[p][0]
                audpat = sptrns[p][1]
                vpf = foilpat[m][p] # 0 or 1
                vispatf = nptrns[vpf][0]
                audsem = sfxs[1][0]
            elif m > 2:
                n = m-3
                vissem = 2
                vismon = smnstrs[n][0]
                audmon = smnstrs[n][1]
                vispat = nptrns[p][0]
                audpat = nptrns[p][1]
                vpf = foilpat[m][p]
                vispatf = sptrns[vpf][0]
                audsem = sfxs[1][1]
            colp = improbclnr[m][p][0]-1 # 1 or 2 so 0 or 1
            cp = clrs[0][colp]
            cs = clrs[1][colp]
            nr = nrdummy[improbclnr[m][p][1]-1]
            pic = "pictures/PNG/111100" + str(cp) + str(vismon) + str(vissem) + str(vispat) + "00.png"
            fpic = "pictures/PNG/111100" + str(cp) + str(vismon) + str(vissem) + str(vispatf) + "00.png"
            sound = "sounds/combined/11111001" + str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + str(audpat) +  '10000.wav'      
            tlist.append([pic, sound, nr, fpic, 'FCimprbitem', 4])
def FCprob(tlist, clrs, nmnstrs, smnstrs, nptrns,sptrns, sfxs):
    """generate a list of FC trials with probable NPs, with vocab, prob and number foils"""
    vocfoil = ['m', 'p', 'c','p','m','m','m','p','m','c','m','p']
    patfoil = [1,2,1,1,2,1,2,1,2,2,1,2]
    #smfoil = [4,5,3,5,6,1,6,1,2,4,2,3] old
    smfoil = [4,6,3,5,4,1,5,1,2,6,2,3]
    trtype = ['vocabitem', 'FCprobitems', 'FCnumbritem', 'FCsemanitem']
    # we're only using all four for the first 36 of these, the last 12 are for semantic trials but those changed to not have a pattern any longer. 
    colnrmonpat = [[[1,1,1,1],[1,1,3,1],[1,1,6,2],[2,2,1,2],[2,2,3,2],[2,2,6,1],[1,2,2,1],[1,2,4,2],[1,2,5,2],[2,1,2,2],[2,1,4,1], [2,1,5,1]],[[1,2,1,1],[1,2,3,1],[1,2,6,2],[2,1,1,2],[2,1,3,2],[2,1,6,1],[1,1,2,1],[1,1,4,2],[1,1,5,2],[2,2,2,2],[2,2,4,1], [2,2,5,1]],[[2,1,1,1],[2,1,3,1],[2,1,6,2],[1,2,1,2],[1,2,3,2],[1,2,6,1],[2,2,2,1],[2,2,4,2],[2,2,5,2],[1,1,2,2],[1,1,4,1], [1,1,5,1]],[[2,2,1,1],[2,2,3,1],[2,2,6,2],[1,1,1,2],[1,1,3,2],[1,1,6,1],[2,1,2,1],[2,1,4,2],[2,1,5,2],[1,2,2,2],[1,2,4,1], [1,2,5,1]]]
    random.shuffle(nmnstrs)
    random.shuffle(smnstrs)
    random.shuffle(nptrns)
    random.shuffle(sptrns)
    colourlist = list(range(2))
    random.shuffle(colourlist)
    nrdummy = ['1','2']
    random.shuffle(nrdummy)
    scmfoil = genalt(smnstrs)
    nmfoil = genalt(nmnstrs)
    for a in range(4): # through all 4 types of testtrials
        for t in range(12): # through all 12 trials
            trialtype = trtype[a]
            inf = colnrmonpat[a][t]
            c = inf[0] # 1,2
            n = inf[1] # 1,2
            m = inf[2]-1 # 1-6 so 0-5
            p = inf[3]-1 # 1-2 so 0-1
            if m < 3:
                vismon = nmnstrs[m][0] # monster pic
                audmon = nmnstrs[m][1]
                vissem = 1
                vissemf = 2
                audsem = sfxs[1][0]
                vispat = nptrns[p][0]
                audpat = nptrns[p][1]
                q = 1-p # if p is 0 q is 1 and the other way around, just picks out the other pattern of the same type
                vvispatf = nptrns[q][0]
                r = patfoil[t]-1 # 0 or 1
                ipvispatf = sptrns[r][0]
                vvismonf = nmfoil[m][0] # foil if need be for vocab
                sf = smfoil[t]-4 # 1-6 except that for nm the smfoil would always be 4-6, or - 4 it would be 0-2
                svismonf = smnstrs[sf][0]
            elif m > 2:
                l = m-3
                vissem = 2
                vissemf = 1
                vismon = smnstrs[l][0]
                audmon = smnstrs[l][1]
                audsem = sfxs[1][1]
                vispat = sptrns[p][0]
                audpat = sptrns[p][1]
                q = 1-p
                vvispatf = sptrns[q][0]
                k = patfoil[t]-1
                ipvispatf = nptrns[k][0] ### smth wrong here
                vvismonf = scmfoil[l][0]
                sf = smfoil[t]-1
                svismonf = nmnstrs[sf][0]
            cp = clrs[0][c-1] # c is 1 or 2
            cf = 3-cp
            cs = clrs[1][c-1]
            nr = nrdummy[n-1]
            pic = "pictures/PNG/111100" + str(cp) + str(vismon) + str(vissem) + str(vispat) + "00.png"
            sound = "sounds/combined/11111001" + str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + str(audpat) +  '10000.wav'    
            if a == 0: # vocabitem
                if vocfoil[t] == 'm':
                    fpic = "pictures/PNG/111100" + str(cp) + str(vvismonf) + str(vissem) + str(vispat) + "00.png"
                    trialtype = 'FCvocabmons'
                    critword = 3
                elif vocfoil[t] == 'p':
                    fpic = "pictures/PNG/111100" + str(cp) + str(vismon) + str(vissem) + str(vvispatf) + "00.png"
                    trialtype = 'FCvocabpatt'
                    critword = 4
                elif vocfoil[t] == 'c':
                    fpic = "pictures/PNG/111100" + str(cf) + str(vismon) + str(vissem) + str(vispat) + "00.png"
                    trialtype = 'FCvocabcolr'
                    critword = 2
            elif a == 1: # probable mon-pat item, so foil is improbable pattern
                fpic = "pictures/PNG/111100" + str(cp) + str(vismon) + str(vissem) + str(ipvispatf) + "00.png"
                critword = 4
            elif a == 2: # foil pic is the same, it's the nr that's diff
                fpic = "pictures/PNG/111100" + str(cp) + str(vismon) + str(vissem) + str(vispat) + "00.png"
                critword = 1
            elif a == 3:
                pic = "pictures/PNG/111000" + str(cp) + str(vismon) + str(vissem) +  "000.png"
                fpic = "pictures/PNG/111000" + str(cp) + str(svismonf) + str(vissemf) +  "000.png"
                sound = "sounds/combined/11100001" + str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + '000000.wav'
                critword = 1
            tlist.append([pic, sound, nr, fpic, trialtype, critword])
def FCvl(tlist, clrs, nmnstrs, smnstrs, nptrns, sptrns, vrbs, plnts, sfx, fcvllist):
    """generates 6 fc test trials to test verb and landscape vocab"""
    planetlist = range(3)
    verblist = range(3)
    lfoils = genalt(planetlist)
    vfoils = genalt(verblist)
    for item in fcvllist: 
        cgen = item[8]
        cp = clrs[0][cgen]
        cs = clrs[1][cgen]
        mgen = item[10]
        if item[9] == 'nice':
            vismon = nmnstrs[mgen][0]
            audmon = nmnstrs[mgen][1]
            vissem = 1
            audsem = sfx[1][0]
        elif item[9] == 'scary':
            vismon = smnstrs[mgen][0]
            audmon = smnstrs[mgen][1]
            vissem = 2
            audsem = sfx[1][1]
        pgen = item[12]
        if item[11] == 'nice':
            vispat = nptrns[pgen][0]
            audpat = nptrns[pgen][1]
        elif item[11] == 'scary':
            vispat = sptrns[pgen][0]
            audpat = sptrns[pgen][1]
        vgen = item[13]
        visverb = vrbs[0][vgen]
        audverb = vrbs[1][vgen]
        lgen = item[14]
        vislan = plnts[0][lgen]
        audlan = plnts[1][lgen]
        nr = item[15]
        cvf = vrbs[0][vfoils[vgen]] # vgen picks out which vfoil it will be
        clf = plnts[0][lfoils[lgen]] # lgen picks out which foil it will be
        pic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(vispat) + str(visverb) + str(vislan)+ 'n' + str(nr) + 'f1.png'
        sound = "sounds/combined/11111111" + str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + str(audpat) + '1' + str(audverb) + str(audsem) + str(nr) + str(audlan) + ".wav"
        if item[7] == 'FCverb\n':
            fpic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(vispat) + str(cvf) + str(vislan)+ 'n' + str(nr) + 'f1.png'
            critword = 6
            trialtype = 'FCvocabvvid'
        elif item[7] == 'FClandscape\n':
            fpic = "slides/v111111"+str(cp) + str(vismon) + str(vissem) + str(vispat) + str(visverb) + str(clf)+ 'n' + str(nr) + 'f1.png'
            critword = 7
            trialtype = 'FCvocablvid'
        tlist.append([pic, sound, nr, fpic, trialtype, critword])
def EMgenerate(tlist, clrs, nmnstrs, smnstrs, nptrns, sptrns, vrbs, plnts, sfx, emlist):
    """make error monitoring trials from input in emlist"""
    for item in emlist: 
        cgen = item[8]
        cs = clrs[1][cgen]
        mgen = item[10]
        if item[9] == 'nice':
            audmon = nmnstrs[mgen][1]
            audsem = sfx[1][0]
            audsemf = sfx[1][1]
        elif item[9] == 'scary':
            audmon = smnstrs[mgen][1]
            audsem = sfx[1][1]
            audsemf = sfx[1][0]
        pgen = item[12]
        if item[11] == 'nice':
            audpat = nptrns[pgen][1]
        elif item[11] == 'scary':
            audpat = sptrns[pgen][1]
        vgen = item[13]
        audverb = vrbs[1][vgen]
        lgen = item[14]
        audlan = plnts[1][lgen]
        nr = item[15]
        sound = "sounds/combined/11111111" + str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + str(audpat) + '1' + str(audverb) + str(audsem) + str(nr) + str(audlan) + ".wav"
        correcttrial = 1 # and set to 0 for incorrect ones.
        trialtype = item[7]
        trialtype = trialtype[:-1]
        if trialtype == 'EMimprob':
            trialtype = 'EMimpr'
        elif trialtype == 'EMswitch1':
            trialtype = 'EMsw1'
        elif trialtype == 'EMswitch2':
            trialtype = 'EMsw2'
        elif trialtype == 'EMswitch3':
            trialtype = 'EMsw3'
        elif trialtype == 'EMswitch4':
            trialtype = 'EMsw4'
        # this is all good for the correct trials (EMimprob, EMprob). For the other trials, generate the sound with the error
        # individual elements to the sentence
        det = "sounds/t1w1s" + str(audsem) + "n" +str(nr) +".wav"
        col = "sounds/t2w" + str(cs) + "s" + str(audsem) + "n" +str(nr) +".wav"
        mon = "sounds/t3w" + str(audmon) + "s" + str(audsem) + "n" +str(nr) +".wav"
        mar = "sounds/combined/0001100000000000" + str(audpat) + "10000.wav" # with ot
        mar1 = "sounds/t4w" + str(audpat) + ".wav"
        ot = "sounds/t5w1.wav"
        ver = "sounds/t6w" + str(audverb) + "s" + str(audsem) + "n" + str(nr) + ".wav"
        lan = "sounds/t7w" + str(audlan) + ".wav"
        nrf = 3-nr # so the other number
        critword = 7
        if item[7][3] == 'a' or item[7][3] == 'n':
            correcttrial = 0
            if item[7] == 'EMnadj\n':
                critword = 3
                mon = "sounds/t3w" + str(audmon) + "s" + str(audsem) + "n" +str(nrf) +".wav"
                name = "nadj1111111"+ str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nrf) + str(audpat) + str(audverb) + str(audsem) + str(nr) + str(audlan) + ".wav"
            elif item[7] == 'EMsadj\n':
                critword = 3
                mon = "sounds/t3w" + str(audmon) + "s" + str(audsemf) + "n" +str(nr) +".wav"
                name = "sadj1111111"+ str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsemf) + str(nr) + str(audpat) + str(audverb) + str(audsem) + str(nr) + str(audlan) + ".wav"        
            elif item[7] == 'EMnnadj\n':
                critword = 6
                ver = "sounds/t6w" + str(audverb) + "s" + str(audsem) + "n" + str(nrf) + ".wav"
                name = "nnadj1111111"+ str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + str(audpat) + str(audverb) + str(audsem) + str(nrf) + str(audlan) + ".wav"        
            elif item[7] == 'EMsnadj\n':
                critword = 6
                ver = "sounds/t6w" + str(audverb) + "s" + str(audsemf) + "n" + str(nr) + ".wav"
                name = "snadj1111111"+ str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + str(audpat) + str(audverb) + str(audsemf) + str(nr) + str(audlan) + ".wav"    
            sname = "data/s" + str(subjectnr) + "/errortrials/" + name
            sound6(det, col, mon, mar, ver, lan, sname) # generate the relevant soundfile
            sounddurlist.append([sname, getdur(sname), getdur(det), getdur(col), getdur(mon), getdur(mar1),getdur(ot), getdur(ver), getdur(lan)])
            sound = sname
        elif item[7][3] == 'w': # switch trials 
            correcttrial = 0
            if item[7] == 'EMswitch1\n': # 1324567 (switch monster and color) - adjacent, early, hard
                critword = 2
                name = "data/s" + str(subjectnr) + "/errortrials/1switch1111111"+ str(audsem) + str(nr) + str(audmon) + str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audpat) + str(audverb) + str(audsem) + str(nr) + str(audlan) + ".wav"       
                sound6(det,mon,col,mar,ver, lan, name)
                sounddurlist.append([name, getdur(name), getdur(det), getdur(mon), getdur(col), getdur(mar1), getdur(ot), getdur(ver), getdur(lan)])
            elif item[7] == 'EMswitch2\n': # 1273456 (put planet between color and monster) - salient
                critword = 3
                name = "data/s" + str(subjectnr) + "/errortrials/2switch1111111"+ str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr) + str(audlan) + str(audmon) + str(audsem) + str(nr) + str(audpat) + str(audverb) + str(audsem) + str(nr)  + ".wav"      
                sound6(det,col,lan, mon, mar, ver, name)
                sounddurlist.append([name, getdur(name), getdur(det), getdur(col), getdur(lan), getdur(mon), getdur(mar1), getdur(ot), getdur(ver)])
            elif item[7] == 'EMswitch3\n': # 1234657 (switch ot and verb) - late, hard
                critword = 5
                name = "data/s" + str(subjectnr) + "/errortrials/3switch1111111"+ str(audsem) + str(nr) + str(cs) + str(audsem) + str(nr)  + str(audmon) + str(audsem) + str(nr) + str(audpat) + str(audverb) + str(audsem) + str(nr) + str(audlan) + ".wav"      
                sound7(det,col, mon, mar1, ver, ot, lan, name)
                sounddurlist.append([name, getdur(name), getdur(det), getdur(col), getdur(mon), getdur(mar1), getdur(ver), getdur(ot), getdur(lan)])
            elif item[7] == 'EMswitch4\n': # 1345627 (color in between verb and planet) - salient
                critword = 2
                name = "data/s" + str(subjectnr) + "/errortrials/4switch1111111"+ str(audsem) + str(nr)  + str(audmon) + str(audsem) + str(nr)  + str(audpat) + str(audverb) + str(audsem) + str(nr)+ str(cs) + str(audsem) + str(nr) + str(audlan) + ".wav"      
                sound6(det, mon, mar, ver,col, lan, name)
                sounddurlist.append([name, getdur(name), getdur(det), getdur(mon), getdur(mar1), getdur(ot), getdur(ver), getdur(col), getdur(lan)]) 
            sound = name
        tlist.append([sound, trialtype, correcttrial, critword])
# functions to paste sounds together, only used in error monitoring to generate sentences with errors.
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
def sound7(s1,s2,s3,s4,s5,s6,s7, s8):
    """combine 7 sounds"""
    sound4(s1,s2,s3,s4, "tt1.wav")
    soundtriplet(s5,s6,s7, "tt2.wav")
    soundcombine("tt1.wav", "tt2.wav",s8)

# most instructions are in the folder 'instructions' for easy editing. # the if statement is just to be able to fold this away.
read = True
if read == True:
    g = open('instructions/activecompmessage1bcd.txt')
    activecompmessage1bcd = g.read()
    g.close()
    g = open('instructions/activecompmessage2.txt')
    activecompmessage2 = g.read()
    g.close()
    g = open('instructions/activecompmessage11.txt')
    activecompmessage11 = g.read()
    g.close()
    g = open('instructions/activeprodmessage.txt')
    activeprodmessage = g.read()
    g.close()
    g = open('instructions/activeprodmessage1.txt')
    activeprodmessage1 = g.read()
    g.close()
    g = open('instructions/activeprodmessage2.txt')
    activeprodmessage2 = g.read()
    g.close()
    g = open('instructions/combinedphrases.txt')
    combinedphrases = g.read()
    g.close()
    g = open('instructions/forcedchoicemessage.txt')
    forcedchoicemessage = g.read()
    g.close()
    g = open('instructions/openingmessagec.txt')
    openingmessagec = g.read()
    g.close()
    g = open('instructions/openingmessagep.txt')
    openingmessagep = g.read()
    g.close()
    g = open('instructions/overviewmessage.txt')
    overviewmessage = g.read()
    g.close()
    g = open('instructions/passivemessage.txt')
    passivemessage = g.read()
    g.close()
    g = open('instructions/passivemessage1.txt')
    passivemessage1 = g.read()
    g.close()
    g = open('instructions/passivemessage2.txt')
    passivemessage2 = g.read()
    g.close()
    g = open('instructions/vocabtestmessage1.txt')
    vocabtestmessage1 = g.read()
    g.close()
    g = open('instructions/endmessagec.txt')
    endmessagec = g.read()
    g.close()
    g = open('instructions/endmessagep.txt')
    endmessagep = g.read()
    g.close()

    # these instructions include unicode and are only available right here. 
    activecompmessage = u"ACTIVE LEARNING BLOCK\n\n\n\n\n[during these trials, press '\u2260' for mismatch and '=' for match]\n\n\n\n(press ENTER to start)"
    activecompmessage1a =    u"Next, we'll do an active learning round. Active learning will help you remember the words better.\n\nIn active learning, you will see a picture and hear some speech. Your job is to decide whether the picture and the speech match or not. You will press the key marked '=' on the right hand side of the keyboard if you think that the picture and speech match. If you think that they don't match, you will press the key marked '\u2260' on the left side of the keyboard.  "
    activecompmessage1 = activecompmessage1a + activecompmessage1bcd
    errormonitoringmessage = u"Let's see how well you know the language! \n\nIn this final test, you'll hear a sentence and your job is to indicate with a buttonpress whether this could be a correct sentence in the novel language or whether there's a mistake in it. Do this AS FAST AS POSSIBLE. Once you know the answer, just press the button, even if the sentence is still unfolding.\n\nPress '\u2260' for mistake and '=' for correct. In order to answer as fast as possible, keep your index fingers on the keys so that you can press a button as soon as you know the answer.\n\nSo note that you will only HEAR a sentence, you will not see a picture on the screen!\n\nThis is a long test, so there are some short breaks during the test.  \n\n\n\n(press ENTER to continue)\n."

# first, get the subjectnr and conditionnr
subjectnr = getsubjectnumber()
# get condition (1 is comp, 2 is prod)
conditionnr = getconditionnumber()
# Open a file for logging the experiment 
filename = 'data/s' + str(subjectnr) + '/log' + str(subjectnr) + '.txt'
f = open(filename, 'w') 
f.write("\ncondition =  %d" %conditionnr)

# this if statement is just to be able to fold all of the experiment generating away
setup = True
if setup == True:
    # Assign word-object mappings for this person and log them
    colors = [[1,2],[1,2],"colors", 'c',2] # colors are 1-6, these are colors, wordtype 2, total of 6
    monsters = [[1,2,3,5,6,7],[1,2,3,4,5,6], "monsters", 'm',6]
    patterns = [[1,2,3,4],[1,2,3,4], "patterns", 'p',4]
    verbs = [[1,2,3],[1,2,3], "verbs",'v',3] 
    landscapes = [[1,2,3],[1,2,3], "landscapes",'l',3] 
    suffixes = [[1,2],[1,2], "suffixes", 's', 2]
    assignlanguage(colors)
    assignlanguage(monsters)
    assignlanguage(patterns)
    assignlanguage(verbs)
    assignlanguage(landscapes)
    assignlanguage(suffixes)

    nicemonsterlist = []
    scarymonsterlist = []
    for i in range(len(monsters[0])):
        vismon = monsters[0][i]
        audmon = monsters[1][i]
        if vismon < 4:
            nicemonsterlist.append([vismon, audmon])
        elif vismon > 4:
            scarymonsterlist.append([vismon, audmon])

    nicemonsterlistshuf = []
    scarymonsterlistshuf = []
    for i in range(len(monsters[0])):
        vismon = monsters[0][i]
        audmon = monsters[1][i]
        if vismon < 4:
            nicemonsterlistshuf.append([vismon, audmon])
        elif vismon > 4:
            scarymonsterlistshuf.append([vismon, audmon])

    nicepatternlist = []
    scarypatternlist = []
    for i in range(len(patterns[0])):
        vispat = patterns[0][i]
        audpat = patterns[1][i]
        if suffixes[0][0] == 1: # nice monsters get stripy patterns
            if vispat < 3:
                nicepatternlist.append([vispat, audpat])
            elif vispat > 2:
                scarypatternlist.append([vispat, audpat])
        elif suffixes[0][0] == 2: # nice monsters get dotty patterns
            if vispat < 3:
                scarypatternlist.append([vispat, audpat])
            elif vispat > 2:
                nicepatternlist.append([vispat, audpat])

    nicepatternlistshuf = []
    scarypatternlistshuf = []
    for i in range(len(patterns[0])):
        vispat = patterns[0][i]
        audpat = patterns[1][i]
        if suffixes[0][0] == 1: # nice monsters get stripy patterns
            if vispat < 3:
                nicepatternlistshuf.append([vispat, audpat])
            elif vispat > 2:
                scarypatternlistshuf.append([vispat, audpat])
        elif suffixes[0][0] == 2: # nice monsters get dotty patterns
            if vispat < 3:
                scarypatternlistshuf.append([vispat, audpat])
            elif vispat > 2:
                nicepatternlistshuf.append([vispat, audpat])

    file = open('sounds/listofsounddurations.txt', 'r')
    sounddurlist = []
    for line in file:
        trial = line.split("\t")
        sounddurlist.append(trial)

    for it in sounddurlist:
        it[8] = it[8][:-1]
        it[0] = "sounds/" + it[0]
        itsum = 0
        for i in range(1,9):
            it[i] = float(it[i])
            if i > 1:
                itsum += it[i]
                it.append(itsum)

    subjecttriallist = 'data/s' + str(subjectnr) + '/fulltriallist.txt'
    file = open(subjecttriallist, 'r')
    fullgeneratedlist = []
    for line in file:
        trial = line.split("\t")
        if trial[1] == 'c1':
            trial.append(0)
        elif trial[1] == 'c2':
            trial.append(1)
        if trial[2] == 'm1':
            trial.append('nice')
            trial.append(0)
        elif trial[2] == 'm2':
            trial.append('nice')
            trial.append(1)
        elif trial[2] == 'm3':
            trial.append('nice')
            trial.append(2)
        elif trial[2] == 'm4':
            trial.append('scary')
            trial.append(0)
        elif trial[2] == 'm5':
            trial.append('scary')
            trial.append(1)
        elif trial[2] == 'm6':
            trial.append('scary')
            trial.append(2)
        if trial[3] == 'p1':
            trial.append('nice')
            trial.append(0)
        elif trial[3] == 'p2':
            trial.append('nice')
            trial.append(1)
        elif trial[3] == 'p3':
            trial.append('scary')
            trial.append(0)
        elif trial[3] == 'p4':
            trial.append('scary')
            trial.append(1)
        if trial[4] == 'v1':
            trial.append(0)
        elif trial[4] == 'v2':
            trial.append(1)
        elif trial[4] == 'v3':
            trial.append(2)
        if trial[5] == 'l1':
            trial.append(0)
        elif trial[5] == 'l2':
            trial.append(1)
        elif trial[5] == 'l3':
            trial.append(2)
        if trial[6] == 'n1':
            trial.append(1)
        elif trial[6] == 'n2':
            trial.append(2)
        fullgeneratedlist.append(trial)
    fullgeneratedlist.pop(0)

    exposuregeneratedlist = [x for x in fullgeneratedlist if x[7] == 'exposure\n']
    FCgeneratedlist = [x for x in fullgeneratedlist if x[7][0] == 'F']
    EMgeneratedlist = [x for x in fullgeneratedlist if x[7][1] == 'M']

    monster1 = []
    monster2 = []
    trialgenm(monster1, monsters, suffixes)
    trialgenm(monster2, monsters, suffixes) # create a copy that remains in order for forced choice vocab trials
    random.shuffle(monster1)

    color1 = []
    trialgenc(color1, colors)

    coloredmonstertrials = []
    trialgenCM(coloredmonstertrials, colors, monsters, suffixes)

    patterns1 = []
    trialgenp(patterns1, patterns)
    random.shuffle(patterns1)

    NPlist = []
    trialgenNP(NPlist, colors, nicemonsterlistshuf, scarymonsterlistshuf, nicepatternlistshuf, scarypatternlistshuf, suffixes)

    verbs1 = []
    trialgenv(verbs1, verbs)
    landscapes1 = []
    trialgenl(landscapes1, landscapes)

    vl = []
    attachalt(vl, verbs1)
    attachalt(vl, landscapes1)

    ftlist = trialgenfull(colors, nicemonsterlist, scarymonsterlist, nicepatternlist, scarypatternlist, verbs, landscapes, suffixes, exposuregeneratedlist)
    plist = ftlist[0]
    alist = ftlist[1]

    vocabtesttrials = []
    # pick half plural for the monster vocab trials
    mpldummy = list(range(6))
    random.shuffle(mpldummy)
    nmvocab = []
    smvocab = []
    for i in range(6):
        pic = monster2[i][0]
        if mpldummy[i] % 2 == 0: # if singular
            pl = '1'
            snd = monster2[i][1]
        elif mpldummy[i] % 2 == 1: # if plural
            pl = '2'
            snd = monster2[i][4] # plural sound
        if monster2[i][5] == 1: #vissem
            nmvocab.append([pic, snd, 'm', pl])
        elif monster2[i][5] == 2:
            smvocab.append([pic, snd, 'm', pl])
    attachalt(vocabtesttrials, nmvocab) # so that foils for nice monsters are nice monsters
    attachalt(vocabtesttrials, smvocab) # so that foils for scary monsters are scary monsters
    attachalt(vocabtesttrials, color1)
    attachalt(vocabtesttrials, patterns1)
    attachalt(vocabtesttrials, verbs1)
    attachalt(vocabtesttrials, landscapes1)
    random.shuffle(vocabtesttrials) 

    FClist = []
    FCvl(FClist, colors, nicemonsterlist, scarymonsterlist, nicepatternlist, scarypatternlist, verbs, landscapes, suffixes, FCgeneratedlist)
    FCprob(FClist, colors, nicemonsterlistshuf, scarymonsterlistshuf, nicepatternlistshuf, scarypatternlistshuf, suffixes) # 48 probable monster-pattern combi trials with diff foils depending on what we're testing here
    FCimprob(FClist, colors, nicemonsterlistshuf, scarymonsterlistshuf, nicepatternlistshuf, scarypatternlistshuf, suffixes) # 12 improbable monster-pattern combi trials, foil is always other type of patterns
    random.shuffle(FClist) 

    errorlist = []
    EMgenerate(errorlist, colors, nicemonsterlist, scarymonsterlist, nicepatternlist, scarypatternlist, verbs, landscapes, suffixes, EMgeneratedlist)

    random.shuffle(errorlist)

    for it in sounddurlist:
        itsum = 0
        for i in range(1,9):
            if i > 1:
                itsum += it[i]
                it.append(itsum)

# here, pick out as the experimenter what blocks you want to see (works only if subjnr == 1)
# default it plays nothing if subjectnr is 1 (all set to 0), so set to 1 the ones you want to play
# the if statement is just to be able to fold it
show = True
if show == True:
    showtrial = []
    showtrial.append(0) # 6 trials monster singular passive
    showtrial.append(0) # 6 trials monster singular active comprehension 1
    showtrial.append(0) # 6 trials monster singular active comprehension 2
    showtrial.append(0) # 6 trials monster singular active production 1
    showtrial.append(0) # 6 trials monster singular active production 2
    showtrial.append(0) # 6 trials monster plural passive
    showtrial.append(0) # 6 trials monster plural active comprehension 1
    showtrial.append(0) # 6 trials monster plural active comprehension 2
    showtrial.append(0) # 6 trials monster plural active production 1
    showtrial.append(0) # 6 trials monster plural active production 2
    showtrial.append(0) # 2 trials color passive
    showtrial.append(0) # 2 trials color active comprehension
    showtrial.append(0) # 2 trials color active production
    showtrial.append(0) # 6 trials colored monsters passive
    showtrial.append(0) # 6 trials colored monsters active comprehension
    showtrial.append(0) # 6 trials colored monsters active production
    showtrial.append(0) # 4 trials pattern passive
    showtrial.append(0) # 4 trials pattern active comprehension
    showtrial.append(0) # 4 trials pattern active production
    showtrial.append(0) # 2*6 = 12 trials full NP passive
    showtrial.append(0) # 2*6 = 12 trials full NP active comprehension
    showtrial.append(0) # 2*6 = 12 trials full NP active production
    showtrial.append(0) # 6 trials verb/landscape passive
    showtrial.append(0) # 6 trials verb/landscape active comprehension 1
    showtrial.append(0) # 6 trials verb/landscape active comprehension 2
    showtrial.append(0) # 6 trials verb/landscape active production 1
    showtrial.append(0) # 6 trials verb/landscape active production 2
    showtrial.append(0) # 6*6 = 36 trial full sentence passive
    showtrial.append(0) # 6*6 = 36 trial full sentence active comprehension
    showtrial.append(0) # 6*6 = 36 trial full sentence active production
    showtrial.append(0) # 18 trials vocabulary noun test forced choice
    showtrial.append(0) # 66 trials forced choice
    showtrial.append(0) # 124 error monitoring trials

# make sure that for real subject numbers it always shows all trials
if subjectnr > 1:
    for k in range(len(showtrial)):
        showtrial[k] = 1
print (showtrial)
# Define the window that the experiment will be run in. In a lot of psychopy functions you will see this window as the first argument, there we tell it to draw stuff in this window.
win = visual.Window(fullscr = False, color = 'white', units = 'pix', size = [1200,700], allowGUI = None)
trialnr = 1

# this is cause the mic doesn't work on my laptop
if subjectnr > 2:
    microphone.switchOn(sampleRate=16000)


# Opening screen
if conditionnr == 1:
    showmessage(win, openingmessagec)
elif conditionnr == 2:
    showmessage(win, openingmessagep)
showmessage(win, overviewmessage)
now = time.strftime("%c")
f.write("\n\nThey started the experiment at \t\t" + time.strftime("%c") + '\n\n')

# this list will keep track of nr of correct active comp trials per block during training
activecompcorrect = []

f.write("\n\nsubjectnr\tconditionnr\ttrialnr\ttrialtype\titemtype\tcorrectanswer?\tkey\tmatch/mismatch\tRT\tsound\tpic\tfoilpic\n")


# Explanation of passive learning trals
# 1 word vocab learning trials
showmessage(win, passivemessage1)
showmessage(win, passivemessage)
# Play a round of singular passive noun learning trials
for t in monster1:
    if showtrial[0] == 1:
        passivetrial(win, t[0], t[1])
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "P\tmsg\t-\t-\t-\t-\t" + t[1] + "\t" + t[0] + "\t-\n") 
    # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm, RT and foilpic are not applicable here! 
    trialnr = trialnr + 1
showmessage(win,passivemessage2)
if conditionnr == 1:
    showmessage(win, activecompmessage1)
    if subjectnr > 1:
        k = activecomptrial(win, "pictures/cat.png", "pictures/cat.png", "sounds/cat.wav")
    showmessage(win, "Great, let's do another practice trial. \n\n\n\n(press ENTER to continue)")
    if subjectnr > 1:
        k = activecomptrial(win, "pictures/cat.png", "pictures/dog.png", "sounds/dog.wav")
    showmessage(win, activecompmessage11)
    showmessage(win, activecompmessage)
    if showtrial[1] == 1:
        trialnr = activecompblock(monster1, trialnr, 'msg')
    random.shuffle(monster1)
    if showtrial[2] == 1:
        trialnr = activecompblock(monster1, trialnr, 'msg')
    showmessage(win, activecompmessage2)
elif conditionnr == 2:
    showmessage(win, activeprodmessage1)
    # Explanation of active production learning trial
    showmessage(win, activeprodmessage)
    # Play an active production learning trial
    random.shuffle(monster1)
    for t in monster1:
        if showtrial[3] == 1:
            info = activeprodtrial(win, t[0], t[1])
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tmsg\t-\t-\t-\t" + str(info) + "\t" + t[1] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
        trialnr = trialnr + 1
    random.shuffle(monster1)
    for t in monster1:
        if showtrial[4] == 1:
            info = activeprodtrial(win, t[0], t[1])
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tmsg\t-\t-\t-\t" + str(info) + "\t" + t[1] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here!
        trialnr = trialnr + 1
    showmessage(win, activeprodmessage2)

showmessage(win, passivemessage)
random.shuffle(monster1) # now just pick the plural sound
for t in monster1:
    if showtrial[5] == 1:
        passivetrial(win, t[0], t[4], pl = '2')
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "P\tmpl\t-\t-\t-\t-\t" + t[4] + "\t" + t[0] + "\t-\n") 
    # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm, RT and foilpic are not applicable here! 
    trialnr = trialnr + 1   

if conditionnr == 1:
    random.shuffle(monster1)
    showmessage(win, activecompmessage)
    if showtrial[6] == 1:
        trialnr = activecompblock(monster1, trialnr, 'mpl', pl = '2')
    random.shuffle(monster1)
    if showtrial[7] == 1:
        trialnr = activecompblock(monster1, trialnr, 'mpl', pl = '2')
elif conditionnr == 2:
    # Explanation of active production learning trial
    showmessage(win, activeprodmessage)
    # Play an active production learning trial
    random.shuffle(monster1)
    for t in monster1:
        if showtrial[8] == 1:
            info = activeprodtrial(win, t[0], t[4], pl = '2')
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tmpl\t-\t-\t-\t" + str(info) + "\t" + t[4] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
        trialnr = trialnr + 1
    random.shuffle(monster1)
    for t in monster1:
        if showtrial[9] == 1:
            info = activeprodtrial(win, t[0], t[4], pl = '2')
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tmpl\t-\t-\t-\t" + str(info) + "\t" + t[4] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
        trialnr = trialnr + 1

# a block of color nouns 
showmessage(win, passivemessage)
random.shuffle(color1)
for t in color1:
    if showtrial[10] == 1:
        passivetrial(win, t[0], t[1])
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "P\tc\t-\t-\t-\t-\t" + t[1] + "\t" + t[0] + "\t-\n") 
    # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm, RT and foilpic are not applicable here! 
    trialnr = trialnr + 1

if conditionnr == 1:
    showmessage(win, activecompmessage)
    if showtrial[11] == 1:
        trialnr = activecompblock(color1, trialnr, 'c')
elif conditionnr == 2:
    # Explanation of active production learning trial
    showmessage(win, activeprodmessage)
    # Play an active production learning trial
    random.shuffle(color1)
    for t in color1:
        if showtrial[12] == 1:
            info = activeprodtrial(win, t[0], t[1])
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tc\t-\t-\t-\t" + str(info) + "\t" + t[1] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
        trialnr = trialnr + 1

#    now do colored monsters
showmessage(win, combinedphrases)
passivernd = coloredmonstertrials[0]
showmessage(win, passivemessage)
random.shuffle(passivernd)
for t in passivernd:
    if showtrial[13] == 1:
        passivetrial(win, t[1], t[4], pl = str(t[8]))
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" %trialnr + "P\tcm\t-\t-\t-\t-\t" + t[4] + "\t" + t[1] + "\t-\n") 
    # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm, RT and foilpic are not applicable here! 
    trialnr = trialnr + 1   

activernd = coloredmonstertrials[1]
if conditionnr == 1:
    showmessage(win, activecompmessage)
    random.shuffle(activernd)
    tc = 0
    for t in activernd:
        info = ['none', 0]
        if showtrial[14] == 1:
            info = activecomptrial(win,t[9],t[1], t[4], pl = str(t[8]))
        key = info[0]
        m = 'mismatch'
        ck = 'none'
        if t[9] == t[1]:
            m = 'yesmatch'
        if m == 'mismatch':
            if key == 'l':
                ck = '0'
            elif key == 'f':
                ck = '1'
                tc = tc + 1
        if m == 'yesmatch':
            if key == 'f':
                ck = '0'
            elif key == 'l':
                ck = '1'
                tc = tc + 1
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AC\tcm\t"+ ck + "\t" + key + "\t" + m + "\t" + str(info[1]) + "\t" + t[4] + "\t" + t[1] + "\t" + t[9] + "\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
        trialnr = trialnr + 1
    activecompcorrect.append([tc,'cm'])
elif conditionnr == 2:
    # Explanation of active production learning trial
    showmessage(win, activeprodmessage)
    # Play an active production learning trial
    random.shuffle(activernd)
    for t in activernd:
        if showtrial[15] == 1:
            info = activeprodtrial(win, t[1], t[4], pl = str(t[8]))
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tcm\t-\t-\t-\t" + str(info) + "\t" + t[4] + "\t" + t[1] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
        trialnr = trialnr + 1

# block of markings
showmessage(win, passivemessage)
for t in patterns1:
    if showtrial[16] == 1:
        passivetrial(win, t[0], t[1])
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "P\tp\t-\t-\t-\t-\t" + t[1] + "\t" + t[0] + "\t-\n") 
    # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm, RT and foilpic are not applicable here! 
    trialnr = trialnr + 1
if conditionnr == 1:
    showmessage(win, activecompmessage)
    if showtrial[17] == 1:
        trialnr = activecompblock(patterns1, trialnr, 'p')
elif conditionnr == 2:
    # Explanation of active production learning trial
    showmessage(win, activeprodmessage)
    # Play an active production learning trial
    random.shuffle(patterns1)
    for t in patterns1:
        if showtrial[18] == 1:
            info = activeprodtrial(win, t[0], t[1])
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tp\t-\t-\t-\t" + str(info) + "\t" + t[1] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
        trialnr = trialnr + 1

# full NPs
for r in range(4):
    round = NPlist[r]
    if r % 2 == 0:
        showmessage(win, passivemessage)
        random.shuffle(round)
        for t in round:
            if showtrial[19] == 1:
                passivetrial(win, t[0], t[4], pl = str(t[8]))
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "P\tNP\t-\t-\t-\t-\t" + t[4] + "\t" + t[0] + "\t-\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm, RT and foilpic are not applicable here! 
            trialnr = trialnr + 1   
    elif r % 2 == 1:
        if conditionnr == 1:
            showmessage(win, activecompmessage)
            random.shuffle(round)
            tc = 0
            for t in round:
                info = ['none', 0]
                if showtrial[20] == 1:
                    info = activecomptrial(win,t[9],t[0], t[4], pl = str(t[8]))
                key = info[0]
                m = 'mismatch'
                ck = 'none'
                if t[9] == t[0]:
                    m = 'yesmatch'
                if m == 'mismatch':
                    if key == 'l':
                        ck = '0'
                    elif key == 'f':
                        ck = '1'
                        tc = tc + 1
                if m == 'yesmatch':
                    if key == 'f':
                        ck = '0'
                    elif key == 'l':
                        ck = '1'
                        tc = tc + 1
                f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AC\tNP\t"+ ck + "\t" + key + "\t" + m + "\t" + str(info[1]) + "\t" + t[4] + "\t" + t[0] + "\t" + t[9] + "\n") 
                # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
                trialnr = trialnr + 1
            activecompcorrect.append([tc,'NP'])
        elif conditionnr == 2:
            # Explanation of active production learning trial
            showmessage(win, activeprodmessage)
            # Play an active production learning trial
            random.shuffle(round)
            for t in round:
                if showtrial[21] == 1:
                    info = activeprodtrial(win, t[0], t[4], pl = str(t[8]))
                f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tNP\t-\t-\t-\t" + str(info) + "\t" + t[4] + "\t" + t[0] + "\t-\n") 
                # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
                trialnr = trialnr + 1

# landscapes and verbs
showmessage(win, passivemessage)
random.shuffle(vl)
for t in vl:
    vd = 'no'
    if t[2] == 'v':
        vd = 'yes'
    if showtrial[22] == 1:
        passivetrial(win, t[0], t[1], vid = vd)
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "P\t" + t[2] +"\t-\t-\t-\t-\t" + t[1] + "\t" + t[0] + "\t-\n") 
    # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm, RT and foilpic are not applicable here!
    trialnr = trialnr + 1

if conditionnr == 1:
    showmessage(win, activecompmessage)
    random.shuffle(vl)
    picknonmatch = range(len(vl))
    random.shuffle(picknonmatch) # random shuffle to pick which half of the trials get to be mismatch
    tc = 0
    for t in range(len(vl)):
        trial = vl[t]
        ck = 'none'
        vd = 'no'
        if trial[2] == 'v':
            vd = 'yes'
        if picknonmatch[t] < len(vl)/2:# match
            if showtrial[23] == 1:
                info = activecomptrial(win, trial[0],trial[0], trial[1], vid = vd)
            if key == 'l':
                ck = '1'
                tc = tc + 1
            elif key == 'f':
                ck = '0'
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AC\t" + trial[2] + "\t"+ ck + "\t" + key + "\tyesmatch\t" + str(info[1]) + "\t" + trial[1] + "\t" + trial[0] + "\t" + trial[0] + "\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
        else: # mismatch
            if showtrial[23] == 1:
                info = activecomptrial(win, trial[4], trial[0], trial[1], vid = vd)
                key = info[0]
            if key == 'f':
                ck = '1'
                tc = tc + 1
            elif key == 'l':
                ck = '0'
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AC\t" + trial[2] + "\t"+ ck + "\t" + key + "\tmismatch\t" + str(info[1]) + "\t" + trial[1] + "\t" + trial[0] + "\t" + trial[4] + "\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
        trialnr = trialnr + 1
    activecompcorrect.append([tc, 'vl'])
    tc = 0
    random.shuffle(vl)
    picknonmatch = range(len(vl))
    random.shuffle(picknonmatch) # random shuffle to pick which half of the trials get to be mismatch
    for t in range(len(vl)):
        trial = vl[t]
        ck = 'none'
        vd = 'no'
        if trial[2] == 'v':
            vd = 'yes'
        if picknonmatch[t] < len(vl)/2:# match
            if showtrial[24] == 1:
                info = activecomptrial(win, trial[0],trial[0], trial[1], vid = vd)
                key = info[0]
            if key == 'l':
                ck = '1'
                tc = tc + 1
            elif key == 'f':
                ck = '0'
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AC\t" + trial[2] + "\t"+ ck + "\t" + key + "\tyesmatch\t" + str(info[1]) + "\t" + trial[1] + "\t" + trial[0] + "\t" + trial[0] + "\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
        else: # mismatch
            if showtrial[24] == 1:
                info = activecomptrial(win, trial[4], trial[0], trial[1], vid = vd)
                key = info[0]
            if key == 'f':
                ck = '1'
                tc = tc + 1
            elif key == 'l':
                ck = '0'
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AC\t" + trial[2] + "\t"+ ck + "\t" + key + "\tmismatch\t" + str(info[1]) + "\t" + trial[1] + "\t" + trial[0] + "\t" + trial[4] + "\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
        trialnr = trialnr + 1
    activecompcorrect.append([tc, 'vl'])
elif conditionnr == 2:
    # Explanation of active production learning trial
    showmessage(win, activeprodmessage)
    # Play an active production learning trial
    random.shuffle(vl)
    for t in vl:
        vd = 'no'
        if t[2] == 'v':
            vd = 'yes'
        if showtrial[25] == 1:
            info = activeprodtrial(win, t[0], t[1], vid = vd)
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\t" + t[2] +"\t-\t-\t-\t" + str(info) + "\t" + t[1] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
        trialnr = trialnr + 1
    random.shuffle(vl)
    for t in vl:
        vd = 'no'
        if t[2] == 'v':
            vd = 'yes'
        if showtrial[26] == 1:
            info = activeprodtrial(win, t[0], t[1], vid = vd)
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\t" + t[2] +"\t-\t-\t-\t" + str(info) + "\t" + t[1] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here! 
        trialnr = trialnr + 1

for r in range(6):
    passivetriallist = plist[r]
    random.shuffle(passivetriallist)
    showmessage(win, passivemessage)
    for t in passivetriallist:
        if showtrial[27] == 1:
            passivetrial(win, t[0], t[1], vid = 'yes')
        f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "P\tfull\t-\t-\t-\t-\t" + t[1] + "\t" + t[0] + "\t-\n") 
        # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm, RT and foilpic are not applicable here!
        trialnr = trialnr + 1    
    activetriallist = alist[r]
    random.shuffle(activetriallist)
    if conditionnr == 1:
        showmessage(win, activecompmessage)
        tc = 0
        for t in activetriallist:
            info = ['none', 0]
            if showtrial[28] == 1:
                info = activecomptrial(win,t[2],t[0], t[1], vid = 'yes')
                key = info[0]
            m = 'mismatch'
            ck = 'none'
            if t[2] == t[0]:
                m = 'yesmatch'
            if m == 'mismatch':
                if key == 'l':
                    ck = '0'
                elif key == 'f':
                    ck = '1'
                    tc = tc + 1
            if m == 'yesmatch':
                if key == 'f':
                    ck = '0'
                elif key == 'l':
                    ck = '1'
                    tc = tc + 1
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AC\tfull\t"+ ck + "\t" + key + "\t" + m +"\t" + str(info[1]) + "\t" + t[1] + "\t" + t[0] + "\t" + t[2] + "\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; 
            trialnr = trialnr + 1
        activecompcorrect.append([tc, 'full'])
    elif conditionnr == 2:
        # Explanation of active production learning trial
        showmessage(win, activeprodmessage)
        # Play an active production learning trial
        for t in activetriallist:
            if showtrial[29] == 1:
                info = activeprodtrial(win, t[0], t[1], vid = 'yes')
            f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + "AP\tfull\t-\t-\t-\t" + str(info) + "\t" + t[1] + "\t" + t[0] + "\t-\n") 
            # log: subjnr, condnr, trialnr, trialtype, itemtype, correct?, key, match/mismatch, RT, sound, pic, foilpic; note that correct, key, m/mm and foilpic are not applicable here!
            trialnr = trialnr + 1

f.write("\n\nsubjectnr\tconditionnr\ttrialnr\ttrialtype\titemtype\tcorrectanswer?\tkey\tlocationcorrectanswer\tRT\ttotsounddur\tsound\tpic\tfoilpic\n")

# vocabulary test
showmessage(win, vocabtestmessage1)
nrvocabtestcorrect = 0
ttype = 'VT'
for t in vocabtesttrials:
    pl = '1'
    vid = 'no'
    if t[2] == 'v': # for verbs we need it to be a video
        vid = 'yes'
    if t[2] == 'm': # for monsters we need to know the plurality
        pl = t[3]
    corr = t[0]
    foil = t[4]
    shuf = [corr, foil]
    random.shuffle(shuf) # randomly decide which one is left and which one is right
    leftp = shuf[0]
    rightp = shuf[1]
    info = ['n', 0]
    if showtrial[30] == 1:
        info = forcedchoicetesttrial(win, leftp, rightp, t[1], pl, vid)
    crct = 0
    if leftp == corr:
        correct = 'left'
        if info[0] == 'x':
            crct = 1
            nrvocabtestcorrect = nrvocabtestcorrect + 1
    elif rightp == corr:
        correct = 'right'    
        if info[0] == 'm':
            crct = 1
            nrvocabtestcorrect = nrvocabtestcorrect + 1
    snd = t[1]
    snddurs = getdurs(snd)
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + ttype + "\t" + t[2] + "\t" + str(crct) + "\t" + info[0] + "\t" + correct + "\t" + str(info[1]) + "\t" + str(snddurs[1]) + "\t" + t[1] + "\t" + t[0] + "\t" + t[4] + "\n") 
    # log: subjnr, condnr, trialnr, trialtype, trialtype within test, correct?, key, location correct answer, RT, sounddur, sound, correctpic, foilpic; 
    trialnr = trialnr + 1

f.write("\n\nsubjectnr\tconditionnr\ttrialnr\ttrialtype\titemtype\tcorrectanswer?\tkey\tlocationcorrectanswer\tRT\tcritword\twordduringwhichtheypressed\ttotaltime\ttimew1\ttimew2\ttimew3\ttimew4\ttimew5\ttimew6\ttimew7\tcumtimew1\tcumtimew2\tcumtimew3\tcumtimew4\tcumtimew5\tcumtimew6\tcumtimew7\tsound\tpic\tfoilpic\n")

# forced choice test
showmessage(win, forcedchoicemessage)
ttype = 'FC'
nrfctestcorrect = 0
for t in FClist:
    nr = t[2]
    corr = t[0]
    foil = t[3]
    shuf = [corr, foil]
    random.shuffle(shuf) # randomly decide which one is left and which one is right
    leftp = shuf[0]
    rightp = shuf[1]
    info = ['n', 0]
    vidfctrial = 'no'
    if t[4] == 'FCvocabvvid' or t[4] == 'FCvocablvid':
        vidfctrial = 'yes'
        nr = '1' # this is icky. I am just setting it to 1 because if i set this to 2 it flips out in terms of playing videos. Nr might be 1 or 2 actually (see t[2])...
    if t[4] == 'FCnumbritem':
        side = ['l', 'r']
        random.shuffle(side)
        if side[0] == 'l':
            nr = '3'
        elif side[0] == 'r':
            nr = '4'
    if showtrial[31] ==  1:
        info = forcedchoicetesttrial(win, leftp, rightp, t[1], pl=nr, vid = vidfctrial )
    crct = 0
    if t[4] != 'FCnumbritem':
        if leftp == corr:
            correct = 'left'
            if info[0] == 'x':
                crct = 1
                nrfctestcorrect = nrfctestcorrect + 1
        elif rightp == corr:
            correct = 'right'    
            if info[0] == 'm':
                crct = 1
                nrfctestcorrect = nrfctestcorrect + 1
    elif t[4] == 'FCnumbritem':
        if t[2] == '1': # correct answer was sg
            if nr == '3': # pl was on left
                correct = 'right'
                if info[0] == 'm':
                     crct = 1
                     nrfctestcorrect = nrfctestcorrect + 1
            elif nr == '4': # pl was on right
                correct = 'left'
                if info[0] == 'x':
                    crct = 1
                    nrfctestcorrect = nrfctestcorrect + 1
        if t[2] == '2': # correct answer was pl
            if nr == '3': # pl was on left
                correct = 'left'
                if info[0] == 'x':
                     crct = 1
                     nrfctestcorrect = nrfctestcorrect + 1
            elif nr == '4': # pl was on right
                correct = 'right'
                if info[0] == 'm':
                    crct = 1
                    nrfctestcorrect = nrfctestcorrect + 1        
    snd = t[1]
    snddurs = getdurs(snd)
    snddurstr = str(snddurs[1])
    respondedduringword = 1
    for g in range(2, 16):
        snddurstr = snddurstr + "\t"  + str(snddurs[g])
        if g > 8: # cumulative times
            if snddurs[g] < info[1]:
                respondedduringword = g-7 # if this is 8 they responded after the end of the sentence    
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + ttype + "\t" + t[4] + "\t" + str(crct) + "\t" + info[0] + "\t" + correct + "\t" + str(info[1]) + "\t" + str(t[5])+ "\t" + str(respondedduringword) + "\t" + snddurstr + "\t" + t[1] + "\t" + t[0] + "\t" + t[3] + "\n") 
    # log: subjnr, condnr, trialnr, trialtype, trialtype within test, correct?, key, location correct answer, RT, critical word, word during which they pressed, breakdown of times, sound, correctpic, foilpic; 
    trialnr = trialnr + 1
    if trialnr == 214:
        showmessage(win, "You are now 1/3 through this test. Press ENTER when you're ready to continue the test.")
    elif trialnr == 236: 
        showmessage(win, "You are now 2/3 through this test. Press ENTER when you're ready to continue the test.")

f.write("\n\nsubjectnr\tconditionnr\ttrialnr\ttrialtype\titemtype\tcorrectanswer?\tkey\twassoundcorrect?\tRT\tcritword\twordduringwhichtheypressed\ttotaltime\ttimew1\ttimew2\ttimew3\ttimew4\ttimew5\ttimew6\ttimew7\tcumtimew1\tcumtimew2\tcumtimew3\tcumtimew4\tcumtimew5\tcumtimew6\tcumtimew7\tsound\n")

# error monitoring test
ttype = 'EM'
showmessage(win, errormonitoringmessage)
nrerrortestcorrect = 0
for t in errorlist:
    if showtrial[32] == 1:
        info = errormonitoringtesttrial(win, t[0])
    crct = 0
    if info[0] == 'f': # they pressed 'wrong'
        if t[2] == 0: # sentence was wrong
            crct = 1
            nrerrortestcorrect = nrerrortestcorrect + 1
    elif info[0] == 'l':
        if t[2] == 1:
            crct = 1
            nrerrortestcorrect = nrerrortestcorrect + 1
    snd = t[0]
    snddurs = getdurs(snd)
    snddurstr = str(snddurs[1])
    respondedduringword = 1
    for g in range(2, 16):
        snddurstr = snddurstr + "\t"  + str(snddurs[g])
        if g > 8: # cumulative times
            if snddurs[g] < info[1]:
                respondedduringword = g-7 # if this is 8 they responded after the end of the sentence
    f.write("%d\t" %subjectnr +"%d\t" %conditionnr + "%d\t" % trialnr + ttype + "\t" + t[1] + "\t" + str(crct) + "\t" + info[0] + "\t" + str(t[2]) + "\t" + str(info[1]) + "\t" + str(t[3])+ "\t" + str(respondedduringword) + "\t" + snddurstr + "\t" + t[0]  + "\n") # print what key they pushed
    # log: subjnr, condnr, trialnr, trialtype, trialtype within test, correct?, key, correct trial?, RT, critical word, word during which they pressed, breakdown of times, sound; 
    trialnr = trialnr + 1
    if trialnr == 283:
        showmessage(win, "You are now 1/5 through this test. Press ENTER when you're ready to continue the test.")
    elif trialnr == 308: 
        showmessage(win, "You are now 2/5 through this test. Press ENTER when you're ready to continue the test.")
    elif trialnr == 333: 
        showmessage(win, "You are now 3/5 through this test. Press ENTER when you're ready to continue the test.")
    elif trialnr == 358: 
        showmessage(win, "You are now 4/5 through this test. Press ENTER when you're ready to continue the test.")

# log time + how much they got correct in the three tests at the end
now = time.strftime("%c")
f.write("\n\nTime they got to questionnaire\t\t" + time.strftime("%c"))
f.write("\n total nr of correct vocabularytesttrials was \n%d\n" %nrvocabtestcorrect)
f.write("\n total nr of correct forcedchoicetrials was \n%d\n" %nrfctestcorrect)
f.write("\n total nr of correct errormonitoringtrials was \n%d\n" %nrerrortestcorrect)

if conditionnr == 1:
    for it in activecompcorrect:
        itemtype = it[1]
        correct = it[0]
        score = "\n\n\n total nr correct in " + itemtype + " trials was " + str(correct)
        f.write(score)

f.write("\ntotal nr possible correct trials: msg = 6, msg = 6, mpl = 6, mpl = 6, c = 2, cm = 6, p = 4, NP = 6, NP = 6, vl = 6, vl = 6, full = 6, full = 6, full = 6, full = 6, full = 6, full = 6")



# debrief
if conditionnr == 1:
    showmessage(win, endmessagec)
elif conditionnr == 2:
    showmessage(win, endmessagep)
    

# if you want webbrowser to pop up automatically - right now experimenter just sets it up by hand in browser
#webbrowser.open('https://uwmadison.co1.qualtrics.com/jfe/form/SV_d5SH7T9oWB98CvH')

# turn of the mic
if subjectnr > 2:
    microphone.switchOff()

# close stuff
f.close()
sys.exit()
