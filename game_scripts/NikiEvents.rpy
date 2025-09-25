label callnikimorning:
    if nikiblock == True:
        "I should probably give Niki some space for now..."
        jump callmorning
    if niki_love >= 0 and nikidate1 == False:
        jump nikidate1
    if niki_love >= 10 and secondbeach18 == True and nikidate10 == False:
        jump nikidate10
    if niki_love >= 20 and slumberreset5 == True and day == 6 and nikilovesyou3 == False:
        jump nikilovesyou1
    if niki_love >= 40 and otohaspring2 == True and day > 5 and nikispring1 == False:
        jump nikispring1
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Niki's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."

        jump callmorning
    if chapthreeactive == True:
        jump nikisummer2morninggen
    else:
        jump nikigenmorning

label callnikiafternoon:
    if nikiblock == True:
        "I should probably give Niki some space for now..."
        jump callafternoon
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Niki's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."

        jump callafternoon
    if nikidate1 == True:
        play sound "phonebeep.wav"

        "I tap on Niki's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        ni "Hello?"
        s "Hey, are you busy right now?"
        ni "Of course I'm busy. It's the middle of the day and I'm a public figure."
        ni "I have things to do."
        s "Is there any chance you'd be able to sneak away for a bit?"
        ni "Nope."
        ni "Call me some other time if you want to meet."
        s "Fine..."

        play sound "phonebeep.wav"

        "I hang up the phone and decide to call someone else."

        jump callafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Niki's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't pick up."
        "I guess I should call someone else."

        jump callafternoon

label callnikinight:
    if nikiblock == True:
        "I should probably give Niki some space for now..."
        jump callnight
    if niki_love >= 5 and rindorm40 == True and nikidate1 == True and nikidate5 == False:
        jump nikidate5
    if niki_love >= 15 and nikidate10 == True and day == 6 and nikidate15 == False:
        jump nikidate15
    if chap4active == True:
        jump nikispringnightgen
    if chapthreeactive == True:
        jump nikisummer2nightgen
    else:
        jump nikigennight

label nikigenmorning:
    play sound "phonebeep.wav"

    "I tap on Niki's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    ni "Hello?"
    s "Yo. Are you too busy and cool or whatever to make time for me this morning?"
    ni "Are you able to ask me out to breakfast {i}without{/i} being a condescending dick or is that a thing I should just give up on?"
    s "I'm honestly surprised you haven't given up already."
    ni "Ugh...fine. Yeah, whatever. But I don't want to go to that stupid sausage place again."
    s "I'll meet you at the sausage place in half an hour."
    ni "I just fucking told you-"

    play sound "phonebeep.wav"

    "I hang up the phone and make my way to the sausage place, Niki's favorite restaurant."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene nikigenmorning
    with dissolve
    play music "remember.mp3"

    ni "I fucking hate you so much."
    s "You look really attractive right now. I love girls who can handle a sausage."
    ni "And I love {i}men{/i} who don't force cute girls into not cute places!"
    s "Hey, in all fairness, I never would have found out about this place if it wasn't for you."
    s "Now shut up and eat your sausage."
    ni "Say {i}sausage{/i} one more time. I dare you."

    "I wind up saying {i}sausage{/i} several more times and nothing bad ever happens."
    "In fact, Niki winds up almost finishing her entire serving and the two of us are left to continue bickering until Kaori asks us to leave the restaurant."

    scene black
    with dissolve

    "Niki puts her mask and sunglasses back on and the two of us take to walking around the city for a little while."
    "It's kind of surreal being out and about with someone who has to hide their identity."
    "But, in a sense, I'm constantly hiding my whereabouts as well since it would be quite troublesome if some girls just always knew where I was."
    "We're not able to do much since Niki has other places she needs to be, but the time we {i}do{/i} spend with one another feels surprisingly natural."
    "In fact, I don't know why that's surprising at all to me at this point."
    "She knows more about me than anyone. Or at least who I was."
    "Not that the current me is all that hard to understand, but-"
    "Well, I guess all that matters is that she can still walk next to me after all this time."

    $ niki_love += 1
    stop music fadeout 5.0

    "{i}Niki's affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label nikigennight:
    play sound "phonebeep.wav"

    "I tap on Niki's name in my phone and wait for her to answer."
    "........."
    "......"
    "..."
    "There's no answer."
    "She's probably busy doing idol stuff or something."
    "I'll just try calling someone else."

    jump callnight

label nikiinvite:
    if nikiblock == True:
        "I should probably give Niki some space for now..."
        jump callnight
    if nikiinvite1 == False:
        jump nikiinvite1
    if nikiinvite1 == True and nikiinvite2 == False:
        jump nikiinvite2
    else:
        jump nikiinvitegen

label nikiinvitegen:
    play sound "phonebeep.wav"

    "I tap on Niki's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    s "Hey, Niki. What are you-"
    ni "Where are you right now?"
    s "Uhh...around. I was going to ask if you wanted to come over."
    ni "Yeah. I'm asking where you are because I am at your house and you're not here."
    s "What? How did you get in?"
    ni "Jesus Christ, are you coming or not?"
    s "I'm..."
    s "On my way, I guess?"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene nikiinvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    ni "About time~"
    ni "So...now what?"

    "How should I spend my time with Niki?"
    menu nikiinvmenu:
        "Hang Out (Raise Affection)":
            jump nikiinviteaff
        "Fingering (Raise Lust)":
            jump nikifingeranim
        "Reverse Cowgirl (Raise Lust)" if nikilovesyou3 == True:
            jump nikireverseanim
        "Headpat" if bonus == True:
            jump nikiheadpat

