screen unlockables():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Unlockables"), scroll="viewport"):

        style_prefix "event"

        vbox:

            text "{color=#AF7F00}{u}Chika Chosokabe{/color}" style "affgrid"

            text "{color=#AF7F00}Profile Outfits{/color}" style "affgrid"
            if chikapatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Chika to Orgasm Via Headpatting")
            if has_care_package("March 2025"):
                text _("{color=00C803}Mummy {b}✓{/b}{/color}")
            else:
                text _("Mummy {b}{size=-10}LiL Fanfest 25 Reward")


            text "{color=#AF7F00}Animation Outfits{/color}" style "affgrid"
            if chika_love >= 25:
                text _("{color=00C803}School Uniform {b}✓{/b}{/color}")
            else:
                text _("School Uniform {b}{size=-10}Achieve 25 Affection")
            if chika_love >= 50:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Achieve 50 Affection")
            if chika_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if chika_lust >= 40:
                text _("{color=00C803}Bunny Girl {b}✓{/b}{/color}")
            else:
                text _("Bunny Girl {b}{size=-10}Achieve 40 Lust")
            if chika_lust >= 60:
                text _("{color=00C803}Dancer {b}✓{/b}{/color}")
            else:
                text _("Dancer {b}{size=-10}Achieve 60 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")
            if returntosummer3 == True:
                text _("{color=00C803}Summer Clothes {b}✓{/b}{/color}")
            else:
                text _("Summer Clothes {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")
            if returntosummer3 == True:
                text _("{color=00C803}New School Uniform {b}✓{/b}{/color}")
            else:
                text _("New School Uniform {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")

            text "{color=#AF7F00}Picture Messages{/color}" style "affgrid"
            if chikaonsen4 == True:
                text _("{color=00C803}The Morning After {b}✓{/b}{/color}")
            else:
                text _("The Morning After {b}{size=-10}Complete Chika's Event: {i}Zanzibar (Counting Cats){/i}")
            if chikalust20 == True:
                text _("{color=00C803}Accidental Selfie {b}✓{/b}{/color}")
            else:
                text _("Accidental Selfie {b}{size=-10}Complete Chika's Event: {i}Into the Woods{/i}")

            #########################
            text "\n"

            text "{color=#d12e2e}{u}Yumi Yamaguchi{/color}" style "affgrid"

            text "{color=#d12e2e}Profile Outfits{/color}" style "affgrid"
            if christmas7 == True:
                text _("{color=00C803}Christmas Outfit {b}✓{/b}{/color}")
            else:
                text _("Christmas Outfit {b}{size=-10}Complete Main Event: Fireworks, Chicken, and the Innate Fear of Death")

            #########################
            text "\n"

            text "{color=#00bab1}{u}Ayane Amamiya{/color}" style "affgrid"

            text "{color=#00bab1}Profile Outfits{/color}" style "affgrid"
            if ayanepatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Ayane to Orgasm Via Headpatting")
            if has_care_package("January 2023"):
                text _("{color=00C803}Kimono {b}✓{/b}{/color}")
            else:
                text _("Kimono {b}{size=-10}January 2023 Care Package Reward")
            if persistent.alexisevent == True:
                text _("{color=00C803}Alexis {b}✓{/b}{/color}")
            else:
                text _("Alexis {b}{size=-10}Discover Lungrot")


            text "{color=#00bab1}Animation Outfits{/color}" style "affgrid"
            if ayane_love >= 25:
                text _("{color=00C803}School Uniform {b}✓{/b}{/color}")
            else:
                text _("School Uniform {b}{size=-10}Achieve 25 Affection")
            if ayane_love >= 50:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Achieve 50 Affection")
            if ayane_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if ayane_lust >= 40:
                text _("{color=00C803}Ser Ayane {b}✓{/b}{/color}")
            else:
                text _("Ser Ayane {b}{size=-10}Achieve 40 Lust")
            if ayane_lust >= 60:
                text _("{color=00C803}Lumine {b}✓{/b}{/color}")
            else:
                text _("Lumine {b}{size=-10}Achieve 60 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")
            if returntosummer3 == True:
                text _("{color=00C803}Summer Clothes {b}✓{/b}{/color}")
            else:
                text _("Summer Clothes {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")
            if returntosummer3 == True:
                text _("{color=00C803}New School Uniform {b}✓{/b}{/color}")
            else:
                text _("New School Uniform {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")

            text "{color=#00bab1}Picture Messages{/color}" style "affgrid"
            if ayane_lust >= 20:
                text _("{color=00C803}Mirror Selfie {b}✓{/b}{/color}")
            else:
                text _("Mirror Selfie {b}{size=-10}Achieve 20 Lust")
            if slumberreset5 == True:
                text _("{color=00C803}Something is Behind Us {b}✓{/b}{/color}")
            else:
                text _("Something is Behind Us {b}{size=-10}Complete Main Event: {i}A Thousand Years{/i}")

            #########################
            text "\n"

            text "{color=#005730}{u}Sana Sakakibara{/color}" style "affgrid"

            text "{color=#005730}Profile Outfits{/color}" style "affgrid"
            if has_care_package("December 2022"):
                text _("{color=00C803}Christmas Present {b}✓{/b}{/color}")
            else:
                text _("Christmas Present {b}{size=-10}December 2022 Care Package Reward")
            if sanapatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Sana to Orgasm Via Headpatting")

            text "{color=#005730}Picture Messages{/color}" style "affgrid"
            if beachfive12 == True:
                text _("{color=00C803}A Thirst That Cannot Be Quenched {b}✓{/b}{/color}")
            else:
                text _("A Thirst That Cannot Be Quenched {b}{size=-10}Complete Main Event: {i}Pros, Cons, and Countermeasures{/i}")

            #########################
            text "\n"

            text "{color=#ff8112}{u}Miku Maruyama{/color}" style "affgrid"

            text "{color=#ff8112}Profile Outfits{/color}" style "affgrid"
            if mikupatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Miku to Orgasm Via Headpatting")
            if has_care_package("March 2025"):
                text _("{color=00C803}Miku Gyaruyama {b}✓{/b}{/color}")
            else:
                text _("Miku Gyaruyama {b}{size=-10}LiL Fanfest 25 Reward")


            text "{color=#ff8112}Animation Outfits{/color}" style "affgrid"
            if miku_love >= 25:
                text _("{color=00C803}Soccer Uniform {b}✓{/b}{/color}")
            else:
                text _("Soccer Uniform {b}{size=-10}Achieve 25 Affection")
            if miku_love >= 50:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Achieve 50 Affection")
            if miku_love >= 75:
                text _("{color=00C803}Summer Dress {b}✓{/b}{/color}")
            else:
                text _("Summer Dress {b}{size=-10}Achieve 75 Affection")
            if miku_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if miku_lust >= 40:
                text _("{color=00C803}Mikubus {b}✓{/b}{/color}")
            else:
                text _("Mikubus {b}{size=-10}Achieve 40 Lust")

            text "{color=#ff8112}Picture Messages{/color}" style "affgrid"
            if dormwartwo4 == True:
                text _("{color=00C803}Miku Gyaruyama {b}✓{/b}{/color}")
            else:
                text _("Miku Gyaruyama {b}{size=-10}Complete Main Event: {i}Gamer Girl Grindfest{/i}")
            if mikuspring3 == True:
                text _("{color=00C803}Trying Something New {b}✓{/b}{/color}")
            else:
                text _("Trying Something New {b}{size=-10}Complete Miku's Event: {i}The Boys{/i}")

            #########################
            text "\n"

            text "{color=#3c55fa}{u}Makoto Miyamura{/color}" style "affgrid"

            text "{color=#3c55fa}Profile Outfits{/color}" style "affgrid"
            if makotopatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Makoto to Orgasm Via Headpatting")
            if has_care_package("April 2023"):
                text _("{color=00C803}Vampire {b}✓{/b}{/color}")
            else:
                text _("Vampire {b}{size=-10}April 2023 Care Package Reward")
            if has_care_package("March 2025"):
                text _("{color=00C803}Date Outfit {b}✓{/b}{/color}")
            else:
                text _("Date Outfit {b}{size=-10}LiL Fanfest 25 Reward")


            text "{color=#3c55fa}Animation Outfits{/color}" style "affgrid"
            if makoto_love >= 25:
                text _("{color=00C803}School Uniform {b}✓{/b}{/color}")
            else:
                text _("School Uniform {b}{size=-10}Achieve 25 Affection")
            if makoto_love >= 50:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Achieve 50 Affection")
            if makoto_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if makoto_lust >= 40:
                text _("{color=00C803}Witch {b}✓{/b}{/color}")
            else:
                text _("Witch {b}{size=-10}Achieve 40 Lust")
            if makoto_lust >= 60:
                text _("{color=00C803}Vampire {b}✓{/b}{/color}")
            else:
                text _("Vampire {b}{size=-10}Achieve 60 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Casual {b}✓{/b}{/color}")
            else:
                text _("Winter Casual {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")
            if returntosummer3 == True:
                text _("{color=00C803}Summer Clothes {b}✓{/b}{/color}")
            else:
                text _("Summer Clothes {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")
            if returntosummer3 == True:
                text _("{color=00C803}New School Uniform {b}✓{/b}{/color}")
            else:
                text _("New School Uniform {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")

            text "{color=#3c55fa}Picture Messages{/color}" style "affgrid"
            if pornshop5 == True:
                text _("{color=00C803}Permanent Wallpaper {b}✓{/b}{/color}")
            else:
                text _("Permanent Wallpaper {b}{size=-10}Complete Makoto's Event: {i}Watching Porn Alone{/i}")
            if makotodorm55p2 == True:
                text _("{color=00C803}Makoto's New Bra {b}✓{/b}{/color}")
            else:
                text _("Makoto's New Bra {b}{size=-10}Complete Makoto's Event: {i}Suffer The Same{/i}")
            if halloweenfour15 == True:
                text _("{color=00C803}Overwhelming Urge {b}✓{/b}{/color}")
            else:
                text _("Overwhelming Urge {b}{size=-10}Complete Main Event: {i}I Won't Say I'm In Love{/i}")


            #########################
            text "\n"

            text "{color=#9326ff}{u}Futaba Fukuyama{/color}" style "affgrid"

            text "{color=#9326ff}Profile Outfits{/color}" style "affgrid"
            if futabapatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Futaba to Orgasm Via Headpatting")
            if has_care_package("August 2023"):
                text _("{color=00C803}Gym Clothes {b}✓{/b}{/color}")
            else:
                text _("Gym Clothes {b}{size=-10}August 2023 Care Package Reward")
            if has_care_package("March 2025"):
                text _("{color=00C803}Ganyu {b}✓{/b}{/color}")
            else:
                text _("Ganyu {b}{size=-10}LiL Fanfest 25 Reward")

            text "{color=#9326ff}Animation Outfits{/color}" style "affgrid"
            if futaba_love >= 25:
                text _("{color=00C803}School Uniform {b}✓{/b}{/color}")
            else:
                text _("School Uniform {b}{size=-10}Achieve 25 Affection")
            if futaba_love >= 50:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Achieve 50 Affection")
            if futaba_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if futaba_lust >= 40:
                text _("{color=00C803}Mami Tomoe {b}✓{/b}{/color}")
            else:
                text _("Mami Tomoe {b}{size=-10}Achieve 40 Lust")
            if futaba_lust >= 60:
                text _("{color=00C803}Ganyu {b}✓{/b}{/color}")
            else:
                text _("Ganyu {b}{size=-10}Achieve 60 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")
            if returntosummer3 == True:
                text _("{color=00C803}New School Uniform {b}✓{/b}{/color}")
            else:
                text _("New School Uniform {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")

            text "{color=#9326ff}Picture Messages{/color}" style "affgrid"
            if secondbeach10 == True:
                text _("{color=00C803}Long Walks {b}✓{/b}{/color}")
            else:
                text _("Long Walks {b}{size=-10}Complete Main Event: {i}Torrential Downpour. Child of Man.{/i}")
            if beachwars10 == True:
                text _("{color=00C803}Favorite Teacher {b}✓{/b}{/color}")
            else:
                text _("Favorite Teacher {b}{size=-10}Complete Main Event: {i}Monsters{/i}")

            #########################
            text "\n"

            text "{color=#a30041}{u}Rin Rokuhara{/color}" style "affgrid"

            text "{color=#a30041}Profile Outfits{/color}" style "affgrid"
            if christmas7 == True:
                text _("{color=00C803}Christmas Outfit {b}✓{/b}{/color}")
            else:
                text _("Christmas Outfit {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")
            if has_care_package("August 2023"):
                text _("{color=00C803}Gym Clothes {b}✓{/b}{/color}")
            else:
                text _("Gym Clothes {b}{size=-10}August 2023 Care Package Reward")

            text "{color=#a30041}Picture Messages{/color}" style "affgrid"
            if futabadorm40 == True:
                text _("{color=00C803}Gym Selfie {b}✓{/b}{/color}")
            else:
                text _("Gym Selfie {b}{size=-10}Complete Futaba's Event: {i}Skin (Start Somewhere){/i}")
            if christmastwo20 == True:
                text _("{color=00C803}Moments Before Disaster {b}✓{/b}{/color}")
            else:
                text _("Moments Before Disaster {b}{size=-10}Complete Main Event: {i}Glued to the Sky{/i}")

            #########################
            text "\n"

            text "{color=#ff4dd2}{u}Ami Arakawa{/color}" style "affgrid"

            text "{color=#ff4dd2}Profile Outfits{/color}" style "affgrid"
            if amipatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Ami to Orgasm Via Headpatting")
            if has_care_package("January 2023"):
                text _("{color=00C803}Kimono {b}✓{/b}{/color}")
            else:
                text _("Kimono {b}{size=-10}January 2023 Care Package Reward")
            if amyevent == True:
                text _("{color=00C803}Amy {b}✓{/b}{/color}")
            else:
                text _("Amy {b}{size=-10}Have a Sufficient Amount of Fun")


            text "{color=#ff4dd2}Animation Outfits{/color}" style "affgrid"
            if ami_love >= 25:
                text _("{color=00C803}School Uniform {b}✓{/b}{/color}")
            else:
                text _("School Uniform {b}{size=-10}Achieve 25 Affection")
            if ami_love >= 50:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Achieve 50 Affection")
            if ami_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if ami_lust >= 40:
                text _("{color=00C803}Sailor Moon {b}✓{/b}{/color}")
            else:
                text _("Sailor Moon {b}{size=-10}Achieve 40 Lust")
            if ami_lust >= 60:
                text _("{color=00C803}Outrider Amber {b}✓{/b}{/color}")
            else:
                text _("Outrider Amber {b}{size=-10}Achieve 60 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")
            if returntosummer3 == True:
                text _("{color=00C803}Summer Dress {b}✓{/b}{/color}")
            else:
                text _("Summer Dress {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")
            if returntosummer3 == True:
                text _("{color=00C803}New School Uniform {b}✓{/b}{/color}")
            else:
                text _("New School Uniform {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")

            text "{color=#ff4dd2}Picture Messages{/color}" style "affgrid"
            if christmastwo20 == True and amifingered == True:
                text _("{color=00C803}Ghost Photographer {b}✓{/b}{/color}")
            else:
                text _("Ghost Photographer {b}{size=-10}Complete Main Event: {i}Glued to the Sky{/i}")
            if beachwars4 == True:
                text _("{color=00C803}Beachside Ramune {b}✓{/b}{/color}")
            else:
                text _("Beachside Ramune {b}{size=-10}Complete Main Event: {i}The Rest of Me{/i}")

            #########################
            text "\n"

            text "{color=#18b500}{u}Maya Makinami{/color}" style "affgrid"

            text "{color=#18b500}Profile Outfits{/color}" style "affgrid"
            if christmas7 == True:
                text _("{color=00C803}Christmas Outfit {b}✓{/b}{/color}")
            else:
                text _("Christmas Outfit {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death{/i}")
            if maya2profile == True:
                text _("{color=00C803}Maya 2 {b}✓{/b}{/color}")
            else:
                text _("Maya 2 {b}{size=-10}Open a Secret Door{/i}")
            if has_care_package("March 2025"):
                text _("{color=00C803}Haruhi Suzumiya {b}✓{/b}{/color}")
            else:
                text _("Haruhi Suzumiya {b}{size=-10}LiL Fanfest 25 Reward")

            #########################
            text "\n"

            text "{color=#4FCB80}{u}Molly MacCormack{/color}" style "affgrid"

            text "{color=#4FCB80}Profile Outfits{/color}" style "affgrid"
            if has_care_package("December 2022"):
                text _("{color=00C803}Christmas Outfit {b}✓{/b}{/color}")
            else:
                text _("Christmas Outfit {b}{size=-10}December 2022 Care Package Reward")
            if mollypatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Molly to Orgasm Via Headpatting")
            if has_care_package("March 2025"):
                text _("{color=00C803}Date Outfit {b}✓{/b}{/color}")
            else:
                text _("Date Outfit {b}{size=-10}LiL Fanfest 25 Reward")

            text "{color=#4FCB80}Picture Messages{/color}" style "affgrid"
            if halloweenfour1 == True:
                text _("{color=00C803}Ginger Wolf {b}✓{/b}{/color}")
            else:
                text _("Ginger Wolf {b}{size=-10}Complete Main Event: {i}Eggside Octopus{/i}")
            if halloweenfive2 == True:
                text _("{color=00C803}The Hermit {b}✓{/b}{/color}")
            else:
                text _("The Hermit {b}{size=-10}Complete Main Event: {i}More Than Her{/i}")

            #########################
            text "\n"

            text "{color=#C8B330}{u}Tsuneyo Tojo{/color}" style "affgrid"

            text "{color=#C8B330}Profile Outfits{/color}" style "affgrid"
            if noodlespatgasm == True:
                text _("{color=00C803}Outfit #3 {b}✓{/b}{/color}")
            else:
                text _("Outfit #3 {b}{size=-10}Commit a Terrible Sin")

            #########################
            text "\n"

            text "{color=#AA4588}{u}Uta Ushibori{/color}" style "affgrid"

            text "{color=#AA4588}Profile Outfits{/color}" style "affgrid"
            if has_care_package("March 2025"):
                text _("{color=00C803}Kunoichi {b}✓{/b}{/color}")
            else:
                text _("Kunoichi {b}{size=-10}LiL Fanfest 25 Reward")

            text "{color=#AA4588}Picture Messages{/color}" style "affgrid"
            if utadorm30 == True:
                text _("{color=00C803}Mistakes From a Younger Age {b}✓{/b}{/color}")
            else:
                text _("Mistakes From a Younger Age {b}{size=-10}Complete Uta's Event: {i}Uta-chan{/i}")

            #########################
            text "\n"

            text "{color=#BBE3A1}{u}Io Ichimonji{/color}" style "affgrid"
            text "{color=#BBE3A1}Picture Messages{/color}" style "affgrid"
            if has_care_package("March 2025"):
                text _("{color=00C803}Older Io's Wiener Practice {b}✓{/b}{/color}")
            else:
                text _("Older Io's Wiener Practice {b}{size=-10}LiL Fanfest 25 Reward")

            #########################
            text "\n"

            text "{color=#B83A6A}{u}Otoha Okakura{/color}" style "affgrid"

            text "{color=#B83A6A}Profile Outfits{/color}" style "affgrid"
            if has_care_package("December 2022"):
                text _("{color=00C803}Christmas Concert Outfit {b}✓{/b}{/color}")
            else:
                text _("Christmas Concert Outfit {b}{size=-10}December 2022 Care Package Reward")

            text "{color=#B83A6A}Picture Messages{/color}" style "affgrid"
            if nikinudetrade == True:
                text _("{color=00C803}You Really Shouldn't Have This {b}✓{/b}{/color}")
            else:
                text _("You Really Shouldn't Have This {b}{size=-10}Betray your childhood friend")

            #########################
            text "\n"

            text "{color=#AF89A2}{u}Nodoka Nagasawa{/color}" style "affgrid"

            text "{color=#AF89A2}Profile Outfits{/color}" style "affgrid"
            if has_care_package("August 2023"):
                text _("{color=00C803}Gym Clothes {b}✓{/b}{/color}")
            else:
                text _("Gym Clothes {b}{size=-10}August 2023 Care Package Reward")
            if nodokapatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Nodoka to Orgasm Via Headpatting")
            if has_care_package("March 2025"):
                text _("{color=00C803}Rindoka Nagahara {b}✓{/b}{/color}")
            else:
                text _("Rindoka Nagahara {b}{size=-10}LiL Fanfest 25 Reward")

            text "{color=#AF89A2}Picture Messages{/color}" style "affgrid"
            if nodokalibrary1 == True:
                text _("{color=00C803}Secondhand Voyeur {b}✓{/b}{/color}")
            else:
                text _("Secondhand Voyeur {b}{size=-10}Complete Nodoka's Event: {i}Cracks in the Armor{/i}")
            if dormwartwo9 == True:
                text _("{color=00C803}Still Life {b}✓{/b}{/color}")
            else:
                text _("Still Life {b}{size=-10}Complete Main Event: {i}Midnight Mom Mosh{/i}")

            #########################
            text "\n"

            text "{color=#F0E68C}{u}Touka Tsukioka{/color}" style "affgrid"

            text "{color=#F0E68C}Profile Outfits{/color}" style "affgrid"
            if has_care_package("April 2023"):
                text _("{color=00C803}Sadako Yamamura {b}✓{/b}{/color}")
            else:
                text _("Sadako Yamamura {b}{size=-10}April 2023 Care Package Reward")
            if has_care_package("March 2025"):
                text _("{color=00C803}Hasshaku-sama {b}✓{/b}{/color}")
            else:
                text _("Hasshaku-sama {b}{size=-10}LiL Fanfest 25 Reward")

            #########################
            text "\n"

            text "{color=#74d9e9}{u}Yasu Yasui{/color}" style "affgrid"

            text "{color=#74d9e9}Profile Outfits{/color}" style "affgrid"
            if has_care_package("March 2025"):
                text _("{color=00C803}Gravure Outfit {b}✓{/b}{/color}")
            else:
                text _("Gravure Outfit {b}{size=-10}LiL Fanfest 25 Reward")

            #########################
            text "\n"

            text "{color=#FF61A9}{u}Noriko Nakayama{/color}" style "affgrid"

            text "{color=#FF61A9}Profile Outfits{/color}" style "affgrid"
            if has_care_package("March 2025"):
                text _("{color=00C803}Yoriko {b}✓{/b}{/color}")
            else:
                text _("Yoriko {b}{size=-10}LiL Fanfest 25 Reward")

            text "{color=#FF61A9}Picture Messages{/color}" style "affgrid"
            if norikoinvite2 == True:
                text _("{color=00C803}Parting Gift {b}✓{/b}{/color}")
            else:
                text _("Parting Gift {b}{size=-10}Complete Noriko's Event: {i}Beginnings. Endings. Things in Between.{/i}")
            if slumberreset5 == True:
                text _("{color=00C803}All Grown Up {b}✓{/b}{/color}")
            else:
                text _("All Grown Up {b}{size=-10}Complete Main Event: {i}A Thousand Years{/i}")
            if halloweenfive1 == True:
                text _("{color=00C803}Norimani Imaiyama {b}✓{/b}{/color}")
            else:
                text _("Norimani Imaiyama {b}{size=-10}Complete Main Event: {i}Rubik’s Cube{/i}")

            #########################
            text "\n"

            text "{color=#9C8080}{u}Kirin Kanda{/color}" style "affgrid"

            text "{color=#9C8080}Profile Outfits{/color}" style "affgrid"
            if kirinpatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Kirin to Orgasm Via Headpatting")
            if has_care_package("March 2025"):
                text _("{color=00C803}Date Outfit {b}✓{/b}{/color}")
            else:
                text _("Date Outfit {b}{size=-10}LiL Fanfest 25 Reward")


            text "{color=#9C8080}Animation Outfits{/color}" style "affgrid"
            if kirin_love >= 25:
                text _("{color=00C803}School Uniform {b}✓{/b}{/color}")
            else:
                text _("School Uniform {b}{size=-10}Achieve 25 Affection")
            if kirin_love >= 35:
                text _("{color=00C803}Soccer Uniform {b}✓{/b}{/color}")
            else:
                text _("Soccer Uniform {b}{size=-10}Achieve 35 Affection")
            if kirin_love >= 50:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Achieve 50 Affection")
            if kirin_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if kirin_lust >= 40:
                text _("{color=00C803}Slutty Schoolgirl {b}✓{/b}{/color}")
            else:
                text _("Slutty Schoolgirl {b}{size=-10}Achieve 40 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")
            if returntosummer3 == True:
                text _("{color=00C803}New School Uniform {b}✓{/b}{/color}")
            else:
                text _("New School Uniform {b}{size=-10}Complete Main Event: {i}Utinam Ne Illum Numquam Conspexissem")
            if kirin_lust >= 50:
                text _("{color=00C803}Cowgirl {b}✓{/b}{/color}")
            else:
                text _("Cowgirl {b}{size=-10}Achieve 50 Lust")
            if kirin_lust >= 69:
                text _("{color=00C803}Misty {b}✓{/b}{/color}")
            else:
                text _("Misty {b}{size=-10}Achieve 69 Lust")
            if kirin_love >= 100:
                text _("{color=00C803}Date Outfit {b}✓{/b}{/color}")
            else:
                text _("Date Outfit {b}{size=-10}Achieve 100 Lust")

            text "{color=#9C8080}Picture Messages{/color}" style "affgrid"
            if kirinlust20 == True:
                text _("{color=00C803}Patiently Waiting {b}✓{/b}{/color}")
            else:
                text _("Patiently Waiting {b}{size=-10}Complete Kirin's Event: {i}Taking the Reins{/i}")
            if halloweenfour1 == True:
                text _("{color=00C803}Amateur Cowgirl {b}✓{/b}{/color}")
            else:
                text _("Amateur Cowgirl {b}{size=-10}Complete Main Event: {i}Eggside Octopus{/i}")

            #########################
            text "\n"

            text "{color=#B02E8C}{u}Haruka Hamasaki{/color}" style "affgrid"

            text "{color=#B02E8C}Profile Outfits{/color}" style "affgrid"
            if harukapatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Haruka to Orgasm Via Headpatting")
            if has_care_package("March 2025"):
                text _("{color=00C803}Fuckubus {b}✓{/b}{/color}")
            else:
                text _("Fuckubus {b}{size=-10}LiL Fanfest 25 Reward")


            text "{color=#B02E8C}Animation Outfits{/color}" style "affgrid"
            if haruka_love >= 25:
                text _("{color=00C803}Work Uniform {b}✓{/b}{/color}")
            else:
                text _("Work Uniform {b}{size=-10}Achieve 25 Affection")
            if haruka_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if haruka_lust >= 40:
                text _("{color=00C803}Cat Girl {b}✓{/b}{/color}")
            else:
                text _("Cat Girl {b}{size=-10}Achieve 40 Lust")
            if haruka_lust >= 60:
                text _("{color=00C803}Devil {b}✓{/b}{/color}")
            else:
                text _("Devil {b}{size=-10}Achieve 60 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")

            text "{color=#B02E8C}Picture Messages{/color}" style "affgrid"
            if halloweentwo5 == True:
                text _("{color=00C803}Ditching the Devil {b}✓{/b}{/color}")
            else:
                text _("Ditching the Devil {b}{size=-10}Complete Main Event: {i}Anglerfish{/i}")

            #########################
            text "\n"

            text "{color=#80C9DC}{u}Imani Imai{/color}" style "affgrid"

            text "{color=#80C9DC}Profile Outfits{/color}" style "affgrid"
            if has_care_package("March 2025"):
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}LiL Fanfest 25 Reward")

            text "{color=#80C9DC}Picture Messages{/color}" style "affgrid"
            if dormwartwo3 == True:
                text _("{color=00C803}Wannabe Student {b}✓{/b}{/color}")
            else:
                text _("Wannabe Student {b}{size=-10}Complete Main Event: {i}A Frame on a Shelf in a House{/i}")

            #########################
            text "\n"

            text "{color=#4B4B4B}{u}Kaori Kadowaki{/color}" style "affgrid"

            text "{color=#4B4B4B}Profile Outfits{/color}" style "affgrid"
            if nyaorifit == True:
                text _("{color=00C803}Nyaori {b}✓{/b}{/color}")
            else:
                text _("Nyaori {b}{size=-10}Obtained from the Roadside Merchant")
            if halloweenfive8 == True:
                text _("{color=00C803}Meowri {b}✓{/b}{/color}")
            else:
                text _("Meowri {b}{size=-10}Defeat the Final Boss of SENSEI-QUEST")

            text "{color=#4B4B4B}Picture Messages{/color}" style "affgrid"
            if nikidate5 == True:
                text _("{color=00C803}Hard Circle Lizard {b}✓{/b}{/color}")
            else:
                text _("Hard Circle Lizard {b}{size=-10}Complete Niki's Event: {i}Like it's Any Other Day{/i}")
            if slumberreset5 == True:
                text _("{color=00C803}Sharp Helmet Bird {b}✓{/b}{/color}")
            else:
                text _("Sharp Helmet Bird {b}{size=-10}Complete Main Event: {i}A Thousand Years{/i}")
            if beachfive16 == True:
                text _("{color=00C803}Tiny Big Nyanfriend {b}✓{/b}{/color}")
            else:
                text _("Tiny Big Nyanfriend {b}{size=-10}Complete Main Event: {i}Perfect Harmony{/i}")

            #########################
            text "\n"

            text "{color=#AC9D77}{u}Karin Kanda{/color}" style "affgrid"

            text "{color=#AC9D77}Profile Outfits{/color}" style "affgrid"
            if has_care_package("August 2023"):
                text _("{color=00C803}Gym Clothes {b}✓{/b}{/color}")
            else:
                text _("Gym Clothes {b}{size=-10}August 2023 Care Package Reward")

            #########################
            text "\n"

            text "{color=#3B84A9}{u}Maki Miyamura{/color}" style "affgrid"

            text "{color=#3B84A9}Profile Outfits{/color}" style "affgrid"
            if makipatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Maki to Orgasm Via Headpatting")


            text "{color=#3B84A9}Animation Outfits{/color}" style "affgrid"
            if maki_love >= 25:
                text _("{color=00C803}Lazy Maki {b}✓{/b}{/color}")
            else:
                text _("Lazy Maki {b}{size=-10}Achieve 25 Affection")
            if maki_love >= 50:
                text _("{color=00C803}Fancy Maki {b}✓{/b}{/color}")
            else:
                text _("Fancy Maki {b}{size=-10}Achieve 50 Affection")
            if maki_lust >= 20:
                text _("{color=00C803}Cat Girl {b}✓{/b}{/color}")
            else:
                text _("Cat Girl {b}{size=-10}Achieve 20 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")

            #########################

            text "\n"

            text "{color=#602F2B}{u}Nao-chan{/color}" style "affgrid"

            text "{color=#602F2B}Profile Outfits{/color}" style "affgrid"
            if nyaofit == True:
                text _("{color=00C803}Nyao-chan {b}✓{/b}{/color}")
            else:
                text _("Nyao-chan {b}{size=-10}Obtained from the Roadside Merchant")

            #########################
            text "\n"

            text "{color=#FF0074}{u}Niki Nakayama{/color}" style "affgrid"

            text "{color=#FF0074}Profile Outfits{/color}" style "affgrid"
            if nikipatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Niki to Orgasm Via Headpatting")


            text "{color=#FF0074}Animation Outfits{/color}" style "affgrid"
            if niki_love >= 75:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Achieve 75 Affection")
            if niki_lust >= 40:
                text _("{color=00C803}Idol {b}✓{/b}{/color}")
            else:
                text _("Idol {b}{size=-10}Achieve 40 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")

            text "{color=#FF0074}Picture Messages{/color}" style "affgrid"
            if christmastwo20 == True:
                text _("{color=00C803}Potentially Lucrative Nude {b}✓{/b}{/color}")
            else:
                text _("Potentially Lucrative Nude {b}{size=-10}Complete Main Event: {i}Glued to the Sky{/i}")
            if beachwars2 == True:
                text _("{color=00C803}Sexual Intercourse {b}✓{/b}{/color}")
            else:
                text _("Sexual Intercourse {b}{size=-10}Complete Main Event: {i}When You Snap{/i}")

            #########################
            text "\n"

            text "{color=#9A6BA1}{u}Osako Osaka{/color}" style "affgrid"

            text "{color=#9A6BA1}Profile Outfits{/color}" style "affgrid"
            if has_care_package("March 2025"):
                text _("{color=00C803}Casual (Alternate Hair) {b}✓{/b}{/color}")
            else:
                text _("Casual (Alternate Hair) {b}{size=-10}LiL Fanfest 25 Reward")

            #########################
            text "\n"

            text "{color=#365D4C}{u}Sara Sakakibara{/color}" style "affgrid"

            text "{color=#365D4C}Profile Outfits{/color}" style "affgrid"
            if sarapatgasm == True:
                text _("{color=00C803}Pajamas {b}✓{/b}{/color}")
            else:
                text _("Pajamas {b}{size=-10}Bring Sara to Orgasm Via Headpatting")
            if has_care_package("March 2025"):
                text _("{color=00C803}Idol {b}✓{/b}{/color}")
            else:
                text _("Idol {b}{size=-10}LiL Fanfest 25 Reward")


            text "{color=#365D4C}Animation Outfits{/color}" style "affgrid"
            if sara_love >= 25:
                text _("{color=00C803}Work Uniform {b}✓{/b}{/color}")
            else:
                text _("Work Uniform {b}{size=-10}Achieve 25 Affection")
            if sara_lust >= 20:
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}Achieve 20 Lust")
            if sara_lust >= 40:
                text _("{color=00C803}Nurse {b}✓{/b}{/color}")
            else:
                text _("Nurse {b}{size=-10}Achieve 40 Lust")
            if christmas7 == True:
                text _("{color=00C803}Winter Clothes {b}✓{/b}{/color}")
            else:
                text _("Winter Clothes {b}{size=-10}Complete Main Event: {i}Fireworks, Chicken, and the Innate Fear of Death")

            text "{color=#365D4C}Picture Messages{/color}" style "affgrid"
            if sara_lust >= 20:
                text _("{color=00C803}A Cougar On the Prowl {b}✓{/b}{/color}")
            else:
                text _("A Cougar On the Prowl {b}{size=-10}Achieve 20 Lust")
            if bathhouse25 == True:
                text _("{color=00C803}Best Non-Sexually Involved Friends Forever {b}✓{/b}{/color}")
            else:
                text _("Best Non-Sexually Involved Friends Forever {b}{size=-10}Complete Io's Event: {i}Work Less, Not Hard{/i}")                             

            #########################
            text "\n"

            text "{color=#f0ca8c}{u}Tsukasa Tsukioka{/color}" style "affgrid"

            text "{color=#f0ca8c}Profile Outfits{/color}" style "affgrid"
            if has_care_package("March 2025"):
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}LiL Fanfest 25 Reward")

            #########################
            text "\n"

            text "{color=#540087}{u}Wakana Watabe{/color}" style "affgrid"

            text "{color=#540087}Profile Outfits{/color}" style "affgrid"
            if has_care_package("March 2025"):
                text _("{color=00C803}Swimsuit {b}✓{/b}{/color}")
            else:
                text _("Swimsuit {b}{size=-10}LiL Fanfest 25 Reward")

            #########################
            text "\n"

            text "{color=#CDCDCD}{u}Yuki Yamaguchi{/color}" style "affgrid"

            text "{color=#CDCDCD}Profile Outfits{/color}" style "affgrid"
            if has_care_package("August 2023"):
                text _("{color=00C803}Gym Clothes {b}✓{/b}{/color}")
            else:
                text _("Gym Clothes {b}{size=-10}August 2023 Care Package Reward")
