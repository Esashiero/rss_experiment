# This script demonstrates all V1.0 features.

label start:
    scene bg black
    show eileen happy at left
    $ player_name = "Alex"
    $ score = 100

    e "Welcome, [player_name]! Your score is [score]."

    menu:
        "Start the test.":
            jump test_logic
        "Leave.":
            e "Goodbye!"
            return

label test_logic:
    play music "upbeat.ogg"
    $ score -= 25

    if score > 80:
        e "You are doing great!"
    elif score > 50:
        e "You are doing okay."
        # Nested if/else
        if player_name == "Alex":
            e "I expected better from you, Alex."
        else:
            e "Keep trying!"
    else:
        e "You are failing."

    hide eileen
    stop music
    e "The test is over."
    return