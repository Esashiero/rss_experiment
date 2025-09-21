init -1 python:

### DO NOT TOUCH
    installed_profile_images = dict()

    class ProfileOutfit:
        def __init__(self, name, file):
            self.name = name
            self.file = file

        def __repr__(self):
            return "(%s, %s)" % (self.name, self.file)

    def install_profile_outfit(character_first_name, outfit_name, file):
        char_outfits = installed_profile_images.setdefault(character_first_name.lower(), list())
        char_outfits.append(ProfileOutfit(outfit_name, file))

    def next_profile_outfit(character_first_name, current, unlocked=list()):
        package_outfits = installed_profile_images.get(character_first_name.lower(), list())

        all_choices = unlocked + package_outfits

        if current is None :
            return all_choices[(1 % len(all_choices))].file

        for idx, outfit in enumerate(all_choices) :
            if current == outfit.name or current == outfit.file :
                return all_choices[(idx + 1) % len(all_choices)].file

        return all_choices[0].file



### Add girls code after here

    def chika_next_outfit() :
        global chikamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuchika.png"),
            ProfileOutfit("Winter", "game_menuchikawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if chikapatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menuchikapajama.png"))
        #
        #

        chikamenuoutfit = next_profile_outfit("Chika", chikamenuoutfit, unlocked_outfits)

    def yumi_next_outfit() :
        global yumimenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuyumi.png"),
            ProfileOutfit("Winter", "game_menuyumiwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if christmas7 :
            unlocked_outfits.append(ProfileOutfit("Christmas", "game_menuyumixmas.png"))
        #
        #

        yumimenuoutfit = next_profile_outfit("Yumi", yumimenuoutfit, unlocked_outfits)

    def ayane_next_outfit() :
        global ayanemenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuayane.png"),
            ProfileOutfit("Winter", "game_menuayanewinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if ayanepatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menuayanepajama.png"))
        if persistent.alexisevent :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menualexis.png"))
        #
        #

        ayanemenuoutfit = next_profile_outfit("Ayane", ayanemenuoutfit, unlocked_outfits)


    def sana_next_outfit() :
        global sanamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menusana.png"),
            ProfileOutfit("Winter", "game_menusanawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if sanapatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menusanapajama.png"))
        #
        #

        sanamenuoutfit = next_profile_outfit("Sana", sanamenuoutfit, unlocked_outfits)

    def makoto_next_outfit() :
        global makotomenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menumakoto.png"),
            ProfileOutfit("Winter", "game_menumakotowinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if makotopatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        makotomenuoutfit = next_profile_outfit("Makoto", makotomenuoutfit, unlocked_outfits)

    def miku_next_outfit() :
        global mikumenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menumiku.png"),
            ProfileOutfit("Winter", "game_menumikuwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if mikupatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumikupajamas.png"))
        #
        #

        mikumenuoutfit = next_profile_outfit("Miku", mikumenuoutfit, unlocked_outfits)

    def rin_next_outfit() :
        global rinmenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menurin.png"),
            ProfileOutfit("Winter", "game_menurinwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if christmas7 :
            unlocked_outfits.append(ProfileOutfit("Christmas", "game_menurinxmas.png"))
        #
        #

        rinmenuoutfit = next_profile_outfit("Rin", rinmenuoutfit, unlocked_outfits)

    def futaba_next_outfit() :
        global futabamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menufutaba.png"),
            ProfileOutfit("Winter", "game_menufutabawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if futabapatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menufutabapajama.png"))
        #
        #

        futabamenuoutfit = next_profile_outfit("Futaba", futabamenuoutfit, unlocked_outfits)

    def ami_next_outfit() :
        global amimenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuami.png"),
            ProfileOutfit("Winter", "game_menuamiwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if amipatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menuamipajama.png"))
        if amyevent :
            unlocked_outfits.append(ProfileOutfit("Amy", "game_menuamy.png"))
        #
        #

        amimenuoutfit = next_profile_outfit("Ami", amimenuoutfit, unlocked_outfits)

    def maya_next_outfit() :
        global mayamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menumaya.png"),
            ProfileOutfit("Winter", "game_menumayawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if christmas7 :
            unlocked_outfits.append(ProfileOutfit("Christmas", "game_menumayaxmas.png"))
        if maya2profile :
            unlocked_outfits.append(ProfileOutfit("Maya 2", "game_menumaya2.png"))
        #
        #

        mayamenuoutfit = next_profile_outfit("Maya", mayamenuoutfit, unlocked_outfits)

    def molly_next_outfit() :
        global mollymenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menumolly.png"),
            ProfileOutfit("Winter", "game_menumollywinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if mollypatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumollypajama.png"))
        #
        #

        mollymenuoutfit = next_profile_outfit("Molly", mollymenuoutfit, unlocked_outfits)

    def tsuneyo_next_outfit() :
        global tsuneyomenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menutsuneyo.png"),
            ProfileOutfit("Winter", "game_menutsuneyowinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if noodlespatgasm :
            unlocked_outfits.append(ProfileOutfit("Noodles", "game_menutsuneyonoodles.png"))
        #
        #

        tsuneyomenuoutfit = next_profile_outfit("Tsuneyo", tsuneyomenuoutfit, unlocked_outfits)

    def uta_next_outfit() :
        global utamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuuta.png"),
            ProfileOutfit("Winter", "game_menuutawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        utamenuoutfit = next_profile_outfit("Uta", utamenuoutfit, unlocked_outfits)

    def io_next_outfit() :
        global iomenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuio.png"),
            ProfileOutfit("Winter", "game_menuiowinter.png"),
            ProfileOutfit("Casual (Original Design)", "game_menuioold.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        iomenuoutfit = next_profile_outfit("Io", iomenuoutfit, unlocked_outfits)

    def nodoka_next_outfit() :
        global nodokamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menunodoka.png"),
            ProfileOutfit("Winter", "game_menunodokawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if nodokapatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menunodokapajama.png"))
        #
        #

        nodokamenuoutfit = next_profile_outfit("Nodoka", nodokamenuoutfit, unlocked_outfits)

    def otoha_next_outfit() :
        global otohamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuotoha.png"),
            ProfileOutfit("Winter", "game_menuotohawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        # if sarapatgasm :
        #     unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menusarapajama.png"))
        #
        #

        otohamenuoutfit = next_profile_outfit("Otoha", otohamenuoutfit, unlocked_outfits)

    def yasu_next_outfit() :
        global yasumenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuyasu.png"),
            ProfileOutfit("Winter", "game_menuyasuwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        yasumenuoutfit = next_profile_outfit("Yasu", yasumenuoutfit, unlocked_outfits)

    def touka_next_outfit() :
        global toukamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menutouka.png"),
            ProfileOutfit("Winter", "game_menutoukawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        toukamenuoutfit = next_profile_outfit("Touka", toukamenuoutfit, unlocked_outfits)

    def noriko_next_outfit() :
        global norikomenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menunoriko.png"),
            ProfileOutfit("Winter", "game_menunorikowinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if norikopatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menunorikopajama.png"))
        #
        #

        norikomenuoutfit = next_profile_outfit("Noriko", norikomenuoutfit, unlocked_outfits)

    def kirin_next_outfit() :
        global kirinmenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menukirin.png"),
            ProfileOutfit("Winter", "game_menukirinwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if kirinpatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menukirinpajama.png"))
        #
        #

        kirinmenuoutfit = next_profile_outfit("Kirin", kirinmenuoutfit, unlocked_outfits)

    def sara_next_outfit() :
        global saramenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menusara.png"),
            ProfileOutfit("Winter", "game_menusarawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if sarapatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menusarapajama.png"))
        #
        #

        saramenuoutfit = next_profile_outfit("Sara", saramenuoutfit, unlocked_outfits)

    def haruka_next_outfit() :
        global harukamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuharuka.png"),
            ProfileOutfit("Winter", "game_menuharukawinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if harukapatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menuharukapajama.png"))
        #
        #

        harukamenuoutfit = next_profile_outfit("Haruka", harukamenuoutfit, unlocked_outfits)

    def kaori_next_outfit() :
        global kaorimenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menukaori.png"),
            ProfileOutfit("Winter", "game_menukaoriwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if nyaorifit :
            unlocked_outfits.append(ProfileOutfit("Nyaori", "game_menunyaori.png"))
        if halloweenfive8 :
            unlocked_outfits.append(ProfileOutfit("Meowri", "game_menumeowri.png"))
        #
        #

        kaorimenuoutfit = next_profile_outfit("Kaori", kaorimenuoutfit, unlocked_outfits)

    def chinami_next_outfit() :
        global chinamimenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuchinami.png"),
            ProfileOutfit("Winter", "game_menuchinamiwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        chinamimenuoutfit = next_profile_outfit("Chinami", chinamimenuoutfit, unlocked_outfits)

    def karin_next_outfit() :
        global karinmenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menukarin.png"),
            ProfileOutfit("Winter", "game_menukarinwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        karinmenuoutfit = next_profile_outfit("Karin", karinmenuoutfit, unlocked_outfits)

    def maki_next_outfit() :
        global makimenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menumaki.png"),
            ProfileOutfit("Winter", "game_menumakiwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if makipatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakipajamas.png"))
        #
        #

        makimenuoutfit = next_profile_outfit("Maki", makimenuoutfit, unlocked_outfits)

    def yuki_next_outfit() :
        global yukimenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuyuki.png"),
            ProfileOutfit("Winter", "game_menuyukiwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        yukimenuoutfit = next_profile_outfit("Yuki", yukimenuoutfit, unlocked_outfits)

    def niki_next_outfit() :
        global nikimenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuniki.png"),
            ProfileOutfit("Winter", "game_menunikiwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        if nikipatgasm :
            unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menunikipajamas.png"))
        #
        #

        nikimenuoutfit = next_profile_outfit("Niki", nikimenuoutfit, unlocked_outfits)

    def wakana_next_outfit() :
        global wakanamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuwakanawinter.png"),
            ProfileOutfit("Winter", "game_menuwakanawinter2.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        wakanamenuoutfit = next_profile_outfit("Wakana", wakanamenuoutfit, unlocked_outfits)

    def osako_next_outfit() :
        global osakomenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuosako.png"),
            ProfileOutfit("Winter", "game_menuosakowinter.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        osakomenuoutfit = next_profile_outfit("Osako", osakomenuoutfit, unlocked_outfits)

    def tsubasa_next_outfit() :
        global tsubasamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menutsubasa.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        tsubasamenuoutfit = next_profile_outfit("Tsubasa", tsubasamenuoutfit, unlocked_outfits)

    def tsukasa_next_outfit() :
        global tsukasamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menutsukasa.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        tsukasamenuoutfit = next_profile_outfit("Tsukasa", tsukasamenuoutfit, unlocked_outfits)

    def imani_next_outfit() :
        global imanimenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menuimani.png"),
            ProfileOutfit("Winter", "game_menuimaniwinter.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        imanimenuoutfit = next_profile_outfit("Imani", imanimenuoutfit, unlocked_outfits)

    def rika_next_outfit() :
        global rikamenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menurika.png"),
        ]


        ### commented out conditional unlock example
        #
        #if makotopatgasm :
        #    unlocked_outfits.append(ProfileOutfit("Pajamas", "game_menumakotopajama.png"))
        #
        #

        rikamenuoutfit = next_profile_outfit("Rika", rikamenuoutfit, unlocked_outfits)

    def nao_next_outfit() :
        global naomenuoutfit

        unlocked_outfits = [
            ProfileOutfit("Casual", "game_menunaocasual.png"),
            ProfileOutfit("Hoodie", "game_menunaohoodie.png"),
        ]


        ### commented out conditional unlock example
        #
        if nyaofit :
            unlocked_outfits.append(ProfileOutfit("Nyaori", "game_menunyao.png"))
        #
        #

        naomenuoutfit = next_profile_outfit("Nao", naomenuoutfit, unlocked_outfits)
