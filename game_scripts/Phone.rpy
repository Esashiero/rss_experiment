init 1 python:
    class Contact: # Stores the data of a phone contact (i.e. one of the girls)
        def __init__(self, tag, firstName, lastName, customName, color, love, lust, haveNumber, canInviteOver):
            self.tag = tag # This is the prefix used to fetch images and jump to labels; naming consistency is important!
            self.firstName = firstName
            self.lastName = lastName
            self.customName = customName
            self.color = color # Their name color
            self.love = love
            self.lust = lust
            self.haveNumber = haveNumber # Whether Sensei has acquired their phone number
            self.canInviteOver = canInviteOver # Whether Sensei can invite them over

    # Initialize the custom contact names
    ami_custom_name = ""
    ayane_custom_name = ""
    chika_custom_name = ""
    chinami_custom_name = ""
    futaba_custom_name = ""
    haruka_custom_name = ""
    imani_custom_name = ""
    io_custom_name = ""
    kaori_custom_name = ""
    karin_custom_name = ""
    kirin_custom_name = ""
    maki_custom_name = ""
    makoto_custom_name = ""
    maya_custom_name = ""
    miku_custom_name = ""
    molly_custom_name = ""
    niki_custom_name = ""
    nodoka_custom_name = ""
    noriko_custom_name = ""
    osako_custom_name = ""
    otoha_custom_name = ""
    rin_custom_name = ""
    rika_custom_name = ""
    sana_custom_name = ""
    sara_custom_name = ""
    touka_custom_name = ""
    tsubasa_custom_name = ""
    tsukasa_custom_name = ""
    tsuneyo_custom_name = ""
    uta_custom_name = ""
    wakana_custom_name = ""
    yuki_custom_name = ""
    yumi_custom_name = ""

    # Returns an up-to-date list of contacts sorted alphabetically
    # Refer to the Contact object abbove for the format
    def getContacts(timeofday=None):
        contactsList = [
            Contact("happy_trinity3", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "", "", Color("#f800ff"), 23, 23, trinity2track and trinity3 and day>=6 and timeofday=="night", False), # Special case for Trinity 3 happy event
            Contact("ami", "Ami", "Arakawa", ami_custom_name, Color("#ff4dd2"), ami_love, ami_lust,  True, christmas7),
            Contact("ayane", "Ayane", "Amamiya", ayane_custom_name, Color("#00bab1"), ayane_love, ayane_lust,  True, christmas7),
            Contact("chika", "Chika", "Chosokabe", chika_custom_name, Color("#AF7F00"), chika_love, chika_lust,  chikanumber, day139 and chikanumber),
            Contact("chinami", "Chinami", "Chosokabe", chinami_custom_name, Color("#FF9999"), chinami_love, -1,  chinaminumber, False),
            Contact("futaba", "Futaba", "Fukuyama", futaba_custom_name, Color("#9326ff"), futaba_love, futaba_lust,  futabanumber, christmas7),
            Contact("haruka", "Haruka", "Hamasaki", haruka_custom_name, Color("#B02E8C"), haruka_love, haruka_lust,  harukanumber, christmas7),
            Contact("imani", "Imani", "Imai", imani_custom_name, Color("#80C9DC"), imani_love, imani_lust, imaninumber, False),
            Contact("io", "Io", "Ichimonji", io_custom_name, Color("#BBE3A1"), io_love, -1,  ionumber, False),
            Contact("kaori", "Kaori", "Kadowaki", kaori_custom_name, Color("#4B4B4B"), kaori_love, -1,  kaorinumber, False),
            Contact("karin", "Karin", "Kanda", karin_custom_name, Color("#AC9D77"), karin_love, -1,  karinnumber, False),
            Contact("kirin", "Kirin", "Kanda", kirin_custom_name, Color("#9C8080"), kirin_love, kirin_lust,  kirinnumber, christmas7),
            Contact("maki", "Maki", "Miyamura", maki_custom_name, Color("#3B84A9"), maki_love, maki_lust,  makinumber, halloweentwo13),
            Contact("makoto", "Makoto", "Miyamura", makoto_custom_name, Color("#3c55fa"), makoto_love, makoto_lust,  makotonumber, makotolust5 and day77),
            Contact("maya", "Maya", "Makinami", maya_custom_name, Color("#18b500"), maya_love, -1, mayanumber, False),
            Contact("happy_totl", "{s}Maya{/s}", "{s}Makinami{/s}", "", Color("#18b500"), 23, 23,  specialclassroom and day>=6 and timeofday=="night", False), # Special case for Turn Off the Light (abbbreviated totl) happy event
            Contact("miku", "Miku", "Maruyama", miku_custom_name, Color("#ff8112"), miku_love, miku_lust,  mikunumber, slumberreset5),
            Contact("molly", "Molly", "MacCormack", molly_custom_name, Color("#4FCB80"), molly_love, molly_lust,  mollynumber, christmasfive8),
            Contact("niki", "Niki", "Nakayama", niki_custom_name, Color("#FF0074"), niki_love, niki_lust,  nikinumber, norikodorm25),
            Contact("nodoka", "Nodoka", "Nagasawa", nodoka_custom_name, Color("#AF89A2"), nodoka_love, nodoka_lust,  nodokalibrary1, christmasfive8),
            Contact("noriko", "Noriko", "Nakayama", noriko_custom_name, Color("#FF61A9"), noriko_love, noriko_lust,  norikonumber, norikodorm10),
            Contact("osako", "Osako", "Osaka", osako_custom_name, Color("#9A6BA1"), osako_love, -1, osakonumber, False),
            Contact("otoha", "Otoha", "Okakura", otoha_custom_name, Color("#B83A6A"), otoha_love, -1,  otohanumber, False),
            Contact("rika", "Rika", "Rokuhara", rika_custom_name, Color("#D18E77"), rika_love, -1,  rikanumber, False),
            Contact("rin", "Rin", "Rokuhara", rin_custom_name, Color("#a30041"), rin_love, -1,  rinnumber, False),
            Contact("sana", "Sana", "Sakakibara", sana_custom_name, Color("#005730"), sana_love, sana_lust,  sananumber, christmasfive8),
            Contact("sara", "Sara", "Sakakibara", sara_custom_name, Color("#365D4C"), sara_love, sara_lust,  saranumber, saradate1),
            Contact("touka", "Touka", "Tsukioka", touka_custom_name, Color("#F0E68C"), touka_love, -1,  toukanumber, False),
            Contact("tsubasa", "Tsubasa", "Tsukioka", tsubasa_custom_name, Color("#eae6aa"), tsubasa_love, -1,  tsubasanumber, False),
            Contact("tsukasa", "Tsukasa", "Tsukioka", tsukasa_custom_name, Color("#f0ca8c"), tsukasa_love, -1,  tsukasanumber, False),
            Contact("tsuneyo", "Tsuneyo", "Tojo", tsuneyo_custom_name, Color("#C8B330"), tsuneyo_love, -1,  tsuneyonumber, False),
            Contact("uta", "Uta", "Ushibori", uta_custom_name, Color("#AA4588"), uta_love, -1,  utanumber, False),
            Contact("wakana", "Wakana", "Watabe", wakana_custom_name, Color("#540087"), wakana_love, -1,  wakananumber, False),
            Contact("yuki", "Yuki", "Yamaguchi", yuki_custom_name, Color("#CDCDCD"), yuki_love, -1,  yukinumber, False),
            Contact("yumi", "Yumi", "Yamaguchi", yumi_custom_name, Color("#d12e2e"), yumi_love, -1,  yuminumber, False)
        ]

        updateContactsDictionary(contactsList)

        return contactsList

    contactsDictionary = {}

    def updateContactsDictionary(contactsList):
        contactsDictionary.clear()
        for c in contactsList:
            contactsDictionary[c.tag] = c

    def getContactByTag(contactTag):
        return contactsDictionary[contactTag]

    # Clears the call stack that allows the phone to navigate through menus and jumps to the given label
    # Not the most elegant way but this should also fix ongoing saves with a bloated call stack
    def clearCallStackAndJump(labelName):
        stackSize = renpy.call_stack_depth()
        for x in range(stackSize):
            renpy.pop_call()
        renpy.jump(labelName)

    # Call once to make sure we have the list and dictionary in memory
    getContacts()

