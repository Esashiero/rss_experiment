label beachsix7:
    scene white
    $ renpy.pause(1, hard=True)
    scene ftwa
    $ renpy.pause(1.3, hard=True)
    scene white
    $ renpy.pause(1, hard=True)
    play sound "static.mp3"
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene flowertime1 with flash
    stop sound
    play music "flowersforalgernon.mp3"
    $ renpy.pause(3, hard=True)
    scene flowertime2
    $ renpy.pause(2, hard=True)
    scene flowertime1
    $ renpy.pause(2, hard=True)
    scene flowertime3
    $ renpy.pause(2, hard=True)
    scene flowertime1
    $ renpy.pause(2, hard=True)
    scene flowertime4
    $ renpy.pause(2, hard=True)
    scene flowertime1
    $ renpy.pause(2, hard=True)
    scene flowertime5
    $ renpy.pause(2, hard=True)
    scene flowertime1
    $ renpy.pause(1, hard=True)
    play sound "pop.mp3"
    scene flowertime6 with hpunch

    taki "Hey, hey, hey! New games you will play! What do you say? "
    s "Nay."
    taki "Neigh? ¿Qué? Are you gay?"
    s "I am not interested in your games, Horseface Taki. You have interrupted my dinner. And for that, you will pay."
    taki "You seem to misunderstand your latest kerfuffle, Akira Arakawa. The whole world is watching you right now. Permission to refuse has NOT been granted."
    s "Aww man. How come they always have to watch me when I’m naked?"
    taki "How come you’re always naked? "
    s "Probably sex. And also because you guys keep taking my clothes off every time I’ve gotta do one of these thingies."
    taki "Ah! So you know where you are after all?"
    s "Another reset right? At least the song is kind of chill this time. I’m straight vibing rn, Horseface Taki."

    "I start to do another jig to appease the God of the Track. Soon, I will race with the best. "
    "He jigs along, but only for a few seconds. He clearly has a job to do and I am but his silly little employee."

    taki "Okay, okay. That’s enough dancing for now. Let me explain the rules of the game. "

    scene flowertime1
    with dissolve

    taki "This one’s pretty simple, all things considered."
    s "Oh god. That means it’s going to be super complicated, doesn’t it?"
    taki "Not at all! In fact, you were already 14.29%% complete before coming here. Just six more pieces and you’re done!"
    s "Pieces of what?"
    taki "I’m getting there, okay?"

    scene flowertime7
    with dissolve2

    taki "The goal of this game is to track down the six missing Maya pieces so you can put her back together and continue your journey."
    s "I don’t like this game, Horseface Taki."
    taki "Not {i}yet{/i} you don’t! But you’ll soon find that this isn’t as complicated as navigating the waiting room or filling out magazine sweepstakes."
    taki "In fact, uncovering the missing Maya pieces is as easy as asking your friends if you can have them! "
    s "You brought my friends here? Which ones?"
    taki "Well, telling you now would spoil the surprise! "
    taki "It’s {i}your{/i} job to look around and figure that out yourself. But be warned — some of them might not be willing to part with their fraction of Maya and might ask for something in exchange."
    s "Sounds simple enough. I’m used to transactions like this. I’ve lost count of how many times I’ve traded my wiener for warmth and affection."
    taki "Unfortunately, you can’t trade your body in this game. You need to trade items instead. And each friend will have specific preferences you’ll need to match."

    scene flowertime1
    with dissolve
    scene flowertime6
    with dissolve

    taki "Just obtaining these items would be too easy, though. You’ll need to assemble them yourself. But hey, that’ll be good practice for when you have to reassemble Maya."
    s "What happens when I do that? Is the game over?"
    taki "Once Maya is reassembled, the portal back to your world will be opened. But you’re also free to keep hanging out here if you want. And who knows? Maybe you’ll find something else too!"
    s "Something else? Like what? Extra body parts for Maya? Because I kind of like her a lot the way she is now. "
    taki "A severed head?"
    s "Huh? Oh. No. I meant when all of her pieces are put together. I kind of forgot she was just a head now."
    taki "Unfortunately, I can’t tell you what you’ll find out there. But I {i}can{/i} tell you you won’t find anything by just standing around and talking to me!"
    taki "Venture out and test your knowledge once more! And remember — the whole world is watching. You wouldn’t want to leave a bad impression, would you?"
    s "Of course not. Thank you, Horseface Taki. You are easily the most helpful god I have encountered thus far."
    taki "Right now, I am just a Lesser God. I must guide at least eighty-five more people through these events until I am eligible for promotion."
    s "Well, get ready. Because it’s {i}about{/i} to be eighty-four."
    taki "I think you might be greatly overestimating the frequency at which these are actually completed."

    scene flowertime1
    with dissolve

    s "Doesn’t matter. The fact remains that it’s time to go collect the pieces of my girlfriend’s corpse and carry her back to my world!"
    s "Reset puzzle...begin!"

    $ mayapieces = 1

    menu buildamayahub:
        "Use the workbench":
            jump buildamayaworkbench
        "Use the PC":
            jump buildamayapc
        "Check your Maya’s progress":
            jump buildamayaprogress
        "Go somewhere":
            jump buildamayaoutside

    ##################################################

label buildamayaworkbench:
    if flowerbenchseen == True:
        scene flowertime8 with fade

        "I return to the workbench and prepare to get my hands dirty."
        "What should I do?"
        jump buildamayaworkbenchmenu

    else:
        $ flowerbenchseen = True

        scene flowertime8 with fade

        "I make my way over to a workbench decorated with everything I could possibly need to grow various plants and craft small trinkets."
        "It seems like this would be a good place to assemble any of the objects my friends are on the prowl for. "
        "What should I do?"
        jump buildamayaworkbenchmenu

    menu buildamayaworkbenchmenu:
        "Plant something":
            jump buildamayaplantmenu
        "Craft something":
            jump buildamayacraftmenu
        "Stop using the workbench":
            "I have grown tired of this workbench. I am going to do something else now."

            scene flowertime1
            with fade

            "What should that be, though?"

            jump buildamayahub

    menu buildamayaplantmenu:
        "Plant corpseflower" if corpseseed == True:
            "I carefully place the corpseflower seed into the soil and drizzle a little water onto it."
            "........."
            "......"
            "..."
            play sound "winner.mp3"
            scene flowertimecorpse

            "Wow! It’s fully grown already!"

            scene flowertime8
            with dissolve

            "I carefully remove the corpseflower from the soil and shove it into my pocket. "
            "It’s way too big for it and it smells kind of bad, but what else am I going to do about it?"

            $ corpseseed = False
            $ buildamayacorpse = True

            jump buildamayaplantmenu
        "Plant lavender" if lavenderseed == True:
            "I carefully place the lavender seeds into the soil and drizzle a little water onto them."
            "........."
            "......"
            "..."
            play sound "winner.mp3"
            scene flowertimelavender

            "Wow! It’s fully grown already!"

            scene flowertime8
            with dissolve

            "I carefully remove the lavender from the soil and shove it into my pocket. "
            "I hear a whisper from the attic but decide it’s just another ghost and ignore it."

            $ lavenderseed = False
            $ buildamayalavender = True

            jump buildamayaplantmenu
        "Plant poppies" if poppyseed == True:
            "I carefully place the poppy seeds into the soil and drizzle a little water onto them."
            "........."
            "......"
            "..."
            play sound "winner.mp3"
            scene flowertimepoppy

            "Wow! They’re fully grown already!"

            scene flowertime8
            with dissolve

            "I carefully remove the poppies from the soil and shove them into my pocket. "
            "I hope this doesn’t get me high."

            $ poppyseed = False
            $ buildamayapoppy = True

            jump buildamayaplantmenu
        "Plant roses" if roseseed == True:
            "I carefully place the rose seeds into the soil and drizzle a little water onto them."
            "........."
            "......"
            "..."
            play sound "winner.mp3"
            scene flowertimerose

            "Wow! They’re fully grown already!"

            scene flowertime8
            with dissolve

            "I carefully remove the roses from the soil and shove them into my pocket. "
            "The thorns dig into my thigh and cause me to bleed. Is this the price of love?"

            $ roseseed = False
            $ buildamayarose = True

            jump buildamayaplantmenu
        "Plant snapdragons" if dragonseed == True:
            "I carefully place the snapdragon seeds into the soil and drizzle a little water onto them."
            "........."
            "......"
            "..."
            play sound "winner.mp3"
            scene flowertimesnapdragon

            "Wow! They’re fully grown already!"

            scene flowertime8
            with dissolve

            "I carefully remove the snapdragons from the soil and shove them into my pocket. "
            "I can feel myself getting stronger. Do I have superpowers now?"

            $ dragonseed = False
            $ buildamayadragon = True

            jump buildamayaplantmenu

        "Go back":
            jump buildamayaworkbenchmenu

    menu buildamayacraftmenu:
        "Corpsecrown" if buildamayacorpse == True and sticks >= 1:
            $ sticks -= 1
            $ buildamayacrown = True
            $ buildamayacorpse = False

            "I bend some sticks into a circle and peel off pieces of the corpseflower to wrap around it."
            "I figure this might make a good accessory for one’s head."

            play sound "winner.mp3"

            "{i}You have received a {b}Corpsecrown{/b}!{/i}"
            s "Fuck yeah."

            jump buildamayacraftmenu

        "Rose Bouquet" if buildamayarose == True and sticks >= 1:
            $ sticks -= 1
            $ buildamayabouquet = True
            $ buildamayarose = False

            "I tear the flowery parts off of the flowers off and place them onto new stick-based stems that won’t decay over time."
            "This should work, right?"

            play sound "winner.mp3"

            "{i}You have received a {b}Rose Bouquet{/b}!{/i}"
            s "Fuck yeah."

            jump buildamayacraftmenu

        "Lavender Perfume" if buildamayalavender == True and sticks >= 1:
            $ sticks -= 1
            $ buildamayaperfume = True
            $ buildamayalavender = False

            "Using some of the sticks Makoto gave me as a makeshift pestle, I grind the lavender into a fine paste and empty it into a jar I found in Ami’s room."
            "Whatever was inside the jar mixes with the lavender quite well. And before I know it, I have perfume."

            play sound "winner.mp3"

            "{i}You have received {b}Lavender Perfume{/b}!{/i}"
            s "Fuck yeah."

            jump buildamayacraftmenu

        "Snapdragon Bracelet" if buildamayadragon == True and sticks >= 1:
            $ sticks -= 1
            $ buildamayabracelet = True
            $ buildamayadragon = False

            "I bend some sticks into tiny circles and braid them around each other before plucking petals from the snapdragons and adhering them to said circles with glue."
            "Horseface Taki looks on in anguish for some reason. I don’t get it."

            play sound "winner.mp3"

            "{i}You have received {b}Snapdragon Bracelet{/b}!{/i}"
            s "Fuck yeah."

            jump buildamayacraftmenu

        "Opium" if buildamayapoppy == True and sticks >= 1:
            $ sticks -= 1
            $ buildamayaopium = True
            $ buildamayapoppy = False

            "I extract opium from the poppy latex and prepare it for distribution."
            "Sticks are somehow involved."

            play sound "winner.mp3"

            "{i}You have received {b}Opium{/b}!{/i}"
            s "Fuck yeah."

            jump buildamayacraftmenu

        "Ultimate Stick Bouquet" if sticks >= 5 and buildamayanoriko and buildamayafutaba and buildamayachika and buildamayasana and buildamayayumi:
            $ sticks = 0
            $ buildamayaultimate = True

            "When I think to myself about what Makoto likes, there is only one thing that comes to mind."
            "Sticks."
            "She has so many of them lately and has never explained why."
            "What this means is that I should make her an ultimate bouquet consisting entirely of sticks in order to show my gratitude for her help."
            "I do that."

            play sound "winner.mp3"

            "{i}You have received the {b}Ultimate Stick Bouquet{/b}!{/i}"
            s "I’m coming, Makoto."

            jump buildamayacraftmenu

        "Go back":
            jump buildamayaworkbenchmenu

    ##################################################

label buildamayaprogress:
    scene flowertime9
    with fade

    "I make my way over to the bed and lay out a sheet of cardboard so the Maya pieces don’t cross-contaminate the place I sleep."

    menu buildmayaprogressmenu:
        "Dump out Maya pieces":
            if mayapieces == 1:
                play sound "tackle.mp3"
                scene flowertimemaya1 with hpunch

                "I dump my bag of Maya out onto the bed and take a look at what I’ve collected so far."
                "Seems like I still have a lot of work to do."

                s "Hang in there, Maya. I’ll put you back together in no time at all."

                menu:
                    "Repack Maya":
                        scene black
                        with dissolve
                        play sound "tackle.mp3"

                        "I shove my collection back into the bag of Maya and get on with my mission."

                        scene flowertime1
                        with dissolve

                        "Now what?"

                        jump buildamayahub

            if mayapieces == 2:
                play sound "tackle.mp3"
                scene flowertimemaya2 with hpunch

                "I dump my bag of Maya out onto the bed and take a look at what I’ve collected so far."
                "I’m making progress, but it still seems like I still have a lot of work to do."

                s "Hang in there, Maya. I’ll put you back together in no time at all."

                menu:
                    "Repack Maya":
                        scene black
                        with dissolve
                        play sound "tackle.mp3"

                        "I shove my collection back into the bag of Maya and get on with my mission."

                        scene flowertime1
                        with dissolve

                        "Now what?"

                        jump buildamayahub

            if mayapieces == 3:
                play sound "tackle.mp3"
                scene flowertimemaya3 with hpunch

                "I dump my bag of Maya out onto the bed and take a look at what I’ve collected so far."
                "I’m almost half-way done now."

                s "Hang in there, Maya. I’ll put you back together in no time at all."

                menu:
                    "Repack Maya":
                        scene black
                        with dissolve
                        play sound "tackle.mp3"

                        "I shove my collection back into the bag of Maya and get on with my mission."

                        scene flowertime1
                        with dissolve

                        "Now what?"

                        jump buildamayahub

            if mayapieces == 4:
                play sound "tackle.mp3"
                scene flowertimemaya4 with hpunch

                "I dump my bag of Maya out onto the bed and take a look at what I’ve collected so far."
                "Only a few pieces remain now. I’m more than halfway done."

                s "We’re getting there, Maya. I’m doing my best."

                menu:
                    "Repack Maya":
                        scene black
                        with dissolve
                        play sound "tackle.mp3"

                        "I shove my collection back into the bag of Maya and get on with my mission."

                        scene flowertime1
                        with dissolve

                        "Now what?"

                        jump buildamayahub

            if mayapieces == 5:
                play sound "tackle.mp3"
                scene flowertimemaya5 with hpunch

                "I dump my bag of Maya out onto the bed and take a look at what I’ve collected so far."
                "Just the legs are left now."

                s "...Do we really even need her legs, though?"

                menu:
                    "Repack Maya":
                        scene black
                        with dissolve
                        play sound "tackle.mp3"

                        "I shove my collection back into the bag of Maya and get on with my mission."

                        scene flowertime1
                        with dissolve

                        "Now what?"

                        jump buildamayahub

            if mayapieces == 6:
                play sound "tackle.mp3"
                scene flowertimemaya6 with hpunch

                "I dump my bag of Maya out onto the bed and take a look at what I’ve collected so far."
                "Only one piece of her remains."

                s "Just a little longer, my sweet girl. "
                s "I will fix you. I promise."

                menu:
                    "Repack Maya":
                        scene black
                        with dissolve
                        play sound "tackle.mp3"

                        "I shove my collection back into the bag of Maya and get on with my mission."

                        scene flowertime1
                        with dissolve

                        "Now what?"

                        jump buildamayahub

            if mayapieces == 7:
                play sound "tackle.mp3"
                scene flowertimemaya7 with hpunch

                "I dump my bag of Maya out onto the bed and take a look at what I’ve collected so far."
                "At long last, she is complete."

                s "You’re as beautiful as the day I met you."

                menu:
                    "Repack Maya":
                        scene black
                        with dissolve
                        play sound "tackle.mp3"

                        "I shove my collection back into the bag of Maya and get on with my mission."

                        scene flowertime1
                        with dissolve

                        "Now what?"

                        jump buildamayahub

                    "Complete Maya assembly":
                        jump endofbuildamaya

        "Complete Maya assembly" if mayapieces == 7:
            jump endofbuildamaya
        "Go back":
            scene flowertime1
            with fade

            "That’s enough of that, I suppose. "
            "What should I do now?"

            jump buildamayahub

    ##################################################

