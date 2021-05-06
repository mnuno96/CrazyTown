# Events for chaper 2
# Import json file with chapter 2 dialogue
init python:
    import json
    dial2 = json.load(renpy.file("chap2_dial.json"))

#lib = library
label chap2_lib:
    $ midleft= Position(xalign=2.8)
    $ midright= Position(xalign=1.8)
    scene chap2 with Pause(2.0)
    show library with fade
    ## Setting school library ##
    ## Walking down school and passes library where a paper is posted on door, sees it says tutoring with open slots and signs up ##
    ## Amanda the tutor, Comes up to his table and introduces herself
    show amanda
    amanda"[dial2[dial][amanda]]"
    hide amanda
    show alex
    alex"[dial2[dial][alex]]"
    hide alex
    show amanda
    amanda"[dial2[dial][amanda-1]]"
    hide amanda
    show alex
    alex"[dial2[dial][alex-2]]"
    hide alex
    show amanda
    amanda"[dial2[dial][amanda-2]]"
    hide amanda

    show alexRoom with fade
    ## Setting bedroom
    show alex
    alex"[dial2[dial][alex-3]]"
    hide alex
    show hailey uninterested
    hailey"[dial2[dial][hailey]]"
    hide hailey uninterested
    show alex
    alex"[dial2[dial][alex-4]]"
    hide alex
    show hailey
    hailey"[dial2[dial][hailey-1]]"
    hide hailey
    show alex
    alex"[dial2[dial][alex-5]]"
    hide alex
    show hailey
    hailey"[dial2[dial][hailey-2]]"
    hide hailey
    show alex
    alex"[dial2[dial][alex-6]]"
    hide alex
    show hailey
    hailey"[dial2[dial][hailey-3]]"
    hide hailey
    ## Setting blank
    scene sessions with Pause(2.0)
    ## A few sessions go by
    scene library with fade
    ## Setting library alex being tutored
    show amanda
    amanda"[dial2[dial][amanda-3]]"
    hide amanda
    show alex
    alex"[dial2[dial][alex-7]]"
    hide alex
    show amanda
    amanda"[dial2[dial][amanda-4]]"
    hide amanda
    show alex
    #talking to himself (the player)
    # show alex blushing?
    alex"[dial2[dial][alex-8]]"
    hide alex
    show amanda
    amanda"[dial2[dial][amanda-7]]"
    hide amanda
    ## Tutoring session ends here
    show alexRoom with fade
    #Setting bedroom
    ## Hailey calling Alex
    show alex
    alex"[dial2[dial][alex-9]]"
    hide alex
    show hailey
    hailey"[dial2[dial][hailey-4]]"
    hide hailey
    show alex
    alex"[dial2[dial][alex-10]]"
    hide alex
    show hailey
    hailey"[dial2[dial][hailey-5]]"
    hide hailey
    show alex worry at midleft
    $temp2 = dial2["dial"]["alex-11"] + persistent.g_name + " ?"
    alex"[temp2]"


    ## Menu asking the player to select yes or no
    menu:
        "Yes":
            hide alex
            show hailey
            hailey"[dial2[dial][hailey-6]]"
            hide hailey
        "No":
            hide alex
            show hailey
            hailey"[dial2[dial][hailey-7]]"
            hide hailey
            show alex
            alex"[dial2[dial][alex-12]]"
            hide alex

    ## Setting school hallway
    scene hallway with fade
    show alex
    alex"[dial2[dial][alex-13]]"
    hide alex
    show amanda
    amanda"[dial2[dial][amanda-5]]"
    hide amanda
    show alex
    alex"[dial2[dial][alex-14]]"
    hide alex
    show amanda
    amanda"[dial2[dial][amanda-6]]"
    hide amanda
    show alex
    alex"[dial2[dial][alex-15]]"
    hide alex
    jump classroom2

## Setting classroom
label classroom2:
    scene classroom with fade
    #talking to himself (the player)
    show alex worry
    alex"[dial2[dial][alex-16]]"
    hide alex
    show hailey uninterested
    hailey"[dial2[dial][hailey-8]]"
    hide hailey uninterested
    show alex
    #asking the player
    alex"[dial2[dial][alex-17]]"
    hide alex
    ## menu asking the player where to go on the date
    menu:
        "Cafe Shop":
            show alex
            alex"[dial2[dial][alex-18]]"
            hide alex
        "Public Library":
            show alex
            alex"[dial2[dial][alex-18]]"
            hide alex
    show hailey
    hailey"[dial2[dial][hailey-9]]"
    hide hailey
    scene hallway with fade
    ## Setting school hallway
    ## Alex sees Amanda exiting the school
    show alex
    alex"[dial2[dial][alex-19]]"
    show alex worry
    alex"[dial2[dial][alex-20]]"
    scene couple with Pause(2.0)
    scene hallway with fade
    show alex sad
    ## Amanda doesnt hear him and exits the school with her boyfriend
    alex"[dial2[dial][alex-21]]"

    ## Setting bedroom
    scene alexRoom with fade
    show alex mad
    alex"[dial2[dial][alex-22]]"
    alex"[dial2[dial][alex-23]]"
    alex"[dial2[dial][alex-24]]"
    show alex sad
    alex"[dial2[dial][alex-25]]"
    alex"[dial2[dial][alex-26]]"
    jump crime2

## SEtting crime scene
label crime2:
    scene reporter with fade
    news_reporter"[dial2[dial][nr]]"
    ## Second character, Trevor Washington, dead.
    news_reporter"[dial2[dial][nr-1]]"
    jump chap3_class