# ALWAYS CALL THIS LABEL TO JUMP OUT OF THE PHONE MENU
# Example: call exit_phone_and_jump("mylabel")
label exit_phone_and_jump(labelName):
    $ clearCallStackAndJump(labelName)

label phone_morning:
    call screen phone_contacts_menu("morning", True)

    while (True):
        call screen phone_contacts_menu("morning", False)

label phone_afternoon:
    call screen phone_contacts_menu("afternoon", True)

    while (True):
        call screen phone_contacts_menu("afternoon", False)

label phone_night:
    call screen phone_contacts_menu("night", True)

    while (True):
        call screen phone_contacts_menu("night", False)

# Animation that slides the phone up from the bottom of the screen (*SHINY*)
transform slide_up:
    subpixel True
    xalign .5 # Centers the phone
    yalign 1.0 yanchor 0.0 # Starts the phone *below* the screen
    easein 0.4 yanchor 0.95 # Animating anchor from 0 to 1, the phone appears

transform contact_full_pic:
    maxsize (190, 190)
    xalign 0.5 yalign 0.5

transform contact_medium_pic:
    maxsize (96, 96)
    xalign 0.5 yalign 0.5

transform contact_small_pic:
    maxsize (48, 48)
    xalign 0.5 yalign 0.5

# ==================================================================================================================================================================
# THIS IS CURRENTLY NOT USED
# ==================================================================================================================================================================
screen phone_home_screen(timeofday, animate):
    modal True # Blocks interactions with anything but the phone
    tag phone # Hides the other phone-related screens

    # Selects the phone theme based on time of day
    python:
        if timeofday == "night":
            phoneTheme = "dark"
        else:
            phoneTheme = "light"

    # Full phone frame
    frame:
        style "phone_frame"

        # Conditional animation to slide the phone up
        if animate:
            at slide_up
        else:
            xalign .5
            yalign 1.0
            yanchor 0.95

        # Phone screen section
        vbox:
            style "phone_screen_{}_vbox".format(phoneTheme)

            # Home screen
            frame style_prefix "phone_home_screen":
                frame:
                    background "#0006"
                    yalign 1.0
                    ysize 160

                grid 4 5:
                    xalign 0.5
                    yalign 0.5
                    xspacing 44
                    yspacing 40
                    for n in range(0,16):
                        null

                    vbox:
                        imagebutton idle "Phone/icon_phone.png" action Call("show_contacts_menu", timeofday)
                        text _("Phone")

                    vbox:
                        imagebutton idle "Phone/icon_messages.png"
                        text _("Messages")

                    vbox:
                        imagebutton idle "Phone/icon_photos.png"
                        text _("Photos")

                    vbox:
                        imagebutton idle "Phone/icon_settings.png"
                        text _("Settings")

            # Button bar
            grid 3 1:
                style_prefix "phone_button_bar"
                xfill True

                if day < 6:
                    button action Call("exit_phone_and_jump", "asmenu") # Returns to the after school menu
                    button action Call("exit_phone_and_jump", "asmenu") # Returns to the after school menu
                else:
                    button action Call("exit_phone_and_jump", "sat{}menu".format(timeofday)) # Returns to the weekend menu based on time of day
                    button action Call("exit_phone_and_jump", "sat{}menu".format(timeofday)) # Returns to the weekend menu based on time of day

                # Third button does nothing
                button