label buildamayaoutside:
    scene flowertime10
    with fade

    "I step outside to find absolutely no one."
    "Looks like I’ve got some walking to do."

    "Where do I want to go?"

    menu buildamayagomenu:
        "DEN OF THE MOLE RAT" if buildamayanoriko == False:
            jump buildamayanorikorealm
        "CARTOGRAPHER’S CRAB-SHACK" if buildamayafutaba == False:
            jump buildamayafutabarealm
        "UNBLEACHED BEACH" if buildamayasana == False:
            jump buildamayasanarealm
        "UNBLEACHED BEACH" if buildamayakoitip == True and swimtrip2 == False:
            jump buildamayaprehappy
        "THE SMILE MILE" if buildamayamakoto == False:
            jump buildamayamakotorealm
        "SPACY’S SUMMER BLAST SAVINGS EVENT" if buildamayachika == False:
            jump buildamayachikarealm
        "OLD(ER) DISTRICT" if buildamayayumi == False:
            jump buildamayayumirealm
        "HOUSE":
            s "On second thought, I’m too scared to be out here."

            scene black
            with dissolve
            play sound "dooropen.mp3"

            s "I’ll feel much safer inside with Horseface Taki."
            "........."
            "......"
            "..."

            scene flowertime1
            with dissolve

            "Now what?"

            jump buildamayahub

    ##################################################
label buildamayapc:
    scene flowertime11
    with fade
    play sound "computeryay.mp3"

    "I sit down at my PC, knowing full well it isn’t going to help me put Maya back together. "
    "I can at least kill some time and rot what’s left of my brain, though."
    "What do I want to do?"

    menu buildamayacomputermenu:
        "Check Messages":
            jump buildamayamessages
        "Research Koi" if buildamayakoi == True and buildamayakoitip == False:
            "If Makoto is going to trust me with this fish, then by golly am I going to raise it right."
            "As such, I pull up the invisible Internet and begin typing invisible letters into an invisible search engine."

            s "K...O...I. Koi. That should do it."

            "I spend the next half hour obtaining fish-based information and come to a saddening realization."
            "Fish belong in the water."

            s "Oh no."

            scene flowertime1
            with fade

            "I step away from the computer and check on the fish."
            "It’s still alive, but just barely. "
            "I need to do something about this."

            $ buildamayakoitip = True

            jump buildamayahub

        "Nothing":
            "I sit there and stare at the screen for hours, but somehow time doesn’t change."
            "I feel kind of dizzy."
            "Now what?"
            jump buildamayacomputermenu

        "Go back":
            s "God, what am I doing? I have to save Maya."

            scene flowertime1 with fade

            s "No more messing around."

            jump buildamayahub

label buildamayamessages:
    "I bring up my invisible email page and begin to filter through my equally invisible messages."

    if buildamayanoriko or buildamayafutaba or buildamayasana or buildamayamakoto or buildamayachika or buildamayayumi:
        play sound "youvegotmail.mp3"

        s "!!!"

        "It appears that I have mail. "
        "Let’s see who’s sent me some love."

        jump buildamayamessagemenu

    else:
        "Unfortunately, it doesn’t look like I have any."
        "Maybe one day, someone will love me enough to send me an email."
        "{i}Sigh.{/i}"

        jump buildamayacomputermenu

    menu buildamayamessagemenu:
        "Noriko" if buildamayanoriko == True:
            s "Let’s see what Noriko’s sent me."

            scene flowertimenorikopc1
            with dissolve

            "I click on her invisible message and bring up the first of two image attachments."
            "Her voice subsequently plays through the laptop’s speakers."

            n "Good afternoon, [norikomaster]. I have decided to send you a picture of my vagina as thanks for the snapdragon bracelet you gave me."
            n "I apologize if you opened this message in public. But I am also happy knowing that anyone who may have seen this now knows that I am yours."
            n "If you would rather masturbate to my breasts, I have enclosed a picture of them as well."
            n "Please click one more time to advance this message and see them."

            s "Heck yeah."

            scene flowertimenorikopc2
            with dissolve

            "I click again and make the boobs happen."

            n "As you can see, my nipples are hard. The reason for this is I am thinking about your penis and how it would feel if you were to insert it inside of my vagina (pictured in image #1). "
            n "I hope that when you are done reassembling Maya, we can have sex again. I enjoy having sex with you. "
            n "Please note that you may also print this picture out and ejaculate onto it in lieu of my physical presence. "
            n "I love you. Goodbye."

            play sound "computeryay.mp3"
            scene flowertime11

            "The boobs go away before I can finish masturbating. "
            "I decide to start my decision cycle over."

            jump buildamayacomputermenu

        "Futaba" if buildamayafutaba == True:
            s "Let’s see what Futaba’s sent me."

            scene flowertimefutabapc1
            with dissolve

            "I click on her invisible message and bring up the first of two image attachments."
            "Her voice subsequently plays through the laptop’s speakers."

            f "Good afternoon, [futabamaster]. I have decided to send you a picture of my vagina as thanks for the rose bouquet you gave me."
            f "I also apologize for my earlier explosion on the beach. I am cured now. And I am ready to be fucked again."
            f "If you would rather masturbate to my breasts, I have enclosed a picture of them as well."
            f "Please click one more time to advance this message and see them."

            s "Heck yeah."

            scene flowertimefutabapc2
            with dissolve

            "I click again and make the boobs happen."

            f "I apologize for my size as I know I am much larger than the rest of the girls in our class and that you are not a good man."
            f "However, I hope that when you are done reassembling Maya, we can have sex again. Your penis makes my vagina feel good and I enjoy when it is in there."
            f "Please note that you may also print this picture out and ejaculate onto it in lieu of my physical presence. "
            f "I love you. Goodbye."

            play sound "computeryay.mp3"
            scene flowertime11

            "The boobs go away before I can finish masturbating. "
            "I decide to start my decision cycle over."

            jump buildamayacomputermenu

        "Sana" if buildamayasana == True:
            s "Let’s see what Sana’s sent me."

            scene flowertimesanapc1
            with dissolve

            "I click on her invisible message and bring up the first of two image attachments."
            "Her voice subsequently plays through the laptop’s speakers."

            sa "Good afternoon, [sanamaster]. I have decided to send you a picture of my vagina as thanks for the corpsecrown you gave me."
            sa "I am wearing it now. And I would like you to know that it increases my arousal when thinking of you by about 50%%. "
            sa "If you would rather masturbate to my breasts, or lack thereof, I have enclosed a picture of them as well."
            sa "Please click one more time to advance this message and see them."

            s "Heck yeah."

            scene flowertimesanapc2
            with dissolve

            "I click again and make the boobs happen."

            sa "As you can see, my nipples are hard. The reason for this is I am thinking about being raped. This is a thing I am interested in and potentially the reason I like you so much."
            sa "I hope that when you are done reassembling Maya, you will remember that I am slightly smaller than she is and fuck me instead."
            sa "Please note that you may also print this picture out and ejaculate onto it in lieu of my physical presence. "
            sa "I love you. Goodbye."

            play sound "computeryay.mp3"
            scene flowertime11

            "The boobs go away before I can finish masturbating."
            "I decide to start my decision cycle over."

            jump buildamayacomputermenu

        "Makoto" if buildamayamakoto == True:
            s "Let’s see what Makoto’s sent me."

            scene flowertimemakotopc1
            with dissolve

            "I click on her invisible message and bring up the first of two image attachments."
            "Her voice subsequently plays through the laptop’s speakers."

            mak "Good afternoon, [makotomaster]. I have decided to send you a picture of my vagina as thanks for all of the sticks that you gave me after I gave sticks to you."
            mak "I had no idea you would go to such lengths for me and I wish you would be this nice back in our world. Unfortunately, I will not remember any of this."
            mak "So, if you would rather masturbate to my breasts, I have enclosed a picture of them as well."
            mak "Please click one more time to advance this message and see them."

            s "Heck yeah."

            scene flowertimemakotopc2
            with dissolve

            "I click again and make the boobs happen."

            mak "As you can see, my nipples are hard. The reason for this is I have become desensitized to the idea of you sleeping with my classmates and I have access to your email account."
            mak "I see what they have sent you and I would like you to know that I hope you will have sex with me once you are done reassembling Maya."
            mak "Please note that you may also print this picture out and ejaculate onto it in lieu of my physical presence. "
            mak "I love you. And sticks. Goodbye."

            play sound "computeryay.mp3"
            scene flowertime11

            "The boobs go away before I can finish masturbating. "
            "I decide to start my decision cycle over."

            jump buildamayacomputermenu

        "Chika" if buildamayachika == True:
            s "Let’s see what Chika’s sent me."

            scene flowertimechikapc1
            with dissolve

            "I click on her invisible message and bring up the first of two image attachments."
            "Her voice subsequently plays through the laptop’s speakers."

            c "Good afternoon, [chikamaster]. I have decided to send you a picture of my vagina as thanks for the lavender perfume you gave me."
            c "It has effectively masked the pungent scent of sex that permeates the Spacy’s Summer Blast Savings event at the mall, leading me to a higher level of comfort."
            c "If you would rather masturbate to my breasts, I have enclosed a picture of them as well."
            c "Please click one more time to advance this message and see them."

            s "Heck yeah."

            scene flowertimechikapc2
            with dissolve

            "I click again and make the boobs happen."

            c "As you can see, my nipples are hard. The reason for this is that despite my new enjoyable perfume, there is still sex everywhere and I am watching it."
            c "I hope you will have sex with me once you are done reassembling Maya as I want to show all of these bitches how to really ride a dick."
            c "Please note that you may also print this picture out and ejaculate onto it in lieu of my physical presence. "
            c "I love you. Goodbye."

            play sound "computeryay.mp3"
            scene flowertime11

            "The boobs go away before I can finish masturbating. "
            "I decide to start my decision cycle over."

            jump buildamayacomputermenu

        "Yumi" if buildamayayumi == True:
            s "Let’s see what Yumi’s sent me."

            scene flowertimeyumipc1
            with dissolve

            "I click on her invisible message and bring up the first of two image attachments."
            "Her voice subsequently plays through the laptop’s speakers."

            y "WHAT’S UP DOUCHEBAG? THANKS FOR THE OPIUM. I’M HIGH AS FUCK."
            y "CHECK OUT THIS PICTURE OF MY VIRGIN PUSSY. BET YOU’RE GONNA JERK OFF TO IT, YOU FUCKING LOSER."
            y "HAHAHAHA. WANT TO SEE MY TITS TOO? I BET YOU FUCKING DO, ASSHOLE."
            y "CLICK AGAIN. YOU KNOW YOU WANT TO."

            s "Heck yeah."

            scene flowertimeyumipc2
            with dissolve

            "I click again and make the boobs happen."

            y "YOU AIN’T THE ONLY ONE WHO’S PACKIN’, DUDE. THIS IS WHAT I’VE GOT HIDDEN UNDER THAT FUCKIN’ SARASHI. FEAST YOUR EYES ON A REAL CHEST."
            y "ALSO, MY NIPPLES ARE ONLY HARD CAUSE IT’S SUDDENLY COLD OVER HERE. I AIN’T THINKIN’ ABOUT RIDING YOUR FAT COCK AT ALL, FUCKER."
            y "ANYWAY PRINT THIS OUT AND JERK OFF TO IT IF YOU WANT I GUESS."
            y "FUCK YOU. BYE."

            play sound "computeryay.mp3"
            scene flowertime11

            "The boobs go away before I can finish masturbating. "
            "I decide to start my decision cycle over."

            jump buildamayacomputermenu

    ##################################################
