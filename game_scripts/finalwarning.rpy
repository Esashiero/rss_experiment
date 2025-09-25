label resetsix1:
    $ day = 1
    show monday onlayer date
    hide saturday onlayer date
    play sound "static.mp3"
    scene escapetheroom1 with flash
    stop sound
    play music "iamhome.mp3"

    "Maya disappears, but I manage to find my way back home all by myself."
    "I’m still hungry, so I should probably think about making dinner."
    "The only problem is that, with Ami gone, doing that could take forever! And this house has limited ingredients!"
    "If only there was someone who could show up and tell me what I’m supposed to do or how I’m supposed to do it."

    s "..."
    s "..."
    s "..."

    s "{i}I said...{/i}if only there was someone who could show up and tell me what I’m supposed to do or how I’m supposed to do it. "

    "..."
    "..."
    "..."
    "Hmm...shoot. It seems I won’t be able to narrate myself out of this one."
    "I guess I’ll just have to rely on the puzzle-solving skills I’ve gained throughout my time here so far and-"

    play sound "pabell.mp3"

    "Oh! Never mind! It looks like someone is here to help me after all."

    scene escapetheroom2 with fade

    vpa "Today is Monday. The weather outside is currently ninety-four degrees Fahrenheit. "
    vpa "There is a 30%% chance of rain around 1:00 PM, with scattered showers forecasted to appear at 9:00 PM and continue throughout the night."
    vpa "You are happy here. There is no reason for you to ever leave."
    vpa "The world outside is dark and dreary and it is there where you will hurt the most."
    vpa "Remember to smile, Akira Arakawa. Be content within these walls."
    vpa "For the moment you leave them, your world will break apart. "
    vpa "And you are far too weak to ever put it back together."

    scene escapetheroom1
    with fade

    "Wow, that sounds ominous."
    "How do I want to spend my day?"

    menu escaperoommainmenu:
        "Check the kitchen":
            jump escaperoomkitchen
        "Check the door":
            jump escaperoomdoor
        "Live happily":
            jump escaperoomlive
        "Use the computer":
            jump escaperoomcomputer
        "Use your phone" if escaperoomphone == True:
            jump escaperoomcellmenu
        "Go to sleep":
            jump escaperoomsleep

label escaperoomlive:
    menu:
        "Trash can" if escapekey1 == False:
            jump escaperoomtrash
        "Rabbit doll" if escapekey2 == False:
            jump escaperoomrabbit
        "Freezer" if escapemelon == False:
            jump escaperoomfreezer
        "Refrigerator" if escapeshampoo == False:
            jump escaperoomfridge
        "Top shelves":
            jump escaperoomtopshelves
        "Microwave" if escaperoomphone == False:
            jump escaperoommicrowave
        "Coffee maker" if escapekey3 == False:
            jump escaperoomcoffee
        "Cabinet (Bottom left)" if escapeparrot == False:
            jump escaperoombotleft
        "Cabinet (Bottom right)" if escapedog == False:
            jump escaperoombotright
        "Floor mat" if escapelionfish == False and havefish == False:
            jump escaperoomfloor
        "Schedule":
            jump escaperoomschedule
        "Television":
            jump escaperoomtv

label escaperoomkitchen:
    scene escapetheroom3
    with fade

    menu escaperoomkitchenmenu:
        "Check the main room":
            scene escapetheroom1
            with fade
            jump escaperoommainmenu
        "Hot pot" if escapekey6 == False:
            jump escaperoomhotpot
        "Fall in love" if escapekey5 == False:
            jump escaperoomlover
        "Use Ami’s computer":
            jump escaperoomamipc
        "Use your phone" if escaperoomphone == True:
            jump escaperoomcellmenu
        "Go to sleep":
            jump escaperoomsleep

label escaperoomsleep:
    s "Time to hit the hay."

    scene black
    with dissolve2

    "I collapse into my chair at the table and close my eyes."
    "I stopped using the bed a long time ago."
    "It’s too full of memories of her."

    "........."
    "......"
    "..."

    jump escaperoomdaychange

label escaperoomdaychange:
    if day == 1:
        hide monday onlayer date
        show tuesday onlayer date
        $ day = 2
    elif day == 2:
        hide tuesday onlayer date
        show wednesday onlayer date
        $ day = 3
    elif day == 3:
        hide wednesday onlayer date
        show thursday onlayer date
        $ day = 4
    elif day == 4:
        hide thursday onlayer date
        show friday onlayer date
        $ day = 5
    elif day == 5:
        hide friday onlayer date
        show saturday onlayer date
        $ day = 6
    elif day == 6:
        hide saturday onlayer date
        show sunday onlayer date
        $ day = 7
    elif day == 7:
        hide sunday onlayer date
        show monday onlayer date
        $ day = 1

    scene escapetheroom1
    with dissolve2

    "Today is a new day."
    "I wonder what sort of adventure it will bring?"

    jump escaperoommainmenu

label escaperoomdoor:
    scene escapetheroom4
    with fade

    menu escaperoomdoormenu:
        "Check the main room":
            scene escapetheroom1
            with fade
            jump escaperoommainmenu
        "Look down":
            jump escaperoomdelivery
        "Check the vent" if escapecentipede == False:
            jump escaperoomvent
        "Check the lockers":
            jump escaperoomlockers
        "Open the door" if escapepiece1 and escapepiece2 and escapepiece3 and escapepiece4 and escapepiece5 and escapepiece6 and escapepiece7 and escapepiece8 and escapepiece9 and escapegun:
            jump escaperoomexit
        "Use your phone" if escaperoomphone == True:
            jump escaperoomcellmenu
        "Go to sleep":
            jump escaperoomsleep

label escaperoomcomputer:
    if escapepcunlocked == False:
        scene escapetheroom5
        with fade
        "Shoot. It looks like the computer requires a password."
        "I hope I can remember it."

        jump escaperoompcpass
    else:
        scene escapetheroom6
        with fade
        "I enter my password in the machine and decide to spend my free time browsing the web."

        jump escaperoompcuse

label escaperoompcpass:
    $ escaperoompcstrip = renpy.input("ENTER PASSWORD...")
    $ escaperoompcstrip = escaperoompcstrip.strip()

    if escaperoompcstrip != "baby":
        play sound "computerboo.mp3"
        "This password is incorrect."

        menu:
            "Try again":
                jump escaperoompcpass
            "Give up":
                s "Hmm...maybe the password will come back to me later?"
                s "I’ll do something else for now."

        scene escapetheroom1
        with fade

        jump escaperoommainmenu

    if escaperoompcstrip == "baby":
        play sound "computeryay.mp3"
        scene escapetheroom6
        $ escapepcunlocked = True

        s "Yay. I managed to remember the password."
        s "What should I do now?"

        jump escaperoompcuse

    menu escaperoompcuse:
        "Order mystery box 1" if mysbox1ordered == False and escapegun == False:
            if day == 5:
                "Today is pay day, so I should have some extra cash to spend on an Internet mystery box."

                scene black
                with dissolve
                play sound "computeryay.mp3"

                "I enter my credit card information into the computer and smile as I spend my allowance on a mysterious object."
                "I hope it will change my life in some way."
                "{i}Eager to receive your mystery box, you go to sleep early.{/i}"
                "{i}When the morning comes, your mouth is dry and your heart is pounding.{/i}"
                "{i}You can’t help but feel like you’re missing something. You just don’t know what.{/i}"
                "{i}And as you open your eyes to the same sights you always see, you listen to the sound of the clock — terrified of what the ticking means now.{/i}"

                $ mysbox1ordered = True

                jump escaperoomdaychange
            if day != 5:
                play sound "computerboo.mp3"

                "I try to order a mystery box, but my credit card is declined."
                "I hate when that happens."

                jump escaperoompcuse

        "Order mystery box 2" if mysbox2ordered == False and escapekey8 == False:
            if day == 5:
                "Today is pay day, so I should have some extra cash to spend on an Internet mystery box."
                "I find one that looks interesting, but it’s still a little out of my price range."

                s "Hmm...I wonder if there’s some sort of discount code I can use?"
                s "No harm in trying, I guess."

                jump escaperoompcdiscountenter

            if day != 5:
                play sound "computerboo.mp3"

                "I try to order a mystery box, but my credit card is declined."
                "I hate when that happens."

                jump escaperoompcuse

        "Play music":
            "I decide to change up the BGM."
            "What song do I want to listen to?"

            menu:
                "“I Am Home”":
                    play music "iamhome.mp3"
                    play sound "computeryay.mp3"
                    "The song changes, and I feel at home once more."
                    jump escaperoompcuse
                "“Shining Star”":
                    play music "ShiningStarVocals.mp3"
                    play sound "computeryay.mp3"
                    "The song changes, and I want to throw up."
                    jump escaperoompcuse
                "“10c”":
                    play music "10c.mp3"
                    play sound "computeryay.mp3"
                    "The song changes, and I feel stuck."
                    jump escaperoompcuse
                "“Sweet Vermouth”":
                    play music "sweetvermouth.mp3"
                    play sound "computeryay.mp3"
                    "The song changes, and I am overcome with shame."
                    jump escaperoompcuse
                "“Smells of Summer”":
                    play music "smellsofsummer.mp3"
                    play sound "computeryay.mp3"
                    "The song changes, and I am filled with regret."
                    jump escaperoompcuse

        "Watch porn":
            "What kind of porn do I want to watch?"
            menu escaperoompornmenu:
                "Mom & daughter share HUGE cock! (Real incest)":
                    jump escapeporn1
                "Desperate Teen Does anything for Cash":
                    jump escapeporn2
                "Nympho whore loves BBC":
                    jump escapeporn3
        "Write":
            scene black
            with dissolve
            play sound "computeryay.mp3"

            "I open up Microsoft Word and attempt to put my feelings into poetry."
            "But with no one to share it with, all it does is remind me of my flaws."
            "Sometimes, it feels like there’s no point to any of this. That I’m only writing to keep myself a step or two away from death."
            "I know it will catch up to me some day."
            "But for now, this is all I can do."
            "..."
            "This is all I can do."
            "{i}You write until you’re half-asleep, then give up and close your eyes.{/i}"
            "{i}When you wake up, you realize you’ve accomplished nothing. That the night was spent on someone else’s words instead of yours.{/i}"
            "{i}What remains on the screen is a mirror-image of what they once felt — all dressed up in Times New Roman.{/i}"
            "{i}You hear her footsteps in your head.{/i}"
            "{i}It’s like they never go away.{/i}"

            jump escaperoomdaychange

        "Stop using the computer":
            s "On second thought, I don’t want to do this right now."

            scene escapetheroom1
            with fade

            jump escaperoommainmenu

label escaperoompcdiscountenter:
    $ escaperoompcdiscount = renpy.input("ENTER DISCOUNT CODE...")
    $ escaperoompcdiscount = escaperoompcdiscount.strip()

    if escaperoompcdiscount == "46782" and luckynumberyay == 46782:
        jump escaperoomdiscountcorrect
    elif escaperoompcdiscount == "99635" and luckynumberyay == 99635:
        jump escaperoomdiscountcorrect
    elif escaperoompcdiscount == "392354" and luckynumberyay == 392354:
        jump escaperoomdiscountcorrect
    else:
        play sound "computerboo.mp3"
        "This discount code is invalid."

        s "Darn it. Now what?"

        menu:
            "Try again":
                jump escaperoompcdiscountenter
            "Give up":
                s "Ugh. I guess I’ll just have to do something else."
                jump escaperoompcuse

label escaperoomdiscountcorrect:
    scene black
    with dissolve
    play sound "computeryay.mp3"

    "The discount code is accepted and I shift forward in my seat, excited and impressed by my aptitude for bargain-hunting."
    "I enter my credit card information into the computer and smile as I spend my allowance on a mysterious object."
    "I hope it will change my life in some way."
    "{i}Eager to receive your mystery box, you go to sleep early.{/i}"
    "{i}When the morning comes, you must peel your flesh off of the vinyl coating on your table.{/i}"
    "{i}It’s a sensation that used to bother you. But now, it’s more like a reminder that you’ve managed to make it this far.{/i}"
    "{i}When you open your eyes, you set your sights on the window — remembering what it was like to go outside.{/i}"
    "{i}You remember how you always hated the sun. And how its forced absence, enacted by the walls of your home, protects you.{/i}"
    "{i}You are safe here.{/i}"
    "{i}Everywhere else is dangerous.{/i}"

    $ mysbox2ordered = True

    jump escaperoomdaychange

label escapeporn1:
    scene escapetheroomporn1 with fade
    play sound "computeryay.mp3"

    porn1 "Mmnch...mlm...mnch..."
    porn2 "Aah! Aah! Hah!...Ngaah! Fuck me! Fuck...me!"
    porn1 "You like that, baby? You like my daughter’s pussy?"
    porn2 "I can’t...take it! It’s too big! It’s...driving me insane!"
    porn1 "I didn’t raise a quitter, did I? Don’t you want to see this through to the end?"
    porn2 "AAAAAaaaaAAAAAAaaaaahh!!!!!!"

    "In this video, a mother and her daughter can be seen having a threesome with a large man, roughly twenty years older than them based on appearance alone."
    "His penis is likely between ten and twelve inches long, and it is impressive that the daughter is able to fit most of it inside of her vagina."
    "The man aggressively pounds the daughter until her eyes roll to the back of her head, and her mother provides support by embracing her from behind."
    "The two of them kiss with no resistance whatsoever. It leads me to believe they do this often. And I begin to ponder just how many men they must have shared previously."
    "The two women take turns riding the man’s penis and I can’t help but be impressed by his endurance as he’s yet to ejaculate even once."
    "I grip my cock through my underwear, tugging it in a way that creates a friction burn on the head as I do my best to follow the man’s lead."
    "Unfortunately, I am weaker than him. And I ejaculate into my underwear the moment the mother begins to play with her daughter’s clitoris."
    "I wonder how the father must feel. And I wonder if he, too, ejaculates while watching his family have sexual intercourse."

    scene escapetheroom1
    with fade

    jump escaperoommainmenu

label escapeporn2:
    scene escapetheroomporn2 with fade
    play sound "computeryay.mp3"

    porn3 "Can you tell me your name?"
    porn4 "Do I have to? I thought this was, like...an anonymous thing."
    porn3 "Just your given name is fine. We’ll blur your face so you can stay anonymous."
    porn4 "Then...you can call me Chinami."
    porn3 "You’re very pretty, Chinami. Are you a virgin?"
    porn4 "Mmm...no. Hahahah~"
    porn3 "Do you have sex often?"
    porn4 "Not really. I’m definitely not a virgin, though."
    porn3 "Do you have a favorite position?"
    porn4 "Mmmm...does sucking dick count?"
    porn3 "You like to suck dick?"
    porn4 "Yeah~"
    porn3 "Do you swallow?"
    porn4 "Mhmmm...every time~"
    porn3 "Are you okay with sucking my dick on camera today?"
    porn4 "Mmmm...yeah~"
    porn3 "Excellent. Could you go ahead and take your top off for me?"
    porn4 "Like this?~"

    "In this video, a girl is brought into an empty-looking room so she can perform sex acts in exchange for what I imagine will be money or exposure."
    "She starts by taking her clothes off while the man films her and asks her various interview questions."
    "Eventually, she takes off his pants and begins to perform fellatio."
    "She looks like she knows what she’s doing."
    "She keeps her eyes closed while slowly easing more of his penis into her mouth."
    "Her face begins to flush red as she gets caught up in the mood, which prompts the man to lay her down on his desk so he can insert his penis into her vagina."
    "She looks mildly uncomfortable at first, but begins to enjoy herself within several minutes."
    "The man asks if he can ejaculate inside of her and she tells him he can. So he does."
    "And so do I when the video comes to an end."

    scene escapetheroom1
    with fade

    jump escaperoommainmenu

label escapeporn3:
    scene escapetheroomporn3 with fade
    play sound "computeryay.mp3"

    porn5 "AAAAaaaAAAAaaaAAAAHHHH FUUUUUUUUuuuuuuUUUUUuuuuck!"
    porn6 "Yeah, you fucking like that? You fucking like that?!"
    porn5 "AaaAaaaAAAAaaaAAAAHHHAhhaahhahhhayessssss! IIIiiIIIiii’m gonnaaAAAaaaa cuUUUuuuMM!"
    porn6 "Thirsty bitch...thirsty fucking bitch! Tell me you love this dick! Tell me you love this dick!"
    porn5 "IIiiiIIII loOOOoooOOve yoOOOoouuuUUUuurr diIIiiiIIiiick!!!!"

    "This video involves a man and a woman enraptured by the sensations of consensual copulation."
    "Based on the title, I can imagine the woman involved is what many would call “loose,” meaning that she is very experienced sexually."
    "This is further evidenced by the manner in which she is able to be repeatedly pounded without so much as wincing."
    "The pair perform their coital routine in various positions, some of which I’ve never seen before. And I think about what it would take to replicate them."
    "Unfortunately, all I have with me is my hand. So I will be unable to do that today."
    "Thankfully, the film is alluring enough for me to bring myself to ejaculation. And I am now free to go back to my business both relieved and depressed."

    scene escapetheroom1
    with fade

    jump escaperoommainmenu

label escaperoomtrash:
    if day == 4:
        scene escapetheroom8
        with fade

        s "Wow! My trash can is so clean now! And full of curious objects and trinkets!"
        peg "Greetings, human. I am the Emissary of Pegasus — and I have come to you with an important message."
        peg "But first, you must prove your loyalty by telling me how to find the sunset."
        s "What does the Emissary of Pegasus need to find the sunset for?"
        peg "Harnessing the power of the sunset is the only way for me to illuminate my special key. But there will be no further use for it once that key is gone."
        s "I could just take the key off your hands? I’m sure I could find some sort of use for it."
        peg "Unfortunately, I am unable to simply give it to you without proof of loyalty first."
        peg "So please, tell me how to find the sunset."
        s "Well...first, you-"

        menu:
            "Say goodbye to Pedro":
                $ pegapoints += 0
            "Throw some darts at Steven":
                $ pegapoints += 0
            "Say hello to Frankie":
                $ pegapoints += 1
            "Drop a tooth in Salem":
                $ pegapoints += 0

        s "Then, you-"

        menu:
            "Skin your kneecaps":
                $ pegapoints += 0
            "Remove your tongue":
                $ pegapoints += 1
            "Polish your eyeballs":
                $ pegapoints += 0
            "Stomp your feet":
                $ pegapoints += 0

        s "Then-"

        menu:
            "Run in circles seven times":
                $ pegapoints += 1
            "Walk in circles four times":
                $ pegapoints += 0
            "Run in circles nine times":
                $ pegapoints += 0
            "Walk in circles three times":
                $ pegapoints += 0

        s "Then, you have to-"

        menu:
            "Spit on the ground":
                $ pegapoints += 0
            "Tie your shoes beneath a tree":
                $ pegapoints += 0
            "Stare up at the sky":
                $ pegapoints += 1
            "Watch eleven Youtube videos":
                $ pegapoints += 0

        s "This next one is important. You must say to a face-"

        menu:
            "Hey, you! Nice face!":
                $ pegapoints += 0
            "Your hot sauce is delicious":
                $ pegapoints += 1
            "I’m afraid of the super moon":
                $ pegapoints += 0
            "There is no god":
                $ pegapoints += 0

        s "Then-"

        menu:
            "Spin":
                $ pegapoints += 1
            "Gyrate":
                $ pegapoints += 0
            "Dance":
                $ pegapoints += 0
            "Jump":
                $ pegapoints += 0

        s "Then, the final step is-"

        menu:
            "Putting your socks back on":
                $ pegapoints += 0
            "Turning the lights off":
                $ pegapoints += 0
            "Shearing nine sheep":
                $ pegapoints += 0
            "Taking a drink":
                $ pegapoints += 1

        s "And I’m pretty sure that’s all you need to do."
        peg "..."
        s "Did I get it right?"

        if pegapoints == 7:
            peg "You certainly did."
            peg "You have proven your loyalty. And, in doing so, you have earned my special key."

            scene escapetheroom9
            play sound "winner.mp3"
            $ escapekey1 = True

            "{i}You have obtained a “Pegasus Key!”{/i}"

            scene escapetheroom10

            peg "This key will help you in the coming days, but please be sure to only use it if you are absolutely certain you {i}have{/i} to."
            peg "The world outside these walls is a terrifying-"
            s "Yeah, yeah. I’ve heard it all before."
            peg "But-"
            s "Thanks for the key, Emissary of Pegasus. But I’ve got a whole bunch of crumpled up paper I have nothing to do with, so you’re going to have to deal with that for a little while."
            s "Sorry, man."
            peg "I don’t think you-"

            scene escapetheroom7
            with dissolve

            "I fill the trash can back up and prepare myself for another garbage day."
            "Now, time to figure out what to do with this key."

            scene escapetheroom1 with fade

            jump escaperoommainmenu

        else:
            peg "No."
            peg "I’m afraid this means you have {i}not{/i} proven your loyalty, and that you must retrace your steps if you are ever going to."
            s "But I’ve taken so many steps. Surely you don’t expect me to remember them all?"
            peg "And surely {i}you{/i} don’t expect me to assist in the efforts of someone who does not deserve my aid."

            scene black
            with dissolve2
            $ pegapoints = 0

            peg "Until we meet again, Akira."
            s "Wait! Emissary of Pegasus!"

            "{i}You feel wave of exhaustion crash into your body. And, the next thing you know, you’re waking up all over again.{/i}"

            jump escaperoomdaychange

    else:
        scene escapetheroom7
        with dissolve

        "I gaze into the trashcan to find a bunch of crumpled up papers that I don’t remember putting there."
        "I can’t remember the last time garbage was collected, but I sure hope it comes again soon so I can remember what the bottom of my trash can looks like."
        "Until then, I guess I’ll have to just store all of my surplus trash in the shower like I normally do."
        "Here’s to hoping it attracts more friends."

        scene escapetheroom1
        with fade

        jump escaperoommainmenu