label nikiinviteaff:
    scene nikiinvitegen
    with fade

    "Niki and I aren't able to decide on anything to do, so she takes it upon herself to use my laptop to play some game and start ignoring me."
    "I guess that's not a big surprise considering she's already coming over uninvited as if she owns the place, but it's still a little rude and I will never forgive her for it."

    if bonus == True:
        ni "You have literally nothing on this computer except porn. Is this really what you've been doing all these years?"
        s "Do people use computers for things other than porn?"
    else:
        ni "You have literally nothing on this computer except essays and stock photos of hugs. Is this really what you've been doing all these years?"
        s "Do people use computers for other things?"

    ni "Sometimes, yeah. This is just so...depressing."
    ni "I'm going to delete everything."
    s "Niki, please go home."
    ni "No. You invited me over. Do something entertaining or your math homework folder is getting nuked."

    if bonus == True:
        s "How did you know that's where the porn was? It was such a flawless disguise."
        ni "It's the same exact thing you named your porn folder when we were in[school]."
    else:
        s "How did you know where I was storing the hug photos? It was such a flawless disguise."
        ni "It's the same exact thing you named your hug folder when we were in[school]."

    ni "This is just one more addition to the list of stuff that basically confirms that you're the real you and not some amnesiac douche bag with an affinity for pink haired girls."
    ni "Jesus, you don't even have Steam on this thing. Did you age an extra thirty years while you were gone? Do you just hate fun now?"
    s "..."

    scene black
    with dissolve

    "I don't {i}hate{/i} fun. I just don't find many things fun to begin with."
    "And, unsurprisingly, that list of things I don't find fun includes watching my ex-girlfriend go through files on my laptop and treat yet another possession of mine as if it's hers."
    "Eventually, though, she calls it quits and the two of us spend the next couple hours watching some televised talent contest sort of thing about a bunch of girls competing to be idols."

    if bonus == True:
        "Niki, being her typical conceited self, calls out the flaws in all of their performances while I, a civilized adult, just see a bunch of girls I want to have sex with."
        "And while I want to be dramatic and say that it's unfortunate I'll never be able to have sex with any of them...I know from experience now that this is not the case."
        "I can have sex with basically anyone."
        "Probably."
        "I just can't tell Niki that or she'll get mad at me and delete my porn for real next time..."

    $ niki_love += 3
    stop music fadeout 5.0

    "{i}Niki's affection has increased to [niki_love]!{/i}"

    if chap4active == True:
        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
    else:
        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label nikifingeranim:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump nikifingeranimx
    else:
        $ niki_lust += 3
        stop music fadeout 5.0

        "{i}Niki's lust has increased to [niki_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label nikidate1:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "I feel like I’m supposed to be a little nervous about doing this considering she is my apparent ex-girlfriend as well as a pop star, but-"
    "Eh."
    "It just feels like any other phone call to me."
    "And if this call is going to be anything like our “first” meeting the other day, I imagine she’s just going to yell at me or something like that."

    if bonus == True:
        "But hey, if we’re ever going to patch things up (And start having sex again), I’ve gotta start somewhere."

    play sound "phonebeep.wav"

    q "Thank you for calling 567 Productions. How can I help you?"
    s "..."
    q "Hello?"

    play music "remember.mp3"

    s "I’d like to speak with Niki Nakayama, please."
    q "..."
    q "No."
    s "But I’m her ex."
    q "That’s even worse."
    q "Please do not call here anymore."
    s "Wait, I think you’re misunderstanding something."
    s "She’s the one who gave me this number."
    q "Then she clearly doesn’t want to talk with you."
    q "You are aware that she has her own phone, correct?"

    "That fucking bitch."

    s "Listen...is she around? Just tell her I’m calling and if she doesn’t want to take it then...hang up on me or something."
    q "...Okay, fine."
    q "Can I have your name?"
    s "It’s...uhh..."

    menu:
        "Noodles":
            $ nikitemp = "Noodles"

            s "My name is Noodles."
            s "Noodles the Bird."
            q "Your name is not Noodles the Bird."
            s "Tell her my name is Noodles the Bird."
            q "Is this some sort of inside joke between the two of you?"
            s "Yes. Now, tell her."
            q "Okay...fine. "
            q "Please hold."

        "Paul":
            $ nikitemp = "Paul"

            s "My name is Paul."
            q "An American? How come I never heard of this?"
            q "How long ago were the two of you together?"
            s "Please stop prying into my personal life. This is between Niki and me."
            q "Apologies, Paul. I’ll let her know you’re calling right away."

        "Barack Obama, 44th President of the United States":
            $ nikitemp = "Barack"

            s "I’m Barack Obama, 44th president of the United States of America."
            q "..."
            s "..."
            q "..."
            s "I don’t have all day. I have meetings to attend."
            q "Please hold for one moment..."

    "I’m placed on hold for several minutes while the receptionist or manager or whoever it was that I was just speaking with tries to find Niki."
    "Hopefully, the original Sensei also had an amazing sense of humor that she will be able to quickly identify immediately upon hearing that she’s received a call."
    "But, more than likely, I just expect to get yelled at again."

    play sound "phonebeep.wav"

    ni "Well good morning, {i}[nikitemp]{/i}..."
    s "Hey. So nice of you to pick up."
    s "Why did you give me a fake number?"
    ni "It’s not fake, asshole. It’s the number to my agency."
    ni "You were just on the phone with my manager."
    ni "Also, why wouldn’t you use your normal fucking name?"
    s "I can’t remember my normal name."
    ni "{i}Hah{/i}...amnesia card again?"
    s "You know me so well."
    s "Almost well enough to give me your normal phone number."
    ni "Oh my fucking God, shut up. Why are you even calling?"
    ni "I’m not sure if you’ve realized, but I’m extremely busy right now and-"
    s "Let’s go out to breakfast."
    ni "At least let me finish my sentence, dick!"
    s "It’s not Dick, it’s {i}[nikitemp]{/i}."
    ni "You’re not funny."
    s "So, are you able to sneak away for a while and catch up? "
    ni "..."
    ni "Can I choose where we go?"
    s "If that’s what makes you happy."
    ni "..."
    ni "Fine. But {i}only{/i} for a little while. I have a class today."

    scene black
    with dissolve

    "The two of us talk for another minute or two and Niki winds up giving me an address to a diner somewhere in the middle of the city."
    "I didn’t really plan on going that far out today, but I guess you need to make certain sacrifices if you’re going to date someone famous."
    "Or at least, {i}go{/i} on a date with someone famous."
    "I doubt Niki would ever want to see me again after I apparently abandoned her for years."
    "But hey, she’s also apparently been waiting around for closure or something, so..."
    "I guess we’ll just have to see how things go."
    "........."
    "......"
    "..."

    scene nikifrtsdate1
    with dissolve

    s "What the fuck are you wearing?"
    ni "I’m a big fucking deal, {i}[nikitemp]{/i}. I need to wear this so people don’t recognize me."
    s "How are you going to eat with that on?"
    ni "I’m obviously going to take it off to eat! Have you never been on a date with an idol before?!"

    scene nikifrtsdate2
    with dissolve

    ni "Oh, what am I saying? Of course you haven’t. Sorry. Sometimes, I just forget how-"
    s "So what do you want to eat?"

    scene nikifrtsdate3
    with dissolve

    ni "STOP INTERRUPTING ME!"
    s "Take the disguise off, then. I want to actually talk to {i}you{/i}, not a mask and a cheap pair of sunglasses."

    scene nikifrtsdate4
    with dissolve

    ni "Cheap?! Those cost me a fucking fortune!"
    ni "Well...I actually got them for free as a gift from the agency. But they cost {i}someone{/i} a fortune!"

    "Niki takes off her mask and her glasses and stuffs them into an oversized bag she placed beside her when she arrived."
    "The two of us got here around the same time, so there was no awkward waiting at the table or anything like that beforehand."

    if bonus == True:
        "Just...two people who used to have sex (Probably) out for breakfast at a diner that totally isn’t something out of a popular first person shooter game."
    else:
        "Just...two people who used to date out for breakfast at a diner that totally isn’t something out of a popular first person shooter game."

    s "There. You look so much prettier now."

    scene nikifrtsdate5
    with dissolve

    ni "Shut up..."
    ni "You..."
    ni "You don’t look half bad yourself."
    ni "I kind of expected you to be huge and fat and all scraggly or something by now."
    ni "But I guess you’ve been doing alright the last few years."
    ni "Even if you managed to make it through them without turning your fucking TV on even {i}once{/i}."
    s "I’ve definitely turned the TV on. I just haven’t seen you."
    s "Maybe you’re just not as famous as you think you are?"

    scene nikifrtsdate6
    with dissolve

    ni "Want to bet on that? "
    ni "I can {i}guarantee{/i} you that our waitress will recognize me right away. "
    s "That’s not fair. You chose this place. For all I know, you could be a regular here."
    ni "I just wanted to choose some place that no one would ever expect me to come to. "
    ni "Which is exactly why I’m expecting our waitress to fall flat on her face the second she realizes she’s serving a pop star."
    s "You’re even more of an egomaniac than I am and I’m one of the last remaining males in Kumon-mi."
    ni "I {i}worked{/i} for this ego, {i}[nikitemp]{/i}. "
    ni "But of course you’re still pretending to have amnesia so you don’t have to remember how self-conscious I always was when we were younger."

    scene nikifrtsdate7
    with dissolve

    ni "Oh, perfect! Here comes our waitress now."
    ni "Watch and prepare to be amazed by my popularity."

    scene nikifrtsdate8
    with dissolve

    ni "Hi there! I’m sooo sorry for showing up unannounced. I hope I didn’t attract any paparazzi-"
    k "Friendburger Man!"
    ni "..."
    ni "I beg your pardon?"

    scene nikifrtsdate9
    with dissolve

    k "Hello! I am Kaori! But you may call me the Queen of Spiders or the Mistress of the Dark if you’d like."
    k "Are you on a date with my Friendburger?"
    s "This is actually my ex-girlfriend, Kaori."

    scene nikifrtsdate10
    with dissolve

    k "Girlfriendburger?!"
    ni "You..."
    ni "You really don’t recognize me?"
    ni "Niki Nakayama? Household name?"
    ni "I’m on billboards and..."

    if bonus == True:
        k "You mated with this creature?!"
    else:
        k "You hugged this creature?!"

    s "I’ll let her answer that question. I don’t think I’m at liberty to discuss my previous...{i}encounters{/i} with a celebrity."

    scene nikifrtsdate11
    with dissolve

    k "You are a celebrity? "
    k "I apologize for not recognizing you, but I do not know many of the popular cultures."
    ni "You don’t...have to apologize. I’m just a little taken aback."
    ni "Normally people have all sorts of questions for me when we first meet, so...this is actually a pleasant surprise, I guess?"
    k "I have two questions for you, actually. "
    k "Number one-"
    k "Is your hair made of cotton candy?"
    ni "...No."
    k "I see. "
    k "Number two-"

    if bonus == True:
        k "Can you describe to me how much you enjoyed mating with this man?"
    else:
        k "Can you describe to me how much you enjoyed doing the human hug move with this man?"

    scene nikifrtsdate12
    with dissolve

    ni "..."

    if bonus == True:
        s "Kaori, are you...curious about mating?"
    else:
        s "Kaori, are you...curious about hugs?"

    k "I am curious about many things. But this is the first female I have encountered with actual experience."
    k "Let alone experience with my friend! I must know!"
    k "Describe to me in vivid detail the things you experienced, Cotton Candy Girl!"

    scene nikifrtsdate13
    with dissolve

    ni "Was this all just some ploy to get me on one of those candid reaction shows?"
    ni "There’s no way any of this is actually happening, right?"
    s "You get used to it after a while. "
    s "I found myself thinking something similar the first few times I encountered Kaori."
    ni "Did she like...hit her head a little too hard?"
    s "There is a high likelihood of that, yes."

    scene nikifrtsdate14
    with dissolve

    ni "Listen...Kaori, was it?"
    ni "I think your curiosity is quite charming, I really do."

    scene nikifrtsdate15
    with dissolve

    ni "But if you ask either one of us about our {i}personal{/i} affairs again, I will not hesitate to destroy you."
    ni "Now, please make yourself useful and take our orders."
    k "I can not do that, Cotton Candy Girl!"
    k "I will remain quiet about your mating rituals, but this restaurant only serves one thing! Taking your order would be a waste of time!"

    scene nikifrtsdate16
    with dissolve

    if bonus == True:
        k "Friend. Your taste in women is very different from your taste in students."
    else:
        k "Friend. Your taste in women is very diverse."

    k "I had no idea you were the type who enjoyed being bossed around."
    k "I shall add this to my friendship journal. Entry number #387."
    s "It was a long time ago. I think my tastes may have been a little different back then."
    k "Whatever the case, Cotton Candy Girl has expressed her hunger and so I must do my duty as the number one waitress in Kumon-mi to please her."
    k "You can continue to please her in ways that I am not allowed to talk about."
    k "Until we meet again in several minutes."

    scene nikifrtsdate17
    with dissolve

    "Kaori darts away from the table and the atmosphere between Niki and I suddenly grows even more...uncomfortable."
    "For her, at least. "
    "I think this is the closest I’ve come to having fun in quite some time."

    ni "Ahem..."

    scene nikifrtsdate18
    with dissolve

    ni "I know it’s been a long time since the two of us have hung out like this."
    s "I feel a “but” coming."

    scene nikifrtsdate19
    with dissolve

    ni "{i}But{/i} would you mind explaining to me exactly {i}how{/i} you know that girl and why she is so interested in us {i}mating{/i}?"
    s "Explain Kaori? You’ve got a lot to learn."
    s "That’s just not possible."
    ni "You are aware that even being {i}seen{/i} in public with a man could destroy my reputation, correct?"
    ni "Do you have any idea what would happen to me if someone overheard that conversation?"
    s "I can’t imagine it would be anything good."
    ni "It would make the last several years of my life meaningless. "
    ni "The idol world is cutthroat. One wrong move and you’re done for good."
    ni "So if we’re going to continue going out together, {i}please{/i} make sure that nothing like that ever happens again."
    s "I think you just accidentally admitted that you want to keep seeing me."

    scene nikifrtsdate20
    with dissolve

    ni "Of course I do..."
    ni "Not as a couple or anything...you ruined that."
    ni "But I’d be...really hurt or whatever if we didn’t at least keep in touch."

    scene nikifrtsdate21
    with dissolve

    ni "Oh! And you owe me an apology! A real one!"
    ni "It’s not fair that you get to just walk back into my life and start talking about mating and...giving yourself weird names!"
    ni "We’re not teenagers anymore. We are grown adults and should be acting like that."

    scene nikifrtsdate22
    with dissolve

    ni "It doesn’t have to be today since...I know you’re still trying to come up with a better explanation than this whole “amnesia” thing, but..."
    ni "Whenever you’re ready to actually {i}talk{/i}...that’s fine."
    ni "We can just keep going out to breakfast or something until then."
    s "And if I have no idea how long that will take?"
    ni "Then you’re going to be buying me a lot of breakfasts."

    scene nikifrtsdate23
    with hpunch
    play sound "thump.mp3"

    k "I present to you, the Route 69 Diner’s special {i}and only{/i} item, the sausage-fest!"
    ni "Wha-"
    ni "People actually...{i}eat{/i} this?"
    k "Friend. Your ex-girlfriend does not seem to grasp the concept of food."
    k "Is this what ended your previous relationship?"
    s "Yes. This is exactly why we broke up."
    s "Niki, enjoy the sausage-fest."

    scene nikifrtsdate24
    with dissolve

    ni "Actually, I already ate breakfast this morning. And that’s way too much food."
    ni "This is all you. "
    s "Kaori, are you hungry?"
    k "Wieners make my mouth feel funny. I think they are too big for me."
    s "Can you say that one more time but a little slower?"

    "I take out my phone to record and-"

    scene nikifrtsdate25
    with hpunch

    ni "Stop hitting on the fucking waitress right in front of me!"
    k "Enjoy your wieners! I must help another customer now!"
    k "Let us hang the outs again soon, Friend! John misses you!"
    s "Sounds good, Kaori. Thanks for your service."
    k "Of course! Please remember to like, comment and subscribe!"

    scene nikifrtsdate26
    with dissolve

    ni "..."
    s "..."
    ni "Really, though. I’m not hungry at all. I can’t eat that."

    "I take one last look at the colossal pile of food before me..."
    "And surrender myself to the sausage-fest."

    scene black
    with dissolve2

    "Of course, I’m barely able to finish any of it. "
    "And apparently this diner doesn’t offer to-go boxes either, so a good thirty pounds of food are left on the table by the time we leave."
    "But at least Niki and I got to “reconnect” a bit. "
    "She’s not much different from how I pictured her after our first meeting in the studio, but..."
    "I guess I can see why the old Sensei might have fallen for her."
    "{i}Congratulations! You now have Niki’s real phone number and don’t have to lie about your name anymore!{/i}"

    $ renpy.end_replay()
    $ niki_love += 1
    $ nikidate1 = True
    stop music fadeout 5.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label nikidate5:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer. "
    "Given that it’s her actual number this time and I won’t need to go through a third party in order to talk to her, I’m feeling a bit optimistic."
    "I mean, I’ve grown pretty accustomed to never being turned down to begin with, but if it was ever going to happen, it was going to be because of that manager of hers."

    play sound "phonebeep.wav"
    play music "love.mp3" fadein 15.0

    ni "Hello?"
    s "Hey. What are you doing tonight?"
    ni "Being famous. Why?"
    s "Are you going to remind me of how famous you are every time we talk?"
    ni "Of course not. I’ll stop once you acknowledge me."
    s "You’re so famous and I’m so glad to know you."
    ni "Once you acknowledge me {i}for real!{/i} "
    s "Oh. That might still be a ways off."
    ni "Do you need something or are you just calling to remind me that you’re unimpressed by the huge strides I’ve made as both a person and a woman?"
    s "Women are people too, Niki. Don’t say things like that."
    ni "That’s not what I meant! Stop being an asshole or I’ll hang up!"
    s "You wouldn’t hang up on-"

    play sound "phonebeep.wav"

    s "..."

    "Did she...actually hang up on me?"

    s "..."

    play sound "phonebeep.wav"

    "I tap on Niki’s name {i}again{/i} and wait for her to answer {i}again.{/i}"
    "........."
    "......"

    play sound "phonebeep.wav"

    ni "Fuck you. "
    s "Okay, fine. I won’t mess with you."
    ni "Oh my fucking- if you're going to invite me out, just do it already!"
    ni "That’s why you’re calling, isn’t it?"
    ni "Didn’t we decide on breakfast as our reconnecting meal? You’re not just waking up now, are you?"
    s "I have been awake for quite some time. And yes, this is me asking you out right now."
    ni "Fine. "
    ni "I want soba noodles."
    ni "What places do you know that sell soba? "
    s "I can...look one up?"
    ni "Okay. Text me when you figure it out. "
    s "I don’t need to pick you up or anything?"
    ni "Wait, did you actually learn how to drive?"
    s "No. I was offering to walk by and physically carry you to-"

    play sound "phonebeep.wav"

    s "..."

    "Wow."
    "She really doesn’t take any shit from me, does she?"
    "She’s like a real ex-girlfriend."

    scene black
    with dissolve

    "Well, I guess she technically {i}is{/i} a real ex-girlfriend...but it still doesn’t seem very real to me."
    "I’ve already learned a little about the past from Noriko, but..."
    "If anyone {i}really{/i} knows anything about the original Sensei, wouldn’t it be Niki?"
    "Even if it’s something as simple as..."
    "........."
    "......"
    "..."

    scene nikidinner1
    with dissolve

    ni "You...what?"
    s "I forgot how old I am. Please tell me."

    "As you can see, I’ve decided to ask Niki some baseline questions to really establish who I am “supposed to be” as a person."

    ni "Are you fucking kidding?"

    "As you can see, she does not like that very much."

    ni "How many times are you going to try and get me to do something stupid for your silly candid reality show thing?"
    s "There is no show. I just genuinely don’t know how old I am..."

    scene nikidinner2
    with dissolve

    ni "Then look at your ID! You’re a grown man! You can’t rely on me for things like this!"
    s "Funny story. I actually lost my ID. "
    ni "That’s not funny! It’s inconvenient! Those things are really annoying to replace!"
    s "So you don’t know?"

    scene nikidinner3
    with dissolve

    ni "Of course I know, idiot. "
    ni "{i}I just don’t want to say it because it will remind me of how old I am.{/i}"
    s "Are we the same age?"
    ni "You’re two years older than me. "
    s "There’s no way I’m only two years older than you."

    scene nikidinner4
    with dissolve

    ni "There is a way! And even that two year gap was annoying in [high_school]!"
    ni "I only got to spend one year in[school] with you and no one ever believed I was dating an older guy when I told them about it!"
    s "I mean...two years older isn’t {i}that{/i} much older."
    ni "It is when you’re in [high_school]! "
    s "Niki, I think you should probably stop yelling."

    scene nikidinner5
    with dissolve

    ni "I’M ON TV! I CAN YELL WHENEVER I WANT!"
    s "Aren’t you the one who said you didn’t want to attract any attention?"

    scene nikidinner6
    with dissolve

    ni "Yeah..."
    ni "I’m just annoyed you’re still keeping up this stupid amnesia thing."
    ni "Pretending to forget your age...pretending to forget {i}me{/i}. "
    ni "It’s all really fucking frustrating after I spent years worrying about you."
    ni "And I haven’t even gotten an actual apology yet."
    s "You’ll get one as soon as I’m able to be sincere about it."
    ni "So you can dump me after five years and leave me to rot but you can’t even fork over an actual apology."
    ni "Can we get the check now? I don’t want to be here anymore."
    s "I can’t be sincere because there really is something...{i}wrong{/i} with my memory."
    s "It’s not amnesia, per se...but it’s like..."
    s "It’s like I’m a different person occupying this body."

    scene nikidinner7
    with dissolve

    ni "Bullshit."
    ni "You’re exactly the same way you’ve always been. Just taller and...with a thicker T-shirt."
    s "Thank you for noticing the T-shirt. No one ever does."

    scene nikidinner8
    with dissolve

    ni "What I’m saying is if there is anyone out there who would be able to catch if you were magically a different person or whatever, it’s me. "
    ni "We grew up together. Shit, you basically lived at my house."
    ni "And I feel like an idiot for ever believing it but, for a long time, I was pretty sure I was going to spend the rest of my life with you."

    scene nikidinner9
    with dissolve

    ni "But now I’m famous and cute and you’re a loser so HA."
    ni "Chance is gone, pal. "
    s "..."

    "That can’t be right."
    "Even if Niki and Sensei {i}did{/i} spend that much time together, what about all of the time they didn’t?"
    "It’s highly possible- no. Highly {i}probable{/i} that he changed as years went by. "
    "And then, for some reason I still don’t quite understand, I wound up taking his place."
    "And not just me, but seemingly countless other people if we’re going by what Maya says."
    "..."
    "But what if Maya’s wrong?"
    "And what if Niki’s wrong?"
    "What if I’m wrong?"

    s "God, this is so fucking confusing."

    scene nikidinner10
    with dissolve

    ni "What’s up?"
    ni "You know I’m just messing around with you, right?"
    ni "You’re not a loser. "
    ni "Noriko says you finally became a real teacher. So I guess your dreams came true to at least some extent. "
    s "I just mean this whole memory thing. "
    s "I don’t even know if I want what you’re saying to be true or not."
    ni "Why on earth would you not want to be yourself?"
    s "Because if that’s true, it’s going to be a lot harder to justify why I can’t remember anything past the last several months."
    s "It’s like I just woke up one day and started a brand new life in a brand new body and just...went from there."
    ni "..."
    s "..."

    scene nikidinner11
    with dissolve

    ni "You’re going to be okay."
    ni "You’re still you."

    scene nikidinner12
    with dissolve

    ni "Something similar happened to me before, you know."
    ni "I never told anyone about it because I was worried it would make me sound crazy."
    ni "But there were a lot of days where I woke up and felt sorta...disconnected from the world. "
    ni "Like I was also just a visitor in my own body."
    ni "I think I even tried convincing myself that you never existed a few times because it would have made everything a whole lot easier."
    ni "It’s really hard to get mad at someone after they go through a tragedy and isolate themselves, but like...it’s hard to {i}not{/i} get mad, too. "
    ni "I wanted to be there for you and you clearly didn’t want me to do that."
    ni "And it got really bad at points."
    ni "I lost sleep."
    ni "I heard things."
    ni "I’m pretty sure I even started hallucinating at some points."
    ni "Looking back on it, though. They could have just been dreams."
    ni "You really did a number on me when you left."
    ni "So I just did what any heartbroken girl would do to fix it. "
    ni "I stayed in bed. Cried a lot. Gained weight."
    ni "Starved myself. Lost weight. Cried a lot more."

    scene nikidinner13
    with dissolve

    ni "I thought about killing myself too."
    ni "Not cause I wanted to die, though. I think I just wanted to teach you a lesson."
    ni "To show you that you’re a selfish asshole and that other people are able to think and feel too."
    ni "But I’m smart and awesome, so eventually I just realized that I was tying too much of my self-worth to you. "
    ni "And that I didn’t need you to exist."
    ni "So I stopped starving myself and staying in bed and started training to become the best possible version of myself that I could be."

    scene nikidinner9
    with dissolve

    ni "And now I’m famous and cute and you’re a loser so HA."
    s "And to think we could have avoided all of that if you’d just told me my age."

    scene nikidinner14
    with dissolve

    ni "Nah. It feels good to get all that off my chest. "
    ni "I’m sure you’ll do the same when you realize that you’re just subconsciously hiding your memories, and that they’re not gone forever."
    s "Maybe. And all of that sounds plausible...but there’s one glaring mistake."

    scene nikidinner15
    with dissolve

    ni "Mistake? What are you talking about?"
    s "That doesn’t explain the time loops."
    ni "..."
    s "..."
    ni "Are you high?"

    "I knew her explanation was too good to be true."
    "It was too convenient."
    "It’s one thing to dwell and break over a tragedy in your life. And sadness can manifest in so many ways."
    "Niki knows that well."
    "But what it {i}can’t{/i} do is toss you into a repeating[school] year where everyone’s memory of time itself is wiped clean every few months, but their interpersonal memories remain."
    "It's not just me that's broken. The {i}world{/i} is broken."
    "Everything ever is broken."
    "And the kind, honest words of a girl who used to love me are not going to change that."

    s "I’m glad you opened up. But I still think what I’m going through is slightly different."
    ni "Are you sure you’re not just being a selfish asshole again? You’ve always been good at that."
    s "Not {i}entirely{/i} sure, but pretty sure. Yeah."
    ni "So what are you going to do then? Give up on the past entirely or try and do something to get it back?"
    s "Good question."
    s "Maybe I should just become an idol too?"
    ni "Holy fuck, you really {i}are{/i} high."
    ni "How long have you been hooked?"
    s "It was a joke, Niki."
    ni "I don’t know if I buy that. Memory loss...delusion...those are textbook symptoms of addiction."
    ni "Probably."
    s "So you’re really not going to tell me how old I am?"

    scene nikidinner16
    with dissolve

    ni "Why do you keep asking me that pointless question? Knowing your age will change literally nothing."
    s "What if it sparks a chain reaction that gives me all of my memories back? "
    s "We’d be one step closer to your apology."
    ni "..."
    s "..."

    scene nikidinner17
    with dissolve

    ni "..."
    s "..."

    if bonus == True:
        ni "You’re 31."
    else:
        ni "You’re 5,000."
        s "Dear God...I'm a wizard?"

    ni "Now shut up and stop asking me stupid questions."

    "Wow. I guess my original guess wasn’t that far off."
    "I’m a little younger than I thought, but Niki is-"

    s "Wait..."

    if bonus == True:
        s "If I’m 31...and you’re two years younger than me-"
    else:
        s "If I’m 5,000...and you’re two years younger than me-"

    s "..."

    if bonus == True:
        s "You’re {i}29?...{/i}"
    else:
        s "You’re {i}4998?...{/i}"

    scene nikidinner18
    with dissolve

    ni "Don’t remind me! I’m practically six feet underground already!"
    ni "I wasted basically my entire 20’s on you and now you apparently don’t even remember your age!"

    if bonus == True:
        s "You look...really good for 29."
        ni "Of course I do!"
        ni "It’s hard to {i}not{/i} look good when you burn six trillion calories a week!"
        ni "From the moment I wake up until the moment I go to bed it’s just training, training, training."
    else:
        s "What does that have to do with anything? That was over 4000 years ago."
        s "Either way, you're hot now."

    scene nikidinner19
    with dissolve

    ni "But...thanks, I guess."
    ni "You look good, too."
    s "..."
    ni "..."

    if bonus == True:
        s "I can’t believe you’re almost 30 years old and you look like that."
    else:
        s "I can’t believe you’re almost a wizard and you look like that."

    scene nikidinner20
    with dissolve

    ni "Shut. Your. Fucking. Mouth."
    k "Friend! Cotton Candy Girl! How are the soggy wheat strings that you have yet to consume?"

    scene nikidinner21
    with dissolve

    s "Fine, Kaori. Thanks for checking in on us."
    k "The manager asked that I come rain silence upon you as Cotton Candy Girl’s vocal chords are extremely strong!"
    s "Probably from being an idol or whatever. Has she mentioned that to you yet?"
    k "Many times! But I have yet to see her in the picture box!"
    ni "Watch closer! I’m there! All the time! It’s not a joke!"
    k "Friend. Can you tell me how you feel about hard circle lizards?"
    s "Turtles? I think they’re okay. "
    s "Can this wait until next time, though? Niki and I are in the middle of a conversation."
    k "Yes! I will send you pictures of a good circle turtle tonight!"
    s "Just a turtle, Kaori."
    k "I understand! "
    k "Hello!"

    scene nikidinner22
    with dissolve

    "Kaori leaves just as quickly as she appeared and I find myself once again talking to someone that I can confirm is a human."

    if bonus == True:
        ni "She’s a lot cuter when she’s not asking if we’ve had sex before."
    else:
        ni "She’s a lot cuter when she’s not around."

    s "Do you want her number?"
    ni "Depends. Do you think she’d have any interest in becoming an idol?"
    s "Kaori?"
    ni "Yeah."
    s "Like, {i}that{/i} Kaori?"
    ni "Yeah. I think she’d be good."
    s "..."
    s "{i}Kaori?{/i}"

    scene nikidinner23
    with dissolve

    ni "I figured you’d have a bit more faith in her, {i}Friend{/i}."
    s "I do, but..."
    s "{i}Kaori?{/i}"
    ni "She’s on her feet all hours of the day. She’s got a nice figure. And heterochromia is highly fetishized for whatever reason, so she’d definitely sell."
    s "She also has a gigantic spider tattoo on her chest."

    scene nikidinner24
    with dissolve

    ni "You’ve seen her chest?"
    s "I don’t think you’re understanding. It’s a {i}big{/i} fucking spider."
    ni "Why on earth would she do that? "
    s "Because she’s Kaori. Just leave it at that."
    s "Why her anyway? Is your agency desperate for idols or something?"

    scene nikidinner25
    with dissolve

    ni "That’s not it."
    ni "I just..."
    ni "Do you remember the first time we went to karaoke together?"
    s "Nope."

    scene nikidinner26
    with dissolve

    ni "Oh. Right."
    ni "Well, basically, I was super nervous about singing in front of you. But you talked me into it and then told me I was great afterward."
    s "So you’re naturally talented. Good for you."
    ni "Oh, no. You totally lied. I was horrible."
    ni "But something clicked in me when I was singing and, even though I sucked, it felt liberating. I really loved it."
    ni "So I wound up taking lessons and, once I figured out how to control my voice, it changed everything. "
    ni "I didn’t have to be nervous anymore."

    scene nikidinner27
    with dissolve

    ni "I just think it would be nice being able to help girls over that same hurdle."
    s "So you’re a famous idol, but...you want to be a vocal coach?"

    scene nikidinner28
    with dissolve

    ni "Who says I can’t do both?"
    ni "News flash, but I’m kind of amazing."
    ni "I’ve already got one girl under my wing and she’s gonna be totally huge one day. Mark my words."
    ni "Super cute, too. She’s the whole package."
    s "You’re just talking about your sister, aren’t you?"

    scene nikidinner29
    with dissolve

    ni "What, Noriko? She wouldn’t be caught dead singing anything that doesn’t sound like it’s filtered through a five dollar guitar amp."
    ni "My girl is friends with her, though. Her name is Otoha."
    s "Woah."
    ni "Woah what? Why woah?"
    s "How many rings does she wear?"
    ni "A lot. Why?"
    s "I know her."
    ni "Why do you know a [teenage]girl from a[school] you don’t teach at?"
    s "One of my students has a crush on her."
    ni "This is a really weird coincidence."
    s "It really is. I had no idea you were the sketchy basement girl."

    scene nikidinner30
    with dissolve

    ni "Well...the...the agency doesn’t want me...teaching classes so..."
    ni "I had to pick somewhere...secret..."
    s "And you just happened to choose a sketchy basement."

    scene nikidinner31
    with dissolve

    ni "It was all I could find..."
    ni "I’m...still looking for somewhere else..."
    s "Either way, it’s nice to know you’re following your dreams. Just don’t let it get in the way of the thing that’s actually making you money."

    scene nikidinner32
    with dissolve

    ni "Obviously. But thanks for the advice, anyway."
    ni "Do you want me to say hi to Otoha for you?"
    s "Nah. I’m sure I’ll be seeing her again sometime. "
    ni "That’s not a creepy thing to say at all."
    s "I’m sure you’ll be hearing plenty more borderline creepy things from me in the future, so you might as well get used to it now."

    scene black
    with dissolve2

    "Niki and I finish our dinner and talk a little more about her life as an idol...and how weird it was for her to blow up out of nowhere."
    "It feels kind of surreal, to be honest-"
    "Having someone so...established acting so familiar with me."
    "Like nothing has changed even after all she’s been through."
    "Like it’s any other day..."

    scene nikidinner33
    with dissolve

    ni "I like this place. We should come back."
    s "Are you going to pay next time? "
    ni "What? No. Why would I do that?"
    s "Because you’re rich?"
    ni "I’m probably not as rich as you think. "
    ni "You’re paying every single time until you apologize for destroying my heart."
    s "I agreed to paying for breakfast, but dinner as well is just-"

    scene nikidinner34
    with dissolve

    ni "You owe me~"
    ni "How about I get you a punch card?"
    ni "Buy me ten meals and I might even let you hold my hand."
    s "What could I get for twenty meals?"

    scene nikidinner35
    with dissolve

    ni "We can discuss that once you get there."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ nikidate5 = True
    $ niki_love += 1
    stop music fadeout 5.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"
    "{i}You've received a new picture message from Kaori!{/i}"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label nikidate10:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "It’s still early, so chances are she has enough time for her daily dose of wiener right now."
    "I’m not usually the type of guy to call up a girl just to give her some sausage, but Niki seems to really enjoy that sort of thing."
    "Besides, Kaori will be there as well. And nothing says bonding like two girls wrapping their lips around some meat together."

    play sound "phonebeep.wav"
    play music "remember.mp3"

    ni "What do you want?"
    s "Oh, you {i}know{/i} what I want."
    ni "Ew, why are you talking like that? Stop it."
    s "Sorry."
    s "Are you free right now?"
    ni "Depends."
    s "On?"
    ni "Whether or not {i}you’re{/i} free."
    s "I am."
    ni "Then I am not. Goodbye, [nikitemp]."
    s "You fucking bitch."
    ni "Hahah! I’m kidding, idiot. "
    ni "Yeah, I can get away for an hour or two. "
    ni "But if you show up with my little sister, I swear to fucking God."

    if bonus == True:
        s "Oh, don’t worry. She’s still asleep in my bed. It was a really long night."
        ni "You fucking-"
    else:
        s "I would never. Noriko is my student and I respect you far too much."
        s "I love you, Niki."
        ni "Wait...did you just say what I-"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and laugh silently to myself as I get dressed."

    if bonus == True:
        "And then I say goodbye to Noriko, who is still asleep in my bed following a very long night."
        "..."
        "Just kidding."

    "........."
    "......"
    "..."

    scene nikidateten1
    with fade

    "Kaori is able to go on break shortly after Niki and I make it to the diner and I move one step closer to watching her eat a wiener."

    s "Kaori."
    k "Yes, Ex-Boyfriendburger?"
    s "I’m not your ex-boyfriend. I’m Niki’s."
    k "What is a “Niki?”"
    s "Sorry. I meant the cotton candy girl."
    ni "You know, Kaori, you should probably think of adding more things to the menu soon. I feel like you’re missing out on a good amount of profit only selling one thing."

    scene nikidateten2
    with dissolve

    k "But you love the wiener! "
    ni "I {i}tolerate{/i} the wiener. It’s different. I’d much prefer something sweeter."
    s "Weird way to admit to being a lesbian, but I’m glad I could be here to witness it."

    scene nikidateten3
    with dissolve

    ni "Shush."
    s "Did you just shush me?..."
    k "What’s a “lesbian?”"

    scene nikidateten4
    with dissolve

    ni "A lesbian is a girl who’s sexually attracted to other girls."
    k "Is that not all girls? "

    scene nikidateten5
    with dissolve

    ni "You like girls, Kaori?"
    k "I like all people! Everyone is attractive in their own way! Even you!"
    ni "..."
    ni "What do you mean, “even” me?"
    k "I apologize for being hard to understand. But it seems that you still have your sights set on Friendburger, which means we can not be together!"
    s "Niki’s straight anyway, so she wouldn't want a relationship with you, Kaori."

    scene nikidateten6
    with dissolve

    ni "What are you talking about? No I’m not."
    s "You’re not?"
    ni "You literally know this. We got into a fight over-"

    scene nikidateten7
    with dissolve

    ni "Oh, right. Your stupid memory sucks or whatever."

    "I learned something today."

    k "Do you see how the one made of aerated sugar did not deny her feelings for you? This must be love!"
    k "Kiss!"

    scene nikidateten8
    with dissolve

    ni "No, Kaori. I’m not going to kiss my stupid, asshole ex-boyfriend in a dirty old diner full of...dirt and stuff."
    k "I cleaned this table myself! You may kiss here whenever you like and I will explain to my manager that I can not stop love!"

    scene nikidateten9
    with dissolve

    ni "Can I kiss you instead? You think I’m cute, right?"
    k "Kissburger?!"

    if bonus == True:
        s "I know I’m probably supposed to be getting jealous or whatever, but I want to let the two of you know that I unconditionally support this development."
    else:
        s "I know I’m probably supposed to be getting jealous or whatever, but I think you two would make a wonderful couple."

    scene nikidateten10
    with dissolve

    if bonus == True:
        ni "Ugh, great. So now I just sound like a slut. Thanks."
        k "Slutburger..."
        s "Apologize to Kaori. You got her hopes up and now she has to learn what a slut is."
    else:
        ni "Ugh, great. That's not what I wanted at all."
        k "Coupleburger..."
        s "Apologize to Kaori. She deserves better than this."

    scene nikidateten11
    with dissolve

    ni "I’m sorry for playing around, Kaori. I have a history of losing my head around this jerkburger and it often leads to me saying things in the heat of the moment."

    scene nikidateten12
    with dissolve

    k "Ah! Jerkburger!"
    s "What? No. Don’t repeat things Niki says. She’s evil and steals clothing from people without realizing they only have two versions of the same shirt."
    ni "I’d like to say I still have a few of your hoodies from back when we dated, but I think I may have {i}accidentally{/i} dropped all of them into a fire. Whoops."
    s "Wow. I really did a number on you, didn’t I?"

    scene nikidateten13
    with dissolve

    ni "Haha! Yeah! You made me want to kill myself! Thanks!"
    k "Uh-oh. This does not seem like a conversation that is friendly for the Mistress of the Dark to be involved with. "
    k "I have already informed both of you that I can not stop love. Please continue confessing your sad human feelings to one another while I go pretend to not listen from behind the counter."

    scene nikidateten14
    with dissolve

    ni "Wait, Kaori. You don’t have to leave. I was just-"
    k "Tell the burger about your feelings while I prepare for the wieners to come!"
    k "They are very big wieners, so it may take them longer to come than normal ones!"
    ni "..."
    s "I think that’s a myth, actually. I have no trouble-"

    scene nikidateten15
    with dissolve

    k "Only I can make your wiener come! Don’t you forget that!"
    ni "..."
    s "Got it."
    s "Thanks, Kaori."
    k "Hello!"

    scene nikidateten16
    with dissolve

    "Kaori storms off into the kitchen and trips over...something. "
    "It’s probably nothing to worry about, though, since a few of the kitchen staff quickly come to her rescue and help her regain her footing before breaking into a fit of laughter."
    "It’s a little tough to remember that people have lives outside of me, but I guess Kaori and Niki are the two best examples of that I can think of."

    if bonus == True:
        "Both of them live to please others while I...live to please myself and various [teenage]girls."
        "Just...in a different way."

    scene nikidateten17
    with dissolve

    ni "Why do I get the feeling you were thinking of something disgusting just now?"

    if bonus == True:
        s "Probably a safe bet. I’m essentially always thinking of something disgusting."
    else:
        s "Because you hate me and refuse to believe I am a good boy."

    "Niki takes off her disguise in preparation for the coming sausages and slides her glasses to the side of the table."
    "But instead of saying anything afterward, she just stares at me like she’s waiting for me to...apologize for my entire existence or something like that."
    "I don’t really know what she wants."
    "That’s probably why our relationship ended."
    "I’m sure it had nothing to do with whatever tragedy that befell me."

    play sound "static.mp3"
    scene handsareweird with flash
    scene imissyoumore with flash
    scene dust5 with flash
    scene nikidateten17 with flash
    stop sound

    s "So, about what happened at the beach."
    ni "What about it?"
    s "Well...that was weird, right?"
    ni "Which part? The one where I showed up? Or the one where I left before you woke up?"
    s "I guess both. I thought we were on a little worse terms than sleeping together."
    ni "As much as we {i}should{/i} be on worse terms, I’m doing my best to not hold anything against you."

    scene nikidateten18
    with dissolve

    ni "I know things were really rough for you back then. "
    ni "I just wish you would have called or something and...you know, {i}not{/i} kept your childhood friend and first ever girlfriend waiting like a fucking lunatic."
    ni "I missed you a lot."
    ni "And like...I don’t know. I guess I still do or whatever."
    s "It’s starting to sound like I won’t be getting my shirt back."

    scene nikidateten19
    with dissolve

    ni "Will you shut up about the fucking shirt?! I’m trying to be serious here!"

    scene nikidateten18
    with dissolve

    ni "You know...I always said all this stuff to myself about what I would do if I actually {i}did{/i} bump into you again."
    ni "And in every single made up scenario, I always had the upper hand."
    ni "I’d catch you in line for one of my concerts or see you in the mall during a signing event...and I’d laugh to myself and look the other way."
    ni "I wanted you to think that I forgot about you, like how {i}you{/i} forgot about me."
    ni "Or...are {i}continuing{/i} to forget about me, because I still have no idea what this shit you’re trying to pull with your memory is."
    ni "But...as much as I hate to say it...I can’t do it."
    ni "I can’t actually forget you."
    ni "And...I don’t even think I want to anymore."
    ni "Which is why I made my driver turn around and take me back to the inn. And why I left in such a hurry that I didn’t even take my bag with me."
    s "You were that excited to see me?"

    scene nikidateten20
    with dissolve

    if bonus == True:
        ni "You know, there are thousands, if not millions of other guys who would be creaming their pants if they were in your position right now."
        s "Do you...do you want me to ejaculate?"
    else:
        ni "You know, there are thousands, if not millions of other guys who would be freaking out if they were in your position right now."
        s "Would it make you feel better if I stole your things and ran away to go sell them on the Internet?"

    scene nikidateten21
    with dissolve

    ni "{i}What?{/i}"
    s "You just sounded a little disappointed that I’m not freaking out about this."

    scene nikidateten22
    with dissolve

    ni "Because I am! I hate that {i}I’m{/i} the one crawling back when I spent years and years and years preparing myself to do the opposite!"
    s "You're not saying you want to get back together, are you?"

    scene nikidateten23
    with dissolve

    ni "No...I don’t think so. "
    ni "I don’t really know what I’m saying."
    ni "I {i}can’t{/i} have a boyfriend because of my job. But I also don’t really want you running off and settling down with anyone either. "
    s "Well...you definitely don’t have to worry about that. I’m not really the “settling” type."
    ni "No...you never were..."
    ni "..."
    s "..."
    ni "Hey."
    ni "You’re not..."

    if bonus == True:
        ni "Still a virgin, are you?..."
    else:
        ni "Still trying to sell my bobsled, are you?..."

    s "..."
    ni "..."
    s "I’m sorry, what?"

    if bonus == True:
        ni "Since we...you know. Never really did it."
    else:
        ni "Nevermind. Just tell me if you're dating anyone."

    s "..."
    ni "..."
    s "You..."
    ni "Mhm."
    ni "But not because I can’t find anyone. I’m famous and I can have whoever I want."
    ni "I was just...never interested in anyone else."

    if bonus == True:
        s "You are a world-famous idol who is about to turn thirty...and is still a virgin?"
    else:
        s "Wow? Not a single person in almost 5,000 years? That is very sad."

    scene nikidateten24
    with dissolve

    if bonus == True:
        ni "What does my age have to do with it?! There’s nothing wrong with being a virgin at thirty!"
        ni "In fact, there are tons of people who go even longer than that! "
        ni "And you’d probably be surprised to hear that some of them may be listening in on this conversation right now!"
        s "I’m sorry if this sounds insensitive, but...we really never had sex?"
    else:
        ni "It is not sad! It is perfectly normal! Now, about that boblsed!"
        s "Do you need a hug?"

    scene nikidateten25
    with dissolve

    if bonus == True:
        ni "We just did...{i}hand{/i} stuff most of the time."
        ni "It was hard since my parents and Noriko were always home..."
        ni "And, believe it or not, you were really understanding about that sort of thing back then. You never pushed me to really {i}do{/i} it, you know?"
        ni "Jesus, why are we even talking about this in a diner? What has my life become?"
        s "..."
        s "Niki, I-"
        ni "I changed my mind. I don’t want to hear it."
        ni "You can keep whatever you’ve done these last eight years to yourself. I don’t want to know."
        ni "I’ll just fill in the blanks with how I want things to be and force myself to believe they’re true. "
        s "Is that really how you want to live? By just pretending things are better than they actually are?"
        ni "Gee, wonder who I learned that from?"
        s "I don’t have a problem with it. I’m just surprised to be seeing this side of you when it still seems like you can’t stand being around me half the time."
        ni "Trust me, this is even weirder for me than it is for you."
        ni "God. None of this ever would have happened if I didn’t bump into you and Noriko at that damn beach. My mind has not stopped being fucking...annoying since then."
        s "Do you think something is actually happening between Noriko and me?"
        ni "I think...that Noriko likes you way more than she should. And I think you’re exactly the type to take that affection and run with it."
        ni "It seems like you’ve always been trying to fill some sort of hole inside of you, and I don’t really know who else is there to do that right now."
        ni "So...I don’t know. Keep me in your thoughts and don’t fuck my sister, I guess?"
        s "..."
    else:
        ni "Maybe a little one..."

    scene nikidateten26
    with dissolve

    if bonus == True:
        ni "Like, really. Please don’t fuck my sister."
    else:
        ni "But only if we can do it in the kitchen."

    s "..."
    ni "..."

    scene nikidateten24
    with dissolve

    if bonus == True:
        ni "Jesus Christ! Repeat after me! You! Will! Not! Fuck! My! Sister!"
        s "You. Will. Not-"
        ni "Not “You!” "
        ni "“I will not fuck your sister!”"
        s "Thank you for making that promise, Niki. But I don’t have a sister for you to fuck no matter {i}how{/i} much you want to. "
    else:
        ni "I want to have a kitchen hug!"
        s "What is happening right now?"

    scene nikidateten27
    with dissolve

    ni "Okay, you know what? This was clearly a mistake. "
    ni "I thought it might be a sign that I wanted to start patching things up when I came to you in the middle of the night, but I can see now that you’re just going to be a prick about it."
    s "I need you to look at things from my perspective, though."
    s "You showed up in the middle of the night, stole one of my shirts, and then left before-"

    scene nikidateten24
    with hpunch

    ni "Oh my fucking God! I will literally buy you a new shirt! Just shut the fuck up about it!"
    k "Incoming wieners! Brace for impact and massive girth!"

    play sound "thump.mp3"
    scene nikidateten28
    with hpunch

    ni "Hah..."
    s "Wait, we didn’t even order-"
    k "You did not have to, Jerkyexboyfriendburger! We only have one thing on the menu!"
    k "Didn't you read it? All we have is the sausage fest!"
    k "Seriously! That’s it!"
    ni "We read the fucking menu, Kaori."
    k "Congratulations! I am very proud of your ability to comprehend words! Good job!"

    scene nikidateten29
    with dissolve

    ni "So, now what?"
    s "What do you mean?"
    s "I figure that if you want to start patching things up, we can-"
    ni "Not about our fucking relationship. About all this food."
    s "Oh. Well, I’m not hungry."
    ni "Remind me again why we keep coming here if you literally never eat anything?"
    s "That’s easy, Niki."

    scene black
    with dissolve2

    if bonus == True:
        s "Because if there is anyone who deserves a good wiener, it’s a twenty-nine year old virgin."
        ni "I fucking hate you."
    else:
        s "Because I have forgotten {i}how{/i} to eat."
        ni "I fucking hate you."

    $ renpy.end_replay()
    $ niki_love += 1
    $ nikidate10 = True
    stop music fadeout 7.0

    "{i}Niki doesn’t actually hate you! Her affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label nikidate15:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "I know it’s a bit of a long shot trying to get her to hang out this late at night, so I am prepared for the worst."
    "Just...the “worst” in this case is simply calling someone else and seeing what they’re up to instead."
    "And, in the event that I am unable to go the rest of the night without the color pink, I’m pretty sure Noriko should be working. And she always accepts my presence."
    "I guess this scientifically proves which Nakayama likes me more."

    play sound "phonebeep.wav"

    q "Hello. Niki Nakayama’s phone. This is her manager."
    s "Weird. I could have sworn I dialed her cell number."
    q "You did. Which is why I answered with, “Hello. Niki Nakayama’s phone.”"
    s "You don’t sound like Niki at all."
    q "I’m- Are you even paying attention?"
    s "Do you have any idea who I am? "
    q "I believe your name was...[nikitemp]? "
    s "As much as I admire the tenacity in both of you still calling me that months later, can you put her on the line?"
    q "I’m afraid Niki is-"
    q "Oh. Wait. Hold, please."
    q "{i}Niki, you’re supposed to go on in five minutes. What are you doing here?{/i}"
    ni "{i}Phone. Now.{/i}"

    "I listen as Niki snatches her phone back and sends her manager away."
    "And, in other news, I think I’m higher on Niki’s priority list than her job now."
    "Probably."
    "Okay, maybe not {i}higher{/i}, but at least-"

    ni "Stop calling me at night. I’m famous."
    s "Are you? I had no idea."
    ni "Ha ha ha. Very funny."
    ni "If you can get to the urban district in five minutes, I’ll let you in for free."
    s "Sure, let me just teleport over there really quick."
    ni "Cool. Just say you’re there for me and they’ll let you in."
    s "It’s your concert. Literally everyone is there for you."
    ni "Jesus, why are you so difficult?"
    s "I’m not even doing anything this time."
    ni "Hah...listen- I have to go on stage now or thousands of people are going to be disappointed."
    ni "But if you want to make your way over to the urban district {i}after{/i} the concert, we can hang out in my hotel. "
    ni "I’m in the master suite at the...Grand Tsukioka...whatever or something?"
    s "I feel as if I’ve heard that name before..."
    ni "Grats. Bye, now."
    s "Wait."
    ni "What? What else could you possibly want?"
    s "Just wanted to say good luck."
    ni "Okay, but what do you {i}really{/i} want?"

    if bonus == True:
        s "To know if I should bring condoms or-"
    else:
        s "If I should bring your grandma's bones or-"

    play sound "phonebeep.wav"

    s "...not."

    scene black
    with dissolve

    "Jokes on her. I wasn’t going to bring them anyway."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene nikihotel1
    with dissolve2
    play music "love.mp3"

    "A few hours go by before I make it to the hotel which, as I've finally remembered, is owned by Toriko Tsukioka, a totally real student of mine."
    "Well, I guess it’s owned by her family, technically. But it wouldn’t surprise me if they’d just...give it to her or something if she asked nicely."
    "Oh yeah, and Niki is here too."
    "And...she’s..."

    s "...Is that my shirt?"
    ni "No. Your shirt had a smaller collar."
    ni "And I’d definitely never borrow it and stretch it out to turn it into a more comfortable pajama top."
    s "After all I’ve done for you..."

    scene nikihotel2
    with dissolve

    ni "Yeah. Thanks so much for all of those years of self-doubt. Appreciate it."
    s "It made you a better person, didn’t it?"
    s "Even if you’re looking a little...different now."

    scene nikihotel1
    with dissolve

    ni "Different for most people, sure. But this is the me you had the pleasure of looking at for pretty much half of your life. "
    ni "If anything, I’d think it would be weirder for you to look at the super...showy version."
    s "Ahh, so this is the {i}real{/i} Niki Nakayama."

    scene nikihotel3
    with dissolve

    ni "Yup. But if you take any pictures or say anything to anyone, I’ll chop your balls off."
    s "Afraid of people finding out you wear glasses?"
    ni "Only losers wear glasses. True story."
    s "I imagine tonight will be incredibly boring, then."

    scene nikihotel4
    with dissolve

    ni "I’m surprised you even came, to be honest. I could have sworn you’d be all like, “Ugh. Too much effort. I’ll just stay home.”"
    s "It’s the least I can do after, as you so aptly put it, “All those years of self-doubt.”"

    scene nikihotel5
    with dissolve

    ni "Woah. That was a really nice thing to say by your standards. I’m impressed."
    s "And {i}I’m{/i} impressed by how that shirt manages to stay on you despite being stretched to twice its original size."

    scene nikihotel6
    with dissolve

    if bonus == True:
        ni "Thanks. You know, it actually used to belong to this one guy I would always hook up with back when I was sexually active and less...sexually inactive."
        s "You’re not sexually active unless you’re actually having sex, Niki."
    else:
        ni "Thanks. Even though I won't be a wizard for another two years, I have already learned some of the powers."
        s "Wow."

    scene nikihotel7
    with dissolve

    if bonus == True:
        ni "Does hand stuff not count anymore? I remember that was kind of a big deal when we were growing up."
        s "Was it? Or were you just a nerd who didn’t understand what all of the cool kids were up to until a few years ago?"
    else:
        ni "Hey, is it just me or is your aura changing colors right now?"
        s "Here you go again with all of the annoying spiritual shit again. This is exactly why we broke up."

    scene nikihotel8
    with dissolve

    ni "Oh, yeah. Like you were one of those cool kids, Mr. I’mgoingtospendeverydayatmyneighbor’shouse."
    s "That is an incredibly long last name and sounds nothing like Arakawa."

    scene nikihotel7
    with dissolve

    ni "Oh, that reminds me. What’s a...Nakayarakawayama? "
    ni "Is that just our last names combined?"
    s "I am...assuming you heard that from Noriko."
    ni "In between declarations of how she was going to “steal you from me,” yes."
    ni "Of course, I had to inform her that you are not {i}mine{/i} to begin with."
    ni "And also that I would tell our parents if she even {i}tried{/i} stealing you from me."
    s "But...didn’t you just say-"
    ni "Do you wanna sit? My legs are a little tired on account of that whole “putting on a show for thousands of people” thing."

    if bonus == True:
        s "An idol in her pajamas, sitting on a bed with a known pervert? What would the news outlets say?"
    else:
        s "An idol in her pajamas, sitting on a bed with the one and only huggy boy? What would the news outlets say?"

    ni "Probably some stuff about how I’m a whore. And how I’m unfit to be a role model for [young_girls] and shouldn’t show my face in stadiums anymore."
    s "Woah."
    ni "Yeah. The idol industry’s rough. I had to fight off a PR nightmare once for just calling some actor cute."
    s "See, this is what you get for looking at someone other than me. "
    ni "You’re not even that cute anymore. The only thing you have going for you is your eyes."
    s "That’s not the {i}only{/i} thing I have going for me."
    ni "..."
    s "I’m referring to-"

    if bonus == True:
        ni "I know exactly what you’re referring to. Hand stuff, remember?"
        ni "If that whole thing about Tsukumogami is real, the old trash can in my room is going to come back and haunt me for all of the jizz-soaked tissues I tossed into it back in the day."
    else:
        ni "The decline of collective responsibility in American poltics?"

    s "Well, this conversation took a turn."

    scene black
    with dissolve2

    "Niki turns around and hops onto the bed, moving aside to allow me on as well. "
    "It’s a much nicer bed than the one we slept in at the beach, but that sort of thing is to be expected in a high class hotel room paid for by Niki’s agency."
    "I imagine she stays in places like this all the time."
    "..."
    "I wonder if she ever gets lonely sleeping in rooms like this without the comfort...or {i}dis{/i}comfort of an ex-boyfriend nearby."

    scene nikihotel9
    with dissolve

    s "..."
    ni "..."
    s "I still can’t believe you destroyed that shirt."
    ni "I still can’t believe you’re so upset about it."
    ni "If it will make you feel better, I’ll give you one of my old idol outfits to stretch out and wear around your house."
    s "I can’t imagine Ami would be very supportive of that new wardrobe choice."

    scene nikihotel10
    with dissolve

    ni "Well, then {i}she{/i} can have them."
    ni "She just needs to grow a little more first. She’s still kinda tiny for her age."
    s "Just don’t say that around her. She’ll cry."
    ni "I know, I know. Lots of girls are sensitive about their size."
    ni "She’s adorable, though. And, who knows? Maybe you’ll scar {i}her{/i} into becoming an idol as well?"
    s "Maybe it's not too late for me to become a producer instead of a teacher."

    scene nikihotel11
    with dissolve

    ni "Nah. You wouldn’t like being a part of this industry."
    ni "Too much...thinking on your feet and...reacting to stuff."
    ni "And, at the end of the day, even on days where you made thousands of people smile...things can still feel a little empty."
    ni "You can never form meaningful relationships with anyone because you belong to the people."
    s "Ah. So you {i}do{/i} get lonely, then."

    scene nikihotel12
    with dissolve

    ni "Hm?"
    s "In hotel rooms. "
    s "I was wondering how many times you must have sat in one of these by yourself. "
    ni "Oh, yeah. All the time."
    ni "It’s definitely lonely, but...not a {i}bad{/i} kind of lonely, you know?"
    ni "I really do like my job. And I like focusing on stuff relating to my job. "

    scene nikihotel13
    with dissolve

    ni "It helps...take my mind off of stuff."
    ni "Not that “stuff” is anything {i}bad{/i} anymore."
    ni "It’s just...stuff..."
    s "I see..."
    ni "Yeah..."
    s "..."
    ni "..."

    scene nikihotel14
    with dissolve

    ni "How about you? Do you ever get lonely? "
    ni "Probably not when you’re surrounded by a bunch of [teenage]girls, right?"
    s "I...guess not? I’m not really sure."
    s "Being around them does help me take my mind off “stuff” as well, though."
    s "And none of them steal my clothes, so it’s already better to hang out with them than it is with you."

    scene nikihotel15
    with dissolve

    ni "Well, gee. If I knew you were going to make such a fuss over it, I would have worn something else."
    s "It’s never too late, Niki. "
    ni "Wanna trade? I like the way the one you’re wearing now looks."
    s "Yeah, probably because you stole the only other one I had and turned it into a pajama tarp."
    ni "You want it back?"
    s "That is exactly what I have been saying since you took it. Yes."

    scene nikihotel16
    with dissolve

    ni "Then..."
    ni "How about you come and get it?"
    s "..."
    ni "..."

    scene nikihotel17
    with dissolve

    ni "Mm! Mnch...mlem...chu...nch...hah...ahh!"

    if bonus == True:
        jump nikihotelx
    else:
        ni "I wish...we were...hugging right now!"
        s "Me...too!"

        scene black
        with dissolve

        "Niki and I give into our unearthly desire to hug and, well, hug each other."
        "I let her keep my shirt because I know how much it means to her."
        "On the way home, I step in a puddle and have to walk home with a wet sock."
        "I didn't really have to tell you that, but I wanted to anyway."

        $ renpy.end_replay()
        $ niki_love += 1
        $ nikidate15 = True

        "{i}Niki’s affection has increased to [niki_love]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label nikiinvite1:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "And, of course, I prepare myself for the worst since she is very rarely able to make any time for me given her incredibly busy schedule as a famous person or whatever."
    "In fact, even if she {i}does{/i} answer by some stretch of the imagination, I doubt she’ll be willing to accept an invite over to-"

    play sound "phonebeep.wav"
    play music "remember.mp3"

    ni "Hey. What’s up?"
    s "Oh, you answered."
    ni "What? Were you starting to think I’m too good for you now or something?"
    s "I wonder what would have given me that idea. "
    ni "I would have given you that idea- because I {i}am{/i} too good for you now."
    s "This is a fun conversation."
    ni "It truly is. "
    ni "Anyway, what are you doing right now?"
    s "I’m working up the courage to invite you over, but your idolic presence is so commanding and intimidating that I’m having trouble finding the words."
    ni "Wow, are you actually going to tell me where you live after all of these years away?"

    if bonus == True:
        s "If I say yes, will you come over and have sex with me?"
    else:
        s "If I say yes, will you come over and hug me?"

    ni "What, like now? Fuck off. No."
    ni "I’ll come say hi, though."
    s "You’re actually able to?"
    ni "I’m taking the night off, so yeah."
    ni "Just text me the address and I’ll have my driver take me."
    ni "Oh- and before I forget, is Ami home?"
    s "I...think so?"
    ni "Even better. See you soon."

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve

    "Welp, it looks like Niki {i}is{/i} going to come over after all. "
    "As I type out my address to her, I think to myself about what it must be like to have people willing to wait on your every beck and call."
    "But, then I remember that Ami exists and realize that Niki just isn’t that special after all."
    "No amount of drivers or bodyguards can live up to the calming, yet mildly intimidating presence of a red-haired [niece]."
    "........."
    "......"
    "..."

    scene girlsnightin1
    with dissolve
    play sound "doorbell.mp3"

    "The doorbell rings shortly after I take my shoes off and I pat myself on the back for making it here in time."
    "I can only imagine how Ami would have reacted if she answered the door to find her icon just...standing there."

    play sound "doorbell.mp3"

    ni "Stop monologuing and open the fucking door."
    s "Well, that’s just plain rude."
    n "Sensei! Let us in!"

    "What? Noriko is here too?"

    if bonus == True:
        "I mean, as much as I love the idea of taking both Nakayama sisters’ virginities at once, I didn’t think that would be in the cards today."
        "But, even with the prospect of that being slightly possible, I have now obtained all of the motivation I need to let them in."
    else:
        "What a pleasant surprise! The more, the merrier!"

    play sound "dooropen.mp3"
    scene girlsnightin2
    with dissolve

    ni "Hi. Your neighborhood sucks. "
    s "Thanks. Why did you even need my address if Noriko was coming? She could have just shown you the way."
    n "I didn’t even know I was coming until a little while ago."
    ni "Also, I had no idea that you routinely invited my little sister over to your house."
    s "I mean...I wouldn’t call it {i}routinely{/i}."

    scene girlsnightin3
    with dissolve

    if bonus == True:
        n "This is where Sensei made me into a woman!"
        n "If you guys are gonna have sex, make sure you dig your nails into his back really hard. That's his favorite."
    else:
        n "This is where Sensei does his laundry!"
        n "I know this because there is a secret tube inside of his dryer that sends me one of his socks every time he uses it."

    ni "Very funny. "
    s "I’m confused."

    scene girlsnightin4
    with dissolve

    ni "About what, exactly?"

    if bonus == True:
        s "Why Noriko came. And why she’s carrying your bags. And why I don’t remember making her into a woman or the sensation of her nails against my skin."
        n "Maybe I drugged you? It certainly wouldn’t be the first time."
    else:
        s "Well, the sock thing for starters."

    ni "Ooookay. Now {i}I’m{/i} confused."

    if bonus == False:
        s "Niki it literally just happened."

    ni "The bags just have some stuff I brought over for Ami. Mostly old clothes and extra merchandise that I didn’t have a use for anymore."
    n "And also a bunch of stuff that she bought because she wants Ami to like her."

    scene girlsnightin5
    with dissolve

    ni "Noriko! Shut the fuck up or I’m not paying you for this!"
    n "Yes, Nee-chan. Anything you say. "
    s "You actually bought stuff for Ami? Even I don’t buy stuff for Ami."

    scene girlsnightin6
    with dissolve

    ni "Yeah, well you’re an asshole and I’m a thoughtful and caring person."
    ni "Where is she, by the way? "
    s "She’ll be here any second now. The scent of females probably set off an alarm in her brain and caused her defense mode to start."
    a "Sensei! Are there girls here?! You know how I feel about you inviting-"

    scene girlsnightin7
    with dissolve

    a "Ah! Niki! My queen!"
    a "My mind says attack but my heart says love!"
    ni "Hi, Ami! Are you free right now?"
    a "Me?! Yes! I am always free for you! I will kill for you! Just say the word!"
    n "Uhh...where should I put these bags? They’re getting kinda heavy."
    ni "Wonderful. Because I was hoping that the two of us would be able to get to know each other a little better if that’s okay with you."
    s "Wait, what?"

    scene girlsnightin8
    with dissolve

    ni "What’s wrong?"
    s "I mean...I just expected this to be a more private or personal invitation."
    ni "Private or-"

    scene girlsnightin9
    with dissolve

    ni "Wait- did you think I came here for {i}you?!{/i}"
    s "Well...considering I was the one who invited you..."
    ni "Oh, you sweet summer child. I’m just here to talk to Ami."
    s "Why am I the sweet summer child? I’m supposed to be the protagonist. "

    scene girlsnightin10
    with dissolve

    ni "Well then, Mr. Protagonist, why don’t you make yourself useful and go on a little side quest to the convenience store and get us some snacks while we have a bit of a girls’ night in?"
    a "A...girls’ night with...Niki?"

    scene girlsnightin11
    with dissolve

    n "And Noriko! I’m here too!"
    ni "Do you like french fries, Ami? We stopped at a fast food place before coming over."

    scene girlsnightin12
    with dissolve

    a "I love you! I mean- I {i}love{/i} french fries!"
    s "But surely your love for me outweighs the chance to hang out with Niki and eat fast-"

    scene girlsnightin1
    with dissolve

    a "This way to the living room!"
    a "If I had known you were coming, I would have cleaned up first!"
    s "Didn’t you clean this morning?"

    scene girlsnightin13
    with fade

    ni "I’m sorry, were you not listening when I asked you to run along and leave us alone?"
    s "I was listening. I just assumed it was a joke on account of {i}this being my house.{/i}"
    n "I vote that Sensei stays!"
    s "See? Noriko and Ami both want me to stay."
    ni "Funny. I don’t remember Ami saying anything like that."
    s "It’s Ami. She doesn’t have to say it. It’s just always true. Right, Ami?"
    a "..."
    s "..."

    scene girlsnightin14
    with dissolve

    ni "Well, would you look at that?"
    s "Of all the times to betray me..."
    n "I tried, Sensei. I really did."
    s "Okay, I’ll go. But I’m taking Noriko with me."
    ni "No, you’re not. Noriko’s on the clock."
    n "She’s right. I am but a slave to the machine that is the idol industry right now."
    s "..."
    s "I won’t forget this, Niki."
    ni "Ooooh, so you won’t forget {i}this{/i}, but you’ll forget the five years we dated and how you ruined my life. I’m glad to understand your priorities a little better now."
    s "Hey, in a roundabout way, if it wasn’t for me-"
    ni "If you are about to take credit for all of the hard work I’ve invested into reforming myself, I’m just going to steal Ami and never give her back."
    s "But then who will do the dishes?"
    n "Oh! Me! Me! Noriko will do them!"
    ni "Goodbye, [nikitemp]. Walk slowly, because if you’re back in any less than two hours, I’m not undoing the chain lock."
    s "But the convenience store is only a few minutes-"
    ni "One more word out of you and it’ll be {i}three{/i} hours."
    s "..."
    ni "..."

    scene black
    with dissolve2

    "You know..."
    "This is really not how I planned on tonight going."
    "The next time I invite Niki over, I should make her clarify that she will be spending her time with {i}me{/i} rather than trying to poach my [niece]."
    "I begrudgingly exit the house- but as I glance back inside to see if Ami is maybe having second thoughts about letting me leave, I see nothing."
    "Just an empty space where my [niece] once stood, only to be stolen away by a girl with cotton candy hair."
    "First my shirt...now this?"
    "Ex-girlfriends really are terrifying..."
    "........."
    "......"
    "..."

    scene girlsnightin15
    with dissolve

    ni "Why do you look so nervous?"
    a "Um...because you’re Niki Nakayama and I’m just some random girl who can’t even get a high score on any of your songs in the karaoke booth?"
    ni "Okay, so...that might be who I {i}normally{/i} am. But right now, you can look at me as a...family friend."
    a "That’s...the part that’s hard for me to do, though."
    a "Even if you did date my [uncle] in the past, I don’t think I was really old enough to remember it."
    ni "And I wouldn’t expect you to. But since {i}I{/i} remember you, that’s really all that matters."
    n "Nee-chan owes you a big debt of gratitude for managing to keep Sensei on his feet after all these years."

    scene girlsnightin16
    with dissolve

    ni "I don’t give two shits about whether he’s on his feet or not. I just want to make sure that Ami is doing okay since I...feel bad that {i}he{/i} had to be her guardian."
    a "I’m doing great. I’ve actually never been happier."
    a "It’s true that things were really bad for a while, but we were there for each other when we had to be."
    a "And even if Sensei isn’t the best guardian and I had to get a job because he wouldn’t buy me things, I can tell he loves me."
    a "In fact, I can tell he loves me even more than {i}he{/i} thinks he loves me. "

    scene girlsnightin17
    with dissolve

    ni "That’s kind of just how it is with that guy. Never understood why, but it’s like he’s always kept how he really feels locked up so tightly that it looks more like he feels nothing at all."
    n "Is that why you’ve always bossed him around?"

    scene girlsnightin18
    with dissolve

    ni "I never {i}bossed him around.{/i}"
    n "Nee-chan, you are {i}still{/i} bossing him around. You just kicked him out of his own house so we could talk to Ami."
    ni "There’s a difference between bossing him around and having to make decisions for him! I’m sure Ami knows, but sometimes you {i}have{/i} to push him in a certain direction or he'll just get lost."
    n "And today...that direction was the convenience store."
    ni "..."
    ni "Okay. Maybe {i}that{/i} was bossy."

    scene girlsnightin19
    with dissolve

    ni "But I did it to get closer to Ami, so it was all worth it."
    a "I don’t understand, though...why do you want to get closer to me? It can’t just be because you think Sensei is a bad guardian or that...you want to thank me."

    if bonus == True:
        a "I just did what any other girl in my position would do because...Sensei’s the only family I have now."
    else:
        a "I just did what any other girl in my position would do because...Sensei’s the only client I have."

    ni "But he doesn’t have to be."

    scene girlsnightin20
    with dissolve

    a "Are you trying to marry him?!"
    n "Uhhhhhh..."
    ni "What? No. I’m not even trying to date him."

    if bonus == True:
        ni "I’m just trying to say that I wouldn’t mind if...there was suddenly a third Nakayama sister or something."
    else:
        ni "I’m just trying to say that I wouldn’t mind if...you helped me with my taxes as well..."

    ni "Even if we’re not as close to [nikitemp] as we used to be, he’s still an important part of our lives that’s never going to go away. And Ami deserves a lot more than just him."
    n "Why do you keep calling him [nikitemp]?"
    a "I was wondering that, too."
    ni "Unimportant. "

    scene girlsnightin21
    with dissolve

    ni "I just want to do my part for both an unofficial family member {i}and{/i} one of my biggest fans in letting her know that I’ll always be here for her."
    ni "Even when her [uncle] manages to fuck things up all over again, which he definitely will."
    n "I’ll be here, too. "
    n "Obviously, that’s probably not as cool as my sister saying it, but you really are like family to us."
    a "I...um..."
    a "I don’t really know what to say..."
    a "This is all really sudden and it feels kinda like a dream. "
    ni "Just a...convenient side effect of us growing up in the house next door to your [uncle]. "
    ni "I always wanted to do something like this if we ever wound up walking into your life again, so consider it my way of making amends for not being there earlier...when I wanted to be."
    a "..."
    ni "..."
    a "Are you sure you’re not trying to marry him?"


    scene girlsnightin22
    with dissolve

    ni "Uh...yeah."
    a "Because if you do, I won’t let you use your big sister powers to get rid of me."
    a "Marrying Sensei includes promising to look after me for the rest of my life, as I have sworn to be there for him whether he wants me to or not."
    ni "That’s...fine?"
    a "Don’t get me wrong, I’d still prefer that you {i}don’t{/i} marry Sensei. But if there is going to be anyone I would make an exception for, it’s you."
    a "As long as you also agree to the thing I said, I mean."
    n "What do you think? She seems like she’ll be even higher maintenance as a sister than I am and I {i}still{/i} steal your clothes without telling you sometimes."
    ni "I don’t care how “high maintenance” she is. I just want her to have somebody else to rely on."

    scene girlsnightin23
    with dissolve

    a "Well...I’m not sure {i}how{/i} I’m supposed to rely on you when I’m already happy with how things are..."
    a "But I...would like to see you more, if that’s okay."
    a "I don’t know if I’ll ever be able to look at you as family...but I know that you really do care about my [uncle] and...that I can’t ignore your past with each other no matter how much I want to."
    ni "Why would you want-"

    scene girlsnightin24
    with dissolve

    a "At the end of the day...I’m just happy to have you two on my side. "
    n "Your side as opposed to what?"
    a "Any side that wants to get rid of me."
    a "Sensei is my entire life- and neither of you think that’s a problem."
    ni "I mean...he’s not your {i}entire{/i} life, is he?"
    a "He is. And if either of you two hurt him, I will be very, {i}very{/i} unkind to you."
    a "If you are okay with that...then I’m okay with letting you two in."

    scene girlsnightin25
    with dissolve

    ni "Any objections, Noriko?"

    if bonus == True:
        n "To a life of nothing but pleasing Sensei? Do you even have to ask?"
    else:
        n "Do you even have to ask?"

    ni "I hate that I don’t."
    ni "Besides, I doubt it’s even possible to hurt him at this point."
    ni "If anything {i}does{/i} hurt him, he’ll just rationalize it in whatever twisted way his weirdo brain wants to come up with and come out totally fine within a matter of days."

    scene girlsnightin26
    with dissolve

    a "It’s settled, then! "
    a "From now on, the two of you can come over as much as you like as long as you don’t touch my [uncle]!"
    n "A step in the right direction! Hooray!"
    ni "I’m happy to hear that, Ami. "
    ni "I really hope that the two of us can grow closer."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene girlsnightin27
    with dissolve

    a "Sensei! I have sisters now!"

    if bonus == True:
        n "Welcome home, Onii-chan! Wanna get in the bath together?"
        ni "I don’t think it’s been two hours yet."
        s "And yet the chainlock remains...unchained."
        ni "It has been brought to my attention that I may have been {i}slightly{/i} too bossy to you earlier- and for that, I apologize."
        ni "I will now allow you to continue using your house, but not before retreating to Ami’s bedroom and having her model all of the outfits I bought for her."
    else:
        n "We're going to Disneyland!"

    s "Can I come, at least?"
    ni "No. But you can put on a pot of coffee for us, if you’d be so kind."
    a "Niki bought me clothes! I’m going to be pretty!"
    s "You {i}are{/i} pretty, Ami. "
    a "Not pretty enough!"

    scene girlsnightin28
    with dissolve

    ni "Come on, Ami! Let’s get those clothes off!"
    a "Yes, Niki! Anything for you!"
    s "..."
    n "..."
    ni "NORIKO! BAGS!"
    s "I think you’re being summoned."

    if bonus == True:
        n "Yes. But, before I go, I would like to remind you that sometimes, fantasies don’t do the job and that you have at least one picture of my boobs in your phone to use however you want."
        s "I...certainly do. But why are you telling me this now?"
        n "So that you don’t think of what’s happening in Ami’s room and that you think of me instead!"
        n "I love you, Onii-chan! Forever and ever!"
    else:
        n "Yes. But, before I go, I would like to remind you that there are roughly 750 million pus cells in every litre of milk!"

    ni "NORIKO! GET THE FUCKING BAGS!"

    scene black
    with dissolve

    n "Coming, Nee-chan!"
    s "..."

    "I think it might be time for me to move out."

    $ niki_love += 1
    $ renpy.end_replay()
    $ nikiinvite1 = True
    stop music fadeout 6.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label nikiinvite2:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "And this time, I’m going to clarify that I am inviting her over to hang out with {i}me{/i} rather than my [niece]."
    "Granted, Ami should be off doing other stuff today anyway, so Niki wouldn’t even be able to ditch me if she wanted to."

    play sound "phonebeep.wav"

    ni "Am I bossy?"
    s "Hello, Niki."
    ni "Hi. Am I bossy?"
    s "Well, considering the last time you came over my house, you kicked me out...I’m going to say yes."
    ni "Damn it."

    if bonus == True:
        s "There was also that one time you stole my shirt and decided that it was yours. And when I asked for it back, you made me finger you."
        ni "I did not {i}make{/i} you do that! "
    else:
        s "There was also that one time you stole my shirt and decided that it was yours. And then when I wanted it back you made me take you to small claims court."
        ni "That last part never happened!"

    s "That’s not how I remember it. "
    ni "Shut the fuck up."
    s "See? You’re being bossy again right now. "
    ni "You fucking-"
    ni "I was talking about my vocal coach. She quit today because, apparently, I’m too bossy. "
    s "Aren’t you a vocal coach? Just teach yourself."
    ni "You’re a fucking idiot. I’m coming over."
    s "I’m getting mixed signals right now."
    ni "Well, we’ll fucking...unscramble them or whatever when I get there. Bye."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "Well, I forgot to have her confirm that she’s coming over for {i}me{/i}, but I guess that with Ami being gone, there’s no one else she {i}can{/i} be there for at the moment."
    "Unless, of course, she brings her sister again."

    if bonus == True:
        "Which, if that’s the case, it once again ignites the fire that is my passion to have sex with two Nakayamas at once."
        "Here’s hoping that fire burns bright tonight."
    else:
        "Which, if that’s the case, I hope I have enough time to clean up the house first."

    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene nikicouch1
    with dissolve
    play music "comfort.mp3"

    ni "Hi. Now, about me being bossy-"
    s "No Noriko tonight?"

    scene nikicouch2
    with dissolve

    ni "Excuse me? Am I not good enough for you anymore? You require the smaller version with shitty taste in fashion as an added bonus? Give me a fucking break."
    s "Jeez. If I had known you were in such a bad mood today, I wouldn’t have invited you over."
    ni "Oh please. I drove {i}myself{/i} here- and I probably would have done that whether you invited me or not."
    s "You have a car?"
    ni "I have three cars. I’m famous. "
    ni "Technically, I’m not the title holder of any of them. They belong to the agency. But they’re still {i}mine{/i}."
    s "Cool. This means I don’t have to take the bus anymore."

    scene nikicouch3
    with dissolve

    ni "Oh, so I’m your chauffeur now? Fantastic. What a huge step up from the most popular public figure to ever emerge from Kumon-mi."
    ni "Do you have Netflix?"
    s "Are you going to see if my [niece] wants to watch a movie?"
    ni "Is she here?"
    s "She is not."

    scene nikicouch4
    with dissolve

    ni "Good. I wanted to be alone. I missed you."
    s "And I thought {i}Yumi{/i} was tsundere."

    scene nikicouch5
    with dissolve

    ni "Who the fuck is Yumi?! Are you cheating on-"

    scene nikicouch6
    with dissolve

    ni "Oh. Right. We’re not dating anymore."
    s "Yeah. And it’s probably good that you remind yourself of that before you say anything else embarrassing."
    ni "Shut up. I hate you. Let’s watch a movie or something."
    s "Yes, dear. Let me just put on the kettle and check our joint bank account first."

    scene nikicouch7
    with dissolve

    ni "That’s not funny."
    s "Would it be funnier if we {i}were{/i} dating?"
    ni "Do you want to?"
    s "..."

    scene nikicouch6
    with dissolve

    ni "Just kidding. Where do you keep the remote?"
    s "..."

    scene black
    with dissolve2

    s "Right on the table..."

    "Girls are confusing."

    if bonus == True:
        "Especially girls that spend their entire life waiting on you despite you being a heaping pile of shit who takes advantage of girls while they sleep."
    else:
        "Especially ones like Niki who always steal clothing and then force you to rack up millions of yen in legal fees trying to get your stuff back."

    "Just kidding."

    if bonus == True:
        "I didn’t do anything."
        "I’ll never do anything."
        "..."
        "Not until I’m supposed to."

    play sound "static.mp3"
    scene nikil1 with flash
    scene nikil2 with flash
    scene nikil3 with flash
    scene nikil4 with flash
    scene nikil5 with flash
    scene nikicouch8 with flash
    stop sound

    "It feels a little different being alone with Niki than it does...pretty much anyone else."
    "You’re free to call it lingering history if you want, but there’s just something about her presence that makes me feel..."
    "“Safe” isn’t the right word."
    "Nor is “comfortable.”"
    "But I feel a little closer to existing than I normally do when I’m with her."
    "Then again, it could always be something a little more primitive than that."
    "I’ve heard in the past that the sense that will whack you over the head with nostalgia harder than anything else out there is scent."
    "Maybe it’s {i}that{/i} that’s causing me to feel the way I do?"
    "And while I can’t pinpoint {i}where{/i} I’ve felt this way before, I know I’ve felt it- which is more than I can say for most things or situations."
    "So as the two of us sit shoulder to shoulder on this couch, watching a series of moving pictures combining to tell a partially intelligible story, I think about the past."
    "Just, there’s nothing there."
    "I attempt to envision a younger version of Niki."
    "But again-"
    "There’s nothing there."
    "And it’s almost as if I never existed at all."
    "And that whatever scent brought on the prospect of me actually being {i}anywhere{/i} is all just a lie."
    "I should focus on the television."

    if bonus == True:
        ni "Oh. They’re having sex."
    else:
        ni "Oh. They’re hugging."

    ni "That means someone is going to die soon."
    ni "That’s like, rule number one of horror movies."
    s "..."

    scene nikicouch9
    with dissolve

    ni "Do you remember that time you came to sleep over and we stayed up all night, watching Friday the 13th under the covers?"
    s "What do you think, Niki?"

    scene nikicouch10
    with dissolve

    ni "Aww, really? That one’s gone too?"
    s "They’re all gone. There’s nothing there anymore."
    ni "Man. That was such an awesome night. It was like {i}right{/i} before we started dating and our hands kept touching and it was so sweet and awkward and now thinking about it makes me want to die."

    scene nikicouch11
    with dissolve

    ni "Not like, sad dying, though. Embarrassment dying. Like it’s just...really cringey and- oh. Yup. They’re definitely dead now."
    s "Your tangent made us miss the murder. Who knows when the next-"

    scene nikicouch12
    with dissolve

    if bonus == True:
        ni "Look. More people having sex. I bet they’re next."
    else:
        ni "Look. More people hugging. I bet they’re next."

    s "Wow. People who write horror are really just...not that impressive, are they?"
    ni "Not this kind, at least. But that’s what makes slashers fun. You always know what’s going to happen, so you never really get jump scared or anything."
    ni "Fucking jumpscares. Such a lazy form of horror, don’t you think?"

    play sound "imscared.mp3"
    scene tree3 with flash
    scene nikicouch12 with flash
    stop sound

    s "I agree wholeheartedly. But I’ve never really been a big fan of horror to begin with."
    ni "What are you talking about? Yes you have. You used to love this stuff."
    s "Oh. Well, not the version of me that I’m familiar with. But it’s not like my memories are that “full” yet. So who knows what’ll happen in the future?"
    ni "You’re weird. "
    s "That’s a fair assessment."

    "The two of us continue to sit there watching the movie and-"

    if bonus == True:
        jump nikicouchx
    else:
        "It's actually a pretty good movie."

        $ renpy.end_replay()
        $ nikiinvite2 = True
        $ niki_lust += 1
        stop music fadeout 5.0

        "{i}Niki’s lust has increased to [niki_lust]!{/i}"
        "{i}You can now invite her over after[school] and on weekends!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label nikilovesyou1:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "And given that mornings are really the only time I can reliably see her, I’m looking forward to a rather peaceful and jovial conversation."

    play sound "phonebeep.wav"

    ni "Die."

    "My hopes are shattered and my day is ruined."

    s "What did I do to deserve this?"
    ni "Uhh, well, to {i}start-{/i} you completely fucking ditched me on Christmas. Does that ring any bells?"
    s "No, but it does {i}jingle{/i} some."
    ni "I’m hanging up now."
    s "Wait, stop. I want to see you."
    ni "Ooooh, okay! Yeah! Because I’m yours to just leave on hold until you’re done wandering around with everyone else! Sounds great! See you in ten?"
    s "Niki, come on."

    play music "starvingtodeathoutofreachofthesun.mp3"

    ni "Who turns down a date with a superstar?! You know damn well how big of a deal I am now! I had a blue check mark before they were uncool and easily obtainable!"
    s "And I’m very proud of you for that even if I don’t know what it means. "
    ni "I thought we were going to spend that day together!"
    ni "And sure you may have technically never...{i}said{/i} that, but you sure as hell didn’t stop me when I spent a month and half talking about it and planning things out!"
    ni "If you knew you weren’t going to come, why did you let me get my hopes up?! I canceled my Christmas concert for you!"
    s "Your concert wasn’t canceled, though. I watched it on TV with the girls."
    ni "I {i}un-{/i}canceled it when Noriko told me about your stupid fucking party. So unless you’re calling me to apologize for that, I don’t want to hear it."
    ni "Also, I know damn well that you “watching it” means it was probably just on in the background while you were being a fucking tool or something."
    s "That’s true, but everyone else really seemed to like it."
    ni "{i}Hah...{/i}Goodbye, [nikitemp]. I have things to-"
    s "I would have gone with you if I had the choice."
    ni "..."
    s "..."

    "There’s a silence on the other end of the phone as Niki attempts to figure out what that means. "
    "But I’m sure she’s not going to immediately jump to the possibility that there was a two-month gap in time, so I know I’m going to have to explain myself."
    "Which, apart from feeling like the choice was made for me, is probably the reason I called her in the first place."
    "Maybe, buried somewhere in the back of my mind, I was {i}also{/i} looking forward to spending Christmas with her."

    ni "..."
    s "..."

    "Or maybe that’s just me rationalizing why something else I’ve done has led to someone getting hurt again."
    "Even if this wasn’t entirely my fault."

    ni "What does that mean...“if I had the choice?”"
    ni "Are you not an adult? Can you not make your own decisions?"
    s "Something...happened. Something complicated. "
    s "But I’ll make it up to you. We can go on a date today. An {i}actual{/i} date, not another...sausage-focused breakfast trip."
    ni "I can’t {i}go{/i} on actual dates. I’m an idol, remember? I’d be crucified if anyone saw us."
    s "But we’ve been to that restaurant-"
    ni "We’ve been to “that restaurant” because I rented the entire place out. And, despite how it may seem, I’m not always 100%% willing to go to the moon and back for you."
    s "Then...you can come here. Or I can come there. I don’t know."
    s "But I want to see you."
    ni "..."
    s "..."
    ni "I look like shit, just FYI. I haven’t been sleeping well."
    s "Why not?"
    ni "Because loving someone without being loved back is a lot harder than you think. "
    s "Niki-"

    play sound "phonebeep.wav"

    ni "This address. Be there in one hour. If you’re not, I’m deleting your number from my phone and then throwing it into the ocean."
    s "There’s no need to delete my number if you’re just going to throw your phone into the-"

    play sound "phonebeep.wav"

    s "...and, she’s gone."

    scene black
    with dissolve2

    "I really would have gone with her if I had the chance."
    "It was difficult to say in the moment since there were two other girls there beckoning the same exact gesture out of me, but..."
    "Niki was there first."
    "Not just that day, but in general."
    "She’s been there from the start and even if there are parts of me that don’t {i}specifically{/i} remember what makes our relationship so different- I know it is."
    "And I know that there must be a future out there where I do more than just disappoint her every waking hour of every day."

    s "..."

    "I’m just not sure if {i}this{/i} is that future."
    "But there are several things in life that I’ve accepted I will never understand-"
    "One of them is what it takes to move forward."
    "Another is what happens when I get there."

    "........."
    "......"
    "..."

    scene nikitired1
    with dissolve2

    s "A playground?"
    ni "I {i}want{/i} to say I picked a place where you wouldn’t hit on anyone else but, honestly, who the fuck even knows at this point?"
    s "Just...going to ignore that. You look-"
    ni "Horrible? Exhausted? I am. Thanks for noticing. And thanks for drawing attention to it."
    s "You’re not going to make today easy for me, are you?"
    ni "I’ll become nicer as the day goes by. You’ve already managed to earn yourself a few points by not making me wait. "
    s "I did it for your phone. As someone paying for several concurrently, I understand how expensive replacing them can be."
    ni "How very generous of you. "
    s "I’m sorry about Christmas, Niki."

    scene nikitired2
    with dissolve

    ni "Same. That’s two Christmases in a row where I would have let you fuck me only to find out you’d rather mingle with a bunch of teenagers instead. Hope they liked the show."
    s "If it’s any consolation, there are very few things in life that I would rather do than fuck you."
    ni "Join the club. "
    ni "Like, really. There’s an actual club for that. “Let me fuck Niki Nakayama” on Facebook or something. Depressing amount of members. And here {i}you{/i} are, squandering the opportunity."
    s "If you really do know me as well as you say, that shouldn’t come as much of a surprise. You and Noriko have both made it sound like I’ve been kind of an asshole for...basically forever."

    scene nikitired3
    with dissolve

    ni "You have. But that doesn’t mean it isn’t still a fucking pain in the ass."
    ni "Do you really think I’d keep giving you chances if I didn’t at least {i}kind of{/i} understand what it is that makes you tick? Fuck no. Not in a billion years."

    scene nikitired4
    with dissolve

    ni "But you’ve gotta give me a fucking {i}break,{/i} {b}[[REDACTED ~ NOT YET READY]{/b}. "
    ni "Loving you as much as I do is {i}hard.{/i} And it’s like every single step you take is in the wrong direction, and that makes {i}me{/i} have to turn around all the time just so you don’t get lost."
    ni "You’ve gotta give me {i}something.{/i} A {i}single{/i} step toward the future. I’m doing all I can here."
    ni "It’s not even about me. I’m worried about {i}you.{/i} "
    ni "Ever since {b}[[REDACTED ~ MORE UNNECESSARY INFORMATION]{/b}, you’ve been a fucking blubbering mess."
    ni "I get that you probably {b}[[REDACTED ~ UNIMPORTANT]{/b}, but it’s time to move on. You can’t just stay a teenager forever because you’re afraid of growing up. Do you understand?"
    s "..."

    scene nikitired5
    with dissolve

    ni "..."
    ni "I’m sorry. "
    ni "I’ve been holding that in for a while, but it’s mostly just me being mad. I didn’t mean it."
    s "It’s fine if you did. "
    s "There aren’t many people who’ve been as straight with me as you were just now."
    ni "There aren’t many people who understand you. And, not gonna lie...you don’t make it easy."

    scene nikitired6
    with dissolve

    ni "But we’re {i}friends{/i} before anything else, you know. "
    ni "That’s how this all started, after all."
    ni "Just...two kids who met by chance one day."

    scene nikitired7
    with dissolve

    ni "She was a bossy nerd who spent all of her free time watching cartoons...and he was a quiet boy who always looked like he was one step away from being snapped in half."
    ni "At first, he made her feel a little uncomfortable. "
    ni "But the more she saw him here, the more she knew she was going to wind up being responsible for him one way or another."
    s "{i}Here?{/i} So...this is-"

    scene nikitired8
    with dissolve

    ni "Mhm."
    ni "This is where it all began."
    ni "And if you didn’t show up today, it’s where it would have ended."
    s "..."
    ni "..."
    s "I’m here, Niki."
    ni "Yeah..."
    ni "You are..."
    ni "And still one step away from being snapped in half all these years later..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nikitired9
    with dissolve2

    s "Where are we now?"
    ni "A hill."
    s "No deeper meaning to it this time? Not the hill where we first held hands or something to that effect?"
    ni "I think you fingered me here once. But other than that, I don’t think it’s particularly important. Nice view, though."
    s "Yeah...you can’t even see the wall from here."
    ni "Feels like it’s visible pretty much everywhere nowadays, doesn’t it? Makes you realize how trapped we are."
    s "I’m sure you have ways of getting out. You’re a famous pop-star and all. The world outside of Kumon-mi needs you."
    ni "There are other Niki Nakayamas in other parts of the world. I’m sure they’ll be fine. "
    ni "There’s somebody I’ve gotta stay here and look after anyway."
    s "You don’t {i}have{/i} to, Niki. I’ll get by on my-"
    ni "Hm? I’m talking about Noriko, obviously. You can go fuck yourself."
    s "Wow. Okay. Fuck you too, then."
    ni "Haha! I’m kidding, calm down. Noriko’s way more independent than you. She’ll be fine on her own."
    ni "I give her a lot of shit since she’s my sister, but I really do think she’ll wind up an amazing woman someday."
    s "I...think so too. She really amazes me sometimes."
    ni "I’d be surprised if she didn’t. She tries harder around you. Always has, always will. "
    ni "But I guess that’s to be expected when you’ve been filling the “cool older brother” role in her life ever since she was little. “Cool” being a word I’m using lightly, of course. {i}I{/i} don’t think you’re cool at all."
    s "Were we ever like that?"
    ni "Like what? Siblings?"
    s "Yeah."
    ni "Mmm...no. Not really."
    ni "There may have been a short period of time where I felt like an older sister to you, but it didn’t last long. Especially when I found out you were older than me."
    ni "We’ve always been close, though. Other people from the neighborhood would always tell me how weird it was when they’d see me walking around without you. Not sure if you ever got that."
    s "Not sure if I’d remember even if I did."
    ni "Yeah...there’s that too."
    s "..."
    ni "..."
    ni "You know, Noriko’s a lot older now. If you’re starting to feel a little differently about her-"
    s "Are we really doing this?"
    ni "Hold on. Let me finish."
    s "There’s no possible way that topic can end on a good note."
    ni "Why not? You’re not already messing around with her, are you?"
    s "Niki-"
    ni "Oh my God, relax! I’m kidding."
    ni "I’m just saying...she’s still in the process of learning how to see you as something other than a brother...but it’s okay if you start to see her as a woman, you know."
    ni "She’s not going to be a kid forever. She barely even copies me anymore. She’s her own person and deserves to be treated as more than my little sister."
    s "..."
    ni "I really love her. Like, a lot. "
    s "I can tell...I can’t wait to let her know you said that."
    ni "Please don’t. It’s still embarrassing even if it’s true. "
    s "Why bother telling me then? You know I’m just going to tease you about it."
    ni "{i}Because,{/i} {b}[[REDACTED ~ REPEATED USAGE OF PROHIBITED WORD]{/b}, you’re one of the few things in this world that can actually hurt her."
    ni "Even if she’s strong, she’s still growing. And since she’s in the process of finding herself, it means there are going to be a bunch of pieces scattered around that she needs to collect."
    ni "I’m sure some of those pieces are in your hands...and that’s why I feel like it’s my duty to tell you, as her sister and {i}not{/i} your psycho ex-girlfriend-"
    s "Don’t hurt her. Got it."
    ni "Not that. Well, yes that. But there’s something more as well."
    ni "{i}Help{/i} her. "
    ni "Even the most independent of us need a hand from time to time. Noriko’s amazing, but she’s no exception to that. And there are things you can do for her that I simply...can’t."
    ni "It sucks, but it’s the truth. "
    ni "The two of us have watched you forever. You’ve helped both of us learn all sorts of things about ourselves without even trying."
    ni "I’m old and decayed and set in my ways at this point, but she’s still young and full of life. And now that you’re back, she’s following your lead again."
    s "You’re 29, Niki. You’re not “decayed.”"
    ni "Maybe not {i}physically,{/i} but my brain is fried from having to balance all of this idol stuff with all of this {i}you{/i} stuff."
    s "Is my existence really causing you that much stress?"
    ni "Oh {i}fuck{/i} yeah. I found a grey hair last week and cried for twenty minutes. But that’s more on me than it is on you."
    ni "I just want you to be happy. That’s all. "
    ni "It doesn’t have to be {i}with me{/i} if you don’t want it to be."
    ni "I love you — and I don’t mean that in a romantic way this time. "
    ni "Please talk to me if there is ever anything you need. "
    s "Anything?"
    ni "If you ask me for a blowjob right now, I swear to God."
    s "I mean...if you’re offering..."
    ni "{b}[[REDACTED ~ FURTHER OFFENSES MAY RESULT IN UNEXPECTED SIDE EFFECTS. PROCEED WITH CAUTION.]...{/b}"
    s "I’m kidding."
    s "I’ll try and lean on you a little more, but don’t blame me if a lot of it sounds crazy because it most assuredly will."
    ni "I’ve been unhealthily obsessed with the same boy for like two thirds of my life. I can handle crazy. "
    s "Well, I wouldn’t blame you if you couldn’t. A lot of what’s been happening to me lately isn’t really all that believable."
    ni "Only one way to find out, I guess."
    s "..."
    ni "..."
    ni "Thanks for calling me today. This is the most productive talk we’ve had ever since...you know."
    ni "Between all of the panic attacks and migraines you give me on a weekly basis, it’s easy to forget how nice the good times can feel."
    ni "And how so many of the best moments in my life have been little things like this — where the two of us just sit under a tree and...talk."
    s "..."
    ni "We’ve come a long way, haven’t we?"
    s "Seems like it."
    ni "Growing up kind of sucks, huh?"
    s "Everything sucks. Accepting that is the first step of obtaining true adulthood."
    ni "Said the perpetual manchild to the thirty-year old virgin."
    s "Hey, you’re not thirty yet. There’s still time."
    ni "Pfft. Yeah, sure. I’m starting to think I’ll die a virgin at this rate."
    s "Not if I have anything to do with it."

    $ renpy.end_replay()
    $ nikilovesyou1 = True

    jump nikilovesyou2

