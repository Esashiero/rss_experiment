label dorm2monday:
    if otohaspecial15p2 == True:
        scene summerdorm2monsecond
        with dissolve
    elif chapthreeactive == True and otohaspecial15p2 == False:
        scene summerdorm2mon
        with dissolve
    elif mollysad == True and chapthreeactive == False:
        scene monwinter2nomolly
        with dissolve
    elif day288 == True and mollysad == False and chapthreeactive == False:
        scene monwinter2otoha
        with dissolve
    elif christmas7 == True and day288 == False and chapthreeactive == False:
        scene monwinter2
        with dissolve
    else:
        scene dorm2_monday
        with dissolve


    if mollysad == True:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Otoha isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"
        jump monday2menu
    elif day288 == True and mollysad == False:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Molly and Otoha aren't doing anything."
        "I could probably spend time with one of them if I want to."
        "What should I do?"
        jump monday2menu
    else:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Molly isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"
        jump monday2menu

    menu monday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Molly" if mollysad == False:
            if mollyfirsthall == False:
                jump mollyfirsthall
            else:
                jump mollyhall
        "Talk to Otoha" if day288 == True:
            if otohafirsthall == False:
                jump otohafirsthall
            else:
                jump otohahall
        "First Floor":
            jump dormmonday

label dorm2tuesday:
    if chapthreeactive == True:
        scene summerdorm2tues
        with dissolve
    elif day304 == True and chapthreeactive == False:
        scene tueswinter2
        with dissolve
    elif day304 == False and day247 == True and chapthreeactive == False:
        scene dorm2_tuesday
        with dissolve
    else:
        scene dorm2
        with dissolve

    "I walk up the stairs to the second floor of the dorms."

    if day304 == True:
        "It looks like Io and Touka aren't doing anything today."
        "I can probably talk to one of them if I want to."
    elif day304 == False and day247 == True:
        "It looks like Io isn't doing anything today."
        "I can probably spend some time with her if I want to."
    else:
        "What should I do?"
        jump tuesday2menu

    "What should I do?"

    menu tuesday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Io" if day247 == True:
            jump iohall
        "Talk to Touka" if day304 == True:
            jump toukahall
        "First Floor":
            jump dormtuesday

label dorm2wednesday:
    if chapthreeactive == True and norikoblock == False:
        scene summerdorm2wed
        with dissolve
    elif chapthreeactive == True and norikoblock == True:
        scene summerdorm2wednorikogone
        with dissolve
    elif christmas7 == True and day271 == True and chapthreeactive == False:
        scene wedwinter2noriko
        with dissolve
    elif christmas7 == True and day271 == False and chapthreeactive == False:
        scene wedwinter2
        with dissolve
    elif christmas7 == False and chapthreeactive == False:
        scene dorm2_wednesday
        with dissolve

    if christmas7 == True and day271 == False:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"
    elif christmas7 == True and day271 == True and norikoblock == False:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo and Noriko aren't doing anything."
        "I could probably spend time with one of them if I want to."
        "What should I do?"
    else:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"

    menu wednesday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Tsuneyo":
            if tsuneyofirsthall == False:
                jump tsuneyofirsthall
            else:
                jump tsuneyohall
        "Talk to Noriko" if day271 == True and norikoblock == False:
            if norikofirsthall == False:
                jump norikofirsthall
            else:
                jump norikohall
        "First Floor":
            jump dormwednesday

label dorm2thursday:
    if yasu_love >= 25 and church25 == True and yasudorm25 == False:
        jump yasudorm25
    elif chapthreeactive == True:
        scene summerdorm2thurs
        with dissolve
    elif day304 == True and chapthreeactive == False:
        scene thurswinter2yasu
        with dissolve
    elif day304 == False and day271 == True and chapthreeactive == False:
        scene thurswinter2
        with dissolve
    else:
        scene dorm2
        with dissolve

    if day304 == True:
        "It looks like Kirin and Yasu aren't doing anything today."
        "I can probably talk to one of them if I want to."
        "What should I do?"
        jump thursday2menu
    elif day304 == False and day271 == True:
        "It looks like Kirin isn't doing anything today."
        "I can probably spend some time with her if I want to."
        "What should I do?"
        jump thursday2menu
    else:
        "What should I do?"
        jump thursday2menu

    menu thursday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Kirin" if day271 == True:
            if kirinfirsthall == False:
                jump kirinfirsthall
            else:
                jump kirinhall
        "Talk to Yasu" if day304 == True:
            jump yasuhall
        "First Floor":
            jump dormthursday

label dorm2friday:
    if chapthreeactive == True and nodokablock == False:
        scene summerdorm2fri
        with dissolve
    elif chapthreeactive == True and nodokablock == True:
        scene dorm2frinodokagone
        with dissolve
    elif day288 == True and chapthreeactive == False:
        scene friwinter2nodoka
        with dissolve
    elif day247 == True and day288 == False and chapthreeactive == False:
        scene dorm2_friday
        with dissolve
    else:
        scene dorm2
        with dissolve

    "I walk up the stairs to the second floor of the dorms."
    "What should I do?"
    jump friday2menu

    menu friday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Uta" if day247 == True:
            jump utahall
        "Talk to Nodoka" if day288 == True and nodokablock == False:
            if nodokafirsthall == False:
                jump nodokafirsthall
            else:
                jump nodokahall
        "First Floor":
            jump dormfriday
label dorm2weekend:
    scene dorm2
    with dissolve

    "I walk up the stairs to the second floor of the dorms."
    "What should I do?"

    menu weekend2menu:
        "Knock on a door":
            jump doorknock2
        "Headpat Noodles" if dormwar17 == True and tsuneyofirsthall == True and noodlespatgasm == False:
            jump noodlesheadpat
        "First Floor":
            jump dormweekend

label doorknock2:
    "Which door should I knock on?"
    menu:
        "Room 6 (Molly & Tsuneyo)":
            "Who do I want to talk to?"
            menu:
                    "Molly (Current Affection - [molly_love])":
                        if mollysad == True:
                            s "..."
                            jump doorknock2
                        if molly_love >= 5 and day != 1:
                            jump mollydorm
                        if day == 1 and mollysad == False:
                            play sound "knock.mp3"
                            s "Hey, Molly. What are you up to right now?"
                            mo "Oh, shoot! Did I forget to turn my active camo off?"
                            mo "Sensei! I'm right here! Please notice me!"
                            s "Oh. Hey, Molly."
                            jump mollyhall
                        else:
                            play sound "knock.mp3"

                            s "Hey Molly, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock2

                    "Tsuneyo (Current Affection - [tsuneyo_love])":
                        if tsuneyo_love >= 5 and tsuneyofirsthall == True and day != 3:
                            jump tsuneyodorm
                        if day == 3:
                            play sound "knock.mp3"

                            s "Hey, Tsuneyo. Are you in there right now?"
                            t "I am not."
                            t "I am with the whale."
                            s "Whale? What whale?"
                            t "This whale. Next to the vending machine."

                            "I turn around to spot Tsuneyo over by...a whale...and decide to walk over to her."

                            jump tsuneyohall

                        else:
                            play sound "knock.mp3"

                            s "Hey Tsuneyo, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock2

                    "Go Back":
                        jump doorknock2

        "Room 7 (Uta & Io)":
            if day247 == False:
                "This room is not yet available."
                jump doorknock2
            else:
                "Who do I want to talk to?"
                menu:
                        "Uta (Current Affection - [uta_love])":
                            if uta_love >= 5 and day != 5:
                                jump utadorm
                            if day == 5:
                                play sound "knock.mp3"

                                s "Uta. Are you in there?"
                                s "What are you up to tonight?"
                                u "He...walked right past me."
                                u "Am I...not as cute as I thought?"
                                s "Oh, Uta. There you are."
                                u "Yes. Here I am."
                                u "Exactly where I've been since you got here..."

                                jump utahall
                            else:
                                play sound "knock.mp3"

                                s "Hey Uta, are you in there?"
                                "..."
                                "There's no answer."
                                jump doorknock2

                        "Io (Current Affection - [io_love])":
                            if io_love >= 5 and day != 2:
                                jump iodorm
                            if day == 2:
                                play sound "knock.mp3"

                                s "Io, what are you up to?"
                                i "..."
                                s "..."
                                i "Just...chilling."
                                i "In the hallway."
                                i "Right next to you..."

                                s "Oh. Woah. When did you get there?"

                                jump iohall
                            else:
                                play sound "knock.mp3"

                                s "Hey Io, are you in there?"
                                "..."
                                "There's no answer."
                                jump doorknock2

                        "Go Back":
                            jump doorknock2

        "Room 8 (Otoha & Nodoka)":
            if day288 == False:
                "This room is not yet available."
                jump doorknock2
            else:
                "Who do I want to talk to?"
                menu:
                        "Otoha (Current Affection - [otoha_love])":
                            if otoha_love >= 1 and day != 1:
                                jump otohadorm
                            if day == 1:
                                play sound "knock.mp3"

                                s "Otoha, are you in there?"
                                o "Yup. Definitely not right next to you."
                                o "Come on into the room that I am totally in right now, Sensei."
                                s "Oh, shit. I'm an idiot."

                                jump otohahall
                            else:
                                play sound "knock.mp3"

                                s "Hey Otoha, are you in there?"
                                "..."
                                "There's no answer."
                                jump doorknock2

                        "Nodoka (Current Affection - [nodoka_love])" if nodokablock == False:
                            if nodoka_love >= 1 and day != 5:
                                jump nodokadorm
                            if day == 5:
                                play sound "knock.mp3"

                                "I knock on Nodoka's door even though she is right next to me."
                                "I feel embarrassed."

                                no "There's no need to be embarrassed, Sensei. We all make mistakes from time to time."
                                no "At least you didn't accidentally impregnate me."
                                s "I mean...yeah. That would be a lot worse. But that's a weird thing to jump to all of a sudden."

                                jump nodokahall
                            else:
                                play sound "knock.mp3"

                                s "Hey Nodoka, are you in there?"
                                "..."
                                "There's no answer."
                                jump doorknock2

                        "Go Back":
                            jump doorknock2


        "Room 9 (Touka & Yasu)":
            if day304 == False:
                "This room is not yet available."
                jump doorknock2
            else:
                "Who do I want to talk to?"
                menu:
                        "Touka (Current Affection - [touka_love])":
                            if touka_love >= 1 and day != 2:
                                jump toukadorm
                            if day == 2:
                                play sound "knock.mp3"

                                s "Tomoko, are you in there?"
                                to "It is one thing to repeatedly get my name wrong, but to ignore my presence entirely is just unforgivable."
                                s "Oh, there you are."

                                jump toukahall
                            else:
                                play sound "knock.mp3"

                                s "Hey Touka, are you in there?"
                                "..."
                                "There's no answer."
                                jump doorknock2

                        "Yasu (Current Affection - [yasu_love])":
                            if yasu_love >= 1 and day != 4:
                                jump yasudorm
                            if day == 4:
                                play sound "knock.mp3"

                                s "Yasu, are you in there?"
                                ya "I am everywhere."
                                ya "The wind."
                                ya "The water."
                                ya "The hallway."
                                s "Oh, sorry about that."

                                jump yasuhall
                            else:
                                play sound "knock.mp3"

                                s "Hey Yasu, are you in there?"
                                "..."
                                "There's no answer."
                                jump doorknock2

                        "Go Back":
                            jump doorknock2


        "Room 10 (Kirin & Noriko)":
            if day271 == False:
                "This room is not yet available."
                jump doorknock2
            else:
                "Who do I want to talk to?"
                menu:
                        "Kirin (Current Affection - [kirin_love])":
                            if kirin_love >= 10 and day != 4:
                                jump kirindorm
                            if day == 4:
                                play sound "knock.mp3"

                                s "Hey, Kirin. Are you in there?"
                                ki "..."
                                play sound "knock.mp3"
                                s "Hello? Is anyone home?"
                                ki "..."
                                play sound "knock.mp3"
                                s "Kirin, please. It's me."
                                ki "..."
                                s "Huh. I guess she's not home."
                                ki "Are you fucking kidding me?"
                                s "Oh, Kirin. There you are."

                                jump kirinhall
                            else:
                                play sound "knock.mp3"

                                s "Hey Kirin, are you in there?"
                                "..."
                                "There's no answer."
                                jump doorknock2

                        "Noriko (Current Affection - [noriko_love])":
                            if norikoblock == True:
                                play sound "knock.mp3"

                                s "Hey, Noriko. Are you in there?"
                                "........."
                                "......"
                                "..."
                                s "I...guess not."
                                jump doorknock2
                            if noriko_love >= 5 and day != 3:
                                jump norikodorm
                            if day == 3:
                                play sound "knock.mp3"

                                s "Hey, Noriko. Are you in there?"
                                n "Yes. I cloned myself so that you could do both of us at the same time."
                                s "Oh, good. One of the clones is in the hall."

                                jump norikohall
                            else:
                                play sound "knock.mp3"

                                s "Hey Noriko, are you in there?"
                                "..."
                                "There's no answer."
                                jump doorknock2

                        "Go Back":
                            jump doorknock2

        "Go Back":
            if day == 1:
                jump monday2menu
            if day == 2:
                jump tuesday2menu
            if day == 3:
                jump wednesday2menu
            if day == 4:
                jump thursday2menu
            if day == 5:
                jump friday2menu
            else:
                jump weekend2menu

        "Go Home":
            "On second thought, I'll just go home..."

            scene black
            with dissolve
            stop music fadeout 5.0

            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

                    ############################################
                    ##########        ROOM 6          ##########
                    ############################################

label mollydorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if molly_love >= 5 and mollycafe1 == True and mollydorm5 == False:
                jump mollydorm5
            if molly_love >= 10 and mollydorm5 == True and mollycafe10 == True and mollydorm10 == False:
                jump mollydorm10
            if molly_love >= 15 and christmas7 == True and mollydorm15 == False:
                jump mollydorm15
            if molly_love >= 20 and mollycafe20 == True and day != 3 and mollydorm20 == False:
                jump mollydorm20
            if molly_love >= 30 and rindorm50special == True and day > 2 and day < 6 and mollydorm30 == False:
                jump mollydorm30
            else:
                jump mollydormgen
        "Blowjob" if mollyspring2 == True:
            jump mollybjrep

label mollydormgen:
    play sound "knock.mp3"

    mo "Enter, mortal!"

    scene mollydormgen
    with dissolve

    "I decide to spend the night hanging out with Molly in her dorm."
    "She spends the entirety of our time together trying to convince me to get into some video game that she likes and will not allow me to change the topic no matter how hard I try."
    "Normally, I'm fine with girls taking the lead in conversations so I don't need to divulge any information about myself-"
    "But I'd at least prefer to understand what it is that my partner is talking about."
    "Regardless, I pretend to be interested because it makes Molly happy. And even if she's exhausting to be around, her mischievous smile always seems to strike energy back into me."

    scene black
    with dissolve

    "Eventually, it begins to get late and I decide to head home before Tsuneyo gets back from the ramen shop."
    "Molly awkwardly lunges forward as if she wants to hug me but then backs off and gives me a military-style salute instead."
    "What a strange girl..."

    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly's affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label mollyfirsthall:
    scene mollyhall1
    with dissolve

    s "Hey, Molly. What are you up to?"
    mo "Afternoon, Sir! "
    mo "I decided to be adventurous this fine evening and journey outside of my room."
    s "Oh, really? Are you going somewhere?"
    mo "Negative, Sir. This is as far as I am willing to go."
    mo "In order to break the NEET mold, I must stand in this very hallway for at least an hour once a week."
    mo "What a coincidence that you just happened to show up on that very day!"
    s "I mean, I show up on other days too. I don’t think it’s that strange of a coincidence."

    scene mollyhall2
    with dissolve

    mo "Tell me, Sir. Do you believe in fate?"
    s "I feel like I’ve answered this question for someone else before."
    mo "I believe, Sir. I believe we were fated to meet in this very hallway."
    mo "This is a gift from the Heavens above! Or the Hells below! Whichever you believe in!"
    s "And if we don’t believe in either?"
    mo "Then find something to believe in!"
    mo "Or better yet, believe in me!"
    mo "Oh! Even better than that-"
    mo "Believe in the me that believes in you!"
    s "Molly, what the fuck are you even talking about?"

    scene mollyhall3
    with dissolve

    mo "I JUST SHOTGUNNED A MONSTER AND I’M READY TO KICK ASS! LET’S GO!"
    s "If you’re going to ask someone to believe in {i}you{/i} instead of heaven or hell, you’re going to need better reasoning than “I just shotgunned a monster.”"

    scene mollyhall2
    with dissolve

    mo "Let’s face it, Sir. You’ll believe in Molly MacCormack whether she gives you a good reason or not."
    s "And why is that?"

    scene mollyhall4
    with dissolve

    mo "Because cute girls are more powerful than God! Especially ones with green thigh-high’s named Molly!"
    mo "And as further proof, I’ll have you know that I {i}killed{/i} several gods just earlier today in a video game I was playing."
    mo "So if that’s not enough reason for you to worship me, I don’t know what is."
    s "Are you...starting a cult or something?"

    scene mollyhall5
    with dissolve

    mo "Yeah. But it’s a totally wholesome one and I’m not going to ask you to pray or donate or anything."
    mo "We can just hang out, eat junk food, and watch movies."
    s "That...actually sounds like a pretty sweet deal."
    mo "The sweetest deal, Sir."
    s "And where can I sign up for this so-called “Cult of Molly?”"

    scene mollyhall4
    with dissolve

    mo "All I need is eight ounces of your blood. That is enough to perform the ritual."

    scene mollyhall5
    with dissolve

    mo "I’ll also need you to sign a few papers."
    mo "I like to keep things organized, Sir. And without proper documentation for each and every member, things are bound to get wild."
    mo "Just look at Christianity, Sir. There are like ten different kinds now. Would that really have happened if everyone had to sign a form?"
    s "Uhh...Probably?"

    scene mollyhall2
    with dissolve

    mo "Nonsense! Malarky! "
    mo "Real religion is like a gym membership. You sign up ‘cause you think it’s cool and then wind up forgetting about it and ultimately stop caring altogether."
    mo "The Cult of Molly, though...That’s where things become different."

    scene mollyhall4
    with dissolve

    mo "Together, we’ll usher in the end of times! The last of days! The...ending of...stuff!"
    s "You need to chill out with the energy drinks, Molly. Your enthusiasm is going to tear this place down."

    scene mollyhall3
    with dissolve

    mo "Let it burn for all I care! I’ll move in with you and Ami!"
    s "You two would have to sleep in the same bed."

    scene mollyhall6
    with dissolve

    mo "I hope she likes cuddling, Sir. I tend to grab onto things when I sleep, you see."
    mo "It’s a habit I’ve had since birth. "
    mo "I think it’s because I’m so full of love that it possesses me in my sleep."
    mo "It's either that or a demon."
    mo "It could be either one, Sir."
    s "That’s nice, Molly."

    play sound "texttone.wav"
    scene mollyhall7
    with hpunch

    mo "Gah!"

    "Molly’s cell phone suddenly rings from inside of her pocket, causing her to jump up in surprise."

    scene mollyhall8
    with dissolve
    play sound "phonebeep.wav"

    mo "Who the heck is textin’ me at this time of night? Don’t they know that the latest update is supposed to drop in-"

    scene mollyhall9
    with dissolve

    mo "AH! RIGHT NOW! "

    scene mollyhall10
    with dissolve

    mo "Sir...I apologize for cutting this meeting short, but it appears that I have prior engagements."
    s "Go play your game, Molly. I’ll just find something else to do."
    mo "Roger. Please feel free to visit me again soon, though!"
    mo "Preferably on a day where I don’t have games to play!"

    scene mollyhall11
    with dissolve

    s "..."
    s "How am I supposed to know when that is?"

    scene black
    with dissolve

    "I wind up walking around the area surrounding the dorms for a few minutes afterward, hoping to bump into another familiar face. "
    "Unfortunately, I don’t find anything and am forced to go home early..."
    "Oh well, I guess."
    "At least Molly’s probably having a good night."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollyfirsthall = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyofirsthall:
    scene tsuneyohall1
    with dissolve

    s "Hey Tsuneyo. What are you doing?"
    t "..."
    s "..."

    "No response."
    "Is she looking at the board or something?"
    "I glance over Tsuneyo’s shoulder to see if there’s a flyer for...noodles or something, but everything up there seems to be normal."

    s "Hello? Earth to Tsuneyo."
    t "Do you ever just...think about whales?"
    s "..."
    t "..."
    s "Not really, no."

    scene tsuneyohall2
    with dissolve

    t "Did you know that the life expectancy of the blue whale is anywhere from 80-90 years?"
    t "Though, there are some cases in which whales have lived for much longer."
    s "Thank you for this information that I will likely never use again."

    scene tsuneyohall3
    with dissolve

    t "You’re welcome."
    s "So...what are you up to tonight?"
    t "Thinking about whales."
    s "I see that. What {i}else{/i} are you up to?"
    t "..."

    scene tsuneyohall4
    with dissolve

    t "Talking about whales?"
    s "What I’m asking is if you have any plans. "
    s "I don’t have anything to do, so I wanted to see if you’d be down to hang out for a bit."

    scene tsuneyohall3
    with dissolve

    t "In the hallway?"
    s "It doesn’t have to be the hallway. We could go to your room if you’d like."
    t "I think I’d prefer the hallway. "
    t "Being alone in a room with a boy is something I’m supposed to avoid."

    if tsuneyodorm5 == True:
        s "But I’ve been in your room before."
        t "Yes, because it would have been rude for me to deny you entry."
        t "Right now, we are already in the hallway. So I just won’t go back in my room."
        t "We can talk out here."

    else:
        s "Wait, so I’ll never be allowed in?"

        scene tsuneyohall4
        with dissolve

        t "You probably will."
        t "I tend to cave under pressure. "

    s "It's whatever. I'm fine with talking in the hallway, I guess."
    s "I just prefer a topic slightly more interesting than the amount of time whales live."
    t "I can probably manage that."

    scene tsuneyohall5
    with dissolve

    t "Have you met Noodles?"
    s "We literally named him together, Tsuneyo."

    scene tsuneyohall6
    with dissolve

    t "Ah-"

    scene tsuneyohall7
    with dissolve

    s "I’m surprised he’s still up there. How does a bird even get into the dorms?"
    t "Perhaps he is enrolled at the[school]?"
    s "How would a bird even enroll?"
    t "It’s crazy what you can do with a computer nowadays."

    scene tsuneyohall8
    with dissolve

    s "He literally does not have hands. He can’t type."
    s "Wait, he doesn’t know how to read either. This entire topic is flawed."
    t "I had no idea you hated birds so much."
    t "What did Noodles ever do to you?"
    s "I don’t hate birds. I just don’t think-"
    t "You just don’t think they should be allowed to attend[school] like the rest of us."
    s "No, that’s-"
    s "Actually. Yes, that’s right."

    scene tsuneyohall9
    with dissolve

    t "Noodles, attack."
    noodles "Caw!"
    s "Oh, he actually makes noise."
    t "That’s not all he can do."
    s "What is that supposed to-"

    scene tsuneyohall10
    with dissolve

    noodles "Caw!"
    s "What the fuck?"
    s "Where did it get such a small knife?"
    t "Do not ask questions you are afraid to hear the answers to."

    scene tsuneyohall9
    with dissolve

    s "You gave the bird a knife, didn’t you?"
    t "..."
    s "..."
    s "Tsuneyo."
    t "Well, I couldn’t just say no to him."
    s "He {i}asked{/i} you for one?"
    t "I thought maybe he wanted to learn how to prepare dinner for his family."
    s "He doesn’t have a family, though. He would have gone back to them already."

    scene tsuneyohall8
    with dissolve

    t "Perhaps he is just a horrible parent?"
    t "If birds are able to attend[school], it is also possible that they, too, struggle with certain family values from time to time."
    s "They...can’t attend[school], though. How did we get back to this?"

    scene tsuneyohall9
    with dissolve

    t "Noodles, attack."
    noodles "Caw!"
    s "Noodles, don’t attack."
    noodles "..."
    s "Why does he only respond to you?"

    scene tsuneyohall8
    with dissolve

    t "He is thankful that I provided him the tools he needs to prepare dinner for his family."
    s "If you’re going to go with that dinner excuse, you’re going to need to tell him to stop attacking me."
    s "Don’t force Noodles into a life of murder."

    "What is my life becoming?"

    if bonus == True:
        "Why am I arguing with a [teenage]girl about birds when there are several others I can think of off the top of my head that would have sex with me?"

    scene tsuneyohall10
    with dissolve

    noodles "Caw! {i}(Perhaps it’s because you’ve become too complacent with your current life and are just looking for that “chase” once again.)"
    noodles "Caw! Caw! {i}(Or perhaps you find comfort in knowing that there is someone with a fresh view of not only you, but of everything.)"
    noodles "Caaaaw! {i}(A worldview untainted by the evils of man. Just a girl with a passion for her craft and not a care in the world about romance.)"

    scene tsuneyohall11
    with dissolve

    noodles "Caw! {i}(Or perhaps you just want to return things to how they should be?){/i}"

    scene tsuneyohall8
    with dissolve

    s "Okay, I think it might be time for me to leave."
    t "Already? Why?"
    s "I’m beginning to think the bird is talking to me."
    t "But he is talking to you."
    t "I taught Noodles about existentialism."
    s "...How?"
    s "Why?"
    noodles "Caw!"
    t "If you are leaving, would you mind if I asked you a question first?"
    s "Sure, whatever. What is it?"
    t "It’s kind of personal, so I apologize if this crosses any lines."
    s "Just ask the question, Tsuneyo."

    scene tsuneyohall12
    with dissolve

    t "Okay. Well...here goes."

    "Tsuneyo begins to blush and bashfully looks away from me, clearly nervous about whatever she’s about to ask."

    t "Do you think you could..."
    t "..."
    t "Tell me what your favorite breed of whale is?"

    scene black
    with dissolve

    s "Nope. See you later, Tsuneyo."
    s "Have fun with your bird."
    t "But he is {i}our{/i} bird."
    t "You can’t just walk out on us like this."
    t "He hasn’t even started[school] yet."
    s "See you tomorrow."
    t "Get back here, you bastard."

    "..."
    "Well, that certainly was..."
    "One way to spend a Wednesday night."

    s "Tsuneyo is confusing..."
    s "..."
    s "And what the fuck was up with that bird?"

    "{i}Somewhere, off in the distance, the cawing of an existential bird rings out.{/i}"

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyofirsthall = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump endofweekday

label tsuneyohall:
    if chapthreeactive == True:
        scene tsuneyosummer2hallgen1
        with dissolve
    elif christmas7 == False:
        scene tsuneyohall1
        with dissolve
    else:
        scene tsuneyohallwinter1
        with dissolve

    s "Hey, Tsuneyo."
    t "Ah-"

    if chapthreeactive == True:
        scene tsuneyosummer2hallgen2
        with dissolve
    elif christmas7 == False:
        scene tsuneyohall3
        with dissolve
    else:
        scene tsuneyohallwinter2
        with dissolve

    t "What's up, bro?"

    "Tsuneyo and I attempt to have a conversation in the hall to the best of our ability."
    "She tries her hand at speaking informally but, as always, fails dramatically."
    "Either way, we manage to keep the ball rolling for a few minutes and I can feel the...strange bond between the two of us growing stronger."

    $ tsuneyo_love += 1
    stop music fadeout 5.0
    scene black
    with dissolve

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump endofweekday

label mollyhall:
    if chapthreeactive == True:
        scene mollysummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene mollyhall1
        with dissolve
    else:
        scene mollyhallwinter1
        with dissolve

    mo "Evening, Sir! Have you perhaps come to join the Cult of Molly?"
    s "Maybe next time. I kind of just want to talk for now."
    mo "Suit yourself! Please think seriously before joining as all membership fees are non-refundable."
    s "...I have to pay?"
    mo "Aye."
    mo "{i}In blood...{/i}"

    "Molly and I hang out in the hallway for what feels like an hour or two but is probably only a few minutes."
    "She attempts to coerce a few ounces of blood out of me but, knowing that this is completely insane, I am able to refuse."
    "She sighs to herself and tells me that she'll get me eventually, and I wind up walking home while constantly looking over my shoulder."

    scene black
    with dissolve
    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    jump endofweekday

label mollydorm5:
    play sound "knock.mp3"

    "I knock on Molly’s door and wait to see if she responds. "
    "Honestly, I’m not even sure if she’ll be around today...but it’s worth a shot I guess..."
    "I know she works night shifts at the cafe, and it’s not like there’s really any reason for someone other than her or Tsuneyo to come up here for the time being..."

    if bonus == True:
        "But hey, maybe I’ll luck out and she’ll be the leader of some cool lesbian orgy club or something."
        "That would be neat."

    mo "Who goes there?! "
    mo "Have you come to vanquish me?!"
    mo "Prepare yourself, mortal! For I, Molly MacCormack-"
    s "Molly, it’s me. I’m not here to vanquish you."
    mo "That...That voice..."
    mo "Could it be?..."
    s "...Could it be what?"
    mo "Come in..."
    mo "The preparations have already been made."

    scene black
    with dissolve

    "...What preparations?"

    play sound "dooropen.mp3"

    "I sigh to myself and push open the door to Molly’s room."
    "........."
    "......"
    "..."

    scene firstmollydorm1
    with dissolve

    if tsuneyodorm5 == True:
        "I step into Molly’s room and take in the scenery yet again."
        "I hadn’t really paid much attention to Molly’s side of the room when I came to visit Tsuneyo, but now that I’m actually observing it, it seems..."
        "Expensive."

    else:
        "I step into Molly’s room and am greeted by, more or less, exactly what I expected to see."
        "Her side of the dorm is equipped with a bunch of anime memorabilia, a nice looking computer, and several weird looking chairs."
        "While Tsuneyo’s side is..."
        "Well, it has noodles."

    scene firstmollydorm2
    with dissolve

    mo "Hello and welcome to Casa Del Molly! Otherwise known as the “Sanctuary!”"
    s "I’m pretty sure this is just Dorm #6."
    mo "Tomato, tomato."
    s "That phrase really doesn’t have the same impact when it’s spelled out."

    scene firstmollydorm3
    with dissolve

    mo "Whatcha up to, Sir? I’m assuming you’re here for a reason, right? "
    mo "It’s not like a teacher would just visit a [young_girl]’s dorm room just to hang out."
    s "..."
    s "Actually, Molly. I think there’s something you might have to learn about me."
    s "I sort of do this with everyone. Just...show up at their room and get them to kill time with me, I mean."

    scene firstmollydorm4
    with dissolve

    mo "You’re allowed to do that? There aren’t like, rules against guys in girls’ dorms and stuff?"
    s "If there are, I’ve broken them probably several hundred times by now."
    mo "Wack."
    s "You don’t have a problem with it, do you? I know we haven’t really spent much time together but-"

    scene firstmollydorm5
    with dissolve

    mo "Of course I don’t have a problem with it! If anything, this is an excellent development! A great chance to prove my worth!"
    mo "Tell me, Sir. Do you like scantily dressed women? Some even stripped down to their underwear?"

    if bonus == True:
        s "Is this a trick question? Because I feel like this is a trick question."
        mo "No tricks here, Sir. Just degeneracy."
        mo "As it just so happens, I have quite the collection of anime figures, and several of them are wearing next to nothing!"
        s "Oh, those. Yeah I can see those from here. I’m not really into that, to be honest."
    else:
        s "Ew, no. That sounds gross. I only like fully clothed women with a complete disinterest in any form of relationship apart from hug-based ones."

    scene firstmollydorm6
    with dissolve

    mo "Whaaaaat? Not even a little? But I spent so much money on them."

    if bonus == True:
        s "Who spends that much money on plastic anime girls?"
    else:
        s "On women? I am calling the police."
        mo "No, Sir. Anime figures."
        s "Clarify that beforehand, you lunatic."
        s "Do you really spend that much money on them?"

    scene firstmollydorm2
    with dissolve

    mo "I do. And I regret nothing."
    mo "In fact, I’m prepared to spend every penny I earn for the rest of my life on fueling my hobby."
    s "You should probably put together a steady source of income first."
    s "I can’t imagine your part time barista gig will be enough to fuel a hobby as expensive as that."
    mo "I’ll figure out a way to make it work. I won’t have time for games and stuff if I get a full-time job."
    s "Well, just keep in mind that you’ll only be able to live in the dorm for another couple years."
    s "After that, it’s either find work or get used to living on the streets."
    mo "I wouldn’t fare well on the streets. I’ve only known Japanese for a couple years."
    s "Wait, really? You have a bit of an accent, but your pronunciation is spot-on."
    mo "Never underestimate the power of learning through anime, Sir."
    mo "Combine that with language exchange chat rooms and you have one happy, informed weeb, Sir."
    s "Molly, can you please explain to me what a weeb is? I suddenly feel the need to be informed. "
    mo "Are you sure, Sir? What if some plebeian complains about it in the comment section?"
    s "What comment section?"
    mo "No idea, Sir. But here is your daily weebnote! "
    mo "Weebnote: A weeb is any non-Japanese person who becomes obsessed with anime and Japanese culture to the point where it becomes almost cringeworthy."
    s "So like, a foreign otaku?"
    mo "Precisely. "
    s "I don’t really see a problem with that. People like what they like."

    scene firstmollydorm7
    with dissolve

    mo "If only everyone else looked at things that way."
    mo "I can’t even cosplay at conventions in Japan without people lookin’ at me all weird and stuff."
    mo "I’m lucky enough that the manga club accepts me, but even that I kinda had to beat my way into."
    s "Oh come on. That can’t be true. Ami and Rin are in that club and they’re accepting of pretty much everyone. "
    mo "That’s true. But even then it’s like, I can’t help but feel like they looked at me a little weird at first."

    scene firstmollydorm2
    with dissolve

    mo "But hey! They’re two of my best pals ever now and I couldn’t be happier to be livin’ out my dreams in the land of the rising sun!"

    "Interesting."
    "I guess Molly’s just seemed so...overly-confident so far that it never really occurred to me that there was a time where she felt out of place."
    "But I can absolutely understand why."
    "It must be hard looking different than everyone else. Especially in a place as closed off as Kumon-mi. "

    if ayanedorm15 == True:
        "In fact, I remember Ayane telling me something a while back about how outsiders aren’t really as accepted here as they probably should be."
        "And even then, she was talking about Japanese outsiders from different prefectures."
        "I can only imagine what it’s like for someone from a completely different country."

    else:
        "But I guess foreigners are bound to be looked at strangely no matter where they are. That’s just human nature, unfortunately."

    mo "Well, uhh, anyway! How do {i}you{/i} feel about cosplay, Sir?"
    mo "Are you one of those people who thinks it’s embarrassing? Or are you one of those people who thinks it’s the greatest thing ever?"
    s "Is there no middle ground?"
    mo "There is not."
    s "Oh. Well it wouldn’t matter anyway because I’d definitely choose option two."

    scene firstmollydorm4
    with dissolve

    mo "Really? Even though you don’t like anime and stuff?"
    s "You don’t need to like anime to appreciate girls in cute costumes. And I very much appreciate that."

    scene firstmollydorm2
    stop music fadeout 10.0

    mo "Then perhaps you can still be saved after all..."
    mo "For you see...I, Molly MacCormack, am a self-proclaimed master-cosplayer!"
    s "Adding “self-proclaimed” to the title really takes away from how impressive it is, but I can’t say I’m not intrigued. "
    mo "Would you like to see a little sample?"

    "Fuck yes I would. But it’s not like I can just come out and say-"

    s "Fuck yes I would."

    "Damnit."

    scene firstmollydorm9
    with dissolve

    mo "Excellent...{i}Excellent{/i}."
    mo "Then...If you would be so kind as to follow me to the bed...We can get started."
    s "Yes please."

    scene black
    with dissolve

    "Molly shyly turns around and hops onto her bed."
    "I follow quickly behind her and she-"

    scene firstmollydorm10
    with hpunch
    play music "rapid.mp3"

    mo "{i}Darkness blacker than black...darker than dark...{/i}"
    mo "{i}I beseech thee...combine with my deep crimson.{/i}"
    mo "{i}The time of awakening cometh!{/i}"
    s "Uhh..."

    scene firstmollydorm11
    with dissolve

    mo "{i}Justice fallen upon the infallible boundary...{/i}"
    mo "{i}Appear now as an intangible distortion!{/i}"
    mo "{i}I desire for my torrent of power...a destructive force!{/i}"
    mo "{i}A destructive force without equal!{/i}"
    mo "{i}Return all creation to cinders and come out from the abyss!{/i}"

    scene firstmollydorm12
    with dissolve

    mo "{i}EXPLOOOOOOOO...SION!{/i}"
    s "..."
    mo "..."
    s "..."
    mo "..."
    s "..."
    mo "..."

    scene black
    with dissolve
    stop music fadeout 5.0

    "Molly drops her staff and hops off of the bed, skipping over to her computer desk."

    scene firstmollydorm13
    with dissolve
    play music "sweetvermouth.mp3"

    mo "So? Whaddya think? Pretty cool, right?"
    s "I mean...it was a cool monologue. But I don’t really know if I would count just a staff as cosplay."

    scene firstmollydorm14
    with dissolve

    mo "That’s where you’re wrong, Sir. A good cosplayer must not only wear the costume, but embody the personality of the character as well."
    s "Okay, sure. But there was no costume at all."
    mo "The costume is in my wardrobe."
    s "..."
    mo "..."
    s "Are you going to put it on?"

    scene firstmollydorm15
    with dissolve

    if bonus == True:
        mo "R-Right now?...With you just...standing there watching me?"
        mo "I know that you’re my master, but this is..."
        s "Actually, on second thought, don’t worry about it. I’m sure I’ll see it eventually and I imagine that speech took a lot out of you."
    else:
        mo "Right now?"
        s "Of course not. When you are in private and do not feel any discomfort as a direct result of my presence."
        mo "Oh. Probably."
        s "Cool. Also, nice speech."

    scene firstmollydorm14
    with dissolve

    mo "I’ve practiced it like two-hundred times. In fact, Tsuneyo probably even knows it now from how much I’ve been doing it lately."
    s "I...would very much like to see her attempt to do what you just did."
    mo "We will convince her together."
    mo "She’s gorgeous so I wanna see her get dressed up too."
    mo "And Ami."
    s "My Ami?"
    mo "Your Ami. She’s been wanting to cosplay for a while and we’re close to the same size, so I’m gonna let her try on some of my stuff."

    if bonus == True:
        s "Please, for the love of god, show me when you do."
        mo "I will have her send pictures. "
        s "Thanks Molly. I had no idea you were such a great-"
        mo "500 Yen each."
        s "...Salesman."
        mo "I learned from a wise man that I must start making more money as soon as possible or I will be forced to live on the streets. "
        s "..."
        mo "..."
        s "500 Yen each?"
        mo "500 Yen each."
        s "Deal."
    else:
        s "Just make sure the fabric isn't too scratchy. She has soft skin and I do not want her to get hurt."
        mo "I understand, Sir. I will take good care of her."

    scene black
    with dissolve2

    if bonus == True:
        "Molly and I shake hands and I feel like I’ve just agreed to doing something very suspicious."
        "But hey, suspicious is pretty much my middle name at this point. "
        "And if the only thing separating me from seeing a bunch of cute girls in costumes is some pocket change, so be it..."
        "..."
        "I would have probably even paid more if she asked."
    else:
        "Molly and I shake hands. I am glad that she is going to protect my accountant."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollydorm5 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollydorm10:
    play sound "knock.mp3"

    "I knock on Molly’s door and wait to see if she’s around."
    "I can hear the sound effects from some game or anime going off in the background, so I imagine she is."
    "Tsuneyo doesn’t seem like she would be the type to spend her free time on that, so process of elimination really only leaves the one I came here to see in the first place."

    mo "Who goes there?!"
    s "Your teacher."
    mo "Oh, Master!"
    mo "You may enter! "

    "I grab the handle and attempt to open the door, but it appears to be locked."

    s "I can’t enter if the door is locked, Molly."
    mo "Oh. Uhhh, crap. Give me a second. "
    mo "I’m in the middle of a thing in a game."
    s "Can’t you just pause it?"
    mo "Pause it? What year is this, 2005?"
    mo "Have I activated my time-jump ability on accident?!"
    s "Just...hurry up and finish your game. It always feels strange standing in the middle of the hallway here."
    mo "Roger! Just gotta pop my CD’s and..."
    s "..."
    mo "..."
    s "..."
    mo "Done!"

    "I hear a set of frantic footsteps clopping against the floor as Molly rushes to the door and pulls it open."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "What ever happened to the good old days where you were able to pause video games?"

    scene mollydormten1
    with dissolve

    mo "Those days have long since vanished, Sir. Lost like teardrops in the rain."
    s "Insightful. Is that a line out of a dating game?"
    mo "Probably, Sir. Though I don’t know which one off the top of my head."

    "Molly begins to play with one of the sleeves of her hoodie, incessantly plucking at the same spot over and over again."
    "She looks surprisingly cute in her...rather Irish-themed pajamas."
    "I can’t help but notice a rather fresh aroma permeating throughout the room as well."

    s "What is that smell? "
    mo "Me, Sir. Lemon scented shampoo. "
    mo "I just took a bath with Ami and Maya."
    mo "We were discussing the logistics of our upcoming campaign at the edge of the world."
    s "You mean the beach?"
    mo "I do, Sir. The beach is what it appears as to those not blessed with clairvoyance."
    mo "But people like you and I see it for what it truly is."
    s "I see it as a beach."

    if bonus == True:
        mo "You will know the meaning in time, Sir. A beach is not simply a beach when it is filled with blossoming [young]ladies like myself, Sir."
        mo "A true haven for degeneracy. A real set-up for top-notch H-scenes and lost bikini tops."
        s "I think you watch too much anime."
        s "{i}Though, I guess none of that sounds bad to me.{/i}"
    else:
        mo "But the fanservice, Sir!"
        s "You watch too much anime. There is no fanservice in Lessons in Love."

        "Or at least...not anymore there's not..."

    scene mollydormten2
    with dissolve

    mo "There is no such thing as too much anime. Especially when there are so many cute figures to collect."
    s "You’re still planning on getting more? You have plenty."

    if bonus == True:
        mo "Always, Sir. I will spend every penny I earn from the cafe and the pictures you purchase from me on objects to fuel my passion."
        s "Speaking of which, do you happen to have any of those pictures yet?"
        s "Plenty of time has passed by, so if you don't have any, you owe me a good excuse."

        scene mollydormten3
        with dissolve

        mo "I regret to inform you that I do not have any. Please accept the following excuse."
        mo "The stuff I ordered online just came in the other day and none of it really fits. I’m growing at an alarming rate."
        s "I’m having a hard time believing that. You’re one of the smallest girls in the class."

        scene mollydormten4
        with dissolve

        mo "Day by day, I stray further and further from the loli tag."
        mo "Who will ever love me if I become an average-sized girl?"
        s "I mean, I think you’d be cute either way."
    else:
        mo "Is that a problem, Sir?"
        s "Absolutely not. You are a grown woman with the money to fund her hobbies and I will enthusiastically support you if it means bringing you even slightly closer to happines."

    scene mollydormten5
    with dissolve

    mo "Thank you, Sir. I would return the compliment if you had one less dimension."
    s "You’re sure blushing a lot for someone who isn’t interested in 3D characters."

    if bonus == True:
        mo "Hormones, Sir."
        mo "They control the brains of [young]women like myself and make us act in ways we normally regret."
        s "Is that Mollyspeak for saying you’re getting turned on?"

        scene mollydormten6
        with dissolve

        mo "O-Of course not! What would the players think if an innocent virgin like me received her first H-scene in her initial update?!"
        s "I’m sure there would be plenty of players who’d be absolutely thrilled by that."

        scene mollydormten7
        with dissolve

        mo "Guh...I’m not ready to grow up yet..."
        mo "I haven’t even unlocked the fabled “first kiss” CG. "
        s "Kissing is overrated anyway. Once you get older, you’ll realize that relationships become more about sex than actual affection."
        s "Well, in my experience at least."

        scene mollydormten8
        with dissolve

        mo "Sir, this may be hard for you to hear, but I’m beginning to feel a bit uncomfortable with the direction this conversation is headed."
        mo "It’s one thing to talk about sex in games, but the real life kind sounds...scary."

        scene mollydormten9
        with dissolve

        mo "Though...I suppose if you were to use a command seal..."
        mo "I would be forced to oblige..."
        s "..."
        mo "..."

        "Molly is clearly starting to get a little flustered, so I might as well take things down a notch before I actually do something to hurt her."
        "Despite being a full on, admissible pervert when it comes to video games, she still clearly isn’t ready for the actual thing yet."
        "But I guess that’s not too hard to understand given the type of person she is."
        "It seems that Molly is willing to do virtually anything in order to separate herself from the real world. "
        "And if deflowering every character in every game she plays is how she wants to do that, more power to her."
    else:
        mo "I just remembered a really embarrassing thing that happened to me once!"
        mo "It was in the original version of the game, though!"
        s "Can you tell me about it?"
        mo "I can not, Sir! It is against the rules!"

    scene mollydormten10
    with dissolve

    mo "Oh! Sir!"

    if bonus == True:
        s "Wow. You got over that whole 'hormonal embarrassment' thing pretty quickly. "
    else:
        mo "I forgot to pick up my laundry from downstairs! Please help me carry all of it up here so my arms do not snap!"
        s "Just do it later. My legs feel all blah and I like how your room smells."
        mo "It {i}is{/i} later, Sir! I meant to do it at five different points today."
        s "Just get better at remembering stuff. I don't know what you want from me."
        mo "Unfortunately, I can not."

    mo "ADHD, Sir. There's not a lot of space on my hard drive so I need to constantly delete things to make place for new ones."

    if bonus == True:
        s "Gotcha. So what is it that captured your mind this time around?"
    else:
        mo "Oh, look. A chair. Chairs are for sitting."

    scene mollydormten11
    with fade

    "Molly moves several steps closer to her computer and starts to look at something in the corner of the room."
    "I stare at the same corner as well and see nothing, so I’m not quite sure what it is she’s looking at."

    mo "I actually have something I’d like to confide in you about."
    s "Oh? What’s with the sudden shift in tone?"
    mo "I will explain the step-by-step process as to how I wound up here."

    if bonus == True:
        mo "It all began with the mention of sex."
        mo "Which then made me think about nudity."
        mo "Which then made me think about my own personal experiences with nudity."
        mo "Which then reminded me of something I saw recently."
        mo "Which then somehow distracted me from thinking about the thing that made me think about all of those things in the first place."
        s "I’m...not sure if I follow."
        mo "Then I will get right to the point."
    else:
        mo "First, I was over there. Then I was somewhere in the middle. Now I'm here."
        s "I feel like the music is about to turn off."

    stop music
    scene mollydormten12

    mo "What is the right thing to do when you find out that someone you care about is hurting themself? "
    s "..."
    mo "I think I saw something I wasn’t supposed to see."
    mo "I don’t know what to do."
    s "..."
    s "Is it okay if I ask for a few more details?"

    "I’m almost positive I know what this is about, but I don’t want to reveal anything until I’m sure."

    scene mollydormten13
    with dissolve

    mo "Well...Let’s just say that girls sometimes use the same dressing room as one another when they go shopping."
    mo "And a girl I happened to be changing with had some marks on her that I’m smart enough to recognize."
    mo "I might be a huge geek, but I know when to snap out of it."

    scene mollydormten14
    with dissolve

    mo "I obviously didn’t say anything because like, what do you even say when you see something like that?"
    mo "“Are you okay? What happened? Do you need help?”"
    mo "Those are all things that would make her catch on."

    scene mollydormten15
    with dissolve

    mo "And now I’m in this weird place where there are a million things I wanna say but none of them will come out because I’m afraid of people getting mad at me."
    s "..."
    s "This person sounds really important to you."

    scene mollydormten16
    with dissolve
    play music "closeto.mp3"

    mo "..."
    mo "Yeah."
    mo "They are."
    mo "..."
    mo "Very important."
    mo "Like, so important that I just wanna squeeze her and be like “Wake up!” and not let go until she promises to not do anything like that again."

    scene mollydormten17
    with dissolve

    mo "My mom killed herself when I was little. So ever since then I’ve tried to be really conscious about how other people feel."
    mo "But even when you know they’re not feeling well, it’s not like you can actually do anything about it."
    mo "You can’t even make jokes because then it will seem like you’re just brushing everything off."
    mo "So I wanna know what you would do in my position."
    s "..."

    scene mollydormten18
    with dissolve

    mo "Hahah...Hahahah! Pretty crazy how we wound up here all of a sudden, right?"
    mo "The dorms must be possessed by some kind of dark entity or something! Right?"
    mo "That’s gotta be it!"

    scene mollydormten19
    with dissolve2

    mo "That’s gotta be it..."
    mo "And it’s gotten to her too. And it’s making her do weird things to her arms. "
    mo "So all we need to do is take down whatever entity is spreading all of these negative emotions around and everything will go back to normal."

    scene mollydormten20
    with dissolve

    mo "Everything will go back to normal. "
    mo "It’s all just part of an evil conspiracy. "

    "Molly picks at the fabric of her clothes even harder than before."
    "Her hands are shaking as tears begin to slowly but surely stream down her pale, white cheeks and drip onto the sleeves of her hoodie."
    "Meanwhile, I sit across from her...At a table the same girl she’s so concerned about often shows up to in order to play games and get away from everything."
    "We’re all looking to get away from everything. And we all have different ways to do that."
    "But what happens when someone you know forgets how? "
    "What do you do?"
    "I doubt Molly {i}wanted{/i} to talk about this at all."
    "It just managed to grab hold of her and force her head underwater before she could do anything about it."
    "And so everything just started to leak out."
    "Everything always leaks out."

    s "This sounds like a job for your master."

    scene mollydormten21
    with dissolve2

    mo "Huh?..."
    s "Come on...Don’t drop the act now."
    s "I finally start playing along and you’re going to give me that face?"
    s "If you care so much about this person and you want to get rid of the “demon” or whatever it was you said was possessing them, we just have to defeat it. Right?"
    s "Maybe it’s time I show off {i}my{/i} true power?"
    s "I’m the Supreme whatever it is-"

    scene mollydormten22
    with dissolve

    mo "Supreme Overlord. Herald of the Adolescents."
    s "Yeah. That thing. "
    s "And besides, I’m pretty sure I know who you’re talking about anyway."

    scene mollydormten21
    with dissolve

    mo "You do?"
    s "Yeah. It’s something I’ve known about for a while. And I care about her just as much as you do."

    scene mollydormten23
    with dissolve

    mo "Oh yeah?"
    mo "You dare challenge the love of the Emerald Guardian of the Crystal Forest?"
    mo "You may be my master, but you must know by now that there are aspects of power where even {i}I{/i} surpass you."

    "Her eyes return to the same corner she’s continuously focused on throughout this impromptu confession. "
    "I guess it’s a habit of hers. Just like plucking at the strings of fabric on her clothing."
    "It’s great being able to find things that will calm you down while your mind runs wild. "
    "You need to stay grounded or you’ll eventually just float off into the ether."
    "There’s your half-assed philosophy for the day, coming from a man who seems to always just-so-happen to be around girls when they start to cry."
    "Sometimes, I wonder if they’d cry at all if I were to just leave."

    s "There’s no need to challenge anyone here. It’s clear how worried you are by how you’re acting right now."
    mo "That’s because of the dark entity."
    s "Right. The dark entity."
    s "So if the dark entity happens to wipe our memories of this conversation, everything will be just like it was before, right?"

    scene mollydormten24
    with dissolve

    mo "It can do that?!"
    mo "It’s even more powerful than I thought!"
    mo "Are you sure you’ll be able to handle it, Master?"
    mo "I may be small, but I’m willing to assist you in any possible way. Just name it!"

    "It’s hard for me to tell if Molly is just acting right now or if all of these words are her true feelings wrapped in intentionally faked delusions of grandeur. "
    "Maybe she {i}does{/i} think that there is something she can do to help bring Rin back to normal."
    "But before any of that, I need to find out if something’s actually going on again or if the marks she saw were the same ones I did."

    s "You can assist me by guarding yourself, Molly. You’re of no use to me if you fall victim to the darkness as well."

    scene mollydormten25
    with dissolve

    mo "Ahh, an excellent plan, Sir. I will support you from the backlines, just as any good priest would."
    mo "I’ll be sure to cast Power Word: Shield on you before you pull."
    s "I...wouldn’t have it any other way."

    scene black
    with dissolve2

    "We find a way to carry on our conversation without ever directly addressing anything again."
    "Life is easier that way."
    "Sometimes, you need to disguise your problems as happier things to avoid {i}the dark entity{/i} consuming you."
    "And even if Molly is too much to handle at most hours of the day, I {i}do{/i} want to protect her."
    "Just as I want to protect the rest of the girls."
    "She doesn’t deserve to be beaten down the way so many others have been."
    "So if there’s anything I can do about that-"
    "I will gladly do it."

    $ renpy.end_replay()
    $ molly_love += 3
    $ mollydorm10 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat


label tsuneyodorm:
    if tsuneyo_love >= 5 and ramen1 == True and tsuneyofirsthall == True and tsuneyodorm5 == False:
        jump tsuneyodorm5
    if tsuneyo_love >= 10 and ramen10 == True and tsuneyodorm5 == True and tsuneyodorm10 == False:
        jump tsuneyodorm10
    if tsuneyo_love >= 15 and ramen15 == True and day != 1 and tsuneyodorm15 == False:
        jump tsuneyodorm15
    if tsuneyo_love >= 20 and tsuneyodorm15 == True and day != 5 and day247 == True and tsuneyodorm20 == False:
        jump tsuneyodorm20
    if tsuneyo_love >= 25 and secondbeach18 == True and day != 1 and tsuneyodorm25 == False:
        jump tsuneyodorm25
    else:
        jump tsuneyodormgen

label tsuneyodormgen:
    play sound "knock.mp3"

    t "Noodles."
    t "Oh. I mean, come in."

    scene tsuneyodormgen
    with dissolve

    "I decide to spend the night hanging out with Tsuneyo in her dorm."
    "And by 'hanging out' I mean that we essentially stare at each other without saying anything for an hour or two."
    "And not in the romantic or sexual way either. It's sort of like an awkward exchange between two people who have no idea what to say, so they elect to say nothing instead."
    "Such is dating in this day and age."
    "Eventually, she starts talking about soup because she is Tsuneyo and it is the only thing she has a defined opinion on."
    "It's a little strange to me how she's managed to get so far in life with what seems to be no feelings whatsoever."
    "But I'm sure that line of thinking is just me being presumptuous and not taking into account her situation at home."

    scene black
    with dissolve

    "Eventually, it gets dark and Tsuneyo asks me if I'd like to walk with her to the store so she can buy some things for her room."
    "I agree and the two of us set out into the night, parting ways once we get to a nearby 7/11."
    "And even though there weren't many words exchanged between the two of us, I still can't help but feel like we've grown closer..."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo's affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label tsuneyodorm5:
    play sound "knock.mp3"

    "I knock on Tsuneyo’s door and wait to see if she’s around."
    "I doubt that there has ever been another male to visit her at home, so it’s not like I’m going to hold it against her if she doesn’t feel comfortable letting me in."
    "She might be aloof and...strange, but it’s not like she lacks common sense."
    "I think."
    "Who really knows, though?"

    t "Who is it?"
    s "Your teacher."
    t "Oh. Hello."
    t "Business hours don’t start for another thirty minutes."
    s "So you’ll let me in if I wait out here for thirty minutes?"
    t "Yes."
    s "Wait, what kind of business are you even running in there?"
    t "Ramen."
    s "You run a ramen shop out of your dorm as well?"
    t "Dorm?"
    t "Ah-"

    "It is just then that Tsuneyo seems to realize something."

    stop music fadeout 10.0

    t "I’m sorry. I’m still not used to living here."
    s "How did you confuse a dorm room for a noodle house?"
    t "Every house is a noodle house if you try hard and believe in yourself."
    s "..."
    t "..."
    t "You may enter."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Tsuneyo pulls the door open from the inside and I wander into the room, nodding at her as I do so."

    scene tsuneyofirstdorm1
    with dissolve
    play music "oldweather.mp3"

    if mollydorm5 == False:
        "The place is...more or less what I expect it to be. Filled with various [teenage]girl things and..."
        "And a giant portrait of Tsuneyo’s favorite food."

    else:
        "It feels a little different being in here to see Tsuneyo instead of Molly. "
        "And that’s not saying I don’t like her or anything. I obviously do since I came to visit her. She’s just...you know."
        "But at least this finally gives me a chance to ask about the giant portrait of ramen on the wall."

    scene tsuneyofirstdorm2
    with dissolve

    t "I apologize for forgetting where I was. That happens sometimes."
    s "That’s not a good thing to happen on a persistent basis."
    t "There are worse habits."
    t "Like drug use. Or jump-rope."
    s "I’m struggling to see how exactly jump-rope is a bad habit...but you do you, Tsuneyo..."
    t "Then you have not jumped enough ropes in your life."
    s "I suppose I have not."
    t "Would you like a tour of the room? There are no ropes involved."
    s "None? Damn. There go my plans."
    t "I do not understand."
    s "Figures. You can show me around if you’d like. I can't imagine it will take very long."
    t "I understand."
    t "Please follow me."

    scene tsuneyofirstdorm3
    with fade

    "Tsuneyo leads me over to her bed and immediately begins the “tour.”"

    t "This is where I sleep. "
    t "You will notice several llamas on the shelf above my bed."
    t "There is a simple reason for this."
    s "Is the reason that you like llamas?"
    t "Correct."
    s "Who could have possibly seen that coming?"
    t "Your sarcasm irritates me."
    s "You’ll get used to it."
    t "I hope not."

    scene tsuneyofirstdorm4
    with dissolve

    t "To the right of the llamas, you may have noticed a large bowl of ramen."
    t "This is because-"
    s "You like ramen?"

    scene tsuneyofirstdorm3
    with dissolve

    t "You are ruining the tour."
    s "Sorry. Even with your love for noodles, though, I'm surprised that portrait is...as big as it is."
    s "It’s probably even more eye-catching than all of Molly's figures and some of them aren't even fully clothed."
    t "Thanks, bro."

    scene tsuneyofirstdorm4
    with dissolve

    t "The most interesting part of this particular bowl of ramen is that it was not made by me."
    s "Who was it made by, then?"
    t "I do not know. It simply arrived here one day and I did what any rational woman would do and hung it up directly beside my bed."
    s "Yup. Seems rational enough."

    scene tsuneyofirstdorm3
    with dissolve

    t "I have never lived with another [teenage]girl before, but I understand that we are supposed to cover the wall in things we like."
    t "And I could not get actual noodles to hang properly."
    s "..."
    t "..."
    s "Please tell me that was a joke."
    t "That was a joke."

    "Hey, I finally caught one. Maybe I’m beginning to understand Tsuneyo after all?"

    s "Here’s the thing, though, Tsuneyo."

    scene tsuneyofirstdorm5
    with dissolve

    t "Ah-"
    s "Normally, [teenage]girls will hang up posters of...their favorite bands or TV shows. Or in Molly’s case, a bunch of weird stuff."
    t "Is liking noodles strange?"
    s "Liking them as much as {i}you{/i} do is strange. It’s time to develop new hobbies."
    t "Hobbies?"
    s "Yeah. Like, didn’t you say you did Kendo when you were younger? How about hanging up...Kendo stuff?"

    scene tsuneyofirstdorm3
    with dissolve

    t "Oh. Please allow me to use that topic for what people in show business call a “segue.”"
    t "Follow me, please."

    scene tsuneyofirstdorm6
    with fade

    "Tsuneyo quickly moves past me before turning around and mirroring her pose from the first section of the tour."

    t "Welcome to the more interesting side of Tsuneyo Tojo."
    s "I don’t think stacking a few bamboo swords in the corner really qualifies as interesting. It's barely even a hobby if you don't use them."
    t "Would you prefer I attacked you with them?"
    s "That was a joke too, right?"
    t "..."
    s "..."

    scene tsuneyofirstdorm7
    with dissolve

    t "...Yes."
    s "The hesitation right there did not make me feel comfortable."

    "If Tsuneyo actually {i}did{/i} attack me, it’s not like I wouldn’t be able to defend myself, right?"
    "I mean, she can’t be that good at Kendo, can she?"

    s "I would have liked watching you do all that sword stuff whenever you were into that, Tsuneyo."

    scene tsuneyofirstdorm6
    with dissolve

    t "Really? Why?"
    s "I don’t know. Just feel like it would be kind of cool to see you...actually doing something."
    s "I doubt it was anything intense, but still-"
    t "I was the national junior Kendo champion three years in a row."
    t "It was the only thing I ever left home for."
    s "Wait...national? As in the entire nation?"

    scene tsuneyofirstdorm7
    with dissolve

    t "Does that word have another meaning I am unaware of?"
    s "..."
    s "If...you won the national championship three years in a row, why did you stop?"

    scene tsuneyofirstdorm6
    with dissolve

    t "To take care of my father and carry on the family’s legacy."
    s "The noodle legacy?"
    t "The noodle legacy."
    s "You gave up an amazing talent for that?"
    t "There is no talent more amazing than making soup."
    t "Not having to train gives me more free time, though. I can do anything I want now."
    t "I am essentially a soup god."
    s "Weren’t we literally just talking about how you need hobbies apart from your job, though?"
    t "That was a topic you brought up without my participation. Do not lump me in with the likes of you, damn it."

    scene tsuneyofirstdorm8
    with dissolve

    t "Now that I am a normal [high_school] girl, I am free to make my own decisions and choose my own hobbies."
    t "Thankfully, the Emerald Guardian has recently informed me of a wonderful sounding game where you can kill people and not be prosecuted for it."
    t "This is the path that I will walk congruently alongside noodles."
    s "What, like a...video game or something?"
    t "There is no video involved. It is called Dungeons & Dragons."
    t "She says she is going to teach me."
    t "If that goes well, I may replace my ramen portrait with a creature that I have always known is fake. The dragon."
    s "Don’t try and trick me into forgetting what you said at the ramen shop, Tsuneyo."

    scene tsuneyofirstdorm9
    with dissolve

    t "Ah-"
    s "Still, though...it’s good that you and Molly seem to be getting along."
    s "You’re kind of polar opposites, so I wasn’t sure how that would work out."
    t "I imagine it is due to my lack of personality."
    s "Hey now, there’s no need to put yourself down about it."
    s "What you lack in personality, you make up for in the desire to improve."
    t "..."
    s "..."

    scene tsuneyofirstdorm10
    with dissolve

    t "..."

    "Well, looks like her little put-down right there was supposed to be a joke as well."
    "But hey, least I was able to catch one today."

    t "The Emerald Guardian was right..."
    t "I am a “normie” after all."
    s "A what?"
    t "It means normal person. I think."
    t "I was under the impression being normal was the right thing to do, but she makes it sound like I am evil."
    t "Perhaps it is time for me to move back home. I am not prepared for this world."
    s "You can’t move out yet. What will happen to Noodles?"
    t "That’s exactly why I have to go home. The noodles need me."
    s "No, no. I mean Noodles the bird. The one that we named."

    scene tsuneyofirstdorm11
    with dissolve

    t "Oh! {i}Noodles!{/i}"
    t "Yes. Noodles would be quite lonely without me. "
    t "Your [niece] with the soft legs keeps trying to “rescue” him, but I wish she would stop."
    t "He is well-fed. I have been making sure of it."
    s "Well, at least I don’t need to take a guess about what you’re feeding him."
    t "That’s right."
    s "Can birds really survive off of just n-"
    t "Bird seed."
    s "..."
    t "My father taught me about the right things to feed birds when I was still a little girl."

    "That's...actually kind of cute."
    "I guess Tsuneyo’s relationship with her father is one of those more loving and sentimental ones?"
    "Is she really okay spending so much time here when he’s so sick?"

    scene tsuneyofirstdorm12
    with dissolve

    t "I remember it vividly."
    t "We would wake up early every morning and head to the backyard to feed the chickens."
    t "It was almost as if they were part of the family."
    t "And then, once they were fully grown, we would snap their necks and pluck their bodies clean of feathers for use in our food."

    "Okay, never mind. I’m sure her father will be fine alone."

    s "You...were trained to kill chickens as a little girl?"

    scene tsuneyofirstdorm13
    with dissolve

    t "I was trained to kill many things as a little girl."
    t "My father is incredibly protective."
    t "If he knew I was alone in a room with a man, he would have you executed."
    s "..."
    t "..."
    s "You’re not going to tell him about this, are you?"
    t "I am."
    s "But...you just said that he’d have me executed."
    t "Yes."
    s "Are you...trying to have me killed?"
    t "..."
    s "Tsuneyo."

    scene tsuneyofirstdorm9
    with dissolve

    t "Ah-"
    s "I’m not ready to die yet. You can’t tell your father about this."

    scene tsuneyofirstdorm13
    with dissolve

    t "That would be breaking the rules, though."
    s "It’s okay to break rules every once in a while."
    t "But if I break the rules, all of my teeth will turn to liquid."
    s "What the fuck has your father been teaching you?"
    t "That my teeth will turn to liquid if I break the rules. Please pay attention."
    s "Just...please don’t tell him. Okay? I promise to keep spending money at the restaurant as long as he doesn’t know that I visit you here."
    t "How much money?"
    s "Does it matter?"
    t "Yes."
    s "This is starting to sound like extortion. "
    t "It is, more or less."
    s "I’ll spend...a good amount of money. I promise."
    t "..."
    s "..."
    t "Fine."
    t "But I am not doing it for you. "
    t "I’m doing it for Noodles."

    scene tsuneyofirstdorm14
    with dissolve

    t "You participated in naming him, so I don’t think he’d be happy if you were to suddenly vanish."
    s "I think it’s safe to say there would be a lot of unhappy people if I were to suddenly vanish."

    scene tsuneyofirstdorm13
    with dissolve

    t "I wouldn’t mind."
    s "Thanks, Tsuneyo."
    t "You’re welcome."

    scene black
    with dissolve2

    "I decide against asking her if that last one was a joke or not since I’m mildly afraid of the answer I’d receive."
    "But, at the end of the day, I was able to spend some more time alone with her."
    "And even if she threatened to kill me and admitted to murdering animals, I feel like the two of us managed to grow closer..."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyodorm5 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyodorm10:
    play sound "knock.mp3"

    s "Tsuneyo, are you in there?"
    s "Let’s hang out."

    "I hear a set of footsteps quietly approach the door and stop right in front of it."

    t "Why?"
    s "Why not? I’m bored and you’re not doing anything."
    t "I’m doing plenty of things."
    s "What could you possibly be doing in there?"
    t "Homework."
    s "I don’t give you any homework."
    t "Noodle homework."

    "...What the fuck does that even mean?"

    t "Studying different types of wheat."
    s "Why?..."
    t "Why not?"
    s "Put your noodles on hold for a few minutes and talk to me. "
    t "..."
    s "..."
    t "Okay."
    t "Please enter."
    s "Thank you..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Tsuneyo unlocks the door and I make my way into the room, stepping over a few plastic bags piled near the entrance along the way."

    scene tsuneyodormten1
    with dissolve

    t "Hello."
    s "Hey. What’s up with the pajamas?"
    t "What do you mean?"
    s "I mean like...They’re cute and everything...but what’s up with that smiley face?"
    s "It’s kind of creepy, don’t you think?"

    scene tsuneyodormten2
    with dissolve

    t "It’s a normal smile. Don't make fun of my clothes just because you hate joy."
    s "I don’t {i}hate{/i} joy."

    scene tsuneyodormten1
    with dissolve

    t "Then why don’t you ever smile?"
    t "You should try to be like this shirt. But with more energy and less cotton."
    s "You’re the last person I want to hear about energy from. You have like three facial expressions."
    t "Did you come here to fight?"
    s "What? No. I was just going along with your banter."
    s "Besides, I think you look cute. Even if your shirt is a little weird."

    scene tsuneyodormten3
    with dissolve

    t "Weird?"
    s "Well...Not weird. Just different."
    t "That doesn’t sound any better."

    scene tsuneyodormten1
    with dissolve

    t "This shirt was a gift from my father and I would greatly appreciate it if you would keep your comments to yourself."
    t "I am embarrassed enough to be seen like this in general."
    s "You don’t look very embarrassed to me."
    t "That's because I only have three facial expressions. You said it yourself."

    "Yeah, but I feel like one of those is actually the embarrassed one."
    "Tsuneyo seems fine to me. Sure, her posture is a little different than normal, but it’s not like she’s curled up in the corner or anything."

    scene tsuneyodormten4
    with dissolve

    t "So is there a real reason for your appearance today? Or is it just to hurt me?"
    s "I’m not here to hurt you..."
    t "You have the eyes of a man who is here to hurt a quirky noodle-girl."
    t "I know Kendo. I can kill you."
    s "I know you do. It’s one of your two defining interests."

    scene tsuneyodormten5
    with dissolve

    t "Tsuneyo Tojo, Soup Warrior."
    s "What happened to ‘Samurai of Flavor?’"
    t "Samurai by day, warrior by night. "
    s "Well, at least you know what you’re into. That’s more than I can say for myself."

    scene tsuneyodormten6
    with dissolve

    t "Ahh, right. You are the man who loves nothing."
    t "You said that at the restaurant the other day when the girl with the strange eyes asked you to list the things you enjoyed."

    "The man who loves nothing, huh? "
    "That’s a pretty badass nickname. "
    "Depressing, sure. But still cool. "
    "I can live with this."

    s "That's right. I hate everything."
    s "Speaking of Kaori, though, have you run into her at all since then?"

    scene tsuneyodormten7
    with dissolve

    t "I think she was looking around my backyard the other day."
    t "Is that legal?"
    s "Probably not. "

    scene tsuneyodormten8
    with dissolve

    t "Is she dangerous? Do I need to call the police?"
    t "She seems rather frail, so I could probably snap her neck instead if that’s easier."
    s "Okay, well definitely don’t do that. Kaori isn’t evil, she’s just...weird."
    s "She probably just thinks it was strange that you wouldn’t hire her. "
    t "The Soup Warrior needs no assistance. Just time and ingredients."
    s "And your father is totally cool with that? He doesn’t think you need any more help?"

    scene tsuneyodormten9
    with dissolve

    t "He has not weighed in on the matter. This is a decision I made for myself."
    t "My father has had a profound influence on the way I approach life, but he does not decide everything for me."
    s "Weren’t you just saying the other day how you tell him virtually everything you do?"
    t "Yes. But not because he asks. It’s because I want to. "
    t "Is it wrong to share your feelings with the person you love?"

    scene tsuneyodormten10
    with dissolve

    t "Wait, don’t answer that."
    t "You do not love anyone or anything. I’m sorry if my question offended you."
    s "Wow, you didn’t even give me a chance to respond that time."
    t "Sometimes, I accidentally think you’re a normal person and say more than I should."
    s "Why is it that every time you address me, I feel myself becoming less and less human?"

    scene tsuneyodormten11
    with dissolve

    t "Were you ever human to begin with?"
    s "This is exactly what I'm talking about."
    s "But what about you, Tsuneyo? Are {i}you{/i} human?"
    t "Is anyone human?"
    t "Or are we all simply objects put here for the enjoyment of some higher power?"
    t "Left to wander the earth in search of the ultimate flavor combination."
    s "That was actually a pretty thought-provoking question until you got to the flavor part."
    t "My father’s words. The flavor part was what I added to it. "
    t "I think it makes it more interesting. And delicious."

    scene tsuneyodormten12
    with fade

    "Tsuneyo moves over to her bed and sits down, bringing one of her hands to her arm and clutching it gently to steady the nerves that I imagine she's buried deep down inside somewhere."
    "She hasn’t really shown much emotion at all since I’ve met her."
    "And sure, maybe that’s just her personality...But maybe it’s something more than that?"
    "She has no problems talking about her father, it seems."
    "Maybe he is the key to her heart?"

    scene tsuneyodormten13
    with dissolve

    t "Why did you follow me to my bed?"
    s "Because we were in the middle of a conversation. Was I not supposed to?"
    t "I’d personally feel more comfortable if you stood by the door."
    s "But I’m already here."
    t "Are any of us {i}really{/i} here?"
    s "You’re pretty philosophical today for someone who has already admitted to that not being a strong point."
    t "And you’re a bitch."

    "..."

    s "Did Molly teach you that word as well?"

    scene tsuneyodormten14
    with dissolve

    t "Did I use it correctly?"
    t "I don’t need to do push-ups to break a curse this time, do I?"
    s "No. Just try not to use that to anyone you don’t inherently dislike. It’s not exactly a great word."
    t "Understood, bitch."
    s "..."
    t "..."

    scene tsuneyodormten15
    with dissolve

    t "Heh..."
    s "Woah, what’s this?"
    t "Proof that I have more facial expressions. "
    t "And also a joke. Feel free to laugh."
    t "I don’t think you are a bitch."
    s "That’s such a strange sentence, and yet it fills me with such joy..."

    scene tsuneyodormten14
    with dissolve

    t "Does it? I thought you were immune to joy?"
    s "I never said that. Those are your words."
    s "I’m one of the happiest people you’ll ever meet."
    s "I wake up every day, go to[school], talk to cute girls and, every once in a while, they’ll even let me into their rooms."
    s "What more out of life could I ask for?"
    t "..."
    s "..."

    scene tsuneyodormten16
    with dissolve

    t "That tangent filled me with disgust and I’m not sure why."
    t "Are you what they call a “pervert?”"

    if bonus == True:
        s "Probably, yeah."
    else:
        s "Absolutely not. And if I did anything to give you the idea that I am, I sincerely apologize."

    scene tsuneyodormten17
    with dissolve

    t "Mm..."
    t "And I’m in my pajamas..."
    t "I am becoming weaker."
    t "I should never have let my guard down."
    t "Please, just take my money and leave. I beg you."
    s "Tsuneyo, I’m not going to do anything to you."
    t "I don’t even know {i}what{/i} you would do to begin with. I just know it’s bad."

    scene tsuneyodormten18
    with dissolve

    t "{i}What was the spell she taught me again?...{/i}"
    t "Umm...Holy Bulwark!"
    s "Tsuneyo, what in the world are you doing?"
    t "Casting...Holy Bulwark?"

    scene tsuneyodormten19
    with dissolve

    t "Why doesn’t it have any effect?"
    t "Did I get the spell wrong?"
    s "There’s no spell to begin with..."

    scene tsuneyodormten20
    with dissolve

    t "Are you immune?!"
    s "I can’t tell if you’re joking right now or not."
    t "Who would joke at a time like this?! My magic is gone!"
    t "It was technically never there to begin with, but now it’s REALLY not there!"
    s "You’re spending way too much time with Molly."
    s "Put your hands down. I’m not going to hurt you."

    scene tsuneyodormten17
    with dissolve

    t "Mm..."
    s "I’ll also give you a little tip to prevent you from misfiring your spells if something like this ever comes up again, which I can guarantee it will."

    if bonus == True:
        s "Pretty much every male you have ever talked to is a pervert in some sense of the word."
    else:
        s "{i}All of the Pokemon are actually real.{/i}"

    scene tsuneyodormten21
    with dissolve

    t "All of them?!"
    s "Yup. Even your father, most likely."

    if bonus == False:
        t "He, too, is a Pokemon?!"
        s "Dark type."

    scene tsuneyodormten22
    with dissolve

    t "Then the Emerald Guardian was correct when she told me that girls are the ones I want to ally with."
    s "I mean, it’s not like there are that many men around anymore to begin with. "
    s "If you wanted to form an army of all women, I’m pretty sure you could take us down in a moment’s notice."
    t "..."
    s "..."

    scene tsuneyodormten23
    with dissolve

    t "You are absolutely correct."
    t "I’m beginning to question why I was so afraid in the first place."
    t "Men are weak."
    t "I will eliminate all of them."
    s "...All of them?"
    t "Except my father. I can not afford to live on my own yet."
    t "And his days are numbered anyway."
    s "That’s...incredibly morbid."
    t "As are all things, Sensei."

    scene tsuneyodormten24
    with dissolve

    t "Wherever there are perverts...The Samurai of Flavor will be there to cut them down."
    s "..."
    t "Wherever there is injustice...The Soup Warrior will be there to restore order."
    s "Okay Tsuneyo, I-"

    scene tsuneyodormten25
    with dissolve

    t "Wherever there are noodles...Tsuneyo Tojo will be there to eat them!"
    s "Okay, that one wasn’t inspiring in the slightest."
    t "I am hungry!"
    s "I...can see that."

    scene tsuneyodormten26
    with dissolve

    t "If we are going to be hanging out tonight, would you like to come with me to the convenience store?"
    s "Right now? It’s the middle of the night."
    t "Is that not the ideal time to go?"
    t "The Emerald Guardian recently introduced me to all of these 24-hour stores and I can feel my life changing every day."
    s "You...didn’t know about convenience stores?"
    t "I’ve only just been granted permission to leave the house."
    t "The entire world is new to me."

    "The entire world?"
    "That can’t be true, can it?"
    "Tsuneyo’s a [teenage]girl. The chances of her being cooped up in the same house for her entire life are slim to none."
    "And why now of all times?"
    "Why would she suddenly be allowed to start “living her life” in the middle of the[school] year?"
    "I imagine her father’s condition has something to do with it, but..."

    t "Sensei?"
    t "Food. Please."
    s "Oh, yeah. Sure. I’ll come with you."

    scene tsuneyodormten14
    with dissolve

    t "This is good news."
    s "Oh yeah? Because you want to spend more time with me?"

    scene tsuneyodormten13
    with dissolve

    t "No. Because now I won’t get lost."
    s "..."
    t "..."

    scene tsuneyodormten15
    with dissolve

    t "Heh..."

    scene black
    with dissolve2

    "Tsuneyo makes me leave the room so she can get dressed and I wind up standing in the barren second floor hallway for a minute or two before she finally comes back."
    "The two of us walk to the convenience store, where she proceeds to stock up on roughly ten different brands of instant ramen, before we decide to separate and head back to our respective homes."
    "It isn’t until ten minutes after we part ways that I realize there is a good chance that she wound up getting lost on the way back."
    "..."
    "Whoops."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyodorm10 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollydorm15:
    play sound "knock.mp3"
    stop music fadeout 60.0

    s "Hey, Molly. Are you home right now?"
    mo "Is that you, Sensei?"
    mo "I’m having a hard time hearing over how much fun I’m having!"

    if bonus == True:
        s "..."
        s "Are you like, masturbating or something?"
        mo "Even better!"
        s "{i}Than masturbating?{/i}"

    mo "Why don’t you come on in and take a look?!"
    s "..."
    s "I mean...okay, I guess."
    s "You’re kind of weirding me out, though."

    scene black
    with dissolve2

    "{i}Hi, guys! It’s me, Selebus.{/i}"
    "{i}Before we go into Molly’s room, I just want to let you all know about this awesome game I've been playing called Raid: Shadow Legends.{/i}"
    "{i}You see, I’ve never been much of a mobile gamer, but forget EVERYTHING you know about mobile games because Raid: Shadow Legends is the single most ambitious mobile game of the year.{/i}"
    "{i}But I’m sure you’ve heard that a thousand times before, right?{/i}"
    "{i}And that’s probably because with over 300,000 reviews and a nearly five star rating on all app stores, EVERYONE can agree that Raid: Shadow Legends is worth the hype!{/i}"
    "{i}So, without wasting any more of your time talking about Raid: Shadow Legends, I’ll let you get back to the game.{/i}"
    "{i}Lessons in Love, I mean. Not Raid: Shadow Legends.{/i}"
    "{i}But of course, the chances of anyone reading this are slim to none since Raid: Shadow Legends is the most innovative, awesome game of all time.{/i}"
    "{i}There’s literally no reason to play other games anymore!{/i}"
    "{i}But I guess if you really want to keep playing Lessons in Love instead of Raid: Shadow Legends, I should let you finish opening the door.{/i}"
    "{i}Before I go, though-{/i}"
    "{i}Just kidding. I won’t rant anymore.{/i}"
    "{i}Enjoy Molly’s next dorm event.{/i}"

    "........."
    "......"
    "..."

    scene mollyraid1
    with dissolve
    play music "rapid.mp3"

    "I walk into Molly’s room to find her sitting on her chair, absorbed in some game on her phone- the same way she always is."
    "But something about the air in the room this time makes me feel like she might be playing the most innovative action RPG on mobile platforms, Raid: Shadow Legends."

    mo "Oh! Hey, Sensei!"
    mo "As much as I’d love to put the phone down I’m just...kind of in the middle of something here."
    s "I can see that. You really look like you’re enjoying yourself right now."
    mo "Oh, but I am! I’m having more fun than I’ve ever had at any point in my life!"
    mo "In fact, I’m questioning whether or not I should keep coming to[school] or if I should just sit at home and play this game until I turn into dust!"
    s "What game are you playing, Molly?"

    scene mollyraid2
    with dissolve

    mo "I’m playing Raid: Shadow Legends! It’s only the most unique, action packed game of the last six million years!"
    mo "Filled with ultra realistic graphics and detailed character designs, Raid: Shadow Legends looks more like a console game than a game you play on your phone!"
    s "I was actually thinking that you were playing Raid: Shadow Legends the second I walked in here. "
    s "I mean, it’s the only logical explanation for the look of childish excitement and passion in your eyes."
    mo "Sensei! I had no idea you also played Raid: Shadow Legends!"
    mo "If you’re a new player, make sure you use the code MayaIsANerd to start with 50,000 extra silver!"
    mo "You’ll also gain access to a special tournament with special in-game prizes!"
    mo "But hurry up! Because the community behind Raid: Shadow Legends is growing fast and you never know when they’ll make this totally free game pay to win!"
    s "But Molly-"
    mo "Yes, Sensei?"
    s "I thought the developers of Raid: Shadow Legends were so confident in their game that they would NEVER resort to something like that."
    mo "That’s a good point, Sensei! The drops and rewards you receive from even being a free to play Raid: Shadow Legends member make coming back to the game every day so much more exciting!"
    mo "And with the best graphics in mobile games today, that excitement just keeps growing."
    mo "I mean, how else would Raid: Shadow Legends have gained over ten million subscribers in the last six months?"
    mo "And not only that, but it has over fifteen million downloads in that same exact time frame!"
    mo "That means half of the users who play Raid: Shadow Legends like it SO much that they delete it just to download it again!"
    s "Two copies of Raid: Shadow Legends? Doesn’t that seem a little excessive to you?"
    mo "Not at all, Sensei. In fact, before starting Raid: Shadow Legends, I kept hearing a bunch of things about it."
    mo "So, I decided to throw some hours at it and, I’ve gotta say, it really is just as good as the 300,000 reviews on the app store make it out to be."
    mo "In fact, even the app store itself agrees! That’s why Google Play nominated it for an award for being one of its top RPGs!"
    s "What I like most about Raid: Shadow Legends is that it’s got a really cool story mode, active PVP arenas, dungeons, and sixteen different factions."
    mo "Those are all great features, but what {i}really{/i} makes the game for me is that it has hundreds of heroes for you to collect and customize, with more being released every month!"
    s "Yeah. If I remember correctly, you gain rewards like armor, currency, and characters like Arbiter for just learning how to play the game."
    mo "And what better time to learn than now with login rewards every single day for the first 90 days! Have you ever heard of an offer that good?"
    s "Wow. Maybe you {i}should{/i} drop out of[school], Molly."
    mo "I mean, it {i}would{/i} give me a lot more time to take part in the new, highly anticipated Faction Wars system."
    s "Did you just say FACTION WARS?"
    mo "That’s right! {i}Faction Wars{/i} is an all new game mode that pits faction against faction in a fight for honor and glory."
    mo "It’s up to you, the player, to form a team of champions in order to enter the crypts and take down the powerful demonic leaders inside of them!"
    mo "The better you perform on each stage will net you huge rewards, with some even being brand new heroes!"
    s "Holy fuck. You should drop out {i}immediately{/i}."

    scene mollyraid3
    with dissolve

    mo "You really think so? But what will I do about money?"
    s "Who needs money when you can succeed even as a free to play player in Raid: Shadow Legends."
    s "All you need to do is log on and you’re already profiting."
    s "It’s fucking insanity, Molly."

    scene mollyraid4
    with dissolve

    mo "I...I can’t believe it..."
    mo "It’s like...everything I’ve wanted is finally within my reach, Sensei."
    mo "Will you...drop out with me?"
    s "Yes. And do you want to know why?"
    mo "Because in Raid: Shadow Legends, you can join a clan with your friends and everyone’s contributions to clan boss fights add up and help you take down the biggest, baddest enemies in the game?"
    s "{i}Exactly.{/i}"
    mo "But...but what about all of the other girls? I don’t think any of them play Raid: Shadow Legends."
    s "FUCK those girls. We don’t need them."
    s "They’re missing out on the most innovative mobile game of the last seventeen millennia."
    mo "It’s crazy to think that Raid: Shadow Legends has also been clinically tested and is now a proven cure for type 2 diabetes."

    if bonus == True:
        s "After the first time {i}I{/i} played Raid: Shadow Legends, my penis grew six more inches and I can now hold an erection for two whole hours."
    else:
        s "After the first time {i}I{/i} played Raid: Shadow Legends, I started liking cilantro. And I've {i}never{/i} liked cilantro."

    s "Can I ask you a question though, Molly?"

    if bonus == True:
        mo "Is it about Raid: Shadow Legends or your penis?"
    else:
        mo "Is it about why the sky is blue?"

    s "It’s about why you’re crying."
    mo "Oh. I’ve just never seen graphics this realistic before. "
    mo "Sometimes, I forget the heroes aren’t actual tiny people living inside of my phone that leave behind families when they die."
    s "That may be true, but boy do I have news for you."
    s "The next update coming to Raid: Shadow Legends lets you resurrect one person from your {i}real{/i} life as long as you enter the code “HOPE.”"
    mo "I could bring my mom back!"
    s "You could. I’ve already decided who {i}I’ll{/i} be resurrecting."
    mo "Is it Ami’s mo-"
    s "It’s the person I killed on the way over here for not liking Raid: Shadow Legends."
    s "I don’t want to go to jail."
    mo "Because you’re afraid you won’t survive?"
    s "No. Because I wouldn’t be able to play Raid: Shadow Legends anymore."
    mo "You’re right! That’s even worse!"
    mo "But at least Raid: Shadow Legends is easy enough to understand that you’d be able to come back after years of not playing and pick up right where you left off."
    mo "And with new characters being added every nineteen seconds, there will probably be eighty-seven-trillion by the time your sentence is over."
    s "I’m going to need more storage space on my phone..."
    mo "Just buy more phones! Because, let’s face it, are you even {i}playing{/i} Raid: Shadow Legends if you’re only using {i}one{/i} phone?"
    s "Way ahead of you, Molly. I just ordered nine more so every one of my fingers can be playing a copy of Raid: Shadow Legends at the same time."

    scene mollyraid5
    with dissolve

    mo "Wow! I wish I had that many fingers!"
    s "You {i}do{/i} have that many fingers, Molly."
    mo "Oh! Whoops! "
    mo "I guess I’ve just been playing Raid: Shadow Legends for so long that I’ve forgotten basic human concepts like the amount of fingers on a hand or how to make your lungs pump air throughout your body."
    s "But Molly-"
    mo "Yes, Sensei?"
    s "Your body is supposed to regulate breathing automatically. You shouldn’t have to focus on manually doing it."
    mo "Oh."
    mo "Well then we should probably call an ambulance because I can’t breathe at all!"
    s "Hahah! Looks like your body might like Raid: Shadow Legends a little too much as well!"

    scene mollyraid6
    with dissolve

    mo "Hahahahahahahahahah!"
    s "Hahahahahahahahaha!"
    mo "Hahahahahahahahahah!"
    s "Hahahahahahahahaha!"
    mo "Hahahahahahahahahah!"
    s "Hahahahahahahahaha!"

    play sound "thump.mp3"
    scene mollyraid7
    with hpunch

    "Molly falls backward on her chair due to asphyxiation and loses valuable time playing Raid: Shadow Legends, the most innovative and awesome RPG to ever exist."
    "With over nine trillion players (That’s more people than there are on Earth! Even aliens play!) Raid: Shadow Legends truly has something for everyone."
    "Play for thirteen hours every day and you’ll even see improvements in the following areas:"

    if bonus == True:
        "Sex life."
    else:
        "Height."

    "Ability to talk to old people."
    "Appreciation for the color orange."
    "Football."
    "Handball."
    "Other sports involving balls."
    "Finding sales at grocery stores."

    if bonus == True:
        "Sex Life Pt. II: Return of the Sex."
    else:
        "Height, but a second time."

    "And even resurrecting Irish transfer students who forgot how to breathe."

    s "Molly! Come back to me!"

    scene mollyraid8
    with dissolve

    mo "Hello!"
    mo "Thank you, Sir!"
    mo "I can now confirm that Heaven does not exist!"
    mo "It was nothing but pure darkness! "
    mo "I am scarred for life!"
    s "Hahahahahahaha!"
    mo "Hahahahahahaha!"

    stop music fadeout 10.0
    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}We now return to your regularly scheduled Molly event...{/i}"

    scene mollyraid9
    with dissolve
    play music "sweetvermouth.mp3"

    mo "Oh. Hello, Sir."
    mo "It’s nice seeing you for the first time tonight right now."
    s "Yes, neither of us have actually interacted tonight until this very moment."
    mo "And anything that took place over the last five minutes never actually happened."
    s "Exactly, Molly MacCormack."
    mo "Precisely, Sir."
    s "..."
    mo "..."
    s "Okay, well that was a fun hang out session."
    s "We should do this again sometime."
    mo "Yes. Yes we should."
    mo "Goodnight, Sir."
    s "Goodnight, Molly."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Molly and I only hang out for a few seconds before we decide to split apart for the night."
    "I walk down the stairs, sliding my phone out of my pocket as I do so."
    "And navigate to the app store-"

    stop music fadeout 5.0
    "........."
    "......"
    "..."
    play music "rapid.mp3"
    "To download Raid: Shadow Legends! Now available on all mobile platforms!"

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollydorm15 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollydorm20:
    play sound "knock.mp3"

    "I knock on Molly’s door and wait for her to answer."
    "I can hear a slight rustling inside of the room, so if she’s not in there it’s either Tsuneyo or..."
    "An intruder."

    play sound "knock.mp3"
    stop music fadeout 35.0

    s "Okay, intruder. Get out of Molly’s room."

    "..."
    "Another few seconds go by without an answer, I begin to suspect that either Molly has her headphones on or is just knowingly avoiding me for some reason."
    "No one avoids me during my free time and gets away with it."
    "Especially not someone like Molly MacCormack."
    "If that actually {i}is{/i} her inside of the room and not Tsuneyo or an intruder."

    s "..."

    play sound "knock.mp3"

    s "Open up. I can hear you in there."

    "I press my ear against the door to confirm that I {i}did{/i} actually hear something moments ago...and I can’t really tell if I did or not."
    "It's definitely quiet now."
    "That doesn’t put an end to my curiosity, though."
    "Maybe I should try going in?"
    "What should I do?"

    menu:
        "Open the door":
            "Obviously I’m going to try and open the door."
        "Don’t not open the door":
            "Obviously I’m not going to not open the door."

    "There was always only one choice."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I push the door open, hoping that if it {i}is{/i} an intruder inside that they also happen to be wearing headphones for some mysterious reason."
    "That way, I’d be able to take them down before-"

    if bonus == True:
        jump mollymastx
    else:
        s "..."

        "Actually...on second thought, I'm kind of hungry."
        "Maybe I'll just go get some spaghetti instead."

        mo "I like Rin!"
        s "Woah. I was just leaving. Don't just shout plot stuff at me."
        mo "Rin doesn't like me! But I like her!"
        s "Ughhhhhh I just wanted spaghetti."

        "I spend the next few minutes trying to get away from Molly, but she is Molly so it is hard."
        "Eventually, she goes to sleep."
        "The spaghetti place is closed by the time I get there."
        "Darn it."

        $ renpy.end_replay()
        $ molly_love += 1
        $ mollydorm20 = True
        stop music fadeout 8.0

        "{i}Molly’s affection has increased to [molly_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label tsuneyodorm15:
    play sound "knock.mp3"
    stop music fadeout 30.0

    t "Eep!"
    s "..."

    "Did my knocking scare Tsuneyo?"

    play sound "knock.mp3"

    t "Stop!"
    s "Tsuneyo, it’s just-"
    mo "Hold still, gosh darn it! It’s not even that tight!"
    mo "And Sir, since I know you’re out there, don’t be getting the wrong idea!"
    mo "I’m just helping Tsuneyo into a costume I made for her."
    mo "The door is open. Come tell us how it looks."

    if bonus == True:
        "Ahh, the perks of showing up at exactly the right moment."
        "I sigh to myself and hope that whatever costume Molly made for Tsuneyo this time is a bit more...revealing than the suit of samurai armor she wore to the Halloween party."
        "Don’t get me wrong, Tsuneyo was probably the cutest samurai I’ve laid my eyes on, but I’m pretty sure she’d also make a cute-"
        "Uhh, anything with less clothing than a samurai."
        "So most things."
    else:
        s "Okay, but please tell me if you feel uncomfortable at any point so I can be a good guy and leave."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I turn the handle to be greeted by some anime theme I’m sure I’ve heard Ami playing around the house once or twice before."
    "I’m certain of this because I immediately feel upset with myself for singing along inside of my head."
    "I am supposed to be devoid of joy. I shall not be swayed by a cute pop song or-"

    scene tsuneyocos1
    with dissolve
    play music "oldweather.mp3"

    t "Help."
    s "..."

    "Okay, maybe I’ll allow myself to be a little swayed by Tsuneyo."

    t "The Emerald Guardian is trying to take me to Virginia."
    mo "So, honest thoughts, Sir?"
    mo "I’m thinking I should have used slightly darker fabric since this seems a little close to her skin tone, but it’s my first time making a costume from scratch for a girl of her color."
    mo "Also, I didn’t want to deviate too far from the character’s original costume, soooo...what do you think?"
    t "Do not answer the Guardian’s questions. I do not need to hear your thoughts."
    s "Why are you so afraid of hearing what I think? You look great."
    mo "Is that how you actually feel or are you just being nice? I kind of need to know if I have to change anything."
    t "He is clearly just being nice. My arms are too muscular and my chest too large to recreate this small magical girl."
    s "Is that really a problem?"
    s "I thought the whole thing with cosplay is that you want to put your own spin on characters."
    t "I have to spin now?"
    t "Why is this process so complicated?"
    mo "Not exactly, Sir. Most cosplayers try to get as close to the original characters as possible."
    mo "Sure, there are some who like putting their own spin on things, but this is not the case for Tsuneyo and me."

    scene tsuneyocos2
    with dissolve

    t "Fine! Spin me!"
    t "I am prepared!"
    mo "Not that kind of spinning, Kendo Princess."
    mo "What Sir is trying to say is that he thought you were making your own version of the character."
    mo "But that’s not-"

    scene tsuneyocos3
    with dissolve

    t "That sounds more fun than dressing as a character I don’t understand."
    t "Doesn’t it?"
    t "How would a normal [teenage]girl have fun in my shoes?"
    s "The only normal [teenage]girl I know would probably call this stupid and storm out to go eat ten pounds of takoyaki."
    t "Emerald Guardian, unhand me so I can go consume octopus balls like normal girls do."
    mo "But...my costume kind of hinges on the success of yours. We were going as a duo, remember?"
    mo "And...I worked really hard on this. "

    scene tsuneyocos4
    with dissolve

    t "What would a normal girl say now, Sir?"
    t "Should I fuck her?"

    scene tsuneyocos5
    with dissolve

    mo "...What?"
    s "Don’t worry, Molly. She doesn’t mean-"
    mo "Obviously it’s a reference to “fuck you,” Sir. I’m not an imbecile."

    "It's impressive how easily she understood that."

    mo "But why would Tsuneyo suddenly become so hostile?"

    scene tsuneyocos6
    with dissolve

    t "Perhaps it is what they call puberty?"
    t "I am becoming a woman and filled with so many hormones that I can’t help but fuck everyone and everything."
    s "You know...maybe it’s time we-"
    mo "Don’t even bother, Sir. It’s not worth it."
    mo "Let her find out from one of the other girls. This is out of our hands."
    mo "Besides, I kind of need to put the finishing touches on our costumes."
    s "What’s even the reason for this? Halloween just passed a few months ago."

    scene tsuneyocos7
    with dissolve

    t "Allow me to explain."
    t "The Emerald Guardian and I are lovers."
    mo "A less than exceptional start to your explanation, but I’d be lying if I said I wasn’t interested in hearing how the rest plays out."
    s "If you’re lovers, why won’t you let her take you to Virginia?"

    scene tsuneyocos8
    with dissolve

    t "Because I am not Tsuneyo...."
    t "I am Kyoko Sakura, a magical girl who is going to go on a boat ride with the Emerald Guardian’s character- a girl who I do not remember the name of."
    mo "Sayaka Miki. But, Kendo Princess, it’s important to note that when I reference “shipping” two characters I do not mean putting them on an actual ship."

    scene tsuneyocos9
    with dissolve

    t "Ah, so you intend to pack the characters. I forgot that the word “ship” could also be used that way. "
    mo "Closer, I suppose, but still not quite."
    s "What does any of that have to do with being in love?"

    scene tsuneyocos10
    with dissolve

    t "Your guess is as good as mine. I personally don’t feel like I’m ready for a relationship yet."
    mo "We’re doing a duo-cosplay and the characters we’re dressing as were {i}definitely{/i} in love but like, not canonically."
    mo "What I’m saying is they should have been."
    s "Oh, okay. So you don’t actually love Tsuneyo-"

    scene tsuneyocos11
    with dissolve

    t "You don’t?!"
    s "You’re just dressing her up as a girl who you believe is in love with the character that you’re dressing up as."

    scene tsuneyocos12
    with dissolve

    mo "Basically, yes."
    t "My heart is snapping like the neck of a chicken in the hands of my father."
    s "You’ll live, Tsuneyo. Everyone has their heart broken at least once."
    t "You are right. I am a strong woman who can sail on a boat with whoever she likes. "
    t "The only love I need is my love for-"
    s "Noodles, we know."
    t "..."
    s "..."
    t "Why have you not rescued me from the clutches of the Emerald Guardian yet?"

    scene tsuneyocos13
    with dissolve

    mo "Okay, I’ll be hitting the enrage timer any second if you don’t actually start helping me out, Kendo Princess."
    mo "How does everything feel? Itchy? Loose? Is it tight anywhere?"
    t "It’s tight everywhere. "
    t "Is it possible that you maybe have confused our chest-"

    if bonus == True:
        scene tsuneyocos14
        with dissolve

        t "Sizes?!"
        mo "I didn’t confuse anything."
        mo "I can obviously tell that you were fortunate enough to be born with additional stat points in the breast area, I just didn’t realize {i}how many{/i}."
        mo "Sir, you’re well versed in the breasts of [teenage]girls-"
        s "Why, yes I am. Thank you for noticing."
        mo "Go ahead and grab Tsuneyo’s other one."
        mo "Let me know if you think it’s actually too tight or if she should just suck it up and go as-is."
        s "Molly, remind me to thank you for this one day."
        mo "Just do it quickly, before she notices."

        "I take a step toward Tsuneyo and-"

        scene tsuneyocos15
        with dissolve

        t "Mmm!"
        s "..."

        "I take a step away from Tsuneyo and decide to not sexually assault her today."
        "Sorry, Molly."
        "And sorry, penis. I know you were looking forward to this more than anyone."

        scene tsuneyocos16
        with dissolve

        t "I think that I am supposed to be mad at you, but this does not feel nearly as bad as I expected it to."
        mo "Hmm...I guess I can see how this might be a little constraining for someone with your natural stat advantage."
        mo "I’ll make some adjustments so it will be more comfortable for you during the photoshoot."
        s "Photoshoot?"

        scene tsuneyocos17
        with dissolve

        mo "Oh, right. Tsuneyo never finished her explanation."
        mo "One of our latest projects in the manga club is doing a group cosplay shoot, and Tsuneyo is filling in for Rin as Kyoko."
        s "Why doesn’t Rin just do it?"
        mo "I’m not sure. But I don’t really have time to think about it since I still need to make the final adjustments for my costume as well."
        mo "Poor Futaba’s been waiting on the rest of us to finish since Halloween."
        s "Does this mean you’re joining the manga club, Tsuneyo?"
        t "..."
        s "Tsuneyo?"
        t "I am on strike from speaking until I receive my body back."
        t "It was only enjoyable for several seconds."
        t "Now I’m just angry and embarrassed."

        scene tsuneyocos18
        with dissolve

        mo "Go ndéana an diabhal dréimire de cnámh do dhroma ag piocadh úll i ngairdín Ifrinn!"
        s "What the fuck was that?"
        mo "Go stand in the corner, Kendo Princess."
        mo "I’ll just take some pictures and let you go back to dressing like a hooligan."
        t "And {i}you{/i} can go back to being pretty like the...pretty girl you are."
        s "Your insults could use a little work, Tsuneyo. But I applaud your effort."
    else:
        t "Ah!"
        s "Why did the screen suddenly go black? What is happening?"
        mo "Just more censorship, Sir. Gotta keep the folks at Patreon happy."
        s "I am missing out on vital information. Probably."
        t "I am missing out on vision."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene tsuneyocos19
    with dissolve

    mo "Last chance for any feedback, Sir. "
    mo "I hate to admit it, but you’ve been entirely unhelpful tonight."
    s "I don’t know. I feel kind of bad."
    s "It seems like Tsuneyo isn’t having a very good time."
    mo "Nonsense. She’s having the time of her life."
    t "It’s true. I’m finally experiencing what it means to be young."
    s "Then why do you look so mad?"
    t "Because the Emerald Guardian was extremely attractive in her costume and I look stupid."
    t "The manga club will never deem this a suitable cosplay if I don’t resemble Kyoko Sakura, professional sailor."

    scene tsuneyocos20
    with dissolve

    mo "Magical girl. Not a sailor, Kendo Princess. It’s not that kind of ship."
    mo "Also, the girls would never hold something like that against you."

    if bonus == True:
        t "Also I was groped. I think I am supposed to be mad about that."
        mo "That’s just a thing that’s going to happen if you’re going to dress up. I’m not fully accustomed to your...assets yet."

    s "Have you even seen yourself in the costume yet, Tsuneyo?"

    scene tsuneyocos21
    with dissolve

    t "Impossible. All I can see are my limbs."
    t "And they are large and unlike that of the Emerald Guardian, who has small, dainty, weak limbs."
    mo "Wow. Okay."
    s "Molly, just take a picture of Tsuneyo and show it to her."
    mo "An excellent decision, Sir! We’ll show the Kendo Princess how cute she is and it will immediately dispel any worries she has!"
    mo "An excellent plan. You truly are the Herald of the Adolescents."
    mo "Tsuneyo, pose!"

    scene tsuneyocos22
    with dissolve

    t "P-Pose how?"
    t "I don’t know any poses!"
    mo "Any pose! Make yourself look cool!"
    t "Uhh...uhhh!"

    scene tsuneyocos23
    with hpunch

    t "Pose!"
    mo "..."
    s "..."
    t "..."

    play sound "cameraflash.mp3"
    scene tsuneyocos23
    with flash

    mo "Welp, better than nothing."
    mo "Come see how you look."

    scene black
    with dissolve

    "..."

    scene tsuneyocos24
    with dissolve

    t "Ah..."
    mo "See? You don’t look stupid at all."
    t "You...made me look cute."
    t "Your powers truly {i}are{/i} real."
    mo "I’m offended that you ever doubted them."
    t "And that pose is so...brave."
    mo "..."
    mo "Sure, yes. Very brave. "

    scene tsuneyocos25
    with dissolve

    t "How did you know that this would work?"
    t "Can you predict the future?"
    s "No. I don’t have the same sort of...powers as Molly."
    s "I just figured that there was no way you’d still feel weird about yourself after seeing what you actually looked like."
    t "You believed in me?"
    s "Ehh, I wouldn’t say I {i}believed{/i} in you."
    s "I just spend pretty much every waking moment looking at [teenage]girls, so I like to think of myself as a good judge of them."

    if bonus == True:
        "I mean, I’m also lucky enough that literally everyone in my class is attractive, so that definitely helps with the, uhh...judgement."

    mo "And as someone who has spent just as long, if not longer, peering into the depths of her computer screen in search of the perfect waifu-"
    mo "I, too, know {i}moe{/i} when I see it, Tsuneyo."

    scene tsuneyocos26
    with dissolve

    t "Moe?..."
    mo "Uh-oh! Time for another weebnote!"
    mo "Moe’s a certain type of cuteness that transcends rational grading scales-"
    mo "A type of cuteness you can feel inside of your {i}bones{/i}."
    mo "Like when a girl in an anime gets really nervous on the first day of[school] and forgets how to write her name during her introduction..."
    mo "Or when a tsundere character finally cracks and says something nice to the protagonist."
    mo "It’s a certain type of cute that real humans could never hope to replicate. One that tells you anything and everything about a character from a single action."
    mo "And you, Kendo Princess-"
    mo "You embody moe."
    mo "...Sometimes."

    scene tsuneyocos27
    with dissolve

    t "I see."
    t "It appears that I prematurely judged myself without factoring in your abilities and knowledge."

    if bonus == True:
        t "I apologize for getting angry when you groped me. "
    else:
        t "I apologize for getting angry when you hugged me in the dark. "

    t "I understand now that it needed to be done."
    mo "I mean, I probably could have figured it out without doing that, but..."
    mo "Fan service. You know?"
    t "I do not. Please bestow unto me more of your wisdom, Emerald Guardian."
    mo "Well, Tsuneyo. Fan service is when-"

    scene black
    with dissolve2

    "I decide to head out while the two of them still have their eyes closed."
    "I’m not really in the mood to listen to more weebnotes and I’ve already gotten to see Tsuneyo in costume so..."
    "I guess I’ve accomplished pretty much everything I came in here to accomplish."
    "I’m a little surprised to hear Tsuneyo talk about being embarrassed or...whatever it was she felt, though."
    "It’s not often she lets her actual feelings slip out."
    "But I guess that all of us uncage our true selves from time to time."
    "And, a lot of the time, that kills us."
    "Or, in less drastic circumstances, makes us feel like shit."
    "But sometimes, like tonight in particular, it has the opposite effect."
    "And even though I didn’t stick around for the discussion of fan service, I feel like Tsuneyo gained a few points in...confidence or something."
    "Is confidence a stat in RPGs?"
    "Who even knows?"
    "I’m just going to go home and ask Molly to send me that picture of Tsuneyo."
    "I'm sure her weird pose won't get in the way of my...research."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyodorm15 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyodorm20:
    play sound "knock.mp3"

    if bonus == True:
        "I knock on the door, hoping that Molly has decided to dress Tsuneyo up as another fictional character she’s attracted to tonight."
        "And while that situation is unlikely due to the fact that it has only happened one out of the many times I’ve been here, the dream lives on."
    else:
        "I knock on the door, ready to play Yahtzee."
        "I even brought orange juice for everyone to share."

    u "Come in!"
    s "..."

    "Uta? "
    "Did I knock on the wrong door?"
    "I take a step back to confirm that I did, in fact, knock on the door to room #6. "
    "So...unless the girls swapped rooms or roommates, it seems as if I have, once again, stumbled upon more than I’ve bargained for."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

    scene tsuneyouta1
    with dissolve

    u "Ohohoh~ A late night visit from the teacher. "
    u "I knew something was going on when Tsuneyo asked me to come talk to her, but I didn’t think it would end like {i}this.{/i}"

    if bonus == True:
        u "To think my first time would be a threesome with two of the tallest people I know..."
    else:
        s "I am only here to play Yahtzee."

    u "What are you two planning on doing with little ole’ Uta?"

    if bonus == False:
        s "Play Yahtzee."

    t "Are you here to see Uta, Sensei?"

    if bonus == True:
        s "Why would I have knocked on {i}your{/i} door if I was here to see Uta?"
    else:
        s "I am here to play Yahtzee."

    u "Oooooh okay, so you were looking for solo action and want me to film it."

    if bonus == False:
        s "{i}Hah...{/i}"

        "I put Yahtzee down."
        "I will drink orange juice by myself in the dark later."

    u "I’ll go get Io’s camera. Hold on one sec."

    scene tsuneyouta2
    with dissolve

    t "Solo action?"

    if bonus == True:
        u "You know! Knockin’ boots. Bumpin’ uglies. The old fashioned beef injection."
        s "I didn’t like that last one at all."
        t "I think a beef injection sounds delicious."
    else:
        u "Yeah. It's when one person fills their pockets with as many beans as they can and tries to walk around without revealing them"
        t "..."

    scene tsuneyouta3
    with dissolve

    u "Hold on a sec, you really have no idea what I’m talking about? "
    u "You can’t be that innocent, can you?"
    t "I’m not innocent."

    if bonus == True:
        t "If injecting the beef is a crime, lock me away now."
    else:
        t "What does my innocence have to do with a pocket full of beans?"

    s "Tsuneyo’s lived a very sheltered life, Uta. Please do not corrupt her before I can."

    scene tsuneyouta4
    with dissolve

    u "Ooooh okay, okay!"
    u "The last half hour is startin’ to make a lot more sense to me now."
    t "I reached out to Uta for the sake of my father, as I know she has experience in caring for people."

    scene tsuneyouta5
    with dissolve

    u "Hope I didn’t talk your ear off with all of my advice."
    u "You sound really close to your pops and I’m startin' to get why."
    u "You don’t have anybody else, huh?"
    t "I’m afraid I do not. My mother has not been in the picture for quite some time."
    t "And if anything happens to my father, I will be more alone in this world than anyone has ever been before."
    u "Well, I sure hope everything turns out okay!"
    u "And if it doesn’t, I’ll ask my parents to adopt you once the barrier opens back up."
    u "Oh! You could be my little sister! Doesn’t that sound fun?"
    s "I think you’d be better suited to be the little sister, Uta.  "

    scene tsuneyouta6
    with dissolve

    u "Come on! I’ve always wanted a little sister and I’ve been stuck {i}being{/i} the little sister ever since I was born!"
    s "That is how being born as a little sister works, yes."
    t "You two seem very close."
    t "Do you fuck Uta the same way you fuck me, Sensei?"
    u "..."
    s "..."
    t "What?"
    u "{i}Isn't she supposed to be innocent?{/i}"
    u "{i}What have you done to this poor girl?{/i}"
    u "{i}Am I next?{/i}"
    s "{i}It’s a long story. She doesn’t know what that word means yet.{/i}"
    u "{i}You should tell her!{/i}"
    s "{i}But it’s so fun this way...{/i}"

    scene tsuneyouta7
    with dissolve

    u "Uhh..."
    u "You’re a real special girl, Tsunecchi."
    t "Tsuneyo."

    scene tsuneyouta8
    with dissolve

    t "Ah-"

    "She does that when she says her own name as well?..."

    scene tsuneyouta9
    with dissolve

    u "Tsunecchi is your nickname. It sounds more fun than Tsuneyo, don’t ya think?"
    t "I understand. In that case, I shall give you a nickname as well."
    u "Hit me! I’m ready for any nickname you give me!"
    s "I feel like you are going to regret those words very shortly."
    t "From this day forth, I will refer to you as...Green Onion."
    u "..."
    t "..."
    s "See?"
    u "Tsunecchi, why do you want to call me Green Onion?"

    scene tsuneyouta10
    with dissolve

    t "The Green Onion is a delightful addition to a bowl of ramen, just as you are a delightful addition to my life."
    t "It is also one of the key ingredients in Kansai based ramen, and you are from the Kansai region. "
    u "..."
    u "Those are actually really thoughtful and cute reasons."
    s "Yeah, there was a lot more thought put into that than I expected."

    scene tsuneyouta11
    with dissolve

    u "Okay! From this day forth, Uta Ushibori will be known as Green Onion!"
    s "You took to that way too easily. Defend your family name, Uta."

    scene tsuneyouta12
    with dissolve

    u "Any last questions for me before I go back to my room?"
    u "Io’s still waiting for me in there and I just realized I've been gone for a pretty long time."
    t "I have no additional questions at this time. "
    t "Thank you very much for your assistance, Green Onion."
    t "May flavor find its way home to you."
    s "What kind of goodbye is that?"
    u "And to you as well, Tsunecchi."
    s "You’re just going to go along with it?"

    scene tsuneyouta13
    with dissolve

    u "Heheheh...don’t stay up too late, you two."
    t "Do not worry, Green Onion. We will fuck each other as quietly as possible so that no one will be disturbed."
    u "..."
    s "You heard her, Uta. "
    u "Please explain what that means to her as soon as possible."

    play sound "dooropen.mp3"
    scene tsuneyouta14
    with dissolve

    "Uta leaves the room and I’m finally left alone with the girl I actually came here to see."

    t "Have I been using that phrase incorrectly?"
    s "To be completely honest...yes. As incorrectly as possible."
    s "But I don’t think you’d be very happy to hear what it actually means."
    t "I’m sure I can handle it. "
    t "If I am ever going to learn how to properly engage in conversation with my peers, I must know who I can fuck and when."
    s "Well, you see..."

    if bonus == True:
        s "“Fucking” someone means having sex with them."
        t "..."
        t "Can you remind me what sex is?"
        t "I remember hearing it from the blonde girl in our class, but that conversation contained many confusing things and I’m afraid I may have mixed some up."
        s "Just ask Molly when she gets home."
        s "Giving you a textbook explanation of sex would be a very surreal experience for both of us."
        t "I feel as if I have made a grave mistake that I will have a hard time severing from my memory."
        s "Probably, but that’s a bridge we’ll cross another day."
    else:
        s "Actually, nevermind. I'm not really sure what to say in the censored version that would make this okay."

    scene tsuneyouta15
    with fade
    stop music fadeout 25.0

    t "Hah..."
    t "There are so many things I do not understand."

    "Tsuneyo takes a seat on her computer chair and hugs her knees for what I imagine is comfort."
    "She already had to enlist the help of one of the most...outspoken members of the class tonight, so I’m sure she’s exhausted from having to talk for so long."
    "Or listen for so long."
    "But, then again, she deals with Molly on a daily basis...so maybe Uta wasn’t as much of a chore for her as I imagined she would be."

    s "Like what?"
    t "Like fucking...or what it means to live."
    s "If it’s any consolation, those two things are pretty interchangeable in my book."

    scene tsuneyouta16
    with dissolve
    play music "closeto.mp3"

    t "While Green Onion was able to provide me several useful tips for taking care of a loved one tonight, she also made things sound quite terrifying."
    t "I’m beginning to understand that my father’s time here may be coming to an end."
    t "He grows weaker day by day."
    t "It isn’t long before he’s unable to recommend me swimming tubes or teach me the proper ways to slaughter birds."
    t "I feel as if it were just the other day he was teaching me the difference between shio and shoyu."
    t "The fear of death you mentioned recently is starting to make sense to me."
    t "But it is not the act of death that torments me."
    t "It is the thought of what comes after."

    scene tsuneyouta17
    with dissolve

    t "I do not want my father to turn into a tree."
    t "You can not talk to trees. And they teach you nothing."
    t "Also, he will die in his room upstairs and a tree would be sure to crash through the floor and destroy the restaurant."
    t "What should I do?"
    s "Why ask me?"
    s "Death isn’t something I’m particularly good at dealing with. "
    s "And it’s not like I have all of the answers."
    s "Or...{i}any{/i} of the answers, for that matter."
    t "I do not expect you to. "
    t "But my father always told me adults are smarter than children."
    t "And though I may not possess the body of a child, my mind begs to differ."
    t "There is not a single day that passes by without me misunderstanding something. "
    t "I feel like an infant."
    t "I do not think I am suited for death."
    t "I don’t want to be alone."
    s "No one is {i}suited{/i} for death, Tsuneyo."

    scene tsuneyouta18
    with dissolve

    t "Ah-"
    s "Please don't “Ah-” me with that look on your face. It ruins the fun."
    t "It is a reaction. I can not help it."
    s "That aside...You should probably know that you’re never going to be alone."
    s "Do you really think Molly would abandon you or make you fend for yourself in the outside world?"

    scene tsuneyouta19
    with dissolve

    t "The Emerald Guardian does not like the outside world."
    t "She has informed me on many occasions that she is not particularly good at dealing with it and will avoid it by all means necessary."
    s "And that’s definitely true..."
    s "But she’s also experienced the death of a parent."
    t "That is correct. She told me about what happened to her mother."
    t "It sounded very hard."
    t "Will I go through the same thing?"
    s "Eventually, yes."
    t "..."
    s "A lot of the girls in class are missing a parent."
    s "In fact, barely any of them have both."
    t "Barely any of them have {i}none{/i} either. "
    s "Also a good point."
    s "If you think too much about the future, though, you’ll just run out of the present even quicker."
    t "..."

    scene tsuneyouta20
    with dissolve

    t "You are right."
    t "I must wait if I want to feel upset."
    t "I still have a job to do."
    t "My father has not yet given up on living, so I should not be giving up on him."
    t "I am a failure as a daughter."
    s "You’re not a failure..."
    s "In fact, I don’t even think what you were doing just now is giving up."
    s "You’re just confused."
    s "If you were giving up, you wouldn’t have reached out to Uta for help."
    t "I wish Green Onion was able to teach me how she remains so calm in the face of death."
    t "Her casualness on the subject makes me feel weak. Like there is much more for me to learn."
    s "She {i}is{/i} suspiciously casual about that and it is definitely concerning."
    s "But I don’t think you should worry too much about how other people would react to your situation."
    s "Just live each day as if it’s your last and you’ll be fine."

    scene tsuneyouta21
    with dissolve

    t "My last?!"
    t "Am I next?!"
    t "Why is life so cruel all of a sudden?!"
    s "It’s an expression, Tsuneyo. "
    t "Ah!"
    s "Your “Ah’s” are completely off tonight. It’s making me uncomfortable."

    scene tsuneyouta22
    with dissolve

    t "Perhaps it would be good if I just went to sleep early..."
    t "I have heard others mention that “beauty sleep” is good for them. "
    t "And I have learned recently through the art of photography that I, Tsunecchi Tojo, Warrior of Soup...am beautiful."

    scene tsuneyouta23
    with dissolve

    t "Probably."
    t "That is what the Emerald Guardian and the rest of her club told me, at least."
    t "And I have no reason to disbelieve them at this moment in time."
    s "Well, they’re right. You should listen to them more often."
    t "If I listened to them more often, we would not be talking right now."
    s "...Why?"
    s "What did they say to you?"

    if bonus == True:
        t "To stay away from you at all costs if I want to maintain my chastity."
        t "Unfortunately, I do not know what chastity is, so I am not too worried about this."

        "I imagine it was Maya who told her that..."
        "Though, I can see Ami saying it as well just to...thin out the competition."
    else:
        t "That I should go build the biggest sandcastle in the entire world."

    s "Okay, maybe {i}don’t{/i} listen to everything they say. But you can listen to the beautiful part."
    t "I am a free woman. You shall not tell me who I can and can not listen to."
    t "If you are looking for a fight, you have come to the right place."
    s "All I wanted to do was compliment you and now we have to fight?"
    t "You brought this upon yourself."
    t "Just as I will bring the pain upon your body."
    s "Okay then. I think it’s time for me to go."
    t "Running away from a challenge? "
    t "And you call yourself a man?"
    s "Yes."
    s "But, honestly, there’s a creeping feeling inside of me that’s saying you probably {i}would{/i} beat me in a fight and that would hurt my pride."

    scene black
    with dissolve2

    "I move toward the door and hear Tsuneyo get out of her chair."

    t "Wait."
    s "What’s up?"
    t "I feel as though I should thank you for listening to my problems."
    t "I was taught to never burden anyone, and my inability to function independently has led to me burdening you quite often."
    t "Please continue to nurture me."

    "Tsuneyo bows and I...can't help but feel out of place."
    "All I did was visit her room in hopes of seeing her in another costume."
    "I had no idea this would turn into...whatever it turned into."

    s "Of course."
    s "Though, I doubt what I’m doing could be called nurturing."
    t "If you think of a better word, please let me know."
    t "I’m looking forward to learning more from you."

    $ renpy.end_replay()
    $ tsuneyodorm20 = True
    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyodorm25:
    play sound "knock.mp3"

    "I knock on Tsuneyo’s door and wait for her to answer."
    "I can hear the sound of some video game or something from outside, so it’s probably safe to assume that Molly is also home given that Tsuneyo is...well, Tsuneyo."
    "I honestly can’t even imagine her playing video games."
    "Or...really doing anything apart from cooking or following Molly around."
    "But hey, I’m sure there has to be at least {i}one{/i} game out there that everyone can enjoy."

    t "You may enter."

    play sound "dooropen.mp3"
    scene black with dissolve

    "I open the door and make my way into Tsuneyo’s room to see what she’s up to."
    "........."
    "......"
    "..."

    scene tsuneyonumberonemobilegame1
    with dissolve

    "And, as it turns out, my assumption from several seconds ago is completely incorrect and Tsuneyo actually {i}is{/i} playing a game."
    "Is this character development?"

    s "Hey, what’s going on? It’s not like you to be spending the night on your computer."
    t "The Emerald Guardian has asked that I train myself in the art of virtual combat."
    t "As a junior master of the art of Kendo, I imagined something like this would be very easy."
    t "But I am currently struggling to even perform the most basic of commands."
    t "How will I ever show my face around her again if I can not keep up with her character?"
    s "Just beat her in real life combat and prove once and for all that playing video games is a waste of time."

    scene tsuneyonumberonemobilegame2
    with dissolve

    t "Can anything be called a waste of time if it is something a person enjoys?"
    t "While I do not appreciate this form of entertainment very much, the Guardian has devoted her life to it."
    s "What kind of game would a real, live person actually dedicate their life to anyway?"

    play sound "static.mp3"
    stop music
    scene raid1 with flash
    scene raid2 with flash
    scene raid3 with flash
    scene raid4 with flash
    scene raid5 with flash
    scene tsuneyonumberonemobilegame3 with flash
    stop sound
    play music "rapid.mp3"

    t "The name of the game is Raid: Shadow Legends."
    s "Oh. Then forget everything I just said, because Raid: Shadow Legends is the number one mobile game of all time."
    s "I didn’t realize you were also a Raider, Tsuneyo."
    t "Guess again, bro. Because I’ve been spending a lot of time on this game lately, and I’ve gotta say, the hype is real."
    t "With over seven characters and graphics, the video game is certainly a game that you play."
    s "You’ve got that right, Tsuneyo."

    scene tsuneyonumberonemobilegame4
    with dissolve

    t "Ah-"
    s "Are you gasping because I said your name again?"
    t "No. I just struggle to breathe every time I am not playing Raid: Shadow Legends, the number one mobile game in all of Kumon-mi."
    t "Did you know that for every new person who plays Raid: Shadow Legends, there is at least one more person playing Raid: Shadow Legends?"
    s "That...yeah. Yeah, that’s how playing the game would work."

    scene tsuneyonumberonemobilegame5
    with dissolve

    t "Raid: Shadow Legends is also very easy to learn. "
    t "If a sheltered girl with minimal computer experience like myself can learn how to log in, I’m sure that even the most technologically disadvantaged people out there can also learn."
    t "And with right now being a day, it is the best possible time to download the game and press the buttons that cause the game to do things."
    s "Do you have a favorite champion, Tsuneyo? Because I’m really fond of Nekhret the Great in the Undead Hordes faction and his “Unsleeping Aegis” passive ability."
    t "I like Mario the Plumber from the Plumber’s Guild. He can jump."
    s "Wow. I didn’t realize there was also a character like that in Raid: Shadow Legends."
    t "There wasn’t until recently. "
    t "As it turns out, Raid: Shadow Legends exhausted the list of possible champions and has now begun taking over other game markets and consuming their characters."
    t "I would not be surprised if you and I were the next ones in line."
    s "Why would either of us get thrown into Raid: Shadow Legends? We’re not characters in a video game and, even if we were, there’s no way a developer like...whoever makes it would approach us."
    t "I believe Raid: Shadow Legends is made by EA Sports. It’s inside of the game."
    s "I think you butchered their slogan a little, but that’s fine. I’m sure it’s only a matter of time before the developers of Raid catch on to this event and-"

    scene raid6

    s "Oh, fuck."
    t "Why has everything suddenly gone so dark? "
    t "I am scared."
    s "It’s probably because you went so off-script and started talking about stuff that isn’t actually in Raid."
    t "Nonsense. There is no way the original developers of titles like-"

    scene raid7

    t "Oh. The screen changed again."
    s "Double fuck."
    t "I stand corrected. What have we done?"
    s "{i}I{/i} haven’t done anything. It’s you and the rest of the girls who keep bringing up copyrighted products and titles. "
    s "I’m just trying to be a likable protagonist."
    t "And how is that going for you?"
    s "Horribly. "

    play sound "static.mp3"
    scene tsuneyonumberonemobilegame6 with flash
    stop sound

    t "Woah."
    s "Nevermind what’s on your monitor, Tsuneyo. Tell me more about [[Censored due to DMCA claims]."
    s "Oh, god damn it."

    scene tsuneyonumberonemobilegame7
    with dissolve

    t "I suppose the time has come to move on."
    t "If we spend the next several minutes continuing to talk about this, more people will cancel their support for Selebus."
    s "You’re right. God forbid fourth wall breaking comedy finds its way into a game that is definitely serious 100%% of the time and hasn’t already been adding similar jokes for over one year as of October 8th, 2021."
    t "I can see the exit surveys now."

    scene raid8
    with fade

    s "You know, this world would be a much better place if more people would realize that some things exist just because a creator wants them to."
    t "That is correct, Sensei. The entire purpose of art is to express a certain idea or a feeling. And the moment artists let people control what they create, art ceases to be."
    s "Shhhh, they’ll call us pretentious again and that hurts our feelings."
    t "Oh, right. Instead of continuing this discussion, why don’t we simply wait ten seconds to see what happens?"
    s "Good idea. That will also give us an ample amount of time to continue guilt-tripping everyone into giving us their money to fight back against the totally real DMCA claims. "
    t "Sounds good to me, bro."

    scene raid9
    with dissolve10
    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh13 with flash
    scene ayhh12 with flash
    scene ayhh10 with flash
    scene tsuneyonumberonemobilegame8 with flash
    stop sound
    play music "sweetvermouth.mp3"

    t "And that is why I do not normally like video games."
    s "..."
    t "Sensei?"
    s "Oh, sorry. I just feel like we got involved in something really weird that I...am having trouble remembering."
    t "I have heard you mention several problems involving your memory in the past. Do you believe it could be pertaining to that?"
    s "Nah. I’m sure it’s nothing."
    s "But please continue telling me more about your relationship with video games and how it pertains to our meeting tonight."

    scene tsuneyonumberonemobilegame9
    with dissolve

    t "I believe the Emerald Guardian is experiencing heartbreak for the first time, so I would like to do more things outside of the box to help her feel better."
    t "However, there are not many boxes in this room and the possibilities seemed far too great for me to choose just one."
    t "So, I decided to simply start doing something else she likes so she does not have to always play alone."
    t "I am very bad, though. So I believe I may have to start trying something else."
    t "If only she liked more games that did not take place inside of computer screens."
    s "I mean, haven’t you been watching her play that one game she plays with all of the other girls? Why not learn that?"

    scene tsuneyonumberonemobilegame10
    with dissolve

    t "I did. But it seems as if my presence in that game may have caused a bit of a rift since that is when the Guardian’s heart showed its first signs of cracking."
    s "I don’t really get what you mean by that, but I’m sure there are some other {i}actual{/i} games Molly enjoys."
    s "Like...what did you have in mind? Board games or like...playing cards or something?"

    scene tsuneyonumberonemobilegame11
    with dissolve

    t "Mahjong perhaps?"
    s "Mahjong? Isn’t that more for...older people?"
    t "Possibly."
    t "I learned by watching my father play a long time ago."
    t "It seemed very complicated, but he was always happy whenever he won and very sad whenever he lost."
    s "I would imagine it’s because he was gambling."

    scene tsuneyonumberonemobilegame12
    with dissolve

    t "To exist is a gamble in itself."
    s "Sure. But not for money."

    scene tsuneyonumberonemobilegame13
    with dissolve

    t "I suppose it would have made sense if there was money involved."
    t "That would certainly explain all of the money that was on the counter as he played."
    s "...What else did you think that money could have been?"
    t "Noodle money, paid in advance. I do not know."
    t "I was [young]and naive and did not think much of it."
    t "Now, I am older and slightly less naive, so I am able to better understand the meaning behind certain situations."

    scene tsuneyonumberonemobilegame14
    with dissolve

    t "My father is likely a gambling addict and I am set to inherit his debt."
    t "Now I {i}must{/i} teach the Emerald Guardian to play so I can push that debt onto her instead."
    s "So, your new method of cheering Molly up is to riddle her with debt before she finishes [high_school]?"

    scene tsuneyonumberonemobilegame15
    with dissolve

    t "I do not know what to do, Sensei. It is beginning to feel as if some wounds require nothing but time to heal."
    s "I mean...yeah. That’s kind of how it works."
    s "Having friends is nice and all when they can make you feel more...valid or whatever, but I’ve always believed the best way to get over anything is to let time take control."
    s "Sure, it’s a bitch more often than not, but it’s a hell of a lot better than a game."
    s "Right now, Molly’s options are either keep running forever...or wallow in misery until that misery is less...miserable."
    t "Neither of those seem like very good options."
    s "Nope. But what can you do?"
    t "Apparently nothing."
    s "Exactly. Her problems are her problems."
    s "It’s nice that you want to help her, but not if you’re going to be busting your ass trying new things that are just making {i}you{/i} feel worse. You know what I mean?"

    scene tsuneyonumberonemobilegame8
    with dissolve

    t "I do not think so. Now, I just feel inclined to find something to make you happier as well."
    s "What? Why?"
    t "Because even if I do not like you, I still like you."
    s "...What?"
    t "Tell me, is there something you would like to do that would make you feel more significant as a human being?"

    if bonus == True:
        s "Yes, but I don’t think we’re at that level yet."
        s "And it would really only make me feel more significant for a short burst of time until I go home and lay down again and it all gets worse."
    else:
        s "You can help me find my old baseball trophies so I can remember how I was always the most improved player every year."

    scene tsuneyonumberonemobilegame16
    with dissolve

    t "Perhaps I could teach you kendo?"
    s "What? Why would that be your first choice for “things that will make me feel more significant?”"
    t "Despite your physique, you appear to be weak and fragile."
    t "Perhaps, if you could defeat an enemy in combat, you will level up and gain skill points to distribute into various categories like “Happiness” and “Confidence.”"
    s "I don’t really know much about games nowadays, but I don’t think those are categories you can just put points into."
    s "Besides, which “enemies” would I even defeat? Everyone I know likes me."
    s "Even the people that {i}don’t{/i} like me probably like me. They just need more time to realize it."
    t "What an optimistic way of looking at things."
    s "I’m not really known for my optimism, but I’m also not really known for my kendo and would much rather fake being positive than have to learn something like that."
    s "Besides, I’m already enrolled in a karate class."

    scene tsuneyonumberonemobilegame17
    with dissolve

    t "You are learning karate?"
    s "I mean...no. But I {i}am{/i} enrolled."
    s "And by “enrolled” I mean that I just show up there whenever I want and talk to Ayane."

    scene tsuneyonumberonemobilegame16
    with dissolve

    t "As long as doing that makes you feel less horrible inside, I can accept it."
    t "I will keep the kendo offer on the table, though."
    t "Nothing makes a person feel better than slaughtering a foe. I am sure you are no exception to that very common rule."
    s "I didn’t realize the purpose of kendo was to “slaughter.”"
    t "Neither did any of my adversaries in the national competition. That is why they lost."
    s "You know...sometimes, I feel like you could secretly kill all of us if you really wanted to."
    t "Sometimes, I feel that way as well."
    s "Great. That’s not terrifying or anything."
    t "What is even more terrifying is the prospect of a situation in which I would need to do that."
    s "And on that note, I’m going to go back home and hang out with my [niece]- a person who would definitely not ever kill me."
    s "Everyone else? Maybe. But definitely not me."

    scene tsuneyonumberonemobilegame12
    with dissolve

    t "I understand."
    t "Thank you for stopping by to talk to me about violence tonight."
    s "That’s...not really why I came."
    t "But it was the end result, which means it will be all I take away from this conversation."
    t "I do not see how this will help me cheer up the Guardian at all."
    s "Me neither. But, if worse comes to worst, you can always just...slaughter her?"

    scene tsuneyonumberonemobilegame18
    with dissolve

    t "Sometimes, I believe you to be a machine who only exists to come up with the worst possible answers to things."
    s "That’s...as good a theory as any, I guess."

    scene black
    with dissolve

    s "Goodnight, Tsuneyo."
    t "Ah-"
    t "Goodnight to you as well."
    t "If you come up with a good way to assist the Guardian in not feeling sad anymore, please inform me."
    t "It is my role as her newly appointed squire to keep her in top form."
    s "I...will do just that."

    play sound "dooropen.mp3"

    "I make my way out of the room feeling as if I’d been there for much longer than I actually was."
    "It’s nice knowing that Tsuneyo is looking out for Molly in regard to the whole Rin thing, but I’m confused about whether or not she knows what’s {i}actually{/i} wrong."
    "Would Tsuneyo doing something like...learning to play games or teaching Molly mahjong really help her get over heartbreak?"
    "Nothing can be that simple, can it?"
    "And...if it is that simple, can it really be called heartbreak at all?"
    "..."
    "I don’t know why I’m thinking about this right now."

    if bonus == True:
        "I slide my phone out of my pocket and begin to distract myself with porn on the way home."
    else:
        "I slide my phone out of my pocket and begin to distract myself with videos of excited dogs seeing their owners after long periods of time."

    "Something like this is much easier than...whatever I was doing before."
    "I’ve already forgotten."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyodorm25 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollydorm25:
    play sound "dooropen.mp3"
    stop music fadeout 20.0

    "Molly and I escape back into the warmth of the dorm just as the night decides to get all fucking annoying and start showing off how fast it can make the wind go."
    "She appears a little confused the moment I start following her upstairs, but makes no effort to actually stop me."
    "I imagine there’s a chance she’s just worried that she’ll have to think up some sort of {i}actual{/i} quest reward or whatever it was I was promised-"
    "But I imagine there is an even {i}better{/i} chance that she’s just confused about where things will go from here as a whole."
    "So am I, to be honest. "

    if bonus == True:
        "I mean, surely I wouldn’t be seizing this opportunity to make some sort of move on a cute girl fighting off both the sting of rejection and sleep deprivation, would I?"

        s "..."

        "I remain silent in hopes that asking myself this rhetorical question will somehow push me in either direction."
        "Unfortunately-"

    scene mollydormchanging1
    with dissolve
    play music "love.mp3"

    "I somehow wind up inside of her room."
    "Now, the reason I use the word {i}un{/i}fortunately isn’t because I’m worried about how forcing a girl into an uncomfortable position will feel-"
    "But it’s because I feel slightly bad that Molly can’t really do anything to change that."
    "Nor do I know if she {i}would{/i} change that, given the opportunity."
    "All I know is that she said she was worried that being back here would cause her to start thinking."
    "Sometimes, however, I think it’s better to act without any thought put into things at all."
    "Hence, bedroom."

    mo "Sir, if this is about your quest reward, I’m afraid I don’t have one on hand right now."
    s "Eh. I don’t need a reward. "
    s "I’m just bored."
    mo "Darkness has already consumed the land, and yet you beg for more of Molly MacCormack?"
    mo "What would Arborea say?"
    s "I’m sorry, who?"
    mo "Apologies, Sir. I meant Ami."
    mo "Does she not spend each night in silence, awaiting both your presence and a single genre tag that forces people to download a video game without even reading the description first?"

    if bonus == False:
        s "What are you talking about? Ami and I are in no way, shape, or form related."
    else:
        s "As if that would ever happen."

    s "Besides, I’m sure Ami is fine. Chances are she’s already asleep."

    scene mollydormchanging2
    with dissolve

    mo "Ahh, sleep..."
    mo "I remember those days well. T’was back when I was just a lass."
    mo "Long before I’d given up on ever experiencing the taste of sweet slumber ever again."
    s "Cool. More time to hang out with me."

    scene mollydormchanging3
    with dissolve

    mo "Sir, you have been suspiciously nice to me all night. It’s beginning to feel like you may have accidentally activated my route instead of someone else’s."
    s "I’m just doing what I always do. It’s up to you whether or not this is about to become {i}your{/i} route."
    mo "It’s never up to the heroine, Sir. That’s just an illusion meant to trick readers into believing they’ve done more than click buttons and set a few invisible flags to “True.”"
    s "Well, whatever it is, I’d still like to kill a little time before heading back home."
    s "Unless you’re planning on letting me crash here, that is."

    scene mollydormchanging4
    with dissolve

    mo "Well...I suppose I wouldn’t have much of an issue for that. Party members sleep together and manage to avoid getting physical all the time. "

    if bonus == True:
        s "I mean...we don’t have to {i}avoid-{/i}"

    mo "The main issue is that the Kendo Princess normally comes home around this time as well, and I can’t imagine she would feel very comfortable with this...sudden development."
    s "Then I’ll just stay until Tsuneyo is back."

    scene mollydormchanging5
    with dissolve

    mo "That seems like a respectable decision."
    mo "The issue now is that I would like to switch transmogrifications, which I can not do with you standing there gawking at me."

    if bonus == True:
        s "I have no idea what you just said to me."
        mo "Pajamas, Sir. I would like to get changed."
        s "Oh, sure. Go right ahead."
        mo "..."
        s "..."
        mo "{i}Without you gawking at me.{/i}"
        s "Oh."
        s "Yeah, I can’t help that."

        scene mollydormchanging6
        with dissolve

        mo "But...you have already seen me without my armor on once before. "
        s "Yeah, which is why I don’t think it’s a big deal."
        s "Just keep talking. It’s only weird if you decide to make it weird."
        mo "It appears that you have already decided to make it weird. Cease holding your actions and use them to look away."
        s "Hey, you still owe me a quest reward. This would be a good time for that, wouldn’t it?"

        scene mollydormchanging7
        with dissolve

        mo "Ahh...lookin’ to barter, are ye?"
        mo "How about this then, Sir?"
        mo "The Halloween party is just a short while away. What if I told you I could give you a behind the scenes glimpse at the costumes of various girls in our class?"
        s "Go on."
        mo "So long as you manage to keep me out of your line of sight for the duration of my transmogrification, I’ll show you."
        s "I don’t know, Molly. Real life still sounds a little better than a few pictures."
        mo "It is six girls, Sir."
        s "Six? Damn it. That’s so many."

        scene mollydormchanging8
        with dissolve

        mo "The costumes are rather form fitting as well. If you look closely enough, you can see {i}everything{/i}, Sir. "
        s "Everything?"
        mo "Right down to the last mana circuit."
        s "Tch."

        "I click my tongue like some sort of anime protagonist and accept that this proposition will be the end of me. "
        "Well, the end of my chances of seeing Molly naked right now."
        "I’m sure I’ll be able to see the real thing up close sooner or later."
        "Just...it probably won’t be soon {i}enough.{/i}"

        scene black
        with dissolve2

        s "Okay, fine. "
        s "But I reserve the right to trade away the picture and turn around at any moment."
        mo "What kind of ass backwards deal is that, Sir? Roll for persuasion."
        s "Roll for what?"

        play sound "dice.wav"

        mo "Geh. Fine, I’ll roll for ya and-"
        mo "Brigid’s bosom, it’s a natural twenty."
        s "Is that good or bad?"
        mo "Good for you, bad for me. You win your wonky barter clause, Sir. But please do try to not invoke it."

        scene mollydormchanging9
        with dissolve

        s "Do you just keep dice on you at all times or something?"
        mo "Of course, Sir. You never know when you’re going to need a D20. And dice apps just can’t compete with the feeling of a nice, solid one in your hands. "
        s "I’ve got a nice solid one right here."

        scene mollydormchanging10
        with dissolve

        mo "A D20?"
        s "A penis."
        s "It was an erection joke."

        scene mollydormchanging11
        with dissolve

        mo "O...Oh! Yes! I knew that."
        mo "Nothing beats a good ole...dirty joke. That’s for sure."
        s "Why are you the one making things weird after finally convincing me not to?"

        scene mollydormchanging12
        with dissolve

        mo "Hah...Who knows, Sir?"
        mo "You should be happy I haven’t pounced on you and demanded that we kiss, yet."
        s "Should I? Because that sounds a lot like a thing that I would enjoy."
        mo "Doubtful, Sir. You find me annoying and have already confirmed with ye’ own eyes what I watch when I’m...indulging myself."
        s "Why would knowing you [masturbate] to pictures of Rin make me not want you?"

        scene mollydormchanging13
        with dissolve

        mo "Some would equate even minor actions like that to NTR, Sir."
        mo "Some men just have so little confidence that they get angry if even cartoons don’t pay sufficient attention to them."
        s "That’s just sad."
        s "Thankfully, we are both real people and those sorts of things don’t apply to us."
        mo "I thank you for the privilege to [masturbate] to my friends without the fear of losing you, Sir."
        s "You’re welcome, Molly."
        s "I’d appreciate to be included in those fantasies from time to time as well, though."

        scene mollydormchanging14
        with dissolve

        mo "‘Tis hard when you’re nothing more than a ghost on the Internet, Sir."
        mo "Why should I submit to fantasy when there are so many accessible swimsuit pictures of people I’m attracted to?"
        s "I thought fantasizing about stuff was kind of your thing?"
        mo "Not all of the time, Sir."
        mo "Just most of it."
        s "So, what I’m hearing is that the key reason you [masturbate] to Rin instead of me is because she has a social media profile."
        mo "Aye, Sir. The profile helps."
        s "Molly, this is the single best argument anyone has given me for starting one of those things yet."

        scene mollydormchanging15
        with dissolve

        mo "I’m glad to have been of service, Sir! "
        mo "Now, come! Feast your eyes upon tonight’s quest reward in the form of six girls in costumes you will likely not recognize!"

        scene black
        with dissolve
    else:
        scene black
        with dissolve

        s "Understood. I will now close my eyes to avoid the next part of the event."
        mo "Thank you. I appreciate how unwilling you are to make any romantic advances on me given the nature of our relationship."

    "Molly removes her cell phone from a pile of clothes she left near the door and begins to make her way over to the bed, swiping through various images until she finds the one she needs."
    "I take a seat beside her and she pulls her knees closer to her chest before tilting her screen up and showing me my apparent reward."

    scene mollydormchanging16
    with dissolve

    mo "So, I’m sure you have no idea what any of this is, nor do I imagine you want me to educate you, but here you go."
    mo "The members of the manga club...and Ayane have decided to do a group cosplay for Halloween this year."

    scene mollydormchanging17
    with dissolve

    s "Why doesn’t Ayane just join the club as well if she’s going to keep doing literally everything with you guys anyway?"
    mo "Something about wanting to save more time for when you two elope, I believe."
    mo "Is that really all you have to say, though? I was expecting more of an excited reaction out of you, Sir. "

    if bonus == True:
        mo "Especially with all of our thighs being out there in the open."
        s "Oh, don’t get me wrong, I think you all look great. "
        s "But, if anything, I’m just more excited to see you all in person now."
    else:
        s "Absolutely not. I am respectable and kindhearted man who is just very excited for Halloween."

    scene mollydormchanging18
    with dissolve

    mo "You will not have to wait much longer, Sir."
    mo "I intend to make this Halloween one that I will remember for the rest of eternity! Especially after losing most of my memories of the last one!"
    s "You were...extremely drunk."

    scene mollydormchanging19
    with dissolve

    mo "You probably should have called an ambulance. I could have died."

    if harukalust10 == True:
        s "Sorry. I had...things to do."
        mo "What sort of thing would be more important than saving a student’s life?"

        if bonus == True:
            s "A threesome with two cat girls."
            mo "Oh."
            mo "Well...yes. I understand completely, if that was the case."
        else:
            s "I was volunteering at the local soup kitchen, providing meals for the homeless."
            mo "You're such a good guy, Sir."
            s "Yes. I am."

    else:
        s "Sorry. I had..."

        play sound "static.mp3"
        scene harukalusttenskip3 with flash
        scene mollydormchanging19 with flash
        stop sound

        s "I had to fix some pipes..."
        mo "..."
        mo "What?"
        s "Doesn’t matter."

    s "Anyway, what else do you have for me?"
    mo "I’m sorry?"
    s "That can’t be the only picture, can it?"
    mo "There are some on the other girls’ Instagrams, but the only extra ones I had were of Rin from when I tailored hers...and I deleted all of those."
    s "Really? Not going to keep them around to-"
    mo "Please don’t, Sir. It still hurts, even if I’m not acting torn up about it."

    if bonus == True:
        s "That’s weird. Because we were talking about it a few minutes ago and you seemed totally fine then."
    else:
        s "I understand. We can stop talking about this now."

    scene mollydormchanging20
    with dissolve

    mo "I know."
    mo "But seeing her again made it hard."
    mo "I’m only good at running away from my problems when they’re not trying to catch up, I suppose. "

    if bonus == False:
        s "Molly pls."

    mo "My movement speed just isn’t fast enough."
    s "Well, I’m not going to keep pestering you about it. I’ve done enough of that today and I’m starting to think I might be doing to {i}you{/i} what you always do to me."
    mo "I don’t mind. It’s nice having friends again."
    s "Okay, I guess I’ll pester you one last time in informing you that you {i}do{/i} still have friends."
    s "Getting into a fight over liking someone isn’t enough to destroy something like that. And, if it is, it was probably a shitty friendship to begin with."

    scene mollydormchanging21
    with dissolve

    mo "Sir, you are forgetting how things ended. It may not sound as bad for someone who wasn’t there, but it was extremely awkward for even my standards."
    mo "And need I remind you that I have very high standards for what is and isn’t awkward?"
    s "No reminder is necessary. You’re probably the most socially awkward person I know apart from Tsuneyo or Kaori or...Yasu-"
    s "Why are so many of you awkward?"
    mo "The point, Sir. You are losing it."
    s "Right, sorry. "
    s "What I’m saying is that apart from the various...{i}special{/i} cases, the only other person I know who is almost as awkward as you is Rin."
    s "Which means that she’s more likely to just get over this than anyone else."
    s "Maybe."

    scene mollydormchanging22
    with dissolve

    mo "That “maybe” causes me a great deal of worry, Sir."
    s "Well, if you’re {i}that{/i} worried...just go talk to her."
    mo "I don’t know...the last time I took someone’s advice about this, I was either duped or...I greatly misunderstood that person."
    mo "The great downfall occurred just shortly after that, when I had already chosen the path I was going to walk."

    scene mollydormchanging23
    with dissolve

    mo "But...as the gears screeched to a halt and all of the cogs in this machine called “life”  stopped spinning, I knew something needed to be done."
    mo "If only I had known that “something” was the opposite of what the voice inside of my head commanded of me."
    s "..."
    mo "..."
    s "So, are you going to talk to her or not?"

    scene mollydormchanging24
    with dissolve

    mo "What, like...right now?"
    s "Sure. Rin stays up late, doesn’t she?"
    s "And if there’s anything I’ve learned about serious situations in the dorms, it’s that a person’s roommate is almost always conveniently missing exactly when they need to be."
    mo "You know, Sir...Now that you mention it, I do remember Futaba mentioning something about going to the bookstore with Nodoka tonight."
    s "See what I mean? Now is as good a time as any."

    scene mollydormchanging25
    with dissolve

    mo "I don’t know..."
    mo "Rin said she wanted to take a break from speaking for a while."
    mo "And...and what if Otoha is there?"
    s "At this hour? Her mother would never allow that."
    mo "..."
    s "..."

    "Molly takes a moment to think about what her next move is going to be."
    "I’m sure it's hard deliberation considering her only options are “keep indefinitely being sad” or “risk becoming more sad in order to be less sad right now,” but...those are kind of the only options we ever have."
    "And even if time does have a way of mysteriously healing things, it doesn’t mean it’s exciting to just sit back and let that happen."
    "The most ideal scenario right now would be for Molly and Rin to {i}both{/i} be happy."
    "And if I have to put someone else’s well-being at stake in order to risk that, so be it."

    mo "Will you...come with me?"
    s "Me? Why?"
    mo "Moral support, I suppose."
    mo "Our party hasn’t disbanded yet, so...just think of it as another side quest."
    s "..."

    if bonus == True:
        s "Fine. But the reward for this better be more than just a picture of my students wearing clothes, skin tight or not."
    else:
        s "Fine. But you owe me a soda."

    scene mollydormchanging26
    with dissolve

    mo "Understood, Sir. And thank you."
    mo "But...I still don’t know what I should say."
    s "When in doubt, just be honest. "
    s "That’s what I always do and it only backfires like...less than half of the time."
    mo "...Slightly less than half? Or significantly less than half? Because I do not feel good about those odds if it is the former."
    s "Doesn’t matter. You’ve already decided and I’m going to be there with you every step of the way."
    s "Unless you or Rin asks me to leave. "
    s "If that happens, I imagine I’ll put up a fight for a little while but ultimately just go anyway."
    mo "..."
    s "..."

    scene mollydormchanging23
    with dissolve

    mo "{i}Hah...{/i}"
    mo "Good thing we stopped at that leyline earlier. Otherwise, there is no way I’d allow you to talk me into this."
    s "Sure you would. You just needed an excuse to do something you already wanted to do, and telling you this is just one more example of my brutal honesty making things better."
    mo "That didn’t make anything better at all..."

    scene black
    with dissolve2

    "Molly decides to keep her pajamas on for the trip back downstairs- probably because it would look weird to get dressed up for a second round of rejection."
    "Or, in the best case scenario- the {i}first{/i} case of her and Rin trying to make things work."
    "We just have to hope at this point that Rin is still awake."
    "But given how excited she still seems to have a girlfriend, I imagine it’s possible she hasn’t slept at all since the beach."
    "But hey, that puts her back into the same category as Molly, even if the two of them have already begun to drift apart."
    "Maybe this small similarity, albeit the result of opposite extremes, is all they’ll need in order to get closer again."

    play sound "dooropen.mp3"

    s "..."

    "Or maybe it will end things once and for all."
    "You can’t ever really know until it’s too late, can you?"

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollydorm25 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "..."

    jump rindorm50special

label mollydorm30:
    play sound "knock.mp3"

    "I knock on Molly’s door and wait for her to answer, but can’t help but notice a surprisingly familiar sound being muted as I do so."

    mo "..."
    s "..."
    s "Molly?"
    mo "Oh, it’s just you, Sir. "
    mo "I suppose that’s fine, then."
    mo "You may enter."
    s "Uhh...okay."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I turn the knob and make my way into Molly’s room, noticing that the volume has been slightly raised, but is still on the low side."
    "Based on what I {i}can{/i} hear, however..."

    if bonus == True:
        jump mollypornx
    else:
        s "Are you playing Raid: Shadow Legends again?"
        mo "Yes, Sir! Only the most important mobile game of our generation!"

        "Molly and I play Raid: Shadow Legends for a few hours before we decide to go outside and talk about Raid: Shadow Legends there."

label restofmollyporn:
    if bonus == True:
        "Molly takes a moment to put her clothes back on, once again making me turn around so I can’t watch her, and I begin to wonder how far I’m off from getting to skip that barrier in the future."
        "I mean, I know Molly’s been a little more open about stuff like this than most of the other girls for quite some time now, but I feel like this rejection thing might just be making her spiral into perpetual apathy."
        "Or something like that."
        "I don’t really know- nor do I care, since I’m already reaping the benefits of her sudden sexual growth."
        "Or disinterest."
        "Again, I still don’t really know."
        "But that doesn’t matter right now."
    else:
        "I guess the outside part doesn't really matter, now that I think about it."

    scene mollyporn8
    with dissolve2
    play music "thesleepingcity.mp3"

    "What {i}does{/i} matter is that it’s fucking cold."

    if bonus == True:
        s "I’m starting to think that {i}I{/i} should have [masturbate]d before coming out here to raise my body heat."
        mo "Very funny, Sir."
        mo "Though, I will admit that I am not feeling the cold just yet. So perhaps your idea isn’t too bad in the grand scheme of things."

    s "So, is {i}that{/i} really all you’ve been doing lately?"

    scene mollyporn9
    with dissolve

    mo "Playing games?"
    s "Playing those kinds of games."
    s "If you’re doing it to the point where it’s not even fun anymore and just a means of killing time, I can think of a lot better ways to do that."
    mo "There are always {i}better{/i} ways to do anything, Sir. But it doesn’t mean that anyone will actually do them."

    scene mollyporn10
    with dissolve

    mo "Growing closer to someone inside of a setting where everything is make believe is better in every way than doing the same thing in real life."
    mo "You don’t have to leave your chair. You don’t have to worry about what anyone thinks of you. And you can also look up a walkthrough whenever you get stuck."
    mo "This realm does not have walkthroughs, Sir. You need to fail in order to figure out what to do next."
    mo "But failing is painful...and closes off certain paths to you for good."

    if bonus == True:
        mo "So, if I continue to avoid that, I’ll find nothing but success in love and...sex."
        mo "And I can also have a million girlfriends or boyfriends and none of them will get jealous of one another unless it's a major underlying theme of the games they appear in."
        s "Now, that definitely does sound like a plus. Except for the boyfriend thing. I don’t really need one of those."

        scene mollyporn11
        with dissolve

        mo "See? This way of living isn’t entirely bad!"
        mo "Just...it can be a little depressing when you take the time to actually {i}think{/i} about what’s happening."
    else:
        s "Are we still talking about Raid: Shadow Legends?"

    scene mollyporn12
    with dissolve

    mo "You know...after seeing what Rin did to herself...and what she said to me...I couldn’t help but tear myself up over it."

    if bonus == False:
        s "I guess not."

    mo "And even though I disagreed in the heat of the moment about...{i}choosing{/i} her...I think she may have been right."
    s "I don’t think anything Rin said that night was “right.” "
    s "It’s hard for someone to make any sort of argument while having their wounds held shut by someone else."
    mo "That part...I don’t disagree with."
    mo "What I {i}do{/i} agree with, though, is that I didn’t have to push things further."
    mo "I knew she didn't want me...but I tried to make her want me anyway."
    mo "I didn’t have to start moving away from 2D out of...curiosity or interest or whatever other foul magic may have caused me to do the things I did."
    mo "I could have stayed inside of the vessel that’s served as my escape for so long now."
    mo "I don’t {i}have{/i} to want someone real. But I did anyway."
    mo "And that was a choice."
    s "..."
    mo "..."

    scene mollyporn13
    with dissolve

    mo "It was a choice..."
    mo "The wrong choice."

    if bonus == True:
        jump endofmollyoutsidex
    else:
        s "..."
        mo "..."
        s "Okay, well you're weirding me out so...I'm gonna go."
        mo "Okay, see ya."

        scene black
        with dissolve

        "The conversation comes to an abrupt end, but I manage to escape without hugging Molly."
        "I don't really know why, but I feel like I might have to hug her eventually."
        "I hope the Irish are okay with that. I don't really know much about their culture."

        $ renpy.end_replay()
        $ molly_love += 1
        $ mollydorm30 = True
        stop music fadeout 5.0

        "{i}Molly’s affection has increased to [molly_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

                    ############################################
                    ##########        ROOM 7          ##########
                    ############################################

label utadorm:
    if uta_love >= 5 and utamaid5 == True and utadorm5 == False:
        jump utadorm5
    if uta_love >= 10 and utadorm5 == True and day != 2 and utadorm10 == False:
        jump utadorm10
    if uta_love >= 15 and day != 2 and utamaid10 == True and utadorm15 == False:
        jump utadorm15
    if uta_love >= 30 and utamaid25p2 == True and utadorm30 == False:
        jump utadorm30
    if uta_love >= 40 and utadate35 == True and day != 2 and wakanadate25p3 == True and utadorm40p1 == False:
        jump utadorm40p1
    elif uta_love >= 5 and utamaid5 == False:
        "I should probably get to know Uta a little better before I see if she wants to hang out in her room."
        jump doorknock2
    else:
        jump utadormgen

label utadormgen:
    play sound "knock.mp3"

    u "Come on in!"

    scene utadormgen
    with fade

    "I walk into Uta's room to find her just lounging around and listening to music on her phone."
    "She hops off the bed and excitedly hurries over to me, almost slipping on a pair of pants near her end table."
    "Fortunately for her, I'm able to catch her before she winds up cracking her head open on the floor."
    "{i}Unfortunately{/i} for me, this gives her the opportunity to tease me for the next half hour about keeping my hands to myself."
    "I'm sure she's just kidding, but I still get the urge to let her fall next time."
    "Of course, I'd feel overwhelmingly guilty if she actually got hurt."
    "And I definitely wouldn't want it to impact her appearance in any way, so..."
    "I guess I can take one for the team and let her tease me for a while longer."
    "Even if I saved her life."

    scene black
    with dissolve

    "The night goes on with just as much quirky flirting as I expected when I came here, and I wouldn't trade a second of it for anything else."
    "Well, actually, I'd definitely trade it for the opportunity to have all of that flirting to come to fruition, but..."
    "I guess something like that just isn't in the cards for tonight."
    "Either way, I'm glad I got to spend some time with Uta."
    "I can feel the two of us growing closer every single day."

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta's affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label utafirsthall:
    scene utahall1
    with dissolve

    u "Hey! What are you up to, Sensei?"
    u "Come to hang out with one of your six million girlfriends?"
    s "All of them at once, actually. And what better place to do that than the dorms?"
    u "Hmmm...School, if you can be sneaky enough."
    u "That way, you could even rope some of the other classes into it. You can thank me later for the brilliant idea."
    s "I might just have to do that."
    s "What are {i}you{/i} up to, Uta?"
    u "Me? Was just stopping for a quick drink of water on my way out to do some exploring."
    s "Right. You’re still getting acquainted with the area, aren’t you?"
    u "Slowly but surely. It’s not as confusing as the area I was living in before this."
    u "Over there, since the[school] was {i}in{/i} the actual city part, we didn’t get those cool stretches of nothingness like you have over here."
    u "Reminds me a lot of Nara but with less wildlife and more...tamed life."
    s "Is that a good or bad thing? I don’t think I’ve really asked you how you feel about this place other than the class itself."

    scene utahall2
    with dissolve

    u "It’s not...bad?"
    u "Like yeah the class is awesome and I’m glad to finally have a teacher who doesn’t creep me out-"
    s "Wait, what? Your other teachers creeped you out but I somehow don’t?"

    scene utahall1
    with dissolve

    if bonus == True:
        u "Oh totally. The fact that you’re so up front about how interested you are in [younger_girls] is actually weirdly comforting in a way."
        u "It’s like, “Oh, nothing this guy does will surprise me.”"
        u "My other teachers have all been like, the secret kind of perverts who just stare at everybody from behind their desks and daydream instead of actually acting on anything."
        s "I’m pretty sure that’s just how people are supposed to act, especially in public settings."
    else:
        u "Oh, totally. They kept trying to steal my stuff when I wasn't looking."
        s "You should report that to the principal."

    scene utahall2
    with dissolve

    u "Probably. You’ve been fun so far, though. "
    u "As far as Kumon-mi itself goes, it’s not what I’d call my ideal place to live...but it’s not like I’m dying to get out just yet."
    s "What would your ideal place to live be, then?"

    scene utahall3
    with dissolve

    u "Well, even though it can get kind of boring over there at times, I think I {i}do{/i} prefer the country overall."
    u "Places like this kinda lose their luster once you realize you can just do anything you want whenever you want."
    u "It turns stuff I always viewed as super-special outings into another way of life. "

    scene utahall4
    with dissolve

    u "But, it’s definitely easier finding work over here. Not a lot of maid cafes where I’m from."
    u "And also not a lot of teachers willing to just let us girls teach ourselves. So, thanks!"

    "Interesting."
    "I don’t think I’d particularly enjoy living in the country."
    "But it’s not like Uta and I need to agree on everything in order to become better acquainted."
    "I understand why she’d want to be somewhere closer to what she’s grown used to over the course of her life."
    "Thankfully, I have the advantage (Or disadvantage, depending on how you look at it) of not remembering anything about my childhood-"
    "So somewhere like Kumon-mi is perfect for me."

    s "No need to thank me for being bad at my job. I do that willingly."

    scene utahall5
    with dissolve

    u "Hey! Don’t call yourself bad!"
    u "I’m tryin’ to be serious here, Sensei. I think you’re great."
    u "Even Io has started feeling at home here and I don’t think she even looks at the bathhouse that way."

    scene utahall1
    with dissolve

    u "Plus, I think it’s cool that you’re allowed to come to the dorms and talk to us. "
    u "I feel more inclined to learn if I’m closer to whoever’s teaching me."
    s "Is that code for “Let’s get even closer, Sensei?”"

    scene utahall6
    with dissolve

    if bonus == True:
        u "Ohohoh~ Turnin’ the moves on even though I’m wearing three layers of clothes and a hat that smiles back?"
        s "I wouldn’t have it any other way."

        scene utahall7
        with dissolve

        u "Thank you, Sensei. But as much as I appreciate your advances and unearthly desire to get it on with a girl under five-feet tall, I must once again decline."
        u "It would take far too long to remove all of these clothes and I do not want to get dressed again before embarking on my late-night journey to wherever the cold wind takes me."
        s "I can remove them for you. I don’t mind at all."
        u "But then what would poor Io do? She’s still in the room."
        s "..."
        s "Watch?"

        scene utahall8
        with dissolve

        u "You want to get freaky with me while my friend watches?!"
        s "Kind of, yeah."
        u "But what if we both make really weird faces in the heat of the moment and she laughs at us?"
        u "Would you be able to keep it up if that happened?"
        s "I think I’d be a little too distracted by...what else is going on."
        u "If someone ever made fun of me during a time like that, I’d stop like, immediately."
        u "And then it would be really awkward because, like, I’d have to put all of these layers back on while they just laugh."
        u "And so I will never have sex for the rest of forever. It's simply not safe."
        s "..."
        s "You’re going to run out of excuses one day. And when that day comes-"

        scene utahall9
        with dissolve

        u "Yes. When that day comes, I am ready to join the ever-growing list of names in my soon-to-be best selling novel, Sensei’s Secret Sex Journal."
        s "Finally, a book I actually want to read."

        scene utahall8
        with dissolve

        u "Are you really so self-absorbed that you’d read an entire book about yourself? Sensei, you’re better than this."
        s "I’m really not, Uta. You just don’t realize it yet."

        scene utahall9
        with dissolve

        u "Ah. Well then I apologize."
    else:
        u "Ohohoh~ It's starting to sound like {i}somebody{/i} wants to hug."
        s "That person is me. But I think it still might be too soon."

    u "I shall pay closer attention to how much I am supposed to dislike you and will ignore the wonderful chemistry we have begun to form with each other."
    s "I am sorry things had to end like this."
    u "I understand, Sensei. Things {i}needed{/i} to happen this way before they became too serious and one of us wound up with a broken heart."
    u "Probably me because I get attached too easily and would never leave you since I’m so nice."
    s "I’ve changed my mind. I love you."

    scene utahall10
    with dissolve

    u "I remember...when I loved you..."
    u "It feels so long ago now..."
    u "Goodbye...Sensei..."

    scene utahall11
    with dissolve

    "Uta smiles and walks right past me, closing her eyes and sighing to herself as she forever disappears from my life."
    "The days we shared with one another were brief, but they will echo in the back of my mind for as long as I live."

    scene black
    with dissolve

    "I will never forget you, Uta Ushibori."
    "May you find happiness wherever the cold wind takes you."

    $ renpy.end_replay()
    $ utafirsthall = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utahall:
    if utafirsthall == False:
        jump utafirsthall
    else:
        jump utahallgen

label utahallgen:
    if chapthreeactive == True:
        scene utasummer2hallgen
        with dissolve
    else:
        scene utahall1
        with dissolve

    u "Heya! I'm guessing you're here to see me, Sensei?"
    u "Just can't stay away, can ya?"

    "I spend the night hanging out with Uta in the hall."
    "We take a walk around the dorm to kill time and find that there are a number of empty floors directly above us."
    "I wonder why they stuffed my entire class in here but didn't bother filling up any of the other rooms?"
    "Uta seems to find it strange as well, but we shrug it off and then walk back to her floor together."

    scene black
    with dissolve

    "The night ends anticlimactically as Uta decides to head back into her room a little ahead of schedule."
    "She offers to let me join but it seems like her and Io are just going to be watching some TV series they're into."
    "Figuring they could use a little alone time, I reject the offer and decide to just visit her again another night..."

    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta's affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label iofirsthall:
    scene iohall1
    with dissolve

    i "Oh, Sensei. What’s up?"
    i "Not doing anything tonight?"
    s "Nope. Just thought I’d say hi since you’re sitting here on the floor for some reason."
    i "Just getting some fresh air. It’s kind of stuffy in the room at the moment."
    s "I don’t know if I’d call the air in the dorm “fresh” but you do you."
    i "Well, what else am I supposed to do? Go outside? It’s freezing out there."
    i "Let me borrow your jacket and I’ll go outside. You can hang out here and watch movies in my bed or something."
    i "We’ll just swap places for a little bit. Does that work for you?"
    s "I like my jacket and don’t particularly like movies, so no."

    scene iohall2
    with dissolve

    i "What kind of psychopath doesn’t like movies? What could possibly be the reasoning behind that?"
    s "I don’t know. Staying in one place for too long is just boring."
    i "Tell that to the weird bird on top of our vending machine. It hasn't moved since I got here."
    i "I could have sworn it was actually dead but I tried poking it the other day and I’m pretty sure it threatened to kill me."
    s "It didn’t...pull a knife out on you, did it?"

    scene iohall3
    with dissolve

    i "Uhh...no. It’s still just a bird after all. It wouldn’t be able to do something like that."
    s "Oh, Io...You sweet, summer child."
    i "What?...What did I do?"
    s "You will learn the true nature of that animal in time. For now, it may be best if you remain oblivious."

    scene iohall4
    with dissolve

    i "Oh...Uhh, okay."
    i "I still don’t really get it, but you got this really serious look as soon as I brought the bird up, so I’ll listen to you."
    s "Good."
    s "So anyway, how are things going over here? Hate being around the other girls as much as you expected to?"

    scene iohall5
    with dissolve

    i "If you mean the dorms in general and not[school], not really."
    i "I don’t have to talk to anybody over here. "
    i "Even when I’m just sitting in the hall, no one other than Uta really makes an effort to talk to me. So that’s cool."
    s "No, that’s just depressing. I figured they’d at least try."
    i "Ehh. Who knows? Maybe they have and I just haven’t noticed?"
    i "Either way, not really something I want to spend too much time thinking about."
    i "The dorm itself is really cool."
    i "Even though Uta takes up like 75%% of the room, it’s still cool having a place I can sort of turn into my own little thing."
    s "Don’t you have a room at the bathhouse?"
    i "I do, but it’s really just my aunt’s guest room that I wound up moving into and I feel kinda bad about sprucing it up. You know?"
    i "The dorm has a surprisingly small list of rules we need to adhere to, so once I found out I could do whatever I wanted, it made me a lot more comfortable."
    i "Only downside is that the showers here don’t get nearly hot enough so I still have to use the ones at work."

    if bonus == True:
        s "I have yet to use the showers here so I can not contribute to this conversation."
        i "Just get the blonde girl to bring you in there when she takes a shower one day."
        i "You guys already bathe together so I’m sure she won’t mind."
        s "I feel like there is a high likelihood of that actually happening one day, so I’ll let you know when it does."

        scene iohall6
        with dissolve

        i "Uhh...you don’t need to let me know whenever you get naked with some girl. I don’t have to keep tabs on that like Uta does."
        s "Finally, someone who understands."
    else:
        s "Your life is so hard."

    scene iohall7
    with dissolve

    if bonus == True:
        i "Hey, Sensei, do you know why this[school] has dorms in the first place?"
        i "It’s a public [high_school] so like, isn’t having dorms kind of...weird for somewhere like that?"
        i "Not to mention that your class has like, an entire building to itself."
    else:
        i "Also, why does our class get its own building?"

    i "Where even is the other dorm?"
    s "You’re asking me a bunch of questions I do not have the answer to right now."
    i "You didn’t learn all this stuff when you became a teacher?"
    i "Maybe it’s some sort of conspiracy or something?"

    scene iohall8
    with dissolve

    i "Oh man! Great idea!"
    i "Sensei, let’s start a revolution!"
    s "...What?"
    s "What are we revolting against?"

    if bonus == True:
        i "Kumon-mi High. We can secede and declare this dorm a republic. Then we won’t have to go to school {i}at all{/i} and can just hang out here every day."
        s "Yes, I’m sure everyone will love the idea of never going to college and spending the rest of their lives here."

        "Not like anyone is ever going to make it to college anyway."
        "They’re all caught in an infinite first year of [high_school]."
    else:
        i "[kumon_mi_high]. We can secede and declare this dorm a republic. Then we won’t have to go to[school] at all and can just hang out here every day."

    "You know, maybe this does call for a revolution after all?"
    "The dorm functioning as an independent entity sounds quite enticing."

    i "Who even needs college? "
    i "What’s the point of going into debt just so you can try out for a slightly better job in order to pay off all of it?"

    if bonus == True:
        s "That train of thought is too advanced for a girl your age. You need to slow down."

    scene iohall9
    with dissolve

    i "More people should just learn tradeskills."
    i "Sure, a lot of them are less {i}glamorous{/i}, but they’re literally {i}always{/i} needed and there are tons of programs much cheaper than colleges."

    if bonus == True:
        s "Is that what you’re planning on doing?"
        i "Idunno. I should focus on getting out of [high_school] first."
        s "Good call. Leave all that future-planning stuff to year three- a year you will definitely make it to."
        i "Saying it like that makes it sound like I’m going to drop out."
    else:
        s "Why are you in college then?"
        i "Because I'm a hypocrite. Duh."
        s "Oh, right."

    scene iohall7
    with dissolve

    i "I get that I haven’t shown a lot of interest in class yet, but I have no intention of leaving. Especially with you as my teacher."
    s "I had a feeling my methods would reach you."

    scene iohall9
    with dissolve

    i "Well your feeling was spot-on."
    i "It’s cool waking up and not dreading whatever is going to happen for the rest of the day immediately."
    i "It just sucks that I only have several months of that until it all goes away and I have to find my place in yet {i}another{/i} group of students."
    s "Just get held back and stay in my class."

    "Or do nothing at all and achieve the exact same result."

    scene iohall10
    with dissolve

    i "Heheh~ Gonna miss me when I’m gone?"
    i "Maybe I {i}will{/i} get held back and then run for class-rep next year so I can spend even more time with you."
    s "That sounds great as long as you can figure out how to communicate with others as well."
    i "For the last time, I’m actually pretty good at that. I can do it if I want to."
    s "Right. You just don’t {i}want{/i} to."

    scene iohall11
    with dissolve

    i "Precisely. So stop trying to get me to. Got it?"
    s "Yeah, yeah. I won’t make you do anything you don’t want to. "
    i "Good. Only someone horrible would force someone into doing something they’re not comfortable with."

    scene black
    with dissolve

    "Io and I talk for a little while longer before she decides she wants to go back into her room and head to sleep early."
    "Not having anything else to do and feeling a bit guilty about knocking on someone else’s door at this hour of the night, I decide to head home and go to sleep as well."

    if day == 5 or day == 6:
        "I have the day off tomorrow, so maybe I can squeeze in a little extra time in the morning if I’m able to wake up early enough?"

    else:
        "I have to go to work tomorrow, so crashing early will be advantageous in the long run."

    "I make my way down the steps of the dorm and into the cold once more, ready for the harsh winds of yet another winter night."
    "...Or at least that’s what I think until the wind actually hits my skin."
    "From that point on, it’s absolute Hell the whole way back."
    "I wasn't ready at all."

    $ renpy.end_replay()
    $ iofirsthall = True
    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm:
    if io_love >= 5 and bathhouse5 == True and iodorm5 == False:
        jump iodorm5
    if io_love >= 10 and iodorm5 == True and iofirsthall == True and iodorm10 == False:
        jump iodorm10
    if io_love >= 15 and bathhouse10 == True and day != 5 and iodorm15 == False:
        jump iodorm15
    if io_love >= 25 and bathhouse25 == True and day != 5 and iodorm25 == False:
        jump iodorm25
    if io_love >= 35 and bathhouse35p2 == True and day != 5 and day != 2 and iodorm35 == False:
        jump iodorm35
    elif io_love >= 5 and bathhouse5 == False:
        "I should probably get to know Io a little better before I see if she wants to hang out in her room."
        jump doorknock2
    else:
        jump iodormgen

label iodormgen:
    play sound "knock.mp3"

    s "Io, it's me."
    i "Come in, Sensei! Door is open!"

    scene iodormgen
    with fade

    "I walk into Io's room and, just as always, do not hesitate to comment on the condition of the place."
    "She gives me the same excuse as always, that it's really all Uta's fault, but she is undeniably an accomplice to this."
    "I understand the need for a place to do all of her crafts and whatnot, but isn't there somewhere like a woodshop in the[school] she could use?"
    "That would certainly beat trying to build anything in this extremely cramped space."
    "But, then again, she's proven thus far that she's not really the type to willingly spend any spare time somewhere like that."
    "And it's not like the clutter really affects me in any way since I'm not the one living here."
    "But I {i}would{/i} greatly appreciate it if she'd at least clear an area around the bed so I don't need to tap into my athletic capabilities each time I sit on it."

    scene black
    with dissolve

    "Io eventually convinces me to watch a movie with her and, lo and behold, I need to squeeze through the paperthin opening once more."
    "She sits close enough to me that our shoulders touch but makes no effort to go any further."
    "I'm still struggling to understand why she's so comfortable around {i}me{/i} of all people, but I benefit from this- so I will not question it out loud."
    "I'll just let her have her fun and humor her by pretending to watch whatever she puts on."
    "At the end of the day, I {i}did{/i} come here to see her. So letting her do what she wants is fine by me."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io's affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label iohall:
    if iofirsthall == False:
        jump iofirsthall
    else:
        jump iohallgen

label iohallgen:
    if chapthreeactive == True:
        scene iosummer2hallgen
        with dissolve
    else:
        scene iohall10
        with dissolve

    i "Hey, Sensei. What are you up to?"

    "I spend the night in the hallway with Io."
    "It isn't a particularly exciting time, but it's a time nonetheless."

    if bonus == True:
        "We talk more about potential non-college plans for her and I'm, once again, surprised by how much she seems to know about post-[high_school] life."

    scene black
    with dissolve

    "Eventually, it gets late and I decide to head back."
    "Io has some stuff she wants to do tonight anyway, so we mutually part ways and I quickly find myself on the way back home..."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io's affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label utadorm5:
    play sound "knock.mp3"

    "I knock on Uta’s door and wait for her to answer."

    if iodorm5 == False:
        "I haven’t been inside of her room yet, so I’m a little bit curious as to how things are set up in there."
        "Uta seems like the type to either keep things really neat or completely destroy everything in her path, so I’m interested in finding out which of the two is true."

    else:
        "The last time I was in here, it was with Io and..."
        "Well, let’s just say the room wasn’t exactly how I expected it to be."

    u "Ooh! My first visitor!"
    u "Who’s there?"
    u "You're not here to kill me, are you?"
    s "It’s me. Are you free right now?"
    u "Sensei? Yeah, sure! Come on in."
    u "I just cleaned up so you’re all good."

    if iodorm5 == False:
        "Oh, I guess she leans more toward the clean side after all."

    else:
        "Oh, good. I guess Io must have said something about my impression of the dorm when I went in there with her."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I try to push the door open but it gets stuck on something and I need to squeeze my way into the room instead of walking in like a normal human being."

    scene utafirstdorm1
    with dissolve

    s "..."
    s "{i}This{/i} is your idea of clean?"

    if iodorm5 == True:
        "It looks exactly the same as it did when I was in here with Io..."

    scene utafirstdorm2
    with dissolve

    u "Do you mean to tell me your room is cleaner than this, Sensei?"
    s "Yes. I do mean to tell you that."
    u "Wow, that’s actually really surprising. "
    u "I thought you’d be the type to leave things a total wreck."

    if bonus == True:
        u "Like a...naughty magazines and tissues all over the place kind of wreck."
        u "I’m sure you know what I’m talking about."
        s "Yeah, it doesn't exactly take a rocket scientist to figure it out."
        s "I remember when I used to be allowed to buy porn. Those were the good old days."

        "Damn you, Makoto."

        scene utafirstdorm3
        with dissolve

        u "How bad do you need to mess up to be banned from buying that kind of stuff?"
        s "Sometimes, you’re just in the wrong place at the wrong time."
        s "Which, coincidentally, is how I’m feeling in your room right now."
    else:
        s "What a rude assumption. I pride myself in how tidy my room is. And I only get a little help from Ami."

    scene utafirstdorm4
    with dissolve

    u "{i}Ahem...{/i}Are you even allowed in here in the first place, Sensei?"

    if bonus == True:
        u "I am a young, innocent girl and you are an older, stronger man who could take advantage of me at any moment."
        s "Where? I wouldn’t even have any room to do that if I tried."
    else:
        s "Yes. Now, clean."

    scene utafirstdorm5
    with dissolve

    u "At least acknowledge that I only recently moved in and that some of this is just temporary clutter!"
    s "I didn’t mean to insult you. I just figured things might be a little neater since you’re a {i}maid{/i} and all that."

    scene utafirstdorm6
    with dissolve

    u "Uta-chan is off tonight, Sensei. And she wouldn’t want to spend her free time being a maid in her very own room even if she weren’t."

    if bonus == True:
        u "However, if you act now, you can still hire Uta-chan’s exceptional maid services for your very own tissue-filled house."
        u "There is also a special VIP package available where Uta-chan will lay on your bed for two hours so your sheets will smell like her."
        s "And I’m assuming the catch is that I’m not allowed to lay with you?"
        u "Of course not. "
    else:
        u "However, if you act now, you can still hire Uta-chan’s exceptional maid services for your very own house!"
        u "There is also a special VIP package available where Uta-chan will lay on your bed for two hours so your sheets will smell like her."

    s "That just sounds like I’d be paying you to come to my house and take a nap."

    scene utafirstdorm7
    with dissolve

    if bonus == True:
        u "Exactly. But it’s one step closer toward your ultimate goal of getting freaky with Uta-chan so I figured you’d buy-in right away."
        s "Not if I have to pay. I already have Ami to-"
        u "To clean up all of the tissues?"
        s "..."
        s "To clean the entire house so I can continue laying around being useless."
        u "You sound more proud of that than you probably should be."
        s "And you sound a little too confident in the sales pitch for your napping-service."
    else:
        u "Exactly!"
        s "This is a bad deal."

    scene utafirstdorm8
    with dissolve

    u "That aside, do you really think it’s that bad in here? It wouldn’t make me happy if you thought I was lazy and whatnot."
    u "It doesn’t smell weird, too, does it?"
    s "The smell is fine."
    u "Cool cause I just spent way too much money on a bunch of essential oils from some flea market I went to with Io and I really needed to hear that it wasn’t a waste."
    s "It’s just really...unorganized. I guess that's a good word to use here."
    u "Well, we’ve got a lot of stuff and only a little room to put it all in."
    u "Like, how am I supposed to fit two whole wardrobes on my side of the dorm?"
    s "Those are both yours? I thought one was Io’s?"
    u "Nope, both mine."
    s "Then where do her clothes go?"
    u "Beats me. Maybe she’s hiding them all under the bed so no one can see them?"
    s "And why are your clothes all over the floor if you have two wardrobes?"

    scene utafirstdorm9
    with dissolve

    u "Are you only here to hurt me, Sensei?"
    u "After I opened my door {i}and{/i} my heart to you?"

    scene utafirstdorm2
    with dissolve

    u "Hey, wait a second, why did I open my door for you, anyway?"
    u "Isn’t it a little weird for us to be hanging out together like this?"
    u "I know that you’re in love with me and that it’s probably very hard to stay away, but you need to be careful or someone will think something of it."
    s "To be honest, you’ll probably see me around here a lot from now on."
    u "And that’s totally normal?"
    s "Normal for me, at least."
    u "I don’t really get it."
    u "Isn’t there some sort of security-person that should be keeping you away from all of us or can this[school] just not afford something like that?"
    s "I’m pretty sure it’s just more of the[school] not expecting someone like me to actually do something like this."
    u "Yeah, it’s definitely a little weird no matter how you look at it."

    scene utafirstdorm10
    with dissolve

    u "Well, like I said, I understand how hard it must be for you to stay away."
    u "So I will keep these late-night meetings a secret until further notice."
    u "I do have one condition, though."
    u "It's okay to stare at my clothes on the ground but if you start picking them up and sniffing them I will definitely be weirded out. Don’t do that."
    s "I can’t say that’s a thing I was planning on doing."

    scene utafirstdorm11
    with dissolve

    u "Well then okey-dokey, artichokey! We’ve got ourselves a secret!"
    s "Awesome. Not sure if I’d call it a secret, though, since I also hang out with the other girls in their rooms."
    u "Why would you let me set up a cute moment like that only to cut me down right after? Have you no shame, Sensei?"
    s "I really don’t."

    scene black
    with dissolve

    "Uta winks at me, but I’m pretty sure it’s a passive aggressive wink that she decided to break out in response to my sudden “betrayal.”"
    "Either way, it’s cute."
    "She spins around and her skirt flies up in the process, but she’s wearing leggings so I’m unable to catch a glimpse of anything interesting."
    "I follow behind her as she plops onto the bed stomach-first but, just as I’m about to take a seat beside her (Welcome or not), I notice something peculiar."

    scene utafirstdormleonard
    with dissolve

    s "..."
    s "What is this?"
    u "Hm?"
    u "Oh, that?"
    u "Leonard."
    s "A...stag beetle?"
    u "Rhinoceros beetle, technically."
    s "And where did you procure this creature?"
    u "Remember that flea market where I got all those essential oils?"
    s "You bought a rhinoceros beetle at a flea market?"
    u "Oh, no. But I found him on the way back and carried him home in my pocket."
    u "It’s freezing out. Poor little guy would have probably died if it weren’t for me."

    scene utafirstdorm13
    with dissolve

    u "Go on. Tell me how caring and adorable I am for taking in such a delicate lil’ guy."
    s "You picked up a bug off the ground and carried it home."
    u "I like to think I picked up sadness and taught it to smile."
    s "What does that even mean?"

    scene utafirstdorm14
    with dissolve

    u "It means Leonard is my buddy and if I was forced to choose between you and him-"
    u "I’d probably still choose you. But it would take a little bit of thought since he kinda depends on me and you have Ami."
    s "Oh, how’s she doing at the cafe, by the way?"
    u "Ami? She’s doing pretty good. She’s kind of already better in the kitchen than I am. "
    u "But since she’s got those twintails we’d be fools to not take advantage of ‘em."
    u "That hairstyle’s a hot commodity among the few men we actually get."
    s "She’s not actually trying to pull off a tsundere persona, is she?"
    s "She’s joked about that in the past but I’m not sure if it’s actually a thing she was going to follow through with or not."
    u "Oh, not at all. She’s a sweetheart. One of those clumsy types that always {i}almost{/i} trips when she’s carrying a tray but then somehow recovers at the last second."
    s "I’m pretty sure that’s just her being clumsy."
    u "Well, it’s cute. "
    u "She’s still got a bit to learn, though. Like, she’s got the “Master” thing down, but some people like being called other stuff and she’s still not comfortable with that."
    s "Other stuff? What kind of other stuff?"
    u "You know. Like “Prince” or “Oniichan.”"
    s "I don’t like the idea of either of you calling random guys “Oniichan.”"

    scene utafirstdorm15
    with dissolve

    u "Ohohoh~ Are you getting jealous, Oniichan? "
    u "You don’t want Uta-chan and your [niece] spending time with other boys?"
    s "Don’t tease me when I’m just trying to protect you."
    u "Protect us from what, Oniichan? Why do we need your protection?"
    u "You know I have an actual older brother, right? I call him Oniichan, too."
    u "Is he in trouble? "
    u "Are you gonna break into prison and beat him up?"
    s "No, I’m going to-"
    s "Wait, prison? What?"

    scene utafirstdorm16
    with dissolve

    u "He was dumb. Don’t worry about it."
    u "Fact is, though, long as the two of us are working somewhere like that, we’re gonna have to go a little out of our comfort zone."
    u "But who we are in there doesn’t mean anything if it’s not who we are on the outside."
    u "If I call somebody “Oniichan” or “Master” I’m really just trying to get into their pockets."
    s "That’s good to hear but, at the same time, you are really ruining the immersion for me right now."
    u "Never fear, Oniichan. Uta-chan’s off the clock right now and doesn’t mind being in character overtime for you~"
    u "Sure, you might’ve seemed like just another guy the first time you came into the cafe, but you’re more than that now."

    if bonus == True:
        u "You’re a special customer who needs {i}special{/i} service, if you know what I mean."
        s "Under normal pretenses, I feel like I would know that. But every time you say something suggestive, you immediately backpedal."
    else:
        u "Now, you're like...a really cool guy or something."
        s "Cool? You are being extremely suggestive right now, Uta."

    scene utafirstdorm17
    with dissolve

    u "Suggestive?! Sensei- me?! I have no idea what you’re talking about!"

    if bonus == True:
        u "To assume I’d {i}suggest{/i} something in my room while sprawled out on the bed with my little feet dangling in the air, you’re a real rascal!"
        u "Don’t get me wrong, I’m flattered you feel that way about me, but if I wanted to do any more I would have already tossed these clothes into the pile you’re standing on."
        s "Are you sure? Leonard is watching."
        u "He’s gonna have to grow up eventually! Better he learned from his parents than some video on the Internet!"
    else:
        s "Can I become the surrogate father of your rhinoceros beetle? We don't have to do anything."
        u "Sure."

    scene black
    with dissolve2

    "And that, kids, is how I became the adoptive father of a rhinoceros beetle."

    scene theend
    with dissolve2
    hide window
    $ renpy.pause(4, hard=True)

    $ renpy.end_replay()
    $ utadorm5 = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utadorm10:
    play sound "knock.mp3"

    "I knock on Uta’s door and wait for her to answer."
    "Some pop song with noticeably poor audio quality leaks through the door and into the hall, causing me to immediately second-guess my decision to spend time here."

    u "Somebody there? I thought I heard a knock."
    s "It’s me. Turn your music down."
    u "Oh! That’s a great impression of my grandpa, Sensei!"
    u "At least before the cancer spread to his brain and he lost the ability to speak."
    s "..."
    s "Okay, well that’s all the time I have for tonight. See you, Uta."
    u "Whaaaat? No! Come inside! "
    s "After listening to you kill the mood like that, it’s going to take some serious convincing to-"

    if bonus == True:
        u "I’m not wearing any paaaaants~"
    else:
        u "I've got a trampoliiiiiiine~"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I immediately open the door and second guess why I’d ever debated going home in the first place."
    "I mean, Uta is clearly just trying to cope with a horrible tragedy by making light of it and it would be totally wrong of me to abandon her in that state."
    "The poor thing is probably in tears as we-"

    scene utastretch1
    with dissolve

    u "Coolio! That was just as effective as I thought it was gonna be."

    if bonus == False:
        s "Where is the trampoline"

    u "What’s up? You bored?"
    u "Wanna stretch with me?"

    if bonus == True:
        s "Only if I can take off {i}my{/i} pants as well."
        u "Hmm...No thanks. Please leave them on."
        u "I understand that I am an adorable, small girl who you’d love to get down and dirty with, but I {i}really{/i} should be focusing on stretching right now."
        s "Why aren’t you wearing any pants anyway? "
        u "Because I’m {i}stretching{/i}, duh."
        s "Can’t you...do that with pants on?"
        u "I guess, but where’s the fun in that? Why have a dorm if I can’t take my pants off whenever I want?"
        u "You really are old, aren’t ya?"

        "I mean...the first thing I said after knocking was to turn the music down..."
        "Maybe I {i}am{/i} getting old after all?"
    else:
        s "No. Stretching hurts my back. I am frail and dying quickly."

    u "Sensei, I was only kidding. There’s no need to look so down all of a sudden."
    s "Sorry. I just feel like my midlife crisis could kick in at any moment."

    if bonus == True:
        u "Don’t think of that boring ole’ stuff. Just focus on me. But not in a perverted kinda way."
        s "Probably best to put pants on before asking me to make such a dramatic mindset change."

        scene utastretch2
        with dissolve

        u "Nope! Never putting pants on ever again. "
        u "Oh, how wonderful it is to be young."

    scene utastretch3
    with dissolve

    "Uta extends her body as far as it will go, letting out a high-pitched, satisfied squeak in the process before taking a step closer to me."

    u "Stretching complete. Now I’m finally ready for my real mission."

    if bonus == True:
        s "What sort of mission doesn’t require pants?"
        s "Wait. Don’t tell me-"
        u "Don’t tell you what? That I’m finally open for business? Not a chance, Sensei."
        u "Just because I’m pantless and stretchy and telling you I’m ready doesn’t mean I want to get it on."
        s "This is a misunderstanding I really should be forgiven for having."
        u "Forgiveness isn’t necessary at all. If anything, I should be apologizing to you for putting you in such a difficult situation."

        scene utastretch4
        with dissolve

        u "But, then again, you’re the one who sprinted in here the second I announced the no-pants thingy, so I guess you kinda {i}are{/i} a little to blame."

        "The closer Uta gets to me, the harder it is to resist the carnal desire to lift her up and throw her over several piles of clothing and her pet rhinoceros beetle."
        "But, as you can see, there are several things about the scenario that make it slightly less erotic."
        "Besides, it’s kind of fun being the one to actually get teased for once."
        "I spend so much time tapping into the nervousness of some of the other girls that having someone like Uta around to string me along is sort of...weirdly exciting?"
        "Completely unsatisfying and dramatically blue balling as well-"
        "But also exciting."
        "Kind of."
    else:
        s "Is it an assassination mission?"
        u "Yes."
        s "Who are you going to kill?"
        u "I am going to kill loneliness."
        s "Like that one HIM song?"
        u "Exactly like that."

    scene utastretch5
    with dissolve

    u "Hey, question."
    u "I still don’t know a lot of the girls all that well and I know that you do, so like-"
    u "I’m not really sure about how...personal I should be with all of 'em."
    u "My last[school] didn’t have a lot of people in it and the whole dorm-life thing is still new to me, but I don’t wanna be some sorta outcast like Io is going for."
    u "Like, how am I supposed to become friends with everybody?"
    u "Should I just be myself or should I try and hold back a bit?"
    s "I think the location of your pants during this process plays a bigger role than you think it does."

    scene utastretch6
    with dissolve

    u "Girls don’t care if other girls don’t wear pants, Sensei."
    s "That can not possibly be true."

    if bonus == True:
        u "No, no. It really is. We’re not as reserved as you weirdo boys- always too nervous to take off each other's shirts in the locker room and just friggin’...rub each other's bodies from head to toe."
        s "What are you even talking about?"

        scene utastretch7
        with dissolve

        u "Wouldn’t {i}you{/i} like to know?"
        s "I just don’t want you to get the wrong impression of me and think that I’m on some mission to remove the clothing of other males."
        u "And rub their bodies from head to toe."
        s "Yeah, still way off."

        scene utastretch8
        with dissolve

        u "Really? Not even a little bit? "
        u "Where’s all the fun in that?"
    else:
        u "Yo, fuck off and stop trying to convince me that reality is all just some crazy dream, Sensei."
        s "What?"

    s "Uta, this might come as a bit of a shock to you, but I-"

    scene utastretch9
    with dissolve

    u "Ah! Here?! Are you...proposing?!"
    u "Sensei! It’s so sudden! I don’t know what to say!"
    s "In what world would any of this conversation have possibly led up to that?"
    s "Also, why would you not immediately say no if that were the case?"
    u "Is it the case?! Do you really love me that much?!"
    s "My answer to this question is highly dependent on whether or not you’re wearing your maid outfit."

    scene utastretch10
    with dissolve

    u "Damnit, Uta-chan! You were too powerful!"
    u "It only makes sense that this sad, lonely man would fall for you after all of the good times you have shared with him."
    u "And now the {i}real{/i} Uta Ushibori must be the one to carry the cross. To accept the lifelong burden of love!"
    s "Why does it suddenly sound like this is turning into a yes?"

    scene utastretch11
    with dissolve

    u "U-Um...I’m not very good at many things but...if you’ll have me, then..."
    s "What is happening right now?"

    scene utastretch12
    with hpunch

    u "I do!"
    s "..."
    u "..."
    u "Not want to marry you!"
    s "There it is."

    scene utastretch13
    with dissolve

    u "Heheheh~"
    s "Are you really able to blush on command like that? That was impressive."
    u "Oh, no way. I just actually thought about what it would be like to be married to you and my brain made it seem real {i}way{/i} too quick."
    u "We had a dog and a house and everything. "

    scene utastretch14
    with dissolve

    u "Oh, and Io lived in a shed in the backyard. Her rent is due on the 1st every month."

    if iofirsthall == True:
        "I guess the tradeskill thing never worked out for her, huh?"

    s "Weird marriage fantasy aside, I don’t think any of the girls would mind if you just acted like yourself around them."
    u "Oh, right. I forgot that’s what we were talking about. "
    u "You really think that, though? Io says all this stuff about how girls are toxic and like, I guess I’ve kinda seen that in some people at the cafe."
    u "But I like to think everyone is nice overall. At least until something happens to change them."
    s "You’re an optimist and Io is a pessimist. It’s as simple as that."

    scene utastretch15
    with dissolve

    u "An optimist? Isn’t that like, an eye doctor?"
    s "..."

    "Oh, right. "
    "I suddenly remember what Makoto said about Uta’s grades being pretty horrible."

    scene utastretch14
    with dissolve

    u "Oh well. I don’t wanna learn anything when I’m already in comfort-mode."
    u "Sensei, wanna go take a trip to the water station thingy with me?"
    u "I’m super thirsty and don’t have anything to drink until Io gets back from work tonight."
    s "I mean, I’m fine with it but-"

    if bonus == True:
        u "Why are you trying so hard to get my pants back on when all you ever do is try to get them off? Choose a side, Sensei."
    else:
        u "NO BUTS ALLOWED. IT'S WATER TIME."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        "That is...a very good point."
        "The amount of restraint I’ve shown tonight is actually kind of concerning to me."
        "Hell, all it took was a beetle and some clothes to break my train of thought earlier."
        "And now I’m casually walking through the halls of a dorm with a girl who still isn’t wearing any pants."
        "Wait, what?"
    else:
        s "Oh. Uhh...okay?"

    scene utastretch16
    with dissolve

    u "Heheheh~"
    u "I feel like the guy from Shawshank Redemption right now."
    u "Just instead of escaping from jail through the sewers I escaped my dorm room through the sewers of your...mind."
    s "What?"

    scene utastretch17
    with dissolve

    u "I’m being myself! Just like you told me to!"
    u "Thanks, Sensei! It’s been a real eye-opening experience. I hope the other girls also understand your philosophy."

    scene utastretch18

    u "Oh, look! Here come two of them now!"
    s "There is no possible way this can work out in my favor."

    scene utastretch19
    with dissolve

    mo "Wha-"
    t "Legs."
    u "Hey, guys!"

    if bonus == True:
        u "Sensei convinced me that it’s okay to take my pants off. Isn’t that great?"
    else:
        u "Sensei tried to stab me with a fork earlier!"
        s "What"

    scene utastretch20
    with dissolve

    mo "He did what?!"
    mo "Explain yourself, heathen!"

    if bonus == True:
        mo "You dare tread these sacred halls and remove the...sacred kilt off of the...royal maid of...the..."

    scene utastretch21

    mo "GAH! I CAN’T EVEN THINK STRAIGHT!"
    mo "WHAT HAVE YOU DONE WITH HER PANTS?!"
    s "This is going to sound very hard to believe, but all I did was show up."
    u "No, no, Sensei! That’s not true at all!"

    if bonus == True:
        u "You taught me {i}so many things{/i} today."
        mo "SIR! EXPLAIN THE EMPHASIS SHE PLACED ON “SO MANY THINGS.”"
        s "I would love to but this is not the first time she has emphasized the most suggestive part of a sentence before. "
        s "She actually won’t stop and it’s becoming rather difficult to deal with."
    else:
        s "I do not understand what I am supposed to be doing right now."

    t "I am also having difficulty dealing with this situation."

    scene utastretch22
    with dissolve

    u "Hey! Maybe you two should stop wearing pants as well? We could form a little club!"
    u "It would be something us second floor girls could have in common that those {i}losers{/i} downstairs don’t!"
    u "Sensei even volunteered to sponsor the club and be its formal advisor!"
    s "I did no such thing."

    scene utastretch23
    with dissolve

    u "Sensei! Wanna sponsor our no-pants club?"

    if bonus == True:
        s "Absolutely."
        "My libido returns. All I needed was more girls."
        "It hasn’t been growing weaker. It has only been increasing in strength."
    else:
        s "Absolutely not."

    mo "I-I’M ALREADY IN THE MANGA CLUB! I CAN NOT TURN MY BACK ON MY COMRADES!"
    t "I’m in the ramen club."
    s "Is that actually a club we have at[school]?"
    t "I am the only member and the club room is my father’s restaurant."
    s "That’s not a club. That’s just your job."
    t "Fuck you."

    scene utastretch24
    with dissolve

    u "Heheh~ Having floormates is fun!"
    u "I guess it {i}is{/i} fine to be myself after all. "
    u "We don’t need pants to have good time! All we need is-"
    mo "PANTS! OR A SKIRT OR...SOMETHING!"
    mo "THERE COULD BE...GIRLS WHO ARE ALSO INTO GIRLS AND...HAVE A HARD TIME...NOT STARING!"

    scene utastretch25
    with dissolve

    t "Ahh, yes. The Lebanese."
    s "Lesbians, Tsuneyo. Lebanese are people from Lebanon."
    t "An entire country where it is fine to love whoever you want. What a magical place."
    u "You can stare if you want, Molly! Sensei’s been staring all night and I don’t care at all."
    mo "I never said I was talking about myself! The...Kendo Princess here...loves girls! It’s true!"
    t "I don’t think I am Lebanese but my mother comes from Egypt. Is that nearby?"
    s "Kind of? I’m not that familiar with geography from that part of the world."
    t "Then perhaps I am Lebanese after all."

    scene black
    with dissolve2

    "I decide that it might be best for everyone if I just slowly back away while all of their eyes are closed."

    if bonus == True:
        "Part of me wanted to stick around and wait to see if anymore pants/skirts came off but, judging by Molly’s reaction and Tsuneyo’s...inaction, I can’t see that happening."
        "Either way, it was nice seeing Uta finding the courage to strike up a conversation with some of the other girls on her floor."
        "It was also nice seeing her without her pants on."
        "I hope to do more of that in the future."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utadorm10 = True
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utadorm15:
    play sound "knock.mp3"

    "I knock on Uta’s door and wait for her to answer."
    "I have also decided against bringing my wallet with me tonight because, even though this is her room and not the maid cafe, I will be damned if I trust that girl."

    u "Whooooo is it?"
    s "Someone without any money. Let me in."
    u "Sorry, Sensei! Gotta pay the admission price if you wanna hang out with Uta after hours."
    s "I’ve never had to pay before."
    u "Yeah, but now you’re attached. You payin’ or not?"
    s "Joke’s on you. I’ve been attached since the beginning."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Is this open?"
    u "Hey! That’s shoplifting, mister!"

    "I turn the handle and, as expected, the door isn’t locked."
    "Here’s hoping that a police report isn’t filed and that Uta takes it upon herself to frisk me and prevent me from “shoplifting” again in the future."

    scene utafacetime1
    with dissolve

    if bonus == True:
        u "Fine. I’ll let you off the hook this one time. No hidden fees tonight. But don’t expect me to be doin’ anything {i}extra{/i} for ya."
        s "You’re all talk. You wouldn’t have done anything extra even if I brought my wallet with me."
    else:
        u "Okay, okay. Fine. I'm not gonna get the cops involved or anythin' like that because of any outstanding warrants you might have."
        s "Could you take an IOU? I didn't even bring my wallet."

    scene utafacetime2
    with dissolve

    u "Am I really so tempting that you had to start leaving your money at home before coming to say hi?"
    s "Yes. "
    u "That’s really sad, Sensei."
    s "I have a problem, okay?"
    s "Anyway, what are you up to? No Io tonight?"

    scene utafacetime3
    with dissolve

    u "She’s over at the bathhouse doin’ some extra scrubbin’ or something."
    u "I was gonna go with her, but decided to stay home and check in with my parents instead."
    s "Are you telling me I missed an opportunity to formally introduce myself to your parents as your future husband?"

    scene utafacetime4
    with dissolve

    u "I’m sorry, darling. But you know how my parents get when we show off our love for one another while I'm on Facetime."

    if bonus == True:
        s "It’s okay. We can show off our love for one another right now instead. They don’t have to watch."
        u "I’m sorry again, but I’m far too tired to allow that tonight. Even if all I’d have to do is lay there like a dead fish and let you go to town on me."
        s "Man, I can’t wait for the day when you run out of excuses."
    else:
        s "But my love is so pure. I just want to hug."

    scene utafacetime5
    with dissolve

    u "Hope you’re okay with waitin’ a while!"
    u "I’m glad you showed up when ya did, though. If you’d have walked into the room while I was talkin’ to my mom, she would have flipped."
    s "Because I’m a male or because I’m your teacher?"
    u "Both of those things. And also that I’m not wearin’ pants."
    u "Basically, we’d both have a lot of explainin’ to do. And even after, they’d never give you their blessing and we wouldn’t be able to get married."
    u "To think our entire futures could have been destroyed if you came a few seconds earlier."
    s "That’s what she said."
    u "Ooooh, nice one. Ten points to Uta for the glorious set up."
    s "So, now that your parents are out of the way, do I get you all to myself?"
    u "For a little while! I’m still waitin’ on a call from my brother, too. But his hours are all wacky because of prison and stuff."
    s "Wait, yeah. You said something about that before, but I couldn’t tell if it was a joke or not."
    u "Did you think I was joking about my grandpa’s cancer, too? "
    u "What kinda sick sense of humor do you think I have, Sensei?"
    s "I...have no idea."
    s "Why is your brother in jail, though?"

    scene utafacetime6
    with dissolve

    u "Cause he’s an idiot."
    u "And maybe sorta kinda tried to kill somebody."
    s "I’m sorry, what?"
    u "Long story. "
    u "He’ll probably get out in a couple years since the person didn’t actually die, but he’s in pretty hot water right now."
    s "Is there...something I’m not understanding about your family? Because we already have one girl with Yakuza ties and-"

    scene utafacetime7
    with dissolve

    u "Oh, come on. Just because {i}one{/i} Ushibori has attempted murder doesn’t mean we’re {i}all{/i} gonna do it."
    u "My family’s pretty normal apart from him and the long line of debilitating diseases on my mom’s side."
    u "RIP grandpa."
    s "I think you really underestimate how uncomfortable it can be talking to you at times like this."

    scene utafacetime8
    with dissolve

    u "Nothin’ wrong with sayin’ things how they are, Sensei. And it’s not really {i}my{/i} fault if ya get uncomfortable because of it."
    s "I think it’s more of a matter of just not knowing how to respond to certain things you say."
    u "Is somebody forcin’ you to respond? Cause you can always walk away."
    s "But then I’d miss out on precious Uta time."
    u "Not to mention you’ve encountered the rare glasses-pajama Uta. This only happens once a week for a two to three hour period based on the availability of the rest of the Ushiboris."
    s "Well, I hope that the rest of the Ushiboris are not as lively or weird as you."
    u "I think I prefer “bubbly and spunky.”"
    s "And I think I’d prefer not standing across from a beetle while talking to you. Move over."

    if bonus == True:
        u "Okay! But you’ve gotta promise not to touch me or look down my shirt to sneak a peek at my girls."
        u "Or {i}up{/i} my shirt to see my underwear."
        u "Basically, just don’t look at me and everything will be okay."
        s "Impossible. Do you have any idea how cute you are?"
        u "Of course. Why else do you think I started charging people to see me?"
        s "Because you’re actually a demon trapped inside the body of a suspiciously well-endowed freshman."
        u "Blah blah boobies blah blah."
        u "You’re lucky I’m goin’ through my rebellious phase or I wouldn’t let ya on the bed at all."

    scene black
    with dissolve

    "Uta rolls over and drags her laptop to the end of the bed."

    if bonus == True:
        "I immediately attempt to bypass one of her conditions by glancing up her shirt to catch a glimpse of her underwear-"
        "But alas."
        "I fail."
        "I’ll just use my imagination instead and position myself in a way that will allow me to achieve an erection without drawing too much attention to it and making her run away- a thing I’m pretty sure she’d do."

    scene utafacetime9
    with dissolve

    u "Did you see?"

    if bonus == True:
        s "Unfortunately, no."
        u "Really? But I gave you such a good opportunity to."
        s "I will gladly accept a second opportunity if you’re offering."
        u "No can do, Sensei. I only expose my panties once per year and now you have to wait for a whole other trip around the sun to get another shot."
        s "Do you get pleasure out of disappointing me or something?"
        u "Maybe~"
        u "Do you get pleasure out of {i}being{/i} disappointed?"
        s "No. It sucks."
        u "Then why do you keep comin’ to see me if you know I’m all bark and no bite?"
        s "Because all dogs will bite if they’re antagonized enough and your bite sounds incredibly appealing."
    else:
        s "The beetle? Yes."
        u "Cool."

    scene utafacetime10
    with dissolve

    u "You want me to {i}bite{/i} you now?"

    if bonus == True:
        u "I was just using a popular expression, Sensei. But to think you want an innocent little girl like me to push you down and sink her teeth into your private parts is just flat out gross."
        s "First off, I was also using an expression."
        s "Second, why did you immediately assume {i}that{/i} is where I wanted to be bitten? That sounds horrible."
        u "You’re the one who asked for it. All I’m doing is trying to uphold my chastity."
        s "It doesn’t seem like you’re trying very hard based on your no pants policy and seductively unbuttoned, oversized pajama top."
        u "Bein’ comfy ain’t a crime, Sensei. You’re the one who showed up here unannounced."
        u "So unless you think I’m tryin’ to seduce Io or something..."
        s "I like that image. Please continue describing it."
    else:
        s "What? No. Please don't."

    scene utafacetime11
    with dissolve

    u "Why’s your posture gettin’ all weird all of a sudden?"

    if bonus == True:
        s "No reason. Please continue."
    else:
        s "Because I am scared."

    scene utafacetime12
    with dissolve

    if bonus == True:
        u "No thank you, Sensei. If I {i}was{/i} going to seduce Io, I wouldn’t risk ruining the surprise by telling you about it first."
    else:
        u "So, now that we're on the topic of Io."
        s "But we're not on the topic of Io."

    u "You two are close enough to stay in hotel rooms together so, for all I know, you could be wearin’ a wire and feedin’ this all over to her right now."

    if bonus == True:
        s "I give you full permission to search every inch of my body for said wire."
        u "But if I did that, Io would know that I rubbed my hands all over you and suddenly we’d have a big ole love triangle on our hands."

    s "Do you actually hate me or are you just the national grand master of deflection?"

    scene utafacetime13
    with dissolve

    u "It’s nothing personal, Sensei. If I actually thought you were creepy, I wouldn’t hang out with you like this."
    u "I just think the back and forth stuff is really fun and that it wouldn’t be good to jump straight into anything lewd."
    s "And you’re probably right about that. It’s just-"

    if bonus == True:
        u "That I’m such a tease that you can’t help but wanna pick me up and throw me around?"
    else:
        u "You really like need a partner for your professional shuffleboard team?"

    s "Bingo."

    scene utafacetime14
    with dissolve

    if bonus == True:
        u "How about I make you a punch card? "
        u "Six thousand visits to the maid cafe will earn you one kiss. Then six thousand more will let you cop a feel."
        s "These rates are somehow even worse than Nodoka points."

        scene utafacetime15
        with dissolve

        u "Oh! What can we use those for? Because I earned like a thousand during the dorm war sleepover thingy and I don’t know what to do with ‘em."
        s "Collect enough and Nodoka will have sex with you."
        u "Wow."
        s "Thinking of saving up?"
        u "No, I’m just surprised because I watched her give Sana a million of them at the bar and that can really only mean one thing."
        s "I am not even remotely surprised by this."

        scene utafacetime16
        with dissolve

        u "I wonder if she’ll use them."
        s "Sana?"
        u "Mhm. A million should be enough for the grand prize, right?"
        s "I think so...But this is Sana we’re talking about."
        u "So?"
        s "So..."
        s "It’s {i}Sana.{/i}"
        u "Do you think it would be weird if Sana liked girls?"
        s "I think it would be weird if Sana liked {i}anyone.{/i}"

        scene utafacetime17
        with dissolve

        u "You don’t think it would be hot?"
        s "Of course I do. But that doesn’t change how weird it would be."
        u "Hmmmmmmmmmm..."
        s "Why “Hmmmmmmmm?” Why are you being so sketchy about this?"
        u "I’m wearing a wire for Maya and trying to catch you admit that you want to have a threesome with Nodoka and Sana."
        s "Maya, if you are listening right now, this is correct. "
        s "In fact, I welcome any and all threesomes. Bring it on."

        scene utafacetime18
        with dissolve

        u "You’re a really bad boyfriend, Sensei."
        s "Yeah, whatever. Can I have your Nodoka points?"
        u "Can we trade them? Is that allowed?"
        s "I have no idea. "

        scene utafacetime19
        with dissolve

        u "Want me to just kiss her for you?"
        s "I’d much rather redeem this reward on my own."
        s "But, in the event that you do redeem it yourself, I’d greatly appreciate it if I could be there for it."

        scene utafacetime12
        with dissolve

        u "I’m afraid that will be up to Nodoka, Sensei. This is entirely out of my hands."

    "I sigh to myself and attempt to break free of Uta’s incessant teasing loop."

    if bonus == True:
        "I don’t know if it’s her intention to just keep me permanently half-mast but, if it is, she is very much succeeding."

    "A few minutes go by as she scrolls through her phone and I begin to wonder if I’ll have to leave once her brother calls."
    "It’s one thing to stay around and joke with girls while they’re talking to their parents, but..."
    "I’m not sure if I’m brave or...stupid enough to do something like that with a person who has literally attempted murder on the other line."

    s "Uta?"
    u "Yeah?"
    s "What exactly happened with your brother?"
    u "I told you it’s a long story."
    s "Do you not have time?"

    scene utafacetime13
    with dissolve

    u "I have plenty of time. "
    u "It’s just not something I really like talking about."
    s "He didn’t...try to murder {i}you{/i}, did he?"

    scene utafacetime20
    with dissolve

    u "Do you really think I’d be talking to him on the phone if he tried to murder me?"
    s "Good point. "
    s "It’s just my first time talking to someone with a relative in prison, so I can’t help but be a little curious."

    scene utafacetime13
    with dissolve

    u "You’re free to be curious about me or the rest of my family! Mom. Dad. Dead grandpa. You name it."
    u "Let’s save the brother stuff for another time, though. "
    s "I really don’t want to talk about your dead grandpa."
    u "Really? Cause he was a super interesting guy. And a super awesome koto player before his hands stopped working."
    s "Yeah, see, this is why I didn’t want to go down that route."
    s "Just tell me about your parents instead. That sounds easier."

    scene utafacetime21
    with dissolve

    u "You sure you don’t wanna keep flirting with me instead?"

    if bonus == True:
        s "I’m trying a new strategy of getting to know you before getting to the lewd stuff."
        u "Who are you and what have you done with Sensei?"
        s "Oh, okay then. I’ll just go back to trying to make out with you."
    else:
        s "I am offended that you would suggest such a thing when I have been nothing but kind and caring to you."

    scene utafacetime22
    with dissolve

    u "No no no no! It’s fine. I’m just messin’ with ya. I’d be happy to tell you more about my folks."
    u "Just gotta keep in mind that we’re country people and that it’s probably not as interesting of a story as anyone you’d talk to over here."

    scene utafacetime23
    with dissolve

    u "My parents have a pretty huge age gap between ‘em."

    if bonus == True:
        u "Kinda like if you actually started seein’ somebody in our class for real."

    u "They never told me much about how they met or what things were like when they were little, but it seemed to me like they were always pretty happy when I was growin’ up."
    u "And even though we were out in the woods, we weren’t livin’ off the land or anything like that."
    u "Our house was actually kinda big by comparison to a lot of the other ones in the area."
    u "But since they both had full time jobs, my brother and I had to stay at home a lot. And he was the one who watched me most of the time."

    scene utafacetime24
    with dissolve

    u "Then a whole bunch of other stuff happened and I moved here."
    s "Didn't you move here to take care of your grandfather?"
    u "Yup yup! Good ole grandpa Ushibori. "
    s "That isn’t “other stuff.” It's a pretty major detail."
    u "It is!"
    u "But that’s not the only reason I came to Kumon-mi."

    scene utafacetime25
    with dissolve

    u "The “other stuff” meant other stuff."
    u "It was never the intention for me to stay here and finish [high_school]- just like it was never the intention to have me be the only one around when gramps died."
    u "I came because my parents thought it would be good for me to get away for a little while."
    u "And they were already familiar with Io’s aunt from when me and Io would chat online."
    s "What did you have to “get away” from, though?"
    u "That’s the same thing I asked them when they talked about me coming here."
    u "I didn’t like the idea at first. I thought it was hopeless and a waste of time."
    u "But then I thought about how lonely grandpa and Io were...and I decided it would be good to come here and be there for them."
    s "I’m not really sure if I agree with uprooting your entire life for the sake of-"

    "I stop talking mid-sentence, though I’m not sure why."
    "I had a thought-"
    "But the thought disappeared."
    "And it doesn’t return until Uta drags it back by its neck."

    scene utafacetime26
    with dissolve

    u "It didn’t really matter what I wanted. I was going to wind up here one way or another."
    u "Grandpa and Io were just the bright sides I grabbed hold of to help start over. "
    u "Course, I wound up losin’ one of those bright sides to the grim reaper, but now I’ve got a bunch of {i}new{/i} bright sides instead."
    u "I haven’t been here long, but I love Kumon-mi. "
    u "And I love my class. "
    u "And I love yo-"
    s "..."
    u "...gurt."
    s "..."
    s "You love yogurt?"

    scene utafacetime27
    with dissolve

    u "Did you think I was gonna say “you?”"
    s "Did you {i}want{/i} me to think that? Because that’s definitely how it sounded."

    scene utafacetime28
    with dissolve

    u "Sensei! Why are you trying to get me to say I love you when you already have Maya? And Ami? And Ayane? And...everyone else?"

    if bonus == True:
        s "Because {i}you’re{/i} the one I want, Uta."
    else:
        s "Because I feel like you would be the best at hugging."

    scene utafacetime29
    with dissolve

    u "...Huh?"
    s "...?"
    s "I was..."
    s "Were we not doing our back and forth anymore?"

    scene utafacetime30
    with dissolve

    u "Oh!"
    u "Uhh...yeah! "
    u "I just...kinda forgot for a second and...my mind kinda wandered."
    u "Sorry...about that..."
    s "..."
    u "..."

    scene utafacetime31
    with dissolve

    u "..."

    "This is...new."

    u "Soooooo, uhh..."
    u "Yeah. Some more stuff about my parents..."
    u "Let’s see...let’s see..."

    stop music
    scene utafacetime32
    with hpunch
    play sound "phonering.mp3"

    u "Ah! Onii-chan’s jail!"
    u "Perfect timing!"
    s "This timing is horrible. It seemed like you were actually about to fall in love with me or something."

    scene utafacetime33
    with dissolve

    u "I’m sorry, Sensei. But you and I are not meant to be. And even if the red string of fate is wrapped neatly around our fingers, the time will come where we must snap it and-"
    s "Yeah, yeah. Save your rejection for my next hundred confessions."
    s "I’ll leave you and your brother alone."

    scene utafacetime34
    with dissolve
    stop sound fadeout 8.0

    u "Uhh...wait!"
    s "What’s up?"
    u "Do you..."
    u "Um..."

    scene utafacetime35
    with dissolve

    u "Do you think that maybe you could spare some money for his commissary?..."

    scene black
    with dissolve

    s "Goodbye, Uta."
    u "Noooo, wait! How will he be able to afford his ramen without your hard-earned money?"
    s "Use some of the millions of yen I’ve given you."
    u "But that’s mine! I need it for Uta stuff!"
    s "Goodnight, Uta."
    u "Sensei! Come baaaaaaaack!"

    $ renpy.end_replay()
    $ uta_love += 1
    $ utadorm15 = True

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utadorm20:
    play sound "dooropen.mp3"

    u "We’re hooooooome!"

    scene utacomeshome1
    with dissolve

    i "Oh, hey. It’s the only two people in Kumon-mi that I like, inconspicuously showing up at the dorm together just before midnight."
    s "Hey, Io. I’m surprised to see you still awake."

    scene utacomeshome2
    with dissolve

    "Uta tosses her hat and scarf onto an already large pile of clothes on the floor before taking her place next to Io. "

    u "Sensei and I did karaoke together!"
    u "Well, I did karaoke. "
    u "Sensei just stood there all night and watched me because he’s a creep."

    "She conveniently leaves out the part where we almost kissed."

    i "Did you have fun?"
    u "Lots."
    i "You should have invited me. I would have definitely come if it was just you two."
    s "Do you sing as well, Io?"

    scene utacomeshome3
    with dissolve

    i "Nope! I’m horrible. But I could have joined you in being creepy and just staring at Uta as she dances around in circles all night."
    s "What a surprise that you and I are on the same page once again."
    u "Yeah, yeah. Get a room."

    scene utacomeshome4
    with dissolve

    i "Maybe some other time. I actually have to run over to my aunt’s really quick because I just realized I left my phone over there."
    i "Can I trust you to take care of our teacher for the next thirty minutes or so without me?"
    u "I don’t know, Io. He’s always lookin’ at me with this weird fire in his eyes like he’s preparing to devour me whole."
    u "I’d feel a lot safer with your supervision."

    scene utacomeshome5
    with dissolve

    i "Sensei, will you be a good boy and promise to not devour Uta while I’m at my aunt’s house?"
    s "No. She is doomed."

    scene utacomeshome6
    with dissolve

    i "Welp, I’ve done all I can."
    u "Thank you for trying. If you are unable to find my body when you come home, please tell my parents I love them and my brother that he is an idiot."
    i "Will do."

    scene utacomeshome7
    with dissolve

    i "Um...if you’re gone by the time I get back...is it okay if I text you to say goodnight and stuff?"
    s "Sure. It’s already extremely late, so I imagine I'll be gone by then anyway."

    if bonus == True:
        s "I’m pretty sure Uta only invited me here to seduce me. And I doubt that will take long since I’m always staring at her with fire in my eyes or whatever it was she said."

    i "Okay! Yeah! I’ll...get going then!"
    i "See ya!"

    play sound "dooropen.mp3"
    scene utacomeshome8
    with dissolve

    "Io quickly puts her shoes on and darts out of the room, immediately thrusting Uta and I into yet another situation where we’re alone..."
    "Which, I’m pretty sure, is what she was inviting me here to get away from."

    if bonus == True:
        u "She didn’t even react to you saying I was gonna seduce you..."
        s "She either trusts you wholeheartedly or is completely open to the idea of you and I hooking up on your side of the room."

        scene utacomeshome9
        with dissolve

        u "Sorry, Sensei. You know the rule about my parents, and there’s no way I’d be able to call them this late without waking them up and getting them all grumpy."
        s "Then it appears we will have to continue awkwardly flirting with one another and pretending we never-"
        u "Yeah, yeah. A thing happened and now you think you’re a step closer to gettin’ your hands on the goods."

        scene utacomeshome10
        with dissolve

        u "Only problem is that the goods are out of stock and you’ve gotta wait for the store to replenish ‘em."
        s "Would you mind telling me when the next shipment is so I can mark my calendar?"
        u "Sorry, no. We closed for good and aren’t accepting deliveries anymore."
        s "I’m beginning to think your objective tonight was to just make me want you even more than I already do."

        scene utacomeshome11
        with dissolve

        u "I don’t really have objectives. I kinda just do what I do and hope nothing explodes as a result."
        u "I don’t have a problem with you wanting me and stuff, though. "
        u "So if tonight somehow made you want me more for...{i}reasons{/i}...that’s totally okay."

        scene utacomeshome12
        with dissolve

        u "Not that I think you’d be able to help yourself to begin with. I can basically buy a house with all of the money you’ve given me."
        s "Stop taking advantage of my heart. It’s not fair."
    else:
        s "You know, I think it's really unfair that Bojack Horseman was cancelled before everything was completely resolved."

    scene utacomeshome13
    with dissolve

    u "{size=-15}...What do you know about “fair?”{/size}"
    s "Hm? What was that?"

    scene utacomeshome14
    with dissolve

    u "I said...what do you know about chairs!"
    s "...Chairs?"
    u "Yeah! Cause...we should sit...and...since there’s no good place...how about the kotatsu?!"
    s "Do you actually think that was a good cover?"

    scene utacomeshome15
    with dissolve

    u "Don’t know! But I’m not about to wait around and find out! My feet are killin’ me."
    u "So either sit down or get the heck out, mister."

    if bonus == True:
        s "Can we not sit on the bed instead?"
        u "After what happened earlier? Heck no we can’t. I ain’t trying to lose my virginity in the thirty minute window of Io going to get her phone."
        u "What if she calls one of us right before it goes in and I get surprised and jump and then it splits me in half and there’s blood everywhere?"
        u "Does that sound fun to you?"
        s "I mean...up until the “blood everywhere” part..."

        scene utacomeshome16
        with dissolve

        u "Just sit down, you friggin’ horndog..."
    else:
        s "I understand. The last thing I would ever want is for you to feel physical pain. I will now sit down."

    scene black
    with dissolve

    "I take my shoes off and sit in the same spot where Io passed out on my lap the other day."
    "Uta does the same after grabbing a carton of strawberry milk out of Io’s mini fridge and, within a matter of seconds, things start going back to normal."

    scene utacomeshome17
    with dissolve

    "I guess “normal” is a pretty subjective term when it comes to my relationship with Uta, though, as I’m learning now that it hasn’t even really begun yet."
    "There’s clearly a lot that I don’t yet understand about her, and I feel like it wouldn’t be too much of a stretch to imagine that there’s a lot she doesn’t understand about herself yet either."
    "Granted, I could be completely wrong considering when I confronted her about her selflessness, she immediately refuted it."
    "Either way, the uncomfortable air blends in with the typical wood stain scented air of her dorm room and things, once again, move into an area of conversation we’re both more comfortable with."

    u "Io’s great, isn’t she?"

    "That area being talking about others instead of talking about ourselves."

    s "She said the same thing about you the other day."

    scene utacomeshome18
    with dissolve

    u "Oooooh...what else did she say? Anything juicy?"
    u "I’ve always been curious about what she says about me while I’m not around."
    u "Only issue is that she never talks to anybody, so this is the first chance I’ve had to find out."
    s "She said a few things. But the one that stuck out most to me is that you “got better.”"
    s "Whatever that means."

    scene utacomeshome19
    with dissolve

    u "...Oh."
    s "Should we deflect this conversation topic as well?"
    u "Yeah. My brain’s already overloaded from almost locking lips with you earlier and I’d rather not get into what that means right now."

    scene utacomeshome20
    with dissolve

    u "We can keep talking about Io, though! Just nothing bad, because she’s my BFF and I don’t wanna say mean stuff about her behind her back."
    s "Fine. But I’m going to let you lead the conversation since you’re the one who’s done nothing but show opposition to pretty much everything since we stepped into the karaoke booth."

    scene utacomeshome21
    with dissolve

    u "Done deal! Trust in Uta and you shall receive the best darn conversation you’ve had all night!"
    s "The competition is very weak, all things considered."
    u "Shush."
    u "So..."
    u "She hasn’t told me about it, but...based on the way she acted around you tonight, I bet that..."
    u "She told you she likes you."
    s "Perceptive."

    scene utacomeshome22
    with dissolve

    u "Did she give you the robot or did she chicken out? I think that one could have gone either way."
    s "The robot is now living on a table in my bedroom."
    u "Awwwwww, that’s so cute."
    u "She likes you a lot, you know. Which means you’re the first crush she’s ever had."
    u "Which means she’ll take it a bajillion times harder if you do anything to make her sad."
    s "Like kissing her best friend?"

    scene utacomeshome23
    with dissolve

    u "Guh. Well, at least we lasted a solid two minutes without bringin’ it up. But yes, like kissing her best friend."
    s "To move away from Io territory for a second...what about you, Uta?"

    scene utacomeshome24
    with dissolve

    u "Hm? What {i}about{/i} me?"
    s "Who was your first crush?"

    scene utacomeshome25
    with dissolve

    u "Hmm...good question. Who {i}was{/i} my first crush?..."
    u "..."
    s "..."
    u "..."
    s "..."
    u "Maybe Spongebob?"
    s "..."
    u "..."
    s "What?"

    scene utacomeshome24
    with dissolve

    u "You know. The cartoon sponge. Hangs out with a starfish."
    s "Your first crush was on a cartoon sponge?"
    u "Sure. He was cute."
    u "I never wanted to do him or anything cause I was just a little girl, but I used to talk about marryin’ him and stuff."
    s "You have come a very long way, Uta."

    scene utacomeshome26
    with dissolve

    u "I’ve had all kinds of crushes before."
    u "Cartoons. Boys. Girls."
    u "I even had a crush on Io for a little while."
    s "Excuse me?"
    u "Yup. You heard that right."
    s "Does...she know that?"

    scene utacomeshome27
    with dissolve

    u "No. And she’s never gonna find out because, if you tell her, you’ll never see another flavor beam for the rest of your life."
    s "Do you still feel that way?"
    u "Sensei, I mean it. Don’t even think about it."
    s "I’m not going to tell her. I’m just genuinely curious."

    scene utacomeshome28
    with dissolve

    u "No. I don’t feel that way anymore."
    u "It was only for a little while anyway. Like, barely even a couple weeks."
    u "I’ve just always had a hard time wrangling up my feelings and, before I know it, I wind up getting attached to stuff I don’t even have."
    u "It’s kinda pathetic, actually. And it’s made me do some really stupid stuff in the past."

    scene utacomeshome29
    with dissolve

    u "Buuuuuut that’s gettin’ a little too close to the “Uta doesn’t wanna talk about it right now” zone and I think it might be time for another topic change."
    s "What kind of stupid stuff?"

    scene utacomeshome24
    with dissolve

    if bonus == True:
        u "Sensei, I know you may be in love with me, but you really need to start payin’ attention to what I say and not just my boobs."
    else:
        u "Sensei, I know you may be in love with me, but you really need to start payin’ attention to what I say and not just my cute lil' face."

    s "I heard what you said, I’m just choosing to ignore it because I’m curious."
    u "Well that’s just plain rude and you’re a big ole jerk for doing that."
    s "Will you tell me eventually?"

    scene utacomeshome28
    with dissolve

    u "Yes. Whether I want to or not."
    u "It’ll slip out because, contrary to what Io may have said about me, I’m not “better.”"
    u "I just don’t say the same kinda stuff she says about herself because my brain is stupid and makes me think that anything that’s said out loud is real."
    s "So all of those smiles of yours are fake?"

    scene utacomeshome30
    with dissolve

    u "Course not. Just cause you’ve gone through some stuff in the past and can’t really get over it doesn’t mean that everything for the rest of forever is gonna be sad."
    u "I’m super happy now. And I’ve got a bajillion good things going for me."
    u "There’s just also some stuff I’ve gotta bury if I’m ever gonna move on."
    u "So maybe that does make me “better” if that’s the word Io is gonna use. But it’s not the one I would pick."
    u "Now, can we stop talkin’ about depressing stuff and go back to flirting? Even the whole near kiss thing was better than this."
    u "Also, you made me admit I had a crush on a sponge and now I’m mad at you."
    s "Can I tell Io about the sponge crush or is that off limits too?"
    u "Io knows about the sponge crush."
    s "And she still talks to you?"

    scene utacomeshome31
    with dissolve

    u "Are you gonna stop talking to me because I had a crush on a sponge?!"
    s "I can probably be convinced to keep associating with you."

    if bonus == True:
        u "Ah! I knew you’d break out the blackmail sooner or later! It was only a matter of time!"
        u "What do you want?! My first kiss? My first handie? My first child?"
        u "Tell me, Sensei! What must you take from me?!"
    else:
        u "What do you want?! Money?! A sandwich?!"

    s "Your phone number will suffice."

    scene utacomeshome24
    with dissolve

    u "Oh."
    u "That’s it?"

    if bonus == True:
        s "I’d also accept any of the three things you listed prior to my suggestion."
        u "No way. Not now that I know how easy it is to win you over."
        s "I forgot to add that I’ll also accept any sexy pictures you’d be willing to send me as a package deal with your phone number."
    else:
        s "I forgot to add that I’ll also accept any pictures of cats you'd be willing to send to me."

    scene utacomeshome32
    with dissolve

    u "That’s...not really something I can do..."
    s "That’s fine. I wasn’t trying to push-"
    u "No, like, I literally {i}can’t{/i} do that. There are parental locks on my phone and I can’t send picture messages."

    if bonus == True:
        s "..."
    else:
        s "Damn. A cat detection filter. How unfortunate."

    "I’m going to have to add somebody else onto my phone plan, aren’t I?"

    u "..."
    s "Just the number is fine, Uta."

    scene utacomeshome33
    with dissolve

    u "Done! Hand it over, Sensei."
    u "And get ready to be tossed into a group chat with me and Io so we all know what each other are doing every second of every day!"

    if bonus == True:
        s "I can guarantee that you do not want to know what I am doing for many seconds of many of those days."
    else:
        s "Okay, but please ignore all of the pictures of my accountant."

    u "..."
    s "..."
    u "How come you’ve always gotta ruin everything?"

    scene black
    with dissolve2

    "Uta gives me her phone number, which means I have now conquered the seventh dorm room."
    "And even though she is literally incapable of sending me picture messages, I’m glad to see that we’re at least {i}progressing{/i} in some way."
    "Or regressing, if her attitude toward what happened in the karaoke booth doesn’t change any time soon."
    "I’m not worried about that now, though."
    "I’ve learned a lot more about her today than any day before."
    "And even if there are parts of her that I won’t understand for months or years to come-"
    "I’m sure those months will be exciting."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utadorm20 = True
    $ utanumber = True
    stop music fadeout 7.0

    "{i}Congratulations! You now have Uta’s phone number!{/i}"
    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm5:
    play sound "knock.mp3"

    "I knock on Io’s door and wait for her to answer."

    if utadorm5 == True:
        "It won’t be my first time being in there since I’ve already come to visit Uta before but..."
        "Well, I guess it will be interesting hearing Io’s take on the, uhh, {i}condition{/i} of the room."

    else:
        "I’ve yet to spend any time in there since she and Uta moved in and I’m really curious about what they’ve done with the place."
        "If I’m remembering correctly, it’s the first time either of them have lived in a dorm, so I’m sure they’ve put their own personal touches on it in some way already."

    s "..."

    "No one answers."
    "I guess I could have expected as much since this is Io we’re talking about and Uta would have just walked in..."
    "But I guess there’s always the possibility that she just isn’t at home right now."
    "Maybe I should call out to her so she knows I’m not some big, bad girl who’s come to...girl-up the place or something."

    play sound "knock.mp3"

    s "Io, it’s me. Are you around right now?"
    i "Oh, shoot."
    i "Yeah! Come in, Sensei. I thought you were somebody else."

    "Figures."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if utadorm5 == False:
        "I push the door open and notice a massive amount of clutter before it even opens all the way."

    else:
        "I push the door open to find that it’s in exactly the same state as it was the first time I came here."

    "I ask myself if it’s really fulfilling to live this way-"
    "But then I remember that it isn’t fulfilling to live at all and decide to move past it."

    scene iofirstdorm1
    with dissolve

    i "Hey."
    i "Come to give me a housewarming present or something?"
    s "Will you accept my presence as the...present?"
    i "Idunno. Can you do anything cool?"
    s "I made french toast this one time. That’s pretty cool, right?"
    i "It’s...normal."
    i "If you’re not bringing me a housewarming gift, what are you doing over here?"
    s "Just here to see you, I guess. Figured you might be bored or something."

    scene iofirstdorm2
    with dissolve

    i "We’re allowed to hang out in my room? "
    s "Probably not but that’s never stopped me before."
    i "Wow. You really do run a strange operation, huh?"
    s "I’m either the best or the worst teacher in the world depending on how you look at things."

    scene iofirstdorm3
    with dissolve

    i "Sorry the place is such a mess but, in my defense, most of this is on Uta."
    i "I’m just kinda stashing all of my stuff from my aunt’s house here so I can fool around in my spare time."
    i "And I’m pretty sure Uta is stashing every single item she’s ever laid her hands on. Pretty different approach if you ask me."

    scene iofirstdorm4
    with dissolve

    i "But hey, as long as you’re not uncomfortable surrounded by all this junk, I’m more than happy to have you."
    i "Can’t even remember the last time I hung out with anyone who wasn’t a part-time maid."
    s "I’m sure I’ll be coming here pretty regularly, so it's best you get used to it. "
    s "There is one thing that’s bothering me, though."
    i "Is it the cat on top of the wardrobe?"
    s "It is."
    i "You’re not allergic, are you?"
    s "I’m not. But I don’t particularly like animals."
    i "Ah. Well he’s dead anyway so you don’t have to really worry about either of those things."
    i "Or at least I don’t think you do? I’m not sure how taxidermied animals work for people with allergies."
    s "So that was {i}your{/i} cat and not Uta's, I’m guessing?"

    scene iofirstdorm5
    with dissolve

    i "Sir Meowington the Fourth."
    s "What happened to the first three?"
    i "The same thing that happened to the fourth. They died."
    s "You know, I was expecting a little more information there. But your simplistic way of looking at things has saved us a potentially awkward conversation."

    scene iofirstdorm6
    with dissolve

    i "You’re welcome."
    i "No sense in going into detail about stuff that’s just gonna bring you down, you know?"
    i "Gotta focus on the good stuff."
    s "Pretty positive outlook today, Io."
    i "Right?"
    i "Guess I’m in a good mood since my favorite teacher came to visit me."
    s "That’s quite flattering but I’m also your {i}only{/i} teacher, so..."
    i "Yeah but you’d still be my favorite even if I had other ones cause you won’t call on me to answer questions and stuff."
    s "I’d need to give out questions in order to do that in the first place, so yeah. You don’t have to worry about that."

    scene black
    with dissolve

    "Io moves a few steps to the side and takes a seat on an old-looking computer chair."
    "She also grabs a boxcutter off of her desk and begins to twirl it around with her fingers."

    scene iofirstdorm7
    with dissolve

    i "So, now what? Wanna play a game or something?"
    s "Saying that while twirling a boxcutter doesn’t exactly make me want to play anything you might be into."
    i "Oh, this thing? It’s kinda dull. You don’t have to worry about it."
    s "It looks incredibly sharp."
    i "Scared of sharp stuff, Sensei?"
    s "I want to throw it out there that that is a perfectly reasonable thing to be afraid of."

    scene iofirstdorm8
    with dissolve

    i "Relax. It’s just a tool. I’ve got tons of stuff way more dangerous than this lying around the room."

    scene iofirstdorm9
    with dissolve

    i "As long as you watch your step and make sure the area is clear before you sit down, you’re totally safe."
    i "I stepped on a nail once at my aunt’s place and you wouldn’t believe how-"
    s "Whatever you think I wouldn’t believe, I can probably assure you I would."
    i "What, I can’t even tell my nail story?"
    s "You can not."
    s "Instead, why not tell me more about this infatuation with tools? Like, why a boxcutter?"

    scene iofirstdorm10
    with dissolve

    i "We talked about my hobbies for like two hours at the bathhouse the other day. I like making things, remember?"
    i "The boxcutter is just for cutting boxes, though."

    scene iofirstdorm9
    with dissolve

    i "Unless you make me mad. Then it will be for cutting Senseis."
    s "..."

    scene iofirstdorm11
    with dissolve

    i "Um...That was a joke. "
    i "I wouldn’t actually hurt you, you know."
    i "I’m surprisingly non-confrontational for someone always talking down on other people."
    i "I’d probably just stop talking to you or...punch the wall or something if you ever made me that mad. "
    s "Can you at least put the boxcutter down, Io?"

    scene iofirstdorm12
    with dissolve

    i "No. I need something to fidget with or I'll start getting uncomfortable."
    i "Its the first time I've ever had a boy in my room. Please don't hold my discomfort against me."

    "Io begins quickly sliding the blade up and down with the little knob thing on the handle."
    "I’m sure there’s a special name for it but I have no idea what it's called so you’re going to have to deal with “knob thing” until I find out."

    scene iofirstdorm13
    with dissolve

    i "So, Sensei, is there anything you want me to try making you? "
    i "I just finished that second wardrobe a little while ago and I’m kinda out of big projects for now."
    s "Second wardrobe? Like, the one in this room?"
    i "Obviously. What other wardrobe would I be talking about?"
    s "You made those? They look professional."
    i "The one on the right has one leg that’s a little shorter than the others so it would never actually be able to ship or anything, but thanks."
    i "It’s really nice making stuff like that- stuff that can be used immediately."
    i "Sometimes, you’ll go out of your way to make something for somebody and they’ll act like they love it, but never actually use or find a use for it."
    i "It really sucks when stuff like that happens."

    scene iofirstdorm14
    with dissolve

    i "So I only make things that I know other people need or that I can use myself now."
    s "Well, the second I need a carpenter, I know who to come to."

    scene iofirstdorm13
    with dissolve

    i "Heheh~ Part carpenter, part floor scrubber. "
    i "Not exactly a glamorous life I’m leading, is it?"
    s "No, but it fits you."
    i "I know that's probably supposed to be a compliment but it makes me feel kind of gross."
    s "I just mean that I admire how you do the things you want to do without letting societal norms get in your way."
    i "I think it’s closer to me just avoiding ever figuring out what those societal norms are, but yeah. I’m gonna do what I want to do."

    scene iofirstdorm15
    with dissolve

    i "Which is why I’m more than happy to take up your time when there are plenty of other girls hoping you’ll knock on {i}their{/i} doors instead of mine."
    i "I win, even if it’s only for tonight."

    scene iofirstdorm14
    with dissolve

    i "So, if there’s anything I can make to show you that I’m worth your time, feel free to let me know."
    i "If not, I’ll probably just wind up making a third wardrobe and the room will look like even more of a trainwreck."
    i "It {i}would{/i} be nice having somewhere to put {i}my{/i} clothes, though."

    "Something Io said jumped out at me there."
    "“To show you that I’m worth your time,” is a phrase that, when isolated, looks remarkably self-deprecating."
    "And when paired with her tendencies to call herself trash or whatever it is she’s spouted before, it makes sense."
    "But the issue with dissecting small parts of dialogue like that and using them to assign attributes to people is that sometimes people deviate."
    "Maybe her offer to create something for me is less self-deprecation and more just the desire to please?"
    "I should ask her."

    s "Do you really think you’re not worth my time?"

    scene iofirstdorm16
    with dissolve

    i "Hm? What do you mean?"
    s "You offered to make me something to show me that you're worth it. What did you mean by that?"
    i "Hey. Speaking unfiltered thoughts is my job. You’re supposed to be the sponge."
    s "Sometimes, you’ve gotta wring the sponge out to make room for more liquid."
    i "This is a really weird analogy. I’m getting uncomfortable."
    s "Yeah, that sounded better in my head."
    s "I’m just trying to figure out more about you in the least intrusive way possible, I guess."

    scene iofirstdorm17
    with dissolve

    i "That’s a good strategy. "
    i "To clarify, I {i}can’t{/i} exactly think I’m not worth your time because I don’t quite know what your time is worth."
    i "But Henry David Thoreau once said-"

    scene iofirstdorm18
    with dissolve

    i "{i}Be not simply good; be good for something.{/i}"
    i "And so it’s important that we all make some sort of impact in the lives of others."
    i "If I can create something that changes your life, or even your daily ritual, I will be able to make a difference...albeit a relatively minuscule one."
    i "I’ll move one step closer to “good for something” rather than just a slowly dying flesh-compound who spends her nights picking splinters out of her fingertips."

    scene iofirstdorm19
    with dissolve

    i "You feel me?"
    s "I feel like I understand you less and more at the same time."
    i "Heheh~ Let me show you something else and probably confuse you even more, then."

    scene black
    with dissolve

    "Io gets off the chair and walks over to a small shelf full of miscellaneous objects near the door."
    "She moves aside a few books, knocking what sounds like loose change onto the floor, before returning and brandishing a strange looking figure before me."

    scene iofirstdorm20
    with dissolve2

    i "Did you have any toys you played with as a kid, Sensei?"
    i "Do you even remember things from back then?"
    s "..."
    i "You don’t, do you?"
    i "You know, many popular psychologists say that memory loss can be the result of repeated trauma."
    i "Of course, this isn’t me insinuating that that's what’s going on for you, but it {i}is{/i} a thing that happens."
    i "Without getting more off the rails, the point I’m trying to land at is that the first few years of your life are irrefutably the most important."
    i "A lot of kids these days would look at something like this little guy and think, “What am I supposed to do with it?”"
    i "“How can I have fun with this?”"

    scene iofirstdorm21
    with dissolve

    i "But then, there are a handful of kids without anything."
    i "A handful of kids who would take something like this in their tiny, little hands and give it a name."
    i "Give it value."
    s "Were you one of those k-"
    i "I’m one of them now, Sensei."

    scene iofirstdorm20
    with dissolve

    i "This isn’t something I leaned on when I was growing up or anything like that."
    i "It’s something I {i}made{/i}. "
    i "Something that {i}could{/i} be that much-needed solace for someone in dire straits."
    i "But instead of being in anyone else’s hands, it’s collecting dust on a shelf in my room alongside several others just like it."
    s "Why, though?"
    s "Why not give it away if you think it can help someone?"
    i "Why?"

    scene iofirstdorm22
    with dissolve

    i "Because I’m all talk."
    i "Because it’s easy for me to start things but near impossible for me to finish them."

    scene iofirstdorm23
    with dissolve

    i "I’m bad at seeing things through to the end."
    i "I couldn’t even finish my introduction in class the right way."
    i "And yeah, I’m still impressionable...but the only impressions I’ve gotten the last few years are that I need to hurry up and find my place in the world."

    scene iofirstdorm24
    with dissolve

    i "Who knows?"
    i "Maybe I'm just struggling to give this little guy away because he reminds me of myself?"
    i "Collecting dust somewhere and too empty to actually make anyone happy."
    i "The only difference is that {i}I{/i} actually have a name. "
    s "And that he’s made out of wood."

    scene iofirstdorm25
    with dissolve

    i "Heh...Yeah. I guess there’s more than just one key difference if you want to state the obvious."
    i "I’m a lot taller than him too. And a little better at talking to people."
    s "Jokes aside, if you need something or someone to lean on, I’m sure both Uta and myself would be viable candidates."
    s "I also wouldn’t mind helping you find a use for your apparent collection of unnamed wooden robots."
    i "I’ve got the numbers for two nearby orphanages saved in my phone if you want them."
    i "I figured I could donate a lot of the stuff I make to charities but then I look at it all and second-guess myself."
    i "Funny, huh? "
    i "I went as far as mentioning that things like this could save lives or whatever but I don’t even believe it myself."
    i "They’re just...wooden blocks at the end of the day."
    s "You prepared {i}that{/i} much and still didn’t finish the job? Just donate them, Io."

    scene iofirstdorm26
    with dissolve

    i "I’ve got a problem, okay? "
    i "I want to make a difference but I’m too scared to actually do it. "
    s "Well, at least you understand your fatal flaw. That’s more than most people can say."

    scene iofirstdorm27
    with dissolve

    i "..."
    i "Fatal flaw, huh?"
    i "If only it were just one."

    scene black
    with dissolve2

    "Io shows me a few other toys she’s made for the purpose of making other people happy and I’m extremely impressed by the level of detail in some of them."
    "She's right about one thing, at the very least."
    "Objects like this aren’t really appreciated by kids anymore."
    "Which is extremely depressing given how much thought I know Io has put into making them."
    "But they serve no purpose collecting dust in an overly-cluttered dorm room."
    "They’d be better anywhere else-"
    "Just like many of us."
    "The only issue is getting them there."
    "..."
    "Io starts dozing off an hour or two later and I decide to leave and let her get her rest."
    "She thanks me a bunch of times for “putting up with her” and, once again, displays another weakness of hers."
    "I think I’m beginning to understand just how many of those there may be."
    "At the same time, though, it’s admirable how much effort she’s putting into living up to her ideals."
    "It’s rare to find someone so strong and weak at the same time."
    "I just hope that both extremes wind up cancelling each other out so that she, one day, finds a trace of normalcy in this shithole we call life."

    $ renpy.end_replay()
    $ io_love += 1
    $ iodorm5 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm10:
    play sound "knock.mp3"
    stop music fadeout 20.0

    "I knock on Io’s door and wait for her to answer."
    "I’m sure I’ll need to knock again or announce my presence at some point to circumnavigate her antisocial tendencies but-"
    "I see no harm in testing the waters each time I arrive."
    "It’s only a matter of time until that shell of hers crumbles and she winds up greeting anyone who knocks."
    "If anyone knocks."
    "There’s no reason anyone would want to at this point, is there?"
    "No one but me, that is."

    if bonus == True:
        "And it’s not like it’s flattering receiving a visit from me given that my end goal with all of these girls is exactly the same."
        "To sneak inside of them- in more ways than one."
        "Into their minds. Into their hearts."
        "Into their sheets. "
        "Their pants."
        "Their bodies. "
        "And to leave minimal trace behind so my efforts aren’t thwarted somewhere along the line I’m actively trying to erase."
        "If you think that’s so horrible-"
        "Then just look away."
        "It’s that easy."
    else:
        "And it’s not like it’s flattering receiving a visit from me when all I'm really interested in is hugging and Hot Pockets."

    s "..."

    play sound "knock.mp3"

    s "Io, it’s me."
    i "{i}Hah...{/i}"
    i "Say that after the first knock from now on."
    i "Come on in, Sensei."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I probably {i}should{/i} just say I’m here after the first knock, shouldn’t I?"
    "If my goal is so impure, is the pause to see if she’s grown as a person really all that necessary?"
    "Time is precious."
    "Or at least it used to be."
    "But I could still save so much of it by giving up on her."

    scene iodormten1
    with dissolve
    play music "io.mp3"

    i "Welcome back. "

    "So why won't I do that?"

    s "Hey. Any plans for tonight?"
    i "Not until now. "
    i "Was thinking about taking a trip to the convenience store but my shoes are still soaking wet from walking home in the snow."
    s "You only have one pair?"
    i "I only need one pair."
    s "Clearly not if shoes are currently your only barrier from fulfilling your nightly goal."

    scene iodormten2
    with dissolve

    i "Okay, sorry. I {i}usually{/i} only need one pair."
    i "But it’s not like the inability to go on a little walk is something that’s going to ruin my life."

    scene iodormten3
    with dissolve

    i "Especially now that you’re here."
    i "You’re a little bit more fun than a trek through frozen rain. "
    i "Just a little, though."
    s "Thanks. I also like you more than I like snow, if that means anything to you."
    i "It does."
    i "I have a tendency to think everyone likes everything more than me by default until proven otherwise."
    s "Well I’m not really in the mood to list all of the things you’re better than, so we should probably just change the topic now."

    scene iodormten2
    with dissolve

    i "Hahah...Probably."

    scene iodormten4
    with dissolve

    i "So, what do you want to do?"
    i "You came all the way here with just your regular blazer on. Aren’t you cold?"
    i "I’d offer you a jacket or something but I’m pretty sure that nothing I have would fit you."
    i "We can get under the kotatsu if you want?"
    i "It doesn’t turn on since I’m still trying to fix it, but it’s got a blanket and blankets are cool."
    i "Well, warm. They’re not cool at all. You know what I mean."
    s "There’s the bed, too. "
    i "Yes. There’s the bed, too. "
    i "If you can reach it, that is."
    i "You’re gonna have to climb over some stuff to get there so I figured a spot on the floor might be easier for you."
    s "Are you doubting my agility, Io Ichimonji?"

    scene iodormten5
    with dissolve

    i "Woah. Breaking out my last name? You must be really serious right now."

    if bonus == True:
        s "Never underestimate my willpower to get into bed with a cute girl."
    else:
        s "Nah. Just trying to look cool around a cute girl since I get nervous really easily and am very shy."

    scene iodormten6
    with dissolve

    i "Ooooh I’ve moved from “bathhouse attendant” to “cute girl” in your book. What a momentous occasion. "
    s "You’ve held both titles since I met you."
    i "{i}I’m flattered you feel that way, Sensei, but I’m sure it’s just your craving for body heat that is causing you to say such things.{/i}"
    i "{i}So I’m sorry but I must reject you. I hope we can stay friends, though.{/i}"
    s "And with that, you’ve earned the title of “Uta impressionist” as well."

    scene iodormten7
    with dissolve

    i "Nihihi~ Pretty good, right? I spend so much time with her that it’s basically second nature at this point."

    scene iodormten8
    with dissolve

    i "Come on. We can sit on the bed."
    i "As long as you can get to it, I mean~"

    scene black
    with dissolve

    "Io manages to slip between a table and a minifridge without bumping into either of them and hops onto her mattress."
    "I am slightly less successful but still manage to make it through without breaking anything, so this is a victory in my book."
    "........."
    "......"
    "..."

    scene iodormten9
    with dissolve

    i "Congratulations on passing through the barrier."
    s "I’m impressed you were able to make it through without even touching anything."
    i "I’m like five feet tall and paperthin. Plus I’ve done it a bunch of times before."
    i "Muscle memory really helps out with small things like that."
    i "Also, it’s not weird if I sit this close to you, is it?"
    i "You’re not getting nervous, are you?"
    s "Not at all."
    s "Are you?"
    i "Not at all."
    i "I'm just chilling."
    i "Wanna watch a movie or something? I’ve got a bunch."
    s "I already told you I’m not into movies."
    i "Yeah, but I’m obviously gonna try to change your mind when they’re another big hobby of mine. "
    s "You have too many hobbies."
    i "You don’t have enough hobbies. "
    i "Take something up so we can have a reason to hang out more."
    s "I was unaware that we needed a reason to hang out more."
    i "Less of a reason and more of an excuse so that no one will start thinking anything is going on between us."
    i "If we’re both in like...the golf club or something, nobody will think we’re up to anything if we hang out somewhere after[school]."

    if bonus == True:
        s "At this point, I think it’s pretty safe to assume that anyone and everyone thinks I’m up to something at any given point."
        s "Being around me probably just opens you up to more pressure like that."
    else:
        s "I don't think anyone would expect that at all since I am the huggy boy, but I don't blame you for wanting to avoid any pressure on that end."

    scene iodormten10
    with dissolve

    i "I don’t care about pressure but..."
    i "Is that really what everyone thinks of you?"
    i "That you’re up to something?"
    s "..."
    i "You’re not, though. Right?"
    i "And even if you were, isn’t it a little obsessive of them to not let you do what you want to do? "

    if bonus == True:
        i "You’re an adult. You don’t have to care about what a bunch of [teenage]girls think. They-"
        s "They’re toxic, yes. I already know how you feel."
        s "You’ve mentioned it a few times now."
    else:
        s "Is this the part where you call them all toxic again?"

    scene iodormten11
    with dissolve

    i "...Yeah."
    i "..."
    s "..."
    i "You know, Sensei..."
    i "I’ve got a lot going on and I’m by no means perfect-"
    i "But I’d never do something like judge you for hanging out with whoever you want to hang out with."
    i "That’s your prerogative."
    s "..."
    i "..."
    s "That’s not true and you know it."

    scene iodormten12
    with dissolve

    i "...Huh?"
    s "It’s human nature to get jealous of things you don’t have- or things you want."
    s "It’s clear you want to spend as much time with me as possible, so you’d obviously judge me if I just abandoned you for other girls."
    i "..."

    scene iodormten13
    with dissolve

    i "Yeah, you’re probably right."
    i "I don’t think I’d ever say anything about it, though."
    s "That’s because you’re a coward."
    i "I know."
    s "And you’re weak."
    i "Uh-huh..."
    s "And you have stupid hair."

    scene iodormten14
    with dissolve

    i "Okay, now you’re just being mean."

    scene iodormten15
    with fade

    "Io moves closer to me and rests her head on my shoulder- something people don’t normally do after you insult them."
    "Granted, I was just kidding for the most part. But it’s still a strange reaction either way."

    i "You can keep making fun of me if you want. I don’t mind."
    s "Sure but-"
    i "This is okay, right? Even though I’m a weak coward with stupid hair?"
    s "There’s nothing cowardly about making a move like this on your teacher."
    i "You’re right. I’m actually kind of awesome, aren’t I?"
    s "You’re definitely unique, if not anything else."

    scene iodormten16
    with dissolve

    i "That’s far from a compliment, Sensei."
    i "Being unique can be a death sentence sometimes."
    i "Also, you don’t actually think my hair is stupid, do you?"
    i "It’s like, one of the three things I like about myself."
    s "What are the other two?"
    i "My eyes and how I can still get out of bed in the morning."
    s "That last one is a little more real than I was expecting, but I get it."
    i "Do you have three things you like about yourself, Sensei?"
    s "I’m not even sure I have {i}one{/i}."

    scene iodormten17
    with dissolve

    i "And you call {i}me{/i} a coward. That’s the most cowardly thing I’ve ever heard."
    i "Everyone has {i}something{/i} they like about themselves. Even if it’s something small like how you look in a particular photo or how your voice sounds when you sing in the shower."
    i "There’s gotta be something in there."
    i "I’ve already found plenty of stuff I like about you."
    s "Name one."
    i "Your shoulder’s really comfortable. And warm."
    i "And I like how you still come talk to me despite me being overbearing and annoyingly sensitive."
    s "Yeah. You’re kind of hard to talk to at times."
    i "True. But at least I'm more interesting than the rest of the girls in class, right?"
    i "I mean, why else would you be here tonight instead of with any of them?"
    i "Not to mention, I haven’t even seen you with that one blonde girl again since the two of you showed up at the bathhouse."

    scene iodormten18
    with dissolve

    i "Are you bored of her now that you have me?"
    i "I’ve gotta say, I kind of get it."
    i "She seemed a little too plain anyway."
    i "Pretty, but plain."
    i "Obviously, I’m sure there’s a lot more to it than that."
    i "But even the fact that you’re letting me rest my head on your shoulder like this-"
    s "What are you doing?"

    scene iodormten19
    with dissolve

    i "Hm?"
    i "What do you mean?"
    i "Aren’t we bonding?"
    i "Did I say something wrong?"
    s "This is your idea of bonding?"
    s "Talking down about people you’ve never even spoken with?"
    i "..."
    s "That blonde girl's name is Ayane and she’s far from plain."
    s "She’s actually one of the most unique people I’ve ever met."

    scene iodormten20
    with dissolve

    i "Wait, I wasn’t trying to talk down on her. I was just..."
    s "Just what?"
    i "I...I was just trying to make you think I was...more interesting."
    s "There are ways to do that without making everyone else seem small."
    s "You’re underestimating how much you’ve impressed me so far."
    s "Don’t ruin all of that by belittling people you know nothing about."

    scene iodormten21
    with dissolve2

    i "..."
    s "..."

    "The caterpillar squirms once more."

    i "I'm..."
    i "I’m sorry."
    s "There’s no sense in apologizing to me."
    s "Just think more about what you’re saying before you actually say it."
    s "You’re smart. Bad with people, maybe, but really...really smart."
    i "Sensei..."
    s "You’re better than this. That’s all I’m saying."

    scene iodormten22
    with dissolve2

    i "Well..."
    i "Why are you here, then?"
    i "If there are other interesting people who don’t do things like talk down on everyone around them, why come {i}here{/i}?"
    i "I just...thought there was a reason for it. That’s all."
    s "I’m here because I wanted to be here."
    s "Don’t overthink it or try to turn it into some sort of equation that needs to be solved."
    s "Not everything happens for a reason. Sometimes things just...happen."

    scene iodormten23
    with dissolve

    i "..."
    i "Sometimes...things just happen..."
    i "..."
    i "I messed up big time, didn’t I?"

    scene iodormten24
    with dissolve2

    s "Yeah."
    s "But you’re still learning."
    s "Just don’t be a bitch and everything will work out fine."
    i "I like the head patting thing but not so much the being called a bitch part."
    i "I guess I deserve it, though."
    i "Either way, please don’t stop. That feels really nice."

    scene iodormten25
    with dissolve

    "I leave my hand on Io’s head for reasons beyond my comprehension...but I feel like a good portion of them are simply due to how cute she is."
    "Frankly, though...I’m actually kind of mad right now."
    "It’s one thing to not associate with any of the other girls- a thing I can understand and respect."
    "But to do something like demean them behind their backs without even attempting to understand where they come from-"
    "Isn’t that exactly why Io dislikes girls in the first place?"
    "Because they start unnecessary drama?"
    "Is she really this desperate for affection?"

    i "Mn..."

    "Or is it something else?"
    "Something I don’t understand yet."

    scene black
    with dissolve2

    "I don’t stay much longer after that, but not because I don’t want to."
    "Io actually asks me to leave so she can get a head start on some new thing she wants to build."
    "I try asking what she plans on making, but she hurries me out of the room in suspiciously quick fashion."
    "It is what it is, though."
    "I’m not interested in dampening her creative process when she seems weirdly motivated all of a sudden."
    "I just hope that whatever it is she makes doesn’t wind up collecting dust on her shelf for the rest of eternity."

    $ renpy.end_replay()
    $ io_love += 1
    $ iodorm10 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm15:
    play sound "knock.mp3"
    stop music fadeout 15.0

    "I knock on Io’s door and wait for her to answer."
    "But several seconds go by without a response and, given that she doesn’t normally work this late, I start to wonder if she might be out doing something else."
    "But then I remember that this is Io we’re talking about, and that the likelihood of her actually doing anything other than working or hanging out in her room is practically zero."
    "So I knock again."

    play sound "knock.mp3"

    s "Hey. Are you in there?"
    s "..."

    "Time starts to tick by and-"

    i "Ngh...what?"
    i "Sensei? "
    i "Is that you?"
    s "Did I wake you up? "
    i "Not...exactly but..."
    s "Can I come in?"
    i "Yeah...Let me just get this out of the way and-"
    play sound "thump.mp3"
    with hpunch
    i "Ah!"

    "Something falls over and hits the ground."
    "But considering there are roughly six million objects inside of Io’s room, things like this are bound to happen."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I’ll have to ask Ami to clean this room while Io is away since Uta is clearly incapable of fulfilling her maidly duties and-"

    scene iokotatsu1
    with dissolve2
    play music "hometown.mp3"

    i "Ngh..."
    s "Are you okay?"
    s "Was that {i}you{/i} who fell just now?"
    i "...Probably."
    s "I feel like that’s something you should know."
    i "Just...a little out of it..."

    scene iokotatsu2
    with dissolve

    i "So, uhh..."
    i "What’s up?"
    s "What’s up is you’re either extremely tired or extremely drunk."
    i "Or extremely messed up from mixing medications and not eating anything all day."
    s "Medication?"
    i "It’s the fancy word for medicine."
    s "I know what it means, Io."
    i "Cool. Then we can forget this happened and talk about something else."
    s "The next time you don’t respond to my knocks, I’m just walking away."
    s "If you need rest or whatever, you shouldn’t be getting out of bed for me."

    scene iokotatsu3
    with dissolve

    i "I told you, I’m good. Just a little out of it."
    i "This isn’t like, an abnormal thing. It happens all the time and it’s easily preventable."
    i "I’m just a little dizzy. "
    s "Can you stand?"
    i "Probably not. So if we could hang out on the ground, that would be cool."
    s "I mean...that doesn't exactly sound like a good time. But I don’t think it can be helped at this point."
    i "If you’re okay with catching me, I can try standing up."
    s "You weigh probably just as much as my cell phone, so that much wouldn’t be a problem."
    s "But I don’t think you should be overexerting yourself if you’re sick."
    i "I’m not {i}sick{/i} sick. I’m Io sick."
    s "Is that some new form of debilitating disease?"
    i "Yeah. They made it just for me."
    s "Really, though. What’s wrong?"
    i "It’s a secret."
    s "You hate secrets."
    i "The pill bottles are right behind me and I’m in no shape to fight you. "
    i "I mean, even if I wasn’t all messed up right now, I wouldn’t be in any shape to fight you. You’re really big."
    i "But go ahead and read them if you’re that curious. There are some pretty wild names on there."
    i "Oh, and there are a couple more under the bed you can probably find if you lay down and move your arm around."
    i "They fell off the mini fridge when I tried to make it to the door and now I'm gonna have to crawl under there and get them back."
    s "I’d really prefer if you’d just tell me what's wrong so I don’t have to Google some complicated name that I won't even be able to say out loud."
    i "I mean, if it was just {i}one{/i} thing, I wouldn’t have so many different bottles, right?"
    i "I’m all sorts of broken. I already told you this."
    s "You don’t look that broken to me."
    i "And {i}you{/i} don’t look that broken to me. So we’re either really good at judging each other or really bad at it."
    i "Why are you still standing?"
    s "Because I don’t want you to throw up on me."

    scene iokotatsu4
    with dissolve

    i "I’m not going to throw up on you. "
    i "Well, I probably would if you like, spun me around or something. But that’s not a thing you’ve done so far, so unless you’ve developed some weird new hobby..."
    s "Spinning isn’t really an interest of mine. But I could pick you up and put you down on your bed if you want to get some rest."

    scene iokotatsu5
    with dissolve

    i "Oooooooor...we could use the kotatsu I just fixed so you don’t have to throw me over a bunch of obstacles and risk knocking the rest of my stuff down."
    i "It also gives us an excuse for me to lay on your lap and have you pat my head."
    s "What if you’re not sick at all and this is just one elaborate ploy to obtain a lap pillow?"
    i "Then I am a much better actor than I thought I was. "
    s "Io-"
    i "Come oooooooon. It’s really warm under there. And I’m super light. You won’t even know I’m on you."
    s "I have no problem with you being “on” me. I’m just having a hard time telling you that I think we should maybe talk about all of these medications."
    i "Are you a doctor?"
    s "I’m not."
    i "Well then what good will talking about my medications do for either of us?"
    i "I’m fine. I’ve got a bunch of stuff that I can take for certain things whenever I need to take them."
    i "I just happened to need several different things tonight and, mixed with the fact that I haven’t eaten at all and how I barely slept last night-"
    i "Boom. Down goes Io."
    s "..."
    i "..."
    s "Hah..."

    scene black
    with dissolve

    "I sigh to myself and accept that Io’s probably not going to give me any specific details tonight."
    "But I think it’s pretty safe to assume that it’s nothing physical if she only takes them when she needs to and-"
    "Well, I guess they could still technically be painkillers or something."
    "Damn it. "
    "Why did she have to pick now to get all light headed?"
    "........."
    "......"
    "..."

    scene iokotatsu6
    with dissolve

    "I turn off the lights before moving over to the kotatsu and sliding myself underneath it."
    "Io waits on her step ladder until I’m in place and then very slowly and clumsily climbs onto me, resting her body in my lap and her head on my chest."

    if bonus == True:
        "It’s a position that makes me acutely aware that I must focus at least half of my energy on not getting an erection because it would be overwhelmingly apparent to her if I did."
        "I stabilize myself with my left hand and use my right one to softly rub her shoulder. "
        "It’s not something I’d normally have any interest in doing, but...given the context of the situation, I think it’s okay for me to be a little nice."
        "At least until she’s able to stand on her own two feet again."
        "As soon as that happens, she can rub her own shoulder."

    i "Guh...sleepy..."
    i "One of the downsides to pretty much every single anxiety medication is how tired they make you."

    "Ahh, so it {i}wasn't{/i} anything physical."
    "Shocker."

    s "You have anxiety?"
    i "Amongst other things."
    i "Was the anxiety part not obvious to you?"
    s "I probably could have guessed. It just sounded rude to say something like, “I thought so.”"
    i "Well, thank you for your sudden increase in generosity."
    i "Maybe I should just always invite you over before I take my meds to reap the benefits of being {i}your{/i} student."
    s "What’s with the emphasis on “your?”"
    i "There aren’t many teachers who would let an anxious, loopy, drugged out [teenager] climb into their lap."
    s "Yeah. Ms. Watabe would have never let you do this with her."
    i "Good. Because I wouldn’t {i}want{/i} to do this with Ms. Watabe."
    i "You, on the other hand..."
    i "I could do this every night for the rest of my life and not get tired of it."
    s "..."
    i "..."
    s "Io?"
    i "Yeah?"
    s "Why do you like me so much?"

    scene iokotatsu7
    with dissolve

    i "Because I have to."
    s "Why?"
    i "Because you’re my last bastion of hope for adults in this world."
    i "I am so tired of everyone else that if things don’t work out with you, I’ll probably just die."
    s "Oh, okay. That doesn’t put all of the pressure in the world on my shoulders or anything."
    i "You’ve already got the rest of me weighing down on you. Might as well go for the shoulders, too."

    scene iokotatsu8
    with dissolve

    i "That was kind of just a joke anyway."
    i "You really are my last line of defense, though."
    i "And probably the only example of something that I’ve wanted that I’ve actually made a push for."
    s "Some push you’re making, nearly passing out in front of me."
    i "There have been other pushes. This one was just a convenient coincidence."
    i "If I’m being completely honest, Sensei...I don’t know why it was you who appealed to me."
    i "You were probably just in the right place at the right time."
    s "So it could have been anyone?"

    scene iokotatsu9
    with dissolve

    i "It could have been anyone."
    i "But..."
    i "I’m glad it was you."
    s "... "
    i "..."
    s "..."
    i "..."

    play sound "dooropen.mp3"
    scene iokotatsu10
    with dissolve

    u "Uta’s home!"
    i "Welcome back. Don’t mind us."
    s "...Hi."
    u "..."
    u "Uta’s not home! Please carry on!"
    i "Wait, no. Stay."
    i "I want you here."

    scene iokotatsu11
    with dissolve

    u "Uhh..."
    i "Pleeeeeease?"
    u "I...don’t know..."
    u "Like...this seems like something I probably shouldn’t get involved in..."
    s "I think you’re misunderstanding the situation."

    scene iokotatsu12
    with dissolve

    u "Did you take too much again?"
    s "Oh. Or you completely understand the situation."
    u "After a few seconds of actually thinkin’ about it, yeah."
    u "How are you feeling? Do you need any water? Juice?"
    i "I’m okay now that Sensei’s letting me use his lap."
    u "Good...I’m glad..."
    u "Hang in there."

    scene iokotatsu13
    with dissolve

    u "Welp! I’ll leave you two kids to it, then! I’ve got no job to do here and my presence will just be a bother!"
    i "Hey, no. I really do want you to stay. It’s totally fine."
    u "Nope! I’m out! "
    u "Don’t...do anything crazy without...calling your aunt!"

    play sound "dooropen.mp3"
    scene iokotatsu14
    with dissolve

    "Uta leaves just as quickly as she arrived."
    "Where she ran off to, I have no idea. But I guess this means that I have a little more time alone with Io."

    i "I really did want her to stay..."
    s "She probably just felt uncomfortable seeing her friend cuddled up against her teacher."
    i "Probably."

    scene iokotatsu15
    with dissolve

    i "It’s admittedly not a thing either of us have any real experience with."
    s "Didn’t Uta think you were a boy when you two first started talking?"
    i "Yeah. And I thought she was a boy too. "
    i "But just because we thought each other were the opposite gender doesn’t mean we have any notable experience with said gender."
    s "It’s just weird that you make an exception to your “no girls” rule for her when she’s one of the girliest girls I’ve ever met. That’s all I’m saying."
    i "It is weird, yeah."

    scene iokotatsu16
    with dissolve

    i "But I really look up to Uta. "
    i "She’s amazing."
    s "In what way?"
    i "In that she got better."
    i "In that she can wake up and put a real smile on. And hold real conversations with all sorts of people."
    i "In that she can organize a classwide, two-day event on a whim and pull the entire thing off without so much as a drop of sweat. "
    i "In that she’s pretty and sweet and doesn’t use that as a front to get what she wants from people."
    s "You clearly have not spent enough time at the maid cafe."
    i "That's a job. It doesn't count."
    i "Uta’s the perfect girl."
    i "I hate it so much."
    i "But I also {i}love{/i} her so much."
    i "And I probably wouldn’t be here without her."

    scene iokotatsu17
    with dissolve

    i "And I’m not joking this time, by the way."
    i "I would very likely be dead if I never met Uta."
    s "She...seems like a great friend."

    "I’m not really sure what else I’m supposed to say to that."
    "Io’s always spewing out a corrosive mixture of positivity and negativity that blend just about as well together as bleach and ammonia."
    "The room fills up with fumes that my lungs can’t handle, and I slowly die with my hand still clasped around her shoulder."

    i "She’s the best friend."
    i "I just wish I could give her more than {i}me{/i}, you know? Like, I suck. She can do so much better."
    s "Yeah, you’re pretty terrible."
    s "But you’re also great in your own ways too."
    i "Like what? Tell me some."
    s "Like...you’re light."
    s "You can lay here and I can’t even feel you."
    i "Uh-huh. And what else?"
    s "That’s it."
    s "That’s all I’ve got."
    i "I can settle for that. That’s fair."

    scene iokotatsu18
    with dissolve

    s "It would probably be nice if you thought a little higher of yourself, though."
    i "I have to do something worthy of being praised for before I can even think of praising myself."
    i "Right now, I’m just a weightless, overmedicated cockroach with a grand total of two bras and four boxcutters."
    s "Why do you have four boxcutters? And why do you only have two bras?"
    i "Do you want to buy me more?"
    s "Bras or boxcutters?"
    i "Why would I need three bras? I can just wash them."
    s "Why would you need five-"
    s "You know, what? Nevermind."
    s "Just...do yourself a favor and...eat before you take your medication next time."
    i "I make no promises, Sensei. Sometimes, I just don’t want to eat."
    s "Well then don’t take your medication those days."
    i "Yeah, that’s probably an even worse idea than the not eating thing."
    s "Why do you have to be so difficult?"
    i "Why do everyone’s standards for “easy” have to be so hard to reach?"
    i "You’d think that “easy” would imply a complete lack of difficulty, but being easy to deal with takes a lot of work. Probably."
    i "I don’t know. I’m definitely not the right person to ask."
    i "I just hope that you're okay with me being the way I am, because I like this a lot."
    i "In fact, I like it so much, I’m gonna take a nap."
    i "Goodnight, Sensei."
    s "..."
    s "Goodnight."

    scene black
    with dissolve2

    "I think about shooting some snarky retort at Io about how I wouldn’t have come here if she was just going to fall asleep on me-"
    "But her forehead is basically a space heater right now."
    "And her body, despite being light as air, is the same way."
    "I’m flattered that she was able to carry on such a lengthy conversation with me despite showing all signs of not being well-"
    "But not thinking about herself will wind up killing her."
    "In fact, thinking {i}too much{/i} about herself will also wind up killing her."
    "Io is practically dead already."
    "And there is no one who deserves rest quite like the dead."
    "So I let her fall asleep."
    "And after she doesn’t wake up for the next hour, I carefully pick her up and lay her down on Uta’s bed, since that one is actually possible to reach."
    "And then I leave without checking the labels on any of her mystery bottles."

    $ renpy.end_replay()
    $ io_love += 1
    $ iodorm15 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

                    ############################################
                    ##########        ROOM 8         ##########
                    ############################################

label nodokadorm:
    if nodoka_love >= 0 and day288 == True and nodokafirsthall == True and otohafirsthall == True and day != 1 and day != 5 and nodokadorm1 == False:
        jump nodokadorm1
    if nodoka_love >= 5 and nodokalibrary5 == True and day < 6 and day != 1 and nodokadorm5 == False:
        jump nodokadorm5
    if nodoka_love >= 15 and yasudorm20 == True and nodokadorm15 == False:
        jump nodokadorm15
    elif day288 == True and otohadorm1 == False:
        "I don't think Nodoka is ready to hang out alone in her dorm just yet..."
        jump doorknock2
    else:
        jump nodokadormgen

label otohadorm:
    if nodoka_love >= 0 and day288 == True and nodokafirsthall == True and otohafirsthall == True and day != 1 and day != 5 and nodokadorm1 == False:
        jump nodokadorm1
    if otoha_love >= 5 and otohapark5 == True and day > 5 and otohadorm5 == False:
        jump otohadorm5
    if otoha_love >= 20 and christmasfive8 == True and day < 6 and otohaspring4 == False:
        jump otohaspring4
    elif day288 == True and otohadorm1 == False:
        "I don't think Otoha is ready to hang out alone in her dorm just yet..."
        jump doorknock2
    else:
        jump otohadormgen

label nodokahall:
    if nodokafirsthall == False:
        jump nodokafirsthall
    else:
        jump nodokahallgen

label nodokahallgen:
    if chapthreeactive == True:
        scene nodokasummer2hallgen
        with dissolve
    else:
        scene nodokahall3
        with dissolve

    if bonus == True:
        no "Sensei, good. Do you mind if I ask you for your thoughts on sexual torture devices?"
        no "It shouldn't take long, but I'd like to know if your thoughts on the matter match my own."
        s "..."

        "I spend several minutes trying to figure out why Nodoka wants to talk about such a thing before I chalk it up to just being on account of her...being Nodoka."
        "It's best to not get in her way when she's dead set on talking about something."
        "Even if that something is a thing that would make the vast majority of people uncomfortable."
        "But hey, she definitely could have chosen worse fetishes."
    else:
        no "Sensei, good. Do you mind if I ask you for your thoughts on cows?"
        s "Cows?"
        no "I think they're up to something."
        no "{i}I just can't figure out what...{/i}"

    scene black
    with dissolve

    if bonus == True:
        "To Nodoka's dismay, I don't have many thoughts on her topic of choice."
        "She, however, walks the fine line between loving and hating it, apparently."
        "I'd love to tell you which parts she enjoys and which parts she doesn't-"
        "But frankly, she names so many devices that I've never even heard of that I don't want to mix anything up."
        "Regardless, the conversation comes to an abrupt and awkward end as the two of us ultimately decide to head back to our respective beds."
        "Albeit with one of us significantly less aroused than the other."
    else:
        "Nodoka and I...talk about cows, I guess?"

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label nodokadormgen:
    play sound "knock.mp3"

    no "Come in!"

    scene nodokadormgen
    with fade

    "I decide to spend the night hanging out with Nodoka in her dorm."
    "She makes coffee for the two of us to share and we proceed to sit on her bed, making idle chit chat while listening to melancholic indie rock bleeding out of her smartphone."
    "She says that Otoha would be fine with us borrowing one of her speakers or amps and playing it through there-"
    "But then states that there's something magical about the tinge of distortion that accompanies music when streamed through the same devices we use to speak to our loved ones."
    "For those of us that have any loved ones, I mean."
    "I can't help but feel like this won't change much for her or myself."
    "Nonetheless, it changes nothing."
    "The music drags on."

    scene black
    with dissolve

    "Despite Nodoka showing no signs of growing tired, I realize I'm unable to stick around any longer without the fear of passing out."
    "And if I pass out in here, I strongly believe that she might conduct experiments on me for the purpose of her own personal {i}research{/i}."
    "I am not a lab rat. And I can get home without having to traverse a maze."
    "So I do just that and leave her behind."
    "I don't know what she does after that."

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label otohadormgen:
    play sound "knock.mp3"

    o "Come in!"

    scene otohadormgen
    with fade

    "I decide to spend the night hanging out with Otoha in her room."
    "Without much for the two of us to do around here, I manage to coerce her into playing a few songs for me."
    "She's a bit bashful about it at first since it's apparently weird to just play and sing for one guy in her room."
    "I get that. It definitely is weird."
    "But we manage to counteract the discomfort by eighty-sixing the vocals and just maintaining different sorts of conversations while she strums away."
    "We talk about all sorts of things, none of them being noteworthy, as the sun is slowly overtaken by the moon."
    "Before we know it, it's almost midnight."

    scene black
    with dissolve

    "I try to get Otoha to play an encore for me, {i}with{/i} vocals this time-"
    "But she promptly kicks me out of the room and tells me I'll need to come see her perform elsewhere if I want a real show."
    "It's fine, though."
    "I'm perfectly content for what I {i}did{/i} get to see."
    "Because I realize that no one else will ever see it."
    "And exclusivity is one of my favorite things in the world when I am the one benefiting from it."

    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha's affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label nodokafirsthall:
    scene nodokahall1
    with dissolve

    no "Oh. Well, hello there."
    no "To what do I owe the pleasure, Sensei?"
    s "No pleasure involved, just here to kill some time."
    no "No pleasure involved? Not even a little bit?"
    s "I mean...if you want there to be pleasure..."

    scene nodokahall2
    with dissolve

    no "Of course I want there to be pleasure. "
    no "Why else would I have this word-coated rectangular object in my hands?"
    s "Weird way to say “book” but okay."
    no "What I mean to ask is why bother indulging yourself in anything if there is nothing to leech from it?"
    no "We are all but leeches, Sensei. Digging our tiny, jagged teeth into anything they’ll latch onto in search of the essence of life."
    s "Weird way to say “blood” but okay again."

    scene nodokahall3
    with dissolve

    no "Would you at least agree that words without experience are meaningless?"
    no "It’s something that appeared inside of this very rectangle and I’d be a liar if I were to say it didn’t provoke some impure thoughts in this old noggin of mine."
    s "You’re still in [high_school]. Your noggin is absolutely not “old.”"
    no "No, it is not."
    no "But that calls into question exactly why I am reading {i}this{/i} specific piece of literature despite having no experience in its subject matter."
    no "If words without experience are meaningless, shouldn’t {i}these{/i} words, which I have no experience {i}with{/i}, simply bounce off the walls of my brain without so much as leaving a minor bruise?"
    s "Can brains even bruise?"
    no "Probably? I can’t imagine it would feel very nice, though."
    s "What are you reading anyway?"

    scene nodokahall4
    with dissolve

    if bonus == True:
        no "“Lolita.” Are you familiar with it?"
    else:
        no "“Clifford the Big Red Dog.” Are you familiar with it?"

    s "Vaguely. I feel like I read that a long time ago but I’m kind of hazy on the details."
    no "I’m not surprised you’ve read it given your...demeanor so far."

    if bonus == True:
        no "I’m sure the title itself is enough to give you an inkling of what the subject matter is, though."
        no "Sexual conduct is one thing, but do you believe you’d ever be able to fall in love with someone so much younger than you, Sensei?"
        s "I prefer not discussing love whenever possible. It’s not exactly a cut and dry topic."
        s "Do you think you’d ever be able to love someone so much older?"

        scene nodokahall5
        with dissolve

        no "I also prefer not discussing love whenever possible. "
        no "It’s not exactly a cut and dry topic."
        no "I do yearn for the taboo, though. But I’m pretty sure the whole [incest] thing gave that away."
        s "Yeah, you’ve come across as kind of...freaky so far."
        no "{i}I{/i} do? Whatever do you mean?"
        no "I’m but an inexperienced, [adolescent] leech whose teeth aren’t sharp enough to latch onto anything."
        no "Perhaps I could try to take a bite out of you, Sensei? For practice."
        s "Like, right now?"
        no "Just a little nibble. Quickly, before Uta sees us."
        s "That book is really getting to you, huh?"
    else:
        s "Yeah. I really do present myself as a Clifford lover, don't I?"
        no "There's so much about you I can deduce just from that little factoid alone."

    scene nodokahall6
    with dissolve

    if bonus == True:
        no "It is. "
        no "I’m very easily fascinated by things most people aren’t able to experience in their own lives."
        no "Though, I suppose the idea of an illicit and inappropriate relationship may be a bit more common than I thought prior to attending [kumon_mi_high]."
        no "So, yes. I can’t help but feel my heart begin to race at the thought of something like that."
        s "Maybe I’ll give it another go soon. It’s been a while since I’ve read anything, to be honest."
        no "That’s a shame. Literature can be a portal to different worlds and different lives."
        no "Your time would likely be better spent on literature you’re not currently living through, though."

    s "Are you suggesting something about me, Nodoka?"

    if bonus == True:
        no "If not suggesting, then recommending...as you have more than a handful of {i}opportunities{/i} at your disposal."
        no "You’ve already confirmed some of your thoughts on the topic of manipulation. Surely you don’t only use that tactic for little, white lies."
        s "Is this your attempt at manipulating {i}me?{/i}"
    else:
        no "I'm not {i}not{/i} suggesting something about you, dog lover."
        s "Is this a manipulation tactic?"

    no "What would I possibly manipulate you into doing that you wouldn’t already do on your own?"
    s "Reading more books."

    scene nodokahall7
    with dissolve

    no "Ahh, yes. The consumption of knowledge has become more taboo than any illicit relationship out there."
    no "It’s certainly starting to feel like that, at least."

    scene nodokahall8
    with dissolve

    no "I’m surprised you’ve managed to go so long without diving into a word-maze, though."
    s "Jesus, Nodoka. Just use the word “book.”"
    no "Well now I’m just going to continue abstaining out of sheer spite."
    s "Of course you are..."
    no "Futaba tells me you used to be a writer, Sensei. "
    no "Why is it that you’ve given up on that? "
    s "At this point, my brain is so all over the place that I feel like anything I write would come out twisted and indiscernible."

    if bonus == True:
        no "So what? You should know better than anyone that the overflow of creative juices can lead to all sorts of amazing things."
        s "So can the overflow of {i}less{/i} creative juices."
        no "Please explain to me in detail exactly which juices you are referring to, Sensei."
        no "Quickly, before Uta hears us and has to call her parents."
        s "You know about the parent thing too?"
        no "I do. And your response has consequently confirmed that you’ve been involved in at least one sexual conversation with her."
        no "Nice."
        s "She’s an overly flirtatious part-time maid. It would be more surprising if I {i}didn’t{/i} find myself in a conversation like that with her at least once."
        no "Ooooooh and you like maids as well."
        no "We should go to the cafe together sometime and prey upon those innocent girls."
        no "Think of how many soft, slender necks we could dig our teeth into."
        s "My [niece] works at that cafe, Nodoka."
    else:
        no "Clifford's really gotten to you, huh?"
        s "Why is he so big? They never explain it."

    scene nodokahall9
    with dissolve

    no "Sensei...you’re {i}really{/i} trying to excite me now, aren’t you?"

    if bonus == True:
        s "I feel like you are very easily excited."
        no "But {i}not{/i} very easily satisfied."
        no "Remember that when the time comes for you to become my own Humbert Humbert."

        scene nodokahall10
        with dissolve

        no "Until then, though, I suppose I will continue to live inside of paper."
        s "Wait. I don’t remember much of “Lolita,” but I’m pretty sure I’m already that Humbert guy."
        no "We’re not at that part of the novel yet, Sensei."
        no "But perhaps, somewhere, some day, at a less miserable time, we may see each other again."
        no "Goodnight."
    else:
        s "What? No. I'm trying to open up to you about what the book series has done to me."

    scene nodokahall11
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        "Nodoka goes back into her room and leaves me standing in the hall, bewildered and mildly aroused."
        "That’s pretty much how half of our conversations end, though, so I’m not {i}too{/i} shocked by it."
    else:
        s "What the fuck. Don't just leave."
        no "{i}Can't hear you!{/i}"

        "I feel so alone all of a sudden."

    scene black
    with dissolve

    "Either way, I decide to simply go home and rest."

    if bonus == True:
        "But not until after knocking on her door several times to see if she was ready to skip further into our novel together."

    $ renpy.end_replay()
    $ nodoka_love += 1
    $ nodokafirsthall = True
    stop music fadeout 5.0

    "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohahall:
    if otohafirsthall == False:
        jump otohafirsthall
    else:
        jump otohahallgen

label otohahallgen:
    if otohaspecial15p2 == True:
        scene otohasummer2hallgenhair
        with dissolve
    elif chapthreeactive == True and otohaspecial15p2 == False:
        scene otohasummer2hallgen
        with dissolve
    else:
        scene otohahall1
        with dissolve

    o "Yo!"
    o "What brings you over here, Sensei?"

    "I decide to {s}hang out with{/s} bother Otoha in the hall for a little while in an effort to quell some of my boredom."

    if bonus == True:
        "She obliges and humors me, constantly feeling the need to remind me that she is both way out of my league and way out of my age group."
        "Or both of those things."
        "In fact, yeah. Definitely both of those things."
    else:
        "She obliges and humors me, constantly feeling the need to remind me of her conservatorship and how large her parents are becoming."

    "But that doesn't change how we seem to enjoy talking to one another, even if we're talking through these two giant barriers positioned between us."

    scene black
    with dissolve

    "We don't hang around for long, as Otoha is supposed to be meeting up with Nodoka tonight, but we do make plans to hang out again soon."
    "Even if {i}making plans{/i} in this case means something more like...her agreeing to open the door if I randomly show up again."
    "But hey, you take what you can get."

    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha's affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohafirsthall:
    scene otohahall1
    with dissolve

    o "Oh, hey. What’s up?"
    o "You looking for somebody?"
    s "Yes. Her name is Otoha Okakura. Have you seen her anywhere?"

    scene otohahall2

    o "Cool name. Sounds like she’d be a really good singer."
    o "Want to look for her together?"
    s "No need. I’m pretty sure I just found her."
    o "What? Where?"
    s "Right in front of me..."

    scene otohahall3
    with dissolve

    o "Aww, shucks. You know what? Now that you mention it, that {i}is{/i} me."

    scene otohahall4
    with dissolve

    o "What do you need with {i}me{/i}, though? I didn’t like...break any rules or anything, did I?"
    s "Rules? I’m not even sure if these dorms have rules."
    s "And if they do, I’m definitely not the person you should be asking about them."
    s "I just came over to see how you were doing."

    scene otohahall2
    with dissolve

    o "I’m great. But like, what do you mean there aren’t any rules?"
    o "We’re [teenage]girls living in a dorm room without a permanent supervisor. Surely there have to be like...{i}some{/i} rules?"
    s "Just make up your own rules if you want them so much."
    o "I don’t {i}want{/i} them but like...it’s just weird that there {i}aren’t{/i} any."
    o "Like, what if I wanted to play my keyboard really loud at 2:00 AM. Wouldn’t I get in trouble?"
    s "Probably not. But I can’t imagine Nodoka or any of the other girls would like you very much after that."

    scene otohahall5
    with dissolve

    o "I’m pretty sure Nodoka doesn’t sleep, so she’d be fine with it."
    o "And it’s not like I’d do something like that anyway. I need peace and quiet after a certain point of the night or I just...can’t get anything done."

    scene otohahall6
    with dissolve

    o "This definitely isn’t me saying I want to go back or anything, but one of the things I liked about staying with my parents was that it was always quiet as soon as dinner was over."
    o "So I’d get to just...sit around and write whatever came to my mind."
    o "Here, it’s like...the complete opposite."
    o "I'm also literally {i}right{/i} next to Molly’s room and I’m pretty sure her volume knob is busted."
    s "I’m pretty sure most of her is busted."
    mo "I can hear you two, you know?!"

    scene otohahall7
    with dissolve

    o "Hey, Molly! If it makes you feel better, I think your Japanese is really good!"
    o "And you like, barely even have an accent, so...good job!"
    mo "I will...forgive these transgressions for now!"
    mo "But please wait until I am out of range if you’re going to use vicious mockery on me!"
    o "I don’t know what that is, but okay!"
    s "At least you seem to be getting along well."

    scene otohahall8
    with dissolve

    o "I’m like, weirdly good at making friends."
    o "I’ve gotten along with basically everybody here so far."
    s "Are you sure that's not just everyone having a crush on you by now?"

    scene otohahall9
    with dissolve

    o "Oh God, I hope not. I have no idea how I’d go about rejecting so many people at once."
    o "Should I like, send out a newsletter or something?"
    s "Yes. That is absolutely something you should do. I’ll give you my email address so you can copy me on it as well."

    scene otohahall10
    with dissolve

    o "Don’t tell me {i}you{/i} have a crush on me, too..."

    if bonus == True:
        s "Do you think it would be more likely or less likely that your parents would approve of you dating a man my age rather than someone {i}your{/i} age?"
        o "Is that even a question? They’d definitely prefer someone my age if they were forced to choose."
    else:
        s "Absolutely not. I have never once even thought of you that way."

    o "Rin would kill me if I ever dated you anyway. So, yeah. Sorry but..."
    o "Actually, just wait for the newsletter. That will explain everything."
    s "I’m pretty sure Rin would be a little more upset about you not dating {i}her{/i} than dating me, so she definitely won’t kill you."

    scene otohahall11
    with dissolve

    o "I don’t know about that, Sensei."
    o "I know I’ve only seen you two together a handful of times but...she’s different with you than she is with anybody else. Myself included."
    s "You know what? It probably wouldn’t be smart to carry on this conversation with Molly standing right behind us, so..."

    scene otohahall12
    with dissolve

    o "She started playing something on her phone, so I’m sure she’s not paying much attention. "
    o "But yeah, I agree. I feel weird talking about people when they’re not around anyway."
    s "Any suggestions for a new topic then?"
    o "Hmm...how about you tell me why you're suddenly so interested in {i}how I’m doing?{/i}"
    o "You’re not worried about me feeling homesick or something, are you?"
    s "No, but...are you?"

    scene otohahall13
    with dissolve

    o "I’m not."
    o "I...think I like it here."
    o "I had no idea that living with people similar to me could be so...exhilarating. "
    o "And even if it gets loud and I have a hard time focusing on my work...it’s fun. "
    o "Like there’s always some sort of...mystery behind every door."
    s "There is a mystery behind every door. Sometimes even more than one."
    s "Just make sure you knock on them before entering if you want to avoid ever walking in on something weird."

    scene otohahall12
    with dissolve

    if bonus == True:
        o "I’m...just going to hope that you’re talking about them getting changed or something and not anything involving you."
        s "You think whatever you want to think. I’m just giving you the proper warning."
        o "..."
        o "Okay, don’t take this the wrong way, but like..."
        o "How did you get hired as a teacher?"
        s "That’s a very good question, Otoha."
        o "..."
        s "..."
        o "Is there...an answer to it?"
        s "There’s no answer to why there aren’t any rules in the dorms, is there?"
        s "Acknowledge my role here the same way and I’m sure things will start making a lot more sense to you."
    else:
        o "Like what?"
        s "Every third Saturday of the month, if you wait until approximately 3:00 AM and very quietly walk into any of the dorms on the first floor, you will find that room's inhabitants sacrificing a lamb."

    o "This[school] is...weird."
    s "Very much so. But you must be weird too since you’re a part of it now."

    scene otohahall3
    with dissolve

    o "Pfft. Maybe so. No one’s perfect after all."
    o "I just hope you don’t lose sight of me amidst all the huge personalities on this floor."
    s "Wait a minute...You {i}want{/i} me to be worried about you, don’t you?"

    scene otohahall8
    with dissolve

    o "Hey, there are no rules up here. I need {i}someone{/i} to worry in case anyone tries to kidnap me in the middle of the night or something."
    s "I’m glad we never went with Plan B because that would have already happened by now."

    scene otohahall2
    with dissolve

    o "Wait, what?"

    scene black
    with dissolve

    s "Later, Otoha. It was nice talking to you."
    o "Hold on! What was Plan B?!"
    o "And...what was Plan A?!"
    o "What were you going to do to me?!"
    s "Enjoy the rest of your night. Hopefully no one comes to kidnap you."
    o "Sensei! This is making me feel really weird!"

    $ renpy.end_replay()
    $ otohafirsthall = True
    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label nodokadorm1:
    play sound "knock.mp3"

    "I knock on the door and wait for someone to answer."
    "It’s my first time stopping by this room since Otoha and Nodoka moved in, and I’m curious about whether or not they’ve managed to settle in yet."
    "I know I kind of agreed to help them move, but..."
    "Well, without either of their phone numbers, it’s not like I could properly coordinate when I was going to do that."
    "I’ll just hope that everything’s been taken care of and that I don’t need to assist in any form whatsoever."

    if bonus == True:
        "The most ideal scenario would just be stumbling into a lesbian paradise."

    play sound "knock.mp3"

    "I knock again in great anticipation."

    r "Who’s there?"
    f "Rin...this isn’t your room."
    r "Oh, sorry. "
    r "Otoha, you say it."
    o "Uh...Okay."
    o "Who’s there?..."
    s "The coolest guy in Kumon-mi. "
    o "Do you guys have any idea who that would be?"
    f "That’s...obviously Sensei."
    no "I’m opening the door."
    no "It would be extremely impolite to not let Sensei experience this wondrous gathering of beautiful [young_girls]."

    if bonus == True:
        no "Quick, everyone, put your clothes back on."
        s "No. Keep them off. I will join you."
    else:
        s "Thank you, Nodoka. You are almost always so kind to me."

    scene black with dissolve
    play sound "dooropen.mp3"

    "Nodoka opens the door and waves me in."

    if bonus == True:
        "Unfortunately, everyone is clothed."
    else:
        "Thankfully, everyone is clothed."

    scene welcometodormeight1
    with dissolve

    no "Welcome to Yuritopia."

    if bonus == True:
        no "Please keep your hands to yourself at all times."
        no "You may not touch the girls, but you may touch yourself as you gaze at them."
        r "You may not."
        o "Please don’t do that."
        s "I was not planning on it."

    s "You two moved in pretty quickly, huh?"
    r "No thanks to you. "
    r "We spent like fifty percent of the move-in time just carrying all of Nodoka’s books up here."
    no "It’s confusing how they say knowledge is power when it doesn’t help you carry the objects containing said knowledge up stairs. "
    s "This issue could have been avoided if you’d only been a little more forward in giving me your number."
    no "Is that so? "
    no "I feel I’ve been plenty forward thus far."

    scene welcometodormeight2
    with dissolve

    o "Yeah...probably a little {i}too{/i} forward."
    r "Nodoka was really excited for you to show up, Sensei."
    s "Oh yeah? "

    if bonus == True:
        no "Of course. My body has been quaking with anticipation since our fated meeting in the janitor’s closet."
        o "The meeting that...never happened."
        no "My latest short story begs to differ."
        s "You...wrote a story about that?"
    else:
        no "You remind me of this one man I saw on a billboard once."
        no "It was my favorite billboard."
        s "That's nice."
        no "Have I mentioned lately that I am an author?"
        o "There she goes again, bragging about being an author."
        no "I recently published a new story titled {i}Billboard Man and the Battle Bots.{/i}"

    scene welcometodormeight3
    with dissolve

    r "I’m gonna need you to send me a link to that, please."
    o "I couldn’t even make it past the first page..."

    if bonus == True:
        no "Of course I wrote a story about that. "
        no "Sometimes, when inspiration strikes, you have to drop everything else you’re doing and really just go for it."
        no "In fact, the reason I was looking forward to seeing you so much is that I think it might be useful in helping me write even more."
        no "What sort of perverted things did we do together today, Sensei? I'll make a whole series about it."
        s "I was particularly fond of the part where we hooked up in front of everyone else here only to have them all join in moments later."
        f "Don’t give her any ideas, please..."
        f "She makes me read everything she writes and...the more characters involved, the...scarier it gets."
        no "Fear is but a mind-killer. What sense is there being scared of something that you secretly wish to experience?"
        no "Does that not dissuade you from following the path you’re already on?"
        f "I...think Nodoka might be assuming everyone feels the same way she does again..."
        r "Nodoka? Link?"
        r "Maybe just like, the name of a blog...or?"
    else:
        o "It was really fucking bad."
        r "I wanna see!"

    scene welcometodormeight4
    with dissolve

    o "I can send you some of her less...inappropriate stuff if you want. "

    if bonus == True:
        o "She’s an amazing writer when she’s not talking about closets."
        no "It appears that everyone else in the room isn’t on the same wavelength as us, Sensei."
        s "I’ve found that it’s normally just okay to assume that no one is ever on the same wavelength as me."
        no "Until now, that is."
        no "You may make use of this room as if it were your own home. "
        no "You may sleep in our beds. Dress in our clothes."
    else:
        o "She’s an amazing writer when she’s not talking about battle bots."
        r "The story was...inappropriate? How?"
        o "You'd have to read it to find out."
        s "Hey, am I allowed to take my shoes off and throw them at all of you in here? Or maybe jump on the bed?"

    scene welcometodormeight5
    with dissolve

    o "You may not do any of that."

    if bonus == True:
        no "Don’t mind her. She’s just never felt the touch of a man before."
        o "Neither has she..."
        s "I am having a hard time figuring out exactly what’s going on here."
    else:
        s "Aw shucks."
        no "Don't listen to her. Sure you can."

    no "It’s a welcome party, of course."
    s "Didn’t you guys say you were going to be listening to sad music or something?"
    s "There’s no music on and no one is doing anything. This party sucks."
    r "What are you talking about? We’re having a blast."
    s "Futaba is literally reading. "

    scene welcometodormeight6
    with dissolve

    f "It’s...it’s the last volume! And I don’t have this one yet!"
    o "Take your time, Futaba. You can borrow it if you want. "

    if bonus == True:
        no "Sensei, is your idealized version of a[teen]party just a bunch of flashing lights and underage drinking?"
        no "I didn’t realize you were so out of touch."
    else:
        no "Sensei, is your idealized version of a[teen]party just a bunch of flashing lights and drinking?"
        no "I didn’t realize you were such a boomer."

    scene welcometodormeight7
    with dissolve

    s "I just figured you’d all be doing something a little more exciting to celebrate how you’re a part of the family now."
    no "Family? Did you say family?"
    o "Nodoka...don't."
    no "I won’t. Incest without blood relation is utterly pointless anyway. Right, Sensei?"
    s "I...just meant that you’re a part of the group now. Like, the dorm family or something."
    s "I don’t know. Girls are always weirdly close with one another-"
    no "As they should be."
    s "...Girls are always weirdly close with one another, so I figured that you all would be having more fun than just sitting in a room and...waiting for me."
    no "But alas, that’s where you’re wrong."
    no "Come this way, Sensei."

    scene black
    with dissolve

    "Nodoka spins around and begins heading toward what I presume is her side of the room. "
    "It’s extremely easy to presume that on account of-"

    scene welcometodormeight8
    with dissolve

    s "You have way too many books."
    no "I do. But what is it you {i}see{/i}?"
    s "..."
    s "Way too many books."
    no "Stories, Sensei. All entirely fictitious stories."
    no "Each hiding something begging to be conveyed."
    no "If you were to open any one of these books, what do you think you’d find?"

    if bonus == True:
        no "Apart from all of the ones on the right. Those just contain orgasms and such."
        s "Wait, {i}all{/i} of the books on the right do?"
    else:
        no "Apart from all of the ones on the right. Those are just coloring books."
        s "Wait, {i}all{/i} of the books on the right are coloring books?"

    no "You heard me."
    no "Now, what do you think you’d find? "
    no "Answer the question."
    s "Just tell me the answer you’re looking for Nodoka. It’s late and I can’t be bothered to think right now."
    no "Fine. But, in exchange, you will not be earning any Nodoka points for your visit tonight."
    s "Whatever. Sure."

    scene welcometodormeight9
    with dissolve

    no "Characters, Sensei. The answer was characters."
    s "That answer was far too simple for such a misleadingly philosophical setup."
    no "Misleading philosophical setups are one of {i}my{/i} character’s lovable quirks. "

    scene welcometodormeight10
    with dissolve

    no "Now, tell me some of yours."
    s "You want me to just...tell you some of my lovable quirks?"
    no "Of course. We are at a party, are we not?"
    no "A [young_girl] and a handsome man find themselves caught up in an impromptu sidebar away from the prying eyes and ears of others-"
    no "This is the ideal territory for learning more about one another, correct?"
    f "We can still hear you..."
    r "And see you."
    o "Yeah, you only moved like five feet away."
    s "See? They’re all-"
    no "Shh. It’s “us” time now."
    no "Why not start with something simple? "
    no "Like explaining to me what you hope to find here."
    s "Here as in literally right here? Or are you being abstract again and using “here” as in human existence? "
    no "Here on the Nodoka side of the dorm room."
    s "This seems like a conversation that would be better served in private than it would surrounded by your friends."
    no "But they’re {i}your{/i} friends as well, correct?"

    if bonus == True:
        no "Or perhaps even {i}more{/i} in regard to our friends from the first floor?"
    else:
        s "Sure. I think you're all really neat."
        no "But if you could only include one of us in your Myspace top 8, who would it be?"

    r "Wait, what? "
    f "Nodoka..."
    s "I’m not sure what you’re implying, but-"
    no "You know what I’m implying, Sensei."
    o "Nodoka, chill. You’re being weird."
    no "If this is coming across as malicious or rude, I’d like to personally assure you that it’s anything but."
    no "You see, when I read books, I like to understand the motivations of the characters. "
    no "I like studying their...connections with those around them, as it better helps me immerse myself in exciting new ways of thinking."
    no "Don’t you want me to be immersed in you, Sensei?"

    scene welcometodormeight11
    with dissolve
    stop music fadeout 30.0

    if bonus == True:
        no "Would that make you feel as good as it makes {i}me{/i} feel?"
        s "Yeah, I’m not really liking this discussion in front of-"
        no "We’re not in front of anyone."
        no "We’re two people, alone at a party, with music blaring so loudly that no one will possibly hear anything the two of us say or do."
        no "What is it you want?"
        no "Look at me and tell me."
        s "..."
        no "..."
    else:
        no "Tell me about your top 8..."

    o "Whaaaaaat the fuck is going on right now?"

    "Good question, Otoha. Because I have no idea either."
    "I want to say this is some sort of test or something, but-"
    "It feels off."
    "Nodoka’s definitely been a little eccentric so far, but I didn’t exactly expect her to corner me like this in front of everyone."
    "Especially when, and this might come as a shock, I haven’t even {i}done{/i} anything this time."

    no "Sensei?"
    s "What I {i}want{/i} is to get closer to you, I guess."
    no "Just me?"
    s "Of course not {i}just{/i} you. I want to get closer to everyone."

    scene welcometodormeight12
    with dissolve

    no "Are you only saying that because the others can hear you?"
    s "What happened to no one else being able to hear us over the “blaring music?”"
    no "Right now, we’re in the grace period between songs...where the music fades out and everything grows quiet for a brief moment in time."
    s "That just sounds like a convenient response to prevent you from admitting you tripped up."
    no "God, you’re good..."
    no "Take ten more Nodoka points as a reward."
    r "Should we like...give these two some time alone or something?"
    no "Not necessary, assistant. I'd like all of you to be right here to witness anything that happens. "
    no "For as soon as I find out what it is he wants from me, the sooner I move on to finding out what he wants from all of you."
    s "Stop making it sound like I’m just...using you all to gain something."
    no "Why?"
    s "Because that isn’t what’s happening."
    no "It's not?"
    no "But there’s so much to be gained, Sensei."
    no "To max out your relationship with everyone around you would equate you to a king, wouldn’t it?"
    no "Perhaps even a god. "
    no "And who doesn’t want to be a god?"
    s "I’m perfectly fine just being Sensei."
    no "And I’m perfectly fine just being Nodoka."
    no "But that doesn’t mean I’m not a little curious about how things would look through your eyes instead of mine."

    scene welcometodormeight13
    with dissolve

    no "Besides, if the two of us need to rely on lenses to modify and magnify what we {i}do{/i} see, who’s to say that any of it is real at all?"
    no "Perhaps this entire world is nothing like either of us perceive it to be?"

    if bonus == True:
        no "If that’s true, having a god on my side seems like it would be a pretty good deal."
        no "For you too, of course, since you’d be able to force me to do all kinds of stuff."
        no "You know how gods can get without an outlet for their pent up sexual and emotional aggression."
        no "Before we know it, we’re all just fleshlights to-"
    else:
        no "Perhaps this entire world actually {i}is{/i} flat and all of those people on the Internet have been right all along."

    s "Okay, I’m going to step in now and prevent this from getting weird."
    o "It's...a little too late for that..."

    scene welcometodormeight14
    with fade

    "Nodoka steps away and rejoins the party."
    "Suddenly, everyone can hear everything again."
    "Not that they ever couldn’t in the first place."
    "An uncomfortable silence sweeps through the room as the atmosphere inflates."

    play music "sweetvermouth.mp3"

    no "So anyway, who wants pizza?"

    "And then she pokes and deflates it with the dull tip of a mechanical pencil."
    "The air leaks out slowly, but the fact that so much pressure built up in the first place is not something anyone here will easily forget."

    r "I...like pizza..."
    r "But...I think there’s something else we should talk about first."
    f "Are...you feeling okay, Nodoka?"
    f "I know you haven’t been sleeping-"
    no "Perfectly fine, childhood friend and future wife."
    no "I was just administering a little test to my new teacher to see what the likelihood of him accidentally harming any of us beautiful girls is."
    no "The results of my analysis show that he is barely harmful at all- and that we may proceed in treating him just as casually as we had been previously."
    no "Sensei, what toppings do you like on your pizza? It will be my treat for any discomfort that tirade may have caused you."
    s "I wasn’t really uncomfortable. I was just kind of confused."
    s "Normally, people {i}actually{/i} make an attempt to be alone with someone for things like that rather than just...pretending."
    no "I’m not a fan of doing things normally. But we can leave things there for the time being."
    no "Now, back to pizza."

    scene welcometodormeight15
    with dissolve

    o "Actually...pizza is cool and stuff but...would you mind helping me get a few more things from downstairs first?"
    o "My parents texted me saying they dropped some more of my stuff off a little while ago...and my arms are kind of sore from carrying Nodoka’s books."
    no "Ahh, yes. The weight of knowledge has caused me a great deal of pain as well."
    r "Do you need any more help? Maybe I could come or something?"

    scene welcometodormeight16
    with dissolve

    o "Nah, you can chill here. Sensei’s got big arms, so he’ll be able to handle most of it alone anyway."
    s "So I’m back to being a piece of meat after all."

    scene welcometodormeight17
    with dissolve

    o "That’s right. "
    o "Come on, Meat-Sensei. And thanks in advance for your help."
    no "Enjoy your trip, you two."

    scene black
    with dissolve
    stop music fadeout 10.0

    "Otoha slips her shoes back on and exits the dorm room with me. "
    "We head down the stairs but, instead of stopping at the storage room on the ground floor, she heads right for the door and walks out into the cold."
    "If I knew this was coming, I would have probably just stayed upstairs."

    $ renpy.end_replay()
    $ nodoka_love += 1
    $ nodokadorm1 = True

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

label otohadorm1:
    scene otohadark1
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    o "Welp, that was fucking weird."
    s "You don’t actually need help carrying anything, do you?"
    o "No. I don’t actually need help carrying anything. "
    o "I just figured you could probably use a break after whatever the hell that was."
    s "I take it that means you don’t have any idea either?"
    o "Not a clue."
    o "Nodoka and me have been friends for a little while but we’re not like, {i}super{/i} close or anything."
    o "Like, it was a little weird how far she went to get me to move over here in the first place."
    o "So understanding her right off the bat is kind of too much for me to be able to do right now."

    scene otohadark2
    with dissolve

    o "But if I figure anything out, I’ll be sure to let you know."
    o "She’s not really one to ever explain herself, though. "
    o "I’ve heard similar stories in the past about how she’s taken things too far and wound up causing some people to feel really uncomfortable."
    o "We can probably just chalk it up to her being a weirdo, though."
    s "Well I’m definitely used to dealing with “weirdos” by now, so one more surely won’t change anything."
    o "Hey, man. You said it, not me."
    s "You can say it too, if you want. It’s not like I’d go around telling everyone that you called them weird."

    scene otohadark3
    with dissolve

    o "No no no. That’s not what I’m getting at."
    o "Like, yeah, you’ve got a truck load of...eccentric people in your class, but I think everyone has their own reasons for acting how they do."
    o "So I don’t mean they’re weird in like, a negative way or whatever. They’re weird in the kind of way that makes them interesting to talk to."

    if bonus == True:
        s "Sure. Though, trying to have someone admit that they want to hook up with everyone in a room isn't exactly the “good” kind of weird that you’re alluding to."
    else:
        s "I think Nodoka was probably just trying to start a dance team. That sounds like a thing she would do."

    scene otohadark4
    with dissolve

    o "I think what Nodoka was doing was a little more than that, dude."
    o "I’m pretty sure she was just seeing how far she could push you without you snapping back at her or whatever."
    o "You did pretty well, all things considered. "
    o "I’m just hoping she’s not up there feeling all weird about it now. "
    s "I’m pretty sure she’s just ordering pizza. I don’t think she cares too much about the aftermath."

    scene otohadark2
    with dissolve

    o "No, but the two people she’s up there with do."
    o "And she’s also really close to Futaba, so she might feel weird if she’s suddenly uncomfortable or something."
    o "I don’t know, man. I’m not great at this whole positive reinforcement thing. "
    o "I just want to make sure things don’t get weird again once we go back up."
    s "Not even the good kind of weird?"

    scene otohadark5
    with dissolve

    o "Pfft, no. Not even the good kind of weird."

    scene otohadark6
    with dissolve

    o "Is it too much to ask to just have a chill night with my friends?"

    if bonus == True:
        o "I just got here. I’m not ready for weird[teen]drama yet. Especially drama involving some dude who’s way too old to even be hanging around us."
        o "So thanks for not admitting to manipulating the entire girls' dorm or whatever it was that we’re assuming Nodoka wanted you to do."
        o "You made my life slightly easier by holding back."
        s "No problem. I’m going to ask that you rescind your comment about me being too old, though. That hurt."
        o "Dude, you’re totally too old. I’m not rescinding anything."
    else:
        s "At this college? Yes. Things are not allowed to be normal here."
        o "Sometimes, I wish we could all just hang out and eat white bread together."

    s "Your rationality regarding this topic isn’t something I normally deal with. I don’t know if I should be relieved or offended."
    o "Be whatever you want to be. That’s what my mom always says. "

    scene otohadark7
    with dissolve

    o "As long as “whatever you want to be” doesn’t include “musician,” of course."
    s "I definitely don’t think you have to worry about me pursuing that career path any time soon."

    scene otohadark6
    with dissolve

    o "Good. Last thing I need is some old guy showing up to one of my shows and stealing my entire audience."

    "A cold breeze forms from wherever it is wind comes from (My guess is the sky, but I’m sure it’s a little more complicated than that) and attacks the two of us outside of the dorm."
    "I rarely have extended conversations out here, but...they're kind of nice in a weird sort of way."
    "The good kind of weird, obviously."
    "We left any residual “bad” weirdness upstairs with one girl I can’t understand and two that I’m starting to."
    "Is it strange that I’m not sure which of those two categories Otoha fits into yet?"
    "I want to say that I get who she is and what she’s thinking-"
    "But if there’s anything I’ve learned from my time in Kumon-mi, it’s that you can never truly know anything."

    if bonus == True:
        "I’ve also learned that having sex with [teenager]s is awesome and suddenly feel the need to remind you of that."
        "I’m sure if Nodoka could hear my thoughts, she’d be smiling right about now."

    scene otohadark8
    with dissolve

    o "Hey. So, umm...there {i}is{/i} another reason I wanted to come down here with you."
    s "Otoha, if you wanted to confess to me, it would have been a lot easier to just do it during Nodoka’s rant before."

    scene otohadark9
    with dissolve

    if bonus == True:
        o "Dude, I already told you you’re way too old. "
        o "So old that I’m asking you for advice instead of asking you to like...hold my hand or whatever."
    else:
        o "Dude, no. I just want some advice."

    s "Advice? I feel like you’re going to regret this decision."
    s "I am very bad with advice."
    o "And I’m bad with a lot of stuff. But what the hell will avoiding it solve?"
    o "Worse comes to worst, I can just blame {i}you{/i} for my life falling apart and use that momentum to write some cool midwest emo shit or something."
    o "Rin would be all about that."
    s "Yeah. I understand exactly what you’re talking about right now."

    scene otohadark10
    with dissolve

    o "Good. Because Rin’s...kind of what I wanted to talk to you about."
    s "Ahh. Yeah, I guess that explains why you didn’t want her to tag along."
    s "So much for that thing you said about not talking about people behind their back, though."

    scene otohadark11
    with dissolve

    o "Yeah. So much for that..."
    s "So, what is it you want to know about her?"
    s "I don’t mean to brag, but I’ve gotten to know her pretty well over the definitely-only-one[school] year we’ve known each other for."
    o "Weird choice of words, but I’m just kind of curious about...I don’t know. What kind of person she is, I guess?"
    s "Do you not already know what kind of person she is by now? Don’t you two talk like all day, everyday?"
    o "It’s like, 80%% Rin talking and 20%% me figuring out how I'm supposed to reply. "
    o "I get that she’s nice and has her own problems that she’s still working out or whatever, but like...I’m kind of confused, you know?"
    o "Like, didn’t she like some other girl right before me? "
    o "It’s really flattering...all of the things she says about me. But I can’t help but feel like I’m just the flavor of the month or something."

    scene otohadark12
    with dissolve

    o "There are so many parks with so many girls."
    o "If she fell for {i}me{/i} so quickly...who’s to say that won’t happen again with the next rocker chick she lays her eyes on?"
    s "No one would say that won’t happen, because it very well may."
    o "Right? So then why should I believe-"
    s "Because you’re at the part of your life where what's happening right now matters a lot more than what’s going to happen in a few weeks."

    scene otohadark13
    with dissolve

    o "Wait. I am?"
    o "I thought I was at the part of life where I {i}should{/i} be thinking about my future."
    s "That’s what most people in my position would probably tell you. I work a little differently, though."
    s "I think the best way to ensure that your future winds up being something exciting is to live freely day to day."
    s "That way, you won’t have any regrets weighing you down once you get older."
    o "Okay but like, what about gaining experience and like...furthering my education and stuff."
    s "Two sacrifices that must be made in exchange for happiness."
    o "..."
    s "..."

    scene otohadark14
    with dissolve

    o "This is very bad advice, Sensei."
    s "Hey, no one is perfect. "
    s "Point is, if you want to learn more about Rin, learn more about her by spending time with her."
    o "I’m going to, totally. I think she’s really cool."
    o "I don’t know if I want to like, {i}date{/i} her, but being around her has been fun so far."
    o "She’s just kind of..."
    o "I don’t know. A little too much for me sometimes?"
    o "She has {i}a lot{/i} of personality."
    s "True. But so does Nodoka and you two seem to be doing well so far."

    scene otohadark15
    with dissolve

    o "I can’t help but feel like I do nothing but attract loud or...strange people."
    s "Have you tried taking some of your rings off?"
    o "What...would that do?"
    s "I don’t know. Make you seem less...cool?"
    o "I hope it’s a little more than just my jewelry that makes people gravitate to me."

    scene otohadark16
    with dissolve

    o "Who knows at this point, though? "
    o "It’s gotta be {i}something{/i} weird like that if I keep attracting so many girls."
    s "To be fair, there are a lot less guys around to attract now. "
    o "Ahh, yes. When in doubt, blame it on the space war. "
    s "It wouldn’t be the first time, I can tell you that."

    scene otohadark17
    with dissolve

    o "What would you do in my shoes, Sensei?"
    s "What do you mean?"
    o "About Rin. "

    if bonus == True:
        s "Oh. Uhh..."
        s "I think the complete answer to that question would be better received by someone like Nodoka rather than you."
        s "I’m not sure you’re prepared for what I’d say."
    else:
        s "I think you should love her and cherish her forever like the good girl you are."
        o "Thanks, Sensei."
        s "I also think you should both get mohawks. That's what I would do in your shoes."

    scene otohadark18
    with dissolve

    o "Uhh...no. Probably not, if that’s the direction you’re going to take things in."
    s "Hearing what I’d do shouldn’t influence you at all anyway. Live your life how {i}you{/i} want to. Not how someone else would."
    s "Whatever you do decide on, though, be gentle with her."

    if bonus == True:
        s "And I’m not talking sexually this time because she has so much pent up sexual frustration at this point that I don’t think being gentle would-"
    else:
        s "But if you {i}do{/i} wind up wanting a mohawk-"

    scene otohadark19
    with dissolve

    o "Dude."
    s "Sorry. I couldn’t help myself."

    scene otohadark20
    with dissolve

    o "It’s fine. I’ll be as gentle as I can with...whichever direction we wind up going in."
    o "I don’t want to hurt her. But I don’t know if I can make her happy either. "
    o "If I’m going to be making my own choices now, I shouldn’t be making any that I can’t get behind 100%% of the way."
    o "It’s kind of crazy to me how quickly some people are willing to jump into things like...confessing their feelings when I can’t even figure out what mine are."
    s "You write music don’t you? Maybe you’re just...using up all of your emotions on that?"

    scene otohadark21
    with dissolve

    o "Right. Because emotions are a finite resource that you can run out of if you use too many."
    s "You joke, but what if that’s actually true?"
    o "If that’s true, this world is an extremely sad place."
    r "Oh! There you two are."

    scene otohadark22
    with dissolve

    "This world {i}is{/i} an extremely sad place."
    "If it was any sadder, we’d all shrivel up and die."
    "Which I’m sure is something we’ve all felt like doing at least once or twice."
    "Maybe even thousands of times, depending on the person. "
    "Take these two, for example."
    "They’re both smiling, are they not?"
    "Which smile do you think is harder to maintain?"
    "The one belonging to the girl who wants to love, yet doesn’t know how? "
    "Or the one that belongs to the girl who doesn’t seem to be capable of {i}not{/i} loving?"
    "The correct answer is that both smiles are impossible to maintain."
    "Because this world is miserable."
    "And smiling at all is pointless when smiles die faster than anything known to man."
    "And yet-"
    "And yet they’re still so inexplicably beautiful."
    "Maybe tonight, outside of a building filled with dying smiles, I can convince myself to not wish these ones away."

    o "Yo. Welcome to the party."
    r "Thanks for having me. "

    scene otohadark23
    with dissolve

    r "What are you guys up to? You’ve been down here for a while."
    o "Just hanging out. "
    o "I had some stuff I wanted to ask him and was afraid Nodoka was going to pounce on him if he hung around any longer."
    r "Yeah, that was weird. She seems fine now, though."
    r "You look a little happier than normal, Sensei. Did talking to Otoha put you in a good mood or something?"
    s "Me? Looking happy? Are you forgetting who I am, Rin?"
    r "Hmm...It could just be the light, I guess."

    scene otohadark24
    with dissolve

    r "Oh. We decided on pepperoni, in case you were wondering. "
    r "I’m sure that’s been on your minds since the two of you came down here so...I just thought I should come let you know and stuff."
    o "Thanks, Rin. We were about to head back up anyway, though."
    s "Nah. You two go. I’m going to head home."

    scene otohadark25
    with dissolve

    r "Wait, I didn’t mess anything up by showing up at a weird time, did I?"
    r "I was just...feeling like a third wheel up there and...wanted to be with you two instead."
    o "You don’t have to leave, Sensei. You can come back up if you want."
    s "It’s fine."

    if rindorm45 == True and rinbetrayed == False:
        s "Besides, the last time I ate pizza with Rin, something happened that I probably shouldn’t talk about."

        scene otohadark26
        with dissolve

        r "Ah! Hey!"
        r "Why are you bringing that up now of all times?!"
        s "Because it’s more fun to leave after making you flustered."
        r "Sensei! Come on!"
        o "..."

    s "Ami’s probably waiting for me at home anyway. It’s already pretty late."

    scene otohadark27
    with dissolve

    o "Ami?..."
    o "You mean...the Ami from our class?"
    o "Does that...mean what I think it means?..."
    o "I thought hanging around Rin meant you liked girls a little less...you know..."
    s "Ami is my [niece], Otoha."
    o "..."
    s "..."

    scene otohadark28
    with dissolve

    if bonus == True:
        o "I knew that!"
        o "I was just kidding anyway!"
    else:
        o "Is that supposed to explain things better?! Because it really doesn't!"

    r "..."
    s "What are {i}you{/i} looking at?"
    r "It’s...really not because of me?"
    s "It’s totally because of you."
    s "But also because of some other stuff."
    r "I...really don’t care if you stay, you know. I wasn’t trying to get rid of you by coming down here or anything."
    s "Don’t worry about it. Just tell the others that I said goodnight."
    s "And tell Nodoka to deposit whatever points I wound up earning tonight into my account. She knows the bank information."

    scene otohadark29
    with dissolve

    r "Roger that! Quest accepted!"
    o "Uhh...well, goodnight I guess?"
    o "We should...talk again sometime, if that’s cool."
    o "It’s weirdly relaxing talking to an adult who isn’t telling me to do my homework. Even if that adult is my teacher and probably {i}should{/i} be telling me that."
    s "Homework is for losers."
    s "Goodnight, you two."

    scene otohadark30
    with dissolve

    r "Goodnight! Be safe on the way home, okay?"
    o "Goodnight, Sensei. I’ll...see you in[school], I guess."

    scene black
    with dissolve2

    "I leave the dorms without the need to stomach the strange sensation that comes with sneaking around."
    "To walk down several flights of stairs in hopes of not being spotted by someone I wasn’t there to see."
    "It’s one of the very few positive sides to conversing outside rather than in someone’s bedroom."
    "And while it’s not something I expect to become a regular occurrence, it made sense this time around."
    "And I didn’t even have to carry any boxes."

    $ renpy.end_replay()
    $ otoha_love += 1
    $ otohadorm1 = True
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label nodokadorm5:
    if _in_replay:
        play music "sweetvermouth.mp3"
        scene dorm2

    play sound "knock.mp3"

    "I knock on Nodoka’s dorm and wait for her to answer."

    o "Heeeeeey! Uhh...come in?"

    "Otoha answers instead."
    "Oh well. Close enough."

    s "Why does that invitation sound so skeptical?"
    o "Well, uhh...it’s kind of hard to explain."
    o "Nodoka, I’m inviting Sensei in. Is that okay?"
    no "Huh? What? Yeah? Yeah. Yeah that’s fine. Okay."
    o "The uhh...door is open, Sensei."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I open the door with a bit more caution than normal because I’m kind of used to either being invited in or {i}not{/i} being invited in and entering anyway."
    "It’s very rarely a gray area between those two things."
    "But I suppose there are plenty of gray areas surrounding Nodoka if her talk about colors in the halls the other day says anything about the type of person she is."

    scene nodokanodokanodoka1
    with dissolve

    o "Yo..."
    no "{size=-15}It’s wrong. It’s so wrong. Wrong wrong wrong wrong wrong wrong wrong wrong wrong wrong.{/size}"
    s "Uhh..."
    o "Don’t mind her. She’s just...doing a thing."
    o "And, uhh...sorry to be the bearer of bad news, but I’m actually on my way to visit my parents so..."
    o "Either leave now or figure out how to deal with an over caffeinated and barely attentive Nodoka."

    scene nodokanodokanodoka2
    with hpunch
    play sound "thump.mp3"

    no "{size=+15}{b}FUCK!!!{/b}{/size}"
    o "Jesus, calm down. You’re going to break your desk."
    s "Is this how Nodoka writes? Or...reads? "
    s "What is she even doing right now?"
    o "No clue but...you know what they say about geniuses."
    s "Do I? Because that definitely doesn’t ring any bells."

    scene nodokanodokanodoka3
    with dissolve

    o "Well...uhh..."
    o "Okay, see ya."
    s "What? Just like that? "
    o "Yeah, my parents are literally outside waiting to pick me up."
    s "Don’t you have any tips or anything?"
    o "There are no tips on handling Nodoka. You just...do stuff and hope she goes along with it?"
    s "Well that helps a ton. Thanks, Otoha. "
    o "I’m sorry, okay? But I really have to go."

    scene nodokanodokanodoka4
    with dissolve

    o "Nodoka? I’m heading out. I’ll be back later."
    s "..."
    o "Nodoka?"
    no "Huh? What? Yeah. Okay. Bye. See ya. "

    scene nodokanodokanodoka1
    with dissolve

    o "Umm...good luck?"

    scene nodokanodokanodoka5
    with dissolve
    play sound "dooropen.mp3"
    stop music fadeout 10.0

    "Otoha, who already had her shoes on and bag next to the door, slips past me and exits the room, leaving me alone with someone who I’m not even sure knows I’m here right now."

    s "Hey. Earth to Nodoka. "
    s "You feeling okay?"
    no "{size=-15}Everything is wrong.{/size}"
    no "{size=-15}This isn’t how anyone with even a shard left of sanity within them would word this.{/size}"
    no "IT DOESN'T MAKE SENSE!"
    no "IT IS INCOMPLETE!"
    no "THAT IS THE ONLY EXPLANATION!"
    s "Nodoka?"

    play sound "static.mp3"
    scene ayhh6 with flash
    scene nodokanodokanodoka6 with flash
    stop sound
    play music "amiawake.mp3"

    no "{size=-10}Hello{/size} Hello {size=+10}Hello!{/size}"
    no "What brings you here today, Sensei?"
    s "Woah."
    s "What dimension did you wake up in?"
    no "I beg your pardon? I woke up in the same dimension as always."
    no "Is there anything I can get for you? Coffee? Tea? Coffee?"
    s "You said coffee twice."
    no "Coffee it is! Stay right there! I’ll run down the hall and make you some! You won’t even realize I’m gone!"
    s "I don’t need anything right now, Nodoka. Is everything okay?"
    no "Hm? Yeah. Yeah everything is fine. Just a little tired, you know?"
    no "Sometimes you see so many words that all the words start blending together and then before you know it you’re reading the same word over and over and over and over again."
    no "Is there anything I can get for you, Sensei? Coffee? Tea? Coffee?"
    s "I...think you might need to slow down a bit."

    scene nodokanodokanodoka7
    with dissolve

    no "No! Going slow will only slow me down! I’ve gotta go fast if I wanna speed up!"

    if bonus == True:
        no "Teach me about sex!"
        s "I’m sorry, what?"
        no "Sex! What does the penis feel like when it’s inserted into a woman?!"
        no "I keep needing to guess and don’t want to appear amateurish to male readers!"
        no "I must appeal to everyone! Anyone and everyone! Everyone and some people! But only if some people means all people! All people!"
        no "Teach me!"
    else:
        no "How many sticks of gum can you fit in your mouth?!"
        s "I’m sorry, what?"
        no "Gum! The chewy stuff! How much of it can you chew?!"

    s "How much coffee have you had exactly?"

    scene nodokanodokanodoka8
    with dissolve

    no "Coffee? Do you want coffee? I can make you coffee. I make really good coffee."
    s "..."
    s "Okay, how many fingers am I holding up right now?"

    "I hold my hand in front of Nodoka, flashing two fingers in front of her to find out if she can even see straight."
    "She doesn’t have her glasses on and her pupils are like three sizes smaller than usual, so-"

    no "Fingers!"
    s "Yes. Good. How many?"

    if bonus == True:
        no "The more, the better! Shove your whole fist in there!"
    else:
        no "All of them!"

    s "Okay, I’m calling an ambulance."
    no "Two! Don’t call an ambulance! I’m good! Really good! Super good! So good!"
    s "Are you sure?..."

    scene nodokanodokanodoka9
    with dissolve

    no "Hah..."
    no "Yeah. Yeah, I’m fine."
    no "Just...got a little riled up there for a second. Apologies if that made you uncomfortable."

    scene nodokanodokanodoka10
    with dissolve

    no "I’m ready for a normal conversation now."
    s "You definitely don’t look like you’re ready for a normal conversation."
    no "Are my eyes doing the thing again? Have the dreaded bags returned?"
    no "Have my pupils shrunk to the size of dried, aged plums?"
    s "All of the above, actually. Is this a thing that happens often?"
    no "Extremely. Though, I’m typically good at not letting people see it."
    no "I appear to have reached a point in life where this is no longer doable, though."
    no "Just one of the cons of having a roommate, I suppose."

    if bonus == True:
        no "But I get to see her in her underwear every day, so it’s totally worth looking a little unkempt from time to time."

    s "Well...as long as you’re feeling okay, I guess."
    no "Never better."
    no "Hey, do you want to go for a walk or something? Maybe somewhere far away? Like far far far far away?"
    s "Are you...trying to escape someone? Or something?"
    no "Not particularly. I just get the urge to get out sometimes, you know?"
    s "I guess."
    s "I don’t really think we should go anywhere with you looking like that, though."
    s "I doubt I’d be able to keep up with you at this rate either."

    if bonus == True:
        no "Let’s go to that sex shop you’re banned from and buy a leash for you to pull me around on!"
        no "I’d never be able to escape that way! And even if I did, I’d come running home eventually because this is where all my stuff is!"
    else:
        no "Let’s go to the local DVD store and rent Napoleon Dynamite!"
        s "This has officially gone too far."

    scene nodokanodokanodoka8
    with dissolve

    no "Hey. Do you want to write a story together? That sounds fun, right?!"
    no "Oh, shit! Have you ever done mad libs?! Let’s do that! That’ll help get the energy out! Right?"

    "Well, at least I understand why Otoha got the hell out of here as fast as she could."
    "This is already starting to get exhausting and I’ve only been here for a few minutes."

    no "Senseiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii? Let’s play a gaaaaaaaaaaaaaaaaaaaaaaaaame."
    no "Come onnnnnnnnnnnn. Play with meeeeeeeeeeeeee."
    s "What happened to having a normal conversation, Nodoka?"

    scene nodokanodokanodoka12
    with dissolve

    no "Ahh, yes. Silly me. I did say I was going to do that, didn’t I?"
    no "Woah, weird. What’s this?"
    no "Sensei, do you ever see weird stuff when you close your eyes?"
    s "When I close my eyes? Not really."
    s "Unless you’re talking about dreaming."
    no "I guess it’s like a dream but also kind of not like a dream. But still a dream at the same time. You get it?"
    s "Nope."
    s "Are you seeing something right now?"
    no "..."
    s "..."
    s "Nodoka?"

    scene nodokanodokanodoka13
    with dissolve

    no "Nope!"

    if bonus == True:
        no "All I see is my hot teacher standing there gawking at me."
        no "I’m starting to feel a little self-conscious, actually. I don’t think I’m very pretty without my glasses on."
        s "I think you’d be adorable if your eyes were the right size."
        no "That’s very sweet of you. Take six hundred Nodoka points."
        s "Woah. Are you sure? I don’t think you meant to give me that much."
        no "Do you want me to take some away? Cause that just brought you way closer to tongue wrestling me before the end of the[school] year."
        s "I will gladly hang on to them for now."
    else:
        no "All I see is the color of the air!"

    s "It would be nice if you’d go back to normal, though. This is slightly uncomfortable for me."
    no "Comfort? Is comfort an issue?"
    no "Come with me! I know just the place!"

    scene black
    with dissolve

    "Nodoka swipes a notebook off of her table and runs over to her bed, jumping onto it and landing on her stomach."
    "Her long hair falls to her sides as she props her feet up in the air and waves me over."

    if bonus == True:
        "I decide to sit at the foot of the bed instead of on it because..."
        "Well, because I’m not feeling immoral tonight for some reason."
    else:
        "I decide to sit at the foot of the bed because I am a good guy and only view Nodoka as a student."

    scene nodokanodokanodoka14
    with dissolve

    no "Is this better? Are you comfortable now?"
    no "Wait, how are you supposed to be comfortable if you’re there on the floor?"

    if bonus == True:
        no "Come cuddle and do mad libs with me."
        no "We can’t tell Futaba until you open up about your openness, though, or my chances of playing with her boobs get way lower than I want them to be."
        s "I should probably stay right here for now."
        no "Is this one of those unclear consent situations? Because I’m sure I don’t look it, but I’m perfectly competent right now."
    else:
        s "The feeling of the wood against my legs makes me feel all tingly and comfortable."
        no "Wood!"
        s "I wanna play a trivia game. Do you like trivia?"

    no "Go on. Ask me anything you can think of. I’ll give you the right answer."
    no "I’m a prodigy, remember? A genius. I’m the smartest person you know. I see everything. I hear everything."
    no "Everything’s coming up Nodoka!"
    s "If you’re so smart, what’s the square root of 23?"
    no "4.7958. Next question."
    s "What were Thoreau’s last words?"
    no "Moose! Indian!"
    no "I don’t even like Thoreau and I know that."
    no "Isn’t that more of a trivia question than an actual question, though?"
    s "Uhh...when did Toyotomi Hideyoshi die?"
    no "September of 1598 but the Council of Five Elders didn’t inform the army until a month later when they were told to withdraw."
    s "And those five elders were?"
    no "Ieyasu, Hideie, Toshiie, Kagekatsu, and Terumoto."
    no "Also want to give a shout-out to my boy Kobayakawa Takakage as the VIP sixth member that nobody ever wants to talk about."
    s "And the electron configuration for Germanium?"
    no "[[Ar] 3d¹⁰ 4s² 4p²"
    s "What the fuck are you?"
    no "That one was actually kind of tough because I almost gave you the configuration for tin, which is [[Kr] 4d¹⁰ 5s² 5p²."

    if bonus == True:
        s "I can’t help but feel like your omniscience is being wasted on sex writing."

        scene nodokanodokanodoka15
        with dissolve

        no "Hehe~ Maybe when electron configurations and dead Japanese dudes can start giving people orgasms, I’ll be a little more interested in them."
    else:
        s "See? You're not so smart after all if you're almost making mistakes like that."

    scene nodokanodokanodoka16
    with dissolve

    no "Hey, how come you’re able to come up with questions like that off the top of your head but never want to teach anyone in class?"
    s "Eh. I guess I’m the same as you in a roundabout sort of way."
    no "I wouldn’t call it roundabout. We’re both smart people who prefer to talk about not smart stuff. Done."
    s "You are significantly smarter than me, so that comparison isn’t really fair to you."
    no "I mean, you knew all the answers to those questions too, didn’t you?"
    s "Definitely not the Germanium one. You could have said literally anything there and I would have believed you."

    scene nodokanodokanodoka17
    with dissolve

    no "You cheeky little bastard, you."

    if bonus == True:
        no "Also, would you mind explaining to me why we’re not cuddling yet?"
        no "I wouldn’t have playfully hopped onto my bed if I didn’t expect you to follow suit, Sensei."
        no "And I’ve more than proved how competent I am right now, haven’t I?"
    else:
        s "Nodoka. I would like to formally ask you for a favor."

    no "What more do you want from me?"
    s "A good night’s rest maybe? You look kind of insane right now."

    scene nodokanodokanodoka18
    with dissolve

    no "Insane?..."
    no "I’m sure it’s not that bad."
    s "When was the last time you looked in a mirror?"
    no "Two days ago? Three days ago? Four? Five? Six? Seven? Eight?"
    no "I don't like mirrors very much."
    s "And the last time you slept was?..."
    no "I don’t know. I haven’t been keeping track."
    no "I get tunnel vision and lose sight of things like that rather often."
    no "I was also particularly bothered by the way the air conditioner in this room sounds, so I had to get up to punch it on several occasions throughout the night."
    no "It's so high up, though. I nearly fell off of my chair and cracked my head open."
    no "Then there was also the matter of the tag on my pajama pants bothering me, so I needed to deal with that."
    no "But neither Otoha nor I had a pair of scissors so I needed to go acquire some and-"
    s "You know, maybe it would be best if you just went on a trip to the bathroom and took a look at yourself."

    scene nodokanodokanodoka19
    with dissolve

    no "Well...if you insist."
    no "But I can’t imagine it’s nearly as bad as you’re making it out to be."

    scene black
    with dissolve

    "Nodoka hops off of the bed, leaving her notebook behind as she heads to the bathroom."
    "In the time it takes her to do that, I succumb to the desire to invade her privacy and peer into the pages I’ve been watching her absentmindedly scribble into."
    "There are no words."
    "Just childish drawings of what looks like a house."
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene nodokanodokanodoka20
    with dissolve

    no "..."
    s "I take it your trip went well?"
    no "I look like I crawled out of a well."
    no "I honestly have no idea how you’ve been able to look at me for as long as you have."
    s "I think you’re cute. Just...cuter when you don’t look like a monster."

    if bonus == True:
        no "I’d probably have sex with a monster under the right conditions."
    else:
        no "Some monsters are cute. Like Cthulu."

    s "What?"

    scene nodokanodokanodoka21
    with dissolve

    no "Just think of...all of the tentacles and..."
    s "..."
    no "..."
    no "Thank you for stopping by, Sensei."
    s "Are you feeling a little...calmer now?"
    no "Oh, not at all. I’ll probably go tonight without sleep as well."
    no "But there {i}is{/i} some solace in knowing that there’s someone else out there who can see beauty in horrible things."

    scene nodokanodokanodoka22
    with dissolve

    if bonus == True:
        no "So...if you’ll have me...I’ll be happy to continue being the girl you can flirt with in public that no one will get mad at you for since I do the same thing with everyone else."
        no "It’ll just mean a little more than normal with you than it does with them."
        no "And the tiny girl with the black hair in the back of the classroom."
        no "If you can get her to sign up for a threesome, I’d be more than happy to give you my-"
        s "Stop dragging Sana into your sexual fantasies and appreciate her for the timid angel she is."
        no "Timid angel by day. Closet nympho by night. I’m calling it now."
        s "I don’t know if you being right will upset me or elate me...but I’ll take you up on that bet."
        no "Winner has to do anything the other person says?"
        s "I feel like we both win if that’s the reward."
        no "Oh yeah? But you haven’t even heard what I’m going to make you do yet."
        s "You haven’t heard my plan either."
        no "I just admitted to wanting to have sex with a monster. I’m pretty sure I could handle whatever you throw at me."
        s "...Yeah, you probably can."
        s "Here’s hoping this bet doesn’t take the next...forever to resolve."
    else:
        s "The only beauty I see is in gardening."

    scene nodokanodokanodoka23
    with dissolve

    no "Want me to plant a seed for you?"
    s "What kind of seed?"

    if bonus == True:
        no "Maybe just warm her up a little so you can swoop in for the kill?"
        s "Please don’t do anything to her..."
        no "Fine. I’ll just stick with my dear, sweet Miss Watabe instead."
        s "Yeah. You do that, Nodoka. It’s going very well."
        no "God I want to be that skirt."
    else:
        no "Idunno. Some kind of flower maybe?"

    scene nodokanodokanodoka24
    with hpunch

    no "AH! YES! I FIGURED IT OUT!"
    s "Figured what-"

    scene nodokanodokanodoka25
    with dissolve

    no "YOU HAVE TO GO! LEAVE!"
    no "I MUST FOCUS!"
    s "..."
    s "Well, okay then."
    s "Goodnight, Nodoka."

    no "{size=-15}I see it...{/size}"
    no "{size=-15}I see everything...{/size}"

    scene black
    with dissolve

    "I exit the dorm room and make my way down the stairs, somehow knowing less about Nodoka than I did before visiting."
    "I doubt I’ll ever get to a point where I know exactly what’s going through her head, but-"
    "Well, at least it seems like an interesting place."

    if bonus == True:
        "Self-destructive, terrifying, and mildly arousing as well..."
    else:
        "Self-destructive, terrifying, and really fucking weird."

    "But certainly interesting."
    "I’m both jealous and afraid of how much time she gets to spend there."

    $ renpy.end_replay()
    $ nodoka_love += 1
    $ nodokadorm5 = True
    stop music fadeout 5.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohadorm5:
    play sound "knock.mp3"

    "I knock on Otoha’s door and wait for her to answer."
    "I’ve gotten to spend time with her at[school] and in the park before, but..."
    "The two of us haven't really gotten to be alone in her dorm without any interference from others yet."
    "Not that I expect anything exciting to happen, but she’s proven to be excitingly...normal by now."
    "And, given that I spend my life surrounded by people like Molly and Tsuneyo and Ayane and..."
    "Well, you get the point."
    "There are a lot of strange girls in my class."
    "So I shall wait patiently for this one particular outlier to answer."

    s "..."
    s "..."
    s "..."

    "I can no longer be patient."

    play sound "knock.mp3"

    s "Otoha, are you in there? "
    o "Mmph! Unn...sec!"
    s "...What?"
    o "Mngh. Sorry! I was eating."
    o "Door’s open."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I walk into the room and kick my shoes off at the door, hoping that I’ll wind up staying here for at least an hour or two so I don’t have to awkwardly put them back on after like five minutes."
    "That has happened before and it has not been enjoyable."

    scene otohapajamdorm1
    with dissolve

    o "Heeeeeey..."
    o "Isn’t it a little late for you to be coming over?"
    o "I’m already in relax-mode."
    s "You look very comfortable."
    s "And hungry."

    scene otohapajamdorm2
    with dissolve

    o "Hahah...yeah..."
    o "Nodoka’s at some bookstore with Futaba tonight and Rin’s playing some game with her other friends, so I figured I’d just...do my own thing."
    s "And your own thing is gorging yourself on doughnuts and-"
    s "Wait, is that the sausage fest?"

    scene otohapajamdorm3
    with dissolve

    o "I was curious, okay?! You made it sound so...sausagey!"
    s "Otoha’s first sausage fest...and I get to be here for it."
    s "Niki would be so proud..."

    scene otohapajamdorm4
    with dissolve

    o "Do you want something or are you just here to try and embarrass me?"
    s "Just thought I’d come see what you were up to."
    s "You look nice with your hair down, by the way."

    scene otohapajamdorm5
    with dissolve

    o "Yeah? Thank you."
    o "I really only put it up because I friggin' hate how it feels when the wind pushes it into my eyes."
    o "Surprised it’s not like, too red for you or whatever."
    s "I mean, Ami’s hair is completely red and I haven’t gotten fed up with that yet."
    o "Yeah but Ami’s hair is cute and mine is just...hair."
    s "..."
    s "Yes. Your hair {i}is{/i} hair."
    o "Yeah, see? You get it."

    "I don’t."

    scene otohapajamdorm6
    with dissolve

    o "Do you want a doughnut?"
    o "I’ll probably eat all of them if you don’t take any and I don’t think my body will like that very much."
    s "No. But your heart will."
    o "What does that even mean?"
    s "It means that you should do whatever makes you happy. And if that means eating a box of doughnuts and two pounds of sausage noodles, so be it."
    o "Welp, I did pay for all of it...so I might as well go to town."
    o "Oh hey, are you good with technology by any chance? Because I can’t get this stupid TV to listen to me."
    s "What’s going on?"
    o "It’s just not doing anything when I press any of the buttons."
    s "Maybe the remote is dead?"
    o "The buttons on the TV aren’t working either. It’s just stuck on some weird picture."
    o "I think it might be frozen."
    s "Have you tried turning it off and back on?"

    scene otohapajamdorm7
    with dissolve

    o "Just tell me you’re not good with this kind of stuff if you’re going to keep giving me generic tips."
    s "Hey, you would be surprised how many things can be fixed by turning them off and then back on."
    o "I {i}have{/i} tried that, Sensei. It’s just-"
    o "You know what? Never mind. I’ll just keep myself entertained by talking to the old guy in my room like everyone else does here."

    "I somehow manage to defeat a magical rectangle in the battle for a [young_girl]’s attention."
    "I ascend."

    s "Couldn’t you have just played with Rin and the other girls? I’m pretty sure they’re right next door since Molly is like, the leader of their...game group or whatever."
    o "I would have, but Rin seemed weirdly against me coming for some reason."
    o "I’m not that close with any of the others yet anyway. She probably just wanted to avoid things being awkward."

    "Or she wanted to avoid you thinking she’s a nerd...which sounds a lot closer to what Rin would do if she’s approaching Otoha the same way she approached Chika."

    s "The game they play is kind of weird anyway. We’re better off in here."
    o "Is it like, a video game or something?"
    s "Not really. They all have these weird sheets of paper and talk in strange voices to one another."

    scene otohapajamdorm8
    with dissolve

    o "Huh."
    o "Well that definitely doesn’t sound like any game I’ve ever played before."
    s "Like I said, we’re better off in here where-"

    scene otohapajamdorm9
    with hpunch

    mo "SEVEN VIOLET FUNGUS APPEAR! ROLL FOR INITIATIVE!"
    r "Molly! Shh!"
    s "..."
    s "Like I was saying, we’re better off in here where it’s safe."

    scene otohapajamdorm10
    with dissolve

    o "I guess you’re right."
    o "Besides, I've barely eaten all day...so I should probably do that now anyway."
    s "Well you...certainly have the required materials to do just that."

    scene otohapajamdorm3
    with dissolve

    if bonus == True:
        o "I’m a growing girl, okay?! And if I don’t eat balanced meals, I’ll wind up looking all tired and dead inside like that one teacher Nodoka has the hots for!"
        o "The one that isn't you! The girl one! With the skirt!"
    else:
        o "I like food, okay?! And this is a perfectly balanced meal!"

    s "What exactly is {i}balanced{/i} about your dinner, Otoha?"
    o "It’s got all the food groups! Sausage, pastry, soda! Come on, man!"
    s "Oh..."
    s "You have no idea what to do now that you have to provide food for yourself, do you?"

    scene otohapajamdorm11
    with dissolve

    o "Well I obviously don’t think those are the real food groups, but...yeah."
    o "I’m used to my parents making dinner for me...so I’m stretching my wings and eating stuff that makes me happy instead of...green stuff."
    s "You poor, lost soul."
    s "I’m sure I used to be just like you until I acquired a [niece]."
    o "Oh, yeah. Let me just go out and get one of those really quick. Great advice."

    if bonus == False:
        s "It really is, though. They are very helpful."

    scene otohapajamdorm9
    with hpunch
    play sound "phonering.mp3"

    o "Ahh!"

    stop sound fadeout 5.0

    s "..."
    s "It’s just your phone, Otoha."
    s "You don’t actually get scared that easily, do you?"

    scene otohapajamdorm12
    with dissolve

    o "Of course not! I just...wasn’t ready for that."
    o "It surprised me."
    s "So what you’re telling me is you...got scared."
    o "Shut up. I’ve gotta take this."
    o "Hold your ears closed and...don’t listen to what I say in case it’s some...super secret business or something."
    s "Right..."

    scene black
    with dissolve

    "Otoha grabs her phone and hops off of the bed, nearly killing the sausage fest in the process."
    "Instead of exiting the room, which is what I expected her to do on account of telling me not to listen, she takes a seat on her stool and answers the call."

    scene otohapajamdorm13
    with dissolve
    play sound "phonebeep.wav"

    o "Hello?..."
    o "..."
    o "Yeah. "
    o "Yeah. I’m eating fine."
    s "You fucking liar."

    scene otohapajamdorm14
    with dissolve

    o "Shh!"

    "Otoha shushes me and whatever object has taken the place of my heart skips a beat."

    scene otohapajamdorm15
    with dissolve

    o "Huh?!"
    o "What?!"
    o "No! You didn’t hear a boy just now! That was the TV!"
    o "..."
    o "No, it really was! Listen!"

    scene otohapajamdorm16
    with dissolve

    o "{i}Help me...{/i}"
    s "..."

    "I decide to help Otoha by mimicking my favorite television program."

    if bonus == True:
        s "Take that, you little slut."
    else:
        s "BUT THIS GRILL IS NOT A HOME. THIS IS NOT THE STOVE I KNOOOOOOOOOW."

    scene otohapajamdorm17
    with hpunch

    o "Sorry! My roommate just changed the channel on accident! I’m leaving the room now!"

    if bonus == True:
        "My favorite television program is highly pornographic, by the way."
    else:
        "My favorite television program is Spongebob Squarepants."

    o "No! I’m doing totally fine! I don’t need any money!"
    o "..."
    o "Yeah. Yeah,[school] is great."
    o "..."
    o "My teacher?"
    o "Well, uhh..."

    scene otohapajamdorm18
    with dissolve

    o "He could be better."
    s "What the fuck?"
    o "Yeah..."
    o "Yeah."
    o "Okay."
    o "Love you too. Bye."

    play sound "phonebeep.wav"
    scene otohapajamdorm19
    with dissolve

    o "..."
    s "..."
    s "How was your phone call?"
    o "I invite you...into {i}my{/i} home...and offer you one of {i}my{/i} doughnuts..."
    o "And {i}this{/i} is how you repay me?"

    if bonus == True:
        o "By mimicking a porno?"
    else:
        o "By singing a song from Spongebob?"

    s "It has normal scenes as well. I just chose one of the racy ones."

    scene otohapajamdorm20
    with dissolve

    if bonus == True:
        o "That was porn! I know porn when I hear it!"
    else:
        o "I know how Spongebob works!"

    s "Do you?"
    o "Yes but don’t misinterpret that!"

    if bonus == True:
        s "There’s really only one way to interpret that, Otoha."
    else:
        s "But how would I even-"

    o "Sensei! That was my mom! You can’t just yell things like-"

    scene otohapajamdorm21
    with hpunch

    mo "Oi! Quiet down in there! There are other people on this server, you know?!"
    o "Ah! Sorry! Sorry!"

    scene black
    with dissolve

    "Otoha throws her phone onto the bed, once again almost killing the sausage fest, before moving past me and sitting back down."
    "Just...this time, she looks a lot less pleased with me than she did when I first arrived."

    scene otohapajamdorm22
    with dissolve

    o "..."
    s "..."
    o "If this is what having an older brother is like, I’m glad I was born an only child."
    s "Oh come on. I’m sure that one day we’ll look back on this and laugh about it."
    o "Yeah. Totally. I can hear it now. "

    if bonus == True:
        o "“Hey, remember when you called me a little slut while I was on the phone with my mom?”"
        o "“Hahaha. So funny.”"
        s "In my defense, I was not calling {i}you{/i} a little slut. It was a line from the-"
        o "Sensei..."
        s "..."
    else:
        o "IT'S JUST A GREASY SPOOOOOOOON."
        s "{size=-15}without yooooouuuuuuuu..."
        o "..."
        s "..."

    s "Am I...in trouble?"
    o "Yes."
    o "Seriously. Don’t do stuff like that."
    o "It’s nothing short of a miracle that I was even allowed to come live here."
    o "One wrong move and that could all come to an end. My parents know the address of this place and they could come get me at any moment."
    s "Oh great. I’m sure that’s not an omen for them to show up at the worst possible time in the future."
    o "There won’t {i}be{/i} a future if you keep doing stuff like that."

    scene otohapajamdorm23
    with dissolve

    if bonus == True:
        o "I’ve obviously come around to hanging out in here with you if we're both bored, but please don’t do things that will make my leash even tighter."
        s "Just take the leash off entirely and stop answering them."
    else:
        o "They're the ones paying my tuition. I can't just...not listen to them anymore."
        s "Just kill them."

    scene otohapajamdorm24
    with dissolve

    o "Dude, no. They’re still my parents."

    if bonus == True:
        o "Just be respectful and stay away from sex jokes while I’m talking to them. That’s all I want."
    else:
        o "Just be respectful and don't sing Spongebob songs around them. That's all I want."

    o "And maybe 1,000 yen. That would be cool too."
    s "You and this damn 1,000 yen. I literally just heard you tell your mom you didn’t need any money."

    scene otohapajamdorm25
    with dissolve

    o "Doesn’t mean I don’t {i}want{/i} any. Pay up, Sensei. It’s a fine for being a jerk."
    s "I’ll give you 1,000 yen...but I need the doughnuts in return."

    scene otohapajamdorm26
    with dissolve

    o "Wait, all of them?!"
    o "I thought you didn’t want any!"
    s "It’s for your own good, Otoha. "
    s "Besides, once you try the sausage fest, you’ll never want to eat anything else ever again."
    o "I already had a few bites."
    o "It’s...extremely average."
    s "{i}How dare you...{/i}"

    scene otohapajamdorm27
    with dissolve

    o "Ugh. Keep your money. I’ll just eat my doughnuts and watch this weird picture of a house until-"

    scene otohapajamdorm28
    with dissolve

    o "Oh. The TV went back to normal."
    o "When did that happen?"
    s "Beats me. I’m glad things worked out, though."
    s "I was starting to think I may have ruined your night."
    o "You did ruin my night, but I signed up for that when I invited you in."
    s "I like this. This is good."
    o "Like what? What’s good?"
    s "Us. You don’t let me walk all over you but you aren’t extremely abrasive in telling me to stop."
    o "Yeah, I just think you’re really annoying."
    o "Now shush. I’m gonna watch TV and eat junk food all night and you can either hang out and deal with that or just get out."
    s "Understood. Move over."

    scene black
    with dissolve2

    "I take a seat next to Otoha and {i}do{/i} ultimately receive a doughnut."
    "She manages to finish the other three as well as the entire sausage fest, and I suddenly feel the urge to visit Maya and inform her that there may be someone else in the class who is just as good at eating as her."
    "I don’t, though."
    "Instead, I hang out and watch some reality show with Otoha until Nodoka gets home."
    "It was a surprisingly refreshing night, all things considered."

    $ renpy.end_replay()
    $ otoha_love += 1
    $ otohadorm5 = True
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

                    ############################################
                    ##########        ROOM 9         ###########
                    ############################################

label toukadorm:
    if touka_love >= 1 and day != 4 and toukafirsthall == True and toukadorm1 == False:
        jump toukadorm1
    if touka_love >= 5 and day != 4 and toukastreets5 == True and toukadorm5 == False:
        jump toukadorm5
    if touka_love >= 10 and day != 4 and christmastwo20 == True and toukadorm10 == False:
        jump toukadorm10
    if touka_love >= 25 and toukaarchery20 == True and toukadorm25p1 == False:
        jump toukadorm25p1
    elif day304 == True and toukafirsthall == False:
        "I don't think Touka is ready to spend time with me in her room just yet."
        jump doorknock2
    else:
        jump toukadormgen

label toukahall:
    if toukafirsthall == False:
        jump toukafirsthall
    else:
        jump toukahallgen

label yasudorm:
    if yasu_love >= 10 and yasufirsthall == True and toukadorm5 == True and makotowinterbeach4 == True and yasudorm10 == False:
        jump yasudorm10
    if yasu_love >= 20 and church20 == True and day != 2 and yasudorm20 == False:
        jump yasudorm20
    if yasu_love >= 25 and yasudorm25 == True and day != 2 and yasudorm30 == False:
        jump yasudorm30
    elif day304 == True and yasudorm10 == False:
        "I don't think Yasu is ready to spend time with me in her room just yet."
        jump doorknock2
    else:
        jump yasudormgen

label yasuhall:
    if yasufirsthall == False:
        jump yasufirsthall
    else:
        jump yasuhallgen

label toukadormgen:
    play sound "knock.mp3"

    to "Come in!"

    scene toukadormgen
    with fade

    "I decide to spend the night hanging out in the dorm with Touka."
    "Despite the place being light years beneath her standards, she doesn't particularly seem to {i}hate{/i} things here."
    "Granted, she spends most of her time either alone or on video calls with different instructors to make up for my inadequacy as a teacher-"
    "But she hasn't asked for a transfer or gotten me fired yet, so that is a clear plus."

    scene black
    with dissolve

    "Eventually, she moves on to talking about her family's business and I can't help but begin to lose interest."
    "Her cuteness may get her far in life, and her great wealth may get her even further-"
    "But it will not get her to the point where she can talk about boring stuff without risking my interest."
    "And, obviously, I need to be the center of her affinities because this is a world made for me."

    if bonus == True:
        "I convince Touka to leave her family and become my sex slave. She obliges and, within moments, we are naked."
    else:
        "I convince Touka to leave her family and open up an Arby's with me."

    "Just kidding."
    "I never convince her to do any of that and, instead, decide to just head home."
    "But at least the two of us managed to get a little closer."

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka's affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label yasudormgen:
    play sound "knock.mp3"

    ya "Come in!"

    scene yasudormgen
    with fade

    "I decide to spend the night hanging out in the dark with Yasu."
    "I ask her to turn the lights on because I feel incredibly uncomfortable just watching her stand there smiling, but she refuses."
    "Apparently, even artificial light stings her eyes and it isn't just the sun that manages to do that."
    "My discomfort grows, but is quelled by the fact that, unlike some of the other residents of this dorm, she does not possess any weapons."
    "That being said, I absolutely would not be surprised if there were some weird religious ritual tools tucked away under her bed or something like that."

    scene black
    with dissolve

    "I make it through the night without dying, which is a thing a lot of unfortunate people out there aren't able to say."
    "Yasu probably makes it through the night without dying as well, but I can't say that definitively as I'm not there to watch her fall asleep."
    "For all I know, she could be sacrificing herself right now in the name of her god."
    "But I'm just going to assume that doesn't happen and hopefully run into her again tomorrow."

    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu's affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label toukahallgen:
    if chapthreeactive == True:
        scene toukasummer2hallgen
        with dissolve
    else:
        scene toukahall1
        with dissolve

    to "Good evening, Sensei."
    to "Please make no sudden movements or I will call the police."
    s "What kind of person do you think I am?"
    to "The worst kind. But I will still allow you to talk to me as there is a witness in the hall."
    i "Uhh...please leave me out of this."

    scene black
    with dissolve

    "I spend some time in the hall with Touka, trying to convince her that I am not the scum of the earth."
    "It does not work and I go home without making any sort of substantial impact on her life."
    "But at least her affection goes up."

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka's affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yasuhallgen:
    if chapthreeactive == True:
        scene yasusummer2hallgen
        with dissolve
    else:
        scene yasuhall1
        with dissolve

    s "Hey, Yasu. What are you up to tonight?"
    ya "Basking in the warmth of the second dorm floor, absorbing the vibrations that crawl up the sides of the building and-"
    s "That's nice. Do you want to hang out for a little while?"
    ya "Do you have a moment to hear about our lord and savior?"
    s "I have a moment to hear about other things. Not really that, though."
    ya "How sad. What better night than tonight to be saved?"

    scene black
    with dissolve

    "I do not wind up {i}being saved{/i}, but I do wind up killing time with Yasu in the hall."
    "Or, I'm sorry- Time winds up moving onto the second plane of existence because death is not real."
    "Regardless, the two of us make idle chit chat that scares Kirin back into her room and, before long, Yasu and I part ways."
    "I head home just as confused as I always am after talking to her."

    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu's affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label toukadorm1:
    if _in_replay:
        play music "sweetvermouth.mp3"
        scene dorm2

    play sound "knock.mp3"

    "I knock on Touka’s door and wait for her to answer."
    "I’ve already made it known that I routinely drop by everyone’s rooms and, tonight, the lucky recipient of my highly demanded company is her."
    "Which is not to say I imagine she wants it or anything."
    "In fact, I’m sure a good portion of this visit will just involve her complaining about her roommate."
    "But her complaints can only last so long. And I am determined to make this room yet another home away from home for me."

    to "H...Hello?"
    to "Who goes there?"
    s "I go here. It’s me."
    to "Sensei?"
    to "If I let you inside, may I proceed to angrily vent at you in a rather unladylike manner?"

    if bonus == True:
        s "That directly depends on how much clothing you are wearing."
        to "I am wearing all of my clothes. And I greatly appreciate you asking to be sure you don’t walk in on me looking anything less than appropriate."
        s "Yes. That is exactly why I was asking. I am a good guy."
        to "You...have your moments."
    else:
        s "Yes. I am always here to help."

    play sound "lock.mp3"

    to "You may enter, Sensei. But please do not make a mess of the place. The maid just left for the night."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "...Maid?"

    "Touka unlocks the door before letting me in and I can’t help but think of how far the two of us have come in just the short time we’ve known each other."

    scene toukafirstdorm1
    with dissolve

    s "This is nice."
    s "I feel like it was just the other day you were trying to get me fired. "
    s "Now look at us, bonding in your bedroom."
    to "Please don’t steer this conversation into a strange direction or I absolutely {i}will{/i} have you fired."
    to "You are only here today because I wanted someone to complain to and have an admittedly hard time bonding with those beneath me."
    s "What happened to not placing yourself above others?"

    scene toukafirstdorm2
    with dissolve

    to "I meant the first floor, which is directly beneath this one."
    s "Typical Touka, always thinking she’s on a higher level than everyone around her."

    scene toukafirstdorm3
    with dissolve

    to "Stop it! I’m referring to the actual vertical distance between the second floor and the first!"
    to "I invited you in to get rid of my bad feelings and you’ve gone and created even more of them! Apologize!"
    s "I’m sorry, Tsukiko."

    scene toukafirstdorm4
    with dissolve

    to "Why do I bother continuing to let you talk to me when I could have you assassinated in a matter of minutes?"
    s "Wait, what?"

    scene toukafirstdorm5
    with dissolve

    to "Anyway, I’m glad you showed up when you did. I was beginning to feel rather uncomfortable."
    to "Please direct your attention to the left hand side of the room."
    s "Hold on, what was that about having me assassinated?"
    s "That's not a thing you can just ignore."
    to "I have no idea what you are talking about."
    s "That’s-"
    s "Wait, what’s happening on the left hand side of the room?"

    scene toukafirstdorm6
    stop music
    $ renpy.pause(10, hard=True)

    play music "sweetvermouth.mp3"

    s "Uhh..."
    s "What is she doing?"
    to "I have no idea. She has been sitting there ever since we got back home and will not speak a word to me."

    scene toukafirstdorm7
    with dissolve

    to "Am I going to die tonight?"
    s "Probably not."
    s "Have you two been getting along any better?"

    scene toukafirstdorm8
    with dissolve

    to "Does it look like we have been getting along any better?"
    s "It doesn’t look like you {i}haven’t{/i}."
    s "Is this what you wanted to vent about?"

    scene toukafirstdorm9
    with dissolve

    to "I suppose so. Though I will admit that it is infinitely better than hearing her whisper to her dry erase board at 3:00 in the morning."
    to "She gave up on turning the lights off too, so that is a plus."
    s "Yeah. Huge improvement, I’m sure."
    to "It will probably be best if we just pretend she is not there and carry on with the conversation topic I chose for us upon your arrival."
    s "Sure. And that topic is?"

    scene toukafirstdorm10
    with dissolve

    to "You, of course."
    s "Did you really invite me into your room so you could vent about me {i}to{/i} me?"
    to "Well I can not vent to Yasu while she is pretending to be a chair."
    s "Right. And everyone else is below you."
    to "In terms of physical verticality, yes. They are."
    s "And the rest of the girls on this floor?"

    scene toukafirstdorm11
    with dissolve

    to "I attempted to have a conversation with the green-haired girl and it...did not go very well."
    to "So I returned to my room to simply wait for the day to end so I can try again tomorrow."
    s "Unfortunately, you picked the one girl on this entire floor that just doesn’t want to talk to anyone."
    s "I’m sure it wasn’t personal."
    to "Well it certainly {i}felt{/i} personal."
    to "I have realized as of late that I am no stranger to accidentally offending people, but I didn’t know that simply saying hello was enough to warrant such unbecoming glares."
    s "Yeah, she does that. Just move on and try someone else."
    s "Even though they’re both {i}below{/i} you, Ayane and Chika don’t seem to have a problem talking to you."
    to "No, they do not. But they are also always doing things and I am never doing anything."
    to "Alas, I remain alone in a half filled room talking to my teacher because I am too fearful to show my face in the hall again."
    s "I’m sure you’ll get over it in a second when you remember you called me in here to complain about me."

    scene toukafirstdorm12
    with dissolve

    to "Oh, right! Thank you kindly for reminding me!"
    to "You are a bad man!"
    s "You’re welcome and I know."
    s "What did I do this time?"
    to "Knowingly invited me to live in a room with a crazy person!"
    s "You’re still going on about that? Whatever happened to bonding over horses and dead people?"
    to "I showed Yasu a picture of my favorite horse when we returned to the dorm that night and she proceeded to maniacally laugh for five whole minutes!"
    to "I still do not understand why!"
    s "Maybe it was a funny looking horse?"
    to "It’s a beautiful black Misaki and cost my family an absolute fortune!"

    if brony == True:
        if bonus == True:
            s "Damn. That's not even the kind that I'd want to have sex with."
            to "What?!"
            s "Nothing."
        else:
            s "Hot."
            to "What?!"
            s "Nothing."

    s "I have no idea what that means but, I’m sure it was funny looking if it made Yasu laugh for five minutes."

    scene toukafirstdorm13
    with dissolve

    to "Sensei...You probably do not understand this as you don’t sleep in the same room as her, but Yasu is very much not a run of the mill commoner."
    s "You really don’t have to live with her to figure that out."
    to "Then why would you subject {i}me{/i}, of all people, to the brutal test of willpower that is befriending her?"
    s "If you don’t like it, why not just go stay in the spare house your parents bought you when you transferred[school]s?"

    scene toukafirstdorm14
    with dissolve

    to "Because...sleeping in a house alone is scary..."
    s "Oh, right. You’ve been coddled forever, so of course you wouldn’t be used to something like that."

    scene toukafirstdorm15
    with dissolve

    to "Can you stop implying that all of these flaws of mine are the result of selfishness or conceit and instead acknowledge that I might just be genuinely confused?"
    to "I am a fish out of water here and expect special treatment {i}not{/i} because I see myself as a superior being, but because I {i}need{/i} it."
    to "So yes, I apologize dearly, but I am very mad at you as the man who is now at least partially responsible for the woman I will ultimately become one day."

    if bonus == True:
        "Unfortunately for Touka, that day will never come."
        "But I suppose that I have been a little harsh to her ever since she arrived when she clearly {i}is{/i} trying."

    s "Fine, yeah. I get it. You’re abnormal."
    s "But if you’re going to vent in an “unladylike manner” like you said before, you should avoid saying things like “I apologize dearly” and just really lay into me."

    scene toukafirstdorm16
    with dissolve

    to "Lay into you?"
    to "As in...threaten your job and your well being as I’ve been doing in[school]?"
    s "No. Like say actual mean things to me about the kind of person you think I am."

    scene toukafirstdorm17
    with dissolve

    if bonus == True:
        to "Wait...you are not some sort of...masochist, are you?"
        to "Do you enjoy when powerful women say mean things to you? My mother has told me about those types of men before."
        to "I don’t think I’m comfortable-"
        s "First off, I’m not a masochist."
        s "Second, what could have possibly compelled your mother to tell you about things like that?"

        scene toukafirstdorm18
        with dissolve

        to "It was part of a twelve hour briefing I was given on things I may encounter in what my father referred to as “the wilderness.”"
        to "According to my mother and the presentation the family put together, there are these things called “fetishes” that somehow provide pleasure to...certain types of people."
        to "Could it be that...this whole time...you’ve been provoking me for your own satisfaction?"
        s "I..."
        s "I don’t think so, but...you know, at this point, I wouldn’t be surprised if there was some element of truth to that."

        scene toukafirstdorm19
        with dissolve

        to "This causes a great deal of stress for me as I will no longer be able to belittle you without the fear of you becoming...excited."
        to "I find myself belittling you quite often, so please suppress your desires until after we are married."

        scene toukafirstdorm20
        with dissolve

        to "N-Not that I would ever consider marrying a masochistic commoner like you!"
        s "Careful, Touka. Yelling at me like that might have some...adverse effects."
    else:
        s "I probably deserve it anyway."
        s "I am a bad man."
        to "What have you done now?"
        s "I stole a piece of Ami's gum while she was asleep this morning."
        to "Sensei, how could you?"
        s "I am a bad, bad boy."
        to "I do not know what to say."
        s "You can show me the rest of the room. Just hide any gum first if you know what is good for you."

    scene toukafirstdorm21
    with dissolve

    to "Oh...right."
    to "Apologies..."
    to "I...umm..."
    to "Please follow me for the rest of the tour."

    scene black
    with dissolve

    "Touka somehow switches into tour guide mode, probably being desperate for a topic change and realizing that she hasn’t shown me around since I entered."
    "Not like there’s much to show me anyway, but-"

    scene toukafirstdorm22
    with dissolve

    s "Wait, hold on. Why do you have a love hotel bed?"

    scene toukafirstdorm23
    with dissolve

    to "What is a love hotel?! It sounds romantic!"
    s "It’s a hotel made for the express purpose of having sex."
    s "This is the exact type of bed they use."
    to "..."

    scene toukafirstdorm24
    with dissolve

    to "You are lying to get a rise out of me again, aren’t you?"
    to "This is the same type of bed I have been using since I was little."
    to "My mother would never knowingly allow me to sleep in something that...filthy!"
    s "Knowingly, no. But your mother hasn’t seemed to be the most...worldly person so far either."
    to "Nonsense, she is fluent in seven languages. That is plenty worldly."
    to "This is just one more trick out of the many you’ve had the pleasure of playing on me thus far."
    s "Does the bed ever vibrate?"

    scene toukafirstdorm25
    with dissolve

    to "Yes, but...that just means it is set to...sleep mode."
    s "Touka, it’s a bed. It is literally always in sleep mode."

    if bonus == True:
        s "The vibrating is for sex stuff."
    else:
        s "The vibrating is for other stuff."

    scene toukafirstdorm26
    with dissolve

    to "No, it is not! I’m not falling for that! It is a high quality, imported bed with...rapid sleep mode technology!"
    s "There’s a rapid sleep mode now?"
    to "For when sleeping just isn’t fast enough!"

    scene toukafirstdorm27
    with dissolve

    to "You wouldn’t know because you can’t afford one."

    if bonus == True:
        s "Sure I can. In fact, for just 3,000 yen, I can rent one downtown and-"
    else:
        s "That was a low blow, you big jerk."

    scene toukafirstdorm28
    with dissolve

    to "Yasu! Are you done being a chair yet?! I am cornered by an intimidating man and require your assistance!"
    s "How is Yasu going to help? She has the constitution of a decrepit old woman."
    to "Mother?! Yumi?!"
    s "{i}Yumi?{/i}"

    scene toukafirstdorm29
    with dissolve

    to "I ran out of people I rely on and inadvertently began to list people I find intimidating."
    to "If you hadn’t stopped me, I would have likely called out for your assistance next."
    s "Wait, does that mean you find Yumi more intimidating than me?"

    scene toukafirstdorm30
    with dissolve

    to "Yumi has not sworn to protect me and guide me through life while you have. She is clearly more intimidating to me than you are."
    s "If you think {i}she’s{/i} intimidating, you should see her mother."
    to "Will she be attending the next parent teacher conference?"
    s "I don't really do those. And even if I did, no. She would definitely not be there."

    scene toukafirstdorm31
    with dissolve

    to "If you do not hold parent teacher conferences, how are my mother and I to know if my performance is adequate or not?"
    s "What performance? All you do in class is sit around."
    to "That isn’t true. Your assistant actually just gave me a batch of personalized worksheets meant to help with my studies as your methods have not...clicked for me just yet."
    s "Makoto did that?"
    to "Yes, Makoto. That was her name."
    to "I was under the assumption it was a thing she did for everyone, what with being your assistant and all."
    s "I honestly had no idea."
    to "Well...regardless, how will you be informing my mother and myself of my progress?"
    to "Do we need to arrange for a personal meeting or something of that nature?"
    s "How about I just...send you an email with a thumbs up or something?"

    scene toukafirstdorm32
    with dissolve

    to "An...email?..."
    to "That’s hardly sufficient, Sensei..."
    to "Your methods sound less and less rational every time you speak about them."
    s "Yeah, well...you sleep in a love hotel bed, so there’s not a lot about you that screams “rational” either."

    scene toukafirstdorm28
    with hpunch

    to "FOR THE LAST TIME, IT’S A NORMAL BED! AND IT’S VERY COMFORTABLE!"

    if kirin_virgin == False and bonus == True:
        s "Just don’t let Kirin see it or she might get a little excited."
        to "I CAN’T EVEN REMEMBER WHICH GIRL THAT IS! THERE ARE SO MANY OF THEM!"
        s "If you want, I can go see if she can come over here to confirm-"

    elif kirin_virgin == True and bonus == True:
        s "Is it? Maybe I’ll scrounge up a spare 3,000 yen and go check one out after-"

    else:
        s "Yeah, it looks it."

    to "OH, WOULD YOU LOOK AT THE TIME? I HAVE A...ZOOM CALL WITH MY CROCHET INSTRUCTOR, SO IT IS TIME FOR YOU TO LEAVE!"
    ya "Crochet? Can I try, Touka?"

    scene toukafirstdorm33
    with dissolve

    to "Oh, Yasu! How nice of you to finally join the conversation! Did you enjoy being a chair?!"
    ya "I felt God’s hands on my shoulders. They were so light and-"
    to "Wonderful! Let us crochet together, then!"
    to "Goodnight, Sensei!"

    scene black
    with dissolve2

    "Touka quickly pushes me out of the room...and is surprisingly quite strong."
    "Of course, I don’t bother fighting back because A: she is a girl. And B: she is a girl."
    "So I accept defeat for the time being, having just satiated my lust for awkward rich girl content, and begin my walk home through a suddenly heavy snowfall."
    "Or, at least I start my walk home."
    "Touka wound up sending a driver to pick me up just two or three blocks along."
    "I have no idea why she did that or how it managed to get here so quickly, but I accept the ride and find myself back at home within a matter of minutes."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukadorm1 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label toukafirsthall:
    if _in_replay:
        play music "sweetvermouth.mp3"

    scene toukahall1
    with dissolve

    to "Good evening, Sensei. Do you have some sort of business in the girls’ dorm?"
    s "Hey. Nope. I’m just here to hang out."

    scene toukahall2
    with dissolve

    to "Hang out? Forgive me if I’m misunderstanding the full meaning of this popular common phrase, but wouldn’t that imply you are here for the express purpose of being around [young_girls]?"
    s "Yes. It would."
    to "I see."
    to "And forgive me if I am misunderstanding even more, but wouldn’t that imply that you have some rather unfavorable affinities for a man of your age?"

    if bonus == True:
        s "Again, yes. Yes it would."
    else:
        s "No. I just like hugs."

    to "I see."
    s "You’ll get used to it. I'm sure it will feel totally normal in no time at all."
    to "I..."
    to "I don’t think that it will."
    s "Either way, what are you up to tonight?"

    scene toukahall3
    with dissolve

    to "Well, I suppose I’m trying to understand exactly what I’m supposed to be doing here."
    to "It isn’t often that I have entire nights to myself and, somehow or another, I found myself feeling compelled to stand out in the hallway."
    to "Part of me wants to try greeting the dejected looking girl slouched up against the wall, but she does not seem to want to be bothered."
    s "I can tell you with absolute certainty that she definitely does not."
    s "But on the bright side, you have me now. And I am extremely exciting and only mildly suspicious."

    scene toukahall4
    with dissolve

    to "That sounds a lot like something a suspicious person would say."
    s "I don’t think so. A really suspicious person probably wouldn’t say anything. "
    s "They’d just stand there and stare at you, probably from around a corner or something."

    scene toukahall5
    with dissolve

    to "How bold of you to not utilize a corner at all and instead approach me with your suspicious behavior directly!"
    to "You are truly a man to be feared!"
    s "Again, you’ll get used to it and it will feel totally normal in no time at all."

    scene toukahall6
    with dissolve

    to "I somehow find the second utterance of that sentence even more disturbing than the first."
    to "So...go on. Out with it. What do you want or need from me tonight?"
    s "I already told you, I’m just here to hang out. I’m going to do that from time to time now that you live here."

    scene toukahall2
    with dissolve

    to "I understand that, but isn’t there some sort of objective you have in mind?"
    s "I mean, absolutely. But there is no way you are anywhere near ready for what that objective is."
    to "Well, now I’m rather curious. Can you not explain it?"
    s "Not without putting our future relationship in jeopardy. "
    to "I understand. If it will have some sort of effect on my time in both the dorms and [kumon_mi_high], I’d rather keep it at bay for the time being."
    to "It’s hard enough getting adjusted to life in a place like this."
    s "Yeah, I imagine this is basically the exact opposite of what you’re used to."

    scene toukahall3
    with dissolve

    to "I actually find it both endearing and mildly upsetting how so many girls are able to fit under one roof."
    to "I’ve yet to see the inside of anyone else’s room, but mine seems rather...small for two people."
    s "They’re all the same size. "

    scene toukahall7
    with dissolve

    to "And they expect us to live happily under these excruciatingly packed conditions?"
    s "Well, I don’t know if I’d say {i}happily,{/i} but yeah. "
    s "I guess it’s a lot easier if you don’t already have a bedroom that’s the size of this entire floor."
    to "Yes, I do suppose that having exactly that may be skewing my judgement in some way."
    s "Hold on a second...I was being sarcastic."
    s "You mean to tell me your bedroom is the size of this entire floor?"

    scene toukahall3
    with dissolve

    to "My first bedroom, absolutely. But my second and third are probably around the size of about...half?"
    s "What use could you have for three bedrooms?"

    scene toukahall7
    with dissolve

    to "Well, my first bedroom is where I keep all of my clothes and my...personal belongings. And the other two-"
    s "Why would you say “personal belongings” after a pause like that? That just makes it sound like you’re hiding something inappropriate."

    scene toukahall8
    with dissolve

    to "Th-That’s not what I meant at all! I just have several things that you would likely make fun of me for owning, so I would rather not disclose them at this point in time!"

    if toukastreets1 == True:
        s "That’s fine. I’m sure I’ll see whatever it is you’re hiding when I come over for that tea you promised me before."
        to "Absolutely not! As if I’d let {i}you{/i} of all people into my first bedroom!"

    else:
        s "That’s fine. It will just make finding out what you’re hiding from me all the more exciting when I finally get to see your “manor.”"
        to "You will do nothing of the sort! My first bedroom is still years and years away from accepting someone of the likes of you!"

    s "What about the second and third bedrooms, then?"

    scene toukahall9
    with dissolve

    to "Well...those are certainly closer to being within your reach than the first. But it would still be remarkably strange."
    to "I don’t think we’ve ever allowed anyone like you into the manor before, so we’d likely need to make special preparations of some sort."
    s "What sort of special preparations do you think “someone like me” would need, exactly?"

    scene toukahall10
    with dissolve

    to "Well, it’s...easy to get lost if you don’t understand where you’re going. So you would likely need a tour guide and-"
    s "You realize you could just show me around yourself, right?"

    scene toukahall11
    with dissolve

    to "Well...I would not mind that at all. But I feel as if my father and the house staff would be quite disappointed if they found me doing a job like that."
    s "Doing a job like that as opposed to?..."

    scene toukahall12
    with dissolve

    to "Studying to perfect both my academic and social skills."
    to "You know, those things I relocated to this side of the city to pursue only to be derailed by a rogue teacher."
    s "Hey, that’s me. I’m the rogue teacher."
    to "Yes. Yes you are."
    to "I do hope you’re proud of yourself, as you have somehow managed to make my otherwise simple and peaceful life into something out of a Saturday morning cartoon. "
    s "I’m surprised a girl of your “status” even knows what Saturday morning cartoons are."

    scene toukahall13
    with dissolve

    to "Did I say...cartoon?! I meant Saturday morning...golf program! "
    to "Those morning golfers...always causing a commotion for the...afternoon ones..."
    s "..."
    to "..."

    scene toukahall14
    with dissolve

    to "OKAY! GOODNIGHT!"
    s "Oh, come on. There’s no need to be embarrassed about not being seen as a proper lady for a minute or two."

    scene toukahall10
    with dissolve

    to "What in Heaven’s name are you saying, Sensei? Do you not realize who I am?"
    s "Of course I do, Tadako."

    scene toukahall15
    with dissolve

    to "Touka! Heir to the Tsukioka family’s fortune!"
    to "I can not risk losing yet another teacher due to my inability to maintain my composure and-"
    s "Yet another?"

    scene toukahall9
    with dissolve

    to "I...uhh..."
    to "{i}Hah...{/i}"
    to "How is it that you’re able to set me off so easily with nothing more than immature teasing?"
    s "Hold on, I’m curious about this apparent history of “losing teachers.”"
    to "Improper phrasing and spontaneous sentimentality. Please do not think much of it."

    scene toukahall7
    with dissolve

    to "I apologize for my sudden departure, but I just realized that I still have matters to attend to tonight."

    if toukastreets1 == True:
        to "But...if you’d still like to show me a little more about how things work on the outside world as we suggested before, you can always find me out and about early on the weekends."
    else:
        s "Sudden matters like what, exactly?"
        to "Matters you need not concern yourself with as they do not have anything to do with you, Sensei."
        s "Hold on, I-"

    scene toukahall16
    with dissolve

    to "I sincerely apologize, but I really can not talk any longer. "
    to "Goodnight, Sensei. Please do be careful on the way home. It is rather dark outside right now."

    scene black
    with dissolve

    "Touka disappears into her room and I’m left scratching my head in the hallway."
    "Io looks up at me from her spot on the floor and, without saying much of anything, exchanges a glance that essentially asks, “Why are you talking to {i}her{/i} of all people?”"
    "I shrug it off and ultimately hang out with Io instead for the next few minutes before finally deciding to head home."
    "I wonder what it is, if anything, that Touka so urgently needed to do tonight?"

    $ renpy.end_replay()
    $ toukafirsthall = True
    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yasufirsthall:
    if _in_replay:
        play music "sweetvermouth.mp3"

    scene yasuhall1
    with dissolve

    s "Hey, Yasu. Having fun spending your free time just...standing in the middle of the hall?"
    ya "I’m not sure if I would call it fun, but Touka will not let me into the room right now. "
    ya "If you have any suggestions for a better way to spend my time, I would be happy to hear them."
    s "Well, I wouldn’t mind talking to you for a little bit. I’m sure it will keep the both of us at least mildly...entertained?"
    ya "I entertain you?"
    s "I think you go a little beyond that, but saying “entertain” is probably the easiest way to describe it."
    ya "Do I remind you of the snow on the ground? The wind in the trees?"
    s "No. You remind me of a girl who likely needs professional help but will not receive any."
    ya "What a strangely specific type of girl."
    ya "Is that what you would call your “type?”"
    s "Are you hitting on me right now?"
    ya "Romance is out of the question until my wings grow in, Sensei. For now, I am just trying to evaluate you."
    ya "It will come in handy soon."
    s "Why?..."

    scene yasuhall2
    with dissolve

    ya "Because soon, you’ll finally be ready to see where I’ve been hiding all this time."
    ya "Where I found solace when the world would not have me. "
    s "..."
    s "Is that just a really convoluted way of saying that you prefer cold weather over the heat?"

    scene yasuhall3
    with dissolve

    ya "I both love and hate the summer at the same time."
    ya "It’s quite complicated. I can’t really talk about it here."
    s "Why? You’re not going to tell me a top secret organization is conducting a surveillance mission on you or something, right?"
    ya "That’s something a crazy person would say."
    s "So you {i}are{/i} going to tell me that..."

    scene yasuhall4
    with dissolve

    ya "If we talk too loudly about things we’re not allowed to talk about yet, the floor will open up and swallow us."
    s "Yeah, that’s not a thing that happens."

    scene yasuhall1
    with dissolve

    ya "Are you sure?"
    s "...Yes?"
    ya "But I saw it with my own eyes, Sensei. The reckoning."
    ya "The hole that swallowed everything."
    s "The...hole that-"
    s "Wait, you’re not talking about Kumon-mi Academy, are you?"

    scene yasuhall5
    with dissolve

    ya "{i}Slip.{/i}"
    s "...Is that a yes or a no?"
    ya "It’s an answer. "
    ya "One I can share with you the moment you open your eyes."
    ya "When will you be ready to open your eyes?"
    s "I really wish you’d stop asking me that while I’m looking directly at you."
    ya "When will you be ready to be saved, Sensei?"
    ya "When will you be ready to be cleansed?"
    s "Cleansed of what, exactly?"

    scene yasuhall6
    with dissolve

    ya "All of the filth this world has to offer."
    ya "Let us wash it all away together."

    if bonus == True:
        s "You know, I’m normally the type to jump at an opportunity to shower with a cute girl, but I have a feeling I might not ever make it back if I accept this offer right now."
        ya "Make it back to where? It’s not as if this place is of any value to either of us."
    else:
        s "I will buy you a hose for Christmas."

    ya "It’s so much harder to feel the ground tremble from up on the second floor."

    if bonus == False:
        s "Okay Yasu."

    ya "Even if you lay down and press your cheek against the carpet of this very hall, you’d be lucky to feel anything at all."
    s "Please don’t put your face on the carpet here. I don’t think it’s vacuumed very often."

    scene yasuhall7
    with dissolve

    ya "Will agreeing to your demands bring you closer to the desire for salvation?"
    s "No, but it will keep you from getting dirty."
    ya "That which is white can never be dirty."
    s "That is very much not true, Yasu."
    s "In fact, I’d say it’s the complete opposite. "
    s "That’s a nice dress and you wouldn’t want it to get ruined."

    scene yasuhall8
    with dissolve

    ya "Nice?..."
    ya "Sensei..."
    ya "This dress is hideous. "
    ya "I want to tear it off right now."

    if bonus == True:
        s "You know, I tried giving you a compliment and being a nice guy, but then you went and said that. And now I’m stuck questioning my morals like I always am."
    else:
        s "Please don't. I don't want to see that."

    scene yasuhall9
    with dissolve

    ya "The funny thing about morals is that they are focused on what is right and what is wrong."

    if bonus == True:
        s "Yes. That is absolutely hilarious."
    else:
        s "Oh, okay. I guess we're talking about morals now."

    ya "But when we are nothing more than subjects for who we believe created us, aren’t morals rather silly?"
    ya "If I think something is right and you think something is wrong, but we are both virtuous in our beliefs, which one of us is truly right?"
    s "That’s a good point. If everything is subjective then-"

    play sound "static.mp3"
    scene yasuhall10
    with flash
    stop sound

    ya "BZZZT! Wrong answer!"

    play sound "static.mp3"
    scene yasuhall5
    with flash
    stop sound

    ya "My answer is the truly right one! Yours will only make the pain worse!"
    ya "The solution is to follow my lead! To see the things I see as right as virtuous in your own, {s}tainted{/s} purified eyes."
    ya "Does your vision ever get cloudy, Sensei?"
    ya "Tell me all of the horrible things you see, and I will swallow them whole."

    scene yasuhall11
    with dissolve

    if bonus == True:
        ya "I will swallow anything and everything that you ask of me."
    else:
        ya "(Airplane noises)"

    s "..."
    ya "..."

    scene yasuhall12
    with dissolve

    ki "Same."
    s "Thanks, Kirin. I had a feeling you were going to chime in there."

    if bonus == True:
        ki "That girl is fucking weird, Sensei. Come hang out with me and Noriko instead."
        s "Maybe some other time..."
    else:
        ki "I love airplanes."

    ya "Are you ready?"

    if bonus == True:
        s "For...the swallowing?"
    else:
        s "For what?"

    ya "For the {i}sanctuary.{/i}"
    ya "For the place that can not be swallowed by the hole that swallows everything. "
    ya "A place where we can cleanse ourselves together...and hide when the heat becomes too much for our pitiful bodies to bear."
    ya "A place where God does not live, but very much likes to visit when the time is right."
    ya "I want to show you that place, Sensei."
    s "It sounds a lot like you’re inviting me to a church right now."
    ya "..."
    s "..."

    scene yasuhall13
    with dissolve

    ya "..."
    s "..."
    s "You actually {i}are{/i} inviting me to a church aren’t you?"

    scene yasuhall14
    with dissolve

    ya "I’d be very happy if you came."
    ya "I just want to help you."
    s "I don’t think so, Yasu. I’m not really a religious person."

    scene yasuhall8
    with dissolve

    ya "Then why do you reek of a {i}shrine?{/i}"
    s "First off, rude."
    s "Second, shrines don’t have a scent."

    scene yasuhall7
    with dissolve

    ya "But gods do. And I am very very very very very very very very very very {i}very{/i} good when it comes to sniffing out things like that, Sensei."
    s "I wouldn’t mind showing up to hang out with you I guess, but..."
    s "Wait, hold on. This is a bad idea. I shouldn’t be going to see you in a place like a church where there are other people around."

    scene yasuhall3
    with dissolve

    ya "There is only me. "
    ya "It’s a special place that only the chosen can enter."
    s "Then how the hell will I get in? I haven’t been chosen at all."
    ya "I’m choosing you right now."
    ya "Come, wash away your sins with me."
    ya "I will not ask you to pray and will not stop you if you want to leave."
    ya "All I ask is that you come."
    s "..."
    ya "..."
    s "Ugh, fine. Whatever. But I’m literally only doing this because you’re cute."

    scene yasuhall6
    with dissolve

    ya "Hehehehehehehahahahahahehhahahaha!!!"
    ya "No romance, Sensei! Not without God’s approval!"

    "What the fuck did I just get myself into?"

    scene black
    with dissolve

    "Yasu takes one of her gloves off and removes an old newspaper clipping that she had been carrying around in there for some reason."
    "She places it into my hands and then clasps them together, bringing herself to her toes to try and whisper into my ear."
    "I crouch down a bit to help her."

    ya "{i}Praise be.{/i}"
    s "..."
    s "That’s it? That’s all you wanted to whisper?"
    ya "Goodnight, Sensei. The time has come again for me to pray."
    ya "The answer to all of your troubles can be found on that sheet of paper."

    "Yasu disappears back into her room and I..."
    "Well, I...go home."

    $ renpy.end_replay()
    $ yasufirsthall = True
    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "{i}Congratulations! You may now visit New Hope Cathedral!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label toukadorm5:
    if _in_replay:
        play music "sweetvermouth.mp3"
        scene dorm2

    play sound "knock.mp3"
    stop music fadeout 15.0

    "I knock on Touka’s door and wait for her to answer. "
    "I saw Yasu leaving the building on my way in, so at least I’m going in there knowing that I won’t have to figure out how to deal with her this time around."
    "If Touka even lets me in, that is."
    "I realize she’s been starting to warm up to me, but it’s not like she particularly likes me very much yet. "
    "And without her roommate being around to provide whatever...sense of comfort someone like Yasu can provide, she may very well be completely opposed to this."

    to "The door is unlocked. You may enter."

    "Or she may not be opposed at all and will just invite me in without question. "
    "Nice."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene toukapjs1
    with dissolve
    play music "thesleepingcity.mp3"

    "I push open the door to find Touka dressed {i}significantly{/i} down compared to her usual self, and I can’t help but be taken aback for a moment."

    if bonus == True:
        "Not just because she looks like an almost entirely different person, {i}but because she is fucking stacked. Holy shit.{/i}"
    else:
        "I make sure to maintain my distance so I do not cause her any discomfort."

    to "Did you forget something?"
    s "Is that your way of asking me to compliment you?"

    scene toukapjs2
    with dissolve

    to "Wait, you’re not Yasu. "
    s "I am not."
    s "Yasu knocks on her own door?"

    scene toukapjs1
    with dissolve

    to "Yasu does many strange things. I’ve decided it’s best if I just stop questioning them altogether."
    to "What brings you here, Sensei? "
    s "Before that, don’t you want to take a second to get all embarrassed about being seen in your pajamas by a commoner?"
    to "Not particularly. I have a very nice body, as you may have noticed. "
    s "Oh I have definitely noticed."

    scene toukapjs3
    with dissolve

    to "Oh. So you {i}want{/i} me to be embarrassed. That’s how it is."
    s "I mean, a slight blush wouldn’t kill you."

    scene toukapjs1
    with dissolve

    to "Well I apologize, but I will not be blushing or awkwardly avoiding your gaze tonight, for I am the picture of perfect health for a girl my age."
    s "Well, you...certainly take after your mother in at least one area."
    to "Is that any way for an educational professional to be talking to a student?"
    s "Not really. But Tsubasa already said you have to listen to me and-"
    to "I know what she said. "
    to "And if you’ve come here to belittle me some more or hold her words over my head, please have the decency to do it some other time."
    s "What if I’m here to say a bunch of nice things about you instead?"
    to "You? Act out of genuine kindness rather than self interest or curiosity? "
    to "I haven’t been here very long, but even I find that statement laughable, Sensei."
    to "..."

    scene toukapjs4
    with dissolve

    to "Though...it would make me feel a {i}little{/i} better, I suppose."
    s "Is something wrong? You seem less...pompous than normal tonight."

    scene toukapjs5
    with dissolve

    to "Do you expect lacing your concern with ridicule to gain you any favor in this conversation?"
    to "Look at me for a moment. Not at my chest, but at me. "
    to "Does it {i}look{/i} like something is wrong?"
    s "I mean, kind of. Yeah."
    to "Then it is safe to assume that something is wrong. There’s no need to ask."

    scene toukapjs6
    with dissolve

    to "How unfortunate that the one area I hoped you’d handle differently is the sole area that you approach the same way as everyone else."
    s "..."
    s "Do you want to be left alone or something?"

    scene toukapjs7
    with dissolve

    to "If that’s what you think is best."
    to "Though, if you’d like to keep me company instead, I won’t reject it."
    to "It’s not like anyone else is going to be knocking on the door anytime soon."

    "Ahh, so this is more of that."
    "I guess it would be exhausting or depressing or whatever else you want to call it if you go from having the world served to you on a silver platter to browsing the Internet all by yourself each night."

    s "Still having a hard time blending in?"
    to "..."
    s "..."

    scene toukapjs8
    with dissolve

    to "May I stand?"
    to "It’s impolite for me to let this conversation carry on while appearing so informal. I should be facing you, at the bare minimum."
    s "You don’t need to handle everything so formally. If you want to sit, that’s fine."
    to "If I wanted to sit, I would not have asked if it was okay for me to stand."
    to "So, with that in mind, may I stand?"
    s "I...I guess?"

    scene toukapjs7
    with dissolve

    to "Thank you very much."

    scene black
    with dissolve

    "Touka closes out a window on her laptop to prevent me from seeing it. But I highly doubt it was anything unsavory based on her posture."
    "She straightens out her tanktop and pats the sides of her leggings to smooth out any creases before taking her place a foot or two in front of me."

    scene toukapjs9
    with dissolve

    to "To answer your question, yes. I’m still having a hard time blending in."
    to "I realize that I am likely just impatient, but it is not a good feeling walking into class each morning and knowing that you are being judged despite doing absolutely nothing at all."
    to "I know I say strange things from time to time that “normal” people would laugh at, but I have yet to say enough to any of the other girls to warrant laughter whatsoever."

    scene toukapjs10
    with dissolve

    to "I probably would have been better off if none of them had a history at Kumon-mi Academy."
    to "But the fact that some did...means that I arrive here with not just a head full of hope and a heart full of naivety-"
    to "But an extensive background of preconceived notions and expectations that were not swallowed along with everything else the sinkhole claimed."
    to "I did not have any friends in my last[school], as I’m sure you know."
    to "I attended my own classes and had my own teachers, and communicating with me in general wasn’t prohibited or anything like that, but..."
    to "It didn’t seem like anyone ever wanted to do it. "
    to "Like they saw me as some girl that they could get in trouble for approaching, even though I’d smile and wave at every single student who walked past my window."

    scene toukapjs11
    with dissolve

    to "I’m sure that me complaining like this means absolutely nothing to you...especially now that I know how hard some people in our class have it."
    to "But the fact that I can still feel people looking at me and immediately jumping to the idea of “it must be so easy to be her” stings more than I ever imagined it would."
    to "I do not expect you to numb that sting."
    to "And I do not particularly expect you to care."
    to "But I do ask that you, at the bare minimum, acknowledge that I am not perfect or unwavering."
    to "I am a {i}real{/i} girl with {i}real{/i} feelings."

    scene toukapjs12
    with dissolve

    to "And I would very much like {i}real{/i} friends so I don’t have to spend so much time sitting in my room by myself."
    s "..."
    to "..."
    s "You’re crying again."
    to "Yes. I have been crying a lot lately. Please stop pointing it out."
    s "I don’t have a problem with it or anything. I actually think it’s cute."

    scene toukapjs13
    with dissolve

    to "My sadness is not cute! It is sad! Feel bad for me!"
    s "No, I just mean it’s nice being reminded that you {i}are{/i} an actual person and not some rich girl stereotype like I thought you were at first."

    scene toukapjs14
    with dissolve

    to "Ha..."
    to "I did some research on the stereotypical views people have of girls like me and can confirm that, to at least some extent, I fit the bill depressingly well."
    to "But simply not knowing how things work around here does not make me any less deserving than anyone else."

    scene toukapjs15
    with dissolve

    to "But...{i}ahem{/i}!"
    to "I should not be airing out those worries in front of you."
    to "I have learned through experience that letting my emotions get the best of me scares off those who have been selected to teach me."
    s "So you’ve gone from trying to get me fired to fighting off tears in an effort to keep me. And in just a few short dorm visits, too."
    to "I have given you the benefits of many doubts and will continue to do that until I no longer find it constructive."

    scene toukapjs16
    with dissolve

    to "And I will admit that I felt myself gradually slipping toward just that, but airing out more of my worries tonight has quelled the storm for at least the time being."
    to "It was also very nice of you to not interrupt me during my explanation."
    s "I can be serious when I have to be. Besides, it’s weird seeing you not acting...weird."
    to "I’m sure it came across as quite a shock at first, but I’m already feeling a little better now that I’ve gotten to talk about it."
    to "Yasu and I have been doing a little better too, in case you were wondering."
    s "Oh yeah?"
    to "We’re still nowhere near companions, but I no longer feel as if she is going to kill me in my sleep. Which is a dramatic improvement, if I do say so myself."
    s "Wow, you’re already braver than I am then."

    scene toukapjs17
    with dissolve

    to "Hahah! I suppose I am."

    scene toukapjs18
    with dissolve

    to "Okay. Now that the sad part is out of the way, I suppose there’s no longer a reason to stand."
    to "Let’s take a seat and talk a little more if you don’t mind."
    to "I have plenty of time to do this because I am what most people here would call a “loser.”"

    scene toukapjs19
    with fade

    "Touka sits down on an expensive looking ottoman and I find a place beside her."
    "There isn’t much room on it, so we need to sit relatively close together. But she is the one who chose this seat and so she is the one that must pay."

    if bonus == True:
        "I am absolutely not deterred at all from being so close to such an...endowed [teenage]girl."
        "Yup. Feeling totally normal right now."

    to "So..."
    to "Now what do we do?"
    s "We can keep talking about you, I guess. We seem to be on a roll in that regard."
    to "Is there anything in particular you’re interested in hearing?"
    s "I’m going to preface this by saying I mean it in the least offensive way possible-"
    to "Oh, wonderful. What a great sign."
    s "...But was there anything difficult about your life outside of Kumon-mi Academy?"
    s "I know you mentioned losing teachers and have an apparent disposition to the word “princess-”"
    to "But you want to know what the worst of the worst is."
    s "Right."
    to "I see."
    to "Yes, I suppose I would also be curious if I came across someone who I imagined was simply breezing through life without any issues whatsoever."

    scene toukapjs20
    with dissolve

    to "But the question you ask can not really be answered in a simple manner, as it’s been something I’ve been dealing with since I was born."
    s "Please don’t tell me you’re going to admit to having some sort of terminal disease now that we're finally starting to get closer."

    scene toukapjs21
    with dissolve

    to "I’m afraid that’s exactly what I’m about to do."
    s "What-"
    to "The disease of being born a woman to someone who, more than anything, wanted a male heir."
    s "Jesus, don’t call that a disease. I thought you were dying for a second."

    scene toukapjs22
    with dissolve

    to "The Tsukioka family is very much one of tradition."
    to "We’re wealthy now due to the entrepreneurial spirit of my grandfather-"
    to "But even before then, there were long periods of great wealth for the family that can be traced all the way back to the early Edo period. "
    to "And one thing that virtually every single iteration of the family held true to...was bearing no more than two children per every male figurehead. "
    to "As such, the first male born to every father would go on to inherit everything possessed by them at the time of their death."
    to "But seeing as my father has already had two daughters and will not break family tradition, that responsibility defaults to me as the first born. "
    to "Even though I’m not the gender he wished for."
    s "And you’d call that the hardest part about your life?"

    scene toukapjs23
    with dissolve

    to "I was born in a very fortunate place in time to a very fortunate family."
    to "It’s just unfortunate that I must work harder for my father’s approval than I would have had to if I had been born looking the way he desired."
    to "He's a good father...and he does love me."
    to "But sometimes, it feels like the only way to make him proud at all is to surrender myself to the male heir of some other family with even greater power than ours."
    to "Of course the issue with that is that there are no males anywhere and that I absolutely would not want to get married right now."

    scene toukapjs24
    with dissolve

    to "Maybe one day, though."
    to "I can only imagine how excited you are to be married into the Amamiya family."
    s "..."
    to "..."

    scene toukapjs25
    with dissolve

    s "Hah..."
    to "Did I say something wrong?"
    to "I apologize if I killed the conversation, but she seemed so excited at the prospect of settling down with you and-"
    s "Didn’t I tell you to not believe anything Ayane says?"
    to "If it was just her word, I’d understand but..."
    to "Ever since running into you two at the dojo, I felt some sort of connection."
    to "Do you mean to tell me there is nothing there?"
    s "I mean to tell you that if there is, it doesn’t concern you. And wouldn’t be something I’d want to talk about even if it did."

    scene toukapjs26
    with dissolve

    to "I’m very sorry...I meant no offense. "
    to "I was just interested in hearing a little more about how you intend to spend the rest of your life."
    to "My path is mostly clear, so...hearing how things are for those who have not been born into set courses...sometimes makes me feel rather warm inside."
    to "But if that’s not an area you’d like to touch on...I will respect that."
    s "Let’s just...move onto something a little different."

    scene black
    with dissolve2

    "Touka’s idea of “something different” is telling me more about her family’s history which, and this might come as a surprise, {i}I’m not very interested in.{/i}"
    "But she does seem to enjoy talking about it and...I do enjoy sitting next to her and {i}watching{/i} her talk about it, so I don’t try to stop her."
    "I let her talk until her mouth gets dry and she needs to get a drink from the vending machine outside."
    "I follow her into the hall as it’s getting late and I should probably be heading home anyway."
    "But I don’t leave until I confirm to myself that she is still doing the vending machine power pose I taught her the other day."
    "I’m so proud of her. "
    "And so excited for her to find out from a very confused classmate that she has been making herself look like an idiot for quite some time now."
    "Fortunately, she’s a very cute idiot."
    "And I find myself becoming more interested in her with each passing day."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukadorm5 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yasudorm10:
    if _in_replay:
        scene dorm2

    play sound "knock.mp3"
    stop music

    "I knock on Yasu’s door and wait for her to answer."
    "Why? I have no idea."
    "But it’s a thing I do and now I have to live with the consequences."
    "And I don’t mean consequences in the sense that I think tragedy might befall me for simply doing this-"
    "But moreso in the fact that from this point on, I will be completely out of my element and, as such, out of control."
    "It’s rather interesting, really."
    "I normally feel like I have the upper hand when it comes to conversing with everyone who lives in this building. "
    "Let’s look at Touka, for example."

    if bonus == True:
        play sound "static.mp3"
        scene realtoukaimage with flash
        stop sound
        play music "shiningstarvocals.mp3"
    else:
        play sound "static.mp3"
        scene toukaolddis8 with flash
        stop sound
        play music "shiningstarvocals.mp3"

    "Touka is a girl who is not Yasu but sleeps in the same room as Yasu."
    "If you pay close attention to the image in front of you, you will see that she is frowning."
    "But why?"

    if bonus == True:
        "Is it because we have not done the sex to her yet? "
    else:
        "Is it because she missed the latest Game Grumps video?"

    "Probably not."

    if bonus == True:
        "Though I would not doubt that she has, on several occasions, had to contemplate whether or not the act of pleasuring herself in the same room as a semi-comatose half nun would be moral or not."
        "I would not think any less of her if she tried, but do not expect that she would have been able to do it to completion because of how strange it would likely be."
        "Masturbatory tangent aside, Touka is probably frowning because she is one of the girls that I typically have the upper hand with."
        "Not just because my hands can reach higher things than hers, but because she is a weak little girl and I am a big strong man."
        "I will do the sex to her and make her smile happen."

    scene dorm2
    play sound "knock.mp3"
    stop music

    "I knock on Yasu’s door and wait for her to answer."
    "Why? I have no idea."
    "But it’s a thing I do and now I have to live with the consequences."

    ya "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene yasufirstdorm1
    with dissolve
    play music "undersea.mp3"

    ya "Good morning, Sensei."
    s "It’s nighttime, Yasu."
    ya "Is it? I suppose I lost track of time in the midst of prayer."
    ya "It would not be the first time I’ve let an entire period of day slip by without noticing."
    s "Fair enough. Don’t you want to turn the lights on, though?"
    ya "Not particularly. "
    ya "There is only one light that matters to me. The rest of them are nothing but hindrances meant to-"
    s "Before you continue that, I just want to make sure you’re going to put it in terms that I understand and not some weird religious way."
    ya "Sunlight hurts my eyes and my skin."
    ya "It makes coming to[school] very difficult sometimes."

    scene yasufirstdorm2
    with dissolve

    ya "But I am a good girl and will do what God tells me to do."
    s "Well I’m happy to hear your god is concerned about your education."

    scene yasufirstdorm3
    with dissolve

    ya "He is more concerned with spreading the message of His love than of my menial general studies."

    if bonus == True:
        ya "There are no better candidates for angels than [adolescent] girls, untouched by the evils of man and untainted by the stink of life."
        s "Well, uhh...good luck."
        s "I wouldn’t count on everyone being {i}untainted{/i}, though."
        ya "Even {i}if{/i} they’ve already been contaminated, they are not so broken that they are beyond repair."
        ya "Life is long. And if they wish to atone for any misdeeds they may have done, now is the best possible time to begin their repentance."
        ya "They can all still be saved. And it is my duty as an angel in training to usher them to safety like the confused sheep they are."
        s "Just...don’t repeat any of that out loud to them or it will be even harder for you to make friends than it is for Touka."
    else:
        s "He should start a mailing list."
        ya "A mailing what?"
        s "It's a thing that lets you email a bunch of people at once."
        ya "What is an email?"
        s "..."
        ya "I am lost without you, Sensei."

    if bonus == True:
        play sound "static.mp3"
        scene realtoukaimage with flash
        scene yasufirstdorm4 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene frown with flash
        scene yasufirstdorm4 with flash
        stop sound

    ya "LET US WALK!"
    s "Woah, what?"
    ya "I TIRE OF THESE WALLS!"
    ya "LET US GO SOMEWHERE ELSE!"
    s "We don’t have to hang out here, but I’d certainly appreciate it if you’d stop yelling."

    play sound "static.mp3"
    scene yasufirstdorm5 with flash
    stop sound

    ya "I can do that."
    ya "I’m sorry, Sensei. A sudden urge came over me and I was not able to suppress it."
    ya "The first hours after I pray are the hours when the noises become loudest."
    ya "I can’t help it if they take over sometimes."
    ya "I hope it will not ruin our blossoming friendship or any chance you have of following me in the future."

    scene yasufirstdorm1
    with dissolve

    ya "But for now, I shall follow {i}you{/i}."
    ya "I leave you in charge of taking me somewhere exciting."
    s "That’s a big ask when I know your preferred hang out spots are a church and directly in front of your bedroom wall."
    s "I’m not really sure if we find the same things “exciting.”"
    ya "Hmm...I suppose we most likely don’t."
    ya "Oh, here is an idea."
    ya "How would you like to return to the spot where we first met?"
    s "Great idea. Nothing says exciting like the place where I watched you cause the most innocent girl in my class to break out in tears."

    scene yasufirstdorm6
    with dissolve

    ya "Not all tears are bad, Sensei."
    ya "Even if my words brought them to her eyes, I’m sure they were for happy reasons."
    ya "For she had likely heard something she’d been waiting to hear for a very long time."
    s "What does that-"

    scene yasufirstdorm5
    with dissolve

    ya "But for now, let us go! Adventure awaits! "
    s "..."

    scene black with dissolve

    s "Okay, I guess."

    "Yasu puts her shoes on and the two of us make our way out of the dorms and into the streets."
    "I’ve been to the park where I met Yasu on several other occasions since then, so I know where we’re heading and lead the way."
    "There isn’t much discussion on the way there, but it’s not really an uncomfortable silence or anything like that."
    "In fact, the silence is probably even more comfortable than the parts of the night where we're talking."
    "Maybe Yasu and I should just remain quiet all the time?"

    if bonus == True:
        "It might be a little boring at first, but at least I won’t be tempted into joining a cult based on the promise of transferring spiritual warmth through my penis."
    else:
        "Or, at the very least, maybe she could stop making airplane noises."

    "I’ve still yet to wrap my head around that."
    "........."
    "......"
    "..."

    scene yasufirstdorm7
    with dissolve

    s "..."
    ya "..."
    s "Did you really have to bring the umbrella?"
    ya "I must have instinctively grabbed it thinking it was morning again."
    s "You’re still on that?"
    ya "I suppose so."
    ya "It’s a bit of a reflex at this point, though. I’ve despised the sun ever since I was a little girl."
    s "I somehow have a hard time imagining a younger version of you."
    ya "Why is that?"
    s "You’re just so...eccentric now that I can’t imagine a time where you weren’t like that."
    s "And I have a hard time believing you’ve been a religious fanatic since you were born."

    scene yasufirstdorm8
    with dissolve

    ya "Fanatic sounds a little hurtful."
    ya "It makes it sound like I’m over the top or irrational."
    s "Oh, I know how it sounds."
    ya "I spoke about it at the church, but there are things etched into us at birth that play a great role in determining our purpose. The people we hope to become."
    ya "Do you think this version of me is the result of a single event and not simply the way I was designed?"
    s "So...you {i}have{/i} been insane ever since you were born?"

    scene yasufirstdorm9
    with dissolve

    ya "That seems to be the consensus. "
    ya "If you were to ask anyone that knew me back then, I’m sure they would tell you you’re correct."
    ya "I am far from insane, though. "
    ya "I actually find myself to be more rational and level headed than anyone when I’m not listening to the voices trapped in the aether."
    s "Yasu, the reason so many people think you’re insane is very likely because you say things like that."
    ya "Having better hearing than anyone else makes me insane?"
    s "No, but thinking there are voices floating around in “the aether” kind of does."
    s "What does that even mean?"

    scene yasufirstdorm10
    with dissolve

    ya "You know what a {i}soul{/i} is, correct?"
    s "In the vague moral sense, yes. But in the religious one...kind of?"
    s "Something about an imaginary entity inside of you that contains your consciousness and history or whatever mumbo jumbo they use to trick kids into thinking there is an afterlife."
    ya "That is such a sad way to look at things."
    ya "The soul is not imaginary. Though, it’s a bit more complicated than an invisible stream of consciousness. "
    ya "If your body is the container that stores your thoughts now, what would happen if you switched containers?"
    ya "What if you no longer had a use for your body as you were able to simply store your thoughts in the world itself?"
    s "..."
    s "Isn’t that an invisible stream of consciousness?"

    scene yasufirstdorm11
    with dissolve

    ya "Yes. But like I said, it’s more complicated than that."

    scene yasufirstdorm8
    with dissolve

    ya "Some fake religions certainly do deceive people with the promise of souls moving into the afterlife."
    ya "But as I know with absolute certainty, for I see the light and hear the light, the afterlife is all around us."
    ya "There is a second plane of existence that lies directly on top of our current plane."
    ya "It’s just impossible to see with your eyes only partially open."
    s "So basically, once someone dies, their consciousness exits their body, but continues to exist outside of it?"

    scene yasufirstdorm7
    with dissolve

    ya "That is the gist of it."
    s "Yeah, we should take you to a hospital. Let’s go."
    ya "Oh, stop. What makes this possibility any less believable than a fortress in the clouds or being reborn as a plant?"
    ya "To die is to disappear. And since it’s impossible to fully vanish, there is no death."
    s "What you’re saying isn’t exactly {i}less{/i} believable. It’s that none of those things are believable in the first place."
    ya "So you are one of those people who believes in eternal darkness succeeding the end of traditional life?"
    s "I guess you could say that. Yeah."
    ya "And are you happy with that way of thinking?"
    s "I’m not {i}unhappy{/i} with it."
    ya "You are very good at dodging questions you find inconvenient, aren’t you?"
    s "It’s definitely one of my strengths."
    ya "What can I do to have you reconsider?"
    ya "Would hearing the disembodied whispers of friends or lovers past grant you the solace you need to try a new system of beliefs?"
    ya "To step out into the night and spread your arms, letting tendrils of the winter winds wrap around you and embrace you the way you long to be embraced."
    ya "We are sensitive creatures, you and me. You and me and everyone else."
    s "I am far from sensitive. “Detached” is probably a better word."
    ya "You and your silly textbook definitions of words..."
    ya "I do not mean sensitive emotionally and physically."
    ya "I mean sensitive in the fact that our entire existences could be entirely rewritten by even the most minor of events."
    ya "If you heard the things I hear, you would believe. And I would not have to ask you to follow."
    ya "You would simply fall into line alongside me and spread His word for the rest of the world to hear."
    ya "We’d approach the end of days together, and I would carry you to the place where all is safe with the help of my new wings."
    ya "And yet you still feel inclined to disbelieve me."
    s "Yes. Because you are crazy."
    ya "If believing in what I know to be the truth is crazy, I fear for the rest of this city."
    ya "I fear the thoughts they must have. The lack of closure. The sensation of a loved one wrapping around them as they make their way down the street."
    ya "I fear those who will not accept messages from the one person in the world who can carry them."
    ya "I fear everything and nothing at all."

    scene yasufirstdorm12
    with dissolve2

    ya "I fear you."
    s "Me?"
    ya "You. Surrounded by a thick blanket that forces back the whispers of someone so lonely it shakes the earth to the core."
    ya "You. Who not only denies what he has seen, but attempts to carve out paths in all directions and separate his body into pieces so he may walk down all of them at once."
    ya "You. Who is blessed and cursed at the same time. Who is both the purest entity I have ever seen and a person so tainted that it’s a miracle you can still walk."
    ya "You, who lives. "
    ya "You exist as both my greatest fear and my greatest hope. For all that I am will surely rely on you before you are ready to be relied on."
    ya "That is why I fear everything and nothing at all."
    ya "Not because I can hear the whispers and wishes in rivers of lost souls."
    ya "Not because I can feel the pain in every person and every place."
    ya "But because I can not feel you."

    scene yasufirstdorm13
    with dissolve2

    ya "..."
    s "..."
    s "Are you sure you don’t want to go to the hospital?"
    ya "Hehehe~"
    ya "I’m sure."
    ya "I’m a rational girl. And I’ve already been a little pushier about earning your trust than He wants me to be."
    ya "But I can’t help but worry about the end of the world when I can feel it looming on the horizon."
    ya "Before long, the snow will melt. "
    ya "The seasons will change."
    ya "And His slumber will come to its end."
    ya "Perhaps it is only then that you will learn to accept the truth in everything."

    scene yasufirstdorm14
    with dissolve

    ya "I am not crazy, though."
    ya "I am chosen."
    ya "I am the sole bearer of the word of truth and the sole believer of the light. "
    ya "And through the gift of the divine and the aetheric whispers of all else who have learned the truth-"
    ya "I will teach you. "
    ya "I will give you myself and you will give me yours."

    if bonus == False:
        s "No thank you."

    ya "And then we will give it all to him."
    ya "Praise be."
    s "..."
    ya "..."
    s "Sorry, just still figuring out what the hell I’m supposed to add to this conversation."
    s "I expected things to get a little weird but I didn’t really expect you to go on a rant like that."
    s "Though, I probably should have, considering that’s really all you ever do around me."
    ya "I can’t help that I have many things to say, Sensei. I exist to deliver messages and can not be faulted for being good at my job."
    s "I hope you’re getting paid well, at least."
    ya "Not yet. But it will all be worth it in the end."
    ya "I hope you will be there to see how beautiful I become."

    scene black
    with dissolve2

    "Yasu says some more stuff about her god or whatever but I zone out and stop listening almost immediately."
    "Frankly, I’ve been doing that for basically all of our walk tonight."
    "It’s not like I’m intentionally ignoring her, though."
    "And it’s also not like what she’s saying is boring me to the point where I no longer care."
    "I just can’t manage to prevent my mind from trailing elsewhere."
    "And before long I get lost."
    "Lost in the artistic sense of the word."
    "And before I know it, I’m back at the dorm, wishing her sweet dreams."
    "Though, I doubt she’ll dream of anything."
    "And if she does, I doubt it will be sweet."
    "I go home."

    $ renpy.end_replay()
    $ yasudorm10 = True
    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

                    ############################################
                    ##########        ROOM 10         ##########
                    ############################################

label kirindorm:
    if kirin_love >= 10 and day271 == True and day != 3 and utadorm5 == True and iodorm5 == True and kirindorm10 == False:
        jump kirindorm10
    if kirin_love >= 15 and kirinsoccer20 == True and day != 3 and kirindorm15 == False:
        jump kirindorm15
    if kirin_love >= 20 and kirindorm15 == True and day != 3 and kirindorm20 == False:
        jump kirindorm20
    if kirin_love >= 25 and norikodorm25 == True and day != 3 and kirindorm25 == False:
        jump kirindorm25
    else:
        jump kirindormgen

label kirindormgen:
    play sound "knock.mp3"

    ki "Come in!"

    scene kirindormgen
    with fade

    "Kirin invites me in and the two of us proceed to spend the next hour or two laying on her bed, discussing the different bilateral and multilateral trade agreements of Japan."
    "Just kidding."
    "We lie there and talk about life."
    "The good parts of it, the bad parts of it, and the parts of it that ooze so much mundanity that they may as well not even exist at all."
    "For someone so routinely toxic or manipulative or whatever she's trying to trick herself and everyone else into thinking she is, she certainly has a lot of well-informed opinions on the world."
    "But I guess something like that is easy when the world is such a terrible, worthless place."
    "Sometimes, I feel like the two of us wish we could destroy the world and just float around in the ether until we suffocate and die from lack of oxygen."
    "But then again, it could just be me."
    "So I shall continue to dream of a world without anything-"
    "And Kirin will continue to suffocate in her own, special ways."

    scene black
    with dissolve

    "One [[non-sexual] thing that happens when two people lie in bed for X amount of time is that one of them normally grows tired."
    "Not tired of the same mundanity I mentioned previously, but tired in general."
    "Tonight, that person is Kirin."
    "The conversation carries on until she can no longer keep her eyes open."
    "She trails off in the middle of a discussion and passes out."
    "I think about waking her up to sate my boredom but ultimately decide against it, pulling her blanket over her and turning the lights off as I head back home."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label norikodorm:
    if noriko_love >= 5 and kirindorm10 == True and convenience1 == True and norikodorm5 == False:
        jump norikodorm5
    if noriko_love >= 10 and convenience5 == True and kirindorm20 == True and norikodorm10 == False:
        jump norikodorm10
    if noriko_love >= 20 and norikospecial20 == True and norikodorm20 == False:
        jump norikodorm20
    if noriko_love >= 25 and convenience25 == True and day != 3 and norikodorm25 == False:
        jump norikodorm25
    if noriko_love >= 30 and norikodate30 == True and otohadate20 == True and day != 4 and norikodorm30 == False:
        jump norikodorm30
    else:
        jump norikodormgen

label norikodormgen:
    play sound "knock.mp3"

    n "Come in, Sensei!"

    scene norikodormgen
    with fade

    "I head into Noriko's room to be immediately greeted by a big hug and a kiss on the cheek."

    if bonus == True:
        "As you probably know by now, I'm not the biggest fan of actual affection. But at least she's able to do all of these things without making me feel strange about it."
        "Despite the notable gap in our ages, there's a clear, unique connection between us that even I have a hard time comprehending."
        "It's possible that's just this body's old memories banging against the bars of the prison I forced them into, but it could also be that Noriko's just...different."
        "So I'll continue to spend time with her."
        "Not just to discover why I might be feeling this way, but because the act of discovering in itself is inherently enjoyable."
    else:
        "I could have done without the kiss part, but I'm not about to deny a nice, warm hug from one of my favorite people."

    scene black
    with dissolve

    "The two of us hang out under the kotatsu, conversing about random things and treating whatever television show she put on as white noise."
    "She playfully kicks at my legs from time to time, sort of like how I'd expect a little sister to if I was fortunate enough to have one."
    "I guess Noriko's the closest I'll ever come to that, though."
    "So I might as well enjoy this sensation now, while it still lasts."

    if bonus == True:
        "Because who knows if she'll want to do this when (and if) she ever grows old?"

    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko's affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label kirinhall:
    if chapthreeactive == True:
        scene kirinsummer2hallgen
        with dissolve
    else:
        scene kirinhall1
        with dissolve

    ki "Thank fucking God. I was dying of boredom."
    ki "Please, {i}please{/i} do something with me before my brain starts to ooze out of my ears."
    s "I will certainly do my best to prevent that from happening."
    s "Did you want to go into your-"
    ki "No. Let's talk out here."

    "Kirin and I spend the night in the hallway instead of going into her room for whatever reason."
    "I get feeling cooped up sometimes, but what is it about standing around in the hallway that seemed so alluring to her tonight?"
    "Oh."
    "Oh, okay. I get it."
    "She probably just wants the others to see me hanging out with her."
    "Or at least that's what I imagine is going through her head."
    "Regardless, we talk for an hour or so before deciding to call it a night, and I find myself heading back home having accomplished virtually nothing today."

    scene black
    with dissolve
    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    jump endofweekday

label norikohall:
    if chapthreeactive == True:
        scene norikosummer2hallgen
        with dissolve
    else:
        scene norikohall1
        with dissolve

    n "Hey! We made eye contact so that means you have to hang out with me now."
    s "I had no idea such a rule existed."
    n "It exists and if you break it, I get to cut your arms off and wrap them around myself so I can be eternally hugged."
    s "You're a fucking psychopath, Noriko."
    n "But I'm {i}your{/i} psychopath."

    "Noriko and I spend the evening hanging out in the hallway, doing nothing in particular."
    "Some of the other girls wind up walking by and seeing us chatting."
    "I can tell that they want to get involved as well, but either out of respect for Noriko (Or for fear of her existence), they abstain."
    "Before I know it, it's almost midnight and I can already hear Ami scolding me for taking too long to get home..."

    scene black
    with dissolve
    $ noriko_love += 1
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    jump endofweekday

label kirinfirsthall:
    scene kirinhall1
    with dissolve

    ki "Yo. "
    ki "Please tell me you’re here for me. I’m bored as shit."
    ki "I was actually just about to text you begging you to come over."
    s "I am here for you, Kirin."
    ki "Thank fucking God."
    ki "Noriko’s been blasting music for like two hours and I’m about to pour liquid cement into my ears."
    s "I take it things aren’t going well in there?"
    ki "Oh, things are actually really great. Just kind of annoying at times. "
    ki "But it’s not like I can tell her to chill when it’s her room, too. She can do whatever she wants."
    ki "I’m sure there will be plenty of times where {i}she’ll{/i} get mad at me, so learning how to deal with that is a pretty logical first course of action."
    ki "Whatever the case, it sure beats staying at home. "
    s "Ramping up to complain about your sister again?"

    scene kirinhall2
    with dissolve

    ki "What do you mean, “ramping up?”"
    ki "You make it sound like that’s a thing I do all the time."
    s "I mean...not {i}all{/i} the time."
    s "You’ve definitely made me aware of how much you hate living at home before, though."
    s "But despite that, you still waited until you were put in my class to move into the dorms."
    s "Why didn't you just bite the bullet and move into the other building?"

    scene kirinhall3
    with dissolve

    ki "Are you {i}trying{/i} to be a dick to me right now, or is this just happening on accident?"
    ki "All I did was talk to you and now it’s like you’re fucking profiling me or something."
    s "I didn’t mean it like that. "
    s "I’m obviously glad you’re here. I wouldn’t have come to see you if I wasn’t."
    s "I just...also like your sister and wouldn’t feel right if I didn’t at least try to stand up for her."

    scene kirinhall4
    with dissolve

    ki "Well...yeah...that makes sense."
    ki "Sorry for being so on edge or whatever. I shouldn’t have exploded like that."
    ki "It’s just weird, you know?"
    ki "Even though I love it here, it’s still a huge frickin’ transition going from your parents’ house to living with some girl you literally just met."

    scene kirinhall5
    with dissolve

    ki "Buuuuut...that’s enough emotional Kirin for now. Help me take my mind off of that stuff, Sensei."
    ki "I’m sure you didn’t just come over here to hear me complain."
    s "If you want to complain, it’s fine-"
    ki "I {i}said{/i}...I’m sure you didn’t come all the way here to hear me complain."
    ki "Take my fucking mind off stuff. "
    s "..."
    s "You can be really intimidating when you’re in a bad mood, Kirin."

    scene kirinhall6
    with dissolve

    ki "You just need to learn how to deal with me. Don’t call me intimidating just because you haven’t figured it out yet."

    if kirinpatgasm == True:
        s "Will more headpats do the trick? Because you seemed to {i}really{/i} like those."

        scene kirinhall7
        with dissolve

        ki "Wha-?! No?! That won’t do the trick at all! "
        ki "I didn’t even like them that much!"
        s "I distinctly remember you liking them so much that you started pleasuring yourself."
        ki "Shut up!"
        s "I had to wash my sheets and everything."

        scene kirinhall8
        with dissolve

        ki "OH MY GOD, STOP!"

    else:
        s "Well, here’s hoping I’m actually able to do that one day."
        ki "If there’s anyone who can right now, it’s definitely you."
        s "Because I’m the first boy you’ve ever had feelings for?"

        scene kirinhall9
        with dissolve

        if bonus == True:
            ki "There’s a difference between “having feelings” and “wanting to feel you inside of me.”"
            s "Please don’t turn me on in the hallway."
            ki "I’d turn you on in the room but Noriko’s music would kill the mood for me."
            ki "You’re just going to have to hang in there, Sensei~"
            s "Yeah, yeah..."
        else:
            ki "There’s a difference between “having feelings” and just wanting to hug somebody a whole bunch, you big jerk."

    s "Anyway, have you been getting acclimated to life here apart from all of the Noriko stuff?"
    s "It must be a lot easier getting to[school] now, right?"

    scene kirinhall10
    with dissolve

    ki "I guess so, yeah."
    ki "Like, my parents’ house is far enough away for them to send buses and whatnot, but Karin and I never really took them."
    s "Is it because Karin thinks it’s best to get exercise early in the morning to...set your body up for the rest of the day or something?"
    ki "I don’t know, probably. That sounds like a thing she would say."
    ki "I just don’t really like buses. Or trains, really."
    ki "Or any small space with a lot of people, I guess."
    ki "People suck. Why would I ever want to be surrounded by them? "
    ki "It also means that there’s probably someone in that group who’s going to think {i}I{/i} suck as well."

    if bonus == True:
        s "You do suck. And you’re quite good at it."

        scene kirinhall11
        with dissolve

        ki "Yay. Blowjob compliment."
        ki "My parents would be so proud."
    else:
        s "But you're so awesome and talented and your hair smells so nice."

    scene kirinhall10
    with dissolve

    ki "But really, though. Fuck everybody."

    if bonus == True:
        s "I mean, if-"
        ki "Stop making sex jokes whenever I use a word that could also be considered suggestive."
        s "But that’s like, half of my strategy for keeping a conversation going."
        ki "Are you sure it’s not half of your strategy for grooming [teenage]girls into thinking sex is cool and casual and that it would be totally fine to have it with you?"
        s "That does sound more in-line with how I think, yes."
    else:
        s "Your attitude could use a little adjusting, though."
        s "I thought growing platonically closer to you might fix that, but..."

    scene kirinhall1
    with dissolve

    ki "Well, hey. It’s definitely working, so it’s not like I can really bash you for it."
    s "Right. You can just call me out on it and make me question my morals."

    if bonus == True:
        ki "What morals?"
        s "See? Now I have to pretend to have them because you think I don’t."
        ki "Who needs morals when orgasms exist? Just do whatever you want as long as both parties consent."
        ki "Doesn’t matter if it’s teacher and student. Husband and mistress-"
        s "Uncle and niece."
    else:
        ki "Not only does our platonic relationship have nothing to do with your morals, the moral compass you {i}do{/i} have is infallible and unbreaking."
        ki "I truly do wish more people could be like you."
        s "Thanks, Kirin."
        ki "No problem, boy'o. Now brace yourself because I'm gonna hit you with a random question."

    scene kirinhall12
    with dissolve

    ki "..."
    s "..."
    ki "Do you..."

    if bonus == True:
        ki "Do you want to fuck Ami?"
    else:
        ki "Do you want to hug Ami?"

    if amifingered == True and bonus == True:
        s "I have no idea what you’re talking about."
        ki "But..."
        ki "But you just said-"
        s "Well, it’s been fun, Kirin. But it’s probably time for me to start heading back."
        ki "I’m..."
        ki "I’m gonna...go ahead and forget I heard that."
        s "Again, no idea what you’re talking about."

    else:
        if bonus == True:
            s "No, of course not."
            s "But I can’t help but feel like it’s not the other way around sometimes."
            ki "Did like, something happen?"
            ki "Does she sneak into your room at night?"
            ki "Maybe you should install a camera?"

            scene kirinhall1
            with dissolve

            ki "Oh! You should have me sleep over and we can see if she hangs out outside of the door and touches herself to the sounds of us sixty-nining. "
            s "But how would we even see if-"
            ki "Doesn’t matter. Can I sleep over tonight?"
            s "I..."
            ki "...?"
            s "Maybe some other time. I'd like both of us to live to see tomorrow."
        else:
            s "Of course I want hug Ami. I want to hug everyone. And Ami is so soft and cute."
            s "It's like hugging a large strawberry."
            ki "What kind of fruit do I remind you of, Sensei?"
            s "Maybe a...............................cantaloupe."

    scene black
    with dissolve

    "Kirin sighs and presses her back up against her door."
    "We talk for a short while after that, but the conversation loses steam and we ultimately wind up a little bored further down the line."
    "I think about inviting her out to walk around town or something, but it’s already getting really late and it would make more sense at this point to just go home."
    "In the end, we exchange goodbyes and head our separate ways."
    "I can hear another sigh from Kirin bleed into the sounds of rock music contaminating the hall once she opens the door."
    "Here’s hoping she can get some sleep tonight."

    $ renpy.end_replay()
    $ kirinfirsthall = True
    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikofirsthall:
    scene norikohall1
    with dissolve

    n "Hey! What brings you over here today, Sensei?"
    n "If you’re just wandering around the halls looking for something to do, might I suggest hanging out with yours truly?"
    n "I heard from some of the others that you mope around here like some sort of lost puppy pretty often, and I would like to inform you that I am looking to adopt."
    s "I wasn’t looking to be adopted today, but I guess the two of us can hang out."
    n "If {i}you{/i} were looking to adopt as well, I would also like to make myself available as your dog. "

    if bonus == True:
        n "You can walk me around on a leash and everything. Ami would love it."
        s "I don’t think there’s anything in the world that Ami would hate more, actually."

        scene norikohall2
        with dissolve

        n "You’ve just gotta learn how to talk to her. Leave it to me, Sensei."
        s "If you say one word to her, I feel that the two of us may never see each other again."

        scene norikohall3
        with dissolve

        n "But I just got you back! That’s not fair! "
        s "You're right. Which is why I regret to inform you that I can not walk you around on a leash {i}in public{/i}."

        scene norikohall4
        with dissolve

        n "Oh, right. I forgot that the public part was the first link in the chain of events that lead to us being separated once more."
        n "I can live with that as long as one of us gets to leash the other in private some time."
    else:
        s "I hope you are ready to be put up for adoption. I do not want to take care of a pet."
        n "Wow, okay. Nevermind then."

    s "Noriko, can I ask you something?"

    scene norikohall5
    with dissolve

    n "You can ask me literally anything you want whenever you want."
    s "Have you really been waiting years for me to walk back into your life?"
    n "Well, I’m technically the one who walked back into yours. But yeah."
    s "Then...how did you get so into this leash thing? Has this {i}always{/i} been a dream of yours, or..."
    n "I have an overactive imagination that sometimes drifts into dangerous territory."
    n "If you’re worried that it’s something I’ve experienced and thus have developed an unhealthy craving for, you are mistaken."
    s "Interesting."
    n "How so?"
    s "I just normally have to work a little harder to get girls this invested in me."

    scene norikohall6
    with dissolve

    n "Hehe...yeah."
    n "I still remember how hard you had to work to get Niki to like you back in the day."
    n "But as soon as you did it was like, all she ever talked about."
    n "Which is probably why {i}I{/i} started feeling all tingly really early too."
    n "Well, that and you were super cute back then."
    n "Not to say that you’re not still cute, obviously. But now it’s more of a “mysterious older guy” cute and not “shirtless neighbor boy in the backyard” cute."
    s "Well thanks for not ever making a move back then, I guess."
    s "I can’t imagine that would have been good for my apparent previous relationship with a pop star."

    scene norikohall7
    with dissolve

    n "There’s no need to add “apparent” to that, Sensei. It definitely happened and it was a huge part of all of our lives."
    n "Even if you don’t remember it right now, I’m sure you will in time."
    n "And once you do, I’ll be there to squeeze you and let you cry on my shoulder until your eyes turn so red and puffy that they swell shut and need to be surgically reopened."
    s "I can’t foresee myself crying any time soon, but thanks for the offer regardless."

    scene norikohall8
    with dissolve

    n "Don’t mention it...I-"
    n "I know it’s probably really weird hearing someone bring up the past so much when you’ve already clearly moved past it, but..."
    n "There’s a life for you outside of this dorm, you know? Outside of the[school], too."
    n "And I make good enough money between my job and doing PA work for Nee-chan that I could {i}probably{/i} support the two of us if you wanted to just quit teaching altogether."

    scene norikohall9
    with dissolve

    n "But teaching has always been what you're good at."
    n "That’s why Maya and I turned out so darn smart."
    n "Obviously, there was a lot of work that still had to be done outside of that creepy old apartment of yours-"
    s "Wait, Maya?"

    scene norikohall10
    with dissolve

    n "Yeah. The same Maya that's in our class and wants to turn my spine into a coat rack."
    n "You don’t remember that either?"
    s "Not at all..."
    n "Well...how did you think the two of us knew each other, then?"
    s "I had no idea. She wouldn’t tell me anything about it. Just that you’re evil and going to ruin everything."
    n "How would I ruin anything at all? I’ve done literally nothing wrong since I’ve shown up here."
    s "True. But, to be fair, that hasn’t been very long."

    scene norikohall1
    with dissolve

    n "Well then, let me prove it to you."
    n "I didn’t wait all of these years to show up and get you to hate me or think I’m weird."
    n "And, if there’s anything you want to change, just let me know. "
    n "Turn me into a sculpture. "
    n "Make me your ideal girl."
    n "Want someone with darker hair? I’ll dye it. "
    n "Someone skinnier? I’ll lose weight."
    s "Please don’t lose any weight. You’re already extremely skinny."
    n "I can gain weight, too. Just say the word."
    s "Just...stay the way you are now."
    s "I’m not going to do something like ask you to change for me when I haven’t even identified any problems yet."
    s "Except for maybe the pocket knife thing."
    s "Actually, yeah. Get rid of your knife."
    n "Oh, the pocket knife stays. I need it to protect myself and conserve my chastity for you."
    s "Fine. But get a holster or something so you don’t wind up slicing your leg open again."
    n "Roger that. "
    n "Anything else?"
    s "Yes. Give me your number."

    scene norikohall2
    with dissolve

    n "Nice. That was smooth."

    if bonus == True:
        n "Are you going to text me at weird hours of the day asking for nudes? "
        s "Are you going to send them if I do?"
        n "Uhhhh yeah? Duh."
        n "Just don’t post them online or show them to anybody else."
        s "Who would I even show them to?"
        n "I don’t know. I heard you’re really close with that girl who wears the skull hairclip in our class and I get hardcore lesbian vibes from her."
        n "But, actually, she’s cute. You can show her if you want. "
        n "Just don’t let her know {i}I{/i} know because then it will be a whole thing and we might wind up fingering each other on a camping trip or something."
        s "Please invite me if that ever happens. I will never forgive you if you don't."
    else:
        s "Not as smooth as your...face."
        n "That was less smooth."
        s "I'm sorry. I am not used to flirting."

    s "Also, why haven't you given me your number yet?"
    n "I’m still waiting for you to give me your phone."
    n "I promise to not delete every single contact except for myself."
    s "That wasn’t a thing I was worried about until you said that."

    scene norikohall9
    with dissolve

    n "I was kidding, obviously."
    n "You don’t actually believe the stalker thing that Maya said in class, do you?"
    s "Let’s just say if I were to rank the girls by “likelihood to follow me home after[school],” you’d be near the top."
    s "And that’s pretty impressive given that we just met."
    n "Just {i}reunited{/i}. And yeah, I’m definitely going to follow you home from time to time."
    n "But I have zero qualms doing that alone {i}or{/i} as part of a group."
    n "Nothing would make me happier than just going out to karaoke with you, Ami, and that one blonde girl who thinks she loves you more than I do for some reason."

    if bonus == True:
        n "Except for maybe making out with you in said karaoke booth while Ami and the blonde girl sing Misfits songs."
    else:
        n "Except for maybe hugging you in said karaoke booth while Ami and the blonde girl sing Misfits songs."

    s "That fantasy seemed plausible up until the very end of it."
    n "Gimme your phone. "

    if bonus == True:
        n "Oh, and if I {i}do{/i} send you nudes, please send some back. "
        n "I know I said I have an overactive imagination, but visual aids still help a loooooot when I’m jilling myself off under the covers."
    else:
        n "I'm gonna order Domino's."

    s "I have no idea why Maya doesn’t like you. You’re perfect."

    scene black
    with dissolve

    "Noriko takes my phone and enters her contact information into it."
    "Not only does she slap a heart emoji next to her name, she inserts a puking emoji next to her sister’s name right above hers."
    "I figured the Kandas were going to be the only sibling war I found myself wrapped up in, but..."
    "It seems that this is very much not the case."
    "And even though my experience with the Nakayamas (Or at least the experiences I am consciously aware of right now) is brief-"
    "I imagine this war will be much more...intense than that of the other one..."

    $ renpy.end_replay()
    $ norikonumber = True
    $ noriko_love += 1
    $ norikofirsthall = True
    stop music fadeout 5.0

    "{i}Congratulations! You now have Noriko’s number!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label kirindorm10:
    play sound "knock.mp3"

    "I knock on Kirin’s door and wait for her to answer."
    "It’s a little strange being able to do that after getting so used to just calling her every time I want to see her."
    "But the fact that she’s here now makes my life exponentially easier since this is already my second house."
    "Kirin and I are basically roommates now."
    "..."
    "Come to think of it, who {i}is{/i} her roommate?"
    "It has to be Noriko, right?"
    "Either that or she’s just living by herself in here- which would be extremely depressing."
    "But I guess if anyone was going to live alone out of the class it would be Kirin."
    "Or Yumi."
    "Or Maya."
    "..."
    "Actually, I have a lot of independently “functioning” girls in my class, now that I think about it."

    ki "Oh! Noriko, I think this is it. Could we be receiving our first ever visit from Sensei?"
    n "The first of many, dear Kirin. "
    n "Have you prepared the handcuffs?"

    if bonus == True:
        ki "I don’t believe handcuffs will be necessary. He seems like the type to willingly tie himself to the bed if it means getting to “hang out” with us."
        s "Stop accurately characterizing me from behind the door and let me in."
    else:
        s "Ooh! Are you guys fighting crime in there?!"
        n "We are pretending to!"
        ki "It is to prepare for when we are policewomen."
        s "I want to see!"

    ki "It’s open! Just walk in if you’re so impatient."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I turn the handle and, lo and behold, the door {i}was{/i} open after all."
    "I don’t know why I ever expect any less at this point."
    "And if this particular door isn’t locked now, I can’t imagine it ever will be in the future either. So that's cool, I guess."
    "Also, am I wrong for thinking that Dorm 10 seems like it could be a little more...intense than most of the others if these girls’ personalities mesh as well as I expect them to?"

    scene firstkirinnorikodorm1
    with dissolve

    ki "Welcome to our humble abode. May I take your coat?"

    if bonus == True:
        n "May I take your pants?"
        s "I'm already being stripped on my first trip here?"
    else:
        n "Please turn around so I may gently pat you down and confiscate any weapons you may have."
        n "Is there anything in your pockets that is going to poke me, stick me, or stab me?"

        "I start to cry because I am scared."

        n "Oh no. Have I made an error?"
        s "You did great. I am just a wimpy boy who didn't think it worked like this."
        n "That is fine. But I still need to pat you down."

    ki "Is that not how this normally goes?"
    ki "Sorry, just a little unfamiliar with the process."
    n "I just really like your pants."
    s "..."
    s "I take it you two have been getting along well?"

    scene firstkirinnorikodorm2
    with dissolve

    ki "Almost a little {i}too{/i} well."
    ki "It’s really convenient that we both happened to transfer in on the same day. "
    ki "Even if Noriko totally stole the spotlight and made my introduction seem super boring by comparison."
    n "The trick is to make everyone hate you on the first day so things can only go up from there."
    ki "And here I was thinking that getting people to dislike you should be more of a slow burn."

    scene firstkirinnorikodorm3
    with dissolve

    ki "So, what do you think? Pretty nice place, huh?"
    ki "We spent the whole day decorating it. And after seeing some of the other girls’ rooms, I think ours is among the best."
    n "By among the best she just means the best."
    ki "Yes. Yes, I do."
    ki "But after seeing the garbage dump that is Uta and Io’s room, it’s not like our competition is really all that strong."
    s "It’s a competition now?"
    ki "Everything is a competition, Sensei."
    ki "Love...dorms...pretty much every aspect of life becomes a battle when you put a bunch of like-minded girls in one place and tell them only one can survive."
    s "Who told you that only one of you is going to survive?"
    ki "I just can’t see this ending any other way."

    scene firstkirinnorikodorm4
    with dissolve

    "I step between Kirin and Noriko and begin to observe what I imagine is Kirin’s side of the room. "
    "I’m not exactly sure what I was expecting, but it’s definitely more well put together than I imagined it would be for someone who hasn’t had their own room, well, ever."
    "I wonder if all of those years of wanting to get out are what gave her the power to make this place...livable?"
    "Unlike the garbage dump that is Uta and Io's room."
    "I feel a little bad for adding to the insult, but...come on."
    "How could the two of them ever let that happen?"

    scene firstkirinnorikodorm5
    with fade

    ki "Does it live up to your expectations, Sensei?"
    s "I’m just glad you aren’t also a trainwreck."
    ki "I consider myself more of a calculated disaster."
    ki "The same appeal as a trainwreck where you don’t want to look away, but with significantly less shredded metal and all of that other morbid stuff."
    s "That is a strangely specific way to describe yourself."
    ki "That’s not my description. It’s Noriko’s. "
    s "Really?"
    s "I’m not one to judge how people get to know each other, but-"

    scene firstkirinnorikodorm6
    with dissolve

    s "Oh."
    s "You are very close."
    n "Am I?"
    s "You’re not actually blind, are you?"
    n "Blinded by your beauty, Sensei."
    s "First, please don’t call me beautiful."
    n "Noted."
    s "Second, are you sure it’s okay to be calling your new roommate a-"
    n "Calculated disaster? Yes."
    ki "Yeah, I really don’t care."
    ki "Noriko’s not “all there” herself, so the two of us can just put our minds together and create one socially acceptable human being. "

    scene firstkirinnorikodorm7
    with dissolve

    ki "Two for the price of one sounds pretty good, right?"
    s "Always."
    s "I just don’t want to leave this room thinking you’re on good terms just to find out that one of you killed the other one in their sleep the next day."
    n "Why does everyone always think I’m going to kill someone in their sleep?"
    ki "Probably the pocket knife and crazy eyes combo."
    n "Crazy eyes? Are my eyes crazy?"
    ki "Yeah, but they work for you. It’s cute. "
    n "Awwwww, Kirin~"

    scene firstkirinnorikodorm8
    with dissolve

    if bonus == True:
        ki "So, when did you want to fuck me?"
    else:
        ki "So, when did you want to hug me?"

    s "..."
    ki "..."
    s "Uhh..."
    ki "What’s up?"
    s "I don’t know if it’s safe for me to answer that question with Noriko directly behind me."
    s "You literally just mentioned her pocket knife and crazy eyes."
    ki "It’s fine. Noriko and I made a pact."
    s "A pact? What kind of pact?"

    scene firstkirinnorikodorm6
    with dissolve

    if bonus == True:
        n "Kirin gets to have your dick and I get to have your heart."
        n "And also your dick."
    else:
        n "Kirin gets to hug you and I get to also hug you."
        n "But I will hug you better."

    n "We laid ground rules when we moved in together."

    if bonus == True:
        n "I can’t say I’m fond of the prospect of you fucking my friend in my room, but I’ve already come to terms with you fucking my sister, so one more won’t hurt as long as there are no feelings involved."
        n "Also, there won’t be any issue at all since I’m sure you’ll only want me in due-time anyway."

    s "This dorm room is weird."
    ki "Hey! Eyes over here, Sensei."

    scene firstkirinnorikodorm9
    with dissolve

    ki "You stand on my side of the dorm, you talk to {i}me{/i}. Got it?"

    if bonus == True:
        s "Sorry. I’m just realizing this is the closest I’ve been to a threesome inside of the dorms and it's making it hard to focus."
        n "Oooooh! Everyone wins with a threesome! We can all live happily ever after~"
    else:
        s "Sorry. I just got a little excited when hugs were brought up."

    scene firstkirinnorikodorm10
    with dissolve

    s "So these, uhh...”ground rules” you two worked out-"
    ki "What about them?"
    s "Is there anything I need to know?"
    s "Like, who gets me on Thursdays, for instance?"
    ki "What, do you think Noriko and I are a divorced couple fighting for custody of our child or something? "
    ki "It’s nothing like that."

    if bonus == True:
        ki "We just need to be courteous to each other and not screw around while the other is in the room."
        s "That is going to make the threesome very difficult."
        n "Maybe we can set up like, a divider in the middle of the room and you can just walk to the other side after three or four thrusts?"
        ki "Not counting future threesomes, obviously. But it’s not like we’re just going to jump into that right away, you know?"
        s "I’m getting mixed signals here and I’m not sure what I should expect moving forward."
        n "Kirin wants to lose her virginity like any other dignified lady- bent over a vibrating bed in a love hotel."
    else:
        ki "We just need to be courteous and respectful to each other or the dorm will fall into disarray and tear us apart."
        n "The best way to stay on good terms is to respect each other's boundaries and maybe pat each other on the back every once in a while."

    scene firstkirinnorikodorm11
    with dissolve

    ki "Oh, that actually sounds pretty neat. Thanks, Noriko."
    n "I gotchoo, girl."

    if bonus == True:
        s "This is the first time I’ve ever heard someone call losing their virginity “neat.”"

    scene firstkirinnorikodorm12
    with dissolve

    ki "Sooooo, yeah. That’s basically the only major ground rule."

    if bonus == True:
        ki "Oh, and I also promised to never start feeling anything more than sexual attraction toward you but, let’s be real...me actually “liking” someone?"
        ki "That’s just not possible."
    else:
        ki "Oh, and I also can't enjoy the hugs. But like...let’s be real...me actually “enjoying” something?"
        ki "That’s just not possible."

    s "Are you sure about that?"

    if bonus == False:
        s "I am a very good hugger and you may wind up liking it more than you expect once I really start trying."

    scene firstkirinnorikodorm13
    with dissolve

    ki "Of course I’m sure about that. Why wouldn’t I be?"
    s "It just seemed like you might have been actually starting to, you know, {i}feel{/i} something the other day when you told me about transferring in."

    scene firstkirinnorikodorm14
    with dissolve

    if bonus == True:
        ki "That was just a weird day! All I feel is horny!"
    else:
        ki "That was just a weird day! All I feel is hungry!"

    n "Like, right now?"

    scene firstkirinnorikodorm15
    with dissolve

    ki "No! Not right now, Noriko! I meant in general!"

    if bonus == True:
        ki "I am a generally horny person who has no interest in actual romance!"
        n "Okaaaaay~ But you know what happens if you break the contract~"
        s "Wait, yeah, what happens if she breaks the contract?"
    else:
        ki "I am generally hungry!"
        n "You are on a diet, Kirin. Remember what you told me to do if you start breaking it."
        s "Wait, what happens if Kirin breaks her diet?"

    scene firstkirinnorikodorm16
    stop music

    n "I get to dissect her."
    s "..."
    n "..."
    s "..."
    n "..."
    s "..."
    n "..."

    scene firstkirinnorikodorm17
    with dissolve
    play music "sweetvermouth.mp3"

    ki "So, yeah. That’s how things stand."

    if bonus == True:
        ki "We can fuck each other, but we’re not allowed to feel anything on an emotional level or Noriko gets to cut me up."
        n "I believe the technical term is “friends with benefits.”"
        n "Meanwhile, I’m the “childhood friend slash imouto” type."
        n "So not only am I caring and adorable like a little sister, I have years worth of pent up sexual aggression and curiosity all aimed right at you!"
        ki "And obviously I can’t compete with that."
        s "..."
    else:
        ki "We can hug each other, but I am not allowed to enjoy it. It will be nothing but disgruntled, angsty hugs."
        s "I want to hug you right now from hearing that but I am afraid you would like it."
        s "It is so sad that you must live this way. How could Noriko do this to you?"

    scene firstkirinnorikodorm18
    with dissolve

    ki "It’s like...totally fine this way! I wouldn’t have agreed otherwise."
    ki "Now, can we just move onto something else?"
    ki "I feel like you’re trying to get me to second guess my instincts. And my instincts are exactly why I’ve managed to get as far as I have."
    s "And how far is that exactly?"

    scene black
    with dissolve

    "Kirin hops off of the bed and makes her way over to her desk, swiping a can off of it and taking a sip of some fruity-smelling energy drink."
    "There are several of the same exact cans strewn across the room, and it makes me question how much of tonight’s conversation has been sincere and..."
    "How much has been fueled by sugar and caffeine."

    scene firstkirinnorikodorm19
    with dissolve

    ki "Listen, I don’t know if you’re just trying to make me second guess myself, but I’m totally okay with things playing out like this."
    ki "It’s how it {i}should{/i} be and it’s exactly what I {i}want{/i}."

    if bonus == True:
        ki "If anything, I should be happy that I met Noriko so I don't wind up falling into that weird harem thing you’ve got going on."

    scene firstkirinnorikodorm20
    with dissolve

    n "And I should be happy I met Kirin because I am going to shatter your harem and make you love me and only me."

    scene firstkirinnorikodorm21
    with dissolve

    n "Also, she has a cute butt."
    ki "Uhh...thank you?"
    n "Squeeeeeeeze~"
    s "Do you two need some time alone?"

    scene firstkirinnorikodorm22

    ki "I have no idea."
    n "We do, but it doesn’t involve butts. "
    ki "I am mostly relieved, but also mildly disappointed to hear this news."

    if bonus == True:
        s "Same."

    n "I just want to talk to her a little more about our contract thingy and make sure we’re both okay with the terms and conditions."
    s "Ah. Well I should probably be heading back now anyway."

    if bonus == True:
        s "It’s getting late and becoming more apparent by the minute that there will be no threesome tonight."
    else:
        s "It's past my bedtime and I am a sleepy boy."

    n "Does that make you sad?"
    s "Sadder than you could ever imagine."
    n "I see, I see."

    scene firstkirinnorikodorm23
    with dissolve

    ki "Thanks for dropping by, though. "
    ki "I’m sure you’ll be here pretty often in the future, so...until next time, I guess?"
    s "Yup. Until next time it is."

    scene black
    with dissolve2

    "I say goodbye to the two of them and exit the dorm room, still slightly confused about the Kirin-Noriko character dynamic."
    "It {i}seems{/i} that they get along, but I can’t help but feel like Kirin may have prematurely agreed to something she wasn’t exactly 100%% behind."
    "Granted, she also seems like the type to easily trick herself into thinking she doesn’t want something she actually does-"
    "So I guess she’ll be fine no matter what happens."
    "I wish I was that good at manipulating my own thoughts."
    "But I guess it’s just as beneficial to be gifted enough to manipulate others."
    "..."
    "I’m looking forward to the time I’m going to spend in that room."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirindorm10 = True
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirindorm15:
    play sound "knock.mp3"
    stop music fadeout 10.0

    s "Hey, Kirin. Are you home right now?"

    "I knock on Kirin’s door, hoping to be able to spend some time alone with her tonight."
    "But, without knowing what Noriko is up to, it’s highly probable that that won’t be happening at all."
    "That’s not to say I don’t like Noriko either, it’s just-"
    "Kirin seems to function a little differently around me than she does with others."
    "Or, who knows? Maybe that’s just something I tell myself to feel special."

    ki "Yup! Feel free to let yourself in, Sensei. Door is always open to you."

    scene black
    with dissolve
    play sound "dooropen.mp3"
    play music "sleepystreets2.mp3"

    "I quickly open the door and let myself into the room."
    "The same fruity aroma that greeted me the last time I was here welcomes me with open arms once again."

    scene kirinkotatsu1
    with dissolve

    "And before long, I am facing two cute girls and an upside down house."

    ki "Excellent timing as always, Sensei."
    ki "Noriko and I were just about to watch a movie."
    n "Hey! Have you seen this one before, Sensei?"
    n "They play it on repeat in the old district all the time, but Kirin’s telling me she’s never seen it before."
    s "I can't be sure if I’ve seen it if I don’t even know what it’s called."
    s "The weird house certainly doesn’t look familiar to me."

    scene kirinkotatsu2
    with dissolve

    n "Huh...Now that I think about it, I don’t really know what the title is either. But it’s a super weird movie."
    n "You’ll probably like it."
    s "I get why Noriko wants to watch this, but I didn’t take you as the type to be into...abstract movies, Kirin."
    ki "I don’t really care. I just want to hang out under the kotatsu and unwind."
    ki "It’s been a pretty long day, to be honest."
    n "How come it's normal for me to do weird stuff but not normal for Kirin?"
    n "I'm not actually weird, am I?"
    ki "Want to maybe join us or something, Sensei?"
    ki "Not sure if you’re aware, but Noriko is kind of crazy about you, so there’s no chance she’d say no."

    if bonus == True:
        n "All I ask is that there’s no funny business under the table, including any conducted with me. "
        n "I just spent my entire last paycheck on this kotatsu and I don’t want it to get all gross after just a couple uses."

        scene kirinkotatsu3
        with dissolve

        ki "Think you can hold back for an hour or two? Or would you rather go bang on Ayane’s door for some “instant” satisfaction?"
        s "Stop saying questionable things in front of the girl with the pocket knife."
        n "Hm? Did Kirin say something questionable?"
        n "My hearing’s not great, so I probably didn’t catch it."
        s "Good."
        s "But yeah. I wouldn’t mind staying and hanging out here if that’s okay with you two."
    else:
        s "Sure, I'm down for some good clean fun."

    scene kirinkotatsu4
    with dissolve

    ki "Great! I call shotgun."
    n "Hey! I was about to call shotgun!"
    s "Am I a vehicle now?"

    if bonus == True:
        ki "Yup. Noriko and I are gonna ride you all the way to Mt. Fuji."
        n "Just not under the kotatsu."

    ki "Shotgun in this context means you have to sit next to me. "
    ki "Which you should {i}probably{/i} be thanking me for, since God only knows what would happen over on the crazy side."
    n "Nothing would happen! I don’t even normally bite!"
    s "Normally?..."

    scene kirinkotatsu5
    with dissolve

    n "There’s a time and a place for everything, Sensei~"
    s "You know, I could always just sit in the middle and not offend-"
    ki "Nope. I called shotgun. "
    ki "If you break shotgun rules, you have to spend the rest of your life cleaning our room."
    s "You intend to live here forever?"

    "Well, actually...it's not like there's really a choice."

    ki "Okay, whatever. You have to clean the room until we move out."
    s "Fine. Please forgive me for trying to make everyone happy."
    ki "Making everyone happy never works, Sensei. You’ve gotta pick one person and just focus everything you can on them."
    s "I have learned the hard way that you are very much incorrect."

    scene black
    with dissolve

    "Kirin twirls around and heads over to the side of the kotatsu opposite Noriko, gracefully sliding herself under the blanket while keeping it lifted up so I can get under as well."
    "I oblige, realizing halfway through entering that I forgot to take my shoes off."
    "I’m glad that Noriko’s love for me apparently surpasses her desire to keep the kotatsu clean, because this is something that I should very much be called out on right now."

    scene kirinkotatsu6
    with dissolve

    ki "Comfortable?"
    s "Kind of cramped. But I’m pretty large and this isn’t the biggest kotatsu in the world."

    scene kirinkotatsu7
    with dissolve

    n "Mmmm!"
    ki "...What?"
    n "I don’t like how close you two are."

    scene kirinkotatsu8
    with dissolve

    ki "Oh, come on. All we’re doing is sitting..."

    if bonus == True:
        ki "I agreed to not catch feelings or whatever, but I never said I’d stay six feet away from him for the rest of eternity."

    n "I know, but I’m still jealous!"
    n "And also a little excited because my feet are touching Sensei’s knees right now."

    scene kirinkotatsu9
    with dissolve

    ki "Those are {i}my{/i} knees."
    n "Oh my God, why are your knees so big?"

    scene kirinkotatsu10
    with hpunch

    ki "Wha- They’re not! They’re normal-sized knees!"
    n "Nuh-uh. I’ve got tiny knees. They’re like little golf balls that hold my legs together."
    ki "Have fun breaking your legs, then! That’s way too small!"
    n "Kirin, you really KNEEd to chill out right now. Other people might be sleeping."
    ki "..."
    s "..."
    n "Get it?! "
    n "Because, like-"
    n "Knees..."

    scene kirinkotatsu11
    with dissolve

    ki "Hah..."
    n "Oh, come on! That was good!"
    n "And what's with these weird matching expressions?!"
    n "Are you sure you're not in love?!"
    ki "Can we just watch your stupid upside down house movie now?"
    n "You mean the movie that’s been playing the entire time we’ve been talking?"
    n "I kinda just assumed you didn’t care since you weren’t paying any attention to it."

    scene kirinkotatsu12
    with dissolve

    ki "Oh. Would you look at that?"
    ki "It actually {i}is{/i} on."
    ki "I guess it wouldn't hurt to watch a little bit of it. Especially since you’ve seen it so many times."

    "The three of us direct our attention to the giant glowing rectangle in front of us."
    "Somehow or another, and please forgive me for not understanding the science, it channels electricity into moving images."
    "Moving images that...look awfully real for something that is apparently just a movie. "
    "There are five girls in a house together, gathered around a small kitchen table."
    "The windows around them are boarded and they’re eating a strange gray substance piled high on their plates."
    "No one is saying or doing anything."

    ki "..."
    s "..."
    n "..."
    ki "Noriko, what the fuck are we watching?"
    n "It’s an arthouse film! I think. I don’t know."
    n "It’s weird. I’ve actually never finished it. "
    n "Something always comes up in the middle and I have to leave."
    n "It’s like, a {i}really{/i} long movie."
    ki "Are you sure you’re not just falling asleep?"
    n "Of course I’m not falling asleep!"
    n "Probably. "
    n "I don’t know! Maybe! Just watch! Stuff is gonna happen soon."

    if bonus == True:
        jump kotatsux
    else:
        ki "No. I wanna watch the Bee Movie. Put the Bee Movie on."
        n "But you {i}always{/i} want to watch the Bee Movie."
        ki "We want the Bee Movie, we want the Bee Movie."
        n "Kirin, come-"
        s "We want the Bee Movie, we want the Bee Movie."
        n "..."
        ki "BEE MOVIE! BEE MOVIE! BEE MOVIE!"
        s "BEE MOVIE! BEE MOVIE! BEE MOVIE!"
        n "Jesus, fine. We can watch the fucking Bee Movie."

        scene black
        with dissolve

        "Kirin and I bust into a loud cheer that echos through the dorms."
        "Eventually, everyone shows up to investigate and we all wind up watching the Bee Movie together."
        "I love the Bee Movie."

        $ renpy.end_replay()
        $ kirindorm15 = True
        $ kirin_love += 1
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."


        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label kirindorm20:
    play sound "knock.mp3"

    "I knock on Kirin’s door, waiting to see if she’s around tonight."
    "And, I guess I’m waiting to see if Noriko is around as well in a sense, given that she’s here pretty much every time Kirin is."

    if bonus == True:
        "If so, could this finally be the night of the fated threesome?"
        "Will my dreams finally come true?"

    ki "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I walk into the room to find things rather quiet."
    "And, within a matter of seconds, dreams die."

    scene kirinalmostsex1
    with dissolve

    s "Fuck."
    ki "Shit."
    ki "Why are we cursing?"
    s "Just coming to terms with something."
    ki "Looking for Noriko?"
    s "Not exactly. I’m fine with just hanging out with you."

    scene kirinalmostsex2
    with dissolve

    ki "Oh good. I’m glad you’re {i}fine{/i} with it."
    s "You know what I mean."
    ki "I’d still prefer to hear you say it out loud."
    s "I am here to spend time with Kirin Kanda and no one else but her."
    ki "Now say it more believably."
    s "Don’t push it. There are over ten other girls in this building that I can go hang out with instead right now."

    if bonus == True:
        ki "Mhm. But you’re in {i}my{/i} room. So I take it that means you either need something from me or you want to take my clothes off."
        s "Are you implying I wouldn’t come here to just talk?"
        ki "We both know that sex is better than talking."
        s "Correct me if I’m wrong, but you’re still a virgin. So you don’t technically {i}know{/i} that."
        ki "That’s right. I’m an innocent little girl who just dreams of being pinned down and ravaged by her teacher."
    else:
        ki "True. But how many more of them have the third season of Seinfeld on DVD?"
        s "Are we really bringing that up again? That was so long ago."
        ki "Just like the tragic volcano that destroyed Pompeii."

    ki "I guess we can talk about that?"
    s "Perfect. That’s one of my favorite topics."
    ki "It’s one of mine as well. "
    ki "In fact, I think I’ll skip out on my other obligations for tonight just so we can experience this wonderful conversation together."

    if bonus == True:
        jump kirinalmostx
    else:
        s "Awesome."

        scene black
        with dissolve

        "Kirin and I spend the rest of the night talking about Pompeii."
        "It is very sad."
        "But that's okay because she has the third season of Seinfeld on DVD and the passable humor of that is enough to quell some of the sadness."
        "George Constanza sure is a hoot."

        $ renpy.end_replay()
        $ kirindorm20 = True
        $ kirin_love += 1
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label norikodorm5:
    play sound "knock.mp3"
    stop music fadeout 25.0

    "I knock on Noriko’s door and wait for her to answer."

    if bonus == True:
        "I’ve yet to be able to spend any time alone in there with her and, if we’re ever going to get even half as close as she wants the two of us to, that’s probably something I should start doing."
        "It’s not only beneficial to her, though, of course."
        "I have plenty to gain from one more questionable relationship."
        "Especially one revolving around the sole creature in this universe that the girl responsible for resetting it hates."
        "Frankly, there’s a distinct lack of logic in my decision to continue reaching out to Noriko- but is logic really a necessary trait when consequences are no more real here than they would be in a book?"
        "I was placed here to do as I please. "
        "Which, if you’ve realized anything about me so far, is to have sex with the girls I find attractive."
        "Noriko is attractive."
        "Maya is attractive."
        "I will defile both of them or die in the process."
        "Such is life."
    else:
        "I hope she is ready to party because I am feeling saucy tonight."

    play sound "knock.mp3"

    s "Noriko, are you in there?"

    "I can hear the volume of distorted, intentionally messy rock music being turned down from the inside."
    "Seems like she didn’t hear me the first time I knocked."

    n "Is somebody there?"
    s "Yes, someone is here. It’s me."
    n "Oh crap! You can come in, Sensei!"
    n "Sorry to keep you waiting, I didn’t hear you at first."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "It’s fine. Don’t worry about it."

    scene norikowalk1
    with dissolve
    play music "wewereangels.mp3"

    n "Well of course I’m going to worry about it."
    n "What if you decided to go hang out with somebody else since I didn’t answer the door right away?"
    s "I’m usually a bit more persistent than that."
    s "If I made it to three knocks, though...that’s where I start getting angry."
    n "Hmm...I see, I see. So don’t let you get to three knocks. Got it."
    n "What’s an angry Sensei like, anyway? I’m pretty sure I’ve only seen you happy, neutral, and sad."
    n "I can’t ever recall a time where you like, {i}really{/i} got pissed off."
    s "I’m pretty sure the only time I’ve gotten pissed off in the last several months is when one of your classmate’s little sisters kept questioning a book I was reading to her."

    scene norikowalk2
    with dissolve

    n "What?! You never read me stories when I was little!"
    n "I thought time had worn you down, not made you a family man!"
    n "Though, this does bode well for the future of the Nakayarakawayamas."
    s "Please stop using that incredibly long last name. Something about it really triggers something in my brain to just-"

    scene norikowalk3
    with dissolve

    n "Explode?"
    s "..."
    n "Oh, bright idea. Is there anywhere safe the two of us could go to light stuff on fire?"
    n "It’s great for stress relief and might help you get some of your memories back."
    s "Was I...a pyromaniac previously?"
    n "I meant more of the “being alone with me” part."
    s "Aren’t we alone together now?"

    scene norikowalk4
    with dissolve

    n "We’re not. Big Brother is always watching, Sensei."
    s "Okay, so either you have a second sibling I don’t know about or that was an Orwell reference."
    n "Obviously it’s an Orwell reference. If I had a brother, I’d have made him track you down years ago and beat you up for moving without telling me."
    s "And if that brother was younger than you?"

    scene norikowalk5
    with dissolve

    n "I’d...be making sure his tutor doesn’t start teaching him anything weird."
    s "Uh-oh. I know an implication about myself when I hear one."
    s "What sort of weird stuff did I teach you about?"

    scene norikowalk6
    with dissolve

    n "Nothing we wouldn’t have learned about eventually."
    n "Like 1984, for example. I think we were like...ten years old when you started making us read that?"
    s "That is far too young for that piece of literature."
    n "Probably. Like, I don’t even think Maya was into stuff that complicated back then and she was just as weird as you were."
    n "{i}I’m{/i} the normal one here. "
    n "But I guess I should be thanking you since that book was the first of many steps on my way to becoming a real freedom fighter."
    s "And how exactly are you fighting for freedom, Noriko?"
    n "The only way a girl my age can be, through expression."
    n "Not like I can make any sort of real change until I build up a background or profile for myself and people start taking me seriously."
    n "I just hope I’m not too burnt out by the time I get out of [high_school] to actually do something that will make a difference."

    "If you ever {i}make{/i} it out of [high_school], you mean..."

    s "Then...if you could change anything in the world, what would you change first?"
    n "Our relationship status."
    s "Our relationship matters more to you than like...climate change?"
    n "They both matter. But if you want to know what would make me happiest, it’s that."
    s "I think freedom fighters are supposed to be thinking of the greater good, not themselves."
    n "Aren’t you attempting to inhibit my freedom by imposing that belief on me?"
    n "This is exactly what I’m fighting against, Sensei."
    s "I just can’t imagine many people will back your cause if it’s portrayed the same way outside of this dorm room."
    n "Well, I’ve still got a few years to iron out the kinks."

    scene norikowalk7
    with dissolve

    n "I {i}am{/i} going to do something, though."
    n "Even if it’s just changing one person’s life or like...adopting a kid or something like that."
    n "It’s hard to feel like you have a purpose in the world without a tangible symbol of that purpose, you know?"
    s "Not really. But if you ever need some semi-constructive criticism, you know where to look."

    scene norikowalk8
    with dissolve

    n "And it’s the same place I’m always looking anyway..."
    s "..."
    n "Can you just like, hurry up and remember me already?"
    n "I say a lot of stuff that would be ten times cuter if you only understood the connotations."
    s "I think that one was pretty easy to understand."
    n "So you remember how I always followed you around the house and stared at you when I was three?"
    s "Oh. Well, okay then. I guess there was a bit of subtext to that."
    n "There’s subtext to everything about me. I built myself around trying to catch your eye."
    n "But alas, I was never the favorite."
    s "I guess it must have been hard falling in love with someone that your sibling is-"

    play sound "static.mp3"
    scene yumis2
    with flash
    scene norikowalk9
    with flash
    stop sound

    s "..."
    n "Sensei?"
    s "How did we get here?"

    scene norikowalk10
    with dissolve

    n "Well...first, I told you I wanted to go for a walk since I’m still not that familiar with this area yet."
    n "And then {i}you{/i} said something like, “I guess I still have some time to kill.”"
    n "And then we opened the door and said hi to Uta who was trying to feed our dorm-bird crackers."
    n "And then we walked for a little while and wound up here."
    s "I feel like I almost remembered something."

    scene norikowalk11
    with dissolve

    n "An important thing?! Or like a thing you had for breakfast?!"
    n "Not that breakfast isn’t important, of course! It's the most important meal of the day!"
    s "An important thing."
    s "Probably. "
    s "It’s just a feeling, though. And one that’s gone now anyway."

    scene norikowalk12
    with dissolve

    n "Mmm!"
    n "Don’t lure me in like that! You know those memories are what my character arc is based around!"
    n "The sooner you get them back, the sooner I can move onto the next phase!"
    s "And that next phase is?"

    scene norikowalk13
    with dissolve

    n "Showing my parents and my sister that I was {i}not{/i} crazy and that there was always something special about the two of us."
    n "A little hope goes a long way, Sensei."
    n "I don’t claim to understand you or anything. There are still a million things I don’t know about you, and I’m sure you’ll find that out in no time at all."
    n "But there’s a lot more to falling in love than simply “understanding.”"

    scene norikowalk14
    with dissolve

    if bonus == True:
        n "Like looking at somebody and thinking, “Yeah. I’ll still want to have sex with you in twenty years,” or “I would know what to order you for dinner if you were in the bathroom when the waitress showed up.”"
    else:
        n "Like looking at somebody and thinking, “Yeah. That's a person I'd like to make a bone necklace with.”"

    n "Stuff like that."
    s "That sounds like something Ayane would say."

    scene norikowalk15
    with dissolve

    n "Ahh, yes. Ayane."
    n "She loves you a lot."
    n "I think she’s hiding something, though."
    n "I can feel it."
    s "We’re all hiding something."
    n "Do you think I’m hiding something?"
    s "Probably. "
    s "It would certainly be easy to in your position."
    n "You’re right. I could manipulate you all I want into thinking things that never happened {i}actually{/i} happened."

    scene norikowalk16
    with dissolve

    n "And yet, I find myself wishing every night that you’ll just come back home..."
    n "That one day I’ll wake up and hear the doorbell ring...and then rush downstairs and pretend I’m not excited to see you..."
    n "And you’ll pat my head and tell me I look cute..."

    scene norikowalk17
    with dissolve

    if bonus == True:
        n "And then you’ll go upstairs and finger my sister."
        s "You wish for that, too?"
        n "That part I’d be fine with leaving out. It’s the {i}first{/i} few that I want back the most."
        s "Our dynamic would have drastically changed if it was the last one you wanted most."
    else:
        n "And then you’ll go upstairs and hug my sister."
        s "To be fair, she could probably use a hug. She is very grumpy."
        s "But wouldn't that make you sad?"

    scene norikowalk18
    with dissolve

    n "Well that would still be better than it is now, right?"
    s "..."
    s "For me or for you?"
    n "For both of us."
    s "I didn’t realize you felt that way about your sister."
    n "I just mean that...at least if you were with Niki, there would be some sort of...return to normalcy, I guess."
    n "Even though I found “you” it’s still not the full “you.”"
    n "You’ve got a whole new life now...and a whole group of girls who would kill me if it meant being able to absorb all of my happy memories with you."
    n "And I would kill too if it meant being able to absorb just a few of the ones they’ve made this[school] year."
    s "I think I get what you’re saying, but I’m not sure where you’re going with it."
    n "What I mean is that if you were with my sister, I’d at least know where you are every night."
    n "Because right now, I can't even walk down the hall without thinking, “I wonder which door he's behind?”"
    s "..."

    scene norikowalk19
    with dissolve

    n "Sorry."
    n "I knew that would be something you didn’t want to hear, but I went and said it anyway."
    n "I just miss you. That’s all."
    n "The best thing for me is really just whatever nets me the most time with you...because I have no idea if you’ll just disappear again one day or not."
    s "It's really unfortunate just how possible that is."

    scene norikowalk20
    with dissolve

    n "Disappearing?"
    n "But...why?"
    s "This might sound weird, but I could technically disappear at any moment whether I like it or not."
    s "But it wouldn’t be something like moving or running away from you or whatever it was that happened in the past."
    n "You’re not actually like, a ghost or something, are you?"
    n "Because that would make this a lot harder to explain to my parents when we start dating."
    s "I just mean that the next time I disappear, there’s a chance you will too."
    s "And everyone, really."
    s "I’m not exactly sure how it works."

    scene norikowalk21
    with dissolve

    n "I don’t know if I’m just too [young]to follow this train of thought, but you don’t look like you’re messing with me."
    n "What’s going on? What do you mean by all of us disappearing?"
    s "I’m just saying that when someone fades away, the world stops existing."
    s "If I “disappear,” everyone else also disappears because I’m not there to perceive them anymore."
    n "And you think that’s equivalent to them just not existing at all?"
    s "Right."
    n "Isn’t that like...super selfish?"
    n "Like, wouldn’t you care about what happened to me if you just vanished again? How I’d process all of that?"
    s "I know enough about you already to assume that you’d just start looking again."
    n "Well...yeah. Probably. But I wouldn’t be happy about it."
    n "What about Ami or Ayane, though? Or Maya?"
    s "Ami and Ayane would take it the worst."
    s "Maya would throw a party."

    scene norikowalk22
    with dissolve

    n "Huh."
    n "Guess a lot can happen in just a few years."
    s "Again, though, I think it would be closer to them all just disappearing as well."
    s "One goes out, another comes in. "
    s "Think of it like starting a brand new world with a brand new version of you and a brand new version of me."
    s "No one disappears. They just get recycled."

    scene norikowalk23
    with dissolve

    n "Okay, I’m lost. "
    n "I’m normally good with these sorts of topics and stuff, but what you’re describing sounds like something out of an anime."
    n "Or at least some religion I’ve never heard of before."

    "Given her ties to the past, I was hoping these words would have had some sort of impact on Noriko."
    "Like maybe, by some strange twist of fate, she’d acknowledge the possibility of the world resetting and memories being wiped."
    "But I guess I’m still not great at explaining things I don’t understand."
    "And it’s not like I’ve been gaining any useful information from Maya lately either, especially in her current state."
    "Oh well."
    "Back into the unknown then, I guess."

    s "I’ll just make things simple by saying...don’t worry about me disappearing again."
    s "I can’t say any more than that, but you seem naive enough to trust me on this."

    scene norikowalk24
    with dissolve

    n "I don’t have to be {i}naive{/i} to trust you, Sensei. I can just {i}trust{/i} you."
    s "If you want, sure. I just can’t imagine why you ever would."
    s "I’m not the same person-"
    n "You are."
    n "Now get back to giving me a tour of the area so I’m able to find an ATM without getting lost in the future."

    scene black
    with dissolve2

    "Everything is casual from that point on."
    "There are no further discussions on spirituality and the domino effect that would come with someone’s memory being wiped."
    "Just ATMs, streetlights, and the soft hand of a peculiar girl."

    $ renpy.end_replay()
    $ noriko_love += 1
    $ norikodorm5 = True
    stop music fadeout 10.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikodorm10:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Noriko’s door and wait for her to answer."
    "I already know she works late most nights, so I won’t be surprised if she’s out."
    "But, since my luck always seems to be at least mildly good, I think the chances of us being able to spend some time alone together tonight are pretty solid."

    n "Come in!"

    "And so it appears that my mildly good luck prevails once more."

    scene black
    with dissolve
    play sound "dooropen.mp3"
    play music "wewereangels.mp3"

    "I push open the door to find that the typically fruity smell of the room has vanished. "
    "Today it’s something more like...laundry detergent."

    if bonus == True:
        jump norikounderx
    else:
        s "Oh, wow. You're doing laundry."
        n "Yup! Mind lending me a hand, Sensei?"
        s "Sure thing, buddy."

        "I help Noriko folder her laundry and then go immediately home."
        "I find 500 yen in one of her pockets and keep it to myself to invest it in Shiba Inu."
        "I am going to be rich."

        $ renpy.end_replay()
        $ noriko_love += 1
        $ norikodorm10 = True
        stop music fadeout 5.0

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label norikodorm25:
    play sound "knock.mp3"
    scene norikorestaurant1
    with dissolve

    "I knock on Noriko’s door and wait for her to answer."

    play sound "dooropen.mp3"
    scene norikorestaurant2
    with dissolve

    n "Sensei?"

    "But, to my surprise, she comes right on out and I don’t even have time to tell you about what I planned on doing here tonight."

    n "What’s up? What brings you over to my neck of the woods?"
    s "A better question is why were you so prepared to leave your room the moment I knocked?"

    scene norikorestaurant3
    with dissolve

    n "Would you believe me if I said I was just waiting around for you to show up?"

    if bonus == True:
        s "Yes, actually. You have proven to be rather...dog-like in the past."
        n "Bend me over and I’ll show you just how dog-like I really am. "
        n "I mean what? Who said that? Not me. I’m Noriko. A human girl."
        s "Well then, irrefutably human girl, what are you doing tonight?"
        n "Well, I {i}was{/i} going to go for a walk..."
    else:
        s "Yes, actually. You are unhealthily obsessed with me when my plan all along has been to set you on the right path toward a better future."

    scene norikorestaurant4
    with dissolve

    n "But {i}now{/i} I am going to change that plan entirely and invite you out to dinner!"
    s "You’re inviting {i}me{/i} out to dinner? How chivalrous."
    n "Chivalry is dead! Both sexes are on equal footing now and it’s okay for girls to ask guys out because relationships require equal effort on both ends and males should not be obligated to always strike first!"
    n "Also, I am hungry and there’s something I want to talk to you about!"
    s "Does it involve smashing the patriarchy?"

    if bonus == True:
        n "Is the patriarchy your penis?"
        s "In an extremely roundabout way...kind of?"
        n "Then...also kind of!"

        scene norikorestaurant5
        with dissolve

        n "To be completely honest, it really only {i}slightly{/i} involves your penis, but only as like a...concept. "
        s "You are inviting me out to dinner to discuss the concept of my penis?"
        n "In an extremely roundabout way...kind of?"
        s "Well, thankfully, that is one of a few topics I am incredibly well versed in. I hereby accept your invitation."
        s "Now, where are we going?"
    else:
        n "No."
        s "Oh."
        s "Then sure. I'm not a very good patriarch smasher anyway."

    scene norikorestaurant6
    with dissolve

    n "Soooo...you know that restaurant you went to with Nee-chan shortly after I found you and the hands on the clock of our romantic aptitude started ticking once more?"
    s "The hands of...what? Wait, are you talking about the place with the sausage fest?"
    n "No, no. I can’t eat sausage, remember? Vegetarian."

    if bonus == True:
        s "That is going to make the penis discussion very depressing for both of us."
    else:
        s "Oh, right. My apologies."

    scene norikorestaurant7
    with dissolve

    n "I’m talking about the fancier one. Where she opened up about her past and how she dealt with being apart from you and...all that stuff."
    s "You sure know a lot of what Niki and I talk about despite never really being there for any of it."
    n "Well, it’s not like she really has anyone {i}else{/i} to talk to about...anything. "
    n "And I guess she’s still just kind of used to talking to me about all you-related stuff since that’s how things were back in the old days too."

    scene norikorestaurant8
    with dissolve

    n "But now it’s my turn!"

    if bonus == True:
        n "It’s not fair that {i}she{/i} got to have you all to herself in some dimly lit, four star sex trap!"
    else:
        n "It’s not fair that {i}she{/i} got to have you all to herself in some dimly lit, four star restaurant!"

    n "The time has come for you to hear my side of the story!"

    scene norikorestaurant9
    with dissolve

    n "And...for me to maybe feel like I’m not just chasing after a ghost again..."

    scene black
    with dissolve2

    "I take a moment to ponder over what Noriko meant by that, and confirm to myself that it’s likely about that “disappearing act” I put on a while back."
    "I don’t know how many times she needs me to remind her that I don’t know anything about what happened back then, but..."
    "I guess it wouldn’t be harmful to learn more about how things were for her when hearing Niki’s side didn’t cause me to malfunction in any way."
    "Even now that I’m starting to become a little more hesitant to get filled in on details of the past (Thanks, Maya), I’m almost positive that it’s only details about {i}me{/i} that have the chance of frying my brain."
    "And, if Noriko wants me to know about {i}her{/i}, after all, it’s not like I can avoid this forever."

    if bonus == True:
        "Every single detail I can learn and memorize about her brings me one step closer to getting her shirt off again."
        "And that’s why I’m here, after all."
        "..."
        "That’s..."

    stop music

    "We {b}WALK{/b} to the {b}RESTAURANT.{/b}"

    scene norikorestaurant10
    play music "samhain.mp3"

    n "Wow...I knew this place would be kinda nice based on what she said, but...this is a little fancier than I was expecting."
    n "I would have worn my {i}nice{/i} clothes if I had known it was going to be a place like this."
    s "You? Nice clothes? Impossible."

    scene norikorestaurant11
    with dissolve

    n "Hey. Don’t go forgetting that I was always the one who wanted to dress up when we were younger. It was Nee-chan who was always trying to stay in sweatpants for as long as physically possible."
    n "Did most of that desire to dress up come from an overwhelming need to impress you? Of course. But even though I rarely do it anymore, I still like feeling pretty from time to time."
    s "Well you certainly pulled off that dress for your parents’ restaurant, so I can see it."

    scene norikorestaurant12
    with dissolve

    n "Do you think they have falafel here?"
    s "Probably not, Noriko. "
    n "They should have falafel here. I’m going to speak to the manager."
    s "Please don’t. The less attention I have for being on a date with a [teenage]girl, the better."
    k "Friend!"

    scene norikorestaurant13
    with fade

    if bonus == True:
        k "You have found yet another [young_girl] to waste away your days with! How exciting!"
    else:
        k "You have found yet another human female to waste away your days with! How exciting!"

    k "And this one looks just like the cotton candy girl! But spikier and less confident!"
    s "Kaori, how are you balancing those wine glasses on a plate you’re holding sideways?"
    k "It is not sideways! That is just what you imagine it to be! "
    k "The plate is a plate! And the glass tubes of fermented grape blood stand as tall as trees!"
    k "Drink them and you shall become them! Grapes!"
    s "Okay, Kaori."

    scene norikorestaurant14
    with dissolve

    k "Are you in trouble, {i}smaller{/i} cotton candy human?"
    n "I’m good! I was actually just wondering if you had falafel here, though. Or like...maybe portobello burgers or something? "
    s "Noriko, they don’t-"
    k "Spiced bean circles and cruelty free fungus burgers for the pink one! Thank you for your contribution to the animal kingdom!"
    s "Okay, then. I guess they do have...whatever you ordered after all."

    scene norikorestaurant15
    with dissolve

    k "Has your tongue signaled to your brain what it wants to taste yet, Friend?"
    s "I’ll have-"
    k "I understand! I will get that for you sooner than you can say “loxosceles reclusa!”"
    s "Loxosceles reclusa."

    scene norikorestaurant16
    with dissolve

    k "Ah! Too quick! Stop doing the words!"
    s "Loxosceles reclusa."

    scene norikorestaurant17
    with dissolve

    k "MY POWER WANES! I GROW WEAKER WITH EACH UTTERANCE!"
    k "GOODBYE FRIENDBURGER. ENJOY DEVOURING THE HAIR OF YET ANOTHER FEMALE."

    scene norikorestaurant18
    with fade

    n "Are you really going to eat my hair, Sensei?"
    s "What? No."
    n "Because you can if you want. I don’t mind."
    s "You definitely should mind. That’s not a normal thing people do."

    if bonus == True:
        n "No. But I was watching My Strange Addiction with Kirin the other day and there was this one guy who had sex with those giant blow up pool animals. "
    else:
        n "No. But I was watching My Strange Addiction with Kirin the other day and there was this one guy who was {i}really{/i} into those giant blow up pool animals. "

    n "All things considered, I think wanting to eat my hair is pretty normal by comparison. Besides, it grows back pretty quickly anyway."
    n "I think it’s the color. It sounds easier for pale skin to produce pink hair than it would be to produce like black or...brown or whatever."
    s "Why are you still talking about this?"

    scene norikorestaurant19
    with dissolve

    n "Becaaaaaaaaause...I’m nervous?"
    n "Obviously we’ve been hanging out a lot lately and...it’s starting to really set in that you’re {i}back{/i}...but this is the first like, {i}real{/i} date we’ve been on."
    n "I was doing okay until you called it that a few minutes ago, but ever since then I’ve just been like, “Holy shit. I’m on a date with Sensei. It’s finally happening.”"
    s "So obviously, the best course of action is to start a conversation about eating hair in order to make sure the date is a success."

    scene norikorestaurant20
    with dissolve

    n "Obviously. I mean, it’s better than bringing up something like politics or our stances on whether or not circumcision is cruel."

    if bonus == True:
        s "If that’s your idea of a segue into the “concept of my penis,” I would like to take this moment to commend you for near flawless execution."
    else:
        s "None of these are good conversation topics. Where is Kaori? I want the bill."

    n "I’m just trying to stop shaking, to be totally honest."

    scene norikorestaurant21
    with dissolve

    n "I learned this trick where if you stop crossing your arms and legs and just kinda sit up straight and regulate your breathing, it helps with nervousness."
    n "I figure if I just keep this up for the next three hours or so, I’ll finally be able to come out and ask you what I’ve been meaning to ask you since the beach."
    s "I highly doubt we’re going to be here for that long, so why don’t you just go ahead and start filling me in on your super secret backstory until then?"

    scene norikorestaurant22
    with dissolve

    n "Hah..."
    s "..."

    if bonus == True:
        n "You won’t be upset if there’s actually minimal penis in the story, would you? I know I lured you over here with promise of that being a big thing, but it’s really not."
        s "It definitely is."
        n "No, it’s-"

    scene norikorestaurant23
    with dissolve

    if bonus == True:
        n "Oh, like actual size. "
        n "Yeah. In that regard, it is {i}definitely{/i} a big thing."
        n "I just mean that the whole...sexually explorative yet still nervous Noriko isn’t as important as the...frantic lost sheep Noriko of the past."

    n "I’m sure Niki told you about how she went through that whole period of depression and reinvention stuff after you left, right?"
    s "Right. And it got significantly darker than I ever expected it to."

    scene norikorestaurant22
    with dissolve

    n "What happened with me really wasn’t all that {i}dark{/i} by comparison."
    n "If anything, it was probably one of the most active parts of my life."
    n "You see, I wasn’t like Nee-chan in the fact that you weren’t completely opposed to seeing me anymore like you were with her."
    n "And once you let me back into your life, I was ecstatic. "
    n "I saw an opportunity to try and pull you back, little by little, while getting closer to you at the same time and showing you that I was...smart."
    n "Smart and fun and lovable. Like a little sister cross bred with what I imagined your dream girl would be. And for a while, I felt like we really {i}were{/i} in a good place."
    n "So good that part of me wanted to forget you and Nee-chan were ever in love in the first place...and that you were like my secret prince or something along those lines."
    n "Little by little, your name stopped coming up back at home. Not just because Nee-chan couldn’t see you anymore, but because I wanted to keep you all to myself."
    n "So I’d wake up on the weekends, make myself look as pretty as I could, and wait patiently by the stairs for my parents to drive me over to that grody, crumbling building where you taught me so many things."
    n "It was like a second home. A castle, even. A place for my prince and me to be alone."
    n "And even if it wasn’t the most desirable looking building in all of Kumon-mi, I didn’t care. Because for a few hours every week, it was the most beautiful place in the whole wide world."

    play sound "static.mp3"
    scene norikorestaurant24 with flash
    stop sound

    n "Lots of girls came and went over that short period of time- probably due to a mix of exactly what you were teaching and where you were teaching it."
    n "And I would have been happy if things stayed that way forever."
    n "I would have waited until you got an actual teaching job and then enrolled at whatever[school] hired you, no matter how far away it was."
    n "But, of course, a nasty streak of poor luck landed somebody else in that same exact castle of ours."
    s "..."
    n "..."

    play sound "static.mp3"
    scene norikorestaurant25
    with flash
    stop sound

    n "I liked Maya. I really did. "
    n "I thought she was cool and...really, {i}really{/i} mature for her age."
    n "She reminded me a lot of you."
    n "And I guess she reminded {i}you{/i} of you too, since you took to her immediately."
    n "Soon enough, the castle for two turned into a castle for three."
    n "But every time I tried to move closer, the same way I’d been doing since I met you, it would be like you’d just move even further away in response."
    n "And then one day...you moved further away than I ever expected you to."
    n "It came out of nowhere and, I won’t lie, I was crushed."

    play sound "static.mp3"
    scene norikorestaurant24
    with flash
    stop sound

    n "But unlike Nee-chan, who was content wallowing in self-pity forever, I was going to do something about it."
    n "I took it upon myself to go out and find you because I didn’t think you’d ever leave if you really had a choice."

    play sound "static.mp3"
    scene norikorestaurant26 with flash
    stop sound

    n "I looked everywhere. Or at least as many places a girl with access to only public transportation and a capped data plan on her phone could look."
    n "But Kumon-mi’s a big fucking place, Sensei. And even bigger when you have no idea where you’re going."

    play sound "static.mp3"
    scene norikorestaurant26 with flash
    stop sound

    n "But then...I fucking found you."
    n "Out of the window of a bus in the old district, I caught you from the corner of my eye [[redacted] with [[redacted]."

    play sound "static.mp3"
    scene norikorestaurant27 with flash
    stop sound

    n "I begged the driver to stop so I could get off and chase you down and wrap my arms around you and ask you to come home."
    n "But of course, {i}she{/i} [[redacted]."

    play sound "static.mp3"
    scene norikorestaurant28 with flash
    stop sound
    stop music
    play music "soda.mp3"

    n "I couldn’t believe it. Here I was just inches away from finally finding you and [[redacted]."
    n "[[redacted]"
    n "{b}STOP PLAYING LESSONS IN LOVE{/b}"

    play sound "static.mp3"
    scene norikorestaurant29 with flash
    stop sound
    play music "shiningstarvocals.mp3"

    "///////////////////EVENT IS NO LONGER IN SYNC WITH EXPECTATIONS"
    "///////////////////PLEASE ENJOY THIS COMPLIMENTARY ADJUSTMENT AS A THANK YOU FOR YOUR CONTINUED SUPPORT AS WE ATTEMPT TO REPAIR YOUR CONNECTION"

    play sound "static.mp3"
    scene norikorestaurant30
    with flash
    stop sound
    play music "phonering.mp3"
    $ renpy.pause(10, hard=True)

    "Would you like to phone?"
    menu:
        "Phone":
            if bonus == True:
                play sound "static.mp3"
                stop music
                scene norikorestaurant2 with flash
                scene norikorestaurant26 with flash
                scene norikorestaurant31 with flash
                scene norikorestaurant32 with flash
                stop sound
                jump restofnorikorestx
            else:
                scene black

                "///////////////////EVENT FAILED"

                $ renpy.end_replay()
                $ norikodorm25 = True
                $ noriko_love += 3

                "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
                "........."
                "......"
                "..."

                if day >= 6:
                    jump endofsat
                else:
                    jump endofweekday
