screen dlc():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("DLC"), scroll="viewport"):

        style_prefix "event"

        vbox:

            if not has_care_package("November 2022"):
                textbutton _("{u}Care Package #1 ~ November 2022 ($3.00)"):
                    text_style "dlcbutton"
                    action OpenURL("https://selebus.booth.pm/items/4630939")

                text "{u}In-Game Content:" style "dlcayane"
                text "Animation: Loli Kirin BJ (Invite Over Variant ~ No New Text)"
                text "Animation: Milf Ayane Prone Bone (Invite Over Variant ~ No New Text)"
                text "Picture Message: Teen Niki Blowjob"
                text "Scene Commentary: Prisoner"
                text "Main Menu Image: Maya (Swimsuit)"
                text "{u}Additional Bonus Content:" style "dlcayane"
                text "Ami Arakawa ~ Character Design Sheets (4)"
                text "Sara Sakakibara ~ Character Info Sheet"
            else:
                text "{u}Care Package #1 ~ November 2022 (Unlocked)" style "dlcmaya"

                text "{u}In-Game Content:" style "dlcami"
                text "{color=00C803}Animation: Loli Kirin BJ (Invite Over Variant ~ No New Text) {b}✓{/b}"
                text "{color=00C803}Animation: Milf Ayane Prone Bone (Invite Over Variant ~ No New Text) {b}✓{/b}"
                text "{color=00C803}Picture Message: Teen Niki Blowjob {b}✓{/b}"
                text "{color=00C803}Scene Commentary: Prisoner {b}✓{/b}"
                text "{color=00C803}Main Menu Image: Maya (Swimsuit) {b}✓{/b}"
                text "{u}Additional Bonus Content:" style "dlcami"
                text "{color=00C803}Ami Arakawa ~ Character Design Sheets (4) {b}✓{/b}"
                text "{color=00C803}Sara Sakakibara ~ Character Info Sheet {b}✓{/b}"

            text "\n"

            if not has_care_package("December 2022"):
                textbutton _("{u}Care Package #2 ~ December 2022 ($3.00)"):
                    text_style "dlcbutton"
                    action OpenURL("https://selebus.booth.pm/items/4630948")

                text "{u}In-Game Content:" style "dlcayane"
                text "Animation: Loli Futaba Christmas Sex"
                text "Profile Outfit: Otoha (Christmas Variant)"
                text "Profile Outfit: Molly (Christmas Variant)"
                text "Profile Outfit: Sana (Christmas Variant)"
                text "Scene Commentary: Stray Cat"
                text "Main Menu Image: Ami (Christmas)"
                text "{u}Additional Bonus Content:" style "dlcayane"
                text "Rin Rokuhara ~ Character Design Sheets (4)"
                text "Kaori Kadowaki ~ Character Info Sheet"
            else:
                text "{u}Care Package #2 ~ December 2022 (Unlocked)" style "dlcmaya"

                text "{u}In-Game Content:" style "dlcami"
                text "{color=00C803}Animation: Loli Futaba Christmas Sex {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Otoha (Christmas Variant) {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Molly (Christmas Variant) {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Sana (Christmas Variant) {b}✓{/b}"
                text "{color=00C803}Scene Commentary: Stray Cat {b}✓{/b}"
                text "{color=00C803}Main Menu Image: Ami (Christmas) {b}✓{/b}"
                text "{u}Additional Bonus Content:" style "dlcami"
                text "{color=00C803}Rin Rokuhara ~ Character Design Sheets (4) {b}✓{/b}"
                text "{color=00C803}Kaori Kadowaki ~ Character Info Sheet {b}✓{/b}"

            text "\n"

            if not has_care_package("January 2023"):
                textbutton _("{u}Care Package #3 ~ January 2023 ($3.00)"):
                    text_style "dlcbutton"
                    action OpenURL("https://selebus.booth.pm/items/4646968")

                text "{u}In-Game Content:" style "dlcayane"
                text "Animation: Loli Maya Handjob (Shrine Maiden)"
                text "Picture Message: Older Uta Is Needy"
                text "Profile Outfit: Ayane (Kimono)"
                text "Profile Outfit: Ami (Kimono)"
                text "Scene Commentary: Bluejay"
                text "Main Menu Image: Chika (Shrine Visit)"
                text "{u}Additional Bonus Content:" style "dlcayane"
                text "Io Ichimonji ~ Character Design Sheets (4)"
                text "Maki Miyamura ~ Character Info Sheet"
            else:
                text "{u}Care Package #3 ~ January 2023 (Unlocked)" style "dlcmaya"

                text "{u}In-Game Content:" style "dlcami"
                text "{color=00C803}Animation: Loli Maya Handjob (Shrine Maiden) {b}✓{/b}"
                text "{color=00C803}Picture Message: Older Uta Is Needy {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Ayane (Kimono) {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Ami (Kimono) {b}✓{/b}"
                text "{color=00C803}Scene Commentary: Bluejay {b}✓{/b}"
                text "{color=00C803}Main Menu Image: Chika (Shrine Visit) {b}✓{/b}"
                text "{u}Additional Bonus Content:" style "dlcami"
                text "{color=00C803}Io Ichimonji ~ Character Design Sheets (4) {b}✓{/b}"
                text "{color=00C803}Maki Miyamura ~ Character Info Sheet {b}✓{/b}"

            text "\n"

            if not has_care_package("February 2023"):
                textbutton _("{u}Care Package #4 ~ February 2023 ($3.00)"):
                    text_style "dlcbutton"
                    action OpenURL("https://selebus.booth.pm/items/4721011")

                text "{u}In-Game Content:" style "dlcayane"
                text "Animation: Older Chinami Love Hotel Sex"
                text "Picture Message: Loli Noriko's Banana"
                text "Advertisement: Loli Tsuneyo For Sale"
                text "Scene Commentary: Delirium"
                text "Main Menu Image: Rin (Valentine's Date)"
                text "{u}Additional Bonus Content:" style "dlcayane"
                text "Miku Maruyama ~ Character Design Sheets (4)"
                text "Chika Chosokabe ~ Character Info Sheet"
            else:
                text "{u}Care Package #4 ~ February 2023 (Unlocked)" style "dlcmaya"

                text "{u}In-Game Content:" style "dlcami"
                text "{color=00C803}Animation: Older Chinami Love Hotel Sex {b}✓{/b}"
                text "{color=00C803}Picture Message: Loli Noriko's Banana {b}✓{/b}"
                text "{color=00C803}Advertisement: Loli Tsuneyo For Sale {b}✓{/b}"
                text "{color=00C803}Scene Commentary: Delirium {b}✓{/b}"
                text "{color=00C803}Main Menu Image: Rin (Valentine's Date) {b}✓{/b}"
                text "{u}Additional Bonus Content:" style "dlcami"
                text "{color=00C803}Miku Maruyama ~ Character Design Sheets (4) {b}✓{/b}"
                text "{color=00C803}Chika Chosokabe ~ Character Info Sheet {b}✓{/b}"

            text "\n"

            if not has_care_package("March 2023"):
                textbutton _("{u}Care Package #5 ~ March 2023 ($3.00)"):
                    text_style "dlcbutton"
                    action OpenURL("https://selebus.booth.pm/items/4881629")

                text "{u}In-Game Content:" style "dlcayane"
                text "Animation: Loli Niki Fingering (Invite Over Variant ~ No New Text)"
                text "Animation: Teen Sara Doggystyle (Invite Over Variant ~ No New Text)"
                text "Scene Commentary: This Town Has Two Halves"
                text "Main Menu Image: Uta (Nude Gravure Pic)"
                text "{u}Additional Bonus Content:" style "dlcayane"
                text "Nodoka Nagasawa ~ Character Design Sheets (4)"
                text "Karin Kanda ~ Character Info Sheet"
                text "Uta Ushibori ~ Gravure Photoset (8)"
            else:
                text "{u}Care Package #5 ~ March 2023 (Unlocked)" style "dlcmaya"

                text "{u}In-Game Content:" style "dlcami"
                text "{color=00C803}Animation: Loli Niki Fingering (Invite Over Variant ~ No New Text) {b}✓{/b}"
                text "{color=00C803}Animation: Teen Sara Doggystyle (Invite Over Variant ~ No New Text) {b}✓{/b}"
                text "{color=00C803}Scene Commentary: This Town Has Two Halves {b}✓{/b}"
                text "{color=00C803}Main Menu Image: Uta (Nude Gravure Pic) {b}✓{/b}"
                text "{u}Additional Bonus Content:" style "dlcami"
                text "{color=00C803}Nodoka Nagasawa ~ Character Design Sheets (4) {b}✓{/b}"
                text "{color=00C803}Karin Kanda ~ Character Info Sheet {b}✓{/b}"
                text "{color=00C803}Uta Ushibori ~ Gravure Photoset (8) {b}✓{/b}"

            text "\n"

            if not has_care_package("April 2023"):
                textbutton _("{u}Care Package #6 ~ April 2023 ($3.00)"):
                    text_style "dlcbutton"
                    action OpenURL("https://selebus.booth.pm/items/5053650")

                text "{u}In-Game Content:" style "dlcayane"
                text "Animation: Loli Ami Ekiben"
                text "Picture Message: Older Miku Shota Gangbang NTR"
                text "Profile Outfit: Makoto (Vampire)"
                text "Profile Outfit: Touka (Sadako)"
                text "Main Menu Image: Molly (Fischl Cosplay)"
                text "{u}Additional Bonus Content:" style "dlcayane"
                text "Futaba Fukuyama ~ Character Design Sheets (4)"
                text "Osako Osaka ~ Character Info Sheet"
                text "Uta Ushibori's Sensei Love Ranking (Pages 1-7)"
            else:
                text "{u}Care Package #6 ~ April 2023 (Unlocked)" style "dlcmaya"

                text "{u}In-Game Content:" style "dlcami"
                text "{color=00C803}Animation: Loli Ami Ekiben {b}✓{/b}"
                text "{color=00C803}Picture Message: Older Miku Shota Gangbang NTR {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Makoto (Vampire) {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Touka (Sadako) {b}✓{/b}"
                text "{color=00C803}Main Menu Image: Molly (Fischl Cosplay) {b}✓{/b}"
                text "{u}Additional Bonus Content:" style "dlcami"
                text "{color=00C803}Futaba Fukuyama ~ Character Design Sheets (4) {b}✓{/b}"
                text "{color=00C803}Osako Osaka ~ Character Info Sheet {b}✓{/b}"
                text "{color=00C803}Uta Ushibori's Sensei Love Ranking (Pages 1-7) {b}✓{/b}"

            text "\n"

            if not has_care_package("June 2023"):
                textbutton _("{u}Care Package #7 ~ June 2023 (Available To Subscribers)"):
                    text_style "dlcbutton"
                    action OpenURL("https://subscribestar.adult/selebus")

                text "{u}In-Game Content:" style "dlcayane"
                text "Animation: Teen Tsukasa Blowjob"
                text "Picture Message: Older Maya is Conceited AF"
                text "Advertisement: Loli Tsubasa For Sale"
                text "Main Menu Image: Io (Bath House)"
                text "{u}Additional Bonus Content:" style "dlcayane"
                text "Touka Tsukioka ~ Character Design Sheets (4)"
                text "Noriko Nakayama ~ Character Info Sheet"
                text "Uta Ushibori's Sensei Love Ranking (Pages 8-13)"
            else:
                text "{u}Care Package #7 ~ June 2023 (Unlocked)" style "dlcmaya"

                text "{u}In-Game Content:" style "dlcami"
                text "{color=00C803}Animation: Teen Tsukasa Blowjob {b}✓{/b}"
                text "{color=00C803}Picture Message: Older Maya is Conceited AF {b}✓{/b}"
                text "{color=00C803}Advertisement: Loli Tsubasa For Sale {b}✓{/b}"
                text "{color=00C803}Main Menu Image: Io (Bath House) {b}✓{/b}"
                text "{u}Additional Bonus Content:" style "dlcami"
                text "{color=00C803}Touka Tsukioka ~ Character Design Sheets (4) {b}✓{/b}"
                text "{color=00C803}Noriko Nakayama ~ Character Info Sheet {b}✓{/b}"
                text "{color=00C803}Uta Ushibori's Sensei Love Ranking (Pages 8-13) {b}✓{/b}"

            text "\n"

            if not has_care_package("August 2023"):
                textbutton _("{u}Care Package #8 ~ August 2023 (Available To Subscribers)"):
                    text_style "dlcbutton"
                    action OpenURL("https://subscribestar.adult/selebus")

                text "{u}In-Game Content:" style "dlcayane"
                text "Animation: Older Ami/Older Molly Tribadism"
                text "Scene Commentary: Too Blind to See"
                text "Profile Outfit: Futaba (Gym Clothes)"
                text "Profile Outfit: Rin (Gym Clothes)"
                text "Profile Outfit: Nodoka (Gym Clothes)"
                text "Profile Outfit: Yuki (Gym Clothes)"
                text "Profile Outfit: Karin (Gym Clothes)"
                text "Main Menu Image: Wakana (Maid Upskirt)"
                text "{u}Additional Bonus Content:" style "dlcayane"
                text "Yumi Yamaguchi ~ Character Design Sheets (4)"
                text "Ayane Amamiya ~ Character Info Sheet"
            else:
                text "{u}Care Package #8 ~ August 2023 (Unlocked)" style "dlcmaya"

                text "{u}In-Game Content:" style "dlcami"
                text "{color=00C803}Animation: Older Ami/Older Molly Tribadism {b}✓{/b}"
                text "{color=00C803}Scene Commentary: Too Blind to See {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Futaba (Gym Clothes) {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Rin (Gym Clothes) {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Nodoka (Gym Clothes) {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Yuki (Gym Clothes) {b}✓{/b}"
                text "{color=00C803}Profile Outfit: Karin (Gym Clothes) {b}✓{/b}"
                text "{color=00C803}Main Menu Image: Wakana (Maid Upskirt) {b}✓{/b}"
                text "{u}Additional Bonus Content:" style "dlcami"
                text "{color=00C803}Yumi Yamaguchi ~ Character Design Sheets (4) {b}✓{/b}"
                text "{color=00C803}Ayane Amamiya ~ Character Info Sheet {b}✓{/b}"