label nikilovesyou2:
    if _in_replay:
        play music "starvingtodeathoutofreachofthesun.mp3"

    scene memorylane1
    with fade

    ni "{i}Do{/i} you have anything to do with it? Because it seems to me like you keep selecting other heroines instead. "
    ni "Who knew the woes of the childhood friend route applied to real life as well?"
    s "You’re starting to sound like a certain Irish girl I know and I can’t say I’m a fan of it."
    ni "Just remember that if you {i}do{/i} continue rejecting my advances, there is an entire Facebook group of people willing to sleep with me. And most of them would probably pay."
    ni "{i}You{/i} get the first-love discount. That’s a once in a lifetime promotion, you know."
    s "Oh, I know. And I’ll be sure to capitalize on it once everything surrounding our relationship stops being so damn depressing."

    scene memorylane2
    with dissolve

    ni "Ugh. I really am going to make it to thirty after all."
    s "..."
    ni "..."

    "Another bout of a certain brand of silence, one that I am beginning to recognize like the back of my hand, carries across the outstretched horizon before planting itself firmly in my lap."
    "It curls up into a ball of intangible warmth and fills me with a dreadful nostalgia that I attempt to wish away by focusing on the head resting upon my shoulder."
    "I wonder if this warmth has invaded her as well — and if the thoughts inside her head at this very moment add up to more than just “I’m happy here.”"
    "Are you?"
    "Happiness is tricky — confusing. And people like me who have grown so disenchanted by the pursuit of it approach the word with extreme caution so as to not {i}think{/i} we’re happy when we’re not."
    "So many good things have happened to me lately."
    "And if that is any indication of what is yet to come, I’d be a fool to not admit I’m terrified as there must always be a balance."
    "What goes up must always come down —but that comes with a caveat."
    "There are things you’ll see and experience in life that will push you further down into the bottomless pit of existence than you’d ever fall on your own."
    "And while there may be people who notice you screaming and begging for help — who take it upon themselves to lend you a hand and attempt to pull you up, no one will ever pull you {i}out.{/i}"
    "In the end, you either drag them down with you or let go and hope they never meet the same fate."
    "It will always be easier to fall than it will be to climb. "
    "And when you’ve fallen as deep as I have, the last thing you possess is the willpower to fight back against fate."
    "So you fall...and fall...and fall forever-"

    ni "I love you so much."

    "And pray that the slowly vanishing light at the top of the well never fully disappears."

    s "..."
    ni "..."
    s "I...love you too, Niki."
    s "Thanks for trying to pull me out of my bottomless pit."

    scene memorylane3
    with dissolve

    ni "It’s that or I jump in there with you. Better to suffer together than to suffer alone, right?"
    s "You don’t deserve to suffer."
    ni "Neither do you."
    s "I do, though. I’m probably not the same person I was when I was with you. A lot has happened since then and I’ve done...a lot of horrible things."
    ni "You can always change."
    s "See, that’s the thing...I don’t {i}want{/i} to. And I have no idea what type of person I’d be if I {i}did.{/i}"
    s "I’ve become the worst parts of myself...I’ve accepted them. And getting rid of those traits would be more like me turning into a new person than turning over a new leaf."
    ni "Then, I hope that bottomless pit of yours is wide enough for two."

    scene memorylane4
    with dissolve

    s "Niki-"
    ni "No matter what you’ve done or what you’ll {i}do,{/i} I’ll be right there with you. "
    ni "You chose a really stubborn person to spend so much time with way back when. This is the result of that."
    ni "You’re too weak to function on your own. Plus, it’s not like I have to {i}agree{/i} with all of those “horrible things” you do, right?"
    ni "You need someone to call you out on your shit — and who better than the girl who’s dealt with more of it than anyone?"
    ni "You’re not like this because you’re a bad person, you’re like this because you never learned how to be a good one. "
    ni "{i}It’s not your fault.{/i}"

    scene memorylane5
    with dissolve

    s "That...doesn’t make it okay."
    ni "Never said it did...just that I’ll always be your home when you have nowhere else to go."
    s "..."
    ni "..."
    s "I wish I remembered more of our past together."
    s "I don’t understand why I ever would have left you behind."
    ni "You left me behind because you’re a selfish asshole who's never been able to grasp the fact that there are other people out there struggling as well."
    ni "But you’re back now. And that’s what matters most."
    ni "We’ll return your memories one way or another- even if I have to force them in myself."
    s "Yeah? And how would you do that?"
    ni "..."
    s "..."
    ni "You don’t have any other plans for the rest of the day, do you?"
    s "I don’t."
    ni "Then...let's go for a walk-"

    stop music
    scene memorylane6
    play sound "broken.mp3"

    ni "[[REDACTED ~ REPEATED USAGE OF A PROHIBITED WORD HAS RESULTED IN A FATAL ERROR]"

    scene black
    stop music

    "////////////////PLEASE NOTE THAT RESTARTING YOUR DEVICE BEFORE AN UPDATE IS COMPLETE MAY RESULT IN IRREPARABLE DAMAGE"
    "........."
    "........"
    "......."
    play sound "static.mp3"
    scene somethinglikethis with flash
    stop sound
    play music "glasswalker.mp3"

    "One's grand flights, one's Sunday baths,"
    "One's tootings at the weddings of the soul"
    "Occur as they occur. So bluish clouds"
    "Occurred above the empty house and the leaves"
    "Of the rhododendrons rattled their gold,"
    "As if someone lived there. Such floods of white"
    "Came bursting from the clouds. So the wind"
    "Threw its contorted strength around the sky."
    "[[BREAK]"
    "Could you have said the bluejay suddenly"
    "Would swoop to earth? It is a wheel, the rays"
    "Around the sun. The wheel survives the myths."
    "The fire eye in the clouds survives the gods."
    "To think of a dove with an eye of grenadine"
    "And pines that are cornets, so it occurs,"
    "And a little island full of geese and stars:"
    "It may be the ignorant man, alone,"
    "Has any chance to mate his life with life"
    "That is the sensual, pearly spouse, the life"
    "That is fluent in even the wintriest bronze. "

    play sound "static.mp3"
    scene ayhh12 with flash
    scene ayhh1 with flash
    scene ayhh3 with flash
    scene specialsky with flash
    stop sound

    "There is a disconnect between that which is real and that which is not — but that disconnection is not one to be perceived by man."
    "It is visible to only those with the eyes of God and those who, in the moments of utmost unholiness, spill liquid sacrament from their pores and tongue."
    "There is a trip to be traveled through unmapped parts of the world."
    "You will see things that happened and didn’t."
    "You will feel things you will never feel again."

    play sound "static.mp3"
    scene roofnoon with flash
    stop sound

    "{b}{size=+20}AND YOU WILL SAVOR THE SPLENDOR IN EVERY SECOND{/b}{/size}"

    play sound "static.mp3"
    scene roofday with flash
    scene roofnoon with flash
    scene roofday with flash
    scene roofnoon with flash
    scene roofday with flash
    scene roofnoon with flash
    scene memorylane7 with flash
    stop sound

    "A walk upon glass through a forest untouched brings us several steps closer to a dance with our mirrored selves."
    "As my eyes connect with a conveyor belt of shadows and familiar unfamiliar faces, it is my legs that wind up moving while the world around me does not."
    "If I could break myself in two and reform with wings I would — but as I’ve never learned to fly, I must grapple with an unbearable truth and squeeze the life from out its body."
    "This is then and this is now."
    "I remember how to make my heart move."

    ni "Do you remember where we are?"
    s "..."
    ni "Would it help if I gave you a hint?"
    s "I can’t really put my finger on it, but..."
    s "I know I’ve been here before."

    scene memorylane8
    with dissolve

    ni "We built a secret base here out of stuff we picked from trash cans."
    ni "We filled it with snacks from my pantry and pretended we were an underground crime-fighting organization."
    ni "Any time we heard a noise, we’d hide behind trees and wait for some evildoer to move through the woods, but no one ever came."
    ni "It was a huge waste of time looking back on things if you don’t count all of the comics we read here as “being productive” but holy shit were we always so excited to come."
    ni "Things stopped being as exciting once Noriko found out about it and we began spending less and less time here as the days went by."
    ni "As you can see, there’s nothing left now...but this place was once really important to us."

    scene memorylane9
    with dissolve

    ni "Ring any bells?"
    s "..."
    ni "Then..."
    ni "How about this-"

    play sound "static.mp3"
    scene memorylane10
    with flash
    stop sound

    ni "We spent a lot of time in the woods when we were younger...but I never really realized it until I stopped going outside."
    ni "This was another spot we loved. Not far from here, there was a hidden path that led to a circle of abandoned gassho houses we’d sneak into to make out."
    ni "It feels like just yesterday we were carving our names on that tree."
    ni "Sucks I wound up coming back to scribble yours out after you left me all alone."

    scene memorylane11
    with dissolve

    ni "Do you have your keys on you? Maybe we could make a new carving?"
    s "You’re still interested in things like that?"
    ni "Oh, come on. Don’t tell me you’re so dead inside that you’re against a little {i}vandalism{/i} now?"

    "My feet are cut deeper as the forest pulls us closer to its core."
    "And while images of the past break their legs trying to run through the four corners of my mind, I see nothing but an endless blur and {i}feel{/i} nothing but the blood soaking into my socks."
    "The one sense that does not deceive me is my hearing as I can faintly make out the sound of a pocket knife being plunged into the flesh of an ancient tree."
    "We’d peel away its skin and replace it with a dream — false hopes in the form of a relationship that would one day perish only to be resurrected by sheer coincidence years later."
    "The rest begins to flow back in."
    "How small her hands were back then."
    "The way her glasses would fog up when it got too hot."
    "Her long, pink hair that would stick to my clothing and get me into trouble with-"

    play sound "static.mp3"
    scene memorylane12
    with flash
    stop sound

    "No. "
    "Stop remembering."

    ni "[[REDACTED]?"
    se "Hmm...how come {i}we{/i} never carved our names into a tree? That would have been cute."
    s "..."
    se "Hellooooo? Anybody home? You can’t just pretend you don’t see me. I know you do."
    ni "Hey, what’s going on? Are you remembering something?"
    se "{i}Hah...{/i}obstinate as ever, I see. And Niki, wow! She’s so pretty now! I can’t help but feel a little jealous."
    se "Are you two together again?"
    se "Does she {i}fuck{/i} you like I did? "
    se "Who’s better, me or her? "
    se "Be honest. I won’t get mad."
    ni "Hey. Talk to me. What’s-"
    s "I remember this place."

    play sound "static.mp3"
    scene memorylane13
    with flash
    stop sound

    ni "What? You do?"
    s "Yeah. We would come here...and there was a...circle of houses and...we would make out..."
    ni "Yeah, but...you’re kind of just repeating what I said a couple minutes ago. Are you really sure you remember? "
    ni "Be honest. I won’t get mad."
    s "More..."
    s "I need to see more..."
    s "Take me somewhere else..."

    scene memorylane14
    with dissolve

    ni "Okay..."
    ni "We’ll go on an all-inclusive tour down memory lane..."
    ni "From where it all began..."

    play sound "static.mp3"
    scene 1 with flash
    scene 2 with flash
    scene 3 with flash
    scene 4 with flash
    scene 5 with flash
    scene 1 with flash
    scene 2 with flash
    scene 3 with flash
    scene 4 with flash
    scene 5 with flash
    scene memorylane15 with flash
    stop sound

    ni "To where it all ended."
    s "Huh?..."
    s "Where..."
    s "Where are we?..."
    ni "I think it’s better if you remember this one without any help."
    ni "This place had a much more profound impact on you than it did on me, after all."

    "Before this, there were other places."
    "A convenience store where we’d stop on the way to school."
    "An old bus stop where we’d wait for over an hour sometimes for a ride into the urban district."
    "An Italian restaurant we never went inside, but always talked about how it would be nice to be able to eat there one day."
    "A softball field."
    "A community pool."
    "The yard of an old house where a dog used to live."
    "It’s gone now and a new one has taken its place."
    "Each of these locations spurred something inside of me to begin moving again. And slowly but surely, the faded traces of what {i}should{/i} be mine have opened up to the idea of coming home."
    "So why has that all come screeching to a halt at the end of the tour?"
    "Why am I numb again {i}now?{/i}"
    "Was I just caught up in the moment earlier?...Piggybacking off of Niki’s nostalgia because I’m so desperate for my own?"

    play sound "static.mp3"
    scene memorylane16 with flash
    stop sound

    "Or am I just suppressing something?"

    ni "You jumped."
    ni "Do you remember?"
    s "I..."
    s "I don’t know..."
    ni "Take as much time as you need."
    ni "This is the hardest part of the trip after all. And I’ve already told you-"
    ni "I’ll return your memories even if I have to force them back in myself."

    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane21 with flash
    scene memorylane22 with flash
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane21 with flash
    scene memorylane22 with flash
    scene memorylane23 with flash
    stop sound
    $ renpy.pause(5, hard=True)

    s "This..."
    s "This is where it happened..."
    ni "That’s right."
    ni "This is where your world was ripped away from you."

    play sound "static.mp3"
    scene imissyoumore with flash
    scene everythingg with flash
    scene memorylane24 with flash
    stop sound

    ni "You can’t only open yourself up to the good memories, you have to let the bad ones in too."
    ni "You’ll never move on if you just keep ignoring the things that make you hurt. You have to {i}work{/i} if you ever want to get better. Only then will you be able to look back on the past without breaking into a million pieces."
    ni "But I promise you, and I mean this with {i}all{/i} of my heart, I will be there {i}every...single...step{/i} of the way."
    ni "You’re not alone..."
    s "..."
    ni "{i}Look at me.{/i}"

    scene memorylane25
    with dissolve2

    ni "{i}You’re not alone.{/i}"
    ni "{i}Okay?{/i}"
    ni "No matter how horrible you become...or how much work it takes to get you through a single day without feeling sorry for yourself..."
    ni "I will be here. I’ve {i}always{/i} been here. "
    ni "You’re my best friend in the whole entire world...and I am so...{i}so{/i} sorry you had to go through what you did..."
    ni "But..."
    ni "I don’t want to watch you suffer anymore..."
    ni "I want my friend back..."
    s "..."
    ni "Will you please stop running? Both literally {i}and{/i} figuratively?"
    s "..."
    ni "Please?..."
    s "You really won’t leave?"
    ni "Of course not. Never."
    s "No matter what I become?"

    scene memorylane26
    with dissolve

    ni "No matter what you become."
    s "Why?..."
    ni "Because I’m a fucking idiot."
    ni "But I’m {i}your{/i} fucking idiot. And you’re my big, melancholic doofus. "
    ni "So let’s go be stupid together...far away from the places that make us hurt."
    ni "Let’s go somewhere quiet...and comfortable..."
    s "..."
    ni "{i}Let’s go home, Akira...{/i}"

    scene black
    with dissolve2

    "Akira..."
    "That’s...my name."
    "My name is Akira."
    "..."
    "I’m a good boy."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ nikilovesyou2 = True

    jump nikilovesyou3

