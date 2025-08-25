label chapter1_start:
    e "You stand at a crossroads."
    # This is a critical choice.
    menu:
        "Go left":
            e "You chose the path of thorns."
            $ thorns_path = True
        "Go right":
            e "You chose the path of flowers."
            # A good choice.
            $ flowers_path = True
    
    e "Your journey continues."