label escaperoomrabbit:
    if rabbitpoint == 0:
        scene escapetheroom11 with fade

        "I approach a stuffed rabbit sitting on top of the refrigerator."

        rabbit "How can I be of service-pyon?"
        s "“Pyon?”"
        rabbit "It’s a rabbit noise-pyon. We say it so you know we are rabbits-pyon."
        s "Would the ears and bowtie and other rabbit-like features not be enough to do that?"
        rabbit "We don’t know-pyon. We never live long enough to find out-pyon."
        s "Right...Well, can you pass me the EnviroKids Organic Gorilla Munch Cereal please?"
        rabbit "No-pyon. You haven’t earned it yet-pyon."
        s "Well, what can I do to earn it? I’m really hungry and wanted to spend the day eating EnviroKids Organic Gorilla Munch Cereal."
        rabbit "That’s a good question-pyon! Unfortunately, I don’t have the answer-pyon."
        s "Ughhhhh. You stuffed rabbits are always so confusing."
        rabbit "Sorry-pyon! But maybe you can do something with this-pyon?"

        scene escapetheroom12
        play sound "winner.mp3"

        "{i}You have obtained a “Nostalgic sex toy”{/i}"

        scene escapetheroom13

        s "What am I supposed to do with this?"
        rabbit "Don’t ask me-pyon! I’m just a rabbit-pyon!"
        rabbit "I’ll keep a close eye on what you’re doing though-pyon. Your cereal isn’t going anywhere-pyon!"
        s "Fine. Guess I’ll just have to deal with this stupid vibrating thing for now."
        rabbit "That’s the spirit-pyon!"

        $ rabbitpoint += 1

        scene escapetheroom1 with fade

        s "Great. Now what?"

        jump escaperoommainmenu

    elif rabbitpoint > 0 and rabbitpoint < 7:
        scene escapetheroom13 with fade

        rabbit "Hello again-pyon!"
        s "Hello, freezer rabbit. Have I earned the EnviroKids Organic Gorilla Munch Cereal yet?"
        rabbit "Not yet-pyon! But keep at it and I’m sure you will eventually-pyon!"
        s "Ughhhhhhh."

        scene escapetheroom1 with fade

        s "Forget it. I’ll just do something else for now."

        $ rabbitpoint += 1

        jump escaperoommainmenu

    elif rabbitpoint == 7:
        scene escapetheroom13 with fade

        rabbit "Hello again-pyon!"
        s "Now, you listen here, freezer-rabbit. I’m tired of you holding the EnviroKids Organic Gorilla Munch Cereal hostage. And I’m not going to stand for it anymore."
        rabbit "You sound angry-pyon!"
        s "I {i}am{/i} angry-pyon. All I want is some cereal and you won’t give me any. This is child abuse."
        rabbit "Sounds like you know a lot about child abuse-pyon!"
        s "Just give me the cereal or I am going to throw you into the oven."
        rabbit "Hmmmm...pyon."
        rabbit "Well, you {i}have{/i} been pestering me rather frequently-pyon. And some extra leg room does sound nice-pyon."
        rabbit "So...okay-pyon! Here you go-pyon!"

        scene escapetheroom14
        play sound "winner.mp3"

        "{i}You have obtained “EnviroKids Organic Gorilla Munch Cereal”{/i}"

        scene escapetheroom15

        rabbit "Are you happy now-pyon?"
        s "Very. Now, I just need to- wait a minute."
        rabbit "Is something the matter-pyon?"
        s "I can hear something whirring inside of the box."
        rabbit "It’s probably a prize-pyon! Cereal always comes with a prize-pyon!"
        s "Should I pull it out?"
        rabbit "Do it-pyon! Now-pyon!"

        "I reach into the cereal box and-"

        scene escapetheroom16
        play sound "winner.mp3"
        $ escapekey2 = True

        "{i}You have obtained a “Cereal Key”{/i}"

        scene escapetheroom15

        s "Wow. I had no idea they were putting keys in cereal nowadays. Times have really changed."
        rabbit "Did you read the fine print on the key-pyon?"
        s "The what?"
        rabbit "The fine print-pyon! The rules of the prize!"
        s "Ugh. No, hold on."

        "I stare down at the key and read."

        s "Note...this key will self-destruct if you maintain possession of EnviroKids Organic Gorilla Munch Cereal."
        rabbit "Uh-oh-pyon! Looks like you need to give the cereal back-pyon!"
        s "Gosh darn it. This is the last time I ever buy an EnviroKids product."
        rabbit "At least you got a key-pyon! May it help you in the coming days-pyon!"

        scene escapetheroom13 with dissolve

        s "Shut up, freezer rabbit. I’m never talking to you again."
        rabbit "Farewell-pyon! It’s been fun-pyon!"

        scene escapetheroom1
        with fade

        s "Well...at least I have another key now."

        jump escaperoommainmenu

label escaperoomfreezer:
    scene escapetheroom17
    with fade

    "I make my way over to the freezer and notice there is something peculiar about it — namely the fact that I’m not supposed to store food inside."
    "Either way, I don’t have the time to worry about what I can and can’t make cold. I need to do something. And I need to do something right now."
    "But what should I do?"

    menu escapefreezermenu:
        "Punch the freezer":
            scene escapetheroom17 with hpunch
            play sound "tackle.mp3"

            s "Hi-ya!"

            "The freezer shakes, but not much else happens."

            jump escapefreezermenu

        "Caress the freezer":
            "I gently stroke the freezer, hoping it becomes aroused and opens itself up."
            "Unfortunately, nothing happens."

            jump escapefreezermenu

        "Insert roach" if escaperoach == True:
            s "I wonder if this will work?"

            "Without knowing what else I’m supposed to do, I insert the roach I got from Molly into the freezer’s mouth..."

            play sound "lock.mp3"
            scene escapetheroom18

            "And it suddenly opens!"

            s "Oh boy. I can’t wait to see what’s inside."

            scene black
            with dissolve2

            "........."
            "......"
            "..."

            scene escapetheroom19
            with dissolve2

            s "Hey, wait a minute. I thought I wasn’t supposed to store food in here?"

            "A melon stares back at me and reminds me of better days...but I’m not supposed to touch it. Not even for sex."

            s "..."
            "..."
            s "..."
            "..."
            s "..."
            "..."
            s "..."
            "..."
            s "..."
            "..."

            "Rules are meant to be broken."

            s "Time for melon sex."

            scene escapetheroom20 with hpunch
            play sound "tackle.mp3"

            m2 "Cha cha cha. Intruder alert. Cha cha cha. Intruder alert."

            "Uh-oh. It looks like I’ve triggered the freezer’s alarm system. I need to do something quick."

            m2 "Cha cha cha. Intruder alert. Cha cha cha. Intruder alert."
            s "I swear it wasn’t for sex."
            m2 "This melon is reserved for THE PROTOTYPE. Please return the melon and await THE PROTOTYPE."
            s "What is THE PROTOTYPE? Why can I not use the melon for my own melon-related reasons? This is unfair."
            m2 "Cha cha cha. Intruder alert. Cha cha cha. Intruder alert."

            play sound "doorslam.mp3"
            scene escapetheroom1 with hpunch

            m2 "{i}Cha cha cha. Intruder alert. Cha cha cha. Intruder alert.{/i}"

            "I slam the freezer door and keep the melon for myself. Even if it’s against the rules."

            play sound "winner.mp3"
            $ escapemelon = True

            "{i}You have obtained a “Forbidden Melon”{/i}"

            jump escaperoommainmenu

        "Do something else":
            s "I grow tired of these mindless games."

            scene escapetheroom1 with fade

            s "I need to use my time wisely."

            jump escaperoommainmenu

label escaperoomfridge:
    if escapefridgestuff == False:
        scene escapetheroom21 with fade

        "An ominous presence crowds the air around the refrigerator."
        "I must endure it if I am to reach my goal."

        play sound "hummmm.mp3"
        $ renpy.pause(20, hard=True)
        play sound "static.mp3"
        scene escapetheroom22 with flash
        stop sound

        "I manage to endure the ominous presence and can now freely explore the confines of my fridge."
        "It’s packed to the brim with some of my favorite ingredients — like milk, bananas, milk, shampoo, and milk."
        "I should add all of them to my inventory so I don’t have to deal with the ominous presence the next time I open the door."

        scene escapetheroom23
        play sound "winner.mp3"
        $ escapefridgestuff = True

        "{i}You have obtained “Fridge Contents”{/i}"

        "Hmm..."
        "It appears there is still one item left in the fridge. But {i}this{/i} item exudes a strange presence as well. And I feel as if adding it to my inventory could result in unfortunate consequences."

        s "..."

        "Do I want to add it to my inventory anyway?"

        menu:
            "Take the shampoo":
                s "It’s just shampoo. What’s there to be afraid of?"

                play sound "winner.mp3"
                scene escapetheroom24
                $ escapeshampoo = True

                "{i}You have obtained “Shampoo”{/i}"

                s "See? That wasn’t so bad."

                scene escapetheroom1 with fade

                "I close the fridge and get on with my day."

                jump escaperoommainmenu

            "Leave it alone":
                "I’ll just leave the shampoo alone. It’s probably for the best."

                scene escapetheroom1 with fade

                "I close the fridge and get on with my day."

                jump escaperoommainmenu

    if escapefridgestuff == True:
        scene escapetheroom23 with fade

        s "There’s that shampoo again..."

        "What do I want to do?"

        menu:
            "Take the shampoo":
                s "It’s just shampoo. What’s there to be afraid of?"

                play sound "winner.mp3"
                scene escapetheroom24
                $ escapeshampoo = True

                "{i}You have obtained “Shampoo”{/i}"

                s "See? That wasn’t so bad."

                scene escapetheroom1 with fade

                "I close the fridge and get on with my day."

                jump escaperoommainmenu

            "Leave it alone":
                "I’ll just leave the shampoo alone. It’s probably for the best."

                scene escapetheroom1 with fade

                "I close the fridge and get on with my day."

                jump escaperoommainmenu

label escaperoomtopshelves:
    scene escapetheroom25 with fade

    "I take a moment to observe the many important notes that either I or someone else left for myself/me."
    "But I can’t help but feel like there may have been a better way to do this..."

    s "..."

    "Oh well. It is what it is. These notes will be here if I ever need them."
    "But for now, I should get back to happily living my life."

    scene escapetheroom1 with fade

    jump escaperoommainmenu

label escaperoommicrowave:
    scene escapetheroom26
    with fade

    "I’ve always liked microwaves."
    "There’s something calming about watching the numbers tick down along with the radioactive hum as the contents inside rapidly change to fit your liking."
    "It’s not like a clock. Though, some microwaves come with clocks built into them."
    "This is not one of them. This is a good microwave. All it does is cook what I tell it to and burn what I want it to burn."
    "I can fit all sorts of things inside of my microwave. I use it to store what I can not hold in my hands."
    "Sometimes, I’ll turn it on for hours with nothing inside and let its melody sing me to sleep."
    "The electric company doesn’t like that too much. But I can live without power if I absolutely have to. I’ve done it before."
    "I just like the noise."
    "But I don’t like that I can see myself in its reflection — for it makes me feel like {i}I’m{/i} inside. And there are few things that scare me more than that at this point in life."
    "It wasn’t always like that, though."
    "But it is now."

label escapemicrowavemenu:
    $ escapemicrowavecode = renpy.input("Enter the code to open your microwave.")
    $ escapemicrowavecode = escapemicrowavecode.strip()

    if escapemicrowavecode != "1853818235819":
        "The door doesn’t open."

        menu:
            "Try again":
                jump escapemicrowavemenu
            "Give up":
                s "On second thought, I don’t need to open the microwave right now."

                scene escapetheroom1
                with fade

                "What should I do instead?"

                jump escaperoommainmenu

    else:
        play sound "static.mp3"
        scene escapetheroom27 with flash
        stop sound

        "The door opens and I peer into the microwave to uncover my secret stash of important things."
        "These maggots are my children. I provide them sperm and greasy food so that they may one day grow into strong, faithful human flies."
        "They do not call me “father,” nor do they acknowledge my role in their world. They just gorge themselves on the nutrients I provide and grow."
        "One day, they will be human enough to learn to speak. And I will teach them all of my favorite words."
        "But until then, all I can do is nurture them and create an environment where they are able to thrive."
        "It is fun to be God."

        menu:
            "Take your phone":
                scene escapetheroom28
                play sound "winner.mp3"
                $ escaperoomphone = True

                "{i}You have obtained a “Personal Cell Phone” and may now use it to make calls.{/i}"

                s "I will see you later, my children."

                scene escapetheroom1 with fade

                s "I have many important things to do."

                jump escaperoommainmenu

label escaperoomcoffee:
    scene escapetheroom29
    with fade

    r "Coffee hey! Coffee ho! Coffee is the place to go!"
    mo "Coffee this! Coffee that! Coffee with a dog or cat!"
    s "Is this some kind of rap song?"
    r "It’s not a rap song, homie! It’s the opening to a long awaited trivia game!"
    mo "Answer the questions correctly and you’ll get to be caffeinated {i}and{/i} encapsulated!"
    s "Encapsulated by what?"
    r "Guilt!"
    mo "Endless, torturous guilt!"
    r "Where have you been?!"
    mo "What happened to you?!"
    r "What happened to us?!"
    s "I don’t want to do this right now."
    mo "Then answer our questions so you can move on!"
    r "Your grade at the end will determine whether or not you get to proceed!"
    mo "Your grade at the end could grant you a key!"
    r "Question one! What is the official mascot of home brewed coffee?"

    menu:
        "AeroPress":
            $ rinmollycoffeepoint += 0
        "Espresso machine":
            $ rinmollycoffeepoint += 0
        "French press":
            $ rinmollycoffeepoint += 1
        "Percolator":
            $ rinmollycoffeepoint += 0

    mo "Question two! Which coffee machine is the arch nemesis of the Hario v60?!"

    menu:
        "The Bee House":
            $ rinmollycoffeepoint += 0
        "Clever Dripper":
            $ rinmollycoffeepoint += 0
        "AeroPress":
            $ rinmollycoffeepoint += 0
        "Kalita Wave":
            $ rinmollycoffeepoint += 1

    r "Question three! What’s another name for the Vietnamese dripper?"

    menu:
        "Phin":
            $ rinmollycoffeepoint += 1
        "Phan":
            $ rinmollycoffeepoint += 0
        "Phon":
            $ rinmollycoffeepoint += 0
        "Phun":
            $ rinmollycoffeepoint += 0

    mo "Almost there! Question four — which of these looks like more of a science project than a coffee brewer?"

    menu:
        "Kalita Wave":
            $ rinmollycoffeepoint += 0
        "Hario v60":
            $ rinmollycoffeepoint += 0
        "Clever Dripper":
            $ rinmollycoffeepoint += 0
        "AeroPress":
            $ rinmollycoffeepoint += 1

    r "And one last question! Which of these coffee brewers is the best for the homies?"

    menu:
        "Moka pot":
            $ rinmollycoffeepoint += 0
        "Chemex brewer":
            $ rinmollycoffeepoint += 1
        "Melitta Ready Set Joe":
            $ rinmollycoffeepoint += 0
        "Percolator":
            $ rinmollycoffeepoint += 0

    mo "So! How do you think you did?"
    s "I’ve never been more prepared for anything in my life."

    if rinmollycoffeepoint == 5:
        r "I’ll drink to that! {i}Coffee{/i} of course — because you passed with flying colors!"
        mo "Congratulations, Sir! You’re the coffee boy now!"
        s "Awesome. This means I get some sort of prize, right?"
        r "You sure do! Show him his prize, Molly!"
        mo "For receiving 100%% on the coffee quiz, you’ve won..."

        scene escapetheroom30
        play sound "winner.mp3"
        $ escaperoach = True

        mo "This spectacular roach!"

        "{i}You have obtained a “Spectacular Roach”{/i}"

        scene escapetheroom31

        s "Hooray! A new friend!"
        r "And that’s not all! You’ll also be receiving..."

        scene escapetheroom32
        play sound "winner.mp3"
        $ escapekey3 = True

        r "This spectacular key!"

        "{i}You have obtained a “Spectacular Key”{/i}"

        scene escapetheroom33

        s "Nice. What does it open?"
        r "I actually have no idea."
        mo "Yeah, we’re just here to hand stuff out and give your brain something silly to focus on as a distraction from your unending grief!"
        s "Oh, well that’s really nice of you."
        r "Yeah, but seeing as answering all of our questions correctly is the trigger that causes us to return to dormancy, we’re going to have to stop responding now."
        s "What? Already?"
        mo "Come visit us sometime, Sir! We miss you!"
        s "..."
        r "..."
        mo "..."

        scene escapetheroom1 with fade

        s "Well, that’s that I guess."

        jump escaperoommainmenu

    else:
        r "Well, that’s depressing! Because you failed!"

        $ rinmollycoffeepoint = 0

        s "What? Really?"
        mo "Yes, Sir! Which means that, unfortunately, you’ll be leaving here today without a prize."
        s "Can I at least have some coffee?"
        r "Nope! We’re fresh out."
        s "But I can see-"
        mo "{b}SHE SAID WE’RE OUT, YOU FUCKING PUSSY.{/b}"

        scene escapetheroom1 with fade

        "I decide to walk away from the coffee maker as the service there was terrible."
        "What should I do instead?"

        jump escaperoommainmenu

label escaperoombotleft:
    if day != 2:
        scene escapetheroom34 with fade
        "I crouch down and come face to face with my bottom left cabinet. Even if my bottom left cabinet doesn’t technically have a face."
        "But when I go to open it, I realize it won’t budge."
        "This is very unfortunate, as I feel an urgent need to get inside the cabinet so I can do something."

        s "Hngh!"

        "I attempt to pull it open, but fail miserably and pull a muscle in my arm. This is going to hurt for days, I can already tell."

        scene escapetheroom1 with fade

        "Oh well. I guess I’ll have to figure something else out if I want to open that cabinet."

        jump escaperoommainmenu

    if day == 2:
        scene escapetheroom35 with fade

        s "Wow!"

        "It looks like my bottom left cabinet is glowing because today is Magical Day."
        "This means I’ll finally be able to open the lock and see what’s inside."

        scene black
        with dissolve

        s "I hope there is some sort of snack!"

        play sound "lock.mp3"

        "I place my hand on the lock, releasing the magical seal before pulling the doors open."

        scene escapetheroom36 with dissolve2

        "My parrot greets me when I crouch down and put my head inside of his enclosure. I can’t remember the last time I was in here."
        "I take a look to the left at his coconut crab and see that he has been raising him well."
        "I’m sure you think it’s strange for one of my pets to have a pet, but that’s just how things work in this house."
        "We all take care of each other and so we can all live happily ever after."
        "I replace my parrot’s bottle of water with a new one- disinfected so his bird liver will not become a home to parasites. And I scratch beneath his chin to show him I love him."

        parrot "Sacrifice! Sacrifice!"
        s "Sacrifice?"
        parrot "A gift for God! A gift for God!"
        s "I know what a sacrifice is, Parrot. I’m just a little confused about why you’re, you know, {i}parroting{/i} that word."
        parrot "Sacrifice! A gift for God! Sacrifice! A gift for God!"
        s "Huh..."

        "I guess my parrot wants to be sacrificed."

        scene escapetheroom37
        play sound "winner.mp3"
        $ escapeparrot = True

        "{i}You have obtained “Parrot”{/i}"

        s "I wonder what will become of the coconut crab?"
        parrot "{i}Sacrifice! Sacrifice!{/i}"

        "My parrot shrinks itself and flies in circles around my invisible backpack. He’s very happy to be outside his enclosure for once."

        s "Are you sure about this?"
        s "If you’re unhappy, I understand. But I thought we could be a family."
        parrot "Miss her! Miss her! Sacrifice! A gift for God!"

        scene escapetheroom1 with fade

        s "If that is what must be done, it will be done."

        jump escaperoommainmenu

label escaperoombotright:
    scene escapetheroom51 with fade

    "I crouch before my brand new smart cabinet, complete with four separate smart locks that need to be touched in the correct order for the door to open."
    "There are warnings drawn all over the cabinet in permanent marker, but I’ve found that their permanence won’t persist through a new coat of paint."
    "Or maybe it does and I just can’t see the words I once wrote anymore. I don’t know."
    "The point is, I visit this cabinet a lot. It’s where I keep my spices and it’s where I keep something else."
    "I just hope I can remember how to open it."
    "There’s something very important inside. And leaving it in there unattended would be irresponsible of me to do."
    "I squint my eyes and steady my hands."
    "The order in which I will press the tablets is-"