label nikilovesyou3:
    if _in_replay:
        play music "glasswalker.mp3"

    scene nikilovesyou1
    with dissolve2

    ni "I’m going to make tea. Do you want any?"
    s "I’m fine."
    ni "Are you sure? Is there anything {i}else{/i} you want? Water? Something a little harder to take the edge off?"
    s "I’m okay. Thank you."
    ni "Okay. I’ll be right back, but make yourself at home. Should be easy since you {i}did{/i} basically live here when we were kids."
    s "Okay..."
    s "Thanks."

    scene nikilovesyou2
    with dissolve
    play sound "dooropen.mp3"

    "After leaving the place where everything went dark, we return to Niki’s childhood home."
    "She collected a key from under the welcome mat to use on the door and said her parents don’t mind if she still crashes here from time to time."
    "They kept her room the same- and while I can’t currently remember its layout from any legitimate memories, I remember bits from when it was forced into my head a little over a year ago."
    "This is where she must have written me those letters — the prison I locked her in when I left her behind."
    "I can only imagine how many tears have been shed on the very bed I’m sitting on — how many times I’ve been cursed and ridiculed without so much as sparing a thought over her."
    "Akira."
    "The name rings out in the back of my head."
    "Who {i}knows{/i} that name?"
    "Ami surely does, yet she’s never said it to me."
    "I’m sure Maya knows too...maybe even Ayane."
    "Have they been saying it all along? Have I been blocking it out?"
    "It’s one word- it shouldn’t make me feel this different."
    "But I don’t deserve a name. I feel {i}real{/i} now. I’m suddenly a person instead of just a title, and...I shouldn’t be gifted something so valuable when everything else is already wrapped around my fingers."
    "The weight of five forbidden letters presses down on my neck and there is nothing I can do but hang my head in response."
    "Something plays on the television, but I can’t focus enough to see what."
    "All I can think is of what will happen next."
    "There is only one way I have ever known comfort — and I am here alone with a girl who wants nothing more than to comfort me."
    "But is {i}this{/i} the way it’s meant to be?"
    "Is {i}this{/i} what she envisioned under luxury blankets in fancy hotels, whispering my name into the dark corner of a room while doing to herself what I was not present to do?"
    "I have never whispered her name."
    "I have never whispered anyone’s."

    play sound "static.mp3"
    scene nikilovesyou3
    with flash
    stop sound

    se "That’s not true. You used to whisper {i}my{/i} name all the time. Just because I {i}made{/i} you doesn’t mean it doesn’t count."

    "I’m seeing things."
    "Things I am not meant to see."
    "This isn’t how it’s meant to be."

    se "I wonder what would happen if you reached out and touched me right now?"
    se "Do you think I’d feel it?...Do you think {i}you’d{/i} feel it?"
    se "You still {i}can{/i} feel, right? You don’t miss me so much that you’re {i}physically{/i} numb now too, I hope."

    "Can you see her too?"
    "Are you even there at all?"

    se "You can’t ignore me forever, Akira."
    se "The harder you try to forget me, the more I’ll want to show up."
    s "..."
    se "Akiraaaa~"
    s "..."
    se "Aki-kun~"
    se "Doff thy name! And for that name which is no part of thee, take all myself."
    se "O nature, what hadst thou to do in hell, when thou didst bower the spirit of a fiend in moral paradise of such sweet flesh?"
    s "You’re mixing monologues..."

    scene nikilovesyou4
    with dissolve

    se "Ah! He speaks!"
    se "Quick, tell me you love me before you fuck your ex-girlfriend. It should be easy. You’ve done it plenty of times before."
    s "..."
    se "Ugh. You’re such a Montague sometimes."

    play sound "static.mp3"
    scene black
    with flash
    stop sound
    play sound "dooropen.mp3"

    ni "Hey, back. Sorry. Slide over a bit."
    s "Yeah...sure."

    play sound "static.mp3"
    scene nikilovesyou5
    with flash
    stop sound

    ni "You sure you don’t want anything? You’re probably dehydrated after walking around all day."
    s "I’ll be fine. But thanks."

    scene nikilovesyou6
    with dissolve

    ni "Okay...You know where the kitchen is if you wind up changing your mind."
    s "..."
    ni "What are you watching? Who’s the girl with the pink hair? And what’s that weird grey stuff they’re eating?"
    s "I don’t know. I haven’t been paying much attention."

    scene nikilovesyou7
    with dissolve

    ni "Do you want to take a nap? I can leave you alone if you want. My parents won’t mind if you stay the night. We’re well past the age where it would be weird."
    ni "And Noriko doesn’t come by much anymore, so you wouldn’t have to worry about her finding you here and getting the wrong idea or something."
    s "{i}Would{/i} it be the wrong idea?"

    scene nikilovesyou8
    with dissolve

    ni "You tell me. You were nearly catatonic on the way over. I’m in big-sister mode right now because I figured I should be gentle, but I can swap back to ex or childhood friend if you like."
    s "Just be yourself. There doesn’t need to be a “mode.”"

    scene nikilovesyou9
    with dissolve

    ni "Uh...maybe “mode” was the wrong way of putting it? It’s not an act or anything. All of those “modes” are real parts of who I am. I just didn’t want to overstimulate you or...something."
    s "..."
    ni "Maybe I should have just made you tea after all?"
    s "I really don’t deserve you, Niki...You’re better than this. You know you are."

    scene nikilovesyou10
    with dissolve

    ni "Better than what? Being there for someone who needs me? Someone I’ve made it {i}pretty{/i} apparent I’d do anything for today?"
    ni "I’m not {i}above{/i} you just because I unlocked compassion in my skill tree and you skipped over that in favor of...penis size or something."
    s "Worthy investment. Compassion gets you nowhere."
    ni "It got you into my room."
    s "It’s equally plausible penis size got me into this room."

    scene nikilovesyou11
    with dissolve

    ni "Pfft...Are you feeling a little better now? Your less miserable side is starting to show."
    s "My head hurts. My legs hurt. I’m exhausted. I’m congested. But on the bright side, I can formulate thoughts again. And that’s a good sign, I guess."

    scene nikilovesyou12
    with dissolve

    ni "You’ve gotta start somewhere."
    ni "Just please forgive me if I start crying once you’re a little more stable. I was holding myself together for your sake and that dam is bound to burst sooner or later."
    s "Please don’t cry for me, Niki. It’s not worth it."
    ni "You know that dude Noah who built the ark to put all those animals on? Pretty sure he did that sometime around when you ran out on me when he caught wind of how much I’d been crying."
    s "Niki-"
    ni "The polar ice caps aren’t actually melting. Sea levels rose because you broke my heart. Global warming really is one big conspiracy."

    scene nikilovesyou13
    with dissolve

    s "I’m really not in the mood to laugh right now."
    ni "Are you ever?"
    s "No. But now I’m really not in the mood."
    ni "Oooh, are you gonna do something about it?"
    s "Not if you’re still in big-sister mode. That would be immoral."
    ni "I’ve moved back into best friend mode over the last several sentences. The transition to ex is still pending."
    ni "Idol-Niki’s not off limits either if that sort of thing will cheer you up."

    scene nikilovesyou14
    with dissolve

    s "I think where you are now is good. Especially since I’m not really sure how I’d even fare around idol-Niki."

    scene nikilovesyou15
    with dissolve

    ni "Ohoho? Not afraid I’d steal your heart with my captivating style and mature brand of wholesome cuteness?"
    s "Oh, okay. That’s not nearly as tempting as I thought it would be."

    scene nikilovesyou16
    with dissolve

    ni "I’m sure you’d think otherwise if I didn’t look like a zombie right now. I doubt even half of that Facebook group would think I’m cute in this condition."
    s "I think you’re plenty cute. I just like your actual personality more."

    scene nikilovesyou17
    with dissolve

    ni "Holy crap. That was like, totally adorable. You’re not allowed to say nice things like that to me. It’s weird."
    s "If I’m not allowed to be nice to you and I’m not allowed to be mean to you either, what do you want me to be?"

    scene nikilovesyou18
    with dissolve

    ni "Happy."
    s "I can’t be happy {i}to{/i} you. That didn’t make sense in context."
    ni "I don’t give a fuck if it makes sense or not. You can say whatever you want to me and I’ll probably give you shit for it because I’m just so {i}used{/i} to giving you shit at this point."
    ni "But the truth is, as long as you don’t feel like the world is caving in around you, I’ll be fully content and fully willing to overlook {i}any{/i} corny compliment you toss at me."
    s "Why are you touching my face?"
    ni "Because it’s a good face and I {i}like{/i} it."
    s "Like it in a less-touchy way or something is going to wind up happening that you’ll regret in the morning."

    scene nikilovesyou19
    with dissolve

    ni "What’s that? You want me to touch you more? I mean...I {i}guess{/i} if you insist."
    s "Niki..."
    ni "We can do it if you want."

    scene nikilovesyou20
    with dissolve

    s "What?..."
    ni "...?"
    s "Do what?"
    ni "Sex."
    ni "Is that not what you were talking about when you said “Something I’ll regret in the morning?”"
    s "It was, but...I kind of figured you wanted the first time to be special since the only times you’ve ever mentioned it being a possibility were...Christmas-related."
    ni "Was today not special to you?"

    scene nikilovesyou21
    with dissolve

    s "It was miserable..."
    s "I felt things I haven’t felt in years and still haven’t really processed them."
    s "We’re both upset and both exhausted...and, with all due respect, you look like you need about a week's worth of sleep in order for your eyes to go back to normal."
    ni "I didn’t ask if today was {i}fun.{/i} I asked if it was {i}special.{/i}"

    scene nikilovesyou22
    with dissolve

    ni "We went on a mini-tour of our entire history together that ended with you confronting something you’ve been avoiding for almost a decade."
    ni "We sat on a hill with a nice view and talked about the past and the future...visited the spot where we built our secret base...and the tree we carved our names in."
    ni "And now we’re back in the room where we shared our first kiss."
    ni "Sure, we might look a little worse for wear...and we might be tired and sweaty from walking all day...and you might not even be able to get it up in your current mental state."
    ni "But, Akira..."
    ni "I don’t think I’ve ever wanted you more than I want you right now."
    s "..."
    ni "How about you?"
    ni "Do you want me too?"
    s "..."
    ni "..."
    s "Will you really never leave me?"

    scene nikilovesyou23
    with dissolve

    ni "I don’t think I’d be able to if I tried."
    s "You’ll stay by my side even when you find out all the awful things I’ve done?"
    ni "You’d have to get rid of me by force. I’d never leave on my own."
    s "I don’t believe you..."
    ni "What can I do to prove it?"
    s "..."
    ni "Akira..."
    ni "What can I do to prove it?"

    scene black
    with dissolve2

    s "Give me all of you."

    "........."
    "......"
    "..."

    scene nikilovesyou24
    with dissolve2

    s "Are you sure that’s how you want to do this?..."
    ni "Oh, please. As if you’re in the state to take things into your own hands."
    ni "Let me do all the work. It’ll be your reward for doing such a good job today."
    s "All I did was follow you around..."
    ni "That’s right...but you never tried to leave."
    ni "You confronted the past head-on. And as your childhood friend, I’m very proud of you..."
    ni "As your ex-girlfriend, I’m very proud of you..."
    ni "And no matter what I become next, I’ll {i}still{/i} be proud of you."
    ni "Now, sit still and let me lose my virginity before I die of old age."

    scene nikilovesyou25
    with dissolve2

    "After a moment of lying there with my cock pressed up against her waist, Niki reaches down and begins to stroke me."
    "Getting hard wasn’t an issue...I knew it wasn’t going to {i}be{/i} an issue the moment she unlocked the door."
    "But I didn’t know if it would come to this."
    "Or perhaps it would be better to say I didn’t {i}want{/i} it to come to this."
    "A girl like her, who’s done so much just to prop me up throughout the years, should not settle for me at my worst when she deserves me at my best."
    "But here I lie as she, once again, goes out of her way to do something that will make {i}me{/i} feel better — utterly unwilling to accept the fact that it’s something she wants as well."
    "This room is held together by a lifetime's worth of memories and all I can do in this moment is try and force a few away so we fall through a hole in the floor before we climb too far up."
    "She kicks down the ladder."
    "She shows me how weak I am."

    ni "Jesus fucking Christ, what the Hell have I gotten myself into this time?"
    ni "You really did dump all of your stats into this thing, didn’t you?"
    s "Compassion is for suckers..."
    ni "Are you ready?"
    s "I think the real question is if {i}you’re{/i} ready."
    ni "Yeah...but I’m gonna move a little slow at first. Just until I get used to it."
    s "Good luck. It’s going to hurt."

    scene nikilovesyou26
    with dissolve

    ni "No it’s not."
    ni "I’ve waited for this moment for {i}far{/i} too long for it to hurt."

    scene nikilovesyou27
    with dissolve

    ni "Ngh?!"
    ni "Hah!...Okay...no...it hurts...you were right..."
    s "Just move slow like you said...you’ll get used to it..."
    ni "Hngh!...Mhm...I can do this...this...this is nothing..."

    "Niki lowers herself onto my shaft and I’m immediately enveloped by a remarkable warmth."
    "There’s a slight resistance that disappears almost immediately as she fills herself with me in one motion."
    "Her hips do not rock and her body does not bounce — but she uses her legs to lift herself very gently up before gliding very gently back down."
    "An inch or two at a time. That seems to be all she’s focusing on for the time being. But I have no complaints about that as just being inside of her is enough to drive a man insane."
    "The tips of her fingers refuse to part ways with my cock as she uses them to steer me deeper into her, all while letting out staggered yelps of lustful anguish."

    ni "Akira...why...ngh...do you have to be so big?...You’re making this...really hard for me..."
    s "On the bright side...you feel amazing..."

    scene nikilovesyou28
    with dissolve

    ni "Yeah?...I do?..."
    ni "It’s not too...cramped in there?...Cause I’m feeling...um...pretty {i}full...{/i}"
    ni "I don’t know if I can take the whole thing just yet..."
    s "It’s just right...don’t worry..."
    ni "Okay...I’ll take your word for it..."
    ni "I’m gonna try...and move a little faster now...okay?"
    s "Do whatever you want...you’re in control..."
    ni "I’m in control..."

    scene nikilovesyou29
    with dissolve

    ni "I’m in control...I’m in control..."

    scene nikilovesyou30
    with dissolve2

    ni "Hah! Oh...mmf! That’s deep. {i}Fuck,{/i} that’s deep."
    ni "Oooh wow. Fingering does not prepare you for this."
    s "Just relax..."
    ni "Shut up. I’m the one who should be saying that to you. I told you I would handle it, so...hah...let me...fucking handle it."

    "She’s rocking now, but I’m unsure if it’s because she’s starting to get used to this or she’s just too stubborn to continue taking things at her own pace."
    "Either way, the feeling of her body weight pressing down on me as she rhythmically pulls my cock back and forth is one of the most thrilling sensations I’ve ever felt."
    "Her hands press down on my chest as she uses them to keep herself balanced, diverting every bit of energy and willpower to slowly riding me."
    "I can feel myself throbbing inside of her, and I think she can feel it as well as she begins to press harder in response."
    "Her breaths grow louder and her legs begin to shake, so I rest my hands on them to keep her steady."

    scene nikilovesyou31
    with dissolve

    ni "Hah...hah...does...it still feel good?..."
    s "Even better than it did before..."
    ni "Really?...You’re not just saying that?..."
    s "Really...the way you’re rocking your hips is...surprisingly intense..."

    scene nikilovesyou32
    with dissolve

    ni "Hah...yeah?...You mean...like this?..."
    ni "The key is...keeping up a steady rhythm...I’m a dancer, so...it comes easy..."
    ni "It also...hngh...helps...distract me from...the pain..."
    s "Look at you, talking like you’re already an expert..."
    ni "Akira......Akira.......Akira~"
    ni "I’m so happy...this is...{i}so{/i} long overdue..."
    s "Starting to enjoy yourself a little?"
    ni "Hah...heheh...maybe a {i}little...{/i}but I’m more turned on by the idea than...ngh...how it actually feels..."

    scene nikilovesyou33
    with dissolve

    s "Then maybe try...getting more into the {i}idea?...{/i}"
    ni "Hah...ngh...and...how can I do that?..."
    s "Looks like you’re still wearing...some extra clothing..."
    ni "If you want to see my tits just ask. You don’t need to manipulate me into it."
    s "Then...shirt, please..."

    scene nikilovesyou34
    with dissolve

    ni "Hah...hah...your wish...is my command..."
    ni "Mmf...mngh...heheh...you know...I think that actually worked...I do feel...a little hotter all of a sudden..."

    "As Niki lifts her shirt and exposes herself, she begins to ramp up her movement and is now full-on riding me the way she was {i}meant{/i} to be."
    "I don’t know if it can be entirely attributed to her dancing skills and sense of rhythm, but the way she rocks her body makes her look like an experienced porn star rather than a girl in the throes of her first time."
    "That, combined with the smug grin creeping across her face and the light bouncing of her breasts as her nipples harden creates an extremely lewd image that I’m more than privileged to see."

    ni "Hah...hah...is it me or...did you just get harder?..."
    s "I definitely got harder...I think you have a knack for this..."

    scene nikilovesyou35
    with dissolve

    ni "Ngh...mmf...you’re not so bad yourself..."
    ni "I’m surprised you let me handle this and haven’t tried pushing me down yet. I thought you’d hate being the submissive type."
    s "I’m enjoying myself a little too much right now to be worried about something like that..."
    ni "Hah......ahh......I’m glad....you deserve it....after today...."
    ni "Now please...enjoy yourself even more as...your childhood friend...squeezes your big cock dry..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nikilovesyou36
    with dissolve2

    ni "Hah! Ngah!....Ahh! Akira...Akira!"

    "We’ve been having sex for around forty-five minutes now."
    "I’ve somehow miraculously abstained from finishing so far but there is no conceivable way I will be able to last much longer."
    "The bright side is that Niki seems to be enjoying herself now — and it’s not just because of the “idea” anymore."

    ni "Ooooh {i}God{/i} I love your dick...I love your dick so much...oh {i}fuck,{/i} Akira...it feels so fucking good inside me..."
    s "Niki...I can’t take much more..."

    scene nikilovesyou37
    with dissolve

    ni "Ahhh...really?...But I’m finally having fun..."
    ni "You can’t hold out for just a {i}little{/i} while longer?..."
    s "Uhhhhh..."

    scene nikilovesyou38
    with dissolve

    ni "Mnf...it’s fine...you can cum..."
    s "Inside?"
    ni "I’m...hah...surprised you even asked...how...hah...considerate of you..."
    s "Inside it is..."
    ni "Go ahead...I wouldn’t...have it any other way..."

    "Instead of increasing her pace or the force with which she slams her waist downward, Niki elects to keep up the same exact pattern and motion she’s had going for ten minutes now."
    "But this is no time to be applauding her stamina and endurance-"
    "It is a time to cement her as one more cornerstone in this waste of a life that I’ve been living."
    "It’s something I should have done when we were younger."
    "But I was far too weak and far too confused back then."
    "I’m not saying I don’t still have those traits now."
    "But it wasn’t until today that I realized just how much I need her."

    stop music fadeout 15.0

    ni "Akira..."
    ni "{size=+10}{i}Akira...{/i}{/size}"
    ni "{size=+20}{b}Akira!!!{/b]{/size}"

    "She gave me a name."

    with sexfade
    with sexfade
    scene nikilovesyou39 with cumflash
    with hpunch

    ni "AAAAAAAHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    scene black
    with dissolve2

    "I spend the night in her bed."
    "I fall asleep in her arms."
    "We make love again in the morning."

    $ renpy.end_replay()
    $ nikilovesyou3 = True
    $ niki_love += 10

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "{i}Who is it you truly belong with?{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    scene street_day
    with dissolve2
    jump satmorningmenu

