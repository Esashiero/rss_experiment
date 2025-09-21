screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
            textbutton _("Load") action ShowMenu("load")
        else:
            if not renpy.variant("mobile"):
                textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Event Tracker") action ShowMenu('eventtracker11')
            textbutton _("Main Girls") action ShowMenu('eventtrackermaincharahub')
            textbutton _("Side Girls") action ShowMenu('eventtrackersidecharahub')
            if dark_mode: 
                textbutton _("Progress") action ShowMenu("progressmod_dark")
            else:
                textbutton _("Progress") action ShowMenu("progressmod")
            if show_hints:
                textbutton _("Hints") action ShowMenu('hinttracker')
            else:
                if not renpy.variant("mobile") and bonus == True:
                    textbutton _("Guide/Wiki") action OpenURL("https://lessonsinlove.wiki/")
        textbutton _("Settings") action ShowMenu("preferences")
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()
        if main_menu:
            textbutton _("About") action ShowMenu("about")
        textbutton _("Feed Chinami") action OpenURL("https://subscribestar.adult/selebus")
        textbutton _("Merch Store") action OpenURL("https://selebus-inc.myshopify.com/")
        if main_menu:
            textbutton _("Jukebox") action ShowMenu("music_room")
        textbutton _("Quit") action Quit(confirm=not main_menu)
    if show_dlc:
        textbutton _("{size=+20}{b}DLC"):
            action ShowMenu("dlc")
            xpos 266 ypos 564

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
            textbutton _("Girls") action ShowMenu('amitrackerm2')
            if dark_mode:
                textbutton _("Progress") action ShowMenu('progressmod_dark')
            else:
                textbutton _("Progress") action ShowMenu('progressmod')
            if show_hints:
                textbutton _("Hints") action ShowMenu('hinttracker')
            textbutton _("Unlockables") action ShowMenu('unlockables')
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

# screen file_slots(title):

#     default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

#     use game_menu(title):

#         fixed:

#             ## This ensures the input will get the enter event before any of the
#             ## buttons do.
#             order_reverse True

#             ## The page name, which can be edited by clicking on a button.
#             button:
#                 style "page_label"

#                 key_events True
#                 xalign 0.5
#                 action page_name_value.Toggle()

#                 input:
#                     style "page_label_text"
#                     value page_name_value

#             ## The grid of file slots.
#             grid gui.file_slot_cols gui.file_slot_rows:
#                 style_prefix "slot"

#                 xalign 0.5
#                 yalign 0.5

#                 spacing gui.slot_spacing

#                 for i in range(gui.file_slot_cols * gui.file_slot_rows):

#                     $ slot = i + 1

#                     button:
#                         action SetVariable("save_name", FileSaveName(slot)), FileAction(slot)

#                         #VIPER
#                         if title == "Save":
#                             alternate Show("save_rename", slot=slot)
#                         #VIPER

#                         has vbox

#                         add FileScreenshot(slot) xalign 0.5

#                         text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
#                             style "slot_time_text"
#                         $ playtime = FileJson(slot, "playtime", empty=0, missing=0)
#                         $ pt_minutes, pt_seconds = divmod(int(playtime), 60)
#                         $ pt_hours, pt_minutes = divmod(pt_minutes, 60)
#                         $ pt_minutes = str(pt_minutes)
#                         $ if len(pt_minutes) == 1: pt_minutes = "0" + pt_minutes
#                         text "[pt_hours]:[pt_minutes]" style "slot_time_text"

#                         text FileSaveName(slot):
#                             style "slot_name_text"

#                         key "save_delete" action FileDelete(slot)

#             #VIPER
#             hbox:
#                 xalign 0.5
#                 yalign 0.9
#                 if title == "Save":
#                     text "Right click a save slot to OVERWRITE IT with a new name" style "gui_text"
#             #VIPER

#             ## Buttons to access other pages.
#             hbox:
#                 style_prefix "page"

#                 xalign 0.5
#                 yalign 1.0

#                 spacing gui.page_spacing

#                 textbutton _("<") action FilePagePrevious()

#                 if config.has_autosave:
#                     textbutton _("{#auto_page}A") action FilePage("auto")

#                 if config.has_quicksave:
#                     textbutton _("{#quick_page}Q") action FilePage("quick")

#                 ## range(1, 10) gives the numbers from 1 to 9.
#                 for page in range(1, 10):
#                     textbutton "[page]" action FilePage(page)

#                 textbutton _(">") action FilePageNext()