label buildamayanorikorealm:
    scene flowertimenoriko1
    with fade

    if buildamayanorikoseen == True:
        s "Noriko? Are you there? I want to talk to you again."

        scene flowertimenoriko2
        with dissolve

        n "Oh! Hey, Onii-chan! What’s up?"

        jump buildamayanorikomenu1

    else:
        "I somehow wind up inside of what seems to be an abandoned school with a sewage problem."
        "A faint sloshing can be heard from one of the stalls, so I call out to investigate."

        s "Who is doing all of that sloshing? Reveal yourself."

        scene flowertimenoriko2
        with dissolve2

        n "It is me! I am the slosher."
        s "Noriko? What are you doing here?"
        n "Mmm...I’m not really sure? Some little girl took me here while I was helping her find her mom and I just haven’t ever figured out how to leave."
        s "I mean...I could show you to the door?"
        n "Nah. I’ve kind of grown to like it here. It’s super dark and the acoustics in the bathroom are great. I even found a cool piece of Maya to keep me company."
        s "Oh, awesome. Can you give that to me, please?"
        n "No."
        s "What? Really? Why? You always do everything I tell you."
        n "I know! But the longer I hold onto this, the longer it takes for you to reassemble her and leave me behind again."
        s "I won’t leave you behind, Noriko. You smell nice and you’re very good at sex."
        n "Thanks! But Maya smells nice too and is probably even better than me at sex since she got a massive head start and has had a ton of practice."
        n "That could’ve been me, Sensei! Nee-chan would have been way less upset watching you fuck me if you just did it earlier. We might have even had a threesome by now."
        s "Noriko...just give me the Maya piece, please. I have a cool workbench now and I can make you something of equal or greater value."
        n "Hmm...well, what do you have in mind exactly? Because I {i}suppose{/i} I can part with a fragment of my rival’s body for the right price."
        s "I was kind of just hoping you’d tell me what you want. That’s way easier than guessing. Especially not really knowing what sort of value you’d place on Maya’s body."
        n "{i}Hah.{/i} Onii-chan, if you’re not even willing to guess, there’s no {i}way{/i} you have anything I need."
        n "I’ll tell you what. Take these. It’s not a piece of your girlfriend, but you {i}should{/i} be able to find some sort of use for them."

        play sound "winner.mp3"

        "{i}Sensei obtained {b}Poppy Seeds{/b}!{/i}"

        s "Do I look like a bagel to you?"
        n "Of course not! But it’s not like I have anything {i}else{/i} to give you. Well, apart from that piece of Maya. Like, I don’t even have clothes anymore."
        s "Ugh...fine. I’ll take your stupid poppy seeds."
        s "But when I come back, you better be willing to do business."
        n "Maybe! We’ll have to just wait and see."

        scene black
        with dissolve

        n "Bye, Onii-chan! Come back soon!"
        n "Oh! And avoid the third classroom on the left! There’s a strange entity in there you can’t find out about yet!"

        "I heed Noriko’s warning, having already met too many strange entities, and head back outside to regroup."
        "Where should I go now?"

        $ poppyseed = True
        $ buildamayanorikoseen = True

        jump buildamayagomenu

    menu buildamayanorikomenu1:
        "Propose a trade":
            s "I’d like to propose a trade."
            n "Sure! What do you have in mind?"

            jump buildamayanorikomenu2

        "Go back outside":
            s "Actually, on second thought, I’m just going to go home. I don’t think I have anything you want."
            n "Aww, man. That’s fine!"
            n "I’ll be here whenever you come back. Just make sure to call my name since I might be busy sloshing around."
            s "Sounds good. Later, Noriko."
            n "Bye, Onii-chan!"

            scene black
            with dissolve2

            "I head back outside to gather my thoughts and figure something else out."

            jump buildamayagomenu

    menu buildamayanorikomenu2:
        "Corpsecrown" if buildamayacrown == True:
            s "This cool crown I made out of a corpseflower for your Maya piece. What do you say?"
            n "{i}Sniff, sniff.{/i} Why does it smell so weird?"
            s "I think it’s just a corpseflower thing."
            n "And you want me to wear that on my head?"
            s "No. {i}You{/i} want to wear it on your head. And then give me a piece of Maya in exchange for it."
            n "Mmm...I don’t think so, Onii-chan. Sorry!"
            s "Damn it."

            jump buildamayanorikomenu2

        "Lavender perfume" if buildamayaperfume == True:
            s "Some perfume made out of lavender and mystery liquid for your Maya piece. What do you say?"
            n "Mystery liquid?"
            s "I found it in some jar Ami was holding onto."
            n "Can I smell it?"
            s "Of course."

            "I give her a quick spritz with the tester bottle of perfume I made as well, knowing that someone was bound to ask me for this."

            n "Ohhhh, I know what this is."
            s "Can you tell me? "
            n "I...probably shouldn’t. Sorry, Onii-chan!"
            n "I {i}do{/i} love it, but I think I’m looking for something else right now. Have any other offers?"
            s "Ugh. Damn it."

            jump buildamayanorikomenu2

        "Opium" if buildamayaopium == True:
            s "How about some opium? That should net me a piece of Maya, right?"
            n "Opium? Don’t tell me that’s what you turned my poppy seeds into?"
            s "Sure. I won’t tell you anything. Do we have a deal?"
            n "Onii-chan! I don’t want you to become a drug dealer! You’re supposed to be a good boy!"
            s "You have pushed me to this, Noriko. {i}I{/i} didn’t want to be a drug dealer either."
            n "Then quit! And make me a {i}new{/i} offer. I don’t want any opium."
            s "Ugh. You’re so difficult sometimes."

            jump buildamayanorikomenu2

        "Rose Bouquet" if buildamayabouquet == True:
            s "Would a nice bouquet of roses be enough to get that Maya piece off of your hands?"
            n "You just bought that from the gas station, didn’t you?"
            s "No! I grew the roses myself with some seeds I got from Chika. Then replaced all of the stems with some sticks I got from Makoto."
            n "That bouquet’s really gotten around then, huh?"
            s "Well...I guess. But-"
            n "Sorry, Onii-chan. I don’t want to think of Chika or Makoto every time I look at them. Do you have any other ideas?"
            s "Uhh...let me think."

            jump buildamayanorikomenu2

        "Snapdragon Bracelet" if buildamayabracelet == True:
            s "How about this cool bracelet I made out of sticks and snapdragons?"
            n "Oooh! Let me see, let me see!"

            "I hand Noriko the bracelet and she begins to inspect it. I think her eyes widen as well, but they’re currently censored and I can’t really tell."
            "Hey, cool. That rhymed."

            n "You made this yourself, Onii-chan? It’s really good!"
            s "They say snapdragons symbolize strength and grace. And no girl encompasses those traits better than you do, Noriko."
            n "Aww! That’s so sweet! I love it. "
            n "Plus, I kind of miss wearing accessories. Being naked all the time is a little boring. "
            s "Do we...have a deal then?"
            n "We have a deal!"

            $ mayapieces += 1
            $ buildamayabracelet = False
            $ buildamayanoriko = True

            if mayapieces == 2:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s torso{b}!{/i}"
            if mayapieces == 3:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s pelvis{b}!{/i}"
            if mayapieces == 4:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left arm{b}!{/i}"
            if mayapieces == 5:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right arm{b}!{/i}"
            if mayapieces == 6:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left leg{b}!{/i}"
            if mayapieces == 7:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right leg{b}!{/i}"

            s "Hell yeah. I’m so good at commerce."
            n "I’m kind of sad that you’re going to leave me again. But hey, at least I get a bracelet out of it this time. That’s more than Nee-chan can say."
            s "Are you just gonna hang out here? Or do you want to come back to my place and help me rebuild Maya?"
            n "I’ll stay here for now. Maybe we’ll meet again on the outside, though? If I ever decide to leave, that is."
            s "I hope you do, Noriko. Take care, okay?"
            n "You too, Onii-chan! Good luck with your crafts and stuff!"

            scene black
            with dissolve2

            "I leave Noriko and head back outside to figure out where to go from here."

            jump buildamayagomenu

        "Go back outside":
            s "Actually, on second thought, I’m just going to go home. I don’t think I have anything you want."
            n "Aww, man. That’s fine! "
            n "I’ll be here whenever you come back. Just make sure to call my name since I might be busy sloshing around."
            s "Sounds good. Later, Noriko."
            n "Bye, Onii-chan!"

            scene black
            with dissolve2

            "I head back outside to gather my thoughts and figure something else out."

            jump buildamayagomenu

    ##################################################
label buildamayafutabarealm:
    scene flowertimefutaba1
    with fade

    if buildamayafutabaseen == True:
        s "Futaba? Are you there? I want to talk to you again."

        scene flowertimefutaba2
        with dissolve

        f "Welcome back, Sensei. I’ve been waiting for you."
        f "Do you need something?"

        jump buildamayafutabamenu1

    else:
        "I suddenly find myself in a peculiar restaurant."
        "After waiting in a relatively long queue behind a number of elongated specters, I’m taken into the dining room to meet my server. "
        "And while the room {i}may{/i} look to the untrained eye like a library flipped on its head, the reality is that this is the best eatery in town."
        "Or at least it used to be. Lately, it’s been occupied by ghosts who can’t let go of the past. And this is where they come to pretend they haven’t grown up."

        scene flowertimefutaba2
        with dissolve2

        f "W-Welcome to the Cartographer’s Crab-Shack! I’m your server, Fu- Sensei?"
        s "Nice to meet you, Fu-Sensei. One cajun seafood boil, please. And for the drink, I’ll just have a water."
        f "Sensei, no. It’s me, Futaba."
        s "Oh, wow. It is. Sorry, I was just so entranced by the menu. There are so many options here."
        f "Only because we’re serving up anything you can imagine."
        s "Really? In that case, can I also have a side of one of Maya’s body parts?"
        f "Uhh...I guess I probably shouldn’t have said {i}anything{/i} you can imagine, huh?"
        s "Are you telling me I need to summon the manager?"
        f "I...actually {i}am{/i} the manager. "
        s "Woah, really? Congratulations. How’d that happen? You’re such a normal girl back home."
        f "Well, to me, this {i}is{/i} my home. I grew up in the corner right behind me. And while it took me a long time to come out of my shell, pun intended, I’m...doing kind of great now."
        s "So you don’t want to come back to our world? You want to stay here and serve imaginary crab to elongated specters?"
        f "There will always be a me somewhere else. And all of our memories are connected, so it’s kind of like I’m everywhere at once."
        s "Weird. I wonder if it’s the same for all of the other girls?"
        f "Probably. It’s been a long time since I’ve seen any of them, though."
        f "Ever since the remainders of Maya were scattered across the land, we’ve all sort of lost touch."
        s "Wait. Are you saying that a piece of her {i}can{/i} be found here after all?"
        f "Oh, yes. You just can’t order it like an appetizer. {i}These{/i} are your appetizers."

        play sound "winner.mp3"

        "{i}Sensei obtained {b}Lavender Seeds{/b}!{/i}"

        s "Lavender seeds?"
        f "Wow, Sensei. Your seed identification skills are very impressive. Only an expert could decipher what type of seeds those are just by looking at them."
        s "I’m supposed to eat them?"
        f "Or hold on to them, if you’d prefer. They might even grow into something else if you care for them enough."
        s "Lavender, I’d assume."
        f "That would make sense, yeah."
        s "How do I get the piece of Maya then?"
        f "Well, imaginary or not, this is still a business. Which means there will be some sort of transaction involved."
        f "The only issue is I have very specific tastes and not just any old item will suffice. I’m sure you’ll figure out what I want in no time at all, though."
        s "I hope so. That Maya back home isn’t going to build itself. Can I just come back whenever I want then?"
        f "Mhm. Just call out for me once you do. This isn’t a real restaurant, so you aren’t going to disturb any customers."
        f "Oh, and if you see other girls that look just like me around here, they’re also me. You can sleep with all of them and I won’t get upset."
        s "Sorry. No sex for me in here, Futaba. I’ve got a job to do."

        scene black
        with dissolve

        s "In fact, I should probably get back to that now if you’re not going to just hand over your fragment of Maya."
        f "Okay! It was nice seeing you, though. Feel free to come back whenever you’re ready to do business. And remember-"
        s "Unlimited Futaba sex. I know."
        f "Oh, no. I was talking about the “calling out to me” part."
        s "Oh, yeah. I’ll remember that too. Later, Futaba."
        f "Bye, Sensei!"
        f "Until we meet again..."

        "I pay my imaginary bill and exit the Cartographer’s Crab-Shack."
        "What do I want to do now?"

        $ lavenderseed = True
        $ buildamayafutabaseen = True

        jump buildamayagomenu

    menu buildamayafutabamenu1:
        "Propose a trade":
            s "I’d like to propose a trade. "
            f "Sure. What do you have in mind?"

            jump buildamayafutabamenu2

        "Go back outside":
            s "On second thought, I don’t think I have anything you’d want. I’ll come back later, once I do."
            f "Sure. I’ll be here. Bye, Sensei."
            s "Later, Fu-Sensei."
            f "Can you...please stop calling me that?"

            scene black
            with dissolve2

            "I head back outside to gather my thoughts and figure something else out."

            jump buildamayagomenu

    menu buildamayafutabamenu2:
        "Corpsecrown" if buildamayacrown == True:
            s "So I made this crown of corpseflowers that I think would look great on you."
            f "Oooh...yeah, I don’t think I should wear that. One of the specters told me some pretty bad rumors about those things."
            s "Probably so he can make his own off-brand versions and peddle them to your coworkers. This one here’s the real deal, Futaba. This thing smells like so many corpses."
            f "Yeah, see, that’s another reason I don’t really want it. "
            f "Do you have anything else?"
            s "Uhh...let me see."

            jump buildamayafutabamenu2

        "Lavender perfume" if buildamayaperfume == True:
            s "How about this lavender perfume I made out of the seeds you gave me?"
            f "I already have some lavender-scented perfume, but maybe yours is nicer? Can you tell me what’s in it?"
            s "Like, specifically? Or vaguely?"
            f "Well...{i}you{/i} made it, didn’t you? So whatever you put it into it."
            s "Lavender."
            f "..."
            f "And?"
            s "Some mystery fluid from a jar in Ami’s room."
            f "..."
            s "Cool, right?"
            f "I think I’m good on perfume right now, actually."
            s "Damn it. What else do I have?"

            jump buildamayafutabamenu2

        "Opium" if buildamayaopium == True:
            s "You look like the kind of girl who likes to have a good time. How about some opium to {i}really{/i} get this party started?"
            f "Your personality has taken a pretty dark shift since Maya was decapitated, huh?"
            s "I’m just trying to get by, Futaba. And sometimes, {i}getting by{/i} means selling opium in exchange for body parts. You know the hustle, right?"
            f "Like, the dance? I don’t think I’m old enough to-"
            s "No, like the {i}hustle.{/i} The struggle. What people like me have to do to get by."
            f "Oooooohhhhh..."
            f "Yeah, no. I don’t know that. And I don’t really want any drugs either, so..."
            s "Tch. Fine. Let’s see what else I have."

            jump buildamayafutabamenu2

        "Rose Bouquet" if buildamayabouquet == True:
            s "I think you’d really like this, Futaba. Look."

            "I give Futaba the bouquet of roses, which she grabs with both hands and subsequently cuts her palms on thanks to the artificial, stick-based thorns I included."
            "The blood drips down her wrists like ice cream off a melting cone, connecting with the floor similarly to the way in which melted ice cream would connect with the same floor if it also did that."

            f "They’re beautiful...where did you get this?"
            s "I grew them myself with some seeds Chika gave me. "
            f "And you’re...giving the bouquet to me instead of Chika? Why?"
            s "Well, roses are a symbol of love or something, aren’t they?"
            f "I repeat — why are you giving this to {i}me{/i} instead of Chika? Or...literally anyone else. You don’t {i}love{/i} me."
            s "But I will one day. And until then, these roses will serve as a symbol of that. "
            s "Plus, I replaced the stems with sticks, so they’ll live forever and you won’t need to water them."
            f "Does it really work like that?"
            s "I don’t know. Maybe?"
            f "{i}Hah...{/i}I still don’t think I’m deserving of this, but...I {i}do{/i} like them. And...I know you really want to put Maya back together, so..."
            f "Here."

            $ mayapieces += 1
            $ buildamayafutaba = True
            $ buildamayabouquet = False

            if mayapieces == 2:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s torso{b}!{/i}"
            if mayapieces == 3:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s pelvis{b}!{/i}"
            if mayapieces == 4:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left arm{b}!{/i}"
            if mayapieces == 5:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right arm{b}!{/i}"
            if mayapieces == 6:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left leg{b}!{/i}"
            if mayapieces == 7:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right leg{b}!{/i}"

            f "Now you’re one piece closer to having a whole girl."
            s "I sure am. Thanks a lot, Futaba. I’m glad to have you as my business partner."
            f "You have me as much more than that, Sensei. Or...at least you {i}could{/i} if you only wanted to."
            s "..."
            f "..."
            s "..."
            f "........"
            s "Good to know. Later, then. I have to go  assemble a teenager."

            scene black
            with dissolve2

            f "{i}Hah...{/i}Goodbye, Sensei."
            f "Thanks again for coming to the Cartographer’s Crab-Shack."

            "I leave Futaba and head back outside to figure out where to go from here."

            jump buildamayagomenu

        "Snapdragon Bracelet" if buildamayabracelet == True:
            s "How about this nice little bracelet I made out of snapdragons?"
            f "I’m allergic to snapdragons."
            s "What? Is that even possible?"
            f "Well, I don’t know if it’s technically {i}allergies,{/i} but I start to panic whenever I’m near them. "
            s "What if I just try to put it on your wrist like-"
            f "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-"
            s "Oh, okay. Never mind."
            f "Sorry. Do you have anything else?"
            s "Uhh...let me see."

            jump buildamayafutabamenu2

        "Go back outside":
            s "On second thought, I don’t think I have anything you’d want. I’ll come back later, once I do."
            f "Sure. I’ll be here. Bye, Sensei."
            s "Later, Fu-Sensei."
            f "Can you...please stop calling me that?"

            scene black
            with dissolve2

            "I head back outside to gather my thoughts and figure something else out."

            jump buildamayagomenu
    ##################################################