label nikifirstlust:
    play sound "static.mp3"
    scene nikifirstlust1 with flash
    stop sound
    play music "acoustic.mp3"

    ima "Alright! Now that {i}that’s{/i} finally over and we’ve got food on the way, it’s time to take a load off!"
    ima "Nothing says “exhausting” like watching a bunch of teenage girls model swimsuits all night, right?! And with an even bigger day ahead of us tomorrow, we’ve gotta rest while we still can!"
    w "I don’t appreciate this sudden excitement. Nor do I appreciate your hand on my shoulder. Nor Arakawa’s presence as a whole."
    s "I’m not the one who organized these rooms. Take that up with Imani. She was really pushing to sleep in the same place as me. She went to HR and everything."

    scene nikifirstlust2
    with dissolve

    ima "My intentions were good. I promise."
    w "Would you prefer to sleep in the bed with {i}him{/i} instead of me?"
    ima "I-"
    w "There’s no need to answer. I already know the truth, and I am already prepared to tell you to shove it as I am not sleeping in a futon when there is a perfectly good mattress available."
    s "I-"
    w "I also veto the prospect of Arakawa joining us as three bodies in one bed is far too many."
    ima "Well, there go my dreams of you and Osako ever tying me up."

    scene black
    with dissolve

    ima "That said! Time to check out where-"

    play sound "slidedoor.mp3"
    scene nikifirstlust3
    with dissolve

    ni "Ah-"
    ima "...we will be sleeping tonight."
    w "Either we have entered the wrong room, or I am about to give this inn a very bad review."
    w "Or a very {i}good{/i} review depending on the context of this."
    s "I think this is my fault."

    scene nikifirstlust4
    with dissolve

    ni "Who are your friends?"
    w "You know this woman, Arakawa?"
    s "This woman here is the alleged darling of Kumon-mi — Niki Nakayama."

    scene nikifirstlust5
    with dissolve

    w "What? No she's not. Why would you know Niki Nakayama?"
    ni "It’s not {i}alleged,{/i} asshole. I am loved by all and I’m sure both of these girls will attest to that."
    ima "You look...different than you do on all of the posters."

    scene nikifirstlust6
    with dissolve

    ni "Yeah. Being perfect all the time is kind of exhausting, so I tend to dress down on my off days. Sorry for the disappointment."
    w "Arakawa, why is there a famous idol in my bed?"
    s "It’s a long story."

    scene nikifirstlust7
    with dissolve

    ni "No it’s not. I’m here to fuck him."
    s "Oh, okay. I guess we’re just going with that, then."
    ni "Why wouldn’t I? It’s the truth."
    ima "Uuuuhhhhh..."
    w "How much did he offer to pay you? Because I would demand at least half up-front as chances are he is lying."
    ni "He doesn’t have to pay me anything. We’re dating. He can hit it whenever he wants."
    ima "Uuuuuhhhhh???"
    s "Niki-"
    ni "Actually, I’m glad you guys showed up now since it saves me having to stop in the middle of sex. "

    scene black
    with dissolve

    ima "Uhhhhhhhhhhhhh????????"
    ni "I came prepared in case something like this would happen. You can never be too safe in places like this."
    w "What in the world is happening right now?"

    scene nikifirstlust8
    with dissolve

    ni "Here. "
    w "What is this?"
    ni "An NDA."
    ima "You’re...You’re making us sign an NDA?"

    scene nikifirstlust9
    with dissolve

    ni "Yeah. I kind of have to if I’m going to have sex in here all night. Idols are supposed to be pure and all that shit. And you might hear some things in the coming hours that will be hard to forget."
    ni "Needless to say, if any of that got out, I’d be fucked. I can get you tickets or money or whatever in exchange for your signatures, but it would be really cool if you would just sign them for free as a favor."
    ima "So...let me get this straight. "
    ima "You came here to have sex in our room...on {i}our{/i} bed...and now you want us to sign an NDA that you {i}would{/i} pay for...as a {i}favor{/i} instead? "
    ni "Pretty much, yeah. Also, it’s not like I’m kicking you guys out. I don’t mind if you stay. You just can’t record any of this or ever talk about it again."
    s "Is this what it means to bang a famous person?"
    w "Just who the fuck are you, Arakawa? How did you land an idol?"
    ni "Fun fact, I’m only an idol in the first place because this douchebag broke my heart into a million pieces. But that’s behind us now."
    ima "Doesn’t sound like it’s behind you."
    ni "Listen, are you going to sign this or not? Because I’m really fucking horny right now and I have been waiting for this moment all fucking day."

    scene black
    with dissolve

    w "Ugh...just give me the fucking paper. You can make a check out to Wakana Watabe. You haven’t earned a favor yet."
    ni "Got it. And you?"
    ima "Uuuhhhhhh..."
    ni "I’m also open to letting you watch as a form of payment. It’s not every day you get to see something like this, you know."
    ima "Yeah, no kidding. Make my check out to Imani Imai. Pen please, Wakana."
    w "Here. And for the record, this is the last time I come to this resort with {i}any{/i} of you."
    ni "Thanks for your cooperation, you two. Now, please vacate the premises as my clothes are about to come off."

    scene nikifirstlust10
    with dissolve2

    s "I feel like you could have handled that in a much less intrusive way."
    ni "And I feel like you probably should have told me you were rooming with two other girls. "
    ni "But, as I am a kind-hearted soul, I’m willing to let bygones be bygones since you will now prove you are mine by fucking me loud enough for both of them to hear."
    s "How did you even figure out which room was mine?"
    ni "Noriko helped."
    s "Did you make her sign an NDA too?"
    ni "She signed her NDA the moment she was born. The NSL prevents either one of us from spilling the other’s secrets."
    s "The...NSL?"

    scene nikifirstlust11
    with dissolve

    ni "Nakayama Sister Law. Why are your pants still on?"
    s "There’s just..."
    s "There’s something I want to talk about first."

    scene nikifirstlust12
    with dissolve

    ni "I swear to God if this isn’t about what position you’re going to rail me in, I’m going to be really fucking pissed, Akira."
    s "It’s not. But don’t be pissed because you’re not {i}that{/i} far off."
    ni "Well, what is it? Because I have work in the morning and want to fit in as much as we possibly can tonight. And no, I was not referring to your penis when I said that. But I am now."
    s "There’s just something I want you to call me in bed from now on."

    scene nikifirstlust13
    with dissolve

    ni "Really? I didn’t think you’d be into that."
    s "Well, I am..."
    s "And the name I’d like you to call me is-"

label nikinaming:
    $ nikimaster = renpy.input("Enter a name for Niki to call you...")
    $ nikimaster = nikimaster.strip()

    if nikimaster.lower() in ["akira"]:
        s "My regular name."

        scene nikifirstlust14
        with dissolve

        ni "Seriously? "
        ni "You’re really going to build me up just to break me down like that? I was looking forward to something creative."
        s "Well, I’m sorry to disappoint you. I just really wanted to make it clear that I want you to refer to me as Akira. "
        ni "Wonderful. And you can call me “Niki.” {i}Now{/i} can we fuck?"
        s "Yes. Now we can fuck."
        ni "Thank God. Because if you said no, I was just going to pounce on you."

        jump restofnikifirstlust

    if nikimaster.lower() in ["sensei"]:
        s "Sensei."

        scene nikifirstlust15
        with dissolve

        ni "That would be really kinky if it wasn’t literally your occupation. Now, it just makes me question your motives."
        s "I like what I like, Niki."
        ni "Want me to put on my old school uniform while I’m at it? Restyle my hair?"
        s "Are you actually willing to do those things?"
        ni "If that’s what you like, sure. I mean...not right now, though. I don’t exactly drag my old uniform with me everywhere I go."
        s "From now on, you probably should. Just to be safe."

        scene nikifirstlust16
        with dissolve

        ni "Deal."
        ni "I’ll be in your care...{i}Sensei.{/i}"

        jump restofnikifirstlust

    if nikimaster.lower() in ["niki", "niki nakayama"]:
        s "Niki Nakayama, world-famous idol."
        ni "Yes?"
        s "..."
        ni "..."

        scene nikifirstlust17
        with dissolve

        ni "Wait. Is that what you want {i}me{/i} to call {i}you?{/i}"
        s "Yeah. But only if that’s cool."
        ni "Akira, I get that I’m amazing and a very big deal. And I’m happy that you’re finally coming around to it. But I’d like you to maybe come around to it in a way that doesn’t involve identity theft."
        s "It would only be during sex, I promise."
        ni "That’s somehow even worse."
        s "You know, I kind of thought you’d go along with it on account of how much of an egomaniac you are. Whispering your own name during sex sounds like it would be right up your alley."

        scene nikifirstlust18
        with dissolve

        ni "Wanna know what’s {i}more{/i} up my alley? Whispering the name of the guy I’m in love with. Now choose something else or fuck off."

        jump nikinaming

    if nikimaster.lower() in ["noriko", "noriko nakayama"]:
        s "Noriko."

        scene nikifirstlust18
        with dissolve

        ni "You want me to call you my baby sister’s name while we’re having sex?"
        s "It would be greatly appreciated, yes."
        ni "Any {i}other{/i} lifelong fantasies you want to air out before fucking me tonight? Should I maybe weave my mom’s name in too just to keep things fresh?"
        s "Just Noriko’s name, please. It’s a very pretty name."
        ni "Do you actually like the name? Or do you just like the idea of me fucking my sister?"
        s "I think {i}everyone{/i} likes the idea of you fucking your sister. "
        ni "Everyone but, you know, {i}us sisters.{/i}"
        s "I feel like Noriko would probably hook up with you under the right pretense."
        ni "Is “the right pretense” somebody holding a gun up to her head and telling her to hook up with me? Because, if so, yeah. I can see that too."
        s "You’re not going to call me Noriko, are you?"
        ni "No, Akira. I’m not."

        jump nikinaming

    if nikimaster.lower() in ["daddy", "dad", "father", "papa"]:
        s "[nikimaster]."

        scene nikifirstlust19
        with dissolve

        ni "Well, it’s not the most {i}creative{/i} of choices...but it’s still hot either way."
        ni "You really want that to be the dynamic we go for, though? Because if memory serves me right, {i}I’m{/i} the one who dommed {i}you{/i} first."
        ni "Maybe you should be calling me “Mommy” instead? Does that sound fun?"
        s "It sounds kind of degrading actually."
        ni "I think that’s kind of the point, genius."
        ni "But hey, if that’s what you want, I won’t argue."
        ni "Just know you better be willing to live up to the title if I start calling you that. "
        ni "Hold nothing back, {i}[nikimaster]...{/i} "

        jump restofnikifirstlust

    if nikimaster.lower() in ["onii-chan", "oniichan", "big brother", "big bro"]:
        s "[nikimaster]."

        scene nikifirstlust20
        with dissolve

        ni "Oh-ho-ho. What have we here?"
        s "Is there a problem?"
        ni "Problem? No. I just figured “[nikimaster]” was more of a Noriko thing since I always looked at myself as more of a {i}big{/i} sister to you."
        s "I’m older than you, Niki."
        ni "Hey, I’m not saying I have a problem with it. I think it’s really hot. Plus, with our history, I think calling you that will add a {i}very{/i} fun layer to things going forward."
        ni "One thing, though — if I’m going to be your little sister, don’t think for a second I’m just gonna let you be all basic and take control all the time."
        ni "This little girl is gonna make her big brother {i}work.{/i}"
        ni "{i}A lot.{/i}"
        s "You really like this one, huh?"
        ni "I just really like {i}you.{/i}"

        jump restofnikifirstlust

    if nikimaster.lower() in ["selebus"]:
        s "Selebus."

        scene nikifirstlust21
        with dissolve

        ni "Hey, I know that guy. He created Lessons in Love."
        s "Oh, awesome. I had no idea you were familiar with him already."
        ni "Yeah. I fucking hate him."
        s "Wait, what?"
        ni "How could I not when it’s {i}his{/i} fault that half of my life has been a living hell? Do you have any idea how much I’ve suffered because of my fucking backstory? {i}He’s{/i} the asshole who came up with that."
        ni "It hasn’t been easy, Akira. And if I have to be reminded of that every single time your custom name shows up, I’m not going to be a happy camper."
        s "I’m sure he did it for a reason, Niki."
        ni "Yeah, probably because the childhood tsundere trope is fucking awesome. But that doesn’t mean my suffering should go unnoticed. So fuck that guy. He can touch grass."
        s "Selebus is a no-go then?"
        ni "Yeah. Not a chance."
        s "Either way, I still think it would be right to go support him on SubscribeStar as he develops this game entirely alone and-"
        ni "Nope. Not happening."
        s "Really?"
        ni "Yeah. Fuck him."
        s "Oh..."
        s "Well...I guess I’ll just choose something else then."

        jump nikinaming

    else:
        s "[nikimaster]."

        scene nikifirstlust22
        with dissolve

        ni "If that’s what you want, that’s fine by me."
        ni "Now...are you done making me wait, [nikimaster]? Because I’ve got two signed NDAs and roughly ten hours worth of waiting for this that says “Hurry up and take me already.”"
        s "Then, I guess I’ll have to do just that..."

        jump restofnikifirstlust

label restofnikifirstlust:
    scene black
    with dissolve2

    "I take a step closer to Niki and the two of us begin to undress one another..."
    "........."
    "......"
    "..."
    "{i}Two hours later...{/i}"

    scene nikifirstlust23
    with dissolve2

    ni "{i}Aaah! [nikimaster]! More! More!{/i}"
    ni "{i}Harder! Fuck me with...your big cock...even harder!{/i}"
    ima "Jesus. She really wasn’t kidding when she mentioned all night, was she?"
    w "I’m going to have to sleep in a fucking futon, aren’t I?"
    ima "Forget about the futon, Wakana. I’m starting to think that idol girl might be draining every last ounce of life out of my poor Senpai."
    w "Forget about your “poor Senpai.” What about {i}us?{/i}"
    w "That was {i}our{/i} bed. And now, we’re going to need to have it professionally cleaned ten times before we’re even able to look at it."
    ni "{i}Aaaaaaah! Yeah! Yeah, yeah, yeah! Right there! Right there, [nikimaster]!{/i}"

    scene nikifirstlust24
    with dissolve

    w "I wonder if that sword in the back of the room needs to be sharpened or not."
    ima "Take it easy, yo. I’m sure they’ll be done in another...twenty minutes. Tops. No man has that kind of stamina."
    w "You’ve been saying that same thing since they started."
    ima "Well, it’s not {i}my{/i} fault Sensei’s got superhuman sex skills. I’m just saying...there’s gotta be a limit, you know?"

    scene nikifirstlust25
    with dissolve

    w "{i}Hah...{/i}Of course this would be the one area Arakawa excels in. No wonder he doesn’t spend time writing anymore if {i}this{/i} is his new skillset of choice."
    ima "Bet you wish Osako was here right now, huh?"
    w "Perhaps."
    ni "{i}Ahh! Fuck! I’m gonna cum! I’m gonna...fucking cum! Aaaaahh!{/i}"
    w "Okay, yes. Despite my demeanor, I am very much not immune to...{i}this.{/i}"
    ima "Like I said...twenty more minutes. Tops."

    scene nikifirstlust26
    with dissolve

    w "Imani, forgive me for asking but...are you really {i}okay{/i} with this?"
    ima "I mean...it’s not my ideal Saturday night, but...why do you ask?"
    w "Why do you {i}think?{/i}"

    scene nikifirstlust27
    with dissolve

    ima "I don’t know what you’re talking about."
    w "We both know that’s not true..."
    ni "{i}[nikimaster]! [nikimaster]! I love your cock! I love your...huge fucking cock! Fuck me, fuck me, fuck me!{/i}"
    ima "Just twenty more minutes..."
    ima "We’re almost there..."

    scene nikifirstlust28
    with fade

    ni "Oh...{i}baby...{/i}you feel so fucking good...I love it when you...fuck me from behind...I love it when you...grab my...{i}fucking{/i} ass..."
    s" Niki...I hate to be the bearer of bad news, but I’m kind of running out of steam right-"
    ni "Don’t be a fucking...pussy! Just...fuck {i}my{/i} pussy!"
    ni "It waited...over a fucking...decade for you! You...owe me...at least a million more...orgasms!"
    s "Okay, but...do they all have to come in {i}one{/i} night?..."
    ni "I’ll...give you a break at...five hundred..."

    "This girl is insane."
    "I’ll be the first to admit, though...this is probably the most sexually compatible I’ve been with someone yet."
    "I’m not sure if any of that has to do with subconscious nostalgia or just being high on someone I love that I’m {i}allowed{/i} to love-"
    "But if it weren’t for biological purposes, I’d be more than happy to keep fucking this girl for the rest of forever."

    ni "Hah...hah...ngah...fuck..."
    ni "[nikimaster]...right there...[nikimaster]..."

    "She makes up for what I lack in energy and repeatedly rams herself into my waist, filling up her body with every single inch of me."
    "And just like our first time, I can’t help but admire her seemingly endless font of stamina."
    "Her pale skin glistens with sweat, reddening in the areas where my hands have lingered the longest."
    "I can see the outlines of my fingers pressed into the flesh of her tight ass each time I pull it toward me, and I wonder to myself if those markings will remain long after the night has ended."
    "I hope they do — for if there has ever been a moment in which I’ve wanted to mark my territory, it is this one."
    "I want to keep her forever. "
    "All to myself."
    "And fill her to the brim with a liquid reminder that she has always been important to me-"
    "Even if I didn’t recognize it or remember her."
    "Because what I have learned tonight and nights before, it’s that even if my mind abandoned Niki Nakayama, my body has yearned for her."
    "And the pressure building up within me, defying what my body believes it is capable of, makes me know that for sure."
    "Now, please excuse me while I empty myself out into my childhood friend for the fifth time tonight."

    ni "Hah! Hah! Yes! Again! I’m gonna...cum...again! [nikimaster]!"
    s "Me too, Niki..."

    scene nikifirstlust29
    with dissolve

    ni "Hah...hah...see? I knew you...had it in you..."
    ni "How’s my...pussy, [nikimaster]?...You like it when I...{i}do that?!{/i} You like it when I...take every...fucking inch of that...thick cock?!"
    s "You’re...amazing..."
    ni "You’re...ahh...not...so bad...your-"

    scene nikifirstlust30
    with dissolve

    ni "{i}Hah!{/i} Ohhh...god...right there...just like that...just...{i}hah...{/i}"
    s "What were you saying just now, Niki? That I’m {i}not bad?{/i}"
    ni "Aahh...ah...uh-huh...you’re...ah...actually...pretty...hah...[nikimaster]..."
    s "Pretty {i}what,{/i} Niki?"
    ni "Pretty...okay at..."

    scene nikifirstlust31
    with dissolve

    ni "Aah! Hah! Ngh...fuck! I take it back! I...take it...back!"
    ni "You’re...even better than me! You fuck me...so good...[nikimaster]! My pussy...doesn’t deserve your...godly fucking...dick!"
    s "Godly?"
    ni "Hah! Hah! Yes, baby! You’re...barely even human! It’s so...fucking good! I’m...hah! [nikimaster]! It..."
    ni "Here...it..."

    with sexfade
    with sexfade
    scene nikifirstlust32
    with cumflash
    with hpunch

    ni "AaaaaAaaaAaaAAAaahahhhh!!!!~~~~~~~~~~"

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Another hour later...{/i}"

    scene nikifirstlust33
    with dissolve2

    ima "..."
    w "..."
    ima "Are..."
    ima "Are they finally done?"
    w "Longest {i}twenty minutes{/i} of my life."
    ima "Rest in peace, Senpai. You will never be forgotten."
    s "{i}Niki, wait. What are you doing?{/i}"

    scene nikifirstlust34
    with dissolve

    ima "Oh. He lives."
    w "Shh. Something’s happening."
    ni "{i}Being a good house guest. It’s only right that I extend my gratitude to your friends since we’re keeping them up all night.{/i}"
    s "{i}I really don’t think that’s-{/i}"

    play sound "slidedoor.mp3"
    scene nikifirstlust35
    with dissolve

    ima "Wha-"
    ni "Hey. "
    w "Umm...hi?"
    ni "Either of you guys want to join in? Neither of us mind as long as I’m involved and I feel kind of bad just making you listen."
    s "Don’t just decide things for me, Niki. Close the door."
    ima "Uhhhhhhh..."
    ni "Don’t listen to him. He’s only pretending to not want to do this because he isn’t good at following his heart."
    ni "Oh, also- it’s fine if you touch me, just try to avoid my face. I’m on camera all the time, so I need to make sure that part of me stays mostly normal."
    ni "Oh. Also part two — that is not a beginner-level dick in there. You’ve gotta be {i}ready{/i} for that thing. It might take a little getting used to."
    ima "Uuuuuuuhhhhhhhhhhhh..."
    w "I..."
    w "Um..."

    scene nikifirstlust36
    with dissolve

    w "{i}Hah...{/i}no thank you."
    ni "Are you sure? You might never get another chance."
    w "I can’t. I have a partner with self-esteem issues who would not take kindly to the idea of me fornicating with a celebrity. "
    ni "Good for you. I hope you guys last a really long time. How about you, other girl?"
    s "Niki, come on. Close the door."
    ni "Again, ignore him. I know what he wants better than he does."
    ima "I..."
    ima "I think I’m...just gonna hang out with my friend instead."
    ni "Okay. Suit yourself. But don’t say I didn’t ask."

    play sound "slidedoor.mp3"
    scene nikifirstlust37
    with dissolve

    ni "{i}Kindness rejected. Looks like we’re flying solo.{/i}"
    s "{i}How are you this much of a freak already?{/i}"
    ni "{i}They signed NDA’s. Now’s the perfect time to be a freak.{/i}"
    ima "What the fuck was that?"
    w "A sudden incentive for me to bring up the celebrity clause in my relationship with Osako again."
    w "Of all the fucking times to be absent."
    ima "Were you seriously considering it?"

    scene nikifirstlust38
    with dissolve

    w "Were you seriously {i}not?{/i} That is Niki Nakayama. {i}And{/i} the man that you like for some ungodly reason. How can you turn that down as a single, horny female?"

    scene nikifirstlust39
    with dissolve

    ima "{i}Because I don’t want him to find out like this.{/i}"
    w "Imani...he doesn’t know yet?"
    ima "I’ll tell him eventually. I’m just waiting for the...right time."

    scene nikifirstlust40
    with dissolve
    stop music fadeout 10.0

    w "{i}Hah...{/i}Okay. If that’s what you want, I’ll respect your wishes."
    ni "{i}Mnch...mmngh...chmp...get...hard already...{/i}"
    w "However, I can not handle any more of this without making a disgrace of myself, so I am going to get some fresh air."
    ni "{i}Mmf! Mmngh...hmm!{/i}"
    ima "Yeah..."
    ima "I think I’ll come with you."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ nikifirstlust = True
    $ niki_lust += 5

    "{i}Niki’s lust has increased to [niki_lust]!{/i}"
    "........."
    "......"
    "..."
    "{i}Meanwhile...{/i}"

    jump beachwars9

label nikispring1:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "It’s something I haven’t been doing nearly as much as I {i}should{/i} lately, given that she’s the single best support system I have...but my legs are tired from running, and now I feel like I have to."
    "She’s told me that I’ll always have a home inside of her. And considering my actual home is plagued by a living reminder of my inadequacy as a guardian, I’ll find solace in being guarded by someone else."
    "Someone who’s always been there."
    "Someone who will always {i}be{/i} there."

    play sound "phonebeep.wav"

    ni "Hey, asshole."

    "But will occasionally be very mean to me for no reason whatsoever."

    play music "remember.mp3"

    s "What did I do now?"
    ni "Nothing specific. I just saw an old couple holding hands a few minutes ago and it reminded me that you never hold my hand. Which you should. I have nice hands."
    s "Holding your hand in public could ruin your career. "
    ni "Yeah. Well, so could sending you nudes and that hasn’t backfired so far."

    if nikinudetrade == True:
        "Nope. Not at all."
    else:
        s "You’re lucky I’m a good person."
        ni "But you’re not a good person. You’re an asshole who doesn’t hold my hand enough."
        s "I’ll keep that in mind for the future, I guess."

    ni "Anyway, what’s up? Why are you calling?"
    s "I just wanted to see what you were up to."
    ni "Right now? I’m just cleaning out the basement. Otoha just left and I don’t have to take any lessons of my own today."
    s "I’m surprised you’re still taking lessons at all considering you’ve been doing this for so long. How do you not know everything already?"
    ni "I {i}do{/i} know everything already. I just need to make sure I {i}keep{/i} knowing everything or someone younger and prettier will dethrone me as the darling of Kumon-mi."
    s "The idol industry sure is competitive, isn’t it?"
    ni "Are you really not going to jump on that opportunity to tell me that there is no one prettier than me?"
    s "I figured I didn’t have to since you’re always telling yourself that."
    ni "You’re seriously terrible with women. Want to come over and pretend I didn’t just say that?"
    s "I don’t know. You seem kind of fiery today."
    ni "You love it and you know it."
    s "Yeah, I’m on my way now. "
    ni "Nice. Bring me lunch."
    s "No."
    ni "Akira-"

    play sound "phonebeep.wav"

    "I hang up the phone and start making my way over to the sketchy basement."
    "But not before stopping for a quick lunch just to spite my childhood friend."
    "My evil knows no bounds."
    "........."
    "......"
    "..."

    scene nikibasementpound1
    with dissolve2

    ni "You ate without me, didn’t you?"
    s "My evil knows no bounds."
    ni "That’s fine. I just won’t ever let you cum in my mouth again. That’ll make us even."
    s "I would like to sincerely apologize for my actions today. It will never happen again."
    s "But also, you are rich and should probably be buying your own lunch."

    scene nikibasementpound2
    with dissolve

    ni "I really should, shouldn’t I? But you see, Akira, it’s exactly that that makes {i}you{/i} buying me things so much sweeter. It’s like having a cute little slave."
    s "I think all of the power and adoration have gone to your head."

    scene nikibasementpound3
    with dissolve

    ni "Oh, please. From what I understand, you’ve made almost an entire class full of high school girls fall in love with you. There’s no way {i}I’m{/i} the only one on a power trip."
    s "At least your power trip only hurts me and mine damages the well-being of approximately twenty girls."
    ni "So what I’m hearing is that I’m better than you."
    s "I didn’t think that was even up for debate."

    scene nikibasementpound4
    with dissolve

    ni "Good, good. Now, dogeza and beg for my forgiveness so that I may retract the cum comment."
    s "I don’t want to get on the ground. It’s dirty."
    ni "Yeah, I haven’t gotten around to cleaning that yet."

    scene nikibasementpound5
    with dissolve

    ni "And now I don’t have to since {i}you’re{/i} here! Which means you can tell me all about how things have been lately without the looming fear that Ami is listening in on our conversation!"
    s "Can we actually...{i}not{/i} talk about how things have been lately?"

    scene nikibasementpound6
    with dissolve

    ni "Why? You’re as fucked up as ever and I’m your adorable and loving girlfriend. This is the part where you’re supposed to lie in my lap and cry about all of your problems."
    s "Yeah, that’s kind of a future I’d like to avoid if at all possible."

    scene nikibasementpound7
    with dissolve

    ni "Akira..."
    s "Please don’t lecture me right now. I have enough going on without the added pressure you’re about to place on me."
    ni "You know this isn’t healthy. You know bottling everything up is going to land you right back in that bed again. I thought we were past this."
    s "If we were past it, I’d have been with you every day since waking up again. "

    scene nikibasementpound8
    with dissolve

    ni "But you {i}know{/i} I-"
    s "I know you love me and I know you’re always here for me. And I love you too. But that’s exactly why I haven’t bothered burdening you with any of this shit."
    ni "It’s not a {i}burden,{/i} idiot. We’re adults now. We’re supposed to be able to lean on each other for things like this."
    s "Niki, I don’t deserve you."
    ni "Yeah, no shit. I rule. But that doesn’t mean you can just conveniently disregard the fact that you already {i}have{/i} me. We need to talk if you’re still hurting. I mean it."
    s "We will, just...not right now. I need a little more time."

    scene nikibasementpound9
    with dissolve

    ni "Mm..."
    s "I promise. "
    ni "Mmmmm..."
    s "Niki..."

    scene nikibasementpound10
    with dissolve

    ni "I exercise my right as your girlfriend to demand an appetizer."
    s "Fine, but we’re getting delivery. I don’t want to go out again right now."

    scene nikibasementpound11
    with dissolve

    ni "An {i}emotional{/i} appetizer, Akira!"
    s "So..."
    s "Mozzarella sticks?"

    scene nikibasementpound12
    with dissolve

    ni "How are those emotional?!"
    s "They just elicit more of a response than fries do, so-"
    ni "Dumbass, I’m talking about your feelings! Can you at least tell me what this is about so I don’t have to stay in the dark for any longer than I already have?! Because this {i}sucks,{/i} Akira! Seriously!"
    s "Niki..."

    scene nikibasementpound13
    with dissolve

    ni "Is it something with Ami? A friend I don’t know about? Be honest with me. I can take it."
    s "It’s..."
    s "It’s a lot of things. But I’d be lying if I said what’s going on with Ami isn’t adding fuel to the fire."

    scene nikibasementpound14
    with dissolve

    ni "{i}Hah...{/i}Your soft spot for her actually makes me jealous. But I get it. She {i}is{/i} family after all. I’m sure I’d be fucked up too if something happened to Noriko."
    ni "Maybe I can come visit her soon and-"
    s "No."

    scene nikibasementpound15
    with dissolve

    ni "No?"
    s "You should stay out of this."
    ni "Uh...{i}why?{/i}"
    s "Because Ami wouldn’t want you to see her right now. She had an...accident involving a pair of scissors and her hair."
    ni "That’s like, a rite of passage for all teenage girls. I’m sure she’ll survive. "
    s "Just...please stay away from her, Niki. She needs to be alone right now. She needs help."
    ni "Well, is she going to {i}get{/i} it? Because she’s needed help for a long ass time, Akira. You both have."
    s "I’ll see what I can do when she’s back to herself, but...for now-"

    scene nikibasementpound14
    with dissolve

    ni "Yeah, yeah. I’ll {i}keep my distance{/i} if that’s what you think is best."
    ni "I think you might be underestimating the impact I could have on her, but {i}fine.{/i} We’ll do things {i}your{/i} way. You {i}do{/i} know best after all..."
    s "Your sarcasm is palpable right now."

    scene nikibasementpound16
    with dissolve

    ni "Probably because I wasn’t trying to hide it. I’m not like {i}you,{/i} dummy. I actually {i}want{/i} you to know how I’m feeling.  "
    s "I told you, I just need some more time. There’s been so much shit spinning through my head lately that it makes me want to just curl into a ball and...set myself on fire."
    ni "You’d burn better if you splayed yourself out. Just saying."
    s "Thanks. I’ll keep that in mind."

    scene nikibasementpound17
    with dissolve

    ni "No need to thank me. I’ll do anything I can to help, you know."
    s "Any more ideas that might help cure the looming desire to fall asleep and never wake up?"

    scene nikibasementpound18
    with dissolve

    ni "Hmm...that’s a good question. Let me think."
    s "Don’t think too hard. That was mostly rhetorical."

    scene nikibasementpound19
    with dissolve

    ni "Oh, was it? "
    s "Yeah. I don’t actually want any advice right now. I just want to go into stasis."
    ni "So what you’re saying is you {i}don’t{/i} want to have lots of lovey-dovey childhood friend sex on the couch. Right?"
    s "..."
    ni "Because I’m not saying {i}I{/i} want to have lots of lovey-dovey childhood friend sex on the couch, but I probably {i}would{/i} have lots of lovey-dovey childhood friend sex on the couch. If {i}you{/i} wanted to."
    s "..."

    scene nikibasementpound20
    with dissolve

    ni "..."
    s "..."

    scene nikibasementpound21
    with dissolve

    ni "..."
    s "..."

    scene black
    stop music

    s "Let’s go."
    ni "Oh, fuck yes."

    play sound "static.mp3"
    scene nikibasementpound22 with flash
    stop sound
    play music "asobeatsex2.mp3"
    play sound "dosex.mp3"

    ni "Aaah! Aaah! Aaah! Aaah! Aaah! This...isn’t...lovey-dovey...at all!"
    s "You want me to go slower? You want me to take it out altogether? Is that what you want?"
    ni "N...Never! Fuck me! Harder! I love it, [nikimaster]! I love the way you...use my pussy! I love it when you...fuck me!"
    s "I bet you do, Niki. Your pussy’s all mine, isn’t it?"
    ni "Yes...baby! My whole body...is yours to use...however you want!"
    s "However I want? "
    ni "Y...Yes! Any...w...way you want.......ooohhhh {i}god{/i} your cock is good. {i}God{/i} I love it when you...fuck me!"
    s "You’re not worried I’ll mess you up too much? That I’ll fuck you too hard and you won’t be able to perform for your {i}adoring{/i} fans?"
    ni "Hah...hah...all...I care about...is [nikimaster]’s dick...I don’t...hah...care if it...hah...breaks me! It feels...soooo...gooooood!"

    play sound "static.mp3"
    scene nikibasementpound23 with flash
    stop sound

    "I thrust harder into Niki from behind, pushing her head down into the cushions and muffling her screams."

    ni "{i}MNNFFFFF!!! [nikimaster]!!!! Yes! Yes, yes, yes! Harder! Harder! Fuck me! Fuck...meeeeee!"

    "I dig my nails into her ass and can feel myself breaking skin in the process. And I apply so much pressure and weight on her body that she wouldn’t be able to thrust back even if she wanted to."
    "I’m glad she can take a beating, though, because I don’t intend to be very {i}kind{/i} to her today."
    "{i}This{/i} will be how I express myself in lieu of a sob story. There’s no need to {i}talk{/i} at all when I can just fuck her sopping wet, idol pussy until I feel a little better inside."
    "It’s not as tight as {b}HERS{/b} was, but it fits me well. It clings to my shaft and begs to be filled, so I reply in kind by pounding it hard, sending ripples through her skin like they’re tiny, little waves."

    ni "AaaaAaaaAAAaahhh!!!! Fuck, fuck, fuck, fuck, fuuuuuck! Oh FUCK I missed your cock! Oh GOD I missed the way you...fuck me, [nikimaster]!"
    s "Did you play with yourself while I was gone?"
    ni "Hah...hahh...yes...yes, [nikimaster]...I’m sorry...I couldn’t wait for you...any longer!"
    s "What’d you think about?"
    ni "Hah...hah! I can’t...remember! I can’t remember!"

    scene nikibasementpound24
    with dissolve

    s "Tell me, you horny bitch!"

    play sound "static.mp3"
    scene nikibasementpound22 with flash
    stop sound

    ni "Hah! Hah! {i}Fuck{/i} I like this side of you! {i}Fuck,{/i} that feels good! Oh god, oh god, oh...fuck...hah! Let’s...ngh...let’s see..."
    s "Spit it out or I’ll stop."
    ni "Costume! My...costumes! I thought of you...in the dressing room...fucking me...while I try them on...for you..."
    s "Isn’t that a little...conceited? That sounds more like...one of my fantasies..."
    ni "There was...hah! There was more! "
    s "Yeah? Tell me."
    ni "Haaah.....haaaAAAaaaaaHhh!"
    s "If you’re too distracted, I’ll-"
    ni "Please...please no...I’m gonna cum...it’s too good...you’re too good! I love you! Fuck me! Harder! [nikimaster]!"

    play sound "static.mp3"
    scene nikibasementpound25 with flash
    stop sound

    s "Already? You wanted it that bad, huh?"
    ni "Yes! So bad! So bad! I’ve been...desperate...for you to rough me up! Harder! I want it...harder, Akira! Harder, harder, harder!"
    s "If only your fans could see you now. What do you think they’d say?"
    ni "I’m a slut! I’m a little...cock-loving slut! Ohhhh FUCK I’m cumming! I’m cumming, [nikimaster]!"
    s "Whose slut are you, Niki?"
    ni "AAAAAAHHHHH YOURS, BABY! FILL ME UP! CUM IN ME, BABY! CUM!"
    s "Sorry, but I’m not even close yet."
    ni "AAAaaaaAAAAAHHHH! NG....AHHH! Hah! HHaaaaaah! FuuuuUUUUUCK!!!! AKIRA!!!!!"
    s "Was that good, baby? You want me to make you cum again?"
    ni "Haah! Hah! Yes! More! Fuck me...more! Don’t stop! Don’t...stop!!!"

    "I do as Niki asks and continue to treat her perfect body like little more than a piece of meat."

    scene nikibasementpound26
    with dissolve

    "Until something interesting catches my eye."

    scene nikibasementpound27
    with fade

    o "..."
    s "..."
    ni "Hah! Hah! Why...are...you...slowing down?! I said...more! More, more, more! More cock! Fuck me harder, [nikimaster]!"

    "I’m not sure when {i}she{/i} showed up, but...I guess she’s not in any rush to leave."

    ni "AaaaAAAaaAAAAhhh babyyyyyy! Fuck my pussy! Fuck my little pussy!"
    o "..."

    "And {i}I’m{/i} not in any rush to shoo her away."

    scene nikibasementpound28
    with fade
    play sound "dosex.mp3"

    s "You like that, huh? "
    ni "It’s...soooo gooood!! AaaaAAAahhh, [nikimaster]!"
    s "Tell me again, Niki. Tell me how much you love my cock."
    ni "I love it...oh FUCK I love it...I can’t get enough...you’re so big...and you’re so {i}good{/i}...oh god you’re so DEEP...oh GOD it’s amazing!"

    play sound "static.mp3"
    scene nikibasementpound22 with flash
    stop sound

    ni "I can feel it...throbbing inside me, baby...I want your cum...I want you to...fill me up! Cum in me, baby! Cum inside me! Give it to me, Akira! Harder! Harder!!!"

    "Despite Niki obediently taking every single inch of my cock and saying everything I tell her to, I can’t help but focus on a certain onlooker instead."
    "Because not only has she decided to stay with us-"

    play sound "static.mp3"
    scene nikibasementpound29 with flash
    stop sound

    "But she’s decided to join in as well."
    "At least...in a sense."
    "I’m sure she’d rather be on the couch with us, but it’s hard to discern whether she’s hungry for the same meal Niki’s having or if she’d rather be {i}eaten{/i} instead."
    "Regardless, I watch carefully as she slides her hand into her jeans and begins to play with herself, keeping as quiet as can be as she watches me treat her idol like a fuck toy."

    ni "Haaah! Akira! Stop...slowing down! Fuck me harder! Fuck me {i}faster!{/i} Love me more! "
    s "More? Don’t I love you enough already?"
    ni "Ha! Haaaah! No! Not...even close! I love you...so much! I couldn’t wait...until you got back...to fuck me even more! I want you! Every day! Every night! You and your...BIG fucking cock, AAAAH!"
    ni "I’m gonna cum again! I’m gonna fucking cum again, Akira! You’re so good!"
    s "Yeah? Want to cum together this time?"

    scene nikibasementpound30
    with dissolve

    o "{i}Ah...{/i}"
    ni "Wait...did you just-"

    play sound "static.mp3"
    scene nikibasementpound31 with flash
    stop sound

    s "Just what, Niki?"
    ni "Agh...aahh....ngah...can’t...remember!...Cumming...again!..."

    "Otoha’s legs begin to tremble as Niki convulses against my waist. And I imagine the high-schooler is likely trying to sync up their orgasms so she can at least {i}pretend{/i} she’s wearing my shoes right now."
    "I’m a little late to the party, though, and haven’t managed to finish just yet. But I probably {i}should{/i} before my {i}girlfriend{/i} here passes out."

    ni "Aagh.....ngah......ack.......gah......hagh....."
    ni "Oh...kay.....you......go.....ngh....softer......now....."
    s "{i}Softer?{/i} No thanks. You gave me permission to do anything I wanted. So now, I’m going to destroy you."
    ni "Des...troy...pussy?..."
    s "Yes...good girl...how about I give you your reward now?"
    ni "Re......ward?......Akira....cum?..."
    s "That’s right, baby. I’m gonna fill you up now. You think you can take it all?"
    ni "C.....Cock......love.....cock!"
    o "{i}Ngh!...Mmn!{/i}"

    with sexfade
    with sexfade
    scene nikibasementpound32 with cumflash
    with hpunch

    ni "AAAAH!~"
    s "NGH!!!"
    ni "Haaah.......aaahh....."
    ni "Warm....so....warm...."

    scene black
    with dissolve2

    ni "So...{i}tired...{/i}"

    "I slide my cock out of Niki and watch as a good portion of her {i}reward{/i} oozes out of her crevice. "
    "She passes out immediately, but likely won’t stay under for long as I’ve seen her do this before only to have her rise like a phoenix just minutes later."

    o "{i}Hah...hah...what the fuck...what the fuck...{/i}"

    "Which means that if I’m going to talk to Otoha about this, {i}which I absolutely am as it could bring me one step closer to another tally mark,{/i} I need to do so now."
    "As such, I quickly throw my pants back on and make my way over to her, now collapsed on the stairs and looking {i}rather{/i} shameful."
    "She gazes up at me and says nothing."
    "I look down at her and reciprocate the silence."
    "Then-"

    stop music

    "We leave without looking back."

    $ renpy.end_replay()
    $ nikispring1 = True
    $ niki_love += 1
    $ niki_lust += 1

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "{i}Niki’s lust has increased to [niki_lust]!{/i}"
    "........."
    "......"
    "..."

    jump otohaspring3

