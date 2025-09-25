label morningch4:
    if chap4active == True:
        if day == 4 and chikaspring3 == False:
            jump chikaspring3
        if day == 7 and rinspring2 == True and osakospring1 == False:
            jump osakospring1
        if day == 5 and osakospring2 == True and osakospring3 == False:
            jump osakospring3
        if day == 3 and tsubasa_love >= 5 and chinamispring2 == True and tsubasaspring1 == False:
            jump tsubasaspring1
        if day == 2 and yumispring2 == True and karinspring1 == False:
            jump karinspring1
        if day == 7 and karinspring1 == True and mikuspring1 == False:
            jump mikuspring1
        if day == 3 and karinspring2 == True and mikuspring3 == False:
            jump mikuspring3
        if day == 7 and karinspring2 == True and karinspring3 == False:
            jump karinspring3
        if day == 2 and karinspring3 == True and nikispring1 == True and nikispring2 == False:
            jump nikispring2
        if day == 5 and nikispring2 == True and tsuneyospring3 == True and sportswars1 == False:
            jump sportswars1
        if day == 6 and saracamp2 == True and toukaspring1 == False:
            jump toukaspring1
        if day == 7 and saracamp2 == True and mollyspring1 == False:
            jump mollyspring1
        if day == 7 and toukaspring2 == True and yasuspring1 == False:
            jump yasuspring1
        if day == 6 and yasuspring3 == True and utaspring1 == False:
            jump utaspring1
        if day == 6 and yasuspring3 == True and utaspring2 == True and norikospring2 == True and kirinspring1 == True and iospring2 == True and wakanaspring1 == False:
            jump wakanaspring1
        if day == 7 and imanispring2 == True and utaspring2 == True and beachfive1 == False:
            jump beachfive1
        if (day == 5 and beachfive2 == True and beachfive3 == False and rinspring3 == True) or (day == 5 and beachfive2 == True and beachfive3 == False and harukaspring1miss == True):
            jump beachfive3
        if day == 6 and osakospring4 == True and wakanaspring3 == False:
            jump wakanaspring3
        if day == 6 and beachfive16 == True and yumispring3 == False:
            jump yumispring3
        if day > 5 and chikaspring4 == True and chinamispring3 == False:
            jump chinamispring3
        if day == 5 and mikuspring5 == True and sanaspring4 == True and chinamispring3 == True and wakanaspring4 == True and halloweenfive1 == False:
            jump halloweenfive1
        if day == 5 and halloweenfive17 == True and christmasfive1 == False:
            jump christmasfive1
        if day == 5 and imani_lust >= 5 and rikaspring4 == True and yumispring6 == True and utaspring5 == True and toukaspring5 == True and tsuneyospring6 == True and dormwarsfive1 == False:
            jump dormwarsfive1
        if day == 6 and mayaspring3 == True and nikispring4 == False:
            jump nikispring4
        if day > 5 and amispring3 == True and wakanaspring5 == False:
            jump wakanaspring5
        if day > 5 and wakanaspring5 == True and makotospring3 == False:
            jump makotospring3
        if day == 6 and karinpic1read == True and molly_lust >= 5 and sana_lust >= 5 and noriko_lust >= 5 and futabaspring2 == True and naospring3 == True and wakanaspring6 == True and makotospring3 == True and beachsix1 == False:
            jump beachsix1
        else:
            "{i}[totaldays] Days have passed...{/i}"

            $ v11check()

            scene bedroom_day
            with dissolve2

            "I wake up again."

            s "..."

            scene black
            with dissolve

            "I need to keep myself busy."
            "........."
            "......"
            "..."

            jump ch4morningmenu

label afternoonch4:
    jump noonch4

label advancetosatch4:

    $ totaldays += 1
    $ day += 1
    if day == 6:
        hide friday onlayer date
        show saturday onlayer date
        jump morningch4
    else:
        jump morningch4

label advancetosunch4:
    $ totaldays += 1
    $ day += 1
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
        jump morningch4
    else:
        "ERROR ADVANCING TO SUNDAY"

