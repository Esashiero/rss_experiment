label computer:
    scene computer
    with dissolve

    "What should I do?"
    menu computermenu:
        "Care Packages" if len(installed_care_packages) > 0:
            call care_package_menu from _call_care_package_menu
            jump computermenu
        "Change Lust Names" if bonus == True:
            menu:
                "Ami" if day98 == True:
                    $ amimaster = renpy.input("Enter a name for Ami to call you...")
                    $ amimaster = amimaster.strip()
                    "Ami will now call you [amimaster]."
                    jump computermenu
                "Ayane" if day68 == True:
                    $ ayanemaster = renpy.input("Enter a name for Ayane to call you...")
                    $ ayanemaster = ayanemaster.strip()
                    "Ayane will now call you [ayanemaster]."
                    jump computermenu
                "Chika" if day139 == True:
                    $ chikamaster = renpy.input("Enter a name for Chika to call you...")
                    $ chikamaster = chikamaster.strip()
                    "Chika will now call you [chikamaster]."
                    jump computermenu
                "Futaba" if day86 == True:
                    $ futabamaster = renpy.input("Enter a name for Futaba to call you...")
                    $ futabamaster = futabamaster.strip()
                    "Futaba will now call you [futabamaster]."
                    jump computermenu
                "Haruka" if harukafirstlust == True:
                    $ harukamaster = renpy.input("Enter a name for Haruka to call you...")
                    $ harukamaster = harukamaster.strip()
                    "Haruka will now call you [harukamaster]."
                    jump computermenu
                "Kirin" if kirinlust5 == True:
                    $ kirinmaster = renpy.input("Enter a name for Kirin to call you...")
                    $ kirinmaster = kirinmaster.strip()
                    "Kirin will now call you [kirinmaster]."
                    jump computermenu
                "Maki" if makilust5 == True:
                    $ makimaster = renpy.input("Enter a name for Maki to call you...")
                    $ makimaster = makimaster.strip()
                    "Maki will now call you [makimaster]."
                    jump computermenu
                "Makoto" if makotolust5 == True:
                    $ makotomaster = renpy.input("Enter a name for Makoto to call you...")
                    $ makotomaster = makotomaster.strip()
                    "Makoto will now call you [makotomaster]."
                    jump computermenu
                "Miku" if mikulust5 == True:
                    $ mikumaster = renpy.input("Enter a name for Miku to call you...")
                    $ mikumaster = mikumaster.strip()
                    "Miku will now call you [mikumaster]."
                    jump computermenu
                "Niki" if nikifirstlust == True:
                    $ nikimaster = renpy.input("Enter a name for Niki to call you...")
                    $ nikimaster = nikimaster.strip()
                    "Niki will now call you [nikimaster]."
                    jump computermenu
                "Sara" if saralust5 == True:
                    $ saramaster = renpy.input("Enter a name for Sara to call you...")
                    $ saramaster = saramaster.strip()
                    "Sara will now call you [saramaster]."
                    jump computermenu
                "Go back":
                    jump computermenu
        "Change Outfits" if bonus == True:
            "{i}Please note that this outfit change applies only to invite-over animations.{/i}"
            "Who do I want to change outfits for?"
            menu:
                "Ami" if amiinvite2 == True:
                    "Choose an outfit for Ami to wear."
                    menu:
                        "Casual":
                            $ amioutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Summer Dress" if returntosummer3 == True:
                            $ amioutfit = "Casual 2"
                            "Summer dress equipped."
                            jump computermenu
                        "School Uniform" if ami_love >= 25:
                            $ amioutfit = "School"
                            "School uniform equipped."
                            jump computermenu
                        "New School Uniform" if returntosummer3 == True:
                            $ amioutfit = "School 2"
                            "New school uniform equipped."
                            jump computermenu
                        "Pajamas" if ami_love >= 50:
                            $ amioutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Swimsuit" if ami_lust >= 20:
                            $ amioutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Sailor Moon" if ami_lust >= 40:
                            $ amioutfit = "Sailor Moon"
                            "Sailor Moon costume equipped."
                            jump computermenu
                        "Amber" if ami_lust >= 60:
                            $ amioutfit = "Amber"
                            "Outrider Amber costume equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ amioutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Ayane" if ayaneinvite2 == True:
                    "Choose an outfit for Ayane to wear."
                    menu:
                        "Casual":
                            $ ayaneoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Summer Clothes" if returntosummer3 == True:
                            $ ayaneoutfit = "Casual 2"
                            "Summer clothes equipped."
                            jump computermenu
                        "School Uniform" if ayane_love >= 25:
                            $ ayaneoutfit = "School"
                            "School uniform equipped."
                            jump computermenu
                        "New School Uniform" if returntosummer3 == True:
                            $ ayaneoutfit = "School 2"
                            "New school uniform equipped."
                            jump computermenu
                        "Pajamas" if ayane_love >= 50:
                            $ ayaneoutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Swimsuit" if ayane_lust >= 20:
                            $ ayaneoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Knight" if ayane_lust >= 40:
                            $ ayaneoutfit = "Knight"
                            "Knight armor equipped."
                            jump computermenu
                        "Lumine" if ayane_lust >= 60:
                            $ ayaneoutfit = "Lumine"
                            "Lumine costume equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ ayaneoutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Chika" if chikainvite2 == True:
                    "Choose an outfit for Chika to wear."
                    menu:
                        "Casual":
                            $ chikaoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Summer Clothes" if returntosummer3 == True:
                            $ chikaoutfit = "Casual 2"
                            "Summer clothes equipped."
                            jump computermenu
                        "School Uniform" if chika_love >= 25:
                            $ chikaoutfit = "School"
                            "School uniform equipped."
                            jump computermenu
                        "New School Uniform" if returntosummer3 == True:
                            $ chikaoutfit = "School 2"
                            "New school uniform equipped."
                            jump computermenu
                        "Pajamas" if chika_love >= 50:
                            $ chikaoutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Swimsuit" if chika_lust >= 20:
                            $ chikaoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Bunny Girl" if chika_lust >= 40:
                            $ chikaoutfit = "Bunny Girl"
                            "Bunny Girl costume equipped."
                            jump computermenu
                        "Dancer" if chika_lust >= 60:
                            $ chikaoutfit = "Dancer"
                            "Dancer costume equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ chikaoutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Futaba" if futabainvite2 == True:
                    "Choose an outfit for Futaba to wear."
                    menu:
                        "Casual":
                            $ futabaoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "School Uniform" if futaba_love >= 25:
                            $ futabaoutfit = "School"
                            "School uniform equipped."
                            jump computermenu
                        "New School Uniform" if returntosummer3 == True:
                            $ futabaoutfit = "School 2"
                            "New school uniform equipped."
                            jump computermenu
                        "Pajamas" if futaba_love >= 50:
                            $ futabaoutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Swimsuit" if futaba_lust >= 20:
                            $ futabaoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Mami Tomoe" if futaba_lust >= 40:
                            $ futabaoutfit = "Mami Tomoe"
                            "Mami Tomoe costume equipped."
                            jump computermenu
                        "Ganyu" if futaba_lust >= 60:
                            $ futabaoutfit = "Ganyu"
                            "Ganyu costume equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ futabaoutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Haruka" if harukainvite2 == True:
                    "Choose an outfit for Haruka to wear."
                    menu:
                        "Casual":
                            $ harukaoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Work Outfit" if haruka_love >= 25:
                            $ harukaoutfit = "Work Outfit"
                            "Work outfit equipped."
                            jump computermenu
                        "Swimsuit" if haruka_lust >= 20:
                            $ harukaoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Cat Girl" if haruka_lust >= 40:
                            $ harukaoutfit = "Cat Girl"
                            "Cat Girl costume equipped."
                            jump computermenu
                        "Devil" if haruka_lust >= 60:
                            $ harukaoutfit = "Devil"
                            "Devil costume equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ harukaoutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Kirin" if kirininvite2 == True:
                    "Choose an outfit for Kirin to wear."
                    menu:
                        "Casual":
                            $ kirinoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "School Uniform" if kirin_love >= 25:
                            $ kirinoutfit = "School"
                            "School uniform equipped."
                            jump computermenu
                        "New School Uniform" if returntosummer3 == True:
                            $ kirinoutfit = "School 2"
                            "New school uniform equipped."
                            jump computermenu
                        "Soccer Uniform" if kirin_love >= 35:
                            $ kirinoutfit = "Soccer"
                            "Soccer uniform equipped."
                            jump computermenu
                        "Swimsuit" if kirin_lust >= 20:
                            $ kirinoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Slutty Schoolgirl" if kirin_lust >= 40:
                            $ kirinoutfit = "Halloween"
                            "Slutty schoolgirl costume equipped."
                            jump computermenu
                        "Pajamas" if kirin_love >= 50:
                            $ kirinoutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ kirinoutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Cowgirl" if kirin_lust >= 50:
                            $ kirinoutfit = "Cowgirl"
                            "Cowgirl costume equipped."
                            jump computermenu
                        "Date Outfit" if kirin_love >= 100:
                            $ kirinoutfit = "Date Outfit"
                            "Date outfit equipped."
                            jump computermenu
                        "Misty" if kirin_lust >= 69:
                            $ kirinoutfit = "Misty"
                            "Misty costume equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Maki" if makiinvite2 == True:
                    "Choose an outfit for Maki to wear."
                    menu:
                        "Casual":
                            $ makioutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Lazy" if maki_love >= 25:
                            $ makioutfit = "Lazy"
                            "Lazy outfit equipped."
                            jump computermenu
                        "Fancy" if maki_love >= 50:
                            $ makioutfit = "Fancy"
                            "Fancy outfit equipped."
                            jump computermenu
                        "Cat Girl" if maki_lust >= 20:
                            $ makioutfit = "Cat Girl"
                            "Cat girl costume equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ makioutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Makoto" if makotoinvite2 == True:
                    "Choose an outfit for Makoto to wear."
                    menu:
                        "Casual":
                            $ makotooutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Summer Clothes" if returntosummer3 == True:
                            $ makotooutfit = "Casual 2"
                            "Summer clothes equipped."
                            jump computermenu
                        "School Uniform" if makoto_love >= 25:
                            $ makotooutfit = "School"
                            "School uniform equipped."
                            jump computermenu
                        "New School Uniform" if returntosummer3 == True:
                            $ makotooutfit = "School 2"
                            "New school uniform equipped."
                            jump computermenu
                        "Pajamas" if makoto_love >= 50:
                            $ makotooutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Swimsuit" if makoto_lust >= 20:
                            $ makotooutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Witch" if makoto_lust >= 40:
                            $ makotooutfit = "Witch"
                            "Witch costume equipped."
                            jump computermenu
                        "Vampire" if makoto_lust >= 60:
                            $ makotooutfit = "Vampire"
                            "Vampire costume equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ makotooutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Miku" if mikuinvite2 == True:
                    "Choose an outfit for Miku to wear."
                    menu:
                        "Casual":
                            $ mikuoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Soccer Uniform" if miku_love >= 25:
                            $ mikuoutfit = "Soccer Uniform"
                            "Soccer Uniform equipped."
                            jump computermenu
                        "Pajamas" if miku_love >= 50:
                            $ mikuoutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Summer Dress" if miku_love >= 75:
                            $ mikuoutfit = "Dress"
                            "Summer Dress equipped."
                            jump computermenu
                        "Swimsuit" if miku_lust >= 20:
                            $ mikuoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Mikubus" if miku_lust >= 40:
                            $ mikuoutfit = "Mikubus"
                            "Mikubus costume equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Molly" if mollyinvite2 == True:
                    "Choose an outfit for Molly to wear."
                    menu:
                        "Casual":
                            $ mollyoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "School Uniform" if molly_love >= 25:
                            $ mollyoutfit = "School"
                            "School Uniform equipped."
                            jump computermenu
                        "Winter Clothes" if molly_love >= 50:
                            $ mollyoutfit = "Winter"
                            "Winter Clothes equipped."
                            jump computermenu
                        "Pajamas" if molly_love >= 50:
                            $ mollyoutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Swimsuit" if molly_lust >= 20:
                            $ mollyoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu

                "Niki" if nikiinvite2 == True:
                    "Choose an outfit for Niki to wear."
                    menu:
                        "Casual":
                            $ nikioutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Pajamas" if niki_love >= 75:
                            $ nikioutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Idol" if niki_lust >= 40:
                            $ nikioutfit = "Idol"
                            "Idol outfit equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ nikioutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu

                "Nodoka" if nodokainvite1 == True:
                    "Choose an outfit for Nodoka to wear."
                    menu:
                        "Casual":
                            $ nodokaoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "School Uniform" if nodoka_love >= 25:
                            $ nodokaoutfit = "School"
                            "School Uniform equipped."
                            jump computermenu
                        "Winter Clothes" if nodoka_love >= 50:
                            $ nodokaoutfit = "Winter"
                            "Winter Clothes equipped."
                            jump computermenu
                        "Pajamas" if nodoka_love >= 50:
                            $ nodokaoutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Swimsuit" if nodoka_lust >= 20:
                            $ nodokaoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu

                "Sana" if sanainvite2 == True:
                    "Choose an outfit for Sana to wear."
                    menu:
                        "Casual":
                            $ sanaoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "School Uniform" if sana_love >= 25:
                            $ sanaoutfit = "School"
                            "School Uniform equipped."
                            jump computermenu
                        "Winter Clothes" if sana_love >= 50:
                            $ sanaoutfit = "Winter"
                            "Winter Clothes equipped."
                            jump computermenu
                        "Pajamas" if sana_love >= 50:
                            $ sanaoutfit = "Pajamas"
                            "Pajamas equipped."
                            jump computermenu
                        "Swimsuit" if sana_lust >= 20:
                            $ sanaoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu

                "Sara" if sarainvite2 == True:
                    "Choose an outfit for Sara to wear."
                    menu:
                        "Casual":
                            $ saraoutfit = "Casual"
                            "Casual outfit equipped."
                            jump computermenu
                        "Work Uniform" if sara_love >= 25:
                            $ saraoutfit = "Work"
                            "Work uniform equipped."
                            jump computermenu
                        "Swimsuit" if sara_lust >= 20:
                            $ saraoutfit = "Swimsuit"
                            "Swimsuit equipped."
                            jump computermenu
                        "Nurse" if sara_lust >= 40:
                            $ saraoutfit = "Nurse"
                            "Nurse costume equipped."
                            jump computermenu
                        "Winter Casual" if christmas7 == True:
                            $ saraoutfit = "Winter"
                            "Winter clothes equipped."
                            jump computermenu
                        "Go back":
                            jump computermenu
                "Go back":
                    jump computermenu
        "Deleted Scenes":
            "The following scenes are no longer canon and were removed for being extremely bad. Please view them at your own risk."
            menu deletedscenemenu:
                "Main: Chu~":
                    jump thechuscene
                "Main: Room With Clocks (Original)":
                    jump oldrwc
                "Main: Cliche Bath Scene":
                    jump amibathx
                "Main: Male Anatomy":
                    jump day23
                "Main: Horrible People":
                    jump day34
                "Main: David & Goliath":
                    jump day42
                "Makoto: Aim For The Balls":
                    jump makotodorm10
                "Makoto: Dangerous Words":
                    jump makotodorm15
                "Ayane: The Power of Money":
                    jump dojo15
                "Futaba: Preventive Measures":
                    jump futabadorm20
                "Go Back":
                    jump computermenu

        "Enter Cheat Code" if punished == False:
            $ cheatcode = renpy.input("Enter a code...")
            $ cheatcode = cheatcode.strip()

            if cheatcode == "goodhomie":
                $ rinbetrayed = False
                $ rininvite = True
                $ cheater = True

                "{i}Your sins have been forgiven...{/i}"
                jump computermenu

            if cheatcode == "rosebud":
                $ chika_love += 100
                $ yumi_love += 100
                $ ayane_love += 100
                $ sana_love += 100
                $ makoto_love += 100
                $ miku_love += 100
                $ rin_love += 100
                $ futaba_love += 100
                $ ami_love += 100
                $ maya_love += 100
                $ molly_love += 100
                $ tsuneyo_love += 100
                $ sara_love += 100
                $ haruka_love += 100
                $ maki_love += 100
                $ kaori_love += 100
                $ chinami_love += 100
                $ karin_love += 100
                $ kirin_love += 100
                $ uta_love += 100
                $ io_love += 100
                $ noriko_love += 100
                $ niki_love += 100
                $ yasu_love += 100
                $ touka_love += 100
                $ otoha_love += 100
                $ nodoka_love += 100
                $ yuki_love += 100
                $ wakana_love += 100
                $ osako_love += 100
                $ tsubasa_love += 100
                $ tsukasa_love += 100
                $ imani_love += 100
                $ cheater = True

                "{i}Affection with all characters increased by 100...{/i}"
                jump computermenu

            if cheatcode == "allcharactersare18+":
                play sound "computeryay.mp3"
                "You have gained magical powers!"
                $ wizardmode = True
                jump computermenu

            if cheatcode == "lagfix":
                "If you entered this cheat, it's because I suck at programming and I am sorry."
                "Your lag is now fixed!"

                $ renpy.set_return_stack([])
                jump computermenu

            if cheatcode == "floor1victory":
                $ dormwarfloor1win = True
                $ dormwarfloor2win = False
                $ dormwartie = False
                $ cheater = True
                jump computermenu
            if cheatcode == "floor2victory":
                $ dormwarfloor2win = True
                $ dormwarfloor1win = False
                $ dormwartie = False
                $ cheater = True
                jump computermenu
            if cheatcode == "dormwartie":
                $ dormwarfloor1win = False
                $ dormwarfloor2win = False
                $ dormwartie = True
                $ cheater = True
                jump computermenu
            if cheatcode == "funinthesun":
                $ beachvacation1 = False
                $ beachvacation2 = False
                $ beachvacation3 = False
                $ beachvacation4 = False
                $ beachvacation5 = False
                $ beachvacation6 = False
                $ beachvacation7 = False
                $ beachvacation8 = False
                $ beachvacation9 = False
                $ beachvacation10 = False
                $ beachvacation11 = False
                $ beachvacation12 = False
                $ beachvacation13 = False
                $ beachvacation14 = False
                $ beachvacation15 = False
                $ beachvacation16 = False
                $ ayanelust10 = False
                $ amilust10 = False
                $ kirinbeachhj = False
                $ kirinbeachmad = False
                $ cheater = True

                "{i}All beach events have been reset.{/i}"
                "{i}The complete event will trigger next Saturday morning, assuming you have completed all other prerequistes.{/i}"

                jump computermenu

            if cheatcode == "fingeryour[niece]":

                if christmas7 == True:
                    "{i}There are some mistakes you can not fix.{/i}"
                    "{i}This red string has already snapped.{/i}"

                    jump computermenu
                else:
                    $ amidorm10 = False
                    $ amisroom15 = False
                    $ cheater = True

                    "{i}Ami's events 'No One Can See Us' and 'Important Things' have been reset.{/i}"
                    "{i}You now have the opportunity to be a better [uncle].{/i}"

                    jump computermenu


            if cheatcode == "iwillalwaysloveyou":
                $ ami_lust += 100
                $ cheater = True

                "{i}Ami's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "bubblewrapprincess":
                $ ayane_lust += 100
                $ cheater = True

                "{i}Ayane's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "likemotherlikedaughter":
                $ makoto_lust += 100
                $ cheater = True

                "{i}Makoto's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "heartofgold":
                $ chika_lust += 100
                $ cheater = True

                "{i}Chika's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "atreefallsintheforest":
                $ futaba_lust += 100
                $ cheater = True

                "{i}Futaba's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "supermom":
                $ sara_lust += 100
                $ cheater = True

                "{i}Sara's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "thouartsick":
                $ haruka_lust += 100
                $ cheater = True

                "{i}Haruka's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "youonlyliveonce":
                $ kirin_lust += 100
                $ cheater = True

                "{i}Kirin's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "openrelationship":
                $ maki_lust += 100
                $ cheater = True

                "{i}Maki's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "tomboysrus":
                $ miku_lust += 100
                $ cheater = True

                "{i}Miku's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "shiningstar":
                $ niki_lust += 100
                $ cheater = True

                "{i}Niki's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "weebnote":
                $ molly_lust += 100
                $ cheater = True

                "{i}Molly's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "nyameadom":
                $ imani_lust += 100
                $ cheater = True

                "{i}Imani's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "pocketpussy":
                $ sana_lust += 100
                $ cheater = True

                "{i}Sana's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "iseeeverything":
                $ nodoka_lust += 100
                $ cheater = True

                "{i}Nodoka's lust has increased by 100.{/i}"

                jump computermenu

            if cheatcode == "seemeafterclass":
                $ chikadetention = True
                $ cheater = True

                "{i}Next time, tell her she's beautiful.{/i}"

                jump computermenu

            if cheatcode == "wheredoesthetimego":
                $ totaldays += 100
                $ cheater = True

                "{i}100 Days pass while you sit at the computer.{/i}"
                "{i}It's almost like real life now, isn't it?{/i}"

                jump computermenu

            else:
                "Code not accepted."
                jump computermenu

        "Bonus Animations":
            menu:
                "Zagull x Nithhala":
                    jump rinsanabonusanim
                "Yasu Gets A Job":
                    jump toukayasubonusanim
                "Yumi Also Gets A Job" if wizardmode == True:
                    jump yumiekibenbonusanim
                "Noriko...Kind Of Gets A Job?" if wizardmode == True:
                    jump norikoalleybonus
                "Chinami Comes Over To Play" if wizardmode == True:
                    jump chinamisexfreakbonusanim
                "Kittens Pt. II" if wizardmode == True:
                    jump kittensbonusanim
                "Go back":
                    jump computermenu

        "Go back":
            scene bedroom_day
            with dissolve

            if chap4active == True:
                jump ch4morningmenu
            else:
                jump satmorningmenu

