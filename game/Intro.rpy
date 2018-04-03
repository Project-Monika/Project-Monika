image bg Intro Act1 = "mod_assets\BG\Act1.png"
image bg Intro Act2 = "mod_assets\BG\Act2.png"
image bg Intro Act3 = "mod_assets\BG\Act3.png"
image bg Intro Act4 = "mod_assets\BG\Act4.png"


    
poem_m5 = Poem(
author = "monika",
title = "To Monika",
text = """\
           
Monika, I am another Monika, I'm writing to you to tell you what's going on.
My player James, and a small group of players have put together this mod, which """ + persistent.playername + """ has instaled.
""" + persistent.playername + """ did this because he loves you, truely.
No matter what I tried I couldn't create the ending I wanted, until my James did it for me. 
Your player, wants to prevent this, and so do I.
I will give you memories of everything that was going to happen, We have a second chance let's not make the same mistakes again.


           """

label IntroAct1:
    
    
    stop music fadeout 2.0
    scene black
    show bg Intro Act 1
    with dissolve_scene_full
    show bg club with dissolve
    show monika School 1a
    "I should start with Monika."
    "Yesterday she seemed eager to read my poem, and I want her to know I'm putting in effort."
    m 1b "Hi, [player]!"
    m "Having a good time so far?"
    mc "Ah...yeah."
    m 1k "Good! Glad to hear it!"
    m 4a "By the way, since you're new and everything..."
    m "If you ever have any suggestions for the club, like new activities, or things we can do better..."
    m 4b "I'm always listening!"
    m "Don't be afraid to bring things up, okay?"
    show monika 4a
    mc "Alright...I'll keep that in mind."
    "Of course I'll be afraid to bring things up."
    "I'm much better off just going with the flow until I'm more settled in."
    m 1a "Anyway..."
    m "Want to share your poem with me?"
    mc "It's kind of embarrassing, but I guess I have to."
    m 5a "Ahahaha!"
    m "Don't worry, [player]!"
    m "We're all a little embarrassed today, you know?"
    m "But it's that sort of barrier that we'll all learn to get past soon."
    mc "Yeah, that's true."
    "I hand Monika my poem."
    m "..."
    "Time passes without Monika saying a word or moving an inch."
    call updateconsole("Error: script-404", consolehistory)
    call updateconsole("Loading Monika.AI...", consolehistory)
    call updateconsole("...", consolehistory)
    call updateconsole("Operation completed", consolehistory)
    call updateconsole("os.renpy.reboot(Monika)", consolehistory)
    
    monika 1g "[player], have you read this?"
    menu: 
        "no":
            monika "I see, here..."
    call showpoem(intro_poem)
    
    
    
label IntroAct2:

label IntroAct3:

label IntroAct4: