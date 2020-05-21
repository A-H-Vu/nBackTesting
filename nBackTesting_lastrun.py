#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on May 21, 2020, at 15:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'n-back-testing'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\n-back-testing\\nBackTesting_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='In this task you will be required to press space if the white square appeared in the same location as the location on the last trial. For example if the square was in the left down corner on trial 1 and then it appeared in the same location on trial 2, press space. Otherwise, do not respond. Press space to continue.',
    font='Arial',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyResp1 = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix1 = visual.TextStim(win=win, name='fix1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
gridLines = visual.ImageStim(
    win=win,
    name='gridLines', 
    image='grid.png', mask=None,
    ori=0, pos=(0, 0), size=[0.6, 0.6],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
tarSquare = visual.Rect(
    win=win, name='tarSquare',
    width=[0.15,0.15][0], height=[0.15,0.15][1],
    ori=0.0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
fix2 = visual.TextStim(win=win, name='fix2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
keyResp2 = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='This is the end of the experiment.\nThank you for your time.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
keyResp1.keys = []
keyResp1.rt = []
_keyResp1_allKeys = []
# keep track of which components have finished
instructionsComponents = [instr, keyResp1]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr.frameNStart = frameN  # exact frame index
        instr.tStart = t  # local t and not account for scr refresh
        instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        instr.setAutoDraw(True)
    
    # *keyResp1* updates
    waitOnFlip = False
    if keyResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyResp1.frameNStart = frameN  # exact frame index
        keyResp1.tStart = t  # local t and not account for scr refresh
        keyResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyResp1, 'tStartRefresh')  # time at next scr refresh
        keyResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyResp1.status == STARTED and not waitOnFlip:
        theseKeys = keyResp1.getKeys(keyList=['space'], waitRelease=False)
        _keyResp1_allKeys.extend(theseKeys)
        if len(_keyResp1_allKeys):
            keyResp1.keys = _keyResp1_allKeys[-1].name  # just the last key pressed
            keyResp1.rt = _keyResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr.started', instr.tStartRefresh)
thisExp.addData('instr.stopped', instr.tStopRefresh)
# check responses
if keyResp1.keys in ['', [], None]:  # No response was made
    keyResp1.keys = None
thisExp.addData('keyResp1.keys',keyResp1.keys)
if keyResp1.keys != None:  # we had a response
    thisExp.addData('keyResp1.rt', keyResp1.rt)
thisExp.addData('keyResp1.started', keyResp1.tStartRefresh)
thisExp.addData('keyResp1.stopped', keyResp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = [fix1]
for thisComponent in fixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix1* updates
    if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix1.frameNStart = frameN  # exact frame index
        fix1.tStart = t  # local t and not account for scr refresh
        fix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
        fix1.setAutoDraw(True)
    if fix1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix1.tStop = t  # not accounting for scr refresh
            fix1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
            fix1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix1.started', fix1.tStartRefresh)
thisExp.addData('fix1.stopped', fix1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nBackTestingCond.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    tarSquare.setPos([loc1,loc2])
    keyResp2.keys = []
    keyResp2.rt = []
    _keyResp2_allKeys = []
    # keep track of which components have finished
    trial1Components = [gridLines, tarSquare, fix2, keyResp2]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *gridLines* updates
        if gridLines.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gridLines.frameNStart = frameN  # exact frame index
            gridLines.tStart = t  # local t and not account for scr refresh
            gridLines.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gridLines, 'tStartRefresh')  # time at next scr refresh
            gridLines.setAutoDraw(True)
        if gridLines.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gridLines.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                gridLines.tStop = t  # not accounting for scr refresh
                gridLines.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gridLines, 'tStopRefresh')  # time at next scr refresh
                gridLines.setAutoDraw(False)
        
        # *tarSquare* updates
        if tarSquare.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tarSquare.frameNStart = frameN  # exact frame index
            tarSquare.tStart = t  # local t and not account for scr refresh
            tarSquare.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tarSquare, 'tStartRefresh')  # time at next scr refresh
            tarSquare.setAutoDraw(True)
        if tarSquare.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tarSquare.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                tarSquare.tStop = t  # not accounting for scr refresh
                tarSquare.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tarSquare, 'tStopRefresh')  # time at next scr refresh
                tarSquare.setAutoDraw(False)
        
        # *fix2* updates
        if fix2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            fix2.frameNStart = frameN  # exact frame index
            fix2.tStart = t  # local t and not account for scr refresh
            fix2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
            fix2.setAutoDraw(True)
        if fix2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix2.tStop = t  # not accounting for scr refresh
                fix2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
                fix2.setAutoDraw(False)
        
        # *keyResp2* updates
        waitOnFlip = False
        if keyResp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyResp2.frameNStart = frameN  # exact frame index
            keyResp2.tStart = t  # local t and not account for scr refresh
            keyResp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResp2, 'tStartRefresh')  # time at next scr refresh
            keyResp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyResp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyResp2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyResp2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                keyResp2.tStop = t  # not accounting for scr refresh
                keyResp2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyResp2, 'tStopRefresh')  # time at next scr refresh
                keyResp2.status = FINISHED
        if keyResp2.status == STARTED and not waitOnFlip:
            theseKeys = keyResp2.getKeys(keyList=['space'], waitRelease=False)
            _keyResp2_allKeys.extend(theseKeys)
            if len(_keyResp2_allKeys):
                keyResp2.keys = _keyResp2_allKeys[-1].name  # just the last key pressed
                keyResp2.rt = _keyResp2_allKeys[-1].rt
                # was this correct?
                if (keyResp2.keys == str(corrAns)) or (keyResp2.keys == corrAns):
                    keyResp2.corr = 1
                else:
                    keyResp2.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('gridLines.started', gridLines.tStartRefresh)
    trials.addData('gridLines.stopped', gridLines.tStopRefresh)
    trials.addData('tarSquare.started', tarSquare.tStartRefresh)
    trials.addData('tarSquare.stopped', tarSquare.tStopRefresh)
    trials.addData('fix2.started', fix2.tStartRefresh)
    trials.addData('fix2.stopped', fix2.tStopRefresh)
    # check responses
    if keyResp2.keys in ['', [], None]:  # No response was made
        keyResp2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           keyResp2.corr = 1;  # correct non-response
        else:
           keyResp2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('keyResp2.keys',keyResp2.keys)
    trials.addData('keyResp2.corr', keyResp2.corr)
    if keyResp2.keys != None:  # we had a response
        trials.addData('keyResp2.rt', keyResp2.rt)
    trials.addData('keyResp2.started', keyResp2.tStartRefresh)
    trials.addData('keyResp2.stopped', keyResp2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thanks]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