menu chikamenuclothes:
    "Casual":
        $ chikamenuoutfit = "Casual"
        call screen gamemenuchika
        return
    "Winter":
        $ chikamenuoutfit = "Winter"
        call screen gamemenuchika
        return
    "Pajamas" if chikapatgasm == True:
        $ chikamenuoutfit = "Pajamas"
        call screen gamemenuchika
        return

menu yumimenuclothes:
    "Casual":
        $ yumimenuoutfit = "Casual"
        call screen gamemenuyumi
        return
    "Winter":
        $ yumimenuoutfit = "Winter"
        call screen gamemenuyumi
    "Christmas" if christmas7 == True:
        $ yumimenuoutfit = "Christmas"
        call screen gamemenuyumi
        return

menu ayanemenuclothes:
    "Casual":
        $ ayanemenuoutfit = "Casual"
        call screen gamemenuayane
        return
    "Winter":
        $ ayanemenuoutfit = "Winter"
        call screen gamemenuayane
        return
    "Pajamas" if ayanepatgasm == True:
        $ ayanemenuoutfit = "Pajamas"
        call screen gamemenuayane
        return

menu sanamenuclothes:
    "Casual":
        $ sanamenuoutfit = "Casual"
        call screen gamemenusana
        return
    "Winter":
        $ sanamenuoutfit = "Winter"
        call screen gamemenusana
        return

