#events for chapter 5
# Import json file with chapter 4 dialogue
init python:
    import json
    dial5 = json.load(renpy.file("chap5_dial.json"))

label chap5_running:
    $ midleft= Position(xalign=2.8)
    $ midright= Position(xalign=1.8)
    #Show scene of alex and hailey running
    scene chap5 with Pause(2.0)
    scene run with Pause(2.0)
    #Setting bedroom
    scene alexRoom with fade
    show alex mad at midleft
    alex"[dial5[dial][alex]]"
    show alex worry at midleft
    alex"[dial5[dial][alex-1]]"

    #crime scene
    scene reporter with fade
    news_reporter"[dial5[dial][nr]]"
    news_reporter"[dial5[dial][nr-1]]"

    #setting room again
    scene alexRoom with fade
    show alex worry
    alex"[dial5[dial][alex-2]]"
    hide alex
    show hailey mad
    hailey"[dial5[dial][hailey]]"
    hide hailey
    show alex mad
    alex"[dial5[dial][alex-3]]"
    alex"[dial5[dial][alex-4]]"
    alex"[dial5[dial][alex-5]]"
    show alex mad at midleft
    #menu to ask player what to do
    menu:
        "Kick out Hailey!?":
            show alex mad at midleft
            alex"[dial5[dial][alex-6]]"
            hide alex
            show hailey worry
            hailey"[dial5[dial][hailey-1]]"
            hide hailey
            show alex mad
            alex"[dial5[dial][alex-7]]"
            hide alex
        "Listen to Hailey's explaination?":
            show alex mad
            alex"[dial5[dial][alex-8]]"
            hide alex
    show hailey mad
    hailey"[dial5[dial][hailey-2]]"
    hide hailey
    show alex mad
    alex"[dial5[dial][alex-9]]"
    alex"[dial5[dial][alex-10]]"
    hide alex
    show hailey worry
    hailey"[dial5[dial][hailey-3]]"
    hide hailey
    show alex mad
    alex"[dial5[dial][alex-11]]"
    hide alex
    show hailey
    hailey"[dial5[dial][hailey-4]]"
    hide hailey

    ##menu asking player
    menu:
        "Yes!":
            show alex worry
            alex"[dial5[dial][alex-12]]"
            hide alex worry
            show hailey worry
            hailey"[dial5[dial][hailey-5]]"
            hide hailey
            show alex mad
            alex"[dial5[dial][alex-13]]"
            hide alex
            show hailey mad
            hailey"[dial5[dial][hailey-6]]"
            hide hailey
        "No!":
            show alex sad
            alex"[dial5[dial][alex-14]]"
            hide alex
            show hailey uninterested
            hailey"[dial5[dial][hailey-7]]"
            hide hailey
            show alex worry
            alex"[dial5[dial][alex-15]]"
            hide alex
            show hailey mad
            hailey"[dial5[dial][hailey-8]]"
    show hailey
    hailey"[dial5[dial][hailey-9]]"
    hide hailey
    show alex worry
    alex"[dial5[dial][alex-16]]"
    #menu asking player
    show alex worry
    alex"[dial5[dial][alex-165]]"
    hide alex
    menu:
        "Yes":
            show alex worry
            alex"[dial5[dial][alex-166]]"
            hide alex
        "No":
            show hailey mad
            hailey"[dial5[dial][hailey-99]]"
            hide hailey
    scene box with Pause(2.0)
    scene alexRoom with fade
    show alex worry
    alex"[dial5[dial][alex-17]]"
    hide alex
    show hailey worry
    hailey"[dial5[dial][hailey-999]]"
    hide hailey
    jump flashback1

#Scenario one
label flashback1:
    scene crime with fade
    show hailey
    hailey"[dial5[dial][hailey-10]]"
    hailey"[dial5[dial][hailey-11]]"
    hide hailey
    show alex worry
    alex"[dial5[dial][alex-18]]"
    hide alex

    #setting bedroom
    scene alexRoom with fade
    show alex mad
    alex"[dial5[dial][alex-18]]"
    hide alex
    show hailey worry
    hailey"[dial5[dial][hailey-12]]"
    hide hailey
    scene box with Pause(2.0)
    scene alexRoom with fade
    show alex worry
    alex"[dial5[dial][alex-19]]"
    hide alex
    #Scenario 2
    jump flashback2

label flashback2:
    scene field with fade
    show hailey worry
    hailey"[dial5[dial][hailey-13]]"
    hailey"[dial5[dial][hailey-15]]"
    scene alexRoom with fade
    show hailey worry
    hailey"[dial5[dial][hailey-16]]"
    hide hailey
    show alex worry
    alex"[dial5[dial][alex-20]]"
    hide alex
    show hailey
    hailey"[dial5[dial][hailey-17]]"
    hide hailey

    #menu asking player to choose
    menu:
        "Yes":
            scene box with Pause(2.0)
            scene alexRoom with fade
            show alex worry
            alex"[dial5[dial][alex-21]]"
            hide alex
            show hailey worry
            hailey"[dial5[dial][hailey-18]]"
            hide hailey
            show alex sad
            alex"[dial5[dial][alex-211]]"
            hide alex
            show hailey sad
            hailey"[dial5[dial][hailey-19]]"
            hide hailey
            jump flashback3
        "No":
            scene box with Pause(2.0)
            scene alexRoom with fade
            show hailey
            hailey"[dial5[dial][hailey-20]]"
            jump flashback3
    return

#scenario 3 from chapter 5 dialogue
label flashback3:
    scene door with fade
    show hailey sad
    hailey"[dial5[dial][hailey-21]]"
    hailey"[dial5[dial][hailey-22]]"
    hide hailey

    #setting bedroom
    scene alexRoom with fade
    show alex sad
    alex"[dial5[dial][alex-22]]"
    hide alex
    show hailey
    hailey"[dial5[dial][hailey-23]]"
    hide hailey
    show alex mad
    alex"[dial5[dial][alex-23]]"
    hide alex
    scene box with Pause(2.0)
    scene alexRoom with fade
    show hailey worry
    hailey"[dial5[dial][hailey-231]]"
    hide hailey
    jump  flashback4

#scenario 4
label flashback4:
    scene girlsRestroom with fade
    show hailey worry
    hailey"[dial5[dial][hailey-24]]"
    hide hailey
    #setting bedroom
    scene alexRoom
    show hailey
    hailey"[dial5[dial][hailey-25]]"
    hide hailey
    show alex worry
    alex"[dial5[dial][alex-24]]"
    show alex mad
    alex"[dial5[dial][alex-25]]"
    hide alex
    show hailey worry
    hailey"[dial5[dial][hailey-26]]"
    hide hailey
    show alex sad at midright
    alex"[dial5[dial][alex-26]]"
    show hailey
    hailey"[dial5[dial][hailey-27]]"
    #show mirror scene of alex and hailey being one. split face?
    ## scene mirror with fade
    hide hailey
    show alex sad
    $temp3 = "It was you, " + persistent.g_name + dial5["dial"]["alex-27"]
    alex"[temp3]"
    alex"[dial5[dial][alex-277]]"
    show alex mad
    alex"[dial5[dial][alex-28]]"
    jump ending_

label ending_:
    #setting do not cross
    scene reporter with fade
    news_reporter"[dial5[dial][nr-2]]"
    news_reporter"[dial5[dial][nr-3]]"
    scene end with Pause(4.0)
    return
