# events from chapter 4

# Import json file with chapter 4 dialogue
init python:
    import json
    dial4 = json.load(renpy.file("chap4_dial.json"))

##Hallway scene chapter 4
label chap4_hallway:
    $ midleft= Position(xalign=2.8)
    $ midright= Position(xalign=1.8)
    ## school hallway
    scene chap4 with Pause(2.0)
    scene hallway with fade
    show hailey
    hailey"[dial4[dial][hailey]]"
    hide hailey
    show alex worry
    alex"[dial4[dial][alex]]"
    hide alex worry
    show hailey worry
    hailey"[dial4[dial][hailey-1]]"
    hide hailey worry
    show alex worry
    alex"[dial4[dial][alex-1]]"
    hide alex worry
    show hailey worry
    hailey"[dial4[dial][hailey-2]]"
    hailey"[dial4[dial][hailey-3]]"
    hide hailey worry
    show alex worry
    alex"[dial4[dial][alex-2]]"
    hide alex worry
    show alex mad
    alex"[dial4[dial][alex-3]]"
    hide alex worry
    jump chap4_class

label chap4_class:
    ## Scene classroom
    scene classroom with fade
    show hailey worry
    hailey"[dial4[dial][hailey-4]]"
    hide hailey worry
    show alex worry
    alex"[dial4[dial][alex-4]]"
    show alex mad
    alex"[dial4[dial][alex-5]]"
    hide alex
    show sarah
    sarah"[dial4[dial][sarah]]"
    hide sarah mad
    show alex
    alex"[dial4[dial][alex-6]]"
    hide alex
    show sarah mad
    sarah"[dial4[dial][sarah-1]]"
    hide sarah mad
    show alex
    alex"[dial4[dial][alex-7]]"
    hide alex
    show sarah mad
    sarah"[dial4[dial][sarah-2]]"
    hide sarah mad
    show hailey mad
    hailey"[dial4[dial][hailey-5]]"
    hide hailey mad
    show hailey mad
    hailey"[dial4[dial][hailey-6]]"
    hide hailey mad
    show alex mad
    alex"[dial4[dial][alex-8]]"
    hide alex mad
    jump hallway_bathroom

label hallway_bathroom:
    scene hallway with fade
    show sarah mad
    ## Scene in the hallway by the girls bathroom?
    sarah"[dial4[dial][sarah-3]]"
    hide sarah mad
    show alex worry
    alex"[dial4[dial][alex-9]]"
    hide alex worry
    show sarah mad
    sarah"[dial4[dial][sarah-4]]"
    hide sarah mad
    show alex mad
    alex"[dial4[dial][alex-10]]"
    hide alex mad

    ## MENU asking player what to do
    menu:
        "Ask who.":
            show sarah mad
            sarah"[dial4[dial][sarah-5]]"
            hide sarah mad
        "Walk away.":
            show alex worry
            alex"[dial4[dial][alex-11]]"
            hide alex worry
            show sarah mad
            sarah"[dial4[dial][sarah-6]]"
            hide sarah mad
    show hailey mad
    hailey"[dial4[dial][hailey-7]]"
    hide hailey mad
    show sarah mad
    sarah"[dial4[dial][sarah-7]]"
    hide sarah mad
    show alex worry
    alex"[dial4[dial][alex-12]]"
    hide alex worry

    ## menu asking the player what to do
    menu:
        "Let my anger out!":
            show alex mad
            alex"[dial4[dial][alex-13]]"
            alex"[dial4[dial][alex-14]]"
            hide alex mad
        "Remain calm.":
            show alex worry
            alex"[dial4[dial][alex-15]]"
            alex"[dial4[dial][alex-16]]"
            hide alex worry
    show sarah mad
    sarah"[dial4[dial][sarah-8]]"
    hide sarah mad
    show alex mad
    alex"[dial4[dial][alex-17]]"
    hide alex mad

    #menu asking the player what to do
    menu:
        ## show girl restroom##
        ## show madalex for push##

        "Push her inside the restroom!":
            scene girlsRestroom with fade
            show alex mad
            alex"[dial4[dial][alex-18]]"
            alex"[dial4[dial][alex-19]]"
            hide alex mad
        "Leave!":
            scene hallway with fade
            show alex mad
            ## show hallway and alex is mad and h is mad##
            alex"[dial4[dial][alex-20]]"
            hide alex mad
            scene girlsRestroom with fade
            show  hailey mad
            ##hailey takes sarah into the restroom
            hailey"[dial4[dial][hailey-7]]"
            hide  hailey mad
            show  alex mad
            alex"[dial4[dial][alex-21]]"
            hide  alex mad
    #Hailey starts sticking sarah head into the toilet
    ##girl bathroom##
    ## h is mad and alex is worry ##
    scene girlsRestroom with fade
    show hailey mad
    hailey"[dial4[dial][hailey-8]]"
    hide hailey mad
    show alex worry
    alex"[dial4[dial][alex-211]]"
    hide alex worry

    #menu asking player what to do
    menu:
        ## show girl bathroom##
        "Help Amanda!":
            scene girlsRestroom with fade
            show alex worry
            ## alexworry and h is mad still and sarah cry/sad##
            alex"[dial4[dial][alex-22]]"
            hide alex worry
            show hailey mad
            hailey"[dial4[dial][hailey-9]]"
            hailey"[dial4[dial][hailey-10]]"
            hide hailey mad
            show sarah worry
            sarah"[dial4[dial][sarah-9]]"
            hide sarah worry
        "Panic!":
            ##hallway and alex sad ##
            scene hallway with fade
            show  alex worry
            alex"[dial4[dial][alex-23]]"
            hide  alex worry
            show alex mad
            #alex leaves bathroom
            ##show alex mad ##
            alex"[dial4[dial][alex-24]]"
            ## show girl bathroom##
            #alex comes back to bathroom and alex25 is mad and h is mad ##
            alex"[dial4[dial][alex-25]]"
            hide alex mad
    ## show girl bathroom and alex and h is worry##
    scene girlsRestroom with fade
    show hailey worry
    hailey"[dial4[dial][hailey-11]]"
    hide hailey worry
    show  alex worry
    alex"[dial4[dial][alex-26]]"
    alex"[dial4[dial][alex-27]]"
    hide  alex worry
    show hailey worry
    hailey"[dial4[dial][hailey-12]]"
    hide hailey worry
    ## hide the a and h ##
    #End of chapter 4
    jump chap5_running