label nikispring2:
    scene sky
    with dissolve2
    $ renpy.pause(1, hard=True)
    scene skyyy
    with dissolve2
    play music "normalday.mp3"

    "There’s a pep in my step as I step up the steps. And in other news, the sky is blue. Just this time there’s a smile too."
    "The smile is red, my girlfriend is dead, and for lack of more rhyming, {b}GET OUT OF MY HEAD.{/b}"

    play sound "static.mp3"
    scene sky with flash
    stop sound

    "Sorry."
    "Now, where was I?"
    "Oh, right. Walking."
    "Right now, I’m on my way home from the store — a place I’ve been regularly visiting lately on account of my niece being broken."
    "It was obnoxious at first, but I’ve come to somewhat appreciate these minor breaks in which I can pretend I’m a normal person doing normal things, buying normal products for his normal family."
    "But of course, the situation is anything but. And while I’ll tell myself the opposite to keep this half-smile plastered to my plaster face, each glance down reminds me that’s anything but true."
    "Because, you see, there’s something unfortunate inside this bag — one more symbol of my inadequacy and the ultimate mark that I’m a failure as a guardian."
    "Girls don’t work the same as boys do."
    "Things happen to them that don’t happen to us."
    "Unfortunate things. {i}Terrible{/i} things. And it’s easy for someone like me to forget what’s required in preparation for things like that when I’ve never had to do anything about them before."
    "But given that Ami can barely get out of bed as she is now..."
    "Do you see where I’m going with this?"
    "Yes, the task itself is simple. And not even remotely as abnormal or depressing as I made it sound with the opening words of this anecdote."
    "But it’s such a simple, baseline reminder of how absent I have been and how pathetic I am as a guardian to not think of this until asked."
    "I have never been present for anyone but myself. That’s what I keep thinking with each and every step up the steps. "
    "So yes, the sky is blue. Yes, my girlfriend is dead. But there is no {i}pep{/i} at all. "
    "Just a confused man fumbling his way through parenthood for the first time in his life while his makeshift daughter cries of embarrassment in the bathroom."

    scene black
    with dissolve2

    "I am a failure."
    "All I’ve done is feed her."

    "........."
    "......"
    "..."

    scene nikishome1
    with dissolve2
    stop music fadeout 10.0
    play sound "dooropen.mp3"

    s "..."

    "As I step into my home and place the bag down on the kitchen counter to avoid drawing attention to its contents, I recall a poem I used to love. But it’s strange that such a thing is possible now."
    "The contents of my past have been slowly bleeding back into me thanks to a metaphorical IV plugged into my arm by some girl with pink hair. "
    "And while it gets caught on things when I roll over too quickly — while the plastic skin-shovel holding it in place pinches me each time I forget it’s there-"
    "It does its job well. "
    "She does her job well."

    scene nikishome2
    with dissolve

    "I just wish she would fucking {i}listen.{/i}"

    scene nikishome3
    with fade

    "You’re probably wondering what poem I was talking about a second ago."
    "It’s called the Clod and the Pebble."
    "It’s a poem about love."
    "I won’t burden you with its entirety, you can find it on your own if your curiosity consumes you."
    "But there are two important lines I will leave you with before severing these thoughts once more."
    "Stanza one, line one — Love seeketh not Itself to please."
    "Stanza three, line one — Love seeketh only Self to please."
    "Note the capitalization."

    s "..."

    "Do you want to know what I keep in {i}my{/i} pocket?"
    "It’s a picture from before this all started."
    "A girl with twintails in a field full of flowers, backlit by a gorgeous sun nestled in the upper right-hand corner of the frame."
    "She’s smiling...laughing at something."
    "I wasn’t there for it, but I wish that I was."
    "Because now-"
    "I would kill for her."

    play sound "static.mp3"
    scene nikishome2 with flash
    stop sound

    "I love my niece."
    "And it is {i}my{/i} job to protect her."

    ni "Oh, you’re home."

    play sound "static.mp3"
    scene nikishome4 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    ni "I didn’t hear you come in."
    ni "Do you want tea? I just made some."
    s "This is my house."
    ni "Mhm."
    s "That’s my mug."

    scene nikishome5
    with dissolve

    ni "Mhm."
    s "Niki...{i}what are you doing?{/i}"
    ni "You weren’t answering the door so I let myself in. Is there a problem with that?"
    s "Yes. There is, actually. "

    scene nikishome6
    with dissolve

    ni "Ooooooh. Are you gonna {i}punish{/i} me? Fine. Just make it quick or my tea will get cold."
    s "I’m being serious, Niki. I told you not to come here. I told you I could handle this on my own."
    ni "Oh, was {i}that{/i} the conversation we had right before you boned me into unconsciousness? Cause my memory’s kinda hazy from around that time."
    s "Yes. Yes it was."
    s "And you agreed that you wouldn’t try to get involved with Ami."

    scene nikishome7
    with dissolve

    ni "I don’t know, Akira. That doesn’t sound like me."
    s "STOP FUCKING AROUND!"

    scene nikishome8
    with dissolve2

    ni "..."
    s "This...is {i}my{/i} responsibility. It’s something I need to figure out on my own. And that’s what {i}Ami{/i} wants as well. It’s not just me."
    ni "Akira...you are {i}not{/i} allowed to yell at me like that. That was not okay."
    s "You’re in my fucking house! "

    scene nikishome9
    with dissolve

    ni "I don’t care if I’m in your fucking {i}room!{/i} You don’t yell at me! {i}Especially{/i} when I’m just trying to help!"

    scene nikishome10
    with dissolve

    ni "Now, speak to me like a fucking adult or you’re going to wake Ami back up."
    s "Ami isn’t asleep, she’s-"
    ni "Yeah, she {i}is.{/i} I just {i}watched{/i} her fall asleep, asshole. She texted me asking for help because she didn’t trust you to buy the right fucking tampons."
    ni "But sorry, {i}what{/i} were you saying about how Ami wants you to handle this on your own?"
    s "You..."
    s "She..."
    ni "Apologize for yelling at me. Now."
    s "..."
    ni "{i}Now.{/i}"
    s "I’m sorry..."

    scene nikishome11
    with dissolve

    ni "You’re forgiven. See? That’s how easy it is to solve problems when you’re open to not being a little bitch about them."
    s "Did she really reach out to you?..."

    scene nikishome12
    with dissolve

    ni "Why do you sound so upset about that?"
    s "..."
    ni "Akira, you’re fighting a losing battle here. There’s no way you can handle Ami on your own. That’s why I wanted to help you."

    scene nikishome13
    with dissolve

    ni "She needs a woman in her life. There’s just...shit you don’t understand yet. And that’s {i}fine{/i} because you never learned. "
    ni "So if you want to think I’m overstepping some boundaries because {i}you{/i} did not invite me into your house, fine..."
    ni "But I urge you to think about what {i}she{/i} needs if you’re seriously invested in getting her out of this. Not what {i}you{/i} need. Because facing this alone will only make her worse."
    s "..."

    scene nikishome4
    with dissolve

    ni "So, do you want tea or not? Speak now or you’re not getting any."
    s "..."
    ni "Okay then. You’re not getting any."
    s "Can I have my mug back?"
    ni "Depends. Is there one that says “#1 Aunt” on it?"
    s "I...don’t think so."
    ni "Then no. You can have it back when you live up to the title. But for now, I’m going to hang onto it since {i}I’m{/i} the one who saved the day, not you."
    s "Niki-"
    ni "Just sit the fuck down and let me make you some god damn tea, asshole."

    scene black
    with dissolve2

    "Okay...so maybe my internal monologuing got a bit darker than it needed to before."
    "But can you really blame me? "
    "How was I supposed to know that Ami would reach out to {i}Niki{/i} instead of one of her friends? "
    "I’m sure Ayane could have done the same exact thing that-"
    "{i}You know exactly why.{/i}"
    "I don’t."
    "{i}Liar! She wants her mother but her mother’s dead!{/i}"

    play sound "static.mp3"
    scene amiani12 with flash
    scene amibus1 with flash
    scene amimakesyoudinner1 with flash
    scene nikishome14 with flash
    stop sound

    "{i}You know it’s true because YOU want her as well! You’re a hopeless piece of shit without her! You can’t do anything on your own!{/i}"
    "{i}You still hear her in the walls! See her reflection in the mirror! And you wish SO BADLY for her to tear down the barrier between life and death to RETURN TO FORM, but she never does!{/i}"
    "{i}So you cry and you fail and you fail and you cry and drag other WORTHLESS girls into your own bullshit problems because you can’t solve ANYTHING on your own!{/i}"

    play sound "static.mp3"
    scene nikishome15 with flash
    scene nikishome14 with flash
    scene nikishome15 with flash
    scene nikishome14 with flash
    stop sound

    "{i}I taught you better than this, my lightning-bug.{/i}"
    "{i}Should I have nibbled on your ear more? Sliced your scrotum with my nails?{/i}"
    "{i}What could I have done to make you better?{/i}"

    ni "Akira...I’m going to ask you again...but do you want to talk or not?"
    ni "Not just about Ami...about {i}everything.{/i} Because I know this runs deeper than just her."
    s "Can we pick just one problem and focus on that instead?"
    ni "If that’s easier for you, sure. But without knowing where to begin, I-"
    s "I don’t want to be a parent."

    scene nikishome16
    with dissolve

    ni "..."
    s "I’m not cut out for it. You know that. Ami knows that. {i}Everyone{/i} knows that. And it really fucking sucks because I {i}have{/i} to be one now and I’m failing so badly that it’s dragging people like you into it."
    ni "I’m here because I want to be, Akira. Not because I {i}have{/i} to be. And besides, I don’t want to be a parent either. "
    ni "But, like you said, sometimes you kind of {i}have{/i} to be one. Even {i}if{/i} it sucks. But that doesn’t mean you can’t figure out a way to make it suck a little less."
    s "There’s this girl in my class who idolizes you, you know. More than even Ami does. "
    s "Her father left her and her mother died. And she has a little sister with some kind of fucking...auto-immune disease that she’s been taking care of ever since."
    s "She makes it look so effortless and she’s only half my age. Why can’t I do that?"
    s "And Kaori- you remember her, right? She has a child of sorts too now."
    ni "I’m aware. She fell asleep on my shoulder. "
    s "Then you probably know that Kaori is better at this than I am as well. {i}Kaori.{/i} She doesn’t even know what hands are called."
    s "Why can’t I be like them? Why can’t I do this alone?"
    ni "Are you asking me for advice or do you just want me to listen?"
    s "Advice. Please. I have no idea what to do."

    scene nikishome17
    with dissolve

    ni "{i}Hah...{/i}"

    scene nikishome18
    with dissolve

    ni "Ready for me to sound pushy and overbearing?"
    s "Sound however you want if it will get me out of this mess."
    ni "Akira, nothing is ever going to get you {i}out{/i} of this mess."
    ni "Even when Ami is old enough to move out...and head off to college or...do whatever it is she wants to do with her life, you’re still going to be her dad. You stopped being an uncle a long fucking time ago, babe."
    ni "And that means you’re always going to worry about her. "
    ni "Take {i}my{/i} dad for example. Did you know he still calls me after every single concert to ask me how things went? "
    s "Are you just bragging now? This isn’t a situation where I can just ask Ami how she is and have her instantly get better."
    ni "I’m not {i}bragging,{/i} asshole. I’m just giving you an example of how the kind of bond you have with Ami is one that’ll never go away no matter {i}what{/i} happens."
    ni "She’s all you have and you’re all {i}she{/i} has. And that makes that connection even stronger. So there’s no way you can just {i}get out{/i} of it and looking at things that way is all wrong."

    scene nikishome19
    with dissolve

    ni "But...she won’t be heading off to college for at least a few more years. Which means you need to make the most of the time you’ve got left with her."

    "{i}Tell her! About the rooftop! About the girl with aquamarine eyes!{/i}"
    "I will tell her nothing."
    "{i}Tell her! Tell her, Akira!{/i}"
    "She does not deserve this pain."

    ni "And one way I think...to make the most of that time together..."

    scene nikishome20
    with dissolve2

    ni "Is to give her a real family again."
    ni "Or at least...something that resembles one."
    ni "Let me move in with you. Let me be her mom. "
    s "Niki-"
    ni "I know how it sounds, which is why I gave you that warning about how it was going to be pushy and overbearing. But you’ve gotta admit- it makes a lot of sense, right?"
    ni "Like, not only does Ami trust me to do what you can’t, but I don’t even really {i}have{/i} a place of my own yet. "
    ni "I basically just bounce around between hotels all the time and...crash with my parents when I’m not doing that. Living here would give me a...base of sorts."
    s "I don’t think Ami would want that, Niki. This is...way bigger than just bringing her emergency feminine hygiene products."
    ni "If she tells me she doesn’t want me here, we can throw out the idea. I’m only suggesting it because A) I care about her. And B) I love you."
    ni "I’m a saint, yes. But even {i}I{/i} wouldn’t offer to move in and become a pseudo-parent if both of those things weren’t true."
    s "As...nice as that sounds...I was hoping for advice that would maybe make things a little easier for me to do this on my own."

    scene nikishome21
    with dissolve

    ni "Baby, I love you, but {i}no.{/i} I can’t let you kill yourself {i}and{/i} your niece because you’re too stubborn to accept my help."
    ni "Ami’s going to get sick if you keep this up. {i}Physically{/i} sick. Like, what have you even been feeding her?"
    s "Whatever I can find. All I have to do is get her back to normal so she can start cooking for herself again. It’s okay if she doesn’t have a perfectly balanced diet until then."
    ni "But without a timeline on {i}when that will happen,{/i} you’re putting the poor girl at risk. And that’s not even touching on what she’s done to her hair."
    ni "I can fix that too, you know. I used to cut yours when we were kids, remember?"
    s "Again, I wish I did..."

    scene nikishome22
    with dissolve

    ni "God, I’ve gotta stop fucking asking if you remember things. It always depresses the fuck out of me when you don’t."
    s "Niki...even if Ami is okay with you living here, which she won’t be...I don’t think it’s something {i}you{/i} want to do."

    scene nikishome23
    with dissolve

    ni "Why would it not be something I want to do?"
    s "Because not only will you have to see my face first-thing every morning, but it will get in the way of your career."
    ni "I’m a professional, Akira. I think I can manage."
    s "Sure, you {i}think{/i} you can manage. But the second you trip on stage or...forget a line of a song because you’re worrying about what Ami’s eating for dinner, you’ll need to make a choice."
    s "And that’s not a situation I want to put you in."
    ni "Akira, I’m 29. My years as an idol are numbered as-is. And frankly, it’s a miracle I’ve lasted this long to begin with."
    s "But still, I can’t do that to you. You’re too...valuable. You’re too {i}good.{/i}"
    ni "You could list a zillion other positive adjectives to describe me, but none of them change the fact that I’d throw everything away for the life I {i}really{/i} want."
    ni "And you’d never guess what it is I see first-thing in the morning in that ideal world, Akira. But, spoiler alert, it’s the same thing I’d see right before going to sleep — you."
    s "I definitely could have guessed that based on context."
    ni "Yeah, well you didn’t guess it fast enough and you’re a jerk for even questioning my commitment at this point. Let’s talk to her."
    ni "Only if you’re on board, though. Because if you really {i}do{/i} think I’m proposing this too soon then, A) I’m sorry. And B) How much fucking longer do you need? Because we’ve known each other forever."
    s "..."
    ni "At the very least, please-"

    play sound "static.mp3"
    scene nikishome24 with flash
    stop sound

    ni "Oh! Hey, Ami. We didn’t wake you up, did we?"
    a "..."
    s "..."

    play sound "dooropen.mp3"
    scene nikishome25
    with dissolve

    ni "Okay. I guess she’s just...using the restroom."
    s "I’ll ask her."

    scene nikishome26
    with dissolve

    ni "So...you’re okay with it? With {i}me?...{/i}"
    s "Ami deserves a better life..."
    ni "But...are {i}you{/i} okay with it, Akira? Because I don’t want to do this if you’re {i}only{/i} doing it for Ami. "
    ni "And, no offense, but you have a hard time making decisions when there’s more than one variable involved."
    s "..."
    ni "Akira?..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    s "Which side of the bed do you prefer to sleep on?"

    $ renpy.end_replay()
    $ nikispring2 = True
    $ niki_love += 5

    "{i}Niki’s affection has increased by 5!{/i}"
    "{i}You worry how many eggs your nest can hold.{/i}"
    "{i}There is no easy way to find out.{/i}"
    "{i}Night comes.{/i}"

    jump nightch4

label beachfive8:
    "{i}Meanwhile...{/i}"

    scene nikiamicards1
    with dissolve2
    play music "wewereangels.mp3"

    a "TSA guidelines now prohibit {i}Go-Gurt{/i} on airplanes..."

    scene nikiamicards2
    with dissolve

    a "What’s Go-Gurt?"
    ni "It’s like a...tube of yogurt. For people who want to eat yogurt on the go."
    a "Are there actually people like that?"
    ni "There won’t be for long if the TSA has anything to do with it."

    scene nikiamicards3
    with dissolve

    a "Okay. Well...I guess that one wins then?"
    ni "It’s not like there are any other options to choose from. Playing this game with two people doesn’t really work well, does it?"
    a "No...but at least we’ll both win? "

    scene nikiamicards4
    with dissolve

    ni "Is there anything you want to do instead, Ami? Maybe we could watch a movie or something? I brought a few of my old concert DVDs as well since I know you’ve been wanting to see them."
    a "I’m fine with anything, really. Just being here with you makes me happy."

    scene nikiamicards5
    with dissolve

    ni "Didn’t I tell you to stop saying things like that when the two of us are practically family already?"
    a "Yeah. But I’m {i}actually{/i} family with Dad and I still say stuff like that to him all the time. Why should I not be happy to spend time with the people I love?"

    scene nikiamicards6
    with dissolve

    ni "F...Fair enough. I just wasn’t sure if you were saying that because I’m your favorite idol or because you actually like {i}me,{/i} you know."
    a "Of course I like {i}you,{/i} Niki. You’ve been so nice to me lately...always coming over to check in on me. Taking care of me while Dad is gone."
    a "Though, I’m not really sure why I need to be taken care of in the first place when I’ve more than proven that I can take care of both myself {i}and{/i} someone else."
    a "When I’m not busy accidentally stabbing them, at least."
    ni "I think it’s less “taking care of you” and more just “keeping you company” so you don’t get bored while all of your friends are at the beach."
    a "They’re not really my friends anymore."

    scene nikiamicards7
    with dissolve

    ni "Ami, that’s not-"
    a "Yeah it is. The only ones who have bothered checking in on me this whole time have been Ayane and Maya. Even the other girls at the maid cafe have been kind of weird to me."
    a "Which is fair. I {i}did{/i} threaten to dismember them and all. But it’s okay. Really. I don’t need that many friends. Just my family and the other members of the Love Squad are enough for me."

    scene nikiamicards8
    with dissolve

    ni "Love Squad?"
    a "That’s the name me and Ayane gave our group of friends since we all love Dad and will do anything he asks of us. Maya hasn’t accepted she’s a member, but we all know she is."
    a "It’s kind of annoying, really."
    ni "So Noriko and I aren’t in the Love Squad? How’s that fair? I’ve loved Akira even longer than you have if you want to get technical about it."
    a "That’s true. But you only {i}just{/i} came back into his life a little while ago. So you weren’t around when the group was formed."
    ni "Also, Ami. It’s not really healthy to say things like “we’d do anything he asks of us.” He’s your Dad-slash-uncle, not your boyfriend."

    scene nikiamicards9
    with dissolve

    a "Ooooh, did I make you jealous just now? Is my love for my dad so strong that even his childhood friend is envious of it?"
    ni "Of course not. I just don’t want you thinking your entire life revolves around him when you’re going to grow up and fall in love with someone else one day."

    scene nikiamicards10
    with dissolve

    a "Pass!"
    ni "Pass?"
    a "Yeah. I’m never going to fall in love with anyone else. I’m not interested in that."
    ni "I mean...you say that {i}now.{/i} But you never know what will happen in the future and-"
    a "Sure. But {i}you{/i} never fell for anyone else, did you? What makes you think that I’m any different?"
    ni "Probably the part where I’ve just been hopelessly in love with Akira for my entire life and that I’d never be able to break free even if I wanted to."
    a "Yeah. And it’s the same for me. I’m just also related to him."
    ni "Which would make a relationship with him even more illegal than it already is."

    scene nikiamicards11
    with dissolve

    a "Some laws are meant to be broken."
    ni "..."
    ni "Ami, {i}why{/i} do you look at him like that?"

    scene nikiamicards12
    with dissolve

    a "Huh? What do you mean?"
    ni "You know what I mean. These feelings you have aren’t normal. I’m worried about you."
    a "You’re worried about me because I have romantic feelings for my dad?"
    ni "Yes. Literally yes. That is a thing that people worry about."
    a "Why?"
    ni "Well...it’s just...{i}weird.{/i} And there’s a power dynamic at play here that makes things really...icky. "
    a "But it’s okay if the feelings are just one-sided, isn’t it? "
    a "It’s not like Dad has ever {i}capitalized{/i} on my feelings for him. Which he could if he wanted to. But then me and you would have to fight and I don’t want that because I like you."
    ni "..."
    a "Did I...say something wrong?"

    scene nikiamicards13
    with dissolve

    ni "No...yes? I don’t know. It’s just a little difficult for me to understand you sometimes since I’ve never wanted to sleep with any of my family members."
    a "Not even in your fantasies?"
    ni "Of course not, Ami."
    a "Wow. That’s kind of crazy to me."

    scene nikiamicards14
    with dissolve

    ni "Yeah, because you’re a creepy little gremlin with no grasp on the laws of the land and I’m a mostly normal girl with {i}abnormal{/i} taste in boys."
    a "Guess that makes me a little abnormal too then, huh?"
    ni "A little? "
    a "A girl’s first love is always her father, Niki! "
    ni "But Akira-"

    scene nikiamicards15
    with dissolve

    ni "Ugh. Forget it. We can continue this another time. "
    a "Can we?"

    scene black
    with dissolve2

    ni "Do you want anything from the kitchen? I think I’m gonna make some food. Akira said you had some stuff in the fridge for the two of us to share."
    a "Mmmm...can you make tea? I finished mine right before the TSA banned portable yogurt."

    scene nikiamicards16
    with dissolve

    ni "Sure thing, Ami. No food?"
    a "No thanks! I’m not really hungry right now."

    "As Niki Nakayama peered through the confines of the Arakawa family refrigerator, she wondered about the best way to tell her prospective daughter that incest is wrong."
    "It was a situation she hadn’t ever imagined finding herself in until the thoughts of moving into this place begun, but it was one she was now mostly prepared to confront."
    "What she did not know is just how impossible such a task would be as Ami Arakawa had never even {i}considered{/i} being with someone who doesn’t share her blood."
    "The blood was what turned her on. She’d dream of bathing it. Drinking it. Filling up a cup and pouring it over her head in the midst of an orgasm to further accentuate those impure feelings."
    "Just that’s not what she really thought. Probably. Most of the time. Some of the time. Maybe she never thought of blood at all. Maybe she was hemophobic. Maybe she wasn’t even real."
    "But whatever the case, Niki’s plan was never going to work. And that was something she’d have to eventually resign herself to if she ever {i}did{/i} want to become Ami’s mother."
    "Which she shouldn’t. She should get away from here as quickly as possible. She should change her name and marry a salary-man or a music producer or something like that."
    "But she keeps wanting to fuck Akira Arakawa and his magic cock because it’s the only cock she’s ever known and it’s a good one so why bother finding another when-"

    if amifingered == False:
        $ renpy.pause(5, hard=True)
        stop music
        scene black
        "{b}THE MIDDLE SECTION OF THIS SCENE HAS BEEN REDACTED DUE TO AN INCORRECT CHOICE THAT HAS RESULTED IN MISSING ASSETS{/b}"
        "{b}THE CUM JAR CAN NOT BE DETECTED, YOU FLACCID FUCK BOY, YOU.{/b}"

        play sound "static.mp3"
        scene nikiamicards22 with flash
        stop sound
        play music "wewereangels.mp3"

    else:
        scene nikiamicards17
        with dissolve

        ni "Hm?"
        ni "What’s that in the back of the freezer?"

        play sound "static.mp3"
        scene nikiamicards18 with flash
        stop sound

        a "Nothing!"
        ni "What? When did you get there?"
        a "It’s nothing! Don’t even worry about it! In fact, why don’t we order a pizza?! Or Chinese?! Frozen food isn’t great for you, you know?! And you should really watch your figure as an idol!"
        ni "You’re being...kind of weird, Ami. Like, even more than normal."

        scene nikiamicards19
        with dissolve

        a "Hahahaha! That’s me! Head completely empty! Nothing in there but controversial views on familial relationships! And kittens! And anime! I’m such a goober! Hahahah!"
        ni "..."
        a "Hahahahahahah! Hahahah...hahaha..."
        ni "You good?"

        scene nikiamicards20
        with dissolve

        a "Yup! But why don’t we just close this and..."

        scene nikiamicards21
        with dissolve

        a "There! All better. Now, you won’t have to worry about contaminating your precious body with all of that {i}junk,{/i} am I right?"
        ni "I...guess so?"

        scene black
        with dissolve2

        a "Great! Movie time it is, then!"

        "........."
        "......"
        "..."

        scene nikiamicards22
        with dissolve2

    "The two girls sat down on the couch, clearing the table of games best played in groups and replaced them with drinks and stacks of DVDs they knew they weren’t going to watch."
    "And in this moment, the two of them were happy. The two of them were at peace. Like mother and daughter."

    play sound "static.mp3"
    scene nikiamicards23 with flash
    stop sound

    "But the real mother was there too. Well, not {i}real.{/i} But also kind of real. The ghost mom! The one who liked children in {i}every{/i} way possible."
    "In a dark corner of the room, just out of reach of the television’s glow, she stood there in all her ghostly envy — wishing {i}she{/i} could be the one providing a lap pillow right now."
    "But unfortunately (or fortunately based on who you ask) she was very, very dead. And also very, very mad that this impostor would try to take her place."
    "Niki Nakayama did not feel this gaze."

    scene nikiamicards24
    with dissolve2

    "Ami Arakawa did."
    "But she was unsure of what she was supposed to do about that."
    "On one hand, she loved her mother. On another hand, she loved Niki. And she {i}longed{/i} for the lap of an older woman but, once more, not in the yuri kind of way."
    "This much was fine though, wasn’t it? "
    "She wasn’t openly welcoming her into the home. And she’d been as polite as possible earlier in letting Niki know that she would steal her “boyfriend” away without a second thought."
    "That damage — the broken piece of furniture she was would {i}surely{/i} dissuade her idol from joining the household, would it not?"
    "If each bed was broken — each floorboard cracked, then Niki would take her kindness elsewhere and leave Ami to her castle of callous thoughts. Again, {i}not a hint.{/i}"
    "And again, incorrect. For in the throes of those happy thoughts, peace would break apart when the two of them realize there’s only room for one on their make-believe raft."

    a "I’m sorry..."
    ni "Sorry for what, Ami?"
    a "..."

    "I don’t know which of them she apologizes to, but I like to believe its both."
    "I like to believe that Ami did not just {i}feel{/i} the presence of her very, very dead mother, but that she {i}saw{/i} her. That she could hear her breathing."
    "That she could listen closely to the way her ghostly feet made contact with those cracked floorboards so vividly that she could make out the shape of them."
    "And I want to believe that because that’s how this story {i}should{/i} go."
    "This house has not been a home for a very long time. And it deserves a scene like this {i}devoid{/i} of the negative connotations that make it, for lack of a better word-"
    "Doomed."

    ni "You know..."
    ni "You’ve never really told me about your mom before."

    scene nikiamicards25
    with dissolve

    "The ghost’s attention was piqued."
    "She’d heard her daughter speak of her before and hung on every single word. But never in the presence of one who may take her place."
    "Would her words remain the same? Or had the seeds of self-doubt already been sown in her precious little girl’s field of dreams?"

    a "..."
    ni "You don’t have to talk about her if you don’t want to. I get how hard it is for you. Akira too."
    ni "You both really loved her, didn’t you?"
    a "She was..."
    a "The closest a girl could ever come to perfection."

    scene nikiamicards26
    with dissolve

    ni "Oh yeah? How so?"
    a "Just...{i}everything.{/i} She was pretty. She was funny. She was talented. And she loved me...{i}so{/i} deeply that I’ve never felt anything like it."

    scene nikiamicards27
    with dissolve

    a "She’s what I want to be...my hero. But she was way smarter than me and I highly doubt I’d ever be able to catch up even if I gave it my all."
    ni "That’s not true, Ami. You’re young. You’ve got plenty of time to catch up."
    a "No, you don’t get it...She wasn’t smart like {i}normal{/i} people are smart. She {i}understood{/i} things. Things about God...things about the world...all sorts of things."
    a "Her words alone could change the way you see. They could change what you hear...what you {i}think.{/i} She was so good at just...impacting people. Changing people."
    a "I saw it every day when she was raising me. How everyone fell in love with her at first glance. And it was like she took that love and just...bundled it up to give to me."
    a "I remember one day...I was probably only four or five back then...but she took me to the top of a hill where you could overlook the whole city."

    scene nikiamicards28
    with dissolve

    a "She put me up on her shoulders...and even though she was so small and skinny, I never thought for a second that I was going to fall."
    a "She sung to me...spun me around beneath her favorite tree...read me some of her favorite poems...and I still dream about that day sometimes. "
    a "How it was like we were the only two people in the world. And sometimes, I wish we were."
    a "Sometimes, I wish I could rewrite the past. Figure out a way to put someone else in her place so that {i}they{/i} could die instead of her. "
    a "And yeah...I know that’s an evil thing to think. But she’s worth it. She’s worth more than anyone. She was just {i}that{/i} perfect."

    scene nikiamicards29
    with dissolve2

    a "That’s all just a fantasy, though."
    a "The truth is no one could {i}ever{/i} replace her. Not even in death. "
    ni "..."
    a "She still watches over me. I can feel her. I can smell her sakura perfume. "
    a "And I just hope that she’s proud."
    a "I’ll die happy if I can be half the mom that she was. I just wish I could explain it better."
    a "It feels like anything I say doesn’t even come close to painting a real picture of her. But that’s just one more example of how she was everything I’m not."

    scene nikiamicards30
    with dissolve

    sekni "Ami..."

    play sound "static.mp3"
    scene nikiamicards31 with flash
    stop sound
    stop music fadeout 10.0

    ni "Huh?"
    a "Niki?..."
    a "What’s wrong?"
    ni "Nothing, I..."
    ni "I just thought I...heard something."
    a "The washing machine maybe? I threw my uniform in there a little while ago."
    ni "Yeah..."

    scene black
    with dissolve2

    ni "Yeah...that must have been it."

    "It wasn’t."

    $ renpy.end_replay()
    $ beachfive8 = True

    "{i}Niki’s sanity has decreased by 1!{/i}"
    "........."
    "......"
    "..."

    jump beachfive9