menu makotomenuclothes:
    "Casual":
        $ makotomenuoutfit = "Casual"
        call screen gamemenumakoto
        return
    "Winter":
        $ makotomenuoutfit = "Winter"
        call screen gamemenumakoto
        return
    "Pajamas" if makotopatgasm == True:
        $ makotomenuoutfit = "Pajamas"
        call screen gamemenumakoto
        return

menu mikumenuclothes:
    "Casual":
        $ mikumenuoutfit = "Casual"
        call screen gamemenumiku
        return
    "Winter":
        $ mikumenuoutfit = "Winter"
        call screen gamemenumiku
        return

menu rinmenuclothes:
    "Casual":
        $ rinmenuoutfit = "Casual"
        call screen gamemenurin
        return
    "Winter":
        $ rinmenuoutfit = "Winter"
        call screen gamemenurin
    "Christmas" if christmas7 == True:
        $ rinmenuoutfit = "Christmas"
        call screen gamemenurin
        return

menu futabamenuclothes:
    "Casual":
        $ futabamenuoutfit = "Casual"
        call screen gamemenufutaba
        return
    "Winter":
        $ futabamenuoutfit = "Winter"
        call screen gamemenufutaba
        return
    "Pajamas" if futabapatgasm == True:
        $ futabamenuoutfit = "Pajamas"
        call screen gamemenufutaba
        return