label advancetomonch4:
    $ totaldays += 1
    $ day -= 6
    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
        jump morningch4
    else:
        "ERROR ADVANCING TO MONDAY"

label advancetotuesch4:
    $ totaldays += 1
    $ day += 1
    if day == 2:
        hide monday onlayer date
        show tuesday onlayer date
        jump morningch4
    else:
        "ERROR ADVANCING TO TUESDAY"

label advancetowedch4:
    $ totaldays += 1
    $ day += 1
    if day == 3:
        hide tuesday onlayer date
        show wednesday onlayer date
        jump morningch4
    else:
        "ERROR ADVANCING TO WEDNESDAY"

label advancetothursch4:
    $ totaldays += 1
    $ day += 1
    if day == 4:
        hide wednesday onlayer date
        show thursday onlayer date
        jump morningch4
    else:
        "ERROR ADVANCING TO THURSDAY"

label advancetofrich4:
    $ totaldays += 1
    $ day += 1
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date
        jump morningch4
    else:
        "ERROR ADVANCING TO FRIDAY"

menu ch4morningmenu:
    "Go somewhere":
        "Where should I go?"
        menu:
            "Archery Range":
                "Who do I want to spend time with?"
                menu:
                    "Touka":
                        jump toukaarchery
                    "Tsuneyo" if senseisad == False:
                        jump tsuneyoarchery
                    "Uta" if senseisad == False:
                        jump utaarchery
            "Koi Cafe" if cafeclosed == False:
                "Who do I want to spend time with?"
                menu:
                    "Rin":
                        jump cafe
                    "Haruka" if senseisad == False or saracamp2 == True:
                        if harukafirstlust == True:
                            "What do I want to do?"
                            menu:
                                "Hang out":
                                    jump harukacafe
                                "Quickie (Doggystyle)" if bonus == True:
                                    jump harukacafedogrep
                        else:
                            jump harukacafe
            "Dojo" if beachfive16 == True and osakospring4 == False and day > 5:
                jump osakodojo
            "Library" if senseisad == False:
                jump library
            "Pool" if senseisad == False or saracamp2 == True:
                jump mikupool
            "Maid Cafe" if senseisad == False and amiblock == False:
                jump amimaidhub
            "Park" if senseisad == False or saracamp2 == True:
                jump otohapark
            "Go Back":
                jump ch4morningmenu

    "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
        jump phone_morning

    "Call someone" if use_new_phone_ui == False:
        jump callmorning

    "Use the computer":
        jump computer

    "Wait until afternoon":
        scene black
        with dissolve
        stop music fadeout 3.0

        "........."
        "......"
        "..."

        jump noonch4

label dellaslump:
    $ totaldays += 1

    "{i}[totaldays] Days have passed...{/i}"

    $ v11check()

    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
    if day == 2:
        hide monday onlayer date
        show tuesday onlayer date
    if day == 3:
        hide tuesday onlayer date
        show wednesday onlayer date
    if day == 4:
        hide wednesday onlayer date
        show thursday onlayer date
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date
    if day == 6:
        hide friday onlayer date
        show saturday onlayer date
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date

    scene bedroom_day
    with dissolve2

    "I wake up again."

    s "..."

    "What do I want to do?"

    jump dellaslumpmenu

menu dellaslumpmenu:
    "Take care of Ami":
        scene black
        with dissolve2

        "I take care of Ami."
        "Afternoon comes."
        "Now, what should I do?"

        jump dellaslumpmenu2

menu dellaslumpmenu2:
    "Take care of Ami":
        "I take care of Ami."
        "She isn't getting any better."
        "Night comes."
        "Now, what should I do?"

        jump dellaslumpmenu3

menu dellaslumpmenu3:
    "Take care of Ami":
        "I finish the day off by taking care of Ami."

        scene bedroom_night
        with dissolve2

        "It's time to go to bed."

        scene black

        "The worm grows."

        $ dellapoints += 1

        if day == 1:
            $ day = 2
        elif day == 2:
            $ day = 3
        elif day == 3:
            $ day = 4
        elif day == 4:
            $ day = 5
        elif day == 5:
            $ day = 6
        elif day == 6:
            $ day = 7
        elif day == 7:
            $ day = 1

        "........."
        "......"
        "..."

        if dellapoints < 7:
            jump dellaslump
        else:
            jump dellaexit