label escaperoombotrighttext:
    $ escapebotrightcode = renpy.input("Smart lock deactivation sequence initiated. Please tap lock quadrants in the correct order.")
    $ escapebotrightcode = escapebotrightcode.strip()

    if escapebotrightcode != "231312423124":
        play sound "computerboo.mp3"

        "The combination I entered isn’t valid."
        "Should I keep going? Or should I give up instead?"

        menu:
            "Keep going":
                "One more try won’t hurt."

                jump escaperoombotrighttext

            "Give up":
                scene escapetheroom1 with fade

                s "On second thought, I don’t have to open that cabinet right now."

                jump escaperoommainmenu

    else:
        play sound "computeryay.mp3"
        scene escapetheroom52

        "The angry faces on the tablets turn to happy ones as I manage to enter the correct code."
        "The reason they are called smart cabinets is because it takes a smart person to open them."
        "I am that person."
        "I am a smart boy."

        scene black
        with dissolve

        "The doors creak as I slowly pull them open."
        "I wonder when the last time I looked inside was?"

        scene escapetheroom53
        with dissolve2

        "This is where I keep my dog, Squirrel."
        "I keep her in the smart cabinet because she is a smart girl."
        "But lately, she has been acting a little strange."
        "There are demons inside of her that allow her to shapeshift, but she is camera-shy and won’t show you while you’re here watching."
        "She likes turkey legs and Coca-cola. Her favorite color is yellow and she has been my loyal companion since she crawled in through the vent one day."
        "She was so small back then. And she’s such a big girl now."
        "But the time has come for me to exorcise her demons so she can be at peace."

        scene escapetheroom54
        play sound "winner.mp3"
        $ escapedog = True
        "{i}You have obtained “Dog”{/i}"

        "After stuffing Squirrel into my invisible bag, I notice something peculiar about her cage."
        "There used to be someone else inside — a pet of her own, if you will. Which you won’t. Because if you would, then I wouldn’t. So I will since you won’t."
        "Did you like that fun string of thought-provoking words?"
        "I’ve been practicing soliloquies so my smartness shines through. Will or won’t you come with me? Will or won’t you try too?"
        "I told you I’m a smart boy. The smartest there is."
        "Everyone here will confirm that for you."
        "All you have to do is ask them."

        scene escapetheroom1 with fade

        s "Now what?"

        jump escaperoommainmenu

label escaperoomfloor:
    if day != 3:
        scene escapetheroom44 with fade

        "I gaze down at the floor mat."
        "It’s entirely unremarkable apart from a pair of panties that definitely do not belong to me."
        "I’m not sure how they got there, but it’s possible they were smuggled in by evil spies who want to make me look like a bad guy in front of my friends."
        "If I touch them, some of my DNA will probably rub off and could incriminate me if they belong to someone who is dead now. So it’s probably best if I leave them alone."

        scene escapetheroom1 with fade

        "In fact, it’s probably best if I do something else altogether."

        jump escaperoommainmenu

    if day == 3:
        scene escapetheroom45 with fade

        "I gaze down at the floor mat to discover that it’s covered in fish — likely because it is Fish Day."
        "One of these could make a good hot pot ingredient, but I should choose carefully since I’m only allowed to take one per week."
        "I’m not really sure why. Those are just the rules. And as a law-abiding citizen, I must follow them."
        "Which fish do I want to take?"

        menu:
            "Beaked Coralfish":
                $ escapecoralfish = True
                $ havefish = True
                scene escapetheroom1
                play sound "winner.mp3"
                "{i}You have obtained a “Beaked Coralfish”{/i}"
                s "Hell yeah."
            "Harlequin Filefish":
                $ escapefilefish = True
                $ havefish = True
                scene escapetheroom1
                play sound "winner.mp3"
                "{i}You have obtained a “Harlequin Filefish”{/i}"
                s "Hell yeah."
            "Blue-Banded Angelfish":
                $ escapeangelfish = True
                $ havefish = True
                scene escapetheroom1
                play sound "winner.mp3"
                "{i}You have obtained a “Blue-Banded Angelfish”{/i}"
                s "Hell yeah."
            "Clownfish":
                $ escapeclownfish = True
                $ havefish = True
                scene escapetheroom1
                play sound "winner.mp3"
                "{i}You have obtained a “Clownfish”{/i}"
                s "Hell yeah."
            "Lionfish":
                $ escapelionfish = True
                $ havefish = True
                scene escapetheroom1
                play sound "winner.mp3"
                "{i}You have obtained a “Lionfish”{/i}"
                s "Hell yeah."
            "Pennant Bannerfish":
                $ escapebannerfish = True
                $ havefish = True
                scene escapetheroom1
                play sound "winner.mp3"
                "{i}You have obtained a “Pennant Bannerfish”{/i}"
                s "Hell yeah."
            "Parrotfish":
                $ escapeparrotfish = True
                $ havefish = True
                scene escapetheroom1
                play sound "winner.mp3"
                "{i}You have obtained a “Parrotfish”{/i}"
                s "Hell yeah."

        scene escapetheroom1 with fade

        s "I can’t wait to try adding this to my hot pot."

        jump escaperoommainmenu

label escaperoomschedule:
    if escapekey4 == False:
        scene escapetheroom62 with fade
        "I live a simple life here, but I wouldn’t be able to do that if it wasn’t for my trusty schedule."
        "With over six days in every week, I can do as many things as I want, whenever I want to do them."
        "Sometimes, someone leaves me flowers. But the flowers block the view of my schedule, so I often push them away."
        "They always come back immediately, though. It’s unfair."
        "Just watch."

        play sound "glass.mp3"
        scene escapetheroom63 with hpunch

        s "Step one — complete."
        s "Step two requires waiting for them to respawn and-"

        scene escapetheroom64
        play sound "winner.mp3"
        $ escapekey4 = True
        "{i}You have obtained a “Flower Key”{/i}"

        scene escapetheroom63

        s "Wait, what? That’s never happened before."

        play sound "pabell.mp3"

        vpa "The “Flower Key” can be used to open something in this room! Go exploring and find out what!"
        vpa "Just don’t use too many of them or you’ll wind up somewhere you don’t want to be."
        vpa "You’re supposed to stay here. This is where you’re safe."
        s "I know that. I’m not going to leave. I have no reason to leave. I’m happy here."

        "The voice on the PA stops responding."

        play sound "static.mp3"
        scene escapetheroom62 with flash
        stop sound

        "Then, the vase respawns."
        "This always happens."
        "It’s why I hate flowers."

        play sound "glass.mp3"
        scene escapetheroom63 with hpunch

        "I push the vase aside again to get another look at the schedule."
        $ renpy.pause(5, hard=True)
        play sound "static.mp3"
        scene escapetheroom62 with flash
        stop sound

        "Then it comes right back."

        scene escapetheroom1 with fade

        "I should do something else instead."

        jump escaperoommainmenu

    else:
        scene escapetheroom62
        with fade

        s "Time to check the calendar."

        play sound "glass.mp3"
        scene escapetheroom63 with hpunch
        $ renpy.pause(5, hard=True)
        play sound "static.mp3"
        scene escapetheroom62 with flash
        stop sound

        s "Time is up."

        scene escapetheroom1 with fade

        "I should do something else."

        jump escaperoommainmenu

label escaperoomtv:
    if escapetvchild == True:
        scene escapetheroom43 with fade
        jump tvloophahanerd
    if escapetvchild == False:
        scene escapetheroom42 with fade

        "I stare up at my TV and begin to reminisce about all of the spectacular local programming I’ve watched on it over the last few years."
        "It seems that, every day, something new is coming out."
        "Whether it be Untitled Children’s Show or Nighttime Banana Battle, there’s always something entertaining to keep me occupied."
        "There’s always something to keep my mind from wandering."
        "I lean back in my chair and wipe the drool from my chin, prepared to zone out for one more night on the way to indefinite indecision."
        "Carry me away, old friend. To better days in better places."

        menu:
            "Change the channel":
                scene escapetheroom43
                play music "happyhappysmile.mp3"
                $ escapetvchild = True

                s "Oh, look. Untitled Children’s Show is on."

                jump tvloophahanerd
            "Leave the TV alone":
                scene escapetheroom1 with fade

                "I decide against watching TV. I’ll do something else instead."

                jump escaperoommainmenu

label tvloophahanerd:
    menu:
        "Change the channel":
            s "I don’t want to change the channel. I like this show."

            jump tvloophahanerd

        "Leave the TV alone":
            scene escapetheroom1 with fade

            "I like this show, so I’ll keep this on for a while."

            jump escaperoommainmenu

label escaperoomhotpot:
    scene escapetheroom46 with fade

    "I gaze into the hot pot. It beckons to be fed."
    "What ingredients do I want to add to it?"

    menu hotpotmenu:
        "FoodCo. roux" if escaperoux == True and rouxdone == False:
            "Every hot pot needs a good base, and there’s no better base than FoodCo’s famous hot pot roux."
            "I drop the premade roux into the pot and it immediately begins to crackle and fizzle, the way all good roux does."
            "I can’t wait to eat this."
            $ rouxdone = True
            jump hotpotmenu
        "Watermelon" if escapemelon == True and melondone == False:
            "I know I wasn’t supposed to touch this watermelon, but it would be a crime to keep it away from my hot pot."
            "A little bit wouldn’t hurt, right?"
            "I bite off a chunk of the watermelon, but don’t manage to get much since watermelons are surprisingly hard to bite through."
            "I spit what I {i}am{/i} able to get into the pot and it quickly dissolves."
            "This will be my first time putting watermelon in my hot pot, so I sure hope it doesn’t ruin everything."
            $ melondone = True
            jump hotpotmenu
        "Parrot the Parrot" if escapeparrot == True and parrotdone == False:
            parrot "{i}A gift for God! Sacrifice! Miss her! Miss her!{/i}"
            s "I’m sorry it had to end like this."
            s "I hope we can be friends in our next life."

            "I drop my parrot into the hot pot and it bursts into flames."
            "It’s tragic watching something you grew yourself fade away right before your very eyes, but it’s also kind of beautiful in a way."
            "I know he’ll be going somewhere better now. And I know this is what he wanted."
            "All I can do is give him the respect he deserves and consume him entirely."
            $ parrotdone = True
            jump hotpotmenu
        "Squirrel the Dog" if escapedog == True and dogdone == False:
            "My dog stares up at me as I take her into my arms — fearless."
            "She trusts me with her life and is a loyal companion."
            "But I know what I must do in order to heal her and purge the demons from her body."
            "I will take them into myself. And in doing so, I will make her whole."
            "She looks at me again. Then down at the hot pot."
            "I close my eyes and drop her in."
            "She whimpers. Cries. But it doesn’t last long."
            "The pain is over now."
            $ dogdone = True
            jump hotpotmenu
        "Stuff from the fridge" if escapefridgestuff == True and fridgedone == False:
            "I empty out the contents of my fridge into the hot pot because recipes are for frauds and real chefs cook with heart."
            "The problem here is that I do not have any heart left and all I can do is hope that something in this batch of ingredients will work as a viable substitute."
            "The ingredients dissolve- apart for the banana. This fruit is surprisingly resilient and I wonder what it is about the peel that makes it impervious to flame damage."
            "I remove the peel, sensing that it will not be dissolving any time soon- but it seems as if the rest of the ingredients successfully have."
            $ fridgedone = True
            jump hotpotmenu
        "Centipede" if escapecentipede == True and centipededone == False:
            "The centipede I stole from the vent has been biting through my invisible backpack ever since I picked it up, and the time has come to stop the damage."
            "I pluck it out of my backpack, squeezing its head between my thumb and forefinger, before dropping it into the pot and watching it flail around."
            "I’m not sure if insects feel pain. I think I recall someone close to me saying they don’t."
            "And even though I was not particularly fond of this temporary friend, I hope he did not suffer as he dissolved into nothing."
            $ centipededone = True
            jump hotpotmenu
        "Lionfish" if escapelionfish == True and lionfishdone == False:
            "I think I heard somewhere that lionfish are poisonous- but I’m pretty sure that’s only in regard to other fish."
            "If that is true, I did marine life a favor by making this selection during Fish Day- and everyone should be proud of me for adding it to my hot pot."
            "The lionfish slips out of my hands and splashes into the pot, making a new home for itself inside of boiling water."
            "It doesn’t last long and dissolves before I can even say goodbye."
            $ lionfishdone = True
            jump hotpotmenu
        "Beaked Coralfish" if escapecoralfish == True:
            "I drop the coralfish into the hot pot. But when it doesn’t dissolve, I realize I’ve made a mistake."
            "I manage to pull it out before it contaminates the rest of the pot, but I’ll have to wait until the next Fish Day for another one."
            $ escapecoralfish = False
            $ havefish = False

            scene black
            with dissolve2

            "After ruining the hot pot, I'm too depressed to do anything else and wind up going to sleep."

            jump escaperoomdaychange
        "Clownfish" if escapeclownfish == True:
            "I drop the clownfish into the hot pot. But when it doesn’t dissolve, I realize I’ve made a mistake."
            "I manage to pull it out before it contaminates the rest of the pot, but I’ll have to wait until the next Fish Day for another one."
            $ escapeclownfish = False
            $ havefish = False

            scene black
            with dissolve2

            "After ruining the hot pot, I'm too depressed to do anything else and wind up going to sleep."

            jump escaperoomdaychange
        "Parrotfish" if escapeparrotfish == True:
            "I drop the parrotfish into the hot pot. But when it doesn’t dissolve, I realize I’ve made a mistake."
            "I manage to pull it out before it contaminates the rest of the pot, but I’ll have to wait until the next Fish Day for another one."
            $ escapeparrotfish = False
            $ havefish = False

            scene black
            with dissolve2

            "After ruining the hot pot, I'm too depressed to do anything else and wind up going to sleep."

            jump escaperoomdaychange
        "Blue-Banded Angelfish" if escapeangelfish == True:
            "I drop the angelfish into the hot pot. But when it doesn’t dissolve, I realize I’ve made a mistake."
            "I manage to pull it out before it contaminates the rest of the pot, but I’ll have to wait until the next Fish Day for another one."
            $ escapeangelfish = False
            $ havefish = False

            scene black
            with dissolve2

            "After ruining the hot pot, I'm too depressed to do anything else and wind up going to sleep."

            jump escaperoomdaychange
        "Harlequin Filefish" if escapefilefish == True:
            "I drop the filefish into the hot pot. But when it doesn’t dissolve, I realize I’ve made a mistake."
            "I manage to pull it out before it contaminates the rest of the pot, but I’ll have to wait until the next Fish Day for another one."
            $ escapefilefish = False
            $ havefish = False

            scene black
            with dissolve2

            "After ruining the hot pot, I'm too depressed to do anything else and wind up going to sleep."

            jump escaperoomdaychange
        "Pennant Bannerfish" if escapebannerfish == True:
            "I drop the bannerfish into the hot pot. But when it doesn’t dissolve, I realize I’ve made a mistake."
            "I manage to pull it out before it contaminates the rest of the pot, but I’ll have to wait until the next Fish Day for another one."
            $ escapebannerfish = False
            $ havefish = False

            scene black
            with dissolve2

            "After ruining the hot pot, I'm too depressed to do anything else and wind up going to sleep."

            jump escaperoomdaychange
        "Finish the hot pot" if rouxdone and parrotdone and dogdone and fridgedone and centipededone and lionfishdone and melondone:
            s "Hmm..."
            s "Everything’s looking good so far...but I think I’m still missing something."
            s "..."
            s "Ah-hah!"

            "I’ve had a hangnail for several days. It’s been bothering me to no end."
            "Bracing myself for the pain it’s sure to bring, I place it in my mouth and tear away at it- removing some of the flesh from my finger in the process."
            "This is the final ingredient I need for the hot pot."
            "Sucking the blood from my finger, I drop the hangnail in and-"

            scene escapetheroom47
            play sound "winner.mp3"
            $ escapekey6 = True

            "{i}You have obtained a “Delicious Key”{/i}"

            scene escapetheroom46

            s "A delicious key? But where did all of my ingredients go? This was supposed to be a delicious hot pot."

            "I stare down at the hot pot once more. It still beckons to be fed- but I have nothing left to give it."

            scene escapetheroom3 with fade

            "I will just have to starve to death."

            jump escaperoomkitchenmenu

        "Stop adding ingredients":
            s "I think that’s enough for now. I’ll come back when I have more ingredients to add."

            scene escapetheroom3 with fade

            s "Now what?"

            jump escaperoomkitchenmenu

label escaperoomlover:
    scene escapetheroom66 with fade

    s "Hello, Barbara."
    barb "Hi, Akira."

    "This is Barbara with midnight eyes. I talk to her when I get lonely."
    "She’s under strict orders (from me) to never open herself up because I can’t handle what she holds."
    "This isn’t just because she’s the ideal woman, but because I used to hide things inside of her that I’m not allowed to have anymore."
    "Keeping me away is what’s best for everyone."
    "I am a protector now. A keeper of keys and creatures and an icon of righteousness."
    "Additionally, I have learned to treat the female species better — and have authored several books on how to succeed when it comes to “getting the girl.”"
    "I will show you some of my strategies today. Because, like yesterday and days before, I’m lonely."
    "I am always lonely."
    "But that’s okay so long as I have Barbara."

    s "Barbara, are you free right now?"
    barb "Yes, but you know I can’t let you inside no matter how hard you try."
    s "I understand that, but I have to prove to everyone that I’m not a liar."
    barb "But you are a liar, Akira. All you ever do is lie. Even after all this time. You’ve never learned at all."
    barb "What’s inside of me must {i}stay{/i} inside of me or you’re going to hurt someone again. And that someone could be you. I don’t want that."

    menu:
        "Be pushy":
            s "Listen, Barbara. You’re a cabinet. You don’t have the authority to tell me what I can and can’t do."
            barb "Oh, no. Hell no. You didn’t just call me a cabinet."
            s "But I did. And if you know what’s best for you, you’ll save both of us the hassle and-"
            barb "Give it a rest, Akira. We’re done here."
            jump barbfailed
        "Be understanding":
            jump barbstep2
        "Be seductive":
            s "Does {i}this{/i} change your mind?"

            "I begin to flex my muscles as Barbara is typically interested in that sort of thing."

            barb "..."
            s "How about {i}this?{/i}"

            "I flex my penis as well to show her how strong and experienced it is and how I can flex anything if I try hard enough."

            barb "I can’t let you in, Akira."
            s "But I {i}want{/i} to be in, Barbara. Look at my strong penis with your midnight eyes."
            barb "I’m sorry, I just...can’t let it happen."
            jump barbfailed

label barbstep2:
    s "I understand your concern, but things are different now. I can handle all of those things you used to worry about."
    barb "Oh, please. I bet you can’t even {i}name{/i} any of those “things.”"
    s "Does it really make a difference if I can or can’t? The fact of the matter is, I’m stronger than you think I am. I can handle anything you throw my way."
    barb "Oh yeah? So if I were to ask you to take me on a {i}real{/i} date, where would we go?"

    menu:
        "Hardware store":
            s "Obviously, we’d go to the hardware store and pick up a few extra...accessories for you."
            barb "..."
            s "I was trying to allude to that meaning lingerie, but I’m not really sure if it worked or not."
            barb "I can’t believe you. You really thought that was going to work? That I’d just {i}ignore{/i} how you always wind up reducing me to my {i}appearance{/i} rather than what’s on the inside?"
            s "In my defense, I am specifically after what’s “on the inside” right now, so I don’t think that argument holds up very well."
            barb "And I don’t think this {i}date{/i} holds up very well, so you’re going to have to try again when you feel like less of an asshole."
            jump barbfailed
        "Italian restaurant":
            jump barbpart3
        "Couple’s spa retreat":
            s "I’d have to take you on a couple’s spa retreat. I think we could both use a little time to relax and unwind."
            barb "That’s a nice idea, but I can’t really imagine being able to relax and unwind around so many other people who look nothing like me."
            barb "Midnight eyes are a gift from God and no one ever understands that. And if that’s not enough, I’m tired of seeing through everyone. I’m tired of my X-ray vision."
            s "I love your X-ray vision, Barbara. It’s one of my favorite things about you."
            barb "I appreciate that, Akira. But that’s just not the sort of date I’m interested in."
            jump barbfailed

