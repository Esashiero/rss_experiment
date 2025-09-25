label kirinarchery:
    if chapthreeactive == True:
        jump kirinsummer2archerygen

label callkirinmorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if chap4active == True:
        "I tap on Kirin's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callmorning
    if chapthreeactive == False:
        "Kirin should be at the soccer field right now. I can probably go there if I want to see her."
        jump callmorning
    else:
        "Kirin should be at the archery range right now. I can probably go there if I want to see her."
        jump callmorning

label callkirinafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if chap4active == True:
        jump kirinspringnoongen
    if kirinbeachhj == True:
        "What do I want to do?"
        menu:
            "Hang out" if chap4active == False:
                jump kirinafternoonhang
            "Hang out" if chap4active == True:
                play sound "phonebeep.wav"

                "I tap on Kirin's name in my phone and wait for her to answer."
                "........."
                "......"
                "..."
                "There's no answer. I guess she's busy right now."
                jump callafternoon
            "Handjob (Raise Lust)" if bonus == True:
                jump kirinhjrep
            "Hug Kirin for Some Reason (Raise Lust)" if bonus == False:
                jump kirinhjrep
    elif chapthreeactive == True and chap4active == False:
        jump kirinafternoonhang
    elif chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Kirin's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callafternoon
    else:
        jump kirinafternoonhang

label kirinafternoonhang:
    if kirin_love >= 0 and kirindate1 == False:
        jump kirindate1
    if kirin_love >= 10 and kirindate5 == True and kirindate10 == False:
        jump kirindate10
    if chapthreeactive == True:
        jump kirinsummer2noongen
    if christmas7 == True:
        jump kirinnoongen2
    else:
        jump kiringenafternoon

label callkirinnight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if kirindate1 == False:
        play sound "phonebeep.wav"

        "I tap on Kirin's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        ki "Hihi~ How can I help you, Sensei?"
        s "Hey, Kirin. I was wondering if you'd want to meet up tonight?"
        ki "Tonight? You should have told me sooner. I already made plans with some friends."
        s "Damn. And you can't get out of them?"
        ki "Sensei, are you really asking me to bail on everyone {i}just{/i} so I can hang out with you?"
        s "Yes. Yes, I am."
        ki "Hmm...Well, I {i}do{/i} like you...But I don't know if I like you {i}that{/i} much."
        ki "How about you just call me a little earlier next time and I'll drop everything so we can hang? Cool?"
        s "Yeah, that's fine. Have fun with your friends tonight."
        ki "I will certainly try~"

        play sound "phonebeep.wav"

        "Looks like Kirin is busy tonight. I guess I'll have to call someone else."
        jump callnight
    if kirin_love >= 5 and kirindate1 == True and beachvacation16 == True and kirindate5 == False:
        jump kirindate5
    if kirin_love >= 25 and kirindorm20 == True and kirinlust5 == True and kirindate25 == False:
        jump kirindate25
    if chap4active == True:
        jump kirinspringnightgen
    if chapthreeactive == True:
        jump kirinsummer2nightgen
    if christmas7 == True:
        jump kirinnightgen2
    else:
        jump kiringennight

label kirinnightgen2:
    scene kirinnightgen2
    with dissolve
    play music "thesleepingcity.mp3"

    "Kirin and I decide to spend the night walking around the city district, looking for various ways to kill time."
    "She drags me around to a few of her favorite hang-out spots and is surprisingly clingy the entire time, refusing to let go of my arm even when I tell her to."
    "It's almost like she wants to be seen like this."
    "Eventually, we run out of places to visit and decide to simply sit with our backs against the wall of some old building, talking about life and what we think comes next."
    "We decide that the answer is nothing and that death will just bring eternal darkness."

    scene black
    with dissolve

    "It's a good night."
    "One I don't think I'd be able to have with anyone but her."
    "And even though our words and theories are as dark as the night sky, I can't help but feel like the two of us have managed to bond."
    "Albeit in a very strange sort of way."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirinnoongen2:
    scene kirinnoongen2
    with dissolve
    play music "normalday.mp3"

    "Kirin immediately invites me over after I give her a call to see what she's up to."
    "I don't find out until I get there that she bailed on going to some get-together with the soccer team to see me...and I can't tell exactly how that makes me feel right off the bat."
    "On one hand, a cute girl wants to spend time with me and prioritized me over a bunch of people she's known for much longer. Awesome."
    "But, on the other hand, it confuses me a bit as to why she's so readily let those people down in exchange for something she didn't even know was happening until half an hour ago."
    "The two of us aren't exactly close."
    "Sure, I like being around her, but virtually everything she does confuses the fuck out of me."
    "And it's not like she's the kind of person who will tell me what it all means either so I guess I'll just..."
    "Keep waiting to see what happens."

    scene black
    with dissolve

    "The two of us spend the afternoon on her couch."
    "We start off on different sides, but she slowly moves her way over to me and rests her head on my shoulder."
    "It's not often that she does cute things like that, so I take in the moment and hope that whatever caused her to do it today was more than just {i}being bored{/i} or whatever she always says."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label soccerfieldkirin:
    if kirin_lust >= 5 and christmas7 == True and kirinlust5 == False:
        jump kirinlust5
    if kirin_love >= 15 and kirindorm10 == True and kirinsoccer15 == False:
        jump kirinsoccer15
    if kirin_love >= 20 and kirinsoccer15 == True and kirinsoccer20 == False:
        jump kirinsoccer20
    if kirin_love >= 25 and kirindorm25 == True and kirinsoccer25 == False:
        jump kirinsoccer25
    if christmas7 == True:
        jump kirinsoccergen2
    else:
        jump kirinsoccergen

label kirininvite:
    if kirininvite1 == False:
        jump kirininvite1
    if kirininvite1 == True and kirininvite2 == False:
        jump kirininvite2
    else:
        jump kirininvitegen

label kirininviteaff:
    scene kirininvitegen
    with fade

    "Kirin and I spend the night inside of my room, gorging ourselves on fast food and talking about whatever things cross our minds."
    "And when I say {i}our{/i} minds, I really just mean hers."
    "She can be really talkative when there's no one else around."
    "And the level of comfort she's been showing with me lately is far surpassing anything I ever expected to get out of her."
    "Sure, there's still plenty that I don't know about her-"
    "But each hour we spend inside of this room, with me dodging french fries that she tries to force-feed me, somehow brings us closer together."
    "There's a certain beauty to moments filled with nothingness like these."
    "And that beauty seems to be amplified when those taking part are overflowing with the complete opposite- packed to the brim with those horrible things called {i}feelings{/i}."
    "It's everything and nothing all at once."
    "Everything and nothing and french fries."
    "Oh, how simple life can be at times."

    scene black
    with dissolve

    "We finish eating and spend the next couple hours playing some trivia game Kirin made me install on my phone."
    "She absolutely demolishes me because, apparently, trivia happens to be something that she's really good at for some reason."
    "I have no idea how she developed this skillset and even less of an idea of why she is trying to hone it alongside me, but at least she's having fun."
    "And if getting demolished is able to make her smile, I suppose I'm fine with it every now and then."
    "This girl could use more smiles."
    "For all I know, they might even renew her warped perspective of everyone and everything."
    "Or everything and nothing."

    $ kirin_love += 3
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love]!{/i}"

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

label kirininvitegen:
    play sound "phonebeep.wav"

    "I tap on Kirin's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    ki "Hihi~"
    ki "How's it going, [kirinmaster]?"
    s "Hey. Are you free right now?"
    ki "Mmm...depends. How much do you miss me?"
    s "The...normal amount?"
    ki "You're gonna have to give me a little more than that if you want to see me right now."
    ki "I'm on my way to meet up with people."
    s "Fine. I miss you more than the normal amount."
    ki "...You're really bad at this."
    ki "But yeah, I {i}can{/i} be free I guess."
    ki "Is this an invite to your place?"
    s "It is. I'm heading there now."
    ki "Kay~ Need me to bring anything?"
    s "Yeah, ask your sister if she wants to-"
    ki "Hanging up now~"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene kirininvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    ki "Why, hello there~"
    ki "What can I do for you today, [kirinmaster]?"

    "How should I spend my time with Kirin?"
    menu kirininvmenu:
        "Hang Out (Raise Affection)":
            jump kirininviteaff
        "Cowgirl (Raise Lust)" if christmaskirin2 == True:
            jump kirininvitecow
        "Blowjob (Raise Lust)" if bonus == True:
            jump kirinbj
        "Lying Doggystyle (Raise Lust)" if kirindate25 == True and bonus == True:
            jump kirinlay
        "Headpat" if bonus == True:
            jump kirinheadpat

label kirinbj:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump kirinbjx
    else:
        $ kirin_lust += 3
        stop music fadeout 5.0

        "{i}Kirin's lust has increased to [kirin_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label kirinlay:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump kirinlayx
    else:
        $ kirin_lust += 3
        stop music fadeout 5.0

        "{i}Kirin's lust has increased to [kirin_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label kirinsoccergen2:
    scene kirinsoccergen2
    with dissolve
    play music "highspeedprinter.mp3"

    "I make my way to the gym for soccer practice to find Kirin sitting up on top of the stage instead of practicing with the rest of the girls."
    "She says something about how she hurt her ankle and is taking the day off, but she looks fine to me."
    "I'm okay with it as it gives me someone to talk to. I mean, I'd be okay with it either way. I am a horrible representative for this soccer team."
    "Regardless, I hop onto the stage and sit next to Kirin."
    "She initially tries starting a conversation with me but starts getting snippy once she realizes my eyes have been-"

    if bonus == True:
        "Well, let's just say my eyes have been basically bouncing back and forth between every girl on the team. I am only a man, after all."
    else:
        "Well, let's just say my eyes have been focused on how high the ceiling is in here."
        "It's such a big gym."

    scene black
    with dissolve

    if bonus == True:
        "She gets over it quickly and, to my surprise, even starts judging the girls along with me."
        "Apparently, Kirin is a bit of a thigh connoisseur herself, so she's full of input and the two of us even come up with a rating system."
        "It's a good rating system, too."
        "But, it's immediately dismantled once I give her sister a perfect score."
        "She did not like that very much."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love] even though you gave Karin's thighs a 10/10{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kirinsoccergen:
    scene kirinmorninggen
    with dissolve
    play music "highspeedprinter.mp3"

    "I decide that there's no better way to spend the morning than by visiting a mischievous girl who I can't quite understand."
    "And while that might seem like a strange way to start the day, it's actually kind of nice."
    "Kirin's extremely...unreserved way of speaking is a nice change of pace and almost even exciting by some standards."
    "The two of us sit on the sidelines and watch the rest of the girls practice as she points out and tells me secrets about each one."
    "At first, I think it's a little strange that she knows so much, but I ultimately chalk it up to her just being on good terms with everyone."

    scene black
    with dissolve

    "Miku and Karin eventually catch on to the fact that Kirin is trying to slack off and they forcibly drag her on to the field to practice."
    "I'm a little surprised to see that she's actually quite good at soccer when she tries to be."
    "It just seems like she never really {i}wants{/i} to try in the first place..."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kiringenafternoon:
    scene kiringenafternoon
    with dissolve
    play music "normalday.mp3"

    "I wind up going over to Kirin's place after she tells me that her parents aren't around."
    "I think it's a little odd that she keeps calling me over here in the middle of the day rather than wanting to actually go anywhere, but I guess that's just the kind of person she is."
    "I don't have a problem with it. Being here just means it'll be harder for anyone to actually see us together."
    "It's not like I'd be able to fall back on the 'she's just my student' excuse with her either. If anyone from class saw us, I'm sure they'd have several questions."
    "But either way, I enjoy the time I get to spend with her...Even if I can't ever quite understand what she's feeling."

    scene black
    with dissolve

    "I notice that my phone is about to die as it starts to get dark and decide to head back home for a little while to charge it."
    "Kirin asks if she can tag along but, not knowing if Ami will be there or not, I decide against it."
    "She gets surprisingly frustrated when I tell her this and proceeds to be dismissive for the entirety of our very-brief goodbye."
    "But even with that in mind, I feel like the two of us have grown somewhat closer..."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label kiringennight:
    scene kiringennight
    with dissolve
    play music "thesleepingcity.mp3"

    "Kirin and I decide to spend the night walking around the city district, looking for various ways to kill time."
    "She drags me around to a few of her favorite hang-out spots and is surprisingly clingy the entire time, refusing to let go of my arm even when I tell her to."
    "It's almost like she wants to be seen like this."
    "Eventually, we run out of places to visit and decide to simply sit with our backs against the wall of some old building, talking about life and what we think comes next."
    "We decide that the answer is nothing and that death will just bring eternal darkness."

    scene black
    with dissolve

    "It's a good night."
    "One I don't think I'd be able to have with anyone but her."
    "And even though our words and theories are as dark as the night sky, I can't help but feel like the two of us have managed to bond."
    "Albeit in a very strange sort of way."

    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin's affection has increased to [kirin_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirindate1:
    "I guess I’ll give Kirin a call."
    "I’ve sort of been sitting on her number ever since she gave it to me, and she seems...normal enough to hang out with."
    "Okay, well, maybe 'normal' isn’t the right word."
    "If anything, she’s actually kind of abnormal. "
    "But it’s the good kind of abnormal."

    if bonus == True:
        "The kind that makes me feel like she’ll be down to sleep with me after hanging out a few times."
        "And it’s not wrong for me to say that, either, since this was basically her idea."
        "I’m just a totally normal teacher who can’t help but do whatever’s possible to make his students happy."
        "And, uhh, other students, I guess. Because Kirin isn’t really my responsibility."
    else:
        "Like she's actually an evil spirit or something."
        "Wait, no. That's paranormal. Silly me."

    "What am I even talking about right now? I should just call her before she winds up doing something else."

    play sound "phonebeep.wav"

    "I press on Kirin’s name in my contact menu and wait for her to pick up."
    "..."

    play sound "phonebeep.wav"

    ki "Hihi~ Whatcha up to, Sensei? Bored on your day off?"
    s "I guess so. Just looking for something to do."
    ki "Cool, cool. "
    ki "Wanna come over?"

    "Woah. Already?"

    if bonus == True:
        s "Really? Your parents aren’t home?"
    else:
        s "Can I have chocolate milk if I do?"
        ki "Uhhhhh...sure?"
        s "Did your parents and or roommates specifically say it was okay for me to drink their chocolate milk? Because I need to know for sure before I make any plans."

    ki "Nope! They’re not here much anyway."
    s "And your sister?"
    ki "Mmm...I think she’s out with Miku? I can’t really remember."
    s "And she’s not planning on coming back any time soon?"
    ki "What’s with all the questions? Do you wanna come over or not?"
    s "Sure. Where do you live?"
    ki "Do you know where Pepper-Lunch is?"
    s "Pepper what?"

    stop music fadeout 10.0

    ki "Some old restaurant that’s popular with people your age. I used to work there ‘til I got
    fired for some stupid stuff."

    s "Getting fired at your age probably isn’t going to look good on future applications."
    ki "Ehh, it’s whatever. That job was super boring anyway."
    ki "Just look up the address of that place and meet me there in like...half an hour. Kay?"
    ki "I’ll walk you to my house and stuff."
    s "Sure thing. See you then."
    ki "Byeeee~"

    play sound "phonebeep.wav"

    "..."
    "After hanging up, I punch in the address to Pepper-Lunch in my phone and begin to make my way there..."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    play music "justbehappy.mp3" fadein 7.0
    scene kirinfirstdate1
    with dissolve

    "I show up in front of the restaurant to find Kirin already waiting there."
    "I feel slightly bad for making her stand around and wait for me to show up, but then I
    remember she doesn’t live far from here and immediately get over it."
    "She’s probably only been here for a few minutes anyway."

    scene kirinfirstdate2
    with fade

    "Kirin pulls herself off of the wall and skips over to me as I approach her. "

    ki "Hey! Find the place okay?"
    s "It was easy enough."

    if day89 == True:
        s "I’ve been around here before, so I more or less knew where I was going."

    else:
        s "Maybe a little confusing at first, but once I figured out the streets were numbered it was fine."

    ki "Well I’m glad you made it. I felt like I was gonna die if I had to sit around the stupid house all day."
    s "Do you...not have any friends or something?"

    scene kirinfirstdate3
    with dissolve

    ki "Of course I have friends...What is that supposed to mean?"
    s "I don’t know. I just figured that if you did, you’d be hanging out with them instead of, you know, a teacher."

    scene kirinfirstdate4
    with dissolve

    ki "I was actually thinking about texting a few of ‘em, but then I saw your number show up and was like “ehh, screw it.”"
    ki "And now here we are, in front of the place that fired me for not showing up to one or two shifts."
    s "Not to take sides here, but I’m pretty sure that’s a good reason to fire someone."

    scene kirinfirstdate5
    with dissolve

    if bonus == True:
        ki "Right, right. Cause you know all about doing stuff that can get you fired, don’t you, Sensei?"
        s "Valid point, Kirin. And thank you for reminding me that you occasionally eavesdrop on what
        happens inside of my office."
        ki "Of course! You’re very welcome~"
    else:
        ki "Yeah. I learned from my mistakes and am attempting to become a better person."
        s "I'm very proud of you for being able to admit that, Kirin. That takes strength."

    scene kirinfirstdate6
    with dissolve

    ki "Are you, uhh, sure you’re ready to come over, though? I figured you’d be kinda hesitant after our talk in your office. "

    if bonus == True:
        s "Why would you think that? I literally agreed to help you ditch[school] in exchange for sex during that same conversation."

        scene kirinfirstdate7
        with dissolve

        ki "Well, yeah, but you didn’t seem as excited about it as I thought you’d be. I was kinda expecting you
        to like, push me down and just shove it in there or something."
        s "That's...kind of vulgar. I don't really think I'd go {i}that{/i} far."
        s "I’m obviously not the best when it comes to expressing emotions, but I can assure you I was very much excited."
        s "I especially liked the part where you showed me your underwear. That was cool and you should do it again."
    else:
        s "I know I didn't seem very enthused by the prospect of watching Seinfeld Season 3 back then, but I have thought more about it and am ready to give it a try."
        ki "Okay, but if you change your mind-"
        s "Just take me to your damn apartment, woman."

    scene kirinfirstdate5
    with dissolve

    ki "Bossing me around already? We’re not even alone yet, Sensei."
    s "So it’s okay to boss you around once we {i}are{/i}?"
    ki "Hehe~ Maybe not today. I’ve still gotta size you up and stuff."

    if bonus == True:
        s "..."
        s "Like, measure my penis?"
    else:
        s "Is there a height limit? Oh! Do you live on a rollercoaster?!"

    scene kirinfirstdate8
    with dissolve

    ki "What? No. It’s a phrase."
    ki "I meant like, I want to at least be alone with you for a little while and stuff to make sure you’re
    not like, a {i}total{/i} creep."
    s "Oh. I, uhh, think that might be a problem then. But I’ll do my best."

    scene kirinfirstdate6
    with dissolve

    ki "You don’t really have to do anything you normally wouldn’t. I mean like, we’ll be alone, so stuff might just happen naturally. "
    ki "That’s how this sort of thing goes, right?"

    if bonus == True:
        ki "A guy and a girl hang out alone. Hands wind up going where they’re not supposed to go. Blah blah blah, orgasms, so on and so forth."
        s "That...was a really weird sentence. But I think I know where you were going with it."
        s "It’s kind of weird to hear you talk like that, though."
        ki "Weird? Why? You barely even know me."

        "That’s...a good point."
        "I really don’t know Kirin at all. It’s just strange hearing girls her age without
        any sexual experience discussing orgasms so bluntly."
        "It’s like she’s another Ayane. And two Ayane’s in the same dimension sounds kind of intimidating."

        s "It’s just odd hearing stuff like that from someone other than Ayane."
    else:
        s "I just want to reiterate that I'm only here for chocolate milk."

    scene kirinfirstdate9
    with dissolve

    ki "Ohhhh. Is that so?..."
    s "..."
    s "Why do you look so pissed off now?"

    scene kirinfirstdate10
    with dissolve

    ki "I’m not pissed off."
    ki "Just...follow me."

    scene kirinfirstdate11
    with dissolve

    ki "I’ll show you where the apartment is..."

    scene black
    with dissolve
    stop music fadeout 10.0

    "Kirin’s anger(?) winds up fading away just moments later."
    "She begins to tell me about all of the different shops in the area- which ones
    have the best prices...which ones are open the latest."
    "From the sound of it, she’s lived in this same area her entire life."
    "I wonder what it is that turned her into who she is now?"
    "Or, at least, what she seems to be."
    "The whole thing about not knowing her is sticking in my head a lot more than I thought it would..."

    play sound "dooropen.mp3"
    scene kandahouse
    with dissolve

    ki "I’m home~"

    "Kirin calls out to absolutely no one and takes her shoes off, leaving them in the entryway."
    "She leads me into a relatively modern looking apartment teetering somewhere between upper middle
    class and high-end. "
    "I’d actually be rather impressed by the place if it wasn’t also the size of a large shoebox. "

    s "Does your entire family really live here?"
    ki "Hm? Yeah. What do you mean?"

    scene kirinfirstdate12
    with dissolve
    play music "love.mp3"

    "I join Kirin, who’s already taken a seat on the couch, and continue on with my train of thought."

    s "It just seems kind of small for four people. Do you and Karin share a room?"
    ki "Technically, yeah. I normally just sleep on the couch, though."
    s "You sleep on the couch in your own home?"
    ki "Yeah. Karin talks in her sleep sometimes and it gets really weird."
    s "She talks? About what?"

    scene kirinfirstdate13
    with dissolve

    ki "Sports stuff, I guess? Nothing interesting or sexy or anything like that."
    s "I see."

    scene kirinfirstdate14
    with dissolve

    ki "What? Boring answer? Did you think she might be saying stuff about you or something?"
    s "Not really, no. Was just hoping for something a little more entertaining."
    ki "Yeah. I can relate to that."
    ki "Life can get pretty boring sometimes, huh?"
    s "It’s not {i}that{/i} bad."
    ki "Says the guy with a harem of [high_school] girls."

    if bonus == True:
        s "Okay, so it’s not that bad {i}for me{/i}."
    else:
        s "Hey, I never wanted that. I just want to teach."

    s "What do you have to be bored of, though? Isn’t this like, the prime of your life?"

    scene kirinfirstdate15
    with dissolve

    ki "It’s supposed to be. I just feel like nothing ever happens around here anymore."
    ki "Yeah, the city’s closed off and stuff, but that’s not really what I’m talking about."
    ki "It’s like, everything I try doing I only do to be around other people. Nothing’s ever fun."

    if bonus == True:
        ki "And so a lot of the time I just wind up sitting at home reading or like, watching porn or whatever."
    else:
        ki "And so a lot of the time I just wind up sitting at home reading or like, donating money to charity or whatever."

    menu:
        "What kind of books do you like?":
            s "Interesting. You didn’t really strike me as a reader."

            scene kirinfirstdate16
            with dissolve

            ki "Is that an insult?"
            s "No, of course not. There’s nothing wrong with reading."
            ki "That’s not what your face says..."
            s "Well I can’t see my face, so I’m no help there...but what kind of books are you into?"

            scene kirinfirstdate15
            with dissolve

            ki "Hmm...Well, I don’t really read books. I guess just like, magazines or...whatever’s laying
            around the house."
            s "I see..."

        "Porn?!?!?! I LOVE porn!" if bonus == True:
            "I suddenly feel the urge to yell about my love for porn, but decide to suppress my desires and inquire normally."

            s "It’s not weird watching porn in the room with your sister?"

            scene kirinfirstdate17
            with dissolve

            ki "Well, she’s out all the time so it’s not like I’m never alone."
            ki "And I normally just use my phone anyway so I can hide under the blanket and..."
            s "..."
            s "Please go on."

            scene kirinfirstdate18
            with dissolve

            ki "..."
            ki "Naaaah. Not today..."

    "An awkward silence suddenly finds its way next to us on the couch, changing the air in the room for a brief moment in time."
    "I can’t tell if Kirin feels comfortable or uncomfortable. To me, she just seems weird."
    "Like she’s got some type of shell up that she’s trying to crack {i}and{/i} glue back together at the same time."

    ki "Hey."
    ki "Something’s been bugging me and I feel like I’m gonna get annoyed if I don’t ask you. Is that cool?"
    s "Sure. There aren’t many questions I have trouble answering. Sometimes, a window even pops up to help me choose."

    scene kirinfirstdate19
    with dissolve

    ki "A what now?"
    s "Nothing. Please just ask me your question."
    ki "Well, okay. But you have to be honest about it."
    s "Sure."
    ki "Okay, so, uhhh-"

    if bonus == True:
        jump kirinfirsthousex
    else:
        ki "How upset will you be if I tell you that one of my friends is actually borrowing my Seinfeld DVD right now?"

        stop music

        s "..."
        ki "You're really upset, aren't you?"
        s "Is that what you do to people, Kirin?"
        s "Invite people over just to cut them down?"
        ki "Not...normally?"
        s "So I'm special?? I'M THE ONE WHO GETS TO HURT?!"
        ki "..."

        scene black
        with dissolve

        s "I can't do this."
        ki "Wait. I have other DVDs. We can-"
        s "I'm going home to hug my accountant."
        s "Have fun dancing all by yourself."
        ki "Sigh. Looks like I'm donating to another charity..."

        play sound "seinfeld.mp3"
        $ renpy.pause(4, hard=True)

        $ renpy.end_replay()
        $ kirin_love += 1
        $ kirindate1 = True
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label kirindate5:
    play sound "phonebeep.wav"

    if ayanelust10 == True and bonus == True:
        "I tap on Kirin’s name in my phone with a slight bit of hesitation."
        "The two of us haven’t really had any...in-depth conversations since what transpired on the beach and, frankly, I’m not really sure what to make of it."
        "Don’t get me wrong, from a sheer sexual standpoint, I’m all about it."
        "That was one of the best things to happen to me since spawning in Kumon-mi."
        "But the effect it had on Ayane was not only surprising but a bit horrifying in a sense."
        "I’ve never seen her look that way before."
        "Kirin’s not just...planning on ignoring that, is she?"

    else:
        "I tap on Kirin’s name in my phone and wait for her to answer..."

    "........."
    "......"

    play sound "phonebeep.wav"

    ki "Hellooooo Sensei~"
    ki "You're calling 'cause you want to see me, right?"
    ki "Do you really miss me that much?"
    s "Yes. I miss you horribly."
    ki "Aww, you’re so cute."
    ki "Wanna come meet up somewhere?"
    ki "My parents are home right now but I can just lie and tell them I’m going out with friends or something."
    s "Am I not actually your friend?"
    ki "Hehehe~ I don’t know. What are you to me, Sensei?"
    s "..."
    ki "..."
    s "I’ll meet you around the corner from your apartment."
    ki "Kay kay! See you soon~"

    play sound "phonebeep.wav"

    "I hang up the phone and slide it back into my pocket."

    scene black
    with dissolve

    "What {i}am{/i} I to Kirin? Because obviously, 'friend' isn’t the right word."
    "At times, it almost feels like I’m being manipulated."
    "But hey, being manipulated isn’t always bad as long as the relationship is mutually beneficial."
    "Sometimes, it’s best to let yourself be manipulated in order to progress."
    "So, if that {i}is{/i} what she’s doing, she can carry on."
    "And I’ll carry on as well."
    "........."
    "......"

    play music "pianomelancholy3.mp3" fadein 10.0
    scene kirinnightdate1
    with dissolve

    "Kirin and I meet up under the cover of a nearby office building that we’ve visited once or twice before."
    "She’s a strange girl, but she’s smart when it comes to keeping things discreet."
    "It’s late enough that whatever office this is has already closed down. And since it’s not even facing the street, there isn’t really anyone who would ever see us here."
    "Well, unless there’s late-night cleaning staff or something along those lines."
    "But who really cares, right?"
    "We’re not doing anything wrong."
    "Yet."

    ki "No [niece] tonight?"
    s "No sister tonight?"
    ki "I asked you first~"
    s "You did. But I think the fact that I’m here is enough to prove that there is, in fact, no [niece] tonight."
    ki "Hmm, yes. Yes, I suppose it does."
    ki "Karin {i}is{/i} home tonight, so I guess I'm not completely devoid of a sister."
    ki "She’s having dinner with our parents, though."
    s "Shouldn’t you be joining them as well, then?"

    scene kirinnightdate2
    with dissolve

    ki "Shouldn’t you be joining your [niece]?"
    s "She’s a big girl. She’ll be fine eating on her own."

    "If she’s even cooking right now."
    "I didn’t bother to ask but it wouldn’t surprise me if she was."
    "Oh well. I guess there will be leftovers either way."

    ki "Ooooh, that means I’m a big girl, too. Doesn’t it?"
    ki "You know, since I’ll wind up eating by myself tonight after we finish doing...whatever it is we’re doing here."
    ki "Which is...what exactly? What {i}are{/i} we doing here?"
    s "Just hanging out like two normal people who definitely aren’t hiding from anyone else."
    ki "You really know how to woo a girl, don’t you?"

    if bonus == True:
        ki "Let's fuck, Sensei. Right up against the vending machine."
    else:
        ki "Hug me up against the vending machine, but don't press your body too closely against mine or I'll get angry."

    s "No way. You have no idea where that thing’s been."

    scene kirinnightdate3
    with dissolve

    ki "It literally hasn’t moved in like seven years."
    s "Why have you been keeping tabs on an office vending machine for seven years?"

    scene kirinnightdate4
    with dissolve

    ki "Maybe I’m involved in a secret relationship with someone who works here?"
    s "Right. So you’ve been sneaking around and engaging in secret relationships with salarymen for seven years."

    scene kirinnightdate5
    with dissolve

    if bonus == True:
        ki "Obviously not. I’m a faithful, innocent virgin who’s promised you her chastity in exchange for whatever that one thing I asked for was."
        s "Delinquency, I believe."

        scene kirinnightdate2
        with dissolve

        ki "Right. Delinquency."
        ki "Maybe you should skip[school] with me one day and deflower me on my sister’s bed? "
        ki "That would be fun, right?"
        s "Wow, you really know how to woo a guy, don’t you?"
        ki "Ohhhh, using my lines against me now?"
        s "It appears that way."
    else:
        ki "Hey. His name is Tony and he is a nice guy."
        s "Tony can go suck an egg for all I care."
        ki "Are you saying you care about me, Sensei."
        s "Yes. But more than that, I {i}don't{/i} care about Tony."

    scene kirinnightdate6
    with dissolve

    ki "Fine by me."
    ki "I mean, the two of us aren’t really that different, are we?"
    ki "We’re both just in this to have a good time."

    if ayanelust10 == True and bonus == True:
        s "I know that’s the case for {i}me{/i}, but is that really how it is for you?"

        scene kirinnightdate2
        with dissolve

        ki "What, was holding your cock while you fucked Ayane’s slutty, rich-girl pussy not enough for you to realize that I maybe-sort-of like that kind of stuff?"
        ki "Are you trying to tell me that you would have just stood there and watched if you walked in on me with another guy?"
        s "Probably. Not really into that multiple males, one female sort of thing."

        scene kirinnightdate7
        with dissolve

        ki "You..."
        ki "You really wouldn’t care if some other guy fucked me?"
        s "It’s not really my place to care about that."

        scene kirinnightdate8
        with dissolve

        ki "Well it fucking should be!"
        ki "I promised you my virginity, remember?!"
        ki "I obviously want you to fucking care about things like that!"
        ki "Is it so much to ask to just be looked at the same way as everyone else?"
        s "It’s just, that mentality contradicts your whole “Life is all about having fun” outlook."
        ki "So what, I need to back up every single outlook I have with logic and reason now? I can’t just think stuff because that’s what I want to think?"

        scene kirinnightdate9
        with dissolve

        ki "Fucking annoying. "
        ki "Just leave. I’m not in the mood to hang out anymore."
        s "..."
        ki "..."
        s "Well, if that’s what you want-"

        scene kirinnightdate8
        with dissolve

        ki "See?! This! This is what I hate!"
        ki "Of course I don’t want you to leave! I just..."
        s "...You just what?"

        scene kirinnightdate10
        with dissolve

        ki "I don’t know. "
        ki "People normally freak out when I start yelling at them."
        ki "No one really sits there and just...lets it happen. This is new for me."
        ki "Lots of new things are happening to me all of a sudden."
        ki "It’s...weird."
        s "If it’s any consolation, a lot of new things are happening to me too."
        s "Like that whole walking in on Ayane and me thing. That was new."

        scene kirinnightdate11
        with dissolve

        ki "But it was fun, right?"
        ki "Looked like you felt really, {i}really{/i} good."
        s "It was pretty amazing, I won’t lie."
        s "But I don’t think Ayane felt the same way."
        ki "You sure about that? "
        ki "Maybe it was just biological or whatever but she was literally dripping all over my hand."

        scene kirinnightdate12
        with dissolve

        ki "I mean...it’s only natural for her to be so turned on when she has a cock as big as yours inside of her."
        ki "I was the same way just from watching."
        ki "But, of course, you wouldn’t know that because you didn’t actually do anything to me."
        s "Sorry. I was too busy dealing with the psychological trauma you inflicted on my [niece]’s best friend."
        ki "Nuh-uh. You were busy filling her with your cum. Liar."
        ki "Besides, do you really think she’s traumatized from a little thing like that?"
        ki "Girls have threesomes all the time. It’s totally normal."
        s "Yeah but normally the third person is invited."
        ki "I took the fact that you both ignored my existence as you stormed through the door as an invitation."
        ki "Next time, tell me you don’t want me there if you don’t want me there."
        s "Why don’t {i}you{/i} tell me what you were doing in my room all by yourself?"
        s "That’s what I want to know."

        scene kirinnightdate13
        with dissolve

        ki "Do you?"
        ki "Well that just sucks, doesn't it?"
        s "Why? What do you mean?"
        ki "Because I don’t have to tell you shit."
        ki "You’re not my boyfriend. You’re just the guy I’ve chosen to take my virginity."
        ki "So sorry if you weren’t entirely satisfied with having two adorable girls service your monster-cock while everyone else played fucking beach-volleyball or whatever."
        ki "I’ll make sure to submit my next threesome application with your secretary."
        s "I just want to know why you do the things you do. That’s all."
        ki "Of course you do. Because I’m weird, right?"
        ki "Because I’m one of those diaries that come with the built-in lock thingy. "
        ki "And all you’re able to do is fit the tips of your fingers in through the tiny, {i}tight{/i}, little cracks and rip out one page at a time instead of reading the whole thing."
        ki "But without the key, you’ll never know what any of it really means. Right?"
        ki "Do you want my key, Sensei?"
        ki "Do you want to look into my diary?"

        scene kirinnightdate14
        with dissolve

        ki "Or do you just want to fuck my tiny, {i}tight{/i}, little pussy?"

        "I can’t tell if I’m intimidated or aroused right now."
        "So yeah, it’s basically a normal night with Kirin. Albeit a significantly less reserved one. "
        "Which is not to say that she’s ever reserved in the first place (She’s not). But even this is more aggressive than normal."
        "She must really despise confrontation..."

        scene kirinnightdate15
        with dissolve

        ki "Hah...Of course you won’t answer that question. It’s too hard."
        ki "I’ll just answer it for you, kay?"
        ki "You want both."
        ki "You want to fuck me and “fix” me at the same time."
        ki "It’s what you want to do with everyone. "
        ki "But things don’t work that way."
        ki "You can only have one or the other."

        scene kirinnightdate14
        with dissolve

        ki "Do you plan on fixing {i}everyone{/i}, Sensei? Even the ones who don’t need it?"
        ki "Or do you just want to push your way inside all of us and see how our faces light up as you fill us with your cum?"
        s "Kirin..."

        scene kirinnightdate16
        with dissolve

        ki "I like fixing things too, you know."
        ki "I’m just not very good at it, I guess."
        ki "Friends will come to me with problems and I’ll give them the advice I think is best. I’ll tell them what I would do in their shoes."
        ki "But then they forget all about it if it’s not what they want to hear and just go ask other people until they finally get an answer they’re satisfied with."
        ki "Why bother asking anyone for help if you’re only looking for validation? Right?"

        scene kirinnightdate15
        with dissolve

        ki "Sorry. I’m rambling."
        ki "You’re all frozen and stuff so I figured I’d just take the lead while you daydream about my virginity."
        s "I’m not frozen, just confused."
        s "I still don’t understand what any of that has to do with Ayane."
        s "I really just want to know what compelled you to break someone else in exchange for your own satisfaction."

        scene kirinnightdate16
        with dissolve

        ki "I want you to think {i}long{/i} and {i}hard{/i} about that last sentence, Sensei."
        ki "Isn’t that one more thing that the two of us have in common?"
        ki "Breaking others for our own satisfaction?"
        ki "If you think you’re going to be able to do all of these things without any sort of consequences, you’re wrong."
        ki "You can't {i}fix{/i} anything. You can only break things."
        ki "So what’s the problem if I do the same every once in a while? It gets both of us off, doesn't it?"

        scene kirinnightdate6
        with dissolve

        ki "And hey! Maybe I’ll even be lucky enough to be the one you finish inside of next time."
        ki "That would be swell. It’s not like I’ve already offered myself to you or anything. "
        ki "And it’s not like I literally followed you behind a bathroom just to ask if I could jerk you off on the beach."
        ki "So just keep fucking other girls. It’s cool. I’ll be good."
        ki "I’ll wait my turn."

        scene kirinnightdate16
        with dissolve

        ki "Anyway, rant over I guess."
        ki "Sorry for the thing with Ayane. Hope she’s not as bummed out as you are about it."
        ki "My bad."
        s "I’m not {i}bummed out{/i}. I just wish you’d think about other people a little more."
        ki "I’ll start doing that the second you do."
        ki "Until then, let’s just keep having fun. Okay?"
        s "..."
        ki "..."

        "Kirin and I stand there staring at each other for what feels like hours."
        "But despite how hard I try to siphon some emotion out of those green eyes, I get nothing."
        "She’s just blank."
        "Wait."
        "No."
        "She’s not blank."
        "She’s pitch black."

    else:
        "Are we really, though?"
        "Something about the way Kirin acts still makes me unsure about that."

        if bonus == True:
            "Sometimes, it feels like a complete facade. And others, I feel like she wants me to just take everything she has by force. "

        "I don’t understand her at all."
        "Are the two of us really the same in her eyes?"

    scene kirinnightdate17
    with dissolve

    ki "Oh! Thanks for never asking for money for letting Karin and me crash in that inn, by the way."
    ki "She wouldn’t shut up about how kind it was for the entire ride home. I almost jumped out of the bus."
    s "To be fair, I didn’t really pay either. That was all Ayane."

    scene kirinnightdate18
    with dissolve

    ki "Of course it was. "
    ki "Fucking bubble-wrap queen of Kumon-mi."
    s "That’s an absolutely horrible nickname."
    ki "Blame her father’s absolutely horrible invention."
    ki "Still cool, though. Being that rich, I mean."
    ki "I don’t even know what my dad does."
    ki "Hell, this could be his office building and I wouldn’t even know it."
    s "Are you not on good terms with your parents or something?"

    scene kirinnightdate6
    with dissolve

    ki "Nothing like that. Our terms are fine. I just try not to get too involved, I guess."
    ki "Which might be why it always seems like I’m trying to get involved elsewhere."

    scene kirinnightdate4
    with dissolve

    if bonus == True:
        ki "Like inside of your pants~"
        s "Thank you, Kirin. For reminding me of your strangely high sex drive despite being a literal virgin."
        ki "Literal, yes. But I can assure you my mind is quite corrupt already."
        s "Oh I’m well aware of that. You talked about porn the first time I came over."
        ki "I’ll talk about it again right now if you want. "
        ki "Wanna compare browser histories? I think you’ll be surprised by some of my tastes."
        s "Honestly, I don’t think anything about you would surprise me at this point."
    else:
        s "Like at a zoo?"
        ki "{i}Exactly{/i} like that, Sensei."
        s "That is so interesting."

    scene kirinnightdate12
    with dissolve

    ki "Can I take that as you thinking I’m interesting?"

    if bonus == True:
        s "Interesting is an understatement."
        s "I’d be down to write a thesis paper with you as the subject if I actually cared anything about actual work."
        ki "That sounds boring. Let’s just make out instead."

        "As much as I'm enticed by the offer to stay here and make out with Kirin, I feel like I should probably be leaving right about now..."
        "It’s already late and I really don’t want to have to walk home in the pitch black."
        "Is that a selfish reason? Sure. But it’s not like Kirin should be out right now either."
        "Her sister and her parents are probably still eating and talking about their day and...other family stuff, I guess."
        "She has no place out here next to me."

        s "We can make out next time. I need to start heading back."

        scene kirinnightdate3
        with dissolve

        ki "Really?"
        ki "Even though I studied in preparation for you to stick your tongue down my throat?"
        s "You...studied how to make out?"
    else:
        s "Yes. Just make sure to study up on the needs and requirements for every single animal there. We don't want any of them getting hurt."
        s "Being a zookeeper is a tough job."

    scene kirinnightdate19
    with dissolve

    ki "Well, I obviously don’t want to suck at it..."
    s "That’s...kind of adorable."
    ki "I know it is. I’m an adorable girl. "
    ki "You should say that more."
    s "I will do my best to remember..."

    scene black
    with dissolve2

    "Kirin and I part ways with an extremely brief goodbye."
    "I watch her take her phone out of her pocket and start typing out a message or social media post the second we part ways."
    "I hope she isn’t writing anything about me."
    "I feel like tonight’s conversation could have gone a little better..."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirindate5 = True
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "{i}Sensei eats a hot dinner when he returns home!{/i}"
    "{i}Kirin does not!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirindate10:
    play sound "phonebeep.wav"

    "I tap on Kirin’s name in my phone and wait for her to answer."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene kirinmakeout1
    with dissolve
    play music "behindabathroom.mp3"

    "I wind up meeting Kirin at the Kanda apartment on account of all of the other...well, Kandas being out of the place."
    "Papa and Mama Kanda (Who I have yet to ever meet and hope I never will) are off at work while Karin is out doing soccer stuff with her friends or something along those lines."
    "Kirin wasn’t willing to provide many details over the phone."
    "It was just a lot of “I’m all alone. Come now,” mumbo-jumbo that, honestly, I’m more than okay with."
    "Good things happen when people get to be alone together."
    "I wonder what sort of good things will happen today?"

    ki "Hey, hey. Guess what?"
    s "What?"
    ki "We’re all alone~"
    s "I was actually just having a short inner-monologue about that."
    ki "Oh yeah? Say anything good to yourself? "
    ki "Anything fun?"
    s "Just that good things normally happen when two people are alone together."
    ki "Oooooh. I wonder what sort of good things will happen today?"
    s "That is literally how I ended the monologue."

    scene kirinmakeout2
    with dissolve

    ki "I know how your mind works. Mine is the same way."
    s "Sorry to break your heart but I still don’t think we’re connected that deeply."

    if bonus == True:
        ki "I know an easy way to change that~"
        s "You say that now, but I have a feeling you’re just going to back out again before anything happens."

        scene kirinmakeout3
        with dissolve

        ki "You really think that?"

        if kirinbeachhj == True:
            ki "I’ve literally let you cum on me before. Did that not earn me any points at all?"
            s "It earned you a few."
            ki "Well can I redeem them for a chance to get you to think I’m being serious right now?"
            s "I think you still need to earn a few more points for that type of reward."
            ki "I better start {i}grinding{/i} some then, huh?"
            s "I’m enticed by the way you said ‘grinding’ right there."

        else:
            s "Yeah. I’ve said it before and I’ll say it again."
            s "I have a hard time reading you."

            scene kirinmakeout1
            with dissolve

            ki "Well that’s a good thing, isn’t it? It makes me more exciting."
            s "It definitely makes you something."

    scene kirinmakeout1
    with dissolve

    ki "Hey, can I ask you a question?"
    s "Fine, yeah. Go ahead. It’s not like we’re doing anything el-"

    if bonus == True:
        jump kirindryx
    else:
        ki "If I ever catch a disease where my hair starts to turn into pasta, will you help me boil it so I can still do my twintails and stuff?"
        s "What?"
        ki "Yeah. Because pasta isn't that malleable when it's uncooked. And I'd feel weird about cooking a part of myself."
        ki "Also, how many ducks do you think there are?"
        s "Uhhhhhhhhhhhhhhhhhhhhhhhh..."
        ki "Have you ever worn a parachute before?"

        scene black
        with dissolve

        "I think Kirin may be having a psychotic episode, so I call an ambulance and wait with her until she is normal again."
        "She is very thankful and tries to hug me, but Karin shows up and the hug gets cancelled."
        "Maybe one day we will complete it."

        $ renpy.end_replay()
        $ kirin_love += 1
        $ kirindate10 = True
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label kirinhjrep:
    play sound "phonebeep.wav"

    "I tap on Kirin's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"
    play music "acoustic.mp3" fadein 10.0

    ki "Hihi~ Good afternoon, Sensei."
    ki "To what do I owe this pleasure?"

    if bonus == True:
        s "Help. I have an erection and don't know what to do about it."
    else:
        s "Help. I need a hug and I don't know what to do about it."

    ki "...Cool!"
    s "Want to hang out?"
    ki "Well, I mean...someone's gotta do something about it, don't they?"
    ki "I suppose I could free up some time for you in my {i}super busy{/i} schedule since you decided to ask {i}me{/i} for help."
    s "Thanks Kirin. You're a real life-saver."
    ki "Next time, you might wanna just text me, though."
    ki "What if I was with my family and had you on speakerphone?"

    if bonus == True:
        s "I highly recommend never putting me on speakerphone. Erections can strike at any minute."
        ki "Why do you need to verbally announce your erections? That's weird."
        ki "Just come over and I'll jerk you off or something."
    else:
        s "It is just a hug. We have nothing to hide."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump kirinhjrepx
    else:
        $ kirin_lust += 1
        stop music fadeout 5.0

        "{i}Kirin's lust has increased to [kirin_lust]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label kirinlust5:
    scene kirinfirstlust1
    with fade
    play music "highspeedprinter.mp3" fadein 5.0

    "I show up at the soccer field...well, soccer-{i}gym{/i} due to the poor weather, and make my way over to Kirin."

    ki "Ohoho~ Approaching me first out of everybody? To what do I owe the pleasure, Sensei?"
    ki "Also, before you tell me that it’s just because I was the first person you saw, allow me to inform you that that is absolutely not an acceptable answer."
    s "It’s not?"
    ki "Nope."
    s "Do you want me to tell you it’s because you’re the prettiest girl in the gym?"
    ki "That would be nice, yes. "
    s "You are the prettiest girl in the gym, Kirin."

    scene kirinfirstlust2
    with dissolve

    ki "Aww, that’s so sweet of you! "

    scene kirinfirstlust3
    with dissolve

    if bonus == True:
        ki "So, what’s up? You actually gonna do some coach-stuff today or are you just here to stare at all of our asses again?"
        s "I don’t exclusively stare at asses, Kirin. I am a man who appreciates the entire package."

        scene kirinfirstlust4
        with dissolve

        ki "More like a man trying to give out {i}the entire package.{/i}"
        s "Perhaps. Interested in buying-in?"
        ki "Is my name Kirin Kanda?"
        s "If it’s not, you’re even less trustworthy than I thought you were."

        scene kirinfirstlust5
        with dissolve

        ki "What do you mean? I’m plenty trustworthy."

        if ayanelust10 == True:
            ki "I never told anybody I caught you fucking Ayane during the beach trip, did I?"
            s "No, you just forced yourself in between us."
            ki "And I’d do it again, too. That was hot as fuck."
            s "I agree as long as you subtract the subsequent trauma. "
            ki "That’s the part that made it hot, though."
            s "Wait, what?"

        else:
            ki "To prove it, I’ll have you know that I still haven’t told a single soul about our little deal."
            s "You mean the one where you have sex with me in exchange for free absences?"
            ki "Yeah, that."
            s "Have you even missed[school] since then?"
            ki "Well...no."
            ki "But it’s still a deal we made and I could really mess things up for you if I recorded it or something."
            s "..."
            s "Please tell me that was a joke."
            ki "Why? I’m so untrustworthy that you wouldn’t believe me either way."

    scene kirinfirstlust6
    with dissolve

    mi "Morning, you two!"
    ki "Oh, Miku. What’s up?"
    ki "Karin told you my ankle is messed up, right?"

    scene kirinfirstlust7
    with dissolve

    mi "Sure did. No sense in worryin’ about practice today, Kirin. Just sit over here and talk to Sensei or somethin’."
    s "What happened to your ankle?"

    scene kirinfirstlust8
    with dissolve

    mi "Sensei! It doesn’t matter what happened! What matters is that she’s hurt!"
    mi "Ya have any idea what could happen to an athlete if they keep goin’ durin’ an injury? Nothin’ good, I’ll tell ya that much!"
    s "But she seems fine to-"
    ki "Listen to the captain, {i}Sensei{/i}."
    ki "If I say I’m hurt, I’m hurt. "
    mi "For real! The nerve of this guy!"

    "What is going on right now?"

    scene kirinfirstlust9
    with dissolve

    ki "You know, Miku, I heard that Sensei’s got some pretty great massage skills."
    ki "Would you mind if maybe he helped me out with my ankle or something? "
    ki "Karin and I cleaned the store-room this morning so there’s plenty of room for the two of us in there."
    ki "Of course, only if you’re okay with it, I mean."

    "Oh. Yeah, I probably should have figured something like that was going on."

    scene kirinfirstlust10
    with dissolve

    mi "I...uhh...well, ya see..."
    mi "There’s a chance Sensei might not be as...great as ya think he is...at that stuff..."

    if bonus == True:
        s "..."
        "She's not going to tell her about what happened in her dorm room, is she?"
    else:
        s "Wtf"

    mi "Two people bein’ alone in the store-room could cause all sorts of trouble..."
    ki "What? But you seemed all-for the idea in the summer. "
    ki "You kept talking about how great it would be for our muscles to get over soreness and blah blah blah soccer-talk."

    scene kirinfirstlust11
    with dissolve

    mi "Yeaaaaaah...I did say all that stuff...didn’t I?..."
    ki "..."
    mi "It’s just...Idunno...I thought more about it and it seems kinda inappropriate...if ya know what I mean."
    ki "Inappropriate? Surely you’re not accusing our dedicated and beloved coach of doing anything {i}weird{/i} with his students, are you?"

    scene kirinfirstlust12
    with dissolve

    mi "I have no idea what the heck I’m even sayin’ anymore."
    ki "Miku, Sensei is a responsible adult who’d {i}never{/i} even think of what you’re suggesting."

    if bonus == True:
        ki "And unless you have..."

        scene kirinfirstlust13
        with dissolve

        ki "Personal experience...to back that up..."
        mi "Huh? I couldn’t hear that last part. Yer gonna have to...speak up or somethin’..."
        ki "..."
        mi "..."

    scene kirinfirstlust14
    with hpunch

    mi "OKAY FINE! GO GET YOUR STUPID LEGS RUBBED!"
    mi "BUT NO FUNNY BUSINESS OR I’M CALLIN’ OFF PRACTICE FOR THE REST OF THE YEAR!"
    ki "Yeah...of course."
    ki "We’ll be in and out in no-time."
    mi "OKAYBYE!"

    scene kirinfirstlust15
    with dissolve

    "Miku quickly sprints away from Kirin and me and falls flat on her face after tripping over a traffic cone."
    "It might be the first time I’ve ever seen her lose her balance, so it’s a little jarring."
    "But not as jarring as the look I receive from Kirin shortly after."

    scene kirinfirstlust16
    with dissolve

    ki "That...was kinda weird..."

    if bonus == True:
        jump kirinfirstlustx
    else:
        s "Yeah. Miku's a fucking weirdo."

        scene black
        with dissolve2

        "Kirin leads me into the storage room where I prefer a completely platonic and not at all sensual massage on only the parts of her body that someone like me would be allowed to touch."
        "I receive express consent regardless because I am a good man and, within a matter of minutes, she's as good as new."

        ki "I'm as good as new."
        s "Hooray!"

        $ renpy.end_replay()
        $ kirinlust5 = True
        $ kirin_lust += 1
        stop music fadeout 5.0

        "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon

label kirininvite1:
    play sound "phonebeep.wav"

    "I tap on Kirin’s name in my phone and wait for her to answer."
    "Whenever the two of us hang out, it’s usually something along the lines of me going over to {i}her{/i} part of town and just...killing time however {i}she{/i} wants to that day."
    "But I feel like we’ve gotten close enough at this point that she’d be willing to hang out at my place instead."
    "Now, knowing Kirin, it’s highly possible that she’s been waiting for me to invite her over this entire time-"
    "But it’s not exactly easy finding an opportunity to bring over a girl from another class, and there’s no way Ami wouldn’t be suspicious of that if she caught it happening."
    "As such, today might be the only chance I have for a while to actually follow through with the idea, as her and some of the others are going shopping in the urban district of Kumon-mi."

    play sound "phonebeep.wav"

    ki "Hey~ Whatcha up to?"
    s "Heading back to my place. You?"
    ki "What a coincidence. I’m {i}also{/i} heading back to my place."
    s "Wow. Maybe this is some sort of sign?"
    ki "Maybe it is! Are you suggesting we hang out?"
    s "I suppose I might be. Do you have any objections to coming over my place this time?"
    ki "Uhh...where do you even live?"
    s "Do you know where Ayane lives?"
    ki "Yeah. You’re over there?"
    s "No. Nowhere near it, actually."
    ki "...Then why would you even bring that up?"
    s "I’ll just text you the address. You can make it in less than an hour coming from your apartment."
    ki "You’ve been traveling that far just to meet up with me this whole time?"
    s "Yeah. I’m so kind, aren’t I?"
    ki "That or you just really like walking."
    ki "Is Ami home right now? Or is this the same kind of secret meeting we have when you come over my place?"
    s "I would absolutely not invite you over if Ami was there."
    ki "Ouch."
    ki "But yeah, text me the address. I’ll head over now."
    ki "We’re ordering food, though. I’m starving."
    s "Deal."
    ki "Sweet. See you soon, [kirinmaster]~"

    play sound "phonebeep.wav"

    "The call comes to an end and I immediately send Kirin my address."
    "She doesn’t respond, but I guess there’s not really any reason to, considering a street name and some numbers aren’t a great start to a conversation."

    scene black
    with dissolve
    stop music fadeout 5.0

    "The walk back is a cold one. The wind is out in full force today."
    "I feel kind of bad for making Kirin bear this all the way over, but one of us was going to wind up suffering through it no matter what."
    "I’ll just make it up to her by buying her dinner whenever we decide on something to order."
    "........."
    "......"
    "..."

    scene kirinfirstinvite1
    with dissolve
    play music "normalday.mp3"

    ki "Thanks for having me~"

    "Kirin lets herself in once I give her the okay and slides her boots off at the door before gleefully trotting up to me."

    s "Your cheeks are bright red. You’re not nervous about being alone in my house, are you?"

    if bonus == True:
        ki "No. I’m just freezing cold since I walked all the way over here on the windiest day ever."
        ki "I basically had to hold my skirt down the entire way so it wouldn’t blow up and give everybody a peek at my underwear."
        ki "They're black, in case you were wondering."
    else:
        ki "No, I'm just cold."
        ki "Also, what the fuck is a canola and how do they get the oil out of it? Do you ever wonder that, Sensei?"

    "Jokes on you, Kirin. I'm {i}always{/i} wondering."

    if bonus == True:
        s "That’s basically the exact opposite of what you did when you came into my office for the first time."
        ki "Ooooh, I remember that. When I showed you my panties and you didn’t even get hard."
        s "I think I did. But it was a pretty confusing meeting and I don’t remember much of it other than that you owe me your virginity now."

        scene kirinfirstinvite2
        with dissolve

        ki "Oh, about that. "
        ki "Do you think there will be a lot of blood? I’m not really sure what to expect."
        s "Just look it up online. I don’t want to talk about the amount of blood that will come out of you."
        ki "I tried, but I keep getting different answers and I figured it would be better to ask you since you’ve definitely taken a few v-cards by now."
        s "You’re wasting no time in getting into the accusations today."

        scene kirinfirstinvite3
        with dissolve

        ki "Heheh~ I know you’ve stolen at least {i}one{/i}. But, for all I know, you could be screwing half of the soccer team by now."
        s "There’s no way I’d be able to do that without you finding out about it."
        ki "Yeah, I think it’s fair to assume that I’ll figure out pretty much everything you do sooner or later, so you should just be open and honest with me."
        ki "That’s more fun anyway, right?"
        s "In that case, let me start this “open and honest” meeting by saying you look very cute today."

        scene kirinfirstinvite4
        with dissolve

        ki "Thanks! But, just so you remember, I’m not blushing and my cheeks are only red from the cold."
        ki "I {i}know{/i} I look extra cute today, though, so I’m glad you’re being honest with me."
        ki "As repayment, I’ll say one honest thing to you as well."

        scene kirinfirstinvite5
        with dissolve

        ki "I’m lowkey really fucking nervous about losing my virginity today."
        ki "Like, I was fine with it when you called me. "
        ki "But the walk over here was so long that it gave me way too much time to think and now I can’t tell if my hands are shaking from the cold or from my nerves."
        s "..."
        s "Well, that’s significantly more open and honest than I was."

        scene kirinfirstinvite6
        with dissolve

        ki "Hahahaha...yeaaaaaah..."
        ki "Also, I didn’t have time to shave since I came directly from the convenience store and that’s making me self-conscious too."
        ki "So like, you can still totally do me some other time buuuuuut I’m kind of scared as fuck right now."
        ki "Just too much all at once, I guess."
    else:
        s "Well, if you need a warm blanket or a mug of hot cacao to warm yourself up, just let me know. My primary concern is making you feel safe and welcome."
        ki "Wait, no. Answer the canola question. It's important."
        s "I can't, Kirin. Knowing the truth would only make you too powerful."
        ki "Sensei-"
        s "Do you want the cacao or not?"
        ki "...Yes please."
        s "I will put the kettle on right away."

    scene kirinfirstinvite7
    with dissolve

    ki "But, uhh...now that {i}that’s{/i} out of the way, what did you want to eat for dinner?"
    ki "I was thinking we could just order from a bunch of different places and then split whatever the cost is."

    if bonus == True:
        s "That jump between subjects was incredibly jarring based on everything I just learned."
        ki "I was just repaying your honesty with my own honesty. Don’t think it was some huge breakthrough or anything."
        ki "The {i}real{/i} breakthrough will be when you tear through my hymen and cause an undisclosed amount of blood to come pouring out of me."
        s "..."
        ki "..."
        s "So, about dinner-"
    else:
        s "Absolutely not. Allow me to front the bill as both your teacher and closest friend."

    scene kirinfirstinvite8
    with dissolve

    ki "This is really awkward."
    s "It is, but I’m definitely not taking the blame for it this time."
    ki "I know. I’m clearly less prepared than I thought I’d be for something like this."
    s "..."
    ki "..."
    ki "So, dinner."
    s "Right, dinner."

    scene black
    with dissolve

    "Well, that was not exactly the start to this visit that I was expecting."
    "It was...nice seeing Kirin be honest about something that wasn’t entirely malicious or confusing for once, though."
    "It’s probably the first thing I’ve seen her do that I can actually say I understand."

    if bonus == True:
        "Opening up about your fears isn’t an easy thing to do, which is likely why she used my compliment as a crutch to piggyback off of."
        "Within minutes of arriving here, she felt threatened and took a defensive stance."
        "And, when you’re around someone like me, or whatever her vision of me is, there’s no harm in taking a few extra precautions."

    "..."
    "The two of us proceed to flip through a number of takeout menus that Ami and I keep on top of the microwave, ordering from a grand total of four of them."
    "I don’t take Kirin up on her offer to split the bill and decide to pay for everything myself, figuring I can keep any leftovers and just...eat them throughout the week."
    "And, within forty-five minutes or so, our feast is finally ready to begin."

    scene kirinfirstinvite9
    with dissolve

    ki "So, uhh...That was kind of weird before, right?"

    if bonus == True:
        ki "I mean, {i}me{/i} being the one to say all that stuff about getting nervous when I’ve done nothing but try and get into your pants since I met you."
        ki "What was that all about, right? Hahaha..."
    else:
        ki "I mean, like...what if {i}Canola{/i} is just the name of the brand?"

    s "You really don’t have to keep bringing this up, Kirin. We can just eat now."

    scene kirinfirstinvite10
    with dissolve

    ki "Ahhhhh I know that!"
    ki "I just feel so immature all of a sudden and I don’t like it."
    ki "Can’t you just come out and admit something equally embarrassing so I can get over this?"
    s "I...can’t really think of anything that embarrassing, to be honest."

    if bonus == True:
        ki "What, you never like, walked in on your parents having sex when you were little or something?"
        s "Not that I can remember."

        "I can’t even remember what my parents looked like..."

        ki "Nothing with your [niece], either?"
        ki "You guys live together so like...she’s probably caught you jerking it or something before, right?"
    else:
        ki "What, you never like, accidentally called your teacher Mom or anything?"

    s "Surprisingly, no."

    scene kirinfirstinvite11
    with dissolve

    ki "Jesus, how boring is your life?"

    if bonus == True:
        ki "How have you not done {i}anything{/i} embarrassing when there are over ten hormonal [teenager]s watching you at all times?"
        ki "Myself included."
        ki "Don’t think I’m quitting the game just because I got nervous and said some stuff I was thinking earlier."
        ki "I still want you to go to fucking town on me eventually."
        s "..."
        s "I’m glad to see you’re back to normal, Kirin."
    else:
        s "It's not boring. It's fulfilling, calm, and full of hugs. Just the way I want it."
        ki "Yeah, yeah...I get it. I'm just feeling a little off today."
        s "Well I hope that the cacao you drank offscreen helped."
        ki "It did."

    scene kirinfirstinvite12
    with dissolve

    ki "Yeah, I’m pretty sure I just needed sugar or something."
    ki "I’m feeling a lot better now and I’m literally like two inches away from you."

    scene kirinfirstinvite13
    with dissolve

    if bonus == True:
        ki "Do you want a blowjob after we’re done eating?"
    else:
        ki "Do you want a hug after we’re done eating?"
        s "Ah! Hug! I love hugs!"

    ki "That’s gotta be worth dinner and those five minutes of counseling I needed earlier, right?"
    s "Not if you’re going to make it sound like I’m extorting you."

    if kirinbeachhj == False and bonus == True:
        scene kirinfirstinvite14
        with dissolve

        ki "So...first you turn down my free handjob on the beach...and now you’re turning down my mouth?"
        ki "You really {i}are{/i} gay, aren’t you?"
        s "I’m not gay..."
        ki "Well then what’s the deal?"
        ki "Why are you pushing me away? What am I doing that’s so wrong?"
        ki "I just..."

    scene kirinfirstinvite15
    with dissolve

    ki "Hah..."
    ki "I don’t offer these things just to get you to like me, Sensei. "
    ki "I want to have fun with you and I want {i}you{/i} to {i}want{/i} to have fun with me."

    if bonus == False:
        s "How are we to have fun without any board games?"

    scene kirinfirstinvite16
    with dissolve

    ki "But I guess having you buy me dinner is enough fun for today."

    if bonus == True:
        ki "I’ll probably be too full afterward to suck you off anyway."
        ki "And you know what they say about giving blowjobs on a full stomach."
        s "I have no idea what they say about that."
        ki "Oh. Well, they probably say it’s bad or whatever."
        ki "I don’t know. I kind of just made that up hoping you wouldn't actually respond to it."
    else:
        ki "Besides, any second now, lock.mp3 is going to play and Ami is going to show up."

    play sound "lock.mp3"
    scene kirinfirstinvite17
    "Our conversation is suddenly interrupted by what may just be the last sound effect I ever hear."

    ki "What was that noise just now?"

    if bonus == False:
        s "lock.mp3"

    ki "You heard that, right?"
    s "Either Ami is home way ahead of schedule or I am about to be robbed."
    ki "Neither of those things are good for me."
    s "Which one of them do you think sounds good for {i}me{/i}?"
    ki "The Ami one, obviously."
    s "It would probably be safer getting robbed than having to deal with the fallout of her finding us together."
    ki "Jesus. What kind of relationship do you two have?"

    play sound "dooropen.mp3"

    a "I’m home!"
    s "I’m going to die."

    scene kirinfirstinvite18
    with dissolve

    ki "No...you’re not."
    ki "Do you have any idea how many times I’ve stealthily [masturbate]d in the same room as my sister, Sensei?"
    ki "I’ll show you how good I am at being undetected."
    ki "Watch."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene kirinfirstinvite19
    with dissolve

    a "..."
    s "..."
    ki "..."
    a "Umm..."
    a "What’s...going on here?"
    s "..."
    s "I was very hungry."

    scene kirinfirstinvite20
    with dissolve

    a "Don’t you think...this is a little much?"
    s "..."
    s "I thought Maya might be coming over when you got home."

    scene kirinfirstinvite21

    a "Oh, okay. Then yeah, that makes sense."
    s "Why are you back so early? I thought you were going shopping."

    scene kirinfirstinvite22
    with dissolve

    a "We were going to but...it was just way too cold and none of us wanted to wait at the bus stop."
    a "So we all just decided to head back."
    s "Cool, cool."
    a "Oh, Sensei. I saw a nice pair of boots at the door. Did you buy those for me?"

    scene kirinfirstinvite23
    with dissolve

    s "...Yes."
    ki "{i}For real? Those are my favorite boots.{/i}"
    a "Hm?"
    a "Did you hear something just now?"
    s "All I heard was the sound of my regret for not being able to wrap the boots I definitely bought you in time."
    a "Do you...want me to go into my room so you can wrap them now?"
    s "...Yes."

    scene black
    with dissolve2

    "Ami, bless her heart, is gullible enough to take the bait and disappears into her room for the next few minutes, giving Kirin enough time to flee the house."
    "Obviously, I didn’t make her walk home without her boots on, so now I just...need to figure out an excuse to give to Ami for why her “present” so suddenly vanished."
    "I don’t hear from Kirin again until she gets home- and even then, all I get are exhausted face emojis."
    "But, despite a rocky start, a rocky ending, and a...normal middle part (?) the evening isn’t a complete disaster."
    "It wasn’t ideal by any means, but I don’t think something like this will be enough to keep her away in the future..."

    $ renpy.end_replay()
    $ kirininvite1 = True
    $ kirin_love += 3
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirininvite2:
    play sound "phonebeep.wav"

    "I tap on Kirin’s name in my phone and wait for her to answer."
    "Our last meeting didn’t exactly go anywhere on account of Ami’s plans being cut short, but I’ve already confirmed that she will {i}definitely{/i} be gone this time around."
    "Unless...of course, she decides to cut things short again."
    "But that’s a chance I’m willing to take if it means getting some alone time with Kirin."

    if bonus == True:
        "Based on some of the things she said last time, there’s a high probability that she’ll, once again, be too nervous to try anything, but-"

    play sound "phonebeep.wav"

    if bonus == True:
        ki "Heya! Can I come give you a blowjob?"
        jump kirinfirstbjx
    else:
        ki "Heya! I'm in Mexico right now."
        s "What? But I thought we weren't allowed to leave Kumon-mi."
        ki "We can in the Patreon version."
        s "Oh. Well, uhh...have fun?"
        ki "Will do! Talk to ya later, Sensei!"

        play sound "phonebeep.wav"
        scene black
        with dissolve

        "I'm unable to hang out with Kirin because she went to Mexico =/"
        "I'll just print out a picture of her face and tape it to one of my pillows and hang out with that instead."

        $ renpy.end_replay()
        $ kirininvite2 = True
        $ kirin_lust += 3
        stop music fadeout 8.0

        "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
        "{i}You can now invite her over to the house on nights and choose to raise your affection or hug her!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label kirinsoccer15:
    scene kirinsitups1
    with fade
    play music "highspeedprinter.mp3"

    "I head over to the gym to see how soccer practice is going."
    "Today, I am finally going to do my job as a coach and teach these girls the true meaning of sportsmanship."

    if bonus == True:
        "Just kidding."
        "I’m probably just going to stare at them and figure out why I have yet to open up a thigh massage stand in the corner of the room."
        "{i}That{/i} is the life I was destined to lead. Not this life of..."
        "Of..."

    s "Where even is everyone?"

    "I reach into my pocket for my phone to see if I’m here too late, but just as my fingers find their way into my pocket, a familiar voice cries out from the opposite side of the gym."

    mi "Sensei! Come quick! Kirin is dying!"
    s "That can’t be true when this background music is so upbeat. "
    ka "Background...music?..."

    if karinlied == False:
        scene kirinsitups2
        with dissolve
    else:
        scene kirinsitups3
        with dissolve

    "I make my way over to Miku and Karin to see what all this commotion about Kirin dying is."
    "But Kirin isn’t even here."
    "Oh no."
    "Was I too late?"

    s "Where will she be buried?"
    mi "Heck if I know. I say we just toss her into the nearest dumpster and set it out to sea."
    s "I can’t imagine it would get very far before sinking."
    mi "Then let’s just drop her out of an airplane and send her off with an even bigger splash."
    s "Miku, what is wrong with you?"
    mi "Pep talk! I’m tryin’ to whip her into shape."
    mi "If she thinks I’ll just get rid of her body when she dies, she’ll be more into...you know, not dying."
    s "I can’t wait to see this study posted in medical journals."
    ki "Can’t...go on!"

    "Another familiar voice wraps around my ankles and crawls its way up my body, slithering into my ears like some sort of miniature snake."
    "Basically, I hear Kirin."
    "That’s how a normal person would describe this."

    scene kirinsitups4
    with dissolve

    ki "Six-thousand-four...six-thousand...five!"
    mi "Woah! How’d she fit in an extra five-thousand-ninety in the time it took us to say hi to Sensei?!"
    mi "Kirin, stop! That’s enough!"
    ka "She’s just trying to make herself look cooler..."
    s "Congratulations on six-thousand sit-ups, Kirin. "
    s "Is this the same routine you used to get in shape for the beach?"

    scene kirinsitups5
    with dissolve

    ki "You mean when you...paid more attention to my sister than...you did to me?"
    s "I’m pretty sure all I did was compliment her."

    if bonus == True:
        s "If I remember correctly, I {i}definitely{/i} spent more time with you that weekend."
    else:
        s "I will compliment you as well if that is what you would like, Kirin."

    ki "Doesn’t matter if your...heart’s...not in it!"

    if bonus == True:
        s "Says the girl who willingly signed away any claim on my heart to her roommate."
        mi "Hm? What’s all this talk about hearts?"
    else:
        s "Says the girl who willingly signed away the right to ever enjoy a hug so her roommate could continue pursuing the elusive path of the huggy girl?"
        mi "Hm? What's all this about hugs?"

    mi "Kirin’s roommate's that creepy girl with the eyes that are all like “BA-BAM!” right?"

    if bonus == True:
        mi "You’re really gonna give your heart to somebody like that?"
    else:
        mi "You thinkin' about givin' your heart away to somebody like that, Sensei?"

    if karinlied == True:
        ka "Miku! Of course S...Sensei isn’t going to just...give his heart away..."
        ka "He’s going to wait for the right person to come along and...and..."
        ka "Ahhh, never mind! It’s too embarrassing to think about!"
    else:
        ka "..."
        mi "...Karin?"
        mi "Why are ya lookin’ all sad all of a sudden? You feelin’ okay?"
        ka "H...Huh?"
        ka "Oh. Yeah."
        ka "Yeah...I’m fine."
        s "..."

    scene kirinsitups6
    with dissolve

    ki "Hey...mind doing me a favor and...holding my legs still for a little while?"

    if bonus == True:
        s "I don’t think I have the willpower to do that in a safe-for-work way."
        ki "Then slide your head between 'em and let me squeeze it with my knees to stabilize myself."
        s "I have no idea how effective that will be, but it would be my pleasure."
        mi "Nobody is squeezing anybody’s head!"
    else:
        s "Sure thing, Kirin. That is a thing I can do because I do not look at you or any of the other girls as anything more than vessels waiting to be filled with knowledge."

        "I grab Kirin's ankles and she starts mimicking the theme song to the popular American sitcom, Seinfeld."

    mi "Kirin, if you’re not gonna take this seriously, I’m gonna have to figure out a way to {i}make{/i} you!"

    scene kirinsitups7
    with dissolve

    ki "I am...taking this seriously! Do you see how much I’m sweating?!"
    ki "It’s like...a fucking sauna in here! Isn’t a hundred enough?! That’s like...way above average!"
    mi "Karin and I both pumped out two-hundred without a problem at all."
    ki "You two are fucking mutants! I’m just a normal player! I’m not even that good!"
    mi "Sensei! Coach! Glasses!"
    s "Glasses is not one of my titles. "
    s "What do you want?"
    mi "We need ya to step in and motivate Kirin. "
    mi "Without your help, she’s gonna stay at the same level she is now for the rest of her life."
    mi "We’re reinventing her!"

    scene kirinsitups8
    with dissolve

    ki "I...ngh...don’t want to be reinvented..."
    ki "Just let me practice...how I want to practice..."
    ka "And how is that? By hanging out on your phone? Or spending the entire period talking to Sensei?"
    ka "We let you slack off every weekend. At least put some effort in today. "
    ka "We’re really trying to-"

    scene kirinsitups9
    with dissolve

    ki "SIX-THOUSAND-TWENTY!"
    ki "SIX-THOUSAND...TWENTY-ONE!"
    s "You’re still pretending you’re in the thousands? That’s just a waste of breath."
    ki "YOU’RE A...WASTE OF BREATH!"
    ki "SIX THOUSAND...TWENTY-TWO!"

    "I watch as Kirin repeatedly pulls her body up, struggling harder each and every time."
    "Miku and Karin pay close attention to her, calling her out whenever she doesn’t rise all the way."
    "It must feel horrible to be in her shoes right now."
    "Or, who knows? Maybe it feels good?"
    "She’s finally the center of attention for once- something even I understand she always wants to be."
    "But the attention isn’t exactly good this time."
    "The spotlight shining on her flickers."
    "It distracts her."
    "And, getting tired of the inconsistent light-"
    "She, too, burns out."

    scene black
    with dissolve

    ki "SIX THOUSAND...FORTY-NINE!"
    ki "I’m done! I can’t do any more!"
    mi "Ahhh no! That’s such a weird place to stop!"
    ka "Please do at least one more for all of our sakes."
    ki "No! That’s it! I’m done!"

    "Her arms go limp and her head falls down to rest in her hands."
    "She’s bright red and drenched in the efforts of her hard work."
    "I’m actually surprised that Miku and Karin were willing to push her this far when it’s clear that she’s at her breaking point."
    "But I guess it makes sense."
    "It’s not just routine. It’s punishment."
    "Like when a player makes a poor choice in a game and has to run extra laps at the next practice in order to make up for it."
    "Or other things that people who actually care about their jobs as team coaches force onto their players in the name of “improvement.”"
    "How much do you need to hurt someone in order to improve them?"

    ki "Hah...hah...hah..."
    ki "Sensei..."
    ki "Help me...up..."

    "Without looking toward Miku and Karin for approval (And also because I just feel bad for her in general) I reach down and grab Kirin’s hand, pulling her to her feet."
    "She winces in pain and clutches her stomach for a moment as she rises, but seems to be okay once she’s standing still."
    "........."
    "......"
    "..."

    scene kirinsitups10
    with dissolve

    ki "Hah...hah...hah..."
    ka "Do you think we might have...been a little too hard on her?"
    ka "She’s not looking so great right now..."
    mi "What are ya talkin’ about? She looks fine! Just a little red. But it’s a nice color for her!"
    ki "Kill...me..."
    ka "Kirin, maybe you should sit down for a second?"

    scene kirinsitups11
    with dissolve

    ki "I’m...fine! Just gotta...catch my breath!"
    s "Weren’t you just talking about how you wanted to call it quits like, a minute ago? "
    s "Maybe a break would-"

    scene kirinsitups12
    with dissolve

    ki "Oh, so now you’re on {i}their{/i} side as well? Figures."
    s "Why do there have to be sides? I just don’t want you pushing yourself too hard."

    scene kirinsitups13
    with dissolve

    ki "Yeah, well...it’s a little too late for that."
    ki "I feel like I fell in a lake."
    ki "But like, the lake was full of hot water that was also really sticky for some reason."
    ki "Probably pollution. "
    ki "Save the whales. Stop littering."

    scene kirinsitups14
    with dissolve

    mi "There are whales in lakes?!"
    mi "How do they fit?!"
    ka "Miku..."
    ka "I know your grades aren’t...the best. But please tell me that was a joke."

    scene kirinsitups15
    with dissolve

    mi "Sensei...How come you never teach us about whales? "
    s "Talk to Kirin. She’s the one who seems to care the most about them."

    scene kirinsitups16
    with dissolve

    mi "Kirin, how come you-"
    ki "I don’t give a shit about whales, Miku. I’m exhausted from doing six thousand sit-ups and am just talking out of my ass."
    ki "Is it cool if I go take a shower to cool down?"
    mi "Oh...uhh...well, we’re still in the middle of practice..."
    mi "But you {i}are{/i} kinda lookin’ a little worse for wear."
    mi "I guess it’s okay. But you’ve gotta come back as soon as you’re done for our practice game."
    ki "Yeah, yeah. Whatever."

    if bonus == True:
        ki "Can I take Sensei with me?"

        if karinlied == False:
            scene kirinsitups17
            with dissolve

            mi "Take him with you to...to the showers?! Why on earth would ya do that?!"
            ki "I’m not as flexible as you guys and can’t reach every part of my body."
            ki "I need his help getting all of the places I can’t get to myself."
        else:
            scene kirinsitups18
            with dissolve

            ka "Kirin! Again?"
            mi "Take him with you to...to the showers?! Why on earth would ya do that?!"
            ki "I’m not as flexible as you guys and can’t reach every part of my body."
            ki "I need his help getting all of the places I can’t get to myself."

        s "Well, if that’s what must be done-"

        scene kirinsitups19
        with dissolve

        mi "Keep it in your pants, Coach! I ain’t tryin’ to have a scandal on my soccer team until at least senior year!"
        mi "We’ve got stuff to focus on until then!"
        s "Hey, I’m just trying to look out for my players the only way I know how."
        mi "By bein’ a heckin’ perv and sneakin’ into the showers with ‘em?"
        s "Yes. Exactly that."
        s "So, now that we’ve all decided that this is okay-"
        mi "We have not decided that! I’m the captain and I say no!"
        ka "I..."
        ka "I also...say no..."
        ki "I say yes, which brings us to two against two."
        ki "The only possible solution is that we all just take a shower together."
        ki "Except for Karin. She can wait out here since she always takes too long."
    else:
        ki "Not sure if Karin was planning on coming or not, but I'd recommend that she stays out here."
        ki "She always uses too much water when she showers and it makes me worry about the future of the fish."

    scene kirinsitups20
    with dissolve

    ka "Wha- I do not! "
    ka "I take just as long as you do! "
    ki "Okay fine, but you also use twice the amount of shampoo."
    ka "I have twice the amount of hair!"
    mi "I..."

    if bonus == True:
        mi "Yeah, I don’t know if I want Sensei...seeing me...like that."

        scene kirinsitups21
        with dissolve

        ki "You {i}sure{/i} about that, Miku?"
        ki "Doesn’t it get your heart racing? Even just a little bit?"
        mi "Of course it does!"
        mi "I know firsthand how big his thing is because I sat on his lap during Halloween. And if I ever saw it up close I'd-"

        scene kirinsitups22
        with dissolve

        mi "Wait! I wasn’t supposed to say that!"
        mi "Makoto told me to never talk about it again!"
        ka "How...big...what is?"
        ka "His...bed?..."
        ki "Woah."
        mi "Kirin! Don’t tell Makoto I said that!"
        ka "Does he...maybe have a dog that’s...really big?"
        ka "But...why would Miku sit on a dog?"
        ka "Something isn’t...adding up..."

        scene kirinsitups23
        with dissolve

        ki "Did you like it?"
        mi "Wha-"
        mi "I mean...it was...fine!"
        mi "I try not to think about it!"
        ki "Because it gets you excited?"
        ki "My little Miku is growing up so quickly~"
    else:
        mi "Umm..."

    scene kirinsitups24
    with dissolve

    mi "Okay! Everybody into the showers except Sensei!"

    if bonus == True:
        mi "He should stay out here and think of Makoto’s naked body instead of ours!"
        mi "Bye, Sensei!"
        ki "Sorry~"
        ki "Can’t say I didn’t try."
        s "I feel like you had the chance to be a lot more persuasive than you actually were."
        ki "Or maybe {i}Miku{/i} was my target all along?"
        s "That’s-"
        mi "Bad! No!"
        mi "Everybody out! Practice is cancelled!"
        ka "A...chair?"
        ka "Those can get pretty big..."
        ka "That...yeah. That would make the most sense."
    else:
        s "That is fair. I will return home and shower in my own private shower, where no one can see me and I won't have to worry about accidentally bumping into any of you."

    scene black
    with dissolve2

    "In the end, the three of them disappear into the showers and I’m left out in the gym with all of the girls I don’t know the names of."
    "None of them really pay any mind to me, so I wind up deciding to get on with my day before Miku and the Kandas come back."
    "I think about apologizing to one of them through text for the disappearance, but-"
    "I’ve inadvertently stirred up enough trouble for the day and don’t want to make things any worse."
    "I’m sure they’ll understand."
    "I’m quite good at disappearing once things aren’t about me anymore."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirinsoccer15 = True
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kirinsoccer20:
    scene kirinthinking1
    with fade
    play music "behindabathroom.mp3"

    "So begins another day beside a calculated disaster."
    "I wasn’t particularly fond of that title when I first heard it in Kirin’s dorm room, but after putting a bit more thought into it, I think it works quite well."
    "In a sense, I’m also a calculated disaster of sorts."
    "And no, that is not another excuse for me to be self-deprecating. I already have plenty of those."
    "It’s a fair evaluation based on my tendency to change or mold myself to fit the ideals of those around me."
    "But I’ve never been fond of changing, so the transformation is always a bit incomplete."
    "Imagine you buy sixteen puzzles, all with at least one or more pieces missing. (It was a really shitty puzzle store.)"
    "And you have a friend who makes puzzles for a living."
    "An enigmatologist, if you will. "
    "The enigmatologist says to you-"
    "“I can likely craft you the missing piece based on a description of it, but there is a chance the size will be slightly off without the proper schematics.”"
    "Of course, that problem could be easily remedied if you’d just bring him the puzzle so he can figure out exactly what it is that’s needed."
    "But you’re a fucking lazy dick and don’t want to be bothered making a second trip."
    "So you have him guess and ultimately wind up with a piece that is slightly off."
    "But you still take it from him and just mash it into the puzzle anyway, not caring if it causes the rest to snap or break or whatever it is that happens when you try to solve a puzzle with brute force."
    "And everything comes falling down."
    "Everything but me, that is."
    "For I am both the enigmatologist as well as the one who was too lazy to ever provide the schematics."
    "I am both the cause of all problems as well as their respective solution."
    "A makeshift god who can provide temporary solace, but never truly guide someone toward salvation."
    "And as long as puzzles with missing pieces exist, I will continue to ruin them."
    "Because an enigmatologist does not just create puzzles, they solve them as well."
    "And if all of the puzzles in all of the world are solved, what is left for me to do?"
    "Break puzzles to make new puzzles."
    "Fuck it. Take every puzzle you bought from that shitty store and dump the contents into a giant bowl."
    "Maybe even a well."
    "Create the ultimate puzzle."
    "Solve it."
    "Become God."
    "Thank you for once again listening to my incessant ramblings about all that is broken and how to both fix and unfix it."

    ki "So...I’m thinking about quitting the team."
    s "Is this about the sit-ups again?"
    ki "Nah."

    if bonus == True:
        ki "Frankly, I was a little more disappointed that Miku wouldn’t let you into the showers with us despite clearly wanting it."
        s "So Miku’s prudence is the reason you’re thinking of quitting?"
    else:
        s "Is it about canola oil again?"

    scene kirinthinking2
    with dissolve

    ki "Nah."
    ki "I’m just thinking it might be time to move onto something I’m a little better at."
    ki "Like, I’ve been playing soccer for pretty much my entire life and have always been a middle-of-the-road player at best."
    ki "I still think it’s fun and everything, but it gets kind of annoying at times."
    ki "Like, you try so hard to improve...only to watch everyone else get better without putting in even half of the effort."
    s "I don’t really think it’s fair to say that they’re putting in less effort when, more often than not, it’s the two of {i}us{/i} up here rather than them."

    scene kirinthinking3
    with dissolve

    ki "Who says that I don’t spend every waking moment outside of practice practicing?"
    s "I think you might have the wrong idea of what “practice” and “outside of practice” are supposed to consist of."
    ki "Maybe I just like practicing alone better?"
    s "Because you’re self-conscious?"

    scene kirinthinking4
    with dissolve

    ki "What’s wrong with being a little self-conscious?"
    ki "I’m a [teenage]girl surrounded by other [teenage]girls who are naturally better at almost everything than me."
    ki "Of course I’m going to be self-conscious."
    ki "Do you think that makes me weak, Sensei?"
    s "No. I think it makes you human."
    s "Which is a good thing because I’ve definitely questioned that about you on several occasions."

    scene kirinthinking5
    with dissolve

    ki "What else would I be if not a human?"
    s "A puzzle."
    ki "Like a jigsaw puzzle or...a crossword puzzle?"
    s "Whichever one is harder for the average person to solve, I guess."
    ki "Probably a jigsaw puzzle, then. Those can get kind of intense once you start adding a bunch of pieces."
    ki "But I guess crossword puzzles can also get intense once you start adding crazy words like-"
    s "Enigmatology?"

    scene kirinthinking6
    with dissolve

    ki "Yeah. Whatever that is."
    ki "How is anyone supposed to guess a word that they’ve never even heard before?"
    ki "I mean, I guess it’s easier now since we all have access to the Internet, but still. That’s way too much work."

    scene kirinthinking7
    with dissolve

    ki "See that girl with the crazy thighs over there? The one with the ball in her hands?"
    s "That is your sister, Karin. I am quite familiar with her."
    ki "Yeah, whatsherface. "
    ki "She and I actually used to team up and put jigsaw puzzles together when we were little. Like, way before we were even in elementary school."
    ki "Neither of us were particularly good at them on account of being stupid little kids but, just like with soccer, she got better and I lagged behind."
    ki "Now, this club is pretty much the only thing the two of us ever do together."
    ki "So you can probably guess how that makes me feel."
    s "Not really any point in guessing when you’re already making it extremely apparent."

    scene kirinthinking8
    with dissolve

    ki "Hey, when a puzzle gets too hard, what do you do?"
    ki "Do you give up?"
    ki "Or do you keep working at it no matter how tough it gets?"
    s "No clue. But I’ll let you know how I feel the next time something like that happens to me."
    ki "Bummer."
    ki "I was hoping to find out what you’re planning on doing with me."
    ki "You know, since I’m just as much of a puzzle as I am a human being to you."
    ki "Once you’ve got all the outer pieces put together, are you really going to go through all of the effort to finish the rest?"
    ki "Or are you just going to call it quits and move onto another?"
    ki "I mean, we all know the outer part of the puzzle is the most fun. So why bother doing the rest when there are puzzles literally everywhere?"
    s "What would the equivalent of that be if we’re counting you entirely as a person and not an object?"

    scene kirinthinking9
    with dissolve

    if bonus == True:
        ki "I guess it would be just...getting close enough to fuck me, proceeding to {i}actually{/i} fuck me, and then running off to fuck somebody else when you realize I’m not worth fucking anymore."
        ki "Or something."
        s "So it all comes back to sex."
        ki "It all comes back to sex."
        ki "I mean, that’s how our relationship started, wasn’t it?"
        ki "A promise that you could have what you want from me as long as I can have what I want from you."
        ki "Luckily, we both want the same thing now."
        ki "Who’s to say either one of us will want to finish the rest of the puzzle once the outline is done?"
        ki "Sure, I guess there’s some momentary satisfaction once you actually {i}solve{/i} a puzzle. "
        ki "But after that, you just break it apart and put it back in the box or use that weird puzzle glue to hang it on the wall or the fridge."
        s "I don’t think you’d look particularly nice hanging on my wall."
        ki "I don’t even think you’d {i}fit{/i} on my wall."
        ki "Hell, I’m not even sure if you’ll fit in {i}me{/i}."
        s "So it all comes back to sex."
        ki "It all comes back to sex."
    else:
        ki "Beats me. You're the teacher, you come up with the comparisons."
        ki "I'm just here to gaze off into the distance and reflect on all of the horrible decisions I have made in my life."

    scene kirinthinking10
    with fade

    "Kirin looks away from me, watching the rest of the girls practice."
    "I can’t say for certain, as I still haven’t completed her outline, but I’m pretty sure she’s hoping that one of them looks over at her right now."
    "That someone smiles and coaxes her into coming down and practicing with them instead of abandoning her atop this stage filled with athletic bags and traffic cones."
    "At the same time, though, Kirin abandoned {i}them{/i}."
    "They’ve abandoned each other, so it wouldn’t make any sense for one of them to reach out."
    "It’s just an unfortunate yet realistic progression of one’s interests and confidence dwindling with the passage of time."
    "Time is the worst."

    ki "Maybe I’ll just find something to do with Noriko."
    ki "She’s fun to be around. And she’s yet to make me feel insignificant, so that’s pretty sweet."
    s "You two are still getting along?"

    scene kirinthinking11
    with dissolve

    ki "We’re kind of like two sides of the same coin."
    ki "We’ve got our differences and will probably never have the same exact mindset as one another, but we’re still out to do the same thing at the end of the day."

    if bonus == True:
        s "Is that “thing” having sex with me?"
    else:
        s "Saving the whales."

    scene kirinthinking12
    with dissolve

    if bonus == True:
        ki "I was talking more about filling a void in our hearts, but I guess the sex thing is also true."
    else:
        ki "I was talking more about filling a void in our hearts, but I guess the whales work too."

    s "Am I just a tool to you?"

    scene kirinthinking13
    with dissolve

    ki "You’re kind of a tool in general."
    s "I did not come here to be insulted."
    ki "A useful tool. Like a hammer or a...chainsaw."

    if bonus == True:
        s "Or a vibrator."
        ki "I guess it’s your turn to turn everything sexual now?"
        s "You did it twice in a row earlier, so now I have to catch up."
        s "From this point on, it’s anyone’s game."
    else:
        s "Or a whale catching net."

    scene kirinthinking14
    with dissolve

    ki "That aside, things have definitely started to look up a bit since Noriko and I moved in together."

    if bonus == True:
        ki "I always knew getting out of my parents’ house would be great for me, but combining that with a cool, new roommate and a teacher I actually like-"
        s "So it all comes back to sex..."
        ki "Stop fucking saying that when I’m trying to hand you a puzzle piece."
        s "Oh, we’re working together now?"
        s "I just thought we were solving our own puzzles in the same room as one another."

        scene kirinthinking15
        with dissolve

        ki "Doesn’t mean we can’t check in on each other’s progress every now and then."
        ki "Basically, I’m just saying that life is changing for me."
        ki "Still have no clue if it’s a good change or a bad one, but it’s definitely something. And I’ve been dying for {i}something{/i} for years."
    else:
        ki "My wardrobe has expanded to nearly three times its original size, even if most of the clothes are gaudy and unwearable now."
        s "I think Noriko's clothes are pretty neat."

    scene kirinthinking16
    with dissolve

    ki "Thanks a lot for being such a horrible person. I was starting to think other people like me didn’t exist."

    if bonus == False:
        "That was uncalled for based on just my outlook on fashion, but I will go along with her judgement regardless."

    s "Oh, we’re everywhere. You just need to figure out how to identify us."

    if bonus == True:
        ki "I found out how to identify {i}you{/i} pretty easily. Just had to lift my skirt and offer up my v-card. "
        ki "Pretty sweet deal in exchange for being able to feel my heart beat again, don’t you think?"
    else:
        ki "I found out how to identify {i}you{/i} pretty easily. Just had to flash my Seinfeld DVD and I had you hooked."
        ki "God, that show makes me feel like such a real New Yorker."

    s "Hopefully I’ll be able to feel that someday too."

    if bonus == True:
        ki "My heart or yours? Cause you can touch my chest pretty much any time you want. Just not sure if this is the best place for it and all."
        s "I meant mine. But I will gladly grope you in front of any amount of girls."
        ki "Grope away, good sir."

    scene black
    with dissolve

    if bonus == True:
        "I reach out for Kirin’s chest."
        "She closes her eyes and-"

        mi "S-Sensei! The heck are you doing over there?!"
        s "Trying to feel whole again."
        ki "Help! I’m being assaulted!"
        s "You fucking traitor."
        ki "Miku! Come save me!"
        mi "Sensei! Start doin’ ‘yer job and put all those friggin’ traffic cones back into the storage room!"
        s "Why did you even bring them onto the stage if you weren’t going to use them?"
        ki "{i}Ahh...Sensei...{/i}"
        s "And why is Kirin making these noises?"
        mi "Because you’re grabbin’ her friggin’ boob! Girls react to stuff like that!"
        s "This is a thing I absolutely did not know as it is my first time ever touching a woman and has definitely never happened before this moment in time."
        mi "I don’t care how many times it’s happened, I-"
        mi "Well, actually...I think I kinda do care."
        mi "But just let her go and do ‘yer job!"

        "I [[reluctantly] listen to Miku and stop groping Kirin."
        "She winks at me before adjusting her bra and skipping over to Miku in the middle of the gym."
        "I wonder if she’s actually going to follow through with quitting the team or if that was just another one of many of her momentary lapses in judgement."
        "But I guess there’s no way of knowing without waiting to see how things play out."
        "Until then, I will keep solving puzzles."
        "Or creating them."
        "Or all of the above."
    else:
        "For the next ten minutes, Kirin and I play rock, paper, scissors."
        "There is no specific reason why. We just get bored and run out of stuff to talk about."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirinsoccer20 = True
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label kirindate25:
    play sound "phonebeep.wav"
    stop music fadeout 10.0

    "I tap on Kirin’s name in my phone and wait for her to answer."
    "It’s already dark out, but not dark enough that she’d be able to shrug off an invitation on account of it."
    "Not like she would anyway, though."
    "Kirin thrives in the dark."
    "But that’s probably only because she’s so weak in the light."
    "And most other places, if you want my honest opinion."

    if bonus == True:
        "As much as I appreciate the constant battering of sexual innuendos and near-pleas for me to take her away to somewhere else [[with my penis], it doesn’t exactly scream “strength.”"
    else:
        "As much as I appreciate the constant near-pleas for me to take her away to somewhere else, it doesn’t exactly scream “strength.”"

    "It screams, though."
    "But the noises are unintelligible and pained like a dying animal."
    "Probably a bird."

    play sound "phonebeep.wav"
    play music "thesleepingcity.mp3"

    ki "Hey. What’s up?"
    s "Not much. Just walking around. "
    s "Are you free?"
    ki "Are you looking to come over? Or are you looking to meet up somewhere?"

    if bonus == True:
        s "We don’t seem to have very good luck in your dorm, so we should probably just meet."
        ki "Are you grading luck entirely on our chances of fucking each other?"
        s "Is there any other way to grade luck?"
        ki "There is not."
    else:
        s "I don't know. Making decisions is hard. You choose."

    ki "Uhh..."
    ki "Hold on a sec."

    "Kirin puts the phone down and a few moments of silence pass by."

    if bonus == True:
        "I’m not sure what she’s doing right now, but I imagine it involves a lot of thinking."
        "Thinking about if tonight is actually the night...or if we’re just destined to “almost” have sex another hundred times or so before actually committing."
        "Fate can be cruel like that."

    ki "Okay. Yeah."
    ki "I’m gonna send you an address. Is it okay if we meet there?"
    s "What sort of address?"
    ki "What, do you need to know if you should bring your bowling shoes or something? Why does it matter?"
    s "Wait, do I actually need to bring bowling shoes?"
    ki "I’ll see you in an hour."
    ki "Bye."

    play sound "phonebeep.wav"

    "Kirin hangs up and immediately texts me an address quite far from where I am now."
    "It’s somewhere between the urban district and the old district and I’m a little curious about why we’d have to go all the way there to meet up."
    "But it is what it is, I guess."
    "It’s not like I had anything else to do tonight anyway..."

    scene black
    with dissolve

    "{i}One hour later...{/i}"
    "........."
    "......"
    "..."

    scene becomingapuzzlepiece1
    with dissolve2

    "I find Kirin leaned up against an unfamiliar building in an unfamiliar part of town, and I realize that it’s the most familiar place I could possibly find her."

    if bonus == True:
        jump kirindate25x
    else:
        s "So we {i}are{/i} bowling after all."
        ki "Yes."

        scene black
        with dissolve2

        "Kirin and I go bowling."
        "I am much better than her and she hates the experience."

        $ renpy.end_replay()
        $ kirin_love += 5
        $ kirindate25 = True
        stop music fadeout 10.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label kirinspecial25:
    if kirinmarry == True and norikokill == True:
        scene kirinfire1
        with dissolve2
        play music "starvingtodeathoutofreachofthesun.mp3"

        ki "What the fuck did you just do?! I gave you the perfect chance to make Noriko happy and you went and fucking did {i}that?{/i}"
        ki "How long has she liked you for again? Half of her life? More? "
        s "I’m surprised you don’t remember since it’s all she ever talks about."
        ki "Why would you do that?! Chika’s not even fucking here! Just {i}lie{/i} and make Noriko happy. Since when are you opposed to lying?"

        scene kirinfire2
        with dissolve

        ki "Actually, that can’t even be the problem since you had no issue lying about what you’d do to {i}me{/i} as well!"
        ki "It’s like you intentionally picked the worst fucking outcome for everybody."
        s "Do you actually believe that? Or are you just saying it because you’re afraid of a future where you and I are more than...this?"

        scene kirinfire3
        with dissolve

        ki "How do you not realize by now that you and I are not the type of people who end up in...make believe fantasy bullshit relationships like {i}that?{/i}"
        s "You’re a [teenage]girl. You know nothing about how you’re going to “end up.”"
        ki "Maybe. But I {i}do{/i} know that going out of your way to hurt people makes you a shitty person. And if that’s what you did to Noriko, you’re even worse off than I thought you were."
        ki "Is she not broken enough for you? Do you want to cut her down before you fuck her? Is {i}that{/i} why it’s taking so long? She’s not sad enough yet?"
        s "It was just a game, Kirin."

        scene kirinfire4
        with dissolve

        ki "...Right."
        ki "It was just a fucking game."
        ki "None of it ever happened. "
        ki "Noriko will be fine...I will be fine...everyone will be fine."
        ki "Shit will go back to normal and you’ll remember that I’m just the girl you’re supposed to fuck and Noriko is the girl you’re supposed to actually care about."
        s "If that’s what makes you happy."

    if kirinmarry == True and norikokill == False:
        scene kirinfire5
        with dissolve2
        play music "starvingtodeathoutofreachofthesun.mp3"

        ki "How can you marry me and not Noriko?! "
        s "You’re still freaking out even now that she’s gone?"
        ki "Yes! Because I still don’t get it!"
        ki "Even with...both of us being shitty people or whatever! That...That doesn’t mean that we’d be happy as anything more than fuck buddies!"
        ki "Relationships are complicated! And weird! We’d have to like...make each other breakfast and...and buy each other presents or something! I don’t know!"
        ki "Take it back! I feel gross now!"
        s "Kirin..."
        s "Will you-"

        scene kirinfire1
        with dissolve

        ki "No! I will fucking not! And it’s not even funny to joke about shit like that!"

        scene kirinfire6
        with dissolve

        ki "You were supposed to marry {i}her{/i}, dude. Not me. I thought you would have realized that."
        ki "Now shit’s gonna be weird and she’s probably going to think you like me more than her or whatever."
        s "Well..."
        s "What if I do?"

        scene kirinfire7
        with dissolve

        ki "..."
        s "..."

        scene kirinfire8
        with dissolve

        ki "Then you keep it to yourself and don’t let either of us know."
        s "Oh."
        s "Then yeah. I guess that was a pretty bad move, then."
        ki "..."
        s "..."

    if norikokill == True and kirinmarry == False:
        scene kirinfire9
        with dissolve2
        play music "starvingtodeathoutofreachofthesun.mp3"

        ki "I know that being an asshole is kind of your thing, but don’t you think that might have been a bit much?"
        s "How so?"
        ki "You just told a girl that has been pining after you for half of her fucking life that she wasn’t even good enough to fuck and dump. Why?"
        ki "And don’t go saying some stupid shit about how you just wanted to be honest, because you are 100%% {i}not{/i} the type of person to do that when lying would bring you closer to someone else."
        s "It’s just...what I chose. "
        ki "..."
        s "..."

        scene kirinfire10
        with dissolve

        ki "You’re a fucking idiot."
        ki "I gave you the perfect set-up. I legit said “Hey, this is Sensei’s chance to exonerate himself” and you went and still fucking {i}married{/i} Chika anyway."
        ki "Married. Not just fucked. You {i}married{/i} her. In front of Noriko. {i}Noriko.{/i} Who fucking {i}loves{/i} you."
        s "That’s a lot of emphasis in such a short batch of sentences, Kirin."

        scene kirinfire11
        with dissolve

        ki "Yes! Yes it is! Because {i}apparently{/i}, you don’t have any fucking common sense anymore and I have to literally spell shit out for you to get you to understand!"
        ki "Do what you do best and fucking {i}lie{/i} if the truth is going to hurt someone! L-I-E. "
        s "It’s just a game, Kirin. Relax."

        scene kirinfire12
        with dissolve

        ki "Maybe for you and me. But for Noriko, it was more than that."
        ki "It was such an easy way to show her that, even if it’s just a little bit, she has a chance."
        ki "But to have you fucking kill her in the first pairing of three girls that was thrown out?..."
        s "..."
        ki "..."
        ki "This is exactly why I fucking hate love."

    if norikomarry == True and chikakill == True:
        if bonus == True:
            scene kirinfire13
            with dissolve2
            play music "starvingtodeathoutofreachofthesun.mp3"

            ki "You know, for a second there, I was worried that you were going to pick something else."
            s "I figured that fucking you and marrying Noriko would give everyone what they want most."
            s "Well, except for Chika. But it’s not like she’s really around to hear about her impending doom."
            ki "So, what position are we going for tonight? I accidentally left my underwear at home, so that opens up a lot of discreet, fully-clothed options."
            s "Choosing you for the fuck option wasn’t me saying “Let’s do it right now, Kirin.”"
            ki "Why not?"
            s "There is a flaming pile of trash behind you and I’m pretty sure we stepped over at least three dead rats on the way here."
            ki "Are you not turned on by dead rats?"
            s "...Are you?"

            scene kirinfire14
            with dissolve

            ki "Nah. But I {i}am{/i} turned on by dudes with huge dicks who tell me they want to fuck me in front of my roommate."
            s "I hope you’re specifically talking about me and that that isn’t just a blanket statement applicable to all well endowed men."

            scene kirinfire15
            with dissolve

            ki "Oh? Are you actually getting jealous thinking about me with someone else this time?"
            ki "Am I finally a slightly important figure in your life, [kirinmaster]?"
            s "Of course. Who else am I going to have sex with after I marry Noriko?"
            s "You’re the permanent threesome enabler and I must use the power I have to keep you locked into that role for the foreseeable future."

            scene kirinfire16
            with dissolve

            ki "Welp, I’m ready whenever she is. So that’s something you’re going to have to take up with her."
        else:
            ki "Did you like my super secret soda throwing move?"
            s "No. But seeing as I am clearly the best when it comes to playground games, I understand why you needed to employ such a dirty tactic."
            s "Also, where did Noriko go?"
            ki "She got upset about not knowing how to play hopscotch and is currently inside researching how to do it properly for next time."
            s "Is there going to be a next time?"
            ki "Sure is. So you better start figuring out how to dodghe soda cans now, mister."
            s "Tch."

    "I crack my knuckles and stare at the fire for a moment."
    "The light emanating from it attacks the back of Kirin Kanda and not only duplicates her figure onto the grease soaked wall behind me, but increases her size by triple or...even quadruple what it normally is."
    "Not like she’s all that large to begin with."

    if bonus == True:
        "I can still carry her in my arms if I want...or slam her body up against the tiled walls of a convenience store bathroom before fucking her and contracting some sort of infectious disease."
        "Not from Kirin, of course. From the bathroom."
        "Though, I’m sure she’d catch the same thing if we’re both...yeah."
    else:
        "In fact, she is just the right size for hugging."

    "Anyway, I tilt my neck to the side and focus on her colossal silhouette, dyed orange by the flames a probable anarchist lit before I arrived."

    if bonus == True:
        "I picture a life in which a twenty foot tall Kirin roams the streets of Kumon-mi, masturbating in public and turning into a legendary figure admired by all men and feared by all parents."
        "Except the male parents."
        "And lesbian/bisexual female parents."
        "I think of a lot of strange things when I don’t know what else to do with my time."
        "And Kirin’s sudden transition into silence has forced me into a position where that is just...what I have to do now."
    else:
        "I picture a life in which a twenty foot tall Kirin roams the streets of Kumon-mi, trying to get everyone to watch the third season of Seinfeld."
        "An ominous bass line plays behind her as she crushes building and asks passersby {i}what's up with that?{/i}"

    ki "..."
    s "..."

    "I wonder if she’s thinking of a twenty foot tall version of me."
    "But then I realize she isn’t."
    "That would be weird."

    scene kirinfire17
    with dissolve

    ki "So..."
    ki "Did you want to maybe like...walk back to the dorms together or something?"
    s "Right now? No. I’m still recovering from the walk over here."
    ki "Let me guess- you didn’t want to ride the bus because of all of the weird people on there this time of night?"
    s "Leave it to you of all people to understand me."
    ki "{i}Nobody{/i} likes riding buses at night, dude. Being one of those people doesn’t make you unique."

    if bonus == True:
        s "You’re right, Kirin. I’m just a normal guy with normal interests and a normal sized penis."

        scene kirinfire18
        with dissolve

        ki "If {i}that thing{/i} was normal sized, it would definitely explain Japan’s declining birth rate."
        s "Is that why you cried when you went back home after the love hotel? It was too big?"
    else:
        s "Yeah, well at least I don't cry after I lose at bowling."

    scene kirinfire19
    with dissolve

    ki "I didn’t...fucking...cry. I had allergies."
    ki "There must have been fucking...bed bugs or something. Dust? It was just a reaction."

    if bonus == True:
        s "Right, right."
    else:
        s "At a bowling alley? Yeah right."

    s "But yeah, if it’s not a problem, I’d like to stay out here for a little while longer. Even if there are bugs and...dead rats everywhere."

    scene kirinfire20
    with dissolve

    ki "Honestly, it skeeved me out the first few times I was here, too. But, after a while, you kinda get used to stuff like this."
    ki "I don’t really mind hanging out in places this gross so long as I’m with people I find interesting. And you and Noriko are pretty much as interesting as they come."
    ki "Karin, on the other hand...I doubt she’d last even a second over here."
    s "Yeah, she...definitely doesn’t seem like the type to...{i}indulge{/i} in urban alleyways."

    scene kirinfire21
    with dissolve

    ki "She’d probably rat me out to our parents if she even knew I was here."
    s "Was that an intentional “rat” pun or should I continue being unimpressed?"

    if bonus == True:
        ki "Continue being unimpressed, please. The less you like me, the harder you’ll fuck me."
        s "Is that how it works?"

        scene kirinfire22
        with dissolve

        ki "Beats me. You’re the one with the dick."
        ki "I just figured that like...hate sex is a thing. And romantic sex is probably more gentle or something."
        s "I don’t really think how much you like someone dictates how aggressive or violent sex with that person is."
        ki "Are you telling me that we live in a world where gentle hate sex exists?"
        s "Well...probably not."
        ki "Good. That’s not a world I’d want to live in."
        s "But you can be romantic and violent. Probably."
        s "I don’t know, Kirin. I just want to confirm that I have no intention of being gentle with you any time soon and that you shouldn’t worry about that happening as a result of us getting closer."
    else:
        ki "Continue being unimpressed, please. My sister is actually really nice and she deserves a chance to hug you as well."
        s "I'll add her to the hug list and let you know how things go."

    scene kirinfire23
    with dissolve

    ki "Works for me."
    ki "Now what, though?"

    if bonus == True:
        ki "We’re not having sex and we’re not walking home to {i}have{/i} sex. Does this mean we’re supposed to actually like...{i}talk{/i} to each other?"
        s "Are we about to challenge ourselves to have a full length conversation without bringing up sex?"

        scene kirinfire24
        with dissolve

        ki "Ew. Why would we ever do that?"
        s "Just to see if we can, I guess?"
        ki "Uhhhhhh..."
    else:
        ki "We're done playing hopscotch and we’re not walking home. Does this mean we’re supposed to actually like...{i}talk{/i} to each other?"
        s "I think that sounds great. Getting to know each other better is a wonderful opportunity that we should both savor and seize."

        scene kirinfire24
        with dissolve

    s "..."
    ki "..."
    ki "Hello, fine sir. Sure is...weather we’re having."
    s "Yes. I have also noticed that the weather is there."
    ki "Indubitably."
    s "Weather."
    ki "..."
    s "..."
    ki "..."
    s "..."

    if bonus == True:
        ki "Did you give Miku an orgasm?"
    else:
        ki "I asked Miku about canola oil and she ran away."

    s "Well that was a fun ten seconds."

    scene kirinfire25
    with dissolve

    if bonus == True:
        ki "No, really. She’s been all sorts of weird lately, and the only reason she was able to defeat me during the dorm war was because she blindsided me with a comment about that."
        ki "Like, Miku was straight up worried about even touching herself at the beginning of the year because she thought it would make her go blind."
        s "Why is that a thing you know? Do girls really just talk about their masturbation habits with one another?"
        ki "I mean, I can’t speak for {i}most{/i} girls. But I certainly do. And believe it or not, Miku and I are really close."
        ki "Not like {i}Noriko{/i} and me close where we watch porn together and walk around naked and stuff, but like...childhood friend close. Kind of."
        ki "I know she’s closer to Makoto than she is to me, but up until recently, she was kinda the closest thing to a best friend that I had."

        scene kirinfire26
        with dissolve

        ki "But nooooow, it looks like she’s finally starting to catch up to the rest of us who aren’t living in perpetual boredom anymore."
        ki "And I was thinking that some of that might have to do with the fact that you’re around."
        ki "I mean, I already know for a fact that she’s not interested in girls, so you’re pretty much the only other constant in her life that’s changed in some way."
        ki "Plus, she’s been getting as red as they come when you show up to practice lately. And you’re definitely the type to notice that and move in on it."
        s "Yes, but so are you."

        scene kirinfire27
        with dissolve

        ki "Oh, I already tried. That’s how I know she’s not interested in girls."
        s "Wait, what did you do?"
        ki "If I tell you, you have to tell me what {i}you{/i} did. That’s the rule."
        s "I mean, I was going to tell you anyway. I doubt you’d use it against me since you actually seem to care about Miku."
        ki "I was gonna tell you anyway, too, so I’m glad we got that out of the way."

        scene kirinfire28
        with dissolve

        ki "It was a hot summer day for the soccer team, just weeks after finding out we’d lost our coach."
        ki "Miku was working herself to the bone trying to keep the team in shape despite virtually all of us sucking and not even having enough players to have an in-team scrim with."
        ki "Enter Kirin Kanda, who spent the morning fingering herself to lesbian porn only to have her sister barge into the living room moments before orgasm and tell her it’s time for[school]."
        ki "Needless to say, I was very unhappy having basically blue balled myself by not giving into the first twenty urges to cum and was ready to fuck literally anything that moved."

        scene kirinfire27
        with dissolve

        ki "But alas. Morning soccer practice meant that Kirin must go even {i}longer{/i} without the sweet release she’d promised herself early that morning."
        ki "And, as the sun poured down onto the field, the urges grew stronger."
        ki "Thighs...everywhere! Boobs...less prevalent, but still there!"

        scene kirinfire29
        with dissolve

        ki "And there she was...in all of her innocent and sexually repressed beauty- skin glistening from the sweat of hard work."
        ki "The time came for Kirin to make her move."
        ki "She’d wanted to for ages because of her target's- err, {i}Miku’s{/i} boyish appearance and what seemed like a high chance she might be into girls."

        scene kirinfire30
        with dissolve

        ki "{i}Hey, Miku! You’re looking awfully stiff today. Want to take a few minutes after practice and have me relieve some of that tension for you?{/i}"
        s "Ah. I’m assuming she didn’t quite understand what you meant by “relieving tension.”"

        scene kirinfire31
        with dissolve

        ki "Of course not. This is Miku we’re talking about."
        ki "Anyway, I pulled her aside and started giving her a massage in the store room, but when I moved in for the kill, she nearly jumped out of her uniform and booked it to class."
        s "I’m sorry to hear that you never achieved that “sweet release” you set out for."
        ki "What? You think I just left the room without finishing myself off first? Come on. You know me better than that."
        ki "What about you, though? How did your first sexual encounter with Miku go?"
        ki "Has there been more than one? What’s her orgasm face like?"
        s "I didn’t see it, to be fair."

        scene kirinfire32
        with dissolve

        ki "Straight to doggystyle on the first go?! Who does she think she is?! Me?!"
        s "Not quite."
        s "I slept next to her and Makoto during a beach trip that just the three of us went on."
        s "But, in the middle of the night- and I don’t really know if it was conscious or not, she started grinding up against me."
        s "So, I did what any sane man would do and grinded back."
        s "One thing led to another and she had what was {i}probably{/i} her first orgasm ever while her best friend remained sleeping right beside us, completely unaware of everything."

        scene kirinfire33
        with dissolve

        ki "Jesus fucking Christ that’s hot."
        s "That’s really all that’s happened, though."
        s "There were a few times where I’ve thought things were about to go further but, like you said, she gets...jumpy and runs away."

        scene kirinfire34
        with dissolve

        ki "Wait...maybe she still likes girls after all then?"
        ki "If she’s running away from {i}you{/i} when you try to take things further, maybe the fact that I’m a girl had nothing to do with it and she was just-"
        s "Running from unwanted sexual contact?"
        ki "Unwanted sexual contact? What’s that?"
        s "The thing normal girls have when-"

        play sound "static.mp3"
        scene lavendersgreen24 with flash
        scene kirinfire34 with flash
        stop sound

        ki "When what? I still don’t get it."
        s "..."
        s "Anyway, we should probably let Miku develop at her own rate. Whenever she’s ready, I’m sure we’ll know."

        scene kirinfire35
        with dissolve

        ki "Hah...Yeah. I guess you’re right. That girl’s been through enough as is. Forcing her into sexual maturity before she’s ready will only fuck her up more."
        s "Do you..."
        s "Actually know what she’s been through?"
    else:
        ki "Why would she run?! It's a good question!"
        s "Speaking of Miku, do you actually know what happened to her?"
        s "Her eyes keep getting all weird any time a loud noise happens and it's giving me second thoughts about inviting her to my Fourth of July barbecue."

    scene kirinfire36
    with dissolve

    "I bite the bullet and ask something I’ve been wondering for a long time."
    "I’ve known Miku since the very beginning and still feel like I know nothing about her other than that she’s hyper and...good at soccer."

    if bonus == True:
        "And that she occasionally gets horny in her sleep and surrenders to the urge to grind up against whatever happens to be there at the time."

    "Would I prefer to learn whatever her secrets are from her directly? Sure."
    "But..."
    "What if that doesn’t happen?"
    "I’m already useless enough when she has those noise-induced episodes of hers."
    "And I’m no psychologist, but maybe understanding the root cause will help me figure out how to better tackle them in the future?"
    "I obviously don’t want her to feel that way, especially when I know that, more often than not, it results in her tearing her hair out."
    "I just want to help her."
    "I want Miku’s mind to remain unclouded."
    "And I don’t want Makoto having to pick up bits of hair with parts of her best friend’s scalp still attached to them off the floor of her dorm room."

    ki "I mean..."
    ki "I don’t know {i}everything.{/i} She doesn’t talk about it."
    ki "Well, I guess it’s more like she {i}can’t{/i} talk about it. And it’s something we know we’re not supposed to ask about."
    ki "I...really like Miku."
    ki "She doesn’t judge me. And she treats me like a normal girl even when I know I’m anything but."
    s "I care about her too, obviously."
    ki "{i}Is{/i} that obvious?"
    ki "It seems like you {i}care{/i} about a lot of people, but I never really know exactly what {i}caring{/i} means to you."
    s "..."
    ki "I guess you’ll find out sooner or later...so it might be better if you hear it from me so you don’t react weirdly and...start asking a million questions."
    ki "But this conversation never happened."
    ki "Miku’s one of the few people I just...really want to hang onto."
    s "I never heard anything."
    ki "...Good."

    scene kirinfire37
    with dissolve

    ki "Miku watched her parents die when she was little."
    ki "And ever since then, loud noises or whatever have kinda...teleported her back in time or something like that."
    ki "I don’t know {i}how{/i} it happened, but I know it was a big enough deal for our[school] to tell all of us to keep our mouths shut and not ask her any questions about it."
    ki "I mean...who {i}would{/i} ask her about something like that in the first place?"
    ki "But yeah. That’s what those episodes are. And that’s why there’s nothing anyone can really do about them."
    ki "Her brain’s fucked beyond repair and neither you nor me can {i}fix{/i} her no matter how we want to."
    ki "Some people just wind up getting so scarred that they never really have a chance to fully develop or something. I don’t know."

    scene kirinfire38
    with dissolve

    ki "That’s just who she is now, I guess."

    scene kirinfire39
    with fade

    s "Are you leaving?"
    ki "Yeah. I’m gonna go see what she’s up to."
    ki "If she’s even awake, I guess. I’m pretty sure the class rep has some sort of sleep schedule she keeps her on to make sure her grades don’t explode."
    s "Grades should be the least of her worries now."
    ki "True. But that’s less because you're our teacher and more because all of her other worries are much, much worse."
    s "Thank you for telling me."
    ki "Telling you what? I never said anything."
    s "..."

    scene kirinfire40
    with dissolve

    ki "Also..."
    ki "You need to do something about Noriko."
    s "What do you mean?"
    ki "I mean that this constant struggle she’s in where she’s...trying to make you understand her while {i}also{/i} trying to change herself to fit your needs is dangerous."

    if norikokill == True:
        ki "Not to mention that now she’s probably sick to her stomach knowing the guy she loves flat out said he’d kill her in favor of two other girls earlier."

    s "..."
    ki "I’m not saying you should {i}date{/i} her or that you two are meant to be together or some sappy bullshit like that..."
    ki "I’m just saying that one friend who’s already had their growth stunted by tragedy is enough for me."
    ki "And I think losing you would break Noriko more than you can possibly understand right now."
    s "..."
    ki "..."

    scene kirinfire41
    with dissolve

    ki "But, then again, what do I know?"

    if bonus == True:
        ki "I’m just your fuck buddy who, on rare occasions, talks to you about non-sex related stuff where we both pretend to feel sad when we know deep down that we’re more numb than anything else."
    else:
        ki "I’m just your hug buddy who, on rare occasions, does impressions of you in the mirror."
        s "Wait, you do what?"

    ki "Goodnight, Sensei."

    if kirinmarry == True:
        ki "And thanks for marrying me."
        s "I thought you hated that?"
        ki "I did."
        ki "Now, please excuse me while I go puke my brains out at the thought of a peaceful life alongside someone as depressing as you."

    else:
        s "Goodnight, Kirin."
        s "I’ve already forgotten everything you’ve told me tonight."
        ki "Hm? Did I tell you something?"
        ki "I honestly don’t remember."

    scene black
    with dissolve2

    if norikokill == True:
        "I go back inside to find Noriko crying behind the counter."
        "She wipes her tears away as I approach her before smiling the same obsessive, partly creepy smile she always has when I’m nearby."
        "And, in spite of what I think my body wants me to do, I wrap my arms around her and tell her I was just kidding."
        "What a powerful pair of words that can be when used in the right context."
        "We break apart and, minutes later, the time comes for me to go home."
        "As I make my way to the door, she reminds me of how much she loves me."
        "And I tell her I love her too."
        "........."
        "......"
        "..."
        "Just kidding."

    else:
        "I go back inside and spend the next few minutes hanging out with Noriko."
        "I neglect to inform her of her roommate's sudden desire to hang out with someone else as I don’t want to negatively impact her self esteem in any way."
        "And as I pat myself on the back for doing yet another good deed, I’m reminded of how truly fulfilling life can be when all goes according to plan."
        "Of course, that only happens once in a blue moon."

        if bonus == True:
            "So as the next two years approach but never arrive due to time’s incessant desire to cum inside of us and leave us passed out on the bedroom floor-"
        else:
            "So as the next two years approach but never arrive due to wibbly wobbly timey wimey stuff-"

        "I will try to keep that in mind."
        "And I will fail miserably."
        "The same way I fail at virtually everything else that matters."
        "Or at least that’s what I {i}would{/i} say if anything else mattered to begin with."
        "Pain is real. It’s all of us that aren’t."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirinspecial25 = True
    stop music fadeout 10.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label kirindorm25:
    play sound "knock.mp3"

    "I knock on Kirin’s door and wait for her to answer."
    "Typically around this time of night, I’d be able to hear the TV on full blast or the unintelligible, angsty yelps of music Noriko has on."
    "However, tonight looks to be a slow one for the girls of dorm 10. "

    if bonus == True:
        "Either that or Kirin is just masturbating, which, all things considered, is an equally probable scenario when compared to the other things I listed."

    ki "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        "Ready for things to get “intense” if my final prediction is true, I bring my fingers to my zipper for easier access when Kirin demands control over my penis."
        "I am prepared, Kirin. "
        "Bring on the sex."
    else:
        "I do a cool spin move before walking into the room because I want to get the dancing out of my system first."

    scene kirinreading1
    with dissolve

    ki "Yo."
    s "Hey."

    if bonus == True:
        "So, it appears that my prediction was not entirely incorrect, but not entirely {i}correct{/i} either seeing as she’s just...casually reading an adult magazine like it’s the news section of the paper."
        "I hesitantly loosen my grip on my zipper as the probability of fucking her becomes unclear."
    else:
        "I do another spin move but Kirin is not impressed."

    if kirinkill == True:
        ki "Looking for Noriko?"
        s "Looking for you, actually."
        ki "Even after voting to kill me over her and Chika? "
        s "Oh, come on. Are you still upset about that?"
        ki "No. I love being murdered. It does wonders for my self esteem."
        s "Kirin, I formally apologize for killing you. "
        s "And, if it will make you feel any better, I will allow you to ride on top tonight."

        scene kirinreading2
        with dissolve

        ki "Golly gee, Sensei! On top? You really think I can do it?!"
        s "I think you can do {i}anything{/i} if you believe in yourself, Kirin."

        scene kirinreading1
        with dissolve

        ki "Get bent. I don’t want to have sex tonight."

        "Oh no. I think I broke Kirin."

    else:
        scene kirinreading3
        with dissolve

        if bonus == True:
            ki "What are you doing? Were you just holding your zipper?"
            s "What? No. Of course not."
            s "Why would I, an upstanding citizen and reliable teacher, come into this dorm room under the assumption that we were going to have sex?"
            ki "Probably becauuuuse...that’s...what we do?"

            "I tighten my grip on the zipper again, waiting for the signal that it’s go-time."

            ki "Well, correction. That’s what we {i}normally{/i} do. I’m too tired tonight."

            "The grip loosens again. This is getting exhausting."

            ki "But if you want to jerk off in mine or Noriko’s underwear, you can go pick up our laundry from downstairs. I’ll take losing one pair as the cost for not having to carry everything up here myself."
        else:
            ki "What was the spin move for?"
            s "What spin move? I don't know what you're talking about."

    if bonus == True:
        jump kirinpornox
    else:
        ki "If you're going to just keep doing that, get out. I'm busy."
        s "Whatcha reading, buddy?"

        "I do another spin. It is my best one yet."

        ki "..."
        s "What is wrong?"

        "More spins."

        scene black
        with dissolve

        ki "Okay. You're done."

        "Kirin gets off the bed and grabs me by the scruff of my neck like I am kitten."
        "It is equal parts comforting and scary, but then she throws me out of the room and I decide that it was {i}mostly{/i} scary."
        "I do another spin move on my way out of the dorm."
        "I am so cool and Kirin is a loser for not seeing that."

        $ renpy.end_replay()
        $ kirindorm25 = True
        $ kirin_love += 1
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label kirinsoccer25:
    scene kirinmassage1
    with fade
    play music "soda.mp3"

    "I decide for whatever reason to spend the morning with Kirin."

    if bonus == True:
        "And also Miku, apparently, seeing as Kirin is now knuckle deep inside of her in the least interesting way possible."
    else:
        "And also Miku, who is busy receiving a wholesome and friendly massage."

    mi "Aaaaaahh...yeahhhhh...that’s the stuff..."
    ki "What the hell have you been doing lately? Your shoulders are even more knotted than that creepy religious girl’s hair."
    mi "Oh...you know...a little of this...a little of...thaaaaaat..."
    s "Good morning, you two. "

    scene kirinmassage2
    with dissolve

    ki "Morning, Sensei. Don’t mind us. Just having a little quality time. Right, Miku?"
    mi "Can’t talk...melting..."

    if kirinspecial25 == True and bonus == True:
        s "Good for you, Kirin. Still being able to massage Miku like this given decisions you have made in the past."

        scene kirinmassage3
        with dissolve

        ki "Mmm!"
        mi "You...say somethin’, Sensei?..."
        mi "Can’t hear over the sound of...my body being turned into mush."
        s "Nope. Just happy to see you’re a trusting and loyal friend who’s still giving the benefit of the doubt to someone who doesn’t deserve it."
        ki "That’s right. Rationalize what {i}you{/i} have done by comparing it to what {i}I{/i} have done. Smart."
        s "I mean, it’s all in good fun. Right, Kirin? That {i}is{/i} what life is all about apparently."
        mi "You two are being...weird..."
        mi "How ‘bout we all just...lay down on this cloud together and...let our worries wash away?..."

    scene kirinmassage4
    with dissolve

    if bonus == True:
        ki "You like that, Miku? You like it when I do it right there?"
        mi "..."
        ki "You like having my fingers deep inside of you?"
        mi "..."
        ki "Too much?"
        mi "I feel like I’ve heard those lines in some kinda adult movie or somethin’."
    else:
        ki "Are you enjoying your platonic massage, Miku?"
        mi "Guhhhhhhhhhhhhhhhhhhhhhhhhhhhh..."

    s "Mind if I step in?"

    scene kirinmassage5
    with dissolve

    mi "And do what?!"

    if bonus == True:
        ki "Oooooh a four hand massage! Leave it to Sensei to turn my definitely-not-lewd massage into a definitely-even-less-lewd massage where we {i}really{/i} loosen Miku up!"
        mi "I just wanted the knots gone! I didn’t know this was gonna turn into a thing!"
    else:
        s "I think if I karate chop you as hard as I can, all of your knots will be defeated and leave."

    mi "W-Wow! My back suddenly feels a lot better! I don’t need any sort of-"

    scene kirinmassage6
    with dissolve

    mi "Ahh~"
    ki "What were you saying, Miku? You want me to stop?"
    mi "Oh god...I can’t..."

    if kirinspecial25 == True:
        "If Kirin is this good at giving massages, I’m surprised she wasn’t able to get Miku to just submit to her back when she tried to make a move."
        "Granted, I have no way of knowing if any of that story is actually true or not since Kirin is Kirin and...isn’t exactly honest 100%% of the time."
        "But there were way too many details for me to assume it was all fabricated."

    scene kirinmassage7
    with dissolve

    ki "As you can see, I’m a bit of a master when it comes to meticulous and aggressive finger movements."

    if bonus == True:
        s "Gee, I wonder why."
        ki "Hey, all I’m saying is there’s no way I’m the only person here with a masturbation problem."
    else:
        ki "It is because I used to play the piano."

    s "Oh, okay. I guess you’re just...not holding anything back in front of Miku anymore."

    scene kirinmassage8
    with dissolve

    if bonus == True:
        ki "Miku’s currently unable to comprehend anything you or I say because I put her into massage paralysis."
        s "There is no way that’s real."
        ki "Okay. True. But her comprehension is definitely at least halved. Here, watch this."
        ki "Mikuuuu...want me to help you cum?"
        mi "What? Come where? Where are we going?"
        s "That’s just normal Miku. She was going to interpret that sentence that way no matter the state she’s in."
        ki "Hmm...want me to say something a little harder to misunderstand then?"
        s "I won’t believe this secret talent of yours unless you do."
        ki "Okaaaay. But don’t be too surprised when you realize how awesome and talented I am."
    else:
        ki "Miku is currently unable to comprehend anything you or I say because I put her into massage paralysis."
        s "Good. Because she has always wanted to play the piano and knowing you can do that would make her feel sad."

    scene kirinmassage9
    with dissolve
    stop music

    if bonus == True:
        ki "{i}I sucked our teacher’s cock.{/i}"
        mi "Wha-?!"
    else:
        ki "{i}I can play the piano.{/i}"
        mi "Wha-?!"

    scene kirinmassage10
    with dissolve

    ki "Uhh...wait! You didn’t actually hear that, did you?"
    s "Kirin, what the fuck?"

    if bonus == False:
        s "Miku hates the piano."

    scene kirinmassage11
    with dissolve

    ki "She’s never broken out of it before! How was I supposed to know that {i}now{/i} would be the-"
    mi "Are you insane?!"
    s "Yeah, are you insane?"
    ki "Not...intentionally! I didn’t mean to-"

    if bonus == True:
        mi "What kinda fuckin’ lunatic shoves a whole rooster in her mouth?! Let alone one that belongs to our teacher!"
    else:
        mi "What kinda fuckin’ lunatic learns how to play the piano?!"

    scene kirinmassage12
    with dissolve

    ki "I couldn't help myself, okay?! It sounded fun and-"
    ki "..."

    play music "soda.mp3"

    if bonus == True:
        ki "...Did you say rooster?"
    else:
        ki "...Wait, why {i}do{/i} you hate the piano?"

    scene kirinmassage13
    with dissolve

    mi "Woah. Have we been at soccer practice this whole time?"
    mi "I’ve gotta find Karin and-"

    scene kirinmassage14
    with hpunch

    ki "God fucking damnit. "
    mi "Ahhhhhyeaaaaaah............right.............there..........."
    s "Okay, well, I think that’s enough borderline tragedies for the day. It might be time to maybe {i}stop{/i} massaging Miku."
    ki "Not gonna lie, I thought my heart was about to burst out of my chest."
    s "Really? You have one of those?"

    scene kirinmassage15
    with dissolve

    ki "Yes, actually. And despite what you may believe about me, there are a handful of things that can actually cause it to start beating a little faster every once in a while."

    if bonus == True:
        s "Well it’s...nice knowing that revealing your sexual relationship with a teacher to one of your close friends is one of the things that can make that happen."
        s "I don’t really know what I’m supposed to say here. But if you keep this up any longer, I fear for Miku’s health."
        mi "Heheh...hehe...haaaaah...fingers..."
        s "See? Next thing we know, she’ll lose what little cognitive ability she actually has and slip into a comatose state that neither of us will ever be able to wake her up from."
    else:
        s "That's exactly how I feel any time there is a curly fry inside my order of regular fries."
        ki "You know you can just order curly fries, right?"
        s "Tch. You just don't understand, Kirin."

    scene kirinmassage16
    with dissolve

    ki "Mikuuuuuu~ Are you going to go into a coma?"
    mi "The comma is...a punctuation...you use to...make pauses in...sentences...and...list stuff..."
    s "Great, she’s already back in first grade."

    if bonus == True:
        ki "Mikuuuuu~ If you {i}do{/i} go into a coma, do you want me to protect you when Sensei tries to fuck your unconscious body?"
    else:
        ki "Mikuuuuu~ Tell me what a canola is..."

    s "..."

    scene kirinmassage17
    with dissolve

    ki "Teehee~"
    s "How many times-"

    if bonus == True:
        scene kirinmassage18
        with dissolve

        ki "Yeah, yeah, yeah. {i}You didn’t do anything.{/i} But can you at least let me {i}believe{/i} you did since it's more fun that way?"
        s "There’s more to life than just-"

        play sound "static.mp3"
        scene beforewefall5 with flash
        scene yumis2 with flash
        scene kirinmassage19 with flash
        stop sound

        s "Than just..."
        ki "Psst. Want me to jerk you off? Spending so much time on Miku got me horny and I kinda wanna fool around for a little while."
        s "..."
        s "We’re in a gym full of other girls right now."
        ki "Then let’s call them all over and we can all take turns on you. Whoever gets you to cum first is the winner."

        if kirinbjcontest == True:
            ki "And, need I remind you, I have a 100%% win rate in contests like this. I’m trying to keep the win streak alive."
        if ayanebjcontest == True:
            s "Is this how you redeem yourself after losing the last contest?"
            ki "I don’t know. Depends on if you like me enough to cum for me or if you’re going to wait for another basic blonde bitch and cum for her instead. "
            ki "Ball’s in your court, Sensei. "
            ki "Like, literally. You’re the coach and there are balls all over the place in here."
            ki "Speaking of which, can I start jerking you off now? I’m bored."

        s "I’m good right now, Kirin."

        scene kirinmassage20
        with dissolve

        ki "Booooring."
        s "I’m sorry to disappoint you, but being reminded of a thing I’m not proud of kind of kills the mood for me."
        s "I just want to forget everything that did or...didn’t happen and just move on."

        scene kirinmassage21
        with dissolve

        ki "No wonder you’re all knotted up if you’re stressing over something like that."
        ki "Sexual stuff aside, I can definitely help you, you know. "
        ki "I have no fucking clue what you’re going to do about the Molly situation but, at the very least, you can let me help you relieve some of the tension."

        scene kirinmassage22
        with dissolve
    else:
        play sound "static.mp3"
        scene yumis2 with flash
        scene kirinmassage22 with flash
        stop sound

    ki "It’s exhausting being such a horrible person sometimes...isn’t it?"

    if bonus == True:
        s "..."
    else:
        s "Wait a second. Does my super secret background trauma involve canola oil now? Why did that just cause me to black out?"

    scene kirinmassage23
    with dissolve

    ki "Don’t you wish you had somebody who understood you? Who saw all of those “bad” things a little differently than everyone else?"
    ki "Someone who accepts you for who you are, even though who you are shouldn’t be allowed to exist in this world?"
    s "Kirin-"

    if bonus == True:
        ki "I was too forward the other night in the dorm."
        ki "Like, the sex was {i}amazing{/i} so I don’t regret it one bit. But somewhere between the multiple orgasms and stained bedsheets, I think my point may have gotten lost."
        ki "I don’t want you to think I’m telling you to just wander around the streets of Kumon-mi [raping] women and cumming on sleeping girls in cosplay and stuff."
    else:
        ki "I'm sorry for not appreciating your spin moves. They were really cool and you are so talented."

    s "Great. Thanks for clearing that up. You really are a good person."

    scene kirinmassage24
    with dissolve

    if bonus == True:
        ki "I’m {i}saying{/i} that if you {i}do{/i} find yourself getting lost and doing things you regret, it doesn’t make you any less human than you were the day before."
        ki "We all have lapses in judgement, and people shouldn’t be ostracized for giving into those lapses from time to time- even if the end result is something really, {i}really{/i} bad."
        ki "You think Molly would still be following you around like a puppy trying to get adopted if you {i}actually{/i} hurt her? No, of course not."
        ki "Whatever you {i}did or didn’t do{/i} clearly isn’t all that bad since she doesn’t even seem to care about it."
        ki "So take one for the team and just fucking talk to her if you’re going to get so down about it. Sure beats crying like a little bitch all day and having one of the soccer players massage you, doesn’t it?"
        s "..."
    else:
        ki "Do you think you could teach me how to do them some time?..."
        ki "I think that if I do one in front of my parents, they will finally understand that I am just as good as my sister..."
        s "..."
        ki "Sensei?"

    scene kirinmassage25
    with dissolve

    s "All things considered, you’re definitely good at shoulder massages."
    ki "Had to be good at {i}something{/i}, you know?"
    ki "For Karin and Miku, it’s soccer and...friendships."

    if bonus == True:
        ki "And for me, it’s shoulder massages and blowjobs. "
    else:
        ki "And for me, it’s shoulder massages and piano. "

    ki "And while that might not seem like a good list of talents to most people, look at who you came here to spend time with today."
    s "..."

    if bonus == True:
        ki "Are you done feeling sorry for yourself now? Or do you wanna rail me in the storage room really quick and get that last bit of negative energy out?"
        s "Maybe tomorrow. One last day of feeling sorry for myself should be enough to make up for anything I may have done at the Halloween party."
        ki "That’s the Sensei I know."
        ki "And Molly? What are you going to do about her?"
    else:
        ki "So, can I learn the spin move now?"
        s "Maybe tomorrow. I just remembered a thing involving Molly that didn't happen in this game and am obligated to address that."
        ki "What are you going to do about her?"

    s "You're not actually worried about her, are you?"

    if bonus == True:
        ki "No. But the sooner you figure out what actually went down, the sooner I can finger myself to it."
        ki "Also, I’m open to threesomes with literally any girl and she seems like one of the ones who might {i}actually{/i} be into it."
        s "So it’s all about what you want in the end."
        ki "..."
    else:
        ki "Of course I am. She is a good person and I only want good things to happen to her."
        ki "And also to me."
        s "So it’s all about what you want in the end."

    scene kirinmassage26
    with dissolve

    ki "That’s right."
    ki "It’s all about what I want."
    s "..."
    ki "..."

    "Kirin presses her head against my shoulder and stops massaging me long enough for me to realize that, underneath the mask, she’s just one more [teenage]girl in a sea of hundreds I see every day."
    "And while her outlooks may be twisted and remorse has no place in her personal dictionary, she’s still as fragile and full of blood as the rest of them."
    "Perhaps she’s even more fragile."
    "Perhaps that’s why she’s focused so intensely on protecting herself from everyone and everything, even those who are on her side."
    "It’s hard to say if I’m one of the people on her side or not."
    "But I know that, even if it's not in the most ideal way, she's helped me more than anyone lately."
    "I don’t particularly {i}want{/i} to talk to her about any of what I think I might be feeling, but...strangely enough, it seems like she might be the only person I {i}can{/i} talk to right now."
    "At least without feeling like I did something wrong."
    "Which I didn’t."
    "Nothing happened on Halloween."
    "And if it did..."
    "It wasn’t my fault."

    s "..."
    ki "..."
    ki "I’ve decided to quit the soccer team."

    scene kirinmassage27
    with dissolve

    s "What?"
    ki "Yeah."
    ki "Once summer comes around, I’m just...done."
    ki "I can’t do it anymore."
    s "..."
    ki "It was nice getting to be around Miku and...I guess Karin, too. But seeing how much better everyone is than me is really fucking exhausting sometimes."
    s "I don’t really know much about soccer, but...I don’t think it’s supposed to matter how good you are as long as you’re having fun."
    ki "Sure. But what if your brain directly links how fun something is to how good you are at it?"
    ki "How am I supposed to enjoy myself when even being next to most of these girls makes me feel like a fucking useless amateur?"

    scene kirinmassage28
    with dissolve

    if bonus == True:
        ki "Wanna start a blowjob club instead? That sounds fun, doesn’t it?"
        s "So fun that I can already feel myself getting fired."
        ki "At this point, you could probably fuck someone in the middle of class and get away with it. Like {i}everyone{/i} knows that you’re into [teenage]girls and you’re still here somehow."
        s "Even so, I think the blowjob club might be a bit of a pipe dream right now."
    else:
        ki "Wanna start a hug club? That sounds fun, doesn't it?"
        s "HUG CLUB?! SIGN ME UP RIGHT NOW."

    scene kirinmassage29
    with dissolve

    ki "Maybe I’ll join some other club then. "

    if bonus == True:
        ki "Our class has a lot of girls in the manga club, but...I don’t really think something like that would be a good fit for me."
        s "Maybe a part time job?"
        ki "I don’t think work is a good fit for me either since the only place I’ve actually worked at fired me."
        s "Oh, right. That was a thing."
        ki "I don’t know. I guess I’ll just figure shit out when it happens."
        ki "All I know is that I can’t do {i}this{/i} anymore...and that I’m kiiiiiinda proud of myself for lasting as long as I have."
        s "..."
        ki "Can you be proud of me too, Sensei?"
        ki "For managing to stay afloat in a sea full of people who keep using my head to hold themselves above water?"
        s "You’re really good at metaphors too, aren’t you?"
    else:
        s "NOOOOOOOOOOOOO! I WANT THE HUG CLUB!"

    scene kirinmassage28
    with dissolve

    ki "Ooh! Metaphor club! We’d both be great at that!"

    if bonus == True:
        s "..."
        ki "Hey, it’s just an idea. You vetoed the blowjob club so I’m kinda just grasping at straws here."
        s "Just..."
        s "Keep an eye out for things you might be interested in, I guess..."
    else:
        s "KIRIIIIIIIIIIIIIIIIIIIIINNNNNNNNN!!!!!!!!!!!"

    scene black
    with dissolve2

    "Kirin stays attached to me for the rest of the gym period, but none of the others seem to mind."
    "Apparently, she’s been doing this a lot lately- spending her time in the club helping others get over their stiffness instead of doing something to remedy hers."

    if bonus == True:
        "And while I’d like to say that it’s nice she’s looking out for her teammates like that, I think there’s a high likelihood she’s only doing it to try and get into their pants."
        "I can relate."
        "It’s still weird thinking about how it will be here without her, though."
        "Even if she doesn’t ever really {i}practice{/i}, I’ve grown familiar with her place atop the stage- basking in the sunlight pouring in through the oversized windows of the gymnasium. "
        "And I’m not all that interested in seeing how the stage looks without her there."
        "Sunlight on its own has never been worth admiring to me."
    else:
        "Also, she is mean and was only joking about the hug club >=("

    $ renpy.end_replay()
    $ kirinsoccer25 = True
    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if ayanelust15 == False:
        $ kirinspecial30skip = True

    jump saturdayafternoon

label kirinspecial30:
    play music "phantomthief.mp3"
    scene kirinayaneoffice1
    with dissolve

    if bonus == True:
        jump kirinspecial30x
    else:
        s "So, Kirin...do you know why I called you here today?"
        ki "Nope. Not a clue."
        s "Do you remember back in 0.8.0 when I ordered Ayane to build one hundred sand castles and you showed up after the 99th and knocked them all over?"
        ki "Is that how that event was remade?"
        s "The time has come for you to finally pay the price."
        ki "But it's been so long since then. Can't we just like...hug and call it a day or something?"
        s "As nice as that sounds, I am unable to accept."
        s "Ayane is a good person. And even if all she talks about nowadays is making bone necklaces-"

        play sound "knock.mp3"

        ay "{i}Booooooooone necklaaaaaace........{/i}"

        s "And even if all she talks about nowadays is making bone necklaces, she has a good heart."
        s "For that reason, and many others, I hereby order you...Kirin Kanda-"
        s "To build one hundred sand castles."
        ki "But...we're in your office. There is no sand-"
        s "You should have thought of that before I raised Ayane's lust to 10 through solely hugging her and triggering the beach update.."
        ki "You will regret this, Sensei."
        ki "I will build the best office sand castles you have ever seen."

        scene black
        with dissolve

        s "I'm sure you will, Kirin."
        s "I'm sure you will..."

        $ renpy.end_replay()
        $ kirin_love += 1
        $ kirin_lust += 1
        $ kirinspecial30 = True
        stop music fadeout 7.0

        play sound "seinfeld.mp3"

        "{i}Kirin’s affection has increased to [kirin_love]!\nKirin’s lust has increased to [kirin_lust]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label kirinlust202:
    scene kirinxmanhall1
    with dissolve2
    play music "justlights.mp3"

    "The sound of the party does not relent even a bit despite how far away Kirin and I move from it."
    "I’m still not sure where she’s taking me but, knowing her, I imagine it’ll be somewhere quieter."
    "For someone with an alleged fear of missing out, she sure does isolate herself a lot."
    "Whether that’s intentional or not, I don’t know."
    "But it’s a part of her that, like many others, I’ll have to accept even when I don’t completely understand the rationale."
    "If there even is any rationale, that is."
    "I know {i}I’ve{/i} been known to do things I don’t fully understand from time to time."
    "But I can take solace in the fact that, at least so far, Kirin has not been on the receiving end of any of them."
    "And that’s in contrast to the irrefutable fact that she’d just convince herself she wanted it if any of that ever {i}did{/i} happen."
    "I’ll never understand her, but that’s okay."
    "Because she’ll never understand herself."

    if bonus == True:
        "Or at least not until she starts doing a little growing up in a way that doesn’t include having meaningless, casual sex with an older man."

        ki "So, wanna go have meaningless casual sex in the boiler room?"
    else:
        "Or at least not until she starts doing a little growing up."

        ki "Boy am I glad I never have to grow up."

    "See what I mean? Eternal youth."

    if bonus == False:
        ki "Let's go hug somewhere really dark and damp."

    s "Are you sure that’s what you really want right now?"

    scene kirinxmanhall2
    with dissolve

    ki "As opposed to what? Holding your hand and crying into your shoulder because some girl I don’t give two shits about said something mildly hurtful to me?"
    s "You seemed a little more than “mildly hurt” a few minutes ago."
    ki "I’m just a good actor, that’s all. "
    s "That would certainly be a convenient excuse."
    ki "It’s no {i}excuse.{/i} It’s true. "
    ki "I just don’t really see the need to act anymore in general."
    ki "If people want to look down on me, they can. It’s not like I think I’m some kind of angel or anything."

    scene kirinxmanhall3
    with dissolve

    ki "That’s why I wear these earrings, you know? Irony."
    s "You know, I kind of forget that Cupid is even an angel sometimes. In my head, he’s just some half naked baby who sunk an arrow into every single girl in class the moment I showed up."

    scene kirinxmanhall4
    with dissolve

    ki "Well, if he didn’t do it, I would have wound up just shooting myself eventually."
    ki "In the good way, of course. Not the super depressing way. Even if that might be the only thing I can imagine making an impact on my parents from time to time."
    s "The whole “holding hands and crying” thing is beginning to sound like a much stronger possibility the further we get down this hallway."
    ki "Sorry, but that’s getting a little closer to the line I already promised Noriko I wouldn’t cross."
    s "I didn’t realize promises actually meant anything to you."
    ki "They don’t."
    s "Then why-"
    ki "Because that’s just how it is, okay?"
    ki "Stop trying to figure me out and just be with me when I want you to be with me."

    if bonus == True:
        ki "You swallow up all of my angst and fury, and I’ll swallow up all of your cum in dark rooms where no one can find us. "
        ki "It’s just one more trade in a relationship completely built out of them."
        s "It doesn’t have to be, though."
    else:
        s "{size=-20}I just don’t want you missing out on more than, well, you’ve already missed.{/size}"

    scene kirinxmanhall5
    with dissolve

    ki "Uhh...what was that?"
    s "I just don’t want you missing out on more than, well, you’ve already missed."
    ki "But...I’m not missing out on anything. I’m getting exactly what I want out of you, and I’m {i}pretty{/i} sure you’re getting exactly what you want out of me."
    s "I am."

    if bonus == True:
        s "I can’t imagine I’ll ever love you. And having meaningless sex with you in...boiler rooms or whatever sounds like a great deal when all I have to do is absorb some of your feelings from time to time."

    scene kirinxmanhall6
    with dissolve

    s "But you’re allowed to want more."
    s "And if you think you’re just settling for what you deserve all the time, just...{i}take{/i} more."
    s "Stop manufacturing situations where everything goes wrong all the time and obviously a few more things will start to go right."
    ki "..."
    s "We’ve all got our reasons and whatnot. Yours just annoy me because there’s no drive to...grow."
    ki "Grow into what, exactly?"
    s "I don’t know. Something a little more valuable."
    s "Cry into my shoulder if you want. We’re going to be alone, aren’t we?"
    s "No one will ever know it happened."
    ki "You will, though."

    scene kirinxmanhall7
    with dissolve

    s "So what?"
    ki "I don’t know. I just don’t want to cry in front of you for some reason. There’s no double meaning to it."
    s "I’ve spent enough time with you to know that there is always a double meaning, Kirin."
    ki "And I’ve spent enough time with you to know that you don’t care about that."
    s "You-"
    ki "You can keep telling yourself I’m some sort of...temperamental brat who’s just forcing herself to be the antithesis of everything she admires in the real world-"
    ki "But that’s only, like...half true."
    s "What’s the other half then? "
    ki "H-"
    s "And don’t say hormones."

    scene kirinxmanhall8
    with dissolve

    ki "...ow are you doing today?"
    s "..."

    scene kirinxmanhall9
    with dissolve

    ki "Hah..."
    ki "Will you think I’m broody if I say there {i}is{/i} no other half?"
    s "Kind of, yeah."
    ki "Well, I’m saying it."
    ki "And since there’s nothing I can really do to fill that void myself, I’ll keep trying out things other people have in hopes that {i}something{/i} will slide into place."
    ki "Just like a puzzle piece."
    s "I feel like we’ve been here before."
    ki "So do I."
    ki "Just in a different sort of way."

    scene black
    with dissolve2

    if kirin_lust >= 20 and bonus == True:
        jump kirinlust202scenex
    elif kirin_lust >= 20 and bonus == False:
        "Kirin and I make our way into a boiler room, but standing in the center is famous Jewish comedian Jerry Seinfeld."

        seinfeld "What's the deal with airline food?"
        ki "Merry Christmas, Sensei."
        s "Kirin why"
        ki "One day, you will understand."
        s "Nooooooooooooooooooooooooooooo!"

        "Jerry Seinfeld tells what I think are supposed to be jokes for a little while before falling through a grate in the floor and disappearing forever."
        "Kirin is very upset about this but I don't really care."

        $ renpy.end_replay()
        $ kirin_lust += 1
        $ kirinlust202 = True
        stop music fadeout 6.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        jump christmastwo10

    else:
        "Kirin and I make our way into a boiler room that she had come across while navigating the halls by herself earlier."
        "She tells me that Noriko wasn’t able to come because she had to help out at her parent’s restaurant or something like that, but that she’s still dropping by to give me a present later."
        "Her voice cracks a little while telling me this- and I can’t figure out whether there’s any meaning to it or not."
        "I’ll just assume there isn’t-"
        "Because that’s what she’d want me to do in the first place."

        $ renpy.end_replay()
        $ kirin_love += 1
        $ kirinlust202skip = True
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        jump christmastwo10

label kirinlust30intro:
    scene thevaliumscene1
    with dissolve2

    ki "How are you feeling?"
    mi "You ever just think about phones?"
    ki "Well, I guess that answers that question."
    mi "No, seriously. I can just, like...press this glass in the right spots and then suddenly know more about bees. "
    mi "Who comes up with this stuff?"
    ki "I can’t tell if you’re so overtired that you’re acting high or if you’re just...you know, literally high."

    scene thevaliumscene2
    with dissolve

    mi "I wanna take a nap."
    mi "I can barely even remember what happened during the costume thing."

    scene thevaliumscene3
    with dissolve

    ki "Yeah. Well, Io did say that short term memory loss can be a side effect. But hey, at least you’re not puking your brains out all over the carpet."
    mi "Where’d Sensei go? I wanna talk to him again now that I don’t have to keep sayin’ all those weird buzzwords anymore. "
    ki "He followed a dolphin outside last I saw."
    mi "A dolphin? Maybe I really am high."
    ki "I’m sure he’ll be back soon. It’s not like him to stay away from an entire room full of girls trying to get into his pants."
    mi "I ain’t been followin’ the tally, but I hope my team wins...I miss the good old days when there were only ten of us fightin’ over Sensei’s pants."

    scene thevaliumscene4
    with dissolve

    ki "Are you officially a part of that fight now?"
    mi "Dunno what you’re talkin’ about."
    ki "I’m asking if you have feelings for him or not. Like, real feelings. Not just pubescent curiosities."
    mi "Pubescial what now?"
    ki "When you see him...how does it make your heart feel? Is it like when you’re playing soccer? Watching a horror movie? Or is it more like...I don’t know. When you’re watching porn or something?"
    mi "Maki says I can’t watch that stuff."
    mi "But if I had to compare it to somethin’..."

    scene thevaliumscene5
    with dissolve

    mi "I’d say it’s closest to wakin’ up from a really nice dream."
    mi "Ain’t so much racin’ as it is feelin’ comfortable. "
    mi "All's I know is that I ain’t ever felt this way ‘bout anyone before. And that I get now why Makoto’s liked him for so long."
    ki "..."
    mi "..."
    ki "Do you think I’ll ever feel that way about someone?"
    ki "That sounds nice...comfort, I mean. Being able to just be with somebody without being tempted to {i}do things{/i} with that person."
    mi "..."
    ki "I don’t know. Maybe I really am just a thirsty bitch at the end of the day. But I can’t help but feel a little jealous when other people know what they want."
    mi "..."
    ki "..."

    scene thevaliumscene6
    with dissolve

    ki "Hey. Wake up."
    mi "Huh? Were you sayin’ somethin’ just now?"
    ki "..."
    mi "..."

    if kirin_lust >= 30 and miku_lust >= 10 and mikucostumewin == True:
        scene thevaliumscene7
        with dissolve

        ki "When Sensei {i}does{/i} come back..."
        ki "Maybe we should see if he wants to hang out with just {i}us{/i} instead of the rest of the girls? "
        ki "That way...you’d get what you want in finally getting to spend time with him..."
        ki "And I could..."
        ki "I could keep an eye on you...and make sure you don’t pass out or anything."
        mi "I think that sounds nice. But Sensei’s not gonna wanna be with me when we’ve got people like Futaba walkin’ around with her bodonhonkaroos takin’ up half the room."

        scene thevaliumscene8
        with dissolve

        ki "He chose you over Uta, you know. And Uta’s got some pretty nice bodonhonkaroos for a girl of her size. "
        mi "Don’t remind me."
        ki "All I’m saying is...if this is the last night you get to be {i}that{/i} version of yourself, why not play it up instead of retreating back to your comfort zone?"
        ki "Sensei clearly likes this Miku. Why take her away?"
        mi "Cause at this point, I don’t know if {i}any{/i} Miku is going to be able to stay awake."

        scene thevaliumscene9
        with dissolve

        ki "Then we’ve just gotta do something fun!"
        ki "You snapped out of it for a second when you won the contest, didn’t you?"
        mi "Did I? I don’t remember."
        ki "You did. Which tells me that, in order to stay awake, you just need a little {i}more{/i} stuff to excite you! And what better way of getting that blood pumping than relying on your new crush?"
        mi "You think he’ll carry me? Cause I ain’t sure if I can walk if we’re goin’ anywhere."
        ki "Oh, yes. I’m quite sure he’d be happy to carry you."
        mi "Then sign me the heck up, Kirin."
        ki "I will. Don’t you worry."
        ki "In fact, don’t worry about anything at all if you’re not feeling up to it. Save that energy for later and leave all of the talking to me. I’ll make sure he comes along."
        mi "Think you can handle it? Sensei ain’t that easy to convince."
        ki "That just tells me you don’t know {i}how{/i} to convince him yet."

        scene black
        with dissolve2

        ki "But again, don’t worry."
        ki "I’ll teach you."

        "........."
        "......"
        "..."

    else:
        scene thevaliumscene10
        with dissolve

        ki "Hah...This is what I get for opening myself up for a second."
        mi "Kirin, you’ve been open for business since the day I met you."
        ki "Not like that, Miku."

        scene black
        with dissolve2

        ki "Let’s just hurry up and get you back to the hotel before anyone realizes that you’re drugged up."
        mi "Kaaaay...I’m gonna sleep like a rock, so I’m trustin’ you to not do anythin’ weird to me."
        ki "Does taking your makeup off count as weird? Because I wouldn’t be able to live with myself if I let you fall asleep with all of that on."
        mi "Just don’t touch my ears. I’m weak there."
        ki "Well, now I {i}have{/i} to..."

        "........."
        "......"
        "..."

    "I make my way back into the bar after miraculously avoiding what was sure to be my hardest decision of the weekend."
    "This means that, fortunately no one had their heart broken or felt betrayed by me tonight."
    "This also means that, unfortunately, my chances of getting laid on Christmas have greatly decreased."
    "But if there is anything I know about my likelihood of getting laid, it is that it’s never 0%%."
    "And that’s good enough for me."

    if kirin_lust >= 30 and miku_lust >= 10 and mikucostumewin == True:
        scene thevaliumscene11
        with dissolve2

        ki "Hey. What are you doing right now?"
        s "I was-"
        ki "Wrong. You’re hanging out with us."
        s "Okay, I guess I’m hanging out with you. But let it be known that the others are going to approach me and take me away after another few lines of dialogue because that’s just how it works."
        ki "Then we’ve just gotta beat them to the punch and get out of here before they have a chance to do that."
        s "Out of here?"

        scene thevaliumscene12
        with dissolve

        ki "Yeah. Miku and I were just talking about how sad we are that we haven’t gotten to spend much time with you this weekend. "
        mi "We were?"
        ki "{i}Yup.{/i} And we thought that maybe the three of us could head back to the hotel early and have a little fun together."

        scene thevaliumscene13
        with dissolve

        ki "What that means, only time will tell!"
        ki "You do like having {i}fun...{/i}don’t you, Sensei?"
        s "Uhh..."
        ki "...Sensei?"
        s "Are you on board with this, Miku?"
        mi "Teach, please. I’m on board with like, literally whatevs. If bestie says let’s go have fun, Miku’s gonna go have fun."
        s "You realize the contest is over right? You don’t have to stay in character anymore."

        scene thevaliumscene14
        with dissolve

        ki "She loves this character! Right, Miku?"
        mi "Huh? Oh. Oh, yeah. It’s great. I love not understanding what I’m saying."

        scene thevaliumscene11
        with dissolve

        ki "See? She’s all about it."
        s "Kirin-"
        ki "Sensei, come on! Before I change my mind! Who knows how many lines of dialogue we have left?!"
        mi "Sensei, can you carry me?"
        s "Carry you? Why would-"
        ki "Contest reward! A little bonus since Miku floored you with her amazing costume and above-average roleplaying skills."
        mi "I also can’t feel my legs."
        ki "Gyaru really do say some {i}crazy{/i} things now, huh?"
        s "This seems a little sketchy to me."
        ki "That’s just because you’re still in work mode! Come relax with us! This top is so tight that it's cutting off my circulation anyway. And I’m sure Miku feels the same way about her fishnets."
        mi "Yeah. And they ain’t even caught any fish."

    else:
        scene thevaliumscene15
        with dissolve

        ki "Hey. How much do you love me?"
        s "Zero."
        ki "Good. But how much do you love Miku?"
        s "I don’t know. Slightly more than zero?"
        ki "Great, because we need your help with something."
        s "I am assuming it’s something that’s going to take me away from the party?"
        ki "And you would be correct in assuming that, yes. "
        s "Yeah. That’s how most parties seem to end for me nowadays."
        s "What is it? What do you need help with?"
        ki "Io gave Miku a Valium and now Miku is about to pass out. "
        s "This sounds like a job for Makoto. "
        ki "Sensei, come on. Do you really want to bother Makoto with this after all she’s been through lately? I can handle it."
        ki "I just need your help carrying her back to the hotel. Or at least the Uber that will take us to the hotel. But you know what I mean."
        s "Wait, why did Miku take some of Io’s medication in the first place?"
        mi "I can’t remember. But I’m sure glad I did. "
        mi "You ever just think of phones before, Sensei?"
        s "Why did you let this happen?"
        ki "Doesn’t matter. Are you in or not?"
        s "..."
        ki "..."
        mi "Phones are like...they put all of the knowledge in the world inside a little box that you have to put {i}another{/i} little box on top of to protect it."
        s "Yeah, I should probably help."

    scene thevaliumscene16
    with fade

    ki "Okay then! On that note, let’s go wait outside. It’s way too stuffy in here and I need some fresh air anyway."
    s "I should probably at least say bye to-"
    ki "And risk getting stopped? No way. We have to do this now."
    s "I really don’t think another two minutes will-"
    mi "Ugh...pathetic. Aren’t you supposed to be a {i}man?{/i} Why don’t you just act like one?"
    s "By submitting to everything Kirin wants from me?"
    mi "Obvs by escorting these...two lovely ladies back to the hotel, loser. I can’t believe I had to spell it out for you. Hilarious."
    ki "So? Are we good? Can we go?"
    s "Yeah...fine. Whatever. Just lead the way."

    scene thevaliumscene17
    with dissolve

    ki "{i}Thank you, Sensei! You’re so- Miku, watch your foot. There’s a drop- okay. You’re on the ground now.{/i}"
    mi "{i}Ugh...can you believe the construction around here? It’s like...so outdated. {/i}"
    mak "..."
    f "..."

    scene thevaliumscene18
    with dissolve

    futamak "Hah..."

    scene thevaliumscene19
    with dissolve

    mak "Ah..."
    f "..."

    scene thevaliumscene20
    with dissolve

    mak "..."
    f "..."
    mak "You too?"
    f "Yeah..."
    mak "I see..."
    f "..."
    mak "..."
    f "Maybe...nothing will happen?..."
    mak "Yeah..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    mak "And maybe the sky will fall."

    if kirin_lust >= 30 and miku_lust >= 10 and mikucostumewin == True:
        jump kirinlust30
    else:
        "Nothing else happens when we return to the hotel."
        "But something almost does."
        "Instead of rushing Miku back to the girls’ room to make sure she gets her rest, Kirin suggests that we all go hang out in mine for a little while instead."
        "And for some reason, I don’t decline."
        "But halfway there, she changes her mind."
        "It doesn’t make me feel any better about myself."
        "But it {i}does{/i} make me feel better."
        "I collapse onto the bed and hide myself beneath the covers."
        "Before the darkness whisks me away, though..."
        "I think about what could have been."
        "And mourn the idea of any body but mine beneath these covers as well."
        "Sleep comes shortly after I do."
        "You’ll never guess who I thought of."

        $ renpy.end_replay()
        $ kirinlust30skip = True

        jump dormwartwo19

label kirinlust30:
    "On the way to the hotel, I take note of how different both Kirin and Miku are acting, but decide to focus more on Kirin instead."
    "Her changes are more interesting."
    "Miku is either overtired or mildly drunk..."
    "And that combined with a persona she’s been embodying for nearly three days now has forced the femininity out of her body quicker than I forced her first climax."
    "But Kirin..."
    "Kirin seems conflicted."
    "It’s a subtle change she hides exceptionally well...but she looks away more."
    "Like she’s ashamed of herself for something."
    "..."
    "It’s beautiful."
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."
    scene thevaliumscene21
    with dissolve2
    play music "asobeatsex3.mp3"

    if ayanelust15 == True:
        ki "Oooooh! What a nice room that I’ve definitely never seen before!"
    else:
        ki "Oooooh! Nice room you’ve got here, Sensei!"

    ki "It’s way different from the one we have. More...intimate, maybe? Am I thinking of the right word?"
    s "I guess. Imani was supposed to stay in here originally as well, but...unforeseen circumstances led to that not happening."

    scene thevaliumscene22
    with dissolve

    ki "I remember from when you first got here. I was, like...{i}soooo{/i} jealous."
    ki "That’s really sad, Sensei. I can only imagine how much {i}fun{/i} you two would have had together."
    ki "I guess we’ll just have to make up for it tonight. Won’t we Miku?"
    mi "Yeah...fun sounds fun right about now."
    ki "But what can {i}we{/i} do that {i}adults{/i} normally do when they’re alone in a hotel room?"

    scene thevaliumscene23
    with dissolve

    mi "Order a bunch of pay-per-view movies {i}and never pay.{/i}"
    ki "Uhh...yeah, maybe. I guess that’s one thing we can do."

    "I’m starting to think Miku is a little worse off than I initially believed, but..."
    "At the same time, she and I have already entered the next stage of our relationship. And there’s not much of a reason for me to hold back when I know she’s more than willing to accept me in the first place."

    ki "Is there a problem, Sensei?"
    s "What?"

    scene thevaliumscene24
    with dissolve

    ki "Oh, nothing. I just thought you just looked a little {i}conflicted{/i} all of a sudden."
    s "Me?"
    s "You’re the one who-"

    scene thevaliumscene25
    with dissolve

    ki "Oh, wow! Is that a bed?!"
    s "Well...it {i}is{/i} a hotel room after all."
    ki "It looks so comfy! Do you mind if I give it a try, Sensei? That won’t make you uncomfortable, will it?"
    s "Uhh..."

    scene thevaliumscene26
    with fade

    ki "W...Woooow! It really {i}i{/i}s comfy..."
    ki "Like...Like laying on a cloud that...smells like Sensei...but that doesn’t bother me at all..."
    mi "Bed...sounds good..."
    ki "And it’s {i}so{/i} big...I bet all three of us could fit on here no problem!"
    mi "Sensei...can I get on the bed too? I also like the way you smell..."
    s "Ask Kirin."
    ki "Kirin..."
    ki "Kirin’s fine with that. We’re just here to have fun, right? And what better way to have fun than...yeah. Kirin’s fine with that."
    mi "Yaaaaay. Here comes the Miku."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene thevaliumscene27
    with dissolve2

    ki "Hey. How do you feel? Do you have to go back to the room?"
    mi "Huh? But we just got here."
    ki "Yeah, but like...how tired are you on a scale of one to ten?"
    mi "Idunno. Like...an eight? But wouldn’t it be kinda rude to just bail on Sensei right after gettin’ here?"
    ki "Not if-"
    mi "I’m fine. Don’t even worry about-"

    scene thevaliumscene28
    with dissolve

    mi "Wait, wait, wait...I get it...You’re just nervous cause you ain’t ever been in a boy’s room before."
    ki "Uhh..."
    mi "Guess you and Karin ain’t so different after all."
    ki "I can guarantee you that is not what’s going on here."
    mi "Omg, you’re like...so cute. I totally had no idea you were this innocent."
    mi "What happened to “Don’t worry, Miku. Leave it all to me.”"
    ki "You...{i}can{/i} leave it all to me. I can handle this. But...I gave you a chance to leave, you know. And if you remember this night at all, you have to remember {i}that{/i} too."

    scene thevaliumscene29
    with dissolve

    mi "Remember what? All we’re doin’ is hangin’ out on the bed. We ain’t done anything yet."
    ki "But if- {i}when{/i} we do, you have to remember that I tried to let you out. Because once things get going, I’m probably not going to reconsider."
    mi "What {i}things?{/i} What are we even doing? I am literally in the dark."

    scene thevaliumscene30
    with dissolve

    ki "Fine. I’m just going to say it. I think we should do something for Sensei."
    ki "It’s clear he likes you since he chose your costume over Uta’s, and this would be a great chance for you to finally get close to him. Like, physically close."
    ki "Plus, I know a {i}little bit{/i} about how this sort of thing works. And doing it with a friend is a lot less scary than doing it on your own the first time."
    mi "Doin’ what? You still ain’t said it."
    ki "{i}Adult{/i} stuff, Miku. Things Sensei was probably going to do with Imani if she wasn’t staying with the girls."
    ki "Don’t you want to be closer to him? Don’t you want to seem more like an adult?"
    mi "Adult stuff?"
    ki "Yeah. Like, sexual stuff."
    mi "You wanna do adult stuff with Sensei?"
    ki "I don’t...{i}not{/i} want to do adult stuff with Sensei. Especially if it means letting him relax and getting you guys closer together in the process."
    mi "Won’t you be getting closer to him too?"
    ki "Stop asking me so many questions. Either do this with me or bail. This is your last chance."
    mi "Sure. I’ll do it."
    ki "See? I knew you weren’t-"

    scene thevaliumscene31
    with dissolve

    ki "Wait...you will?"
    mi "Yeah."
    mi "But under one condition."
    ki "You...have a condition...for {i}me{/i}?"
    mi "Yeah."

    scene thevaliumscene32
    with dissolve

    mi "We’re makin’ it a contest."
    ki "..."
    ki "Seriously?"
    mi "Super seriously."
    ki "That’s a lot of confidence for someone who’s never done this before and is also high."
    mi "I still don’t know what we’re doing. But I know I kicked your ass in the Dorm War last year and I’m gonna kick your ass again this year."
    mi "Floor one forever."
    ki "Uh..."

    scene black
    with dissolve

    mi "Sensei! Come here!"

    scene thevaliumscene33
    with dissolve2

    s "Is your meeting over?"
    mi "Yeah. Kirin thinks we should do adult stuff with you since it might make you like me more."
    mi "Can’t guarantee I ain’t gonna pass out halfway through, but if bestie says we’re doin’ adult stuff with the teacher, Miku ain’t got any reason to refuse."
    mi "One thing, though. I ain’t got any idea what to do. But that’s fine since Kirin said she’ll teach me."
    ki "This..."
    ki "It's too easy..."
    ki "It’s way too easy..."

    scene thevaliumscene34
    with dissolve

    mi "That a surrender I hear?"
    ki "No..."
    ki "It all just..."
    ki "It all feels kind of fake..."
    s "Can I ask what sort of “adult stuff” we’ll be doing?"

    scene thevaliumscene35
    with dissolve

    mi "Ask Kirin. She’s the expert here, not me."
    s "Kirin?"
    ki "Uhh..."
    ki "I guess we can start small and just...jerk you off?..."
    mi "How does that work as a contest? Whoever scores the most cumshots wins?"
    s "That is not how that works."

    "I also should have figured this was going to be a contest the second two girls walked into the room but, up until a minute ago, I wasn’t even sure if it was going to happen or not."

    ki "We’ll just take turns doing it and...he’ll choose a winner when he’s ready."
    mi "It’s settled, then. How do we start? Do I keep my clothes on? Which hand do I use?"
    s "Kirin will handle it. She {i}is{/i} the expert, after all."
    ki "Yeah..."
    ki "Yeah, that’s fine."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene thevaliumscene36
    with dissolve2

    "Both girls drop to their knees at the foot of the bed, but Miku almost falls over in the process as her body and mind aren’t moving at the same pace."
    "Kirin unzips and unbuttons my pants, sliding them down to my ankles before hesitantly reaching for my shaft and angling it up toward her."
    "Miku watches on in awe as it goes from flaccid to erect in less than a minute and Kirin..."
    "Kirin looks away."
    "It’s something I’ve never seen her do before."
    "But that being said, her skills are no different than normal."
    "She lightly massages the head with one hand while gently tugging with the other."
    "And Miku, who appears to be at a loss for words, just continues to watch on."

    mi "Sensei..."
    mi "The heck is that thing?"
    ki "His cock, obviously."
    mi "Is it real?"
    ki "Feels real to me."
    mi "It don’t look real."

    scene thevaliumscene37
    with dissolve

    ki "So, uhh...there isn’t really a manual involved in this sort of thing. It’s mostly just gauging reactions and letting your perverted mind wander."
    mi "Why ain’t ya movin’ any faster?"
    ki "He’s only been hard for like, a minute. Going that fast right now would probably just hurt."
    ki "Plus, a lot of pleasure comes in savoring the feeling. So starting off gentle and getting progressively more, uhh...{i}passionate{/i} is always a good strategy."
    mi "Why do you know so much about this?"
    ki "I...pay attention in health class?"

    scene thevaliumscene38
    with dissolve

    mi "When the heck have we had a health class?"
    ki "Does that...feel good?"
    s "You look extremely uncomfortable right now."
    ki "I {i}am{/i} extremely uncomfortable right now."
    s "Is it because you lured your best friend into an older man’s hotel room while she was high or drunk or...whatever she is right now with every intention of coercing her into performing a sex act?"

    scene thevaliumscene39
    with dissolve

    ki "..."
    s "Or is it because you don’t like how it feels when you remember you actually have a heart?"
    ki "..."
    s "Do you want me to praise you? Or do you want me to ridicule you? Because there are two ways this can go."
    s "I can tell you it feels good...and that you’re doing an amazing job..."
    s "Or I can remind you that you’re pathetic."
    s "And that the only thing that matters to you is using everyone, even someone like Miku, so that {i}you{/i} can feel better about yourself."
    ki "..."
    s "Which one do you want?"
    ki "..."
    s "..."
    ki "I..."

    scene thevaliumscene40
    with dissolve

    ki "Here. Your turn."

    "Coward."

    mi "Woah...when did this get here? How long we been goin’ for?"
    s "Are you sure you’re okay to keep going, Miku?"
    mi "I can’t tell if I’m feelin’ dizzy cause it’s hot in here or if it’s because I’m holdin’ a penis for the first time."
    ki "I’m sure the Valium doesn’t help."
    mi "Stop talkin’ to me...I gotta focus..."
    s "Where did Miku get Valium?"
    ki "From Io. She was about to have a panic attack before she got on stage for the costume contest and we got her high to get her through it."
    s "Was taking advantage of her always part of the plan? Or was that something you thought up afterward?"

    scene thevaliumscene41
    with dissolve

    ki "Maybe {i}don’t{/i} keep saying things like that right in front of her, please?"
    s "She’s in her own little world right now. And if she’s as high as she looks, she’ll probably think that was all some sort of dream anyway."
    ki "I didn’t {i}plan{/i} on taking advantage of her. I just-"
    s "Saw an opportunity to finally do something you’ve been curious about for a very long time?"
    s "Thought it would be okay so long as she didn’t remember?"
    ki "Sensei..."
    s "Show me your tits when you’re talking to me."

    scene thevaliumscene42
    with dissolve

    ki "O...Okay..."
    mi "What was the hand thing Kirin was doin’ again? Was it like this?"

    "Miku’s fake nails dig into the tip of my cock, scratching the skin and causing my body to shiver in a way that I can’t even {i}pretend{/i} is pleasant."
    "And yet, I don’t try to stop her."
    "I’m too busy making someone else feel human."
    "Or {i}inhuman.{/i}"
    "I’m not quite sure which one she prefers."

    s "Are you wet right now, Kirin?"
    ki "Yes..."
    s "Do you like watching Miku jerk me off?"
    ki "Yes?...Maybe?..."
    s "You’re better at it than she is."
    s "Does that make you happy? Being better at something than someone?"
    s "Is that why you try so hard to please me this way?"
    ki "I don’t know..."
    s "Show me. Show me how much better you are."

    scene thevaliumscene43
    with dissolve

    ki "Like this?..."
    mi "Hey...I wasn’t done with that..."
    ki "You..."
    ki "You poor thing..."
    ki "Was Miku too rough with it?...Do you need me to make it better?"
    mi "How come Kirin’s shirt is pulled up like that? I didn’t get the memo sayin’ we could flex our assets."

    scene thevaliumscene44
    with dissolve

    mi "Screw it...I ain’t got much, but here ya go. Ain’t fair if only Kirin gets to cheat."
    ki "Hah...hah...hah...cum for me...cum for me..."
    s "And what? End your misery?"
    ki "No...cum for me because I want your cum...I want it all over me, [kirinmaster]..."
    ki "You were right...I’m pathetic...I brought Miku here to take advantage of her...all I’m good for...is getting you off..."
    ki "So cum...cum for me...cum...please..."
    s "No."
    s "I want both of you at the same time."
    s "It’s only fair after you dragged her here when you should have let her rest, don’t you think?"
    ki "But I’m the filthy one.. I’m the one you should paint..."

    scene thevaliumscene45
    with dissolve

    mi "Let the man make his own decisions. And we didn’t even bring any paint."
    ki "Miku...I’m sorry I dragged you into this...but I’ve been thinking about it forever..."
    ki "I think you’re so cute...so petite and...adorable...I just want to mess you up...I want to mess you up...so bad..."
    mi "Yeah tell me somethin’ I don’t know, ya friggin’ nympho."

    scene thevaliumscene46
    with dissolve

    ki "God...and that costume...fuck...just thinking about Sensei’s big dick in your little pussy makes me want to cum..."
    mi "How long does this normally take? Cause I’m runnin’ outta steam over here."
    s "Just...a little longer..."

    scene thevaliumscene47
    with dissolve

    ki "Hah...yeah?..."
    ki "You’re gonna cum for me, right?..."
    ki "You’re not gonna hold back...you’re gonna give me everything you’ve got..."
    ki "Punish me, [kirinmaster]...Punish me!"
    mi "Kirin makes a good argument, but I’m gonna counter it by sayin’ this..."
    mi "{i}Fuck{/i} Kirin. I wanna win. That’s my argument."
    s "Open your mouths."

    scene thevaliumscene48
    with dissolve

    ki "Mmm...yes, [kirinmaster]...whatever you want..."
    mi "Aaaahhhhnnn~"
    mi "By the way, how’s this stuff supposed to taste?"

    "The two of them continue jerking my cock, each with different speeds and motions, which makes for a rather...unique experience that I, once again, can’t really pretend feels {i}good.{/i}"
    "But I’m close enough at this point that it doesn’t really matter either way."
    "What does matter, however...is choosing a victor."
    "And right now, the girl I want to cum for is..."

    menu:
        "Miku":
            s "Kirin...back off."
            s "Miku deserves this. And there’s no better punishment for you than giving everything you want to {i}her{/i} and making you watch."

            scene thevaliumscene49
            with dissolve

            $ dorm1war2points += 1
            $ mikuwarhjwin = True

            ki "But you said I was better...so why-"
            mi "Ahn...ahn...sounds to me like...somebody’s a sore loser..."

            "Miku’s handjob becomes a lot clumsier in its final moments, which is not surprising considering she’s also multitasking by licking the tip of my cock as well."
            "But as Miku’s eyes remain closed, I feel obligated to look at Kirin- who refuses to break eye contact for even a moment."
            "This makes it ten times more pleasurable when I finally ejaculate right before her eyes..."

            with sexfade
            with sexfade
            scene thevaliumscene50
            with cumflash
            with hpunch

            mi "Mmf! Geh!"

            scene thevaliumscene51
            with dissolve2

            mi "Okay, now what?"
            s "There is no “now what?” You won."
            mi "Yeah but how do I get this off of me? I can’t open my eyes and if I keep ‘em closed any longer I’m gonna fall asleep."
            ki "I’ll get you some tissues..."

        "Kirin":
            s "Miku...step aside. Kirin wins."

            scene thevaliumscene52
            with dissolve

            $ dorm2war2points += 1
            $ kirinwarhjwin = True

            mi "No way! I demand a recount!"
            ki "Mm! Thank you...[kirinmaster]...thank you so much!"
            ki "Don’t hold back..I’ll drink every last drop..."
            mi "I woulda studied if I knew this was coming! And no! That metaphor was not intentional!"
            s "That...was a pun..."
            mi "Whatever! Same thing..."
            ki "Pay...attention...to me!"

            "Kirin diverts all of her focus to the end of my cock as she presses it against her tongue, hoping to get a mouth full of semen."
            "Choosing her wasn’t very hard, to be honest."
            "Not only is her technical skill light years ahead of Miku, but she was actually {i}into it.{/i}"
            "And the way she came humming back to life as soon as I called her on her shit was perhaps the best part of my day."
            "But it doesn’t change the fact that she was willing to do something despicable..."
            "That she {i}did{/i} do something despicable...and that I helped her do it."
            "But that’s fine."
            "Because there’s no guarantee Miku will remember this in the morning."
            "And while that doesn’t make taking advantage of her {i}okay-{/i}"
            "It makes it a hell of a lot safer."
            "And I’m already taking advantage of these girls to begin with."

            ki "[kirinmaster]...[kirinmaster]!"

            with sexfade
            with sexfade
            scene thevaliumscene53
            with cumflash
            with hpunch

            ki "Mmngh! Mmnn........mmph......"

            scene thevaliumscene54
            with dissolve

            ki "{i}*Gulp*{/i}"
            mi "Gross."
            ki "I know."
            ki "Perfect for someone like me."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "........."
    "......"
    "..."

    scene thevaliumscene55
    with dissolve2

    ki "Falling asleep standing up."
    ki "If only she’d have done that forty five minutes ago."
    s "Do you regret it?"

    scene thevaliumscene56
    with dissolve

    ki "Do you regret what you did to Molly?"
    s "..."
    ki "..."
    s "I didn’t do anything."
    ki "Yeah."
    ki "And neither did I."

    scene thevaliumscene57
    with dissolve

    ki "Come on, Miku. Let’s get you to bed."
    mi "Hm? Oh...yeah..."
    mi "Night, Sensei..."
    mi "Hope ya...had fun..."
    s "..."

    scene black
    with dissolve2

    s "Goodnight."

    play sound "dooropen.mp3"

    "The two of them exit the room and I remove my phone from my pocket to find a flurry of text messages from essentially everyone."
    "I ask myself if it was worth it as I climb into bed...or if I should try and head back to the bar to see if anything is still happening."
    "But instead-"
    "I find myself wondering if Kirin would be any different if she never met me."

    s "..."

    "I think that she would."

    $ renpy.end_replay()
    $ kirinlust30 = True
    $ kirin_lust += 1

    "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
    "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo19

label kirinspecial40:
    scene nightsky
    with fade
    play music "noriko.mp3"

    "The stars are shining, the air is cool, and I’m on my way to a distant convenience store to bother a girl who is more than likely thinking about having sex with me right now."

    scene kirinwalkhome1
    with fade

    "There must be some sort of special tonight, though, as I get two for the price of one the moment I arrive."

    s "Just out of curiosity, are you two ever {i}not{/i} together?"
    n "Not really. Kirin follows me around a lot."
    n "She’s kind of like a horny puppy who keeps trying to hump my leg."
    ki "I have no other options when she won’t let me hump her face."
    s "Keep at it, Kirin. You’ll get your wish one day."
    ki "He says, not realizing it is {i}he{/i} who prevents my wishes from coming true in the first place."
    n "Are you here to see me, Sensei? Or are you just passing by on your way to hang out with Tsuneyo again? Answer honestly. I promise I won’t get jealous when you tell me it's the latter."
    s "I’m actually here for Kirin. I installed a GPS tracking device on her phone when she wasn’t looking and I can now pinpoint where she is at all times."
    ki "I know that’s supposed to creep me out, but I kind of like it."
    n "You’d have to figure out the passcode to her phone before you could do that, wouldn’t you?"
    s "Is it 6969?"

    scene kirinwalkhome2
    with dissolve

    ki "Aww. It’s always so cute when you unintentionally remind me of how close we are."
    n "Hey! We have the same passcode! Now we can spy on one another and go through each other’s camera rolls!"

    scene kirinwalkhome3
    with dissolve

    ki "Wow, good idea! I definitely haven’t already gone into your phone and sent myself copies of the nudes you sent Sensei!"

    if kirinlust20 == True:
        n "I saw one of yours too, but I don’t know if it was for him or your sister. You have really nice nipples."
        ki "Thank you, Noriko! It was for Sensei."
        s "Can you please not throw me under the bus every chance you get? It’s starting to wear me down."
    else:
        n "I didn’t find any in your phone. I was actually really surprised. Tons of porn, though. I didn’t realize you had such a thing for twins."
        ki "It’s kind of sad how I can pinpoint exactly when you must have looked at my phone by the porn you found. "
        n "A little, yeah."

    scene kirinwalkhome4
    with dissolve

    ki "Anyway, assuming the GPS tracker thing is true, which I kind of hope it is...are you {i}actually{/i} here to see me?"
    s "No. I’m here for Noriko. How would I have even known you were here?"

    scene kirinwalkhome5
    with dissolve

    ki "Ugh, that was such an easy opportunity for you to earn points with me and you completely squandered it. "
    n "It earned plenty of points with me!"
    ki "Cool, but what the fuck is he going to do with them when you’d already do literally anything he asks?"
    s "Would you not? Because I’m pretty sure you were in that same boat before I even met Noriko."
    n "{i}Re-{/i}met Noriko. Don’t forget the years and years I spent secretly being in love with you."
    ki "There’s a clear difference there, Sensei. I would do anything you ask me to do because I am a horrible, deviant person. {i}Noriko{/i} would do anything you ask because she is your pet."
    n "That’s what the collar’s for, you know. There’s a slot on the back you can attach a leash to. I keep the one that came with it in my underwear drawer."

    scene kirinwalkhome6
    with dissolve

    ki "Oh, is {i}that{/i} what that was? I thought it was a belt."
    n "Stop taking my panties, Kirin."
    ki "Why? I always put them back."
    s "Ignoring the fact that Noriko might actually be a dog and the equally unsurprising fact that Kirin will do anything to get herself off, it’s nice seeing you two so {i}together{/i} all the time."
    s "Most people would think that two roommates would struggle balancing a shared sexual connection with one guy without their feelings starting to get in the way."

    scene kirinwalkhome7
    with dissolve

    ki "Maybe. But I don’t have feelings for you. That’s Noriko’s thing. I’m the cool sex friend you secretly invite on business trips and bone on the side."
    n "Also, even with you and me teetering off the precipice of finally making our genitals touch, as well as my infallible desire to have my first time with you be private-"
    ki "With a special exception made for her best friend."
    n "No. But, as I was saying, even with that we’re probably, like...the second or third dorm room closest to having casual threesomes with you!"
    s "Is this like Uta’s “Sensei love journal” thing? Are you two ranking the sexual stuff while Uta ranks how much I care about everyone?"
    ki "What else are we supposed to do in class? You don’t make us work."
    n "There’s some disagreement on who we have for first place, though. My money’s on Dorm 7. In fact, I’d be really surprised if Uta & Io aren’t already screwing around together."
    s "And what-"
    ki "Makoto and Miku and it’s not even close."

    scene kirinwalkhome8
    with dissolve

    n "But they’re the only dorm room that’s completely straight. I’ve confirmed at least one bisexual member of every other room."
    s "What? How?"

    scene kirinwalkhome9
    with dissolve

    n "I asked."
    s "Damn. If only Rin had that idea."
    n "Dorm 2 and Dorm 9 have both {i}technically{/i} not admitted to anything indicating a break in pure heterosexuality thus far, but that is subject to change based on progression throughout the year."
    n "I remain steadfast in my predictions of both Sana’s lesbian awakening as well as Yasu’s pansexual one."
    ki "It’s really surprising just how much a room can accomplish when both of the girls in it were born without filters."

    scene kirinwalkhome10
    with dissolve

    n "It also helps that pretty much everyone likes me and doesn’t mind telling me stuff. "
    ki "I don’t have any exceptional social abilities like Noriko does, but I’m pretty sure my drive and thirst for sexual knowledge help in some way too."
    s "Not like I’m complaining, but do you two ever talk about anything that {i}isn’t{/i} sexual?"
    ki "..."
    n "..."
    n "We go to the movies sometimes?"

    scene kirinwalkhome11
    with dissolve

    ki "Oh, speaking of which, I should probably start heading back. I have to stop at home to watch some stupid fucking video with my parents."
    n "It’s not one of those “Pray the gay away” things, is it? Because I watched some documentary last night about homosexuality in Japan and what some of those parents do is fucking wild."

    scene kirinwalkhome12
    with dissolve

    ki "God, I {i}wish.{/i} At least that sounds entertaining. We’re watching their stupid fucking wedding video. They make a whole thing out of it every year and we all have to watch it together."
    ki "Everybody always fucking cries and talks about how cute it is and blah, blah, blah. Weddings are stupid. I’m never getting married. It looks exhausting."

    if kirinmarry == True:
        s "Really? Even after I chose you in that fuck, marry, kill game?"

        scene kirinwalkhome13
        with dissolve

        ki "Wh...Why do you even remember that?! That was so long ago! And was literally just {i}a game!{/i} There’s no way we’re ever actually getting married!"
        ki "Can you seriously picture {i}me{/i} gathering kids up and making hot chocolate while we all sit around and pull from the same box of tissues?!"
        s "I imagine that same scene every night...It’s the last thing I think of before going to sleep."

        scene kirinwalkhome14
        with dissolve

        ki "S...Shut up! No it’s not!"
        n "Uhh...well ignoring Kirin’s thoughts on marriage, why don’t you take this chance to walk her home?"

    else:
        s "Never?"

        scene kirinwalkhome15
        with dissolve

        ki "Do {i}you{/i} want to get married?"
        s "No...but you’re not me. You’re in high school."
        s "For all we know, this whole rebellious thing of yours could end any day now and you could turn into another Karin but...with smaller boobs and more sexual experience."
        ki "That’s the single dumbest thing you’ve ever said."
        n "Ignoring Kirin’s thoughts on marriage, why don’t you take this chance to walk her home?"

    scene kirinwalkhome16
    with dissolve

    ki "Hm? Why? I can walk myself home. I do it all the time."
    s "Are you sure? You don’t want to, you know, use this time to {i}be alone?{/i}"
    n "I’ve gotta do inventory tonight. I’ve been slacking off way too much lately and having you around will just make me slack off even more."
    s "I mean...okay. If it’s fine with Kirin, I can walk her home."

    scene kirinwalkhome17
    with dissolve

    ki "It’s fine with me. All the homeless people around here creep the fuck out of me anyway. But if you try to hold my hand, I’m going to make you walk five steps behind me."
    s "When have I literally ever tried to do that before?"
    ki "When have you ever been nice enough to walk me home before? I normally just blow you and leave."
    s "In my defense, this was Noriko’s idea."
    n "Yeah. Sorry for forcing you two who definitely don’t like one another together. I’ll think harder about my choices next time."

    scene kirinwalkhome18
    with dissolve

    ki "What are you talking about? Of course I like Sensei."
    ki "I just happen to like his penis more."
    s "Which is fair. That is my greatest feature, after all."
    n "Call me when you get home? I can put you on speaker while I count boxes of Twinkies."
    s "It’s a date."
    ki "And this is exactly why I don’t date. You two are gross."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "Kirin and I exit the convenience store together and take off in the direction of her parents’ house."
    "The homeless are out in full force tonight."
    "Thankfully, “full force” for them just means leaning up against chain-link fences and staring at us as we move through the streets."
    "There’s one person in particular, an old woman with grayed-out hair and several missing teeth, who opens her mouth and shouts something incoherent at us."
    "Kirin jumps."
    "It’s the first time I’ve ever heard any of them speak, if you could even call that indiscernible cry “speaking.”"
    "And so I misinterpret it as a desperate plea for help and lose myself for a moment, turning back toward her to stare once more."
    "She yanks out one of her few remaining teeth and throws it at me."
    "It lands at my feet, covered in blood and what I assume is gum-residue."
    "Kirin never notices."

    play sound "static.mp3"
    scene kirinwalkhome19 with flash
    play music "justlights.mp3"
    stop sound

    "But then we make it to a riverbank and things begin again."
    "The silence and unease disintegrates, leaving nothing but the two of us and a fading crooked skyline comprised of abandoned apartment buildings, decorating the murky water with reflections of the past."
    "Within them, if I focus hard enough, I can see into the windows."
    "And in those rooms, now devoid of everything, were people."
    "Some were eating, some were dancing-"
    "But all of them were blind."
    "I could tell by the lack of irises."

    ki "So, was I right?"
    s "Right about what?"
    ki "Makoto & Miku, obviously. Have you three taken the plunge yet? What’s Makoto like in bed?"
    s "Is this really what we’re going to talk about?"
    ki "If we talk about anything else, we might accidentally enjoy ourselves."
    s "And that would be bad...why?"

    scene kirinwalkhome20
    with dissolve

    ki "Well, it wouldn’t be right to steal Noriko’s thunder right when you two are...how did she word it again? “On the precipice of making your genitals touch?”"
    s "Yeah, I have no idea why she put it that way."

    scene kirinwalkhome21
    with dissolve

    ki "Because she’s nervous. I’m pretty sure her heart hasn’t stopped palpitating ever since she dry-humped you on the beach."
    ki "Which reminds me, I’m mad at you."
    s "What? Why?"
    ki "A few reasons."
    ki "Not only did you totally butcher Noriko’s big moment by bailing on her to go see someone else, but you neglected to tell me that you made it to third base with Miku."
    s "Oh yeah. Surprise."
    ki "Yeah. {i}Surprise.{/i}"

    if kirinlust30 == True:
        ki "You toyed with me on purpose when I brought her to your hotel room."
        ki "You {i}knew{/i} that I wouldn’t feel bad if I’d known you two had already started messing around."
        ki "So you took advantage of me and made me feel like shit. I won’t forget that."
        s "Well, excuse me for exposing your humanity. I didn’t realize you were so opposed to it."
        ki "No, I think you’re misunderstanding something. Yes, I’m mad. And yes, that is in large part to you taking advantage of me, but it’s not like there was no...unexpected benefit that came from it."
        s "Like?"

        scene kirinwalkhome22
        with dissolve

        ki "Well, for one, I think I might have a humiliation kink now."
        ki "But the more impactful part is that all of those things you said made me feel...different."
        ki "It’s not often I feel genuinely bad about the things that I do. But Miku has always been a thing in my life that I’ve truly wanted to protect."
        s "You mean when you're {i}not{/i} taking advantage of her for being high, right?"
        ki "Yeah, exactly."
        ki "There’s a lot of stuff I “almost” go through with. And that night, I was probably hoping she would have talked me out of it."
        ki "You see, when things become too real, I normally still have an {i}out.{/i} And once she agreed, my choices were to either admit that I’m weak or just go along with it."
        ki "As you saw, I went along with it."

        scene kirinwalkhome21
        with dissolve

        ki "You made me pay for that. And, while I’m mad, I appreciate it."
        ki "I didn’t think you had it in you."

        scene kirinwalkhome23
        with dissolve

        ki "But, then again, I didn’t think Miku had it in {i}her{/i} to let a grown man finger her and here we are."
        ki "Maybe I’m less special than I thought?"

    s "Well, the Noriko thing I can understand. I feel bad about that as well. But I fully intend to make up for it soon."

    scene kirinwalkhome24
    with dissolve

    ki "Don’t fuck her just to “make up for it.” She’s not me. She won’t be able to separate sex from the more mushy, emotional parts of it."
    s "That’s not-"
    ki "Just say “okay.” I don’t want to get any more involved in your Romeo & Juliet bullshit than I already am."
    s "Can I comment on the Miku thing, at least?"
    ki "Yes, because that I {i}do{/i} want to get more involved in."
    ki "Were you keeping it a secret on purpose? Or did you just not think it was important enough to tell me about it?"
    s "Honestly? I didn’t think about it at all."

    scene kirinwalkhome25
    with dissolve

    s "I appreciate your “drive and thirst for sexual knowledge” or whatever, but that doesn’t mean I’m going to hand-deliver all of my new sexual encounters to you so you can rate and review them."
    ki "Not even the ones with people who are important to me?"
    s "You’ve proven there’s no issue getting that information from those people directly, so I don’t really see what {i}me{/i} being the one to tell you instead of them accomplishes."
    ki "You don’t?"
    s "No, I really don’t."
    ki "You {i}really{/i} don’t understand why I’m mad about you keeping the Miku thing a secret from me?"
    s "It’s not because you still like her, is it? I thought you got over that a while ago?"
    ki "I love Miku, but I don’t {i}like{/i} her. Like, don’t get me wrong, I would do {i}heinous{/i} things to that little tomboy if given the opportunity, but that’s not why I’m upset."
    s "Then why-"
    ki "Because it’s {i}both{/i} of you."
    s "What?"

    scene kirinwalkhome26
    with dissolve

    ki "Listen, I am {i}not{/i} the kind of girl who’s going to go on some long-winded rant about what you mean to me or my {i}feelings{/i} or any of that stuff because-"
    ki "Well, frankly, all of that makes me {i}way{/i} more uncomfortable than anything involving sex ever will."
    ki "But when two people that I’m close to hook up in a way I can understand and relate to and feel {i}good{/i} about...not telling me is like, robbing me of that happiness or whatever."

    scene kirinwalkhome27
    with dissolve

    ki "Like I said, I suck when it comes to explaining things like this. It would have been way easier if I could’ve just blackmailed you about it instead or something."
    ki "When it comes down to it, I’m happy for you two. What I’m upset about is not being included in something I thought I {i}would{/i} be included in."
    ki "Like, I feel like {i}I’m{/i} making a bigger deal out of this development than either of you are and that’s like, totally weird for me."
    s "I think the weirdest part of all is how you’re able to root for both Miku {i}and{/i} Noriko without feeling like you have to choose sides."

    scene kirinwalkhome28
    with dissolve

    ki "Yeah...but as long as you’re able to keep things under wraps, which you’ve been pretty good at so far, I think everyone might be able to walk away when this is all said and done without getting hurt."
    s "Fortunately, I don’t think that’s much of an issue with Miku as she seems to be entirely open to me being with...literally everyone that I want to be with."

    scene kirinwalkhome29
    with dissolve

    ki "Yeah, what’s up with that? I got that same vibe on the beach and it, like...totally threw me for a loop."
    ki "You don’t think she accidentally picked that up from me, do you?"
    s "Probably not, Kirin."

    scene kirinwalkhome30
    with dissolve

    ki "Hey, how can you be so sure? For all we know, I might be a major role model for her on her way to sexual addiction."
    s "Probably because Miku is {i}actually{/i} okay with me seeing other people and you’re just pretending to be."

    scene kirinwalkhome31
    with dissolve

    ki "I’m...what?"
    ki "Why would you say that? That’s not true. That’s definitely not true. Where did you get that idea?"
    s "Well, let me ask you this-"
    s "If I asked you to abandon everyone and everything else to run away with me right now, would you?"
    s "We could fuck a million times a day...and “watch the world burn” or whatever it was you said when we first started hanging out."
    s "If I gave you the chance to have me all to yourself, would you take it?"
    ki "..."
    s "..."

    scene nightsky
    with dissolve2

    ki "Yeah."
    ki "We should do it."
    ki "We should leave everyone...and everything else behind."
    s "It was a hypothetical question, Kirin. I’m not actually asking you to do this with me. I just wanted to prove a point."

    scene kirinwalkhome32
    with dissolve2

    ki "Why does it have to be hypothetical?"
    ki "If we can make a world for ourselves amidst all of this shit...why don’t we just do it?"
    ki "What’s stopping us?"
    s "We probably care more about other people than we let ourselves believe."
    s "You and I are similar in that way. We don’t like admitting to things we think are weaknesses, but the fact we think of them as weaknesses at all is confusing."
    ki "Am I not enough for you?"
    s "..."
    ki "..."
    s "I don’t think you are."
    ki "..."
    s "Am {i}I{/i} enough for {i}you?{/i}"
    ki "..."
    s "..."
    ki "Do you..."
    ki "Maybe want to hold hands on the way home?"
    s "..."
    ki "Just because it would be, like...ironic. For {i}us{/i} to do that, I mean. Since we’re just not the type and whatnot."
    s "..."
    ki "..."
    s "Not really."
    ki "Y...Yeah! Me neither, obviously. That was just a joke anyway. As if {i}we{/i} would..."
    ki "Ever do..."

    scene black
    with dissolve2

    ki "Are you sure?..."

    "I’ve always been weak, so I let her get the better of me three times before the night comes to an end."
    "The first is when I take her hand at the edge of the riverbank."
    "The second is when she takes my arm beneath a crumbling overpass."
    "The third is when I take her lips just outside her parents’ home."
    "As I walk away, I recall a recent reflection."
    "I recall bodies in windows and eyes without irises."
    "And I tell myself it matters not if those who peer through glass are blind at all."
    "What matters is what they think about the things they see."
    "And what those thoughts could do to me."

    $ renpy.end_replay()
    $ kirinspecial40 = True
    $ kirin_love += 1
    stop music fadeout 7.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label kirinspecial45p1:
    scene noonsky
    play music "summerwind.mp3"

    "And so another day of actually working hard at the job I actually care about comes to an end."
    "I say that almost unironically, as I actually {i}did{/i} contribute in some form to the greater good after the last bell rang today."
    "With Imani and Makoto busy at swim club and the club that I'm meant to advise being mostly fine without any form of supervision, there was no one left to grade the papers my subordinates assigned but me."
    "Needless to say, everyone received an A+ regardless of whether or not they deserved one and now my wrist hurts from having to write and circle that twenty times."
    "So, what better place to go from here than a location where everyone {i}else’s{/i} wrists hurt as well?"

    scene kirinarcade1
    with dissolve2

    "See: the archery range. Or, as I like to refer to it — probably the only club that actually does club stuff instead of just fucking around."
    "You’ll have to peer past the soul (and cock)-sucking entity in front of you to see it, but I can assure you it is there."
    "And that it is filled with girls who are unintentionally training themselves to become better at giving me handjobs one day."

    ki "Hey. You haven’t gone home already?"
    s "The one speaking to me now is already good at giving handjobs. But I’m looking forward to seeing how much she improves as the days go by."

    scene kirinarcade2
    with dissolve

    ki "Thanks! Though, I think you might have accidentally said that out loud instead of keeping it to yourself."
    s "No, I just knew there wasn’t a need to keep it inside anymore as having my innermost thoughts heard by you won’t really change the way either one of us thinks."
    ki "That’s fair. And if it gets you to say nice things about me more often, I’m totally cool with it. "
    ki "What are you doing over here? You know Miss Watabe doesn’t like you interrupting practice."
    s "I’m pretty sure she doesn’t like you leaving in the middle of it either. It looks like everyone else is still out there."

    scene kirinarcade3
    with dissolve

    ki "Yeah...I’m kind of bailing while she’s not paying attention to me. I wasn’t feeling it today."
    s "Don’t tell me you’re already giving up on {i}this{/i} club too?"

    scene kirinarcade4
    with dissolve

    ki "I’m not “giving up.” My relationship with kyudo is totally different from my relationship with soccer since this is something I actually chose and didn’t just...get sucked into."
    s "Why leave then? What aren’t you {i}feeling?{/i}"

    scene kirinarcade5
    with dissolve

    ki "Uhh...good enough, I guess?"
    s "So it’s the same thing as soccer, just in a slightly different way."
    ki "It’s still different. This is just me getting in my own head."

    scene kirinarcade6
    with dissolve

    ki "That’s the thing with kyudo, though. It’s like 80%% mental and 20%% physical. Even super old people can be really good at it since the mechanics aren’t that demanding."
    s "So basically, you’re even more screwed than you were in soccer."

    scene kirinarcade7
    with dissolve

    ki "Nuh-uh. Why would I be screwed? All I have to do is just convince myself I’m better than I actually am and I’ve been doing that in pretty much every area of my life for as long as I’ve been alive."
    s "Like how you still won’t admit you’re actually in love with me."

    scene kirinarcade8
    with dissolve

    ki "Exactly! See? You get it."
    s "Cool, so I’ll just take that as your admission and we can move onto dating for real."
    ki "Cool! Sounds good."
    s "That was a joke, Kirin."

    scene kirinarcade9
    with dissolve

    ki "So was mine. I don’t actually love you. I just want you to {i}think{/i} I love you since holding your hand the other night felt kind of nice."
    ki "Also, Karin saw us kiss. Whoops."
    s "Wait...she did?"
    ki "No. I just wanted to see what kind of face you’d make. And judging by the one I got, I think it’s safe to say you want to fuck my sister."
    s "I think it’s safe to say you already knew I wanted to fuck your sister. "
    ki "Yeah, but now I {i}really{/i} know."
    s "What’s getting into you, Kirin? I’m not going to stop you from leaving, but I’d at least like to know what’s going on."
    ki "Kind of like how I would have liked to know what was going on while you were fingering Miku?"
    s "Exactly like that. You are being given an opportunity right now to prove how much better than me you are at something. And that’s like, your whole thing."

    scene kirinarcade10
    with dissolve

    ki "Hah...fine."
    ki "It’s Uta. She’s too good already."
    ki "I thought joining a club like this would be the best way to sort of...get ahead of everybody else. I thought I’d finally get to be the good one if I put in the work."
    ki "Last thing I expected was for someone to have experience already. It’s fucking kyudo, not soccer."
    ki "I swear, it’s like every single club has some sort of prodigy in it. "
    s "Not the swim club. They-"
    ki "Karin’s in the swim club."
    s "Oh. Yeah."
    s "Well, Karin’s just good at everything, so..."
    ki "Yeah...you don’t have to remind me."
    ki "That’s really all it is, though. I was gonna go home and watch some videos to study that way, but..."

    scene kirinarcade11
    with dissolve

    ki "Do you maybe wanna...hang out for a little while instead?"
    ki "Like...in a...{i}non-{/i}sexual way or...something?..."
    s "..."
    ki "..."
    s "Let me feel your forehead. I think you’re sick."

    scene kirinarcade12
    with dissolve

    ki "It’s not like that! We just...don’t {i}always{/i} have to do that stuff, you know?!"
    s "How hard is it for you to say all of this right now?"
    ki "You have no fucking idea. But I’m serious. Let’s, like...go bowling. Or...go to the arcade or something. Anywhere with air conditioning is fine, really. I just don’t want to be outside."
    s "Don’t you have other friends for stuff like that? I’m the sex guy, remember? That’s the whole point of our relationship."

    scene kirinarcade13
    with dissolve

    ki "Oh...yeah. I guess I could...call Noriko or-"
    s "Kirin, I’m joking."

    scene kirinarcade14
    with dissolve

    ki "You are?!"

    scene kirinarcade15
    with hpunch

    ki "I mean...uhh...you are?"
    s "Were those just stars-"
    ki "No. Anyway, arcade? Let’s go to the arcade. I like the arcade."

    scene kirinarcade16
    with dissolve

    ki "The arcade is really cool. It’s a place where all kinds of people who aren’t even dating go to hang out."
    ki "Which doesn’t mean that people who {i}are{/i} dating aren’t allowed there, but- hey. What are you just standing there for? We’re going to the arcade."
    s "You’re really funny when you try to act like a normal girl, Kirin."
    ki "I’m...plenty normal when I want to be! It’s your fault you’re only just seeing that now!"

    scene black
    with dissolve2

    "Thanks to the location of the archery range being a bit of a walk from the main building and clubs still ongoing, we manage to make it off of school grounds without bumping into anyone else."
    "Well, anyone else we {i}know{/i} at least. There are plenty of other girls who see us together and, while Kirin pretends to know who some of them are, I’m almost certain it’s a bluff."
    "It’s pretty clear at this point that she doesn’t have any friends outside of the class and, if she does, I’m sure it’s all on a superficial basis."
    "Plus, I’m not too worried about what anyone will think at this point since I leave school with Ami and the others all the time and no one’s said anything yet."

    scene kirinarcade17
    with dissolve

    "There’s also the fact that arcades are {i}full{/i} of teenagers after school lets out, and it was obvious from the get-go that we’d be trying to blend in with them."
    "After Kirin drops her stuff off in a nearby coin-locker, we make our way into a small, unfamiliar arcade that is, expectedly, filled with other girls from the school."
    "Some of them look at me, probably because I have a penis, but it’s never for more than a few seconds before they carry on with their business. "
    "Meanwhile, Kirin spends at least 2,000 yen trying to pull a blue turtle out of a glass box."

    scene kirinarcade18
    with dissolve

    ki "Fuck!"
    s "Wow, Kirin. This sure is fun."

    scene kirinarcade19
    with dissolve

    ki "For your information, it wasn’t my intention to repeatedly fail. I’m normally pretty good at these types of games. But at this point, Sensei, I have a vendetta and we can not leave until the Squirtle is mine."
    s "That is not a good name for whatever that thing is."
    ki "You know what fucking Pokemon are. Stop pretending you were born in like...the mid-Showa period. It’s weird and you’re cool enough without acting all oblivious and shit."
    s "No one can ever be cool {i}enough,{/i} Kirin. But thank you for acknowledging my mysterious air of...mystery."
    ki "Stop cherry-picking the good things out of my insults and just help me already."
    s "How? Do you want me to turn this into a scene from a rom-com and grip the joystick with you? Move in for a kiss as we pull a weird blue turtle out of a machine?"

    scene kirinarcade20
    with dissolve

    ki "What kind of rom-coms are {i}you{/i} watching? "
    s "None. I’ve already made it apparent today that I’m too cool for them."
    ki "I just wanted you to stand on the other side of the machine and check my angles, not {i}kiss{/i} me in front of like, twenty other girls."
    ki "You want to do that, go for it. It’s your death sentence. Not like I have anything to lose from kissing a teacher."
    s "Except, you know, the respect of your classmates and whatever sort of reputation you’ve built for yourself."

    scene kirinarcade21
    with dissolve

    ki "Woo boy. Reputation and respect. Yippee. "
    ki "You want to know what my reputation is, Sensei? It’s “Karin’s sister.” If anything, making out with a teacher in broad daylight would help put me on the map."
    s "It would help put {i}me{/i} in jail."
    ki "As long as I get my Squirtle, I don’t really care."
    s "You’d have much more success in that regard if we were in my bedroom."

    scene kirinarcade22
    with dissolve

    ki "Was that...supposed to be a squirting joke? I don't even do that."
    s "Cool joke though, right?"

    scene kirinarcade23
    with dissolve

    ki "Yeah, Sensei. Super-"

    scene kirinarcade24
    with dissolve

    ki "FUCK!"
    ka "Kirin? Is that you?"

    scene kirinarcade25
    with dissolve

    ki "Heh?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene kirinarcade26
    with dissolve2

    ka "What happened? Aren’t you supposed to be at archery club?"
    ki "Uhh...aren’t {i}you{/i} supposed to be at swim club?"
    ka "It was cancelled after Ayane accidentally killed the janitor. We have the rest of the day off now."
    s "How does she keep doing that and why isn’t anyone suspicious of it?"

    if karinlied == True:
        scene kirinarcade27
        with dissolve

        ka "Ah! Sensei! Hi! I’m Karin! It’s nice to meet you!"
        ka "Again!"
        s "..."
        ka "Kirin, take over. I messed up."
        ki "How are you still this nervous around him? Haven’t you two, like, literally gone on a date together?"
        s "She wasn’t much better during that. "
        s "She {i}was{/i} adorable, though. But Karin is always adorable, so-"

        scene kirinarcade28
        with hpunch
        play sound "thump.mp3"

        ki "And down she goes."
        ka "I’m okay! Don’t mind me!"
        s "Yeah, I had a feeling that was going to happen."

        scene kirinarcade29
        with dissolve

        ka "Haha! Floors! Am I right?!"
        ki "You need, like...serious, psychiatric help."

    else:
        scene kirinarcade30
        with dissolve

        ka "Oh...Sensei..."
        ka "You’re here too..."
        ki "What’s up with that reaction?"
        ka "What reaction? I’m just...happy you two are..."
        ka "Uhh..."

    scene kirinarcade31
    with dissolve

    ka "A-Anyway! Is everything...you know...working out over there? In your new club?"
    ka "Because it’s a little lonely not having you around anymore and...if you ever want to maybe, like...spend more time together..."
    ki "Things are fine. I’m just taking a little time off. I’ve been there way more than the other girls lately and Miss Watabe said I should rest my wrist for a little while so I don’t mess it up."

    "Kirin lied as naturally as she breathed."

    scene kirinarcade32
    with dissolve

    ka "Really?! That’s great! "

    scene kirinarcade33
    with dissolve

    ka "I was so worried you wouldn’t fit in there since you’ve always been with Miku and me. But to hear that everything is going well is-"
    ki "Yup. All good. Don’t need to be checked up on. Thanks, Sis."
    ka "..."
    ki "..."

    scene kirinarcade34
    with dissolve

    ka "Okay...well, I...made plans with a friend, so...I’ll leave you alone now."
    ka "Are you coming home for dinner? You don’t have to if you don’t want to, it’s just...it’s my turn and...I want to...know how much to make..."
    ki "Uhhh, not sure. You can make some for me and I’ll just reheat it if I swing by later."
    ka "Okay..."
    ka "Guess I’ll just...see you later then."
    ki "Yup. See you."

    scene kirinarcade35
    with dissolve

    "Karin leaves without saying goodbye to me, but I’m not about to berate her for it when Kirin, as always, is basically the one who {i}forced{/i} her away."

    s "Why not go hang out with her instead?"

    scene kirinarcade36
    with dissolve

    ki "Because {i}we’re{/i} hanging out. She said she made plans with a friend anyway. I’d just be getting in the way."
    s "I think Karin would be more than happy to have you tag along."
    ki "That’s nice. But it doesn’t change the fact that I’d rather be with you."
    s "Why though? You can be with me whenever you want."
    ki "No. I can be with {i}Karin{/i} whenever I want. Getting to spend time with you after school is like winning the lottery. Obviously I’m gonna cash in."
    ki "Karin could be, like...delivering a baby or pulling a cat out of a tree and she’d immediately stop doing either of those things if I asked her to come hang out with me."
    ki "Actually, she’d probably finish them first because she’s Karin and she’s fucking perfect and good at everything and wholesome and everyone likes her."
    ki "But, my inferiority complex aside, I can’t do that with you. Your time is spread too thin between all of the other girls who want your fat dick inside of them."
    ki "Which isn’t to say that’s {i}all{/i} I want, of course. It’s just..."

    scene kirinarcade37
    with dissolve

    ki "Well, you said it yourself the other night."
    ki "“I’m not enough for you.”"
    ki "So, like...it got me thinking...how do I {i}become{/i} enough?"
    ki "It’s gotta be this, right? Spending time together and seeing if we’re compatible in ways where we keep our clothes on instead of just resorting to sex."
    s "..."
    ki "..."
    s "Kirin, are you {i}growing?{/i}"

    scene kirinarcade38
    with dissolve

    ki "Am I? I thought I stopped."
    s "No, as a person."

    scene kirinarcade39
    with dissolve

    ki "Oh. Maybe. I don’t know."
    ki "I’m trying not to think too much about it because that’s the same exact problem I’m having with kyudo."
    ki "I just want to hold your hand more. "
    ki "And the thought of other girls holding your hand is starting to piss me off."
    s "But...the thought of me fucking them, isn’t?"
    ki "Weirdly enough, the hand thing pisses me off more."
    ki "They both kinda suck, though. But until I’m-"
    s "Stop groping yourself. It’s getting distracting."

    scene kirinarcade40
    with dissolve

    ki "But until I’m “enough” for you, there’s not really anything I can do about that."
    s "..."
    ki "You were right. I’m not as okay with sharing you as I thought I was. I was just telling myself that."
    s "It’s...really surprising to have to hear you admit that here and now of all times and places."
    ki "I’m surprised too. None of this would have happened if you didn’t show up at my club today. Way to go and ruin my life, Sensei. You know I have feelings now."
    s "I’ve always known that, Kirin. But, just to set the record straight, you’re the one who’s ruining {i}my{/i} life now."
    ki "I’m not at all surprised to hear that, but please tell me why."
    s "It’s just going to be a lot harder to hurt your feelings now that you’re acknowledging them."
    ki "Is running away still on the table?"
    s "It never was."
    ki "{i}Can{/i} it be on the table? Because starting over as a brand new person sounds like...the ultimate blessing right now."
    ki "Especially since I have no clue how I’d ever face Noriko if I ascended from the sex-friend category into...whatever category she’s in."
    s "Let’s...go on a few more dates first before we start categorizing what we are now."

    scene kirinarcade41
    with dissolve

    ki "Dates?..."
    ki "Was this a date?"
    s "I...think so?"

    scene kirinarcade42
    with dissolve

    ki "What the fuck? I didn’t even get to dress up for it. "
    ki "Now we have to go on another one. It’s literally the only option."
    s "Well...what are you doing tomorrow night?"

    scene kirinarcade43
    with dissolve

    ki "Heh..."
    ki "..."
    s "..."

    scene black
    with dissolve2

    ki "Sounds like I’m getting dressed up..."

    $ renpy.end_replay()
    $ kirinspecial45p1 = True
    $ kirin_love += 1
    stop music fadeout 15.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    scene bedroom_night
    with dissolve
    play sound "dooropen.mp3"

    "I make it back to my room after another eventful day."
    "And I worry about how much my life is about to change."
    "That seems to be all that’s happening lately."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 4
    hide wednesday onlayer date
    show thursday onlayer date

    jump kirinspecial45p2

label kirinspecial45p2:
    scene nightsky
    with dissolve2
    play music "behindabathroom.mp3"

    "I decide to be a man of my word and tap on Kirin’s name in my phone since apparently the two of us go on dates now."
    "I figure there’s a decent chance she’s either not going to answer or just bail on me once she does as organizing something like this is a lot different than just bumping into each other and running with it."
    "I get that she likes me — that’s not a new development. And it was obvious she’d have to come to terms with that sooner or later, but that doesn’t mean any of this feels “normal.”"
    "What if it’s becoming too real for her?"
    "If she’s as much like me as she thinks she is, she might already be in the process of backing down."
    "It’s taken me several iterations of the same exact school year to even {i}begin{/i} to accept the idea of change that isn’t directly tied to coital probability and...I just don’t know if she’s there yet."
    "She might think she wants to run away, and she might think that {i}I’m{/i} enough for {i}her,{/i} but I know that’s just flat out untrue."
    "But {i}how{/i} do I know it’s untrue, you ask?"
    "That’s easy."
    "It’s because I’m not enough for anyone."
    "How {i}can{/i} I be when there are still so many parts of me that are missing?"

    s "..."

    "The phone stops ringing."
    "I had a feeling it would."

    scene black
    with dissolve2

    "The night ends without me ever hearing from Kirin."
    "And the two of us move backward instead of forward."
    "Right back to where we belong."
    "........."
    "......"
    "..."
    play sound "phonering.mp3"

    "But then {i}my{/i} phone begins to ring."

    scene nightsky
    with dissolve
    play sound "phonebeep.wav"

    "And the night begins again."

    ki "Hey! Sorry! I left my phone in the other room while I was doing my makeup. Are we still doing this?"
    s "You mean acknowledging the probability of a relationship between the two of us that exists without any immediate promise or expectation of sex?"
    ki "Just say dating, it’s shorter. But yeah. Basically that."
    s "Then I guess so. That is why I’m calling, after all."
    s "I think I’m actually getting pretty good at this dating thing. You’re like the third or fourth girl in recent memory I’ve gone on an actual date with."
    ki "Wow, you know exactly what to say to get a woman excited, don’t you?"
    s "You’re not a woman, you’re a girl. "
    ki "Doesn’t that make you, like, five times creepier in this context? I’m trying to give you a hand here."
    ki "Also, we’ll see if you’re still calling me a {i}girl{/i} after you get a look at me tonight. I am fucking {i}hot{/i} right now."
    s "Great, that means you’ll attract all of the attention and people will stare at you instead of focusing on the age gap between us."
    ki "{i}I’m telling you{/i} that won’t be a thing tonight. Trust me. The last thing I want is somebody interrupting our date by asking if you’re my dad."
    ki "Inside the bedroom, that kind of thing is okay. Out at dinner? Not so much."
    s "Is that what we’re doing? Dinner?"
    ki "Do you seriously not even know?"
    s "...Just kidding?"
    ki "We could always go dancing instead! I have plenty of experience grinding on you already, so we won’t even look out of place."
    s "Dinner it is. I’ll send you an address."
    ki "Okay, but pick a nice place. I want people to see me."
    s "How nice?"
    ki "If there are prices listed on the menu, it’s probably too cheap."
    s "But I only know one place like that and-"
    ki "Cool! Then you know where to go! "
    s "Kirin-"
    ki "See you soon, Sensei!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Kirin hangs up the phone before I have the chance to tell her that the only place I know of that fits that criteria is the restaurant Touka took me to during the first Dorm Wars."
    "This is even more problematic because, if my memory serves me well, I couldn’t even pronounce anything on that menu."

    s "..."

    "But I guess it’s fine to be frivolous every now and then considering that saving up my money will do absolutely nothing."
    "And hey, if it lets Kirin finally experience something she can lord over her sister or anyone else who tries to pick on her, fine. "
    "She doesn’t have many things like that."
    "And if she’s as attractive tonight as she’s making herself sound-"
    "Actually, if she’s as attractive tonight as she’s making herself sound, I {i}don’t{/i} want other people to see her. But I guess it’s too late for that."

    play sound "phonebeep.wav"

    "After typing “Kumon-mi fancy restaurants” into a search engine, I manage to find the place and...swallow my tongue as I send Kirin the address. "
    "........."
    "......"
    "..."

    scene kirinfancydate1
    with dissolve2

    "We decide to meet around the corner from the restaurant as standing directly in front of a place as high-class as that would have been extremely weird for whichever one of us got there first."
    "Which, judging by the fact that I am staring at a pair of vending machines instead of a girl, seems to be me."

    scene kirinfancydate2
    with dissolve

    ki "Excuse me, sir...you wouldn’t happen to be my date, would you?"
    s "No. I have no idea who you are."

    scene kirinfancydate3
    with dissolve

    ki "Hey. I’m not {i}that{/i} unrecognizable."
    s "You wouldn’t happen to be Kirin’s mom, would you? You look really familiar."

    scene kirinfancydate4
    with dissolve

    ki "That’s me- here to cheat on my husband and open up the opportunity for you to fuck {i}all{/i} of the Kanda women one day."
    s "You look like five years older than normal, Kirin. It’s weird."
    ki "I clean up pretty good, right? I could probably pass for a college student right now, don’t you think?"
    s "Unfortunately, all I can think of right now is pushing you up against those vending machines and impregnating you."

    scene kirinfancydate5
    with dissolve

    ki "It’s the skirt, right? It makes me look at least three times more breedable than normal. "

    scene kirinfancydate6
    with dissolve

    ki "Maybe don’t impregnate me, though? I’d be a horrible mom and you’d be no better of a father."
    s "Yeah, I’d normally agree, but that skirt is doing things to me."

    scene kirinfancydate7
    with dissolve

    ki "I’ll keep that in mind for the future. Right now, we have reservations."
    s "I didn’t make reservations. I didn’t think we needed them."
    ki "Yeah, I figured that’s what would happen. Which is why {i}I{/i} called and made reservations. "
    s "Oh, cool. That means you’re paying, right?"

    scene kirinfancydate8
    with dissolve

    ki "Not. A. Fucking. Chance."

    scene black
    with dissolve2

    "Kirin (The suddenly older model) and I round the corner and head into the restaurant. "
    "The first time I came here, the entire venue was rented out for the sake of Touka flaunting her wealth or whatever. But this time, the place is pretty much packed."
    "The only tables that remain vacant are ones with “Reserved” signs propped up on top of them. "
    "And while this amount of people would normally cause me to worry on account of my {i}date’s{/i} age...that doesn’t seem to be a problem tonight."
    "Sure, Kirin is still significantly smaller than me, but her new look combined with the way she’s carrying herself makes her seem old enough to not be problematic, I guess."
    "In fact, people probably think I’m rich as hell for bagging someone like her. "

    scene kirinfancydate9
    with dissolve2

    "We’re sat down at a table near the piano, equipped with an accompanying lounge singer, and our orders are taken almost immediately after."
    "Kirin also manages to order a glass of wine without the waitress thinking anything suspicious- which completely validates my thought just moments ago about this not being that weird."
    "Well...not {i}looking{/i} that weird."
    "It’s still pretty fucking weird when you think about it. But that’s exactly why I just try not to think about it."

    ki "Good pick, Sensei. How’d you find out about this place?"
    s "I came here on a date with another girl."
    ki "There you go again, always knowing exactly what to say to make me happy."
    s "This is different than that, though. I don’t think either of us really felt comfortable on that first date. "
    ki "Are you saying you feel comfortable with me?"
    s "Kind of, I guess? Which is pretty surprising considering there are other people here this time and the restaurant was empty during my maiden voyage."
    ki "Empty? Did you come with Ayane?"
    s "Touka. Ayane and I don’t really do stuff like this."
    ki "But you and {i}Touka{/i} do?"
    s "When there is a prize on the line, I guess so."

    scene kirinfancydate10
    with dissolve

    ki "Ahh, Dorm Wars then. I’m still jealous I wasn’t picked for that this year. But I guess I {i}did{/i} manage to actually win my contest this time, so not {i}all{/i} was lost."
    s "There’s always next year. Assuming the Date War isn’t banned for being too divisive, that is."

    scene kirinfancydate11
    with dissolve

    ki "To be honest, I’m surprised it wasn’t banned after the first time. Either way though, it’s not like I’d have a real chance at winning against...like, 75%% of the class."
    ki "I refuse to believe I’d lose to, like...Yasu and Yumi. And maybe Nodoka and Molly. But I can see you choosing basically anyone other than those few over me. "
    s "That’s because you have crippling self-esteem issues and dwell on the worst parts of everything ever said to you. "

    scene kirinfancydate12
    with dissolve

    ki "I mean, yeah. But also, there’s not really any “good” part of “You’re not enough for me” that I can latch onto to overcompensate for the bad part. Which was all of it."
    s "Hey, either I can be honest with you or I can lead you on. Which one do you want?"
    ki "Honesty, obviously. I know you might think I’m upset about the whole “not enough” thing, but that’s really not it. I get it. "
    ki "In fact, if you told me back then that I {i}was{/i} enough, it probably would have been creepy and made me feel weird about seeing you again. So I’m glad that’s not what happened."
    s "And yet, here we are out on a date because you want to {i}become{/i} “enough,” right?"

    scene kirinfancydate13
    with dissolve

    ki "No. We’re out on a date because I wanted to dress up and look hot and there isn’t anyone else who I think would appreciate that as much as you."

    scene kirinfancydate14
    with dissolve

    ki "But if you just so happen to start liking me more {i}during{/i} that date, that’s cool too. I won’t complain."
    ki "And if that just so happens to continue blossoming into something more than just highly-compatible friends with benefits, I also won’t complain."

    scene kirinfancydate13
    with dissolve

    ki "You’re taking me dancing next time, though. What’s the point in looking all sexy if I don’t get to flaunt it?"
    s "Kirin, do {i}I{/i} look like I have ever danced at any point in my life to you?"

    scene kirinfancydate15
    with dissolve

    ki "No. You look like a pathetic, mopey loser. But {i}I{/i} look hot and all of my attention will go to you. So, by extension, everyone will think {i}you’re{/i} cool as well. We both win."
    ki "And that’s {i}before{/i} the grinding happens. When that kicks in, we just win even harder. "
    ki "Lowkey, you could probably straight up fuck me in the middle of a dance club and no one would give a shit."
    s "So it all comes back to sex once again."

    scene kirinfancydate13
    with dissolve

    ki "It all comes back to-"

    scene kirinfancydate16
    with dissolve

    ki "Wait, no. That’s not the point I wanted you to get from that."
    ki "Yeah, sex is good. And pretty pivotal to the...overall foundation of our relationship, but the whole reason I’m starting to branch out like this is because I want stuff to, like...be more than that. I think."
    ki "Like...I want the {i}option{/i} to fuck you in front of a room full of strangers. But I also want the option to just, like...eat with you sometimes."
    ki "And the strangers thing isn’t even like, pure exhibitionist desire either. I only want to do it because it would mean that people, like...see us together."
    s "That...is what exhibitionism is."

    scene kirinfancydate17
    with dissolve

    ki "No, like...uhh..."
    ki "How do I even put this?"
    s "Oh. You want them to see us {i}together.{/i} Like, as an actual couple."

    scene kirinfancydate18
    with dissolve

    s "Who just...have sex in public because that’s normal."
    ki "Sensei...no one ever wants me."
    ki "And I want people to think I’m wanted...."
    ki "If we say it like that, we can avoid the idea of us being an “actual” couple."
    s "If you want to be wanted, why are you always saying and doing things that you know will make people dislike you?"

    scene kirinfancydate19
    with dissolve

    ki "I don’t know! I have no idea why I do half of the things I do when barely anything ever comes out the way I want!"

    scene kirinfancydate20
    with dissolve

    ki "Maybe it’s...time for a change of strategy? Maybe it’s good to, like...you know, do stuff that {i}won’t{/i} directly hurt people every once in a while?"
    s "You don’t say..."
    ki "I’m not pretending I’m an angel when I know full well why no one likes me but you, Noriko, and Miku. And, you know, maybe I don’t need anyone other than you guys. "
    ki "I’m just tired of feeling so empty all of the time and sex didn’t work as well as I thought it would in filling me up."
    s "You seem-"
    ki "Don’t do it, Sensei. Don’t make the joke. "
    s "..."
    ki "..."
    s "You seem pretty “filled up” every time we have sex."

    scene kirinfancydate21
    with dissolve

    ki "Hah...pathetic. "
    ki "Both of us. "
    ki "Here we are in what’s probably the nicest restaurant in all of Kumon-mi, completely incapable of relating to one another {i}without{/i} being perverted."
    s "Well, when a relationship is formed by a girl storming into your office, flashing you her underwear, and trading you her virginity for a handful of excused absences, it’s kind of hard to shake that."
    s "The chances of that changing at this point basically don’t exist."

    scene kirinfancydate9
    with dissolve

    ki "What if they don’t have to? What if we can figure out a way to be ourselves {i}and{/i} become “enough” for one another?"
    s "That’s exactly what you’ve been missing all along. You don’t {i}have{/i} to pretend to be someone you’re not just to get closer to other people. Because, more often than not, that only pushes everyone away."
    ki "Sensei...You do the same exact thing. "
    s "I’m completely real with you, Kirin."
    ki "Yeah, I know. But you’re {i}not{/i} real with Noriko and Miku and Karin. The Sensei I see with those people is totally different from the one {i}I{/i} always see. "
    ki "And, listen...I’m not gonna make this about other girls because this is {i}my{/i} chance to be in the spotlight after hiding from it for so long."
    ki "I just want to move forward in whatever fucked up way the two of {i}us{/i} can because watching you progress with all of them makes me realize that we haven’t gone {i}anywhere{/i} yet."
    s "We weren’t supposed to."
    s "This was never meant to be anything more than a way for the two of us to benefit without any sort of emotional attachment. {i}That’s{/i} what we wanted."

    scene kirinfancydate22
    with dissolve

    ki "The convenience store was out of salmon onigiri this morning."
    s "...What?"
    ki "And the vending machine near the gym? Out of CC Lemon."
    s "Kirin, what the fuck are you talking about?"

    scene kirinfancydate23
    with dissolve

    ki "I wound up buying ume onigiri...and a can of coffee instead."
    ki "And you know what? I enjoyed them. They really hit the spot for lunch today."
    ki "It was a bit of an abnormal flavor combination, but I’ll probably buy them again next time."
    s "I don’t-"
    ki "No one {i}always{/i} gets what they want. And that’s not a bad thing."
    ki "Because sometimes, we don’t even really {i}know{/i} what we want until something else falls into our hands."
    ki "Maybe we {i}are{/i} destined to be fuck buddies. And maybe I’ll just wind up being your perpetual side-chick on account of my amazing blowjob skills and unrivaled sex drive."
    ki "But maybe...that’s not actually what we want at all. "
    ki "Maybe we just want someone we can be ourselves with. "
    ki "Someone to fuck when we want to fuck. "
    ki "Someone to get dressed up with for no real purpose whatsoever."

    scene black
    with dissolve2

    ki "Someone to {i}dance{/i} with."
    s "What are you-"
    ki "Hey! Lounge guy! Play something slower! I want to dance with my boyfriend!"
    s "She doesn’t mean that. You guys are doing great. Keep playing what you’re already playing."
    ki "Don’t listen to him. He has no idea what he wants."

    scene kirinfancydate24
    with dissolve2

    s "Kirin, what the fuck are you doing?"
    ki "I don’t know! "

    scene kirinfancydate25
    with dissolve2

    ki "And that’s exactly why it’s so exciting!"

    scene kirinfancydate26
    with fade

    pianoman "Ahh...to be young."
    loungeguy "What should we do, man? My heart says play them a song, but my mind keeps reminding me of that one guy who was fired by that rich little girl despite doing absolutely nothing wrong."
    pianoman "If we’re gonna go out, we’re gonna go out with a bang."
    loungeguy "Do you think...we should play {i}that{/i} song?"

    scene black
    with dissolve2

    pianoman "As if there was ever any other option..."

    scene kirinfancydate27
    with dissolve

    loungeguy "Ladies and gentlemen...we’re going to slow things down for a moment."
    loungeguy "This next one..."
    loungeguy "Is called “Despacito.”"
    ki "Not...what I had in mind. But this will have to do."
    s "It’s like this song is following me or something."

    scene kirinfancydate28
    with dissolve

    ki "Do you know what to do?"
    s "Absolutely not. I would like to sit back down now."
    ki "One song. That’s all I ask."
    ki "Just hold onto me exactly like you’re doing and just...sway back and forth a little."
    s "People are looking at us."

    scene kirinfancydate29
    with dissolve

    ki "I know! Isn’t it amazing?!"
    ki "We’re the center of attention. Everyone thinks we’re together."
    s "That’s great for someone like you who likes being the center of attention, but for me it’s-"

    scene kirinfancydate30
    with dissolve

    ki "Who cares? If it bothers you knowing other people are watching, just look at me instead."
    ki "They served me wine and everything. No one has any idea I’m in high school. Let alone that you’re my teacher."
    s "While that is...slightly better, it doesn’t fix everything."
    ki "No...but it makes me happy. And so it would be nice if you could bear with it for a few minutes."
    s "..."
    ki "..."

    scene kirinfancydate31
    with dissolve

    s "And so we stay like that for a few minutes..."
    ki "You’re thinking out loud again."
    s "I thought if I narrated how much time went by, you’d believe it."
    ki "It’s been ten seconds, Sensei."
    s "That’s it? This is even worse than I thought."

    scene kirinfancydate32
    with dissolve

    ki "Want me to help make it better?"
    s "By poking my face? Why does everyone always do that?"
    ki "By kissing you."
    s "In front of a crowd of people in a fancy restaurant?"
    ki "It’s not sex and it’s not a dance club, but I think it’ll have the same sort of mental effect on me."
    s "Kirin-"
    ki "I like you."

    scene kirinfancydate33
    with dissolve

    ki "I, like...{i}actually{/i} like you."
    ki "And I...kind of want...to maybe, like..."
    ki "You know..."
    ki "Keep doing that...if that’s cool?"
    s "..."
    ki "..."

    scene kirinfancydate34
    with dissolve

    s "Yeah...it’s cool."
    ki "Even though it invalidates the pact I made with Noriko?"
    s "I think you’re probably the only one who still believed in that pact anyway."
    ki "Even though my sister also likes you? And Miku?"
    s "Your sister doesn’t know the real me yet and Miku is fine with me being with anyone."
    ki "Even though I talked for so long about how I’d never want anything more? And that I’m only in this for sex? And how love is stupid and fake and boring?"
    s "As much as I appreciate you talking through Despacito, I would also like if you would stop talking now. You’re attracting more-"

    scene kirinfancydate35
    with dissolve

    ki "Mm!"

    "Okay. Well, I guess that’s one way to stop talking."

    ki "Mn...mnch...mm~"
    ki "{i}Sensei...{/i}"
    ki "{i}Kiss me...harder...{/i}"
    s "..."

    "Ahh, fuck it. They’re already looking at us."

    scene kirinfancydate36
    with dissolve

    ki "Mm! Mmf...mlm...mnnh......hmm!"
    ki "I like you...mmlm...I like you...mmh! I really...really...mlm...like you!"

    scene black
    with dissolve2

    pianoman "What did I tell you, Lounge Guy?"
    loungeguy "You were right, Piano Man."
    pianoman "There was never another option."

    scene bedroom_night
    with dissolve2

    "For the second night in a row, I make it back home after parting ways with Kirin."
    "Tonight is a little different than the last, though."

    scene black
    with dissolve2
    play sound "phonebeep.wav"

    "Because tonight, I received an extra gift upon lying down in bed."
    "Yes, my phone may have just beeped."
    "And yes, you’re probably thinking that, based on context, she sent me a picture of herself without any clothes on."
    "That’s what any reasonable person would believe, of course."
    "This is Kirin we’re talking about."
    "But what I received instead is something entirely different."
    "And it fills me with both a sense of extreme discomfort...and another feeling I have a hard time putting into words."

    play sound "phonebeep.wav"

    "I tap on the new message notification-"
    "And all it says is this:"

    ki "{i}Goodnight <3{/i}"

    $ renpy.end_replay()
    $ kirinspecial45p2 = True
    $ kirin_love += 5
    stop music fadeout 7.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "........."
    "......"
    "..."

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    if day == 5:
        jump advancetosat
    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon

label sportswars9:
    scene kirincafteria1
    with dissolve2
    play music "normalday.mp3"

    "And we enter the somewhat less exciting section of the day centered around the “affection-starved” Kirin Kanda."
    "Kirin was an interesting character. Not just in the fact that she was significantly more open to sexually exploring with her older sister than most other girls her age, but in the fact that she was {i}weird.{/i}"
    "Again, not {i}just{/i} because she wanted to fuck her sister, but because there were so many elements to her as a person that she intentionally hid from everyone else while begging for them to be found."
    "She gained little to no satisfaction in handing those traits to others. She wanted to be the type of girl who someone would sacrifice their fingernails for in the process of unearthing them bare-handed."
    "But the only person she ever encountered who seemed willing to do that (sister aside) was missing in action. "
    "Her friends, Noriko and Miku, weren’t {i}opposed{/i} to getting their hands dirty. But without {i}love{/i} at the forefront of their actions, she wouldn’t {i}expect{/i} them to dig like she expected of {i}him.{/i}"
    "It was a selfish, conflicted way of seeing the world — and the way she’d complain about the rain while rolling her windows down would only dampen things further."
    "And lately, it felt like she was being stalked by rain clouds."
    "The permanent shelter attached to her hip had been sexually assaulted just a short while ago and forgotten the point of {i}permanence{/i} entirely and had been starting to show cracks in its roofing."
    "Meanwhile, the man who became a storm and hailed down upon it/her was wandering around the town completely useless."
    "And sure, there were other storms around. "
    "Sure, it wouldn’t be {i}that{/i} hard for Kirin, a young and attractive high school girl, to find some creepy, perverted old man to dick her down in a love hotel if she really wanted that right now. "
    "Even in a town like this, such a thing was possible. And such a thing would {i}always{/i} be possible."
    "She kept that thought in her back pocket — how she could sell her love at a moment’s notice. "
    "It didn’t have to be in exchange for money. It didn’t have to be in exchange for praise."
    "All she wanted was attention."
    "{i}Was.{/i}"
    "Lately, she’d begun to want something else."
    "Lately, she’d been thinking more and more about maybe putting some of those rubber traits on display rather than burying them beneath the soil and waiting for someone to trip over them."
    "She wasn’t thinking about sex as much as she used to. Right now, for example, all she really wants is a hug."
    "But she’s the type of girl who, despite knowing that, would ask for something else instead. Because no one will ever think she’s interesting if she isn’t {i}complicated.{/i}"
    "Or was it more that {i}she{/i} wouldn’t think she’s interesting if she isn’t complicated?"
    "I’m not sure, to be honest. It’s not as if I can read her thoughts. "
    "I can only guess them. "
    "I can only tell you what I see."
    "And right now, I see a normal girl in a normal cafeteria- worrying about normal things like “Where are the people I know?” and “If I can’t find them, where should I go to eat?”"
    "And the normal response to that would be to just ignore her and let her get on with her life. "

    scene kirincafteria2
    with dissolve

    "But that isn’t the way things work when you’re a disembodied bystander."

    scene black
    with dissolve2

    ki "Miku! Hey! Can I come sit with you guys?"

    "That isn’t the way things work when you can never close your eyes."

    play sound "static.mp3"
    scene kirincafteria3 with flash
    stop sound

    "That isn’t the way things work when you want them to work because nothing ever works and nothing ever {i}fits.{/i}"
    "Kirin is {i}weird.{/i} She lost her virginity in a {i}love hotel.{/i} She’s a high school girl and she let her teacher fuck her doggystyle for her {i}first time{/i} in a fucking {i}love hotel.{/i}"
    "Who does she think she is wanting {i}love{/i} now? What makes her believe she should be worthy of affection or praise in {i}ANY{/i} form?"
    "{i}She’s a WHORE. She’s a filthy whore who wants to fuck her sister.{/i} THAT is what makes her interesting. Everything else just makes her {i}WEIRD.{/i}"
    "Goodbye."

    ki "Heya! Sorry for intruding. Noriko’s helping with the scavenger hunt clean-up right now and I’d feel like a fucking loser if I had to eat alone."
    mi "Ain’t nothin’ to feel sorry for, Kirin! And with the next contest bein’ the relay race, this gives us a good opportunity to con ya into tellin’ us your team’s strategy!"
    ki "I believe the strategy is to “run really fast.”"

    scene kirincafteria4
    with dissolve

    mi "Crap! That was ours too! "
    mak "I’m pretty sure that’s just...the basic way to approach {i}any{/i} race. But given the fact that Miss Imai has been becoming rather unhinged lately, I’m sure some other obstacles will be added to the mix."

    scene kirincafteria5
    with dissolve

    mi "God, I hope it ain’t another horse dick. Been seein’ way too many of them lately."
    ki "I’m sorry, what?"

    scene kirincafteria6
    with dissolve

    mi "Oh, right. You weren’t there for that. Imani put a horse dick in the ball pit."
    ki "Uhhhhhhhhh-"
    mak "Not a real one. A dildo."
    mi "Might as well have been a real one. Thing was the size of my torso."

    scene kirincafteria7
    with dissolve

    ki "Do you think it’s still there?"
    mi "Don’t go gettin’ any ideas, Kirin! "
    mi "I know ‘yer one of them loose women, but I ain’t about to let a fellow athlete paralyze herself from the waist down for somethin’ some good ole finger-wigglin’ can take care of!"

    scene kirincafteria8
    with dissolve

    ki "Miku, sex is {i}way{/i} better than {i}finger-wigglin’.{/i} It’s like, barely even comparable."
    mi "Really? Was kinda workin’ under the assumption that, like...thing goes in, stuff feels good, thing comes back out. Seems pretty simple to me. "
    mak "Shouldn’t you have maybe been a {i}little{/i} offended that Miku just referred to you as a “loose woman?”"
    ki "Miku doesn’t know any better yet. And it’s our job to teach her. Which is why I hereby volunteer myself to take her virginity via strap-on so she can learn firsthand just how glaring the difference is."
    mi "I think I’d rather try it with a real one."
    mak "Just for clarity’s sake, we’re not still talking about horses, are we?"

    scene kirincafteria9
    with dissolve

    mi "I AIN’T GONNA DO IT WITH A HORSE NO MATTER HOW BAD YOU AND YOUR MOM WANT ME TO!"
    w "Maruyama. I don’t even know where to begin right now, so please just...stop existing."

    scene kirincafteria10
    with dissolve

    mi "Great. Now all’a Class B’s gonna think I’m some kinda horse do-er when that’s Touka’s job."
    ki "I’d pay to see that."
    mak "I know someone you can pay to see something similar. "
    ki "And now I suddenly have plans this weekend. Thanks, Makoto."

    scene kirincafteria11
    with dissolve

    mak "You’re welcome. Just-"

    scene kirincafteria12
    with dissolve

    mak "Huh?"

    scene kirincafteria13
    with fade

    na "!!!"
    mak "Oh. The mug girl is back."
    ki "The...mug girl?"

    scene kirincafteria14
    with dissolve

    mak "I met her in Sensei’s office after school one day. She kept showing me a mug and smiling. I was very confused."
    ki "About the mug part or the fact that Sensei was hanging out with a little girl in his office?"
    mak "I’m sad to say this, but I think the mug part is easily the more shocking of those two things."

    scene kirincafteria15
    with dissolve

    mi "Yeah. If he’s openly doin’ the frisky tango with me, I don’t think anybody’s off limits. Mug Girl included."
    na "?..."
    mak "Do you need something, Mug Girl?"

    scene kirincafteria16
    with dissolve

    na "!!!"
    mak "What’s this?"
    na "!!!!...!!!!!....!!!!"

    scene kirincafteria17
    with dissolve

    mak "A picture? For me?"
    na "!!!!!!!!"

    stop music
    play sound "static.mp3"
    scene kirincafteria18 with flash
    stop sound

    "this is wilford blackhole hands the creator of hands and black holes"
    "he has five legs because he is a flower which is why there are hearts that float behind him"
    "at the ends of his arms are black holes that he sucks his enemies into"
    "he has two faces so he can give multiple expressions at once and extra necks that come out of his shoulders that tell you how to feel"
    "inside his stomach is the first black hole ever created and he can never become pregnant because the baby will disappear into the hole"
    "this is wilford blackhole hands and he is one of the good guys"

    play sound "static.mp3"
    scene kirincafteria19 with flash
    stop sound
    play music "normalday.mp3"

    mak "Thaaaaank yoouuuu...."
    ki "What is it? It’s hard to see from over here."
    mi "Looks like some kinda monster."
    mak "What...do I do with it?"

    scene kirincafteria20
    with dissolve

    mi "Everybody knows that if a kid hands ya a picture, you’ve gotta put it up on the fridge! That’s rule numero uno of takin’ anythin’ from a kid!"
    ki "None of my drawings ever made it onto the fridge when I was a kid."

    scene kirincafteria21
    with dissolve

    mi "I sincerely apologize for your loss."
    ki "Ew. Hearing you say something in such a normal way makes me feel surprisingly uncomfortable. "
    mak "Well, how else are we supposed to respond to you brutally decapitating the mood? Who even are you? The aliens who brutally decapitated my father?"

    scene kirincafteria22
    with dissolve

    ki "Okay, now {i}that{/i} is killing the mood!"
    mi "Makoto, come on. "
    mak "I’m sorry, Miku. This is the only way I’ve learned how to cope. And it actually got my mom to laugh the other day. So I guess that’s a thing now."
    ki "Okay. New conversation topic. How does everyone feel about Taylor Swift? Illuminati? Or {i}not{/i} Illuminati? Go."

    scene kirincafteria23
    with dissolve

    mi "Illuminati and it ain’t even close. "
    ki "Right?"
    mak "Why must we always attack strong, successful women? Is she not a role model for young girls all across the country?"

    scene kirincafteria24
    with dissolve

    ki "I heard she ate a baby on live television but all of the footage of it was scrubbed from the Internet and now people’s memories are starting to vanish."
    mi "I’m pretty sure she’s the one who keeps hidin’ cans of soup under our beds."
    mak "Neither of those things are happening! Stop believing everything you hear online! Especially when there are way less believable things happening that are actually true!"
    ki "Like?"
    mi "Yeah. Like what?"
    mak "For example — the fact that I’m in a secret club that meets on the rooftop to usher in a brand new timeline where-"

    scene kirincafteria25
    with dissolve

    mi "You think {i}that’s{/i} unbelievable? Just wait until ya find out what {i}I{/i} did the other day."
    mak "I never even finished my- ugh! Why even bother?"
    ki "Well, I know based on the earlier part of this conversation that it’s definitely not sex. And I can’t imagine anything else surprising me, so just go ahead and tell me."
    mi "I..."

    scene kirincafteria26
    with dissolve

    mi "Went out to a karaoke bar."
    ki "You did?! Even with your sound phobia thing?! That’s, like...a huge step forward for you, isn’t it?!"
    mi "Yeah. I {i}am{/i} pretty impressive, after all."
    mak "Now tell her how long you stayed for."
    mi "We don’t have to talk about that part."
    ki "I won’t hold it against you if you fell asleep and spent the night there. I did that once after getting into a fight with my parents. I slept surprisingly well too."
    mak "She stayed for three minutes."

    scene kirincafteria27
    with dissolve

    ki "Oh..."
    mi "Thanks, Makoto. Now I ain’t gonna look impressive anymore."
    ki "Well...there’s always next time. The important thing is that you tried. That’s way more than I would have been able to do in your shoes."

    scene kirincafteria28
    with dissolve

    mi "Yeah, I know. I just feel like a jerk for leavin’ Sensei and Karin alone since it was me who invited ‘em out in the first place."
    ki "Karin, like...my {i}sister{/i} Karin? All three of you went together?"
    mi "If you count me only bein’ there for three minutes as goin’, yeah. If not, it was just those two."
    ki "And..."
    ki "Wait, {i}when{/i} was this?"

    scene kirincafteria29
    with dissolve

    mi "Uhh...I’m pretty sure it was a Sunday. But I ain’t sure if it was last Sunday or...or the one before it or..."
    mi "Weird. All the weeks are kinda just blurrin’ together in my head. Maybe I need one of those big bananas Ayane’s always gettin’ delivered? They help with memory. Don’t they, Makoto?"

    scene kirincafteria30
    with dissolve

    ki "Sunday..."
    mak "Well, Miku...while there are numerous studies linking the consumption of potassium to improved cognitive function, the concept of memories is-"
    ki "Can you guys excuse me for a second? I have to...go make a call."

    scene black
    with dissolve2

    "........."
    "......"
    play sound "phonedial.mp3"
    "..."

    scene kirincafteria31
    with dissolve2

    ki "There’s no fucking way...is there?"
    ki "..."
    ki "{i}No.{/i} "
    ki "He wouldn’t. That’s ridiculous. He’d at {i}least{/i} call me to suck his dick if he was feeling decent enough to go out to fucking {i}karaoke.{/i}"
    ki "..."

    scene kirincafteria32
    with dissolve

    ki "Come on! Pick up the fucking phone!"
    seco1 "Karin...isn’t that your sister?"
    ka "Kirin? What’s she doing out in the hall? And-"

    scene kirincafteria33
    with dissolve

    ka "{i}Hah!{/i} And she’s on her phone during school hours..."
    seco2 "Karin...you’re the only girl in all of Kumon-mi who follows that rule. "
    seco1 "Yeah, but that’s why we love her."
    ka "I must do something about this...It is my duty..."
    seco2 "Heh. Duty."
    ka "I don’t get it."
    seco1 "We can go back to the gym for a few minutes. I wanted to ask Rise something anyway."
    ka "Sorry, guys. I’ll meet up with you in a minute."

    scene kirincafteria34
    with dissolve
    stop music fadeout 15.0

    ka "Kirin...You’re not supposed to be on your phone in school. "
    ki "You’re the only girl in all of Kumon-mi who follows that stupid, fucking rule."
    ka "Don’t curse at me when I’m just trying to help. Besides, shouldn’t you be in lunch right now?"

    scene kirincafteria35
    with dissolve

    ki "Shouldn’t you be minding your own fucking business right now?"
    ka "Yes, but I don’t want you getting in trouble. If our parents find out you’ve been disobeying school policy again, you won’t be able to-"

    scene kirincafteria36
    with dissolve
    play sound "phonebeep.wav"

    ki "Did you go out to karaoke with Miku and Sensei?"
    ka "Did I...go to karaoke with..."
    ki "Did you or did you not go out to karaoke with Miku and Sensei?"

    scene kirincafteria37
    with dissolve

    ka "Hahah! Did I...do something like that?..."
    ka "I don’t know...I go out to karaoke with...so many friends that it can get kind of hard remembering who I’ve done {i}what{/i} with {i}when{/i} and-"
    ki "The night you came home bawling your fucking eyes out. {i}That{/i} night. "
    ki "Was {i}he{/i} involved then? Did something happen?"

    scene kirincafteria38
    with dissolve

    ka "Hahah......hah......."
    ki "Karin. I am {i}asking{/i} you a question. Did he...or did he {i}not...{/i}do something that night?"
    ka "Hahaha...."

    scene kirincafteria39
    with dissolve

    ka "Bye!"
    ki "Don’t you dare fucking-"

    play sound "doorslam.mp3"
    scene kirincafteria40
    with hpunch

    ki "Don’t you dare fucking run from me, damn it!"

    scene kirincafteria41
    with dissolve

    ki "{i}Karin! Get back here!{/i}"

    $ renpy.end_replay()

    "........."
    "......"
    "..."

    scene kirincafteria42
    with dissolve

    na "!..."

    $ sportswars9 = True

    jump sportswars10

label sportswars18:
    scene sexgrindcumyeah1
    with dissolve2
    play music "amiawake.mp3"

    ni "That son of a fucking bitch. Who does he think he is just disappearing and leaving you to fend for yourself like this? And why the fuck won’t he answer his phone?"
    a "I’m sure he has a good explanation, Niki..."
    a "Sensei loves me...and he’d never just leave me here by myself on purpose..."
    a "But...at least I have {i}you{/i} to take care of me tonight..."
    ni "Yeah, but you {i}should{/i} have your fucking uncle. Or at least an idea of where he ran off to this time. Because it’s so late that I’m starting to worry something might have happened to him."

    scene sexgrindcumyeah2
    with dissolve

    a "You think...something might have happened? "
    ni "Oh, no! I didn’t mean it like that. I’m sure everything is fine. I’m just...mad. That’s all. "
    ni "You’re right. I’m sure there’s a perfectly reasonable explanation for all of this."

    scene sexgrindcumyeah3
    with dissolve

    a "I hope so..."
    a "But if he doesn’t come back home tonight...can you maybe...stay here with me?..."

    scene sexgrindcumyeah4
    with dissolve

    ni "Of course, Ami. There’s no way {i}I’d{/i} just leave you here on your own. "
    ni "Should I use the couch? Or do you have a futon in your closet I could pull out? Maybe we can make this into a little sleepover? How’s that sound?"

    scene sexgrindcumyeah5
    with dissolve

    a "A sleepover?...With my favorite idol?...You really mean that?"
    ni "I’m not {i}just{/i} an idol, Ami. I’m family at this point. Remember how I told you to think of yourself as an honorary Nakayama sister?"
    a "Sorry...I guess that just felt like such a dream that I must have convinced myself it {i}was{/i} one."
    ni "It wasn’t a dream. You and me are gonna be like glue, okay? Or like...glued together, I mean. Not just glue. That would be gross."
    a "You’re a lot better with words on stage, aren’t you?"
    ni "There are just certain things that come a little more naturally when you’re wearing a mask, don’t you think?"
    a "Should you really be telling an adoring fan that the Niki Nakayama she’s familiar with is only an act?"
    ni "A fan? No. A sister? Sure. "
    ni "Besides, it’s not {i}all{/i} an act. Everything I write about comes from the heart, you know?"
    ni "It’s just all about your uncle. Which means it’s probably easy to tell how exaggerated some of it is since he’s only partially human and mostly just...carbon or whatever."

    scene sexgrindcumyeah6
    with dissolve

    a "He’s really lucky to have a childhood friend like you, Niki."
    ni "He sure is, Ami."
    a "I wish {i}I{/i} had a friend like that."
    ni "You do, don’t you? I could have sworn you had other girls coming over here and stuff."
    a "I do, but..."

    play sound "static.mp3"
    scene sexgrindcumyeah7 with flash
    stop sound

    a "{i}I can’t trust any of them...{/i}"
    ni "{i}Yeah...it’s hard to really trust anyone, isn’t it?{/i}"
    a "{i}Yeah...especially when you have something everyone else wants.{/i}"
    a "{i}But I’m sure you know about that already...onee-chan.{/i}"
    ni "{i}Onee-chan...{/i}"
    a "{i}Is it okay if I rest my eyes for a little? I’m getting kind of sleepy...{/i}"
    ni "{i}Hm? Oh, sure! Yeah. I’ll just read or something...{/i}"
    a "{i}Okay...goodnight, Niki.{/i}"
    ni "{i}Night, Ami...{/i}"
    ni "{i}Sleep well...{/i}"
    m "..."
    s "..."
    m "So, would you mind explaining to me why our clothes are still on?"
    s "Would you believe me if I told you I was scared?"
    m "I’m over 100lbs lighter than you and about a foot shorter. The worst I’m going to do is scratch up your back. Which, to be fair, you will both deserve {i}and{/i} enjoy."
    s "That’s not what I’m afraid of."
    m "Is there something about the term “safe day” you don’t understand? Do I need to give you a biology lesson? Or do you want to just man up already and continue rewriting the meaning of “high school sweetheart?”"
    s "..."
    m "..."
    s "..."
    m "..."

    scene black
    with dissolve2

    s "Get on the bed."

    play sound "static.mp3"
    scene sexgrindcumyeah8 with flash
    stop sound

    no "Our second contest will be one I’m sure many of you will be familiar with if you’ve spent any amount of time scrolling through the “game show” genre on your favorite pornographic web sites."
    no "I’ve taken it upon myself to procure two {i}very{/i} special machines that are meant to test one’s {i}endurance,{/i} if you will."
    no "Your objective will be to spend as much time as possible on these machines {i}without{/i} climaxing."
    no "If you have an orgasm...or if you decide to remove yourself from the machine to spare yourself the {i}embarrassment,{/i} you will be disqualified and your opponent will automatically win. "
    no "In the event that both of you climax together, the competition will either end in a draw or go to sudden death if both contestants agree."
    no "Does anyone have any questions?"
    mak "Yes. Why am I here?"

    scene sexgrindcumyeah9
    with dissolve

    no "Isn’t that something you’d be more suited to ask yourself? I did not {i}force{/i} you to come, Makoto. I just had a feeling you {i}would.{/i} "
    no "And quite thankful I am as I hope to draw your name here and watch a straight girl climax in front of a room full of lesbians."
    r "Ahem. {i}Bisexuals,{/i} thank you very much."
    no "Ahh, yes. Forgive the writer in me for editing out the uninteresting part."
    ki "I {i}wish{/i} I had a writer in me right now."
    n "Bruh."
    ki "I’m talking about Sensei in case anyone didn’t pick up on that. I wish he was fucking me right now. "
    mo "Yes, I believe that was quite clear."
    no "Fortunately, Kirin — you won’t have to go unsatisfied for much longer as your name has been drawn to compete in our next contest."

    scene sexgrindcumyeah10
    with dissolve

    ki "Let’s goooo! I want to compete against Makoto and turn her bi as well so we can all have an orgy after this."
    r "Just kiss her. That’s how I did it to Sana. "
    sa "That didn’t do anything!"
    n "If you think about it, this is kind of {i}already{/i} an orgy, right?"

    scene sexgrindcumyeah9
    with dissolve

    mo "If it is, it’s the most clothed orgy I’ve ever laid my eyes on. Especially since Zagull has already re-equipped all of his gear."
    ki "Noriko’s still in her underwear at least."
    mak "And soon to be two more of you."
    no "Makoto-"
    ki "Ha!"
    mak "Oh, you’ve gotta be fucking kidding me. Is it my turn already?"
    no "No, I just wanted to startle you. Kirin will be competing against Rin."
    r "Whaaaaaaaaaaaaaaaaaaaaaaaaaaaaat? "

    scene black
    with dissolve2

    no "Step forward, you two. Allow me to introduce you to our new “friends.”"
    r "I...I have to ride a sex machine in front of everyone? And they’re just...they’re just going to watch?! And that’s okay?!"
    no "It’s never too late to back out, Rin. Consent can be revoked at any moment. Your silence, however, can not."
    r "Uhhhhhhhhhhhhhhhhh..."
    ki "Rin, pleeeeeeease? Don’t you want to play together?"

    scene sexgrindcumyeah11
    with dissolve2

    r "Yes! But normally, thoughts like that stay inside my head! It wasn’t until Otoha that I realized I’d ever actually get to touch or experience things with other girls! "
    r "And also, {i}you{/i} definitely weren’t on the list of people I expected to “experience” things like that with!"
    ki "Perhaps this will be the start of a very long and exciting {i}extra-curricular{/i} relationship, then?"
    no "May I introduce you to our machines now? Or would you two like to continue flirting for a little while longer?"

    scene sexgrindcumyeah12
    with dissolve

    r "Sorry. Nervous. Horny. Scared."
    no "We may have the makings of a very short contest on our hands, then. "
    no "Kirin, Rin — please meet Irene and Matilda. They’re state of the art, vibrating ride-ables developed in partnership with NODOKorp, creator of the quadrildo. Just not really."
    no "I purchased them secondhand. I’ve made sure to clean them quite thoroughly, though. "
    no "I’ve also taken the liberty of removing their penetrative attachments, opting for the standard model instead as I have tested the machines myself and can attest to their ability to {i}function{/i} without them. "
    r "And we just...we just sit on them?"
    no "You may gyrate and shift to your heart’s content. But please be advised that I {i}will{/i} be operating the controls for these machines and that your fate is very much in my hands."
    no "I promise to keep things even, though. Scout’s honor."
    r "And we...have to take our clothes off?"
    no "Just the outermost layer of your bottoms. Your underwear may remain on if you’d like — for hygienic purposes, of course. "
    ki "No thanks. I’ll be taking Matilda raw if no one is opposed."

    scene sexgrindcumyeah13
    with dissolve

    r "Seriously?"
    no "You sound quite confident, Kirin. Are you not worried that direct stimulation will provide somewhat of a handicap if your opponent refuses to shed her undergarments?"
    ki "Frankly, I don’t care about the competition at all. I just want to ride a sex machine next to Rin and make her want to do me."

    scene black
    with dissolve

    no "Then, without further ado, please step forward."
    r "Already? We don’t get time to prepare or strategize?! Because I got thirty minutes before the cheer contest and this is {i}way{/i} more intimidating than-"
    no "Shorts off, Rin. And Kirin- oh. You’re already unclothed."
    ki "Taking my clothes off is kind of a superpower. I can strip down to {i}nothing{/i} in five seconds flat."
    r "F...Five?..."
    ki "Hey, can we move the machines a little closer together? I want Rin to catch me when I collapse from cumming too hard."
    r "I’m very bad at catching things. I can’t be trusted. Move the machines further apart!"
    no "They’ll remain precisely where they are. Now, if you two don’t mind — please greet our vibrating friends with your respective genitals."

    scene sexgrindcumyeah14
    with dissolve4

    no "Excellent."
    n "Is it just me or does Kirin look happier now than she’s ever looked before?"
    mak "Well, based on everything I’ve learned about her today, this is likely the happiest she’s ever {i}been.{/i}"
    ki "The only thing that would make it better is if I was up against Makoto instead."
    r "I don’t know what the third competition is yet. But, if Makoto wants to trade places, I’ll take her up on the offer."
    mak "Though I am quite worried about what “increasing intensity” may mean, I’m afraid I’m not keen to the idea of climaxing in front of my classmates."
    mak "Even if I would likely win as I’m most assuredly the only girl in this room who doesn’t need to change her underwear yet."
    sa "I..."
    mak "Apart from Sana, who has already proven she doesn’t have any underwear to even {i}change.{/i}"
    r "So...you say these things-"

    play sound "vibrate.mp3"
    scene sexgrindcumyeah15 with hpunch

    r "Eep!"
    no "Vibrate, yes."
    ki "Whoo, boy. That’s really good for some thrift store sex toy."
    no "To reiterate, the two of you will remain on these machines until one of you climaxes. And whoever lasts the longest will be crowned the winner."
    r "Mhm! Got it!"
    ki "{i}God{/i} that’s good."
    n "Doing okay over there, Molly?"
    mo "My hand...it has...a mind of its own! I must...fight back...against this dark urge!"
    r "Molly! Keep talking! It’ll...prevent me...from getting turned on!"
    mo "Then I’ll take a vow of silence just to spite you! {size=-15}And also because I want to see what happens next.{/size}"
    ki "Hey...can you make this thing go any-"

    play sound "vibrate.mp3"
    scene sexgrindcumyeah16 with hpunch

    ki "Hah!"
    r "Oh shit! Oh shit! We really have to stay on this the whole time?! We can’t even take breaks?!"
    no "Don’t tell me you’re so weak that you can only last several seconds on Irene. She deserves far better than that, Rin."
    r "Sorry, Irene! But if you could maybe...slow down a bit...that would be nice!"

    scene black
    with dissolve2

    no "Irene, Matilda — please enter second gear."
    ki "Second gear? But first is- ah! Aaaaaah fuck. Oh god, I need one of these for my room."
    n "Ugh, no. You’d never get off of it."
    r "Ngh...mmf....ngh!"
    mak "Power through, Rin. I know this doesn’t technically count as a Dorm Wars competition, but I’m still pulling for you to win over Kirin since I’m more attached to the first floor."
    mo "Whatever happens...I hope it lasts very long...."

    scene sexgrindcumyeah17
    with dissolve2

    r "Yeah...about that! Probably...not going to happen! "
    r "This is...way more intense...than fingering! And this...is only second gear! "
    n "Nodoka, how many gears are there exactly?"
    no "Ten."

    scene sexgrindcumyeah18
    with dissolve

    r "Ten?!?!?!"
    no "Yes. Joking aside, you two appear to be rather weak if this is all you’re able to handle."

    scene sexgrindcumyeah19
    with fade

    ki "Hah...hah...this...is nothing! I can handle...at least...up to eighth gear..."
    r "What happened to...not caring about the competition?! Just...finish already! Put us...out of our misery!"
    ki "Misery?...Are you kidding?...I edge myself for fun every weekend...I’ve got...endurance like...you wouldn’t believe!"
    mo "While we were out partying, Kirin was studying the blade. And by blade, I mean Matilda. "
    n "You really need to find some new hobbies, Kirin."
    ki "Go...fuck yourself..."
    ki "Or me...either one works..."
    mak "Can Rin actually compete here? "
    sa "I don’t know...even with the...handicap...Kirin seems to be...hanging on...a lot better..."

    scene sexgrindcumyeah20
    with fade

    r "I’m...fine, okay?! This thing is just...hah! This thing...is really good at its job!"
    no "I offer only the best up to my precious contestants. And fabulous prizes to those who win as well."
    r "What does...the winner even get?!"
    no "Hmm...the satisfaction of {i}eventually{/i} climaxing? But at a later stage in time than the loser?"

    scene sexgrindcumyeah21
    with dissolve

    r "How is that a prize at all?!"

    play sound "vibrate.mp3"
    scene sexgrindcumyeah22 with hpunch

    r "Hngh! "
    no "Shush, you. You’re scaring Irene."
    r "Irene can...fuck off!"

    play sound "vibrate.mp3"
    scene sexgrindcumyeah23 with hpunch

    r "Aaagh!"
    mo "The tongue! The tongue is out! The fabled ahegao approaches! Nithhala is nearing the end of her great journey!"

    scene sexgrindcumyeah24
    with fade

    r "I already said...I’m fine! I can...hang on longer!"
    no "Third gear, engaging."

    play sound "vibrate.mp3"
    with hpunch

    r "HNGH!!"
    ki "Oh fuck...ooooh fuck..."
    ki "I’m gonna...cum so fucking hard once this is done...oooooh fuck..."
    n "Looks like Kirin’s getting close too."

    if kirin_lust > 49:
        ki "No way...I’ve got...way too much...experience under my belt...to lose to a...virgin on a sex machine..."
        r "Hah...hah...I’m only...a virgin by...some metrics! Some people...would say...that ship has sailed already!"
        ki "Either way...there’s no way I’m losing to the likes of you..."

        scene sexgrindcumyeah25
        with dissolve

        ki "I will {i}watch{/i} though...cause {i}God{/i} you look hot right now..."
        r "Hngh...mngh...please...don’t watch...I already...can’t take it!"
        ki "Why not? You can watch me too...unless you don’t {i}like{/i} watching me grind my little pussy back and forth...but you do...right, Rin?..."
        r "Hah...hah..."
        ki "You little perv...I bet you wish...you were grinding all over my face right now instead, don’t you?..."
        r "I didn’t...until you said that!..."
        ki "Come on over, baby. Get off the machine and I’ll finish you myself. I’ve always wanted to try using my tongue on a girl..."
        mak "Is verbal assault like this against the rules in any way or are there truly no limits to this madness?"
        no "I see nothing wrong with Kirin’s method here. In fact, it seems rather effective based on Rin’s current state."

        play sound "static.mp3"
        scene sexgrindcumyeah26 with flash
        stop sound

        ki "Just think, Rin..."
        ki "You...and me...Two girls who barely even know each other...exploring our bodies...kissing each other all over...hah..."
        ki "Don’t you want me to touch you?...Don’t you want me to play with your pussy?..."
        r "Kirin......stop!"
        ki "Come on...I know you’re wet...I can see you shaking..."
        ki "I just want to {i}help{/i} you..."

        scene sexgrindcumyeah27
        with dissolve

        r "Kirin...stop! Holy shit!"
        ki "No..."
        ki "I want to lick you...I want to taste you..."
        ki "I want to nibble on your little clit...I want to eat you out until you’re begging for-"
        r "No more! Can’t...take it!"
        ki "Until you’re {i}begging{/i} for me to {i}fuck{/i} you and cumming your brains out all over the floor!"

        scene sexgrindcumyeah28
        with dissolve

        r "Hah! Oh god! Oh god! I can’t! I’m...hah!"
        r "I’m cumming!...I’m cumming! I-"

        with sexfade
        with sexfade
        scene sexgrindcumyeah29 with cumflash
        with hpunch

        r "AAAAaaaAAAAhhh! AAAaaaaAAAAAhhh! AAAAAaaaaaaaHHHHH!!!!!!!!"

        scene black
        with dissolve2

        r "Aaah!......Hah!......."
        r "Oh no...oh, fuck...I lost...didn’t I?..."
        mak "Quite dramatically, at that."
        no "Ladies and- well, only ladies. It appears that your winner is Kirin Kanda. "
        no "Now, if our friends could clear the stage, I’d like to begin preparations for-"
        ki "Wait!"

        scene sexgrindcumyeah24
        with dissolve

        ki "Turn...the machine up! I still...haven’t finished!"

        scene sexgrindcumyeah30
        with dissolve2

        no "Oh? Is it my responsibility to make sure that happens? I can’t just shut the machine off?"
        ki "No! Don’t shut it-"

        play sound "computerboo.mp3"

        ki "Hah! No! Nodoka! Turn it back on! Please!"
        no "Perhaps ask Rin if she would like to take you up on your {i}fantasy{/i} from a moment ago? I imagine she would be able to help, would she not?"
        ki "Rin...please...fuck me..."
        r "Hah...hah...can’t...breathe...can’t...think..."

        scene sexgrindcumyeah31
        with dissolve

        no "Alas. What a shame it is to see that you’ve-"

        scene sexgrindcumyeah32
        with dissolve

        no "Wait. What are you doing?"
        n "Rescuing my friend, of course."
        ki "Noriko! Thank-"

        play sound "vibrate.mp3"
        scene sexgrindcumyeah33 with hpunch

        n "Don’t worry, Kirin! I already know how these things work! Straight to tenth gear we go!"
        no "Wait! Stop! Matilda!"

        scene sexgrindcumyeah34
        with fade

        ki "HAH! FUCK!"
        no "She’s a secondhand machine! She can’t withstand the tenth gear! "
        n "Yeah, well neither can Kirin. So neither one of them will have to stand it for long!"
        ki "FUCK FUCK FUCK FUCK FUCK FUCK! YES! YES YES YES! JUST LIKE THAT! JUST...HAH!"

        scene sexgrindcumyeah35
        with dissolve

        ki "AAAAAAAH! HAAAAAH! AAANGHHHHH!"
        mo "Another journey meets another end?! Two prophecies fulfilled in one night?!"
        ki "CUM.......CUM..........."

        scene sexgrindcumyeah36
        with dissolve

        ki "CUMMING!!!!!!!"

        with sexfade
        with sexfade
        scene sexgrindcumyeah37 with cumflash
        with hpunch

        ki "NNNNNNNNNNGGGHHHHGNNNNNGH!!!!!!!!!!!!!!!"

        scene black
        with dissolve2
        play sound "computerboo.mp3"

        no "{i}Hah...{/i}fantastic. Now I’ll have to find {i}another{/i} machine for next year’s rerun."
        ki "Hah...hah...hah..."
        n "Okay, guys! Looks like the winner of this round is Kirin! Now, please help me mop up the floor to prepare for whatever Nodoka’s final competition is."

        $ kirinnod2win = True

    else:
        scene sexgrindcumyeah38
        with dissolve

        ki "Hah...hah...{i}who’s...{/i}getting close now?"
        n "You, obviously. But this is exactly what you get for riding that thing without your panties on. Just look at Rin. She’s doing great."
        r "Hah! Fuck! Shit! Hah! So good! So good!"
        n "Okay, maybe “great” isn’t accurate. But still, she’s doing better than you."
        ki "She...is not! I’m...doing fine! I just...hah!"
        no "Jumping to fifth gear."
        r "Fifth?! But I can barely-"

        play sound "vibrate.mp3"
        scene sexgrindcumyeah39 with hpunch

        ki "HAAAAH!"
        r "NGHHHHHHHHHH!!!! IRENE!!!!! STOP IT!!!!!!"
        n "Kirin, just cum already. There’s literally no reason to hold yourself back at this point."
        ki "HAH! HAH! I DON’T...WANT IT TO END! I WANT...TO RIDE IT FOREVER!"
        n "Just go buy one from Makoto’s mom. They sell them over at her place."
        mak "Why do you know that?"
        n "I have my reasons, okay?"
        ki "I...can buy one?!"
        no "Sixth gear."

        play sound "vibrate.mp3"
        scene sexgrindcumyeah40 with hpunch

        ki "AAAAAAAH! CUMMING, CUMMING, CUMMING!"

        with sexfade
        with sexfade
        scene sexgrindcumyeah35 with cumflash
        with hpunch

        ki "AAAAaaaaAAAaAAaaaaaAAAAAHHHHhhhhh!!!!!!~~~~~~"

        play sound "static.mp3"
        scene sexgrindcumyeah28 with flash
        stop sound

        r "Oh, thank god! "

        with sexfade
        with sexfade
        scene sexgrindcumyeah29 with cumflash
        with hpunch

        r "AAAAAH! AAAH! HAAAAAH! HAAAAAAAAAAAAAAH!"

        scene black
        with dissolve2

        r "Hah! Oh my god...oh my god...I just came...in front of half my class...oh my god..."
        n "Yeah, but I think it’s safe to say we’ve all lost a little bit of dignity today."
        sa "Not Molly...or Makoto..."
        no "{i}Yet.{/i} But, given that their names are the only two that remain in the box, what will become of them is yet to be seen."
        no "Now, if everyone could please help me mop up the stage to prepare for the final contest, it would be greatly appreciated."

        $ rinnod2win = True

    mo "{i}Hah...{/i}I sure wish Sir was here. I’m positive he’d love Nodokathon just as much as I do so far."
    sa "Yeah..."
    sa "I imagine he’s...probably really bored right now..."

    stop music

    $ renpy.end_replay()
    $ sportswars18 = True

    jump sportswars19

label kirinspring1:
    scene noonsky
    with dissolve2
    play music "ame.mp3"
    play sound "phonering.mp3"

    "I’m minding my own business when, suddenly, my phone rings. "

    play sound "phonebeep.wav"

    "And while this would not be anything worth noting on its own, I figured I’d let {i}you{/i} know since Kirin is the one calling and that probably means I’m going to have sex."

    s "Hey."
    ki "Hi! What are you doing right now?"
    s "Castrating myself. Sorry to ruin your plans for the day."
    ki "Can I keep what’s lopped off as a souvenir? A memento of all the great times we once had?"
    s "Sure. Just make sure you split the memento with Noriko since she never got to have actual sex with me."
    ki "Bad decisions aside, come meet up with me."
    s "But you just said “bad decisions aside” and that is very obviously a bad decision."
    ki "Why is it a bad decision? What is that supposed to mean?"
    s "It’s supposed to be an acknowledgment of how improper our relationship is. But I guess that wouldn’t click for someone who can’t grasp the concept of that."
    ki "Oh, lame. Well, we’re going on a date and you can’t say no. Meet me near my place in an hour."
    s "I don’t like this assertiveness. Bring back the cute Kirin who says cute things and wears that very tight dress."
    ki "Mmmmm no. Bye!"

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve

    "Kirin hangs up the phone and I guess I now have something (or someone) to do this afternoon."
    "Was I {i}planning{/i} on getting laid today? No. But I never really plan on doing that since it always sort of happens no matter {i}what{/i} I do. And today will be no exception."

    stop music
    scene thegreatbluehole
    play sound "seek.mp3"

    "{b}which is good because i keep thinking about the clockless watch on my baby-like wrist//how the bones don’t fit like they did in her{/b}"

    scene black
    play sound "likepigstopigwater.wav"

    "{b}{size=+20}WHAT AM I SUPPOSED TO DO NOW??????{/b}{/size}"

    play sound "static.mp3"
    scene kirinmadyo1 with flash
    stop sound
    play music "ame.mp3"

    ki "Oh, good! You made it."
    s "And only had one mental breakdown on the way."

    scene kirinmadyo2
    with dissolve

    ki "As if {i}you{/i} have anything worth being tormented over when you live in a world where everyone will still want to fuck you no matter {i}what{/i} you do."
    s "You have no idea how accurate that is."
    s "Also, aren’t you supposed to be weirdly in-tune with mental impairments and {i}not{/i} the type to accuse someone of being too privileged to bypass them?"
    ki "You know, I’m really glad you mentioned {i}tune,{/i} because that’s pretty relevant to what I wanted to do today!"
    s "No, I will not teach you how to play the piano. Ask someone else."

    scene kirinmadyo3
    with dissolve

    ki "You know how to play the piano?"
    s "No — which is why I won’t teach you. "
    ki "Damn. I was actually a little impressed for a second."
    s "Well, you shouldn’t be. I am talentless and miserable and only good for inducing orgasms."
    ki "Well, at least we have that in common. Now, come with me."
    s "Where? "
    ki "To wherever the fuck I want to go. It’s my date. And I literally just gave you a hint."
    s "Yes, but the only answer I can come up with in regard to that hint is a place I definitely don’t want to go."

    scene kirinmadyo4
    with dissolve

    ki "Well, that’s too bad because it isn’t up to you!"
    s "Kirin-"

    scene noonsky
    with dissolve2

    ki "This way, Sensei! I’ve already called ahead and reserved a time-slot for us!"
    s "You’ve had this planned the whole time?"
    ki "Mhm! I just really feel like singing today! And you’ve never gotten to hear my voice either! So, come on! It’ll be fun!"
    s "What if I never showed up?..."
    ki "Then I’d just have to go alone!"
    ki "Or find another random boy who wants to come with me. But hey! Nothing bad ever happens in karaoke booths, right?"
    s "..."
    ki "Senseiiiii! Let’s gooooooo!~"

    scene black
    with dissolve2
    stop music fadeout 20.0

    "She knows."
    "There’s no way she doesn’t."
    "But how did she find out?..."
    "She and Karin aren’t the type who actually {i}talk{/i} to one another now...are they?"
    "And if they {i}are{/i} talking, why does Kirin even care? "
    "Is it just jealousy?"
    "Is she only grilling me about this because she wanted to be {i}there{/i} for it?"
    "I don’t know...and she’s so busy dragging me down the road like an oversized doll that I don’t even have time to wrap my head around it."
    "My hands begin to sweat. She notices. She wipes hers off before repeating that same contact again. "
    "She keeps doing it. Hand to hand. Skirt. Awkward stare upward. Hands again. I’m in trouble."
    "No. It’s not trouble. It’s jealousy. Hands again. Skirt. "

    ki "Something wrong, Sensei? You seem a little more nervous than usual."
    s "I’m fine."

    "I’m fine."

    ki "You’re fine?"

    "I’m fine."

    s "I’m fine."

    "I’m not fine."
    "But I should be fine because this is a thing I’m fine with now and it doesn’t matter if I hurt Karin since Karin is just a side character and I don’t need her to progress. Right, Pareidolia?"
    "{b}wrong.{/i}"
    "Shit."
    "{b}when you were younger, you loved cereal.{/b}"

    play sound "static.mp3"
    scene cereaaal with flash
    stop sound
    play music "snowchildren.mp3"

    "I did?"
    "{b}yeah. you loved the little toys that came in the little boxes.{/b}"
    "{b}and you were the type of spoiled brat who was never okay with only having one of them. so you wanted to collect them all.{/b}"
    "That doesn’t sound like me."
    "{b}you have no idea what you actually sound like since you’re always focusing on bone conduction rather than the product of your voice and the air.{/b}"
    "What?"
    "{b}think of it like this, akira. the you inside of you is a different you from the you outside of you.{/b}"
    "{b}and the you outside of you isn’t as much of a bitch as the you inside of you.{/b}"
    "Okay, but what does that have to do with cereal?"
    "{b}i’d have gotten to that part already if you hadn’t interrupted me.{/b}"
    "I’m sorry. I’m a bad boy."
    "{b}only because you keep focusing on bone conduction. but that’s beside the point.{/b}"
    "{b}you loved cereal. but cereal is bad for your teeth. it can turn them into liquid. and your mother wanted to protect you from liquid teeth.{/b}"
    "{b}your father had a sweet tooth as well. but his vice was candy, not cereal.{/b}"
    "I don’t remember my father."
    "{b}no one does.{/b}"
    "I don’t remember my mother either."
    "{b}yeah. well a mixture of childhood trauma and timeline fuckery will do that. BUT ANYWAY, CEREAL.{/b}"
    "Sorry, Pareidolia."
    "{b}even today, you want to collect them all.{/b}"
    "{b}and no matter how many times you tell yourself you don’t, you know you’re wrong.{/b}"
    "{b}you’ll regret that one day. but you’ll live in bliss for now, pretending to be a better man than you actually are — which isn’t so much of a man at all.{/b}"
    "{b}you’re just a little boy with a walk-in toy box. and if you want to play with something, you CAN.{/b}"
    "Okay. I’m sorry for talking back, Pareidolia."
    "{b}don’t apologize to me — apologize to kirin for almost raping her big sister.{/b}"

    stop music
    play sound "static.mp3"
    scene kirinmadyo5 with flash
    stop sound
    play music "undersea.mp3"

    "{b}THEN TELL HER TO FUCK OFF AND STOP GETTING IN THE WAY OF WHAT NEEDS TO BE DONE{/b}"
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa shit"

    ki "Well, we’re here! "
    ki "I wonder what song I should sing first?"
    s "..."

    scene kirinmadyo6
    with dissolve

    ki "Any preference, Sensei? Is there a certain genre you try to stick to when you come here with other girls?"
    s "I don’t-"
    ki "You {i}don’t{/i} come here with other girls? Really? Because that’s not what I heard, Sensei."
    s "I don’t...have a genre I try to stick to..."

    scene kirinmadyo7
    with dissolve

    ki "Oooooh! {i}That’s{/i} what you meant!"

    scene kirinmadyo8
    with dissolve

    ki "Sorry. Guess I got a little ahead of myself there."
    s "..."
    ki "Something wrong, Sensei? It’s not like you to be so {i}uncomfortable{/i} in a dark room with a defenseless girl."
    s "And it’s not like you to beat around the bush instead of saying what you really want to say."

    scene kirinmadyo9
    with dissolve

    ki "No. I guess it’s not, is it?"
    s "..."
    ki "I guess we’re {i}both{/i} dealing with something we’re not really sure of how to handle then, huh?"
    s "..."

    scene kirinmadyo10
    with dissolve

    ki "Ahh...this is so annoying. I hate having to be the good guy. "
    ki "But having a story arc without some sort of hero in it just doesn’t make much sense, huh?"
    ki "We can’t {i}both{/i} be villains this time, Sensei."

    scene kirinmadyo11
    with dissolve

    ki "And it is for that reason that I must ask you what you did to my sister."
    s "You have to..."
    s "You have to...{i}ask{/i} me?"
    s "You don’t already know?"
    ki "I know that {i}something{/i} happened. And I know that she’s really beaten up over it. But all I have to work with is context."
    ki "And the context that I {i}do{/i} have, Sensei...it doesn’t paint a very good picture."
    s "..."
    ki "This is the part where I tell you to hurry up and spit it out since we only have this room for two hours and I don’t have time to watch you hesitate for the next ninety minutes."
    s "Why do you even care?"

    scene kirinmadyo12
    with dissolve

    ki "What do you mean, {i}why do I care?{/i}"
    s "I mean you’re the same girl who routinely gets turned on by the thought of me treating everyone you know like human-sized tissues I can soak up my cum with before tossing aside."

    scene kirinmadyo13
    with dissolve

    ki "Wha...since when?!"
    s "Since I first met you. But you can go ahead and pretend you were never like that since I don’t want to ruin your “good girl” arc when it’s just getting started."

    scene kirinmadyo14
    with dissolve

    ki "Wow. Okay. So {i}that’s{/i} how we’re going to do this, huh?"
    s "How else would you prefer? Because tricking me into thinking we were hanging out before luring me into a place I’m not comfortable with doesn’t exactly scream “friendly chat” to me."
    ki "Did you stop to think that maybe me doing that should have given you the hint you needed to confess without me having to force it out of you?"
    s "I did. But then you immediately started trying to force it out of me without giving me {i}any time at all{/i} to tell you what happened on my own."
    ki "Well, {i}would{/i} you? Because you’ve had a long fucking time since shit happened to do just that and all you’ve done is leave me in the dark."
    s "I’m not sure. Maybe? Want to spend the next ninety minutes listening to me hesitate before finding out?"

    scene kirinmadyo15
    with dissolve

    ki "You’re {i}spicy{/i} today. All that quarantining get you a little pent up? Is {i}that{/i} why you raped my sister? Couldn’t hold back anymore?"
    s "I didn’t {i}rape{/i} your sister, Kirin."

    play sound "static.mp3"
    scene kirinmadyo16 with flash
    stop sound

    se "Because my good boy would never {i}rape{/i} someone! He’d just convince them that they {i}want{/i} to have sex. Right, Aki-kun?"
    ki "Wait, you didn’t?"
    s "..."

    "{i}Ignore Her...{/i}"

    ki "Well...what the fuck’s she so beaten up about then?"
    s "Have you not talked to your sister {i}at all?{/i}"

    scene kirinmadyo17
    with dissolve

    ki "No, because she won’t fucking {i}tell{/i} me anything! I had to find out from Miku that you two came here together! But ever since she came back, she’s seemed friggin’ traumatized!"
    se "Aki-kun, what’s your childhood friend’s band called again? I wanna sing one of her songs."

    play music "shiningstarinstrumental.mp3"

    se "Oh, nevermind. Found it! Forgot she was an idol. I should’ve been one of those. Idols can get away with anything."
    s "Kirin...just because I didn’t do anything to Karin doesn’t mean I didn’t {i}want{/i} to. That’s what she’s probably traumatized about."

    scene kirinmadyo18
    with dissolve

    ki "But...nothing actually {i}happened?{/i}"
    s "No. I ran away like a little bitch after a failed and somewhat subconscious attempt at coercing her into taking her clothes off for me."
    se "Some girls just don’t understand what a catch you are, Aki-kun! It’s okay!"
    ki "You still like...touched her, though. Right?"
    s "There was some grappling involved. We may have ended up on the floor. "

    scene kirinmadyo19
    with dissolve

    ki "So...the two of you came here together...you tried to get into her pants...brought her to the ground...and then ran away before actually getting into them?"
    s "Yup. "

    scene kirinmadyo20
    with dissolve

    ki "Oh."
    ki "Well, that’s not nearly as bad as I expected. But still, keep your hands off of Karin. "
    s "I don’t think my putting my hands {i}on{/i} her is much of an option anymore, to be honest. She basically told me she doesn’t want anything to do with me anymore."

    scene kirinmadyo21
    with dissolve

    ki "Well...good for her, I guess. But it’s kind of fucked up that you even {i}tried{/i} getting with her in the first place when you can use me for that stuff any time you want."
    s "There’s the Kirin I know."
    ki "I never went anywhere. But where’s the Sensei {i}I{/i} know? You’ve been fuckin’...weird all afternoon."

    play sound "static.mp3"
    scene kirinmadyo22 with flash
    stop sound

    s "I’m right here."

    play sound "static.mp3"
    scene kirinmadyo23 with flash
    stop sound

    se "Me too! I wanna see if you’ve learned any new tricks while I’ve been getting eaten by worms."
    ki "Wha...is this seriously the time for this? I’m trying to, like...scold you and stuff."
    s "It’s nice that you’re trying to be a good sister for once. I’ve always thought you’re the cutest when you’re trying to do the right thing."

    scene kirinmadyo24
    with dissolve

    ki "And now you’re just...saying stuff you know will get to me. That’s not fair."
    s "You know..."
    s "If you had been there with us, I don’t know if I’d have ever touched Karin at all."

    scene kirinmadyo25
    with dissolve

    s "Can I really use you “any time I want,” Kirin?"
    ki "..."
    s "Can I use you right now?..."
    s "Will you get off from being fucked in the same spot where I almost took your big sister?"

    scene kirinmadyo26
    with dissolve

    ki "..."
    s "You’ve always wanted to...{i}explore{/i} with her, haven’t you? Are you just pretending to be mad because I almost took that opportunity from you?"
    ki "You’re being {i}too{/i} spicy now. I don’t like this."
    s "Why not?"
    ki "Because it’s fucking weird, that’s why. "

    scene kirinmadyo27
    with dissolve

    ki "I get that shit’s been hard or whatever. But if that’s the truth, I want to {i}see{/i} that. And all I see right now is some douchebag trying to talk his way out of trouble."
    s "..."
    ki "I know I’ve probably said some shitty things before...and I even probably meant them in the moment, but..."
    ki "If you’re going to fuck my big sister, just...make sure it’s consensual, okay?"

    scene kirinmadyo28
    with dissolve

    ki "I don’t want to, like...deal with her acting all sad at home and shit."
    s "..."
    ki "..."
    s "Kirin."
    ki "What now?"

    scene black
    stop music

    s "Bend over."

    play sound "tackle.mp3"

    $ renpy.end_replay()
    $ kirinspring1 = True
    $ kirin_lust += 1

    "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
    "{i}She can’t win against you!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label christmaskirin1:
    if _in_replay:
        play music "stpartynight.mp3"

    ki "{i}Ahem.{/i}"

    play sound "static.mp3"
    scene kirinxmad1 with flash
    stop sound

    s "..."
    ki "..."
    ki "I said...{i}ahem!{/i}"
    s "Uhh..."
    s "Bless you?"

    scene kirinxmad2
    with hpunch

    ki "That was a cough, not a sneeze!"
    s "Do you...want me to ask Touka if she has any NyQuil or something?"
    ki "No, idiot! I want you to apologize to me so we can go back to being normal again and put an end to all this frustrating tension!"
    s "Oh. My bad. Apologize for what, though?"

    scene kirinxmad3
    with dissolve

    ki "I can’t really remember. Something with my sister, I think."
    s "You mean that time I tackled her to the ground and completely ruined my relationship with her? The one that I already informed you about?"
    ki "I don’t know. Probably."
    s "Well, what else would it be? Because I-"
    ki "We can just call it the Karin thing and be done with it. I’m waiting."
    s "So...Wait, I still don’t really get what I’m apologizing for. You already know what happened. We even had sex afterward."
    ki "Yeah. But it wasn’t even, like...{i}that{/i} enjoyable."
    s "You came like six times."

    scene kirinxmad2
    with hpunch

    ki "{i}Four!{/i} Now, stop making me yell! It’s embarrassing!"
    s "Kirin, what are you doing?"

    scene kirinxmad4
    with dissolve

    ki "I don’t know, okay?! Like, I’m mad at you for some reason! But I don’t fully understand it and I don’t want to go back to normal like nothing happened! But I {i}also{/i} don’t want to stop spending time with you!"
    s "That sounds both extremely complicated and extremely on-par with your character thus far."
    ki "Feeling bad isn’t supposed to be a part of my character! I’m the cool sex-friend! Feelings are for people like Ayane and Noriko! Not me!"
    s "So...what do you want me to do? Take you into some secret room and fuck you back to normal or something?"
    ki "Yes! But only after you apologize and things go back to normal."
    s "Kirin, {i}you’re{/i} the one making things {i}abnormal{/i} right now. I’m completely fine with going back to the way we were whenever you want. {i}You’re{/i} the one who’s been avoiding me."
    ki "Why?!"
    s "Why...are you avoiding me?"

    scene kirinxmad5
    with dissolve

    ki "Yeah! Like...why would I do that?"
    s "If I had to take a guess, you’re probably just pissed off at me for what I did to your sister because you secretly love her."
    ki "No. That’s ridiculous. It has to be something else."
    s "Okay. So you’re totally cool with me fucking her then?"

    scene kirinxmad8
    with hpunch

    ki "Don’t even fucking-"

    scene kirinxmad6
    with dissolve

    ki "Oh my God. That {i}is{/i} what it is."
    s "You really didn’t know that?"
    ki "No! I’m not supposed to be like this!"
    ki "Like, yes. I like you now. I have accepted that. It’s a thing. But literally anyone with half a brain would want to bone Karin and it doesn’t make sense for me to be mad if-"
    s "Kirin, you’re not mad because I want to bone Karin. You’re mad because I upset her and you care about her."

    scene kirinxmad7
    with dissolve

    ki "No, because why would I want you to apologize to {i}me{/i} then?"
    s "You don’t. You’re just dumb."

    scene kirinxmad8
    with dissolve

    ki "And {i}you’re{/i} an asshole!"
    s "I sure am. "
    s "So, are we back to normal yet?"
    ki "If I say yes, can we go talk somewhere more private so everyone isn’t looking at me anymore?"
    s "No one is looking at you. I put up my anti-eavesdropping barrier that I break out whenever I have private conversations in crowded rooms. So there really isn’t any {i}reason{/i} to go somewhere more-"

    scene black
    with hpunch
    play sound "tackle.mp3"

    ki "Shut up! We’re going somewhere else."
    s "Okay, but you’re underestimating how large this place is and we’re totally going to get lost."

    stop music
    play sound "static.mp3"
    scene kirinxmad9 with flash
    stop sound

    ki "{i}We’ll be fine. I downloaded the Tsukioka Manor navigation app.{/i}"
    s "{i}Oh, right. That’s a thing. I’m telling you though, we really don’t need to-{/i}"
    ki "{i}You don’t have some kind of forcefield, Sensei! Now, give me your hand!{/i}"
    s "{i}We’re holding hands too?{/i}"
    ki "{i}No! I’m simply pulling you along!{/i}"
    s "{i}With interlaced fingers? Is that really necessary?{/i}"
    ki "{i}It’s so you can’t get away!{/i}"
    c "............................................................."
    r "...what do you think about that, Chika?"

    scene kirinxmad10
    with dissolve2

    c "I think that doesn’t look like “love” at all."
    r "...{i}What?{/i}"
    r "We were talking about Secret Santa. {i}What{/i} doesn’t look like-"

    scene black

    c "Tick tock. "

    play sound "static.mp3"
    scene kirinxmad11 with flash
    stop sound
    play music "hallelujah.mp3"

    "Kirin drags me through Tsukioka Manor until we reach an area almost entirely devoid of life, save the straggling butler and occasional maid."
    "It seems the entire place is decorated for Christmas, though. So it’s hard finding a space to remind her that we don’t live in a beautiful, happy world where everything can always go the way we want."
    "It’s something the two of us know, sure. But it’s also something we delude ourselves into thinking isn’t the case at times because escapism comes easier than accepting that."
    "I’ve been fine with being avoided by her. Because, on one hand, my absence in regard to {i}anyone{/i} is nothing short of an improvement. "
    "But even if she was pained by it, the idea of her being crushed by the weight of her sisterly love or whatever you want to call it seemed even greater. Just in a good way."
    "Of course, that was never meant to last. She can love her sister {i}and{/i} think that she loves me. And I can encourage her or bully her or do whatever it takes to turn her on since it’s different any given day."
    "We’ll end up on a bed again soon. We’ll tell each other we’re bad people...then kiss or something. And it’ll feel great. But it’ll also feel empty. "
    "It’s kind of like waking up Christmas morning and finding a bunch of presents with nothing in them."
    "Box after box of unrealized joy, because it’s never been what’s on the inside that counts. It’s always been the wrapping."
    "She wore a bow for me today. "
    "I can not wait to open her."

    s "..."
    ki "Do you...really think I love my sister?"
    s "I’d be extremely surprised if you didn’t."
    ki "Oh? And why is that?"
    s "Because we’re alike."
    s "We both pretend not to care as much as we actually do. And while I’m sure the reasons for that are different, I can understand the basics like the back of my hand. It just...keeps things easier."
    ki "I guess it...doesn’t sound like the end of the world when you put it that way."
    s "Yeah..."
    s "You wouldn’t believe how the end of the world really looks."

    scene kirinxmad12
    with dissolve

    ki "{i}Hah...{/i}I could be talked into believing anything right now with how...all over the place I’ve been lately."
    ki "This has been eating at me more than you probably know. And, like...it’s so fucking {i}dumb.{/i} Like, why am {i}I{/i} more hung up on it than {i}she{/i} is?"
    s "Because it’s the first time I’ve hurt anyone really close to you."
    ki "You hurt Noriko like every fucking week."
    s "Yeah, but Karin is different. You’ve known her your whole life."
    s "You’ve seen firsthand just how much of a ball of sunshine she is. Faulting you for cursing my solar eclipse of an existence helps nothing or no one at all."
    ki "I’ve always hated the sun."
    s "That’s not true. You thrive during all of our beach trips."
    ki "Only when you’re around. But that’s because I {i}have{/i} to if I want to stand out."
    ki "Do you have any idea how fucking...difficult it is having to compare myself to {i}her{/i} every day, though? "
    ki "I want nothing more than to just...be able to fucking {i}hate{/i} her because I have no shortage of reasons to. But she..."
    ki "Karin puts me before {i}everyone.{/i}"
    ki "That has to be why she didn’t tell me. She knows how much you mean to me and she...didn’t want to shatter that image when, like you said, nothing {i}technically{/i} happened."
    s "Why {i}do{/i} I mean so much to you, Kirin?"
    ki "I don’t know..."
    s "Is it just because I give you attention?"

    scene kirinxmad13
    with dissolve

    ki "Well, why do you like {i}me?{/i}"

    scene kirinxmad14
    with dissolve

    ki "If you even...{i}do{/i} like me, I mean."
    s "Of course I like you. "
    ki "Well, it’s sure as fuck not because I give {i}you{/i} attention then. You get that from fucking everyone."
    s "Yet it fixes nothing."

    scene kirinxmad12
    with dissolve

    ki "..."
    s "Even if everyone ever starts looking at you, Kirin..."
    s "If you get all the attention you’ve ever dreamed of...If you become that “perfect girl” you see your sister as..."
    s "You’re not going to be any happier. Because that’s when you’ll pivot to not thinking you deserve it."
    ki "So I’m just doomed to fucking hate myself for the rest of my life then?"
    s "It’ll get easier to stop hating yourself when you stop trying so hard to be liked."

    scene kirinxmad15
    with dissolve

    ki "Is that what you’re doing then? Just...trying to get people to like you? "
    s "Or hate me. Depends on the mood I’m in. "
    s "Seems to always backfire though since I’ve done that with you and {i}you’re{/i} still interested in me for whatever reason you’ve landed on."

    scene kirinxmad16
    with dissolve

    ki "Yeah..."
    ki "If almost raping my sister didn’t make me want to leave you behind, I’m worried nothing will."
    ki "I’ve never felt that strongly about anyone before. It’s scary."
    s "Now imagine you {i}keep{/i} feeling it."
    s "And imagine every time you do, there’s something {i}else{/i} that shows up out of nowhere and pulls it away."

    scene kirinxmad17
    with dissolve

    s "So you try to chase after it...even when you know you’ll never catch up. And you’re aware that it would be so much easier to just {i}stop{/i} and...find something similar, but you can’t."
    s "Until you {i}can.{/i} But then that gets pulled away too."
    s "I wish I was you. "
    s "I wish I could just...{i}not{/i} feel strongly about anyone or {i}anything.{/i} But that’s only because I’ve been beaten down by how it feels to do the opposite to the point where I can barely even breathe nowadays."

    play sound "static.mp3"
    scene kirinxmad18 with flash
    stop sound

    dia "Woah there, friend! Perhaps it’s time you ease back on all the melodrama? It’s Christmas after all! Today’s not the day to get all sentimental like this. You’re probably boring the poor girl!"
    s "Yeah...you’re probably right."
    s "Kirin doesn’t care about what happened to me. She doesn’t care about the steps I took and all of the shit I fell over to get here."
    s "She only cares about how I make {i}her{/i} feel. The rest is just noise."
    s "I’m a tool, like everything else. One that she can use to make herself grow. "
    dia "Now you’re getting it! "
    s "And one day...many years from now, if we ever manage to get there, I’m sure she’ll look back on all of this as a great learning experience."
    s "She’ll regret letting me do what I did to her. She’ll regret feeling this strongly at all. She’ll regret me."
    s "I just hope she doesn’t have to go through what it’s like to have me plucked from her hands."
    dia "Oh, Akira. How have you fallen so far? Your eyes were so bright when you were young. "
    dia "Don’t you remember all the time we spent together? Were {i}we{/i} plucked from your memories as well? Or were we simply casualties of time itself while you moved on and became an adult?"
    s "An adult?..."
    s "Is that what you think I am?"

    play sound "static.mp3"
    scene kirinxmad19 with flash
    stop sound

    s "I have not grown...a day in my life."
    s "It’s all just a lie I tell myself to sleep better at night. "
    s "But when even my lying doesn’t help put me to sleep anymore, what’s there left to do?"
    ki "Stop..."
    s "Stop what? I-"

    scene kirinxmad20
    with dissolve

    s "...oh."
    s "Sorry, Kirin."
    s "I’m seeing things today."
    ki "Well, whatever you’re seeing isn’t right! I don’t think you’re a tool at all! It’s not like that! "
    s "Our entire relationship is built on you storming into my office and trying to sell me your virginity."

    scene kirinxmad21
    with dissolve

    ki "Who gives a shit about what it’s {i}built{/i} on?! That’s not what it is anymore! "
    ki "Tons of shit has happened since then and...now I...Sensei, I-"
    s "Don’t say it..."
    ki "Fuck you! I {i}want{/i} to feel this for once! You don’t get to take that from me!"
    ki "I’m tired of nothing ever being enough! And I’m tired of forcing myself to {i}not{/i} feel things! But if that’s going to make me end up like {i}you,{/i} fuck it! I’ll feel everything ever right fucking now!"
    s "Don’t, Kirin..."
    ki "I...{i}love{/i} you."

    scene kirinxmad22
    with dissolve2

    ki "I won’t regret anything about whatever this is...or whatever it winds up being."
    ki "If it’s just history when everything is said and done, then...fine. I’ll deal with that when it happens."
    ki "But that other thing you said...about not wanting something to pluck you from my hands?..."
    ki "What the fuck, Sensei?..."
    ki "I’m supposed to be the one depriving myself of experiences and now {i}you{/i} want to do that {i}for{/i} me? Once I’m finally starting to accept that I {i}shouldn’t?{/i}"
    ki "Maybe {i}I’m{/i} just the tool then? Maybe {i}I’m{/i} the one who-"
    s "I love you too."

    scene kirinxmad23
    with dissolve2

    ki "................"
    s "..."
    ki "{i}What?...{/i}"
    s "Why do you think I didn’t want you to say it?"
    ki "You..."
    s "Maybe we {i}should{/i} run away? "
    s "Because even if we’re forced back here in the end, it sounds like something that could be good for us."
    s "A way to...deceive ourselves into thinking we’re decent people when we’re really just two perpetual train wrecks."
    ki "You...{i}love{/i} me?..."
    s "I shouldn’t."
    ki "But...you {i}do.{/i}"
    ki "You’re not just saying that."
    s "Yeah."
    ki "Okay..."
    ki "Why?"
    s "Why what?"
    ki "Why do you love me? I’ve been terrible basically the entire time I’ve known you. Was starting to own up to that really all it took to-"
    s "I think I have for a while, if we’re being honest."
    ki "And you just..."
    ki "You just...kept that to yourself. Didn’t think it was at all relevant to {i}me.{/i}"
    s "I just want you to hate me."
    s "I’m tired of falling, Kirin. I just want someone to put me out of my misery at this point."
    ki "Let’s do it."
    s "Run away? Or put me out of my misery?"
    ki "Neither. Let’s like, {i}literally{/i} do it. Because I’m feeling extremely emotional right now and I feel like the only way I can get better is by seeing what it feels like to “make love” instead of “fuck” for once."
    s "It’s more or less the same at the end of the day. The only thing that changes is the monologue."
    ki "Is that why all I can hear inside of my head right now is screaming?"
    s "It’ll go away in time."
    ki "Are we doing it or not?"
    s "We-"
    ki "Trick question. The answer is yes. "
    s "Kirin-"
    ki "You can “Kirin” me all you want later. "

    scene black
    with dissolve2

    ki "I want {i}this{/i} moment to be a good one for once..."

    "........."
    "......"
    "..."

    scene kirinxmad24
    with dissolve2

    "She kisses differently when she’s happy."
    "Both times I’ve experienced it, she’s been wearing this dress."
    "Maybe it’s good luck. Or maybe it’s just something about the way it fits her that makes me want to chop her into pieces and box her up so she can stay by my side forever."
    "It’s hard to explain how I’m feeling right now. But it’s like that any time I fall for {i}anyone.{/i}"
    "Like Kirin, though, I’m tired."
    "I’m tired of doubting myself when it comes to things like this. I’m tired of being one step away from “happy” just to lose my footing after pretending to see a copperhead. "
    "By all rights, Kirin Kanda is a terrible person. "
    "By all wrongs, I have fallen for her."
    "May the two of us be banished to hell — for it is the only place we’d be accepted."

    ki "Mmnh! Mm! Again..."
    s "I love you..."
    ki "I love you! Mmnch! Sensei! I love you!"
    ki "Mmh! Mnh! Again!"
    s "Kirin..."
    ki "{i}Again!{/i}"
    c "{i}Ahem.{/i}"

    stop sound
    play sound "static.mp3"
    scene kirinxmad25 with flash
    stop sound

    ki "Ah..."
    s "Oh...shit."
    c "..."
    ki "..."
    ki "Uhhhh........"
    ki "Hi?"
    c "Oh, don’t mind me. "
    c "I’ll just {i}watch.{/i}"
    ki "Can you, like...not?"
    s "Chika-"

    play sound "static.mp3"
    scene kirinxmad26 with flash
    stop sound

    c "You know, I was {i}kinda{/i} worried that maybe Sensei had been lying to me about only fucking girls he loves when the two of you left the room together! But now I know he wasn’t! Further proof that I’m winning!"
    ki "W...Winning? What are you-"
    c "You should probably stop crying if you’re about to fuck, though. Sensei has this thing about not sticking it in girls with tears in their eyes and, while I get that sex is emotional and stuff, maaaaaaybe get over it?"
    s "How do you even-"

    scene kirinxmad27
    with dissolve

    c "Because I’m your perfect girlfriend! How {i}else{/i} would I know something like that about you? Nothing gets past me! No-siree! "
    c "Except the fact that all of the sexual experience Kirin has been touting has apparently been about you! Silly Chika! But if {i}you{/i} have found something to like about her, I’ll just have to believe it!"
    c "Maybe she’s super tight? Maybe she makes cute noises or something? I don’t know! Guess I’ll find out soon, though! Please continue!"

    play sound "static.mp3"
    scene kirinxmad28 with flash
    stop sound

    ki "Uhh...no thank you?"
    ki "Under normal circumstances, I’d be, like...all for this. But this is {i}kind of{/i} a special moment that I don’t really want someone lurking in the corner for..."
    c "Sensei supports it, though! Don’t you, Sensei?"
    s "..."

    scene kirinxmad29
    with dissolve

    ki "Sensei?..."
    s "I’m not going to be able to make her leave, Kirin..."
    ki "What the fuck even {i}is{/i} this? "
    s "It’s...hard to explain."
    c "Not really!"

    play sound "static.mp3"
    scene kirinxmad27 with flash
    stop sound

    c "Sensei is my boyfriend! But he has an interesting, super-awesome take on love that allows him to “love” a whole bunch of people at one time! And {i}you{/i} are one of those people!"
    c "We made an agreement where he still gets to fuck them and stuff. But since I’m his {i}actual{/i} love, I should probably be able to watch. Or join in! Just to make sure you’re doing everything correctly. "
    c "You’re still totally special, though! So if you’re currently beating yourself up about how this doesn’t make you unique or that it isn’t “true love” or whatever, just stop. That’s, like...so immature. Right, Sensei?"

    play sound "static.mp3"
    scene kirinxmad30 with flash
    stop sound

    ki "What the fuck is she going on about?..."
    spo "{b}SPORK.{/b}"
    s "Kirin..."
    s "Maybe we should pick this back up after the Christmas party?"

    stop music
    play sound "broken.mp3"
    scene kirinxmad31

    "{size=+12}{b}YOU ONLY THINK YOU LOVE HER{/b}{/size}"

    scene kirinxmad32
    $ renpy.pause(7, hard=True)

    $ renpy.end_replay()
    $ christmaskirin1 = True
    stop sound

    jump christmaskirin2

label christmaskirin2:
    play sound "static.mp3"
    scene kirinretrieval1 with flash
    stop sound
    play music "samhain.mp3"

    ki "You!"
    n "Me?"
    ki "No, {i}you!{/i}"
    y "Me?"
    n "Her?"
    ki "Yes!"
    y "Do you...want some?"
    ki "Yes! But not in the context you are referring to!"

    scene kirinretrieval2
    with dissolve

    n "Kirin, what’s going on? It’s not like you to storm into a room with feelings any bigger than concern for the amount of penises you have inside of you."
    ki "What’s “going on” is that I was having perhaps the single cutest moment of my young life and that fucking {i}semen demon{/i} showed up and ruined everything!"
    y "Which one? You’ve gotta realize that’s how I see like 90%% of the class at this point."

    scene kirinretrieval3
    with dissolve

    ki "Chika! Who else would I come to {i}you{/i} screaming about?! Get with the fucking program, Yumi! Do something!"
    y "The fuck do you want {i}me{/i} to do? Throw meat at her? I’m eating."
    ki "I don’t care what you do! Just make her go away so I can make passionate love to the teacher!"

    scene kirinretrieval4
    with dissolve

    y "Why is nothing easy anymore?"
    n "{i}Love?{/i}"
    ki "Or...sex or...fucking or whatever you want to call it."
    n "Kirin, tell us exactly {i}what{/i} happened or we won’t be able to do anything about it."
    y "Are you not fucking listening? I won’t be able to do anything about it either way. Chika’s like an entirely fuckin’ different person all of a sudden and I ain’t got the faintest fuckin’ idea about how to handle her."
    n "Okay. But still, Kirin should tell us everything anyway because I’ve never heard her use the phrase “making love” in regard to herself before and I want to know how that found its way into her head."

    scene kirinretrieval5
    with dissolve

    ki "It...It doesn’t matter what led to me learning new phrases! I was just talking to Sensei and stuff and then...you know...semen demon!"
    n "I’m pressing X so hard right now. You don’t even {i}know.{/i}"
    y "Did she swipe him from you or some shit? Because if that’s the case, just let her have him for a little while and wait until she’s done. There ain’t shit any of us can do about it. Girl’s fierce as all hell."
    ki "Well, it’s...less like she {i}swiped{/i} him and more like I...{i}gave him away...{/i}"

    scene kirinretrieval6
    with dissolve

    n "Then take him back, idiot! Telling me is counterproductive when I want him even harder than you do! "
    ki "Nuh-uh! You’re too nice to take him for yourself, so I know you’ll help me! And Yumi’s the only person I know who can probably reason with Chika!"
    n "Stop using my martyr complex against me! It’s too effective! I’m in!"
    y "Well, {i}I’m{/i} not. I don’t give a shit about whoever is fucking the teacher at any given moment here."
    y "In fact, maybe he can screw Chika back into being an actual human again? Beats me. Only one way to know for sure. Can I eat now?"

    scene kirinretrieval7
    with dissolve

    n "No. You can eat later. We have to go save Kirin’s heart. This is the first sign of life it has ever showed and I’ll be {i}damned{/i} if I let it slip through the cracks."
    y "Why are you touching me?"
    n "Because we’re in love."
    y "No. We ain’t."
    n "I’ve already talked you out of wearing the sarashi and I will talk you out of heterosexuality next."

    scene kirinretrieval8
    with dissolve

    y "You haven’t talked me out of shit, weirdo!"
    n "Those double-D’s say otherwise, damn it."
    ki "Can you two stop flirting and come help me already?! I want my moment back!"

    scene black
    with dissolve2

    n "To the Batmobile! Away!"
    y "Wait! Don’t take my fuckin’ food out of my-"
    n "You won’t be able to focus if there’s meat around! I know how omnivores function! Kirin, where are we going?"
    ki "It’s, like...half a mile that way. Just hug the wall and you won’t get lost!"
    y "What are we even supposed to be doing?!"

    play sound "static.mp3"
    scene kirinretrieval9 with flash
    stop sound

    "The mission was simple — infiltrate the bedroom and find a way to restore Kirin’s first “lovemaking” opportunity. "
    "But just because it was simple didn’t mean it would be easy. Chika Chosokabe was rabid after all. And it takes a trained professional to deal with creatures like that. "
    "Or a gun. But Ayane Amamiya wasn’t around. And Kirin wasn’t about to ask {i}her{/i} for help since A — she didn’t know where she was. And B — she didn’t think Ayane would help to begin with."
    "Regardless, Kirin was trying not to think about what might be happening behind that door because she didn’t want her first taste of love being wasted on someone else."
    "At the same time, though, she was beginning to question whether or not it was “love” to begin with if Chika was telling the truth about the way Akira had been spreading himself out."
    "She was thinking about all sorts of things to try and cope with this loss. Things she didn’t want to say out loud. Things that would embarrass her. Things about the past and things about the future. "
    "But more than anything, she simply didn’t want this to slip away."
    "For far too long, she’s been letting that happen — pretending she doesn’t want what she {i}knows{/i} she does because she feels like she needs to fit a certain image in order to stand out."
    "But this time — this time, she thought it would be okay to want something. So much so that she didn’t even think about how this might be hurting those she brought here to help her."
    "If it would even hurt them at all, that is. "
    "They have much thicker skin than she does."

    ki "They were in there the...last time I saw them."
    n "And you just...left them there? In what is presumably a romantic bedroom with a really soft king-size mattress?"
    ki "I think it was bigger than a king. It was one of those princess bed things."

    scene kirinretrieval10
    with dissolve

    n "Oh, Kirin...You left Sensei and {i}Chika{/i} alone on a princess bed? Leaving him in that situation with {i}anyone{/i} is a recipe for disaster — let alone a girl who, according to Yumi, has gone absolutely cock-crazy."
    y "Okay, for the record, I have never used the term “cock-crazy” in my life."
    n "It’s accurate though, isn’t it?"
    y "I don’t fuckin’ know, man. She’s just...friggin’ delusional all of a sudden. Like she’s thrown out all reason and morals or whatever because she thinks he’ll tell her to fuck off if she doesn’t."

    scene kirinretrieval11
    with dissolve

    n "That’s a classic case of cock-craziness, alright. So basically, to help Kirin, we must first help {i}Chika.{/i}"
    ki "Help {i}Chika{/i} later. Just rescue Sensei for now so he and I can pick up where we left off and screw-love-fuck each other’s brains out."
    n "Got it."

    play sound "dooropen.mp3"
    scene kirinretrieval12
    with dissolve

    n "Well, the first course of action is finding out if they’re-"
    c "{i}Yes! Yes! Harder! Just like that! Oh, fuck! I’m cumming! I’m...fucking cumming!{/i}"

    scene kirinretrieval13
    with dissolve

    n "Uh...phase one complete, I guess."
    ki "{i}Hah...{/i}"
    y "Thank you for forever tainting my ears, Noriko. Now, even if me and Chika {i}do{/i} manage to get close again, I’ll be stuck remembering the way she sounds when she’s getting her back blown out."
    n "I’m honestly surprised to find out that’s not something you’ve already heard before."

    scene kirinretrieval14
    with fade

    y "Yeah! Well, unlike you two, I try to {i}avoid{/i} situations where I’d be bumping into people having sex!"
    n "It’s not like I’m actively {i}trying{/i} to encounter that! I love Sensei more than anyone! He’s just...having sex like 50%% of his waking life! It’s going to happen if you’re involved with him!"
    ki "Of {i}course{/i} he was just lying..."
    ki "That makes way more sense than expecting he’d actually be able to fall for a girl like me."
    n "Hm? What was that about lying? I couldn’t really-"
    ki "Don’t worry about it, Noriko. I’m just making myself look like a fucking idiot again for thinking anyone would ever choose {i}me{/i} over someone else."

    scene kirinretrieval15
    with fade

    n "What? But you’re not-"
    ki "Nice?..."
    ki "Smart?..."
    ki "Funny? Caring? Pretty?..."
    ki "Why?..."
    ki "Why is it so much harder to name things that I’m not than things that I {i}am?!{/i}"

    scene kirinretrieval16
    with dissolve

    n "That’s not what I was trying to-"
    ki "I...I know! Because you {i}are{/i} good! Too good! Fucking...annoyingly good! You’re the exact type of person who someone {i}would{/i} fall for! I’ve never been that! Not for a day in my life!"
    ki "So why did I fucking {i}believe{/i} it, Noriko?! Why did I think for even a second that I might be wrong about myself?! About who I am and what I’m worth?!"
    n "Kirin-"
    ki "I’m going home..."
    ki "Thanks for trying."

    play sound "footsteps.mp3"
    scene kirinretrieval17
    with dissolve2

    n "..."
    y "{i}Now{/i} do you see why I never try to get involved with any of this shit?"

    scene kirinretrieval18
    with dissolve

    n "Huh?..."
    y "All this romance and...sex and...{i}everything.{/i}"
    y "All it does is make people fucking crazy. "
    y "Everywhere I look, someone’s either getting hurt or...changing everything about themselves for no reason other than wanting to be with someone else."
    y "Isn’t being alone just...so much safer than that?"
    n "It is...but we already know that, Yumi. Sensei knows it too. That’s why he’s so desperately trying to push everyone away all the time."

    scene kirinretrieval19
    with dissolve

    y "Then why-"
    n "Because we can’t help it."
    y "I don’t..."
    y "I don’t get it."
    n "Neither do I. But no one said there needs to be logic to any of this. We’re just a bunch of idiots running around trying to experience and feel new things."
    n "You might be perfectly content with just never doing that. And that’s awesome. But Kirin can’t sit still the way you can."

    play sound "static.mp3"
    scene kirinretrieval20 with flash
    stop sound

    n "{i}She’s always wanted someone to look at her. But not like how you and I look at each other. Like...REALLY look at her. As a girl...a woman...a princess...whatever she wants to be that day.{/i}"
    n "{i}But she’s never felt like she deserves it. So of course she’d take it hard on herself if...{/i}"
    n "{i}If she heard the person she’s been trying to catch the eye of say one thing then do another.{/i}"
    y "{i}Well...what the fuck do you think he said to her then?{/i}"
    n "{i}The same thing you’ll want to hear sooner or later when YOU can’t sit still anymore.{/i}"
    n "{i}The most terrifying...most amazing thing you could ever say to anyone.{/i}"
    n "{i}I think that’s what she heard tonight.{/i}"
    n "{i}That’s why I’m not chasing after her.{/i}"

    "But Noriko didn’t {i}need{/i} to chase after Kirin."
    "She’d find her way back to normal sooner or later."
    "She just needed to hurt a little first. "

    if ayanelust10 == False:
        "And what better place to hurt than all on your own?"

        ay "Kirin? Is everything-"
        ki "Fuck off, Ayane. You’re the second-to-last person I want to talk to right now."

        scene kirinretrieval21
        with dissolve
        stop music fadeout 10.0

        ay "What? Who the hell is the last then?"
        ki "Another blonde! Just...one parading as something she’s not!"
        ay "...Rin?"
        ki "No! Fucking...ugh! "
        ki "Merry Christmas! Goodnight!"

        scene black
        with dissolve2

        ay "G...Goodnight?"

        "{i}Kirin has left the party!{/i}"

        $ renpy.end_replay()
        $ christmaskirin2 = True
        $ kirin_love += 1
        $ kirin_love -= 2
        $ kirin_love += 4
        $ kirin_love -= 3
        $ kirin_love += 3
        $ kirin_love -= 1
        $ kirin_love += 5
        $ kirin_love -= 1
        $ kirin_love += 2
        $ kirin_love -= 2
        $ kirin_love += 3

        "{i}Her affection is all over the place!{/i}"
        "........."
        "......"
        "..."

        jump christmasotoha1

    else:
        "And what better place to hurt than in the arms of a rival?"

        ay "What the hell happened to {i}you?{/i}"

        scene kirinretrieval22
        with dissolve

        ki "Oh, wouldn’t {i}you{/i} like to know?!"
        ay "A little, yeah. But only because I’m mildly curious about what sort of tragedy it would take to make you look like you’re actually experiencing human emotions for once."
        ki "Cool! So let’s fucking talk about it then!"
        ay "What?"
        ki "You and me! Let’s talk! Right now!"

        scene kirinretrieval23
        with dissolve

        ay "Why? I don’t want to know {i}that{/i} badly."
        ki "Because no one else will fucking get it!"
        ay "And I will?"

        scene kirinretrieval24
        with dissolve

        ki "I don’t fucking know, Ayane! Just come over here!"
        ay "Ugh...seriously?"

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene kirinretrieval25
        with dissolve2

        ay "So, did one of our classmates rape {i}you{/i} this time?"
        ki "Obviously fucking not."
        ay "Oh, okay. I just figured that since it was something “no one else would get,” it had to be that."
        ki "She might as well have. Certainly fucking feels like she did."
        ay "Yeah, I think you might be lacking some critical understanding of how it feels to be sexually assaulted here."
        ki "I’m fucking sorry about that, okay?"

        scene kirinretrieval26
        with dissolve

        ay "Yup. You’re completely forgiven now. Thanks, Kirin."
        ki "Ayane, you’re in love with Sensei. Right?"

        scene kirinretrieval27
        with dissolve

        ay "Of course."
        ki "And if I said {i}I{/i} was too...what would you think about that?"
        ay "I’d think that you’re a delusional and hypersensitive piece of shit human who could never possibly feel such a wholesome emotion."

        scene kirinretrieval28
        with dissolve

        ki "Right?!"
        ay "You weren’t supposed to agree."
        ki "No, I {i}do{/i} agree! Because that’s {i}exactly{/i} how I’m supposed to feel! But all of a sudden, my whole fucking world has been flipped on its head and I don’t know what to do about it!"
        ay "Uhhh..."
        ki "What if I really {i}do{/i} love him, Ayane? How can I ever expect him to {i}actually{/i} love me when I’m like...this?"

        scene kirinretrieval29
        with dissolve

        ki "You’re like...the ideal girl. Better than me at virtually everything. Except for maybe, like...blowjobs."

        if ayanebjcontest == True:
            ay "I’m better at those too. I won the contest the second time you forced me into sexually engaging with you. Remember?"
            ki "Yeah, but I’ve improved a lot since then. "
            ay "Fantastic."

        else:
            ay "Thank...you?"

        ki "Either way, I can’t fucking hold a candle to you. So if, for some reason, Sensei {i}did{/i} tell me he loves me...it would totally {i}have{/i} to just be him fucking with me. Right?"
        ay "He didn’t...actually {i}say{/i} that. Did he?"
        ki "He might have. But it might have also been in the middle of him talking to, like...ghosts or something? I don’t know. It was weird."

        scene kirinretrieval30
        with dissolve

        ay "{i}Hah...{/i}"
        ki "I’ve never felt this way before, Ayane. I have no idea what to do."
        ki "Like, it makes total sense for you to be all broken up about him fucking everyone ever. But for {i}me,{/i} that’s only, like...kind of mattered. But now it suddenly matters a lot more and I hate it."
        ay "And you want...what? My advice on how to cope with that? Even though you’ve effectively traumatized me for life and I want you to go away forever?"
        ki "Yeah. Kind of."

        scene kirinretrieval31
        with dissolve

        ay "You have no shame at all, do you?"
        ki "Sure I do. I actually feel super bad about the whole sexual assault thing since you took it way worse than I ever expected you to."
        ay "You expected me to enjoy being sexually assaulted?"
        ki "Maybe a little? "
        ay "...No."
        ay "That’s fucking stupid, Kirin."
        ki "Yeah! That’s why I’m all shameful about it. But at the end of the day, I still like...want to be friends with you and stuff."

        scene kirinretrieval32
        with dissolve

        ay "{i}What?{/i}"
        ki "Yeah. I, like...really admire you, Ayane. "
        ay "And {i}I,{/i} like...really want to throw up now."
        ki "Like it or not, we have a lot in common. So shouldn’t you {i}want{/i} to help me if it means I’ll become less of a shitty person and stuff?"
        ay "I think you’re overestimating just how much I {i}can{/i} help you. "
        ay "There’s no secret method when it comes to coping with the man I love having sex with, like...all of my friends. It sucks. And it’s going to keep sucking forever. But it’s unavoidable when it comes to Sensei. "
        ki "I see, I see..."
        ki "But when he tells you he loves you despite that...you still believe him?"

        scene kirinretrieval33
        with dissolve

        ay "It sounds...extremely stupid when you put it that way. But yeah. "
        ki "Do you think he’s just like...poly then?"
        ay "I don’t know, Kirin..."
        ay "But what I {i}do{/i} know is that he has an extremely hard time both thinking {i}and{/i} saying those words to anyone."

        scene kirinretrieval34
        with dissolve
        stop music fadeout 10.0

        ay "So if he said them to you...I doubt he was lying."
        ki "...Really?"
        ay "Stop looking at me like that. I don’t want to feel bad for you."
        ki "Thank you, Ayane...Really."
        ki "And I’m sorry. I’m seriously...seriously sorry."
        ki "I know that we probably won’t ever be friends again after what I did to you. But if you ever-"
        ay "Are we done here?"

        scene kirinretrieval35
        with dissolve2

        ki "...Yeah."

        scene black
        with dissolve2

        ki "Sorry again..."

        "{i}Kirin has left the party!{/i}"

        $ renpy.end_replay()
        $ christmaskirin2 = True
        $ kirin_love += 1
        $ kirin_love -= 2
        $ kirin_love += 4
        $ kirin_love -= 3
        $ kirin_love += 3
        $ kirin_love -= 1
        $ kirin_love += 5
        $ kirin_love -= 1
        $ kirin_love += 2
        $ kirin_love -= 2
        $ kirin_love += 3

        "{i}Her affection is all over the place!{/i}"
        "........."
        "......"
        "..."

        jump christmasotoha1
