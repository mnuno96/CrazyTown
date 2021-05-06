#Chapter 1 and introduction

#Access script with character dialogue for chapter 1

# Import json file with chapter 1 dialogue
init python:
    import json

    dial = json.load(renpy.file("chap1_dial.json"))

## INTRO AND FIRST ROOM SCENE
label chap1_crime:
# position setters
    $ midleft= Position(xalign=2.8)
    $ midright= Position(xalign=1.8)
    scene chap1 with Pause(2.0)
    scene reporter with fade
    # Intro scene with 1st murder
    news_reporter"[dial[dial][nr]]"
    news_reporter"[dial[dial][nr-2]]"

    #Scence changes to the main characters room.
    show room with fade
    show alex

    alex "[dial[dial][alex]]"

    #Call getName to get the players name
    call getName from _call_getName
    $temp = "Nice to meet you, " + persistent.g_name + dial["dial"]["alex-2"]
    alex"[temp]"
    alex"[dial[dial][alex-3]]"
    jump hs
    return

## HIGH SCHOOL SCENE
label hs:
    show classroom with fade
    ## ADD SCENE OF BEST FRIEND (HAILEY) tapping shoulder of ALEX ##
    show haileyTAlex
    hailey"[dial[dial][hailey]]"
    hide haileyTAlex
    ## CHANGE EMOTION OF HAILEY SMIRKING ABOUT THE MURDER ##
    ## show alex at midleft
    show hailey at midright
    hailey"[dial[dial][hailey-1]]"
    hide hailey
    ## CHANGE EMOTION OF ALEX UNEMOTIONAL SILENCE ##
    show alex uninterested at midleft
    hide alex
    show hailey
    hailey"[dial[dial][hailey-2]]"
    hide hailey
    ## ALEX SUPRISED ##
    show alex at midleft
    alex"[dial[dial][alex-4]]"
    ## HAILEY UPSET ##
    hide alex
    show hailey mad at midright
    hailey"[dial[dial][hailey-3]]"
    hailey"[dial[dial][hailey-4]]"
    hide hailey
    ## SHOW ALEX NO EMOTION ##
    show alex uninterested at midleft
    ## SHOW ALEX THINKING
    #alex"[dial[dial][alex-9]]"
    ## MENU
    menu:
        alex"[dial[dial][alex-9]]"
        "Yes.":
            ## SHOW ALEX HANDS IN POCKET
            show alex at midleft
            alex"[dial[dial][alex-5]]"
            ## SHOW HAILEY EXCITED
            show hailey at midright
            hailey"[dial[dial][hailey-6]]"
        "No.":
            ## SHOW ALEX HANDS IN POCKET
            show alex at midleft
            alex"[dial[dial][alex-7]]"
            show hailey sad at midright
            ## SHOW HAILEY SMIRKING
            show hailey
            hailey"[dial[dial][hailey-7]]"
            ## SHOW ALEX EMOTIONLESS
            show alex uninterested at midleft
            alex"[dial[dial][alex-8]]"
            ## SHOW HAILEY EXCITED
            hailey"[dial[dial][hailey-6]]"
            hide hailey
            hide alex
            jump crime
            return

    ## BACK AT CRIME SCENE BODY ON FLOOR
label crime:
    scene crime with fade

    ## ALEX WORRIED
    show alex worry at midleft
    show hailey at midright
    alex"[dial[dial][alex-10]]"
    ## SHOW HAILEY EXCITED
    hailey"[dial[dial][hailey-8]]"
    ## SHOW BROKEN BOTTLE GLASS WITH BLOOD
    scene bottle with fade
    alex"[dial[dial][alex-11]]"
    hailey"[dial[dial][hailey-9]]"
    ## SHOW ALEX MAD
    show alex mad at midleft
    alex"[dial[dial][alex-12]]"
    show hailey
    hailey"[dial[dial][hailey-10]]"
    ## SHOW SCENE WITH COP CARS DRIVING TOWARDS THE SCENE
    scene cop with fade
    alex"[dial[dial][alex-13]]"
    hide alex
    hide hailey
    ## MENU
    menu:
        "RUN!":
            show hailey at midright
            show alex worry at midleft
            hailey"[dial[dial][hailey-11]]"
        "HIDE!":
            show hailey worry at midright
            show alex worry at midleft
            alex"[dial[dial][alex-13]]"
            alex"[dial[dial][alex-14]]"
            hailey"[dial[dial][hailey-11]]"

    ## CRIME SCENE WITH ALEX WORRIED
    scene crime with fade
    show alex worry
    ## SCENE ENDS HERE
    alex"[dial[dial][alex-15]]"

    jump hallway
    return

## BACK TO SCHOOL SETTING. SHOW ALEX AND HAILEY IN THE HALLWAY
label hallway:
    #Show alex with hailey
    scene hallway with fade
    show hailey at midright
    show alex mad at midleft
    alex"[dial[dial][alex-16]]"
    hailey"[dial[dial][hailey-12]]"
    hailey"[dial[dial][hailey-13]]"
    #Remove hailey from the scene
    hide hailey
    alex"[dial[dial][alex-17]]"
    jump chap2_lib
    return

# getName asks for the players name
label getName:
    #Assign the players name
    $persistent.g_name = renpy.input("My first name is:", default=" ", allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-", length=10)

    #If the player does not input a name then their name will be assigned
    if persistent.g_name == " ":
        $ persistent.g_name= "Player"
    return