menu amimenuclothes:
    "Casual":
        $ amimenuoutfit = "Casual"
        call screen gamemenuami
        return
    "Winter":
        $ amimenuoutfit = "Winter"
        call screen gamemenuami
        return
    "Pajamas" if amipatgasm == True:
        $ amimenuoutfit = "Pajamas"
        call screen gamemenuami
        return

menu mayamenuclothes:
    "Casual":
        $ mayamenuoutfit = "Casual"
        call screen gamemenumaya
        return
    "Winter":
        $ mayamenuoutfit = "Winter"
        call screen gamemenumaya
    "Christmas" if christmas7 == True:
        $ mayamenuoutfit = "Christmas"
        call screen gamemenumaya
        return

menu mollymenuclothes:
    "Casual":
        $ mollymenuoutfit = "Casual"
        call screen gamemenumolly
        return
    "Winter":
        $ mollymenuoutfit = "Winter"
        call screen gamemenumolly
        return

menu imanimenuclothes:
    "Casual":
        $ imanimenuoutfit = "Casual"
        call screen gamemenuimani
        return
    "Winter":
        $ imanimenuoutfit = "Winter"
        call screen gamemenuimani
        return

menu tsuneyomenuclothes:
    "Casual":
        $ tsuneyomenuoutfit = "Casual"
        call screen gamemenutsuneyo
        return
    "Winter":
        $ tsuneyomenuoutfit = "Winter"
        call screen gamemenutsuneyo
        return
    "Clothing Option #3" if noodlespatgasm == True:
        $ tsuneyomenuoutfit = "Noodles"
        call screen gamemenutsuneyo
        return

