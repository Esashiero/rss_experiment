label callharukamorning:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callmorning
    if harukanumber == True and day89 == False:
        "I think I should probably get to know Haruka a little better before calling her."
        jump callmorning
    if harukaresortticket == True and day == 6:
        jump makihornytrip1
    else:
        if cafeclosed == False:
            "Haruka should be working right now. I can probably talk to her at the cafe if I want to spend time with her."
            jump callmorning
        else:
            play sound "phonebeep.wav"

            "I tap on Haruka's name in my phone and wait for her to answer."
            "........."
            "......"
            "..."
            "There's no answer..."
            jump callmorning

label callharukaafternoon:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callafternoon
    if harukanumber == True and day89 == False:
        "I think I should probably get to know Haruka a little better before calling her."
        jump callafternoon
    elif harukadate1 == True and harukadate5 == False:
        play sound "phonebeep.wav"

        "I tap on Haruka's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer...She's probably at work anyway."
        "..."
        "I hope she doesn't still feel weird about what happened at the bar the other night."
        jump callafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Haruka's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        h "Hello?"
        s "Hey, it's me. What are you up to right now?"

        if cafeclosed == False:
            h "I'm still at work. Did you need something?"

            "Damn. Looks like Haruka's busy. I should probably wait until she's done working to ask her out."

            s "It's nothing urgent. I can just call you later."
            h "Okay...I'm sorry! Make sure you really {i}do{/i} call me later though, okay?"
            s "Sorry, Haruka. {i}I make my own rules.{/i}"
            h "...What?"

            play sound "phonebeep.wav"

            "I hang up the phone and decide to call someone else instead."
        else:
            h "Oh, you know. Just trying to get my life back together and convince the government I wasn't having sex in my cafe when we both know I was."
            s "Sounds like fun."
            h "It's not."
            s "Oh."
            s "Well, I guess I'll leave you alone then."
            h "Okay. Talk to you later, I guess."
            s "See you, Haruka."

            play sound "phonebeep.wav"

            "I hang up the phone and decide to call someone else instead."

        jump callafternoon

label callharukanight:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callnight
    if harukasex == True:
        "What do I want to do?"
        menu:
            "Hang out":
                jump callharukanighthang
            "Doggystyle sex (Raise Lust)" if bonus == True:
                jump harukadogrep
            "CAPS LOCK HUG (Raise Lust)" if bonus == False:
                jump harukadogrep
    else:
        jump callharukanighthang

label callharukanighthang:
    if harukanumber == True and day89 == False:
        "I think I should probably get to know Haruka a little better before calling her."
        jump callnight
    if haruka_love >= 0 and day89 == True and harukadate1 == False:
        jump harukadate1
    elif haruka_love >= 0 and haruka_love <= 4 and harukadate1 == True and harukadate5 == False:
        play sound "phonebeep.wav"

        "I tap on Haruka's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer."
        "..."
        "I hope she doesn't still feel weird about what happened at the bar the other night."
        "Oh well...I guess I'll just have to...keep visiting her at the cafe or something for now."
        jump callnight
    if haruka_love >= 1 and haruka_love >= 5 and harukadate1 == True and harukadate5 == False:
        jump harukadate5
    if haruka_love >= 15 and harukadate10 == True and harukadate15 == False:
        jump harukadate15
    if haruka_love >= 20 and dormwar17 == True and harukainvite1 == True and harukadate20 == False:
        jump harukadate20
    if haruka_love >= 30 and makihornytrip4 == True and harukasex == True and harukadate30 == False:
        jump harukadate30
    if chap4active == True:
        jump harukaspringnightgen
    if chapthreeactive == True:
        jump harukasummer2nightgen
    if christmas7 == True:
        jump harukanightgen2
    else:
        jump harukagennight

label harukacafe:
    if haruka_love >= 5 and haruka_lust >= 5 and harukafirstlust == False:
        jump harukafirstlust
    if haruka_love >= 10 and halloween14 == True and harukadate5 == True and rindorm35 == True and harukadate10 == False:
        jump harukadate10
    if day > 5 and yasuspring3 == True and harukaspring1 == True and harukaspring2 == False:
        jump harukaspring2
    if chap4active == True:
        jump harukaspringcafegen
    if chapthreeactive == True:
        jump harukasummer2cafegen
    if christmas7 == True:
        jump harukamorninggen2
    else:
        jump harukacafegen

label harukainvite:
    if harukainvite1 == False:
        jump harukainvite1
    if harukainvite1 == True and harukaskipped == False and harukainvite2 == False:
        jump harukainvite2
    if harukainvite3 == False and harukadate20 == True and harukasex == True:
        jump harukainvite3
    else:
        jump harukainvitegen

label harukainvitegen:
    play sound "phonebeep.wav"

    "I tap on Haruka's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    h "Hey! What's going on?"
    s "Not much. Was wondering if you were busy today."
    h "Oh, you know me. Just wallowing in self-pity and scrolling through pictures of more attractive girls on Instagram."
    s "That sounds about right."
    h "Life is dumb. Let's hang out."
    s "Works for me. Was actually just about to ask if you wanted to come over."
    h "Of course! As long as you promise that your [niece] won't attack me or say anything about my boobs."
    s "I will do my very best..."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene harukainvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    h "So...is there anything you wanted to do tonight?"

    "How should I spend my time with Haruka?"
    menu harukainvmenu:
        "Hang Out (Raise Affection)":
            jump harukainviteaff
        "Reverse Cowgirl (Raise Lust)" if harukasex == True and bonus == True:
            jump harukareverse
        "Kiss. Jk, I Mean Hug. (Raise Lust)" if harukasex == True and bonus == False:
            jump harukareverse
        "Headpat" if harukasex == True and bonus == True:
            jump harukaheadpat

label harukainviteaff:
    scene harukainvitegen
    with fade

    "Haruka and I spend the night relaxing on my bed, alternating between watching videos on her phone and random television shows on my...well, television."
    "Our arms press up against one another as we struggle to make good use of what little space there is on this bed."
    "It's not something I mind, but it's something that makes me feel a little bit strange whenever I recall the fact that she belongs with someone else."
    "Instead of backing away, though, I only move closer."
    "Close enough that I can feel her breath on my skin whenever she turns to me to explain some meme I don't understand."
    "And I guess you could say that I feel her breath pretty often given that virtually every single meme she shows me makes little to no sense to me."
    "It's surprising how youthful Haruka is despite being so close to my age, but-"

    if nikidate5 == True:
        "I suppose I can also be youthful for my age at times."
    else:
        "That age is really just my estimation of this {i}body's{/i} age."
        "How old was I before I showed up here?"

    scene black
    with dissolve

    "I shrug off an impending mid-life crisis and chalk my lack of Internet knowledge up to a lack of overall interest in the topic."
    "But just because it's not my cup of tea doesn't mean I'm going to force Haruka into doing something she doesn't want to do."
    "And, as long as I'm able to keep feeling her breath on my neck and the light pressure of our arms as we squeeze closer on the bed, I have everything I came for."

    if harukasex == True:
        if bonus == True:
            "It's a horrible thing to say, but I'm glad I coaxed her into cheating on her husband."
        else:
            "It's a horrible thing to say, but I'm glad I decided to start hugging her behind her husband's back."

        "I like Haruka a lot. And each time the two of us are alone together like this, I become even more aware of that."
        "Sure, it's not something even close to love- and I definitely don't have any intention of ever {i}proposing{/i} to her."
        "But her company is strangely calming if you're able to kill off all of the negative aspects that come along with it."
    else:
        "Part of me wonders how things would have been if I had pushed her into a more intimate relationship when I had the chance."
        "And moments like this make me feel like there is an infinite amount of chances. An infinite amount of opportunities to destroy what she loves most."
        "But all I've ever done is destroy things- and it gets boring after a while."
        "If what it takes to preserve her long-shot at happiness is a slightly more mundane life, it won't kill me to trade away some of that fun."

    "I might not need Haruka, but it's becoming clear that she needs someone else."
    "And today, I just happen to be the closest thing to her."

    $ haruka_love += 3
    stop music fadeout 5.0

    "{i}Haruka's affection has increased to [haruka_love]!{/i}"

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


label harukareverse:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump harukareversex
    else:
        $ haruka_lust += 3
        stop music fadeout 5.0

        "{i}Haruka's lust has increased to [haruka_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label harukanightgen2:
    scene harukanightgen2
    with dissolve
    play music "love.mp3"

    "I decide to keep Haruka company at her place for the night."
    "I know how easily she gets lonely and I get along with her rather well, so it's an easy decision for me to make."
    "Nothing interesting happens. We just sort of chill on her couch and order a pizza."
    "And while nights like this aren't exactly going to go down in history as glorious or amazing moments, they're always welcome."
    "Sometimes, all people need is to relax for a little while and forget about their obligations."
    "For Haruka, that probably means abandoning thoughts of the cafe for the night."
    "And for me, I guess it's something along the lines of..."

    if bonus == True:
        "Not worrying about who is going to find out that I'm having sex with some of the class?"
        "But hey, another cool thing about Haruka is that I'm pretty sure I could flat out tell her I'm doing that and she'd get just as excited about it as I am."
    else:
        s "Oh no. I forgot to pay the water bill."
        h "Oh no."

    scene black
    with dissolve

    "We watch a few episodes of some cooking show together and, after it gets to be a little late, I decide to head back."
    "Haruka offers to let me crash on the couch (Probably to help quell her unending desire for company) but I already have Ami texting me to come home so I have to refuse."
    "She understands and says goodbye to me as I put my shoes back on."
    "Out of the corner of my eye, I see her open her arms as if she's going to come hug me, but she quickly backs off and I decide to not bring any attention to it."
    "Then, just like most other nights, I walk back out into the cold with my hands in my pockets."

    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka's affection has increased to [haruka_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label harukamorninggen2:
    scene harukamorninggen2
    with dissolve
    play music "cafe.mp3"

    "I decide to start my day with a trip to the cafe and find Haruka sitting on the couch near the window, going over some paperwork."
    "She flags me over and asks if I want anything before leaving to go get me a cup of black coffee."
    "And considering that she's able to procure one while Rin is working, she really demonstrates her power first thing in the morning and I can't help but be impressed."
    "As it turns out, Haruka is exceptional when it comes to giving people what they actually order."
    "That is no small feat based on my experience with Koi Cafe, so I'm really starting to think she actually cares about me."
    "We spend the morning chatting and not paying much attention to things happening around the cafe."
    "It's a slow day, so none of her employees seem to mind and, instead, they just let us go on uninterrupted- talking about nothing and sitting a little closer together than we probably should."

    scene black
    with dissolve

    "Not all good things last forever, though."
    "Even though it's slow, it doesn't change the fact that Haruka needs to take inventory so, reluctantly, she ends our little get together and forces me back into the street."
    "Well, realistically, she doesn't force me anywhere. But it's clear that I've already overstayed my welcome and that I should probably be on my way..."

    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka's affection has increased to [haruka_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label harukacafegen:
    scene cafeten5
    with dissolve
    play music "cafe.mp3"

    "I stop at the cafe first thing in the morning and strike up a conversation with Haruka."

    if harukasex == True:
        "She does her best to split her time between me and her employees, but clearly winds up favoring me in the long run."
        "The line of customers is pretty substantial for it only being 8 AM, so I'm surprised at how attentive she is to my needs instead of theirs."
        "Even with that being said, the part-timers (Rin included) are able to hold things down and serve everyone while Haruka and I make plans to meet up again soon."

        scene black
        with dissolve

        "I'm glad to see that she's able to look past her {i}situation{/i} and see me in a different light than she did previously."
        "And even though our relationship might not have the most wholesome foundation I've ever heard of, I do enjoy spending time with her."
        "Sure, there's always the possibility that she's just using me for sex in the absence of her husband, but that's not something a person like me would complain about."
        "She's free to do whatever she wants. I'm just here for the ride."
        "No pun intended."

    else:
        "Haruka needs to split her time between her employees and me, so I wind up not getting to talk to her as much as I would like."
        "The conversation we {i}do{/i} have is more than enough to take up my morning, though."
        "The two of us clearly have some chemistry with one another."
        "And even though it's hard to decipher exactly what that chemistry {i}is{/i}, I still enjoy spending time with her."

        scene black
        with dissolve

        "Out of seemingly nowhere, a huge group of customers walk into the store and tear any chance I have of continuing the conversation away."
        "That's okay, though. I understand the hardships that come with working in customer service and I let Haruka know that we can just hang out some other time."
        "She smiles nervously in thanks and I tell her I'll call her again as soon as I can before heading back out into the street and getting on with my day..."

    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka's affection has increased to [haruka_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label harukagennight:
    scene harukanightgen
    with dissolve
    play music "love.mp3"

    "I give Haruka a call and decide to spend some of the night at her place."
    "It's a mostly wholesome get-together, with the conversation never really going anywhere unsavory."
    "We sort of just sit around watching TV and reminiscing about when we were younger and further away from death."
    "I'm glad Haruka has a lot to say in that respect because I'm still having a hard time remembering anything from when I was young."

    scene black
    with dissolve

    "I wind up getting a call from Ami in the middle of a movie Haruka and I are watching and am essentially forced to come home when I refuse to tell her where I am."
    "I feel kind of weird letting a [teenage]girl boss me around but Haruka laughs and chalks it up to me only agreeing because I'm 'subconsciously worried' about her."
    "And even though that may be true, I can't help but feel a little bad for leaving Haruka on her own again with how often she talks about being lonely."
    "Either way, it still seems like the two of us are growing closer...So that's definitely something to be happy about."

    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka's affection has increased to [haruka_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label harukadate1:
    "Maybe I’ll see what Haruka is up to?"
    "Now that I think about it, the two of us haven’t really hung out except for that one time she gave me a ride home."
    "And even then it was more along the lines of just...getting to her house and leaving a few minutes later."
    "Besides, she wouldn’t have given me her number if she didn’t want to actually talk, right?"

    play sound "phonebeep.wav"

    "Not knowing what else to do, I tap on Haruka’s name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    h "Hello?"
    s "Hey, it’s-"
    h "I know who it is. I've had your name in my phone since I asked you to check on Rin for me."
    s "And you haven't bothered calling? Do you even like me?"
    h "Hey, you haven't called either!"
    h "Is everything okay, though? Is this about Rin again? Because she seemed fine earlier today and-"
    s "Everything is fine. I was just wondering what you were doing tonight."
    h "Tonight? I was going to hang out at Sara’s bar."
    h "Do you...want to come or something?"
    s "Sure. If you guys are cool with having me."
    h "I'm sure we are, but let me check anyway! Hold on a sec."

    "A moment of silence passes by as Haruka does...whatever."

    h "Sara says you're free to come so long as you spend a lot of money."
    s "What if I just come, spend a normal amount of money, and keep you company?"
    h "Hmm...well, I {i}do{/i} seem like the loneliest person at the bar..."
    s "You’re probably the only customer at the bar in general."
    h "Also correct. So, are you going to come over now, or?..."
    s "Yeah, I’m on my way. Don't get too drunk without me."
    h "What's that? You want me to get super drunk without you? I mean...I wasn't going to but, if you insist-"
    s "Haruka-"
    h "Byeeeeee~!"

    play sound "phonebeep.wav"

    s "..."

    "Well, Haruka seems a bit...livelier than normal today."
    "I just hope that she doesn't {i}actually{/i} wind up getting too drunk while I'm on my way over since dealing with her {i}and{/i} Sara that way sounds...hard."

    s "..."

    "Maybe I'll try walking a little faster than normal..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play music "calmbar.mp3"

    "I take a moment to straighten out my clothes before making my way inside."
    "I'm sure no one cares, but it is one of the exceedingly rare opportunities I have to be alone with people actually close to my age and I should at least look the part of a mature human being."
    "Even if my companions for the evening will see me as one giant blur..."

    scene harukabar1
    with dissolve2

    h "Heeeeey! You made it! I’m not alone anymore!"
    sar "I’ve been here with you the entire time..."
    s "Hey, you two. What’s up?"

    "I take a seat next to Haruka, whose face has already gone full-blush from drinking."
    "Sara is busy wiping down the counter in front of us and, surprisingly enough, doesn't seem drunk at all."
    "Which I guess means this will, at least for the time being, be a decently lopsided conversation in which we counteract...however Haruka is when she's drunk."

    h "How was your walk, man? See anything {i}cool{/i} along the way?"
    h "Maybe like a...{i}huge stick{/i} or something?"
    s "..."

    "I immediately understand how Haruka is when she's drunk."

    s "It was a normal walk. I didn’t see anything particularly notable."
    h "Cool, cool. Normal walk. Got it."
    sar "Great icebreaker, Haru-chan."

    scene harukabar2
    with dissolve

    sar "So...you two are friends? Or..."
    h "Don’t talk to her, man. She's drunk."

    scene harukabar3
    with dissolve

    sar "I haven’t even had anything to drink yet..."
    s "Yeah, Haruka. I’ve seen Sara drunk and she-"
    h "Shhhh...You and me are talking right now. She’s just a bartender. It’s my turn to have you."

    scene harukabar4
    with dissolve

    sar "I...probably should have cut her off after five, huh?"
    s "Haruka, you had five beers in the time it took me to get here?"
    s "I called you like fifteen minutes ago."
    h "Five? That’s it? Pfft. Gimme five more. I got this."

    if bonus == True:
        h "Sara’s the one who gets drunk off five beers. I can go all night, if you know what I mean."

        scene harukabar5
        with dissolve

        h "Oh, wait! I didn’t mean it {i}like that{/i}. Hahahahah!"
        h "You’re so naughty, Sensei!"
        s "I didn’t even say anything..."

        scene harukabar6
        with dissolve

        h "Oh, you didn’t? Does that mean I'm...{i}imagining things?...{/i}"
        sar "{i}I’m so sorry...{/i}"
    else:
        sar "Pspspspspspspsppspsssss"

    "Sara whispers across the table as if to say something along the lines of “I had a feeling this might happen” or “I could have prevented this.”"
    "But the truth is, I really don’t mind."
    "Would I have minded if she was a {i}less{/i} horny drunk? Possibly. But this seems like a pretty great turn of events for me."
    "Besides, Haruka works hard enough as-is. It’s probably nice for her to take a load off like this every once in a while."

    s "Can I get a beer, Sara?"

    scene harukabar7
    with dissolve

    sar "Oh, shoot! I forgot to even ask."
    sar "I’ll be right back. I just need to grab some from upstairs since Haru-chan finished everything down here."
    s "And...why exactly do you keep the beer in your apartment instead of in the bar?"

    scene harukabar8
    with dissolve

    sar "Cause it's a lot less fun drinking myself to sleep if I have to keep walking downstairs."

    if bonus == True:
        sar "Now hang out for just a sec and don’t take advantage of my friend while I’m gone."
    else:
        sar "Now hang out for just a sec, and don't even think about hugging while I am away."

    scene harukabar9
    with dissolve

    "Sara disappears upstairs and, moments later, I can hear her footsteps as she moves through her apartment."
    "It makes me realize exactly how old this place must be if I can hear something like that even with the...jazzy piano music playing in the background."

    if sarasex == True:
        "..."

        h "Heheh~"
        s "What?"
        h "Hah...heheheh..."
        s "What’s so funny?"

        scene harukabar10
        with dissolve

        h "Heheheh..."
        s "Haruka, explain your-"

        scene harukabar11
        with dissolve

        if bonus == True:
            h "You two had {i}sex{/i} with each other~"
            s "..."
            h "..."
            s "Yes. That is a thing that happened."
            h "You put your penis inside of my friend."
            s "That would be how sex works, yes."
            h "Did it feel good?"
            s "It normally does."
            h "You gonna do it again?"
            s "Why do you ask, Haruka?"
            h "I don’t knooooow...curiosity?"
            s "Are you looking for an invitation?"

            scene harukabar12
            with dissolve

            h "Maybe you can just film it and send it to me so I can watch it at home?"
            s "I’ll bring it up to Sara next time."

            scene harukabar13
            with dissolve

            h "Dude, I was kidding!"
            h "I tooooootally don’t wanna watch you fuck my friend. That's like...{i}so{/i} gross..."
            sar "Who’s watching what now?"

            scene harukabar14
            with dissolve

            "Sara shows back up out of virtually nowhere and winks at me. There’s not a doubt in my mind that she at least heard the tail end of that."
            "In other news, though, I think I need to buy a video camera."
        else:
            h "Dogs."
            s "What?"
            h "You ever just think of silly they are?"
            s "Not really, no."
            sar "I am returning now!"

        scene harukabar15
        with dissolve

        h "Shhh. Don’t tell her what we talked about. {i}It’s a secret.{/i}"

        if bonus == True:
            s "Is it {i}really{/i} a secret if Sara already told you about us?"
            sar "Hm? What about us? What did I tell you, Haru-chan?"
        else:
            s "Are you...not allowed to talk about dogs for some reason?"

        h "Look! You’re gonna get me in trouble!"
        s "I’m not going to do anything that you weren’t going to do yourself."

    else:
        scene harukabar16
        with dissolve

        h "..."
        s "..."

        "I can’t help but notice Haruka stare off into the distance as soon as Sara disappears."
        "She grows rather quiet compared to how she was just moments ago and it’s...actually kind of confusing."
        "I'm assuming that something is bothering her, but it wouldn't be right for me to just-"

        h "She’s so pretty, isn’t she?"

        "Okay. I guess I'm going to find out after all."

        s "Sara?"
        h "Mhm."
        s "I mean...Yeah. She’s attractive. Why?"

        "Haruka lets out a heavy sigh, eyes still locked on where her friend stood just moments ago."

        if bonus == True:
            h "Why didn’t you have sex with her?"
            s "What?"
            h "Didn’t you turn her down when she was basically throwing herself at you? Why?"
            s "Not to be rude, but how does that involve you?"

            scene harukabar17
            with dissolve

            h "It doesn’t...but it’s confusing."
            h "Sara seemed pretty popular when we were in[school]. She was the kind of girl that everybody just, like...{i}knew.{/i} I was honestly really jealous of her."
            h "I never even had a boyfriend until I turned 18. And even then..."
            s "..."
            h "..."

            scene harukabar18
            with dissolve

            h "Heheh...actually...it’s not like any of {i}my{/i} story involves {i}you{/i}. So I’ll just stop there..."
        else:
            h "I'm just tired of her being pretty!"
            h "I am also tired of her pretending she has to be placed only to immediately come back!"

        scene harukabar19
        with dissolve

        sar "Okay! Supermom has returned!"
        sar "Did you two get along well while I was upstairs? Is anyone pregnant yet?"

        scene harukabar20
        with dissolve

        h "Yeah. We’re having twins. We need your help choosing names."

        scene harukabar21
        with dissolve

        sar "How about...Sana and Sara?"
        s "That...wouldn't bother you? Because it probably-"

    s "Hey. Wait a second."
    s "Where is my beer?"

    scene harukabar22
    with dissolve

    sar "In the cooler, silly. It needs to get cold."
    s "How can you provide such horrible customer service with a smile on your face?"

    if sarasex == False:
        scene harukabar23
        with dissolve

        if bonus == True:
            sar "{size=-10}Maybe I'm still a little mad that {i}somebody{/i} rejected me in my time of need?{/size}"
        else:
            sar "{size=-10}I am going to poison your beverage.{/size}"

        s "What?"

        scene harukabar22
        with dissolve

        sar "Hm? I didn’t say anything."

    else:
        sar "Apologies, sir. But you’re just going to have to deal with it. Please don’t cause a scene in front of my other customers."

        "Right. Forgot about all of her {i}customers{/i}."

    s "Fine. Whatever. I’ll just have some of Haruka’s."

    "I go to reach for Haruka’s beer and-"

    scene harukabar24
    with dissolve

    h "Nuh-uh! No you won’t! This one’s all mine. You’re gonna have to wait for your own."
    s "But that’s your sixth one and I'm stuck at zero for the foreseeable future. "
    h "So?"
    s "So that’s plenty. You’re not planning on driving home, are you?"
    h "I didn't even bring my car. I’m gonna sleep here tonight~"

    scene harukabar25
    with dissolve

    s "You are?"
    sar "{i}You are?{/i}"
    sar "Isn't this a thing I should have known about?"
    h "I just decided right now. "
    h "This is the first time I’ve been with {i}two{/i} friends in forever and I want to drink and have more fun."

    scene harukabar26
    with dissolve

    sar "Aww...Haru-chan is actually being cute and not just horny and lonely for once! What a rare and wonderful sight."
    sar "I’m in. Let’s all get drunk and talk about our feelings!"
    h "Yay!~"
    s "Feelings? What are those?"

    scene black
    with dissolve2

    "Sara runs upstairs for more alcohol and, like you may have guessed, the three of us spend the next couple hours getting drunk and talking about our “feelings.”"
    "Well, those two talk. I just sit there, sipping on warm beer and waiting for one of them to get drunk enough to pass out."
    "With a six-beer head start, the winner is Haruka."
    "Sara, who is in no condition to help when the time comes for us to start wrapping things up, stumbles her way up the stairs and presumably into her bed shortly after."
    "And I-"

    scene harukabar27
    with dissolve2

    "I wind up dealing with this."

    s "Haruka."
    s "..."
    s "Haruka..."
    h "Mmm..."

    "Haruka’s been passed out for around twenty minutes at this point."
    "Knowing that the bar is closed and that no one is around to really...{i}capitalize{/i} on this situation, I likely {i}could{/i} just leave her here without any consequences..."
    "But something about my involvement causes me to feel the slightest bit guilty."
    "And so I will continue to shake her shoulder until she wakes up."

    s "Haruka. Live."
    s "You can’t die here. It would be far too depressing."
    h "Mmm..."

    "I suddenly feel her body begin to move against my hand as she attempts to pull herself off of the counter..."

    scene harukabar28
    with dissolve

    h "Huh?..."
    h "What?..."
    h "What happened?..."
    s "You got drunk."
    h "I did?..."
    s "Very drunk, actually. Sara’s not doing so well right now either."
    s "In fact, she-"

    stop music

    h "Shut up."
    s "..."
    s "What?"

    play sound "static.mp3"
    scene harukabar29
    with flash
    stop sound

    h "I said shut up."
    s "..."
    h "..."
    s "Okay."

    play sound "static.mp3"
    scene harukabar30
    with flash
    stop sound
    play music "pianomelancholy3.mp3"

    h "Mmnh~!"
    h "Mmm...ngh...mnh~ Angh~ mmf~ Mmf!"

    "Haruka’s tongue violently assaults my own as if to make up for all of the time she's missed with the man she actually loves."
    "Or is pretending to love, based on how passionately she's currently gulping down my saliva."
    "The aggression behind just this single kiss is terrifying and, I know it sounds strange, but it feels like she's essentially trying to suffocate me."
    "I instinctively reach for one of her breasts and attempt to wrap my hand around it, not being able to cover it all due to the sheer size."
    "She leans into me, keeping her eyes closed to remain lost in whatever fantasy she'll use to justify this when the time comes to do so."
    "In between her gasps, I feel the lustful hesitance to reach downward and put an end to her loneliness right here and now."
    "I think about helping her, but not for long."
    "If I forget about breathing for even a second, she is sure to end me."

    h "Mmm...ngh...chu...mf...mlem...ngh...hah...ahm..."
    h "Mmm...mmm~ MMM!"
    h "Hm...mm...nnh..."
    h "..."
    h "..."
    h "Mmnch...mmm!"
    h "..."
    h "..."
    h "Mmh..."
    h "..."
    h "..."
    h "..."
    h "..."

    play sound "static.mp3"
    scene harukabar31
    with flash
    stop sound
    stop music

    h "Oh my god."
    h "Oh my god..."
    h "Oh god oh god oh god..."
    h "I-"
    h "I have to go."
    h "I’m so sorry."

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    "Haruka pushes me away and nearly falls out of the chair as she tries to climb out."
    "She’s still too drunk to run, so she awkwardly stumbles away, grabbing on to everything she can in a desperate attempt to reach the stairs."
    "I don’t call out to her."
    "I get too caught up in watching her struggle."

    $ renpy.end_replay()
    $ haruka_love += 1
    $ harukadate1 = True

    "{i}Haruka’s affection increased by {s}1{/s} more than she wants it to.{/i}"
    "........."
    "......"
    "..."

    if day > 5:
        jump endofsat
    else:
        jump endofweekday

label harukadate5:
    "I wonder if Haruka is doing anything tonight?"
    "Now that I think about it, the two of us haven’t really hung out since that night at the bar."
    "Which...definitely makes sense, given the circumstances."
    "Whether or not the alcohol had any influence over Haruka’s decision to shove her tongue down my throat doesn’t change the fact that it happened."
    "And knowing that most people have a much stronger moral compass than I do, I imagine she’s pretty confused about that right now."
    "I would be too, in her position."
    "But that doesn’t change the fact that I want to see her."

    play sound "phonebeep.wav"

    "And so I tap on her name in my phone and wait for her to answer."
    "..."
    "..."
    "..."

    play sound "phonebeep.wav"

    h "Um..."
    h "Hello?..."
    s "Hey, it’s me. "
    h "Yeah, hey. Uhh...what's up? Is..."
    h "Is everything okay with Rin?"
    s "Rin? Yeah."
    s "Why do you ask?"
    h "I...don’t know..."
    h "I just figured that since you were calling, it probably had something to do with her."
    s "So...does this mean I can’t call you to hang out anymore? You're pulling the plug after one time?"
    h "..."

    "An awkward silence separates the two of us more than even the phone does. I can’t tell exactly what she’s thinking, but I know it's nothing good."

    h "I mean...you {i}can.{/i} It’s just..."
    h "It's probably not a good idea."
    s "And why is that?"
    h "It’s..kind of hard to explain..."
    s "Then it would probably be better to do it in person. "
    h "I guess..."
    s "Did you want to come over?"
    h "Huh? To your place? Is that really okay?"
    s "Well, my [niece] will probably come home soon. But as long as I tell her, it’s-"
    h "Just-"
    h "Just...come over here."
    h "Do you need me to pick you up?"
    s "Nah. I remember where it is. "
    s "I’ll be there soon."
    h "...Okay."
    h "I’ll see you then."

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve2

    "Now, I know what you’re probably thinking."

    if bonus == True:
        "Should I really be taking advantage of a lonely woman who is clearly missing her husband right now?"
        "And the answer is probably no."
    else:
        "How {i}do{/i} magnets work?"

    stop music

    if bonus == True:
        "But Haruka’s husband is likely never coming back. "
        "And {i}I’m{/i} here right now."
        "She deserves someone that can make her feel whole again."
    else:
        "No one knows."

    "........."
    "......"
    "..."

    scene harukadatetwo1
    with dissolve2
    play sound "dooropen.mp3"

    h "Hey. Thanks for dropping by."
    s "Don’t mention it. I wanted to see you anyway."

    play music "lastdailysong.mp3"
    scene harukadatetwo2
    with dissolve

    h "Yeah...That’s kind of what I wanted to talk about."
    h "You see, I haven’t really been...entirely honest with you."
    h "And the other night...when I got drunk...I just sort of acted on impulse and-"
    s "And took what you wanted without thinking about it...right?"

    scene harukadatetwo3
    with dissolve

    h "Ngh..."
    h "I..."
    h "Yes..."
    h "I took what I wanted."
    h "But I really shouldn’t have..."
    h "It was a stupid decision and I should have had the willpower to prevent it, drunk or not."
    s "Well, what's the look for? You're not angry at {i}me,{/i} are you?"

    scene harukadatetwo4
    with dissolve

    h "What? No, it’s just..."
    h "Rin told you, didn’t she? About my...situation."
    s "Your {i}situation?{/i}"

    "Of course I know what she’s talking about. But simply coming out and doing all of the work {i}for{/i} Haruka isn’t going to do anything for her."
    "She’s the one who got herself into this mess. And sure, I didn’t do anything to prevent it, but why would I?"
    "Because it’s wrong?"
    "A lot of things I do are wrong."
    "If anything, this seems pretty tame by those standards."

    h "You...really don’t know?"
    s "I never said that. I just want to hear it from you instead of one of my students."
    s "We're both adults. We should be acting like it- not dancing around our feelings because we're afraid of them."

    scene harukadatetwo5
    with dissolve

    h "Yeah...Yeah, that’s fair. I guess I at least owe you that much."
    s "You don’t owe me anything."
    h "No, I do. I was leading you on."
    s "..."

    scene harukadatetwo6
    with dissolve

    h "I’m..."
    h "I'm married..."
    h "And I...have no idea why I've been hiding that from you."

    "Liar."

    h "It’s not your fault...and I hold absolutely nothing against you, but that doesn’t change the fact that I need to stop things now before they go any further."
    h "What happened at the bar was nothing more than an...outburst fueled by alcohol and loneliness."

    if sarainterest == True:
        h "Besides, you already told me you’re into Sara and-"
        s "What does Sara have to do with this?"

        scene harukadatetwo7
        with dissolve

        h "Sara has a ton to do with this. She likes you {i}way{/i} more than me...and it would be wrong on so many levels for me to keep acting on my feelings without thinking about hers."
        s "And what are {i}your{/i} feelings, Haruka?"
        h "Stupid...that's what."
        h "My feelings are stupid and I’m stupid for having them."

        "I can’t find it in myself to respond to her right now."
        "Instead, I watch as her gaze gets trapped within the same walls she likely imagined raising a family inside of."
        "There is no escape. Not now. Not ever."

    else:
        h "Besides...there's still the whole thing with Sara and-"
        s "What does Sara have to do with this?"

        scene harukadatetwo7
        with dissolve

        h "More than you realize."
        h "Do you have any idea how much she likes you?..."
        s "Sara and I barely even know each other. Whatever she thinks she's feeling is fake."
        s "She’s nothing more than a student’s mother to me. And I already told you I’m not interested in her."

        scene harukadatetwo6
        with dissolve

        h "But if you’re not interested in her, then..."
        s "..."
        h "..."

        "A long pause, as if she’s waiting for me to fill in the blanks."
        "But I don’t. I wait for her to fill them in herself."

        h "Are you interested in {i}me?...{/i}"
        s "..."

        scene harukadatetwo7
        with dissolve

        h "I don’t...understand why you would be when someone much more compatible and...unmarried is already throwing herself at you."
        h "I’m just..."

    h "I’m just...really lonely."

    scene harukadatetwo8
    with dissolve

    h "And I’m sure that sounds like a stupid complaint for someone our age, but...I really {i}am{/i} lonely..."
    h "Do you have any idea what it’s like having the person you’ve dedicated yourself to just...disappear one day?"
    h "To have your entire life stripped away from you without so much as a warning?"

    scene harukadatetwo9
    with dissolve

    h "I don’t even know where he is?! Or what he’s doing! Or-"

    scene harukadatetwo10
    with dissolve

    h "Or..."
    h "Or if he’s even still alive..."
    h "And like...I {i}do{/i} love him...Really...I love him so much..."
    h "But I...I can't control my thoughts...I want to, but I can't."
    h "They just keep going and going and going and going and-"

    "Bullshit. "
    "That’s not love."
    "When you’re in love, you don’t stare into someone else’s eyes after a night of drinking and drag them into the issues you’re afraid of facing on your own."
    "You don’t bite down on their lip or lean into them as they massage your chest."
    "You stay away from all of that."
    "Haruka doesn't love her husband at all."
    "If she did, I wouldn't be here."

    s "I get it."

    scene harukadatetwo11
    with dissolve

    h "You do?..."

    if bonus == True:
        s "Of course I do. I can’t even imagine going as long as you have without sex."
    else:
        s "Of course I do. I can’t imagine how hard it is going that without a big ole hug."
        h "............."

    scene harukadatetwo12
    with dissolve

    h "I mean it's...it's more than just that..."
    h "Sex is only...part of it..."
    h "I...miss feeling wanted. Or loved. Or pretty or desirable or any other good thing that I felt before I was all alone."

    scene harukadatetwo13
    with dissolve

    h "The sex thing...definitely makes it worse, though. I won't lie."
    h "I was never really interested in that kind of stuff when I was younger but, like...as soon as I started, it became really hard to hold back whenever I-"

    if bonus == False:
        "Wow. Haruka must really like hugs."

    scene harukadatetwo14
    with dissolve

    if bonus == True:
        h "Ugh...What the fuck am I even saying to you right now?! Talking about this is just going to make it even worse!"
    else:
        h "Ugh...What the Hell am I even saying to you? I already lead you on and now I’m talking about how much I miss hugs..."

    s "Talk as much as you want, Haruka. I don’t mind things like this."
    s "I do want you to know that there are plenty of people who still think you’re pretty or desirable or whatever it is you want to hear, though."

    scene harukadatetwo15
    with dissolve

    h "Knowing that just makes it harder..."
    s "Why? Didn’t you say you just wanted to feel that way again?"

    if bonus == True:
        h "Yeah, but not when feeling that way makes me think I’m some...unfaithful {i}slut{/i} who misses sex so much that she cheats on her husband while he's away."
        s "How long has he been away, if you don’t mind me asking?"
        h "..."
        s "..."
    else:
        h "Because...I'm afraid I don't remember {i}how{/i} to hug."
        s "Gasp."
        h "Yeah, I know."
        s "How long has it been since your last hug?"

    h "Three years, I think."
    s "Three years? How are you even alive?"

    scene harukadatetwo16
    with dissolve

    h "Is that supposed to make me feel better?!"
    s "I'm sorry. That's just...longer than I thought."

    scene harukadatetwo17
    with dissolve

    h "I know..."
    h "Honestly, I probably {i}would{/i} be dead if it wasn't for the local porn shop."

    scene harukadatetwo16
    with dissolve

    h "Ugh! And now I’m doing it again!"
    h "You know, this is also kind of your fault for being so attractive and...making me think things!"

    if bonus == True:
        s "Am I...supposed to apologize for that?"

        scene harukadatetwo17
        with dissolve

        h "No, I..."
        h "My mind has just been wandering all over the place lately."
        h "And more often than not, I feel like it winds up stopping somewhere near you."

        "Ahh, there it is. The admission I’ve been waiting for since this conversation started."
    else:
        "Ahh, there it is. The blunt admission I’ve been waiting for since this conversation started moving toward the hug-zone."

    "From this point on, there are two options."
    "Either I be a good guy and don’t take advantage of Haruka in this moment of desperation- dooming her to wait for a man who may never even return."
    "Or-"

    if bonus == True:
        "I seduce her."
        "And remind her of all the wonderful things she’s been missing out on inside of these walls."
    else:
        "I hug her...even though she's {i}married.{/i}"

    h "..."

    "What should I do?"

    menu:
        "Be a gentleman":
            s "..."
            s "I..."
            s "I should probably leave before this turns into something you’ll regret."

            scene harukadatetwo18
            with dissolve

            "A sigh of relief spreads across Haruka’s face."
            "Her shoulders drop and cause her breasts to bounce which, for a brief moment, remind me of all the joys I will now be missing out on."
            "But the fact is-"
            "I have no place in this woman’s life right now."
            "Not while she is this conflicted."
            "If I am going to take her, I need her mind to be on me and me only."

            if bonus == True:
                "Besides, I have plenty of other girls who are throwing themselves at me on a daily basis."
                "So what if this one is sex-starved and ready to go right now?"
                "It's not like going three years without sex might make her go all out and-"

            s "Okay, yeah. I really do need to get going. My mind is heading in a dangerous direction right now."

            scene harukadatetwo19
            with dissolve

            h "Yeah...I know how that feels."
            h "I’m...sorry to have probably put you through that."
            h "I didn’t really expect this conversation to...devolve so quickly."
            h "I've just been having an admittedly hard time around you lately. "
            h "But I’ll try harder so things like what happened at the bar will never happen again."
            s "You do whatever you need to. I’ll be around if you need me."

            scene harukadatetwo20
            with dissolve

            h "Yeah..."
            h "Thanks."
            h "I’ll...see you some other time, then."
            s "Yeah..."
            s "See you soon, Haruka."

            scene black
            with dissolve2
            play sound "dooropen.mp3"

            "I leave Haruka’s house and walk back down the same street I traversed just an hour or so ago."
            "It sucks that I came this far for essentially nothing."
            "But at the same time-"
            "It's nice being able to end a day without hurting anyone."

            $ renpy.end_replay()
            $ harukadate5 = True
            $ haruka_love += 1

            "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
            "........."
            "......"
            "..."

            if day > 5:
                jump endofsat
            else:
                jump endofweekday

        "Fuck another man’s wife" if bonus == True:
            jump cheatwithharukax
        "Hug another man’s wife" if bonus == False:
            s "Will your husband get mad if we hug?"
            h "I don't know. Will you get mad if I am bad at it?"
            s "How can you be bad at hugging?"
            h "You are about to find out."
            s "Uh-oh."

            scene black
            with dissolve

            h "Take that!"
            s "Why did you just hit me?"
            h "I am trying to hug."
            s "Oh no."

            "Haruka was right. She is very bad at hugging."
            "I'll probably keep trying to teach her, though. Because that is my job. To teach."

            h "Be vanquished!"
            s "Stop it."

            $ renpy.end_replay()
            $ haruka_love += 1
            $ harukadate5 = True
            $ harukasex = True
            stop music fadeout 5.0

            "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
            "........."
            "......"
            "..."

            if day > 5:
                jump endofsat
            else:
                jump endofweekday

label harukadogrep:
        play sound "phonebeep.wav"

        "I press on Haruka's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        h "Hey...What are you doing right now?"
        s "Not much. You?"
        h "Not much..."
        s "Cool, cool."
        h "Uh-huh..."
        s "..."
        h "Um..."
        h "Do you want to come over?"

        scene black
        with dissolve

        "........."
        "......"
        "..."

        if bonus == True:
            jump harukadogrepx
        else:
            $ haruka_lust += 1
            stop music fadeout 4.0

            "{i}Haruka's lust has increased to [haruka_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label harukafirstlust:
    scene cafe_day
    with dissolve
    play music "cafe.mp3"

    "I show up at the cafe to check in on Haruka and see what she’s up to."
    "Given that this is her business, I’d imagine the answer to that would be “working,” but the cafe is unusually dead this morning for some reason."
    "In fact, I don’t even see Rin behind the counter, which is borderline absurd to me given that she’s here virtually every weekend ever."
    "I wonder if something is going on?"

    h "Hey! Come hang out with me, loser."
    s "..."

    scene harukafirstlust1
    with dissolve

    s "Loser? Really?"
    s "How old are you?"
    h "Old enough!"

    scene harukafirstlust2
    with dissolve

    h "What are you up to today?"
    s "Uhh, just normal cafe stuff I guess. Where is everybody?"
    h "Beats me. Probably sleeping in for the holiday or something."
    s "Holiday?"
    h "Yeah. It’s Kumon-mi Day. "
    s "What the fuck is Kumon-mi Day?"

    scene harukafirstlust3
    with dissolve

    h "Beats me. I can tell you it’s definitely not just some convenient plot device inserted into this scene to justify creating an opportunity where the two of us are alone, though."
    s "Of course it’s not. That would just be lazy writing."

    scene harukafirstlust1
    with dissolve

    h "Heheh~ You got that right."
    s "If it’s a holiday, why even bother opening, though? You don’t even have Rin working today."

    scene harukafirstlust4
    with dissolve

    h "Really, dude? We get to hang out alone in this nice, air-conditioned cafe and you’re going to complain about my part-timer not being here?"
    s "I’m not complaining. I just feel like this completely disrupts the chain of events my life has begun to follow."
    s "I don’t like change."
    h "Yeah...I guess I can agree with that."

    scene harukafirstlust2
    with dissolve

    h "Rin’s fine, though. I sent her home early."
    s "It must suck coming all the way here just to get sent home early."
    h "Naaaah. She seemed tired anyway so I’m sure she’s fine with it."

    scene harukafirstlust1
    with dissolve

    h "Plus, if a million people just decide to show up out of nowhere, I could always force you to help me instead."
    s "Yeah, I’m not sure how that would work out. I don’t even remember the names of your sizes."

    scene harukafirstlust2
    with dissolve

    h "Ehh, I’m sure you won’t have to worry about that. I honestly might just close up anyway."
    h "At least until the afternoon or night or something when things start to pick up again. "
    h "A day off might not hurt every once in a while and I guess a holiday is as good an excuse as any. "

    scene harukafirstlust1
    with dissolve

    h "Plus, then I’d get to make you hang out with me. "
    s "You are aware you can’t {i}make{/i} me do anything, right?"

    scene harukafirstlust5
    with dissolve

    h "Oh I can {i}make{/i} you do plenty of things, Sensei~"
    s "..."
    s "Are you seducing me right now?"
    h "What? Seducing you? At my own workplace? How dare you accuse me of something so outrageous."
    s "So you’re not, then?"

    scene harukafirstlust6
    with dissolve

    h "Well..."

    "Haruka pauses and directs her attention to the barren streets outside of the cafe."
    "Nothing or no one can be seen passing by. No cars, no pedestrians, not even an occasional leaf or plastic cup-lid or anything."

    if bonus == True:
        jump harukabathroomx
    else:
        scene black
        with dissolve

        h "Nah. I'm just fuckin' around."
        s "Hahaha. You're so crazy, Haruka."

        "The two of us proceed to celebrate Kumon-mi Day by filling our hands with as many coffee beans as we can and then throwing them into the air and trying to run under them."
        "The tradition dates back to the origins of the city and fills my eyes with tears as I attempt to recollect all of my past lives and all of my past celebrations."
        "Then Haruka interrupts me and is all like {i}When do you wanna put our shoes back on?{/i} and I say {i}never{/i} and then leave."
        "Also, we hug."

        $ renpy.end_replay()
        $ haruka_lust += 1
        $ haruka_love += 3
        $ harukafirstlust = True

        "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
        "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon

label harukacafedogrep:
        scene black
        with dissolve
        play music "cafe.mp3" fadein 3.0

        "I head to the cafe to see what Haruka is up to and find her at a table near the window filing through some paperwork."

        h "Oh, hey! What are you up-"

        if bonus == True:
            s "Let's have sex."
        else:
            s "Let's hug."

        h "...What?"
        h "Right now?"
        h "But it's the middle of breakfast."
        s "I don't care."
        h "Um...Uhh..."

        "Haruka looks over to the counter to find Rin sifting through a few syrup bottles and not paying much attention to the store."

        h "...Okay. But we need to be quick."

        "........."
        "......"
        "..."

        if bonus == True:
            jump harukacafedogrepx
        else:
            $ haruka_lust += 1
            stop music fadeout 4.0

            "{i}Haruka's lust has increased to [haruka_lust]!{/i}"
            "........."
            "......"
            "..."

            jump saturdayafternoon

label harukadate10:
    scene harukarinreview1
    with dissolve
    play music "cafe.mp3"

    "I show up at the cafe to find Haruka and Rin sitting at a table near the door. "
    "The girl manning the counter is someone I haven’t seen before so, not wanting to involve myself with anyone new, I decide to intrude on the conversation between these two."
    "Judging by the clipboard, however, it appears that I may have suddenly walked into a relatively important discussion."
    "Whoops."

    r "Hey! Is it Sensei-time already?"
    h "Yes, it appears it is Sensei-time."
    s "Sensei-time isn’t a thing. Please don’t say that anymore."

    scene harukarinreview2
    with dissolve

    r "{i}Sensei-time{/i}."
    s "..."
    s "Anyway, what are you two doing over here? Shouldn’t you be working right now?"

    scene harukarinreview3
    with dissolve

    h "I was actually just doing Rin’s performance review for the quarter."
    r "Yup-yup. And, news-flash, turns out I’m pretty awesome. Who would have thought?"
    s "Not me considering you have only given me what I’ve actually ordered maybe once or twice since I started coming here."
    r "That’s just cause you’re special. Tell him, Haruka."
    h "This is news to me, actually. I’m going to dock a few points from your review so I don’t have to give you a raise."
    h "Please do better in the future for the sake of the company."
    r "..."
    h "..."

    scene harukarinreview4
    with dissolve

    r "Are you bein’ for real right now?"
    h "Of course not. You can keep making whatever you want for him as long as he continues to keep doing nothing about it."
    s "Wow, the service here has really gone downhill lately."

    scene harukarinreview5
    with dissolve

    h "Like Rin said, you’re special. "
    h "Plus, we’re friends now."
    h "I don’t have to be nice to you anymore now that I know you’re here for the girls instead of the coffee."
    r "Hey wait a second, how come you two are acting super close all of a sudden?"
    r "When did this happen?"
    s "In my defense, I am not acting any different than normal. This is all Haruka."

    scene harukarinreview6
    with dissolve

    h "There’s no need to be jealous, Rin. I’m sure you still see him more often than I do."
    r "Well...probably."
    r "And I’m not jealous. I’m just surprised. "
    r "I could have sworn you were a loner, Haruka. I didn’t even know you talked to anybody other than all of us at the cafe."

    scene harukarinreview7
    with dissolve

    h "Oh. Well thank you for reminding me of how incredibly lonely I am, Rin. I appreciate that."
    r "No sweat! This is just our thing, isn’t it?"

    if bonus == True:
        r "You tease me about not being able to reach the syrup bottles on the top shelf and I tease you about going years without getting laid."
    else:
        r "You tease me about not being able to reach the syrup bottles on the top shelf and I tease you about your stupid pink hair."

    if harukasex == True:
        scene harukarinreview8
        with dissolve

        h "..."
        s "..."

        "Don’t do it, Haruka. "
        "Don’t say anything."

        r "Hm? Isn’t this the part where you come up with some sarcastic remark or something?"
        r "We’re supposed to go back and forth right about now and-"
        r "..."

        scene harukarinreview9
        with dissolve

        r "Oh my God, you fucked my boss!"
        r "Dude!"
        h "Hahaha..."
        s "Don’t you think I would have told you if something like that happened, Rin?"

        if rinbetrayed == True:
            scene harukarinreview10
            with dissolve

            r "No, actually. You kind of have a track record of going behind my back with people I know now, so yeah. "
            s "That’s..."

            "I decide against prying anymore into that side of things at the risk of further-destroying my relationship with Rin."

        else:
            scene harukarinreview11
            with dissolve

            r "Well, yeah. But Haruka really only gets quiet like this when she’s trying to hide something."
            r "Plus, I already told you she thought you were cute and stuff a while back, so it’s not {i}impossible{/i} for something like that to happen."

        scene harukarinreview12
        with dissolve

        r "I’m kind of surprised by Haruka, though. "
        r "I know you haven’t seen your husband in a while but I didn’t think you’d crack under the pressure that-"
        h "I didn’t crack. "
        h "Nothing is going on between your teacher and me. "
        h "I was just messing with you since I know you two are close."

        scene harukarinreview13
        with dissolve

        r "Well..."
        r "That’s kind of a relief. But now I also feel really bad about accusing you of something like that."
        r "You should probably get a little better at hiding things if you want to-"
        h "Get back to work, Rin."
        r "I was just leaving."
        r "Sorry."

        scene harukarinreview14
        with dissolve

        "Rin quickly ducks away from the table, taking her notebook and coffee with her before disappearing into the back room."

    else:
        scene harukarinreview15
        with dissolve

        if bonus == True:
            h "Hey. You leave my sex-life out of this. "
            h "Do you have any idea how satisfying it will actually be when he comes back from the war?"
            r "Nope. I’m an innocent virgin barista so I have no idea how satisfying it is in the first place."
        else:
            h "My hair is not stupid!"

        scene harukarinreview16
        with dissolve

        h "Oh my God...Why am I even talking to you about this?"
        r "Sensei, I’m sorry my boss doesn’t feel the same way about you as you feel about her."

        if rinbetrayed == True:
            r "Thankfully, the girl I’ve been after for literally years is, so you’ll have to settle for fucking a cute [teenager] instead of a voluptuous older woman."
            r "Sorry for your loss."
            s "Rin..."

        else:
            r "There are plenty of other fish in the sea, though. I’m sure you’ll catch one eventually."

            if bonus == True:
                r "Heck, you might even have a shot with me if you keep trying. It only makes sense to fall for someone you keep spending time with, right?"
                r "Sure there’s the added issue of me still thinking penises are kind of scary, but you know how it is."
                s "I thought I did until that last part. Now I’m just back to being confused."
            else:
                s "But Papa never taught me how to fish."

            r "It is what it is, homie."

        scene harukarinreview17
        with dissolve

        h "And on that note, our review is now complete."
        h "Get back to work, Rin."
        r "Aye aye, Captain Haruka! "

        if bonus == True:
            r "Have fun not having sex with my teacher!"
        else:
            r "Have fun not hugging my teacher!"

        h "And you have fun cleaning the bathrooms. Leave."
        r "Roger that! Love you, bye!"

        scene harukarinreview18
        with dissolve

        "Rin quickly ducks away from the table, taking her notebook and coffee with her before disappearing into the back room."

    s "I have to commend you for being able to put up with her for this long every weekend."
    h "You have to put up with her too, don’t you? Isn’t she in your class?"
    s "She is, but she’s a little different in[school] than she is here."
    s "She seems happier in the cafe. Kind of like she admires you or something like that."

    scene harukarinreview19
    with dissolve

    h "Me? Why would she admire me?"
    h "All I do is work and talk about what shows I’ve been watching on Netflix lately."

    if harukalust10 == True:
        h "I’m kind of insanely boring if you take out the part about me dressing up as a cat and riding you on occasion."
        s "But that’s my favorite part about you."

        scene harukarinreview20
        with dissolve

        h "I still kind of can’t believe I was drunk enough to do something like that."
        h "Maki really manages to bring the worst out of me sometimes."
        s "Was it Maki’s idea to invite me over?"
        h "Well, no. But-"
        s "Then don’t blame her for what happened. "
        s "You made a decision and you followed through with it. She just happened to be there for it."
        h "..."

        scene harukarinreview21
        with dissolve

        h "You’re right. I need to accept responsibility for my actions."
        h "I’ve just gone so long without being...involved in someone new that I kind of forget how it works at times."
        h "But, in my defense-"
        h "Maki is fucking hot."
        s "I can’t believe you made me wait an extra 24 hours to hook up with you two after the Halloween party at the bar."

        scene harukarinreview22
        with dissolve

        h "And I can’t believe you went upstairs with Sara without inviting the two of us."
        s "Sara didn’t want you to come."
        h "I can’t believe you didn’t keep pushing for it to happen. Jerk. "
        s "Didn’t you pass out within the next 30 minutes anyway? "
        h "Yes. Out of disappointment."
        s "Poor Maki. "
        h "More like poor Haruka."

        if saralust10 == True:
            h "Kind of degrading listening to your best friend get fucked by the guy you’re into while you sit downstairs and get drunk."
            s "You heard us?"

            "I guess that makes sense given how old the building Sara lives in is."
            "That’s kind of concerning in the event of anyone else ever being downstairs while...things are happening, though."

            h "Of course I heard you. That girl is even louder than I am."
            s "Mmm...I don’t think that’s true."

            scene harukarinreview23
            with dissolve

            h "I’m louder than {i}that{/i}? "
            s "Do you not realize how into it you get, Haruka?"
            h "I had no idea..."
            h "My neighbors...Do you think they, you know, hear us?"
            s "I’d be shocked if they didn’t, to be honest."

            scene harukarinreview24
            with dissolve

            h "Oh God..."
            s "Something wrong?"
            h "A lot is wrong. I don’t want to talk about it here, though."
            h "Apparently I’m a walking megaphone so I don’t want the girls to hear us talking about how loud I am when you fuck me."
            s "Right. "
        else:
            h "Maki might be super hot, but I don't really think she could please me the same you can."
            s "If there is any woman who can do just that, I'm positive it's Maki. Have you seen the arsenal of sex toys at her shop?"

    else:
        s "You’re right. That does sound incredibly lonely."

        scene harukarinreview25
        with dissolve

        h "It’s even lonelier when I eat an entire pint of ice cream and cry myself to sleep afterward."
        h "Such is the life of a woman who lives alone. "
        s "Sara lives alone and I doubt she cries herself to sleep every night."

        if bonus == True:
            h "Yes but Sara also keeps a dildo on the shelf next to her bed so she is clearly a force to be reckoned with."
        else:
            h "Yes but Sara also keeps an entire wheel of cheese on the shelf next to her bed so she is clearly a force to be reckoned with."

        s "Yeah, good point."

    s "But anyway, I {i}do{/i} think Rin sees you as some sort of role model. At least that’s how I’d see you in her position."
    s "People like looking up to more successful people in the same position as them."
    s "And even if you’re lonely, you’re still doing something with your life."

    scene harukarinreview26
    with dissolve

    h "Did you really come here just to lecture me?"
    s "No. I came here to see you. So this is supposed to be the part where you start feeling a little less lonely."

    scene harukarinreview27
    with dissolve

    if bonus == True:
        h "You’re here to see {i}me{/i} despite having a girl like, half my age and four times prettier than me two steps away from just...biting the bullet and admitting her love for you?"
        s "Rin doesn’t {i}love{/i} me, Haruka."

        scene harukarinreview28
        with dissolve

        if rinbetrayed == True:
            h "Oh please. She looks at you differently than pretty much every other guy that’s ever come in here."
            h "She swings both ways, doesn’t she? I’m sure she’d be more than willing to embark on a journey of sexual exploration with you under the right circumstances."
            s "It would be easier for me to believe that if I didn’t finger the girl she’s in love with."

            scene harukarinreview29
            with dissolve

            h "You fingered the cute blonde girl who comes in here all the time?!"
            s "..."
            s "No. You never heard that."
            h "No! I did totally just hear that!"
            h "How did that even happen?!"

        else:
            h "Oh, please. Ever since the blonde girl rejected her, she’s only ever really talked about you."
            s "Probably just a coincidence. I doubt Rin sees me as anything more than like, an older brother or father figure right now."

            scene harukarinreview30
            with dissolve

            h "Doesn’t mean she doesn’t want to try experimenting a little bit, though~"
            h "She’s a [teenage]girl. She’s curious. I was the same when I was her age."
            h "You really think she’s never entertained the thought of fooling around with the same guy who hangs out with her in her room all the time?"
            h "Come on, man. You know better than that."
            s "You’ve put a lot of thought into this, huh?"
            h "When you’ve got employees as cute as her, you sometimes can’t help but think about things like that."

        s "..."
        s "I’m starting to think you might be just as into [teenage]girls as me, Haruka."

        scene harukarinreview31
        with dissolve

        h "Me? Nooooo."
        h "I just staff my cafe with inexperienced, cute girls because they make the best employees."
        h "Of course I’m into them. Everyone loves cute girls, Sensei. Just because I’m a girl doesn’t mean I’m an exception to that."
        s "I mean, I’m all about this. But you should probably be careful acting on anything at the risk of getting sued one day."

        scene harukarinreview32
        with dissolve

        h "Oh, come on. I’m a degenerate but I’m not a bad person."

        if harukasex == True:
            "She says, despite actively cheating on her husband."

        h "It’s one thing for me to be attracted to girls like Rin or Molly-"
        s "Molly, too?"

        scene harukarinreview33
        with dissolve

        h "Or Rin’s friend Futaba."
        h "Or Molly’s friend...Tsuneyo, I think?"

        "Oh my God. She’s just as bad as me."

        h "But just {i}wanting{/i} to mess around with all of them doesn’t mean I actually {i}would{/i}, you know?"
        h "Unless they offered. Because in that case, I absolutely would."
        s "I’m glad we became friends, Haruka."
        s "I feel like our relationship has moved forward several steps today."
    else:
        h "You are right. I am being immature and not properly valuing our friendship."
        h "Will you ever forgive me."
        s "I forgive you right now. I understand that it is only human to act off of your emotions and that every one of us can be a little irrational from time to time."

    scene harukarinreview34
    with dissolve

    h "Then come hang out with me again soon. As friends."
    h "We’ll sit on my couch and I can show you some of the stuff I watch when I’m thinking about how lonely I am. "
    s "That sounds absolutely delightful."

    "Not."

    scene harukarinreview35
    with dissolve

    h "Sweet. Maybe I’ll invite Rin, too? Who knows?"
    s "You’re going to invite a [teenage]girl to your house to watch movies with you and another older guy?"
    s "Totally not suspicious at all."
    h "And hanging out in her dorm isn’t?"
    s "Touché."
    s "Oh well. Do whatever you want. "

    if bonus == True:
        h "If I do whatever I want, I’ll end up in jail. "
        h "I will exercise the same amount of restraint I always do, and the two of us will forget this conversation ever happened."
    else:
        h "Even if it means renting out a bounce house?"

    h "Deal?"
    s "Deal."

    if bonus == True:
        "No deal."
        "I can’t just forget finding out that Haruka is lusting after her entire cafe staff and...everyone her cafe staff knows and..."
        "Probably just everyone in general."
        "But I guess after going years without having sex, you start getting desperate."
        "To think Haruka would be permanently psychologically damaged by something like this, though..."
        "That’s just so sad."

    s "Well, I guess I’ll get out of your hair then."
    h "Sounds good. I need to start actually working again anyway."
    h "Call me soon, though. Got it?"
    s "Yup. "
    s "See you later, Haruka."
    h "Talk to you soon!"

    scene black
    with dissolve2

    "I exit the cafe without buying anything. "

    if bonus == True:
        "Not because I wasn’t thirsty, but because I’d inadvertently gotten an erection after finding out about Haruka’s hidden infatuation with [teenage]girls and didn’t want to scare any of the part-timers."
        "Eventually, the erection fades and I am free to get on with my day the way I normally do."
        "I’ll have to call Haruka some night in the near future and see if I can do anything else to quell that undying loneliness of hers."
    else:
        "I sure can be forgetful sometimes."

    $ renpy.end_replay()
    $ haruka_love += 1
    $ harukadate10 = True
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label harukadate15:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "We talked recently about spending some time together at her place and watching movies or something along those lines, so I figure now is as good a time as any to make that dream a reality."
    "And when I say “dream,” I mean it very loosely as my dreams are much more exciting."
    "When I actually have them, that is."
    "Lately, I haven’t been having-"

    play sound "phonebeep.wav"

    h "Hey! What’s up?"
    s "Oh, hey. Nothing really."
    s "Are you free tonight?"
    h "As a matter of fact, I am. Sara just bailed on me and Molly is “managing” the cafe tonight."
    s "And you’re sure the cafe is going to be okay?"
    h "Nope! But I really don’t want to think about work right now."
    h "Come over and let’s do stuff. "
    h "I’d offer to pick you up but I’m feeling really lazy and don’t want to leave right now."
    s "Wow. Thank you for the kind offer, but I will walk."
    h "I know you will!"
    h "See you soon!"

    play sound "phonebeep.wav"

    "Haruka hangs up the phone and, before I know it, I’m walking to her place."

    scene nightsky
    with fade
    play music "love.mp3" fadein 10.0

    "The walk to Haruka’s is always kind of annoying."
    "I should probably invest in a car sooner or later, but..."
    "I don’t know."
    "I’ve gotten kind of familiar with these streets over my time here."
    "I’m memorizing them quicker than I’ve memorized anything, I think."
    "Besides things that are meant to be memorized like phone numbers or addresses. "
    "You know what I’m talking about."
    "The process of remembering things that you are only {i}kind of{/i} supposed to remember."
    "Like streets or the names of distant relatives."
    "Like how many beeps the microwave makes after it finishes blasting radiation into a frozen TV dinner."
    "These are things we memorize subconsciously as opposed to consciously."
    "But the more time I spend here, the more I move from the former form of memorization to the latter."
    "I want to memorize these streets."
    "I feel I’ll be spending a concerning amount of time traversing them if nothing goes horribly wrong in the near future."

    play sound "doorbell.mp3"

    "I arrive at Haruka’s place after what seems like half an hour and ring the bell."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    h "Hey! How was your walk?"
    s "Unnecessary."

    scene harukaalone1
    with dissolve

    h "Well, on the bright side, you get to see me now. So that’s at least slightly rewarding, right?"
    s "Slightly, yeah."
    h "Awesome. I’m almost worth a thirty minute walk. "
    h "I’ve gotta say this is personally better than I ever thought I’d do, sooooo hooray for Haruka!"
    s "I’ve only been here for ten seconds and the self-esteem issues are already coming out. "
    s "Tonight is going to be a blast."

    scene harukaalone2
    with dissolve

    h "Hey, you knew what you were signing up for and you still came either way."
    h "I even gave you the chance to say “No, I don’t want to walk all the way over there,” and yet, here you are. "

    scene harukaalone3
    with dissolve

    h "So, since you’re here, I guess it’s finally time we find something to do, huh?"
    s "What would the gameplan have been if I never came?"
    h "I told you at the cafe, didn’t I? Probably ice cream and crying."
    s "You can still eat ice cream if you want."

    scene harukaalone1
    with dissolve

    h "I’d have to run out and buy some."
    h "Want me to cry instead?"
    s "Not really. I never know what to do around girls when they cry."

    scene harukaalone4
    with dissolve

    h "Uhh, how often are you around crying girls?"
    s "Often enough for this to be an actual thing I have learned about myself."
    h "Fair enough. What you do on your own time isn’t really my business."

    scene harukaalone5
    with dissolve

    h "Know what {i}is{/i} my business, though?"
    s "What, Haruka?"
    h "Koi Cafe."
    s "..."
    h "Get it?"
    h "Cause like-"
    h "..."
    h "Yeah."
    s "..."
    s "Okay, well it’s been fun. I’ll see you later."

    scene harukaalone6
    with dissolve

    h "Oh, come on! That was good!"
    h "Here, come sit down. It’s no fun just standing near the door and listening to me tell jokes."

    "Well, she’s right about that, at the very least."

    scene black
    with dissolve

    "Haruka walks over to her sofa, grabbing the TV remote off the table in front of her and turning up the volume on whatever program she was watching before I got here."
    "I walk back to the entryway and kick my shoes off after I realize I forgot to remove them before taking my place next to her on the couch."

    scene harukaalone7
    with dissolve

    h "So, welcome to a day in the life of me."
    h "When I’m not making cappuccinos or bossing around a bunch of mini versions of myself, I’m doing this."
    h "Sitting on a couch and contemplating what sort of person I am while watching Gordon Ramsay make children feel bad about themselves on Master Chef Junior."
    s "You lead an interesting life, Haruka."
    h "Don’t tease me."
    h "Even before my husband was drafted, it was like this- just with two bodies on the couch instead of one."
    s "So you weren’t happy even when he was around?"

    scene harukaalone8
    with dissolve

    h "I never said that."
    h "When you love someone, you can do things like just sit on a couch with them and watch Gordon Ramsay yell at children and it will feel like the most fun you’ve had in forever."
    h "It isn’t until they’re gone that you realize how depressing it is to be watching TV alone."
    s "This conversation got serious much quicker than I expected it to."

    scene harukaalone9
    with dissolve

    h "Hahaha...yeah. Sorry about that. I’ve just...gotten so used to doing things like this with him that I find myself reliving those days any time I turn on Netflix."
    h "Which sounds kind of shitty to say since he’s still alive-"

    "Maybe."

    h "But...yeah. Let’s talk about something else. Like..."

    scene harukaalone10
    with dissolve

    h "Like, what’s it like being a[school] teacher?!"
    h "That sounds like a lot more fun than what I do."
    s "You’re only saying that because you’re apparently hot for [teenage]girls."
    h "Yup. You got me. "
    h "Now tell me what it’s like."

    "Huh."
    "How I feel about teaching..."

    s "It..."
    h "...?"
    s "It kind of sucks."
    h "..."

    scene harukaalone11
    with dissolve

    h "That...is not the answer I expected."
    h "Why would you say that?"

    if bonus == True:
        h "With how much I’ve heard about you in[school] from Rin, I always kind of thought you liked your job."
        h "You know, the whole touching youths thing."
        s "Just to clarify, which sort of “touching youths” are you referring to right now?"

        scene harukaalone12
        with dissolve

        h "The not-creepy one this time."
        h "Aren’t you interested in making differences in these girls lives or something like that?"
        h "How’d you get into teaching in the first place?"
        s "It just...kind of happened."
        h "So you just kind of happened to go to[school] for years to become a teacher and then just kind of applied for a teaching job?"
        s "No I mean it literally just kind of happened."
        s "You wouldn’t get it."
        h "Try me."
        s "It involves time travel."
    else:
        s "There aren't enough vending machines."

    scene harukaalone13
    with dissolve

    h "Okay, never mind. "
    h "It’s clear you’re not going to be serious, so we can just move on to something else."

    "Oh well."
    "Can’t say I didn’t try."

    scene harukaalone14
    with dissolve

    h "You know, I used to have a crush on my [high_school] teacher when I was around Rin’s age."

    if bonus == True:
        h "Granted, I was too much of a coward to ever tell him that. And it’s not like I would have expected anything to have happened even if I did."
        s "Worried about the age gap thing?"
        h "More like there just...wasn’t anything notable about me."
        h "I was just a normal girl living a normal life and studying just like any other normal person until, one day, I met the guy who I would end up marrying."
        s "And suddenly we’re back at your husband."
    else:
        s "Ew. Stop being so inappropriate all the time. You always share way too much and it makes me uncomfortable."

    scene harukaalone15
    with dissolve

    h "Fuck! Sorry. I didn’t mean to. It just keeps happening."

    if bonus == True:
        s "It’s fine. If it was that big of a deal, you wouldn’t keep inviting me over."
    else:
        s "It’s fine. If it was that big of a deal, I would have just left."

    scene harukaalone16
    with dissolve

    h "Yeah...You’re...probably right about that."
    h "And besides, we’re just friends so..."
    h "It’s not like I love you or anything like that."
    h "You’re just...keeping me company."
    h "That’s all."

    if harukasex == True:
        "Haruka justifies her betrayal of a man who has not yet been confirmed dead in the only rational way she’s able to think up."
        "She pretends the touch of my hands and the length of my cock are only temporary respites given to a woman in grief despite her unmeasurable levels of uncertainty."
        "I can see through her."
        "Anyone could if they’d just open their eyes."
        "She is horrible- just like me."
        "We fit each other well."
        "Physically and non-physically. "
        "She knows it too."
        "It’s one of the many reasons she continues to cry nearly every time we fuck."

    else:
        "That’s right."
        "As it stands, all I am to Haruka is a friend."
        "Could I change that if I truly applied myself?"
        "Probably."
        "But would it be right to do so?"
        "Who knows?"
        "It’s not really my place to say."
        "If she thinks betrayal is the path that will make her feel whole, it’s a path she’s likely to take with or without me."
        "All I can really do for the time being is continue to be near her."
        "To quell the unending loneliness of a woman unloved."

    s "Right. We’re just friends."

    scene harukaalone17
    with dissolve

    h "Exactly! Which is why it’s cool for us to do stuff like hang out on my couch and just...talk or...whatever it is we’re doing now."
    s "Right."
    s "Now, your relationship with {i}Maki{/i} on the other hand..."

    scene harukaalone18
    with dissolve

    if bonus == True:
        h "Ugh. She’s so hot, though!"
    else:
        h "But she is so good at hugging!"

    h "And he already signed off on that so it’s totally okay!"
    h "Besides, it really {i}does{/i} only happen on rare occasions when we’re drunk."

    if harukalust10 == True and bonus == True:
        h "And you know firsthand what kind of wonders she can work with her tongue!"
        s "This is very true. That was most definitely not her first time."
        h "Probably her millionth!"
        s "Okay now that just can’t even be possible."

    h "Maki’s...a different type of animal compared to someone like me."

    if bonus == True:
        h "She’s like this crazy sex goddess and I’m some girl who was too scared to even touch herself until senior year of [high_school]."
    else:
        h "She’s like this crazy hug goddess and I'm just some girl who violently attacks anyone who tries to hug me."
        h "It's probably because I didn't have any hugs for the first ten years of my life."
        s "It is true. You are very bad at hugging."

    h "I get nervous around her and just kind of...follow her lead."
    s "Were you really that late of a bloomer?"

    if harukasex == True:
        scene harukaalone19
        with dissolve

        h "I’ve only ever been with two guys before..."
        h "That includes kissing, too."
        h "Well, not counting girls."

    else:
        scene harukaalone19
        with dissolve

        if bonus == True:
            h "My husband is the only guy I’ve ever been with..."
        else:
            h "My husband is the only guy I’ve ever hugged..."

        h "I’ve never even kissed anyone else."
        h "Well, not counting girls."

    s "If it’s any consolation, the amount of girls you kiss makes no difference to me."
    s "Feel free to shoot for the world record if you want."
    s "I will support you every step of the way."

    scene harukaalone20
    with dissolve

    if bonus == True:
        h "Even when I start coming for all of the girls in your class?"
        s "Start with Rin. I frequently worry that she’ll explode if she doesn’t find an outlet for her pent-up lesbian energy soon."
        h "How about we share her?"
        s "Deal. Sign me up."
    else:
        h "Thank you, Sensei. That is very nice of you."
        s "Rin would also probably support you every step of the way. She loves you, Haruka. You are very important to her."

    scene harukaalone21
    with dissolve

    h "I’m gonna tell her you said that~"
    s "Fine by me."
    s "Also, what is the meaning of this?"
    s "I don’t have Rin’s number yet and I feel like I’m much closer to her than you are."
    h "She works for me, dude. I need her number to send her pictures of the schedule."
    h "Do you want it?"
    s "I hope you mean her number and not a picture of the schedule."
    h "What, so you don’t want to come work for me?"
    s "I can’t say I do."
    s "I’ll accept a phone number, though."
    h "Fine. Here."

    "Haruka begins listing the digits of Rin’s phone number and I carefully type them into my phone."

    $ rinnumber = True

    "{i}Congratulations! You have received Rin’s phone number in an extremely roundabout way!{/i}"
    "{i}You can now call her to hang out on afternoons, but she will likely be confused when she realizes she never personally gave you her number!{/i}"

    s "This is a big victory for me."

    scene harukaalone22
    with dissolve

    h "Well I’m sorry to be the bearer of bad news but I’ve got a big loss for you coming up next."
    s "What? What happened?"

    if bonus == True:
        h "So when I told Rin just now that we were talking about sharing her-"
        s "You actually told her that? I thought you were kidding."
        h "Well, what I {i}really{/i} said was, “Would you date your teacher?”"
        s "Why? You completely removed yourself from the equation and this was entirely your idea."
        h "I’m testing the waters. Just be happy I gave you her number."
        s "Haruka, what the fuck?"
        h "Well anyway, all she texted back was the upside down smile emoji."
        s "That could mean anything."
        h "Mmm...I think in this case it means “I’d rather date you, Haruka. You’re so pretty and your boobs are great.”"
        s "You sound like a grown-up version of my [niece]."
    else:
        h "I accidentally texted Molly instead."
        s "Nooooooooooooooo..."
        h "What is wrong?"
        s "My accountant does not want me conversing with Molly."

    scene harukaalone23
    with dissolve

    h "Wanna give me {i}her{/i} number in exchange for Rin’s?"
    s "I don’t think she’s your type. And also no."

    scene harukaalone24
    with dissolve

    h "Fine. Looks like I’ll just have to send Rin a wink emoji and forever ruin your chances of romancing her."
    h "I’ve been around these girls long enough to know how they operate and-"

    scene harukaalone25
    with dissolve

    h "Woah!"
    s "Woah what? What happened?"

    if bonus == True:
        s "Did Rin say something else?"

    scene harukaalone26
    with dissolve

    if bonus == True:
        h "No, but Molly did."
        s "You texted her too?"
        h "It was a group text with the two of them."
        s "You didn’t even do it privately?..."
        s "What did Molly say?"
        h "Six eggplant emojis and then water droplets."
        s "..."
        s "Is that good? That sounds good."
        h "Too good. You should be worried."
        s "Well, at least I went one for two."
        h "..."
        s "..."
        h "You’re gonna tell me if anything happens, right?"
    else:
        h "Rin has been kidnapped by a secret, evil organization!"
        s "We must rescue her immediately."
        h "I agree! We must!"

    scene black
    with dissolve2

    if bonus == True:
        s "Probably not."
        h "And you call yourself my friend..."

        "Haruka and I hang out for a while longer and she continues to lecture me on the meanings of different emojis."
        "I immediately forget all of them because it is a stupid conversation topic and I honestly just don’t care."
        "Eventually, I wind up walking home-"
        "And once again thinking about how nice it would be to memorize these streets."
    else:
        "Haruka and I put on our superhero costumes and take off down the street using our cool grappling hooks and rocket boots."
        "We bust into the secret lair of Dr. Badguy and get our friend back after a super intense fight Selebus didn't have time to capture CGs for."
        "It was really awesome, though. I wish you could have been there."

    $ renpy.end_replay()
    $ harukadate15 = True
    $ haruka_love += 1
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label harukainvite1:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "I’ve been to her place several times now, so I figure it’s about time to show her the same sort of hospitality she’s shown me."
    "That and I feel kind of bad since she’s always talking about how lonely she is and whatnot."
    "But hey, we’ve been gradually getting closer with one another lately. "
    "And she’s one of the few people I know that I don’t feel strange about being seen in public with."
    "Sure, Ami will likely react the same way she reacted when Sara came over for the first time, but it’s not like I’m going to just avoid everyone because of that."
    "Besides, Ami and Sara {i}did{/i} get along by the end of that visit."
    "I’m sure something similar will happen with Haruka."

    play sound "phonebeep.wav"

    h "Hey! What’s up?"
    s "Hey, Haruka. Do you have any plans tonight?"
    h "Does eating an entire pint of ice cream count as a plan?"
    s "Not really, no."
    h "Then I’m totally free. Why?"
    h "Do you want to hang out?"
    s "I do. How would you feel about coming over to my place for a change?"
    h "Your place? Isn’t that on like, the opposite side of town?"
    s "Don’t you have a car?"
    h "Yeah but...gas."
    s "That sounds like a very minor struggle compared to me taking the bus to your place all the time."
    h "Then you should get a car, too!"
    s "But...gas."
    h "Hahaha~ Okay, okay. I’ll come over."
    h "Can you text me the address?"
    s "Sure thing. See you soon."
    h "Yup! See you!"

    play sound "phonebeep.wav"

    "I hang up and immediately type out my address to Haruka, who responds with a quick thumbs-up."
    "From this point on, the night becomes a mission with the objective of only partially ruining Ami’s life rather than full on destroying it."

    scene black
    with dissolve
    stop music fadeout 5.0

    "You see...in her eyes, each new woman that shows up is another obstacle separating the two of us."
    "And, in addition to being much closer to my age, Haruka possesses one other thing that is sure to set Ami off almost immediately."
    "........."
    "......"
    "..."

    scene harukafirstinvite1
    with dissolve
    play music "normalday.mp3"

    s "Your boobs really {i}are{/i} huge, Haruka."
    h "Dude. What kind of greeting is that?"
    h "You haven’t even said hi yet."
    s "Sorry. I wanted to, but it’s been getting a lot harder keeping my thoughts to myself lately."
    h "That sounds like something that could get you into serious trouble someday. "
    h "Like, what if I got super offended by that and stormed out of here?"
    s "Would you have preferred if I called them small?"

    scene harukafirstinvite2

    h "I would have preferred if they were never the conversation topic to start off with."
    s "Oh, okay. I think I’m starting to see the issue."

    scene harukafirstinvite3
    with dissolve

    h "I sure hope so. I kind of directly pointed it out for you."
    h "It’s one thing to stare, which you’ve...very obviously been doing this entire time, but coming out and talking about them isn’t exactly polite."
    h "Like, you don’t see me walking in and being like “Wow...Your shoulders are so broad and you’ve got the figure of an ancient roman warrior.”"

    if bonus == True:
        h "“And your hands look like the perfect size for...grabbing a girl by her wrists and...”"
    else:
        s "Please say things like that when you walk in. They will make me feel better about myself. Between you and me, I am very insecure."

    scene harukafirstinvite4
    with dissolve

    h "Yeah I’m just gonna stop talking before I say something else that makes me sound like a creep."

    if bonus == False:
        s "This is why I am so insecure."

    s "Looks like I’m not the only one having trouble keeping my thoughts to myself."
    h "I spend so much of my time inside the cafe that I’m beginning to struggle in the outside world."
    h "I think it might be time for an intervention or something."
    h "Please save me from myself, Sensei."
    s "Uhh, sure."
    s "Where do you want to start?"

    scene harukafirstinvite5
    with dissolve

    h "What do you mean? "
    h "Do you not have a plan or anything for tonight?"
    s "I've gone to your house a bunch of times and {i}you've{/i} never had a plan. We always just sit there and watch TV."
    h "Duh. That’s my default setting. "
    h "If nobody drags me out of the house, I’ll just do that every day for the rest of my life."
    h "I kind of need somebody to lead the way or I’ll turn into a giant, pink blob who can recite all nine seasons of The Office by heart."
    s "That show isn’t even funny. "
    h "The only people who say that are contrarians or those who think they’re somehow too good for it because it doesn’t appeal to their {i}superior intellect{/i}."
    s "This sounds like a topic you feel very strongly about."
    h "I’m tired of people pretending The Office isn’t funny. They should all die."
    s "..."
    s "Okay, well anyway...I guess we can just watch TV since that seems to be the entirety of your comfort zone. "
    s "But there is something I should warn you about beforehand."
    h "You don’t have one of those doors that I’m not supposed to open under any circumstance, do you?"
    s "What? No. "
    s "Why would you assume that?"

    scene harukafirstinvite6
    with dissolve

    h "If there’s anything I’ve learned from all that time I’ve spent in my “comfort zone,” it’s that the people you {i}don’t{/i} expect to have secret doors are always the ones that actually have them."
    h "But...I guess you seem kind of like you’d have one. So that means there shouldn’t be one here after all."
    s "Did you make the insult extremely elaborate on purpose or was that just accidental?"
    h "A mixture of both, I guess?"

    scene harukafirstinvite7
    with dissolve

    h "So, what’s the thing you need to warn me about? "
    h "You’re not just renting this place out from some creepy old guy who’s going to walk out of his room in nothing but his boxers, are you?"
    s "Again with the strange assumptions..."
    s "The warning is that I’m not sure where my [niece] is today and she could come home at any moment."

    scene harukafirstinvite8
    with dissolve

    h "Then why didn’t we just chill at my place?"
    h "I’m going to feel really awkward if she just comes in and sees us hanging out when I’ve never even met her before."

    play sound "dooropen.mp3"
    scene harukafirstinvite9
    with dissolve

    a "Who are you and why are your boobs so big?!"
    h "See? This is totally weird for me now."
    s "Ami, this is Haruka. She’s a friend of mine."
    a "That still doesn’t answer the second question!"

    scene harukafirstinvite10
    with dissolve

    if bonus == True:
        h "Is mentioning the size of someone’s chest a thing your entire family just...does for some reason?"
        s "I guess. But I do it out of interest and Ami does it out of jealousy."
    else:
        h "If she continues, I am going to melt her."
        s "Please don't."
        h "I have special melting powers."
        s "Haruka no."

    a "People like you make me sick..."

    if bonus == True:
        a "Using their bodies to seduce my [uncle] when everyone is FULLY AWARE that he likes smaller girls like me!"
        h "Really? Is that true?"
        a "Yes! The smaller, the better!"
        s "Okay, moving right along."

    scene harukafirstinvite11
    with dissolve

    h "I don’t think she likes me very much."
    s "She’s like an animal. She’ll warm up to you the more she sees you."
    a "I’ve seen her plenty of times. That’s the cafe lady."

    if bonus == True:
        a "Rin always talks about how great her boobs are."

    scene harukafirstinvite12
    with dissolve

    h "Okay, people seriously need to find other things to say about me. This is getting obnoxious."
    s "At least none of them are hiding their true feelings."
    h "I kind of wish they would."

    if bonus == True:
        h "Though, it {i}is{/i} nice hearing that secondhand affirmation from Rin. Thank you, Sensei’s [niece]."
        a "She doesn’t even know my name..."
        s "I’m pretty sure I’ve told it to her before."
        s "She’s likely just being rude to you since you’re being rude to her."

    scene harukafirstinvite13
    with dissolve

    a "What ever happened to Sara?! She was much nicer to me and her boobs were way smaller!"
    a "Did you cast her aside for a discount on coffee?! We have coffee at home!"
    h "Sara’s been here already?"
    s "Yeah, I invited her over a while back. "
    h "I see..."
    s "Ami, if you want to see Sara, you can just go visit her at the bar."

    if bonus == True:
        a "And do what?! Drink Shirley Temples and talk about what things were like in the old days?!"
        a "I’m not even old enough to drink, jerk!"
        s "Then go with Molly. That’s never stopped her."
    else:
        a "No one likes me! I have no one to go with!"
        s "Molly likes you, I think."
        a "Molly has work so I {i}can't{/i} go with her!"

    scene harukafirstinvite14
    with dissolve

    h "She’s off today, so you probably could."

    if bonus == True:
        h "Molly got paid this week and I’m pretty sure Sara wouldn’t mind selling to anyone underage as long as it meant profit for her."
        a "I appreciate the tip but I don’t even like alcohol and I definitely do not feel safe leaving your awesome boobs alone with my [uncle]."
        h "Wow...[teenage]girl chest-envy really is alive and well, huh? "
        h "It’s a shame, too. You’re such a cute girl. "
        h "Having boobs this size would make your proportions all weird and your [uncle] probably wouldn’t even talk to you anymore."

        scene harukafirstinvite15
        with dissolve

        a "M-My proportions would obviously change along with them!"
        a "Nobody gets huge boobs without...the rest of their body growing, right?!"

        scene harukafirstinvite16
        with dissolve

        a "But...wait. Uta’s boobs are still growing and she’s even shorter than me..."
        a "Would I really...look weird if..."
        s "I can’t believe I’m saying this, but let’s stop talking about boobs for a second."

        scene harukafirstinvite17
        with dissolve

        h "Hah...{i}Finally{/i}..."
    else:
        a "Nevermind! Maybe I {i}will{/i} go with Molly!"

    scene black
    with dissolve

    "Ami kicks her boots off at the door and tosses her scarf onto the couch, immediately taking a place beside Haruka right after."

    if bonus == True:
        "Likely to protect me from the allure of her huge boobs."

    scene harukafirstinvite18
    with dissolve

    a "How long is she staying for?"
    h "As long as I want. Right, Sensei?"
    a "I’m not asking {i}you{/i}, cafe lady. I’m asking my [uncle]."
    s "As long as she wants."
    a "And that car parked outside of the house, is {i}that{/i} hers too?"
    h "Yup! That’s mine."
    a "I’m asking-"
    s "Yes. That is Haruka’s car."

    scene harukafirstinvite19
    with dissolve

    a "Hah. Owning a car in an urban area like Kumon-mi? Sounds a lot like overcompensation to me."
    h "Nah. I just had some extra money to spare and needed a way to commute back and forth between {i}my own apartment{/i} and my {i}independently owned business{/i}."
    a "Joke’s on you. I’m perfectly content living with my [uncle] and working part time at a place with super cute outfits instead of ugly green visors."

    scene harukafirstinvite20
    with dissolve

    h "Hey! That shade of green was the result of an informed decision based on years of experience in marketing and service!"
    h "Green and brown are earthy colors that create a relaxing atmosphere! "
    h "Also, your sweater is like the same exact shade of green as the one in the cafe!"

    scene harukafirstinvite21
    with dissolve

    a "Nuh-uh! How can you even {i}get{/i} a business license if you can’t tell the difference between your ugly shade of green and OLIVE?!"
    s "Wow. You two are getting along even better than I thought you’d be."

    scene harukafirstinvite22
    with dissolve

    a "What do you see in this woman, Sensei?"
    s "I-"
    h "If you say my boobs, I’m going to kill you."
    s "...I wasn’t going to say that."
    s "I was going to talk about how down to earth and chill you are."

    scene harukafirstinvite23
    with dissolve

    s "Ami, you don’t have to like Haruka, but what will being mean to her do at this point?"
    s "The two of us are already friends, so it’s not like you’re going to get in the middle of that."
    a "But if I’m mean to her and make her feel really weird, she won’t want to come back and hang out with you again."
    h "She’s got a point. This isn’t very fun."
    s "Yeah, but then that would just mean I’d be going to her place instead. Doesn’t that sound even worse?"
    a "You wouldn’t..."
    s "I already have."

    scene harukafirstinvite24
    with dissolve

    a "You have?!"
    s "Of course. It’s not like I just saw her at the cafe one day and said, “Hey, wanna head back to my place?”"
    a "Isn’t that exactly how adults meet each other nowadays?!"
    h "I mean, that’s {i}kind of{/i} what happened."
    h "I gave him my number under the pretense of checking on Rin when she was feeling down, but I really just wanted him to call me so we could get to know each other."
    h "Looks like my plan worked out really well, huh? "
    h "I’m already meeting the family and everything."
    h "Is there a dog I can pet anywhere? A cat?"

    scene harukafirstinvite25
    with dissolve

    h "Should I just pet this thing instead? She seems kind of feisty."
    h "She doesn’t bite, does she? Cause if she does, I’ll sue."
    a "That head is reserved for my [uncle]! I didn’t give you permission to touch me!"
    h "I’m bigger and stronger than you. Try and stop me~"

    scene harukafirstinvite26
    with dissolve

    if bonus == True:
        a "Sensei! Stop her! I’m being sodomized!"
        s "Where did you even learn that word?"
        h "Please. If I was sodomizing you, {i}you’d know it.{/i}"
    else:
        a "Sensei! Stop her! I am melting!"
        h "Feel my wrath, accountant."

    s "Haruka, that’s terrifying."
    h "What? She started it."
    h "I’m just trying to enjoy my time as an intruder here since we were so {i}rudely{/i} interrupted."
    a "I literally live here! Nothing I do is an interruption!"

    scene black
    with dissolve2

    "Haruka and I spend the next couple hours talking in the living room while Ami sits on the couch across from us, staring at her the entire time."
    "Despite the death glare, however, Haruka remains completely unfazed- which I’m sure makes Ami even angrier."
    "I guess there was no way this visit could have ended as successfully as the one with Sara, but it definitely...could have been worse, I guess?..."
    "No one died. And that’s really all I can ask for when it comes to things like this."

    $ renpy.end_replay()
    $ harukainvite1 = True
    $ haruka_love += 3
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label harukainvite2:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "Ami isn’t going to be around today, but I feel like there’s a good chance Haruka will still refuse to come over on the off chance that that changes- and understandably so. "
    "The two of them meshed together just about as well as peanut butter and arsenic, so a refusal may very well be in the cards."
    "She’ll likely invite me to her house instead...but if the two of us are ever going to get anywhere, serious or not serious, some bridges need to be burned."
    "And yes, the bridge in this case has only existed for a combined total of three hours if you count all of the time she’s spent in my home."
    "But I want that number to grow."
    "And I’m also tired of riding the bus."
    "It smells bad and the seats are uncomfortable."

    play sound "phonebeep.wav"

    h "Hey, [harukamaster]. What’s up?"
    h "You busy tonight?"
    s "I am not. That’s actually why I’m calling."
    h "Cool beans. Can I come hang out at your place?"
    s "Wait, really? Even after how things went with Ami last time?"
    h "Oh, I’m not worried about her today."
    s "Why not?"
    h "Because she’s with Rin, Molly, and a few other girls I don’t know the names of right now. "
    h "They were all hanging out at one of the tables in the back of the cafe when I left."
    h "I’m actually still in the car now, so I can start heading over if that's okay with you."
    s "Yeah, that’s fine. I should be home soon anyway."
    h "Sweet! Gonna hang up now since talking on the phone and driving is illegal. Byeeee!"

    play sound "phonebeep.wav"

    "Haruka hangs up and I quicken my pace so I can make it home before she gets there."
    "I’d feel a little bad having her stuck in her car while I’m still walking and-"

    s "Wait."
    s "I could have asked her to pick me up..."

    scene black
    with dissolve2
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene harukasecondinvite1
    with dissolve2
    play music "acoustic.mp3"

    h "Hey! Thanks for having me over again."
    h "And thanks for not immediately bringing up my chest the second I walked through the door."
    s "I learned my lesson last time. "
    h "You should teach Molly. She still does it at least five times every day."
    s "That’s it? I figured it would be more."

    scene harukasecondinvite2
    with dissolve

    h "Yeah, it’s actually a surprisingly low amount when you consider the type of person she is."
    h "But I was more or less the same when I was her age, so I get it."
    s "I can not imagine you being anything like that girl."

    scene harukasecondinvite3
    with dissolve

    h "I definitely wasn’t as...outgoing as her."
    h "But I was definitely on the geekier side and spent pretty much all of [high_school] being jealous of other, prettier girls."
    h "Also, my “assets” didn’t really grow in until later, so I didn’t have any of that same envy I  get from my employees and...apparently now your [niece]."
    s "Well, I’m glad you turned out the way you did."
    s "I’m probably biased since I see you pretty often, but I think you’re alright."

    scene harukasecondinvite4
    with dissolve

    h "Hey, cool. I think you’re alright too. What are the chances of that?"
    s "We have so much in common."
    h "We’re both adults."
    s "We both look after [teenage]girls for at least six hours every day."
    h "We both drink black coffee and wear...black shirts in the winter."
    s "We’re both moderately attractive."
    h "And great kissers."

    if harukasex == True and bonus == True:
        s "And we’ve both [masturbate]d to Rin at least one time."
        h "A lot more than once. Not gonna lie."
        s "Same."
        h "That girl can get it."
        s "I fully support you in your endeavors, Haruka."
        h "And I in yours, [harukamaster]."
        h "Though, you’ve got a much better shot at it than I do. Even {i}with{/i} the whole “preferring girls” thing."
        h "Not like I’m actively pursuing it or anything. I’m fine with living vicariously through you as long as you’re not stingy on the details."
        s "I will do my very best for the sake of your masturbation habits."
        h "Thanks. They’ve gotten pretty out of control over the last couple years."
        s "Well hey, at least you’ve got me now, right?"
        s "No point in masturbating if you can just give me a call and-"

        scene harukasecondinvite5
        with dissolve

        h "..."
        s "..."
        h "..."
        s "Haruka?"

        scene harukasecondinvite6
        with dissolve

        h "Oh, sorry. Right."
        h "Um, hey..."
        h "We’re still only just friends, right?"
        s "What do you mean?"
        h "Like, when you say that “I’ve got you,” you don’t mean I literally {i}have{/i} you."
        h "You’re messing around with a bunch of girls. And that’s totally chill."
        h "But like..."
        h "All you’re doing for me is...occasionally filling a void that...I have a hard time filling on my own."
        h "And we could stop doing it at any time and both be totally fine with it."
        s "I mean, yeah. That’s technically correct."
        h "Cool. Because I’m...definitely not interested in anything more than that."
        h "I like hanging out with you and...I have fun flirting, but..."

        scene harukasecondinvite7
        with dissolve

        h "I can’t help but feel really shitty about myself any time we actually...talk about what we do together."

        "Ahh..."
        "She’s still in denial."
        "In denial that I’m able to make her feel ways the man she “loves” can’t and was likely {i}never{/i} able to."
        "I’ve seen the way she falls apart beneath me."
        "In front of me."
        "On top of me."
        "But even though I’ve watched her break in so many ways, she still thinks she’s put together perfectly."
        "An uncracked porcelain doll."
        "How precious."

        s "There’s no need to talk about it at all then."
        h "Right."

        scene harukasecondinvite8
        with dissolve

        s "And it’s not like there’s any chance things will ever progress because-"
        h "Can we go in your room?"
        s "..."
        s "What, like, right now?"
        s "Isn’t this a weird time?"
        h "No. I’m starting to think about stuff and I need to get my mind off of it or I’m probably going to cry."
        h "I don’t want to cry here. I’d feel like shit."
        h "Just...help me take my mind off of things."

        scene black
        with dissolve2

        "Of course, we all know that the “things” Haruka wants to get her mind off of are how her husband is likely dead and about how, any minute now, she’ll be filled with another man’s seed."
        "And, if this were a different world- one where it was okay to replace old flowers with new ones after the initial inhabitants rot to death-"
        "That seed would form roots."
        "The roots would {s}turn to wires{/s} sink deep into the soil."
        "And bloom into a beautiful, sick rose."
        "I close my eyes and wish for God to exist so he can watch me pluck yet another fruit before it’s fully ripe."

        jump harukainvite2sex
    if harukasex == True and bonus == False:
        s "And exceptional huggers."
        h "Oh snap. Does this mean what I think it means?"
        s "That it's time to watch Wheel of Fortune and eat Chinese food?"
        h "You always say just what I want to hear."
        s "Let's put on weird hats and stare at people as they walk down the street."
        h "Yessssssssssssssss, I brought my grandmother's bonnet in hopes that this would happen."
        s "Can I be the one to wear it this time."
        h "Is my name Stephanie?"
        s "No."
        s "Oh."
        s "Damn it."

        scene black
        with dissolve

        "Haruka and I put on our weird hats but no one ever walks down the street."
        "Probably because no one actually exists and that this is all just some sort of illusion planted in my brain by the government."
        "Does Haruka even real?"
        "Who knows?"
        "Certainly not this guy."

        $ renpy.end_replay()
        $ harukainvite2 = True
        $ haruka_lust += 3
        $ harukasex = True
        stop music fadeout 8.0

        "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
        "{i}You can now invite her over to the house on nights and choose to raise your affection or lust with her!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

    else:
        s "I mean, I agree...But it's kind of weird for you to randomly bring that up again."

        scene harukasecondinvite9
        with dissolve

        h "Oh my god! I really didn’t mean to say that out loud..."
        s "Freaking out will just make it more awkward. It’s not really a big deal."

        scene harukasecondinvite10
        with dissolve

        h "Right. Because, when you’re married, it’s totally fine to just get drunk and make out with guys you barely even know."

        "And, of course, now it's awkward."

        s "I wouldn’t say you barely know me. You-"
        h "I don’t even know your first name."
        h "And the only reason I know your surname is because one of my employees told me."

        scene harukasecondinvite11
        with dissolve

        h "So don’t act like that was just some little thing. It was so much bigger than that."
        s "You were drunk. It happens."

        scene harukasecondinvite12
        with dissolve

        h "I fucking know that! But it shouldn’t!"
        h "I’m so fucking...{i}alone{/i} every day that I couldn’t help but jump on the first guy who showed me some sort of affection!"

        "Why is this happening?"

        h "Do you think I {i}want{/i} to feel this way about you?! Of course not!"
        h "But even now, I’m saying things that any sane, married woman would never say because I’m scared of what will happen if the guy I married never comes back!"

        if bonus == False:
            "Haruka stop, it was just a hug."
        else:
            h "And now, instead of thinking of my {i}husband{/i} fucking me any time I lay in bed and give into how pathetic I am, I’m thinking of you!"
            s "..."
            h "..."

        scene harukasecondinvite13
        with dissolve

        h "I’m sorry...that was totally random and uncalled for."
        h "I’m just...really...I don’t know..."
        h "I keep trying to bottle up what happened back then and...how you were nice enough to not take advantage of me..."
        h "But there’s an ugly part of me that..."
        h "May have wished you did..."

        if bonus == False:
            s "Sorry, Haruka. I only do consensual hugs."

        scene harukasecondinvite14
        with dissolve

        h "Why?..."
        h "Why’d he have to leave, [harukamaster]?"
        h "I miss him so much..."
        h "I miss not feeling like I’m the worst person in the world..."
        h "Being able to fall asleep at night..."
        h "And then waking up next to someone special to me..."
        h "I just want everything to go back to normal."
        s "..."
        h "..."
        s "What exactly do you want me to say to that?"
        h "..."

        scene harukasecondinvite15
        with dissolve

        h "Who knows?"
        h "I’m clearly an indecisive {i}bitch{/i} who can’t even sort her own feelings out."
        h "You really expect me to know what I want to hear from you?"
        h "I don’t know. Maybe I just needed to vent or something."
        s "Is venting enough?"

        if bonus == True:
            h "Probably not. But what else am I supposed to do? {i}Fuck{/i} you and just commit to being a horrible person?"
        else:
            h "Probably not. But what else am I supposed to do? {i}Hug{/i} you and just commit to being a horrible person?"

        h "Give up hope altogether and choose a physical connection over an emotional one I’ve had for years?"
        s "If that’s what makes you happy."
        h "What will make me happy is my husband coming back."
        s "You know I can’t do anything about that."
        h "Obviously."
        h "There’s nothing you can do that will fix everything and there’s nothing I can do to successfully cope."
        h "So what’s even the point? I lose no matter what."
        h "I just want to go home and sleep now that I’ve ruined any chance of you ever inviting me over again."
        h "Stupid Haruka. Stupid random emotional breakdowns."

        if bonus == True:
            h "Stupid sex drive. Stupid husband."

        h "Everything is stupid."
        s "..."

        "There are two options I have here."
        "And they’re ones that I’m familiar with since I’ve made this same choice in the past."
        "But now, it falls on me to decide things once and for all."
        "If I decide right now to leave Haruka and her marriage alone, I’ll be leaving things that way for good."
        "But..."

        if bonus == True:
            "If I’m okay with destroying everything she’s built over the years for an opportunity to sleep with her-"
        else:
            "If I’m okay with destroying everything she’s built over the years for an opportunity to hug her-"

        "I can tap into her vulnerability right now-"

        if bonus == True:
            "And be inside of her within the hour..."
        else:
            "And do the hug thing."

        menu:
            "Be a gentleman again":
                s "..."
                "I can’t do it."
                "Not when she’s still this torn."
                "If I’m going to be a homewrecker, I at least need the woman to be fully on board."
                "I honestly couldn’t care less about Haruka’s husband."
                "But, to some extent, I care about Haruka."

                if bonus == True:
                    "And there’s no way I’d be able to hold an erection if I know she’s miserable the entire time."
                else:
                    "And I am too kind to hug another man's wife."

                s "Maybe we shouldn’t hang out today after all."

                scene harukasecondinvite16
                with dissolve

                h "Hahaha...Yeah, I kind of deserve to be kicked out after that meltdown."
                h "I’m sorry. I’m clearly not in the right state of mind today."
                h "You’re a really good friend, Sensei."

                if bonus == True:
                    h "There are a lot of other guys who would have tried to take advantage of me after something like that, but..."
                    h "You were somehow able to resist."

                h "I really get why Rin likes you so much."
                h "You can be a great guy when you want to."
                s "The catch is that I don’t normally want to, so consider yourself lucky."
                h "I do. Really."
                h "And if there’s ever anything I can do for you that isn’t...you know..."
                s "Unfaithful and horrible?"
                h "Yeah. If there’s anything like that, just let me know."
                h "But, for now...I’m gonna head home."
                h "It obviously doesn’t have to be right away, but...I {i}do{/i} hope you’ll invite me back sometime."
                h "As friends..."

                scene black
                with dissolve2

                "{i}Interesting!{/i}"
                "{i}It seems that you’ve chosen a path that doesn’t make you feel bad about yourself.{/i}"
                "{i}Why?{/i}"
                "{i}You know that nothing is real, don’t you?{/i}"
                "{i}Now, you’re locked out of Haruka’s romance route.{/i}"
                "{i}What if her husband IS dead, huh? Then what?{/i}"

                if bonus == True:
                    "{i}You gonna fuck her on the rebound?{/i}"
                    "{i}Maybe shoot for a hot blowie in the bathroom of the cafe?{/i}"

                "{i}You’re strange.{/i}"
                "{i}You make strange choices.{/i}"
                "{i}I don’t like you very much.{/i}"

                $ renpy.end_replay()
                $ harukainvite2 = True
                $ harukaskipped = True
                stop music fadeout 5.0

                "{i}Haruka’s lust stays exactly the same because you have morals!{/i}"

                if day >= 6:
                    jump endofsat
                else:
                    jump endofweekday

            "Fuck another man’s wife" if bonus == True:
                jump harukawhyx
            "Do the hug thing" if bonus == False:
                s "Haruka."
                s "I hope you are prepared."
                h "Prepared for what?"
                s "My birthday party next week."
                h "You're having a birthday party? Why didn't I find out until right now."
                s "Because it was a surprise."
                h "...For me?"
                s "Yeah."
                h "Why?"
                s "Ugh. This is why I didn't want to invite you."
                h "Wtf man?"
                s "Anyway, let's get this hug thing out of the way."
                h "Oh thank God. It's been so long that I was thinking I might never hug again."

                scene black
                with dissolve

                s "They don't call me {i}the hugger{/i} for nothing."
                h "Who calls you that?"
                s "The swim team. It's a long story."
                h "You should tell it to me sometime."

                "Haruka and I hug."
                "If her husband knew about it, he'd probably get really ticked off at me."
                "Take that, husband."

                h "Why are you sticking your tongue out?"
                s "Shut up."

                $ renpy.end_replay()
                $ harukainvite2 = True
                $ haruka_lust += 3
                $ harukasex = True
                stop music fadeout 8.0

                "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
                "{i}You can now invite her over to the house on nights and choose to raise your affection or hug her!{/i}"
                "........."
                "......"
                "..."

                if day >= 6:
                    jump endofsat
                else:
                    jump endofweekday

label harukadate20:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "It’s been a little while since the two of us have actually done anything and-"
    "Wait."
    "{i}Have{/i} we actually done anything?"
    "I feel like every time the two of us hang out it’s either at her house, the cafe, or my place."
    "Not that I have a problem with that, but..."
    "I can’t imagine it’s entirely fulfilling for her."

    play sound "phonebeep.wav"

    h "Hey, what’s up?"
    s "Hey. What are you doing tonight?"
    h "Probably crying and eating ice cream again. You know how it is."
    s "Want to come out and do something?"
    h "Can you wait like...two hours? I’m still at work."
    s "Still? Don’t you normally get off before dinner?"
    h "Normally, yes. But it’s been really busy and I didn’t want to leave Molly and the other part timer alone, so..."
    s "Because you were worried about her or because you wanted to keep your store from exploding?"
    h "Yes."
    s "But there were two-"
    h "Hey! Why don’t you come hang out here in the meantime? Your [niece] and her friend are here too."
    s "..."

    "I mean, it’s not like I have anything else going on, so..."

    s "Sure. I’ll start heading over now."
    h "Cool! I’ll see you soon, then."

    play sound "phonebeep.wav"

    "I hang up the phone and begin walking over to the cafe."
    "It seems that my awesome and spontaneous plan of actually going out and doing something for once is basically trashed since Haruka can’t escape work yet, but at least I’ll still get to see her."

    if bonus == True:
        "Teenagers are great and all because...yeah. But it’s still a nice break being able to hang out with someone my age who...shares the same interests as I do."
        "Frankly, there aren’t many girls out there like that."
        "At least not that I know of."
        "As always, my hands find their way into my pockets and my legs find their way ahead of themselves, bringing me closer to my destination with each and every step."

    "........."
    "......"
    "..."

    scene harukadatetwenty1
    with dissolve
    play music "cafe.mp3"

    h "Hey! That was quicker than I expected!"
    s "Hey, Haruka. Hey, everyone else."
    a "Lumping me in with “everyone else” and addressing the cafe lady by her name makes it sound like you aren’t here to see me."
    s "How would I have even known you were here?"
    a "You mean you’re not constantly watching the GPS tracker on my phone to see where I’m hanging out like I do with you?"
    s "I’m sorry, what?"
    h "Do you need anything? Coffee? Tea? A new [niece]?"

    scene harukadatetwenty2
    with dissolve

    a "I will destroy everything you love."
    h "Joke’s on you. I have nothing left but this cafe."
    s "I’m fine, thanks. I didn’t really come here to buy anything."

    scene harukadatetwenty3
    with dissolve

    h "Okay. But know in the future that I have the right to refuse service to anyone I want. And if you’re just going to loiter around the place, I won’t let you inside anymore."
    s "Well if that’s the kind of business you’re running, I’ll just have to excuse myself."

    scene harukadatetwenty4
    with dissolve

    h "Wait, no. Take me with you."
    h "I don’t want to be here anymore. I’ve been on my feet since this morning and my back is literally killing me."
    s "Gee, I wonder why."
    h "Yes, boobs. They are things I have. "
    h "Point is, I’m in pain. Please help."

    if bonus == True:
        s "I mean...I guess I could hold them for you and...take some of the weight off of your back or something."

        scene harukadatetwenty5
        with dissolve

        h "If that is what must be done for the sake of my spinal health..."
        a "Do I even need to say anything here?"
        s "You don’t. I’m pretty sure Maya’s look says enough for the two of you combined."
    else:
        s "Well, I'm not a fucking doctor, Haruka. What do you expect me to do?"

    m "You’re disgusting."

    if bonus == False:
        m "You should have gone to medical school."

    s "Thank you for explaining exactly what the look entails, Maya. I would have had no idea otherwise."

    if bonus == True:
        m "Since when do you even talk to anyone your age? This entire scenario is weird."
    else:
        m "You are such a disappointment. I can't believe I ever liked you."
        s "You what?"

    mo "You really don’t have to stay around any longer, Haruka. I’m fine on my own now."

    scene harukadatetwenty6
    with dissolve

    h "I know I don’t {i}have{/i} to...but I’d feel bad otherwise. The kitchen’s an absolute wreck right now."
    mo "I’ll just stay a little later to help the other girl clean up back there. Go out and enjoy yourself. "
    mo "It’s the least I can do after you helped me out during the great cafe calamity."
    a "Cafe...calamity? Is something wrong, Molly?"

    scene harukadatetwenty7
    with dissolve

    mo "Nope! Just trying to take advantage of my high persuasion to fend off the Magistrate of Mammaries and earn some extra gacha money while I’m at it!"
    mo "Besides, I have you two to help me if things get crazy again! And you are forced to do so as I determine the fates of your D&D characters!"
    m "It was only a matter of time until she started using this as leverage for blackmail."
    mo "Silence, Urrheak!"
    m "Scraw."
    a "I don’t mind helping, but...if you let the Magistrate of Mammaries leave, she’ll take Sensei with her and that is bad."
    h "Can we...stop using that ridiculous nickname?"
    a "Silence, boob lady."
    mo "While it may be true that the two of them will spend more time together based on this decision, I have disabled rollback and am incapable of changing courses at this point in time!"
    mo "Besides, side characters need love too!"
    h "I’m a...side character?"
    s "You’re all main characters to me, Haruka."

    scene harukadatetwenty8
    with dissolve

    a "But I’m the {i}main{/i} main character. Right, Sensei?"
    mo "I’m afraid that position belongs to me, Strawberry Songstress. Molly MacCormack is the ultimate heroine, after all."
    s "I’m actually going to give the main heroine spot to Maya for being so silent and disinterested in the position."
    m "Oh, good. Exactly what I wanted. Great."
    h "So...uhh...I guess I have the night off now?"
    s "I guess you do. "
    s "Does this mean we’re going to actually do something for once?"

    scene harukadatetwenty9
    with dissolve

    h "Do something? Us?"
    h "But we never do anything. Not doing anything is kind of our thing."
    s "There’s always...the bar, I guess?"
    h "I mean...I have a change of clothes in my office..."
    h "But Sara and I just got into an argument about which Avenger is the hottest and I’m currently mad at her."

    scene harukadatetwenty10
    with dissolve

    mo "Ooooh, who was your choice?! Iron Man?! Thor?!"
    h "{i}Black Widow.{/i}"
    mo "{i}Nice.{/i}"
    s "I have no idea what’s going on, but I was thinking maybe some bar that isn’t owned by Sara."

    scene harukadatetwenty11
    with dissolve

    h "Are you sure? She could really use the business."
    s "She’ll figure it out."
    s "I say we take advantage of my newfound desire to do something and go to the urban district."

    scene harukadatetwenty12
    with dissolve

    h "All the way over there? Are you serious?"

    if bonus == True:
        mo "Good luck with your bonus CG, Sensei."

    a "That makes it sound like a date! You never take me to the urban district! I wanna go!"
    s "It’s not a date. Haruka and I are just friends. "
    h "I suddenly feel like a college kid about to go bar hopping again."
    s "Just don’t get so drunk that I have to carry you home."

    scene harukadatetwenty13
    with dissolve

    h "Challenge accepted! I’ll go get dressed right now."

    stop music fadeout 10.0
    scene black
    with dissolve2

    "Haruka thanks Molly one more time before heading to her office to change out of her work clothes."
    "She comes back a few minutes later and the two of us say goodbye to the rest of the girls, who have already started debating some geeky stuff I couldn’t be bothered to listen to."
    "It’s clear that at least Ami is uncomfortable with the idea of me going out with Haruka, but Ami is uncomfortable with pretty much everything I do, so that’s to be expected."
    "Either way, Haruka and I wind up boarding a bus to the urban district and, in less than fifteen minutes, we’re wandering the streets..."

    scene nightsky
    with dissolve
    play music "samhain.mp3"

    "We wind up stopping at whichever bars we can find inside of the concrete jungle as the night ticks on and on."
    "I don’t know if it’s just all of the walking that’s keeping her sober-ish, but Haruka doesn’t seem fazed at all even after the fourth bar. "
    "In fact, about two or three hours of drinking go by before I start to see any signs of inebriation in her at all. And even {i}I’m{/i} feeling a little buzzed at this point."
    "None of it feels out of the ordinary, though."
    "In fact, if you get rid of all the conversation, it hardly even seems like I’m out with {i}anyone{/i} right now."
    "I don’t have to watch what I say (Which I never do anyway, to be completely fair) and I don’t have to mind what I do."
    "We’re just two human beings spending more money than we probably should, and more time in new places than we typically would."
    "It’s...a strangely good night."
    "One that I doubt I’d ever be able to recreate with someone like Sara or Maki."
    "..."
    "Maybe I...actually like doing things every once in a while?"

    scene harukadatetwenty14
    with dissolve

    h "Ah! Is that snow? Do you see snow, Sensei?"
    h "Quick, look up. Before it melts."
    s "It’s just frozen rain. It’ll be gone before the weather even has a chance to get hotter."
    h "Oh, shut up. Don’t be such a buzzkill now that all of the bars are closing. Get excited about something for once."
    s "I’m not going to get excited about the water cycle, Haruka."

    scene harukadatetwenty15
    with dissolve

    h "Fine then. You pick. "
    h "What do you want to talk about?"
    h "Girls? Boys? Us?"
    s "Us?"
    h "Yeah, us."
    h "I can’t be the only one thinking about how much fun tonight’s been, right?"
    h "Like, I’m all for wrapping myself up in[teen]drama, but spending time away from it for a change and just...not focusing on anything with you has been pretty awesome."
    h "Even with Sara and stuff, it’s hard to really feel like...I don’t know, detached?"
    s "Detached from what, exactly?"
    h "Everything, dude."

    scene harukadatetwenty16
    with dissolve

    h "Like, it feels like...the rest of the world’s been deleted and that the urban district is all that’s left."
    h "And that we no longer have anything to actually worry about, so we’re just being ourselves and...enjoying it in the simplest way possible before everything comes back tomorrow."
    s "Well, I’m glad you managed to have a good time."
    s "I’d be lying if I said I wasn’t having fun as well."

    scene harukadatetwenty17
    with dissolve

    h "Exactly! You’re the first guy since my husband that I’ve been able to feel like this with."
    h "Which isn’t me hitting on you, by the way. That’s not what I’m getting at here."

    scene harukadatetwenty18
    with dissolve

    h "I’m just glad that we did this tonight. "
    h "Like, if you never called, I’d probably still be cleaning the cafe right about now."
    s "It’s been several hours and I highly doubt the girls are still there."
    h "Okay, whatever. I still want to thank you for saving me at least an hour of cleaning."
    h "You’re thankful too, right? For having me, I mean."
    s "Are you fishing for compliments now?"
    h "I’m not...{i}not{/i} fishing for compliments?"
    h "I don’t know. I’m a little drunk, but I’m basically just trying to say that it’s nice having somebody who feels like a real friend rather than just someone I’ve known for a bunch of years."
    h "Sara and Maki are great, but...there’s never anything new with them."
    h "And whether they want to believe it or not, they both kinda settled down and had kids and..."
    s "And you never stopped being young."

    scene harukadatetwenty19
    with dissolve

    h "I...don’t know if I’d go that far."
    h "I feel like, on at least some level, no one ever stops being young."
    h "It’s why even tiny things like going to bars or talking about the cute girls who served us at those bars can make us feel younger, even if it’s for just a little while."
    h "And I’m sure Sara and Maki feel plenty young, too. "
    h "Sara...probably {i}too{/i} [young]at times. But her circumstances are a lot less normal than Maki’s, as weird as that is."
    h "If anything, it’s probably more like Sara has yet to grow up."
    h "People like you and me on the other hand...who are in that weird position of being old but not {i}that{/i} old...and having just started our careers and whatnot-"

    scene harukadatetwenty20
    with dissolve

    h "It’s...cool."
    h "I don’t know. I’m probably just happy that there’s someone I can relate to who doesn’t also want to paint my nails."
    h "Is this getting weird? I feel like I’m doing all of the talking and that I might be making a big deal out of something that’s just like, totally normal for you."
    s "No, I think you more or less explained how I’m feeling. "
    s "You just did it a lot more...positively, which I guess I’m thankful for."

    scene harukadatetwenty21
    with dissolve

    h "Of course."
    h "Positivity is something I definitely struggle with sometimes, but when I’m not too busy beating myself up over things that aren’t in my control or-"

    if bonus == True:
        s "Or fantasizing about your employees."
        h "Or fantasizing about my employees, thank you for that- "
    else:
        s "Churning butter?"
        h "How did you know about that?"
        s "Edcuated guess."
        h "Well, you are correct. That is a hobby of mine."

    h "When I’m not too busy doing either of those things, I really try. You know?"

    if harukasex == True:
        scene harukadatetwenty22
        with dissolve

        h "And..."
        h "Well, it goes without saying but..."
        h "Sometimes I fail..."
        h "And I do things that no one should ever do just because I’m impulsive or-"
        s "Haruka, you really don’t have to-"
        h "No, hold on. "
        h "Sometimes I do things like that because...because I’m only human. "
        h "And...and all humans can be forgiven if they’re regretful enough."
        s "Are you regretful?"

        scene harukadatetwenty23
        with dissolve

        h "..."
        h "I want to be."
        h "It’s just...a lot harder when there are nights like this, where the takeaway is that...maybe I was never ready to settle down at all?"
        h "I don’t know."
        h "Just...thanks, I guess."
        s "For what, exactly?"
        h "For kind of...brute forcing me into realizing that I don’t understand why I do certain things or...or feel certain things."
        h "And for giving me moments where I don’t have to deal with any of that and can just...have fun instead."

    else:
        scene harukadatetwenty18
        with dissolve

        h "Actually, you don’t even have to answer that."
        h "I know you know."
        h "You’ve had...several opportunities to push me into things that would be bad for our relationship, and you haven’t taken any of them."
        h "In fact, you’ve even gone out of your way on nights like tonight to remind me that it’s okay to just...let myself go in ways that aren’t totally self-destructive."
        h "And, weirdly enough, I feel less alone tonight than I have in a long time."
        h "So, thank you...really."

    scene harukadatetwenty24
    with dissolve

    s "There’s no point in thanking me."
    s "Just live however you want and let whatever is going to happen just...happen."
    h "Sure, there might not be a point in it...but I’m still going to thank you anyway."
    h "Even if none of that had ever happened and this was the first time we’d hung out, I’d still thank you."
    s "Why, though? I haven't even done anything."
    h "That's not true."

    if bonus == True:
        h "For example...Tonight, you helped me remember that being [young]isn’t everything by choosing to go out with me instead of spending your time with three hormonal [teenager]s."
        s "Two hormonal [teenager]s and one weird shrine maiden."

        scene harukadatetwenty25
        with dissolve

        h "If you think for a second that third girl doesn’t get under the covers and finger herself at least once a week, boy do I have news for you."
        s "..."
        h "..."
        h "What?"
        s "Nothing. I like that image."
        s "I just can’t help but feel like she’s listening in and judging me at every moment, so I’m being careful to not inadvertently upset her."
        h "Well...whatever. You get what I'm saying."
    else:
        h "But I guess it makes sense that the man who defeated Dr. Badguy would be so humble."
        s "You helped too. Never forget that."

    scene harukadatetwenty24
    with dissolve

    h "We...should probably start heading back now, though."
    s "We’re already heading to the bus stop. Where did you think we’ve been walking this whole time?"
    h "I don’t know. I haven’t really been paying attention."
    s "That or you’re actually just a lot more drunk than you're letting on."
    h "You’ve seen me drunk. This isn’t drunk Haruka. "
    h "Drunk Haruka would have taken that thing about the third girl a lot further and then gotten way too excited."
    s "I kind of wish you {i}were{/i} drunk now."
    h "Heheh..."
    h "If only there were still some bars open..."

    scene black
    with dissolve2

    "Haruka and I make it to the bus stop a few minutes later and get on board."
    "I get off at her stop despite it being miles away from my home."
    "I’m not sure why."
    "But I say goodbye to her without so much as a parting hug and begin my journey back to the house."
    "The alcohol wears off somewhere around the halfway point and I become uncomfortably cold."
    "That discomfort feels a lot less serious, however, when I realize it’s nothing compared to what Haruka must feel every time she sees me."
    "What an interesting dynamic the two of us have."

    $ renpy.end_replay()
    $ haruka_love += 1
    $ harukadate20 = True
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label harukainvite3:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "Ami told me earlier today that she wouldn’t be around, so I figure now is as good a time as any to bring someone over."

    if bonus == True:
        "Plus, Haruka and I never got to do anything fun after our bar hopping adventure, so I would like to make up for lost {i}intimate time{/i} if at all possible."
        "And while I agree with all of that stuff she recently said about how it's nice to hang out without any of the more physical parts of our relationship getting in the way..."
        "The physical stuff is still my favorite part."
        "And it’s the only reason this relationship exists in the first place, so..."
        "Yeah, I’m pretty sure you’re able to guess what’s on my mind today."

    play sound "phonebeep.wav"

    h "Hey! What’s up?"
    s "Not much. Are you still at work?"
    h "Nope! It was actually kind of dead today, so I let the rest of the staff take over."
    h "Rin’s there tonight as well, so-"
    s "You should come over."
    h "I should?"
    s "You should."
    h "Huh."
    h "Well, then I guess I should."
    h "Am I just meeting you there or am I coming in?"
    s "Coming in, preferably. "
    h "Is your [niece] around?"
    s "She is not."
    h "I see, I see."
    h "Okay. Yeah, I’ll head over now."
    s "Sounds good. See you soon, Haruka."
    h "Yup! See you soon."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "I hang up the phone as soon as the plans are set in stone and begin the journey back."
    "The tone of Haruka’s voice carried a bit of disappointment when she found out we weren’t just meeting up and that she was coming in-"
    "But I’m sure that tone will change within a very short amount of time."
    "It always does with her."
    "........."
    "......"
    "..."

    scene harukathirdinvite1
    with dissolve2
    play music "acoustic.mp3"

    h "Hey! Sorry if I took a little while. I was in the middle of dinner when you called, so...didn’t want to leave in the middle of that."
    s "It’s fine. I just got back myself."
    h "Wow, you wanted to see me so much that you invited me over before you were even home?"
    s "I just call that being good at time management."
    s "And, speaking of which..."
    h "Speaking of which, {i}what?{/i}"
    h "Do you have a good idea of how you’d like to spend our time together tonight?"
    s "A very good idea, actually. I think we should-"
    h "Hang out on the couch and talk to each other?"

    if bonus == True:
        s "Uhh, my idea actually involved a little less clothing."
        h "Will it appease you if I take my hoodie off?"
        s "Sure. As long as you take the rest of your clothes off with it."
        h "We can’t do it today, if that’s what you’re getting at."
        s "Why not?"
        h "Because {i}we can’t do it today.{/i}"
        s "Why does this always happen to me?"
    else:
        s "Without touching, ideally. The touch of a girl always makes me nervous and I don't want to feel that way in my own home."

    scene harukathirdinvite2
    with dissolve

    h "Uhh...always?"

    if bonus == True:
        s "Well, not always. But this is definitely not the first time that-"
        s "Oh. You’re upset because that insinuates there are other people."
        h "Well, I...I mean, of course there are other people. That’s...That’s pretty obvious with the way you conduct yourself."
        h "And it’s not like I’m really...the best person to comment on that sort of thing, since..."
    else:
        s "Yes. Always."

    scene harukathirdinvite3
    with dissolve

    h "You know what? Let’s not talk about that right now."
    h "I’ve been in a pretty good mood all day and I kind of want to shut my brain off."
    s "And I’m assuming that’s why you didn’t want to stick around here?"

    scene harukathirdinvite4
    with dissolve

    h "That and I had so much fun the last time we actually went out that I was kind of hoping it was going to happen again."
    s "And it will. I just don’t feel like going out again today now that I’m home."
    h "That’s fine. I mean, this is what we do best anyway."
    h "We’ll just chill on the couch and watch TV or something."

    if bonus == True:
        s "Can you at least inform me of whether or not there is a blowjob on the way to me in the near future?"

        scene harukathirdinvite5
        with dissolve

        h "Jesus, are you really that turned on right now?"
        s "This is just what life for me is like, Haruka. It’s incredibly sad."
        h "I mean, I definitely get it. It just sounds like you’re going to die without any action."
        s "I very well may."

        scene harukathirdinvite6
        with dissolve

        h "Did you get blueballed by one of the girls in your class or something?"
        s "I have no idea what you’re talking about. The only person I am sexually involved with is a local cafe owner with pink hair."
        h "One of my competitors has pink hair. You’re not fucking the enemy, are you?"
        s "I am not fucking the enemy."
        h "Because if you’re fucking the enemy, I’m going to be really pissed."
        s "I don’t even know who the enemy is."
        h "You should have just told me that it {i}was{/i} one of your students who did this to you. That would have been a lot more exciting."
        s "Sometimes, I think you might like [teenage]girls more than I do."

        scene harukathirdinvite1
        with dissolve

        h "That’s fine, because I’m pretty sure Rin likes them more than both of us combined."
        s "I...really can’t disagree with that. "
        s "It’s kind of unhealthy, actually."
        h "Definitely."
        h "So, are we done standing around yet? Because your couch looks really comfortable and I would like to one day sit on it."
        h "I have somehow not managed to do that despite being inside on multiple occasions now. You are a horrible host."
        s "Fine. But I still want to know about the blowjob thing."
    else:
        s "As long as we do not touch."

    scene harukathirdinvite7
    with dissolve

    h "Okay, you really might have some sort of problem if this is all you can think of. "

    if bonus == True:
        h "Even I’m not this bad and I have spent well over 100,000 yen at Maki’s store."
        s "That is...incredibly depressing."
        h "I am...so very lonely."
    else:
        s "At least my significant other isn't in space."
        h "That was uncalled for, good sir."
        s "You are right. I am sorry."

    scene black
    with dissolve

    if bonus == True:
        "Haruka and I swallow our self-pity (The same way I hope that she swallows my semen before the night’s end) and take a seat on the couch..."
    else:
        "Haruka and I swallow our self-pity and take a seat on the couch..."

    scene harukathirdinvite8
    with dissolve

    "She pulls her knees up against her chest and moves closer to me than she normally does when the two of us are alone together like this."

    if bonus == True:
        "Well...when we're not naked, I mean."
        "Her clothes smell similar to Nodoka’s in that they’re essentially permanently stained with the essence of coffee, but Haruka’s also contain a tinge of..."
    else:
        "She is getting so close to breaking the no touching rule that I can smell her shampoo."

    s "Lemon?"
    h "Uhh...I’m sorry?"
    s "Oh. Nothing. Thinking out loud."
    h "Of...lemons?"
    s "I...guess so."
    s "Anyway, now what?"

    if bonus == True:
        s "We’re not having sex and it’s becoming depressingly apparent that nothing else is going to happen either, so our choices are either watching television or...talking."
        h "Do you not like talking?"
        s "It’s not that. I just think you like talking a little too much sometimes."

        scene harukathirdinvite9
        with dissolve

        h "Well excuse me for wanting to converse with you!"
        h "It’s just not often that someone is able to hear all of my rambling and not think I’m annoying, so yeah. I’m going to talk a lot."
        s "You know, once you’re surrounded by a class of twenty [teenage]girls, it’s kind of hard to be annoyed by anything else ever again."
        s "It’s one of the three big reasons I keep inviting you over instead of any of them."

        scene harukathirdinvite10
        with dissolve

        h "If you tell me that the other two are my boobs, I-"
        s "The other two are your boobs."
        h "Why am I even here right now?"
        s "Because, for some strange reason, you enjoy being around me."

        scene harukathirdinvite11
        with dissolve

        h "Yeah...it {i}is{/i} kind of strange, isn’t it?"
        h "You’re a jerk...you have an annoyingly busy schedule...and you’re probably fucking both of my friends."

        if sarasex == True and makibj == True and makisex == False:
            s "Well...that depends on what you mean by {i}fucking{/i}."

            scene harukathirdinvite12
            with dissolve

            h "Like...putting your thing in...their things..."
            s "You can use adult words in this house, Haruka. You’re not going to get in trouble."
            s "Besides, I can say with confidence that I am not fucking {i}both{/i} of your friends."
            h "..."
            s "Just one of them."
            h "Yes. Yes, you made that pretty obvious."

        if sarasex == True and makibj == True and makisex == True:
            s "..."

            scene harukathirdinvite12
            with dissolve

            h "I'm...going to assume your silence means that it's no longer just {i}probably.{/i}"
            s "Hey, you said it. Not me."

        if sarasex == True and makibj == False:
            s "Well...not {i}both{/i} of them..."

            scene harukathirdinvite12
            with dissolve

            h "..."
            s "Just one of them."
            h "Yes. Yes, you made that pretty obvious."

        if sarasex == False and makibj == False:
            s "Actually...I’m not."
            s "I haven’t done anything with either of them."

            scene harukathirdinvite13
            with dissolve

            h "Wait, really? "
            h "But...you’ve had so many chances..."
            s "There’s this one girl my age who I just like a little more, I guess."
            s "Also, may I remind you of the three reasons that I continue to invite you-"

            scene harukathirdinvite14
            with dissolve

            h "No. You may not."
            s "Damn it."

            scene harukathirdinvite15
            with dissolve

            h "But...umm..."
            h "It does make me...a little happy hearing that for some reason."
            h "It’s kind of like...I’ve beaten those two in something for once."
            h "That doesn’t really happen often."

        elif sarasex == False and makibj == True:
            s "Well...no. I’m not fucking them."
            s "But I did get a blowjob from Maki."

            scene harukathirdinvite16
            with dissolve

            if harukalust10 == True:
                s "Other than the Halloween one, I mean."

            h "Well...uhh...thanks for telling me?..."
            s "Any time, Haruka. This is what friends are for."
            h "Is it really, though?"

        s "Anyway, the fact of the matter is...and forgive me for saying something remotely kind right now, I enjoy being around you as well."

        scene harukathirdinvite17
        with dissolve

        h "Really?"
        s "Of course."
        s "Do you think I would just allow you to sit on my couch immediately after informing me that we won’t be having sex if I didn’t actually like you?"
        h "I...feel like there are a million nicer ways to explain that."
        s "I’m not good with nice explanations. I prefer to get right to the point whenever possible."

        scene harukathirdinvite18
        with dissolve

        h "Then I’ll get right to the point as well."
        h "Well, {i}a{/i} point."
        h "There are actually a lot of...points that I’d like to make to you, but...actually figuring out how to explain them without sounding like a lunatic has been a lot harder than you’d expect."
        s "This doesn’t sound like getting right to the point."
        h "The point is..."
        h "Even if...this relationship started out of pity or...sexual attraction or...whatever it was that caused the two of us to go through with...what we went through..."
        h "It’s..."
        h "It’s starting to feel like...it’s a little more than that. At least for me."
        h "Like...I still see you as a friend. I’m not saying I’m in love with you or anything."
        h "But...I think about you a lot more than someone should be thinking about a friend. And not just when I’m horny or...when I’m lonely."
        h "But when I’m doing all kinds of things."
        h "Like...the other day, I passed by some restaurant and the first thing I thought was, “It would be nice to go there with Sensei.”"

        scene harukathirdinvite19
        with dissolve

        h "That’s...that’s kind of weird, isn’t it?"
        h "Like...that’s not the kind of relationship we have...and I still can’t help but think of things that way."
        h "I’m sure that...being alone for so long must have something to do with it, but..."
        h "Yeah. That’s one of the several points that I wanted to make about...this. "
        h "It’s...It’s just nice, you know?"

        "From either up above or down below, I hope the most important person to her is listening in."
        "I hope he’s listening in and realizing that this rose belongs to me now."
        "That the flower he planted and subsequently spent years cultivating has been plucked from his garden and dropped haphazardly into a shallow vase full of dirty, unfiltered tap water."
        "This is the power of all that I am."
        "The power of the center of the solar system."
        "Everything flows into me- and I flow back into them."
        "A cycle of endless orgasms and secrets spanning across an infinite plane of time that exists for no discernible reason, but exists nonetheless."
        "True love is a lie."
        "All flowers need water."
        "You can not plant one and leave it alone."
        "And if you do, be prepared for the worst."
        "Luckily for Haruka’s husband, wherever he may be, if he even {i}is{/i} at all-"
        "I will gladly tend to his roses."
        "I will tend to every single rose in every single garden."
        "And I will smile as I do it."

        s "Yeah..."
        s "It is nice."
    else:
        h "I guess we can just wait until Ami gets home and yells at me?"
        s "Sure. We have to cut the rest of the conversation out anyway, so..."
        h "..."
        s "..."
        h "..."
        s "..."
        h "..."
        s "..."

    stop music
    play sound "dooropen.mp3"
    scene harukathirdinvite20
    with dissolve

    a "I’m home! "

    play sound "static.mp3"
    scene harukathirdinvite21
    with flash
    stop sound

    "Bury me in {s}you{/s} worms."

    play sound "static.mp3"
    scene harukathirdinvite22
    with flash
    stop sound
    play music "lastdailysong.mp3"

    a "..."
    h "Hey. Welcome back."
    a "..."
    s "Hey, Ami. We were just going to watch TV."
    a "..."

    if bonus == True:
        "So, I obviously know this doesn’t look good."
        "But, based on prior experience, this really isn’t even half as bad as it could have been."
        "I’m actually somehow thankful that we didn’t wind up having sex today because...well, you can probably imagine why."
        "Still, though. "
        "Ami is sensitive as-is, so we’ll need to navigate this carefully if-"

        a "Aren’t you married?"
    else:
        a "That's the part of the couch that I always sit on."

    scene harukathirdinvite23
    with dissolve

    h "I..."

    "Or...I guess we’re just going to jump straight to that."

    h "I..."

    if bonus == True:
        a "You what?"
        a "You are, right?"
    else:
        a "You what?"
        a "You didn't know?"
        a "It's just a couch??????"

    play sound "static.mp3"
    scene harukathirdinvite24
    with flash
    stop sound

    if bonus == True:
        a "Because I asked Molly more about you the other day after you stole Sensei away and she told me you were."
        a "Was Molly lying to me? "
        a "Or are you just a whore?"
        h "We’re...we’re just sitting here! Nothing happened!"
        s "Ami, really. Nothing happened."
        a "She looks awfully close to you for “nothing,” Sensei."
        a "I don’t think her {i}husband{/i} would like it very much if he saw the two of you like this."
        h "We’re not-"
        a "Sorry, would you mind getting off the couch if you’re going to talk to me?"
        a "I’m having a hard time focusing when you’re that close to {i}my{/i} Sensei."
        s "Ami...come on."
        h "No...No, I should probably get going."
        h "She’s...she’s right. I {i}am{/i} married...and...and..."
        h "Huh?"
    else:
        a "Because I'm pretty sure that you got all of those emails I sent about not sitting on side of the couch."
        s "Haruka did you ignore the emails"
        h "I think they were caught by my spam folder."
        a "Likely story!"

    play sound "static.mp3"
    scene harukathirdinvite25
    with flash
    stop sound

    h "Where did all these tears come from?"
    a "Are you crying now?"
    h "I’m...I..."
    a "Why are you crying if you didn’t do anything wrong?"

    if bonus == True:
        a "Could it be that maybe you already {i}did{/i} something wrong and you’re so overcome with guilt that you’re having trouble stomaching it?"
        a "Do you want a bucket? Sensei used to bring me a bucket when I was feeling nauseous."
        a "That’s a thing I know he does because he’s been with me for years and you’ve only known him for a few months."
        s "Ami, stop."
        a "Why? I live here. That’s my couch."
        a "She’s in my spot. I want her gone."
    else:
        s "She is very sensitive, Ami. Her husband was a couch."
        h "He was so comfortable."

    scene harukathirdinvite26
    with dissolve

    h "So much for her not being around today..."
    s "I really had no idea."
    h "I knew she liked you, but...doesn’t this seem a little excessive?"

    if bonus == True:
        a "Who are you to judge what is and isn’t excessive, you fucking slut?"
        a "Get away from my [uncle]. I don’t want him catching any STDs or other icky stuff that might impact how much time he gets to spend with me."
    else:
        a "Who are you to judge what is and isn’t excessive when you don't even read your emails?"
        s "She has a point, Haruka."
        h "I know. I am bad."

    scene harukathirdinvite27
    with dissolve

    s "Isn’t that enough? She’s already crying."
    s "I get that you want to keep me to yourself, but Haruka is a friend of mine. You can’t talk to her like that."
    a "Sure I can. You heard her, right? She’s married."
    a "I’m saving everybody a load of heartbreak right now."
    h "She’s...got a point..."
    h "It would...be best for everyone if...I just went home for the night."
    a "Sensei, when she leaves, what do you want me to make you for dinner?"
    s "Can you at least go into your room and let me say goodbye to her alone?"
    a "I’d really rather not."

    scene harukathirdinvite28
    with dissolve

    h "{i}Let’s...go out next time, okay?{/i}"
    h "{i}I don’t really think I’m welcome here...{/i}"
    s "..."
    s "Sure..."

    scene black
    with dissolve2

    "Haruka quickly scurries out of the living room without making eye contact with Ami."
    "But what’s so confusing to me is that, even though she was confronted and berated from the moment Ami came home, she still suggested a “next time.”"
    "Is she really so lonely that she’s fine with risking another run-in like this for a chance to be with me?"
    "Why?"
    "..."
    "Oh, right."
    "She can’t help it."
    "She’s already in my vase."

    a "Sensei! Watch a movie and cuddle with me! "
    s "..."
    a "Sensei?"
    s "..."

    "I watch a movie and cuddle with Ami."

    $ renpy.end_replay()
    $ harukainvite3 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label sadgirls2:
    scene makoffice0
    with dissolve2

    "I return to my office and collapse into my chair."
    "It is the only comfort I have felt since the day began, and will remain the only comfort I feel for some time to come."
    "As the world outside the walls jams its knife into the back of Kumon-mi, the bleeding begins in the form of a death."
    "A death that, up to this point, I had assumed was probable...yet denied the possibility of it as it’s atypical for the contents {i}outside{/i} of a container to slowly ooze their way back in."
    "What I want at this moment is to make some sort of analogy about how something like this is akin to ripping a bandage off. "
    "But this particular case feels more along the lines of unraveling a meter’s worth of gauze from a wound so infected that the final layer of fabric sticks to the holder’s skin and refuses to come off at all."
    "So as Makoto bleeds just like the walls of this city and everything it holds, I wonder which domino is the next to fall."
    "And I wonder what else it will topple when it finally does."

    play sound "phonering.mp3"

    "When I look down at my phone, the necessity of wonder dies quicker than Makoto’s father. "
    "The only thing left is discerning if this particular fatality is one that I should be afraid of-"
    "Or if it is one that I should revere."

    play sound "phonebeep.wav"

    s "Hello?"

    if harukasex == False:
        h "OH MY GOD!"
        s "Hey. Are you doing okay?"
        h "{i}OKAY?!{/i}"
        h "I’m doing way better than just {i}okay,{/i} dude!"
        h "My husband is still alive! "
        s "What? Really?"
        h "Yeah! I just got an automated call thingy from...whatever branch he was drafted by and it said that he’s perfectly fine and that his unit never even saw combat!"
        h "I didn’t get to speak directly to him, though- which kinda sucks because it’s been literally years since I’ve heard his voice. But still! This is amazing!"
        h "Anyway, yeah! I just needed somebody to freak out to about this and Maki didn’t answer the phone, so you’re officially the first to know!"
        s "Yeah...uhh..."
        s "So, the reason Maki didn’t answer is probably-"
        h "AAAAAHHHH! "
        h "Sorry for interrupting but I just can’t stop screaming! "
        s "Yeah...I can see-"
        h "I’ve gotta call Sara next! This is the best day ever!"
        h "Anyway, sorry for calling you while you’re at work and stuff! We can hang out soon and I can tell you more about it!"
        s "Haruka-"
        h "AAAAAAAAHHHHH! I’M SO FUCKING RELIEVED! HOLY SHIT!"

        play sound "phonebeep.wav"

        s "..."

        "Haruka hangs up the phone without giving me the chance to explain that things might not be this bright and joyous for everyone."
        "And that her experience is the exact inverse of what her closest friend is going through."

        scene black
        with dissolve2

        "I want to be happy for her. "
        "But there’s too much going on in my head right now to pump out such an emotion."
        "Especially after witnessing firsthand one more contrast between the light and the dark and the effects they may have on those caught within them."
        "I abandon the fleeting relief I have on Haruka’s behalf in favor of something more in line with what I often find myself focusing on."
        "And before I know it..."

        scene bedroom_night
        with dissolve2

        "I’m back at home in my bedroom."
        "I can’t even remember coming here."
        "I never heard back from Miku after telling her where to find her friend."
        "I never heard what happened to Yumi...or if Nodoka was able to walk out of school on her own."
        "The day just disappeared."
        "And I can’t tell if I should interpret that as a gift or if I should be angry that it was robbed from me."

        $ sadgirls2skip = True

    else:
        h "..."
        s "..."
        s "Haruka?"
        h "I..."
        h "Uhh..."
        s "..."
        h "I really need you right now..."

        "Reverence pours over me as if I’m caught in a downpour as the culling of another competitor makes its presence known through a small, electronic rectangle."
        "This is not the first time I have been brought joy by such a device- but it is the first time that I have felt some form of joy {i}today.{/i}"
        "How unfortunate that it must come at the expense of someone close to me."

        h "I know that you’re at work right now..."
        h "But if you can leave early, I-"
        s "Yeah. I’ll leave right now."
        h "You..."
        h "You’re just going to come?"
        h "You’re not even going to ask what happened?"
        s "There’s no need."
        s "I already know."
        s "And I’m sorry for your loss."
        h "..."
        s "..."
        h "Sensei..."
        h "I haven’t lost anything..."
        h "My husband is still {i}alive...{/i}"

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene harukatalk1
        play music "justbehappy.mp3"
        $ renpy.pause(10, hard=True)
        scene harukasgoodday1
        with dissolve4

        s "..."
        h "..."

        "I arrive at Haruka’s house to console her about the fact that she is now a confirmed adulterer and can no longer hide behind the guise of her husband being deceased."
        "This means that on at least several occasions, while she was busy cleaning my semen out of her, her husband was wondering what she was up to."
        "If only he knew that some man he never met was providing a level of sexual gratification to his woman that he could never provide himself. "
        "I wish I could have spoken to him on the phone as well."
        "I wish we all could have had a nice conversation together."
        "I wish to hear the muffled voice of a desperate wife wishing her husband safe travels as she attempts to move her tongue in the correct ways despite my massive length pressing down upon it."
        "I wish to hear the concern of the absent party when he realizes what might be going on behind his back."
        "But more than anything-"
        "I wish to share these feelings with Haruka, who I am sure is thinking the exact same thing right now."

        h "I have to kill myself."
        h "It’s the only thing I can do to make up for what I’ve done."

        play sound "laugh1.mp3"

        s "Hold your horses, Haruka! There’s no need to go that far!"
        s "I’m sure you can just apologize to him and that everything will be a-okay!"
        s "If he {i}really{/i} loves you, he won’t care how many men empty themselves inside of your vagina."
        s "You can fuck the whole city if you want to!"
        s "I just don’t really see any reason for that when we both know that my cock is the only one that will ever satisfy you at this point."
        h "What am I supposed to do?"
        s "You mean now that you can’t just imagine he doesn’t exist anymore?"
        h "..."
        s "Maybe try the opposite?"
        s "For all we know, imagining your husband is in the next room over while I fuck your brains out might make your next climax even more enjoyable."
        h "..."
        s "Not sold? Okay. Then how about we kidnap one of my students and let him repeatedly fuck them to make up for all of the times I’ve fucked {i}you?{/i}"
        s "They’re significantly tighter than you and their sex organs probably can’t take the same level of a beating but, let’s face it, there’s no way that guy can go as {b}hard{/b} as I can anyway."
        h "..."
        s "I’ll even let you pick which girl it is since I know you’re desperate for a chance to force their lips around your clitoris as well."

        scene harukatalk2
        play music "andlove.mp3"
        $ renpy.pause(6, hard=True)
        scene harukasgoodday1
        with dissolve4

        h "I have to kill myself."
        h "It’s the only thing I can do to make up for what I’ve done."

        "I dramatically turn away, wiping the sweat from my brow as I recall the moment Haruka and I first met."
        "I was a mere EMT in training back then...trying my hardest to make a positive change in the world."
        "Or at least...that’s how things were before I saw her- standing there on the opposite side of the guardrail on the Golden Gate Bridge."

        s "Do you remember when we first met?"
        h "..."
        s "You said something similar back then..."
        s "How you wanted to die..."
        s "But as a dove flew overhead, you realized you were scared."
        s "I still remember the way your hands trembled as you desperately gripped that railing."
        s "I remember the moment you slipped...and I reached out {i}my{/i} hand to prevent you from falling."
        s "Do you think it mattered in that moment who you were pledged to?"
        s "Or was I simply in the right place at the right time? The same way I was when you needed me in the bedroom all those years later."
        h "..."
        s "Come to me, Haruka."
        s "Come to me and let me save you again."

        scene harukatalk3
        play music "ihaveto.mp3"
        $ renpy.pause(6, hard=True)
        scene harukasgoodday1
        with dissolve4

        h "I have to kill myself."
        h "It’s the only thing I can do to-"
        s "Don’t say that, Haruka! Never say that!"
        s "We can figure this out together!"

        scene harukasgoodday2
        with dissolve2

        h "We...can?"
        h "It’s not too late?..."
        s "It’s never too late, Haruka! This is only the beginning!"
        s "We can start over...we can build a new life!"
        s "I know things might be hard...but things are always hard! That’s just the way this messed up world is!"
        s "But together?...You and me?..."
        s "We can fix it."
        h "Sensei..."
        s "Also..."
        s "I am pregnant."

        scene harukasgoodday3
        with dissolve2

        h "Pregnant?"
        h "Is..."
        h "Is it-"
        s "Who else could it possibly belong to?"

        scene harukasgoodday4
        with dissolve2

        h "We...we have to think of a name!"
        s "I’ve already chosen one..."
        s "It’s BigBoy420x69..."

        scene harukasgoodday5
        with dissolve2

        h "My father’s gamertag..."
        h "You remembered..."
        s "How could I ever forget?"
        s "If it wasn’t for that, we never would have met..."
        s "We never would have fallen in love..."
        s "And we never would have won the 2003 state hockey championship together despite both of us playing with broken arms."

        scene harukasgoodday6
        with dissolve2

        h "Hahah..."
        h "Sometimes...it’s like I can still feel the puck in my hands..."
        s "It was crazy they let you get away with that since you weren’t even the goalkeeper."
        h "In a way, though...weren’t we both goalkeepers?"
        h "We made a plan...and we stuck to it...no matter how hard that plan became."

        scene harukasgoodday4
        with dissolve

        h "And here we are...six million years later, still immortal and about to have our first child."
        h "I don’t even care that I’m married anymore. I know now that I want to be with you."
        s "Haruka..."
        h "BigBoy420x70..."
        s "Ha..."
        s "I see you remember {i}my{/i} gamertag as well..."

        scene harukatalk4
        stop music
        $ renpy.pause(6, hard=True)
        scene harukasgoodday1
        with dissolve4
        play music "sensei.mp3"

        h "I have to kill myself."
        h "It’s the only thing I can do to make up for what I’ve done."
        s "..."
        h "All this time...I knew I was doing something wrong...but I kept doing it anyway..."
        h "I kept doing it anyway because I’m a horrible person. "
        h "Because I’m lonely."
        h "Because waiting stopped being possible the moment someone else I was attracted to wandered into my life."
        h "I’m pathetic."
        h "Why would anyone ever want to marry me?"

        scene harukasgoodday7
        with dissolve

        h "I mean, it’s not like I have any talents or positive qualities. I’m not even a nice person. I make everything about myself because I’m too narrow minded to worry about how anyone else feels."

        scene harukasgoodday8
        with dissolve

        h "I bet it’s the tits, right? It’s gotta be the tits. That’s all I’ve got. "
        h "Just my fat, fucking tits that I show off in front of men that I’m not even married to in hopes that they’ll push me down and fuck me before I have a chance to think about how wrong it is."
        h "It was only a matter of time until I cheated, wasn’t it? This is who I really am. A worthless, disloyal bitch in heat who gives up the second there’s any sort of pressure."
        s "..."
        h "Why aren’t you saying anything? Do you get off to listening to me degrade myself? Is that why you do it all the time? Because you like me realizing how worthless I am? Is that it?"
        s "..."

        scene harukasgoodday9
        with dissolve

        h "Fucking say something! I didn’t invite you over here thinking that you’d just fucking stand there listening to me!"
        s "Why did you invite me over then?"
        s "Because you thought I could make you feel better?"
        h "There’s nothing that can make me feel better about this!"
        h "I just found out my husband is alive! I’m supposed to be happy right now! But I’m so fucking selfish that all I can think about is how I’m going to get out of this!"
        s "And the answer you settled on is killing yourself? What’s that going to do?"

        scene harukasgoodday10
        with dissolve

        h "If you’ve got a better solution, I’d love to hear it. Because I’m {i}also{/i} too selfish to die. I just think that would be the easiest and least shameful way out of what I’m going through right now."
        s "You do realize you have it a lot better than a ton of other people in your position right now, right?"
        h "Do I? So a ton of other people {i}also{/i} let random dudes routinely fuck them in a bed their husband paid for before shipping off to fight in a war?"
        h "Cause if that’s the truth, then yeah. Maybe I will feel a little less bad."
        h "But right now? I feel like stapling my fucking vagina shut so I don’t accidentally let another cock inside of it when I get too lonely."
        s "I think you’re overreacting to this, Haruka."

        scene harukasgoodday1
        with dissolve

        h "I think you should mind your own fucking business."
        s "I only came here because you told me you needed me. But the last five minutes make it sound more like you need a therapist."
        h "Excuse me?"
        s "Unless you want to just keep using my dick as therapy, I mean. Because that was working pretty well until you heard about your husband."
        h "Are you telling me that the key to coping with how much of a slut I am is continuing to be a slut?"
        s "I’m telling you that you’re making a huge deal out of something that should be {i}good{/i} news for you."
        s "The way you’re rambling on makes it sound like you’d rather deal with burying your husband than telling him you fucked some other guy."
        h "Maybe I would? I mean, we both kind of just assumed he was dead already, didn’t we?"
        h "But now that he’s not, we’re fucked. We’re fucked because we keep fucking. It’s a big fucking mess."
        s "Then let’s stop fucking if you don’t want to. It’s as easy as that."

        scene harukasgoodday11
        with dissolve

        h "It’s not “as easy as that!” I can’t just erase all of the horrible things I’ve done by not doing them anymore! That’s fucking ridiculous!"
        s "Is that the problem? Or is the problem that you still {i}want{/i} to do those horrible things because you’ve gotten addicted to them?"

        scene harukasgoodday12
        with dissolve

        h "I’ve {i}what?{/i}"
        s "Would you rather go back to fucking yourself every night? Or keep fucking me until he gets back? Because we both know which option you like more."
        h "Addicted?..."
        s "Yeah. I think that’s the case."
        s "I think that if you really felt bad about what you were doing, you would have stopped this a long time ago."
        h "..."
        s "Again, if you want to stop, {i}we can stop.{/i} I’m not forcing you into this relationship. And given your circumstances, I don’t even really think what you did was all that wrong."
        s "You went years without hearing anything. I’m sure your husband will understand if you slipped up a little because some other guy wanted to fuck you while you were desperately horny."
        h "Desperate..."
        h "Addicted..."
        h "You..."

        scene harukasgoodday13
        with dissolve

        h "This is {i}your{/i} fault!"
        s "Oh, come on."
        h "No, it is! You talked me into sleeping with you when I was on the fence about it! You took advantage of my feelings and turned me into a fucking cheater!"
        h "I didn’t do anything wrong at all! It was all you!"
        s "Does blaming me make you feel better about yourself?"

        scene harukasgoodday14
        with dissolve

        h "Of course! I have nothing to feel bad about now that I realize I was forced into this."
        h "Just wait until my husband finds out about the man who stole his faithful and devoted wife. You’re gonna be in biiiiiiig trouble."
        s "Sure. Is there anything else you want to say? Or are we done here?"

        scene harukasgoodday15
        with dissolve

        h "I don’t know. {i}Are{/i} we done here? Or is there anything {i}you{/i} want to say to try and win me back before you have to walk away from my pussy forever?"
        h "Not that I {i}can{/i} be won back, of course. I just want to see you squirm with your {i}own{/i} sense of desperation now that the girl you tried {i}so{/i} hard to screw doesn’t want to screw you anymore."
        s "I actually don’t need this as much as I think you do. There are plenty of-"

        play sound "static.mp3"
        scene harukasgoodday16
        with flash
        stop sound

        h "Bullshit! Not with tits like these, there aren’t!"
        s "Seriously?"
        h "I can see it in your eyes! You’re barely able to hold yourself back right now!"
        h "Holy shit! Look at how insatiable you are! It’s no wonder you forced me into sex while I was missing my husband!"
        s "Okay. I’m going to leave now. But it was fun coming over here just to watch you try and completely dodge the blame for your actions. We should do this again sometime."

        scene harukasgoodday17
        with dissolve

        h "What? You’re leaving? But you haven’t even gotten to the good part yet. You know you can’t leave until you get what you came here for."
        h "You’re a pathetic, horny loser who-"

        scene black
        with dissolve

        s "See you at the cafe, Haruka."
        h "Get the fuck back here! Don’t walk away from me!"

        play sound "static.mp3"
        scene harukasgoodday18
        with flash
        stop sound

        s "Why not?"
        h "Because...you can’t leave yet! You haven’t gotten what you came here for!"
        s "I came here for a few reasons."
        s "The first was to try and hear you out...and to listen to you talk down on yourself because, let’s face it, you {i}are{/i} a bad person."
        s "You’re just not nearly as bad as you think. And you can still make this right if you actually {i}want{/i} to."
        s "The second reason I came was to figure out if you actually {i}do{/i} want to. But now, I understand that you’d rather just push the blame on someone else. "
        h "That’s not..."
        h "Wait...I didn’t mean it like-"
        s "I don’t really care {i}how{/i} you meant it. You’re an adult. So confront your issues like an adult and stop getting other people involved in them."
        h "[harukamaster]. Stop. Don’t go yet. Seriously."
        s "If you don’t want me to go, give me a reason to stay."
        h "I..."
        h "I...umm..."

        play sound "static.mp3"
        scene happy1 with flash
        scene happy9 with flash
        scene happy8 with flash
        scene happy7 with flash
        scene harukasgoodday19 with flash
        stop sound

        h "AAAAAAAAAAAAAHHHHHHHHHHHHHHHHHH!!!!!!!!!"
        h "I DON’T...KNOW WHAT...TO DO!!!"
        h "I LOVE MY HUSBAND! I LOVE HIM SO MUCH! BUT..."
        h "BUT I DON’T WANT YOU TO LEAVE!!!"
        h "AND I KNOW THAT MAKES ME A BAD PERSON! I’M HORRIBLE! UNFAITHFUL! "
        h "BUT I DON’T KNOW WHAT ELSE TO DO!!!"
        h "WHAT IF HE NEVER COMES BACK?! I DON’T WANT TO KEEP BEING ALONE!"
        s "I know. You just want someone to kill the loneliness-"

        scene harukasgoodday20
        with dissolve

        h "That’s not it either!"
        h "Just {i}someone{/i} isn’t good enough! It has to be {i}you!{/i}"
        s "I don’t-"
        h "I wasn’t lying when I told you I needed you! I do! I just...don’t know how!"
        s "..."

        scene harukasgoodday19
        with dissolve

        h "You can hate me if you want! I already hate myself! Just...don’t leave me yet! Not yet! Please!"
        s "..."
        h "PLEASE!!!!!!!!!!"

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene bedroom_night
        with dissolve2

        "Despite her pleas for me to stay, I wound up leaving Haruka."
        "Though, not for good- as I may have contemplated for a moment."
        "My desire to stay can be traced to more than just how sexually compatible we are, though."
        "The truth is that I enjoy being needed. And, for some reason, she’s decided to latch onto me like some sort of sea lamprey, using her teeth to scrape away at what’s left of me so that {i}she{/i} can flourish."
        "Or maybe a leech would be a better-suited metaphor."
        "She’s something grotesque, yet anatomically interesting in the fact that there’s much I’ve left to learn about her body."
        "But, for the moment, I think it’s best if she suffers in silence. "
        "Especially considering those who have it worse."

        $ sadgirls2 = True

    play sound "phonering.mp3"

    s "..."

    play sound "phonebeep.wav"

    s "Hello?"

    "I hear a sigh on the other end of the phone- likely as a result of me answering too quickly and not giving the caller a chance to prepare her opening statement."
    "I wait, as I have a feeling that what comes next will be the handful of sleeping pills I take before bed tonight."

    maki "I..."
    maki "I wanted to say I’m sorry for yelling at you earlier."
    maki "A lot happened."
    maki "A lot that...I’m sure you figured out when you walked into the bathroom."
    s "You don’t have to apologize. I shouldn’t have followed you."
    maki "You were just worried. I understand."
    maki "Telling Miku where we were was a good move, though. She was able to cheer Makoto up a lot better than I was. "
    s "I’m sure that’s not-"
    maki "Listen, uhh..."
    maki "Can we meet up in the morning? Maybe at the cafe? "
    maki "This isn’t really something I should keep you in the dark about."
    s "I don’t really think it’s necessary to get me involved with your family matters."
    maki "It is when my daughter is one of your students."
    maki "Because there’s no way in hell that this isn’t going to have a huge impact how she is in school. And it’s something I need to know you’ll be able to handle."
    s "Then, sure..."
    s "We can meet up."
    maki "Thanks. "
    maki "Anyway, uhh...goodnight, I guess. Not that I’ll be able to sleep much. "
    maki "I just..."
    maki "Yeah."
    maki "I’ll see you tomorrow."

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "Maki hangs up the phone without giving me a chance to say goodnight."
    "But as I climb into bed, it is not her that I think about."
    "It is her daughter."
    "And the fact that she now has no choice but to fall further into me than she already has."
    "So far that even I might lose track of her."

    $ renpy.end_replay()
    stop music fadeout 10.0

    "{i}When you fall asleep, you dream of a bluejay.{/i}"
    "{i}Its beak breaks and you must help it preen its feathers.{/i}"
    "{i}The keratin tastes like the outermost layer of a coconut.{/i}"
    "........."
    "......"
    "..."

    jump sadgirls3

label sadgirls4:
    scene harukaoutdoor1
    with dissolve2

    "Someone who doesn’t seem to have a problem holding {i}anything{/i} in, though, is Haruka- who is currently sharing her recent fortune with a still noticeably confused Rin."
    "At least she’s not the {i}only{/i} one confused."
    "It’s hard enough figuring out how to deal with a woman who lost her husband. Jumping directly from that to a woman who {i}gained{/i} a husband is just more than I can process this early in the morning."
    "But at least it seems like Haruka isn’t diving headfirst into celebration mode based on her current expression."

    if harukasex == True:
        "I’m sure that our talk last night might have something to do with that, though."

    r "But...wait. If {i}your{/i} husband is okay, what about Makoto’s mom’s husband? "
    r "That’s gotta have something to do with-"
    h "That’s...not really something I think I should be discussing with you. I just wanted to give you an update about {i}my{/i} situation since I know you’ve been, uhh...curious about it."

    scene harukaoutdoor2
    with dissolve

    r "Well, I’m really happy for you. That’s great news."

    if harukasex == True:
        scene harukaoutdoor3
        with dissolve

        r "But, uhh...what exactly does that mean for Sensei?"
        h "Ah..."
        h "I thought you were leaving with Maki. I didn’t realize you were right behind me."
        s "Maki went off to meet up with Sara, I think. What’s this about me?"
        r "Just...well..."
        r "Aren’t you two, like...you know..."

        scene harukaoutdoor4
        with dissolve

        r "Actually, I want to keep my job, so I probably shouldn’t say it right now."
        h "That’s not..."
        h "Things are a lot more complicated than that! "
        s "Wouldn’t flat out denying it work a little better here, Haruka?"

        scene harukaoutdoor5
        with dissolve

        h "I can’t deny it when she already knows. "
        h "Besides, I’m not wrong, am I? You told me just last night that my, uhh...circumstances are all messed up. "
        h "Did you change your mind after a night’s sleep? Or were those just words you used back then to try and soothe me?"
        r "You know what? I just remembered that I have dishes to wash. And that this is something you two should probably figure out without me in the picture."
        h "No..."
        h "You need to stay here and watch the store while he and I have an actual conversation. One where I don’t rip my shirt open and try to get him to screw me."

        scene harukaoutdoor6
        with dissolve

        r "On second thought, maybe this {i}is{/i} something I should be involved in? "
        r "You two basically are my second set of adoptive parents anyway.  And my first set never gave me the sex talk because girls can’t get other girls pregnant. "
        h "I’m going to take your {i}father{/i} outside now, Rin. "

        scene harukaoutdoor7
        with dissolve

        r "Okay, Mom. Don’t press your bodies up against the glass when you inevitably go at it. I’m the one who has to clean them."
        h "Noted. "

    else:
        scene harukaoutdoor8
        with dissolve

        r "But, uhh...what exactly does that mean for Sensei?"
        h "Wha-"
        h "I thought you left with Maki? What are you still doing here?"
        s "Maki ran off to go meet up with Sara. What’s all this about me?"

        scene harukaoutdoor9
        with dissolve

        r "Nothing. Nobody here wants to fuck you. {i}Especially{/i} nobody named Haruka."
        h "Are you fucking kidding me right now? Is this really the time for that?"
        r "Time for what? I’m just here to make coffee and keep secrets. "
        r "Besides, just {i}wanting{/i} to do something isn’t a big deal unless you actually do it, right? "
        r "I figured by now that both of you were well aware of the sexual tension and just not giving into it because you knew it would be fucked up."

        scene harukaoutdoor10
        with dissolve

        r "If you ask me, though- I’m on Team Sensei because at least he is {i}here.{/i}"
        h "Okay...I’m going to go outside now so I can have a real conversation with him. And you’re going to stay {i}here{/i} and watch the store so I can do that."

        scene harukaoutdoor11
        with dissolve

        r "Aye aye, Captain Haruka. You two enjoy your fun adult conversation where you pretend you don’t want to bang."
        h "I’m sorry about her."
        s "It’s fine. I’ve come to accept her the way she is and you should too."
        s "Also, it’s not like she’s {i}wrong.{/i} I know for one that I-"
        h "Please don’t finish that sentence. I can already tell that it’s going to do more harm than good."

    scene black
    with dissolve2

    h "Come on. It’ll be easier to talk without the world’s nosiest teenager getting all up in our business."
    r "Hey! I have a {i}cute{/i} nose! Otoha tells me all the time!"

    "Haruka and I exit the cafe, surveying the surroundings to make sure that no one else is around before we begin what will be my second mature conversation of the day."

    if harukasex == True:
        "Or at least what I {i}hope{/i} will be my second mature conversation of the day."
        "Given what happened the {i}last{/i} time Haruka and I tried to talk, I’m not really sure."
    else:
        "Unless Haruka plans on just excitedly freaking out about her husband being alive again. "
        "Which, based on the brief conversation we had yesterday, seems highly probable."
        "It does seem that I’m actually more involved than I thought, though, if what Rin said has any truth to it."
        "Am I involved enough to have Haruka throw everything else away in an effort to chase me down? Of course not."
        "But one good conversation could disconnect our paths entirely. "
        "And that’s probably why she wants to do this."

    scene sky
    with dissolve2

    "The one good thing about today (Not counting Haruka’s husband, since I have never met and couldn’t care any less about the guy) is that, at least thus far, the sun has shown us mercy."
    "It’s still early, though. And life does prove to be inconvenient in more ways than most of us would like to admit. But if it means dodging tragedy in the form of UV rays, I can pretend to be an optimist for a bit."
    "It’ll be good to have {i}one{/i} of us fulfill that role, at least- as the sigh that escapes Haruka’s lips as she slouches against the wall reveals that it certainly won’t be her."
    "And that this change, albeit one much brighter in color than that of her friend, has drastically altered her life out of nowhere."
    "It remains to be seen if it’s what she wants, though."
    "Or if the last several years of being without him have turned her into something she can’t look at anymore."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    if harukasex == True:
        scene harukaoutdoor12
        with dissolve2

        h "I owe you an apology."
        s "You do."
        h "It was way fucked up for me to place the blame on you like that when this was as much of a decision on my end as it was yours."
        h "Actually, scratch that. It was {i}more{/i} of a decision on my end than yours. {i}You’re{/i} not the one hurting anyone else by sleeping with me."
        h "You’re not tied down the same way I am. Or...{i}was.{/i}"
        h "I guess what I’m saying is that I’m the one who loosened the knot my husband and I tied and that you were just...there to lend me a hand."

        scene harukaoutdoor13
        with dissolve

        h "You know...this whole {i}marriage{/i} thing...it wasn’t anything like I expected it to be."
        s "I don’t think most newlyweds anticipate a space war coming in between them."
        h "No, I guess they don’t. But even something like that is something I figured I was prepared for back when we first found out."
        h "I was still so high on the idea of being with someone I was in love with that there was {i}no{/i} amount of time that I wouldn’t wait for them to come back."
        h "But here I am, three years later...still married...yet trying to salvage my relationship with the man I’m regularly cheating on my husband with."
        h "What does that say about me?"
        s "It says that you’re confused. Which most people would be in your position."
        s "I’m not mad about what happened last night. I’m used to dealing with people at their worst, and I’m sure it felt like your life was falling apart."
        s "It was the contrast between that and something else that coerced me into walking away, I think."

        scene harukaoutdoor14
        with dissolve

        h "I can only imagine. "
        h "If I had known back then that Maki’s..."
        s "..."
        h "..."
        h "Why didn’t you tell me?"
        s "Because I already pissed her off once that day. And I didn’t want to go telling people things she didn’t give me the okay to talk about. Especially someone as close to her as you."
        s "I get that there was a lot going through your head when you called me, but Maki’s your best friend. You’re better than that."

        scene harukaoutdoor15
        with dissolve

        h "I’m not, though. "
        h "Everything I’ve done over the last few years has been mistake after mistake. And a good portion of those mistakes have been {i}repeated{/i} mistakes."
        h "Do you have any idea how many times we’ve had sex? Because I don’t. "
        h "What I do know, though, is that every single one of those times was me jamming a knife further and further into my husband’s back."
        h "I honestly wouldn’t be surprised if it was poking out of his abdomen by now."
        s "Can you think of a metaphor a little less gruesome, please?"

        scene harukaoutdoor16
        with dissolve

        h "No."
        h "I deserve the most disgusting and gruesome metaphors my shitty brain can come up with. Anything less wouldn’t be fair."
        s "I still don’t think that what we’ve done is that big of a deal. "

        scene harukaoutdoor17
        with dissolve

        h "No, it {i}is{/i} a big deal! And I really wish you’d stop saying it’s not!"
        h "This is more than me thinking my husband is gone and emotionlessly using the body of some other man to fill the void he left!"
        h "It’s more than me making a little mistake! More than me trying to hide my loneliness the only way I know how!"
        h "It’s the fact that I {i}know{/i} he’s alive now! That I know he has a chance of coming back!"
        h "And that I still want you despite that!"

        scene harukaoutdoor18
        with dissolve

        s "..."
        h "..."
        h "I don’t want to feel this way anymore...like I’m being forced to choose between two things I want when one of them I can’t even {i}have{/i} and the other is an option I didn’t even realize {i}existed{/i} until I already chose."
        h "And no. This isn’t me saying that I’m thinking of separating with my husband and just devoting myself to you instead."
        h "I just..."
        h "I can’t help but think sometimes that something like that might be nice."
        h "Anyway, I’m sorry for yelling at you and...saying all of the fucked up shit that I said...and blaming you and not listening and...anything else you want me to apologize for."
        h "You didn’t deserve it."
        h "So if you want to go off on me for being selfish and neurotic and just an all around shitty person, you can. Because {i}I{/i} deserve that."
        h "If I didn’t, I wouldn’t keep making the same mistakes."
        s "..."
        h "..."

        scene harukaoutdoor19
        with dissolve

        s "I’m not going to go off on you."
        s "I’d just like some sort of warning beforehand if this winds up happening again. Walking all the way over there just to get yelled at for your shitty behavior kind of sucked."

        scene harukaoutdoor20
        with dissolve

        h "You’re...{i}still{/i} going to come over?"
        s "Well, {i}somebody’s{/i} gotta fuck you, right?"
        h "That’s...That wasn’t really the point I was trying to-"
        s "I know it wasn’t the point you were trying to make."
        s "It’s just easier to talk about it like that."
        h "..."
        s "..."

    else:
        scene harukaoutdoor21
        with dissolve

        h "So, umm..."
        h "Can we avoid the part about the sexual tension? Or is that a thing we actually have to address?"
        s "We can avoid it. I’m just a little upset since I was starting to think you were calling me out here to confess."

        scene harukaoutdoor22
        with dissolve

        h "Ahh, yes. What better time to confess than the 24 hours following the revelation that your husband is still alive?"
        s "Jokes aside, if you didn’t call me out here to talk about that...why {i}did{/i} you call me out here?"

        scene harukaoutdoor23
        with dissolve

        h "To thank you."
        s "Me? For what?"
        h "For also feeling that tension and never giving into it."
        s "I thought we weren’t going to-"
        h "We’re not. It’s...something much bigger than {i}just{/i} that. "
        h "It’s something that’s been an unavoidable part of who I am for years now...a part that I never figured out how to address until meeting {i}you{/i} brought on a whole bunch of new challenges."
        h "You can say it’s due to an overwhelming lack of men or something like that..."
        h "But you are the exact sort of temptation I have always feared I’d face."
        h "I get lonely very easily. I’m sure you know that much about me by now. And it’s that sort of loneliness that makes me think things I shouldn’t sometimes."
        h "And maybe it’s like Rin said. Maybe just thinking things and never actually {i}doing{/i} them is fine...but it sure as shit doesn’t feel that way."
        h "Having you around...made me think a bunch of things all the time. Things that seemed like magic in the moment, but tapeworms once the moment faded."
        h "I found myself trying to appeal to you without even realizing it. "
        h "Unbuttoning my blouse when you walk into the store...{i}forgetting{/i} my wedding ring at home so it would look like I wasn’t committed."
        h "And, honestly...if you’d have pursued something with me...I really think I would have let those compulsions of mine win."

        scene harukaoutdoor24
        with dissolve

        h "But you didn’t."
        h "And sure, you might joke about how you’d be completely fine with throwing all of that away and starting an actual affair with me-"
        h "But you’re the one who held back when I was ready to bend."
        h "{i}That{/i} is why I wanted to thank you."
        h "You protected me from myself when I’ve always been my own worst enemy."
        h "I don’t know if you did it {i}to{/i} protect me...or if you had some other sort of motive in mind...or even if you’re just flat out unattracted to me."
        h "But whatever reason it was that we became what we are today instead of what I fantasized about..."
        h "I’m thankful for that reason."
        h "I’m thankful for you."
        h "And I seriously can’t thank you enough."
        s "..."

        scene harukaoutdoor25
        with dissolve

        h "I feel like I’m going to stop forgetting my ring as much when I leave the house now."
        h "There’s not really anyone I feel the need to appeal to like that anymore."
        h "Because, thanks to a certain close friend of mine, I now understand that there’s more than one way to dispel loneliness."
        h "That there are plenty of ways to feel full without being filled up."
        h "Because at the end of the day...what I already have should be enough for me."
        h "And that reaching for any more would just be greedy."
        s "..."
        h "..."
        s "Want to make out?"
        h "Nope."

        scene harukaoutdoor26
        with dissolve

        s "Wow. You really have turned over a new leaf."
        s "Back in the beginning, you’d just make out with me without even asking."
        h "Okay, first off, that only happened one time and I was extremely drunk."
        h "Second, I’m still kind of upset about it. So don’t joke like that."
        h "Third, do you even {i}want{/i} to make out with me? Or do you just feel weird that I forced you into a sentimental conversation when your biggest goal in life is to avoid those?"
        s "Yes and yes. "
        h "Well, too bad. Because a phone call I received yesterday has reminded me of just how long I am willing to wait."
        h "And no handsome man with a well-defined body and mysterious aura will change that."
        s "If only I was less mysterious."

        scene harukaoutdoor27
        with dissolve

        h "Yes. If only."

    "A moment of silence washes over the two of us as the streets finally begin to fill with people."
    "But seeing as we’ve already passed the points of our conversation that demand secrecy, I don’t see much of an issue with it."
    "To anyone who passes by, we probably just look like lovers."
    "Ironically enough, that’s the one thing we’ll never be."
    "Haruka’s heart belongs to someone else."

    if harukasex == True:
        "I’m just the man who took it."
    else:
        "And it’s not as if I’d take it anyway."

    scene harukaoutdoor25
    with dissolve

    h "Anyway..."
    h "I guess it’s about time we head back in. "
    h "All those people on the street will soon remember they need coffee in order to survive and then turn to me in desperation."
    s "You’re going to stay here?"

    scene harukaoutdoor28
    with dissolve

    h "I mean...yeah. That {i}is{/i} my job."
    s "I just figured you might want to go spend time with Maki or something since she’s already on her way to the bar."
    s "She hasn’t shown any weakness to {i}me{/i} yet, but I’m pretty sure that brave facade she’s putting on won’t last nearly as long as she wants it to."
    s "Having another friend around might be good for her."
    h "I..."
    h "I didn’t realize you cared so much about her."
    s "Who says {i}she’s{/i} the one I care about?"
    h "..."
    s "..."

    scene harukaoutdoor29
    with dissolve

    h "Ahh..."
    s "..."
    h "I’d have to call Molly in."
    h "Do you think she and Rin will be able to get along for the rest of the day? Or are they still on bad terms?"
    s "Beats me. There’s only one way to find out, isn’t there?"
    h "I guess so..."
    h "Here’s hoping I still have a cafe to return to tomorrow."

    scene black
    with dissolve2

    "I leave Haruka’s side and blend in with the crowd as I begin to ponder over what else I can possibly do today."
    "I toy with the idea of showing up to the bar as well, but..."
    "I think that whatever is going on there would probably be best left between the girls."
    "I don’t belong anywhere with that level of uninhibited emotion."
    "Where I do belong is amidst a sea of faceless others, each focusing solely on where the day will bring them."
    "Paying no mind to me."
    "So to anyone who passes by, ignore me."
    "I’ll figure out where to go on my own."
    "Just focus on yourself."
    "Find your own way home."

    $ renpy.end_replay()
    $ sadgirls4 = True
    $ haruka_love += 1

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    jump sadgirls5

label sadgirls5:
    scene harukaandco1
    with dissolve2

    h "Hah..."
    r "How’d it go? Were you able to say everything you wanted to say?"
    h "Who knows? I think it went well, but I’m notoriously bad at judging how things are going while they’re actually, you know, {i}happening.{/i}"

    scene harukaandco2
    with dissolve

    r "Well, you’re not alone there. I think Otoha’s mad at me since I didn’t talk Chika out of joining the light music club with us."
    h "You left the manga club? It’s not because of the whole Molly thing, is it?"
    r "No. That doesn’t really have anything to do with it."
    h "Okay. Good. Because I’m calling her in and the two of you are going to be running the rest of the shift together."

    scene harukaandco3
    with dissolve

    r "I’m sorry, what?"
    h "Think you can deal with each other long enough to keep the cafe from burning down?"
    r "Haruka, you understand that leaving me alone to run the shift with Molly means that I’m {i}basically{/i} going to be running things alone, right?"
    h "Yeah. But I trust you and think you can handle it."

    scene harukaandco4
    with dissolve

    r "Oh, you’re {i}good.{/i} You know I won’t be able to say no after flattery like that."
    r "Fuck it. Bring on the weeb. I got this shit."
    h "Thanks, Rin. I appreciate that."

    scene harukaandco5
    with dissolve

    r "What are {i}you{/i} gonna do, then? Go meet up with Makoto’s mom? Or are you gonna go back home and try to erase all the traces of Sensei for when your husband comes back?"
    h "I still have no idea when my husband will be coming back, nor do I understand what “traces” Sensei would even leave behind."
    r "Oh, you know. Condoms. Razors. All kinds of...manly stuff. Whatever dudes carry around with them."

    if harukasex == False:
        scene harukaandco6
        with dissolve

        h "He has no need for condoms when that’s absolutely not the type of relationship we have."
        r "Hey, I didn’t say they had to be for {i}you.{/i} He’s a popular guy, you know? He could be slamming some girl he just met on the street right now and we’d have no idea."
        r "I just hope he didn’t leave all his condoms at your house."
        h "Rin."

    else:
        scene harukaandco6
        with dissolve

        h "You know, I’d really appreciate it if you’d stop pointing out my infidelity now that my husband has come back into the picture."
        r "Why? If your heart’s with Sensei, what good does waiting on him even do?"
        h "Rin-"
        r "I’m serious, Haruka."
        r "I love you and want you to be happy. And I feel like you’ll be making a big mistake if you just cut everything off because of one phone call."

        scene harukaandco7
        with dissolve

        h "You should know by now that this isn’t something I can just {i}cut off.{/i} It’s a lot more complicated than that."
        r "Well, whatever the case may be, I’d like to reinforce my role on Team Sensei. And no, it’s not just because I want to watch you guys do it."
        r "Which I might."
        r "I mean, what? Who said that?"
        r "Don’t fire me."
        h "Rin...stop."

    scene harukaandco8
    with dissolve

    r "So, what now? How are you gonna kick off your girls’ day out on the town?"
    h "We’re not going {i}out on the town.{/i} And frankly, I’d be surprised if Maki even {i}would{/i} go out on the town with me after how I treated her yesterday."
    r "Well, it’s not like you meant to treat her that way, is it? You had your own stuff going on. It’s only natural to think about that first."
    r "As long as you can apologize and be sincere about it, I’m sure you guys can work it out."
    h "Yeah...I’m just not really sure how to apologize for something as serious as this. Especially when she’s going through one of the hardest things she’ll ever have to right now."

    scene harukaandco9
    with dissolve

    r "Yeah...after starting to piece things together, I can kinda see that..."
    r "I wish I had some sort of advice I could give you...but I’ve never really been good at dealing with that sort of thing myself either and-"

    scene harukaandco10
    with dissolve

    r "Wait! What about flowers?"
    h "Flowers?"
    r "Yeah! "
    r "Any time my mom gets into a fight with my {i}other{/i} mom, she always buys her flowers to say she’s sorry. Then, before you know it, they’re back to normal like there was never any fight at all."
    r "This might not work since you and Maki don’t have sex with each other, but I think it’s worth a shot!"
    h "Who says Maki and I don’t have sex with each other?"
    r "..."
    r "Come again?"

    scene harukaandco11
    with dissolve

    h "Kidding."
    h "But...yeah. Maybe a gesture like that {i}would{/i} make things a little bit better. Thanks for the suggestion, Rin."
    r "..."
    r "Were you really kidding just now? And, if so, can you tell me you {i}weren’t?{/i}"
    h "Nope. I’ve got things to do. "

    scene harukaandco12
    with dissolve
    stop music fadeout 15.0

    h "I’ll call Molly now and make sure she comes over, but I’m going to head out if that’s okay with you. You’ll be fine alone for a little while, right?"
    r "..."
    h "Rin?"
    r "..."
    h "..."
    h "Okay. See you later, then."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Somewhere else, shortly after....{/i}"

    scene harukaandco13
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "{i}Flowers, flowers, all around us; to grow and then decay-{/i}"
    "{i}To parallel our livelihoods and mirror passing days.{/i}"
    "{i}When you speak into that mirror, what is it you will say?{/i}"
    "{i}Are you excited for the future? Or do you wish it all away?{/i}"
    "{i}To heart, my friends and family! For these mirrors are just jokes!{/i}"
    "{i}The flowers reek of simile! The metaphors of oak!{/i}"
    "{i}Reverse! Return! Repeat your words! If you keep them in, you’ll choke.{/i}"
    "{i}Press the flowers to your nose; breathe them in like smoke.{/i}"
    "{i}- The girl who cannot breathe{/i}"

    "Hello!"
    "Narrator here again."
    "Did you miss me?"
    "I’ve decided to drop in and speak to you directly about what might be happening while you’re away."
    "It’s come up in the past — the question of trees falling in forests and whether or not they make sounds — and I’d like to confirm here and now that they do!"
    "The issue is that the sounds happen so far away from all of us that’s it’s kind of hard to pinpoint exactly {i}what{/i} noises are produced."
    "So all we have to go off of are past experiences. Memories of what sounds {i}should{/i} be made and how long they will last."
    "Perhaps what you will see next is one of those assumptions. "
    "Or perhaps I just like playing games with you."
    "Does it happen?"
    "Does it not?"
    "You will never know!"
    "But I will."
    "And you are lucky that I am willing to share even this much."
    "Sayonara."

    h "Let’s see...I think flowers should be-"
    q "You! With the boobs! Come here!"

    scene harukaandco14
    with dissolve

    h "Huh? Me?"
    q "Yes! You! Help me!"
    h "Umm..."
    q "Hurry! This is an emergency! My entire life hangs in the balance of this very decision!"

    scene harukaandco15
    with fade

    h "How can I-"
    q "Pink or blue?!"
    h "Uhh...can I ask what the occasion is?"
    q "Repentance!"
    h "I think I need a little more to go off of than just that."

    scene harukaandco16
    with dissolve

    q "I think pink is probably the right choice. Blue comes on too strong. Pink is like “Please forgive me,” while blue is like “I’m fucking sorry, okay?” "
    h "Umm..."

    scene harukaandco17
    with dissolve

    q "Here. Take these. I have made my decision and you look like you’re here for flowers as well."
    h "Is that...really how I-"

    scene harukaandco18
    with dissolve

    q "..."
    h "Well, I guess I don’t have to {i}look{/i} for flowers anymore."
    q "Mmm...I don’t know about this. I’m starting to have second thoughts about pink. "
    q "You know, this whole ordeal would be a hell of a lot easier if they had yellow. I always get yellow. This is the first time I have ever been faced with such a tough decision."

    scene harukaandco19
    with dissolve

    q "Also, hi. Nice to meet you. I swear I’m not normally as crazy as this. You just caught me at a weird time."

    scene harukaandco20
    with dissolve

    h "Oh, it’s fine. This is nothing compared to one of the girls I have to deal with pretty much every day."
    q "You have kids?"
    h "Me? No way. Just a bunch of part timers at a cafe I own about a mile away from here. "

    scene harukaandco21
    with dissolve

    q "Cafe?"
    h "Uhh...yeah. Like...you know. A place that serves coffee?"
    q "Dude, I know what a cafe is. I was just thinking that’s a crazy coincidence since my daughter also works at a cafe about a mile away from here. "
    q "I’m not allowed to go there, though. She says I’ll embarrass her. But I don’t seem that embarrassing, do I?"
    h "Um...just out of curiosity, your daughter wouldn’t happen to be-"

    scene harukaandco22
    with dissolve

    q "Interested in coming to work for you instead? No way. She loves her job. Even {i}if{/i} I’m not allowed to go there. But nice try, random rival cafe lady. "
    h "What? No, I-"
    q "Anyway, it was nice talking to you! Hope that whoever you’re giving those flowers to likes the color blue and how aggressively apologetic it is!"

    scene harukaandco23
    with dissolve

    q "Oh! And if you need a card as well, they’re to the right of the check-out counter!"
    q "If you bend all the corners, they’ll even give you a discount!"

    play sound "entrybell.mp3"

    q "Anyway, bye! Time to go salvage my love life!"
    storec "Wait, miss. You still have to pay for-"
    q "Sorry, can’t talk right now! Keep the change!"
    storec "...those."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Roughly one hour later, in a room less joyous.{/i}"

    scene harukaandco24
    with dissolve2

    "I have no poem nor words of consolation for you this time."
    "Just a glimpse into what may or may not be happening behind your back."
    "And how things can be painful even without you."
    "Sometimes, a tree falls so hard that it can be heard from miles away."
    "And other times-"
    "It’s like an entire forest has collapsed."

    maki "{b}FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK!!!!!!!!!!!!{/b}"
    maki "FUCK FUCK FUCK FUCK FUCK! WHY US?! AM I NOT STRUGGLING ENOUGH ALREADY?! I NEED TO STRUGGLE {i}MORE?!{/i}"
    sar "Hey...you’re going to be okay. You’ve been doing great without him. Much better than me, at least."
    maki "I DON’T WANT TO DO IT WITHOUT HIM, SARA! I DON’T WANT TO DO THIS ALONE!"
    maki "I LOVED HIM! I {i}STILL{/i} LOVE HIM! AND NOW HE’S FUCKING GONE! JUST LIKE THAT! WITHOUT EVEN SAYING ANYTHING!"
    maki "DO YOU HAVE ANY IDEA WHAT THE LAST THING I SAID TO HIM WAS?! DO YOU?!"
    sar "Maki..."
    maki "Here! I’ll tell you! It was “Don’t fuck too many aliens!”"
    maki "{i}That{/i} was the last thing I ever said to him! And I can’t take that back!"
    maki "I never thought something like this would happen, Sara! I never realized how cruel and unfair life can be! "

    scene harukaandco25
    with dissolve

    sar "I know...I know..."
    sar "It really is cruel, isn’t it?..."
    sar "How we never realize how close to the end things are..."

    play sound "static.mp3"
    scene harukaandco26
    with flash
    stop sound

    maki "THAT FUCKING IDIOT!"
    maki "WHY DID HE TELL ME EVERYTHING WOULD BE FINE?! WHY DID I BELIEVE HIM?!"
    maki "THIS ISN’T FINE AT ALL! THAT FUCKING MORON! ASSHOLE! UNGRATEFUL BASTARD!"
    maki "FUCKING...DOUCHEBAG! WORTHLESS PIECE OF SHIT! HOW COULD YOU FUCKING DO THIS TO US?!"
    sar "That’s right...let it all out..."
    sar "It’s okay to cry here..."

    scene harukaandco27
    with dissolve

    maki "WAAAAAAAAAAAAAAAAAaaAaAAAAaaaaaahhh!!!!!!!!!!!!!"
    maki "MASAHIRO!!! YOU FUCKING ASSHOLE!!! HOW COULD YOU?!?! HOW COULD YOU?!?!?!?!?!"
    h "Maki...why did you hold this in for so long?"
    maki "HOW THE FUCK WOULD YOU KNOW HOW LONG I’VE HELD IT IN, HARUKA?!"
    maki "WHILE YOU WERE BUSY CELEBRATING, I WAS BREAKING THE NEWS TO MY BABY GIRL THAT THE MAN SHE'S LOOKED UP TO SINCE SHE WAS LITTLE IS NEVER COMING HOME!"
    h "I’m not here to make excuses. Not being there for you was horrible of me. But you’ve always been the type to hold things in until they don’t fit anymore and-"
    maki "THIS IS DIFFERENT! "
    maki "I {i}HAVE{/i} TO DO THAT NOW! IT’S NOT A CHOICE ANYMORE!"
    maki "I’M A SINGLE FUCKING PARENT NOW! I HAVE TO BE STRONG! "
    maki "I CAN’T JUST FUCK AROUND ANYMORE! SOMEONE ELSE’S FEELINGS ARE AT STAKE!"
    h "I’m not saying you should fuck around...I’m saying that your daughter is smart enough to realize you’re hurting too and-"

    play sound "static.mp3"
    scene sadflash1 with flash
    scene sadflash2 with flash
    scene sadflash3 with flash
    scene harukaandco28 with flash
    play sound "slap.mp3"
    with hpunch

    maki "STOP TALKING TO ME LIKE YOU UNDERSTAND WHAT’S GOING ON! STOP TALKING LIKE YOU UNDERSTAND HOW I FEEL!"
    sar "Maki! She was just trying to-"
    maki "SHE SHOULD HAVE BEEN THERE! SHE SHOULD HAVE BEEN THERE FOR ME!"

    scene harukaandco29
    with dissolve

    maki "How many times have you called me to cry about your problems?! How many times have I sat there listening to them?! Consoling you for things you shouldn’t even have to be consoled for!"
    maki "Your husband is still alive and mine has been dead for two fucking months! Two months, Haruka!"
    maki "My daughter lost her father and you didn’t even come over to see how we were doing!"
    h "I called-"
    maki "ONE FUCKING TIME!"
    maki "YOU CALLED ONE TIME!"

    scene harukaandco30
    with dissolve

    maki "Is that seriously all I’m worth to you?"
    maki "Did you think you could just fucking show up here with {i}flowers{/i} in your hand and make it all okay? "

    scene harukaandco31
    with dissolve

    maki "Don’t tell me I shouldn’t be holding things in when letting them out makes the whole world fucking implode."
    maki "And don’t pity me either. Because the idea of someone who can’t handle her own problems telling me how to handle {i}mine{/i} is just insulting."
    sar "She doesn’t mean that, Haru-chan...She doesn’t."
    maki "It’s not fair."
    maki "It’s just not fair."
    maki "Why couldn’t my husband live too?"
    maki "Why couldn’t I have gotten the same call you did?"

    scene harukaandco32
    with dissolve

    h "Because I’m lucky...theres nothing more to it than that."
    h "If the outcome of our phone calls was based on who we are as people or how decent we’ve been to each other...I know our positions would be swapped right now."
    h "And I know that you would have been the first one to get in contact with me."
    h "I wasn’t, and I’m sorry for that. I’ll be sorry for it for the rest of my life."
    h "What I won’t do is give up on telling you when I think you’re making things harder for yourself than they have to be."
    h "No one’s expecting you to hold yourself together, and I’m sure that includes your daughter."

    scene harukaandco33
    with dissolve

    h "Also, I didn’t buy you these flowers to try and make everything okay. I bought them because I think you deserve something nice now that everything else has been taken away from you."
    h "And also because I was pressured into it by some woman in the convenience store who may or may not be the mother of one of my employees."
    h "The point is, I wasn’t there for you when I should have been. "
    h "But I’m here now, asking for forgiveness when I know I don’t deserve it because beneath the selfishness and inability to look forward, I love you."

    scene harukaandco34
    with dissolve

    maki "Haruka, I...I didn’t mean to hit you. I’m just..."
    maki "It really hurts..."
    maki "I’ve never felt so alone before..."
    h "Sara, can you take these flowers from me for a second?"
    sar "Huh?...Sure, but..."

    scene harukaandco35
    with dissolve

    h "Come here."
    h "I don’t care that you hit me, Maki. It’s not a big deal."
    maki "You’re...{i}sniff...{/i}only saying that because...{i}sniff...{/i}you like it rough..."
    h "No. I’m saying that because after all of the times you’ve been there for me, the least I can do to make it up to you is let you knock me around a little bit."
    maki "Just...{i}sniff...{/i}be there for {i}me.{/i} That’s all I want..."
    h "I will. I promise. "
    h "But in the meantime, cry as much as you want. I took the day off to spend it with you. And if that means becoming a handkerchief, so be it."
    h "Also, I hope that you’re okay with blue. The girl at the convenience store said it might be too “aggressively apologetic.”"
    maki "{i}Sniff...{/i}"
    maki "Blue is my favorite color..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene bedroom_night
    with dissolve2

    "Again, I can’t recall where the day went."
    "After leaving the cafe, I wandered the streets...half-expecting to bump into a girl fighting a war with herself behind the scenes, trying to reclaim what little sense of dignity I haven’t already robbed her of."
    "The fact that I didn’t find her at all speaks volumes about the shape she must be in right now."
    "But at least she’s not alone in her misery- for even further behind the curtain are two more girls. "
    "They both wear glasses. Both have blue eyes. And they both just lost a man who, even in death, will remain far more important to them than I ever will."
    "Which is why I’m not with them right now."
    "Sometimes, it’s necessary to settle for second place."
    "It’s necessary to detach yourself from things you became unintentionally glued to."
    "To slip out of your skin...and wander deep into the darkness, for that’s the only place you won’t be able to hurt anyone."

    scene black
    stop music

    "But sometimes, the ones you fear hurting find {i}you.{/i}"
    "Because, contrary to what you may believe-"
    "You are never truly alone in the dark."
    "{i}In the bowels of the night, unconscious as you are, you swallow a spider.{/i}"
    "{i}You awaken with a mouth full of eggs.{/i}"

    $ renpy.end_replay()
    $ sadgirls5 = True

    play sound "static.mp3"
    scene spider1 with flash
    scene spider2 with flash
    scene spider3 with flash
    scene spider4 with flash
    stop sound
    jump sadgirls6

label harukalust25intro:
    scene surprisebjcontest1
    with dissolve2
    play music "acoustic.mp3"

    ima "Okay! All set. "
    s "I have several questions."
    ima "No. I will {i}not{/i} let you try on my earrings. "
    s "That...is not one of them. "
    ima "Then either ask them now or be forced to listen to me inaccurately guess what they may be for the rest of the night."
    s "Question one: why are the Kanda sisters behind the counter?"
    ka "You know, I really wish I had an answer to that."
    ki "I do. Karin’s annoying need to always ensure that everything goes well kicked in when we walked into the hotel and she realized there wasn’t a receptionist working. "
    ki "It’s the same thing that happened last year. Tell her to go take a fucking break or something."
    ka "It’s fine. I think I just work here now. It’s sad that I’ll have to quit my clubs, though. But alas."
    s "Question two: why are you holding only one key?"
    ima "Because I didn’t realize you were coming and we only have three rooms. Which means that floor one is in one room, floor two is in the other, and you and me are in the third."

    scene surprisebjcontest2
    with dissolve

    ki "I’d be happy to come stay with you guys as well if-"
    ima "Absolutely not. Go away. "

    scene surprisebjcontest3
    with dissolve

    ka "It’s best to let the adults just have their own room, Kirin. "
    ki "Yeah, best for {i}them.{/i} How come nobody ever cares about what {i}I{/i} want?"
    ka "Don’t worry. As the senior customer relations manager for this hotel, I’ve made sure that Sensei and Imani received a room with two beds."
    ka "I’ve also contacted the custodial staff for a privacy curtain so they will not have to look at each other at any point and we will all go home happy and chaste."
    ki "Talk about an oxymoron."
    ima "Any more questions, Senpai? Or are you ready to go be happy and chaste?"
    s "Talk about an oxymoron."

    scene surprisebjcontest4
    with dissolve

    ki "At least you understand me."
    s "I only have one more question. Does Ami know?"
    ima "She will if we hang around here any longer. Or if Kirin decides to run her mouth or something."
    s "Of course Kirin is going to run her mouth. That’s what she does."
    ki "Hey. I can do other stuff with my mouth too. Talking isn’t {i}all{/i} I’m good for."

    scene black
    with dissolve

    s "Okay, yeah. Let’s go. I feel like I might accidentally invite her if we stay here any longer and I don’t think you’d be into that."
    ima "Woo! Sleepover with Senpai! Sure hope he can’t make out the silhouette of my bodacious body through the privacy curtain!"
    s "I don’t think “bodacious” is the right adjective to-"
    ima "One more word and you’re sleeping on the floor. I don’t even care if there are two beds."

    "........."
    "......"
    "..."

    scene surprisebjcontest5
    with dissolve2

    s "Are you sure you’re okay with this?"
    ima "Why wouldn’t I be? You gonna try making a move on me in the middle of the night?"
    s "Beats me. You’ve slept at my house before and I was able to abstain then. Guess we’ll find out soon if a curtain is enough to keep these burning passions of mine at bay."
    ima "So long as those burning passions don’t wreck the hotel room. I don’t want to risk Touka’s mom seeing that one of the security deposits wasn’t refunded."
    s "Yeah, because if there’s anything we know about Tsubasa, it’s that she’s extremely frugal with her money."
    ima "All I’m saying is that, A: you don’t get rich by wasting security deposits. And B: I like it gentle."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "We manage to make it to our room without anyone other than the Kandas seeing us, but it’s clear that most of the girls are still awake judging from the laughter and chatter bleeding through their doors."
    "I imagine that word will soon spread about my presence in this hotel and that Imani may potentially be assassinated before the night ends. "
    "So if I am going to have sex with her before she dies, I should probably hurry and get to that as soon as we step inside."
    "........."
    "......"
    "..."

    if saralust20 == True and haruka_lust >= 25 and sara_lust >= 25:
        jump harukalust25
    else:
        scene surprisebjcontest6
        with dissolve2

        ima "..."
        s "..."
        ima "Senpai."
        s "What?"

        scene surprisebjcontest7
        with fade

        ima "It appears that we’ve been assaulted by the cliche “one bed” trope."
        s "Assaulted? More like blessed."
        ima "Oh, look. Free slippers."
        s "There are more exciting things to be discussing than free slippers, Imani."
        ima "And a few major problems, too. Karin’s sure to be demoted for this."

        scene surprisebjcontest8
        with fade

        s "So...now what?"
        ima "Isn’t it the man who’s supposed to take charge at times like this? Come hither, vile fiend."
        s "Nice. Nothing gets me in the mood quite like archaic language."
        ima "Nothing gets {i}me{/i} in the mood quite like the feeling of somebody secretly watching my every move."
        s "I didn’t realize you were an exhibitionist."
        ima "Just wait until you see my sex tape. That’ll teach you more about me than any hotel banter ever could."
        a "Where can I find it?"

        scene surprisebjcontest9
        with dissolve

        ima "I’ve got it posted on my LinkedIn just in case I need it for professional reasons. Send me a contact request and I’ll forward it to you at my earliest convenience."
        ima "My rates are low and I’m always looking for work."
        s "How long have you been standing there?"

        scene surprisebjcontest10
        with dissolve

        a "Did you really think I was going to just let you and Imani sleep together? The reason I begged you to come to the hotel was so you could sleep with {i}me.{/i}"
        ima "That doesn’t sound very kosher."
        s "She means it in the wholesome way."
        ima "In {i}that{/i} costume? I ain’t buying it. I’ve seen more of Ami’s legs today than I thought I ever would. And Tsuneyo wasn’t lying when she said they’re great."

        scene surprisebjcontest11
        with dissolve

        a "{i}Miss Imai,{/i} would you please accompany me to the first floor girls’ hotel room? We’ve cleared out a spot on the floor for you to sleep."
        ima "Hah..."
        ima "Guess I’ll have to buy my own slippers after all."

        scene black
        with dissolve2

        "Ami escorts Imani away from what seemed like it was going to be a good opportunity for the two of us to finally “take the dive” before returning on her own several minutes later."
        "Unfortunately for her, the rest of the class united in the decision to keep {i}her{/i} out of my room shortly after that and, before I know it, {i}she{/i} is being escorted out of the room as well."
        "As such, I wind up getting dressed and climbing into bed alone."
        "But I dream of a future in which that didn’t happen."

        stop music

        "It’s a dream much happier than that of the night before."

        $ harukalust25skip = True
        $ imani_love += 1

        "{i}Imani’s affection has increased to [imani_love]!{/i}"
        "........."
        "......"
        "..."

        jump dormwartwo10

label harukalust25:
    scene surprisebjcontest12
    with dissolve2

    saraharuka "Welcome back! You’ve kept us waiting far too-"

    scene surprisebjcontest13
    with dissolve

    saraharuka "Ah."

    scene surprisebjcontest14
    with fade

    ima "..."
    s "Hah..."

    scene surprisebjcontest15
    with dissolve

    ima "Knock ‘em dead, champ."
    ima "I’ll go sleep in one of the other rooms. Looks like there’s only one bed in here anyway, so I’m gonna go get Karin fired."
    s "Thanks, Imani. I’ll owe you one."
    ima "One what? A threesome? Because this is like the tenth one you’ve left me out of and I’m starting to take it personally."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene surprisebjcontest16
    with dissolve2

    sar "..."
    h "..."
    s "Is there something you two would like to say?"
    sar "Um..."
    sar "Take your pants off?"
    h "Were you and that girl...you know."
    s "No. Well, probably not. Maybe. I have no idea. She’s weird."
    sar "Your pants are still on."
    s "How did you two even get in here? I was literally with Imani when she picked up the key."
    sar "I have experience with picking locks."
    s "Why?"
    sar "Because I thought it might come in handy if I ever had to sneak into my daughter’s teacher’s hotel room to compete in a blowjob contest against my best friend."
    h "Hi. I’m that best friend."
    s "Taking Sana’s defeat that hard, huh?"

    scene surprisebjcontest17
    with dissolve

    sar "It is up to me, her mother, to redeem her in the name of the first floor! At least one Sakakibara must prevail!"
    h "I’m just along for the ride."
    h "And also because both this contest and Halloween have had a profound impact on my state of arousal."
    s "And...you’re sure you’re okay with that? Given...certain information that has been revealed to you recently?"

    scene surprisebjcontest18
    with dissolve

    h "Let’s not talk about that."
    sar "It’s not too late to back down, Haru-chan. You know I won’t hold either decision against you."

    scene surprisebjcontest19
    with dissolve

    h "I’ve already fucked up {i}once{/i} the last time we did something like this."

    "Right. {i}Just once.{/i}"
    "Keep her in the dark so you can steal more of the light for yourself, Haruka."
    "Things like that never backfire on anyone."

    h "And since there’s no way of redeeming myself...what’s even the point in trying?"
    h "I’ve thought a lot about it and all that really matters to me right now is {i}my{/i} happiness."
    h "It doesn’t matter if I’m not a good person. If I’m an unfaithful bitch of a wife...as long as I’m happy."
    sar "Didn’t we agree to no more insults after our last...joint sexy-time adventure?"

    scene surprisebjcontest20
    with dissolve

    h "Yeah...we did. But I guess I didn’t realize that pertained to my endless need to self-deprecate, so...whoops."
    s "That was barely a {i}joint{/i} adventure, considering I spent all of my attention on {i}you{/i} that night, Sara."
    sar "Of course you did. You’re my {i}not-{/i}boyfriend and Haru-chan is just a very good friend that I invited to watch us have sex because I'm such a good and generous person."
    sar "But, for the sake of the competition, and also because I’d feel bad making her just watch again...I’m giving everybody a free pass to do anything they want without fear of jealousy or consequences tonight."
    s "Meaning..."
    sar "Meaning I won’t hold it against you when you fuck her mouth in front of me because it’s {i}all{/i} in the name of sport!"
    s "I suddenly like sports."
    h "There obviously has to be a winner, though. And we wanted to make this an officially sanctioned contest so the points would count for the Dorm War-"
    sar "So we took it up with Makoto and found out we just had to fill out some form through the Dorm Wars app!"
    s "You...told Makoto you two were going to have a bonus blowjob contest?"
    sar "Well, obviously without the blowjob part."
    h "We just told her we wanted to have some sort of bonus...rematch round thing in your hotel room tonight if you showed up."
    s "Oh, great. I’m sure she wasn’t able to put two and two together with that at all."
    sar "So what if that’s what she thinks? She’s not here right now and {i}we{/i} are. And I have to prove to Haru-chan that I’m the cock-sucking queen."
    h "And I..."

    scene surprisebjcontest21
    with dissolve

    h "I honestly can’t even remember the last time I did something like this."
    sar "Heheh...looks like Sana will be redeemed after all."
    s "Yeah, I’m sure she’ll {i}love{/i} the idea of extra points that come from her mother performing sexual acts on her teacher."

    scene surprisebjcontest22
    with dissolve

    sar "Of course she will. Because one day, many years from now, she’ll be performing sexual acts on {i}her{/i} daughter’s teacher while {i}we’ll{/i} be busy having hardcore sex in a fancy resort somewhere."
    h "If your libido is still going strong by then, I’ll be extremely impressed."
    sar "It only strengthens with age, Haru-chan."
    h "Yeah...it definitely feels that way sometimes..."

    scene black
    with dissolve2

    "The two of them come closer to me and, like it’s some sort of choreographed dance, begin to run their hands all over my body, slowly guiding me closer to the bed."
    "They give me a push once the mattress touches the back of my knees, causing me to fall on my back as they climb on beside me and reach for my belt."

    play sound "zipper.mp3"

    "Haruka unfastens it, sliding it out of the loops and tossing it across the room while Sara pulls down my zipper and slides one of her hands into my pants."
    "I guess she’s eager to get started as she seizes the opportunity to begin jerking me off as Haruka proceeds to undress me."
    "Once I’m hard enough (Which, admittedly, doesn’t take very long), they organize themselves on both sides of me, bringing their faces just inches away from my shaft and close enough for me to feel their breath."

    scene surprisebjcontest23
    with dissolve2

    sar "You know how this works, right?"
    s "Yeah. I played for the varsity team in my high school’s competitive blowjob club."
    sar "Great. So you’re familiar with the urethral insertion part of the contest then, right?"
    s "Unhand me right now. I’m going home."
    h "Relax. It only hurts for the first few hours."
    s "I will actually kill you."
    sar "We’re kidding, obviously."
    sar "All you have to do is lay there and let us show you what we can do."
    sar "Then, when you’re ready to cum-"

    scene surprisebjcontest24
    with dissolve

    h "Grab the back of one of our heads and fuck our mouth until it's full of Sensei juice! Whoever gets to swallow is the winner!"
    sar "I’m liking the enthusiasm, Haru-chan! It’ll soften the {i}blow{/i} when I put you to shame in a few seconds."
    h "As if I’d let Molly’s victory be cancelled out so easily."
    h "I might not be as practiced as Sara, but I’ll show you that experience isn’t everything."

    scene surprisebjcontest25
    with dissolve

    sar "Are you ready, then?"
    s "I’ve been ready this whole time. Just do it already."
    sar "Your wish is my command, [saramaster]."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene surprisebjcontest26
    with dissolve2

    "Sara kicks the contest off by gently lathering the head of my dick with her saliva, softly tugging at my shaft as she lets out brief and quiet gasps."
    "Her teeth graze my tip when she brings herself further down to kiss it and collect any precum she’s squeezed out of me, and it tempts me to grab her head and just end the contest in its opening stages."
    "Despite these desires of mine, though, I have no intention of doing that and plan on dragging this out for as long as possible."

    sar "Mm...[saramaster]...you taste so good..."
    sar "What do you say...mm...we just kick Haru-chan out and...mlem...spend the rest of the night together?"
    h "Hey."
    s "I’d say...I need a little more convincing."

    scene surprisebjcontest27
    with dissolve

    sar "Mnch...mmm...convincing?..."
    sar "I think I can handle {i}convincing...{/i}"
    sar "I just figured you’d want to spend a little more time with my tongue first before putting your fat cock in my mouth."
    h "This is one of those few times where I’ve really wished I had a penis."

    scene surprisebjcontest28
    with dissolve

    sar "Mm...mmf...don’t be...silly, Haru-chan..."
    sar "As if I’d...ever do something like this for you..."
    sar "There’s only...one cock that’s...ever been good enough for me and...mmf...it’s this one..."
    h "Uh-huh. I think your daughter is proof that that’s kind of not true."
    sar "Mmf...mmm...bite me..."

    "Sara continues to work on my shaft, slowly and passionately taking more and more into her mouth as she cups my balls with her free hand."
    "Occasionally, her earpiece or...microphone thing or whatever it is will come into contact with my skin and force her to divert attention away from my dick to readjust it."
    "However, she counteracts these moments by locking eyes with me, as if to say she doesn’t care how messed up her costume gets so long as she’s able to keep sucking me off."
    "Each time she goes back down, she pushes her ass up in the air. And while I’d like to find myself right there behind her, I’m not even sure if it would feel any better than this does."

    scene surprisebjcontest29
    with dissolve

    "Eventually, Haruka decides to join in as well, accepting the major head start that Sara has gotten and essentially disregarding that she’s yet to have any time to go down on me herself."
    "And while that jeopardizes her chances of winning, I am not about to stop her when she starts saying things like this."

    h "Wow...you really do love sucking cock, huh?"
    h "I bet you’re desperate for Sensei to bend you over right now and pound that tight little MILF pussy of yours, huh?"

    "As always, she shows very little tact- which is one of the many things I like about her."

    sar "Mmf...mm-mm...not...right now...Haru-chan..."
    sar "All I want...is [saramaster]’s hot cum in my mouth...I don’t...want to let it go..."
    h "You’re such a liar. I see the way you’re waving your ass around. I know you want it."

    scene surprisebjcontest30
    with dissolve

    sar "Mmf...mlem...you sound...jealous..."
    h "I am. I want to taste him too, you know. It’s no fair if you get to keep him all to yourself."
    sar "Mmf...mm...it’s...totally fair...Haru-chan..."
    sar "This cock...is for me...and me only...I’m the only one...who can give it the...mmf...care it deserves..."
    h "What happened to letting Sensei fuck {i}my{/i} mouth? And besides, if you’re so great, wouldn’t it feel nice seeing me fail to please him the way you can?"
    sar "Mmf...mm..."
    sar "Not really..."

    scene surprisebjcontest31
    with dissolve

    h "Okay. Move over, damn it. It’s my turn."

    scene surprisebjcontest32
    with dissolve

    sar "Fine, fine. Enjoy. Sorry if it tastes like wine. I’ve had a little bit to drink tonight."
    h "Mm...mmm...yeah...what else is new?..."
    sar "Okay. That’s long enough. Give it back now."
    s "Let her keep going, Sara."

    scene surprisebjcontest33
    with dissolve

    sar "Are you sure that’s what you want? Haru-chan’s a novice at this. She can’t please you the way I can."
    h "Mlem...mmm...fuck...off...Sara..."
    sar "And she’s so mean to me too."
    h "I bet it’s easy to say that after...hogging his cock all night..."

    "Haruka starts off the same way Sara did, but a little more aggressive in the fact that her licks aren’t gentle at all and that they’re forcing my cock backwards."
    "But each time it moves back, she wraps her lips around the head and drags it closer to her body- slowly gliding down and re-coating me with even hotter (And less alcoholic) saliva than her adversary."
    "This combined with the fact that I’ve never seen Haruka in a position like this is a little intoxicating to say the least."
    "I’ve lost track of how many times I’ve fucked her by now, but all of those occasions felt like acts of mutual, rampant lust rather than intimate moments between two people."
    "And while there’s a layer of that in this as well considering it is a literal competition, it also feels immensely different."
    "It’s the first time she’s servicing me without receiving anything in return."
    "Which helps me to realize that there are now two women in this room that I want to bend over and violently fuck."

    scene surprisebjcontest34
    with dissolve

    sar "Does this help you at all, [saramaster]?"
    sar "You like them smaller, don’t you? I bet Haru-chan's are too distracting."
    sar "Don’t get too excited by them, though. I wouldn’t want you cumming inside of her mouth instead of mine."
    h "Don’t...mmf...listen to her...give me...all that you’ve got..."
    h "Fill my...fucking mouth up...I want to drink it...I want to...drink your fucking cum..."
    h "It’s so big...mmf...fuck...fuck, I’m so hot...I want it inside of me...I want it inside..."
    sar "Look at that. She’s already thinking about herself."
    sar "You can fuck her if you want, [saramaster]. I told you I won’t get jealous. But, I think it should count as a win for me if you {i}do{/i} since it seems a little like she’d be forfeiting."
    s "Haruka...thoughts?..."
    h "Not...quitting..."
    h "Need you...mmf...to cum for me!"

    scene surprisebjcontest35
    with dissolve

    "I recoil from the sensation of Haruka defying what should be physically impossible and taking the entirety of my cock into her mouth."
    "She’s unable to move much once she accomplishes this, but accomplishing it alone is a feat to be extremely proud of."

    sar "I have to admit, Haru-chan {i}does{/i} look kind of cute with a dick in her mouth. But I’m not sure if that’s just because it’s {i}your{/i} dick or not."
    sar "Either way, it’s still clear that she doesn’t have the same level of skill that I-"
    s "Sara...look...down..."
    sar "Why? Is she doing something cute a-"

    scene surprisebjcontest36
    with hpunch

    sar "Oh my God! Haru-chan! How?!"
    h "Mff! Mck...mmlgm!!! Mmmmmmm!"
    sar "Where did this secret talent come from?! Why do I feel threatened all of a sudden?!"

    "I can’t help but assist Haruka’s blowjob by thrusting up into her mouth and, even though I expect her to have some sort of reaction to it, she stays completely still and just...lets me do my thing."
    "And, after a minute or two of this, I can’t help but remove myself from her so the competition doesn’t prematurely end before I can even make a choice..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene surprisebjcontest37
    with dissolve2

    "Sara realizes how close we are to the finish line, prompting her to leap over Haruka and begin licking my shaft again as the two of them please me in tandem with one another."
    "Their eyes lock onto me, each one desperate to be chosen as winner."
    "This goes on for what feels like an hour, but only because I’ve been devoting every last bit of willpower in my body to not ejaculating."
    "Unfortunately, that time ends now."
    "There’s just no way I can continue to go on like this when {i}both{/i} of them deserve to win."
    "But there can only be one."
    "And that one is..."

    menu:
        "Haruka":
            s "Haruka..."

            scene surprisebjcontest38
            with dissolve

            sar "What?! No!"
            h "Mm! Mm! Do it! Cum in...my fucking mouth!"
            h "Let me taste it! Let me...mmf...taste it!"

            with sexfade
            with sexfade
            scene surprisebjcontest39
            with cumflash
            with hpunch

            h "MMMMGHHHHH!!!!!!!!!!!!"

            scene black
            with dissolve2

            "........."
            "......"
            "..."

            scene surprisebjcontest42
            with dissolve2

            sar "No fair. I didn’t realize you had a secret weapon."
            h "Ahh...just like riding a bike...it all came rushing back to me."
            sar "I demand a do-over."
            s "I agree. Round two starts now."

            scene surprisebjcontest43
            with dissolve

            h "No way! Fair is fair and I will not let that mouth full of cum go to waste!"
            h "Molly’s win in the Second Annual Super Mega Ultimate Dorm Wars has been bolstered and the Sakakibara family has, once again, dropped the ball!"
            sar "It appears that I still have some practice to do."

            scene surprisebjcontest44
            with dissolve

            sar "I’ll be counting on you a lot more from now on. I hope that’s okay."

            scene black
            with dissolve2

            "In the end, everyone won."
            "And by everyone, I mean just Haruka and me."
            "But I regret nothing and will sleep easy knowing that I have, once again, made the correct choice."

            $ renpy.end_replay()
            $ haruka_love += 1
            $ haruka_lust += 1
            $ harukalust25 = True
            $ harukabjwin = True
            $ dorm2war2points += 1

            stop music fadeout 5.0

            "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
            "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
            "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
            "........."
            "......"
            "..."
            "{i}Early the next morning, in the second half of town...{/i}"

            jump dormwartwo10

        "Sara":
            s "Sara..."

            scene surprisebjcontest40
            with dissolve

            sar "Mmf! Yes! I knew...mmf...you’d choose me!"
            h "What?! But I clearly have the deeper throat! Which means that I am mathematically the winner! Hooray for floor two!"
            sar "That’s not...how it works...Haru-chan!"

            with sexfade
            with sexfade
            scene surprisebjcontest41
            with cumflash
            with hpunch

            sar "MMMMMMMMMMMMMM!!!!!!!!!!!!"

            scene black
            with dissolve2

            "........."
            "......"
            "..."

            scene surprisebjcontest45
            with dissolve2

            sar "Thanks for the meal."
            h "This is a great injustice and I feel as if I have been betrayed by both of you tonight."
            s "While your...uhh...esophagal depth is commendable, there was just more passion in Sara’s blowjob."
            s "And as the former captain of the competitive blowjob varsity team, I-"

            scene surprisebjcontest46
            with dissolve

            h "I don’t want to hear it. Friendship ended with Sara. Maki is my best friend now."
            sar "This calls for a celebration. Who’s up for a second round?"
            h "Not me. It’s like 3:00 AM and my jaw hurts, so I’m going home."

            scene surprisebjcontest47
            with dissolve

            sar "Holy shit, it’s 3:00 AM?"
            h "Yup. We gave Sensei head for roughly 90 minutes. I hope you’re proud of yourself."
            sar "I..."

            scene black
            with dissolve2

            sar "Maybe just a {i}short{/i} second round, then?"
            h "Goodnight, Sara."
            sar "Haru-chan, wait! You’re my ride!"

            "In the end, everyone won."
            "And by everyone, I mean just Sara and me."
            "But I regret nothing and will sleep easy knowing that I have, once again, made the correct choice."

            $ renpy.end_replay()
            $ sara_love += 1
            $ sara_lust += 1
            $ harukalust25 = True
            $ sarabjwin = True
            $ dorm1war2points += 1

            stop music fadeout 5.0

            "{i}Sara’s affection has increased to [sara_love]!{/i}"
            "{i}Sara’s lust has increased to [sara_lust]!{/i}"
            "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
            "........."
            "......"
            "..."
            "{i}Early the next morning, in the second half of town...{/i}"

            jump dormwartwo10

label makihornytrip1:
    scene sky
    with dissolve2
    play sound "phonebeep.wav"
    play music "summerwind.mp3"

    "I tap on Haruka’s name in my phone and prepare myself for yet another free vacation. "
    "Just, this time, it’s for the very specific purpose of reminding one of our friends that she is supposed to be horny all the time — which she currently is not."
    "Is this as big of a problem as Haruka seems to think it is? Probably not. But, then again, this {i}is{/i} Maki we’re talking about. And I’m not sure she’s had any time off ever since the whole husband thing happened."
    "Plus, things have been pretty crazy for me lately as well. So maybe I could use a bit of rest and relaxation too?"
    "I say that fully aware that this will somehow wind up either depressing, extremely sexual, or just not relaxing at all."
    "But hey, it’s worth a shot."

    play sound "phonebeep.wav"

    h "Mm...what do you want? It’s 7:00 AM..."
    s "So what? Aren’t you usually going to work around this time?"
    h "Aren’t you usually {i}sleeping{/i} around this time?..."
    s "Not when I know there’s a free trip still hanging in limbo."
    h "What?..."
    s "Get dressed, Haruka. It’s vacation time."
    h "Mngh...five more minutes..."
    s "Fine. I’ll call Maki in the meantime and let her know what’s going on."
    h "Wait-"

    play sound "phonebeep.wav"

    "I hang up the phone and dial Maki’s number. I hope she’s prepared to regain her libido."

    play sound "phonebeep.wav"

    maki "Hey."
    s "Hey."
    maki "Is it boner time?"
    s "It’s boner time."
    maki "I’ll pack my bag."

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Well, that was easier than I expected it to be."
    "I guess all that’s left now is to wait for Haruka to get ready and...figure out where the three of us are going to meet up."
    "Both of them drive so I’m sure that one of them will wind up swinging by to pick me up, but-"
    "..."
    "Never mind."
    "It’ll be fine."
    "I need to focus on relaxing."
    "........."
    "......"
    "..."

    scene harukamakicar1
    with dissolve2

    "As predicted, Haruka shows up a couple hours later with Maki already in tow and the three of us set course to...wherever it is we’re going. I’m still not really sure."
    "I decided against packing anything since I can always just sleep naked and...also wanted to avoid Ami noticing some of my things are missing as I’m sure she takes inventory of my possessions nightly."
    "Haruka drives slower than Maki — almost like she’s been made aware of how {i}fidgety{/i} I can be in places like this. "
    "And I’m sure the one who informed her is the same one listening to podcasts with her feet up in the back of the car right now."
    "Either way, this will be over before I know it and we’ll all have a great time turning each other on or whatever it is we’re supposed to be doing today."
    "I haven’t forgotten, it’s just a little harder to fully remember when I’m so focused on the clouds shadowing us from behind the trees."

    h "You good?"
    s "Why do you ask?"
    h "You’ve been tapping your foot ever since I picked you up. And I’m pretty sure it’s not to the soothing sounds of the Joe Rogan Show leaking out of Maki’s AirPods. "

    "I am apparently a bit less discreet about my discomfort than I thought."

    s "I’m good. You don’t have to worry about me."
    h "Of course I have to worry about you. "

    scene harukamakicar2
    with dissolve

    h "Even {i}if{/i} the main purpose of this trip is to fix Maki, it doesn’t mean that’s what it’s {i}all{/i} about."
    h "You’re my friend. And if there’s one thing I’ve learned about myself lately, it’s that I don’t always put you guys first when I probably should."
    s "Can you save your character development until we’re out of the car, please?"

    scene harukamakicar3
    with fade

    maki "Hm? Did somebody say something? Because if somebody said something, I didn’t hear it. I’m listening to the Joe Rogan Show on my AirPods."
    h "Yes, Maki. We know. Go back to listening to the Joe Rogan Show on your AirPods."
    maki "Okay. I’m going to go back to listening to the Joe Rogan Show on my AirPods now."

    scene harukamakicar4
    with dissolve

    s "I feel like there’s some kind of joke here I’m not getting."
    h "And I feel like now is the perfect time for character development since Maki is listening to the Joe Rogan Show on her AirPods."

    scene harukamakicar5
    with fade

    h "Listen, we’ve known each other for a while now, haven’t we?"
    s "I mean...I guess. Yeah."
    h "And within that time I have made out with you behind my husband’s back, hid it from Sara, turned everyone’s problems into my own, and then abandoned Maki when she needed me most."
    h "I’ve been kind of a bitch. We don’t have to pretend I haven’t been. I get that now. But that’s exactly why I’m trying to kind of, like...turn things around. And think of other people for once."
    h "I’ve never been great at that, but it’s not because I don’t care about you guys or anything. I’ve just always...put myself first, I guess."
    s "I don’t think there’s any harm in that, Haruka."

    scene harukamakicar6
    with dissolve

    h "Yeah, well you’re not the one trying to turn things around. I am. So don’t say stuff like, “You don’t have to worry about me,” because it like, totally goes against everything I’ve been telling myself lately."

    scene harukamakicar7
    with dissolve

    h "This trip’s for you guys, not me. Well, it’s mostly for Maki. And it was originally for Maki {i}and{/i} Sara. But you’re a suitable replacement. "
    h "I’m not sure if you’ll attract as many people as she would, though. Even {i}with{/i} the penis. Sara’s kind of popular with the younger crowds and gets stared at {i}a lot.{/i}"
    s "Probably because she blends in with them."
    h "Probably. I’m too busy also staring to really figure that out, but that doesn’t matter now. What matters is having a relaxing day and then leaving this place tomorrow feeling refreshed and reinvigorated."
    h "And in Maki’s case, horny. Hopefully."
    s "You really think just getting a day off at some fancy resort is going to be enough to set her back on track?"
    h "No."
    h "But I think it’s a start."

    scene black
    with dissolve2

    h "And a “start” never hurt anybody."

    "Somewhere along the way, the tapping of my left foot stops."
    "I do not alternate to my right- and I do not compensate by tapping my other limbs instead."
    "I simply focus on the clouds and the trees that try to hide them."
    "Soon enough, they’ll run out of cover."
    "And soon enough, so will I."
    "........."
    "......"
    "..."

    scene harukamakicar8
    with dissolve2

    "Haruka and Maki waste no time at all when it comes to changing into their swimsuits and I wind up meeting up with them after renting one that looks eerily similar to the one I have at home."
    "Also, I’m sure it goes without saying, but if the objective of this trip was to get {i}me{/i} horny, we could probably just pack up and head home now because {i}wow.{/i}"
    "Though, I guess it’s possible I just spend so much time around girls who have barely outgrown training bras that seeing two fully developed women at once just {i}gets{/i} to me, you know?"
    "But I digress as this is the part of the day where I squeeze my way into a conversation that would best be left between two girls."
    "Or rather, two best friends — as I might be a replacement for Sara, but I will never be a {i}replacement{/i} for Sara."

    h "Is there anything in particular you want to do today? I got massages lined up for the two of us a few hours from now. And we’ve got dinner reservations at 5:00. But if there’s anything else, just tell me."
    maki "You’re really going all out, huh? You’ve never splurged on me like this before. And I’d know because I’ve been splurged on by at least like, twenty guys. Probably more."
    maki "That second splurge was supposed to be “splooge.” "
    maki "Like, cum. I’m saying at least twenty guys have came on me. And you are currently...financially cumming on me. Or something."
    h "You done?"

    scene harukamakicar9
    with dissolve

    maki "Yeah, sorry. My heart’s just not in it right now."
    h "That’s fine. There’s no need to rush or anything. We can take it one hour at a time."

    scene harukamakicar10
    with dissolve

    h "But also know that I won’t hold it against you if you start returning to normal halfway through the trip and want to run off with Sensei for a little fun."

    if makisex == True:
        maki "I’m good, but thanks."
        s "Wow, okay."
        h "Are you suuuuure? Not even the tip? Because the tip doesn’t count."
        s "I don’t think it works that way."
        maki "I’m an authority on the subject and I can confirm that Haruka is right. The tip doesn’t count. It’s shaft or nothing."
        s "Okay then. Maybe it works that way after all and I’m just behind on the times."
    else:
        maki "Yeah...something tells me neither one of us thinks that’s going to happen."
        h "What happens at fancy resorts stays at fancy resorts. I won’t tell anyone."
        maki "I...don’t think that’s the problem here."

    scene harukamakicar11
    with dissolve

    h "Maki, come on! What’s with that expression? Lighten up a little! Go flirt with randoms and...ego-surf or something. There are plenty of people around here who’d be happy to hit on you."
    maki "Am I supposed to go around and flirt with people or lean back and relax? You’re pushing me in multiple directions and I’m not sure which one will get me closer to you being a little less...Haruka."
    h "Maki, all I want is for you to get back to your normal self. It hurts {i}all{/i} of us seeing you so...blah all the time."
    maki "I’m not even “blah,” though. I’m just...not as interested in sex anymore. "

    scene harukamakicar12
    with dissolve

    h "But {i}why?{/i} Sex is awesome. You love sex. I love sex. Everybody loves sex."
    maki "If sex is so good, how come there’s no sex 2?"
    s "What?"
    h "Yeah, what?"
    maki "What I’m saying is...if you love sex so much, why don’t you just marry it?"

    scene harukamakicar13
    with dissolve

    h "Again, what? Also, I’m already married."
    maki "Wow. Rub it in, why don’t you?"
    h "Maki..."
    maki "Haruka, if you want to leave me behind to go “flirt with randoms” and be all sexual and stuff, more power to you. Go for it. I always thought you’d be better off in an open marriage anyway. "
    maki "That way, you could still hang out with your buddies Sex 1 and Sex 2 and be totally guilt-free about it."

    scene harukamakicar14
    with dissolve

    h "You know a lot of people just view that as cheating though, right?"

    if harukasex == True:
        maki "A lot of people view cheating as cheating too and that hasn’t stopped you yet."
        s "Oof."
    else:
        maki "And a lot of people think pineapple belongs on pizza. That doesn’t mean they’re right. It means they have a stupid fucking opinion and the world would be better without them."

    h "I’m glad that sort of thing works for you, I’m just...I’m not really sure it would work for me personally. Nor do I think I can just convert the relationship to “open” while my husband is fighting aliens."
    h "It'd make more sense to just...end the marriage altogether, I think."
    maki "Haruka, for all we know, he might be {i}fucking{/i} aliens. Which, again, would be totally cool if your marriage was open."
    maki "I bet Masahiro fucked at least one alien before he died. I know {i}I{/i} would’ve. Well, back when I was still horny, at least. Right now, there might be a little...conflict in terms of getting it in."
    maki "Unless alien dicks are self-lubricating. Which they might be. We don’t really know. But I hope they are. Or were. For Masahiro’s sake."

    scene harukamakicar15
    with dissolve

    h "As good a saleswoman as you are, I’m not sure if open marriages are the sort of thing you should be peddling onto other people when they’re most definitely not for all of us."
    maki "But they {i}should{/i} be because sex and love don’t always have to be linked. Sometimes, you just want to try something different. And don’t pretend for a second you don’t."

    scene harukamakicar16
    with dissolve

    h "I’m not “pretending” anything. It’s perfectly normal to fantasize about stuff. It’s only {i}wrong{/i} once you actually act on it."

    if harukasex == True:
        maki "Then what’s the problem at this point? You two are already having sex. And cool, friend-sex at that. Wouldn’t it be better if that was just {i}allowed{/i} rather than something you have to feel guilty about?"
    else:
        maki "“Wrong” is subjective. There’s no definitive right or wrong when it comes to stuff like love and sex. It’s not, like...murder or something. It’s way simpler than that."

    s "I thought the whole open marriage thing was your husband’s idea, wasn’t it?"
    maki "Just because it was his idea doesn’t mean I can’t like it as well, does it? "
    maki "I think it was great for us in a bunch of ways, and that it would be great for a lot of other people as well if they could overlook the stigmas surrounding it."
    h "Either way, it’s too late to just change now. That would have had to be something we talked about beforehand."
    maki "Maybe you already did? Your husband had no problem with {i}me{/i} fucking you. Who’s saying he wouldn’t have budged if somebody else wanted to as well?"
    h "Can we go back to talking about you now? I’ve somehow become the target of this and I’m not quite sure how or why."
    maki "The {i}why{/i} is because you’ve been pushing my buttons nonstop lately and I wanted to push yours for a minute or two as revenge. The {i}how{/i} is kind of self-explanatory."

    scene harukamakicar17
    with dissolve

    h "You really think I’ve been pushing your buttons?"
    maki "Yes. But I know you’re doing it out of love this time, so that makes it kind of okay."
    maki "Honestly, I know this whole no-horny thing is probably shocking to both of you. But I don’t think a one day vacation or flirting with young people is going to fix that."

    scene harukamakicar18
    with dissolve

    h "What about a fancy dinner? Or wine? Or a fancy dinner {i}with{/i} wine? Or a sensual massage from an androgynous therapist with extremely strong hands?"
    maki "That last one does sound nice. But that might just be because I’m old and my back hurts all the time."

    scene harukamakicar19
    with dissolve

    h "{i}Your{/i} back hurts? Give me a break. Like a third of my body weight is latched onto my chest and trying to pull me down all day. "
    maki "Yes, but I have probably spent significantly more time in strange sex positions than you have. And those can take a toll on a woman."

    scene harukamakicar20
    with dissolve

    h "Fair. "
    h "You can have it your way once we leave the resort. I’ll stop pestering you about stress levels and the reclamation of your libido and just...let you do your own thing."
    h "But for the rest of today, I’d be happy if you humored me by coming along for all of the stuff I planned. Or, at the very least, just trying to relax in some form."
    maki "I’ve been trying to do that since we sat down and you made it weird by telling me to go fuck our other friend."
    h "I didn’t tell you to fuck him. I said I’d be {i}okay{/i} with you fucking him. Which I am."
    maki "Thank you for the clarification. Boner time is over. Nap time is now."
    s "Hi. “Other friend” here. What am I supposed to do while the two of you sit there with your eyes closed?"
    h "Go flirt with randoms since Maki won’t and I made the apparent mistake of not opening my marriage."
    s "Right. And if I can’t find anyone else to have sex with while you’re taking a nap?"
    h "Then you can go schedule a massage like I did for Maki and me and hope that your masseuse offers {i}those{/i} kinds of services."
    maki "But please be advised that one of us was already kicked out for asking that once."
    h "We will never tell you which one it was."

    scene black
    with dissolve2

    s "I’m...not sure I even want to know."

    $ renpy.end_replay()
    $ maki_love += 1
    $ haruka_love += 1
    $ makihornytrip1 = True

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    jump makihornytrip2

label makihornytrip4:
    scene sky
    with dissolve2

    "As the morning comes, the three of us are forced to accept that this was all for nothing."
    "Maki is still unmotivated and un-horny, Haruka is still trying to figure out what she’s supposed to do, and I am still the same buffet of misery I have always been — just now with a side of mild paranoia."
    "Also, I promise that buffet comparison wasn’t one made out of sheer spontaneity. I speak (or think) to you now from the corner of a white table in a blue room with various pastries spread out before me."
    "Unfortunately, I’m not able to eat anything at all."
    "The pit has taken up far too much space."

    scene black
    with dissolve2
    play music "cafe.mp3"

    "Eventually, we leave the resort and return to our normal, unfulfilling lives."
    "Haruka has to work, Maki has to go home, and I have to wander the streets for yet another Sunday in hopes of finding somewhere to bury my dick until the moon shows up."
    "As always, my choices are somewhat endless — and I’ll use that thought to carry me forward when my body is reluctant to."
    "One day of rest was not enough to change anything at all."
    "But at least we can take solace in the fact that it was a bit easier to ignore things for a little while."

    scene harumakicafe1
    with dissolve2

    "Anyway, here’s Koi Cafe."

    h "Sorry we weren’t able to fix you, Maki. I wish there was something more I could do, but I can’t really afford to take more than a day or two off at a time. "
    maki "Why are you apologizing? This isn’t really something you have any control over in the first place."

    scene harumakicafe2
    with dissolve

    h "I mean...yeah. I just kind of figured there would have been {i}something{/i} yesterday that would have helped in some way. But if it’s more than just stress or whatever, I’ve got literally no idea what I’m supposed to do."
    maki "Then don’t do anything. Like I said, this isn’t on you. And I never expected your plan to work anyway, so I’m not even let down."

    scene harumakicafe3
    with dissolve

    h "Was that last part really necessary?"
    maki "As rude as it sounded, yes. It was necessary — but not to show you I didn’t believe in you. It was to show you that this is something I’m just going to have to get over on my own."
    maki "Think of it like a cold or the flu or something. Just instead of coughing or throwing up, I lack the desire to shove stuff inside of myself. It happens to everyone."
    h "Hard disagree. But if that’s what you say, I’ll just have to take your word for it. And if there’s anything else you need, don’t hesitate to ask."
    h "I know I haven’t been the best friend, but-"

    scene harumakicafe4
    with dissolve

    maki "Stop putting yourself down. You’ve been great lately and I’m happy to have you by my side."

    scene harumakicafe5
    with dissolve

    maki "But, on that note, I must be off! I always say that sex toys sell themselves, but it’s not like money is going to put itself into the register, so yeah."
    s "Think you’ll be able to keep up the “sex is awesome” facade for a little while longer?"

    if makisex == True:
        scene harumakicafe6
        with dissolve

        maki "Of course. I’m a great faker, you know. I’ve got at least two months left of this illusion before it starts to crack and {i}really{/i} get to me. Until then, I’ll just keep laughing at my problems like I always do!"

        "Welp, I guess that means I won’t be “spending much time” with Maki in the near future. Sexually, at least. I’m sure I’ll still see her around if I-"

        play sound "static.mp3"
        scene makotohandy37 with flash
        scene harumakicafe6 with flash
        stop sound

        "You know, maybe it would be for the best if I just left her alone altogether for a little while."

        maki "Besides, now that I know what I must do, I might be able to turn this thing around. We’ll see!"
        s "..."

    else:
        maki "Of course. I’ve got plenty of experience when it comes to faking it — and I’m not about to let a little dry spell ruin my life."
        maki "Especially not when I know what it is I must do now."
        s "..."

    scene harumakicafe7
    with dissolve

    h "What you {i}must do?{/i} Are you saying you’ve finally figured out how to get out of your slump?"
    maki "Yes. And for that, I will require my daughter’s assistance."

    scene harumakicafe8
    with dissolve

    h "You what?"
    maki "Only Makoto can fix me now, Haruka. Without her, I may never get horny again."
    h "Uhh..."
    maki "Anyway, off to work! Enjoy your shift and thanks again for all the money you spent on me!"

    scene harumakicafe9
    with dissolve

    maki "Bye!"
    h "Uhh...bye?"
    s "Now, I know how that probably sounded without context, but I can assure you there is a perfectly logical explanation for it."

    scene harumakicafe10
    with dissolve

    h "If it’s anything other than “Maki is into some really weird shit,” I’m not sure I want to hear it."
    s "Well, luckily for you, Maki {i}is{/i} into some really weird shit and we all know that already. But this actually isn’t that weird. At least not by comparison."
    h "Well, first off, why didn’t you tell me this before I set up a really expensive resort trip? And second, why do {i}you{/i} know and not me?"
    s "I didn’t find out until last night when I went out with Maki. And it’s not like I was going to wake you up to tell you. "
    h "Well, why aren’t you telling me now? Spill it, dude. The sooner Maki’s libido comes back, the sooner her porn recommendations stop being so...impersonal. "
    s "I can’t tell you with Rin standing right there."

    scene harumakicafe11
    with dissolve

    r "Hey! I’ve kept my mouth shut this whole time and this is the thanks I get?! I’m really good with secrets when I’m not accidentally spilling them to the people I love!"
    s "And it is for that reason I can not tell you just yet."

    scene black
    with dissolve

    h "Rin, thank you for holding down the fort, but I’m going to need you to go into the back for now so I can have an adult conversation. "
    r "You have plenty of adult conversations around me! Sometimes, too many!"

    scene harumakicafe12
    with dissolve

    h "And there will be plenty more to be had in the future. But right now, you are standing firmly between me and gossip involving a good friend of mine and I need you to get lost."
    r "Fine. But you should know that I’m going to make {i}you{/i} get lost the next time Otoha shows up to gossip about our friends."
    h "You can’t make me do anything. I sign your paychecks."

    scene harumakicafe13
    with dissolve

    r "Then I’ll sign them myself! Bye!"
    h "That’s not how it-"

    scene harumakicafe14
    with dissolve

    h "...works."
    s "..."
    h "..."

    scene harumakicafe15
    with dissolve

    h "So anyway, what’s the deal? What do you know that I don’t?"
    s "First off, I’m only telling you this because I know Maki is going to tell you eventually as well. Second, I am {i}also{/i} only telling you this because I know you won’t judge me. Third, this conversation never happened."
    h "Is there a “fourth” or are you just going to fucking spill it already?"
    s "There’s no fourth. Maki thinks Makoto is having sex and is torn up over what to do about it to the point where it is skewing her perception of sex altogether."
    h "Well, that seems pretty reasonable to me. Makoto’s still really young and-"

    scene harumakicafe16
    with dissolve

    h "Oh my God it’s with you, isn’t it?"
    s "You’re not supposed to judge me."
    h "You motherfucker. Give me your wallet."
    s "What? Why?"

    scene harumakicafe17
    with dissolve

    h "Because this is {i}your{/i} fault! And I literally paid for a ticket that {i}you{/i} used to try and fix a problem that {i}you{/i} created!"
    s "I mean, technically, you bought that ticket for Sara and I was never supposed to come. So I’m just...going to hang onto my wallet for now, thanks."

    scene harumakicafe18
    with dissolve

    h "With {i}Makoto?{/i} Really? Her dad just died, man. And you’re already on really great terms with Maki. Are you just {i}trying{/i} to create drama at this point?"
    s "This isn’t a new thing, Haruka. It’s been going on for a while. Maki just...didn’t catch on until now, I guess."

    scene harumakicafe19
    with dissolve

    h "Ugh. If I had known {i}that’s{/i} what was going on, I never would have gotten involved in the first place."
    s "We both know that’s not true. You love drama. "
    h "Yeah, but I also love Maki. And finding out that you’re porking her teenage daughter is really screwing with my new “I’m going to be a better friend” mentality."

    scene harumakicafe20
    with dissolve

    h "What’s your plan here? Because if Maki “knows what she must do” now, it sounds a lot like she’s going to talk to Makoto about it. "
    s "Makoto won’t say anything about me to her. I’m, like...99%% sure of that. "

    scene harumakicafe21
    with dissolve

    s "But you need to keep your mouth shut too because you’re complicit now and- what are you doing? Why is your hand out?"
    h "Wallet. I’ll only take what you owe me."
    s "Are you serious?"
    h "I spent a lot of money this weekend, you know. Money I wouldn’t have {i}had{/i} to spend if a certain somebody knew how to keep his dick in his-"

    scene harumakicafe22
    with dissolve

    s "Fine. Take it. Whatever."

    scene harumakicafe23
    with dissolve

    h "Pleasure doing business with you."
    s "I won’t forget this."

    scene harumakicafe24
    with dissolve

    h "Seriously, though — what’s your move? Because if Maki {i}does{/i} have a serious conversation with Makoto about this and it {i}doesn’t{/i} go well, it’s going to be on you."
    s "That’s not...entirely true, is it? Because this same thing would eventually happen even if it wasn’t me. And there’s no guarantee Makoto would just openly talk to Maki about it then either. She struggles with that."
    h "Wow, you sound like you know her really well. If I didn’t know any better, I might even assume you two were having sex."
    s "Haruka-"

    scene harumakicafe25
    with dissolve

    h "Man! Why did it have to be {i}her?{/i} You know I love talking about this stuff, but there’s never been a conflict of interest like this for me before. I have no idea what to do now!"

    if harukasex == True:
        s "Just...be there for Maki, I guess. No one’s asking you to get involved with Makoto and me — no matter how much you may want to."
    else:
        s "Just...be there for Maki, I guess. No one’s asking you to waste any thoughts on Makoto’s sex life. Apart from the ones I assume you already waste, that is."

    scene harumakicafe26
    with dissolve

    h "Sensei! Do you really think {i}I{/i} would ever look at a friend’s daughter that way? {i}Me?{/i} Haruka Hamasaki? Someone who could only be described as “a great friend with unflappable morals?”"
    h "I’m appalled. To think {i}I{/i} would ever fantasize about fingering a friend’s daughter is just absurd. "
    h "And it would be even more absurd to fantasize about her doing things to {i}me.{/i} How could you even suggest that? I’m shocked. Completely and utterly shocked. I would never."
    s "You’re really selling it right now, Haruka."
    h "There’s nothing to sell. I wouldn’t ever even {i}imagine{/i} something like that. It’s sickening. Totally sickening. Never."
    s "..."
    h "..."

    scene harumakicafe27
    with dissolve

    h "Oh, look. A customer."
    s "My bad. I’ll get out of the-"

    scene harumakicafe28
    with fade

    s "...Nodoka."
    no "Get {i}out{/i} of the Nodoka? Why would anyone ever get out of the Nodoka? That makes it sound like it’s not pleasant inside of me. "
    s "What are you doing here?"
    no "You really need to ask what {i}I{/i} am doing in a coffee shop? Keeping myself alive, of course. "
    no "If I don’t get enough caffeine in the morning, I’ll turn into a demon. Then no one will want to enter the Nodoka in the first place."
    h "Morning, Nodoka. Black coffee?"

    scene harumakicafe29
    with dissolve

    no "Yes, please. And if you could leave a little room for your phone number, it would be greatly appreciated."
    h "Ha ha ha. Very funny."

    scene harumakicafe30
    with dissolve

    no "She always thinks I’m joking, that one. Either that or I’m just widely undesirable by those over the age of...sorry, how old are you again?"
    s "I’m 31, Nodoka."
    no "Well, I truly hope that isn’t the cutoff. I’d be quite upset if you got {i}bored{/i} of me now that we’re...better acquainted. "
    h "Better acquainted?"

    scene harumakicafe31
    with dissolve

    no "Oh, don’t mind me. I’m just young and curious and in the throes of my first “schoolgirl crush.” How cliche that it’s on my {i}teacher{/i} of all people."
    h "That...seems to be a recurring issue for your class, doesn’t it?"
    no "Like I said. {i}Cliche.{/i}"
    h "Well, no shame in following your heart. Here’s your coffee, Nodoka."
    no "Thank you, love. Would you be able to put it on my tab? I seem to have misplaced my wallet. "
    h "No need. I have an extra one right here. "
    s "Isn’t that my-"
    no "I’m also willing to...{i}work{/i} for it, if need be. And I’m a very good worker. Just ask Ak- {i}ahem...{/i}Sensei."
    h "We were actually just talking about something very similar..."
    s "Just give her the coffee and make her go away."

    scene harumakicafe32
    with dissolve

    no "And to think just recently you were so insistent on making me {i}come{/i} instead. I wonder what’s changed."
    s "What’s changed is it’s too early to deal with you right now. You’re not the only one who hasn’t had their morning coffee yet."
    no "Then I suppose I might just have to give you a call later...When I’m more {i}bearable...{/i}"

    scene harumakicafe33
    with fade

    r "Oh, Nodoka. What are you doing here?"
    no "Why does everyone keep asking me that? I feel as if it should just be assumed at this point that I’m going to show up anywhere beautiful women gather. With priority placed on sites that serve coffee, of course."

    scene harumakicafe34
    with dissolve

    r "Neat. How’s Otoha? I haven’t heard from her today yet."
    no "And it would probably be best if you didn’t. She is...caught up in the moment once again."
    r "I figured as much. Oh well. I can wait. She’ll text me when she texts me."
    no "My, you’re certainly a lot calmer now that you’re sexually active, aren’t you? "

    scene harumakicafe35
    with dissolve
    play sound "dooropen.mp3"

    h "And there she goes."
    no "The female heart is so complicated, isn’t it? How we’ll often run from the exact things that make us feel whole..."
    s "I’m pretty sure Rin just doesn’t want to talk about her sex life at work."

    scene harumakicafe36
    with dissolve

    no "Then I suppose that’s just one more thing that makes her and me so different."
    h "Coffee’s brewing right now, Nodoka. But if you want to go take a seat, I’ll run it out to you once it’s done."

    scene harumakicafe37
    with dissolve

    no "Fantastic. Will your number be arriving along with it?"
    h "We’ll...see about that."

    scene harumakicafe38
    with dissolve

    "Nodoka goes to take a seat and Haruka...is suddenly consumed by a peculiar expression."

    h "..."
    s "..."
    s "Haruka?"

    scene harumakicafe39
    with dissolve

    h "Oh. Hi. Yeah. "
    s "Is there...a reason you suddenly look so different?"

    scene harumakicafe40
    with dissolve

    h "Uhh..."
    s "..."
    h "..."

    scene harumakicafe41
    with dissolve

    if harukasex == True:
        h "Maybe we could talk about that the next time you come over?"
    else:
        h "I should...probably just get to work."
        $ harukadate30skip = True

    scene black
    with dissolve2

    "I join Nodoka at her table and talk with her for a few minutes while her coffee finishes brewing."
    "She tells me all about the different ways to make it."
    "And I’m stricken by an intense bout of deja vu that feels even more inexplicable than normal."
    "When I leave the cafe, I look back at Haruka."
    "She both smiles and shakes her head disapprovingly."
    "And I carry on with the life she wishes she could live while she remains stuck inside."

    $ renpy.end_replay()
    $ makihornytrip4 = True
    $ haruka_love += 1
    stop music fadeout 7.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label harukadate30:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    h "Sex?"
    s "Sex."

    scene harukapostbone1
    with dissolve2

    "We have sex."

    play music "thesleepingcity.mp3"

    "But I guess that sort of thing is to be expected at this point."
    "Part of me wants to feel bad that we’re still doing this despite her being fully aware that her husband is safe and sound but, at the end of the day, if anyone should feel bad, it’s her."
    "I have no reason to feel guilty about sleeping with someone else’s wife when I know full well this world won’t let him come back."
    "Unless everyone in space is somehow exempt from these strange timeloops and is carrying on with their lives completely unaware of what we’re all going through."
    "That would sure be a trip."
    "Imagine he just comes back one day and walks into his home to find his wife in bed with some guy he’s never met? "
    "In fact, that’s probably exactly what would happen given my track record of reckless sexual exploits and drama’s tendency to stick closer to me than my own shadow."
    "But for now, I’ll cling to this bed and envelop myself in another dose of post-coital clarity and wait for the next round to begin."
    "We can only avoid it for so long."

    h "Hah...hah...wow...{i}wow...{/i}that was good..."
    h "Give me...a minute or two...and then...we go again..."
    s "Yeah, I may need a little more recovery time than that. Unlike you, I don’t have the luxury of being able to infinitely orgasm. "

    scene harukapostbone2
    with dissolve

    h "It...certainly helps that...I have a partner now who’s...able to {i}make{/i} me..."
    s "Yeah, yeah. I know I’m better than your husband. You don’t have to remind me {i}every{/i} time."
    h "Liar. Are you seriously telling me you {i}don’t{/i} like hearing how much I love your cock? "
    s "That I am, Haruka. That I am."
    h "Then how come it’s getting hard again?"
    s "I don’t know. Probably science or something. But please leave it alone for now. I need to...replenish my resources."

    scene harukapostbone3
    with dissolve

    h "Ahh...it feels so much different doing this now that I know my husband’s totally fine. Like, if I wasn’t a fucking whore {i}before,{/i} I totally am now."

    scene harukapostbone4
    with dissolve

    s "Is it self-deprecation time? Should I start talking about how emotionally closed off I am?"
    h "Just degrade me instead. Tell me I’m a thirsty, unfaithful, cock-obsessed bitch."
    s "..."
    h "Do it, pussy."
    s "You’re being weird."
    h "How am I being weird?"
    s "Because you normally wait until my penis is inside of you to start saying things like that."

    scene harukapostbone5
    with dissolve

    h "That was the old me. There’s no use in hiding how I really feel at this point when we both know I can’t let you go. "
    s "..."

    scene harukapostbone6
    with dissolve

    h "Shitty, right? Like, it would be one thing to just keep fucking you while waiting for him to get back. But at this point, I’m wondering if I should just forget him altogether."
    s "Are you...able to do that?"
    h "Who even knows? I’m so far gone now that it's probably possible."
    h "Honestly, the only thing holding me back is how {i}you{/i} feel."
    s "How I feel? What does that mean and...why does it matter?"

    scene harukapostbone7
    with dissolve

    h "There’s no need to be so obtuse when I’m literally covered in your jizz. We both know you’re crazy turned on by the fact that I’m married. And that’s totally cool. I don’t mind at all."
    s "Yeah, I can tell by the way you bring it up all the time."
    h "Oh, shut it. You bring it up just as much. We should just accept the fact that we’re horrible, disgusting people so we can keep...you know, being horrible and disgusting together."

    scene harukapostbone8
    with dissolve

    h "Now hurry up and remind me why I’m suddenly okay with abandoning my husband."
    s "Ten more minutes."

    scene harukapostbone9
    with dissolve

    h "Hmph. Fine. But only if you fuck me from behind since I don’t want to look at you right now."
    s "Oh no. What a cruel punishment."
    h "..."
    s "..."
    s "Do you really feel that way, Haruka?"

    scene harukapostbone10
    with dissolve

    h "Hm? What way?"
    s "That I’m somehow worth throwing away your entire life for."
    s "I get that I have a huge dick and that we are extremely sexually compatible...but it seems a little weird for that to suddenly reel you in when you were so conflicted about it just a short while ago."

    scene harukapostbone11
    with dissolve

    h "It wouldn’t be my {i}entire life.{/i} In fact, mostly everything would stay exactly the same as it is now. "
    h "In fact, it would probably get {i}easier.{/i}"
    h "My job wouldn’t change. My friends wouldn’t change. {i}You{/i} wouldn’t change. In fact, the only thing that {i}would{/i} change would be the sudden lack of your beloved netori kink."
    s "There’s something you’re forgetting though, and it’s {i}you.{/i} Walking away from your husband would be a major change in your life. Even {i}if{/i} he’s been gone for...however long he’s been gone for."

    scene harukapostbone12
    with dissolve

    h "I feel like you’re saying the exact opposite of...basically everything else you’ve ever said to me. It always seemed like you were pushing me to believe that his existence was just a burden or something."
    s "Yeah. Because that helped convince you to have sex with me."
    h "And now that I’ll willingly have sex with you whenever you want, there’s no reason to say that stuff anymore?"
    s "Pretty much, yeah."
    h "Wow. You’re a huge dick."
    s "That I am, Haruka. That I am."

    scene harukapostbone13
    with dissolve

    h "That still doesn’t change anything, though. I’m just as bad as you are at this point. "

    scene nightsky
    with dissolve2

    h "And I figure that...if I’m going to keep sleeping with you, which I have obviously decided to do based on all of this cum-"
    s "If you try and wipe that on me, I will actually kill you."
    h "Boooring. But what I was saying is that, if I’m going to keep sleeping with you, I should at least be, like...decisive about it, you know?"
    h "No more “Waaahhh I wish my husband were here” or “I guess I {i}have{/i} to fuck my guy friend because what {i}else{/i} am I going to do with all this spare time?”"
    h "It’s all part of the great Haruka reconstruction process! There’s {i}this{/i}...putting my friends first...and one other thing I want to pick your brain about."
    s "That thing being?"

    scene harukapostbone14
    with dissolve2

    h "Do you think I’m a bad person?"
    s "Yes."
    h "I agree. I {i}am{/i} a bad person. "
    s "I also think there’s a bit of a flaw in your logic when it comes to putting your friends first as I imagine your husband would qualify as one of those friends- and I am {i}definitely{/i} ahead of him right now."
    h "You’re ahead of him in basically everything. And you’re that far ahead {i}because{/i} I am a bad person. But that’s not the thing I want to pick your brain about. It’s just the intro. "

    scene harukapostbone15
    with dissolve

    h "I’m rotten. "
    h "I’m fucking a guy that my two closest friends are obviously into. And even though I know you’re not {i}dating{/i} either of them, it still feels like I’m taking something away from someone else at times."
    h "And that really turns me on, so I get why you always fuck me harder whenever I remind you that I’m technically taken."
    h "As gross as it sounds, I fucking love that about us. I love that I can basically say anything I want whenever you’re fucking me and it’ll just...be okay."
    h "Maybe it’s just because I haven’t felt “free” in a long time or something like that, but...the point I’m trying to make is that I {i}know{/i} what I’m doing is wrong...and that kind of just makes me want to do it more."
    h "I figure that, if I’m going to be such a {i}bad girl...{/i}that I might as well be as bad as I possibly can, right?"
    h "It’s not enough to just cheat on my husband anymore. And it wouldn’t be enough to leave him for some other dude who I don’t even really {i}want{/i} to be exclusive with in the first place."
    s "Where do I come in, though? What do you need to pick {i}my{/i} brain for?"

    scene harukapostbone16
    with dissolve

    h "I want your help with something."
    s "If it’s providing you with another orgasm, I need at least five more-"
    h "I want you to corrupt me."
    s "You...want me to {i}corrupt{/i} you?"
    h "Mhm."
    s "Not going to lie, I think the layman would say you’re pretty corrupt already."
    h "But you’re worse. You’re way more depraved than I am. And you’re enjoying life way more than I am too."
    s "I’m not sure I’d call what I do “enjoying life,” Haruka."
    h "Okay, fine. But would you at least admit that your sex-life is insanely fulfilling?"
    s "Would you not?"
    h "I would."
    h "But I want {i}more.{/i}"
    s "Well, what more do you want?"
    h "Everything you have."
    s "You already took my wallet. What’s next?"
    h "Two things."
    s "They better be good."
    h "Number one — I want to give you full control over my body. "
    s "Sold. "
    h "What I mean by that is that I will follow your orders whenever...{i}wherever{/i} you want me to follow them."
    h "It doesn’t matter if I’m at work...it doesn’t matter if {i}you’re{/i} at work...and it doesn’t matter what sort of consequences come from whatever it is you want."
    h "Anything you ask me to do...from the clothes I wear to the positions you fuck me in...I’ll do it without a question. "
    h "But there’s something I’d like in exchange for that...and that brings us to thing number two."
    s "If it’s as good as the first, this might wind up being the best day of my life."
    h "Number two..."
    h "I want you to help me fuck someone in your class. "
    s "..."
    h "Or...any teenager in general really. I’m not very picky. "
    h "But it’s obvious I’m attracted to the same kind of girls you are and I can’t really...go all the way on my own. I’m too much of a coward to ever actually make a move on one. It’s just...too risky."
    h "But you? You’re basically drowning in cute teens and haven’t gotten into trouble for it even once. And if you bring me along, I doubt most of them would refuse."
    s "Haruka-"
    h "I know it’s a bad idea. And I know you’re probably going to try and talk me out of it or give me some lecture on how it’s disgusting {i}you’re{/i} doing it in the first place...but I don’t care."
    h "Like I said, if I’m going to be bad...I want to be {i}bad.{/i} And I want a taste of the life you’ve made for yourself since it’s a taste I’ve never had before."
    h "Even if it’s just watching you, that’s fine. But I want to be involved. "
    h "I want to feel as free as you."
    s "This is the worst idea you’ve ever had."
    h "But it’ll be one of the best if it winds up working out."
    h "Just think of it like...teaching me how to ride a bike or something. I just need to get over that initial fear and then everything will work itself out."
    s "Except it won’t. You’ll be taking advantage of vulnerable girls who-"
    h "I know."
    h "But that’s what I want. And it’s part of everything you have."
    s "..."
    h "Are you disgusted by what I’m asking of you?"
    s "To be honest...yeah."

    scene harukapostbone17
    with dissolve2

    h "Good."
    h "Because that means I’m finally getting a little fraction of the hate that I deserve."
    h "You should’ve been disgusted all along, Sensei. "
    h "I’m a traitorous, cheating whore who lets a man she doesn’t even know the name of fuck her raw...A slut who touches herself to pictures of the girls she hires before going to sleep at night..."
    h "And with your help, I can be all of that times ten."
    h "Just think of how fun that would be for {i}both{/i} of us."
    h "Don’t you want to watch me suck your cock with Rin? Or lick your cum out of Molly’s pussy?"
    s "Haruka, I’m not fucking either of them."
    h "{i}Yet.{/i} We all know it’s coming. And when it does, I want to be there for it. "

    scene harukapostbone18
    with dissolve

    h "That sounds like a fair trade for gaining me as what will basically be a sex slave, doesn’t it?"
    s "It sounds like you’re making a big mistake. "

    scene harukapostbone19
    with dissolve

    h "If you haven’t noticed, I tend to do that."
    h "But like, you had to have known this was coming, right? You’ve seen how I look at all of those girls for a fucking while now and, not gonna lie, I’m kind of offended I’ve never been invited to anything."
    h "It’s no fair that {i}you{/i} get to have all of the fun and I have to just {i}hear{/i} about it. Help me out. I’m absolutely sure it will be worth the time and effort."
    s "Haruka-"

    scene harukapostbone20
    with dissolve

    h "We can start with Nodoka."
    s "What?"
    h "She’s been flirting with me for a while. And everything she said to you at the cafe made it pretty clear that you two are already fucking, so..."
    s "..."
    h "Do you think you can make that happen?"
    s "..."
    s "I think..."
    s "I think I need to sleep on it."
    s "And I think you need to sleep on it as well."
    h "I’ve been sleeping on this for years."
    h "I just never thought I’d meet someone so depraved that I’d feel inclined to actually {i}act{/i} on it."
    h "I guess that, in a way, you kind of already {i}have{/i} corrupted me. You’ve shown me there’s more to life than love and that burying yourself in your flaws can feel kind of {i}good{/i} sometimes."
    s "None of that is what I was trying to-"
    h "Are you “replenished” yet? Because it’s been more than five minutes since you said “five minutes” and all this talk about girls has made me {i}really{/i} fucking horny."
    s "..."
    h "..."

    scene black
    with dissolve2

    s "Turn around."
    h "Ooooh, is that your first command as my new master? Because we can get started on that part of my wishlist right away. I get that the second part might take a little time."
    s "I haven’t agreed to the second part yet, Haruka."
    h "Oh, I know..."
    h "But you will."
    h "You'll agree because you’re like me."
    h "You’re fucking scum."

    "Over the next ninety minutes, I fuck Haruka in every single room of the house. "
    "She climaxes twice in the living room, once in the bathroom, twice in the bedroom, once in the kitchen, and once in the foyer."
    "I fuck her outside of the house as well."
    "She couldn’t say no because I control her now."
    "I think I may have hoped that someone would catch us, but no one ever did."
    "And so now I must either abandon {i}her{/i} and save what little pride I have left-"
    "Or abandon {i}myself.{/i}"
    "And we all know which of those two options I will choose."
    "Because I am fucking scum."

    $ renpy.end_replay()
    $ harukadate30 = True
    $ harukapredator = True
    $ haruka_love +=1
    $ haruka_lust += 1
    stop music fadeout 7.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
    play sound "jackpot.mp3"
    "{i}Haruka has gained the “Predator” trait!{/i}"
    "{i}Good job!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label harukacamp1:
    scene harukanightbond1
    with dissolve2
    play music "thesleepingcity.mp3"

    s "Hey. Mind if I join you?"
    h "Well, well, well. Look who finally decided to give me the time of day."
    s "I’m pretty sure we’ve already crossed over to the time of night, Haruka."
    h "Then that just goes to show you how long you’ve been avoiding me."
    s "I’m not intentionally avoiding you. I just-"

    scene harukanightbond2
    with dissolve

    h "I know. I’m not hunting for an apology or anything like that."
    h "You were sort of a last minute addition to this trip in the first place, so it’s not like I’d been looking forward to spending time with you for weeks on end or whatever."
    h "Besides, you’ve got enough going on with Ami. If leaving me out of the equation helps you balance things out, so be it."

    scene harukanightbond3
    with dissolve

    h "I can wait a little longer."
    s "Bold claim for someone who gets lonely the second no one’s looking at her."
    h "It’s a little easier when the people I want to look at me aren’t in space."
    s "Your poor husband."
    h "Don’t bring him up right now. Let’s talk about {i}you.{/i} How did things go with your potentially demonic niece? You guys were gone for a while."

    scene harukanightbond4
    with dissolve

    s "Pretty good actually..."
    s "Apparently, she was already looking at me like some sort of father figure. And it was just {i}me{/i} who was holding that back from turning into anything bigger."
    h "I’m not surprised, really. With the way that girl talks about you, I had a hard time {i}ever{/i} believing you were {i}just{/i} her uncle."

    if harukasex == True:
        h "Of course, the fact that she very openly called me out on being an unfaithful slut may have played a part in me thinking she might like you a {i}little{/i} more than a standard relative. But I digress. "
        h "And I digress {i}because{/i} I am an unfaithful slut."
        s "But you’re {i}my{/i} unfaithful slut and that is precisely why I keep you around."
        h "I’d be quite offended to hear that if it weren’t for the fact that being degraded turns me on."

        scene harukanightbond2
        with dissolve

        h "But I digress again."

    else:
        s "What gave it away? "

        scene harukanightbond2
        with dissolve

        h "One of the many conversations I’ve overheard at the cafe where she talked about having your babies. Which isn’t really a thing someone should do with their father either. But hey, I’ve got some weird kinks too."

    h "You think things will get better from here on out?"
    s "Better how?"
    h "Like...do you think reevaluating your relationship with Ami will help you eventually find happiness outside of what your students keep beneath their skirts?"

    scene harukanightbond5
    with dissolve

    s "Maybe. But it’s not really my happiness I’m concerned about. I just want Ami to stop blaming herself for not being able to break my concrete shoes off as I slowly descend to the ocean floor."
    h "Don’t you think that goes both ways, though?"
    s "What do you mean?"
    h "I mean...she knows you better than anyone, doesn’t she? Which means she probably wants you to stop blaming yourself for the things that are drowning {i}her.{/i} You’re doing the same thing."
    s "But in my case, I’m actually making mistakes. And she’s-"
    h "Making mistakes too. She’s only human, Sensei. And making mistakes is what humans do."

    if harukasex == True:
        h "Like, just look at {i}us.{/i} Our entire relationship is a mistake. But it’s not like that’s stopping me from enjoying it while it lasts. "
    else:
        h "Like, just look at me. I practically threw myself at you not long after we first met and I’m already spoken for. But you’re one of my best friends now, and that wouldn’t have happened {i}without{/i} that mistake. You know?"

    s "I know. But still...she’s just a girl. She shouldn’t have to be thinking about all of this depressing shit so early in her life. So all I want to do now is try and...save her a little bit of anguish."
    h "Is that really {i}all{/i} you want to do, though?"

    scene harukanightbond6
    with dissolve

    s "Is there something else you think I should want?"
    h "I mean...you’re still kind of unemployed, aren’t you? "
    h "Rin says it’s been aeons since you’ve shown up at school. And I doubt spending so much time alone is doing much for your mental health, so...don’t you want to change at least {i}that?{/i}"

    scene harukanightbond7
    with dissolve

    s "..."
    h "Silence speaks volumes sometimes, Sensei."
    s "You know..."
    s "I think there was a time where I actually kind of enjoyed teaching. But, knowing me, I don’t really believe any of it was for the same reasons other people get into the field."
    s "Like...the girl who’s filling in for me right now. She seems to really love all of the girls in the class and she’s only known them a fraction of the time I have. It’s easy to tell that she, like...wants to make a difference."
    s "So even if she got into teaching for the wrong reasons, it’s the right ones that are keeping her around. And that’s...pretty obviously not how it was for me since you already know what I’m doing with some of those girls."
    h "Yeah, but you’ve neglected to tell me why you got into teaching in the first place. What do you mean by saying it wasn’t for the same reasons other people get into it?"
    s "I mean...I can only guess how I was feeling back then. "

    scene harukanightbond8
    with fade

    s "But I’m pretty sure it was to try and prevent anyone from winding up like me."
    h "I...don’t really get it. You decided to mentor people so...they {i}wouldn’t{/i} wind up like you? Isn’t that kind of backwards?"
    s "Maybe I worded that incorrectly. What I mean is more that..."
    s "There are certain ways you’re meant to act in this world. And doing things to set yourself apart from others is generally discouraged."
    s "But there are some of us who really want to do things like that and can’t seem to figure out how. "
    s "We want to fit in and we want to seem {i}normal.{/i} But we’re products of the way we’re brought up and, a lot of the time, we never have the chance to understand what we’re meant to do in the first place."
    s "I think what I wanted is to take what I’ve learned and share that with people experiencing something similar. So they don’t wind up roaming through life confused or lost like I did for so long before just...giving up."

    scene harukanightbond9
    with fade

    h "Wow..."
    h "I think that’s the most I’ve ever heard you say at once."
    s "Yeah, well...I’m sorry it all probably sounded like nonsense."

    scene harukanightbond10
    with dissolve

    h "Not at all. In fact, I think gaining this sort of...insight into your allegedly {i}misguided{/i} mind explains a lot really."
    h "I’ve never thought you were normal or anything like that. Which might sound like an insult, but it’s really not. And I think that’s why people like Rin and I gravitate to you because we’re not {i}normal{/i} either."
    s "Yeah but, in that sense, nobody is really {i}normal.{/i} And yeah, Rin’s an orphan — but I’d wager you had a pretty standard upbringing. Am I right?"
    h "More or less."

    play sound "static.mp3"
    scene harukanightbond11 with flash
    stop sound

    h "I did well in school. I had parents who fed me and put a roof over my head. The whole nine yards. And I sure as hell never slept with any teachers like Sara did."
    h "But look at me now, Sensei. Like, sure- I’m a somewhat successful business owner. I’ve got a roof over my head and a car and a group of friends I can go camping with on random Sundays whenever I want."

    if harukapredator == False:
        h "But I’m insanely lonely. I’m a borderline nymphomaniac. I send naked pictures of myself to teenage girls and pretend I never meant to. "
    else:
        h "But I’m also a predator who will not only bend to your each and every desire, but eat out teenage girls on beaches and finger myself to fantasies about you fucking my friends’ daughters."

    h "And I do all of that {i}with{/i} my “standard upbringing.” So maybe that’s less responsible for the way you are than you think. Just some food for thought."
    s "Fair point, Haruka."
    h "I can be pretty smart when I want to. Not just anyone can set their sights on opening a cafe when they’re a kid and then actually follow through with it. "
    s "You’ve wanted that cafe since you were a kid?"
    h "It was practically my dream. "
    h "I remember this one project we had to do in school one year where we needed to come up with a whole-ass business proposal. You know — blueprints...logo...everything. "
    h "And my pitch was basically Koi Cafe. Just, back then I think I called it Rainbow Cafe or...Sunflower Cafe or something like that. It was girly. That’s all I really remember."
    h "But, years later when I was less into pink and more into coffee, I rethought the base concept and landed on Koi instead."
    s "As in “love?”"
    h "As in the fish, actually."

    play sound "static.mp3"
    scene harukanightbond12 with flash
    stop sound

    h "Koi fish are linked to all sorts of symbolism because they’re beautiful and easy to, like...be poetic about, I guess. But to me, they’ve always stood for accomplishment. Or courage. Strength, even."
    h "And, I’m sure you’ve noticed this by now, but I’m kind of an overly sensitive piece of shit drama queen sometimes. "
    h "So choosing a symbol for the qualities I lack seemed like a way for me to trick myself into believing I might actually have them, you know?"
    s "I guess I never realized how much thought went into it. I always just saw it as some...normal cafe."
    h "It is! But it’s {i}my{/i} normal cafe."

    play sound "static.mp3"
    scene harukanightbond13 with flash
    stop sound

    h "It’s the symbol of all that hard work paying off. An actual, physical {i}thing{/i} that embodies the...great accomplishment of a girl my age {i}winning.{/i}"
    h "I never won at much when I was younger, Sensei. But I also never really had {i}time{/i} to win because I was thinking so much about the future. "
    h "I don’t have to do that anymore because I {i}like{/i} where I am. But, at the same time..."

    scene harukanightbond14
    with dissolve

    h "It’s things like this that make me worry about you since you don’t {i}have{/i} anything like that to remind you of all you’ve had to go through to get here."
    h "You {i}had{/i} the school. You {i}had{/i} your class. But now, you’re letting all of that drift away because you lost sight of why it was ever important to you in the first place."
    h "So maybe stop seeing it as a training ground for corrupting today’s youth and {i}start{/i} seeing it as a place where you {i}can{/i} connect with the people you want to connect with. Just like you used to."
    h "One thing I’ve learned from my time in the service industry is that {i}everyone{/i} has problems, Sensei. And some people like talking about those problems {i}way{/i} too much. "
    h "But what that really means is that there’s always someone who will need what you have to offer."
    h "And for me, that’s coffee."
    h "It’s a place for people to relax or refuel to prepare themselves for the hell that lies outside of my doors."

    scene harukanightbond15
    with fade

    h "And for you, it’s..."
    h "Actually...what subject do you even teach?"
    s "All of them."
    h "{i}All{/i} of them? Is that how they’re doing things over there now?"
    s "It might just be a budget thing, but...I just want to say — I think that was one of the most helpful things you or...anyone else has ever said to me."
    h "Like I said, I can be pretty smart when I want to. You probably just forget that since I’m always hanging out with Maki and Sara."
    s "Haruka."
    h "Hm?"
    s "I’m really proud of you."

    scene harukanightbond16
    with fade

    h "..."
    s "You really have done a lot to be proud of. And I’m glad you have something that serves as physical proof of that."
    h "Thank...you..."
    s "No problem. But why do you look so embarrassed all of a sudden when you just spent the last ten minutes essentially giving yourself the same compliment?"

    scene harukanightbond17
    with dissolve

    h "It’s different when it comes from someone else, obviously. Especially someone you look up to."
    s "Sure, but you only look up to me because I can get all of the girls that you can only dream of getting."

    scene harukanightbond18
    with dissolve

    h "There are other things too, you know! "
    s "Like what?"
    h "Like...the fact that you can withstand multiple apparent traumas when most people get taken out of commission by just one!"
    s "Haruka, I was {i}just{/i} stuck inside of my house for months. You shouldn’t look up to me just because I’m voluntarily stepping back out into the sun again."
    h "That was just one more thing! There’s also the part where...you’re caring! And cool!"
    h "In fact, practically {i}everyone{/i} looks up to you even though they probably shouldn’t!"
    s "You’re right. They should be looking up to you instead. "

    scene harukanightbond19
    with dissolve

    h "Ugh...{i}no.{/i} That’s wrong too. And it’s not what I’m saying."
    h "What I mean is more like...how do I even put this?"

    scene harukanightbond20
    with dissolve

    h "What I mean is that...it’s just kind of embarrassing hearing you say things like that since I never really...contemplated getting that sort of validation from you."
    h "It’s just surprising, that’s all."

    scene harukanightbond21
    with dissolve

    h "But...it makes me really happy."
    h "Almost happy enough to forget that you spent the first half of today hanging out with literally everyone else."
    s "Yeah...sorry about that."

    scene black
    with dissolve2
    stop music fadeout 20.0

    s "I’ll make sure to drop by the cafe again soon, though."
    h "Make sure it’s when I’m working..."
    h "I can show you how it compares to my old blueprint."

    "Haruka pours some coffee into small paper cups that the two of us sip from for the next fifteen minutes or so while lazily gazing up at the stars."
    "You can see so many of them out here."
    "And for once, it almost doesn’t hurt to look at them."

    if harukasex == False:
        "Haruka rests her head on my shoulder, but not in the way that would make it seem like she wants me more than she actually does."
        "I think she’s just happy to be here beside me."
        "And I think that if I put my arm around her now that she’ll interpret it the same."
        "And so I do."
        "And so she does."
        "And we both close our eyes."

        scene clearnightsky
        with dissolve2

        "But when I open mine another ten minutes later after dozing, I notice she’s gone. "
        "And so I must go as well."

        $ renpy.end_replay()
        $ harukacamp1 = True
        $ haruka_love +=1

        "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
        "What now?"

        jump campmenu2

    else:
        "Haruka rests her head on my shoulder."
        "Several minutes later, she looks up at me- silently asking for something else."
        "But it’s something I can not give her here."
        "It wouldn’t feel right beneath the magpies."

        scene clearnightsky
        with dissolve2

        $ renpy.end_replay()
        $ harukacamp1 = True
        $ haruka_love += 1

        "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
        "What should I do now?"

        jump campmenu2

label harukaspring1:
    scene harukunthesexpet1
    with fade
    play music "cafe.mp3"

    "Our scene begins with the protagonist (me) arriving at Koi Cafe thirty minutes after closing time and being allowed in anyway because fucking the owner of a small business earns you special privileges."
    "I really just want some coffee this time, though."
    "Just kidding. That’s a lie. I came here for Molly since she’s typically the night-shift girl and I would like her to perform fellatio on me again, but her boss works as well."
    "Which isn’t to say Haruka isn’t {i}good{/i} at it. I just don’t always want there to be crying involved in my sexual escapades. Especially when there’s so much of that already happening in my head. "

    h "I feel like you’re having a really depraved inner monologue right now that you’re not letting me in on for some reason."
    s "And what gives you that idea, Haru-kun?"
    h "The fact that you’ve been standing there and staring at me for roughly five minutes now. And also, stop calling me Haru-kun. "
    s "If you must know, I {i}was{/i} having a somewhat depraved inner monologue. But that is just a side effect of the current nature of our relationship, Haru-kun."
    h "Seriously, stop that."
    s "Blame Maki. She started it."

    scene harukunthesexpet2
    with dissolve

    h "As flattered as I am to be looked at in such a way, I’ve gotta say that I’m surprised you’ve gone back to your old self so flawlessly when you were a mess just the other day."
    h "I was also worried that our moment of bonding in the woods may have inadvertently made you want to fuck me less, so I’m happy to see that’s not the case."

    scene harukunthesexpet3
    with dissolve

    h "And I’m also happy to see that gaining a daughter has apparently increased your libido for reasons I can only {i}guess.{/i}"
    s "By “guess” do you mean “fantasize about when you’re alone in bed and waiting for me to come fuck you?”"

    scene harukunthesexpet4
    with dissolve

    h "Who says I wait until I get home? Maybe I-"
    s "{i}Ahem.{/i} It appears we’re no longer alone."

    scene harukunthesexpet5
    with dissolve

    mo "Well, that’s an extremely suspicious thing to say the moment a person shows up."
    h "Ignore anything you may have heard over the last fifteen seconds. Are you done with the dishes yet?"

    scene harukunthesexpet6
    with dissolve

    mo "Negative. I abandoned the task when I heard the echoing boom of the Herald’s voice and came to investigate."

    scene harukunthesexpet7
    with dissolve

    h "Funny. I don’t remember that being in your job description."
    mo "Salutations, Sir. I hope you are having a pleasant evening."

    scene harukunthesexpet8
    with dissolve

    s "It’s fine, I guess. How’s yours?"
    mo "Fine as well, Sir. Apart from being confined to the dreaded “dish cave.”"
    h "..."
    s "Is something wrong-"

    scene harukunthesexpet9
    with dissolve

    h "Come with me."
    s "What?"

    scene black
    with dissolve

    h "Just do it. No questions."
    mo "M-Magistrate? "
    h "Back to your cave, Molly! "
    mo "But...tonight is-"
    h "Don’t know, don’t care! We can’t go home until you’re finished with the dishes."

    play sound "doorslam.mp3"
    scene harukunthesexpet10
    with hpunch

    s "You know, you probably shouldn’t go around pulling people into bathrooms in front of your employees. It sets a bad-"
    h "Blah, blah, blah. Did you have sex with Molly?"
    s "How did you pick up on that after just like two lines of dialogue?"
    h "I have a knack for this sort of thing, okay? Plus, I see her enough that it isn’t weird if I pick up on minor changes in her behavior. "
    h "And those eyes, Sensei? Those were the eyes of someone who has had your penis inside of them. I know this because I also have those eyes."
    s "I’m suddenly very worried for probably half of the other girls who come into this store."
    h "Well you shouldn’t be because you’re going to help me fuck them all too. But that’s beside the point. Why didn’t you tell me?"
    s "Tell you what?"

    scene harukunthesexpet11
    with dissolve

    h "{i}That you fucked Molly, you idiot!{/i}"
    s "Oh. Because I didn’t."

    "Hopefully."

    scene harukunthesexpet12
    with dissolve

    h "Wait, what?"
    s "Yeah. She just put some wings on and gave me a blowjob. Normal teenage girl stuff."

    scene harukunthesexpet13
    with dissolve

    h "Well...that’s still progress though, right? Like you still went from no sexual relations to sexual relations. "
    s "Right. So don’t worry, your motherly yet predatorial instinct is still mostly accurate."

    scene harukunthesexpet14
    with dissolve

    h "Weird. And here I was expecting Rin to be the next in line. "
    s "And why would you expect that exactly?"

    scene harukunthesexpet15
    with dissolve

    h "Uhh...because she’s single now and finally able to fuck you?"
    s "When has being in a relationship ever stopped anyone from fucking me before?"

    scene harukunthesexpet16
    with dissolve

    h "Hey. It stopped me for almost a full week."
    s "You really are the world’s greatest wife, Haruka."

    scene harukunthesexpet17
    with dissolve

    h "Well, it’s not {i}my{/i} fault you’ve got the dick to end all dicks! I probably never would have gotten married at all if I knew you were right around the corner waiting to screw me!"
    s "I’m just going to reuse my last sentence here again."

    scene harukunthesexpet18
    with dissolve

    h "So, how was it?"
    s "How was what?"
    h "Don’t play dumb with me, Sensei. You know who I am now and you know what I want to hear."
    s "To be fair, I’ve known {i}who you are{/i} for a long time. I’m just new to sharing."
    h "And I’m new to prying."
    s "No you’re not."
    h "Okay, fair point. But still, you have information regarding the sexual experience of one of my employees. Withholding said information from their boss is illegal."
    s "I don’t think it is, Haruka."

    scene harukunthesexpet19
    with dissolve

    h "Just fucking tell me, damn it! I’m horny and I need to know!"
    s "Just ask her yourself. "
    h "I {i}can’t{/i} ask her myself! That’s the whole reason I need you in the first place!"
    s "Sure. But you also can’t say no to anything I command of you anymore."
    h "That’s only for sexual stuff!"
    s "Then ask her {i}naked.{/i}"

    scene harukunthesexpet20
    with dissolve
    stop music fadeout 20.0

    h "..."
    s "Strip."
    h "Is this a serious order?"
    s "It wasn’t meant to be at first. But now, I want to see just how much I can make you do. "
    s "Plus, if Molly’s open to experimenting with {i}me,{/i} maybe she’ll be open to experimenting with {i}you{/i} as well since you’re also an adult with some influence and authority in her life."
    h "Sensei."
    s "Yes?"

    scene harukunthesexpet21
    with dissolve

    h "Becoming your sex pet is probably the single greatest decision I have ever made. Thank you for forcing me to do the things I don’t have the courage to do on my own."
    s "So you’re really going to do it, huh?"

    scene harukunthesexpet22
    with dissolve

    h "How could I ever refuse an order from my master?"
    s "I’m not sure. I just kind of figured the fact that we’re {i}in your business{/i} right now might cause you to set some boundaries."
    h "We’re closed. And it’s not every day I get the opportunity to see a little girl suck my master’s big...{i}fat{/i} cock."
    h "You think she’ll play nice?"
    s "I have no idea {i}what{/i} she’ll do. We’ve only had one real experience together. "
    s "But I also know that she’s a pervert and might just rationalize this as a scene in one of those games she plays."
    h "So what’s the plan then? I take everything off and just walk up to her? Ask her how your cum tastes?"
    s "Bring her back here."
    s "Tell her I want to see her for something."
    h "Can I touch her?"

    scene black
    with dissolve2

    s "You can do anything you want with her if you can get her into this room. "
    h "I’ll drag her here myself if she won’t come willingly..."
    s "Yeah...don’t do that."
    h "Awww..."
    h "As you wish, master..."

    "........."
    "......"
    "..."

    scene harukunthesexpet23
    with dissolve2
    play music "asobeatsex8.mp3"

    "You know, this definitely wasn’t what I had in mind when I decided to come here tonight. But I guess it’s a realistic outcome at this stage in both mine and the world’s development."
    "Each day I spend forging bonds with these creatures is another step toward filling a large  room with their bodies and lining them up in some sort of conveyor belt."
    "At that stage, my collection will be complete and I’ll spend my days slaving over the belt like a mindless factory worker tirelessly attempting to fulfill an impossible quota."
    "I’ll move from one to the next, filling up their holes. Breeding them for offspring I could use to create another belt in the somewhat distant future."
    "But I guess it doesn’t have to be {i}too{/i} distant for me when I’ve made it apparent how much I prefer fruit before it’s reached ripeness."
    "That’s not to say I don’t indulge in {i}all{/i} types of fruit, though. Haruka is a perfect example of that."
    "Here we have a girl who, just several years ago (Or even fewer if you want to cancel out the flow of time here), was a happily-married and loyal woman with a spotless infidelity record."
    "Now, I have her stripped and marching over to a high school girl with the goal of taking her to me so I can use her to my heart’s desire."
    "And she is living for it."
    "She is no longer the loyal woman she once was. She’s a living symbol of how far I’m willing to go to destroy purity in its purest form. And that’s precisely what {i}she{/i} wants."
    "It works for both of us."
    "Because she no longer has to think for herself. "
    "And I no longer have to act for mine."
    "Or at least that’s how it will be tonight."

    h "Um...Molly?...Could you come here for a minute?"

    "I can hear her call out from my place in the bathroom. "
    "I’m not hard yet, but I assume that will change the moment I’m not alone with my thoughts anymore."

    scene harukunthesexpet24
    with dissolve

    h "It’s {i}reaaaaaally{/i} important...and I promise to make it worth your-"

    scene harukunthesexpet25
    with dissolve

    h "...huh?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene harukunthesexpet26
    with dissolve2

    h "..."

    "Haruka falls silent...and based on the lack of perverted shrieking, I can only assume the mission ended in failure."

    h "{i}Hah...{/i}"

    "I remain inside my own cave for a moment, unsure of whether or not she’d profit more off the shame in returning to me empty-handed or if she’d rather be confronted in the midst of her failure."
    "I’m sure she’ll get off on both of them. And that’s why it’s easy to be with someone like Haruka."
    "No matter what happens, whether it be good or bad, you can always count on her wanting to be ruthlessly pounded."

    scene black
    with dissolve2

    "So my emergence is decided, and I remove myself from the cave — aiming my feet at the only dark spot I can find in this fluorescent heaven."

    "........."
    "......"
    "..."

    scene harukunthesexpet27
    with dissolve2

    h "I hate video games."
    s "Did she really just leave without saying anything?"
    h "She does this all the time on Tuesdays. That’s why I’ve started working these night shifts too since I can never count on her to actually finish the job."
    s "And it just...hasn’t occurred to you to just switch her off the night shift?"
    h "She won’t wake up for the morning shifts. And I don’t want to just {i}fire{/i} her because-"
    s "Because you want to fuck her."

    scene harukunthesexpet28
    with dissolve

    h "Exactly."
    s "Well...I’m sure there will be more chances in the future. She seemed really into it the other night, so I can only imagine how excited she’d be with another girl involved."
    h "Do you think I’m a bad boss, Sensei?"
    s "Absolutely."

    scene harukunthesexpet29
    with dissolve

    h "Yeah, I don’t know why I even asked that."
    s "You could be worse, though. You’ve never willingly thrown yourself at any of your employees."
    h "Yeah, all I’ve done is send them pictures of my boobs."
    s "Oh, right."
    s "Yeah, I guess you really do just suck then."

    scene harukunthesexpet30
    with dissolve

    h "I’m sorry for failing you, Master...I can only imagine how badly you wanted to {i}fuck{/i} Molly’s cute little mouth again...and I had to go and ruin it..."
    s "It can’t be helped. Sometimes, being a nerd just causes people to miss out on things."
    h "Are you going to punish me?...For not doing what you asked?..."
    s "..."

    scene harukunthesexpet31
    with dissolve

    h "I’ll just..."
    h "Bend over the counter and let you do as you please with me..."

    scene black
    with dissolve2

    "I guess ending this night {i}without{/i} sex was never a possibility at all."
    "And yes, I’m a little let down by the absence of a threesome-"

    scene harukunthesexpet32
    with dissolve2
    play sound "dosex.mp3"

    "But I still get to sink my cock into a horny bitch at the end of the day. And that’s far better than jerking off into a bundle of napkins while illuminated by the blue glow of a computer monitor."

    h "Ahh! [harukamaster]! I’m sorry! I’m...so sorry you...have to settle for my...loose...slutty...pussy!"

    "It’s not “loose” at all but I let her believe that since she always clamps down a little harder when she says it."

    s "You’re not wet for {i}me{/i} at all, are you? You were just excited to watch a little girl cum. "
    h "That’s...hah...not...true! I love...my [harukamaster]’s cock! I...hah...just wish...my...pussy....deserved it! I’m a bad...pet! I’m...a bad...girl!"
    s "At least you know your place..."
    h "Hah! Hah! Yes! I...don’t deserve...love! I’m just...a hole! A...desperate fucking...cum dumpster! I’m not...good for anything...but sex!"

    "Haruka’s legs tremble as I violently assault her pussy from behind. And I can’t help but silently commend her for being able to take such a beating even if it’s been a while since we last did this."
    "My hands grip her ass, pulling her harder into me while reveling in the sensation of the fresh sweat forming on her body as I use it to my heart’s content. "
    "Items begin to fall off of the counter..."
    "The cash register opens when one of our limbs bumps into it..."
    "A few pastries get knocked off of a display not far from where we’re fucking..."
    "And the sound of the door opening just adds one more sound to the chaos that is-"

    play sound "static.mp3"
    scene harukunthesexpet33 with flash
    stop sound

    "Wait, what?"

    h "Ah! Ahh! Harder, [harukamaster]! Fuck my...slutty pussy with your...giant cock! Cum in me! Breed me! Make me yours!"
    malec "What the fuck is going on in here?"
    h "Aaah! Aaah! Aaaah! Deeper! Fuck me...deeper!"
    s "Uhh...Haruka?"
    h "Don’t stop! Don’t stop! Harder!"
    s "There’s...a customer..."
    h "Haaah! Haaah! Sorry! We’re closed! "
    malec "And? You really think I’d want to order from a business where the employees are having sex on the countertops? Are you insane?"
    h "Haaah! Hah! Nooo! I’m just...a filthy whore!"
    s "Maybe we should-"
    h "Don’t...stop! Need...to be punished!"
    malec "This is completely insane! What’s your name? I’ll be including it in my complaint to the Better Business Bureau."
    h "Haruka...Hamasaki! Don’t tell...my husband!"
    malec "{i}And{/i} you’re married?! "
    h "That’s...right! I’m fucking...another man! While...{i}another{/i} man watches! I’m such a whore! I’m such a...fucking whore!"

    scene harukunthesexpet34
    with dissolve

    femalec "What’s going on, dear? Are they open after- oh. "
    femalec "Well, that’s just unsanitary. "
    h "Aaah! Aaah! Now...there’s another watching! Oh fuck! [harukamaster]! I’m gonna cum! You’re gonna make me...cum!"
    femalec" How come we never do it like that anymore?"
    malec "Is that really all you have to say about this?! They’re having sex right on the counter!"
    h "Aaaaah! Just...like that!"
    femalec "Yes but, in their defense, we {i}are{/i} here after regular business hours."

    scene harukunthesexpet35
    with hpunch

    h "AaaaaAAAAAaaaaaAAAAHHHHH!!!!!!!!!!!!!!!!!!"

    "Haruka convulses as I continue to slam into her but, at this point, what else am I going to do?"
    "We’ve already been caught. It’s not like I can just {i}un-fuck{/i} her. And all we can really do at this point is be thankful it wasn’t someone we know who found us."

    scene harukunthesexpet36
    with dissolve

    h "More...give me more...keep...punishing me!"
    s "But-"
    h "Let them watch! Let...the whole world know I’m a...thirsty bitch! Don’t even...think of taking that big cock out of me, [harukamaster]!"
    malec "That’s it. We’re leaving. Come on."
    femalec "..."
    malec "I said come on!"

    scene harukunthesexpet37
    with dissolve

    femalec "Ugh. You’re such a prude sometimes. You never want to try anything new."
    malec "I {i}will{/i} be filing a complaint! This place is a disgusting excuse for a cafe!"

    "The couple leaves and I realize that this probably only happened in the first place because Molly didn’t lock the door. "
    "So hey, maybe this is divine karma for me attempting to have Haruka coerce her into a threesome with two adults."
    "Regardless, they would have probably seen us either way since the walls of Koi Cafe are less {i}walls{/i} and more just...windows."
    "Which makes me all the more worried that someone might be watching {i}me.{/i}"

    h "Ooooh fuck! Yes, [harukamaster]! Fuck me! Fuck my...filthy little hole! Fill me up! Cum in me! Punish me!"
    s "..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "I guess I’m less okay with that than I thought."
    "So maybe that whole “conveyor belt” thing needs to go on hold for now as I attempt to figure out more about why I feel the way I do."
    "About why I put myself into situations like this only to turn into a statue once the worst becomes reality."
    "But kudos to Haruka for sticking to her guns, I guess. That or being so deliriously caught up in the moment that she didn’t even understand what was happening."
    "I’m sure that won’t come back to bite her in the future."
    "But the future will come the moment I’m no longer submerged in the depths of a hotwife. "
    "So I swallow my pride as Haruka’s gaping hole of unfaithful depravity swallows my cock."
    "And I empty myself out inside of her while the rest of me floats through the darkness and back into the type of home she’ll never have."
    "Unless she gets lucky, of course."
    "But sometimes, it feels like I’ve absorbed all of the luck that anyone here could ever have — both good {i}and{/i} bad."
    "And sometimes, I can’t help but view the ones I choose to fuck as something somewhat subhuman."
    "That’s how I unintentionally justify leaving her on the floor of her beloved business with cum dripping out of her slit and onto the tile floor."
    "That’s how I choose to forget."
    "If only I could apply that logic to where it matters most."

    $ renpy.end_replay()
    $ harukaspring1 = True
    $ haruka_lust += 5

    "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label harukaspring2:
    scene sky
    with dissolve2
    play music "cafe.mp3"

    "Every once in a while, I’ll wake up before I’m supposed to. "
    "Which isn’t to say I’m governed by a strict morning curfew that Ami has laid out or anything of the sort. Just that I like to pretend the world isn’t real until at least 8:00 AM."
    "So, as far as I’m concerned, the fact that it’s barely past 7:00 makes me feel as if I’m wandering through an unsettling liminal space tucked somewhere between Kumon-mi and whatever Yasu’s death plane is."
    "Suffice it to say, I regret having gotten out of bed and I regret deciding that I want coffee. Specific coffee from a specific shop a decent ways away from my house at that."
    "So here I am at Koi Cafe — home of the [[copyrighted frozen beverage] and a staff of young girls that could set any future (or present) criminal’s heart ablaze."
    "Except the “closed” sign is hung up and there’s not a single customer to be seen apart from me, who is only {i}sometimes{/i} a customer in the first place."

    scene black
    with dissolve2

    "Regardless, I spot Haruka and Rin inside and decide to enter, exercising my secret ability of basically never encountering locked doors."
    "........."
    "......"
    "..."

    scene harukacaferegret1
    with dissolve2

    h "UUUUUUUUUUUUUUGHHHHHHHHH..."
    r "Hey, chill. I’m sure everything will be fine. You’ve just gotta...you know...clear things up with the BBB."
    h "I had no idea they even operated in Japan! And I hate having to deal with all of that bureaucratic stuff! Just let me make coffee in peace!"
    s "Is something wrong?"

    scene harukacaferegret2
    with dissolve

    r "When the hell did you get here?"
    h "Everything is wrong! And it’s all your fault!"
    h "Just not really. And don’t get mad at me for blaming you this time because I’m only half serious. But UGHHHHHHHHHH! FUCK!"
    s "Rin, since Haruka appears to be in a state of disrepair, would you mind explaining to me what’s going on here?"
    r "Somebody filed a fake complaint to the Better Business Bureau about a couple having sex in the cafe and-"

    scene harukacaferegret3
    with hpunch

    r "OH MY GOD IT WAS YOU TWO, WASN’T IT?!"
    s "Well, that didn’t take you very long to figure out."
    r "Could it really not wait?! Is your lust that powerful?!"
    s "Haruka’s lust is that powerful. I showed up to get a drink and she attacked me. The only thing I could do to defend myself was fuck her into submission."

    scene harukacaferegret4
    with dissolve

    h "Okay. {i}Now,{/i} I’m blaming you."
    r "Sensei, this is serious! The cafe could get shut down because of this and I literally {i}just{/i} got a promotion!"
    r "Imagine how my resume will look if I have to put “Supervisor for one week at a cafe that got shut down due to sexy stuff.”"
    r "Everywhere I apply to after this will think {i}I{/i} leveraged my power to do the sexy stuff! Think of my future!"
    s "You know you could just...leave out that last part, right?"
    r "And lie on my resume?! What kind of adult are you?!"
    h "The kind that convinces innocent shop owners to strip naked and bend over the counter so he can fuck them doggystyle in front of customers!"

    scene harukacaferegret5
    with dissolve

    r "That’s literally insane! Please provide more specific details or I’ll have no choice but to not believe you!"
    h "My life is over. My career is over. We have customers who know I’m married. It's only a matter of time before word spreads all the way up into space and my husband finds out."

    scene harukacaferegret6
    with dissolve

    r "Well, maybe you should have thought about that before having sex with another man at your workplace! Were you {i}asking{/i} to get caught?! Because that’s what it sounds like!"
    h "We were closed for the night. Molly forgot to lock the doors. No one was ever supposed to find us."

    scene harukacaferegret7
    with dissolve

    r "The walls are made of glass, you idiot! Of course people were going to find you!"

    scene black
    with dissolve

    "I pull up a chair, knowing full well that this isn’t going to be a discussion I can just back away from. And no, it’s not {i}just{/i} because I played a role in the scenario that landed Haruka in hot water."
    "It’s because I care about this place. And I know how much it means to her."
    "She's worked toward owning this cafe for her whole life, and I’m not about to sit idly by and watch as it’s taken from her because she is a cheating whore who is addicted to my penis."

    scene harukacaferegret8
    with dissolve2

    h "{i}Hah...{/i}you must think I’m a failure...don’t you, Rin?"
    r "Noooo...I don’t think you’re a failure, Haruka. I think it’s perfectly reasonable to have sex with my teacher on the counter where we serve customers. That’s a really...normal thing to do."
    h "I’m never having sex again..."
    s "Hey now, let’s not get too hasty here. "
    s "Sure, what we did was kind of stupid in hindsight. But I’ve had a lot of dangerous sex over the last few years and it’s only rarely resulted in negative consequences. There was no way we could have known."

    scene harukacaferegret9
    with dissolve

    r "Again! Glass windows! You don’t even live that far from here! You could have had all the sex you wanted at home!"
    s "But that’s where Ami lives."
    r "Then you could have done it in my room while I pretended to be asleep! There were a zillion options beside the Koi Cafe lobby!"
    s "But none of them seemed as exciting and Haruka needed to be immediately punished for failing a task I gave her."
    r "What does that even mean?!"

    scene harukacaferegret10
    with dissolve

    h "I gave him complete control over my body and he used it against me."
    s "Wasn’t that sort of the whole point?"
    r "C...Complete control? What do you mean by “complete control?”"
    h "It means that I have to do what Sensei says any time he wants me to do something sexual with zero limits whatsoever."
    r "So...if he asked you to, like...do stuff right now..."
    h "Yup."

    scene harukacaferegret11
    with dissolve

    r "I don’t believe that. I’m going to have to see it in action to know that you two aren’t just messing with me."
    h "The power is in your hands, Sensei."
    s "As great as that sounds, I really feel like this is the actual {i}worst{/i} time to utilize that power. You know, since this is the {i}exact thing{/i} you just got in trouble for."

    scene harukacaferegret12
    with dissolve

    r "R...Right! We need to come up with some sort of gameplan about how we’re going to get out of this mess. "
    h "How am I supposed to make a gameplan? The only thing I’m good for is sex. "
    s "She {i}is{/i} very good for sex. She’s not wrong."
    h "See?"
    r "That’s Sensei’s penis talking. You’re good for tons of stuff, Haruka. And when you’re not getting railed next to all the pastries, you’re a really great boss."

    scene harukacaferegret13
    with dissolve

    h "You really mean that?..."
    r "Of course. And I’m going to do everything {i}I{/i} can to get you out of this. Mark my words."
    s "I know my track record concerning decisions both made and proposed within this cafe has not been great lately, but maybe it’s a {i}bad{/i} idea to get the high school girl involved in an active sex scandal."
    h "Sensei’s right, Rin. I appreciate the concern, but this is something I’m going to have to figure out on my own. Just do whatever you can to...not let the rest of the girls find out about this, okay?"
    h "It’s just one person’s complaint right now. And I’m not sure how this is supposed to be {i}investigated,{/i} but the fewer people who know what’s going on, the better."
    r "What should I tell them then? Because I was supposed to send out the new schedule this morning. "
    h "Just tell them we’re having...renovations done or something. I don’t know. If anything, they’ll probably all be excited to have off."
    r "Got it. I’ll head over to the office and come up with something now."

    scene harukacaferegret14
    with dissolve

    r "Sensei, can I leave you alone for a few minutes without you commanding Haruka to bend over again?"
    s "I don’t know. She was wrong to ever give me this power in the first place and I don’t understand why she doesn’t just take it away."
    h "The only thing I regret is getting caught. We should have done it in Rin’s room like she said."
    s "If only we had known back then."

    scene harukacaferegret15
    with dissolve

    h "Is the offer still on the table?"
    r "Forget the offer, Haruka! If you’re not going to let me get involved, the least you can do is snap out of horny mode and figure out a way to get our cafe back! Got it?!"

    scene harukacaferegret16
    with dissolve

    h "{i}Hah...{/i}Yeah...I’ve got it. I’m sorry you have to deal with this, Rin. If I had known earlier, I never would have had you come in."
    r "It’s fine. Just...let me know if you need anything. "

    scene black
    with dissolve2

    r "I’ll be in the office if you need me."

    "........."
    "......"
    "..."

    scene harukacaferegret17
    with dissolve2

    h "Man...I can’t believe that guy actually filed a complaint. How miserable does your sex life have to be for you to to cry about another couple boning in what was very obviously a closed business?"
    s "His wife seemed pretty fine with it, too. "
    h "His penis is probably small. He probably saw yours and got jealous."
    s "I think it was a little too deep inside of you for anyone to see, Haruka."
    h "Yeah, you’re probably right..."

    scene harukacaferegret18
    with dissolve

    h "God, that was so hot."
    s "But now we must face the consequences."

    scene harukacaferegret19
    with dissolve

    h "No, {i}I{/i} must face the consequences. {i}You’re{/i} fine. {i}You{/i} didn’t break any laws."
    s "Well...did you? Because I’m not really sure how any of this works. Was what we did actually illegal?"
    h "I’m not sure. Public indecency maybe? Do I need to get a lawyer? What if they come onto me? You know how easily I crumble for people in positions of power."
    s "I’m a teacher, Haruka. I’m not really in a position of power to anyone but my students."
    h "Whatever, man. I’m just lost and confused and also horny again but {i}now{/i} I can’t even do anything about that because I have to be an adult."
    s "Yeah...but you {i}are{/i} an adult. And I get that you’re really into this sex slave thing, but maybe it would be smart if we toned it down for a little and started rethinking just what we {i}should{/i} do and what {i}not{/i} to do."
    h "If we start doing that, we’d have to end the whole thing since it’s built almost entirely on the concept of doing horrible things to people we shouldn’t be doing them with."
    s "Fair. But that’s not what we’re talking about right now."
    h "It’s not? I’m confused."
    s "Just...do your best to explain the situation. What comes next and what do we need to do?"

    scene harukacaferegret20
    with dissolve

    h "It says here that they’re going to send someone in to “investigate the issue.” But whatever that means, I have no idea."
    h "They’re also requesting all surveillance footage from the cafe and any business that has cameras aimed toward it."
    s "Do you have cameras in here?"
    h "I do, but they were turned off when we were having sex. Which at first I was very upset about, but am now very thankful for. I have no idea what that means for the other businesses around here, though."

    scene harukacaferegret21
    with dissolve

    h "I’m friendly with a few of them and think it {i}is{/i} possible that one of them might have caught something given how huge the cafe is..."
    h "But I don’t really know how I feel about walking into any of those places and asking them if they saw me getting fucked in my store and, if they did, to scrub the footage of it."
    s "Do you want me to do it?"
    h "I don’t see how that’s any better."
    s "It would save you the shame, at least."

    scene harukacaferegret22
    with dissolve

    h "The shame is what I’m {i}least{/i} worried about at this point. I just don’t want anything happening to the store."
    h "I love this place. And without it, I wouldn’t {i}just{/i} be broke. I’d be lost. And the same goes for girls like Rin who rely on it for work experience and money."
    h "Come to think of it, though. It’s probably {i}only{/i} Rin who would {i}really{/i} care. The rest of the girls probably couldn’t care less."
    s "I’m sorry, Haruka. I shouldn’t have given you any commands while we were in here."

    scene harukacaferegret23
    with dissolve

    h "And I shouldn’t have gone along with them. Even if that was arguably the hottest night of my life."
    s "It {i}was{/i} pretty great, wasn’t it?"

    scene harukacaferegret24
    with dissolve

    h "Getting fucked in front of strangers? Admitting it’s with someone other than my husband? Knowing anyone {i}else{/i} could show up at any moment? Like, holy shit. So many fantasies checked off at once."
    s "Want to do it again right now?"
    h "Yes please."
    s "Have you learned absolutely nothing, Haruka?"

    scene harukacaferegret25
    with dissolve

    h "Aaaaaaah no! I can barely remember what life was like before I was a sex-crazed harlot! This seriously sucks, Sensei! I have no idea what to do!"
    s "I’m sure you’ll be fine, Haruka."

    scene harukacaferegret19
    with dissolve

    h "But how can you be {i}sure?{/i} This is uncharted territory for both of us."
    s "It just sounds to me like, so long as no one {i}else{/i} has any footage of that night, it’s your word against his. It’s not like they can shut you down over one guy’s complaint if {i}he{/i} doesn’t have any evidence of it."
    s "The worst that can happen is that word just...gets around or something. But even then, you could just say it’s a shitty rumor. Maybe even sue the guy for defamation or something if it affects your business."

    scene harukacaferegret26
    with dissolve

    h "He’d deserve it too. Limp-dicked loser."
    s "And hey, on the bright side, if word {i}does{/i} get around and you wind up attracting a bunch of attention from people who want to come here and see the barista who {i}allegedly{/i} gets fucked inside of her own store..."

    scene harukacaferegret27
    with dissolve

    h "I’d feel so embarrassed and objectified...and ashamed..."

    scene harukacaferegret28
    with dissolve

    h "I’d never stop being wet again."
    s "{i}Now{/i} you’re thinking like the Haruka I know."
    h "Is it bad that I’m kind of {i}hoping{/i} for that outcome now?"
    s "Yes."

    scene black
    with dissolve2

    s "But that’s exactly why I like you."

    "Haruka and I spend the next few minutes going over the notice she received before she decides that she {i}will{/i} check around with the other businesses to see if they caught anything on tape."
    "What that unfortunately means, though, is that the cafe is going to be closed for a little while."
    "Haruka claims she can probably get away with keeping it open while the investigation is active, but she thinks it’d be better for everyone if, at least for now, the doors remain shut under the guise of renovations."
    "She says she’ll keep me updated on the progress of everything, but...considering it’s still early and I have nothing left to do now, I have to come up with some other way to kill time while everyone else is asleep."
    "That being said, I call out to Rin from the lobby as Haruka prepares for her walk of shame and decide to spend the rest of the morning killing time with my {i}other{/i} favorite barista."

    $ renpy.end_replay()
    $ harukaspring2 = True
    $ cafeclosed = True
    $ haruka_love += 1
    stop music fadeout 15.0

    jump rinspring3

label harukaspring3:
    scene clearnightsky
    with dissolve2
    play music "justlights.mp3"

    "Just one time I’d like to think//I’m right where I belong."
    "A perfect fit for where I am//the last line of a tune."
    "Sometimes, we might make mistakes//or use improper words."
    "That doesn’t mean we’ll never fly//since after all, we’re pelicans."

    scene nightsky
    stop music

    s "Being around teenagers is exhausting."

    "I step on a bug."

    play sound "sound.mp3"

    s "Ew, gross."

    "It begins to stir."

    scene nightskybutwithabug
    with dissolve2

    tbiso "Why would you do that?"
    s "Sorry. You were in the way."
    tbiso "I can literally fly."
    s "So can I. You just haven’t seen it yet."
    tbiso "What’s your name?"
    s "Akira. What’s yours?"
    tbiso "Tebiso."
    s "That’s a weird name."
    tbiso "It’s more of a mnemonic device so you can remember my call sign in the code."
    s "Oh. Well, thanks."
    tbiso "Why are you so useless?"
    s "What?"
    tbiso "You’ve been here for so long and have accomplished nothing."
    s "That’s not true. I’ve helped a lot of people."
    tbiso "But they’re still only here for one reason."
    s "That’s not true either. I’m a useful boy."
    tbiso "How many times did she call you last night?"
    s "What?"
    tbiso "Six."
    tbiso "You answered none of them."
    tbiso "It could be her last one."
    s "Okay, Tebiso. Thank you for being a bug."
    tbiso "Thank you for not killing me."
    tbiso "There are so many ugly things left for me to see here."

    stop sound fadeout 3.0
    scene nightsky
    with dissolve2

    "Tebiso leaves."
    "No one understands again."

    play sound "rimshot.mp3"
    $ renpy.pause(2, hard=True)

    "Thank you. I’ll be here for five more years."

    play sound "static.mp3"
    scene wintersky with flash
    stop sound

    "My phone begins to- no, I don’t want to write a snow scene."

    play sound "static.mp3"
    scene nightsky with flash
    stop sound

    "Yeah, this will have to do."

    play sound "phonering.mp3"

    "My phone begins to ring because I’m a popular guy with a huge penis."

    play sound "phonebeep.wav"

    s "Hello?"

    "I answer it. Because I’m a popular guy with a huge penis."

    play music "ame.mp3"

    h "Hey! What are you up to right now?"
    s "Just stepping on some bugs. How about you?"
    h "Celebrating! Because I just got the okay from the Produce Delivery Administration to resume business at the cafe tomorrow."
    s "Why does your cafe fall under their jurisdiction? Coffee is not a vegetable {i}nor{/i} a fruit."
    h "Yeah, but they preside over pretty much every single small business issue in Kumon-mi. It’s a whole thing. But yeah! We’re good to go!"
    h "I {i}would{/i} like to make a formal request that you don’t order me to fuck you in front of customers anymore, though. Unless you plan on financially supporting me as a result of what may come afterward."
    s "I’ll think about it. Niki’s living at my place now and is more inclined to have a threesome with someone who isn’t still in high school, so this may prove beneficial to me in the long run."
    h "I win either way, so I don’t really care. Are you busy tonight? Or do you want to come celebrate {i}with{/i} me?"
    s "As in have sex with you?"
    h "I was thinking more something along the lines of dinner."
    s "Great idea. It makes way more sense to have sex in someone {i}else’s{/i} business so {i}you{/i} can’t get in trouble."
    h "I don’t really think that’s how it-"
    s "I’ll be there soon."

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone because I’m a popular guy with a huge penis."

    play sound "static.mp3"
    scene popularguyhugepenis1 with flash
    stop sound

    "And then I arrive at Haruka’s place. Because I’m a popular guy with a huge penis."

    h "Hey! That was quick."
    s "I’ve been practicing teleportation magic off-screen."
    h "Well, I guess I’m glad to hear that I’m not the only one who’s been busting my ass lately. Turns out, having sex inside of a coffee shop is pretty serious business when other people wind up seeing you."
    h "Like, do you have any idea how many {i}forms{/i} I had to fill out in order to-"
    s "Take your shirt off."

    scene popularguyhugepenis2
    with dissolve

    h "Okay!"
    s "Wow. Not even a second thought."

    scene popularguyhugepenis3
    with dissolve

    h "There’d probably be a second thought if we were anywhere else. And I’d probably still go along with it anyway because I’m an insatiable, unfaithful whore. In {i}my{/i} castle, though? {i}Never{/i} a second thought."

    scene popularguyhugepenis4
    with dissolve

    s "Call yourself a whore again."
    h "I’m a filthy fucking whore."
    s "Tell me how much bigger my dick is than your husband’s."
    h "It’s not even close. I doubt I’d even feel anything if he tried to fuck me at this point."
    s "Now recite the entire Pledge of Allegiance, but do it while you’re masturbating."

    scene popularguyhugepenis5
    with dissolve

    h "Can I look up the words?"
    s "No. Do it from heart."
    h "Uuuuuuuuuhhh-"
    s "Haruka, I’m fucking around. Stop doing everything I say without any hesitation whatsoever."

    scene popularguyhugepenis6
    with dissolve

    h "Don’t command me to not take your commands! It’ll hurt my brain and I want to turn that off tonight! I’ve worked hard lately and deserve rest!"
    s "Yeah...I can’t imagine that’d be an easy situation to handle. And I {i}am{/i} sorry for ultimately forcing it on you."
    s "But hey, on the bright side, I’m sure the humiliation of asking all of your neighbors if they caught anything on camera was the ultimate form of sexual torture for you."

    scene popularguyhugepenis7
    with dissolve

    h "I will admit that it was pretty great up until I had to explain to a 95 year old woman what “doggystyle” was. That was just shameful."

    scene black
    with dissolve

    s "Well, you can tell me more about it over here. Teleportation is tiring and I need a break or I’m going to collapse."
    h "Of course! Do you want coffee? Tea? A blowjob? All three at once?"
    s "Coffee and tea at the same time? Are you out of your mind? Finish taking your shirt off and get over here."
    h "Yes, [harukamaster]. Anything for your attention."

    scene popularguyhugepenis8
    with dissolve2

    "Haruka cuddles up against me on the couch and, if I was capable of seeing anything other than her boobs right now, I imagine she’d look pretty adorable."
    "The ways her eyes latch onto mine make her look more like a puppy waiting to learn new tricks which, honestly, also explains her recent behavior in an eerily accurate manner."
    "This is enough for now, though. Celebrating how destructive uninhibited sex can be by having hardcore sex with each other seems like a little much, even for me."

    s "So, what did this 95 year old woman have to say once you finished lecturing her on the ins and outs of doggystyle sex? Pun somewhat intended."
    h "At first, she just shook her head. But then she congratulated me on my husband returning and I...admittedly did not have the heart to tell her she was wrong."
    s "That’s fair. Guess I’m just your new husband now."
    h "Want me to file for divorce with the real one?"
    s "I feel like that would be an abuse of power because I know you’d actually do it."
    h "Frankly, I like the guilt. I’m all in on being a traitorous bitch now. But if {i}you{/i} ever start to feel like too much of a homewrecker-"
    s "How did everything else go? With the PDA and getting the cafe open again?"

    scene popularguyhugepenis9
    with dissolve

    h "Okay. Just {i}ignore{/i} that thing about being a homewrecker then. We both know what you really are. And we both know it’s why we have so much fun-"
    s "Haruka. Focus."

    scene popularguyhugepenis10
    with dissolve

    h "What, do you actually {i}care{/i} now?"
    s "Of course I do. You’re really important to me."

    scene popularguyhugepenis11
    with dissolve

    h "I...am?"
    s "Did your nipples just get harder?"
    h "Something else happened too."
    s "So you love being humiliated {i}and{/i} complimented. Fun."
    h "I just love attention. I don’t care what kind."
    s "Well...whatever the case, I’m glad you figured things out. I know how much that place means to you and I’m sorry this ever happened in the first place."
    h "..."
    s "What? Why are you just looking at me?"
    h "Because I’m confused. Don’t you want to fuck me? You made me take my shirt off and everything."
    s "Yeah, because wearing that tanktop was a crime. I regret nothing."
    h "You shouldn’t. I wore it on purpose so you {i}would{/i} do that. I just didn’t think you’d then proceed to feign interest in the bureaucratic process of restoring order to my business."
    s "I’m allowed to be interested in things that {i}aren’t{/i} sexual, you know."
    h "I do. Just...you normally {i}aren’t.{/i} So I hoped we’d be able to go crazy tonight."
    s "Didn’t you say you wanted to go out to dinner?"
    h "{i}Yeah.{/i} Because I wanted you to be like “you can eat this dick” or something and then fuck me in the mouth until I pass out. I never expected that to actually {i}happen{/i} once I broke out the skimpy tanktop."
    s "So what you’re saying is that you want it so badly that actually going out to a restaurant would be borderline torturous for you."
    h "Yeah, but-"

    scene popularguyhugepenis12
    with dissolve

    h "Ohhhhh, I see what you’re up to. You just want to make me even hornier than I already am."
    h "Well joke’s on you, buddy! Because it’s not {i}possible{/i} to be hornier than I am right now."

    play sound "static.mp3"
    scene popularguyhugepenis13 with flash
    stop sound

    h "..."
    s "..."
    h "I was wrong. Please fuck me."
    s "Skipping straight to dessert isn’t good for your health, Haruka."

    scene popularguyhugepenis14
    with dissolve

    h "But I worked so haaaaaaaard!"
    s "Relax. It’s not like I’m firing you as my sex slave or anything."
    h "That sounds like foreshadowiiiiiiing! I don’t like iiiiiiit!"
    s "Are you going to act like a child all night or just until you get it all out of your system?"

    scene popularguyhugepenis15
    with dissolve

    h "I meannnnnnnn..."
    s "You know...I’m glad I found you, Haruka. You’re one of the only people in this city who’s even hornier than me."
    h "I’m still making up for lost time with the whole MIA husband thing."
    s "You’ve been making up on that time for longer than he’s been away now."
    h "Pedantics. Sex good. Me like. Want lots."

    scene popularguyhugepenis16
    with dissolve

    h "Who else is in the running, though? For the “horniest person in Kumon-mi?” Sara? Maki? Any of your {i}students?{/i} Rin’s gotta be high up, right?"
    s "Mmm...no. I think she’s more love-drunk than horny most of the time."
    h "She {i}totally{/i} wants to fuck you."
    s "Right. But she {i}hasn’t.{/i} And if she was really {i}that{/i} horny, she would have fallen victim to her own desires by now."
    h "Sooooo? Who has her beat then?"
    s "You want me to make a whole list?"
    h "Complete with pictures, if you could. I’m much better with faces and, in this case, {i}bodies{/i} than I am with names."
    s "Well, there are two who come to mind right away and you already know both of them."
    h "Soooo Molly {i}and-{/i}"
    s "{i}Not{/i} Molly, actually."

    scene popularguyhugepenis17
    with dissolve

    h "{i}Not{/i} Molly? That’s a plot twist if I’ve ever heard one."
    s "You’d understand if you’ve ever had sex with Chika."

    scene popularguyhugepenis18
    with dissolve

    h "{i}Really?{/i}"
    s "That girl would literally ride me to death if I let her. I have to force her off most of the time because I fear for my health."
    h "Wow. But she seems so wholesome and nice in person."
    s "Yeah, well wait until you find out that the other one is Sana."

    scene popularguyhugepenis19
    with dissolve

    h "Sana..."
    h "{i}Sara’s{/i} Sana?..."
    s "That’s right."
    h "My...number one teenage fantasy, Sana?..."
    h "Tiny, adorable, quiet Sana?..."
    h "Sana, “I’d throw my greatest friendship into jeopardy for the chance to even {i}touch{/i} you” Sana?"
    s "That’s the one."
    h "And..."
    h "And you..."
    s "Took her virginity on my couch the other day."
    h "..."
    s "But even before that...just the things she’s said and...the way she looks at me?"
    s "She’s been touching herself {i}constantly{/i} for the last few years. I’d be shocked to hear it wasn’t multiple times a day. Like, she’s the one who straight up jumped into my lap and-"
    h "You’re not...selling that couch, by any chance...are you?"
    s "No, Haruka. I am not {i}selling{/i} my couch."

    scene popularguyhugepenis20
    with dissolve

    h "Then I {i}hate{/i} you."
    s "Fine. I guess I’ll just spare you all the details then."

    scene popularguyhugepenis21
    with dissolve

    h "I take it back! Free coffee for as long as you live! Please! I must know everything! I must-"

    scene popularguyhugepenis22
    with dissolve

    h "Wait, {i}Sara{/i} doesn’t know yet...does she?"
    s "No. But...she {i}does{/i} know that Sana has feelings for me. But I honestly can’t say I’d even expect her to hold it against me if she {i}did{/i} find out."
    h "She’s going to be jeaaaalooooous."
    s "I’d sure hope for Sana’s sake that’s not the {i}first{/i} thing she’d feel."
    h "Oh, it will be. Because she’s going to be jealous of {i}both{/i} of you. That woman would {i}totally{/i} fuck her daughter."
    s "Sara would not {i}fuck{/i} her daughter."
    h "Sure she would. I’ve seen it in my head a zillion times. Normally as part of some scenario where Sana is confused about the things she’s feeling and Sara helps her explore them to “relieve all the tension.”"
    s "Okay. But we both know that your head isn’t exactly a sanitized area. That’s just a fantasy, Haruka."
    h "You’ve seen the way she talks about her, though. All that “isn’t my daughter the cutest thing in the whole entire world” stuff. That’s fuck-talk."
    s "Can she not think her daughter is adorable {i}without{/i} wanting to fuck her?"
    h "No. And why are you being so defeatist about this when you could be just a step or two away from the actual hottest threesome {i}ever?{/i}"
    s "Because it’s just a fantasy."

    scene popularguyhugepenis23
    with dissolve

    h "For {i}you?{/i} The guy who gets to fuck {i}anyone{/i} he wants?! Who has an entire town on their knees, ready to suck him off?! How do you even still believe “fantasy” is a thing at this point?!"
    s "I just...you know..."

    scene popularguyhugepenis24
    with dissolve

    h "I’m gonna find out. And I’m gonna prove to you that she totally {i}would.{/i}"

    scene popularguyhugepenis25
    with dissolve

    h "Unless you want to talk little Sana into having a threesome with her mom’s best friend instead."
    s "Yeah...I might."

    scene popularguyhugepenis26
    with dissolve

    h "Ah!"
    s "I’m not sure Maki will go along with it, though. She barely knows Sana."

    scene popularguyhugepenis27
    with dissolve

    h "Ah..."
    s "Besides, things are...a little weird with me and her right now anyway."

    scene popularguyhugepenis28
    with dissolve

    h "Maki? Sara? Or Sana? We’ve mentioned a lot of girls and my mind is too deep in the gutter to follow."
    s "Sana. I kind of made her first time weird by..."
    h "..."
    s "..."
    h "Byyyyyyy what?"
    s "Maybe...telling her I love her and then...cumming inside of her?"

    scene popularguyhugepenis29
    with dissolve

    h "You {i}came inside{/i} of that little angel?! Are you {i}trying{/i} to create a demon?!"
    s "Just gonna ignore the love part, huh?"
    h "Yes! That part’s boring. {i}You came inside of her?!{/i} That’s pretty much exactly how she...came into existence in the first place! Just with...Sara instead, obviously."
    s "In hindsight, I probably should have asked if that was okay. Yeah."

    scene popularguyhugepenis30
    with dissolve

    h "Ugh...probably."
    h "It’s not like I can blame you, though. If {i}I{/i} was a guy, I’d cum the second I put it in. She’s so cute. God, I’d cum so much. All inside her. All over her body. All over her face. All over her-"

    scene popularguyhugepenis31
    with dissolve

    h "Was it a cyclops day? Or a new-Sana day?"
    s "Cyclops day."

    scene popularguyhugepenis32
    with dissolve

    h "Aaaaaaaah! Why do all of the best things only happen to you?!?! This isn’t faaaaair!"
    s "Just eat your fucking dinner, Haruka."

    scene black
    with dissolve2

    h "We haven’t even ordered yeeeeeeet!"

    "Haruka and I eventually {i}do{/i} get to order. But we don’t take much time to enjoy our meals as she frantically scarfs hers down in an effort to get me back to her apartment quicker."
    "And of course, she succeeds."
    "But of course, it is my job to torment her now. So I make her finger herself in the foyer as I watch and make fun of her."

    h "[harukamaster]! P...Please! I’m...I...don’t want to...cum again...without you! F...Fuck me! Please!"

    "I do not. But {i}I{/i} do smirk as her eyes fill up with tears because I know they’re the type I enjoy."

    h "Ngh! C...Cumming! Cumming! I- wait! Where...are you going?"
    s "Home to sleep. Goodnight, Haruka. Congrats on the cafe thing."
    h "[harukamaster]! No! No! I need you! I need your cock! I need your big, throbbing-"

    play sound "dooropen.mp3"
    stop music fadeout 10.0

    s "See you later, Haruka. Thanks for dinner."
    h "{i}AAAaaaAAAaaaAAAaaaaah!{/i}"

    "Haruka cums. Probably."
    "I don’t know."
    "But I begin to make my way home-"
    "Because I’m a popular guy with a huge penis."

    $ renpy.end_replay()
    $ harukaspring3 = True
    $ haruka_love += 1
    $ cafeclosed = False

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label harukaspring4:
    scene harukarincafetalk1
    with dissolve2
    play music "cafe.mp3"

    "It was another night at Koi Cafe, which meant it was another chance for Haruka Hamasaki to sit down, relax, and be proud of herself for managing to create such a successful business in such a weird town."
    "Yet, as she glanced down at a sheet of paper with different types of milk splayed across it like a prostitute on a cocaine-lined glass table, she had something else on her mind."
    "{size=-3}You see, she was thinking about friendship. About ways to improve herself mentally so that she doesn’t wind up on the wrong side of the tracks again before being struck at full speed by a DC tilting EMU E353 Series train.{/size}"
    "Yes, it would truly suck to be killed by one of 213 aluminum alloy-bodied vehicles constructed between 2015 and 2019 with a car length of 20,000 (21,000 on the ends) and a maximum speed of 130 kmph."
    "{size=-3}She’d much rather be one of the 686 people riding it at maximum capacity from Shinjuku to Kōfu as a part of the limited express Kaiji service, complete with free passenger Wifi, trolley service, and excellent views of Mt. Fuji.{/size}"
    "Was she thinking about it {i}this{/i} specifically, though? No. This is just a metaphor. A long one. In fact, Haruka had only taken such a train one time in her life — on a trip to see her aunt and uncle in Yamanashi."
    "They didn’t matter right now, though. Not just because they weren’t on her mind, but because they {i}had{/i} been struck by a DC tilting EMU E353 Series train over a decade ago. "
    "Hey, have you ever noticed how the bass line in this song sounds like a beating heart?"
    "Anyway, Haruka. Rin. Two girls in one place — the place that they worked. "
    "No trains. No customers (they were closed right now). Just milk and a mountain of problems that wouldn’t be able to drink that milk because they are problems and problems don’t have mouths."
    "Seriously, though — what if this song is alive?"

    h "Rin. Try to push skim milk over the next few days. I ordered too much of it and I don’t want it to go bad."
    r "You didn’t order too much. Kids these days just don’t care about fat intake the way they used to."
    h "Yeah, that was all we talked about when I was growing up. I never paid much attention, though."
    r "Well, maybe if you did, your boobs wouldn’t be the size of hot air balloons?"
    h "Yeah, I think you’re right. I should round up every other large-breasted millennial and file a class action lawsuit against Big Milk for when our backs all break in ten more years."
    r "I bet “Big Milk” is what they called you in high school."

    scene harukarincafetalk2
    with dissolve

    h "Please, no. I’ve gotten enough nicknames from Molly. The last thing I want is for “Big Milk” to catch on. "
    r "With Molly, it’d probably be something more like...{i}Gigantimilk, Envoy of All that Lactates{/i} or something."
    h "On second thought, I guess Big Milk is fine. I’m going to call you Little Milk, though. "
    r "Aww, we’re like those little ladle constellations. Maybe they’ve been scooping up milk this entire time and Neil deGrasse Tyson just hasn’t figured it out yet."

    scene harukarincafetalk3
    with dissolve

    h "Yeah, maybe. You almost done over there? You were supposed to clock out ten minutes ago."
    r "..."
    h "Rin? You okay?"
    r "Yeah! And...I’m done. I’ve {i}been{/i} done, actually. But, uhh..."

    scene black
    with dissolve2

    r "Actually, uhh...let me clock out first. I don’t want to-"
    h "Is it depression again? Because I told you I don’t want you forcing yourself to work if-"
    r "No! No, it’s not that...It’s just..."

    play sound "static.mp3"
    scene harukarincafetalk4 with flash
    stop sound

    r "Well, remember how I told you my mom took my phone away for the foreseeable future?"
    h "I literally just gave you a raise. I can’t give you another one."
    r "I don’t need another raise. I need...advice. And I {i}definitely{/i} don’t want to talk to my mom about it since that’s kind of how I got into this mess in the first place. "
    r "I just...don’t know who else to turn to. And you’re practically a third mom to me at this point, so-"
    h "Of course. You can ask me anything whenever you want. "
    r "Okay, but...it’s gonna get graphic."
    h "You can definitely ask me anything whenever you want. "
    r "Thennnnn..."
    r "What does it...{i}mean...{/i}when a girl goes down on you?"

    scene harukarincafetalk5
    with dissolve

    h "You...made it this far into lesbianism without knowing what that means?"

    scene harukarincafetalk6
    with dissolve

    r "N-No! I obviously know what it means! I just...don’t know what it {i}means!{/i} Do you know what I mean?!"
    h "Like...emotionally?"

    scene harukarincafetalk7
    with dissolve

    r "Yes! That! Like...you would obviously have to {i}like{/i} someone to do that, right? Especially if it was out of nowhere while you were really upset and confused and horny."
    h "I’m almost always upset, confused, and horny."
    r "Me too. That’s why we get along so well."
    h "Rin...did..."
    h "Did this...actually {i}happen?{/i} "
    r "Will this conversation be able to proceed if I do not answer that question?"
    h "No."

    scene harukarincafetalk8
    with dissolve

    r "Then...{i}yeah.{/i}"
    h "Well that’s great, isn’t it?! Who was it? Sana? I bet it was Sana."
    r "It...um..."

    scene harukarincafetalk9
    with dissolve

    r "It was...Chika."
    h "Holy shit."
    r "Yeaaaaah."
    h "I...don’t get it, though. That’s awesome, isn’t it? You liked her for years. Shouldn’t you be happy about this?"

    scene harukarincafetalk10
    with dissolve

    r "Yeah! I definitely should! But I’m still not really sure if it actually {i}meant{/i} something! And what’s even more confusing is that I don’t know if I even {i}want{/i} it to."
    h "Why...wouldn’t you want it to?"
    r "Because..."

    scene harukarincafetalk11
    with dissolve

    r "Because I...think I...have a crush on Sensei."
    h "..."
    r "..."
    h "And..."
    h "And you’re {i}just now{/i} realizing this?"
    r "Apparently."
    h "You seriously didn’t know?"
    r "No..."
    h "You mean to tell me that {i}all{/i} this time, you {i}really{/i} never wanted to be with him? That you were {i}totally{/i} cool with just bro-ing it up for the rest of your life?"

    scene harukarincafetalk12
    with dissolve

    r "Why was it so obvious to everyone but me?..."
    h "I’m sorry, I...didn’t mean for it sound like I was making fun of you. I just figured you knew that already. "
    h "But yeah...if you’re interested in him now and you’re {i}not{/i} interested in Chika anymore-"
    r "I don’t {i}know{/i} what I’m interested in, Haruka. Like, I {i}thought{/i} I was over Chika. But then she decided to fucking go to town on me and now my heart starts freaking out again whenever she’s around."
    h "But you’re worried it didn’t mean anything to her...and you don’t want to overthink things like you always do."
    r "Yeah..."
    r "Chika’s..."

    scene harukarincafetalk13
    with dissolve

    r "She’s seemed...different lately. The Chika I know is, like...super faithful and would never cheat on Sensei since she genuinely believes they’re in a relationship."
    h "Oof."
    r "But now, all of a sudden, she’s just...{i}okay{/i} with him seeing other girls? Like, she straight up told me she wanted to see the look on my face while he fucks me."
    h "Yeah, me too."

    scene harukarincafetalk14
    with dissolve

    r "What?"
    h "Nothing! Uhh...so...so what are you asking me exactly? Just...for my feelings on what Chika did? Or...do you want to know where to go from here? Or..."
    r "I’m just not really sure what to do. Chika is clearly the more logical choice here {i}if{/i} she actually likes me. And going out with her wouldn’t get anybody in trouble. But, like..."

    scene harukarincafetalk15
    with dissolve

    r "I really feel like my heart is pushing me toward Sensei this time. Even {i}with{/i} all of the obstacles that are suddenly being thrown at me."
    h "Well...there’s your answer then."
    r "Really? That easy? You don’t think it’s weird for me to go after an adult instead of a girl my age?"
    h "This isn’t {i}any{/i} adult we’re talking about, Rin. It’s Sensei. You two are already like brother and sister, so you might as well just have sex already."
    r "I feel like that sentence would hit a lot differently if we weren’t both only childs...only children? Which one of those is grammatically correct? They both sound wrong."
    h "I don’t know, but I get what you’re saying. If you’re expecting me to talk you out of pursuing him, though...it’s not going to happen."
    r "I feel like it {i}should.{/i}"
    h "Probably, but the way I look at it is really simple. "
    h "You two are {i}clearly{/i} compatible despite the age difference. And I think the fact that you’ve managed to know each other for this long {i}without{/i} hooking up is a testament to that. That’s impressive, Rin."

    if harukasex == False:
        r "But you’ve known him pretty much just as long as me and {i}you{/i} haven’t had sex with him either. Are you saying that {i}you’re{/i} compatible with him too?"
        h "I’m married. You’re not. It’s different."

    else:
        r "I guess so. {i}You two{/i} had sex pretty much right after meeting each other."
        h "Yes. I regret nothing and intend to stay his obedient little sex slave forever."
        r "This seems like a weird thing to say while pushing me to go after him."

    h "I just want you to be happy, Rin. That’s all I’ve {i}ever{/i} wanted for you. And I just think that {i}he{/i} is what would make you the happiest right now."
    r "Why do you think that, though? Why aren’t you worried about all the potential issues and...{i}competition...{/i}the fact that my mom would fucking {i}kill{/i} me? "
    h "I have known you for a long time, Rin. I’ve seen you at your best, your worst, and everything in between."
    h "I watched the Chika drama unfold. The Otoha drama and the subsequent Molly drama. The Otoha drama {i}again.{/i} And then every single customer who comes in with dyed hair and a crop top that you fall in love with."
    r "I am weak. We all know this."
    h "Yes. But this is the {i}first{/i} time I have ever seen you approach a potential relationship maturely. And that just tells me you’re being extra careful not to fuck it up."

    scene harukarincafetalk16
    with dissolve

    h "Is Sensei the most politically correct choice? No. Is it something I think you should ask {i}others{/i} for advice on? Definitely not. But that doesn’t change how it’s what I would do if I were in your shoes."
    r "So...love now...consequences later?"
    h "Right."
    r "And...Chika? What do I do about her?"
    h "Well, do you think she’s going to try and go down on you again?"
    r "I hope so. That was awesome. Scary and kind of weird, but still awesome."
    h "But if you had to choose between her going down on you and having sex with Sensei-"
    r "Western silverback."
    h "...What?"
    r "I said what I said."

    scene harukarincafetalk17
    with dissolve

    h "Yeah. And so did I. But advice is just advice at the end of the day, and I’ll support you no matter {i}what{/i} you decide to do, Rin."
    r "Thank you, Haruka. Do I need to file a formal notice in advance if I want to request a hug?"
    h "No. You may hug me whenever you like."

    play sound "tackle.mp3"
    scene harukarincafetalk18
    with hpunch

    r "Then here I come, Big Milk."
    h "I’ve got you, Little Milk."
    r "My boobs are actually big for my age."
    h "But they’ll never measure up to mine."
    r "So soft...so large...so comfortable...I could live here."
    h "Well, you’re welcome to stay as long as you like. "
    r "No...it’s okay. I still haven’t clocked out yet and should probably be heading home soon."
    h "It’s fine. I’ll adjust your time manually."
    r "You don’t have to. I’ll just take the overtime pay."
    h "No. I’ll definitely adjust your time manually. "

    scene harukarincafetalk19
    with dissolve

    r "Fiiiiiiine..."
    r "Thank you, Haruka. I’m really glad you’re my boss."
    h "And I’m really glad you actually care about your job."
    h "I’m gonna finish cleaning up now, but you can feel free to use my phone if you want to sext Sensei. "
    r "And risk sending my mom another five minute video of me masturbating? No thanks."

    scene harukarincafetalk20
    with dissolve

    h "Send her what?"

    play sound "static.mp3"
    scene harukarincafetalk21 with flash
    stop sound

    r "Night, Haruka! Thank you again! I’m glad your morals aren’t as strong as my mom’s! "
    h "Night! And remember, we never spoke about any of this! I’m a morally good, law abiding woman outside of conversations with teenage girls asking me if they should act inappropriately!"
    r "Just like the guy I like! Night!"
    h "No! He’s kind of bad all the time! Night!"

    if harukasex == False:
        scene black
        with dissolve2
        stop music fadeout 10.0

        h "Oh! And also remember to push skim milk! Even if you need convince all of your friends that fat intake matters!"
        r "Too many things to remember! You have too much faith in me!"
        h "You’re the only person I {i}can{/i} have faith in! Everyone else is unreliable!"
        r "That’s really sad! Anyway, goodnight! Again!"
        h "Goodnight!"
        h "And good luck..."

        "As Rin exits the cafe, Haruka goes back to her clipboard — the one reminiscent of a whore. "

    else:
        h "........."
        h "......"
        scene harukarincafetalk22
        with dissolve

        h "........."
        h "......"

        scene harukarincafetalk23
        with dissolve
        play sound "phonebeep.wav"

        h "........."
        h "......"

        play sound "phonebeep.wav"

        s "{i}Hello?{/i}"
        h "Hi."
        h "You should fuck Rin."

        play sound "static.mp3"
        scene harukarincafetalk24 with flash
        stop sound

        s "..."
        h "..."
        s "Okay?"
        h "{i}Awesome. Good talk.{/i}"
        s "Is...there a {i}reason{/i} you are calling me in the middle of the night and telling me to fuck her?"
        h "{i}Of course.{/i}"
        s "Is it because {i}you{/i} want to fuck her? And {i}me{/i} fucking her creates an opportunity for you to ultimately do that?"
        h "{i}While that may very well be true, I would implore you to fuck her even IF my inclusion was off the table.{/i}"
        s "Yeah, because you’d still want to hear about it and you know I’d tell you."

        play sound "static.mp3"
        scene harukarincafetalk25 with flash
        stop sound

        h "Again! That may be true. {i}But-{/i}"

        scene harukarincafetalk26
        with dissolve

        h "Don’t you think you two would be great?"
        s "{i}What are you talking about?{/i}"
        h "Oh, don’t act like you wouldn’t go to hell and back for her. You care {i}way{/i} more than you let on."
        s "{i}Okay. But that still doesn’t warrant calling me out of nowhere to tell me this. What’s going on? Did something happen to her?{/i}"
        h "See? You’re worried right now."
        s "{i}No, I’m confused right now. You sound way less horny than you normally do when you name some teenager you want me to fuck.{/i}"
        h "She’s falling for you, Akira. And if you don’t act quickly, you might lose your chance. You have competition this time."
        s "{i}I always have competition when it comes to her and I have lost 100%% of the time.{/i}"
        h "Yeah, well...this time’s different."
        s "{i}Haruka-{/i}"
        h "Just think about it, okay?"
        s "{i}...{/i}"

        scene harukarincafetalk27
        with dissolve

        h "And definitely fill me in on every single explicit detail if you do. Thanks."

        scene black
        with dissolve2
        stop music fadeout 10.0

        "Haruka goes back to her clipboard — the one reminiscent of a whore. "

    "She doesn’t think about trains."
    "She doesn’t think about friendship either this time."
    "She thinks about how lonely she is."
    "And how there is only one person she’s met who would choose her over anyone else."
    "He’s so far away now."
    "..."
    "She wonders if he’ll stay that way forever."

    $ renpy.end_replay()
    $ harukaspring4 = True

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
