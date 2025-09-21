label chapter2_logic:
    $ score = 85
    e "You approach the gatekeeper."
    menu:
        "Bribe the guard":
            if score > 90:
                e "The guard is insulted!"
                $ score -= 10
            else:
                e "The guard accepts the bribe."
                $ bribed_guard = True
        "Persuade the guard":
            e "You make your case."
    e "You are past the gate."