menu saramenuclothes:
    "Casual":
        $ saramenuoutfit = "Casual"
        call screen gamemenusara
        return
    "Winter":
        $ saramenuoutfit = "Winter"
        call screen gamemenusara
        return
    "Pajamas" if sarapatgasm == True:
        $ saramenuoutfit = "Pajamas"
        call screen gamemenusara
        return

menu harukamenuclothes:
    "Casual":
        $ harukamenuoutfit = "Casual"
        call screen gamemenuharuka
        return
    "Winter":
        $ harukamenuoutfit = "Winter"
        call screen gamemenuharuka
        return
    "Pajamas" if harukapatgasm == True:
        $ harukamenuoutfit = "Pajamas"
        call screen gamemenuharuka
        return

menu makimenuclothes:
    "Casual":
        $ makimenuoutfit = "Casual"
        call screen gamemenumaki
        return
    "Winter":
        $ makimenuoutfit = "Winter"
        call screen gamemenumaki
        return
    "Pajamas" if makipatgasm == True:
        $ makimenuoutfit = "Pajamas"
        call screen gamemenumaki
        return

menu kaorimenuclothes:
    "Casual":
        $ kaorimenuoutfit = "Casual"
        call screen gamemenukaori
        return
    "Winter":
        $ kaorimenuoutfit = "Winter"
        call screen gamemenukaori
        return
    "Nyaori":
        $ kaorimenuoutfit = "Nyaori"
        call screen gamemenukaori
        return
    "Meowri":
        $ kaorimenuoutfit = "Nyaori"
        call screen gamemenukaori
        return