# ==================================================================================================================================================================

screen phone_contacts_menu(timeofday, animate):
    modal True # Blocks interactions with anything but the phone
    tag phone # Hides the other phone-related screens

    # Selects the phone theme based on time of day
    python:
        if timeofday == "night":
            phoneTheme = "dark"
        else:
            phoneTheme = "light"

    # Full phone frame
    frame:
        style "phone_frame"
        # Conditional animation to slide the phone up
        if animate:
            at slide_up
        else:
            xalign .5
            yalign 1.0
            yanchor 0.95

        # Phone screen section
        vbox:
            style "phone_screen_{}_vbox".format(phoneTheme)

            # Header section
            frame:
                style "phone_header_{}_frame".format(phoneTheme)
                style_prefix "phone_header_{}".format(phoneTheme)

                text _("Contacts")

            # Scrolling contacts section
            frame:
                style_prefix "phone_contacts_list_{}".format(phoneTheme)

                side ("c r"):
                    viewport id "contacts_scroller":
                        draggable True mousewheel True
                        vbox:

                            # The getContacts() function updates the contacts list to make sure we have up-to-date data
                            # For example, the player could've acquired a new number since the last call
                            # This is probably the most elegant way to do this without making significant changes to the rest of the code
                            # Ideally, the rest of the code would be refactored so that each girl's data is stored in a class rather than dozens of separate flags
                            # *HOWEVER* not sure if rollbacks and saves work properly with instanced classes?
                            for contact in getContacts(timeofday):
                                # Loop through list of contacts to create a button for each
                                if contact.haveNumber: # Only add girl to the UI if we have her number
                                    button:
                                        xfill True

                                        hbox:
                                            frame:
                                                style "clear_frame"
                                                xsize 96
                                                ysize 96

                                                # Uses the girl's tag to get the right image, e.g. "ami" --> ami.png, "happy_trinity3" --> happy_trinity3.png
                                                image AlphaMask(At("Phone/{}.png".format(contact.tag), contact_medium_pic), At("mask", contact_medium_pic)) xalign 0.5 yalign 0.5

                                            null width 20 # Spacer

                                            if contact.customName == "":
                                                text contact.firstName
                                            else:
                                                text contact.customName
                                            #text _("{} {}".format(contact.firstName, contact.lastName)) # Girl's name

                                        # When a contact button is clicked, plays a beep (remove if annoying?) and calls the contact page
                                        action [Play("sound", "phonebeep.wav"), Call("show_contact_page", contact.tag, timeofday)]


                    vbar value YScrollValue("contacts_scroller") xmaximum 50 # Chonky scrollbar for mobile; needs testing

            # Button bar
            grid 3 1:
                style_prefix "phone_button_bar"
                xfill True

                if chap4active:
                    button action Call("exit_phone_and_jump", "{}ch4".format(timeofday)) # Returns to the weekend menu based on time of day
                    button action Call("exit_phone_and_jump", "{}ch4".format(timeofday)) # Returns to the weekend menu based on time of day
                elif day < 6:
                    button action Call("exit_phone_and_jump", "asmenu") # Returns to the after school menu
                    button action Call("exit_phone_and_jump", "asmenu") # Returns to the after school menu
                else:
                    button action Call("exit_phone_and_jump", "sat{}menu".format(timeofday)) # Returns to the weekend menu based on time of day
                    button action Call("exit_phone_and_jump", "sat{}menu".format(timeofday)) # Returns to the weekend menu based on time of day

                # Third button does nothing
                button



