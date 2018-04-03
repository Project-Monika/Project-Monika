# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.
init python:
    #import enum
    #import math
    import MonikaAI
label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ a_name = "Amy"
    
    
    
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ AI = MonikaAI.AIManager()
    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    if persistent.FirstRun:
         call import_ddlc_persistent
         call IntroAct1
    
    if persistent.playthrough == 0:
        #Call example script
        call Space_Room

    if persistent.playthrough == 1:
        #Stuff here will only play after you increased the playthrough count
        
        call Space_Room
        pass

    return


label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
