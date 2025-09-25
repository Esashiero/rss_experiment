label mall:
    if chika_love >= 0 and firsttimemall == False:
        jump firsttimemall
    if chika_love >= 5 and mall5 == False:
        jump mall5
    if chika_love >= 10 and mall10 == False:
        jump mall10
    if chika_love >= 15 and chikadorm15 == True and day79 == True and mall15 == False:
        jump mall15
    if chika_love >= 20 and chikadorm20 == True and mall20 == False:
        jump mall20
    if chika_love >= 40 and chikaspecial40 == True and mall40 == False:
        jump mall40
    if chinami_love >= 30 and yumiyukispecial1 == True and chinamidate30 == False:
        jump chinamidate30
    if chika_love >= 45 and nikilovesyou3 == True and shrine40 == True and mall45 == False:
        jump mall45
    if chapthreeactive == True:
        jump chikasummer2mallgen
    if christmas7 == True:
        jump mallgen2
    else:
        jump mall2to4

label chikamaid:
    if chika_love >= 40 and chikaspring5 == True and chikaspring6 == False:
        jump chikaspring6
    if chap4active == True:
        jump chikaspringmaidgen
    else:
        "ERROR"
        jump morningch4

label chikainvite:
    if chikablock == True:
        play sound "phonebeep.wav"
        "........."
        "......"
        "..."
        "Huh. I guess Chika's busy right now."
        jump callnight
    if chikainvite1 == False:
        jump chikainvite1
    if chikainvite1 == True and chikainvite2 == False:
        jump chikainvite2
    else:
        jump chikainvitegen

label mallgen2:
    scene chikanoongen2
    with dissolve
    play music "mall.mp3"

    "I show up at the mall to find Chika sitting in her usual spot."
    "She's too absorbed in some song on her phone to notice me at first and I wind up placing my hand on her shoulder to get her attention."
    "Instead of jumping at the sudden sensation, though, she makes the bold decision to lay her head atop my fingers and thank me for the company."
    "I go out on a limb and assume that she knew it was me beforehand because the idea of doing this to a random stranger seems quite worrisome."
    "The two of us go on to spend the rest of her break together, with her being a bit overly flirtatious and unfazed by anyone who comes across us."
    "Eventually, she needs to get back to work and I decide to stop bothering her."
    "It's unfortunate that the two of us can't spend more time together on the weekends, but I guess it makes sense if she wants to continue, you know, having a home."

    scene black
    with dissolve

    "I put my hands in my pockets as I move through the automatic doors and brace myself for the cold walk that is about to follow."
    "Maybe I should ask Chika to shoplift me some gloves or something?"

    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika's affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chikainvitegen:
    play sound "phonebeep.wav"

    "I tap on Chika's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    c "Hihi~"
    c "What's going on, [chikamaster]?"
    c "Trying to get me to come over?"
    s "Wow. It's almost like you read my mind."
    c "Nahh. I was actually just about to text you to see if you wanted to hang out anyway sooo...yeah."
    c "I'll get dressed and head on over."
    s "Better yet, don't get dressed at all. Just head over now."
    c "Nice try, loser~"
    c "I'll see you soon."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    if halloweenfive17 == True:
        scene chikainvitehub2
        with fade
    else:
        scene chikainvitehub
        with fade

    play music "acoustic.mp3" fadein 3.0

    c "Heya!"
    c "So, what's going on tonight?"
    c "We're all alone, so we can do whatever we want~"

    "How should I spend my time with Chika?"
    menu chikainvmenu:
        "Hang Out (Raise Affection)":
            jump chikainviteaff
        "Almost-Fellatio (Raise Lust)" if bonus == True:
            jump chikainvitelicking
        "Handjob (Raise Lust)" if bonus == True:
            jump chikainvitehandjob
        "Missionary Sex (Raise Lust)" if chika_virgin == False and bonus == True:
            jump chikainvitemissionary
        "Almost-Hug (Raise Lust)" if bonus == False:
            jump chikainvitelicking
        "Actually Hug (Raise Lust)" if bonus == False:
            jump chikainvitehandjob
        "Hug Hard (Raise Lust)" if chika_virgin == False and bonus == False:
            jump chikainvitemissionary
        "Headpat" if bonus == True:
            jump chikaheadpat

label callchikamorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if onsenticket == True and streets30 == True and day == 6:
        jump chikaonsen1
    if chika_love >= 45 and mall40p2 == True and chikadate45 == False:
        jump chikadate45
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Chika's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't."

        jump callmorning
    if chapthreeactive == True:
        jump chikasummer2morninggen
    else:
        play sound "phonebeep.wav"

        "I tap on Chika's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        c "Hihi~ Good morning, Sensei. You're up early today."
        c "Any reason why?"
        s "Just seeing what you're up to."
        c "Wanna see for yourself and come on over?"
        c "I'll make you breakfast~"

        scene black
        with dissolve

        "Being the type who never says no to free breakfast (Or cute girls), I get dressed and take the bus over to the second half of town..."

        scene chikamorninggen
        with dissolve
        play music "normalday.mp3"

        "I show up to find Chika stirring a pot of beef stew on the stove."
        "And while this isn't exactly the type of breakfast I envisioned, I decide to go along with it."
        "I vaguely remember a time in my life where I wound up making similar dishes due to the low price point-"
        "But that memory fades as the two of us get to talking about some gossip she heard involving some of her coworkers at the mall."

        scene black
        with dissolve

        "Chika finishes 'breakfast' and the two of us eat together while Chinami watches TV in the other room."
        "It feels almost like I'm part of the family for a moment or two."

        if bonus == True:
            "And then it feels even stranger when I realize Chika is playing the 'mother' role when she very much could be my daughter."

        "But regardless, we take our time enjoying the beef stew and wind up walking to the bus stop together so Chika can make it to work on time."
        "I get off at the last stop and decide to get on with my day..."

        $ chika_love += 1
        stop music fadeout 5.0

        "{i}Chika's affection has increased to [chika_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon

label callchikaafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if chika_love >= 45 and tsubasa_love >= 15 and mall45 == True and chikaspecial45 == False:
        jump chikaspecial45
    else:
        "I think Chika is working right now...I can probably see her if I make my way over to {i}her.{/i}"
        jump callafternoon

label chikanightgen2:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if chapthreeactive == True:
        jump chikasummer2nightgen
    else:
        scene chikanightgen2
        with dissolve
        play music "love.mp3"

        "I show up at Chika's place to find Chinami already in bed for the night."
        "She mentions going out on the balcony to talk for a bit, but quickly changes her mind the second she slides the door open."
        "Winter in Kumon-mi can be a bit dramatic at times, and it's definitely not the ideal setting for a girl who isn't wearing pants."
        "Instead of braving the cold, we decide to remain indoors and spend the night talking about random things."
        "Well, they're random to me, at least."
        "I'm sure that all of the things Chika tells me about are thoughts that linger in her head for longer than she'd like."
        "I seem to have become some sort of...informational trash-compactor that she tosses all of her thoughts into ritualistically."
        "And while I'm happy that she's enjoying sharing all of these things with me, I do wish I could understand them a little bit better."

        scene black
        with dissolve

        "But, who knows?"
        "Maybe one day, I will."

        $ chika_love += 1
        stop music fadeout 5.0

        "{i}Chika's affection has increased to [chika_love]{/i}!"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label callchikanight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if chap4active == True and senseisad == False:
        jump chikaspringnightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Chika's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        c "Heya! Great timing. I actually just got back to the apartment."
        s "Not staying at the dorm tonight?"
        c "Nahh. Gonna hang out with my sister instead."
        c "You wanna come over and watch movies or something?"
        s "Sure. I'll be right there."
        c "Kay kay! See you soon~"

        scene black
        with dissolve

        "I drop what I'm doing (Which is essentially nothing) and get on the first bus to the second half of town..."

        if christmas7 == True:
            jump chikanightgen2
        else:
            scene chikanightgen
            with dissolve

        play music "love.mp3"

        "I arrive to find both Chika and Chinami in their pajamas and huddled under the blanket watching some drama I've never seen before."
        "I'm glad that the two of them are comfortable enough to let me into the house like this, but I guess they don't really have any reason to {i}not{/i} trust me given that I pay their phone bill."
        "Regardless, Chika lets Chinami watch a few episodes alone so the two of us can hang out on her balcony and talk."
        "I watch as she gazes joyfully up at the stars, her body outlined by the subtle light of the moon."
        "And even if the moment comes and goes the second a cloud gets in the way, it's a sight I'll find hard to forget."

        scene black
        with dissolve

        "Chinami is already asleep by the time the two of us go back inside, so I decide to go home a little ahead of schedule."
        "Chika apologizes for making me come all the way here to just hang out on her balcony, but I don't mind."
        "She hugs me tightly just as I'm about to leave, and the two of us reluctantly break apart and go back to our respective lives..."

        $ chika_love += 1
        stop music fadeout 5.0

        "{i}Chika's affection has increased to [chika_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label firsttimemall:
    scene chikanewmall1
    with fade
    play music "mall.mp3"

    "I decide to spend my afternoon at the mall because-"
    "Well, I don’t really know. "
    "It’s probably safe to just chalk it up to some subconscious desire to hang around teenage girls, though, since that’s pretty much all there is to do with my life now."
    "Not like there are many other things I’d prefer doing in the first place, but you get the point."
    "Without an inkling of what to do as a middle-aged man in a shopping mall, I spend my time walking around in circles, hoping to bump into someone I know."
    "Unfortunately, this process repeats itself a good five times before I’m able to find any amount of success."

    scene black
    with dissolve2

    "That success comes in the form of one of the girls from my class, alone on a bench I’ve passed several times over now."
    "I doubt she’ll be happy to see me since the mall is like a...recreational sanctuary to girls her age, but that’s not something I’m going to dwell on when I’m getting desperate at this point."
    "Worse comes to worst, I simply walk away and the two of us forget I ever tried to talk to her in the first place."

    q "Sensei? Is that you?"

    scene chikanewmall2
    with dissolve

    s "Hey, Chika."
    c "Hey! It’s not often I see you outside of school. What brings you to the mall?"
    s "A mix of despondence, boredom, and lack of direction. You?"

    scene chikanewmall3
    with dissolve

    c "I work here. Just sat down for my break, actually."
    c "You’re welcome to join me if you want, but I doubt you’d-"
    s "Deal."

    scene chikanewmall4
    with dissolve

    c "Oh! Okay. Nevermind, then."
    c "I didn’t really think you’d want to spend your day off hanging out with somebody like, half your age."
    s "And I didn’t think you’d want to spend your break with someone old enough to be your father, but here we are."
    c "Oh, come on. You’re not {i}that{/i} old..."
    c "Are you?"
    s "I really wish I could tell you."
    c "Uhh...why can’t-"
    s "Anyway, which one of these stores do you work at? Maybe I can drop by sometime and like, support local business or whatever."

    scene chikanewmall5
    with dissolve

    c "If by “support local business” you mean pump some money into a major corporation, feel free to drop by. It’s the really fancy looking place at the east end of the mall."
    s "Does it have a weird, French name? Because I passed by a place like that earlier and couldn’t even bring myself to look inside again after catching a glimpse of the prices."
    c "Yup. That’s the one. I am but a humble slave to the retail machine that is {i}Les Vêtements{/i}."
    c "Gotta pay the bills somehow, though. You know?"
    s "Sure, but I can’t imagine someone your age has very many bills to worry about."

    scene chikanewmall6
    with dissolve

    c "Hahah...yeah..."

    scene chikanewmall7
    with dissolve

    c "But, uhh...yeah. That’s where I work. So if you ever want to drop by just to say hi or something, feel free. I won’t pressure you into buying anything since I know how crazy expensive it all is."
    s "I appreciate that. Here’s hoping the “retail machine” doesn’t eat you alive."
    c "Have you ever worked a job like that before, Sensei? "
    s "Me? No. "

    "Or at least I don’t think so?"
    "For all I know (which isn’t much on account of the whole “rebirth” thing), I could have worked in the same exact store as Chika when I was her age."
    "Without any experience to pull from, though, I’m probably better off just steering the topic toward something else."

    s "So about those bills you supposedly have to pay-"

    scene chikanewmall8
    with dissolve

    c "What? No. Why? How are we back to that?"
    s "I’m just curious, that’s all."

    "I’m not, really. I just don’t want to risk talking about myself before understanding a little more about...who I am or where I’m from or...anything like that."
    "And if making Chika slightly uncomfortable is the price to pay for saving face, I suppose she’ll just have to suffer."

    scene chikanewmall9
    with dissolve

    c "I’ve just got...other obligations, I guess. It’s not really something I want to get into right now."
    s "Other obligations? You mean like, a boyfriend?"

    scene chikanewmall10
    with dissolve

    c "Boyfriend?! No way. Nuh-uh. It’s nothing even remotely {i}close{/i} to that. I have literally never even held hands before."
    c "My obligations are like, way more boring."
    s "Well, I’m sorry to hear that."

    "But I’m not sorry I was able to confirm that Chika is, at this moment in time, completely and entirely single."

    s "I have a hard time believing you’re completely inexperienced, though. Like, based on how you look, I kind of just figured that-"

    scene chikanewmall11
    with dissolve

    c "What’s wrong with how I look?"
    s "What? Nothing. I was just trying to say you look a lot more...{i}mature{/i} than the other girls in class."

    scene chikanewmall7
    with dissolve

    c "Oh! Well, that’s totally fine then."
    c "I thought you were gonna lean into that whole “gyarus are slutty” stereotype thing for a sec and I was about to get really upset."
    s "That’s not where I was going. I just kind of figured that someone as attractive as you would be popular with the opposite sex."
    c "I don’t know. I guess I just never really- "

    scene chikanewmall12
    with dissolve

    c "Wait a second. What did you just call me?"
    s "Should I not have said that?"
    c "No, you should say it again. I want to confirm that I’m not going crazy and that those words actually did just come out of your mouth."
    s "I’m not being recorded, am I? Because this is starting to sound like a set-up."
    c "A set-up for what? If I didn’t want you around, do you really think I would have invited you to chill with me during my break?"
    s "This is our first time spending time together outside of school. I have no idea what sorts of strategies you employ."
    c "Sensei, just friggin’ say it already. It’s totally cool."
    s "Fine. I think you’re attractive. Are you happy now?"

    scene chikanewmall13
    with dissolve

    c "Duh! I’m obviously not gonna get upset by a compliment I basically forced out of you."
    s "To be fair, the first time was voluntary. "
    c "Well...thanks, Sensei. "

    scene chikanewmall14
    with dissolve

    c "Even if we’re like, way out of each other’s dating ranges, I’m totally flattered. And, just for the record, I think you’re pretty handsome too."

    "Well, {i}now{/i} we’re getting somewhere."

    s "Oh?"

    scene chikanewmall15
    with dissolve

    c "{i}Oh{/i} what? Don’t believe me? You want it in writing or something?"
    s "No, I think that would be just as risky as the whole recording thing."
    c "Do {i}you{/i} have someone back at home, Sensei? You asked me, so it’s only fair that I get to ask you as well."
    s "Me? No. I already have ten teenagers I have to keep track of and that’s more than enough for me."
    s "Also, I {i}quite literally{/i} have Ami back at home, but that’s a totally different sort of thing."

    "A thing that I should...probably start putting some more thought into since that is absolutely a bridge I’ll have to cross one day."

    c "I would {i}really{/i} hope so! Because I’m pretty sure that would be like, way illegal."
    s "This is not a thing we should be talking about at the mall."

    scene chikanewmall14
    with dissolve

    c "Probs not, but we’ve been crossing boundaries for a few minutes now, so it would probably be good to start backing things up a bit."
    s "Agreed. The big takeaway from today’s conversation is that we’re equally attracted to one another and that I’m going to be coming to the mall more often from now on."

    scene chikanewmall16
    with dissolve

    c "For real? You actually are? "
    s "Is there a problem with that?"
    c "Not at all. It’s just..."
    c "This is all kinda coming out of nowhere."
    c "Like, just a few days ago, I looked at you as a totally normal teacher. And now we’re, like...bantering and stuff, and..."
    c "I don’t know. Doesn’t this feel a little weird to you, Sensei? Like, why’d your whole outlook on teaching change all of a sudden?"
    s "Just...woke up a brand new person, I guess."

    scene chikanewmall15
    with dissolve

    c "Well, for what it’s worth...I like this person a lot more so far. "
    c "He’s a lot of fun to talk to if this...spontaneous meeting on a bench says anything about the kind of guy he normally is outside of school."
    c "Unfortunately, that’s kind of all the time I have to hang out today since I’ve gotta be getting back to work."
    c "But I’ll be looking forward to seeing you more from now on, Sensei. Both in {i}and{/i} out of school."
    s "I’ll be looking forward to that as well."
    s "See you around, Chika."

    scene black
    with dissolve2

    "“The kind of guy I normally am outside of school...”"
    "This can’t possibly be that, can it?"
    "I was able to contain myself today, but...wasn’t it only because I was dead set on doing that?"
    "Moving too quickly in the beginning tends to scare people away. It doesn’t take a genius to understand that."
    "In order to get closer, sometimes you need to lure a person into a false sense of security."
    "There’s no way that girl is truly {i}safe{/i} with me when I’ve already begun planting seeds in her garden."
    "Soon, the flowers will begin to bloom and the two of us will flourish."
    "But it will be all because I got a head start."
    "And because she left her gate unlocked."
    "I leave the mall and try to figure out what else to do with my day."


    $ renpy.end_replay()
    $ firsttimemall = True
    $ chika_love += 1

    "{i}Chika’s affection has increased to [chika_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdaynight

label mall2to4:
    play music "mall.mp3" fadein 2.0
    scene mall1
    with dissolve

    "I decide to kill some time at the mall again."
    "Chika is sitting on a bench when I get there and she quickly waves me
    over to come watch some video on her phone."
    "She goes on to talk about a few new pop-stars and makeup
    tutorials and I basically just sit there and absorb her words, understanding very little."
    "Despite the two of us having virtually nothing in common, I feel strangely comfortable with her..."

    scene black
    with dissolve

    $ chika_love += 1

    "{i}Chika’s affection has increased to [chika_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdaynight

label mall5:
    scene mall1
    with dissolve
    play music "mall.mp3"

    "Once again, I decide to kill some time at the mall."
    "This time, however, it doesn’t look like Chika is on her normal bench."
    "I suppose my streak of perfect convenience comes to an end today as I must now scan the halls of this brightly colored, obnoxiously loud building in order to find her."
    "But it is what it is, I guess."
    "I was honestly beginning to question whether or not she even had a job or if she was just pretending to have one to impress me."
    "Granted, she could {i}actually{/i} be working right now, but...I don't know."
    "I won't believe it until I see it."

    scene mall2
    with dissolve2

    "I walk around the mall for a good ten minutes or so without any sign of Chika, meaning she’s either off today or on the clock right now."
    "If I remember correctly, I think she said she worked at some high-end boutique or something along those lines."
    "The only problem is that I have no idea what counts as {i}high-end,{/i} so I don't even have a place to start."
    "Not knowing what else to do, I check out a nearby directory and pinpoint the store with the fanciest name I can find before beginning my search there..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mallfive1
    with dissolve2

    c "Hey, welcome-"
    c "Woah! Sensei! I had no idea you were coming in today!"

    scene mallfive2
    with dissolve

    "Chika excitedly throws a handbag onto a display shelf and hurries over to me."

    c "Hey! What are you doing here? Shopping on your day off?"
    c "We're actually having a sale on men's clothing right now, so instead of everything costing like, 90%% of your annual salary, it's probably closer to, like...70%%."
    s "Wow, you really weren’t kidding when you said ‘high-end’ were you?"

    scene mallfive3
    with dissolve

    c "Hahahah~ Oh, come on! You know I’m just messing around!! There's no way we'd charge more than 60%% of your annual salary, tops."
    s "You know, I think I'll stick to my one outfit."

    scene mallfive4
    with dissolve

    c "I get it, no worries. I guess everything here {i}is{/i} still kind of expensive when you compare it to...literally everywhere else."

    scene mallfive4r
    with dissolve

    c "But you’re like, a big shot teacher, right? I’m sure you’ve got some extra cash to spare."
    s "I mean...I wouldn't say I'm {i}poor{/i} by any means, but I'm not really sitting on a mountain of cash either."
    s "Besides, I don’t really think any of this stuff would suit me."

    scene mallfive5
    with dissolve

    c "Hey, don’t say that! I think you’d look really handsome in some of our stuff."
    c "I can help you pick some stuff out, if you want. I'm pretty good at that sort of thing."
    s "Maybe some other time. I sort of just dropped by to see how you were doing today."

    scene mallfive6
    with dissolve

    c "Oh my God! Did you really come all the way over here just to see me?! That’s like, totally adorable!"
    c "How come? Isn’t there someone like, closer to your age you’d rather spend your time with?"
    s "Someone I’d rather hang out with than Chika Chosokabe? Unlikely."

    scene mallfive7
    with dissolve

    c "Oh, stop it. I don't believe that for even a second."
    c "There’s gotta be {i}someone{/i} out there you’ve got, like...more in common with or whatever."
    s "I don’t think we need to have anything in common to enjoy being around each other."
    s "If you enjoy being around me, I mean."

    scene mallfive2
    with dissolve

    c "Oh my God, of course I like being around you! Haven’t you noticed that I’ve been skipping class waaaaay less often lately?"
    c "My grades have been getting a little better-ish, too!"
    c "I mean, I’m sure that’s also thanks to you barely giving us any work, but yeah. I like you."

    scene mallfive8
    with dissolve

    c "Oh! Wait! No! Not like that! That...That probably sounded weird, didn't it? Like...I like you as a {i}teacher.{/i} Or a...friend. Or something."
    s "Don’t worry, Chika. I like you too."

    scene mallfive6
    with dissolve

    c "I...okay! Yeah!"
    c "We...like each other! Which is awesome!"
    s "..."
    c "Well, uhh...just so you know, you can come hang out here whenever you want."
    c "I work most of my shifts alone, so as long as my boss isn’t here and it’s not super busy, I'd love to see you."

    scene mallfive9
    with dissolve

    c "And who knows? Maybe I’ll even let you judge some of the stuff I try on but can’t afford!"
    s "Well, I'm not really known for my fashion sense, but I’d love seeing you dress up."
    c "You’re in luck, then! Part of the job is knowing what would look good on who, and I can't really {i}know{/i} that without trying stuff on myself."
    s "Again, not a fashion icon, but I don't really think that's true."
    c "Well, I won't tell anyone you're here to watch me try on clothes if {i}you{/i} don't tell anyone that it's a perk I've been taking advantage of."

    scene mallfive4
    with dissolve

    c "Just kinda wish dresses looked a little better on me."
    s "Really? Why is that?"

    scene mallfive7
    with dissolve

    c "Mmm...Idunno. I guess they just don’t really fit my style?"
    c "All the clothes I wear are pretty flashy, so trying on cutesy stuff just makes me feel like a loser."
    s "I’m sure you don’t look like a {i}loser.{/i} I can't really see anything not working on you, if you want my opinion."
    s "In fact, I'm going to seize this opportunity and say that you should model a dress for me before anything else."

    scene mallfive10
    with dissolve

    c "How come we've gotta start on hard mode?! What about, like...a tank top or something?"
    c "We've got a whole lingerie section too, you know. Which isn't me implying that I'd model any of it for you. But at this point I'm just trying to steer the conversation away from the dress thing and-"
    s "If lingerie is off the table, I'm going to stick to the dress suggestion."

    scene mallfive7
    with dissolve

    c "I mean...I wouldn't say it's off the table {i}forever...{/i}just..."
    c "Oh my God. What am I even saying right now? I'm sorry, Sensei. I just-"
    s "There's no need to apologize. {i}Other{/i} teachers might get weirded out by the idea of a student offering to one day model underwear for them, but not me."
    s "Which sounds a lot worse when I say it out loud, but I can guarantee it's-"
    c "Uhh...would you maybe...mind keeping your voice down a little? I don't really have a problem with what we're talking about, but I don't want you to, like...get in trouble or anything."

    "I quickly look around to make sure no one's been paying attention to the conversation and confirm that we at least {i}appear{/i} to have gone unnoticed just now."

    s "I think we're fine. But yeah, that's probably not something we should talk about."
    s "Even if it was a completely normal conversation between two people without any ulterior motives whatsoever."

    scene mallfive6
    with dissolve

    c "See, this is why I like you! You’re so chill about everything and like, never make me feel uncomfortable even when we're talking about uncomfortable stuff."
    c "It's kind of like you’re my...big brother or something."

    if bonus == True:
        s "You would model lingerie for your big brother?"
    else:
        s "Sure. A big brother who really fucking likes clowns."

    scene mallfive10
    with dissolve

    c "Well, I-"
    c "Uhh..."
    c "No! Of course not!"
    c "Also, I thought we were moving on!"
    s "I'm sorry if this bursts your bubble, Chika, but I don't really see you as a little sister."

    scene mallfive5
    with dissolve

    c "Well...what {i}do{/i} you see me as, Sensei? Just out of curiosity."
    c "I’ve never had a teacher come visit me at work before. And it’s not like I really view you as {i}just{/i} a teacher either, so..."
    s "I view you as Chika."

    scene mallfive4
    with dissolve

    c "That feels...weirdly embarrassing to hear for some reason..."

    scene mallfive6
    with dissolve

    c "Like, I’m glad you see me as me and not just some...flirty bimbo who’s always breaking dress code and stuff."
    s "It would be kind of hard to view you as a {i}flirty bimbo{/i} since you recently confirmed to me that you’ve never done anything with a boy before."

    scene mallfive10
    with dissolve

    c "Well, that's not because I’m {i}against{/i} it! I just...haven't met the right person yet! Nobody's really interested me or whatever!"
    c "Plus, I’m super busy all the time and like, no one’s schedule would ever match up with mine."
    s "You think so? Because my schedule seems to match up pretty nicely. We even see each other during[school] days."

    scene mallfive3
    with dissolve

    c "Yeah, but it’s not like I can have my teacher as a boyfriend, right? Isn’t that like, totally against the rules?"
    s "Since when do you care about rules?"

    scene mallfive6
    with dissolve

    c "Ooooh, good point. So what, then? You wanna go out, Sensei?"
    s "Would you be able to keep it a secret?"

    scene mallfive10
    with dissolve

    c "Wait, we're still joking, right? I wasn’t...really being serious, but you look super serious right now and it's making me unsure of how to answer."
    s "..."

    if bonus == True:
        "I guess I should probably wait a {i}little{/i} longer before I go down that path with Chika."
        "I keep forgetting how innocent she is despite her subconscious desire to flirt with me every second of the day."
        "I can definitely feel the two of us getting closer quickly, so I'm sure {i}more{/i} is bound to happen eventually, but..."

        s "Let's take a rain check on dating. I need to at least see you in lingerie before I make my final decision."
    else:
        s "Of course it’s a joke. I need to at least see you in a clown costume before I make my final decision."

    scene mallfive9
    with dissolve

    c "Heheh...sounds good to me."
    c "I guess all we can really do is hope you’re not disappointed whenever that time finally comes..."

    scene black
    with dissolve2

    "Chika and I hang out for a little while longer before a few customers walk in and she needs to focus on them."
    "I decide it’s time to head back and we say our goodbyes to one another."
    "Having no other reason to stay at the mall, I board a bus back to the main part of the city and attempt to figure out what to do with the rest of my day..."

    $ renpy.end_replay()
    $ mall5 = True
    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label mall10:
    scene mall2
    with dissolve
    play music "mall.mp3"

    "I show up at the mall a little later than usual after getting caught up in traffic."
    "Chika’s break should have already ended by now, so I guess I’ll wind up hanging out with her at her work again today."
    "Not like that’s a problem, though."
    "In fact, it might be {i}good{/i} that I showed up late because it increases the chances of her taking her clothes off for me."
    "Obviously, she'd be putting on {i}different{/i} clothes and not letting me watch the act of doing so- but either way. She is taking off her clothes for me."
    "And that is all I need to know."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mallfive1
    with dissolve2

    c "Heya! Welcome-"
    c "Ah! Sensei!"

    scene mallfive2
    with dissolve

    c "Great timing. I was just thinking about you."
    s "You mean you aren’t {i}always{/i} thinking about me? Bummer."

    scene mallfive3
    with dissolve

    c "Cut me some slack, Sensei! If I spent literally {i}all day{/i} thinking about you, I’d forget to come to work and lose my job and it would be like, a whole thing."
    c "Besides, there's no way you think about me even half as much as I think about you."

    "Sure I do. I just can't talk about the majority of those thoughts out loud."

    s "I suppose that you dedicating any amount of time to me is more than enough, but I still implore you to try and fit more in whenever possible."

    scene mallfive9
    with dissolve

    c "I'll see if I can pull some strings and make that happen."
    c "So, you ready?"
    s "Ready for what?"
    c "Seeing me try some stuff on, dummy! That's why you came, isn't it?"
    s "I mean...that wasn't the {i}only{/i} reason."
    c "Well, I'm ready whenever you are."

    scene mallfive4
    with dissolve

    c "Plus, I found a dress that I might actually look good in, so..."
    s "Do you need any help putting it on?"

    scene mallfive9
    with dissolve

    c "Mmm...no. I think I can handle that part myself. You can follow me over to the dressing room, though."
    c "And if there’s anything you wanna try on, just let me know. Maybe I can judge you after you do me?"
    s "You can do me whenever you want, Chika."

    scene mallfive2
    with dissolve

    c "Thanks! Just follow me to the-"

    scene mallfive8
    with dissolve

    c "Wait! No! I said a weird thing again! I didn't mean it like that!"
    s "So...we're {i}not{/i} going to do each other?"
    c "Not yet!"
    s "But doesn't that imply-"
    c "Nope!"
    s "..."
    c "Anyway! Time to get dressed!"

    scene black
    with dissolve2

    "Chika awkwardly shuffles her way over to a separate part of the store, straightening out her skirt and shaking off whatever nerves started acting up as a result of her inappropriate wording just now."
    "I have to do the same, but it's less {i}awkward{/i} and I can't imagine it looking even half as attractive."
    "Either way, she stops in front of the dressing rooms before turning to face me."

    scene mallten1
    with dissolve2

    c "Okay, so. Disclaimer-"
    c "I’ve already told you that dresses aren’t my thing...so even if I said that I like this one...please don’t expect too much."
    s "Deal."
    c "Great. Disclaimer part two-"
    c "Make sure you wait until I’m done getting dressed to actually come in."

    scene mallten2
    with dissolve

    s "I liked the first disclaimer more."
    c "I bet you did, Sensei."
    c "And remember- I’m still {i}technically{/i} at work, even if there aren’t any customers right now."
    s "I hope there's not a third disclaimer stating that I need to help any of them while you're getting changed."
    c "..."
    s "Chika, I don't know how-"

    scene mallten3
    with dissolve

    c "Then, I guess all we can do is hope that nobody comes in!"
    c "But yeah! Other than that, just don’t make fun of me when I look like a fish out of water and we'll be all good!"
    s "Sounds easy enough. Apart from the idea of helping customers, I mean."
    c "Great! Then, hang out here for a couple minutes while I get dressed and...I'll see you soon."
    s "Sure thing. Let me know if your bra gets stuck and you need help getting it off."
    c "One of the hooks is already broken, so I doubt that'll be a problem. But thanks for the offer."

    scene black
    with dissolve2
    stop music fadeout 25.0

    if bonus == True:
        "Chika disappears into the dressing room and I can hear her clothes beginning to fall to the floor moments later."
        "It takes every ounce of self-control I have to not sneak in there, but I respect Chika's wishes and remain outside."
        "I'm sure a day will come when I don't have to do that anymore but, for now, the best way for me to get closer to her is to respect the very few boundaries she actually establishes."
        "I know that, at the end of the day, she is taking her clothes off for me right now."
        "So I justify my wait by reiterating that single thought over and over in my head until the time finally comes to-"
    else:
        "Chika disappears into the dressing room and I wait outside like the respectable man I am."

    c "Sensei! I'm...suddenly having second thoughts about this."

    "The time comes sooner than expected."

    s "What? Why?"
    c "Because I look like a freaking idiot."
    s "Chika-"
    c "Fine! Fine..."
    c "You can come in, just..."
    c "I'm sorry in advance for the disappointment..."

    scene black
    with dissolve2

    "I follow the sound of Chika's voice, slightly muffled by a thick red curtain-"

    scene mallten4
    with dissolve2
    play music "love.mp3"

    "And stumble upon a wonderful sight."

    c "Yeahhh, so...I kinda thought I’d look a little cuter than this...but it’s whatever, I guess."
    c "Dresses just aren’t my thing. I promise I’ll wear something more exciting next time."

    if bonus == True:
        c "Maybe not something as exciting as {i}lingerie{/i}, but..."
    else:
        c "I know that this probably isn't that great compared to a clown costume, but..."

    s "Don’t say that. Just because it's different from how you normally look doesn't mean it's {i}bad.{/i}"
    c "It doesn't mean it's {i}good{/i} either, though..."
    c "Like...how do you really think I look like dressed in stuff like this, Sensei? Be honest."

    menu:
        "I think you look beautiful":
            s "I think you’re beautiful, Chika."
            c "Yeah, that’s what I-"

            scene mallten10
            with dissolve

            c "Wait, what? Who? Me?"
            c "What did you just say?"
            s "I said I think you look beautiful."
            c "Yeah, but like...sarcastically, right? Like what you {i}really{/i} think is that I resemble an out-of-place[teen]on her way to Easter breakfast with her grandparents."
            s "I would...never think something that specific. I just genuinely think you look great."
            c "You...You know that I’ll still like you even if you tell me the truth, right? You don't have to be nice 100%% of the time."
            s "I am telling you the truth."

            if bonus == True:
                c "And you know I’ll still eventually do the lingerie thing even if you don’t compliment literally everything I ever wear, right?"
                s "Just accept the compliment, Chika."

                scene mallten11
                with dissolve

                c "Ahhhhh! I wanna! It’s just super embarrassing and I didn’t expect you to say anything good!"
                c "Maybe you just...need to take a closer look or something?! I don't know!"
                c "You wear glasses so your eyes are probably bad and-"
                s "Fine. "

                scene mallten12
                with hpunch
                play sound "thump.mp3"

                s "Nope. Still beautiful."
                c "Oh my God. A real kabedon. Am I dreaming?"
                s "What?"
                c "Nothing. Don't stop."
                s "Uhh...I don't really know what else there is to say other than you still look great."
                c "You’re not even looking at the dress anymore."
                s "Yeah. There's something else I like looking at a little more."
                c "Oh my fucking God, my hot teacher is kabedoning me. I'm in an anime. This isn't real."

                "Chika presses her back against the mirror not to get away, but to make herself more comfortable."
                "She's obviously surprised by me suddenly closing the distance like this...but she {i}was{/i} the one who suggested it, so..."

                scene mallten13
                with dissolve

                c "..."
                s "..."
                c "Your..."
                c "Has anyone ever told you how pretty your eyes are?..."
                c "And like, not even just that...you're straight up {i}really{/i} attractive up close..."
                s "I'll make sure to get as close as I can when I flirt from now on, then."
                c "Do you...really not have a girlfriend?"
                s "I already told you. I’m preoccupied with a bunch of [teenager]s instead."
                c "Sorry, I just..."
                c "My heart’s beating out of control right now and it’s kinda hard to remember stuff."
                s "Is it?"
                c "Uh-huh..."
                s "And why is that, Chika?"

                scene mallten14
                with dissolve

                c "Oh, I don't know, Sensei! Why do you think?!"
                s "Is that sass I hear right now?"

                scene mallten15
                with dissolve

                c "Are you gonna give me detention if I say yes?"
                s "I am now. Please drop by my office after[school] as soon as possible."
                c "What are you gonna make me do, Sensei?"
                s "I guess we’ll find out soon enough, won’t we?"
                c "Is it wrong for me to be a little excited?"
                s "Do you want the real answer or the hotter one?"
                c "Gimme the hotter one."
                s "Then, no."
                c "I've never had a detention before, Sensei. You might have to give me directions."

                "This is so much better than lingerie."

                scene mallten16
                with dissolve

                "I bring my hand to Chika’s face, not knowing exactly how she'll react but, as you can see, it works out pretty favorably."

                c "About time."
                s "Am I moving too slow for you?"
                c "Yes."

                scene mallten17
                with dissolve

                c "Ahm~"

                "Oh."
                "Oh, okay."

                c "Mnh...mmm..."
                s "..."

                scene mallten18
                with dissolve
                stop music fadeout 15.0

                c "Mnch...mmm..."

                "In a welcome turn of events, Chika slowly and gently wraps her tongue around my thumb, sensually taking as much of it into her mouth as she can."
                "To say I'm shocked is a bit of an understatement, but she's been more or less full of surprises thus far and the idea of her being into things like {i}this{/i} isn't too absurd."
                "And again, this is so much better than lingerie."

                c "Mm...mm...you like that, Sensei?..."
                c "This is...amf...what you wanted...right?..."
                s "..."
                c "..."

                scene mallten19
                with hpunch
                play music "mall.mp3"

                c "Oh my God. Please tell me I didn't just {i}dramatically{/i} misread the situation."
                c "Cause I really thought that was where we were going with that and-"
                s "No, it's just...I'm a little surprised."
                s "I thought you were innocent, is all."
                c "I am innocent!"
                s "The saliva all over my thumb begs to differ."
                c "That's...I don't know, Sensei! It seemed like the right thing to do at the time!"
                c "I just got worried that you were talking about an {i}actual{/i} detention when you stopped talking and just let me keep going and...and..."

                scene mallten20
                with dissolve

                c "And your thumbs are big! You should...apologize! For...for having such..."
                c "Such...large..."
                s "..."
                c "..."
                c "I'm going back to work now!"

                scene black
                with dissolve2

                "Chika storms out of the dressing room and, once I follow her out, she begs me for the next ten minutes to forget any of that ever happened."
                "Well, not {i}any{/i} of it- but the part where she started fellating my finger."
                "Regardless, it’s clear now that there’s at least some form of chemistry between us."
                "What that chemistry {i}is{/i} remains to be determined."
                "But once it reaches its full potential-"
                "I can see Chika becoming someone I'll never forget."
                "........."
                "......"
                "..."
                "Oh, and also, she is good with her tongue."

                $ renpy.end_replay()
                $ chikadetention = True
                $ mall10 = True
                $ chika_love += 1
                stop music fadeout 5.0

                "{i}Chika’s affection has increased to [chika_love]!{/i}"
                "........."
                "......"
                "..."

                jump saturdaynight
            else:
                c "Even though I'm not a clown?"
                s "Even though you're not a clown."

                scene black
                with dissolve2

                "Somehow, nothing else happens in that dressing room."
                "The two of us just stared at each other for what felt like hours and then left as if nothing had ever happened in the first place."
                "But it’s clear now that there’s chemistry between us, and I’ll be damned if I don’t capitalize on that as soon as possible..."

                $ renpy.end_replay()
                $ chikadetention = True
                $ mall10 = True
                $ chika_love += 1
                stop music fadeout 5.0

                "{i}Chika’s affection has increased to [chika_love]!{/i}"
                "........."
                "......"
                "..."

                jump saturdaynight

        "I think you look fine":
            s "I think you look fine."
            s "Sure, it’s not as fitting as your normal clothes, but you’re still adorable."

            scene mallten5
            with dissolve

            c "Guh...Maybe if I started, like...styling my hair differently, I could pull stuff like this off?"
            c "I’m sure makeup plays some part in it too, but that's like, a crazy amount of work."

            scene mallten6
            with dissolve

            c "Sorry for subjecting you to this, Sensei. Just can't help but feel like I should maybe try and change up my image every once in a while."
            s "What are you apologizing for? I don't see anything wrong with your normal style."
            c "I don't know. It's just that the whole gyaru thing attracts some unwanted attention at times."

            scene mallten7
            with dissolve

            c "Plus, you hanging around with a girl who looks like I do might...send some bad signals out or something."
            s "Dress however you want to dress, Chika. Don't tailor your style to fit me or anyone else."
            s "If you like it, wear it. That's really all there is to it."

            scene mallten8
            with dissolve

            c "Yeah...Yeah, that's a good point."
            c "As long as you don’t think I look weird or whatever, I’ll probs just keep dressing how I have been."
            c "It would suck having to buy a whole new wardrobe anyway..."
            s "At least if you start saving now, you might be able to afford something here by the time you retire."

            scene mallten9
            with dissolve

            c "Hahah! Yeah...maybe."

            scene mallten7
            with dissolve

            c "Well, uhh...I guess I should probably be getting back to doing my job or whatever now."
            c "You’re sure no one saw you follow me in here, right?"
            s "I...don’t remember checking, actually."

            scene mallten8
            with dissolve

            c "Oh well. We've been slow all day anyway, so I doubt there were any customers while we were in here."
            c "Just...you go out first and I'm sure everything will be alright. I still need to put my regular clothes back on anyway."

            if bonus == True:
                s "It's fine. I'll stay for that part. I want to understand your process."
            else:
                s "But you haven't turned into a clown yet. Is that-"

            scene mallten9
            with dissolve

            c "You will most certainly not stay for that part, Sensei."
            s "Well, you can't blame me for trying."

            scene black
            with dissolve2

            "I exit the dressing room and Chika comes out a minute or two later."
            "We chat for a little while longer before her boss calls and she needs to go over some inventory stuff with her."
            "As such, I exit the store and am once again subjected to aimlessly wandering the streets of Kumon-mi..."

            $ renpy.end_replay()
            $ mall10 = True
            $ chika_love += 1
            stop music fadeout 5.0

            "{i}Chika’s affection has increased to [chika_love]!{/i}"
            "........."
            "......"
            "..."

            jump saturdaynight

label mall15:
    scene mall1
    with dissolve
    play music "mall.mp3"

    "I show up at the mall around the same time I always do and immediately take note of Chika not being on what I will now just refer to as {i}our{/i} bench."
    "Being an adult who's able to pick up on context clues, I understand that her absence means she’s working right now and I begin to ponder over whether or not today is the day I have been waiting for."
    "It's been a while since Chika has modeled anything for me and we've definitely grown closer since then. So either we're at the lingerie stage {i}now{/i} or we will be soon."
    "Either way, I must do my duty and find out."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene whyissheadog1
    with dissolve

    s "Chika, are you around? I was thinking that today we-"

    scene whyissheadog2
    with dissolve2

    s "..."
    q "..."
    s "..."
    q "..."
    s "..."
    q "..."
    s "Okay, nevermind. I’ll come back later."

    scene black
    with dissolve

    "Not knowing how to handle the situation I have somehow found myself in, I immediately turn around and head for the door."
    "Of course, the small hand of the strange...helmeted figure reaches out and grabs my wrist."
    "Her grip obviously isn’t strong enough to prevent me from leaving since she is only a fraction of my size...but I’m pretty sure I know who this is anyway and that there isn't any {i}real{/i} reason to run."

    scene whyissheadog2
    with dissolve

    chd "Woof!"
    s "Hello, Chinami."
    chd "Woof!"
    s "Would you mind explaining to me why you’re dressed like that? And...out in public?"
    chd "Big sis made Chinami put on her special mall clothes so she could be safe at work!"
    s "You’re not...covering your sister’s shift, are you? Because I don't think you're old enough to work here."
    chd "Chinami is a 5,000 year old wizard! She is more than old enough to work!"
    chd "But no! Chinami didn’t want to be alone today and big-sis Yumi couldn’t come over."
    s "Yeah, you’re probably better off without Yumi anyway."
    chd "Woof!"
    s "Chinami, would you mind telling me where your sister is?"
    c "I’m coming! Hold on one sec!"
    chd "..."
    s "..."

    "This stare-down is making me incredibly uncomfortable."

    c "Chinami, go be a good girl and go...organize the underwear or something."
    chd "Okay! But Chinami needs to be sure she'll be fairly compensated!"

    scene whyissheadog1
    with dissolve

    "What exactly would be {i}fair{/i} compensation for child labor?..."

    scene whyissheadog3
    with dissolve

    c "That kid, I swear."
    s "She’s not a kid. She’s an ancient wizard. Be careful."

    scene whyissheadog4
    with dissolve

    c "Right, right. My bad."

    scene whyissheadog5
    with dissolve

    c "So, whatcha up to today, Sensei? Come to spend some time with your favorite student?"
    s "It certainly appears that way."
    c "Well, sorry to break your heart, but I’m kinda slammed right now. I’ve even resorted to having Chinami help since I can't handle all of this on my own."
    s "I’m pretty sure that's against the law, but whatever."
    c "I mean, it at least got her out of my hair for a little while...but you're right. I should probably figure something else out instead."
    c "It's just kinda hard since I can't really afford a-"

    scene whyissheadog6
    with dissolve

    c "Wait a second..."
    s "..."
    c "..."
    s "Please, no."
    c "I just got like, a totally awesome idea."
    s "No you didn't."
    c "Do you think that maybe {i}you{/i} could watch her?"
    s "No."

    scene whyissheadog7
    with dissolve

    c "Pleeeeeeease, Sensei? I’ll make it up to youuuuu~"
    s "How?"
    c "I don't know. Is there anything you want? What if I like, buy you lunch or something?"

    if bonus == True:
        s "I demand an expedited lingerie modeling session."
    else:
        s "Clown costume????"

    c "You’re still going on about that? That was like, forever ago."
    s "There are some promises you can’t back down from, Chika."
    c "This is a weird time to start dropping inspirational quotes."
    s "It's also a weird time for me to become a babysitter."

    scene whyissheadog8
    with dissolve

    c "How about this! Either you watch my sister or I call security and tell them some old guy is harassing me."
    s "This is blackmail."
    c "I guess maybe it is a little, yeah."
    s "You’ve been hanging out with Yumi too much."

    scene whyissheadog9
    with dissolve

    c "Kinda unavoidable when we sleep in the same room."
    s "Fine. I’ll do it. You’re going to have to explain the dog thing, though."

    scene whyissheadog8
    with dissolve

    c "I’m sure it’s not far off from whatever you're thinking. "
    c "Chinami doesn’t like wearing face-masks because they make her look funny. But, for some reason, she’s totally cool with a giant dog helmet."
    c "And she has to wear gloves to prevent herself from touching anything with germs. And the scarf thingy-"

    scene whyissheadog3
    with dissolve

    c "Well...that I don’t really have an answer for. I think she just likes it."

    scene whyissheadog9
    with dissolve

    c "She’s still super cute, though, right? And the way she’s all like “woof!” Oh my god. I wanna die."
    s "You might want to keep an eye on her in case she walks up to any other customers, though."

    scene whyissheadog6
    with dissolve

    c "Who, Chinami? She wouldn’t do something like that. She never talks to strangers."
    s "Are you sure about that?"
    c "Mhm. Why do you ask?"
    s "Because she’s trying to pet a customer’s dog right now."

    scene whyissheadog10
    with dissolve

    c "What?! Chinami! Stop that right now!"
    c "Just because you're in dog form doesn't mean you can play with...{i}other{/i} dogs!"

    scene black
    with dissolve

    "Chika runs over and snatches her sister away right before she comes into contact with a small dog hanging out of a wealthy-looking woman’s purse."
    "Feeling the need to get her out of here in order to avoid any other possible issues, Chika pawns Chinami off on me and sends the two of us out to go...walk around the mall or something."
    "........."
    "......"
    "..."

    scene whyissheadog11
    with dissolve

    s "What has my life become?"
    chd "Woof!"

    "Chinami’s tiny hands wrap around mine as the two of us walk through the mall."

    if bonus == True:
        "I’m sure everyone around thinks she’s my daughter-"
        "Or...at least, I {i}hope{/i} everyone around thinks she’s my daughter. It would be extremely problematic for them to think anything else at this point."
        "I'm sure the dog mask isn’t doing us any favors, either."
    else:
        "I wonder if this is what owning a dog is like."

    chd "Are you going to be Chinami’s new daddy?"

    if bonus == False:
        "I don't think this is what owning a dog is like."

    scene whyissheadog12
    with dissolve

    s "..."
    chd "..."
    s "No."
    chd "Why not? You and my big sister are in love, aren’t you?"
    s "No."
    chd "You’re not?"
    s "No, Chinami. I’m just her teacher."
    chd "Chinami doesn’t know much about teachers since Chinami is home-schooled. Do all teachers visit you at work?"
    s "..."
    s "No."
    chd "Then why are you visiting Big Sis? Do you need to buy new clothes?"
    chd "You look like you need to buy new clothes."
    s "I...Yeah, sure. Let’s go with that."
    chd "Do you have lots of money?"
    s "I have an adequate amount of money."
    chd "Will you buy Chinami a cell phone?"
    s "What are you going to do with a cell phone, Chinami?"
    chd "Chinami likes the game where you shoot birds at pigs and make them blow up."
    s "Then, no. I'm not going to buy Chinami a phone."
    chd "Do you actually hate Chinami?"
    s "No. I just don’t think your sister would be happy if I bought you a phone."

    scene whyissheadog13
    with dissolve

    chd "Why not? Are cell phones expensive?"
    chd "Chinami has 500 yen at home that she found at the beach."
    s "That’s nowhere near enough."
    chd "Okay. Chinami will save up more."
    chd "Thank you for telling her."
    s "... "
    chd "..."
    chd "Can Chinami ask you a question?"
    s "What is it, Chinami?"

    if bonus == True:
        chd "Where do babies come from?"
    else:
        chd "Why do you like clowns so much?"

    s "Ask something else, Chinami."
    chd "Okay. Chinami has another question anyway."
    s "What is it this-"

    scene whyissheadog13r
    stop music

    chd "Where do people go when they die?"
    s "..."
    chd "..."
    s "..."
    chd "..."

    scene whyissheadog12
    play music "mall.mp3"

    s "How about I just ask you some questions instead?"
    chd "Okay! Chinami thinks that sounds fun."

    "I can’t see through the dog helmet, but I can tell that there is a demon inside."

    s "Are...dogs your favorite animal, Chinami?"
    chd "Yes! Chinami wants a dog but she’s not allowed to have one cause dogs can get people sick."
    s "Can they? I thought that was just a myth."
    chd "Chinami doesn't know because she is home-schooled. She just believes whatever her big sisters tell her."
    chd "But if you want to teach Chinami all about animals, she’ll pay close attention."
    chd "She is currently very interested in giraffes!"
    s "I can barely even teach my students math. I don’t really think I’m qualified to teach you about what diseases animals carry."
    chd "You can teach Chinami math, then! And you can teach big-sis Yumi, too!"
    s "I’d love to if she would actually show up to class every once in a while."
    chd "Oh. Chinami forgot Yumi goes to[school] again."
    s "Don’t worry, Chinami. I forget that too sometimes."
    chd "Can Chinami ask another question?"
    s "That depends. Is it going to be something else incredibly difficult to answer given the nature of our relationship?"
    chd "Woof!"
    s "..."
    s "What’s your question, Chinami?"
    chd "Who are the girls in front of us?"
    s "Girls? What g-"

    scene whyissheadog14
    with fade

    a "..."
    m "..."
    chd "..."
    s "I can explain."
    a "Um...what?"
    chd "Woof!"
    s "..."
    s "This is a dog."
    chd "Woof!"
    a "Oh. Okay. Yes. That makes perfect sense."
    a "Sensei...wants to get me a present and...is looking at dogs..."
    m "That's-"
    a "It is clearly a dog, Maya. Just look at it."
    m "..."
    s "Nothing to see here."

    scene whyissheadog14r
    with dissolve

    m "What the actual fuck?..."
    a "Let’s go, Maya. Staying here and getting to know the dog will spoil the surprise."
    s "That’s a good idea. Hurry along, Ami. Forget what you saw here."
    a "I will. I'm sorry for bothering you on your day off, Sensei. I’ll see you later."

    scene whyissheadog15
    with fade

    if bonus == True:
        m "Do you need me to call the police?"
        s "Maya, come on. There is a perfectly reasonable explanation for this."
        chd "Woof!"
        m "..."
        s "..."
        m "Run."
        m "Run as far away as you can."
    else:
        m "Whatever you do, don't talk about clowns."
        m "I know from previous timelines that he really likes them."
        chd "Woof!"

    scene whyissheadog16
    with fade

    a "..."

    "Maya leaves, but Ami appears to be having some difficulty regaining control of her legs."

    a "..."
    s "..."
    a "You know...the more I look at her-"
    s "Forget what you saw here, Ami."
    chd "Woof!"
    a "..."
    s "..."

    scene whyissheadog17
    with dissolve

    a "My head hurts..."
    s "Okay. We’re heading back to your sister’s store now whether she likes it or not."
    chd "Chinami agrees! She feels like that could have gone better!"

    scene black
    with dissolve2

    "Thankfully, by the time we get back to the boutique, Chika’s already caught up on restocking the store and is able to take Chinami back without issue."
    "Myself, on the other hand..."
    "Well, it looks like I might have some explaining to do later..."

    $ renpy.end_replay()
    $ chika_love += 1
    $ mall15 = True
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label mall20:
    scene mall2
    with dissolve
    play music "mall.mp3"

    "I show up at the mall around the usual time and head directly over to Chika’s store when I notice she’s not on her normal bench."
    "The only issue is...she’s not at the store either."
    "Instead, some random girl around the same age as me is. Chika’s manager, maybe?"
    "Either way, I'm forced to look around the store for a few minutes so that it doesn't seem like I'm just some random guy who came in looking for a specific [teenage]girl."
    "And {i}now{/i} I’m forced to look around the mall to find Chika...if she’s even here."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene mall1
    with dissolve

    s "Huh...No Chika anywhere to be found. "
    s "Maybe she’s just off today?"

    "Chika having the day off is a thought that never even crossed my mind. "
    "I mean, she’s been here virtually every weekend since I woke up in Kumon-mi."
    "But I guess that even scripted events sometimes-"

    c "Okay, Chinami. Remember what I told you?"
    s "Hm?"

    scene chinamisphone1
    with fade

    chd "No talking to strangers!"
    c "Good girl. And what else?"
    chd "No microtransactions!"
    s "What’s going on here?"

    scene chinamisphone2
    with dissolve

    c "Hm? What do you-"

    scene chinamisphone3
    with dissolve

    c "Oh, Sensei! I didn’t expect to see you here so late in the day."
    s "Late in the day? It’s basically the same time it always is when I show up."
    c "That’s not true. It’s like, almost thirty minutes later."
    s "That’s only because I’ve been scouring the place looking for you."

    scene chinamisphone4
    with dissolve

    c "Oh, crap! I totally forgot to tell you I have the day off today."
    s "If you have the day off, what are you doing at the mall?"
    chd "Chinami is getting a phone!"

    scene chinamisphone5
    with dissolve

    c "Yup. Just like she said, I caved and I’m letting her get a phone."
    c "She’s been having to stay at home alone a lot more lately and I figured it would be good for her to be able to keep in touch with me at all times of the day."
    c "Especially since our house-phone was just deactivated and stuff."
    s "Deactivated? Why?"

    scene chinamisphone6
    with dissolve

    c "Money, obviously."
    c "Adults have so many bills that it’s kinda hard to keep up with all of ‘em."
    c "So when I missed the payment for the landline I figured I could just add Chinami to my cell-plan."

    "I figured it was something along those lines. I honestly feel a little foolish for even asking."
    "It makes sense that she’s not able to keep up with all of her bills just working part-time at a boutique in the mall."
    "Hell, it would probably be hard no matter how many hours she worked here every week."

    s "How much is it to add Chinami to your plan?"

    scene chinamisphone7
    with dissolve

    c "I looked it up online and I think it was somewhere around another 4,000 yen. And I imagine that will go up a bit after convenience fees or whatever."
    s "And you’re able to afford that?"

    scene chinamisphone6
    with dissolve

    c "I don’t really have a choice. It’s either fork over another 4,000 yen or leave my sister high and dry in the event of an emergency."
    s "..."
    c "...What? Why are you looking at me like that?"

    "I think it’s time to activate good-person mode for the week."
    "I figure I might as well get my one good deed out of the way while I have the chance to."

    s "Chika."
    c "Sensei."
    s "Let me pay your phone bill from now on."

    scene chinamisphone8
    with dissolve

    c "What?! Absolutely not. There’s no way I could let you do something like that."
    s "Why not? I make significantly more money than you."
    c "Well, duh. You’re a teacher and I’m a [teenage]girl working at the mall."
    c "But that doesn’t mean you should be friggin’ payin’ my bills for me and stuff."
    s "Just think of it as an early Christmas present or something."
    c "What kind of crazy Christmas present is a whole friggin’ phone plan?"
    chd "Chinami likes this idea! "

    scene chinamisphone9
    with dissolve

    c "Chinami, you stay out of this. This is between me and Sensei."
    chd "Woof!"

    scene chinamisphone10
    with dissolve

    "Chinami barks and sends Chika into emotional overload as she shows a rare moment of defeat, taking a deep breath as she closes her eyes."

    c "Listen...I’m flattered that you would even offer something like that...But this is {i}my{/i} problem."
    c "And besides, I’m already paying for half of Yumi’s bill as well. She’s on my plan, too."
    c "Yeah, an extra 4,000 yen a month is kind of rough for me, but I’ll figure something out."
    s "Why are you even trying to argue this? I’ve already made my decision."

    scene chinamisphone11
    with dissolve

    c "Your decision sucks. And it’ll make me feel like, a trillion times worse about everything."
    c "There’s literally nothing I’d be able to do to pay you back."
    s "You don’t need to pay me back. I wouldn’t be offering this if I didn’t want to do it."

    "Plus...there’s absolutely no way I could put Chinami in a situation like that. "
    "If she’s going to be alone, I’d be a lot more comfortable knowing she has a reliable service plan."

    scene chinamisphone12
    with dissolve

    c "Sensei...It’s fine. Really. I’ll figure it out."
    s "I’ve already figured it out. I’ll pay for you, Chinami, {i}and{/i} Yumi."
    s "I’m already paying for Ami’s bill. A few more won’t make much of a difference to me, but it’s a world of difference to you."
    s "Use that money to buy more food or something. You guys deserve it."

    scene chinamisphone13
    with dissolve

    c "Stop trying to be so cool in front of my little sister."
    s "I’m trying to be cool in front of you, too, you know."
    c "I already think you’re really cool, though."
    s "But I bet you think I’m even cooler now, right?"
    c "I don’t know. What do you think?"
    chd "Chinami thinks she doesn’t care who pays! She just wants a phone!"
    c "Quiet, Chinami. "
    chd "Woof!"

    scene chinamisphone14
    with dissolve

    c "You’re really okay with doing something like this for me?"
    s "Of course."
    c "And you’re not gonna try and extort me for something or whatever, right?"
    s "Uhh...That wasn’t something I was planning on, no."
    c "And Yumi, too?"
    s "Yumi, too."
    s "It would probably be best not to tell her about it, though."
    s "I feel like she’d throw her phone into the river if she found out I was the one paying for it."

    scene chinamisphone15
    with dissolve

    c "That’s sad because it’s true. "
    s "It really is..."

    scene chinamisphone16
    with dissolve

    c "Heheh..."
    c "Chinami, can you cover your ears for a second?"

    scene chinamisphone17
    with dissolve

    chd "Chinami isn’t sure if this will do anything, but she will listen to her sister!"
    c "Good girl, Chinami. "
    chd "Woof!"
    c "Sensei. Can you come here for a sec?"

    scene chinamisphone18
    with dissolve

    s "What’s up?"
    c "Are you really sure you’re okay with this?"
    s "Of course."
    c "And you don’t expect anything in return?"
    s "Nope. Just doing my good deed for the week. "
    c "I think a deed this good counts for the whole year."
    s "That’s even better. It means I can go back to being an asshole again after this."
    c "Hahaha, yeah, I guess it does."
    s "So, I’m assuming the store right behind you is the one where-"

    scene chinamisphone19
    with dissolve

    c "Oh! Umm, one more thing."
    s "What is it?"

    scene chinamisphone20
    with dissolve

    c "Are we like, allowed to kiss in public yet? Or is that still a no-go? "
    c "Cause I kinda wanna squeeze the life out of you right now and stuff."

    "I take a quick look around the mall to find that it’s actually rather busy today."

    if bonus == True:
        "And apart from Chika being my student, there’s still a considerable age gap between us."
        "I can’t imagine something like kissing her in broad daylight {i}not{/i} attracting attention to us, so..."

    s "I don’t think we should just yet..."

    scene chinamisphone21
    with dissolve

    c "Yeeeeah, I figured as much."

    if bonus == True:
        c "I’ll just have to make it up to you some other time then, huh?"
        s "The whole sticking your tongue out thing makes that seem pretty suggestive, Chika."

    scene chinamisphone22
    with dissolve

    if bonus == True:
        c "Oh? Does it?"
        c "Maybe I should be a little more careful with my expressions then?"
        c "I wouldn’t want you thinking I’m {i}suggesting{/i} something."

    chd "Chinami’s arms are getting tired. Can we buy her a phone now?"
    c "..."
    s "..."
    s "Let’s continue this some other time."
    c "Heheh...sure~"

    scene black
    with dissolve

    "The three of us enter the cell-phone store and let Chinami pick out whichever phone she wants."
    "Fortunately, she winds up choosing an older model that isn’t extremely expensive, and after signing a few forms, she’s ready to go."
    "Chika hugs me from behind at the checkout counter while the clerk is distracted filling things out and whispers her thanks to me once again."
    "..."

    scene chinamisphone23
    with dissolve

    chd "At last! Chinami’s true power can now be unleashed!"

    "Chinami holds the key to her true power (IE: A cell phone) above her head and screams loud enough for the entire mall to hear."
    "She’s so happy that neither of us have the heart to tell her to stop, though."

    c "Remember to take good care of that, Chinami. Sensei bought it for you, so you need to be super careful to not break it."

    scene chinamisphone24
    with dissolve

    chd "Chinami will be very careful. She will protect this phone with her life."
    c "Good girl, now thank Sensei or I’m going to take it away."
    chd "Thank you Sensei! Chinami will never forget this moment! Not even when you become her new daddy!"

    scene chinamisphone25
    with dissolve

    c "Hey, Chinami! No one is becoming anyone’s new daddy!"
    chd "What is Chinami’s phone number? She wants to make her first friend."

    scene chinamisphone26
    with dissolve

    c "Hm? You can’t give your number to Sensei, Chinami. He’s-"
    s "I don’t mind."

    scene chinamisphone27
    with dissolve

    c "Wait, what? I don’t even have your number yet and you’re going to give it to my little sister? She doesn’t even know how to use a phone yet."
    chd "Lies. Chinami has destroyed many pigs in the bird-game. She is a master of the phone."
    s "Give me your number then. And besides, wouldn’t it be good for me to have Chinami’s number in case there’s ever some sort of emergency?"
    c "Well, yeah but...It still seems kind of weird. "
    s "It’s not weird at all, I promise."

    scene chinamisphone28
    with dissolve

    c "Well...if you insist...I guess there's no fighting it."
    c "I’m more than happy to give you my number, at the very least..."

    scene black
    with dissolve

    "Chika walks over to me and swipes my phone out of my hand, entering hers and Chinami’s phone numbers into it with lightning-quick speed."
    "I expected no less from the cell-phone goddess of Kumon-mi."
    "Chika hands my phone back to me and I find that she’s added a heart next to it and..."
    "And a dog emoji next to Chinami’s..."

    $ renpy.end_replay()
    $ chikanumber = True
    $ chinaminumber = True
    $ chika_love += 1
    $ mall20 = True
    stop music fadeout 7.0

    "{i}Congratulations! You now have the phone numbers of the Chosokabe sisters!{/i}"
    "{i}Feel free to call them after[school] and on weekends to see what they’re up to!{/i}"
    "{i}Chika's affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chikainvite1:
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "I’ve been thinking lately that it might be safe for her to come visit the house soon."

    if bonus == True:
        "Obviously, Ami might show some opposition to it, but would she really be skeptical of something going on between {i}Chika{/i} and me?"
        "Now that I think of it, I can’t even remember any situations where the two of them have talked to one another."
        "And that’s not to say I don’t think they’d get along or anything."
        "It’s just...a strange combination."
        "Ami probably doesn’t even realize that Chika and I are on {i}good terms{/i} with each other."

    if invitetip == False:
        call invitetip from _call_invitetip_1

    scene noonsky
    with dissolve
    play music "normalday.mp3"
    play sound "phonebeep.wav"

    c "Hihi~ What’s up, Sensei?"
    s "Hey. Do you have any plans tonight?"
    c "Tonight? Not really. I’m just hanging out in the dorm right now."
    c "Yumi’s with Chinami so I’ve got the night to myself."
    c "Which means I’m totally free if you wanna come over~"
    s "Actually, how would {i}you{/i} feel about coming over to my place?"

    if bonus == False:
        c "Do you have a chandelier?"
        s "No."
        c "Okay, good."
        s "What?"
        c "I just wanted to make sure."
    else:
        c "Ooooooh kinky~"
        s "Not like that. I think Ami is home."
        c "More kinky~"
        c "Wait, isn’t she your [niece]? That’s kind of fucked up."
        s "I’m not suggesting a threesome..."

        "Yet."

        s "I’m just saying come over and hang out. We can tell Ami you need to catch up on[school]-work you’ve missed from taking so many “bathroom” breaks."
        c "It’s too loud in class to watch all of my idol interviews and viral videos! Where else am I going to do it?!"

    s "Are you coming over or not?"
    c "Of course I am! "
    c "But isn’t Ami a little smarter than you’re letting on? Are you sure she won’t get the wrong idea or whatever?"
    s "I can’t even mention another girl without her getting the wrong idea, so she probably will."
    s "But maybe if we just act really casual about it, she won’t even notice?"
    c "Seems like wishful thinking to me...but I’m up for a little risk! I like her anyway."
    s "I didn’t realize you two were friends."
    c "We’re not."
    c "Yet!"
    c "See ya, Sensei~ Text me your address!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Chika hangs up the phone and I type out my address to her. "
    "I decide to give Ami a warning as well so that, if Chika manages to somehow get ready and make it to my place before me, she isn’t entirely too surprised."
    "........."
    "......"
    "..."

    scene chikafirstvisit1
    with dissolve

    a "Umm...would you mind explaining to me why both you {i}and{/i} Chika texted me about her coming over tonight?..."
    s "She texted you as well? I didn’t tell her to do that."
    a "She must have thought it was weird that her {i}teacher{/i} was inviting her to his house."
    s "Do you also think it’s weird, Ami?"

    scene chikafirstvisit2
    with dissolve

    a "Of course I do! You have me!"
    a "And why Chika of all people?!"
    s "You don’t have a problem with her, do you?"

    scene chikafirstvisit3
    with dissolve

    a "Well...no."
    a "She’s really nice and...popular and...pretty much everyone likes her now that I think about it."
    a "I just don’t understand why she’s coming to our house all of a sudden. I didn’t even know you two knew each other."
    s "Of course we know each other. She’s in the class."
    s "I could invite over pretty much anyone from there and it wouldn’t be {i}completely{/i} random."

    scene chikafirstvisit4
    with dissolve

    a "I don’t recall giving you permission to start inviting all of the other girls over, Sensei. "
    a "I don’t like this at all. Cancel your plans."

    play sound "doorbell.mp3"

    "The doorbell suddenly rings."

    a "..."
    s "Damn. If only you would have told me to cancel them a few minutes earlier."
    s "It would be rude to turn her away after she came all the way here, wouldn’t it?"
    a "I’ll tell her if you don’t want to."
    s "No need. Come on in, Chika!"

    "I ignore Ami’s suggestion and shout at the door to let Chika know that it’s [[mostly] safe for her to enter."

    play sound "dooropen.mp3"
    scene chikafirstvisit5
    with dissolve

    c "Hey! Long time, no see!"
    a "Yeah...hey."
    a "Thanks for...letting me know you were coming over? I think?"
    c "Well it would obvs be pretty weird if I were to just come over and hang out with your [uncle] without you at least knowing about it."
    c "But rest assured, I’m here for you just as much as I am for him."
    a "You are?"
    s "You are?..."

    scene chikafirstvisit6
    with dissolve

    c "Obviously! "
    c "Ami lives here too, so we’ve gotta include her in any conversation that you and I have together or she’ll get all dejected and left out and stuff."
    c "I appreciate all you do for me as a teacher, Sensei, but I don’t really think I’m comfortable being alone with you just yet."
    c "Not saying you think about me that way or anything, but you know what I mean."

    "Jesus. Someone give this girl an Oscar. "

    a "Hmm..."
    a "I was skeptical at first...but when she puts it like that, maybe this isn’t as weird as I thought?"
    a "Chika's obviously out of your league anyway. So I don’t know what I was even worried about in the first place."
    s "Wait, what?"

    scene chikafirstvisit7
    with dissolve

    c "Aww come on...don’t flatter me like that. I don’t even have a league."
    c "I’m just regular old Chika. "
    a "Don’t be so humble. You’re out of everyone’s league."
    a "You shouldn’t even waste your time talking to someone like Sensei when there are zillions of other boys who’d be much better for you."
    a "Well, at least there were until the space war. I guess your options are a bit more limited now."
    a "Still better than Sensei, though."
    s "You do realize I’m right here, don’t you?"

    scene chikafirstvisit8
    with dissolve

    a "Of course!"

    "Chika flashes me a look that seems to be a cross of “I’m so sorry” and “There’s no way I agree with her,” but the looming thought of being underappreciated by my very own [niece] eats away at me."

    scene chikafirstvisit9
    with dissolve

    c "So...now what?"
    a "Yes, now what?"
    a "Since I’m apparently needed in order for this little hang-out session, may I offer a suggestion?"
    s "Sure. Even though you just insulted me in front of a guest."

    "It’s not like I had a plan in mind for this evening anyway. I’m just glad I was able to get Chika inside without much resistance."
    "But I guess that’s one of the benefits to her being liked by pretty much everyone."
    "And also apparently one of the bright sides to being “out of her league...”"

    a "How about we show Chika the best part of our house?"

    if bonus == True:
        s "You mean my bed?"
    else:
        s "The chandelier?"
        c "You lied to me."

    scene chikafirstvisit10
    with dissolve

    if bonus == True:
        a "No! I don’t mean your stupid bed!"
    else:
        a "No! Not the chandelier!"

    a "I mean our TV! The one that we watch movies on all the time!"

    if bonus == True:
        s "I like my bed a little more than the TV."
        a "You’re not showing Chika your bed!"
        c "Hahaha...I’m...fine with TV..."
        c "My legs are kind of tired from walking all the way here and whatnot anyway."
    else:
        s "Oh, that."
        c "Thank God."

    scene black
    with dissolve

    "Ami shoots me one final death glare before moving to the living room and taking her place on the couch."
    "Chika sits on the opposite end, leaving the space in the middle completely unoccupied."
    "Before Ami is able to slide over and prevent me from sitting directly next to Chika, I manage to find my place between the two of them."

    scene chikafirstvisit11
    with dissolve

    c "Wow! This is so much bigger than the one at my place!"
    c "You can even hear it without having to turn the volume all the way up!"
    a "The glories of surround-sound."
    c "I thought surround-sound was something only rich people could afford."

    scene chikafirstvisit12
    with dissolve

    c "Are you guys really that well off, Sensei?"
    s "Not particularly. I don’t even remember what all of this cost us."

    "Mostly due to the fact that I’m not technically the one who paid for everything."
    "Well, I guess...technically, I {i}am{/i}."
    "But a different...me. Or something."
    "Wait, why am I thinking about the cost of our entertainment set-up when I’m sandwiched between two cute [teenager]s?"

    a "Sensei and I used to spend almost every day on this couch."
    a "But now that I’m getting older, he’s losing interest in me and inviting other girls over to the house instead."
    c "You need to cherish your family, Sensei. You never know when something bad might happen to them."

    scene chikafirstvisit13
    with dissolve

    a "Listen to your guest, Sensei. Cherish me more! Buy me things!"
    s "Who invited you here, Ami?"
    a "Chika did! You’re not insinuating that {i}your{/i} guest might have made some sort of mistake, are you?"
    s "That’s exactly what I’m insinuating. Go to your room."

    scene chikafirstvisit14
    with dissolve

    a "Mmm!"
    c "Now, now...I didn’t mean to stir up any trouble between you two. I just think things like this are more fun when everyone can enjoy them together."

    scene chikafirstvisit15
    with dissolve

    c "I kind of wish my little sister could be here to experience this today."

    "The wording of that sentence makes it sound as if Chinami is dead. What a horrible thought."

    c "The only family I really have left is her and Yumi."

    "Chinami lives again. What a joyous occasion."

    a "My only family is Sensei, so I can relate to that..."
    a "I didn’t know you had a sister, Chika. All this time I thought you were an only child."
    c "Two sisters if you count Yumi. "
    c "She’s independent, but I feel like she’s even more of a kid than my actual little sister at times."
    s "If Chinami ever starts talking like Yumi, though, I’m never coming over again."

    scene chikafirstvisit16
    with dissolve

    a "Wait! Coming over?!"
    a "You’ve been to Chika’s house?!"
    a "You met her sister?!"
    a "What else are you hiding from me, bastard-[uncle]?!"
    c "Ah- Nononononono, you’ve got it all wrong! Sensei’s never come to my house before."
    c "He meant...coming to the mall! The store I work at! I bring my sister with me sometimes when I can’t find a babysitter!"

    scene chikafirstvisit17
    with dissolve

    a "Wait just a second..."
    a "Little sister..."
    a "Mall..."
    a "Does she perhaps...wear a funny-looking...dog mask?"
    c "Hahaha...yeah...that’s...a thing she does..."
    s "I was beginning to think you were never going to bring up that incident."
    a "Up until now, I’d been pretending it was all some strange delusion due to lack of sleep."
    a "Something about this story doesn’t add up, though."
    c "What?...What could possibly not add up about...this?..."

    scene chikafirstvisit18
    with dissolve

    a "If you two don’t normally spend time alone together...why are you going to visit her at the mall?"
    a "And why are you watching her little sister while she works?"
    a "Just how close are you two?"
    c "Umm...uhh..."
    s "I have a passion for luxury clothing."

    scene chikafirstvisit19
    with dissolve

    c "Y-Yes! That’s exactly it!"
    c "Sensei is a regular customer! The only times I ever see him are at[school] and work, though..."
    c "He’s never invited me to the house before, so I wouldn’t have really felt comfortable unless you were here as well, Ami!"
    a "If you’re so passionate about luxury clothes, how come you wear that same stupid blazer every day?"
    s "Stupid?"
    c "He’s...saving up money to take you on a trip!"

    scene chikafirstvisit20
    with dissolve

    a "A trip? Really? "
    a "Where are we going?"
    s "..."
    c "The...moon!"
    a "We’re going to...the moon?"
    s "..."
    s "Yes."

    "Really, Chika? The moon?"
    "Couldn’t you have at least named somewhere on this planet?"
    "How much money am I going to need to save up now?"
    "I can feel my fake passion for luxury clothing diminishing by the moment."

    a "I...don’t know if I want to go to the moon, though."
    a "That seems like it would take a really long time."
    s "Damn. I guess I’ll need to cancel our plans then."

    scene chikafirstvisit21
    with dissolve

    a "Well...I mean...I {i}would{/i} get to be alone with you...so maybe it wouldn’t be all that bad in the end."
    s "Too late. I’ve already cancelled the trip."

    scene chikafirstvisit22
    with dissolve

    a "What?! Already?! But I changed my mind!"
    a "I want to go to the moon!"
    c "Hahaha...hahah..."
    c "Hah..."

    scene chikafirstvisit23
    with dissolve

    a "Mmm..."
    s "..."
    c "..."
    s "{i}The moon? Really?{/i}"
    c "{i}It was all I could think of on such short notice.{/i}"
    s "{i}How were you so good at lying up until that part?{/i}"
    c "{i}I had a script in my head. The trip part was all improv.{/i}"
    s "{i}Was it really? I had absolutely no idea.{/i}"

    if bonus == True:
        scene chikafirstvisit24
        with dissolve

        c "{i}I’ll make it up to you...kay?{/i}"
        c "{i}Invite me over again when Ami isn’t home and you’ll see~{/i}"

    scene chikafirstvisit25
    with dissolve

    a "Hey...what are you two whispering about over there?"
    c "W-Whispering? No one’s whispering! We were sitting here in silence!"
    s "I think we need to take you to a psychiatrist, Ami. You appear to be hearing things."
    a "No! You appear to be {i}hiding{/i} things!"
    a "Tell me what you were whispering about!"

    scene black
    with dissolve2

    "Obviously, we never tell Ami what we were whispering about."
    "It takes her roughly fifteen minutes to give up on asking."
    "Within that time, Chika and I mutually decide that it might be best if she heads back to the dorm early today."
    "I feel a little bad for having her come all the way here just to leave shortly after, but I guess things like that can’t be avoided at times."
    "I’ll just need to make sure Ami isn’t around the next time I invite Chika over so we don’t have to go through something like this again..."

    $ renpy.end_replay()
    $ chikainvite1 = True
    $ chika_love += 3
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label chikainvite2:
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "Ami told me earlier in the day that she’d be hanging out at the dorm with some of the other girls tonight so, assuming Chika isn’t one of them, the two of us might actually be able to be alone for a while."

    play sound "phonebeep.wav"
    scene noonsky
    with dissolve

    c "Hihi~ Chika’s phone, this is Chika speaking!"
    s "Strange way to answer the phone but hey."
    c "Hey~"
    c "I miss you."
    s "You could always text me if you miss me, you know. You’re always on your phone anyway."
    c "I need to restrain myself or you’ll think I’m needy."
    s "I wouldn’t really care either way."
    c "Then can I come bother you at your house tonight? I just saw Ami and some of the others down the hall, so you should be alone, right?"
    s "Funny you mention that because that’s actually why I was calling."
    c "Well I’m glad we’re on the same page!"
    c "Should I head over now?"
    s "Sure. You remember how to get there, right?"
    c "Obvs. I still have your message with your address in it anyway. "
    c "I’ll be there soon!"
    s "Cool. See you then."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "I hang up the phone and slide it back into my pocket, only to have it vibrate seconds later."
    "When I pull it back out to check again, all I see is a heart emoji sent by none other than Chika Chosokabe."
    "........."
    "......"
    play sound "doorbell.mp3"
    "..."

    scene chikasecondvisit1
    with dissolve
    play music "asobeatsex5.mp3" fadein 8.0

    "Chika walks in when I give her the go-ahead and kicks her heels off at the door before skipping her way over to me."

    c "You have no idea how glad I am to not have to act this time."
    c "Ami’s cute, but that girl’s a friggin’ hawk when it comes to you."
    c "I felt like she was analyzing every single thing I said to try and frame me somehow or another."
    s "Probably because she was. She tends to do that."
    c "Guess I can’t blame her for being a little overprotective of her super-cool [uncle]."

    scene chikasecondvisit2
    with dissolve

    c "I’ve got ya all to myself this time, though. So here’s hoping we can make it at least a few hours without being interrupted."
    s "I have a feeling Ami will be gone for quite some time, so I wouldn’t worry too much about any interruptions."
    c "Heheh~ Good."

    scene chikasecondvisit3
    with dissolve

    c "It’s like...a completely different feeling being alone in here with you. I feel...weirdly special all of a sudden."
    s "Do I not normally make you feel special?"
    c "I never said that. You make me feel special all the time. This just feels a lot more...real."

    if bonus == True:
        c "Like we’ve taken it a step further than just messing around in my dorm and stuff."

    scene chikasecondvisit4
    with dissolve

    c "I almost want to suggest that the two of us just hang out and cuddle or something but I’m pretty sure I already hinted something a little special to make up for my last visit."

    if bonus == False:
        s "I hope it is a hug."

    c "It would be quite rude to only cuddle when you’re probably expecting me to go the extra mile, right?"

    if bonus == False:
        s "No. That would be great, actually."
    else:
        s "Wow, it’s almost like you understand me or something."

    scene chikasecondvisit5
    with dissolve

    c "I live to please~"
    c "Besides, I’m excited too. My heart was racing the whole way here."
    c "And now that we’re alone, I kinda just want to squeeze you until you explode. Is that weird?"

    if bonus == True:
        s "I can’t tell if you mean literally squeezing me or if that was a euphemism for jerking me off."
        c "Would the answer to that change your response?"
        s "Uhh, kind of. Yeah."
        c "I meant literally squeezing {i}you{/i} but I guess I’d also be okay with jerking you off if that’s what you want."
        c "Unless you maybe want me to do something else this time?~"
        s "What else did you have in mind? I’m open to suggestions."

        jump chikasecondinvx
    else:
        s "No. Begin the hugging."

        scene black
        with dissolve

        "Chika and I hug for a really long time."
        "She is pretty good at it, but I think I'm a little better."

        $ renpy.end_replay()
        $ chikainvite2 = True
        $ chika_lust += 3
        stop music fadeout 5.0

        "{i}Chika’s lust has increased to [chika_lust]!{/i}"
        "{i}You can now choose between affection and hugs when inviting her over!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label chikainviteaff:
    if halloweenfive17 == True:
        scene chikainvitegen2
        with fade
    else:
        scene chikainvitegen
        with fade

    "Chika and I spend the night eating junk food and asking each other questions about things we'd like to know about one another."
    "She has a lot more questions than I do."
    "Real questions. Big ones...like 'What did you want to be when you grew up' or 'Do you ever want to get married?'"
    "I have a hard time finding answers to all of them, to be honest."
    "But even when that happens, it doesn't faze her one bit."
    "In between the barrage of questions, she wastes no time in reaching her feet out underneath the table and playfully poking and kicking me with them."
    "She smiles the entire night. Even when nothing is happening."
    "I wish I could do that."
    "I have a hard enough time smiling even when good things happen."

    scene black
    with dissolve

    "If I was any good at smiling, I'd smile back at her."
    "But, being the person I am, I sit back and let her continue to play one-sided footsie with me as I finish off the last of the french fries on the table."
    "Eventually, Chika moves to my side and rests her head on my shoulder."
    "She tells me about her dreams. How {i}she{/i} wants to get married."
    "And how some day, in the distant future, she'd like to eat junk food and play question-games with someone who will look only at her."
    "She smiles one last time."
    "And then she leaves."

    $ chika_love += 3
    stop music fadeout 5.0

    "{i}Chika's affection has increased to [chika_love]!{/i}"

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

label chikainvitelicking:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump chikainvitelickingx
    else:
        $ chika_lust += 3
        stop music fadeout 5.0

        "{i}Chika's lust has increased to [chika_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label chikainvitehandjob:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump chikainvitehandjobx
    else:
        $ chika_lust += 3
        stop music fadeout 5.0

        "{i}Chika's lust has increased to [chika_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label day272:
    scene chikaonseninv1
    with fade
    play music "normalday.mp3"

    c "Oh, hey! Fancy meeting you here!"
    c "Do...um...do you have a sec?"

    "I wind up running into Chika between classes."
    "And by “running into” I mean that I’m pretty sure she’s been following me around every time I leave the classroom today."

    s "Depends. "
    s "Are you trying to extort me?"
    c "What...would I be trying to extort you for?"
    s "I don't know. But you’ve been following me around all day, haven’t you?"
    s "What’s going on?"

    scene chikaonseninv2
    with dissolve

    c "Not all day! Just like, three times!"
    s "Spit it out, Chika. I am a very busy man."
    c "I...um..."

    scene chikaonseninv3
    with dissolve

    c "I wanted to show you these..."
    s "Cool."
    s "What are they?"
    c "I umm..."
    c "So, there’s this radio show I listen to with Chinami in the morning...and they were doing this thing where the 23rd caller wins a prize..."
    c "Sooo...I somehow wound up winning two tickets to some like, super nice hot spring at the edge of town."

    scene chikaonseninv4
    with dissolve

    c "Would you...you know..."
    c "Wanna come with me?"
    s "Me? You don’t want to take Yumi or Chinami?"
    c "I’d rather go with you..."
    c "But if you think it’s weird to go on a random one night vacation with a cute girl who follows you around in the hallway, that’s fine. "
    c "I’ll just go cry in the bathroom."
    s "Of course I’ll go."

    scene chikaonseninv5
    with dissolve

    c "Really?! You will?!"
    s "Sure. Why would I say no to a free vacation with a cute girl?"

    scene chikaonseninv6
    with dissolve

    c "I don’t know. Cause it’s like, super random and the middle of winter?"
    s "The middle of the winter is the best time to go to a hot spring."
    s "When are we supposed to be there?"
    c "The tickets don’t have an expiration date so we can kinda just go whenever we want I guess."
    c "Just call me in the morning whenever you’re ready and I’ll find someone to cover my shift or something."
    s "Is that really okay?"

    scene chikaonseninv7
    with dissolve

    c "Probably not, but I’m a [teenage]girl and I’m sure they'll understand if it’s for a trip with my boyfriend."

    scene chikaonseninv8
    with hpunch

    c "Ah! Forget I said that! I didn’t just call you what you think I called you!"
    s "..."
    c "I’m gonna go!"
    c "Umm...call me!"

    scene chikaonseninv9
    with dissolve

    "Chika darts down the hallway and I now have to figure out if being called her boyfriend is potentially troublesome or not."
    "But hey, at least I get to spend a whole day off with her soon. "
    "And I don’t even have to pay."

    $ onseninvite = True
    $ onsenticket = True

    "{i}Congratulations! You can now go on a special trip with Chika!{/i}"
    "{i}Things like this might happen every once in a while because you’re a super awesome, super likable guy who lights up the room just by walking in.{/i}"
    "{i}To go on this trip, call Chika in the morning.{/i}"
    "{i}But, before that, you might want to pay her roommate a visit.{/i}"

    scene black
    with dissolve
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    jump afterschoolevent

label chikaonsen1:
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "Now that I know Yumi’s going to be watching Chinami, I feel a little less bad about stealing Chika away for a night."
    "And given how excited she was for the prospect of spending some time alone with me, I’m sure she’ll be ready to go as soon as I give the word."
    "In fact, she’d probably ditch work even if she was on the clock right now."
    "Not that I want her to do that or anything."
    "But...it would be kind of nice, I guess."
    "It’s a good feeling having so many lives that revolve around yours."

    play sound "phonebeep.wav"

    c "Hihi~ Good morning, Sensei."
    s "Morning. Are you busy today?"
    c "I’m actually off today! "
    s "Really? Don’t you work every weekend, though?"
    c "Yup! But I had a feeling that today was gonna be {i}that{/i} day, you know?"
    s "...Your period?"
    c "What? No. I meant the day you invite me out."

    "Thank God."

    c "So, are you ready to go?"

    "{i}Saying “Yes” will trigger a four part event that will last until Sunday morning.{/i}"
    "{i}Are you absolutely sure you’re ready to go?{/i}"

    menu:
        "Yes":
            play music "acoustic.mp3"

            s "Let’s do it. Start packing now."
            c "Heheh~ It’s only one night. It’s not like I need to bring all of my stuff."
            c "I’ll just grab my charger and some underwear and start heading over to your place. Is that okay?"
            s "You’re coming here?"
            c "Duh. Unless you want to stop by here. But that’s like, totally out of the way since there’s a bus stop right around the corner from your place."
            s "True. Alright, sure."
            s "Let me know when you’re here."
            c "Yup! See you soon, Sensei!"

            play sound "phonebeep.wav"

            "Chika hangs up and I take a seat on the bed, wondering what a one-night vacation with her will wind up being like."

            scene black
            with dissolve

            "........."
            "......"
            "..."

            jump onsenbegin

        "No":
            s "Actually...on second thought, maybe we should wait a little bit?"
            c "What? How come?"
            s "I’m pretty sure Ami and I already have plans tonight. "
            c "Ugh...stupid Ami."

            "Living with a [niece] shows off its convenience once again."

            c "Fine...but only because I like you so much."
            c "You’re lucky you have a girl like me, you know? Not many people would offer up a chance like this just to let you do whatever you want with it."
            s "Yeah, yeah. I’m glad that you exist."
            s "I’ve gotta go, though. Enjoy your day off, Chika."
            c "Guhhhh...Maybe someone will let me take one of their shifts or something now that I know I’m not busy?"

            play sound "phonebeep.wav"

            "The two of us hang up and I suddenly have to figure out something else to do today."

            $ renpy.end_replay()
            jump callmorning

label onsenbegin:
    scene wintersky
    with dissolve

    "Chika shows up around an hour later with only one bag."
    "I know she mentioned not needing much but, for some reason, I expected her to be the type to pack her entire closet away for even a short trip."
    "The two of us make our way to the bus station and decide to remain standing so as to not freeze ourselves against the cold steel of the bench."
    "She tells me a little more about the hot spring. How it’s not really a place someone like her could ever afford without little miracles like this."
    "The fact that she refers to it as a “miracle” is actually quite humbling."
    "I never thought of myself as the type to be involved in anything miraculous, let alone a miracle with a girl that is far too good for me by every stretch of the word."
    "I guess that applies to most of the girls I hang around, though."
    "But I probably shouldn’t be thinking of any of them right now."
    "If Chika’s going to be kind enough to use something like this on me instead of someone else she's close with, the least I can do is give her my undivided attention."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene firstonsen1
    with dissolve

    c "Soooo...you like?"

    "We arrive at the onsen half an hour later and receive yukata to change into."
    "I shrug mine off because I’m too stoic and manly to ever be seen in something like that, but Chika happily accepts hers and scurries off to a changing room to put it on right away."
    "And now...here we are."
    "In a completely unfamiliar environment, face to face with one another and-"

    s "You are adorable."

    scene firstonsen2
    with dissolve

    c "Heheh~ Thanks!"
    c "I haven’t worn one of these in ages. I’m surprised I even remembered how to put it on."

    if bonus == True:
        s "I hope it is equally as easy to take off."
    else:
        s "I am surprised as well. Your hippocampus must be very impressive."

    scene firstonsen3
    with dissolve

    c "[chikamaster]...we’ve only been here for five minutes and you’re already trying to rile me up?"

    if bonus == True:
        c "What if I wanted this to be a completely wholesome weekend without any of those {i}extra-curricular{/i} activities you’ve started having me do?"
        s "I’d say that you should probably put on normal clothes because it is hard to not get excited right now."
        c "Just don’t get {i}too{/i} excited or someone’s bound to notice."
    else:
        s "Of course not. I just want to hold your brain for a little while and see what it feels like."

    scene firstonsen4
    with dissolve

    c "Why aren’t you wearing yours, by the way? Isn’t that like, disrespectful or something?"
    s "I’ll be fine. I don’t think I’d look normal in one of those."
    c "Really? I think you’d look hot."
    s "Thanks. But I’ll stick to my normal clothes for-"

    scene firstonsen5
    with dissolve

    q "Get out of here, peasant!"
    q "This hot spring belongs to me!"
    q "Do yourselves a favor and run off before I call security!"
    c "But...we have tickets."
    s "You look a little [young]to be the owner of an onsen."

    scene firstonsen6
    with dissolve

    tk "Silence! I am Tsukasa Tsukioka of the Tsukioka family! A very powerful, 5,000 year old wizard!"

    "Tsukioka? Why does that name sound familiar?"

    tk "I own many hot springs! Now, be gone!"
    s "Another wizard."
    c "Just like Chinami..."

    scene firstonsen7
    with dissolve

    q "Tsukasa, dear..."
    tk "Yes, mother?"
    tk "I was just informing this lovely [young]couple of the amenities this facility has to offer."
    q "Oh?"
    q "So I {i}didn’t{/i} just hear you talking about being a wizard again?"
    tk "Whatever do you mean, Mother? Why would I ever say something as silly as that?"

    scene firstonsen8
    with dissolve

    q "Hah...please forgive my daughter."
    q "It’s not often that she gets to converse with those outside of the manor, so she gets a little excited at times."
    c "Oh, yeah. It’s fine. I have a sister her age, so I kinda get what you mean."
    c "I’m Chika. Are you two actually the owners of this place? It’s absolutely beautiful so far."
    c "I mean...we still haven’t made it out of the entrance. But it was suuuuper nice on the outside."

    scene firstonsen9
    with dissolve

    q "Oh dear, pardon my manners."
    tb "I'm Tsubasa. And I assume you’ve already heard my family name from my daughter here."
    tb "We {i}do{/i} own this building, but we’re not here very often."
    tb "We just happen to be on a little retreat right now as my husband renovates our own hot spring."
    tb "I have another daughter who was supposed to be joining us, but it seems she had other matters to attend to this evening."
    tk "How disappointing Big Sister can be at times."
    tk "Does she not understand that a place like this is a truly splendid environment for mothers and daughters to bond?"

    scene firstonsen10
    with dissolve

    c "You love your mom a lot, huh?"
    tk "She is perfectly adequate. Though, I do wish she’d allow me a bit more freedom like Papa does."
    tb "And you are?"
    s "You can just call me Sensei."
    tb "Oh? You’re a teacher? Kumon-mi Academy or [kumon_mi_high]?"
    s "Uhh..."
    s "Chika, which one is ours again?"

    scene firstonsen11
    with dissolve

    c "[kumon_mi_high], Sensei."
    s "Sorry. The names are so similar that I wind up confusing them pretty frequently."
    tb "That’s hilarious. Do you enjoy teaching there?"
    tb "My oldest daughter attends Kumon-mi Academy, but I can’t say I’m exactly pleased with their...performance so far."
    s "Yeah. Crazy how they’d do something as outside of the curriculum as falling into a sinkhole."

    scene firstonsen12
    with dissolve

    tb "Hahahahah! Hilarious!"
    tb "I forgot how funny people could be outside of the manor!"
    tk "Mother? Papa told us not to laugh at commoners because it’s rude."

    scene firstonsen13
    with dissolve

    tb "I’m not laughing {i}at{/i} them, Tsukasa dear. I’m laughing because Sensei said something funny."
    tb "Now, come with me and leave these two alone. I’m sure they didn’t come all the way here to converse with a little girl and an old woman."
    s "You’re not old. You look the same age as me."

    scene firstonsen14
    with dissolve

    if bonus == True:
        tb "Apologies, again. I meant {i}older{/i} than your...tastes, given the lovely [young_girl] you’ve shown up with."
    else:
        tb "Why, how kind of you. I will be sure to remember that when my events are obtainable."

    tb "Now, please do excuse us."

    scene firstonsen15
    with dissolve

    tk "Bye bye, peasant man!"
    tk "Do enjoy your stay at Casa del Tsukasa!"
    tb "Good day to both of you."

    scene firstonsen16
    with dissolve

    "The two rich girls wander into what looks like a sauna and leave Chika and I to ourselves in the entryway again."

    c "That was...umm...interesting."
    c "Do you think she knows we’re like...here {i}together?{/i}"
    s "I’m fairly sure that much was obvious."
    s "I’m more surprised by how casual she was about everything."
    c "Heheh...maybe we just look {i}that{/i} good as a couple?"
    s "Yeah."
    s "I guess that must be it."

    scene black
    with dissolve

    "We turn around and begin to head toward the room we were assigned to."
    "The halls are lined with ornate lights that don’t quite match the overall Japanese theme of the place, but they definitely don’t look bad either."
    "And it seems that despite this being on the more “high class” side, there really aren’t many rooms."
    "Or people, for that matter."
    "It’s remarkably empty."
    "But I guess that just means it’ll be easier having some...”private time” in the hot spring."
    "........."
    "......"
    "..."

    scene firstonsen17
    with dissolve

    c "Woah! This place is like, totally retro!"
    c "I don’t even think there’s a TV in here!"
    s "I think the whole point of places like this is to relax and detach yourself from normal society or something."

    scene firstonsen18
    with dissolve

    c "And there’s only one futon~"
    c "It looks tiny, too. We’re probably gonna have to cuddle if we both want to fit."
    s "Oh no. What a horrible turn of events. However will we survive?"

    scene firstonsen19
    with dissolve

    c "Heheh~ I’m glad you’re just as excited as I am."
    c "This whole thing like, still hasn’t even set in for me I don’t think."
    c "Like, if I heard at the beginning of the[school] year that I’d be talking about cuddling my teacher at some high class onsen, I never would have believed it."
    s "I feel like that applies to pretty much everyone once they start [high_school]."
    s "We live in a sad world if people expect those things right away."
    c "You know what I mean."
    c "It’s just crazy how far we’ve come in such a short amount of time."
    c "Like, it doesn’t even feel like just one[school] year. You know?"
    s "Oh, I know very well."

    "Or at least better than you ever will, Chika."

    scene firstonsen20
    with dissolve

    c "Soooo...now what do we do?"
    s "Hell if I know. This is your trip."
    s "Not like there’s much {i}to{/i} do here other than like...relax or bathe."

    scene firstonsen21
    with dissolve

    c "Want to make out?"
    s "And that. That’s also a thing we can do."
    c "Is that a yes?"
    s "That’s obviously a yes."
    c "Then what are we waiting for? We’ve only got one night."
    c "We need to get as many kisses in as we possibly can, [chikamaster]~"

    scene black
    with dissolve

    "Chika grabs me by the wrist and pulls me into the bedroom."
    "She slides my blazer off and brings her hands to my chest, poking and pulling at the fabric of my shirt."

    scene firstonsen22
    with dissolve

    c "Actually, before we start, I wanna ask you something."
    c "And it’s important, so you’re not allowed to laugh at me."
    s "Can this really not wait until after we make out?"
    c "I don’t think you’ll want it to wait that long."
    s "Okay then. Color me intrigued."

    scene firstonsen23
    with dissolve

    c "Then..."

    if bonus == True:
        c "How do you feel about being my “first” tonight?"
        s "You were right. I’m glad you didn’t make me wait to hear that."
        c "You know what I’m talking about, right?"
        s "I sure hope so. If I don’t, this would be one hell of a tease."

        scene firstonsen24
        with dissolve

        c "It’s not a tease, [chikamaster]."
        c "I want to lose it tonight."
        c "This is the perfect place for a first time, isn’t it?"

        scene firstonsen25
        with dissolve

        c "I would have preferred you being in a yukata for it since I {i}do{/i} think that would be really hot..."
        c "But I wanna do it either way."
        s "Then why are we just standing here?"

        scene firstonsen26
        with dissolve

        c "Probs cause you haven’t kissed me yet."

        scene firstonsen27
        with dissolve

        "Chika presses her body against mine and immediately slides her tongue into my mouth."
        "Our hands find each other’s heads as we forcefully kiss, moving our waists closer together with every inhale and exhale."

        c "Mmn~"
        c "Mnch...mmm...hmm...[chikamaster]..."
        c "I’m so...mmnch...glad we can be...mmm...alone~"

        "I reach for her ass with my free hand and grab onto her, forcing her even closer to me."
        "She seems to like it as she bites my lip in response, moaning gently and running her fingers through my hair."

        c "[chikamaster]...[chikamaster]..."
        c "You want me...mmn...really bad...don’t you?..."

        "I bite her lip next to say yes since not everyone is as good at talking while kissing as Chika is."
        "And she must take that as a signal because-"

        scene firstonsen28
        with fade

        "She winds up pushing me to the ground and climbing on top of me just seconds later."

        c "Hah...hah...hah..."
        c "[chikamaster]..."
        c "Are you gonna make me feel good?"
        s "Hate to break it to you now of all times, but the first time probably won’t feel that great."
        c "You think you’re gonna hurt me?"
        s "I mean...yeah. Kind of."
        c "I don’t think so."
        c "I’ve got pretty high pain tolerance."
        c "And also-"
        c "I {i}really{/i}...fucking want it..."

        "I reach toward Chika’s chest to open her yukata-"

        scene firstonsen29
        with dissolve

        c "Nuh-uh-uh. Not yet, [chikamaster]."
        s "What? Why?"
        s "I am way too into this for any more foreplay right now."
        c "Who says I’m looking for any foreplay?"
        c "Maybe I just wanna watch you squirm a little bit?"
        c "Really make you work for it, you know?"
        s "Since when are you evil? You’re supposed to be the wholesome one."
        c "Hmm...maybe I just feel strong cause I’m on top right now?"
        c "Besides, I’m still totally wholesome. But there’s a time for that and that time is definitely not now."
        s "Okay, time to switch positions then."
        c "Positions or locations?"
        s "What does that even mean?"

        scene firstonsen30
        with dissolve

        c "Hmm...I think I wanna go check out the hot spring first."
        c "That is the purpose of an onsen, after all."
        c "And the bus was kinda hot on the way here, so a bath {i}does{/i} sound refreshing."
        s "Cool. Let’s go have sex in the bath."

        scene firstonsen31
        with dissolve

        c "No, no! That won’t do, [chikamaster]! The baths here aren’t co-ed."
        s "Excuse me?"
        c "But I’ll go by myself and I’ll try to be really quick, okay?"
        s "Why are you doing this to me?"

        scene firstonsen32
        with dissolve

        c "I'm sorry."
        c "I just need a few minutes to mentally prepare myself."
        c "Like yeah, I’m really fucking horny right now, but I didn’t think this was gonna happen like, {i}right away{/i}."
        s "You literally started this."

        scene firstonsen33
        with dissolve

        c "Sorry. But you were just so cute that I couldn’t help myself."
        c "I’ll be quick, okay?"
        s "Can you at least jerk me off or something first?"
        c "No way, Jose. You’ve gotta save everything up for me."
        c "And as a reward for your hard work and dedication, I’ll let you do it inside."
        s "Gee, thanks. Being blue-balled feels so much better now."

        scene firstonsen32
        with dissolve

        c "I’m really sorry...I am."
        c "But I’m not backing out."
        c "All I’m asking for is like...twenty minutes. Thirty tops."
        c "Why don’t you take a bath, too? Then we can have sex for a few hours and then take another bath and then go to sleep."
        c "Doesn’t that sound fun?"
        s "If you manage to go for a few hours without wanting to stop, I will be extremely impressed."
        c "Well, you know how much I like to impress you, so I’ll try my hardest to make that happen."

        scene firstonsen33
        with dissolve

        c "Sorry for killing your hard-on~"
        c "But think about me while I’m gone, kay?"

        scene black
        with dissolve2
        stop music fadeout 15.0

        "Chika hops off of me and happily skips out of the room, humming some upbeat pop song to herself as she goes."
        "I feel kind of betrayed for being left in this...condition."
        "But I get it."
        "This {i}is{/i} still a big moment for her after all."
        "She probably just wants to savor it."

        s "..."
        s "I guess a quick bath wouldn’t hurt..."

        "I lift myself off of the futon and make my way over to the apparent single-sex baths, wondering exactly how Chika is “preparing herself” right about now."

        $ renpy.end_replay()
        $ chikaonsen1 = True
        $ chika_love += 1

        "{i}Chika’s affection has increased to [chika_love]!{/i}"
        "........."
        "......"
        "..."

        "{i}Ten minutes later...{/i}"
    else:
        c "How do you feel about hugging me tonight?"

        scene black
        with dissolve2
        stop music fadeout 15.0

        s "Sure. That sounds like an enjoyable experience."

        "Chika hops off of me and happily skips out of the room, humming some upbeat pop song to herself as she goes."
        "I feel kind of betrayed for being left in this...condition."
        "But I get it. I also thing hugs are awesome."

        "I lift myself off of the futon and make my way over to the apparent single-sex baths, wondering exactly how Chika is “preparing herself” right about now."

        $ renpy.end_replay()
        $ chikaonsen1 = True
        $ chika_love += 1

        "{i}Chika’s affection has increased to [chika_love]!{/i}"
        "........."
        "......"
        "..."

        "{i}Ten minutes later...{/i}"

label chikaonsen2:
    if bonus == False:
        scene noonsky
        with dissolve
    else:
        scene chikaonsen1
        with dissolve2

    play music "gentle.mp3"

    "The mixture of cold air and hot water is one of the single most under appreciated sensations in the entire world."
    "Especially for a girl who so easily gets goosebumps."
    "So, there she sits, watching steam rise off the surface of the water-"
    "Counting the bumps on her arms and then submerging them until they’re gone, acutely aware of how easy it is to control certain changes in our bodies."
    "She will undergo one more dramatic shift in that regard soon."
    "Because roughly two hundred feet away from here lies a bath for the opposite sex, currently housing a man she has fallen helplessly in love with over the last several[school] years."
    "Or perhaps it’s more like hundreds."
    "Thousands, maybe?"
    "What if, by some stretch of the imagination, she’s been slowly falling in love over the course of millions of[school] years?"
    "And what if, by an even larger stretch of the imagination, this isn’t the first time at all?"
    "How many onsen tickets have there been? "
    "And what has happened on those respective visits?"
    "Can we truly surmise that this is the first of all of them?"
    "One more deviation in an incessantly deviating timeline doesn’t seem so far fetched now, does it?"
    "Please forgive me."
    "I get lost in thought during times like these."
    "I’d like to take a moment and blame it on the mixture of temperatures."
    "I don’t get goosebumps the same way this girl does, but I {i}do{/i} see the beauty in life when it so rarely shows up on a silver platter."
    "And even though the girl in front of us doesn’t see things the same way I do-"
    "She does see things."
    "She sees a world much brighter than us."
    "A world where even those who are lost in the dark are able to crawl out as long as they persist and shed a little blood."
    "Bleed, you beautiful girl."
    "Bleed and feel alive."
    "Bleed and remind yourself that you are loved-"
    "Even though everyone else you’ve ever loved has already left you."

    tb "Is this spot taken?"

    if bonus == True:
        scene chikaonsen2
        with dissolve

    c "Oh, Tsubasa! I didn’t realize you were-"

    if bonus == True:
        scene chikaonsen3
        with dissolve

    c "Woah."
    tb "Hm?"
    c "You’re uhh...pretty stacked."
    tb "Just try not to stare too much or you’ll go blind."

    if bonus == True:
        scene chikaonsen4
        with dissolve

    c "Oh, sorry! Just...took me by surprise there."
    c "You’re like, super beautiful. "
    c "Is that a weird thing to say when we're both totally naked and sitting next to each other in a hot spring?"
    tb "Not at all. In fact, I’m flattered."

    if bonus == True:
        scene chikaonsen5
        with dissolve

    tb "Unfortunately, I’m married. So I can’t exactly reciprocate your feelings, dear."
    tb "I also can’t imagine your boyfriend would be very fond of you abandoning him on your getaway for someone like me."

    if bonus == True:
        scene chikaonsen6
        with dissolve

    c "Oh, he’s not my boyfriend."
    c "Though...I did accidentally call him that in[school] the other day. Which was like, super embarrassing."
    tb "Embarrassing why? "
    tb "Are you ashamed of him for some reason?"

    if bonus == True:
        c "No, no. Not at all. But like, he’s still my teacher and there’s a pretty huge age gap between the two of us."
    else:
        c "No, no. Not at all. But like, he’s still my teacher. And also the huggy boy."

    c "So I’ve gotta try like, really really hard to not be clingy when all I wanna do is just hold his hand all day every day."

    if bonus == True:
        scene chikaonsen7
        with dissolve

    tb "Ahh, yes. Being [young]and in love."
    tb "I wish I could have experienced something like that at least once in my life."
    tb "Treasure it while you can, dear."
    tb "Before you know it, you’ll be old and raising kids...thinking to yourself, “Where did all the time go?”"

    if bonus == True:
        scene chikaonsen8
        with dissolve

    c "Wait, aren’t you married?"
    c "Do you not love your husband, Tsubasa?"
    tb "Can you keep the answer to that question a secret?"
    c "Of course. Who would I even tell?"
    tb "For all I know, you could be a spy he sent here for this exact reason. "
    tb "Though I doubt a spy would have stared so blatantly at my breasts for as long as you did."
    c "I could be a really perverted spy. You never know."
    tb "I suppose that’s true. But I also suppose that even if you are a spy, hiding the truth from you wouldn’t do much this far into life."

    if bonus == True:
        scene chikaonsen9
        with dissolve

    tb "My husband is...a good man."
    tb "But he’s not a man I chose for myself."
    tb "I do love him, but...I don’t think I’ve ever been {i}in{/i} love with him."
    tb "We both come from wealthy families and our marriage was arranged from the moment we were born."

    if bonus == True:
        scene chikaonsen10
        with dissolve

    tb "And between you and me, he can {i}not{/i} perform. Like, at all."

    if bonus == False:
        tb "And no matter how many times I tell him to put down the clarinet, he just refuses to do so."

    c "I...don’t really know what I’m supposed to say to that."

    if bonus == True:
        scene chikaonsen11
        with dissolve

    tb "Have you and your not-boyfriend made it that far yet, dear?"

    if bonus == True:
        c "We’ve done other stuff but...haven’t gone {i}all{/i} the way yet."
        c "We were kind of about to, but then my heart started going crazy and I wanted to take a minute or...thirty to prepare myself."
    else:
        c "We’ve done other stuff but...haven't played the clarinet yet..."

    if bonus == True:
        scene chikaonsen12
        with dissolve

    tb "Oh! This means I’ll get to be around for your first time! Splendid!"

    if bonus == False:
        tb "I've hidden clarinets in every room, so you'll surely be able to find one if you look hard enough!"

    tb "If you wind up wanting someone to talk to afterward, come over to my room. I’d love to hear all about it! Tsukasa and I are in #3."
    c "You want to...hear all about my first time?"
    tb "Of course! In vivid detail!"
    c "Tsubasa...are you actually a deviant?"

    if bonus == True:
        scene chikaonsen13
        with dissolve

    tb "What? No. Of course not. I just-"
    tb "Don’t normal girls like talking about things like that?"
    c "I mean...not in {i}detail{/i}. "
    tb "Oh dear. It seems I’ve said something horribly inappropriate then."

    if bonus == True:
        scene chikaonsen14
        with dissolve

    c "Pfft! It’s fine. No need to get all apologetic about it."

    if bonus == True:
        scene chikaonsen15
        with dissolve

    c "I’ll probably wind up spending the rest of the night with my not-boyfriend afterward, but I’ll definitely come visit if something changes."
    tb "So you’ve decided to follow through after all? It’s not an invasion of privacy for me to ask that much, is it?"
    c "Nah, you’re fine. "
    c "And yeah. I’m gonna do it."
    c "I love him, so-"
    tk "Do what?"

    if bonus == True:
        scene chikaonsen16
        with dissolve

    tk "What are you going to do with the man you love, Miss? He looks too old for you."
    c "Oh...Tsukasa. You’re here too..."
    tb "Tsukasa. Chika and I are talking about {i}adult{/i} matters right now. It’s not something you should be listening in on, dear."
    tk "I can listen. I’m an adult. Please, carry on."

    if bonus == True:
        scene chikaonsen17
        with dissolve

    c "I mean...I guess it’s fine as long as we leave out all the...explicit language, right?"
    tb "Whatever you’re more comfortable with, dear."
    tb "Even if it’s just talking about love in general, feel free to vent."
    tb "Being a mother is a full-time job for me, so I like to think I’m a pretty good listener."
    tb "Not that I think your mother has done a poor job, of course. She must be truly wonderful if she’s managed to raise a girl like you."

    if bonus == True:
        scene chikaonsen18
        with dissolve2

    c "..."
    c "Mhm."
    c "She did great."
    tb "..."
    tk "..."
    tb "Oh dear..."
    tb "I’ve said something insensitive again..."
    tk "What happened to your mother, Miss?"

    if bonus == True:
        scene chikaonsen19
        with dissolve

    tb "Tsukasa!"
    c "She’s not around anymore. "
    tk "So your father takes care of you all by himself?"
    c "He’s...not around either."
    tb "Tsukasa! Leave the two of us alone and I’ll have your father buy you anything you want!"
    tk "If your mother and father are both gone, who takes care of you? Your butler?"
    c "I take care of myself. I’m craaaaazy strong. Like a superhero."
    tk "Superheroes don’t exist. You should be old enough to understand that."
    c "Heheh~ Yeah, I guess I should."

    if bonus == True:
        scene chikaonsen20
        with dissolve

    tk "I do agree that you’re really strong, though."
    tk "If {i}I{/i} had to take care of myself, I’d eat nothing but candy. And Papa always says that candy makes you fat and ugly."
    tk "And you’re not fat and ugly at all, Miss. You’re almost as pretty as I am and I still have both of my parents!"

    if bonus == True:
        scene chikaonsen21
        with dissolve

    tb "Tsukasa! This is your final warning!"
    tb "Leave the two of us alone or we’ll be going home {i}tonight{/i} instead of tomorrow!"
    tk "Eek! Mother is angry!"
    tk "It was nice talking to you, Miss!"

    if bonus == True:
        tk "Have fun doing things I’m not old enough to talk about!"
    else:
        tk "Have fun playing the clarinet!"

    if bonus == True:
        scene chikaonsen22
        with dissolve

    "The youngest of the three leaps out of the water and heads back to her room, leaving the concerned mother alone with a makeshift orphan."
    "They bleed together."

    tb "I am...so sorry for her behavior."
    tb "She’s been a total troublemaker ever since she was born. I can’t even tell you how many of our maids have quit because of her."

    if bonus == True:
        scene chikaonsen23
        with dissolve

    c "It’s fine. Really. It’s my fault for tearing up anyway."
    c "This is supposed to be a getaway, not some place for me to bawl my eyes out in front of somebody else’s mom."
    c "Thanks for even taking the time to talk to me."
    c "It..."
    c "It helps."

    if bonus == True:
        scene chikaonsen24
        with dissolve

    tb "You don’t have to thank me at all, dear. It’s my pleasure. "
    tb "I’ll be more considerate in the future before saying things like that."
    tb "Now...back to the topic of love."

    if bonus == True:
        scene chikaonsen25
        with dissolve

    c "You’re really excited to talk about all this love stuff, huh?"
    tb "Can you blame me for wanting to hear about something I was never able to experience on my own?"
    c "Course not. I’m just not really sure where to start since my experience with “love” is just as limited as my experience with...the other thing."
    c "Like, I didn’t even receive my first confession until a few months ago."

    if bonus == True:
        scene chikaonsen26
        with dissolve

    tb "Your teacher confessed?! Chika, that’s wonderful!"
    tb "What are you waiting for?! Get back to your room and-"
    c "It was...actually a girl."
    c "A girl confessed to me."
    c "One of my friends."
    tb "..."
    c "..."

    if bonus == True:
        scene chikaonsen27
        with dissolve

    tb "..."
    c "..."
    tb "Perhaps I’m just too old to talk to [young]people anymore."
    tb "I’m making far too many mistakes for just one conversation."

    if bonus == True:
        scene chikaonsen28
        with dissolve

    c "You don’t have to blame yourself for that one. The way I said it was kind of misleading, I guess."
    c "I’m actually really glad you asked since I...haven’t really had anyone to talk about it with."
    tb "Well...if you’re fine with me continuing to make things horrible..."
    c "You’re not making anything horrible. This is actually really fun."
    tb "So...this {i}girl{/i} then...you said she was a friend of yours?"
    c "Yeah. We’ve known each other since middle[school]."

    if bonus == True:
        scene chikaonsen29
        with dissolve

    c "She’s really nice and super funny, but in like a...“not trying to be funny” sort of way."
    c "Like she’s a total nerd who talks way too much and makes herself look like an idiot and you kinda just wanna...hug her and pat her head."
    c "And she’s sooo pretty and like, doesn’t even realize it. It’s actually kind of annoying."
    c "But it’s not all good stuff. She has her problems too. "
    c "I mean, we all have our problems I guess. But hers just seem to come out of nowhere, so she can never even prepare for them."
    c "I don’t know if she knows that {i}I{/i} know that. But it’s kind of hard to not pick up on somebody’s tics after being around them for so long."
    tb "It seems to me like you really like this girl."
    c "I do. She’s amazing."
    c "And if she told me about it sooner, before I met the guy I’m here with today..."
    c "I probably would have given it a shot."
    tb "And this “guy.” Sensei? Is he aware of this?"
    c "..."
    c "Maybe?"
    c "Probably?"

    if bonus == True:
        scene chikaonsen30
        with dissolve

    c "I don’t know."
    c "I’d kind of prefer him to not get involved since it’s between her and me."
    c "If he knows, he knows. But it’s not like I’m going to vent to him about it when it will only make things more confusing than they already are."
    c "There are...a {i}lot{/i} of girls who seem to like him just as much as I do."

    if bonus == True:
        scene chikaonsen31
        with dissolve

    c "And I’m secretly a bitch, so I want to keep all of them as far away as possible."
    c "It’s better that things stay simple. "
    c "He’s not the type who likes drama so, if I can, I’m gonna avoid drudging it up by all means necessary. "
    c "He’s like, really protective of the other girl, so I don’t want to risk him trying to get the two of us together or anything like that."
    c "The more he thinks of me, the better. You know?"

    if bonus == True:
        scene chikaonsen32
        with dissolve

    tb "You really do love him, don’t you?"
    c "Sooooo much. Like, a gross amount of love."
    tb "Have you told him yet?"

    if bonus == True:
        scene chikaonsen33
        with dissolve

    c "Told him what? That I love him?"
    c "No...I mean..."
    c "I mean, he probably already knows."
    c "Right?"
    tb "He’s a man. He won’t know unless you tell him."
    c "I don’t know, Tsubasa. I feel like I make it pretty damn obvious."
    tb "Well...here’s a new question, then."
    tb "What are you waiting for?"
    tb "You want to keep those other girls away from him, don’t you? "
    tb "Wouldn’t telling him you love him help with that?"
    c "I feel like it could go either way. "
    c "Like, he’d either be really happy to hear it or he’d think I was moving too fast and try to distance himself from me."
    tb "Forgive me if this is one more thing I’m not fully comprehending due to lack of experience but-"
    tb "Do you really think you’d fall in love with someone who would run away after hearing that?"
    tb "Have some more faith in yourself. You’re a bright, beautiful [young_girl] with a great future ahead of you."

    if bonus == True:
        scene chikaonsen34
        with dissolve

    c "Tsubasa..."
    c "I really don’t know how to thank you for all of this."
    c "I’ve never been able to talk about stuff like this with anyone before...and that advice was like, exactly what I needed."
    tb "You don’t need to thank me at all, dear."
    tb "Just go back to your room and give the man you love that WAP."
    c "..."
    tb "..."
    c "..."
    tb "..."
    c "I’m sorry, what?"

    if bonus == True:
        scene chikaonsen35
        with dissolve

    tb "Did I not use that term correctly? "

    if bonus == True:
        tb "I often turn on the radio when I have time to myself. And I’ve been hearing that word thrown around by [young]people in sexual contexts."

    c "That’s..."
    c "I mean...you’re not {i}wrong{/i}...it was just a really weird time to say that..."
    c "I...I’m not sure how I feel about it."

    if bonus == True:
        scene chikaonsen34
        with dissolve

    tb "Well, whatever the case...I think we both know you’ve overstayed your welcome here."
    tb "The poor man is probably still up there waiting for you."
    tb "And, I’m sorry if this suggestion is insensitive-"
    tb "But if you wind up being too scared to follow through-"

    if bonus == True:
        scene chikaonsen36
        with dissolve

    tb "Or perhaps you just want to talk to a mother-"
    tb "You know where to find me."
    c "Yeah..."
    c "Probably sounds weird and corny, but like...I kinda feel like fate brought the two of us together today."
    c "I try my best but...not having my mom around to talk about stuff like this with can be really overwhelming."
    c "So hearing from you that I’m not just rushing into things is..."
    c "It’s a big help."
    c "Thank you."
    tb "I don’t know much about fate, but I {i}do{/i} know that I’m happy to have helped you. "
    tb "It’s okay to be scared. And it’s okay to worry about things like this."
    tb "But if {i}you{/i} think you’re ready for your first time...and {i}you{/i} think you’re ready to tell the WAP man you love him-"
    c "Please don’t call him the WAP man, Tsubasa."
    tb "Then all you need to do is follow your heart."
    c "Yeah..."
    c "Yeah. I think this bath has gone on for long enough."
    c "Are you getting out, too?"
    tb "Oh, heavens no. The longer I can relax and not have to deal with Tsukasa, the better."
    tb "Good luck, though."
    tb "I’ll be here if you need anything."

    scene black
    with dissolve2

    "Sometimes, bleeding freely {i}isn’t{/i} ideal."
    "Sometimes, it’s better to have someone there beside you, holding your wound closed and making sure bacteria doesn’t find its way in."
    "Someone to apply a tourniquet."
    "Relying on people like that is fine if you find yourself caught in a pinch."
    "Does it make you stronger? No."
    "But it doesn’t make you weaker either."

    stop music fadeout 10.0

    "Be happy!"
    "Find your place in the world!"
    "And if one does not exist, create your own!"
    "Just know-"
    "That even if everything goes according to plan-"
    "And all of the puzzle pieces in all of your world fit into place-"
    "You will still bleed."

    "{i}Chika has acquired a new mother!{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ chikaonsen2 = True

label chikaonsen3:
    scene chikavirgin1
    with dissolve
    play music "asobeatsex3.mp3"

    c "Uhh...where did that TV come from?"
    s "I asked the front desk if they had one and they brought it over."
    c "What happened to taking a bath?"
    s "I took one. I just didn’t realize how long you were going to be gone for."

    scene chikavirgin2
    with dissolve

    c "Yeah...sorry about that."
    c "That woman, Tsubasa. The one we met when we got here..."
    c "The two of us started talking for a little bit and time just sorta flew by without me realizing it."
    s "I see."
    s "Well I’m glad you’re back."
    c "Yeah. Me too."
    c "Whatcha watching?"
    s "This place only has basic cable, so it’s just some random baseball game."
    c "Cool, cool."
    c "Mind if I watch it with you?"
    s "I’m not really watching it. I was just figuring out how to pass the time."

    scene chikavirgin3
    with dissolve

    c "Oh, cool. Then you won’t mind if I do this."

    if bonus == True:
        jump chikavirginx
    else:
        scene black
        with dissolve

        "Chika walks in front of me and gives me a long, aggressive hug."
        "Unbeknownst to her, I do mind. She is interrupting my television program."
        "Anyway, we hug for a little while longer. And even though we have hugged many times before, this hug seems particularly important."

        $ renpy.end_replay()
        $ chika_virgin = False
        $ chikaonsen3 = True
        $ chika_love += 5
        stop music fadeout 10.0

        "{i}Chika’s affection has increased to [chika_love]!{/i}"
        "........."
        "......"
        "..."

        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date
        else:
            "ERROR"

        "{i}[totaldays] days have passed...{/i}"

label chikaonsen4:
    if bonus == True:
        scene chikawakesup1
        with dissolve2
    else:
        scene wintersky
        with dissolve

    play music "justlights.mp3"

    "I wake up again. A wonderful start to the day."
    "I stare at the girl in front of me who, in what I imagine is a vast departure from normal, fell asleep with her makeup on."
    "Sunlight leaks in through a small paper window and informs me that it’s morning."
    "Or, in more depressing terms- time to leave."
    "It’s unfortunate that this getaway was only for one night, but I’m sure that there will be plenty more just like it in the future."
    "I just have to hope Chika decides to call into more radio shows."
    "Of course, there’s always the chance for me to just...{i}buy{/i} tickets to places like this..."
    "But where’s the fun in that?"
    "It’s much better to have things dropped into your lap than it is to work for them."
    "You’re probably used to hearing that sort of opinion from me by now, aren’t you?"
    "Which means that you probably understand that it’s time for me to, once again, butcher the words of someone much smarter than I am."
    "I believe it was Thoreau who said, “It is not worth the while to go round the world to count the cats in Zanzibar.”"
    "Now, when he said this, he probably meant something along the lines of “It’s better to search within yourself for what you want than to go greatly out of your way for it.”"
    "Why someone would be so dedicated to counting cats, I don’t understand."
    "So I’m going to chalk his words up to insanity and repurpose them to fit my own narrative."
    "Don’t work hard because working hard sucks. "
    "Buy your own cats and count them."
    "There. Problem solved."

    if bonus == True:
        "I spit on Thoreau’s grave from my place beside a naked [teenager] and wish away my morning erection."
        "It probably sounds hard to believe, but after last night, the last thing I want is to have sex right now."
        "And I worry that if Chika wakes up and sees that her new best friend is already fully erect, I may never fuck again."
    else:
        "I spit on Thoreau's grave and think a few other things I'm not allowed to say in the censored version of the game."

    s "..."

    "Just how long is she going to sleep for, though?"
    "What time even is it right now?"
    "I reach over to grab my phone out of my pants (Which are conveniently only several feet away) and find that it’s just after 6:00 AM."
    "Also, my phone is about to die because I passed out without plugging it in last night."
    "I sigh to myself and bring my face closer to hers, hoping that she wakes up and quells this boredom soon."
    "I’d hate to be the one to disturb her slumber, but I honestly might have to at this rate."
    "Sometimes, I feel like I’ll waste away if I just stay in bed."
    "Like I’ll disintegrate and turn into sand."
    "And then, before I know it, girls will be having their hearts broken as they confess their feelings on top of me."
    "Thankfully, I managed to avoid that same tragedy last night."
    "Though, it was in a way that would not quite turn to glass if heated thoroughly."

    s "..."

    "My mind connects the word “thorough” to “Thoreau” and I loop back to the idea of cats and Zanzibar."
    "God, I hope Chika wakes up soon."

    c "Mn..."

    "All of the cats die and I don’t have to count anything anymore."

    c "Sen...sei..."
    s "..."
    s "Chi...ka..."

    if bonus == True:
        scene chikawakesup2
        with dissolve

    c "Mm...what time is it?"
    s "It’s a little after 6:00 AM."
    c "So...early..."

    if bonus == True:
        scene chikawakesup1
        with dissolve

    c "Goodnight..."
    s "You can’t say goodnight when the sun is rising."
    c "Good...sun..."
    s "That’s not even a thing."
    c "Mn..."
    s "..."

    "Huh."
    "All this time, I thought Chika was a morning person."
    "She’s always waking up early to make breakfast and...listening to radio shows with Chinami and-"
    "I wonder if maybe she’s only sleeping in now because she rarely ever has the chance to?"
    "But...then again, it is 6:00 AM."
    "I guess it doesn’t really constitute sleeping {i}in{/i} until it’s around...10:00 AM, I guess?"
    "Wait."
    "How come you can sleep {i}in{/i} but not {i}out?{/i}"

    s "Chika, please wake up. I can’t do this anymore."

    if bonus == True:
        scene chikawakesup3
        with dissolve

    c "Wha?...Do what?..."

    if bonus == True:
        scene chikawakesup4
        with dissolve

    if bonus == True:
        c "Do you wanna...have sex again?..."
        s "No. I’m pretty sure both of us would die."
        c "Sex~"
        s "Yes, Chika. That is a thing we did...many, many times last night."
        c "You’re a...good...sex guy..."
        s "Thank you very much for that completely normal compliment."
        c "{i}Sex man...{/i}"
    else:
        c "Do you wanna...hug again?..."
        s "No. I’m pretty sure both of us would die."
        c "Huuuuug~"
        s "Yes, Chika. That is a thing we did...many, many times last night."
        c "You’re a...good...hug guy..."
        s "Thank you very much for that completely normal compliment."
        c "{i}Hug man...{/i}"
    s "Wow, you’re really out of it, aren’t you?"

    if bonus == True:
        scene chikawakesup5
        with dissolve

    c "Pancakes..."
    s "You want breakfast?"
    c "Chinami likes...pancakes..."
    c "Gotta...make her some..."
    s "Chinami isn’t here right now, Chika. We’re at the onsen."
    c "Call...Yumi..."
    c "About the...pancakes..."
    s "My phone is basically dead."

    if yuminumber == False:
        s "Also, I don’t even have her number."

    if bonus == True:
        scene chikawakesup6
        with dissolve

    c "Mmm...I’ll do it..."
    c "I’m...up now."
    c "Good morning, Sensei~"
    s "Good morning, Chika."
    c "Did you enjoy our first night together?"
    s "I’m sure I’ll be remembering this for the rest of my life."
    c "Heheh~ I’m glad..."
    c "Hey, do you think they have a gift shop downstairs?"
    s "A gift shop? I don’t remember seeing one. Do you want a snack or something?"

    if bonus == True:
        c "I need a morning after pill."
        s "Oh."
        s "Uhh."
        c "Unless you want me to drop out, marry you, have a baby, and then move into Ami’s room."
        s "I can’t say I want any of those things right now."
        c "I didn’t think so."

        scene chikawakesup7
        with dissolve

        c "It’ll just be for this one time."
        c "I’ll start taking birth control now that I know we’re going to be “sexually active” together."
        s "I’m glad you didn’t suggest something as outrageous as a condom."
        c "Why would I do that when having you cum in me feels so good?"
        s "Okay, time to change the topic before I-"
        s "Wait. Too late. It’s hard again."

        scene chikawakesup6
        with dissolve

        c "Oh nooo~ Whatever will we do?"
        s "Nothing right now. "
        c "What if I’m really, really gentle?"
        s "Hands to yourself, woman. I can’t have you turning into a nymphomaniac on me."

        scene chikawakesup8
        with dissolve

        c "Hey! Just because you came in me like ten times last night and we passed out totally naked and covered in sweat doesn’t mean I’m any less wholesome than I was last week!"
        s "It...kind of {i}does{/i}, though."

        scene chikawakesup9
        with dissolve

        c "Nuh-uh."
        s "I am not going to argue with you about this."
        c "Put it in me or face the consequences, [chikamaster]."
        s "What kind of consequences would even come from this?"

        scene chikawakesup10
        with dissolve

        c "I only {i}pretend{/i} to take the morning after pill and just let myself get pregnant."
        s "That is...way too huge of a thing to do out of spite."

        scene chikawakesup11
        with dissolve

        c "I’m obviously kidding, Sensei. I can barely take care of Chinami."
        c "I’m {i}not{/i} a nympho, though. So don’t go saying anything like that to anybody."
        s "Who would I even say that to?"

        scene chikawakesup12
        with dissolve

        c "I mean, you can talk about what we did to whoever you want. I don’t care."
        c "Like, I’ve obviously gotta tell Yumi."
        s "I’m sorry, what?"
        c "She’s my best friend and this was like, a super big deal. I totally have to tell her."
        s "I...don’t think that’s a good idea."
        c "Why not? Cause she always acts all tough and talks about not liking you?"
        c "That’s only like, half-serious. You know that, right?"
        s "That is still enough seriousness for me to think it’s better if she doesn’t know that we’re having sex."
        c "I mean...I can probably leave out the sex part, but..."
        c "I can still tell her you’re my boyfriend now, right?"
        s "..."
        c "..."
    else:
        c "I want...coffee..."
        c "Also, I still have to tell Yumi that...you and me are dating now..."
        s "I'm sorry, what?"
        c "Yeah...because of the hugs...right?"
        s "..."

    "Uh-oh."
    "It appears we have a...dramatic misunderstanding about our future together."

    if bonus == True:
        "But how am I supposed to come out and say something like “Oh, I’m not your boyfriend, but thanks for telling me you loved me and letting me cum in you a bunch of times?”"
    else:
        "But how am I supposed to come out and say something like “Oh, I’m not your boyfriend. All of those hugs meant absolutely nothing?”"

    "How the fuck do I get out of this?"

    s "Why do you want to tell her anyway?"
    c "Because I love her. And I love you."
    c "And I want all of us to be happy together."
    s "And you think Yumi knowing about {i}us{/i} is going to make her happy?"
    c "I don’t think it would make her...{i}not{/i} happy?"
    s "I kind of think she’d oust the both of us."
    c "Yumi? No way, she-"

    if bonus == True:
        scene chikawakesup13
        with dissolve

    c "Wait...you’re not like...embarrassed of me, are you?"
    s "What? Not at all. I think you’re amazing."
    s "But I don’t think it would be safe for anyone else to really know just yet. And that’s including Yumi."

    if bonus == True:
        scene chikawakesup14
        with dissolve

    c "I...don’t want to keep this a secret from Yumi, Sensei. "
    c "You probably don’t get it since you’re a guy, but I need to like...I don’t know, mark my territory, I guess?"
    s "Do you...think Yumi is going to make a move on me or something?"
    c "Not at all. But I don’t think it’s impossible for her to like, wind up liking you or whatever."
    c "I don’t think she’d do something like that to me since the two of us are so close, but like-"
    c "If she knows we’re already together, it might prevent things from ever progressing that far."
    s "I really don’t think you need to worry about that happening, Chika."

    if bonus == True:
        scene chikawakesup12
        with dissolve

    c "Hmm..."
    c "Okay. It looks like we need to compromise."
    c "How about this?"
    c "I won’t go out of my way to tell her...but if it ever comes up in conversation, I’m not going to lie to her about it."
    c "It’s not like Yumi ever really wants to talk about stuff like that anyway. "
    c "And even if I do wind up telling her, I’ll make sure she never even {i}thinks{/i} about mentioning it to the other girls."
    c "She’s surprisingly loyal. And I don’t think she’d ever want to hurt either one of us."
    s "..."

    "Well-"
    "It’s better than nothing, I guess."

    if bonus == True:
        "I mean, Yumi already assumes I’m having sex with the entire class anyway."
    else:
        "I mean, Yumi already assumes I’m hugging the entire class anyway."

    "So having one of the girls confirmed (If things do come to that), likely won’t change much."
    "And, as far as the boyfriend things goes-"
    "I don’t think it’s necessarily {i}bad{/i} to let Chika go on thinking that."
    "I mean, I’m sure the other girls I’m involved with look at me the same way as well. "
    "They just haven’t come out and said it."
    "But that’s what sets Chika apart from the others."
    "She’s mature enough to set her sights on something and then just...take it without thinking of how it will affect anyone else."
    "It’s actually kind of relentless."
    "I admire her."

    s "Yeah. Okay."
    s "Let’s just try and keep it as secretive as possible until [high_school] is over."
    c "Heheh~ I never would have imagined my [high_school] sweetheart would be my teacher."
    s "And I never would have imagined we’d end up in a position like this after our first meeting at the mall."

    "That’s a lie. I imagined this a lot."

    if bonus == True:
        c "Really?"
        c "So you didn’t go home and rub one out to me?"
        s "Nope. Definitely not a thing that’s ever happened."
        c "Weird. Cause I totally did."
        s "Oh, come on. I literally just stopped being hard."

        scene chikawakesup7
        with dissolve

        c "Sensei, as long as the two of us are together, you can kinda count on getting hard pretty much all the time. "
        c "I’m gonna make your life Hell from now on."
        s "Yeah, that sounds like a real nightmare."
        c "Heheh~ Just wait until I start sending you naughty pictures of myself in the middle of class."
        s "Wow, the nightmare never ends."

        scene black
        with dissolve2

        "Chika laughs and hops out of the futon, making her way into the living room and rearranging some of the furniture we may have...knocked around last night."
        "I think about helping, but decide to bask in the stray sunlight for a moment longer."
        "And, once I’m able to do so without much of an...obstacle, I put my pants back on and head over to meet her."

        scene chikawakesup15
        with dissolve

        c "Why am I suddenly the only one that’s naked?"
        s "Why are you still naked and reaching for your bag as if you’re ready to leave?"
        c "Am I not supposed to walk back to the front office like this?"
        c "It’s not like I can wear the yukata anymore."
        s "Definitely don’t do that."
        c "Jealous somebody else might see me?"
        s "That and I don’t want us to be arrested for indecent exposure."
        c "People get naked in the hot spring, though. I’m sure they wouldn’t mind if we do it in the lobby."
        s "Uh-huh. And what about the bus stop that’s right outside of the building?"
        c "What about it?"
        s "Are you going to wait outside like that as well?"
        s "..."
        c "..."
        s "Chika."

        scene chikawakesup16
        with dissolve

        c "Oh my God, Sensei. Do you really not understand a joke when you hear it?"

        scene chikawakesup17
        with dissolve

        c "It’s kind of sad, though..."
        c "Like...I really don’t want to leave. "
        c "I had so much fun yesterday."
        c "Even if all we did was...you know...each other."
        s "Hey, that’s not {i}all{/i} we did. You took that extremely long bath as well."
        c "Yeah..."
        c "And that was...somehow just as good..."

        scene black
        with dissolve2

        "I stand there for a moment as Chika gets dressed, trying to come to terms with how a bath can be just as good as having sex with me."
        "I know Chika can get a little...crazy...but-"
        "Am I...not enough for her?"
        "Just what the hell is that girl into?"
        "........."
        "......"
        "..."
    else:
        scene black
        with dissolve

        "Some other stuff happens or whatever and then we wind up leaving the onsen."
        "........."
        "......"
        "..."

    scene chikawakesup18
    with dissolve

    "We make our way back to the lobby and hand in our room key. "
    "I wound up carrying the TV down as well since the person who brought it up while Chika was away seemed far too old to be doing manual labor like that."
    "And..."
    "Well, I guess that’s it."
    "It was short. It was sweet."
    "It was definitely a vacation."

    c "Have everything? Not forgetting anything in the room?"
    s "Not that I’m aware of."
    s "I mean, it’s not like I really brought anything to begin with."
    s "How about you?"
    c "Nope! Totally good."
    c "Guess...that’s that then."
    s "..."
    c "..."
    s "..."
    c "..."
    s "Cool, so what are we waiting for?"

    scene chikawakesup19
    with dissolve

    c "I was..."
    c "Kinda just hoping to..."
    tb "Oh! Good morning, you two."

    scene chikawakesup20
    with dissolve

    c "Oh, hey! "
    c "I was just hoping I’d run into you one last time."
    tb "Another example of fate, perhaps?"

    scene chikawakesup21
    with dissolve

    tk "Good morning, Mister."
    tk "Would you be willing to discuss with me what game you two were playing last night? "
    tk "It sounded very exciting."
    tb "Tsukasa...how many times do I have to tell you? They were playing a game for adults."
    s "You...uhh..."
    s "You heard all that?"

    scene chikawakesup22
    with dissolve

    if bonus == True:
        tb "You two...sure are lively."
    else:
        tb "Why, it sounded just like the two of you were hugging."
        tb "I could have sworn I heard a bit of clarinet as well."
        s "That was me. I'm not very good."

    c "Hahah...hah...hah..."
    c "This totally isn’t embarrassing at all..."
    s "I am...sorry you had to hear all that."
    tb "Oh, there’s no need to apologize."
    tb "Lovers will be lovers."

    scene chikawakesup23
    with dissolve

    tb "And Chika, dear...I forgot to bring it up yesterday, but I’d be happy to exchange contact information with you in the event that you’d want to meet up for lunch or something of the sort."

    scene chikawakesup24
    with dissolve

    tb "Please forgive me if I’m overstepping my bounds by saying that."
    c "No! Not at all! I’d like, totally love that!"

    "..."

    s "How about I leave you two alone for a little while?"
    s "To say goodbye, I mean."

    scene chikawakesup25
    with dissolve

    c "I’ll only be a few minutes. I promise."
    s "No worries. I’ll just wait outside."
    s "It was nice meeting you."
    tb "It’s been a pleasure meeting you as well. Truly."
    tk "Bye-bye! Please try to be a little more quiet when you play games in the future!"
    s "Right..."

    scene black
    with dissolve2

    "I head outside and come to terms with the trip being over."
    "Chika spends the next five or so minutes talking to the girls inside."
    "And while I can’t say for certain that I understand why, I’ve got a pretty good idea."

    if bonus == True:
        "Teenage girls are fragile."
    else:
        "College girls are fragile."

    "Sometimes, they require fully grown specimens to latch onto so they don’t float off into the air and get sucked into a jet engine. "
    "I don’t think Chika is close to floating away any time soon."
    "Especially now that the two of us are...whatever we are."
    "I’m sure our respective answers to that would be slightly different."
    "But I’m glad she seems to have found someone else to latch onto."
    "Frankly, I’d like to latch onto Tsubasa as well."
    "Albeit in an immensely less wholesome way."
    "But thoughts like that will have to wait until there aren’t feelings at stake."
    "For now...I’ll just-"

    s "..."

    "I see a group of cats off in the distance."

    $ renpy.end_replay()
    $ chika_love += 1
    $ chikaonsen4 = True
    $ onsenticket = False
    stop music fadeout 15.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "{i}The trip to the onsen has come to an end.{/i}"

    if bonus == True:
        play sound "texttone.wav"

        "{i}You have received a photo from Chika to commemorate the occasion!{/i}"
        "........."
        "......"
        "..."
        "My stop comes first."
        "I get off the bus and watch Chika fade from my sight."
        "But not before giving her a few thousand yen for a morning after pill."

    jump saturdayafternoon

label chikalust15skip:
    play sound "dooropen.mp3"
    scene goodmorningio1
    with dissolve

    "I collapse into my hotel bed once more in a rather anticlimactic end to an action packed day."
    "I’m not sure what it was that compelled me to hang around the bar instead of coming back here earlier, but it is what it is."
    "Housekeeping made my bed, and now I must lay in it."
    "I notice that Io never turned the air off after leaving this morning."
    "This is good because it saves me a trip across the room and will prevent a second injury for her should she manage to sneak in again."
    "Which I’m sure she won’t."
    "Not after discovering that I’m not the only person actively seeking something out with repeated knocks on the doors of people who may or may not want to see me at that given moment."

    scene black
    with dissolve

    "I close my eyes and accept, however, that there will always be someone who wants to see me at {i}every{/i} given moment."
    "There’s no real reason for it, really."
    "I just conveniently exist in a convenient place during a convenient crack in time."
    "And, conveniently enough, I’ll be reminded of that all once more tomorrow morning-"
    "When every girl gathers around to hear the announcement of who it will be that can have me for one more night."
    "One more night."
    "That’s literally it."
    "That’s what all of this was about."
    "I am undeservedly blessed."
    "..."
    "I fall asleep to the violent whir of an air conditioner working its non-existent heart out."

    $ totaldays += 1
    $ day -= 6
    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
    else:
        "ERROR ADVANCING DAYS"

    "........."
    "......"
    "..."
    "[totaldays] Days have passed..."

    jump dormwar17

label chikalust15:
    play sound "dooropen.mp3"
    scene goodmorningio1
    with dissolve

    "I collapse into bed after being dropped off at the hotel by Maki."
    "I was hoping that by sticking around for so long and watching so many girls get intoxicated, that one of them might let their judgement slip and make my night a bit more interesting."
    "But here I lay, in the same clothes I slept in last night, completely alone. "

    s "..."

    "The bed smells like Io."
    "She probably slept here for a few hours after I left this morning."
    "I wonder if she’ll come again tonight."

    play sound "knock.mp3"

    "I imagine the sound of her knocking, worried that one of the other girls might be rounding the corner at that moment."
    "She’d peer over her shoulder every few seconds while I make my way to the door- an explanation or excuse already prepared in the event of being caught."
    "An explanation that she’d probably throw away the second she's confronted."
    "What an adorable coward she is."
    "It would be nice if she came tonight."

    play sound "knock.mp3"

    s "..."

    "Perhaps I wasn’t imagining anything at all?"

    scene black
    with dissolve

    "I get off the bed and make my way over to the door."
    "It appears I won’t have to be alone after all."

    scene chikatoukafun1
    with dissolve
    play music "asobeatsex2.mp3"

    c "{i}*Hic*{/i} Hiiiiiiiiiiiii~"
    s "You...can still walk?"
    c "Can’t...{i}*hic*{/i}...get rid of me...that...eashilyyy..."
    to "My face...feels...{i}*hic*{/i}...rather strange..."

    "Welp, there is absolutely no way that at least one of them won’t be regretting this in the morning."

    c "Whatcha...doin’ Sensei?..."
    c "We weren’t...{i}*hic*{/i}...finished hangin' out yet..."
    s "Really, how did you two even get over here? You could barely walk when we left the bar."
    c "It’s the...{i}*hic*{/i}...power of love, Sensei!"
    c "Now...let’s...{i}*hic*{/i}...make out..."
    s "And was Touka brought here by the power of love as well?"
    to "Love..."
    to "Love sounds...lovely..."
    c "Touka’shhh...fine..."
    c "We were just {i}*hic*{/i}...talking about our...dates with you..."

    if bonus == True:
        jump chikatoukax
    else:
        scene black
        with dissolve

        s "This is no time for tomfoolery. I must nurse the two of you inebriated women back to health."

        "I take it upon myself to make some coffee for the girls and sit with them until they are sober enough to return to their rooms."
        "But, for some strange reason, I feel compelled to choose one of them as the winner of being drunk."

        menu:
            "Chika wins":
                $ dorm1warpoints += 1
                $ chikalingeriewin = True

                "Chika is clearly the better drunk."
                "I am glad I was able to swiftly reach a decision."
            "Touka wins":
                $ dorm2warpoints += 1
                $ toukalingeriewin = True

                "Touka is clearly the better drunk."
                "I am glad I was able to swiftly reach a decision."

        stop music fadeout 5.0
        $ renpy.end_replay()
        $ chikalust15 = True
        $ chika_lust += 1

        "{i}Chika's lust has increased to [chika_lust]!{/i}"
        "........."
        "......"
        "..."

        $ totaldays += 1
        $ day -= 6
        if day == 1:
            hide sunday onlayer date
            show monday onlayer date
        else:
            "ERROR ADVANCING DAYS"

        "[totaldays] Days have passed..."

        jump dormwar17

label chikainvitemissionary:
    scene black
    with dissolve

    ".........."
    "......"
    "..."

    if bonus == True:
        jump chikainvitemissionaryx
    else:
        $ chika_lust += 3
        stop music fadeout 5.0

        "{i}Chika's lust has increased to [chika_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label chikaspecial40:
    scene chikalunch1
    with dissolve
    play music "lifeismostlygood.mp3"

    "Okay. "
    "I’m tired of winter."
    "And I would very much like summer to come back now."
    "I wonder if Maya knows any way to sort of just...push up the date of the next reset and usher in another change of seasons or something."
    "The cold was nice at first- but even now, in the earliest stages of its death, I grow tired of its tomfoolery."
    "Desperate for a change of pace, I clutch my fists together and wait for Maya to conveniently appear before me."
    "Everyone knows that once I think of something like that, it almost always immediately happens. And I see no purpose in a reversal of fortune this early on a Monday morning."

    s "..."
    s "Any minute now."

    scene chikalunch2
    with dissolve

    c "Hey! Crazy seeing you here, Sensei."
    s "Hey, Maya. You got exponentially taller, tanner, and less weird since I last saw you."

    scene chikalunch3
    with dissolve

    c "Maya? Are you wandering around looking for her or something?"
    s "It’s more like I’m...wandering around in search of summer. And Maya is the only person I know with time manipulation powers."
    c "You know, I always thought there was something weird going on with her, but time manipulation was pretty low on my list."
    s "Well, now that you know, I’m excited for you to either forget all about it or just think I’m joking."

    scene chikalunch4
    with dissolve

    c "Oh, come on. If superpowers like that were real, Chinami would be like, flying around and killing dragons or whatever it is wizards actually do."
    s "Fantasy isn’t my favorite genre, so I'm not going to pretend to know much about it, but I’m pretty sure wizards don’t fly."

    scene chikalunch5
    with dissolve

    c "So, is this just what you’re doing for lunch? Walking around, fantasizing about Maya instead of your real girlfriend?"
    s "This is actually one of the very rare occasions where I’m {i}not{/i} fantasizing about something that would make you mad at me."

    scene chikalunch6
    with dissolve

    c "Wait, what is that supposed to mean?! How often are you fantasizing about stuff like that?!"
    s "Sorry, did I say stuff that would make you mad at me? I meant...fantasizing about the two of us on some sort of romantic getaway or...some other cute thing."

    scene chikalunch7
    with dissolve

    c "Aww~ You’re so sweet. This is why I love you."

    "Every day I spend with Chika is one day closer to realizing that she lives in a world of blissful ignorance, where only the things she {i}wants{/i} to hear manage to stick to whatever part of the brain stores memories."
    "Which is great for me, don’t get me wrong. But being that far into dreamland might be a little dangerous, especially when it comes time for her to leave."
    "She...has to realize eventually, doesn’t she? "
    "That even on the days where I want this to be anything more than it is, there’s another side of me buried somewhere in the back of my head mocking me for even pretending it’s real."
    "I just don’t want to be the one to force her into realizing that it’s not...and that this {i}relationship{/i} was all built on one huge misunderstanding."

    if bonus == True:
        "A misunderstanding that is, of course, my fault. And I’m an idiot for thinking that even a teenager as mature as Chika would think like an adult 100%% of the time."
        "But I really can’t just let this go on forever."

        c "Wanna go have sex in your office?"
    else:
        c "Wanna go hug in your office?"

    "A little longer wouldn’t hurt, though."

    s "Yes."

    scene chikalunch8
    with dissolve

    c "Too bad. I’m hungry."

    "I hate girls."

    scene chikalunch9
    with dissolve

    c "Hey, wanna come with me to the cafeteria? We can eat lunch together and no one will think it’s weird because you’re a teacher."
    s "I think me doing things like this is exactly why there are so many rumors apparently spreading about me."
    c "Yeah, but those are just rumors. Rumors are {i}always{/i} going to exist, Sensei."
    c "Like that one about you dating Niki Nakayama. Like, obviously that never actually happened, but people are still saying it."
    s "That did actually happen, though."
    c "Hahah~! Sure it did, Sensei."
    s "Before I offer to call her and prove you wrong, will you tell me why you don’t think it’s true? Am I not cool enough to date an idol?"
    c "I think you’re the coolest guy in the world. And one of the hottest, too."
    s "One of?"
    c "Idols are on another level, though. Especially ones like Niki. They don’t date {i}anyone{/i} because they belong to all of us."

    "Boy, do I have bad news for her."

    s "This was before she became an idol, though."
    c "Well, she wasn’t {i}Niki{/i} before she became an idol. She was just Niki."
    s "Oh, okay. My mistake. I didn’t realize she was possessed by the soul of music."

    scene chikalunch10
    with dissolve

    c "Well, I’m glad I got to be the one to educate {i}you{/i} for once. "

    if bonus == True:
        s "When have I ever educated-"

    c "Now, come with me to the cafeteria and eat lunch with me like the awesome, loving, loyal boyfriend you are."
    s "..."
    c "..."
    s "You know, I’m not really feeling that hungry today."

    scene chikalunch2
    with dissolve

    c "Well, I am. So that sucks for you."
    s "I’m sorry?"
    c "Because you’re coming with me whether you like it or not."
    s "I don’t think this is how relationships are supposed to work."
    c "It’s exactly how they’re supposed to work. Besides, it’s not like anybody is going to come up to us and tell us to like, not eat together or something."
    c "We’re not doing anything wrong. We’re just...making the most of our lunch period since we’re not {i}always{/i} able to spend time together, you know?"
    s "..."
    c "..."

    "I...guess this could be a good time to talk to her about this whole “dating” thing?"
    "Especially now that she’s trying to act like we’re dating {i}in{/i}[school], which is exactly what I wanted to avoid at all costs."
    "And something I thought she’d care a little more about avoiding too, but...it is what it is."

    s "Fine."
    s "But I’m not paying for your food since I’m already paying for your phone bill."
    c "Yeah, yeah. I can buy my own food. I’m a big girl."

    scene black
    with dissolve2

    "Chika tries to grab my hand to lead me down the hall, but I am able to dodge her grasp and inform her that holding hands is a little too much."
    "And by a little, I mean a lot."
    "It’s not like we’re in the lobby of a hotel or a private onsen or anything like that. There are people here."
    "There are times when it’s okay to be clingy and times when it’s not."
    "And while the two of us are fully clothed and out in the open, I’d say the current status of acceptability is far closer to {i}not.{/i}"
    "........."
    "......"
    "..."

    scene chikalunch11
    with dissolve2

    "So, the good thing is that the cafeteria is mostly empty today."
    "The bad thing is that a few of the people who {i}are{/i} here are people that I know. "
    "No one “dangerous” like Ami or Noriko or...anyone else who would get mad at me for sitting with a girl who isn’t them."
    "But there's Yasu, Touka, that one new teacher, and Io- all the way back in the corner of the room, doing her best to assume the role of a socially anxious wallflower."
    "And, even though I can’t see her from where I’m sitting, I’m sure she’s thinking something along the lines of, “Oh, good. They’re still {i}together,{/i}” while, unbeknownst to everyone but me, we’re not."

    c "You sure you’re not hungry? Because I probably won’t finish all of this and you can have whatever’s left of it."
    s "I’m okay. Ami made a big breakfast this morning."
    s "But, Ami makes a big breakfast pretty much every morning, so that’s nothing to really write home about."

    scene chikalunch12
    with dissolve

    c "Yeah...that’s actually super impressive. Like, doesn’t she leave the dorms really early every morning just so she can go home and cook for you? That’s some serious dedication."
    s "Yeah, but I let her live in my house for free, so there’s that too."

    if bonus == True:
        c "Aren’t you also her legal guardian?"
        s "I prefer the term “uncle.”"
        c "..."
        c "Okay, but aren’t you like, {i}legally{/i} her legal guardian?"
    else:
        c "I mean, she does your taxes though, doesn't she?"
        s "I sure hope so. I've yet to see any copies of my returns."
        c "You should let Chinami try doing your taxes next time. She's getting really good at-"

    s "You’re sure talking a lot for someone who was very hungry just a moment ago."

    scene chikalunch13
    with dissolve

    c "All I’m saying is that she...really goes out of her way for you."
    c "It kinda makes me a little jealous."
    c "Like...{i}I{/i} want to cook breakfast for you and like, help out around your house and stuff."
    s "One key difference between you and Ami is that Ami doesn’t have to also take care of a kid. Just me."
    s "Though, I guess there {i}is{/i} Ayane sometimes, and she can be a bit of a handful."

    scene chikalunch14
    with dissolve

    c "Your house sounds really...lively."
    s "Sometimes, yeah. Most of the time, it’s just me and her, though."
    c "..."
    c "I really hate to ask like this...but..."
    c "When I’m like, out of [high_school] and stuff..."
    c "Do you think there’s any chance that maybe Chinami and I could move in with you?"
    c "Like, you won’t have to hide how we’re seeing each other anymore once I’m not a student, and it would definitely help me out since I wouldn’t have to worry about rent anymore."
    s "What about Yumi? Where will she go?"

    scene chikalunch15
    with dissolve

    c "I don’t know. I’m sure she doesn’t expect me to take care of her forever, though. Like...she’s going to {i}have{/i} to find something to do on her own."
    c "And it’s not like I’m going to ask you if she can just come live with us as well when you haven’t even agreed to my sister and me coming yet."
    s "I’d...have to run it by Ami."

    if bonus == True:
        c "Is Ami not leaving for college once she’s out of high school? Is all of that stuff she says about just devoting her entire life to you really true?"
        c "Or do you think maybe she’s just saying that for now and...she’ll change her mind once it’s time to start like, growing up?"
    else:
        c "What if she gets hit by a bus sometime over the next three years? I've been thinking a lot about that recently."

    s "I think that you probably shouldn’t think too much about things that will be happening three years from now when we don’t even know what’s going to happen tomorrow."

    scene chikalunch16
    with dissolve

    c "Yeah? Are you gonna run off with my favorite idol and forget all about me?"
    c "Cause I wouldn’t really blame you. There’s no way I could compete with her."
    s "At the risk of shattering your borderline inhuman expectations of Niki, I’m going to tell you now that she’s probably...not what you think she is."
    c "Yeah, because I’m sure you know her {i}so{/i}, so well."
    s "Well, considering that {i}she is my ex-girlfriend{/i} I think it’s safe to say I know her at least a {i}little{/i} well."

    "Just...only the tsundere parts. Not the ones Niki so desperately wants me to remember."

    scene chikalunch17
    with dissolve

    c "Sensei, I’m not going to believe that! Are you and Noriko working together to spread this rumor or something?"
    c "Because if I believe this one, I’ll have to start believing the ones about how you’re secretly seeing like half of our class. Or how you and Maya-"

    scene chikalunch18
    with dissolve

    c "Wait, weren’t you looking for Maya when I bumped into you in the hall?"
    s "Nope. But back to the topic of Niki, we really did date in high school."

    scene chikalunch19
    with dissolve

    c "Yeah, okay. I mean, I obviously don’t have a problem with it, but aren’t you in your thirties? How would you have dated Niki in high school if she’s like, ten years younger than you?"
    s "Chika, just out of curiosity, how old do you think Niki is?"

    scene chikalunch20
    with dissolve

    c "She’s 22 and her birthday is March 3rd. Her favorite color is pink (Shocker, I know) and if she could live anywhere in the world, it would be Hawaii."
    s "And where did you get that information?"
    c "Fan books...online...interviews. The info is all over the place, Sensei. At least do your research before trying to make me think you dated my role model."

    "Well, if nothing else, Niki was certainly right about the idol industry being ruthless and cutthroat. "
    "I’ll have to add this newfound revelation to the exposé I’m writing."

    s "Chika, Niki is 29 years old. Only a couple years younger than me."

    scene chikalunch21
    with dissolve

    c "Oh, please. She’s 29 and she still looks like {i}that?{/i} Funny joke, Sensei."

    scene chikalunch22
    with dissolve

    if bonus == True:
        c "Besides, if I ever found out that my lips have been on the same penis as Niki's, I’d probably bite it off out of excitement."
    else:
        c "Besides, if I ever found out that I hugged someone Niki hugged, I’d probably just kill myself right there since life couldn't possibly get any better."

    s "..."
    c "..."

    scene chikalunch23
    with dissolve

    c "Sensei, come on! I’m obviously joking! "

    if bonus == True:
        s "Chika, there are certain things in life that you really just shouldn’t joke about...and biting someone’s penis off is one of them."
        c "Don’t worry. I like your penis too much to bite it off."
        s "I am very relieved to hear that. Now, if only you’d stop acting like that during the day at school."
    else:
        s "Chika, there are certain things in life that really just shouldn’t joke about...and suicide is one of them."
        c "Don't worry. I would never {i}actually{/i} do something like that."
        s "Good. Also, stop liking me so much in public. It makes me feel weird."

    scene chikalunch24
    with dissolve

    c "What do you mean?"
    s "Just that {i}this{/i} was supposed to be a little more secretive than eating lunch together and trying to hold my hand in the hallway."
    c "Well, gee. Sorry for being in love with you. I don’t really see what the big deal is."
    s "The “big deal” is that you could get me in trouble."
    s "You could get {i}both{/i} of us in trouble."
    s "And if you’re not going to respect that-"

    scene chikalunch25
    stop music

    c "Wait....Are you breaking up with me?..."
    s "Woah, hold on a second."
    c "Why?"
    c "What did I do wrong? "
    c "Is..."
    c "Is this because I asked to move in with you after [high_school]?"

    scene chikalunch26
    with dissolve

    c "You can say no! I didn’t mean to move so fast!"
    c "Oh god, no. I really wasn't trying to-"
    s "Chika, calm down."

    scene chikalunch27
    with dissolve

    c "..."
    c "I'm sorry. "
    c "I just thought that you were about to give me like...an ultimatum or whatever..."
    c "Then it clicked that I just asked about moving and..."
    s "..."
    c "..."
    c "Are we okay?..."
    s "We won’t be if you don’t stop crying."
    s "People are going to start thinking something is going on which, need I remind you, is exactly what I’m trying to avoid."
    s "But we can forget about that for now..."
    s "You still haven’t eaten. Your food is going to get cold."

    scene chikalunch28
    with dissolve

    c "..."
    c "Yeah."
    c "I’m...suddenly not very hungry anymore..."

    scene black
    with dissolve2

    "The rest of the lunch period goes by in mostly silence as I realize how foolish I was for even {i}thinking{/i} that now would be a good time to tell Chika to tone it down."
    "And, at this point, I’ll be lucky if {i}any{/i} time winds up being a good time to tell her that."
    "The worst part is that I want to blame {i}her{/i} for all of it."
    "I want to blame her for misunderstanding what I wanted out of our time together...and painting me into a portrait of the family she’s always wanted."
    "I’m the one who handed her the brush, though. And blaming her for using it just makes me question why I ever gave it to her in the first place."
    "She loves that portrait so much, though. So how am I supposed to tell her I hate it?"
    "It doesn’t matter now, I guess."
    "I’ll just keep putting it off."
    "The same way I've been doing from the start."
    "But, hey. At least on the bright side-"
    "I’m one day closer to summer."

    $ renpy.end_replay()
    $ chika_love += 1
    $ chikaspecial40 = True

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label mall40:
    scene chikashopping1
    with fade
    play music "mall.mp3"

    "I head to the mall for the afternoon and, like clockwork, Chika immediately finds me and makes her way over."
    "Surprisingly enough, she’s able to abstain from grabbing onto me and actually shows some restraint this time."
    "And all it took was making her think I was about to break up with her."
    "It’s funny how people are willing to change once you threaten to take away the things they love."
    "And it’s even funnier when you don’t even have to get the full threat out of your mouth in order to do that."
    "Anyway, here’s hoping I don’t have to break her heart again today in order to get her to act how I want."

    c "Hey! Great timing."
    s "Leave it to me to show up right when you clock out for break."

    scene chikashopping2
    with dissolve

    c "Actually, I’m not even working today. "
    s "Did you get fired after customers complained about the adult male constantly hanging around the store hitting on you?"

    scene chikashopping3
    with dissolve

    c "I don’t really think that’s something I would get fired for. If anything, people would probably just call the cops thinking you’re harassing me."
    s "Fair point. If you’re not fired, though, why bother spending time at the mall? Don’t you see enough of this place?"

    scene chikashopping4
    with dissolve

    c "Coming to the mall as an employee and coming to the mall as a customer are two completely different things, Sensei."
    c "You probably just don’t understand because you wear the same thing every day."
    s "But...so do-"
    c "Anyway, I came here with Yumi and Chinami, but the two of them are off doing something else right now."
    s "Well, why aren't you with them?"
    s "You weren’t wandering around in hopes that I’d just show up, were you?"
    c "I mean, I’m kind of always hoping you’ll show up. But nah, I’m just shopping."
    s "Since when do you have the money to shop?"
    c "Since you started paying for my phone, obviously. Plus, I’ve been picking up a lot more hours since it’s getting close to Christmas."
    c "So, I figured why not treat myself to a little present?"
    s "Hmm..."

    scene chikashopping5
    with dissolve

    c "Why {i}hmm?{/i} What did I do this time?"
    s "I just figured you’d be using that money on stuff for Chinami."

    scene chikashopping6
    with dissolve

    c "I...I am! I just wanted to get something for myself, too! "
    c "What’s wrong with a little self care to make yourself happy every once in a while?"
    s "Well, nothing’s {i}wrong{/i} with it. You’re free to use your money however you want."

    scene chikashopping7
    with dissolve

    if bonus == True:
        c "Good. Because I’m tired of seeing Noriko and Touka with their fancy underwear in the locker room. It’s making me feel like some kind of...lower class blob."
        s "If it’s any consolation, I think you look great in your-"

        scene chikashopping8
        with dissolve

        c "No! I want to feel sexier!"
        s "Why? I’m pretty sure that neither of those girls are looking down at you for not being able to afford the things they can."
        s "Who cares about what they think?"

        scene chikashopping9
        with dissolve

        c "It’s not {i}just{/i} about what they think."
        c "I wanted to like, you know...surprise you and stuff."
        c "And even if like, nobody else can see what I’m wearing under my clothes, having something nicer under there would make me feel...more desirable and stuff."
        c "I don’t know. It’s probably dumb."
        s "Nah. I get it now that you’ve explained it like that."
        s "Plus, this finally gives me the chance to see you modeling lingerie for me, and I have been waiting for that for a very long time."
    else:
        c "Good. Because there's this one clown costume I really like and-"
        s "Say no more. Let's go."

    scene chikashopping10
    with dissolve

    c "Really?! You’ll come with me?!"

    if bonus == True:
        s "Are you really that surprised that I’m agreeing to come see you with less clothing on? Because that’s one of my absolute favorite things to do."
    else:
        s "Are you really that surprised that I’m agreeing to come see you in a clown costume? I've been trying to do this for ages."

    c "I’m not really surprised at all. I’m just happy. "

    scene chikashopping2
    with dissolve

    c "Plus, it means I can finally show you something I’ve been keeping a secret for a little while now."
    s "That is...both alluring and mildly suspicious?"
    c "It’s nothing huge- just something I’ve wanted for a long time that I finally pulled the trigger on."

    if bonus == True:
        c "Now, hurry up and follow me if you want to see me in my underwear."
    else:
        c "Now, all aboard the Chika express if you're ready for a honkin' good time."

    scene black
    with dissolve2

    s "What, are we not just going to the store you work at?"
    c "Not today. There’s a sale at this other place on the opposite end of the mall and I want to check out what they have."

    "Chika tries to reach for my hand, probably out of instinct, but manages to catch herself before following through with it."
    "I’m sure it’s a weird position to be in for her- like she’s being pulled in two different directions at once."
    "On one hand, I’m constantly telling her to be careful about giving ourselves away and doing everything in our power to keep this a secret..."

    if bonus == True:
        "But, on the other hand, I’m now following her through a semi-crowded mall during the holiday season in an attempt to watch her try on new underwear."
    else:
        "But, on the other hand, clowns."

    "I’m a little annoyed at myself for this, but I ultimately choose to stop caring for at least a little while."
    "Eventually, Chika leads me into a store that definitely does not sell anything for men and starts browsing through a few racks of clothing."
    "She quickly dismisses most of the stuff she sees, and in the process of doing so, I can make out some of the price tags."
    "I breathe a sigh of relief knowing that it’s nothing expensive and that she isn’t just throwing away her money to try and impress me."
    "And I don’t know if her pride is just too strong to admit it, but I’m willing to put money on the fact that she’s only here because the sale they’re having is making everything semi-affordable."
    "I guess there’s no point in putting money on anything when there’s no chance for a return, though."

    scene chikashopping11
    with dissolve2

    "In fact, with the way Chika is looking at me, I’m beginning to think that there might be money to be {i}lost...{/i}"

    s "..."
    c "..."
    s "What? Why are you looking at me like that?"
    c "Like what?"
    s "Like you’re trying to seduce me."

    if bonus == True:
        s "You know we’re past that, right? Seduction serves no purpose anymore. I’m already very attracted to you."
    else:
        s "I have no interest in that sort of sinful relationship."

    c "Oh yeah?"
    c "Then, before I try stuff on, I’d like to make you a little trade offer."

    "Here it comes- the inevitable loss of income."

    if amifingered == True:
        "I hope Ami never learns this trick."

    c "So...I found something that I really like, but it’s a little out of my price range."
    s "..."
    c "And what I was thinking was..."

    scene chikashopping12
    with dissolve

    c "You could maybe buy it for me?"
    s "..."

    if bonus == True:
        s "Is there another end to this trade? Or are you just asking me to buy you underwear for nothing in return?"
    else:
        s "Is there another end to this trade? Do I get anything?"

    scene chikashopping13
    with dissolve

    if bonus == True:
        c "If you buy it for me, I’ll let you fuck me in the dressing room."
    else:
        c "If you buy it for me, I’ll let you hug me while I'm wearing it."

    s "..."
    c "..."

    "You know, this is starting to sound like a pretty good investment after all."

    s "Fine, but..."
    c "But what? "
    c "Nervous that we’ll get caught?"
    s "I think that’s a pretty reasonable thing to be nervous about."

    scene chikashopping14
    with dissolve

    c "It’ll be fine. The girl working here still owes me a favor from when I gave her a tampon."
    s "I feel like you’re getting a much bigger favor out of this than she did."
    c "It was a while ago, so I’ve accrued interest or whatever. "
    c "So, what do you say? "
    c "Wanna do it?"

    if bonus == True:
        c "It’s pretty cramped in there, so you’ll probably have to fuck me up against the wall, though."
    else:
        c "It’s pretty cramped in there, so you’ll probably have to hug me really tightly, though."

    s "Oh no. However will I survive?"

    scene chikashopping13
    with dissolve

    c "Heheh~"
    c "Who says you will?"

    scene chikashopping15
    with dissolve

    s "..."
    s "Chika, that’s a really weird thing to say before luring me into a private room."

    if bonus == True:
        jump mall40x
    else:
        scene black
        with dissolve
        stop music fadeout 8.0

        "Chika pulls aside the curtain to the dressing room, but it is filled with chickens and there is nowhere for her to put on the clown costume. She says the shoes are too large."
        "Not knowing what else to do, we decide to play with the chickens for a little while. But then Yumi and Chinami show up and we have to stay quiet because we want to keep the chickens to ourselves."

        jump mall40p2

label mall40p2:
    if _in_replay:
        play music "asobeatsex5.mp3"
        scene dorm

    if bonus == True:
        scene chikawallfuck1
        with dissolve2

        "I’m able to slip inside of her with no resistance whatsoever."
        "In the midst of our connection, we knock over a coat rack that comes dangerously close to falling directly into the curtain separating us from the general public."
        "And while I would have expected to {i}fear{/i} something like that given that it could demolish one of the many illicit relationships I'm involved in-"
        "I fear nothing at all."
        "I simply sink into Chika as her lower body beckons me forward, pulling me in like it’s where I belong."
        "And, at the risk of detracting from the mood-"
        "Right now, I think it {i}is{/i} where I belong."

        c "Ahh! Ahh! Agh! Yes! Just...like that! [chikamaster]!"
        s "Keep it down. There are people right outside of the curtain."

        scene chikawallfuck2
        with dissolve

        c "Mmf...mmm......ngh...yes...[chikamaster]...whatever you say..."
        c "Guess you wouldn’t want...everybody seeing you fuck a high schooler...huh?..."
        s "I...don’t think you’d want anyone here seeing that either..."
        c "Ngh...mnf...I don’t...care if...they think I’m a slut..."
        c "I should...ahh...be able...to take my boyfriend’s big cock...whenever I want~"
        c "And I wanted it...so bad, [chikamaster]...so, so bad...I thought I was going to explode without it..."
        s "You practically did. Why do you think I picked you up?"
        c "Heheh~ Were you jealous I might cum without you?"
        s "..."

        scene chikawallfuck3
        with dissolve

        c "Hah...ahh...well...don’t...worry about that because...because I...I’m definitely..."

        scene chikawallfuck4
        with dissolve

        c "Ahh! Yeah! Just like that...fuck me, [chikamaster]...fuck me...make me cum...make...me..."

        scene chikawallfuck5
        with hpunch

        c "Ahh! Yeah! Yeah! Fuck! Fuck! Fuck!!!!!"

        "Chika begins convulsing as I continue to plow away at her, and it appears that she may have jumped this gun this time around."
        "I mean, I kind of expected that considering how close she was before we started, but I would have appreciated it if her climax involved less screaming at the top of her lungs."

        s "You’re...going to give us away..."

        scene chikawallfuck6
        with dissolve

        c "I can’t help it, [chikamaster]. I just love the way you fuck me...I love it so...so much..."
        c "I love the way your huge cock feels inside of me. Don’t you like it too, baby? Does my pussy feel good? Doesn’t it make you wanna fuck me harder?"
        s "Chika-"
        c "Do it, [chikamaster]. Fuck me harder. See if you can make me...cum again before you do..."
        c "It’ll probably be easy for you since...you’re so...fucking good...oh my {i}God,{/i} yes..."

        "It starts getting a little harder to effectively fuck Chika, as with each passing moan, she starts losing control over her body."
        "And having to continuously prop her up every few seconds so she doesn’t slip and take me down with her is starting to take a toll on my energy."

        scene chikawallfuck7
        with dissolve

        c "Mmm...holy shit...I really...can’t get enough of this..."
        c "You’re so hot, [chikamaster]...the way you can...keep me held up like this...and not even slow down..."

        "Welp, that compliment does enough for my ego that it’s guaranteed us at least a few more minutes."
        "Frankly, though, I’d still prefer to just pin her down on the ground instead. But I’m pretty sure that might be harder to conceal because of the gap in the curtain beside us."

        c "Mmf...fuck...baby...I can’t wait...for you to cum in me...it’s making me...so fucking hot..."
        s "I’m glad that you consistently seem more excited for me to cum than you. That’s a nice quality."

        scene chikawallfuck8
        with dissolve

        c "Hah...hah...yeah?...You like that, [chikamaster]?...You like when I beg for your cum?"
        c "You like...relieving yourself inside of my...tight, schoolgirl pussy?"
        s "..."
        c "What’s the matter?...You’re not starting to get gun shy because of all of the people outside, are you?"
        c "Want me to scream so loud that they’re {i}forced{/i} to hear us?"
        s "Absolutely not. Don’t even think about it."

        scene chikawallfuck9
        with dissolve

        c "Hah...ahh! But what if I...want them to find out?...What if I...want them to see me beg for my teacher’s cock?..."
        s "Chika, I’m not kidding."
        c "Ahh...hah! Neither am I! I’m your...little cumslut, [chikamaster]! What good am I if...no one knows it?..."
        s "What good are you if someone catches us and we can’t do this at all anymore?"
        c "I’ll...wait for you...forever, [chikamaster]..."
        s "What? No. I don’t want there to be any waiting involved. That’s a horrible thing to say."

        scene chikawallfuck10
        with dissolve

        c "Then...shut me up with that big cock of yours..."

        "Chika tightens her legs around my back and pulls me in as deep as I’ll go, once again proving that she has no limit to the amount of both pain and penis that she can handle."

        scene chikawallfuck11
        with dissolve

        c "Ahh.....guh...fuck...yeah..."
        c "It’s so deep...[chikamaster]...I can’t even...feel my legs anymore..."
        s "Well, whatever you do, don’t move them because it could result in me breaking something I definitely don’t want to break..."
        c "I’ll do...whatever you want me to do...[chikamaster]...just...keep fucking my pussy..."
        c "I’m..........oh....God....."
        c "I’m...gonna......."

        scene chikawallfuck12
        with hpunch

        c "Ahhhhhh!!!! Ahhh! Yeah! Yeah!!! [chikamaster]! [chikamaster]!!!"

        "Chika explodes into yet another orgasm and I’m immediately jealous of how she was able to get two out of the way before I could even have one."
        "At this rate, she may very well orgasm herself to death before I get to cum inside of her, and that just sounds completely unfair."

        c "Ah! Ahh!......Ahhh! Yes! Right there...Just...like that!"
        c "So...deep...holy shit...you’re so big, [chikamaster]...your...fucking cock is so big..."
        c "I love it...I love it so fucking much..."
        s "Yeah?"

        scene chikawallfuck13
        with dissolve

        c "Yeah..."
        c "There’s nothing...in the world...that can make me feel even...half as good as this..."
        s "Then shut the fuck up and stop almost giving us away."
        c "Don’t get...snippy with me, [chikamaster]...you agreed to...fuck me in here..."
        c "You know how much I love your cock. Of course I’m going to get a little loud."
        s "That’s-"

        scene chikawallfuck14
        with dissolve

        c "Blah blah blah. Take it out on my pussy, not me. You can lecture me after you cum."
        s "You really need to-"

        scene chikawallfuck15
        with dissolve

        y "Chinami! I told you I ain’t buyin’ you new fuckin’ clothes! I don’t have any money!"
        ch "Chinami just wants to look! She already knows how poor big sis Yumi is!"
        c "Oh my God. Did you hear that?"
        s "Yes, and I’m glad they decided to show up now instead of during one of your multiple orgasms."
        c "Hah...ahh...what do we do?"
        c "Are you gonna keep fucking me? How close are you?"
        s "I’m...getting there."

        scene chikawallfuck16
        with dissolve

        c "You sure took your time today."
        s "Yeah, well, this isn’t exactly the most comfortable position."
        c "Cum for me, [chikamaster]."
        c "I’ll be quiet. I won’t say a single word until you let it out. I promise."
        s "That’s what you should have been doing from the start."
        c "..."

        "Chika doesn’t reply, just looks up at me with anticipation and what is...annoyingly and unmistakably love in her eyes."
        "Her legs loosen up a bit and allow me some more control."
        "I stabilize myself and prop her up in a way that lets me slide in and out of her without any intense bouncing, creating a consistent stimulus that brings me to the brink of orgasm."

        s "Not...much-"
        ch "Wow! That purse looks just like big sister’s!"
        y "Hm? The one near the dressing room?"
        s "Why the fuck did you leave your purse {i}outside{/i} of the dressing room?"
        c "..."
        y "Wasn’t Chika’s more...pink?"
        ch "No! Chinami knows that’s hers because of the keychain on it!"
        ch "Big sister! Are you in there? Your darling Chinami wants to say hello!"
        y "Yo! You can’t just go in there! What if it ain’t her?!"
        c "...!"
        s "{i}You can respond, Chika.{/i}"

        scene chikawallfuck17
        with dissolve

        c "NOT RIGHT NOW, CHINAMI! YOUR SISTER IS BUSY WITH SOMETHING!"
        ch "Busy with what?! You are supposed to check in with Chinami every ten minutes and you have been gone for forever!"

        "This is probably a bad time to say that I’m about to cum."

        ch "Chinami is bored! Chinami wants tacos!"
        c "Chinami can...mm! Get tacos in a minute!"

        "Like, really. This is going to happen mid-conversation and there’s nothing I can do about it."

        y "Hear that, twerp? Now, come on. Let’s leave her alone."
        ch "Ahhhh! Fine! Goodbye, big sis Chika!"
        c "Bye, Chinami! Don’t forget to-"

        scene chikawallfuck18
        with hpunch

        c "HAAAAAAaaaaaAAAAAAaaaaaAAAaaaaAAave fun with Yumi!"

        "Excellent save, Chika. This almost redeems giving us away on roughly fifty occasions in the last fifteen minutes."

        ch "Okay! Bye! See you soon!"
        c "Hah...hah.......holy shit...oh my God..."
        c "I can’t believe you just.......while I was......"
        s "Yeah, well..."
        s "Sorry?"

        scene black
        with dissolve2
        stop music fadeout 8.0

        "Chika and I wait a moment before putting our clothes back on, making sure that Chinami and Yumi have had enough time to get far, far away from this store."
        "Then, once we’re sure the coast is clear, we step back into the store, ready to carry on with our day as if nothing ever happened."
    else:
        "Eventually, the two of them leave and our chicken time expires."

    scene chikawallfuck19
    with dissolve2

    if bonus == True:
        "Yup. Just like nothing ever happened."

    y "..."
    c "..."

    if bonus == True:
        ch "Chinami knew something weird was going on! That’s why she had big sis Yumi stay quiet and wait out here!"
        ch "What were you two doing in there?! You don’t even have any clothes with you!"
        c "We left them inside, Chinami."
        ch "Likely story! You’re grounded, missy!"
        y "..."
        s "..."
    else:
        ch "Where are the chickens, you bastards?!"

    scene chikawallfuck20
    play music "mall.mp3"

    c "So, how is everybody’s afternoon going?!"
    s "..."
    y "..."
    y "Good."
    y "It’s...going pretty good."
    ch "Can Chinami still have tacos? Conducting a stakeout really works up an appetite!"

    scene chikawallfuck21
    with dissolve

    c "Yes, Chinami. You can still have tacos."
    c "In fact, how about all {i}four{/i} of us get tacos?"
    y "..."
    s "..."
    ch "Hooray! Taco party!"
    ch "Does Chinami have to wait until she gets home to eat? Or can she put the tacos inside of her dog helmet?"
    c "Chinami has to wait until she gets home to eat so the evil mall germs don’t get her."
    ch "Rats!"
    y "..."
    s "..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene chikawallfuck22
    with dissolve2

    s "..."
    c "What? Why are you being all silent when we’ve had a totally normal day where nothing weird happened?"

    if bonus == True:
        s "Are you...still wearing the bra you picked out inside of that store?"
        c "Hm? Yeah. Why?"
        s "I just...I never paid for it."
        c "Oh, nice. Free underwear."
        c "This means you got a little reward for no payment at all {i}and{/i} I get to feel sexier from now on. We both win."
        s "When do you think Yumi will be able to talk again?"
        c "Yumi? Probably the first time something annoys her. And since she’s with Chinami, maybe like...ten minutes?"
        s "Fair enough."
        s "Do we really have to eat lunch with them, though?"
    else:
        s "I want to hug again."

    scene chikawallfuck23
    with dissolve

    c "What? One helping of me wasn’t enough? You want to go find {i}another{/i} dressing room to fool around in?"
    s "No. But I would like to have a private conversation with you about something."

    scene chikawallfuck24
    with dissolve

    c "Another one?..."
    s "I don’t think it will take long, but it has to happen."
    s "And, since you managed to shoplift and save me some money, how about I buy you lunch after we’re done?"
    c "...Done?"
    s "With the conversation."
    c "Oh."
    c "Okay..."
    c "Sure..."

    scene black
    with dissolve2

    "Chika and I split apart from Yumi and Chinami so they can go back to taco hunting."

    if bonus == True:
        "As it turns out, the two of them had spent the afternoon window shopping due to lack of money while Chika was off getting railed in a dressing room."
    else:
        "As it turns out, the two of them had spent the afternoon window shopping due to lack of money while Chika was off playing with chickens."

    "And, in other news, I think we can all agree that Chika had the better day."
    "Well, until now that is."
    "But I guess we can wait until the two of {i}us{/i} get lunch to really make our final decision."
    "........"
    "......"
    "..."

    scene chikawallfuck25
    with dissolve2

    s "..."
    c "..."
    c "Can you say something? This is making me really nervous..."
    s "I’m trying to figure out how to say what I want to say in a way that won’t make you cry."
    s "The more I think about it, though, the more I realize how hard that is to do."
    c "..."
    s "Basically-"
    s "You really need to slow down."
    s "Like...way down."

    scene chikawallfuck26
    with dissolve

    c "Slow...down?..."
    s "Again, {i}way{/i} down."

    scene chikawallfuck27
    with dissolve

    c "So..."
    c "You’re {i}not{/i} breaking up with me, then?"
    s "..."
    s "No."

    scene chikawallfuck28
    with dissolve

    c "Oh, thank God. The second you told me you wanted to talk, I thought it was coming."
    s "..."

    scene chikawallfuck29
    with dissolve

    c "Okay."
    c "I’ll do it."
    c "I’ll slow down. And I’ll be serious about it this time."
    c "Not just in school, but everywhere public. The mall, the...park? I don’t know. Anywhere the two of us meet that isn’t my apartment."
    c "As long as I have that...I’ll be okay."

    scene chikawallfuck30
    with dissolve

    c "Honestly, almost getting caught by my sister back in the dressing room was...weirdly enough, kind of the wake up call I needed."
    c "I’ve just...never had a boyfriend before. And I keep wanting to do stuff to impress you and...and stuff that I think will bring us closer together..."
    c "But...I didn’t even think about how clingy that may have made me seem. And I’m better than that. I {i}know{/i} I am."
    c "I {i}have{/i} to be."
    s "You don’t {i}have{/i} to be anything."
    s "You accomplish more on your own than pretty much anyone else I know. I don’t expect you to be perfect 100%% of the time."
    s "If the world was okay with it, I’d be {i}fine{/i} with you clinging on to me all day long."

    "Another half truth- my specialty."
    "Frankly, I don’t care much about what the world thinks."
    "But I {i}do{/i} care about what the people directly surrounding me- the ones I see every single day think."
    "Not in the sense that I want them to worry about me or anything as sentimental as that."
    "But in the sense that my life would be much more difficult if most of them were to find certain things out."
    "I’m sorry, Chika."
    "And I’m sorry everyone else for having to hide all of this."
    "Until recently, I never even imagined thinking something like that because, while many people struggle with apologizing, I struggle with even {i}wanting{/i} to."
    "It’s a part of myself I’m not proud of."
    "But, then again, there are very few parts of myself that I {i}am{/i} proud of."
    "So I should at least take solace in the fact that, right now, my heart is a little closer to the right place than it normally is."
    "Or at least I think so."
    "It's near impossible to ever confirm things like that."

    s "It’s just that, the more time we spend together...the riskier you’ve been making things."
    s "I don’t want you accidentally sabotaging something that I think both of us...really like."

    scene chikawallfuck31
    with dissolve

    c "Hearing you say it that way is...kind of like having the world lifted off of my shoulders."
    c "Like, I never dreamed in a million years that I’d worry so much about a boy, but..."
    c "I’ve fallen for you, Sensei..."
    c "I’ve fallen really hard."
    s "..."

    scene black
    with dissolve

    s "Well-"
    s "I’m glad the fall didn’t kill you."

    "I buy Chika lunch, as promised."
    "She stays five to ten feet away for the rest of the afternoon."

    $ renpy.end_replay()
    $ mall40p2 = True
    $ chika_love += 1
    $ chika_lust += 1
    stop music fadeout 8.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "{i}Chika’s lust has increased to [chika_lust]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chikadate45:
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "And, since it’s still early in the day, I figure that meeting up with her now will give her the chance to {i}not{/i} have to monitor her instinct to always act like we’re the world’s cutest couple."
    "She’s been having to do a lot of that lately. And...let’s just say that I’ve been a little closer to feeling bad than I normally am after telling her to tone it down."
    "A break can be good for everyone."
    "Depending on the {i}type{/i} of break, of course. Because I’m pretty sure if I asked Chika to take a {i}real{/i} break, all hell would break loose."
    "But that’s enough iterations of the word “break” for the moment. "
    "Here’s hoping she’s awake, I guess."

    play sound "phonebeep.wav"

    c "Hey! Good morning!"
    s "Hey. You sure seem lively for someone who probably just woke up."
    c "Chinami wanted waffles, so I had to run over to the store to get stuff for them."
    s "Stop letting her control your life. If you don’t want to make waffles, don’t make waffles. It’s as simple as that."
    c "Do you...have something against waffles, Sensei?"
    s "I have something against eternal kindness. And waffles just appear to be the connection between that and you this morning."
    c "Do you want me to be meaner to Chinami or something?"
    ch "{i}Who wants to be mean to Chinami?! She wants to give them a piece of her mind!{/i}"
    c "Shush. Eat your waffles."
    ch "{i}Okay! I love you, big sister!{/i}"
    c "Do you hear that? {i}That’s{/i} who you want me to be mean to."
    s "I never said-"
    s "You know what, forget it. Are you busy this morning?"
    c "Nope!"
    s "Sweet."
    c "Mhm. I guess it is pretty sweet."
    s "..."
    c "..."
    s "This is the part where you’re supposed to invite me over."
    c "Is it? I wasn’t sure if that would be moving too quickly."
    s "..."
    c "Sensei! It was a joke! Of course you can come over."
    c "I’m not making you waffles unless you bring more ingredients, though."
    s "I think I’m okay without waffles. I’ll see you soon."
    c "We’ll be here!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and start getting ready to head to Chika’s place."
    "When I make it to the second half of town, I see a surprising amount of its inhabitants showing a bit more life than they normally do at this time of day."
    "Upon trying to come up with a reason for their sudden shift in behavior, I decide to go with the simple fact that the seasons are changing."
    "And that, soon enough, they’ll be wandering around in search of shade or shadows instead of fire. "
    "Good luck, old district. I wish you the best in your endless battle against death and nature. "
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene controversialscene1
    with dissolve2
    play music "love.mp3"

    "I step into the Chosokabe apartment to find absolutely no one."
    "Could it be that Chika was so torn up about me asking her to slow down that she took her sister and moved to some far away land?"
    "And, if that’s the case, why did she invite me here? Is this all just to inconvenience me?"
    "That bitch."

    play sound "water1.mp3"

    c "In here, Sensei!"
    s "The bathroom?..."
    c "Don’t worry! It’s safe to come in."

    if bonus == True:
        jump chinamibrx
    else:
        scene black
        with dissolve

        "I make my way into the bathroom and, to my great surprise, there are chickens again."

        s "Why does this keep happening?"
        ch "It's Chicken Day, Papa! Here! Take one!"

        "Chinami hands me a chicken."

        s "Thank you."

        "I accept the chicken."
        "We all dance around in circles for a little while before the chickens have to go home, then the event continues."

        jump restofchinamibr

label restofchinamibr:
    scene controversialscene14
    with dissolve2

    "Chinami jumps onto the bed next to me, wearing nothing but an oversized t-shirt, before gazing into my eyes with a look that essentially screams, “I am secretly evil.”"

    c "Chinami, come on. That’s my spot."
    ch "Chinami wants to know what your intentions are with her big sister."
    s "Chinami should mind her own fucking business."

    scene controversialscene15
    with dissolve

    ch "Did you just curse at Chinami?! You can’t do that!"
    ch "Go put all of your money in the swear jar!"
    s "Do you actually have one of those things?"
    c "Why else do you think Yumi is so poor?"

    scene controversialscene16
    with dissolve

    c "Oh crap. I can’t believe I just made that joke. I’m sorry, Yumi. If it makes you feel any better, I’m also poor."
    ch "While big sis Chika apologizes to the air, Chinami demands that you be nicer to her in the future."
    s "To you? Or to your sister?"
    ch "Yes."
    s "Oh."
    s "Well, uhh...okay."
    ch "Good."
    ch "Chinami will give back her sister’s spot now, but she’ll be watching you..."
    s "Sure, Chinami. And I’ll make sure to drop a coin in your swear jar the next time I have cash on me."

    scene black
    with dissolve2

    "Chinami gets off the bed and, within a matter of seconds, Chika stops apologizing to the spirit of Yumi for calling her poor and lays down beside me."
    "She rests her head on my lap and talks a little about how she really doesn’t want to go into work later because of the holiday rush, and I sit there the same way I always do and pretend to be interested."
    "Before long, though, the conversation begins to die down and more gaps begin to form- ones even larger than the half-open bathroom door that she and her sister emerged from just a short while ago."
    "But I guess there have been plenty of gaps forming between us as of late."
    "Gaps between what we want to do and what we have to do."
    "Gaps between what we {i}actually{/i} do and what we struggle to."
    "Gaps in our own personal mindsets as they sink further into a pit that will be near impossible to climb out of if neither one of us has climbing equipment."
    "Chika didn’t bring hers as she believed me to be some sort of experienced climber."
    "And I am."
    "But the truth is that I don’t even know how to use my equipment."
    "And, at this point, I don’t know if it’s even worth the effort to learn."

    scene controversialscene17
    with dissolve2

    "The biggest gap of all is one of consciousness as Chika passes out on my lap."
    "I don’t mean to, but somewhere along the line, I rest my hand on her head and begin stroking her hair."
    "It’s slightly damp, so I’m able to figure out that she took a bath before Chinami."
    "But, with that {i}and{/i} a trip to the store...just how early did she have to wake up?"

    scene controversialscene18
    with dissolve

    ch "..."
    s "..."
    s "Yes, Chinami?"
    ch "Nothing."
    ch "Chinami is just happy you’re here."

    scene controversialscene19
    with dissolve

    ch "Big sis hasn’t been sleeping much lately. But she was able to fall asleep on you right away."
    ch "She must really, really like you."
    s "..."
    s "Yeah. She must."

    scene controversialscene20
    with dissolve

    ch "Can Chinami tell you a secret?"
    s "Chinami is probably going to tell me anyway, so yeah."
    ch "Well, last night, Chinami woke up in the middle of the night because she was thirsty, but she never got out of bed."
    s "What a fascinating secret. Thank you, Chinami."
    ch "No, no. You don’t understand."
    ch "Chinami didn’t {i}want{/i} to get out of bed because her sister was crying."

    scene controversialscene21
    with dissolve

    ch "So she just pretended to stay asleep and hugged her instead."
    s "..."
    ch "..."
    ch "Did you two get into a fight?"
    s "..."
    s "Something like that."
    ch "Does this mean you’re going to stop coming over?"
    s "No, it doesn’t."

    "Not...now, at least."
    "I have no idea what’s going to happen in the future-"
    "Or what other gaps will form."

    ch "That’s good."

    scene controversialscene22
    with dissolve

    ch "Chinami likes when you’re here. And she doesn’t want to hear her sister cry anymore."
    s "Do you have to hear that often?"
    ch "Not really."
    ch "Not since Mommy died."
    ch "But Chinami thinks big sis Chika will stop crying as much if you tell her you love her."
    s "..."
    ch "Or give Chinami a little sister."
    s "Okay, stop that."
    ch "Chinami will convince you one day."
    s "If Chika had a baby, it wouldn’t even be your sister. It would be your [niece]."

    scene controversialscene23
    with dissolve

    if bonus == True:
        ch "Chinami would be an aunt?!"
        s "Yes. And you’re way too young to be an aunt."
    else:
        ch "What?! How does that work?!"
        s "It just does. Don't question it."

    ch "This is a really sticky situation!"
    s "That’s right. So, for everyone’s sake, please stop asking me to have a baby with your sister."

    scene controversialscene24
    with dissolve

    ch "Fine! But Chinami isn’t happy about it!"
    s "Chinami seems to very rarely be happy about anything I do."

    scene controversialscene25
    with dissolve

    ch "Then make it up to her by not letting big sis cry anymore."
    ch "Chinami can only do so much to cheer her up all alone. She needs your help."
    s "..."
    ch "..."
    s "I’ll see what I can do..."

    scene black
    with dissolve2

    "Chinami lays down beside her sister and falls asleep as well."
    "Next thing I know, I’m surrounded by two lightly breathing, unconscious blondes and unable to figure out a way to escape this situation."
    "Not that it’s a bad one, just...not how I imagined my morning going."
    "But, I guess there are more ways to ensure that these two get a good night’s sleep than just buying them a brand new bed."
    "Or...good morning’s sleep."

    s "..."

    "I’ll just hang around here until they wake up, I guess."

    $ renpy.end_replay()
    $ chika_love += 1
    $ chinami_love += 1
    $ chikadate45 = True
    stop music fadeout 8.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "{i}Both sisters wake up a few hours later and you’re able to get on with the rest of your day...{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chikalust25skip:
    scene poorgirldoggystyle1
    with dissolve

    c "So, now what? "
    c "We’ve got like forty-five minutes before we need to start heading over to the next contest. And I’m pretty sure the Tsukioka kitchen staff is setting up a buffet for everybody before that happens."
    c "If you don’t have anything else going on, want to head over there with me? "
    c "Or would you rather I walk ten steps behind you the whole way so no one gets any ideas about us dating? Which is a thing we are totally not doing."
    s "Chika-"
    c "Fine, fine. Twenty steps. But that’s my final offer."
    s "I think we can manage to walk to whatever fancy dining hall the Tsukiokas have without anyone thinking we are having sex."
    c "Sex? Me? Nuh-uh. Not until marriage, Sensei. But I {i}guess{/i} I can find the time to accompany you to the buffet."
    s "You {i}guess?{/i} You’re the one who invited me."
    c "Only because I feel bad that you’re all alone, obviously. It doesn’t have anything to do with that fact that I, the reigning Dorm Wars date champion, have barely gotten to spend time with you the last couple days."
    s "You do realize there is a new champion, right?"
    c "Sure, but...come on. We all know who the {i}real{/i} champion is."
    c "Hint, {i}it’s the one who lets you cum inside of her.{/i}"

    if datewarfutaba == True:
        "{i}That does not help narrow it down...{/i}"

    scene black
    with dissolve2

    "Chika and I exit whatever room I was kidnapped and tossed into and I am forced to follow her on account of having no idea where I am."
    "Sure, I’ve toured at least part of the place before, but when your house is so big that it requires a GPS to get around, it’s easy to find yourself being completely and utterly lost."

    c "Oh, we have to go left down the next hallway in order to make it to the dining hall?"
    s "How do you even remember that? This place is only half a step away from being a full-on maze."
    c "Hm? Did you not download the Tsukioka Manor app? There’s a whole map built in."

    "Oh. So I guess it actually {i}does{/i} require a GPS to get around."
    "Regardless, we make it to the dining hall after a five minute walk and spend the next half hour gorging ourselves on food we can not pronounce until it is finally time to leave..."

    $ yumi_love += 1
    $ nodoka_love += 1
    $ chikalust25skip = True

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo14

label chikalust25:
    scene poorgirldoggystyle1
    with dissolve

    c "So! Looks like it’s just you and me now. {i}Finally.{/i}"
    s "Was that “finally” supposed to be audible or are you just really bad at whispering?"
    c "As you may have observed in the past, I am not exactly good at being quiet. But I don’t really mind if you heard either way."
    c "As the reigning Dorm War date champion {size=-15}and your adoring girlfriend,{/size} I think I deserve some time alone with you too, you know."
    s "You realize there’s a new champion now, right?"
    c "Sure, but...come on. We both know I’m the {i}real{/i} champion since I’ve swallowed at least three gallons of your cum so far."
    s "There is absolutely no way it has been that much."

    scene poorgirldoggystyle2
    with dissolve

    c "Probably not, {i}but I can wish.{/i}"
    s "..."
    c "..."
    s "You’re horny, aren’t you?"

    scene poorgirldoggystyle3
    with dissolve

    c "Arf."
    c "That’s wolf for “yes.”"
    s "..."
    c "What gave it away? Was it the part just now where I wished for three gallons of cum?"
    s "Stop saying “three gallons of cum.” It makes me uncomfortable."
    c "You know what makes me uncomfortable?"
    s "..."
    c "Not being covered in three gallons of cum right now."
    s "You have a problem."
    c "Hey, it’s your fault I have this problem. Up until I met you, I couldn’t care less about-"
    s "Don’t say it again."

    scene poorgirldoggystyle4
    with dissolve

    c "Fine. But I refuse to let this rare opportunity of being alone with you in a fancy mansion go to waste! Come with me!"
    s "Come with you where? Don’t we have to go to the next contest thing?"
    c "That’s not for another forty-five minutes and all of the girls are in the dining hall right now. I want to explore because, let’s face it, the chance of {i}me{/i} ever living in a place like this is less than zero."
    s "We’re going to get lost."
    c "It’s fine. I have the Tsukioka Manor GPS app."
    s "Why is there a Tsukioka Manor GPS app?"
    c "So we don’t get lost, obviously."
    s "That’s-"
    s "You know what. That’s fair. But I still don’t think it’s a good idea to-"

    scene poorgirldoggystyle5
    with dissolve

    c "I’ll let you hold my leeeeaaaaash~"
    s "Okay, that is {i}definitely{/i} not a good idea."
    s "I’m in."

    scene black
    with dissolve
    stop music fadeout 15.0

    c "Woo! Here you are, Master- the chain of your new best friend. Please make sure you take very good care of her. Especially when she goes into h-ckh?! Why are you pulling?! This is animal abuse!"
    s "You know you like it."
    c "Ugh...you’re right. Pull harder."

    "Chika and I walk through the halls of the manor, though I {i}do{/i} release my grip on the chain as soon as we exit the room as I figure that’s...not a thing anyone should see."
    "Thankfully, we don’t run into anyone {i}at all{/i} as it seems the entirety of the class really is in the dining hall at the moment."
    "And while that is certainly a place I would like to be as well considering investing really runs up an appetite, I {i}also{/i} want to savor this moment with Chika."
    "At first, I was indifferent."

    scene poorgirldoggystyle6
    with dissolve2
    play music "asobeatsex7.mp3"

    c "{i}Oh my God...{/i}"

    "But the moment her eyes lit up upon walking into a more western style grand foyer...I realized just how much of a fantasy this must be for her."

    c "This place is, like...like something out of Cinderella. Or Titanic or...Sensei, name some other movies with really lavish rooms like this."
    s "You are asking the wrong person, Chika."

    scene poorgirldoggystyle7
    with fade

    c "Sensei...you should get rich so we can live in a place like this one day."
    s "This is not what I had in mind when I monologued about building a castle that one time."

    scene poorgirldoggystyle8
    with dissolve

    c "Castle? Monologue? Was I there for that?"
    s "In the background, yeah. Just a thought I had once."
    s "It feels like such a long time ago at this point, though."

    scene poorgirldoggystyle9
    with dissolve

    c "Yeah. We’ve sure come a long way, haven’t we?"
    c "Thinking that while standing in a place like this makes it feel like the final scene of a movie."
    s "That’s the second time you’ve brought up movies in like, thirty seconds."
    c "I know, but {i}just look at it.{/i}"
    c "When you grow up in a tiny apartment in a run-down neighborhood, you really start to forget that places like this actually exist and aren’t just made up."
    s "I think the Tsukiokas are a rare case and that this isn’t really a good indicator of life outside of your bubble. Especially when your bubble contains a lot more people than one like this ever will."
    c "That’s just the thing, though. {i}All{/i} of us in that bubble dream of having stuff like this one day, but we know that it’s a height we’ll never be able to reach."
    c "So, instead...we rely on tiny bursts of luxury like new accessories or HBO movie rentals or...bleaching our hair or...getting an extra topping on pizza. The little stuff, you know?"
    s "And seeing something like this...you don’t feel disheartened? Or think it’s a waste of money? Because this hall is probably worth more than your entire building and it’s not even being used."
    c "Jealous, sure. But disheartened? Not at all."
    c "I’m happy there are people who get to live like this...in their own little fairy tales."
    c "But I guess I shouldn’t be {i}too{/i} jealous."
    s "And why’s that?"

    scene poorgirldoggystyle10
    with dissolve

    c "Because...I’ve got my own fairy tale."
    s "..."
    c "..."
    c "{i}It’s you. You’re the fairy tale.{/i}"
    s "I got that. It was just so cute that my brain short-circuited and wouldn’t let me respond."
    c "If I had to choose between you and the house, though...I’d definitely go with the house. I’m not an idiot."
    s "Yeah, I’d go with the house too. And thanks for retroactively making your previous statement less cute. I think I’ve finally regained feeling in my legs and can walk again."
    c "Want to put ‘em to use and look around a little more? I doubt Tsubasa will care if it’s just us."
    s "If she even finds us, you mean. Which I highly doubt she will considering just how massive this place is."
    c "Then it shouldn’t be a problem at all. Right, Sensei?"
    s "..."
    c "Sensei?"
    s "I was just wondering if I could hold the leash again."
    c "Arf."
    c "That’s wolf for-"
    s "Just hand over the chain."

    scene black
    with dissolve2

    c "Yes, Mas-ckh! Careful! You almost broke my neck that time!"
    s "You know you like it."
    c "Even I have limits, Sensei!"

    "........."
    "......"
    "..."

    scene poorgirldoggystyle11
    with dissolve2

    "Our exploration comes to a screeching halt once we reach a room that looks like this."
    "I’m sure you understand why."

    c "..."
    s "..."
    c "Welp."
    s "Did you plan this?"

    scene poorgirldoggystyle12
    with dissolve

    c "Plan? No."
    c "Hope? Yes."
    s "Welp."
    c "Remind me- how firm is that “No more sex in places we probably shouldn’t have sex” rule? Because I’ve done very well so far and I’m not saying we should {i}break{/i} that rule, but..."
    c "I think we should break that rule."
    s "We don’t even know whose bed this is."

    scene poorgirldoggystyle13
    with dissolve

    c "And?"
    s "..."
    c "Sensei?"
    c "Speechless again from how cute I am?"
    s "Oh, no."
    s "I was just wondering why you aren’t on the bed yet."

    scene black
    with dissolve

    c "Oh, thank fucking God because I was legit two minutes away from going full wolf and just humping your leg out of desperation."
    s "I’m pretty sure that’s supposed to be a sign of dominance when a canine does it."
    c "Awesome. Then, how about you get the fuck over here and show me what else you know about dominance?"

    scene poorgirldoggystyle14
    with dissolve2

    s "You don’t have to ask me twice when you look like {i}that.{/i}"
    c "Oh yeah? Does it get you hard when I give myself up like this, [chikamaster]?"
    c "You like it when I wave my little ass in the air for you?"
    s "Don’t take this the wrong way, but that is certainly not a {i}little{/i} ass."
    c "It’s little compared to {i}you,{/i} [chikamaster]."
    c "Those big, strong hands...grabbing and slapping my skin until you can see your hand prints..."
    c "Pulling me closer...pressing it up against your waist...remembering how {i}tight{/i} it’ll be inside of me..."
    c "Then taking that {i}huge{/i} cock of yours into your hands...angling yourself down..."
    c "You’ve practically got me panting already...what are you waiting for?"
    s "The end of your story."
    c "You really want me to spoil it when you can just find out yourself?"
    s "It’s more that I just want to hear you say it."
    c "Fine. But only because I love you."
    c "The story ends with you grabbing my fluffy, little tail..."
    c "Pulling me closer again..."
    c "Guiding that big dick right up to my pussy..."
    c "And then breeding me like there is no tomorrow."

    scene black
    with dissolve2

    "I take my cue to join Chika on the bed and remove my pants with a level of speed I’m not sure I’ve ever achieved before..."

    scene poorgirldoggystyle15
    with dissolve2

    "Not wanting to ruin her story...I grab her tail, which seems to be sewn directly onto a pair of underwear she deemed modest enough to wear as a Halloween costume, and pull her ass up a little further."
    "My grip on this new appendage also allows me to make it to the penultimate part of her story’s ending as I bend it to the right to slide her panties aside before guiding my dick to her slit..."
    "And then, just as she said I would- I throw myself into mating season and breed her like there’s no tomorrow."

    c "AaaaAAAaaahhhhhhh fuuuUUUuuuuck, [chikamaster]...thank you...thank you...thank you..."
    c "Thank you so much for...fucking the heat out of your little doggy...whatever...hah! Whatever...can I do...to repay you?..."
    s "No need...this is reward enough for me..."
    c "Hah...hah...yeah?...Are you gonna...give me...lots and lots...of cum...[chikamaster]?..."
    s "I’ll see what I can do..."
    c "Are you...gonna give me...three gallons of-"
    s "Chika."
    c "Heheh...hehehaha...ngh...just a little...joke...is all..."
    c "Just trying to...be man’s best friend...and nothing says loyalty like...keeping you entertained as you...fuck my tight...undeserving pussy..."
    s "Undeserving?"
    c "Hah...ngh...mhm! I might be your...girlfriend by day, but...I’m just your pet right now...and you’re just...fulfilling your duties as...my loving master."
    s "Ah, so we’re roleplaying."
    c "Hah...aaaaahhhh fuck! Is that...not allowed? Want me to...go back to being...normal Chika?..."
    c "Or can I stay a...horny wolf for...a little while longer?..."
    s "You really like this, don’t you?"
    c "I think...something is...awakening in me..."

    scene poorgirldoggystyle16
    with hpunch

    c "Aah! Ah! Ah! AAAAAhhh! [chikamaster]! Ahhh! Yes! Yes, yes, yes!"

    "I begin pounding Chika at full force to see what else I can awaken in her. But, at this point, I’d be surprised if she was able to make it an extra five minutes without having an orgasm so intense she passes out."
    "Her hips begin to shake violently and it’s hard to discern whether it’s because of the amount of force I’m placing on them or if she’s just so far gone into ecstasy that she can barely feel anything else."

    c "Aaaahhhh! AAAAAHhhh FUuuuuUUCK! Just like...that! AAAAAHHHHHH!!!!"

    "The silence in this wing of the manor makes the slapping of our skin so loud that I’m convinced anyone even halfway down the hall could hear it."
    "Chika’s screams are no different as they begin to ramp up in both passion and pleasure, but there is something {i}else{/i} I want to make her do right now."

    c "Ahhhh! Yes! Harder, [chikamaster]! Harder!"
    s "Bark for me."

    scene poorgirldoggystyle17
    with dissolve

    c "Hah......what?....Really?....You actually want me to?...."
    s "Embarrassed?"
    c "No...I’ll do it. I’ll {i}gladly{/i}...ngh...I’ll {i}gladly{/i} do it...I was just worried...Jesus fuck that’s good...worried that it might be too weird..."
    s "You’re my pet right now...so act like my fucking pet."

    scene poorgirldoggystyle18
    with dissolve

    c "{i}God{/i} this is so hot..."

    scene poorgirldoggystyle16
    with dissolve

    "Again, I increase the speed and strength with which I fuck the quivering body before me, now crumbling under the weight of a command that only I can issue."

    c "Arf! Arf...arf...arf! Ahhhhhhhh!!!!! Arf! Arf arf! Arf!"

    "And sure, she might look ridiculous to anyone on the outside-"
    "But to me, the man who’s loved...and desired enough to make her do this, her barks and howls are a symbol of accomplishment."
    "Her tight, hot, dripping pussy and the tail still firmly clasped in my hand...{i}they{/i} are symbols of accomplishment."
    "She is not just my pet right now...she is my pet {i}forever.{/i}"
    "Which makes me elated to continue fulfilling these duties of mine."
    "And making her scream so loud she scares off all the other animals in the area."

    scene poorgirldoggystyle19
    with dissolve

    c "Hah...hah...hah...hah...hah..."

    "The barking turns to panting."
    "She’s no longer human at all. Just a bitch in heat getting the tension fucked out of her."
    "There are no rational thoughts, nor fanciful dreams of a mansion or a life in which things are actually {i}good...{/i}"
    "Just primitive body to body contact."
    "And fluids dripping from both her crotch and her mouth onto the unknown sheets beneath us."

    scene black
    with dissolve2

    "Over the next fifteen minutes, Chika cums three times in three different positions."
    "Her body grows uncharacteristically weak for someone who is, for lack of a better term, an expert at taking dick...so I do what any good master would do."
    "I grab her leash for a third time today and pull her body back toward me, propping her up on my lap as I insert myself once more and force her to ride me like the {i}undeserving{/i} bitch she is."
    "........."
    "......"
    "..."

    scene poorgirldoggystyle20
    with dissolve2

    c "Hah! Hah! Hah! Hah! Hah! Hah! Hah! Hah!"
    c "So good! So good! So good! Want...more!"
    s "Remembering how to talk again?"
    c "Fuck...harder...pound me...pound my fucking pussy!"

    scene poorgirldoggystyle21
    with dissolve

    c "AaaaaAAAAAAH! [chikamaster]! You’re so good! You’re so fucking good!"
    c "Oh God...I’m gonna cum again...I’m gonna cum again! Fuck me fuck me fuck me fuck me!"
    c "Yes! Fuck! Yes! AAAAAHHHH!"

    play sound "dooropen.mp3"
    scene poorgirldoggystyle22
    with dissolve

    tb "Dear lord! Can you two not keep it down?! I could hear you from halfway down the hall!"
    c "Tsu...basa....don’t...look at me..."
    c "I’m...oh God...oh fuck..."

    with sexfade
    with sexfade
    with cumflash
    scene poorgirldoggystyle23
    with hpunch

    c "NGHHHHH!!!!!!!!!!!!!!!!!~~~~~~~~"

    "Chika does her best to suppress her orgasm, but the shaking of her body and the way she bites down on her lip tells Tsubasa all she needs to know."
    "And yes, I probably should have stopped fucking her seeing as a powerful adult woman has now caught me having sex with a teenage student and could end my career in the blink of an eye."
    "But, let’s face it, that’s something she also could have done {i}before{/i} this happened."
    "Plus, it feels way too good inside of Chika right now to stop."

    c "Ngh...Sensei...not so hard...right after I...ngh~"
    c "Tsubasa...help me...he’s being...too rough!"
    tb "Yes...I can see that."

    scene poorgirldoggystyle24
    with dissolve

    tb "Just-"
    tb "Just quiet down, please! And have some tact next time! You’re in someone else’s home!"
    c "Ngh...mmnh...yes...ma’am..."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene poorgirldoggystyle25
    with dissolve2

    tb "The nerve of some people! Could they not hold it in until they were in their {i}own{/i} homes?"
    tb "And is it really necessary to be that {i}loud?{/i}"
    tb "I understand what it’s like to be young and full of energy, but there is a line that must be drawn and..."

    scene poorgirldoggystyle26
    with dissolve

    tb "And..."
    tb "..."
    tb "..."

    scene poorgirldoggystyle27
    with dissolve

    tb "No."
    tb "I mustn’t."
    tb "Chika is like a daughter to me. I couldn’t possibly look in on-"

    scene poorgirldoggystyle28
    with dissolve

    tb "But..."
    tb "Then again...she {i}is{/i} still young. And she was certainly taking a beating just now."
    tb "Perhaps I should make sure she’s-"

    scene poorgirldoggystyle29
    with hpunch

    tb "No! I refuse to give into temptation! I am a powerful, independent woman!"
    tb "A powerful, independent woman who..."

    scene poorgirldoggystyle26
    with dissolve

    tb "Who has not had sex in...a very long time..."
    tb "..."
    tb "..."

    scene poorgirldoggystyle30
    with dissolve

    tb "I’m just making sure she’s okay. That is all."
    tb "And there is nothing wrong with looking out for those you care about."

    scene poorgirldoggystyle31
    with dissolve

    c "{i}Ahh! Ahh! Harder! Right there! Sensei!{/i}"
    c "{i}Oh....God! You’re seriously...gonna make me cum...five times before letting it out!?...{/i}"
    c "{i}Just...give it to me already! Give it to me!{/i}"
    tb "{i}Five?{/i}"
    tb "Is such a thing even possible? That sounds-"

    play sound "doorslam.mp3"
    scene poorgirldoggystyle32 with hpunch

    tb "What on earth am I doing?! I’m no peeping tom! I’m a distinguished woman of utmost importance who..."

    scene poorgirldoggystyle33
    with dissolve

    tb "Who has not had sex in a very long time."
    c "{i}Ah! Ah! Ah! Yeah! Just like that! Just...like that!{/i}"
    tb "I’m just making sure they don’t break anything. There are very expensive items in that room."
    c "{i}AAAAAAAHHHHHH FUCK IT’S SO BIG!{/i}"
    tb "Oh, who am I kidding? I haven’t seen anything this exciting in ages."

    scene poorgirldoggystyle34
    with dissolve

    tb "I suppose watching for a little while won’t hurt."
    to "Watching what, Mother? Is something happening in my room?"

    play sound "doorslam.mp3"
    scene poorgirldoggystyle35
    with hpunch

    tb "No."
    to "I see."
    to "In that case, would I be able to enter? I left my-"
    tb "Whatever you need, go buy a new one."
    to "But-"
    tb "Right now. That is an order."
    to "But Mother, you always say-"

    scene black
    with dissolve

    tb "Oh, how about I go with you?! That sounds like a fun bonding experience, doesn’t it?!"
    to "It does! But...I have the next Dorm War contest to attend and-"
    tb "Here’s an excellent idea! How about you tell me all about it on the way out of the grand foyer?!"

    "........."
    "......"
    "..."

    scene poorgirldoggystyle36
    with dissolve2

    c "Hah...hah...hah...hah...hah..."
    c "That was...the greatest thing...that has ever happened to me..."
    s "You’re just high on the afterglow right now. Pretty soon, you’re going to realize that your costume is ruined and that your surrogate mother just watched you have an orgasm."

    scene poorgirldoggystyle37
    with dissolve

    c "Yeah...that was weird. But it’s not like she didn’t already know about us after the onsen."
    c "Plus, she’s my {i}surrogate{/i} mother. Which means it’s a lot less weird for her to watch me getting fucked than if my {i}actual{/i} mom did."
    s "I think we’d have much bigger problems on our hands if your actual mother was watching us have sex as that would imply the existence of zombies."
    c "Ugh...what the fuck am I gonna do about my costume?"
    s "Save it. This outfit is a treasure and I will not let it go to waste."

    scene poorgirldoggystyle38
    with dissolve

    c "Yeah. I was way more into that than I thought I’d be. Even the barking part. It was like...{i}primal.{/i}"
    c "I felt like you were gonna tear me in half."
    s "I don’t think I could if I tried. You’re pretty indestructible in the bedroom."
    c "That’s not true. I almost ran out of steam at the end."
    s "And yet you had two more orgasms afterward."

    scene poorgirldoggystyle39
    with dissolve

    c "I’ll be damned if I let my man out of the bedroom before he finishes. That’s like, a cardinal sin or something."
    c "Sure, it wasn’t a full three gallons of cum. But-"

    scene black
    with dissolve
    stop music fadeout 7.0

    s "Okay. I’m putting my clothes back on now."
    c "Heheh...fine. I’m gonna lay here for a while and...uhh...dry out. But if you see Tsubasa, can you ask her to bring me a towel or something?"
    s "Just a towel and not a change of clothes?"
    c "Oh, no way. I’m totally wearing this outfit to the bar tonight. I’ve just gotta clean it up first."
    s "I think you’re gravely misinterpreting how...wet it is."
    c "And I think you’re gravely misinterpreting how much of a turn on it will be knowing I’m standing in front of all of my friends wearing the outfit you just came all over~"
    s "Again...you have a problem."

    $ renpy.end_replay()
    $ chikalust25 = True
    $ chika_love += 1
    $ chika_lust += 2

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "{i}Chika’s lust has increased to [chika_lust]!{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo14

label mall45:
    scene mall1
    with fade
    play music "mall.mp3"

    "I make my way to the mall because I’m in a generous mood and want to buy presents for Ayane and Maya since they’ve been through a lot lately."
    "Oh, who am I kidding? I’m here to hang out with Chika."
    "The “Sensei Love Squad” is nice and all, don’t get me wrong. Like, it’s an entire squad centered around loving me and things don’t really get any better than that."
    "But it’s also nice taking time off every now and then to remind myself that there are girls still mostly detached from the crazy happenings of the universe."

    scene black
    with dissolve2

    "As I round the corner and head into Le French Store or whatever Chika’s business is called, that thought rings out in my head."
    "It bounces back and forth in the leftmost section of my brain until dissolving into nothingness and leaving me with the cranial aftertaste of complacency and nonchalance. "

    scene chikascarves1
    with dissolve2

    "But then it sours as I see Chika holding a familiar scarf — and those dissolved thoughts reform once more."
    "No one is detached from the crazy happenings of the universe."
    "But it would be nice if I was able to believe they were for more than just a few minutes at a time."

    c "Can I help you?"
    s "Yeah. I’m looking for a girl around your age who might want to make out for a little while."
    c "Sorry. I have a boyfriend."
    s "I know. I am him."

    scene chikascarves2
    with dissolve

    c "Huh? You’re-"

    scene chikascarves3
    with hpunch

    c "Ah! Hey! I wasn’t expecting you today."
    s "I could tell by the way you so quickly rejected me."

    scene chikascarves4
    with dissolve

    c "Yeah, sorry about that. There was another guy a couple hours ago who tried the same thing, so I like, half-expected you to just be him coming back."
    s "There was another guy who just...approached you and asked you to make out?"

    scene chikascarves5
    with dissolve

    c "He actually only asked where the bathroom is. But I still told him I had a boyfriend and that made him go away."
    c "I wonder if he ever found the bathroom?"

    "Well, at least I know she’s loyal."

    c "Kinda weird, though. We’ve had several guys come into the mall today. Thought for a second the war might have ended. Turns out there’s just some porn convention going on this weekend."
    s "And we’re not there...why?"

    scene chikascarves6
    with dissolve

    c "Because I can’t legally get in."
    s "Oh. Yeah, that’ll do it."
    c "Are you that into porn, Sensei?"
    s "That depends."
    c "On?"
    s "If this is some sort of trap."

    scene chikascarves7
    with dissolve

    c "It’s not a {i}trap.{/i} I’m not one of those girls who forbids her boyfriend from watching porn. I get that I can’t be there to assist you {i}all{/i} the time. "

    scene chikascarves8
    with dissolve

    c "So, in my moments of absence, feel free to jerk off to whatever or whoever you like without the fear of me getting jealous. "
    c "But also know that if any of that ever leaks into reality and you wind up cheating on me...I will destroy everything you love. Not including myself, of course."
    s "I feel like that part didn’t need to be included, but thank you nonetheless. I will also allow you to look at porn if that makes me sound like a good and respectful significant other."

    scene chikascarves9
    with dissolve

    c "I’ll keep that in mind. Not like I have much time for that stuff anyway, though. Between work, Chinami, Yumi, and you...my time is pretty much all taken up."
    c "I would have liked going to that convention with you, though. Sounds fun. "
    s "On that note, how’s Chinami doing?"

    scene chikascarves2
    with dissolve

    c "Chinami? Fine. Why do you ask?"
    s "Between the fever and her immune-thing-"
    c "Fever? Chinami hasn’t had a fever in months. Where did you hear that?"
    s "So...she’s totally fine?"
    c "Probably even {i}better{/i} than fine. Her and Tsukasa have been going crazy lately. Something about making the Fortune 500 or something? "
    s "..."

    "Did the reset...somehow cure Chinami?"
    "I know Maya alluded to physical stuff being reset sometimes as well, but I guess it didn’t occur to me that it could work like this."
    "That’s...kind of great, actually. There’s finally another benefit to this whole infinite time thing other than just giving me the ability to bone teenage girls for the rest of my life."

    c "Sensei?"
    s "Oh, my bad. Must have been misremembering or something. I’m glad to hear she’s doing okay, though."

    scene chikascarves8
    with dissolve

    c "Heh...it’s cute you were worried about her. But yeah, she's fine."
    s "Great. So, back to the porn thing."

    scene chikascarves10
    with dissolve

    c "Are you really that desperate to not come across as sentimental? It’s fine if you sound a little caring every now and then, you know. I like that side of you."
    c "I wouldn’t be dating you if {i}all{/i} I was into was the sex. "
    s "To be fair, the sex is pretty great. I wouldn’t blame you."

    scene chikascarves11
    with dissolve

    c "It {i}is{/i} pretty great, isn’t it? Maybe {i}we{/i} should do porn? Couples videos are getting pretty big nowadays, aren’t they?"
    s "How do you know that if you never have time to watch anything?"
    c "I didn’t say {i}never.{/i} I just said it was hard to find the time for that stuff. Which is true. "
    s "Either way, we probably shouldn’t have any physical, recorded evidence of our sexual relationship."
    c "Not even for when we’re older and you want to relive the glory days of fucking my tight, teen pussy?"
    s "Welp, congratulations. Now I’m turned on."

    scene chikascarves12
    with dissolve

    c "Just doing my job. I’m only half-serious about the porn thing, though. "
    c "Like, yeah, it would be nice to look back on that kind of stuff one day. But at the same time, the idea of anyone else being able to see us online is pretty nerve-wracking."
    c "So if we ever {i}did{/i} make any sort of videos, I’d probably want to keep them private."

    scene chikascarves13
    with dissolve

    c "It does hurt kissing all of that potential money goodbye, though. Between your huge dick and my body, we could probably rake it in."
    s "I know you’re desperate for cash on account of the whole poverty thing, but I didn’t think you’d gotten to “considering porn” territory just yet."

    scene chikascarves14
    with dissolve

    c "It’s not a real consideration — just a little thought that came to me today on account of the convention buzz. "

    scene chikascarves15
    with dissolve

    c "I do have to do {i}something,{/i} though. It dawned on me during Christmas that what I make now is fine for just getting by, but it doesn’t really let me {i}save{/i} anything."
    c "I don’t want to have to rely on you to take care of me forever. I want to be able to, like...put money away for a house or something. Or at least a nicer apartment."
    c "Folding scarves is easy, laid-back work...but it’s not going to get me to that point."
    s "That said...that scarf looks a little familiar, doesn’t it?"

    scene chikascarves16
    with dissolve

    c "I’m trying to have a melancholic talk about my future and you’re more focused on the {i}scarf{/i} part? What the heck?"
    s "Am I right, though?"

    scene chikascarves17
    with dissolve

    c "Hmm...now that you mention it, it does look kind of like Maya’s. And the other one looks a lot like Ami’s."
    c "They have to be different, though. I mean, they’re {i}obviously{/i} different since they already own theirs. But these ones here were like, {i}just{/i} made for this brand’s new winter line. "
    c "In fact, I’m not even supposed to be putting them out yet. But we needed display pieces over here and I figured it would be fine so long as they’re not priced."

    "They’re the same scarves. "
    "Chika might have an eye for fashion, but I’ve seen them both up close far too often to mistake them at this point."
    "But, if they’re from a brand new clothing line...how would that even work, exactly?"
    "Were the ones I bought here previously just...prototypes or something?"

    scene black
    with dissolve2

    "I do my best to think back on how that conversation went..."

    scene chikascarves18
    with dissolve2

    nce "Looking for a gift now, Sir?"
    nce "These actually just came in this morning."

    scene chikascarves19
    with dissolve

    nce "It was so strange as well. We never ordered anything like these."
    nce "But it’s not like I was about to just let them go to waste so...voila. "
    s "So you’re selling things you never even ordered? How do you know how they should be priced?"

    scene chikascarves20
    with dissolve

    nce "Oh, I have no idea. I just guessed."
    nce "If you act now, I’ll let you have both for just 4,000 Yen. My regional manager is on the way here anyway so I was actually just about to take them down and hide them."
    s "So I’m basically the only chance you have of selling these?"
    nce "You are! And-"
    s "I’ll give you 2,000 Yen."

    scene chikascarves21
    with dissolve

    nce "...That’s half of the asking price."
    s "There is no asking price. This isn't even an item you're supposed to carry."
    s "2,000 Yen or I walk."
    nce "Fine..."
    nce "I guess this is my fault for revealing my secrets to you in the first place..."
    c "Helloooo? Sensei? Anyone home?"

    scene chikascarves2
    with fade

    s "Was there ever another girl who worked here?"
    c "Uhh...yeah. Tons. This is a high end fashion store in the mall."
    c "Why, though? Is there another girl who hit on you that I need to jump? I mean...talk to?"
    s "I’m just pretty sure I bought these exact scarves from someone else here..."
    c "Uhh, well...first off, never buy anything here from anyone but me. "
    c "But second, that’s not possible. Like I said, these are brand new. So unless you got your hands on, like, rough cuts of them or something, there’s no way."
    s "Would something like that even be sold here?"
    c "I doubt it. That stuff is normally saved for, like...models or the family of the designers and whatnot. "
    s "Huh..."
    c "Why are you so fixated on these scarves anyway? It’s not even winter yet. "
    s "I..."
    s "I don’t really-"

    play sound "static.mp3"
    scene amibreak4 with flash
    scene happy4 with flash
    scene chikascarves22 with flash
    stop sound

    s "...know."
    c "Right?! Like, there are so many other places I’d be a better fit for. My talents are wasted on Les Vêtements."

    scene chikascarves23
    with dissolve

    s "Sorry, what were we talking about just now?"
    c "Hm? Different places for me to work."
    c "You told me I had to get out of there like, five minutes ago. Is that not what you meant?"
    s "I don’t really...know what I-"
    u "Ohohoh...is that Sensei I spy?! And with a top-fiver, no less?! Io, get my journal! It’s time for a ranking update!"

    scene chikascarves24
    with dissolve

    c "{i}What’s our excuse?{/i}"
    s "I’m just here to hang out with you."

    scene chikascarves25
    with dissolve

    c "They won’t think that’s weird?"
    s "Probably not. You’re a top-fiver, so it should be fine."
    c "Top-fiver in what? What’s this ranking for?"
    s "Uta has an unofficial ranking of how much I love all of you."

    scene chikascarves26
    with dissolve

    c "And I’m not number one?! "
    s "It’s an {i}unofficial{/i} ranking, Chika. No one knows about us but Yumi."
    c "I’m still mad either way! "
    u "Heyo! What are you guys yelling about?"

    scene chikascarves27
    with dissolve

    c "Oh, nothing! Hahahah! Sensei was just telling me the funniest joke! Weren’t you, Sensei?"

    scene chikascarves28
    with fade

    s "Uhh...yes."
    s "Knock knock."
    u "Who’s there?"
    s "Doctor."
    u "Doctor who?"

    scene chikascarves29
    with dissolve

    u "Oh, I get it! Like that one British TV show with the phone-"
    s "Doctor Patterson. I regret to inform you that the cancer has spread to your grandfather’s brain and...he isn’t going to make it."
    u "..."
    s "..."
    s "I'm sorry you have to find out like this. I know it's sudden."

    scene chikascarves30
    with dissolve

    c "Hahah...hah...funny, right?"
    u "Normally, my traumas don’t catch up to me until nighttime. Good joke, Sensei. I’ve never had comedy change my entire schedule around before."
    c "Sooooo...ignoring everything that’s happened over the last twenty seconds, what are you guys doing here?"
    u "I don’t know anymore. I just don’t know."
    i "You don’t have to pretend to be interested in us. It’s not like you’re obligated to greet every single familiar face you encounter out in the open. You’re just going to make people uncomfortable doing that."

    scene chikascarves31
    with dissolve

    c "What was that, Io?"

    "Well, it seems that Io’s distaste for Chika is one thing the reset can {i}not{/i} cure."

    i "I said-"
    u "Hahah! She’s got jokes of her own too! You’d just never know with how quiet she is in school! Hahaha! Anyway, hi! Don’t kill us, please."

    scene chikascarves32
    with dissolve

    c "I wouldn’t kill you, Uta. I like- are you blushing right now?"
    u "You’re really pretty and being touched by you sent special signals to my brain. I'm sorry. "

    scene chikascarves33
    with dissolve

    c "God, you are so friggin’ adorable!"
    u "{i}Hah...Heaven...{/i}"
    c "Who’s a good girl? {i}Who’s a good girl?{/i}"
    u "Uta-chan...is a good girl..."
    i "I’m going to puke."
    c "If only your best friend wasn’t so unbearable! Maybe then you and me could hang out more?"

    scene chikascarves34
    with dissolve

    i "Oh, please. As if Uta would ever stoop to-"
    u "Shh..."
    u "Let me have this..."
    s "Pardon the interruption, but my partially-twisted mind has immediately come up with a way to make that happen {i}and{/i} potentially solve your financial issues, Chika."

    scene chikascarves36
    with dissolve

    c "It has?! How?! What is it?! What do I have to do?!"
    s "Sell your soul."
    c "I thought I already told you porn was a no-go."
    s "Which is why you settle for the next best thing — a maid cafe."

    scene chikascarves37
    with dissolve

    u "Mm!"
    u "Thank you, Sensei! I’ve remembered my place in the world and am now back to normal!"
    c "Me? Working at a maid cafe? Alongside Uta and Ami? Yeah, no way. They’ve got a totally different appeal than me. There’s no way that would work."
    c "Besides, wouldn’t that be like, objectifying me or whatever? Aren’t you against that?"
    i "{i}Not as against it as you might think, slut.{/i}"

    scene chikascarves38
    with dissolve

    c "The fuck did you just-"
    u "Ignore Io! She wasn’t being serious! And...I think you’d be great, Chika! You don’t need the same appeal as me and Ami! Gyaru maids are like, totally a thing!"
    u "We don’t have anybody like you! And I’m sure you could make more than whatever you’re making here!"

    scene chikascarves39
    with dissolve

    c "Well, how much are you making exactly?"
    u "I’m going to ignore all of the nights where Sensei shows up as they greatly skew the average, but...on a good night, I can walk out of there with around...20,000 yen?"

    scene chikascarves40
    with hpunch

    c "20,000?!"
    u "Maybe...closer to 25,000? We get a percentage of every table and it gets kinda crazy some nights."
    s "Plus you get to keep the dress. Which isn’t to say that {i}I{/i} would benefit from that in any way. It just seems like a thing you’d want to own since you like clothes."

    scene chikascarves41
    with dissolve

    c "Do you think I should do it? That’s, like...{i}way{/i} more than I make here. "
    s "Yes. Adding the maid outfit and shrine maiden dresses to everyone’s wardrobe is my unspoken mission on this planet and I will not rest until it is complete."
    c "And it won’t be weird for you? Knowing that people would-"
    s "Chika."

    scene chikascarves42
    with hpunch

    c "Oh, yeah! I mean...because you’re my teacher. And a high school girl working somewhere like that might...cause problems!"
    c "But I guess if you’re okay with Uta and Ami doing it, there’s...nothing to worry about at all!"
    u "Come by when you’re free and I can show you around. I normally work nights. But since I’m {i}basically{/i} the head maid, I can pretty much do whatever I want."

    scene chikascarves43
    with dissolve

    c "Uta, you are like, seriously saving my life right now. If there’s ever anything I can do to make it up to you-"
    u "You can scratch under my chin and call me a good girl again. "
    c "Are you sure that’s-"
    u "Yes."
    s "I will also volunteer to-"
    u "Please."
    u "Anyone."
    u "I need this."

    scene black
    with dissolve2

    "Io walks away as Chika and I take turns scratching Uta’s chin."
    "That wasn’t the point of all of this, though — just a nice bonus."
    "The point is that Chika’s life may soon be changing as well."
    "And, if I’m remembering correctly, Ami’s eventual appearance at the maid cafe was the first major divergence in the world according to Maya."
    "I doubt Chika, if she decided to follow up on this, will make that same sort of impact."
    "But it is nice realizing that soon, things might get a little easier for her."
    "And a lot hornier for both of us."

    $ renpy.end_replay()
    $ mall45 = True
    $ chika_love += 1
    stop music fadeout 7.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label chikaspecial45:
    scene noonsky
    with dissolve2
    play music "comfort.mp3"
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "I know she’s normally working around this time but, based on what may be a change of heart centered around a hopeful change in income...that might not be the case any longer."
    "I doubt she’s made any major moves yet. I feel like she would have told me if she did. Or, at the bare minimum, sent me a picture of her with at least {i}part{/i} of the costume on."
    "She’s sent me nothing at all."
    "Which is why I’m now reaching out to her — so she can be reminded of what is important."
    "Me."

    play sound "phonebeep.wav"

    c "Helloooo?"
    s "Hey. Are you working right now?"
    c "I am not! I took today off to hang out with Tsubasa."
    s "I see...Just to satisfy my own curiosity though, are you still employed by the clothing place? Or have you moved onto bigger, pinker things yet?"
    c "I am still employed by the clothing place. I haven’t followed up with Uta yet. But if you’re {i}that{/i} desperate to see me in the uniform, I can ask her if I can borrow one."
    s "That would be greatly appreciated. Is this thing with Tsubasa something I can join in on? Or are you two being a weird, unrelated mother-daughter couple again?"
    c "You can drop by if you want! We’re at my place. "
    c "Not sure how much fun you’ll have, though. We’re kind of just talking and making sure the kids don’t accidentally take over the world."
    s "I guess I’ll come meet you then. It’s not like I have anything else going on."
    c "Cool! I’ll let everybody know. I’m sure they’ll all be happy to see you."
    s "Doubtful."
    c "Oh, shut it. I love you and I’ll see you soon."
    s "Yeah...you too."

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "As you may have noticed, I’ve given up on fighting the boyfriend thing — even mentally."
    "I’ve waited too long at this point to say anything about it and, even if Chika only started believing it due to me not making my stance on relationships clear enough, I’m here now and...I don’t want to leave."
    "It’s by that metric, however, that I realize I’m dating a ton of people."
    "Some of them understand my stance a little better than others, sure- but when it comes down to it...I’m not really anything more than the student body’s universal boyfriend."
    "All that’s left to do is check off the rest of the boxes pertaining to those I haven’t slept with yet and further diminish the meaning of the word “boyfriend” until it's no longer worth it to anyone."
    "I’ll get there."
    "But before that, there’s somewhere else I need to go."

    scene chikasflashback1
    with dissolve2

    "A place where I am always welcome — with paperthin walls and a foundation I’m sure is already in the process of crumbling."
    "Much like the rest of the buildings in this half of town, this one surely doesn’t have much time left."
    "I have somewhere else I could take her."
    "It’s a place that’s still a secret to most, and I could make it {i}Chika’s{/i} secret as well if I was anywhere near a good person."
    "But I’m not. "
    "And so I’ll wait for her new mother to do it instead because it will spare me a slightly difficult talk."

    c "Hey! You hungry? Tsubasa’s making curry."
    tb "Look at me, cooking when it’s not even a competition. It’s like university all over again."
    s "I’m fine. You two can eat without me. "
    c "Are you sure? We made enough for like ten people so there would be plenty of leftovers for tomorrow. "
    s "Follow up with me tomorrow then. In the meantime, what are Chinami and Tsukasa arguing about? They look...passionate."

    scene chikasflashback2
    with dissolve

    c "Chinami! What’s Tsukasa trying to convince you to do now?!"
    ch "Chinami doesn’t even know! Tsukasa just keeps yelling letters at her!"
    tk "I’m trying to teach you the difference between CEO, CRO, CMO, CTO, CFO, COO, CSO, CHRO, and CIO! This is elementary level stuff, Chinami! You need to know this as my partner!"
    ch "See?!"
    tk "Yes! {i}C!{/i} For {i}Chief!{/i} Now, tell me what the other letters stand for!"

    scene chikasflashback3
    with dissolve

    c "And that’s basically why we stopped paying attention. "
    tb "Oh, Tsukasa and her acronyms. I’m just glad she’s outgrown speaking entirely through abbreviations. That was quite a difficult month for me."
    s "Yeah, I’m good not taking any part in their conversation and will gladly just continue conversing with you two instead."
    s "So long as that doesn’t pertain to business as well, I mean. Because if you two are being anywhere near as boring as them, I’m out of here."
    c "I was actually just telling Tsubasa about my mom."
    s "Without crying?"

    scene chikasflashback4
    with dissolve

    c "I don’t {i}always{/i} cry when talking about her, you know. I have plenty of good memories to talk about too."
    s "Then why haven’t you ever told me about them?"
    c "Becaaaaause it’s not an exciting conversation topic and we’re normally doing...{i}other stuff?{/i}"
    s "Well, I see there’s no need to fully censor yourself around Tsubasa anymore."

    if chikalust25 == True:
        scene chikasflashback5
        with dissolve

        tb "After what I saw during your Halloween party? No, there’s no need for such formalities anymore. "
        c "Arf..."
        s "Arf indeed."

    else:
        scene chikasflashback5
        with dissolve

        tb "To this day, I can no longer walk down the halls of the ryokan without hearing phantom {i}noises{/i} that are {i}quite{/i} similar to those you two made when you stayed there."
        c "Hahah...hah..."
        s "I apologize for our actions somehow haunting your halls. But also, I regret nothing."

    scene chikasflashback6
    with dissolve

    c "Are you like, actually cool hearing about her though? It won’t be weird for you?"
    s "Why would it be weird?"
    c "I don’t know...You never really talk about {i}your{/i} parents, so I figured there might be some hostility there or-"
    s "There’s nothing. Just finish whatever story you were telling Tsubasa and I’ll fill in the gaps."
    c "You’re positive?"
    s "I’m positive."

    scene chikasflashback7
    with dissolve

    c "Okay."
    c "Then..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene chikasflashback8
    with dissolve2

    c "{i}It was in this very kitchen...on curry night...{/i}"
    c "Mom! Have you seen my bracelet anywhere?"
    chi "Which one, Chika? You have many, many bracelets."
    c "The one with the beads! That we got from the flea market near the beach!"

    scene chikasflashback9
    with dissolve

    chi "Didn’t you say you were going to take good care of that one? Taking care of something means not losing it, you know."
    c "I didn’t lose-"
    c "Oh. Here it is."

    scene chikasflashback10
    with dissolve

    c "Told you I didn't lose it."
    c "It was in Chinami’s playpen. It must have fallen off when I was playing with her."
    chi "Please be more careful around your sister, Chika. She’s at that age where she wants to put everything in her mouth and I’m {i}pretty sure{/i} that bracelet isn’t edible."

    scene chikasflashback11
    with dissolve

    c "Do you know when she’s coming home?"
    chi "Why? Do you miss her?"
    c "Not really. I’m just wondering."
    chi "Are you just too {i}embarrassed{/i} to admit you miss her?"

    scene chikasflashback12
    with dissolve

    c "No. I already told you. I’m just wondering."
    c "She’s been gone for a while and I just want to know when she’ll be back. That’s all."
    chi "Well, regardless of whether or not you’re embarrassed, {i}which you are,{/i} I’m glad you’re “wondering.”"

    scene chikasflashback13
    with dissolve

    chi "It’s your job to look out for her, after all. And having a responsible girl like you as my backup takes a huge load off of my mind, Chika. "

    scene chikasflashback14
    with dissolve

    c "Of course! You know I’d do anything I can to help! And I won’t even ask for a raise on my allowance in exchange!"
    chi "What do you want now?"
    c "I don’t know what you’re talking about, Mommy. There isn’t anything I want. And if there is, it’s definitely not a gold necklace like yours."
    chi "This isn’t real gold, Chika. How many times do I have to tell you that?"
    c "Yeah, but it {i}looks{/i} gold and I want to look more like you. "

    scene chikasflashback15
    with dissolve

    chi "Between your hair, your clothes, your attitude...you’re basically already {i}me,{/i} Chika. A necklace isn’t going to bring you any closer."
    chi "You know I don’t have any money to give you anyway."
    c "Can I at least use your makeup kit?"

    scene chikasflashback16
    with dissolve

    chi "Absolutely not and you are grounded for even asking."
    c "Pleeeeease? I’m almost nine years old. I should be allowed by now."

    scene chikasflashback17
    with dissolve

    chi "Oh, my beautiful daughter..."
    chi "No."
    c "But why?!"
    chi "Because I said so."
    c "But Mom-"

    scene chikasflashback18
    with dissolve

    chi "In regard to the youngest member of the Chosokabe family, I estimate another...three hours until she’s back from her check-up at the hospital."
    c "That long? What are they even doing over there?"

    scene chikasflashback19
    with dissolve

    chi "Blood work. More tests to figure out what’s wrong so we can start making her better."
    c "Do they not have enough of her blood already? How much more do they need?"
    chi "I don’t know. Nobody does. But all we can do is keep listening to what the doctors say since they know better than us."

    scene chikasflashback20
    with dissolve

    c "I wish it was me instead."
    chi "Chika-"
    c "Why can’t they take my blood? We’re sisters. It’s the same, isn’t it?"

    scene chikasflashback21
    with dissolve

    chi "You know it doesn’t work that way. You’re smarter than this."
    chi "Chinami’s special. Which means she needs special care."
    c "We can’t even go with her, though? Why do we have to stay here?"

    scene chikasflashback22
    with dissolve

    chi "Because it would only make things harder."
    chi "If we go with her, we’ll get questioned. She looks just like us and we don’t have enough money for her tests."
    c "But people {i}aren’t{/i} going to question your friend bringing her when they look nothing alike?"
    chi "Nope! Because my friend has connections at the hospital and has been pretending Chinami is her daughter for two years now."
    chi "No one’s going to question her at this point...and we need her insurance."
    chi "In fact, I doubt anyone would question her in general. She’s a little intimidating sometimes. But it’s better to be safe than sorry."
    c "It still feels weird..."

    scene chikasflashback23
    with dissolve

    chi "That’s because it’s extremely illegal! But sometimes, drastic measures must be taken to ensure that-"

    play sound "static.mp3"
    scene chikasflashback24
    with flash
    stop sound

    chi "Aghahhck!!! Mnnfghckkck! HMmf! Ngchghchkl!"
    c "Mom?! Are you okay?!"

    scene chikasflashback25
    with dissolve

    chi "Mgh...fhmhckh...."
    chi "{i}Purse...{/i}"
    c "Which one?!"
    chi "The...knockoff Louis..."
    c "I know that! I meant which medication?!"
    chi "In...haler..."
    c "Okay!"

    scene black
    with dissolve2

    c "Okay! Okay! Okay!"
    c "Hang in there! I’ve got it!"

    scene chikasflashback26
    with dissolve2

    c "She lasted a few more years after that."
    c "It probably could have been longer if we were wealthy but, that’s...just the hand you’re dealt sometimes."
    c "On the bright side, she got to keep all of her hair. And she died prettier than most people ever live."
    tb "Oh, Chika...you poor thing."
    s "So much for happy memories. That was fucking miserable."

    scene chikasflashback27
    with dissolve

    c "It wasn’t, though."
    c "Like, yeah, the way it {i}really{/i} ended was...but I learned {i}so much{/i} from her. And if it weren’t for her teaching me all about responsibility, I have no idea where I’d even be today."

    scene chikasflashback28
    with dissolve

    c "In hindsight, it was pretty clear she knew she wasn’t going to last forever."
    c "In fact, I probably believed that back then as well but just chose to ignore it because I was too afraid."
    c "I think that’s why she was as strict with me as she was...why she always called me her “backup.”"
    c "It was only a matter of time until it was my turn."

    scene chikasflashback29
    with dissolve

    c "It’s my turn now."
    c "But she’s still watching over me, wherever she is."
    c "And she can’t tell me I’m not allowed to use her makeup kit anymore."
    tb "..."
    c "..."

    scene chikasflashback30
    with hpunch

    tb "Sincerest apologies! I couldn’t hold back any longer!"
    c "Hey! Hey, hey, hey! It’s okay! You don’t have to cry! That was a hopeful, happy ending! I’m okay now!"
    tb "Well, I’m not!"

    scene chikasflashback31
    with dissolve

    ch "Oh no! What will become of Chinami when Tsukasa’s mommy kills her big sister?!"
    tk "You can come live in my house. Your house sucks anyway."
    tb "You can both come live with me right now!"

    scene chikasflashback32
    with dissolve

    chtk "Yaaaaaay!"
    c "Woah, no way! I couldn’t do that to you! That’d be, like...totally unfair!"
    s "But it wasn’t unfair having me buy multiple phones for you?"
    c "Don’t even think of putting that on the same level as this, Sensei!"
    tk "Let’s go kill pigs to celebrate!"
    ch "Okay! Chinami goes first!"

    scene chikasflashback33
    with dissolve

    c "God your boobs are so fucking big."
    tb "You can cry into them. It’s okay."
    c "Crying is...kind of the last thing I want to do right now."

    scene chikasflashback34
    with dissolve

    tb "Hah...I can’t remember the last time I shed real tears and not just fake ones at all of those charity drives."
    c "Like I said...you don’t have to cry. I’m fine now."

    scene chikasflashback35
    with dissolve

    tb "Chika, I was serious about what I said. There is plenty of room at the manor for both you and your sister."
    c "I know...and thanks, Tsubasa. Really. But I have more control over Chinami’s health while I’m here and..."

    scene chikasflashback36
    with dissolve

    c "I think both of us still have a lot of...attachment to this place. I might have moved on and grown up, but...I don’t know if I’m ready to leave that behind just yet."
    tb "Well, my offer will remain open indefinitely. And should you change your mind or require {i}any{/i} assistance at all, please just let me know."

    scene chikasflashback37
    with dissolve

    c "Of course...thank you, Tsubasa."
    c "For everything."

    scene black
    with dissolve2

    "I can’t help but feel like it may have been better if I didn’t come here today."
    "It was “nice” finally getting to hear more about Chika’s mother, don’t get me wrong-"
    "But it seems to me like I may have interrupted a moment that would have just...been better without me."
    "While Tsubasa cried her eyes out and Chika did all she could to cheer her up, I kind of just...stood there."
    "I mean, what else was I supposed to do?"
    "I couldn’t {i}help.{/i}"
    "I couldn’t {i}relate.{/i}"
    "My presence was nothing more than an unnecessary afterthought."

    play sound "dooropen.mp3"

    "Which is why it feels so wrong to still be splashing around in puddles even after the rain subsides."

    $ renpy.end_replay()
    $ chikaspecial45 = True
    $ chika_love += 1

    jump tsubasaspecial15

label chikadorm45:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Chika’s door, convince her to move out of her shitty apartment for the sake of her sister, and we all live happily ever after."
    "The end."
    "No. Obviously that’s not how today is going to play out because, even after spending an entire night going over all of the questions Tsubasa asked me, I still haven’t really figured out how I feel."
    "And that {i}includes{/i} not fully understanding why I’m so hesitant about this either."
    "On paper, there’s not really a good reason {i}for{/i} me to feel so strange about this."
    "Having Chika live in a better neighborhood wouldn’t just be safer for her and Chinami, but it would make getting to them a million times easier."
    "It would also likely increase the amount of times we’re able to have sex per month as a result of this- and that is a statistic I’d be damned if I overlooked."
    "And yet...something about it feels wrong."

    c "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Call it sympathy or empathy or whatever other pathy is the one that makes you start feeling all gross inside, but the truth is it’s a lot more complicated than that."
    "I just can’t help but feel like having her so close by won’t end well."
    "At the very least, it would make me a lot more hesitant before organizing any slumber parties again."

    scene chikatres1
    with dissolve2

    c "Hey! "

    "It’s fine. It’s not like I’m in any rush."
    "And, like Tsubasa said, Chinami getting sick might cause Chika to spring into action. "
    "I don’t want things to {i}have{/i} to come to that, but...if it’s the easiest option-"

    c "I said “Hey!”"

    "If it’s the easiest option...maybe that would-"
    "No."
    "I don’t want to think about that."

    s "Hey. My bad. Inner monologue is now complete."
    c "Was it about how casually seductive I look right now and how much you want to fuck my brains out?"

    "She says, looking so casually seductive that it makes me want to fuck her brains out."

    s "No, but it is now."

    scene chikatres2
    with dissolve

    c "Want to see ‘em?"
    s "Is it my birthday? Because normally there’s a little more banter involved before we get to the good stuff."

    scene chikatres3
    with dissolve

    c "There doesn’t {i}have{/i} to be. We’re without Yumi and Chinami tonight- and with you being my amazing and loving boyfriend, you can ask me to flash you basically whenever you want."
    s "You’re buttering me up for something, aren’t you?"

    scene chikatres4
    with dissolve

    c "I’m glad you asked."
    s "You’re evil, but your methods are genius."

    scene chikatres5
    with dissolve

    c "Yes, yes. I’m the greatest {size=-15}and only{/size} girlfriend you’ll ever have, but save all of the praise for a little while from now after we have a serious, heated discussion about the future of our relationship."
    s "I knew there was a catch."
    s "Chika, I don’t know if I-"

    scene chikatres6
    with dissolve

    c "..."
    s "..."
    s "What was I saying again?"

    scene chikatres7
    with dissolve

    c "You know, it’s actually a little concerning how well that works. "
    s "The only thing concerning about this is how powerful you’ve become. Now tell me, what’s this “serious and heated” relationship discussion about?"

    scene chikatres8
    with dissolve

    c "It’s nothing bad. Just...different. "
    c "But it’s been something I’ve been thinking about for a while now and I’m {i}pretty{/i} sure you’ll be into it, but like...we should talk first since it’s definitely not normal for us."
    s "Uhh..."

    scene chikatres9
    with dissolve

    c "You know what? Why don’t we sit down? All of our best talks always happen on the bed and, if things start turning weird, I can just suck your dick or something and we can forget about it."

    scene black
    with dissolve2

    "You know..."
    "Maybe living with (or closer to) Chika wouldn’t be so bad after all?"
    "........."
    "......"
    "..."

    scene chikatres10
    with dissolve2

    "She stays silent for a moment once the two of us take our places on the bed."
    "She made a good point about some of our most important talks taking place here...In fact, nearly {i}everything{/i} took place here when we were first starting out."
    "But, as life marches onward, I find myself spending less and less time atop this mattress and more time everywhere else."
    "What was once so familiar to me is now a bittersweet touch of nostalgia..."
    "And all I can hope is that the sweetness isn’t ruined by something that might be hard for me to hear."

    c "So..."
    c "Let me start by saying I love you very much."

    "My hopes are quickly cut down."

    s "Are you...breaking up with me?"

    scene chikatres11
    with dissolve

    c "Ha! {i}Me{/i} breaking up with {i}you?{/i} After that huge freak-out I had in the cafeteria? As-if!"
    s "What’s this about then? This feels...weird."

    scene chikatres12
    with dissolve

    c "I was getting there...you need to let me finish."
    s "My bad, yeah. Go ahead. "

    scene chikatres13
    with dissolve

    c "So...I’ve been doing a lot of thinking. And I love how things are for us. I love what we have going and how...{i}whole{/i} you make me feel."
    c "Sure, there are moments when that’s hard. And I really wish I could share my happiness with other people, but...I totally understand why I {i}can’t{/i} since it puts you at risk."

    scene chikatres14
    with dissolve

    c "But, for the most part, things are amazing. {i}You’re{/i} amazing."
    c "Which is why I want to do more for you."
    s "I knew it. I knew the porn conversation planted a seed in your head and it was only a matter of time before-"
    c "Wrong again."
    s "Honestly, Chika, you might just have to suck my dick at this point. I don’t think I’m going to be able to guess this."

    scene chikatres15
    with dissolve

    c "You don’t have to guess, loser. Just listen to me."
    c "I want to do more for you, and...I think I might have figured something out."
    c "Originally, I wanted to tell you about this on Christmas since I couldn’t afford to get you a real present. But, like..."

    scene chikatres16
    with dissolve

    c "Ugh...I guess I’ve been beating around the bush {i}way{/i} longer than I thought since Christmas was months ago."
    s "It’s likely a little more complicated than that, but please proceed."
    c "Okay...I’ll tell you what I had in mind. But I need you to hear me out fully before you make your decision. That way, if you want something else, I can go back to the drawing board."
    s "Just tell me, Chika. I’m sure whatever it is is fine."

    scene chikatres17
    with dissolve

    c "Are you...interested at all in having a three-"
    s "Yes."
    c "...some."
    s "Yes."

    scene chikatres18
    with dissolve

    c "You answered a little quickly there, {i}lover.{/i}"
    s "I just think it’s an extremely thoughtful gift and that it would be wrong for me to refuse it."

    scene chikatres19
    with dissolve

    c "Are you sure it doesn’t make you uncomfortable?"
    s "Just to clarify- we’re talking about another girl, right? There’s not some other guy you want to rope into this, is there? "
    c "Obviously not. It’s a present for you, so it would totally be a girl. There are just a few issues with it that I think you might want to put a little more thought into first."
    s "Like?"
    c "Well, first and foremost, it would totally expose us. And I know how important keeping this all a secret was to you."
    c "Second, I just...wouldn’t want you to go through with it if it...feels weird for you."
    s "Why would it feel weird for me?"
    c "Because you’re so loyal."
    s "..."

    "Oh, Chika..."

    s "It might...be a little weird at first. But I’m sure it will all work out in the end."
    c "You’re absolutely positive? You don’t want a night to think it over or anything?"
    s "I’m positive. If anything, I’m surprised {i}you{/i} want to do this."

    scene chikatres20
    with dissolve

    c "Really? How come?"
    s "Because you’re insanely possessive. And you get jealous easier than...pretty much everyone other than Ami."
    s "I just figured you’d hate the idea of sharing me."

    scene chikatres21
    with dissolve

    c "Well, it wouldn’t be {i}sharing,{/i} for one. You’ll still be my boyfriend after all is said and done and I’ll still be your girlfriend. "
    c "There wouldn’t be any love at all for the second girl — she’d only be there to spice things up and help make it a special night for you."
    c "I might be a sex goddess, but it’s not like I have four arms, you know?"
    s "Is there...someone you had in mind for this?"
    c "I’m actually more interested in hearing who {i}you’d{/i} have in mind for this."
    s "That sounds like a trap to me."

    scene chikatres22
    with dissolve

    c "I promise it’s not. {i}But,{/i} I do implore you to think about this carefully. Because it should be someone we trust and someone who we think would actually do it."
    c "There are a lot of girls in our class, but I’m not sure if all of them would take kindly to finding out that I’ve been boning the teacher this whole time."
    s "And...{i}you’re{/i} going to be the one to bring this up to one of them? Not me?"
    c "I’ll do 100%% of both the scouting {i}and{/i} organizing. It’s {i}your{/i} present after all. All {i}you{/i} need to do is show up and let us take care of you."
    s "It sounds hard, but...I think I can manage that."

    scene chikatres23
    with dissolve

    c "Your acting needs a little work, [chikamaster]..."
    c "So...is there anyone who fits that criteria you want me to try and {i}enlist?{/i}"

    "I should think carefully about this..."
    "Who can I suggest that Chika might actually be able to convince?"
    "Just being someone we can trust isn’t enough. It has to be someone who won’t make her suspicious. "
    "There’s also a higher chance of success if it’s someone she gets along with, so..."
    "That leaves-"

    menu chikathreemenu:
        "Yumi":
            s "How about Yumi?..."

            scene chikatres24
            with dissolve

            c "Hmmmmm...{i}interesting.{/i}"
            s "That is not a normal face from you."
            c "Why Yumi? Is it the attitude? If you want me to be a little bit meaner to you in bed, all you have to do is ask, you know."
            s "I have several good reasons for this and I will now present all of them in a professional manner."
            c "You want to fuck my tsundere roommate. How cute."

            if day == 1:
                c "She's probably still out in the hall right now. Want me to go grab her?"
                s "After my presentation. This is important."

            s "First and foremost, your relationship with Yumi is one that would likely not be ruined by proposing such a thing, even if she were to turn it down."
            c "Mhm. Continue."
            s "Secondly, Yumi might think she’s the “boss” out of you two, but everyone knows it’s actually you. Which means you could probably talk her into it."
            c "Anything else?"
            s "Third-"
            s "Third, I just think she’s hot."

            scene chikatres25
            with dissolve

            c "Well, I can’t disagree with you there. I don’t know how successful I’d be in convincing her to go along with it, though. You know how hot-headed and stubborn she can be."
            c "All things considered, it’s a good pick. She’s probably who I would choose if it entirely were up to me."
            s "I mean...it kind of {i}is.{/i} You don’t {i}have{/i} to give me a choice here if you don’t want to."

            scene chikatres26
            with dissolve

            c "For the millionth time, this is for {i}you.{/i} And if you want to have a threesome with my best friend and me, it’s my duty as your girlfriend to try and make that happen."
            c "I’ll talk to her soon."
            s "Cool, but don’t tell her I had anything to do with this because I already know she’s going to yell at me for it."
            c "It’ll be hard for her to yell with your cock in her mouth."
            s "It is so strange that I’m hearing these words come out of your mouth right now."
            c "What can I say? I’m a catch."

            $ yumicthree = True

        "Rin":
            s "How about Rin?..."

            scene chikatres14
            with dissolve

            c "You know, I was actually going to suggest her."
            c "The only problem is Otoha. Those two have been doing a lot better lately and, even if I still don’t {i}care{/i} for Otoha, that sounds like a tough position to put Rin in."
            c "Like, if it weren’t for her girlfriend, she would fuck {i}both{/i} of us 100%%. Wouldn’t even have to be a threesome. But with Otoha around, we can’t even be entirely sure she’ll agree."
            s "Do you think it’s worth a shot?"
            c "I can talk to her, yeah. Worse comes to worst, I can just tell her I was fucking around and wasn’t being serious."
            c "Plus, I {i}very{/i} highly doubt she’d tell anyone since she’s really close to both of us."
            s "I mean...if you’re cool with this...yeah. Go for it."
            c "How long have you wanted to fuck Rin for?"
            s "I’m not answering that question."
            c "Good. Because {i}that{/i} was a trap."

            $ rincthree = True

        "Ayane":
            s "How about Ayane?..."

            scene chikatres27
            with dissolve

            c "Ayane? That’s certainly an interesting choice. "
            s "Is it? Think about it. She’s been openly obsessed with me forever. Everyone already {i}knows{/i} that she’s obsessed with me...and no one will think it’s weird if she starts saying stuff about threesomes."
            s "Which she probably wouldn’t even do in the first place since she’s honest and loyal as well."
            c "Well...it’s definitely true that she’d fuck you. But aren’t you a little worried there might be, like...actual {i}love{/i} involved if she’s there? Wouldn't that make things weird for all of us?"
            s "I think she’s smart enough to avoid that and...appreciate the situation for what it is."

            "No I don’t. "
            "And, honestly, I’d feel a little bad asking her to join in on sex with Chika and me shortly after telling her about it. "
            "But hey, she already knows so it’s not like she’d be blindsided and go and tell everyone else."

            c "You must really have a thing for blondes, huh?"
            s "It kind of just worked out that way."

            scene chikatres14
            with dissolve

            c "Well, Ayane is definitely cute. And she’s certainly hyper enough that it would probably make things really interesting for us. "
            c "But she might be a little harder to enlist since the two of us aren’t very close. "
            s "I doubt it will be hard at all the moment she finds out I’m involved, but I’d be willing to talk to her instead if-"
            c "Nuh-uh. Your job is to relax and let me handle all of this."
            c "You want to have a threesome with Ayane and me? I’ll make it happen."
            c "But don’t get mad at me if it turns into a contest and I kick her out of the room halfway through. I {i}am{/i} the jealous type after all."

            $ ayanecthree = True

        "Tsubasa" if chikalust25 == True:
            s "How about Tsubasa?..."

            scene chikatres28
            with dissolve

            c "Tsu...basa?"
            s "Does...that answer surprise you?"
            c "Honestly, I wasn’t even considering girls outside of the class. So...yeah."
            c "You really want me to...ask my new mother figure if she’ll have a threesome with us? "
            s "Are you trying to tell me you haven’t at least {i}thought{/i} about it? "
            s "I saw the way you blushed when she forced you into her chest at your apartment. There are definitely some non-daughterly feelings there, Chika."

            scene chikatres29
            with dissolve

            c "In my defense, Tsubasa is very soft and I had the great privilege of our first conversation being completely nude. So yes, I {i}have{/i} thought of things like that before."
            c "But it’s not exactly easy to approach an adult as a high school girl, let alone one who’s like a mom, and ask her to fuck the teacher with you as a Christmas present."
            c "How would I even start that conversation? "
            c "Hey Tsubasa, I like your top. It would look better on the floor of my dorm room while we’re both sucking my boyfriend’s dick. Then later, I can cry and tell you more sad stories about my life. Love you!"
            s "Sounds like a fool-proof approach to me. No one in their right mind would be able to say no to that."

            scene chikatres30
            with dissolve

            c "I don’t know, Sensei...I feel like this could backfire."
            s "You’re aware that she hung around after barging in on our hardcore petplay sex, right?"

            scene chikatres31
            with dissolve3

            c "She {i}what?{/i}"
            s "Saw it all. Enjoyed the show enough to keep on watching."
            c "But I...I was {i}barking...{/i}"
            s "Maybe she’s into that?"

            scene chikatres32
            with dissolve

            c "I can never face her again. Our relationship is over."
            s "{i}Unless...{/i}"

            scene chikatres17
            with dissolve

            c "You’re 100%% sure that’s who you want? Tsubasa. Not Touka."
            s "Consider it a challenge. I sense chemistry there and I want to exploit it."
            c "..."
            s "..."

            scene chikatres25
            with dissolve

            c "Okay. Fine. I’ll talk to Tsubasa. "

            "{i}Yes.{/i}"

            c "But if you lied to me about her watching us and this blows up in my face, I will destroy you. Sexually, of course. But in a way that is not very pleasant for you and will likely scar you for life."
            s "I’m...afraid of finding out what that means."
            c "Then let’s hope this works."

            $ tsubasacthree = True

        "Chinami" if sawchinami == True:
            s "I..."
            s "I don’t know if you’ll like my answer."

            scene chikatres14
            with dissolve

            c "Oh, come on. I won’t judge you for your tastes. You know me better than that."
            c "Even if it’s Ami or something, I won’t mind. It’s not like she’s your {i}daughter{/i} or anything. I’m sure there are plenty of uncles who fuck their nieces out there."
            s "It’s worse."
            c "Just tell me. Come on."
            s "It’s not a good idea, Chika. "
            c "Why not? It’s not like you’re asking me to-"

            scene chikatres33
            with dissolve

            c "Oh my god."
            s "..."
            c "It {i}is{/i} like you’re asking me to get my little sister in on this..."
            s "I told you it wasn’t a good idea."
            c "..."
            s "Do you see now why I didn’t ask?"
            c "Are you..."
            c "You’re not, like...serious, are you? You’re just...you’re joking, right?"
            s "..."
            c "Chinami’s a {i}kid{/i}, Sensei. And like, I get that by some metric I am too, but that’s a totally different-"
            s "I’m not serious. Don’t worry."

            scene chikatres34
            with dissolve

            c "You’re...you’re not?"
            s "Of course not. I just wanted to see what your reaction would be."
            c "By...lying about...having a threesome with my kid sister? You were telling a joke?"
            s "..."
            c "Do you not realize how fucked up that is?"
            s "I do. Which is why I tried backing down and wasn’t going to say anything. But then {i}you{/i} filled in the blanks, so..."
            c "..."
            s "Anyway, let’s move on."
            c "Yeah...let’s."

            scene chikatres35
            with dissolve

            "My eyes fixate on the corner of the room."
            "I do this at night sometimes when my thoughts wander off in directions I don’t want them to."
            "I just stare...and I stare and I stare and I stare...until I can’t hear them anymore."
            "But sometimes they find their way back."
            "And they start pushing me in directions I never thought I’d walk."

            s "..."
            c "..."

            "If she had agreed..."
            "If she had not been so appalled..."
            "What would I have done?"

            c "At..."
            c "At the end of the day, if you {i}really{/i} can’t think of anyone...I can just, like...try and find someone myself."
            c "All that matters is we-"
            s "Chika, I don’t mean to interrupt, but I really don’t want things to be weird with us after one bad joke."

            scene chikatres36
            with dissolve

            c "Sensei, it is {i}my{/i} job to protect Chinami. And I really don’t think you’ll be able to convince me in any way that what you just suggested, joke or not, was even remotely acceptable."
            s "I’m sorry. It won’t happen again."
            c "Promise me. Promise me it won’t happen again."
            s "I...I promise."

            scene chikatres37
            with dissolve

            c "{i}Hah...{/i}okay."
            c "I trust you."
            c "But, as I was saying-"

            $ chinamicthree = True

    scene chikatres38
    with dissolve

    c "At the end of the day, what really matters is making things fun for {i}everyone.{/i}"
    c "This will be a new experience for all of us, so...it’s important we’re understanding and blah, blah, blah. You don’t care about this part. You just want to get your dick wet."
    s "Correction: I want to get my dick wet in the company of my loving significant other who is giving me an amazing and thoughtful present."

    scene chikatres39
    with dissolve

    c "Oooh? Maybe I should bring up threesomes more often if it’s going to make you {i}this{/i} nice?"
    s "You’re learning too many tricks to control me. "
    c "Pretty soon, I’ll have you eating out of the palm of my hand."
    s "Let’s not go that far."
    c "How far do you think you’ll go with girl number two?"
    s "Is...there a limit on how far I’m {i}allowed{/i} to go? I don’t know your threesome rules."

    scene chikatres24
    with dissolve

    c "Rules are lame. If we’re gonna do this, we’re gonna {i}do{/i} this."
    s "And you won’t get jealous?"
    c "I admit there might be some pushing and shoving involved if I’m feeling a little neglected. But you can avoid that by paying more attention to me than her."
    s "That goes for you too, you know. I don’t see a single male on your wall. For all I know, you might prefer females in general."
    c "Maybe I do? We’ll find out soon. "
    s "..."
    c "..."
    s "Quick question, on the off-chance I was able to get Niki Nakayama to sign up for a threesome with us instead of the girl we’re going with, how would you feel?"

    scene chikatres40
    with dissolve

    c "Extremely, intensely, dramatically, impossibly wet."
    c "But it’s not going to happen. She’s an angel and her vagina is so tight that it won’t open for human beings who aren’t deemed worthy by a higher power."

    "Shout-out to whoever deemed me worthy, I guess."

    s "But...what if I defied those expectations of yours and somehow got her to sign on?"
    c "Sensei, if you think that much about fucking Niki, which I wouldn’t blame you for since I do that pretty much every night before I go to sleep, I can send you the link to a Facebook group I’m in."
    s "I am somehow not surprised you’re in that group."
    c "Huh? You know about the group already? I thought you weren’t on social media?"
    s "I learned about it from Niki."
    c "No you didn’t. Niki doesn’t know about the group. It’s invite only. And she doesn’t know about you either."
    s "She knows about the group. She also knows about me — and has been in love with me, just like her sister, for basically her entire life."
    c "Haha. Funny joke. But you’re obviously lying. Niki’s never had any male friends. She prefers girls."
    s "Then...who do you think all of her songs are about?"
    c "The fandom as a whole. She loves us so much that she has no need for true romance and our existence to her is akin to the physical manifestation of her dreams come true."
    c "She said that in an interview once. I have it recorded."
    c "Also, your penis would burst into the flames the moment it came into contact with her, so I wouldn’t even think about it if I were you."
    s "But...if I could get her to agree to a threesome-"

    scene chikatres41
    with dissolve

    c "Do you want your penis to burst into flames?! I told you to stop talking about the queen that way!  We both know damn well that we’re unworthy!"
    s "I just can’t think of a better time to tell you that Niki and I are actually childhood friends who-"
    c "You think I haven’t heard that same story a bazillion times before?! I {i}wrote{/i} that story! Just because it’s real to you doesn’t mean it’s real to...reality!"
    s "You know, maybe I’ll just call her and-"

    scene chikatres42
    with dissolve

    c "You so much as {i}touch{/i} that phone and I’ll kill you. I don’t know who you got to sign up for this, but I refuse to be pranked just minutes after giving you a big, important, relationship-changing present!"
    s "Aren’t you overreacting a little bit?"

    scene chikatres43
    with dissolve

    c "Overreacting?! This demon was dormant until you uttered the magic words!"
    c "No one casually talks about having sex with the queen and gets away with it! You’ll pay for those words, you limp-dicked fuck!"
    s "Wow. Okay. Find out the hard way. See how that works out for you."
    c "Fine! I will! Because you’re a liar and you’re lying to me! What’s your name in the group?! I’m an admin and I’m getting you kicked out!"
    s "You know, this whole time I was thinking you were overprotective of {i}me.{/i} But if this is how you act toward a girl you haven’t even met-"
    c "I don’t need to meet Niki to connect with her on a personal and spiritual level! She speaks to me through music and {i}art{/i} and I can feel her in my bones!"
    s "No offense, Chika, but I think you might actually be insane."
    c "I’m not insane! I’m just mad you’d come into {i}my{/i} room and desecrate {i}my{/i} walls with all of your lies! "
    c "Apologize to Niki!"
    s "I can’t. You won’t let me call her."
    c "Niki doesn’t have a phone! She doesn’t need one when her love is all around us!"
    s "Then how does she order a pizza?"
    c "Radio waves!"
    s "Are all idol fans like this? "
    c "Yes!"
    s "Can you please stop yelling at me now?"
    c "No!"
    s "Why not?"
    c "Because I am {i}super{/i} fucking turned on right now!"
    s "..."

    scene chikatres44
    with dissolve

    c "..."

    play sound "static.mp3"
    scene chikatres45 with flash
    stop sound

    c "AHH! AHH! AHH! AHH! AHH! "
    c "FUCK...OH FUCK! HAH! YES! JUST LIKE THAT! FUCK!"
    c "ANGRY SEX...IS AMAZING! HOLY SHIT!"

    "And so the night ends like this..."

    scene black
    with dissolve2

    "But soon, it will end with another beside us."
    "Or Chika will fail and we’ll return to this mattress alone."
    "Either way, life will move on...but some aspects of it will remain buried beneath the soil."

    stop music

    "What will happen when that soil turns to mud?"
    "What worm-covered secrets will we pull from out the earth? "

    $ renpy.end_replay()
    $ chikadorm45 = True
    $ chika_love += 1
    $ chika_lust += 1

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "{i}Chika’s lust has increased to [chika_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label chikaspring1:
    play sound "static.mp3"
    scene chikafurious1 with flash
    stop sound
    play sound "thump.mp3"
    with hpunch

    c "{b}You creepy, clingy, incestuous bitch! Who the {i}fuck{/i} do you think you are?!{/b}"
    a "Ami Arakawa! Were you not paying attention to my introduction?"
    y "Chika...chill. Don’t do anythin’ you might regret. She’s obviously off her fuckin’ rocker. Ain’t nobody takin’ her seriously right now. Just let it go."
    n "Ami...maybe you should listen to Sensei and go home early today?"
    c "No, fuck that! I’m not gonna let her get away with standing up there and making {i}everyone else{/i} in this room feel small just so {i}she{/i} can feel wanted for the first time in her miserable fucking life."
    y "Chika, seriously. Don’t do this."
    a "Chika, if you have a question, you’re supposed to raise your hand. I can’t call on you if you don’t do that!"

    scene chikafurious2
    with dissolve

    c "Miss Arakawa! I have a question."
    a "Yes, Miss Chosokabe! What is it?"
    c "Just out of curiosity, how does it feel knowing your uncle isn’t ever going to fuck you and that your sheer existence is causing him an excruciating amount of pain?"
    a "I’m not sure I understand. Didn’t you hear him talking about how good of a job I did just a few minutes ago? Or were you too busy pretending he’d rather sleep with {i}you{/i} instead? Because that’s just sad."

    scene chikafurious3
    with dissolve

    c "I’m going to rip your spine out."
    y "Fuck it. Let {i}me{/i} handle this. It ain’t gonna make a difference if {i}I{/i} get kicked outta school again. Yo, Ami! Why don’t you tell me again what you just said about my best friend?!"
    to "Both of you, please settle down. We can solve this without violence."
    c "Touka, I love you, but stay the fuck out of this. "
    y "Yeah, me and Chika have this shit on lock."

    scene chikafurious4
    with dissolve

    c "You stay out of this too. I’d prefer to be the one to teach her a lesson today, thank you very much."
    a "Oooooh, yeah. Really sorry about that, but my speech isn’t over yet. I haven’t gotten to the part where I talk about what I’ll do to all of you {i}after{/i} I remove your organs."

    scene chikafurious5
    with dissolve

    c "Then why don’t I come a little closer so you can tell it to me personally?!"
    y "Chika, come on! You’re better than this!"

    play sound "static.mp3"
    scene chikafurious6 with flash
    stop sound

    a "No, I don’t think she is. In fact, I’m starting to think she’s the most obsessed out of all of you. "
    a "Hate to break it to you, Chika, but Sensei doesn’t have very much money. So why don’t you be a good little girl and go dig for gold somewhere else. Okay? Okay!"
    c "You think I care about his {i}money?{/i} Is that how it looks to you? "
    a "That or you’re just a slut. Which, you know, really wouldn’t be all that surprising since your costumes at all of our holiday parties always come off as super desperate and icky."
    c "Almost as {i}desperate and icky{/i} as forcing your uncle to come with you into dressing rooms. Or getting up in front of the class and pretending like you have {i}any{/i} say in who he does or doesn’t sleep with."
    ima "Senpai, what the fuck is going on right now?"
    s "I don’t...I..."
    a "Why wouldn’t I have a say in that? As his future wife and the mother of his children, I think I have the right to express disinterest in him cheating on me. Even {i}if{/i} he’s cheating down."
    a "Like way down. Beneath the poverty line. "

    scene chikafurious7
    with dissolve

    c "He’s not your plaything, you psychotic cunt! He’s a man! A good man! And he’d never stoop to the levels you’re insinuating! Not everyone is as deranged as you, Ami! Not everyone wants to fuck their family!"
    a "Stop yelling, you’re scaring me~"

    scene chikafurious8
    with dissolve

    c "Bitch, you {i}should{/i} be scared. ‘Cause I ain’t fuckin’ around anymore, Ami. And I will gut you like a fucking {i}pig{/i} if you think for a second that you can tell me what to do with {i}my{/i} life."

    scene chikafurious9
    with dissolve

    a "I’m not telling you what to do with your life. Just that Sensei doesn’t have any interest in you or anyone else because you’re all gross and he loves me. "
    a "And that ignoring his interests {i}may{/i} lead to some light organ removal as I will interpret it as an attack on his well-being."
    c "Have you considered at all that maybe {i}you’re{/i} what’s damaging his well-being? Because I recall you mentioning something about him calling you...what was it again? Suffocating?"
    c "And he’s never said anything like that to {i}me.{/i} So I think this might be a you problem. And I think that maybe {i}you{/i} should stay as far away from your uncle as humanly possible. "

    scene chikafurious10
    with dissolve

    c "The bottom of the ocean might be a good fit. I can help you get there, you know. ‘Cause I might be poor, but concrete’s pretty cheap. An 80lb bag only goes for ¥1,000 last time I checked."
    ki "How the fuck does she know that?"
    y "Hell if I know. This is exactly why you don’t fuck with Chika."
    ima "Easy on the death threats, okay? I’ve accepted that today is just gonna be “drama day,” but there are like...ten different lines you guys shouldn’t cross and you’re standing on all of them right now."
    s "Both of you...stop. Please."
    c "You gonna open your eyes, Ami? Or are you just gonna keep standing there smiling like a fucking-"

    scene chikafurious11
    with dissolve

    a "This you?"
    c "Huh? Wha-"

    scene chikafurious12
    with dissolve

    ima "Hm? What’s she got there?"
    c "You..."

    scene chikafurious13
    with dissolve2

    c "{i}You went through his fucking phone?...{/i}"
    r "What’s Ami showing her? I can’t hear from all the way back here."
    f "I can’t...really tell..."
    no "I think I know what’s happening right now. And it makes me sad to know that I’m the only one who appreciates the beauty of this perfect full circle."
    ima "Senpai?..."
    a "Cute picture, Chika. Blonde suited you way better than whatever you have going on right now."
    c "You...are {i}dead.{/i} Do you hear me?"

    scene chikafurious14
    with dissolve

    a "What was that? I’m gonna need you to speak up."

    scene black
    with dissolve2

    s "Both of you. My office. Now."

    "I push past Imani and grab Chika’s arm before she’s able to attack Ami. Meanwhile, Imani and the others look on in shock."
    "I can’t tell you what’s going through their heads. And I don’t have the time to sit here and think about it right now. Not while two girls I love are trying to kill each other."

    play sound "doorslam.mp3"
    scene chikafurious15 with hpunch

    "Is this the right time to talk about love? To question its validity? To ask what exactly it means?"

    c "You disgusting, little demonspawn! You probably touched yourself to that picture, didn’t you?! Hope you liked it since it’s the closest you’ll ever get to Sensei’s dick, you fucking monster!"

    "No. Now is probably not the right time."
    "But I’m sure we’ll touch on it later since the thought of love as a whole right now just makes me want to puke."

    a "I’ve seen his penis a zillion times. We live together, remember? It’s not like I lied and manipulated him into showing me like you had to."
    c "Someone could have seen that, you fucking moron! You could have ruined his career! "
    a "See? I knew you were only concerned about his money. So how about this? I'll give you my next week’s allowance, and you can use it to go fuck off where you can’t bother us anymore."

    scene chikafurious16
    with dissolve

    c "Sensei! Let go of me so I can fucking kill her! She’ll expose {i}everything{/i} at this rate! "
    a "Awwww, she thinks there’s more to your relationship than just unwanted nudes and forced physical contact. "
    c "Do you hear this shit?! Because if {i}you’re{/i} just going to let her say it, at least give {i}me{/i} the pleasure of knocking her teeth out!"
    s "Don’t hit her, Chika. She needs help. She isn’t always like this."
    c "What do you mean she “isn’t always like this?!” Because she sure as fuck seems like the crazy, obsessive freak she’s always been to me!"
    c "We all know she wants to fuck you! You know it too! But we let it slide and never did shit about it because we always thought it was harmless! But it isn’t fucking harmless anymore, Sensei!"

    scene chikafurious17
    with dissolve

    c "She’s {i}trying{/i} to hurt us now! She’s weaponizing her ditzy fucking cuteness and gaslighting you into thinking she’s helping when all she’s {i}really{/i} doing is making everything worse! "
    a "Oh, give me a fucking break. You wouldn’t last five minutes in my shoes. You’d see how much work it is and then fuck off to the next hot, big-dicked guy who’s willing to pay for your phone bill."
    a "Which I canceled, by the way. Your service should be shutting off tomorrow or the next day. But hey, maybe you can start selling your nudes or something. You sure seem to like taking them."

    play sound "tackle.mp3"
    scene chikafurious18
    with hpunch

    c "{b}KANTOTERO!!!!!!!! ANAK NG PUTA!!!!!!!!!! SIPSIPIN MO ANG TITI KO!!!!!!!!!!!{/b}"
    a "Awwww, I love you too! I just love you more when you’re not tricking my uncle into thinking you actually care about him."
    c "You have no fucking clue what you’re talking about, Ami! What he and I have is bigger and better than {i}anything{/i} you’ll ever get from him! You’re just a jealous little cunt who doesn’t know her place!"

    scene chikafurious19
    with dissolve

    a "My place is beside my uncle. Which is something {i}you’ll{/i} never understand since you don’t know the first thing about where his pain comes from."
    a "None of you do. But you all {i}loooooooove{/i} to pretend that you’d be fine swapping places with me because the side of him {i}you{/i} know is a facade. And you probably think it’ll just be more of that."
    a "But that’s just the thing, Chika. The person I take care of and the person you pretend to “love” aren’t the same. They just have the same shell."

    scene chikafurious20
    with dissolve

    a "The problem is, I really like that shell. And I don’t want you to mess it up with all your cheap makeup and perfume and stuff."
    a "So if you could do me a favor and mind your own fucking business from now on, that’d be really swell. Oh, and since the rest of the girls seem to like you, let {i}them{/i} know playtime’s over too."
    a "Because I might not have Sensei’s phone anymore, but that doesn’t mean I won’t notice if he disappears into the bathroom with it for an...{i}extended{/i} period of time."
    c "Bullshit. I’m the only person who sends him anything like that. Right, Sensei?"
    s "..."
    a "Sensei! Chika asked you a question."

    scene chikafurious21
    with dissolve

    c "Right?"
    s "..."
    a "He’s hiding something when he stays quiet like that."

    scene chikafurious22
    with dissolve

    c "E-Even if he is...it doesn’t change that you’re a fucking maniac and that you’ve gone so far out of line this time that I should wring your fucking neck."
    c "But out of respect for Sensei, I won’t."
    a "Aww, how kind."
    c "To be clear, I won’t {i}this{/i} time. But if I find out that you’re {i}still{/i} being a fucking creep when you walk out of here today...and doing {i}more{/i} shit that puts him in an uncomfortable position-"

    scene chikafurious23
    with dissolve

    c "I will flay the skin from your body and feed it to the homeless people outside of my house. "
    c "And {i}yes.{/i} There {i}are{/i} homeless people outside of my house. {i}Yes,{/i} I am poor as shit. {i}Yes,{/i} Sensei paid for my phone bill up until you canceled it..."
    c "But don’t you {i}dare{/i} insinuate {i}that{/i} being the reason I’m in love with him."
    a "Oh, I didn’t mean to insinuate you being “in love” with him at all. So I’m sorry if it came across that way. But thankfully, you’ll be staying away from now on. Right?"

    scene chikafurious24
    with dissolve

    c "Not. A. Fucking. Chance."
    a "Hm."
    a "I was afraid you’d say something like that."
    s "Ami, go home."
    a "..."
    s "Now."
    a "Are you gonna fuck her, Sensei?"

    scene chikafurious25
    with dissolve

    c "I’ll be sure to send you a picture if and when he does."
    a "This is {i}really{/i} how you want to celebrate being out in the world again? Sex with...{i}her?{/i} Wander down any narrow alley in the urban district and you can find someone twice as hot for half the price."
    s "What I do with my own time is none of your business.  "
    a "Yes it is. "
    c "No it’s not."
    a "Yes it is."
    c "No it’s not."
    s "Shut up. Both of you. "
    s "Ami...I think we need to stay at home for a little while longer. And I think {i}you{/i} need some rest before you start acting out even worse than you did today."
    a "Oh, this wasn’t bad at all. But I agree. We should spend more time alone, Sensei. "

    scene chikafurious26
    with dissolve

    a "I’ll warm up your onahole so you can have something to relieve yourself into when having sex with Chika feels more like throwing a hot dog down a hallway."

    scene chikafurious27
    with dissolve

    a "That is, unless you want to relieve yourself in {i}me.{/i} But you’d neeeeeeever want to do that because you’re not attracted to your family. Riiiiiiight?"
    s "Go. Home."
    a "Boooooooooooring! You’ll call me when you’re on the way, right? You’re leaving right after me?"
    s "Yes, I’ll call you. Just leave."
    a "Okaaaaay! Love you, Sensei!"

    play sound "dooropen.mp3"

    s "..."

    play sound "doorslam.mp3"
    with hpunch

    c "..."
    s "I’m...so sorry you had to deal with that."
    c "Sorry?..."
    s "..."
    c "You think saying {i}sorry{/i} is going to make me feel better?"

    play sound "static.mp3"
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene chikafurious28 with flash
    stop sound

    c "You leave me in the dark for two fucking months and the first thing I get when you come back is an argument with your niece and the revelation that you have nudes from {i}other girls{/i} on your phone?!"
    c "You didn’t even think to tell me about that?! How long have they been on there?! Whose are they?! Are you responding?! Are they just sending them to you out of nowhere?! What the fuck?!"
    s "Chika, I think the Ami thing is a more pressing matter than that right now."
    c "They’re both “pressing matters,” asshole! I’ve been looking forward to this reunion since the second I found out you weren’t feeling well, but {i}now{/i} I just feel like another face in the crowd!"
    c "Did you miss me {i}at all?{/i} Did you even think about me {i}at all?{/i}"
    s "Chika, I didn’t think about {i}anything{/i} at all. I’ve been in what was effectively a coma. I hadn’t even taken a real bath until just a few days ago."

    scene chikafurious29
    with dissolve

    c "Well, what the fuck happened?! What could you have possibly lost that hurt you that badly?! Was it a family member? A friend? What happened, Sensei?"
    c "I can’t help you if I don’t know what-"
    s "You wouldn’t be able to help me even if you did."

    scene chikafurious30
    with dissolve

    c "But Ami {i}can?...{/i}"
    s "Better than you can, at least. And I really {i}hate{/i} saying that after everything I just saw her say to you and everyone else, but she’s right about one thing — you guys {i}don’t{/i} get it."
    s "She and I have been together forever, and she’s seen me at my worst. She knows better than anyone the things that hurt me and...she creates an environment where they don’t have to."

    scene chikafurious31
    with dissolve

    s "But it’s not a {i}good{/i} environment. It doesn’t {i}fix{/i} me. I just wind up feeling numb and broken until something forces me out of bed again."
    c "What was it that forced you out of bed this time?"
    s "An angel with scissor wings and spider legs."
    c "I don’t get it."
    s "Neither do I. But the point is that Ami is just as broken as me, Chika. And instead of being stuck in bed for two months, she’s lashing out like this and trying to shape the world back into what {i}she{/i} wants."
    c "Yeah, but what she wants is your dick. And a lifetime worth of nothing but you. It’s unrealistic, irrational, and entirely selfish."
    s "And that’s just the kind of girl she is."
    c "So, what? You want me to just...{i}like{/i} her? Because I seriously {i}will{/i} kill her if she pulls that shit again, Sensei. I don’t care about the consequences."
    s "Then you’re just as unrealistic, irrational, and selfish as she is. You have a sister to take care of."
    c "And a boyfriend."
    s "I can take care of myself."
    c "Apparently not if Ami’s the only one who’s able to help in that department."
    s "Chika-"

    scene chikafurious32
    with dissolve

    c "Listen...I don’t want our first day back together to be a big fight, so I’m just going to go home. I don’t know if you’ve heard, but I haven’t been showing up all that much lately anyway."
    s "Because of me, right?"

    scene chikafurious33
    with dissolve

    c "Well, obviously! It’s kind of hard to focus when I can’t stop worrying!"

    scene chikafurious32
    with dissolve

    c "But...you’re okay now. Well, not {i}okay.{/i} But...you know what I mean. And just knowing that helps...{i}way{/i} more than you can imagine."
    s "I’m sorry you had to worry, Chika. I’m sorry for everything."

    scene chikafurious34
    with dissolve

    c "If you’re really sorry, you’ll babysit for me tomorrow."
    s "What?"
    c "I said, if you’re really sorry-"
    s "I heard what you said. I just...don’t think I’m really in the correct mindset to be babysitting right-"
    c "Well, then I guess you’re not sorry and I guess I’m going to have to kill your niece."
    s "..."
    c "..."
    s "Fine. But after that, I need to stay with Ami. Okay?"

    scene chikafurious35
    with dissolve

    c "We’ll see."
    s "..."

    scene chikafurious36
    with dissolve

    c "Also, my address is going to be a little different. But I’m closer to you now, so..."
    s "You moved?"
    c "I’m {i}moving.{/i} My boiler busted so I was going to take some of mine and Chinami’s stuff to the new place after school today. Guess I’m able to get started early now, huh?"
    s "Does this...new place happen to be-"

    scene chikafurious37
    with dissolve

    c "You’ll see tomorrow. It’s a {i}surprise.{/i}"
    s "..."

    scene chikafurious38
    with dissolve

    c "Well...I guess I’ll be going then."
    s "And I guess I’ll see you tomorrow."
    c "Poison Ami’s water for me."
    s "I don’t think I can do that, Chika."
    c "Rats."

    play sound "dooropen.mp3"
    scene chikafurious39
    with dissolve

    "Chika leaves without saying anything else, and..."
    "Suddenly, I’m alone again."
    "For a second, it’s like nothing even changed."
    "But the air feels a little bit heavier."
    "My plant in the corner of the room looks dryer than normal. "
    "And I-"

    play sound "dooropen.mp3"
    scene chikafurious40
    with dissolve

    c "Hey. You don’t by any chance want to have sex right now, do you?"
    s "Not right now, Chika."
    c "Fair. I just wanted to make sure."

    play sound "dooropen.mp3"
    scene chikafurious39
    with dissolve

    "And I-"
    "..."
    "What was I saying again?"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Oh, right."
    "I have one less student to worry about than I used to."

    $ renpy.end_replay()
    $ chikaspring1 = True
    $ chika_love += 10

    "{i}Chika’s affection has increased by 10!{/i}"
    "........."
    "......"
    "..."

    jump rinspring1

label chikaspring2:
    $ day = 2
    $ totaldays += 1
    hide monday onlayer date
    show tuesday onlayer date

    scene sanatochika1
    with dissolve4

    "It isn’t often that I wake up in unfamiliar rooms, but it {i}is{/i} often that I feel out of place."
    "This is strange on one hand, and all too common on the other."
    "And as I lie here in bed with a girl half my size and half my age, I come to terms with the fact that I have never been pure."
    "I was born just as everyone else — with original sin and a cord attached to my belly. But while one was severed and left to decay in a dumpster somewhere, the other sits with me to this day."
    "It’s never bothered me before. Knowing I had never had a chance, I mean. Because, when it really comes down to it, there isn’t a single person on the face of this earth that’s truly pure."
    "I thought there was once."

    play sound "static.mp3"
    scene sanaisbetternow27 with flash
    scene sanatochika1 with flash
    play music "sidecharacter.mp3"
    stop sound

    "But I was just deluding myself."
    "I latched onto something that felt impossible and out of reach. But in my head, it was more like I was latching onto the idea of holding something I knew I couldn’t have."

    scene sanatochika2
    with fade

    "What I know now is that there is nothing I can not take."
    "It’s that I {i}should have{/i} taken something when I was told to."
    "Because if I had only listened to directions, the girl beside me might be different right now."
    "And while their sizes are similar, I can’t imagine one as the other even when I close my eyes."
    "I know this to be true, because I tried all throughout the night."

    play sound "knock.mp3"

    sar "Sana! Are you still asleep in there? It’s half-past nine already!"
    s "..."
    sa "..."

    play sound "knock.mp3"

    sar "Sana, don’t you have school today? You’re gonna be late! You need to get up!"
    s "..."
    sa "..."
    sar "{i}Hah...{/i}Fine! You can stay home! But I have things to do, so I won’t be here to make you breakfast whenever you decide to get out of bed! Got it?!"
    sa "..."
    s "..."
    sar "{i}Ah, who am I kidding? It’s not like she can hear me.{/i}"

    "Sara’s footsteps fade away, only to be replaced by the creaking of her stairway seconds later."
    "Part of me wished she would have opened the door. That she would have seen me here in bed beside her daughter, with nothing more than a thick blanket covering the two of us."
    "But even this I get away with."
    "I’m practically invincible."

    play sound "vibrate.mp3"

    s "..."

    "But only practically."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene sanatochika3
    with dissolve2

    s "..."
    s "That’s not as many as I thought."

    "I wonder if Ami got any sleep last night."
    "I can’t imagine she did. But the last call from her came in around 6:00 AM, so I guess it’s possible she finally crashed after being hysterical for so long."
    "Or she’s dead."
    "If that’s the case, I’ll probably just end it today as well."
    "I got to knock Sana off my bucket list, so at least I’d be going out with a bang. Just not {i}literally{/i} as we didn’t have sex last night."
    "It’ll happen soon, though."
    "She’s the type who won’t ever say no."

    scene black
    with dissolve2

    s "What am I doing?..."

    play sound "vibrate.mp3"

    "The phone begins to vibrate once more."

    s "..."

    "But it’s not who I expect it to be."

    scene sanatochika4
    with dissolve2
    play sound "phonebeep.wav"

    s "Hello?"
    c "Hey! Are you just waking up now? You sound tired."
    s "I had a long night."
    c "Because you were burying Ami’s body in a ditch somewhere? God, please tell me that’s it."

    scene sanatochika5
    with dissolve

    s "Something like that."
    c "Awesome! That means I might get to work a double today. You don’t mind staying a little longer, do you? Chinami’s super excited to see you."
    s "Oh, right. Babysitting."
    c "Babysitting, indeed. I’ll send you the new address just as soon as I’m done with my makeup. Don’t worry about travel time, though. It’s waaaaay closer than my old place. Way nicer too. You’ll love it."
    c "Can you come now? Should I make some coffee for you? "
    s "..."
    c "Sensei? You there? You didn’t fall back asleep, did you?"
    s "No, I’m here."
    s "..."
    s "I can come now."
    c "Great!"

    scene black
    with dissolve2

    c "Go ahead and get ready then. And, if you get here early enough, I might even have a little surprise in store for youuuuu~"
    s "Is it sex?"
    c "Not this time, unfortunately. But {i}God{/i} I wish it was. I’ve been literally dying without you. "
    c "{i}And between the two of us, I didn’t touch myself at all the whole time you were gone~{/i}"
    s "Oh yeah?"
    c "{i}Yeah...so you can bet I’ll be extra eager to ride your big, hard-{/i} PANCAKES!"
    s "...My what?"
    c "Sorry! Gotta go! Chinami’s breakfast is burning!"

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve2

    "Chika hangs up the phone and sends me her new address a few minutes later."
    "As expected given the Tsukiokas’ ability to “make things happen,” she’s in the same building as me. "
    "But thankfully, she’s on a different floor. So at least I’ll have that layer of privacy in...a building I barely spend any time in to begin with."
    "But...maybe that will change."
    "Ami doesn’t know about it yet, so I could always disappear there if I need to get away from-"
    "No. No, I shouldn’t think that. I don’t need to get away from her. I love her. And right now, she needs me. "
    "Right now, she’s hurting and..."
    "..."
    "And..."
    "..."
    "I put my clothes back on...and cover the rest of Sana’s body with the blanket."
    "She doesn’t move a muscle."
    "But when she finally wakes up, I hope she thinks of me."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "And our house inside of my head."
    "........."
    "......"
    "..."

    scene sky
    with dissolve2

    "I make it there by 10:30, but I’m surprised to find a completely empty parking lot without a single moving truck in sight."
    "Maybe Chika’s the first one to move in apart from me? I still have no idea what Touka’s plan is- or {i}was,{/i} considering that she likely didn’t stop just because I was bedridden."
    "..."
    "I wonder how she’s doing."
    "And I wonder how she felt about my last ditch effort to regain some sanity by leaning on her during the Halloween party."
    "I hope she didn’t mind."
    "If only I was brave enough to ask her."

    scene sanatochika6
    with dissolve2
    play music "love.mp3"

    c "Well, look who it is! And without his mosquito of a niece buzzing around him this time!"
    s "Hey...and...Touka’s here too, I see."
    ch "And Chinami! Hi, Papa! Chinami missed you lots and hopes you’re feeling better now!"
    to "Good morning, Sensei. I was just explaining some things about the apartment complex to Chika as I’m the new owner of this building and will be renting out several units to low-income families."

    scene sanatochika7
    with dissolve

    to "That’s not offensive language, is it? “Low-income families?” Do you prefer “lower class” instead?"
    c "Definitely not. Low-income is both accurate and preferred over the latter. And thanks again for making this place affordable, Touka. It really means a lot to us."
    s "You’re really okay with living here? I thought your place in the old district, like...held a lot of sentimental value and whatnot?"

    scene sanatochika8
    with dissolve

    c "It did. But staying there forever just...wasn’t going to be possible. Especially with the place practically falling apart over the last couple months. "
    c "But, on the bright side, {i}this{/i} place is so cheap that I can keep both of them. At least for a little while, I mean. Which is great since it gives Yumi a place to stay as well when she doesn’t want to be here."
    s "Yumi? She’s staying at the old apartment?"

    scene sanatochika9
    with dissolve

    c "Kinda? I actually think she likes the old district for whatever reason. And I’m pretty sure she’s trying to get a job at the convenience store since Noriko brought up an opening there to her."
    c "So I think the plan now is for her to just bounce around and chip in for rent if she {i}does{/i} get the job. "

    scene sanatochika10
    with dissolve

    c "But, of course none of this would be possible without you, Touka! You’re seriously saving my ass. And this place will be way better for Chinami in the long run."
    ch "Chinami liked her old house, but she likes this one a lot better! There’s hot water here! And Chinami loves hot water!"
    to "There’s no need to thank me, Chika. This is simply a business venture and not an act of charity by any means. And I {i}will{/i} evict you if you do not make your payments on time."
    c "Oh, you don’t have to worry about that. The maid cafe’s got me covered. And I’ve got auto-pay set up on the same day my new phone bill goes through, so I’ll always know when it’s coming!"
    s "Oh, right. I’m saving money now."

    scene sanatochika11
    with dissolve

    c "You sure are! And with how cheap this place is, maybe {i}you{/i} can get a room here as well."
    to "This complex is for women only, I’m afraid. I apologize for the inconvenience, Sensei."
    c "Don’t worry. You’re still allowed to sleep over whenever you want. My name’s on the lease, so I get to do what I want."
    to "That much is true, yes. There are no rules in place prohibiting “sleepovers” of any sort. Just please keep the noise down as I’ve heard the two of you play {i}games{/i} that tend to be rather...{i}loud{/i} at times."

    scene sanatochika12
    with dissolve

    c "Oh, you must be talking Yahtzee. I get really into...dice-based board games."
    to "Yes...{i}Yahtzee.{/i}"

    scene sanatochika13
    with dissolve

    to "Anyway, I must be leaving. I have other matters to attend to. Namely {i}school,{/i} as I’m sure Miss Imai is currently wondering why my perfect attendance has suddenly become {i}imperfect{/i} attendance."
    s "Touka...wait."

    scene sanatochika14
    with dissolve

    to "Wait?..."
    to "Do you need something, Sensei?"
    c "Yeah. What do you need from Touka? She’s a busy...business woman now. She’s got stuff to do and things to learn. "
    s "Can we...talk?"
    to "About what?"
    c "..."
    s "I..."
    s "Uhh..."

    scene sanatochika15
    with dissolve

    to "Ah. You must be referring to those business tips you inquired about before your two-month absence. I apologize, it’s just been so long that I must have forgotten."
    c "Business tips? "

    scene sanatochika16
    with dissolve

    to "Is that correct, Sensei? Am I mistaken?"
    c "Have you been thinking about quitting teaching for that long? What sort of business are you trying to get into?"
    s "I...don’t know yet. Which is why I was looking for Touka’s help as I know she has experience with...business."
    to "Then, I will give you my {i}business{/i} phone number. Which is not to be confused with my personal phone number. I am very wealthy, so the fact that I have two phone numbers is believable."
    c "She’s got a point. That is believable."
    to "Your phone please, Sensei. I’ll enter my contact information that you may use to reach me during {i}business{/i} hours only."

    scene sanatochika17
    with dissolve

    "Touka snatches my phone out of my hand and...all I can do is silently thank her inside of my head as she expertly covers for me in every which way possible."

    $ toukanumber = True
    play sound "winner.mp3"

    "{i}You have obtained Touka Tsukioka’s “business” phone number!{/i}"

    c "Hey, isn’t that your personal number?"

    play sound "computerboo.mp3"

    "{i}Or not!{/i}"

    to "No. But they look very similar, so I can not fault you for thinking that."
    to "I {i}can{/i} fault you for glaring at my belongings, though. That is very unbecoming of you, Chika."
    c "Well, if you’re just gonna let them hang out like that-"

    scene sanatochika18
    with dissolve

    to "Really?"
    c "Oh. You meant your phone."
    to "..."
    c "What? They’re nice. We all know it."
    to "Yes, well..."
    to "Goodbye."

    scene sanatochika19
    with dissolve

    c "You can look at mine if it makes you feel better!"
    to "I believe I will be fine without doing that, but thank you for the offer. Now again, goodbye."

    play sound "dooropen.mp3"

    to "And Sensei, please do call about those business tips whenever you can. There are a few things I would like to ask you as well."
    s "Yeah...see you."

    scene sanatochika20
    with dissolve

    "Touka leaves and...honestly, I was not ready to see her today. But I guess I should have expected her to be here considering this is {i}her{/i} building and all."
    "But...I need to focus on Chika for now. I’ve already messed things up with her after allowing Ami to walk all over her yesterday, so any chance I get to patch things up is-"

    c "Okay. So. I don’t have much time before I have to leave for work, but I wanted you to see me in my outfit before I go since I heard from Uta how much you love maids."

    "I guess patching things up can wait. "

    s "I haven’t even commented on your hair yet, have I?"

    scene sanatochika21
    with dissolve

    c "No, actually. I was so busy wanting to kill Ami yesterday that I forgot to ask you how you felt about it."
    s "You look beautiful, Chika."

    scene sanatochika22
    with dissolve

    c "Y...Yeah? You...really think so? It’s not weird after...seeing me blonde for so long?"
    c "Also, don’t look at the rest of me because I’m pretty sure I gained weight while you were gone. And I finally have enough money for a gym membership, but I haven’t had time to go yet and-"
    s "Sorry to interrupt, but aren’t you short on time? I just really don’t want you to regret not showing me your costume, which is a thing I know you really want to do."
    c "R...Right! Be right back!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene sanatochika23
    with dissolve2

    ch "..."
    s "What? Why are you looking at me like that?"
    ch "Chinami knows flirting when she hears it. Exposure to cable television has made her more aware of love than ever before."
    s "Chinami, go back to watching TV. Your sister is-"

    scene sanatochika24
    with dissolve

    ch "My sister really missed you."
    ch "Chinami will give you all the alone time you need together."

    scene sanatochika25
    with dissolve

    ch "And if you just happen to give Chinami another sister, Chinami won’t mind."
    s "Yeah, I’m sure..."
    c "Okaaaaay! Here I coooooome!"

    scene sanatochika26
    with dissolve

    c "Ta-da! Kumon-mi’s hottest new maid, at your service!"

    scene sanatochika27
    with dissolve

    c "Oh! And speaking of which, did you know Niki was a maid once too?! I have no idea how I never heard about that! It must have been, like, a super underground early promo thing! But wow!"
    c "Learning that was part of my orientation and just knowing I stood in the same locker room as her is...aaah! I’m so friggin’ pumped going to work every day now!"

    "Yeah, you’ve done much more than just “stand in the same locker room.”"

    c "Like...what if she wore this same dress? Our bodies aren’t {i}that{/i} different, right? She was probably a little smaller back when she did the promo, right? Right???"
    s "Can I appreciate the way {i}you{/i} look instead of thinking about {i}her{/i} right now?"
    c "Yes! Please do!"
    c "And please say a bunch of sweet things about me since I could really use the dopamine boost after the emotional rollercoaster that has been my last two months!"
    s "You’re the second prettiest maid I’ve ever laid my eyes on."
    c "That sucked! Hard! But I also knew it was coming since Uta told me all about your obsession with her!"
    s "My obsession is with Uta-chan, not Uta. "

    "Though, I’d be lying if I said the two of them haven’t already merged together inside my head."
    "Chika doesn’t need to know that, though. "

    c "Whatever! Say more nice things!"
    s "You’re adorable."
    c "More!"
    s "You’re...cute?"
    c "More, more, more!"
    s "I love you."

    scene sanatochika28
    with dissolve

    c "Kyah!"
    s "Kyah?"
    c "It’s just been so long since I’ve heard you say you love me that my heart skipped a beat! I feel like I’m ready to take on the world now!"
    s "Then get out there and show the unnamed maid cafe what you’re {i}made{/i} of."
    c "..."
    s "I’m sorry. I’ve never been good at making jokes to begin with, but making them when I feel like I could be crushed by the weight of the world at any given moment is significantly harder."
    c "I’m just going to pretend you stopped saying things after “I love you” and go to work now!"
    s "Sounds good, Chika."

    scene black
    with dissolve2

    c "Chinami! Be good for Sensei, okay?"
    c "Sensei, I love you too. Mwah!"

    play sound "doorslam.mp3"

    c "{i}LET’S FUCKING GOOOOO!{/i}"

    $ renpy.end_replay()
    $ chikaspring2 = True
    $ chika_love += 1

    "{i}Chika’s affection has increased to [chika_love]!{/i}"

    jump chinamispring1

label chikaspring3:
    scene chikarinmusic1
    with dissolve2
    play music "ame.mp3"

    "Another unexciting day winds down as two young creatures begin to contemplate finding their way back to their burrows."
    "And while they’re silently thankful to have made it to sundown without their necks being torn open, it’s been unmistakably dull on the plains as of late. And they’re not sure how to feel."
    "Without the looming threat of predation, they’ve spent their time chewing on grass and picking bugs out of the dirt."
    "They have so much space to run, but nothing to run {i}from.{/i} So why does that make them feel incomplete?"
    "One creature stares outside and ponders whether or not the act of being chased is what excited her at all to begin with. And if these days are only boring now since her legs have begun to atrophy from lack of use."
    "The other creature’s thoughts are more complicated and conflicted, but we’ll get to them in a moment."

    c "Hah..."

    "For now, we’ll zero in on Chika Chosokabe — a gyaru turned bad-girl who would not hesitate to take up the role of {i}predator{/i} if the plains stay dull for far too long."
    "Which isn’t to say she has anything against the other prey. It’s just that these seasons of unintended hibernation can cause things to get a little out of control every now and again. "
    "As the eldest of the pack, the responsibility to reestablish control would likely fall on her. And she’s loved and feared enough that the others would be sure to follow."

    c "Rin, question."
    c "How often do you think about jumping off a bridge?"

    "But the leader of a pack must not be chosen based on age and status alone. Because, in this case, it’s the eldest who’s grown the most weary. "
    "You see, this creature spends the bulk of its time foraging for berries, just to split them with lesser creatures upon returning to the burrow. "
    "She grows weaker and more tired by the day now that she does not need to remain alert at all times."
    "When her eyes close at night, she feels less inclined to keep them open to see what happens next."
    "And when the wind rushes into the hole in which she sleeps, she silently wishes for it to carry her away."

    scene chikarinmusic2
    with dissolve

    r "Uhh..."

    "But it won’t. "
    "If she’s ever going to go {i}anywhere,{/i} she needs to be the one to take the first step."
    "No wind, nor nature in any form will rescue her from the complete absence of motivation. "
    "And as she emerges from her hole and gazes at her reflection in the lake, it becomes clear that she must either drink from these waters for the rest of her life-"

    r "Probably...not as much as you’d think?"

    "Or drown herself in them."

    c "Fuck."

    "For this field is actually a farm."

    r "Is that...something you’re thinking about doing?"

    scene chikarinmusic3
    with dissolve

    "And the only ones who can move in and out are those big enough to hop the fence."

    c "Maybe."
    c "But, like...not a big bridge. Maybe a small one. With some water below it that, like, wouldn’t {i}definitely{/i} kill me if I fell in. But {i}could.{/i} You know?"
    r "..."
    c "..."
    r "No."

    scene chikarinmusic4
    with dissolve

    c "Sorry. I’m just being dramatic. You don’t need to put me on suicide watch or anything. "
    r "That’s good, because I have no idea how I would even do that. And I’m pretty sure people wouldn’t actually take me seriously when I say it’s “for a friend.”"

    scene chikarinmusic5
    with dissolve

    c "Would you mind if I ranted about personal stuff for a few minutes? Because Yumi sucks at listening and it’s not like I can get my sister involved in any of my problems."
    r "You can rant as much as you want. I just have no idea how useful I’m going to be since I kind of suck at dealing with...almost everything, now that I think about it."
    c "It’s about boys. Is that okay?"
    r "Chika...I’m not allergic to boys. I’m bisexual. Why would that not be okay?"
    c "Because romance can be an annoying, touchy subject and you’re still getting over a breakup. "
    r "With...a {i}girl.{/i}"
    r "Otoha is a girl, Chika. There was no penis there. I checked."

    scene chikarinmusic6
    with dissolve

    c "I meant “boys” as a concept! Not literal boys, Rin! Just pretend I said “romance” instead!"
    r "Fine, yeah. But again, dealing with that kind of stuff isn’t exactly my forte. Especially now that 100%% of my relationships have ended in complete and utter failure."

    scene chikarinmusic7
    with dissolve

    c "No they haven’t. Otoha was never good enough for you anyway. And, if I were you, I’d see this as a good opportunity to get back out there and try again with someone who deserves your time."
    r "..."
    c "But anyway...if you haven’t already guessed, this is about Sensei and me."

    scene chikarinmusic8
    with dissolve

    r "Whaaaaaaaaaaaat?"
    c "You’re a bad actor."

    scene chikarinmusic9
    with dissolve

    r "I’m a bad everything but that’s never stopped me before."
    c "I like that. Your...perseverance is one of my favorite qualities about you."
    r "Liar. If that were true, you’d have been immediately impressed by my confession and we would have made out on the beach and wouldn’t even be talking about Sensei right now."
    c "Fair. But still, it’s cool that you can just...keep going the way you have been."

    scene chikarinmusic10
    with dissolve

    c "Sensei and I aren’t even broken up and I feel like my whole life is being torn apart. I can’t even imagine how I’d be if we ended things."
    r "Are you...actually thinking about ending things?"

    scene chikarinmusic11
    with dissolve

    c "{i}I’m{/i} not! But between the last couple months and just...the first few interactions he’s had since rejoining the world, it feels like he’s pushing me away."
    c "Like, he came over to babysit the other day and was totally gone by the time I came back. He didn’t even tell me he was leaving. I could have, like...called Yumi or something if I knew."
    r "Well...I mean..."
    r "Uhh..."
    c "“Uhh” what? Give it to me straight. I can’t afford to beat around the bush at a time like this. My relationship is potentially on the line here."
    r "I just mean...don’t you maybe think asking him to babysit in his current condition is kind of...not a great idea?"

    scene chikarinmusic12
    with fade

    c "What do you mean?"
    r "I mean...you remember what he said, right? About losing something?"
    r "Sensei’s kind of like...miserable right now. And he’s gone through patches like that in the past, sure. But this is way worse than {i}I’ve{/i} ever seen. And I doubt {i}I’d{/i} want to babysit in that condition."

    scene chikarinmusic13
    with dissolve

    c "Aaaaaaaaah fuck. Yup. I’m an idiot. I was so excited to have him back that I didn’t even think of that. It’s no wonder he just up and left. I would’ve done the same thing."
    r "Oh. Oh, okay. That was easy then. Is the rant over?"

    scene chikarinmusic14
    with dissolve

    c "No. I don’t get very many opportunities to do this, so I need to make sure I get everything off my chest. But you’ll be allowed to rant back to me once I’m done. It’s only fair."
    r "Can I...postpone my half of the rant session? I have work today."
    c "I’ll allow it. Now, please brace yourself as I am about to talk about sex."

    play sound "thump.mp3"
    scene chikarinmusic15 with hpunch

    r "Ah!"
    c "You dropped your guitar."

    scene chikarinmusic16
    with dissolve

    r "No I didn’t."
    c "I told you to brace yourself."
    r "Yeah, but there wasn’t a big enough gap between that and the sex word. You have to let me brace myself before you tell me to brace myself. Don’t you understand how my brain works by now?"
    c "I’ll do a better job in the future, I promise."
    r "Then...what do you want to say about...the designated topic of sexual intercourse? Which is a topic you have decided to discuss. Not me."
    c "Should I or should I not press him for sex? "
    r "I’m...pretty sure it’s the boy who presses the girl for the mating press, right?"

    scene chikarinmusic17
    with dissolve

    c "Rin, no!"
    r "No? Hold on. I have to Google this."
    c "No, I meant like...press him in general! "
    r "Huh? Are you seriously that horny that you can’t wait until he doesn’t feel like he’s dying anymore to have him do you?"

    scene chikarinmusic18
    with dissolve

    c "That’s not...the {i}entire{/i} reason. It’s more like..."
    c "I know Sensei uses sex to make himself feel better rather than talking things out. But when I tried the other day, he didn’t want to."
    c "And I’m not sure if I should try {i}again{/i} because I’m not sure if it was, like...just a bad {i}time{/i} or if he doesn’t want to have sex {i}at all{/i} for a little while."
    c "And it’s fine either way, I just don’t know how to make him feel better and..."
    c "And yes, I am also very horny. "
    r "Well, as someone who has never had sex with Sensei, I do not think I can properly instruct you when it is and is not a good time to try and do that with, to, or on him."

    scene chikarinmusic19
    with dissolve

    c "Figures."

    if rincthree:
        c "I guess I should wait for a better time to ask about the threesome then."

        scene chikarinmusic20
        with fade

        r "A better time to ask about the {i}what?{/i}"
        c "Threesome. You, me, and Sensei."
        r "Like...going to the movies?"
        c "Sure."
        r "Because for a second-"
        c "And then having sex with each other."

        play sound "thump.mp3"
        scene chikarinmusic21 with hpunch

        r "Ngh!"
        c "You dropped your guitar again."

        scene chikarinmusic22
        with dissolve

        r "You didn’t even tell me to brace myself that time! And what’s this about a three-"
        c "{i}Shh. Keep your voice down.{/i}"

        scene chikarinmusic23
        with dissolve

        r "What is this about a threesome? Why me? Why now?"
        c "The short version is that I wanted to do something special for Sensei and that I told him I’d be open to a threesome with him and a girl of his choosing."
        r "So who backed down and why am {i}I{/i} the replacement for them?"
        c "Rin. He chose you, dummy."

        scene chikarinmusic24
        with dissolve

        r "{i}Me?!{/i} Why?"
        c "A bunch of reasons, probably. You two are close...you swing both ways...{i}and{/i} you had a crush on me for a million years, so he probably wants to see the chemistry."
        c "But I guess there’s no point in trying to arrange this now if I have no idea when he’ll even {i}want{/i} to do it again."
        r "And you...you’re okay with this? With {i}me?{/i}"
        c "Hm? Of course. Why wouldn’t I be? I’d have probably chosen you as well if he let me pick."

        scene chikarinmusic25
        with dissolve

        r "Oh my God. I should have known this was a dream the moment you said the word “sex.”"

        scene chikarinmusic26
        with fade

        c "You realize you’re going to make me blush too if you keep blushing like that, right?"
        r "You’re already blushing! And this is {i}your{/i} fault! I just wanted to play guitar!"
        c "Okay but, in my defense, it’s been over two months since I’ve done {i}anything{/i} and I can’t even walk down the produce aisle without getting hot at this point."
        r "What kind of fetish is that?!"
        c "Are you in or out? Whenever things start moving again, I mean. Just give me a yes or no answer. We don’t need to spend any more time on it than that."
        r "Chika..."
        r "I..."
        r "I need to...think about this..."
        r "There is...{i}literally{/i} no denying that this is a dream come true in {i}many{/i} ways, but...I..."
        c "It’s fine. Just...we can drop it for now and get back to it later. You’re still freshly broken-up with, so I can see why you’d want to maybe-"
        r "{i}Mutually{/i} freshly-broken up with."
        c "Yeah. That."
        c "Anyway, we can talk about it later."

    scene chikarinmusic27
    with dissolve

    c "For now, I guess I just need to...figure out the next steps when it comes to handling this whole relationship thing."
    c "We’ve got into little fights and stuff before. And all of them were because of things {i}I{/i} was doing wrong, so..."
    c "I’m sure this is all going to blow over and that I’ll...have more mistakes to learn from when it does."

    scene chikarinmusic28
    with fade

    r "Are you sure you should be looking at them as mistakes at all, though? Because you’re like...the one person I can’t imagine tripping up when it comes to relationship stuff."
    r "You’re nothing like me when it comes to that. Your head’s so firmly on your shoulders at all times that I often think you’re just a really hot, fleshy mannequin."
    c "I think making little mistakes is pretty unavoidable when it comes to relationships. I’m just not really sure how to handle or...even {i}accept{/i} that I might not be able to help this time."
    c "And that sucks. It {i}really{/i} sucks. Like...you know things are bad when {i}Ami{/i} is able to help and I’m not."

    scene chikarinmusic29
    with dissolve

    c "Hey. Unrelated note — just out of curiosity, if I ever needed help burying a body, could I rely on you?"
    r "I’m...not going to bat for Ami when it comes to all that weird shit she said in class the other day. But I don’t think murdering her is the answer."

    scene chikarinmusic30
    with dissolve

    c "{i}Murder?{/i} Ami? That thought never even occurred to me."
    r "She needs help, Chika. Like...{i}serious{/i} help."
    c "But she’s so stable and normal."
    r "I get that she rubbed you the wrong way. She rubbed {i}all{/i} of us the wrong way. But I think some of us might be taking things a little too hard on her right now."
    r "Especially since she’s not even here to defend herself."
    c "To be fair, I’m not really sure there’s anything she could say that {i}would{/i} help her defend herself. Not from me, at least. Especially not when she’s going to try to blackmail me with my own nudes."
    r "Yeah...I had a feeling that’s what she showed you."
    c "Whatever. At least now she knows I’m fucking her uncle and I don’t have to dance around it anymore. If she wants to use that against me, whatever. I know she’s not going to expose Sensei, though."
    c "I thought more about it and she’d gain literally nothing from him being arrested, so at least I’ve got peace of mind in knowing {i}he’ll{/i} be okay."
    r "You’re thinking too much about him and not enough about yourself..."

    scene chikarinmusic31
    with dissolve

    c "..."
    r "It’s like..."
    r "With Otoha and me...it’s pretty clear in hindsight that I was asking for way more than what she was willing to give. And I love Sensei...but I don’t want you to fall into that same trap with him."

    scene chikarinmusic32
    with dissolve

    c "Hm."
    r "..."
    c "I guess that’s how it would look to you."
    c "We’ve kept our situation pretty confidential because of the impact it could have on him, so it’s probably tough to see how much he really loves me from the outside."
    c "He’s nothing like Otoha, though. She was straight up evil and I still can’t believe the way she treated you."
    r "You’re making her out to be way worse than she actually was, Chika. She just..."
    r "She didn’t love me."
    c "But she said she did. And that’s unforgivable."
    r "..."

    scene chikarinmusic33
    with dissolve

    c "Okay! Rant over. I feel way better now."
    c "Did it accomplish anything? No. Am I still just as lost and screwed as I was ten minutes ago? Yes!"

    scene chikarinmusic34
    with dissolve

    c "But at least I got to talk to somebody who will actually listen."
    r "Yumi listens too. She’s just scary."
    c "You only think she’s scary because you don’t know her."

    scene chikarinmusic35
    with dissolve

    r "And because I watched her beat Nodoka halfway to death. Even if that’s something we’ve all kind of wanted to do at times."
    c "Fair enough. What’s the plan now, though? Still going to work? Or would you rather come over and see my cool, new apartment?"

    scene chikarinmusic36
    with dissolve

    r "Definitely the apartment. But I’m trying to get promoted, so I don’t think skipping work is a thing I should be doing right now."
    c "Offer’s still there whenever you’re free. And if you bring a peanut-free snack, you can immediately gain the undying affection of my little sister who will one day be the prime minister of Japan."
    c "It’ll be good to have her on your side for when the next space war starts."

    scene black
    with dissolve2

    r "I’ll keep that in mind for my next day off. But for now, I must get dressed!"
    c "Need any help?"
    r "Need? No. Want? Yes. Will accept? No again. Bye!"

    play sound "slidedoor.mp3"

    c "Hahah! Later, Rin."
    c "Thanks for listening to me complain! I’ll be sure to keep you updated on my sex life and the status of my relationship with someone I shall not name within these walls!"
    r "You don’t have to do that, but thank you!"

    "And so our segment focusing on Chika Chosokabe comes to an end-"

    $ renpy.end_replay()
    $ chikaspring3 = True

    jump rinspring2

label chikaspring4:
    scene noonsky
    with dissolve2
    play music "sensei.mp3"

    "I laugh myself all the way over to the new Chosokabe apartment, but not because this is funny."
    "Like sure, it’s a bit degrading and a bit comedic being an adult male being called a bitch by a teenage girl, but it’s not like Chika’s {i}wrong{/i} about that. "
    "I {i}have{/i} been running away from her and I {i}have{/i} been off moping and crying and whining about all of my other problems when she’s been readily available to help me with them."
    "But no, that’s not why I’m laughing. I’m laughing about the irony."
    "I’m laughing about how she could have found me with twenty other girls back there and that probability dictates I’d likely be fucking one of them when she did."
    "But instead, she found me with her best friend — a girl I’ve done {i}practically{/i} nothing with — and she must now face the music after going out of her way to turn the volume up."
    "So yeah, I think that’s kind of funny. "
    "I think it’s cute that something so innocent in nature could break her."
    "But I wonder-"
    "How much more damage can I inflict upon her today?"

    scene black
    with dissolve2
    play sound "doorbell.mp3"

    "Which isn’t to say I {i}want{/i} to. But I {i}have{/i} to."

    ch "{i}Coming!{/i}"

    play sound "dooropen.mp3"

    "Some animals, like the opossum, are hesitant to fight. They either flee or they play dead. Or they flee and {i}then{/i} play dead once you’ve got them cornered."

    scene chikaargue1
    with dissolve2

    "But then there are those like dogs and cats — specifically the ones who are afraid of this world — but will fight and claw and bite for a chance to stay here."
    "And they might not be happy to do it. It might be a huge waste of energy for them. But if that’s what it takes to survive, that’s what they’ll do."
    "So I walk myself into this corner knowing what awaits me. I’ll make myself look tall or bare my teeth or spread my wings because I {i}want{/i} to submit, just not {i}all{/i} the way."
    "And if she swoops in to try and end things, I won’t hesitate to strike back in defense."
    "Animals work on instinct, you know. And here in Kumon-mi, it’s always mating season. "
    "I can’t afford to let my species go extinct."
    "But more than that-"
    "The thought of her mating with anyone else just makes me mad."

    ch "H...Hi, Papa."
    c "..."
    s "Hey, Chinami. Hey, Chika."
    c "..."
    ch "B...Big sis Chika is...a little grumpy today from...getting into a fight with big sis Yumi, so..."
    s "I know. But it’s my fault that fight happened in the first place, so I’m here to try and clear things up."
    c "It takes two to tango, asshole. Yumi’s not {i}absolved{/i} just because you came over here to take the blame for her."

    scene chikaargue2
    with dissolve

    ch "Mm..."
    s "Even if she didn’t do anything wrong?"
    c "She did plenty wrong, even {i}if{/i} your story checks out."
    s "And if it doesn’t, what then?"
    c "I don’t know, Sensei. You tell me. Gonna trade me in for a brand new toy? You a little bored after using me so many times?"
    s "Should we maybe go outside for-"

    play sound "static.mp3"
    scene chikaargue3 with flash
    stop sound

    ch "Mm!"
    s "...this."
    c "Chinami...let go of him."

    scene chikaargue4
    with dissolve

    ch "Ch...Chinami has a better idea! Why don’t you two talk later and we can all play a game now? Chinami is very bored and thinks her family should be having fun! Right, Papa?"
    s "..."
    ch "P...Papa?"
    c "Chinami...let go. Your sister and your {i}father{/i} need to have a very important talk right now."

    scene chikaargue5
    with dissolve

    ch "But...Chinami is scared..."
    ch "She doesn’t want to lose a second daddy..."
    s "..."
    c "The first one never deserved us anyway."
    ch "But this one does, doesn’t he?"
    c "Well...I guess we’ll have to see. "
    c "But we can’t {i}do{/i} that if you don’t let go of him. Understand?"

    scene chikaargue6
    with dissolve

    ch "Papa..."
    s "..."
    ch "You won’t leave us too...will you?..."
    s "I think that’s up to your sister, Chinami."
    ch "Big sis Chika doesn’t want you to leave. I heard her say that. Does this mean the talk is over? You’ll stay together and we can be a family for a little while longer?"
    c "Chinami, let go right now or you’re grounded."

    scene black
    with dissolve2

    s "..."
    ch "Chinami is sorry..."
    ch "Chinami will leave you alone now..."

    play sound "static.mp3"
    scene chikaargue7 with flash
    stop sound

    "We wind up on the balcony once Chinami releases her hold on me — which is great, because I was only a second or two away from caving and giving them everything they’d ever want."
    "At least now I can get back to what I was thinking earlier with the animals and how I...how..."
    "What was it again?..."

    play sound "static.mp3"
    scene chikaargue7 with flash
    stop sound

    "What did I...how I was..."
    "What was the plan again?..."

    c "..."
    s "..."
    c "If you’re waiting for me to be all sweet and forgiving, we’re going to be out here for a while. That ship sailed the second I saw you fucking Yumi."
    s "You didn’t see me {i}fucking{/i} her, Chika."
    c "Yeah, well I might as well have with how fucking close the two of you were back there."
    s "How did you see us anyway? "
    c "With my fucking {i}eyes,{/i} idiot. Don’t tell me you were so lost in hers you forgot other people {i}had{/i} them."
    s "No, I meant...I didn’t even know where you were. I kind of figured you just went home after running away or something."
    c "I’m sure that would have been convenient for you, huh? But I guess it’s not like it mattered in the first place since you just took her back to your room anyway."
    s "..."

    scene chikaargue8
    with dissolve

    c "I was looking for you."
    c "I got tired of passively waiting for you to come find me since it felt like you were never going to. "
    c "So I forced myself to confront the fear that you might be giving those feelings to someone else and...{i}boy,{/i} do I regret that."
    s "Nothing happened, Chika."

    scene chikaargue9
    with dissolve

    c "And why should I believe you, huh? You’ve been getting nudes from other girls and never bothered telling me about them. You {i}kissed{/i} Yumi and never told me about {i}that.{/i}"
    c "Hell, I don’t even know who this fucking person you {i}lost{/i} that you’ve been crying about for months is because you’ve been keeping me in the dark about literally everything."
    s "I’m doing that because I l-"

    play sound "static.mp3"
    scene chikaargue10 with flash
    stop sound

    c "You can’t just tell me you love me to get out of shit, okay?! Those aren’t magic words that make all the pain disappear!"
    c "When you hurt, {i}I{/i} hurt! I’ve been trying to tell you that this whole time! But you were too busy screwing my best friend to even give a shit! What kind of man are you?! "
    s "The worst kind imaginable, pretty much."

    scene chikaargue11
    with dissolve

    c "But {i}why?{/i} Are you seriously just bored of me? I stopped being clingy like you asked."
    s "I know."
    c "I gave you so much space that it basically started killing me. I haven’t pressed you for sex. I even went out and got an apartment and changed my phone plan so you wouldn’t have to pay for me anymore."
    c "And did I mention how I haven’t pressed you for sex? Because I’ve been going crazy over here and think that deserves a little more fanfare. But the fact remains, I did everything you wanted!"
    s "You did. You’re right."
    c "So why?! How could you do this to me?! To Chinami?! She practically thinks you’re her real father!"
    s "Can I talk now? Or do you need to get more of this out of your system? Because I’m not sure how much you’ve saved up ever since the whole sadness coma thing."

    scene chikaargue12
    with dissolve

    c "I had a fucking million things I wanted to say...but I can barely remember {i}any{/i} of them now."
    c "I’m sad...and angry...and {i}scared...{/i}and it’s all your fault. {i}This{/i} is what happens when you leave me alone."
    c "I thought things would change once you started leaving the house again. I thought you’d go back to normal. But you’ve been more distant than ever and {i}now{/i} I understand why."
    s "Chika...you {i}don’t,{/i} though. "

    scene chikaargue13
    with dissolve

    s "It’s true that I was with Yumi and it’s true that it looked {i}really{/i} bad, but nothing happened. And nothing happened when we went back to my room either because {i}we’re not like that.{/i}"
    s "There were a bunch of other girls in my room that night too. That was the whole reason I came to the beach in the first place."
    c "You fucked an entire room full of girls while I was bawling my eyes out in a public bathroom?"
    s "Wha- no. That’s not what I meant. We were having a...meeting."
    c "You...were having a meeting?"
    s "...Yeah."
    c "..."
    c "How fucking {i}gullible{/i} do you think I am, Sensei?"
    s "I know how it sounds. But you could ask any of the girls who were there and they’ll tell you the same thing."
    s "Or...wait. Maybe not all of them. I’m not sure who remembers what, but...Yumi. Yumi remembers. Noriko and Sana probably don’t. Ayane and Makoto definitely remember too."
    c "You didn’t even think up a believable story on the way over, huh? So {i}that’s{/i} how little I mean to you. "
    s "Chika-"
    c "Just break up with me now and get it over with. I have to figure out how I’m going to break the news to Chinami."
    s "..."
    c "That’s what you want, isn’t it?"

    scene chikaargue14
    with dissolve

    c "Even if I’m mad at Yumi...I can’t say she wouldn’t be good for you. In fact, that’s probably why this is so hard for me in the first place."
    c "All the signs were there. You’d never choose a girl like me if someone like her was an option. Someone who won’t ever press you about anything and just...lets you be {i}you.{/i}"
    c "I’m sorry that couldn’t be me. I tried. I really did. But if you’re {i}still{/i} not comfortable with me after all this time, I’m not sure what else I can do."
    s "Chika, for the last time...{i}nothing happened with Yumi.{/i}"

    scene chikaargue15
    with dissolve

    c "But you {i}want{/i} something to happen with her...don’t you?"
    s "..."
    c "Just the way you two were looking at each other back there was enough to do this to me. I guess I just...wanted to be the only girl you ever stared at like that."
    c "So even if “nothing” happened...even if that kiss was a stupid thing you guys did before we ever started hanging out...it {i}feels{/i} like something happened. And I hate it. So fucking much."
    c "Like...yeah. It’s probably dumb, but I don’t think you really comprehend just how in love with you I am, Sensei. In {i}my{/i} mind, we’re basically husband and wife already."
    c "If you want to be creeped out by that, feel free. Go...stare into the eyes of some other girl who’s probably wishing the same thing and then...forget {i}us{/i} entirely."
    c "But next time...maybe don’t tell someone you love them unless you mean it...okay?"
    s "Chika...I..."
    s "{i}Hah...{/i}"
    s "I know you said these words alone can’t make the pain go away, but I {i}do{/i} love you. It’s just..."
    s "The thing is...love is kind of confusing."
    c "You can fucking say that again."
    s "I mean, like...I don’t think I see it the way other people do. It’s hard to describe. And sometimes I don’t think I see it at all."
    s "But when I look at you, I see someone I want to spend the rest of my life with. "
    s "And I want to kiss you and fuck you and hold your hand and do all of those things, but...I’m not sure if I’ll ever be able to {i}talk{/i} to you. "
    c "You don’t have to {i}talk,{/i} Sensei. You just have to be there. I already resigned myself to a life of never knowing what the fuck is going on in your head."
    s "Right. But can you resign yourself to a life where those feelings aren’t unique to {i}you?{/i} Because that’s the next part I was getting to."

    scene chikaargue16
    with dissolve2

    c "..."
    c "So-"
    s "I {i}would{/i} get together with Yumi if she wanted to. Even though I know it would hurt you. "
    s "The...unfortunate truth is that there are {i}so many{/i} of you that I want to spend the rest of my life with. Physically {i}and{/i} emotionally. Albeit with the emotional part kind of suppressed, but still."
    c "So...you want a life where you can kiss me...and fuck me...and hold my hand...but then turn around and do that same thing with everyone else?"
    s "That’s right. "
    c "And you don’t think that’s the most selfish, disgusting thing you could possibly say to a girl who would literally die for you?"
    s "No, {i}I do.{/i} I {i}get{/i} that. Which is why I never brought it up. "
    s "Do you think I {i}want{/i} to feel like this? Do you have any idea how much easier all of this would be if I could just {i}choose{/i} someone? Because I’d take that over whatever {i}I{/i} am any day of the week."
    s "I live in a perpetual state of having to hide who I am from {i}everyone{/i} because who I am {i}sucks.{/i} And you’ve been more sheltered from that than anyone because of how deeply I care about you."
    c "So..."
    c "I’m winning?"
    s "..."
    c "..."
    s "{i}What?{/i}"

    scene chikaargue17
    with dissolve

    c "If I’m the most sheltered...it means you...think about me the most...and...then...everyone else, you’re...more okay with hurting...so I’m...being prioritized and..."
    c "That means if...you had to make a choice...it’d be me...it would definitely be me...because you’re okay with other girls...being in pain and...I’m the special one..."
    c "I’m the special one...and if I’m special...it means that {i}I{/i} am loved...and everyone else, you just...you {i}think{/i} you love them...but it’s really {i}me...{/i}"
    c "{i}I’m{/i} the one you love..."
    s "..."
    c "I’m the one you love..."
    s "Chika?..."

    scene chikaargue18
    with dissolve
    stop music fadeout 7.0

    c "Huh?"
    s "Are you...okay?"
    c "Yeah. Why?"
    s "You just...it seems like you’re having a...hard time processing what I’m trying to say to you."
    c "Oh, no. I think I get it now."
    s "I’m...not sure you do."
    c "No, yeah. You want to fuck other girls, right?"
    s "..."
    c "But you also want to fuck me. Just more."
    s "..."
    c "Because you love me."
    s "And others."
    c "Right. But you {i}love{/i} me."
    s "I “love” multiple people."
    c "But I’m winning."
    s "It’s not a competition, Chika..."
    c "Yes it is. And I’m winning it."
    s "You’re not-"
    c "Do you love Yumi?"
    s "Well...{i}no.{/i} "
    s "But-"

    scene chikaargue19
    with dissolve

    c "Great! "
    s "No, {i}not{/i} great. I think we need to keep talking."
    c "No, no. It’s fine. I get it now!"
    c "But I’m gonna do the same thing and go fuck a bunch of other guys too."
    s "..."

    play sound "static.mp3"
    scene chikaargue20 with flash
    stop sound
    play music "undersea.mp3"

    c "Just kidding! Hahahah! You’re the only one who can get a piece of this because I’m {i}your{/i} special girl! And like, where would I even find other guys anyway? Hahahaha!"
    c "I bet their dicks are all small and stuff. Not like yours, [chikamaster]. You’ve got the best dick of all. And it fits inside me so perfectly! We’re practically made for each other, right?! Hahahaha!"
    s "Chika-"
    c "Hey, here’s an idea! Why don’t you fuck me over the railing right now? Then maybe we can fall and die and be on the news and everyone would call us the next Romeo and Juliet! Just hotter. God, I love you."
    s "Uh..."
    c "So, just to clarify, we’re not breaking up. Right? Like, we’re still together. And that whole thing with you and Yumi was just a misunderstanding. But you {i}would{/i} fuck her. Just, {i}I’m{/i} the special one."
    c "And you love me and I love you and we all love each other but you also “love” other girls because they’d all feel bad if you didn’t. I’m so glad we had this talk! "

    "Something went wrong."
    "I must have given her rabies."

    s "Chika-"
    c "{b}{size=+25}What?????{/b}{/size}"
    s "I need you to calm down...and take a deep breath."
    c "Okay! Anything for you and your amazing, awesome dick that isn’t {i}actually{/i} my property but is, like, {i}totally{/i} my property! Hahahaha!"
    s "Chika...{i}breathe.{/i}"

    scene chikaargue21
    with dissolve2

    c "{i}Haaaaaaaaaah....{/i}"

    scene chikaargue22
    with dissolve2

    c "{i}Hooooooooooooh...{/i}"

    scene chikaargue23
    with dissolve

    c "..............................."
    s "Are you...feeling any better?"

    stop music
    play sound "static.mp3"
    scene chikaargue24 with flash
    stop sound
    play music "ame.mp3"

    c "Yes."
    s "..."
    c "..."
    s "Are you {i}really{/i} sure you’re feeling better?"
    c "I am really sure I’m feeling better."
    s "Okay. Because I just dropped a pretty big revelation on you and I don’t want this to be one of those things where you’re just {i}pretending{/i} to feel better but actually aren’t."
    c "I’m feeling better, Sensei."
    s "I also don’t want it to be one of those things where you don’t actually understand what’s going on and just rewrite it all into the most ideal situation inside of your-"

    scene chikaargue25
    with dissolve

    c "I am feeling better, Sensei! There is no longer a need to worry about Chika Chosokabe! All is good here in the life I’ve always wanted."
    s "Right..."

    scene chikaargue26
    with dissolve

    c "Want to stick around for dinner? There was a sale on beef at the grocery store, so I was planning on making stew or something tonight."
    c "Just don’t tell Yumi about it if you do. I told her there was only enough for two when I was mad and wanted to kill her."
    s "I’m good. But you should probably try and get in contact with her soon since you now know she’s done literally nothing wrong and that I am the truly horrible one here."
    c "Nah, you’re just a little confused. But that’s something we can work on together!"
    s "..."
    c "..."
    s "Chika...are you {i}really{/i} okay?"
    c "Mhm!"
    s "And you {i}really{/i} get what I was trying to tell you a couple minutes ago?"
    c "Mhm!"
    s "..."
    c "..."
    s "You know rabies is pretty much 100%% fatal if you don’t treat it immediately, right?"

    scene chikaargue27
    with dissolve

    c "What?"

    scene black
    with dissolve2

    s "Nothing. Forget I said anything."
    c "Wait! You forgot your kiss goodbye."

    "Chika pounces on me just as I turn to head back for the door, forcing my neck down by the collar of my shirt before planting a kiss on my lips."

    c "I love you!"
    s "..."
    c "Say it back~"
    s "I love you too..."
    c "Heheheh..."
    c "Come back soon, okay?"
    c "{i}I bought something super hot with my first paycheck from the maid cafe that I’ve been waiting to use with you.{/i}"
    s "Uhh...okay. Yeah."
    c "Oh, and tell Chinami I’ll come back inside in a sec. Just gonna take a minute to collect my thoughts and...finish air-drying my face from the tears."
    s "Yeah..."
    s "I’ll...see you later, Chika."
    c "Mhm! Laters!"

    "........."
    "......"
    "..."

    scene chikaargue28
    with dissolve2

    c "{i}Hah...{/i}"
    c "Well, this’ll definitely take some getting used to."

    scene chikaargue29
    with dissolve

    c "But at least I wasn’t dumped!"

    play sound "static.mp3"
    scene chikaargue30 with flash
    stop sound

    c "I just have a “different idea of what love is.” "
    c "He’s so cool. That’s such a mature thing to say. Like, obviously he would know better than me. "

    play sound "static.mp3"
    scene chikaargue29 with flash
    stop sound

    c "Yet, he’d still pick me over everyone else! "

    play sound "static.mp3"
    scene chikaargue31 with flash
    stop sound

    c "Ah! I have to apologize to Yumi. "

    if yumicthree == True:
        c "The threesome is back on."
    else:
        c "I was super hard on her earlier."

    play sound "static.mp3"
    scene chikaargue32 with flash
    stop sound

    c "But then I get to tell Chinami that everything is going to be okay!"

    scene chikaargue33
    with dissolve2

    c "That everything is going to be okay."

    scene chikaargue34
    with dissolve2

    c "That everything is going to be okay!"

    scene black
    stop music

    "{i}Chika has contracted [[RABIES]!{/i}"
    "{i}Her sanity has decreased by 10!{/i}"

    $ renpy.end_replay()
    $ chika_love += 1000
    $ chikaspring4 = True

    "{i}Her affection has increased by 1,000!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label chikaspring5:
    scene noonsky
    with dissolve2
    play music "notabluearchivesong.mp3"

    "Ahh, the afternoon — that magical time sandwiched between day and night. "
    "Not as magical as “noon” itself as that only lasts for sixty seconds, but magical nonetheless. "

    play sound "static.mp3"
    scene chikarinbath1 with flash
    stop sound

    "Which is further evidenced by these two naked girls in a bathtub! Just one of them is having a much easier time than the other for reasons you’re already well aware of."

    c "Are you just going to sit there and blush the entire time?"
    r "That’s the plan, yeah."
    c "Weird. I figured you’d be more open to looking at me naked after what happened in your room the other night."
    r "In my defense, you had your clothes on back then. And I was also not in the strongest state of mind after being yelled at by my mom for trying to fuck your boyfriend."
    c "Want me to rub your shoulders?"

    scene chikarinbath2
    with dissolve

    r "Don’t touch me. I’ll cum."
    c "Just relax, okay? I’m not gonna touch you, especially when Chinami is right outside the bathroom. Just think of it like being in the shower at school or the dorms."
    r "Those are way less...{i}intimate,{/i} though. In here, it’s just you and me. Which, up until recently, would have {i}probably{/i} been okay? But now, I’m...well...you know. There’s...history and stuff."

    scene chikarinbath3
    with dissolve

    c "You’re not going to feel weird around me forever now, are you? I was just trying to help you feel better."
    r "N-No! It won’t be forever! Just...probably for the immediate future since there’s still a lot I’m...confused about when it comes to you."
    c "Like what? Can I, like...help clear anything up? Or..."
    r "I, uhh..."
    r "You..."
    r "You still...love Sensei...right?"

    scene chikarinbath4
    with dissolve

    c "Yeah. With all of my heart. "
    r "Buuuut...you’re okay with...hooking up with other people now?"
    c "Not anybody. Just you. You’re the only person I’ve ever done anything with apart from Sensei."
    r "Okay, but..."
    r "Would you have ever {i}done{/i} that to...err...{i}with{/i} me if you hadn’t found out he’d been hooking up with other people?"
    c "Probably not, no."

    scene chikarinbath5
    with dissolve

    r "See?! That’s why I’m freaking out! The Chika I know wouldn’t ever do anything like that!"
    c "People change, Rin. I’m not the same girl I used to be. I’m smarter now."

    scene chikarinbath6
    with dissolve

    r "But are you “smarter” because you {i}want{/i} to be? Or because you {i}have{/i} to be?"
    c "What?"

    scene chikarinbath7
    with fade

    r "I just...you...you’re only the second person I’ve ever done stuff with. And if that was just because you were doing it to, like...get back at Sensei or something...I’m going to feel really shitty."
    c "It’s not like that at all, Rin. I promise. "
    r "Don’t promise me things like that because I’m just going to get hung up on it. You know how I am."
    c "I {i}do{/i} know how you are, which is why I’d never try and use you for something petty like that. "
    r "So...you wouldn’t do that to try and push me one way or the other? "
    r "Because another thought I had was that...you were kind of just...trying to pull me closer to you so I’d stop thinking about Sensei so much."

    scene chikarinbath8
    with fade

    c "..."
    r "Is that...wrong?"
    c "Yeah...and it really hurts to hear you say that."
    r "But you see how it must look from my point of view, right?! I followed you for {i}years{/i} and nothing happened! But then the second I like your boyfriend, you suddenly want to hook up with me? "
    c "I just wanted to-"
    r "I {i}know{/i} you...said you just wanted to make me feel better. I know. But...doing that kind of stuff with other people, like...{i}means{/i} something to me, Chika."
    c "It means something to me too. That’s why I did it. "
    r "But the timing is just...so...{i}off.{/i} And you’ve already been getting kind of crazy lately. So in my head it was all just, “does she even realize what she’s doing right now?” "
    c "You keep saying that. {i}Everybody’s{/i} saying that. How am I crazy? Just because I don’t look at things the same way as you? Is {i}that{/i} it?"
    r "Chika, do you have any idea just how many times you vented to me about being terrified that Sensei was seeing someone else? "
    c "Probably...a lot...I imagine."
    r "And now you’re just {i}fine{/i} with it? What happened to loyalty? What happened to being his and {i}only{/i} his?"

    scene chikarinbath9
    with dissolve

    c "That’s not...how love works. "
    r "No, that’s not how love works for {i}him.{/i} So it feels like you’re just changing your definition of that to adapt and...I don’t know...protect yourself? Does {i}that{/i} make sense?"
    c "..."
    r "I’m sorry, Chika. I know this isn’t the time or place, but..."
    r "I’m really worried about you. And if you’re not okay, you can just {i}talk{/i} to me. You don’t have to...you know..."
    c "How long...have you known about him, Rin?"
    r "What?"
    c "When I told you he was seeing other people, you didn’t seem surprised at all. "
    r "I-"

    scene chikarinbath10
    with dissolve

    c "How long have you known?"

    scene chikarinbath11
    with fade

    r "..."
    c "Do you think it was right of you to hide that? To just keep your mouth shut while I vent to you about fearing something you {i}know{/i} is happening? "
    r "No...I don’t think it was right. But I-"
    c "You did it because you wanted to protect me. You didn’t want to see me hurt."
    r "And...you’re not {i}mad{/i} about that?"
    c "Of course I’m mad. I could drown you right now."
    r "Please don’t. I want to die with my clothes on."
    c "I don’t intend to. You already told me you’d cum if I touched you and it’d be really degrading to watch you orgasm right before dying. "
    r "I feel like it would be kind of fitting, though. It makes sense that I’d go out like that."
    c "Well, you’re not going to go out at all. I’m keeping you here forever."

    scene chikarinbath12
    with dissolve

    r "You’re taking me hostage?! See?! I knew you were going crazy!"

    scene chikarinbath13
    with fade

    c "No, I’m keeping you {i}with me{/i} forever. How could I ever throw away someone who’d go through so much for my sake?"
    c "I know you hate keeping secrets and I know how hard you must have worked to hide all of that from me. And I’m sure it’s the same for Sensei too since I know you care about {i}him.{/i}"
    c "And maybe you’re right. Maybe I...am going out of my way to try and rewrite my thoughts on “love” to try and protect myself. I’m not saying it isn’t possible."
    r "Well, what {i}are{/i} you saying then? Because I still don’t get it. How can you go from being so loyal and so focused on him to pushing me down on the bed and making me cum my brains out?"
    c "I told you the other night. Because I love you."
    r "But you love me as a {i}friend.{/i} Sensei’s the one you {i}actually{/i} love."
    c "Maybe. But that still doesn’t change the fact that I {i}wanted{/i} to do what I did that night. I wasn’t just using you. I could never."
    r "But..."
    r "Hold on. If you {i}wanted{/i} to do that and {i}weren’t{/i} just confused or trying to push me in one direction, it would mean-"
    c "Don’t...try and figure it out. It’s confusing and weird and...{i}uncharacteristic, {/i} sure. But we don’t need to come up with some clear-cut definition of {i}what{/i} that was. It just...{i}was.{/i}"
    c "If you {i}and{/i} Yumi both think I’m going insane, there’s clearly some merit to it. You guys know me better than anybody. But then, that begs the question — if it’s keeping me happy...what’s the problem?"
    r "{i}Are{/i} you happy, Chika? Or are you just pretending to be because you’re afraid of everything falling apart?"
    r "You’ve already lost so much. No one would hold it against you for trying to keep yourself from losing Sensei {i}too.{/i}"

    scene chikarinbath14
    with dissolve

    c "I won’t lose Sensei...I’m winning."
    r "Winning {i}what?{/i} Him?"
    c "Yeah..."
    c "He loves {i}me{/i} most of all. "
    r "Chika..."
    c "..."
    r "What will happen if you find out he doesn’t?"
    c "If you know something about that, please just keep your mouth shut and don’t risk making me feel even worse. Okay?"
    r "I don’t...know anything about who he loves the most. But I hope for your sake that it {i}is{/i} you. If you’re actually fine with that and aren’t just pretending, I mean."
    c "..."
    r "Can you look at me for a second?"
    c "Hold on...I’m trying not to start crying."
    r "You can cry if you want. It’s okay. "
    c "Just...hold on. Okay?"
    r "..."
    c "..."

    scene chikarinbath15
    with dissolve

    c "Okay. Hi."
    r "I love you."
    c "I love {i}you.{/i}"
    r "..."
    c "..."
    c "Do we, like...kiss now? How does this work?"
    r "I don’t know. Like, I {i}want{/i} to. But it still feels weird."
    c "Yeah, same. "
    r "So you, like...like {i}really{/i} want to do stuff like that with me then? It’s not all just...for my sake?"
    c "Rin, do you really think I have been flirting and trying to dress you up in cute outfits for so long just because we’re {i}really good friends?{/i}"
    r "You...You’ve  been trying to seduce me this whole time?!"

    scene chikarinbath16
    with dissolve

    c "I don’t know if I’d say {i}seduce.{/i}"
    c "But I’d definitely be lying if I said I didn’t {i}occasionally{/i} imagine the two of us making out in my bed sometimes. "
    r "..."
    c "..."
    r "I need to get out of the bath now."
    c "Yes. I also need to do that."

    play sound "static.mp3"
    scene chikarinbath17 with flash
    stop sound

    c "Chinami! How would you feel if big sis Chika started dating girls instead of boys?!"
    r "Are we really going to drag {i}her{/i} into this now?"
    ch "Chinami wouldn’t care! But she’d be confused if it was big sis Yumi because that would make our family like the Lannisters! "
    ch "Also, she’s worried about what would happen to Papa!"

    scene chikarinbath18
    with dissolve

    c "I just wanted to see what she’d say. "
    r "Does she really call Sensei “Papa?”"
    c "Of course. He’s the closest thing to a dad she’s ever had. "

    scene chikarinbath19
    with dissolve

    r "Which...adds one {i}more{/i} reason you’re so afraid of losing him. Two hearts would be breaking instead of just one."
    c "Mhm! But we don’t have to worry about that since he’s never going anywhere. "
    r "..."
    c "..."

    scene chikarinbath20
    with dissolve

    r "Yeah...things will work out for you. They’ve {i}got{/i} to eventually."

    scene chikarinbath21
    with dissolve

    r "I guess you {i}did{/i} manage to score this apartment, though. This place seems really nice for what you’re paying for it."
    c "Right? I have no idea how the Tsukiokas make so much money with rent prices like these. "
    r "Again...it’s gotta be the fucking bubble wrap. I chose the wrong line of work."
    c "No cursing in front of Chinami. Remember?"

    scene chikarinbath22
    with dissolve

    r "Oh, shit. Sorry."
    c "Rin. Please."
    r "What?"
    c "..."

    scene chikarinbath23
    with dissolve

    r "Oh, fuck! I did it again!"
    c "Am I going to need to ban you from my apartment?"
    r "Probably! How the f...{i}frog{/i} does Yumi manage to control herself here?!"
    ch "Yumi froggin’ loves Chinami and wishes only the froggin’ best for her! That’s how! "
    c "Did you just accidentally corrupt my little sister?"

    scene chikarinbath24
    with dissolve

    r "I’m sorry. You can’t take me anywhere without me ruining everything. Just ban me now."
    c "You know, if you moved into one of the vacant rooms, I could ban you {i}and{/i} we could still hang out here. Then, I wouldn’t ever really need to go back to the dorms either."

    scene chikarinbath25
    with dissolve

    r "Move in? There are still empty rooms here?"
    c "Yeah, I don’t think all of them are listed yet. You can afford it after your raise, can’t you? Even more so if you bring Futaba along and add in what she gets from her parents."
    r "Futaba’s parents stopped sending her money months ago."

    scene chikarinbath26
    with dissolve

    c "What? They’re not still, like...MIA right?"
    r "She doesn’t seem as worried as she was in the beginning, but...yeah. She hasn’t heard from them in a while."
    c "Oh my God. I hope they’re okay. And not just because I want you guys to live here too. Futaba is a sweetheart and deserves only the best."

    scene chikarinbath27
    with dissolve

    c "{i}She’d{/i} never try to steal Chinami’s papa. Right, Rin?"
    r "Uh..."
    ch "What’s Chinami hearing about somebody trying to steal her papa?! Chinami will froggin’ kill them!"
    c "Chinami better stop using “frog” as a replacement for bad words or big sis Chika is going to take her games awaaaay!"

    scene chikarinbath28
    with dissolve

    ch "One day, Chinami will have justice!"
    r "Chika...about...what you just said..."
    c "Should I text Sensei and tell him to come over? This complex is {i}technically{/i} for women only, but Touka would definitely bend the rules if it’s for him, right?"

    scene chikarinbath29
    with dissolve

    r "Here?! Now?! Us?! Together?! Pajamas?!"
    c "What’s wrong, Rin? You’re not {i}nervous{/i} around him now, are you?"
    r "I am nervous around everyone. It’s part of my nature. "
    c "Theeeeeen should I press send?"

    scene chikarinbath30
    with dissolve

    r "I don’t even know what you wrote yet. Let me-"
    c "..."

    scene chikarinbath31
    with dissolve2

    r "Western silverback..."

    scene noonsky
    with dissolve2
    stop music fadeout 12.0

    c "I’m gonna do it. Here goes-"

    play sound "tackle.mp3"

    r "Don’t you dare! "
    c "Aah! Chinami! Your sister is under attack! Help!"
    ch "Hey! Get your froggin’ hands off of big sis Chika! "
    c "Chinami is grounded now!"
    ch "For helping?!"
    r "Chika! Give me the phooooone!"
    c "Neveeeeeeer!"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ chikaspring5 = True

    "Rin manages to secure the phone and backspaces the message before Chika ever sends it, but surely that doesn’t stop them from thinking about it."
    "Right?"
    "Surely, he remains the centerpiece of their fantasies."
    "Right?"
    "..."
    "Right?"

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label chikaspring6:
    scene noonsky
    with dissolve2
    play music "maidcafe.mp3"

    "Since the dawn of time, human beings have striven for one thing and one thing only — a place where all is bright and beautiful. And in the 1970’s, we finally found it. "
    "What I’m speaking of is, of course, the maid cafe. Which, believe it or not, was actually first conceived in the US."
    "And it would remain there for roughly three decades until Japan finally got its hands on it and turned it into the ever-growing empire it is to this day."
    "Tonight, that’s where I’ll be going. But it’s not just because I am a pervert. It’s not just because I’m bad with money. It’s not just because I’m adept at talking to girls either."
    "It’s because I am {i}all{/i} of those things at once. Which, as I’m sure you don’t understand since you are weak, is essentially {i}required{/i} to survive a place like a maid cafe — where cute girls prowl the room like lions."
    "{i}We,{/i} my friend, are meant to be their meals. But tonight? Tonight, I will feast upon them. And I will show them what humans are {i}truly{/i} capable of."

    play sound "static.mp3"
    scene chikathemaid1 with flash
    stop sound

    "Oh god, there are two of them. I’m done for."

    c "Sensei! Hi! Welcome in!"
    u "Not {i}Sensei,{/i} Chika-chan! This precious prince goes only by “Master” within these sacred walls! "
    c "Right! Of course! "

    scene chikathemaid2
    with dissolve

    c "Thanks so much for coming, Master! We’ve been eagerly awaiting your arrival!"
    u "That’s right, Chika-chan! And we’re super-duper excited to take extra good care of you today!"
    s "I would like to place an order for takeout."

    scene chikathemaid3
    with dissolve

    c "Do we even do that here?"
    u "I think Master is implying that he wants to take {i}us{/i} home."

    scene chikathemaid4
    with dissolve

    c "Then yes! You may place your order right now! Free of charge! But why wait until you get home when you can have us right here in the maid cafe?!"
    u "{i}Because,{/i} Chika-chan, that is something that we in the business call “illegal.”"
    c "It’s only illegal if you get caught! Right, Master?"
    s "Right. I’ll be taking Chika as my entree and Uta as dessert."

    scene chikathemaid5
    with dissolve

    u "And what would you like as an appetizer, Master? Might I recommend our brand new blueberry banana brownie batter baumkuchen?"
    s "That’s too many B’s. I’ll just take Osako."

    scene chikathemaid6
    with dissolve

    u "I think Osako-chan is off limits to everybody but precious princesses. "
    s "Just put a mask on her and tell her I’m Wakana. It’ll be fine. "

    scene chikathemaid7
    with dissolve

    u "Aah! Bad Master! You are bringing dark energy into a place of joy and love! Don’t force Uta-chan to cast her infamous death beam on you!"
    c "Sen...Master! You’re gonna pick me, right?! Do I get to serve you today?! I do, right?! Right?! RIGHT?!?!?!"

    scene chikathemaid8
    with dissolve

    u "Oh, Chika-chan. You sweet summer child. {i}This{/i} master is Uta-chan’s number one customer. He chooses her without fail any time he has the option. "
    u "And how could he not? Uta-chan {i}is{/i} the ultimate male fantasy of course."
    s "I choose Chika."
    u "See? Without fail. Every-"

    scene chikathemaid9
    with hpunch

    u "{b}{size=+20}YOU WHAT?!?!?!?!?!?{/b}{/size}"
    c "Yay! I knew it! I {i}knew{/i} Master would choose me! "

    "I’m sorry, Uta-chan...but this is for your own good."

    u "{b}{size=+20}WHY?!?!?!?! NO!!!! MONEY!!!{/b}{/size}"
    u "{b}{size=+20}I MEAN...MASTER!!!!{/b}{/size}"

    scene chikathemaid10
    with dissolve

    c "Don’t worry, Uta-chan! I’m sure you’d be his first pick if I wasn’t working! And if money’s the problem, I’ll split his bill with you as a special thanks for being so darn cute!"
    u "............"
    c "You look really upset right now."

    play sound "static.mp3"
    scene chikathemaid11 with flash
    stop sound

    u "Uta-chan is fine! Albeit mildly betrayed! But that’s okay because she’s going to make Master pay for it somehow!"
    c "How? "
    s "Yeah, how? I am also suddenly very intrigued. "
    u "That’s for {i}you{/i} to know and...wait, I said it wrong. That’s for Uta-chan to know and {i}you{/i} to find out! Ha!"
    c "You...sure you’re okay, Uta-chan? "

    scene chikathemaid12
    with dissolve

    u "{i}More{/i} than okay, Chika-chan. Because it just so happens that I have decided to dine {i}with{/i} Master today! And you will be serving {i}both{/i} of us! "
    c "Yay! Double money!"
    u "Uta-chan eats free."
    c "Boo! Single money!"
    s "Well, I guess I didn’t have to wait long to figure out how you were going to make me pay."

    scene chikathemaid13
    with dissolve

    u "Oh, this is just the beginning. Uta-chan is going to make you pay for this transgression for {i}years{/i} to come. You will regret this choice, Master. Mark my words."
    s "Uhhhh..."
    c "Come on, Sen...Master! Let’s get you seated and taken care of!"

    scene black
    with dissolve
    play sound "tackle.mp3"

    c "In the locker room! "
    u "Bad, Chika-chan! Are you {i}trying{/i} to turn this place into a blueberry banana brownie batter brothel?!"
    c "Buuuuuut don’t you think {i}this{/i} master deserves a little {i}special{/i} treatment? Huuuuuuh?"

    "Chika grabs my arm and all I can hope is that Uta’s anti-sexual contact forcefield is weak today."

    u "No touching! Bad! Bad, Chika-chan!"

    "Ugh. It’s not. It’s just as annoyingly strong as always."

    play sound "static.mp3"
    scene chikathemaid14 with flash
    stop sound

    "Regardless of the lack of hot locker room maid sex, I still {i}do{/i} get to order and be treated like a prince. "
    "But apparently, Chika is not yet trained in the art of the flavor beam, so it’s just a normal...huge omelet served to me by a cute girl."
    "Granted, it’s a cute girl who, just like in the bedroom, is eager and ready to do whatever I say."
    "And it brings me comfort knowing she would gladly suck me off beneath the table in uniform if only this {i}was{/i} a blueberry banana brownie batter brothel."

    c "Is there anything else I can get for you, Master? Osako-chan’s oolong tea is to {i}die{/i} for! And that {size=-20}bluebanberobthbaumukuchen{/size} is probably great too!"
    u "Say it right! That was way too quiet {i}and{/i} way too wrong!"
    c "Baumkuchen! It’s good!"
    u "Tch. Ami-chan was right. I guess that {i}is{/i} too many B’s."
    s "Is she here tonight? Can you tell her I’m-"
    c "Nope! No Ami here! Just Chika-chan! So it’s time for you to pay attention to {i}her!{/i}"
    u "Ahem. Chika-chan? You seem to have skipped my order. I would like one blueberry-"

    play sound "static.mp3"
    scene chikathemaid15 with flash
    stop sound

    c "One blueberry, coming right up!"
    u "You better bring me more than one blueberry, woman! This type of service would be unacceptable if Uta-chan had a penis! "
    s "If Uta-chan had a penis, I probably wouldn’t be her number one customer."

    scene chikathemaid16
    with dissolve

    u "Yeah well, you’re {i}not{/i} anymore. You’ve been demoted. Uta-chan’s number one customer {i}always{/i} picks Uta-chan. "
    s "Can I make it up to you by marrying you instead?"

    scene chikathemaid17
    with dissolve

    u "Fine. Ring please."
    s "..."
    s "I don’t have one on me."

    scene chikathemaid16
    with dissolve

    u "All talk like always. How predictable."
    s "You’re not, like...actually mad at me, are you?"

    scene chikathemaid18
    with dissolve

    u "Noooooo..."
    s "You totally are."
    u "Uta-chan is just jealous. That’s all. But she understands that Chika-chan can be unpredictable at times and is just going to hope that you’re only doing this so nobody gets hurt."
    s "That’s exactly it. She seems kind of...okay in {i}here,{/i} though. Apart from all the begging and...probably preparing you a single blueberry thing."

    scene chikathemaid19
    with dissolve

    u "Yeah, she actually fits in great here. She’s number two right after me now. Like, the gap is still pretty substantial. But she definitely has her fans. "
    s "Does she? I didn’t realize that many people would be into the whole maid gyaru archetype thing."
    u "Gyaru? No. Chika went with a different archetype."
    s "Did she? She didn’t seem to be putting on a character for me at all."
    u "Yeah, because it’s you. Just look at how she treats the other customers, though."

    play sound "static.mp3"
    scene chikathemaid20 with flash
    stop sound

    cf1 "C-C-C-Chika-chan! "
    c "Hi! Do you need something?"
    cf2 "We...um...we were thinking about maybe...asking Uta-chan to...serve us...n...next time..."
    c "................"
    cf1 "Oh God...her eyes...here it comes..."
    c "So you’re going to leave me all alone?..."
    cf2 "Mnh..."
    c "You realize this is my job, right?..."
    c "Should I just starve and die? Is {i}that{/i} what you want? You want Chika-chan to die?!"
    c "You’d never do that to me, right?! You {i}love{/i} Chika-chan! Don’t you?! You love me, don’t you?! Tell me you love me! Say it! Say it, say it!"
    cf1 "W-We love you, Chika-chan! We love you!"
    cf2 "W-We were only kidding about...asking for someone else!"
    c "Good! Because you don’t want to know what I would have done to you if you {i}weren’t.{/i} Your parents wouldn’t even be able to recognize you."

    scene chikathemaid21
    with dissolve

    c "It’s all because I love you, though! And I can’t wait to stay together forever and ever and ever and ever and ever and ever and if you ever look at another girl I will cut you into pieces!"
    c "Hahahah! Whoops! Just kidding!"

    scene chikathemaid22
    with dissolve

    c "Never fucking joke with me like that again. Got it? Good. Die, you fucking pigs."

    scene chikathemaid23
    with dissolve

    os "Uhh...{i}sorry{/i} about that. Chika-chan is-"
    cf1 "She called us {i}pigs!{/i}"
    cf2 "She told us to {i}die!{/i} Did you hear that?!"

    scene chikathemaid24
    with fade

    s "Oh."
    u "Yeah. Apparently, a lot of girls are just really into that. Either that or they just fear for their lives. But any first-timer who’s ever been served by Chika has never asked for anyone else."
    u "Not like I’m gonna complain, though. If it works, it works. She’s clearly got a {i}thing.{/i}"
    s "Yeah...I think I like your style a little more. Fearing for my life doesn’t really do it for me most of the time."

    scene chikathemaid25
    with dissolve

    u "She’s okay though, right? Like...that’s not {i}actually{/i} something we should be worried about her saying to customers."
    s "..."
    u "Master?"
    s "..."
    u "Master, are you in danger? Blink once for yes and twice for no."
    s "How many more years until we can move to Nara together?"

    scene chikathemaid26
    with dissolve

    u "D-Don’t make my heart hurt at work, dummy! Uta-chan needs to look presentable and I can already feel myself getting hot!"
    c "Well, you better not be getting hot for {i}my{/i} master, Uta-chan!"

    play sound "static.mp3"
    scene chikathemaid27 with flash
    stop sound

    c "One very special blueberry for a very special girl! Where would you like it? Shall I feed it to you myself?"
    u "{i}Ahem.{/i}"
    u "Chika. You are fired."

    scene chikathemaid28
    with dissolve2

    c "Should I just starve and die?..."
    c "Is {i}that{/i} what you want? You want Chika-chan to die?! Is {i}that{/i} it, Uta?! HUH?!"

    scene black
    with dissolve2

    u "I just want dessert! Why can’t you treat me like Sensei?!"
    c "His...name...is...MASTER! YOU WILL ADDRESS HIM AS SUCH OR I WILL TELL HIM ABOUT THE TIME YOU ALMOST KISSED AMI!"
    s "The time you {i}what?{/i}"
    u "PHPHPHBHBHHBHAAAA!!!! NOTHING!!! SHE’S MAKING THAT UP, MASTER! UTA-CHAN ONLY HAS EYES FOR YOU!"
    c "KEEP YOUR EYES OFF OF MY MASTER!!!!"
    cf1 "Um! C-Chika-chan! We’re ready for our b-"
    c "WHEN DID I GIVE YOU PERMISSION TO SPEAK!?"
    cf2 "W-W-W-We’re sorry!!!!!!!"

    "So yeah, I think it’s probably safe to say that Chika has gone off the deep end."
    "Which...was probably safe to say quite a while ago."

    stop music
    play sound "static.mp3"
    scene chikathemaid29 with flash
    stop sound
    play music "starvingtodeathoutofreachofthesun.mp3"

    "But there are moments every now and then where her true self peeks out again. And {i}those{/i} are the moments I hope for every time I go out of my way to see her."
    "I still love her at the end of the day. And if I’m not able to do that just because she’s a little bit broken now, how am I supposed to expect anyone to ever love {i}me?{/i}"
    "This rings especially true when I remember I’m the one who cracked her in the first place. I just can’t really see any of the damage when she looks at me with eyes like those."

    c "I am {i}so{/i} glad you came to see me at work today. It was nice getting to serve somebody I actually {i}like{/i} for a change."
    s "Yeah...you seemed pretty harsh on those two girls back there."
    c "That’s because they look at me with eyes that only {i}you{/i} should look at me with. The hungry kind. Like they want to devour me whole."
    s "And it would be fine if I devoured you then?"
    c "You can devour me whenever you want. And I’m not just the entree, Sensei. I’m a full three-course meal."
    s "Well, you definitely look great in the uniform."
    c "And yet a certain someone still hasn’t gotten to experience what it’s like to take it {i}off{/i} of me."
    s "One day, sure. Not tonight though, if that’s what you’re getting at."
    c "Why not? There’s a karaoke place on the way back to my apartment that I’ve heard basically no one ever monitors."
    s "Yeah...{i}definitely{/i} not a karaoke place. I don’t have a good track record with those."

    scene chikathemaid30
    with dissolve

    c "...oh."
    c "I didn’t realize you’d...done stuff there with other girls."
    s "..."
    c "..."
    s "Chika, can we talk?"

    scene chikathemaid31
    with dissolve

    c "Please don’t break up with me."
    s "...What?"
    c "Everyone’s telling me I’m going crazy. But I don’t {i}feel{/i} crazy. So if {i}you{/i} think I’m going crazy too, just...I don’t know. {i}Please{/i} don’t break up with me, though. I’m really trying. Really."
    s "Who have you heard that from? That you’re going crazy. Yumi?"
    c "Plus Rin. And the girls at the maid cafe. Hell, even Sana’s pointed it out and I barely even know her."
    s "Yeah, well...Sana’s not the most particularly sane person either, I don’t think."
    c "And it’s not just because I’m seeing love the way you do now, right? Like...there’s more to it than that. There has to be, right? Because no one calls {i}you{/i} insane for thinking that way. Why me? Why-"
    s "Chika...you really don’t need to try and adapt to my way of thinking if you’re struggling with it."
    c "No, I {i}do.{/i} Because the alternative is me finding out you’ve been cheating on me with a million other people and...I don’t..."
    c "I don’t think you understand what that would do to me, Sensei."

    scene chikathemaid32
    with dissolve

    s "So you’d rather I just...what? Keep you in the dark forever?"
    c "I’d rather you love just me and only me. And I get that you {i}don’t.{/i} I {i}obviously{/i} get that. It just...fucking sucks. Like, I don’t even know who else you’ve {i}been{/i} with. I feel so...ignored. And just...all around shitty."
    s "Yet, you’re desperate for me to not break up with you."
    c "Hurting with you beats hurting alone."
    s "You’re not alone, Chika. There are plenty of other people with more love to offer you than I can."
    c "Well, what if I took it all?"
    s "What?..."
    c "Would you be able to stay with me if I did the same thing {i}you{/i} do? And {i}love{/i} other people?"

    scene chikathemaid33
    with dissolve

    s "It’s not my place to tell you what you can and can’t do."
    c "But it {i}is{/i} your place to tell me how it would make you feel!"
    c "I have given you {i}everything.{/i} Not just my body and my heart, but my {i}family.{/i} I have cried more tears for you at this point than I did for my fucking father when he walked out on me. That {i}means{/i} something."
    c "So yeah. I {i}am{/i} going to force myself to change if you need me to do that in order to live with the guilt that I {i}know{/i} you have for hurting me. But I need you to give me something too. I deserve that."
    s "What do you want, Chika?..."
    s "I can’t just {i}stop{/i} being the way I am. If I could, I’d have done it already."
    c "I need you...to {i}need{/i} me."

    scene chikathemaid34
    with dissolve2

    c "It’s {i}that{/i} simple."
    c "I can handle the love thing. I can {i}make{/i} myself believe it. And..."

    scene chikathemaid35
    with dissolve

    c "Maybe, I’ve...kind of...already {i}started{/i} to."

    scene chikathemaid36
    with dissolve

    c "But there’s still this huge void in my chest that feels like it’s getting wider every single day, and you’re the one I want to fill it."
    s "Chika...why are you betting everything on the {i}first{/i} person you’ve ever fallen for? A depraved and depressed teacher, no less. You’re {i}so{/i} much smarter than this. Smarter than {i}me.{/i}"
    c "Words can’t explain it."
    c "You just have to believe me when I say it has to be you...or no one at all."
    s "..."

    scene chikathemaid37
    with dissolve

    c "I’m sorry for just...springing this on you. Things have been weird lately and it’s all just...coming out."
    s "No, it’s fine...this is what I wanted when I told you in the first place."
    c "You only told me at all because you {i}had{/i} to or I was going to kill Yumi."
    s "Well, what do you want me to do now then? Give you every single detail? Weigh in on what I’d {i}really{/i} do if you followed in my footsteps? How do I fix this?"

    scene chikathemaid38
    with dissolve

    c "Fix?..."
    s "..."
    c "So..."
    c "You’re not going to break up with me then?"
    s "I don’t have the fucking balls to break up with {i}anyone.{/i}"
    s "And even if I did...you’re..."
    s "Special...I guess."

    scene chikathemaid39
    with dissolve

    c "Mm."
    c "I’m winning..."
    s "..."
    c "..."
    c "Can I ask you something?"
    s "Sure. I can’t guarantee my answer won’t just make everything worse, though."
    c "If I was never in your class...and just some girl you met maybe five...ten years from now..."
    c "Do you think you’d ask me for my number?"

    scene chikathemaid40
    with dissolve2

    s "...I don’t get it."
    c "Me neither."
    c "I just want to know."
    s "Uh..."
    s "I’m...not really sure. I think the...context would probably matter? Asking someone for their number out of nowhere is a little weird, isn’t it?"
    c "Fair. I think I’d ask for yours before you even had a chance to anyway."
    s "Yeah well, your feelings for me are clearly stronger than mine since they’re only aimed at one person instead of everyone you’ve ever met. Of course you’d win out in that scenario."
    s "Assuming you don’t already have a boyfriend in this make believe world five or ten years from now."
    c "Who says I wouldn’t have a girlfriend instead?"
    s "Your track record of sleeping with only men."
    c "And if I had a secret lesbian tryst behind your back? Would your opinion of me change at all?"
    s "Yeah. I think you’d be way cooler."

    scene black
    with dissolve2

    s "But I’d also never forgive you for not inviting me."
    c "Hahah! I’ll keep that in mind for next time."
    s "{i}Next{/i} time?"
    c "I’m a baaaaaad girl, Sensei! Really just following in your footsteps. Always horny and always open for business!"
    s "Mhm. Right. So you just want me to think you’re cool."
    c "Maaaaaybe! I’ll just have to keep you in the dark, though. For your {i}own{/i} good, of course."
    s "Is that what you want {i}me{/i} to do then? Just...never bring this up again? Let you keep living your monogamous fantasy life where you’re always winning and always blissfully ignorant?"
    c "Heheh...maaaaaybe."
    s "That’s a serious question, Chika. I want to avoid hurting you however I can. Just-"
    c "Just without changing who you are."
    s "..."
    c "Leave the changing to me, Sensei...I’m young. I still {i}can.{/i}"
    s "I hate that I’m doing this to you."
    c "I think you {i}love{/i} that you’re doing this to me. Otherwise, you’d go after girls your own age."
    s "Okay, maybe you {i}are{/i} actually cool. That’s a level of sass I fully deserve."
    c "If you think I’m cool now, you should see me at karaoke."
    s "I already told you, no sex tonight."
    c "But there’s no better time {i}to{/i} have sex than right after talking your feelings out! I wanna do it! Pleeeeeeease?"
    s "..."
    c "{i}Pleeeeeeeeease?{/i}"
    s "Not tonight."
    s "I feel like this is a good place to leave things."

    $ renpy.end_replay()
    $ chikaspring6 = True
    $ chika_love += 1

    jump chikaspring7

label chikaspring7:
    if _in_replay:
        play music "starvingtodeathoutofreachofthesun.mp3"

    scene clearnightsky
    with dissolve4

    "It was a good night for Chika Chosokabe."
    "She was taking either a step forward or backward depending on your motivations for being here and, for the first moment since her tongue departed her good friend’s clitoris, she was actually kind of happy."
    "She wasn’t happy in the sense that things were going well, though. Just that they weren’t getting any worse. And that they probably couldn’t {i}get{/i} any worse unless her boyfriend started fucking her little sister too."

    if chinamicthree == True:
        "It was a possibility, she thought. She hadn’t forgotten the time he brought her name up during discussions of a potential threesome, despite how much she wanted to."

    "That would be rock bottom, though. She’d probably just die if things ever came to that. But things would {i}obviously{/i} never come to that because she had just solved everything!"
    "She’d managed to confront him and partially explain her stance and mindset in a mostly mature way, reminiscent of the way she used to be before the worm of Giles Corey began to eat away at her brain."

    scene hypercube1
    stop music

    "But it all felt too easy. It all felt too simple. Which meant it all felt so wrong."
    "This wasn’t the type of issue that could be solved in a single talk on the way home from work. This would require tears. Pain. Memories of hints that sneak in before late night panic attacks in the bathroom."
    "She was far too coherent for any of it to feel real."
    "Which, in turn, led to her questioning just how much of what she knew was actually {i}fake.{/i}"

    play sound "dooropen.mp3"
    scene hypercube2
    with dissolve

    c "Chinami! I’m home!"
    ch "Welcome home, big sis Chika! Chinami missed you while you were at work today!"

    "Oh, good. She wasn’t being fucked."

    scene black
    with dissolve2
    scene hypercube3
    with dissolve2

    "But she {i}was{/i} being different."
    "What a silly girl she was — always using her femur to bash the dinner bell. Idling like the bed of Jesus as she gazes out the window, dreaming of peanuts and pancakes."

    c "What are you doing, weirdo? Come give me a hug."
    ch "Welcome home, big sis Chika! Chinami missed you while you were at work today!"
    c "Uh...yeah. Big sis Chika missed you too. And guess what? She ran into Papa on the way home. And she thinks she’s going to start trying to act a little more like her old self again so-"
    ch "Welcome home, big sis Chika! Chinami missed you while you were at work today!"
    c "..."
    c "Chinami?"
    c "Are you okay?"

    scene black
    with dissolve2
    scene hypercube4
    with dissolve2

    ch "Welcome home, big sis Chika! Chinami missed you while you were at work today!"
    c "Yes. Chinami has said that many times now. Which means Chika is worried Chinami is sleepwalking again."

    "She used her hand to shoulder. An act of reassurance. The kind that Mom would bake."

    ch "Welcome home, big sis Chika! Chinami missed you while you were at work today!"

    scene hypercube5
    with dissolve

    "But when that shoulderbird don’t sing, we’re left to question how to make-"

    c "Chinami...come on. Stop acting weird."

    "Coffee in each glorious way — each melodious aroma misconstrued."

    ch "Welcome home, big sis Chika! Chinami missed you while you were at work today!"

    "With the creaking of seventh step, you’ll see {b}what{/i} I am to you."

    c "Chinami. Wake up. You’re doing it again."
    six "The one who really needs to wake up is {i}you!{/i}"

    play sound "static.mp3"
    scene hypercube6 with flash
    stop sound

    c "Huh?! Who’s there?! What are you doing in my-"
    six "{size=-10}e2 e6 96 16 76 16 02 56 67 96 c6 02 e2 47 96 02 56 b6 16 47 02 e2 56 d6 f6 36 02 e2 c6 56 56 66 02 57 f6 97 02 47 16 86 47 02 b6 37 16 02 56 77 02 e2 e6 56 47 37 96 c6 02 57 f6 97 02 47 16 86 47 02 b6 37 16 02 56 77 02 e2 d6 f6 f6 27 02 56 47 96 86 77 02 56 86 47 02 e6 96 02 37 57 02 e6 96 f6 a6 02 57 f6 97 02 47 16 86 47 02 b6 37 16 02 56 77 02 e2 27 56 86 47 f6 e6 16 02 f6 47 e6 96 02 76 e6 96 e6 27 57 47 02 56 27 f6 66 56 26 02 56 b6 16 47 02 e6 16 36 02 e6 f6 37 27 56 07 02 56 e6 f6 02 47 16 86 77 02 f6 47 02 47 96 d6 96 c6 02 16 02 37 96 02 56 27 56 86 47 02 c2 76 e6 96 56 26 02 56 d6 96 47 02 56 86 47 02 27 f6 66 02 57 f6 97 02 c6 56 57 66 02 97 16 d6 02 e6 96 16 07 02 56 c6 96 86 77 02 46 e6 16 02 e2 e6 96 16 07 02 e6 96 02 46 56 47 c6 57 37 56 27 02 37 16 86 02 66 c6 56 37 27 57 f6 97 02 27 f6 66 02 b6 e6 96 86 47 02 f6 47 02 46 56 67 96 56 36 56 27 02 56 67 16 86 02 57 f6 97 02 97 47 96 e6 57 47 27 f6 07 07 f6 02 86 36 16 56 02 e2 56 36 96 f6 86 36 02 47 86 76 96 27 02 56 86 47 02 76 e6 96 b6 16 d6 02 56 27 16 02 56 77 02 47 16 86 47 02 57 f6 97 02 56 27 57 37 37 16 02 e6 16 36 02 56 77 02 c2 56 56 27 76 16 02 97 c6 56 47 16 96 46 56 d6 d6 96 02 47 f6 e6 02 97 16 d6 02 57 f6 97 02 56 c6 96 86 77 02 46 e6 16 02 e2 e6 96 02 66 c6 56 37 27 57 f6 97 02 46 e6 57 f6 66 02 56 67 72 57 f6 97 02 56 36 16 c6 07 02 56 76 e6 16 27 47 37 02 37 96 86 47 02 e6 96 02 56 67 96 67 27 57 37 02 f6 47 02 57 f6 97 02 86 36 16 56 47 02 46 e6 16 02 57 f6 97 02 56 b6 16 47 02 c6 c6 96 77 02 56 77{/size}"

    scene black
    $ renpy.pause(3, hard=True)
    scene hypercube7
    $ renpy.pause(3, hard=True)
    scene black
    with dissolve4
    $ renpy.pause(2, hard=True)
    scene hypercube8
    with dissolve4
    $ renpy.pause(3, hard=True)
    play sound "pabell.mp3"
    $ renpy.pause(4, hard=True)
    scene hypercube9
    with dissolve4
    $ renpy.pause(3, hard=True)
    c "Mm?..."
    vpa "Chika Chosokabe — your attendance is required for the Transpacific Sadness Symposium in nineteen years, eleven days, six hours, and fourty-four minutes."
    vpa "The current temperature is a sweltering ninety-seven degrees Fahrenheit. You may experience difficulties using certain outdated technology due to the heat."
    vpa "The time of day is somewhere between 2:00 PM and 4:30 PM. The exact time is not currently able to be confirmed. We apologize for the inconvenience."
    vpa "To show you how sorry we are, we cordially invite you to the Spacy’s Summer Blast Savings event. Please speak to your guide in order to request more information."
    play sound "pabell.mp3"
    $ renpy.pause(3, hard=True)
    c "A...dream?..."
    scene hypercube10
    play sound "cube1.mp3"
    $ renpy.pause(2.5, hard=True)
    play sound "static.mp3"
    scene hypercube11
    with flash
    stop sound
    c "What?..."

    scene black
    with dissolve2
    $ renpy.pause(1, hard=True)
    scene hypercube12
    with dissolve3
    $ renpy.pause(1, hard=True)
    scene hypercube13
    play sound "cube2.mp3"
    $ renpy.pause(3, hard=True)
    scene hypercube12
    $ renpy.pause(1, hard=True)
    scene hypercube14
    play sound "cube3.mp3"
    $ renpy.pause(3, hard=True)
    scene hypercube12
    $ renpy.pause(1, hard=True)

    scene black
    with dissolve2
    $ renpy.pause(1, hard=True)
    scene hypercube15
    with dissolve4
    $ renpy.pause(1, hard=True)

    c "Hello?..."
    $ renpy.pause(1, hard=True)
    scene hypercube16
    play sound "cube4.mp3"
    $ renpy.pause(2, hard=True)
    scene hypercube15
    $ renpy.pause(1, hard=True)

    c "Everyone is right. I {i}am{/i} going insane."

    scene hypercube17
    play sound "cube5.mp3"
    $ renpy.pause(4.2, hard=True)
    scene hypercube15
    $ renpy.pause(1, hard=True)
    scene hypercube18
    play sound "cube6.mp3"
    $ renpy.pause(2, hard=True)
    scene hypercube15
    $ renpy.pause(0.5, hard=True)
    c "Why would God...give {i}me{/i} a gift?"
    c "I’ve never been special at all."
    c "I’ve done nothing to deserve this."
    $ renpy.pause(1, hard=True)
    scene hypercube19
    play sound "cube7.mp3"
    $ renpy.pause(2, hard=True)
    scene hypercube15
    $ renpy.pause(1, hard=True)
    scene hypercube20
    play sound "cube8.mp3"
    $ renpy.pause(2, hard=True)
    scene hypercube15
    $ renpy.pause(1, hard=True)

    c "Am I supposed to do something?..."
    c "What do you mean?..."
    $ renpy.pause(1, hard=True)
    scene hypercube21
    play sound "cube9.mp3"
    $ renpy.pause(2, hard=True)
    scene hypercube15
    $ renpy.pause(1, hard=True)
    scene hypercube12
    $ renpy.pause(1, hard=True)
    scene hypercube22
    play sound "cube10.mp3"
    $ renpy.pause(2.2, hard=True)
    scene hypercube12
    $ renpy.pause(1.5, hard=True)
    c "Excuse me?..."
    scene hypercube23
    play sound "cube11.mp3"
    $ renpy.pause(2.2, hard=True)
    scene hypercube12
    $ renpy.pause(1, hard=True)
    scene hypercube24
    play sound "cube12.mp3"
    $ renpy.pause(2.8, hard=True)
    scene hypercube12
    $ renpy.pause(3, hard=True)
    scene hypercube25
    play sound "cube13.mp3"
    $ renpy.pause(2, hard=True)
    scene hypercube12
    $ renpy.pause(1, hard=True)
    scene hypercube26
    $ renpy.pause(4, hard=True)
    scene hypercube27
    with dissolve3

    "She approaches the cube, which remains perfectly still. The way it always has. The way it always will."
    "She gazes into its depths, uncovering secrets of the earth’s formation. Every way to brew coffee. How to make yourself look even more beautiful for the person you love."
    "There are so many answers packed inside that she can’t figure out what to ask."
    "So she defaults to what an earlier voice told her."

    c "I’d like to know more about the Summer Blast Savings event at Spacy’s."

    $ renpy.pause(1, hard=True)
    scene hypercube28
    play sound "cube14.mp3"
    $ renpy.pause(1.7, hard=True)
    scene hypercube27
    $ renpy.pause(1, hard=True)
    scene hypercube29
    play sound "cube15.mp3"
    $ renpy.pause(1.8, hard=True)
    scene hypercube27
    $ renpy.pause(1, hard=True)
    scene hypercube30
    with dissolve4

    "She reaches out toward the cube."
    "She feels like she has to."
    "It’s what everyone else in her grade is doing."

    scene black
    $ renpy.pause(5, hard=True)
    "Success."
    "Finally, something."

    play sound "static.mp3"
    scene chikasymp1 with flash
    stop sound
    play music "firstsecondmall.mp3"

    "After being sucked into the cube, Chika Chosokabe awakens with a renewed sense of self — directly in front of the Spacy’s Summer Blast Savings event."
    "And what she sees before her is nothing short of the most exciting thing in {i}any{/i} context that she has ever seen."

    play sound "static.mp3"
    scene chikasymp2 with flash
    stop sound

    "Lovers! As far as the eye can reach with its fingers! So long as they’re nearsighted eyes that can’t escape the grips of the Great [[REDACTED] Mall."
    "As the pungent stenches of sex and body odor assault her senses, however, she can do little more than stand there in shock."
    "So many penises! So many vaginas! So much moaning and groaning, turning and churning!"
    "But while her heart’s quickly burning, she’s suddenly learning that she hasn’t been crazy at all!"
    "One more misbegotten beguiling for the pile, she smiles — scribbling neatly of self-deceit on the back of a treat receipt before begrudgingly smudging her words in defeat. That cheat!"
    "He had swooned her! Groomed her! Touched her from her head to her feet! Yet he’s been out on the street, calling others his sweet, while she slaved over a stove so her sister could eat?!"
    "No! Unacceptable! But sad. So sad. She was so very, sad. She knew he meant no wrong! Sex is like bowling for adults. She just needed to get better at it. And she was in just the right place to do that."

    play sound "static.mp3"
    scene chikasymp3 with flash
    stop sound

    "She probably wouldn’t though, seeing as the only thing keeping her from vomiting in her mouth at the idea of someone else entering it was the fact that she had never seen so many dicks at the same time before."

    play sound "pabell.mp3"
    $ renpy.pause(4, hard=True)

    vpa "Thank you for attending the annual Spacy’s Summer Blast Savings event. The sale is now complete."
    vpa "Please exit the store and find a partner for the dance as soon as possible. Refreshments will be provided for those in need of a break."
    c "{b}What the fuck is happening right now?{/b}"
    seco1 "It’s the...Spacy’s...Summer Blast...Savings event! It’s the best...aah...orgy...of the year!"
    limo "I’ve...gotten...nine different girls...pregnant today! My wife...is going to be...so proud! She’s always...wanted kids!"
    rmo "If you...still need a partner...you can...join me! I’m almost...done with...this one!"
    littlegirl "Noooo! I want more! Stay with me! I need it! I need more cuuuuuum!"
    pmee "(Very loud sex noises)"

    play sound "static.mp3"
    scene chikasymp4 with flash
    stop sound

    c "No...No...Sex isn’t...supposed to be like this! It’s...something you do...with...someone...someone you..."
    q "{b}MAY I HAVE THIS DANCE?{/b}"

    play sound "static.mp3"
    scene chikasymp5 with flash
    stop sound

    c "What?! Huh?! Who the...{i}what{/i} the fuck are you?!"
    q "LONELY..."
    q "SAME...AS YOU..."
    c "I...I have a boyfriend! I-I-I don’t “dance” with just anyone. Especially not creepy fucking monster things. Not even in my dreams. Sorry. Bye."
    q "NO ONE...SINGLE HERE..."
    q "ALL...WANT...FUCK..."
    c "Absolutely not. Leave. Now. Go."
    q "EVERYBODY’S DOING IT..."
    q "WHY MATTER IF NOT LOVE?..."
    c "Because I’m not going make myself vulnerable for some...{i}thing{/i} that probably wants to eat me!"
    q "YOU FUCK...HUMAN? ONLY?"
    c "Yes. Human only. Boyfriend only. His name “Sensei.” I fuck him. He not here."
    q "YOU HERE."
    c "Yes. I’m here."
    q "IF YOU HERE...YOU WANT FUCK..."
    c "No. For the last time, I-"
    ch "Ah! Big sis Chika!"

    play sound "static.mp3"
    scene chikasymp6 with flash
    stop sound

    ch "Chinami didn’t know you were coming to the Spacy’s Summer Blast Savings event!"
    c "C-Chinami?! What are you doing here?! Get away from that thing right now!"
    ch "Chinami loves the Spacy’s Summer Blast Savings event! She comes every year! There are so many nice ojii-sans who always give her tons of treats! All she needs to do is make them feel good."
    c "Chinami...does what?"

    scene chikasymp7
    with dissolve

    ch "Who’s that, big sis Chika? Is that your dance partner? I haven’t seen him here before!"
    q "H...HELLO...PRETTY GIRL..."
    c "He’s not my partner, Chinami! I’m in love with your papa, remember?! Good girls are only supposed to have {i}one{/i} partner! Now please let go of that thing and come here!"

    scene chikasymp8
    with dissolve

    ch "That’s no good, big sis Chika! Everyone helps everyone at the Spacy’s Summer Blast Savings event! So it’s {i}our{/i} job to make all of the ojii-sans feel good!"
    c "Chinami!"
    ch "What’s wrong? Everybody’s doing it."
    q "WANT...TOUCH...PRETTY GIRL..."
    ch "Okay! Chinami will help {i}two{/i} ojii-sans at once today! And she’s super experienced, so she’ll help you both feel reeeeeeally good!"

    play sound "static.mp3"
    scene chikasymp9 with flash
    stop sound

    c "No. Stop. I will do it. I will dance with the faceless ones. All of them."
    c "I will do whatever it takes to protect my sister."
    ch "Aww, big sis Chika loves Chinami so much! But Chinami isn’t in any {i}danger,{/i} so there is no need to protect her at all!"
    ch "Maybe Chinami and big sis Chika can help our ojii-sans together?"
    c "Yes. That is a good idea, Chinami."
    c "Everybody’s doing it."
    q "FUCK...TWO PRETTY GIRLS...ONE TIME..."
    q "THIS...HEAVEN...YES?"
    c "Yes."

    stop music
    scene black

    c "This is Heaven."

    $ renpy.pause(4, hard=True)
    play sound "dooropen.mp3"
    $ renpy.pause(1.5, hard=True)
    c "Chinami!"

    play sound "static.mp3"
    scene chikasymp10 with flash
    stop sound

    c "I’m home."

    play sound "static.mp3"
    scene chikasymp11 with flash
    stop sound
    $ renpy.pause(5, hard=True)
    scene chikasymp12
    $ renpy.pause(5, hard=True)
    scene chikasymp13
    $ renpy.pause(5, hard=True)
    scene hypercube1
    $ renpy.pause(5, hard=True)
    scene black
    $ renpy.pause(5, hard=True)

    $ renpy.end_replay()
    $ chikaspring7 = True

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label chikaspring8:
    scene noonsky
    with dissolve2
    play music "notabluearchivesong.mp3"

    "The sun is shining, the wind is blowing, and I once again feel like throwing myself off of a bridge."
    "That’s happening pretty frequently now that both my childhood friend and daughter have left me to rot in the house alone."
    "It happened when they were there, too. It’s just especially bad now."
    "But that’s nothing a little medicine won’t fix."

    play sound "vibrate.mp3"

    "And by medicine I mean sex because Chika is calling me right now and I’m not sure if I’ve ever been this happy to say that before."

    play sound "phonebeep.wav"

    s "Hello?"
    c "{i}Hi! Are you busy? Because if you’re not, I would very much like for you to come have all of the sex with me right now.{/i}"
    s "All of it?"
    c "{i}Yes. All of it. There will be no sex left for anyone after tonight.{/i}"
    s "I don’t know if I can do that to humanity, Chika. Can’t we just have {i}some{/i} of the sex instead?"
    c "{i}No. It needs to be all of it. This is one thing I will not budge on, Sensei.{/i}"
    s "That’s fine. I always figured I’d cause the destruction of the universe in one way or another. Might as well go out with a bang."
    c "{i}Many bangs. I am going to destroy you.{/i}"
    s "Wow. You are {i}feeling{/i} it today, huh?"
    c "{i}Just get over here and usher in the apocalypse with me! I’m going crazy!{/i}"

    play sound "phonebeep.wav"

    "Chika hangs up the phone without realizing that the apocalypse is infinitely closer than she could ever imagine."
    "Also, she is already crazy — so she is clearly lying about going crazy right now."

    scene black
    with dissolve2

    "Regardless, I have a duty to uphold. "
    "And if my borderline insane girlfriend thing (or whatever you want to call her) needs me to have all of the sex with her, I’ll be damned if I don’t give her what she wants."

    play sound "static.mp3"
    scene chikamaidsex1 with flash
    stop sound

    "I can’t say I expected a foursome, though. Especially one of this nature."

    c "Yes! Finally!"

    scene chikamaidsex2
    with dissolve

    c "Okay! Bye, you two! Have fun in Tsukasa’s room for the indefinite future! I need to study! Immediately!"
    ch "Papa, what have you done to Big Sis Chika?"
    s "How should I know? I literally just got here."
    c "I just really want to learn so I can get a high-paying job one day and repay Touka and Sensei for all of the kindness they have showed me! Bye now!"
    ch "Something tells Chinami this isn’t about studying."

    play sound "static.mp3"
    scene chikamaidsex3 with flash
    stop sound

    c "Nonsense! Big Sis Chika has been working super hard in school lately to make up for a distinct lack of Papa! "
    c "But there are certain things only {i}Papa{/i} can teach her! Which is why she needs to study with him {i}right{/i} now!"
    ch "Chinami just doesn’t understand why Big Sis Chika doesn’t study with her friend who wears the skull pin and keeps visiting our house! "

    scene chikamaidsex4
    with dissolve

    c "RIGHT NOW."
    ch "But {i}Chinami{/i} wants Papa-time too!"

    play sound "static.mp3"
    scene chikamaidsex5 with flash
    stop sound

    tk "Come on, Chinami. We can go be deprived of our fathers together."
    tk "We’re clearly not wanted here and they clearly want to do {i}adult{/i} things they think we aren’t ready for."
    c "Nope! We just need to study, remember? But it’s an extra super secret studying session you can’t be around for. So please come nowhere near the door until I call you. Thanks!"
    ch "Papa! Make Big Sis Chika let Chinami stay! Her time on this planet is limited!"
    s "No can do, Chinami. Not this time."

    scene chikamaidsex6
    with dissolve

    ch "AAAAAAAAH! FINE!"

    scene black
    with dissolve

    ch "BUT IF CHINAMI GETS SICK ON THE WAY TO TSUKASA’S ROOM, HER BLOOD WILL BE ON BOTH OF YOUR HANDS!"
    tk "I’m right next door. Are you really that weak?"

    play sound "dooropen.mp3"

    ch "YES! AND IT’S VERY SAD AND MORE PEOPLE SHOULD CARE!"

    play sound "doorslam.mp3"
    scene chikamaidsex7 with hpunch

    c "..."
    s "..."
    c "Why are my clothes still on?"
    s "I don’t know. Why do you seem like you’re one step away from murdering me and blaming it on uncontrollable love or something like that?"
    c "Silly, Sensei. I’ve been one step away from doing that for years now. And it’s currently exacerbated by the thought of you having this exact conversation with other girls! Probably!"
    s "Has Rin really been coming over like Chinami-"

    scene chikamaidsex8
    with dissolve

    c "Why are we talking about Rin?! She’s not here! I am! No mentioning other girls! Just get your fucking cock out and push me down already! I don’t want to think tonight! I just want sex!"

    play sound "zipper.mp3"
    scene chikamaidsex9
    with dissolve

    s "Okay, well that’s a sound argument if I’ve ever heard one. Let’s do this."
    c "Also, we only have like two hours because I work tonight."
    s "What? Two hours? You expect me to have “all of the sex” in two hours? I might be great at this, but I’m not a {i}god,{/i} Chika."

    scene chikamaidsex10
    with dissolve

    c "Not {i}yet{/i} you’re not. But that’s only because I haven’t broken out the secret weapon yet."

    play sound "static.mp3"
    scene chikamaidsex11 with flash
    stop sound

    c "Wait right there and you shall ascend!"

    play sound "static.mp3"
    scene chikamaidsex12 with flash
    stop sound

    c "{i}I’ll be right back!{/i}"

    "Chika sprints off to the bathroom and I’m left to wonder if there was some sort of trigger for this or if she just broke again after being neglected for too long. That happens sometimes. "
    "And it’s a level of slightly high maintenance that I was mostly okay with in the beginning, but it’s gotten obviously worse now that she knows I’ve never been as faithful as she wants."
    "I {i}am{/i} still in love with her, though. In my own makeshift way. So I {i}do{/i} want her to be happy."
    "I just...haven’t really figured out a strategy for tackling that with her yet since she’s taking my forced polyamory a little harder than everyone else I’ve signed onto it."
    "Well, apart from her idol at least. But hey, that just means they have something in common now that she won’t believe until she sees with her own eyes."
    "And based on my track record, she very well might."

    play sound "static.mp3"
    scene chikamaidsex13 with flash
    stop sound

    c "Ta-dah! Chika-chan is ready to serve you, Master! And as her number one customer, there is nothing, and I repeat {i}NOTHING{/i} that she will not do to make you happy!"
    s "Oh god, you’re not gonna make me pay for this are you? Because I definitely would. "

    scene chikamaidsex14
    with dissolve

    c "I can tell. I thought you were reaching into your pants to pull out your dick just now, but it turns out it’s just your wallet. "
    s "I have a weakness and it’s not fair that you would use it against me."

    scene chikamaidsex15
    with dissolve

    c "Oh, but it’s no weakness at {i}all,{/i} Master! It’s just a tactic to make you fuck me so hard that my brain goes blank! And yes, it’s 100%% free."
    c "Hell, I’d pay {i}you{/i} at this point! Just not a lot because I still have a sister to feed."
    s "Chika-"
    c "Okay, fine. You can take my entire savings. But {i}just{/i} this once, Master! And don’t tell any of my customers because I can’t afford to lose them."
    s "Chika-"

    scene chikamaidsex16
    with dissolve

    c "Fine! Tell them! Or better — fuck me in front of them! I don’t care! Just put it inside of me already!"
    s "I love you."

    play sound "static.mp3"
    scene chikamaidsex17 with flash
    stop sound

    c "Ah."
    s "Did that work?"

    scene chikamaidsex18
    with dissolve

    c "Sensei? What happened? And why am I so wet all of a sudden?"
    s "I think you were somehow put on horny auto-pilot. But it started to get scary, so I broke you out of it by telling you I love you."

    scene chikamaidsex19
    with dissolve

    c "Awwww! I love you too..."

    scene chikamaidsex20
    with dissolve

    c "Now, let’s go have sex in the kitchen! "

    play sound "static.mp3"
    scene chikamaidsex21 with flash
    stop sound

    s "{i}Hah...{/i}well, at least it worked for a few seconds. "
    c "Senseiiiiiiii~"

    scene chikamaidsex22 with fade

    c "I bought these just for youuuuu~"
    c "Now you don’t have to worry about taking them off and you can just fuck me whenever you want so long as I’m wearing a skirt. Which I always will from now on if you tell me to."
    s "Can I just interrupt the craziness for a second to tell you that you are infuriatingly hot sometimes?"
    c "Can you tell me with your cock instead of your mouth? Because that’s what I really want. "
    s "Nope. I’ll tell you with my mouth."

    scene chikamaidsex23
    with dissolve

    c "But that’s not what I-"

    scene chikamaidsex24
    with dissolve

    c "{i}Ah!~{/i}"

    scene chikamaidsex25
    with dissolve

    c "So th...{i}thaaaat’s{/i} what you meant..."
    s "This...is fine...right?"
    c "Uh-huh...you can...use your mouth like that...{i}whenever{/i} you want..."

    "As if the begging wasn’t enough to clue me in, I have now orally confirmed that Chika {i}is{/i} exponentially hornier than normal. Even by Chika-standards."
    "But the question now is {i}why?{/i} It’s just hard to ask that while my tongue is currently...{i}occupied,{/i} for lack of a better word."

    c "{i}Ahh...aaaah...fuck...{/i}"

    scene chikamaidsex26
    with dissolve

    c "These panties...are already worth the investment..."
    c "But I...aaah....I feel bad...Master..."
    c "Isn’t...Chika-chan...supposed to be the one taking care of...mnh...{i}you?{/i}"
    s "I think...Chika-chan...needs me a little more than...I need her right now..."
    c "Haaaah...w...wow....{i}wow...{/i}"
    c "How come you’re...so good at this...{i}Master?...{/i}I thought that...guys were supposed to be...bad at this...kinda thing..."
    c "Guess you’ve...got plenty of experience, though...with...aah...other girls...aaah....right?"
    s "Not...as much...as you’d think..."

    scene chikamaidsex27
    with dissolve

    c "Ah...aaahh....oh yeah?...Does that make me special then, Master?..."
    s "Of course...you’re special...I love you..."
    c "Say it again...{i}slower...{/i}and look up at me..."

    "I do as she says, locking eyes with her as my tongue traces circles around her clit. "

    s "I.....love......you......"

    scene chikamaidsex28
    with dissolve

    c "Oh my fucking god, yes...{i}yes...{/i}this is exactly what I needed..."
    c "Again! Say it...again...Master!"
    s "I love you...I love you..."

    scene chikamaidsex29
    with dissolve

    c "Mnnghhh! Yes! Right there! You’re gonna make me cum! Oh my god...oh my god! "
    c "{i}Bite it...{/i}just...make sure you...do it softly or I’ll-"

    scene chikamaidsex30
    with hpunch

    c "HYAAAAH! AAAAH! R...MASTER...SENSEI! AAAAH! YAAAAH! AAAAAH!"

    scene chikamaidsex31
    with dissolve2

    c "{i}Haaah....{/i}oh my god...that one was good..."
    c "You should...do this more often...I like you...down there..."
    s "You’re so wet that I’m convinced you’d like {i}anything{/i} right now."
    c "Well, what do you {i}expect{/i} to happen when you leave me alone so much now, Master? You need to take better care of me or I’ll go crazy..."
    c "You’ve seen it yourself, haven’t you? Like, I’m clearly not {i}all{/i} there. And the only way to fix me is to-"

    scene chikamaidsex32
    with hpunch

    c "AAAH! W-WAIT! NO! I W...WASN’T DONE...SP...TALKING! NOT...AAAH....M...MASTER?! A....AGAIN?! R...REALLY?!"
    s "You said you wanted all of the sex...and I’m going to give you all of the sex..."
    c "AAAH! AAAH! I KNEW THIS OUTFIT...WOULD DO THINGS TO YOU! BUT I THINK IT’S...DOING THINGS TO ME TOO! HYAAAH! FUCK! ALREADY?! HOW CAN I BE-"

    scene chikamaidsex30 with hpunch

    c "YAAAH! AAAH! AAAAAAH! FF....FUUUUUCK! AAAAAAAHHHH!"

    scene black
    with dissolve2

    "I bite down once more, forcing another orgasm out of her before she slumps back against the wall out of breath."

    scene chikamaidsex33
    with dissolve2

    "Of course I never intended to just do {i}that{/i} all night, though. And I quickly seize an opportunity to flip her over and claim her from behind."

    c "MNNNGGHHH! YES, MASTER! USE ME! FUCK ME! TREAT ME LIKE YOUR OWN PERSONAL SERVANT! THIS IS...EXACTLY WHAT CHIKA-CHAN NEEDS!"
    s "You poor thing...I can’t believe I’ve...neglected you for so long!"
    c "NGH! NGH! YOU {i}HAVE!{/i} I’VE BEEN...SO LONELY, MASTER! YOU USED TO...FUCK ME EVERY DAY! YOU CAN’T JUST...{i}STOP!{/i} I DON’T HAVE...ANYBODY ELSE LIKE...YOU DO!"
    s "And you don’t want anybody else...do you, Chika-chan? Say it...tell me I’m the only-"

    scene chikamaidsex34
    with dissolve

    c "MNNNNGGHGHHHH DEFINITELY NOT! OBVIOUSLY NOT! {i}YOU’RE{/i} THE ONE I WANT! ANYTHING ELSE IS JUST...FANTASY!"
    s "Oh? Want to tell me about the apparent {i}fantasies,{/i} Chika-chan?"
    c "THAT...AAAH...JUST A...FIGURE OF SPEECH! I THINK! HARDER! DEEPER! MORE, MORE, MORE! FUCK ME!"

    scene chikamaidsex35
    with dissolve
    play sound "dosex.mp3"

    s "You mean like...this?! Is {i}this{/i} what you want, Chika?! "
    c "AAH! AAAH! YES! M...MASTER! HARDER! HARDER! AAAH! AAAAH! HAAAAARD....ER!"

    "In a desperate effort to stabilize herself, Chika frantically latches onto the faucet, dousing one of her sleeves in water as I proceed to pound her further and further into the sink."
    "I can feel her tightening around my cock, likely cumming again as I take years worth of maid-based lust out on her body. "

    c "AAAaaAAAhhh! AaaAAAAAaaahhh! YeEEEEeeeeEEESSS! MY MIND.......GOING BLANK!"
    c "M....MORE....MORE! GIVE ME...MOOOOOOORRREEEE! MASTER!!!!!! MAS....TEEEEER!"

    "I pull her hair until her neck twists back. I slap her ass until it’s bright red. I grip her breasts with so much force that I can see the indentations my fingers leave on them."
    "And {i}none{/i} of it so much as makes her flinch."
    "This girl has a gift, really. And I’m eternally thankful that she’d just re-gift it all to me."

    c "AAAAH!! AAAAH! AAAAAH! AAAAAAHHH! MAS....TER! MAS....TER!!! HARDER.....HARDER!!!! "

    if tsukasacurious == True and chinamirefused == False:
        $ renpy.end_replay()
        $ chikaspring8 = True
        $ chika_lust += 1

        jump tsukasaspring5

    else:
        scene black
        with dissolve2

        c "HARDER!!!!!!!!!!!!!"

        "This would normally be the part where Chika thrusts back against me with so much force that she nearly knocks me over."
        "But the way I’m handling her tonight prevents that from happening."
        "In fact, the way I’m handling her tonight prevents her from really doing {i}anything{/i} at all."
        "She wants me to use her...so that’s exactly what I plan on doing until one of us collapses."
        "Or...at least until she has to go to work."

        stop music fadeout 7.0

        "{i}Neither of you collapse and Chika winds up going to work with your seed still lingering inside of her.{/i}"
        "{i}It somehow makes her service better.{/i}"

        $ renpy.end_replay()
        $ chikaspring8 = True
        $ tsukasaspring5miss = True
        $ tsukasaspring6miss = True
        $ chinamispring5miss = True
        $ chinamispring6miss = True
        $ tsubasaspring4miss = True
        $ tsubasaspring5miss = True
        $ chika_lust += 1

        "{i}Chika’s lust has increased to [chika_lust]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4
