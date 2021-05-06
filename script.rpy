
# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Define characters, variables, constants, etc

init:
    define news_reporter = Character("News Reporter")
    # MAIN CHARACTER
    define alex = Character("Alex")
    # BFF
    define hailey = Character("Hailey")
    #friend that dies at house
    define luke = Character("Luke")
    # TUTOR
    define amanda = Character("Amanda")
    #from chapter 4 Amanda = Sarah
    define sarah = Character("Sarah")
    define teacher = Character("Teacher")
    define parents = Character ("Luke's Parents")
    define player = Character(["player_name"])

init -200:
    define fade = Fade(0.2, 0.2, 0.2)

#Game starts here
label start:

    jump chap1_crime

    return