# This label is used to open a contact page that is compatible with rollbacks
label show_contact_page(contactTag, timeofday):

    # Special case to trigger happy event as soon as you click the contact
    if contactTag == "happy_trinity3":
        call exit_phone_and_jump("trinity3") from _call_exit_phone_and_jump

    # First we need to get the right contact from the contacts list using the passed-in tag
    $ contact = getContactByTag(contactTag)

    # Show the contact page for that contact and pass in the time of day so it knows what event to trigger when you call the girl
    call screen contactpage(contact, timeofday)

    $ _return -= 1
    while (_return < 0):
        call screen contactpage(contact, timeofday)
        $ _return -= 1

    return _return

# The contact page screen that displays the girl's name, info and buttons to call, invite over, etc.
screen contactpage(contact, timeofday):
    modal True # Blocks interactions with anything but the phone
    tag phone # Hides the other phone-related screens

    python:
        # Selects the phone theme based on time of day
        if timeofday == "night":
            phoneTheme = "dark"
        else:
            phoneTheme = "light"

    # Full phone frame
    frame:
        style "phone_frame"

        # Phone screen section
        vbox:
            style "phone_screen_{}_vbox".format(phoneTheme)

            # Header section
            frame:
                style "phone_contact_page_header_{}_frame".format(phoneTheme)
                padding (10,10)
                xfill True

                vbox:
                    # Uses the girl's tag to get the right image, e.g. "ami" --> "Phone/ami.png"
                    fixed:
                        ymaximum 227
                        text _("●") size 226 color contact.color xalign 0.5
                        image AlphaMask(At("Phone/{}.png".format(contact.tag), contact_full_pic), At("mask", contact_full_pic)) xalign 0.5 yalign 0.5

                    if contact.customName == "":
                        text _(contact.firstName + " " + contact.lastName) xalign 0.5 style "phone_contact_page_name_{}_text".format(phoneTheme)
                    else:
                        text contact.customName xalign 0.5 style "phone_contact_page_name_{}_text".format(phoneTheme)

                    text _("Affection: {}".format(contact.love)) xalign 0.5 style "phone_contact_page_stats_{}_text".format(phoneTheme)

                    # Don't show lust if set to -1 (N/A)
                    if contact.lust >= 0:
                        text _("Lust: {}".format(contact.lust)) xalign 0.5 style "phone_contact_page_stats_{}_text".format(phoneTheme)

            # Content section
            frame:
                style "phone_contact_page_content_{}_frame".format(phoneTheme)

                # Special case for Turn Off The Light happy event replaces the usual 3 buttons with a single one
                if contact.tag == "happy_totl":
                    textbutton _("There is something buried underneath your feet") action Call("exit_phone_and_jump", "specialclassroom")
                else:
                    # Default contact page
                    grid 1 3:
                        xfill True

                        # When the Call button is clicked, jump to the appropriate label based on the tag of the girl and time of day
                        # !!! Relies on consistent label naming !!!
                        # Every girl in the list needs to have a label for morning, afternoon and night
                        # Example: Ami needs an existing label to jump to for callamimorning, callamiafternoon and callaminight
                        textbutton _("Call") action Call("exit_phone_and_jump", "call{}{}".format(contact.tag, timeofday))

                        # Only enable the Invite Over button if we've unlocked it for that contact AND it's night time
                        # When the Invite Over button is clicked, jump to the appropriate label based on the tag of the girl
                        # !!! Relies on consistent label naming !!!
                        # Example: Ami needs an existing label to jump to for amiinvite
                        if contact.canInviteOver and timeofday == "night" and senseisad == False:
                            textbutton _("Invite Over") action Call("exit_phone_and_jump", "{}invite".format(contact.tag))
                        else:
                            # Disabled button if invite overs aren't unlocked OR it's morning/afternoon
                            textbutton _("Invite Over")

                        textbutton _("Rename") action Call("rename_contact", contact)

            # Button bar
            grid 3 1:
                style_prefix "phone_button_bar"
                xfill True

                button action Return(1) # Returns to the contacts menu

                if chap4active:
                    button action Call("exit_phone_and_jump", "{}ch4".format(timeofday)) # Returns to the weekend menu based on time of day
                elif day < 6:
                    button action Call("exit_phone_and_jump", "asmenu") # Returns to the after school menu
                else:
                    button action Call("exit_phone_and_jump", "sat{}menu".format(timeofday)) # Returns to the weekend menu based on time of day

                # Third button does nothing
                button

label rename_contact(contact):
    $ newName = renpy.input("Enter a new nickname for [contact.firstName] (leave blank to restore default)", length=230).strip()
    $ contact.customName = newName
    $ globals()["{}_custom_name".format(contact.tag)] = newName
    return 0
