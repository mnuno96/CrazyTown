#Events for chapter 3

# Import json file with chapter 3 dialogue
init python:
    import json
    dial3 = json.load(renpy.file("chap3_dial.json"))

label chap3_class:
    $ midleft= Position(xalign=2.8)
    $ midright= Position(xalign=1.8)
    scene chap3 with Pause(2.0)
    ## SETTING CLASSROOM
    scene classroom with fade
    show teacher
    teacher"[dial3[dial][teacher]]"
    hide teacher
    ##classmate luke talks to player(alex) scene
    show luke
    luke"[dial3[dial][luke]]"
    hide luke
    show alex uninterested
    alex"[dial3[dial][alex]]"
    hide alex
    show luke
    luke"[dial3[dial][luke-1]]"
    luke"[dial3[dial][luke-2]]"
    hide luke
    show alex
    alex"[dial3[dial][alex-1]]"
    alex"[dial3[dial][alex-2]]"
    hide alex
    show luke
    luke"[dial3[dial][luke-3]]"
    hide luke
    show alex
    alex"[dial3[dial][alex-3]]"
    hide alex
    show luke
    luke"[dial3[dial][luke-4]]"
    hide luke
    # go to lukes house scene
    jump luke_house

label luke_house:
    ##alex arriving at house
    scene house with fade
    show alex
    alex"[dial3[dial][alex-4]]"
    ##luke meets outside of house
    hide alex
    show luke
    luke"[dial3[dial][luke-5]]"
    hide luke
    show alex
    alex"[dial3[dial][alex-5]]"
    hide alex
    show luke
    luke"[dial3[dial][luke-55]]"
    luke"[dial3[dial][luke-6]]"
    hide luke
    # Menu for player to choose where to study
    menu:
        "Luke's Bedroom":
            show luke
            luke"My room it is!"
            hide luke
            scene bedroom
            show alex
            alex"[dial3[dial][alex-00]]"
            show parents
            parents"[dial3[dial][md]]"
            hide parents
            show luke
            luke"[dial3[dial][luke-7]]"
            hide luke
            show alex
            alex"[dial3[dial][alex-6]]"
            hide alex
            show luke
            luke"[dial3[dial][luke-8]]"
            hide luke
        "Dining Room":
            show luke
            luke"Okay, dining room it is!"
            hide luke
            scene dining with fade
            show alex
            alex"[dial3[dial][alex-00]]"
            hide alex
            show parents
            parents"[dial3[dial][md]]"
            hide parents
            show luke
            luke"[dial3[dial][luke-7]]"
            hide luke
            show alex
            alex"[dial3[dial][alex-6]]"
            hide alex
            show luke
            luke"[dial3[dial][luke-8]]"
            hide luke
    ##show alex
    #alex"[dial3[dial][alex-00]]"
    #hide alex
    #show parents
    #parents"[dial3[dial][md]]"
    #hide parents
    #show luke
    #luke"[dial3[dial][luke-7]]"
    #hide luke
    #show alex
    #alex"[dial3[dial][alex-6]]"
    #hide alex
    #show luke
    #luke"[dial3[dial][luke-8]]"
    #hide luke
    #scene dinner table
    scene diningroom with fade
    show parents
    parents"[dial3[dial][md-1]]"
    hide parents
    show luke mad
    luke"[dial3[dial][luke-9]]"
    hide luke
    show parents
    parents"[dial3[dial][md-2]]"
    parents"[dial3[dial][md-3]]"
    hide parents
    show alex
    alex"[dial3[dial][alex-7]]"
    alex"[dial3[dial][alex-8]]"
    hide alex
    # menu asking player what to eat
    menu:
        "Lobster":
            show parents
            parents"[dial3[dial][md-4]]"
            hide parents
        "Steak":
            show parents
            parents"[dial3[dial][md-4]]"
            hide parents

    show luke worry
    luke"[dial3[dial][luke-10]]"
    hide luke
    show alex
    alex"[dial3[dial][alex-9]]"
    alex"[dial3[dial][alex-10]]"
    hide alex
    show parents
    parents"[dial3[dial][md-5]]"
    hide parents
    show luke
    luke"[dial3[dial][luke-11]]"
    hide luke
    show parents
    parents"[dial3[dial][md-6]]"
    parents"[dial3[dial][md-7]]"
    hide parents
    show luke sad
    luke"[dial3[dial][luke-12]]"
    luke"[dial3[dial][luke-13]]"
    show luke mad
    luke"[dial3[dial][luke-14]]"
    hide luke
    show parents
    parents"[dial3[dial][md-8]]"
    hide parents
    show luke sad
    luke"[dial3[dial][luke-15]]"
    luke"[dial3[dial][luke-16]]"
    hide luke
    show alex worry
    alex"[dial3[dial][alex-11]]"
    hide alex
    show luke mad
    luke"[dial3[dial][luke-17]]"
    hide luke
    #luke leaves
    show parents
    parents"[dial3[dial][md-9]]"
    hide parents
    show alex worry
    alex"[dial3[dial][alex-12]]"
    #alex walking to go check on him
    show alex
    alex"[dial3[dial][alex-13]]"
    hide alex
    menu:
        "Luke's Bedroom":
            ##alex knocking on door
            scene door with fade
            show alex
            alex"[dial3[dial][alex-14]]"
            alex"[dial3[dial][alex-15]]"
            hide alex
            show bedroom with fade
            show alex sad
            alex"[dial3[dial][alex-16]]"
            hide alex
            show parents
            parents"[dial3[dial][md-10]]"
            hide parents
        "Luke's Bathroom":
            ##alex knocking on door
            scene door with fade
            show alex
            alex"[dial3[dial][alex-14]]"
            alex"[dial3[dial][alex-15]]"
            scene bathroom with fade
            show alex sad
            alex"[dial3[dial][alex-16]]"
            hide alex
            show parents
            parents"[dial3[dial][md-10]]"
    jump crime3

#Label crime scene at luke house?
label crime3:
    ##show crime scene
    scene reporter with fade
    news_reporter"[dial3[dial][nr]]"
    jump chap4_hallway
