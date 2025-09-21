# Game Start
label start:
    $ health = 100
    e "Welcome to the game."
    $ health -= 10 # take some damage
    if health < 95:
        e "You are injured!"