label buildamayasanarealm:
    scene flowertimesana1
    with fade

    if buildamayasanaseen == True:
        s "Sana? Are you there? I want to talk to you again."

        scene flowertimesana2
        with dissolve

        sa "Mhm...Welcome back, Sensei..."
        sa "Do you...need something?"

        jump buildamayasanamenu1

    else:
        "I arrive at a beach that could use some bleach, but I won’t let that deter me from having a good time. "
        "I just don’t like the fact that I can {i}tell{/i} the time at all as places like this are meant to be an escape from that."
        "Yet a clock hangs high upon a wall painted to resemble the sky, towering precariously over my desire for leisure and and even more hidden desire to drown myself in the ocean."
        "At least then I’d be able to escape the humidity from the world’s largest indoor pool."

        scene flowertimesana2
        with dissolve2

        sa "Hi..."
        s "Oh. Sana. I didn’t expect to see you here. You don’t seem like much of a beach person."
        sa "One could say the same for you, Sensei...but the truth is I’ve already met you here once before."
        s "What? When?"
        sa "You were younger...I was not...and you rejected my advances, but..."
        sa "You won’t do that anymore, will you?..."
        s "Well...uh..."
        sa "Because my brother is here too and I think it’d be really hot if you guys, like...restrained me and filled both of my holes at the same time."
        s "That’s not really what I had in mind when coming here. I’m glad to hear he’s doing okay, though."
        sa "He doesn’t move anymore, but it seems like bodies don’t really decay in here. I think it must be due to the humidity. "
        s "Ahh, so you were just going to make me do all of the restraining myself while you humped your brother’s corpse."
        sa "And you. You’d get a turn too. Don’t make me out to be weird because of that, though. You’re doing the same thing by trying to reassemble Maya, aren’t you?"
        s "I’m reassembling Maya so I can bring her back home. Not so I can have sex with her."
        sa "Suuuuuuuuuuuuuure..."
        s "I’m {i}serious,{/i} Sana."
        sa "Suuuuuuuuuuuuuuuuuuuuuuuuuuure..."
        s "Sana."
        sa "I get it, Sensei. You’re only going to use her body for {i}wholesome{/i} purposes. I {i}completely{/i} understand."
        s "Stop winking at me. I don’t like it."
        sa "Sorry...it’s just been a while since I’ve seen anything move..."
        sa "Even the water is completely still. And the hands on the clock are stuck, so...I sort of just wander around and look for things to hump..."
        s "I get it. I did the same when I first came to Kumon-mi."
        sa "Ah! Kumon-mi! I remember that place..."
        sa "Wow, it’s been so long..."
        s "Do you have any desire to go back? I can probably take you with me, you know. "
        sa "And leave Shota behind? I can’t do that, Sensei."
        s "Isn’t he dead?"
        sa "Yeah. But in a sense, aren’t we all?"
        sa "If time won’t move and {i}we{/i} won’t change, we’re all just walking corpses."
        sa "Which reminds me-"

        play sound "winner.mp3"

        "{i}Sensei obtained a {b}Corpseflower Seed{/b}!{/i}"

        s "What is this?"
        sa "A seed that’ll help you grow a corpseflower. Something to remember me by when you finish building your Maya and stop coming to see me."
        s "Fortunately for you, I still have some pieces to collect. So we can keep hanging out for a little while."
        s "And if you just so happen to have a piece of her-"
        sa "Hump it?"
        s "What? No. Give it to me."
        sa "So {i}you{/i} can hump it?"
        s "Sana, not everything has to be about sex."
        sa "You’ve changed, Sensei...I’m finally more like you and now you’re just pushing me away."
        sa "I’ll never give you my piece of Maya at this rate."
        s "Then you leave me no choice but to make you something you won’t be able to say no to."
        sa "Nobody can say no if you just cover their mouth with your hand. "

        scene black
        with dissolve

        s "And, on that note, I am leaving."
        sa "Okay...but you’ll know where to find me if you need to let off some steam."
        sa "Shotaaaaa! Where are- oh, right. You can’t move. "

        "I leave Sana behind at the Unbleached Beach and figure out where to go from here..."

        $ corpseseed = True
        $ buildamayasanaseen = True

        jump buildamayagomenu

    menu buildamayasanamenu1:
        "Propose a trade":
            s "I’d like to propose a trade. "
            sa "Um...okay...What kind of trade?..."

            jump buildamayasanamenu2

        "Go back outside":
            s "Actually, I think I’d rather go back outside and try and find something else for you. I know you won’t let go of your Maya fragment easily."
            sa "Heheh...you’ve got that right..."
            sa "Come back when you have something for me..."

            scene black
            with dissolve2

            "I head back outside to gather my thoughts and figure something else out."

            jump buildamayagomenu

    menu buildamayasanamenu2:
        "Corpsecrown" if buildamayacrown == True:
            "I remove the corpsecrown from my inventory and immediately capture Sana’s attention."

            sa "That’s..."
            s "I made it out of the seed you gave me. It was a little difficult cutting it down to a size that could fit a crown, but I think the end result is pretty good."
            sa "..."
            s "Do you like it?"
            sa "..."
            s "Do you...want to try it on?"
            sa "..."
            sa "Can I?..."
            s "Of course. Here you go."

            "I hand the corpsecrown over to Sana, who then places it over her head with trembling fingers, gazing up at the splintering wood I used to make it as if it’s meant to hold her skull in place."
            "Her gaze is trapped there for a moment before it shoots to me. And then to nothing."
            "Her eyes glaze over and develop a fine blue film over them that makes it appear as if she is a snake about to shed its skin."
            "Her mouth drops open, emitting a low hum as the crown settles into her."

            s "Cool right?"
            sa "{size=-10}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhh...{/size}"
            s "I...take it we have a deal, then?"
            sa "{size=-10}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhh!!!{/size}"

            $ mayapieces += 1
            $ buildamayasana = True
            $ buildamayacrown = False

            if mayapieces == 2:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s torso{b}!{/i}"
            if mayapieces == 3:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s pelvis{b}!{/i}"
            if mayapieces == 4:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left arm{b}!{/i}"
            if mayapieces == 5:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right arm{b}!{/i}"
            if mayapieces == 6:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left leg{b}!{/i}"
            if mayapieces == 7:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right leg{b}!{/i}"

            s "Awesome. Thanks, Sana. "
            sa "{size=-10}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhh?????{/size}"
            s "Right. Well, I’ll see you later then."
            sa "{size=-10}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhh!?!?!?&&!?!?!!?!@@!!{/size}"

            scene black
            with dissolve2

            "I leave Sana and head back outside to figure out where to go from here."

            jump buildamayagomenu

        "Lavender perfume" if buildamayaperfume == True:
            s "How about some lavender perfume? It smells like-"
            sa "No."
            s "You didn’t even let me finish. It smells like lavender."
            sa "I don’t want to smell like lavender...I want to smell like dried cum and sweat..."
            s "Ew. "
            sa "Just...personal preference, I guess...it makes me feel more human and less artificial..."
            sa "It’s something you have to work for rather than something that comes from a bottle..."
            s "Would it help knowing the perfume has a special mystery fluid I found in Ami’s room?"
            sa "Can I drink it?"
            s "Uh...probably not?"
            sa "Mm...I think I’ll pass then, Sensei..."
            sa "Do you have any other offers?"
            s "Uhh...hold on. Let me see."

            jump buildamayasanamenu2

        "Opium" if buildamayaopium == True:
            s "How about some opium? It might take your necrophilia to the next level."
            sa "It also might impact my thinking...and I’m the type who enjoys being fully immersed in my actions, Sensei...even when they’re actions I haven’t chosen for myself."
            s "I don’t get it."
            sa "Like...if someone chooses what to do with me and doesn’t give me any say in it...I still want to experience it all...even if I {i}hate{/i} it."
            s "Still don’t get it."
            sa "Oh..."
            sa "Have you been taking the opium too? I think I’d...be more open to it if we did it together..."
            s "Me? No. I need to be completely lucid for when I reassemble Maya. If I put a single part where it doesn’t belong, she might never be able to walk in the correct direction again."
            sa "I guess I have to...refuse your offer, then..."
            sa "But if you have something else...I’d be happy to hear it?"

            jump buildamayasanamenu2

        "Rose Bouquet" if buildamayabouquet == True:
            s "How about a nice bouquet of roses to show you how much I care?"
            sa "Roses?...What am I supposed to do with those?..."
            sa "You can’t hump a rose...it’ll break..."
            s "It’s not about the humping. It’s about having a physical representation of my feelings for you."
            sa "Can you...not just use the “physical representation” that’s dangling there between your legs?..."
            s "I could. But it feels wrong to receive a piece of Maya in exchange for my body when hers is so much better."
            sa "You know mine...isn’t that much different, right?..."
            s "Your ribs are slightly more visible. You need to eat more."
            sa "Then feed me, Sensei...{i}feed me...{/i}"
            sa "Fill me up with your love..."

            "Looks like Sana doesn’t want roses. I’ll have to try something else."

            jump buildamayasanamenu2

        "Snapdragon Bracelet" if buildamayabracelet == True:
            s "How about a snapdragon bracelet? I made it myself."
            sa "Would someone...really trade you a body part for this?..."
            sa "Appendages alone go for a few thousand on the black market...I could get a bracelet from a vending machine for around 100 yen..."
            s "Is it not the thought that counts to you? I worked hard on this."
            sa "I don’t...really care {i}how{/i} hard you worked..."
            sa "If I’m going to give up my piece of Maya, I need something of equal or greater value...a tiny bracelet just...isn’t that, Sensei..."
            s "Damn it. Let’s see what else I have."

            jump buildamayasanamenu2

        "Go back outside":
            s "Actually, I think I’d rather go back outside and try and find something else for you. I know you won’t let go of your Maya fragment easily."
            sa "Heheh...you’ve got that right..."
            sa "Come back when you have something for me..."

            scene black
            with dissolve2

            "I head back outside to gather my thoughts and figure something else out."

            jump buildamayagomenu
    ##################################################
