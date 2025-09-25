init -1 python:

    import time

    installed_care_packages = list()
    installed_menu_images = list()

    class CarePackage:

        def __init__(self, name, label):
            self.name = name
            self.label = label

    class BackgroundImage:
        def __init__(self, name, file):
            self.name = name
            self.file = file

    def care_package_choices():
        choices = list()

        for package in installed_care_packages:
            choices.append((package.name, (package.label,)))

        choices.sort(key= lambda choice : time.strptime("01 " + choice[0] + " UTC", "%d %B %Y %Z"))

        choices.append(("Go Back", (None,)))

        return choices

    def main_menu_choices():
        choices = list()

        for image in installed_menu_images:
            choices.append((image.name, (image.file,)))

        choices.append(("Default", (None,)))

        return choices

    def has_care_package(name) :
        for package in installed_care_packages :
            if package.name == name :
                return True

        return False


#label care_package_menu:
#    python:
#        open_package = renpy.display_menu(care_package_choices())[0]
#        if open_package is not None :
#            renpy.jump(open_package)
#    return

label care_package_menu:
    $ renpy.dynamic("open_package")
    $ open_package = renpy.display_menu(care_package_choices())[0]

    if open_package is not None:
        call expression open_package from care_package_menu_call
        jump care_package_menu
    else:
        jump computermenu

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
