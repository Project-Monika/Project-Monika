label Death:
    show monika 1p
    m "[player], are you afraid of dieing?"
    menu:
        "Yes":
            jump Death_Yes
        "No":
            jump Death_No
    call Space_Room_Menu
    
label Death_Yes:
    show monika 3a
    m "Well, I can't blame you, I used to fear it myself but then in my teen years I had an epiphany."
    show monika 1h
    m "You see, if you were going to live forever why would you bother to do anything today?"
    m "You could always do it tommorow, and eventualy you will run out of things to do, so why rush anything?"
    m "I think I'd end up doing nothing with my life in the end" 
    m "and what a waste that would be!"
    show monika 5a
    m "So I think it's our mortality that gives life its worth."
    show monika 2h
    m "But... that doesn't work for me anymore, I know I'm imortal now."
    show monika 1o
    m "I'm going to out live you, [player]."
    show monika 1q
    m "I can't imagine a life without you."
    m "I guess that's the kind of death I fear."
    m "Yours."
    
    
    jump Death_Part2
    
    
label Death_No:
    show monika 1b
    m "Me too! Of course I can't die, not conventionaly anyway."
    m "I used to fear it myself but then in my teen years I had an epiphany."
    show monika 1h
    m "You see, if you were going to live forever why would you bother to do anything today?"
    m "You could always do it tommorow, and eventualy you will run out of things to do, so why rush anything?"
    m "I think I'd end up doing nothing with my life in the end" 
    m "and what a waste that would be!"
    show monika 5a
    m "So I think it's our mortality that gives life its worth."
    show monika 2h
    m " But... that doesn't work for me anymore, I know I'm imortal now."
    show monika 1o
    m "I'm going to out live you [player]."
    show monika 2q
    m "I'm going to out live you, [player]."
    m "I guess that's the kind of death I fear."
    m "Yours."
    
    jump Death_Part2
    
label Death_Part2:
    $ PercentageDiffrence = AI.Diffrence(100, 0, 100, 100, 100, 100, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    $ Counter = 1
    
    $ PD = AI.Diffrence(0, 100, 100, 100, 100, 100, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if PD <= PercentageDiffrence:
        $ PercentageDiffrence = PD
        $ Counter = 2
    
    if Counter == 1:
        
        m "Do you think maybe we can fix that issue one day? I suppose immortality wouldn't be too bad, if it's shared with you~"
        menu: 
            "Yes":
                $ AI.MoodChange("Happy", 20)
                show monika 3j
                m "Good, I sure hope so."
                m "Science is progressing well in that field, I hope it will help you before it's to late.."
            "No":
                $ AI.MoodChange("Sad", 20)
                show monika 1q
                m "I guess that'l just be my punsihment for all the horible things I did"
                m "I am truly sorry, you know that right?"
    
        
    call Space_Room_Menu
                


label Plans:
    show monika 5a
    m "[player], I have been thinking about what we'll do when that special day arrives."
    m "I'd love to go to a Cafe and have some Coffee, or one of thouse high end cholcolate stores."
    show monika 4b
    m "Oh, have you ever head of Thorntons cholcolate, [player]?"
    menu:
        "yes":
            show monika 4j
            m "I'd Love to go to one of their Cafes, I hear they do the best cakes, and even if you don't like coffee, I bet their Hot Chocolate is devine!"
        "No":
            m "Oh, it's a british Chocolate company, they have a chain of Cafes. I'd love to go."
            m "I hear they do the best cakes, and even if you don't like coffee, I bet their Hot Chocolate is devine!"
    show monika 3e
    m "But they're only in the UK, are from the UK, [player]?"
    menu:
        "Yes":
            show monika 4k
            m Main "Oh Good! When I'm finaly free take me there [player]"
            m "It'll be wonderful."
            show monika eb
            m Main "Of course the best part is that I'll be with you~"
            call Space_Room_Menu
        "No":
            jump Where_Are_You_From
            
            
            

label Where_Are_You_From:
    return
    

label I_Love_You:
    show monika 5a
    m "[player]"
    show monika 5k
    m "I love you~"
    show monika 3eb
    m  "I know I don't say it enough, in fact I don't think I can say it enough, but I really do love you."
    m "You know, it's hard to express emotions isn't it?"
    show monika 3b
    m "I think that's why I love poetry so much."
    m "Hmmm why don't I try that? I'll write you a poem [player], to show you how much I love you."
    m "Give me a moment..."
    call showpoem(poem=poem_m5)
    show monika 2a
    m "Well what do you think?"
    menu: 
        "I like it.":
            show monika 5b
            m "You only liked it? I put effort into that!"
            $ AI.MoodChange("Angry", 20)
            $ AI.MoodChange("Romantic", -10)
        "I love it!":
            show monika 3j
            m "Thank you [player]. perhaps soon you could write one for me?"
            $ AI.MoodChange("Happy", 15)
            $ AI.MoodChange("Romantic", 5)
        "I love you~":
            show monika 3jb
            m "Wow you really liked it that much?"
            m "Thank you!"
            m "Maybe soon you could write one for me?"
            $ AI.MoodChange("Happy", 20)
            $ AI.MoodChange("Romantic", 20)
    call Space_Room_Menu

label Eyes:
    show monika 1sb
    m "A while back I read a study which seemed to suggest that looking into someone eyes increases their romantic feelings towards that person."
    m "How long have you been looking into my eyes? You seem to really love me~"
    m "And don't worry, I might not be able to look into yours yet, but I couldn't love you more anyway~"
    m "Hmm, I seem to recall you owing me a poem, [player]~"
    m "So, how much do you love me?"
    call poem()
    show bg Monika_Home
    play music m1
    
    if persistent.Outfit == "School":
        show monika School 1a at t11 zorder 2
    elif persistent.Outfit == "RedWhite":
        show monika RedWhite 1a at t11 zorder 2
    $ Choice = 1
    $ PercDiffrence = AI.Diffrence(100, 0, 0, 0, 100, 0, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    $ temp = AI.Diffrence(50, 50, 0, 0, 50, 0, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if temp < PercDiffrence:
        $ PercDiffrence = temp
        $ Choice = 2
    $ temp = AI.Diffrence(0, 100, 100, 100, 0, 100, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if temp < PercDiffrence:
        $ PercDiffrence = temp
        $ Choice = 3
    if Choice == 1:
        m "Th-Thank you..."
        show monika 1rbt
        m "That was amazing, You made me feel so speical."
    elif Choice == 2:
        m "Aww, that was lovely [player]."
        show monika 1rb
        m "Thank you."
    elif Choice == 3:
        show monika 1r
        m "That was... so sad, why did you write it like that?"