label dellaexit:
    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
    if day == 2:
        hide monday onlayer date
        show tuesday onlayer date
    if day == 3:
        hide tuesday onlayer date
        show wednesday onlayer date
    if day == 4:
        hide wednesday onlayer date
        show thursday onlayer date
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date
    if day == 6:
        hide friday onlayer date
        show saturday onlayer date
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date

    $ totaldays += 1
    "{i}[totaldays] Days have passed...{/i}"

    $ v11check()

    scene bedroom_day
    with dissolve2

    "I wake up again."

    s "..."

    "Someone slid a note under my bedroom door in the middle of the night."
    "I can only imagine who it must have been."

    scene black
    with dissolve2

    "I pick it up and read it."
    "All it says is-"
    "{i}You don't have to wait for me.{/i}"

    s "..."

    "I should keep myself busy."

    $ chap4active = True

    jump noonch4

label noonch4:
    if day == 2 and tsuneyospring1 == True and otohaspring1 == False:
        jump otohaspring1
    if day == 6 and nikispring2 == True and tsuneyospring2 == False:
        jump tsuneyospring2
    if day == 6 and norikospring1 == True and kirinspring1 == False:
        jump kirinspring1
    if day == 7 and norikospring1 == True and utaspring1 == True and norikospring2 == False:
        jump norikospring2
    if day == 7 and christmasfive8 == True and tsukasacurious == True and tsukasaspring4 == False:
        jump tsukasaspring4
    if day == 7 and sanainvite2 == True and iospring4 == False:
        jump iospring4
    if day > 5 and harukaspring4 == True and chikaspring5 == False:
        jump chikaspring5
    if day < 6 and christmasfive8 == True and karinspring5 == False:
        jump karinspring5
    if day > 5 and karinspring5 == True and yasuspring4 == False:
        jump yasuspring4
    if day == 5 and dormwarsfive14 == True and ayanespring3 == False:
        jump ayanespring3
    if day < 6 and yukispring5 == True and yumispring8 == False:
        jump yumispring8
    if day > 5 and yumispring8 == True and chikaspring8 == False:
        jump chikaspring8
    if day == 3 and wakanaspring5 == True and wakanaspring6 == False:
        jump wakanaspring6
    else:
        "What do I want to do?"

        jump ch4noonmenu

menu ch4noonmenu:
    "Go somewhere":
        "Where should I go?"
        menu:
            "City Streets" if senseisad == False:
                jump streets
            "Shrine" if senseisad == False or saracamp2 == True:
                jump shrine
            "Dojo" if senseisad == False:
                jump osakodojo
            "Pond" if tsuneyospring1 == True and yumispring2 == False and day == 7:
                jump yumispring2
            "Bathhouse" if senseisad == False and ioblock == False:
                jump bathhouse
            "Library":
                jump nodokalibrary
            "Maid Cafe" if senseisad == False:
                jump chikamaid
            "Pool":
                menu:
                    "Ayane":
                        jump ayanepool
                    "Karin" if karinbetter == True:
                        jump karinpool
            "Go Back":
                jump ch4noonmenu

    "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
        jump phone_afternoon

    "Call someone" if use_new_phone_ui == False:
        jump callafternoon

    "Wait until night" if firsttimeshrine == True:
        s "I'll just...walk around until it starts to get dark, I guess."

        scene black
        with dissolve
        stop music fadeout 3.0

        "........."
        "......"
        "..."

        jump nightch4