label buildamayamakotorealm:
    if buildamayamakotoseen == True and buildamayaq10 == True:
        jump buildamayaallquestionsdone

    scene flowertimemakoto1
    with fade

    if buildamayamakotoseen == True and buildamayaq10 == False:
        s "Makoto? Are you there? I want to talk to you again."

        scene flowertimemakoto2
        with dissolve

        mak "Oh, Sensei. Welcome back. "
        mak "Are you here to try and earn some sticks?"
        s "You know it. "
        s "Let’s hear some riddles, Makoto. It’s time to knock your socks off."

        jump buildamayamakotoquestions

    else:
        "I arrive at what looks like the remnants of a children’s television show set, but there’s a plaque near the door referring to this building as the “Smile Mile.”"
        "It smells faintly of peppermint and there’s a light green mist bleeding in through the vents that I’m not sure what to make of. I don’t think the scent is coming from that."
        "I don’t really care either way, though. And if I need to deal with a little green mist to uncover a piece of Maya’s body, so be-"

        mak "Sensei? Is that you?"

        scene flowertimemakoto2
        with dissolve2

        s "Makoto? How’d you get into the Smile Mile? I hopped like seven fences to make it inside of here and there’s no way you’re that athletic."
        mak "I was invited by a good friend of mine. I assumed that the two of you may have already been acquainted, but that doesn’t seem to be the case."
        mak "Are you looking for something?"
        s "Yeah. I have Maya’s head in a bag, but I need to collect the rest of her to-"
        mak "Say no more. Here."

        $ mayapieces += 1

        if mayapieces == 2:
            play sound "winner.mp3"
            "{i}Sensei obtained {b}Maya’s torso{b}!{/i}"
        if mayapieces == 3:
            play sound "winner.mp3"
            "{i}Sensei obtained {b}Maya’s pelvis{b}!{/i}"
        if mayapieces == 4:
            play sound "winner.mp3"
            "{i}Sensei obtained {b}Maya’s left arm{b}!{/i}"
        if mayapieces == 5:
            play sound "winner.mp3"
            "{i}Sensei obtained {b}Maya’s right arm{b}!{/i}"
        if mayapieces == 6:
            play sound "winner.mp3"
            "{i}Sensei obtained {b}Maya’s left leg{b}!{/i}"
        if mayapieces == 7:
            play sound "winner.mp3"
            "{i}Sensei obtained {b}Maya’s right leg{b}!{/i}"

        s "Woah, really? Just like that?"
        mak "Of course. What use do {i}I{/i} have for Maya’s body?"
        mak "I was actually holding onto that in hopes that you’d show up. You seemed pretty distraught when you opened that box from Ami."
        s "What box? I’m not allowed to open boxes. The game doesn’t let me."
        mak "Ahh, I see. You haven’t grown your reset legs yet. That might make this next part difficult then."
        s "Next part? What next part? Are you holding out on me, Makoto? Do you have more body parts back there?"
        mak "No more body parts, unfortunately. But I {i}do{/i} have a large collection of sticks that you could probably find something to do with."
        s "Sorry. Sticks? What am I supposed to do with sticks?"
        mak "You could use them as some sort of crafting reagent, I suppose? Or perhaps there’s just someone else out there who’s really interested in sticks? I don’t know."
        s "I mean, I can {i}try.{/i} Hand them over and I’ll see what I can-"
        mak "Ah! Not so fast, Sensei. That piece of Maya may have been on the house, but these sticks are a lot more valuable than that."
        mak "I’m {i}still{/i} willing to let go of them for free, of course. No one wants you to succeed more than I do. But I need to know that you’re serious about escaping this time."
        s "Do you see this face, Makoto? This is my serious face. I am {i}so{/i} serious right now. Give me the sticks."
        mak "I can’t, Sensei. I need you to prove {i}how{/i} serious you are by showing me how much attention you’ve been paying. So I’ve prepared a handful of riddles."
        s "Ughhhhhh! I {i}knew{/i} there’d be questions again. I hate paying attention."
        mak "Thankfully, you should only need about half of them to achieve your goal. And you can guess as many times as you like. Does that work for you, Sensei?"
        s "I mean...it’s better than nothing, I guess."

        $ buildamayamakotoseen = True

        jump buildamayamakotoquestions

label buildamayamakotoquestions:
    mak "Excellent! Let’s start now then."

    if buildamayaq1 == False:
        jump buildamayaquestion1
    if buildamayaq2 == False:
        jump buildamayaquestion2
    if buildamayaq3 == False:
        jump buildamayaquestion3
    if buildamayaq4 == False:
        jump buildamayaquestion4
    if buildamayaq5 == False:
        jump buildamayaquestion5
    if buildamayaq6 == False:
        jump buildamayaquestion6
    if buildamayaq7 == False:
        jump buildamayaquestion7
    if buildamayaq8 == False:
        jump buildamayaquestion8
    if buildamayaq9 == False:
        jump buildamayaquestion9
    if buildamayaq10 == False:
        jump buildamayaquestion10
    elif buildamayaq10 == True:
        jump buildamayaallquestionsdone

label buildamayaquestion1:
    mak "Be it torture or torment, whatever you need, there’s a White Princess waiting to swallow your seed."
    mak "Countless spidersilk hammocks she happily weaves, laced with infinite toxins you shan’t ever leave."
    mak "What is Her name?"

    $ buildamayaquiz1 = renpy.input("Her name is...")
    $ buildamayaquiz1 = buildamayaquiz1.strip()
    if buildamayaquiz1.lower() in ["gossamer"]:
        s "Gossamer, God of Torment! "

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq1 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "I knew you had it in you. Now just replicate that success nine more times and you’ll have aced my quiz!"
        s "It’s so lame that you’re being a smart girl here in brain-vacation."
        mak "You’ll thank me later, I’m sure. "
        mak "Are you ready for the next question?"

        menu:
            "Yes":
                s "Hell yeah, Makoto. Hit me."
                jump buildamayaquestion2

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz1]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion1

            "No":
                s "I think I’m good for now. I’ll come back when I need some sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion2:
    mak "If you ever feel sad and forget how to smile, abandon your fears and rest here for a while."
    mak "A man with five heads but only four faces. Just don’t make him mad, for it’s air he displaces."
    mak "What is His name?"

    $ buildamayaquiz2 = renpy.input("His name is...")
    $ buildamayaquiz2 = buildamayaquiz2.strip()
    if buildamayaquiz2.lower() in ["giuseppe"]:
        s "Giuseppe, God of Clowns!"

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq2 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "You’re doing great. Just eight questions remain now."
        mak "Are you ready for the next one?"

        menu:
            "Yes":
                s "Hell yeah, Makoto. Hit me."
                jump buildamayaquestion3

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz2]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion2

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion3:
    mak "A cage for your heart and the things you’ve done wrong. Four ears to remember the words of each song."
    mak "A chance for a wish to fulfill your ambitions. Your misdeeds mean nothing if he says you’re forgiven."
    mak "What is His name?"

    $ buildamayaquiz3 = renpy.input("His name is...")
    $ buildamayaquiz3 = buildamayaquiz3.strip()
    if buildamayaquiz3.lower() in ["pegasus"]:
        s "Pegasus, Peerless God of Forgiveness! "

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq3 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "You’re doing great. Only seven questions left."
        mak "Are you ready for the next one?"

        menu:
            "Yes":
                s "Hell yeah, Makoto. Hit me."
                jump buildamayaquestion4

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz3]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion3

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion4:
    mak "If the world is a game, then there must be a master. Or at least someone who will keep track."
    mak "On the wings of white noise, he can play what comes after a choice you can’t ever take back."
    mak "What is His name?"

    $ buildamayaquiz4 = renpy.input("His name is...")
    $ buildamayaquiz4 = buildamayaquiz4.strip()
    if buildamayaquiz4.lower() in ["halftone"]:
        s "Halftone, God of Save Slots! "

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq4 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "You’re doing awesome! You’re almost halfway done now."
        mak "Are you ready for the next one?"

        menu:
            "Yes":
                s "Hell yeah, Makoto. Hit me."
                jump buildamayaquestion5

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz4]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion4

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion5:
    mak "In a room full of children who don’t dare to tempt you, there’s a bed that you wouldn’t dare sleep in."
    mak "Its caregiver cares not for what you have gone through, but she’ll watch as the plot you’re in deepens."
    mak "What is Her name?"

    $ buildamayaquiz5 = renpy.input("Her name is...")
    $ buildamayaquiz5 = buildamayaquiz5.strip()
    if buildamayaquiz5.lower() in ["floral laura"]:
        s "Floral Laura, God of the Hedgemaze! "

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq5 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "You’re officially halfway done!"
        mak "I’ve gotta say, I’m really impressed. I had no idea you’d make this far."
        mak "Do you want to keep going?"

        menu:
            "Yes":
                s "Hell yeah, Makoto. Hit me."
                jump buildamayaquestion6

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz5]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion5

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion6:
    mak "Lacerations for you and badges for me. You might think that you’re strong, but she’s stronger."
    mak "As of now she’s just hearsay and hasn’t been seen. Just a scepter could make your arms longer."
    mak "What is Her name?"

    $ buildamayaquiz6 = renpy.input("Her name is...")
    $ buildamayaquiz6 = buildamayaquiz6.strip()
    if buildamayaquiz6.lower() in ["necalli"]:
        s "Necalli, God of Knives! "

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq6 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "You’ve officially entered the more difficult half of the quiz."
        mak "Think you still have what it takes to keep going?"

        menu:
            "Yes":
                s "Hell yeah, Makoto. Keep ‘em coming."
                jump buildamayaquestion7

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz6]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion6

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion7:
    mak "Summer, winter, autumn, spring — each is perfect for the Fruit Fly’s Wing."
    mak "Often a perched on a desk with no place to sit, he once carved his home in the Heavenly Pit."
    mak "What is His name?"

    $ buildamayaquiz7 = renpy.input("His name is...")
    $ buildamayaquiz7 = buildamayaquiz7.strip()
    if buildamayaquiz7.lower() in ["onund"]:
        s "Onund, God of the Hole! "

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq7 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "Only three questions left now. You’re doing so well!"
        mak "Ready for the next one?"

        menu:
            "Yes":
                s "Hell yeah, Makoto. Keep ‘em coming."
                jump buildamayaquestion8

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz7]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion7

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion8:
    mak "How nice it would be to sleep in her bosom, dodging claws or the cords in her hair."
    mak "For when I wake up and the sun starts to shine, a glass of her warmth is already prepared."
    mak "What is Her name?"

    $ buildamayaquiz8 = renpy.input("Her name is...")
    $ buildamayaquiz8 = buildamayaquiz8.strip()
    if buildamayaquiz8.lower() in ["harimanti"]:
        s "Harimanti, God of Milk! "

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq8 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "Two more! You’re better than anyone could have ever imagined!"
        mak "Ready for the next one?"

        menu:
            "Yes":
                s "Hell yeah, Makoto. Keep ‘em coming."
                jump buildamayaquestion9

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz8]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion8

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion9:
    mak "This one might be tough as he’s still up and coming."
    mak "I now speak of the god who rules one more than nothing."
    mak "What is His name?"

    $ buildamayaquiz9 = renpy.input("His name is...")
    $ buildamayaquiz9 = buildamayaquiz9.strip()
    if buildamayaquiz9.lower() in ["arramin"]:
        s "Arramin, God of Something! "

        play sound "computeryay.mp3"

        mak "Great work, Sensei!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq9 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "I can’t believe it! There’s only one question left!"
        mak "Are you ready, Sensei? Can you complete the quiz?"

        menu:
            "Yes":
                s "Let’s fucking do this..."
                jump buildamayaquestion10

            "No":
                s "I think I’m good for now. I’ll come back when I need more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready for more."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

    else:
        s "[buildamayaquiz9]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "Shoot. I thought I had that one."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion9

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Okay! I’ll be here. Just call out to me and tell me you’re ready."
                s "Thanks, Makoto. You’re the best."

                scene black
                with dissolve2

                "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaquestion10:
    mak "A creator of many, yet a peer of no one. If you call him a clown, you’re a bother."
    mak "His domain is familiar. His power is unmatched. He’s the one we call Sorrowful Father."
    mak "What is His name?"

    $ buildamayaquiz10 = renpy.input("His name is...")
    $ buildamayaquiz10 = buildamayaquiz10.strip()
    if buildamayaquiz10.lower() in ["apollo"]:
        s "Apollo, Peerless God of Dolor! "

        play sound "computeryay.mp3"

        mak "Oh my {b}GOD!{/b} You did it!"

        play sound "winner.mp3"

        $ sticks += 1
        $ buildamayaq10 = True

        "{i}Sensei has obtained {b}a stick{/b}!{/i}"

        mak "That’s amazing! You answered every single question correctly!"
        s "I have so many sticks now."
        mak "You sure do. But unfortunately, that means I don’t have {i}any{/i} anymore. And that’s kind of upsetting."
        mak "I’ve grown pretty attached to those sticks lately."
        s "If it makes you feel any better, they’ll all be going to a good cause. "
        mak "I believe you, Sensei. I know you’ll complete your rebuild of Maya any day now. And when you do, I hope to be right there on the other side when you return to our world."
        s "It’ll probably be Ayane."
        mak "Yeah, you’re probably right."
        s "Either way, Makoto, you’ve been a huge help. I need to go put these sticks to work, though. I refuse to let you down this time."
        mak "I’ll hold you to that, Sensei..."

        scene black
        with dissolve2

        mak "Good luck out there."

        "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
        "The place that I’ll go next is-"

        jump buildamayagomenu

    else:
        s "[buildamayaquiz10]!"

        play sound "computerboo.mp3"

        mak "I’m sorry, Sensei. That’s incorrect."
        s "God, this shit is so hard."
        mak "Do you want to try again?"

        menu:
            "Yes":
                s "Fuck it. Yeah. Ask me again."
                jump buildamayaquestion10

            "No":
                s "I think I’m good for now. I’ll come back when I need some more sticks, though."
                mak "Really? You’re just...going to leave in the middle of the very last question?"
                s "Damn right."

                scene black
                with dissolve2

                mak "Sensei, no! Come back! You can’t just leave me in suspense like this!"

                "I sure can. So I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
                "The place that I’ll go next is-"

                jump buildamayagomenu

label buildamayaallquestionsdone:
    scene flowertimemakoto1
    with fade

    s "Makoto? Are you there? I want to talk to you again."

    scene flowertimemakoto2
    with dissolve

    mak "Sensei?..."
    mak "What are you doing here? You’ve already answered all of my questions."

    if buildamayaultimate == True:
        s "I wanted to give you this."

        play sound "winner.mp3"

        "{i}Sensei has gifted the {b}Ultimate Stick Bouquet{/b} to Makoto!{/i}"

        mak "Wha-"
        s "I had some extra sticks left over after making a bunch of trinkets and I figured I’d craft something for {i}you{/i} as a means of thanking you for all of your help."
        s "I’d be stuck in here forever if it wasn’t for you, Makoto."
        mak "My sticks..."
        mak "They’re so beautiful now..."
        s "Perhaps they’ve {i}always{/i} been beautiful...and we just couldn’t see it."
        mak "Sensei, I...I know they’re just {i}sticks,{/i} but...this really means a lot to me. "
        mak "To think that you’d learn how to make the {b}Ultimate Stick Bouquet{/b} in such a short amount of time and then...give it to {i}me{/i} of all people?"
        mak "I don’t get it..."
        s "You don’t need to. You just need to accept it."
        s "Accept it and live your life, Makoto. Escape from the Smile Mile and go back home. Be free."
        mak "I mean...I kind of {i}can’t{/i} until you finish your mission."
        s "Oh."
        mak "B...But! And, uhh...o-okay. So..."
        mak "I actually...{i}do{/i} have something else that...I didn’t tell you about before. But only because I didn’t think you were ready!"
        s "I {i}knew{/i} you had extra body parts back there."
        mak "It’s not an extra body part! Just...wait here, okay? I’ll be back in one minute!"
        s "I’ll be counting..."

        scene flowertimemakoto1
        with dissolve
        play sound "escape.mp3"
        $ renpy.pause(57, hard=True)
        scene flowertimemakoto2
        with hpunch

        mak "Okay! I’m back."
        s "That was only fifty-seven seconds. You have deceived me."
        mak "That’s a level of pedantry even I have a hard time accepting. But here! "
        mak "This is my final gift to you..."

        play sound "winner.mp3"

        "{i}Sensei has obtained a {b}Koi{/b}!{/i}"

        s "Woah! You’re seriously going to trust me with a koi? This guy is huge. He’s gotta be worth at least $10."
        mak "Much more than that, Sensei."
        s "Well, duh. That’s why I said “at least.” Where did you even get it, though?"
        mak "I caught it while I was fishing somewhere I wasn’t supposed to. It’s probably illegal. But it’s also yours now, so that’s not my problem anymore."
        s "Makoto Miyamura, you have turned me into a criminal."
        mak "I mean...{i}did I,{/i} though?"
        s "I have no idea what you’re talking about. Anyway, you enjoy the sticks and I will enjoy this fish. I am suddenly hungry."
        mak "You’re not going to eat him, are you? Because I want you to look after him, Sensei. Give him a home. Do what {i}I{/i} can’t."
        s "Well...why {i}can’t{/i} you?"
        mak "Because he’s yours now."
        s "But that’s-"
        mak "Bye!"

        play sound "pop.mp3"
        scene flowertimemakoto1 with hpunch

        s "..."
        s "..."
        s "..."
        s "Well...I guess I have a fish now?"

        $ buildamayakoi = True
        $ buildamayamakoto = True

        scene black
        with dissolve2

        "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
        "The place that I’ll go next is-"

        jump buildamayagomenu

    else:
        s "I just wanted to say hi. "
        mak "Oh. Okay. Hi."
        s "Hi."
        mak "..."
        s "..."
        mak "..."
        s "..."
        mak "Is that really all?"
        s "Yup. See you later, Makoto."

        scene black
        with dissolve2

        mak "Oh...okay. "

        "I exit the Smile Mile and spend the next few minutes figuring out where to go from here."
        "The place that I’ll go next is-"

        jump buildamayagomenu

    ##################################################
