style clear_frame:
    background None
    padding (0,0)
    margin (0,0)

style phone_button_bar_button is button:
    ysize 72 
    idle_background "#fff0"
    hover_background "#fff1"

style phone_frame is frame:
    background Frame("images/Phone/phone.png", 35, 200, 35, 300)
    xsize 660
    ysize 1150
    xalign 0.5 
    yalign 1.0
    yanchor 0.95 # Phone is slightly off-screen at the bottom

style phone_screen_vbox is vbox:
    pos (29, 135)
    xsize 590
    ysize 790

style phone_screen_light_vbox is phone_screen_vbox:
    background "#fff"

style phone_screen_dark_vbox is phone_screen_vbox:
    background "#222"

style phone_home_screen_frame:
    background "Phone/wallpaper.png"
    xfill True
    yfill True
    padding (0,0)

style phone_home_screen_text is text:
    xalign 0.5
    color "#fff"
    size 20

# Phone header common style
style phone_header_frame:
    xfill True
    yfill False

# Phone header in light mode
style phone_header_light_frame is phone_header_frame:
    background gui.accent_color

# Phone header in dark mode
style phone_header_dark_frame is phone_header_frame:
    background "#111"

# Phone header text common style
style phone_header_text:
    size 48
    adjust_spacing False
    font "Roboto-Regular.ttf"

# Phone header text in light mode
style phone_header_light_text is phone_header_text:
    color "#fff"

# Phone header text in light mode
style phone_header_dark_text is phone_header_text:
    color gui.accent_color

style phone_contacts_list_light_frame:
    background "#fff"

style phone_contacts_list_dark_frame:
    background "#222"

# Phone contacts list style for each contact button in light mode (button contains the picture + name of girl)
style phone_contacts_list_light_button:
    background "#0000"
    hover_background "#0001"

# Phone contacts list style for each contact button in dark mode (button contains the picture + name of girl)
style phone_contacts_list_dark_button:
    background "#0000"
    hover_background "#fff1"

# Phone contacts list text 
style phone_contacts_list_text is text:
    adjust_spacing False
    font "Roboto-Regular.ttf"
    size 36
    yalign 0.5

# Phone contacts list text 
style phone_contacts_list_light_text is phone_contacts_list_text:
    color "#555f61"

# Phone contacts list text 
style phone_contacts_list_dark_text is phone_contacts_list_text:
    color "#cecece"

style phone_contact_page_header_light_frame:
    background "#fff"

style phone_contact_page_header_dark_frame:
    background "#222"

# Phone contact page, name of girl text style
style phone_contact_page_name_text is text:
    size 36
    adjust_spacing False
    font "Roboto-Regular.ttf"

style phone_contact_page_name_light_text is phone_contact_page_name_text:
    color "#555f61"

style phone_contact_page_name_dark_text is phone_contact_page_name_text:
    color "#cecece"

# Phone contact page, stats of girl text style (affection/lust)
style phone_contact_page_stats_text is text:
    size 20
    adjust_spacing False
    font "Roboto-Regular.ttf"

style phone_contact_page_stats_light_text is phone_contact_page_stats_text:
    color "#707c80"

style phone_contact_page_stats_dark_text is phone_contact_page_stats_text:
    color "#cecece"

style phone_contact_page_content_frame:
    xfill True
    yfill True
    padding (20, 20)

style phone_contact_page_content_light_frame is phone_contact_page_content_frame:
    background "#fff"

style phone_contact_page_content_dark_frame is phone_contact_page_content_frame:
    background "#222"

style phone_message_header_frame:
    padding (10, 10)
    background gui.accent_color
    xfill True
    yfill False

style phone_message_header_text is text:
    size 40
    adjust_spacing False
    font "Roboto-Regular.ttf"
    yalign 0.5
    color "#fffc"

style phone_message_frame:
    padding (12, 8)
    margin (10, 10, 10, 5)
    xfill False
    yfill False
    xmaximum 480

style phone_message_girl_frame is phone_message_frame:
    background gui.accent_color
    xalign 0.0

style phone_message_sensei_frame is phone_message_frame:
    background "#cecece"
    xalign 1.0

style phone_message_girl_text is text:
    color "#fffc"
    size 24
    adjust_spacing False
    font "Roboto-Regular.ttf"

style phone_message_sensei_text is text:
    color "#000c"
    size 24
    adjust_spacing False
    font "Roboto-Regular.ttf"