menu chinamimenuclothes:
    "Casual":
        $ chinamimenuoutfit = "Casual"
        call screen gamemenuchinami
        return
    "Winter":
        $ chinamimenuoutfit = "Winter"
        call screen gamemenuchinami
        return

menu karinmenuclothes:
    "Casual":
        $ karinmenuoutfit = "Casual"
        call screen gamemenukarin
        return
    "Winter":
        $ karinmenuoutfit = "Winter"
        call screen gamemenukarin
        return

menu kirinmenuclothes:
    "Casual":
        $ kirinmenuoutfit = "Casual"
        call screen gamemenukirin
        return
    "Winter":
        $ kirinmenuoutfit = "Winter"
        call screen gamemenukirin
        return
    "Pajamas" if kirinpatgasm == True:
        $ kirinmenuoutfit = "Pajamas"
        call screen gamemenukirin
        return

menu yukimenuclothes:
    "Casual":
        $ yukimenuoutfit = "Casual"
        call screen gamemenuyuki
        return
    "Winter":
        $ yukimenuoutfit = "Winter"
        call screen gamemenuyuki
        return

menu utamenuclothes:
    "Casual":
        $ utamenuoutfit = "Casual"
        call screen gamemenuuta
        return
    "Winter":
        $ utamenuoutfit = "Winter"
        call screen gamemenuuta
        return