label nikispring3:
    scene sky
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "That funny feeling starts to fade halfway through the bus ride. Something else died near the side of the road."
    "Its guts were left out on display for the few of us who stayed for breakfast, making the meal less than worth it and one more batch of intestines away from being emptied out into one of the aisles."
    "The sun is bright, at least. It kind of has to be. It’s made of fire. Did you know that?"
    "Anyway, yeah. Dead bodies and bus rides. That’s been the morning so far. That and the casual admittance of sex with two parties sometime during a party without sex."
    "If that doesn’t make sense, it’s because it doesn’t make sense. And nothing ever makes sense. But we keep on trucking anyway because people are a lot like truck drivers."
    "Moving from one place to the next. Urinating in plastic jugs because we’re too lazy or busy to pull off to the side of the room. And sometimes you miss. Sometimes you become the pee boy."
    "But the fact of the matter is that facts don’t matter, matter does. And since we all have to share it, we might as well figure out the best ways. "
    "So I unfold a piece of paper I found in my pocket this morning. I don’t know how it got there, nor do I understand the words written in red ink across it. But it reads, “see me in the spring time.”"
    "Does this mean it was written in one of the better seasons?"
    "Are there any seasons better than this?"
    "Or does the writer only write what needs to be written, for that is the right thing to do?"
    "I don’t have an answer for you. And I don’t have a solution for me."

    scene black
    with dissolve2

    "But the bus pulls up to where it’s meant to drop me off and I leave, passing a girl waiting outside holding a briefcase on my way out."
    "I wonder where she’s going. Why she looks so familiar. Which row she sits in when she gets on the bus. But it’s on the opposite side of the street, and I never get to see."
    "I roll up my sleeves, then roll them back down as I want to look cool but always hate the sensation of something gripping me a little too tightly. And sleeves are like children you can never get rid of."

    scene livingintheroom1
    with dissolve2

    "I prepare myself to open the door. To see those shadows in suspicious places that never quite match the light. And I wonder to myself if I really am inside of a video game."
    "To some extent, I probably am. But to some extent, I’m probably not. My feelings are feelings. My dreams are dreams. So does it really make a difference the amount of pixels and promises I can fit in one hand?"
    "I ask you this question as a man about to give a part of himself away. Or one who attempts to create another part so that he can continue to exist in the presence of someone kind."

    play sound "dooropen.mp3"
    scene livingintheroom2
    with dissolve

    s "Ami? I’m home."
    a "Dad!"

    play sound "static.mp3"
    scene livingintheroom3 with flash
    stop sound

    a "Welcome back! We were just talking about you!"

    "Two girls with the seasons in their hair — one just right while the other’s cut short. But every day it grows some more. And both are bright. Both are beautiful. "
    "They look like a pair. The kind that comes shrink-wrapped."

    ni "How was your trip? Did you have fun?"
    s "..."

    scene livingintheroom4
    with dissolve2

    a "..."

    "I struggle to speak, for it feels like I’ve stepped out of {i}my{/i} world and into another. One where I never made mistakes and never cut my hand."
    "But if I never cut my hand, I’d have never cut my knee. And if I never cut my knee, I’d have never felt the touch of the departed as it lingers on my softskin. That untimely desperation. The cancer it became."

    s "..."
    s "Yeah."
    s "It was fun."
    a "That’s great! {i}We{/i} had lots of fun too. Niki even brought one of her old costumes for me to try on! But I don’t want to talk about why it didn’t fit. "

    scene livingintheroom5
    with dissolve

    ni "Maybe one day, Ami. Not everyone can be born {i}gifted.{/i}"
    a "I’ll show all of you one day. Mark my words. I’m just one of those “late bloomer” types. "
    s "So apart from your boobs basically not existing, how did it feel wearing the costume? It didn’t light some sort of spark that will propel {i}you{/i} to become the next top idol, did it?"

    scene livingintheroom6
    with dissolve

    a "Me? An idol? I wish. I barely pass as a maid. "
    ni "I say you should go for it. It’d be fun tormenting your dad by having {i}both{/i} of his favorite girls wind up as super popular, super famous idols who could get anyone they want but wind up with {i}him.{/i}"
    s "I’m not sure if “torment” is really the right word there. I’m really proud of you, Niki. And Ami...well, I’m also proud of you. Just in a different way."

    scene livingintheroom7
    with dissolve

    ni "I’m sure you {i}are{/i} proud. But the truthier truth is that you’re {i}totally{/i} jealous that there are a trillion other guys and girls thinking {i}impure{/i} things about me every day. "
    ni "Now, imagine they were doing that same thing about {i}Ami.{/i}"
    s "I would kill them."

    scene livingintheroom8
    with dissolve

    ni "I rest my case."
    a "Yay! Murder!"
    a "But in a context that doesn’t make me look like the bad guy!"

    scene black
    with dissolve2

    "I drop what little luggage I have off in my room before coming back out to have the girls fill me in on their weekend alone together."
    "All things considered, this was a bit of a trial run. And that was the exact intention I had in mind when I asked Niki to do it. "
    "But I guess I must have been a little pessimistic as I didn’t expect her to agree so readily."

    scene livingintheroom9
    with dissolve2

    "She’s serious about this “moving in” thing. The matching pajamas were the straw that blew the camel’s back out or however that one phrase goes. "
    "But there’s a glaring problem with them — as they have overthrown that downtrodden, unkempt look from our tour down memory lane that I previously crowned as the most attractive she’s ever been."
    "In this moment, I want her more than ever before. And I’m sure that was calculated on her behalf as I now have no desire to back out from something that may very well change my life."

    ni "Coffee? Ami taught me how to make it the way you like."
    s "..."
    a "You guys are looking a little close there, aren’t you?"

    scene livingintheroom10
    with dissolve

    ni "Got a problem with that, loser? Akira and I aren’t blood-related. That means I’m {i}allowed{/i} to get all close to him."
    a "Those laws will change one day! I just have to wait for Nodoka to become the prime minister, I think. Unhand my father!"
    ni "Nnnnnnnnnno! Phbhhbhht!"
    a "Dad! Tell Niki to-"
    s "Ami..."

    scene livingintheroom11
    with dissolve2

    s "How would you feel if Niki moved in with us?"
    ni "You’re sure you want to do this now? You don’t want coffee first?"
    a "Yeah, you should probably have some coffee first. You’re clearly super-tired since that made like zero sense to me."
    s "What part of it didn’t make sense?"

    play sound "static.mp3"
    scene livingintheroom12 with flash
    stop sound

    a "The part where you’re inviting a famous idol to come live in our tiny house that barely fits the two of us when it’s always been just you and me. Go on, have some coffee."
    ni "Why don’t...I just go and brew that now? I’ll give you two a second."

    play sound "static.mp3"
    scene livingintheroom13 with flash
    stop sound

    s "So you’re against it? "
    a "Against what? Was that not just one of those hypothetical thingies? "
    s "No, it wasn’t. In fact, this is something I’ve been wanting to talk to you about for a while now."
    a "Dad, come on. You can’t just invite Niki into our house like this without even asking {i}her{/i} first! She’s one of the busiest people in the whole city. "
    a "And if word got out that she was living with her childhood friend, it could ruin her career! You’ve really gotta think these things through before just blurting them out like that, silly."
    ni "Umm...if I may interject-"

    scene livingintheroom14
    with dissolve

    ni "This was actually...{i}my{/i} idea."
    s "Niki, I’ve got this. But thank you."

    scene livingintheroom13
    with dissolve

    ni "Okay. Back to coffee. I’ve never used this Kalita Wave thing before, though, so be prepared for potential failure."

    play sound "static.mp3"
    scene livingintheroom15 with flash
    stop sound

    a "Now I’m even more confused. Why would this be Niki’s idea? "
    a "Like, I get that she loves you and stuff. And that’s fine. But wouldn’t moving in together be a little too {i}serious?{/i} Only families are supposed to live together, not friends."
    s "Yeah, that’s what I’m trying to say. {i}That’s{/i} why Niki wants to move in."
    a "Are you guys actually related or something? Because that would be a crazy plot twist."
    s "Ami, no. We-"

    scene livingintheroom16
    with dissolve

    a "Ooooooh! It’s because she made me an honorary Nakayama sister. I get it now. She {i}has{/i} been saying I’m like family a lot lately, so that tracks. And it’s really sweet, but no thanks. "
    s "Just listen to me, okay? Niki is-"

    play sound "static.mp3"
    scene livingintheroom17 with flash
    stop sound

    ni "Now an active participant in this conversation. I used the normal coffee brewer. It should be done in a few minutes."
    s "Niki, I can handle this."
    ni "I’m sure you can, babe. But I think it’s best if I speak for myself here so Ami doesn’t keep misunderstanding everything."
    a "{i}Babe?{/i} I don’t like that. Call him Sensei or something. Even “Dad” is fine since we’re technically sisters, right?"
    ni "Ami, didn’t you have fun this weekend? Wasn’t it nice having an older girl around here for once?"
    a "I mean...yeah. It was a lot of fun. I really liked spending time with you."
    ni "And I really liked spending time with you. So wouldn’t it be nice if that’s just how things {i}were{/i} from now on? "
    ni "Like yeah, I’ve got a busy schedule {i}now.{/i} But I’m also nearly thirty years old and the chances of my career lasting more than a few more years are pretty slim, don’t you think?"
    ni "After that, I’ll be free to coast off of residuals and convention signings for the rest of my life. I’ll have practically all the time in the world. And I want to spend as much of that time as I can with you."
    a "Niki, with all due respect, that last part sounds like something a mom would say. So why not just reword that part and-"
    ni "Ami, you’re not getting it. That’s {i}exactly{/i} what I want."

    play sound "static.mp3"
    scene livingintheroom18 with flash
    stop sound

    a "No, I’m not getting it. That doesn’t make any sense."
    ni "Oooookay, then I’ll be as blunt as I possibly can."
    ni "I’m in love with your dad, and I want to move in so I can become your new mom. Which isn’t to say I think I can {i}ever{/i} replace your {i}real{/i} mom. That’s absolutely not what I’m trying to do. "
    ni "But I love you, and I want to be here for {i}both{/i} of you. I want {i}this{/i} to be my life now. And if I can’t balance that with work, I will quit. This is what’s most important to me."
    a "Maybe you should have some coffee too, Niki? You’re acting kinda crazy."

    play sound "static.mp3"
    scene livingintheroom19 with flash
    stop sound

    s "{i}Should we maybe try again some other time?...I’m not sure if this is going to work...{/i}"
    ni "No, we shouldn’t try again {i}some other time.{/i} She needs to get it {i}now{/i} or she’s just going to give us this same runaround every single time we try because she knows it’ll work."
    ni "Ami, I know you don’t approve of me being {i}with{/i} your dad, but that’s not {i}up{/i} to you. He can make his own decisions."
    a "If he can make his own decisions, why do you keep talking over him? Why aren’t you just making coffee right now? "

    scene livingintheroom20
    with dissolve

    ni "I’m {i}not{/i} talking over him. In fact, if we {i}were{/i} to toss somebody out of this conversation, which we shouldn’t since that not what families do, it would {i}be{/i} him. This is about you and me, isn’t it?"
    ni "{i}He’s{/i} already approved of this. But {i}you’re{/i} the one who needs to approve of it next since we {i}all{/i} have to be involved. Which is why I have to figure out a way to get through to you."
    ni "So what’s the main problem? Is it that I’m in love with him? Is it that you think I’m trying to be the next Sekai? Is it that you’re afraid you guys won’t get any alone time together anymore? What is it?"

    play sound "static.mp3"
    scene livingintheroom21 with flash
    stop sound

    se "{i}All of the above.{/i}"
    a "It’s all of the above, obviously. "
    a "Weekends are one thing, but I don’t know how to be a part of an {i}actual{/i} family. I haven’t done that since I was a little kid. Let alone with someone who doesn’t even share my blood."
    se "{i}And it would really suck to hear them going at it all the time, wouldn’t it?{/i}"
    a "Plus, if I have to hear you two having sex every night, I’m probably just going to off myself."
    se "{i}Unless they let you join in.{/i}"
    a "Unless you let me get in on it, of course."

    play sound "static.mp3"
    scene livingintheroom22 with flash
    stop sound

    ni "Ami! This isn’t something we should be joking about right now! "
    a "Who said I’m joking? I’m not joking. I’m super serious. I think that sounds fun, actually. "
    ni "Ami, no one said anything about sex. The thought hasn’t even crossed my mind. "
    a "Wow, what’s {i}that{/i} like?"

    scene livingintheroom23
    with dissolve

    ni "Normal. What matters most to me is making both of you happy. And if you’re 10000%% sure you can do that without me, okay. We can leave it at that and I’ll give up for now. "
    ni "But there are going to be more moments than you can even {i}count{/i} where you’ll wish you had someone like me to share them with."
    a "I have Sen- Dad. That’s plenty. "
    ni "But {i}he’s{/i} not going to paint your nails. {i}He’s{/i} not going to have spa days with you or play dress-up with you or even {i}understand{/i} you because he’s just a stupid boy."
    ni "And yeah, {i}some{/i} boys would be great at that. There are millions of single fathers out there who can do {i}everything{/i} for their daughters. But {i}he{/i} isn’t one of them."

    scene livingintheroom24
    with dissolve

    ni "And that’s okay..."
    ni "Not everybody has to be strong. There’s {i}no{/i} problem asking for help. And it’s not like your dad {i}chose{/i} this life."
    ni "He’s doing all he can and he loves you {i}very{/i} much..."

    scene livingintheroom25
    with dissolve

    ni "But he needs help, Ami. He can’t do this alone. Which is why I volunteered to step in and become a part of this family if you’ll let me. "
    ni "The two of you have been through {i}so{/i} much. More than anyone should ever have to. And I get that that’s why you’re so adamant about continuing this way since you’ve already come so far."
    ni "But it’ll always be easier to eat cereal with a spoon than a fork."
    a "..."
    s "..."
    a "{i}What?{/i}"

    play sound "static.mp3"
    scene livingintheroom26 with flash
    stop sound

    ni "It’s a dumb analogy {i}my{/i} mom used to say to me when I was little since I’m just as stubborn as you two. "
    ni "Just because you can do things the harder way doesn’t mean you {i}should.{/i} Things are so much easier if you just use the right tools. "
    ni "Ami Arakawa, let me be your spoon."
    a "..."
    ni "Yes, I am aware of how dumb that sounds."

    scene livingintheroom27
    with dissolve

    a "Dad...do you really think you need help?..."
    a "Are you actually struggling that much?..."
    s "..."
    ni "..."
    s "I need help, Ami."
    s "I can’t figure all of this out on my own."
    s "And I think Niki is the missing piece of our puzzle."
    a "But..."
    a "Inviting her into our home..."
    a "Do you really understand what that means?..."
    s "She already told you...she isn’t trying to replace anyone."

    scene livingintheroom28
    with dissolve

    s "She’s just an idiot who loves us for no discernible reason."
    a "Yeah...there are a million other families you’d be better suited for. What makes {i}us{/i} so special? Why choose {i}this{/i} home to be a part of?"
    ni "I don’t know. Boredom, I guess?"
    a "Boredom?..."

    scene livingintheroom29
    with dissolve

    ni "I’m joking, dummy."
    ni "I don’t {i}have{/i} a good reason. That’s just kind of the way things played out, so maybe I {i}am{/i} an idiot."
    ni "All I know is that I wouldn’t trade either one of you for the world. And that our potential for happiness is way greater if we just merge families."
    ni "Which would mean you’d have to inherit Noriko as well. And if that’s the deal-breaker, I totally get it. But hey, at least I tried."

    scene livingintheroom30
    with dissolve

    a "Niki...can I ask you one more thing?"
    ni "You can ask me anything at any time. That’s the relationship I want to have with you."
    a "Just...this one thing is fine for now."
    ni "Then, sure. Shoot."

    scene livingintheroom31
    with dissolve

    a "I...um..."
    a "You already know, but...I went a little crazy a while ago and...I accidentally hurt Dad..."
    a "And I’ve been...{i}really{/i} hard on myself ever since then because...it never even occurred to me that I could harm the person I love the most..."
    a "Now I’m...constantly afraid that something like that might happen again and...it’s really scary...not being able to trust even myself, so I..."
    a "I wanna know, like..."

    scene livingintheroom32
    with dissolve

    a "Would you still love me if...something like that ever happened to you?"
    ni "I can assure you that a lifetime worth of fawning over your father has inflicted more damage on me than anything {i}you{/i} could possibly do. I’ll be fine."
    s "Okay, sure. But now {i}I’m{/i} having second thoughts about this and-"

    scene livingintheroom33
    with dissolve

    ni "Talk to the hand, Akira. We’re having a moment over here."
    ni "Ami, I am not going to love you any less for having an emotional breakdown. I had plenty of those when I was your age as well."
    ni "And while my circumstances were {i}entirely{/i} different from yours, I’ll still do my best to try and understand. That’s the ultimate goal here."

    scene livingintheroom34
    with dissolve

    ni "So...what do you say, kid? Want to give it a shot?"
    ni "Or am I going to have to return these pajamas?"
    a "..."
    ni "..."
    a "Okay..."

    scene black
    with dissolve2

    a "I’ll try using a spoon from now on."

    "........."
    "......"
    "..."

    scene livingintheroom35
    with dissolve2
    stop music fadeout 15.0

    "Ami heads to her room to have a moment to herself, and Niki wastes no time at all in skipping over to me and aggressively shaking my shoulder in triumphant victory."

    ni "And {i}that{/i} is how it’s done, loser. The beating heart of Kumon-mi strikes again."
    s "I wasn’t really competing with you, you know. I {i}wanted{/i} you to have success there."

    scene livingintheroom36
    with dissolve

    ni "And what a resounding victory it was!"
    ni "Ami gets a mom, {i}I{/i} get a house, and {i}you{/i} get to spend even more time with a girl {i}so{/i} far out of your league that it’s almost criminal."

    stop music
    play sound "static.mp3"
    scene livingintheroom37 with flash
    stop sound

    ni "I guess Noriko gets kind of shafted, though. Just not the good kind of shafted. That’s what you’re going to do to {i}me{/i} later since I did such a good job today."
    s "{i}Quiet, Niki. The walls are thin. Ami might hear you.{/i}"
    ni "{i}Hm? Oh, I’ll call my sound-proofing guy later then. When should I start moving my stuff in? It’s like 90%% clothes. That shouldn’t be a problem since you only have one outfit in your closet, right?{/i}"
    s "{i}We’ll figure that out later. I want coffee.{/i}"
    ni "{i}Ooooh, me too. It’s exhausting having so many feelings so early in the morning. But you probably wouldn’t know that as a robot.{/i}"
    s "{i}This robot is effectively your husband now.{/i}"
    ni "{i}Beep-boop. Initiate hug protocol.{/i}"
    s "{i}I’m going to live in hell from now on, aren’t I?...{/i}"
    a "..."

    scene livingintheroom38
    with dissolve3

    a "Heh."

    scene black

    $ renpy.end_replay()
    $ nikispring3 = True
    $ niki_love += 1

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label nikispring4:
    scene black
    with dissolve2

    "Some nights I dream of things my brother tells me to ignore."
    "But in my sleep I can’t control the grip of her allure."
    "The way she combs my hair; how she moves across the floor."
    "There will always be a limit to how much I can endure."
    "{s}You kissed me after this one.{/s}"

    play sound "static.mp3"
    scene nikipretrip1 with flash
    stop sound
    play music "normalday.mp3"

    n "{i}KYAAAAAAAH! Onii-chan’s sleeping face!{/i} "
    n "Onee-chan...you seriously mean to tell me you get to wake up to this every day of the week?"
    ni "You’re just lucky he’s wearing clothes this time."

    scene nikipretrip2
    with dissolve

    n "Am I {i}really,{/i} though? Like...would it really be {i}so{/i} bad if, as both his sister and sort of his sister {i}in-law,{/i} for me to just...accidentally see his penis in the morning?"
    ni "Yes."
    n "Not even with your permission?"

    scene nikipretrip3
    with dissolve

    ni "Why would I give you my permission, you fucking psychopath?!"
    n "Because you love me!"
    ni "Not {i}that{/i} much! Find your own penis! I mean...boyfriend!"

    scene nikipretrip4
    with dissolve

    n "But sisters are supposed to {i}share.{/i} And you {i}always{/i} give me your hand-me-downs. "
    ni "I {i}wouldn’t{/i} have if Mom didn’t pressure me to."
    n "So you’re telling me if Mom pressures you into letting me have a turn with Onii-chan-"

    scene nikipretrip5
    with dissolve

    ni "It’s not going to happen, Noriko! Now stop wanting to fuck your brother! I deal with incestual tendencies enough on a day-to-day basis! I don’t need you adding to that!"

    play sound "knock.mp3"

    a "{i}Hey, are you guys talking about incest in there?{/i}"
    ni "Great! Now look what you’ve done!"

    scene nikipretrip6
    with dissolve

    n "What if you just cover his eyes for a few minutes and let me...you know...{i}sample{/i} him a little bit? Heheh..."
    ni "Akira! Get out of the fucking bed already! I know you’re awake!"

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "Ugh...how did you know?"
    ni "Because you kept opening your fucking eyes, idiot. Some backup would’ve been nice, you know."

    scene nikipretrip7
    with dissolve2

    s "I’m sorry, Niki. But unlike you, I’m actually {i}kind{/i} to my little sister."
    ni "Perhaps {i}too{/i} kind if you can hear all of that and not tell her to knock it off."
    s "Noriko’s her own girl and I won’t tell her how to live her life. Just one more example of me being a better sibling than you."
    n "I love you, Onii-chan!"
    s "That’s nice, Noriko."

    scene nikipretrip8
    with dissolve

    n "Gah! Being rejected so early in the morning is doing unspeakable things to me! If only someone could teach me what to do with these sudden urges!"
    ni "I hate both of you. But I am pleased to announce that I won’t {i}have{/i} to for much longer as we are leaving."
    s "Oh, really? Did Ami finally convince you to move back out?"

    scene nikipretrip9
    with dissolve

    ni "No, asshole! I meant I’m leaving for the weekend. And I’m taking Noriko and Ami with me. That’s why I’m waking you up so early. To say goodbye."
    s "Ahh. I thought it was kind of weird that you weren’t waking me up in the normal way."

    scene nikipretrip10
    with dissolve

    n "What’s the normal way?"
    ni "Unfortunately, this means you’ll have to wake yourself up until we get back on Monday. And also cook for yourself. Which basically means you’ll wind up ordering. "
    ni "That said, I left all of the menus out on the dining room table so you don’t text me a million times looking for them instead of just using DoorDash like a god damn adult."
    n "Onii-chan, what’s the normal way?"
    s "What’s with the sudden trip? And why am I not invited?"
    ni "It’s not sudden. I’ve told you about it every day this week. You’re just a fucking idiot and only retain information directly relevant to your dick."
    s "Well, that’s clearly not true because your absence is very relative to my dick."

    scene nikipretrip11
    with dissolve

    n "Can somebody tell me what the normal way is?! I have a very understandable and rational interest in what the two of you do together!"
    ni "Act innocent all you like, twerp. We both know you’re mature enough to have figured out what that meant immediately."

    scene nikipretrip12
    with dissolve

    n "If I’m so mature, why won’t you let me sample my brother? Huh, Nee-chan? What’s the reasoning behind that?"
    ni "The same reason I won’t let you wear this sweater. It’s my property and I’m not done with it yet."

    scene nikipretrip13
    with dissolve

    n "Fine! Then I guess I’ll just have to be a good girl and act more like a {i}normal{/i} little sister until you {i}are!{/i}"
    ni "That’s...yeah. That’s exactly what I want, actually. I think I just won."
    n "Of course you won. You’re older. You {i}always{/i} win."

    scene nikipretrip14
    with dissolve

    n "That just means I get to spend more time with Onii-chan, though! And none of it will be suspicious!"
    ni "Oh good. So exactly the way things are supposed to be."
    ni "That said, your special {i}sibling time{/i} won’t begin until after our trip. Now, please excuse me while I go make sure the {i}real{/i} incest demon is packed."

    scene nikipretrip15 with fade
    play sound "dooropen.mp3"

    n "Bye, Nee-chan! This is the part where I’d normally make some kind of joke about locking the door! But I won’t do that now since I’m going full sister-mode from now on!"
    s "And how long will that last, do you think?"
    n "Until you get me really flustered and tell me you want to do me or something. You know. Regular little sister stuff."

    scene nikipretrip16
    with dissolve

    s "Where are you guys even going? And...{i}why{/i} are you going without me? Am I not a part of this family anymore?"

    scene nikipretrip17 with fade

    n "Of course you are, Onii-chan! And perhaps the most important part of all since you’re the only one who possesses the genetic capability to extend and grow our family."
    s "Yeah. That’s not really doable by myself, though. "
    n "Sure. But if you take just one of us girls away, the family can still grow. And between Nee-chan and Ami both claiming you as their property, I guess that piece is going to be me."
    s "Yeah, well I’d prefer you don’t go anywhere either since you’re the only one of them I can confidently call {i}my{/i} property."
    n "The feminist part of me hates that, but the brocon part of me has never been happier to hear anything. I’m so conflicted all of a sudden, Nii-chan."
    s "Noriko. Where are you going and why?"

    scene nikipretrip18
    with dissolve

    n "The beach. Nee-chan has a photo-shoot tomorrow and wants to try and cultivate her new, motherly bond with Ami. The inclusion of me apparently makes that easier."
    s "What are you going to do then?"
    n "Secretly invite you, of course."
    s "Oh. "
    s "Well, that was way easier than I thought it’d be."

    scene nikipretrip19
    with dissolve

    n "You can’t let either of them find out though, okay? It’s apparently harder to connect with Ami while you’re around. So you need to be removed from the picture entirely."
    n "And if Nee-chan finds out I brought you, she’ll invoke Nakayama Sister Law 19A-B-42L. We do {i}not{/i} want that to happen, Onii-chan."
    s "Why? What does that law do?"
    n "If Nakayama Sister Law 19A-B-42L is invoked, Nee-chan has the right to sacrifice me to a demon of her choice. "
    n "And there’s nothing I can do about it either because that’s the law and laws are meant to be followed."
    s "Aren’t you an anarchist?"

    scene nikipretrip20
    with dissolve

    n "For actual laws, yeah. Sister Law, though? That’s way bigger and scarier. You think I want to be sacrificed to a demon, Nii-chan? Because I don’t."
    s "Then why not just invite Kirin instead or something if my inclusion is so dangerous for you?"

    scene nikipretrip21
    with dissolve

    n "Because I like you better than her and want to spend more time with you since I’m pretty sure this is the largest gap in character events any of your love interests have ever had."
    s "What?"
    n "Just a hunch. Molly’s not the only one who thinks of dating in video game terms. "
    n "...Is what I {i}would{/i} say if I hadn’t already pledged to engage sister-mode."
    s "..."
    n "Does Nee-chan really give you a blowjob every single morning?"

    scene black
    with dissolve2

    s "I don’t even want one sometimes. I think she has a problem."
    n "So, hypothetically, if someone were to hide a camera in here, where would you least likely check? "

    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene nikipretrip22
    with fade

    ni "Ami — you almost ready to go? We’re about to- what are you doing?"
    a "Oh. Sorry, Aunt Niki. I just had to do something really quick before we leave."
    ni "Is that “something” increasing the amount of fanservice we have in this game? Because there’s really no other reason for you to be standing like that."

    scene nikipretrip23
    with fade

    a "Fanservice? Whatever do you mean? This is just how I stand when I use my laptop."
    ni "Okay. As long as you’re not only doing it to try and increase the appeal of the game to people who don’t like to read."

    scene nikipretrip24
    with fade

    ni "Because, as far as I’m concerned, fanservice is the worst possible way to do that. And I can tell you now that I won’t take any part in it."
    a "Really? But aren’t we only going to the beach so you can do the photo-shoot for your swimsuit calendar?"
    ni "There’s a big difference between gravure photography and overly-gratuitous, weirdly angled upskirt shots. You’ll know what I mean one day, Ami. I’m sure."

    scene nikipretrip25
    with fade

    a "Maybe. And yeah, I’m all packed. Can we really not bring Sensei, though?"
    ni "You say that like he’s our dog."
    a "..."
    ni "..."

    scene nikipretrip26
    with dissolve

    a "That’d be nice..."
    ni "I can only be disappointed in myself for giving you the opportunity to say that."

    scene nikipretrip27
    with dissolve

    ni "But no — we can not bring your father. If you really want a dog, you have Noriko. That’s close enough."
    a "But I don’t want to sit on Noriko’s face."
    ni "I’m sure Noriko would be very upset to hear you say that. "
    ni "You’ll be fine for two days without Akira, Ami. You’ve done it plenty of times before."

    scene nikipretrip28
    with dissolve

    ni "Plus! This gives you and me more time to do girl stuff! And bond! And this time, we’ll have a {i}third{/i} player for Cards Against Humanity! That’s slightly less depressing!"
    a "Yeah...but every time you try to hang out with me, I always make it weird. And I’m tired of disappointing you..."
    ni "You don’t disappoint me, Ami! You just gross me out. It’s different."

    scene nikipretrip29
    with dissolve

    a "That’s even worse! I’d rather you just be disappointed in me. Or, ideally, just generally open to the idea of a father and daughter who sexually experiment together. Every day."
    ni "You’re doing it again."
    a "But Aunt Niki! What if I never meet or even {i}encounter{/i} another boy?! "
    a "Will you really subject me to a life of forced abstinence when there’s a perfectly good dad right across the hall?"
    ni "Yes."

    scene nikipretrip30
    with dissolve

    a "Now, that’s just mean. I bet you’d have sex with {i}your{/i} dad if he was the only guy around."
    ni "I am going to pretend you didn’t just say that. Now, go put your shit in the limo."
    a "Can I maybe just...you know...{i}sample{/i} him? With your supervision? "

    scene nikipretrip31
    with dissolve

    ni "What is with you creeps and {i}sampling{/i} him all of a sudden? This isn’t fucking Costco. And {i}he’s{/i} not really desirable in any way whatsoever. I don’t get it."
    a "Then why do you wake him up with a blowjob every day?"

    scene nikipretrip32
    with dissolve

    ni "Because I have a problem, Ami! I love dick, okay?! And if that’s a crime, then lock me up! Because I’m not stopping any time soon!"
    ni "I didn’t go over a decade without the touch of a man just for that man’s {i}daughter{/i} or my {i}sister{/i} to ask me to share! Find your own dick! Akira’s is mine! Got it?!"
    a "Wow."

    scene nikipretrip33
    with dissolve

    a "That was actually kind of...cool. I really respect you for that outburst, Aunt Niki."
    a "As a daughter, of course. As a fan, I am heartbroken."
    ni "Grab your shit and get in the car. Now."

    scene black
    with dissolve2

    a "{i}Hah...{/i}yes, ma’am. Let me just close my laptop."
    ni "Fine, but if you need to- wait a minute. What- Ami?! What the fuck were you Googling before I walked in?!"
    a "I think {i}trying{/i} to Google it would be a more accurate description. There are shockingly few dad and daughter sex tips available on the Internet. I just keep getting called weird."
    ni "You probably just got us put on a list, you fucking idiot! How’s your father going to explain this to the Internet company?! "
    a "He won’t need to! Because thanks to Makoto, we now have NordVPN. And with the following discount code, you {i}too{/i} can feel safe and secure online where-"
    ni "Don’t hijack my event with ads! We’ve broken the fourth wall enough already and we haven’t even made it to the beach yet!"

    $ renpy.end_replay()
    $ nikispring4 = True
    $ niki_love += 1
    $ noriko_love += 1
    $ ami_love += 1

    jump amispring2

