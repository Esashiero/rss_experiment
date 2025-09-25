label dojo:
    if ayane_love >= 0 and firsttimedojo == False:
        jump firsttimedojo
    if ayane_love >= 5 and dojo5 == False:
        jump dojo5
    if ayane_love >= 10 and dojo10 == False:
        jump dojo10
    if ayane_love >= 10 and ayanenew1 == True and ayanenew2 == False:
        jump ayanenew2
    if ayane_love >= 20 and ayanedorm15 == True and dojo20 == False:
        jump dojo20
    if ayane_love >= 25 and halloween14 == True and ayanedorm20 == True and dojo25 == False:
        jump dojo25
    if ayane_love >= 30 and ayanedorm25 == True and dojo30 == False:
        jump dojo30
    if ayane_love >= 35 and day333part2 == True and amiinvite3 == True and dojo35 == False:
        jump dojo35
    if chapthreeactive == True:
        jump ayanesummer2dojogen
    if christmas7 == True:
        jump dojogen2
    else:
        jump dojo3to4

label ayanepool:
    if chap4active == True:
        jump ayanespringpoolgen
    else:
        "ERROR"
        jump noonch4

label ayaneinvite:
    if ayaneinvite1 == False:
        jump ayaneinvite1
    if ayaneinvite1 == True and ayaneinvite2 == False:
        jump ayaneinvite2
    else:
        jump ayaneinvitegen

label ayaneinvitegen:
    play sound "phonebeep.wav"

    "I tap on Ayane's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    ay "I love you!"
    s "Please at least greet me first, Ayane."
    ay "Hi, Sensei! I love you!"
    s "That's better."
    s "What are you up to right now?"
    ay "Sana and I are watching a movie. Do you want to come over and watch it with us?"
    s "I was actually wondering if you'd want to come over to {i}my{/i} place instead."
    ay "Oh, of course! {i}I will come over and help fix your oven right away, Sensei!{/i}"

    "Is that really the best cover story she could come up with?"

    s "See you soon, Ayane."
    ay "Byeeee! I love you!"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene ayaneinvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    ay "So, now that your oven is fixed, what do you wanna do?"

    "How should I spend my time with Ayane?"
    menu ayaneinvmenu:
        "Hang Out (Raise Affection)":
            jump ayaneinviteaff
        "Laying Doggy Style (Raise Lust)" if ayanenosex == False:
            jump ayanedoggylay
        "Grinding (Raise Lust)":
            jump ayanegrindanim
        "Headpat":
            jump ayaneheadpat

label ayaneinviteaff:
    scene ayaneinvitegen
    with fade

    "Ayane and I spend the next few hours sitting beside the bed and watching TV."
    "Ami isn't around tonight, nor would I expect her to help in this regard even if she were, so the two of us order takeout food and wind up sharing our respective orders with one another."
    "I get talked into eating several vegetables and expectedly hate every single one of them."
    "I'm not sure how Ayane is able to stand things like that, but I guess there are a lot of things I'm not sure of when it comes to her."
    "The show we wind up watching features several girls in a strange looking house."
    "Each one of them eats garlic bread off of a paper plate in a very cramped kitchen."
    "It actually seems like more of a live-feed of someone's house rather than a standard program."
    "What channel are we even watching right now?"
    "Ayane slides closer to me and wraps her arm around mine, pressing her head against my shoulder and offering up some of her body heat to counteract the cold temperature of the room."
    "Well, I say that it's to counteract the temperature, but it's obviously a lot more than that."

    scene black
    with dissolve

    if bonus == True:
        "I never would have thought that things would get to the point with Ayane where the two of us could just sit here, watching TV and eating food without fucking each other's brains out."
    else:
        "I never would have thought that things would get to the point with Ayane where bone necklaces don't come up."

    "But, as time goes by, she's starting to feel more and more like another Ami."
    "Like a member of the family."
    "I don't say this out loud because I hate expressing myself."
    "But I also know that I don't {i}need{/i} to say it because she's felt that way for years."
    "For her, this is just another wonderful day with someone she would die for."

    $ ayane_love += 3
    stop music fadeout 5.0

    "{i}Ayane's affection has increased to [ayane_love]!{/i}"

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

label ayanedoggylay:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump ayanedoggylayx
    else:
        $ ayane_lust += 3
        stop music fadeout 5.0

        "{i}Ayane's lust has increased to [ayane_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label ayanegrindanim:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump ayanegrindanimx
    else:
        $ ayane_lust += 3
        stop music fadeout 5.0

        "{i}Ayane's lust has increased to [ayane_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label dojogen2:
    scene ayanenoongen2
    with dissolve
    play music "sakuya4.mp3"

    "I wind up in the dojo and spend the afternoon watching Ayane spar with various other...karate people. Or whatever they're called."
    "It's become pretty evident by now that I have no real intention of improving my ability, but Ayane has seemed more determined than ever lately."

    if bonus == True:
        "I worry that she might be drifting out of her seemingly endless honeymoon-phase with me but, in some way, this feels like a little more than that."
        "It's like she's becoming so comfortable with the bond between us that just being around me is enough to validate her feelings."

    "It's cute. So cute that I can't help cheering her on as she tries to take down her sparring partners."

    scene black
    with dissolve

    if secondbeach18 == True and christmastwo20 == False:
        "Ayane wins every single match she takes place in and, riding a high of confidence, challenges {s}the karate instructor{/s} NO ONE. OSAKO IS NOT HERE RIGHT NOW. AYANE FIGHTS ALONE."
        "Of course, she is then promptly annihilated and spends the next ten minutes convincing me to give her a massage."
        "I agree but, the second I attempt to do so, the {s}instructor{/s} NO ONE asks us to either focus up or leave."
    else:
        "Ayane wins every single match she takes place in and, riding a high of confidence, challenges the karate instructor."
        "Of course, she is then promptly annihilated and spends the next ten minutes convincing me to give her a massage."
        "I agree but, the second I attempt to do so, the instructor asks us to either focus up or leave."

    "Ayane focuses up."
    "I leave."

    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane's affection has increased to [ayane_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label callayanemorning:
    if ayane_love >= 10 and cafesugar == True and dojo10 == True and ayanedorm5 == True and ayanenew1 == False:
        jump ayanenew1
    if ayane_love >= 45 and ayanespecial40 == True and bar55 == True and ayanesanabeach1 == False:
        jump ayanesanabeach1
    if chap4active == True:
        jump ayanespringmorninggen
    if chapthreeactive == True:
        jump ayanesummer2morninggen
    if amisroom5 == True and ayanedorm10 == True:
        play sound "phonebeep.wav"

        "I tap on Ayane's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        ay "Good morning, my love!"

        "Ayane shouts so loudly that I instinctively need to move the phone away from my ear for a moment."

        s "Hey...You seem a little energetic for this hour of the day."
        s "How long have you been awake?"
        ay "Mmm...An hour or two? I just got out of the shower."
        s "Are you always this energetic after a shower?"
        ay "Not always! I'm probably just a little excited that you called so early."
        ay "Do you want to maybe get breakfast with me or something? I can tell you all about the crazy dream I had."
        s "Sure. I was actually wondering if you wanted to meet up."
        ay "Hooray!"
        ay "Does the diner sound okay? Your house is on the way so I can just meet you there."
        ay "Oh! Wait. Ami would probably get jealous if I did that."
        ay "Maybe just meet me there?"
        s "Yeah, that's probably best."
        ay "Okay! I'll get dressed right now."
        ay "I love you!"

        play sound "phonebeep.wav"

        "Ayane excitedly hangs up the phone and, before I know it, I'm on the way to the diner."

        scene black
        with dissolve

        "........."
        "......"
        "..."

        if christmas7 == True:
            jump ayanemorninggen2

        scene ayanemorninggen
        with fade
        play music "normalday.mp3"

        "Ayane shows up at the diner a few minutes after I do and greets me with a huge hug."

        if bonus == True:
            "It attracts the attention of a few other customers, but I think most of them just chalk it up to our relationship being familial in nature."
            "I doubt anyone would expect a guy my age to be having a romantic meeting with someone like Ayane this early in the morning in front of so many people."
            "But, I mean...I guess this {i}is{/i} sort of a romantic meeting in a sense."
            "Sure. We're on opposite ends of the table and Ayane is just going on about a dream she had, but it feels like the connection between us is stronger than ever before."
        else:
            "We proceed to bond over our shared love of doughnuts."

        "It's strange how just doing normal things together can manage to bring people so close."

        scene black
        with dissolve

        "Ayane says goodbye to me with a hug just as strong as the one she gave me when she arrived."
        "She presses her face against my chest and closes her eyes, smiling like a girl bidding goodbye to her father on his way to work."
        "Of course, that daughterly illusion doesn't last long."

        if bonus == True:
            "It's broken when she whispers into my ear to come see her at night soon before kissing me on the cheek and skipping away."
        else:
            "It's broken when she whispers into my ear about a sale on eggs at the convenience store."

        $ ayane_love += 1
        stop music fadeout 5.0

        "{i}Ayane's affection has increased to [ayane_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Ayane's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "No answer. Maybe she's busy?"

        jump callmorning

label ayanemorninggen2:
    scene ayanemorninggen2
    with dissolve
    play music "normalday.mp3"

    "Ayane shows up at the diner a few minutes after I do and greets me with a huge hug."
    "It attracts the attention of a few other customers, but I think most of them just chalk it up to our relationship being familial in nature."
    "I doubt anyone would expect a guy my age to be having a romantic meeting with someone like Ayane this early in the morning in front of so many people."
    "But, I mean...I guess this {i}is{/i} sort of a romantic meeting in a sense."
    "Sure. We're on opposite ends of the table and Ayane is just going on about a dream she had, but it feels like the connection between us is stronger than ever before."
    "It's strange how just doing normal things together can manage to bring people so close."

    scene black
    with dissolve

    "Ayane says goodbye to me with a hug just as strong as the one she gave me when she arrived."
    "She presses her face against my chest and closes her eyes, smiling like a girl bidding goodbye to her father on his way to work."
    "Of course, that daughterly illusion doesn't last long."

    if bonus == True:
        "It's broken when she whispers into my ear to come see her at night soon before kissing me on the cheek and skipping away."
    else:
        "It's broken when she whispers into my ear to come organize bones with her at night."

    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane's affection has increased to [ayane_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label callayaneafternoon:
    if firsttimedojo == False:
        play sound "phonebeep.wav"

        "I tap on Ayane's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "No answer. Maybe she's busy?"
        jump callafternoon
    elif chap4active == True:
        "Ayane normally hangs out at the pool around this time."
        "I can probably see her there if I head over now."
        jump callafternoon
    else:
        "Ayane should be at the dojo right now."
        "I can probably see her there if I head over now."
        jump callafternoon

label callayanenight:
    if chap4active == True:
        jump ayanespringnightgen
    if chapthreeactive == True:
        jump ayanesummer2nightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Ayane's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "No answer. Maybe she's busy?"
        "I might be able to see her if I visit the dorms."

        jump callnight

label firsttimedojo:
    play music "sakuya4.mp3" fadein 2.0
    scene ayanefirstdojo1
    with fade

    "I decide to use this brand new lease on life to become a karate champion and check out the dojo."
    "Just kidding."
    "Well, about the karate champion part at least."
    "I just figure that there's a relatively high likelihood of me bumping into someone from class here because..."
    "Wait, why {i}do{/i} I feel like that?"
    "I get lost in quiet contemplation for a moment and don't manage to shrug it off until I can hear the excited pounding of footsteps on the floor mat inching closer to me at a frighteningly rapid pace."

    scene ayanefirstdojo2
    with dissolve

    ay "Sensei? What are {i}you{/i} doing here? I've never seen you come by the dojo before."
    s "Better question: what are {i}you{/i} doing here? You just provided weight to an inner monologue I didn't fully understand and now I have to wrap my head around two things at once."

    scene ayanefirstdojo3
    with dissolve

    ay "Me? I'm training."
    s "Training for what, exactly?"

    scene ayanefirstdojo4
    with dissolve

    ay "{i}Battle.{/i}"
    s "Well, good luck. I can't imagine there's a lot of that around here."
    ay "The first rule of karate is to be ready for anything, especially {i}war.{/i}"
    s "I thought the first rule of karate was to only use it as self-defense?"

    scene ayanefirstdojo5
    with dissolve

    ay "Hmph. Of course that’s what someone without any experience or training would think."
    ay "But me? I’ve been here for centuries...honing the Amamiya family secret techniques...and waiting for the perfect moment to showcase my unwavering bravery and reclaim these lands."
    s "Where was that {i}unwavering bravery{/i} when you ran away from my penis the other day?"

    scene ayanefirstdojo6
    with dissolve

    ay "That was no normal penis! And I know a normal penis when I see one! I have done plenty of research!"
    kin "Amamiya! What the fuck do you think you're yelling about over there?! And who's that guy with you?!"

    scene ayanefirstdojo7
    with dissolve

    ay "Sorry, Miss Osaka! He's my...dad!"
    kin "Your-"
    kin "You know what? Fuck it. I don't want to deal with this right now. Tell him to either pay up or get out."

    scene ayanefirstdojo8
    with dissolve

    ay "You need to pay up or get out, Sensei. I'm already on thin ice from bringing my chicken here all the time and can't afford another demerit."
    s "I have so many questions and feel like none of them are going to be answered."

    scene ayanefirstdojo3
    with dissolve

    ay "If you want to stick around, I wouldn't mind paying for you."
    ay "There's a 50%% discount on your first lesson here and, if you like it, it means we can start spending every single waking moment of every single day together."
    ay "Doesn't that sound amazing?"
    s "No. It sounds loud."
    ay "Loud can be good. That's another thing I've learned from research."
    s "Ayane, how exactly do you spend all of your free time?"
    ay "Thinking about you! Which is where all of the research comes into play. I need to be ready for when {i}you're{/i} ready to love me."
    s "Again, you ran away from a solid opportunity to put that to the test and-"

    scene ayanefirstdojo6
    with dissolve

    ay "Well, forgive me for not expecting the gateway to my dreams to open up in the middle of a sleepover!"
    ay "This isn't one of those sex games that Ami and I {i}accidentally{/i} downloaded while you weren't home, Sensei! Things like that don't happen in real life!"
    ay "I'm a real girl with real feelings and-"
    kin "Amamiya!"
    ay "And a real dad who I am trying to convince to start karate right now!"
    s "I know you're just covering up, but being called that twice in such quick succession is making me feel weird."

    scene ayanefirstdojo9
    with dissolve

    ay "Well...then tell me what you're doing here. Because you still haven't answered that and it feels extremely random if it's not to see me."
    ay "And I haven't even been doing this for long, so I doubt anyone else told you."
    ay "Shouldn’t you be like, spending time with Ami or something?"
    s "Ami is old enough to do things on her own, just like I’m old enough to visit a random dojo in the middle of the afternoon."

    scene ayanefirstdojo3
    with dissolve

    ay "So it {i}is{/i} just a completely random visit without any purpose or goal."
    s "Humans are strange creatures, Ayane. We often do things we can't explain or understand."
    s "Like, you're a teenager in a city nearly devoid of male life and you're spending your afternoon practicing self defense when I imagine all of your friends are off having fun."
    s "What's your explanation for that?"
    ay "I-"
    s "And don't give me that whole {i}it's to reclaim my land{/i} thing again. Why are you {i}really{/i} here?"

    scene ayanefirstdojo10
    with dissolve

    ay "Humans are strange creatures, Sensei. We often do things we can't explain or understand."
    s "See? I'm right. You're no different than me."
    s "We're just two people who somehow landed in a place we don't belong and are now left to either abandon it or adapt."
    ay "I vote for adaptation."
    s "I think we might be members of different parties, then."

    scene ayanefirstdojo11
    with dissolve

    ay "No, no! Hear me out! Karate is crazy fun and {i}great{/i} for your body and mind!"
    ay "Just look what it's done for my muscles! Feel!"

    "Ayane forcefully grabs my wrist and places my hand on one of her biceps."
    "Her arms are so small that I’m able to wrap my entire hand around them, but I {i}do{/i} feel a bit of definition there."

    ay "See? Aren't you impressed?"
    ay "I feel like it was just yesterday you were poking my arms and calling them squishy. Now, I could probably beat you to death blindfolded!"
    s "That's an absurd amount of progress for still being relatively new to this."

    scene ayanefirstdojo3
    with dissolve

    ay "I'm pretty great at stuff when I actually apply myself, you know. And, up until you showed up, I was trying really hard."
    s "Are you saying that I'm the main obstacle preventing you from achieving your goals now?"
    ay "No, I'm saying that there are certain goals that take priority. And one of them decided to show up out of nowhere and surprise me."

    "Unsure of how to respond to that, I shift my gaze across the room to find a good number of girls from all ages doing various drills or...techniques or...whatever you call karate practice."

    scene ayanefirstdojo12
    with dissolve

    "The instructor, who looks around my age (Give or take a few years), swiftly moves from group to group, skeptically locking eyes with me every once in a while as if to say {i}get out.{/i}"
    "Which, to be fair, I probably should. I'm clearly not the...demographic this place is shooting for."
    "But if this is where Ayane is going to be spending most of her time..."
    "Maybe coming around a little more often wouldn't be all that bad?"

    ay "You know...I really wasn't kidding when I suggested that you should enroll here, Sensei."
    s "Wouldn't it be weird, though? I'm the only male and probably the oldest person here."
    ay "I don’t think it would be {i}that{/i} weird. We’d just have to act normal and not be all over each other."
    s "That sounds hard when a great deal of your personality seems to revolve around verbally suffocating me."
    ay "I can hold back if I have to."
    ay "If that's what it takes to get you here, I'll do it."
    s "Ayane-"

    scene ayanefirstdojo10
    with dissolve

    ay "I want more of you, Sensei. A lot more. And I don't just mean that in a weird way."
    ay "I do mean it in a {i}kind of{/i} weird way. But not entirely weird. Maybe like...fifty-fifty?"
    s "And you think one of those fifties would be able to keep the other in check if I decide to start...doing karate or whatever?"
    ay "Isn't that the whole idea of halves? To balance each other out?"
    ay "Join the class, Sensei. I really don't mind paying for you. I put it all on my credit card anyway."
    s "I just...can't foresee myself actually enjoying karate, Ayane."
    ay "Then enjoy my company- the same way I've been enjoying yours for years."
    ay "I'm not young and immature anymore."
    s "Yes you are."

    scene ayanefirstdojo13
    with dissolve

    ay "Okay. Yes, I am...But I am {i}less{/i} young and {i}less{/i} immature."

    scene ayanefirstdojo3
    with dissolve

    ay "And I'm ready to take things to the next level in the least creepy way I could possibly say that which, I admit, still probably sounds kind of creepy."
    s "It's fine. I'm kind of creepy for not walking away by now anyway."
    ay "So..."
    ay "Does this mean we can be creeps together?"

    "I take another look around the dojo and try to figure out if this is really where I want to be spending a good chunk of my time."
    "And...I don't think it is."
    "But when my eyes realign and I'm stuck staring directly ahead-"
    "I make a decision."
    "For sometimes, it's a matter less of {i}where{/i} you are and more {i}who{/i} you're with."
    "And I struggle to say it in a way that wouldn't land me on a list somewhere-"
    "But I think I want more of Ayane just as badly as she wants more of me."

    s "I think it does."

    scene ayanefirstdojo14
    with dissolve

    ay "Heck yeah, let's go!"
    ay "I'll sign the papers right now! You just wait right here, Sensei!"
    s "Wouldn't I need to sign them if-"
    ay "Nope! I've already memorized your signature and used it on several official documents, so you can just leave this part to me!"
    s "What? What documents did-"

    scene ayanefirstdojo1
    with dissolve

    s "Ayane, come on. You can't just walk away without telling me that."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ firsttimedojo = True
    $ ayane_love += 1

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdaynight

label dojo3to4:
    play music "sakuya4.mp3" fadein 2.0
    scene dojo
    with dissolve

    "I head back to the dojo to practice with Ayane."
    "The two of us get dressed and she begins to go over some of the basics of karate."
    "Of course, this quickly devolves into her becoming overly-affectionate and she
    winds up needing to take several breaks to 'reset' her emotions."
    "I learn next to nothing and leave the dojo no better at martial arts than I was when I arrived."
    "But hey, at least I got to hang out with a cute girl..."

    $ ayane_love += 1

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdaynight


label dojo5:
    stop music fadeout 3.0
    scene black
    with dissolve2

    "{i}Legends have it that centuries ago...a single family ruled over all of Kumon-mi.{/i}"
    "{i}Many armies, with the aid of mercenaries and sellswords tried to overthrow this family...{/i}"
    "{i}But every attempt amounted to nothing more than senseless bloodshed and a shameful voyage back home...{/i}"
    "{i}But one day, after hundreds of years and nearly one thousand fruitless attempts..."
    "{i}The family that had once ruled over Kumon-mi...{/i}"
    "{i}Fell.{/i}"
    "{i}And from that moment on...{/i}"
    "{i}They were never able to recover.{/i}"
    "{i}...{/i}"
    "{i}Until today.{/i}"
    "{i}When one girl begins her conquest...{/i}"
    "{i}To reclaim what is rightfully hers...{/i}"
    "Disclaimer: Lessons in Love contains large amounts of information and data that is factually incorrect and no words should be taken as gospel."

    scene karate1
    with dissolve2
    play music "rapid.mp3"

    ay "My name is Ayane Amamiya of the Amamiya family...and I am here to take back what is mine!"

    scene karate2
    with fade

    s "Oh please...You really expect me to believe that a {i}child{/i} like you aims to take back Kumon-mi?"
    ay "Woah, where did that huge lens flare come from?!"
    s "This territory belongs to the Arakawas now, little girl..."
    s "The Amamiyas have had no place here since the...War of...Blood."

    scene karate3
    with fade

    ay "Who are you calling a little girl, you pathetic weakling?"
    ay "The War of Blood may have ended a long time ago, but the stains it left on these grounds have yet to be forgotten."
    ay "Do you have any idea how many lives have been taken with just these hands alone? Because it's more than you could possibly fathom."
    ay "Heed my words, Arakawa. If you have even the {i}slightest{/i} desire to survive, you'll-"

    scene karate4
    with hpunch

    s "I’ll what? Walk away from here and give up on Kumon-mi?"
    ay "Ahh! There are even more of them now!"
    s "You’re out of your mind."
    s "I have spent the last nine thousand years honing my power and-"

    scene karate5
    with hpunch

    ay "What?! Nine thousand?!"
    ay "There is no way that can be right! Can it?!"

    scene karate4
    with dissolve

    s "Nine thousand years is nothing to me."
    s "After all, I was born with..."
    s "{i}That{/i} bloodline..."

    scene karate5
    with hpunch

    ay "What?! {i}That{/i} bloodline?!"

    scene karate6
    with fade

    s "Yes..."

    scene karate7
    with hpunch

    s "{i}THAT{/i} BLOODLINE!!!"

    scene karate8
    with fade

    ay "This can't be...all this time I thought {i}I{/i} was the protagonist, but..."
    ay "If he has {i}that{/i} bloodline..."
    ay "Could this be the end of my journey?..."
    ay "No..."
    ay "It can’t be..."
    ay "Not after all I've sacrificed..."
    ay "I’ve come too far to give up now...there has to be {i}something{/i} I can do..."

    scene karate4
    with dissolve

    s "It’s over, Ayane...I have the high ground."

    scene karate5
    with hpunch

    ay "We’re on the same level! You're just a little taller!"

    scene karate6
    with dissolve

    s "But, you see...that’s where you’re wrong..."
    s "You and I will {i}never{/i} be on the same level..."

    scene karate4
    with dissolve

    s "It doesn’t matter how much you train or how many of my underlings you defeat..."
    s "This is the end of the road. Defeating me isn’t possible..."

    scene karate9
    with fade

    ay "Then you leave me no choice..."

    play sound "static.mp3"
    scene karate10
    with flash
    stop sound

    s "No...It can’t be!"
    ay "It can!"
    ay "You’ve given me no choice but to unleash the Amamiya family’s hidden technique!"
    kin "Amamiya, for the last time, put that thing away! You’re going to get us shut down!"
    ay "Miss Osaka! Turn the fan speed up! My hair isn't blowing fast enough!"
    kin "We don't have a-"
    kin "Wait, where did this giant fan even come from?!"

    scene karate11
    with fade

    ay "I’m sorry things have to end this way..."
    ay "You deserve the death of a warrior, not that of a dog."

    scene karate12
    with fade

    s "Hah..."
    s "Hahahah..."
    ay "...What's so funny?"
    s "Hahahahaha!"
    ay "Wait...No..."
    ay "He {i}can't{/i} be..."

    scene karate13
    with hpunch

    s "But I can..."
    s "You’ve fallen into my trap, little girl."
    s "You see..."
    s "I was born {i}immune{/i} to bullets."

    scene karate5
    with hpunch

    ay "No! That can’t be!"

    scene karate7
    with hpunch

    s "It is!"

    scene karate14
    with dissolve

    "The staredown between the two fierce warriors goes on for hours..."
    "Days..."
    "Weeks..."
    "Millennia..."
    "But the sheer respect for one another’s power is enough to force them into exercising more caution than they ever have before."
    "{i}This{/i} was the moment they had lived for..."
    "The moment to finally prove who the rightful ruler of Kumon-mi is!"

    "{i}How will it end?!{/i}"
    "{i}Who will triumph?{/i}"
    "{i}Will Ayane Amamiya take back the land her family had all but built with their bare hands?!{/i}"
    "{i}Or...{/i}"
    "{i}Will the mysterious ronin, clad only in sweatpants and a T-shirt, be able to fend off the legendary Amamiya fighting style?!{/i}"
    "{i}Find out next time on Lessons in Love ~ The Battle for Kumon-mi!{/i}"

    scene battletwo6
    with dissolve2

    "{i}This program was brought to you in part by Koi Cafe! Home of the [[copyrighted frozen beverage]!{/i}"
    "{i}Long day? Short night? Come to Koi Cafe and try our specialty handcrafted drinks made by adorable girls!{/i}"
    "{i}See you again next time!{/i}"
    "{i}Pluuuuus...EXTRA!{/i}"

    scene black
    with dissolve2
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    scene karateredux1
    with dissolve2
    play music "sakuya4.mp3" fadein 2.0

    ay "So yeah, that’s basically how you do karate."
    kin "Are you two seriously just going to leave this thing here?! What am I supposed to do about this?!"
    s "I feel like I actually did pretty well."
    ay "Yeah, you were surprisingly good. You really had me going with that whole bloodline thing."
    s "Thanks. Came up with that off the top of my head. Totally not a play on a mildly obscure video series from 2009."
    ay "Wow, that seems so long ago."
    s "Yeah. We’re dying faster than we like to admit."

    scene karateredux2
    with dissolve

    ay "Well, you are at least. I’m a perfectly healthy, able-bodied [young_girl] who is going to take back her family’s land through martial arts!"
    s "Just remember, you’ll have to defeat me first."
    kin "Seriously. What the fuck am I supposed to do about this?"
    ay "Pfft. You make it sound like defeating you is supposed to be a challenge."
    s "It will be now that you know I’m immune to bullets."
    s "Also, where the hell did you get that gun? It looked real."

    scene karateredux3
    with dissolve

    ay "There are three things you never ask a lady, Sensei! Her age, her weight, and where she got her automatic rifle."
    s "I don’t remember ever learning about that last one."
    ay "Then maybe it’s time to start studying up!"

    scene karateredux2
    with dissolve

    ay "When you aren’t too busy training to defeat me, I mean."
    s "Right, right."
    s "Anyway, we should probably get a move on before the instructor asks us to do something about the industrial size fan you had air lifted here for our sparring match today."
    ay "Yeah. It's a good thing she hasn't noticed it yet."

    scene karateredux4
    with dissolve

    kin "I want this thing gone in ten minutes or the two of you aren't allowed back anymore."

    scene karateredux5
    with dissolve

    ay "..."
    s "..."
    ay "I'll call in another helicopter..."

    scene black
    with dissolve

    "Ayane and I finish up our ‘karate’ routine for the day and change back into our normal clothes while waiting for the helicopter to arrive."
    "Unfortunately, she has to feed her chicken after this, so the two of us need to break apart and go our separate ways."
    "Without anything left to do, I depart the dojo and begin to wander the streets in search of something to close out the day with..."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo5 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    jump saturdaynight

label dojo10:
    scene namesredux1
    with dissolve
    play music "lifeismostlygood.mp3"

    "I begin to make my way to the dojo because I have lost all control over my life and am slowly falling into the clutches of a rich blonde girl."
    "But hey, she's cute and she likes me- which is really way more than I should be asking for in the first place."
    "So if going along with her weird roleplay stuff is all I have to do to get closer to her, I'm absolutely going to do that."
    "Would she continue falling for me even if I decided to {i}not{/i} do things like that with her? Probably."
    "But I want her to fall faster."
    "And me looking like an idiot is a small price to pay for getting an attractive teenager's pants off."

    scene namesredux2
    with dissolve

    ay "Oh, Sensei! What are you up to?"

    "Or dress, I suppose."

    s "I was actually just on my way to the dojo. Are you heading there now?"

    scene namesredux3
    with dissolve

    ay "Actually...I'm coming {i}back{/i} from the dojo right now..."
    s "Don't tell me you actually got kicked out?"
    s "Was it the giant fan? The guns? Never listening to the instructor? Ordering pizza in the middle of lessons? Riding a-"
    ay "I get it. I like to have fun."
    ay "But no, I wasn't kicked out. The dojo is just closed for the day- which is a real bummer since I was in the mood to actually practice for {i}real{/i} this time."
    s "Yeah, I'm not buying that."

    scene namesredux4
    with dissolve

    ay "I mean it! I was feeling really fired up today!"
    ay "And just so you know, until you started showing up all the time, I really {i}was{/i} giving it my all!"
    ay "It's just a lot harder to focus on things when you're there. I blame your sweatpants."
    s "My sweatpants?..."

    scene namesredux5
    with dissolve

    ay "Yeah. Don't you feel the same way about girls in pajamas? Like, they'd just be so easy to just slip off and..."
    s "...and what?"
    ay "I can't finish that sentence because there is a woman pushing a stroller behind you and I don't want to taint the poor baby's ears with all of the impure thoughts I have."
    s "How are you able to maintain friendships when it seems like the only thing you have on your mind at all times is me?"

    scene namesredux6
    with dissolve

    ay "Mmm...I guess it probably helps that my best friend is the only other person in this city who can compete with me in terms of how much we love you."
    s "You need new hobbies."

    scene namesredux7
    with dissolve

    ay "Sorry, my only other hobby closed down for the day, so you're going to have to deal with me just talking about how much I love you for the rest of the afternoon."
    ay "Have I mentioned lately that I love you? Because I love you."
    s "I had no idea. You hide it so well."
    ay "Not as well as you hide your freakishly huge penis behind those old sweatpants in karate class."
    s "..."

    scene namesredux2
    with dissolve

    ay "Do you have a bucket of cold water you could dump on my head? That's what Maya always does when I start rambling on about you and I think it would come in handy right now."
    s "I don't, no..."

    "It never ceases to amaze me how open Ayane is about her feelings for me..."

    if bonus == True:
        "I really don’t get it, to be honest."
        "I'm not particularly attractive or...interesting..."
        "I'm not even fun."
        "I'm just...there."
        "But...maybe that's exactly {i}why{/i} she likes me?"
        "Because I'm the only man she's in regular contact with- and one that she's apparently been around for years."
        "How far back do these feelings go?"
        "And what sorts of feelings were locked away inside of {i}this{/i} body before I was granted the opportunity to take over?"

        play sound "static.mp3"
        scene namesredux8 with flash
        stop sound
        stop music

        "{s}NONE{/s}"

        play sound "static.mp3"
        scene namesredux2 with flash
        stop sound
        play music "lifeismostlygood.mp3"
    else:
        "I really wish she'd just accept me as her teacher and not constantly drop hints about a deeper type of relationship when I do not intend to ever have something like that with her."
        "Girls are gross."

    s "Well anyway, since we can’t do anything at the dojo, did you want to hang out around here?"

    scene namesredux9
    with dissolve

    ay "Like...around here? But what if people see us?"

    if bonus == True:
        s "Weren't you ranting about my penis to a mysterious woman like, thirty seconds ago?"
        ay "No, I was ranting about the layer of suspiciously provocative fabric that {i}conceals{/i} your penis. It's totally different."
        s "Either way, it’s not like we’ll be holding hands or making out or anything. It's not a big deal if people see us together in the middle of the day."

        scene namesredux10
        with dissolve

        ay "Darn it...I thought you were asking me on a date for a second."
        s "You can call it a date if you want. I’m just not a fan of the idea of publicly displaying affection."

        "Let alone publicly displaying affection with a girl young enough to be my daughter."

        scene namesredux9
        with dissolve

        ay "I figured as much. Even with Ami, you've never really liked showing affection in public. Or...really anything, for that matter."
        ay "You know, it's weird. I'm never really a fan of the mysterious type in manga...but with you, I kind of can't really imagine anything else."
        s "I'm going to take your undying love for me as an {i}okay{/i} and assume that you're fine with hanging out around here."

        scene namesredux2
        with dissolve

        ay "Sensei, you literally never have to ask me if I'm okay with anything. {i}Especially{/i} if that thing is spending time with you."
        ay "I'm just not really sure what you want to do. I've never gone on a not-date that I'm still allowed to call a date before. Let alone one with my best friend's uncle and teacher."
        s "Then I guess we can just...start off small and go for a walk or...sit on a bench and talk or something? Preferably {i}not{/i} about the type of pants I wear at the dojo."
        ay "Good call, Sensei. If there's anything I've learned from my butler, it's that you never want to get horny on a park bench."
        s "..."
        ay "..."
        ay "What?"
    else:
        s "Then we will kill them."

    scene black
    with dissolve2

    s "Nothing, Ayane."
    s "Just thinking about how I wound up here."

    "The two of us do a few laps around the block, not straying far at all from where we met up, before taking a seat on a bench near the subway station."

    scene ayanestreet1
    with dissolve

    "Ayane moves as close to me as she can without making it look like we're the world's least appropriate couple."
    "The chaotic horny energy that was radiating off of her a few minutes ago has since been replaced by an aura of adoration that painfully perforates my nostrils and lures me into a false sense of security."
    "I do not feel insecure in believing that this girl will change at the drop of a hat- but in the fact that inching closer to comfort somehow makes me less comfortable than anything else I can think of."

    ay "So, now what? Want to talk about holding hands since we're not actually allowed to do it?"
    s "I can't imagine that conversation topic lasting very long."
    ay "Then pick a better one. You're the leader of this not-date and I'm just a girl who's really thirsty for some good old-fashioned handholding."
    s "Tone it down, Ayane. Who knows what would happen to us if someone overheard you saying something as taboo as {i}that.{/i}"

    scene ayanestreet2
    with dissolve

    ay "Good point! We should talk about more socially accepted topics like the current political climate or...whether or not pineapple belongs on pizza."
    s "It doesn't."
    ay "Well, of course {i}I{/i} know that and {i}you{/i} know that, but there could be people who don't know any better walking past us and it's up to us as a responsible not-couple to not offend them."
    s "Are you sure you're okay with this, Ayane?"

    scene ayanestreet3
    with dissolve

    ay "Hm? What do you mean?"
    s "I mean, obviously I'm okay hanging out with you like this since I'm the one who asked. But the more you talk, the more I feel like you should be off bantering with someone a little better at bantering back."
    ay "But I don't want to banter with anybody else. If I did, I wouldn't have agreed to not-date you today."
    s "I guess I just don't want the not-date to be too boring for you."

    "That and I'm feeling an overwhelming difficulty being near her without capitalizing on her raging (Yet temporarily dormant) hormones."

    ay "I'm not bored at all, Sensei. I'm having tons of fun."
    ay "And it's not like I’ve ever been on a real date before, so there's no bar you need to pass or anything."

    scene ayanestreet4
    with dissolve

    s "Really? Not even once?"
    ay "Not even once."
    s "Why not?"
    ay "Because you never asked me."
    s "You make it sound like you've been saving yourself for me or something."

    scene ayanestreet5
    with dissolve

    ay "You make it sound like that's a bad thing {i}or something.{/i}"
    s "I mean, it kind of is. What if nothing ever came of it? Would you have just...gone on forever? Indefinitely waiting for me?"
    ay "Of course not, Sensei."
    s "That’s a relief. Because for a second I thought-"

    scene ayanestreet6
    with dissolve

    ay "I made a promise to myself a long time ago...that if you didn’t reciprocate my love by the time I graduate high school..."
    ay "That I would blow up the city..."
    s "..."
    ay "..."

    scene ayanestreet7
    with dissolve

    s "..."
    ay "..."

    scene ayanestreet8
    with dissolve

    ay "So, Sensei, when we get married...what are we going to name our kids?"
    ay "I really like the name Ami, but that one’s kind of already taken, so..."
    ay "Do you think Ami would be okay with changing her name if we asked her really nicely?"
    s "..."

    scene ayanestreet9
    with dissolve

    ay "Of course, there are also names like Airi or...Ayaka...or Ai..."
    ay "Or maybe Aki if we wind up having a boy first."
    ay "I like A-Names if you couldn’t tell. Like Ayane!"
    s "..."

    scene ayanestreet8
    with dissolve

    if bonus == True:
        ay "I’ve been thinking about it a lot and I’m pretty sure I want seven children if that’s okay with you."
    else:
        ay "I’ve been thinking about it a lot and I’m pretty sure I want to adopt if that’s okay with you."
        s "Oh, cool. That makes this event significantly cleaner and saves the writer from further censoring the dialogue."

    ay "I was actually telling Ami that the other day and-"

    scene ayanestreet9
    with dissolve

    ay "Oh, sorry. {i}Your{/i} Ami, not {i}our{/i} Ami. Our Ami hasn’t been born yet."
    s "..."
    ay "Anyway, I was telling her that I want seven kids with you and she was all like ‘What are you planning on doing to my [uncle]!?’"

    scene ayanestreet8
    with dissolve

    ay "And I had to be all like, ‘Nothing!’ and-"
    s "..."
    ay "..."

    scene ayanestreet10
    with dissolve

    ay "I’m a bad date, aren’t I?"
    s "What? No, that’s not it."
    s "I just don’t think I’m ready to talk about children and marriage and all that just yet..."
    ay "Is it...because you can't imagine a future with me?"
    s "I think it's more that people are...you know...sexually involved with one another before the topic of kids comes up."

    "And also the fact that I can't imagine myself ever wanting {i}any{/i} children."

    ay "I mean...I guess that makes sense."
    s "Sex is kind of required to make children, so yeah. I think it's safe to say it makes sense."
    ay "Am I wrong for daydreaming, though?"
    s "I wouldn't say {i}wrong...{/i}But I'd also maybe think a little harder before sharing some of those daydreams with people."

    scene ayanestreet11
    with dissolve

    ay "Yeah..."
    ay "Yeah, I can...get ahead of myself at times. I know."
    ay "It's just a...unique challenge to have parts of your fantasy start to come true while the other parts are forced to sit on the sidelines and wait for their turn."
    ay "I guess I'm just not great at dealing with that yet."
    ay "But I'll get better. For your sake {i}and{/i} my sake."
    ay "I don't want this to be some sort of...temporary thing, you know? I'm really serious about this, Sensei."
    s "You're-"
    ay "And before you go and say something like {i}You're just a teenager{/i} or {i}you have your whole life ahead of you{/i} I'd like an opportunity to counter."
    s "It's not really a counter unless an opposing point has been made first."
    ay "Yeah, well I've prepared myself for any opposing point you can possibly come up with-"

    scene ayanestreet12
    with dissolve
    stop music fadeout 5.0

    ay "And my counter is this..."
    s "..."
    ay "..."

    "Ayane stares deep into my eyes and I can tell that whatever she's about to say has had not months, but years of time poured into it."
    "I can only imagine how hard it must be to incessantly agonize over whether or not your dreams are achievable."
    "And with hers so close, yet so far away..."
    "These words will have to move mountains."
    "But I am no normal mountain. I am-"

    ay "I want to wake up next to those sweatpants every day for the rest of my life."
    s "..."
    ay "..."

    scene ayanestreet12r
    with dissolve
    play music "lifeismostlygood.mp3"

    s "Hah..."
    ay "I had you concerned there, didn't I?"
    ay "To be totally honest, I {i}did{/i} have a really cute, really sweet thing I was going to say- but I figured that now probably isn't the time and, well, I'm still kind of regretting not being able to do karate with you today."
    s "Well, you're definitely right. Now was most certainly not the time."
    s "Save any huge bombshells about the future of our relationship for at least a few more not-dates. {i}Then{/i} you can consider dropping them on me."
    ay "Sensei, I am going to drop so many bombshells on you that-"
    s "I'm going to cut you off right there as I can't imagine {i}any{/i} possible way for that joke to not end extremely offensively."

    scene ayanestreet13
    with dissolve

    ay "See, this is why I love you! You've been looking out for me for as long as we've known each other."
    ay "So if I can look out for you for even a fraction of that...it'll be everything I've ever wanted."
    ay "Well, almost everything."
    ay "I have several fantasies I will require your assistance in living out, but I think they would be considered bombshells, so I'll keep them to myself for now."
    s "I mean...I'd be fine with you sharing {i}those{/i} ones if-"
    ay "Nope. You made your bed and- now you have to put on your sexy sweatpants and lay in it."
    s "Okay, this date is over now."

    scene black
    with dissolve2

    ay "Woo! Best date ever! I didn't even have to use my hand grenade!"
    s "You don't have a grenade, Ayane."
    ay "That's what you think, Sensei!"
    s "Why do I feel like I understand less about you every time the two of us talk?"

    "Ayane and I leave the bench after another few minutes and make our way back to the dorms. "
    "She locks me in a bear hug for a good thirty seconds as she says goodbye and I go to pat her on the head, but have to stop myself as I don't think she's earned it quite yet."
    "Despite her mild insanity, though, she really is cute at times."
    "That cuteness just normally vanishes whenever I'm reminded that her handbag is filled with things that could get us killed."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo10 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    jump saturdaynight

label dojo20:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene ayanelay1
    with dissolve
    play music "sakuya4.mp3"

    ay "Hah...hah...hah..."
    ay "Oh my god..."
    ay "That was...so much...more intense...than it normally is..."
    s "I think I’m going to die..."
    s "I had no idea you could even do that with your legs."

    scene ayanelay2
    with dissolve

    ay "It’s not like I...wanted to!"
    ay "I just...needed to listen to orders or...I’d get in trouble..."
    s "You did well..."
    s "I’m not going to lie, I thought you’d crack under the pressure with all of the other girls watching."

    scene ayanelay3
    with dissolve

    ay "I’ve told you before, haven’t I? I don’t mind if people watch. It just puts pressure on me to do even better."

    scene ayanelay4
    with dissolve

    ay "But to think we’d have to spar the instructor herself...especially at our skill level..."
    ay "That’s just not fair. I could barely even land a hit."
    s "I think I landed one or two, but I doubt she even felt it."

    "Ayane and I just finished our training session for the day and are taking a much-needed and well-deserved rest."
    "Who would have thought that the wooden floor of the dojo could ever feel so comfortable?"
    "But I guess anything would be comfortable after expelling almost all of your energy for what feels like no purpose whatsoever."
    "In fact, no one in the entire dojo was even able to land a substantial blow on the instructor."
    "And here I was thinking this was just some random training ring for novice martial artists."

    scene ayanelay5
    with dissolve

    ay "[ayanemaster], I think we might be in trouble. What will we do if the two of us can never defeat her?"
    ay "Will we simply give up our homeland? Is she destined to be the true ruler of Kumon-mi?"
    s "Why are you grabbing my arm? Let go of me."

    scene ayanelay6
    with dissolve

    ay "Perhaps this is what must be done, though."
    ay "Our clans have been at war with one another for centuries...millennia even..."
    ay "Maybe it’s up to you and I to put an end to all of that?..."

    scene ayanelay7
    with dissolve

    if bonus == True:
        ay "What do you say, [ayanemaster]?...Are you ready to start a family?"
        s "Absolutely not. Let go of my arm."
        ay "But I like your arm. It’s big and strong and makes me feel safe."
        s "That’s great, but there’s a time and a place for everything. You clinging to me doesn’t exactly make me look like a model citizen."
    else:
        s "Absolutely not. Let go of my arm, you harlot."

    scene ayanelay8
    with dissolve

    if bonus == True:
        ay "It’s just a little grab. No one cares. It’s not like we’re having sex."
        s "What kind of warped perception do you need to have on the world to think the only
        inappropriate thing to be doing in public is having sex?"
        ay "I don’t know. But I’m not letting go. You’ll have to pry your arm away from my-"
    else:
        ay "But I paid good money of this on the black market!"

    scene ayanelay9
    with dissolve

    ay "Ah! My arm!"
    s "It’s {i}my{/i} arm, psycho."

    scene ayanelay10
    with dissolve

    ay "All I ever do is love you, and yet you break my heart."
    ay "Alas...pain is all the Amamiya dynasty has ever known. Perhaps this
    will not be the end to years of endless torment after all."
    s "Can we go back to resting now?"

    scene ayanelay11
    with dissolve

    ay "Sure! Goodnight, [ayanemaster]. Please wake me up when class is over so we can walk home together."
    s "Ayane-"
    ay "Every time you push me away, I’m only going to want you more~"
    s "So if I push you away now-"

    if bonus == True:
        ay "I’ll grab your penis and start waving it around in front of everyone like
        it’s a sparkler at a summer festival."
        s "..."
    else:
        ay "I will shrink down to microscopic size, climb inside of you, and build a home in your heart."

    s "That doesn’t sound fun at all."
    ay "It won’t be. So I suggest you let me stay like this until I fall asleep or someone tells us to break apart."
    ay "But until then, please let me hold onto you."
    ay "I’ve been feeling a little down lately and I need to be as close as possible to you so I can recharge."

    "That’s strange. It’s not like Ayane to admit when she’s upset or in a
    bad mood or whatever it is that she’s feeling right now."
    "I wonder what’s going on?"

    s "You’ve been feeling down?"
    ay "Yeah."
    s "Why?"
    ay "I don’t really wanna talk about it right now. It’s stupid."
    s "You know you can-"
    ay "Sensei. Please don’t ask me again."
    ay "I’ll tell you soon. I just don’t want to think about it right now."
    ay "I love you a lot, but even I can’t help but get a little angry if you keep asking me
    things when I tell you not to."
    s "..."
    s "Okay then."

    if bonus == True:
        s "But if someone tells you to get off of me, please don’t wave my penis around like a firework."
        ay "I won’t. That will only happen if you try to get away yourself."

    scene ayanelay12
    with dissolve

    ay "See how nice I can be when you’re obedient?"
    s "Aren’t you supposed to be the obedient one?"
    ay "I {i}am{/i} obedient. I’ll do whatever you want me to do whenever you want me to do it."
    s "Except talk about your feelings."
    ay "I’ll talk about my feelings for {i}you{/i}."
    s "I know about those already."

    scene ayanelay11
    with dissolve

    ay "I know you do. But I want to remind you again anyway so it stays in your head."
    ay "I love you more than anything in the world."
    ay "I love the way your arm feels when you let me squeeze it."
    ay "I love the way you knock on my door when you visit me at night."

    scene ayanelay12
    with dissolve

    ay "I love the way you look at me when I tell you all of these things."
    ay "I love the way you care so much about me even when you pretend not to."

    "This is...new."
    "It’s actually kind of heartwarming to spend a moment like this with Ayane without her-"

    scene ayanelay13
    with dissolve

    if bonus == True:
        ay "I love the way your giant dick feels when you put it in my-"
        s "Okay, Ayane. I get it. You love me."
    else:
        ay "And I really love the third season of Seinfeld."
        s "What?"
        ay "I used to watch it with Kirin."
        s "??????????????"
        ay "(Mimics funny bass line)"
        s "Ayane stop"

    scene ayanelay14
    with dissolve

    ay "You’re not gonna let me finish? I was just getting to the good part."

    if bonus == True:
        s "I don’t know if you’ve realized this, but I’m wearing sweatpants and I really don’t
        want to have to walk out of here with an erection."
        ay "Yeah, that would be pretty bad, wouldn’t it?"
        ay "If only having sex in public were legal. You could just let it out inside of me
        and walk out of here like nothing ever happened."
        s "How did we get back to this?"
        ay "I’m horny now."
        s "You’re always horny."
        ay "It’s easier to forget other stuff when I think about sex."
        s "..."
        s "What?"
    else:
        ay "(Continues mimicking funny bass line)"
        s "Ayane why"

    scene ayanelay11
    with dissolve

    ay "Nothing. Just thinking out loud."
    ay "I’m going to keep my eyes closed now, Sensei. Can I put your arm around me and sleep on your shoulder?"
    s "What? No. This already looks bad enough as is."
    ay "Boo~"
    ay "I guess I’ll just sleep like this, then. "
    ay "Oh, and I have a gun on me, so don’t even think about trying to run away. Got it?"
    s "Why do you always have a gun on you?"
    ay "To protect myself from muggers or anyone who tries to steal my boyfriend."
    s "..."
    s "Ayane, I’m not your-"
    ay "Goodnight, Sensei~ I love you so much."
    s "..."
    s "Ayane?"
    ay "..."

    "Ayane falls asleep seconds later, still exhausted from sparring just moments ago."
    "She was one of the last girls to go up, but despite her lack of time doing this compared to many of the others, she was actually really impressive."
    "I’ve learned by now that she’s the type of girl to never stop pursuing what she wants. And hey, if she actually wants to be a martial artist, more power to her."
    "But at the same time, that sort of mindset can be destructive. "
    "People who spend their entire life chasing one thing often forget the importance of others."
    "And no, I’m not talking about karate anymore."
    "I’m talking about me."
    "Why does she like me so much when I haven’t done anything to even almost warrant deserving that?"
    "What is it about me that is magnetizing her?"
    "Is it because she thinks I’m playing hard to get?"

    scene black
    with dissolve2

    "..."
    "Or is it something else?"

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo20 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label dojo25:
    scene black
    with dissolve2

    "{i}Somewhere...in a far-off, distant land...{/i}"
    "{i}The war rages on...{/i}"
    "{i}Previously, on the Battle for Kumon-mi...{/i}"

    scene battletwo1
    with dissolve
    play music "prairie.mp3"

    "{i}Ayane Amamiya of the famed Amamiya dynasty made her run at a lifelong adversary in hopes of reclaiming the land that was rightfully given to her at birth.{/i}"
    "{i}But after a long and painstaking series of setbacks, it finally set in that this battle might not be as easy as she originally thought!{/i}"
    "{i}With a fire in her heart and the determination to finish out the fight and reclaim her holy land, will she be able to summon the strength needed to defeat her arch-nemesis?!{/i}"

    scene battletwo2
    with dissolve2

    "{i}Or will that nemesis simply be too powerful for her to overcome?{/i}"
    "{i}The leader of the Arakawa clan has no intention of giving up the land he has worked so hard to refine and reconstruct over the course of his anguish-filled life!{/i}"
    "{i}Can one battle truly decide the fate of everything he loves?!{/i}"
    "{i}Can one battle turn the tide and restore the land to its original state, long before the endless wars and all of the lives lost?!{/i}"

    scene battletwo3
    with dissolve2

    "{i}Two hearts become one!{/i}"
    "{i}Two lost souls with nothing but regret and heavy expectations on their shoulders must set aside their love for one another to fight for the greater good!{/i}"
    "{i}Who will win?!{/i}"

    scene battletwo4
    with dissolve

    ay "I will..."

    scene battletwo5
    with dissolve

    s "No..."
    s "I will."

    scene battletwo6
    with dissolve2

    "{i}The following program is brought to you in part by Koi Cafe! Home of the [[copyrighted frozen beverage]!{/i}"
    "{i}Long day? Short night? Come to Koi Cafe and try our specialty handcrafted drinks made by adorable girls!{/i}"
    "{i}We will now return to our regularly scheduled programming.{/i}"
    "{i}Please enjoy the show!{/i}"
    "{i}Pluuuuus...EXTRA!{/i}"

    scene battletwo7
    with dissolve2

    ay "You haven’t learned a thing, have you?"
    ay "You’d think that after our last battle ended in a near-truce, you’d be a lot more welcoming today...father."

    scene battletwo8
    with dissolve

    s "That’s right. I am your father. This was a necessary plot development."
    s "I didn’t want you to find out like this, but I suppose it needed to happen eventually."
    s "So what do you say, Ayane? "
    s "Will you join forces with me and rule this land in the name of the Arakawas?"
    s "Or will you resign yourself to the cowardly Amamiyas? The same family who raised you and never told you of my existence..."

    scene battletwo9
    with dissolve

    ay "They only hid you from me because they knew it would hurt!"
    ay "But what hurts even more is knowing we are in love!"
    ay "Which I am totally okay with, by the way, but other people will probably think it’s weird!"

    scene battletwo10
    with dissolve

    s "Yes! Tap into those feelings! "
    s "Use them to become stronger, sudden-daughter of mine!"
    s "If the two of us join forces, we’ll be able to activate the hidden Arakawa-technique! The one that can only be used when father and daughter are united!"

    scene battletwo11
    with dissolve

    ay "The hidden Arakawa-technique?! Do you mean the ultra-hyper-mega-drive-flame-tornado wheel-dropkick-of-unity?!"
    s "Heh...I guess the technique wasn’t as hidden as I thought, was it?"

    scene battletwo12
    with dissolve

    ay "Tch! "
    ay "Is it really okay for me to abandon the parents who raised me in order to reunite with my biological father? Especially when both of them are dying from an unidentified disease?"

    scene battletwo13
    with dissolve

    s "Unidentified, you say?"
    s "Well that’s just simply not true."
    s "In fact, I’m the one who created the disease that’s destroying their bodies as we speak."
    s "And what’s even better-"

    scene battletwo14
    with hpunch

    s "Is that they only have three weeks left to live!"

    scene battletwo15
    with hpunch

    ay "Only three weeks?!"
    ay "How could you do this, father?!"
    ay "It’s one thing to abandon me by floating my body down the river-of-lost-hope, but to create a life-threatening disease in order to kill my adoptive parents?! "
    ay "That’s simply too much!"

    scene battletwo16
    with dissolve

    s "Funny. Some say “too much” while others say “not enough.”"
    s "Frankly, I thought about killing them much longer ago. "
    s "But six years ago, after I saw you training with a wooden sword next to your above-ground pool in the backyard, I decided I couldn’t."
    ay "That was you?!"
    s "That was me."

    scene battletwo17
    with dissolve

    ay "And to think that all of this time I’d been hoping to meet that man..."
    ay "Never did I once expect him to be the leader of the Arakawa clan who is also coincidentally my father and the man who poisoned my non-biological parents."

    scene battletwo18
    with dissolve

    s "And that’s not all..."
    ay "It’s not?!"
    ay "How much more convoluted can this get?!"
    s "You see, [young]Amamiya. I am also..."

    scene battletwo10
    with hpunch

    s "You from another timeline!!!!111111111"

    scene battletwo19
    with dissolve

    ay "NOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!111111"
    ay "I’m my own dad!!!!"
    ay "And I killed my parents!"
    ay "Well, almost!"

    scene battletwo20
    with dissolve

    ay "This means that the only way to prevent their demise is to take back Kumon-mi by going into the past and destroying my future self before I can create me."
    ay "But how?"
    ay "I haven’t learned the ability to time travel yet."

    scene battletwo21
    with dissolve

    ay "Wait..."
    ay "What about...him?"

    scene battletwo22
    with dissolve

    s "Him?..."
    s "Who are you talking about, exactly?"
    s "This is a battle between father and daughter. And also father and self."
    s "And daughter and self."
    s "And Amamiya and Arakawa."

    scene battletwo23
    with dissolve

    ay "It {i}was...{/i}"
    ay "Until now."

    scene battletwo24
    with dissolve

    s "What do you mean by that?..."
    s "We’re the only two people here."
    ay "People, yes...But why not take a look behind you?"
    s "Behind me? But what-"

    scene battletwo25
    with hpunch

    tod "BACAWK! (Prepare to be eliminated!)"
    s "I-It...It can’t be!"
    ay "Todd! Attack!"
    s "Todd?!"
    s "You should be dead!"
    ay "Todd is immortal in this timeline!"
    tod "BACAWK! (I can never die!)"
    s "I-Impossible!"

    scene battletwo26
    with dissolve

    ay "Little did you know, that girl who you saw training with her sword in the backyard was also an expert chicken-tamer!"
    s "I didn’t even know that was a thing!"
    ay "So what’ll it be, Master Arakawa? Are you ready to concede to Todd, the only person who has ever bested you in battle?"
    ay "Or will you fight to the death, ultimately killing me in the process because we’re the same person? "
    ay "Or something."

    scene battletwo27
    with dissolve

    tod "BACAWK! (Bow before me, mortal! It is I! Todd!)"
    s "Can he...drain my energy?"
    ay "Oh? You’re feeling it already?"
    ay "And here I was thinking you were stronger than that."
    ay "The only reason Todd is immortal is because he can consume the life essence of others by simply looking at them."
    s "So much...power..."
    s "My legs are...getting weaker..."
    s "I...don’t think I can stand much longer..."

    scene battletwo28
    with dissolve

    ay "Don’t worry. You won’t have to."
    ay "Lucky for you, which basically means lucky for {i}us{/i}, I’ve thought up a way to defeat you without killing you."
    s "Without...killing me?..."
    s "But...how?"
    ay "Don’t worry about that, future-me."
    ay "Just close your eyes and everything will be okay..."

    scene battletwo29
    with dissolve

    ay "AMAMIYA FAMILY HIDDEN-TECHNIQUE! THROW!"
    s "Your hidden technique is “Throw?!”"

    scene battletwo30
    with fade

    ay "Pray to whichever god you believe in, Master Arakawa..."
    ay "Your time on this planet ends now..."
    s "No...Not like this..."

    scene battletwo31
    with dissolve

    "..."

    scene battletwo32
    with dissolve

    "..."

    scene battletwo33
    with dissolve

    "..."

    ay "..."
    tod "..."
    s "Ouch."
    s "That actually kind of hurt."

    scene black
    with dissolve2

    "{i}And so the battle comes to a close!{/i}"
    "{i}Ayane Amamiya of the Amamiya clan was able to defeat her arch-nemesis, the future version of herself, alongside her trusted chicken-companion, Todd!{/i}"
    "{i}But even though the battle has been won...things do not end here.{/i}"
    "{i}What will happen next?! Has Ayane truly reclaimed the land of Kumon-mi?!{/i}"
    "{i}Or is there an even greater evil lurking somewhere in the shadows?...{/i}"

    scene battletwo6
    with dissolve2

    "{i}This episode of The Battle for Kumon-mi was brought to you in part by Koi Cafe!{/i}"
    "{i}Long day? Short night? Come to Koi Cafe and try our specialty handcrafted drinks made by adorable girls!{/i}"
    "{i}Thank you for watching our regularly scheduled broadcast!{/i}"
    "{i}See you next time!{/i}"
    "{i}PLUUUUUS...EXTRA!{/i}"

    stop music fadeout 5.0

    "........."
    "......"
    "..."

    scene battletwo34
    with dissolve2
    play music "sakuya4.mp3"

    ay "Well fought today, Sensei."
    ay "I had no idea you were really me this entire time."
    ay "But I guess it makes sense given how much the two of us have in common."
    s "Yeah, I figured you might like that part."
    s "Also, I had no idea you owned a chicken."
    ay "Really? He follows me around all the time."
    ay "Sometimes, I don’t even realize he’s there. "
    ay "He’s a good boy, though."
    s "Why did you name him Todd? Is he American?"
    ay "No, he’s a chicken. Idiot."

    scene battletwo35
    with dissolve

    ay "It’s kind of sad that we might not be able to do stuff like this anymore soon, though..."
    s "What do you mean? The dojo isn’t closing down, is it?"

    scene battletwo36
    with dissolve

    ay "I’m not sure, to be honest."
    ay "I heard the instructor talking about how someone was looking into buying it."
    ay "I don’t have any idea what would happen to it after that."
    s "Well I can’t imagine they’d buy a dojo to just make it...not a dojo anymore."
    s "Sounds like we’ll just have new management or something. "
    s "I don’t think we’ll be impacted that much."
    s "Besides, couldn’t {i}you{/i} just buy it if things really came to that? You’re rich."

    scene battletwo37
    with dissolve

    ay "True. But just because I’m rich doesn’t mean I could buy an entire dojo without any problems."
    ay "I can’t just put it on my credit card and my dad is the one with the actual bank-access and stuff."
    ay "I’m pretty sure if I asked him to buy a dojo when we already have a nicer one on the premises, he'd say no."
    s "Good point."
    s "I don’t think we need to worry, though. I can’t imagine anything will happen to this place in the end."

    scene battletwo38
    with dissolve

    ay "Hopefully you’re right. All of the times we’ve spent here have become really important memories to me."
    ay "Seeing them taken away would be kind of devastating."
    s "Worse comes to worst, we just hang out at your house, I guess."
    ay "Yeah...Let’s hope it doesn’t come to that, though."

    scene black
    with dissolve2

    "Ayane and I remain in the dojo for another half hour or so, reminiscing about all of the times we’ve spent here over the last few months."

    if bonus == True:
        "The reminiscing turns to something slightly more suggestive once she starts recollecting how far we've come since then."
        "But at least it got her mind off of the sudden potential for our normal hang-out spot to become a thing of the past."
        "I really hope that rumor doesn’t wind up actually being true."
        "I’m finally starting to get used to this..."

    $ renpy.end_replay()
    $ dojo25 = True
    $ ayane_love += 1
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label dojo30:
    scene ayanetoukadojo1
    with dissolve
    play music "sakuya4.mp3"

    "Ayane and I are resting for a bit after actually spending the afternoon training."
    "Given that we’ve been spending most of our recent days messing around and playing with her chicken (Which is apparently not allowed in the dojo), we figured it was about time to actually try."
    "That and the instructor has been getting on our case about taking things seriously or we’ll be removed from the class."
    "To be honest, I wouldn’t mind being kicked out since it would mean less time physically exerting myself...but Ayane likely would, so I’ve been bearing with it for her sake."
    "And yes, I can be nice like this every once in a while if I actually apply myself."

    ay "Sensei! Did you see my sweet dropkick earlier? I almost landed a hit on the instructor!"
    s "Yes. And I also saw you get scolded shortly after for using a pro-wrestling style dropkick in karate class."

    scene ayanetoukadojo2
    with dissolve

    ay "Hey, if it works, it works."
    s "It didn’t work, though."
    ay "Yeah, but neither does normal karate so I was trying to improvise."
    ay "It's not my fault Miss Osaka is some kind of martial arts goddess."
    s "I didn’t say that was your fault. I’m just saying you might want to start using, you know, {i}karate{/i} moves if you ever plan on getting better at karate."

    scene ayanetoukadojo3
    with dissolve

    ay "Guh. Maybe we should just take up pro-wrestling instead? Especially with all of those rumors floating around about the place being sold and stuff."
    s "Those are {i}still{/i} going around?"

    scene ayanetoukadojo4
    with dissolve

    ay "They haven’t even slowed down. "
    ay "I tried asking Miss Osaka about it the other day and even she wasn’t sure what was going on."
    ay "She doesn’t even know if she’ll be allowed to keep her job, so I told her I’d ask my dad about hiring her as my personal instructor if things really came to that."
    s "Is this really what you want to keep on doing? You're not going to, like...move on or something?"

    scene ayanetoukadojo1
    with dissolve

    ay "Do you remember the first time you showed up here, Sensei?"
    s "I am reminded every time the instructor makes fun of me for not paying my own membership."
    ay "There's no shame in having a sugar mama, Sensei."
    s "Yes there is and please don't call yourself that."
    ay "Anyway, it might sound a little silly...but I think it may have been fate that led you here."
    ay "So unless there’s some sign that descends from up above telling me that I should stop doing karate, I’m going to keep going."
    ay "Besides, even if I’m using American wrestling moves, I’ve definitely been feeling way better physically lately."

    if bonus == True:
        ay "My body’s actually in such good shape that pretty soon, I might be able to pull off some super crazy sex moves."
        s "I’m quite interested in finding out what sort of {i}super crazy sex moves{/i} derive from amateur karate lessons."
    else:
        ay "It is probably due to all of the steroids I am on."
        s "What?"

    scene ayanetoukadojo5
    with dissolve

    ay "They’d probably be easier for you to understand if you actually practiced every once in a while."
    s "What do you think I was doing today? I very clearly practiced."

    if bonus == True:
        ay "For three minutes, sure. After that, you just sat around and stared at all of the other girls’ butts."
        s "I was practicing my observational skills- one of the key fundamentals of karate."

        scene ayanetoukadojo6
        with dissolve

        ay "Well observe {i}me{/i} more next time instead of everybody else or I’ll be forced to become a martial arts master and eliminate all of them."
    else:
        ay "You call that practice, you little shit? Drop and give me twenty."
        s "But twenty is so many."

    scene ayanetoukadojo7
    with dissolve

    rlg "Pardon me, you two, but would either of you be willing to spare a moment of your time?"
    rlg "I’d like to ask you a few questions about this establishment, if you don’t mind."

    scene ayanetoukadojo8
    with dissolve

    ay "Hm? Who’s that?"
    s "No clue. She looks really...elegant, though."

    scene ayanetoukadojo9
    with dissolve

    ay "And I don’t?!"
    s "Not really. Her rich-girl aura is much stronger than yours. Especially considering you’re wearing a karate uniform."
    ay "It’s called a {i}Karategi{/i}, Sensei! Pay attention in class!"
    s "But there are just so many butts to look at."
    rlg "Umm...hello? Can you not see me?"
    rlg "Is there some sort of...karate code barring you from speaking with people dressed in normal attire?"

    scene ayanetoukadojo10
    with dissolve

    ay "Oh, no. Sorry."
    ay "You can come talk to us as long as you promise not to steal this man away from me."
    rlg "I have no intention of that whatsoever. He seems rather brutish in nature."
    s "You know, maybe it would be better if you two just spoke in private. I’m clearly not needed here."

    scene ayanetoukadojo11
    with dissolve

    ay "Oh, stop. You know I need you every minute of every day...Every day of every year. Every-"
    rlg "Every year of every decade."

    scene ayanetoukadojo12
    with dissolve

    ay "..."
    s "..."
    rlg "Oh, sincerest apologies. I thought we were playing a game."
    rlg "You’ll need to forgive me. I don’t typically converse with the middle class and may say some things that are quite hard for people of your kind to understand."
    ay "Middle class? But I’m not middle class at all."
    ay "I have the second largest house in Kumon-mi. We even have a room that's literally just a giant ball pit."
    s "What? Since when?"

    scene ayanetoukadojo13
    with dissolve

    rlg "The second largest..."
    rlg "Then that must mean-"

    scene ayanetoukadojo14
    with dissolve

    rlg "You wouldn’t happen to be Ayane Amamiya, would you?"
    ay "That's my name!"
    ay "But...who are you exactly? You've yet to introduce yourself."

    scene ayanetoukadojo15
    with dissolve

    rlg "Oh my, where are my manners?"
    to "My name is Touka Tsukioka- daughter of Tomonori Tsukioka and planned heir of the Tsukioka Foundation. It’s wonderful to finally meet you."
    ay "Nice to meet you too! Judging by your clothes, I’m guessing you’ve got an even bigger ball pit than I do."
    to "Ball...pit?"
    ay "It's like a swimming pool full of plastic balls."
    to "How wonderfully creative. My family prefers to fill our pools with water. It had not occurred to me until today that there were other options available."
    ay "You don't get out much, do you?"

    scene ayanetoukadojo16
    with dissolve

    to "And you are? A butler perhaps?"
    ay "Oh, that’s my teacher. And future husband."

    scene ayanetoukadojo17
    with dissolve

    to "I beg your pardon?"
    ay "He's my future husband, I said. We're going to get married and have a disturbing amount of children one day."
    to "Future husband? This man?"
    to "You’ll have to forgive me if this is some sort of joke I’m not picking up on, but he seems rather...unfitting. Don’t you think?"
    s "That's fair. But also kind of rude."

    scene ayanetoukadojo18
    with dissolve

    ay "Woah- hold on a second. I don’t care {i}how{/i} rich you are, no one talks down to Sensei in front of me. And {i}definitely{/i} no one questions whether he and I are meant to be together."

    "I can think of at least eleven other girls who question that off the top of my head."

    to "Oh dear, I’m terribly sorry. I didn’t mean to offend."
    to "I just assumed you’d be getting married to someone of slightly higher status to propel your family’s name forward."
    to "But, perhaps...that’s just the way my family handles things? If so, I humbly ask for forgiveness."

    scene ayanetoukadojo19
    with dissolve

    ay "Uhh...it’s fine, just..."
    ay "What’s up? Why did you need to talk to us?"

    scene ayanetoukadojo20
    with dissolve

    to "Oh, yes. I was actually just looking to speak with some of the common folk who use this dojo about their feelings for it."
    to "You see, I’ve recently taken an interest in martial arts and have been looking into acquiring an establishment like this one for my own personal use."

    scene ayanetoukadojo21
    with dissolve

    to "Of course, it’s overwhelmingly clear that a large amount of work must be done in order to bring it up to my family's standards-"
    to "So hearing about the condition of the building from people who are here regularly would provide some much-needed peace of mind."
    ay "Wait...hold on...{i}You’re{/i} the one who’s planning on buying this place out?"
    s "I don't mean to brag, but I kind of saw that one coming."

    scene ayanetoukadojo22
    with dissolve

    ay "I didn’t! I thought she was just here to try out the class or something!"
    to "Oh, heavens no. I could never practice in a place like this given its current state. Especially not alongside people like this commoner here."
    to "I’m sure you understand that I mean no offense by that, yes?"
    s "I think you could probably use a little more practice when it comes to {i}not{/i} offending people."
    s "You’re not wrong, though."
    to "I seldom am."

    scene ayanetoukadojo23
    with dissolve

    ay "With all due respect, Touka...this place really means a lot to me and everyone else here."
    ay "Having this dojo taken from us would leave pretty much nowhere else to practice."
    to "I’m sure there is a...parking lot or vacant warehouse somewhere in the city that you can use if you truly want, correct?"
    ay "Doesn’t the same go for you? Do you even know karate?"
    to "Not yet, but my father is insistent on hiring the greatest instructor in Kumon-mi to tutor me directly."
    to "You know how fathers can be. Only the best for their daughters and whatnot."

    scene ayanetoukadojo24
    with dissolve

    ay "Only...the best for..."
    to "Miss Amamiya?...Did I say something wrong?"
    to "Is it because you don’t think you’ll be able to practice here anymore?"
    to "If it truly upsets you, I may be able to convince my father to let you train alongside me given our respective statuses in the city."
    to "Though...I unfortunately can not guarantee that the others will be able to join us as well."
    to "I’m sure you understand."
    ay "Not really..."
    ay "And I’m kind of starting to lose hope now, so..."
    ay "I think I’m going to go for a walk."
    s "Ayane-"

    scene ayanetoukadojo25
    with dissolve

    ay "Don’t...follow me, okay? I’ve gotta try and figure some stuff out..."
    ay "I’ll call you later."
    s "Uhh...sure. Okay."
    s "See you later, then."
    to "Miss Amamiya, I-"

    scene ayanetoukadojo26
    with dissolve

    "Ayane walks out of the dojo without even changing back into her normal clothes and suddenly I’m alone with a girl who has likely never been this close to someone as “middle-class” as me."

    to "Oh dear..."
    to "I had no idea that these circumstances would affect her so dramatically."
    s "You didn’t think that buying out the place she comes to every weekend would upset her?"

    scene ayanetoukadojo27
    with dissolve

    to "I did not know she came here in general."
    to "Miss Amamiya’s family is not one I know on a personal level, but I’ve heard my father speak of them on numerous occasions."
    to "Never in a million years did I think she’d be spending time somewhere so...{i}this{/i}."
    to "Perhaps her wealth is not as great as I’d been led to believe..."
    s "I think it’s more along the lines of Ayane wanting to feel like a normal girl. She definitely has money."
    s "I was at her house just recently and can testify that it was pretty remarkable."

    scene ayanetoukadojo28
    with dissolve

    to "They let you in?"
    s "...Yes. They let me in."
    to "Wow. It’s just one surprise after another today."
    s "Ayane was right. You don’t really get out much, do you?"

    scene ayanetoukadojo29
    with dissolve

    to "I actually go horseback riding rather frequently. And I’m part of a women’s golf organization as well."
    s "You’re just a walking rich-girl stereotype, aren’t you?"

    scene ayanetoukadojo30
    with dissolve

    to "Hahah! I suppose I am!"

    scene black
    with dissolve2

    "Touka gets off the ground (Which I’m sure was a real pain to sit on for someone of her status) and exits the dojo minutes later."
    "With Ayane still nowhere to be found, I make my way over to the instructor to figure out whether or not she knows anything..."
    "........."
    "......"
    "..."

    scene ayanetoukadojo31
    with dissolve

    kin "What now? Don’t you give me enough problems already?"
    s "No. I’m here to give you one more."
    kin "Of course you are. What do you need?"
    kin "Is this about the rich girl who just waltzed in here like she owned the place?"
    s "I mean...{i}isn’t she{/i} actually about to own the place, though?"

    scene ayanetoukadojo32
    with dissolve

    kin "Beats me. I'm more worried about keeping my job than anything else."
    kin "It's not like any of you take this seriously anyway. Why does it matter if someone else buys the place out?"
    s "Ayane takes it seriously."

    scene ayanetoukadojo33
    with dissolve

    kin "Then she should stop bringing guns in. We’re lucky she hasn’t gotten us closed down to begin with."
    s "I can't believe I'm asking this...but is there anything we can do?"

    scene ayanetoukadojo34
    with dissolve

    kin "If you’re really that worried, which I’m sure you aren’t considering you’ve spent maybe less than an hour actually doing anything since you signed up, why not talk to Ayane first?"
    s "I talk to Ayane all the time."
    kin "Not like that, you fucking idiot."
    kin "Ayane's crazy rich too, isn’t she? Maybe their families can start some sort of bidding war or something?"
    s "Maybe?...She didn’t seem to think her dad would be into the idea, though."
    kin "Don’t know until you try, right?"
    kin "It's not really my place to interfere. I'm just hoping this Tsukioka girl isn’t a pain in the ass."
    kin "Because based on first impressions alone, she really comes off as that “Don’t hit me” type and girls like that are the actual worst to teach."
    kin "Especially when their fathers step in and prevent you from doing things how you know they need to be done."
    kin "Really lucked out with Ayane not being like that, now that I think about it."
    kin "I guess she is kind of a good girl...even if she’s broken literally every single rule I set."
    s "Well, no matter what happens to the dojo, I hope things work out for you."
    kin "What? No you don't. You have never expressed an ounce of concern for me in my life."
    s "Then I will start right now."
    kin "Cool. Start by practicing."

    scene black
    with dissolve

    s "On second thought, it's getting late and I should probably start heading home."
    kin "Yeah, that's exactly what I thought..."

    "Obviously, I don't intend to actually go home. But as I exit the dojo, I {i}am{/i} hoping to find Ayane sulking on the steps or something."
    "Of course, she’s nowhere to be found- so I take a few laps around the block in an attempt to bump into her before giving up on it entirely and deciding to just...do something else for the rest of the day."
    "She'll call me if she needs me."
    "Maybe."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo30 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label ayaneinvite1:
    play sound "phonebeep.wav"

    "I tap on Ayane’s name in my phone and wait for her to answer. "
    "I figure that if there’s anyone who would be happy to receive an invite to the house from me directly, it would be her."
    "But, then again, there’s a good chance she’s already there right now if she went home with Ami."
    "If that were the case, I’d feel a little strange about calling her right now...but I guess it’s going to wind up being strange no matter what at this point."
    "As long as she agrees, that is."
    "Which she will because she is Ayane."

    play sound "phonebeep.wav"

    ay "Yes! I will!"
    s "What? I haven’t even asked you anything yet."
    ay "Whatever you want, the answer is yes!"

    if bonus == True:
        ay "Unless you’re breaking up with me. Then the answer is no."
        s "We’re not even dating, Ayane."
        ay "That’s okay! We don’t need to put a label on our love!"
        ay "I’ll be excited to spend the rest of my life with you no matter what we call it~"
        s "..."
    else:
        ay "Unless you are planning on ordering dinner from Wendy's! If that is the case, I don't want any!"
        s "That is not what is happening here."

    ay "So, anyway, what was it you wanted?"
    s "I was going to see if you wanted to come over but now I might be having second-"
    ay "I’m on my way!"

    play sound "phonebeep.wav"

    s "..."

    "Welp, any second thoughts I might have had don’t matter now."

    scene black
    with dissolve
    stop music fadeout 5.0

    "Ayane is already on the way to the house...and since I'm the one who invited her over, a certain [niece] of mine might be a little taken aback by a sudden appearance from the bubble wrap princess."
    "Especially an appearance that would likely begin with something along the lines of “I am here for your [uncle],” or whatever it is Ayane would say."
    "So I guess I should hurry up and get home before something like that happens."
    "........."
    "......"
    "..."

    scene ayanefirstinvite1
    with dissolve
    play music "happyandplotting.mp3"

    "I manage to show up at the house before Ayane makes it here and find Ami microwaving something in the kitchen."
    "She tries to start a conversation with me but, knowing how things like this tend to go, I dismiss her entirely and make it seem like I’m in no mood to talk."
    "An excellent strategy, if you ask me."
    "This way, once Ayane makes it over, the two of us can quickly duck into my room before Ami has a chance to-"

    play sound "knock.mp3"

    ay "Open up! I’m ready for love!"
    s "..."

    "Before Ami has a chance to find out that she’s here."

    play sound "lock.mp3"

    "The lock suddenly...unlocks?"

    play sound "dooropen.mp3"
    scene ayanefirstinvite2
    with dissolve

    ay "Oh, good. You’re right here."
    ay "I had to use my emergency key since you took too long to answer the door."
    s "You walked in two seconds after knocking."
    ay "And they were the longest, most painful two seconds of my life."

    scene ayanefirstinvite3
    with dissolve

    ay "Thanks for inviting me over today, Sensei."
    ay "Normally, it’s Ami who asks me to come over and I need to think up creative ways to get to you instead."
    ay "I’m glad that she isn’t around and that I won’t have to do that today."
    s "Here’s the thing, Ayane. Ami {i}is{/i} around today."

    scene ayanefirstinvite4
    with dissolve

    ay "And you still invited me over?"
    ay "Do you have a deathwish?"
    s "No. I do not have a deathwish."
    ay "Then are you trying to get {i}me{/i} killed? Because there is no way that one of those two things won’t be happening."

    if bonus == True:
        ay "Especially since you called me over to have sex with me on her bed."
        s "It’s going to be fi- "
        s "Wait a second. That is {i}not{/i} why I called you over here."
        ay "It’s not?"

    s "I feel like you gravely misinterpreted the purpose of this meeting."

    if bonus == True:
        ay "But we’ve already done it on my bed and your bed so the next logical step has to be hers, doesn’t it?"
        s "I just wanted to spend time with you..."
        ay "With me or in me?"
        ay "I’m very horny today."
        s "I can see that."

        scene ayanefirstinvite5
        with dissolve

        ay "I can’t imagine it will be easy doing something like that with Ami around, though."
        ay "I mean, I guess we could wait until she’s in the bath or something, but-"
        s "Why don’t we just hang out in my room and {i}not{/i} risk dismantling our relationship today?"

        scene ayanefirstinvite6
        with dissolve

        ay "Ah! You said relationship! I {i}knew{/i} we were dating! "
        ay "No take backs, [ayanemaster]! I hereby pronounce us husband and wife!"
        ay "You may kiss the Ayane!"

    play sound "dooropen.mp3"
    scene ayanefirstinvite7
    with dissolve

    a "Sensei? Is somebody else out here? I thought I heard-"

    scene ayanefirstinvite8
    with dissolve

    a "Ayane? What are you doing here?"
    a "Did we have plans to hang out today?"
    a "I’m really sorry. I completely forgot."
    a "If you want to come hang out in my room, I’m watching this show about-"
    ay "A-Actually, Ami..."
    ay "I’m...here to..."
    s "..."

    scene ayanefirstinvite9
    with dissolve

    ay "I’m sorry. I don’t want to be the one to break her heart."
    ay "Ami is my best friend and I could never hurt her like this."
    a "Hurt me like what? What are you talking about?"
    a "Also, what are you still doing out here, Sensei? "
    a "I thought you wanted to be left alone today?"
    a "This whole situation is starting to feel really-"

    scene ayanefirstinvite10
    with dissolve

    a "Hey, wait a second! I see what’s going on here!"
    ay "You...do?"
    a "You two were going to cook me a surprise dinner, weren’t you?!"
    s "..."
    ay "..."
    ay "Yes."

    if bonus == True:
        ay "I did not come here to defile your bed."

    ay "I came here to cook food."

    scene ayanefirstinvite11
    with dissolve

    a "Sensei...you weren't in a bad mood after all. You were just upset because you saw me microwaving food instead of cooking dinner..."
    a "So you probably called the first name in your phone and had them rush over here to help since you can’t cook at all."
    a "And since Ayane is the first name to come after Ami in your contacts, you just threw a Hail Mary and prayed she’d be free."
    a "I’m so sorry that I worried you so much. "
    a "I’m okay, Ayane. You can go home now and I will spend the rest of the night comforting my [uncle]."
    s "..."
    ay "..."
    s "Actually-"
    s "I asked Ayane to hang out today."

    scene ayanefirstinvite12
    with dissolve

    ay "Ah..."
    a "You...what?"
    a "You mean you tried to call me in your phone and then...pressed her name on accident and felt bad about turning her away...or?"
    ay "I really hope not. That would break my heart."
    s "No, I called her intentionally because I wanted to see her."
    ay "..."
    a "So...you probably just assumed I was working or something then, right?"
    a "Cause there’s no reason you’d ever...call her instead of me..."
    ay "{i}Just roll with it, Sensei. This is the best escape route you’re going to get.{/i}"
    s "..."
    a "..."
    s "Yeah, sure. Why not."

    scene ayanefirstinvite13
    with dissolve

    a "Jeez...Just check with me next time, Sensei...Do you really get lonely that easily?"
    a "You don’t have to invite people here just because you think I’m going to be away."
    a "In fact, if you close your eyes and think of me, it’s almost like I’m always there! Or something!"
    a "Hahaha...hahahahah..."

    "This level of denial is something I’d expect from a relapsing drug addict, not a girl catching her [uncle] spending time with one of her friends."
    "Though, to be fair, both of those things sound kind of bad when put into words."
    "If anything, mine might actually sound worse."
    "But that doesn’t change the fact that I {i}did{/i} invite Ayane to the house today, and abandoning her now of all times would be too rude even for me."
    "I just have to think of a way to get Ami out of the picture- which might actually be a little harder than normal given that she’s on high alert right now."

    s "Well...I {i}did{/i} promise Ayane that the two of us could do something tonight, so if you could-"

    scene ayanefirstinvite14
    with dissolve

    ay "Actually..."
    ay "How about we all just hang out together? Like old times."
    a "You mean like...when you first started coming over a billion years ago?"
    ay "Yeah, before Maya came into the picture."
    a "That makes it sound like you don’t like Maya."
    ay "I love Maya. But you and Sensei are basically family to me."
    ay "So spending time with the two of you like how we used to is really all I could ask for."

    scene ayanefirstinvite15
    with dissolve

    "Ayane and I lock eyes for a moment and I honestly can’t tell whether or not she’s actually okay with this."
    "Her words sound sincere but, just a few moments ago, she was over the moon at the prospect of hanging out alone with me."
    "Taking that away from her now seems like it would just be adding more weight to the burden she already carries in hiding (Or at least {i}trying{/i} to hide) her feelings for me."

    s "{i}Are you really okay with that?{/i}"
    ay "{i}Of course.{/i}"

    if bonus == True:
        ay "{i}Hearing you stand up for me made me happier than getting pounded on Ami’s bed ever would.{/i}"
        s "{i}That’s not a thing you should be whispering with her right there.{/i}"
        ay "{i}I’m going to go home and [masturbate] to you tonight.{/i}"
        s "{i}Cool.{/i}"

    a "Uhh...guys?"
    a "If the {i}three{/i} of us are going to hang out, you should probably stop whispering to each other."
    a "I’d like to be included too, you know."

    scene ayanefirstinvite16
    with dissolve

    ay "Oh, of course! "
    ay "Sorry, Ami. I was just striking up a compromise with Sensei since we’ve now included you in our plans."
    a "What kind of compromise?!"
    a "What happened to all that stuff about the “old times” or whatever?! Why is there suddenly a condition?!"
    ay "It’s a simple condition."
    ay "All I ask is that I get to hold Sensei’s hand for the rest of the day while you stay ten feet away from us."
    a "I might as well be in a different room at that point!"
    ay "Well, if that’s what you’d prefer, then feel free to-"
    a "Unhand my [uncle], Ayane! Your compromise is denied!"
    a "If anyone is holding Sensei’s hand, it is his [niece] and your {i}alleged{/i} best friend!"
    s "Let the record show that I have two hands and can easily solve this problem for everyone."
    ay "See, Ami? I was even kind enough to leave his other hand available for you."
    ay "As long as you’re able to remain ten feet away, that is."

    scene ayanefirstinvite17
    with dissolve

    a "Sensei’s super tall but even {i}his{/i} stupid hand won’t reach that far! This is an unrealistic condition!"
    ay "Five feet?"
    a "No!"
    ay "Four?"
    a "Still no!"
    ay "Okay, okay. Fine. You’re free to hold his other hand. But I also get to rest my head on his shoulder when we sit on the couch."

    scene ayanefirstinvite18
    with dissolve

    a "Then so...do...I..."

    if bonus == True:
        a "I’m gonna cuddle with him in ways that someone like you could never even imagine..."

    ay "Oh? Is that a challenge, Ami?"
    ay "I’m sure you remember how our last challenge ended up, don’t you?"
    a "You mean the cooking one?"
    a "I defeated you. I asserted dominance."
    ay "You may have won, yes..."
    ay "But who got to hold the giant banana?"

    scene ayanefirstinvite19
    with dissolve

    a "A...ya...neeeeeeeeeeeeeeeeeeee!!!!!!!!!!!"
    ay "{i}This banana belongs to me...{/i}"

    scene black
    with dissolve2

    "And that basically explains how the rest of the night went."
    "Ayane and Ami proceeded to fight over me for the next several hours, using my arms like some sort of tug-of-war rope and leaving me broken and bruised by the time the day ended."
    "But even though it’s become hard to feel my fingers, it was nice seeing two girls who care so much about me fight each other like that."
    "I kind of wish they would have pulled each other's hair or something, though."
    "That’s what this night {i}really{/i} needed."

    $ renpy.end_replay()
    $ ayane_love += 3
    $ ayaneinvite1 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayaneinvite2:
    play sound "phonebeep.wav"

    "I tap on Ayane’s name in my phone and wait for her to answer."
    "Ami told me earlier today that she was covering a shift for Uta at the maid cafe so, unless something has changed, the house should be completely empty tonight."
    "Ayane’s last visit to the house was nice, but I’m sure it wasn’t exactly the type of visit she was looking forward to."

    if bonus == True:
        "The blame for that falls on me, obviously, so the least I can do is make it up to her with some proper “alone time.”"
    else:
        "The blame for that falls on me, obviously, so the least I can do is make it up to her with some proper “hug time.”"

    play sound "phonebeep.wav"

    ay "[ayanemaster]! I was wondering when you would call."
    s "You were?"
    ay "Yes!"
    ay "I mean, I’m always wondering that. But I had a good feeling that it would actually happen today."
    s "I see..."
    s "Well, you’re in luck because I was wondering if you’d want to come over today."
    s "Ami isn’t going to be around and-"
    ay "I know. I’m already inside of your house."
    s "...Why?"
    ay "I was waiting for you to get home."

    if day < 6:
        s "How did you even get there so quickly? Class just ended a little while ago."
    else:
        s "Since when?..."

    ay "That doesn’t matter! Just hurry up and get over here so I don’t miss out on any teacher-time!"
    s "Again, please stop calling it that. I really don’t like it."
    ay "And I really don’t like being alone in your house, so run! Run, [ayanemaster]!"

    stop music fadeout 5.0
    scene black
    with dissolve
    play sound "phonebeep.wav"

    "I hang up the phone and absolutely do {i}not{/i} run."

    if bonus == True:
        "Why would I waste energy on something like that when I’m likely going to wind up having sex as soon as I get there?"
        "I’m taking my time for Ayane’s sake. She should thank me for showing up fashionably late."

    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene lr2_noon
    with dissolve2
    play music "behindabathroom.mp3"

    "I don’t see Ayane when I walk into the house."
    "I figure this means she’s hanging out in my bedroom already, so I’m kind of excited to see what she has in store for me."

    if bonus == True:
        "She’s been here for god knows how long at this point so there might even be some sort of lavish set up like there was when I took her virginity."
        "I still think back on how cute that was sometimes."
        "Of course, that thought slips away when I remember the look on her face shortly after turning her into a woman."

    play sound "dooropen.mp3"
    scene bedroom_noon
    with fade

    s "Okay Ayane, let’s see what you’ve got..."
    s "...in store for me."
    s "..."

    "She didn’t leave, did she?"

    if bonus == True:
        jump ayaneamisbedx
    else:
        scene black
        with dissolve

        "In the end, it turned out that she did."

        $ renpy.end_replay()
        $ ayaneinvite2 = True
        $ ayane_lust += 3
        stop music fadeout 8.0

        "{i}Ayane’s lust has increased to [ayane_lust] even though she left and you didn't get to hug her!{/i}"
        "{i}You can now invite her over to the house on nights and choose to raise your affection or lust with her!{/i}"
        "{i}Hopefully, she won't leave next time!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label ayanelust15:
    play sound "knock.mp3"

    ay "Um...Sensei?"
    ay "You’re in there, right?"

    "Ayane shows up at my door because...well, she’s Ayane. And it’s my door."
    "Of course she’d be here."

    s "I am, but are you sure it’s a good idea to come visit me while there are people looking for you?"
    ay "..."
    s "Ayane?"
    ay "Can you just let me in?"

    scene black
    with dissolve

    "I turn around and head to the door to save both of us some time since she’s not really someone I can just turn away."
    "Besides, if she doesn’t want anyone to find her, it would be a lot safer in here than if she was aimlessly wandering around the halls."

    play sound "lock.mp3"

    "I unlock the door and pull it open."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene ayanekirinfuntime1
    with dissolve
    play music "asobeatsex8.mp3"

    ki "Surprise!"

    if bonus == True:
        jump ayanelust15x
    else:
        "Kirin and Ayane show up to play a game of Monopoly despite Ayane really not wanting to."
        "We wind up making our own rules and I am forced to choose which one of them is the winner."

        menu:
            "Ayane wins":
                s "Ayane is the Monopoly champion."
                ay "Yay!"

                $ ayanebjcontest = True
                $ dorm1warpoints += 1
            "Kirin wins":
                s "I think Kirin is better at Monopoly."
                ay "Aww. Darn it."

                $ kirinbjcontest = True
                $ dorm2warpoints += 1

        $ ayane_lust += 3
        $ kirin_lust += 3
        $ renpy.end_replay()
        $ ayanelust15 = True
        scene black with dissolve2
        stop music fadeout 7.0

        "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
        "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
        "........."
        "......"
        "..."

        jump dormwar9

label dojo35:
    scene ayanedojothreefive1
    with dissolve
    play music "sakuya4.mp3"

    "I make my way through a crowd of girls practicing roundhouse kicks or something."
    "Actually, I can't even tell what kind of kick it is."
    "I feel like I should probably pay more attention in this class if I’m going to start calling moves and techniques by their proper names."
    "Anyway-"
    "I make my way through a crowd of girls doing indiscernible karate kick things and find Ayane pressed up against a wall in the back half of the dojo."
    "The sun must be feeling particularly feisty today as it leaps in through the window and reminds us that, even in winter, it is a giant, vicious ball of fire."

    ay "So...you came after all..."

    "Wind blows in through the window and misses Ayane’s hair by an inch or two."
    "I decide to mention it anyway, though, because I feel like I’m going to have to set the stage for what I imagine will be another roleplaying session."

    os "Amamiya! Are you doing anything today or are you just going to sit there?!"
    ay "Do you know what day today is, Sensei?"

    if day == 6:
        s "Saturday."
        ay "Not just Saturday."
        ay "It’s the anniversary of our fated first encounter under the world tree."
    else:
        s "Sunday."
        ay "Not just Sunday."
        ay "It’s the anniversary of our fated first encounter under the world tree."

    s "There’s a world tree now?"

    scene ayanedojothreefive2
    with dissolve

    ay "Oh, right...you lost your memories after retreating to the mountains and overworking yourself to the point of amnesia."

    "No, I was just reincarnated."
    "Probably."

    ay "But that’s fine...I’m already shouldering some of the world’s greatest secrets."
    ay "One more will not do me in."

    scene ayanedojothreefive3
    with dissolve

    ay "Just know...this is an important day for both of us."
    ay "And the fact that I must live through it each and every year on my own is tearing me up inside."
    s "Are you crying?"
    ay "Yes, but only in character. I’m fine otherwise."
    s "You’re a surprisingly good actress."

    scene ayanedojothreefive4
    with dissolve

    ay "Thank you!"
    ay "Ami and I used to have fake battles in her bedroom while you were out doing Sensei stuff, so I got a lot of practice in then."

    scene ayanedojothreefive5
    with dissolve

    os "At least give me a fucking answer, come on!"
    os "What happened to the two of you who were fighting to keep this place open?"
    os "Was it really all so you could just sit around and stare at each other all day?"
    ay "Sitting around and staring at Sensei is far more important to me than karate lessons."
    ay "Besides, I’m not feeling well today."

    scene ayanedojothreefive6
    with fade

    os "Again?"
    os "This is like the third weekend in a row."
    ay "On the bright side, I still showed up to see your beautiful face!"
    os "Flattery won’t earn you a belt, Ayane."
    os "If you want to get serious about this like you said, you’re going to have to actually start putting in the time."
    ay "I know, I know. And I will soon, I promise."
    os "Also, what the hell is with that posture? At least sit up straight if you’re going to be taking {i}another{/i} day off."

    scene ayanedojothreefive7
    with dissolve

    ay "No can do, Sensei...I have to sit this way or I won’t look cool. It’s half the reason my monologue succeeded."
    s "I know Osako is the instructor, but please don’t call her “Sensei.” It is needlessly confusing for me."

    scene ayanedojothreefive8
    with dissolve

    os "Are {i}you{/i} the reason she’s sitting out over and over again? Because I have no problem kicking you out of here for doing...literally nothing at any point ever."
    s "I’ll take you on right now, Osako."

    if bonus == True:
        s "I have to fight naked, though. It’s part of Arakawa family tradition."
        ay "Ahh yes, {i}crouching sausage style.{/i} One I’m all too familiar with."

    scene ayanedojothreefive9
    with dissolve

    if bonus == True:
        os "Yeah...I bet you are."
        ay "Hahah...hah..."
    else:
        os "I would rather fight Ayane. She is smaller than me and I want to see how many bones of hers I can break."
        ay "I must become stronger."

    s "Ayane will start practicing again next session. Just take it easy on her today."
    s "She’s still getting over how I lost my memory when I went into the mountains to-"

    scene ayanedojothreefive10
    with dissolve

    os "Leave and never come back."
    s "I’m sorry, who are you again? I lost my memory and can’t seem to remember your-"
    os "I’m the woman who is going to end your life."
    s "At least give your girlfriend that sweet release first. She’s been asking for it ever since I met her."

    scene ayanedojothreefive11
    with dissolve

    os "Wha- Never mention Wakana and “sweet release” in the same sentence again or I really {i}will{/i} end your life!"

    if bonus == True:
        s "Don’t worry. I only fantasize about you two on occasion. It doesn’t happen every night."
        os "Don’t fantasize about us ever!"
        s "I can’t help it. That’s just the way I am, unfortunately."
    else:
        s "I apologize for offending you. I did not mean it."

    scene ayanedojothreefive12
    with dissolve

    os "Whatever. Just don’t be expecting another invite out anytime soon."
    s "But we had so much fun."
    os "Fuck off. Goodbye."

    scene ayanedojothreefive13
    with dissolve

    "Osako storms off and-"

    ay "Did you go out with our karate instructor recently?"

    "And Ayane wastes no time getting to the interrogation that was sure to spring up as a result of that."

    s "It was just a spur of the moment thing."
    s "She and Wakana were leaving[school] together and they invited Maya and me to come get coffee with them."

    scene ayanedojothreefive14
    with dissolve

    ay "Maya was there too? But wouldn’t that make it kind of like a...double date?"
    s "With anyone other than Maya, sure. She only came because she was hungry."

    scene ayanedojothreefive15
    with dissolve

    ay "Well...okay. That does check out."
    ay "She’s kind of an abyss when it comes to food."
    s "That aside, though...what’s going on with you?"

    scene ayanedojothreefive16
    with dissolve

    ay "With me? What do you mean?"
    ay "Didn’t I already tell you that I’m grieving over having to spend our anniversary alone?"
    s "Were you grieving the apparent last several times you’ve sat out training as well?"
    ay "I’ve just been tired."
    s "That’s been happening a lot lately, though."
    s "You didn’t show up to the end of the dorm war. And you passed out extremely early the last time you slept over my place with Ami."

    scene ayanedojothreefive17
    with dissolve

    ay "What are you getting at, exactly?"
    s "I just want to know if everything is okay."
    ay "You’re worried about me?"
    s "I mean, I didn’t want to come out and say it. But yeah. Of course."
    s "One or two times would be fine. In fact, it {i}was{/i} fine. But this whole karate thing on top of that is just a pretty big red flag for me to think something’s actually going on."

    scene ayanedojothreefive18
    with dissolve

    ay "Well...thank you for your concern. But I haven’t really figured out a good way to talk about it yet."
    ay "You already know that I’m pretty bad when it comes to stuff like this, so I guess I’ve just been coasting on secret girl powers to get by."
    s "Secret...what now?"

    scene ayanedojothreefive19
    with dissolve

    ay "A hidden technique every girl is born with!"
    ay "The option to get out of stuff by blaming it on not feeling well!"
    ay "Want to get out of gym class? Say you’re on your period! Don’t want to go hang out with your friends? Period again!"

    if bonus == True:
        "My mind immediately jumps to the several times girls have dodged having sex with me for reasons related to that and I suddenly lose trust in everyone."
        "Nowhere is safe anymore."

    s "That’s evil."

    scene ayanedojothreefive20
    with dissolve

    ay "It’s not evil. It’s just a way for us to take advantage of our cuteness and gain some kind of benefit in the process."
    s "Yeah, well, I’m pretty sure people are going to catch on if you’ve been blaming your lack of participation on your period for several months straight."

    scene ayanedojothreefive21
    with dissolve

    ay "Uhh...well, all I said is that I wasn’t feeling well. So it was kind of a gray area."
    ay "But you’re right. I should stop trying to get the world to revolve around me and only take advantage of secret girl powers once a week at most."
    s "You know, that wasn’t really the lesson I was trying to teach you, but I’m glad that you at least got something out of it."

    scene ayanedojothreefive20
    with dissolve

    ay "Since I can’t turn back on using my power today, though, does this mean you’ll hang out with me and protect me if Osako tries to roundhouse kick my head off?"

    "A-ha. So it {i}was{/i} called a roundhouse kick."

    s "Sure."
    s "I’m pretty sure everyone in the dojo already assumes that you and I are-"
    ay "In love?"

    if bonus == True:
        s "In{i}volved{/i}."
    else:
        s "No. That we are friends."

    ay "Call it love. I want to hear you say you love me."
    s "Why?"
    ay "Because you barely ever say “love” and I could really use the pick me up right about now."
    s "..."
    ay "..."
    ay "I can wait all day. I hope you know this."
    s "Fine. Whatever. I love you."

    scene ayanedojothreefive22
    with dissolve

    ay "Heheh~! I love you too!"
    ay "Now come sit next to me and let me rest my head on you so I don’t have to hold this weird sitting pose thingy anymore."

    scene black
    with dissolve

    "Ayane straightens herself out and slides over a few inches so that she’s not in direct sunlight anymore."
    "I take my place beside her and, before I can even open my mouth, she cuddles up against me in complete disregard for the stigma surrounding public displays of affection."

    scene ayanedojothreefive23
    with dissolve

    if bonus == True:
        ay "Hello, sir. Could I interest you in a horny blonde girl who wants to jerk you off in the bathroom right now?"
        s "What happened to not feeling well?"
        ay "Teacher time is the cure for everything."
        s "For the last time-"

        scene ayanedojothreefive24
        with dissolve

        ay "I’m kidding."
        ay "Well, mostly."
        ay "To be honest, I’d be okay with doing anything with you whenever you want. Wherever you want."
        ay "But right now isn’t the time."
        ay "Unless you want it to be, I mean."
        s "..."
        ay "..."
        ay "Cause if you want it to be-"
        s "I’m fine right now, Ayane."
        s "Osako is already keeping an eye on us. I’m pretty sure if we both went to the bathroom at the same time, she’d understand exactly what’s going on."
        ay "True, but I already told you I saw her making out with Ms. Watabe once. So maybe we could make it one of those “eye for an eye” thingies?"
        s "You seem pretty desperate right now."
        ay "Hormones are evil."
        ay "As soon as we touched heads, I started thinking about kissing. And then kissing made me think about touching. And then touching led to sex. And then sex led to more kissing."
        ay "Now I’m going round and round and round and round and I’m going to have to change my underwear soon."

    s "..."
    ay "..."
    s "..."
    ay "..."

    scene ayanedojothreefive25
    with dissolve

    ay "What can I do to make you want me more?"
    s "What do you mean exactly?"
    ay "I mean that...pretty soon I..."
    ay "I might want a lot more attention than I’m currently getting."
    ay "So I’m...looking for tips, I guess."

    if bonus == True:
        s "And I’m assuming that’s why you jumped straight to the horny talk?"

        scene ayanedojothreefive26
        with dissolve

        ay "Oh, no. That was just me making casual conversation."
        ay "If sex drive was all it took to convince you to be with me more, we’d be on our honeymoon in Hawaii right now."
        ay "I don't know if you've realized this, but I love your penis almost as much as I love you."
        s "I can’t just give you tips on how to steal my attention away from the others, Ayane. It doesn’t really work that way."
        ay "I know, but...let’s pretend it {i}does{/i} work that way for a second."
        ay "You’re in a room with all twenty of us and you can only choose one to spend the rest of forever with."
        s "This hypothetical situation is already flawed because Yumi would not show up for that."
        ay "Okay, so you’re in a room with nineteen of us and Yumi isn’t there."
        s "Io probably wouldn’t show up either."
        ay "So there are eighteen girls in the room and-"
        s "And if Io wasn’t there, Uta would probably be out looking for her and-"

        scene ayanedojothreefive27
        with dissolve

        ay "Can I just finish, please?"
        s "Sorry, go ahead."
        ay "If you were in a room with...pretty much every girl you know and had to choose only one of them..."
        ay "Is there anything I could do to stand out a little more?"
        s "You’re not going to just ask me who I would pick?"
        ay "Of course not. I’m afraid of what I’d hear."
        ay "I know you love me...and {i}everyone{/i} knows I love you..but I feel like there might still be more I can do to show it or..."
        s "You do more than enough."
        s "Don’t even waste your time thinking about that. There’s no point to it."
        ay "There kind of is, though..."
        ay "Like...I get that some of the other girls might {i}want{/i} you, but..."
        s "But you {i}need{/i} me?"

        scene ayanedojothreefive28
        with dissolve

        ay "Yeah."
        ay "Pretty...{i}pretty{/i} badly..."
        s "Don’t you think you should be giving yourself a little more credit?"
        s "You’re independent and smart and...can do basically anything you set your mind to."
        ay "This isn’t about {i}me{/i}."
        s "Well, if it’s about me-"

    scene ayanedojothreefive29
    with dissolve

    ay "A-Actually! Let’s just change the topic completely."

    if bonus == True:
        ay "This isn’t really the best place to get all serious and...and I think things were going in a weird direction anyway."
        ay "This is...exactly why I don’t really like talking about this kind of stuff unless I have to..."
        s "..."
        ay "..."
        s "..."
        ay "Soooooo...could I interest you in a horny blonde girl who wants to jerk you off in the bathroom right now?"
        s "You already used that line."

        scene ayanedojothreefive30
        with dissolve

        ay "And you’ve already used {i}me{/i}, but it hasn’t made you any less “excited” whenever we do it."
        ay "Some stuff is made to be reused, Sensei."
        ay "Just look at your clothes. You wear the same thing every day and I don’t love you any less for it."
        s "I have two completely different outfits, thank you very much."

        scene ayanedojothreefive31
        with dissolve

        ay "And they’re both adorable!"
        ay "But if we’re not going to complain about reusing our clothes or our bodies, don’t you think it’d be okay to reuse some lines?"
        ay "Like, if that wasn’t the case, we would have only been able to exchange “I love you’s” one time and that would not be nearly enough for my gigantic, Sensei shaped heart."
        s "If there is anything even remotely resembling me inside of you, we should rush you to the hospital immediately. That is entirely abnormal and you require immediate surgery."
        ay "Nope! It being shaped that way lets me fit more of you inside of me than it would normally and-"

        scene ayanedojothreefive32
        with dissolve

        ay "Heh."
        ay "{i}Fit more of you inside of me.{/i}"
        ay "I wasn’t even trying to make that one dirty. It just happened on its own."
        s "..."
        ay "..."
        s "You have a problem."
        ay "I do."
        ay "A big Sensei shaped problem."
        ay "But I wouldn’t trade it for the world."
    else:
        s "I would like to talk about the destruction of the Amazon rainforest and how horrible it is."
        ay "Yes. That is precisely what I wanted to talk about as well."

    scene black
    with dissolve2

    "The rest of the afternoon proceeds normally."
    "There are no more immediate or sudden tonal jumps in conversation and Ayane and I manage to make it through yet another lesson without exerting any energy whatsoever."
    "However-"

    stop music

    "I couldn’t shake the idea of there being something looming in the background."

    if bonus == False:
        "I must save the Amazon rainforest."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo35 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label ayanespecial1:
    s "Hey."
    s "What’s up?"
    ay "Oh, you know. Just...Ayane stuff."
    ay "Are you...busy right now?"
    s "I’m just watching Tsuneyo cook."
    ay "Huh? Are you all the way in the old district right now?"
    s "Nope. I’m at my house- where {i}you{/i} would also be if you weren’t using your “secret girl powers” again."
    ay "Oooooh..."
    ay "Yeah. "
    ay "Yeah, I’m feeling fine."
    ay "But...I was actually wondering if you’d want to come meet up for a little while."
    s "So you don’t want to come here, but you want me to come to you?"
    ay "Right."
    s "Am I a delivery service now?"
    ay "Hahah...maybe. "
    ay "It really is only for a little while, though."

    "I sigh to myself and look over at Tsuneyo, who isn’t paying any attention to me at all."
    "I doubt I could get away from the house without things looking suspicious, but..."
    "It isn’t often that Ayane actually asks me to come meet up with her in the middle of the night."

    s "Are you at your dorm?"
    ay "Nope."
    ay "I’m at[school]."
    s "What? Why?"
    ay "Hahah..."
    ay "That’s the weird part. "
    ay "I don’t really know."
    ay "I just got this urge to come here all of a sudden."
    s "Well that’s not suspicious at all."
    s "I’ll start heading over now."
    ay "Thanks..."
    ay "It really shouldn’t take long. Just tell Ami that you’re running out to buy them snacks or something and I’m sure everything will be okay."
    s "I kind of already botched that idea earlier by telling them to eat whatever's in the house. "
    s "I’ll think of something, though."
    ay "Okay..."
    ay "I’ll be on the roof when you get here."
    s "The roof? Why?"
    ay "The sky is all...pretty again."
    ay "You’ll see when you get here...hahah."

    "Each time Ayane laughs, it feels as if she’s punctuating a sentence that she’s either resistant to utter or just doesn’t want to bother with at all."
    "It’s a strange type of laugh- nothing like the bright and jovial giggles I’ve grown accustomed to hearing from her."
    "It means she’s hiding something again."
    "I don’t want to make things sound like I’m some sort of magician who can just tell how people are feeling at all times-"
    "But it doesn’t require a magician to discern the most obvious of verbal tics."
    "I heard somewhere that tics can be treated with medication, though."
    "So I utilize and accept my newfound role as the sole proprietor of Kumon-mi’s latest delivery service and offer up myself to her."
    "She will be fixed in no time at all."

    s "Okay."
    s "I’ll see you soon."
    ay "I love you."
    s "..."
    ay "..."

    play sound "phonebeep.wav"

    "One of us hangs up."

    s "Tsuneyo-"
    t "Go."
    t "I will inform the Emerald Guardian and the others of your absence."
    t "Dinner will be on the stove when and if you return."
    s "If?"
    t "Tragedy could strike at any moment. You must always be prepared."
    s "...Right."
    s "Anyway, I guess I’ll see you later."
    t "Perhaps."
    t "Goodnight, Sensei."

    "........."
    "......"
    "..."

    scene clearnightsky
    with dissolve2
    play music "undersea.mp3"

    "I attempt to look up at the clouds once I make my way outside but see nothing at all."
    "Nothing apart from a few stray nebulas and the remnants of dead celestial bodies drifting haplessly through the air."
    "I, too, drift haplessly through the air."
    "I float through the streets of Kumon-mi, tapping my fingers against glass boxes encasing the bulbs of streetlights as if I were tapping extensions of a ceiling in the halls of an old[school]."
    "A[school] I would have attended before my (?)  body had grown to its current size."
    "A[school] where I would have learned who I am or what I am or where I am or how I am."
    "A[school]."

    if bonus == True:
        "School."
    else:
        "College."

    "That is where I’m heading."
    "I need to remind myself, as being this close to the sky is somehow distracting me from the order at hand here."
    "To meet with a girl who needs to see me now more than ever."

    if bonus == True:
        "I wonder if we will have sex."
        "I hope that we will have sex."
        "I am happy when I have sex."

    scene black
    with dissolve2

    "I close my eyes and allow my metaphorical wings to carry me the rest of the way."
    "What I mean by this is that I’ve walked the path so many times now that I don’t even need vision in order to make it there."

    play sound "thump.mp3"

    "Or at least that’s what I think until I walk face first into a dumpster."
    "From that point onward, I keep my eyes open-"
    "Proving once and for all that you can never see more with them closed."
    "........."
    "......"
    "..."

    scene nevermind1
    with dissolve

    if bonus == True:
        "Ayane Amamiya\nOccupation: Happy girl\nVaginal Depth: Medium-Shallow"
    else:
        "Ayane Amamiya\nOccupation: Happy girl\nFavorite Fruit: Bananas"

    "She sits on a bench with a scarf wrapped around her that she had to purchase for herself because a man whom she would give her life for bought her friends one instead of her."
    "All she wanted was to match."
    "Some nights, she lays awake in bed, pondering over things those friends may have said to him while she was not around."
    "She worries that both of them are more compatible with him than she is."
    "She worries the same thing for virtually everyone else that she encounters, for sometimes simply hearing that the person you love loves you back is not enough to convince you."
    "She claims to have the blood of a warrior, but she is really just O-."
    "Giving to everyone, receiving from no one. And destined to lurk somewhere in the background until it is her time to shine."
    "Occasionally, she will glance up at the sky, wondering how much longer it will take for her “future husband” to arrive."
    "Unbeknownst to her, he is floating through the streets below, colliding with trash receptacles and attempting to catch birds."
    "He catches none, but several land beside her as she waits."
    "And waits."
    "And waits."
    "All the while, it grows."

    scene black
    with dissolve2

    "I eventually arrive at the[school] and glance down at my phone to discover that it’s taken me relatively longer than normal to make it here."
    "I have several missed messages from Ayane, but see no purpose in responding to any of them as I’ll be seeing her any minute now."
    "I spread my arms out and part the[school] gates like Moses parting the Red Sea."
    "It’s incredibly effective because the gates were actually left open, and it enables me to feel much more important than I actually am for a brief moment in time."
    "I move through the[school]."
    "I make it to the roof."
    "I open the door."

    scene nevermind2
    with dissolve

    ay "Oh, good...I was starting to worry that maybe you were...abducted or kidnapped or something."
    s "I don’t really think it would count as “kidnapping” if someone my age was taken, so abducted works fine here."

    scene nevermind3
    with dissolve

    ay "Right, yeah. I should have just followed my gut."
    s "So, you really weren’t joking about the sky."
    ay "Crazy, right? It’s been like this pretty much every night lately."
    ay "Do you know if this means anything for the weather? Like, is winter going to end early or something?"
    s "Nah. The world is just coming to an end."

    scene nevermind4
    with dissolve

    ay "Well, if that is the case, I’m glad that I get to share my final moments with you."
    s "If you’d have actually come to the slumber party thing, we could have all weathered the apocalypse together."
    ay "But, Sensei, I don’t want to be around anyone else right now."
    ay "I wanted to lure you all the way over here so I could adultnap you and hide you in a secret passage underneath my house and be together forever."
    s "Okay, well, this has been fun. But I’ve got to head out."

    scene nevermind5
    with dissolve

    ay "Oh, stop. You know I’m only kidding."
    ay "If that were ever going to happen, I’d abduct Ami, Maya, and Sana too so all of us could live happily ever after in my secret underground bunker."
    s "Sounds to me like it would get pretty cramped in there rather quickly."

    scene nevermind6
    with dissolve

    ay "Probably, yeah..."

    if bonus == True:
        ay "And that would make it kinda hard to have “private time” together, so...maybe I’ll have to have Geoffrey construct additional bunkers or something like that?"
    else:
        ay "Hey...are you forklift certified?"

    s "Ayane."

    scene nevermind3
    with dissolve

    ay "Yeah?"
    s "You didn’t invite me here for construction tips, did you?"
    ay "I did not."
    s "Then what’s going on?"
    s "This isn’t like you."

    if bonus == True:
        ay "I’m a [teenage]girl, Sensei. My body is changing. And along with it, my interests, desires, and even my personality."
    else:
        ay "You know nothing, Jon Snow."

    s "I find that hard to believe."
    ay "How come?"
    s "Because a good chunk of your personality is rooted in how much you love me."
    ay "I can promise you that at least that much will never change."
    s "I don’t want any of you to change, though."

    scene nevermind7
    with dissolve

    ay "Huh?"
    s "Why is it surprising that I preferred the version of you that wasn’t using excuses to get out of everything?"
    ay "It’s not! I just..."
    ay "My heart skips a beat every time you look at me and say something like that."
    ay "So hearing it will probably always make me gasp."

    scene nevermind3
    with dissolve

    ay "I hope that’s okay."
    s "It’s fine."
    s "Now, tell me what this is really all about."
    ay "Aww, come on. Can’t I use stall tactics a little more before we start getting to the serious stuff?"
    s "Nope. I {s}flew{/s} walked all the way here for you and I expect there to be some actual substance tonight."

    scene nevermind8
    with dissolve

    ay "Even if it’s something you really don’t want to hear?"

    if bonus == True:
        s "If you pull the pregnancy trick on me again, I swear-"
        ay "Are you really that afraid of becoming a daddy?"
    else:
        s "If this is about bone necklaces, I swear-"
        ay "It is not, but would it really be bad if-"

    s "Yes. Now tell me what this is really about."
    ay "..."
    s "..."

    "I want to say something about how the wind assaults us on the rooftop-"
    "But it feels as if we’re already in space."
    "There is no wind anywhere. "
    "There is no sound anywhere."
    "There is nothing."

    ay "Can I have a hug?"
    s "..."
    s "You made me walk all the way over here for a hug?"
    ay "Do you have any idea how much I love your hugs?"
    s "Ugh, fine. Come here."

    scene nevermind9
    with dissolve

    ay "Heheh~ Yes, [ayanemaster]."

    scene black
    with dissolve2

    "I’ve noticed something about Ayane over the time we’ve spent together in this strange excuse for a world."
    "Nearly every time she wraps her arms around me, there’s always an extravagant build-up first."
    "Kind of like a dog who is obedient enough to stay off of the couch until invited onto it-"
    "But once it is, it leaps nearly ten feet in the air and crashes into the cushions with more vigor than a male rabbit during mating season."
    "I guess dogs can’t exactly jump ten feet, though."
    "That sounds more like a demon."
    "Either way, there’s no vigor at all in tonight’s embrace."
    "It’s more like wrapping my arms around a dying family pet that I’ll never get to hold again."
    "Its legs are shaking as it struggles to even stand up."
    "They snap- and all of the weight is forced onto me."
    "Everything always comes back to me."
    "I can’t stretch my arms around all of it."
    "........."
    "......"
    "..."

    scene nevermind10
    with dissolve

    ay "You’re warm."
    s "This is what you missed out on that night we went to the park with Sana."
    ay "That was really hard, you know?"
    ay "If it were up to me, we’d be like this every hour of every day."
    s "That would make it very hard to perform necessary daily functions."

    scene nevermind11
    with dissolve

    if bonus == True:
        ay "But you wouldn’t have to jerk off anymore."
        s "Also true."
        s "I guess there are pros and cons to everything."

    ay "I saw you once, you know."
    s "Saw me what?"

    if bonus == True:
        ay "Jerking off."
        s "What? When?"
        ay "A really long time ago. "
        ay "Ami and I both saw it because we went to your room to see if you’d make us a snack and then...surprise. Penis."
        s "Was that before or after I apparently caught you two kissing one another?"
    else:
        ay "Dancing."
        s "Was that before or after the world destroying robot thing?"

    scene nevermind12
    with dissolve

    ay "That..."
    ay "..."
    ay "That never actually...happened."
    ay "Well, apart from the Christmas party. But I was kinda just scrambling to keep things under wraps there and..."
    s "You made that up?"

    scene nevermind13
    with dissolve

    ay "..."
    ay "Yeah."
    s "Why?"
    ay "..."
    ay "You know..."
    ay "I’ve been getting the feeling lately that you’re kind of just...going along with a lot of stuff."
    ay "Like there’s part of you that’s just not really...there anymore."
    ay "And I’ve heard you joking about your memories in the past, but like...then I started wondering if it really {i}was{/i} a joke."
    ay "What if parts of your memories really {i}were{/i} gone and...weren’t coming back?"
    ay "What would that mean for me?"
    ay "When did the new memories start being recorded?"
    ay "Was it after I’d already fallen in love with you?"
    ay "And if so, how would that make me look?"
    ay "Needy?"
    ay "Desperate?"
    ay "Naive?"

    scene nevermind14
    with dissolve

    ay "So...yeah..."
    ay "I thought that maybe...if I could catch you going along with things that didn’t really happen...I’d know for sure."
    s "Ayane-"
    ay "It’s okay that you’re hiding things from me. I don’t need to know about them."
    ay "I just wanted to know how much of what we have is real and...how much I may have lost."
    s "You haven’t {i}lost{/i} anything."

    if bonus == True:
        s "Everything that’s happened since the moment we became...intimate has been all me."
    else:
        s "Everything that’s happened since the moment we started hugging each other has been not only consensual, but entirely of my own choosing. I regret nothing and you have no reason to believe any of it is not real."

    scene nevermind15
    with dissolve

    ay "Right, but..."
    ay "What about the moments that led us there?"
    ay "All of the...horrible feelings I felt...and all of the good things that came from meeting you and Ami..."
    s "They’ll come back."

    "Maybe."

    ay "And if they don’t?"
    s "If they don’t, they don’t."
    s "There’s nothing we can do about it."
    s "But I’m here now, so just focus on that."
    ay "..."
    s "..."

    scene nevermind16
    with dissolve

    ay "Okay."
    ay "There’s still...a lot more I want to talk about, though."
    ay "Well, I don’t {i}want{/i} to talk about it, but I kind of have to if things are ever going to change."
    s "Why do they have to change?"
    ay "Everything has to change. That’s how the world works."
    s "Change is so exhausting, though..."

    scene nevermind17
    with dissolve

    ay "I know it is...I agree..."
    ay "But...there is one change we kind of...have to acknowledge..."
    s "And what is that?"
    ay "Sensei..."
    ay "You know that Ami is...actually in love with you, right?"
    ay "Like, not just as a [niece]. As a girl."

    if bonus == True:
        s "..."
    else:
        s "Do accountants not count as girls?"

    ay "I...don’t even know why I’m asking. Of course you know. It would be impossible not to."
    ay "But, like...Ami is my best friend."
    ay "And...I also love you..."
    ay "And I’m fine with keeping that hidden from everyone else, but..."
    ay "I kind of...want to at least tell her that it's not really one-sided anymore."
    s "That’s a bad idea, Ayane."
    ay "Why?"
    s "Because Ami would literally kill you."
    ay "She wouldn’t {i}kill{/i} me."
    s "I wouldn’t be so sure of that."

    scene nevermind18
    with dissolve

    ay "I would."
    ay "We might get into little arguments and stuff, but she’s pretty much my sister."
    ay "And since I obviously know everything that’s going on with her, she should probably know everything that’s going on with me as well."
    ay "And that everything is you."
    s "This is a horrible idea, Ayane."
    ay "I’m sure it will be really awkward and confusing at first..."
    ay "But, in the long run, I think this is best for everyone."
    ay "I...don’t know if anything has actually {i}happened{/i} between you and Ami since you’re always so closed off and stuff...but I do know what’s happening on her side of things."
    ay "She’s getting very anxious and nervous with all of these new girls showing up. "
    ay "And I’m sure that the two of us getting closer every day doesn’t help that at all."

    if bonus == True:
        s "And you think her knowing that I’m fucking her best friend will?"

        scene nevermind19
        with dissolve

        ay "That’s not the part that’s important, Sensei. The important part is that our feelings for each other are specifically {i}more{/i} than just sex."
        ay "That’s what Ami’s afraid of- you leaving her."
        ay "It’s the same exact fear that I have."
        ay "Just...my fear has been getting a lot stronger lately."
        s "Because of Ami?"

        scene nevermind10
        with dissolve

        ay "..."
        ay "Because of a few things."
    else:
        s "She is just an accountant. Stop being dramatic."

    scene black
    with dissolve2

    "We break apart."
    "Not emotionally, but physically."
    "Emotionally, it’s hard to say if a strong enough bond has ever formed on my end at all."
    "Let’s, in typical “me” fashion, turn this into a strange anecdotal metaphor."
    "I am a half-finished statue based on the outer layer of a real human being."
    "The process of turning me into stone is my relationship with Ayane."
    "I am poised and ready for my body to be covered in a thick coat of cement."
    "But the artists have only made it up to my knees before running out of whatever cement is made of."
    "Is cement even made of anything?"
    "Is it just cement?"
    "I don’t know."
    "I once again distract myself from anything but the topic at hand because I am afraid of thinking."
    "I am afraid of all things."
    "I am afraid of nothing."
    "I grow wings and fly away."

    scene nevermind2
    with dissolve2

    ay "So...umm...remember how I said I might need some more attention soon?"
    s "Does this meeting not qualify as that? Because you’re already kind of acting out of the ordinary here."
    ay "No. I’m talking about the...you leaving me thing."
    s "If you’re really intending to break the silence of our relationship to Ami, we should worry more about you leaving {i}me{/i}."
    ay "The things I mentioned don’t all involve Ami, Sensei."
    s "Well, can we at least fully address that part first? Because I still don’t like the idea of you coming out about this."

    scene nevermind8
    with dissolve

    ay "Because you’re embarrassed of me?"
    s "What? No."
    ay "Because you don’t want to hurt Ami’s feelings?"
    s "That’s closer, but still...no."
    ay "Because you’re worried she’ll tell other people?"
    s "Ayane-"
    ay "Because you’re worried she’ll tell Maya?"
    s "What would Maya have to do with this?"
    ay "Remember the other day when I asked you about who you’d choose if all twenty of us were lined up in class and you were forced to pick one?"
    s "I remember it being a flawed hypothetical scenario based on several of the students’ attendance, but yes."
    ay "If that were true, and all of us really {i}were{/i} in the same room, I think your choice might actually surprise you."
    ay "That’s all I’m saying."
    s "You think I’d choose Maya in that situation?"
    ay "I just think you look a little differently at her than you do anyone else."
    ay "I don’t know what it means, but I’d be lying if I said it doesn’t bother me."
    s "And that’s another one of your worries?"
    ay "That’s another one of my worries."
    ay "I have a lot all of a sudden."
    ay "I’m even here actually talking to you about my feelings for once because I’m so overwhelmed right now that I think I might explode."
    s "You should have come to my house tonight."

    scene nevermind6
    with dissolve

    ay "I should have come to your house tonight."
    ay "I don’t belong up here."
    ay "I belong with everyone else...being loud and overly-expressive about the things I love most."

    scene nevermind2
    with dissolve

    ay "But, most of all...with you."
    ay "If the world really {i}was{/i} ending tonight, I’d be scared. But, in a way, I’d kind of also be a little happy."
    ay "Maybe the world ending would just mean that it starts all over again?"
    ay "A fresh start doesn't sound bad, does it?"
    ay "You'd have some of your memories back."
    ay "I'd have both of my parents."
    ay "And then one day, I’d bump into Ami and meet you."
    ay "And I’d fall in love all over again."

    scene nevermind5
    with dissolve

    if bonus == True:
        ay "And then I’d catch you jerking off again."
    else:
        ay "And then you would finally make a bone necklace with me."

    s "Why does that part have to come up now in the middle of a big, emotional moment?"

    scene nevermind2
    with dissolve

    ay "Neither of us are good at big, emotional moments."
    ay "Maybe I learned it from you, but I think it’s easier to just move onto things that aren’t painful to talk about most of the time."
    ay "Tonight is just...a special exception."
    s "I just want to know if there’s anything that can be done to make you-"

    scene nevermind3
    with dissolve

    ay "Ayane again?"
    s "..."
    s "Yeah."
    ay "I see, I see."
    ay "All you really have to do is love me."
    s "I can do that much."
    ay "And let me share those feelings with anyone that I think it’s safe to share them with."
    s "That one’s a little further off, but I could probably be swayed with a few more conversations."
    ay "And accept that sometimes, there will be parts of me you wish didn’t exist."
    s "Fine. Whatever."
    ay "And that sometimes, those parts might be hard to say out loud...so I’ll be forced to drop hint after hint after hint, hoping that you manage to understand what I’m trying to tell you."
    s "I get it. Yeah."
    ay "Do you, though?"
    s "Of course I do."
    ay "..."
    ay "{i}Do you, though?{/i}"
    s "Ayane...come on."

    scene nevermind9
    with dissolve

    ay "Heheheh~ "
    ay "It’s fine. It’s fine."
    ay "I kind of expected things to play out like this anyway."
    ay "It’s actually a pretty amazing quality being able to just effortlessly ignore the things you don’t want to acknowledge or hear."
    ay "I always have so much trouble with that."
    ay "Maybe one day, far off in the future, you can teach me how to be as intentionally dense as you."
    s "Are we done talking about serious stuff and just moving onto “insult Sensei time?”"
    ay "Is {i}that{/i} what time it is?"
    s "If you call it teacher time again, I’m leaving."
    ay "Already? But teacher time isn’t over yet."

    scene black
    with dissolve

    s "Okay. Goodnight, Ayane."

    "Sensing that things are going to end here within a matter of moments, I turn around and-"

    ay "Wait!"

    scene nevermind20
    with dissolve2

    s "What is it?"
    ay "I don’t want you to leave yet."
    s "Then come back with me."

    scene nevermind21
    with dissolve

    ay "I...don’t want to do that either."
    ay "I mean, I do..."
    ay "But if I come back to your house, I’ll wind up telling Ami about us...and you asked for at least a few more conversations to be persuaded."
    s "I can’t just spend the entire night here, though."
    s "There are other people waiting for me."

    scene nevermind22
    with dissolve

    ay "There are always other people waiting for you..."
    ay "And I’m okay with that. That’s just...the effect you have, I guess."
    ay "It happened to me so...of course it would happen to everyone else."
    ay "But right now, I...really need you to listen to me."
    ay "Sensei.."
    ay "Something..."
    ay "Something happened and..."
    ay "And it's something I really need your help with and..."
    s "..."
    ay "..."
    s "..."
    ay "..."
    s "I’m listening, Ayane."
    s "Whatever it is, I’m sure it won’t change anything between us."
    s "So, if that’s what you’re worried about-"

    scene nevermind23
    with dissolve

    ay "Nevermind."
    s "...What?"
    ay "Nevermind."
    ay "Don’t worry about it."
    ay "I can tell you some other time."
    s "Just tell me now. If there’s more to the reason you called me out here-"

    scene nevermind24
    with dissolve

    ay "I just wanted to look at the sky with you."
    ay "That’s all."
    ay "I’ll stop telling everyone I’m not feeling well for real this time."
    ay "And I’ll...keep doing my best."
    ay "Just...try to be there for me if I need you..."

    scene nevermind25
    with dissolve2

    ay "Okay?"
    s "..."
    ay "I love you..."
    ay "So...so much..."
    s "..."
    s "Ayane-"
    ay "I’ll head home in a little while. I promise."
    ay "I just want to be alone for a few minutes."
    s "..."
    s "Okay."
    s "I love you too."

    scene black
    with dissolve2

    "My wings retreat back into my flesh and I’m forced to walk down several flights of stairs with the image of a crying blonde girl etched into my mind."
    "I don’t know what it is Ayane was about to tell me at the end..."
    "But I’m sure that it will come up again in due time."
    "Either that or I’m just once again being “intentionally dense” or whatever it is she called me."
    "That doesn’t sound too far off."
    "I hope she’s okay, though."
    "I really do."
    "Just not enough to drop everything and be with her regardless of her plea for privacy."
    "Perhaps one day I’ll get there."
    "But for now-"

    s "..."

    "I slide my hands into my pockets for the millionth time and go back home."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanespecial1 = True
    stop music fadeout 10.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump thirdreset1

label ayanespecial2:
    scene postrthree1
    with dissolve

    s "Huh?"
    m "..."
    s "Where did Ayane go?"
    m "..."
    m "If I had to take a guess-"
    m "I’d assume she was sent back to the beginning."

    scene postrthree2
    with dissolve

    s "The beginning of what?"
    m "Everything, obviously."
    m "That her mind was “factory restored” the same way it is every time you swap places with another “you.”"
    m "Then again, that’s just an assumption."
    m "I figure it’s equally probable that she’s just asleep in her dorm room right now- entirely unaware of everything that transpired tonight."
    s "And you’re just okay with that?"
    m "Of course."
    m "It’s part of the cycle."
    m "Even if I weren’t “okay with it,” there’s nothing I’d be able to do."
    m "Everyone stopped being real to me a long time ago."
    m "They’re more like puppets with...invisible hands or something inside of them now."
    m "I imagine it’s hard to understand given that you’ve only gone through this three times."
    s "Well...we need to go check on her then, right?"
    m "Is that what you want to do?"
    m "Or would you rather go home and collapse into bed?"
    s "You should be more worried about this."

    scene postrthree3
    with fade

    m "Perhaps I should."
    m "But have you begun to take into consideration exactly {i}why{/i} Ayane may have made it to the roof tonight?"

    if bonus == True:
        s "I was sort of hoping you would be able to tell me."
        m "It could be a number of things."
        m "But the reason that’s sticking out in my mind the most is so vile that I have an issue with even coming out and saying it."
        s "What does that-"
        m "It means that you’re disgusting."
        m "Do you understand?"
        s "That I’m disgusting?"
        m "Yes."
        s "Well...you certainly remind me enough."
        m "Good. "
        m "Can you maybe try to be {i}less{/i} disgusting in the future then?"
        m "Not only for your sake- but for my sake and the sake of everyone else unfortunate enough to become involved with you in any manner other than student and teacher."
        s "What happened to the Maya from like, an hour ago? The one who laid out a picnic for me?"
    else:
        s "..."
        m "..."
        s "Oh no. It was the hug."
        m "Can you maybe try to be {i}less{/i} disgusting in the future?"
        m "Not only for your sake- but for my sake and the sake of everyone else unfortunate enough to become involved with you in any manner other than student and teacher."
        s "What happened to the Maya from like, an hour ago? The one who laid out a picnic for me?"

    scene postrthree4
    with dissolve

    m "Gone with the reset, I suppose."
    m "Also, your blanket is gone."
    m "Sorry."
    s "..."
    m "..."
    m "Well, I guess we better head back to the dorm."
    m "It’s not like I really have anywhere else to go anyway."
    s "Maya, if Ayane really {i}is{/i} gone-"

    scene postrthree3
    with dissolve

    m "You and I will be the only ones to know."
    m "To everyone else, she’ll be exactly the same as she’s always been."
    m "And any memories that overlap in confusing ways will be rewritten or recontextualized in her mind to make perfect sense to everyone around her."
    m "Do you understand?"
    s "No."
    m "I didn’t think so."

    scene black
    with dissolve

    m "Now, come."
    m "If you’re so curious about her wellbeing, it’s probably best for you to find out firsthand exactly what’s happened."
    s "..."

    "The two of us leave the roof together."
    "As we move through the halls of the[school], I find an assortment of strange items dumped haphazardly onto the stairs and several halls barricaded with boxes."
    "When we make it outside, I notice that the weather has suddenly turned colder than it’s been in quite some time."
    "Maya tightens her scarf and sighs to herself."
    "I slide my hands into my pockets."
    "........."
    "......"
    "..."

    scene postrthree5
    with dissolve2
    play music "undersea.mp3"

    m "You can go on ahead."
    s "You’re not coming with me?"
    m "It’s nearly 3:00 AM. I won’t be as easily forgiven for waking anyone up as you will be."
    s "What are you going to do instead, then? Your room is right across the hall from Ayane's."
    m "It appears that we left in such a hurry that I may have forgotten several things in several places."
    m "If you’re still here by the time I return, which I truly hope you won’t be, I implore you to ignore my presence entirely and let me sleep."
    m "I am incredibly tired and depressingly frustrated."
    s "That sounds like more or less how you always are."
    m "It does, doesn’t it?"
    m "Anyway, goodbye."

    scene postrthree6
    with dissolve

    "Maya blows right by me as if we hadn’t just lost a close friend and restarted the world together."
    "I guess it’s possible that she’s just one of those people who internalizes her problems and-"

    s "..."

    "What am I doing?"
    "I need to go upstairs..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene postrthree7
    with dissolve

    "I make it to the room despite a pit in my stomach, which I imagine has already begun to sprout roots and transform into a tree, beckoning me to return home instead."
    "I stand there for what must be a total of five minutes, hoping to hear something- anything on the opposite end."
    "Of course, it’s the middle of the night right now. And even if Ayane were in there, I doubt she’d be conscious enough to make any noise."

    s "..."

    play sound "knock.mp3"

    "I knock on the door, hoping that if anyone {i}does{/i} wake up, it’s a resident of this dorm room."
    "I might be incredibly popular with all of the girls on this floor (Save Yumi), but even I can’t imagine having an easy time explaining to them exactly why I’m-"

    play sound "dooropen.mp3"
    scene postrthree8
    with dissolve

    sa "{i}Uaaaahhh~{/i}"

    scene postrthree9
    with dissolve

    sa "Sensei?..."
    sa "What are you...doing here?..."
    s "Hey, Sana. Sorry to wake you up."
    sa "It’s okay..."
    sa "Did you...need something?"
    s "Yes, actually."
    s "I was just wondering if Ayane was around."
    s "Do you think you could wake her up for me?"
    sa "Ayane?..."
    s "Yeah. I just wanted to make sure she’s okay."
    sa "Sensei..."

    play sound "static.mp3"
    scene postrthree10 with flash
    stop music
    stop sound

    sa "Who is Ayane?..."
    s "...What?"

    "It’s...not possible that she just...disappeared completely, is it?"
    "No."
    "No, that can’t be right."
    "Maya didn’t even factor that into any of the possibilities that-"

    ay "Sensei?..."
    ay "What are you doing over here this late?"

    play sound "static.mp3"
    scene postrthree11 with flash
    stop sound
    play music "lastdailysong.mp3"

    s "..."

    "If I believed in God, I’d thank him right now."

    s "What are {i}you{/i} doing here this late?"
    ay "I live here."
    s "Yes, but why are you walking around at 3:00 AM? Shouldn’t you be asleep?"

    scene postrthree12
    with dissolve

    ay "Sleep is for the weak!"
    ay "3:00 AM is the perfect time for a late night trip to the convenience store when you’re just too strong to sleep!"

    scene postrthree13
    with dissolve

    sa "Nguh..."
    ay "Sensei...you didn’t...wake up Sana just to check on me, did you?"
    s "The ideal scenario would have been you answering the door, but yes. It appears that I did wake up Sana to check on you."

    scene postrthree14
    with dissolve

    ay "And I’m guessing this is the first time you’ve ever seen her immediately after waking up in the middle of the night."
    s "Uhh, yes. That is not a thing I have really had the chance to do before."
    ay "Well...she can be a little...delusional when that happens."
    s "She didn’t even remember who you were."
    ay "If anything, I’m surprised she {i}did{/i} remember you."
    sa "Sleep...now..."

    scene postrthree15
    with dissolve

    ay "Yes, Sana. Sleep now."
    ay "Let’s get you inside..."

    scene black
    with dissolve2

    "Ayane gently guides Sana back into the bedroom, leaving her standing in the middle of the floor before sliding off her boots and her skirt."
    "I notice a small puddle beginning to form near the door as a result of residual snow meeting its demise at the hand of a heated room."
    "She returns to Sana and strokes her hair for a moment before leading her to the bed."

    if bonus == True:
        "If Sana wasn’t mostly unconscious at the moment, it would probably look as if the two of them were getting ready to do something interesting."
        "Something that, for some reason, isn’t having the same effect on me that a lesbian fantasy typically would."

    ay "Sensei, come sit with me for a little while."
    s "..."

    scene postrthree16
    with dissolve2

    "I take a seat beside Ayane and notice, even in this unlit room, two swollen, reddish circles surrounding her eyes. "
    "If I ask her now what caused them, she’ll deflect."
    "The same way she does every time I ask her anything."
    "Even when we were on the roof, when she was doing everything she could to pour a tiny bit of her heart out-"

    s "The roof..."
    ay "The roof?"
    ay "What roof?"
    s "Ayane, where were you tonight?"
    ay "What are you talking about? I was with you, remember?"
    ay "I was being weird and kept trying to talk about stuff that...didn’t really come out the way I wanted it to."
    s "And where was Sana? "
    ay "Wasn’t she just here?"
    s "No, she was at my house."

    scene postrthree17
    with dissolve

    ay "Sana was?"
    s "And Ami. And Molly. And Tsuneyo."
    s "There was a sleepover that you were supposed to come to, but you decided against it because you wanted to talk to me instead."
    ay "Why would I ever turn down a sleepover? I love sleepovers."
    ay "Couldn’t I have just talked to you-"

    scene postrthree18
    with dissolve

    ay "Actually...I probably couldn’t have talked to you at your house since there was all that stuff about Ami."
    ay "But...I don’t remember anything about a sleepover."
    ay "And I can’t really figure out why Sana would be here if there actually {i}was{/i} one."
    s "..."

    "So-"
    "It looks like Ayane hasn’t been completely “factory restored.”"
    "But...I’m not understanding why it’s suddenly as if the last day has just been entirely rewritten."
    "And it’s not like I can even ask Maya about it since she is mad at me for yet another reason beyond my comprehension."
    "But where do Ayane’s memories end?"
    "Why can she recollect her first trip to the roof, but not her second? And-"
    "Wait, didn’t she say “What roof?”"

    s "Ayane, where did we meet up tonight?"

    scene postrthree19
    with dissolve

    ay "Sensei...is everything okay? You’re acting really weird..."
    s "Just tell me where we met tonight."
    ay "We met at the same park we went to with Sana the other day."
    ay "And we talked about Ami and...and your memories and..."
    ay "Is this...another example of that?"
    ay "Are you...misremembering, maybe?"
    ay "I didn’t realize it was this bad..."

    "I’m not the one misremembering anything this time."
    "It’s you."
    "You’re the one who forgot."

    s "We met on the roof of the[school]."
    ay "I don’t even have a key to the roof of the[school]..."
    s "That’s-"

    "Wait..."
    "Yeah."
    "How did we meet there anyway?"

    s "This next part might make me sound a little crazy, but I need you to listen closely and answer as honestly as possible."
    ay "Sure...yeah. Anything for you."
    s "By any chance, do you remember {i}anything{/i} about going to the roof with Maya tonight? And...resetting the world and...anything like that?"

    scene postrthree20
    with dissolve

    ay "..."
    s "..."

    "We let the silence overtake us for a moment."
    "It’s hard to tell if Ayane is genuinely trying to remember or just...trying to figure out if I need immediate medical attention, but..."
    "Whatever the cause for the silence is-"
    "I hate it."

    ay "I don’t remember anything like that..."
    ay "All I remember is that I called you to meet up...and then we did...and then I went home."
    s "But..."
    s "But that doesn’t explain why you were walking around at 3:00 AM with dark, red circles around your eyes."
    s "And I don’t buy that whole “sleep is for the weak” thing. "
    s "What else happened?"

    scene postrthree21
    with dissolve

    ay "What else?..."
    ay "I guess it’s my turn to sound a little crazy then, huh?..."
    ay "The truth is...I tried to sleep, but..."
    ay "But I had this really weird dream."
    ay "A dream that I...can’t quite remember anymore."
    ay "And...when I woke up..."
    ay "I felt like I’d lost something."

    scene postrthree22
    with dissolve

    ay "Something really, really important to me and...and I couldn’t even put my finger on what it was."
    ay "Which made me kind of hate myself a little bit."
    ay "Like there was some really big thing that was just...stripped from my mind as if it never even existed..."
    ay "If it was so important, how come I forgot it so easily?"
    ay "None of it made sense..."
    ay "And...I didn’t want to call you about it since I already bothered you enough tonight..."
    ay "But...the fact that you’re back before the sun comes up kinda shows me that...maybe I didn’t bother you as much as I thought I did..."

    scene postrthree23
    with dissolve

    ay "Do you think this is what I was talking about when I told you I’d need a little more attention soon?"
    s "I have no idea."
    ay "Yeah...and it's kind of funny cause, like..."
    ay "Neither do I..."
    ay "I’m...really confused all of a sudden..."
    ay "My stomach kind of hurts a little too..."
    ay "Is this anxiety? Do I have anxiety now?"
    s "I highly doubt it. You probably just need to get some rest."
    ay "How am I supposed to rest when you came all the way here to see me, though? "
    ay "It wouldn’t be right for me to just kick you out when you're this worried."
    s "Ayane-"

    scene postrthree24
    with dissolve

    if bonus == True:
        ay "Do you wanna at least have sex first? "
    else:
        ay "Do you wanna at least hug first? "

    ay "I’d feel a little better about going to sleep if I gave you a little reminder to take with you when you go."
    s "Sana is literally asleep on your lap right now."

    if bonus == False:
        s "The hug would disturb her."

    ay "She won’t wake up. It’ll be fine."
    s "She woke up after one knock on the door. It won’t be fine."

    if bonus == True:
        s "Besides, I can’t touch you while you’re crying anyway. That’s one of the rules on my...incredibly short list of them."

    scene postrthree25
    with dissolve

    if bonus == True:
        ay "Okay, okay. We won’t have sex."
        ay "But I owe you at least one blowjob in the future as payment for coming to make sure I was okay tonight."
        ay "I still don’t really know what it is that made me cry like this, but I’m sure it’ll be okay soon enough."
    else:
        ay "Okay, okay. No hugs, then."

    ay "I probably just need some sleep like you said."
    s "Then...I guess I’ll go home, then."

    scene postrthree26
    with dissolve

    ay "Are you sure you don’t want to sleep here?"
    ay "My bed is huge. All three of us could fit if we snuggled a little bit."
    s "Maybe some other night. I’m kind of curious about whether anyone else from the apparent “made up slumber party” is still at my house or not."
    ay "Well, if they are, feel free to give me a call. I don’t wanna miss out on the fun even if it’s almost time for[school]."
    s "Oh, shit. School."
    s "I didn’t even realize it was Sunday."
    ay "On the bright side, I doubt you had any tests planned or anything like that."
    s "Jokes on you, Ayane. Tomorrow is the day I’m going to become a real teacher."
    s "Well, {i}today{/i} technically, I guess."
    ay "Whatever you decide to do, I'll support it."
    ay "I love you, Sensei. And thank you for coming to see me again tonight."
    ay "I feel a lot better now..."

    scene black
    with dissolve2

    "I leave shortly after that."
    "I don’t understand anything at all."
    "What happened this weekend?"
    "Why did Ayane show up to the roof? And why did she immediately forget it?"
    "This isn’t even resetting. "
    "It’s rewriting things that {i}did{/i} happen with things that didn’t."
    "If they even...did happen?"
    "I don’t know anymore."
    "Not that I ever did, but-"
    "..."
    "But at least I’m still here."
    "And I guess that’s really the most important thing of all right now."
    "..."
    "Huh."
    "I feel like I may have lost something too."

    $ renpy.end_replay()
    $ ayanespecial2 = True
    $ ayane_love += 5
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if ami_lust >= 15:
        $ totaldays += 1
        $ day -= 6
        if day == 1:
            hide sunday onlayer date
            show monday onlayer date
        jump amilust15
    else:
        $ amilust15skip = True
        jump advancetomon

label ayanelust20:
    scene ayaneofficebang1
    with dissolve2
    play music "asobeatsex4.mp3"

    "Ayane and I retreat to my office because, well, where else would we go during school hours?"

    if bonus == True:
        "Well...apart from the nurse’s office, which we've already made out in once before."
        "But- wait, isn’t the nurse absent on Fridays? We really could have just gone there after all."
        "Assuming that there is going to be sex, of course. For all I know, this really {i}could{/i} just be about giving me a sneak peek of something."
        "But when Ayane and I are alone, the chances are that one of us is probably going to want to get a little closer."
        "And by {i}one{/i} of us, I really mean {i}both{/i} of us."
        "We are very...horny people."
        "Destructively horny, if you will."

        if ayanelust10 == True:
            "But I probably don’t have to remind you of that on account of the entire Kirin situation."

    ay "Are you ready to have your mind blown, Sensei?"

    if bonus == True:
        jump ayanelust20x
    else:
        s "Yes, but please be gentle."

        scene black
        with dissolve2

        "Ayane spends the next ten minutes showing me the mech suit she has been working on, which she will soon reveal to the class before beginning her quest for world domination."
        "Unfortunately, the mech suit falls apart shortly after she gets inside because it was held together tomato paste."
        "This will teach her not to use cooking ingredients on heavy machinery in the future."
        "Ayane cries a lot, which makes me cry too."
        "Eventually, we stop crying and hug each other. Then we leave."

        $ renpy.end_replay()
        $ ayane_lust += 1
        $ ayanelust20 = True
        stop music fadeout 5.0

        "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
        "........."
        "......"
        "..."

        jump christmastwo4

label ayanenew1:
    play sound "phonebeep.wav"

    "I tap on Ayane’s name in my phone and wait for her to answer."
    "I know that it’s relatively early in the morning...and I know that it isn’t really like me to go out of my way to make plans as soon as I wake up..."
    "But I also know that Ayane has verbally confirmed a desire to have sex with me and that I must now do things I would not normally do in order to make that happen."
    "I also had a dream about it, which further justifies the fact that I am now listening to a constant ringing that may or may not determine where my penis ends up today."

    play sound "phonebeep.wav"

    ay "Sensei? "
    s "Good morning."
    ay "Good morning, indeed! Why are you calling me so early? Did something happen?"
    ay "Did Ami fall in a well?"
    s "Yes, and I need your help to get her out."
    ay "Darn it. I was hoping you’d suggest using this as an opportunity to have me replace her as your niece and hope no one notices."
    s "Your hair isn’t even the same color."
    ay "Tell that to the five bottles of red hair dye I just ordered off of Amazon Prime. I can be your new Ami within the hour."
    ay "Seriously, though, what’s up? You never call me. I didn’t even think you’d be awake right now."
    s "I want to see you."

    with hpunch
    play sound "glass.mp3"

    ay "Ah!"
    s "...Everything okay?"
    ay "Yeah, sorry. I just felt the need to throw the glass I was holding across the room after hearing that. In a good way, of course."
    ay "Sorry, Sana!"
    s "..."
    ay "Do you...want to maybe go out for coffee or something? I was actually about to head over to Koi Cafe to study for our standardized tests and stuff."
    s "..."

    "While I want to say “No” or “I’d rather go somewhere less public,” I also understand that things being too easy would take away from the value of the gift I’m soon to be given."
    "And so I will swallow my pride and watch a rich girl study for the morning instead of enacting some of last night’s lingering fantasies both with and to and on her."

    ay "Sensei? Are you still there? "
    s "Yeah. Just thinking."
    ay "About me?"
    s "There’s a more complicated answer to that question, but the short version is “yes.”"
    ay "Great! I guess I’ll start heading over then. See you soon, future husband!"
    s "Ayane, I’m not-"

    play sound "phonebeep.wav"

    s "...your future husband."

    scene black
    with dissolve2

    "Well, looks like deflowering my niece’s best friend will have to wait until she is more confident about standardized tests or...something like that."
    "I guess it wouldn’t hurt to at least pretend to be a teacher every once in a while, though."
    "I just hope Ayane doesn’t wind up actually needing me to {i}teach{/i}, though, since it’s still way too early in the morning to be bothered with that."
    "I will be a teacher in name and appearance only."
    "At all other times-"
    "I will be the worst man I can be."
    "........."
    "......"
    "..."

    scene ayanecafe1
    with dissolve2
    play music "cafe.mp3"

    "I show up to the cafe to find Ayane already studying at the counter and, apparently, she also took the liberty of ordering for me based on years of secondhand experience in what I like."
    "Or at least what I would like if I was actually the person she wants me to be."
    "All things considered, though, her choices are fine and I don’t mind them at all. "
    "I don’t consider myself a very picky eater, though, so chances are I would have been fine with literally anything she chose."

    ay "So, what brought this on? And don’t tell me it was Ami actually falling into a well because she just sent me a picture of her and Maya at the mall. "
    ay "Unless the well is in the mall. Or leads to the mall. Or-"
    s "Aren’t you supposed to be studying?"
    ay "Aren’t you supposed to be loving me?"
    s "I don’t think that’s in my job description."
    ay "Really, though...should I be taking this as a sign of good things to come? Or is it more of a sign that you just didn’t have anything else to do and I was the second name in your phone after Ami?"
    s "I’d probably say it's closer to a sign of things to come, I just don’t know if any of them would be considered “good.”"
    ay "Ominous. That makes it sound like you’re either here to kill me or to ask me to kill someone else."
    s "I’m just here to hang out with you and maybe look like a teacher in the process."
    s "Besides, I come to this place in the morning all the time. It’s not like this is some crazy, unheard of event or something like that."

    scene ayanecafe2
    with dissolve

    ay "You come {i}here?{/i} Isn’t this a little far from your house for a morning coffee routine?"
    s "It’s not {i}that{/i} far. And Rin works here, so I normally get to talk to her as well."

    scene ayanecafe3
    with dissolve

    ay "Hmm..."
    s "What?"
    ay "Oh, nothing. "
    ay "I just would have chosen a different place to meet up if I knew the {i}real{/i} object of your affection was currently behind the counter making cappuccinos for old ladies."
    s "Ayane-"

    scene ayanecafe4
    with dissolve

    ay "I’m obviously kidding, Sensei. I know better than anyone how important the bond you and I share is. "

    scene ayanecafe5
    with dissolve

    ay "And I’m not going to worry too much about Rin stealing you away from me when, in all actuality, she’d probably try to steal {i}me{/i} away from {i}you{/i} first."
    s "No one is stealing anyone from anyone because no one here belongs to anyone else."

    scene ayanecafe6
    with dissolve

    ay "False!"
    ay "My body and mind belong to you and you only, Sensei. And you are free to do with them as you please so long as the first time is special."

    scene ayanecafe7
    with dissolve

    ay "But I guess yelling about the future of our relationship in a crowded cafe isn’t really the brightest or most secretive idea and you seem to be in teacher-mode today."
    ay "So, if you wouldn’t mind helping me with-"
    q "Blackest of night...darkest of day...hear and feel the magic that courses through these veins..."

    scene ayanecafe8
    with dissolve

    q "What is thy wish, children of the nameless? Nectar of the gods? A draught of unspeakable potency? Or perhaps...{i}a lemon poppy seed muffin.{/i}"
    s "..."
    q "..."
    ay "One draught of unspeakable potency, please."

    scene ayanecafe9
    with fade

    q "Understood. Now, if you’d please hold out your palms for me to collect but the smallest portion of blood...I can begin the alchemical process."
    s "Should we call 911?"
    ay "That won’t do anything, Sensei. We need to call 119 in Japan."
    ay "Besides, that’s just how Molly speaks. She’s in one of the other classes at our school."

    scene ayanecafe10
    with dissolve

    mo "You have entered the realm of none other but the Gem of the Emerald Isle and yet you sit before her with nothing but half-iced doughnuts and a {i}coffee noir.{/i}"
    mo "Do you quiver with anticipation, Sir?"
    s "Anticipation for what?"
    mo "The Molly route! This is simply a cameo to hold you over while you grind your stats, for I do not appear until later in the game."
    s "Right. Do you actually work here? Or did you just steal that uniform from someone?"
    mo "I can guarantee I work here, Sir."

    scene ayanecafe11
    with dissolve

    mo "Now, please order something from me. It is my first day and I need to keep this job or my gacha addiction is sure to drain me entirely."
    s "I’m good, thanks. "
    mo "Fair enough. I suppose I will just have to compose the draught for your female party member, then."

    scene ayanecafe12
    with fade

    ay "What’s in the thing I ordered anyway? I didn’t see that on the menu here."
    mo "It is a mixture of every single syrup and milk we have, packed into one extremely potent beverage. "

    "I’m just going to assume that Rin is the one who’s been training her."

    ay "Sounds good...ish!"
    mo "It might be. I have no idea. I’ve only had a job for three hours and haven't tried anything yet."
    mo "Anyway, adieu! Until the sun no longer sets above us..."

    scene ayanecafe13
    with dissolve

    ay "Until the...but where else would it even set?"
    s "I obviously don’t know that girl very well, but I think it would probably be best if we just ignored everything she ever says from this point on."

    scene ayanecafe14
    with dissolve

    ay "Deal! That gives me more time to focus on what’s really important to me anyway."
    ay "So, where was I?..."

    scene ayanecafe15
    with dissolve

    ay "Oh! Right, so...it would probably make the most sense to have you help with language arts stuff since that’s what you’ve always liked the most."
    ay "Not to mention that you seem to be getting a little burnt out on teaching in general given that your new primary objective is being everyone’s friend instead."
    s "I prefer less “friend” and more “mysterious, cool older guy.”"
    ay "You can be the mysterious, cool older guy and still teach, Sensei. Come to think of it, that’s pretty much what you’ve always done since you used to be a tutor and stuff."
    ay "At least that’s what Ami says. I was never fortunate enough to have you actually tutor me back then."
    ay "And sure, you’ve helped me with homework a few times, but that was mostly me pretending to not know stuff so I could sit really close to you."
    s "Have you really always been this crazy?"

    scene ayanecafe16
    with dissolve

    ay "Not {i}always.{/i} Just since I learned about the wonders of boys and imprinted on one."

    "That’s probably a good way to put it...albeit with a few caveats."
    "From what I understand, imprinting doesn’t typically happen this late into life, but I’m not about to argue the science of how badly Ayane wants my penis inside of her."
    "I am simply here to pretend that I am a teacher."
    "And all of the strange compulsions I’m feeling to actually help right now are not actually real."
    "None of this is real."
    "This is a new world filled with new and pretty things."
    "Things for me. Things-"

    scene ayanecafe17
    with dissolve

    ay "Hey! Here’s an idea! How about we relive the old days a little and I pretend to not know stuff {i}again{/i} and just gaze lovingly into your eyes until we get kicked out of here?"
    s "I’m beginning to think that’s exactly what you’ve been doing this entire time and that you didn’t need to study at all."
    ay "..."
    s "..."

    scene ayanecafe18
    with dissolve

    ay "Okay, so...it’s {i}possible{/i} that the original plan was to come here with Sana so I could help {i}her{/i} study."
    ay "Which means it’s also possible that I asked her to stay behind so I could meet up with you instead."
    s "Which means it’s also possible that Sana flunks out of school and it’s all your fault for abandoning her in her time of need."

    scene ayanecafe19
    with dissolve

    ay "What?! No! It has to be at least a {i}little{/i} bit your fault, since-"

    scene ayanecafe20
    with dissolve

    ay "Oh! Oh, I get it. You need {i}me{/i} to take the fall so you can keep your job."
    s "I mean...that would be great. But that was also kind of a joke, so..."

    scene ayanecafe21
    with dissolve

    ay "No...No, I know what I must do. And if you need both Sana and me to get kicked out of school in order for me to prove my love, I’ll do it."
    ay "But if Ami ever makes it back from the well, you need to tell her that I am your new niece and that she is no longer needed since she never got kicked out of school for you."
    s "The metrics you use to define your love are getting progressively stranger every day."
    ay "And we’re still in the very beginning. Imagine how things will look ten years from now when we have fifteen children."
    s "That would be-"
    ay "Highly improbable as it would take 135 months to go through 15 pregnancies- and that’s with zero downtime between popping them out."


    scene ayanecafe14
    with dissolve

    ay "But if I’m able to have more than one at once, we’ve got a chance! Believe in me, Sensei!"
    s "This might sound selfish, but I’m a lot more worried about how {i}I’d{/i} fare in that situation."
    ay "Then...believe in the me that believes in you!"
    s "..."
    ay "Or just believe in me! I’ll figure it out!"
    s "..."
    ay "..."

    scene ayanecafe21
    with dissolve

    ay "You know, I could really go for a draught of unspeakable potency right now..."

    scene black
    with dissolve2

    "Sensing that Ayane doesn’t need to study at all, the two of us wind up eating breakfast and drinking coffee until the sun starts to set."
    "She leaves the cafe with her virginity still intact-"
    "And I leave the cafe with a lemon poppy seed muffin."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanenew1 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label ayanenew2:
    scene ayanenewtwo1
    with fade
    play music "sakuya4.mp3"

    ay "Ahh! Seven losses in a row. I swear Miss Osaka, it’s like you’ve been doing this for your entire life or something."
    kin "I mean...yeah. If you were able to beat me at all, I’d probably just hang it up and open a flower shop or something."
    s "I somehow have a hard time picturing that."

    scene ayanenewtwo2
    with dissolve

    kin "Good. Keep me as far away from your fantasies as possible."

    "The three of us are relaxing in the dojo after a mildly eventful training session in which Ayane and I both gave it our all."

    kin "Oh, and if you go one more class without doing anything, I’m going to beat your ass without even giving you a warning first."

    "The three of us are relaxing in the dojo after a mildly eventful training session in which Ayane gave it her all."
    "Unfortunately, her all was not even close to enough and now she is extremely exhausted from overexerting herself- meaning her virginity will likely survive at least one more day while she recovers."
    "{i}If{/i} she recovers, that is. Because I’ve had this same exact inner monologue several times today, and each one has ended with another-"

    ay "One more round. I can do it this time. And...I won’t even make you give me a handicap again! That’s how confident I am!"

    scene ayanenewtwo3
    with dissolve

    kin "Fuck no. I’ve already spent pretty much the entire day with you. It’s not fair to the rest of the girls."
    kin "Besides, if I wind up hurting one of the richest girls in the entire city from pushing her too hard, your father will run this place into the ground."
    kin "I can’t afford a legal battle with...whatever the hell your dad’s name is."

    scene ayanenewtwo4
    with dissolve

    ay "Nice try, Miss Osaka. But I’ve already told you that Sensei is my dad."
    kin "That would be a little more believable if you stopped referring to him as “Sensei,” which, honestly, you shouldn’t be doing at all since {i}I{/i} am Sensei while we’re in here."
    s "What would I be called, then?"

    scene ayanenewtwo5
    with dissolve

    kin "Oh, I don’t know. Maybe your fucking {i}name?{/i}"
    ay "Can I ask you something, Miss Osaka?"

    scene ayanenewtwo6
    with dissolve

    kin "For the last time, no. I will not teach your chicken karate."
    ay "While I implore you to reconsider, that’s not what I was going to ask."
    ay "I just want to know why, if you know Sensei isn’t my real dad...you’re letting the two of us continue to show up together."
    kin "I care more about the fact that he does literally nothing here than the fact that he also happens to be your teacher."
    kin "If he even...is your teacher and that’s not just some weird pet name he’s making you refer to him as."
    s "What kind of person do you think I am?"

    scene ayanenewtwo7
    with dissolve

    kin "“Person” is generous. I don’t think you’ve earned the right to call yourself that yet."
    s "Okay, Ayane. It’s time to find a new instructor."
    kin "Good luck. Nobody in this city comes even close to the level I’m at. Which I guess {i}you{/i} don’t care about, but I’m sure Amamiya does."
    ay "To get back on track...he really {i}is{/i} my teacher. But we’ve also known each other for a really long time, so..."

    scene ayanenewtwo8
    with dissolve

    kin "I guess that kind of explains why you two act so “friendly” all the time, then."
    ay "Friendly? I mean...I don’t know if I’d call us {i}friends...{/i}"
    kin "There are definitely other words I’d use in place of that, but saying any of them out loud might make me throw up in my mouth and that would be...unprofessional or something."

    scene ayanenewtwo9
    with dissolve

    kin "To be frank, your entire relationship confuses the shit out of me. It’s just not really my place to get involved when, at least so far, it’s seemed {i}mostly{/i} innocent."
    kin "If Amamiya seemed genuinely creeped out or something, I’d be a lot more concerned. But, if anything, it kind of seems like {i}she’s{/i} the pursuer and not {i}Sensei{/i} over here."

    scene ayanenewtwo10
    with dissolve

    ay "That’s accurate. I’ve been pursuing Sensei for quite some time now as the two of us are destined to be together one day."
    kin "See, this is the kind of shit that I don’t want to hear because {i}now{/i} it’s a hell of a lot weirder."
    ay "The world needs to know."
    kin "Well, don’t lump me in with the rest of the world. I’m here to teach karate, not offer relationship counseling."
    s "Much like the flower shop job, you don’t really seem fit for that either."

    scene ayanenewtwo11
    with dissolve

    kin "Hey! I’ll have you know that I’ve been in a very successful relationship for quite some time now!"
    s "You mean with karate?"
    kin "No! I mean with a live, human being!"
    s "The fact that you had to specify “live” makes me a little wary of this alleged partner of yours."

    scene ayanenewtwo12
    with dissolve

    kin "Okay! Time for {i}your{/i} turn to spar, smartass."
    ay "I don’t think Sensei and I need counseling right now, but I’ll keep you in mind if we ever do, Miss Osaka."

    scene ayanenewtwo13
    with dissolve

    kin "Why? I literally just said that I’m not here to do stuff like that."
    ay "It’s just that you seem really happy most of the time, so I am assuming your relationship must be going pretty strong."

    scene ayanenewtwo14
    with dissolve

    kin "W-Well, it’s...I guess we {i}are{/i} pretty good together...but we’ve also known each other for a really long time and-"

    scene ayanenewtwo15
    with dissolve

    kin "Wait, why am I even talking about this with you two?!"
    ay "Because...we want to hear about your amazing and successful relationship?"
    kin "It’s amazing and successful! There you go! Conversation over!"

    scene ayanenewtwo16
    with dissolve

    kin "Now, pack your stuff and get ready to leave! We’ve only got ten minutes left of class and I still have to make up for all of the time everyone else lost during the seven ass-kickings I gave you."

    "So...the instructor is in a relationship."
    "I can’t say I saw that coming."
    "Which isn’t to say I don’t find her attractive or anything- she certainly has her own brand of...tomboyish charm."
    "She just doesn’t really seem like the type to fawn over someone based on first impressions alone."
    "But if every book on every shelf mirrored its cover, libraries would be a lot less exciting."
    "So I guess it’s good that people like her exist and remind us that not everything is always as it seems."

    ay "Sensei-"

    "Though, of course-"
    "Some things are."

    s "Yes, Ayane?"

    scene ayanenewtwo17
    with fade

    ay "Are you surprised to find out that Miss Osaka is dating somebody?"
    s "Yeah. It ruins my plan of asking her to marry me after beating her in a sparring match."
    ay "Normally, I’d worry after hearing something like that. But after going seven rounds with her today, I can pretty much confirm that there’s no reason to worry at all."
    s "Is she really that tough?"
    ay "Have you ever tried to punch a bird out of the sky before?"
    s "...No?"
    ay "Neither have I, but I imagine it’s kind of like that."
    ay "She’s super fast and pretty much impossible to hit. And when she hits {i}you,{/i} it’s way harder than you expect it to be."

    scene ayanenewtwo18
    with dissolve

    ay "I wonder if that’s what loving her is like as well?"
    s "I’m pretty sure that wasn’t meant to be a sexual innuendo, but I’m going to imagine it as one."
    ay "I mean, I guess that would be part of it. But yeah, I’m talking more along the lines of just...having something that {i}real,{/i} you know?"
    s "..."
    ay "Do you..."

    "Don’t ask it, Ayane."

    ay "Do you think..."
    ay "Do you think that we’ll ever have something like that?"
    s "..."
    ay "..."

    "Of course not."
    "All it would take is one look at us to know that something like that isn’t possible."
    "And, on the off chance it ever would be, it would take us years to get there."
    "Time is not known to be kind to the segmented nature of unblossomed, unrequited love."
    "And so there is no way that this girl and I will ever be happy together."
    "The same goes for everyone else who falls as deep into this hole as her."
    "I am not built for love-"
    "But I was built by someone somewhere."
    "So I will try on new goals as if they are outfits and peer into the glass, hoping that whatever is reflected back at me looks closer to something with purpose."
    "Or, at the very least-"
    "Something not far from fantasy."

    s "Ayane-"

    scene ayanenewtwo19
    with dissolve

    ay "On second thought...don’t answer that, Sensei."
    ay "It was a stupid question."
    s "It wasn’t a stupid question, it-"
    ay "No, it was."
    ay "And honestly, it’s stupid that I asked in the first place since I’ve known from the beginning that we could never have anything like that."
    ay "It’s one of the many unfortunate side effects of falling for someone the world doesn’t want you with."
    s "..."

    scene ayanenewtwo20
    with dissolve

    ay "But...I’m okay with that."
    ay "And sure, we might not ever have something {i}amazing and successful{/i} by everyday standards, but that doesn’t mean it won’t be amazing and successful {i}to us.{/i}"
    ay "Isn’t that what really matters? That we’re happy?"
    s "Do you actually think you’d be happy with me, Ayane?"

    scene ayanenewtwo21
    with dissolve

    ay "Yes."
    s "You didn’t even think-"
    ay "I don’t have to think, Sensei."
    ay "There are some things in life that you just know."
    ay "This is one of those things."

    scene ayanenewtwo22
    with dissolve

    ay "So, you can deny it all you want or think to yourself that there’s no real way for us to be happy, but I know that I’m happier than I’ve ever been just getting to say these things to you."
    ay "And I know that there’s next to nothing you can do to change that, whether you want to or not."

    scene ayanenewtwo23
    with dissolve

    ay "I’m kind of like a disease you’ll have to live with for the rest of your life."
    s "That is a significantly more grotesque note than I expected that mini-monologue to end on."
    ay "Same here, but I really couldn’t think of any other way to put it."
    ay "Things will never be normal between us. And very few people will ever accept it because its face value isn’t covered up by the masks they expect us to wear."
    ay "But one day, the two of us will be standing in front of a mirror together."
    ay "Your hands will either be on my shoulders or my belly {size=-15}assuming that I’m pregnant, which I probably will be-{/size}"
    ay "And what’s reflected back at us will be something with purpose. Something no one thought would ever work out."
    s "Ayane-"
    ay "I’ll make it work, Sensei."
    ay "I promise I’ll make it work."
    s "..."
    ay "..."

    scene black
    with dissolve2

    "I’m not sure how, but Ayane managed to tap into the same worries I had just moments ago when contemplating the unlikely future the two of us may have."
    "And while it would be easy to chalk that strain of hivemind up to the fact that she’s known me for years, I can’t help but feel like there’s a little more to it than that."
    "Love as pure as hers has no right to exist in the world-"
    "But neither do I."
    "And if the fact that I can wake up and step into a world that doesn’t want me is a symbol that things in life may happen without a reason, I have no right to say what can or can’t exist."
    "Not that I ever did in the first place, it’s just-"
    "I’m not built for love."
    "But that doesn’t mean no one else was."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanenew2 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label ayanenew3:
    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene ayanenewthree1
    with dissolve2
    play music "meanttobe.mp3"

    "The day came to an end a long time ago and I still haven’t left."
    "Which, of course, means that Ayane hasn’t left either as staying late with me under the guise of cleaning duty is the type of convenient excuse a girl like her lives for."
    "No cleaning was done today, as you have probably guessed."
    "In fact, not much of anything was done today."
    "Time ticked by and the sun disappeared without much of anything happening at all."
    "And something about the way the light of the moon pierces the window and lands on me erases any chance I have to contemplate how or why that happened."
    "I’m just here."
    "Ayane is here too, but the main thing is that {i}I’m{/i} here."

    s "..."
    ay "..."

    "I’m here."
    "This is my world now."
    "And despite the irrational thoughts that have been crawling through every inch of...whatever section of the brain creates what is {i}supposed{/i} to be rational thought-"
    "Despite that, I am here."
    "Alone, even with the warm body of a young girl beside me."

    ay "It’s beautiful, isn’t it?"
    s "What is?"
    ay "The sky...The moon...All of it."
    ay "There’s something really magical about looking up at the stars on a hot summer night."
    ay "It’s just one of those things that makes your mind and your body go, “Ahh...youth!” "
    ay "You know?"
    s "..."

    "It would be nice to leech such trivial, little thoughts from whatever it is that causes celestial bodies to glow. "
    "It’s something about energy, I’m assuming- which may partially explain the second wind Ayane is feeling all of a sudden."
    "I wonder if this light would have the same effect on me if it were not for the transparent barrier I hide behind."

    ay "Is something going on, Sensei?"
    s "..."
    ay "You’ve been acting off ever since school ended. And I’ve got a feeling that whatever it is runs a little deeper than just exhaustion."
    ay "Do you want to talk about it?"
    s "There’s not really anything {i}to{/i} talk about. I feel the same as always."
    ay "Is that supposed to reassure me? Because it really just makes it sound like you’re putting on some sort of front all the time."
    ay "Like...you’re pretending to be someone you’re not."
    s "..."
    ay "..."

    scene ayanenewthree2
    with dissolve

    ay "Well, if you change your mind, I’ll be right beside you."
    ay "You already know that I’d do anything for you, so consider me staying a little later today as one more testament in Ayane Amamiya’s love bible."
    s "If anyone else asks, we’re going to have to stick to the cleaning duty excuse. “Love Bible” doesn’t sound like a legitimate excuse."
    ay "To be honest, I doubt anyone would believe any sort of excuse we gave them to explain me staying after school with you, Sensei."
    ay "This might be a little hard to believe, but my love for you is pretty widely understood among us girls."
    s "I’m surprised Ami showed no resistance to this if that’s the case."
    ay "I don’t think it’s {i}that{/i} surprising. Especially considering that Ami probably noticed something was wrong as well."
    s "Nothing is wrong, though."
    ay "Then I guess Ami was okay with it because she noticed {i}nothing{/i} was wrong."
    ay "I know I obsess over you literally all the time, but I know when I should stop. And I think that even if Ami wishes I’d flirt with you a little less...that she trusts me with your heart."
    s "That’s a bad move. I don’t even trust you with my heart."

    scene ayanenewthree3
    with dissolve

    ay "You don’t?"
    s "Of course not. It’s nothing personal, though, since there’s not anyone I would trust with something as important as that."
    s "It might sound romantic to some people to have someone they can be open and honest with but, to me, that sounds-"

    scene ayanenewthree4
    with dissolve

    ay "I get it. I really do."
    ay "Maybe not 100%%, but I can relate to the whole “Not wanting to open up to someone” thing."
    s "You say, despite opening up way too much to me almost every single day."
    ay "Ahh, there’s the difference, Sensei. The door you’re referring to was left open for way too long and doesn’t close anymore."
    ay "But there are plenty of other doors in my house that lead to different rooms...and I doubt that I’d open those up to even you right now."
    s "Then I guess you {i}can{/i} relate in some way."

    scene ayanenewthree2
    with dissolve

    ay "Of course I can. I’m your future wife."
    ay "And I’m sure there will be plenty of nights in the future where the two of us gather beneath the stars- sharing all sorts of worries or secrets or...anything we want to share with one another."
    ay "It’s just a little hard for us right now since the real stuff will just come across as annoying."
    s "You’re a lot more perceptive than you look, Ayane."
    ay "Are you calling me ugly?"
    s "What? No."
    ay "Good. Because if you were calling me ugly, I would throw myself out of this window."
    s "Please don’t. That sounds like an incredibly stressful situation to deal with."
    s "And I guess..."
    s "I might miss you a little if you were gone."

    scene ayanenewthree5
    with dissolve

    ay "..."
    ay "Did you just-"
    s "Nope."
    ay "I could have sworn I just heard you say something actually romantic for...probably the first time ever."
    s "Is saying I’d miss you {i}a little{/i} really that romantic?"

    scene ayanenewthree6
    with dissolve

    ay "You {i}did{/i} say it! Oh my God! I wish Ami was here to see this!"
    s "I feel like that would significantly increase the chances of you ending up as a puddle of flesh and blood on the concrete below us."

    scene ayanenewthree7
    with dissolve

    ay "Then, at least I would die happy..."

    scene black
    with dissolve2

    "The night gets darker and the reasons we have to stick around reduce to somewhere near zero."
    "But even with that in mind, the two of us feel a shared inclination to go higher rather than lower."
    "And I follow Ayane as she begins to move toward the wrong set of stairs."
    "........."
    "......"
    "..."

    scene ayanenewthree8
    with dissolve2

    "I continue following her until we can go no higher."
    "Through an unlocked door and onto the roof of the school-"
    "Up a ladder, then another-"
    "And before long, we are free to look down on everything and everyone."
    "That power is quickly diminished and made irrelevant by the simple fact that I can see nothing from up here."
    "But still-"
    "Something about it allows me to relax my shoulders."
    "I am more unguarded when closer to death than I am in the safety of my own home."
    "Ayane speaks again. "
    "Her words cut through the haze of a trillion dying lights."

    ay "This is a lot better, don’t you think?"
    s "I guess. It’s a little hot, though."
    ay "{i}You’re{/i} a little hot, though."
    s "Hilarious."
    ay "Hey! I’ll have you know that I consistently rank among the top ten funniest girls in our class based on the polls I force Sana to run online."
    s "I’m honestly amazed that she hasn’t asked for a new roommate yet."
    ay "And {i}I’m{/i} honestly amazed by {i}how hot you are.{/i}"
    s "Ayane, please."
    ay "Sorry. I’m done now."
    ay "For real, though. Doesn’t it feel much better up here?"
    ay "I’ve never actually been on the roof of the school before- just heard about it from Ami. But my bedroom at home did have a window I could climb out of and sit on the roof."
    ay "I remember doing that a lot after my mom left."
    ay "And I guess it became some sort of coping mechanism for me or something like that since I’m still compelled to climb as high as I can whenever I’m feeling down."
    ay "Even your worries seem smaller when you’re this far off the ground."
    ay "And I’m not saying that the reason I brought you up here is to try and force the way I handle things on you-"
    ay "I just thought it might be a little easier to breathe in a place with more air."
    s "..."
    ay "..."
    s "That line would have been a lot better if higher altitudes didn’t make it {i}harder{/i} to breathe. "
    ay "Ooh! Maybe we should just have class on the roof from now on if being up here is going to help you remember cool facts like that?"
    s "Thank you, Ayane."
    s "Not for your sarcastic teaching comment, but for looking out for me even when you probably shouldn’t be."
    ay "..."
    s "..."
    ay "You’re welcome, Sensei."
    ay "You were there for me, so I’ll be here for you."
    ay "I didn’t expect you to actually thank me, though. It’s not really like you to lean into serious moments like this."
    ay "But I guess we all act a little differently when we’re on top of the world."
    ay "Oh! Here’s a fun idea. How about we take turns admitting some of our deepest, darkest secrets to one another? That’ll help kill some time before we head back, won’t it?"
    s "I’m good. I don’t really have anything I’m actively hiding from you anyway."
    ay "What? Really? Well, that’s no fun."
    ay "I guess we’ll just have to have sex instead, then."
    s "..."
    ay "..."

    "Wait, what?"

    s "Was that for real? Because it’s hard to tell with you sometimes."
    ay "Yeah. It was."
    ay "I’m a little nervous, but...I think I’m ready."
    ay "Assuming you’re still okay with it, of course. Because I absolutely wouldn’t blame you if you felt weird about this and, like...wanted to wait until I graduate or something."
    s "What would waiting that long change? "
    s "You’ll still be my niece’s best friend and I’ll still be a man who was supposed to be looking after you."
    s "This is wrong no matter what angle you look at it from."
    ay "I know."
    ay "But this is a mistake I’ve wanted to make for a very long time."
    ay "And I am also very horny right now."
    s "Sounds like a pretty normal day for you."
    ay "I am a girl in love in the throes of puberty and I will not allow you to shame me for my overactive imagination and desire to touch you."
    s "I’m not shaming you for anything. Nor am I trying to talk you out of it since I have no intention of refusing."
    ay "Then-"
    s "I just need you to promise that no one will ever find out about this."
    ay "..."
    s "Because, if they do-"
    ay "Sensei, I’m not an idiot. I may be blindly in love, but even a blind woman would be able to prevent herself from diving head first into a meat grinder."
    s "Please refrain from using the word “meatgrinder” while I am in the process of forming an erection."
    ay "I am about to sleep with my friend’s uncle...who is also my teacher...who is also nearly double my age."
    ay "I’m obviously going to keep that a secret."
    ay "When I say I love you, I don’t mean immature, schoolgirl love. I mean {i}real{/i} love. The kind that is protective and loyal and understanding."
    ay "I will do anything you ask me to, and {i}not{/i} because I’m worried that you’ll leave if I don’t-"
    ay "But because I want you to be happy."
    ay "I want us to be happy together."
    ay "But right now-"
    ay "More than anything-"
    ay "I want you to take me home and make love to me before I have an orgasm from just thinking about it."
    s "..."
    ay "..."
    s "Do we really need to go all the way back to the dorm?"
    ay "Sensei, when I said that I want my first time to be special, I didn’t mean “doggystyle on the roof” special. "
    s "I mean...there are other positions."
    ay "But my bed is so big and soft...and Sana is sleeping at her mom’s tonight."
    ay "And also, if we fall off the roof, there’s a good chance you could break your penis and never be able to have sex with me again."
    s "Dorm room it is."
    ay "Heheh...thank you."
    ay "Not just for agreeing to take me home...but for everything you’ve ever done since the moment we’ve met."
    ay "Tonight will be the start of something beautiful, Sensei."
    ay "I am forever yours...any way you want me."
    ay "Any way you-"
    s "Stop talking and start walking or I am going to wind up deflowering you on the stairs."
    ay "Deal. "

    scene black
    with dissolve2

    "We make our way off of the roof and back into the school."
    "Ayane excitedly and hurriedly pulls me through the halls by the wrist, occasionally turning around and giggling."
    "It’s a childish giggle that fills me with a sense of lustful dread in both knowing and accepting that I am about to cross a boundary that I {i}know{/i} should not be crossed-"
    "And yet none of the horrible things that I have acknowledged both verbally and mentally even partially dissuade me."
    "This is who I am."
    "I am not built for love- but if I can help someone like Ayane {i}feel{/i} loved while gaining something for myself in return..."
    "I will help her time and time again."
    "And I will take her body in my hands, the same way she has dreamt of time and time again-"
    "And cocoon myself in the idea that I am only as broken as she thinks I am."

    $ renpy.end_replay()
    $ ayane_love +=1
    $ ayanenew3 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump ayanedorm10

label ayanespecial40:
    scene ayanecantbone1
    with fade
    play music "phantomthief.mp3"

    "I’m not going to lie, not having Makoto around fucking sucks."
    "Because, in addition to being one of the girls I am currently allowed to have sex with (Thanks, Maya), her {i}not{/i} being here is beginning to increase the amount of time I have to spend in this building."
    "And it certainly doesn’t help that Imani is a pretty good teacher and has actually started assigning work to the girls. "
    "Now, you may be asking yourself, just how much paperwork can there possibly {i}be{/i} for a class of twenty-ish who receive maybe one written assignment per week. And the answer to that is simple."
    "There is paperwork."
    "It’s not a large amount. In fact, the amount I have to handle is so minuscule that I’m sure Wakana would mock and ridicule me if she could only hear my thoughts."
    "But when you don’t want to work, any amount of work at all is too much."
    "I have far too many things to think about."

    play sound "knock.mp3"

    s "..."

    "And far too many girls to have sex with."

    s "Come in."

    play sound "dooropen.mp3"
    scene ayanecantbone2
    with dissolve

    "Or not."

    ay "Good! You’re still here. I was worried you may have left with Ami and Maya."
    s "Is there any reason {i}you{/i} didn’t leave with Ami and Maya?"
    ay "Swim club, obviously."
    s "Ahh, yes. I can see that it’s going very well by the fact that...you are here and not there."

    scene ayanecantbone3
    with dissolve

    ay "Yeah...I got halfway there and then thought to myself- you know what, Ayane? It’s been a long time since you’ve hung out with Sensei in his office after school. You should go do that."
    s "Good on you for being mentally stable. You’ll have more free time that way."

    scene ayanecantbone4
    with dissolve

    ay "I wouldn’t mind being a little crazier if it meant I got to spend more time with you."
    ay "And, at the rate things have been going lately, that seems like it might be a real possibility!"
    s "Is the fact that this is all some sort of infinite cycle finally starting to weigh on you?"

    scene ayanecantbone5
    with dissolve

    ay "Of course. I just haven’t quite figured out the right way to talk about it yet because I don’t understand nearly as much as you and Maya even {i}with{/i} all of the questions I’ve asked her."
    ay "Which is doubly annoying since it’s starting to seem like being the “runner up” just might be who I am as a person."
    s "You’re not a runner up at all, Ayane. You’re...Well, you’re you."

    scene ayanecantbone6
    with dissolve

    ay "Yeah. Second place to Ami when it comes to your list of interpersonal priorities and second to Maya when it comes to your list of...apocalyptic ones."
    s "If you weight the points you get from both of those categories, I think that would put you in first."

    scene ayanecantbone7
    with dissolve

    ay "Sensei, I’m being serious right now. This is all still really scary to me and there are so many things I don’t understand. "
    ay "Also, I’m worried that if I have to go any longer without having sex with you that my vagina is going to close up and we’ll never be able to have sex again."
    s "What were you saying about going insane just a minute ago? Because I think that sentence may have just put you over the edge."

    scene ayanecantbone8
    with dissolve

    ay "You know...when I first heard that abstinence suggestion thingy from Maya...I thought to myself, “That sounds hard and annoying...but I think I can do it for the sake of science.”"

    scene ayanecantbone9
    with dissolve

    ay "Now? Now, I just want you to pin me down and fuck my brains out until I can’t even move anymore."
    s "Please don’t say things like that to me when I’ve been doing so well with this so far."

    scene ayanecantbone6
    with dissolve

    ay "But...Sensei! Think about it for a second..."
    ay "Why should we even have to do this in the first place? It doesn’t make any sense."
    s "It’s for Maya’s...theory or whatever."
    ay "Yes, I know that. But what would even be the point of proving that theory? "
    ay "Isn’t me finally showing up after...the bajillions of times you guys have done it a step in the {i}right{/i} direction? Won’t getting rid of me just send you backwards?"
    s "First off, I’ve only done it a handful of times. Maya’s the one who has reached  “bajillions” territory...possibly."
    ay "I’m fine with suffering for the sake of you being happy. I am. But-"
    s "I’m not asking you to {i}suffer,{/i} Ayane. In fact, I’m not the one asking you anything at all."
    ay "I know. You’d never ask me to do something like that. But the truth is that I {i}am.{/i} And I’m not just talking about the sex at this point even if that {i}is{/i} an admittedly huge part of it."

    scene ayanecantbone10
    with dissolve

    ay "I just..."
    ay "I can’t help but feel like if Maya is right and everything {i}does{/i} work out..."
    ay "That I’ll just go back to being excluded again..."
    s "..."

    scene ayanecantbone11
    with dissolve

    ay "Listen, uhh..."
    ay "Can we sit on the couch if I promise not to try and have sex with you? Doing things this way makes it feel too much like counseling and I kind of need you to feel like {i}you{/i} right now."
    s "Sure. But I’m blaming you if Imani yells at me for not finishing all of this grading stuff on time. "
    ay "I probably shouldn’t be encouraging this type of behavior when the school has already decided you needed a student teacher, but...grades should be the last of your priorities right now..."

    scene black
    with dissolve2

    "Ayane moves over to the couch and curls herself up into a ball, waiting for me to come join her as I slide the remainder of my “work” back into my desk."
    "I understand where these worries are coming from. Especially when, for the most part, she’s kept them bottled up ever since the three of us “respawned” in this very room."
    "But that’s what Ayane does. She keeps things to herself until she literally can’t anymore. "
    "And if she’s worried enough about this to actively seek me out...and shirk responsibilities she personally signed up for..."
    "Something must really be wrong."

    scene ayanecantbone12
    with dissolve2

    ay "Thank you. I needed this."
    ay "I’m sure it’ll sound stupid since it’s something you’ve been shouldering for a long time, but...I guess my shoulders aren’t as big as yours. Which means this whole thing has been really hard for me so far."

    scene ayanecantbone13
    with dissolve

    ay "And you’ve been great...really."
    ay "But...Maya, on the other hand..."
    s "Maya cares about you. "
    ay "Does she?"
    s "Uh...probably? I guess it’s hard to ever really know {i}anything{/i} with-"
    ay "If she cares about me, why is her top priority right now making sure I don’t get any closer to either one of you?"
    ay "If the whole pregnancy theory thing is true and I don’t get to come with you guys to the roof next time...won’t I just be...you know, reset? Why would she do that to me?"

    scene ayanecantbone14
    with dissolve

    s "That’s not {i}exactly{/i} how things work, I don’t think. "
    s "It seems that, so long as nothing happens to me, everyone keeps most of their memories. And only {i}some{/i} things wind up getting wiped away after Maya does...whatever it is she does."
    ay "But those are still {i}my{/i} memories. Memories I want to keep because they’re memories that brought me closer to you."
    ay "It shouldn’t be up to Maya to decide that I should just throw them away to put an end to a little bet that she has with herself. "
    s "If you’re so confident that her theory is wrong...it shouldn’t be a problem, though. Right?"

    scene ayanecantbone15
    with dissolve

    ay "I mean...kind of?"
    ay "I guess?..."
    ay "It’s less about the theory itself and more about what asking us to go through with it means."
    ay "I still think she’s wrong and I still think I’ll be able to stay with you guys, but I’m worried that she doesn’t {i}want{/i} me to. "
    ay "Like she...wants this weird, paranormal universe to be one for just the two of you. And that she’s so used to different versions of me getting discarded that I’m barely even a human to her anymore."
    ay "I wish...she wasn’t so hard to understand sometimes, you know?"
    s "Trust me. I know."

    scene ayanecantbone16
    with dissolve

    ay "So...what now, then? What else can we do while we wait for the next {i}thing{/i} to happen?"
    s "Just...wait, I guess. That’s all I normally do. "
    ay "No wonder you guys haven’t made any progress. There has to be, like...{i}something{/i} we can do to find out more about this, right?"
    s "Sure. It’s never too late to start studying chronokinetics. Act now and Wakana may even take you into her class. You’ll certainly have more luck with something like that there."
    ay "Sensei-"
    s "I don’t know what you want me to say, Ayane. "
    s "I get that you’re scared. And I’m here to...try and make you feel better in whatever sort of sexless way I can. "
    s "But, despite having experienced this more than you, I really don’t know that much. And I have no idea what we can do to find out more."
    s "If you have any ideas, I’ll be happy to indulge them. But right now, all we have is Maya’s...so I still think the best course of action is just figuring out if she’s right or not."
    ay "If she’s right, though...aren’t you worried that the current {i}me{/i} won’t come back?"
    ay "Or..."
    ay "Or will any old version of me do?..."
    s "What is that supposed to mean?"
    ay "Do you love me?...Or do you love {i}me?{/i}"
    s "That is...way too deep of a question for regular office hours."
    s "Besides, Maya finding out that she’s wrong about the one thing she thinks she knows more about than everyone could be a very humbling experience for her and, not gonna lie, I think she needs that."

    scene ayanecantbone17
    with dissolve

    ay "Fine. But just so you know, if I make it to that roof again after X months of not having sex with you and {i}don’t{/i} have my brain wiped, I am throwing myself at you with a level of aggression you have never seen before."
    s "I don’t think Maya will be very happy about that."
    ay "I honestly don’t care."
    s "I mean...yeah. If we manage to prove that’s not why you’re showing up, I’m not going to reject any of your advances."

    scene ayanecantbone18
    with dissolve

    ay "We?"
    ay "So...you’re on my side now?"
    s "There are sides? Is my life not already complicated enough having to fend off so many girls vying for my affection?"
    ay "Oh, please. As if you’re fighting any of them off. "
    ay "I’m not talking about an Ayane vs Maya, choose your heroine battle. I’m talking about whether or not you think getting me pregnant is the key to all of this world’s mysteries."
    s "I think that if it {i}is,{/i} I am going to be more confused than ever. So, sure. Go ahead and chalk that up to me being on your {i}side.{/i} "
    s "But I will not get sucked into whatever spat you and Maya start with one another. So please do not tell her I said that."

    scene ayanecantbone12
    with dissolve

    ay "I won’t. I don’t have any intention of starting any problems with Maya. I love her."
    ay "I just don’t want her trying to tackle this entire burden herself when she finally has a friend willing to take on some of it for her."
    ay "I have no idea what the future holds for any of us...and despite how confident I am, I can’t even guarantee {i}my{/i} short-term future anymore. "
    ay "And who knows? Maybe we never wind up learning anything."
    ay "Maybe this loop never breaks and we all wind up complacently conquering the end of the world together. Over and over and over and over..."

    scene ayanecantbone18
    with dissolve

    ay "But we’ll be doing it together. "
    ay "And none of us will ever have to feel...left out or..."

    scene ayanecantbone19
    with dissolve

    ay "Or like we’re the runner up ever again."
    s "..."
    ay "..."
    s "I do love {i}you,{/i} you know."

    scene ayanecantbone20
    with dissolve

    ay "Huh?"
    s "To answer your question from before."
    s "The {i}you{/i} you are now is the only Ayane Amamiya I care about. And if anything were to ever happen to {i}you,{/i} I doubt I’d be able to look at you the same."
    ay "Sensei..."
    s "But that doesn’t mean I wouldn’t still have sex with the other Ayanes. "
    ay "..."
    s "..."

    scene ayanecantbone21
    with dissolve

    ay "I can’t tell if I’m horny because of the way you just told me you loved me, the fact that we haven’t had sex in what feels like a whole year, or the idea of you having sex with my clones."
    s "Cloning you sounds fun. I don’t think I’d be able to handle more than three Ayanes at once, though."
    ay "I think I would also cut myself off at three Senseis."
    s "That sounds...painful."
    ay "That sounds {i}amazing.{/i}"
    s "..."
    ay "..."

    scene ayanecantbone22
    with dissolve

    ay "Okay! We should probably call it a day here since I know what you are thinking and you know what I am thinking."
    s "If Hell exists, this is it."

    scene ayanecantbone23
    with dissolve

    ay "Yes, Sensei."
    ay "Yes it is."

    scene black
    with dissolve2

    "Ayane leaves my office and..."
    "And I wind up heading over to the school restroom to {i}relieve{/i} myself before going home for the day."
    "Maya is lucky that I feel like my existence rests in the palms of her hands. Because otherwise, I would have gone against her wishes at least three times in the last hour."
    "One for every single Ayane clone I imagined having sex with as I was jerking off in the bathroom."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayane_lust += 1
    $ ayanespecial40 = True
    stop music fadeout 7.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    "{i}Too bad you can’t have sex with her!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label ayanesanabeach1:
    "I tap on Ayane’s name in my phone and wait for her to answer. "
    "Given that she’s normally out and about early in the morning, I figure that meeting up with her might be the start to my day I need after the {s}SERIES OF HORRIBLE NIGHTMARES{/s} uninteresting dreams I had last night."
    "Here’s hoping that she is still alive."

    play sound "phonebeep.wav"
    play music "summerwind.mp3"

    ay "Sensei! Good morning!"

    "She is."

    s "Good morning, Ayane. What are you up-"
    ay "Are you home right now?"
    s "What? Yes. I just woke-"
    ay "Good! I’ll be there in thirty seconds. Get dressed."
    s "What? Thirty seconds?"
    ay "I don’t have time to explain!"
    s "Well...why not? Because the fact that you’re only thirty seconds away means-"
    ay "I don’t have time to explain why I don’t have time to explain! Now get dressed! And pack a swimsuit!"
    s "A swimsuit?"
    ay "Fifteen seconds!"

    play sound "phonebeep.wav"

    "I hang up the phone and frantically begin to search for my clothes, only to remember that I keep all three of my shirts in the same drawer- directly above the drawer I keep my pants and swim trunks in."

    scene ayanebeachtrip1
    with fade

    "Having all of the required equipment (But still only a vague idea of what is going on), I make my way into the living room."

    play sound "dooropen.mp3"

    "As soon as I go to reach for the door, though, Ami’s niece alarm goes off and she comes running out of her bedroom to catch me before I head out."

    scene ayanebeachtrip2
    with dissolve

    a "What’s going on? You haven’t even eaten breakfast yet. Why are you leaving in such a hurry?"
    s "I think Ayane is coordinating a kidnapping of me."
    a "Ayane is...what?"
    s "I’m pretty sure I am about to be dragged to the beach. Or...pool. Or any other place that requires a swimsuit."

    scene ayanebeachtrip3
    with dissolve

    a "What?! But I have work today! You guys aren’t allowed to have fun on days that I have work!"
    s "I’m sorry, Ami. But this is beyond my control. It’s already been a full minute since I called her, which is twice as long as the amount of time I was given to get out of the house."

    play sound "knock.mp3"

    ay "Sensei! You’ve had twice as long to get ready as I gave you! Hurry up! "
    s "See? She’s already here."

    scene ayanebeachtrip4
    with dissolve

    a "Go away, Ayane! Sensei is too busy loving me to-"

    play sound "dooropen.mp3"
    scene black
    with dissolve

    ay "Sorry, Ami! No time to argue! I’ll be taking your uncle now!"
    a "Stop! Thief! "
    ay "I’ll make it up to you by providing you your very own Sensei clone once I figure out the technology! "
    a "I want three!"
    ay "Hey, we have the same fantasy! "
    ay "Anyway, bye! See you tomorrow!"

    "Ayane grabs my wrist and is somehow strong enough to pull me out of the doorway and..."

    scene ayanebeachtrip5
    with dissolve2

    "...Into the backseat of a limo?"

    s "This seems excessive. And unnecessarily fast-paced."
    ay "I probably could have slowed down a bit, but things were more fun this way."
    ay "I’m glad you called me when you did. Any later and we would have already passed your house."
    s "I seem to be riding in cars a lot more than normal lately and I can’t say I like it."
    ay "Don’t worry. Geoffrey is a great driver from all the time he spent working for Al Capone back in the day."
    s "Wait, how old is Geoffrey?"
    ay "That doesn’t matter. What {i}does{/i} matter is that we’re going to the beach!"
    s "Yeah, I kind of figured as much. Why so early, though?"
    ay "Because having an entire day full of fun is better than having...only part of the day full of fun?"
    s "Well, I’m glad that Sana seems to be getting a head start."

    scene ayanebeachtrip6
    with dissolve

    sa "Can’t talk...in the zone!"
    ay "Sana got a new game for her Switch and refused to take her eyes off of it all morning. "
    ay "Originally, the plan was for just the two of us to go to the beach together, hence her uncharacteristically showy outfit. But, seeing as she has abandoned me, it looks like it’s the two of {i}us{/i} now."

    scene ayanebeachtrip7
    with dissolve

    ay "Is that okay? "
    s "Does asking me even matter when I have already been borderline kidnapped?"
    ay "No. It does not."
    ay "But I’m primed and ready to make up for this inconvenience by giving you a first look at my brand new swimsuit."
    s "But I liked your old swimsuit."
    ay "This one shows significantly more skin."
    s "The old swimsuit sucks. I like the new one now."
    ay "Just make sure you stare a little more at {i}me{/i} than you stare at Sana, okay? Because she got a new one too and I don’t want my painstaking selection process to have been for nothing."
    s "I’m pretty sure Sana wouldn’t even know that I’m staring at her at this point, but...sure. For your sake, I’ll make sure to spend the bulk of my time looking at you."
    sa "Silence! You are...making it hard to aim!"

    scene ayanebeachtrip8
    with dissolve

    ay "Sana, it’s just Splatoon. Would it really kill you to-"

    scene ayanebeachtrip9
    with hpunch

    sa "{i}JUST{/i} SPLATOON?!"
    sa "DO YOU HAVE ANY IDEA WHAT YOU JUST SAID?!"
    sa "THIS IS SPLATOON {i}3!{/i} IT’S THE {i}SECOND SEQUEL,{/i} AYANE! THE THIRD INSTALLMENT OF A TRILOGY! COME ON!"
    ay "R...Right..."
    ay "Sorry..."

    scene black
    with dissolve2

    "Sana immediately goes back to ignoring us and focusing on her game, prompting Ayane and me to figure out what to spend the rest of the drive talking about."
    "Having never been in the same place at the same time as him before, I attempt to usher Geoffrey into the conversation as well but, unfortunately, find that the window in the back of the limo is stuck shut."
    "I accept that I may never get another chance to speak to him and just focus on Ayane’s detailed explanation of his backstory instead."
    "Unfortunately for you, that backstory is far too graphic. So I will keep all of the details to myself and patiently await the opportunity to see two adorable girls in revealing clothing."
    "........."
    "......"
    "..."

    scene ayanebeachtrip10
    with dissolve2

    "Boy, did all of that patiently waiting pay off."

    ay "What do you think? Still like the new swimsuit more? Or do I seem like more of a one-piece girl after getting a look at both of them?"
    s "I think this new one works a lot better. And no, that is not me being biased or generally favorable of anything that shows me more of your body at once."
    ay "I’d ask for a more in-depth description of your thoughts on my body but, unfortunately, it appears that Sana is taking a short break from Splatoon {i}3{/i} to hear what you have to say about {i}her{/i} swimsuit."
    sa "I...I don’t really...have to know what Sensei thinks..."
    sa "I...obviously...can’t pull...off this kind of thing as well as you...so..."
    s "Interesting choice, Sana. What prompted you to follow Ayane’s example and start revealing more of yourself if you’re still uncomfortable with that?"

    scene ayanebeachtrip11
    with dissolve

    sa "Um...p...peer pressure?..."
    sa "Character...development?..."
    sa "Thinking that...it was just going to be...Ayane and me?..."
    s "Well, whichever one of your many potential reasons it may be...I support it. I think you look just as cute as Ayane."

    scene ayanebeachtrip12
    with dissolve

    sa "I think...um...you’re...an idiot..."
    s "And I think I’m just never going to compliment you again. "
    ay "That works out beautifully! Because that means Sana can go back to playing her game while the two of us get some sun!"
    s "I’m not a fan of the sun. But you go ahead and have fun, Ayane."
    ay "Nope! Not letting you off that easily, Sensei. If you don’t get some vitamin D every once in a while, you’re going to die early. And I’ll be damned if I have to bury you before our thirtieth anniversary."
    s "I’ve got some vitamin {i}D{/i} for you right here."
    ay "God, I wish."
    sa "Uhh..."
    sa "Okay...I’m going to leave now..."

    scene ayanebeachtrip13
    with dissolve

    ay "Bye, Sana! Remember to put on sunscreen! And to not accept any candy from strangers!"
    sa "I’m just going to...find somewhere dark and...shady to...ignore everyone..."

    "Sana disappears behind the bathroom and, once again, Ayane and I are on our own."

    scene black
    with dissolve2

    "My rich blonde “princess” and the newest member of our unnamed apocalypse squad takes this as a cue to head closer to the water, once again grabbing my wrist and pulling me along beside her."
    "It’s a lot more gentle and a lot less urgent this time, though- like a way for her to be closer to me without having to use words or spread her legs. "
    "And while methods like that last one are a lot easier for me to understand and {i}feel,{/i} I don’t hate the sensation of her small hand slowly inching closer to mine. "
    "Nor the scent of her sunscreen or the shape of her silhouette as it slithers across the sand like a snake."

    scene ayanebeachtrip14
    with dissolve2

    "We come to a halt where the water meets the land and I try to wrap my head around why {s}God{/i} {s}the gods?{/s} {s}GOD{/s} god can’t just make it a few degrees colder."
    "You know- enough to keep us all alive but not enough to scorch our skin or give us cancer if we stay beneath it for too long."
    "But in thinking this, I realize that my mind has strayed so far from the path it’s meant to walk that it takes every ounce of self-control I have to not create a distraction in the form of a hand inside of Ayane’s swimsuit."

    ay "I really love the summer, Sensei."
    s "You’re insane."
    ay "I know you’re more of a winter person. But weather like this is actually perfect for me. There’s just something about the way the heat hits my skin that makes me...I don’t know. Comfortable?"
    ay "The only problem is now I don’t know whether or not it’s even real."
    s "What do you mean by that?"
    ay "I mean that Christmas is only a couple months away and it still feels like the height of summer. "
    ay "Isn’t that kind of...weird?"
    ay "At this rate, we might even wind up having our annual Christmas party right here on the beach."
    s "There’s another suspicious element to that last sentence I’m not even sure if you’ve grasped yet. But you’re on the right track. "
    ay "Is it the fact that we’re only a short while away from Christmas party number three despite still being first years? Because I’ve been thinking a lot about that lately too."
    ay "There are...all sorts of weird things going on with this timeline, aren’t there?"
    s "Bingo. "
    ay "I assume that’s just more...infinite loop fuckery?"
    s "I assume so as well. I also don’t know if I like the sound of you cursing without my penis inside of you. It’s rare."
    ay "Less rare than your penis being inside of me at this point. "
    s "Don’t remind me."
    ay "You want to know the weirdest part of all of it, though? Any time I try to bring that up to the other girls, they just...change topics. And completely ignore what I said. "
    s "Yeah...I’ve noticed that too. "
    ay "Why doesn’t anyone think it’s weird? That we have years worth of memories packed into one...and that even the holidays aren’t properly lining up with the seasons anymore?"
    ay "Is it really just us two and Maya who understand that?"
    s "Saying we {i}understand{/i} it might be a bit too generous as neither of us have any idea what that even means."
    ay "True. But we know it’s {i}happening-{/i} which is more than most can say."
    s "You’re...really taking in a lot of information about this whole reset thing, aren’t you?"
    ay "I’m naturally curious...about all sorts of things. And I think you’d have to be insane to not try and understand anything after being dropped into a situation like this."
    ay "Is any of it real? Are {i}we{/i} real? "
    ay "Just how deep does all of this go?"
    s "At this rate, you’ll be telling all of us and we won’t even {i}need{/i} Maya anymore."
    ay "Maybe we don’t need her to begin with?"
    s "..."
    ay "Anyone can do the reset thingy, right? Not just her. "
    ay "If that’s the case..."
    ay "I think I want to try it next time. "
    ay "Do you think she’ll teach me how if I ask?"
    s "I can’t say for sure, but...probably not. "
    s "Maya doesn’t exactly like change."
    ay "I don’t think any of us do. I mean, if I {i}liked{/i} this, I wouldn’t be losing sleep over it. I wouldn’t feel like I’m the only one going insane for realizing things everyone around me just...ignores."
    s "You still have me. And despite your tendency to take pictures of me when I’m sleeping, I still think you’re surprisingly {i}sane.{/i}"
    ay "..."
    s "..."
    ay "I’ve got another question."
    s "I’m sure you have hundreds so just...ask me whenever you think of one instead of wasting words on warning me first."
    ay "I felt like this one deserved a warning due to its depressing nature."
    s "Uh-oh."

    scene ayanebeachtrip15
    with dissolve

    ay "So..."
    ay "Makoto’s dad..."
    s "..."
    ay "That...was the first time anything like that has ever happened before, right?"
    s "As far as I know, yes..."
    s "But Maya’s made it sound like other people have met similar fates in the past."
    ay "Did those people come back?"
    s "I’m pretty sure {i}we{/i} were among them, so...I’m going to say yes."
    ay "Does that mean Makoto’s dad might come back too?"
    s "..."
    ay "..."
    s "I hope so."
    ay "It’s so weird how time is moving both forward {i}and{/i} backward at the same time."
    ay "How people who should be gone wind up coming back...how our memories get reverted...and how new things are {i}still{/i} happening every day according to Maya."
    ay "How do we know that {i}this{/i} hasn’t ever even happened before? That we’ve never had this conversation?"
    s "We...don’t."
    ay "Exactly. We don’t."
    s "Aren’t you worried of knowing too much, though?"

    scene ayanebeachtrip16
    with dissolve

    ay "Should I be?"
    s "I know I am. But I’ve also been repeatedly told that finding out anything about my past might result in my brain imploding, so...yeah."
    ay "I guess it would be kind of hard to {i}not{/i} worry about something like that, yeah."
    s "What if we all have something like that? Key memories that whatever is controlling this world doesn’t want us to have back?"
    ay "You mean, like...God?"
    s "Is that something you believe in?"

    scene ayanebeachtrip17
    with dissolve

    ay "I did."
    ay "But now?"
    ay "I’m not so sure anymore."
    ay "If God is real, what is this supposed to be? "
    ay "A test?"
    ay "What are we supposed to gain from this...incomplete knowledge of how the world works when we can’t even share it with anyone else?"
    s "Beats me. But I’ll leave the critical thinking to you on account of the whole mind implosion thing."
    ay "That’s fine. I’m just thinking out loud at this point anyway."
    s "Look at you, learning to share your thoughts instead of keeping them all to yourself."

    scene ayanebeachtrip18
    with dissolve

    ay "Yes...look at me."
    s "..."
    ay "..."
    ay "No, seriously. Look at me. I bought this swimsuit with you in mind and you’ve done nothing but stare at the water for the last ten minutes."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Our talk about the inner workings of the world grinds to a halt as Ayane resets her mind (No pun intended) and refocuses on the real reason I think she came here today."
    "To get away from everything."
    "To take a break from this great new burden and remind herself that, beneath the mountain of troubles she’s taken it upon herself to excavate-"
    "She is still young."
    "That she still has the rest of her school life ahead of her and that she shouldn’t have to worry about caring for {i}me{/i} or {i}Maya{/i} when all that should matter to her is {i}herself.{/i}"
    "But that is just the type of person she is."
    "Someone with more love inside of her than she has ever been shown. "
    "Why?"
    "Why does she have no regard for the way {i}she{/i} feels?"
    "Why would she sacrifice this brief respite for the chance to reflect on how there is no respite for those like us at all?"
    "I don’t know."
    "And I will not find out today- for I leave her as soon as the sun sets."
    "And I make my way over to someone who was smart enough to avoid it in the first place."

    if sarasex == True:
        $ renpy.end_replay()
        $ ayanesanabeach1 = True
        $ ayane_love += 1

        "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
        "........."
        "......"
        "..."

        jump ayanesanabeach2
    else:
        stop music

        "Just kidding."
        "I never find anyone like that."

        $ renpy.end_replay()
        $ ayanesanabeach1 = True
        $ ayanesanabeach2skip = True
        $ ayane_love += 1

        "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
        "........."
        "......"
        "..."

        jump ayanesanabeach3

label ayanespecial50:
    scene hall_noon
    with fade
    play music "notabluearchivesong.mp3"

    "School ended about an hour ago. And with Makoto now returning to class (And refusing to take a break from doing more work than everyone) I am left with nothing do to but, once again, wander the halls."
    "My wandering is not aimless this time, though- for I’ve already decided to pay a visit to the manga club to provide some...advice. Or whatever it is an advisor is supposed to provide."
    "Did anyone {i}ask{/i} for this advice? No. But everyone knows that people who go around providing unsolicited advice to everyone are great and awesome and definitely not annoying."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "As I begin to pull the door open, I notice a distinct lack of chatter. Meaning I am either disturbing silent reading or-"

    scene ayanefitting1
    with dissolve2

    "Or Ayane and Molly are about to have sex."
    "I should have known something like this would happen the moment my penis was banned from being inside of her."

    ay "Hi!"
    s "So this is how it’s going to be, huh?"

    scene ayanefitting2
    with dissolve

    ay "How what’s going to be? "
    s "The future."
    ay "What?"
    s "Anyway, what’s going on in here? Why is Molly groping you?"
    mo "Taking measurements, Sir. For Ayane’s Halloween costume."
    s "That is not how you measure someone."
    mo "Aye. But it is how things would work in a video game and it provides much needed fan service for when people complain about the lack of sexual content."
    mo "Also, Ayane’s skin is soft and touching it gives me an XP boost."

    scene ayanefitting3
    with dissolve

    ay "Moisturize daily! Remember that, guys and girls!"
    s "I’m good. I’ve survived 31 years without ever having to do that and I do not intend to start now even {i}if{/i} it would make Molly more inclined to put her hands all over my body for a...boost thing."
    mo "No, Sir. If I laid hands on you only to find that your skin rivaled Ayane’s in terms of softness, the only status effect I’d receive would be confusion. And I have already hurt myself enough for the next year, thank you."

    scene ayanefitting4
    with dissolve

    ay "Aren’t you proud of me, Sensei? "
    s "For what? Having a tryst with a small, Irish girl on school grounds?"
    ay "No. For keeping my body in tip-top shape so we’ll be able to go fifty rounds on the night of our wedding."

    "Is {i}that{/i} how Chika does it? Moisturizing?"
    "Maybe I {i}should{/i} start doing that if it yields those sorts of benefits."

    s "Sure, whatever. I’m proud."
    ay "I’ll bet. You haven’t taken your eyes off of me this entire time."
    s "Why would I? Fanservice is cool."
    mo "Arms up."

    scene ayanefitting5
    with dissolve

    ay "Yes, ma’am."
    s "Correction- fanservice is {i}very{/i} cool."
    mo "Hmm..."
    mo "These feel bigger than I remember them. "
    ay "When was the last time you grabbed them?"
    mo "Last Halloween, I believe."
    ay "Don’t you think it’s weird that there have been multiple Halloweens in our first year of-"

    scene ayanefitting6
    with dissolve

    mo "What do you think, Sir? Want to give ‘em a grab and see how they compare to your memory? Assuming you’re not already providing every day checks for Ayane, that is."
    s "Ahh, those were the days."
    ay "Go ahead, Sensei. I don’t mind."
    s "I’m going to refrain from groping you in front of your classmates for now, Ayane."
    mo "Is it even groping if it is for the sake of fashion, Sir?"
    s "I’m sure that would sound great in court. Thanks, Molly."

    scene ayanefitting7
    with dissolve

    mo "‘Tis no trouble at all, Sir. I’m simply doing my job as club president."
    s "I understand now why you wanted the role. "
    mo "Sir, I’ve touched so many boobs at this point that I may as well be immune to them."
    ay "I can’t help but feel offended by that."

    scene ayanefitting8
    with dissolve

    mo "Don’t be. Yours are consistently the most enjoyable to grab. I mean measure. Which is what I’m doing. Measuring them. "
    s "I think Molly’s just a pervert."
    ay "She is. But as long as she gets my costume right, I don’t really care about how incorrect her methods are."

    scene ayanefitting9
    with dissolve

    mo "Worry not, Lidearel. I can assure you our group cosplay for this year’s Halloween party will be both my best work yet {i}and{/i} brimming with full-on lesbian energy."
    s "I once again remain adamant that Halloween is the best holiday."
    ay "I’m not really sure how much lesbian energy I can handle between the costumes and this club room."

    scene ayanefitting10
    with dissolve

    mo "Ahh. Is {i}that{/i} why you sided with those normie athletes instead of your companions in the manga club? Because of the amount of yuri power?"
    ay "Noooo...I just like swimming and staying active."
    mo "And using us for your own benefit when the time comes to look cute."

    scene ayanefitting11
    with dissolve

    ay "Joke’s on you, Molly. I always look cute. Plus, I have the perfect boobs according to whatever metric you use to rate them."
    s "They certainly are nice."
    ay "Thank you, Sensei. I am glad we’ve reached the point where you are able to compliment them in front of my friends."
    s "It’s just Molly. She’s not going to do anything."

    scene ayanefitting12
    with dissolve

    mo "Oi! What’s with this “Just Molly” crap? Shouldn’t ye’ be holdin’ me to the same standard everybody else is kept at?"
    s "Not when you’re even more of a degenerate than I am. "
    mo "Nobody is more of a degenerate than you, Sir."
    s "How many cartoons have you masturbated to now?"

    scene ayanefitting13
    with dissolve

    mo "Like...ever? Or...within a certain timeframe?"
    ay "It’s a weird day when I am somehow the least sexually charged person in the room."

    scene ayanefitting14
    with dissolve

    mo "Either way, we’re done for now. I got what I needed, so you can go ahead and put your clothes back on. Your {i}normie{/i} club is waiting for you, after all."
    ay "My normie club is taking the day off since Imani and Karin both had stuff to do today. But if you two wanted to come over to the pool and do a little swimming, I’m sure I can get us in."
    mo "Me? Swimming? Have you gone mad?"
    s "I would have agreed to come and watch if it was going to be both of you. But I can’t say I’m fond of the idea of just watching you swim by yourself. That sounds both extremely creepy and extremely lonely."

    scene ayanefitting15
    with dissolve

    ay "You guys are no fun. Is it really too much to ask to be covered in spandex and soaking wet with my teacher and an exchange student?"
    s "When you put it that way, probably."
    mo "Besides, I’ve got a batch of quests I need to be turnin’ in anyway. You two’ll be alone from here on out as Molly MacCormack is logging off."
    ay "But how are you going to turn your quests in if you-"
    mo "They’re in a different game, obviously."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    mo "Farewell! And don’t forget to lock the door when you leave! There are collector's items in here!"

    "Molly exits the clubroom and I am, for probably the first time ever, the sole person inside who is actually {i}affiliated{/i} with it in some way."
    "Granted, this affiliation is still pretty new to me and I have no idea what it even entails, but still. "
    "Anyway, Ayane non-chalantly puts her clothes back on like I’ve watched her do a thousand times before and then slides a couple of chairs out from underneath the table for us to sit down on."

    scene ayanefitting16
    with dissolve2

    ay "So, how excited are you to see my costume on a scale of one to ten?"
    s "One being your suit of armor and ten being you...wearing absolutely nothing?"

    scene ayanefitting17
    with dissolve

    ay "Leave my armor alone. I looked gallant and beautiful and strong and-"
    s "And zero fuckable."

    scene ayanefitting18
    with dissolve

    ay "I’m zero fuckable now and you’re still spending time with me."
    s "Good point. See you later, Ayane. "
    ay "Ha ha ha. Very funny."
    ay "I think you’ll like this one, though. I’ll still be gallant and elegant, but I’ll be the type of gallant and elegant that you’ll want to ejaculate in."
    s "Halloween can’t come soon enough."
    s "I’m not sure how I feel about having two parties in such quick succession, though. What with everyone talking about the Dorm Wars making a return and whatnot."

    scene ayanefitting19
    with dissolve

    ay "Oh, has nobody told you yet? We’re combining them this year to save time. Especially since we still have both our annual beach trip {i}and{/i} Christmas party right around the corner as well."
    ay "Time can sure get pretty fucky because of this reset business, huh? I don’t remember ever feeling this...rushed before."
    s "I mean, it’s not like anything is going anywhere. We don’t have to rush if combining everything seems like it’s going to be stressful to plan since I know you like being involved in that sort of thing."

    scene ayanefitting20
    with dissolve

    ay "Nah...I’m sure it’ll be fine. We’ll just have to figure out the new contests as soon as possible since I’m pretty sure we’ll be changing most of them."
    ay "Match-ups too since losing to the same person two years in a row would probably make all of us feel like shit."
    s "Not out for ruthless...rap....revenge or whatever?"

    scene ayanefitting21
    with dissolve

    ay "Probably not. There’s no way I can compete with Uta without some serious training. And with the exception of Kirin, nobody is really looking for revenge on anyone."
    ay "In fact, both Maya and Makoto were extremely adamant about {i}not{/i} repeating the same contest two years in a row. Though, Makoto might still just be feeling kind of down."
    s "Anything you have your eye on, then? Anyone you’re looking to take down?"

    scene ayanefitting20
    with dissolve

    ay "Not off the top of my head. I’m sure something will come to me, though."
    ay "Or, who knows? Maybe not. Finding motivation at all lately has been damn near impossible. That’s why I’m hoping this party can get me back into the swing of things."
    s "Ayane-"
    ay "Don’t worry. I’m not going to talk your ear off again with more of my apocalyptic worries. I’ve been battering you with them pretty much every time we’ve talked lately and I don’t think either of us likes it."

    scene ayanefitting16
    with dissolve

    ay "I might ask you for a reward if I {i}do{/i} win, though. "
    s "A reward? What kind of reward?"
    ay "A date, maybe?"
    s "We’ve been on dates before, haven’t we?"
    ay "I guess. Maybe some sort of promise, then? Or...maybe a memento of yours that I can hang onto for good luck? I’m not really sure."
    ay "But I kind of need something to latch onto right now since latching onto the whole idea of the world being one big cycle isn’t good for me and you’re only a viable distraction when I can actually see you."
    ay "If there’s some sort of reward for me if I come out on top of my dorm war thingy...I feel like I’ll be able to look forward to it a little bit more. The issue is just figuring out what the reward should {i}be.{/i}"
    s "Well, what do you want it to be?"
    ay "Maybe an engagement ring?"
    s "Uh-huh. Anything else you had in mind?"

    scene ayanefitting21
    with dissolve

    ay "A...promise ring?"
    s "Isn’t that just an engagement ring for someone who’s too much of a pussy to actually propose?"
    ay "Well, it obviously has to be something involving you since that’s pretty much the only thing getting me out of bed at this point."

    scene ayanefitting19
    with dissolve

    ay "Oh! What if you be my slave for a day?"
    s "Are you into BDSM now? Because, if so, I think you’ve been spending too much time with Osako."
    ay "Are the rumors about Miss Watabe and Miss Osaka actually true?"
    s "Where did those rumors even come from?"
    ay "One of the girls in Class D works in the entertainment district and said she saw the two of them going into a love hotel carrying a pair of handcuffs."
    s "Maybe Osako just...fights crime?"
    ay "And Miss Watabe is her sidekick?"
    s "Seems plausible to me."
    ay "..."
    s "Or one of them was handcuffed to the bedpost and consensually abused for the next several hours."
    ay "That sounds more accurate. "

    scene ayanefitting20
    with dissolve

    ay "Anyway, there is {i}one{/i} thing I want from you. I’m just not sure if it’s something I want for my own peace of mind or if..."
    ay "If it’s something I want because I think it might make things a little bit easier for us."
    s "That’s..."
    s "I’m not really sure how to interpret that, actually."

    scene ayanefitting21
    with dissolve

    ay "That’s not your fault. I didn’t really know how to {i}say{/i} it."
    ay "How about this, then...if I win my contest this year...you can reward me by..."

    scene ayanefitting22
    with dissolve

    ay "By..."
    ay "Answering a question."
    s "That’s it?"
    ay "It’s a multi-layered and complicated question that could wind up changing everything, though. So I reserve the right to change my mind if I get scared and want to back down."
    s "Am I allowed to know the question ahead of time?"
    ay "Absolutely not. You’ll find out if I win. "
    s "I see..."
    s "I’ve got a question of my own then. Why ask {i}anything{/i} with that much potential for change? I figured you’d...want to avoid that, if at all possible."

    scene ayanefitting23
    with dissolve

    ay "Because everything {i}else{/i} is already changing. "
    ay "I figure slipping this question in might make it a little easier for me to adapt if I don’t like the answer."
    s "Not {i}everything{/i} is changing, though. We might not be able to have sex at the moment, but that doesn’t mean I don’t still-"
    ay "You love me and I love you. {i}That{/i} much hasn’t changed. But “everything” rarely means {i}everything{/i}. "
    ay "What it means in this context is that {i}I’m{/i} changing..."
    ay "Cracking under pressure..."
    ay "But most importantly..."

    scene ayanefitting24
    with dissolve

    ay "It means I’ve accepted that I’ve gotta grow up a little sooner than I wanted to."
    ay "It sucks, really. I like being a kid."
    ay "But I literally {i}can’t{/i} be a kid anymore if I want to maintain the life I have now. {i}Not{/i} changing and just going with the flow the way you do in the face of the end of days, is..."
    ay "That wouldn’t work for me."

    scene ayanefitting16
    with dissolve

    ay "I think I understand why Maya is the way she is now. "
    ay "And since I already promised I wouldn’t talk your ear off again, I’ll keep this as brief as I can."
    ay "I {i}absolutely...{/i}"
    ay "{i}Vehemently...{/i}"
    ay "Refuse to lose you."
    s "Ayane-"

    scene ayanefitting25
    with fade

    "Ayane shows no intention of letting me finish my sentence by leaping into my arms before I’m able to get the second word out."
    "And I guess I’m glad she does as...I have no idea what that second word was even going to be."
    "If it were up to me to decide her fate and whether or not she ever {i}will{/i} lose me, of course I’d make it so she doesn’t."
    "But the sad truth is I have no power over that."
    "And neither does she."
    "But if growing up ahead of schedule is her way of combating that-"
    "If sacrificing the remainder of her youth is the weapon she needs to slaughter it-"
    "I will be the sheath to her sword."

    scene black
    with dissolve2

    "Or the grass the blood that coats it falls on."

    $ renpy.end_replay()
    $ ayanespecial50 = True
    $ ayane_love += 1
    stop music fadeout 7.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label ayanekirintalk:
    scene furlough1
    with fade
    play music "normalday.mp3"

    m "...and that’s just one of the many reasons I don’t think children under the age of ten should be allowed in public spaces."
    s "Well said, Maya. Though, I’m a little confused as to why you’re the one kicking off this event when Ayane is the typical open-ended intro provider."
    ay "Hey, I’m fine with Maya stealing the spotlight every now and then. It’s not like I have an infinite amount of stories to tell all of you like she does."

    scene furlough2
    with dissolve

    a "What does that mean? I’m pretty sure Maya is younger than you and it’s not exactly like she leads a very exciting life."
    m "Hey."
    ay "What’s more exciting than immortality?"

    scene furlough3
    with dissolve

    a "Are you immortal now? Or is this just one more inside joke between you, Ayane, and Sensei that I am not a part of because you are slowly removing me from both the Love Squad and your lives?"
    m "I have no interest in the “Love Squad.” I simply wanted to share an opinion of mine. But if me having thoughts is going to be the cause of so many problems, I’ll just go back to being quiet."

    scene furlough4
    with dissolve

    a "So, what’s the plan now?"
    a "I was thinking we could stop at that cafe with all of the cool parfaits again. But if nobody else is hungry, we can always just go back to my house and play games or something."
    ay "Oh, yeah. About that. I forgot to tell you- I actually wound up making plans with somebody else today, so you guys can head over to...wherever without me."

    scene furlough5
    with dissolve

    a "Other plans? But we always go home together if we’re still around when our clubs finish meeting."
    ay "And I’m sure we’ll continue to do that in the future! I just can’t today. Sorry, Ami."

    scene furlough6
    with dissolve

    a "Man. I was really hoping we’d get to use your black card. I always feel so important whenever we get to pay with that. "
    a "Oh. What I actually meant to say there is that I will miss you and hope that whatever plans you made with someone I can only assume is Sana go well."
    s "Everything alright? It’s one thing to not provide the intro, but bailing on everyone isn’t exactly in-character for you."
    ay "Mhm! Everything is totally cool. Just have a couple loose-ends I need to tie up before leaving school today. But I’ll meet up with you guys again once it’s all over."
    a "Well...have fun, I guess. The three of us will probably just go home if you’re not coming since I don’t want to have to share a parfait with Maya. She’ll eat it all. And Sensei doesn’t eat anything “cute.”"
    s "It’s true. I have to remain masculine at all times or people won’t take me seriously anymore."

    scene black
    with dissolve2
    stop music fadeout 15.0

    ay "I guess I’ll just wind up seeing you all back at Ami’s house, then! Bye bye!"

    "{i}Four becomes three as Ayane wanders away from those she loves the most.{/i}"
    "{i}It is not the only example of numbers becoming numbers in recent memory, but it is the one I am contractually obligated to inform you of right now.{/i}"
    "{i}But where is she going, I wonder? And what or who will she find when she gets there?{/i}"
    "{i}A snake? A rabbit? A bat? A cat?{/i}"

    play sound "static.mp3"
    scene furlough7
    with flash
    stop sound
    play music "pianomelancholy3.mp3"

    "{i}Or the human embodiment of a trash can pretending to be sentient as it leans against the hood of a stranger’s car and thinks to itself about why sexual assault is okay so long as the majority of parties orgasm.{/i}"
    "{i}Anyway, I’m done here.{/i}"
    "{i}I don’t want to stick around for this.{/i}"

    ki "Hey. I was beginning to think you weren’t going to show up."
    ay "I wouldn’t have asked to meet you here if I was planning on ditching. Not all of us thrive on the amount of inconveniences we cause for those around us."
    ki "Well, you know me. The “amount of inconveniences I cause for those around me” is what gets my motor running in the morning."
    ki "And yet, despite that, I still took the time out of my extremely busy practice schedule to see you today. I’m such a good friend, aren’t I?"
    ay "Don’t give me that shit. We haven’t been friends in a long time."

    scene furlough8
    with dissolve

    ki "Hmm...when did our friendship end again?"
    ki "Was it the time you came all over my hand at the beach house? Or was it the time we treated Sensei’s cock like a giant lollipop together?"
    ki "Come to think of it, it was probably the first time since you weren’t even wet when I tried to put my fingers in during the Dorm Wars. And that’s just plain unfriendly."
    ay "Are you done?"

    scene furlough9
    with dissolve

    ki "I can be. Though, I’d be lying if I said I wasn’t a {i}little{/i} hopeful that the reason you called me out here today was to organize our next threesome."
    ki "Or twosome. I’d let you fuck me alone if you want. Or vice versa. See, I’ve been practicing this thing with my tongue where-"
    ay "We’re done."

    scene furlough10
    with dissolve

    ki "{i}Done?{/i}"
    ay "It’s over. I’m not letting you hold my life hostage anymore."
    ay "You want to keep seeing Sensei behind my back? Fine. But I’m done letting you come between us. "
    ki "Yeah, here’s the thing. That’s not really up to you, sweetheart."

    scene furlough11
    with dissolve

    ay "Don’t call me “sweetheart,” you fragile little bitch. We both know you’re overcompensating for how insignificant and unneeded you feel right now."
    ki "Ooooh. Where’d this side of you come from? It’s kind of turning me on."
    ay "Do me a favor and kindly fuck off for the rest of forever, please. I don’t have time for this anymore."
    ki "You don’t? What changed?"
    ay "Kirin."
    ki "If you’re worried about Sensei falling for {i}me{/i} instead, don’t. Like you said, I’m “insignificant” and “unneeded.”"
    ki "But I’m a great receptacle for his semen since he always seems to like it when I wrap my legs around him and make it so he can’t pull out."

    scene furlough12
    with dissolve

    ki "Oh, but don’t worry about me getting pregnant. I’m on birth control, so he can cum inside of me as much as he wants and everything will be totally fine!"
    ki "In terms of actual raw, {i}love{/i} though...don’t worry. I’m just not that type of girl."
    ay "Fantastic. Can I take that as you agreeing to simply fuck him while I’m not around then? Or are you still going to try and drag all three of us under the sheets together?"

    scene furlough13
    with dissolve

    ki "Hmm...depends on how horny I am, I guess. Just Sensei won’t always do it for me, you know. I like having you around as well. "
    ki "You do this cute, little...high pitched yelp thing whenever you’re feeling good that makes me a lot hotter than any cock ever has, that’s for sure."
    ki "I’m just not sure if I’m ready to give that up. Nor do I understand why I’d {i}have{/i} to just because you decided to finally stand up to me."

    scene furlough12
    with dissolve

    ki "{i}Why{/i} you decided to stand up to me, I’m not sure. It’s not like having you point out my flaws and cry about how you don’t like me touching you is going to make me magically not want to do it anymore."
    ki "Remember, Ayane- you’re the one who agreed to this little...{i}arrangement{/i} in order to protect Sensei."
    ki "If you’re going to try and back out of it, nothing’s stopping me from just telling everyone about the two of you and ruining {i}both{/i} of your lives once and-"

    play sound "static.mp3"
    scene furlough14 with flash
    stop sound

    ay "Do it."
    ki "Huh?"
    ay "Fucking do it. I dare you."
    ay "Ruin our lives."
    ay "Tell the world about us and see what happens. Sensei will love me just the same."
    ay "But you? "
    ay "You’ll never know what it’s like to feel what I feel. To feel any amount of love at all."
    ay "So stop fucking chasing it, you hear me?"
    ay "Don’t you fucking dare ruin {i}my{/i} time with him because you’re so desperate for a taste of affection that you’d sooner drink it from my pussy than take a second to {i}grow the fuck up.{/i}"
    ki "The fuck is this? Since when are you this aggro about literally anything?"
    ay "I told you. I don’t have time for this anymore."
    ay "And I’m not going to let you fuck up what little time I may have {i}left{/i} with your petty insistence on being there during our most private moments."
    ay "You want to tell everybody about it? Go ahead. Because I’d sure as fuck prefer being called a whore over having to spend one more second around your filthy fucking cunt."

    scene furlough15
    with dissolve

    ki "And Sensei’s career? You’re suddenly fine with throwing {i}that{/i} in the trash if it means the two of you get to fuck each other more privately from now on?"
    ay "Mhm. "
    ki "See! So you {i}don’t{/i} want-"

    scene furlough16
    with dissolve

    ki "Wait, what?"
    ay "I don’t think {i}shit{/i} will happen to Sensei’s career. Nor do I think you have the balls to actually {i}tell{/i} anyone about this. {i}Nor{/i} do I think anyone would believe a thirsty, jealous bitch like you."

    scene furlough17
    with dissolve

    ki "You’ll regret saying that to me, you know. I might not be as popular as you, but people will still believe what I-"
    ay "The only thing I regret is letting things get to this point in the first place. "
    ay "If I had known back then what I know {i}now,{/i} I would have hopped off his dick and slammed that door right in your fucking face."
    ay "You should have been stuck outside of it like the fucking parasite you are...thriving off of what the two of us were doing together because you know damn well you’d die on your own."
    ki "Parasite?..."
    ki "Well..."
    ki "Well at least I don’t have a fucking daddy complex that drove me to fucking my teacher in the first-"

    play sound "static.mp3"
    scene furlough18 with flash
    stop sound

    ki "NGH-?!"
    ay "Why {i}would{/i} you? Your parents don’t even {i}like{/i} you. That’s why they spend all of their time and energy on Karin instead."
    ay "So what if Sensei stepped in when my dad started neglecting me? So what if he filled a role I desperately needed someone to fill? We’re in love now and that’s all that matters."
    ay "Meanwhile, you’re so fucking desperate for attention that I bet you’d let your {i}actual{/i} father fill that loose cunt of yours if it meant making you feel alive for a fraction of a second."

    scene furlough19
    with dissolve

    ki "Let...go..."
    ay "Shut the fuck up. I’m barely even squeezing."
    ki "You think you’re...so much better...than me!"
    ay "Of course I do. I {i}am{/i} better than you. "
    ay "I don’t get off on hurting people. I {i}accept{/i} the parts of myself I’m not comfortable with. "
    ay "All {i}you{/i} do is involve yourself in everyone else’s issues because the ones {i}you{/i} have are so uninteresting and petty that they’re barely even {i}issues{/i} at all."
    ay "Get over yourself, Kirin. It’s very sad. "
    ay "But what’s even sadder is that, when I let go, you’re probably going to tell me that you {i}still{/i} refuse to leave Sensei and me alone."
    ay "But that wouldn’t be very good for you because, if you haven’t been able to figure it out so far, {i}I don’t give a shit anymore.{/i}"
    ay "And I can ruin your life a hell of a lot easier than you can ruin mine."

    scene furlough20
    with dissolve

    ki "S..."
    ay "..."
    ki "S...S-"
    ay "Stop?...Sensei?...Sorry?..."
    ay "What are you trying to say? Speak up."

    scene furlough21
    with dissolve

    ki "S..."
    ki "Science...fair!"
    ay "..."

    scene furlough22
    with dissolve

    ay "Heh?"
    ki "The...science fair!"
    ki "This...never would have happened if...you just...didn’t beat me!"
    ay "..."
    ki "You ruined...everything! I finally...could have...made my parents...proud of me!"

    scene furlough23
    with dissolve

    ki "If that never happened...I never would have wanted revenge...I never would have started watching you...being jealous of you..."
    ki "It’s all because you ruined the {i}one{/i} thing in my life that I felt like I did well! You ruined it!"
    ay "..."
    ki "..."
    ay "Are you fucking kidding me?"

    scene furlough24
    with dissolve

    ki "It’s not funny!"
    ay "You...tried to ruin my life...over the fucking {i}science fair?{/i}"
    ki "You...You ruined mine first! You-"

    scene furlough25
    with dissolve

    ay "Hah...hahah...hahaha..."
    ay "Hahahahahah!"
    ki "Why are you laughing? It’s not-"

    scene furlough26
    with dissolve

    ay "I'm laughing because you’re a fucking joke."
    ki "I’m not a joke. Just because I’m not as lucky or gifted as you doesn’t mean I-"
    ay "No. You’re seriously a fucking joke. "
    ay "And if you ever try to come between Sensei and me again, I will snap your trachea like a twig."

    scene furlough27
    with dissolve

    ki "D...Don’t laugh at me! Ayane!"
    ay "I wonder if Sensei and the others are back at home yet? I might still be able to catch up if I start running."
    ki "Pay attention to me! This is serious!"

    scene furlough28
    with dissolve

    ay "What’s so serious about you wanting attention? That’s literally all you ever do. It’s pathetic. {i}You’re{/i} pathetic. Trash. Worthless. Scum. Go fuck yourself."
    ki "I just...I just wanted to feel like I-"
    ay "I don’t care."
    ay "In fact, I kind of wish you were dead."
    ay "Now, if you’ll please excuse me, I am going to go hang out with a group of people who enjoy my presence. Which is, coincidentally and quite hilariously, something you will never be able to do."
    ki "There are...people who-"
    ay "No. "
    ay "There really aren’t, Kirin."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "{i}I heard from someone else that things went better than I thought they would.{/i}"
    "{i}How ironic.{/i}"
    "{i}I’ve grown so used to the slow burn of divine comedy that any punchline dissimilar to the feeling brought on by fiery coals beneath my feet is like an ice pack for an aneurysm.{/i}"
    "{i}It helps, but just slightly enough to distract me from the fact that everything is horrible and that it will all be over soon.{/i}"
    "{i}Or at least it would be in most cases.{/i}"
    "{i}The cycle would see otherwise.{/i}"
    "{i}But it seems the cycle can’t see at all.{/i}"
    "{i}For if it could, none of this would happen.{/i}"
    "{i}For if it could, things would never change.{/i}"
    "{i}It’s so interesting that they finally are.{/i}"

    $ renpy.end_replay()
    $ ayanekirintalk = True

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayanespecial55:
    scene ayanegamenight1
    with dissolve2
    play music "10c.mp3"

    ay "Oh! Oh! What is the “echidna!”"
    a "What {i}is{/i} the echidna? It sounds made up."
    m "Apparently, it is an egg-laying mammal without teeth. As for why Ayane knows that, I have no idea. But she’s gotten more than half of these questions correct so far, so I’m not exactly surprised."

    "It’s another Saturday night at my place. And for the first time in what feels like forever, the three girls I hold closest to my heart are together and bonding."
    "And I use the word “bonding” loosely because the majority of the night has consisted of them shouting words at my television and keeping the neighbors that I probably have awake."
    "Come to think of it, it’s a little strange that I’ve never once interacted with anyone in any of the surrounding houses. But I guess it’s probably better off that way."
    "The fewer people I know, the better."
    "Unless, of course, those people are attractive (And likely pubescent) teenage girls who dream of riding my penis. But, I repeat, I’m probably better off not knowing them for reasons I’m sure you can understand."
    "As for these ones, though...I’m glad I {i}do{/i} know them."
    "Knowing Ami is inevitable given our blood relation and whatnot. But I can’t even fathom what life without Maya or Ayane would be like."
    "On one hand, I’d have a lot more free time — and I’d never have to worry about things like the size of the moon or where to put my hands when hugging on a rooftop."
    "But, on the other, I’d lack the household harem that has provided me so much comfort when you strip away all of the anguish that rides in on their shoulders."
    "I am home. In more ways than one."
    "And I intend to stay here for as long as I can."
    "Because these days, while uncertain and burdensome-"
    "Are the best days I have ever had."
    "Praise be."

    scene ayanegamenight2
    with dissolve

    a "Can we maybe play something else soon? I’m starting to get a little tired of Ayane’s weird internal bank of useless knowledge."
    ay "It clearly isn’t useless if it’s coming in handy tonight, right? Without my weird internal bank thingy, we’d just be watching some old guy on the TV ask a bunch of questions none of us know the answers to."
    m "What is “Sirius.”"

    scene ayanegamenight3
    with dissolve

    a "Like the radio? What was the question? I might have actually known that one."
    m "This star, in Canis Majoris, is the brightest in the night sky."
    a "The heck does that have to do with the radio?"
    ay "Wow, Ami. You’re {i}seriously{/i} bad at this game, aren’t you?"

    scene ayanegamenight4
    with dissolve

    a "..."
    m "..."
    ay "Get it? Like...{i}Sirius.{/i}"
    s "Okay. I’m going to sleep."
    m "Yeah, I think I’ve also reached my horrible joke limit for the night. And every single one of them just so happened to come from Ayane."
    ay "Don’t hate the player, Maya. Hate the game."
    a "I hate the game. We’re playing Wii Sports next sleepover and I don’t care what anyone says."

    scene ayanegamenight5
    with dissolve

    a "But, on that note, I guess it’s time we take baths. It’s getting pretty late anyway."
    m "I feel like that’s a thing we should have done {i}before{/i} putting our pajamas on. This was not an effective order of operations."
    ay "You two can go ahead. I’ll hang out here with Sensei in the meantime and finish up Jeopardy with him."

    scene ayanegamenight6
    with dissolve

    a "Oh! Instead of that, how about {i}I-{/i}"
    ay "Nope! You can go on ahead, Ami. I’m perfectly capable of hanging out in the living room without making love to your uncle. I’ve been doing it for years."

    "Huh."
    "Come to think of it, I guess we {i}haven’t{/i} had sex in the living room yet."

    scene ayanegamenight7
    with dissolve

    a "Uhh..."
    m "You do know that all three of us should be able to- never mind. I just realized what’s going on here. But good luck getting Ami to agree to-"

    scene ayanegamenight8
    with dissolve

    a "{i}Hah...{/i}fine."
    m "Wait, seriously? You’re not going to, like...sew your skin to Sensei’s or tie him up and drag him into the bathroom with us?"
    a "No...I’m pretty sure those things fall under “suffocating” and I told Sensei I’d be good from now on. Let’s just go take our stupid bath without Ayane."
    m "What the fuck is going on tonight? "
    ay "What’s going on is Ami is learning to be less clingy and we should all be very proud of her! Hooray for Ami!"

    scene black
    with dissolve

    a "Hooray my butt! You know darn well I’m doing this against my will. Come on, Maya."
    m "You don’t have, like...surveillance cameras anywhere, do you? Because I can’t imagine any other reason you’d so easily accept-"
    a "I said come on!"
    m "Jesus, chill. The bath’s not even warm yet."
    ay "Sensei! Couch!"

    "........."
    "......"
    "..."

    scene ayanegamenight9
    with dissolve2

    "Ami and Maya head into the bathroom and, in between wondering why it’s totally normal for girls to do things like this, I find a moment to savor this newfound peace and quiet."
    "But that’s not without the mildly worrying caveat that there must have been some sort of catalyst needed to get here."
    "I know Ami better than anyone. Even more so than Maya and Ayane. So why is it that Ayane is suddenly able to seize me without any sort of repercussion?"
    "This can’t just be the result of Ami actually taking my words to heart, can it?"
    "I’ve said plenty of {i}words{/i} to her since waking up in my own body again, and her heart has gone entirely unchanged up to this point in time."

    s "..."
    ay "..."

    "Maybe she’s like me?"
    "Finally changing."
    "Finally attempting to look forward instead of glancing over her shoulder every five seconds."

    s "..."

    "Or maybe it’s something else?"

    ay "Sensei..."

    "All I know is that, whatever it is...might just be the single most worrying thing I’ve ever seen from my beloved niece."
    "Who would never hurt anyone."

    ay "I missed you."

    "Who would never hurt anyone."

    ay "I’m glad to be back."

    "Especially me."

    s "What do you mean by “back?” You haven’t gone anywhere."

    scene ayanegamenight10
    with dissolve

    ay "Maybe not {i}physically.{/i} But mentally, I’ve been in a pretty bad place for a while now. And I’m just starting to snap myself out of it."
    s "Things like that wouldn’t happen if you’d stop being such a martyr, you know. "
    ay "Martyrs die. And I’m not going anywhere ever again."
    s "None of us are. None of us {i}can.{/i} What I meant is that you’d have less mental voyages if you’d get better at talking about your problems."

    scene ayanegamenight11
    with dissolve

    ay "That’s really funny. Coming from you, I mean."
    s "I’m aware that I could benefit from the same thing. I’m just too caught up in my ways at this point."
    ay "You and Maya both. Kudos to me for being the mature and logical one in the group. I bet nobody saw that coming."
    s "Careful or Makoto might gun for your position. I’m pretty sure her biggest fetish is {i}logic.{/i}"
    ay "Do you think she’ll still be “around” after the next reset? Or do you think she’ll go back to not knowing how any of this stuff works?"
    s "None of us know how any of this stuff works. Which includes me not having any clue what will or won’t happen to Makoto."
    s "I’m just trying not to get my hopes up. I did that with Yumi and Tsuneyo and that didn’t pan out how any of us wanted. So expecting nothing will-"
    ay "Be the best way to avoid getting hurt. You’re right."
    ay "I’m doing the same thing. Or...trying to, at least. "
    ay "The problem with hope is that it always finds its way in whether you want it to or not. And there’s no way any of us could be, like...immune to that."

    scene ayanegamenight12
    with dissolve

    s "You seem a little...{i}reflective{/i} tonight. Did something happen?"
    ay "Of course something happened. I’m not nearly strong enough to break free from inner turmoil without {i}something{/i} causing it."
    s "I don’t think you’re giving yourself enough credit, Ayane. You’re one of the strongest people I know."
    ay "And I just got a whole lot stronger."
    s "Meaning...what, exactly?"

    scene ayanegamenight13
    with dissolve

    ay "Unfortunately, I promised I wouldn’t tell you. It’s nothing but good news, though. For me, definitely. And...for {i}all{/i} of us, I think. But that last part is more of an expectation than actually {i}knowing.{/i}"
    s "So...you’re just going to tell me you had some intense inner struggle that you’ve now recovered from, but won’t provide any of the details and I have to just...go along with it?"
    ay "Yeah."
    s "Well, that’s fun."

    scene ayanegamenight14
    with dissolve

    ay "Trust me when I say that hearing the details would just make things even more confusing. And that’s exactly what I’m trying to {i}avoid{/i} right now."
    ay "We’ve been looking at things all wrong. Worrying about {i}how{/i} things work instead of {i}why{/i} the world is like this."
    s "Do you know {i}why{/i} the world is like this, Ayane?"

    scene ayanegamenight15
    with dissolve

    ay "What I know is that I love you."
    s "{i}Everyone{/i} knows that. It’s not exactly a revelation."
    ay "No. But it’ll be my crutch again as both of us begin a new chapter of our lives."
    s "And that chapter is what?"
    ay "One without fear. "
    ay "One where {i}we{/i} come first and the world comes second."
    ay "I have eternity to spend with you. That’s lifetimes and lifetimes worth of happiness and laughter and the backwards spider crawl."
    s "I still haven’t figured out what that is."
    ay "Neither have I. But the point is that we can figure it out {i}together.{/i}"
    s "I’m not really sure what you’re saying, Ayane. Is this, like...a resignation from the Rooftop Apocalypse Squad?"
    ay "It sounds kind of weird hearing you call it that."
    s "It feels kind of weird saying it."
    ay "Sensei, I’m not resigning from anything. And I’m honestly not sure if I even {i}could.{/i} "
    ay "I’ll still be on that roof with you and Maya. And maybe Makoto. But it’ll be a better me."
    ay "I’ll be an Ayane you can lean on."
    ay "And I’ll protect you from anything and everything that would ever want to hurt you."
    s "Do you...know something that might want to hurt me?"

    scene ayanegamenight16
    with dissolve

    ay "Other than yourself? It’s hard to say. But...let me ask you this."
    ay "What do you think of the way Ami’s been acting lately?"
    s "Honestly?..."
    s "It’s concerning."

    scene ayanegamenight17
    with dissolve

    ay "Isn’t it? She seems all cute and cuddly on the outside, but she can be a real {i}monster{/i} on the inside sometimes, can’t she?"
    s "She’s doing it out of love, though."
    ay "Is that what you actually think? Or is it something she’s just said so many times now that you can’t help but accept it as truth?"
    s "It’s what I actually think. But a better question is what happened between you two where she’s suddenly no longer combative against your attempts to steal alone time with me?"
    ay "I did what any friend would do. I talked to her. "
    ay "I called her out on all of the things she does that piss me off and I told her I wouldn’t stand for them anymore."
    s "And she just...accepted that?"
    ay "Only time will tell."
    ay "But I have a good feeling she did."
    ay "And I have a good feeling she won’t be getting in the way of us as much as she used to. "

    scene ayanegamenight18
    with dissolve

    s "Well...I hope you’re right. About everything."
    s "I’m not sure if I’ll be able to just stop worrying about stuff the way you have...but whatever it is that’s helped you feel better, whether that be your talk with Ami or anything else that may have happened..."
    s "I’m glad."
    s "I missed the happier version of you."
    ay "Same here. Life’s been on a constant downward spiral ever since that half-year stretch where we weren’t allowed to have sex. I’m glad things are finally turning around."
    ay "And also, we should have sex."
    s "Like...Like {i}now?{/i}"

    scene ayanegamenight19
    with dissolve

    ay "Don’t know. Think my new sway with Ami will get her to agree to the two of {i}us{/i} taking a bath together next?"
    s "I’m not sure if there’s anything in the world that could get her to agree to that..."

    scene black
    with dissolve2

    ay "Neither am I."
    ay "But just this is enough for now."
    ay "Even if I know she hates it."

    "........."
    "......"
    play sound "water1.mp3"
    "..."

    scene ayanegamenight20
    with dissolve2

    a "That gosh darn bubblewrap princess. She’s lucky I’m in such a good mood tonight."
    m "Question. Why {i}are{/i} you in such a good mood tonight? That was the least...{i}aggressive{/i} I’ve ever seen you when it comes to cock-blocking Sensei."

    scene ayanegamenight21
    with dissolve

    a "Don’t call it that. Calling it that makes it sound like the two of them are getting up to no good out there."
    m "For all we know, they are. They’re both insatiable. I wouldn’t put it past them."

    scene ayanegamenight22
    with dissolve

    a "Sensei is not {i}insatiable.{/i} He’s just a pervert with unsophisticated taste. Or...sophisticated taste if it’s in relation to me. But it’s normally not, so..."
    a "He’s just a pervert."
    m "If that’s what helps you sleep at night, Ami."

    scene ayanegamenight23
    with dissolve

    a "What about you, Maya?"
    m "What {i}about{/i} me?"
    a "I mean...how do {i}you{/i} feel about Ayane getting to spend alone time with Sensei while the two of us are stuck in here?"
    m "Um...normal?"
    a "You’re not even a little jealous?"
    m "What would I have to be jealous of?"
    a "The pervy stuff that might be happening."

    scene ayanegamenight24
    with dissolve

    m "I couldn’t be any less interested in that sort of thing if I tried."
    a "You can be honest with me, Maya. I won’t get mad. I’ve already accepted that everyone in our class is constantly fantasizing about Sensei because he’s the perfect man."
    m "You have an expectedly horrid definition of the word “perfect.”"
    a "As long as it’s just fantasy, you can do whatever you want. It’s only when it becomes real that it’s a problem."
    a "You could even think of me if you want. "

    scene ayanegamenight25
    with dissolve

    m "Okay, seriously, what is going on with you? You’ve been weird ever since we got back from the beach."
    a "And Ayane hasn’t?"
    m "You {i}both{/i} have. But Ayane hasn’t outright told me that she wouldn’t care if I sexually fantasized about her."
    a "It probably just hasn’t come up yet."
    m "And it probably won’t because it’s weird."
    a "It’s not {i}that{/i} weird. What {i}is{/i} weird is how sexually open our entire class seems to be despite all of us being teenage girls. Or how every single one of us is absolutely adorable."
    a "Or how our class has its own dorm building. Or how the weather suddenly isn’t as hot as it’s supposed to be."

    scene ayanegamenight26
    with dissolve

    a "Or how the sidewalk just ends and drops off into nothing sometimes, but no one ever says anything about it."
    a "There are millions of things we can see that we don’t speak of because it would ruin something bigger."
    m "Ami...what are-"
    a "It’s only when it becomes real that it’s a problem. Right, Maya?"
    m "Only when..."
    m "{i}What?{/i} I have no idea what you’re trying to-"
    a "Just keep it all a fantasy...okay?"
    a "Can you do that?"

    scene ayanegamenight27
    with dissolve

    m "Could you let me go now? I’d kind of like to pay a visit to the other side of the bath."
    a "But I’ll get lonely if you’re gone."
    m "Then...get lonely. You’re weirding me out."

    scene black
    with dissolve2

    a "Psht...fine. And here I was thinking we were about to have a cute bonding session."
    m "We can bond from opposite ends of the bath..."

    $ renpy.end_replay()
    $ ayanespecial55 = True
    $ ayane_love += 1
    stop music fadeout 7.0

    if ayanecthree == False:
        $ ayanebonus1skip = True
        $ ayanebonus2skip = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayanebonus1:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Ayane’s door and wait for her to answer."
    "And, after spending at least fifteen minutes thinking about all she said regarding the way we’ve been looking at the world the other night, I’m ready to spend {i}this{/i} one free of worry."
    "I’m ready to get back to the way things have always been between us."
    "Just a man, a girl, and that man’s penis {i}inside{/i} of that girl."
    "It’s simple, really. But we get caught up in other things and forget that sometimes."

    ay "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I don’t want to forget anymore."
    "I want to confront this world head-on."
    "I want to put my penis inside of that girl."
    "And no matter what tragedy queues up to assault us next, I won’t care. "
    "The darker side of life is always just a step or two behind me. But there is a light inside of this room that will scare it away."
    "Even if it’s only for a little while."

    scene ayanebedtalk1
    with dissolve2
    play music "meanttobe.mp3"

    "The aforementioned light is a faint pink glow leaking out of a thick plastic bulb, nestled atop one of four columns that keep a second roof over Ayane’s head when she goes to sleep at night."
    "The room smells like a combination of fresh laundry and meticulously suppressed sorrow and, I am well aware that the latter is not something that can appeal to the sense in question-"
    "But if it could, it would be something like this."
    "If it could, it’d be something that goes well with fresh laundry or a night under a dying pink light. "
    "It would be soft — like a pure, white pillow or the fabric of a young girl’s pajama pants. "
    "Or her skin. "
    "Or her long, blonde hair."
    "Or her hands as her fingers curl around yours and subtly remind you of how much bigger than her you are in a manner that is mildly predatory, but partially pure when carefully refined by a novice heartsmith. "
    "It matches the pillow. You think that to yourself."
    "You take a step back because you’re worried about trampling such a delicate, precious flower. But a second glance at its petals reveals that it has already been trampled time and time again. And still, it rises."
    "Still, it lives to see the faint pink light of day as imaginary clouds take tiny bites out of a blue sky that reminds you of the color of her eyes. The same eyes you find yourself drowning in as we speak."
    "There are no words, just a prolonged duel between irises — silently trying to infect what they focus on, but helplessly bouncing off of one another because this is impossible."
    "This is love."
    "And it’s a love you never thought you’d know."
    "But a flicker of the light distracts you from that realization."
    "The imaginary clouds consume the imaginary sky, and you’re left in the same room where you first trampled that flower."
    "Long before you knew it would rise again."

    ay "Sensei."

    "Will you trample it once more?"

    s "Yeah?"
    ay "I’m glad you’re here."

    "Of course you will."
    "Because you’re pathetic."
    "You’re worthless."
    "And you do not deserve these prolonged glares or pure, white pillows."
    "Or soft skin or blonde hair or a blue sky or {i}anything{/i} because we all know you’re just a cicada."
    "And you crawled your way out of the earth with the rest of them."
    "The aforementioned light flickers once more."
    "And a reprieve from an unwelcome happiness carves its name on the tree that is your heart."

    s "And {i}why{/i} are you glad, Ayane?"
    ay "Because I love you, of course. Why {i}wouldn’t{/i} I be glad that you’re here?"
    s "Because I know you well enough at this point to understand when something is wrong even when you refuse to admit it. "
    ay "But Sensei, we {i}just{/i} had a discussion about how I’m all better now. And that I wouldn’t let anything bother me anymore so I could spend more time being the crutch you need to walk the streets of Kumon-mi."
    s "And yet you’re already backtracking."

    scene ayanebedtalk2
    with dissolve

    ay "I have no idea what you’re talking about. But I suppose it’s possible you might be confusing me with my evil twin sister, Efrosinia. That happens sometimes."
    s "Then, does this {i}Efrosinia{/i} have anything she’s hiding from me?"
    ay "She’s hiding all sorts of things. She’s a spy. That’s her job."
    s "You realize I’m not going to hold it against you for not being unmistakably happy 100%% of the time, right?"
    ay "Right. But {i}I{/i} will hold it against me as I literally {i}just{/i} went on a huge rant about how the world is my oyster and you are my pearl. I should wait a little longer before giving myself a sadness allowance."
    s "A...sadness allowance?"

    scene ayanebedtalk3
    with dissolve

    ay "One emotional breakdown per month. Conducted privately, of course. So as to not disrupt your daily schedule. But the rest of the time, I’ll be the good ole, happy-go-lucky Ayane. The one you love!"
    s "I love every Ayane."
    ay "Even Efrosinia?"
    s "Even Efrosinia."

    scene ayanebedtalk4
    with dissolve

    ay "That was the wrong answer, Sensei. You just admitted to sleeping with my made-up twin sister. Now we’re going to have to go to made-up divorce court so I can collect my made-up alimony."
    s "Talk to me."
    ay "I {i}am{/i} talking to you."
    s "Talk to me {i}about whatever is bothering you.{/i}"
    ay "That is a bad idea."
    s "But {i}why{/i} is it a bad idea? I can’t help you if I don’t know."
    ay "You can’t help me because it’s {i}your{/i} fault in the first place. That’s why I decided to just suck it up and suppress it."

    scene ayanebedtalk5
    with dissolve

    ay "But of course you managed to see through it. And here I thought I was doing a good job."
    s "It’s something {i}I{/i} did? What?"

    scene ayanebedtalk6
    with dissolve

    ay "It’s nothing. Don’t even worry about it. Even {i}I{/i} forgot about it for a little while. "
    ay "But that’s probably just because a bunch of other, more extravagant things went down right after and I’m still in disbelief that this is even a thing I have to confront in the first place."
    s "Well, on that note, if your method of confronting it is acknowledging it and then ignoring it, I should both commend you and scold you for tackling things the same exact way I would."

    scene ayanebedtalk1
    with dissolve

    ay "Thanks and understood. I’ll take some time to rethink my approach for future confrontations once I’m done being mad at you. "
    s "Is there anything I can do in the meantime to assist with that?"

    scene ayanebedtalk2
    with dissolve

    ay "You know, as a matter of fact, there is. But revealing that to you is exactly what I’ve been trying to avoid in-"
    s "Chika talked to you, didn’t she?"

    scene ayanebedtalk7
    with dissolve

    ay "..."
    s "..."
    ay "Oh."
    ay "So you already knew."
    s "I had a feeling that had to be it. I don’t think I’ve made any other big mistakes involving you recently."

    scene ayanebedtalk8
    with dissolve

    ay "{i}Hah...{/i}"
    s "Ayane-"
    ay "This is a sit-down conversation, Sensei. If we’re going to talk about something that makes me extremely {i}un{/i}comfortable, I’d at least prefer to do it in a comfortable spot."
    s "The bed’s right behind you. And I’d be happy to discuss this at length if it helps clear things up."
    ay "Yeah...I bet you would."

    scene black
    with dissolve2

    "That aforementioned light from moments ago dims as I move beneath it. And while I’m sure that just means my eyes are taking in less of it, I like to think that it’s changing for me."
    "That it sees me as undeserving of its warmth or vibrancy. That it’s conserving its color for the one who sees it most."
    "The one who has never done anything wrong, yet continues to be trampled because she bloomed in the wrong garden."

    scene ayanebedtalk9
    with dissolve2

    "But I can not pluck this flower as its stem is too tightly rooted to the ground of my inadequacy."
    "And I can not look away as it's far too beautiful."
    "All I can do is try to avoid stepping on it in the future — but this entire field is full of flowers."
    "And anywhere I go, I’ll be trampling something."

    ay "Are you going to start or should I?"
    s "I’ll start."
    ay "Good. That was the right answer."
    s "Guess it’s not just Ami you’re not taking any nonsense from anymore, huh?"
    ay "I’m tired of being stepped on. And if I’m going to get caught up in a never-ending time loop, I need to stop letting that happen or my life is going to be miserable. And that extends to you as well, Sensei."
    ay "You’re not exempt from my wrath just because I love you. I still have feelings, you know. I’m not some girl you can just sacrifice to make your life easier and-"
    s "I said I’d start."

    scene ayanebedtalk10
    with dissolve

    ay "Sorry...go ahead."
    s "Well...as you know, I’m {i}involved{/i} with a number of girls."
    ay "That’s putting it lightly."
    s "It seemed more gentle to put it that way than outright saying I’m fucking a sizable portion of the class. But if you want me to be more brutally honest, I will."
    ay "Fine by me. I can take it at this point."
    s "When Chika came to me about this, I was probably just as shocked as you were when {i}you{/i} first found out."
    s "You obviously don’t know all the details of our relationship, but Chika is extremely possessive and-"
    ay "Everybody and their mother knows that. It’s just {i}me{/i} who has the fortune of knowing you’re sleeping with her."
    s "You’re not the only one who knows that, Ayane."
    ay "Oh, okay. So I’m just the first one in line for the threesome. Got it."
    s "There is no {i}line.{/i} Now, let me finish."
    s "When Chika came to me, I was shocked. I didn’t think she’d be the one to propose something like this when she’s more or less looked at every other girl the same way Ami has in regard to me."
    s "And, I know how this is going to make me sound, but that’s not really an opportunity I wanted to just give up."

    scene ayanebedtalk11
    with dissolve

    ay "Of course not. You think with your penis. I just kind of figured your penis would care a little more about my feelings on account of how well it knows me by now."
    s "It does. {i}I do.{/i} And I get that you and Chika aren’t really close or anything, but I still wanted it to be you."

    scene ayanebedtalk12
    with dissolve

    ay "Do you have any idea how that makes {i}me{/i} feel? It’s hard enough just knowing that I have to secretly share you with everyone. But having one of them come up to me and rub it in my face?"
    ay "Do you have any idea how degraded that made me feel? Do you know what it was like being looked down on like that? And having you held in front of my face like some kind of carrot on a stick?"
    s "No. I don’t have any idea how any of that feels. Just like I had no idea how it must have felt when you read the list I gave you for the first time."
    ay "Then why-"
    s "Because it felt wrong hiding even more from you after you showed me just how much you value my honesty. "
    s "I wrote you that list because I care about you. And I never thought for a second that it would be something you’d just gloss over and forget about."
    s "If there’s an option, I want you to be involved. And this was a way to do that without outright telling the world that I’m in love with you."

    scene ayanebedtalk13
    with dissolve

    ay "I...I get that. But that feels like too convenient of an excuse and...and I know there has to be to more to it than that."
    ay "Chika thinks you two are super serious...and that you’re this masterpiece of a man who’s fully committed to her and no one else. But that’s not who you are at all."
    ay "You don’t care about loyalty. You don’t care about exclusivity. You’re practically {i}allergic{/i} to commitment. And those are all things {i}I{/i} know because I love you and accept you despite all of that."
    ay "But Chika?..."
    ay "It’s like..."
    ay "It’s like she has no idea who you even are."
    ay "Who is she so in love with? What kind of mask are you wearing when you’re with her?"
    s "The Chika situation spiraled out of control before I could do anything about it."
    ay "You could have, you know, {i}not{/i} had sex with her. That might have helped."
    s "But I {i}like{/i} having sex with her. And I like having sex with you. And I get that I’m disgusting for suggesting you to her, but {i}you{/i} were the one I wanted."

    scene ayanebedtalk14
    with dissolve

    ay "That...hold on. I feel like you’re kind of just sweet-talking me here. There’s no way that’s all it was. "
    ay "You probably just...you probably think I’m the {i}safe{/i} option because I already know about her and- "
    s "I already told you. You’re not the only one who knows about her."
    ay "Then...you might have thought I’d be the first to agree since I’d do anything for you and-"
    s "I just wanted it to be you, Ayane. "
    s "I can’t say for certain there wasn’t more that went into the decision, but the important part is that I wanted you there for it."
    s "I can be with you in front of someone else in a way that is {i}okay.{/i} Won’t it be nice not having to hide for once?"

    if ayanelust10 == True:
        ay "You’ve {i}been with me{/i} in front of someone else before and, I’m not sure if you remember this, but it was kind of traumatic for me."
        s "This won’t be like that. Chika might be intimidating, but she’s not evil the way Kirin is. She’s just genuinely trying to do something nice for me. And if you don’t want to do it, you don’t have to."
    else:
        ay "Not if I have to share you with someone else...I have no idea how I’ll feel about that."
        s "You don’t have to do it if you don’t want to, Ayane. No one is forcing you."

    scene ayanebedtalk12
    with dissolve

    ay "But if it’s not me, it’ll just be someone else! And that’s even worse!"
    s "I don’t want someone else. I want you. And I get that it might be uncomfortable, but...try to look at it the way {i}she{/i} does — as a celebration of our...passion for one another. Or something."
    ay "Adding “or something” doesn’t make that sound very convincing, Sensei. Nor does the part where Chika would be celebrating her apparent passion for some fake version of you. I lose no matter what here."
    s "You’re not losing anything. And this doesn’t have to be some sort of depressing experience. If you already know it’s happening behind the scenes, what’s the harm in just...participating?"
    ay "The harm is that seeing you fuck some other girl is a lot easier to ignore when it’s just a thing that happens inside of my head. But in person? That’ll hurt me. Do you {i}want{/i} to hurt me?"
    s "Of course not. Which is why I’ll do everything in my power to make it enjoyable for you if you decide to go through with this."

    scene ayanebedtalk15
    with dissolve

    ay "Sensei, I’ve {i}already{/i} decided to go through with it. I told Chika I would and everything. "
    ay "I’m no stranger when it comes to suffering for someone else's sake. I gave up sex with you for like, an eternity just to make Maya shut up. I just wanted you to know I’m not happy about this. "
    ay "And I really wish you would have come to me before she did. It’s one thing to hear about wanting a threesome from {i}you,{/i} but having it come from someone else just makes me feel like an afterthought."
    s "You’re not an afterthought, Ayane. And, if it’ll make you feel any better, I promise to have a threesome with you and anyone else {i}you{/i} want afterward to make up for this."

    scene ayanebedtalk16
    with dissolve

    ay "I’m not in the mood for jokes right now, Sensei. "
    s "Sorry. That was in poor taste."
    s "I do want you to know that you weren’t just a {i}sacrifice,{/i} though. I love you and I want you to be there for this."
    ay "..."
    s "..."

    scene ayanebedtalk17
    with dissolve

    ay "Ugh. Why does love have to be so hard?"
    ay "I feel like you could convince me to do literally anything by just telling me you love me over and over. Hearts are annoying. Stop taking advantage of my biggest weakness."
    s "I’m not taking advantage of-"

    scene ayanebedtalk18
    with dissolve

    ay "I know. I’m just being a bit of a jerk to try and get back at you for hurting my feelings again."
    ay "But if you really want to do this...fine. I’ll try to put up with sharing you for a little while. "
    ay "I had a feeling this would happen eventually, you know. I just kind of figured I’d be more of a deciding factor in it rather than the third wheel."
    s "You’ll never be a third wheel at this point, Ayane. You’re too important to me."
    ay "There you go again...trampling all over my poor heart with those little reassurances."

    scene ayanebedtalk19
    with dissolve

    ay "The only question now is whether or not I’ll be any fun as a threesome partner despite not being into girls. She’s probably going to try and touch me, isn’t she?"
    s "I feel like it would be difficult not to."

    scene ayanebedtalk20
    with dissolve

    ay "You’re gonna owe me for this, by the way. "
    s "Oh, I’m well aware. Anything you want is fine by me."
    ay "I don’t have anything yet, but I’ll keep that in mind."
    s "Understood."
    s "And thank you, Ayane. For everything."

    scene ayanebedtalk21
    with dissolve

    ay "{i}Hah...{/i}yeah, yeah. I’m pretty great. And only a little bit disappointed in myself for not being able to stay mad."
    ay "But I guess I {i}was{/i} just mentioning how I wanted to go back to being the careless, happy Ayane I promised to be. So...maybe I can do that now."
    ay "All things considered, this definitely isn’t as grave of a problem as the world literally ending. So maybe it won’t be all that bad after all."
    s "I’ll take good care of you. Don’t worry."

    scene ayanebedtalk20
    with dissolve

    ay "You always do."
    ay "And {i}we’ll{/i} take care of you as well. "
    s "I’m looking forward to it."
    ay "I can tell. Your eyes just lit up."
    s "Yeah, I had a feeling. This can’t come soon enough."
    ay "There’s a joke to be made there, but I think I’ll let it slide for now."
    ay "How about this weekend? "
    s "Are you sure that’s okay? You don’t need more time to...prepare or anything?"
    ay "I feel like every day we wait, you’ll be dying a little inside. So just relax and let Chika and I work out the specifics or something. I don’t know. I’m new to threesome organization."
    s "I’m looking forward to this weekend, Ayane. "
    ay "I bet you are."

    scene black
    with dissolve2

    ay "But that doesn’t mean {i}tonight{/i} has to be over just yet."

    "The flower tramples me for once."
    "But that’s okay — for we nurture one another soon after."
    "And the night {i}does{/i} come to an end."
    "Just other things happen first."
    "Things I decide to keep to myself this time."
    "She deserves at least that."
    "We deserve at least this."

    $ renpy.end_replay()
    $ ayanebonus1 = True
    $ ayane_love += 1
    $ ayane_lust += 1
    stop music fadeout 7.0

    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayanebonus2:
    scene nightsky
    with dissolve2
    play sound "phonebeep.wav"

    s "..."

    "My phone goes off and, once I look at the caller ID, I get a pretty good grasp of what is about to happen."
    "And I come one step closer to making a little dream come true."

    play sound "phonebeep.wav"

    s "Hello?"

    play music "asobeatsex3.mp3"

    ay "Hello future husband and current adulterer. Tell me, on a scale of one to ten, how hard is your penis right now?"
    s "Like a three. But I can change that whenever I want."
    ay "Do they really work that way? Can you just, like...do that whenever?"
    s "It’s a special power of mine. "
    ay "Then how come it always takes a while to get back up after I make you cum? Do your powers only work for Chika?"
    s "I can’t tell if that is a genuine question or just passive aggressiveness. "
    ay "Oh, you’re going to be getting a lot of passive aggressiveness for pretty much the whole night, Sensei. If you {i}can{/i} make it, that is. If not, we can just call this whole thing off and-"
    s "I’m on my way."
    ay "I am not at all surprised to hear this."
    ay "Meet me in my room. I want to talk to you alone one more time before I have to watch you have sex with another girl."

    scene black
    with dissolve

    s "I’ll be there quicker than you can even blink."
    ay "I highly doubt-"

    play sound "static.mp3"
    scene ayanedoesthething1 with flash
    stop sound

    s "I’m here."
    ay "Wow. You really weren’t kidding. How did you do that?"
    s "I’m not really sure, but that doesn’t matter right now. It’s boner time."
    ay "Boner...time?"
    s "It’s a thing. You weren’t there for it."

    scene ayanedoesthething2
    with dissolve

    ay "Why was I not there for it? Boner time sounds like a thing I should be there for. Especially if I’m now tasked with being the third wheel to sexual escapades with your eight thousand other girlfriends."
    s "It’s just Chika. "

    scene ayanedoesthething3
    with dissolve

    ay "It’s just Chika {i}now.{/i} But then it’ll be Makoto. And then Futaba. And then everyone else you’re seeing until I’ve slept with basically our entire class. I know how your brain works."
    s "If you hate it, we’ll never have to do it again."

    scene ayanedoesthething4
    with dissolve

    ay "Forever? Or just until the next time you volunteer me without talking to me first?"
    s "That won’t happen again. But I’m not going to make that into a promise because I feel like it would only compel me to break it for reasons I can’t really explain."
    ay "Me too. So maybe just...come to me if it ever happens again. That’s the whole reason I got upset in the first place. "
    s "To be fair, you would have gotten upset either way. "

    scene ayanedoesthething5
    with dissolve

    ay "Not about you asking. Wanting to make your fantasies into reality is a totally normal thing. Like {i}my{/i} thing about wanting to have sex with you and a bunch of your clones at once. "
    ay "But unfortunately, my fantasy is way harder to make into a reality. "

    scene ayanedoesthething6
    with dissolve

    ay "So we’ll just have to settle for yours for now."
    s "This is starting to feel like more of a gift from you than the girl who started all of this."
    ay "I’m inclined to agree. Just do me a favor and keep that in mind ten minutes from now when we’re both inevitably going down on you."
    s "Thank you, Ayane. Really."
    ay "Thank me later. For now, I just want you to know I love you and...and I guess I have a few questions about how this is going to work."
    s "Did you not already go over that with Chika?"
    ay "This is something I can’t go over with Chika. I’m talking about the specifics of {i}our{/i} relationship."

    scene ayanedoesthething7
    with dissolve

    ay "She thinks you’re really loyal, doesn’t she? Which means I’m probably going to have to pretend I’ve never done anything like this before, right?"
    s "..."
    ay "Gotcha. So I’ll be putting on a mask after all. But hey, at least we’ll match."
    s "Ayane-"
    ay "Don’t “Ayane” me. We both know you don’t want her to find out about us. Let alone in the middle of sex."
    s "I know. I just feel bad about making you pretend to be something you’re not."
    ay "Good. You should feel bad about that. But I’m amazing and wonderful and so I will do this for your sake and your sake only. "
    ay "And, to maintain the illusion of my innocence, I’m just going to call you “Sensei” instead of any sexy name. Okay? That should throw her off our trail. "
    s "Is there anything else you wanted to inform me of before we call her over?"
    ay "Have I mentioned that I love you?"
    s "A few times, yeah."
    ay "I guess that’s it then."

    scene ayanedoesthething8
    with dissolve

    ay "Oh, no. There is one more thing. But it’s just that I want a cut of the profits if you’re going to secretly film this and sell the footage on the dark web."
    s "That...is not a thing I was planning on doing."

    scene ayanedoesthething7
    with dissolve

    ay "Then that really {i}is{/i} it. "
    ay "I hope you enjoy yourself, Sensei. And...I know it’ll sound weird for me to say this after I just gave you shit about the other night..."
    ay "But thank you for choosing me. I’ve decided that it’s better if I’m involved after all."
    s "We’re ready then?"
    ay "We’re ready."

    scene black
    with dissolve2

    ay "I’ll go get Chika..."

    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene ayanedoesthething9
    with dissolve2

    c "Heeeeeey..."
    c "I guess this is really happening after all, huh?"
    ay "I don’t mind having him all to myself if you’re getting cold feet, Chika. In fact, why don’t Sensei and I get this party started without you and you can just join in whenever you’re ready?"
    ay "Or never. Never works too."

    scene ayanedoesthething10
    with dissolve

    c "I’m ready! Super ready. This isn’t my first rodeo, Ayane. I just kind of expected you to be a little more...nervous, maybe? "
    ay "Nope. Can’t wait to watch the man I love put his dick inside his caring and beautiful girlfriend, who is definitely you and not me."
    c "I’m...I’m glad you’re looking forward to it."

    scene ayanedoesthething11
    with dissolve

    c "There are a few ground rules we need to cover first, though. Particularly what you are and {i}aren’t{/i} allowed to do with Sensei."
    ay "I have limits?"
    c "Right. I want this to be fun for everyone, but there are a few things I’m not really comfortable with."
    ay "Like?"
    c "Like...I don’t want him {i}actually{/i} fucking you. Fingering you and eating you out is fine and stuff, but I’m drawing the line at real sex. But I’m sure you were kind of expecting that already."
    ay "No, actually. To be honest, I was kind of hoping he’d rail me so hard that my bed breaks."

    scene ayanedoesthething12
    with dissolve

    c "You do realize it’s actually, like...kind of painful the first time, right?"
    ay "Yeah, but I’m pretty sure I can handle it. I’ve done my research."
    c "I think you’ll be having second thoughts about that once you see Sensei’s cock up close, but...still. No sex. Okay? I’m not cool with that."
    s "Chika, if Ayane thinks she’s ready-"

    scene ayanedoesthething13
    with dissolve

    ay "It’s fine, Sensei. I suppose this fragile body just isn’t ready to be sexually penetrated yet. Alas."
    c "Thanks, Ayane. And if there’s anything you’re uncomfortable with, feel free to let me know."
    ay "Well, I told you on the beach already, but I’m not into girls. So if you could keep the touching to a minimum, that would be nice."

    scene ayanedoesthething14
    with dissolve

    c "Meaning like...barely any touching at all? Or just certain body parts are off limits?"
    ay "You’re free to use your judgement and I’ll stop you if it gets too weird for me."
    c "I can just avoid all the sensitive parts and let Sensei take care of those."
    s "Fine by me."

    scene ayanedoesthething15
    with dissolve

    c "Don’t get {i}too{/i} excited, cowboy. You’re still {i}my{/i} boyfriend after all."
    s "Why did you just call me “cowboy?”"
    c "I don’t know. It just kind of happened. I’m definitely a little nervous. I’ve never done stuff with another girl before."
    ay "Neither have I. But I haven’t done anything with anyone ever and am totally inexperienced when it comes to sexual contact. I’m excited to get going, though!"

    scene ayanedoesthething16
    with dissolve

    c "So should we, like...take our clothes off right here? Or...or do we go to the bed first? Or...I’m not really sure what happens now."
    ay "Neither am I. But again, that is because I am totally inexperienced when it comes to sexual contact and have never done anything like this ever before. Ever."
    s "Both of you get on the bed right now. All of these ground rules and boundaries are ruining boner time."

    scene ayanedoesthething17
    with dissolve

    c "Boner time? What’s boner time? That sounds like a thing I should be there for and I’ve never heard of it before."
    ay "That’s exactly what I said."

    scene black
    with dissolve

    c "{i}When?{/i}"
    ay "In a dream I had, obviously. I’m just an inexperienced virgin after all."
    c "Heheh...well..."
    c "Here I come, little miss virgin..."

    "Ayane and Chika get onto the bed and holy shit this is actually happening."

    scene ayanedoesthething18
    with dissolve2

    c "Aren’t I just the best girlfriend ever, Sensei? Like, who else would just {i}let{/i} you play with another girl? Supervised, of course."
    ay "Yes. Who else indeed?"
    s "Yes, Chika. You’re great. But now is the part where your clothes come off."
    c "Really? You don’t want to ramp up to it a little more? You’ve got two adorable girls basically on top of each other and they’re both here for {i}you.{/i} I figured you’d want to savor this for a little longer."
    ay "Technically, Chika’s the one on top of me. But yes, I am also here and I am very excited to do sexual things with you for the first time ever."
    c "Just not actual sex."
    ay "Yes. Apparently not actual sex. "

    scene ayanedoesthething19
    with dissolve

    c "This is probably a dream come true for you, huh? How long have you wanted Sensei?"
    ay "Since way before he ever met you."
    c "Then you’re probably really excited for him to touch you...aren’t you, Ayane?"
    ay "Thrilled. Couldn’t be happier."

    scene ayanedoesthething20
    with dissolve

    c "And how about you? Don’t you feel a little bad making moves on a girl you’ve pretty much watched grow up?"
    ay "Clearly not since he’s the one who suggested me. For no reason at all, of course."
    s "Yes, I’m very excited for anything and everything. Why are your clothes still on?"

    scene ayanedoesthething21
    with dissolve

    c "Wow, you really can’t contain yourself, can you? "
    c "I bet you’re so fucking hard right now...I can’t wait until Ayane gets her first look at my favorite toy."
    ay "Your hand’s getting a little close to the danger zone, Chika."

    scene ayanedoesthething22
    with dissolve

    c "Permission to lift your shirt up so Sensei can see your tits and stop throwing a temper tantrum?"
    ay "Permission granted."
    s "Finally. Something good."

    scene ayanedoesthething23
    with dissolve

    c "Ooooh...something {i}very{/i} good. This is totally different from just seeing them in the shower."
    ay "Kyaaaah. My breasts are exposed to the man I have a crush on. I am so very embarrassed. "
    s "..."

    "I want to say that her acting could use some work, but there is absolutely no way this isn’t intentional."

    scene ayanedoesthething24
    with dissolve

    c "Do you like what you see, Sensei? "
    s "If I say yes, are you going to get pissed off or threaten to kill one of us?"
    c "No, dummy. You can say whatever you like tonight and I won’t hold it against you. So go on and tell me how much you want to fuck Ayane."
    ay "Just remember that you’re not allowed to because of reasons."
    s "In that case, I {i}love{/i} what I see. And I’d love it even more if I was allowed to do more than just watch right now."

    scene ayanedoesthething25
    with dissolve

    c "You’re not the only one excited to play with her, Sensei. In fact...maybe I’ll have a go at it first?"
    s "I would be willing to make an exception for such a thing."
    ay "And I once again feel very strange about this."
    c "Too far?"
    ay "Almost. This much is fine, I guess."
    c "Do you want to make out?"

    scene ayanedoesthething26
    with dissolve

    ay "Not really, no."
    c "Not even if Sensei wants to see it?"

    scene ayanedoesthething27
    with dissolve

    ay "Hey, here’s a better idea! How about Sensei takes his pants off and we use our mouths on him?! What’s that called again? A suckjob? A blowhead? I have no idea. I’m totally new to this!"
    c "Sorry, Sensei. I tried. I know you wanted to see us kiss."
    s "I’m pretty sure you wanted that even more than me. But I like Ayane’s suggestion more either way."

    scene black
    with dissolve
    play sound "zipper.mp3"

    s "The pants are coming off."
    c "Heheh...brace for impact, Ayane. My boyfriend is {i}packing.{/i}"
    ay "Wow! What a large penis! Probably! I’ve never seen one before!"

    "Even if she’s doing this intentionally, I am now dead set on buying Ayane acting lessons after this."

    scene ayanedoesthething28
    with dissolve2

    "But that is a thought I am going to completely abandon now because things are finally getting to where I want them."
    "Chika flips her own shirt up to match Ayane before sliding my pants down around my ankles and grabbing my shaft."
    "The two girls crawl toward the edge of the bed and I step forward to get even closer to them, ending up just inches away from both of their faces as they gaze up at me in anticipation."
    "Well, at least Chika’s eyes gleam with anticipation. I’m pretty sure Ayane is just toying with me right now based on her expression."

    c "So, Mr. Boyfriend, tell me — you’re about to have your cock sucked by two cute teens at once. How do you feel? "
    s "I believe the way I feel is extremely evident based on the condition of my penis."
    c "Yeah...you’ve gotten so hard for us, baby. Which means it’s {i}our{/i} job to take responsibility...Right, Ayane? Do you want to suck the teacher’s cock with me?"
    ay "I’ll do my best. Which will probably be bad because I’m an amateur."

    scene ayanedoesthething29
    with dissolve

    c "It’s easy. I’m sure you’ll get the hang of it in no time at all. "
    c "Just start slow...and gradually work up the pace. Maybe ease into it with a little lick or two? Sensei loves that. Then, when you’re ready, you can try to fit it in your mouth. Kay?"
    ay "I’ll try, Chika. But it sounds really hard."
    c "Don’t worry. He’ll love it no matter what."

    scene ayanedoesthething30
    with dissolve

    c "Chu..."
    ay "Mm......mnh...."

    "Both girls begin their respective roles — Chika softly kisses the tip of my cock while Ayane gently lubricates my shaft with her saliva."
    "Of course, she isn’t the novice she claims to be, so I’m carried away to ecstasy almost instantaneously as I gaze down at the two of them, devoting their entire selves to making {i}me{/i} feel good."

    scene ayanedoesthething31
    with dissolve

    "Within minutes, Chika adds a bit of stroking into the mix."
    "The two of them open their eyes and gaze up at me as I’m gently jerked off. But even if it {i}is{/i} gentle, it does not put an end to my burning desire to paint both of their faces white this very instant."
    "The most surprising thing of all so far, though...has been Ayane. Despite being so hesitant at first, she gone right back to her usual self and is barely paying any attention to Chika at all."
    "Maybe that’s her strategy — to just ignore her and act like it’s the two of us."

    scene ayanedoesthething32
    with dissolve

    ay "Mm..."

    "Or maybe she’s just trying to take what little charge she can. "
    "Maybe she wants to prove to Chika that she’s not the only one who can get me to feel this way. "
    "Ayane saw me first. And while that isn’t enough to lay claim to my heart, it does go a long way in displaying just how much of herself she’s willing to surrender to me."
    "And so begins the section of the night where my {i}girlfriend{/i} watches on in awe or shock or jealousy as another girl fills her mouth with my flesh. "
    "The gentle tugging stops, but Ayane begins to slowly bob her head in order to make up for it."

    c "..."
    ay "Mm...mm...mlm...mnch..."
    c "Wow..."
    c "You’re kind of a natural at this..."

    scene ayanedoesthething33
    with dissolve

    ay "Mm!...Mm!...Mm!..."
    c "How’s it feel, Sensei? Getting to fuck Ayane’s mouth?"

    "The reprieve from the tugging doesn’t last long as Chika goes back to stroking my cock. This time, with much more fervor than before."

    ay "Hngh...mlm...mnch...chmp...mmlm!"
    c "Careful or you might corrupt her...the same way you did to me..."
    c "Remember when I was all innocent and {i}not{/i} your little cumslut? That feels like forever ago now, doesn’t it?"
    s "It...does..."
    c "You’re still gonna give all your cum to {i}me{/i} though, right?..."
    s "At this rate...I’m not really sure..."
    c "Uh-oh..."
    c "Looks like I’m gonna have to fight for it then..."

    scene ayanedoesthething34
    with dissolve

    "Chika opens her mouth and, unable to seize any of my tip, winds up dragging her tongue across the length of my shaft while refusing to let up on the stroking."
    "Ayane joins her, bringing one of her hands up to my dick and using it to stabilize it rather than jerk me off so she’s able to focus a little better on sucking."
    "It’s a beautiful sight, watching the two of them fight over me like this. But what’s even more beautiful than that is how it {i}feels.{/i}"
    "I’m enveloped by pleasure. "
    "I could spend forever like this."

    scene ayanedoesthething35
    with dissolve2

    c "Mm!"

    "Just kidding. I’m screwed."

    ay "Hah...hah...hah..."

    "Ayane slides my cock out of her mouth and, to my surprise, willingly surrenders it to Chika."
    "It’s hard to say whether she’s just giving her jaw a break or {i}actually{/i} sharing but, either way, I’m not going to last much longer at this rate."

    c "Mngh...mlm...mnch..."
    ay "You do this a lot, don’t you?"

    scene ayanedoesthething36
    with dissolve

    c "Mnch...mm..mmhmm..."
    ay "Wow...I’m so jealous..."
    ay "I can only imagine how much fun {i}I’d{/i} get to have if I was dating Sensei..."
    ay "You’re so lucky, Chika...seriously..."
    c "Mmm...mngh.......mlm....."
    ay "Is he gonna cum soon? Can you make him cum?"
    ay "It’s kind of throbbing, isn’t it? I think I can feel his heartbeat...Does that mean he’s getting close?..."

    scene ayanedoesthething37
    with dissolve

    c "Mm!....Mmnh...."

    "Chika speeds up, knowing from experience that what Ayane is suggesting is just moments away."
    "But instead of trying to take me back, Ayane is the one who begins to jerk me off — staring right into my eyes as she does it."
    "And for the first time tonight, I can feel that she’s either beginning to {i}actually{/i} get into this..."
    "Or that she's capable of being a good actress when she really wants to be."

    ay "Did I do a good job sucking your cock, Sensei?...It might be the only chance I ever get...so I had to be good..."
    s "..."
    ay "God...I want you so bad..."
    ay "Just hurry up and cum already so you can finger me...I’m so wet...and I’m tired of waiting..."
    c "Mlm...hmng....mnhh.....mlm!"
    ay "Do it...cum in Chika’s mouth..."

    "She jerks harder."

    ay "Do it..."
    ay "Do it...do it...do it..."

    with sexfade
    with sexfade
    scene ayanedoesthething38
    with cumflash
    with hpunch

    c "MMMLMMLMLMLMMMMMM!!!!!"
    ay "Hah....hah....hah....."

    scene ayanedoesthething39
    with dissolve

    ay "Lucky...I wanted some..."
    c "Mm...mlm...mnh..."
    s "You can still share..."

    scene ayanedoesthething40
    with dissolve

    ay "It’s okay if we do? It’s not all for her?"
    s "There’s more than enough to go around. The only issue is how-"

    scene ayanedoesthething41
    with dissolve

    s "Oh."
    s "Well, okay."
    ay "Mlm...mnch...mmff..."
    c "Mmf...mngh...chlm..."

    scene ayanedoesthething42
    with dissolve

    ay "Mm......mlfm......mnch....."
    c "Hmn!......Mm.......Hmm...."

    scene ayanedoesthething43
    with dissolve

    c "Hah......hah.......I thought.....you didn’t want to kiss me?....."
    ay "I still don’t..."
    ay "You just had something I wanted..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene ayanedoesthething44
    with dissolve2

    ay "Hah!...Aahh!......AAaaaaah!"
    c "Harder!...Ngh...Harder!...."

    "Things progress rather quickly from there."
    "I flip both of them over and line them up on the bed, pulling their bodies up to my waist the moment I’m hard again."
    "There’s a little physical overlap needed for me to be able to reach both of them, but neither one of them seems to mind bumping into one another after sharing a mouthful of my cum."
    "My cock sinks into Chika with no trouble at all, and she wastes no time when it comes to using my body to pleasure herself."
    "Ayane is a little more difficult. She needs to arch her back and push out her ass in order for me to reach her."
    "This results in her waving it around like a bitch in heat until I’m able to slip my way in."
    "My fingers attack the roof of her insides as I pound away at the girl beside her, wishing I was allowed to swap every now and then just to get a nice comparison of their respective sensations."
    "And you know what? Maybe I could. But is that really something I want to risk doing when I know it could put an immediate end to what is already one of the most sexually gratifying events of my life?"
    "No. {i}Fuck{/i} no."
    "I’m going to enjoy this to the very end."

    ay "AAAAAHHH!...MNGH!"

    "Over."

    c "Fuck me! Fuck...me!!!!"

    "And over."

    ay "I’m gonna cum! I’m gonna cum!....Hah!"

    "And over. "

    c "Oooooh fuck! I love your dick! I love your...big fucking dick!"

    "And over again."

    play sound "static.mp3"
    scene ayanedoesthething45 with flash
    stop sound

    "Until there is nothing left of me."
    "I lose track of how many times I empty myself out for them. And I lose track of how many ear-piercing mutual orgasms I encounter in the process."
    "But in between visions of the pale white flesh of Ayane’s ass and her beautifully pink pussy that I am {i}horrifically{/i} disallowed to penetrate tonight- something catches my eye."
    "A line of photos on her wall."
    "I’m the subject of all of them. And I recall a long time ago that this actually worried me."
    "But look where it has gotten us today."
    "After mountains of problems and more drama than you’d be able to fit into a ten-season soap opera-"
    "I can nibble on her clit while fucking her hypersexual gyaru classmate."
    "This is a good outcome for me. "
    "It’s the {i}best{/i} outcome for me. "
    "{s}And I owe it all to God.{/s}"

    c "Ooooh...fuck! I feel like...I’m gonna explode..."
    ay "Hah....ah......aahh.....are you sure I......can’t have a turn to....ride him too?...."
    c "Get...ahh...your own...hah...boyfriend..."
    ay "The only...boyfriend I’ll ever want...has his...tongue inside of me right now..."
    c "That’s...hah! Your...problem! Not...mine! Fuck! Ayane...play with my tits...you’re not...using your hands for anything...are you?..."

    scene ayanedoesthething46
    with dissolve

    ay "Are you...kidding me?...My hands are...the only thing...keeping me up right now...and for...ngh...the millionth time...I’m not into that..."
    c "How can you...still be saying that...at a time like this?..."
    c "I’d do...whatever you wanted me to...right now..."
    ay "Can you...let your boyfriend fuck me then?..."
    c "I’d do...{i}almost{/i} anything you want me to...right now..."
    ay "I feel like...we’re not...ah...going to...find anything we...agree on..."

    scene ayanedoesthething45
    with dissolve

    c "Hah...hah...fine...Then...back to...riding Sensei’s...cock!..."
    ay "Rub it in...why don’t you?..."

    scene black
    with dissolve2

    "It’s sad to say, but I never came again."
    "That didn’t stop Ayane and Chika from having three and four more orgasms respectively, though."
    "I’m not sure if it was the pictures on the wall that did me in or the strange sexual rivalry that began to sprout up between the girls, but something just wound up feeling off near the end."
    "I guess it could very well be because I climaxed more times than I can count, though."

    scene ayanedoesthething47
    with dissolve2

    c "Okay...time to go take eleven showers..."
    ay "I will be joining you for at least nine of them."
    s "And I...am going to go home."

    scene ayanedoesthething48
    with dissolve

    c "You ran out of steam kind of early tonight, didn’t you? We’ve gone way longer than that before."
    s "I clearly anticipated this too much and am now paying the price. I’ll be back to normal in no time at all."

    scene ayanedoesthething49
    with dissolve

    c "You were still great either way. {i}And{/i} you got to fool around with Ayane. Everybody wins."
    c "Best Christmas gift ever, right? When’s round two?"

    scene ayanedoesthething50
    with dissolve

    ay "Round {i}two?{/i} I thought we made it to, like...round twenty just now."
    c "I meant the second threesome. We should do this again sometime. I had fun. And based on the fact that you’re still naked, I think you did too."
    ay "I am naked because this is my room. This is the one place I’m allowed to be naked without getting arrested."
    c "Bath house. Onsen. Locker room. My room. Probably the whole dorm in general, to be honest."

    scene ayanedoesthething51
    with dissolve

    ay "Okay. So there are more rooms. But I’d like to at least take my nine showers before I decide whether or not this is something I want to do again. I assumed this was, like...a one time thing."

    scene ayanedoesthething52
    with dissolve

    c "What do you think, Sensei? Wanna do this again sometime?"
    s "I think..."
    ay "..."
    c "..."
    s "That we should let Ayane take her nine showers before we decide anything."
    c "Psht. Whose boyfriend even are you?"
    ay "That’s a great question..."

    scene ayanedoesthething53
    with dissolve

    c "Well, I’m satisfied. That’ll hold me over for about a week or so. "
    c "Come on, Sensei. You can walk me back to my dorm."
    s "Your dorm is literally right across the hall. I think you can make it yourself, Chika."

    scene ayanedoesthething54
    with dissolve

    c "Fine. Then I will go myself."

    scene ayanedoesthething55
    with dissolve

    c "But if you’re gonna hang around in here any longer, remember — no putting it in Ayane."
    c "In fact, no touching at all since I’ll be out of the room. Capiche?"
    s "Understood."

    scene ayanedoesthething56
    with dissolve

    c "And {i}you.{/i}"
    ay "And me?"
    c "Put some clothes on."
    ay "..."
    c "..."
    ay "But this is my room. I’m allowed to be naked here."
    c "Not around a teacher, you’re not."
    ay "But that teacher just had his fingers {i}and{/i} his tongue inside of me. Shouldn’t there be some kind of exception here?"
    c "Good point! I’m still high on sex, so be naked for the rest of the night or whatever. I don’t care right now. But in the {i}future,{/i} no being naked around the boyfriend without girlfriend supervision."
    ay "Umm..."
    ay "Okay. Sure."
    c "Cool. Good times."

    scene black
    with dissolve

    c "Anyway! Great job tonight, guys! Good workout! See you all in school on Monday!"

    play sound "dooropen.mp3"
    "........."
    "......"
    "..."

    scene ayanedoesthething57
    with dissolve2

    ay "Well, that was an experience."
    s "Did you hate it?"
    ay "Not as much as I thought I would. I’m not sure if I’m in any rush to do it again though."
    ay "As expected, I don’t really like watching you put your penis in other girls."
    s "You literally jerked me off into Chika’s mouth."

    scene ayanedoesthething58
    with dissolve

    ay "You know the old phrase, Sensei — “When in Rome, help your future husband cum in the mouth of another woman.”"
    s "Ahh, yes. I do know that phrase quite well now that you mention it."

    scene ayanedoesthething57
    with dissolve

    ay "All that really matters is that you had a good time. "
    ay "But again, {i}please{/i} don’t blindside me with another situation like this in the future. Talk to me first and we can figure it out like adults."
    s "But-"
    ay "And don’t go calling me a kid because I’m more of an adult than you are and you know it."
    s "That...is a fair point."
    s "But, now that this is all out of the way, can I expect the return of the newer, happy Ayane any time soon?"

    scene ayanedoesthething58
    with dissolve

    ay "That’s something you’ll have to ask her. I’m not actually Ayane at all. I’m Efrosinia Aleksandrova, Russian spy — and {i}you{/i} just had a threesome with me."
    ay "Hope you’re okay with me selling all of your personal information online, because you know it’s coming."
    s "Then, {i}Efrosinia...{/i}"
    s "Tell Ayane the next time you see her that I’m sorry for this bump in the road. And that I hope she can go back to not worrying about stuff."
    s "She’s been doing that all too much lately."

    scene ayanedoesthething57
    with dissolve

    ay "Okay...but Efrosinia makes no promises. And {i}all{/i} information she obtains may be sold to Facebook at any given moment."
    s "That is a risk I guess I’ll have to take."
    ay "I guess it is."
    ay "Goodnight, Sensei. I have to go take nine showers now."
    s "And I will go take {i}one{/i} because I am a normal human being."
    ay "If you were a normal human being, you wouldn’t have just had a threesome with two high-schoolers."

    scene black
    with dissolve
    play sound "dooropen.mp3"
    stop music fadeout 13.0

    s "And now I am definitely leaving."
    ay "You know it’s true!"

    "I exit Ayane’s room and..."

    s "..."

    "And..."
    "I guess I..."
    "I guess I just..."
    "Go home?"

    $ renpy.end_replay()
    $ ayanebonus2 = True
    $ ayane_love += 1
    $ chika_love += 1
    $ ayane_lust += 5
    $ chika_lust += 5

    "{i}Ayane’s affection has increased by 1! Her lust has increased by 5!{/i}"
    "{i}Chika’s affection has increased by 1! Her lust has increased by 5!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayanepool55:
    scene ayanepooltalk1
    with dissolve2
    play music "notabluearchivesong.mp3"

    "I decide to spend the end of the school day at the pool with Ayane instead of being responsible and utilizing these hours to pretend to be a guidance counselor instead."
    "It is not the most mature decision I have made, particularly because the amount of latex in this room directly impacted my decision to come here, but I suppose that doesn’t really matter right now."
    "If Ayane really is trying to face the world with a renewed lease on life and that same level of optimism she had when I {i}first{/i} started having sex with her, I owe it to her to reciprocate that."
    "Not the optimism, of course. Or the happiness either as I’m pretty sure I’m almost entirely incapable of showing {i}either{/i} of those traits. "
    "But what I {i}will{/i} reciprocate is a level of focus that miraculously evades the many asses in this room and hones in on her instead."
    "We have each other. And we will continue to have each other in every way until one of our brains turn into goo or our memories are wiped clean like the world’s most complicated dry-erase board."
    "Everything begins to spin again."
    "Just this time, it’s in a way that doesn’t make us dizzy."

    ay "...and that’s how I wound up freeing all of the lobsters in Kumon-mi from the tyranny of those evil grocery stores."
    s "Admirable story, Ayane. I particularly enjoyed the part with the bowling tournament."
    ay "I don’t know how I could have accomplished my goal without that. But that’s enough about my Tuesday- we can talk about more interesting stuff now."
    s "More interesting than lobster liberation? That’s a pretty big ask. I’m not sure if I’ll be able to contribute in a meaningful way."
    ay "Well...Halloween’s right around the corner. We could always talk about that? That should be pretty interesting-ish, right?"
    ay "I still haven’t decided what I’m going to dress up as this year. Maybe you can help me brainstorm or something?"
    s "Giving me full control over what you wear is a dangerous thing to do, Ayane."
    ay "If Chika can dress up as a sex-dog, I’m pretty sure that anything you want to put me in will work out just fine."
    s "Then I will ask that you also dress up as a sex-dog this year. Even if I’m pretty confident there’s a better name for whatever costume that was."

    scene ayanepooltalk2
    with dissolve

    ay "I will see what I can do. But keep in mind that I’m not exactly known for {i}risque{/i} costumes like that."
    s "I can see why. They don’t really fit your personality."

    scene ayanepooltalk3
    with dissolve

    ay "You think so?"

    if ayanelust10 == True and ayanebonus2 == True:
        s "Yeah. For a hypersexual teen who has now had threesomes with two of her classmates, you’re extremely wholesome. It’s kind of weird actually."
        ay "The first threesome didn’t count. And yeah, it’s probably a little harder to call me wholesome now that you’ve watched me suck your jizz out of the sex-dog’s mouth."
        s "Is Chika just permanently “the sex-dog” now?"
        ay "Sure. I think it fits her pretty well."
    elif ayanelust10 == False and ayanebonus2 == True:
        s "Yeah. For a hypersexual teen coming off of her first threesome, you’re extremely wholesome. It’s kind of weird actually."
        ay "Yeah, it’s probably a little harder to call me wholesome now that you’ve watched me suck your jizz out of the sex-dog’s mouth."
        s "Is Chika just permanently “the sex-dog” now?"
        ay "Sure. I think it fits her pretty well."
    else:
        s "Yeah, for a hypersexual teen who’s let me cum inside her more times than I can count, you’re surprisingly wholesome. It’s kind of weird actually."
        ay "Thanks. I think. "
        ay "That {i}was{/i} a compliment, right?"
        s "Sure. Why not?"

    s "In regard to your actual Halloween costume, though- just do whatever you want. I’d be lying if I said I wasn’t a fan of the group cosplay stuff you guys have done the last couple years, so that’s always welcome."
    s "I’ll be happy as long as you don’t pull a Maya and go to whatever party we’re having this year dressed up as me."

    scene ayanepooltalk4
    with dissolve

    ay "Aww, but I think I’d look really cute in your clothes."
    s "Ayane, I might be a narcissist. But even {i}I{/i} don’t want to have sex with myself."
    ay "Yeah, but that’s only because you have a penis. If you didn’t, you’d be all over yourself. And I’d also probably become bisexual."
    s "I’m just going to warn you now. If I come home one of these days and find you in my closet, I am not going to be happy."
    ay "Really? I can’t even borrow a big shirt to sleep in or something? Wouldn’t it be nice seeing me in an oversized t-shirt the night after sleeping over while I cook you breakfast? I think that sounds nice."
    s "I’m sure it would be very nice in the ten seconds before Ami chops your head off."

    scene ayanepooltalk2
    with dissolve

    ay "Ami won’t do anything to me. I’m safe and free to do anything I please and nobody can stop me. That’s Ayane 2.0’s whole thing. Remember?"
    s "Can you teach me whatever this mysterious anti-Ami method of yours is next? Because, even if she’s been easing up lately, I still feel like it’ll come in handy knowing how you’re keeping her at bay."
    ay "I’m keeping her at bay with the power of friendship of course."
    s "Ayane-"

    scene ayanepooltalk5
    with dissolve

    ay "Didn’t I already tell you that was a secret? Just accept my safety and go back to telling me what sort of costumes you want to make love to me in. "
    ay "My confidence has taken a beating over the last year and I could really use the boost."
    s "I would have sex with you no matter what you’re wearing. "
    ay "Dolphin costume it is. "
    s "Wouldn’t be the first time I’ve had sex with someone who’s been in that thing."

    scene ayanepooltalk6
    with dissolve

    ay "{i}You had sex with Sana?! When?! She wasn’t on the list! Also, how?!{/i}"
    s "Not Sana, Niki. She was the one in the costume last year."

    scene ayanepooltalk7
    with dissolve

    ay "Niki was the mystery-dolphin? But why would she-"

    scene ayanepooltalk8
    with dissolve

    ay "Wait, Niki wasn’t on the list either. At least...not in the sex column."
    s "That...is a relatively new development."
    ay "So...you and your long-time ex-girlfriend who is not only very famous, but your childhood-friend...are together again?"
    s "If you’re worried, you shouldn’t be. I don’t plan on leaving you any time soon."
    ay "Is there...anyone {i}else{/i} you’ve added to the list since writing it? Should I grab you another pen and paper?"
    s "There..."
    s "There is."

    scene ayanepooltalk9
    with dissolve

    ay "{i}Hah...{/i}Okay. Hit me. Who is it this time?"
    s "It..."
    s "It’s Nodoka."

    scene ayanepooltalk10
    with dissolve

    ay "Tch. So she’s not all talk after all."
    s "She’s...different, though."

    scene ayanepooltalk11
    with dissolve

    ay "Considering who we’re talking about, that could mean a number of things."
    s "What I mean is that I don’t really feel anything for her. It’s just sort of a thing that happened."
    ay "As in you both accidentally got naked and slipped and your penis wound up inside of her vagina?"
    s "I actually kind of wish it {i}did{/i} go down like that. That would be way easier to...accept and understand."
    ay "I’m...confused. But, at the risk of learning more details and tarnishing my happiness, I say we just get back to the topic at hand."
    s "Fine. Where’d we leave off again? Something about having sex with Sana?"

    scene ayanepooltalk12
    with dissolve

    ay "Almost. We were talking about Halloween before we got sidetracked by another sex-animal."
    s "Right, right. Any word on where this year’s party will be? We haven’t been to your place in a while. Maybe that will work?"
    ay "There’s no word on that just yet. But I’ve actually been thinking it might be fun if we do our {i}own{/i} thing this year too. After the party, I mean."
    s "Just you and me?"

    scene ayanepooltalk1
    with dissolve

    ay "And the other members of the Love Squad. Sana too if you can promise not to have sex with her."
    s "Do I have to?"
    ay "Only if you want her to maintain the feeling in her lower body. "
    s "I’ll have to get back to you on that."
    ay "What do you think, though? Is that something you’d be interested in? We could do it at your place or...maybe the karaoke lounge? I don’t know. I just kind of feel like trying something a little different."
    ay "The big group parties are fun and all, but something a bit more intimate sounds like it would be way more enjoyable for me on a personal level. And I’m sure Sana would agree."
    s "Fine by me. We’ll just have to think of a way to get me away from everyone else since I’m {i}kind of{/i} the center of attention at all of our group outings."
    ay "Well, all things considered, it’ll definitely be easier than it would have been last year. I’m sure we’ll think of something."
    s "Just let me know. We’ll call breaking away from the other girls for a {i}second{/i} party one of my first steps toward adopting this new carefree outlook you seem to have on life. "

    scene ayanepooltalk13
    with dissolve

    ay "Follow me into the light, Sensei. For only {i}I{/i} can show you what it means to be free."
    s "Is that...a Yasu impression?"

    scene ayanepooltalk14
    with dissolve

    ay "Pretty good, right? I’ve been practicing. "
    s "{i}Why?{/i}"
    ay "I figure that if I get good enough at imitating all of the other girls that you won’t have a reason to have sex with any of them anymore."
    s "..."
    ay "That was a joke. I’m not being serious."
    s "I never really know with you."

    scene ayanepooltalk15
    with dissolve

    ay "Hey, I’ve gotten pretty good at suppressing my crazy side. "
    s "That’s what I thought until you gave me an exact duplicate of my phone, complete with all of my contacts and wallpaper."
    ay "Pretty good doesn’t mean “perfect.” I still have my flaws. I’m just a little better at not showing them now. But again, this will continue to improve with every cycle. "
    ay "Ayane 2.0 is here not just to {i}stay,{/i} but to be the backbone everyone needs when confronting this big, scary world we find ourselves in."
    s "Well, keep it up and even {i}Maya{/i} might be smiling soon enough."

    scene ayanepooltalk16
    with dissolve

    ay "Actually, I’m glad you brought her up- because I’ve been meaning to ask you something."
    ay "I know Ami’s changes are kind of obvious because of this whole “Stop suffocating me” policy you’re starting to enforce, but...don’t you think Maya’s been acting a little different lately too?"
    s "Different how?"
    ay "Well, for one, she asked me if I needed a {i}hug{/i} the other day."
    s "You’re right. That is very concerning."
    ay "It’s not just that either, but...it’s kind of hard to describe. She just feels kind of off. Did anything happen with you two?"
    s "Apart from the near-kiss? Not really. Maybe her...real personality is just starting to leak out or something?"
    s "She’s had to keep a brave face on for what I can only imagine is an absurd amount of time. We can’t really fault her if that mask starts to crack now that she’s starting to feel a little more comfortable."

    scene ayanepooltalk17
    with dissolve

    ay "I guess you’re right. There’s no way of knowing how either one of us would feel in her shoes, so...it could just be normal character development or something."
    ay "She’s just been the same old {i}Maya{/i} for so long though that I can’t help but worry any time she does something even slightly different."
    ay "Either way, you know her better than I do. So I’ll just take your word for it."
    s "I wouldn’t say I know her any better than you. Just that I have a higher chance of making out with her."
    ay "Is it the same for Miku as well? Because I’ve noticed she hasn’t been acting like herself lately either."
    s "I...might have an idea as to why. But, for clarity’s sake, what do {i}you{/i} mean?"

    scene ayanepooltalk18
    with fade

    ay "Well, for one, she’s not running around and screaming."
    ay "In fact, I can’t even tell if she’s awake right now."
    s "..."
    ay "I know Imani and Makoto have been cracking down on the girls with lower grades lately. And come to think of it, I'm pretty sure that’s why Makoto isn’t here today."
    ay "Do you think this might have something to do with that?"
    s "It...could."

    "Or it could be something completely different that I shouldn’t bother Ayane about as it has nothing to do with her..."

    scene ayanepooltalk19
    with dissolve

    ay "Hey, Miku. Are you awake over there? Aren’t you going to swim today?"
    mi "..."
    s "..."

    scene ayanepooltalk20
    with fade

    ay "...huh."
    ay "Maybe she really is asleep?"
    ay "Should we...just let her rest? She probably needs it if it’s from overworking herself, right? I can’t imagine all those worksheets are doing her any favors."
    s "I’ll..."
    s "Uhh..."

    scene black
    with dissolve
    stop music fadeout 12.0

    s "Actually, I’m going to let someone who’s better at this sort of thing deal with it. I think this might be a little more than just...being overworked."
    ay "More how? Do you know what’s going on?"

    "Leaving Ayane on the bench, I make my way over to the girl who is inarguably the most mature person in this room."

    s "Karin, have you talked to Miku today?"
    ka "Hm? I did earlier. Why do you ask?"
    s "She’s just..."
    s "She looks a little out of it right now, don’t you think?"
    ka "Out of it how? What’s- "
    ka "Wait, is she {i}asleep?{/i} During {i}club?{/i}"
    no "I was beginning to wonder why it’s been so quiet all day...I suppose that explains it."
    ka "Sorry, Nodoka. I’ll be back in a second. I’m just gonna go check up on her really quick."

    "Karin leaves Nodoka’s side, prompting Ayane to get off the bench and head over toward me as the lot of us move closer to Miku."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ ayanepool55 = True
    $ ayane_love += 1
    jump mikupool55

label ayanespring1:
    "Ami leaves the room and I’m left alone again."
    "I can hear the sounds of seven different locks being closed and, if I hadn’t already realized just how desperately she’s been trying to keep me safe, I’d know it now for sure."
    "I don’t hear her call Ayane. And I’m not sure I’d even want to as I’m positive the call would be laced with countless clauses and concerns Ami has."
    "I just sit there, on a bed drenched in sweat, and wonder what will happen next."
    "I wonder what she’ll say when she sees me. Or if she even {i}will{/i} see me if she’s not open to adhering to whatever my niece’s demands are."
    "She probably will be."
    "She’s probably desperate by now."
    "I know this to be true because that’s the case for me. And while Ayane might be able to put on a brave face in my times of peril, there are limits to just how brave that face can be."
    "She’s only human, after all."
    "She’s just a girl, after all."
    "If the fraying of the ropes that hold me up does not cease within the coming days, I will fall for the rest of my life. So why should I abstain from reaching out for someone who can cover it in knots?"
    "I owe her the chance to save my life after all she’s done for me. And I’m sure that sounds selfish. The things I say seldom don’t."
    "But when she fails, and she likely will, I hope she won’t hate herself for being incapable of cushioning the blow."
    "Because right now, I feel as if I could crack my head on anything."
    "I feel as if it’s egg time."
    "........."
    "......"
    "..."

    scene ayanecameback1
    with dissolve2
    play music "meanttobe.mp3"

    ay "Are you sure it’s okay? I can really go in?"
    a "Actually, Ayane, I’m {i}not{/i} sure. This obviously wasn’t my idea. {i}I{/i} want you as far away from my house and my uncle as humanly possible."
    a "But he’s weak right now...and I’m not going to tell him he can’t have something when I know he truly wants it. And, for some reason, he wants {i}you.{/i}"
    ay "He asked for me specifically? Not, like...you know...{i}anyone else?{/i}"
    a "He’s been calling a different name in his sleep. But since the two of you have gotten so {i}close{/i} behind my back, I assume you already know who that is. Correct?"

    scene ayanecameback2
    with dissolve

    ay "Ami..."
    a "If you do {i}anything{/i} to hurt him while you’re in there, you will never see either one of us again. Do you understand?"
    ay "Ami, I’ve been telling you this whole time — I have no intention of hurting him. "
    a "See, I don’t really care about your {i}intentions.{/i} Even if you hurt him on {i}accident,{/i} you will never see either one of us again. {i}Do you understand?{/i}"

    scene ayanecameback3
    with dissolve

    ay "Yes. I understand. And thank you, Ami. I mean it."
    a "..."
    ay "I really, really mean it."
    a "We’ve known each other a long time, haven’t we?"
    ay "We have. "
    a "Do you love me, Ayane? Like...really {i}really{/i} love me?"
    ay "I do."
    a "Why? "

    scene ayanecameback4
    with dissolve

    ay "{i}Why?{/i}"
    a "I’ve been getting on your nerves a lot lately, haven’t I? Between keeping Sensei here...and ditching you in the woods...and forcing myself into your “private affairs...”"
    a "Even the way I’ve looked at you...{i}argued{/i} with you. Despite all of that “Waaaah, my friends are leaving me” crap, what I {i}really{/i} wanted was some peace and quiet."
    a "I don’t care if you hate me. I don’t care if {i}anyone{/i} hates me. The only person who will ever {i}really{/i} matter to me is Sensei. And I would trade {i}your{/i} happiness for {i}his{/i} complacency in a heartbeat. "
    ay "Why are you telling me this?..."
    a "Because, for whatever reason, you’ve stopped falling for it. And I trust Sensei enough to trust that {i}you{/i} will not go out of your way to “rescue” him from this house. He does not need to be {i}rescued.{/i}"
    a "Do I make myself clear, Ayane? "
    a "If Sensei goes back to school like none of this ever happened, it will ruin everything. {i}Everything.{/i} And even if I know what’s best for him, I can’t {i}keep{/i} him here if he doesn’t want to {i}be{/i} here."
    ay "What do you mean by “like none of this ever happened?” And “it will ruin everything?” Because I’m pretty sure you have no idea what even {i}happened{/i} in the first place."
    a "And that’s something you {i}do{/i} know?"

    scene ayanecameback5
    with dissolve

    ay "Yes! I tried to tell you in the karaoke booth! But you were so focused on getting Sensei back home that you wouldn’t listen to what-"
    a "I don’t care about {i}what.{/i} I care about {i}why.{/i}"
    a "{i}Why{/i} do you know what’s wrong, Ayane? This shouldn’t involve you."
    a "You should be back at the dorms, goofing around and playing games with Sana. Or practicing karate at the dojo. Or...getting kicked out of various local businesses or whatever it is you’re {i}supposed{/i} to do."
    a "But you’re not. You’re {i}here.{/i} And I’m having a little trouble understanding how that could possibly be a good thing for {i}any{/i} of us or {i}why{/i} it’s even happening in the first place."

    scene ayanecameback6
    with dissolve

    ay "I don’t care about what’s “good” or what I’m “supposed” to be doing anymore. I’m just worried about Sensei. And I know you can relate to that, Ami. If {i}anyone{/i} can relate to that, it’s you."
    a "Stop comparing your “love” for him to mine. It’s going to make me sick."
    ay "Ami-"
    a "You have ten minutes. Go in there, say what is you have to say, listen to whatever it is {i}Sensei{/i} has to say...then leave."
    a "Go back to your normal routine. Find someone else to burden with your undying affection. Just leave my uncle out of it."
    a "You two were never meant to be."

    scene ayanecameback7
    with dissolve

    ay "..."
    a "..."
    ay "You know...I feel really bad for you, Ami. "
    a "Yeah. You’re kind of supposed to."
    ay "Do you want to know why, though?"
    a "Not really. I still have to make breakfast since the first dish I made wound up all over the floor."
    ay "It’s because you think you understand what love is, but I’m not sure you’ve actually {i}felt{/i} it even once in your life."
    a "Cute. How long have you been holding onto that line for?"
    ay "Depends. How long have you been holding onto literally everything you’ve said to me today?"

    scene black
    with dissolve2

    a "You don’t want to know."

    "........."
    "......"
    "..."

    scene ayanecameback8
    with dissolve2

    "It’s hard to explain the look that was on Ayane’s face when she first walked into the room, but I think I’d describe it as somewhere between pity, gratefulness, and frustration."
    "I’m not sure if she was expecting me to look a little more “broken” than I currently am given just how long I’ve been away, but it took all of three seconds to make me feel as if I disappointed her."
    "Besides, what’s on the outside very rarely exemplifies the way my heart moves."
    "Right now, there are a million different thoughts swirling through my head. And if you’ve ever lost anyone before, I’m sure you know that none of them are good."
    "Finding a way to shelve them for the sake of communicating with someone else, especially someone who reminds you of that person, isn’t easy."
    "But she knows I’m alive, at least. And that’s more than everyone else has gotten as of late."
    "Where do we begin, though? What words can I say to break the two month silence in a way suitable to her perception of me as a human being?"
    "Is this the part where I attempt to make a joke and fail miserably? Should I apologize for my absence? Would it be normal to say something mildly sexual? Just wrap my arm around her and tell her I love her?"
    "What am I like? Who am I supposed to be? The answers to such questions used to only be slightly more difficult than breathing. But now, it’s like I’m struggling with both."
    "And I can’t even retreat to the self-soothing plea that “I want to go home” because I’m already here."

    s "..."
    ay "Sensei...you don’t have to talk. I’m sure it’s...not exactly easy after all you’ve been through."
    s "I can talk. But you’re right...it’s not easy. "
    s "I can barely even move my limbs right now. And between that and my complete inability to remember how to converse with another person, it’s like I’m the world’s most miserable mannequin."
    ay "Staying in bed for two months will do that to a person..."
    ay "I imagine you’ll be feeling pretty terrible for at least another few weeks. But...at least you’re conscious? I think? Unless...you’ve {i}been{/i} conscious this whole time?"
    ay "I don’t...really know what’s been going on in here, to be honest. Nobody does. Ami’s kept you guarded like the vaults of Fort Knox."
    s "Then kudos to Uta and Io for managing to break in last night."

    scene ayanecameback9
    with dissolve

    ay "Oh, is {i}that{/i} what happened to the window? I was wondering what the boards were all about."
    s "Yeah. According to Ami, they were here. I don’t really know any of the details, though."

    scene ayanecameback10
    with dissolve

    ay "I guess that explains why they weren’t at the party, then. I’m glad it was that and not them just...growing distant from everybody else."
    ay "Which isn’t to say Io’s already not like that, but...yeah..."
    ay "I’m...happy you’re okay. Even {i}if{/i} okay doesn’t really mean “okay” in this context. "
    ay "I guess what I’m saying is I’m just happy to see you again. Even if the situation itself is kind of...the worst thing that could have possibly happened."
    s "It could have been worse. You could be gone too."

    scene ayanecameback11
    with dissolve

    ay "Without spending too much time whining about {i}my{/i} problems, the last couple months have made me feel like that wouldn’t have changed much."
    s "Has it been hard? Being alone this whole time, I mean. Because at least I’ve had Ami. Even if I haven’t really been {i}present{/i} at all within that time."

    scene ayanecameback12
    with dissolve

    ay "Well...here’s where things get interesting. Because I {i}haven’t{/i} been alone. Makoto made it to the rooftop that night as well."

    scene ayanecameback13
    with dissolve

    s "Makoto {i}what?{/i}"
    ay "Yeah...so that’s a new development. A development I obviously don’t blame you for not remembering since you were kind of catatonic when the reset happened."
    s "Then...who actually {i}started{/i} the reset? It had to be you, right?"

    scene ayanecameback14
    with dissolve

    ay "Uhhhhh..."
    ay "Sure. Let’s just go with that."
    s "...What?"

    scene ayanecameback15
    with dissolve

    ay "Anyway...Maya’s still here too. It’s just...you know...her {i}memories{/i} that..."
    s "What’s she like? Without being jaded by centuries of meaningless time travel?"

    scene ayanecameback16
    with dissolve

    ay "Honestly...not that different. "
    ay "Like, she kind of blends in with everyone else a little better since she’s not so busy trying to figure out the secrets of the universe all the time."
    ay "But other than that, she’s just sort of...sassier. But in a typical Maya sort of way."
    s "Has she said anything about me?"

    scene ayanecameback17
    with dissolve

    ay "Just...the same kind of stuff she always says when other people are around. Like how you’re gross and...a pervert and...you know. Stuff like that."
    s "Well, at least that hasn’t changed. "
    ay "Yeah..."
    s "..."

    scene ayanecameback18
    with dissolve

    ay "Um..."
    ay "I...talked to Chika too. Last night."
    s "Oh, good. I can only imagine how she’s handling this."
    ay "Yeah...she hasn’t been doing so great. She’s cutting class almost every day now that you’re not around anymore...And, weirdly enough, Yumi’s been showing up {i}more.{/i}"
    s "Yeah, that also makes sense."
    ay "But, uhh..."

    scene ayanecameback19
    with dissolve

    ay "You know, Chika had a really good idea. And she called me last night to talk about it since she figured I’d be the easiest way to infiltrate your house."
    ay "Little did she know, I had no clue when I’d even be able to {i}do{/i} that until just a little while ago. "
    ay "But she thought it might be good for you if all of us, like...put a card together for you. To tell you that we’re all waiting for you to come back and stuff."
    s "And you managed to collect everyone’s signature in just one night?"

    scene ayanecameback20
    with dissolve

    ay "Um...no."
    ay "See, she didn’t call me until it was really late and...I kind of just took her idea and ran with it. So, this is a card. Yeah. But it’s...from me. I didn’t get anyone else’s signature."
    s "Then...can I read it now? Or do you want me to wait until you’re gone?"

    scene ayanecameback21
    with dissolve

    ay "You can read it now, but...I’m sorry in advance if it seems frantic or rushed or anything like that. It’s...weirdly difficult putting your feelings down on paper when you have so many of them."

    scene ayanecameback22
    with dissolve

    ay "You’d think after all the ones I wrote for my mom that I’d be better at this by now, but...nope. Still suck."
    ay "I should have just written you an essay instead."
    s "You’ve been writing letters to your mom?"

    scene ayanecameback23
    with dissolve

    ay "I keep them in a box underneath my bed in case I ever find out where she lives now. I’ve got...probably hundreds down there."
    ay "And I know I’ll be holding onto them for the rest of my life, but...miracles happen sometimes. And I’m dumb enough to keep believing in them."

    scene ayanecameback24
    with dissolve

    ay "I shouldn’t be greedy, though."
    ay "Like, who would I be to ask for a second miracle with the first one sitting right beside me?"
    s "Bold move to flirt with me while Ami is very likely right outside the door."

    scene ayanecameback25
    with fade

    ay "Oh, she’s definitely right outside the door. And she gave me a real earful when I first came in. But I’ve been keeping my voice low enough that she won’t be able to hear it."
    ay "Either way, though...I’m not worried about her."
    ay "Ami loves you, Sensei. In a way that...I don’t think any of us will ever understand. I just don’t think she understands how crazy that can make her look at times."
    ay "Like, she’s been even worse than normal when it comes to you lately. {i}A lot{/i} worse. To the point where some of the girls have thought about reporting your case to the police."
    ay "I think some might have even gone through with it. Especially since Uta and Io were willing to go as far as breaking into your house. A little report seems like nothing by comparison."
    ay "I guess nothing ever came of it, though, if Ami’s still got you locked up after all this time."
    s "Either that or she killed and buried all of the police who were brave enough to come knocking on the door."
    ay "Hahah...yeah..."

    scene black
    with dissolve2

    ay "Let’s maybe not joke about that."

    "........."
    "......"
    "..."

    scene ayanecameback26
    with dissolve2

    "Ayane’s letter is just as frantic and rushed as she said it might be. But it’s honest in the same way Niki’s old letters were when Noriko handed a box of them to me a few Christmases ago."
    "Granted, this one is far less insane- and it focuses primarily on recapping everything that’s happened while I’ve been over here in agony."
    "Imani and Wakana are losing it. Rin and Otoha broke up. Makoto’s joined the Rooftop Apocalypse Squad and Sana’s been-"

    play sound "static.mp3"
    scene sanaisabadgirl21 with flash
    scene fuckherdoityoupussydoit36 with flash
    scene fuckherdoityoupussydoit40 with flash
    scene ayanecameback26 with flash
    stop sound

    "Sana’s been acting differently..."
    "There are other things in here too. Like how much she misses me or how different school is now that she’s actually required to work again."
    "She likes it. It keeps her busy so she’s not stuck thinking about me all the time. But of course, those thoughts pick back up at night."
    "She’s been crying a lot. The letter doesn’t say that, but there’s a smudge near the bottom left corner of the page that I’m pretty sure is a tear drop."

    scene ayanecameback27
    with dissolve

    "I put my arm around her. But I do it because I want to, not because I want to comfort her."
    "And for a brief moment in time, I forget just why I’m here in the first place. "
    "I forget the grief and the loss and the sensation of connecting with someone who seemed so out of reach for so, so long. "
    "But it comes back near the end of the letter when she talks about {i}her.{/i}"

    scene ayanecameback28
    with dissolve

    "{i}I watched Maya struggle with her collar after school the other day. The one with the bell she always wears.{/i}"
    "{i}Were you the one who bought that for her? Was it so you could always hear her coming? Did the sound of walking beside her cheer you up like it always does for me?{/i}"
    "{i}Regardless of the reason, I watched her struggle. She couldn’t get the clasp to work and she slammed it down on the table.{/i}"
    "{i}For a moment, it looked like she was going to cry. But she held her breath, tried again, and eventually got the clasp to work.{/i}"
    "{i}I’m pretty sure she misses you. Even if she won’t say it.{/i}"
    "{i}Please, come back to us.{/i}"
    "{i}Please.{/i}"

    s "..."
    ay "..."
    s "Thank you, Ayane."
    ay "You don’t have to thank me. In fact, I’d prefer if you didn’t. Things have been so hectic lately that I didn’t even remember to get you a real present for Christmas."
    s "This is more than enough. And way more than I’ve ever gotten you for any occasion."
    ay "You’re right. You should buy me presents more often."
    s "I should."
    ay "You should say more nice things to me and spend more time with me and tell me you love me more often and stuff."
    s "I should."
    ay "You should marry me."
    s "I should."

    scene ayanecameback29
    with hpunch

    ay "!..."
    s "..."

    scene ayanecameback30
    with dissolve

    ay "Uhh..."
    s "..."
    ay "Saying it like that kind of makes it sound like you’re actually...considering it?"
    s "Does it? Interesting."
    ay "{i}Interesting?{/i}"
    s "It’s risky, though. Makoto already has my signature on a marriage registration and I’m pretty sure submitting both might cause some problems."
    ay "Why does Makoto have your signature on a wedding registration, exactly?"
    s "It was an accident."
    ay "And I’m going to guess your penis also wound up inside of her after the two of you slipped on a banana peel?"
    s "It was a large banana. You’re familiar with them. You know how it works."
    ay "Sensei...do you really-"
    s "Ayane."

    scene ayanecameback31
    with dissolve

    ay "What? What is it?"

    scene black
    with dissolve2

    s "I need your help talking to Ami."

    $ renpy.end_replay()
    $ ayanespring1 = True
    $ ayane_love += 10

    "{i}Ayane’s affection has increased by 10!{/i}"
    "........."
    "......"
    "..."

    jump springend3

label beachfive3:
    scene sky
    with dissolve2
    play music "notabluearchivesong.mp3"

    "It’s Friday morning and, as previously agreed upon, I’m currently on my way to the Amamiya mansion to listen to whatever it is Ayane has to say regarding the state of our world and how immeasurably fucked up it is."
    "Granted, I’m sure a lot of it will just be me dejectedly agreeing to whatever she proposes since I really don’t care anymore...but maybe Makoto will miraculously start caring in my stead and balance her out?"
    "Which is doubtful (as everything is doubtful) considering that Ayane has specifically informed me of just how little she seems to care, but there are crazier things that have happened."
    "Like, for example, have I ever told you about the time I was having sex with Maya on the roof only to have her disappear partway through? Because {i}that{/i} was crazy, wasn’t it? Way crazier than whatever this is."
    "So yeah, today is going to be a day. And it will be a day that I do my best to not phone-in out of respect for the one girl I know who is doing a better job of keeping it together than everyone else combined."

    scene black
    with dissolve2

    "So cheers to you, Ayane Amamiya — may your morning be full of joy and squandered opportunities to abandon a man who does not deserve you."
    "........."
    "......"
    "..."

    scene ayanepresentation1
    with dissolve2

    ay "Lady and gentleman, I present to you...my foolproof plan to save the world and marry Sensei! Please be advised that the real title is still in progress and that this one is just a placeholder."

    play sound "static.mp3"
    scene ayanepresentation2 with flash
    stop sound

    mak "Did you really have to make shirts for us?"
    s "Did you really have to wear one?"

    scene ayanepresentation3
    with dissolve

    mak "I wasn’t going to. But it looks good on me, doesn’t it?"
    s "Yeah. Where are your glasses, though? "

    scene ayanepresentation4
    with dissolve

    mak "I’m actually wearing {i}contacts{/i} today. Cool, right? And it only took me half an hour to put them in."
    s "I feel like that is significantly longer than such a thing is supposed to take. "
    ay "Hey! Stop flirting and pay attention to my plan to restore the world and everyone in it to the proper state!"

    scene ayanepresentation5
    with fade

    s "Sorry, Ayane. It’s been a while since I’ve hung out with Makoto and I’ve forgotten the level of rude that I am supposed to be with her."
    mak "Zero rude. You decided to be nice to me, remember? I think I’d actually prefer it if you’d bring that up to a four or five, though. It feels weird when you’re too nice."
    s "Shut up, Ayane is talking. "
    mak "Yeah, like that. That’s a good level."
    ay "Are you two done now?"
    s "Yeah, sorry. "

    scene ayanepresentation6
    with dissolve

    ay "Good! Then, let me begin by thanking both of you for coming and saying that I greatly appreciate you humoring me as my mind continues to be thrown into turmoil on a day-to-day basis!"
    s "Amen."

    scene ayanepresentation7
    with dissolve

    ay "Now, as you {i}may{/i} already know, things have happened that have caused our world to reset near the end of every school year. What {i}are{/i} these things, you ask? No clue! But what we {i}do{/i} know is that it sucks!"
    mak "Do I need to raise my hand to disagree or can I just verbally do that right now?"
    ay "I think you just kind of did."

    scene ayanepresentation8
    with fade

    s "I continue to be surprised by just how okay with this you are when all it does is prevent you from ever achieving the future you’ve been working toward your entire life."
    mak "I continue to be surprised by just how {i}not{/i} okay with this you are when all this does is allow you to indefinitely have sex with a rapidly multiplying number of teenagers for the rest of eternity."
    ay "And I continue to be ignored! Pay attention! I worked hard on this!"

    scene ayanepresentation9
    with dissolve

    mak "Sorry. But let the record show that I am right. And also that I think it would be okay if we’d take it a little easier in trying to uncover the secrets of a thing that defies all logic and science."
    s "Let the record also show that I have a photo of Makoto sucking a dildo backed up on my computer."
    mak "Permission to strike the record, madam speaker?"

    scene ayanepresentation10
    with dissolve

    ay "Granted. Now, back to the topic at hand."

    scene ayanepresentation11
    with dissolve

    ay "Right now, only {i}three{/i} of us are aware of the state of the world: me, Sensei, and Makoto. And with Maya’s memories purged, we have no evidence that {i}more{/i} than three people can safely know at any given time."

    scene ayanepresentation12
    with dissolve

    ay "There have been instances in the past where that number has increased, but {i}no{/i} evidence of such information carrying over from one timeline to the next as a value {i}greater{/i} than three."
    ay "{i}Additionally,{/i} we’ve never had more than three people on the rooftop at once. "
    ay "And while this is in no way {i}proof{/i} that such a thing is impossible, what it {i}does{/i} do is provide a precedent and warning in regard to how we proceed from here. "

    scene ayanepresentation13
    with dissolve

    ay "What that means is even {i}if{/i} we find someone with the ability to {i}retain{/i} information about the loops, we have no guarantee that they’ll remember it once the next cycle begins..."
    ay "It also seems so far that this information is stored in a sort of...seniority-focused way. Maya was the first to know, followed by Sensei, then me, then Makoto. "
    ay "Once {i}Makoto{/i} started retaining information and making it to the roof, Maya {i}lost{/i} that ability. Which would mean, if that’s an indication of things to come, {i}Sensei{/i} would be the next to go back to “normal.”"
    mak "Objection. I’d like to strike that from the record as well so Sensei doesn’t start blaming {i}me{/i} for the disappearance of his beloved Maya."
    ay "Denied. I’m not doing this to try and point fingers at anyone, I’m just saying that we need to be aware of the risks involved if we {i}do{/i} start trying to tell other people about this."

    scene ayanepresentation14
    with dissolve

    ay "It’s very possible that none of this is relevant at all. I just think it would be best if we didn’t get our hopes up since all that’s done in the past is let us down."
    ay "As such, I think we need to accept that {i}any one of us{/i} could be “gone” at any given moment. And, should that happen again, we can’t let ourselves fall into the state Sensei did after Maya."
    ay "Our time is only infinite to a certain degree. And what we learned through Maya’s disappearance is that we need to cherish each and every single day we have together because we never know when our days will end."

    scene ayanepresentation15
    with dissolve

    ay "Understood?"

    scene ayanepresentation16
    with fade

    s "I’m sorry...to both of you. I wasn’t really thinking of that...I just didn’t know how to get out of bed."
    mak "Way to go, Ayane. Your morbid message of “hope” has made Sensei upset."
    ay "Sensei, you don’t have to apologize! I know exactly how hard this has been for you. But the reason we need to be careful about stuff like this is because we want to {i}prevent{/i} it from happening again."
    ay "So let this presentation be {i}my{/i} promise that if you {i}do{/i} vanish, I’ll keep working hard until I get you back. We’ve gotta keep the ball rolling or we’ll never get anywhere. Do you understand?"

    scene ayanepresentation17
    with dissolve

    mak "If this theory {i}is{/i} true, though — this one based on “seniority,” we only have to experience it once more before pulling the plug on informing others, correct? "
    mak "Because Sensei being reset after one more {i}new{/i} person makes it to the roof would establish a definitive pattern. "
    mak "And repeatedly cycling through three people over and over won’t give anyone a long enough time to really {i}investigate{/i} anything. Right?"

    scene ayanepresentation18
    with fade

    ay "Right. Which is why I propose that we come up with a list of people who we think are both {i}capable{/i} of maintaining a level head in the face of an apocalypse, as well as those we think are {i}able{/i} to."

    scene ayanepresentation19
    with dissolve

    ay "We already know that Maya, Yumi, and Tsuneyo are capable of {i}knowing{/i} about the loops, but that’s the extent of our knowledge. And since I like to believe in everyone, I think they’d be able to remain strong. "
    ay "I’ve also included Miku and Sana in this list because of their respective connections to Makoto and I — and Nodoka and Noriko because they’re both really smart. "
    ay "I’m sure Noriko’s connection to Sensei counts for something as well. So if we’re going to tell {i}anybody,{/i} I think these are the ones we need to stick to."
    mak "You can go ahead and just remove Miku from that list now. I love her with all of my heart, but there’s no way she’d ever be able to comprehend any of this. And I know that for a fact because I’ve already tried."
    s "Actually...I’m glad you included Noriko on there. Because something she said the other day really got me thinking."

    scene ayanepresentation20
    with fade

    s "You guys already know that my memories got pretty messed up somewhere within the fifty-billion timelines we must’ve experienced, but they’ve been coming back little by little."
    s "Noriko mentioned that Maya might be in the same boat. Maybe {i}her{/i} memories are just...locked away somewhere? Maybe something just needs to sort of...trigger them and remind her?"
    mak "With all due respect, Sensei, we don’t know for sure {i}what{/i} caused your memories to fade. I’d argue that the effects of trauma are significantly more plausible than...timeline interference."

    scene ayanepresentation21
    with dissolve

    s "And I won’t argue against that. But if I need to be positive right now, I’m going to regurgitate the only bit of hope I’ve gotten since she vanished. And right now, that’s what I have."
    s "Maybe I’m wrong. In fact, I’m {i}probably{/i} wrong."
    s "But, at the very least, it shows that Noriko is capable of picking up the differences in Maya’s behavior- and that seems to be something everyone else has struggled with."
    ay "That’s actually another reason I included her."

    scene ayanepresentation22
    with fade

    ay "Noriko told me about the talk you guys had and how you told her to come to me. That’s when I really started trying to throw this plan together. "
    mak "Well, what {i}is{/i} the plan in the first place? Because I’m not sure if I’d call just doomsaying to all of our friends a concrete strategy."
    ay "I’ll get to that in a second. I have to do more doomsaying first."

    scene ayanepresentation23
    with dissolve

    ay "It’s been over six months since our last apocalypse. "
    ay "And while I’ve yet to catch onto whatever sort of vibes Maya used to pick up on that made her aware of their approach, I imagine we’re getting close to another based on the time-frame alone."
    ay "Taking that into consideration and measuring it against the {i}other{/i} apocalypses I’ve gone through, I can only assume the next one might happen any day now."

    scene ayanepresentation24
    with dissolve

    ay "And that means we need to act sooner rather than later if we want to make any progress this time around."
    ay "Sensei, you’re probably not aware of this since you and Ami have both been away from school for a while, but our next beach trip is tomorrow. And I want you to come. But I want you to come {i}without{/i} Ami."
    s "That’s...probably a little easier said than done. "
    ay "I’m sure you’ll figure it out. And, in the event that you’re uncomfortable being around the entire class at once again, don’t be. Because I’m already working on a plan for that as well."
    mak "Question — why does it need to be during the beach trip? Do these apocalypses {i}always{/i} occur during class gatherings, or-"

    scene ayanepresentation25
    with dissolve

    ay "I’m glad you asked, Makoto! Because this is where phase one of my foolproof plan comes into play!"
    ay "We are but young girls, oblivious to the ways of the world! But what we {i}do{/i} know is how to create a vast network of information and different methods of exchanging it! And the best method of all, you ask?"

    scene ayanepresentation26
    with dissolve

    ay "We throw a slumber party!"

    scene ayanepresentation27
    with fade

    mak "That’s phase one of your plan to “save the world?” A slumber party?"
    ay "Not just {i}any{/i} slumber party! A beach slumber party in Sensei’s room at the inn! Super secret and invite-only, just like the {i}last{/i} time we did this."
    mak "You’ve used this method before?"
    s "Yes and, if I’m remembering correctly, it immediately invoked an apocalypse. "
    ay "That it did, Sensei. Which means it’s very possible that it happens again. "
    s "Sure. But last time, I had a little more of an opportunity to get Yumi and Tsuneyo to agree. I have no idea how I’d manage that on such short notice this time."
    ay "Leave all of that to me, Sensei! You just worry about a way to keep Ami at home and make it so {i}you{/i} can come to the party without her. Because I love Ami, but all she’d do here is get in the way."
    mak "And what do {i}I{/i} do? "
    ay "Just show up, I guess. I didn’t really factor you into the equation since I wasn’t positive you were even going to make it here today. "

    scene ayanepresentation28
    with dissolve

    mak "Yeah, I probably wouldn’t have if you didn’t show up at my house with your butler."
    s "So...I just worry about getting to the beach alone-"
    ay "And we throw a midnight bash where we poke and prod at our classmates’ minds with apocalyptic info to see if anything sticks! "
    ay "It’s not foolproof by any means. But we’re running out of time, and it’s way easier to get everyone together when we’re already...you know...{i}together.{/i}"
    s "If that’s...what you think is best."

    scene ayanepresentation29
    with dissolve

    mak "How do {i}you{/i} feel, though? Are you really ready to start doing things like this again? Because I was under the impression you were trying to just...remove yourself from the class atmosphere altogether."
    s "Frankly? I’m not ready. And I’m not looking forward to it at all."

    scene ayanepresentation30
    with dissolve

    s "But I trust Ayane...so I’m going to put all my faith in her since I have nowhere else to put it now."

    scene ayanepresentation31
    with fade

    ay "Thank you, Sensei..."
    ay "I know I’m no Maya, but I’m going to do my best."

    scene ayanepresentation32
    with dissolve

    ay "And honestly? Doing my best is way easier when she’s not here to doubt me all the time. Like seriously, what the fuck was that about?"
    mak "I mean, if {i}I{/i} was an immortal time-traveler, which I guess I kind of...{i}am{/i} now?...I’d doubt you too if your first plan was throwing a slumber party."
    ay "The slumber party method has worked 100%% of the time. Kind of. It’s foolproof. Mostly."
    ay "Also, it’ll be fun sneaking into Sensei’s bed while everyone else is asleep and reclaiming his body as mine. "

    scene black
    with dissolve2
    stop music fadeout 15.0

    mak "Note to self — wear earplugs to bed."
    ay "Earplugs will be provided to all attendees free-of-charge! Except Sensei. I want him to {i}hear{/i} me."
    s "Okay. I’m going to head home now if that’s all we’re doing today."
    ay "Wait, Dad-"
    mak "{i}Dad?{/i}"
    s "Don’t worry, I’ve got a plan for Ami. Just call me tomorrow when the coast is clear for me to head over."
    ay "Got it. I love you! Makoto, do you need a ride? Geoffrey’s probably in his cryo-chamber right now, but I can page him if you-"
    mak "I’ll walk home with Sensei, it’s fine."
    s "I’d rather be alone right now, actually. But I’ll see you tomorrow night, Makoto. "
    mak "Ugh...fine. Also, cryo-chamber?"
    ay "Oh, yeah. Geoffrey is actually-"

    "I leave the Amamiya mansion and...try to snap myself into whatever state of mind will allow me to pretend things are normal again."
    "........."
    "......"
    "..."

    scene nightsky
    with dissolve2

    "I spend the rest of the day by Ami’s side."
    "It’s the least I can do since I’ll be leaving her tomorrow. "
    "But it’ll also be a good opportunity."
    "Not for me, but for her."
    "And for the girl who volunteered to stay by her side."

    scene black
    with dissolve2

    "I think I’ll be ready to have a talk soon."

    $ renpy.end_replay()
    $ beachfive3 = True
    $ ayane_love += 1
    $ makoto_love += 1

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump beachfive4

label beachfive15:
    play sound "static.mp3"
    scene ayaneshowerlust1 with flash
    stop sound
    play music "acoustic.mp3"

    "{b}BACK TO THE GOD DAMN TEEN SLUMBER PARTY{/b}"

    y "Think I’m gonna have to wear my fuckin’ swimsuit to bed at this rate."
    s "You could always sleep naked. I’m sure Noriko would like that."
    y "No thanks. Rather chop my fuckin’ tits off than let either of you two get a hold of ‘em."

    scene ayaneshowerlust2
    with dissolve

    ay "Hey, welcome back. You guys are really wet. "
    y "Yeah. Blame {i}this{/i} fuckin’ asshole for that. "
    ay "Don’t worry, Yumi. It happens to me too."
    y "...What?"
    ay "How did things go? Any...fun conversation topics?"
    y "You talkin’ bout the weird timeloop memory shit? You call that fun?"

    scene ayaneshowerlust3
    with dissolve

    ay "So-"
    s "Yeah. Yumi seems to be aware again. And I barely even had to say anything this time."
    ay "Aware to what extent exactly? Because Sana’s sort of “aware” now too but I don’t think she believes or understands anything. "

    scene ayaneshowerlust4
    with dissolve

    y "If we’re supposed to “understand” shit just count me out now. I ain’t got a fuckin’ clue what any of this means. And if I’m gonna just forget all of it in a week or two, ain’t like it matters in the first place."
    ay "{i}Can{/i} it matter? Because you’re the closest we have to a fourth member of the Rooftop Apocalypse Squad now and that may or may not mean something soon."
    y "Maybe. Can I take a fuckin’ shower first so I don’t have to talk about this while dripping water all over the fuckin’ floor?"

    scene ayaneshowerlust5
    with dissolve

    ay "Sure! I’ll even come with you so we can talk more since I want to take one too."
    y "Pass."

    scene ayaneshowerlust6
    with dissolve
    play sound "slidedoor.mp3"

    ay "See you in a few minutes, Yumi! "
    s "Sana overheard our conversation earlier, you know."

    scene ayaneshowerlust7
    with dissolve

    ay "Yeah, she told me. "
    ay "She told me some other stuff too. But that was both {i}not{/i} today and {i}not{/i} relevant to the topic at hand. "
    s "Well, seeing as that can only mean one thing, I’ll just ask. Are you bothered by it?"
    ay "Could be worse. But it’s not going to change anything. I’ll love you no matter which of my friends you conquer next. I just might have to buy another notebook at this rate."
    s "So that’s...Sana, Yumi, and Nodoka who are “aware” now. What about Noriko? And did anyone try talking to Tsuneyo or did we just leave her out after the public nudity thing?"
    ay "Tsuneyo’s a no-go. I tried. And Makoto hasn’t had any luck with Noriko either so the two of them are just playing chess for now."
    s "So...what’s the next step? Buckle up and wait to see if the world ends?"
    ay "Guess so."
    s "And if it doesn’t? "
    ay "Idunno. Maybe another slumber party? See if any of them have any ideas on how to break a timeloop? Nodoka’s probably a gold mine."
    s "Maybe, if she can actually get a thought or solution out. Because she made it sound like she needed to trick the fucking world itself before she could figure anything out."

    scene ayaneshowerlust8
    with dissolve

    ay "Holy shit. Maybe this is like one of those rom-coms where New York City is one of the characters in the story? Just with Kumon-mi instead."
    s "I mean...at this rate, I feel like that’s a given. This place is fucking weird."

    scene ayaneshowerlust9
    with dissolve

    ay "Don’t you think it’s weird in other places too, though? "
    ay "Like, what if we’re {i}all{/i} going through something similar right now. And there’s some other rooftop trio in Yamanashi or someplace doing the same thing we are?"
    s "It’s not {i}impossible,{/i} I guess. But there’s no way of knowing without being able to leave. Which is sketchy all on its own."
    ay "That’s for our safety, though. There’s nothing sketchy about the space war. That’s a real thing that’s happening."
    s "So we think."
    ay "Sensei, Makoto’s dad died. "
    s "Or maybe...he never existed in the first place?"
    ay "Are you a conspiracy theorist now?"
    s "I need to contribute in any way I possibly can if you’re going to keep going all-out like this. And right now, that method involves brainstorming random and implausible ideas."

    scene ayaneshowerlust10
    with dissolve

    ay "You’d really sacrifice your sanity and common sense like that for me?"
    s "When you’ve been doing precisely that for well over a year now, I think it’s only fair."

    scene ayaneshowerlust11
    with dissolve

    ay "Thanks. But there are {i}other{/i} ways to reward me too, you know."
    s "I think I know where this is going."
    ay "Did you bring any shampoo with you? I forgot mine and want to go shower."
    s "I did not know where this was going."

    scene ayaneshowerlust12
    with dissolve

    ay "Do you have any or not? I have no way of knowing if Yumi will actually share with me."

    if escapeshampoo == True:
        "Hmm..."
        "I {i}have{/i} been dragging along this extra shampoo bottle for quite some time now, but I’m not even sure how I got it."
        "Should I give it to Ayane?"

        menu:
            "Give Ayane the mysterious shampoo":
                "I don’t want to give Ayane the shampoo."
                "I think I’ll hang onto it for a little while longer."
            "Hang onto the mysterious shampoo":
                "Ayane can go fuck herself. This is {i}my{/i} shampoo."

    s "I don’t, sorry. You’ll have to bother Yumi for some."

    scene ayaneshowerlust13
    with dissolve

    ay "Oh well. If worse comes to worst, you’ll just have to deal with my hair not being at its softest when I sneak into your bed tonight."
    s "Yeah, I’m not sure if this is the perfect setting for something like-"

    scene ayaneshowerlust14
    with dissolve

    n "Ah! Affection spotted! Ayane is hugging Oniichan’s arm without his or anyone else’s consent!"
    s "I consent."
    n "You’re too young! You can’t!"
    s "I...what?"
    n "Release the arm, Ayane!"

    scene black
    with dissolve2

    ay "Fiiiiiine~ I have to go wash Yumi’s back anyway."
    y "Fuck no you don’t. Touch me and you die."
    n "Yeah! You tell her, Yumi. Don’t let her just steal my job like that!"
    y "{i}Both{/i} of you can die! Jesus, fuck!"
    sa "Are we...showering together? Right now?..."
    mak "It appears that way. But thankfully, we don’t have to deal with Nodoka this time."
    ay "Makoto! Do you have extra shampoo?"

    play sound "slidedoor.mp3"

    mak "{i}I...might? It’s coconut-scented, though. And if Miku refuses to use it-{/i}"
    ay "{i}Coconut’s fine! Sensei can just pretend I’m you when he’s snuggling with me later.{/i}"
    n "{i}No touching my Oniichan! Sana! Attack!{/i}"
    sa "{i}I...uhh...huh?!{/i}"

    "The five of them wander off together and I’m suddenly left on my own..."
    "{b}go chase them down and stick your wiener in one{/b}"
    "Never mind."

    play sound "static.mp3"
    scene ayaneshowerlust15 with flash
    stop sound
    play sound "shower.mp3"

    "Despite not being alone, I manage to avoid confrontation and effectively stave off some very uncomfortable thoughts for roughly thirty minutes until the girls return from their shower."
    "But seeing as I was still in need of one after getting caught in the same storm Yumi did, I had Ayane check to see if the coast was clear before I headed off to the men’s bath."

    if escapeshampoo == True:
        "I also brought along my favorite shampoo and it turns out the bottle is endless so I will have it forever."
    else:
        "I also found this nifty shampoo that someone left here just for me."

    "As I sit on my stool, contemplating what will or won’t change after tonight, all I can really do is hope that there isn’t another apocalypse on the horizon. But if there {i}is{/i} one, at least I’m already naked."
    "I don’t think there will be, though. At least not tonight. And I may have just jinxed myself by admitting that, but I’m going to stick to my guns here as I’m actually...feeling a little hopeful for a change."

    stop sound fadeout 10.0

    "In just a few hours, the amount of people aware of this world has doubled. Maybe the cracks are...finally starting to get a little too large to be patched up just once every few months?"
    "At this rate, it’s only a matter of time until everyone knows, but..."
    "What exactly happens when {i}that{/i} happens?"
    "A class full of teenagers isn’t going to be able to iron out any wrinkles in time, even {i}if{/i} there are girls like Nodoka and Makoto in it."
    "Maybe we’re all just doomed to keep doing this forever? But...maybe everyone knowing would give us everything we {i}want?{/i}"
    "Maybe we already {i}have{/i} everything we want? And it’s just that looming worry that someone could be taken from us at any moment that makes it so-"

    scene ayaneshowerlust16
    with dissolve

    "Oh, wait..."
    "There’s no escape from that even {i}in{/i} the real world."

    s "..."

    "At least we don’t get older here."

    if ayane_lust >= 40:
        jump ayanelust40
    else:
        scene black
        with dissolve2
        stop music fadeout 10.0

        "I finish my shower and head back to the room to find most of the girls already bundled up in their respective futons. The lone exception being, you guessed it, Ayane Amamiya."
        "I sit next to her for a moment and watch on quietly as she uses the light from her phone to illuminate a journal."
        "She rests her head on my shoulder and continues to scribble into the pages, but even those who notice don’t seem to mind."
        "Soon enough, every one of them is asleep. Even Ayane. And the last thing she wrote is this:"
        "{i}She’ll come again.{/i}"
        "{i}I know it.{/i}"

        $ renpy.end_replay()
        $ beachfive15skip = True
        $ ayane_love += 1

        "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
        "........."
        "......"
        "..."

        jump beachfive16

label ayanelust40:
    scene ayaneshowerlust17
    with dissolve
    play sound "slidedoor.mp3"

    "But then again, a world where I actually get to see my class grow up sounds interesting. Even if they’re only {i}loosely{/i} my class at this point."
    "I think Ami’s an exception to that, though. Maybe it’s just the new “father” in me saying this, but I’m kind of worried about how she’ll be when she gets older. I just hope she-"

    ay "{i}Ahem.{/i}"

    play sound "static.mp3"
    scene ayaneshowerlust18 with flash
    stop sound

    s "...Ayane?"
    ay "Present."
    s "What are you doing here?"

    scene ayaneshowerlust19
    with dissolve

    ay "What do you {i}think{/i} I’m doing here? I want my reward."
    s "But I-"
    ay "My {i}actual{/i} reward. Not shampoo."
    s "I get that. But won’t the others think it’s kind of suspicious if you vanish at the same time I go to take a shower?"
    ay "Is it wrong if I {i}want{/i} them to be?"
    s "Wrong? Not really. Mildly uncharacteristic, though."

    scene ayaneshowerlust20
    with dissolve

    ay "Uncharacteristic? Has it been so long since we’ve had a romantic rendezvous that you’ve forgotten all about me being your little sex princess?"
    s "I’m not sure if “sex princess” is a real thing."
    ay "It is and it’s me. And I deserve to have passionate love made to me for all of my hard work lately. Please and thank you."
    s "You’re right. It {i}has{/i} been too long."

    scene black
    with dissolve2

    s "Come here...{i}princess.{/i}"

    "........."
    "......"
    "..."

    scene ayaneshowerlust21
    with dissolve2

    ay "Mmng.....mlmp.....amf.....mlp......nphh......[ayanemaster]......"

    "Expecting her to jump right into my lap, I’m a little surprised when Ayane immediately drops to her knees the moment I tell her to come closer. Only a {i}little{/i} surprised, though."
    "She fits herself between my legs and pushes them apart, easing the first few inches of my cock into her dainty mouth as she gently cups my balls with her hand."
    "Caught beneath a steady stream of water from the shower, she laps up each and every bit of it that coats my shaft, replacing it with saliva and making it easier for her to suck me off."
    "I stroke her hair, maintaining eye contact as she gazes up at me with her mouth full. And the mere sight of that as her face turns red from the heat is enough to get me close to the edge."

    ay "Mmph......mmlm......not yet....I....ammf....want more....."
    s "{i}You{/i} want more?...I’m the one getting everything right now..."
    ay "Almp.....mlmf.....mmmhmmm.......I......want more...."
    ay "I love your taste, [ayanemaster].......I love.....sucking you off like this....almmf....it gets me......so wet....."
    s "I-"
    ay "Don’t make.....a shower joke....."

    scene ayaneshowerlust22 with hpunch

    s "Ah!"

    "She bites down gently. Enough to shock and surprise me but not nearly enough to actually hurt."

    ay "Mlm....amf....you like that, [ayanemaster]?.....You like when I......tease you with my teeth?...."

    "She slides more of my cock into her mouth, but proceeds to repeatedly graze my skin with her teeth, planting gentle bite after gentle bite on me."

    ay "Amm....mmm.....you {i}do{/i} like that....huh?....You want me to be a {i}feisty{/i} princess today?...."
    s "Ayane-"

    scene ayaneshowerlust23 with hpunch

    ay "Ahm!~"
    s "Ngh!"
    ay "Heheh.....I learned a new weakness....ahm!"
    s "Seriously...that’s...dangerous...."
    ay "Mmm?......Mlm.......mlmp....dangerous?.....But I’m not gonna hurt you, [ayanemaster]......I love you.....see?...."

    scene ayaneshowerlust22
    with dissolve

    ay "Chu.....chu.....chu.....chhhuuuu~"
    s "Hah......fuck......."

    "She goes from biting to kissing, planting her soft lips all over every inch of me- lingering in each spot just long enough for me to fight back to urge to grab her head and fuck her mouth."

    ay "Mm...mlm......uh-oh.....some came out already...."
    ay "You like my kisses that much, [ayanemaster]?...."

    "She plants another kiss on the tip of my cock before quickly licking the precum off of it, desperate to taste it before it’s washed away by the shower."

    ay "Mm.....mmf.....[ayanemaster]......that must feel so good.....but are you really gonna cum from just kisses?....Chu~"
    s "It’s...a little more than...{i}just{/i} kisses, Ayane...."
    ay "Mlem....mlam......chu....I could...go back to biting if you want?...."
    s "I don’t care...what you do...it’s all...too good..."
    ay "Mm...mmmmm? Oh yeahhh?...."
    ay "Then imagine waking up to this every day......Wouldn’t I be the cutest little alarm clock ever?...."
    s "You-"

    scene ayaneshowerlust23 with hpunch

    ay "Amph~"
    s "Geh!"
    ay "Heheh...you’re {i}really{/i} holding back now, huh?..."
    s "You told me...not yet..."
    ay "That’s right...just hold out...amph....for another hour....and {i}then{/i} you can cum..."

    scene ayaneshowerlust21
    with dissolve

    s "An hour?...Are you trying to kill me?..."
    ay "Mm-mm...amph...I just...slllrp....really love....sucking your {i}big{/i} cock....I never wanna stop...."
    s "Well, I’ve got some...pretty bad news for you..."
    ay "Ahm....aaahmm....yeaaaah? What is it, [ayanemaster]?..."

    "Once more, she transitions from biting to kissing."

    ay "Chu....don’t tell me....chu....you won’t last even one more minute?...."
    s "Fine...then I’ll just...keep my mouth shut and...let you find out on your own..."
    ay "Heheh......mmph.....heheheh......sllrp......yeah?...."
    ay "But if you keep your mouth shut...how am I supposed to hear those cute little moans that make me so wet?..."
    s "What...m-"

    scene ayaneshowerlust24 with hpunch

    s "Hah!"
    ay "Mm! Those ones, [ayanemaster]...that’s what I love to-"

    with sexfade
    scene ayaneshowerlust25 with cumflash
    with hpunch

    ay "MMLLPHGRGHGHRHGGMMMGHHH?!???!!!!"

    scene black
    with dissolve2

    ay "PAAAAH!!!!.....{i}Wow...{/i}"
    ay "Really couldn’t hold back anymore, h- aaah?! [ayanemaster]?!"
    s "We’re not done yet..."

    "........."
    "......"
    "..."

    scene ayaneshowerlust26
    with dissolve2

    ay "Aaah! Ahnf...mlam....aahmf! [ayanemaster]...I love you...I love you so much!"

    "I prop Ayane up against the wall and raise her body up for direct access to the hole I’ve wanted this whole time."
    "She accepts me with ease as I slip through her folds and thrust as deeply into her as her body will allow."
    "And with assisted lubrication of the cum she just sucked out of me and didn’t have time to fully swallow, I can go as hard as I want right from the get-go without having to wait for her body to adjust."

    ay "Aaah! Ahaaah! Hah! So hard! You’re gonna...drive me crazy!!! AAAAH!"

    "I get caught up in the moment and force her mouth open with mine, accidentally tasting myself to some degree but, honestly, I don’t care right now."
    "I’m completely absorbed in her and would do anything she asks of me so long as it would extend this meeting by even a second."

    ay "Aaah! Aaah! So good! So good! I’m gonna cum! I’m...hah....cumming! HAAAAH! AAAAAH!"

    with sexfade
    with sexfade
    scene ayaneshowerlust27 with cumflash
    with hpunch

    ay "NGAAAaaaaAAAAaaaAAAAaaaahhhaAAAAAAAAAAAAAAAAhhhHHH!!!!!!!!!!!!!!!!!"

    scene ayaneshowerlust28
    with dissolve

    ay "Haaah.....haaah.....haaaah....hi....."
    s "And you made fun of {i}me{/i} for being too quick..."

    scene ayaneshowerlust29
    with dissolve

    ay "Of course I did. I’m a {i}feisty{/i} princess today."
    ay "Plus, I really {i}do{/i} love sucking your cock. I just love it when you fuck me {i}more.{/i}"
    s "Then I guess you’re in luck since I don’t need to recharge today."
    ay "Oh yeah? So you’re gonna fuck me even longer than normal? Does three hours sound good? Any less and I might {i}really{/i} need to attack you in the middle of the night."
    s "You need me that bad, huh?"
    ay "I need you like {i}air.{/i} I can’t even {i}breathe{/i} without you. And the only time I feel alive is when you’re inside me like this."
    s "Yeah? Then how alive do you feel {i}now?{/i}"

    play sound "dosex.mp3"
    scene ayaneshowerlust30
    with dissolve

    ay "AAAAAH! OH MY GOD! YOU’RE SO...HARD....[ayanemaster]! WAIT!....WAIT, WAIT, WAIT! I’M SENSITIVE RIGHT-"
    s "Shut up and cum again. I know you want to."
    ay "I don’t want to! I don’t want-"

    with sexfade
    with sexfade
    scene ayaneshowerlust31 with cumflash
    with hpunch

    ay "NGHHGGHHHHHHEEGHHGHHHHHHHHH?!?!!!!!!!! MMF!....MMMM!!!!!"
    s "You poor thing...I’ll just have to keep fucking you until you get it all out of your system, huh?"
    ay "Nghhh...."

    scene ayaneshowerlust32
    with dissolve

    ay "Yeah...that’s what you’re gonna have to do..."
    ay "But you’ve got your work cut out for you this time...because I am {i}very{/i} horny today. And extremely resilient. So you might {i}actually{/i} have to break me. Think you can do it?"
    s "Two orgasms in less than five minutes makes me think I can, yeah."
    ay "Then {i}be my guest...{/i}"

    scene black with dissolve2

    "........."
    "......"
    "..."
    "{i}Not even fifteen minutes later...{/i}"

    scene ayaneshowerlust33
    with dissolve

    ay "NGAAAHCKCKLKKKGH!!!!!!!!! AAAAGHHHgGHHGHHNNGHH!!!! MMLAAMMFGGHGGHFG!!!!!!!!"
    s "I should have asked you to put your money where your mouth is. I’d be rich right now."
    ay "AAAAGHHGHHKLKLKKLL!!!! AAAAAAAAAAAAHHHHGGHHGHGHGHGH!!!!!!"

    "I’ve genuinely lost count of how many times she’s climaxed so far, but it’s definitely over fifteen since I’m averaging AT LEAST one per minute."
    "I wonder if competitive sex is a thing? I think I’d be good at it."

    ay "SEN....SEI!!!!!!!!! I CAN’T!!!!! AGAAAH! I CAN’T....ANYMORE!!!! I’M....AAAAAAH! AHHH...AGAHHHHH!!! CUMMING! CUMMING! AGAIN!!!!!!"

    with sexfade
    with sexfade
    scene ayaneshowerlust34 with cumflash
    with hpunch

    ay "Aaaah.......aaah.............aaaaah......ah......."
    s "Think you’ve got one more in you?...I’m almost there..."
    ay "Aaaah.............................ahhhhhhhh................."

    scene ayaneshowerlust35
    with dissolve
    play sound "dosex.mp3"

    ay "N..........guh.........."

    "Despite barely clinging to consciousness, Ayane's hands stay latched onto my body as her legs continue to bounce up and down while I slam into her petite frame."
    "She’s getting a little harder to hold onto for sure, but I also think that might just be because I’m losing strength."
    "I don’t think I’ve been this rough with anyone in...actually, I can’t remember if I’ve ever even been this rough {i}at all.{/i} But if I have, it was probably with Chika."
    "Regardless of that, though, I haven’t let up even once since I lifted her. And, while Ayane might be strong for her age and size, that size is barely {i}half{/i} of mine."
    "And I can only imagine the sort of toll it would take on a teenage girl to have someone like {i}me{/i} treating her like an over-sized fleshlight in a room where it’s hard to breathe in the first place."

    ay "Hah........haaaaa......aaah~"
    s "Just a little longer, princess...you’re almost free..."
    ay "Aaaah.............aaaah........"
    s "Not as {i}feisty{/i} as you were in the beginning, though."
    ay "F............"
    s "F?........"
    ay "Fuck............me..............."
    s "........"
    ay "........"
    s "Well, if you say so."

    scene ayaneshowerlust33
    with dissolve
    play sound "dosex.mp3"

    ay "HAH! HAH! HAH! HAH! YES! YESSSSSSS! FFFFFFUCK!!!!!!!! MEEEEE!!!!!!! AAAAAAAAHHHH!"

    "Ayane gets hit by her...twentieth wind (?) just as I speed up one last time and shove myself into the deepest depths of her pussy."
    "But I can feel her hands losing strength, so I’m going to have to hurry if I don’t want to finish her off on the floor."

    ay "INSIDE! INSIDE! SAFE DAY! PROMISE! CUM! LOTS! LOTS! PLEASE!"
    s "As you wish..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    ay "AAAAAaaaaaAAAaaaaAAAAAaaaaaaaAAAAAAAAHHHHHHHH!!!!!!!"

    "I spray my load so deep inside of her that her now-frail body had no choice but to swallow every last drop."
    "Just seconds after placing Ayane down on the very stool I was using when she walked in, she begins to shake like a dog left out in the rain."
    "And yes, I {i}do{/i} worry because it’s not at all implausible that I may have caused irreparable damage to her insides tonight."
    "But that worry subsides when she flashes me a thumbs-up just before slipping into complete unconsciousness."
    "And that’s good. But what’s not good is that I receive four separate blank stares when I return to the bedroom with her slumped over my shoulder and have to lay her down on her futon."

    play sound "slidedoor.mp3"

    "No one says a single word, and I disappear into my room hoping that no one ever brings it up again."
    "Goodnight."

    $ renpy.end_replay()
    $ beachfive15 = True
    $ ayane_lust += 5

    "{i}Ayane’s lust has increased by 5!{/i}"
    "........."
    "......"
    "..."

    jump beachfive16

label halloweenayane1:
    play sound "static.mp3"
    scene ayanefreakin1 with flash
    stop sound
    play music "thingsthathurt.mp3"

    ay "What do you {i}mean{/i} you have no idea what’s going on right now?! "
    ay "Everything was fine and normal a second ago and...and we were at my house! And then there was this girl who showed up and dragged Sensei away and now we’re {i}here!{/i} You remember, right?!?! RIGHT?!?!?!"
    ima "Uhh, Ayane? You maybe want to, like...take a chill-pill for a second? Because I’m not really sure what’s going on, but yelling about it in front of everyone isn’t going to-"
    ay "Sensei! {i}You{/i} remember, don’t you?! You came with me, right?! You’re still the {i}you{/i} I know, aren’t you?! The one I’m supposed to be with forever?! Please tell me you’re still here! Please!"
    a "Ayane, you’re scaring me. Please calm down."

    scene ayanefreakin2
    with dissolve

    ay "{i}Calm down?!{/i} You want me to {i}calm down?!{/i} After being sent back this far?! After everything that happened?! How the fuck am I supposed to calm down, Ami?! How?!"
    s "Ayane...if you need to go outside and talk, we can. But let the record show that I have no clue what you’re talking about and that I {i}also{/i} think you should stop yelling."

    scene ayanefreakin3
    with dissolve2

    ay "..."
    a "Did you have a bad dream or something maybe?"
    ay "...bad dream?"
    a "Well...yeah. "
    a "You said all that weird stuff about being “sent back,” but you’ve been right here with us the whole day. "
    ima "You said she’d been practicin’ her set a lot, didn’t you? Think maybe she’s just overworked herself or something like that?"
    s "I wouldn’t be surprised. She’s been trying so hard to make sure her stand-up thing will be perfect lately that {i}I{/i} could probably go up there and perform it."
    a "You might have to at this rate. The second floor is still winning and we were really relying on Ayane to come through here."

    scene ayanefreakin4
    with dissolve2

    ay "Heh..."
    a "Ayane...why not just take a seat and-"

    scene ayanefreakin5
    with dissolve2

    ay "{b}HAHAHAHAHAHAHAHAHA!!!!!! SO {i}THIS{/i} IS HOW IT WORKS!??!!??!! OH MY GOD!!! THAT’S EVEN MORE CRUEL THAN I THOUGHT!!!! HAHAHAHAHA!{/B}"
    ima "I...think I’m gonna go see if the cafe lady can make her some tea or something. Chamomile’s supposed to help with nerves, right?"

    scene ayanefreakin6
    with dissolve

    ay "Yes! Chamomile! Bring me all the fucking chamomile in the world! Because I’m sure fucking going to need it if I’m going to have to sit through both of these two breaking into a million fucking pieces again!"

    scene ayanefreakin7
    with dissolve

    ima "On it. Nothing to see here, girls! Everybody mind your own business until Ayane calms down, please! Thanks!"
    ay "You still love me at least, right?"
    s "Ayane, what in the world are you talking about?"
    ay "Things I can’t say in front of everyone else. Things that we do when we’re alone. You still love me, right? "
    ay "Because you look different. You smell different. But I know it’s {i}you.{/i} It’s you, right? Where were we just a minute ago? What was I wearing? Where did that girl take you?"
    a "..."
    s "..."

    scene ayanefreakin8
    with dissolve

    ay "Please don’t make me start all over..."
    ay "{i}Please{/i} be you."
    m "Molly, move."
    mo "Wha- Bronya!? We’re supposed to be in love! You can’t just push past me like-"

    scene ayanefreakin9
    with dissolve

    m "Ayane...shut the fuck up."
    ay "...huh?"

    play sound "static.mp3"
    scene ayanefreakin10 with flash
    stop sound

    m "You. Me. Outside. Now."
    ay "..."
    ay "Are you..."
    ay "Who I {i}think{/i} you are?..."
    m "That’s a great question. Especially since you’re decidedly {i}not{/i} who I thought you were just a second ago. But that doesn’t change the fact that you’re saying too much. "
    ay "I’m sorry! I’m just...really scared and...{i}confused{/i} and...everything’s suddenly different, but...it’s the {i}same{/i} and-"
    m "Yeah. It’s very, very sad. But I’m going to need you to grow the fuck up for a second and talk to me {i}outside{/i} because it’s dangerous for you to keep throwing your little temper tantrum in here."
    ay "Temper...tantrum? "
    m "Outside. {i}Now.{/i}"

    play sound "static.mp3"
    scene ayanefreakin11 with flash
    stop sound

    s "..."
    a "..."
    s "What the hell was that about?"
    a "I have no idea. I’ve never seen Ayane get that...{i}crazy{/i} before."
    a "You don’t think what Miss Imai said was true about the whole...overworking thing, do you? Because Ayane always works hard. Just...{i}this...{/i}"
    s "Yeah...I hope everything’s okay. Are you sure you don’t want to go out there with them, though?"
    a "Not really. Maya scares me when she gets all serious like that."

    play sound "static.mp3"
    scene ayanefreakin12 with flash
    stop sound

    a "{i}Besides, I doubt I’d have any idea what the two of them are talking about anyway...{/i}"
    m "Okay, so...To start, mind explaining to me what the fuck is going on here?"
    ay "Is it...really {i}you,{/i} Maya?..."
    m "What kind of question is that? Who else would I be? "
    ay "Well...still {i}you,{/i} but...like...a different version? One that’s...way more upfront about her feelings for Sensei and-"

    scene ayanefreakin13
    with dissolve

    m "H...How do you even know about that?! I’ve barely said a word to or {i}about{/i} him in years! And especially not to you!"
    ay "But in {i}my{/i} world you did!"

    scene ayanefreakin14
    with dissolve

    m "Huh?..."
    ay "In {i}my{/i} world, you two..."
    ay "Well, it pains me to admit it, but you two were in love. You were still a bitch about it, of course. But I knew how you felt and you knew that {i}I{/i} knew that."
    m "I doubt what you witnessed was “love.” I was probably just going through another lustful rage. That happens sometimes. But...wait, how the fuck are {i}you{/i} involved now? Do you know about the resets?"

    scene ayanefreakin15
    with dissolve

    ay "Yeah...Do you think that’s what’s...happening right now?"
    m "..."
    ay "Also, can I hug you? Because it’s been a long time since I’ve seen the {i}real{/i} you and...I miss you a lot."
    m "Maybe later. I’m just...I need a minute to try and wrap my head around everything right now."
    ay "You and me both. One second, I’m at {i}one{/i} party. The next, I’m at a party several years before that and no one remembers where we were just a second ago. Unless {i}you-{/i}"
    m "No...I’ve been here the whole time. My last reset was months ago. But nobody else is supposed to know about them here. "
    ay "Not even Sensei?"
    m "{i}Definitely{/i} not Sensei. He’s too busy fucking Ami to figure any of that stuff out. And I doubt he’ll-"

    scene ayanefreakin16
    with dissolve2

    m "Wait..."
    m "Was that you...implying he actually figures it out in your timeline? Or...is that just wishful thinking on my end?"
    ay "Where or...{i}when{/i} I come from, he knows. Makoto too. And then...Yumi sometimes and...Tsuneyo sometimes and...I {i}thought{/i} Sana did, but..."

    scene ayanefreakin17
    with dissolve

    m "And you said I...loved him?"
    ay "Yeah...and I can promise you it wasn’t just a “lustful rampage” like you suggested."

    scene ayanefreakin18
    with dissolve2

    m "Is it nice there?..."
    ay "As nice as it...{i}can{/i} be when you’re caught in a timeloop, I guess."
    m "So...he and I are..."
    m "We’re {i}together{/i} there?..."
    ay "..."
    m "Why are you hesitating? What happened? What did he do? What did {i}I{/i} do? Why aren’t your eyes filled with joy and envy describing this to me?"
    ay "Maya, I don’t know how you’re going to react to this, so I’m just going to come out and say it..."
    ay "You get sent back during a reset. And the {i}you{/i} who takes your place is just as oblivious to all of this as everyone here."

    scene ayanefreakin19
    with dissolve

    m "Wait, {i}I{/i} get sent back?! How?! That’s not how it’s supposed to work! What the fuck happened?!"
    ay "I, uhh..."
    ay "I’m pretty sure you guys had sex on the roof."
    m "..."
    ay "..."

    scene ayanefreakin20
    with dissolve2

    m "You’re joking, right?"
    ay "I mean...I didn’t {i}see{/i} what happened...just the...the aftermath..."

    play sound "static.mp3"
    scene ayanefreakin21 with flash
    stop sound

    m "{b}{size=+20}FUCKING HELL! SERIOUSLY, ME?!{/b}"

    scene ayanefreakin22
    with dissolve

    m "Am I that bad at controlling myself even a gajillion years into the future where I’d risk everything to just fuck him one more time?! Does this lust know no bounds?!"
    ay "Uhh...I...I don’t know?"
    m "Do you have any idea how many Senseis I’ve broken, Ayane? Because it’s a fucking lot! So if {i}I’m{/i} actually the one who broke this time, I probably deserve it! But still!"

    play sound "static.mp3"
    scene ayanefreakin23 with flash
    stop sound

    ay "Aren’t there...more pressing matters to talk about than your sexual relationship with Sensei?"
    m "Yeah, we’ll get to those. For now, I want to hear more about what happened in {i}your{/i} world. Because I can’t even remember the last time there was any sort of new development {i}here.{/i}"
    m "What happened to {i}him{/i} when I vanished? Did he blame himself? He probably did, didn’t he?"
    ay "He kind of, just...shut himself off from everyone but Ami for a few months. He still hasn’t fully recovered really. It’s been...probably a year since then."
    m "Ugh! I can’t believe I fucking did that! Guess it just goes to show no matter {i}how{/i} many times I tell myself I’ll be able to keep my distance when he comes back, I’ll still fucking crumble in the end!"
    m "But this is huge, Ayane. This means it’s {i}possible.{/i} This means there’s a method to all of this madness and that through enough trial and error, things can actually start to work!"
    m "Of course, it will probably be millions of years until it actually does considering my luck, but {i}still!{/i} I can find him! "
    ay "..."
    m "What? Why do you look so sad?"
    ay "Because I don’t want to wait millions of years...I want him {i}now.{/i}"

    scene ayanefreakin24
    with dissolve

    m "Yeah, well get in line. You’ve been without him for like ten minutes while I’ve legitimately lost track of the last time there was even someone I could delude myself into believing is him here."
    ay "That doesn’t make it any less scary for me, Maya! And also, I don’t understand what that means! Aren’t they {i}all{/i} Sensei? Just at...different points in time or something? Like, isn’t that what being “reset” means?"
    m "Maybe for you and me and everyone else with a vagina. He’s the exception to that. All {i}this{/i} one does is fuck Ami and watch football."

    scene ayanefreakin25
    with dissolve

    ay "{i}What?{/i}"
    m "I mean, they all fuck Ami. The football thing is, like...seriously annoying though. I have no idea how this one made it so far. Just bring on the next one already."
    ay "Maya...I really miss you."

    scene ayanefreakin26
    with dissolve

    m "I mean...I wish I could say the same, but...you’re just Ayane to me."
    m "Do we have a...better relationship where you’re from? Do I become less mean once I finally find what I’m looking for? Also, {i}Yumi?{/i} Really? How does {i}she{/i} become involved?"
    ay "I’m not really sure which of those questions to answer first, so I’ll just say that our relationship is still mostly one-sided. I doubt you...cared much about me there either."
    ay "But I’d have never learned about this world if it wasn’t for you, so...I owe you a lot of thanks. And I never got to really say that before you disappeared."
    m "Don’t thank me for unintentionally dragging you into an eternity worth of misery and regretful encounters with people who resemble the man you love. If I really did that, I ruined your life."
    ay "It’s not like you went out of your way to get me involved. It was kind of the opposite, actually. Like you never wanted me to be involved to begin with."
    m "Well, yeah. Why would I want to drag anyone else into this mess? It sucks. The best case scenario is you being repeatedly sent back every few semesters so you don’t have to deal with it."
    m "Like sure, you might have to deal with Sensei fucking Ami and binging football for a few months sometimes. But eventually, there’s going to be one who likes blondes and you’ll get to be happy again for a little while."
    ay "That’s not {i}true{/i} happiness, though."

    scene ayanefreakin27
    with dissolve

    m "But you’ll {i}feel{/i} like it is because you’ll be none the wiser to what’s actually going on behind the scenes. Trust me, I’m right. "
    ay "Well, even if you are...I don’t regret learning. I don’t regret falling even harder for him than I already had before all of this started."
    m "Sorry, should I take this as an admission that you’re {i}also{/i} fucking my boyfriend in the future where he and I get back together?"

    scene ayanefreakin28
    with dissolve

    ay "..."
    m "..."
    m "He’s fucking everyone, isn’t he?"
    ay "You said it, not me."

    scene ayanefreakin29
    with dissolve

    m "This rage will fuel me for millennia."
    ay "O-On the bright side! He’d definitely pick you over everyone else if he really had to!"

    scene ayanefreakin30
    with dissolve

    m "Well, duh. That’s how being star-crossed lovers works. I just never realized other stars would start getting dragged into our tragic love story and turn this into some sort of everlasting meteor shower."
    ay "So do you, like...want to try and figure out how to go back {i}together{/i} then?"

    scene ayanefreakin31
    with dissolve

    m "Ayane..."
    ay "We {i}can,{/i} right? Like...this is probably just another one of those weird...reset puzzle things! And we just have to solve it and we’ll go right back to the hyper-depressive harem comedy where we belong! "

    scene ayanefreakin32
    with dissolve

    m "..."
    ay "D-Don’t look at me like that! This is only temporary! I’m...I’m here for a reason! I have to be! So I’ll just...stay positive and-"
    m "Just stop, okay?"

    scene ayanefreakin33
    with dissolve2

    m "Getting your hopes up is...the worst thing you can do here."
    m "Just take solace in the fact that you have someone who won’t look at you like you’re insane whenever you talk about the world ending."
    m "Plus, I doubt the “me” who took my place would be happy to be swapped out for a more jaded, narcissistic version."
    ay "But she’ll become that way on her own...won’t she? Just like you did."
    m "Then let her."
    ay "Maya...you don’t mean that."

    scene ayanefreakin34
    with dissolve

    m "Oh, I know. I would {i}gladly{/i} screw myself over if it meant getting out of this loop. I just felt like I was supposed to say something like that there or it might negatively affect my future in some way."
    ay "Oh."
    m "We’re still fucked, though. I have no idea when the next reset is coming. And if {i}that{/i} was the catalyst that sent you here, I imagine it’ll have to be another that takes you back."
    ay "So am I just...supposed to wait here until that happens? Isn’t there something we can do?..."

    scene ayanefreakin35
    with dissolve

    m "..."
    ay "..."
    m "I don’t know. Do you like football?"

    $ renpy.end_replay()
    $ halloweenayane1 = True

    stop music

    jump halloweenfive10

label halloweenayane2:
    m "You made it {i}how{/i} many years into the loop?"

    play sound "static.mp3"
    scene ayanemayahallyeah1 with flash
    stop sound
    play music "undersea.mp3"

    ay "I think it’s like...five? Four maybe? I’d have to ask Sensei. But even then, he always talks about how it all just blurs together. I’m kind of starting to see where he’s coming from too."
    m "I guess it really is him then. That’s further than I’ve ever heard of at least. None of the imposters have ever made it past the fourth."

    scene ayanemayahallyeah2
    with dissolve

    ay "The fourth? But {i}my{/i} Maya told me the record was two. "
    m "Then either your Maya was wrong, lying, or hadn’t learned enough yet. But I’m going to hope that last part isn’t accurate as it would imply the timeline you come from is {i}not{/i} the one that ends this."
    m "I think. I’m not sure. Time is weird. But my record is four."
    ay "And what happened in that loop? Do you remember? Or is that like a gajillion years in the past by now?"

    scene ayanemayahallyeah3
    with dissolve

    m "That one was odd. I’m not sure Sensei ever really left his house. But I remember Ami always being kind of pissed off too, so I doubt it was because he was too busy screwing her."

    scene ayanemayahallyeah4
    with dissolve

    m "Watch out for her, by the way. She tends to kill people when she doesn’t get what she wants."
    ay "Yeah...my Maya already told me about that. But...I don’t know. "
    ay "Like, I’m not saying she was lying. I think my Maya genuinely {i}did{/i} see something like that. But...I think the Ami from my Kumon-mi might be different."
    m "And if I had a dollar for every time I thought that, I’d be able to buy every melon bread in the city."
    ay "You’d need to convert all those dollars to yen first. And the exchange fees can get pretty high in some places."
    m "Okay, so I’d be able to buy {i}most{/i} of the melon bread in the city. The fact remains — you shouldn’t ever trust her. And you shouldn’t ever trust {i}me{/i} either. "
    m "I’m extremely selfish and won’t hesitate to throw you under the bus for my own personal gain."
    ay "And you’re just going to flat out admit that?"

    scene ayanemayahallyeah5
    with dissolve

    m "That actually felt pretty good to get off my chest."
    ay "Well, I’m glad {i}you{/i} feel good at least. Because finding out there is literally no one for me to trust back home except Sensei isn’t really a great motivator for continuing my journey through time."

    scene ayanemayahallyeah6
    with dissolve

    m "It isn’t my job to motivate you. It’s my job to fill you in on as much as I possibly can {i}while{/i} I can in the event that you {i}do{/i} get sent back."
    m "And seeing as you’ve managed to make it all the way here, I have no reason to doubt that you’re almost as big of a player in this as I am. But {i}your{/i} Maya probably won’t think that."

    scene ayanemayahallyeah7
    with dissolve

    m "I’m stubborn. And I doubt I’d have an easy time just accepting that someone like you could be dragged into this out of nowhere. "
    m "The only reason I can do that {i}here{/i} is because you effectively just climbed out of a time machine in front of me."
    ay "Well, it’s definitely true that my Maya didn’t immediately accept me. She thought I must have been pregnant or something since she and Sensei were the only ones that ever made it to the roof."
    m "Yeah, that sounds about right. So forget everything she ever said to you. Also, please stop subtly reminding me that you’re actively sleeping with the man I love or I am going to subtly strangle you to death."
    ay "This has to get easier eventually, doesn’t it?"

    scene ayanemayahallyeah8
    with dissolve

    m "What part exactly?"
    ay "I don’t know...accepting that this is the way things are? It’s a lot to shoulder all by yourself. I have no idea how you managed to keep it together for as long as you did."
    m "I didn’t."

    scene ayanemayahallyeah9
    with dissolve

    ay "You didn’t?"
    m "Absolutely not. Do you think I would have fucked so many Senseis to death if I was emotionally stable the whole time? Hell no. I’ve made more mistakes than I can even count. "

    scene ayanemayahallyeah10
    with dissolve

    m "I’m also pretty sure I literally strangled one to death in the middle of an orgasm once. But that one was really vulgar so he had it coming."
    ay "I’m...surprised you even had the strength to do that."
    m "Rope helps. Anyway, that’s beside the point."
    ay "Well, what {i}is{/i} the point? Because now it just feels like you subtly bragging to {i}me{/i} about having sex with the man I love."

    scene ayanemayahallyeah11
    with dissolve

    m "I guess in a sense I am."
    ay "Why are you smiling? My Maya doesn’t smile. "
    m "She does when she feels safe. I imagine she just never felt that way with you looming over her shoulder, threatening to take away the role she spent countless years getting comfortable in."
    m "It’s nothing personal. So allow me to apologize on her-slash-my behalf now. I’m a very, {i}very{/i} selfish girl. And I’ve seen what happens in worlds where Ayane Amamiya gets her wish."

    scene ayanemayahallyeah12
    with dissolve

    ay "You have? "
    m "I have."
    ay "Well...what wish? Because I have a lot. Do Sensei and I get married? Do we have kids? How many? If the record is four loops, that should be time for {i}at least{/i} two and-"
    m "You never get married. You’re still in high school at the end of the day."

    scene ayanemayahallyeah13
    with dissolve

    m "And while I’ve never personally {i}seen{/i} your body become infested with the life-ending parasite known as a “human child,” I wouldn’t be surprised if it happened."
    m "I’ve watched the two of you fall hopelessly in love more times than I can count."
    ay "..."

    scene ayanemayahallyeah14
    with dissolve

    m "But, then again, none of those instances were with the {i}real{/i} Sensei. So I guess your “love” is just not nearly as real and unbending as mine."
    ay "Which one of us has had world-ending sex with fake Senseis again?"

    scene ayanemayahallyeah15
    with dissolve

    m "Me, obviously. But you’ve collectively screwed more of them than I have. I’m just better at it."
    ay "Oh..."

    scene ayanemayahallyeah16
    with dissolve

    ay "{i}Oh...{/i}"
    ay "Ew...I feel super gross all of a sudden. I really wish you hadn’t told me that."
    m "The shame will be short-lived, don’t worry. Or at least it is for me as I’ve decided it’s acceptable to blame one’s temporary uncharacteristic behavior on just what we have to go through here."
    m "Cheating on your significant other with someone wearing their skin is more forgivable than someone who isn’t, right?"

    scene ayanemayahallyeah17
    with dissolve

    ay "I guess so. So I’ll just tell Sensei that his Maya approves him screwing the new Maya clone and we can all live happily ever after."
    m "I take it back. All cheating is bad. And I will spend the next thousand years repenting for my transgressions."

    scene ayanemayahallyeah18
    with dissolve

    ay "..."
    m "..."

    scene ayanemayahallyeah19
    with dissolve

    aymay "Pfft!"
    ay "Hahah! Hahahah!..."
    m "Heh...hahah...heh..."

    scene ayanemayahallyeah20
    with dissolve

    ay "I wish..."
    ay "I wish we got to laugh like this before you went away."
    m "Yeah..."

    scene black
    with dissolve2

    m "Maybe one day we’ll be able to..."
    m "Without feeling like the world’s about to end."

    "........."
    "......"
    "..."

    scene ayanemayahallyeah21
    with dissolve2

    ay "Oh, we got so caught up in talking about our pasts that I forgot to ask. Just what are we doing here exactly?"
    m "Looking for something that might help."
    ay "And we’re looking in an...empty classroom?"
    m "Do you not see me fumbling through this locker right now? Just trust me, okay?"

    scene ayanemayahallyeah22
    with dissolve

    ay "But you literally just told me not to trust you like five minutes ago."
    m "{i}No,{/i} I told you not to trust the {i}other{/i} me. {i}This{/i} me you can trust because {i}this{/i} me believes you. Which is the reason I brought you here in the first place."
    ay "But where is {i}here?{/i} What are you looking for?"

    scene ayanemayahallyeah23
    with dissolve

    m "Notes."

    play sound "static.mp3"
    scene ayanemayahallyeah24 with flash
    stop sound

    ay "I don’t think now is the time to be studying, Maya."
    m "Shut up. Surely you know that’s not what I’m talking about. I’m looking for {i}my{/i} notes — on time, resets, and the like. I’ve been collecting them for as long as I’ve been here."

    scene ayanemayahallyeah25
    with dissolve

    ay "Yeah, I’m not really sure if I want to wait around while you read through an eternity’s worth of notes. That sounds like it could take a while."
    m "Maybe, if I had the organizational skills of a child. But I’m sure I have some sort of...emergency instructional book somewhere. That sounds like a thing I’d have probably made by now."

    play sound "static.mp3"
    scene ayanemayahallyeah26 with flash
    stop sound

    ay "Instructions?! You made instructions for this?! That’s great! We-"
    m "Don’t jump for joy just yet. I still haven’t found anything and-"
    m "Oh. Oh, never mind. There it is. I put it right where I figured I would."
    ay "Well, hurry up and read it then! I want to go home!"
    m "Again, no jumping for joy. I can’t remember the last time I opened this book and, even if I could, it’s all just speculation anyway. It’s not like I know how to fix this."
    m "And, for all I know, we might not even be {i}able{/i} to."

    play sound "static.mp3"
    scene ayanemayahallyeah27 with flash
    stop sound

    ay "What do you mean we might not be able to?..."

    play sound "static.mp3"
    scene ayanemayahallyeah28 with flash
    stop sound

    m "I mean you might be stuck here forever. Has that part really not settled in yet? I thought we were on the same page there."

    play sound "static.mp3"
    scene ayanemayahallyeah29 with flash
    stop sound

    ay "No, Maya! I guess that hadn’t settled in yet! I’ve been too busy trying to stay optimistic since that’s the only way I’ve learned how to cope with the never-ending tragedy that comes with being a perpetual teenager!"
    m "Okay, well then you definitely don’t want to know what was in my “emergency instructions” book just now."
    ay "What’s that supposed to mean?! What did it say?!"
    m "You really don’t want to know, Ayane."
    ay "So you can keep a bunch of secret notes on how to fix the world, but you won’t even tell me what they say?! What happened to filling me in on as much as you can {i}while{/i} you can?! What changed?!"
    ay "You just want me here forever, don’t you?! I bet your “notes” said you wouldn’t be able to come! And you can’t stand that {i}I’d{/i} get to go back to the person you’ve been chasing after forever while {i}you{/i} stay here!"
    ay "That’s what it is, isn’t it?! You’re holding me back again! Just like you used to whenever I tried to help! Nothing’s changed! You’re still the same selfish, clingy bitch you’ve always-"

    play sound "slap.mp3"
    scene ayanemayahallyeah30 with hpunch

    ay "NGH?!?!?!"

    scene ayanemayahallyeah31
    with dissolve2

    ay "Ow! What the hell, Maya?!"
    m "Are you done yet? Or will yelling at me for a little while longer help get all of {i}this{/i} out of your system?"

    scene ayanemayahallyeah32
    with dissolve

    ay "I’m sorry...I just...I got my hopes up when I heard you’d prepared for this. That’s all."
    m "Well, I warned you not to jump for joy. And it turns out that doing so was the correct move, even if the end result didn’t really change."
    ay "I take it that means...{i}even older{/i} Maya didn’t know what to do for a case like this then?"

    scene ayanemayahallyeah33
    with dissolve

    m "Ayane, I’ve been writing everything down for so long that it’s rare for me to remember {i}any{/i} of it. It’s practically just a formality at this point. Or something to read when I get bored."
    m "The initial idea was to chronicle everything. To keep a log of what happens and when. Of who does what in which loop since I figured {i}knowing{/i} this would help. And maybe one day it will."
    m "That’s why I came here. I wanted today to be that day. But I know now that it’s not going to be since...there was nothing {i}in{/i} that book yet."

    scene ayanemayahallyeah34
    with dissolve

    ay "N...Nothing?..."
    m "Nothing. So either I’d never gotten around to recording anything or past-Maya thought this would be a funny joke. And it’s not. So I’m still not funny all this time later."
    ay "...You’re kidding."
    m "I’m not. But again, I’m not funny. So you probably wouldn’t even know if I was."
    ay "So you brought me over here...to open up a blank notebook...and tell me I’m screwed?"

    scene ayanemayahallyeah35
    with dissolve

    m "I mean...that wasn’t the intention. But yeah, I guess that’s kind of what happened."
    ay "I don’t believe this..."
    m "We can keep looking, Ayane. I’ve been hiding things in here forever. There’s a room in the basement I keep all of the older stuff in. Maybe there’s something in there that can help?"
    ay "You don’t know?..."

    scene ayanemayahallyeah36
    with dissolve

    m "What- do {i}you{/i} remember everything you’ve ever written down? Because, even if by some stretch you {i}do,{/i} multiply that by a trillion and {i}then{/i} try."
    m "The human mind can only hold so much information. And with limited space for memories, I need to be forgiven for not holding onto every single one of them."
    ay "But this isn’t a memory we’re talking about...this is my ticket out of here..."
    m "And {i}why{/i} is that a thing I would have? I’d obviously have escaped by now if I knew how, Ayane. And while I’m {i}very sorry{/i} the first book I opened didn’t have the answer, maybe there’s...one that will?"
    ay "I think you’re going to have to hit me again because I am about to say some very mean things to you."

    scene ayanemayahallyeah37
    with dissolve

    m "I’m sorry, okay?..."
    m "Maybe I just...put that book there so I {i}could{/i} write something in it once I knew? But the fact that there’s nothing just-"
    ay "It means you’ve never learned anything..."
    ay "You don’t know what to do..."
    ay "And I really might actually be stuck here."

    scene ayanemayahallyeah38
    with dissolve

    m "We...We won’t know that for sure until the next reset comes. I still think that’s your best bet in terms of “escaping.”"
    ay "But then we won’t be leaving together..."

    scene ayanemayahallyeah39
    with dissolve

    m "..."
    m "Probably not...no."
    ay "{i}Hah...{/i}"
    m "..."
    ay "I’m sorry for raising my voice...I’m just really scared of..."
    ay "You know..."
    m "Yeah..."

    scene ayanemayahallyeah40
    with dissolve

    ay "Maya? What are you-"

    play sound "static.mp3"
    scene ayanemayahallyeah27 with flash
    stop sound

    m "There’s something in here I want you to hold onto...in the event that you {i}do{/i} return to your timeline. But it’s not for you to keep, do you understand? You need to give it to me when you get there."
    m "If you do that, I’ll know that I can trust you."
    ay "But...But is that even possible? Bringing physical objects from one timeline to another?"
    m "Hell if I know. Everything I do is a shot in the dark at this point. But there’s only one way of finding out, and this thing has done nothing but collect dust for {i}years{/i} now."

    play sound "static.mp3"
    scene ayanemayahallyeah41 with flash
    stop sound

    m "Here."
    ay "This is..."
    ay "Your...scarf?..."
    m "I take it you’ve already seen it then?"
    ay "Yeah...Sensei bought this for you. You treasure it. You can’t just...give it to me. It’s too important."
    m "That’s exactly {i}why{/i} I’m giving it to you."

    scene ayanemayahallyeah42
    with dissolve

    ay "But it might not even work! And on the off chance it {i}does,{/i} I doubt the Maya in my timeline even knows about it! It’s spring there! She hasn’t been around for a winter yet!"
    m "That’s precisely why you need to-"

    scene ayanemayahallyeah43
    with dissolve

    m "Wait, spring? You guys have spring there?"
    ay "Oh, yeah. I guess you weren’t ever around for that."
    m "What’s the weather like? Have the cherry blossoms started blooming yet?"
    ay "It’s nice. And I haven’t seen any yet, but there aren’t really a lot of places to see them in- is that really important right now?"

    scene ayanemayahallyeah44
    with dissolve

    m "Oh, sorry. No. Just...give this to that other me if you manage to bring it back."
    m "I’m sure it sounds like something out of a movie, but this might be the “shock” I need to pull me back to reality. Better than just letting my clone continue to fuck my boyfriend at least."
    ay "Do you really think it’ll work?"
    m "Probably not, but it’s worth a shot. And it’ll get me to like you a whole lot more too."
    ay "Are you saying my Maya doesn’t like me?"
    m "Probably not, to be honest. I tend to block out everyone who isn’t Sensei or Ami."

    stop music fadeout 15.0

    ay "Why Ami though? If you’ve seen her at her worst so many times and...have literally witnessed her kill people...how is she closer to your heart than me? I’ve always liked you, Maya. Even before you were {i}you.{/i}"
    m "Just take the fucking scarf, okay? We have like six million boxes to go through and it’s only a matter of time until people start calling us to ask where we are."
    ay "What’ll we tell them when they do?"
    m "Whatever you want. I really don’t care."

    scene black
    with dissolve2

    ay "Then I’m telling them we’re on a date."
    m "Ew. Why that?"
    ay "Because we make a good couple, obviously. And no one will ask any questions if they think we’re spending a passionate night of-"

    play sound "slap.mp3"

    ay "Ouch! Maya! Did you really have to hit me again?!"
    m "Just take the damn scarf!"

    $ renpy.end_replay()
    $ halloweenayane2 = True

    jump halloweenfive12

label halloweenayane3:
    play sound "static.mp3"
    scene ayaneopendoor1 with flash
    stop sound
    play music "itsingsinitssleep.mp3"

    "It all used to look like this. "
    "Long ago, when the sun still shone — when the sweat on your skin made it stick to the sleeves of that old blazer as you wandered mindlessly through the better part of this world."
    "I assume you barely remember that now. And on the off chance you do, I imagine it’s because you forced yourself to. "
    "Either something spoke to you or {i}you{/i} spoke to something. So either this worm has always been a part of you or you went back to find it."
    "Are you happy now — peering into the mason jar you used to recreate its habitat? Carefully combing through all of the information you can find in an effort to know a little more than you did before?"
    "A worm is just a worm, you know. And while I’m glad you’d take it upon yourself to go so far out of your way to properly care for it, I’d be foolish to not advise you that there’s always a chance this could lead to regret."
    "Because right now, there are thousands of other people on the Internet talking about worms — spewing their thoughts and feelings out into the ether. What one person says is right, another says is wrong."
    "But it’s not like the worm can ever tell you which leaves it prefers, so there’s no way of knowing if you chose the right ones."
    "If you don’t like worms, maybe you like fleas. Maybe you found a handful of those. Maybe you’re starting a circus."
    "So you send your cats out to wander the fields, using a comb to weed them all out several days later."
    "But the thing with fleas is that you’ll never be able to comb {i}all{/i} of them out. You can go through that fur until your cat is bald and you’ll still find their dirt on its skin."
    "What this means is that time is limited for everyone. Even the ones you may have believed could live on forever. The truth is they won’t. The truth is they’ll be forgotten. {i}All{/i} of this will be forgotten."
    "But that doesn’t change the pursuit of knowledge. It doesn’t change that curiosity alone is the driving force behind the success of man. But cats are not the only thing curiosity can kill."
    "So the goal then becomes to dig up some sort of happy medium. To find two people who know about worms and are willing to reach an agreement. Or to start up a flea sideshow instead of a circus."
    "There are so many things you can do. There are so many worlds {i}you{/i} can build. Yet you long for the days of zmr_005_LUT32 with that heavy-left slider because {i}that{/i} is when things felt simple."
    "{i}That{/i} is when you {i}could{/i} wander through the better part of town, asking yourself questions like “Why’s that one the way it is?” or “I wonder what will happen when that thing happens?” "
    "Simple questions. {i}Easy{/i} questions. Questions that seem like {i}nothing{/i} now that there’s a divine compendium and countless threads running simultaneously while a single red one still hangs overhead."
    "It’s so high up you don’t know when you’ll reach it. {i}I{/i} don’t know when you’ll reach it. And every day, it gets further and further away."
    "This is not the world that you knew. Just like those long hallways that faintly smelled of chlorine and scraggly green carpets also seem impossible now. It’s because they {i}are.{/i}"
    "Everything changes whether you want it to or not. Sometimes it’s for the better. Sometimes it’s not. But it’s hard to ever really know that until you make it to the next world."
    "I wonder what color the next carpet will be?"
    "I wonder if I’ll like it."
    "I don’t {i}know{/i} if I’ll like it."
    "I just know that if I don’t make it there, the next click will be me."
    "..."
    "Trash is collected every Tuesday and Friday."
    "The other five days, I am waiting."
    "It’s not a hint. It’s motivation."
    "For those days when everything tastes grey."
    "..."
    "One day, I hope someone will get it."
    "Until then, I’ll have a soliloquy to keep me company."
    "It has no mouth. It can not see."
    "But {i}God{/i} does it hold me tightly."

    play sound "static.mp3"
    scene ayaneopendoor2 with flash
    stop sound

    ay "So I guess we’re just headed back to the hotel now?..."
    m "We can come back to school tomorrow night if you feel like reading again. It’s trickier getting into the basement during school hours."
    ay "I’m confused as to how you can keep so much stuff down there in the first place. Has anyone ever, like...tried moving any of it? I’m sure the sports clubs have to go into the basement from time to time, don’t they?"
    m "You {i}should{/i} be confused. It’s a confusing subject. And if you want my honest answer, I’d say it’s because the rules of this world and {i}logic{/i} as a whole don’t really apply to me."
    m "Which means that, by extension, they probably don’t apply to {i}you{/i} either now or I’m just flat out wrong.  Probably the former if I had to guess."
    ay "I’d guess the latter. You were wrong pretty frequently in my world. And you were wrong about that thing with the emergency escape instructions earlier too."
    m "A watched clock is right twice a day, Ayane."

    scene ayaneopendoor3
    with dissolve

    ay "I’m pretty sure you used that phrase incorrectly as well."
    m "That phrase is incorrect on a conceptual basis when time is quite literally just a thing we made up. How can a clock be right when there’s no correct answer?"
    ay "Can we not get all philosophical right now? I’ve had a long, miserable day and I need to turn my mind off for a few minutes so I can get a tiny reprieve before my nightly panic attack."
    m "Would you rather just sleep at the dorms instead? I can’t imagine being in an environment as loud as that hotel will do you any favors if you’re trying to take your mind {i}off{/i} of things."
    ay "Will you come with me if I say yes?"

    scene ayaneopendoor4
    with dissolve

    m "Sure. "
    m "You’re the closest thing I have to a friend in this world. Even if the me who befriended you is no longer present. "
    m "The fact remains that you’re the only person who understands me. And that’s surely good for something, isn’t it?"
    ay "Y...Yeah. You just...never really put it that way when you were alive."

    scene ayaneopendoor5
    with dissolve

    ay "F...Forgive me for wording it that way, though. It’s not like you {i}technically{/i} died. It’s just easier to say that than “you were suspiciously replaced with a clone” every time."
    m "Just because I didn’t say it doesn’t mean I never thought it. And even if I doubted you, which I most assuredly did, I likely enjoyed your company on at least {i}some{/i} level."

    scene ayaneopendoor6
    with dissolve

    ay "Maybe we can sleep in the same bed then?!"
    m "Denied."
    ay "And we can hold each other and cry about how we’re the only two people in this universe who know about how cruel and unfair and evil it is!"
    m "Denied again. Did you not hear me the first time?"

    scene ayaneopendoor7
    with dissolve

    ay "Yay! We’re going to have so much fun together! I’m gonna love you {i}so{/i} hard that you won’t even know what hit you!"
    m "You’re disgusting. I take back all of the compassionate things I said. Please leave me alone for the rest of your time on this planet."

    scene ayaneopendoor8
    with dissolve

    ay "I’m only teasing you, obviously. I know you like your space. At least with everyone not named Ami. You’ve never {i}once{/i} put up a fight when {i}she{/i} asks to share a bed. "
    ay "{i}Me,{/i} though? Pfft. Somebody’s sleeping on the floor."
    m "Is that a thing we did often where you come from? "

    scene ayaneopendoor9
    with dissolve

    ay "Wait, is it {i}not{/i} a thing you do often here? Are you and Ami not particularly close in this timeline? "
    m "Not in this one, no. She’s barely shown an interest in me with Sensei taking up her every waking moment."

    scene ayaneopendoor10
    with dissolve

    m "The loop before this one was the opposite, though. We were...certainly close there."
    ay "Yeah, it’s super weird to hear that you’re not here. I kind of just always associate the two of you together. "
    ay "I guess you started “falling out of love” in the last world, though. Right before the whole character swap thing happened."

    scene ayaneopendoor11
    with dissolve

    m "What do you mean by that? "
    ay "It wasn’t anything personal, I don’t think. Ami got weird with everybody. And it only got worse after you died."
    ay "Like, she’s always been a little crazy. But at one point, it seemed like she was almost trying to, like, get Sensei to hate us or something."
    m "You didn’t tell her about the loops, did you?"
    ay "Of course not. You always said not to and then got all intense about how she’d kill me and everyone else or something."
    m "Hmm..."
    m "Yeah, I’m not really sure then-"
    y "Aaaah! Finally!"

    play sound "static.mp3"
    scene ayaneopendoor12 with flash
    stop sound

    ay "Yumi? What’s-"
    y "I’ve been lookin’ all over the fuckin’ place for you, Blondie! Tried like three different phones and none of ‘em worked! Did the thing happen?! It did, right?! Is it always this fuckin’ disorienting?!"
    ay "The...thing?"
    m "No fucking way..."
    y "The friggin’ apocalypse or whatever! One minute we were at your place and the next-"
    ay "You...You came too?! You were at the party?! Are we thinking of the right one?! What was I dressed as?!"
    y "I don’t know...A fuckin’...BDSM girl? With a...tail thing?"

    play sound "static.mp3"
    scene ayaneopendoor13 with flash
    stop sound

    ay "Holy shit, you {i}were{/i} there!"
    m "I have...{i}several{/i} questions about your choice of a costume, but I am going to ignore them in favor of asking if this is a usual occurrence for you. You {i}did{/i} mention Yumi being a part of this, correct?"
    ay "Yeah, but she’s never made it {i}through{/i} one before! If I had known that was possible, I would have looked for her too!"
    y "So this shit {i}ain’t{/i} normal then? Cause I didn’t think we’d go all the way back {i}here.{/i}"
    m "You weren’t by any chance impregnated by the teacher, were you?"

    scene ayaneopendoor14
    with dissolve

    ay "Maya, don’t start. Seriously."
    y "Impregnated?! Are you out of your fuckin’ mind?! "
    m "Just figured I’d ask. Might as well follow in my own footsteps if it gets me back to Sensei one day."

    scene ayaneopendoor15
    with dissolve

    m "Love {i}is{/i} a working theory of mine, though. So if Yumi’s feelings are strong enough for Sensei, perhaps it’s possible that she’d have hitched a ride with-"

    scene ayaneopendoor16
    with dissolve

    m "Oh...wait."
    m "I guess that theory falls apart if Sensei himself wasn’t sent here."
    m "Just what the hell decides this? I don’t get it."
    y "Love?...No way, I..."

    scene ayaneopendoor17
    with dissolve

    y "I mean, we did kiss once though?...So if you’re lookin’ for theories-"
    ay "Since {i}when?!{/i} When the fuck did that happen?! "
    ay "You’re supposed to be one of the safe, non-threatening ones! If {i}you’re{/i} already kissing Sensei, everyone is going to be kissing Sensei soon! I don’t want to see that!"
    m "Could be worse. I’ve had multiple threesomes with every single girl in the class."

    scene ayaneopendoor18
    with dissolve

    y "You’ve what?!"
    ay "I didn’t need to know that, Maya!"
    m "What? I told you I’d be honest now that you’ve earned my trust. The more you know about me, the better you’ll be able to take advantage of me when you go home. "
    m "It’s a calculated move, Ayane. Now’s not the time to question it."
    ay "But still! Yumi’s a virgin in our timeline! She doesn’t need to be hearing about weird threesomes in alternate realities!"
    m "How are you sure she’s a virgin? She could be fucking him behind your back."

    scene ayaneopendoor19
    with dissolve

    y "Man, seriously? I {i}just{/i} dealt with this shit the other day and now I gotta do it again with someone who barely even knows me? Shit’s weak, dude."
    ay "No, Maya. I know for a fact because I-"
    m "..."
    ay "Because..."

    scene ayaneopendoor20
    with dissolve

    ay "Wait...because I..."
    ay "Why...Why {i}do{/i} I know that again?..."
    ay "Something’s...something’s not coming to me, I...I think I’m-"
    y "Forget it, Blondie. We’ve got bigger fish to fry right now. I bumped into my cousin a couple hours ago and she said another one of those fuckin’ reset things’ is gonna happen {i}tonight.{/i}"

    scene ayaneopendoor21
    with dissolve

    ay "{i}Tonight?!{/i} Are you sure?! And who the hell is your cousin?! Why do {i}they{/i} know about this?!"
    y "Kaori Kadowaki. You’ve probably seen her at...every fuckin’ restaurant in Kumon-mi. And it beats the fuck outta me how she knows about this shit. But I clearly ain’t in the position to be callin’ people out on that."

    scene ayaneopendoor22
    with dissolve

    ay "{i}Kaori{/i} knows about the resets?..."
    m "It can’t be tonight...no. No, I haven’t felt anything at all. I’d know if it was coming."

    scene ayaneopendoor23
    with dissolve

    ay "Yeah, unless you’re wrong {i}again!{/i} This might be the only chance we have to get out of here, Maya! "
    ay "So I’m going to follow Kaori’s advice for now and question just how she’s involved {i}later!{/i} We’ve gotta get to the roof!"

    play sound "static.mp3"
    scene ayaneopendoor24 with flash
    stop sound

    m "Yeah, I..."
    m "I’ll..."
    ay "What’s wrong?! Is this really the time to hesitate?! It could happen at any moment if what Kaori said is true!"

    scene ayaneopendoor25
    with dissolve2

    m "{i}Hah...{/i}"
    ay "Maya...{i}come on.{/i}"
    m "I will. I just..."
    m "I need to do something first."
    ay "...What?"

    scene ayaneopendoor26
    with dissolve

    m "You two head to the school now. I’ll meet you there once I’m done. I promise."
    ay "I don’t like this, Maya. You’re keeping something from me again. You always do that and it {i}never{/i} helps at all. And I don’t want you missing {i}your{/i} chance to come home over something so-"
    m "I won’t be long. I promise."
    m "So please allow me to be dishonest one last time."
    ay "..."
    y "So, like...we’re supposed to go to the roof of the school? Cause I’ll book it there right now. I ain’t gotta wait around for whatever lesbian shit’s goin’ on here."
    ay "No, Yumi. I’ll come with you. But Maya-"
    m "If you’re about to hit me with some sappy goodbye, don’t. I’ll be there."

    scene black
    with dissolve2

    m "And we’ll surely meet again."

    "........."
    "......"
    "..."

    scene ayaneopendoor27
    with dissolve2

    y "..."
    ay "..."
    y "So, uhh..."
    y "Is it just me, or does “we’ll surely meet again” sound super fuckin’ final to you?"
    ay "It does...and I hate that she said that."
    ay "But Maya’s going to be Maya. And if she’s going to make me do something as stupid as choosing between her or everyone else I love, of course I’m not going to wait around."
    ay "This might be my only chance to get back to Sensei...and Ami...and Sana...and this might be {i}your{/i} only chance to get back to Chika. And...whoever else you care about."
    y "I don’t know...I kinda like the Chika in this world better. And that’s even factorin’ in how the one here is dressed like a literal bitch in heat."
    ay "You don’t mean that, Yumi. Friendship isn’t that flimsy."
    ay "I promise, though. The apocalypse is only scary at first. You’ll get used to it pretty quickly if you’re going to be joining us from now on."
    y "No, it ain’t that..."
    y "Like...yeah, that shit sounds lowkey terrifying. But Chika’s gotten fuckin’ {i}weird{/i} lately. Like somethin’ fuckin’ snapped and turned her into a different girl outta nowhere."
    ay "Maybe that’s just growing up? Sana’s been weird lately too. So has Makoto. And Ami’s been changing personas so frequently lately that I never know which one I’m going to get when I visit her."

    scene ayaneopendoor28
    with dissolve

    ay "Maybe this is just how things are meant to be, though?"
    ay "Maybe some of us are {i}supposed{/i} to feel left behind while everyone else keeps moving forward? I wouldn’t put it past this world to fuck some of us over that way when we’re already being put through {i}this.{/i}"
    y "So, we’re...tryin’ to go back then?"
    ay "Is that not what you want?"
    y "I..."

    scene ayaneopendoor29
    with dissolve

    y "I don’t know..."
    y "I feel like that’s what I {i}should{/i} do, but...I’ve got just as much in this world as I did in the other one. And with some extra time, maybe I’d..."
    y "Maybe I could do shit a little better? Be nicer to some people...go to that convenience store a little earlier...actually call my mom..."
    y "That shit seems harder where we come from. Doin’ {i}everything{/i} seems harder where we come from. And somethin’ about this place just feels less...I don’t know...real?"
    y "Maybe I just ain’t settled in yet?..."
    y "Maybe shit’ll get just as hard as it is back home."

    scene ayaneopendoor30
    with dissolve

    y "Did you feel this way after your first reset too? Or am I just bein’ a sappy piece of shit?"
    ay "You never have to worry about being sappy around me, Yumi. I get it. "
    ay "This is {i}nothing{/i} like my first time, though. And I want to get out of here as soon as possible."
    y "Yeah, but you’re only sayin’ that cause you’ve got a “future husband” in that other world. I ain’t got that to look forward to back there."
    ay "Do you {i}want{/i} to look forward to that, though?"

    scene ayaneopendoor31
    with dissolve

    y "..."
    ay "Because if you do...or if you even think you {i}might...{/i}home is where you’re going to find it."
    ay "There’s nothing for us here. "

    scene black
    with dissolve2

    ay "We’re just wearing someone else’s clothes."

    $ renpy.end_replay()
    $ halloweenayane3 = True

    "........."
    "......"
    "..."

    jump halloweenfive15

label ayanespring2:
    scene nightsky
    with dissolve2
    play music "calmbar.mp3"

    "It was a normal night at a local bar. "
    "Unfortunately, the word “normal” had taken on a new meaning for its proprietor recently."
    "Or perhaps it would be more accurate to say it had taken on an {i}older{/i} one."
    "One where the baseline was lowered from somewhere near happy to somewhere closer to the dirt."
    "This had good and bad sides, you see."
    "The good was that the slightest thing now could turn an average day into a great one."
    "The bad was that, despite how much easier it would be to improve at this point, things seldom seemed to click."
    "And that statement applied to more than just one person as you’ll see shortly."

    scene sarasadayanebar1
    with dissolve2

    sar "..."
    cussy1 "..."
    cussy2 "..."
    cussy1 "Should we, like...say something?"
    cussy2 "I’ve needed to order another drink for like ten minutes now, but I just feel bad."
    sar "..."
    cussy1 "You don’t think the bar might be going out of business, do you?"
    cussy2 "Come to think of it, I haven’t seen that scary Yakuza lady around here lately. Maybe she was laid off?"
    cussy1 "Shh! She can still hear us. I feel like that might be a sore topic right now."
    cussy2 "{i}Can{/i} she hear us? Because she hasn’t reacted at all since we-"
    sar "Of course I can hear you. I’m not deaf."
    cussy2 "Th...then...would I be able to get another-"
    sar "Just take whatever you want. It’s on the house tonight."
    cussy1 "..."
    cussy2 "..."
    cussy2 "I somehow feel even weirder now."

    scene sarasadayanebar2
    with dissolve

    cussy1 "Let’s just, uhh...give her the night off. We can go somewhere else. "
    cussy2 "R...Right! Plus, if the bar {i}is{/i} going out of business, I’d feel kind of bad about just...helping myself to what could be the very last of their stock."

    play sound "dooropen.mp3"
    scene sarasadayanebar3
    with dissolve

    sar "Thanks for coming to Sakaki-bar-a. The last family-run bar in Kumon-mi. Probably."

    scene sarasadayanebar2
    with dissolve

    sar "If you can even call us {i}family{/i} at this point."

    "A normal night it was — just one that leaned closer to the negatives than the aforementioned hope for a possible uptick in whatever chemical could contort one’s face into a smile."
    "For Sara, wine typically helped with that. "

    play sound "dooropen.mp3"

    "Not so much anymore, though. "
    "Not since seeing her daughter get dicked down by a cock the size of her torso. "
    "Let alone a torso-sized cock that had been inside of {i}her{/i} as well."
    "It was a great cock. "
    "Strong. "
    "Solid girth. "
    "The best cock that she and her daughter ever had. "

    scene sarasadayanebar3
    with dissolve

    sar "Welcome to Sakaki-bar-a. Just take whatever you want."

    "This was no time to be thinking about cocks, though."

    ay "Um...Sara?"

    scene sarasadayanebar4
    with fade

    "It was time to confront the reality of this seemingly hopeless situation — and hearken back to what I mentioned just minutes ago about “normal” being worse for more than just her now."

    sar "Ayane?..."
    ay "Yeah...hey."
    sar "Sana’s not here right now if you’re looking for-"
    ay "I’m not...looking for Sana."
    ay "I was hoping that we could maybe...talk. If that’s okay."
    sar "Talk..."
    ay "Yeah. But only if you’re okay with it. You look...tired."
    sar "Did Sana send you here to {i}talk{/i} to me?"
    ay "No, but...I’d be lying if I said it wasn’t {i}because{/i} of her that I’m here."
    sar "..."
    ay "She still hasn’t...confronted you about...anything, uhh...{i}disturbing{/i} lately...has she?"

    scene sarasadayanebar5
    with fade

    sar "Oh, good. So {i}you{/i} know too then. Wonderful."
    ay "Sara-"

    scene sarasadayanebar6
    with dissolve

    sar "Just go home, Ayane. This isn’t something I want to get you involved with."
    ay "Well, me knowing what’s happening means I’m {i}already{/i} involved, doesn’t it? Besides, keeping everything locked away isn’t going to make you feel better."
    sar "And talking about it {i}is?{/i}"
    sar "Which part, exactly? The one where my daughter is seeing the same guy as me? Or the part where she wants me to join in so we can {i}see{/i} him together?"
    ay "That’s-"

    scene sarasadayanebar7
    with dissolve

    sar "Or, better yet, maybe we should talk about how it’s all my fault she ended up like this in the first-"

    play sound "static.mp3"
    scene sarasadayanebar8 with flash
    stop sound

    ay "Stop."
    sar "Why?...It’s the truth and you know it."
    sar "{i}I’m{/i} the one who raised her. And {i}I{/i} set an example by {i}also{/i} screwing my teacher when I was her age. "
    sar "She’s just doing what I did...She’s following in my footsteps."
    sar "And none of it would have happened if I had just...been a better mother. "
    sar "I never should have told her the truth about her father. I should have just lied like they do in the movies."
    ay "If that were true, I wouldn’t be doing the same exact thing {i}she{/i} is."

    play sound "static.mp3"
    scene sarasadayanebar9 with flash
    stop sound

    sar "...What?"
    ay "You know my mom left years ago, so you know I-"
    sar "You’re sleeping with Sensei too?..."

    play sound "static.mp3"
    scene sarasadayanebar10 with flash
    stop sound

    ay "That’s right...Since long before Sana was."
    ay "And if you want to blame that on my mom not being around, fine. But you know I’m my own person. You know I can make my own choices."
    sar "Psht. The only thing I know is that we’re {i}all{/i} the same at your age apparently."
    ay "Maybe so. But I can also tell you that, if my mom were still here, I wouldn’t do what Sana did. That was wrong on every level possible, Sara. "
    ay "And I’m here to tell you it’s not your fault since {i}she{/i} won’t. "
    sar "..."
    ay "So please...can we talk? Like, {i}really{/i} talk? I’ll tell you everything."
    ay "You deserve to know, Sara. You’ve been through enough."
    sar "..."
    ay "..."
    sar "{i}Hah...{/i}do you want a drink?"
    ay "No thanks. I’m not old enough."

    scene black
    with dissolve2

    sar "Heh...the irony..."

    "........."
    "......"
    "..."

    scene sarasadayanebar11
    with dissolve2

    ay "I {i}do{/i} have one request if...that’s okay."
    sar "Please tell me you’re not in a sex competition and need the assistance of your best friend’s mother."
    ay "I’m not currently in any sort of sex competition, no."
    sar "That’s good at least. Did you win the last one?"
    ay "Unimportant. I just..."
    ay "Sara, I’m doing all of this behind Sensei’s back. He doesn’t know you were involved in that...horrible situation in any way. And I’d like you not to tell him I told you any of this."
    sar "I wouldn’t really know where to begin if I did. Nor do I understand why you feel like it’s your responsibility to try and make me feel better."
    ay "You’re the closest thing to a mom I have, you know. Which is why I know how heartbroken you must be right now after seeing all of that."

    scene sarasadayanebar12
    with dissolve

    sar "I don’t even know if “heartbroken” is the word...I don’t think it is."
    ay "Well, what is it then? Betrayed? Disappointed? Shocked?"
    sar "Shocked, yes. That was, uhh...quite the surprise. But I should have suspected {i}something{/i} based on how...nice she was being to me that weekend."

    scene sarasadayanebar13
    with dissolve

    sar "I’m sure you know Sana and I don’t have the...best relationship. So when she’s nice to me, I..."
    sar "I’ll do anything..."
    ay "Sana’s only like that because she doesn’t realize how lucky she is to have someone who loves her as much as you do. "
    sar "I’d die for that girl, Ayane..."
    sar "And if Haruka wasn’t there to take me home, I-"

    scene sarasadayanebar14
    with dissolve

    ay "Sara, don’t."
    sar "Shame...that’s what it is. {i}That’s{/i} what I feel."
    sar "She thinks so little of me, Ayane. And just listen to me. {i}Look{/i} at me. She’s right. She’s right about all of it. So who am {i}I{/i} to want to step in when all I’d do is-"

    scene sarasadayanebar15
    with dissolve

    ay "Look — your daughter is a pervert, okay?! It’s disappointing, yes! But it’s who she is and there’s nothing we can do about it!"
    sar "What about you, then? And that Molly girl she was competing against? Is there nothing that can be done for either of you two either?"

    scene sarasadayanebar16
    with dissolve

    ay "Sara, I can’t speak for anyone else...but I love Sensei. "
    ay "And yes, I {i}make{/i} love to him. But I do it because I want to deepen our bond."
    sar "And the fact that he’s doing it with other people you know...your friends...that doesn’t bother you?"
    ay "Of {i}course{/i} it bothers me. It hurts just as bad as it did when my mom left. Just now I get to experience it every single day. "
    sar "Then why don’t you look like {i}me?{/i} How can {i}you{/i} find the strength to come all the way over here when I can’t even confront my own daughter?"

    scene sarasadayanebar17
    with dissolve

    ay "Well..."
    ay "Because I’m used to it."
    sar "Ayane..."

    scene sarasadayanebar18
    with fade

    ay "It doesn’t stop with just {i}us,{/i} you know. Me. Sana. Molly. "
    ay "The sad truth is you could probably walk into our classroom, point out any girl at random, and chances are {i}she’d{/i} be involved with Sensei too."
    ay "It’s just a...fact of life for us now. And pretty much everyone knows it, which is why Sana is...well...suddenly getting a lot {i}bolder.{/i}"
    sar "So Sensei is...sleeping with an entire class of high-schoolers..."
    ay "Pretty much. "
    sar "You were right, Ayane. Talking about this makes me feel so much better."

    scene sarasadayanebar19
    with dissolve

    ay "I’m not trying to hurt you, Sara. I just think that you deserve to know what’s going on so you can either avoid getting pulled into this again, or...I don’t know..."
    ay "Maybe just...avoid Sensei altogether if...that's what you think is best for {i}you.{/i}"

    scene sarasadayanebar20
    with fade

    sar "Mm..."
    sar "And be all alone again, you mean."
    ay "You’re not alone, Sara...you’ll always have me. Sana too, just...she, umm...I think she needs to try and...understand you a little better."
    sar "I think you do too, Ayane. That’s not what I meant by “alone.”"
    sar "Sensei’s the first guy I’ve seen since Sana’s father. And for a while, I...thought he might be different. That I might actually be enough for him and...that he’ll want to stay."
    sar "Looks like he might see me the same way Sana does though. "
    sar "Easy...desperate...and any other word you can throw at a woman who so easily welcomes a man she knows barely anything about into her home."
    sar "Even now, I barely know anything about him...and he’s out there fucking my daughter like {i}he’s{/i} a teenager himself."
    sar "It’s tough, you know? I don’t know whether I should strip down and show him how it’s done or grill him about his future and whether or not he’s right for my little girl."

    scene sarasadayanebar21
    with fade

    ay "It’s definitely a...weird predicament, yeah.."
    ay "And you know...I think Sensei might actually just {i}want{/i} to be a teenager sometimes. I don’t think he ever really {i}got{/i} to be one in the first place."
    sar "I do too. Having a threesome with my daughter would be much less awkward if I was in the same grade as her."
    ay "You’re not...seriously considering actually doing that with her, though...right?"
    sar "What would you think of me if I {i}did,{/i} Ayane?"

    scene sarasadayanebar22
    with dissolve

    sar "Am I somehow {i}above{/i} doing something like that in your head? Because if so, thank you. You already think more of me than Sana does."
    sar "Let’s face it, though — I’m not cut out to be a mother. I lost one child already. Now, the second one is begging to be taken away and framing {i}this{/i} as the one way to keep her close."
    sar "At least if Sana and I are {i}both{/i} there with him, all three of us could “deepen our bond.” The same way you do when the two of you are alone."
    ay "You don’t...mean that."
    sar "You don’t {i}know{/i} that."
    sar "We Sakakibaras are cursed, you know. In more ways than one. "
    sar "We’re not {i}allowed{/i} to be happy. Or live normal lives. But I tricked myself into thinking I could change that by building a home for my kids. "
    sar "I never knew what I was doing, though. I {i}still{/i} don’t. I’m just fucking...not good at this. Any of it. "
    ay "But at least you stayed..."

    scene sarasadayanebar23
    with dissolve2

    ay "At least you stayed, Sara..."
    ay "Even when you had to raise your kids on your own, you {i}stayed.{/i} And what I’ve learned through my experiences and tons of my friends, that seems to be the hardest part."
    sar "When I love something...I can’t bring myself to let go of it. It needs to be torn from me."
    ay "I’m the same way. {i}That’s{/i} why I stay with Sensei. {i}That’s{/i} why I still cling to the idea that one day, I {i}will{/i} be enough."
    ay "Just, in my head, that’s less of an idea and more of an eventuality. I {i}will{/i} be with him in the end. And if he ever leaves, I know at least one girl very experienced in finding him."
    sar "You really are special, Ayane..."
    sar "You’re more confident in high school than I’ve {i}ever{/i} been at any point in my life."
    ay "Just wait until I tell you how many kids {i}I’m{/i} going to have."

    scene sarasadayanebar24
    with dissolve

    sar "How many?"
    ay "However many are on a football team?"
    sar "Isn’t that like...forty? How are you going to afford that?"
    ay "I’m rich, remember?"
    sar "Then how is your {i}body{/i} going to afford that? You’d need to start having a kid a year like...now."
    ay "Or just twenty sets of twins."
    sar "Do twins run in your family? I’ve heard that’s a genetic thing."
    ay "Not yet they don’t. A couple years from now, though? Who knows?"

    scene sarasadayanebar25
    with dissolve

    sar "Heh..."
    ay "{i}Now{/i} do you feel better?"
    sar "Nope."
    ay "Fuck."

    scene sarasadayanebar26
    with dissolve

    sar "I’m glad you came and talked to me, though. I’ve been in a pretty dark place ever since I watched my boyfriend impale my daughter."
    ay "Ahh, see that’s where you’re wrong. Sensei is {i}my{/i} boyfriend. I’m just sharing him with all of you because I’m kind and like to give back to the community."
    sar "There’s that confidence again. Can I borrow some of it so I can have the courage to ask my daughter why she now thinks incest is okay?"
    ay "I can assure you that incest is perhaps the single most {i}tame{/i} thing on Sana’s kink list."
    sar "I’m both curious and terrified of what that could mean. I’m sure yours is no better though if you’ve been seeing Sensei for as long as you imply."

    scene sarasadayanebar27
    with dissolve

    ay "Yeah...does that not weird you out?"
    sar "I’m more weirded out by my daughter wanting to have a threesome with me than my daughter’s friend wanting consensual sex with the guy she likes."
    ay "No, not me. Sensei. I figured you’d be...less okay with, you know, him sleeping with more or less an entire school."
    sar "I mean...I wouldn’t say I’m {i}okay{/i} with it. It’s certainly...unethical. But sleeping with my teacher was the single best choice I ever made because it gave me my children."
    sar "It’d be wrong for me to take that from anyone else."
    ay "With all due respect, that is a very irresponsible thing for an adult to say."
    sar "With all due respect, you’re okay with it too and you’re way smarter than I am even {i}with{/i} the age gap."
    ay "Fair enough. But I still-"
    sar "We’re done talking about me, Ayane. You’ve said your piece and adequately filled in for my real daughter. Now it’s my turn to listen to you."
    ay "What?"
    sar "I’m the closest thing to a mom that you have now, yeah? You must have a lot you want to get off your chest. And even if I look like this, I can still hear you out. "
    ay "I mostly just wanted to come over here and tell you not to blame yourself but, if it’s okay, could I maybe yell a few things really loudly while you keep stroking my cheek?"
    sar "Sure. That works for me."
    ay "Great. Here I go."

    scene sarasadayanebar28
    with hpunch

    ay "I CAN NOT BEGIN TO FATHOM NOR EXPLAIN THE HATE THAT I HAVE FOR THE FACT THAT MY STUPID PREDATOR BOYFRIEND-DAD KEEPS FUCKING ALL MY FRIENDS {b}AND{/b} THEIR MOMS!"
    ay "I ALSO TAKE GREAT EXCEPTION TO THE FACT THAT THE ONES HE SEEMS TO PRIORITIZE ARE LESS LOVING AND LESS MATERNAL AND HAVE SMALLER BOOBS THAN ME!"
    ay "AS THE MORE PHYSICALLY AND EMOTIONALLY DEVELOPED LOVE INTEREST, IT SEEMS ONLY FAIR THAT I, AYANE AMAMIYA, WOULD BE THE FAVORITE! BUT NOPE! FUCK ME, I GUESS!"
    ay "AND ALSO! ALL OF THIS MOM STUFF IS MAKING ME REALLY PISSED OFF AT MINE FOR LEAVING AND I COULD REALLY USE HER RIGHT NOW! NO OFFENSE TO SARA, THOUGH! "
    ay "OH! AND AMI?! REALLY FUCKING WEIRD ALL OF A SUDDEN! MAYA? HUGE BITCH! WHICH IS BASICALLY THE SAME AS SHE’S ALWAYS BEEN, BUT STILL! MASSIVE BITCH!"
    ay "MAKOTO SHOULD TRY HARDER! YUMI SHOULD CARE MORE! APOCALYPSES ARE CONFUSING AND SCI-FI STUFF ISN’T EVEN REALLY THAT INTERESTING! LIFE SUCKS! I’M HORNY!"
    ay "OH AND ONE LAST THING! THE CONVENIENCE STORE CLOSEST TO THE DORMS STOPPED STOCKING THE CANNED COFFEE I LIKE AND NOW I HAVE TO BLOW IT UP! FUCK ME AGAIN!"

    scene sarasadayanebar29
    with dissolve

    ay "Okay. I’m good now. Thank you, Sara."
    sar "Don’t mention it. And if you ever need to talk-"

    scene sarasadayanebar30
    with dissolve

    ay "I know where to find you."
    ay "What are you going to do about Sana though? She’s supposed to work on Saturday, isn’t she?"
    sar "Don’t worry about me. You’ve done enough of that already."
    ay "All I do is worry now. It’s really no big deal."
    sar "Well, go worry at home. I’m gonna clean up in here and go to sleep."
    ay "Want some help? I can check if Efrosinia is free right now. I heard she’s in town and I’m sure she wouldn’t mind."
    sar "I’d actually like some alone time if that’s okay."
    ay "Got it."
    ay "In the meantime, I’ll try and find a muzzle that fits your daughter so you don’t ever have to hear her say such gross things to you again. "

    scene sarasadayanebar31
    with dissolve

    ay "Or...at least that’s what I {i}would{/i} do if I...wasn’t absolutely certain that she’d like it."
    sar "Ayane? Alone time?"

    scene black
    with dissolve2

    ay "Right. Sorry."
    ay "And remember! Secret conversation! Because I have cried enough lately and can assure you that Sensei getting mad at me would only make me cry more!"
    sar "Of course, Ayane..."
    sar "I won’t tell anyone you were even here..."

    $ renpy.end_replay()
    $ ayanespring2 = True

    jump saraspring3

label ayanespring3:
    scene black
    with dissolve2

    "{i}After the last bell has rung and the doors have been opened...{/i}"
    "........."
    "......"
    "..."

    scene ayanemakotoofficemeet1
    with dissolve2
    play music "phantomthief.mp3"

    ay "Meeting — start! Attendance will now be taken. Makoto!"
    mak "Present."

    scene ayanemakotoofficemeet2
    with dissolve

    ay "Wonderful. That concludes the taking of attendance. We may now proceed with the matters at hand."
    mak "Which are...what, exactly?"
    ay "Oh, you know. Assorted apocalypse stuff. What we’re going to wear for the next reset. How I’m your new best friend. Things like that."

    scene ayanemakotoofficemeet3
    with fade

    mak "Okay, but you’re going to have to be the one to break the news to Miku. "
    mak "Losing me leaves her with either Kirin, Io, or my mom as her new best friend. And I’m sure you can see the negative impact any of them would have on her."
    ay "Isn’t Miku becoming a little sex gremlin thing now? Wouldn’t that mean that {i}you{/i} have also had a negative impact on her?"
    mak "Yes. It is {i}my{/i} fault. {i}Not{/i} the fault of the adult man who claimed her virginity with the same amount of thought he’d put into redeeming a 500 yen scratch off ticket."

    scene ayanemakotoofficemeet4
    with dissolve

    ay "Is all that stuff I've been hearing about him breaking her vagina really true?"
    mak "No comment."
    ay "Not even a little comment? A tiny one? You really won’t spare any details for your new best friend?"
    mak "Sorry — where is this sudden interest in Miku’s vagina coming from? Is there something you’re not telling me, Ayane?"
    ay "No, but there’s something {i}you’re{/i} not telling me."

    scene ayanemakotoofficemeet5
    with dissolve

    ay "I am willing to look past that if it brings us closer together, though."
    mak "It won’t, but okay."
    ay "Vaginas aside! It’s time to continue planning our escape from this mortal coil. And seeing as I have so far been the idea girl, I am now passing the torch to you."
    mak "Wait, {i}me?{/i}"
    ay "Yes. You. Who else am I going to pass it to?"

    scene ayanemakotoofficemeet6
    with fade

    mak "Well, for one, Yumi still exists. Which you may or may not have forgotten based on the fact that you didn’t invite her to our meeting."
    ay "Yumi doesn’t want to be involved in any of the apocalypse stuff, though."
    mak "And {i}I{/i} do? Correct me if I’m wrong, but I’m pretty sure I have verbally stated on several occasions now that things are better for me here. Why would I want to get out of this timeloop?"
    ay "It’s less that you’d want to get out and more the fact that you’re the type of person who habitually solves problems. And what bigger problem is there than this?"
    mak "Oh, okay. So you’re just taking advantage of my intellect then."

    scene ayanemakotoofficemeet7
    with dissolve

    ay "Right."
    mak "And you have no shame regarding this at all."
    ay "Nope. Not even a little. So, what’s your plan?"
    mak "I don’t have one."
    ay "Buuuut, if you were to come up with one, what would it be?"
    ay "I’m not asking you to figure out time travel in one sitting. I just want something to run with and build off of. "
    ay "And I’ve had my hands too full with my own misery lately to be able to come up with anything worth trying."
    mak "Well, we could maybe start by finding you a therapist."

    play sound "static.mp3"
    scene ayanemakotoofficemeet8 with flash
    stop sound

    ay "Denied. I am formally requesting a {i}new{/i} idea."
    mak "And I am formally requesting that you take my legs off of your lap. How did you get there so quickly?"
    ay "Doesn’t matter. What {i}does{/i} matter is that we create a comfortable environment for one another. And sometimes, mild physical touch can help with that!"
    mak "Or, and hear me out here, make everything way {i}less{/i} comfortable."
    ay "Jeez, Makoto. You’d think for someone who’s had a foot-long cock inside of her over a thousand times that you’d be more open to putting your legs on someone’s lap."

    scene ayanemakotoofficemeet9
    with dissolve

    mak "Sorry, do you have a foot-long cock you’ve just never told me about?"
    ay "Maybe. Would you think any less of me if I did? And be careful with your answer, Makoto. It’s Pride month. "

    scene ayanemakotoofficemeet10
    with dissolve

    mak "Okay, you want an idea? Here. I think we should start taking Yumi’s position in our {i}team{/i} a little more seriously, whether she {i}wants{/i} to be included or not."
    ay "You think she’ll actually go along with it?"

    scene ayanemakotoofficemeet11
    with fade

    mak "I think she doesn’t have much of a choice. What’s the worst thing that could happen? She says no and we just stay the same way we’ve been since {i}I{/i} got thrown into this?"
    ay "The worst thing that can happen is that she beats you up. And I wouldn’t be able to live with myself if I put you in danger, Makoto."
    mak "Thank you, but I think I’ll be fine."

    play sound "static.mp3"
    scene ayanemakotoofficemeet12 with flash
    stop sound

    ay "Don’t you think Yumi’s seemed a little {i}off{/i} lately though?"
    mak "Because she’s...actually coming to school? And participating in stuff like the Dorm Wars?"
    ay "Yeah, exactly. Doesn’t that make you think something might be going on with her?"
    mak "Could that “something” not just be resignation? Like, maybe she’s accepted this situation {i}already{/i} and figures there’s no point in just waiting for it to blow over anymore?"
    ay "I’d agree under normal circumstances. But something about the way she’s been carrying herself lately makes me feel like she’s more {i}sad{/i} than anything."

    scene ayanemakotoofficemeet13
    with fade

    mak "Can Yumi even feel such an emotion?"
    ay "Of course. Everybody gets sad, Makoto. I’m sure you’ve had a good cry in the bathroom at least once over your time here."
    mak "Yeah. My dad just needed to die for it."
    ay "Then I am sorry for making you think about that again. But the fact remains, Yumi seems like she’s not in the sort of mindset we need to make any sort of progress right now."
    mak "And what sort of mindset is that, Ayane? Because I was under the impression we just {i}never{/i} made any progress here."
    ay "Sure we do. You and Yumi even being able to talk about this is progress. And I’m sure Maya and Sensei would have said the same thing about me when I joined."
    mak "Yeah, where is {i}he?{/i} Shouldn’t he be here too?"
    ay "Probably. In regard to the mindset thing, though, I feel like you and I are the only ones {i}normal{/i} enough to figure anything out at the moment."
    mak "I think you’re gravely overestimating just how much two teenagers can accomplish in the field of metaphysics."
    ay "Sure. But people would say the same about our ability to receive Sensei’s penis and here we are. Just two penis experts hanging out on a couch."
    mak "Ayane — my {i}idea{/i} is simple. We let time run its course and just carry on the same ways we would if we were {i}not{/i} involved in a timeloop. "
    mak "Trying to interfere with any of it will likely just confuse us more or, even worse, fuck something up. Is that really something we want to risk?"

    scene ayanemakotoofficemeet14
    with dissolve

    ay "{i}Hah...{/i}no. It’s just that “letting time run its course” is exactly what Maya did. And if she were here today, she’d be jumping at every single opportunity to actually {i}do{/i} something."
    mak "Just...she {i}is{/i} here today. And you’re more than welcome to try talking to her about any of this if you want. I’m sure the {i}old{/i} her would have approved of that too."
    ay "I {i}have{/i} been trying. It’s just..."
    mak "..."

    scene ayanemakotoofficemeet15
    with dissolve

    ay "It...hurts."
    ay "Sensei’s not the only one {i}affected{/i} by her disappearance. And being able to experience this with her, like...formed a bond that felt...really special to me. "
    mak "Well...I’m sorry I’m not her. And I’m sorry I’m not approaching things the way {i}she{/i} would. "
    mak "But she {i}is{/i} still here. So there has to be something the two of you can-"
    ay "She’s weird too, though. And lately, I..."
    mak "..."

    scene ayanemakotoofficemeet16
    with dissolve

    ay "..."
    mak "You {i}what?{/i} What is that expression?"
    ay "Um..."

    scene ayanemakotoofficemeet17
    with fade

    ay "Just...out of curiosity...have you noticed anything {i}odd{/i} about the way she’s been with Ami lately?"
    mak "I feel like we’re at a point in this timeline where every single interaction with Ami is going to be “weird” in some way or another."
    ay "Well, yes. But I can’t help but feel like the two of them are hiding something from me. From everyone. And neither one of them will clue me in on it."
    mak "Hmm...maybe they’ve started a second “Love Squad” specific to only those with A-cups?"
    ay "Or maybe they just don’t trust me the way they used to..."

    scene ayanemakotoofficemeet18
    with fade

    mak "Well, you {i}did{/i} lose the Maya you apparently had a “special bond” with. So I imagine this one wouldn’t just inherently trust you right off the bat."
    ay "Right, I get that. And I wouldn’t expect that either. But it’s like..."
    ay "I can hang out with Ami and everything will be normal. I can talk to Maya and everything will be “normal.”"
    ay "But when the two of them are together, it always feels like I’m being left out of something. "
    ay "And I don’t know...maybe it’s just karma for Maya and I making {i}Ami{/i} feel that way before everything happened. But maybe it’s {i}more?{/i}"
    mak "What would “more” even be, though? It’s not like they’re secretly having sex behind closed doors or anything."

    scene ayanemakotoofficemeet19
    with fade

    ay "That’s the part I can’t figure out. And any time I try to probe Ami for answers, she just gaslights me into thinking everything’s completely normal."
    mak "Well, that’s no surprise at all given her relationship with Sensei and how she likely does the same with him. "
    mak "If I were you, I wouldn’t be probing {i}her{/i} at all. I’d be trying to figure things out from Maya instead. At least she can likely be annoyed into submission."
    ay "My relationship with Ami is different, though. She and I have always been really close. She’s basically my little sister. "
    mak "Or...maybe she just {i}wants{/i} you to think you’re really close and the reality is that she’d stab you in the back at any moment if it meant getting closer to what she really wants?"
    ay "She can’t, though. "
    mak "What do you mean she “can’t?”"
    ay "I mean she literally can’t. My guardian angel told me as much."
    mak "..."

    scene ayanemakotoofficemeet20
    with dissolve

    ay "..."
    mak "Your what?"
    ay "You wouldn’t get it. In fact, {i}I{/i} don’t really get it. But questioning seemingly paranormal entities here has never led me to any good, so I just listen to them now. "
    mak "Ayane, if Big Boi has been secretly visiting you at night, you should probably let me know."
    ay "It’s not Big Boi, I swear."

    scene ayanemakotoofficemeet21
    with dissolve

    ay "I wonder how he’s doing, though."

    play sound "dooropen.mp3"

    mak "Yeah. He kind of just showed up that one time and then disappeared forever."

    scene ayanemakotoofficemeet22
    with fade

    ima "..."
    ay "Oh. Hi, Imani. "
    ima "Guys, I know it’s Pride month, but if the two of you are going to do lesbian stuff together, you should at least do it in the dorms."
    ay "We’re not doing lesbian stuff, though. We’re having a meeting."
    ima "A meeting that requires Makoto’s legs in your lap?"
    mak "For what it’s worth, I also told her this was not conducive to a proper setting for a meeting."
    ima "The hell are you two having a “meeting” for anyway? School ended an hour ago. Shouldn’t you be out having fun and being social and shit?"
    ay "Me, probably. Makoto, not so much."
    ima "Yeah, I wasn’t really talking about her."
    mak "I let you use my office and this is how you repay me?"

    scene ayanemakotoofficemeet23
    with dissolve

    ima "It ain’t {i}your{/i} office, ho! This place belongs to Sensei! And now that he ain’t here, it {i}probably{/i} belongs to me!"
    mak "I’ve been here longer! I have seniority!"
    ima "I’m your senior! Which should literally imply that {i}I{/i} have seniority! "
    ay "And I’m Sensei’s wife, which means that half of this office belongs to me."

    scene ayanemakotoofficemeet24
    with dissolve

    mak "Lies! I’m definitely the closest to being his actual wife! But I will not reveal how or why!"
    ima "Fine, Mrs. Ayane Arakawa. Compromise reached. But {i}I{/i} get the half with the desk because I have papers to grade and doing it on the floor of my apartment hurts my back."

    scene black
    with dissolve2
    stop music fadeout 12.0

    ay "Ooh! Can I get extra credit if I help?"
    ima "Sure. You don’t really need it, though. "
    mak "Can I help too or will grades not go higher than 100%%?"
    ima "You can give your extra credit to Miku. Lord knows she needs it."
    mak "Ugh. Fine."
    ay "See? This is what I was talking about. You always have to help. It’s in your DNA."
    ima "Cool! You two handle these then and I’ll go home early. But remember — no lesbian stuff!"
    mak "Miss Imai-"
    ima "{i}Hah.{/i} Okay, fine. You can do a {i}little{/i} lesbian stuff. But only because it’s Pride month. Above the clothes only. Got it?"
    mak "Wha-"
    ay "Got it! Thanks, Imani! Love you!"

    play sound "dooropen.mp3"

    ima "Love you too! See you both on Monday! "
    mak "We’re not lesbians! "
    ima "{i}Can’t hear you! Too busy being an ally!{/i}"

    $ renpy.end_replay()
    $ ayanespring3 = True

    "{i}Ayane and Makoto’s affection for one another has increased by 1!{/i}"
    "{i}They swear it’s not because of gay stuff, though.{/i}"
    "........."
    "......"
    "..."

    jump noonch4