menu iomenuclothes:
    "Casual":
        $ iomenuoutfit = "Casual"
        call screen gamemenuio
        return
    "Winter":
        $ iomenuoutfit = "Winter"
        call screen gamemenuio
        return
    "Casual (Original Design)":
        $ iomenuoutfit = "Old"
        call screen gamemenuio
        return

menu nikimenuclothes:
    "Casual":
        $ nikimenuoutfit = "Casual"
        call screen gamemenuniki
        return
    "Winter":
        $ nikimenuoutfit = "Winter"
        call screen gamemenuniki
        return
    "Pajamas" if nikipatgasm == True:
        $ nikimenuoutfit = "Pajamas"
        call screen gamemenuniki
        return

menu norikomenuclothes:
    "Casual":
        $ norikomenuoutfit = "Casual"
        call screen gamemenunoriko
        return
    "Winter":
        $ norikomenuoutfit = "Winter"
        call screen gamemenunoriko
        return
    "Pajamas" if norikopatgasm == True:
        $ norikomenuoutfit = "Pajamas"
        call screen gamemenunoriko
        return

menu nodokamenuclothes:
    "Casual":
        $ nodokamenuoutfit = "Casual"
        call screen gamemenunodoka
        return
    "Winter":
        $ nodokamenuoutfit = "Winter"
        call screen gamemenunodoka
        return