label buildamayachikarealm:
    scene flowertimechika1
    with fade

    if buildamayachikaseen == True:
        s "Chika? Are you there? I want to talk to you again."

        scene flowertimechika2
        with dissolve

        c "Mhm! Welcome back, Sensei. The sale’s extended until Maya’s finally put back together."
        c "What’s up?"

        jump buildamayachikamenu1

    else:
        "Now that the mall is finally open again, I decide to head on over and see if any of the shops are selling pieces of Maya."
        "What I find instead is quite shocking, though. It appears as if an orgy is taking place here. The mall {i}I{/i} am currently accustomed to never had those."
        "Times sure are changing, huh? It must be all of that fluoride in the water."

        scene flowertimechika2
        with dissolve2

        c "Sensei! Hey! Welcome to the Spacy’s Summer Blast Savings event! You just missed Chinami. She would have been so happy to see you."
        s "You brought your little sister to an orgy?"
        c "Hm? Of course not! She was here before {i}I{/i} was. But apparently it’s not as big of a deal as you’d expect. I’ll admit, though. I was pretty shocked at first too."
        c "You just looking to shop? Or do you need a partner for the ritual? Because I’m still searching as well."
        c "Or...I guess “waiting” would be more accurate. Nobody here has really suited my tastes until you showed up. But now that you’re {i}here,{/i} we can finally join in!"
        c "I hear the pair who lasts the longest gets a prize. And you and I both know that we can knock these losers out of the water."
        s "Is the prize a piece of Maya by any chance?"
        c "I don’t think so. I’m pretty sure it’s some kind of helmet, actually."
        s "Fuck."
        c "{i}I{/i} have a piece of Maya, though."
        s "Un-fuck. That’s awesome, Chika. Can I have it?"
        c "Depends. What are you gonna do with it?"
        s "Add it to my collection bag and ultimately put her back together so Horseface Taki will let me leave."
        c "Who’s Horseface Taki?"
        s "The God of the Track. Whatever that means. Cool guy. His voice is kind of hoarse, though."
        c "Hahah! Awesome pun, Sensei!"
        s "What pun?"
        c "Oh. Uhh...nevermind, I guess? "
        c "And Sensei, I love you, but I really can’t just let go of this Maya fragment for nothing. I’m going to need something in exchange for it."
        s "Can I not just be your orgy partner? Because we might have to go at it for days if these people are serious and that time is {i}worth{/i} something, Chika. I know this because I’m a professional."
        c "You sure are, Sensei. And frankly, I think your experience is needed here. Like, just look at the couple to my left. There’s no way he’s got it inside. The angle is all wrong."
        s "We have a deal then? I have a lot of sex with you and {i}you{/i} give me one of Maya’s body parts?"
        c "I just can’t agree to that, unfortunately. Contest-slash-ritual rules don’t allow payment or bribery in exchange for sex. Any deal we make needs to be done behind the scenes."
        s "Ugh. Nothing’s ever as easy as it looks, is it?"
        c "Doesn’t seem that way, no. But hey! You know what I like, so I’m sure you’ll find something worth trading me."
        c "And in the meantime, you can have these!"

        play sound "winner.mp3"

        "{i}Sensei obtained {b}Rose Seeds{/b}!{/i}"

        s "Seeds?"
        c "Mhm. Rose seeds. They’re worth their weight in gold if you can grow them. Or...maybe not {i}gold.{/i} But they’re definitely worth their weight in roses. Because...they {i}are{/i} roses."
        s "Right."
        c "You get what I’m saying, don’t you? Plant them and...do something with them. Then do {i}more{/i} things and return to me and-"
        s "Okay, yeah. I get it. Thanks, Chika."
        c "Mhm! Anything for you, Sensei."
        c "So...can we start now? Because being around {i}this{/i} for so long has got me kind of {i}eager{/i} to join in, if you know what I mean."
        s "Maybe later. I need to finish crafting stuff for my mission first. "
        c "Damn it! Even Chinami’s gonna beat me at this rate..."

        scene black
        with dissolve

        s "I don’t think she should be allowed here, but I don’t really have the time to enforce any rules. I have work to do."
        c "I’ll be here when you need me! Or {i}want{/i} me! Or {i}anything{/i} me! I’m so lonely and so left out!"

        "And I am so busy, so I leave."
        "Where to next?"

        $ roseseed = True
        $ buildamayachikaseen = True

        jump buildamayagomenu

    menu buildamayachikamenu1:
        "Propose a trade":
            s "I’d like to propose a trade. "
            c "Kay! What kind of trade do you have in mind?"

            jump buildamayachikamenu2

        "Go back outside":
            s "Actually, I don’t think I’m ready yet. Let me gather some more stuff and come back later."
            c "Okay! I’ll be here then. Just...waiting."

            scene black
            with dissolve2

            c "Watching all these...other couples have sex..."

            "I head back outside to gather my thoughts and figure something else out."

            jump buildamayagomenu

    menu buildamayachikamenu2:
        "Corpsecrown" if buildamayacrown == True:
            s "How about this corpsecrown that I made from a giant flower and a bunch of sticks?"
            c "Ew, creepy. Why does it look like that?"
            s "I think it might be alive."
            c "So you’re giving it to me as, like...a {i}pet?{/i} Like, am I supposed to feed it? Or what?"
            s "I kind of hoped you’d just put it on your head and be like, “Cool, thanks” then give me a piece of Maya I could stuff in my bag."
            c "Oh, so it’s like some new kind of accessory then? Neat. Kinda retro, even. I don’t really think it fits my style, though."
            c "Plus, it already smells pretty terrible in here and that crown isn’t exactly helping."
            s "Damn it. Guess I’ll have to try something else then."

            jump buildamayachikamenu2

        "Lavender perfume" if buildamayaperfume == True:
            s "I can offer you this perfume I made?"
            c "Ooh, perfume! Let me see!"

            "I try to hand Chika the tester bottle I made but, before I can, she snatches the {i}bigger{/i} bottle out of my hands and takes a swig of it."

            c "Delicious! Is that lavender?"
            s "I don’t think you’re supposed to drink that."
            c "I do that with all of my perfumes when I’m testing them. I learned it from my mom."
            s "No wonder she died so young."

            "Chika takes another swig of the lavender perfume I worked so hard on."

            c "..."
            c "Is there cum in here?"
            s "It’s possible. The only ingredient apart from lavender was some mystery fluid I found in a jar Ami was holding onto."
            c "She’s so fucking weird."

            "Chika takes another sip from the lavender cum bottle."

            c "Anyway, yeah. This is perfect, Sensei. And the lavender totally helps mask the smell of sex in here! I feel like a brand new girl all of a sudden!"

            $ mayapieces += 1
            $ buildamayachika = True
            $ buildamayaperfume = False

            if mayapieces == 2:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s torso{b}!{/i}"
            if mayapieces == 3:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s pelvis{b}!{/i}"
            if mayapieces == 4:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left arm{b}!{/i}"
            if mayapieces == 5:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right arm{b}!{/i}"
            if mayapieces == 6:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left leg{b}!{/i}"
            if mayapieces == 7:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right leg{b}!{/i}"

            c "I wonder if that’s just because I haven’t had any cum in so long?"
            s "Well...I wanted you to {i}wear{/i} the perfume, but I guess drinking it is fine too so long as I get my piece of Maya out of it."
            c "What are you gonna do once you finish rebuilding her? And also, you {i}are{/i} going to come back, right? "
            c "Because, again, the sale ends once Maya’s put back together. And if I’m the one girl at this orgy who doesn’t get any dick, my self-esteem is going to take a real blow."
            s "Uhh...probably? I don’t know. "
            s "I’m kind of busy right now, though. So I’ll see you later, Chika."
            c "Whaaaaat?! Really?! Ugh!"

            scene black
            with dissolve2

            c "Guess it’s back to masturbating then..."

            "I leave Chika and head back outside to figure out where to go from here."

            jump buildamayagomenu

        "Opium" if buildamayaopium == True:
            s "What’s a sex party without a little opium? Want to trade your piece of Maya for-"
            c "Sensei, no! I don’t do {i}drugs.{/i} I’ve seen the effect those had on Yumi and I still have a little sister to take care of. "
            s "Where is she {i}now{/i} by the way?"
            c "Idunno. Fucking some kind of dog-man I think?"
            s "You’re right. Drugs would be a horrible influence on her."
            c "Exactly. So put that stuff away and make me a better, more wholesome offer. I’m going to keep watching this orgy in the meantime."

            "Damn. Looks like Chika doesn’t want any opium."
            "I’ll need to try something else."

            jump buildamayachikamenu2

        "Rose Bouquet" if buildamayabouquet == True:
            s "How about this bouquet of roses? I did what you told me and turned them into a product. Now they are more valuable and worth at least one Maya part."
            c "Oh, wow! You totally {i}did!{/i} You even replaced the stems and everything. And- oh! Are those fake thorns?"
            s "I am a master craftsman in this world. Life is so much better when I don’t destroy everything I touch."
            c "It sounds like it. And, like...I {i}love{/i} the bouquet, don’t get me wrong, but roses are kind of {i}out{/i} right now. That’s why I gave you the seeds. "
            c "I have a reputation to uphold and can’t really be caught dead with them until they’re back in season."
            s "But I worked so hard on this."
            c "And you did great! I just...{i}don’t really want them...{/i}"
            s "..."
            c "Maybe something else, though! What else do you have?"

            jump buildamayachikamenu2

        "Snapdragon Bracelet" if buildamayabracelet == True:
            s "I could give you this awesome snapdragon bracelet I made? "
            c "Snapdragons? Did you get those from Yumi? I {i}thought{/i} I heard something about her raiding people’s gardens recently."
            s "I got the seeds from her but grew the snapdragons myself. And it was really sad having to kill them for the sake of fashion, so I’d appreciate it if you would take their carcasses off my hands."
            c "I want to. Really. Just the Spacy’s Summer Blast Savings event has a strict “no bracelets” rule and I don’t want to get disqualified once we start."
            s "Only bracelets are banned? Why?"
            c "Anklets too. People started putting razorblades in them to sort of shock themselves out of arousal and keep themselves from cumming. Unfair advantage in a sex contest, unfortunately."
            c "Or a handicap if you’re into bloodplay, I guess. Either way, I don’t make the rules."
            c "Is there anything else you can trade?"
            s "Uhh...let me see."

            jump buildamayachikamenu2

        "Go back outside":
            s "Actually, I don’t think I’m ready yet. Let me gather some more stuff and come back later."
            c "Okay! I’ll be here then. Just...waiting."

            scene black
            with dissolve2

            c "Watching all these...other couples have sex..."

            "I head back outside to gather my thoughts and figure something else out."

            jump buildamayagomenu

    ##################################################
