################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style aff:
    size 35
    font "YuGothM.ttc"

style event_button:
    size 33
    font "YuGothM.ttc"
    color "#00C803"
    hover_color "#FF00F7"
    padding (0, 0)
    margin(0, 0)

style affgrid:
    size 35
    font "YuGothM.ttc"
    padding (0, 0)
    margin(0, 0)
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style mybutton:
    size 35
    font "YuGothM.ttc"
    color "#00C803"
    hover_color "#FF00F7"
    padding (0, 0)
    margin(0, 0)

style dlcbutton:
    size 35
    font "YuGothM.ttc"
    color "#ff4dd2"
    hover_color "#00bab1"
    padding (0, 0)
    margin(0, 0)
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style dlcmaya:
    size 35
    font "YuGothM.ttc"
    color "#18b500"
    padding (0, 0)
    margin(0, 0)
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style dlcami:
    size 35
    font "YuGothM.ttc"
    color "#ff4dd2"
    padding (0, 0)
    margin(0, 0)
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style dlcayane:
    size 35
    font "YuGothM.ttc"
    color "#00bab1"
    padding (0, 0)
    margin(0, 0)
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style profile:
    size 55
    #font "yugothm.ttc"
    font "hellowins.ttf"
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style progress:
    size 32
    #font "yugothm.ttc"
    font "YuGothM.ttc"
    #outlines [ (absolute(1.3), "#000", absolute(0), absolute(0)) ]

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

#screen choice(items):
#    style_prefix "choice"
#
#    vbox:
#        for i in items:
#            textbutton i.caption action i.action

screen choice(items):
    style_prefix "choice"

    if len(items) >= 10:
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"

            xsize gui.choice_button_width
            ysize config.screen_height - 180

            xalign 0.5
            yalign 0.5

            vbox:
                for i in items:
                    textbutton i.caption action i.action
    else:
        vbox:
            for i in items:
                textbutton i.caption action i.action

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Event Tracker") action ShowMenu('eventtracker11')
            textbutton _("Girls") action ShowMenu('eventtrackercharahub')
            textbutton _("Progress") action ShowMenu('affection')
            textbutton _("Unlockables") action ShowMenu('unlockables')
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            if not renpy.variant("mobile"):
                textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

            textbutton _("Event Tracker") action ShowMenu('eventtracker11')

            textbutton _("Main Girls") action ShowMenu('eventtrackermaincharahub')

            textbutton _("Side Girls") action ShowMenu('eventtrackersidecharahub')

            if not renpy.variant("mobile") and bonus == True:
                textbutton _("Guide/Wiki") action OpenURL("https://lessonsinlove.wiki/")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if main_menu:
            textbutton _("About") action ShowMenu("about")

            textbutton _("Donate") action OpenURL("https://subscribestar.adult/selebus")

        textbutton _("Merch Store") action OpenURL("https://selebus-inc.myshopify.com/")

        if main_menu:
            textbutton "Jukebox" action ShowMenu("music_room")

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")

        #if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
        textbutton _("Quit") action Quit(confirm=not main_menu)

    textbutton _("{size=+20}{b}DLC"):
        action ShowMenu("dlc")
        xpos 266 ypos 564


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    if persistent.main_menu_image is not None and renpy.loadable(persistent.main_menu_image) :
        add persistent.main_menu_image
    else :
        add gui.main_menu_background

    add gui.main_menu_overlay

    if len(installed_care_packages) > 0:
        textbutton _("Change Menu Image"):
            action ShowMenu("main_menu_image_picker")
            xpos 60 ypos 900

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            if bonus == True:
                text "[config.name!t]":
                    style "main_menu_title"
            else:
                text "Hug Simulator":
                    style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

screen main_menu_image_picker:
    tag menu

    use game_menu(_("Picker"), scroll="viewport"):

        style_prefix "aff"

        vpgrid :
            cols 2
            align (0.6, 0.45)
            spacing 80

            imagebutton:
                idle im.FactorScale("gui/main_menu.png", 0.3, bilinear=True)
                action [SetVariable("persistent.main_menu_image", None), Return()]

            for img in installed_menu_images:
                imagebutton:
                    idle im.FactorScale(img.file, 0.3, bilinear=True)
                    action [SetVariable("persistent.main_menu_image", img.file), Return()]


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

#style main_menu_frame:
    #xsize 420
    #yfill True
    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45



## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            if bonus == True:
                label "[config.name!t]"
            else:
                label "Hug Simulator"

            text _("Version [config.version!t]")

            if bonus == True:
                text _("\nThank you for downloading Lessons in Love!\nAll character models and scenes in this game were created using Koikatsu by Illusion.")
            else:
                text _("\nThank you for downloading THE LEGEND OF THE HUGGY BOY!\nAll character models and scenes in this game were created using Koikatsu by Illusion.")

            text _("Please support them as well as the many modders and community members who have contributed to Koikatsu and made games like this possible.\n")
            text _("{b}Music:{/b} MusMus, Bensound, ASOBEAT, Ramine, Bungakuseinen, Bubblebeats, SougetsuOn, 369Musiq, and various others.")
            text _("{b}Menu Song:{/b} 'Shining Star' performed by Shiho. Written and composed by Koichi Morita")
            text _("{b}Everything Else:{/b} Selebus\n")
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

screen affection():

    tag menu

    $ v11check()

    use game_menu(_("Progress"), scroll="viewport"):

        style_prefix "profile"

        vbox:
            if ami_love >= 0:
                if resetsix4 == True:
                    if chap1point + chap2point + chap3point + chap3miss + chap4point + chap4miss != 392:
                        text "Main Events Available!"  style "affgrid"
                    if happypoint + happymiss != 20:
                        text "Secret Events Available!"  style "affgrid"
                elif chapthreeactive == True:
                    if chap1point + chap2point + chap3point + chap3miss != 304:
                        text "Main Events Available!"  style "affgrid"
                    if happypoint + happymiss != 17:
                        text "Secret Events Available!"  style "affgrid"
                elif hoorayanotherreset == True and chapthreeactive == False:
                    if chap1point + chap2point != 203:
                        text "Main Events Available!"  style "affgrid"
                    if happypoint + happymiss != 14:
                        text "Secret Events Available!"  style "affgrid"
                else:
                    text "Main Events Available!"  style "affgrid"
                    if happypoint + happymiss < 11:
                        text "Secret Events Available!"  style "affgrid"

                text "\n"

                grid 4 36:
                    xspacing 90
                    yspacing 20

                    text "{u}Name{/u}" style "affgrid"
                    text "{u}Affection{/u}" style "affgrid"
                    text "{u}Lust{/u}" style "affgrid"
                    text "{u}Events{/u}" style "affgrid"

                    text "{color=#ff4dd2}Ami Arakawa{/color}" style "affgrid"
                    text "{color=#ff4dd2}[ami_love]{/color}" style "affgrid"
                    text "{color=#ff4dd2}[ami_lust]{/color}" style "affgrid"
                    if amitotal == 40:
                        text "{color=#ff4dd2}[amitotal]/40 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#ff4dd2}[amitotal]/40{/color}" style "affgrid"

                    text "{color=#00bab1}Ayane Amamiya{/color}" style "affgrid"
                    text "{color=#00bab1}[ayane_love]{/color}" style "affgrid"
                    text "{color=#00bab1}[ayane_lust]{/color}" style "affgrid"
                    if ayanetotal == 42:
                        text "{color=#00bab1}[ayanetotal]/42 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#00bab1}[ayanetotal]/42{/color}" style "affgrid"

                    text "{color=#AF7F00}Chika Chosokabe{/color}" style "affgrid"
                    text "{color=#AF7F00}[chika_love]{/color}" style "affgrid"
                    text "{color=#AF7F00}[chika_lust]{/color}" style "affgrid"
                    if chikatotal == 36:
                        text "{color=#AF7F00}[chikatotal]/36 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#AF7F00}[chikatotal]/36{/color}" style "affgrid"

                    text "{color=#FF9999}Chinami Chosokabe{/color}" style "affgrid"
                    text "{color=#FF9999}[chinami_love]{/color}" style "affgrid"
                    text "{color=#FF9999}N/A{/color}" style "affgrid"
                    if chinamitotal == 13:
                        text "{color=#FF9999}[chinamitotal]/13 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#FF9999}[chinamitotal]/13{/color}" style "affgrid"

                    text "{color=#9326ff}Futaba Fukuyama{/color}" style "affgrid"
                    text "{color=#9326ff}[futaba_love]{/color}" style "affgrid"
                    text "{color=#9326ff}[futaba_lust]{/color}" style "affgrid"
                    if futabatotal == 40:
                        text "{color=#9326ff}[futabatotal]/40 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#9326ff}[futabatotal]/40{/color}" style "affgrid"

                    text "{color=#B02E8C}Haruka Hamasaki{/color}" style "affgrid"
                    text "{color=#B02E8C}[haruka_love]{/color}" style "affgrid"
                    text "{color=#B02E8C}[haruka_lust]{/color}" style "affgrid"
                    if harukatotal == 22:
                        text "{color=#B02E8C}[harukatotal]/22 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#B02E8C}[harukatotal]/22{/color}" style "affgrid"

                    text "{color=#80C9DC}Imani Imai{/color}" style "affgrid"
                    text "{color=#80C9DC}[imani_love]{/color}" style "affgrid"
                    text "{color=#80C9DC}[imani_lust]{/color}" style "affgrid"
                    if imanitotal == 11:
                        text "{color=#80C9DC}[imanitotal]/11 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#80C9DC}[imanitotal]/11{/color}" style "affgrid"

                    text "{color=#BBE3A1}Io Ichimonji{/color}" style "affgrid"
                    text "{color=#BBE3A1}[io_love]{/color}" style "affgrid"
                    text "{color=#BBE3A1}N/A{/color}" style "affgrid"
                    if iototal == 23:
                        text "{color=#BBE3A1}[iototal]/23 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#BBE3A1}[iototal]/23{/color}" style "affgrid"

                    text "{color=#4B4B4B}Kaori Kadowaki{/color}" style "affgrid"
                    text "{color=#4B4B4B}[kaori_love]{/color}" style "affgrid"
                    text "{color=#4B4B4B}[kaori_lust]{/color}" style "affgrid"
                    if kaoritotal == 18:
                        text "{color=#4B4B4B}[kaoritotal]/18 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#4B4B4B}[kaoritotal]/18{/color}" style "affgrid"

                    text "{color=#AC9D77}Karin Kanda{/color}" style "affgrid"
                    text "{color=#AC9D77}[karin_love]{/color}" style "affgrid"
                    text "{color=#AC9D77}N/A{/color}" style "affgrid"
                    if karintotal == 15:
                        text "{color=#AC9D77}[karintotal]/15 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#AC9D77}[karintotal]/15{/color}" style "affgrid"

                    text "{color=#9C8080}Kirin Kanda{/color}" style "affgrid"
                    text "{color=#9C8080}[kirin_love]{/color}" style "affgrid"
                    text "{color=#9C8080}[kirin_lust]{/color}" style "affgrid"
                    if kirintotal == 28:
                        text "{color=#9C8080}[kirintotal]/28 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#9C8080}[kirintotal]/28{/color}" style "affgrid"

                    text "{color=#3B84A9}Maki Miyamura{/color}" style "affgrid"
                    text "{color=#3B84A9}[maki_love]{/color}" style "affgrid"
                    text "{color=#3B84A9}[maki_lust]{/color}" style "affgrid"
                    if makitotal == 18:
                        text "{color=#3B84A9}[makitotal]/18 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#3B84A9}[makitotal]/18{/color}" style "affgrid"

                    text "{color=#3c55fa}Makoto Miyamura{/color}" style "affgrid"
                    text "{color=#3c55fa}[makoto_love]{/color}" style "affgrid"
                    text "{color=#3c55fa}[makoto_lust]{/color}" style "affgrid"
                    if makotototal == 39:
                        text "{color=#3c55fa}[makotototal]/39 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#3c55fa}[makotototal]/39{/color}" style "affgrid"

                    text "{color=#18b500}Maya Makinami{/color}" style "affgrid"
                    text "{color=#18b500}[maya_love]{/color}" style "affgrid"
                    text "{color=#18b500}N/A{/color}" style "affgrid"
                    if mayatotal == 32:
                        text "{color=#18b500}[mayatotal]/32 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#18b500}[mayatotal]/32{/color}" style "affgrid"

                    text "{color=#ff8112}Miku Maruyama{/color}" style "affgrid"
                    text "{color=#ff8112}[miku_love]{/color}" style "affgrid"
                    text "{color=#ff8112}[miku_lust]{/color}" style "affgrid"
                    if mikutotal == 32:
                        text "{color=#ff8112}[mikutotal]/32 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#ff8112}[mikutotal]/32{/color}" style "affgrid"

                    text "{color=#4FCB80}Molly MacCormack{/color}" style "affgrid"
                    text "{color=#4FCB80}[molly_love]{/color}" style "affgrid"
                    text "{color=#4FCB80}[molly_lust]{/color}" style "affgrid"
                    if mollytotal == 25:
                        text "{color=#4FCB80}[mollytotal]/25 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#4FCB80}[mollytotal]/25{/color}" style "affgrid"

                    text "{color=#602F2B}Nao-chan{/color}" style "affgrid"
                    text "{color=#602F2B}[nao_love]{/color}" style "affgrid"
                    text "{color=#602F2B}N/A{/color}" style "affgrid"
                    if naototal == 10:
                        text "{color=#602F2B}[naototal]/10 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#602F2B}[naototal]/10{/color}" style "affgrid"

                    text "{color=#FF0074}Niki Nakayama{/color}" style "affgrid"
                    text "{color=#FF0074}[niki_love]{/color}" style "affgrid"
                    text "{color=#FF0074}[niki_lust]{/color}" style "affgrid"
                    if nikitotal == 17:
                        text "{color=#FF0074}[nikitotal]/17 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#FF0074}[nikitotal]/17{/color}" style "affgrid"

                    text "{color=#AF89A2}Nodoka Nagasawa{/color}" style "affgrid"
                    text "{color=#AF89A2}[nodoka_love]{/color}" style "affgrid"
                    text "{color=#AF89A2}[nodoka_lust]{/color}" style "affgrid"
                    if nodokatotal == 21:
                        text "{color=#AF89A2}[nodokatotal]/21 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#AF89A2}[nodokatotal]/21{/color}" style "affgrid"

                    text "{color=#FF61A9}Noriko Nakayama{/color}" style "affgrid"
                    text "{color=#FF61A9}[noriko_love]{/color}" style "affgrid"
                    text "{color=#FF61A9}[noriko_lust]{/color}" style "affgrid"
                    if norikototal == 22:
                        text "{color=#FF61A9}[norikototal]/22 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#FF61A9}[norikototal]/22{/color}" style "affgrid"

                    text "{color=#9A6BA1}Osako Osaka{/color}" style "affgrid"
                    text "{color=#9A6BA1}[osako_love]{/color}" style "affgrid"
                    text "{color=#9A6BA1}N/A{/color}" style "affgrid"
                    if osakototal == 10:
                        text "{color=#9A6BA1}[osakototal]/10 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#9A6BA1}[osakototal]/10{/color}" style "affgrid"

                    text "{color=#B83A6A}Otoha Okakura{/color}" style "affgrid"
                    text "{color=#B83A6A}[otoha_love]{/color}" style "affgrid"
                    text "{color=#B83A6A}N/A{/color}" style "affgrid"
                    if otohatotal == 18:
                        text "{color=#B83A6A}[otohatotal]/18 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#B83A6A}[otohatotal]/18{/color}" style "affgrid"

                    text "{color=#D18E77}Rika Rokuhara{/color}" style "affgrid"
                    text "{color=#D18E77}[rika_love]{/color}" style "affgrid"
                    text "{color=#D18E77}N/A{/color}" style "affgrid"
                    if rikatotal == 8:
                        text "{color=#D18E77}[rikatotal]/8 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#D18E77}[rikatotal]/8{/color}" style "affgrid"

                    text "{color=#a30041}Rin Rokuhara{/color}" style "affgrid"
                    text "{color=#a30041}[rin_love]{/color}" style "affgrid"
                    text "{color=#a30041}N/A{/color}" style "affgrid"
                    if rintotal == 34:
                        text "{color=#a30041}[rintotal]/34 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#a30041}[rintotal]/34{/color}" style "affgrid"

                    text "{color=#005730}Sana Sakakibara{/color}" style "affgrid"
                    text "{color=#005730}[sana_love]{/color}" style "affgrid"
                    text "{color=#005730}[sana_lust]{/color}" style "affgrid"
                    if sanatotal == 33:
                        text "{color=#005730}[sanatotal]/33 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#005730}[sanatotal]/33{/color}" style "affgrid"

                    text "{color=#365D4C}Sara Sakakibara{/color}" style "affgrid"
                    text "{color=#365D4C}[sara_love]{/color}" style "affgrid"
                    text "{color=#365D4C}[sara_lust]{/color}" style "affgrid"
                    if saratotal == 20:
                        text "{color=#365D4C}[saratotal]/20 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#365D4C}[saratotal]/20{/color}" style "affgrid"

                    text "{color=#F0E68C}Touka Tsukioka{/color}" style "affgrid"
                    text "{color=#F0E68C}[touka_love]{/color}" style "affgrid"
                    text "{color=#F0E68C}N/A{/color}" style "affgrid"
                    if toukatotal == 19:
                        text "{color=#F0E68C}[toukatotal]/19 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#F0E68C}[toukatotal]/19{/color}" style "affgrid"

                    text "{color=#eae6aa}Tsubasa Tsukioka{/color}" style "affgrid"
                    text "{color=#eae6aa}[tsubasa_love]{/color}" style "affgrid"
                    text "{color=#eae6aa}N/A{/color}" style "affgrid"
                    if tsubasatotal == 12:
                        text "{color=#eae6aa}[tsubasatotal]/12 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#eae6aa}[tsubasatotal]/12{/color}" style "affgrid"

                    text "{color=#f0ca8c}Tsukasa Tsukioka{/color}" style "affgrid"
                    text "{color=#f0ca8c}[tsukasa_love]{/color}" style "affgrid"
                    text "{color=#f0ca8c}N/A{/color}" style "affgrid"
                    if tsukasatotal == 9:
                        text "{color=#f0ca8c}[tsukasatotal]/9 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#f0ca8c}[tsukasatotal]/9{/color}" style "affgrid"

                    text "{color=#C8B330}Tsuneyo Tojo{/color}" style "affgrid"
                    text "{color=#C8B330}[tsuneyo_love]{/color}" style "affgrid"
                    text "{color=#C8B330}[tsuneyo_lust]{/color}" style "affgrid"
                    if tsuneyototal == 26:
                        text "{color=#C8B330}[tsuneyototal]/26 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#C8B330}[tsuneyototal]/26{/color}" style "affgrid"

                    text "{color=#AA4588}Uta Ushibori{/color}" style "affgrid"
                    text "{color=#AA4588}[uta_love]{/color}" style "affgrid"
                    text "{color=#AA4588}N/A{/color}" style "affgrid"
                    if utatotal == 23:
                        text "{color=#AA4588}[utatotal]/23 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#AA4588}[utatotal]/23{/color}" style "affgrid"

                    text "{color=#540087}Wakana Watabe{/color}" style "affgrid"
                    text "{color=#540087}[wakana_love]{/color}" style "affgrid"
                    text "{color=#540087}N/A{/color}" style "affgrid"
                    if wakanatotal == 13:
                        text "{color=#540087}[wakanatotal]/13 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#540087}[wakanatotal]/13{/color}" style "affgrid"

                    text "{color=#74d9e9}Yasu Yasui{/color}" style "affgrid"
                    text "{color=#74d9e9}[yasu_love]{/color}" style "affgrid"
                    text "{color=#74d9e9}N/A{/color}" style "affgrid"
                    if yasutotal == 19:
                        text "{color=#74d9e9}[yasutotal]/19 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#74d9e9}[yasutotal]/19{/color}" style "affgrid"

                    text "{color=#CDCDCD}Yuki Yamaguchi{/color}" style "affgrid"
                    text "{color=#CDCDCD}[yuki_love]{/color}" style "affgrid"
                    text "{color=#CDCDCD}N/A{/color}" style "affgrid"
                    if yukitotal == 14:
                        text "{color=#CDCDCD}[yukitotal]/14 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#CDCDCD}[yukitotal]/14{/color}" style "affgrid"

                    text "{color=#d12e2e}Yumi Yamaguchi{/color}" style "affgrid"
                    text "{color=#d12e2e}[yumi_love]{/color}" style "affgrid"
                    text "{color=#d12e2e}N/A{/color}" style "affgrid"
                    if yumitotal == 32:
                        text "{color=#d12e2e}[yumitotal]/32 {b}✓{/b}{/color}" style "affgrid"
                    else:
                        text "{color=#d12e2e}[yumitotal]/32{/color}" style "affgrid"

## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

#VIPER
screen save_rename(slot):
    style_prefix "rename"
    modal True
    default desc = FileSaveName(slot)
    default new_name = desc
    if desc == "":
        $ desc = "<blank>"

    frame:
        xsize 800
        ysize 200
        xalign 0.5
        yalign 0.5
        has vbox:
            xalign 0.5
            yalign 0.5
        text "Current save name is %s. Input the new name:" % desc style "input_prompt"
        input value ScreenVariableInputValue("new_name", default=True, returnable=True)
        hbox:
            button:
                style "rename_button"
                text _("Confirm") style "rename_button_text"
                action SetVariable("save_name", new_name), FileAction(slot), Hide("save_rename")
            button:
                style "rename_button"
                text _("Cancel") style "rename_button_text"
                action Hide("save_rename")
style rename_button is gui_button
style rename_button_text is gui_button_text
#VIPER

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action SetVariable("save_name", FileSaveName(slot)), FileAction(slot)

                        #VIPER
                        if title == "Save":
                            alternate Show("save_rename", slot=slot)
                        #VIPER

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            #VIPER
            hbox:
                xalign 0.5
                yalign 0.9
                if title == "Save":
                    text "Right click a save slot to OVERWRITE IT with a new name" style "gui_text"
            #VIPER

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                        if "outlines" in h.who_args:
                            text_outlines [(absolute(1), "#000", absolute(0), absolute(0))]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

#define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "small"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()
            textbutton _("Events") action ShowMenu('eventtracker11')
            textbutton _("Girls") action ShowMenu('eventtrackercharahub')
            textbutton _("Progress") action ShowMenu('affection')
            textbutton _("Unlockables") action ShowMenu('unlockables')
            if bonus == True:
                textbutton _("Wiki") action OpenURL("https://lessonsinlove.wiki/")
            textbutton _("Hide") action HideInterface()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900


#########################
screen gallerys:
    tag menu

    use game_menu(_("{s}Memories{/s}"), scroll="viewport"):

        style_prefix "aff"

        grid 3 3:
            align (0.6, 0.45)
            spacing 80

            if roomwithtrack == True:
                imagebutton:
                    idle "clocksrep1.png"
                    hover "clocksrep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("roomwithclocks", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")

            if letterttrack == True:
                imagebutton:
                    idle "lettertrep1.png"
                    hover "lettertrep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("lettert", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")

            if swimmingtrack == True:
                imagebutton:
                    idle "sitcomrep1.png"
                    hover "sitcomrep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("swimming", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")

            if howifeeltrack == True:
                imagebutton:
                    idle "howifeelrep1.png"
                    hover "howifeelrep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("howifeel", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")

            if connecttrack == True:
                imagebutton:
                    idle "sakirep1.png"
                    hover "sakirep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("everythingisconnected", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")
            if specialclassroomtrack == True:
                imagebutton:
                    idle "breakrep1.png"
                    hover "breakrep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("specialclassroom", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")
            if ticktocktrack == True:
                imagebutton:
                    idle "ticktockrep1.png"
                    hover "ticktockrep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("ticktock", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")
            if trinity1track == True:
                imagebutton:
                    idle "trinity1track1.png"
                    hover "trinity1track2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("trinity1", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")
            if trinity2track == True:
                imagebutton:
                    idle "calmrep1.png"
                    hover "calmrep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("trinity2", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")

        hbox:
            align (0.5, 0.5)
            spacing 40
            textbutton _("Previous") action ShowMenu('gallery5') ypos 25
            textbutton _("Next") action ShowMenu('gallerys2') ypos 25

screen gallerys2:
    tag menu

    use game_menu(_("{s}Memories{/s}"), scroll="viewport"):

        style_prefix "aff"

        grid 3 3:
            align (0.6, 0.45)
            spacing 80

            if trinity3track == True:
                imagebutton:
                    idle "concernrep1.png"
                    hover "concernrep2.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action Replay("trinity3", locked=False)
            else:
                imagebutton:
                    idle "lock.png"
                    hover "lock.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Start("sarafirst")

            null
            null
            null
            null
            null
            null
            null
            null

        hbox:
            align (0.5, 0.5)
            spacing 40
            textbutton _("Previous") action ShowMenu('gallerys') ypos 25

