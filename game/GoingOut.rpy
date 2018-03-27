label StartTrip:
    m 2a "That sounds wonderful, [player]."
    $ Has_Swimware = False
    if True: #persistent.UnlockedOutfits[5]
        m 5a "Am I going to need my bathing suit [player]?"
        menu:
            "Yes!":
                $ Has_Swimware = True
                m 5k "Ahah~ Okay, I'll go get it."
                $ AI.MoodChange("Romantic", 5)
            "No":
                m 1sb "Okay, but surely you want to see me in it?"
                m "I'm just teasing you, [player]"
    m 2b "Let's go!"
    show bg house
    m 2h "Right, now where's the nearest bus stop again?"
    m 4b "Ah! Yes, this way."
    show bg BusStop
    m 1a "Here we are, so where are we going today?"
    $ Choice = ""
    if Has_Swimware:
        menu:
            "We could go to the Shopping Centre":
                $ Choice = "Shoping"
            "We could go to a Cafe":
                $ Choice = "Cafe"
            "We could go to the Beach":
                $ Choice = "Beach"
    else:
        menu:
            "We could go to the Shopping Centre":
                $ Choice = "Shoping"
            "We could go to a cafe":
                $ Choice = "Cafe"
    
    
    m 5a "Well the bus is here, we'd better get on."
    show bg BusInterior
    
    m 5b "These seats arent very comfy but atleast it's cheap."
    
    if Choice == "Shoping":
        m 1k "Oh [player], I'm imagine all the things we could buy."
        m 1j "Like some new outfits"
        if persistent.Outfit == "School":
            m m "This one is quite old."
        else:
            m 1b "I could get something cute, and maybe even..."
            m 1sb "Something a little sexy? hehe~"
            m 1a "Oh, don't be so embarrassed [player]."
            m "There's nothing wrong with getting excited other the Idea. In fact, I think it's quite cute, and maybe even exciting for me too~"
        
        m "We could go to chocolate shop too, I love all the free samples they give out."
        m 1b "And while it may not be healthy it does make for a good treat."
        
        
    elif Choice == "Cafe":
        m 1a "I have been craving a coffee for a while."
        m 1b "What about you [player], do you like Coffee?"
        menu:
            "No":
                m 1bb "Well it is an aquired taste. I guess your tastebuds are as sweet as you!"
                "Monika's expression turns into a develish grin."
                m 1sb "Maybe I could get a taste?~"
                show monika 1sb at face(y=800) with dissolve
                "Monika has leaned in close, her lips are centimeters from yours."
                show monika 1kiss at face(y=1100,z=1.1) with dissolve
                "Leaning forward, you've closed the gap."
                "At first it's gentle, but never being one for patience in passion, Monika forces her way in."
                "She's passionate and dominate and yet somehow gentle at the same time, regarless it's an amazing kiss."
                m "Oaahhh~"
                show monika 1db at t11 zorder 2
                m "..."
                m 1nb "I'm sorry, that just slipped out."
                m 1kb "But wow... I know that wasn't real but it felt amazing anyway."
                m 1sb "I'll be doing that again, if you don't mind~"
                
            "Yes":
                m "not finished"
            "I didn't":
                m "Not finished"
            
        
    

    