label buildamayayumirealm:
    scene flowertimeyumi1
    with fade

    if buildamayayumiseen == True:
        s "Yumi? Are you there? I want to talk to you again."

        scene flowertimeyumi2
        with dissolve

        y "Huh? The fuck you want?"

        jump buildamayayumimenu1

    else:
        "Apparently, there is a district even older than the old one. And, even more apparently, I am there now. Which is odd because I don’t exactly remember {i}coming{/i} here."
        "{size=-1}The sky twists and morphs and gives me slight motion sickness, but a peculiar sunflower peering over the wooden barrier emits a soft whirring noise that acts as verbal Dramamine and makes me feel a little better.{/size}"

        y "Ahh, fuck."

        scene flowertimeyumi2
        with dissolve2

        y "I ain’t even safe from you in a brand new world, am I?"
        s "Oh. Hey, Yumi. I guess it makes sense that you’d be here. Where’d all your clothes go?"
        y "It’s hot as balls over here, ain’t it? And I don’t wanna fuckin’ deal with that, so birthday suit it is."
        s "Awesome. Well, happy birthday."
        y "You’re a fucking idiot. Go home, Sensei."
        s "I can’t. I need to collect a bunch of pieces of Maya and then reassemble them on my bed so we can return home together."
        y "Sounds like wishful thinkin’ to me. ‘Specially after I watched you pull her head from a goddamn box just a little while ago. "
        s "A box? Don’t you mean a {i}bag?{/i}"

        play sound "tackle.mp3"
        with hpunch

        "I remove Maya’s head from my sack and hold it out to Yumi by the hair."

        y "Ew! Put that shit away! I don’t want to fuckin’ look at a {i}head.{/i} It’s bad enough just keepin’ {i}this{/i} on me."

        "Yumi vomits up one of Maya’s body parts to show me, holding it in her slimy hands before opening her mouth back up and swallowing it whole."

        y "Girl’s gotta eat."
        s "I might have the head, sure. But at least {i}I{/i} have the decency to keep mine in a sack."
        y "Ain’t human bodies just sacks of meat at the end of the day? Ain’t no issue holdin’ shit like I do. I get some nutrients out of it too. "
        y "Only downside is I get people like you tryin’ to come after me and tear open my body to get to the good stuff. "
        s "Someone else has come here searching for Maya parts? Who?"
        y "Some dude in a purple hat. Didn’t give me a name. As you can see, though, part’s still in my possession. "
        y "At least until somebody makes me a good offer, that is."
        s "Well...what are you looking for exactly? Maybe I have something that-"
        y "You ain’t got shit. I can tell by the look on your face."
        s "But I-"

        "Yumi vomits something else up and throws it at me."

        play sound "winner.mp3"

        "{i}Sensei obtained {b}Snapdragon Seeds{/b}!{/i}"

        s "Ew. Why?"
        y "Think that Maya fragment’s growing or some shit. Body’s probably tryin’ to make more room for it or whatever."
        s "Are these flower seeds?"
        y "Like I said, fucker. Girl’s gotta eat. I don’t bitch about your diet, so you damn well better not bitch about mine."
        y "Now get the fuck out of here and don’t come back until you’ve got somethin’ to trade. You hear me?"
        s "Ugh...fine."

        scene black
        with dissolve

        "I sink into the cement and emerge in a strange field somewhere, slightly wet."
        "Now where should I go?"

        $ dragonseed = True
        $ buildamayayumiseen = True

        jump buildamayagomenu

    menu buildamayayumimenu1:
        "Propose a trade":
            s "I’d like to propose a trade. "
            y "Ugh...fine. What’s your offer?"

            jump buildamayayumimenu2

        "Go back outside":
            s "Actually, I think I’ll just come back another time. It seems like you’re in a bad mood."
            y "The fuck would give you that idea, douche-monkey?"

            scene black
            with dissolve2

            s "That. I’m sorry, Yumi."
            y "Good. Fuckin’ go then. See if I care."

            "I head back outside and try to figure out where to go from here."
            "Now what?"

            jump buildamayagomenu

    menu buildamayayumimenu2:
        "Corpsecrown" if buildamayacrown == True:
            s "Could I interest you in this crown, my princess? It’s made of sticks and corpseflower bits."
            y "Can I interest {i}you{/i} in never fucking calling me your princess again? Put that stupid fucking crown away."
            s "I think it’d look great on you, though. I probably should have made a tiara, huh?"
            y "You probably shouldn’t try treating me like some fuckin’ doll to play dress up with! Should throw you over this fuckin’ ledge for trying."
            s "I’m sorry, Yumi. I just don’t like the idea of you being out in public naked and a crown atop your head would make me more comfortable."
            y "Well, I don’t give a shit about your {i}comfort,{/i} so offer something else or get the fuck out of here."
            s "Ugh...fine."

            jump buildamayayumimenu2

        "Lavender perfume" if buildamayaperfume == True:
            s "How about some fragrant lavender perfume?"
            y "How about you kill yourself?"
            s "I already tried that and you stopped me because you know you care about me deep down."
            y "Nah, I just didn’t want you fuckin’ crash landing into somebody’s house and then having to deal with all the cops in the area and shit. Too many kids to rob and I don’t want ‘em snitching."
            s "You still do that?"
            y "I {i}would{/i} if it weren’t for the lack of kids around these days. Guessin’ you already took ‘em all and chained ‘em up in your house, though."
            s "I don’t have time to kidnap anyone right now. I’m too busy trying to rebuild Maya."
            y "Well, you should try a little fuckin’ harder then. Because you ain’t gettin’ shit from me at this rate."

            "Damn it. This girl is so mean."

            jump buildamayayumimenu2

        "Opium" if buildamayaopium == True:
            s "I’ve got...opium?"
            y "Opium?"
            s "Yeah. Like...drugs."
            y "I know what fucking {i}opium{/i} is, dumbass. Why the hell do {i}you{/i} have it, though? You ain’t cool enough for that shit."
            s "I didn’t really know what else to do with the poppies I grew. And I figured that {i}someone{/i} would be willing to pay for this."
            s "I just didn’t think it would be the girl whose life had already been ravaged by drugs. "
            y "Course you didn’t, cause you’ve got no fuckin’ clue what you’re doing. It’s people specifically like {i}me{/i} who give into that shit and fall into the same goddamn hole they grew up in."
            s "But you’re better than that now, right?"
            y "Nope. Give it here, fucker."

            play sound "sword.mp3"
            with hpunch

            "Yumi snatches the opium from me and swallows it the same way she swallowed a piece of Maya earlier."

            y "Now {i}THAT{/i} is what I’m fuckin’ talking about! {i}THAT{/i} is a god damn trade."

            $ mayapieces += 1
            $ buildamayayumi = True
            $ buildamayaopium = False

            if mayapieces == 2:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s torso{b}!{/i}"
            if mayapieces == 3:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s pelvis{b}!{/i}"
            if mayapieces == 4:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left arm{b}!{/i}"
            if mayapieces == 5:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right arm{b}!{/i}"
            if mayapieces == 6:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s left leg{b}!{/i}"
            if mayapieces == 7:
                play sound "winner.mp3"
                "{i}Sensei obtained {b}Maya’s right leg{b}!{/i}"

            s "Will just swallowing it like that even get you high, though?..."
            y "You think I don’t know what I’m fuckin’ doing, numnuts?! I’m the goddamn {i}OPIUM QUEEN{/i} of the older district. "
            y "You get more of this shit, you bring it directly to me. You understand?"
            s "Why, though? I already got your Maya fragment."
            y "Because if you {i}don’t,{/i} I will find you and fucking {i}gut{/i} you. "
            y "You {i}really{/i} want something in exchange, I’ll just suck you off or whatever."
            s "I’m not sure I want that. Your throat seems to be a bit of an abyss given the things I’ve watched you both swallow and regurgitate up here."
            y "Ain’t that kind of a selling point, though?"
            s "Not if you puke on me..."
            y "Jesus Christ, you’re such a little bitch! Just take your god damn body part and get out of here!"

            scene black
            with dissolve2

            s "Okay, Yumi...Thanks for your help. Even if it was mostly self-motivated and toxic."
            y "And thank {i}you{/i} for the drugs! I’m gonna be high as FUCK soon. "

            "I leave Yumi and head back outside to figure out where to go from here."
            "I can hear her excitedly shouting from half a mile away."

            jump buildamayagomenu

        "Rose Bouquet" if buildamayabouquet == True:
            s "How about this nice bouquet of roses to-"

            play sound "sword.mp3"
            with hpunch

            "Yumi snatches the bouquet out of my hands and throws it over the ledge."

            s "Yumi, what the heck? I worked hard on that."
            y "And now you can work hard on goin’ to get it, fucker."
            s "Ugh...hold on."

            scene flowertimeyumi1
            with dissolve

            "I dash down to the lower level of the street and retrieve the bouquet I made."

            scene flowertimeyumi2
            with dissolve

            s "{i}Hah...{/i}very funny, Yu-"

            play sound "sword.mp3"
            with hpunch

            "That bitch does it {i}again!{/i}"

            s "This is so unfair! Why are you so much faster than me in this dimension?"
            y "Beats me. Why are {i}you{/i} such a little bitch?"

            "I guess roses are a no-go..."

            scene flowertimeyumi1
            with dissolve

            "I head back down to the lower level to retrieve the bouquet again, tucking it safely back into my pocket before returning to Yumi..."

            scene flowertimeyumi2
            with dissolve

            y "That’ll teach you to keep all that {i}pretty{/i} shit away from me, fuckface."
            y "Either make me a real offer or beat it."

            jump buildamayayumimenu2

        "Snapdragon Bracelet" if buildamayabracelet == True:
            s "How about this snapdragon bracelet? I made it out of those seeds you vomited up and threw at me the first time I came here."
            y "Oh, great. So now it’s even {i}bigger{/i} and I’ll have to puke it up again. You don’t think this shit through at all, do you?"
            s "Not really. I’m kind of just guessing. "
            y "Well, I’ll tell you what. Either you start guessing {i}better,{/i} or I’m going to divide my piece of Maya up into even {i}more{/i} pieces and make this puzzle {i}really{/i} fucking tough for you."
            y "Do you understand, fucker?"
            s "Yes, Yumi...I understand."
            y "You gonna be a good boy?"
            s "I’ll be a good boy..."
            y "You gonna get on your knees and bark like a little doggy?"
            s "I’d really prefer not to..."
            y "Do it or I’ll fucking kill you."
            s "{i}Hah...{/i}"

            "I get on my knees and bark like a little doggy."
            "This is a new low for me."

            y "Good..."
            y "Now rise and make me a new offer."
            s "Uhh...let’s see..."

            jump buildamayayumimenu2

        "Go back outside":
            s "Actually, I think I’ll just come back another time. It seems like you’re in a bad mood."
            y "The fuck would give you that idea, douche-monkey?"

            scene black
            with dissolve2

            s "That. I’m sorry, Yumi."
            y "Good. Fuckin’ go then. See if I care."

            "I head back outside and try to figure out where to go from here."
            "Now what?"

            jump buildamayagomenu
    ##################################################
label endofbuildamaya:
    scene black
    with dissolve2
    play sound "tackle.mp3"

    "Slowly and methodically, I begin to fuse all of Maya’s pieces back together by mixing my saliva with a jar of fleshglue."

    play sound "sound.mp3"

    "It’s a long and arduous process that culimates in my bed becoming a sopping wet mess of bodily fluids, but I manage to do it without sacrificing most of her organs."
    "There are a few I need to take out as they don’t agree with the fleshglue, but I preserve them in a series of large jars provided by Horseface Taki in the event that Maya wants them back one day."

    stop sound fadeout 5.0
    scene flowertime12
    with dissolve4

    s "Fuck yeah! "
    taki "You’ve done it, Akira Arakawa! You’ve completed another reset puzzle by reassembling your lost love! "
    taki "Do you have anything you’d like to say to the viewers back home?"

    scene flowertime13
    with dissolve

    s "I’m just glad I didn’t have to do this with Sekai. There were {i}way{/i} more pieces of her when she died."
    s "Plus, Maya being freshly deceased once the puzzle began let me finish everything before she went cold. "
    s "It was a pretty smooth experience, I’ve gotta say. And I wouldn’t have been able to do it without the support of my fans."
    taki "And what would you say is in store for those fans, {i}next?{/i} Where will Akira Arakawa go from here?"

    scene flowertime14
    with dissolve

    s "Well, Horseface Taki — the {i}first{/i} thing I’m going to do is get this body back home and give my daughter a stern lecturing about proper beach conduct."
    s "{i}Then,{/i} I think I’ll probably kick back and relax with a nice warm cup of Joseph. And hey, if I’m feeling crazy, I might even call my ex and apologize to her for fucking her little sister."
    taki "Wow! So it seems like you’re {i}really{/i} trying to put a positive spin on your life following the completion of this mission. Is that true?"
    s "It sure is, Horseface Taki. No more mistakes for me. I’m a changed man now that I have made death my little cumslut."

    scene flowertime15
    with dissolve

    taki "You heard it here first, folks! Akira Arakawa has every intention of turning his life around! But is it perhaps {i}too late{/i} for that given the {i}state{/i} of his world?"
    s "What?"
    taki "{size=-1}In just a few short moments, Akira Arakawa will learn that the events he experienced prior to our program are actually {i}irreversible!{/i} And I can assure you that you won’t want to miss {i}that!{/i}{/size}"
    s "Wha- irreversible? But that’s...No. That’s not how this is supposed to work. Reset puzzles always end with things going back to normal and-"
    taki "Unfortunately, that’s all the time we have for today! But-"
    s "No it’s not! There’s plenty more time! What do you mean “that’s all?!”"
    taki "...But join us next time for an all new reunion episode where we bring two fan-favorite girls back to the house of their dreams!"
    s "STOP TALKING! I’M NOT DONE!"
    taki "{i}I’m{/i} Horseface Taki. And {i}you’re{/i} watching HBTV. See you next time!"
    s "NO! DON’T-"

    if swimtrip2 == False:
        $ swimtrip2miss = True

    stop music
    play sound "static.mp3"
    scene colorbars with flash
    play sound "colortone.mp3"
    $ renpy.pause(10, hard=True)

    $ renpy.end_replay()
    $ beachsix7 = True

    jump beachsix8

    ##################################################
label buildamayaprehappy:
    scene flowertimesana1
    with fade

    "I return to the UNBLEACHED BEACH and call out to Sana for help, but she is not here."
    "In her place stands an unrecognizable mass of flesh, slowly gurgling and pulsating with boils and growths of various sizes as the corpsecrown sits atop what looks like the remnants of a head."
    "This is clearly not important right now. I have a fish to save."
    "I remove it from my pocket and make a mad dash to the water, pleading for it to hold on for at least one more minute."
    "And it does."

    scene black
    stop music
    play sound "water1.mp3"

    "And I drop it into the water."
    "It looks up at me, thankful."
    "I stare back, fulfilled — but empty."

    s "..."

    play sound "water1.mp3"

    "I jump in after it."
    "I belong in the sea."

    jump swimtrip2
    ##################################################