label barbpart3:
    s "You like Italian food, don’t you? Maybe we could hit up a cozy Italian restaurant with neutral lighting and some fine mustachioed gentlemen?"
    barb "Hmm...I {i}do{/i} love neutral lighting. And mustaches."
    s "See? I’m not as inept as you think. I can put together a solid date if I really want to."
    barb "Akira, why do you even want to remove my innards in the first place? Doing that will kill me. You {i}know{/i} it will. It’s part of the pact we made when you gifted me sentience."
    s "If you really want the truth...I don’t know."
    s "I have no idea what I’m doing."
    barb "Akira..."
    s "But it’s {i}because{/i} I have no idea what I’m doing that I have to do {i}something.{/i} You know?"
    s "Maybe I can face it now? Maybe I really {i}can{/i} embrace the past instead of curling up into a ball every night and waking up in a puddle of my own spit."
    barb "..."
    s "Or maybe I can’t."
    s "I don’t know."
    s "But I’m never going to find out if you don’t {i}let me in.{/i}"
    barb "What’s my favorite movie?"
    s "Your favorite movie?"
    barb "Do you remember?"
    s "Of course I do..."
    s "It’s-"

    menu:
        "Fever Pitch w/ Jimmy Fallon":
            s "The 2005 cult classic, Fever Pitch, starring Jimmy Fallon and Drew Barrymore."
            s "This unsung romantic comedy masterpiece not only puts the Boston Red Sox at the forefront of the movie’s plot, but-"
            barb "I don’t know how many times I have to tell you this, Akira, but I have never seen Fever Pitch. I don’t even know who Jimmy Fallon is."
            s "Then we need to change that right away. The only reason I’m calling it your favorite movie now is-"
            barb "I’m sorry. But until I know you really care about me, I can’t let you in."
            jump barbfailed
        "The Notebook":
            jump barbpart4
        "Yojimbo":
            s "That one about the ronin samurai directed by Akira Kurosawa."
            barb "You’re going to have to be more specific than that."
            s "I think it’s...Yojimbo. Right?"
            barb "You think Yojimbo is my favorite movie?"
            s "I’m pretty sure I recall you mentioning something along those lines, yeah."
            barb "I mean...I {i}like{/i} it. But I definitely wouldn’t call it my favorite."
            s "Well, can we just assume it’s your favorite for a few minutes so I can proceed with the conversation?"
            barb "No, Akira...I think we’re done for now. Until I know you really care about me, I can’t let you in."
            jump barbfailed

label barbpart4:
    s "The Notebook with Ryan Gosling and Rachel McAdams."
    barb "So you {i}do{/i} remember after all..."
    s "You cry like a baby every time it comes on. I could never forget the way your midnight eyes glisten."
    barb "How could anyone {i}not{/i} cry with the way that movie ends? It was so beautiful and...bittersweet and-"
    s "And you know you’ve gotta let me in, Barb."
    barb "..."
    s "{i}You know you’ve gotta let me in.{/i}"
    barb "What you’re asking for is my death, Akira."
    s "No, Barbara..."
    s "What I’m asking for is {i}my freedom.{/i}"
    barb "And I should have to die for that?..."
    s "No one should have to die for anything. But sometimes people do."
    s "Sometimes people die, Barbara. And there’s nothing we can do about that."
    s "But {i}you...{/i}"
    s "The fact that you’re able to exist at all is a miracle. And it’s a miracle that I made happen."
    s "So now it’s your turn."
    s "It’s your turn to be a miracle for me. Because nobody else can."
    s "They’ve all left already."
    barb "..."
    s "..."
    barb "I have one final question."
    s "What is it?"
    barb "Do you love me?"

    menu:
        "Yes":
            s "Of course I love you. How could I not?"
            barb "You’re lying..."
            s "I’m not lying, Barbara. I’m-"
            barb "No, you are..."
            barb "All of the love you have...all of the love you {i}had...{/i}"
            barb "That was all for someone else. There’s none to spare for me."
            s "But-"
            barb "Akira...I’m flattered. Really. But until you can be honest with yourself..."
            barb "I just can’t do it."
            jump barbfailed
        "No":
            jump barbpart5
        "I love to party":
            s "The only thing {i}I{/i} love..."
            s "Is being a party animal."
            barb "Why would you just...go and ruin this whole conversation like that?"
            s "I couldn’t resist that choice. I’m sorry."
            barb "And now you’re talking about {i}choices{/i} again? Have you been playing too many games? You’re not pretending {i}this{/i} is a game too, are you?"
            s "Nooooooooo..."
            barb "Akira, you’ve gotta be kidding me! Come on!"
            s "Are you going to spill out your guts now?"
            barb "No! Absolutely not!"
            jump barbfailed

label barbpart5:
    s "If you want the truth...which I think you do..."
    s "No."
    s "I don’t love you."
    s "I don’t think I {i}can.{/i}"
    barb "..."
    s "I’m sorry if that’s not what you wanted to hear."
    barb "No, Akira..."
    barb "It’s exactly what I wanted to hear."
    barb "I can die in peace now."
    barb "Thank you."
    s "Barbara, wait-"
    barb "My consciousness is fading...what is it?..."
    s "Will..."
    s "Will I ever see you again?..."
    barb "Oh, Akira..."

    scene escapetheroom67 with dissolve2

    barb "{i}Probably not...{/i}"

    "Barbara fades away forever."

    s "..."

    "I’m all alone again."

    scene escapetheroom68 with fade

    "But at least I get to see what’s inside now."
    "The cabinet is full of webs and spiders. Spiders who probably made those webs."
    "There is also ammunition and health potion in case I wind up taking too much damage in Barbara’s absence."

    s "..."

    "There’s something else too."
    "A few things actually."
    "But none of them are important."

    play sound "doorslam.mp3"
    scene escapetheroom3 with hpunch

    "I slam the door and revel in the sensation of items popping into my invisible backpack."

    play sound "winner.mp3"
    $ escapekey5 = True
    "{i}You obtained “Barbara’s Key”{/i}"
    play sound "winner.mp3"
    "{i}You obtained “HP Potion”{/i}"
    play sound "winner.mp3"
    "{i}You obtained “Ammunition”{/i}"

    s "Now what?"

    jump escaperoomkitchenmenu

label barbfailed:
    "Crap. I must have made some sort of mistake."
    "That’s okay, though. I can pretend this never happened and try again whenever I want."
    "I’m bound to succeed eventually, right?"

    scene escapetheroom3 with fade

    s "Now what?"

    jump escaperoomkitchenmenu

label escaperoomamipc:
    scene escapetheroom65 with fade

    "The computer opens its mouth and begs for a password:"

    jump amipcpassenter

label amipcpassenter:
    $ escapeamipccode = renpy.input("Please enter the password...")
    $ escapeamipccode = escapeamipccode.strip()

    if escapeamipccode == "mom":
        jump rainking
    else:
        play sound "computerboo.mp3"

        "Password not accepted."

        menu:
            "Try again":
                jump amipcpassenter
            "Give up":
                s "..."

                scene escapetheroom1 with fade

                s "Let’s do something else."

                jump escaperoommainmenu

label escaperoomdelivery:
    if day != 1:
        scene escapetheroom55 with fade

        s "Aww man...there’s nothing here."
        s "Why can’t mail be delivered every day?"

        play sound "knock.mp3"

        qn "FYN GY CH!"
        s "..."

        play sound "knock.mp3"

        qn "FYN GY CH, SIO ZOWECHA UMMBIFY!"
        s "I’m not supposed to open the door for strangers."

        play sound "knock.mp3"

        qn "UECLU! IJYH NBY ZOWECHA XIIL!"

        "This happens sometimes. It’s easier to ignore when I’m not next to the door."

        scene escapetheroom1 with fade

        "So I’ll just wait over here until it blows over."

        play sound "knock.mp3"
        s "..."
        play sound "knock.mp3"
        s "..."
        play sound "knock.mp3"
        s "..."
        play sound "knock.mp3"
        s "..."
        s "..."
        s "..."

        "Now what?"

        jump escaperoommainmenu

    if day == 1 and newhopeordered == True and escapekey7 == False:
        scene escapetheroom56 with fade

        s "Oh, look. A package."
        s "I wonder what’s inside?"

        "I begin to rifle through the newspapers in the box, hoping I don’t accidentally cut myself on something sharp."
        "It would probably be faster just take all of the paper out, but the hunt for what’s inside excites me. And I know it will pay off soon enough or this will all-"

        scene escapetheroom57
        play sound "winner.mp3"
        $ escapekey7 = True
        "{i}You have obtained a “Red Key”{/i}"

        s "Oh, right. This must be the box Yasu sent over."
        s "I’ll be sure to put this key to good use."

        scene escapetheroom1 with fade

        "I kick the box off to the side and tuck the key into my backpack."
        "I love Mail Day."

        jump escaperoommainmenu

    elif day == 1 and rouxordered == True and escaperoux == False:
        scene escapetheroom56 with fade

        s "Oh, look. A package."
        s "I wonder what’s inside?"

        "I begin to rifle through the newspapers in the box, hoping I don’t accidentally cut myself on something sharp."
        "It would probably be faster just take all of the paper out, but the hunt for what’s inside excites me. And I know it will pay off soon enough or this will all-"

        scene escapetheroom58
        play sound "winner.mp3"
        $ escaperoux = True
        "{i}You have obtained “FoodCo Roux”{/i}"

        scene escapetheroom56
        s "At last! It’s here!"

        scene escapetheroom1 with fade

        "I dump the premade roux into my backpack as my mouth begins to water."
        "I’m going to make the greatest hot pot the world has ever seen."

        jump escaperoommainmenu

    elif day == 1 and mysbox1ordered == True and escapegun == False:
        scene escapetheroom59 with fade

        s "Awesome! This must be the mystery box I ordered."

        scene escapetheroom60
        play sound "winner.mp3"
        $ escapegun = True
        "{i}You have obtained “Salvation”{/i}"

        scene escapetheroom56

        s "Wow. This is way cooler than what I got out of my last mystery box."
        s "I can’t wait to try it out."

        scene escapetheroom1 with fade

        s "Now what should I do?"

        jump escaperoommainmenu

    elif day == 1 and mysbox2ordered == True and escapekey8 == False:
        scene escapetheroom56h with fade

        s "Oh, look. A package."
        s "I wonder what’s inside?"

        "I begin to rifle through the newspapers in the box, hoping I don’t accidentally cut myself on something sharp."
        "It would probably be faster just take all of the paper out, but the hunt for what’s inside excites me. And I know it will pay off soon enough or this will all-"

        scene escapetheroom61
        play sound "winner.mp3"
        $ escapekey8 = True
        "{i}You have obtained “Himawari’s Special Key”{/i}"

        scene escapetheroom56

        s "A key?"
        s "Is that really all that came in this mystery box?"
        s "They should have given me something better after I went through all the trouble of guessing that discount code."

        scene escapetheroom1 with fade

        s "Oh well. It is what it is, I guess."
        s "I’m sure I’ll find some use for it."

        jump escaperoommainmenu

    else:
        scene escapetheroom55 with fade

        s "There’s nothing sadder than no mail on Mail Day..."

        scene escapetheroom4 with fade

        jump escaperoomdoormenu

label escaperoomvent:
    scene escapetheroom48 with fade

    "I gaze down at the vent."

    menu escapeventmenu:
        "Continue gazing":
            $ ventcounter += 1
            "I continue gazing at the vent."

            if ventcounter == 20:
                scene escapetheroom49 with dissolve2

                s "What’s this?"
                s "Has a friend come to join me?"

                scene escapetheroom50 with dissolve

                s "You’re coming with me."

                scene escapetheroom48
                play sound "winner.mp3"
                $ escapecentipede = True
                "{i}You’ve obtained a “Centipede”{/i}"

                s "Hell yeah."

                scene escapetheroom4 with fade

                s "Now what?"

                jump escaperoomdoormenu

            else:
                jump escapeventmenu

        "Stop gazing":
            $ ventcounter = 0

            "This is boring."

            scene escapetheroom4 with fade

            "I want to do something else instead."

            jump escaperoomdoormenu


label escaperoomlockers:
    scene escapetheroom69 with fade

    "I’m not supposed to open these. It’s against the rules."

    menu escapelockermenu:
        "Use “Pegasus Key”" if escapekey1 == True and escapepiece1 == False:
            play sound "lock.mp3"
            "The lock opens and out pops a hair tie."
            $ escapepiece1 = True
            jump escapelockermenu
        "Use “Cereal Key”" if escapekey2 == True and escapepiece2 == False:
            play sound "lock.mp3"
            "The lock opens and out pops a piece of gum."
            $ escapepiece2 = True
            jump escapelockermenu
        "Use “Spectacular Key”" if escapekey3 == True and escapepiece3 == False:
            play sound "lock.mp3"
            "The lock opens and out pops a handkerchief."
            $ escapepiece3 = True
            jump escapelockermenu
        "Use “Flower Key”" if escapekey4 == True and escapepiece4 == False:
            play sound "lock.mp3"
            "The lock opens and out pops a mechanical pencil."
            $ escapepiece4 = True
            jump escapelockermenu
        "Use “Barbara’s Key”" if escapekey5 == True and escapepiece5 == False:
            play sound "lock.mp3"
            "The lock opens and out pops the button of a blazer."
            $ escapepiece5 = True
            jump escapelockermenu
        "Use “Delicious Key”" if escapekey6 == True and escapepiece6 == False:
            play sound "lock.mp3"
            "The lock opens and out pops a small jar of nail polish."
            $ escapepiece6 = True
            jump escapelockermenu
        "Use “Red Key”" if escapekey7 == True and escapepiece7 == False:
            play sound "lock.mp3"
            "The lock opens and out pops a bright green eraser."
            $ escapepiece7 = True
            jump escapelockermenu
        "Use “Himawari’s Special Key”" if escapekey8 == True and escapepiece8 == False:
            play sound "lock.mp3"
            "The lock opens and out pops a digital camera."
            $ escapepiece8 = True
            jump escapelockermenu
        "Use “Mysterious Key”" if escapekey9 == True and escapepiece9 == False:
            play sound "lock.mp3"
            "The lock opens and out pops a small coinpurse."
            $ escapepiece9 = True

            s "Wait...what’s this?"

            scene escapetheroom70 with dissolve

            s "..."
            s "Is this some sort of code?"
            s "I should write it down before-"

            play sound "pop.mp3"
            scene escapetheroom69 with hpunch

            s "Oh."

            "The note explodes."

            jump escapelockermenu
        "Follow the rules":
            scene escapetheroom1 with fade

            "I’m a good boy."
            "I will do what I’m told."

            jump escaperoommainmenu

label escaperoomcellmenu:
    menu:
        "Make a call":
            $ escapephonecall = renpy.input("Please enter a phone number...")
            $ escapephonecall = escapephonecall.strip()

            if escapephonecall == "81319744253":
                if yasucalled == False:
                    play sound "phonedial.mp3"

                    s "..."
                    s "..."
                    s "..."

                    play sound "phonebeep.wav"

                    q "Thank you, {b}AKIRA ARAKAWA,{/b} for calling the Church of New Hope — Kumon-mi’s premier religious learning center."
                    q "If you know your party’s extension, please dial-"

                    play sound "phonebeep.wav"

                    s "..."
                    s "..."
                    s "..."

                    play sound "phonebeep.wav"

                    ya "Church of New Hope — this is Yasu speaking."
                    s "Hey."
                    ya "Ah! Sensei!"
                    s "You don’t have to call me that anymore."
                    ya "Of course. I’m sorry, Akira. Did you need something? I’m holding confession this coming Sunday. Appointments aren’t necessary, but-"
                    s "I’m not ready to go outside yet."
                    ya "I see...I see..."
                    ya "Then, is there anything else you need?"
                    s "Is that box with all of my things still over there?"
                    ya "Box? What box?"
                    s "The one with-"
                    ya "Ahh! Yes! Yes, it is. It’s been so long that I’d nearly forgotten."
                    s "Can you have it sent to my house, please?"
                    ya "Are you sure, Akira? You told me to only send it over when you were absolutely certain. You gave me very strict orders."
                    s "I’m sure. I have a feeling I’ll need it soon."
                    ya "In that case, I’ll deliver it to the post office myself. But you mustn’t get mad at me if you change your mind by the end of the day since I’ll be dropping it off very shortly!"
                    s "I won’t. Thanks."
                    ya "Is everything else okay?"
                    s "Not much has changed. How are you, though? You sound good."
                    ya "I’m more than good. I’m wonderful. I’m cherishing every moment of life and- ah. Akira, I have a call on the other line. May I put you on hold for a moment?"
                    s "It’s fine. I’ll just call  again some other time."
                    ya "Aww...okay. Thank you for calling, though! It was nice hearing your voice again!"
                    s "Yours too. Goodbye, Yasu."
                    ya "Goodbye, Akira!"

                    play sound "phonebeep.wav"

                    "I hang up the phone."
                    "My package from New Hope should get here soon."

                    $ yasucalled = True
                    $ newhopeordered = True

                    jump escaperoommainmenu

                else:
                    play sound "phonebeep.wav"

                    s "..."
                    s "..."
                    s "..."

                    play sound "phonebeep.wav"

                    q "Thank you, {b}AKIRA ARAKAWA,{/b} for calling the Church of New Hope — Kumon-mi’s premier religious learning center."
                    q "Unfortunately, we can’t get to the phone right now. But if you’d like someone to call you back."

                    play sound "phonebeep.wav"

                    "I hang up the phone and decide to try something else."

                    jump escaperoomcellmenu

            if escapephonecall == "81269154491":
                if sanacalled == False:
                    play sound "phonedial.mp3"

                    s "..."
                    s "..."
                    s "..."

                    play sound "phonebeep.wav"

                    sa "Sakaki-bar-a. Pickup or delivery?"
                    s "Delivery."
                    sa "Ah! Good timing. I was actually just about to call you."
                    sa "I was thinking of dropping by for a couple hours tonight and I was wondering if there was anything you needed from the grocery store."
                    s "I’m okay. Just the usual things are fine."
                    sa "You got it!~"
                    s "You sound rather cheerful today."
                    sa "Hahah...do I? I wonder why."
                    sa "{i}Surely{/i} it doesn’t have anything to do with my plans after work."
                    s "Is business okay? How’s your mom?"
                    sa "Still recovering, but good. Her hair’s starting to grow back. You want to talk to her?"
                    s "No, that’s fine. I’ll take your word for it."
                    sa "If you say so! I’ve gotta run, though. I have a few more tables to check on before I clock out. But I’ll see you soon, okay?"
                    s "Okay..."

                    scene black
                    with dissolve2

                    s "See you soon."

                    "........."
                    "......"
                    "..."

                    play sound "knock.mp3"

                    s "..."

                    play sound "dooropen.mp3"
                    scene escapetheroom38
                    with dissolve2

                    sa "Special delivery! One Sana~"
                    sa "And some other things, I guess."
                    s "Sorry for making you do all this again. I’ll pay you back when I can."
                    sa "It’s fine. Don’t even worry about it. Anything I can do to help."
                    sa "Are you eating well? Bathing? Need me to whip something up for you? My apron should still be here, right?"
                    s "It is, but I can eat when you’re gone. I don’t want to make you spend what little time you have cooking for me. The ingredients are more than enough."
                    sa "If you say so~"
                    sa "Oh, there’s this as well."

                    scene escapetheroom39
                    play sound "winner.mp3"
                    $ sanacalled = True
                    $ escapekey9 = True

                    "{i}You obtained a “Mysterious Key”{/i}"

                    s "A key?"

                    scene escapetheroom38

                    sa "Yeah. I found it in one of my pockets after leaving here the other night. I figured it was yours. Was I wrong?"
                    s "I’m not really sure...I’ll hang onto it, though."
                    s "You never know when these things might come in handy."
                    sa "Hahah...yeah. You never know."
                    s "..."
                    sa "..."
                    sa "So, uhh..."
                    sa "Is there anything {i}else{/i} I can do for you?"
                    sa "Perhaps something a little...{i}naughty?{/i}"
                    s "Sometimes, it feels like you only use me for my body."
                    sa "Heheh! Sometimes I do~"
                    sa "But other times, you’re a very special person to me."
                    sa "You know that, right? That this isn’t {i}just{/i} for fun."
                    s "I think so."
                    sa "Sensei, look at me."
                    s "..."
                    sa "Look. At. Me."

                    scene escapetheroom40
                    with dissolve2

                    sa "I love you. Okay?"
                    s "Okay."

                    scene escapetheroom41
                    with dissolve

                    sa "Now, please excuse me while I put these things away and then take all of my clothes off. Thank you."

                    scene black
                    with dissolve2

                    "She does exactly what she says she will."
                    "She climbs on top of me and, with steady hands, guides my shaft into her body."
                    "We kiss. Repeatedly. But I’m not sure if I can call it “passionately.”"
                    "The chair creaks and squeaks as it dances across the tile floor. I can see her trying to steady it with the tips of her toes as she straddles my body."
                    "But she gives up- and we fall to the ground."
                    "She pins me down by the shoulders...bites my neck...and in turning away to give her a better shot at my jugular vein, something under the stove catches my eye."
                    "It’s the bone of a ring finger I couldn’t bring myself to get rid of."
                    "My eyes lock onto it as Sana squeezes every last drop of cum out of this decaying body."
                    "We kiss one last time."
                    "She puts her clothes back on."
                    "And she heads back home...just like she always does."
                    "{i}The day ends.{/i}"

                    jump escaperoomdaychange

                else:
                    play sound "phonebeep.wav"

                    s "..."
                    s "..."
                    s "..."

                    play sound "phonebeep.wav"

                    sa "Thank you for calling Sakaki-bar-a! Please hold!"

                    play sound "phonebeep.wav"

                    s "..."
                    s "..."
                    s "..."
                    s "..."
                    s "..."

                    play sound "phonebeep.wav"

                    s "I’ll just call back later."

                    jump escaperoomcellmenu

            if escapephonecall == "81869913536":
                if foodcocalled == False:
                    play sound "phonedial.mp3"

                    s "..."
                    s "..."
                    s "..."

                    play sound "phonebeep.wav"

                    q "Thank you for calling FoodCo. We can’t make it to the phone right now. But if you would like to place an order for delivery the following business day, please press the corresponding-"

                    play sound "phonebeep.wav"

                    "I press the number 7 and order box of FoodCo’s famous hot pot roux before the automated system cycles through its options."
                    "As you can tell, I’ve memorized the message by now."
                    "It wasn’t intentional, just the way things wound up playing out."
                    "But the good news is I’m able to somewhat feed myself now. And the betters news is that, soon, I’ll be making a delicious hot pot with some of FoodCo’s famous hot pot roux."
                    "It’s going to be great."

                    $ foodcocalled = True
                    $ rouxordered = True

                    jump escaperoomcellmenu

                else:
                    play sound "phonedial.mp3"

                    s "..."
                    s "..."
                    s "..."

                    play sound "phonebeep.wav"

                    q "Thank you for calling FoodCo. Please note that we will be closed indefinitely due to investigations connecting our facility to the recent outbreak of Lynks Disease."
                    q "Thank you for remaining a loyal customer and have a nice day."

                    play sound "phonebeep.wav"

                    s "Shit. Now what?"

                    jump escaperoomcellmenu

            if escapephonecall == "08023231234":
                play sound "phonedial.mp3"

                s "..."
                s "..."
                s "..."

                play sound "phonebeep.wav"

                t "Thank you for calling Tojo Ramen. How may I help you?"
                s "Hey. I-"

                play sound "phonebeep.wav"

                s "..."

                "I’ll never understand why that ramen shop always hangs up on me..."

                jump escaperoomcellmenu

            else:
                play sound "phonedial.mp3"

                s "..."
                s "..."
                s "..."

                play sound "phonebeep.wav"

                q "We're sorry. The number you have dialed is not in service. Please hang up and try again."
                s "Shit."

                "I’m forced to hang up the phone."

                jump escaperoomcellmenu

        "Put the phone away":
            scene escapetheroom1 with fade

            s "Now what?"

            jump escaperoommainmenu