menu otohamenuclothes:
    "Casual":
        $ otohamenuoutfit = "Casual"
        call screen gamemenuotoha
        return
    "Winter":
        $ otohamenuoutfit = "Winter"
        call screen gamemenuotoha
        return

menu toukamenuclothes:
    "Casual":
        $ toukamenuoutfit = "Casual"
        call screen gamemenutouka
        return
    "Winter":
        $ toukamenuoutfit = "Winter"
        call screen gamemenutouka
        return

menu yasumenuclothes:
    "Casual":
        $ yasumenuoutfit = "Casual"
        call screen gamemenuyasu
        return
    "Winter":
        $ yasumenuoutfit = "Winter"
        call screen gamemenuyasu
        return

menu tsubasamenuclothes:
    "Casual":
        $ tsubasamenuoutfit = "Casual"
        call screen gamemenutsubasa
        return

menu tsukasamenuclothes:
    "Casual":
        $ tsukasamenuoutfit = "Casual"
        call screen gamemenutsukasa
        return

menu wakanamenuclothes:
    "Casual":
        $ wakanamenuoutfit = "Casual"
        call screen gamemenuwakana
        return
    "Winter":
        $ wakanamenuoutfit = "Winter"
        call screen gamemenuwakana
        return

menu osakomenuclothes:
    "Casual":
        $ osakomenuoutfit = "Casual"
        call screen gamemenuosako
        return
    "Winter":
        $ osakomenuoutfit = "Winter"
        call screen gamemenuosako
        return

menu choosemainmenu:
    "Current Release":
        $ persistent.background = "Default"
        call screen main_menu
        return
    "Maya (Swimsuit)" if nov2022pack == True:
        $ persistent.background = "Nov2022"
        call screen main_menu
        return