label swimtrip2:
    image swimtrip2movie movie = Movie(play="subscribestar/images2/swimtrip2movie.webm")

    scene 5
    $ renpy.pause(1, hard=True)
    scene 4
    $ renpy.pause(1, hard=True)
    scene 3
    $ renpy.pause(1, hard=True)
    scene 2
    $ renpy.pause(1, hard=True)
    scene 1
    $ renpy.pause(1, hard=True)
    scene 0
    $ renpy.pause(1, hard=True)
    scene neg1
    $ renpy.pause(1, hard=True)
    play sound "thisep.mp3"
    $ renpy.pause(5, hard=True)
    play sound "tvtrans.mp3"
    scene swimagain1
    with dissolve2
    $ renpy.pause(8, hard=True)

    "Beach."

    play music "oldweather.mp3"
    play sound "pop.mp3"
    scene swimagain2 with hpunch

    fam "WE FINALLY MADE IT!"

    play sound "cheer1.mp3"
    $ renpy.pause(4, hard=True)
    stop sound fadeout 2.0

    s "I can’t believe we’re actually at the beach!"
    ay "Rock on!"
    a "That was the longest car ride of my life! And also thankfully not the last!"

    play sound "laugh1.mp3"

    ay "Rock on!"

    scene swimagain3
    with dissolve

    s "I guess now we need to figure out how we’re going to spend our time."
    s "I want to build a sand castle!"

    scene swimagain4
    with fade

    a "I want to eat ice cream!"

    scene swimagain5
    with fade
    play sound "laugh4.mp3"

    ay "I want my mom back!"

    scene swimagain6
    with fade

    m "(symbolism)"

    scene swimagain7
    with fade

    s "I sure hope we have enough time for all of these fun activities. The last thing any of {i}us{/i} needs is a little more sunburn."

    play sound "cheer1.mp3"

    a "You’ve got that right, Dad! Sensitive skin runs in our family, and I don’t want to go back home looking like one of the red types of shellfish!"

    stop sound

    ay "Shellfish aren’t red until you cook them, Arnold!"
    a "Don’t call me Arnold, Arnold!"

    play sound "laugh2.mp3"

    ay "No, really! It’s because heat denatures a protein in their shells called crustacyanin that masks the natural red-orange pigment called astaxanthin and makes them brighter!"
    a "You’re only saying that because you’re coated in your own natural lubricant that makes it impossible for you get sunburnt at all!"

    scene swimagain5
    with fade

    ay "Oh, Ami! You know me so well!"

    scene swimagain8
    with dissolve4
    play sound "cheer1.mp3"

    ay "I guess {i}that’s{/i} why they call it a CAT-fish!"

    scene swimagain9
    with fade
    stop sound fadeout 3.0

    s "She said the line!"
    a "How come {i}Ayane{/i} gets her own catchphrase but I don’t?! I’m the main character and she’s just my friend who comes over to use the bath sometimes!"
    s "It must be the results of the latest popularity poll. You’re lacking when it comes to male voters age 35-45."
    a "But {i}Maya{/i} was the popular one before either of us and she’s thriving now."

    scene swimagain6
    with fade
    play sound "laugh3.mp3"

    m "(thriving)"
    s "She seems kind of green to me."

    play sound "cheer1.mp3"

    ay "I guess {i}that’s{/i} why they call it a CAT-fish!"

    scene swimagain4
    with fade

    a "Okay, {i}that’s{/i} it! I’m going to start my fun beach vacation without either of you!"
    s "With ice cream?"
    ay "More like {i}NICE{/i} cream!"

    play sound "laugh2.mp3"
    scene swimagain10
    with dissolve

    a "Stop being popular! This is my show!"
    a "Now please excuse me while I impress you all with my latent diving ability!"

    scene swimagain11 with fade

    s "Ami, no! The last time you showed everyone your latent diving ability, you got sucked into a vortex!"

    scene swimagain12 with dissolve
    play sound "cheer1.mp3"

    ay "Look, guys! I can fly now!"

    stop sound

    a "DAMN IT AYANEEEEEEEEEEE!"

    play sound "cheer1.mp3"

    s "Ah! And {i}I’m{/i} being sucked into quicksand!"

    play sound "laugh1.mp3"

    a "DAMN IT QUICKSANNNNNNNNNNNNND!"

    stop sound

    s "Ami, help! This sand is so much faster than normal! I’m not ready to be a short king!"

    scene swimagain13
    with dissolve

    a "No can do, Dadsei! I’ve gotta show everyone my latent diving ability for REAL this time! No more messing around!"
    ay "{size=-10} WHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!{/size}"
    s "Okay! Just be careful. That bucket looks particularly violent today!"
    ay "{size=-10}I’M GOING SO FAST!{/size}"
    a "You just need to know how to do it! Watch!"

    scene swimagain14
    with dissolve2

    a "First, you-"

    play sound "laugh3.mp3"

    a "Oh no! I must have made a mistake! I’m being sucked in!"
    ay "{size=-15} SUPERRRRR AYANEEEEEEEEE!{/size}"
    s "AMI!"
    a "Dad, help! The beach bucket is making me feel weird! I’m supposed to be good at diving!"
    s "And I’m supposed to be taller! Is the beach actually evil?!"

    scene swimagain15
    with dissolve2

    a "{size=+6}{b}AHAHAHAHAHAGAHAHAGABHGHGAHAHAHH!!!!!!!!!{/b}{/size}"
    s "Ami!"
    a "{size=+6}{b}IT IS CHANGING ME!{/b}{/size}"
    s "Ami!"
    ay "{size=-15}Everyone, look! Check out my latent diving ability!{/size}"
    a "{size=+6}{b}CURSE YOU, POPULARITY POLL!!!!!{/b}{/size}"
    s "Ami!"

    play sound "pop.mp3"
    scene swimagain16 with hpunch

    s "..."
    m "(not currently pictured)"

    scene swimagain17
    with dissolve2
    $ renpy.pause(3, hard=True)
    scene swimagain18 with dissolve
    play sound "laugh3.mp3"

    s "I guess {i}that’s{/i} why they call it a CAT-fish!"

    scene swimagain19 with dissolve2

    ay "{i}Almost there! Make sure to watch me, Sensei!{/i}"
    s "{i}I can’t! The sand is claiming me!{/i}"
    ay "{i}Then I’ll come rescue you right after my dive! Here I go!{/i}"
    s "{i}Ami! I mean- Arnold!{/i}"
    ay "{i}WHEEEEEEEEEE-{/i}"

    play sound "thump.mp3"
    scene swimagain20 with hpunch

    ay "Ack!"
    s "Nice dive, future sex!"
    ay "Pfhbfhbfht! What the heck?! This isn’t water at all! It’s just a blue image layer!"

    scene swimagain21 with fade

    s "What?! You mean to tell me we came all the way here for blue?! We have blue at home!"
    s "I wanted to be a wet boy!"
    ay "Oh, it’s actually blue raspberry flavored. Sensei! The beach is good again!"
    s "Okay! But {i}I’m{/i} not! Could you lend me a hand, please?!"

    scene swimagain22
    with dissolve

    q "Did somebody ask for HAND?"
    s "Woah! {i}Big{/i} hand!"

    scene swimagain23
    with fade

    s "{i}Ayane! I’m okay now! You can keep your hands!{/i}"
    ay "Okay, Sensei! That’s actually great news because the blue raspberry image layer is trying to eat me!"
    s "{i}What?!{/i}"
    ay "I SAID THE BLUE RASPBERRY IMAGE LAYER IS TRYING TO EAT ME! THE BEACH IS EVIL AGAIN!"
    s "{i}Oh, okay! Good luck!{/i}"
    a "{size=-15}{i}GUYYYYYYSSSSS! OVER HEREEEEEEE!{/i}{/size}"

    scene swimagain24
    with fade
    play sound "laugh3.mp3"

    a "{size=-15}The beach bucket leads to a magic circle just beyond a section of the beach guided by an assortment of spiderlike creatures! Come help!{/size}"
    s "We can not for we are fighting our own battles just the same!"
    a "{size=-15}Maya! Do something! Only you can save me!{/i}"

    play sound "laugh3.mp3"

    m "(vibing)"

    scene swimagain25
    with fade

    a "GRAAAAAAHAHHHAHAHHhh! I’M MORPHING AGAIN! WHY WON’T SOMEONE TEACH ME HOW TO CONTROL THIS!?!?!??!! CUT TO COMMERCIAL!"

    play sound "laugh1.mp3"
    scene swimagain26 with dissolve2

    a "NOT LIKE THISSSSSSSSSSSSSSSSSSS!!!!!!!!!!"

    play sound "static.mp3"
    scene swimagain27 with flash
    stop sound

    s "So this is what my life has come to."
    s "Had I had only known the beach was evil, I never would have sat in that car for five years, further endangering the life of my family on my journey toward being a wet boy."
    s "If anyone ever finds my body, let them know this — I enjoyed life. And in my next one, I hope to be faster than the sand."
    ay "{size=-10}I have escaped the blue!{/i}"
    s "I wonder if I’d turn to glass if I swallowed enough of this before being cremated?"
    s "..."
    s "..."
    s "..."

    play sound "moyo.mp3"
    scene swimagain27r
    s "{size=+15}NOTHING VENTURED, NOTHING GAINED.{/size}"

    play sound "static.mp3"
    show swimtrip2movie movie
    stop sound

    ay "Sensei, wait! Do not eat the sand yet, for I have come to rescue you."
    s "Ayane? How are you moving like that? I thought animations were only for sex."
    ay "Because I’m an object of favoritism and not bound by the same constraints everyone else is!"
    ay "I think I need to get better at walking, though. This sand sure is quick!"

    play sound "laugh1.mp3"

    s "Well, DUH. How do you think I got into this mess in the first place?!"
    ay "Say, have you seen the other Arnold around here? Whatever happened after she jumped into the beach bucket?"
    s "She’s been crying for help inside of some magic circle just beyond the spider imagery."
    ay "It may be easier to rescue her with my flying. Should I-"
    s "No! I want to spend private beach time with {i}you!{/i} Ami is merely an obstacle!"
    ay "(Gasp!) Sensei! For real?! It’s not just because I can move like this, is it?"
    s "You can move in all sorts of ways. That’s why I love you. And why I’ve welcomed you into this family despite you not being my real daughter."
    ay "It’s not just because I give awesome head?"

    play sound "laugh3.mp3"

    s "Is that supposed to be a pun?"

    scene black
    with dissolve2

    ay "HAHAHEHEHAHA! I’m also funny! And have guns! The real heroine has been me the whole time! Welcome to the Ayane show! Now, it’s time to- ah!"
    ay "Sensei! Where are you going?!"

    play sound "cheer1.mp3"
    scene swimagain28
    with dissolve2

    s "Now that I am free, I refuse to let the sand catch me again! Arakawa secret technique — ninja legs!"
    ay "You’ve been a ninja this whole time and you’ve never told me?!"

    scene swimagain29
    with dissolve
    stop sound

    s "That’s right! Just {i}try{/i} handling this massive burst of speed!"
    ay "But we were supposed to have private beach time alone where I can give you awesome head and you can be like, “Wow, Ayane! Good job!” and then let me drink all your milk!"
    s "This cow’s run its last race, babe! And if you want milk, you’re gonna have to go to the store!"
    ay "What?!"
    s "Sorry! I can’t hear you over the mountain of dust I am leaving behind that you are subsequently being buried by!"
    ay "That’s not dust at all! It’s sand! And you’re getting it in my cute girl-mouth!"

    scene swimagain30
    with dissolve

    s "{size=-10}WHOOOOOOSHHHHH!{/size}"
    ay "MOUUUUU! MATTE YO SENSEI-KUUUUUUN!~"

    scene swimagain31
    with fade

    a "..."
    a "..."
    a "..."

    play sound "laugh2.mp3"

    a "I will be up here forever, won’t I?"

    play sound "static.mp3"
    scene swimagain32 with flash
    stop sound

    s "Ah!"
    s "What is this?"
    s "It appears I have encountered a seashell. It stopped me in my tracks!"
    s "I should {i}do{/i} something about this before Ayane catches up."
    s "Perhaps if I scoop it up and clean it off, I can present it to her as part of a mating ritual and further earn her favor."
    ay "{i}Sensei!!!!! I’ll never catch up at this- oh, right. I can fly!{/i}"
    ay "{i}WHEEEEEEE!{/i}"

    play sound "static.mp3"
    scene swimagain33 with flash
    stop sound

    s "Arnold, look. I found a seashell!"
    ay "Whaaaaaaaaat? At the {i}beach?!{/i} How?!"
    s "It’s weird, though! When I press my ear to it, I don’t hear the ocean at all! And that’s {i}extra{/i} weird because the ocean is right next to us."

    play sound "laugh1.mp3"

    ay "It’s probably because you’re holding it wrong, dummy! It’s dangerous to hold a seashell like that!"

    scene swimagain34
    with dissolve

    s "Dangerous? Are you saying it might bite me?"
    ay "No, idiot! Seashells don’t have teeth! It’s dangerous for the seashell! Are you {i}trying{/i} to break it?!"
    s "Of course not! I only picked it up to earn your favor!"
    s "Look on and be amazed by my manliness and dependability. I am totally prepared to keep this item forever!"
    ay "Just give it to me already! {i}I{/i} want to hold it! I’ve never gotten to before!"

    scene swimagain35
    with fade

    s "Yeah, go ahead. I don’t like it. It’s weird."
    ay "Awwwww! It’s not weird at all, Sensei! Seashells are natural and beautiful and-"

    play sound "static.mp3"
    scene swimagain36 with flash
    stop sound

    ay "Huh?"
    s "Wha- the seashell made you ugly?!?! I don’t like you anymore!"

    scene swimagain37
    with dissolve

    ay "Huh?! What?! What’s-"

    play sound "static.mp3"
    scene swimagain38 with flash
    stop sound

    a "Chotto frickin’ matte, Ayane-chan! You’re not supposed to have that yet!"
    a "Give it here! I’ll put it back where it belongs."
    s "Ami! You have escaped! I love you the most again. Even {i}if{/i} you’re doing weird things with your fingers right now."
    a "Just making sure she didn’t take any of your parts, Dad!"
    ay "Ami?...Sensei?...Why do you look like that?..."
    ay "Is it happening again? Are we-"
    q "Aaah....aaaaaaaah!"
    ay "Shh! No, no! You’re okay! Don’t be scared~"
    s "What the heck? That seashell sounds nothing like the ocean."
    a "Because it’s not a seashell at all, Dad! It’s a poisonous fish that washed up on shore. And it’s going to kill us all if we don’t do something about it!"

    scene swimagain39
    with dissolve

    s "Oh no! I have endangered Ayane! I feel bad about this even {i}if{/i} she is ugly now!"
    a "Give us the fish, woman!"
    ay "No...No! You can’t have her! She’s mine! Get away! Both of you!"
    s "It’s already poisoned Ayane! She’s acting delusional!"

    scene swimagain40
    with hpunch
    play sound "cheer1.mp3"

    ay "Ngh!"
    s "And {i}now{/i} she is running away!"
    a "Stop! Thief! That woman stole my fish! She’ll doom us all by replicating it and distributing it to fish markets across Japan!"

    stop sound fadeout 3.0

    s "Ayane! We can still save you! Don’t make me use my ninja legs!"

    scene swimagain41
    with dissolve

    s "MMNMNH?!"
    a "It’s no use, Dad. Once someone’s poisoned by the fish, there {i}is{/i} no saving them."
    a "Even if we get it back, Ayane’s now destined to live a life of panic and anxiety any time the fish isn’t in her sight. She has already imprinted on it and has no use for you anymore."
    s "Mmmnnnn..."
    a "I know...her freedom is no more."
    a "It is only misery from here on out."
    s "..."
    a "..."

    scene swimagain42
    with dissolve2
    play sound "laugh4.mp3"

    a "I guess {i}that’s{/i} why they call it a CAT-fish!"

    stop music fadeout 4.0
    scene black
    with dissolve4

    "Sensei and Ami went on to live a happy life together in a house decorated with colorful shells."
    "Ayane was never seen again."
    "Some say she’s still buried in the sand, patiently waiting to be turned to glass."

    $ renpy.end_replay()
    $ swimtrip2 = True

    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene flowertime1 with flash
    stop sound
    play music "flowersforalgernon.mp3"
    jump buildamayahub
