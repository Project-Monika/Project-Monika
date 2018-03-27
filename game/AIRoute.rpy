
label Space_Room:
    show bg Monika_Home
    play music m1
    
    if persistent.Outfit == "School":
        show monika School 1a at t11 zorder 2
    elif persistent.Outfit == "RedWhite":
        show monika RedWhite 1a at t11 zorder 2
    m "Hi [player]!"
    m "It's nice to see you my love"
    jump Space_Room_Menu
    return

label Space_Room_Menu:
    #$ AI.MoodSwing()
    show monika 4a 
    m "What shall we do?"
    
    menu:
        "Chat":
            jump Chat
        "Ask a Question":
            jump Questions
        "Wardrobe":
            jump Wardrobe
        "Mini Games":
            m "Okay!"
        "Go Out":
            jump StartTrip
        "Online Shop":
            m "Okay!"
        "Good Bye":
            m "Goodbye [player]."
            return
    jump Space_Room_Menu
    return

label Chat:
    call I_Love_You
            
    
    return

label Questions:
    
    menu:
        "How are you?":
           call How_Are_You
        "Back":
           jump Space_Room_Menu
    
    return

label Wardrobe:
    menu:
        "School Uniform":
            show monika School 1b
            m "Well, this is nostalgic, but I think I perfer something more casual."
            $ persistent.Outfit = "School"
            jump Space_Room_Menu
        "White shirt with red dress":
            show monika RedWhite 1b
            m "Ah, It feels so good to finnaly be out of that uniform!"
            m "Thanks for buying me this [player]!"
            $ persistent.Outfit = "RedWhite"
            jump Space_Room_Menu
        
    

            