label nikispring5:
    if _in_replay:
        play music "wewereangels.mp3"

    "{i}A short while later...{/i}"

    scene nikiamibathtime1
    with dissolve2

    ni "{i}Hah...{/i}I’m starting to get the feeling Noriko won’t be joining us after all."
    a "I’m sure she’ll come eventually, Aunt Niki. We probably just need to wait a little while longer."
    ni "I don’t think so, Ami. Haven’t we been in here for, like...an hour?"
    a "Has it really been that long? I feel like we only just stepped in."

    scene nikiamibathtime2
    with dissolve

    ni "You’re sure you’re not overheating? Because we don’t {i}need{/i} to stay in here if you are. Are you thirsty, maybe? Should I call out to Patrice for a bottle of-"
    a "I’m fine, really. But thanks for asking. And sorry I’m not exciting enough to entertain you without Noriko."

    scene nikiamibathtime3
    with dissolve

    ni "What? No. That’s not it at all. I just thought you’d be more comfortable with her around since-"
    a "Since you’ve already made a trillion attempts to get closer to me and I’ve squandered them all by bringing up the amount of sex I want to have with my dad?"

    scene nikiamibathtime4
    with dissolve

    ni "I was going to say since she’s your age and you know her better. But yeah, that too I guess."
    ni "Can we not talk about dad sex anymore, though? I kind of just want this to be normal and relaxing since I’ll be working most of tomorrow."
    a "I can be normal, I think. "
    a "You’re wrong about one thing, though. I don’t know Noriko as well as I know you."

    scene nikiamibathtime5
    with dissolve

    ni "Really? Even though you guys are in the same class? You don’t, like...hang out during lunch or anything? Pass notes during math?"
    a "Nobody “passes notes” anymore, Aunt Niki. We all have cell phones now. You’re dating yourself again."
    ni "So, if I go through your cell phone, I’m not going to see any messages from Noriko sent during school hours?"
    a "Nope. In fact, you probably won’t see many messages at all."

    scene nikiamibathtime6
    with dissolve

    a "Most of my friends stopped going out of their way to contact me after that whole breakdown thing happened. It’s pretty much just Ayane and sometimes Molly in my messages now."
    ni "Not even that Maya girl?"
    a "We don’t really text. Our relationship is a little...different from how I am with my other friends."
    ni "Would...you like {i}me{/i} to text you more?"

    scene nikiamibathtime7
    with dissolve

    a "You don’t have to feel {i}bad{/i} for me, okay? I’m fine with things being this way. It gives me more time to focus on what’s actually important. "
    ni "Don’t bring up dad sex. I told you no dad sex."

    scene nikiamibathtime8
    with dissolve

    a "I won’t. I meant myself. "
    ni "You...did? "
    a "Mhm. I can’t be the {i}perfect{/i} Ami if I’m always distracted by what everyone else is doing. And I {i}have{/i} been. Distracted, I mean. Which is why it’s been a while since I’ve felt 100%%."
    ni "What do you mean by “perfect Ami?” People can’t be {i}perfect.{/i} And I don’t want you trying to live up to unrealistic standards like that. It’s not healthy."

    scene nikiamibathtime9
    with dissolve

    a "Do you really believe people can’t be perfect? You mean you’re not trying to do that too?"
    ni "What, be perfect? Absolutely not. "
    a "But you’re an idol. Isn’t that your job?"

    scene nikiamibathtime10
    with dissolve

    ni "I’m a {i}Japanese{/i} idol, Ami. It’s those fucking K-Pop girls who turn themselves into statues for the sake of their work. {i}We{/i} actually put emphasis on flaws over here.  "
    a "Do you...have a vendetta against K-Pop, Aunt Niki?"
    ni "Mmm...it’s less of a {i}vendetta{/i} and more just feeling bad for them. All those plastic surgeries...veneers...ridiculous diets. It’s like they can’t even live or be themselves."
    a "If that’s the case, what {i}are{/i} your flaws then? Because I can’t find any at all."

    scene nikiamibathtime11
    with dissolve

    ni "Then you’re either lying to me or not looking hard enough, because I have tons. Just most of them don’t really affect my public persona, thankfully. "
    a "It’s probably hard to emphasize any of that to the public then, right? "
    a "Cause like, if Japanese idols are {i}supposed{/i} to be imperfect, and all of your flaws occur behind the scenes, what exactly are you trying to portray when you’re on stage?"
    ni "See, that’s the interesting part. Because while my physical {i}image{/i} might be perfect, the flaws come out in droves when you actually listen to what I’m singing about. "

    scene nikiamibathtime12
    with dissolve

    ni "At least in all of the songs that don’t get really popular. But those songs are how I connect with my audience on a {i}real{/i} level. That’s where {i}Niki{/i} is."
    a "I’m still not really sure I get it, but I don’t really pay much attention to lyrics so..."

    scene nikiamibathtime13
    with dissolve

    ni "Aren’t you a poet now? You mean to tell me you can write stuff like that and {i}not{/i} listen to the words of a song? "
    a "I’m not a very {i}good{/i} one. I sort of just...write how I feel and...rhyme stuff. "
    ni "I’m sure you’re great. You just come from a family of poets, so it’s probably hard to compare yourself to them and {i}not{/i} feel a little disadvantaged."
    ni "My music’s just like that too, though. I write how I feel and try to rhyme stuff. "
    ni "My producers hate me for it, of course. And yes, they do help with the production, but writing my own lyrics is something I refuse to budge on because I kind of...{i}want{/i} to emphasize my flaws."
    ni "It makes me feel better about myself. It’s how I kept going when your father left me behind. "

    scene nikiamibathtime14
    with dissolve

    ni "I just have to be creative when I do it. Generic-ish, I guess. Use symbolism instead of things that {i}actually{/i} happened because the hard truth would just turn people off."
    a "“Hard truth” as in the fact that you’ve been obsessed with my dad for over a decade now and can’t leave him alone despite how much you know you should?"

    scene nikiamibathtime15
    with dissolve

    ni "Bingo. Anyone who pays {i}any{/i} amount of attention to my lyrics understands that there’s something I can’t let go of. "
    ni "They get that I’m clingy and obsessive and desperate and scared. And they {i}get{/i} it because I share it with them. {i}Those{/i} are the flaws I emphasize. Internal ones."
    ni "Which creates this sweet duality because you’ve got this picture-perfect babe who everyone’s pining over that is actually just permanently dying on the inside due to the way she naturally is!"
    a "Okay, yeah. I get it now. I {i}can{/i} see the flaws when you put it that way. I just try not to think of stuff like that as a {i}flaw{/i} to begin with. "

    scene nikiamibathtime16
    with dissolve

    ni "Because {i}you’re{/i} crazy too. And you do the same thing as me. Just {i}you{/i} happen to be related to the thing you’re obsessed with."

    scene nikiamibathtime17
    with dissolve

    a "Well, {i}I{/i} like to consider that a strength. It just means that {i}my{/i} love transcends societal norms while everyone else’s is weak and breakable."
    ni "Heh. I kind of {i}wish{/i} my love was breakable. It would definitely make my life easier. "

    scene nikiamibathtime18
    with dissolve

    ni "But also — I wouldn’t be able to do things like {i}this{/i} if it was. And you’d probably be in this bath with that {i}Sara{/i} lady right now if that were the case."
    a "Wow. You’re really jealous of her, aren’t you?"

    scene nikiamibathtime19
    with dissolve

    ni "You could have so easily kept me oblivious to her existence and you decided not to. This is {i}your{/i} fault, twerp."
    a "It’s just a little funny. Cute, even. Because you never seem to get jealous when me or my friends spend time with my dad."

    scene nikiamibathtime20
    with dissolve

    ni "Well, yeah. This is a grown woman we’re talking about this time. And {i}you{/i} like her too. So it’s like a double whammy of jealousness."
    a "So her age is the main factor? You don’t think my dad could possibly fall for anyone younger?"
    ni "I...try not to think about that, to be honest."
    a "Is that because you have faith that he wouldn’t actually do anything like that? Or because you’d have no choice but to live in a constant state of worry if you {i}did?{/i}"
    ni "I..."
    a "?..."

    scene nikiamibathtime21
    with dissolve

    ni "You know what? Why don’t we change topics? Tomorrow will be your first time coming to a photo-shoot, right? What if afterwards, we-"
    a "No, no! Don’t change the topic. As a high-schooler myself, your thoughts on this are directly relevant to us getting closer."
    a "Plus, if you have any tips on how to {i}not{/i} be jealous of other girls my age, I’d love to hear them. Because I know {i}I{/i} struggle having faith in my dad sometimes. Do you, Aunt Niki?"

    scene nikiamibathtime22
    with dissolve

    ni "...Of course I have faith in him. He’s...the single most important person in my life."
    a "Noriko’s up there too though, isn’t she? And {i}she{/i} spends a ton of time with him. Are you not worried about {i}her?{/i} Why is it just Sara?"
    ni "Noriko’s more like a little sister to Akira than anything else. I’m not...jealous of that."
    a "But you know she’s in love with him, right?"
    ni "I know...she {i}thinks{/i} she’s in love with him. The same way {i}you{/i} do. But you two are still teenagers and...you’ll grow out of that. "
    ni "You’ll realize in time it was more...hormones or...admiration than actual romantic feelings. And you’ll get older and...fall for somebody else. "
    a "But if my dad were to {i}return{/i} any of those blossoming feelings-"
    ni "He wouldn’t..."
    ni "He knows better than that."

    scene nikiamibathtime23
    with dissolve

    a "Hm..."
    ni "..."
    a "{i}Does{/i} he, though?"
    a "Are you sure this isn’t just another one of your “flaws?” Having too much faith in someone and just tricking yourself into thinking they’re governed by the same principles as you?"
    ni "..."
    a "How do you think that happens to someone, Aunt Niki?"
    a "If it’s true that he’s worse than you imagine...do you think he’s {i}always{/i} been that way? "

    play sound "static.mp3"
    scene nikiamibathtime24 with flash
    stop sound

    a "{i}Or do you think someone made him into that?{/i}"
    s "Okay — I just finished chapter 215. What one are you on? "
    ni "The middle of...210."

    scene nikiamibathtime25
    with dissolve

    s "Wait, really? But you always read faster than me. I figured you’d be at the end of the latest volume by now."
    ni "I guess I’m just reading slower than normal today."

    scene nikiamibathtime26
    with dissolve

    s "Oh no. I know that tone. "
    ni "What tone? I don’t know what you mean."
    s "{i}That{/i} tone. The one you only use when you’re mad at me and want me to ask what’s wrong so you can scold me about something."

    scene nikiamibathtime27
    with dissolve

    ni "Oh, great. Well, since you’ve asked, I think you’ve been spending a suspicious amount of time with your teacher lately. "
    ni "And I do not approve of this since I am tired of waiting for you to be here to continue reading manga we’re supposed to read {i}together.{/i}"
    s "Then just...read it without me and I’ll catch up when I can."
    ni "I’m sorry, Akira — do you not understand what “together” means? Has your teacher not gotten to that word yet?"

    scene nikiamibathtime28
    with dissolve

    s "I just...have a lot to catch up on. And the only hours she’s available just...happen to be the hours I also spend here."
    ni "Akira, you’re the smartest boy I know. What do you possibly have to “catch up” on? "

    scene nikiamibathtime29
    with dissolve

    s "W...Why do you care anyway? I’m still here every day. It’s not like I’ve just...left you behind or something."
    ni "Because it’s {i}weird!{/i} My parents think so too. "
    ni "She picks you up like every single day, they’ve never met her, and you’re always dismissive when they tell you to invite her over for dinner. {i}Why?{/i}"
    s "Why do they want to invite her over for dinner in the first place? {i}That’s{/i} weird!"
    ni "Oh, I don’t know. Maybe because she’s in our driveway every single day and just happens to spend more time with you than your {i}actual{/i} mom. Is that not reasonable?"
    s "Not really, no! She’s just my teacher. There’s no reason for you or your parents to get involved."

    scene nikiamibathtime30
    with dissolve

    ni "Are we {i}not{/i} allowed to worry about you or something? Because you’re basically family, Akira. And if {i}I{/i} started spending every waking hour with some weird adult-"
    s "She’s not weird. She’s just...eccentric. And she’s engaged to my brother, so {i}she’s{/i} family too. "
    s "I have a life outside of this house, Niki. And...I’d like to {i}keep{/i} having that life without having to worry about {i}you{/i} being there too."
    ni "Can you at least promise me you’re not in danger then?"

    scene nikiamibathtime31
    with dissolve

    s "Danger? What? Do you think she’s going to kill me? "
    ni "There are ways to hurt someone without killing them, Akira. I just want to know you’re okay. That’s all. "
    s "I’m fine, Niki. I just need extra tutoring. {i}That’s{/i} all."
    ni "You promise?"
    s "Yes. {i}I promise.{/i}"

    play sound "static.mp3"
    scene nikiamibathtime32 with flash
    stop sound

    ni "..."
    a "Aunt Niki? Are you overheating? Do we need to get out of the bath?"
    ni "What do {i}you{/i} think about Akira, Ami?"
    a "Hm?"
    ni "Do {i}you{/i} think he’d ever cross the line with a girl your age? Or even...{i}want{/i} to?"
    ni "If Noriko was {i}your{/i} little sister, how would {i}you{/i} feel about having her spend so much time alone with him?"
    a "Hm..."

    scene nikiamibathtime33
    with fade

    a "If I was in your shoes, I think I’d definitely be worried."
    a "Not because my dad is evil, though. Because he’s sad. "
    a "And he’ll take love in any form that he can get because it’s the only way he can distract himself from the pain of losing his {i}first{/i} true love."
    ni "..."

    scene nikiamibathtime34
    with dissolve2

    a "..."
    ni "You’re talking about your mom, aren’t you?"
    a "..."
    ni "Were they..."
    ni "Did she..."
    a "..."
    ni "..."
    a "If she did, would you think {i}she{/i} was evil?"

    scene nikiamibathtime32
    with fade
    stop music fadeout 15.0

    ni "Yes..."
    ni "I would."
    a "Then would my dad be evil too if he did the same?"
    ni "I..."
    ni "I just..."
    ni "I can’t forgive anyone who would hurt Akira that way."
    a "Could you forgive someone who’d hurt your sister that way?"
    ni "No...I don’t think I’d be able to forgive someone like that either..."
    a "Hm..."

    scene black
    with dissolve2

    a "Then maybe you {i}should{/i} worry, Aunt Niki. "
    a "And maybe there are people out there who lean further into their flaws than just throwing sad words into happy-sounding songs."
    a "I don’t think that makes them unforgivable, though."
    a "If anything, I think it might even make them beautiful."
    a "I’m sure you understand that as someone who’s learned to appreciate imperfections. "
    a "And even if you don’t...even if you {i}can’t,{/i} you made a promise...didn’t you? "
    a "To stay by his side forever?"
    ni "I did...yeah..."
    ni "But he made a promise to me too. And if he lied-"
    a "If he lied, it was only to protect you."
    ni "..."
    a "Ahh..."
    a "I wish I could be as kind as him."

    $ renpy.end_replay()
    $ nikispring5 = True

    "........."
    "......"
    "..."

    jump norikospring4

label nikispring6:
    play sound "slidedoor.mp3"
    "{i}Three hours later...{/i}"

    scene nikiverysad1
    with dissolve2

    n "I entered as a girl...but I emerge as a woman."
    s "I formally apologize for all of the things I did to you in that room. As your brother, I should know better."
    n "{i}Apologize?{/i} Are you kidding? That was the best night of my life. "
    n "Will I be paying for it in the morning? Probably. But that is a problem for tomorrow’s Noriko, when tonight’s Noriko is no longer dealing with the aftershock of over a hundred orgasms."
    s "Do you know what time it is by any chance?"

    scene nikiverysad2
    with dissolve2

    n "Like 3:30 last I checked? "

    scene nikiverysad3
    with dissolve

    n "Want to go take a shower together? Because my body says “sleep,” but neither my mind nor the hotel staff will ever forgive me if I crawl into my futon drenched in sweat and brother juice."
    s "..."
    n "Onii-chan? Shower? We can go separately if you are sufficiently grossed out by me right now. Which you may be and I would not blame you for."
    s "Not that."
    s "Look down."

    scene black
    with dissolve2
    $ renpy.pause(1, hard=True)
    scene nikiverysad4
    with dissolve2

    ni "....................."
    n "Nee-chan?..."
    n "Have you...been outside the door the whole time?"
    s "........."
    ni "......."
    n "Uhh..."
    n "I’m...gonna let {i}you{/i} handle this one. "
    s "Yeah..."
    s "Goodnight, Noriko. I’ll see you in the morning."

    scene black
    with dissolve2

    n "Goodnight...Onii-chan. Onee-chan."

    "........."
    "......"
    "..."

    scene nikiverysad5
    with dissolve2
    play music "lastdailysong.mp3"

    s "{i}Hah...{/i}"
    ni "..............."
    s "............."

    "Where do I even begin?"
    "At what point could I even {i}start{/i} my explanation that wouldn’t cause her head to sink even further into her knees?"

    ni "................"

    "There isn’t one, is there?"
    "I’ve really fucked up this time."
    "So much so that I don’t even know if I should be pivoting to damage control or just piling more pain onto her in an effort to tear her away from other doors in the future."
    "Because there will be more. And she was always going to find out one way or another. "
    "I just didn’t expect her to subject {i}herself{/i} to the same hurt I thrust upon her when it would have been infinitely easier to just...walk away and face me later."
    "She’s not like me, though."
    "She’s never been like me."
    "She doesn’t run. She doesn’t hide. And when something hurts or scares her, she does what {i}any{/i} adult should do and just...confronts it."
    "I envy that. I envy her. I always will and I always have. But there’s a brief respite during times like this. For despite how much {i}I{/i} am hurting, I can’t imagine it even compares to what she feels."
    "That’s always been her greatest weakness. That unwavering faith in me. The belief that I can be better if she just {i}presses on{/i} and {i}breaks through.{/i}"
    "But everyone feels that way. And when everyone feels that way, what am I supposed to do?"
    "It could have just as easily been Noriko in her sister’s place tonight. The same way it is with Ami {i}every{/i} night now. And I can’t please {i}everyone.{/i} "
    "But that doesn’t stop me from trying. And failing. And winding up next to girls that I really {i}do{/i} wish would just...go away."
    "Because for all she’s done for me...{i}with{/i} me..."
    "{i}She’s{/i} the one I want to hurt the least."
    "But that just means I’m forced to hurt her the most. "
    "And it might not make sense to you, but it’s what I’ve always done when it comes to her."
    "It’s all to protect her. From whatever I may do. From whatever fears may come."
    "She just...{i}keeps{/i} coming back. "
    "How much can this girl take?"

    s "..............."
    ni "................"
    s "................."
    ni "Five hours..."
    s ".........."
    ni "You had sex with her for {i}five hours.{/i}"
    s ".........."
    ni "My sister..."
    ni "My little {i}fucking{/i} sister who loves you with all her heart and has done nothing but look up to you her {i}entire{/i} life..."
    ni "And you do {i}that?{/i}"
    ni "The same things that were done to {i}you?...{/i}That turned {i}your{/i} life into a living hell?!"
    s "............"
    ni "Where did I go wrong?..."
    s "........"
    ni "What else could I have done?..."
    s "There is nothing, Niki."
    s "There is nothing you could have done that would have changed this outcome."
    ni "Then why did you let me {i}try?!{/i}"
    s "Because trying to stop you would just make you try even harder. That’s what you do. "
    s "You’ve always wanted to fix me. But it’s wanting that that’s going to destroy you in the end. "
    s "If this...isn’t the end right now."
    ni "Are you breaking up with me then?..."
    s "Shouldn’t I be the one asking you that question? Because it’d be hard to see you as anything but an idiot if you’re not. And I don’t want you to ruin my image of you."
    ni ".............."
    s "Guess you finally know about what was going on with Sekai then. Took you long enough."
    ni "I’ve always {i}known...{/i}"
    ni "I just didn’t want it to be real."
    s "..............."
    ni "And I don’t want {i}this{/i} to be real either."
    ni "I keep sitting here...with my eyes closed...hoping I’ll just...{i}wake up{/i} and this will all be a part of some nightmare."
    ni "But now my...knees are soaked from crying into them...my {i}eyes{/i} hurt. And I’m {i}hungry.{/i} And I just want this to be over."
    s "............"
    ni "Why are you like this, Akira?..."
    ni "Why do you go out of your way to make things even {i}worse{/i} for yourself?..."
    ni "I don’t understand..."

    scene nikiverysad6
    with fade

    s "..."
    ni "You’re not even supposed to {i}be{/i} here...This weekend was for {i}me!{/i} So {i}I{/i} could do something to make {i}my{/i} life better without you getting in the way again!"
    ni "And you fucking {i}ruined{/i} it! Why didn’t you just stay at home?! That’s all you had to do!"
    s "So you’d be happier just continuing to lead a life of delusion? Where you willfully ignore the things I’m doing behind the scenes?"
    ni "No, you fucking idiot! You’re over-complicating things {i}again!{/i} I just wanted to bond with Ami and my sister! "
    ni "Not everything has to be some super deep and complex mental puzzle about you getting molested as a child! And yeah, that was horrible! But this world doesn’t revolve around you!"
    ni "Just let me {i}have{/i} something! Anything! To distract me from the fact that I’ve wasted two thirds of my life on someone who will never love me as much as {i}I{/i} love him!"
    s "I’m sorry..."
    ni "No, you’re not! You’re just {i}saying{/i} you are because it’s the easiest fucking way to roll over and submit to how fucking weak and stupid you are! Why won’t you just fight?!"
    ni "Do you have any idea how fucking annoying this is?! Being a fountain of fucking moral and mental support for you every day, just to watch you set yourself on fire?! Just to be ignored?!"

    play sound "static.mp3"
    scene nikiverysad7 with flash
    stop sound

    ni "That’s why I ask if there’s something else I could have done..."
    ni "Something I could have changed that would have stopped you from perpetuating this fucking death spiral where you destroy the only meaningful connections you’ve ever had with anyone."
    s "Honestly, I think some people are just...destined to live terrible, hurtful lives. "
    ni "Honestly, I think you’re a fucking moron. That’s the dumbest thing I’ve ever heard."
    s "If it’s so dumb, then why has my life been nothing but endless torment from the moment I was born? "
    ni "Why has {i}my{/i} life been nothing but endless torment from the moment I met you? "
    s "Because you met me, obviously."
    ni "Oh, good. At least you’re not a {i}complete{/i} moron if you can acknowledge {i}that{/i} then."
    s "You get what I’m saying though, right? "
    ni "What, that all of these years have been fucking wasted trying to convince someone who’s never known happiness that the concept itself isn’t a fucking myth?"
    ni "And here I thought that being a father would get you to wake the fuck up. {i}Here{/i} I thought trying to show you what a {i}real{/i} family felt like might finally {i}change{/i} you."
    ni "But Ami’s just as deranged as you are and {i}now{/i} you’re fucking my sister too. So silly me, right? Silly fucking Niki for trying {i}again!{/i} When all she wants to do is help!"
    s "You and Noriko have that in common...that whole “wanting to help people” thing."
    ni "Mhm! Want to know what else we have in common now too?"

    scene nikiverysad8 with fade

    s "..........."
    ni "You’re so fucking weak, Akira...{i}so{/i} fucking weak."
    ni "It’d be one thing if I just found weird shit on your computer...but {i}actually{/i} sleeping with a girl her age?..."
    ni "I can’t watch what happened to you {i}again...{/i}you were so fucking smart and precious. And {i}Noriko’s{/i} so fucking smart too, but now she has to deal with this!"
    ni "And sure, she’s giddy and all like, “look at me, I’m a woman” now, but what if she looks back on this in five years and realizes how fucked up it was?"
    ni "You want to trash your connection to {i}her{/i} too?! Someone who has rooted for you harder than {i}anyone{/i} ever?! "
    ni "You were her fucking role model! You still are! So what if {i}she{/i} turns around and does this same shit to someone else’s kid in the future?! What if you just created {i}another{/i} monster?!"
    s "Asking me the same questions I ask myself every day isn’t going to just magically help me come up with an answer."
    ni "So she’s {i}not{/i} the first then. And you’ve done this before."
    s "That’s right..."
    ni "How many times? With who? Because I assume now that’s what had that Maya girl storming out of the house when she found out I was living there. You fuck her too, Akira? "
    s "Yes...I have."

    scene nikiverysad9 with fade

    ni "Pfft. Un-fucking-believable. Only you could have someone like me {i}begging{/i} to be your one-and-only just to turn around and fuck some random high schooler. "
    ni "My parents should’ve called the cops on that fucking tutor of yours {i}long{/i} before she died. But {i}I{/i} told them everything was fine. Because I believed you."
    ni "I have always believed you. Always just let you {i}do your thing{/i} because I had enough faith in you to think you’d be able to fix things on your own. How fucking dumb I was."
    s "You weren’t dumb, Niki...You were a kid. "
    ni "Yeah, and so were you. But while {i}I{/i} was in bed watching Pokemon and painting my nails, you were in bed with a grown woman, learning everything about life except what’s important."
    s "It wasn’t like that, Niki. She loved me. She {i}really{/i} loved me. "
    ni "Yeah, and I’m sure you think you {i}really{/i} love Noriko too, don’t you?"
    s "Because I do."
    ni "So what then? It’s okay to fuck whoever you want {i}regardless{/i} of their age so long as you convince yourself you love them? Is that the message you’re trying to send me here?"
    s "Niki, there’s only one message I’m trying to send you right now and it’s the same one you’re trying to send me. That I’m irredeemable and you’re an idiot for still caring this much."
    ni "But {i}why{/i} are you irredeemable?...And how can you not blame that woman for what you’ve turned into? Without her, it would’ve just been you and me. Forever."
    s "I don’t...know what I’d be without her, though. Because I barely existed {i}before{/i} her."
    ni "You existed. You had interests and hobbies and foods that you liked. But her being nicer to you than your mom or your brother doesn’t mean she gave you {i}life.{/i} "
    ni "{i}I{/i} was nice to you too, Akira. I opened myself up to you in a way I’ve never done with anyone else. "
    ni "And {i}now{/i} I finally have to face the fact that the entire time we were together, you were with someone else. Someone who probably made {i}me{/i} look like a worthless amateur by comparison."
    ni "Is that why you left when she died? Started {i}hunting?{/i} Because I wasn’t good enough? Couldn’t give you what you really wanted? {i}Artificial{/i} love instead of the real kind?"

    scene nikiverysad6
    with fade

    s "I don’t know what I was doing back then...I was just..."
    s "I acted on instinct after she died. And my instinct was to leave you behind."
    ni "But {i}why?!{/i} Why am {i}I{/i} your punching bag?! That can’t be why I was put here, Akira! I’m more than that! {i}Better{/i} than that!"
    s "I imagine I thought the same thing back then that I do now...that if I hurt you badly enough, you’ll stop subjecting yourself to this. "
    s "You and Noriko weren’t supposed to find me again. You guys were supposed to move on..."
    s "But here you are, years later, still wrapped up in the same shit that kept me up at night back then. Just now, I’m on the opposite end of things."
    s "But the two of you are exactly where you’ve always been — caught in the middle of my bullshit and trying to jump in front of the gun I aim at myself in exchange for...{i}nothing.{/i}"
    s "You two love me so much...but I have never given you {i}anything.{/i} I don’t get it."
    ni "You don’t get it because love is more than just an exchange, idiot!"

    play sound "static.mp3"
    scene nikiverysad10 with flash
    stop sound

    ni "I don’t {i}want{/i} to love you! I don’t {i}want{/i} to try and be a mom to a creepy red-head in my twenties! I want to focus on myself and my career!"
    ni "I want to help other girls learn how to sing! I want to start a fashion line and do makeup ads and be on billboards and go to fancy beach inns and get paid lots of money! "
    ni "I want people to pamper me and tell me I’m great! That I’m pretty! That all those years of hard work were {i}not{/i} wasted! But every second I’m with you, I feel like they {i}were!{/i}"

    scene nikiverysad11
    with dissolve2

    ni "I could conquer the world before making you happy...and I just don’t understand that. Because the logic would dictate here that if I hadn’t gotten through yet, that you just...don’t like me."
    ni "But you {i}do.{/i} And I wish that you didn’t because it would make all of this {i}so{/i} much easier."
    s ".........."
    ni "That was my {i}sister,{/i} Akira..."
    ni "You didn’t cheat on me with just {i}anybody.{/i} It wasn’t just {i}any{/i} teenager. It was my {i}sister.{/i}"
    ni "Can there {i}be{/i} a greater betrayal than this?...What am I supposed to do {i}now?{/i} Just...get over it?! Accept that you’re a fucking pig and just...move on?!"
    s "Just...{i}leave...{/i}"

    scene nikiverysad12
    with dissolve2

    ni "You think I don’t {i}want{/i} to?! You think I can walk into a room, see {i}that{/i} and think, “Haha! Typical Akira! Hey, everyone! Look at how sad he is! Feel bad for him!” No, moron! "
    ni "I want to fucking {i}kill{/i} you right now! I’m so mad that it is taking every ounce of self-restraint in my body to not just strangle you to death! "
    s "But you’re not doing that...because you made a promise to me."

    scene nikiverysad13
    with dissolve2

    ni "Because you {i}asked{/i} me to make a promise to you..."
    ni "You looked at me, more terrified and helpless than I have ever seen you, and you {i}asked{/i} me if I’d really never leave you."
    ni "It’s the only time you have ever asked me for help...and it proved to me that you {i}want{/i} me by your side. "
    ni "That’s why I took you home that night. And do you remember what happened next?"
    s "Of course I remember what happened next..."
    ni "I waited over a decade for that moment. And I thought to myself once we were done that things were going to start getting better. "
    ni "That you’d open up to me more. That you knew you didn’t need to keep secrets from me...and that I wouldn’t {i}judge{/i} you for telling me them."
    s "We both know that’s a lie, though. You were always going to judge me when you found out about {i}this.{/i}"
    ni "Maybe. {i}Probably!{/i} Because it’s fucking horrible! But that doesn’t mean you should just do it {i}in front of me!{/i}"
    s "Yeah, that..."
    ni "?..."
    s "I probably...should have stopped when you walked in."
    ni "{i}You think?{/i}"
    s "I’m sorry, Niki...that I’ve done nothing but hurt you. I can promise you that’s the exact opposite of what I-"
    ni "Your {i}promises{/i} mean literally nothing to me, Akira. They’re worthless. {i}So{/i} worthless that you can’t even look me in the eye when you make them."
    s "I’m ashamed..."
    ni "Good. You {i}should{/i} be ashamed. But what does that mean for {i}me?{/i} What do {i}I{/i} do now? "
    ni "Because being there for you doesn’t work. {i}Not{/i} being there for you doesn’t work. "
    ni "Do you want me to castrate you? Because I will. And I am {i}very{/i} tempted to do that right now."
    s "I’m often tempted to do that myself...Figure it would shave at least 50%% of my problems off. "
    s "I’m a coward as always, though. I can’t follow through with it. Imagine it would probably be easier to just kill myself if anything."

    scene nikiverysad14
    with dissolve2

    ni "..........."
    s ".............."
    ni "You’re an asshole, but..."
    ni "I don’t...think you need to go {i}that{/i} far."
    s "......."
    ni "........"
    s "Can you just..."
    s "Chain me up or something, please?"
    ni "Is the...{i}temptation{/i} really that bad? I don’t get it..."
    s "I don’t either...but I want it to stop just as badly as {i}you{/i} want to stop having feelings for me."
    s "I just...keep going, though. I keep doing it. Even when I know it isn’t good for anyone. "
    s "I just can’t stop myself, Niki...I cave every single time."
    ni "............"
    s "............"
    ni "Akira..."
    ni "I can’t help you this time."
    ni "Or even...{i}try{/i} to since you never accept my help in the first place."
    ni "It’s just..."
    ni "This has gone way too far. "
    ni "And I think that..."

    scene nikiverysad15
    with dissolve2

    ni "Well..."
    ni "Maybe some...time apart will..."
    ni "Help me figure out what I...want to do about...all of this."
    s ".........."
    ni "Because I love you, but..."
    ni "You make it...very hard for me to just...exist sometimes."
    ni "And not having to worry about me...waking up beside you...how you’ll hurt me next..."
    ni "Maybe that’ll be good for you too..."
    s "........"
    ni "......."
    s "I take it you’re moving out then?..."

    scene nikiverysad16
    with dissolve2

    ni "............."
    s "............."
    ni "I have a...lot of work coming up soon."
    ni "And I didn’t want to say anything about it until I was 100%% sure, but..."
    ni "This next album...is going to be my last."

    scene nikiverysad17
    with dissolve2

    ni "So there’s a lot of {i}recording{/i} and {i}practice{/i} and {i}promo{/i} stuff that needs to be done, and I-"
    s "You’re quitting?..."

    scene nikiverysad18
    with dissolve

    ni "....."
    s "Niki-"
    ni "Akira, I’m almost 30. It’s a miracle people still {i}want{/i} to see me in a swimsuit at this point."
    s "That’s nothing, though. That’s-"
    ni "It is in the idol world. And besides, with how...drastically my life has changed since you came back into it, I don’t...really think I’m in the right head-space to keep going."

    scene nikiverysad19
    with dissolve
    stop music fadeout 15.0

    ni "I started doing this to get back at {i}you,{/i} remember? And yeah...I love my job. I love sharing my songs with everyone. But nothing..."
    ni "Nothing comes out...{i}right{/i} now that we’ve been reunited. And, no offense, but most of the stuff that’s happened since we {i}have{/i} has...{i}kinda{/i} sucked."
    ni "And I don’t want that to negatively impact an otherwise...nearly flawless career, so...I figure if I go out with a bang...I can sort of just...well..."
    ni "My mark’s been made already..."
    ni "And there’s not much more I can do here, I don’t think..."
    s "..."
    ni "That’s...another reason I wanted to move in with you."

    scene nikiverysad20
    with dissolve

    ni "I figured that...once my career was over...I’d have a lot more time for you and Ami and..."
    s "..."
    ni "And we could figure out a way to make this work..."
    s "But now you don’t know...and I’ll have destroyed your career for nothing."
    ni "I just need time, okay?..."
    ni "So I’m {i}not{/i} moving out. I’ll just...be in hotels a little more than normal and...sleep on the couch whenever I’m {i}not.{/i}"
    ni "And if you...{i}do{/i} need help with anything, I {i}will{/i} still be there. I just..."
    s ".........."
    ni "Maybe we should...just be friends again..."
    ni "For a little while..."
    s ".........."
    ni "Akira?..."
    ni "That’s okay...right?"

    scene black
    with dissolve3

    s "Mm..."
    s "You do...whatever it is you {i}need{/i} to do. For yourself."
    s "For your art."

    $ renpy.end_replay()
    $ nikispring6 = True
    $ nikiblock = True
    $ niki_love -= 50

    "{i}Niki’s affection has decreased by 50!{/i}"
    "........."
    "......"
    "..."

    jump amispring3