label nightch4:
    if day == 6 and osakospring3 == True and tsuneyospring1 == False:
        jump tsuneyospring1
    if day == 6 and sportswars20 == True and makicamp1 == False:
        jump makicamp1
    if day == 6 and yasuspring1 == True and yasuspring2 == False:
        jump yasuspring2
    if day == 3 and yasuspring3 == True and utaspring1 == True and iospring2 == True and utaspring2 == False:
        jump utaspring2
    if day == 6 and beachfive16 == True and rikaspring1 == False:
        jump rikaspring1
    if day == 3 and chinamispring3 == True and toukaspring3 == False:
        jump toukaspring3
    if day == 5 and yukispring2 == True and sanaspring4 == False:
        jump sanaspring4
    if day == 6 and sanainvite2 == True and osakospring5 == False:
        jump osakospring5
    if day == 7 and iospring4 == True and iospring5 == False:
        jump iospring5
    if day == 3 and sanainvite2 == True and harukasex == True and harukaspring3 == False:
        jump harukaspring3
    if day == 5 and christmasfive8 == True and tsuneyospring4 == False:
        jump tsuneyospring4
    if day == 6 and christmasfive8 == True and rinspring4 == False:
        jump rinspring4
    if day == 4 and cafeclosed == False and rinspring6 == True and harukaspring4 == False:
        jump harukaspring4
    if chikaspring5 == True and osakospring6 == True and rikaspring3 == False:
        jump rikaspring3
    if day == 7 and toukaspring4 == True and toukaspring5 == False:
        jump toukaspring5
    if day == 3 and nodokathontwo3 == True and ayanespring2 == False:
        jump ayanespring2
    if day == 7 and ayanespring3 == True and yumispring7 == False:
        jump yumispring7
    if day < 6 and saraspring4 == True and saraspring5 == False:
        jump saraspring5
    if (day == 5 and yumispring8 == True and tsubasaspring4 == True and tsubasaspring6 == False) or (day == 5 and yumispring8 == True and tsubasaspring4miss == True and tsubasaspring6 == False):
        jump tsubasaspring6
    if day < 5 and naospring2 == True and naospring3 == False:
        jump naospring3
    else:
        "What do I want to do?"

        jump ch4nightmenu

menu ch4nightmenu:
    "Go somewhere":
        "Where should I go?"
        menu:
            "Bar":
                if sarasex == True or saradate1 == True:
                    "What do I want to do?"
                    menu:
                        "Hang out with Sana":
                            jump sanasbar
                        "Hang out with Sara" if (senseisad == False and sarablock == False) or (saracamp2 == True and sarablock == False):
                            jump sarasbar
                        "Hang out with Yuki" if yukiblock == False and senseisad == False or saracamp2 == True and yukiblock == False:
                            jump yukibar
                        "Missionary Sex (Sara)" if senseisad == False and sarasex == True and sarablock == False:
                            jump saramissionaryanim
                        "Cunnilingus (Sara)" if senseisad == False and sarasex == True and sarablock == False:
                            jump saraeatoutanim
                        "Blowjob (Sara)" if senseisad == False and sarasex == True and sarablock == False:
                            jump sarabjreplay
            "Porn Shop" if senseisad == False or saracamp2 == True:
                "What do I want to do?"
                menu:
                    "Hang out with Makoto" if senseisad == False:
                        jump pornshop
                    "Sitting Doggystyle (Makoto)" if beachwars19 == True and senseisad == False:
                        jump makotowatchpornrep
                    "Hang out with Maki":
                        jump pornshopmaki
                    "Blowjob (Maki)" if makibj == True and makiblock == False:
                        jump makibjanim
            "Koi Cafe" if cafeclosed == False and (senseisad == False or mollycamp1 == True):
                jump mollycafe
            "Tojo Ramen" if senseisad == False:
                jump ramenshop
            "Bathhouse" if yasuspring3 == True and day < 6 and iospring1 == False:
                jump iospring1
            "Bathhouse" if iospring1 == True and iospring5 == True and day < 5 and utaspring3 == False:
                jump utaspring3
            "Maid Cafe" if senseisad == False and amiblock == False:
                jump utamaid
            "Convenience Store" if senseisad == False or yasuspring3 == True and norikospring1 == False:
                jump convenience
            "New Hope Cathedral":
                jump church
            "Dive Bar" if (day == 5 and senseisad == False) or (day == 5 and imanispring2 == True):
                "Who do I want to spend time with?"
                menu:
                    "Imani":
                        jump imanidive
                    "Imani but, like...sexually" if christmasimani3 == True:
                        jump imanidivedoggyanim
                    "Osako":
                        jump osakodive
                    "Rika":
                        jump rikadive
                    "Wakana":
                        jump wakanadive
            "Streets" if (yumispring8 == True and kaori_love >= 45 and tsubasaspring4 == True and kaorispring1 == False) or (yumispring8 == True and kaori_love >= 45 and tsubasaspring4miss == True and kaorispring1 == False):
                jump kaorispring1
            "School Dorms" if senseisad == False or mollyspring2 == True:
                jump dormsch4
            "Go Back":
                jump ch4nightmenu

    "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
        jump phone_night

    "Call someone" if use_new_phone_ui == False:
        jump callnight

    "Invite over" if use_new_phone_ui == False and senseisad == False:
        jump inviteover

    "Go home and sleep":
        scene black
        with dissolve
        stop music fadeout 3.0

        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekdaych4
        if day >= 6:
            jump endofsatch4