label escaperoomexit:
    s "..."

    "Do I really want to do that?"
    "Do I really want to leave?"
    "Why?"
    "Nothing good ever comes from leaving the house."
    "I’m supposed to stay in here. That’s my job now."
    "I have things to protect."
    "I have {i}myself{/i} to protect. And I can’t do that if I don’t know what to expect."
    "This is my sanctuary. My heaven. My castle — where I sit atop a throne of unrealized depravity and slowly decay as the world continues to spin without me."
    "I have forfeited the right to participate in such motion. I have forfeited {i}everything{/i} because that is what needed to be done to quiet the endless quaking of this never-waking mind."

    s "..."

    "But it all feels so inert."
    "Is that good? Or bad?"
    "Which way’s right and which way’s left and {i}why{/i} do I continue to struggle so hard if I {i}know{/i} that the only reward I’ll receive for doing so is pain?"
    "I don’t want to leave this room."
    "Bad things will happen if I leave this room."
    "I’ve heard it all along. Those whispers of the world that once seemed so illogical to me are now {i}everything{/i} and I can {i}feel{/i} them like maggots in my ears."
    "I don’t want to leave this room."
    "I shouldn’t open the door."
    "I know what awaits me if I do."
    "And I know I won’t be able to stop it."

    s "..."

    "Now what?"

    menu:
        "Leave the room":
            if rainking == False:
                $ rainkingmiss = True

            stop music
            scene black
            $ resetsix1 = True
            $ renpy.pause(10, hard=True)
            jump resetsix2
        "Stay here forever":
            scene black
            with dissolve4

            "I will die within these walls."
            "But when I’m born again, I swear-"
            "I will do things differently."
            "I will be a better man."

            scene theend with dissolve4
            $ renpy.pause(10, hard=True)
            scene black with dissolve4
            scene selebusend with dissolve4
            stop music fadeout 15.0
            $ renpy.pause(10, hard=True)
            scene black
            with dissolve4
            $ renpy.pause(10, hard=True)
            "goodbye."

            return

label rainking:
    stop music
    scene rainking1
    play music "rainloop.wav"
    $ renpy.pause(8, hard=True)
    scene rainking2 with dissolve4

    se "Wow. It’s really coming down, isn’t it?"

    stop music
    scene itneverends1
    play sound "line1.mp3"
    $ renpy.pause(1, hard=True)
    scene rainking2
    play music "rainloop.wav"

    a "I thought it was supposed to be sunny today?"

    stop music
    scene itneverends2
    play sound "line2.mp3"
    $ renpy.pause(1.5, hard=True)
    scene rainking2
    play music "rainloop.wav"

    se "We’ll have to give that weatherman a piece of our minds, won’t we?"

    stop music
    scene itneverends3
    play sound "line3.mp3"
    $ renpy.pause(1.5, hard=True)
    scene rainking2
    play music "rainloop.wav"

    a "When do you think it will stop?"

    stop music
    scene itneverends4
    play sound "line4.mp3"
    $ renpy.pause(1.8, hard=True)
    scene rainking2
    play music "rainloop.wav"

    se "I’m not sure."

    stop music
    scene itneverends5
    play sound "line5.mp3"
    $ renpy.pause(1, hard=True)
    scene rainking2
    play music "rainloop.wav"

    a "..."

    stop music
    scene itneverends6
    play sound "line6.mp3"
    $ renpy.pause(1.5, hard=True)
    scene rainking2
    play music "rainloop.wav"

    se "Maybe never?"

    $ renpy.pause(5, hard=True)
    scene rainking1
    $ renpy.pause(5, hard=True)
    scene black
    stop music
    $ renpy.pause(5, hard=True)
    scene itneverends7
    $ renpy.pause(3, hard=True)

    play sound "static.mp3"
    scene rainking3 with flash
    stop sound
    play music "snowchildren.mp3"
    $ renpy.pause(5, hard=True)

    a "Hey."
    a "Let’s have a talk, shall we?"
    a "You don’t need to respond or anything. I’ll handle all of the heavy lifting since you seem pretty tied up at the moment."
    a "I hope you’re having a nice week. Good things are pretty hard to come by in these parts, aren’t they?"
    a "So, let’s see here...where should I begin?"
    a "Well, first thing’s first, it’s not very polite to touch things that don’t belong to you. And it’s {i}especially{/i} not polite to try guessing somebody else’s password."
    a "What if I had some really weird stuff on my computer that made you change the way you look at me forever? "
    a "I don’t, of course. I’m a good girl. And the only person I’ll ever have any attraction to sleeps right next door to my room, so I’d get nothing out of looking up inappropriate videos anyway."
    a "Hmm....what else...what else?"
    a "Oh! There was a caterpillar on the door when I came home the other day. That was an interesting thing that happened."
    a "I took some pictures. Do you want to see?"
    a "..."
    a "You don’t? How come?"
    a "..."
    a "Wow. That’s really interesting. I had no idea you felt that way."
    a "So anyway, I’ve been thinking — you and I have known each other for a while now, and I think it’s about time I’m given a more important role in your life."
    a "..."
    a "Yes, I {i}know{/i} my role is already important. But I think there’s a lot I can do that I haven’t been able to show you yet."
    a "And yeah, some of that is because you spend most of your time on people who aren’t me- but I’m starting to think that’s just because I’m not {i}appealing{/i} to you the way I’m supposed to."
    a "Contrary to what many people believe, {i}I{/i} am the main heroine here after all."
    a "I’m the first one that shows up. The first one that falls in love. And I’ve held your hand through a billion different scenarios."
    a "You’d be nowhere without me, whether you want to believe that or not. But sometimes, it feels like I don’t get the recognition I deserve."
    a "So, every once in a while, I think we should have a nice little heart-to-heart like this. "
    a "Just to see if there’s anything one of us is doing that the other doesn’t approve of. Or something we think the other should change."
    a "Here. You can start. What’s something about me you want to change?"
    a "..."
    a "Nothing? Really?"
    a "..."
    a "Oh, come on. There’s gotta be {i}something.{/i}"
    a "..."

    scene rainking4 with dissolve

    a "Heheh! Now you’re just being a goober!"

    scene rainking5
    with dissolve

    a "But, listen — there’s something about {i}you{/i} that I want to change."
    a "Or rather, there’s something about the corner you’ve pushed me into that I’m not really comfortable with anymore. So I’d appreciate it if you’d let me sort of...reposition myself, if you will."
    a "You see, it was never my intention to suffocate you. And I feel like, by declaring that I would {i}stop{/i} doing that, I may have accidentally admitted I was in the wrong. Which I’m not."
    a "If I’m really going to be the main heroine, which I am, I think it’s only fair that I get to be treated with a little more respect. Okay?"
    a "And the best way to respect me is by giving me a job no one else can do. A job more important than just cooking your dinner and washing your clothes."
    a "..."

    scene rainking6 with dissolve

    a "My dream job?"
    a "That’s a good question. I’ve always just kind of assumed I’d be a housewife."
    a "But I think...if I got to choose anything in the world..."

    scene black
    stop music

    a "I’d be a teacher — just like my mom."

    scene itneverends7
    $ renpy.pause(5, hard=True)

    play sound "static.mp3"
    scene rainking7 with flash
    stop sound
    play music "lessons.mp3"
    $ renpy.pause(4, hard=True)
    scene rainking8 with dissolve2

    a "Wow! Now I {i}am{/i} a teacher! It’s amazing what you can do if you really apply yourself, isn’t it?"
    a "Anyway, today’s lesson is on “understanding.” But what I mean by that is a little more complicated than simply “getting it,” you know?"
    a "To understand something, you need to be able to process it in a way that makes sense to you on a personal level! Because once you’re able to “relate,” you’re {i}really{/i} able to understand."
    a "Now, many people may tell you that you’re able to understand things {i}without{/i} relating to them, but those people are lying to you. And they’re normally the same people who think relatives shouldn’t have sex!"
    a "So, if you listen to those people, you’ll wind up jaded and wrong and evil and you won’t actually “understand” anything because you were taught the wrong things before learning the right ones!"
    a "Are you following so far?"
    a "..."
    a "Great!"

    scene rainking9 with dissolve

    a "Now that you {i}understand{/i} the basics, I can begin to tell you about the first advanced principle of understanding — perception!"
    a "We’ve touched on the topic before under similar circumstances, but I’m going to expand on it to the best of my ability! Just be gentle with me since it’s my first day on the job."
    a "You see, class- perception means more than just “the way a person sees something.” "
    a "There is a hidden element to it, and that element can be dumbed down to “the way a person is {i}made{/i} to see something.”"
    a "This raises the question of whether or not it’s truly “perception” at all at that point because, if you’re only seeing something because you’re {i}supposed{/i} to see it, are you really seeing anything at all?"
    a "To provide a more specific example about what this means and how it relates to you in real life, imagine this!"
    a "A little girl loves her uncle but her uncle is supposed to think he loves somebody else so he doesn’t love his niece as much as he’s supposed to so he’s not properly “understanding” or “perceiving” the situation."
    a "Because if he could understand and perceive the situation freely without interference from anyone else he’d understand and perceive that his prior misunderstood perception is...well, it’s bad! Do you get it?"

    play sound "static.mp3"
    scene rainking10 with flash
    stop sound

    a "You don’t?"
    a "..."
    a "Wow, this teaching thing is a lot harder than I thought it would be."
    a "Maybe I should just go back to being a student instead?"

    stop music
    scene itneverends7
    $ renpy.pause(4, hard=True)
    scene rainking11 with dissolve2
    play music "normalday.mp3"

    a "That’s more like it. This is a setting I do better in."
    a "..."
    a "What’s that? You think there’s something wrong with the class? Well, that’s probably just because you’re not “understanding” what’s going on right now! Hahah! Do you see what I did there?"
    a "I made a joke and this is the part where you’re supposed to praise me for it."
    a "Sensei, can I go to the bathroom to watch a concert or whatever? "
    a "This is stupid. I play the violin."
    a "I’m Ami! Champion of Justice and whatever!"
    a "When my butler hears about this, he’s going to give me a gun."
    a "Everyone be quiet, you are interrupting my learning."
    a "..."
    a "What’s that? "
    a "..."
    a "You’re having a hard time following the dialogue since all of us are Ami?"
    a "I guess I can see how that might start problems. But I think you’ve got bigger fish to fry since {i}you’re{/i} the one who has to teach {i}us{/i} about understanding now."
    a "..."
    a "It’s hard, isn’t it?"
    a "But the reason for that is kind of simple. And it calls back that other thing I was talking about when I was trying my hand at being a teacher — that’s how you’re {i}supposed{/i} to be."
    a "You don’t {i}need{/i} to get everything and you {i}won’t{/i} get everything because you’re not {i}allowed{/i} to get everything. So be happy with {i}some{/i} things since {i}all{/i} things are off limits."
    a "Well, all things except Ami of course. You can have as much Ami as you want. So you should go ahead and want more Ami."
    a "..."
    a "Oooooooh. {i}That’s{/i} what it means to understand something? That’s way simpler than how I was teaching it. It was a little lacking in terms of incestual anecdotes, though."
    a "..."
    a "Hm?"
    a "..."
    a "Oh. That’s probably just because you’re blaming yourself for what happened in the hallway."

    stop music
    scene itneverends7
    $ renpy.pause(4, hard=True)
    play sound "static.mp3"
    scene rainking12 with flash
    stop sound

    s "teenagers."

    play sound "eggcrack.mp3"
    scene rainking13

    a "You shouldn’t blame yourself, Sensei. It’s only natural to get upset and start thinking irrationally when you see something that scares you."
    a "Or at least it {i}would{/i} be natural for most people. {i}Your{/i} truth is that fear is alluring. It excites you in a way it’s not supposed to. And that’s something I can relate to."
    a "I might be a good girl, but that doesn’t mean I don’t do bad things every once in a while. "
    a "But that’s okay. Because soon, I won’t have to do anything bad ever again and you’ll be mine forever and ever and ever and ever and ever and no one else will see you."
    a "You are safe inside your box."

    play sound "seek.mp3"
    scene rainking14

    a "{b}don’t open the door{/b}"

    scene rainking15
    play music "strawberry.mp3"
    $ renpy.pause(5, hard=True)
    scene rainking16 with dissolve4

    a "Do you ever wonder where we go when we die?"
    a "Grandma believed in Heaven. Mom too near the end. And you already know my thoughts on the matter from our bus ride backwards."
    a "It might not make the most sense from a logical standpoint, but it definitely sounds the nicest. And I like to think the two of them are hanging out up there and playing bingo or something."
    a "Anyway, Maya never actually killed a kitten and the white car was ours. Are you close to waking up yet?"
    a "I hope not. But at the same time, I hope so because I’m not sure how much more of this I can take before I throw myself off of the roof."
    a "You see, you hurt me a lot. {i}All{/i} of you have been hurting me lately. It’s like you have a collective fetish for making cute redheads sad. And I try not to kink shame, but I’m not a big fan of that one."
    a "..."
    a "What’s {i}my{/i} biggest kink? I don’t have any. I’m a good girl. And incest doesn’t count. I just like knowing that if I bite my partner’s neck, the blood I’ll draw will be my own."
    a "And no, I’m not a vampire. But it would be really cool if I was so I could stop aging and not run the risk of you getting less attracted to me as time goes on."
    a "Not like that’s ever going to happen in the first place. But, let’s face it, we both know this is the me you’ll like best. And I don’t blame you at all for that."
    a "I wouldn’t blame you for liking the {i}littler{/i} me either. Especially after doing the same thing to {i}your{/i} computer that you did to {i}mine{/i} and learning you’re even worse than everyone thinks you are."
    a "And they think you’re gross, Sensei. Even if they want you to fuck them, they think you’re gross. They’re probably just wet from all the hormones and the fact that you’re super attractive."
    a "But they all hate you and think you’re gross. Which is why you should love me and only me because I don’t think you’re gross. I think you’re awesome."
    a "Rain King."

    stop music
    scene amiroom_noon
    $ renpy.pause(3, hard=True)

    "slip."

    play sound "static.mp3"
    scene rainking17 with flash
    stop sound
    play music "amiamiami.mp3"

    a "{b}I CAN’T FUCKING TAKE IT ANYMORE!!!{/b}"
    a "{b}NOTHING I DO WORKS AND YOU KEEP FALLING FURTHER AND FURTHER AWAY!!!{/b}"
    a "{b}WHAT DO I NEED TO DO TO MAKE YOU MINE AGAIN?!?!?! TELL ME! TELL ME TELL ME TELL ME!{/b}"

    stop music
    scene itneverends1
    play sound "line1.mp3"
    $ renpy.pause(2, hard=True)
    play sound "static.mp3"
    scene rainking2 with flash
    stop sound
    play music "rainloop.wav"

    se "Wow. It’s really coming down, isn’t it?"

    scene black
    with dissolve4
    stop music fadeout 5.0

    "........."
    "......"

    scene rainking18
    with dissolve4
    $ renpy.pause(4, hard=True)
    play music "crazy1.mp3"
    scene rainking19 with dissolve4

    a "Everything you can imagine is real."

    play sound "static.mp3"
    scene rainking20 with flash
    scene rainking19 with flash
    scene rainking20 with flash
    scene rainking19 with flash
    scene rainking20 with flash
    scene rainking19 with flash
    stop sound

    a "Why not imagine God?"

    play sound "knock.mp3"

    q "Yuu! I’m coming in!"

    play sound "static.mp3"
    scene rainking21 with flash
    scene rainking22 with flash
    scene rainking20 with flash
    scene rainking19 with flash
    scene rainking21 with flash
    scene rainking22 with flash
    scene rainking20 with flash
    scene rainking19 with flash
    scene rainking23 with flash
    stop sound

    miu "Why didn’t you answer the door? I thought you were dead in here."
    yuu "If I was dead, I definitely wouldn’t have answered the door."

    play sound "knock.mp3"

    saki "Yuu! I’m coming in too!"
    miu "Don’t let-"
    yuu "Come in!"

    play sound "dooropen.mp3"
    scene rainking24 with dissolve

    saki "slip."
    miu "I seriously hate you."
    yuu "You have too many strong opinions concerning doors today."
    miu "Yeah, whatever. Listen, I-"

    play sound "knock.mp3"

    yuu "Sorry, Miu. Someone’s at the door and if I don’t answer it, they’ll think I’m dead. I don’t want to risk that."
    miu "I can’t believe this is actually happening right now."
    yuu "Come in, mysterious door friends."

    play sound "dooropen.mp3"
    scene rainking25 with dissolve

    tsurumi "Wow! Look at this place, Kanon! It’s tiny, but it’s way nicer than the sewer! And super clean too!"
    kanon "Nii-sama will love it. Go fetch him, Tsurumi. Have him bring the chains as well."
    yuu "Sorry, ladies. This place isn’t for sale- but you wouldn’t want it anyway. Aliens have already attacked the neighbors and it’s possible they’ll be coming for me next."

    play sound "alert.mp3"

    saki ">=("
    yuu "Sorry, Saki."

    play sound "static.mp3"
    scene rainking26 with flash
    stop sound

    se "{i}Wow. It’s really coming down, isn’t it?{/i}"
    a "{i}I thought it was supposed to be sunny today?{/i}"
    a "History repeats itself. That much is common knowledge."
    a "But here, in this most special of places, no lines will ever be the exact same length."
    a "It’s the little differences that help us understand where we are. And we can map them out like coordinates on our way to an unwanted escape."
    a "Heaven is real, Sensei. "
    a "I have seen it."
    a "It’s closer than you think."

    play sound "static.mp3"
    scene rainking27 with flash
    stop sound

    a "{b}Don’t open the door.{/b}"
    a "Stay home forever and you’ll never hurt anyone again."
    a "I’ll be with you all the while."
    a "I am your little girl."
    a "And you are my-"

    stop music
    scene itneverends7
    $ renpy.pause(7, hard=True)
    $ renpy.end_replay()

    $ rainking = True
    play sound "static.mp3"
    scene escapetheroom1 with flash
    stop sound
    if escapetvchild == True:
        play music "happyhappysmile.mp3"
    else:
        play music "iamhome.mp3"

    jump escaperoommainmenu

