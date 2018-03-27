label How_Are_You:
    $ PercentageDiffrence = AI.Diffrence(100, 100, 100, 50, 50, 0, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    $ Counter = 1
    $ PD = AI.Diffrence(100, 100, 50, 25, 50, 50, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if PD <= PercentageDiffrence:
        $ PercentageDiffrence = PD
        $ Counter = 2
    
    $ PD = AI.Diffrence(100, 100, 100, 100, 100, 100, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if PD <= PercentageDiffrence:
        $ PercentageDiffrence = PD
        $ Counter = 3
    
    $ PD = AI.Diffrence(100, 0, 100, 100, 100, 100, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if PD <= PercentageDiffrence:
        $ PercentageDiffrence = PD
        $ Counter = 4
    
    $ PD = AI.Diffrence(0, 100, 100, 100, 100, 100, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if PD <= PercentageDiffrence:
        $ PercentageDiffrence = PD
        $ Counter = 5
    
    $ PD = AI.Diffrence(100, 100, 0, 0, 0, 100, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if PD <= PercentageDiffrence:
        $ PercentageDiffrence = PD
        $ Counter = 6
    
    $ PD = AI.Diffrence(100, 100, 0, 0, 100, 0, 100, 100) #happy,sad,angry,disgusted,romatic,calm,brave,fear
    if PD <= PercentageDiffrence:
        $ PercentageDiffrence = PD
        $ Counter = 7
    
    if Counter == 1:
        m "I'm Angry at you [player]!"
    if Counter == 2:
        m "I'm Annoyed with you"
    if Counter == 3:
        m "I'm Alright"
    if Counter == 4:
        m "I'm Really Happy!"
    if Counter == 5:
        m "I'm sad"
    if Counter == 6:
        m "I'm feeling calm"
    if Counter == 7:
        m "I'm feeling Romatic"
    call Questions
    return