label endofsatch4:
    if day == 6:
        play sound "dooropen.mp3"
        scene bedroom_night
        with dissolve

        "I open the door and immediately collapse onto the bed."
        "Being alive is exhausting."

        scene black
        with dissolve
        play sound "tackle.mp3"

        "I wonder how much longer I can take this for?"
        "........."
        "......"
        "..."
        jump advancetosunch4
    else:
        play sound "dooropen.mp3"
        scene bedroom_night
        with dissolve

        "I open the door and immediately collapse onto the bed."
        "Being alive is exhausting."

        scene black
        with dissolve
        play sound "tackle.mp3"

        "I wonder how much longer I can take this for?"
        "........."
        "......"
        "..."

        jump advancetomonch4

label endofweekdaych4:
    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve

    "I open the door and immediately collapse onto the bed."
    "Being alive is exhausting."

    scene black
    with dissolve
    play sound "tackle.mp3"

    "........."
    "......"
    "..."

    if day == 1:
        jump advancetotuesch4
    if day == 2:
        jump advancetowedch4
    if day == 3:
        jump advancetothursch4
    if day == 4:
        jump advancetofrich4
    else:
        jump advancetosatch4

label dormsch4:
    if day < 6 and yumispring7 == True and mayaspring1 == False:
        jump mayaspring1
    if escapeshampoo == True:
        scene dorm
        with fade
        play music "sweetvermouth.mp3"
        $ renpy.pause(2, hard=True)

        "A rumbling approaches."

        scene dormshampoo
        with dissolve2

        s "What the fuck is this?"

        "{i}Uh-oh! It appears that you are soap-locked!{/i}"

        s "What the hell does that mean?"

        "{i}It means you've taken something you were warned not to take and must now pay the price!{/i}"

        s "What price? How do I make this giant bottle of shampoo go away?"

        "{i}Sorry! The removal of the shampoo bottle is not yet implemented.{/i}"
        "{i}It looks like you just won't be able to use the dorms again until it is!{/i}"

        s "This seems both entirely unfair {i}and{/i} pointless. Do you have any idea how much time I've put into this game?"

        "{i}I know exactly how much time you've put into this game! Which is why I'm so surprised that you still mess up the easiest decisions!{/i}"

        s "So what? I just...can't advance anymore? That's it?"

        "{i}You can always go back in time!{/i}"
        "{i}That's what you really want anyway, isn't it?{/i}"

        s "Yes. But I don't need to hear it from a mysterious narrator and/or a bottle of shampoo."

        "{i}Well, hey! Maybe if you come back tomorrow, it won't be here anymore!{/i}"

        s "Might as well try."
        s "Later, I guess."

        "{i}Goodbye, Akira!{/i}"

        scene black
        with dissolve2

        "{i}Remember to sleep facing up tonight.{/i}"

        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        scene dorm
        with fade
        play music "sweetvermouth.mp3"

        "I decide to pay a visit to the dorms."
        "What should I do?"

        menu ch4dormmenu:
            "Knock on a door":
                jump dorm1knockch4
            "Second Floor":
                jump dorm2ch4