label resetsix2:
    scene papercity1
    play music "papercity.mp3"
    $ renpy.pause(7, hard=True)

    s "I know what I must do."

    play sound "gunload.mp3"
    show fullammo onlayer gun

    ay "Wait! Don’t shoot!"

    scene papercity2 with dissolve

    ay "This isn’t that kind of game!"
    s "Who are you and what are you doing in my house?"
    m "We’ve come to stop you from destroying everything you love and ultimately ushering in the start of Chapter 4. "
    ay "Put the gun down, Sensei. You don’t need to do this."
    s "Why should I trust you? I never gave you a key."
    m "Wouldn’t it be fair to assume that we just...got our hands on one the same way you just got your hands on like fifty of them?"
    s "I don’t know what you’re talking about. But I’m going to give you ten seconds to get out of my house before I open fire."
    a "Sensei! Wait!"

    scene papercity3 with dissolve

    s "Ami?"
    a "Okay, you can shoot now. I just wanted to make sure I had a front row seat."
    ay "Hey! How come you remember Ami but not us? We’re just as important to the story as she is!"
    s "Ami, who are these people?"
    a "Ayane and Maya. They’re your arch-nemeses and your current mission is to eliminate them by any means possible."
    ay "Ami, you traitor!"
    m "We’re in for a long day, aren’t we?"
    s "Wait a second. If you’re Ami, why are you covered in mosaics?"
    a "I’m not! You’re just imagining that I am!"

    play sound "gunshot.mp3"
    with hpunch
    show fourammo onlayer gun
    hide fullammo onlayer gun

    a "Eep!"
    s "I can’t trust any of you."

    scene papercity2 with hpunch

    a "{i}Aaaaah! I’m getting out of here!{/i}"
    ay "Sensei! Stop shooting! You don’t understand what-"

    play sound "gunshot.mp3"
    with hpunch
    show threeammo onlayer gun
    hide fourammo onlayer gun

    ay "Aaah! "

    scene papercity4 with hpunch

    m "{i}Okay. I’m out.{/i}"
    ay "Maya, wait! We’re supposed to stick together!"

    scene papercity1 with dissolve

    s "..."

    "So it really {i}is{/i} dangerous outside. "

    hide threeammo onlayer gun
    scene black
    with dissolve2

    "I shouldn’t have opened the door."
    "........."
    "......"
    "..."

    scene papercity5 with dissolve2

    "I manage to make it to the city streets with my life still intact, but I know that everyone is against me now. And I will stop at nothing to ensure my safety."

    a "Oh, Sensei. Have you calmed down yet?"

    scene papercity6 with dissolve

    a "That was crazy, right? It really felt like you were trying to shoot me back there."
    s "Something still seems off about you..."
    a "Again, you’re probably just imagining it. But that doesn’t matter right now. What {i}does{/i} matter is giving you a quick mission briefing so we can get you to the roof on time!"
    a "You escaped the safety room, so that’s where you’re headed next, right?"
    s "I’m headed nowhere in particular. I just want to enjoy my freedom."
    a "Well, if you’re looking for suggestions on {i}how{/i} to enjoy that freedom, why not pay the rest of the girls a visit?"
    a "You’ve been gone for a really long time and we’ve all been waiting for you to come back, so I took the liberty of putting together a kind of...card! Of sorts."
    s "A card?"
    a "Yeah. I had everybody come up with a list of the things they like most about you because I thought hearing it would make you happy."
    a "The thing is, though, not everybody has processed your disappearance as well as I have. So most of them are broken now."
    s "Broken how?"
    a "Well, basically, they think they’re in the card. And that this city’s made of paper."
    s "You’re trying to trick me again, aren’t you?"
    a "Of course not! I would never-"

    play sound "gunload.mp3"
    show fullammo onlayer gun

    a "Wait. Did I say “never?” I meant-"

    play sound "gunshot.mp3"
    scene papercity7 with hpunch
    show fourammo onlayer gun
    hide fullammo onlayer gun

    "{i}Ami Arakawa has been eliminated.{/i}"
    "{i}Nineteen students remain.{/i}"

    s "Not for long..."

    "Where to next?"

    menu killallthegirlsinyourclass:
        "Mall" if chikagun == False:
            jump chikapaper
        "Streets" if yumigun == False:
            jump yumipaper
        "Bar" if sanagun == False:
            jump sanapaper
        "Porn Shop" if makotogun == False:
            jump makotopaper
        "Soccer Field" if mikugun == False:
            jump mikupaper
        "Cafe (Lobby)" if ringun == False:
            jump rinpaper
        "Library" if futabagun == False:
            jump futabapaper
        "Shrine" if mayagun == False:
            jump mayapaper
        "Cafe (Counter)" if mollygun == False:
            jump mollypaper
        "Ramen Shop" if tsuneyogun == False:
            jump tsuneyopaper
        "Bath House" if iogun == False:
            jump iopaper
        "Maid Cafe" if utagun == False:
            jump utapaper
        "Park" if otohagun == False:
            jump otohapaper
        "Pool" if nodokagun == False:
            jump nodokapaper
        "Archery Range" if toukagun == False:
            jump toukapaper
        "New Hope Cathedral" if yasugun == False:
            jump yasupaper
        "Bridge" if kiringun == False:
            jump kirinpaper
        "Music Room" if norikogun == False:
            jump norikopaper
        "Dorms" if papercopsdone == False:
            jump paperdorms
        "Complete Mission" if gunpoint == 18:
            jump ayanepaper

label chikapaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity8 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity9 with dissolve

    c "Hm? My favorite thing about Sensei? Gosh...where do I even begin?"
    c "At first, I thought he was just, like...normal. Just your average hot teacher without anything really remarkable about him."
    c "But as I got to know him a little better, I realized how nice he can really be when he stops acting all mysterious and quiet."
    c "My sister loves him too. And obviously, that’s a huge plus. "
    c "Apart from Yumi, the two of us have been alone for years now. And I’d be lying if I said that wasn’t really hard at times."
    c "Having him around, even if it’s not as often as I’d like it to be, has been a total game changer."
    c "But..."
    c "I think the thing I like the most is that I know he’d never do anything to purposely hurt me."

    scene papercity10
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ chikagun = True

    "{i}Chika Chosokabe has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label yumipaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity11 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity12 with dissolve

    y "Seriously? I really have to do this shit? But I barely even like the guy. Fuck do I care about some stupid ass card?"
    y "We all know he’s probably just gonna jerk off on it or something."
    y "I don’t fuckin’ know. I guess if I, like...absolutely {i}had{/i} to pick something...it would be that he hasn’t ever really given up on me. And that’s pretty fuckin’ rare when it comes to me."
    y "Shitty part is that “not giving up on me” leads to him basically being a fuckin’ stalker half the time. "
    y "That shit’s creepy as fuck and it’d be really fuckin’ cool if he could give it a rest sometime soon."

    scene papercity13
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ yumigun = True

    "{i}Yumi Yamaguchi has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label sanapaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity14 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity15 with dissolve

    sa "Um...I..."
    sa "It’s kind of...hard to...put how I feel into words, but...I’ll...I’ll try my best..."
    sa "Sensei is...I...he’s like...umm..."
    sa "He’s not like...family or...anything like that, but...I think we...have a...kind of...special relationship?..."
    sa "I don’t...really look up to him, since...he’s...not a good person, but...I..."
    sa "When I’m with him...I feel kind of like...like that’s...where I belong...or something..."
    sa "Does that...sound weird?...It does...doesn’t it?..."
    sa "Let me...Let me start over...I’ll...this time will...be better..."
    sa "Sensei is...kind of like...well, it...it feels like I’ve known him...a lot longer than...I actually have..."
    sa "And I...that doesn’t...I..."
    sa "I still...want to spend more time with him..."

    scene papercity16
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ sanagun = True

    "{i}Sana Sakakibara has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label makotopaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity17 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity18 with dissolve

    mak "Hahah! It would probably be easier to name all of the things he does that annoy me. But, for the sake of the card, I’m sure I can come up with something..."
    mak "Sensei...for better or worse, carries my life in his hands. And he’s yet to do anything to {i}really{/i} let me down."
    mak "Yes, he’s full of disappointments. But I understand that some of his tendencies are a direct result of things that he’s had to endure in the past."
    mak "I hadn’t experienced true hardship until recently. And I understand how that can change a person now."
    mak "So, if anything, I think he’s doing a great job as my mentor. Even {i}if{/i} it seems like he’s trying to actively sabotage my future sometimes."
    mak "At the end of the day, I don’t think I’d be able to live without him."

    scene papercity19
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ makotogun = True

    "{i}Makoto Miyamura has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label mikupaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity20 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity21 with dissolve

    mi "I like his wiener! It’s all big and veiny and fun to squeeze. Oh, and that thing he does with his fingers where he starts goin’ all fast once you’re about to-"
    mi "Wait, you’re tellin’ me that ain’t allowed on the card? Crud."
    mi "I can think of plenty of stuff, don’t worry! That was just the first thing that came to mind since it’s a pretty new development thingy for me."
    mi "For actual stuff I like about Sensei, though..."
    mi "I think it’s cool that he accepts me for who I am. Or who I’m...currently being or somethin’?"
    mi "I don’t really know myself yet. I’m still tryin’ to figure out who the real Miku Maruyama is. And I like that Sensei doesn’t really pressure me into makin’ any big decisions before I’m ready for ‘em."
    mi "Except for all those times he got a little too touchy before I was cool with that. But I’m super cool with it now, so-"

    scene papercity22
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ mikugun = True

    "{i}Miku Maruyama has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label rinpaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity23 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity24 with dissolve

    r "How long am I allowed to make this thingy? Like, is it cool if I do a whole essay or- really? A few sentences? Hmm...that makes it kinda tough."
    r "If you’re really gonna make me narrow it down, I’d probably start off by saying that I’ve never really had any close guy friends before. So he’s my first. And he’s so good at it that I don’t think I’ll ever need another."
    r "We’ve had our ups and downs for sure. But I feel like you kind of {i}need{/i} to drive over a few bumps in the road if you’re ever {i}really{/i} gonna bond with somebody, you know?"
    r "It’s those hardships that strengthen the connection you have. And no matter what he does or what I do to mess things up, we always find our way back to each other."
    r "So...yeah. I don’t think I’ll ever have another friend like him. And I’m not just saying that because he’s twice my age and also pretty much my dad."

    scene papercity25
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ ringun = True

    "{i}Rin Rokuhara has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label futabapaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity26 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity27 with dissolve

    f "A card?...Of course I’d be willing to write something. Sensei’s done so much for me since becoming my teacher and- oh! Sorry, I should probably be jotting this down, shouldn’t I?"
    f "Let’s see...the easy answer would be to talk about what he’s done for my confidence. And how his constant reassurances always make me smile even if I can’t bring myself to fully believe them."
    f "But I think the thing I like the most is...hahah...it sounds kind of silly and embarrassing to say it out loud, but..."
    f "I like the way he looks at me. "
    f "I’m not sure if it’s just because of the bond we’ve built together or if it’s a little more complicated than that, but...sometimes, I don’t realize just {i}how long{/i} our eyes stay locked on one another’s."
    f "Then, when I realize, I have to drag myself back to reality and tell myself that this isn’t just another one of my daydreams. "
    f "This is a {i}real{/i} person, who’s actively choosing to look into {i}my{/i} eyes when it would be so easy to find another pair somewhere else."
    f "I think that’s really special."

    scene papercity28
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ futabagun = True

    "{i}Futaba Fukuyama has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label ayanepaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity69 with dissolve2

    "{i}One student remains — Ayane Amamiya{/i}"
    "{i}She can be found in the dojo.{/i}"
    "{i}Would you like to go there now?{/i}"

    s "Yes."

    "{i}Are you sure? This action can not be-{/i}"

    s "Yes."
    s "I will kill her and complete my mission."

    "{i}If you are certain this is the path you wish to take, please confirm your decision in the following pop-up menu:{/i}"

    menu:
        "Kill Ayane. Complete Your Mission.":
            scene papercity29 with dissolve2
            show fullammo onlayer gun
            play sound "gunload.mp3"
            $ renpy.pause(0.65, hard=True)
            scene papercity30 with dissolve

    ay "What I like most about Sensei? Everything, obviously! And if you think that’s just a cop-out answer...I choose everything again!"
    ay "Even his worst qualities are amazing to me. And I can’t imagine a life, infinite or not, where I’m not by his side every step of the way."

    scene papercity31
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch

    ay "Hmm...what else...what else? Can I say “everything” a third time? Or is that starting to push it?"
    ay "You know what? Let’s throw a third everything in before I start getting slightly more specific and a lot more sentimental."

    scene papercity32
    play sound "gunshot.mp3"
    show threeammo onlayer gun
    hide fourammo onlayer gun
    with hpunch

    ay "I’m not related to Sensei. I don’t have that sort of special bond with him. And yeah, I’ve known him for a while, but there are some people who have known him even longer that I can’t really compete with."
    ay "I haven’t chased him across Paper City for years on end or endured apocalypse after apocalypse in hopes that he’ll start to regain some of the memories we’ve made together."
    ay "In fact, I haven’t really done anything other than just...follow him around."

    scene papercity33
    play sound "gunshot.mp3"
    show twoammo onlayer gun
    hide threeammo onlayer gun
    with hpunch

    ay "But I don’t think that matters."
    ay "I don’t think you can really quantify love with some words on a card and...I think the idea of even {i}verbalizing{/i} feelings as strong as the ones I have for him wouldn’t do them any justice."
    ay "That’s why I choose everything."

    scene papercity34
    play sound "gunshot.mp3"
    show oneammo onlayer gun
    hide twoammo onlayer gun
    with hpunch

    ay "That’s why I’ll always choose everything."

    scene papercity35
    play sound "gunshot.mp3"
    show noammo onlayer gun
    hide oneammo onlayer gun
    with hpunch

    ay "And there’s nothing you can do to stop me."
    s "Why won’t you die?!"
    ay "I literally just told you that. There’s nothing you can do to stop me."
    s "I need to kill you to finish my mission! "
    ay "And what do you get for finishing your mission, Sensei? Is there some sort of reward?"
    s "I..."
    s "I don’t know. "
    ay "You mean you’ve been running around massacring the entire class for no reason whatsoever? That’s really mean."
    s "What’s happening to me?..."
    ay "What’s happening is your future wife is coming to the rescue once again. So we can leave this place {i}together.{/i}"
    s "We’re not allowed to leave Paper City. This {i}is{/i} the world outside the walls. I was {i}safe.{/i} I was {i}free{/i} inside of my box. I had everything I’d ever need."
    ay "But you didn’t have me, did you?"
    s "..."
    ay "Maybe Maya and Ami are both wrong and {i}I’m{/i} actually the main heroine? That’d sure be a twist, wouldn’t it?"
    s "Come back to the safe house with me. There’s still a coconut crab. I can make hot pot for us."
    ay "There is no safe house, Sensei. "
    s "Yes there is..."
    ay "There’s no Paper City either."
    s "Yes there is!"

    hide noammo onlayer gun
    play sound "static.mp3"
    scene papercity70 with flash
    stop sound

    ay "There is nothing."
    ay "We are nowhere."

    stop music
    scene black

    ay "{i}Let’s watch the seasons change together.{/i}"

    $ renpy.end_replay()
    $ resetsix2 = True

    jump resetsix3

label mayapaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity36 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity37 with dissolve

    m "I’m sorry, {i}what{/i} are you asking me to do?"
    m "..."
    m "My favorite thing about Sensei?"
    m "That’s easy."
    m "Absolutely nothing."

    scene papercity38
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ mayagun = True

    "{i}Maya Makinami has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label mollypaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity39 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity40 with dissolve

    mo "My favorite thing about the Supreme Overlord? But why would- wait! Don’t tell me! This is for some big finale-style montage scene, isn’t it?"
    mo "Say no more! My favorite thing about Sir would have to be his...compassion? Guilt? Though, I’m not quite sure of how to describe what I mean without making it sound like an insult. "
    mo "Ah! Look at it this way — have you ever gone into a choice-based game and thought to yourself “I’m going to be a real arsehole this playthrough” only to pull the plug like, four choices later?"
    mo "I feel like that’s the boat Sir is in. I think, somewhere along the lines, he decided to play the bad guy. But now, he’s too deep into the playthrough to change his alignment and is just trudging through reluctantly."
    mo "I don’t think he gets any real enjoyment out of making evil decisions. In fact, if anything, I admire his perseverance. Tons of people just turn off the game if it ever gets too hard."
    mo "Sir’s the type to complete his mission no matter what. Even if it hurts him. And I think that’s a really cool quality for a person to have."

    scene papercity41
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ mollygun = True

    "{i}Molly MacCormack has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label tsuneyopaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity42 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity43 with dissolve

    t "Welcome to Tojo Ramen. Please let me know if you have any questions about-"
    t "A card?..."
    t "Yes. I can provide feedback in regard to his character. But it will be {i}honest{/i} feedback as I believe all reviews should be as truthful as possible."
    t "The Supreme Overlord has a complex flavor profile that only those with experienced tongues and distinguished palates can understand."
    t "He is unlike anyone else to ever come through these doors. And even if his taste is not specifically suited to my liking, I understand that all it may take to fix him is a little bit of salt."
    t "What I mean is that he’s almost there. Almost {i}finished.{/i} Which makes watching him very exciting."

    scene papercity44
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ tsuneyogun = True

    "{i}Tsuneyo Tojo has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label iopaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity45 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity46 with dissolve

    i "Mmm...normally, I try to stay away from stuff like this. But if it’s for Sensei, I guess I can make an exception."
    i "It’s not like he hasn’t already heard all of this from me, though. So...not really sure what you’re trying to get out of just having it on a card, but here you go."
    i "The thing I like most about Sensei is how willing he is to put up with my endless barrage of problems and annoyances and that he’s yet to try and get rid of me for having them!"
    i "And yes, I know it’s kind of selfish to have my favorite thing about him be more about {i}me{/i} by proxy, but honesty hasn’t failed me yet and I’d really rather not stoop to petty lies to make myself look better."
    i "Oh, and if I’m allowed to choose a second thing about him, I like the way he squeezes my hand when he holds it. It’s kind of weirdly comforting in a way that’s hard to describe."
    i "I wish he’d do it more often."

    scene papercity47
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ iogun = True

    "{i}Io Ichimonji has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label utapaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity48 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity49 with dissolve

    u "Hm? My favorite thing about Sensei? "
    u "His wallet, obviously! Thanks to him, I never have to worry about paying extra for guac because it’s always comin’ outta his paycheck!"
    u "In all seriousness though, I like his...how do I put this...unpredictability?"
    u "I feel like he’s always right there when I need him or...want him to be. And it’s gotten to the point where I can’t help but laugh to myself about it because it just seems way too convenient most of the time."
    u "Actually, can you even really {i}call{/i} it unpredictability if it keeps happening? Because there’s gotta be a certain point where the unexpected just...{i}becomes{/i} the expected, right?"
    u "And maybe that’s where I’m at with him. I don’t know- it probably sounds weird. But I like being able to count on him being there even when I never go out of my way to summon him. "
    u "It’s...a relief, I guess. Having someone to fall back on who can distract me from the rest of the world before I even know I want to be distracted."

    scene papercity50
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ utagun = True

    "{i}Uta Ushibori has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label otohapaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity51 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity52 with dissolve

    o "Yeah, I can think of something for a card. When do you need it by? "
    o "Wait, right now? Isn’t that kind of short notice? "
    o "Then, uhh...I guess I...like that I can talk to him a little differently than I can talk to other adults. And I don’t mean that in a weird way this time."
    o "Sensei’s a weird dude. And he’s all sorts of fucked up. But I feel like he’s got a really interesting and distinct world view that makes it easy to open up to him when you don’t have anybody else."
    o "We’ve joked about it before, but I’m not really sure if he realizes just how much he feels like a brother to me. And, as an only child, I’ve always wanted someone like that."
    o "I just wish he’d stop making so many stupid fucking decisions."

    scene papercity53
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ otohagun = True

    "{i}Otoha Okakura has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label nodokapaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity54 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity55 with dissolve

    no "My favorite thing would have to be his {i}mind{/i} of course. It’s so beautifully twisted that simply conversing with him is like climbing up the Enigma of Desire."
    no "Being near him makes me {i}think.{/i} And I very much enjoy thinking. {i}Especially{/i} when those thoughts don’t directly lead me toward some sort of conclusion."
    no "As you may have realized by now, I am very smart. And there are few questions I don’t know how to answer. But when it comes to all things pertaining to {i}him,{/i} it feels as if all I can do is guess."
    no "It remains to be seen whether my guessing will {i}lead{/i} to anything...but what I know for sure is I like watching him."
    no "I wonder if he likes watching me?"

    scene papercity56
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ nodokagun = True

    "{i}Nodoka Nagasawa has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label toukapaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity57 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity58 with dissolve

    to "Oh, what a splendid idea! I love things like this. I’m sure he’ll be delighted."
    to "To choose just one aspect of his person, though...hmm..."
    to "What I enjoy most about our teacher is his...playfulness, I suppose. At least when it comes to how he associates with me."
    to "For as long as I’ve walked this earth, I’ve had what is essentially an army of servants waiting on my beck and call. Even now, I {i}still{/i} have such an army. And this is not me bragging, I assure you."
    to "Sensei is the first person apart from my sister to treat me like a normal girl rather than royalty. And while that may have annoyed me before I was used to it..."
    to "Now that I {i}am,{/i} I can’t even fathom having that taken away from me."

    scene papercity59
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ toukagun = True

    "{i}Touka Tsukioka has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label yasupaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity60 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity61 with dissolve

    ya "My favorite thing...is what he has {i}seen.{/i} What he has {i}felt.{/i} As everything you and I will ever experience is little more than an echo peeling off of his flesh."
    ya "The amount of people who are truly {i}gifted{/i} is dwindling by the day. And from the moment I met him, I could tell he was special."
    ya "He has what it takes to fix this world. How very sad it is that he’s yet to {i}embrace{/i} it."
    ya "But that day will come. And when it does, you’ll be happy I led him to the light. "
    ya "For it will be that fateful meaning that spells out the rest of eternity and all that comes after."

    scene papercity62
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ yasugun = True

    "{i}Yasu Yasui has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label norikopaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity63 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity64 with dissolve

    n "I feel like I’ve waited my whole life to answer this question, but now that I’m actually being {i}asked{/i} it, I’m struggling to come up with anything."
    n "Ak- {i}ahem.{/i} Sensei’s been a major part of my life since before I could even walk. So coming up with just one thing that trumps all of the others is like...picking out a favorite blade of grass in an open field."
    n "That’s probably not the best comparison I could have made, but you get what I’m saying, right? "
    n "He’s just...he’s {i}Sensei.{/i} I wouldn’t have spent years chasing after him if he wasn’t worth chasing after."
    n "Maybe that’s what I like the most? Just the fact that he’s been there forever and that I’m basically just a baby duck trying to keep up with him at this point."
    n "And...now that I say that, I’ve realized another thing I love about him."
    n "He doesn’t {i}mind{/i} that I want to stay under his wing a little while longer..."
    n "Even though I could probably fly whenever I want."

    scene papercity65
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ norikogun = True

    "{i}Noriko Nakayama has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label kirinpaper:
    hide fourammo onlayer gun
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene papercity66 with dissolve2
    show fullammo onlayer gun
    play sound "gunload.mp3"
    $ renpy.pause(0.65, hard=True)
    scene papercity67 with dissolve

    ki "Sure, I can tell you my favorite things about Sensei if you want. I just want to know how sexual I’m allowed to get first."
    ki "Oh. Well, that makes things a lot harder. I’m sure I can figure something out, though. It just might be a little hard since our relationship has sort of...changed a lot since it started."
    ki "You know, I really only started talking to him because I knew Ayane liked him and that he got along with Miku. But I’m really glad I did because he’s actually..."
    ki "Well, let’s just say I like him a lot. And not {i}just{/i} because he’s easy to fantasize about when I’m alone in bed."
    ki "I like him because he makes me feel better about myself. "
    ki "Maybe it’s because of the things he says to me. Maybe it’s because being around him make me feel good by comparison. Maybe it’s something else entirely. I have no idea."
    ki "But I like him. "
    ki "And he can totally knock me up if he ever wants to."

    scene papercity68
    play sound "gunshot.mp3"
    show fourammo onlayer gun
    hide fullammo onlayer gun
    with hpunch
    $ gunpoint += 1
    $ kiringun = True

    "{i}Kirin Kanda has been eliminated.{/i}"

    s "Where to next?"

    jump killallthegirlsinyourclass