screen maintracker():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Main Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "Main Story"
            if everyday == True:
                textbutton _("Every Day I Grow Some More {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("start", locked=False)
            else:
                text _("Every Day I Grow Some More")
            if clichebath == True:
                textbutton _("A New You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("startsleepover", locked=False)
            else:
                text _("A New You")
            if amiawake == True:
                textbutton _("Am I Awake? {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firstfriday", locked=False)
            else:
                text _("Am I Awake?")
            if firstclass == True:
                if bonus == True:
                    textbutton _("First (?) Day of School {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("thefirstclass", locked=False)
                else:
                    textbutton _("First (?) Day of College {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("thefirstclass", locked=False)
            elif bonus == True:
                text _("First (?) Day of School")
            else:
                text _("First (?) Day of College")
            if sleepover == True:
                textbutton _("Slumber Party {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("slumparty", locked=False)
            else:
                text _("Slumber Party")
            if day5 == True:
                textbutton _("The Devil Incarnate {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day5", locked=False)
            else:
                text _("The Devil Incarnate")
            if day7 == True:
                if bonus == True:
                    textbutton _("Super Secret Sex Dungeon {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("day7", locked=False)
                else:
                    textbutton _("Super Secret Dungeon {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("day7", locked=False)
            elif bonus == True:
                text _("Super Secret Sex Dungeon")
            else:
                text _("Super Secret Dungeon")
            if day8 == True:
                textbutton _("Delinquent {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day8", locked=False)
            else:
                text _("Delinquent")
            if day12 == True:
                textbutton _("Mitochondria {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day12", locked=False)
            else:
                text _("Mitochondria")
            if day14 == True:
                textbutton _("Self-Esteem {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day14", locked=False)
            else:
                text _("Self-Esteem")
            if day16 == True:
                textbutton _("Operation: Fallen Angel {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day16", locked=False)
            else:
                text _("Operation: Fallen Angel")
            if day20 == True:
                textbutton _("I Thought of You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day20", locked=False)
            else:
                text _("I Thought of You")
            if day21 == True:
                textbutton _("Not Even Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day21", locked=False)
            else:
                text _("Not Even Me")
            if day24 == True:
                textbutton _("No Romeo {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day24", locked=False)
            else:
                text _("No Romeo")
            if day26 == True:
                textbutton _("Outside of Everything {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day26", locked=False)
            else:
                text _("Outside of Everything")
            if day28 == True:
                textbutton _("Ponytail {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day28", locked=False)
            else:
                text _("Ponytail")
            if day30 == True:
                textbutton _("Drowning {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day30", locked=False)
            else:
                text _("Drowning")
            if day33 == True:
                textbutton _("So Many Voices {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day33", locked=False)
            else:
                text _("So Many Voices")
            if day36 == True:
                textbutton _("Cleaning Duty {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day36", locked=False)
            else:
                text _("Cleaning Duty")
            if day38 == True:
                textbutton _("Walk in the Park {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day38", locked=False)
            else:
                text _("Walk in the Park")
            if day40 == True:
                textbutton _("Saved by the Bell {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day40", locked=False)
            else:
                text _("Saved by the Bell")
            if day44 == True:
                textbutton _("This Town Has Two Halves {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day44", locked=False)
            else:
                text _("This Town Has Two Halves")
            if day48 == True:
                textbutton _("Little Girl {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day48", locked=False)
            else:
                text _("Little Girl")
            if day50 == True:
                textbutton _("Missing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day50", locked=False)
            else:
                text _("Missing")
            if day54 == True:
                textbutton _("The Sakakibara Diet {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day54", locked=False)
            else:
                text _("The Sakakibara Diet")
            if day56 == True:
                textbutton _("Normal Office Visit {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day56", locked=False)
            else:
                text _("Normal Office Visit")
            if day60 == True:
                textbutton _("O World (In Our Final Moments) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day60", locked=False)
            else:
                text _("O World (In Our Final Moments)")
            if day63 == True:
                textbutton _("One to Seven {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day63", locked=False)
            else:
                text _("One to Seven")
            if day65 == True:
                textbutton _("Girl-Talk {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day65", locked=False)
            else:
                text _("Girl-Talk")
            if day70 == True:
                textbutton _("The 'S' Word {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day70", locked=False)
            else:
                text _("The 'S' Word")
            if day72 == True:
                textbutton _("Weight Limit {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day72", locked=False)
            else:
                text _("Weight Limit")
            if day77 == True:
                textbutton _("Slope Intercept Form {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day77", locked=False)
            else:
                text _("Slope Intercept Form")
            if day79 == True:
                textbutton _("Scientific Research {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day79", locked=False)
            else:
                text _("Scientific Research")
            if day80 == True:
                textbutton _("Secret Ingredient {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day80", locked=False)
            else:
                text _("Secret Ingredient")
            if day83 == True:
                textbutton _("Parasite {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day83", locked=False)
            else:
                text _("Parasite")
            if day85 == True:
                textbutton _("Contractions {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day85", locked=False)
            else:
                text _("Contractions")
            if day89 == True:
                textbutton _("Milk, Eggs, and Water {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day89", locked=False)
            else:
                text _("Milk, Eggs, and Water")
            if day91 == True:
                textbutton _("Stronger I Become {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day91", locked=False)
            else:
                text _("Stronger I Become")
            if day96 == True:
                textbutton _("Recall {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day96", locked=False)
            else:
                text _("Recall")
            if day102 == True:
                textbutton _("Rewrite {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day102", locked=False)
            else:
                text _("Rewrite")
            if day103 == True:
                textbutton _("Reset {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day103", locked=False)
            else:
                text _("Reset")
            if day110 == True:
                textbutton _("Cursed Birds {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day110", locked=False)
            else:
                text _("Cursed Birds")
            if day114 == True:
                textbutton _("Human Trafficking {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day114", locked=False)
            else:
                text _("Human Trafficking")
            if day120 == True:
                textbutton _("Girl Talk Pt. II {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day120", locked=False)
            else:
                text _("Girl Talk Pt. II")
            if day121 == True:
                textbutton _("A Different View {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day121", locked=False)
            else:
                text _("A Different View")
            if day126 == True:
                textbutton _("On The Bright Side {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day126", locked=False)
            else:
                text _("On The Bright Side")
            if day128 == True:
                textbutton _("Everything Horrible {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day128", locked=False)
            else:
                text _("Everything Horrible")
            if day130 == True:
                if bonus == True:
                    textbutton _("Erotic Game Protagonist {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("day130", locked=False)
                else:
                    textbutton _("Dating Sim Protagonist {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("day130", locked=False)
            elif bonus == True:
                text _("Erotic Game Protagonist")
            else:
                text _("Dating Sim Protagonist")
            if day138 == True:
                textbutton _("Rumors {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day138", locked=False)
            else:
                text _("Rumors")
            if day140 == True:
                textbutton _("The Gem of the Emerald Isle {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day140", locked=False)
            else:
                text _("The Gem of the Emerald Isle")
            if day142 == True:
                textbutton _("Size Matters {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day142", locked=False)
            else:
                text _("Size Matters")
            if day144 == True:
                textbutton _("Tsuneyo Tojo, Stand-up Comedian {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day144", locked=False)
            else:
                text _("Tsuneyo Tojo, Stand-up Comedian")
            if day150 == True:
                textbutton _("A Proper Introduction {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day150", locked=False)
            else:
                text _("A Proper Introduction")
            if day153 == True:
                textbutton _("Supreme Overlord {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day153", locked=False)
            else:
                text _("Supreme Overlord")
            if day154 == True:
                textbutton _("Lifting the Curse {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day154", locked=False)
            else:
                text _("Lifting the Curse")
            if beachvacation1 == True:
                textbutton _("What's Done is Done {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation1", locked=False)
            else:
                text _("What's Done is Done")
            if beachvacation2 == True:
                textbutton _("All Along the Shoreline {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation2", locked=False)
            else:
                text _("All Along the Shoreline")
            if beachvacation3 == True:
                textbutton _("My Heart is Full {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation3", locked=False)
            else:
                text _("My Heart is Full")
            if beachvacation4 == True:
                textbutton _("Extra French Fries {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation4", locked=False)
            else:
                text _("Extra French Fries")
            if beachvacation5 == True:
                textbutton _("Behind a Bathroom, Under the Blazing Sun {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation5", locked=False)
            else:
                text _("Behind a Bathroom, Under the Blazing Sun")
            if beachvacation6 == True:
                textbutton _("Three Girls in a Line on the Beach {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation6", locked=False)
            else:
                text _("Three Girls in a Line on the Beach")
            if beachvacation7 == True:
                textbutton _("The Moon is Beautiful {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation7", locked=False)
            else:
                text _("The Moon is Beautiful")
            if beachvacation8 == True:
                textbutton _("The Legacy of Thaum Pt. I {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation8", locked=False)
            else:
                text _("The Legacy of Thaum Pt. I")
            if beachvacation9 == True:
                textbutton _("Summer and Winter {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation9", locked=False)
            else:
                text _("Summer and Winter")
            if beachvacation10 == True:
                textbutton _("Where Puppies Roam Free {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation10", locked=False)
            else:
                text _("Where Puppies Roam Free")
            if beachvacation11 == True:
                textbutton _("Die For What You Believe In {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation11", locked=False)
            else:
                text _("Die For What You Believe In")
            if beachvacation12 == True:
                if bonus == True:
                    textbutton _("Reverse Cowgirl {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("beachvacation12", locked=False)
                else:
                    textbutton _("Censored Event Title {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("beachvacation12", locked=False)
            elif bonus == True:
                text _("Reverse Cowgirl")
            else:
                text _("Censored Event Title")
            if beachvacation13 == True:
                textbutton _("Smile Guide {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation13", locked=False)
            else:
                text _("Smile Guide")
            if beachvacation14 == True:
                textbutton _("Prayer Position {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation14", locked=False)
            else:
                text _("Prayer Position")
            if beachvacation15 == True:
                textbutton _("Cry. Cry. Cry. {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation15", locked=False)
            else:
                text _("Cry. Cry. Cry.")
            if beachvacation16 == True:
                textbutton _("See You in the Morning {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachvacation16", locked=False)
            else:
                text _("See You in the Morning")
            if halloween1 == True:
                textbutton _("The Value of Sharing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween1", locked=False)
            else:
                text _("The Value of Sharing")
            if halloween2 == True:
                textbutton _("Guest of Honor {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween2", locked=False)
            else:
                text _("Guest of Honor")
            if halloween3 == True:
                textbutton _("The Meat has Come {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween3", locked=False)
            else:
                text _("The Meat has Come")
            if halloween4 == True:
                textbutton _("Mysterious Abundance of Chickens {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween4", locked=False)
            else:
                text _("Mysterious Abundance of Chickens")
            if halloween5 == True:
                textbutton _("Sexy Land {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween5", locked=False)
            else:
                text _("Sexy Land")
            if halloween6 == True:
                textbutton _("They're Just Lights {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween6", locked=False)
            else:
                text _("They're Just Lights")
            if halloween7 == True:
                textbutton _("Once, Twice, Ten Times {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween7", locked=False)
            else:
                text _("Once, Twice, Ten Times")
            if halloween8 == True:
                textbutton _("Mechanical Bull {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween8", locked=False)
            else:
                text _("Mechanical Bull")
            if halloween9 == True:
                textbutton _("At Least It's Not Christmas {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween9", locked=False)
            else:
                text _("At Least It's Not Christmas")
            if halloween10 == True:
                textbutton _("Samhain {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween10", locked=False)
            else:
                text _("Samhain")
            if halloween11 == True:
                textbutton _("Wicked Witch of Kumon-mi {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween11", locked=False)
            else:
                text _("Wicked Witch of Kumon-mi")
            if halloween12 == True:
                textbutton _("The Depressing Implication of Goosebumps {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween12", locked=False)
            else:
                text _("The Depressing Implication of Goosebumps")
            if halloween13 == True:
                textbutton _("Pry With a Smile {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween13", locked=False)
            else:
                text _("Pry With a Smile")
            if halloween14 == True:
                textbutton _("Kadrillionbilliontrillion {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloween14", locked=False)
            else:
                text _("Kadrillionbilliontrillion")
            if day214 == True:
                textbutton _("As Loud as a Whisper Can Be {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day214", locked=False)
            else:
                text _("As Loud as a Whisper Can Be")
            if day215 == True:
                textbutton _("Two Wooden Doors {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day215", locked=False)
            else:
                text _("Two Wooden Doors")
            if day216 == True:
                textbutton _("Happy Places {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day216", locked=False)
            else:
                text _("Happy Places")
            if day217 == True:
                textbutton _("Tradition {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day217", locked=False)
            else:
                text _("Tradition")
            if day218 == True:
                textbutton _("Stray Cat {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day218", locked=False)
            else:
                text _("Stray Cat")
            if day220 == True:
                textbutton _("There is Nothing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day220", locked=False)
            else:
                text _("There is Nothing")
            if hoorayanotherreset == True:
                textbutton _("Changing of Seasons {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("hoorayanotherreset", locked=False)
            else:
                text _("Changing of Seasons")
            textbutton _("Back") action ShowMenu('eventtracker11')

screen secrettracker():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("HAPPY SCENES"), scroll="viewport"):

        style_prefix "event"

        vbox:
            label "\n{color=141414}HAPPY SCENES{/color}"
            if roomwithtrack == True:
                textbutton _("The Room With Clocks {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("roomwithclocks", locked=False)
            else:
                text _("???")
            if letterttrack == True:
                textbutton _("The Letter 'T' {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("lettert", locked=False)
            else:
                text _("???")
            if swimmingtrack == True:
                textbutton _("Swim Trip {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("swimming", locked=False)
            elif amidorm10 == True and amifingered == False:
                text _("{color=EF1A1A}{s}You Don't Love Me, Do You?{/s}{/color}")
            else:
                text _("???")
            if howifeeltrack == True:
                textbutton _("How I Feel {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("howifeel", locked=False)
            else:
                text _("???")
            if connecttrack == True:
                textbutton _("Everything is Connected {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("everythingisconnected", locked=False)
            elif day103 == True and connecttrack == False:
                text _("{color=EF1A1A}{s}Nothing is Beautiful{/s}{/color}")
            else:
                text _("???")
            if specialclassroomtrack == True:
                textbutton _("Turn Off The Lights {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("specialclassroom", locked=False)
            elif amisroom15 == True and amifingered == False:
                text _("{color=EF1A1A}{s}List the Things You Love{/s}{/color}")
            else:
                text _("???")
            if ticktocktrack == True:
                textbutton _("Tick Tock Tick Tock Tick Tock {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ticktock", locked=False)
            else:
                text _("???")
            if trinity1track == True:
                textbutton _("Trinity Pt. I: Stations of the Cross {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("trinity1", locked=False)
            else:
                text _("???")
            if trinity2track == True:
                textbutton _("Trinity Pt. II: Hell is Empty {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("trinity2", locked=False)
            else:
                text _("???")
            if trinity3track == True:
                textbutton _("Trinity Pt. III: Non Est Deus {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("trinity3", locked=False)
            else:
                text _("???")
            if babyfinches == True:
                textbutton _("Baby Finches {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("babyfinches", locked=False)
            elif babyfinches == False and hoorayanotherreset == True:
                text _("{color=EF1A1A}{s}A Time When Things Were Horrible{/s}{/color}")
            else:
                text _("???")
            if lesson1 == True:
                textbutton _("Something Everyone Knows and Ignores {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kindergartenclass", locked=False)
            elif lesson1 == False and thirdreset1 == True:
                text _("{color=EF1A1A}{s}LET ME OUT{/s}{/color}")
            else:
                text _("???")
            if goodboy == True:
                textbutton _("Good Boy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("goodboy", locked=False)
            elif sarabar25 == True and anewkey == False and goodboy == False:
                text _("{color=EF1A1A}{s}Bad Boy{/s}{/color}")
            else:
                text _("???")
            if lamblegs == True:
                textbutton _("Lamb Legs {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("specialbonusamiscene", locked=False)
            elif returntosummer2 == True and anewkey == False:
                text _("{color=EF1A1A}{s}Ground Into Nothing{/s}{/color}")
            else:
                text _("???")
            if buckettrack == True:
                textbutton _("Second Sun {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bucketscene", locked=False)
            else:
                text _("???")
            if mothersmilk == True:
                textbutton _("Mother's Milk {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mothersmilk", locked=False)
            elif mothersmiss == True:
                text _("{color=EF1A1A}{s}Overlooked{/s}{/color}")
            else:
                text _("???")
            if amyevent == True:
                textbutton _("Amy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amyevent", locked=False)
            else:
                text _("???")
            if rainking == True:
                textbutton _("Rain King {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rainking", locked=False)
            elif rainkingmiss == True:
                text _("{color=EF1A1A}{s}Drought God{/s}{/color}")
            else:
                text _("???")
            if armsbenttrack == True:
                textbutton _("Arms Bent Back {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("armsbentback", locked=False)
            elif armsbentmiss == True:
                text _("{color=EF1A1A}{s}Lost in the Red Room{/s}{/color}")
            else:
                text _("???")
            if kyotoevent == True:
                textbutton _("Kyoto {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("postfreddeathscene", locked=False)
            elif kyotomiss == True:
                text _("{color=EF1A1A}{s}No One Leaves This City{/s}{/color}")
            else:
                text _("???")
            if persistent.alexisevent == True:
                textbutton _("Alexisthymia {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("alexisevent", locked=False)
            else:
                text _("???")
            if swimtrip2 == True:
                textbutton _("Sally Sells Seashells {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("swimtrip2", locked=False)
            elif swimtrip2miss == True:
                text _("{color=EF1A1A}{s}Sally is Homeless{/s}{/color}")
            else:
                text _("???")
            textbutton _("Back") action ShowMenu('eventtracker11')

screen eventtracker11 ():
    tag menu

    use game_menu(_("Event Tracker"), scroll="viewport"):

        style_prefix "aff"

        grid 1 3:
            #align (1, 0.45)
            spacing 20

            imagebutton:
                idle "mainview1.png"
                hover "mainview2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('eventtrackermainhub')
            imagebutton:
                idle "charaview1.png"
                hover "charaview2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('eventtrackercharahub')
            imagebutton:
                idle "happyview1.png"
                hover "happyview2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('secrettracker')

screen eventtrackermainhub ():
    tag menu

    use game_menu(_("Event Tracker"), scroll="viewport"):

        style_prefix "aff"

        grid 3 2:
            #align (1, 0.45)
            spacing 40

            imagebutton:
                idle "chap1idle.png"
                hover "chap1hover.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('maintracker')
            if hoorayanotherreset == False:
                imagebutton:
                    idle "chaplocked.png"
                    hover "chaplocked.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Replay("roomwithclocks", locked=False)
            else:
                imagebutton:
                    idle "chap2idle.png"
                    hover "chap2hover.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('maintrackerch2')
            if chapthreeactive == False:
                imagebutton:
                    idle "chaplocked.png"
                    hover "chaplocked.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Replay("roomwithclocks", locked=False)
            else:
                imagebutton:
                    idle "chap3idle.png"
                    hover "chap3hover.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('maintrackerch3')
            if resetsix4 == False:
                imagebutton:
                    idle "chaplocked.png"
                    hover "chaplocked.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    #action Replay("roomwithclocks", locked=False)
            else:
                imagebutton:
                    idle "chap4idle.png"
                    hover "chap4hover.png"
                    #xalign 0.2 yalign 0.5
                    focus_mask True
                    action ShowMenu('maintrackerch4')
            imagebutton:
                idle "chaplocked.png"
                hover "chaplocked.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                #action Replay("roomwithclocks", locked=False)
            imagebutton:
                idle "chaplocked.png"
                hover "chaplocked.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                #action Replay("roomwithclocks", locked=False)



        vbox:
            textbutton _("Back") action ShowMenu('eventtracker11')

screen eventtrackercharahub ():
    tag menu

    use game_menu(_("Characters"), scroll="viewport"):

        style_prefix "aff"

        grid 2 1:
            #align (1, 0.45)
            spacing 20

            imagebutton:
                idle "maincharaview1.png"
                hover "maincharaview2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('eventtrackermaincharahub')
            imagebutton:
                idle "sidecharaview1.png"
                hover "sidecharaview2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('eventtrackersidecharahub')
        vbox:
            textbutton _("Back") action ShowMenu('eventtracker11')


screen eventtrackermaincharahub ():
    tag menu

    use game_menu(_("Main Characters"), scroll="viewport"):

        style_prefix "aff"

        grid 5 4:
            align (1, 1)
            xspacing 60
            yspacing 20

            imagebutton:
                idle "chikathumb1.png"
                hover "chikathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuchika')
            imagebutton:
                idle "yumithumb1.png"
                hover "yumithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuyumi')
            imagebutton:
                idle "ayanethumb1.png"
                hover "ayanethumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuayane')
            imagebutton:
                idle "sanathumb1.png"
                hover "sanathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenusana')
            imagebutton:
                idle "makotothumb1.png"
                hover "makotothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenumakoto')
            imagebutton:
                idle "mikuthumb1.png"
                hover "mikuthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenumiku')
            imagebutton:
                idle "futabathumb1.png"
                hover "futabathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenufutaba')
            imagebutton:
                idle "rinthumb1.png"
                hover "rinthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenurin')
            imagebutton:
                idle "amithumb1.png"
                hover "amithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuami')
            imagebutton:
                idle "mayathumb1.png"
                hover "mayathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenumaya')
            imagebutton:
                idle "mollythumb1.png"
                hover "mollythumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenumolly')
            imagebutton:
                idle "tsuneyothumb1.png"
                hover "tsuneyothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenutsuneyo')
            imagebutton:
                idle "utathumb1.png"
                hover "utathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuuta')
            imagebutton:
                idle "iothumb1.png"
                hover "iothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuio')
            imagebutton:
                idle "nodokathumb1.png"
                hover "nodokathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenunodoka')
            imagebutton:
                idle "otohathumb1.png"
                hover "otohathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuotoha')
            imagebutton:
                idle "toukathumb1.png"
                hover "toukathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenutouka')
            imagebutton:
                idle "yasuthumb1.png"
                hover "yasuthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuyasu')
            imagebutton:
                idle "norikothumb1.png"
                hover "norikothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenunoriko')
            imagebutton:
                idle "kirinthumb1.png"
                hover "kirinthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenukirin')

screen eventtrackersidecharahub ():
    tag menu

    use game_menu(_("Side Characters"), scroll="viewport"):

        style_prefix "aff"

        grid 5 3:
            align (1, 1)
            xspacing 60
            yspacing 20

            imagebutton:
                idle "sarathumb1.png"
                hover "sarathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenusara')
            imagebutton:
                idle "harukathumb1.png"
                hover "harukathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuharuka')
            imagebutton:
                idle "kaorithumb1.png"
                hover "kaorithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenukaori')
            imagebutton:
                idle "chinamithumb1.png"
                hover "chinamithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuchinami')
            imagebutton:
                idle "karinthumb1.png"
                hover "karinthumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenukarin')
            imagebutton:
                idle "makithumb1.png"
                hover "makithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenumaki')
            imagebutton:
                idle "yukithumb1.png"
                hover "yukithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuyuki')
            imagebutton:
                idle "nikithumb1.png"
                hover "nikithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuniki')
            imagebutton:
                idle "wakanathumb1.png"
                hover "wakanathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuwakana')
            imagebutton:
                idle "osakothumb1.png"
                hover "osakothumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuosako')
            imagebutton:
                idle "tsubasathumb1.png"
                hover "tsubasathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenutsubasa')
            imagebutton:
                idle "tsukasathumb1.png"
                hover "tsukasathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenutsukasa')
            imagebutton:
                idle "imanithumb1.png"
                hover "imanithumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenuimani')
            imagebutton:
                idle "rikathumb1.png"
                hover "rikathumb2.png"
                #xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenurika')
            imagebutton:
                idle "naothumb1.png"
                hover "naothumb2.png"
                xalign 0.2 yalign 0.5
                focus_mask True
                action ShowMenu('gamemenunao')

screen gamemenuami():

    tag menu
    if amimenuoutfit is not None and renpy.loadable(amimenuoutfit) :
        add amimenuoutfit
    else :
        add "game_menuami.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#ff4dd2}Height: 5'2/157cm{/color}") style "profile"
        text ("{color=#ff4dd2}Birthday: August 31st{/color}") style "profile"
        text ("\n{color=#ff4dd2}Affection: [ami_love]{/color}") style "profile"
        text ("{color=#ff4dd2}Lust: [ami_lust]{/color}") style "profile"
        text ("{color=#ff4dd2}Headpats: [amipats]{/color}") style "profile"
        if amimiss < 1:
            text ("{color=#ff4dd2}Events: [amipoint]/40{/color}") style "profile"
        else:
            text ("{color=#ff4dd2}Events: [amipoint]/40{/color} {color=#FF0000}([amimiss] Missed){/color}") style "profile"

    imagebutton:
        idle "amievrep1.png"
        hover "amievrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('amitracker')

    if amifingered == True:
        imagebutton:
            idle "subscribestar/images2/amimaidrep1.png"
            hover "subscribestar/images2/amimaidrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')

    if aminudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('amiphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('amiphone')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(ami_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen amitracker():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Ami Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=ff4dd2}Ami Arakawa ([ami_love] Affection){/color}"
            if firsttimeamisroom == True:
                textbutton _("Harem Tutorial {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimeamisroom", locked=False)
            else:
                text _("Harem Tutorial")
            if amifirsthall == True:
                textbutton _("Uninvited {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amifirsthall", locked=False)
            else:
                text _("Uninvited")
            if amisroom5 == True:
                textbutton _("The Queen of Spiders {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amisroom5", locked=False)
            else:
                text _("The Queen of Spiders")
            if amidorm5 == True:
                textbutton _("Home Away From Home {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidorm5", locked=False)
            else:
                text _("Home Away From Home")
            if amisroom10 == True:
                textbutton _("Something Darker {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amisroom10", locked=False)
            else:
                text _("Something Darker")
            if aminew1 == True:
                textbutton _("Couple's Discount (Sea of Diamonds) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("aminew1", locked=False)
            else:
                text _("Couple's Discount (Sea of Diamonds)")
            if aminew2 == True:
                textbutton _("Ode to a Marsh Warbler {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("aminew2", locked=False)
            else:
                text _("Ode to a Marsh Warbler")
            if amidorm10 == True:
                textbutton _("No One Can See Us {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidorm10", locked=False)
            else:
                text _("No One Can See Us")
            if day98 == True:
                textbutton _("Walking on Air {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day98", locked=False)
            elif amidorm10 == True and amifingered == False:
                text _("{color=EF1A1A}{s}Falling, Falling, Falling{/s}{/color}")
            else:
                text _("{color=FF85FD}Walking on Air{/color}")
            if amidorm15 == True:
                textbutton _("Back Out in the Heat {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidorm15", locked=False)
            else:
                text _("Back Out in the Heat")
            if amisroom15 == True:
                textbutton _("Important Things {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amisroom15", locked=False)
            else:
                text _("Important Things")
            if amilust10 == True:
                textbutton _("Wake Up Call {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amilust10", locked=False)
            elif beachvacation16 == True and amilust10 == False:
                text _("{color=EF1A1A}{s}Sleep Forever{/s}{/color}")
            else:
                text _("{color=FF85FD}Wake Up Call{/color}")
            if amisroom20 == True:
                textbutton _("Cute Girls and Stuff {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amisroom20", locked=False)
            else:
                text _("Cute Girls and Stuff")
            if amidorm20 == True:
                textbutton _("Divergence {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidorm20", locked=False)
            else:
                text _("Divergence")
            if amisroom25 == True:
                textbutton _("Such Small Hands {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amisroom25", locked=False)
            elif amidorm20 == True and amifingered == False:
                text _("{color=EF1A1A}{s}Ghosts in the Walls{/s}{/color}")
            else:
                text _("Such Small Hands")
            if amidorm25 == True:
                textbutton _("Everlasting Love {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidorm25", locked=False)
            else:
                text _("Everlasting Love")
            text _("-----------------------------------------------------------")
            if amiinvite1 == True:
                textbutton _("Living {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amiinvite1", locked=False)
            else:
                text _("{color=778EFF}Living{/color}")
            if amiinvite2 == True:
                textbutton _("Rising to the Challenge {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amiinvite2", locked=False)
            elif amiinvite2miss == True:
                text _("{color=EF1A1A}{s}Failing at Everything{/s}{/color}")
            else:
                text _("{color=778EFF}Rising to the Challenge{/color}")
            if amiinvite3 == True:
                textbutton _("Best Friends Forever {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amiinvite3", locked=False)
            else:
                text _("{color=778EFF}Best Friends Forever{/color}")
            if amimaid30 == True:
                textbutton _("Third Place {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amimaid30", locked=False)
            else:
                text _("Third Place")
            if amidate35 == True:
                textbutton _("The Big Sleep (Cute Girl Magic) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidate35", locked=False)
            else:
                text _("The Big Sleep (Cute Girl Magic)")
            if amidorm40 == True:
                textbutton _("Heaven for Human Blood {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidorm40", locked=False)
            elif amidorm40miss == True:
                text _("{color=EF1A1A}{s}A Horse Misused{/s}{/color}")
            else:
                text _("Heaven for Human Blood")
            if amilust15 == True:
                textbutton _("As Light as Air {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amilust15", locked=False)
            elif amilust15skip == True:
                text _("{color=EF1A1A}{s}Does She Remind You?{/s}{/color}")
            else:
                text _("{color=FF85FD}As Light as Air{/color}")
            if amilust20 == True:
                textbutton _("Conscious or Not {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amilust20", locked=False)
            elif amilust20skip == True:
                text _("{color=EF1A1A}{s}A Hallway Full of Eyes{/s}{/color}")
            else:
                text _("{color=FF85FD}Conscious or Not{/color}")
            if amidate50 == True:
                textbutton _("Outcry of the Hunted Hare {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidate50", locked=False)
            else:
                text _("Outcry of the Hunted Hare")
            if amidate50p2 == True:
                textbutton _("Fruits of the Two Seasons {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidate50p2", locked=False)
            else:
                text _("Fruits of the Two Seasons")
            if amidate50p3 == True:
                textbutton _("My Life With You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidate50p3", locked=False)
            else:
                text _("My Life With You")
            if amidate50p4 == True:
                textbutton _("Somnambula {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amidate50p4", locked=False)
            else:
                text _("Somnambula")
            text _("-----------------------------------------------------------")
            if amilust35 == True:
                textbutton _("No One Can Hear Us {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amilust35", locked=False)
            elif amilust35skip == True:
                text _("{color=EF1A1A}{s}Splat{/s}{/color}")
            else:
                text _("{color=FF85FD}No One Can Hear Us{/color}")
            if amimaid50 == True:
                textbutton _("Not Safe For Work {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amimaid50", locked=False)
            else:
                text _("Not Safe For Work")
            if amiinvite4 == True:
                textbutton _("Mama's Girl {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amiinvite4", locked=False)
            else:
                text _("{color=778EFF}Mama's Girl{/color}")
            if amispecial50 == True:
                textbutton _("Worry Not, The Mason Jar {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amispecial50", locked=False)
            else:
                text _("Worry Not, The Mason Jar")
            if amilust50 == True:
                textbutton _("Family Matters {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amilust50", locked=False)
            elif amilust50skip == True:
                text _("{color=EF1A1A}{s}Fucking Die You Piece of Shit{/s}{/color}")
            else:
                text _("{color=FF85FD}Family Matters{/color}")
            text _("-----------------------------------------------------------")
            if amilust60 == True:
                textbutton _("The Caretaker {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amilust60", locked=False)
            elif amilust60skip == True:
                text _("{color=EF1A1A}{s}Bucket, Bucket, Lovely Old Bucket{/s}{/color}")
            else:
                text _("{color=FF85FD}The Caretaker{/color}")
            if amispring1 == True:
                textbutton _("Della {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amispring1", locked=False)
            else:
                text _("Della")
            if amicamp1 == True:
                textbutton _("Every Day Birds (In Nothing But Blood) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amicamp1", locked=False)
            else:
                text _("Every Day Birds (In Nothing But Blood)")
            if amicamp2 == True:
                textbutton _("There Is A Light That Never Goes Out {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amicamp2", locked=False)
            else:
                text _("There Is A Light That Never Goes Out")
            if halloweenami1 == True:
                textbutton _("Soon (Another Nightmare) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenami1", locked=False)
            else:
                text _("Soon (Another Nightmare)")
            if amispring2 == True:
                textbutton _("Faith & Sacrifice {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amispring2", locked=False)
            else:
                text _("Faith & Sacrifice")
            if amispring3 == True:
                textbutton _("Shiritori {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amispring3", locked=False)
            else:
                text _("Shiritori")
            textbutton _("Back") action ShowMenu('gamemenuami')

screen gamemenumaya():

    tag menu
    if mayamenuoutfit is not None and renpy.loadable(mayamenuoutfit) :
        add mayamenuoutfit
    else :
        add "game_menumaya.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#18b500}Height: 5'0/152cm{/color}") style "profile"
        text ("{color=#18b500}Birthday: January 1st{/color}") style "profile"
        text ("\n{color=#18b500}Affection: [maya_love]{/color}") style "profile"
        text ("{color=#18b500}Lust: N/A{/color}") style "profile"
        text ("{color=#18b500}Headpats: 0{/color}") style "profile"
        if mayamiss < 1:
            text ("{color=#18b500}Events: [mayapoint]/32{/color}") style "profile"
        else:
            text ("{color=#18b500}Events: [mayapoint]/32{/color} {color=#FF0000}([mayamiss] Missed){/color}") style "profile"

    imagebutton:
        idle "mayashrinerep1.png"
        hover "mayashrinerep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('mayatracker')

    if bonus == True:
        if day102 == False:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')
        else:
            imagebutton:
                idle "subscribestar/images2/mayayayrep1.png"
                hover "subscribestar/images2/mayayayrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('mayareplays')

    if mayanudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('mayaphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('mayaphone')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(maya_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen mayatracker():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Maya Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=18b500}Maya Makinami ([maya_love] Affection){/color}"
            if firsttimeshrine == True:
                textbutton _("A New Beginning {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimeshrine", locked=False)
            else:
                text _("A New Beginning")
            if mayafirsthall == True:
                textbutton _("Mondays {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayafirsthall", locked=False)
            else:
                text _("Mondays")
            if shrine5 == True:
                textbutton _("Different Worlds {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("shrine5", locked=False)
            else:
                text _("Different Worlds")
            if mayadorm5 == True:
                textbutton _("Secrets Worth Keeping {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayadorm5", locked=False)
            else:
                text _("Secrets Worth Keeping")
            if shrine10 == True:
                textbutton _("Past/Present/Future {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("shrine10", locked=False)
            else:
                text _("Past/Present/Future")
            if mayadorm10 == True:
                textbutton _("Rewind/Repeat/Refuse {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayadorm10", locked=False)
            else:
                text _("Rewind/Repeat/Refuse")
            if shrine15 == True:
                textbutton _("You and Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("shrine15", locked=False)
            else:
                text _("You and Me")
            if mayadorm15 == True:
                textbutton _("Takoyaki {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayadorm15", locked=False)
            else:
                text _("Takoyaki")
            if shrine20 == True:
                textbutton _("Nothing is Real {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("shrine20", locked=False)
            else:
                text _("Nothing is Real")
            if mayadorm20 == True:
                textbutton _("Close Your Eyes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayadorm20", locked=False)
            else:
                text _("Close Your Eyes")
            if shrine25 == True:
                textbutton _("Watermelons and Violin {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("shrine25", locked=False)
            else:
                text _("Watermelons and Violin")
            if mayadorm25 == True:
                textbutton _("FLAVOR BEAM! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayadorm25", locked=False)
            else:
                text _("FLAVOR BEAM!")
            text _("-----------------------------------------------------------")
            if mayadorm30 == True:
                textbutton _("What it Means to Be Destroyed {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayadorm30", locked=False)
            else:
                text _("What it Means to Be Destroyed")
            if shrine30 == True:
                textbutton _("Now More Than Ever {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("shrine30", locked=False)
            elif mayadorm30 == True and ami_virgin == True:
                text _("{color=EF1A1A}{s}Breaking, the Best Way{/s}{/color}")
            else:
                text _("Now More Than Ever")
            if mayadorm35 == True:
                textbutton _("A Place That Can Only Exist in Our Minds {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayadorm35", locked=False)
            else:
                text _("A Place That Can Only Exist in Our Minds")
            if shrine35 == True:
                textbutton _("Stop Looking For Answers {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("shrine35", locked=False)
            else:
                text _("Stop Looking For Answers")
            if mayafestival1 == True:
                textbutton _("Somewhere Inside of a Dream {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayafestival1", locked=False)
            else:
                text _("Somewhere Inside of a Dream")
            if mayafestival2 == True:
                textbutton _("Three Halves Make a Whole (Itadakimasu) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayafestival2", locked=False)
            else:
                text _("Three Halves Make a Whole (Itadakimasu)")
            if mayafestival3 == True:
                textbutton _("As The Sun Disappears {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayafestival3", locked=False)
            else:
                text _("As The Sun Disappears")
            if mayafestival4 == True:
                textbutton _("Everlasting Mercy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayafestival4", locked=False)
            else:
                text _("Everlasting Mercy")
            text _("-----------------------------------------------------------")
            if shrine40 == True:
                textbutton _("The Sun, And All Its Toxic Rays {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("shrine40", locked=False)
            else:
                text _("The Sun, And All Its Toxic Rays")
            if mayadate45 == True:
                textbutton _("Anything & Everything {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayadate45", locked=False)
            else:
                text _("Anything & Everything")
            if mayaspecial45 == True:
                textbutton _("A Brutal, Violent Creaming {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayaspecial45", locked=False)
            else:
                text _("A Brutal, Violent Creaming")
            text _("-----------------------------------------------------------")
            if sportswars5 == True:
                textbutton _("The Motherland Calls! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars5", locked=False)
            else:
                text _("The Motherland Calls!")
            if sportswars10 == True:
                textbutton _("Miraculous Human-Glue {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars10", locked=False)
            else:
                text _("Miraculous Human-Glue")
            if sportswars14 == True:
                textbutton _("Radio Silence {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars14", locked=False)
            else:
                text _("Radio Silence")
            if halloweenmaya1 == True:
                textbutton _("The Girl Who Leapt Through Time {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenmaya1", locked=False)
            else:
                text _("The Girl Who Leapt Through Time")
            if halloweenmaya2 == True:
                textbutton _("Wake Up (My Story) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenmaya2", locked=False)
            else:
                text _("Wake Up (My Story)")
            if halloweenmaya3 == True:
                textbutton _("Right as Rain {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenmaya3", locked=False)
            else:
                text _("Right as Rain")
            if mayaspring1 == True:
                textbutton _("Billy Pilgrim {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayaspring1", locked=False)
            else:
                text _("Billy Pilgrim")
            if mayaspring2 == True:
                textbutton _("A Second Haunting {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayaspring2", locked=False)
            else:
                text _("A Second Haunting")
            if mayaspring3 == True:
                textbutton _("My Perfect World {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mayaspring3", locked=False)
            else:
                text _("My Perfect World")
            textbutton _("Back") action ShowMenu('gamemenumaya')

screen gamemenuchika():

    tag menu
    if chikamenuoutfit is not None and renpy.loadable(chikamenuoutfit) :
        add chikamenuoutfit
    else :
        add "game_menuchika.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#AF7F00}Height: 5'5/167cm{/color}") style "profile"
        text ("{color=#AF7F00}Birthday: May 9th{/color}") style "profile"
        text ("\n{color=#AF7F00}Affection: [chika_love]{/color}") style "profile"
        text ("{color=#AF7F00}Lust: [chika_lust]{/color}") style "profile"
        text ("{color=#AF7F00}Headpats: [chikapats]{/color}") style "profile"
        if chikamiss < 1:
            text ("{color=#AF7F00}Events: [chikapoint]/36{/color}") style "profile"
        else:
            text ("{color=#AF7F00}Events: [chikapoint]/36{/color} {color=#FF0000}([chikamiss] Missed){/color}") style "profile"

    imagebutton:
        idle "chikamorningrep1.png"
        hover "chikamorningrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('chikatracker')

    if bonus == True:
        if chikadorm20 == False:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')
        else:
            imagebutton:
                idle "subscribestar/images2/chikafinger1.png"
                hover "subscribestar/images2/chikafinger2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('chikareplays')

        if chikanudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('chikaphone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('chikaphone')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(chika_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen chikatracker():

    tag menu

    use game_menu(_("Chika Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=AF7F00}Chika Chosokabe ([chika_love] Affection){/color}"
            if firsttimemall == True:
                textbutton _("The Retail Machine {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimemall", locked=False)
            else:
                text _("The Retail Machine")
            if chikafirsthall == True:
                textbutton _("A Dog that Does Math {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikafirsthall", locked=False)
            else:
                text _("A Dog that Does Math")
            if mall5 == True:
                textbutton _("Big Shot Teacher {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mall5", locked=False)
            else:
                text _("Big Shot Teacher")
            if chikadorm5 == True:
                textbutton _("Something About Biting {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikadorm5", locked=False)
            else:
                text _("Something About Biting")
            if mall10 == True:
                textbutton _("Behind The Curtain {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mall10", locked=False)
            else:
                text _("Behind The Curtain")
            if chikadorm10 == True:
                textbutton _("Side Event {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikadorm10", locked=False)
            else:
                text _("Side Event")
            if chikadorm15 == True:
                textbutton _("A Castle for Everyone {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikadorm15", locked=False)
            else:
                text _("A Castle for Everyone")
            if mall15 == True:
                textbutton _("A Dog that Doesn't Do Math {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mall15", locked=False)
            else:
                text _("A Dog that Doesn't Do Math")
            if chikadorm20 == True:
                textbutton _("Schadenfreude {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikadorm20", locked=False)
            else:
                text _("Schadenfreude")
            if mall20 == True:
                textbutton _("True Power: Unleashed {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mall20", locked=False)
            else:
                text _("True Power: Unleashed")
            if day139 == True:
                textbutton _("Detention {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day139", locked=False)
            else:
                text _("{color=FF85FD}Detention{/color}")
            if chikainvite1 == True:
                textbutton _("A Trip to the Moon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikainvite1", locked=False)
            else:
                text _("{color=778EFF}A Trip to the Moon{/color}")
            if chikainvite2 == True:
                textbutton _("First Hunt {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikainvite2", locked=False)
            else:
                text _("{color=778EFF}First Hunt{/color}")
            text _("-----------------------------------------------------------")
            if chikalust10 == True:
                textbutton _("Baby it's Cold Outside {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikalust10", locked=False)
            elif chikalust10miss == True:
                text _("{color=EF1A1A}{s}Freezing to Death{/s}{/color}")
            else:
                text _("{color=FF85FD}Baby it's Cold Outside{/color}")
            if chikaonsen1 == True:
                textbutton _("Little Miracles {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaonsen1", locked=False)
            else:
                text _("Little Miracles")
            if chikaonsen2 == True:
                textbutton _("Bleed {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaonsen2", locked=False)
            else:
                text _("Bleed")
            if chikaonsen3 == True:
                textbutton _("Three Words {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaonsen3", locked=False)
            else:
                text _("Three Words")
            if chikaonsen4 == True:
                textbutton _("Zanzibar (Counting Cats) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaonsen4", locked=False)
            else:
                text _("Zanzibar (Counting Cats)")
            if chikalust15 == True:
                textbutton _("The Princess & The Pauper {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikalust15", locked=False)
            elif chikalust15skip == True:
                text _("{color=EF1A1A}{s}Them{/s}{/color}")
            else:
                text _("{color=FF85FD}The Princess & The Pauper{/color}")
            if chikalust20 == True:
                textbutton _("Into the Woods {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikalust20", locked=False)
            elif chikalust20skip == True:
                text _("{color=EF1A1A}{s}Out of the Woods{/s}{/color}")
            else:
                text _("{color=FF85FD}Into the Woods{/color}")
            if chikaspecial40 == True:
                textbutton _("In Search of Summer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspecial40", locked=False)
            else:
                text _("In Search of Summer")
            if mall40 == True:
                textbutton _("Self Care {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mall40", locked=False)
            else:
                text _("Self Care")
            if mall40p2 == True:
                textbutton _("The Gap in the Curtain {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mall40p2", locked=False)
            else:
                text _("The Gap in the Curtain")
            if chikadate45 == True:
                textbutton _("The Gap in the Door {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikadate45", locked=False)
            else:
                text _("The Gap in the Door")
            text _("-----------------------------------------------------------")
            if chikalust25 == True:
                textbutton _("Mating Season {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikalust25", locked=False)
            elif chikalust25skip == True:
                text _("{color=EF1A1A}{s}Hibernation{/s}{/color}")
            else:
                text _("{color=FF85FD}Mating Season{/color}")
            if mall45 == True:
                textbutton _("Rough Cuts {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mall45", locked=False)
            else:
                text _("Rough Cuts")
            if chikaspecial45 == True:
                textbutton _("Curry Night {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspecial45", locked=False)
            else:
                text _("Curry Night")
            if chikadorm45 == True:
                textbutton _("Our Time Atop This Mattress {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikadorm45", locked=False)
            else:
                text _("Our Time Atop This Mattress")
            text _("-----------------------------------------------------------")
            if chikaspring1 == True:
                textbutton _("Gold Digger {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspring1", locked=False)
            else:
                text _("Gold Digger")
            if chikaspring2 == True:
                textbutton _("Original Sin {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspring2", locked=False)
            else:
                text _("Original Sin")
            if chikaspring3 == True:
                textbutton _("To Drink, To Drown {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspring3", locked=False)
            else:
                text _("To Drink, To Drown")
            if chikaspring4 == True:
                textbutton _("Rabies {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspring4", locked=False)
            else:
                text _("Rabies")
            if chikaspring5 == True:
                textbutton _("Frogging {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspring5", locked=False)
            else:
                text _("Frogging")
            if chikaspring6 == True:
                textbutton _("Everyone I've Ever Loved {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspring6", locked=False)
            else:
                text _("Everyone I've Ever Loved")
            if chikaspring7 == True:
                textbutton _("Transpacific Sadness Symposium V: NEW BLACK PARADIGM {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspring7", locked=False)
            else:
                text _("Transpacific Sadness Symposium V: NEW BLACK PARADIGM")
            if chikaspring8 == True:
                textbutton _("Chika-chan vs. Auto-Pilot {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chikaspring8", locked=False)
            else:
                text _("Chika-chan vs. Auto-Pilot")
            textbutton _("Back") action ShowMenu('gamemenuchika')

screen gamemenuyumi():

    tag menu
    if yumimenuoutfit is not None and renpy.loadable(yumimenuoutfit) :
        add yumimenuoutfit
    else :
        add "game_menuyumi.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#d12e2e}Height: 5'6/166cm{/color}") style "profile"
        text ("{color=#d12e2e}Birthday: October 31st{/color}") style "profile"
        text ("\n{color=#d12e2e}Affection: [yumi_love]{/color}") style "profile"
        text ("{color=#d12e2e}Lust: N/A{/color}") style "profile"
        text ("{color=#d12e2e}Headpats: 0{/color}") style "profile"
        text ("{color=#d12e2e}Events: [yumipoint]/32{/color}") style "profile"

    imagebutton:
        idle "yumievrep1.png"
        hover "yumievrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('yumitracker')

    if nodokaspecial15p3 == True:
        imagebutton:
            idle "subscribestar/images2/matadorrep1.png"
            hover "subscribestar/images2/matadorrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('yumireplays')
    else:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(yumi_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen yumitracker():

    tag menu

    use game_menu(_("Yumi Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=d12e2e}Yumi Yamaguchi ([yumi_love] Affection){/color}"
            if firsttimestreets == True:
                textbutton _("Five Million Dollars {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimestreets", locked=False)
            else:
                text _("Five Million Dollars")
            if yumifirsthall == True:
                textbutton _("Micropenis {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumifirsthall", locked=False)
            else:
                text _("Micropenis")
            if streets5 == True:
                textbutton _("Three Second Smile {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("streets5", locked=False)
            else:
                text _("Three Second Smile")
            if streets10 == True:
                textbutton _("I See You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("streets10", locked=False)
            else:
                text _("I See You")
            if yumidorm5 == True:
                textbutton _("Fuck The Police {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumidorm5", locked=False)
            else:
                text _("Fuck The Police")
            if yumidorm10 == True:
                textbutton _("Yumi Revitalization Project {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumidorm10", locked=False)
            else:
                text _("Yumi Revitalization Project")
            if yumidorm15 == True:
                textbutton _("Worse Comes to Worst {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumidorm15", locked=False)
            else:
                text _("Worse Comes to Worst")
            if streets15 == True:
                textbutton _("Apples to Apples {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("streets15", locked=False)
            else:
                text _("Apples to Apples")
            if streets20 == True:
                textbutton _("Token Tsundere {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("streets20", locked=False)
            else:
                text _("Token Tsundere")
            if yumidorm20 == True:
                textbutton _("Great Expectations {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumidorm20", locked=False)
            else:
                text _("Great Expectations")
            if streets25 == True:
                textbutton _("A Place Like This {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("streets25", locked=False)
            else:
                text _("A Place Like This")
            if yumidorm25 == True:
                textbutton _("Caught in the Vortex {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumidorm25", locked=False)
            else:
                text _("Caught in the Vortex")
            text _("-----------------------------------------------------------")
            if streets30 == True:
                textbutton _("Where the Sidewalk Ends {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("streets30", locked=False)
            else:
                text _("Where the Sidewalk Ends")
            if yumidorm30 == True:
                textbutton _("Walls Too Thick to Hear Through {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumidorm30", locked=False)
            else:
                text _("Walls Too Thick to Hear Through")
            if yumidorm35 == True:
                textbutton _("Tech Support {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumidorm35", locked=False)
            else:
                text _("Tech Support")
            if yumicallnight35 == True:
                textbutton _("Abyss {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumicallnight35", locked=False)
            else:
                text _("Abyss")
            if yumispecial40 == True:
                textbutton _("Reconciliation {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispecial40", locked=False)
            else:
                text _("Reconciliation")
            if yumispecial40p2 == True:
                textbutton _("Neon Heart (If I Close My Eyes) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispecial40p2", locked=False)
            else:
                text _("Neon Heart (If I Close My Eyes)")
            if streets40 == True:
                textbutton _("Unsung Heroes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("streets40", locked=False)
            else:
                text _("Unsung Heroes")
            if yumispecial45 == True:
                textbutton _("See You Around {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispecial45", locked=False)
            else:
                text _("See You Around")
            text _("-----------------------------------------------------------")
            if yumislumber1 == True:
                textbutton _("Two Months of Nothing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumislumber1", locked=False)
            else:
                text _("Two Months of Nothing")
            if yumislumber2 == True:
                textbutton _("Loggerhead {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumislumber2", locked=False)
            else:
                text _("Loggerhead")
            if yumislumber3 == True:
                textbutton _("A Day in the Life {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumislumber3", locked=False)
            else:
                text _("A Day in the Life")
            text _("-----------------------------------------------------------")
            if yumispring1 == True:
                textbutton _("Kid of the Month {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispring1", locked=False)
            else:
                text _("Kid of the Month")
            if yumispring2 == True:
                textbutton _("Frog Boy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispring2", locked=False)
            else:
                text _("Frog Boy")
            if beachfive13 == True:
                textbutton _("Wake Me Up When It's Over {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive13", locked=False)
            else:
                text _("Wake Me Up When It's Over")
            if yumispring3 == True:
                textbutton _("A Life I Never Wanted {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispring3", locked=False)
            else:
                text _("A Life I Never Wanted")
            if yumispring4 == True:
                textbutton _("Pogonomyrmex Occidentalis Owyheei {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispring4", locked=False)
            else:
                text _("Pogonomyrmex Occidentalis Owyheei")
            if yumispring5 == True:
                textbutton _("The Dragon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispring5", locked=False)
            else:
                text _("The Dragon")
            if yumispring6 == True:
                textbutton _("Ittekimasu {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispring6", locked=False)
            else:
                text _("Ittekimasu")
            if yumispring7 == True:
                textbutton _("Transpacific Sadness Symposium VI: STICK(BUG) SICKNESS {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispring7", locked=False)
            else:
                text _("Transpacific Sadness Symposium VI: STICK(BUG) SICKNESS")
            if yumispring8 == True:
                textbutton _("Death With Dignity {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumispring8", locked=False)
            else:
                text _("Death With Dignity")
            textbutton _("Back") action ShowMenu('gamemenuyumi')

screen gamemenuayane():

    tag menu
    if ayanemenuoutfit is not None and renpy.loadable(ayanemenuoutfit) :
        add ayanemenuoutfit
    else :
        add "game_menuayane.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#00bab1}Height: 5'3/161cm{/color}") style "profile"
        text ("{color=#00bab1}Birthday: September 25th{/color}") style "profile"
        text ("\n{color=#00bab1}Affection: [ayane_love]{/color}") style "profile"
        text ("{color=#00bab1}Lust: [ayane_lust]{/color}") style "profile"
        text ("{color=#00bab1}Headpats: [ayanepats]{/color}") style "profile"
        if ayanemiss < 1:
            text ("{color=#00bab1}Events: [ayanepoint]/42{/color}") style "profile"
        else:
            text ("{color=#00bab1}Events: [ayanepoint]/42{/color} {color=#FF0000}([ayanemiss] Missed){/color}") style "profile"

    imagebutton:
        idle "ayaneevrep1.png"
        hover "ayaneevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('ayanetracker')

    if bonus == True:
        if ayane_virgin == True:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')
        else:
            imagebutton:
                idle "subscribestar/images2/ayanefirstlust1.png"
                hover "subscribestar/images2/ayanefirstlust2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('ayanereplays')

        if ayanenudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('ayanephone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('ayanephone')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(ayane_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen ayanetracker():

    tag menu

    use game_menu(_("Ayane Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=00bab1}Ayane Amamiya ([ayane_love] Affection){/color}"
            if firsttimedojo == True:
                textbutton _("The Unwavering Bravery of Ayane Amamiya {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimedojo", locked=False)
            else:
                text _("The Unwavering Bravery of Ayane Amamiya")
            if ayanefirsthall == True:
                textbutton _("Spy on Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanefirsthall", locked=False)
            else:
                text _("Spy on Me")
            if dojo5 == True:
                textbutton _("The Battle for Kumon-mi {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dojo5", locked=False)
            else:
                text _("The Battle for Kumon-mi")
            if dojo10 == True:
                textbutton _("Names of Our Children {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dojo10", locked=False)
            else:
                text _("Names of Our Children")
            if ayanedorm5 == True:
                textbutton _("Home Sweet Home {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanedorm5", locked=False)
            else:
                text _("Home Sweet Home")
            if ayanenew1 == True:
                textbutton _("Imprinting {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanenew1", locked=False)
            else:
                text _("Imprinting")
            if ayanenew2 == True:
                textbutton _("Far From Fantasy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanenew2", locked=False)
            else:
                text _("Far From Fantasy")
            if ayanenew3 == True:
                textbutton _("Forever Yours (Top of the World) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanenew3", locked=False)
            else:
                text _("Forever Yours (Top of the World)")
            if ayanedorm10 == True:
                textbutton _("Less Like the Vulture {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanedorm10", locked=False)
            else:
                text _("Less Like the Vulture")
            if ayanedorm15 == True:
                textbutton _("First Words {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanedorm15", locked=False)
            else:
                text _("First Words")
            if day68 == True:
                textbutton _("Backwards Spider Crawl {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day68", locked=False)
            else:
                text _("{color=FF85FD}Backwards Spider Crawl{/color}")
            if dojo20 == True:
                textbutton _("Endless Torment {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dojo20", locked=False)
            else:
                text _("Endless Torment")
            if ayanedorm20 == True:
                if bonus == True:
                    textbutton _("Still Young {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("ayanedorm20", locked=False)
                else:
                    textbutton _("Still Young, But Old Enough To Legally Consent {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("ayanedorm20", locked=False)
            elif bonus == True:
                text _("Still Young")
            else:
                text _("Still Young, But Old Enough To Legally Consent")
            if ayanelust10 == True:
                textbutton _("Prisoner {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanelust10", locked=False)
            elif beachvacation16 == True and ayanelust10 == False:
                text _("{color=EF1A1A}{s}Back to Normal{/s}{/color}")
            else:
                text _("{color=FF85FD}Prisoner{/color}")
            if dojo25 == True:
                textbutton _("Regularly Scheduled Programming {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dojo25", locked=False)
            else:
                text _("Regularly Scheduled Programming")
            if ayanedorm25 == True:
                textbutton _("Cold Air of an Encroaching Winter {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanedorm25", locked=False)
            else:
                text _("Cold Air of an Encroaching Winter")
            if dojo30 == True:
                textbutton _("First and Second {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dojo30", locked=False)
            else:
                text _("First and Second")
            if ayanedorm30 == True:
                textbutton _("Crazier Things Have Happened {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanedorm30", locked=False)
            else:
                text _("Crazier Things Have Happened")
            text _("-----------------------------------------------------------")
            if ayaneinvite1 == True:
                textbutton _("Hail Mary {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayaneinvite1", locked=False)
            else:
                text _("{color=778EFF}Hail Mary{/color}")
            if ayaneinvite2 == True:
                textbutton _("One of Many Rooms {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayaneinvite2", locked=False)
            else:
                text _("{color=778EFF}One of Many Rooms{/color}")
            if ayanelust15 == True:
                textbutton _("What a Wonderful World {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanelust15", locked=False)
            elif ayanelust15skip == True and dormwar7 == True:
                text _("{color=EF1A1A}{s}The World is Bad!{/s}{/color}")
            else:
                text _("{color=FF85FD}What a Wonderful World{/color}")
            if dojo35 == True:
                textbutton _("Under the World Tree {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dojo35", locked=False)
            else:
                text _("Under the World Tree")
            if ayanedorm35 == True:
                textbutton _("Crash of Thunder {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanedorm35", locked=False)
            else:
                text _("Crash of Thunder")
            if ayanespecial1 == True:
                textbutton _("Nevermind {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanespecial1", locked=False)
            else:
                text _("Nevermind")
            if ayanespecial2 == True:
                textbutton _("Before the Sun Comes Up {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanespecial2", locked=False)
            else:
                text _("Before the Sun Comes Up")
            if ayanelust20 == True:
                textbutton _("Out With the Old {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanelust20", locked=False)
            elif ayanelust20skip == True:
                text _("{color=EF1A1A}{s}In With the New{/s}{/color}")
            else:
                text _("{color=FF85FD}Out With the Old{/color}")
            text _("-----------------------------------------------------------")
            if ayanespecial40 == True:
                textbutton _("Chronokinetics (Hell Exists) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanespecial40", locked=False)
            else:
                text _("Chronokinetics (Hell Exists)")
            if ayanesanabeach1 == True:
                textbutton _("How the World Works {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanesanabeach1", locked=False)
            else:
                text _("How the World Works")
            if ayanespecial50 == True:
                textbutton _("Chiburi {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanespecial50", locked=False)
            else:
                text _("Chiburi")
            if ayanekirintalk == True:
                textbutton _("Furlough (Tell the World) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanekirintalk", locked=False)
            elif ayanekirintalkskip == True:
                text _("{color=EF1A1A}{s}Indefinite Parole{/s}{/color}")
            else:
                text _("Furlough (Tell the World)")
            if ayanespecial55 == True:
                textbutton _("Double Jeopardy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanespecial55", locked=False)
            else:
                text _("Double Jeopardy")
            if ayanebonus1 == True:
                textbutton _("The Aforementioned Light {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanebonus1", locked=False)
            elif ayanebonus1skip == True:
                text _("{color=EF1A1A}{s}Dark Side of the Room{/s}{/color}")
            else:
                text _("The Aforementioned Light")
            if ayanebonus2 == True:
                textbutton _("Over & Over {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanebonus2", locked=False)
            elif ayanebonus2skip == True:
                text _("{color=EF1A1A}{s}A Failed Attempt at Being Good{/s}{/color}")
            else:
                text _("Over & Over")
            if ayanepool55 == True:
                textbutton _("Dizzy On The Comedown {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanepool55", locked=False)
            else:
                text _("Dizzy On The Comedown")
            text _("-----------------------------------------------------------")
            if ayanespring1 == True:
                textbutton _("...But Home is Nowhere {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanespring1", locked=False)
            else:
                text _("...But Home is Nowhere")
            if beachfive3 == True:
                textbutton _("Doomsayer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive3", locked=False)
            else:
                text _("Doomsayer")
            if beachfive15 == True:
                textbutton _("As You Wish {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive15", locked=False)
            elif beachfive15skip == True:
                text _("{color=EF1A1A}{s}As You Wash{/s}{/color}")
            else:
                text _("{color=FF85FD}As You Wish{/color}")
            if halloweenayane1 == True:
                textbutton _("Chamomile {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenayane1", locked=False)
            else:
                text _("Chamomile")
            if halloweenayane2 == True:
                textbutton _("Time, Resets, and the Like {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenayane2", locked=False)
            else:
                text _("Time, Resets, and the Like")
            if halloweenayane3 == True:
                textbutton _("Soliloquy (Wearing Someone Else's Clothes) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenayane3", locked=False)
            else:
                text _("Soliloquy (Wearing Someone Else's Clothes)")
            if ayanespring2 == True:
                textbutton _("In Shoes That Don't Fit {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanespring2", locked=False)
            elif ayanespring2miss == True:
                text _("{color=EF1A1A}{s}Bipedal Deformation{/s}{/color}")
            else:
                text _("In Shoes That Don't Fit")
            if ayanespring3 == True:
                textbutton _("Mortal Coil (Gay Stuff) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanespring3", locked=False)
            else:
                text _("Mortal Coil (Gay Stuff)")
            textbutton _("Back") action ShowMenu('gamemenuayane')

screen gamemenusana():

    tag menu
    if sanamenuoutfit is not None and renpy.loadable(sanamenuoutfit) :
        add sanamenuoutfit
    else :
        add "game_menusana.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#005730}Height: 4'10/147cm{/color}") style "profile"
        text ("{color=#005730}Birthday: January 4th{/color}") style "profile"
        text ("\n{color=#005730}Affection: [sana_love]{/color}") style "profile"
        text ("{color=#005730}Lust: [sana_lust]{/color}") style "profile"
        text ("{color=#005730}Headpats: [sanapats]{/color}") style "profile"
        if sanamiss < 1:
            text ("{color=#005730}Events: [sanapoint]/33{/color}") style "profile"
        else:
            text ("{color=#005730}Events: [sanapoint]/33{/color} {color=#FF0000}([sanamiss] Missed){/color}") style "profile"

    imagebutton:
        idle "sanaevrep1.png"
        hover "sanaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('sanatracker')

    if sananudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('sanaphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('sanaphone')

    if sanaspring3 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/sanabjrep1.png"
            hover "subscribestar/images2/sanabjrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('sanareplays')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(sana_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen sanatracker():

    tag menu

    use game_menu(_("Sana Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=005730}Sana Sakakibara ([sana_love] Affection){/color}"
            if firsttimebar == True:
                textbutton _("Family Business {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimebar", locked=False)
            else:
                text _("Family Business")
            if sanafirsthall == True:
                textbutton _("Nothing to Do {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanafirsthall", locked=False)
            else:
                text _("Nothing to Do")
            if bar5 == True:
                textbutton _("The Bare Minimum {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar5", locked=False)
            else:
                text _("The Bare Minimum")
            if sanadorm5 == True:
                textbutton _("Recluse {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm5", locked=False)
            else:
                text _("Recluse")
            if bar10 == True:
                textbutton _("Supermom {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar10", locked=False)
            else:
                text _("Supermom")
            if sanadorm10 == True:
                textbutton _("Anywhere At All {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm10", locked=False)
            else:
                text _("Anywhere At All")
            if bar15 == True:
                textbutton _("Carry Me Home {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar15", locked=False)
            else:
                text _("Carry Me Home")
            if sanadorm15 == True:
                textbutton _("Shaking The Tree {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm15", locked=False)
            else:
                text _("Shaking The Tree")
            if bar20 == True:
                textbutton _("Scouting Mission {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar20", locked=False)
            else:
                text _("Scouting Mission")
            if sanadorm20 == True:
                textbutton _("Nice Weather We're Having {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm20", locked=False)
            else:
                text _("Nice Weather We're Having")
            if bar25 == True:
                textbutton _("Life is a Tomato {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar25", locked=False)
            else:
                text _("Life is a Tomato")
            if sanadorm25 == True:
                textbutton _("The Girl in the Black Dress {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm25", locked=False)
            else:
                text _("The Girl in the Black Dress")
            if bar30 == True:
                textbutton _("Self-Medication {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar30", locked=False)
            else:
                text _("Self-Medication")
            if sanadorm30 == True:
                textbutton _("Tortoises and the Concept of Friendship {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm30", locked=False)
            else:
                text _("Tortoises and the Concept of Friendship")
            text _("-----------------------------------------------------------")
            if bar35 == True:
                textbutton _("Purest Intentions {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar35", locked=False)
            else:
                text _("Purest Intentions")
            if sanadorm35 == True:
                textbutton _("Waiting for Anything {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm35", locked=False)
            else:
                text _("Waiting for Anything")
            if bar40 == True:
                textbutton _("Closer to Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar40", locked=False)
            else:
                text _("Closer to Me")
            if sanadorm40 == True:
                textbutton _("The Inside of a Triangle {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm40", locked=False)
            else:
                text _("The Inside of a Triangle")
            if bar45 == True:
                textbutton _("Sweet Vermouth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar45", locked=False)
            else:
                text _("Sweet Vermouth")
            if sanadorm45 == True:
                textbutton _("The Complete Absence of Everything {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm45", locked=False)
            else:
                text _("The Complete Absence of Everything")
            if sanadorm50 == True:
                textbutton _("Mine (Yours) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanadorm50", locked=False)
            else:
                text _("Mine (Yours)")
            if bar50 == True:
                textbutton _("Melatonin {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar50", locked=False)
            elif bar50miss == True:
                text _("{color=EF1A1A}{s}Why Don't You Ever Lock the Door?{/s}{/color}")
            else:
                text _("Melatonin")
            text _("-----------------------------------------------------------")
            if bar55 == True:
                textbutton _("Black Sandy Beaches {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bar55", locked=False)
            else:
                text _("Black Sandy Beaches")
            if ayanesanabeach2 == True:
                textbutton _("Ad Meliora {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanesanabeach2", locked=False)
            elif ayanesanabeach2skip == True:
                text _("{color=EF1A1A}{s}It's All Wrong{/s}{/color}")
            else:
                text _("Ad Meliora")
            if ayanesanabeach3 == True:
                textbutton _("It Comes to Claim Us All {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanesanabeach3", locked=False)
            else:
                text _("It Comes to Claim Us All")
            if ayanesanabeach4 == True:
                textbutton _("Ad Infinitum {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ayanesanabeach4", locked=False)
            elif ayanesanabeach4skip == True:
                text _("{color=EF1A1A}{s}Gods Don't Smile Down{/s}{/color}")
            else:
                text _("Ad Infinitum")
            text _("-----------------------------------------------------------")
            if sanaspring1 == True:
                textbutton _("Taller {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanaspring1", locked=False)
            else:
                text _("Taller")
            if sanaspring2 == True:
                textbutton _("Stutter-Step {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanaspring2", locked=False)
            else:
                text _("Stutter-Step")
            if sanaspring3 == True:
                textbutton _("Weak Man, Weak Boy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanaspring3", locked=False)
            else:
                text _("Weak Man, Weak Boy")
            if sanaspring4 == True:
                textbutton _("Transpacific Sadness Symposium III: TWO-HEADED HORSE {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanaspring4", locked=False)
            else:
                text _("Transpacific Sadness Symposium III: TWO-HEADED HORSE")
            if sanainvite1 == True:
                textbutton _("Piggy & The Boulder {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanainvite1", locked=False)
            else:
                text _("{color=778EFF}Piggy & The Boulder{/color}")
            if sanainvite2 == True:
                textbutton _("Four Letter Words {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sanainvite2", locked=False)
            else:
                text _("{color=778EFF}Four Letter Words{/color}")
            if beachsixsana1 == True:
                textbutton _("Despicable Meat Toilet {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixsana1", locked=False)
            else:
                text _("{color=FF85FD}Despicable Meat Toilet{/color}")
            textbutton _("Back") action ShowMenu('gamemenusana')

screen gamemenumakoto():

    tag menu
    if makotomenuoutfit is not None and renpy.loadable(makotomenuoutfit) :
        add makotomenuoutfit
    else :
        add "game_menumakoto.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#3c55fa}Height: 5'3/159cm{/color}") style "profile"
        text ("{color=#3c55fa}Birthday: December 9th{/color}") style "profile"
        text ("\n{color=#3c55fa}Affection: [makoto_love]{/color}") style "profile"
        text ("{color=#3c55fa}Lust: [makoto_lust]{/color}") style "profile"
        text ("{color=#3c55fa}Headpats: [makpats]{/color}") style "profile"
        if makotomiss < 1:
            text ("{color=#3c55fa}Events: [makotopoint]/39{/color}") style "profile"
        else:
            text ("{color=#3c55fa}Events: [makotopoint]/39{/color} {color=#FF0000}([makotomiss] Missed){/color}") style "profile"

    imagebutton:
        idle "makotoevrep1.png"
        hover "makotoevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('makototracker')

    if bonus == True:
        if makotonew2 == False:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')
        else:
            imagebutton:
                idle "subscribestar/images2/pornshophjrep1.png"
                hover "subscribestar/images2/pornshophjrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('makotoreplays')

        if makotonudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('makotophone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('makotophone')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(makoto_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen makototracker():

    tag menu

    use game_menu(_("Makoto Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=3c55fa}Makoto Miyamura ([makoto_love] Affection){/color}"
            if firsttimepornshop == True:
                textbutton _("Unexpected Profession {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimepornshop", locked=False)
            else:
                text _("Unexpected Profession")
            if makotofirsthall == True:
                textbutton _("Teacher's Pet {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotofirsthall", locked=False)
            else:
                text _("Teacher's Pet")
            if pornshop5 == True:
                if bonus == True:
                    textbutton _("Watching Porn Alone {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("pornshop5", locked=False)
                else:
                    textbutton _("Totally Legitimate DVD Store {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("pornshop5", locked=False)
            elif bonus == True:
                text _("Watching Porn Alone")
            else:
                text _("Totally Legitimate DVD Store")
            if makotodorm5 == True:
                textbutton _("Completely Platonic {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotodorm5", locked=False)
            else:
                text _("Completely Platonic")
            if pornshop10 == True:
                textbutton _("Rising of the Tide {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("pornshop10", locked=False)
            else:
                text _("Rising of the Tide")
            if makotonew1 == True:
                textbutton _("Frogger {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotonew1", locked=False)
            else:
                text _("Frogger")
            if makotonew2 == True:
                textbutton _("Sowing the Seeds {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotonew2", locked=False)
            else:
                text _("Sowing the Seeds")
            if makotonew3 == True:
                textbutton _("Egg Tooth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotonew3", locked=False)
            else:
                text _("Egg Tooth")
            if pornshop15 == True:
                textbutton _("Fishing For Love {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("pornshop15", locked=False)
            else:
                text _("Fishing For Love")
            if makotolust5 == True:
                if bonus == True:
                    textbutton _("Quid Pro Quo {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makotolust5", locked=False)
                else:
                    textbutton _("Censored Makoto Event {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makotolust5", locked=False)
            elif bonus == True:
                text _("{color=FF85FD}Quid Pro Quo{/color}")
            else:
                text _("{color=FF85FD}Censored Makoto Event{/color}")
            if makotoinvite1 == True:
                textbutton _("Declaration of War {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotoinvite1", locked=False)
            else:
                text _("{color=778EFF}Declaration of War{/color}")
            if makotoinvite2 == True:
                if bonus == True:
                    textbutton _("Studious Teen Virgin {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makotoinvite2", locked=False)
                else:
                    textbutton _("Studious Virgin {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makotoinvite2", locked=False)
            elif bonus == True:
                text _("{color=778EFF}Studious Teen Virgin{/color}")
            else:
                text _("{color=778EFF}Studious Virgin{/color}")
            if pornshop20 == True:
                textbutton _("Aftermath {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("pornshop20", locked=False)
            else:
                text _("Aftermath")
            if makotodorm20 == True:
                textbutton _("Residual Sadness {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotodorm20", locked=False)
            else:
                text _("Residual Sadness")
            if pornshop25 == True:
                textbutton _("Service Charge {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("pornshop25", locked=False)
            else:
                text _("Service Charge")
            if makotodorm25 == True:
                textbutton _("Bluejay {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotodorm25", locked=False)
            else:
                text _("Bluejay")
            text _("-----------------------------------------------------------")
            if makotolust10 == True:
                textbutton _("Semblance of a Soul {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotolust10", locked=False)
            else:
                text _("{color=FF85FD}Semblance of a Soul{/color}")
            if makotowinterbeach1 == True:
                if bonus == True:
                    textbutton _("Condoms in the Sand {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makotowinterbeach1", locked=False)
                else:
                    textbutton _("Jammies in the Sand {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makotowinterbeach1", locked=False)
            elif bonus == True:
                text _("Condoms in the Sand")
            else:
                text _("Jammies in the Sand")
            if makotowinterbeach2 == True:
                textbutton _("Humans With Hollow Bones {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotowinterbeach2", locked=False)
            else:
                text _("Humans With Hollow Bones")
            if makotowinterbeach3 == True:
                textbutton _("I'm Not Here {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotowinterbeach3", locked=False)
            else:
                text _("I'm Not Here")
            if makotowinterbeach4 == True:
                textbutton _("Something, Somewhere {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotowinterbeach4", locked=False)
            else:
                text _("Something, Somewhere")
            if makotolust20 == True:
                textbutton _("Hot Water {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotolust20", locked=False)
            elif makotolust20skip == True:
                text _("{color=EF1A1A}{s}Cold Water{/s}{/color}")
            else:
                text _("{color=FF85FD}Hot Water{/color}")
            text _("-----------------------------------------------------------")
            if sadgirls1 == True:
                textbutton _("Whispers of the World {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sadgirls1", locked=False)
            else:
                text _("Whispers of the World")
            if sadgirls7 == True:
                textbutton _("Parallelogram {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sadgirls7", locked=False)
            else:
                text _("Parallelogram")
            if makotolust30 == True:
                textbutton _("White Oak Doors {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotolust30", locked=False)
            elif makotolust30skip == True:
                text _("{color=EF1A1A}{s}Daddy's Girl{/s}{/color}")
            else:
                text _("{color=FF85FD}White Oak Doors{/color}")
            if sadgirls8 == True:
                textbutton _("A Beautiful Mind {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sadgirls8", locked=False)
            else:
                text _("A Beautiful Mind")
            if makotospecial50 == True:
                textbutton _("Young Cardinals {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotospecial50", locked=False)
            else:
                text _("Young Cardinals")
            if makotopool55 == True:
                textbutton _("Cool Sex Tips {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotopool55", locked=False)
            else:
                text _("Cool Sex Tips")
            if makotodorm55p1 == True:
                textbutton _("Bra Shopping {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotodorm55p1", locked=False)
            else:
                text _("Bra Shopping")
            if makotodorm55p2 == True:
                textbutton _("Suffer the Same {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotodorm55p2", locked=False)
            else:
                text _("Suffer the Same")
            text _("-----------------------------------------------------------")
            if sportswars19 == True:
                textbutton _("The Pit of Despair {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars19", locked=False)
            else:
                text _("The Pit of Despair")
            if makotospring1 == True:
                textbutton _("Midnight Snack {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotospring1", locked=False)
            else:
                text _("Midnight Snack")
            if makotospring2 == True:
                textbutton _("T Is For Time (Trees & Threes) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotospring2", locked=False)
            else:
                text _("T Is For Time (Trees & Threes)")
            if halloweenmakoto1 == True:
                textbutton _("Six Ways From Sunday {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenmakoto1", locked=False)
            else:
                text _("Six Ways From Sunday")
            if halloweenmakoto2 == True:
                textbutton _("Precious Little Life {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenmakoto2", locked=False)
            else:
                text _("Precious Little Life")
            if halloweenmakoto3 == True:
                textbutton _("Transpacific Sadness Symposium IV: TALKATIVE OBLONG MIRROR {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenmakoto3", locked=False)
            else:
                text _("Transpacific Sadness Symposium IV: TALKATIVE OBLONG MIRROR")
            if makotospring3 == True:
                textbutton _("The World, Alive (Ant Farm) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotospring3", locked=False)
            else:
                text _("The World, Alive (Ant Farm)")
            if beachsixmakoto1 == True:
                textbutton _("Black Mass {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixmakoto1", locked=False)
            else:
                text _("Black Mass")
            if beachsixmakoto2 == True:
                textbutton _("A Matter of Time {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixmakoto2", locked=False)
            else:
                text _("A Matter of Time")
            textbutton _("Back") action ShowMenu('gamemenumakoto')

screen gamemenumiku():

    tag menu
    if mikumenuoutfit is not None and renpy.loadable(mikumenuoutfit) :
        add mikumenuoutfit
    else :
        add "game_menumiku.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#ff8112}Height: 5'0/153cm{/color}") style "profile"
        text ("{color=#ff8112}Birthday: June 8th{/color}") style "profile"
        text ("\n{color=#ff8112}Affection: [miku_love]{/color}") style "profile"
        text ("{color=#ff8112}Lust: [miku_lust]{/color}") style "profile"
        text ("{color=#ff8112}Headpats: [mikupats]{/color}") style "profile"
        text ("{color=#ff8112}Events: [mikupoint]/32{/color}") style "profile"

    imagebutton:
        idle "mikuevrep1.png"
        hover "mikuevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('mikutracker')

    if bonus == True:
        if mikudorm25 == False:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')
        else:
            imagebutton:
                idle "subscribestar/images2/mikuthighrep1.png"
                hover "subscribestar/images2/mikuthighrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('mikureplays')

    if mikunudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('mikuphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('mikuphone')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(miku_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen mikutracker():

    tag menu

    use game_menu(_("Miku Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=ff8112}Miku Maruyama ([miku_love] Affection){/color}"
            if firsttimesoccerfield == True:
                textbutton _("Daytime Stalking Pass {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimesoccer", locked=False)
            else:
                text _("Daytime Stalking Pass")
            if mikufirsthall == True:
                textbutton _("Behind Closed Doors {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikufirsthall", locked=False)
            else:
                text _("Behind Closed Doors")
            if soccer5 == True:
                textbutton _("It's Always Sunny in Kumon-mi {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("soccer5", locked=False)
            else:
                text _("It's Always Sunny in Kumon-mi")
            if mikudorm5 == True:
                textbutton _("Broken Bones {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm5", locked=False)
            else:
                text _("Broken Bones")
            if soccer10 == True:
                textbutton _("Nightvision {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("soccer10", locked=False)
            else:
                text _("Nightvision")
            if mikudorm10 == True:
                textbutton _("You and Me and the Night {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm10", locked=False)
            else:
                text _("You and Me and the Night")
            if soccer15 == True:
                textbutton _("Hormones Running Wild {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("soccer15", locked=False)
            else:
                text _("Hormones Running Wild")
            if mikudorm15 == True:
                textbutton _("Moments Like This {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm15", locked=False)
            else:
                text _("Moments Like This")
            if soccer20 == True:
                textbutton _("Coach {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("soccer20", locked=False)
            else:
                text _("Coach")
            if soccer25 == True:
                if bonus == True:
                    textbutton _("Thighs On-Demand {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("soccer25", locked=False)
                else:
                    textbutton _("Leg Event {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("soccer25", locked=False)
            elif bonus == True:
                text _("Thighs On-Demand")
            else:
                text _("Leg Event")
            if mikudorm25 == True:
                textbutton _("Scaredy Cat {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm25", locked=False)
            else:
                text _("Scaredy Cat")
            if soccer30 == True:
                textbutton _("An Extra Set of Arms {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("soccer30", locked=False)
            else:
                text _("An Extra Set of Arms")
            if mikudorm30 == True:
                textbutton _("One. Two. Three. {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm30", locked=False)
            else:
                text _("One. Two. Three.")
            text _("-----------------------------------------------------------")
            if soccer35 == True:
                textbutton _("Loxonin {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("soccer35", locked=False)
            else:
                text _("Loxonin")
            if mikuwinterbeach1 == True:
                textbutton _("To Sleep, Perchance to Dream {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuwinterbeach1", locked=False)
            else:
                text _("To Sleep, Perchance to Dream")
            if mikudorm35 == True:
                textbutton _("Triple Whammy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm35", locked=False)
            else:
                text _("Triple Whammy")
            if mikudorm40 == True:
                textbutton _("Speed of Light {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm40", locked=False)
            else:
                text _("Speed of Light")
            if mikudorm45 == True:
                textbutton _("Acute Love Triangle {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm45", locked=False)
            else:
                text _("Acute Love Triangle")
            if mikudorm45p2 == True:
                textbutton _("Chrysalis {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm45p2", locked=False)
            else:
                text _("Chrysalis")
            if mikuspecial50 == True:
                textbutton _("Someone Else's Skin {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuspecial50", locked=False)
            else:
                text _("Someone Else's Skin")
            if mikudorm50 == True:
                textbutton _("The Devil & God Are Raging Inside Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm50", locked=False)
            else:
                text _("The Devil & God Are Raging Inside Me")
            text _("-----------------------------------------------------------")
            if mikuinvite1 == True:
                textbutton _("Breakaway {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuinvite1", locked=False)
            else:
                text _("{color=778EFF}Breakaway{/color}")
            if mikuinvite2 == True:
                textbutton _("Fair is Fair {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuinvite2", locked=False)
            else:
                text _("{color=778EFF}Fair is Fair{/color}")
            if mikupool55 == True:
                textbutton _("Voice of Vibration {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikupool55", locked=False)
            else:
                text _("Voice of Vibration")
            if mikudorm55p1 == True:
                textbutton _("Essence of Eiderdown {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm55p1", locked=False)
            else:
                text _("Essence of Eiderdown")
            if mikudorm55p2 == True:
                textbutton _("Rostrum of Recollection {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikudorm55p2", locked=False)
            else:
                text _("Rostrum of Recollection")
            text _("-----------------------------------------------------------")
            if mikuspring1 == True:
                textbutton _("Captain Sorrow {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuspring1", locked=False)
            else:
                text _("Captain Sorrow")
            if mikuspring2 == True:
                textbutton _("Bonerville {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuspring2", locked=False)
            else:
                text _("Bonerville")
            if mikuspring3 == True:
                textbutton _("The Boys {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuspring3", locked=False)
            else:
                text _("The Boys")
            if mikuspring4 == True:
                textbutton _("Live Fast, Die Young {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuspring4", locked=False)
            else:
                text _("Live Fast, Die Young")
            if mikuspring5 == True:
                textbutton _("The Gazelle {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikuspring5", locked=False)
            else:
                text _("The Gazelle")
            if mikulust5 == True:
                textbutton _("Practice Makes Perfect {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mikulust5", locked=False)
            else:
                text _("{color=FF85FD}Practice Makes Perfect{/color}")
            textbutton _("Back") action ShowMenu('gamemenumiku')

screen gamemenufutaba():

    tag menu
    if futabamenuoutfit is not None and renpy.loadable(futabamenuoutfit) :
        add futabamenuoutfit
    else :
        add "game_menufutaba.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#9326ff}Height: 5'7/171cm{/color}") style "profile"
        text ("{color=#9326ff}Birthday: November 28th{/color}") style "profile"
        text ("\n{color=#9326ff}Affection: [futaba_love]{/color}") style "profile"
        text ("{color=#9326ff}Lust: [futaba_lust]{/color}") style "profile"
        text ("{color=#9326ff}Headpats: [futabapats]{/color}") style "profile"
        if futabamiss < 1:
            text ("{color=#9326ff}Events: [futabapoint]/40{/color}") style "profile"
        else:
            text ("{color=#9326ff}Events: [futabapoint]/40{/color} {color=#FF0000}([futabamiss] Missed){/color}") style "profile"

    imagebutton:
        idle "futabaevrep1.png"
        hover "futabaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('futabatracker')

    if bonus == True:
        if futabadorm15 == False:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')
        else:
            imagebutton:
                idle "subscribestar/images2/futababoobrep1.png"
                hover "subscribestar/images2/futababoobrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('futabareplays')

        if futabanudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('futabaphone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('futabaphone')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(futaba_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen futabatracker():

    tag menu

    use game_menu(_("Futaba Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=9326ff}Futaba Fukuyama ([futaba_love] Affection){/color}"
            if firsttimelibrary == True:
                textbutton _("Impossible Blossoms {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimelibrary", locked=False)
            else:
                text _("Impossible Blossoms")
            if futabafall == True:
                textbutton _("Fan Fiction {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabafall", locked=False)
            else:
                text _("Fan Fiction")
            if library10 == True:
                textbutton _("Upside Down {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library10", locked=False)
            else:
                text _("Upside Down")
            if futabafirsthall == True:
                textbutton _("Unidentical Twins {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabafirsthall", locked=False)
            else:
                text _("Unidentical Twins")
            if futabafirstvisit == True:
                textbutton _("Under the Radar {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabafirstvisit", locked=False)
            else:
                text _("Under the Radar")
            if futabadorm10 == True:
                textbutton _("Cutting Through Cocoons {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabadorm10", locked=False)
            else:
                text _("Cutting Through Cocoons")
            if library15 == True:
                textbutton _("Self-Insert {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library15", locked=False)
            else:
                text _("Self-Insert")
            if futabanew1 == True:
                textbutton _("Broken Flowers {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabanew1", locked=False)
            else:
                text _("Broken Flowers")
            if futabanew2 == True:
                textbutton _("Great Burdock Leaves {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabanew2", locked=False)
            else:
                text _("Great Burdock Leaves")
            if futabanew3 == True:
                textbutton _("Clam's Tongue {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabanew3", locked=False)
            else:
                text _("Clam's Tongue")
            if futabadorm15 == True:
                textbutton _("Legs of a Dying Spider {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabadorm15", locked=False)
            else:
                text _("Legs of a Dying Spider")
            if library20 == True:
                textbutton _("Only Child {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library20", locked=False)
            else:
                text _("Only Child")
            if library25 == True:
                textbutton _("A Book About Dragons {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library25", locked=False)
            else:
                text _("A Book About Dragons")
            if futabadorm25 == True:
                textbutton _("Two Hours {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabadorm25", locked=False)
            elif library25 == True and bookdate == False:
                text _("{color=EF1A1A}{s}I Just Want to Be Loved{/s}{/color}")
            else:
                text _("Two Hours")
            if day86 == True:
                if bonus == True:
                    textbutton _("Like Fucking a Cloud {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("day86", locked=False)
                else:
                    textbutton _("Like Hugging a Cloud {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("day86", locked=False)
            elif bonus == True:
                text _("{color=FF85FD}Like Fucking a Cloud{/color}")
            else:
                text _("{color=FF85FD}Like Hugging a Cloud{/color}")
            if library30 == True:
                textbutton _("Under the Table {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library30", locked=False)
            else:
                text _("Under the Table")
            if futabadorm30 == True:
                textbutton _("A Tree Falls in the Forest {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabadorm30", locked=False)
            else:
                text _("A Tree Falls in the Forest")
            if library35 == True:
                textbutton _("No, You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library35", locked=False)
            else:
                text _("No, You")
            if futabadorm35 == True:
                textbutton _("Overload {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabadorm35", locked=False)
            else:
                text _("Overload")
            text _("-----------------------------------------------------------")
            if futabalust10 == True:
                textbutton _("Selfless {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabalust10", locked=False)
            elif futabalust10miss == True:
                text _("{color=EF1A1A}{s}Loveless{/s}{/color}")
            else:
                text _("{color=FF85FD}Selfless{/color}")
            if futabainvite1 == True:
                textbutton _("Sonnet 18 {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabainvite1", locked=False)
            else:
                text _("{color=778EFF}Sonnet 18{/color}")
            if futabainvite2 == True:
                textbutton _("Floral Aura {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabainvite2", locked=False)
            else:
                text _("{color=778EFF}Floral Aura{/color}")
            if futabalust15 == True:
                textbutton _("C'est La Vie {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabalust15", locked=False)
            elif futabalust15skip == True and dormwar9 == True:
                text _("{color=EF1A1A}{s}Mourir. Dormir.{/s}{/color}")
            else:
                text _("{color=FF85FD}C'est La Vie{/color}")
            if futabadorm40 == True:
                textbutton _("Skin (Start Somewhere) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabadorm40", locked=False)
            else:
                text _("Skin (Start Somewhere)")
            if library40 == True:
                textbutton _("Shadowplay {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library40", locked=False)
            else:
                text _("Shadowplay")
            if library40part2 == True:
                textbutton _("Without Running Away {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library40part2", locked=False)
            else:
                text _("Without Running Away")
            if futabadorm45 == True:
                textbutton _("Hall of Mirrors {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabadorm45", locked=False)
            else:
                text _("Hall of Mirrors")
            text _("-----------------------------------------------------------")
            if futabadorm50 == True:
                textbutton _("This Infected Wound {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabadorm50", locked=False)
            else:
                text _("This Infected Wound")
            if library50 == True:
                textbutton _("Bestial Vigor {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("library50", locked=False)
            else:
                text _("Bestial Vigor")
            if futabainvite3 == True:
                textbutton _("Too Blind To See {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabainvite3", locked=False)
            else:
                text _("{color=778EFF}Too Blind To See{/color}")
            if makotofutabafuntimelustevent == True:
                textbutton _("Toys {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makotofutabafuntimelustevent", locked=False)
            elif makotofutabalustskip == True:
                text _("{color=EF1A1A}{s}Grounded{/s}{/color}")
            else:
                text _("{color=FF85FD}Toys{/color}")
            if futabaspecial60p1 == True:
                textbutton _("Book Burning {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabaspecial60p1", locked=False)
            else:
                text _("Book Burning")
            if futabaspecial60p2 == True:
                textbutton _("Pg. 99 {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabaspecial60p2", locked=False)
            else:
                text _("Pg. 99")
            if futabaspecial60p3 == True:
                textbutton _("Fish Eyes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabaspecial60p3", locked=False)
            else:
                text _("Fish Eyes")
            text _("-----------------------------------------------------------")
            if futabalust25 == True:
                textbutton _("Weapons of Mass Destruction {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabalust25", locked=False)
            else:
                text _("{color=FF85FD}Weapons of Mass Destruction{/color}")
            if futabaspring1 == True:
                textbutton _("My Curse {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabaspring1", locked=False)
            else:
                text _("My Curse")
            if beachfive9 == True:
                textbutton _("Transpacific Sadness Symposium II: SISTER SOFTSKIN {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive9", locked=False)
            else:
                text _("Transpacific Sadness Symposium II: SISTER SOFTSKIN")
            if futabalust40 == True:
                textbutton _("The Meat in the Hole in the Wall in My Room {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabalust40", locked=False)
            elif futabalust40miss == True:
                text _("{color=EF1A1A}{s}Maisie Belle{/s}{/color}")
            else:
                text _("{color=FF85FD}The Meat in the Hole in the Wall in My Room{/color}")
            if futabaspring2 == True:
                textbutton _("The Taking Tree {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("futabaspring2", locked=False)
            else:
                text _("The Taking Tree")
            if beachsixfutaba1 == True:
                textbutton _("Spam {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixfutaba1", locked=False)
            else:
                text _("Spam")
            textbutton _("Back") action ShowMenu('gamemenufutaba')

screen gamemenurin():

    tag menu
    if rinmenuoutfit is not None and renpy.loadable(rinmenuoutfit) :
        add rinmenuoutfit
    else :
        add "game_menurin.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#a30041}Height: 5'4/163cm{/color}") style "profile"
        text ("{color=#a30041}Birthday: February 14th{/color}") style "profile"
        text ("\n{color=#a30041}Affection: [rin_love]{/color}") style "profile"
        text ("{color=#a30041}Lust: N/A{/color}") style "profile"
        text ("{color=#a30041}Headpats: 0{/color}") style "profile"
        if rinmiss < 1:
            text ("{color=#a30041}Events: [rinpoint]/34{/color}") style "profile"
        else:
            text ("{color=#a30041}Events: [rinpoint]/34{/color} {color=#FF0000}([rinmiss] Missed){/color}") style "profile"

    imagebutton:
        idle "rinevrep1.png"
        hover "rinevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('rintracker')

    if postnodokachain1 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/rinotoharep1.png"
            hover "subscribestar/images2/rinotoharep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('rinreplays')

    if rinnudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('rinphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('rinphone')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(rin_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen rintracker():

    tag menu

    use game_menu(_("Rin Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=a30041}Rin Rokuhara ([rin_love] Affection){/color}"
            if firsttimecafe == True:
                textbutton _("Guinea Pig {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("firsttimecafe", locked=False)
            else:
                text _("Guinea Pig")
            if cafesugar == True:
                textbutton _("The Flavor of Love{b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafesugar", locked=False)
            else:
                text _("The Flavor of Love")
            if cafe10 == True:
                textbutton _("Haruka {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe10", locked=False)
            else:
                text _("Haruka")
            if rinfirsthall == True:
                textbutton _("Locked Out {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinfirsthall", locked=False)
            else:
                text _("Locked Out")
            if rinfirstvisit == True:
                textbutton _("Skulls {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinfirstvisit", locked=False)
            else:
                text _("Skulls")
            if rindorm10 == True:
                textbutton _("Rin's Secret {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm10", locked=False)
            else:
                text _("Rin's Secret")
            if cafe15 == True:
                textbutton _("Window of the Waking Mind {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe15", locked=False)
            else:
                text _("Window of the Waking Mind")
            if rindorm15 == True:
                textbutton _("Boundaries {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm15", locked=False)
            else:
                text _("Boundaries")
            if cafe20 == True:
                textbutton _("Nothing Was Missing, Except Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe20", locked=False)
            else:
                text _("Nothing Was Missing, Except Me")
            if rindorm20 == True:
                textbutton _("Delirium {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm20", locked=False)
            else:
                text _("Delirium")
            if cafe25 == True:
                textbutton _("Good Day, Humans {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe25", locked=False)
            else:
                text _("Good Day, Humans")
            if rindorm25 == True:
                textbutton _("Sock Fetish {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm25", locked=False)
            else:
                text _("Sock Fetish")
            if cafe30 == True:
                textbutton _("Nothing Was Different {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe30", locked=False)
            else:
                text _("Nothing Was Different")
            if rindorm30 == True:
                textbutton _("Two Steps Back {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm30", locked=False)
            else:
                text _("Two Steps Back")
            if rindorm35 == True:
                textbutton _("Ten Steps Forward {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm35", locked=False)
            else:
                text _("Ten Steps Forward")
            if cafe35 == True:
                textbutton _("I Died With You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe35", locked=False)
            elif rindorm35 == True and rininvite == False:
                text _("{color=EF1A1A}{s}Love Life, Let Go{/s}{/color}")
            else:
                text _("I Died With You")
            text _("-----------------------------------------------------------")
            if cafe40 == True:
                textbutton _("Sketchy Basement {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe40", locked=False)
            else:
                text _("Sketchy Basement")
            if rindorm40 == True:
                textbutton _("Semantics {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm40", locked=False)
            else:
                text _("Semantics")
            if cafe45 == True:
                textbutton _("Debatably Bisexual Musicians {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe45", locked=False)
            else:
                text _("Debatably Bisexual Musicians")
            if rindorm45 == True:
                textbutton _("The Art of Never Knowing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm45", locked=False)
            else:
                text _("The Art of Never Knowing")
            if cafe50 == True:
                textbutton _("The Paragon of Not Worrying About Stuff {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("cafe50", locked=False)
            else:
                text _("The Paragon of Not Worrying About Stuff")
            if rindorm50 == True:
                textbutton _("Technicolored Happiness Explosion {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm50", locked=False)
            else:
                text _("Technicolored Happiness Explosion")
            if rindorm50special == True:
                textbutton _("Lifejacket {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm50special", locked=False)
            else:
                text _("Lifejacket")
            if rindate50 == True:
                textbutton _("The Happiest Girl in the World {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindate50", locked=False)
            elif rindorm50special == True and rinbetrayed == True:
                text _("{color=EF1A1A}{s}The Raw Sting of Lacerated Skin{/s}{/color}")
            else:
                text _("The Happiest Girl in the World")
            text _("-----------------------------------------------------------")
            if rindorm55 == True:
                textbutton _("Disaster Lesbian {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm55", locked=False)
            else:
                text _("Disaster Lesbian")
            if rindorm55p2 == True:
                textbutton _("Hot Boy Summer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rindorm55p2", locked=False)
            else:
                text _("Hot Boy Summer")
            if rinspecial55 == True:
                textbutton _("Ever Fallen In Love {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinspecial55", locked=False)
            else:
                text _("Ever Fallen In Love")
            text _("-----------------------------------------------------------")
            if rinspring1 == True:
                textbutton _("Anthem of the Heart {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinspring1", locked=False)
            else:
                text _("Anthem of the Heart")
            if rinspring2 == True:
                textbutton _("Voices of a Distant Star {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinspring2", locked=False)
            else:
                text _("Voices of a Distant Star")
            if rinspring3 == True:
                textbutton _("Sex Dreams {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinspring3", locked=False)
            elif harukaspring1miss == True:
                text _("{color=EF1A1A}{s}Virgin Nightmares{/s}{/color}")
            else:
                text _("Sex Dreams")
            if rinspring4 == True:
                textbutton _("Voice of Reason {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinspring4", locked=False)
            else:
                text _("Voice of Reason")
            if rinspring5 == True:
                textbutton _("Dear Sensei (Red Sea) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinspring5", locked=False)
            else:
                text _("Dear Sensei (Red Sea)")
            if rinspring6 == True:
                textbutton _("Love Long Overdue {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rinspring6", locked=False)
            else:
                text _("Love Long Overdue")
            if dormwarsfiverin1 == True:
                textbutton _("The First Time Since the Last Time {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfiverin1", locked=False)
            else:
                text _("The First Time Since the Last Time")
            textbutton _("Back") action ShowMenu('gamemenurin')

screen gamemenumolly():

    tag menu
    if mollymenuoutfit is not None and renpy.loadable(mollymenuoutfit) :
        add mollymenuoutfit
    else :
        add "game_menumolly.png"

    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#4FCB80}Height: 5'1/155cm{/color}") style "profile"
        text ("{color=#4FCB80}Birthday: March 18th{/color}") style "profile"
        text ("\n{color=#4FCB80}Affection: [molly_love]{/color}") style "profile"
        text ("{color=#4FCB80}Lust: [molly_lust]{/color}") style "profile"
        text ("{color=#4FCB80}Headpats: [mollypats]{/color}") style "profile"
        if mollymiss < 1:
            text ("{color=#4FCB80}Events: [mollypoint]/25{/color}") style "profile"
        else:
            text ("{color=#4FCB80}Events: [mollypoint]/25{/color} {color=#FF0000}([mollymiss] Missed){/color}") style "profile"

    imagebutton:
        idle "mollyevrep1.png"
        hover "mollyevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('mollytracker')

    if mollynudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('mollyphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('mollyphone')

    if mollydorm20 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/mollymastrep1.png"
            hover "subscribestar/images2/mollymastrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('mollyreplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(molly_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen mollytracker():

    tag menu

    use game_menu(_("Molly Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=4FCB80}Molly MacCormack ([molly_love] Affection){/color}"
            if mollycafe1 == True:
                textbutton _("NTR & Pregnancy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe1", locked=False)
            else:
                text _("NTR & Pregnancy")
            if mollyfirsthall == True:
                textbutton _("The Cult of Molly {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollyfirsthall", locked=False)
            else:
                text _("The Cult of Molly")
            if mollycafe5 == True:
                textbutton _("Remnants of Forgotten Memes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe5", locked=False)
            else:
                text _("Remnants of Forgotten Memes")
            if mollydorm5 == True:
                textbutton _("Torrent of Power {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollydorm5", locked=False)
            else:
                text _("Torrent of Power")
            if mollycafe10 == True:
                textbutton _("Something Out of a Nukige {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe10", locked=False)
            else:
                text _("Something Out of a Nukige")
            if mollydorm10 == True:
                textbutton _("The Dark Entity {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollydorm10", locked=False)
            else:
                text _("The Dark Entity")
            text _("-----------------------------------------------------------")
            if mollycafe15 == True:
                textbutton _("Onward to Valhalla {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe15", locked=False)
            else:
                text _("Onward to Valhalla")
            if mollydorm15 == True:
                textbutton _("Unpaid Promotion {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollydorm15", locked=False)
            else:
                text _("Unpaid Promotion")
            if mollycafe20 == True:
                textbutton _("The Legacy of Thaum Pt. II {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe20", locked=False)
            else:
                text _("The Legacy of Thaum Pt. II")
            if mollydorm20 == True:
                textbutton _("Ahead of the Curve {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollydorm20", locked=False)
            else:
                text _("Ahead of the Curve")
            if mollycafe25 == True:
                textbutton _("Resurrection Sickness {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe25", locked=False)
            else:
                text _("Resurrection Sickness")
            if mollycafe25p2 == True:
                textbutton _("Tír na nÓg {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe25p2", locked=False)
            else:
                text _("Tír na nÓg")
            if mollydorm25 == True:
                textbutton _("Transmogrification {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollydorm25", locked=False)
            else:
                text _("Transmogrification")
            if mollydorm30 == True:
                textbutton _("Walkthrough {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollydorm30", locked=False)
            else:
                text _("Walkthrough")
            text _("-----------------------------------------------------------")
            if mollycafe30p1 == True:
                textbutton _("Hook {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe30p1", locked=False)
            else:
                text _("Hook")
            if mollycafe30p2 == True:
                textbutton _("A Night to Remember {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycafe30p2", locked=False)
            else:
                text _("A Night to Remember")
            if mollydate35p1 == True:
                textbutton _("Anar'alah Belore {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollydate35p1", locked=False)
            else:
                text _("Anar'alah Belore")
            if mollydate35p2 == True:
                textbutton _("Sardines {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollydate35p2", locked=False)
            else:
                text _("Sardines")
            text _("-----------------------------------------------------------")
            if mollycamp1 == True:
                textbutton _("Corrupted Blood {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollycamp1", locked=False)
            else:
                text _("Corrupted Blood")
            if mollyspring1 == True:
                textbutton _("Level One {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollyspring1", locked=False)
            else:
                text _("Level One")
            if mollyspring2 == True:
                textbutton _("Fated to Love You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollyspring2", locked=False)
            else:
                text _("Fated to Love You")
            if mollylust10 == True:
                textbutton _("The Farmer’s Daughter {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollylust10", locked=False)
            elif mollylust10miss == True:
                text _("{color=EF1A1A}{s}Goblin Queen{/s}{/color}")
            else:
                text _("{color=FF85FD}The Farmer’s Daughter{/color}")
            if mollyinvite1 == True:
                textbutton _("No Murder in the House {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollyinvite1", locked=False)
            else:
                text _("{color=778EFF}No Murder in the House{/color}")
            if mollyinvite2 == True:
                textbutton _("Pixels & Polygons {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("mollyinvite2", locked=False)
            else:
                text _("{color=778EFF}Pixels & Polygons{/color}")
            if beachsixmolly1 == True:
                textbutton _("Power-Leveling {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixmolly1", locked=False)
            else:
                text _("{color=FF85FD}Power-Leveling{/color}")
            textbutton _("Back") action ShowMenu('gamemenumolly')

screen gamemenutsuneyo():

    tag menu
    if tsuneyomenuoutfit is not None and renpy.loadable(tsuneyomenuoutfit) :
        add tsuneyomenuoutfit
    else :
        add "game_menutsuneyo.png"

    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#C8B330}Height: 5'10/177cm{/color}") style "profile"
        text ("{color=#C8B330}Birthday: October 6th{/color}") style "profile"
        text ("\n{color=#C8B330}Affection: [tsuneyo_love]{/color}") style "profile"
        text ("{color=#C8B330}Lust: [tsuneyo_lust]{/color}") style "profile"
        text ("{color=#C8B330}Headpats: 0{/color}") style "profile"
        text ("{color=#C8B330}Events: [tsuneyopoint]/26{/color}") style "profile"

    imagebutton:
        idle "tsuneyoevrep1.png"
        hover "tsuneyoevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('tsuneyotracker')

    if halloweentsuneyo1 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/tsuneyosekairep1.png"
            hover "subscribestar/images2/tsuneyosekairep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('tsuneyoreplays')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(tsuneyo_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen tsuneyotracker():

    tag menu

    use game_menu(_("Tsuneyo Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=C8B330}Tsuneyo Tojo ([tsuneyo_love] Affection){/color}"
            if ramen1 == True:
                textbutton _("Snake Venom {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ramen1", locked=False)
            else:
                text _("Snake Venom")
            if tsuneyofirsthall == True:
                textbutton _("The Life of a Blue Whale {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyofirsthall", locked=False)
            else:
                text _("The Life of a Blue Whale")
            if ramen5 == True:
                textbutton _("Between the Slurps of Pork Broth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ramen5", locked=False)
            else:
                text _("Between the Slurps of Pork Broth")
            if tsuneyodorm5 == True:
                textbutton _("Drug Use & Jump-Rope {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyodorm5", locked=False)
            else:
                text _("Drug Use & Jump-Rope")
            if ramen10 == True:
                textbutton _("A Short List {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ramen10", locked=False)
            else:
                text _("A Short List")
            if tsuneyodorm10 == True:
                textbutton _("The Man Who Loves Nothing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyodorm10", locked=False)
            else:
                text _("The Man Who Loves Nothing")
            text _("-----------------------------------------------------------")
            if ramen15 == True:
                textbutton _("Seeds {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ramen15", locked=False)
            else:
                text _("Seeds")
            if tsuneyodorm15 == True:
                textbutton _("Moe Fan Service {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyodorm15", locked=False)
            else:
                text _("Moe Fan Service")
            if tsuneyodorm20 == True:
                textbutton _("Fucking...Or What it Means to Live (Shio & Shoyu) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyodorm20", locked=False)
            else:
                text _("Fucking...Or What it Means to Live (Shio & Shoyu)")
            if ramen20 == True:
                textbutton _("Blackout {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ramen20", locked=False)
            else:
                text _("Blackout")
            if ramen25 == True:
                textbutton _("Like Noodles in the Wind {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ramen25", locked=False)
            else:
                text _("Like Noodles in the Wind")
            if ramen25p2 == True:
                textbutton _("Green Onions and Contraceptives {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ramen25p2", locked=False)
            else:
                text _("Green Onions and Contraceptives")
            if tsuneyodorm25 == True:
                textbutton _("Unsleeping Aegis {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyodorm25", locked=False)
            else:
                text _("Unsleeping Aegis")
            if ramen30 == True:
                textbutton _("Things Like Stairs {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ramen30", locked=False)
            else:
                text _("Things Like Stairs")
            text _("-----------------------------------------------------------")
            if tsuneyoslumber1 == True:
                textbutton _("With Her {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyoslumber1", locked=False)
            else:
                text _("With Her")
            if tsuneyoslumber2 == True:
                textbutton _("Stripped Away {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyoslumber2", locked=False)
            else:
                text _("Stripped Away")
            if tsuneyoslumber3 == True:
                textbutton _("Sudden Light {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyoslumber3", locked=False)
            else:
                text _("Sudden Light")
            text _("-----------------------------------------------------------")
            if tsuneyospring1 == True:
                textbutton _("Ramen Girl {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyospring1", locked=False)
            else:
                text _("Ramen Girl")
            if tsuneyospring2 == True:
                textbutton _("Soothsayer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyospring2", locked=False)
            else:
                text _("Soothsayer")
            if tsuneyospring3 == True:
                textbutton _("TH15 15NT M3 {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyospring3", locked=False)
            else:
                text _("TH15 15NT M3")
            if halloweentsuneyo1 == True:
                textbutton _("ELATION PROTOCOL 99: NOODLEFOOT DISCO {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentsuneyo1", locked=False)
            else:
                text _("ELATION PROTOCOL 99: NOODLEFOOT DISCO")
            if tsuneyospring4 == True:
                textbutton _("Thomas Mato, M.D. {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyospring4", locked=False)
            else:
                text _("Thomas Mato, M.D.")
            if tsuneyospring5 == True:
                textbutton _("Yamato Nadeshiko {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyospring5", locked=False)
            else:
                text _("Yamato Nadeshiko")
            if tsuneyospring6 == True:
                textbutton _("WORMGOD54 {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsuneyospring6", locked=False)
            else:
                text _("WORMGOD54")
            if beachsixtsuneyo1 == True:
                textbutton _("Defilement of a Temple {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixtsuneyo1", locked=False)
            else:
                text _("Defilement of a Temple")
            if beachsixtsuneyo2 == True:
                textbutton _("Denouement {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixtsuneyo2", locked=False)
            else:
                text _("Denouement")
            textbutton _("Back") action ShowMenu('gamemenutsuneyo')

screen gamemenusara():

    tag menu
    if saramenuoutfit is not None and renpy.loadable(saramenuoutfit) :
        add saramenuoutfit
    else :
        add "game_menusara.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#365D4C}Height: 5'4/162cm{/color}") style "profile"
        text ("{color=#365D4C}Birthday: July 6th{/color}") style "profile"
        text ("\n{color=#365D4C}Affection: [sara_love]{/color}") style "profile"
        text ("{color=#365D4C}Lust: [sara_lust]{/color}") style "profile"
        text ("{color=#365D4C}Headpats: [sarapats]{/color}") style "profile"
        if saramiss < 1:
            text ("{color=#365D4C}Events: [sarapoint]/20{/color}") style "profile"
        else:
            text ("{color=#365D4C}Events: [sarapoint]/20{/color} {color=#FF0000}([saramiss] Missed){/color}") style "profile"

    imagebutton:
        idle "saraevrep1.png"
        hover "saraevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('saratracker')

    if bonus == True:
        if sarasex == False:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')
        else:
            imagebutton:
                idle "subscribestar/images2/saraeatout1.png"
                hover "subscribestar/images2/saraeatout2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('sarareplays')

        if saranudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('saraphone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('saraphone')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(sara_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen saratracker():

    tag menu

    use game_menu(_("Sara Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=365D4C}Sara Sakakibara ([sara_love] Affection){/color}"
            if saradate1 == True:
                textbutton _("A Woman's Heart {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saradate1", locked=False)
            else:
                text _("A Woman's Heart")
            if saralust5 == True:
                textbutton _("Zero Friction {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saralust5", locked=False)
            elif bar15 == True and sarasex == False:
                text _("{color=EF1A1A}{s}The World Moves too Quickly{/s}{/color}")
            else:
                text _("{color=FF85FD}Zero Friction{/color}")
            if sarainvite1 == True:
                textbutton _("Third Wheel {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sarainvite1", locked=False)
            else:
                text _("{color=778EFF}Third Wheel{/color}")
            if sarainvite2 == True:
                textbutton _("A Mostly Empty Home {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sarainvite2", locked=False)
            else:
                text _("{color=778EFF}A Mostly Empty Home{/color}")
            if saralust10 == True:
                textbutton _("Medical Assistance {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saralust10", locked=False)
            elif halloween8 == True and saralust10 == False:
                text _("{color=EF1A1A}{s}Almost Burning{/s}{/color}")
            else:
                text _("{color=FF85FD}Medical Assistance{/color}")
            text _("-----------------------------------------------------------")
            if saradate10 == True:
                textbutton _("Uptown Girl {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saradate10", locked=False)
            else:
                text _("Uptown Girl")
            if sarabar20 == True:
                textbutton _("She's Always a Woman {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sarabar20", locked=False)
            elif saradate10 == True and sarasex == False:
                text _("{color=EF1A1A}{s}I've Loved These Days{/s}{/color}")
            else:
                text _("She's Always a Woman")
            if sarabar25 == True:
                textbutton _("Tell Me When {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sarabar25", locked=False)
            else:
                text _("Tell Me When")
            if sarabar25p2 == True:
                textbutton _("The Place She Falls Asleep At Night {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sarabar25p2", locked=False)
            else:
                text _("The Place She Falls Asleep At Night")
            if saralust20 == True:
                if bonus == True:
                    textbutton _("Engulfed {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("saralust20x", locked=False)
                else:
                    textbutton _("Engulfed {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("saralust20intro", locked=False)
            elif saralust20skip == True:
                text _("{color=EF1A1A}{s}Swallowed Whole{/s}{/color}")
            else:
                text _("{color=FF85FD}Engulfed{/color}")
            text _("-----------------------------------------------------------")
            if saraspecial30p1 == True:
                textbutton _("The Creaking of the Seventh Step {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saraspecial30p1", locked=False)
            else:
                text _("The Creaking of the Seventh Step")
            if saraspecial30p2 == True:
                textbutton _("Halfway Down the Wishing Well {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saraspecial30p2", locked=False)
            elif saraspecial30p2skip == True:
                text _("{color=EF1A1A}{s}Zoopledoop{/s}{/color}")
            else:
                text _("Halfway Down the Wishing Well")
            if sarabar30 == True:
                textbutton _("Nicolas Cage {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sarabar30", locked=False)
            else:
                text _("Nicolas Cage")
            text _("-----------------------------------------------------------")
            if saracamp1 == True:
                textbutton _("The One With A Happy Ending {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saracamp1", locked=False)
            else:
                text _("The One With A Happy Ending")
            if saracamp2 == True:
                textbutton _("I've Been Thinking About Leaving This Place {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saracamp2", locked=False)
            else:
                text _("I've Been Thinking About Leaving This Place")
            if saraspring1 == True:
                textbutton _("Details in the Fabric {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saraspring1", locked=False)
            else:
                text _("Details in the Fabric")
            if saraspring2 == True:
                textbutton _("Silent Night (Onee-san) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saraspring2", locked=False)
            elif saraspring2miss == True:
                text _("{color=EF1A1A}{s}Sister Says No{/s}{/color}")
            else:
                text _("Silent Night (Onee-san)")
            if saraspring3 == True:
                textbutton _("Worthless Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saraspring3", locked=False)
            elif saraspring3miss == True:
                text _("{color=EF1A1A}{s}Worthless You{/s}{/color}")
            else:
                text _("Worthless Me")
            if saraspring4 == True:
                textbutton _("Two for the Price of One {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saraspring4", locked=False)
            elif saraspring4miss == True:
                text _("{color=EF1A1A}{s}One for the Price of Two{/s}{/color}")
            else:
                text _("Two for the Price of One")
            if saraspring5 == True:
                textbutton _("The Puppeteer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("saraspring5", locked=False)
            elif saraspring5miss == True:
                text _("{color=EF1A1A}{s}The Puppet{/s}{/color}")
            else:
                text _("The Puppeteer")
            textbutton _("Back") action ShowMenu('gamemenusara')

screen gamemenuharuka():

    tag menu
    if harukamenuoutfit is not None and renpy.loadable(harukamenuoutfit) :
        add harukamenuoutfit
    else :
        add "game_menuharuka.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#B02E8C}Height: 5'8/173cm{/color}") style "profile"
        text ("{color=#B02E8C}Birthday: June 20th{/color}") style "profile"
        text ("\n{color=#B02E8C}Affection: [haruka_love]{/color}") style "profile"
        text ("{color=#B02E8C}Lust: [haruka_lust]{/color}") style "profile"
        text ("{color=#B02E8C}Headpats: [harukapats]{/color}") style "profile"
        if harukamiss < 1:
            text ("{color=#B02E8C}Events: [harukapoint]/22{/color}") style "profile"
        else:
            text ("{color=#B02E8C}Events: [harukapoint]/22{/color} {color=#FF0000}([harukamiss] Missed){/color}") style "profile"

    imagebutton:
        idle "harukaevrep1.png"
        hover "harukaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('harukatracker')

    if bonus == True:
        if harukasex == False:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')
        else:
            imagebutton:
                idle "subscribestar/images2/harukadogrep1.png"
                hover "subscribestar/images2/harukadogrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('harukareplays')

        if harukanudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('harukaphone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('harukaphone')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(haruka_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen harukatracker():

    tag menu

    use game_menu(_("Haruka Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=B02E8C}Haruka Hamasaki ([haruka_love] Affection){/color}"
            if harukadate1 == True:
                textbutton _("Drunk Again {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukadate1", locked=False)
            else:
                text _("Drunk Again")
            if harukadate5 == True:
                textbutton _("Invisible Worm {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukadate5", locked=False)
            else:
                text _("Invisible Worm")
            if harukafirstlust == True:
                textbutton _("The Need to be Hurt {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukafirstlust", locked=False)
            elif harukadate5 == True and harukasex == False:
                text _("{color=EF1A1A}{s}Hurt Me{/s}{/color}")
            else:
                text _("{color=FF85FD}The Need to be Hurt{/color}")
            if harukalust10 == True:
                textbutton _("Bad Kitty {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukalust10", locked=False)
            elif halloween14 == True and harukalust10 == False:
                text _("{color=EF1A1A}{s}Fixing Pipes{/s}{/color}")
            else:
                text _("{color=FF85FD}Bad Kitty{/color}")
            if harukadate10 == True:
                textbutton _("Performance Review {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukadate10", locked=False)
            else:
                text _("Performance Review")
            if harukadate15 == True:
                textbutton _("Watching TV Alone {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukadate15", locked=False)
            else:
                text _("Watching TV Alone")
            text _("-----------------------------------------------------------")
            if harukainvite1 == True:
                textbutton _("Shades of Green {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukainvite1", locked=False)
            else:
                text _("{color=778EFF}Shades of Green{/color}")
            if harukainvite2 == True:
                textbutton _("Roses {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukainvite2", locked=False)
            else:
                text _("{color=778EFF}Roses{/color}")
            if harukadate20 == True:
                textbutton _("Sober-ish {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukadate20", locked=False)
            else:
                text _("Sober-ish")
            if harukainvite3 == True:
                textbutton _("Unfiltered Tap Water {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukainvite3", locked=False)
            elif harukadate20 == True and harukasex == False:
                text _("{color=EF1A1A}{s}Worms{/s}{/color}")
            else:
                text _("{color=778EFF}Unfiltered Tap Water{/color}")
            text _("-----------------------------------------------------------")
            if sadgirls2 == True:
                textbutton _("The World Outside The Walls {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sadgirls2", locked=False)
            elif sadgirls2skip == True and sadgirls1 == True:
                text _("{color=EF1A1A}{s}Personal Hell{/s}{/color}")
            else:
                text _("The World Outside The Walls")
            if sadgirls4 == True:
                textbutton _("To Anyone Who Passes By {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sadgirls4", locked=False)
            else:
                text _("To Anyone Who Passes By")
            if sadgirls5 == True:
                textbutton _("Again, I Can't Recall {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sadgirls5", locked=False)
            else:
                text _("Again, I Can't Recall")
            if harukalust25 == True:
                textbutton _("Secret Weapon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukalust25", locked=False)
            elif harukalust25skip == True:
                text _("{color=EF1A1A}{s}Fatal Misfire{/s}{/color}")
            else:
                text _("{color=FF85FD}Secret Weapon{/color}")
            if makihornytrip1 == True:
                textbutton _("Stress Level Midnight {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makihornytrip1", locked=False)
            else:
                text _("Stress Level Midnight")
            if makihornytrip4 == True:
                textbutton _("Conflict of Interest {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makihornytrip4", locked=False)
            else:
                text _("Conflict of Interest")
            if harukadate30 == True:
                textbutton _("Scum {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukadate30", locked=False)
            elif harukadate30skip == True and makihornytrip4 == True:
                text _("{color=EF1A1A}{s}Soap{/s}{/color}")
            else:
                text _("Scum")
            text _("-----------------------------------------------------------")
            if harukacamp1 == True:
                textbutton _("Small Paper Cups {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukacamp1", locked=False)
            else:
                text _("Small Paper Cups")
            if harukaspring1 == True:
                textbutton _("Subhuman {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukaspring1", locked=False)
            elif harukaspring1miss == True:
                text _("{color=EF1A1A}{s}Crisis Averted!{/s}{/color}")
            else:
                text _("Subhuman")
            if harukaspring2 == True:
                textbutton _("Limp-Dicked Loser {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukaspring2", locked=False)
            elif harukaspring2miss == True:
                text _("{color=EF1A1A}{s}Open For Business!{/s}{/color}")
            else:
                text _("Limp-Dicked Loser")
            if harukaspring3 == True:
                textbutton _("This Town, On its Knees {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukaspring3", locked=False)
            elif harukaspring3miss == True:
                text _("{color=EF1A1A}{s}The Ballad of Tebiso{/s}{/color}")
            else:
                text _("This Town, On its Knees")
            if harukaspring4 == True:
                textbutton _("JR East's DC Tilting EMU E353 Series (Kaiji) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("harukaspring4", locked=False)
            else:
                text _("JR East's DC Tilting EMU E353 Series (Kaiji)")
            textbutton _("Back") action ShowMenu('gamemenuharuka')

screen gamemenumaki():

    tag menu
    if makimenuoutfit is not None and renpy.loadable(makimenuoutfit) :
        add makimenuoutfit
    else :
        add "game_menumaki.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#3B84A9}Height: 5'9/176cm{/color}") style "profile"
        text ("{color=#3B84A9}Birthday: November 25th{/color}") style "profile"
        text ("\n{color=#3B84A9}Affection: [maki_love]{/color}") style "profile"
        text ("{color=#3B84A9}Lust: [maki_lust]{/color}") style "profile"
        text ("{color=#3B84A9}Headpats: [makipats]{/color}") style "profile"
        if makimiss < 1:
            text ("{color=#3B84A9}Events: [makipoint]/18{/color}") style "profile"
        else:
            text ("{color=#3B84A9}Events: [makipoint]/18{/color} {color=#FF0000}([makimiss] Missed){/color}") style "profile"

    imagebutton:
        idle "makievrep1.png"
        hover "makievrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('makitracker')

    if bonus == True:
        if harukalust10 == True or makibj == True:
            imagebutton:
                idle "subscribestar/images2/makibjrep1.png"
                hover "subscribestar/images2/makibjrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('makireplays')
        else:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(maki_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen makitracker():

    tag menu

    use game_menu(_("Maki Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=3B84A9}Maki Miyamura ([maki_love] Affection){/color}"
            if makidate1 == True:
                if bonus == True:
                    textbutton _("Beautiful Porn Salesman {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makidate1", locked=False)
                else:
                    textbutton _("Beautiful DVD Salesman {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makidate1", locked=False)
            elif bonus == True:
                text _("Beautiful Porn Salesman")
            else:
                text _("Beautiful DVD Salesman")
            if makidate5 == True:
                textbutton _("Maki Miyamura's Mom-Mode Mission {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makidate5", locked=False)
            else:
                text _("Maki Miyamura's Mom-Mode Mission")
            text _("-----------------------------------------------------------")
            if makidate10 == True:
                textbutton _("A Fair Trade {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makidate10", locked=False)
            else:
                text _("A Fair Trade")
            if makiday351 == True:
                textbutton _("Three Afloat On One Raft {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makiday351", locked=False)
            else:
                text _("Three Afloat On One Raft")
            if makidate15 == True:
                textbutton _("Thank You For Your Business {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makidate15", locked=False)
            elif makiday351 == True and makibj == False or makiday351 == True and harukalust10 == False:
                text _("{color=EF1A1A}{s}Closed for Renovation{/s}{/color}")
            else:
                text _("Thank You For Your Business")
            if makiinvite1 == True:
                if bonus == True:
                    textbutton _("Traveling Lube Dealer {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makiinvite1", locked=False)
                else:
                    textbutton _("Traveling Lotion Dealer {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("makiinvite1", locked=False)
            elif bonus == True:
                text _("{color=778EFF}Traveling Lube Dealer{/size}")
            else:
                text _("{color=778EFF}Traveling Lotion Dealer{/size}")
            if makiinvite2 == True:
                textbutton _("Special Occasions {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makiinvite2", locked=False)
            else:
                text _("{color=778EFF}Special Occasions{/color}")
            text _("-----------------------------------------------------------")
            if sadgirls3 == True:
                textbutton _("Adulting {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sadgirls3", locked=False)
            else:
                text _("Adulting")
            if sadgirls6 == True:
                textbutton _("Rolling Stop (Turned Backwards) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sadgirls6", locked=False)
            else:
                text _("Rolling Stop (Turned Backwards)")
            if makiinv3 == True:
                textbutton _("Baby Steps {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makiinv3", locked=False)
            else:
                text _("{color=778EFF}Baby Steps{/color}")
            if makihornyquestintro == True:
                textbutton _("The Maltese Falcon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makihornyquestintro", locked=False)
            else:
                text _("The Maltese Falcon")
            if makihornytrip2 == True:
                textbutton _("Shut Up & Cum {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makihornytrip2", locked=False)
            elif harumakihornyskip == True and makihornytrip1 == True:
                text _("{color=EF1A1A}{s}You Missed Something Again{/s}{/color}")
            else:
                text _("Shut Up & Cum")
            if makihornytrip3 == True:
                textbutton _("Rotting From the Inside Out {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makihornytrip3", locked=False)
            else:
                text _("Rotting From the Inside Out")
            text _("-----------------------------------------------------------")
            if makicamp1 == True:
                textbutton _("Wires...and the Concept of Breathing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makicamp1", locked=False)
            else:
                text _("Wires...and the Concept of Breathing")
            if makicamp2 == True:
                textbutton _("A Place Between the Trees {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makicamp2", locked=False)
            else:
                text _("A Place Between the Trees")
            if makilust5 == True:
                textbutton _("To Boldly Go... {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makilust5", locked=False)
            elif makilust5miss == True:
                text _("{color=EF1A1A}{s}Humble ABITCH{/s}{/color}")
            else:
                text _("{color=FF85FD}To Boldly Go...{/color}")
            if makispring1 == True:
                textbutton _("Sex Box Memories {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makispring1", locked=False)
            else:
                text _("Sex Box Memories")
            if makispring2 == True:
                textbutton _("Hello Alone {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("makispring2", locked=False)
            else:
                text _("Hello Alone")
            textbutton _("Back") action ShowMenu('gamemenumaki')

screen gamemenukirin():

    tag menu
    if kirinmenuoutfit is not None and renpy.loadable(kirinmenuoutfit) :
        add kirinmenuoutfit
    else :
        add "game_menukirin.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#9C8080}Height: 5'2/158cm{/color}") style "profile"
        text ("{color=#9C8080}Birthday: February 27th{/color}") style "profile"
        text ("\n{color=#9C8080}Affection: [kirin_love]{/color}") style "profile"
        text ("{color=#9C8080}Lust: [kirin_lust]{/color}") style "profile"
        text ("{color=#9C8080}Headpats: [kirinpats]{/color}") style "profile"
        if kirinmiss < 1:
            text ("{color=#9C8080}Events: [kirinpoint]/28{/color}") style "profile"
        else:
            text ("{color=#9C8080}Events: [kirinpoint]/28{/color} {color=#FF0000}([kirinmiss] Missed){/color}") style "profile"

    imagebutton:
        idle "kirinevrep1.png"
        hover "kirinevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('kirintracker')

    if bonus == True:
        if kirinbeachhj == True or ayanelust10 == True or kirindate10 == True:
            imagebutton:
                idle "subscribestar/images2/kirindryrep1.png"
                hover "subscribestar/images2/kirindryrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('kirinreplays')
        else:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')

        if kirinnudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('kirinphone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('kirinphone')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(kirin_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen kirintracker():

    tag menu

    use game_menu(_("Kirin Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=9C8080}Kirin Kanda ([kirin_love] Affection){/color}"
            if kirindate1 == True:
                textbutton _("Partners in Crime {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirindate1", locked=False)
            else:
                text _("Partners in Crime")
            if kirindate5 == True:
                if bonus == True:
                    textbutton _("Long and Hard {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kirindate5", locked=False)
                else:
                    textbutton _("Average in Every Way {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kirindate5", locked=False)
            elif bonus == True:
                text _("Long and Hard")
            else:
                text _("Average in Every Way")
            if kirindate10 == True:
                textbutton _("Politics! Pleasure! Ponies! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirindate10", locked=False)
            else:
                text _("Politics! Pleasure! Ponies!")
            text _("-----------------------------------------------------------")
            if kirinlust5 == True:
                textbutton _("Full Blossom {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinlust5", locked=False)
            else:
                text _("{color=FF85FD}Full Blossom{/color}")
            if kirininvite1 == True:
                textbutton _("Too Much, All at Once {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirininvite1", locked=False)
            else:
                text _("{color=778EFF}Too Much, All at Once{/color}")
            if kirininvite2 == True:
                textbutton _("No Extortion Necessary {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirininvite2", locked=False)
            else:
                text _("{color=778EFF}No Extortion Necessary{/color}")
            if kirinfirsthall == True:
                if bonus == True:
                    textbutton _("Morals vs. Orgasms {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kirinfirsthall", locked=False)
                else:
                    textbutton _("Kirin Hallway Event {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kirinfirsthall", locked=False)
            elif bonus == True:
                text _("Morals vs. Orgasms")
            else:
                text _("Kirin Hallway Event")
            if kirindorm10 == True:
                textbutton _("Love, Dorms, and Other Things {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirindorm10", locked=False)
            else:
                text _("Love, Dorms, and Other Things")
            if kirinsoccer15 == True:
                textbutton _("Flickering Spotlight {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinsoccer15", locked=False)
            else:
                text _("Flickering Spotlight")
            if kirinsoccer20 == True:
                textbutton _("Enigmatology {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinsoccer20", locked=False)
            else:
                text _("Enigmatology")
            if kirindorm15 == True:
                if bonus == True:
                    textbutton _("Bye Bye, Boner {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kirindorm15", locked=False)
                else:
                    textbutton _("Hello Hello, Huggy Boy {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kirindorm15", locked=False)
            elif bonus == True:
                text _("Bye Bye, Boner")
            else:
                text _("Hello Hello, Huggy Boy")
            if kirindorm20 == True:
                textbutton _("Terms & Conditions {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirindorm20", locked=False)
            else:
                text _("Terms & Conditions")
            if kirindate25 == True:
                textbutton _("All That is Contaminated {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirindate25", locked=False)
            else:
                text _("All That is Contaminated")
            if kirinlust20 == True:
                if bonus == True:
                    textbutton _("Taking the Reins {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kirinlust20", locked=False)
                else:
                    textbutton _("Taking the Reins {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kirinlust20intro", locked=False)
            elif kirinlust20skip == True:
                text _("{color=EF1A1A}{s}Falling Off the Tracks{/s}{/color}")
            else:
                text _("{color=FF85FD}Taking the Reins{/color}")
            if kirinspecial25 == True:
                textbutton _("Dyed Orange, Drenched in Sun {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinspecial25", locked=False)
            elif kirinspecial25skip == True:
                text _("{color=EF1A1A}{s}Drowned in Blue{/s}{/color}")
            else:
                text _("Dyed Orange, Drenched in Sun")
            if kirindorm25 == True:
                textbutton _("Temporary Bliss {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirindorm25", locked=False)
            else:
                text _("Temporary Bliss")
            if kirinsoccer25 == True:
                textbutton _("Four Hand Massage {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinsoccer25", locked=False)
            else:
                text _("Four Hand Massage")
            if kirinspecial30 == True:
                textbutton _("Made Out of Nothing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinspecial30", locked=False)
            elif kirinspecial30skip == True:
                text _("{color=EF1A1A}{s}At Least Someone Smiles{/s}{/color}")
            else:
                text _("Made Out of Nothing")
            if kirinlust202 == True:
                textbutton _("The Other Half {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinlust202", locked=False)
            elif kirinlust202skip == True:
                text _("{color=EF1A1A}{s}Eternally Empty{/s}{/color}")
            else:
                text _("{color=FF85FD}The Other Half{/color}")
            text _("-----------------------------------------------------------")
            if kirinlust30 == True:
                textbutton _("Falling Asleep Standing Up {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinlust30", locked=False)
            elif kirinlust30skip == True:
                text _("{color=EF1A1A}{s}Drugs Are Bad{/s}{/color}")
            else:
                text _("{color=FF85FD}Falling Asleep Standing Up{/color}")
            if kirinspecial40 == True:
                textbutton _("At the Edge of the Riverbank {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinspecial40", locked=False)
            else:
                text _("At the Edge of the Riverbank")
            if kirinspecial45p1 == True:
                textbutton _("Never Enough {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinspecial45p1", locked=False)
            else:
                text _("Never Enough")
            if kirinspecial45p2 == True:
                textbutton _("Salmon Onigiri {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinspecial45p2", locked=False)
            else:
                text _("Salmon Onigiri")
            text _("-----------------------------------------------------------")
            if sportswars9 == True:
                textbutton _("Rubber Traits {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars9", locked=False)
            else:
                text _("Rubber Traits")
            if sportswars18 == True:
                textbutton _("Girls Vs. Robots {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars18", locked=False)
            else:
                text _("Girls Vs. Robots")
            if kirinspring1 == True:
                textbutton _("Clockless Watch {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kirinspring1", locked=False)
            else:
                text _("Clockless Watch")
            if christmaskirin1 == True:
                textbutton _("Solar Eclipse {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmaskirin1", locked=False)
            else:
                text _("Solar Eclipse")
            if christmaskirin2 == True:
                textbutton _("Animal Control {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmaskirin2", locked=False)
            else:
                text _("Animal Control")
            textbutton _("Back") action ShowMenu('gamemenukirin')

screen gamemenukarin():

    tag menu
    if karinmenuoutfit is not None and renpy.loadable(karinmenuoutfit) :
        add karinmenuoutfit
    else :
        add "game_menukarin.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#AC9D77}Height: 5'9/176cm{/color}") style "profile"
        text ("{color=#AC9D77}Birthday: October 27th{/color}") style "profile"
        text ("\n{color=#AC9D77}Affection: [karin_love]{/color}") style "profile"
        text ("{color=#AC9D77}Lust: N/A{/color}") style "profile"
        text ("{color=#AC9D77}Headpats: 0{/color}") style "profile"
        if karinmiss < 1:
            text ("{color=#AC9D77}Events: [karinpoint]/15{/color}") style "profile"
        else:
            text ("{color=#AC9D77}Events: [karinpoint]/15{/color} {color=#FF0000}([karinmiss] Missed){/color}") style "profile"

    imagebutton:
        idle "karinevrep1.png"
        hover "karinevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('karintracker')

    imagebutton:
        idle "lock.png"
        hover "lock.png"
        xalign 0.925 yalign 0.935
        focus_mask True
        #action ShowMenu('amireplays')

    if karinnudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('karinphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('karinphone')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(karin_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen karintracker():

    tag menu

    use game_menu(_("Karin Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=AC9D77}Karin Kanda ([karin_love] Affection){/color}"
            if karindate1 == True:
                textbutton _("Further and Further {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karindate1", locked=False)
            else:
                text _("Further and Further")
            if karindate5 == True:
                if bonus == True:
                    textbutton _("Walking Penis Monster {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("karindate5", locked=False)
                else:
                    textbutton _("Walking Monster {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("karindate5", locked=False)
            elif bonus == True:
                text _("Walking Penis Monster")
            else:
                text _("Walking Monster")
            if karindate10 == True:
                textbutton _("If Only {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karindate10", locked=False)
            else:
                text _("If Only")
            text _("-----------------------------------------------------------")
            if karindate15 == True:
                textbutton _("Dying Alone With Ten Cats {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karindate15", locked=False)
            elif day264 == True and karinlied == False:
                text _("{color=EF1A1A}{s}The Price of Honesty{/s}{/color}")
            else:
                text _("Dying Alone With Ten Cats")
            if karinsoccer15 == True:
                textbutton _("Tendrils of Flame {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karinsoccer15", locked=False)
            else:
                text _("Tendrils of Flame")
            if karinsoccer20 == True:
                textbutton _("The Adventures of Karli & Steve {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karinsoccer20", locked=False)
            else:
                text _("The Adventures of Karli & Steve")
            if karindate20 == True:
                textbutton _("Sweet Tooth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karindate20", locked=False)
            else:
                text _("Sweet Tooth")
            text _("-----------------------------------------------------------")
            if karindate25 == True:
                textbutton _("Emerald Eyes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karindate25", locked=False)
            else:
                text _("Emerald Eyes")
            if karindate30 == True:
                textbutton _("Wrong Places/Wrong Times {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karindate30", locked=False)
            else:
                text _("Wrong Places/Wrong Times")
            text _("-----------------------------------------------------------")
            if karinspring1 == True:
                textbutton _("Touch of Grey {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karinspring1", locked=False)
            else:
                text _("Touch of Grey")
            if karinspring2 == True:
                textbutton _("Paranoid {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karinspring2", locked=False)
            else:
                text _("Paranoid")
            if karinspring3 == True:
                textbutton _("Better Boy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karinspring3", locked=False)
            else:
                text _("Better Boy")
            if karinspring4 == True:
                textbutton _("Back to the Basics {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karinspring4", locked=False)
            else:
                text _("Back to the Basics")
            if karinspring5 == True:
                textbutton _("A Trip to Uzbekistan {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karinspring5", locked=False)
            else:
                text _("A Trip to Uzbekistan")
            if karinspring6 == True:
                textbutton _("Top 10 Thoughts to Think {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("karinspring6", locked=False)
            else:
                text _("Top 10 Thoughts to Think")
            textbutton _("Back") action ShowMenu('gamemenukarin')

screen gamemenukaori():

    tag menu
    if kaorimenuoutfit is not None and renpy.loadable(kaorimenuoutfit) :
        add kaorimenuoutfit
    else :
        add "game_menukaori.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#4B4B4B}Height: 5'5/166cm{/color}") style "profile"
        text ("{color=#4B4B4B}Birthday: December 25th{/color}") style "profile"
        text ("\n{color=#4B4B4B}Affection: [kaori_love]{/color}") style "profile"
        text ("{color=#4B4B4B}Lust: [kaori_lust]{/color}") style "profile"
        text ("{color=#4B4B4B}Headpats: 0{/color}") style "profile"
        text ("{color=#4B4B4B}Events: [kaoripoint]/18{/color}") style "profile"

    imagebutton:
        idle "kaorievrep1.png"
        hover "kaorievrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('kaoritracker')

    if halloweenkaori2 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/kaoriroofrep1.png"
            hover "subscribestar/images2/kaoriroofrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('kaorireplays')

    if bonus == True:
        if kaorinudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('kaoriphone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('kaoriphone')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(kaori_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen kaoritracker():

    tag menu

    use game_menu(_("Kaori Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=4B4B4B}Kaori Kadowaki ([kaori_love] Affection){/color}"
            if kaoridate1 == True:
                textbutton _("How to Date a Human {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoridate1", locked=False)
            else:
                text _("How to Date a Human")
            if kaoridate5 == True:
                if bonus == True:
                    textbutton _("The Best Ways to Rub a Cock {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kaoridate5", locked=False)
                else:
                    textbutton _("Another Chicken Event {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("kaoridate5", locked=False)
            elif bonus == True:
                text _("The Best Ways to Rub a Cock")
            else:
                text _("Chicken Event")
            if kaoridate10 == True:
                textbutton _("Objects and Appendages {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoridate10", locked=False)
            else:
                text _("Objects and Appendages")
            text _("-----------------------------------------------------------")
            if kaoridate15 == True:
                textbutton _("To Die, To Sleep {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoridate15", locked=False)
            else:
                text _("To Die, To Sleep")
            if kaoridate15p2 == True:
                textbutton _("Sad Girl Special {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoridate15p2", locked=False)
            else:
                text _("Sad Girl Special")
            if kaoridate15p3 == True:
                textbutton _("Clouds {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoridate15p3", locked=False)
            else:
                text _("Clouds")
            if kaoridate20 == True:
                textbutton _("Såsom i en Spegel {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoridate20", locked=False)
            else:
                text _("Såsom i en Spegel")
            if kaoridate25 == True:
                textbutton _("Wither {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoridate25", locked=False)
            else:
                text _("Wither")
            text _("-----------------------------------------------------------")
            if kaorispecial35 == True:
                textbutton _("Where the Trees Live {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaorispecial35", locked=False)
            else:
                text _("Where the Trees Live")
            if kaorispecial40 == True:
                textbutton _("Human Females {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaorispecial40", locked=False)
            else:
                text _("Human Females")
            if kaoridate40 == True:
                textbutton _("Run, Rabbit, Run (Why the Fieldmice Hide) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoridate40", locked=False)
            else:
                text _("Run, Rabbit, Run (Why the Fieldmice Hide)")
            text _("-----------------------------------------------------------")
            if kaoricamp1 == True:
                textbutton _("Tree Village (The Color Machine) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoricamp1", locked=False)
            else:
                text _("Tree Village (The Color Machine)")
            if kaoricamp2 == True:
                textbutton _("Il Cervo {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaoricamp2", locked=False)
            else:
                text _("Il Cervo")
            if halloweenkaori1 == True:
                textbutton _("Friend {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenkaori1", locked=False)
            else:
                text _("Friend")
            if halloweenkaori2 == True:
                textbutton _("Kittens {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenkaori2", locked=False)
            else:
                text _("Kittens")
            if kaorispring1 == True:
                textbutton _("Seas of White (Why Not Here?) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaorispring1", locked=False)
            else:
                text _("Seas of White (Why Not Here?)")
            if kaorispring2 == True:
                textbutton _("Clearer Skies & Changing Eyes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaorispring2", locked=False)
            else:
                text _("Clearer Skies & Changing Eyes")
            if kaorispring3 == True:
                textbutton _("Breeding Material {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("kaorispring3", locked=False)
            else:
                text _("Breeding Material")
            textbutton _("Back") action ShowMenu('gamemenukaori')

screen gamemenuimani():

    tag menu
    if imanimenuoutfit is not None and renpy.loadable(imanimenuoutfit) :
        add imanimenuoutfit
    else :
        add "game_menuimani.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#80C9DC}Height: 5'8/174cm{/color}") style "profile"
        text ("{color=#80C9DC}Birthday: March 7th{/color}") style "profile"
        text ("\n{color=#80C9DC}Affection: [imani_love]{/color}") style "profile"
        text ("{color=#80C9DC}Lust: [imani_lust]{/color}") style "profile"
        text ("{color=#80C9DC}Headpats: 0{/color}") style "profile"
        text ("{color=#80C9DC}Events: [imanipoint]/11{/color}") style "profile"

    imagebutton:
        idle "imanievrep1.png"
        hover "imanievrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('imanitracker')

    if imanispring2 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/imanieatfourrep1.png"
            hover "subscribestar/images2/imanieatfourrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('imanireplays')

    if imaninudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('imaniphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('imaniphone')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(imani_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen imanitracker():

    tag menu

    use game_menu(_("Imani Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=#80C9DC}Imani Imai ([imani_love] Affection){/color}"
            if imanidate1 == True:
                textbutton _("Somewhere I Belong {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanidate1", locked=False)
            else:
                text _("Somewhere I Belong")
            if imanidate5 == True:
                textbutton _("A Hairline Fracture {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanidate5", locked=False)
            else:
                text _("A Hairline Fracture")
            if imanidate15p1 == True:
                textbutton _("Knotted Up {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanidate15p1", locked=False)
            else:
                text _("Knotted Up")
            if imanidate15p2 == True:
                textbutton _("Arm's Length {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanidate15p2", locked=False)
            else:
                text _("Arm's Length")
            if imanispecial15 == True:
                textbutton _("Debbie Downer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanispecial15", locked=False)
            else:
                text _("Debbie Downer")
            text _("-----------------------------------------------------------")
            if imanispring1 == True:
                textbutton _("Antoa Suo Nyamaa {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanispring1", locked=False)
            else:
                text _("Antoa Suo Nyamaa")
            if imanispring2 == True:
                textbutton _("I Will Carry You, My Light {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanispring2", locked=False)
            else:
                text _("I Will Carry You, My Light")
            if christmasimani1 == True:
                textbutton _("Yehoshua {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasimani1", locked=False)
            else:
                text _("Yehoshua")
            if christmasimani2 == True:
                textbutton _("The Truman Show {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasimani2", locked=False)
            else:
                text _("The Truman Show")
            if christmasimani3 == True:
                textbutton _("Now & Forever {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasimani3", locked=False)
            else:
                text _("Now & Forever")
            if imanilust5 == True:
                textbutton _("The Devil's Bed {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanilust5", locked=False)
            else:
                text _("{color=FF85FD}The Devil's Bed{/color}")
            textbutton _("Back") action ShowMenu('gamemenuimani')

screen rikatracker():

    tag menu

    use game_menu(_("Rika Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=#D18E77}Rika Rokuhara ([rika_love] Affection){/color}"
            if rikadate1 == True:
                textbutton _("Impregnation Spree {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rikadate1", locked=False)
            else:
                text _("Impregnation Spree")
            if rikaspecial2 == True:
                textbutton _("Back on Track {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rikaspecial2", locked=False)
            else:
                text _("Back on Track")
            if rikadive1 == True:
                textbutton _("James and the Giant Peach (Together-ish) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rikadive1", locked=False)
            else:
                text _("James and the Giant Peach (Together-ish)")
            text _("-----------------------------------------------------------")
            if sportswars1 == True:
                textbutton _("Ten Tips and Tricks to Make Even Straight Girls Want to Fuck You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars1", locked=False)
            else:
                text _("Ten Tips and Tricks to Make Even Straight Girls Want to Fuck You")
            if rikaspring1 == True:
                textbutton _("Rat College {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rikaspring1", locked=False)
            else:
                text _("Rat College")
            if rikaspring2 == True:
                textbutton _("Sixty-Minute Mark {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rikaspring2", locked=False)
            else:
                text _("Sixty-Minute Mark")
            if rikaspring3 == True:
                textbutton _("Sins of Thy Beloved {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rikaspring3", locked=False)
            else:
                text _("Sins of Thy Beloved")
            if rikaspring4 == True:
                textbutton _("Four Hours, Thirteen Minutes, Eleven Seconds {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rikaspring4", locked=False)
            else:
                text _("Four Hours, Thirteen Minutes, Eleven Seconds")
            textbutton _("Back") action ShowMenu('gamemenurika')

screen naotracker():

    tag menu

    use game_menu(_("Nao Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=#D18E77}Nao ([nao_love] Affection){/color}"
            if naospecial1 == True:
                textbutton _("Silver Tongue {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("naospecial1", locked=False)
            else:
                text _("Silver Tongue")
            if naospecial2 == True:
                textbutton _("Becoming a Kidnapper {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("naospecial2", locked=False)
            else:
                text _("Becoming a Kidnapper")
            if naospecial3 == True:
                textbutton _("Eternity Until {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("naospecial3", locked=False)
            else:
                text _("Eternity Until")
            text _("-----------------------------------------------------------")
            if naocamp1 == True:
                textbutton _("Flora {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("naocamp1", locked=False)
            else:
                text _("Flora")
            if naocamp2 == True:
                textbutton _("What's in the Pot? {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("naocamp2", locked=False)
            else:
                text _("What's in the Pot?")
            if halloweennao1 == True:
                textbutton _("Even Gods Get Lost {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweennao1", locked=False)
            else:
                text _("Even Gods Get Lost")
            if halloweennao2 == True:
                textbutton _("A House Near a Lake (The Same Place as Always) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweennao2", locked=False)
            else:
                text _("A House Near a Lake (The Same Place as Always)")
            if naospring1 == True:
                textbutton _("Wings of Anhedonia {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("naospring1", locked=False)
            else:
                text _("Wings of Anhedonia")
            if naospring2 == True:
                textbutton _("Miracle {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("naospring2", locked=False)
            else:
                text _("Miracle")
            if naospring3 == True:
                textbutton _("Nao More Than Ever {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("naospring3", locked=False)
            else:
                text _("Nao More Than Ever")
            textbutton _("Back") action ShowMenu('gamemenunao')

screen gamemenuchinami():

    tag menu
    if chinamimenuoutfit is not None and renpy.loadable(chinamimenuoutfit) :
        add chinamimenuoutfit
    else :
        add "game_menuchinami.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#FF9999}Height: 4'5/134cm{/color}") style "profile"
        text ("{color=#FF9999}Birthday: January 21st{/color}") style "profile"
        text ("\n{color=#FF9999}Affection: [chinami_love]{/color}") style "profile"
        text ("{color=#FF9999}Lust: N/A{/color}") style "profile"
        text ("{color=#FF9999}Headpats: 0{/color}") style "profile"
        if chinamimiss < 1:
            text ("{color=FF9999}Events: [chinamipoint]/13{/color}") style "profile"
        else:
            text ("{color=FF9999}Events: [chinamipoint]/13{/color} {color=#FF0000}([chinamimiss] Missed){/color}") style "profile"

    imagebutton:
        idle "chinamievrep1.png"
        hover "chinamievrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('chinamitracker')

    imagebutton:
        idle "lock.png"
        hover "lock.png"
        xalign 0.925 yalign 0.935
        focus_mask True
        #action ShowMenu('amireplays')

    if chinaminudecheck >= 1 and wizardmode == True:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('chinamiphone')
    elif wizardmode == True and chinaminudecheck == 0:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('chinamiphone')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(chinami_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen chinamitracker():

    tag menu

    use game_menu(_("Chinami Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=FF9999}Chinami Chosokabe ([chinami_love] Affection){/color}"
            if chinamidate1 == True:
                textbutton _("5,000 Year-Old Wizard {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamidate1", locked=False)
            else:
                text _("5,000 Year-Old Wizard")
            if chinamidate5 == True:
                textbutton _("Chinami-Corp {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamidate5", locked=False)
            else:
                text _("Chinami-Corp")
            text _("-----------------------------------------------------------")
            if chinamidate10 == True:
                textbutton _("Giant Pool of Jell-O {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamidate10", locked=False)
            else:
                text _("Giant Pool of Jell-O")
            if chinamidate15 == True:
                textbutton _("Pool Party (Love & Puppies) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamidate15", locked=False)
            else:
                text _("Pool Party (Love & Puppies)")
            if chinamidate20 == True:
                textbutton _("Happy Hour {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamidate20", locked=False)
            else:
                text _("Happy Hour")
            text _("-----------------------------------------------------------")
            if chinamidate25 == True:
                textbutton _("Death Trap {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamidate25", locked=False)
            else:
                text _("Death Trap")
            if chinamidate30 == True:
                textbutton _("Bad News Bears {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamidate30", locked=False)
            else:
                text _("Bad News Bears")
            text _("-----------------------------------------------------------")
            if chinamispring1 == True:
                textbutton _("Lucky (China Doll) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamispring1", locked=False)
            else:
                text _("Lucky (China Doll)")
            if chinamispring2 == True:
                textbutton _("Holden Caulfield {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamispring2", locked=False)
            else:
                text _("Holden Caulfield")
            if chinamispring3 == True:
                textbutton _("Backwards Boulevard {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamispring3", locked=False)
            else:
                text _("Backwards Boulevard")
            if chinamispring4 == True:
                textbutton _("Feed Me to the Farm {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamispring4", locked=False)
            elif chinamispring4miss == True:
                text _("{color=EF1A1A}{s}Mad Cow Disease{/s}{/color}")
            else:
                text _("Feed Me to the Farm")
            if chinamispring5 == True:
                textbutton _("Obnoxious Sexual Rampage {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamispring5", locked=False)
            elif chinamispring5miss == True:
                text _("{color=EF1A1A}{s}Even More Obnoxious Abstinence{/s}{/color}")
            else:
                text _("Obnoxious Sexual Rampage")
            if chinamispring6 == True:
                textbutton _("Five Hundred Pancakes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chinamispring6", locked=False)
            elif chinamispring6miss == True:
                text _("{color=EF1A1A}{s}Zero Pancakes{/s}{/color}")
            else:
                text _("Five Hundred Pancakes")
            textbutton _("Back") action ShowMenu('gamemenuchinami')

screen gamemenuwakana():

    tag menu
    if wakanamenuoutfit is not None and renpy.loadable(wakanamenuoutfit) :
        add wakanamenuoutfit
    else :
        add "game_menuwakanawinter.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#540087}Height: 5'6/169cm{/color}") style "profile"
        text ("{color=#540087}Birthday: October 10th{/color}") style "profile"
        text ("\n{color=#540087}Affection: [wakana_love]{/color}") style "profile"
        text ("{color=#540087}Lust: N/A{/color}") style "profile"
        text ("{color=#540087}Headpats: 0{/color}") style "profile"
        text ("{color=#540087}Events: [wakanapoint]/13{/color}") style "profile"

    imagebutton:
        idle "wakanaevrep1.png"
        hover "wakanaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('wakanatracker')

    if wakanaspecial15 == True:
        imagebutton:
            idle "subscribestar/images2/osakanabrrep1.png"
            hover "subscribestar/images2/osakanabrrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('wakanareplays')
    else:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(wakana_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen gamemenuosako():

    tag menu
    if osakomenuoutfit is not None and renpy.loadable(osakomenuoutfit) :
        add osakomenuoutfit
    else :
        add "game_menuosako.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#9A6BA1}Height: 5'8/173cm{/color}") style "profile"
        text ("{color=#9A6BA1}Birthday: November 27th{/color}") style "profile"
        text ("\n{color=#9A6BA1}Affection: [osako_love]{/color}") style "profile"
        text ("{color=#9A6BA1}Lust: N/A{/color}") style "profile"
        text ("{color=#9A6BA1}Headpats: 0{/color}") style "profile"
        text ("{color=#9A6BA1}Events: [osakopoint]/10{/color}") style "profile"

    imagebutton:
        idle "osakoevrep1.png"
        hover "osakoevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('osakotracker')

    if wakanaspecial15 == True:
        imagebutton:
            idle "subscribestar/images2/osakanabrrep1.png"
            hover "subscribestar/images2/osakanabrrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('osakoreplays')
    else:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(osako_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen gamemenutsubasa():

    tag menu
    if tsubasamenuoutfit is not None and renpy.loadable(tsubasamenuoutfit) :
        add tsubasamenuoutfit
    else :
        add "game_menutsubasa.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#eae6aa}Height: 5'8/174cm{/color}") style "profile"
        text ("{color=#eae6aa}Birthday: January 12th{/color}") style "profile"
        text ("\n{color=#eae6aa}Affection: [tsubasa_love]{/color}") style "profile"
        text ("{color=#eae6aa}Lust: N/A{/color}") style "profile"
        text ("{color=#eae6aa}Headpats: 0{/color}") style "profile"
        if tsubasamiss < 1:
            text ("{color=#eae6aa}Events: [tsubasapoint]/12{/color}") style "profile"
        else:
            text ("{color=#eae6aa}Events: [tsubasapoint]/12{/color} {color=#FF0000}([tsubasamiss] Missed){/color}") style "profile"

    imagebutton:
        idle "tsubasaevrep1.png"
        hover "tsubasaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('tsubasatracker')

    if saraspring2 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    elif christmastsubasa1 == True:
        imagebutton:
            idle "subscribestar/images2/tsubasaxmasrep1.png"
            hover "subscribestar/images2/tsubasaxmasrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('tsubasareplays')
    elif christmastsubasa1 == False and saraspring2 == True:
        imagebutton:
            idle "subscribestar/images2/saracounterrep1.png"
            hover "subscribestar/images2/saracounterrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('tsubasareplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(tsubasa_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen gamemenurika():

    tag menu
    if rikamenuoutfit is not None and renpy.loadable(rikamenuoutfit) :
        add rikamenuoutfit
    else :
        add "game_menurika.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#D18E77}Height: 5'7/171cm{/color}") style "profile"
        text ("{color=#D18E77}Birthday: September 23rd{/color}") style "profile"
        text ("\n{color=#D18E77}Affection: [rika_love]{/color}") style "profile"
        text ("{color=#D18E77}Lust: N/A{/color}") style "profile"
        text ("{color=#D18E77}Headpats: 0{/color}") style "profile"
        text ("{color=#D18E77}Events: [rikapoint]/8{/color}") style "profile"

    imagebutton:
        idle "rikaevrep1.png"
        hover "rikaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('rikatracker')

    imagebutton:
        idle "lock.png"
        hover "lock.png"
        xalign 0.925 yalign 0.935
        focus_mask True
        #action ShowMenu('amireplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(rika_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen gamemenunao():

    tag menu
    if naomenuoutfit is not None and renpy.loadable(naomenuoutfit) :
        add naomenuoutfit
    else :
        add "game_menunaohoodie.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#602F2B}Height: 4'4/132cm{/color}") style "profile"
        text ("{color=#602F2B}Birthday: ???{/color}") style "profile"
        text ("\n{color=#602F2B}Affection: [nao_love]{/color}") style "profile"
        text ("{color=#602F2B}Lust: N/A{/color}") style "profile"
        text ("{color=#602F2B}Headpats: 0{/color}") style "profile"
        text ("{color=#602F2B}Events: [naopoint]/10{/color}") style "profile"

    imagebutton:
        idle "naoevrep1.png"
        hover "naoevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('naotracker')

    imagebutton:
        idle "lock.png"
        hover "lock.png"
        xalign 0.925 yalign 0.935
        focus_mask True
        #action ShowMenu('amireplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(nao_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen gamemenutsukasa():

    tag menu
    if tsukasamenuoutfit is not None and renpy.loadable(tsukasamenuoutfit) :
        add tsukasamenuoutfit
    else :
        add "game_menutsukasa.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#f0ca8c}Height: 4'5/136cm{/color}") style "profile"
        text ("{color=#f0ca8c}Birthday: January 10th{/color}") style "profile"
        text ("\n{color=#f0ca8c}Affection: [tsukasa_love]{/color}") style "profile"
        text ("{color=#f0ca8c}Lust: N/A{/color}") style "profile"
        text ("{color=#f0ca8c}Headpats: 0{/color}") style "profile"
        if tsukasamiss < 1:
            text ("{color=f0ca8c}Events: [tsukasapoint]/9{/color}") style "profile"
        else:
            text ("{color=f0ca8c}Events: [tsukasapoint]/9{/color} {color=#FF0000}([tsukasamiss] Missed){/color}") style "profile"

    imagebutton:
        idle "tsukasaevrep1.png"
        hover "tsukasaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('tsukasatracker')

    imagebutton:
        idle "lock.png"
        hover "lock.png"
        xalign 0.925 yalign 0.935
        focus_mask True
        #action ShowMenu('amireplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(tsukasa_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen maintrackerch2():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Main Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "Chapter 2"
            if christmas1 == True:
                textbutton _("Snow-Covered Footprints {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmas1", locked=False)
            else:
                text _("Snow-Covered Footprints")
            if christmas2 == True:
                textbutton _("Patent-Pending {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmas2", locked=False)
            else:
                text _("Patent-Pending")
            if christmas3 == True:
                textbutton _("Fuck Christmas {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmas3", locked=False)
            else:
                text _("Fuck Christmas")
            if christmas4 == True:
                textbutton _("Disappointing Everyone {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmas4", locked=False)
            else:
                text _("Disappointing Everyone")
            if christmas5 == True:
                textbutton _("Bottled Dreams {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmas5", locked=False)
            else:
                text _("Bottled Dreams")
            if christmas6 == True:
                textbutton _("Christmas Miracle {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmas6", locked=False)
            else:
                text _("Christmas Miracle")
            if christmas7 == True:
                textbutton _("Fireworks, Chicken, and the Innate Fear of Death {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmas7", locked=False)
            else:
                text _("Fireworks, Chicken, and the Innate Fear of Death")
            if day237 == True:
                textbutton _("Suicide Pact {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day237", locked=False)
            else:
                text _("Suicide Pact")
            if day239 == True:
                textbutton _("A Door that People Move Through {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day239", locked=False)
            else:
                text _("A Door that People Move Through")
            if day240 == True:
                textbutton _("Uta's Last Stand {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day240", locked=False)
            else:
                text _("Uta's Last Stand")
            if day244 == True:
                textbutton _("Opposites Attract {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day244", locked=False)
            else:
                text _("Opposites Attract")
            if day246 == True:
                textbutton _("All Kinds of People, All Kinds of Things {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day246", locked=False)
            else:
                text _("All Kinds of People, All Kinds of Things")
            if day247 == True:
                textbutton _("Caterpillar {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day247", locked=False)
            else:
                text _("Caterpillar")
            if day261 == True:
                textbutton _("Let Me Die in Spring {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day261", locked=False)
            else:
                text _("Let Me Die in Spring")
            if day263 == True:
                textbutton _("There's Always a Chance {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day263", locked=False)
            else:
                text _("There's Always a Chance")
            if day264 == True:
                textbutton _("Forty Degrees Below Zero {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day264", locked=False)
            else:
                text _("Forty Degrees Below Zero")
            if day269 == True:
                textbutton _("What Could Have Been {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day269", locked=False)
            else:
                text _("What Could Have Been")
            if day270 == True:
                textbutton _("What Is {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day270", locked=False)
            else:
                text _("What Is")
            if day271 == True:
                textbutton _("What Was {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day271", locked=False)
            else:
                text _("What Was")
            if day280 == True:
                textbutton _("Annabel Lee {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day280", locked=False)
            else:
                text _("Annabel Lee")
            if day281 == True:
                textbutton _("Yuritopia {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day281", locked=False)
            else:
                text _("Yuritopia")
            if day282 == True:
                textbutton _("Birdcage {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day282", locked=False)
            else:
                text _("Birdcage")
            if day283 == True:
                textbutton _("Survive! Grow! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day283", locked=False)
            else:
                text _("Survive! Grow!")
            if day287 == True:
                textbutton _("Another Long Year {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day287", locked=False)
            else:
                text _("Another Long Year")
            if day288 == True:
                textbutton _("Adult Supervision {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day288", locked=False)
            else:
                text _("Adult Supervision")
            if day295 == True:
                textbutton _("The WAP Man {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day295", locked=False)
            else:
                text _("The WAP Man")
            if day295parttwo == True:
                textbutton _("The Color of a Heart {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day295parttwo", locked=False)
            else:
                text _("The Color of a Heart")
            if day297 == True:
                textbutton _("Call Me By Your Name {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day297", locked=False)
            else:
                text _("Call Me By Your Name")
            if day302 == True:
                textbutton _("Lives and Minds of Laymen {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day302", locked=False)
            else:
                text _("Lives and Minds of Laymen")
            if day303 == True:
                textbutton _("Sounds of Cicadas {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day303", locked=False)
            else:
                text _("Sound of Cicadas")
            if day304 == True:
                textbutton _("Horses or the Whispers of the Dead {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day304", locked=False)
            else:
                text _("Horses or the Whispers of the Dead")
            if day318 == True:
                textbutton _("Operation: Firestarter {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day318", locked=False)
            else:
                text _("Operation: Firestarter")
            if dormwar1 == True:
                textbutton _("Super Mega Ultimate Dorm War! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar1", locked=False)
            else:
                text _("Super Mega Ultimate Dorm War!")
            if dormwar2 == True:
                textbutton _("Pre-Game Show! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar2", locked=False)
            else:
                text _("Pre-Game Show!")
            if dormwar3 == True:
                textbutton _("Imouto Mode! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar3", locked=False)
            else:
                text _("Imouto Mode!")
            if dormwar4 == True:
                textbutton _("Alive & Active! All Out Athletics! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar4", locked=False)
            else:
                text _("Alive & Active! All Out Athletics!")
            if dormwar5 == True:
                textbutton _("Friend Zone Fight! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar5", locked=False)
            else:
                text _("Friend Zone Fight!")
            if dormwar6 == True:
                textbutton _("Sphenopalatine Ganglioneuralgia {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar6", locked=False)
            else:
                text _("Sphenopalatine Ganglioneuralgia")
            if dormwar7 == True:
                textbutton _("Ruthless Rhyme Rhomp! Rap Rampage! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar7", locked=False)
            else:
                text _("Ruthless Rhyme Rhomp! Rap Rampage!")
            if dormwar8 == True:
                textbutton _("Chaperone {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar8", locked=False)
            else:
                text _("Chaperone")
            if dormwar9 == True:
                textbutton _("Why Now? {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar9", locked=False)
            else:
                text _("Why Now?")
            if dormwar10 == True:
                textbutton _("In Some Cases, Love {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar10", locked=False)
            else:
                text _("In Some Cases, Love")
            if dormwar11 == True:
                textbutton _("The Legacy of Thaum Pt. Z: Alentha Amastacia {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar11", locked=False)
            else:
                text _("The Legacy of Thaum Pt. Z: Alentha Amastacia")
            if dormwar12 == True:
                textbutton _("Us {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar12", locked=False)
            else:
                text _("Us")
            if dormwar13 == True:
                textbutton _("First Last Date {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar13", locked=False)
            else:
                text _("First Last Date")
            if dormwar14 == True:
                textbutton _("The Scary Room {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar14", locked=False)
            else:
                text _("The Scary Room")
            if dormwar15 == True:
                textbutton _("Fallen Angels {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar15", locked=False)
            else:
                text _("Fallen Angels")
            if dormwar16 == True:
                textbutton _("Post-Game Celebration! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar16", locked=False)
            else:
                text _("Post-Game Celebration!")
            if dormwar17 == True:
                textbutton _("War's End {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwar17", locked=False)
            else:
                text _("War's End")
            if day333 == True:
                textbutton _("Record Breaker {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day333", locked=False)
            else:
                text _("Record Breaker")
            if day333part2 == True:
                textbutton _("Lesbian Stuff {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day333part2", locked=False)
            else:
                text _("Lesbian Stuff")
            if day340 == True:
                textbutton _("Mana Transfer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day340", locked=False)
            else:
                text _("Mana Transfer")
            if day344 == True:
                textbutton _("The Price of Experience {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day344", locked=False)
            else:
                text _("The Price of Experience")
            if thirdreset1 == True:
                textbutton _("Word of the Day {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("thirdreset1", locked=False)
            else:
                text _("Word of the Day")
            if thirdreset2 == True:
                textbutton _("Backwards Dancing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("thirdreset2", locked=False)
            else:
                text _("Backwards Dancing")
            if thirdreset3 == True:
                textbutton _("Sayonara {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("thirdreset3", locked=False)
            else:
                text _("Sayonara")
            if day351 == True:
                textbutton _("Food Groups {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day351", locked=False)
            else:
                text _("Food Groups")
            if day355 == True:
                textbutton _("Permission Slip {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day355", locked=False)
            else:
                text _("Permission Slip")
            if secondbeach1 == True:
                textbutton _("Good Morning {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach1", locked=False)
            else:
                text _("Good Morning")
            if secondbeach2 == True:
                textbutton _("Egg Tossing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach2", locked=False)
            else:
                text _("Egg Tossing")
            if secondbeach3 == True:
                if bonus == True:
                    textbutton _("De-Briefing the Teacher {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("secondbeach3", locked=False)
                else:
                    textbutton _("Third Event of the Second Beach Update {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("secondbeach3", locked=False)
            elif bonus == True:
                text _("De-Briefing the Teacher")
            else:
                text _("Third Event of the Second Beach Update")
            if secondbeach4 == True:
                textbutton _("TPK (Banana Boat) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach4", locked=False)
            else:
                text _("TPK (Banana Boat)")
            if secondbeach5 == True:
                textbutton _("The Next Best Thing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach5", locked=False)
            else:
                text _("The Next Best Thing")
            if secondbeach6 == True:
                textbutton _("The Yellow Wallpaper {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach6", locked=False)
            else:
                text _("The Yellow Wallpaper")
            if secondbeach7 == True:
                textbutton _("Everything Ephemeral (Face Forward) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach7", locked=False)
            else:
                text _("Everything Ephemeral (Face Forward)")
            if secondbeach8 == True:
                textbutton _("The Legacy of Thaum Pt. III: Changeling {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach8", locked=False)
            else:
                text _("The Legacy of Thaum Pt. III: Changeling")
            if secondbeach9 == True:
                textbutton _("Alderaan {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach9", locked=False)
            else:
                text _("Alderaan")
            if secondbeach10 == True:
                textbutton _("Torrential Downpour. Child of Man. {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach10", locked=False)
            else:
                text _("Torrential Downpour. Child of Man.")
            if secondbeach11 == True:
                textbutton _("Getting Comfortable {b}✓{/b}"):
                    text_style "mybutton"
                    if dormwarfloor1win == True:
                        action Replay("secondbeach11floor1", locked=False)
                    if dormwarfloor2win == True:
                        action Replay("secondbeach11floor2", locked=False)
            else:
                text _("Getting Comfortable")
            if secondbeach12 == True:
                textbutton _("Left Out in Light {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach12", locked=False)
            else:
                text _("Left Out in Light")
            if secondbeach13 == True:
                textbutton _("We Were Angels {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach13", locked=False)
            else:
                text _("We Were Angels")
            if secondbeach14 == True:
                textbutton _("Lavender's Blue {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach14", locked=False)
            else:
                text _("Lavender's Blue")
            if secondbeach15 == True:
                textbutton _("Pluto Was Never Really a Planet {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach15", locked=False)
            else:
                text _("Pluto Was Never Really a Planet")
            if secondbeach16 == True:
                textbutton _("Try. Try. Try. {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach16", locked=False)
            else:
                text _("Try. Try. Try.")
            if secondbeach17 == True:
                textbutton _("Goodnight {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach17", locked=False)
            else:
                text _("Goodnight")
            if secondbeach18 == True:
                textbutton _("All is Bright. All is Beautiful. {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("secondbeach18", locked=False)
            else:
                text _("All is Bright. All is Beautiful.")
            if halloweentwo1 == True:
                textbutton _("Girls in Spandex {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo1", locked=False)
            else:
                text _("Girls in Spandex")
            if halloweentwo2 == True:
                textbutton _("Butterfly Facts {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo2", locked=False)
            else:
                text _("Butterfly Facts")
            if halloweentwo3 == True:
                textbutton _("Immernachtreich {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo3", locked=False)
            else:
                text _("Immernachtreich")
            if halloweentwo4 == True:
                textbutton _("Take Me Anywhere {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo4", locked=False)
            else:
                text _("Take Me Anywhere")
            if halloweentwo5 == True:
                textbutton _("Anglerfish {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo5", locked=False)
            else:
                text _("Anglerfish")
            if halloweentwo6 == True:
                textbutton _("Porcelain Labyrinth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo6", locked=False)
            else:
                text _("Porcelain Labyrinth")
            if halloweentwo7 == True:
                textbutton _("The First Signs of Fraying Threads {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo7", locked=False)
            else:
                text _("The First Signs of Fraying Threads")
            if halloweentwo8 == True:
                textbutton _("Official Unofficial Double Date {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo8", locked=False)
            else:
                text _("Official Unofficial Double Date")
            if halloweentwo9 == True:
                textbutton _("In Circles {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo9", locked=False)
            else:
                text _("In Circles")
            if halloweentwo10 == True:
                textbutton _("Escape Rope {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo10", locked=False)
            else:
                text _("Escape Rope")
            if halloweentwo11 == True:
                textbutton _("Lavender's Green {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo11", locked=False)
            else:
                text _("Lavender's Green")
            if halloweentwo12 == True:
                textbutton _("Gallows Edge {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo12", locked=False)
            else:
                text _("Gallows Edge")
            if halloweentwo13 == True:
                textbutton _("Metal in Microwaves {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweentwo13", locked=False)
            else:
                text _("Metal in Microwaves")
            if christmastwo1 == True:
                textbutton _("Three Amigos {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo1", locked=False)
            else:
                text _("Three Amigos")
            if christmastwo2 == True:
                textbutton _("The Reliable and Totally Legitimate Princess Imani {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo2", locked=False)
            else:
                text _("The Reliable and Totally Legitimate Princess Imani")
            if christmastwo3 == True:
                textbutton _("Room to Grow {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo3", locked=False)
            else:
                text _("Room to Grow")
            if christmastwo4 == True:
                textbutton _("Dodging Snowflakes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo4", locked=False)
            else:
                text _("Dodging Snowflakes")
            if christmastwo5 == True:
                textbutton _("Everything Evil {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo5", locked=False)
            else:
                text _("Everything Evil")
            if christmastwo6 == True:
                textbutton _("Tokimeki Labyrinth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo6", locked=False)
            else:
                text _("Tokimeki Labyrinth")
            if christmastwo7 == True:
                textbutton _("Love Set to Max (Class Warfare) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo7", locked=False)
            else:
                text _("Love Set to Max (Class Warfare)")
            if christmastwo8 == True:
                textbutton _("Dohoonkabhankoloos {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo8", locked=False)
            else:
                text _("Dohoonkabhankoloos")
            if christmastwo9 == True:
                textbutton _("Fear of Missing Out {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo9", locked=False)
            else:
                text _("Fear of Missing Out")
            if christmastwo10 == True:
                textbutton _("Walking on Eggshells {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo10", locked=False)
            else:
                text _("Walking on Eggshells")
            if christmastwo11 == True:
                textbutton _("New Age Entrepreneurs {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo11", locked=False)
            else:
                text _("New Age Entrepreneurs")
            if christmastwo12 == True:
                textbutton _("The Smile, The Face {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo12", locked=False)
            else:
                text _("The Smile, The Face")
            if christmastwo13 == True:
                textbutton _("Shadowmeld {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo13", locked=False)
            else:
                text _("Shadowmeld")
            if christmastwo14 == True:
                textbutton _("Chashu (A Cracked Bowl) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo14", locked=False)
            else:
                text _("Chashu (A Cracked Bowl)")
            if christmastwo15 == True:
                textbutton _("A Way's Away {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo15", locked=False)
            else:
                text _("A Way's Away")
            if christmastwo16 == True:
                textbutton _("No Escape {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo16", locked=False)
            else:
                text _("No Escape")
            if christmastwo17 == True:
                textbutton _("Spotless Mind {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo17", locked=False)
            else:
                text _("Spotless Mind")
            if christmastwo18 == True:
                textbutton _("Me Without You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo18", locked=False)
            else:
                text _("Me Without You")
            if christmastwo19 == True:
                textbutton _("The Color White {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo19", locked=False)
            else:
                text _("The Color White")
            if christmastwo20 == True:
                textbutton _("Glued to the Sky {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastwo20", locked=False)
            else:
                text _("Glued to the Sky")
            if returntosummer1 == True:
                textbutton _("The Light of Last Summer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("returntosummer1", locked=False)
            else:
                text _("The Light of Last Summer")
            if returntosummer2 == True:
                textbutton _("A Life of Prizes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("returntosummer2", locked=False)
            else:
                text _("A Life of Prizes")
            if returntosummer3 == True:
                textbutton _("Utinam Ne Illum Numquam Conspexissem {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("returntosummer3", locked=False)
            else:
                text _("Utinam Ne Illum Numquam Conspexissem")
            textbutton _("Back") action ShowMenu('eventtracker11')

screen maintrackerch3():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Main Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "Chapter 3"
            if chapthree1 == True:
                textbutton _("The Virgin of the Apocalypse {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chapthree1", locked=False)
            else:
                text _("The Virgin of the Apocalypse")
            if chapthree2 == True:
                textbutton _("Memories {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chapthree2", locked=False)
            else:
                text _("Memories")
            if chapthree3 == True:
                textbutton _("Empty Eyes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chapthree3", locked=False)
            else:
                text _("Empty Eyes")
            if chapthree4 == True:
                textbutton _("The Great Migration {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chapthree4", locked=False)
            else:
                text _("The Great Migration")
            if chapthree5 == True:
                textbutton _("Creatures of Habit {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chapthree5", locked=False)
            else:
                text _("Creatures of Habit")
            if chapthree6 == True:
                textbutton _("Everything Everywhere All At Once {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chapthree6", locked=False)
            else:
                text _("Everything Everywhere All At Once")
            if chapthree7 == True:
                textbutton _("Normal-ish {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chapthree7", locked=False)
            else:
                text _("Normal-ish")
            if chapthree8 == True:
                textbutton _("Life is Changing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("chapthree8", locked=False)
            else:
                text _("Life is Changing")
            if yumichikaspecial1 == True:
                textbutton _("Dead in the Water {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumichikaspecial1", locked=False)
            else:
                text _("Dead in the Water")
            if yumiyukispecial1 == True:
                textbutton _("The Road to Recovery {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yumiyukispecial1", locked=False)
            else:
                text _("The Road to Recovery")
            if imanispecial1 == True:
                textbutton _("No Strings Attached {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("imanispecial1", locked=False)
            else:
                text _("No Strings Attached")
            if rikaspecial1 == True:
                textbutton _("Metronome In Love {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("rikaspecial1", locked=False)
            else:
                text _("Metronome In Love")
            if day543 == True:
                textbutton _("Grief Seed {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("day543", locked=False)
            else:
                text _("Grief Seed")
            if dormwartwo1 == True:
                textbutton _("A Walk Through Hell {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo1", locked=False)
            else:
                text _("A Walk Through Hell")
            if dormwartwo2 == True:
                textbutton _("Dorm War II: Pre-Game Show {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo2", locked=False)
            else:
                text _("Dorm War II: Pre-Game Show")
            if dormwartwo3 == True:
                textbutton _("A Frame on a Shelf in a House {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo3", locked=False)
            else:
                text _("A Frame on a Shelf in a House")
            if dormwartwo4 == True:
                textbutton _("Gamer Girl Grindfest {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo4", locked=False)
            else:
                text _("Gamer Girl Grindfest")
            if dormwartwo5 == True:
                textbutton _("Hiding in Plain Sight {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo5", locked=False)
            else:
                text _("Hiding in Plain Sight")
            if dormwartwo6 == True:
                textbutton _("She Is {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo6", locked=False)
            else:
                text _("She Is")
            if dormwartwo7 == True:
                textbutton _("Burden to Bear {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo7", locked=False)
            else:
                text _("Burden to Bear")
            if dormwartwo8 == True:
                textbutton _("Everyone {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo8", locked=False)
            else:
                text _("Everyone")
            if dormwartwo9 == True:
                textbutton _("Midnight Mom Mosh {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo9", locked=False)
            else:
                text _("Midnight Mom Mosh")
            if dormwartwo10 == True:
                textbutton _("The Way it Scatters {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo10", locked=False)
            else:
                text _("The Way it Scatters")
            if dormwartwo11 == True:
                textbutton _("Misfit Maid Madness {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo11", locked=False)
            else:
                text _("Misfit Maid Madness")
            if dormwartwo12 == True:
                textbutton _("Somewhere Far From Here {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo12", locked=False)
            else:
                text _("Somewhere Far From Here")
            if dormwartwo13 == True:
                textbutton _("Swimming With Sharks {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo13", locked=False)
            else:
                text _("Swimming With Sharks")
            if dormwartwo14 == True:
                textbutton _("Remove Curse {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo14", locked=False)
            else:
                text _("Remove Curse")
            if dormwartwo15 == True:
                textbutton _("The Cracking of the Egg (Nothing is Beautiful) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo15", locked=False)
            else:
                text _("The Cracking of the Egg (Nothing is Beautiful)")
            if dormwartwo16 == True:
                textbutton _("World of Lines {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo16", locked=False)
            else:
                text _("World of Lines")
            if dormwartwo17 == True:
                textbutton _("Popping Off {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo17", locked=False)
            else:
                text _("Popping Off")
            if dormwartwo18 == True:
                textbutton _("Tip Your Bartender {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo18", locked=False)
            else:
                text _("Tip Your Bartender")
            if dormwartwo19 == True:
                textbutton _("Redeemer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwartwo19", locked=False)
            else:
                text _("Redeemer")
            if beachmas1 == True:
                textbutton _("Walk Into the Water {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas1", locked=False)
            else:
                text _("Walk Into the Water")
            if beachmas2 == True:
                textbutton _("Imaginary Veins {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas2", locked=False)
            else:
                text _("Imaginary Veins")
            if beachmas3 == True:
                textbutton _("Friends (The Maya Route) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas3", locked=False)
            else:
                text _("Friends (The Maya Route)")
            if beachmas4 == True:
                textbutton _("Chandler's Law {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas4", locked=False)
            else:
                text _("Chandler's Law")
            if beachmas5 == True:
                textbutton _("The Chains That Bind {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas5", locked=False)
            else:
                text _("The Chains That Bind")
            if beachmas6 == True:
                textbutton _("No Cumming on Christmas {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas6", locked=False)
            else:
                text _("No Cumming on Christmas")
            if beachmas7 == True:
                textbutton _("Fetch Quest {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas7", locked=False)
            else:
                text _("Fetch Quest")
            if beachmas8 == True:
                textbutton _("A Thousand Truths {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas8", locked=False)
            else:
                text _("A Thousand Truths")
            if beachmas9 == True:
                textbutton _("The Bending of Italics {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas9", locked=False)
            else:
                text _("The Bending of Italics")
            if beachmas10 == True:
                textbutton _("Treasured {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas10", locked=False)
            else:
                text _("Treasured")
            if beachmas11 == True:
                textbutton _("いないいない。。。ばあ！ {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas11", locked=False)
            else:
                text _("いないいない。。。ばあ！")
            if beachmas12 == True:
                textbutton _("Robin Hood {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas12", locked=False)
            else:
                text _("Robin Hood")
            if beachmas13 == True:
                textbutton _("The Legacy of Thaum Pt. IV {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas13", locked=False)
            else:
                text _("The Legacy of Thaum Pt. IV")
            if beachmas14 == True:
                textbutton _("On The Fence {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas14", locked=False)
            else:
                text _("On The Fence")
            if beachmas15 == True:
                textbutton _("To the Future With a Smile {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas15", locked=False)
            else:
                text _("To the Future With a Smile")
            if beachmas16 == True:
                textbutton _("Neverender {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas16", locked=False)
            else:
                text _("Neverender")
            if beachmas17 == True:
                textbutton _("Moon-Touched {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas17", locked=False)
            else:
                text _("Moon-Touched")
            if beachmas18 == True:
                textbutton _("Smells of Summer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas18", locked=False)
            else:
                text _("Smells of Summer")
            if beachmas19 == True:
                textbutton _("I Will Deliver You to the Fireflies {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas19", locked=False)
            else:
                text _("I Will Deliver You to the Fireflies")
            if beachmas20 == True:
                textbutton _("Shelter {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachmas20", locked=False)
            else:
                text _("Shelter")
            if slumberreset1 == True:
                textbutton _("To Catch Me If I Fall {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("slumberreset1", locked=False)
            else:
                text _("To Catch Me If I Fall")
            if slumberreset2 == True:
                textbutton _("Approximation {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("slumberreset2", locked=False)
            else:
                text _("Approximation")
            if slumberreset3 == True:
                textbutton _("December 28, 2020 (Clay & Clockwork) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("slumberreset3", locked=False)
            else:
                text _("December 28, 2020 (Clay & Clockwork)")
            if slumberreset4 == True:
                textbutton _("Untitled {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("slumberreset4", locked=False)
            else:
                text _("Untitled")
            if slumberreset5 == True:
                textbutton _("A Thousand Years {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("slumberreset5", locked=False)
            else:
                text _("A Thousand Years")
            if postnodokachain1 == True:
                textbutton _("White-Fronted Parrot {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("postnodokachain1", locked=False)
            else:
                text _("White-Fronted Parrot")
            if treasureisland == True:
                textbutton _("First Contact {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("treasureisland", locked=False)
            else:
                text _("First Contact")
            if amispecial50mainp1 == True:
                textbutton _("All For You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amispecial50mainp1", locked=False)
            else:
                text _("All For You")
            if amispecial50mainp2 == True:
                textbutton _("From the Desk of the Ninth God {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("amispecial50mainp2", locked=False)
            else:
                text _("From the Desk of the Ninth God")
            if predormwars3 == True:
                textbutton _("May the Winter Come {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("predormwars3", locked=False)
            else:
                text _("May the Winter Come")
            if beachwars1 == True:
                textbutton _("Boner on the Bus {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars1", locked=False)
            else:
                text _("Boner on the Bus")
            if beachwars2 == True:
                textbutton _("When You Snap {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars2", locked=False)
            else:
                text _("When You Snap")
            if beachwars3 == True:
                textbutton _("Until My Back is Broken {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars3", locked=False)
            else:
                text _("Until My Back is Broken")
            if beachwars4 == True:
                textbutton _("The Rest of Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars4", locked=False)
            else:
                text _("The Rest of Me")
            if beachwars5 == True:
                textbutton _("Hyzenthlay {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars5", locked=False)
            else:
                text _("Hyzenthlay")
            if beachwars6 == True:
                textbutton _("More Human Than Human {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars6", locked=False)
            else:
                text _("More Human Than Human")
            if beachwars7 == True:
                textbutton _("Eyes Closed, Chin Up {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars7", locked=False)
            else:
                text _("Eyes Closed, Chin Up")
            if beachwars8 == True:
                textbutton _("Sexy Swimsuit Showdown {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars8", locked=False)
            else:
                text _("Sexy Swimsuit Showdown")
            if beachwars9 == True:
                textbutton _("Fairytale (The End Until Tomorrow) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars9", locked=False)
            else:
                text _("Fairytale (The End Until Tomorrow)")
            if beachwars10 == True:
                textbutton _("Monsters {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars10", locked=False)
            else:
                text _("Monsters")
            if beachwars11 == True:
                textbutton _("Pairs in Different Places {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars11", locked=False)
            else:
                text _("Pairs in Different Places")
            if beachwars12 == True:
                textbutton _("Forbidden Artistry {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars12", locked=False)
            else:
                text _("Forbidden Artistry")
            if beachwars13 == True:
                textbutton _("Too Many Cooks {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars13", locked=False)
            else:
                text _("Too Many Cooks")
            if beachwars14 == True:
                textbutton _("Judgement Day {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars14", locked=False)
            else:
                text _("Judgement Day")
            if beachwars15 == True:
                textbutton _("Mother May I {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars15", locked=False)
            else:
                text _("Mother May I")
            if beachwars16 == True:
                textbutton _("Cicadian Rhythm (The Gardener) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars16", locked=False)
            else:
                text _("Cicadian Rhythm (The Gardener)")
            if beachwars17 == True:
                textbutton _("Bidder's Organs {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars17intro", locked=False)
            elif beachwars17skip == True:
                text _("{color=EF1A1A}{s}Bitter Organs{/s}{/color}")
            else:
                text _("Bidder's Organs")
            if beachwars18 == True:
                textbutton _("Flowerchild {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars18", locked=False)
            else:
                text _("Flowerchild")
            if beachwars19 == True:
                textbutton _("Danger to Society {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachwars19", locked=False)
            else:
                text _("Danger to Society")
            if halloweenfour1 == True:
                textbutton _("Eggside Octopus {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour1", locked=False)
            else:
                text _("Eggside Octopus")
            if halloweenfour2 == True:
                textbutton _("The Tenth Step {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour2", locked=False)
            else:
                text _("The Tenth Step")
            if halloweenfour3 == True:
                textbutton _("BONE-TOWN {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour3", locked=False)
            else:
                text _("BONE-TOWN")
            if halloweenfour4 == True:
                textbutton _("Try Honesty {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour4", locked=False)
            else:
                text _("Try Honesty")
            if halloweenfour5 == True:
                textbutton _("Heartache {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour5", locked=False)
            else:
                text _("Heartache")
            if halloweenfour6 == True:
                textbutton _("The King of Thebes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour6", locked=False)
            else:
                text _("The King of Thebes")
            if halloweenfour7 == True:
                textbutton _("Our Fathers {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour7", locked=False)
            else:
                text _("Our Fathers")
            if halloweenfour8 == True:
                textbutton _("Eighth Eye of the Wolf Spider {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour8", locked=False)
            else:
                text _("Eighth Eye of the Wolf Spider")
            if halloweenfour9 == True:
                textbutton _("Childspawn {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour9", locked=False)
            else:
                text _("Childspawn")
            if halloweenfour10 == True:
                textbutton _("An Excerpt From a Waterlogged Journal {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour10", locked=False)
            else:
                text _("An Excerpt From a Waterlogged Journal")
            if halloweenfour11 == True:
                textbutton _("Party Animal {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour11", locked=False)
            else:
                text _("Party Animal")
            if halloweenfour12 == True:
                textbutton _("Girls Just Want to Have Fun {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour12", locked=False)
            else:
                text _("Girls Just Want to Have Fun")
            if halloweenfour13 == True:
                textbutton _("Happy Memories {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour13", locked=False)
            else:
                text _("Happy Memories")
            if halloweenfour14 == True:
                textbutton _("For More Than Just Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour14", locked=False)
            else:
                text _("For More Than Just Me")
            if halloweenfour15 == True:
                textbutton _("I Won't Say I'm In Love {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour15", locked=False)
            else:
                text _("I Won't Say I'm In Love")
            if halloweenfour16 == True:
                textbutton _("The End of the World {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfour16", locked=False)
            else:
                text _("The End of the World")
            if resetsix1 == True:
                textbutton _("Times New Roman {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("resetsix1", locked=False)
            else:
                text _("Times New Roman")
            if resetsix2 == True:
                textbutton _("Paper City {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("resetsix2", locked=False)
            else:
                text _("Paper City")
            if resetsix3 == True:
                textbutton _("Meant to Be {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("resetsix3", locked=False)
            else:
                text _("Meant to Be")
            if resetsix4 == True:
                textbutton _("Remember to Smile {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("resetsix4", locked=False)
            else:
                text _("Remember to Smile")
            textbutton _("Back") action ShowMenu('eventtracker11')

screen maintrackerch4():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Main Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "Chapter 4"
            if springtime1 == True:
                textbutton _("The Collector {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime1", locked=False)
            else:
                text _("The Collector")
            if springtime2 == True:
                textbutton _("On the Count of Three {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime2", locked=False)
            else:
                text _("On the Count of Three")
            if springtime3 == True:
                textbutton _("Not the Nightingale {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime3", locked=False)
            else:
                text _("Not the Nightingale")
            if springtime4 == True:
                textbutton _("Silver & Gold {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime4", locked=False)
            else:
                text _("Silver & Gold")
            if springtime5 == True:
                textbutton _("November 1st {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime5", locked=False)
            else:
                text _("November 1st")
            if springtime6 == True:
                textbutton _("Visibly Impatient {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime6", locked=False)
            else:
                text _("Visibly Impatient")
            if springtime7 == True:
                textbutton _("The Final Human on the Face of the Earth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime7", locked=False)
            else:
                text _("The Final Human on the Face of the Earth")
            if springtime8 == True:
                textbutton _("Actual Jesus Quotes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime8", locked=False)
            else:
                text _("Actual Jesus Quotes")
            if springtime9 == True:
                textbutton _("In Regard to the Peony {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime9", locked=False)
            else:
                text _("In Regard to the Peony")
            if springtime10 == True:
                textbutton _("When the Sun Sleeps {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime10", locked=False)
            else:
                text _("When the Sun Sleeps")
            if springtime11 == True:
                textbutton _("Hunger Games {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime11", locked=False)
            else:
                text _("Hunger Games")
            if springtime12 == True:
                textbutton _("Shut Up & Kiss {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime12", locked=False)
            else:
                text _("Shut Up & Kiss")
            if springtime13 == True:
                textbutton _("Death (And Other Sad Stuff) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime13", locked=False)
            else:
                text _("Death (And Other Sad Stuff)")
            if springtime14 == True:
                textbutton _("The Legacy of Thaum Pt. V: The Faceless Empyrean {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime14", locked=False)
            else:
                text _("The Legacy of Thaum Pt. V: The Faceless Empyrean")
            if springtime15 == True:
                textbutton _("Goodnight Moon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime15", locked=False)
            else:
                text _("Goodnight Moon")
            if springtime16 == True:
                textbutton _("Your Blood in Spring {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime16", locked=False)
            else:
                text _("Your Blood in Spring")
            if springtime17 == True:
                textbutton _("Rhythm of a Black Heart {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime17", locked=False)
            else:
                text _("Rhythm of a Black Heart")
            if springtime18 == True:
                textbutton _("You & Me Against the World {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime18", locked=False)
            else:
                text _("You and Me Against the World")
            if springtime19 == True:
                textbutton _("Miserably Ever After {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springtime19", locked=False)
            else:
                text _("Miserably Ever After")
            if springend1 == True:
                textbutton _("Episcopalis: Pickled Plums & Polyrhythmic Psalms {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springend1", locked=False)
            else:
                text _("Episcopalis: Pickled Plums & Polyrhythmic Psalms")
            if springend2 == True:
                textbutton _("Okonomiyaki {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springend2", locked=False)
            else:
                text _("Okonomiyaki")
            if springend3 == True:
                textbutton _("500 Channels {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springend3", locked=False)
            else:
                text _("500 Channels")
            if springend4 == True:
                textbutton _("Wild Boar {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springend4", locked=False)
            else:
                text _("Wild Boar")
            if springend5 == True:
                textbutton _("All Eyes On Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("springend5", locked=False)
            else:
                text _("All Eyes On Me")
            if sportswars3 == True:
                textbutton _("War Never Changes: Egg Time Madness {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars3", locked=False)
            else:
                text _("War Never Changes: Egg Time Madness")
            if sportswars4 == True:
                textbutton _("Shohei Ohtani {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars4", locked=False)
            else:
                text _("Shohei Ohtani")
            if sportswars6 == True:
                textbutton _("Sea of Balls (Wise Turtle) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars6", locked=False)
            else:
                text _("Sea of Balls (Wise Turtle)")
            if sportswars7 == True:
                textbutton _("Cock Party 2 (Better Than The First) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars7", locked=False)
            else:
                text _("Cock Party 2 (Better Than The First)")
            if sportswars8 == True:
                textbutton _("Flowers & Forklifts {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars8", locked=False)
            else:
                text _("Flowers & Forklifts")
            if sportswars11 == True:
                textbutton _("David Beckham's Large Banana {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars11", locked=False)
            else:
                text _("David Beckham's Large Banana")
            if sportswars12 == True:
                textbutton _("Mr. Bones' Wild Ride {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars12", locked=False)
            else:
                text _("Mr. Bones' Wild Ride")
            if sportswars13 == True:
                textbutton _("Priestess of Fallen Snow {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars13", locked=False)
            else:
                text _("Priestess of Fallen Snow")
            if sportswars15 == True:
                textbutton _("Trauma Bond {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars15", locked=False)
            else:
                text _("Trauma Bond")
            if sportswars16 == True:
                textbutton _("Irregular Heartbeat {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars16", locked=False)
            else:
                text _("Irregular Heartbeat")
            if sportswars20 == True:
                textbutton _("Happy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars20", locked=False)
            else:
                text _("Happy")
            if beachfive1 == True:
                textbutton _("From The Heart (Red Shell) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive1", locked=False)
            else:
                text _("From The Heart (Red Shell)")
            if beachfive2 == True:
                textbutton _("Monkey's Paw {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive2", locked=False)
            else:
                text _("Monkey's Paw")
            if beachfive4 == True:
                textbutton _("Operation: Sleepytime {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive4", locked=False)
            else:
                text _("Operation: Sleepytime")
            if beachfive5 == True:
                textbutton _("Sod in the Seedbed {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive5", locked=False)
            else:
                text _("Sod in the Seedbed")
            if beachfive7 == True:
                textbutton _("Recycling {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive7", locked=False)
            else:
                text _("Recycling")
            if beachfive11 == True:
                textbutton _("Albatross {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive11", locked=False)
            else:
                text _("Albatross")
            if beachfive12 == True:
                textbutton _("Pros, Cons, and Countermeasures {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive12", locked=False)
            else:
                text _("Pros, Cons, and Countermeasures")
            if beachfive16 == True:
                textbutton _("Perfect Harmony {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive16", locked=False)
            else:
                text _("Perfect Harmony")
            if halloweenfive1 == True:
                textbutton _("Rubik’s Cube {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive1", locked=False)
            else:
                text _("Rubik’s Cube")
            if halloweenfive2 == True:
                textbutton _("More Than Her {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive2", locked=False)
            else:
                text _("More Than Her")
            if halloweenfive3 == True:
                textbutton _("Action/Inaction {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive3", locked=False)
            else:
                text _("Action/Inaction")
            if halloweenfive4 == True:
                textbutton _("Empty Heart Appeal {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive4", locked=False)
            else:
                text _("Empty Heart Appeal")
            if halloweenfive5 == True:
                textbutton _("The Art of Tribadism {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive5", locked=False)
            else:
                text _("The Art of Tribadism")
            if halloweenfive6 == True:
                textbutton _("Four Walls, A Garden {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive6", locked=False)
            else:
                text _("Four Walls, A Garden")
            if halloweenfive7 == True:
                textbutton _("SENSEI-QUEST {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive7", locked=False)
            else:
                text _("SENSEI-QUEST")
            if halloweenfive8 == True:
                textbutton _("Restart {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("endofgameworld", locked=False)
            else:
                text _("Restart")
            if halloweenfive9 == True:
                textbutton _("Recap {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive9", locked=False)
            else:
                text _("Recap")
            if halloweenfive10 == True:
                textbutton _("Yellow Patch (Heaven in My Hands) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive10", locked=False)
            else:
                text _("Yellow Patch (Heaven in My Hands)")
            if halloweenfive11 == True:
                textbutton _("Episcopalis: A Hymn for Him and She and Her {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive11", locked=False)
            else:
                text _("Episcopalis: A Hymn for Him and She and Her")
            if halloweenfive12 == True:
                textbutton _("Sigma Grindset {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive12", locked=False)
            else:
                text _("Sigma Grindset")
            if halloweenfive13 == True:
                textbutton _("All Around the Mulberry Bush {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive13", locked=False)
            else:
                text _("All Around the Mulberry Bush")
            if halloweenfive14 == True:
                textbutton _("Pop Goes the Weasel {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive14", locked=False)
            else:
                text _("Pop Goes the Weasel")
            if halloweenfive15 == True:
                textbutton _("God of Light {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive15", locked=False)
            else:
                text _("God of Light")
            if halloweenfive16 == True:
                textbutton _("Sonny Boy & The Magnificent Waiting Room {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive16", locked=False)
            else:
                text _("Sonny Boy & The Magnificent Waiting Room")
            if halloweenfive17 == True:
                textbutton _("What We’ll See When We Get There {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenfive17", locked=False)
            else:
                text _("What We’ll See When We Get There")
            if christmasfive1 == True:
                textbutton _("Aunt Niki (A Hundred Christmases) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasfive1", locked=False)
            else:
                text _("Aunt Niki (A Hundred Christmases)")
            if christmasfive2 == True:
                textbutton _("Caught in the Crossfire {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasfive2", locked=False)
            else:
                text _("Caught in the Crossfire")
            if christmasfive3 == True:
                textbutton _("The Legacy of Thaum Pt. VI: Thought Mirror {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasfive3", locked=False)
            else:
                text _("The Legacy of Thaum Pt. VI: Thought Mirror")
            if christmasfive4 == True:
                textbutton _("DON’T TALK TO MONKS {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasfive4", locked=False)
            else:
                text _("DON’T TALK TO MONKS")
            if christmasfive5 == True:
                textbutton _("The One With All the Sex Toys {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasfive5", locked=False)
            else:
                text _("The One With All the Sex Toys")
            if christmasfive6 == True:
                textbutton _("Seed of Self-Doubt {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasfive6", locked=False)
            else:
                text _("Seed of Self-Doubt")
            if christmasfive7 == True:
                textbutton _("Even Heaven {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasfive7", locked=False)
            else:
                text _("Even Heaven")
            if christmasfive8 == True:
                textbutton _("Post-Nut Clarity {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasfive8", locked=False)
            else:
                text _("Post-Nut Clarity")
            if dormwarsfive1 == True:
                textbutton _("Prepare For Battle! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive1", locked=False)
            else:
                text _("Prepare For Battle!")
            if dormwarsfive2 == True:
                textbutton _("Poetry At Best {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive2", locked=False)
            else:
                text _("Poetry At Best")
            if dormwarsfive3 == True:
                textbutton _("Beach(?) Babe Breakfast Barrage! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive3", locked=False)
            else:
                text _("Beach(?) Babe Breakfast Barrage!")
            if dormwarsfive4 == True:
                textbutton _("Dungeons & Divas! Normies Gone Nerdy! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive4", locked=False)
            else:
                text _("Dungeons & Divas! Normies Gone Nerdy!")
            if dormwarsfive5 == True:
                textbutton _("Talentless & Talkative! Trivia Turmoil! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive5", locked=False)
            else:
                text _("Talentless & Talkative! Trivia Turmoil!")
            if dormwarsfive6 == True:
                textbutton _("Sweet Joy Befall Thee! Be Nice to Sensei Battle! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive6", locked=False)
            else:
                text _("Sweet Joy Befall Thee! Be Nice to Sensei Battle!")
            if dormwarsfive7 == True:
                textbutton _("Shadow Word: Death Ball {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive7", locked=False)
            else:
                text _("Shadow Word: Death Ball")
            if dormwarsfive8 == True:
                textbutton _("Lovely Lawyers & The Laws of...Love! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive8", locked=False)
            else:
                text _("Lovely Lawyers & The Laws of...Love!")
            if dormwarsfive9 == True:
                textbutton _("Silhouettes of Scorned Princesses {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive9", locked=False)
            else:
                text _("Silhouettes of Scorned Princesses")
            if dormwarsfive10 == True:
                textbutton _("A Ghost's Guide on Haunting {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive10", locked=False)
            else:
                text _("A Ghost's Guide on Haunting")
            if dormwarsfive11 == True:
                textbutton _("Strippers? No! Swimsuits! (Pool-Toucher) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive11", locked=False)
            else:
                text _("Strippers? No! Swimsuits! (Pool-Toucher)")
            if dormwarsfive12 == True:
                textbutton _("Goth Girl Glamour Gala! {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive12", locked=False)
            else:
                text _("Goth Girl Glamour Gala!")
            if dormwarsfive13 == True:
                textbutton _("And Then There Were Two {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive13", locked=False)
            else:
                text _("And Then There Were Two")
            if nodokathontwo1 == True:
                textbutton _("John 13 (From God to God) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokathontwo1", locked=False)
            elif nodokathontwo1miss == True:
                text _("{color=EF1A1A}{s}New Commandments{/s}{/color}")
            else:
                text _("John 13 (From God to God)")
            if nodokathontwo2 == True:
                textbutton _("Genesis 19 (Pillars of Salt) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokathontwo2", locked=False)
            elif nodokathontwo2miss == True:
                text _("{color=EF1A1A}{s}Zoar in Flames{/s}{/color}")
            else:
                text _("Genesis 19 (Pillars of Salt)")
            if nodokathontwo3 == True:
                textbutton _("Thessalonians 4 (Lust Like the Pagans) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokathontwo3", locked=False)
            elif nodokathontwo3miss == True:
                text _("{color=EF1A1A}{s}The Trumpet Call of God{/s}{/color}")
            else:
                text _("Thessalonians 4 (Lust Like the Pagans)")
            if dormwarsfive14 == True:
                textbutton _("Partial to Jasmine {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfive14", locked=False)
            else:
                text _("Partial to Jasmine")
            if beachsix1 == True:
                textbutton _("The Legacy of Thaum (On a Bus) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsix1", locked=False)
            else:
                text _("The Legacy of Thaum (On a Bus)")
            if beachsix2 == True:
                textbutton _("Natural Instinct {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsix2", locked=False)
            else:
                text _("Natural Instinct")
            if beachsix3 == True:
                textbutton _("Buyer's Remorse (Suicide Fund) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsix3", locked=False)
            else:
                text _("Buyer's Remorse (Suicide Fund)")
            if beachsix4 == True:
                textbutton _("Peregrine Falcon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsix4", locked=False)
            else:
                text _("Peregrine Falcon")
            if beachsix5 == True:
                textbutton _("Pulling Ahead {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsix5", locked=False)
            else:
                text _("Pulling Ahead")
            if beachsix6 == True:
                textbutton _("Cities in Gifu {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsix6", locked=False)
            else:
                text _("Cities in Gifu")
            if beachsix7 == True:
                textbutton _("Flowers for Algernon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsix7", locked=False)
            else:
                text _("Flowers for Algernon")
            if beachsix8 == True:
                textbutton _("Into the Void {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsix8", locked=False)
            else:
                text _("Into the Void")
            textbutton _("Back") action ShowMenu('eventtracker11')

screen gamemenuyuki():

    tag menu
    if yukimenuoutfit is not None and renpy.loadable(yukimenuoutfit) :
        add yukimenuoutfit
    else :
        add "game_menuyuki.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#CDCDCD}Height: 5'9/175cm{/color}") style "profile"
        text ("{color=#CDCDCD}Birthday: April 20th{/color}") style "profile"
        text ("\n{color=#CDCDCD}Affection: [yuki_love]{/color}") style "profile"
        text ("{color=#CDCDCD}Lust: N/A{/color}") style "profile"
        text ("{color=#CDCDCD}Headpats: 0{/color}") style "profile"
        text ("{color=#CDCDCD}Events: [yukipoint]/14{/color}") style "profile"

    imagebutton:
        idle "yukievrep1.png"
        hover "yukievrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('yukitracker')

    if yukispring5 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/yukigangrep1.png"
            hover "subscribestar/images2/yukigangrep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('yukireplays')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(yuki_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen yukitracker():

    tag menu

    use game_menu(_("Yuki Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=CDCDCD}Yuki Yamaguchi ([yuki_love] Affection){/color}"
            if yukidate1 == True:
                textbutton _("Rule #1 {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukidate1", locked=False)
            else:
                text _("Rule #1")
            if yukidate5 == True:
                textbutton _("Better Off Alone {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukidate5", locked=False)
            else:
                text _("Better Off Alone")
            if yukidate10 == True:
                textbutton _("Opposite Directions {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukidate10", locked=False)
            else:
                text _("Opposite Directions")
            if yukidate10p2 == True:
                textbutton _("A Thing of the Past {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukidate10p2", locked=False)
            else:
                text _("A Thing of the Past")
            text _("-----------------------------------------------------------")
            if yukidate20p1 == True:
                textbutton _("Funeral Plans {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukidate20p1", locked=False)
            else:
                text _("Funeral Plans")
            if yukidate20p2 == True:
                textbutton _("Douchebag McDouchefuck {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukidate20p2", locked=False)
            else:
                text _("Douchebag McDouchefuck")
            if yukidate25 == True:
                textbutton _("Pride & Joy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukidate25", locked=False)
            else:
                text _("Pride & Joy")
            text _("-----------------------------------------------------------")
            if yukicamp1 == True:
                textbutton _("Big Dog {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukicamp1", locked=False)
            else:
                text _("Big Dog")
            if yukicamp2 == True:
                textbutton _("My Heart is in Rotenburg {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukicamp2", locked=False)
            else:
                text _("My Heart is in Rotenburg")
            if yukispring1 == True:
                textbutton _("Small Plastic Baggies {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukispring1", locked=False)
            else:
                text _("Small Plastic Baggies")
            if yukispring2 == True:
                textbutton _("Better Than Sex {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukispring2", locked=False)
            else:
                text _("Better Than Sex")
            if yukispring3 == True:
                textbutton _("As the Footsteps Die Out Forever {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukispring3", locked=False)
            else:
                text _("As the Footsteps Die Out Forever")
            if yukispring4 == True:
                textbutton _("Heart of Fear {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukispring4", locked=False)
            else:
                text _("Heart of Fear")
            if yukispring5 == True:
                textbutton _("When I Say “Jump” {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yukispring5", locked=False)
            else:
                text _("When I Say “Jump”")
            textbutton _("Back") action ShowMenu('gamemenuyuki')

screen wakanatracker():

    tag menu

    use game_menu(_("Wakana Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=540087}Wakana Watabe ([wakana_love] Affection){/color}"
            if wakanadate1 == True:
                textbutton _("To the River {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanadate1", locked=False)
            else:
                text _("To the River")
            if wakanadate5 == True:
                textbutton _("Soup, or Another Year With You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanadate5", locked=False)
            else:
                text _("Soup, or Another Year With You")
            text _("-----------------------------------------------------------")
            if wakanadate15 == True:
                textbutton _("Pseudonym {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanadate15", locked=False)
            else:
                text _("Pseudonym")
            if wakanaspecial15 == True:
                textbutton _("Don't Hold Back {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanaspecial15", locked=False)
            else:
                text _("Don't Hold Back")
            if wakanadate25p1 == True:
                textbutton _("The Desk Scene {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanadate25p1", locked=False)
            else:
                text _("The Desk Scene")
            if wakanadate25p2 == True:
                textbutton _("Human Error {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanadate25p2", locked=False)
            else:
                text _("Human Error")
            if wakanadate25p3 == True:
                textbutton _("Follow My Lead {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanadate25p3", locked=False)
            else:
                text _("Follow My Lead")
            text _("-----------------------------------------------------------")
            if wakanaspring1 == True:
                textbutton _("Enough is Not Enough {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanaspring1", locked=False)
            else:
                text _("Enough is Not Enough")
            if wakanaspring2 == True:
                textbutton _("In the Morning, I'll Forget {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanaspring2", locked=False)
            else:
                text _("In the Morning, I'll Forget")
            if wakanaspring3 == True:
                textbutton _("I'm Wide Awake, It's Morning {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanaspring3", locked=False)
            else:
                text _("I'm Wide Awake, It's Morning")
            if wakanaspring4 == True:
                textbutton _("Dark White (Pretty Joy) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanaspring4", locked=False)
            else:
                text _("Dark White (Pretty Joy)")
            if wakanaspring5 == True:
                textbutton _("Connect the Dots {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanaspring5", locked=False)
            else:
                text _("Connect the Dots")
            if wakanaspring6 == True:
                textbutton _("From the Horse’s Mouth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("wakanaspring6", locked=False)
            else:
                text _("From the Horse’s Mouth")
            textbutton _("Back") action ShowMenu('gamemenuwakana')

screen osakotracker():

    tag menu

    use game_menu(_("Osako Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=9A6BA1}Osako Osaka ([osako_love] Affection){/color}"
            if osakodate1 == True:
                textbutton _("Pressure Point {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakodate1", locked=False)
            else:
                text _("Pressure Point")
            if osakodojo1 == True:
                textbutton _("Floating Forever, Unfulfilled {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakodojo1", locked=False)
            else:
                text _("Floating Forever, Unfulfilled")
            text _("-----------------------------------------------------------")
            if osakodate15 == True:
                textbutton _("Young At Heart {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakodate15", locked=False)
            else:
                text _("Young At Heart")
            if osakodate20 == True:
                textbutton _("House of the Unholy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakodate20", locked=False)
            else:
                text _("House of the Unholy")
            text _("-----------------------------------------------------------")
            if osakospring1 == True:
                textbutton _("Chaos Spiral (Heterosexual Sex) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakospring1", locked=False)
            else:
                text _("Chaos Spiral (Heterosexual Sex)")
            if osakospring2 == True:
                textbutton _("Meat-Pocket {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakospring2", locked=False)
            else:
                text _("Meat-Pocket")
            if osakospring3 == True:
                textbutton _("Indecent Proposal {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakospring3", locked=False)
            else:
                text _("Indecent Proposal")
            if osakospring4 == True:
                textbutton _("MILF of the Month Club {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakospring4", locked=False)
            else:
                text _("MILF of the Month Club")
            if osakospring5 == True:
                textbutton _("Girl C {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakospring5", locked=False)
            else:
                text _("Girl C")
            if osakospring6 == True:
                textbutton _("All Good Things {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("osakospring6", locked=False)
            else:
                text _("All Good Things")
            textbutton _("Back") action ShowMenu('gamemenuosako')

screen tsubasatracker():

    tag menu

    use game_menu(_("Tsubasa Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=eae6aa}Tsubasa Tsukioka ([tsubasa_love] Affection){/color}"
            if tsubasadate1 == True:
                textbutton _("Everbloom (Pride of the Sinful Sort) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasadate1", locked=False)
            else:
                text _("Everbloom (Pride of the Sinful Sort)")
            if tsubasadate1p2 == True:
                textbutton _("The Deep End {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasadate1p2", locked=False)
            else:
                text _("The Deep End")
            text _("-----------------------------------------------------------")
            if tsubasaspecial15 == True:
                textbutton _("Heart of Gold {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasaspecial15", locked=False)
            else:
                text _("Heart of Gold")
            if tsubasadate20 == True:
                textbutton _("Playing God {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasadate20", locked=False)
            else:
                text _("Playing God")
            if tsubasaspecial20 == True:
                textbutton _("The Lucky Few {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasaspecial20", locked=False)
            else:
                text _("The Lucky Few")
            text _("-----------------------------------------------------------")
            if tsubasaspring1 == True:
                textbutton _("The Bird & The Worm {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasaspring1", locked=False)
            else:
                text _("The Bird & The Worm")
            if tsubasaspring2 == True:
                textbutton _("Petite Sirah {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasaspring2", locked=False)
            elif tsubasaspring2miss == True:
                text _("{color=EF1A1A}{s}Bum Wine{/s}{/color}")
            else:
                text _("Petite Sirah")
            if tsubasaspring3 == True:
                textbutton _("The Pleasures of the Flesh {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasaspring3", locked=False)
            elif tsubasaspring3miss == True:
                text _("{color=EF1A1A}{s}It Changes With The Light{/s}{/color}")
            else:
                text _("The Pleasures of the Flesh")
            if christmastsubasa1 == True:
                textbutton _("Yes, Mother {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastsubasa1", locked=False)
            elif christmastsubasa1miss == True:
                text _("{color=EF1A1A}{s}You Are a Very Bad Boy{/s}{/color}")
            else:
                text _("Yes, Mother")
            if tsubasaspring4 == True:
                textbutton _("Hands-On Learning {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasaspring4", locked=False)
            elif tsubasaspring4miss == True:
                text _("{color=EF1A1A}{s}The Good Guy Approach{/s}{/color}")
            else:
                text _("Hands-On Learning")
            if tsubasaspring5 == True:
                textbutton _("For the Sake of Brevity {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasaspring5", locked=False)
            elif tsubasaspring5miss == True:
                text _("{color=EF1A1A}{s}Solitary Bath Time{/s}{/color}")
            else:
                text _("For the Sake of Brevity")
            if tsubasaspring6 == True:
                textbutton _("When We Dead Awaken {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsubasaspring6", locked=False)
            else:
                text _("When We Dead Awaken")
            textbutton _("Back") action ShowMenu('gamemenutsubasa')

screen tsukasatracker():

    tag menu

    use game_menu(_("Tsukasa Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=f0ca8c}Tsukasa Tsukioka ([tsukasa_love] Affection){/color}"
            if tsukasaspecial1 == True:
                textbutton _("National Tsukasa Day {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsukasaspecial1", locked=False)
            else:
                text _("National Tsukasa Day")
            if tsukasaspecial1p2 == True:
                textbutton _("Jeeves Tsukioka XIII {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsukasaspecial1p2", locked=False)
            else:
                text _("Jeeves Tsukioka XIII")
            text _("-----------------------------------------------------------")
            if tsukasaspring1 == True:
                textbutton _("Vow of Silence (Pole Position) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsukasaspring1", locked=False)
            elif tsukasaspring1skip == True:
                text _("{color=EF1A1A}{s}YOU{/s}{/color}")
            else:
                text _("Vow of Silence (Pole Position)")
            if tsukasaspring2 == True:
                textbutton _("Blood & Sunset {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsukasaspring2", locked=False)
            elif tsukasaspring2skip == True:
                text _("{color=EF1A1A}{s}ARE{/s}{/color}")
            else:
                text _("Blood & Sunset")
            if tsukasaspring3 == True:
                textbutton _("Failsafe {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsukasaspring3", locked=False)
            elif tsukasaspring3skip == True:
                text _("{color=EF1A1A}{s}WEAK{/s}{/color}")
            else:
                text _("Failsafe")
            if christmastsukasa1 == True:
                textbutton _("A Part of Your World {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmastsukasa1", locked=False)
            else:
                text _("A Part of Your World")
            if tsukasaspring4 == True:
                textbutton _("The Talk {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsukasaspring4", locked=False)
            elif tsukasaspring4skip == True:
                text _("{color=EF1A1A}{s}WEAK{/s}{/color}")
            else:
                text _("The Talk")
            if tsukasaspring5 == True:
                textbutton _("Six Inches of Suffering {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsukasaspring5", locked=False)
            elif tsukasaspring5miss == True:
                text _("{color=EF1A1A}{s}No Penis, No Gain{/s}{/color}")
            else:
                text _("Six Inches of Suffering")
            if tsukasaspring6 == True:
                textbutton _("Useless, Flightless Fledgling {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("tsukasaspring6", locked=False)
            elif tsukasaspring6miss == True:
                text _("{color=EF1A1A}{s}Leaving the Nest{/s}{/color}")
            else:
                text _("Useless, Flightless Fledgling")
            textbutton _("Back") action ShowMenu('gamemenutsukasa')

screen gamemenuuta():

    tag menu
    if utamenuoutfit is not None and renpy.loadable(utamenuoutfit) :
        add utamenuoutfit
    else :
        add "game_menuuta.png"

    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#AA4588}Height: 4'11/149cm{/color}") style "profile"
        text ("{color=#AA4588}Birthday: August 1st{/color}") style "profile"
        text ("\n{color=#AA4588}Affection: [uta_love]{/color}") style "profile"
        text ("{color=#AA4588}Lust: N/A{/color}") style "profile"
        text ("{color=#AA4588}Headpats: 0{/color}") style "profile"
        text ("{color=#AA4588}Events: [utapoint]/23{/color}") style "profile"

    imagebutton:
        idle "utaevrep1.png"
        hover "utaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('utatracker')

    imagebutton:
        idle "lock.png"
        hover "lock.png"
        xalign 0.925 yalign 0.935
        focus_mask True
        #action ShowMenu('amireplays')

    if utanudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('utaphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('utaphone')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(uta_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen utatracker():

    tag menu

    use game_menu(_("Uta Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=AA4588}Uta Ushibori ([uta_love] Affection){/color}"
            if utafirsthall == True:
                textbutton _("Far From Home {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utafirsthall", locked=False)
            else:
                text _("Far From Home")
            if utamaid1 == True:
                textbutton _("Abuse of Power {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utamaid1", locked=False)
            else:
                text _("Abuse of Power")
            if utamaid5 == True:
                textbutton _("Love Me to Pieces {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utamaid5", locked=False)
            else:
                text _("Love Me to Pieces")
            if utadorm5 == True:
                textbutton _("The VIP Treatment {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utadorm5", locked=False)
            else:
                text _("The VIP Treatment")
            if utadorm10 == True:
                textbutton _("Shawshank Redemption {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utadorm10", locked=False)
            else:
                text _("Shawshank Redemption")
            if utamaid10 == True:
                textbutton _("Happier Things {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utamaid10", locked=False)
            else:
                text _("Happier Things")
            if utadorm15 == True:
                textbutton _("Facetime With My Mom (Tonight) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utadorm15", locked=False)
            else:
                text _("Facetime With My Mom (Tonight)")
            if utamaid20 == True:
                textbutton _("Veins and the Circulatory System {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utamaid20", locked=False)
            else:
                text _("Veins and the Circulatory System")
            if utadorm20 == True:
                textbutton _("Blood Everywhere {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utadorm20", locked=False)
            else:
                text _("Blood Everywhere")
            text _("-----------------------------------------------------------")
            if utaarchery1 == True:
                textbutton _("Impulse {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utaarchery1", locked=False)
            else:
                text _("Impulse")
            if utamaid25p1 == True:
                textbutton _("Where Wishes Come True {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utamaid25p1", locked=False)
            else:
                text _("Where Wishes Come True")
            if utamaid25p2 == True:
                textbutton _("After the Rain {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utamaid25p2", locked=False)
            else:
                text _("After the Rain")
            if utadorm30 == True:
                textbutton _("Uta-chan {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utadorm30", locked=False)
            else:
                text _("Uta-chan")
            if utaspecial35 == True:
                textbutton _("Young & Stupid {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utaspecial35", locked=False)
            else:
                text _("Young & Stupid")
            if utadate35 == True:
                textbutton _("Enjo Kousai {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utadate35", locked=False)
            else:
                text _("Enjo Kousai")
            if utadorm40p1 == True:
                textbutton _("Whore {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utadorm40p1", locked=False)
            else:
                text _("Whore")
            if utadorm40p2 == True:
                textbutton _("The Girl From Nara {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utadorm40p2", locked=False)
            else:
                text _("The Girl From Nara")
            text _("-----------------------------------------------------------")
            if utaspring1 == True:
                textbutton _("To Be Wanted {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utaspring1", locked=False)
            else:
                text _("To Be Wanted")
            if utaspring2 == True:
                textbutton _("Meet Me At Our Spot {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utaspring2", locked=False)
            else:
                text _("Meet Me At Our Spot")
            if beachfive14 == True:
                textbutton _("Reasons For Rain {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive14", locked=False)
            else:
                text _("Reasons For Rain")
            if utaspring3 == True:
                textbutton _("Songs of Autumn {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utaspring3", locked=False)
            else:
                text _("Songs of Autumn")
            if utaspring4 == True:
                textbutton _("Heebie-Jeebies {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utaspring4", locked=False)
            else:
                text _("Heebie-Jeebies")
            if utaspring5 == True:
                textbutton _("A Thousand Times, Yes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("utaspring5", locked=False)
            else:
                text _("A Thousand Times, Yes")
            textbutton _("Back") action ShowMenu('gamemenuuta')

screen gamemenuio():

    tag menu
    if iomenuoutfit is not None and renpy.loadable(iomenuoutfit) :
        add iomenuoutfit
    else :
        add "game_menuio.png"

    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#BBE3A1}Height: 5'1/155cm{/color}") style "profile"
        text ("{color=#BBE3A1}Birthday: May 24th{/color}") style "profile"
        text ("\n{color=#BBE3A1}Affection: [io_love]{/color}") style "profile"
        text ("{color=#BBE3A1}Lust: N/A{/color}") style "profile"
        text ("{color=#BBE3A1}Headpats: 0{/color}") style "profile"
        if iomiss < 1:
            text ("{color=#BBE3A1}Events: [iopoint]/23{/color}") style "profile"
        else:
            text ("{color=#BBE3A1}Events: [iopoint]/23{/color} {color=#FF0000}([iomiss] Missed){/color}") style "profile"

    imagebutton:
        idle "ioevrep1.png"
        hover "ioevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('iotracker')

    if iospring3 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/iostomachacherep1.png"
            hover "subscribestar/images2/iostomachacherep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('ioreplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(io_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen iotracker():

    tag menu

    use game_menu(_("Io Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=BBE3A1}Io Ichimonji ([io_love] Affection){/color}"
            if iofirsthall == True:
                textbutton _("Viva la Revolución {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iofirsthall", locked=False)
            else:
                text _("Viva la Revolución")
            if bathhouse1 == True:
                textbutton _("Nonetheless, I'm Here {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bathhouse1", locked=False)
            else:
                text _("Nonetheless, I'm Here")
            if bathhouse5 == True:
                textbutton _("The Girl with the Dragon Tattoo {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bathhouse5", locked=False)
            else:
                text _("The Girl with the Dragon Tattoo")
            if iodorm5 == True:
                textbutton _("Unnamed Wooden Robots {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iodorm5", locked=False)
            else:
                text _("Unnamed Wooden Robots")
            if iodorm10 == True:
                textbutton _("Paperthin {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iodorm10", locked=False)
            else:
                text _("Paperthin")
            if bathhouse10 == True:
                textbutton _("Turn On The Lights {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bathhouse10", locked=False)
            else:
                text _("Turn On The Lights")
            if iodorm15 == True:
                textbutton _("Amongst Other Things {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iodorm15", locked=False)
            else:
                text _("Amongst Other Things")
            if bathhouse20 == True:
                textbutton _("One Man's Trash {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bathhouse20", locked=False)
            else:
                text _("One Man's Trash")
            if bathhouse20part2 == True:
                textbutton _("Another Man's Treasure {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bathhouse20part2", locked=False)
            else:
                text _("Another Man's Treasure")
            text _("-----------------------------------------------------------")
            if ioarchery1 == True:
                textbutton _("Cupid's Arrow {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ioarchery1", locked=False)
            else:
                text _("Cupid's Arrow")
            if bathhouse25 == True:
                textbutton _("Work Less, Not Hard {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bathhouse25", locked=False)
            else:
                text _("Work Less, Not Hard")
            if iodorm25 == True:
                textbutton _("Heartbreak & Harmony {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iodorm25", locked=False)
            else:
                text _("Heartbreak & Harmony")
            if iospecial30 == True:
                textbutton _("1999 PC Classic, Rollercoaster Tycoon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iospecial30", locked=False)
            else:
                text _("1999 PC Classic, Rollercoaster Tycoon")
            if bathhouse35p1 == True:
                textbutton _("Tennis Ball {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bathhouse35p1", locked=False)
            else:
                text _("Tennis Ball")
            if bathhouse35p2 == True:
                textbutton _("Hold You Over {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("bathhouse35p2", locked=False)
            else:
                text _("Hold You Over")
            if iodorm35 == True:
                textbutton _("Yellow Cactus Flower {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iodorm35", locked=False)
            else:
                text _("Yellow Cactus Flower")
            if ioarchery35 == True:
                textbutton _("Two Of Us Are Thinking {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("ioarchery35", locked=False)
            else:
                text _("Two Of Us Are Thinking")
            text _("-----------------------------------------------------------")
            if iospring1 == True:
                textbutton _("My Indigo (The Blue Death) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iospring1", locked=False)
            else:
                text _("My Indigo (The Blue Death)")
            if iospring2 == True:
                textbutton _("Komorebi {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iospring2", locked=False)
            else:
                text _("Komorebi")
            if iospring3 == True:
                textbutton _("Stomachache {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iospring3", locked=False)
            elif iospring3miss == True:
                text _("{color=EF1A1A}{s}Dress-Up{/s}{/color}")
            else:
                text _("Stomachache")
            if iospring4 == True:
                textbutton _("1997 PC Classic, Theme Hospital {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iospring4", locked=False)
            else:
                text _("1997 PC Classic, Theme Hospital")
            if iospring5 == True:
                textbutton _("Even Winning Feels Bad {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("iospring5", locked=False)
            else:
                text _("Even Winning Feels Bad")
            if dormwarsfiveio1 == True:
                textbutton _("Endless Black (Sea of Nothing) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("dormwarsfiveio1", locked=False)
            else:
                text _("Endless Black (Sea of Nothing)")
            textbutton _("Back") action ShowMenu('gamemenuio')

screen gamemenunoriko():

    tag menu
    if norikomenuoutfit is not None and renpy.loadable(norikomenuoutfit) :
        add norikomenuoutfit
    else :
        add "game_menunoriko.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#FF61A9}Height: 5'6/168cm{/color}") style "profile"
        text ("{color=#FF61A9}Birthday: July 28th{/color}") style "profile"
        text ("\n{color=#FF61A9}Affection: [noriko_love]{/color}") style "profile"
        text ("{color=#FF61A9}Lust: [noriko_love]{/color}") style "profile"
        text ("{color=#FF61A9}Headpats: [norikopats]{/color}") style "profile"
        if norikomiss < 1:
            text ("{color=#FF61A9}Events: [norikopoint]/22{/color}") style "profile"
        else:
            text ("{color=#FF61A9}Events: [norikopoint]/22{/color} {color=#FF0000}([norikomiss] Missed){/color}") style "profile"

    imagebutton:
        idle "norikoevrep1.png"
        hover "norikoevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('norikotracker')

    if bonus == True:
        if norikoinvite2 == True:
            imagebutton:
                idle "subscribestar/images2/norikofirstinvrep1.png"
                hover "subscribestar/images2/norikofirstinvrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('norikoreplays')
        else:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')

        if norikonudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('norikophone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('norikophone')

    textbutton _("{size=+20}Change Profile Outfit{/size}"):
        action Function(noriko_next_outfit)
        xalign 0.305 yalign 0

    textbutton _("{size=+20}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.255 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen norikotracker():

    tag menu

    use game_menu(_("Noriko Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=FF61A9}Noriko Nakayama ([noriko_love] Affection){/color}"
            if norikofirsthall == True:
                textbutton _("Sculpture (Dream Girl) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikofirsthall", locked=False)
            else:
                text _("Sculpture (Dream Girl)")
            if convenience1 == True:
                textbutton _("Nakayarakawayama {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("convenience1", locked=False)
            else:
                text _("Nakayarakawayama")
            if norikodorm5 == True:
                textbutton _("Semi-Constructive Criticism {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikodorm5", locked=False)
            else:
                text _("Semi-Constructive Criticism")
            if convenience5 == True:
                if bonus == True:
                    textbutton _("Mouthjob {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("convenience5", locked=False)
                else:
                    textbutton _("Dental Occupation {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("convenience5", locked=False)
            elif bonus == True:
                text _("Mouthjob")
            else:
                text _("Dental Occupation")
            if norikodorm10 == True:
                textbutton _("Kind Of, Yes. Kind Of, No. {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikodorm10", locked=False)
            else:
                text _("Kind Of, Yes. Kind Of, No.")
            if norikoinvite1 == True:
                textbutton _("New Shoes {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikoinvite1", locked=False)
            else:
                text _("{color=778EFF}New Shoes{/color}")
            if norikoinvite2 == True:
                textbutton _("Beginnings. Endings. Things in Between. {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikoinvite2", locked=False)
            else:
                text _("{color=778EFF}Beginnings. Endings. Things in Between.{/color}")
            if norikospecial20 == True:
                textbutton _("Fair & Square {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikospecial20", locked=False)
            else:
                text _("Fair & Square")
            if norikodorm20 == True:
                textbutton _("Homes for the Homeless {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikodorm20", locked=False)
            else:
                text _("Homes for the Homeless")
            if convenience25 == True:
                if bonus == True:
                    textbutton _("That One FMK Scene {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("convenience25", locked=False)
                else:
                    textbutton _("That One Hopscotch Scene {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("convenience25", locked=False)
            elif bonus == True:
                text _("That One FMK Scene")
            else:
                text _("That One Hopscotch Scene")
            if norikodorm25 == True:
                textbutton _("Loxosceles Reclusa {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikodorm25", locked=False)
            else:
                text _("Loxosceles Reclusa")
            text _("-----------------------------------------------------------")
            if norikodate30 == True:
                textbutton _("Hotel Noriko {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikodate30", locked=False)
            else:
                text _("Hotel Noriko")
            if norikodorm30 == True:
                textbutton _("Dotted Line {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikodorm30", locked=False)
            else:
                text _("Dotted Line")
            if norikoinvite3 == True:
                textbutton _("I Really Want to Stay at Your House {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikoinvite3", locked=False)
            elif norikoinvite3skip == True:
                text _("{color=EF1A1A}{s}CONSUMED BY THE OLD ONE{/s}{/color}")
            else:
                text _("{color=778EFF}I Really Want to Stay at Your House{/color}")
            if norikoinvite4 == True:
                textbutton _("Somewhere {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikoinvite4", locked=False)
            elif norikoinvite4skip == True:
                text _("{color=EF1A1A}{s}NOWHERE{/s}{/color}")
            else:
                text _("{color=778EFF}Somewhere{/color}")
            text _("-----------------------------------------------------------")
            if sportswars2 == True:
                textbutton _("Rivals (Taco Tuesday) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars2", locked=False)
            else:
                text _("Rivals (Taco Tuesday)")
            if norikospring1 == True:
                textbutton _("The Long Road Ahead {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikospring1", locked=False)
            else:
                text _("The Long Road Ahead")
            if norikospring2 == True:
                textbutton _("Transpacific Sadness Symposium I: DEN OF THE MOLE RAT {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikospring2", locked=False)
            else:
                text _("Transpacific Sadness Symposium I: DEN OF THE MOLE RAT")
            if norikospring3 == True:
                textbutton _("Hard-Off {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikospring3", locked=False)
            else:
                text _("Hard-Off")
            if norikospring4 == True:
                textbutton _("Haiku {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikospring4", locked=False)
            else:
                text _("Haiku")
            if norikospring5 == True:
                textbutton _("At The Beach, In Every Life {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("norikospring5", locked=False)
            else:
                text _("At The Beach, In Every Life")
            if beachsixnoriko1 == True:
                textbutton _("Circling the Drain {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixnoriko1", locked=False)
            else:
                text _("{color=FF85FD}Circling the Drain{/color}")
            textbutton _("Back") action ShowMenu('gamemenunoriko')

screen gamemenuniki():

    tag menu
    if nikimenuoutfit is not None and renpy.loadable(nikimenuoutfit) :
        add nikimenuoutfit
    else :
        add "game_menuniki.png"

    $ v11check()
    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#FF0074}Height: 5'7/170cm{/color}") style "profile"
        text ("{color=#FF0074}Birthday: March 3rd{/color}") style "profile"
        text ("\n{color=#FF0074}Affection: [niki_love]{/color}") style "profile"
        text ("{color=#FF0074}Lust: [niki_lust]{/color}") style "profile"
        text ("{color=#FF0074}Headpats: [nikipats]{/color}") style "profile"
        text ("{color=#FF0074}Events: [nikipoint]/17{/color}") style "profile"

    imagebutton:
        idle "nikievrep1.png"
        hover "nikievrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('nikitracker')

    if bonus == True:
        if nikidate15 == True:
            imagebutton:
                idle "subscribestar/images2/nikifingerrep1.png"
                hover "subscribestar/images2/nikifingerrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('nikireplays')
        else:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')

        if nikinudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('nikiphone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('nikiphone')

    textbutton _("{size=+10}Change Profile Outfit{/size}"):
        action Function(niki_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+10}Go Back{/size}"):
        action ShowMenu('eventtrackersidecharahub')
        xalign 0.242 yalign 0.075

    textbutton _("Return"):
        style "return_button"

        action Return()

screen nikitracker():

    tag menu

    use game_menu(_("Niki Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "\n{color=FF0074}Niki Nakayama ([niki_love] Affection){/color}"
            if nikidate1 == True:
                textbutton _("Cotton Candy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikidate1", locked=False)
            else:
                text _("Cotton Candy")
            if nikidate5 == True:
                textbutton _("Like it's Any Other Day {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikidate5", locked=False)
            else:
                text _("Like it's Any Other Day")
            if nikidate10 == True:
                textbutton _("Thousands, If Not Millions {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikidate10", locked=False)
            else:
                text _("Thousands, If Not Millions")
            if nikidate15 == True:
                textbutton _("Hotel Rooms {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikidate15", locked=False)
            else:
                text _("Hotel Rooms")
            if nikiinvite1 == True:
                textbutton _("Sisters {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikiinvite1", locked=False)
            else:
                text _("{color=778EFF}Sisters{/color}")
            if nikiinvite2 == True:
                textbutton _("Dear You {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikiinvite2", locked=False)
            else:
                text _("{color=778EFF}Dear You{/color}")
            text _("-----------------------------------------------------------")
            if nikilovesyou1 == True:
                textbutton _("What it Takes to Move Forward {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikilovesyou1", locked=False)
            else:
                text _("What it Takes to Move Forward")
            if nikilovesyou2 == True:
                textbutton _("The End of the Tour (Glasswalker) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikilovesyou2", locked=False)
            else:
                text _("The End of the Tour (Glasswalker)")
            if nikilovesyou3 == True:
                textbutton _("How To Make Love Stay {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikilovesyou3", locked=False)
            else:
                text _("How To Make Love Stay")
            if nikifirstlust == True:
                textbutton _("Non-Disclosure Agreement {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikifirstlust", locked=False)
            else:
                text _("{color=FF85FD}Non-Disclosure Agreement{/color}")
            text _("-----------------------------------------------------------")
            if nikispring1 == True:
                textbutton _("They Came Together {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikispring1", locked=False)
            else:
                text _("They Came Together")
            if nikispring2 == True:
                textbutton _("The Clod and the Pebble {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikispring2", locked=False)
            else:
                text _("The Clod and the Pebble")
            if beachfive8 == True:
                textbutton _("Broken Furniture {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive8", locked=False)
            else:
                text _("Broken Furniture")
            if nikispring3 == True:
                textbutton _("That Funny Feeling {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikispring3", locked=False)
            else:
                text _("That Funny Feeling")
            if nikispring4 == True:
                textbutton _("Costco (Dick Lover) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikispring4", locked=False)
            else:
                text _("Costco (Dick Lover)")
            if nikispring5 == True:
                textbutton _("Beauty in What's Broken {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikispring5", locked=False)
            else:
                text _("Beauty in What's Broken")
            if nikispring6 == True:
                textbutton _("Artificial Love {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nikispring6", locked=False)
            else:
                text _("Artificial Love")
            textbutton _("Back") action ShowMenu('gamemenuniki')

screen gamemenunodoka():

    tag menu
    if nodokamenuoutfit is not None and renpy.loadable(nodokamenuoutfit) :
        add nodokamenuoutfit
    else :
        add "game_menunodoka.png"

    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#AF89A2}Height: 5'5/165cm{/color}") style "profile"
        text ("{color=#AF89A2}Birthday: April 17th{/color}") style "profile"
        text ("\n{color=#AF89A2}Affection: [nodoka_love]{/color}") style "profile"
        text ("{color=#AF89A2}Lust: [nodoka_lust]{/color}") style "profile"
        text ("{color=#AF89A2}Headpats: [nodokapats]{/color}") style "profile"
        if nodokamiss < 1:
            text ("{color=#AF89A2}Events: [nodokapoint]/21{/color}") style "profile"
        else:
            text ("{color=#ff4dd2}Events: [nodokapoint]/21{/color} {color=#FF0000}([nodokamiss] Missed){/color}") style "profile"


    imagebutton:
        idle "nodokaevrep1.png"
        hover "nodokaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('nodokatracker')

    if bonus == True:
        if futabalust15 == True:
            imagebutton:
                idle "subscribestar/images2/futabanodokawar1.png"
                hover "subscribestar/images2/futabanodokawar2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('nodokareplays')
        elif kirinlust20 == True:
            imagebutton:
                idle "subscribestar/images2/kirinnodokarep1.png"
                hover "subscribestar/images2/kirinnodokarep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('nodokareplays')
        elif nodokaspecial15p1 == True:
            imagebutton:
                idle "subscribestar/images2/nodokashowerrep1.png"
                hover "subscribestar/images2/nodokashowerrep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('nodokareplays')
        else:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')

        if nodokanudecheck >= 1:
            imagebutton:
                idle "phonenotif.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('nodokaphone')
        else:
            imagebutton:
                idle "phoneblank.png"
                hover "phonehover.png"
                xalign 0.925 yalign 0.500
                action ShowMenu('nodokaphone')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(nodoka_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen nodokatracker():

    tag menu

    use game_menu(_("Nodoka Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=AF89A2}Nodoka Nagasawa ([nodoka_love] Affection){/color}"
            if nodokafirsthall == True:
                if bonus == True:
                    textbutton _("Humbert Humbert {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("nodokafirsthall", locked=False)
                else:
                    textbutton _("Clifford the Big Red Dog {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("nodokafirsthall", locked=False)
            elif bonus == True:
                text _("Humbert Humbert")
            else:
                text _("Clifford the Big Red Dog")
            if nodokadorm1 == True:
                textbutton _("The Man Who Would Be King {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokadorm1", locked=False)
            else:
                text _("The Man Who Would Be King")
            if nodokalibrary1 == True:
                textbutton _("Cracks in the Armor {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokalibrary1", locked=False)
            else:
                text _("Cracks in the Armor")
            if nodokalibrary5 == True:
                textbutton _("Coloring Book {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokalibrary5", locked=False)
            else:
                text _("Coloring Book")
            if nodokadorm5 == True:
                textbutton _("I See Everything {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokadorm5", locked=False)
            else:
                text _("I See Everything")
            text _("-----------------------------------------------------------")
            if nodokadorm15 == True:
                textbutton _("Beyond the Reach of God {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokadorm15", locked=False)
            else:
                text _("Beyond the Reach of God")
            if nodokaspecial15p1 == True:
                textbutton _("So Far Below {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokaspecial15p1", locked=False)
            else:
                text _("So Far Below")
            if nodokaspecial15p2 == True:
                textbutton _("Matador {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokaspecial15p2", locked=False)
            else:
                text _("Matador")
            if nodokaspecial15p3 == True:
                textbutton _("Things That Hurt {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokaspecial15p3", locked=False)
            elif nodokaspecial15p3skip == True:
                text _("{color=EF1A1A}{s}Seeing Red{/s}{/color}")
            else:
                text _("Things That Hurt")
            if nodokaspecial20 == True:
                textbutton _("Twisting Ivy {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokaspecial20", locked=False)
            else:
                text _("Twisting Ivy")
            if nodokaspecial30p1 == True:
                textbutton _("Amoeba (Incontrovertible Peculiarity) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokaspecial30p1", locked=False)
            else:
                text _("Amoeba (Incontrovertible Peculiarity)")
            if nodokaspecial30p2 == True:
                textbutton _("This is Us {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokaspecial30p2", locked=False)
            else:
                text _("This is Us")
            if nodokaspecial30p3 == True:
                textbutton _("Taco Attack {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokaspecial30p3", locked=False)
            else:
                text _("Taco Attack")
            if nodokaspecial30p4 == True:
                textbutton _("Lavender {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokaspecial30p4", locked=False)
            else:
                text _("Lavender")
            text _("-----------------------------------------------------------")
            if sportswars17 == True:
                textbutton _("Meet & Fuck {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("sportswars17", locked=False)
            else:
                text _("Meet & Fuck")
            if beachfive6 == True:
                textbutton _("The Silver King {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive6", locked=False)
            else:
                text _("The Silver King")
            if beachfive10 == True:
                textbutton _("Mille Crepe {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachfive10", locked=False)
            else:
                text _("Mille Crepe")
            if halloweennodoka1 == True:
                textbutton _("When the Well Runs Dry {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweennodoka1", locked=False)
            else:
                text _("When the Well Runs Dry")
            if nodokainvite1 == True:
                textbutton _("Perfect Hair Forever {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokainvite1", locked=False)
            else:
                text _("{color=778EFF}Perfect Hair Forever{/color}")
            if nodokainvite2 == True:
                textbutton _("Number One Fan {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokainvite2", locked=False)
            else:
                text _("{color=778EFF}Number One Fan{/color}")
            if nodokainvite3 == True:
                textbutton _("How to Fuck Your Father {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("nodokainvite3", locked=False)
            elif nodokainvite3miss == True:
                text _("{color=EF1A1A}{s}How to Cuck Your Daughter{/s}{/color}")
            else:
                text _("{color=778EFF}How to Fuck Your Father{/color}")
            textbutton _("Back") action ShowMenu('gamemenunodoka')

screen gamemenuotoha():

    tag menu
    if otohamenuoutfit is not None and renpy.loadable(otohamenuoutfit) :
        add otohamenuoutfit
    else :
        add "game_menuotoha.png"

    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#B83A6A}Height: 5'7/169cm{/color}") style "profile"
        text ("{color=#B83A6A}Birthday: September 19th{/color}") style "profile"
        text ("\n{color=#B83A6A}Affection: [otoha_love]{/color}") style "profile"
        text ("{color=#B83A6A}Lust: N/A{/color}") style "profile"
        text ("{color=#B83A6A}Headpats: 0{/color}") style "profile"
        text ("{color=#B83A6A}Events: [otohapoint]/18{/color}") style "profile"

    imagebutton:
        idle "otohaevrep1.png"
        hover "otohaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('otohatracker')

    if postnodokachain1 == False:
        imagebutton:
            idle "lock.png"
            hover "lock.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            #action ShowMenu('amireplays')
    else:
        imagebutton:
            idle "subscribestar/images2/rinotoharep1.png"
            hover "subscribestar/images2/rinotoharep2.png"
            xalign 0.925 yalign 0.935
            focus_mask True
            action ShowMenu('otohareplays')

    if otohanudecheck >= 1:
        imagebutton:
            idle "phonenotif.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('otohaphone')
    else:
        imagebutton:
            idle "phoneblank.png"
            hover "phonehover.png"
            xalign 0.925 yalign 0.500
            action ShowMenu('otohaphone')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(otoha_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen otohatracker():

    tag menu

    use game_menu(_("Otoha Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=B83A6A}Otoha Okakura ([otoha_love] Affection){/color}"
            if otohafirsthall == True:
                textbutton _("Everybody Loves Otoha {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohafirsthall", locked=False)
            else:
                text _("Everybody Loves Otoha")
            if otohadorm1 == True:
                textbutton _("Conversations Outside of a Girls’ Dorm {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohadorm1", locked=False)
            else:
                text _("Conversations Outside of a Girls’ Dorm")
            if otohapark1 == True:
                textbutton _("Japanese Summer (Double Suicide) {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohapark1", locked=False)
            else:
                text _("Japanese Summer (Double Suicide)")
            if otohapark5 == True:
                textbutton _("Locked In {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohapark5", locked=False)
            else:
                text _("Locked In")
            if otohadorm5 == True:
                if bonus == True:
                    textbutton _("Highly Pornographic {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("otohadorm5", locked=False)
                else:
                    textbutton _("Just a Greasy Spoon {b}✓{/b}"):
                        text_style "mybutton"
                        action Replay("otohadorm5", locked=False)
            elif bonus == True:
                text _("Highly Pornographic")
            else:
                text _("Just a Greasy Spoon")
            if otohapark10 == True:
                textbutton _("Pull the Plug {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohapark10", locked=False)
            else:
                text _("Pull the Plug")
            if otohaspecial10 == True:
                textbutton _("Two-Octave Pitch Glide {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohaspecial10", locked=False)
            else:
                text _("Two-Octave Pitch Glide")
            if otohadorm10 == True:
                textbutton _("Breathing in Unison {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohadorm10", locked=False)
            else:
                text _("Breathing in Unison")
            if otohadorm10p2 == True:
                textbutton _("Vanilla Bean {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohadorm10p2", locked=False)
            else:
                text _("Vanilla Bean")
            text _("-----------------------------------------------------------")
            if otohaspecial15p1 == True:
                textbutton _("King Midas {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohaspecial15p1", locked=False)
            else:
                text _("King Midas")
            if otohaspecial15p2 == True:
                textbutton _("White People {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohaspecial15p2", locked=False)
            else:
                text _("White People")
            if otohadate20 == True:
                textbutton _("Breaking Character {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohadate20", locked=False)
            else:
                text _("Breaking Character")
            text _("-----------------------------------------------------------")
            if otohaspring1 == True:
                textbutton _("This Curse Called Youth {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohaspring1", locked=False)
            else:
                text _("This Curse Called Youth")
            if otohaspring2 == True:
                textbutton _("Taint the Sapling {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohaspring2", locked=False)
            else:
                text _("Taint the Sapling")
            if otohaspring3 == True:
                textbutton _("Something Wonderful {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohaspring3", locked=False)
            else:
                text _("Something Wonderful")
            if christmasotoha1 == True:
                textbutton _("Sisterly Love {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("christmasotoha1", locked=False)
            else:
                text _("Sisterly Love")
            if otohaspring4 == True:
                textbutton _("Becoming Closer to Closure {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("otohaspring4", locked=False)
            else:
                text _("Becoming Closer to Closure")
            if beachsixotoha1 == True:
                textbutton _("Something in the Water {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("beachsixotoha1", locked=False)
            else:
                text _("Something in the Water")
            textbutton _("Back") action ShowMenu('gamemenuotoha')

screen gamemenutouka():

    tag menu
    if toukamenuoutfit is not None and renpy.loadable(toukamenuoutfit) :
        add toukamenuoutfit
    else :
        add "game_menutouka.png"

    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#F0E68C}Height: 5'6/167cm{/color}") style "profile"
        text ("{color=#F0E68C}Birthday: February 9th{/color}") style "profile"
        text ("\n{color=#F0E68C}Affection: [touka_love]{/color}") style "profile"
        text ("{color=#F0E68C}Lust: N/A{/color}") style "profile"
        text ("{color=#F0E68C}Headpats: 0{/color}") style "profile"
        text ("{color=#F0E68C}Events: [toukapoint]/19{/color}") style "profile"

    imagebutton:
        idle "toukaevrep1.png"
        hover "toukaevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('toukatracker')

    if bonus == True:
        if chikalust15 == True:
            imagebutton:
                idle "subscribestar/images2/chikatoukastriprep1.png"
                hover "subscribestar/images2/chikatoukastriprep2.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                action ShowMenu('toukareplays')
        else:
            imagebutton:
                idle "lock.png"
                hover "lock.png"
                xalign 0.925 yalign 0.935
                focus_mask True
                #action ShowMenu('amireplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(touka_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen toukatracker():

    tag menu

    use game_menu(_("Touka Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=F0E68C}Touka Tsukioka ([touka_love] Affection){/color}"
            if toukafirsthall == True:
                textbutton _("Spontaneous Sentimentality {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukafirsthall", locked=False)
            else:
                text _("Spontaneous Sentimentality")
            if toukastreets1 == True:
                textbutton _("Trial Period {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukastreets1", locked=False)
            else:
                text _("Trial Period")
            if toukadorm1 == True:
                textbutton _("Fish Out of Water {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukadorm1", locked=False)
            else:
                text _("Fish Out of Water")
            if toukastreets5 == True:
                textbutton _("A Brief Moment in Time {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukastreets5", locked=False)
            else:
                text _("A Brief Moment in Time")
            if toukadorm5 == True:
                textbutton _("Loser {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukadorm5", locked=False)
            else:
                text _("Loser")
            if toukadorm10 == True:
                textbutton _("House Call {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukadorm10", locked=False)
            else:
                text _("House Call")
            if toukaspecial15 == True:
                textbutton _("A Commoner's Tour of Summer {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaspecial15", locked=False)
            else:
                text _("A Commoner's Tour of Summer")
            if toukaspecial15p2 == True:
                textbutton _("Red-ish Light District {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaspecial15p2", locked=False)
            else:
                text _("Red-ish Light District")
            if toukaspecial15p3 == True:
                textbutton _("Something Less Lonely {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaspecial15p3", locked=False)
            else:
                text _("Something Less Lonely")
            text _("-----------------------------------------------------------")
            if toukaarchery20 == True:
                textbutton _("Kryptonite {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaarchery20", locked=False)
            else:
                text _("Kryptonite")
            if toukadorm25p1 == True:
                textbutton _("For Want Of {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukadorm25p1", locked=False)
            else:
                text _("For Want Of")
            if toukadorm25p2 == True:
                textbutton _("To Lift This Aching Head {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukadorm25p2", locked=False)
            else:
                text _("To Lift This Aching Head")
            if toukadorm25p3 == True:
                textbutton _("Under My Wing {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukadorm25p3", locked=False)
            else:
                text _("Under My Wing")
            text _("-----------------------------------------------------------")
            if toukacamp1 == True:
                textbutton _("Salt in the Wound {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukacamp1", locked=False)
            else:
                text _("Salt in the Wound")
            if toukaspring1 == True:
                textbutton _("Blankets & Ball-Gags {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaspring1", locked=False)
            else:
                text _("Blankets & Ball-Gags")
            if toukaspring2 == True:
                textbutton _("Artisan Hands {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaspring2", locked=False)
            else:
                text _("Artisan Hands")
            if toukaspring3 == True:
                textbutton _("One Thousand Penises {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaspring3", locked=False)
            else:
                text _("One Thousand Penises")
            if toukaspring4 == True:
                textbutton _("Come For Me {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaspring4", locked=False)
            else:
                text _("Come For Me")
            if toukaspring5 == True:
                textbutton _("One of the Girls {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("toukaspring5", locked=False)
            else:
                text _("One of the Girls")
            textbutton _("Back") action ShowMenu('gamemenutouka')

screen gamemenuyasu():

    tag menu
    if yasumenuoutfit is not None and renpy.loadable(yasumenuoutfit) :
        add yasumenuoutfit
    else :
        add "game_menuyasu.png"

    use navigation

    vbox:
        xalign .85
        yalign .38

        text ("{color=#74d9e9}Height: 5'3/159cm{/color}") style "profile"
        text ("{color=#74d9e9}Birthday: April 4th{/color}") style "profile"
        text ("\n{color=#74d9e9}Affection: [yasu_love]{/color}") style "profile"
        text ("{color=#74d9e9}Lust: N/A{/color}") style "profile"
        text ("{color=#74d9e9}Headpats: 0{/color}") style "profile"
        text ("{color=#74d9e9}Events: [yasupoint]/19{/color}") style "profile"

    imagebutton:
        idle "yasuevrep1.png"
        hover "yasuevrep2.png"
        xalign 0.625 yalign 0.935
        focus_mask True
        action ShowMenu('yasutracker')

    imagebutton:
        idle "lock.png"
        hover "lock.png"
        xalign 0.925 yalign 0.935
        focus_mask True
        #action ShowMenu('amireplays')

    textbutton _("{size=+8}Change Profile Outfit{/size}"):
        action Function(yasu_next_outfit)
        xalign 0.28 yalign 0

    textbutton _("{size=+4}Go Back{/size}"):
        action ShowMenu('eventtrackermaincharahub')
        xalign 0.242 yalign 0.065

    textbutton _("Return"):
        style "return_button"

        action Return()

screen yasutracker():

    tag menu

    use game_menu(_("Yasu Events"), scroll="viewport"):

        style_prefix "event"

        vbox:

            label "{color=74d9e9}Yasu Yasui ([yasu_love] Affection){/color}"
            if yasufirsthall == True:
                textbutton _("The Hole That Swallowed Everything {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasufirsthall", locked=False)
            else:
                text _("The Hole That Swallowed Everything")
            if church1 == True:
                textbutton _("Transference {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("church1", locked=False)
            else:
                text _("Transference")
            if church5 == True:
                textbutton _("Armor of Older Gods {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("church5", locked=False)
            else:
                text _("Armor of Older Gods")
            if yasudorm10 == True:
                textbutton _("Repentance {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasudorm10", locked=False)
            else:
                text _("Repentance")
            if church10 == True:
                textbutton _("Sakura Season {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("church10", locked=False)
            else:
                text _("Sakura Season")
            text _("-----------------------------------------------------------")
            if church15 == True:
                textbutton _("Down The Rabbit Hole {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("church15", locked=False)
            else:
                text _("Down The Rabbit Hole")
            if yasuspecial15 == True:
                textbutton _("Sore Thumb {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasuspecial15", locked=False)
            else:
                text _("Sore Thumb")
            if church20 == True:
                textbutton _("Mother Duck {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("church20", locked=False)
            else:
                text _("Mother Duck")
            if yasudorm20 == True:
                textbutton _("Glossolalia {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasudorm20", locked=False)
            else:
                text _("Glossolalia")
            if yasuspecial20 == True:
                textbutton _("The River Styx {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasuspecial20", locked=False)
            else:
                text _("The River Styx")
            if church25 == True:
                textbutton _("Frankincense & Myrrh {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("church25", locked=False)
            else:
                text _("Frankincense & Myrrh")
            if yasudorm25 == True:
                textbutton _("Hand of God {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasudorm25", locked=False)
            else:
                text _("Hand of God")
            if yasudorm30 == True:
                textbutton _("An Apple Each Day {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasudorm30", locked=False)
            else:
                text _("An Apple Each Day")
            text _("-----------------------------------------------------------")
            if yasuspring1 == True:
                textbutton _("Throne of Flesh {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasuspring1", locked=False)
            else:
                text _("Throne of Flesh")
            if yasuspring2 == True:
                textbutton _("Fruits of Torment {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasuspring2", locked=False)
            else:
                text _("Fruits of Torment")
            if yasuspring3 == True:
                textbutton _("The Art of Drowning {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasuspring3", locked=False)
            else:
                text _("The Art of Drowning")
            if halloweenyasu1 == True:
                textbutton _("Infinity House {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("halloweenyasu1", locked=False)
            else:
                text _("Infinity House")
            if yasuspring4 == True:
                textbutton _("False Chameleon {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasuspring4", locked=False)
            else:
                text _("False Chameleon")
            if yasuspring5 == True:
                textbutton _("Etinsib Ziwa & The Book of Colors {b}✓{/b}"):
                    text_style "mybutton"
                    action Replay("yasuspring5", locked=False)
            else:
                text _("Etinsib Ziwa & The Book of Colors")
            textbutton _("Back") action ShowMenu('gamemenuyasu')