label dorm2ch4:
    scene dorm2
    with fade

    "Now what?"

    menu ch4dorm2menu:
        "Knock on a door":
            jump dorm2knockch4
        "First Floor":
            if bendyarms == True:
                stop music fadeout 2.0
                jump armsbentback
            else:
                jump dormsch4

label dorm1knockch4:
    "Which door should I knock on?"
    menu:
        "Room 1 (Yumi & Chika)":
            "Who do I want to talk to?"
            menu:
                "Yumi (Current Affection - [yumi_love])" if yumiblock == False:
                    jump yumidorm
                "Chika (Current Affection - [chika_love])" if chikablock == False:
                    jump chikadorm
                "Go Back":
                    jump dorm1knockch4
        "Room 2 (Ayane & Sana)":
            "Who do I want to talk to?"
            menu:
                "Ayane (Current Affection - [ayane_love])":
                    jump ayanedorm
                "Sana (Current Affection - [sana_love])":
                    jump sanadorm
                "Go Back":
                    jump dorm1knockch4
        "Room 3 (Makoto & Miku)":
            "Who do I want to talk to?"
            menu:
                "Makoto (Current Affection - [makoto_love])" if makotoblock == False:
                    jump makotodorm
                "Miku (Current Affection - [miku_love])"if mikublock == False:
                    jump mikudorm
                "Go Back":
                    jump dorm1knockch4
        "Room 4 (Rin & Futaba)":
            "Who do I want to talk to?"
            menu:
                "Rin (Current Affection - [rin_love])":
                    jump rindorm
                "Futaba (Current Affection - [futaba_love])":
                    jump futabadorm
                "Go Back":
                    jump dorm1knockch4
        "Room 5 (Ami & Maya)" if senseisad == False:
            "Who do I want to talk to?"
            menu:
                "Ami (Current Affection - [ami_love])" if amiblock == False:
                    jump amidorm
                "Maya (Current Affection - [maya_love])" if mayablock == False:
                    jump mayadorm
                "Go Back":
                    jump dorm1knockch4
        "Go Back":
            jump ch4dormmenu
        "Go Home":
            "On second thought, I'll just head back home..."
            scene black
            with dissolve2

            stop music fadeout 3.0

            "..."

            if day < 6:
                jump endofweekdaych4
            else:
                jump endofsatch4

label dorm2knockch4:
    "Which door should I knock on?"
    menu:
        "Room 6 (Molly & Tsuneyo)":
            "Who do I want to talk to?"
            menu:
                "Molly (Current Affection - [molly_love])":
                    jump mollydorm
                "Tsuneyo (Current Affection - [tsuneyo_love])":
                    jump tsuneyodorm
                "Go Back":
                    jump dorm2knockch4
        "Room 7 (Uta & Io)":
            "Who do I want to talk to?"
            menu:
                "Uta (Current Affection - [uta_love])":
                    jump utadorm
                "Io (Current Affection - [io_love])" if ioblock == False:
                    jump iodorm
                "Go Back":
                    jump dorm2knockch4
        "Room 8 (Otoha & Nodoka)":
            "Who do I want to talk to?"
            menu:
                "Otoha (Current Affection - [otoha_love])":
                    jump otohadorm
                "Nodoka (Current Affection - [nodoka_love])":
                    jump nodokadorm
                "Go Back":
                    jump dorm2knockch4
        "Room 9 (Touka & Yasu)":
            "Who do I want to talk to?"
            menu:
                "Touka (Current Affection - [touka_love])":
                    jump toukadorm
                "Yasu (Current Affection - [yasu_love])":
                    jump yasudorm
                "Go Back":
                    jump dorm2knockch4
        "Room 10 (Noriko & Kirin)":
            "Who do I want to talk to?"
            menu:
                "Noriko (Current Affection - [noriko_love])":
                    jump norikodorm
                "Kirin (Current Affection - [kirin_love])":
                    jump kirindorm
                "Go Back":
                    jump dorm2knockch4
        "Go Back":
            jump ch4dorm2menu
        "Go Home":
            "On second thought, I'll just head back home..."
            scene black
            with dissolve2

            stop music fadeout 3.0

            "..."

            if day < 6:
                jump endofweekdaych4
            else:
                jump endofsatch4