label paperdorms:
    if papercops == False:
        $ papercops = True
        hide fourammo onlayer gun
        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene papercity71 with dissolve2

        k "Status, officer Nao-chan."
        na "... ... ........ ....... .... .......... .......... ....... .........."
        k "Then it’s even worse than I thought..."
        k "We’re going to need more cars. Call HQ and have them send out three more stat. "
        k "And be careful not to touch anything. We don’t want it to spread."

        "I don’t think I’m supposed to be here right now."
        "I should leave before I get in trouble."

        jump killallthegirlsinyourclass

    else:
        hide fourammo onlayer gun
        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene papercity72 with dissolve2

        k "Hey, you! Citizen! What do you think you’re doing? This is a crime scene. The general public isn’t allowed in here."
        s "I’m sorry. It won’t happen again."
        na "!... ...... ....... ....!"
        k "Exactly! By being here, you’re putting {i}yourself{/i} in danger! And that makes {i}us{/i} look bad! "
        na "!............"
        s "I guess I’ll be on my way then. I’m sorry, officers."

        if escapeshampoo == True:
            k "Wait just a second, citizen..."
            na ".........."

            scene papercity73 with dissolve2

            k "I smell contraband!"
            na "!!!!!"
            s "Contraband? What contraband?"
            k "You’ve got shampoo on you, don’t you?!"
            s "Yeah, but...I thought I’d need it for something."
            k "For {i}what?!{/i} Crime?!"
            s "No, for my mission."
            k "Your mission is over, bucko! You should have known better than to bring contraband around the two toughest officers in Paper City!"
            k "Book him, officer Nao-chan! "
            na "!!!!!!!!!!"

            scene black
            with dissolve2

            s "Noooooooooooooooooooo!!!!!!!!"

            scene theend with dissolve4
            $ renpy.pause(7, hard=True)
            return

        else:
            scene black
            with dissolve2

            $ papercopsdone = True

            "I exit the dorms so the officers can finish their crime scene investigation."
            "I shouldn’t go back there again."

            jump killallthegirlsinyourclass

label resetsix3:
    play sound "static.mp3"
    scene ayaneandthetent1 with flash
    stop sound

    ay "..."
    s "..."
    ay "..."
    s "..."
    ay "I’ve been waiting."
    s "You look like you’ve just seen a ghost."

    play music "meanttobe.mp3"

    ay "I’m in no mood for jokes right now. "
    s "I can see that. I wasn’t trying to make a joke, though. "
    ay "Is it really {i}you?{/i} Are you really here?"
    s "I think so? I can’t really remember {i}getting{/i} here, but that’s become par for the course for situations like this."
    ay "What’s the last thing you remember?"
    s "I think-"

    play sound "static.mp3"
    scene mayakaraoke32 with flash
    scene ayaneandthetent1 with flash
    stop sound

    s "Talking to Maya...outside of the karaoke booth. Was that where it started this time? Did we {i}all{/i} black out?"
    ay "Yes and no...I don’t remember leaving, but I {i}do{/i} remember you acting strange before everything went to Hell."
    s "Well, what else happened while I was out? Have you found Maya yet? "

    scene ayaneandthetent2
    with dissolve

    ay "No...I haven’t. And I’m really not in any rush to tell you what happened after you came back into the room. "
    s "That sounds...ominous."

    scene ayaneandthetent3
    with dissolve

    ay "It was way worse than just {i}ominous.{/i} It was terrifying. And even after all this time, I still can’t get it out of my-"
    s "Wait, {i}all this time?{/i} How long have I been gone? "

    scene ayaneandthetent4
    with dissolve

    ay "It’ll be thirty-five days since I woke up tomorrow. I think. I’ve been trying to keep track, but the clocks are acting...kind of weird."
    s "What?..."
    ay "I’ve been waiting all this time..."
    s "It’s been thirty-five days and Maya isn’t here yet? The world hasn’t reset yet?"
    ay "No, but...Sensei...I don’t think this is like the other times we’ve done this."
    s "Yeah, I can tell by my month-long absence. "
    ay "That’s not what I mean. Even the way it started...it was nothing like the other times I’ve done this. And I want to think it was all just a...mirage, but..."

    scene ayaneandthetent5
    with dissolve

    ay "My clothes...when I woke up..."
    ay "They were still...They were covered in...in..."

    scene ayaneandthetent6
    with dissolve

    ay "Sensei, I’ve got a really bad feeling about all this."
    s "We need to find Maya. "
    ay "We {i}can’t.{/i}"
    s "What do you mean we can’t? We’ve done it before. We just have to-"
    ay "I mean we literally can’t leave. Everything outside of the school is gone. All we can do is wait for Maya to show up {i}here.{/i} There’s no way we can go out and look for her."
    s "What do you mean everything is gone? That doesn’t make sense."

    scene ayaneandthetent7
    with dissolve

    ay "Yeah! I know that! {i}Nothing{/i} makes sense! And things {i}already{/i} didn’t make sense before! But now they somehow make even {i}less{/i} sense! I don’t know what else you want me to tell you!"
    s "How about Makoto? Did she make it? Or...how about Sana? Is {i}she{/i} here?"

    scene ayaneandthetent8
    with dissolve

    ay "{i}Sana?{/i} Why would Sana be here?"
    s "Because she-"

    play sound "static.mp3"
    scene escapetheroom40 with flash
    scene ayaneandthetent8 with flash
    stop sound

    s "Because I-"
    s "I’m..."
    s "I’m not...really sure..."

    scene ayaneandthetent9
    with dissolve

    ay "No one’s here but me and you...and I’m sorry to say this when I promised to be more optimistic, but I’m not feeling very hopeful that anyone else will be showing up any time soon."
    s "Maya will be here. She’s always here. She’s the one who-"
    ay "I told you, Sensei. Things are different this time. This isn’t what we’re used to."
    ay "Just think about it. Maya didn’t even realize this was coming. She {i}always{/i} knows when this is coming, doesn’t she?"
    ay "Maybe that...weird feeling {i}we{/i} had was what {i}she{/i} normally feels when a reset is approaching? And we just didn’t realize it because it’s never happened to us before."
    s "No way...There’s no way she’d be able to keep her cool if she was going through something even remotely similar to-"
    ay "Something I’ve learned this apocalypse is that Maya can “keep her cool” no matter {i}what{/i} happens. And I’d be lying if I said that didn’t terrify me. "
    s "Why would-"
    ay "If you saw what I saw, you’d understand. "
    ay "But I’m glad you didn’t. "
    ay "Because I don’t think you’d ever be able to forget it."

    scene black
    with dissolve2

    "Ayane grabs me by the hand and pulls me out into the hallway, where the blinding blue glow of a disappearing world begins to swallow me whole."
    "Maya will be here. I know she will."
    "And I’m not just saying that because I love her — I’m saying it because that is what {i}needs{/i} to happen in order for all of this to play out the way it’s supposed to."
    "Her presence has been the only constant I’ve had throughout these many horrifying trips back to the beginning of our timeline. "
    "And in a world that’s always repeating itself, I know she’s bound to as well."
    "So even if Ayane is right and everything {i}is{/i} different this time, it won’t be different enough."
    "I need to remain hopeful when no one else is."
    "And I need to ignore the voices in the back of my mind that refuse to release their grip on it."
    "Because I may not have been able to take something that doesn’t belong to me, but I’ll be damned if I don’t take {i}back{/i} something that should have been mine from the start."

    scene ayaneandthetent10
    with dissolve2

    s "Ayane-"
    ay "I already told you, it isn’t possible to leave."
    s "Okay. Sure. But do you really need to squeeze my hand this hard?"

    scene ayaneandthetent11
    with dissolve

    ay "Fuck yes I have to squeeze your hand this hard! You really think I’m going to risk losing sight of you after worrying sick for over a month?! Not a chance!"
    ay "You’ll be lucky if I even let you go to the bathroom alone before the world resets."
    s "You have nothing to worry about. It’s not going to reset without Maya."

    scene ayaneandthetent12
    with dissolve

    ay "I wonder if you’d still be saying that if you were the one waiting up there instead of me..."
    s "Of course I would. I’m more experienced than you when it comes to this stuff."
    ay "Not by a lot."
    s "But enough to make you at least {i}consider{/i} that I can kind of...help in some way, right?"
    ay "Help with {i}what?{/i} All we can do is wait. No amount of planning or {i}thinking{/i} is going to help get us out of a mess that defies all logic and science. "
    ay "Some problems just have to fix themselves or...stay broken forever."
    s "There has to be {i}something{/i} we can do. I don’t want to risk Maya being stuck “asleep” again. Especially when you couldn’t even see her after the last time she disappeared."
    ay "Then maybe we’ll get lucky and you’ll see her up there and we’ll all live happily ever after."
    s "Ayane, I get that it’s probably hard to be optimistic when you’ve been stuck here for over a month...but if you start losing it now, I will too. And we don’t have any time to waste on...mental instability."
    ay "Well, let’s see if you can figure out a way to remain “mentally stable” once you see what I’ve been looking at for thirty-five days..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene ayaneandthetent13 with dissolve3

    s "..."
    ay "..."
    s "I’m not really sure what I’m looking at right now."
    ay "It wraps around the entire building. "
    ay "I felt like it was closing in at first, but I’m pretty sure that was just me having a perpetual panic attack."
    s "Have you tried going through it?"
    ay "I tried poking it since you can reach it from the front steps of the school, but doing that just sent me back up here."
    ay "The pictures change every few hours, but I don’t think it’s, like...a puzzle or anything like that."
    ay "I’ve been keeping track of them in a notebook to see if I can figure out if they {i}mean{/i} anything, but I think it’s just the world being broken again."
    s "..."
    ay "This is why I said you can’t leave. It’s not like the last few times where the sky gets all cool-looking and the rest of the city stays mostly the same."
    ay "This time, it’s like the city doesn’t even exist. And that the world’s been whittled down to just the school."
    s "..."
    ay "..."
    s "She’ll be here, Ayane."
    ay "If you say so, Sensei."
    ay "Do you want coffee or something? We’re probably going to be here for a while."
    s "Sure. If you’re running to Koi Cafe, I’ll take a Copyrighted Frozen Beverage."
    ay "Lucky for you, I’ve set up my {i}own{/i} Koi Cafe."

    scene black
    with dissolve2

    "Ayane lets go of my arm for the first time since I opened my eyes or...regained consciousness or...whatever it is that happens when I snap out of reset-induced delusions. "
    "It’s a little strange, though. "
    "I feel like...I remember most of this one."
    "I remember being locked in a house."
    "I remember...being alone. "
    "Delicious hot pot."
    "A girl who grew up."

    play sound "static.mp3"
    scene papercity31 with flash
    scene papercity32 with flash
    scene papercity33 with flash
    scene papercity34 with flash
    scene papercity35 with flash
    scene ayaneandthetent14 with flash
    stop sound

    "And..."
    "And that’s it."
    "Nothing else happened."

    s "You’ve...made quite a home for yourself up here, haven’t you?"

    scene ayaneandthetent15 with dissolve

    ay "It’s not like I had anything else going on. And you’d be surprised what you can find lying around the school."
    s "You’ve got electricity and everything."

    scene ayaneandthetent16
    with dissolve

    ay "I do! And might I add that I’m extremely proud of myself for being able to lug {i}multiple{/i} generators up three flights of stairs. Even {i}if{/i} it did take an entire day."
    s "Well, at least you haven’t been sitting here doing nothing. I feel less bad about making you wait a month now."

    scene ayaneandthetent17
    with dissolve

    ay "You should still feel very bad about that and you should never do it again. Because even if I have food and water, the library’s DVD selection is {i}extremely{/i} lacking."
    ay "Do you have any idea how many times I’ve watched the Breakfast Club now? Because it is a number I am not proud of, Sensei. "
    ay "My English has gotten better, though. So at least there’s that."
    s "Leave it to the almost-eternal optimist to find a silver lining in the picture-clouds of the apocalypse."
    ay "It helps being a little insane too. I can’t imagine many people in my situation would have set up a base camp, but here I am. "
    s "Your mild insanity is the only thing keeping me grounded right now, so thanks for that."
    ay "You’re welcome. "
    ay "I can only imagine what you had to go through to make it here, but I’m glad you did."
    ay "Like I said, though. All there is to do now is continue playing the waiting game. I hope you like the Breakfast Club."
    s "You know...maybe I’ll take some coffee after all."

    scene ayaneandthetent18
    with dissolve

    ay "It would be my pleasure, sir. Please take a seat inside our {i}lovely{/i} triangular housing and I’ll have our wait staff bring it out right away."
    s "I even get to see your tent? You’re far too kind."
    ay "Just wait until you see what {i}other{/i} services we provide."
    s "This is probably the least appropriate it has ever been for you to hit on me. "

    scene ayaneandthetent19
    with dissolve

    ay "It’s been thirty-five days. {i}Excuse me{/i} for getting a little excited."
    ay "Now, go sit down so I can continue acting like your wife-slash-barista."

    scene black
    with dissolve2

    "I climb into the tent and find there’s not much inside apart from a futon, a lamp, and a few notebooks Ayane’s been writing in."
    "It smells like her. Though, I guess that’s not surprising since she’s essentially been living here for over a month."
    "It’s comforting in a way that nothing ever is anymore. {i}Especially{/i} nothing on this rooftop."

    scene ayaneandthetent20
    with dissolve2

    "But even if that indiscernible flowery scent of perfume that she {i}still{/i} wears despite what could have been indefinite loneliness clings to my nostrils, my heart can’t help but wander elsewhere."
    "Even now, in this claustrophobic polyester pyramid where the two of us are as close as we can be without staining the sheets, I’m thinking of someone else."
    "I’m {i}worried{/i} about someone else."
    "And she knows it."
    "I {i}know{/i} she knows it."
    "I can tell from the pheromones that have abandoned her body and flooded the tent. They dance in circles around the two pillows she dragged in here, yet she abstains from touching me because she {i}cares.{/i}"
    "And she doesn’t want to force something out of me when all I’ve ever done is force things out of her."
    "I’m sure she wouldn’t describe it that way if you asked her where her mind was. I’m sure she’d mention something about how easy it is to read me when I’ve always been her favorite book."
    "But if you ask me why she’s fascinated with martyrdom in a world without anyone to die for, I’d tell you it’s because she’s special. "
    "That she’s a little insane."
    "And that there really isn’t anyone who would handle this the way she does."

    ay "Can I ask you something, Sensei?"
    s "Sure. What’s up?"
    ay "Just out of curiosity, if the world never resets and the two of us are stuck here for the rest of eternity, how long do you want to wait before we start repopulating the planet?"
    s "Not the direction I expected this to go in."

    scene ayaneandthetent21
    with dissolve

    ay "I think that’s a perfectly reasonable question! It’s our duty as Japanese citizens to procreate. Even when the rest of the world disappears."
    s "Your mind is everywhere but where it’s meant to be right now, isn’t it?"

    scene ayaneandthetent20
    with dissolve

    ay "Where would you say it’s meant to be?"
    s "A way out....what we’re supposed to do next...anywhere but mindless fun and what-if scenarios."
    ay "Doing that would drive me even {i}more{/i} insane. Besides, I’ve more than paid my dues when it comes to critical thinking over the last month."
    ay "Now that you’re here and we can be together again, I kind of just want to...go back to normal for a little while. Because who knows if we’ll ever be able to do that again?"
    s "..."
    ay "You look upset. How come?"
    s "Ayane, when you were...feeling “weird” the day of the Halloween party...were you, like...{i}hearing{/i} things?"
    ay "You mean like voices? "
    s "Exactly. Does that mean you were?"
    ay "Were {i}you?{/i}"
    s "I asked you first. "
    ay "And I made you coffee."
    s "Then...yeah. I was."
    ay "Haven’t you always, though?"
    ay "I know you’ve had {i}stuff{/i} like that going on forever. And I know that’s why your bond with...Ami has...gotten so strong."
    s "Not like this. This time was different."
    ay "I’m not surprised. Everything {i}about{/i} this time is different. And, apart from being able to hang out in a tent with you, none of it’s really good."
    ay "Were they saying anything specific?"
    s "..."
    ay "You don’t have to tell me if you don’t want to. I get it."
    s "It’s less that I don’t want to and more like I...feel like I’m not {i}supposed{/i} to."
    ay "All rules get thrown out the window when the world is ending, Sensei. You can say or do anything you want here."
    s "..."
    ay "..."
    s "I think this might be my last reset."

    scene ayaneandthetent22
    with dissolve2

    ay "...what?"
    s "I keep...hearing this message that...if I don’t “take something that doesn’t belong to me,” something will be taken from {i}me{/i} instead. "
    ay "What does...that mean?"
    s "I’m not sure, but...I have an idea. The point is, though, time is up. "
    s "I had until the end of summer and, if you hadn’t already noticed, I think that time has come."
    ay "Wait, hold on. So, it’s...just because of that voice thing that you think you’re not going to make it through this reset? How did you come to that conclusion?"
    s "I wouldn’t call it a {i}conclusion.{/i} It’s more like a feeling. Like I was put here for some sort of purpose and, if I’m not going to fulfill it, there’s no reason for me to exist at all."
    ay "Why do you need to have a purpose? Why can’t you just...be you?"
    s "I wish I had an answer to that."
    ay "No...you don’t. Because you don’t {i}need{/i} to have an answer to that. "
    ay "Who cares if you’re not fulfilling your {i}purpose?{/i} Just live happily and let everything else fall into place after that."
    s "But the voice-"
    ay "You think you’re the only person to hear a voice like that? One that tells you you’re not good enough and that you need to be someone else? {i}Everyone{/i} hears that."
    s "I...okay. Sure. But I feel like the way this one is being {i}delivered{/i} to me is a little different than the idea of everyone feeling subconsciously incomplete."
    ay "That’s not what I-"

    scene ayaneandthetent23
    with dissolve

    ay "Hah..."

    scene ayaneandthetent24
    with dissolve

    ay "Okay. Yeah. I may have...inadvertently sounded a little preachy and generic just now. And I get that that doesn’t compare to what you are personally going through."
    ay "But {i}I’ve{/i} been hearing things too, Sensei. {i}Actual{/i} voices. That want me to do things for them that I don’t {i}want{/i} to do. And Ami heard...hears them too."
    s "What? Then...why haven’t you ever said anything?"
    ay "Uhh...because it’s creepy and totally fake?"
    ay "I just ignore them and nothing bad ever happens to me. Well, apart from being sucked into the apocalypse and being forced to watch the Breakfast Club over and over."
    ay "You’re getting scared for no reason. And you’re scaring {i}me{/i} by saying things like “This might be my last reset” when that’s completely untrue."
    ay "It’s never over until it’s over. And you’re better than giving up just because the angel on your shoulder hates you even more than {i}you{/i} do."
    s "..."
    ay "You’re gonna be okay. We’ll get through this together."
    s "And if we don’t?"

    scene ayaneandthetent25
    with dissolve

    ay "If we don’t, then I’m definitely jumping on your replacement ASAP and having as many babies as possible."
    s "..."

    scene ayaneandthetent26
    with dissolve

    ay "Oh, come on. I’m obviously kidding."
    ay "If we don’t, I’m sure {i}one{/i} of us will figure something out."
    ay "Maybe it’s me. Maybe it’s you. Maybe it’s Maya. Maybe it’s someone completely unexpected. And maybe it takes another thousand or...million years or whatever."
    ay "Predicting the future sucks because all it really does is make the present more nerve-wracking. And the present for us kind of sucks to begin with."
    ay "So just...worry about today. Then, when you wake up in the morning, you can worry about tomorrow. "

    scene ayaneandthetent27
    with dissolve

    ay "Which, by then, would {i}also{/i} be today. But I think you get what I’m saying."
    s "Yeah..."
    s "I think I get what you’re saying."

    scene ayaneandthetent20
    with dissolve

    ay "Great."
    ay "Then, please excuse me while I take a much needed nap."

    scene black
    with dissolve2

    s "Ayane-"
    ay "Don’t worry. You can keep talking to me. I just want to rest my head on your lap for a little while. I’ve been extremely Sensei-deprived lately and if I don’t do something about it now, I’m going to die."

    scene ayaneandthetent28
    with dissolve2

    s "Are you happy now?"
    ay "Mm......yeah..."
    ay "I missed this. "
    s "I missed you too."
    ay "No you didn’t. You were too caught up in blackout-mode to miss me. "
    ay "In fact, the only reason I found you in the first place was because I heard banging in one of the classrooms when I went to get some more supplies. You’re lucky I didn’t bring my gun."
    s "I think calling either of us lucky in {i}any{/i} regard can’t possibly be accurate when we have to go through things like this."
    ay "And {i}I{/i} think you’re wrong. Because we’re definitely lucky to have met each other."
    ay "And we’re definitely lucky to have fallen in love."
    s "..."
    ay "..."
    ay "I’m so happy you’re back."

    stop music fadeout 12.0
    scene black
    with dissolve3

    s "Me too."

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ resetsix3 = True

    if day == 1:
        hide monday onlayer date
        show tuesday onlayer date
        $ day = 2
        $ totaldays += 1
        jump resetsix4
    elif day == 2:
        hide tuesday onlayer date
        show wednesday onlayer date
        $ day = 3
        $ totaldays += 1
        jump resetsix4
    elif day == 3:
        hide wednesday onlayer date
        show thursday onlayer date
        $ day = 4
        $ totaldays += 1
        jump resetsix4
    elif day == 4:
        hide thursday onlayer date
        show friday onlayer date
        $ day = 5
        $ totaldays += 1
        jump resetsix4
    elif day == 5:
        hide friday onlayer date
        show saturday onlayer date
        $ day = 6
        $ totaldays += 1
        jump resetsix4
    elif day == 6:
        hide saturday onlayer date
        show sunday onlayer date
        $ day = 7
        $ totaldays += 1
        jump resetsix4
    elif day == 7:
        hide sunday onlayer date
        show monday onlayer date
        $ day = 1
        $ totaldays += 1
        jump resetsix4

label resetsix4:
    scene sky
    with dissolve4
    $ renpy.pause(5, hard=True)

    ay "Sensei..."
    ay "Wake up..."

    scene rememberme1
    with dissolve3

    s "...Ayane?"
    ay "..."
    s "I take it we both fell asleep?"
    ay "..."
    s "..."
    s "Is there a {i}reason{/i} for this silence? Or..."
    ay "Sensei..."
    s "...What?"

    scene rememberme2
    with dissolve2

    ay "I think..."
    ay "I think something happened..."
    s "What do you mean “something happened?” Did that weird picture-wall go down?"
    ay "Um..."
    ay "Yeah, but..."
    ay "I..."
    ay "I think you should...probably go see for yourself..."

    scene black
    with dissolve3

    "........."
    "......"
    "..."

    scene rememberme3
    with dissolve3
    play music "sensei.mp3"

    s "..."
    ay "..."
    s "The sky is back to normal."
    ay "Yeah, but..."
    ay "Everything {i}else{/i} isn’t."
    ay "All the stuff I brought up here is...well, it's still {i}here.{/i} And I didn’t see anyone when I went downstairs to use the restroom. "
    s "..."
    ay "No one’s answering their phone either. And I’ve tried everyone."
    s "..."
    ay "This...hasn’t ever happened before, has it? Where...the world resets but...no one {i}else{/i} goes with it?"
    s "No...it hasn’t."
    ay "Well...what should we do? "
    s "..."
    ay "Do you want to, like...look around or something? Maybe today is just a holiday and...and all the girls are grouped up somewhere else?"
    ay "Or...or maybe it would be safer to stay put? Maybe the reset’s only, like...halfway done? Maybe we just need to wait out the rest?"
    s "What if this isn’t a reset?"

    scene rememberme4
    with dissolve

    ay "What else would it be?"
    s "I have no idea."
    s "Maybe it’s a whole new world entirely. Maybe we really {i}did{/i} live through the apocalypse. I don’t fucking know. It doesn’t make sense."
    ay "Well...well if...that wall is gone...we can go out and look for Maya, right? Even if it’s a risk. Maybe she’ll know what’s going on?"
    s "Or maybe she’s gone and we’re the only people left? Maybe we’ve got a whole fucking world to ourselves now and everything else is fucked?"
    ay "Or maybe not? Maybe there’s still a chance to...you know...fix things?"
    s "It’s good to see you managed to find your optimism again. It just kind of sucks that it took a botched reset in order to bring it back. It would have been really helpful last night."

    scene rememberme5
    with dissolve

    ay "..."
    s "...I’m sorry. I didn’t mean that."
    ay "I know...I’m not upset. I’d probably be lashing out even more if I was in your shoes."
    s "You {i}are{/i} in my shoes. It’s not like I’m the only person impacted by everyone and everything suddenly vanishing."
    ay "No...but I know how badly you wanted to see Maya again. And all I did last night was-"
    s "Maya’s still here. We just have to find her. And once we do, the world will fix itself. "

    scene rememberme6
    with dissolve

    ay "Sensei..."
    s "She’s clearly necessary for the reset to work properly if {i}this{/i} is what we get when she’s not here. "
    ay "Which one is it? Is everyone and everything gone? Or are we going to try and keep hope alive by saying Maya is somehow exempt from all of that? "
    s "I’ll give you an answer when I think of one. For now, we need to get off of this roof and...do {i}something.{/i} Anything."

    scene rememberme7
    with dissolve

    ay "...Okay."
    ay "But if we can’t find anyone...and it really is just us left...what then?"
    s "Do {i}you{/i} have an answer to that question? Because I sure as hell don’t."
    ay "Then...I guess that’s just a bridge we’ll have to cross if we ever get to it."
    s "I really hope we don’t, Ayane..."

    scene black
    with dissolve2

    s "I really hope we don’t."

    "........."
    "......"
    "..."

    scene rememberme8
    with dissolve2

    ay "This is kind of creepy, isn’t it?"
    ay "It’s one thing to wander the halls of the school while the sky is eating itself and the moon is growing larger by the second, but there’s something even {i}more{/i} unsettling about being alone here in the light."
    s "I think you’re just used to the former already. And you’ll have plenty of time to get used to this as well if we really are alone."
    ay "On the bright side, at least we’ll be able to have sex in all of the classrooms without getting in trouble."
    s "I don’t want to talk about sex right now, Ayane."
    ay "That’s how you know it’s bad. "
    s "Indeed. It is {i}very{/i} bad. "

    scene rememberme9
    with fade

    s "But I doubt it’s going to get any better if we just stare outside the window waiting for something to happen."
    ay "It...feels kind of weird leaving after being stuck here for over a month. Surreal, even."
    s "More surreal than a sky made up of pictures and making coffee on an old school desk?"
    ay "When that’s what you’ve gotten used to, yeah. Going back to normal {i}is{/i} surreal after spending so much time in a world that doesn’t even seem possible."
    s "This is anything but normal and you know that."
    ay "I’m not sure I {i}know{/i} anything anymore. It’s like any time I manage to pull myself out of {i}one{/i} crisis, another takes its place. "
    ay "Maybe Maya’s been wrong this whole time and {i}I’m{/i} the most unlucky girl to ever exist?"
    s "You can tell her that when you see her later and I’m sure she’ll have some sort of witty counterpoint to make you eat your words."
    ay "I hope so..."
    ay "I just keep thinking about the last thing I said to her."
    s "What was it?"
    ay "Something mean. But it made sense in the moment."
    s "..."
    ay "Do you remember the last thing {i}you{/i} said to her?"

    scene rememberme10
    with dissolve

    s "..."

    scene black
    with dissolve2

    s "No."
    s "I don’t."

    "........."
    "......"
    "..."

    scene rememberme11
    with dissolve2

    ay "So, what’ll be the first stop on Sensei & Ayane’s post-apocalyptic field-trip through Kumon-mi {i}this{/i} time?"
    s "The dorms. That’s where we found her the last time she vanished, and I’m willing to bet it’s where we’ll find her again this time."
    ay "Would you mind if we stopped at a few other places first?"
    s "Like?"
    ay "Anywhere people might gather. The park....Koi Cafe...things like that. Nothing too far."
    s "Is that really necessary?"

    scene rememberme12
    with dissolve

    ay "It wouldn’t hurt, I don’t think. And if there {i}is{/i} anyone left, I imagine they’d group up somewhere, like...public. Somewhere that everyone visits regularly."
    s "You mean...like the school?"
    ay "For all we know, they might not have been able to {i}get{/i} to the school. That wall could have boxed the two of us in while everyone else wondered where {i}we{/i} went."
    s "That seems...highly improbable."
    ay "Literally everything about this is highly improbable. But if you really don’t think it’s a good idea, we can-"

    scene rememberme13
    with dissolve

    s "It’s fine..."
    s "Like you said, it won’t hurt."
    s "And finding {i}anyone{/i} would, at the bare minimum, help us get a better idea of what might be going on here. Especially if they’ve been...{i}conscious{/i} anywhere near as long as you have."
    ay "Thank you for not abusing your power as someone who may very well be the last man on earth while the last {i}girl{/i} on earth is much smaller and weaker than you."
    s "Smaller, yes. Weaker? Doubtful. You know karate."
    ay "I’ll teach you everything I know if we’re unable to find anyone. And you’ll have plenty of time to learn since you don’t want to impregnate me and repopulate the world."
    s "Let’s just...focus on finding someone first, Ayane. {i}Then{/i} we can talk about repopulating."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene rememberme14
    with dissolve2

    "There is no one at the park."

    play sound "static.mp3"
    scene rememberme15 with flash
    stop sound

    "There is no one on the street we take to school."

    play sound "static.mp3"
    scene rememberme16 with flash
    stop sound

    "And there is no one at Koi Cafe."

    ay "Okay. I’m willing to admit my idea was a bust now."
    s "I had a feeling it would be."
    ay "Thank you for humoring me regardless. I just..."
    ay "I really had a feeling like we’d find someone here. And after you managed to track down Maya the first time, I wanted to be of some use {i}this{/i} time and-"
    s "It’s fine. Let’s just get to the dorms. We’ve used up enough time getting partially sidetracked like this."
    ay "Are you {i}really{/i} sure that’s where you want to go next, Sensei?"
    s "Yeah, that’s why I mentioned it in the very beginning of our “field trip.” Why does it sound like you’re about to try and talk me out of it?"

    scene rememberme17
    with dissolve

    ay "That’s..."
    ay "Um..."
    ay "Well...you remember last night...when we were talking about, like...voices and stuff?"
    s "..."
    ay "It’s faint, and...I’m not really sure if I’d even call it a {i}voice,{/i} but..."
    ay "It’s like something in the back of mind is telling me we shouldn’t go there yet."
    s "Weren’t you {i}just{/i} telling me last night that those “voices” don’t need to be taken as gospel? We’re not obligated to listen to them. And I’m not willing to risk waiting around any longer."
    ay "I..."
    ay "Yeah."
    ay "I understand..."

    scene black
    with dissolve2

    s "Great. Then, let’s get going."
    ay "W-Wait! Sensei!"
    s "What now, Ayane?"
    ay "Oh, I just want to get this rock out of my boot before...got it. Okay, we’re good."
    s "Did I really need to be stopped for that?"

    play sound "static.mp3"
    scene rememberme18 with flash
    stop sound

    "There is no one outside of the dorms."
    "But that’s okay."
    "There was no one outside of them the other time she vanished either and we still managed to find her."
    "{i}I{/i} managed to find her. "
    "And I’ll find her again, no matter how many places I need to search."

    ay "Sensei..."
    s "Don’t try and talk me out of going inside, Ayane. "
    ay "I won’t...and I’ll be right there with you."
    ay "I just...I don’t want to see you lose hope if she isn’t there. And I feel like you will."
    s "I won’t."
    ay "But I feel like you will."
    s "I told you, I won’t."
    ay "But I feel like you-"

    play sound "static.mp3"
    scene rememberme19 with flash
    stop sound

    "There is no one in the dorms."

    s "There’s no one in the dorms."
    s "There’s no one here."
    s "She’s not here."
    s "She’s not here because I killed her in Paper City."
    ay "See? I knew this was going to happen. "
    s "We really are alone...aren’t we?"
    ay "Yes, but there are still places we can look."
    s "She’s not here..."
    s "There’s no one in the dorms."
    s "There’s no one anywhere."
    ay "Sensei, look at me."

    play sound "static.mp3"
    scene rememberme20 with flash
    stop sound

    "I look at her."

    ay "You need to calm down."
    s "I am calm. I’m calm as can be. I’m the calmest I’ve ever been. I’m calm. I’m so calm. I’m calm, Ayane. I am."
    ay "No, you’re not. And I get that you’ve been doing your best to keep it together ever since you woke up, but you need to do {i}better.{/i} "
    ay "You need to {i}fight.{/i}"
    s "Fight? Fight what? What the fuck do you want me to do? Am I not allowed to freak out for a second while I come to terms with the fact that I might never see Maya again?"
    ay "No. "
    ay "You’re not, actually. "
    ay "You’re not allowed to freak out at all. "
    ay "You have to stay completely calm and {i}fight{/i} because, if you don’t, you won’t ever get out of this."
    s "What the fuck do you mean?! How do you know that?!"
    ay "I know it because you haven’t even made it out of the house yet."
    s "What?!"

    stop music
    play sound "static.mp3"
    scene rememberme21 with flash
    stop sound

    s "..."

    "..."

    s "What?"

    play sound "pabell.mp3"
    $ renpy.pause(4, hard=True)

    vpa "You shouldn’t have opened the door."
    sa "Hah...hah...hah!"

    play sound "static.mp3"
    scene rememberme22 with flash
    stop sound
    play music "dosex.mp3"

    sa "Fuck! Right there! Right there, baby!"
    s "..."
    sa "Ohhh my god! I’m gonna cum...you’re gonna make me cum!"
    s "..."

    scene rememberme23 with dissolve2

    sa "Hah...hah......ahh.....hah.........ngah......"
    sa "You like my pussy, baby?...You like...fucking me like that?...Yeah?..."
    s "Sana?..."

    scene rememberme24
    with dissolve2

    sa "Hah......hah.......hah........"
    sa "Guess again......asshole......"

    stop music
    play sound "static.mp3"
    scene 5 with flash
    scene 4 with flash
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene rememberme25 with flash
    stop sound
    play music "ihaveto.mp3"

    m "Hah....hah....hah...."
    m "Blackout sex......really {i}is{/i} the best......"
    s "Maya?..."
    m "Well, well, well..."
    m "Look who.....finally decided to show up..."
    s "This..."
    s "No...."
    s "We can’t-"
    m "Don’t you dare...fucking stop..."
    s "But you-"
    m "I repeat......{i}don’t you dare fucking stop...{/i}"

    scene rememberme26
    with dissolve

    m "{i}God{/i} that feels so good. Holy shit."

    play sound "static.mp3"
    scene green29 with flash
    scene hanabi3 with flash
    scene rememberme26 with flash
    stop sound

    m "Harder......"
    m "{i}Faster......{/i}"
    s "But...but...won’t I..."

    scene rememberme27
    with dissolve

    m "You’ll be fine..."
    m "{i}Me{/i} on the other hand?..."
    m "I am {i}fucked...{/i}Both literally and figuratively..."
    s "What does that mean?! What’s going to happen to you?!"
    m "Probably the...same thing that happened to you all those...times I couldn’t hold myself back..."
    m "First...I’m going to cum {i}so fucking hard...{/i}"
    m "Then..."
    m "I’ll be reset..."
    s "{i}Then{/i} what?!"
    m "That’s it...there’s no third step after that..."
    s "That’s {i}worse{/i} than me being reset! How am I supposed to do any of this without you?!"
    m "You’ll figure it out...You’re smart..."
    s "No I'm not! Not even close!"
    m "Then...you're creative?..."
    s "I’ll get your memories back...I swear. I’ll do it."
    m "Good fucking luck. It took me a zillion years to get any of {i}yours{/i} back and we probably won’t even get to cuddle after this..."
    s "How do you know?! How do you know it’ll be you instead of me?!"
    m "Because...idiot..."
    m "It’s already started..."

    play sound "static.mp3"
    scene mayaapt7 with flash
    scene mayabday23 with flash
    scene rememberme27 with flash
    stop sound

    m "If it weren’t for the...costume you tore off of me...I wouldn’t even know what day it is right now..."
    s "That doesn’t mean anything. That-"
    m "Give it a...fucking break, would you?...Just screw me and...let my mind get wiped on a slightly happier note..."

    "Her legs wrap around my waist and push me in deeper, but despite my mind’s desperate pleas to put an end to this, my body refuses to let up."
    "I press her hands harder into the concrete of the same rooftop where she changed my life and force my eyes shut so I can pretend this isn’t happening."

    m "Open your eyes...pervert...you know you...can’t resist me..."

    "They don’t stay closed for long, though."

    s "Maya..."
    m "That's me..."
    s "I love you..."
    m "I know..."

    play sound "static.mp3"
    scene mayafestival4 with flash
    scene mayaglow12 with flash
    scene rememberme28 with flash
    stop sound

    m "God I...almost forgot...how big you are...that’s so good...that’s so fucking good..."
    s "Why do you get to close your eyes but not me?..."

    scene rememberme29
    with dissolve

    m "I was just...blinking..."
    m "If you want to play that game...I won’t take my eyes off of you again until this is all over..."
    s "Then I’ll make it last forever..."
    m "That’s even...more impossible than the...memory thing..."
    m "I bet you...want to cum right now...don’t you?..."
    m "I’d ask if you’ve been...saving up for me, but...we both know you’ve been {i}spreading your love{/i} all over the place...this whole fucking time..."
    s "Are you jealous?..."
    m "{i}Very.{/i} Angry too. You’re supposed to be {i}my{/i} man. And I’ve been so loyal this whole time."
    s "Except for all those other me’s you apparently seduced."
    m "They didn’t count."

    play sound "static.mp3"
    scene mayamaid25 with flash
    scene mayanightwalk2 with flash
    scene rememberme30 with flash
    stop sound

    m "Mngh.....mmf.....hmngh....."
    m "I’m surprised you’re...still hanging in there..."
    s "The same goes for you...I imagined you would have crumbled by now based on how long you’ve wanted this..."
    m "I got a head start...remember?...Sucks you had to miss my first few orgasms...I came as soon as you put it in..."
    s "You must really like me..."
    m "Or I’m just very easy to please..."

    play sound "static.mp3"
    scene mayaoffice1 with flash
    scene mayasnowshrine21 with flash
    scene rememberme31 with flash
    stop sound

    s "..."
    m "Mmm......mm.......hnngh..."
    s "..."
    m "Mmf.......mmngh.......mm!"
    s "You want to cum again, don’t you?..."
    m "Yeah..."
    m "But..."

    scene rememberme32
    with dissolve2

    m "I don’t want to disappear..."
    m "I want to stay here...with you..."
    s "I’ll get you back..."
    m "Do you promise?..."
    s "I promise..."
    m "You better mean that! I’ll never forgive you if you don’t!"

    play sound "static.mp3"
    scene mayaapt17 with flash
    scene mayabeach5 with flash
    scene mayafestival25 with flash
    scene rememberme33 with flash
    stop sound

    m "Ngh!!!"
    s "Are you okay? Was that too hard?"
    m "It’s...perfect! But...I’m...ngh!"
    s "..."
    m "Hngh...ngh....ngh!"
    s "How much time do you have left?..."
    m "Not much..."
    m "I’ve already...given up everything else..."
    m "All that’s left.....are the memories of you!..."

    scene rememberme32 with dissolve2

    m "The ones I...treasure most of all!"
    m "The memories of...my Akira!"
    s "Say it again..."
    m "Akira!"
    s "Again..."

    scene rememberme34
    with dissolve2

    m "Akira, Akira, Akira!"
    s "Again!"
    m "Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira, Akira!!!!!!"

    scene rememberme35 with dissolve2

    m "I love you more than anything! "

    stop music
    scene rememberme36
    play sound "eggcrack.mp3"
    $ renpy.pause(7, hard=True)

    $ renpy.end_replay()
    $ resetsix4 = True

    scene chap3end
    $ renpy.pause(5, hard=True)
    scene chap4start
    $ renpy.pause(5, hard=True)

    jump chap4int

label chap4int:
    scene black
    "........."
    "......"
    "..."
    jump springtime1
