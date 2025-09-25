label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
    if rin_love >= 10 and cafe10 == False:
        jump cafe10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False:
        jump cafe15
    if rin_love >= 20 and ayanenew1 == True and cafe15 == True and day50 == True and cafe20 == False:
        jump cafe20
    if rin_love >= 15 and cafe15 == True and day63 == False:
        jump rincafegone
    if rin_love >= 25 and rindorm20 == True and amisroom5 == True and day65 == True and cafe25 == False:
        jump cafe25
    if rin_love >= 30 and beachvacation16 == True and cafe30 == False:
        jump cafe30
    if rin_love >= 35 and library30 == True and rindorm35 == True and rininvite == True and cafe35 == False:
        jump cafe35
    if rin_love >= 40 and christmas7 == True and cafe40 == False:
        jump cafe40
    if rin_love >= 45 and rindorm40 == True and cafe45 == False:
        jump cafe45
    if rin_love >= 50 and secondbeach18 == True and cafe50 == False:
        jump cafe50
    if otoha_love >= 20 and otohaspecial15p2 == True and otohadate20 == False:
        jump otohadate20
    if rinsad == True:
        jump rincafegone
    if chap4active == True:
        jump rinspringcafegen
    if chapthreeactive == True:
        jump rinsummer2cafegen
    if christmas7 == True:
        jump rinmorninggen2
    else:
        jump cafe6to9

label callrinmorning:
    if cafeclosed == False:
        "Rin should be working right now."
        "I can probably see her if I go to the cafe."
        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I tap on Rin's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "She doesn't."

        jump callmorning

label callrinafternoon:
    if dormwar17 == False:
        "Rin doesn't know I have her number yet, so I probably shouldn't call her..."
        jump callafternoon
    if rinphoneblock == True:
        play sound "phonebeep.wav"

        "I tap on Rin's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "She doesn't."

        jump callafternoon
    if rinsad == True:
        play sound "phonebeep.wav"

        "I tap on Rin's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "She doesn't."

        jump callafternoon
    if chapthreeactive == True:
        play sound "phonebeep.wav"

        "I tap on Rin's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."

        jump callafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Rin's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        r "Greetings and salutations, Sensei!"
        r "What's up?"
        s "Hey, what are you doing right now?"
        r "Sad girl stuff."
        s "And what does that entail, exactly?"
        r "Coffee and loud music about girls."
        s "Are you still at work?"
        r "Would I have answered the phone if I was?"
        s "Probably."
        r "Dude! I am a GOOD employee. I follow the rules!"
        s "Unless the rule is making what the customer actually orders."
        r "I've already told you! You're special."
        r "So special that I'm giving you a once in a lifetime opportunity to come hang out and be a sad girl with me."
        s "I don't want to be a sad girl."
        r "{i}The coordinates are on the way.{/i}"
        r "{i}Godspeed, Sensei...{/i}"
        s "Rin-"

        play sound "phonebeep.wav"

        s "..."

        scene black
        with dissolve

        "The call comes to an end and I receive a text with an address shortly after."
        "........."
        "......"
        "..."

        scene rinnoongen
        with dissolve
        play music "cafe.mp3"

        "It turns out that the address I was sent was actually the address to another cafe in the area."
        "I'm not exactly sure what would compel someone who works at a cafe to spend their free time at a {i}second{/i} cafe, but I guess that's how things are going to be today."
        "Rin orders some drink I immediately forget the name of as well as a few pastries and the two of us find a place to sit at a table near the window."
        "Despite being a self-proclaimed {i}sad girl{/i}, she seems pretty fine today."
        "I don't know if that's just a thing [young]people are saying now, but I also acknowledge the fact that true despair can strike at any moment."
        "And, more often than not, it's lurking somewhere in the background- waiting to devour people like her whole."

        scene black
        stop music

        "No one is devoured and we have a good time."

        $ rin_love += 1

        "{i}Rin's affection has increased to [rin_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label callrinnight:
    if dormwar17 == False:
        "Rin doesn't know I have her number yet, so I probably shouldn't call her..."
        jump callnight
    if rinbetrayed == False and rindorm50special == True and rindate50 == False:
        jump rindate50
    if rinphoneblock == True:
        play sound "phonebeep.wav"

        "I tap on Rin's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "She doesn't."

        jump callnight
    if rinsad == True:
        play sound "phonebeep.wav"

        "I tap on Rin's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "She doesn't."

        jump callnight
    if chap4active == True:
        jump rinspringnightgen
    if chapthreeactive == True:
        jump rinsummer2nightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Rin's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        r "Yo!"
        s "Hey. What are you up to?"
        r "Hanging out in my room!"
        r "It's very exciting."
        s "Sounds it."
        s "Did you want to meet up or something?"
        r "Sure!"
        r "But you're going to have to come to me because I don't feel like getting up. Sorry not sorry."
        s "You expect {i}me{/i} to come to you?"
        s "Who do you think I am?"
        r "Just some LOSER!"
        r "{i}You know where to find me, Sensei.{/i}"

        play sound "phonebeep.wav"

        s "..."

        "Looks like I'm going to have to go to the dorms if I want to see Rin tonight."

        jump callnight

label rinmorninggen2:
    scene rinmorninggen2
    with dissolve
    play music "cafe.mp3"

    "I show up at the cafe a little earlier than normal and find Rin cleaning the place up before the morning rush."
    "She says a bunch of confusing things about stuff the closing crew didn't do and I don't really understand any of them."
    "What I do grasp, however, is that it was likely all Molly's fault that this happened."
    "With a bit of prodding, I'm able to get Rin to talk about some more interesting things and we ultimately wind up bonding over none other than girls."
    "She pulls her phone out and begins showing me a bunch of models she follows on social media and I'm...pretty sure she's even more attracted to them than I am based on her high praise."
    "Haruka winds up coming over to break up the conversation but ultimately joins in on the fun."
    "I'm not sure how much time goes by as we do this, but I am sure that I become aroused."
    "Whoops."

    scene black
    with dissolve

    "Our bonding experience is cut short when a group of customers walks through the door."
    "Rin quickly goes back to cleaning while Haruka mans the counter, and I-"
    "Well, I get in line to order a coffee."
    "Having a customer service job must suck."

    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin's affection has increased to [rin_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label firsttimecafe:
    play music "cafe.mp3" fadein 2.0
    scene cafe_day
    with dissolve

    "I decide to stop by the cafe after refusing breakfast from Ami a good four or five times."
    "It's nothing against her cooking. In fact, it kind of feels like Ami's carefully tailored her abilities to the best of my liking."
    "I just feel compelled to get out and actually do things every once in a while."
    "Or at least trick myself into thinking that I'm doing things when, in all actuality, I'm just roaming around in hopes of more easily bridging the first half of the day to the second."
    "Regardless, I am at the cafe now. And so I must do what is customary for any cafe-goer-"
    "Hit on the barista."

    q "Next customer!"

    scene cafe1
    with fade

    r "What can I get y-"

    scene cafe2
    with dissolve

    r "Wait, Sensei? I almost didn’t recognize you on account of the normal clothes and slightly threatening aura."
    s "Threatening aura?"
    r "Slightly threatening. Like a bear, but if the bear was asleep or missing both of its hind legs."
    s "Good. That's pretty close to what I was going for so I'm glad the change of clothes helped."

    scene cafe1
    with dissolve

    r "Weird seeing you drop by, though. Didn't take you for much of a coffee drinker."
    r "So, what can I get you?"
    s "I'll take, uhh..."

    menu:
        "Black coffee":
            s "Just a large coffee please."
            s "Unless you're going to force me to use whatever the Italian word for large is."
            s "If that's the case, I'll just leave with nothing."

            scene cafe3
            with dissolve

            r "No one actually {i}forces{/i} anyone to use those sizes, dude. They're more of a quirky suggestion than a flat out rule."
            r "Forcing people to say {i}Venti{/i} and {i}Grande{/i} and stuff is more like a...fun little movie thingy."
            r "But anyway, what do you take in your coffee? Milk? Sugar?"
            s "Just black, please."

            scene cafe2
            with dissolve

            r "Woah, really? You're not just trying to upgrade your slightly threatening aura to full on threatening, are you? Cause I wasn't trying to wake the bear."
            s "Nope. That's just how I drink coffee."
            r "And you're not just trying to make things easy for me either?"

            scene cafe4
            with dissolve

            r "Because I’ll have you know I’m pretty great when it comes to this barista stuff."
            r "Humble brag, but I can kind of run circles around the rest of the staff here."
            s "Impressive, but no. I really do just drink my coffee black."
            r "If you say so. At least it’ll be easy to remember your order."
            s "Who says I’m coming back? You still have a chance to blow this."

            scene cafe2
            with dissolve

            r "How could anyone mess up a black coffee? You just...pour it into a cup."
            s "Honestly, you would be surprised."

            scene cafe4
            with dissolve

            r "Guess I'll just have to take your word for it."
            r "Total's 200 yen, Sensei."
            s "Is that before or after my teacher discount?"
            r "Oh, sorry. My b."
            r "New total is 500 yen, Sensei."
            s "Wait, why did the total go up?"
            r "Probs cause I used my employee discount on you. But hey, if you want to feel cool and use the teacher one instead, be my guest."
            s "No, I think I'm fine with being an employee for the length of this transaction. Thanks, Rin."
            r "I gotchoo, pal."
            r "Now go grab a seat and I'll bring your coffee right over."
            jump chosedrink

        "(Copyrighted frozen beverage)":
            s "I’ll take one (copyrighted frozen beverage) please."

            scene cafe3
            with dissolve

            r "Gotcha. One (copyrighted frozen beverage) coming right up!"

            scene cafe2
            with dissolve

            r "I’m surprised, though. Ordering a feminine drink like that really makes your slightly threatening aura even {i}less{/i} threatening."
            r "Now, it's like you're an unconscious bear without any legs at all."
            s "Not only girls can enjoy (copyrighted frozen beverages), you know."
            s "Sometimes, even a manly man like me likes to kick back and relax with a nice, cold (copyrighted frozen beverage)."

            scene cafe3
            with dissolve

            r "Right, right. I guess you were just so masculine that I expected you to order a bowl of nails and beard oil."
            s "I have no use for beard oil without a beard."
            r "You still want the nails, then?"
            s "Extra nails, actually. Thank you for asking."
            r "Damn, you're actually pretty good at this barista banter, Sensei. Most people would've said something really awkward or lame by now and here you are about to eat nails for me."
            r "I admire your dedication."
            s "So, what do I owe you?"
            r "Total is 600 yen. You can just leave your money on the counter and go take a seat. I'll bring it over when it's ready."
            jump chosedrink

        "Tacos":
            s "I’ll have the tacos, please."

            scene cafe6
            with dissolve

            r "The what?"
            s "Tacos. The small, tortilla shell filled with meat and other various ingredients."
            r "Have...Have you ever been to a cafe before? Or are you just guessing what's on the menu? Because all the stuff we have is listed right above-"
            s "It's tacos or nothing, Rin."
            r "Sensei, we don't sell tacos here."
            s "Then why was I even given this option? That doesn't make any sense."
            r "What option? What are you talking about?"
            s "Forget it. I'll just have a black coffee instead."

            scene cafe2
            with dissolve

            r "Woah, really? You're not just trying to upgrade your slightly threatening aura to full on threatening, are you? Cause I wasn't trying to wake the bear."
            s "Nope. That's just how I drink coffee."
            r "And you're not just trying to make things easy for me either?"

            scene cafe4
            with dissolve

            r "Because I’ll have you know I’m pretty great when it comes to this barista stuff."
            r "Humble brag, but I can kind of run circles around the rest of the staff here."
            s "Impressive, but no. I really do just drink my coffee black."
            r "If you say so. At least it’ll be easy to remember your order."
            s "Who says I’m coming back? You still have a chance to blow this."

            scene cafe2
            with dissolve

            r "How could anyone mess up a black coffee? You just...pour it into a cup."
            s "Honestly, you would be surprised."

            scene cafe4
            with dissolve

            r "Guess I'll just have to take your word for it."
            r "Total's 200 yen, Sensei."
            s "Is that before or after my teacher discount?"
            r "Oh, sorry. My b."
            r "New total is 500 yen, Sensei."
            s "Wait, why did the total go up?"
            r "Probs cause I used my employee discount on you. But hey, if you want to feel cool and use the teacher one instead, be my guest."
            s "No, I think I'm fine with being an employee for the length of this transaction. Thanks, Rin."
            r "I gotchoo, pal."
            r "Now go grab a seat and I'll bring your coffee right over."
            jump chosedrink

label chosedrink:
    scene black
    with dissolve

    "I reach into my pocket for a few coins and place them directly into a tray on the counter before heading back over to find somewhere to sit."
    "Or, at least that's what I {i}would{/i} be doing if I actually intended to hang around, which I most certainly do not."
    "Should I have informed Rin of this at the time of placing my order? Maybe. But she also should have asked."
    "So now there is not much to do apart from standing awkwardly in the middle of the cafe and waiting for her to return..."
    "........."
    "......"
    "..."

    scene cafe7
    with dissolve

    r "Yo, why are you being such a sketchball? I told you to go find a seat."
    s "I meant to order my drink to-go."
    r "You know you...can still sit down if you order something to-go, right? Then just...get up once it's ready?"
    s "Or I could remain standing and make everyone here equally uncomfortable."
    r "I mean...{i}I guess?{/i}"
    s "So, do you have my drink?"

    scene cafe8
    with dissolve

    r "Yup! Got it right here."

    "Rin hands me my order and smiles at me in what seems to be anticipation, constantly shifting her gaze from me to the drink I'm holding."

    s "..."
    r "..."
    s "Are you going to watch me drink it?..."

    scene cafe9
    with dissolve

    r "Ah- sorry! I was just curious about whether you’d like it or not."
    s "I mean, I did order it. I wouldn't have bought something if I wasn't sure I'd like it."

    "Wanting to appease Rin and quell how uncomfortable this is beginning to make me, I bring the beverage to my mouth and-"

    s "..."
    r "So? Good?"
    s "I mean...yeah. But..."
    r "But what? Tell me."
    s "Rin, this isn't even close to what I ordered."

    scene cafe10
    with dissolve

    r "No. I suppose it is not."
    s "..."
    r "..."
    s "Well, is there an explanation for that? Or..."

    scene cafe11
    with dissolve

    r "Oh, I guess. Though, it's less of an explanation and more of just me using you as a guinea pig."
    r "You see, that's a custom recipe of mine. And I’ve been trying to get my manager to add it to the menu, but she’s been all like, “No way! You can't just change the menu, Rin!”"
    r "So, I figured if I was able to actually get some more people on my side, I might be able to persuade her."
    s "I see..."
    r "So, now that you've tried it and liked it, I'm going to need you to write on one of her comment cards that I'm the best barista ever and that she should listen to me more."
    s "I'm not sure if I can, in good faith, call you the best barista ever when you didn't even bring me my actual order."

    scene cafe12
    with dissolve

    r "I swear I was going to right after you tried this one!"
    r "Here, I'll even go get it right now. I just-"
    s "It's fine, Rin. I'll just keep whatever this is instead."
    s "It really {i}is{/i} good."

    scene cafe13
    with dissolve

    r "You...You really think that? And you're not just lying to me because it's customary to flirt with your barista?"
    s "I really think that. I'm going to need one of those comment card things if I'm going to recommend it to your manager, though."

    scene cafe14
    with dissolve

    r "Yeah! Totally! I'll go get one right now!"
    r "Just hang tight, okay?! I'll be right back!"

    scene black
    with dissolve2

    "Rin quickly dashes to the counter to grab me a card and I wind up having to sit down after all."
    "Unfortunately, a wave of customers all decide to show up at once and I'm unable to continue talking to her once I have my comment written."
    "Not knowing how long it will be until she's free again, I wait for a moment where she's distracted and place the card down on the counter before leaving."
    "And as I step out into the street with an indiscernible beverage in my hand, I come to realize something."
    "It's that I am now only slightly more than a lab rat."
    "And that the future of my beverage choice hangs in great jeopardy at the hands of a single teenager."

    scene black
    with dissolve

    $ renpy.end_replay()
    $ firsttimecafe = True
    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label cafe2to4:
    scene cafe_day
    with dissolve
    play music "cafe.mp3" fadein 2.0

    "I head to the cafe to grab a quick cup of coffee and a bite to eat."
    "Rin remembers my order from last time, but still decides to make me some super secret mystery-concoction instead."
    "Even though I have no idea what’s in it, it tastes great...And it makes her happy knowing that I like it."
    "I hang out for the next couple hours playing games on my phone before deciding to get on with the rest of my day."

    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 3.0

    scene black
    with dissolve

    "........."
    "......"
    "..."
    jump saturdayafternoon

label cafesugar:
    play music "cafe.mp3"
    scene cafe_day
    with dissolve

    r "Next customer!"

    scene cafe1
    with dissolve

    r "Oh! Morning, Sensei! What'll you be having today?"
    s "Rin, why do you even bother taking my order if you're just going to give me some random concoction instead?"

    scene cafe2
    with dissolve

    r "Hey, it won't be random! I put a lot of thought and love into the drinks I make."
    s "Then I guess I will order one cup of thought and love, please."

    scene cafe4
    with dissolve

    r "Excellent choice, Sensei! I’ve got a really good one for you today, I swear."
    s "They've all been good so I guess I'll just, once again, trust the judgement of the self-proclaimed best barista ever."
    r "Nuh-uh-uh. It's not just self-proclaimed anymore since you wrote it on a card. Now, there is written proof that I am the best barista ever."
    s "I don't think I'm really fit to be making the final decision on that, but I'm glad you're happy."
    s "So, what's so different about today's drink?"

    scene cafe1
    with dissolve

    r "The one today is made with {i}extra{/i} love."
    s "Can I have extra {i}thought{/i} instead? Love is a little too sweet for me."
    r "No. Because love tastes like vanilla and we ordered extra vanilla syrup that I am now responsible for getting rid of."
    s "There's no actual love in this drink at all, is there?"

    scene cafe4
    with dissolve

    r "There is love in {i}everything{/i} I make for you, Sensei."
    s "The barista isn't the one who's supposed to initiate the flirting. I think there's some sort of code against that."
    r "There's a code against a lot of things. But then there are cheat codes that let you ignore them."
    r "My love is but one more bug in the system. A bug that just happens to taste like vanilla."
    s "Well, I'm glad that you've at least confirmed it won't be anything with the potential to kill me."

    scene cafe3
    with dissolve

    r "Kill you? Of course not. If you die, who will I have to experiment on?"
    s "Is your need for a guinea pig all that is keeping me tethered to this world?"

    scene cafe1
    with dissolve

    r "Probably. So it would be in your best interest if you'd just leave all this stuff to me and go take a seat while I pour you a nice cup of love."
    r "With maybe a {i}little{/i} bit of arsenic for added flavor."
    s "..."
    r "..."
    s "Is your manager around? I'd like to inquire about a refund."
    r "Sorry, no returns. Tough luck."

    scene black
    with dissolve

    "I sigh to myself and slide a 500 yen coin across the counter to Rin, who picks it up and shoots it into a register like it's a basketball."
    "Unfortunately, she does not appear to be very good at basketball as she misses completely and it bounces off the counter and right back over to me."
    "But, being the gentleman I am, I give her the money {i}again{/i} and go to find a table as she starts preparing my drink."
    "........."
    "......"
    "..."

    scene sugarredux1
    with dissolve

    r "Alrighty, here you go. I brought some extra pastries and stuff too."
    s "I...see that. Not like I care, but is it really okay for you to be taking this much stuff from work?"
    r "Totes. All this stuff needs to get thrown out anyway since we can't hold stuff for more than two days."
    s "Well, thank you very much for the expired pastries."

    "I take a sip of the drink Rin slid across the counter to me and, just like always, it's...good."
    "A bit on the sugary side due to the amount of {i}love{/i} in it, but still good."

    s "I give it a seven out of ten."

    scene sugarredux2
    with dissolve

    r "Wait, a seven?! That's it?!"
    r "But I put so much love into it!"
    s "I think that's exactly the problem. All I can taste is the love."
    r "But the love is good! The love is great! Love the love, Sensei!"
    s "Do you want to give it a try? Because I'm fine for now, but I have no idea if I'll be able to drink the whole thing."
    r "Is it really that sweet?"
    s "Shouldn't you be testing things before handing them off to me?"
    r "Do scientists test chemicals on themselves before pumping rodents full of them, Sensei? You are my guinea pig for a reason."
    s "As the person responsible for establishing the footing of your new drink platform, you should really value me more."

    scene sugarredux3
    with dissolve

    "Rin looks down at my mug for a few seconds, contemplating whether or not she wants to become a rodent of her own, before sighing to herself and admitting defeat."

    r "Okay, fine. I'll take your word. Some people are really into the super sugary stuff, though."
    r "Like, we get customers all the time who order coffee and then proceed to dump like, 50%% of it out and fill the rest with cream and sugar."
    s "That's not even coffee at that point."

    scene sugarredux4
    with dissolve

    r "I know! Like, why are you even ordering coffee if you don't like the taste of coffee? Do you just like the {i}idea{/i} of coffee? Do you think it will make people like you or something?"
    r "I don't get it. Especially those customers who are like...{i}umm...the place near my house uses extra syrup.{/i}"
    r "Like, whoopdy-fucking-do, Karen. Why not just go there instead if you like them so much?"

    scene sugarredux5
    with dissolve

    r "I'm gonna punch somebody in the face one day, Sensei. I just know it."
    s "Is it really okay to be saying things like that while you're still in uniform?"
    r "Yeah, I clocked out for my break so it's no big deal."
    r "I get what you're saying about the less sugar thing, though. I guess my mind was just tainted by all of the customers with shittier tastebuds than yours."
    r "Anyway, rant over. Let's order pizza."
    s "You sure you're done? Because it looked like you were enjoying yourself just now."
    s "It almost might be good to find out if there is anything that I, as a customer, should be doing to avoid invoking your wrath."

    scene sugarredux6
    with dissolve

    r "You’re fine, Sensei. I like you as a customer."
    s "That’s just because I let you experiment on me."
    r "The experimenting part definitely helps. But even without that, I'd like you."
    s "I think you're breaking the flirting code again, Rin."

    scene sugarredux7
    with dissolve

    r "This isn't flirting! I seriously do."
    r "We get a lot of customers in here and I'm never really {i}excited{/i} to deal with any of them."
    r "But with you, it's like...not like that."
    r "I don't know. It's hard to explain. But I'm going to ask that you keep showing up whenever possible as it definitely makes my mornings a little better."

    scene sugarredux8
    with dissolve

    r "But, now that I've gotten that embarrassing piece of information out of the way, I should probably be getting back to work."
    s "Already? But you just clocked out for your break a few minutes ago, didn't you?"

    scene sugarredux6
    with dissolve

    r "Yeah. I get a few breaks because of labor laws and stuff like that, though. What you just experienced was one of the short ones."
    r "But hey, time your visits better and you might be able to catch me on a full-length break one day."
    s "I'll do my best. Sorry your entire mini-break was wasted on me."
    r "It's not a waste at all."
    r "Do you want an actual drink now? Or are you going to force yourself to finish that one for my sake?"
    s "The plan was to tell you I'd finish this so I could look cool, then drop it into a trash can a few blocks away from here."
    s "Now that I know a replacement is possible, I will graciously accept."
    r "Roger that. But, just so you know, it's gonna be another patented Rin Rokuhara creation."
    r "Easy on the love this time."

    scene black
    with dissolve

    "Rin steps away from the table before swiftly spinning around and skipping over to the counter, starting on my new drink as soon as she arrives."
    "As is customary, another wave of customers crashes into the store and prevents the two of us from being able to actually say goodbye to one another-"
    "But I do get my replacement drink."
    "And go figure, but it's much more enjoyable without all of the love."

    $ renpy.end_replay()
    $ cafesugar = True
    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 3.0
    "........."
    "......"
    "..."
    jump saturdayafternoon

label cafe6to9:
    scene cafe1
    with dissolve
    play music "cafe.mp3"

    "Once again, I find myself killing time at the cafe with Rin."
    "She takes my order and promptly discards it before dumping a bunch of random ingredients into a cup and handing it over."
    "Despite my initial skepticism, it actually tastes pretty good and I finish the entire thing."
    "Rin smiles from ear to ear and tells me that she can't wait to rub this in her manager's face."

    scene black
    with dissolve2

    "Things get busy and I wind up having to leave before the two of us can start up a new conversation, but at least we managed to get a little bit closer."

    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe10:
    scene cafe_day
    with dissolve
    play music "cafe.mp3" fadein 2.0

    "I make my way into the cafe a bit more tired than usual because, for some reason, the world decided to spite me by disallowing me to sleep for more than an hour at a time last night."
    "But apart from how hard it is to be me and how cruel the world can be at times, I am now prepared to see my favorite barista and consume whatever strange concoction she cooks up for me today."

    scene cafeten1
    with fade

    "Or not."

    nr "Good morning! How's your day going so far?"
    s "It's...fine. And yours?"
    nr "Living the dream."
    s "That bad, huh?"
    nr "Thank you for being the first person to ever understand how canned and robotic that response is."
    nr "I take it you've worked in customer service before?"
    s "No, I've just gotten very good at bantering with baristas lately."

    scene cafeten2
    with dissolve

    nr "Oh. So this isn't your first time here?"
    s "Nope. I guess you could say I've become a bit of a regular."
    nr "A bit of a-"

    scene cafeten3
    with dissolve

    nr "Wait, you wouldn't happen to be Rin's teacher, would you?"
    s "I would. I'm a little surprised to have you guess that based on...literally no information apart from being a new regular, though."

    scene cafeten4
    with dissolve

    nr "Well, it's not like we've had many customers that fit your description lately."
    s "That description being?"
    nr "The owner of a penis."
    s "Well, that's a fun new way to say {i}man.{/i}"

    scene cafeten5
    with dissolve

    nr "Thanks for always stopping by, though. I think you'll be happy to know that I let Rin add her mystery beverage to the menu after reading your comment card."
    nr "I don't really think the part about her being the best barista ever was necessary, though. Especially since I'm the proud owner of that title."
    s "Well, as the proud owner of a penis, I would like to congratulate you for being the actual best barista and will offer Rin my condolences the next time I see her."
    r "Sensei! Don't give in that easily! You know in your heart of hearts that it is I, Rin Rokuhara, who is the true champion of (copyrighted frozen beverages)!"

    "Rin calls out from behind me and I begin to question how I walked in without noticing her."

    nr "So, what would you like? I don't want to keep you from talking to your regular barista for too long."
    s "Just a black coffee is fine."
    s "Oh, and your name."

    scene cafeten6
    with dissolve

    h "Haruka."
    h "And yours?"
    s "You can just call me Sensei."
    h "..."
    s "..."

    scene cafeten7
    with dissolve

    h "Wait, really?"
    s "Yup. And I'll just take a black coffee, please."
    h "But...your name-"

    scene black
    with dissolve

    s "You can just write {i}Sensei{/i} on the cup. It's fine."
    h "But...but..."

    "Haruka stands there for a moment as if she's waiting for the punchline to a joke."
    "Unfortunately, that punchline never comes and she is forced to awkwardly pour me a drink without ever learning my true identity."
    "She finishes and hands it to me across the counter, eyes unblinking and focusing on mine."
    "I stare back, nod, then walk away."
    "........."
    "......"
    "..."

    scene cafeten8
    with dissolve

    r "What the Hell was that? You trying to look cool in front of my boss or something?"
    s "Did it work?"
    r "She's still staring at you, so...I think so?"

    "Excellent."

    r "Also, aren't you here a little later than normal today? You actually caught me on my real break for once."
    s "Yeah...I couldn't really get any sleep last night, so I wound up not getting out of bed until a little while later."
    r "How come? Nightmares or something?"
    s "Nothing like that. Just one of those nights, I guess."

    scene cafeten9
    with dissolve

    r "Guess I can feel that. I've had my share of sleepless nights, but I'm typically a pretty heavy sleeper when my brain isn't exploding."
    s "Really?"
    r "Oh yeah. You could probably beat me with a pillow or something and I'd stay asleep."
    s "That’s kind of worrying in the event of some type of emergency."

    scene cafeten10
    with dissolve

    r "Nah, I'm sure Futaba would rescue me if something like that ever happened."
    r "Unless she's just been pretending to like me all these years and is secretly waiting for me to die."
    s "That doesn't sound like Futaba."
    r "I don't think so either. But I guess you never truly know someone until they have to save your life due to unforeseen circumstances."
    s "That's...yeah, okay."

    scene cafeten11
    with dissolve

    r "So, you finally got to meet my boss."
    s "Yeah. And she even got me exactly what I asked for. I didn’t realize this place could do that."
    r "Thoughts? She your type?"
    s "That depends. Is this a trick question?"

    scene cafeten12
    with dissolve

    r "No way! You can tell me. We're pals, right?"
    r "Plus, we have today off, so it's kind of like you're not even my teacher."
    s "I mean, I don’t think the time of day really determines my relationship with you."
    r "Hot or not, Sensei? Hot or not?"
    s "She's attractive, yeah."
    s "And...{i}very{/i} well endowed."

    scene cafeten13
    with dissolve

    r "You've got that right. Those things could feed a village of starving children for like a decade."
    s "I...don't think starving children would need to breastfeed for ten whole years...but I...guess I wouldn't blame them for wanting to?"

    scene cafeten14
    with dissolve

    r "Well, sorry to break your heart, but she’s married."
    s "Then why did you make it sound like you were trying to hook me up?"
    r "Cause I figured that would be the easiest way to get you to tell the truth."
    s "Is her husband still around with the whole space war thing going on?"

    scene cafeten10
    with dissolve

    r "Nope. He got drafted a few years ago and she hasn’t seen him since."
    r "She's actually really torn up about it underneath the buxom, bubbly exterior, though."

    scene cafeten15
    with dissolve

    r "I {i}may{/i} know someone else who’s into you, though. And it may or may not be a girl you know pretty well."
    r "But you’ve gotta promise not to tell her I told you."
    s "I'm guessing it's one of the students, then?"

    scene cafeten16
    with dissolve

    r "Woah! How did you know?"
    s "Well if it’s not Haruka, it kind of has to be. I don't really know anyone else."
    r "Oh, true. Good point."
    r "But yeah, it's a student. And she may or may not be my roommate."
    s "Ahh, so it's Futaba you're talking about."

    scene cafeten15
    with dissolve

    r "Bingo! "
    s "Yeah, I kind of figured. She tends to trip over her words whenever she talks to me, so...kind of a dead giveaway."

    if futabadorm15 == True:
        "She has also had my penis in her hand, but I don't think that's a detail I should really divulge right now."

    scene cafeten17
    with dissolve

    r "Yeah...I guess she's never been good at hiding her feelings."
    r "Not that she's ever really had any romantic ones but, like...yeah. Just speaking her mind has always been kinda tough for her."
    r "Truth be told, she’s been head over heels for you since the first day of school."
    s "Is it really okay for you to be telling me this?"
    r "As long as you don’t tell her I told you, I don't think there's a problem with it."
    r "If anything, I see it as kind of a favor. Who knows when she'd tell you on her own?"
    s "How is revealing a friend's secret a favor, exactly?"
    r "Because now that you know someone as cute and cuddly as Futaba is attracted to you, aren't you tempted to take things a little further?"
    s "Is that...actually something you're okay with?"

    scene cafeten8
    with dissolve

    r "Hm? Why wouldn’t it be? If it makes the two of you happy, I’m all for it."
    s "That’s...a little unexpected."

    if bonus == True:
        s "You do realize how much older I am than you, right?"
    else:
        s "She is your friend and you should be vigorously screening all of her potential love interests to ensure that she is good hands."
        s "Also, I am, her teacher."

    scene cafeten9
    with dissolve

    r "Mm...That kind of stuff doesn't really matter to me."
    r "I'm sure it wouldn't really fly in school, but it's not my business to tell you where you can and can't stick your wiener."
    r "I know if {i}I{/i} had a wiener, {i}I'd{/i} want to stick it in Futaba. She smells nice and her skin is really soft."
    s "This is a side of you I did not expect to come out today."
    r "I regret nothing."
    h "Rin, are you almost done over there? Your break ended five minutes ago."

    scene cafeten18
    with dissolve

    r "Ahh...shoot. I didn't realize what time it was. I've gotta get back to work."

    scene cafeten14
    with dissolve

    r "Try and get some sleep tonight. Okay, Sensei?"
    r "And remember to not tell Futaba what I told you or I will sell your organs for discounted rates on the black market."
    s "You really scare me sometimes, Rin."
    r "Good."

    scene black
    with dissolve2

    "I follow Rin back to the counter to dispose of my remaining coffee and watch her disappear into the kitchen."
    "Haruka, still in an apparent state of shock after giving me her name only to be robbed of mine, stares blankly at me as I nod to her once more and make my way out of the cafe..."

    stop music fadeout 3.0

    $ renpy.end_replay()
    $ cafe10 = True
    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe15:
    scene cafe_day
    with fade
    play music "cafe.mp3" fadein 3.0

    r "Next customer, please!"

    "..."

    scene cafe1
    with fade

    r "Oh hey, Sensei. What’s up?"
    s "Morning, Rin. Just stopping by to play my weekly game of coffee-roulette."

    scene cafe4
    with dissolve

    r "Well, you’re in luck because I’m actually about to clock out."
    s "Already? Are you getting your hours cut or something?"

    scene cafe6
    with dissolve

    r "Huh? No, it’s nothing like that."
    r "Haruka would never cut my hours. I’m too good at this stuff."
    r "So good that I have {i}two{/i} shifts, actually. I just need to clock out between them for a doctor's appointment."

    scene cafe4
    with dissolve

    r "But, hey! Drop by again later and you can get all the Rin you want!"
    s "A doctor’s appointment? Is something wrong?"

    scene cafe3
    with dissolve

    r "Oh, nah. It's no big deal. Just some...check-up sorta thing. You don’t need to worry about it."
    s "Well, I'm not going to try and get involved where I'm not welcome. Hope it goes well, though."

    scene cafe4
    with dissolve

    r "I'm sure it will!"
    r "So, what can I get for you today, sir?"
    s "I appreciate that you still ask even though we both know you aren’t going to listen."
    r "Just doing my job, Sensei!"

    "Are you really, though?..."

    scene black
    with dissolve

    "I choose a random drink off of the menu and prepare myself for whatever it is Rin will be making for me today."
    "Considering that her last drink wasn't as solid as the preceding ones, I'm thinking that this time-"

    r "Done!"

    scene cafemocharedux1
    with dissolve

    s "What? Already? But I haven't even sat down yet."
    r "Yup! Here ya go! One cafe mocha!"
    s "Like...a normal cafe mocha? With nothing weird about it?"
    s "Did you just have one left over from another customer or something?"
    r "Nope. Just the greatest barista in the world working extra hard to deliver quality beverages to her favorite teacher."
    s "..."
    r "...What?"
    s "Are you dying or something?"

    scene cafemocharedux2
    with dissolve

    r "What? Of course not. I told you it was just a check-up."
    s "Then why are you giving me a normal drink? Have I done something to offend you?"

    scene cafemocharedux3
    with dissolve

    r "No...it's not like that. I just wasn't really feeling creative today."
    r "But if you really want, I can go dump a bunch of stuff into a cup and see how that comes out instead. Just didn't wanna give you something I couldn't put my heart into, you know?"
    s "I don't think that's necessary. I'm just a little surprised to see you going through such a slump."

    scene cafemocharedux4
    with dissolve

    r "A...slump?"
    s "Maybe that's not the right word for it. You've just seemed a little out of sorts lately."
    r "Out of sorts?"
    s "Besides, I thought you loved making weird drinks and laughing silently to yourself as I test them before anyone else."

    scene cafemocharedux5
    with dissolve

    r "I do, though. Just not today, okay?"
    s "You know you can talk to me if-"
    r "Didn't I like, just tell you the other day that I was fine? You don’t have to worry about me, Sensei. Really."
    s "It’s not just me, though. Chika is worrying about you too."

    scene cafemocharedux6
    with dissolve

    r "Wait...what? Chika is...worrying about {i}me?{/i} Are you sure? What if she was talking about another Rin?"
    s "I really don't think she was."
    r "But why? Like, how does she even know something is wrong?"
    s "I thought nothing was wrong?"
    r "Yeah, that. That's what I meant to say. Why does she think that something is wrong?"
    s "Because you keep getting all weird around her."
    s "She's noticed that you haven't been acting like yourself and seems to think it might be her fault."
    r "She thinks...it's {i}her{/i} fault?"
    s "That’s not the case though, is it?"
    r "Of course that's not the case. It's just..."

    scene cafemocharedux7
    with dissolve

    r "Hah..."

    "I decide to let Rin stay quiet for a little while as she figures out the best way to talk about this."
    "When she remains quiet for an uncomfortable amount of time, though, I decide it might be best to provide a little positive reinforcement..."

    s "Take your time, Rin."
    s "I’m not going anywhere anytime soon. So if you-"

    scene cafemocharedux8
    stop music

    r "Sensei, do you ever have any thoughts that you wish you didn’t?"
    s "..."
    s "What do you mean exactly?..."
    r "You know. Like, stuff that pops into your head that you realize shouldn’t be there but, like..."
    r "You can’t really do anything about it."

    if roomwithtrack == True:
        scene newroom1
        with flash
        play sound "static.mp3"
        scene newroom9
        with flash
        scene newroom17
        with flash
        scene newroom8
        with flash
        scene cafemocharedux8
        stop sound

        s "I guess I do sometimes."

    else:
        play sound "static.mp3"
        scene whygodwhy
        with flash
        scene cafemocharedux8
        stop sound

        s "Maybe every now and then, sure."

    r "Okay."
    r "Good."
    r "Well, {i}not{/i} good. But I’m at least glad that I’m not the only one it happens to."
    s "Do you want to talk about what you’re-"
    r "Not really. But thanks."

    play music "cafe.mp3"
    scene cafemocharedux1

    r "You know what? Why don't we just talk about something else?"

    play sound "static.mp3"
    scene happy1
    with flash
    scene happy2
    with flash
    scene happy3
    with flash
    stop sound
    scene cafemocharedux9
    with flash

    r "{b}Like the inevitable collapse of our relationship when you start fucking the girl I habitually touch myself to.{/b}"
    r "{b}Or the ever present, looming darkness bubbling up inside of us. Expanding in size until it's brave enough to crawl through our throats.{/b}"
    r "{b}Frothing like the foam atop a cafe mocha.{/b}"
    r "{b}A window of the waking mind, thick with saliva and the remnants of days gone by.{/b}"
    r "{b}Why don't we talk about that?{/b}"
    r "{b}Or better yet-{/b}"

    scene cafemocharedux10
    stop music

    r "why dont we talk about nothing"

    play sound "alert.mp3"
    scene colorbars
    $ renpy.pause(4, hard=True)
    play sound "static.mp3"
    scene happy1
    with flash
    scene happy2
    with flash
    scene happy3
    with flash
    scene cafemocharedux11
    with flash
    stop sound
    play music "reversecafe.mp3"

    "//////////////////TERMINAL 23 IS EXPERIENCING A DISRUPTION IN SERVICE"
    "//////////////////A SUSPICIOUS AMOUNT OF FAILED LOGIN ATTEMPTS HAVE BEEN MADE"
    "{s}//////////////////PLEASE RENEW YOUR MEMBERSHIP IN ORDER TO{/s} NO"
    "GREETINGS, YOU ARE HIGHLY FAVORED"
    "GAZE AT THE MARTYR BEFORE YOU AND TELL ME WHAT YOU SEE"
    "IS THIS STRENGTH???"
    "OR IS THIS SOMETHING ELSE???"
    "THIS IS WHAT BECOMES OF THOSE WHO CAN NOT WALK ON THEIR OWN TWO FEET"
    "THIS IS WHAT BECOMES OF THOSE WHO LEAD INSTEAD OF FOLLOW"
    "THE WAY OUT IS LIT WITH THE LIGHT OF A THOUSAND SUMMERS"
    "HOW MANY OF THEM WILL YOU SEE???"
    "WHO WILL BE DRAGGED DOWN WITH YOU???"

    scene cafemocharedux12
    stop music

    "IF I TOLD YOU THE ANSWER, WOULD YOU EVEN BELIEVE ME???"
    "OR WOULD YOU RATHER THE DREAMS REMAIN???"
    "SHE HURTS WHILE SHE WAITS"
    "HER BODY IS FULL OF NEW GUINEA FLATWORMS"
    "GIVE HER WHAT SHE WANTS"
    "FILL HER WITH YOUR CUM"

    scene cafemocharedux13
    play music "cafe.mp3"

    s "{s}Why won’t you tell me what's wrong with you?{/s} Sure. What would you like to talk about instead?"
    r "Thanks, Sensei..."
    r "And, umm...this is probably pretty predictable...but since we're already on the topic..."

    scene cafemocharedux14
    with dissolve

    r "Did...Chika say anything else about me?"
    s "Hmm...Well, it’s not like we really had a lot of time to talk when you were only gone for a couple of minutes."
    r "But like...she hasn't said anything about me apart from when the three of us were here together?"
    s "Not really. Nothing worth mentioning, at least."

    scene cafemocharedux15
    with dissolve

    r "UGH. Fuck my life."
    s "So...how long have you had a crush on her?"

    scene cafemocharedux16
    with dissolve

    r "Hah...Was only a matter of time until you figured it out."
    s "I had a feeling ever since I caught you staring at her in the hallway. What I didn't know was how long you've felt this way."
    r "I literally have not stopped thinking about her for like two years."
    s "Interesting choice, Rin."
    s "I mean, Chika’s definitely cute. She just seems like the complete polar opposite of you."

    scene cafemocharedux8
    with dissolve

    r "I mean, she’s not {i}that{/i} different, is she? We’re both girls and we both...like...you know..."
    r "..."

    scene cafemocharedux6
    with dissolve

    r "Holy shit. We’re nothing alike, are we?"
    s "Did...that really not ever occur to you?"
    r "Not even once."

    "How?..."

    s "Either way, I’m glad it's finally out in the open."

    scene cafemocharedux17
    with dissolve

    r "Let's...not use the word {i}open{/i} just yet. Because if you leak this to anyone, I will chop your body in half and feed it to sharks."
    s "Deal."
    r "Oh, and don’t try and steal her from me either! I see the way you look at her sometimes!"

    if chikatownfirst == True:
        "Yeah...it might be a little too late for that."

    else:
        "I don’t think I’ve looked at Chika any differently than the others?..."

    s "I'll stay away, but...do you even know if she's into girls?"
    r "..."
    s "..."

    scene cafemocharedux18
    with dissolve

    r "You're really killing my vibes today, Sensei. I don't appreciate it."
    s "I think what I asked was a pretty decent question, Rin."
    r "All girls are at least {i}kind of{/i} into other girls! I mean...come on!"
    r "Have you {i}seen{/i} girls? How can you not be?!"
    r "But even if she pretends she isn't! Keep your hands to yourself until she properly rejects me!"

    if chikadorm20 == True:
        "I obviously can't find it in myself to tell Rin that Chika and I are already a little more than just friends."
        "But even if Rin had come to me with this request before all that, would it have changed anything?"
        "When have I ever allowed my choices to be guided by the hands of others?"
        "Chika and Rin have known each other for a long time now."
        "If anything was going to happen..."
        "Well, I think it would have happened already."

    s "Are you actually planning on asking her out?"

    r "Well...yeah. Eventually."
    r "I just don't know when."
    s "..."

    scene cafemocharedux19
    with dissolve

    r "What?! Stop judging me! I’ve never done something like this before! I don’t know what the correct order to do things in is!"
    r "And like you said, I don’t even know if she’s into girls yet! Let alone {i}me{/i}."
    r "She’s probably just being friendly with me like she is with literally everyone else but my stupid brain is all like “AHHH CHIKA!” or whatever."
    s "This sounds a little more serious than just a normal crush."

    scene cafemocharedux8
    with dissolve

    r "I have an actual folder of her Instagram photos saved on my laptop."
    s "You...do realize that's essentially stalking, right?"
    r "Nuh-uh. I'm nice. Stalkers aren’t normally nice. Probably."
    r "I'm sure some are. But I'm not one of them. Probably."
    s "You can't just keep adding {i}probably{/i} to the ends of sentences to dodge blame, Rin."
    r "Sure I can. Probably."
    s "..."
    r "..."

    scene cafemocharedux20
    with dissolve

    h "Rin, you can head out now! I’ve got it from here. And thanks again for coming in to open."
    r "No prob, Haruka! I’ll be back later! Probably!"
    h "Wait, what do you mean probably?"

    scene cafemocharedux1
    with dissolve

    r "I guess I’ll...see you later, Sensei."
    h "Rin, seriously! What did you mean by that?"
    r "And sorry if I've been acting weird and making you worry lately. I really do appreciate that you're looking out for me."
    r "I'm sure I'll be back to normal in no time at all and you'll be free to become my {s}NEW GUINEA FLATWORM{/s} guinea pig once more."
    s "Sounds good. Best of luck with your check-up."
    r "Gracias, mi amigo. ¡Adiós!"

    scene black
    with dissolve2

    "Rin quickly grabs her bag from behind the counter and rushes out of the cafe."
    "I watch her jog down the street toward the bus stop and decide it’s best to stay inside for a little while longer so I don't have to awkwardly pass by her again."
    "Or at least that's what I intend to do before the thought of her and Chika together forces me into the bathroom for several minutes before I decide to go home."

    $ renpy.end_replay()
    $ cafe15 = True
    $ rin_love += 1
    $ lettert = True

    "{i}You masturbate to a lesbian fantasy and Rin’s affection increases to [rin_love]!{/i}"

    stop music fadeout 5.0

    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe20:
    scene cafetwentyredux
    with dissolve

    s "..."
    r "..."

    "Rin spots me from behind the counter but, instead of calling out to me, she just...turns around."
    "No. She turns around and {i}pretends to start cleaning something.{/i} Which is an obvious sign that she doesn't want to talk to me...but why?"
    "I can't recall doing anything wrong, but I guess it's in my nature to sort of do things like that without realizing."
    "She's one of the last people I'd expect to just avoid me, though."

    s "..."

    "Or maybe it's something that doesn't involve me at all?"

    scene black
    with dissolve2

    "Maybe, in my selfish obsession with all things flowing into me, I just expected it to be."
    "And meanwhile, she's drowning in a different lake."
    "........."
    "......"
    "..."

    scene cafesad1
    with fade
    play music "lastdailysong.mp3" fadein 8.0

    r "{i}Mm...{/i}"
    s "Rin?"
    r "Oh, S-Sensei! Fancy...meeting you here."
    r "How are you doing this morning? Everything good? Have any...cool dreams or something?"
    s "I’m fine."
    s "The real question is how are {i}you?{/i}"
    r "Oh, you know...Pretty good. Can't complain."
    s "I see."

    "Obviously, I know that's not true."
    "It's not like Rin to just...hide away."
    "At the same time, though...what do I even know about her to begin with?"
    "It's not like I've experienced what becomes of her in times of crises before. This could just be par for the course."
    "But, if that's the case, why do I still feel compelled to push further when that is likely the last thing she wants me to do?"

    play sound "static.mp3"
    scene happy9 with flash
    scene cafesad1 with flash
    stop sound

    s "How was your doctor’s appointment the other day?"
    s "I never got a chance to ask you."
    r "Uhh...pretty good, I guess. Blood pressure is fine. BMI is fine. You know the deal."
    s "Good to hear."
    s "Would you mind turning around by any chance? It feels kind of weird talking to the back of your head."
    r "Yeah...about that..."
    r "I actually...kind of {i}would{/i} mind. I don’t look so great today."
    s "I’m not here to judge a beauty pageant."
    r "That's good, because I wouldn't even make it past auditions looking like this."
    s "Just turn around, Rin."
    r "Why do I have to?..."
    s "Because I don't care what you look like right now."

    scene cafesad2
    with dissolve

    r "But that doesn't mean it isn't weird for me..."
    r "I just don’t want you to think anything’s going on or whatever because I know you were already worrying and stuff."
    r "So like, if you want to just order something and leave your money on the counter, that’s-"
    s "Rin. Turn around."
    r "..."
    r "Okay, but if you run away, my feelings will be really hurt."
    s "I won’t run."
    r "..."
    r "Then..."

    play sound "static.mp3"
    scene cafesad3
    with flash
    stop sound

    r "Good morning..."

    "..."
    "She wasn’t kidding when she said she didn’t look good today...It looks like she hasn’t slept in weeks."
    "She’s drenched in sweat and her eyes are swollen so badly that she can't even fully open them."

    s "Good morning, Rin."

    scene cafesad4
    with dissolve

    r "So, uhh...how bad is it?"
    s "It’s, uhh..."
    s "Let’s just say you’ve had better days."

    scene cafesad5
    with dissolve

    r "{i}Mm...{/i}"
    r "I feel fucking gross...I haven’t even showered in like a week."
    s "Are you really okay to be working right now?"

    scene cafesad3
    with dissolve

    r "Yeah, I'm good..."
    r "Besides, I can't let Haruka run the place by herself since the only other girl on the schedule for this morning called out today."

    scene cafesad6
    with dissolve

    r "Oh, and if you could forget you ever saw me like this, that would be nice. Thanks."
    s "I’m not sure if that’s possible."
    s "Are you...really okay?"

    scene cafesad3
    with dissolve

    r "Well, it’s not like you’ve been believing me even when I say yes, so..."
    s "..."

    "The two of us stand there in silence for an uncomfortable amount of time before I feel the need to speak up again."
    "I doubt she'll bite, but I at least need to cast some sort of lure that might tempt her to...go home or..."
    "I don't know. I should probably learn literally anything about fishing before attempting to make fishing analogies."

    s "You should ask to go home. I’ll work the rest of your shift for you if I really have to."

    scene cafesad5
    with dissolve

    r "Sensei...I know you’re worried, but you really don’t have to do that..."
    r "I’ve been through much worse and you don’t even know the drinks...this job isn't something you can just jump into, you know."
    r "You need tons of training and..."
    r "I’ll be okay."
    r "I promise. I just need a few minutes to-"
    s "Stop saying you’re going to be okay when you have no idea if that's true or not."

    scene cafesad7
    with dissolve

    "Rin stops speaking and jolts up in surprise."

    r "Huh?..."
    s "I’m not going to pretend to know how you feel or even...what's going on. But I'm pretty damn sure that forcing yourself to stay out in public isn’t going to help."
    s "Get out of here. Go lay down. Try to get some rest. Do literally anything."
    r "I'm not-"
    s "When was the last time you slept?"
    r "That's..."

    scene cafesad4
    with dissolve

    r "Um...three days ago?"
    r "Four, maybe?..."
    r "A week?"
    s "Why? What’s keeping you awake?"
    r "That’s not exactly easy to answer, Sensei..."
    r "And I don’t really want to talk about it so..."

    scene cafesad3
    with dissolve

    r "If you could like...maybe just give me a little space or something..."
    s "Will that help you?"
    r "Well...it won’t {i}hurt{/i} me..."

    "The sound of hurried footsteps rounding the corner suddenly interrupts our conversation."

    scene cafesad8
    with fade

    h "Rin, please go home...Molly is going to come in and work for you."
    r "Molly? Seriously? There's no way you and Molly can work an opening shift yourselves. That's only slightly better than you working alone."
    h "I'll figure it out. And Rin, if you’re ever not feeling well...please let me know."
    h "I can’t make you work when you’re like this."

    scene cafesad8r
    with dissolve

    r "I can do it, though! Really!"
    r "I just...didn’t have time to do my makeup this morning!"
    h "And you look beautiful even without it. That’s not why I’m sending you home."
    h "I don’t want you to have to worry about helping customers on top of whatever else is going on right now."
    h "So do as your teacher says and go get some rest, okay? "

    "Was...Haruka listening this entire time?"

    h "We’ll talk more about your schedule as soon as you’re feeling better."
    h "Until then, I'm going to have to take you off."

    scene cafesad9
    with dissolve

    r "Ngh-!"

    "Rin clenches her teeth, frustrated by the sudden realization of her weakness not just to her peers, but to herself."
    "Why she wants to keep picking at a wound before it's even had the chance to scab over, I don't know."
    "But watching that won't do any of us good and will only make the healing process that much harder if it's ever given the opportunity to start."
    "Before us lies a girl on the verge of breaking and all we can do is attempt to cushion the blow as she's hurled from the twenty-third story of a building we can't see the top of."
    "I say, as if I made any sort of difference at all."

    scene cafesad10
    with dissolve

    r "I’m sorry, Haruka..."

    scene cafesad11
    with dissolve

    r "I’m sorry, Sensei..."
    r "I'll..."

    scene cafesad11r
    with dissolve

    r "I’ll get better soon! I promise!"

    scene black
    with dissolve2

    "Rin quickly grabs her things from underneath the counter and runs out of the store in the direction of the dorms."
    "I hope she's able to get some sleep once she arrives but, at this point, who's to say if she will?"
    "Haruka lets out a heavy sigh as if the weight of the world has been lifted off of her shoulders before turning her attention to me and displaying an expression halfway between exhausted and distressed."
    "For a moment, it's almost like looking into a mirror."

    scene cafesad12
    with dissolve2

    h "..."
    s "Are you going to be okay with just you and that Molly girl?"
    h "Not a chance in hell...But you saw Rin. I couldn’t just let her stay here in that condition..."
    h "I swear, she can be so...fucking stubborn sometimes...Is she like that in[school] too?"
    s "Not that I’ve seen. She zones out in class a lot but, most of the time, she's extremely energetic."
    h "I see...I take it that she hasn't told you the specifics then either?"
    s "She won’t tell me anything."
    s "All I know is that sometimes she ‘thinks things she shouldn’t.’"

    scene cafesad13
    with dissolve

    h "Don't we all kind of do that from time to time, though?"
    s "Maybe. It's hard to tell exactly what she meant by it since she just sort of stopped talking about it a few seconds later."
    s "I’ll go and check on her soon, though."

    scene cafesad14
    with dissolve

    h "Good...I think she’d like that."
    h "She talks about you a lot, you know?"
    h "Ever since you started coming to the cafe. Now, every time you show up she gets really excited and won't shut up about you for like, an hour afterward."

    "I didn't realize there was even an hour worth of things to say about me?..."

    h "Honestly, I’ve never seen her get that way with anyone before. Not even that blonde girl she has a crush on."
    s "Oh. You know about that too?"

    scene cafesad15
    with dissolve

    h "Of course. I mean, she hasn’t {i}told{/i} me or anything. But it’s not like she’s doing a great job of hiding it."
    s "Yeah, I guess she does get a little panicky whenever something involving Chika comes up."
    h "Ahh, right. Right. Chika was her name. Thanks for reminding me."
    h "I promise that I won’t tease her about it when she’s back to normal."
    s "We can tease her about it together. I’m sure she'll be back to her normal routine in no time at all."

    scene cafesad14
    with dissolve

    h "Yeah...I’m sure we will..."

    "Haruka pauses for a moment."
    "Her eyes scan the room, but not in a way that makes it look like she's searching for customers or tables to be cleaned."
    "It's a way that makes it seem like she's about to do something she doesn't want anyone to know about."

    scene cafesad16
    with dissolve

    h "Hey...so this might sound a little weird or something...but do you think you could maybe let me know whenever you {i}do{/i} check on Rin?"
    h "Just so I can know for sure she's fine."
    s "Why would that sound weird? And sure. I can try. I can’t guarantee I’ll be here every day, though."
    h "Well, yeah. That's the part where it gets kind of weird since...I was going to ask that you take down my number and just...text or call instead."
    s "Sure. I can do that."

    scene cafesad17
    with dissolve

    h "Oh, really?! C-Cool! Yeah...Yeah, that’s totally great."
    h "Let me...uhh...let me get a pen or something. I'll be right back."

    scene cafesad17r
    with dissolve

    "Haruka...seems to forget that physically writing down phone numbers isn't necessary anymore and sets off to find a {i}pen or something.{/i}"
    "She's able to find one without much effort and then proceeds to scribble down her number on the back of a napkin."
    "There’s a slight hesitation between each digit, as if she’s trying to convince herself it’s okay to be doing this."
    "Of course, I think it is."
    "Though I may be immensely biased."

    scene cafesad14
    with dissolve

    h "Okay, here you go."
    h "I’m kind of busy during the day, so....if I don’t answer right away, it’s nothing personal."
    s "Got it. I’ll be sure to let you know if anything happens with Rin."
    s "That aside, do you want me to hang around until Rin's cover gets here?"
    s "Because I told her earlier that I wouldn’t mind helping out a bit if necessary, but I can't guarantee I will be of any {i}actual{/i} help whatsoever."
    h "No, no, no. It’s fine. I’ve worked alone before. I actually think it’s kind of relaxing."

    scene cafesad15
    with dissolve

    h "Just go cheer up my employee already. She needs it."
    s "Works for me."
    s "It was nice talking to you, Haruka."
    h "You too. I look forward to...further communication."
    s "..."

    scene cafesad16
    with dissolve

    h "I'm sorry. I have no idea why I said it like that."
    s "Yeah, that was weird."
    s "Anyway, see you later."
    h "Y-Yeah...Later."

    scene black
    with dissolve2

    "I leave the cafe without ever purchasing a drink."
    "It wouldn't be the same if it wasn't Rin who made it."

    $ renpy.end_replay()
    $ cafe20 = True
    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label rincafegone:
    scene cafesad14
    with dissolve
    play music "cafe.mp3" fadein 3.0

    "Rin isn't working today, so I wind up talking to Haruka instead."
    "We make idle chat about a few random things, but wind up spending the bulk of the conversation
    talking about Rin herself."
    "It seems like Haruka might be even more worried about her than I am."
    "I hope everything turns out okay. My mornings just aren't the same without the rush brought on by coffee-roulette."

    scene black
    with dissolve

    "Haruka tells me that she'll let Rin know I dropped by the next time she sees her."
    "I should keep checking back until my normal barista is on her feet again..."

    $ rin_love += 1
    stop music fadeout 3.0

    "{i}Rin later finds out that you stopped by and her affection increases to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe25:
    scene gooddayredux1
    with dissolve
    play music "cafe.mp3"

    "Another morning at the cafe means another chance to be poisoned by an overly creative and mildly intimidating barista."
    "But upon entering, I realize that Rin isn’t behind the counter."
    "In fact, {i}no one{/i} is behind the counter."
    "No one is in the cafe at all..."
    "What exactly is going on here?"

    r "Hey, {i}loser.{/i} Can’t you read?"

    scene gooddayredux2
    with dissolve

    s "What's going on? Where is everyone? Also, don't call me a loser."
    r "I'll call you whatever I want to call you, loser. And what, was the big sign on the door saying we're closed today not enough to tip you off?"
    s "Why are you closed? It's just a random weekend."
    s "Also, why are you here if you're closed? And why are you wearing your casual clothes?"
    r "Damn, Sensei. Didn't realize we were gonna be playing twenty questions today. You know you can just ask me what color my underwear is, right? You don't have to beat around the bush."
    s "Wait, I can?"

    scene gooddayredux3
    with dissolve

    r "No. But I thought I'd be a good friend and give you some hope since I can't give you any coffee today."
    s "What good is hope if you're just going to take it away immediately?"
    r "I don't know, homie. Ask the Rin floatin' around in your fantasies later. She'll probs know better than I do."
    s "...Homie?"
    r "Sorry. I meant to say Sensei. I mix those two words up all the time."
    s "I feel like that would be mildly problematic if you had literally anyone else as a teacher."
    r "Well, I guess I'm lucky I ended up with you then, huh?"
    s "I guess so..."
    s "For real, though. Why are you closed?"

    scene gooddayredux4
    with dissolve

    r "Repairs or something, I think. Wasn't really informed of the full details."
    r "All I know is that Haruka needed somebody to come in and tidy stuff up before the repair people came and I just happened to have some extra time on my hands this morning."

    scene gooddayredux3
    with dissolve

    r "Lucky for you, I've got even {i}more{/i} spare time now since I've already finished up everything that needed to be done."
    s "Do you mean we're actually going to spend the morning together with you {i}not{/i} in that funny visor?"

    scene gooddayredux5
    with dissolve

    r "Woah, there! What did my visor ever do to you? You can't just talk crap on it like that."
    s "I blame the lack of caffeine. So, in a roundabout sort of way, it's actually your fault I said that."

    scene gooddayredux6
    with dissolve

    r "Well, I don't follow that logic at all. But if you want coffee, we can get some on the way. There are plenty of cafes between here and the urban district."
    s "What? We're going all the way over there?"

    scene gooddayredux2
    with dissolve
    stop music fadeout 10.0

    r "Hell yeah, man. I wanna walk around the city."
    r "I haven’t been getting out much lately and I need some exercise before my limbs fall off or stop working or something."
    s "Neither of those things happen due to lack of exercise but sure, I guess I’ll walk around with you."
    r "Neat! Well, I'm ready whenever you are."
    r "Oh, and the answer was black, by the way."
    s "The answer to- oh."

    scene gooddayredux3
    with dissolve

    r "You're welcome, homie."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene gooddayredux7
    with dissolve2
    play music "justbehappy.mp3" fadein 4.0

    "Rin and I spend some time walking around the more...{i}metropolitan{/i} section of Kumon-mi."
    "It's not one I venture too often, so I wind up sticking close to her as she leads us...well, wherever she's in the mood to lead us, I guess."
    "So far, that has equated to nothing but anime stores where she proceeded to freak out about the prices of things before getting upset and leaving."
    "This has happened five times now and I still do not have any coffee."

    scene gooddayredux8
    with dissolve

    r "Who shoved a stick up your butt, Mr. Crankypants?"
    s "..."
    s "Excuse me?"
    r "You've barely said anything since we left the cafe. Am I {i}boring{/i} you, Sensei?"
    r "Or are you just a little embarrassed to be walking around with a moderately cute girl?"
    s "I'd rank you several levels above moderate, Rin."
    r "Why, that's the nicest thing anyone has ever said to me. Thank you, Sensei."
    s "You're welcome. Can I get coffee now?"

    scene gooddayredux9
    with dissolve

    r "Oh, crap! I totally forgot!"
    r "Why didn’t you say anything sooner?!"
    r "I even dragged you into that one anime store that you were totally uninterested in!"
    s "It was five."
    r "Five?! Why did you let me carry on for so long?!"

    scene gooddayredux10
    with dissolve

    r "You need to be more open about your needs, Sensei."
    r "If this relationship is ever going to work, we're going to have to keep each other in check."
    s "Using the word {i}relationship{/i} makes it sound like we're more than just friends, you know."

    scene gooddayredux11
    with dissolve

    r "But...we are, aren't we?"

    "Rin pauses for a moment as her face begins to redden and her eyes get locked on mine."
    "I know this face. She’s about to confess her-"

    scene gooddayredux12
    with dissolve

    r "Homies."
    s "..."
    r "..."
    s "Why do you keep saying that all of a sudden?"
    r "What?! You said we're just friends, but we're so much more than that! Homies are like...four steps above friends."
    r "But I guess you probs wouldn't know that since you're such a friggin' boomer."
    s "Why am I being bullied today? All I wanted was coffee."
    r "And all I want is a cute gyaru girlfriend with fishnets and a cell phone addiction."
    r "I guess we can't always get what we want, though, can we?..."

    scene gooddayredux8
    with dissolve

    r "Buuuuut...since I’m the greatest and coolest homie in the entire world, we can stop for coffee at the next cafe we see."
    r "And I just so happen to know a pretty good place right around the corner and-"

    scene gooddayredux13
    with hpunch

    r "Ah-!"

    "Rin suddenly stops walking when something catches her attention."

    r "Holy shit."
    r "Holy shit. Holy shit. Holy shit."
    s "What? What's wrong?"
    r "We..."
    r "We have been graced by the presence of an angel..."

    scene omgkaori1
    with fade

    "Rin lunges forward toward the {i}angel{/i} who is none other than the Queen of Spiders herself- Kaori."
    "I'm surprised to see this sort of reaction out of her, though."
    "I get that Rin is {i}incredibly{/i} attracted to girls, but the way she's acting toward Kaori makes it seem like-"

    r "Oh my god! No friggin’ way! Kaori?! Is that really you?!"
    k "H-How do you know my name?! Who are you?!"
    k "Identify yourself!"
    s "Uhh...what’s going on here, exactly?"

    scene omgkaori2
    with dissolve

    k "Hamburger Man! Help! I am under attack!"

    scene omgkaori3
    with dissolve

    r "...Hamburger Man?"
    s "It’s better to not ask."
    s "How are you doing, Kaori?"
    k "Horrible! I require immediate assistance and will pay you in meat for the favors you will perform today!"
    s "And what exactly do you need immediate assistance with? You’re not actually under attack."

    scene omgkaori4
    with dissolve

    k "I’m...not under attack?"
    s "Of course not. Rin's just a mildly annoying, extraordinarily horny teenager."
    r "It's true. I really am."
    s "Rin, would you mind explaining how you know Kaori? Because she...definitely does not seem like she knows you."
    s "Was she your waitress before or something?"

    scene omgkaori5
    with dissolve

    r "Waitress? Are you kidding? She’s like, a totally famous Instagram model!"
    k "A...what?"
    k "What is this ‘instant gram’ you speak of, extraordinarily aroused girl? Explain yourself."

    scene omgkaori6
    with dissolve

    r "Sensei, remind me to show you her page later! She takes tons of super cute pictures of all kinds of stuff."
    s "I'm good. Not really big on social media."

    scene omgkaori7
    with dissolve

    k "Media can talk?!"
    r "You sure? There's a bunch of risque underwear pics on there that you'll be missing out on..."

    if bonus == True:
        s "My interest in this conversation has suddenly skyrocketed."
    else:
        s "Keep them away. I want no part of this."

    k "What does that strange word mean? {i}Risque?{/i}"
    s "It means sexy."
    k "Sexy?! Tell me it is not so, Hamburger Man!"
    s "Rin, how risque are these photos exactly?"
    k "Why do you not show more concern for my well-being when I am in a clear state of crisis?!"
    r "There aren't like, nudes or anything. Just some closeups of her tattoo and a bunch of pictures of her trying on different types of underwear."
    k "This can not be true! I do not even know what an instant gram is! "
    k "The only pictures I have inserted into the digital world have been for the sake of personal documentation of my journey through this planet!"

    scene omgkaori9
    with dissolve

    r "Wait...I kinda feel like you’re being serious right now."
    r "You haven’t actually been...posting all of those pictures on accident, have you?"
    s "Are we really not going to question why she’s been taking pictures in her underwear for ‘personal documentation?’"

    scene omgkaori10
    with dissolve

    k "Whose team are you on, Hamburger Man?!"

    if bonus == True:
        s "I’m on the team that wants to see those pictures."
    else:
        s "Whichever team is closest to the parking lot. I get embarrassed after playing sports and like running away as soon as games end."

    k "Those pictures are not to be seen by the prying eyes of a human male such as yourself!"

    scene omgkaori11
    with dissolve

    if bonus == True:
        k "Even if you are a prime mating specimen who I am extraordinarily attracted to!"
    else:
        k "Even if you are extraordinarily attractive!"

    r "Ah-"
    s "..."
    k "..."
    r "..."
    k "What?! What is the reason for this sudden silence?!"
    k "I am not yet familiar with human conversation! Is openly discussing mating rituals not acceptable behavior?!"

    scene omgkaori12
    with dissolve

    if bonus == True:
        r "Sensei...I think Kaori wants to...{i}mate with you...{/i}"
    else:
        r "Sensei...I think Kaori has a crush on you..."

    k "I...I said no such thing!"

    scene omgkaori13
    with dissolve

    r "Can I...maybe...watch?"
    k "You may watch nothing! You are already aroused enough! Any more will result in spontaneous combustion!"

    if bonus == True:
        s "I don't mind if you watch, Rin. Kaori and I are ready to mate whenever."
    else:
        s "I also do not understand what she wants to watch. You can not {i}see{/i} people have feelings."

    scene omgkaori15
    with dissolve

    if bonus == True:
        k "I will not mate with you, Hamburger Man! I have yet to even discover what the instant gram is!"
    else:
        k "I do not have feelings!"

    k "Too much remains undone! My body is simply not prepared!"
    r "Kaori...wants you...to prepare her body..."

    scene omgkaori17
    with dissolve

    k "You should be referred to as the extraordinarily dishonest girl instead! The lies drip from your mouth like water from a leaky faucet!"
    r "Sensei...what will you do?"

    menu:
        "Prepare Kaori’s body":

            $ kaoriprepared = True

            s "I suppose I’ll have to do what must be d-"

            scene omgkaori18
            with dissolve

            k "You will do no such thing!"

        "Don’t do that thing":

            $ kaoriprepared = False

            s "I’m not sure if she’s ready yet, Rin..."
            r "Maybe...{i}I{/i} can help her get ready then?..."

            scene omgkaori19
            with dissolve

            k "Do not come near me, heathen!"

    scene omgkaori20
    with dissolve

    k "Why must so many confusing things happen today of all days?!"

    scene omgkaori21
    with dissolve

    r "Is something wrong, Kaori? Are you having a bad day?"
    k "The worst day. The woman at the pet store would not provide me a furry companion to nurture and call my own!"
    r "Why not? Did you not have enough money or something?"
    k "I have many of the moneys! And yet each attempted transaction was refused!"
    k "There is no justice in this world!"
    s "Just find an animal outside. There are plenty of them just...wandering around."

    scene omgkaori22
    with dissolve

    k "But they are so fast and I am so average-speed. I simply can not keep up."
    s "I...really don't know what else to tell you, Kaori."

    scene omgkaori23
    with dissolve

    k "Of course you do, Hamburger Man..."
    k "And yet you conceal your vast amounts of human knowledge from me."
    s "I..."
    s "What?"
    k "I do not trust you."

    if bonus == True:
        k "And I will not mate with you."

    k "And I will now leave."
    k "Good day, humans."

    scene omgkaori24
    with dissolve

    r "..."
    s "..."
    r "She’s...{i}different{/i} from how I expected her to be."
    s "Yes, Rin."
    s "Yes she is."

    scene black
    with dissolve2

    "Shortly after that, we obtained my normal human coffee and-"
    "Oh, god damn it."
    "Now even I’m beginning to sound like Kaori."
    "We bought coffee and then I walked Rin back to the dorm."
    "The end."

    $ renpy.end_replay()
    $ cafe25 = True
    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe30:
    scene cafe_day
    with dissolve
    play music "cafe.mp3"

    "I arrive at the cafe as if it’s any other day."
    "Everything is completely normal and the bubbly girl behind the counter is going to force me to drink her latest concoction. "
    "We’ll chat for a bit and probably laugh about[school] and life or whatever else is on our minds."
    "Rin will bring up her roommate and how she’s been in a much better mood as of late."
    "And then she’ll pick up her guitar from behind the counter and play the other customers and myself a song she wrote about getting over her first heartbreak."
    "It will be a wonderful day."

    play sound "static.mp3"
    scene postbeach1
    with flash
    stop sound
    stop music

    "Just kidding. Everything is horrible."

    s "..."
    s "..."
    s "..."
    s "..."
    s "..."
    s "..."
    s "..."
    s "..."
    s "..."
    s "..."
    s "Rin?..."

    play sound "static.mp3"
    scene postbeach2
    with flash
    stop sound
    play music "cafe.mp3"

    r "Surprise!"
    s "Why were you hiding underneath the counter?"

    scene postbeach3
    with dissolve

    r "Uhh...probably because I look like I was hit by a bus."
    s "You look fine. Just a little...tired. "

    scene postbeach4
    with dissolve

    r "You’re just obligated to say that because you’re my friend."
    r "I looked in the mirror this morning. I know what I saw."

    scene postbeach3
    with dissolve

    r "Crazy, right? Imagine reacting like this to something as simple as being rejected. Hahah...Hahahaha..."
    r "But...I guess that’s just how brains work sometimes."
    r "You take one little thing and just blow it up and up and up until it’s way bigger than you."
    r "Then, all of a sudden, POP!"

    scene postbeach2
    with dissolve

    r "I think, right now, I’m probably a few more pumps away from the popping stage."
    r "So as long as I’m able to not keep pumping up the balloon, I should be able to get by. No sweat!"

    "While her description of life is a bit childish, it’s not completely inaccurate."
    "Learning how to deal with your problems is 10%% acceptance and 90%% damage control."
    "Why try to fix anything when you can just consistently avoid it until it becomes a much smaller problem?"
    "The passage of time {s}heals{/s} fixes all."

    s "True, but I wouldn’t say “No sweat” when you look like you’re burning up. "
    s "Maybe you should take your hoodie off?"

    scene postbeach5
    with dissolve

    r "B-But I like my hoodie! It’s...comfortable."
    r "And it gets really cold in the kitchen."
    r "I don’t want to freeze when I go back there and wind up having to miss[school] or anything."
    s "And you’re sure it’s not because you’re using it to hide something from me?"

    scene postbeach6
    with dissolve
    stop music fadeout 15.0

    r "Is that an accusation, Sensei?..."
    s "If that’s what you want to call it."
    s "You don’t exactly have the cleanest track record when it comes to {i}not{/i} hurting yourself."
    r "Harsh."
    r "I told you on vacation that I was done with stuff like that, didn’t I?"
    s "You did. But that was prior to you crying your eyes out for an entire night and vanishing before any of us even woke up."

    scene postbeach7
    with dissolve

    r "Well what else was I supposed to do?! Wake up and pretend nothing ever happened?!"
    r "My eyes were friggin’ swollen from crying and I had a headache."
    r "I wasn’t thinking clearly then and I’m not thinking clearly now either."
    s "What did Chika even say to you to make you want to avoid her so badly?"

    scene postbeach8
    with dissolve

    r "Uhh...well, I mean, she kind of...didn’t really say anything."
    r "But I could tell from the look in her eyes that there was no chance of it ever happening."

    play music "reversecafe.mp3" fadein 3.0

    r "Then, before long I felt my head spinning. "
    r "I kept thinking things about what it would be like to be with her."
    r "And how she might act when she’s alone with the person she loves."

    scene postbeach2
    with dissolve

    r "And then I thought of you...and how lucky you are to be able to catch the eye of someone as great as her."
    r "What’s it like, Sensei?"
    r "Gaining the affection of others without ever really doing anything to {i}earn{/i} it?"
    s "I can’t tell if you’re insulting me right now..."

    scene postbeach9
    with dissolve

    r "Not insulting you. Just an observation."
    r "You’re very important to me as well but, in some way or another, I feel like you’ve {i}always{/i} been important to me."

    scene postbeach2
    with dissolve

    r "I had a crazy dream the other night, Sensei. Do you want to hear about it?"
    s "{s}No{/s} Yes."

    scene postbeach9
    with dissolve

    r "It was a dream of a new world."
    r "Well, kind of."
    r "It was the same world as this one. But it was one where we got to redo all of our mistakes."

    scene postbeach10
    with dissolve

    r "Kind of like a reset button."

    scene postbeach2
    with dissolve

    r "And in that world, after Chika rejected me, I just kept pressing the button over and over..."
    r "And over and over and over and over and over and over and over and over and over and over and over and over until I found a world where she loved me!"
    r "It took a while, but it worked in the end. I also got to experience how good of a kisser she is. "
    r "It was really hot."

    scene postbeach11
    with dissolve

    r "But then, before any good stuff happened, I woke up. "
    r "How come dreams always end before we get to the saucy stuff? "
    r "The kiss felt so real...I wanted to know what the things that come next felt like as well."

    if bonus == True:
        if rinbetrayed == True:
            scene postbeach6
            with dissolve

            r "But I guess we can’t all be that lucky...can we, Sensei?"
            r "{i}You{/i} know what she feels like, don’t you?"
            r "Do you know how she tastes as well?"
            r "I bet it’s sweet...like candy."

            scene postbeach12
            with dissolve

            r "Hah..."
            r "It’s so unfair..."
            r "I woke up so hot, too..."
            r "I almost started rubbing up against you while you were asleep just to scratch the itch...but, you know."

            scene postbeach10
            with dissolve

            r "I remembered how you broke your promise to me and all of those naughty feelings just...went away."
            r "Poof!"
            r "Funny, right? Hahaha!"

        else:
            r "But I guess there’s just no way that would ever happen..."
            r "Not to me, at least."
            r "All I can really do is hope that the dream comes back and I can press the button a few more times."
    else:
        r "I want to know what it is like to hug."

    stop music

    s "Okay, you know what? Why don't we talk about something happier?"
    s "It might be best to just...get your mind off Chika entirely for a little while."

    scene postbeach12
    play music "cafe.mp3"

    r "Fiiiiine..."
    r "But if this is one of those things where you try to pick me up on the rebound, I think I’m going to have to ask you to wait."
    r "I’m glad that you feel that way about me, but I’m still getting over a broken heart and need time to mend my wings."

    if bonus == True:
        s "Oh, come on. Even I know not to make my move that early."
    else:
        s "Oh, come on. We all know that I'm only here to hug and that I don't want any sort of romantic relationship."

    scene postbeach10
    with dissolve

    r "That gives away that you’re planning on making a move eventually, you know."

    if bonus == True:
        s "I thought that was pretty apparent since the get-go."
    else:
        s "If that move is a hug, sure."

    scene postbeach2
    with dissolve

    r "You mean you’re fine with me even if I look like this all the time?"

    if bonus == True:
        s "If you looked like that all the time while seeing me, I’m pretty sure I’d question my validity as a romantic counterpart."

    scene postbeach10
    with dissolve

    r "How’s that saying go? If you can’t handle me at my worst, you don’t deserve me at my best?"
    s "This isn’t your worst. You’re at least able to hold a coherent conversation this time. "
    s "You just look like shit."

    scene postbeach9
    with dissolve

    r "How very kind of you."
    s "Is Haruka not here or something? I figured she wouldn’t let you work in that condition again."

    scene postbeach4
    with dissolve

    r "Uhh...About that."
    r "Please don’t tell her this time...I really need the money. I’m still able to do my job, too."
    r "This sad version of Rin is a little different than the last one."
    r "It’s one thing to experience heartbreak or disappointment or whatever, but it’s a lot different when you don’t know where those feelings are coming from."

    scene postbeach10
    with dissolve

    r "I was able to prepare for this kind of pain, I guess. I’m not being blindsided by my fear of mortality, I just...really like someone who doesn’t like me back."

    "I guess she makes a good point."
    "She might look like she was dropped from the tenth story of a building in the middle of a thunderstorm but...Well, at least she’s being mature about it."
    "There is still one thing that seems to contradict that, though."

    s "If you’re so prepared to deal with these feelings now, what exactly are you hiding beneath your hoodie?"

    scene postbeach13
    with dissolve

    r "Umm..."
    r "A crutch?"
    r "There’s obviously no point in lying to you since you’ve figured it out already but...I may have impulsively awakened a bad habit when I came home from the beach."

    scene postbeach14
    with dissolve

    r "But that’s all it is...A bad habit."
    r "Just a little kick in the back to say, “Rin, get yourself back into gear. You’re still alive.”"
    r "It’s no different than any other coping mechanism. It’s just leaning on something a little...unconventional to take some of the pain away."
    s "You are aware that there are plenty of people you can lean on instead, right?"
    r "Of course I am. Which is why I’m able to smile while talking to you right now."
    r "I’m...glad that you care about me. But that doesn’t mean I can just drop habits I’ve had for years. "

    "Years?"
    "Has she really been doing things like this for that long?"

    scene postbeach2
    with dissolve

    r "Hey! How about I take my break a little early and we go sit by the window or something?"
    r "It would be nice to...get my mind off stuff for a little while. "
    r "Do you want something to drink? I’ll actually make you whatever you want this time~"
    s "Nah, that’s fine. You can just make me another one of your weird concoctions. "

    scene postbeach15
    with dissolve

    r "Heheh~ You got it!"

    scene black
    with dissolve

    "I take a seat at a table near the window and watch as Rin starts pumping a few different syrups into a cup."
    "She looks a little lost behind the counter, but I imagine that’s more due to lack of sleep than incomparable misery."
    "Before long, another girl takes her place at the register and Rin joins me at the table..."

    scene postbeach16
    with dissolve

    r "So uhh...Yeah, sorry about the whole beach thing."
    s "Why would you need to apologize for that?"
    r "Because I’m pretty sure I held onto your hand so tightly that it may have turned blue while you were sleeping."
    s "Small price to pay for making you feel a little more comfortable."

    scene postbeach17
    with dissolve

    r "I guess, but that still doesn’t mean I can’t feel bad about it."
    r "I didn’t even tell Futaba where I was. Poor girl was worried sick. "
    s "How did Futaba even know? Didn’t she go home early?"
    r "There are other girls in our class, idiot. One of them probably asked if she knew where I was that night when I disappeared into your room."

    scene postbeach18
    with dissolve

    r "Thanks for locking the door to make sure no one could bother us, by the way."
    r "I don’t think seeing me hysterically crying on your bed would have left a good impression on anyone."
    s "Yeah, I have enough to deal with as-is. The last thing I need is someone thinking I’m taking advantage of you behind closed doors."
    r "The last thing {i}I{/i} need is you taking advantage of me behind closed doors."

    scene postbeach16
    with dissolve

    r "But I guess even someone like {i}you{/i} wouldn’t stoop that low. You care about me, after all."

    if rinbetrayed == True:
        r "Sure, you might have done the {i}one{/i} thing I asked you not to do, but that doesn’t mean you don’t also think I’m...cool or whatever."
        s "You’re really not going to let me live that down, are you?"
        r "Why would I? It was really fucked up."
        r "Friends don’t do that to each other."

        if bonus == True:
            r "You really think I can look at you the same way after finding out the girl I spent years fawning over probably pleasures herself while thinking about you?"
            r "Not really an easy thing to forget."
            s "..."
        else:
            s "I know, and I feel very bad. I will die filled with regret. I will never hug again."

        "Part of me wants to apologize, but I know it won’t do any good."

        if bonus == True:
            "I never understood why people apologize for things like this."
            "An apology isn’t just a magic set of words that can make your misdeeds vanish. It draws attention to them."
            "So it’s best to just ignore things like them entirely."
        else:
            "I am a bad boy."
            "I can not be redeemed."

    else:
        s "Someone like me? What is that supposed to mean?"

        if bonus == True:
            r "Just that you're a boy. You think with your penis instead of your brain."
            s "If I truly thought with my penis, your anti-perversion crying barrier wouldn’t have any effect."
            r "Ew, you get turned on by crying girls? Pervert."
            s "I’m not a pervert. I’m a man."
            r "Same thing. That’s why I like girls more."
            r "They’re only perverted like, 50%% of the time instead of 100%%."
            s "I’ll keep that in mind every other meeting we have."
        else:
            r "Just that you're the huggy boy and that everything you do is in the best interest of advancing your secret hug agenda."
            s "My hug agenda is very public. I don't try to hide that at all."

    scene postbeach19
    with dissolve

    pt "Umm...Rin? I’m sorry to bother you during your break, but could you help me with this for a second?"
    r "Huh? Yeah, hold on a sec."

    scene postbeach20
    with dissolve

    r "Sorry Sensei, but I’ll be right back..."
    s "It’s fine, actually. I’m probably going to head out now anyway."
    s "I just wanted to stop by and make sure you were doing alright. "
    s "You scared a few of the girls with the way you left, so I needed to make sure you didn’t go and do something stupid."
    r "Well, I did do {i}something{/i} stupid, but not as stupid as what you’re insinuating."
    r "But we can talk more about that soon, okay?"
    r "Futaba and I were probably gonna hang out in our room sometime in the near future and just...talk about stuff if you want to join."
    r "I’m sure she wouldn’t mind. It’ll probably all be about me anyway."
    s "Are you scheduling your own intervention?"

    scene postbeach21
    with dissolve

    r "It sounded a lot more normal in my head before you put it that way..."
    r "Just come hang out with us. It’ll be fun. "
    r "Depressing too, I imagine. But also fun."
    s "Sounds like a blast..."

    scene black
    with dissolve

    "I...apparently make plans to have a depressing, yet fun conversation with Rin and Futaba in the near future."
    "I really hope this doesn’t turn out to be one of those ‘group therapy’ sort of things but, if it does, I guess it will be warranted. "
    "Rin’s taking this a lot better than I thought she would, so there’s a chance this could just be the calm before the storm or something like that."
    "I should visit her dorm room whenever I can..."

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe30 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe35:
    scene firstotoha1
    with dissolve
    play music "justbehappy.mp3" fadein 4.0

    "I wind up showing up to the cafe after taking an obnoxiously long detour."
    "The path I normally take here was completely blocked off for construction or something so, after an extra fifteen minutes of finding an alternate route, I’m finally here."

    scene firstotoha2
    with dissolve

    f "Oh, good morning."
    f "We were just wondering when you were going to show up."
    s "Oh, right. Rin’s post-heartbreak excursion is today."
    s "I may or may not have forgotten about that."

    scene firstotoha3
    with dissolve

    f "So you just happened to show up at the cafe at the exact time we were supposed to go out on accident?"
    s "Yeah, kind of. "
    s "I would have shown up fifteen minutes earlier but I think they’re building something nearby."

    scene firstotoha4
    with dissolve

    f "Is that what all of that traffic was about? I had no idea. "
    f "We came from the opposite direction, but some of the roads were backed up over there as well. "
    f "I wonder what they’re building?"
    s "Beats me."

    "I look around the cafe, expecting to see Rin behind the counter or something, but can’t seem to find her at all."

    s "So, where’s our leader?"

    scene firstotoha2
    with dissolve

    f "In the bathroom doing her makeup. "
    f "She’s feeling much better today."
    s "Really? What happened?"

    scene firstotoha3
    with dissolve

    f "If anyone should know what happened, it’s you."
    f "Rin told me you were the one who let Chika into the room the other night so the two of them could talk."

    scene firstotoha2
    with dissolve

    f "Well, apparently that talk went really well."
    f "And even though nothing has really changed since then, she’s definitely held her head up a little higher."
    r "Hm? Who you guys talkin’ about?"

    scene firstotoha5
    with dissolve

    "Rin rounds the corner and stops in front of me, playfully punching me in the arm and feigning obliviousness to the fact that we're talking about her."

    s "Welcome back to the world of the living."
    r "Thank ya! Glad to be here!"
    r "And thanks again for all of your help since the beach. "
    r "I already thanked Futaba like six million times, but I really don’t think I would have gotten over this so quickly if it weren’t for you two."
    f "There’s no need to thank us. We’re just happy you don’t look like a zombie anymore."

    scene firstotoha6
    with dissolve

    r "As am I, dearest Futaba. "
    r "I can finally venture forth and be among normal people once again. It feels great to be alive."

    scene firstotoha7
    with dissolve

    r "Do you know the plan, Sensei?"
    s "Nope. I honestly still don’t even know where we’re going."
    r "Ohohoh, then you’re in for a treat."
    r "We’re returning to our native land at the far reaches of the outer-barrier."
    s "The what?"
    f "She means the area where our old school is. "
    f "Some people call it the outer-barrier because of the wall that was erected to prevent people from leaving the city."
    s "Is there an...inner barrier?"
    r "Nope. Just the outer one. But that’s beside the point."
    r "All you need to know is that you’ll be seeing our old stomping-ground for the first time."
    r "I haven’t been there ever since we moved, so I might be a little lost. But Futaba is there pretty often so she’ll be able to show us around."
    s "Why do you still go over there, Futaba?"

    scene firstotoha8
    with dissolve

    f "Oh, a good friend of mine still goes to the [high_school] in that part of town."
    s "Wait...if there is a [high_school] over there, why did you two wind up coming here?"
    s "You didn't move for the sole purpose of coming to this[school], did you?"

    scene firstotoha9
    with dissolve

    f "Oh...Well, um...That’s-"
    r "N-Nevermind that! It’s old news and doesn’t matter at all. "

    scene firstotoha10
    with dissolve

    r "What {i}does{/i} matter is getting this show on the road!"
    r "The last stage of fixing a broken heart is buying a bunch of stuff to get yourself over the final hurdle."
    s "So is that what we’re doing? Shopping?"
    r "Shopping. Eating. Enjoying life. You name it."

    "I really didn’t expect to be spending the majority of my day tagging along with girls while they buy clothes, but..."
    "Hey, maybe they’ll be willing to sample outfits for me or something?"
    "There’s got to be a bright side to this, right?..."

    scene black
    with dissolve2

    "..."
    "Okay, so there was no brightside."
    "We went into roughly fifteen stores and I did not get to see them sample even one article of clothing for me."
    "What is it with girls?"
    "How are they able to do things like spending hours upon hours in department stores without buying anything?"
    "I’ll never understand it."

    scene firstotoha11
    with dissolve

    "After department store number 20 or 21 (I’ve honestly lost count), we begin to make our way to some dessert place that Rin and Futaba know about."

    r "Look at this trooper, still standin’ tall after chaperoning two [young]lasses into half of the clothing stores in the city."
    f "Sorry for not buying anything. I just haven’t really been able to find anything that looks good on me..."
    r "Yeah, same here. But hey, that just means more money for food, am I right?"
    s "Another bright side to the fact that you two haven’t bought anything is that it's actually a huge plus for me."
    r "Why? Cause you think you’d end up carrying it?"
    s "Because I {i}know{/i} I’d end up carrying it."
    r "Excuse me, good sir, but who did most of the heavy lifting when Molly was moving into her dorm?"
    s "Me."

    scene firstotoha12
    with dissolve

    r "Heck no you didn’t! I carried like, triple the amount of boxes you did!"
    s "Yeah, but they were all light. Who’s the one who carried her eight hundred gaming chairs upstairs?"

    scene firstotoha13
    with dissolve

    r "Bad homie! You’re supposed to only say nice things about me today. I’m wounded."
    s "Sorry, Rin. I’ll make sure to give you any leftover compliments after you drain my wallet at the dessert buffet."

    scene firstotoha14
    with dissolve

    f "Oh, you don’t have to worry about that. I’m treating Rin today."
    r "What, really? You don’t have to do that. Sensei can pay."

    "Why is it okay for {i}me{/i} to do it?..."

    scene firstotoha15
    with dissolve

    f "Mhm. My parents gave me an advance on my allowance, so I have some extra money to spare."
    r "They still give you an allowance even though you don’t work for it or anything?"
    f "Well, it’s not like there’s really anything I can do for them when they’re thousands of miles away..."
    r "True, true. But you don’t have to use that on me, you know. I’m perfectly fine with Sensei paying."
    s "Is paying for yourself a thing that has even crossed your mind today?"

    scene firstotoha16
    with dissolve

    r "Hm? Did you say something? I can’t really hear you over the sound of the guitar."

    scene firstotoha17
    with dissolve

    r "Wait, guitar? "
    r "What’s going on down there?"

    scene firstotoha18
    with dissolve

    "I turn around to see a girl around the same age as Rin and Futaba playing guitar in the center of a small park."
    "It’s hard to hear from all the way over here, but it looks like she’s singing as well."

    scene firstotoha17
    with dissolve

    r "..."

    "Rin stops dead in her tracks as she watches the girl play. "
    "It’s hard to tell what she’s thinking, but she becomes absorbed within a matter of seconds."

    scene firstotoha19
    with dissolve

    f "We have time to stop and watch for a little while, right?"
    f "I think it would make Rin really happy."
    s "Hey, this isn’t my day. It’s hers. If she wants to go watch guitar-girl for a little while, that’s fine by me."
    r "Woah..."
    r "She’s really good."
    r "Do you guys hear her?"
    s "It’s kind of hard to from up here."
    s "Did you want to get closer?"

    scene firstotoha20
    with dissolve

    r "Yes! Please! "
    r "Come with me!"

    scene black
    with dissolve

    "Rin nearly jumps down the entire flight of stairs and dashes over to the park. "
    "I worry that something like that might make a scene because it’s rather busy around here but, somehow or another, no one seems to notice..."

    scene firstotoha21
    with dissolve

    "We wind up stopping a decent distance away from the girl, who’s busy playing and singing to a small and mostly inattentive group of people."
    "But despite the lack of attention she’s getting from the crowd, she’s surprisingly good."
    "Her words are clear and emotional. And even though I don’t know much about music, her guitar playing seems pretty good as well."

    r "..."

    "Rin stands still, taking in every ounce of the performance. It's almost like she's getting lost in it. "
    "Futaba stands to her side, gently tapping her foot and nodding her head along with the music."

    gg "...{i}Untie the knot around your finger set me loose again{/i}-"
    gg "{i}I'm longing for a chance to breathe and-{/i}"

    scene firstotoha22
    with dissolve

    gg "{i}A chance to make amends-{/i}"

    scene firstotoha23
    with dissolve

    r "Oh my God, she looked at me."
    s "She’s still looking at you."
    r "What? Why?"
    s "Probably because you seemed interested."
    s "No one else was really paying attention."
    r "Is it safe to look back?"
    s "Why wouldn’t it be?"
    r "I don’t know, dude. It’s embarrassing. She’s pretty and talented and I...have a ponytail!"
    s "Is there something wrong with ponytails that I'm not aware of?"

    scene firstotoha24
    with dissolve

    r "I DON’T KNOW! LEAVE ME ALONE!"

    scene firstotoha25
    with dissolve

    "The girl with the guitar goes through the chorus one more time before finishing her song and staring at the ground."
    "She takes a few moments to catch her breath before beginning to pack her things up."
    "The music that had seamlessly blended in with car horns and sidewalk chatter fades into nothingness and, once again, we’re left without a clear goal in mind."

    scene firstotoha26
    with dissolve

    r "Sensei."
    r "I call upon you for help."

    "Well, one of us seems to have a goal, apparently."

    s "What’s up?"
    r "I want to talk to her."
    s "Are you in love again?"
    r "Of course not. But...she’s really cool and really pretty and...maybe we could play together or something."

    if bonus == True:
        r "Like, guitar I mean. Not sexually."
    else:
        r "Like, guitar I mean. We are not children and we will not be confined to the sandboxes of playgrounds."

    r "Unless she wanted to."

    scene firstotoha27
    with dissolve

    r "AHHH! Just help me!"

    "I wonder how vulnerable Rin is at a time like this?"
    "I suppose now is as good a time as any to find out..."

    s "Okay, okay. Just look at her and repeat after me. Got it?"

    scene firstotoha26
    with dissolve

    r "Got it."
    s "First, tell her...{i}I love your music! I came running the second I heard it!{/i}"
    r "Roger!"

    scene firstotoha28
    with dissolve

    r "Uh...ummm! I love your music! I came running the second I heard it!"
    gg "Wow, really?! Thank you so much!"
    gg "You have no idea how much it means for me to hear that!"
    s "Now tell her, {i}You’re very pretty. Like...supermodel-pretty.{/i}"
    r "A-Also! You’re very pretty! Like a supermodel!"

    scene firstotoha29
    with dissolve

    gg "Oh, come on...that's not true. You’re just trying to make me blush."
    s "Okay, ready for the final move?"
    r "Hit me, wingman."
    s "With every ounce of confidence in your body, shout...{i}I would give anything just to kiss you!{/i}"
    r "I-I would give anything just to kiss you!"

    scene firstotoha30
    with dissolve

    r "Wait, what?! What are you making me say?!"
    gg "Uhh..."
    gg "..."
    gg "Cool?..."
    f "Okay...Futaba to the rescue."

    scene black
    with dissolve

    "Futaba pushes both myself and Rin toward the girl, who carefully places her guitar back in her case and comes to stand next to us."

    scene firstotoha31
    with dissolve

    f "Hey! We just wanted to say we really liked your performance."
    r "And {i}I{/i} want to say that I am so, SO sorry for that...last thing I said."
    gg "You mean the part about kissing me?"

    scene firstotoha32
    with dissolve

    r "Yuuuuup...That’s the one..."
    gg "Don’t sweat it...I’ve heard much weirder stuff playing out here. Trust me."
    f "Do you perform here often?"

    scene firstotoha33
    with dissolve

    gg "Every weekend, pretty much. So if you ever get bored and want to come watch, feel free."
    gg "I don’t ask for money or anything. I’m just kind of doing this for fun."
    r "Do you...go to[school] around here?"
    gg "Mhm. I’m a first-year at the [high_school] a couple miles away."
    f "So you’re in the same grade as us then."
    f "Do you know Nodoka Nagasawa by any chance?"

    scene firstotoha34
    with dissolve

    gg "Ah! Nodoka! I {i}do{/i} know her!"
    gg "I’m always going to her for writing tips and stuff."
    gg "That girl’s like...a pillar of infinite wisdom."

    scene firstotoha35
    with dissolve

    f "Yeah...She definitely knows a little too much for her own good at times..."
    r "Umm...Is it cool if I ask you for your name?"

    scene firstotoha36
    with dissolve

    gg "Why? Need it for your next pickup line?"

    scene firstotoha37
    with dissolve

    r "Okay. Time to go back into depression-mode."
    r "It’s been a good day, everyone. Rin Rokuhara is signing off."

    scene firstotoha38
    with dissolve

    o "Otoha. Otoha Okakura."
    o "It’s nice to meet you, Rin. You don't have to sign off yet."

    scene firstotoha39
    with dissolve

    r "Y-Yeah! It’s really nice to meet you too!"
    r "I promise to be less weird in the future!"

    scene firstotoha40
    with dissolve

    o "Speaking of weird, who’s this guy?"
    o "Boyfriend for one of you two?"
    r "Oh, no. That’s just some guy. He’s been following us around for like two miles now."
    r "I thought about calling the police, but my phone died."
    s "She’s lying. I’m their teacher."

    scene firstotoha41
    with dissolve

    o "Their teacher?"
    o "Then what are you doing out with them on the weekend?"
    f "He’s not exactly a normal teacher..."
    s "I’m really not."

    scene firstotoha42
    with dissolve

    o "Well, uhh...Okay then."

    "Yeah, that’s pretty much the reaction I’d expect out of any [high_school] girl who {i}isn’t{/i} in my class."

    scene firstotoha43
    with dissolve

    o "Anywho, I need to be getting a move on. I’ve got some stuff I need to take care of before tonight."
    o "It was really nice meeting you all, though!"

    scene firstotoha44
    with dissolve

    o "Oh! And Nodoka’s friend- I didn’t get your name! Tell me who you are and I’ll tell her I ran into you."
    f "Oh, Futaba Fukuyama. You don’t need to tell her, though. I’m sure I’ll be seeing her again soon anyway."
    o "Nah, nah. Totally telling her first thing Monday morning. We have science together."

    scene firstotoha45
    with dissolve

    o "And you! Make sure you take good care of these girls."
    o "You’re a lot older, so people might get the wrong idea if they see you out and about with them after dark."
    s "They’re in good hands..."

    "Kind of."

    o "Well, I don’t really have any reason to distrust you right now. So I guess they are."

    scene firstotoha43
    with dissolve

    o "Anyway, I’ll see you later! Thanks for listening to me play!"
    o "I’m here every weekend if you ever want to come say hi!"

    scene firstotoha46
    with dissolve

    r "W-We will!"
    r "..."
    r "...See ya."
    f "..."
    s "..."

    scene black
    with dissolve2

    "Shortly after that, the three of us make our way over to the dessert buffet."
    "We spend almost three hours there as Rin apparently has seventeen stomachs when it comes to dessert."
    "And even though Futaba offers to foot the bill for both her and Rin, I ultimately wind up paying for everyone."
    "I figure it’s the least I can do to thank them for a surprisingly fun day in a part of town I’ve never seen before."
    "And hey, we even managed to meet someone new."
    "I wonder if Rin and Futaba will wind up going back to see her again sometime soon?"
    "I can’t imagine myself ever wanting to go {i}that{/i} far away just to spend time with a girl, so there’s no guarantee I’ll ever see Otoha again."
    "But even if I don’t, I’m glad that she was able to make Rin smile."
    "That was the happiest I’ve seen her in quite some time..."

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe35 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label cafe40:
    scene cafeotoha1
    with dissolve
    play music "cafe.mp3"

    "I walk into the cafe first thing in the morning to suddenly remember that I am not the only person of importance in Rin’s life."
    "What a shitty way to start the day."

    if cafe35 == True:
        "Seated with her at the table appears to be the same girl we ran into at the park during her post-rejection blues."
    else:
        "Seated with her at the table is a girl around the same age as her, likely the one who she couldn’t stop talking about during the Christmas party."

    "The real question is whether or not I should leave the two of them alone or try to insert myself into the conversation."
    "I think back to what seems like aeons ago when I ran into a similar situation, but with Chika at the table next to Rin instead of this new girl."
    "Back then, Rin was barely able to hold a conversation on account of how nervous she was."
    "So...if something like that is happening again today, surely she’d want me to step in."
    "Right?"

    s "..."

    "Well-"
    "Only one way to find out, I guess."
    "Time to, once again, involve myself in the daily lives of [high_school] girls and see where I’m able to fit in."

    if cafe35 == False:
        scene cafeotoha2
        with fade

        r "Oh, Sensei! Good morning."
        r "If you need anything, Haruka’s manning the counter right now."
        q "Sensei? "
        q "You’re Rin’s teacher?"
        q "You look younger than she made you sound."
        s "...How did she make me sound, exactly?"

        scene cafeotoha3
        with dissolve

        r "I have no idea what Otoha’s talking about. "

        if bonus == True:
            r "I totally didn’t say anything about the gigantic age gap between us and about how you’re way too comfortable around [teenage]girls."
            o "Yeah, you walked right up to us. Show some restraint, dude."
            r "Yeah, Sensei. Show some restraint."
        else:
            r "I totally didn't tell her you were a wizard or anything."
            s "That was confidential! I trusted you!"

        "Why am I being ganged up on before I’ve even had the chance to do anything?"

    else:
        scene cafeotoha4
        with fade

        r "Oh, Sensei! Good morning!"
        o "Hey, it’s that guy from the park who hangs out with [teenager]s."
        s "I liked Rin’s greeting more."
        s "Good morning, you two."
        r "If you need anything, Haruka is manning the counter right now."
        r "If not, you’re free to chill with us, though."
        r "Or both. You’re not limited to just one of those two things."
        o "I’d probably prefer it if you’d buy something. Otherwise it seems like you just came here to hang out with Rin."

        scene cafeotoha5
        with dissolve

        r "Oh, he probably did. He does that a lot."
        s "Stop saying things that give her a bad first impression of me."

        scene cafeotoha6
        with dissolve

        r "{i}Second{/i} impression, Sensei. The first impression was when you were hanging out with Futaba and me in the park."
        r "Besides, we’re pals. I love that you come here to hang out."
        o "I still think it’s weird. But it is what it is, I guess. You do you, man."

    s "...That aside, isn’t it too early for you to just be hanging out at a table instead of working?"

    scene cafeotoha7
    with dissolve

    r "Normally, yeah. But I’m taking my break a little early since this is the only time Otoha is able to show up today."

    scene cafeotoha8
    with dissolve

    o "Wait, you’re doing this for {i}me{/i}? Dude, how much longer is your shift after this?"
    r "Like another seven hours or something. But it’s cool. I don’t need a break."
    r "I can drink coffee whenever I want, so I’ll just run on that until I collapse or something."

    scene cafeotoha9
    with dissolve

    o "Well shit, man. Now I feel really bad."
    r "I told you, it’s fine. I really don’t mind."
    s "What kind of life do you lead where nine in the morning is the only time you have to stop at a cafe?"

    scene cafeotoha10
    with dissolve

    o "I live pretty much as far away from this side of town as possible, so it’s kind of a journey every time I need to come down."
    r "Otoha takes vocal lessons in some sketchy girl’s basement not far from here."
    o "She’s not sketchy...she’s a professional musician."
    r "She just has a really sketchy basement. I saw pictures."
    o "Yeah, that much is definitely true."
    o "She’s been a big help, though. I can’t imagine where I’d be without her."

    if cafe35 == True:
        s "Right, you’re a musician."
        s "Still playing in that park we found you at?"
    else:
        s "You’re a musician?"
        o "Yup! Just like Rin here."
        r "Otoha is a million times better than me and I could never hope to achieve even an ounce of her talent or beauty."
        r "Also, I didn’t just mention her beauty. Forget that happened."
        r "Really, though. She’s so pretty."
        s "Please excuse Rin. She talks a little too much when she gets nervous."
        o "Yeah, that’s one of the first things I realized about her. I just ignore it at this point."
        r "Otoha used to play mini concerts every weekend at some park in the area Futaba and I used to live in."
        r "That’s how I met her."
        s "Used to?"

    scene cafeotoha11
    with dissolve

    o "Had to stop since I’ve been really busy lately."

    if bonus == True:
        o "After my[school] sunk into the ground out of nowhere, I started being homeschooled instead."
        o "And, weirdly enough, it’s actually a little harder being homeschooled than it is going to actual[school]."
    else:
        o "After my[school] sunk into the ground out of nowhere, I started spending all of my free time knitting socks for my cats, but all of the cats hate them."
        o "It's really stressful, to be honest. Sometimes I think about just ending everything right then and there."
        o "But then I see their sockless little paws and I'm like naaaaaaah."

    s "Yeah, I honestly can’t imagine anything easier than being in my class."
    r "Sensei hasn’t given us a single assignment in months. It’s awesome."
    o "I’m lucky if I can go a day without some ridiculous assignment."
    o "My parents are super strict about my education now that I’m not in[school] anymore."

    scene cafeotoha12
    with dissolve

    r "I’ve been trying to convince her to transfer into our[school] but she feels weird about moving into the dorms without having a roommate."
    s "Can’t she just stay in your room?"
    r "I mean...I think there’s a rule about having no more than two girls in one room-"

    scene cafeotoha13
    with dissolve

    r "Unless...we slept in the same bed and no one ever found out about it..."
    o "..."
    r "..."
    o "You good?"

    scene cafeotoha14
    with dissolve

    r "Huh?"
    r "Where am I right now?"
    s "So, you’re only in this part of town so you can go hang out and sing in some sketchy girl’s basement?"
    o "Some girl’s sketchy basement. Slightly different, but you get the gist."
    o "Rin and I have been talking a lot ever since bumping into each other in the park, but I don’t really have a lot of time to ever hang out or anything like that."
    o "So the only chances we have to meet up involve me getting up mad early and sacrificing sleep in the name of friendship."

    scene cafeotoha15
    with dissolve

    r "She’s awesome, right?! Coming all the way over here just to see me!"
    o "It’s not that big of a deal..."
    o "But yeah, I guess I can be kind of awesome at times."
    s "I come here to see you all the time."
    r "Yeah, but I see you so much that I’m starting to become immune."
    s "Can you...become immune to people?"
    r "Of course!"

    scene cafeotoha16
    with dissolve

    o "You two really spend {i}that{/i} much time together, huh?"

    if bonus == True:
        r "Yeah, but he’s only seen my boobs like once or twice so we’re probably not as close as you think we are."
        s "Why would you even say that?"
        r "Say what? What did I say?"
        r "I literally can’t remember. Am I having a stroke?"
    else:
        r "Yeah, but only because we were coworkers in our past lives. We worked at a cannery in Alaska, so we had plenty of time to get to know one another."

    o "I’m just going to pretend I didn’t hear that, so don’t even worry about it."

    "Good. I guess this Otoha girl is just as cool as she looks."
    "Which is pretty damn cool, not gonna lie."
    "Do you see how many rings she’s wearing?"

    scene cafeotoha17
    with dissolve

    r "Hey, umm...you wouldn’t happen to have any free time tonight or something would you?"
    r "It’s like...the weekend and stuff, so I can’t imagine your parents are making you study all day today."
    o "I might have some free time later on but like, I don’t really have the money to afford another bus trip."
    o "Maybe we could meet halfway? Like, walk around the mall for a little while or something?"
    r "Uhhhhhhhhhh...or literally anywhere else. Malls are weird anyway. Like, who likes malls?"
    o "What? I like malls. Plenty of people like malls."
    r "Yeah but like...there are so many...fluorescent lights and...shoe stores..."
    s "Chika doesn’t normally work nights if that’s what you’re worried about."

    scene cafeotoha18
    with dissolve

    r "Dad! Are you {i}trying{/i} to embarrass me?!"
    s "...Did you just call me Dad?"
    o "I definitely heard her call you Dad."
    r "Yes! Because you’re doing a really “Dad” thing right now!"
    o "So uhh...who's this Chika person anyway?"

    scene cafeotoha20
    with dissolve

    r "Her."
    s "How did you pull up a picture of her that quickly?"
    s "Also, where did your phone even come from?"
    r "Don’t ask questions you don’t want to hear the answers to, Sensei."
    s "But...I {i}do{/i} want to hear the answers."
    o "She’s hot."
    r "Painfully so."

    scene cafeotoha21
    with dissolve

    o "Why’s one person keeping you away from the mall, though? I don’t get it."
    r "Well...she’s not {i}keeping{/i} me away..."
    r "I’m...distancing myself for...personal reasons."

    scene cafeotoha22
    with dissolve

    o "Care to elaborate since you seem to actually understand Rin?"

    if rinbetrayed == True:
        r "I’m sure he’d be {i}thrilled{/i} to tell you all about it considering he played such a big role in everything that went down."
        s "I...should probably stay out of this, to be honest."
        o "But...you’re literally the one who brought it up."
    else:
        r "Leave my dad out of this."
        s "As much as I’d love to explain things to you, it would probably be best if Rin told you herself."
        o "Yeah...it doesn’t look like that’s going to happen."
        r "Not yet. I need time to prepare."
        r "And to...delete pictures."

    scene cafeotoha23
    with dissolve

    r "But...um, since I don’t want to go to the mall, maybe I could just come over to...your place or something?"
    r "I have some extra money for the bus and I {i}kind of{/i} know my way around that part of town anyway, so...I could just stop by tonight?"
    o "That’s sweet, but you don’t have to do that. It’s a crazy long trip to make that late at night."
    o "My house is kind of boring anyway, so I can’t imagine it would be any fun."
    o "How about you just text me tonight and we try to make plans sometime in the future?"
    o "Does that work?"

    scene cafeotoha24
    with dissolve

    r "Y-Yeah! Totally."
    r "I’ll text you all day and make like, all of the plans ever."
    o "Um...I mean, if you want to text me all day that’s fine. But I don’t think I’ll be able to respond right away a lot of the time."
    r "I will do my best to not think you hate me if you take too long to reply."
    o "Hey, if that’s what makes you happy..."
    o "I’ve gotta get a move on, though. There’s a sketchy basement with my name on it and drinking caffeine before singing really isn’t a great idea anyway."
    r "Yeah, totally! That’s a thing I definitely knew!"
    r "Um...have fun in the basement!"
    o "..."
    o "Yeah. I will...do just that."
    o "Bye, Rin."

    scene cafeotoha25
    with dissolve

    o "And see you, Sensei."
    o "Thanks for only moderately creeping up the place this morning."
    s "That’s what I’m here for."
    o "Wild."

    scene cafeotoha26
    with dissolve

    "Otoha grabs her cup of coffee off the table and chugs the entire thing down despite how bad caffeine apparently is before singing."
    "Which is also a thing I definitely knew."
    "And Rin is now beaming with so much excitement and energy that she doesn’t even feel the need to bring up Chika."

    r "Why the ever-living fuck did you bring up Chika?"

    "Oh. Nevermind, I guess."

    s "Your expression really does not match your tone right now."

    scene cafeotoha27
    with dissolve

    r "No, like really, though! Why did you do that?!"
    r "You totally knew why I didn’t want to go to the mall and you brought it up anyway."
    r "And don’t say it’s because you’re my dad and you were trying to embarrass me!"
    s "Yeah, that is definitely not a thing I was going to say. Stop calling me your dad."
    r "Fine! Then why were you being such a bad homie?"
    r "I’m just now starting to get over Chika and every time I hear her name it adds like one more week to the time it will take for that to happen."
    r "And now I’ve just added another week. Thanks a lot, Sensei."
    s "I don’t know. I guess seeing you with Otoha made me feel like you were a little closer to being over her."
    r "Dude, Otoha doesn’t even know I’m bi yet."
    s "I am...pretty sure she does."
    r "But I do such an awesome job hiding it!"
    s "..."
    r "What?! Why are you being so quiet all of a sudden?!"
    s "You literally told her that you wanted her to sleep in your bed and that she was beautiful like five minutes ago."

    scene cafeotoha28
    with dissolve

    r "That actually happened?!"
    r "I thought that was just in my head!"
    s "It absolutely was not."

    scene cafeotoha29
    with dissolve

    r "I’m such a creep. Why do you even like me?"
    s "Probably because I’m a creep, too."
    r "You really are. You’re a total weirdo."

    if bonus == True:
        r "Remind me to never flash you again."
        s "Absolutely not. I embrace all future flashing."
        r "Dude, weird. You just told me you want me to flash you."
        s "Yes. I am not hiding that."
        r "Gross. Super gross. You’re the worst."
        r "Get out of here, Dad. And stop going through my underwear drawer while I’m at[school]."
    else:
        s "No, stop. It's fine when I say it, but it hurts my feelings when you do it."
        r "Jeez. Grow up already, weirdo."

    scene black
    with dissolve2

    if bonus == True:
        "It isn’t long before Rin’s break comes to an end and I need to head back out into the street to find some other way to spend my time."
        "Even though she gave me shit about it, I think it’s safe to assume that Rin isn’t actually mad at me."
        "But a lot of that is probably due to the fact that it didn’t backfire."
        "Her friend seems really chill. The two of them would make a good couple."
        "So much so that I’m only mildly concerned about her becoming yet another barrier between Rin and me in the future."
    else:
        s "I don't like you anymore. Goodbye, Rin."
        r "Bye, Sensei! See ya later!"

    $ renpy.end_replay()
    $ cafe40 = True
    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Your daughter, Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe45:
    scene rindate1
    with dissolve
    play music "cafe.mp3"

    "I arrive at the cafe bright and early to find someone who is definitely not Rin hanging out behind the counter."
    "I check my phone to make sure that I didn’t somehow oversleep and wander in at night instead, but I quickly realize that even {i}that{/i} wouldn’t explain the sunlight."
    "So, why is Molly here?"
    "And why are her eyes closed?"
    "What is the meaning of this?"

    s "Molly."
    h "Shh...She’s sleeping."
    s "Yes, Haruka. I have eyes. I can see that."
    h "Well, it didn’t stop you from talking to her, soooo..."
    s "Because she’s supposed to be {i}working{/i}. As the owner, you should know this."
    h "All I know is that I’d be asleep too if I had to go from night shift to morning shift so suddenly."

    "I start snapping my fingers, hoping that Molly will react in some sort of way."

    mo "..."

    "As you can see, she doesn’t."
    "So perhaps it’s time for me to try something different?"

    s "..."
    mo "..."
    s "Anime is stupid."

    scene rindate2
    with hpunch

    mo "Hah?! Wha?"
    mo "Where am I? What’s going on?!"

    scene rindate3
    with dissolve

    mo "Wait...this world looks almost exactly like the cafe..."
    mo "But it’s so bright...so it can’t be the {i}real{/i} cafe."
    mo "There’s even a Haruka clone sitting at the counter."
    h "Not a clone. Morning, Molly."
    mo "And she speaks our language as well..."
    mo "This can't be...Earth...can it?"
    s "{i}Ahem.{/i}"

    scene rindate4
    with dissolve

    mo "Ah! Now there's a Sensei clone!"

    if bonus == True:
        mo "Three more and I can finally make my greatest fantasy come true!"
    else:
        mo "I thought I was the only one who possessed one of those!"

    s "...Excuse me?"
    mo "Don’t worry about it!"
    s "No, now I’m genuinely curious."
    h "Same. Do tell, Molly."

    scene rindate5
    with dissolve

    mo "So, ummm..."
    mo "I take it I was just sleeping on the job and I...haven’t been teleported into a nearly identical isekai?"
    s "Correct. But why are you working so early? You’re a night person."

    scene rindate6
    with dissolve

    mo "Ask Nithhala. She’s the one who went and scheduled her stupid date for today."
    mo "Now I’ve gotta be the one to help all the morning people."
    mo "Do you have any idea how low my mana is right now? "
    s "Not a clue. "

    "Huh. I knew Rin had a “date” with Otoha coming up, but I didn’t realize it was today."
    "I wonder if she’s still planning on taking her to that arcade thing?"

    s "I’m sorry you have to cover her shift, Molly. But just think of all the extra money you’ll have to spend on..."
    mo "..."
    s "..."
    mo "Spend on what? I want to hear your guess."
    s "Dragon...stuff?"

    scene rindate7
    with dissolve

    mo "Hohohoho...an excellent guess, Sir. But you’ll have to be a bit more specific about what type of dragon if you’re really going to excite me."
    s "Your eyes are on fire, though."
    mo "And so is my heart..."
    h "Umm, sorry to bother you two while you’re...bonding or whatever, but look who just came in."
    s "Hm?"

    scene rindate8
    with fade

    "I turn around to find Rin standing there, decked out in her winter garb and looking up at me with a smile on her face."

    s "Oh, hey."
    s "Aren’t you supposed to be meeting Otoha this morning?"
    s "Molly just told me that was supposed to be today."
    r "I got ditched."
    s "Oh..."
    mo "Rin..."

    scene rindate9
    with dissolve

    r "Yeah, yeah. I know how it sounds. That’s really not what happened, though."

    if bonus == True:
        r "Otoha’s parents are just really strict and they don’t want her going out today since she’s been struggling with her homeschool stuff."
    else:
        r "Otoha’s parents are just really large and she couldn't get around them in time."

    mo "I depleted my mana for nothing?! "
    mo "Rin, open me a portal to Dalaran! Drop a mage table! Do something!"

    scene rindate10
    with dissolve

    r "Do you hear something, Sensei? I thought I heard Molly but I’m pretty sure she only works nights."
    s "I haven’t heard anything all morning."
    mo "I’ll...I’ll use thaumaturgy to make my voice three times louder!"
    mo "RIN! PORTAL!"
    r "There it is again. So weird."

    scene rindate11
    with dissolve

    r "Umm...a-anyway!"
    r "Are you...busy today?"
    r "I already took the day off and Futaba is at the library so I’ve kinda got...nothing going on for the next 24 hours."
    s "And you’re absolutely sure Otoha isn’t able to go? I know how much you were looking forward to it."
    r "Yeah...maybe some other time. Definitely not happening today, though."
    r "She had her phone taken away. Pretty sure her mom texted me back or something since her texts started getting abbreviated all weird out of nowhere."
    s "Then sure. I don’t mind at all."
    s "It was a little shocking seeing Molly so early anyway. I don't have the energy to deal with her yet."

    scene rindate12
    with dissolve

    r "Molly?..."
    r "Sensei...Molly died five years ago..."
    mo "Wha-?!"
    mo "I’m...a poltergeist?!"
    mo "This explains so many things!"
    s "I still think about her every day..."

    scene rindate13
    with dissolve

    r "As do I...One never forgets their first kiss, after all."
    h "Uhh, excuse me? You two kissed and I didn’t hear about it?"
    r "Quiet, Haruka. This conversation is not meant for adults."
    h "But...Sensei is..."
    r "Shhhh...everything will be okay."
    h "...What?"

    scene rindate14
    with dissolve

    r "So! Ready to come to a bunch of places you probably won’t enjoy and prevent me from getting all sad and feeling sorry for myself?"
    s "There’s nowhere else I’d rather be."
    r "That’s a lie, but thank you for saying it."
    r "I’d hold your hand but I don’t want you to get arrested and make today even worse."
    s "That works for me."

    scene black
    with dissolve2
    stop music fadeout 10.0

    h "Uhh...have fun?"
    mo "Haruka...can..."
    mo "Can you see me?..."
    h "..."
    mo "..."
    h "Weird...I could have sworn I heard something just now..."
    mo "HARUKA!!!!!!"

    scene rindate15
    with dissolve
    play music "justbehappy.mp3"

    "Rin and I get off the bus probably twenty or thirty minutes later and step into yet another area of the city that I’m completely unfamiliar with."
    "She checks a navigation app on her phone for a few seconds before grabbing my wrist and pulling me along."
    "We walk several blocks and it quickly becomes apparent that I may have needed an even {i}thicker{/i} T-shirt to survive this weather."
    "The buildings are lined up in a way that turns the streets into a wind tunnel. "
    "And considering how cold it is today, there are barely any people ahead of us to serve as additional breaks for said wind."
    "We take everything in full force."
    "But luckily for Rin, she’s so wrapped up in her thoughts that she remains completely unfazed."

    r "Like, for real, though. Why’d her parents have to pick {i}today{/i} to get all stupid?"
    r "Any other day would have been cool, but nooooo. Let’s wait for a cute bisexual girl to come along and want to hold hands with our daughter before RUINING EVERYTHING."
    r "I should kill them. "
    r "Sensei, let’s go kill people."
    s "Rin, I know you want to impress Otoha, but I can’t help but feel like there are better ways of doing that than killing her parents."

    scene rindate16
    with dissolve

    r "Okay, fine. You wait outside and I’ll take care of the tough part."
    r "If Otoha tries to run away, though, you’ve gotta grab her so I can have a chance to explain myself."
    s "You’re not actually insane, are you?"
    r "Is it insane to kill the people between you and your goal?"
    s "Yes."
    r "Oh."

    scene rindate17
    with dissolve

    r "Well, maybe I am then."
    r "I don’t know. I’m just so friggin’ pissed off, you know?"
    r "I could barely even sleep because of how excited I was for this and now I’ve gotta hang out with {i}you{/i} instead."
    s "..."

    scene rindate18
    with dissolve

    r "Dude, I’m kidding!"
    r "That was obviously a joke. You know you’re my favorite."

    if rinbetrayed == True:
        if bonus == True:
            r "Like, what other person do you think could hook up with the one girl I wanted more than anyone else in the world and {i}still{/i} be able to spend time with me? "
            r "We’re stuck together, whether we like it or not."
            r "Just like how I’m stuck with the memories of you burying your fingers inside of Chika while I was burying mine inside of myself."
        else:
            r "Like, what other person do you think could hug the one girl I wanted more than anyone else in the world and {i}still{/i} be able to spend time with me?"
            r "I bet you aren't even that good at hugging."
            s "Ah!"

        scene rindate19
        with dissolve

        r "Whoops! Said too much. "

        if bonus == True:
            r "Don’t want you taking advantage of {i}me{/i} next!"
            s "You’re really going to remind me of that every time we hang out, aren’t you?"
            r "Or until one of us dies. Either one works."
        else:
            s "You bet your bottom dollar you did!"

    else:
        if bonus == True:
            r "Like, as far as people with penises go, you’re the number one prospect in my book."
            s "I know that compliment isn’t really anything I should write home about, but that does make me feel good."
            s "Where do I stack up against the people without penises?"

            scene rindate19
            with dissolve

            r "Hmm..."
            r "Close to the top still, I guess."
            r "Like obviously below Chika and Otoha...But like, somewhere above Molly and Ami."
            s "Why is Ami on the list? "
            r "Ami’s cute and has good taste in manga."
            r "Plus she’s girly and I like girly girls."

            scene rindate20
            with dissolve

            r "I’d totally bang your [niece], dude."
            s "I can’t tell if I’m confused or aroused right now."
            r "Why not both?"
        else:
            s "Platonically though, right?"
            r "Of course, homie. We'll be buds forever."

    scene black
    with dissolve2

    "We walk several more blocks before finally arriving at the arcade Rin planned on taking Otoha to."
    "Just like she said, the place has a distinct “cool” aura to it. So much so that I feel a little out of place even coming here."
    "But, I guess this arcade wasn’t exactly picked out with me in mind."
    "This was supposed to be a date for her and another, equally cute girl."
    "I’m just a backup right now."
    "So I guess it falls on me to...soak up Rin’s handpicked, special date stuff and make her happy."

    scene rindate21
    with dissolve

    r "Here we are! Couch Potato! "
    s "What did you just call me?"
    r "Huh? Couch Potato is the name of the arcade."

    if bonus == True:
        r "To my right, you will see a wonderful selection of alcoholic beverages that I am not yet legally allowed to consume."
        r "If you want to get hammered, though, go right ahead! I understand the risks that come with dating an adult!"
        s "I think I can go the afternoon without drinking, but thank you."
        r "You sure? I’m kind of interested in what drunken Sensei would be like."
        s "I can’t imagine it would be anything you enjoy."
    else:
        r "To my right, you will see a wonderful selection of alcoholic beverages that I am legally allowed to consume because I am an adult woman."
        s "Does this mean you're going to have some?"

    r "Probably not but REGARDLESS-"

    scene rindate22
    with dissolve

    r "We are here to have a good time and forget all about our debatably bisexual musician friends."
    s "I only have one musician friend and she is already a confirmed bisexual."
    r "Maya is also a musician, Sensei. And she’s still up in the air."
    r "So while I’m thinking about {i}my{/i} debatably bisexual musician friend, you can just think about Maya."
    s "Thinking about Maya is exhausting. I’ll just think about Otoha as well."
    r "Fine. But please keep her clothes on in your imagination."
    s "Will you be abiding by that same rule?"
    r "Absolutely not."

    scene rindate23
    with dissolve

    r "But anyway, all the games and stuff should be somewhere behind me in the back corner."
    r "I’m not really sure what you’re into, so just come with me and play some of the stuff I do."
    r "Oh, and don’t cry too hard when I {i}friggin’ annihilate you.{/i}"
    s "You’re very good at being intimidating and adorable at the same time, Rin."
    r "And you’re very good at...stuff!"
    s "..."

    if bonus == True:
        r "Sorry. I planned out a bunch of compliments for my original date, but she’s doing homework right now."
    else:
        r "Sorry. I planned out a bunch of compliments for my original date, but her parents were just so large."

    r "I’ll get back to you with some nice stuff later once I can think of some."

    scene rindate24
    with dissolve

    r "But for now, let’s play some games and forget about our feelings!"

    scene black
    with dissolve2

    "Rin leads me to the back of the arcade rather confidently despite never having been here before."
    "I guess she really did her research online first."
    "The only issue is that now I have to try to not look like a complete imbecile playing whichever game Rin decides she wants to play first."
    "As long as it’s not one of those...dancing machines I’ve seen other [teenager]s play, though, I should be fine."
    "........."
    "......"
    "..."

    scene rindate25
    with dissolve

    "Nevermind. There is apparently more than one type of machine that can make me feel like a child."
    "I do not like this."

    r "You look like a moron right now."
    s "I want to insult you as well but you look pretty fucking cool."
    r "It’s the hoodie, not me."
    s "It definitely helps."

    scene rindate26
    with dissolve

    r "So, it’s probably safe to assume you’ve never played anything like this before, right?"
    s "Very safe. I have absolutely no idea what I’m doing."
    r "Just make sure you have your feet on the little foot-holder thingies and put both hands on the grips up here."
    r "You’ll notice a button on one of them. Press that to accelerate and move the bars around to steer."
    r "Each race has three laps and it’ll be you, me, and a bunch of AI opponents."
    r "Don’t underestimate them, though. This game might be a little retro, but the AI will fuck your day up."
    s "I am fully prepared for my day to be fucked up. Congratulations on defeating me in advance."
    r "Hey, man. There’s no fun if you give up beforehand. You’ve gotta at least try."
    r "Just think of how easy it would be to tease me if you defeated me at a game I literally taught you how to play."
    s "One can only hope."

    scene rindate27
    with dissolve

    r "Ready to do this, then?"
    s "As ready as I’ll ever be..."
    r "Good! Then-"

    scene rindate28
    with dissolve

    r "Prepare to get railed~"
    s "..."
    s "I understand that the game’s tagline is “Rail on” but don’t you think what you just said is a little...racy?"
    r "I’m gonna rail you so hard."
    s "Uh-huh."
    r "So hard you won’t even be able to walk afterward."
    r "And then when I’m done, I’m gonna call Ami over and rail your [niece]. "
    s "Rin, please."
    r "I’m gonna rail {i}everybody{/i}. All day. All night."
    r "You’ll be begging me to rail you again once we leave today. Calling it now."
    s "If your plan is to distract me through phrases that can be easily misinterpreted, it’s really not necessary. "
    s "You’re going to win no matter what."

    if bonus == True:
        r "What can I say? I’ve been railing ever since I was a little girl."
        r "I know my way around the block, man."

    scene rindate29
    with dissolve

    r "NOW, PREPARE TO DIE, LOSER!"

    scene rindate30
    with fade

    "Rin’s shout was a bit pre-emptive as we still needed to select a track and I guess...different types of motorcycles or something?"
    "I don’t know. I chose the first one I saw and, as expected, was demolished so quickly that I couldn’t even blame the bike."
    "The same pattern repeated for the next few hours."
    "Rin would take me to a machine, explain how the machine works, and then make me look like an absolute idiot in front of the...three other people that were there."
    "I’m pretty sure they may have even started laughing at me after a while."
    "And while something like this would normally bother me, today it was fine."
    "Because not only was the purpose of this trip to help cheer Rin up after the new object of her affection bailed on her-"
    "But it was the first few hours in quite some time that I’ve felt like she was actually focused on me."
    "Backup date or not, it was fun getting to see this side of her. "
    "Otoha really did miss out on something great this afternoon."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Eventually, we run out of machines to try out and head over to a pizzeria on the corner of the street."
    "We take our time sharing a pizza and wind up begrudgingly leaving one slice that we were unable to finish behind."
    "Instead of the night ending there, though, Rin urges me to come back to the dorm since she still has more time to kill and Futaba is with Nodoka tonight."
    "Having nothing else to do, I obviously agree and allow the backup date to move into its second phase."

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe45 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump rindorm45

label cafe50:
    scene cafefifty1
    with fade
    play music "cafe.mp3"

    "I make my way into the cafe to find things a little busier than normal this morning."
    "It’s particularly windy today, so I figure that might have something to do with it."
    "Does wind make cafes busier? That sounds like a thing."
    "Either way, I am prepared to order myself a hot beverage and immediately vacate the premises because there is clearly no reason for me to ever stay here."

    s "..."

    "That’s right. I said there is no reason for me to ever stay here."

    s "..."
    s "{i}Ahem.{/i}"

    scene cafefifty2
    with dissolve

    r "Yo! Sorry for the wait. Been a little wild this morning, if you know what I mean."
    s "What else could that possibly mean apart from the cafe being busy?"
    r "Beats me. Maybe I killed someone on the way to work? You know...found a machete and just went to town on an innocent bystander."

    if day == 6:
        r "Saturdays, am I right?"
    else:
        r "Sundays, am I right?"

    s "Sure, Rin. "
    r "So, I’m gonna assume you’re here to congratulate me on the fact that I have a girlfriend now, right?"
    s "I’m actually here to order a drink."

    scene cafefifty3
    with dissolve

    r "What? Why? "
    s "Because that is literally the purpose of this building. "
    r "No. The purpose of this building is giving you and me some time to chill outside of[school] while {i}also{/i} allowing me to get paid."
    s "Right. So what does that mean for the days that I {i}don’t{/i} come here?"

    scene cafefifty4
    with dissolve

    r "On those days, I normally just sit around frowning...hoping you’ll show up to keep me company."

    scene cafefifty5
    with hpunch

    r "Or at least that’s what I {i}would{/i} be doing if I didn’t have a girlfriend now!"
    r "So, did you hear that I have a girlfriend now? Because I totally have a girlfriend now. "
    r "Like, a real one. Not just a picture of a girl I like that I carry around in my wallet and whisper sweet nothings to when no one is looking."
    s "Is that...a thing you actually do? Or {i}have{/i} done?"

    scene cafefifty6
    with dissolve

    r "What? No. Weren’t you listening? "
    r "Besides, who prints out pictures anymore? Just set a picture of the girl you secretly like as your lock screen and move on like everybody else."
    r "Which reminds me, I have a girlfriend now."
    s "Wow, really? I had no idea."

    scene cafefifty7
    with dissolve

    h "Rin, as happy as I am for you, I {i}kind of{/i} need you...actually working today."
    r "I kind of need you to congratulate me on the fact that I have a girlfriend now."

    scene cafefifty8
    with dissolve

    h "I’ve congratulated you like ten times today alone. I can’t keep doing this for the rest of forever. It’s wasting too many words."
    r "Okay, okay. Fine. You’re off the hook for the rest of the day."
    r "But if my {i}girlfriend{/i} finds out that you don’t care about her, you can bet those huge mommy milkers of yours that she’ll have something to say about it."
    r "Just kidding. Otoha is really nice. "
    r "Otoha is my girlfriend, by the way. We’re dating now."

    scene cafefifty9
    with dissolve

    h "You didn’t bring a leash, did you?"

    if bonus == True:
        s "I wish."
        r "Careful, Sensei. The only girl who can put me on a leash is Otoha. My girlfriend."
        s "We’ll see about that, Rin."
    else:
        r "Why would he do that? There are no animals here."
        s "We will see about that."

    scene cafefifty10
    with dissolve

    r "Wait, we will? Why do you sound so sure? "
    s "Just a hunch."
    r "Ominous. "
    r "Make sure you check with my girlfriend first. Her name is Otoha, by the way. She’s the one who is dating me. Have you heard of her?"
    s "Never."
    s "But anyway, how are you doing, Haruka? You seem easier to talk to in your current mental state."

    scene cafefifty11
    with dissolve

    r "Hey! I’ll have you know that {i}my{/i} current mental state is better than ever! I’m totally happy and totally cool!"
    h "Oh, uhh...I’m doing well. "
    h "Just trying to keep things afloat in here, which is admittedly a little tough when my best employee is now somehow {i}worse{/i} at her job after getting a...girlfriend, I think it was?"
    s "If this is your best, you might want to look into hiring a few more girls."
    r "Oh, okay. Yeah. Now that Rin has a girlfriend, it’s fine to just make fun of her all day. I see how it is."
    r "You two wait until my girlfriend hears about this. She’ll show you what’s up."
    r "Her name is-"

    scene cafefifty12
    with dissolve

    h "Okay, seriously? Stop. "
    r "Ugh. Fine. I’ll keep doing my job. "
    r "If I’m ever going to inherit the family business, I can’t be slacking off like this."
    h "Thank-"

    scene cafefifty13
    with dissolve

    h "Wait, are we related now? How is this a “family” business?"
    r "You’re kinda like a mom to me, aren’t you? You’ve definitely got the boobs of one."
    h "Can we stop talking about my boobs? Also, there are plenty of mothers out there who-"
    r "You’re also just as related to me as my actual mom. So yeah, basically a family member. "
    r "If I’m not in your will, I’m gonna be really pissed."
    h "Okay. You know what? There’s a customer in the corner who just ordered a vanilla latte. "
    h "If you can get it to them in less than two minutes, I’ll add you to my will. If not, I’m leaving the cafe to Sensei."

    scene cafefifty14
    with dissolve

    r "Over my dead body..."
    s "Take your time, Rin. Inheriting a business for literally nothing sounds like a pretty sweet deal."
    r "The only thing {i}you’re{/i} going to inherit is...disappointment."
    s "Cool. Thanks."

    scene cafefifty15
    with dissolve

    h "Hah..."

    if day == 6:
        h "Saturdays, am I right?"
    else:
        h "Sundays, am I right?"


    s "You know...I really do see the nonbiological resemblance."

    if bonus == True:
        s "And I would also like to take this moment to confirm that I like your breasts just as much as Rin appears to."

        if harukasex == True:
            scene cafefifty16
            with dissolve

            h "Yeah...I am quite aware of that."
            h "You don’t really need to remind me."
        else:
            scene cafefifty16
            with dissolve

            h "Watch it. We’re just {i}friends{/i}, remember?"
            h "Saying things like that is something we should try to avoid for both of our sakes."
            s "Yeah, yeah. I get it. "

    s "Anyway, if you’re concerned about her carrying this on for much longer, you probably don’t have to worry."

    scene cafefifty17
    with dissolve

    h "You’re not rooting for those two to fail, are you?"
    r "Better not be!"
    s "No. I just mean that Rin is naturally obsessive and probably just wants to get some of that rare...{i}true{/i} happy energy out of her or something."
    s "I don’t know. I’m not really well-versed in what it means to feel happy and...do happy things."

    scene cafefifty18
    with dissolve

    h "Uhh...sorry?"
    h "Is this a cry for help? Do you need a shoulder to dry all your tears of loneliness on?"
    s "What? No."

    scene cafefifty19
    with dissolve

    h "Good. Because I do. And if we both had to cry, the angles would be all weird and we’d probably just be crying into the air."
    s "Are you feeling even lonelier than normal, Haruka?"

    scene cafefifty20
    with dissolve

    h "I mean...not any more than {i}normal{/i}. But my default state is enough to make most people want to cry."
    h "All things considered, though. It hasn’t really been that bad lately. "
    h "I’m just trying to stay focused on the business and-"

    scene cafefifty21
    with hpunch
    stop music
    play sound "glass.mp3"

    h "Ah-"

    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene cafefifty22
    with flash
    stop sound

    r "..."
    h "Rin? What’s wrong?"
    r "..."
    s "..."
    h "..."
    s "Should we...do something?"

    scene cafefifty23
    with dissolve

    h "Uhh...Rin? You okay?"
    r "...huh?"
    r "That’s weird. Wasn’t I just..."

    scene cafefifty24
    with dissolve

    r "Ah! Crap!"
    r "I’ll get a broom! And a...mop!"
    r "Cleaning stuff! Yeah!"
    r "Gonna...Gonna go do that!"
    r "..."
    r "Be right back!"

    scene black
    with dissolve2

    "Rin scurries off to the back of the cafe and returns moments later with a mop bucket and a broom to sweep up the broken glass of the mug she dropped."
    "Not really sure how to handle the situation, I stand around and wait for things to pass while Haruka makes another drink for the customer who just lost theirs."
    "After a few minutes, Rin finishes cleaning and returns to the two of us."
    "........."
    "......"
    "..."

    scene cafefifty25
    with dissolve
    play music "cafe.mp3"

    r "So, uhh...whoops! Hahaha..."
    r "Guess mistakes happen to even the best of us, right?"
    r "You can deduct whatever the cost of that mug was from my paycheck. It’s my fault, so I don’t really mind."
    h "I’m not really worried about the mug. I just want to make sure you’re feeling okay since you...seemed a little out of it just now."

    scene cafefifty26
    with dissolve

    r "Nah, dude. I’m good. My hand just twitched or something. It’s fine."
    h "No lightheadedness or...nausea or anything like that?"
    h "You’ve been running around all morning, so-"
    r "No nothing, Haruka. Won’t happen again."
    s "Have you gone on break yet today?"

    scene cafefifty27
    with dissolve

    r "Hm? Even {i}you’re{/i} worried? But...you’re like the...paragon of not worrying about stuff."
    h "He’s probably worried as a friend. Not an authority figure or teacher or...counselor or whatever other jobs he neglects."
    s "Thank you, Haruka. I appreciate that."
    s "And not to throw away another title so soon after getting it, but I’m not really worried right now either."
    s "I just think your {i}new girlfriend{/i} might get a little upset if her lover collapsed at work."

    scene cafefifty28
    with dissolve

    r "L-Lover?...I mean...what even is “love,” you know?"
    r "It’s still way too early to be using words like that because it would make whoever said it first clingy. And if there is anything Rin Rokuhara {i}isn’t{/i}, it’s clingy."
    r "Besides, how can I even {i}be{/i} clingy when we only kissed the one time? "
    r "And even then, it was only for a few seconds. "
    r "Was it a good few seconds? Yeah. It was awesome. But it was only a few seconds. There’s no way I {i}love{/i} her, you know? "
    h "Do you want to go on break a little early today, Rin?"

    scene cafefifty29
    with dissolve

    r "What, like now? But we’re still super busy and I’m totally fine. I swear."
    h "I’ll manage. Besides, Sensei doesn’t typically spend entire days here, and I’m sure you want to talk a little more about Otoha with him."
    r "I mean...kiiiiind of. But there’s not much to say."
    s "I’m right here, you know. You can tell me that directly."

    scene cafefifty30
    with dissolve

    r "Sure. There’s not much to say."
    s "You sure sounded like you had a lot to say earlier. Granted, it was mostly just repeating the same thing over and over again."
    h "Just take her outside and give her a breath of fresh air or something. She’s been in here since we opened and could probably use it."
    r "I’d kind of rather we stayed inside on account of the whole...evil winter wind thing going on outside."
    s "Then I guess we’ll just do that."
    r "Can it be on the couch, though? I still feel awkward about spilling that one customer’s drink and I don’t want them looking at me like I ruined their day."
    s "You certainly have a lot of demands for your break."
    r "Dude, I only get one. I’ve gotta make it the best possible break I can."
    s "Outlooks like that are better aimed toward more vague concepts like life as a whole."
    r "But what does it mean to {i}live?{/i} What if we’re all trapped in some sort of simulation, and one day we’ll all wake up and have, like...cheese for eyes or something?"
    s "What?"
    r "I don’t know. It’s possible."
    r "What if all we are is just cheese in general? What kind would {i}I{/i} be? Mozzarella? Gouda?"
    r "What’s the most bisexual cheese? I wanna be that."
    h "Since a conversation like this would {i}never{/i} happen while clocked in, I’m just going to assume that Rin’s break has already begun and start counting down the time now."
    h "Have fun, you two."

    scene black
    with dissolve2

    "Rin and I take a seat on the couch and she begins telling me all about her rather brief and uneventful first brush with romance."
    "But despite saying just moments ago that she didn’t really have anything worth mentioning, she manages to talk for the duration of her break about all sorts of things."
    "Well, all sorts of things relating to Otoha."
    "How she’s trying her best to take things slow...where she expects things to go by the end of the year...and even her hopes of being in the same class again once I’m no longer her teacher."
    "Of course, I don’t say anything about how I’ll be her teacher for the rest of eternity if all goes according to plan."
    "Just like I don’t say that I expect this honeymoon period to fizzle out over time...and how I think all connections can be broken ten times easier than they can be formed."
    "She has achieved her goal for now, but what comes next?"
    "If it follows the path of most other [young]romances, I would predict tragedy."
    "Even with the mass amount of flags popping up, though, Rin doesn’t seem particularly fazed."
    "Obviously, everything Rin says about Otoha is laced with a dose of hormonal excitement...but there’s a complete lack of worry."
    "In fact, all of the worry I imagined there would be has been swapped out with what feels like a burning sense of conviction."
    "..."
    "Which raises the question-"
    "Why does something still feel off?"

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe50 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon


label rindate50:
    play sound "phonebeep.wav"

    "I tap on Rin’s name in my phone and wait for her to answer. "
    "I’m not sure if she’ll pick up or not following the recent episode in her dorm room, but even {i}I’m{/i} not horrible enough to just leave her hanging if she feels like shit."
    "I was there for Molly, wasn't I? "
    "Granted, I don’t really think I did anything to {i}help{/i} her...but {i}she’s{/i} still alive and, at least to my knowledge, not cutting herself."

    s "..."

    "The phone rings for longer than normal."
    "I’m not sure if Rin is just one of those people who never bothered setting up a voicemail box, but at this point, I feel like I’d probably be better off-"

    play sound "phonebeep.wav"

    s "..."

    "Well, nevermind then."

    s "Rin?"

    "..."

    "I can hear breathing, so I know she’s there...but she’s sure taking her sweet ass time to say hello."

    s "I know you’re there, you know. I can hear you."
    s "..."

    play music "lastdailysong.mp3"

    r "Hey. "

    "I stop pacing around and lean up against the first wall I see to better focus on the conversation."
    "I have a feeling it might be a rough one."

    s "What’s up?"
    r "..."
    s "..."
    s "Rin-"
    r "Are you...free right now, by any chance?"
    s "I wouldn’t have called you if I wasn’t."
    r "Do you think we could maybe...meet up or something?"
    r "Like, somewhere private."
    s "You don’t want to bring Futaba along?"
    r "No...Not this time."
    r "I kind of just want it to be you."
    s "That’s...odd."
    r "Why? Do you not want to?"
    s "No, it’s just that you don’t normally ask to be alone with me when it doesn’t involve your feelings for a girl in some way or another."
    s "Did something happen with Otoha?"
    r "No, Otoha’s great. It’s just..."
    r "It’s just not something I can talk to her about. And Futaba’s already worried sick, so..."
    s "There’s always Molly."
    r "Please, I’m asking for you. "
    r "I want to see you."
    s "Well then hurry up and tell me where to go. It’s not doing you any good just waiting wherever you are."
    s "Oh, where {i}are{/i} you by the way?"
    r "Just in the dorm right now. "
    r "I don’t really want anyone else to see us, so...is it okay if we hang out in some sketchy alley or something like that?"
    s "What a strange request."
    s "You’re not planning on taking advantage of me, are you?"
    r "The only thing I’ll be taking advantage of is your................time."
    s "..."
    r "Get it? Because I paused for a-"
    s "You’re not upset at all, are you?"
    r "I have no idea what I am, Sensei."
    r "I’ll see you soon."

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Rin hangs up the phone and sends me an address not far away from the creepy cathedral Yasu hangs out at."
    "Great."
    "I slide my phone into my pocket and figure that it’s just a coincidence and that Rin isn’t also just a religious cult member now..."
    "But, in the event that she starts trying to indoctrinate me next, I should be prepared."
    "I slide a bullet into the chamber of my revolver and get ready to fight for what I love, which is...not loving anything."
    "Then, I wave my hand to remind myself that the revolver is imaginary and set out toward an area of Kumon-mi that’s almost as sketchy as the second half of town."
    "........."
    "......"
    "..."

    scene rinhappynight1
    with dissolve

    r "Umm...hey."
    s "Hey. You look like shit."
    r "I feel like shit. But I think I’m getting close to the tail end of it."
    s "Did you...come all the way here without a jacket? Aren’t you cold?"
    r "Yeah. I don’t know."
    r "I left it at the dorm and didn’t feel like going back for it."
    s "So you just walked a few miles without it instead."
    r "Pretty much, yeah."
    s "So, what’s the reason for this incredibly suspicious private meeting in the middle of nowhere?"
    r "Venting, I guess? Taking my mind off of stuff."
    r "Probably just going to rattle off a bunch of stuff that’s been popping into my head and hope you can help with some of it because, weirdly enough, I really trust your judgement."
    s "Well, that seems like a horrible idea on your end. My judgement is terrible."

    scene rinhappynight2
    with dissolve

    r "It’s really not, though..."
    r "Like...you’ve never done anything messed up to me and we’ve been friends for a really long time now."

    if bonus == True:
        r "You even gave me a chance to confess to Chika before going after her...when you knew all along that you could have had her whenever you wanted."
    else:
        r "You even gave me a chance to confess to Chika before you started hugging her when you knew all along that you could have had her whenever you wanted."

    r "I...really care about your advice. And I kind of need a lot of it right now."
    s "I’m starting to think I might be a bad influence on you if you’re coming to {i}me{/i} for advice."

    scene rinhappynight3
    with dissolve

    r "Then just pretend I’m coming to you like you’re my counselor and not {i}Sensei{/i}."
    s "You wouldn’t know this since you never show up for counseling, but I’m just as bad at that as I am at normal advice."
    s "In fact, I’m probably even worse when the counselor mask is on."

    scene rinhappynight4
    with dissolve

    r "Well then I guess you {i}are{/i} a bad influence and...that you’re just rubbing off on me or something, because I have no idea who else to talk to about this, or..."
    r "Or how I’m even {i}going{/i} to talk about this because it’s all just circling around inside of my head like some...fucked up, broken washing machine."
    s "Weird comparison, but I get it."
    s "Before that, though, how is your arm?"

    scene rinhappynight5
    with dissolve

    r "Sore."
    r "I obviously have to wear sweaters and stuff to cover everything up, but my sleeves keep sticking to the cuts as the scabs are forming."
    r "And every time I move my arm too quickly, it rips them off and reopens a few and it’s just rinse-repeat, rinse-repeat."
    r "It’s weird, cause like...when I’m doing it, I can barely even feel it. It’s always the days after that hurt the most."
    s "Well, if you don’t mind me going on one of my famous depressing tangents-"

    scene rinhappynight6
    with dissolve

    r "Ooh, I love those! They’re fun!"
    s "Thank you."
    s "But anyway, that feeling you described is essentially just how pain works as a whole."
    s "Nothing is ever its worst as soon as it happens."
    s "The natural reaction to bad news or a traumatic injury is panic."
    s "You don’t have time to really {i}think{/i} about what went down or...feel anything, because it’s all happening so fast."
    s "I’m sure whatever was going through your head at the time of...what you were doing to yourself is no exception to that."

    scene rinhappynight7
    with dissolve

    r "I told you, though...there wasn’t {i}anything{/i} going through my head. That’s why it was all so weird."
    r "It’s like when the battery of your phone dies or something. An immediate switch from full of life to...complete blackness."
    r "And the only thing that can bring it back to life is a surge of power."
    s "You don’t need to explain it or anything. I just don’t want you doing something that will not only put you in danger but ruin everything you finally have going for you."

    scene rinhappynight2
    with dissolve

    r "See, this is why I wanted to see you."
    r "Futaba’s great, but she’s too sentimental when it comes to stuff like this. You’ll just give it to me straight."
    r "Call me a fucking idiot, Sensei. Do it."
    s "Okay. You’re a fucking idiot."
    r "Now...tell me to beat this stupid depression’s...stupid face!"
    s "Beat your stupid depression’s face or whatever."
    r "Now tell me you love me!"
    s "No."

    scene rinhappynight8
    with dissolve

    r "Aww. Mean."
    r "I love {i}you{/i}."
    s "Sorry, did I turn into Otoha overnight or something?"

    scene rinhappynight6
    with dissolve

    if bonus == True:
        r "No, but if you ever do, please send nudes."
        r "I need them to hold me over as I endlessly fight off the undying need to tackle her and just...{i}ugh.{/i}"
        s "Hang in there, Rin. I’m sure it’ll happen soon enough."
    else:
        r "No way. You don't have nearly enough rings."
        s "I would if they could only fit on my stubby little fingers."

    scene rinhappynight7
    with dissolve

    r "I know, I know...It’s just..."
    r "You know what, come with me."
    r "I know nobody’s around because this part of town is dead, but I’d feel a little more...secretive if we weren’t in the middle of the sidewalk."

    scene black
    with dissolve2

    "Rin scurries off and, for a brief moment, her childish energy distracts me from the bags beneath her eyes."
    "It takes a special type of person to wear a smile like that on a body covered in scars, and I’m reminded once more of why I took to Rin in the first place."
    "She’s like a canvas that an artist accidentally spilled every one of his paints on."
    "But instead of trashing it like anyone else would do, he started punching it and punching it, filling it with holes in the shape of a face that, if you look closely enough, resembles something we’ve all felt before."
    "The inherent desire to love and be loved, mixed with a tinge of self-doubt and so many hormones that one good stroke would do it in for the night."
    "This is the person Rin is."
    "A mixture of bad things and good things, held together with glue made from only the best of bodily fluids."
    "It’s a shame she still seems so far away from that last part, though."

    scene rinhappynight9
    with dissolve

    r "Okay. This is {i}slightly{/i} better than out there in the open."
    s "What was it that you couldn’t tell me twenty feet away from where we’re standing right now?"
    r "Just more stuff about Otoha, probably."
    r "And how I’m worried I’m gonna snap and do something bad before she’s ready for it."
    s "Probably not the best idea, Rin."

    scene rinhappynight10
    with dissolve

    r "Then...teach me how to control myself better!"
    r "I don’t wanna mess things up, and I’m already one step closer to doing that by hiding my cutting from her."

    if bonus == True:
        s "You’re asking {i}me{/i} how to...not have sex with girls?"
    else:
        s "Are you asking me to purchase you a straight jacket?"

    r "No, dude. I’m asking you how you always manage to hold yourself back."

    scene rinhappynight11
    with dissolve

    r "The Chika thing {i}still{/i} surprises me."
    r "Like...I’m not allowed to say this anymore because girlfriend-"
    s "I won’t say anything. Don’t worry."
    r "I know. I was gonna say it anyway because I trust you. But yeah, Chika is {i}so{/i} fucking hot."
    r "I don’t know how you kept your hands to yourself. I really don’t."

    if bonus == True:
        s "There was just someone else I liked more, I guess."
    else:
        s "Easy. I have a complete disinterest in both romance and intercourse and am only here to make all of you happy and help you pass college."

    scene rinhappynight12
    with dissolve

    r "And, like..."
    r "With me too."

    if bonus == True:
        r "Not just with the delirious flashing stuff and the...random kiss we had after our date. But like, as a whole."
        r "Why didn’t you ever push for more?"
        r "You wanted to, didn’t you?"
        r "I might seem dense sometimes...but there have been a lot of moments where I’ve thought, “You know, I wouldn’t stop him if he did something right now.”"
        r "But you never did."
        r "I don’t want you to tell me {i}why{/i}, though. I want you to tell me {i}how{/i}."
        r "How can I do that with Otoha to avoid ruining the best thing that’s happened to me since meeting you?"
        s "Wow. Was I really the best thing up until that?"
    else:
        r "I know you know about the trombone, Sensei..."
        r "And I know...you've always wanted to try playing it as well..."
        s "Not now, Rin. I'm not ready to talk about that yet."

    scene rinhappynight13
    with dissolve

    r "I wasn’t kidding when I said I loved you, you know."
    r "Not everyone would hold my wrist and call my roommate in the middle of the night to come take care of me."
    r "Not everyone would volunteer to let me cry into them if things get terrible."
    r "And not everyone would come meet me in some sketchy part of Kumon-mi this late to just...talk about stuff."
    r "You are...{i}so{/i} important to me, Sensei. So important."
    r "Like..."
    r "Yeah."
    r "{i}So{/i} important..."
    s "Well, thanks. But I’m pretty sure this conversation was supposed to be about Otoha and not me."

    if bonus == True:
        r "I’m still waiting on you to tell me how to not start groping her in the middle of casual conversation."
        s "I mean, that’s just kind of a common sense thing. Don’t grope {i}anyone{/i} in the middle of casual conversation."
    else:
        r "I'm still waiting on you to tell me how to not start hugging her in the middle of casual conversation."
        s "The best hugs are those not witnessed by entire groups of people. Keep that in mind."

    scene rinhappynight14
    with dissolve

    r "Got it! Next tip, please."

    if bonus == True:
        s "Masturbate frequently."
    else:
        s "Dance frequently."

    s "Like, before every time you two hang out."

    scene rinhappynight15
    with dissolve

    if bonus == True:
        r "Oh my god. Is {i}that{/i} why you never made a move on me? Because you were too busy making moves on yourself?"
        s "Some secrets are meant to stay hidden, Rin."
        r "I don’t know if I should be flattered, embarrassed, or grossed out."
        s "You should be listening to my advice, because I’m about to give you the most important piece of the puzzle you’re trying to solve."
        r "Okay, okay. I’m all ears. Hit me."
        r "Just not in the arm because it still hurts."
        s "The best way to hold yourself back is to just...do it."
        r "..."
        s "..."
        r "That’s it? That’s your super awesome, foolproof advice? Just don’t do it?"
        s "Simple, right?"
        r "So simple that it must be a joke."
        s "Rin, have you stopped to think that maybe the reason you’re having such a hard time holding back is because that’s {i}all{/i} you’re thinking about when you’re with Otoha?"
        s "Just enjoy your time finally being happy or whatever."
        s "And, it sounds very weird saying this, but stop thinking of sex so much."
    else:
        r "That helps?"
        s "Surprisingly, yes. Dancing gets the blood pumping and prevents you from making bad decisions."
        r "But every time I try to dance, I fall down and scrape my knee."
        r "And every time I'm around Otoha, I get this crazy urge to just dance anyway. Even when I know my knees will hate me for it."
        s "You must learn to control the dance."

    scene rinhappynight16
    with dissolve

    r "But she’s so hot! It’s hard!"

    if bonus == True:
        s "Well, the only alternative is just making {i}her{/i} want {i}you.{/i}"
        r "But I’m dorky and weird and awkward. And if I take my clothes off, she’ll see my arm."
        s "Then just...put yourself into risky situations. Sleep in the same bed. Lock yourselves in a room together. Shower in the same stall."
        s "There are a bunch of opportunities open to you as two girls in an all-girls[school]. We make literally no effort to separate you all."
    else:
        s "Do not give into the dark, Rin. You are better than that."

    scene rinhappynight17
    with dissolve

    if bonus == True:
        r "That was quite a few scenarios you managed to drum up off the top of your head, Sensei."
        s "I spend a lot of time thinking about lesbians."
        r "You sure you’re not just trying to spy on Otoha and me?"
        s "No. But if you happen to accidentally call me before the first time you two start experimenting on one another, I won’t mind."
        r "I don’t know if I like the idea of you listening to Otoha’s sexual moaning and stuff."
        r "Assuming of course that I’m actually able to make her feel anything and that I’m not the world’s worst bisexual."
        s "Just keep the phone closer to you then. Just one voice will do."
        r "Okay but what if I sound really weird? Like, not sexy at all. Just weird noises."
        s "..."
        s "I can always hang up?"
    else:
        r "I am?"
        s "Maybe? I don't really know. I'm just trying to give good advice."

    scene rinhappynight18
    with dissolve

    r "Solid plan. Thanks, homie."
    r "Will keep it in mind when I try and inevitably fail at making Otoha want to do stuff."

    play sound "texttone.wav"
    scene rinhappynight19
    with dissolve

    r "Oh! Speaking of which, that’s probably her."
    r "We send each other goodnight texts because we’re dating."
    r "Have I mentioned yet that Otoha and I are dating?"

    if bonus == True:
        s "I’ll consider it a real relationship the moment one of you two gets the other to orgasm."

        scene rinhappynight20
        with dissolve

        r "Like, physically? Because...you know..."
        r "If fantasies are involved and stuff, it’s prooooooobably safe to assume it’s already a real relationship based on that criteria."
        s "Obviously not counting that."
        r "You sure? Cause I’m not confirming anything, but it’s prooooooooobably happened more than once. By like...somewhere in the double digits."
        r "Or triple."
        r "She’s so hot."
        s "..."
        s "Just text her back, Rin."

    scene black
    with dissolve2

    if bonus == True:
        "Instead of just texting her, Rin decides to call Otoha and say goodnight."
        "They continue to chat for a few moments, and it ultimately leads to Rin admitting that she went out for a late night walk to “get her mind off of stuff.”"
        "Of course, she never admits that she met up with me. And I don’t blame her for that."
        "Otoha knows that Rin and I have kissed. And she doesn’t seem to have fully warmed up to me just yet in general...so keeping it secret is probably for the best."
        "The call ends shortly after and, without really exchanging any words about it, Rin and I appear to silently and mutually agree that it’s time to head back."
        "Along the way, we talk about a number of other things."
        "I don’t remember any of them."
        "I wound up, once again, getting too distracted by the dramatic contrast between her appearance and her actions."
        "When we make it back to the dorm, she tells me she loves me again."
        "I nod and head home."
    else:
        "Rin quickly goes back to doing that thing where she just repeatedly talks about dating Otoha and I have to escape into an alleyway because I drank too much water and had to pee."
        "I do it while she's looking away, so she doesn't realize I'm gone at first and I feel really bad about it afterwards."
        "But this is for the best and now my bladder is happy."

        r "Sensei? Where did you go? I have to tell you about my girlfriend."
        s "Oh no."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindate50 = True
    $ rinsad = False
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm55:
    scene mommyshome1
    with fade
    play sound "knock.mp3"

    "I knock on Rin’s door and wait for her to answer."

    play sound "dooropen.mp3"
    scene mommyshome2 with dissolve

    ri "..."
    s "..."

    "Oh."

    ri "You’re not Rin."
    s "Shouldn’t...I be the one saying that to you? What are you doing in her room?"
    ri "Oh, you know. Just having a crisis. The usual."
    ri "Where’s Wakana? Or Imani?"
    s "Sorry to be the bearer of bad news, but I don’t usually take them to the dorms with me."
    ri "You come here often?"
    s "Are you hitting on me?"
    ri "I wasn’t trying to. "
    s "I was joking."
    ri "Oh."
    ri "Well, you’re not very funny."
    s "And you’re not very clothed."

    scene mommyshome3
    with dissolve

    ri "Yeah. Rin took my clothes to the laundry room so I’ve been stuck wearing this towel for the last twenty minutes. "
    s "I take it that means...you’re one of her moms?"

    scene mommyshome2
    with dissolve

    ri "I’ve been told that I am not allowed to reveal that information to anyone. "
    s "Would you rather I just assume you’re some sort of prostitute she hired, then?"
    ri "Hey. I may occasionally make out with random people I have only known for several minutes, but I’m certainly not a prostitute. "

    scene mommyshome4
    with dissolve

    ri "Though, there was one time in high school that I jerked off the singer of some band for a pair of front row tickets to a show."
    ri "Turned out later the show was free and it was all standing room, but hey. You live and you learn."
    s "I can’t tell if...that was supposed to be a joke or not."

    scene mommyshome5
    with dissolve

    ri "Honestly, man. My whole life is a joke right now, so go ahead and laugh at whatever you want. Just don’t tell Rin you saw me here. Or know that I’m her mom. Which I am. But I didn’t tell you that."
    ri "Anyway, want to come inside and hang out? I’m bored."
    s "Is it really a smart idea to be inviting me in when you just said literally ten seconds ago that I’m not supposed to know you’re here?"
    ri "Probably not. But since I have made nothing but poor choices over the last several months, I’m worried that breaking that pattern will lead to something even worse happening."
    s "Fine. But I don’t have any concert tickets to offer you in exchange for your services."
    ri "I downloaded that CashApp thing to send Rin money for a date last month. I can take that too if you also have the app."
    s "Okay, are you {i}actually{/i} a prostitute? Because I’m starting to think my joke was less of a joke than I intended."
    ri "Man, I don’t know {i}what{/i} I am anymore. But hurry up and come inside before anyone sees me dressed like this and thinks I’m a prostitute."

    play sound "dooropen.mp3"
    scene black
    with dissolve

    "I follow Rika into Rin’s room and..."
    "Check to see if I have CashApp installed."
    "........."
    "......"
    "..."

    scene mommyshome6
    with dissolve2

    ri "Look at us- like two peas on a bed. Hanging out on our own instead of in the company of a group."
    ri "We can finally play Yahtzee."
    ri "Not sure how fun it'll be with only two people, though."
    s "You know, I really should have guessed you were Rin’s mom the second I found out you had a daughter. I can see where she gets her...Rin-ness from now."

    scene mommyshome7
    with dissolve

    ri "No way. She’s way too level-headed and smart to be anything like me. My partner always said I’m just a few steps away from..."
    ri "From..."
    s "Don’t do it."

    scene mommyshome8
    with hpunch

    ri "GAAAAAAAAAAAAAAHHHHHH!!!!!"
    s "Okay. Have fun crying, I guess."
    ri "I’m not crying! I’ve moved away from the sad stage and am now in the angry one! "
    ri "I’m a grown woman living in my teenage daughter’s dorm room! Why is this happening to me?!"
    s "Wait, you’re {i}living{/i} here now?"

    scene mommyshome9
    with dissolve

    ri "Pathetic, right?"
    s "Kind of, yeah."
    ri "I won’t be here for long. Just trying to...get back on my feet, I guess. Start over."
    ri "Rin’s other mom is the one who technically owns our house, so when she told me to pack my shit and leave..."
    ri "Well, I packed my shit and left. No way am I getting arrested again. Jail is cold."
    s "You were...arrested?"

    scene mommyshome10
    with dissolve

    ri "You haven’t been?"
    s "Why would you just assume that someone else has been arrested? You barely even know me."
    ri "Dude, look where you are right now. If the wrong person showed up, you’d be in the back of a cop car in no time at all. And that shirt’s so thin you wouldn’t even survive intake."
    s "That’s...fair. But what were you arrested for?"

    scene mommyshome11
    with dissolve

    ri "Nothing fun. Went through a rebellious phase a while back. Lots of protests and breaking shit and maybe occasionally setting a building or two on fire."
    s "..."
    ri "We’ve all got our embarrassing background stories, though. Things don’t stay the same forever. "
    ri "I mean, just look at me now. I’m-"

    scene mommyshome12
    with dissolve

    ri "Wait...I’m even worse now. "
    ri "My life {i}sucks.{/i}"
    ri "And it’s totally shitty because, like...everything was great just a couple years ago."
    s "Did something happen? Because the impression I got from Rin is that you and your “partner” were doing really well together."

    scene mommyshome13
    with dissolve

    ri "We were. For a {i}long{/i} time. Like, I’m talking multiple decades..."
    ri "But one day, the spark just started fading. "
    ri "We tried making it work for Rin since we thought it would be good for her to grow up in a functional same-sex household, but somewhere around the time she started middle school..."
    ri "Things just...I don’t know. Felt beyond repair."

    scene mommyshome14
    with dissolve

    ri "I get it. I {i}hate{/i} it...but I get it."
    ri "There was always this feeling in the back of my head that the next fight would be the last. But when that feeling was finally {i}right...{/i}"
    ri "Well, turns out I wasn’t as ready as I thought I was."
    ri "It fucking blows, man. I really wanted things to work. Spent like half of my life with that woman."
    ri "But you can fall out of love just as easily as you fall into it. So...here’s hoping that the two of us manage to fall again someday. "

    scene mommyshome15
    with dissolve

    ri "So anyway! Tell me about Rin’s girlfriend since I still haven’t gotten to meet her!"
    s "She lives right upstairs in Dorm 8. Just go knock if you want to meet her that badly."
    ri "I thought about it. But Rin told me she’ll introduce us soon and that rushing things would make stuff weirder than it already is or something. Which is apparently pretty weird."
    s "They’re a...good couple, I guess. Otoha’s just a little uncomfortable about certain aspects of the relationship, I think."
    ri "Like the aspect where they both have vaginas?"
    s "Not how I would have worded it, but I think so."

    scene mommyshome16
    with dissolve

    ri "It’s like that with a lot of girls at first."
    ri "I lost count of how many I had feelings for only to find out later that they were “just experimenting.”"
    ri "I’m sure it’ll happen to Rin too, but...hey. Maybe she’ll luck out and get a good twenty-odd years with this Otoha girl in before {i}she{/i} gets kicked out and has to go live with {i}her{/i} daughter."
    ri "Man, I’m gonna be such a cool grandma."

    play sound "dooropen.mp3"

    s "Maybe...wait a little while longer before you start fantasizing about grandchildren."
    r "MOM!"

    scene mommyshome17
    with fade

    ri "Hi! Welcome home."
    r "What are you doing?! I told you not to answer the door for anyone!"
    ri "Yeah, but what if it was {i}you?{/i} I didn’t want you getting locked out of your own room for all eternity because you forgot your key."
    r "I {i}have{/i} my key!"
    ri "How was I supposed to know that?! I thought I was being considerate!"
    r "By letting my teacher into the room while wearing nothing but a towel?! Sensei is very weak to girls! Things like this aren’t good for his mental health!"
    s "Hey, you’re weak to them as well."

    scene mommyshome18
    with dissolve

    r "Yes! I know! And just imagine how things would go if a friend’s mom led {i}me{/i} into a cramped room wearing nothing but a bath towel! It would not end well!"
    s "That’s a fair point. What I’m hearing is this is all Rika’s fault and that I did nothing wrong by going along with it."
    ri "Rin, I know you’re embarrassed- but hear me out. I already {i}know{/i} this guy."

    scene mommyshome19
    with dissolve

    r "What? How? You live like a gajillion miles away. "
    r "Well...{i}lived.{/i} You live here now. But I’m like 99%% sure that’s against the rules, so I have no idea how I am going to make this work. Especially with you...opening doors for strangers."
    ri "But he’s not a stranger. I just said that. "
    ri "We’re actually drinking buddies."

    scene mommyshome17
    with dissolve

    r "You don’t even drink!"
    ri "I do now. {i}I am not the Mom you once knew.{/i}"
    r "What the fuck is going on right now?!"
    ri "You tell me! Imagine {i}my{/i} surprise when my drinking buddy showed up at my front door looking for my daughter."
    ri "I felt like a character in one of those Lifetime movies your other mom always watches."
    ri "Not to mention I’m barely even- wait! Where are my clothes?! You said you would wash them! I have an interview tomorrow!"

    scene mommyshome20
    with dissolve

    r "I {i}am{/i} washing them. It takes {i}time.{/i} This is something you would know if you didn’t always make Mom do your laundry instead of doing it yourself."
    s "Didn’t she just call {i}you{/i} “Mom” a second ago?"
    ri "We’re both “Mom.”"
    s "Doesn’t that get confusing?"
    ri "You’d think so, but not really. "
    r "Get up. Both of you."
    ri "But what if my towel falls off? I haven’t even given Sensei my CashApp yet and it wouldn't be fair to everyone else if he got to see something like that for free."
    s "I knew it. You {i}are{/i} a prostitute."

    scene mommyshome21
    with hpunch

    r "NOBODY HERE IS A PROSTITUTE! "
    ri "Oh, thank God. It’s always so hard asking your daughter if she’s selling her body. Now I know for sure."

    scene black
    with dissolve

    r "I SAID GET UP, DAMN IT!"
    "........."
    "......"
    "..."

    scene mommyshome22
    with dissolve

    r "Ugh...isn’t it supposed to be the mother who takes care of the daughter? How did all of this fall on {i}me{/i} all of a sudden?"
    ri "Hey, I took care of you for years. It’s up to the child to take care of the parents once they can’t function on their own anymore."
    r "You are 43. You are plenty “functional.”"

    scene mommyshome23
    with dissolve

    ri "I’m 42! There is a big difference!"
    r "Not really!"
    s "I take it your house was always pretty loud, wasn’t it?"

    scene mommyshome24
    with hpunch

    riri "Shut up!"
    s "Well, fuck me I guess."

    scene mommyshome25
    with dissolve

    r "Mom, I’m happy to have you here. I don’t even mind sharing a bed with you while you look for a new place. But {i}please{/i} be careful."
    r "Not only do I want Otoha’s first impression of you to be, you know...{i}normal,{/i} but showing yourself around here could get me in trouble. And I can’t risk that right now. I {i}like{/i} school."
    ri "How come Sensei can show himself around the dorms, but I can’t? He has a penis and penises are dangerous. I have seen things."
    s "What does that even mean?"
    r "Can we not talk about Sensei’s gigantic penis and focus on the matter at hand, please?"

    scene mommyshome26
    with dissolve

    ri "Wait a second...how do you know it's a {i}gigantic{/i} penis?"
    r "I...don’t. I just...you know."
    ri "..."
    r "..."

    scene mommyshome27
    with dissolve

    ri "..."
    s "Hey, don’t look at me. I haven’t done anything sexual with your-"

    scene mommyshome28
    with hpunch

    ri "Hm!"
    s "Welp. Guess this is happening now."
    r "Mom! What the fuck are you doing?! That is literally sexual assault!"
    s "Leave it to a convicted felon to grab someone’s crotch without permission."

    scene mommyshome29
    with dissolve

    r "You’re a convicted felon?!"
    ri "I was planning on telling you on your twentieth birthday."
    r "What kind of present is that?!"
    ri "Also, for the record, you were right. This thing is intimidating. Stay away, you hear me? They’re {i}dangerous.{/i}"

    play sound "dooropen.mp3"
    scene mommyshome30
    with dissolve

    f "Rika! You really {i}are{/i} here!"

    scene mommyshome31
    with dissolve

    f "I thought Rin was just joking when she said you were coming to live with us, but-"
    ri "..."
    f "..."
    r "Hah..."

    scene mommyshome32
    with hpunch

    ri "Hey, Futaba! How’s it going?!"
    ri "Nothing to see here. Just checking the size of your teacher’s penis. You know how it is."
    f "Uhh..."
    s "I really didn’t have anything to do with this."

    scene mommyshome33
    with dissolve

    f "I’m just...going to forget I saw that, since...that would...probably be best for everyone..."
    ri "You stay away from it too, you hear me? That thing could cause some major damage to a delicate flower like you."

    "Joke’s on you, Rika. It already has."

    f "I will...be sure to keep that in mind."
    r "..."
    s "..."
    s "What? Why are you looking at me like that?"
    r "I need somewhere to direct my anger. Futaba is a cinnamon roll and all of my rage just bounces off of my mom. You are the only target I have left."
    s "It’s not fair that I am now the sponge for your anger when the only reason I am here right now is because I wanted to talk to {i}you.{/i} I did not ask to be groped."

    "But that doesn’t mean I didn’t like it."

    scene mommyshome34
    with dissolve

    ri "How are things going for you, Futaba? Good? Because my life’s a fucking mess right now."
    f "I’m sure you’ll be back on your feet in no time at all. Our room is your room."
    r "Yes. Hooraaaaay."
    ri "Come on, Rin. Would it kill you to sound a little more excited? I might be homeless, but I’ve still got more money than you. I think."
    ri "I hope."
    ri "And I’m full of awesome bisexual knowledge that I can bestow on you to make sure your relationship goes well."

    scene mommyshome35
    with dissolve

    r "My relationship is going just fine! I don’t need your “awesome bisexual knowledge” when that’s, like...the {i}one{/i} thing I’m really good at!"
    s "{i}Are{/i} you good at it? Because most of the time it seems like it’s your greatest weakness."
    ri "Aww, my little girl’s a disaster lesbian just like her mom."

    scene mommyshome36
    with dissolve

    r "Okay! That’s it!"
    r "Sensei, a word please? {i}Outside?{/i}"
    s "Ugh...fine."
    s "But only because I feel like you might actually pop a blood vessel if you stay in here for any longer."

    scene black
    with dissolve2
    stop music fadeout 12.0

    "Rin storms out of the room and I follow closely behind, leaving Rika and Futaba to...continue embracing one another while I step {i}away{/i} from girl on girl contact and into the hall."
    "Not being quite sure of how much Rin even {i}knows{/i} about Rika’s situation, though...I’m not really sure how I’m going to approach this “talk” we’re about to have."
    "The fact that Rika and...whatever the name of Rin’s other mom is were concealing the decaying nature of their relationship from her makes me feel like...well, like I shouldn’t reveal it either."
    "But without being directly told {i}not{/i} to do that-"
    "I’m not really sure how things will end."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm55 = True

    "........."
    "......"
    "..."

    jump rindorm55p2

label rindorm55p2:
    scene rinoutsidemom1
    with fade
    play music "summerwind.mp3"

    r "Dude! How come you never told me you knew my mom?!"
    s "How come you never told me she was so hot?"

    scene rinoutsidemom2
    with dissolve

    r "Wait, really? You think so?"
    s "Do..."
    s "Do you {i}not?{/i}"

    scene rinoutsidemom3
    with dissolve

    r "I don’t know. Not really? I guess I’ve never thought of it before."
    r "..."
    s "..."
    r "Yeah, I guess I just don’t see it."

    "????????????"

    s "Didn’t you say something about wanting to marry your mom when you were younger, though?"
    r "I was talking about my other mom, obviously."

    scene rinoutsidemom4
    with dissolve

    r "But, back to the topic at hand! What the Hell, Sensei?!"
    s "I seriously had no idea you two were even related. Though, in hindsight, if I put any amount of thought into it at all, I probably could have figured it out."
    s "It’s not like we’ve known each other for very long or anything. She’s just the newest addition to my cool new adult friend group."

    scene rinoutsidemom5
    with dissolve

    r "Since when do you have an adult friend group?! What about me?! Why is everything falling apart all of a sudden?! Stuff like that is supposed to be saved for when we go to the beach!"
    s "How much do you even know about your mom’s situation, Rin? "

    scene rinoutsidemom6
    with dissolve

    r "Well...how much do {i}you{/i} know? Because it’s plain as day that they’re not together anymore on account of the fact that I am washing her clothes, but I still don’t get {i}how{/i} it happened."
    s "I’m going to be trustworthy for once and not reveal anything since this is my “hot boy summer” and I am attempting to turn over a new leaf as a decent person."
    r "Okay, first off, stop trying to sound young. Second, it’s hot {i}girl{/i} summer. Third, you weren’t even {i}close{/i} to using that term right. Fourth, you are a bad person. Fifth-"
    s "How many numbers are there going to be? Because I’m starting to think I don’t have time for this."
    r "Just seven more. Fifth, you-"
    s "Okay, moving right along- just get all of the details from Rika if you really want to know what went down."
    s "Unless you two are on weird terms or something. Which I’m starting to think you might be on account of the fact that she still hasn’t met Otoha and that you don’t find her attractive."
    r "Would not wanting to fuck my mom really put us on weird terms?"
    s "Probably. It’s the first girl I’ve ever encountered that you don’t want to have sex with. "
    s "Well, two counting Molly."
    r "Oof."

    scene rinoutsidemom7
    with dissolve

    r "We’re not on weird terms or anything. I wouldn’t have invited her to stay with me if we were. And the Otoha thing is...well, suddenly a lot harder to approach. So I’m still trying to figure out what to do."
    r "Otoha’s...Well, she’s got some issues or...doubts about same-sex couples. And I’ve always pitched my parents to her as the perfect example of how it’s done and how it can work."
    r "But considering the fact that {i}that{/i} relationship is now knocking on death’s door, it doesn’t really make my pitch all that reliable, does it?"
    s "No...but you can’t hide her forever, you know?"

    scene rinoutsidemom8
    with dissolve

    r "Of course. I know it’s only a matter of time. "
    r "I just think that waiting until she’s not {i}living in my room{/i} is probably for the best right now since I don’t want Otoha thinking I’ve just been lying about how functional my life is."
    s "You have one of the most dysfunctional lives I know, Rin."
    r "Me, personally? Sure. But apart from the whole being adopted thing, my home life was always totally normal and not at all {i}dysfunctional.{/i}"
    r "They always say that children are a reflection of their parents. And while my mom is great, you’ve gotta admit that she’s been in better shape, right?"
    s "Beats me. She’s been a wreck ever since I met her. Think the issues with mom number two might run a little deeper than we think."

    "I expertly pretend like I have no idea what I’m talking about and keep my “hot boy summer (whatever that means)” alive. "

    scene rinoutsidemom9
    with dissolve

    r "Wow. You really weren’t kidding when you said you haven’t known each other long, have you?"
    s "I only see her on Fridays, really. And even then we haven’t exactly talked much."
    s "She reminds me a lot of you, though."
    r "She does? How?"
    s "Just in the fact that she’s easy to get along with and clings to others as if it’s second nature."

    scene rinoutsidemom10
    with dissolve

    r "Clings to...others..."
    s "..."
    r "..."
    s "R-"

    scene rinoutsidemom11
    with hpunch

    r "That’s it!"
    s "What’s {i}it?{/i} What does that-"

    scene rinoutsidemom12
    with dissolve

    r "You have to date my mom!"
    s "..."
    r "It’s the shortest and easiest way to solve the issue of her being too dependent on my other mom! Plus, it will help get her out of my room so I can finally introduce her to Otoha!"
    s "And...how did you reach that conclusion, exactly?"

    scene rinoutsidemom13
    with dissolve

    r "She’s clingy and you’re obsessed with girls. If she falls in love with you, she won’t need my other mom anymore and she’ll go back to not crying every five minutes."
    s "You don’t feel weird about me dating your mom?"
    r "Nah. You’re already like a dad to me anyway."

    if rinbetrayed == False:
        s "Even though we’ve made out?"
        r "I’m technically an orphan. Chances are that sort of thing would have happened if I had a foster dad anyway."
        s "I feel like saying that doesn’t exactly set a good example for other orphans or...foster fathers out there."
    else:
        s "Gee, thanks. I feel myself falling further into the friend zone every single day."
        r "Maybe you’ll find Chika down there as well and not have to feel so alone?"
        s "Okay, you really need to get over that."
        r "Fuck you."

    s "Besides, if anyone is going to date your mom, it should be Imani."

    scene rinoutsidemom14
    with dissolve

    r "Why should it be Imani?"
    s "Because those two have already made out."

    scene rinoutsidemom15
    with dissolve

    r "My mom made out with Imani?!"
    s "Yeah. It was awesome."
    r "I want to make out with Imani!"
    s "You have a girlfriend."
    r "She wants to make out with Imani too! We all do! Imani is hot!"
    s "Also, what about Futaba? I thought you wanted me to be with {i}her?{/i}"

    if harukasex == True:
        "Haruka as well, but...I’m pretty sure that might just be some sort of sexual fantasy of Rin’s and not something she actually sees working out any time soon."

    s "Dating your mom would throw a wrench in that plan, wouldn’t it?"

    scene rinoutsidemom16
    with dissolve

    r "Ahh, fuck...you’re right. Futaba would feel super betrayed and used if you started seeing my mom right after taking her virginity."
    s "Oh. So I guess that’s a thing you know now. Thanks, Futaba."

    scene rinoutsidemom17
    with dissolve

    r "How was it?"
    s "Are you seriously asking me for a review of sex with your best friend?"
    r "Is that weird?"
    s "No. It was great. But now you have to tell me how sex with Otoha is whenever you two get there."
    r "I touched her boobs for like five minutes once. That was cool. They’re very...firm. Real quality breasts. A lot different from Futaba’s."
    s "If you’ve groped Futaba as well, it seems only fair that I get to grope Otoha next."
    r "I mean..."

    scene rinoutsidemom18
    with dissolve

    r "So long as it’s all three of us...but I don’t really think she looks at you that way."

    if rinbetrayed == True:
        r "Which is great news for me since you won’t be able to beat me to having sex with her while I’m nervously lagging behind. "

    s "I don’t think she looks at me that way either. But I’m glad to hear that this threesome isn’t entirely impossible as I was starting to think you were losing interest in me."

    if rinbetrayed == True:
        scene rinoutsidemom19
        with dissolve

        r "And why exactly would I be interested in you after all you’ve done to me?"
        s "Because even if you’re mad at me for everything I did, you keep me close to your heart. Which means there must be {i}something{/i} there, right?"
        r "It’s not like I’d tell you if there was. Especially not when I already have someone I care about more than...almost anything."
    else:
        scene rinoutsidemom20
        with dissolve

        r "What...What exactly do you mean by that?"
        r "I already told you that Otoha’s the one I-"
        s "For the sake of your impulsiveness and the fragility of both your heart and relationship, I’m going to keep my mouth shut."

    s "Regardless, I just feel like the two of us have been getting a lot more...distant ever since you started seeing Otoha."
    s "Which I don’t blame you for, of course. She's the one you care the most about and I can’t expect to just change that by having a penis and talking to you."
    s "We’re just not as close as we used to be, I guess. "
    s "But if that’s just me talking too much, I-"
    r "No...You’re right."

    scene rinoutsidemom21
    with dissolve

    r "I feel the same way. And I miss you. "
    r "I was actually really upset for a day or two after I heard about the virginity thing from Futaba."
    r "Not just because I wasn’t there, though. But because you didn’t even think to come to me about it and I feel like you {i}would{/i} have if this were still..."

    scene rinoutsidemom22
    with dissolve

    r "The beginning of..."
    r "The...school...wait, what month is it?"

    scene rinoutsidemom23
    with dissolve

    r "A-Anyway! You’re totally right. It’s just really hard for me right now to find time for both of you."
    r "I want things to be as normal as possible for Otoha since she’s still so, uhh...anxious about everything. And when I’m with you, I..."
    r "I..."

    scene rinoutsidemom24
    with dissolve

    r "I get a little too excited."
    r "I don’t want her to feel like she’s moving down my priority list. And she's actually really sensitive despite always seeming so cool and collected."
    r "But that’s not fair to you either since you’re...a good friend of mine..."
    r "And one that, even with all of the hiccups, I still cherish."

    scene rinoutsidemom25
    with dissolve

    r "There’s always a place for you in my heart, Sensei. And even if it feels like the walls are caving in, I can guarantee you that place isn’t shrinking at all. "
    r "The rest of it’s just getting bigger."
    s "I can accept that. Like I said, I understand it and don’t hold anything against you. The top priority right now is keeping things stable with Otoha. "
    s "Which means that I will have to take one for the team and fuck your mom. But remember, Rin- I am only doing this for {i}you.{/i}"
    r "Woah, hold on. Nobody said anything about {i}fucking.{/i} I was just suggesting that you make her {i}want{/i} to fuck you since that would keep her sane long enough to look like a functional adult in front of Otoha."
    r "But if you’re planning on making me a little brother or sister, I don’t think I-"

    scene rinoutsidemom26
    with dissolve

    r "Wait..."
    r "..."
    s "..."
    s "Rin?"
    r "Shut up, I’m thinking."
    s "I was just joking, you know. There’s no way I’m going to impregnate your-"
    r "Call me “onee-chan” but do it in like, a...girly voice. I think I might want a little sister."
    s "I don’t think I’m capable of making a girly voice. Nor am I willing to call you “onee-chan.”"

    scene rinoutsidemom27
    with dissolve

    r "Ugh. You’re no fun. Guess I’ll just be an only child forever because no one will have sex with my mom."
    s "Wait, so {i}am{/i} I supposed to have sex with Rika? Or am I not supposed to do that? Because I feel like you’ve flipped positions over the last two minutes."

    scene rinoutsidemom28
    with dissolve

    r "I don’t know, man. Do whatever you want. I still think my parents are going to get back together, but my mom could definitely use a good “magic missile” right now."
    s "Please don’t call it that ever again. "
    r "Whatever happens, just don’t tell Futaba about it. Or {i}me.{/i} I don’t want to know. "
    r "Finding out you banged my mom would be, like...the weirdest form of NTR ever."
    r "And now that I’m leveling with you, I might as well add that I have no clue if the dating thing would even work in the first place. I’m just running out of ideas over here, Sensei. "
    r "I desperately want things to work out with Otoha and me. But it’s mega stressful feeling like I have to fucking choreograph my entire life to make it work."
    r "Maybe I just need to get laid too. That sounds like it would help."
    s "I’ve felt that way since the day I met you and agree that it would probably turn your life around."
    r "Sometimes, I feel like I’m going to die a virgin."
    s "Not if I have anything to do with it."

    scene rinoutsidemom29
    with dissolve

    r "That would certainly fix our “distance” problem, wouldn’t it?"

    if harukasex == True:
        s "Yes, but I have already wrecked your boss’s home and plucked her from the clutches of another man. Destroying one more might make me a bad person. "
        r "Maybe. But on the bright side, it would mean that Haruka, Futaba, {i}and{/i} me all got boned by the same person! We’d have something to bone over! I mean...bond. "
    else:
        s "It would. But I’ve got a good streak so far of not having sex with people in relationships. So just keep hoping Otoha takes your pants off while I pretend that I won’t be fantasizing about that later."
        r "Don’t worry. The amount of time I will spend fantasizing about that will more than make up for it."

    scene rinoutsidemom30
    with dissolve

    r "So...we cool? No longer worried that I’m gonna just slowly wean you out of my life?"
    s "I wouldn’t ever let that happen anyway since you’re such an essential part of mine."
    r "Likewise, homie."
    r "Let’s...get together soon. Find time for just the two of us and see if we can get things back to the way they were before all of the chaos and stress and stuff."

    scene rinoutsidemom31
    with dissolve

    r "But, for now...I’ve got a load of laundry to finish."
    r "Thanks for letting me vent a little bit. And for not telling me when you ultimately sleep with my mom."
    s "And...thanks for your blessing, I guess?"

    scene black
    with dissolve2

    "Rin heads back into the dorm- and while I should be narrating about how this conversation went way better than I expected it to...really all I can think about is having sex with her mom."
    "That’s on Rin, though. I was planning on saving those thoughts until I got home later. It’s not my fault they’ve been pushed up. "
    "The “weirdest form of NTR” aside, though...I’m worried about her."
    "She’s surprisingly calm for being in such a stressful predicament right now. "
    "And all I can hope is that it doesn’t wind up getting to her."
    "Or that something else doesn’t get to her first."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm55p2 = True
    stop music fadeout 7.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label rinspecial55:
    scene otoharinoutside1
    with dissolve2

    o "..."
    r "..."
    o "So...are you gonna start? Or should I? "
    r "You start. Talking about serious stuff is hard and awkward and I feel like I’ve been doing it with literally everyone lately."
    r "Plus, I’ve apparently already got another talk lined up for later tonight and I feel like I’m going to be the one to have to get that one started."
    o "On the bright side...at least you’re getting pizza?"
    r "Yeah. That’s pretty much the only thing keeping me hanging on at this point, Otoha."

    scene otoharinoutside2
    with dissolve
    play music "samhain.mp3"

    o "Hah..."
    o "Being in a relationship is a lot of fucking work, isn’t it?"
    r "Yeah. But that’s exactly why I-"
    o "Shut up. You literally just told me to start and I’ve barely even said anything yet."
    r "My bad. The nerves are kicking in. "
    o "There shouldn’t be any nerves at this point, Rin. "
    r "There will always be nerves. I’m a nervous person. Especially around people as pretty and talented as you."

    scene otoharinoutside3
    with dissolve

    o "Think buttering me up will make me go any easier on you?"
    r "Think? No. Hope? Yes."
    o "Well, it won't."

    scene otoharinoutside4
    with dissolve

    o "Thankfully...I’m not mad. So there’s not really anything to “go easy” about."
    o "I’m just...confused. Your parents breaking up is such a huge...important thing to hide from me. And I thought I made it plenty clear in the past that I don’t want you keeping those things to yourself."
    r "You have. But you also made it clear that you want things to be easy and fun and-"
    o "Shut up. I’m still not done."
    r "Okay. But you might be better off just bringing a roll of duct tape with you whenever you leave the house from now on because I’m extremely bad at keeping quiet and might require some assistance. "

    scene otoharinoutside5
    with dissolve

    o "I didn’t realize you were into that sort of thing."
    r "I am into literally anything you want to do to me whenever you are ready to actually do things to me. Which might be never at this rate because I suck at this."
    o "You wanna know what you really suck at? Understanding me. "

    scene otoharinoutside6
    with dissolve

    r "Yeah...Yeah, that’s hard. "
    r "It’s not just you, either. I’m kind of like that with everyone."
    r "If I don’t see or hear something firsthand and just have to figure out whatever the issue is on my own, I’m basically screwed. Which is one of the big reasons I didn’t tell you about my parents."
    r "Everything happened so quickly and I panicked because I’ve been making them out to be the paragon of all things lesbian and if {i}they{/i} couldn’t last-"
    o "You didn’t think we would either."
    r "It’s more like I didn’t think {i}you{/i} would think we would last."
    o "I have no idea if we will or not. But it’s not like I’m in any rush to find out. I like taking things slow, remember?"
    r "It’s hard not to. And if that sounded insulting, it wasn’t supposed to be. We’re just really different people on the inside. "

    scene otoharinoutside7
    with dissolve

    r "Kind of ironic how the hardest part of dating a girl so far has been also just, you know, {i}being{/i} a girl."
    o "As much as I want to tell you you’re looking at it all wrong and that has nothing to do with how, uhh...bumpy things have been so far, I can’t. You’re exactly right."
    o "That’s on me, though. I’ve got like, zero exposure to this sort of thing and all I really know is that I like you and don’t mind having your tongue in my mouth a few times a day."
    o "But where you’re wrong is thinking whatever happens between your parents has anything to do with {i}us.{/i}"
    o "It’s not like hearing about them splitting up is going to make me think, “Oh. I guess all lesbians are doomed now. How sad.”"

    scene otoharinoutside8
    with dissolve

    r "See! Then this is just one more example of me not understanding something I’m supposed to understand because that’s exactly what I thought you’d think!"
    o "I might be inexperienced, but I’m not a fucking idiot."

    scene otoharinoutside9
    with dissolve

    r "Well, I am and I apologize. "
    r "It’s no secret that things are still a little weird with us and I just wanted to keep them as minimally weird as possible."
    r "But unfortunately, I am going to be further complicating our relationship by now being the only daughter of a fractured household who must go on an epic journey to pick up all of its pieces."
    o "I think you should maybe...leave the epic journey to the two of them. I doubt there’s much you can do to fix whatever problems may have led to this."
    r "I can’t fix {i}their{/i} relationship. I can’t fix {i}ours.{/i} What good even am I?"
    o "Do you actually think we need “fixing?”"

    scene otoharinoutside10
    with dissolve

    r "Do you?"
    o "Nah. Just a little...tuning."
    r "Music analogy. Because we’re in the light music club. And we play music. You’re so cool."
    o "That better not be sarcasm."
    r "It’s not. I really do think you’re the coolest person, like...ever. And I’m sorry that I have once again burdened your greatness by accidentally exposing it to the downfall of my parents."
    o "Oh, please. The downfall of your parents is the least of my worries when it comes to our relationship right now."

    scene otoharinoutside11
    with dissolve

    o "Wait, no. Forget I said that. That came out wrong."
    r "..."
    o "I...didn’t mean to make it sound like I’m worrying about something. I’m good. "
    r "It’s okay, Otoha. You can say it."
    r "Chances are I already know what it is anyway."

    scene otoharinoutside12
    with dissolve

    o "Then..."
    o "If you already know what it is...how come you haven’t said anything about it?"
    r "Because you’re wrong."

    scene otoharinoutside13
    with dissolve

    o "..."
    r "..."
    o "..."
    r "This is technically a new conversation, so I’m going to start this time if that’s okay with you."
    o "Good. Because I have no idea how I’d do it without sounding like a complete bitch."
    r "Can I start by asking you for a favor?"
    o "A little unorthodox for the beginning to a serious talk, but sure."
    r "Have more faith in me."
    r "There’s a big difference between keeping things from you because I’m an idiot who can’t figure out how you’ll react and literally just straight up cheating on you with a girl who doesn’t even like me."
    o "If she did like you, though...would that change anything?"
    r "No. Right now, you’re the only girl I have my eyes on. And it’ll stay that way for as long as we’re together."

    scene otoharinoutside14
    with dissolve

    o "Why...Why’d you even let her into the club in the first place? She doesn’t even play music."
    o "And you were so excited about it too. It’s almost like you {i}wanted{/i} her to join."
    r "Because I did."

    scene otoharinoutside15
    with dissolve

    o "You what?"
    r "I did want her to join. And I’m happy she’s a part of the club."
    o "But-"
    r "She’s my friend, Otoha. A friend I’ve had for years. So what if I had a crush on her for most of those? She turned me down and I’m with you now."
    r "I’m not going to just remove her from my life because of a thing that happened that never even went anywhere."
    o "Rin, don’t take this the wrong way...but you’re not exactly well known for always thinking things through."

    scene otoharinoutside16
    with dissolve

    r "That’s kind of hard to {i}not{/i} take the wrong way when it makes it sound like you don’t trust me."
    o "..."
    r "Is that what you’re saying?"
    o "I don’t know what I’m saying. I just...I see the way you look at her and I can’t help but get worried."
    r "Worried about what? That I’m just waiting for Chika to realize she was wrong and that she {i}does{/i} actually want to date me after all?"
    o "See, this is why I didn’t want to talk about it. I know how it sounds. But even if we’re dating now, we still barely even know each other."
    o "Why {i}wouldn’t{/i} you choose Chika over me if she actually {i}did{/i} change her mind about you?"

    scene otoharinoutside17
    with dissolve

    r "Ohhhhh...so that’s how it is."
    o "What?"
    r "It’s less that you don’t trust me...and more that you’re just jealous."
    r "You think Chika has something you don’t...and that I’m only dating {i}you{/i} because things didn’t work out with her."

    scene otoharinoutside18
    with dissolve

    o "That’s not...no. There’s still a lot of context you’re ignoring. Or...missing. Or something."
    r "Is there? Should I go back to being apprehensive? Or should I stay playful and fun so this conversation doesn’t take a turn for the worse?"

    scene otoharinoutside19
    with dissolve

    o "Huh?"
    r "Hearing you’re jealous makes me happy. It means you don’t want to lose me. Which is good, because I was half convinced you were kind of indifferent about that at this point."
    o "Of course not."
    r "So, what part are you {i}most{/i} jealous about? The fact that she has several years of a head start on you? Or the fact that she was the first girl I fell in love with?"

    scene otoharinoutside20
    with dissolve

    o "The {i}first{/i} girl you...fell in love with?"
    r "Should I...not have said the L word? Because I know it’s weird to use it when nothing ever happened, but I still think my feelings at the time were strong enough for me to-"
    o "No, no...I mean..."
    o "Wouldn’t saying {i}first{/i} imply that...I’m the second?"
    r "..."
    o "..."

    scene otoharinoutside21
    with dissolve

    r "...Noooooo?"
    o "Oh. Okay, yeah. Yeah, because now is still way too soon to start throwing big, serious words like that around."
    r "Yuuuuuuup."
    o "And, like...we’re still too young to really even understand what “love” is anyway. Right?"
    r "Yuuuuuu- "

    scene otoharinoutside22
    with dissolve

    r "Wait, no."
    o "No?"
    r "Yeah."
    o "...Yeah?"
    r "Yeah as in no. Like...I don’t agree with the thing you just said."
    r "What does it even mean when people say you can’t fall in love until you’re an adult? That makes literally zero sense."
    r "Do our feelings not count until we reach a certain age? At what point have we lived long enough to fall in love?"
    o "Uhh...I’m just...you know...repeating what I’ve heard before..."
    o "Did you...really feel that strongly about Chika, though?"

    scene otoharinoutside23
    with dissolve

    r "Uhhhh..."
    r "Will you get jealous again if I say yes?"
    o "Nuh-uh. Because that would imply that I want you to love me and...it would be, like...totally way too early for that sort of thing. You know?"
    r "..."
    o "..."
    o "Rin?"
    r "I did feel that way about her."
    r "I would have done anything."

    scene otoharinoutside24
    with dissolve

    r "But getting my heart broken was a good thing...because it wound up leading me to you."
    r "If I had never fallen in love with Chika, you and I never would have met. We wouldn’t be here right now trying to work out our problems."
    r "We wouldn’t be anything."
    r "You don’t have to be jealous...or worry...or anything like that, Otoha. I’ll be just as loyal to you as you are to me. I promise."
    r "Besides, Chika’s already sleeping with Sensei anyway, so she’d never even hook up with me in the-"

    scene otoharinoutside25
    with dissolve

    r "Mm!"
    o "Chika is {i}what?{/i}"

    scene otoharinoutside26
    with dissolve

    r "Nothing! I...I have no idea why I..."
    o "That was a joke, right? Like...there’s no way those two are actually..."

    scene otoharinoutside27
    with dissolve

    r "I never said that, okay? Erase the last thirty seconds from your memory. I have no idea how I even..."
    r "Neither of them can know, okay? They’re both really important to me and I don’t want anything happening that might change the way they-"
    o "Yeah...Yeah, okay. Yeah, I won’t say anything. Yeah."
    o "Should, like..."
    o "Should we...{i}tell{/i} someone, though?"
    r "Tell them what? What are you talking about?"
    o "That...our teacher is sleeping with a-"
    r "He’s not! {i}They’re{/i} not! Just..."

    scene otoharinoutside28
    with dissolve

    r "That...was just a fantasy of mine! Hahah! Silly, Rin! Always thinking about...people I know...having sex with each other..."
    o "..."
    r "..."

    scene otoharinoutside29
    with dissolve

    r "Otoha, please..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otoharinoutside30
    with dissolve2

    ri "So, yeah. That’s basically how you do it."
    sa "So...cool!"
    ri "Me? Nah. I’m embarrassing and worthless. I couldn’t even tie my tie this morning, so I had to leave it at home."
    ri "But you? You’ve got a tie on right now. We are not the same."
    c "What do you think they’re talking about out there?"

    scene otoharinoutside31
    with fade

    ri "Hm?"
    c "Rin and Otoha. Rin looks really...panicky for some reason."
    ri "Yeah, she does that."
    c "I hope they’re not breaking up. I like those two together."
    ri "If they are, this is probably the best possible time since the two of us could cry together about it. But yeah, I hope they’re not either. Even though I have only known Otoha for half an hour."
    c "Well, whatever it is, I hope it turns out okay. Rin’s been through enough as-is and I really hate seeing her like that."
    ri "Wow. No wonder she liked you for like a billion years. You’re sweet."

    scene otoharinoutside32
    with dissolve

    c "Hah..."
    c "She’s just..."
    c "She’s really unlucky."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene noonsky
    with dissolve2

    "I wound up staying in my office with Noriko for at least another hour."
    "By the time we left, everyone else had already vacated the school."
    "Everyone except Rin and Otoha, that is."
    "But as I walked past them on the way out, neither of them made eye contact with me."
    "Thankfully, I had Noriko to distract me from their inattentiveness and keep me occupied the rest of the way home."
    "Once we part ways, though...I can’t help but dredge it up again-"
    "The image of two young girls, just inches apart on a bench-"
    "The mild red hues taking residence in their cheeks-"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "And the slew of inappropriate things I think that could mean."

    $ renpy.end_replay()
    $ rinspecial55 = True

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label rinspring1:
    scene sky
    with dissolve2

    "It isn’t long until Ami starts blowing up my phone, because scissor angel forbid that I take a moment to myself in order to get my head straight."
    "But, now that my neck is broken and I can no longer look from side to side, it’s about time that I head out."
    "I’m not sure when the next time I’ll be coming back here is. But one thing I {i}do{/i} know is that my presence will cause nothing but problems for everyone now. "
    "I know they’ll understand. And I know they’ll likely be hurt when I don’t wind up calling them, but how {i}could{/i} I when my hands shake every time I pick up my phone?"
    "Her number is still in there. And I know that Ami would happily delete it if I asked her to, but I can’t bring myself to {i}do{/i} that because it’s the only thing I have left."
    "I wonder who would answer if I were to call that number now. But I don’t wonder for long as I find more comfort pretending it would be the dulcet sound of an infinite dial tone."
    "I want to grind this machine to pieces and swallow them like capsules so that I may consume and sacrifice everyone I know all at once."
    "Perhaps that’s what’s needed to carry on without destroying someone else. "
    "All other sacrificial means just seem far too exhausting now."

    s "..."

    "I make my way through the courtyard."

    r "Ah! There!"

    "But I encounter a barbed tripwire that severs my feet from my body before hoisting me up into a cypress tree where I will be ultimately consumed by a plethora of hungry insects."

    play sound "static.mp3"
    scene rinandthegang1 with flash
    stop sound
    play music "fallishere.mp3"

    mo "See? You all doubted my abilities to predict his actions, but I have played far too many otome games to not know where to find my favorite characters by now."
    s "Oh. It’s you guys. "
    s "Shouldn’t you be in class?"
    f "We...we all decided to leave. And Miss Imai wasn’t opposed considering today’s...um...{i}circumstances.{/i}"
    s "Rin and Molly I’d expect this from. But not you, Futaba. You’re not the type to cut class. Get back in there and...learn things. Or whatever."

    scene rinandthegang2
    with dissolve

    r "What do you mean you’d expect that from me?! When have I ever cut class before?!"
    mo "‘Tis true that I have been known to skip school in favor of new releases from time to time. Mental health is important after all."
    sa "Which...is a good thing to bring up after...everything we just heard from you in there..."
    s "Ah, yes. "
    s "Yeah, I’m not doing so great right now. But it’s nothing you need to concern yourself with."
    r "Uhh...it kind of {i}is,{/i} dude. This isn’t a thing we can just shrug off. Especially not with Ami on the verge of going fucking postal. I could have sworn Chika was about to slit her throat."
    s "She did. I just finished cleaning up the blood. So, if you’ll please excuse me, I’ll be going home to take a shower now."

    scene rinandthegang3
    with dissolve

    f "Sensei, please don’t make jokes about this. We’re all really worried about you. And we get that you need some time off to handle things, but-"
    r "But we’re not really sure if that time should be with {i}Ami.{/i}"
    mo "You’re more than welcome to come stay with me, Sir. The Kendo Princess and I can share a bed while we wait out the duration of your debuffs."
    sa "You can...stay with me too...if you want...but...yeah...Ami is..."
    sa "She seems kind of...not {i}safe{/i} right now..."
    s "Yeah, that’s exactly the issue. She’s going fucking insane and I’m literally the only person in the world who can do anything about it. And I owe her that much after she just looked after me for so long."

    scene rinandthegang4
    with dissolve

    r "Well...what about Ayane? She’s known Ami long enough to be able to help with stuff like this, hasn’t she?"
    r "There’s also-"
    s "There’s no one else. It has to be me. "
    s "And, to be honest, I probably should have noticed this coming and got her help a long time ago. But that would have required me actually {i}helping{/i} in some way, so of course I didn’t."

    scene rinandthegang5
    with dissolve

    r "Now, hold the fuck up before you start going on some annoying rant about how “useless” you think you are. Because you’ve helped me with so much of my shit that I’ve legitimately lost track of it all."
    mo "Me as well, Sir. Even if we’ve had our fair share of issues."
    sa "People say I’ve been...talking more lately and...I think all of that is thanks to you, Sensei..."

    scene rinandthegang6
    with dissolve

    f "And I’ve talked about this subject so many times that I feel like I shouldn’t even bother you with it anymore..."
    s "Thanks, guys. I feel a lot better knowing that I’ve made positive impacts on all of you while ignoring the one girl who’s been under my nose this entire time."
    r "You’re welcome!"
    sa "I think...that was sarcasm, Rin..."
    r "Then you’re {i}not{/i} welcome! And you’re also obligated to come hang out with us right now so we can take {i}our{/i} turn to try and make you feel better! {i}Without{/i} locking you in your room!"
    mo "While I may not entirely agree that time outside of one’s room is necessary to replenish one’s mana, I do believe Nithhala may be correct in recommending such a thing this time, Sir."
    f "It might be a little selfish of us, but...we have a lot we’ve been wanting to talk to you about."
    r "And you haven’t even commented on how awesome my new hair looks yet!"
    s "Cool hair, Rin."

    scene rinandthegang7
    with dissolve

    r "Why thank you, Sensei. What a nice thing of you to say completely unprovoked."
    sa "You can...wait a little longer before...going back home, can’t you?..."
    sa "We’ve...already left school, so...it’s not like we have anything else to do now...and...there’s some stuff I want to talk to you about too...so..."
    s "And none of this can wait the indeterminate amount of time it will take for me to leave my house again?"
    r "We inch closer to death every minute. And so we must savor the few opportunities we have to bond with one another!"

    scene rinandthegang8
    with dissolve

    r "Because you never know when the person you love is going to leave you and you don’t want to regret not saying certain things that you probably wish you would have said."
    f "Subtle."
    s "Right...you and Otoha broke up. How are you holding up?"

    scene rinandthegang9
    with dissolve

    r "I kissed Sana. "
    sa "Hahah......hah....."
    s "I feel like the old me would have said something like, “I wish I was there to see it.”"
    f "Then...what would the new one say?"
    s "I want to fucking die."
    r "Maybe we should invite Miss Watabe too then? You guys have that in common. Maybe she can help?"
    s "I think she’s mad at me right now. And again, I’m not hanging out with you guys."
    r "Sure you are. You can shower and get Ami’s blood off of you later. It’s only fair that you come with us now since we were the ones to find you."
    f "We kind of...branched off into teams and...chose different areas outside of the school to wait for you in."
    mo "They all doubted me when I suggested the side entrance. But if there’s anything I know about Irish goodbyes, it’s that the back is far more conspicuous from the front. Not a sex joke."
    s "It would have been a terrible one if it was. "

    scene rinandthegang10
    with dissolve

    mo "I may be a comedic relief character, but I’ve never claimed to be funny, Sir."
    sa "You’ll...come with us right?...Just...for a little while?..."
    s "Ami’s called me a million times, Sana. She needs me."
    sa "Well...have you answered any of those calls yet?"
    s "..."
    sa "Then...if you haven’t...doesn’t that mean you...{i}don’t{/i} want to see her?..."
    r "Just say your phone died! Then we can all go hang out at the cafe for an hour or two and Ami won’t be able to get mad because...you can’t control electricity?"
    s "..."

    scene rinandthegang11
    with dissolve

    r "Pweeeeeeeeease?"
    s "Rin-"

    scene rinandthegang12
    with dissolve

    sa "Pweeeeeeeeeease?......"
    r "God, you’re good at that."
    mo "Oh, he’s done for now. There’s no denying that face."
    s "Sana..."
    sa "Pwetty pweeeeeeease?...We wub you..."
    s "What has happened to you in the two months I’ve been gone?"

    scene rinandthegang13
    with dissolve

    sa "A lot."
    r "God damn it. My nose is bleeding again, isn’t it?"

    scene rinandthegang14
    with dissolve

    f "It appears that our only course of action now is to take Rin to the cafe so we can fix her nosebleed."
    r "Don’t let me die, Dad. I’m too young to leave this world."
    s "..."
    sa "..."
    mo "..."
    s "Fine."

    scene rinandthegang15
    with dissolve

    r "LET’S FUCKING GOOOOOOOOO!"
    mo "An excellent choice, Sir!"

    scene black
    with dissolve2

    mo "To the zeppelin! Thunder Bluff awaits!"
    f "How about we walk instead? It’ll be faster."
    mo "Aspect of the pack, on! Go, go, go, go, go!"

    "Molly is the only one who takes off running, leaving the rest of us to follow behind her at a speed much more suited to my current status as an unmotivated sack of shit."
    "I don’t want to do this."
    "But..."
    "I don’t want to see Ami right now either."
    "..."
    "I just want to sleep."

    scene rinandthegang16
    with dissolve2

    "But a liquid barrier between that one goal and me is placed on the table just inches from my trembling hands and I realize just how far away sleep is."
    "And while I want to approach this meeting just as I’d approach a dream-"

    play sound "static.mp3"
    scene rinandthegang17 with flash
    stop sound

    "In my dreams, there’s someone else."

    play sound "static.mp3"
    scene rinandthegang16 with flash
    stop sound

    r "Hey...you good? Still with us?"
    s "Huh? "
    s "Oh. Yeah. Sorry. Mind just wandered a bit."
    sa "When that...happens to you...what’s it like?"
    s "What do you mean?"
    sa "Like...you kind of, like...black out sometimes...don’t you? Are you...seeing anything when that happens?...Or is kind of like...everything just...you know...stops or something?"
    s "A little of both, actually. I think. But I rarely ever remember anything I see once I’m brought back to reality."
    f "That’s unfortunate. Not remembering means you can’t even channel those visions into something creative. And I’ve heard that helps a great deal when it comes to battling stress."
    s "Yeah, I think this is a little worse than just “stress.”"
    mo "Sounds like an interesting power to me, Sir. Almost like time-hopping. You get to slip through the cracks in reality without remembering any of the terrible things you see within them."
    r "I get what you’re saying, though. When my depression kicks in, it’s often like I’m blocking out entire days or...weeks as a whole."
    r "Everything just kind of stops. And it doesn’t pick back up until something pulls me out of it. It just sucks extra hard because the only thing that really {i}can{/i} pull me out of it is time."
    r "So it’s like getting caught in some mini paradox where you need to rely on time to heal, but you have no idea how much time is actually passing because you’ve lost all touch with it. You know what I’m saying?"
    s "Almost too well."

    scene rinandthegang18
    with dissolve

    r "Really? Because I feel like that explanation barely scratched the surface of how it actually {i}feels.{/i} But I get that our situations are different."
    s "Yeah. I’m sure you have no shortage of issues yourself right now, though. And I’m sorry I wasn’t around to help you with your breakup situation."

    scene rinandthegang19
    with dissolve

    r "Don’t be. I have Futaba to help with that stuff."
    f "All things considered, Rin handled herself surprisingly well after the first few days. She’s just...still a little bitter. But I’m sure that will go away in time."
    r "Probably not, to be honest. I’ve heard that most people never get over the unwelcome shattering of their first love."
    s "Just kiss Sana a few more times and I’m sure it’ll start to go away."

    scene rinandthegang20
    with dissolve

    r "Weirdly enough, that didn’t do as much for me as I thought it would. So either I’ve ruled out being an exhibitionist, or I just see Sana as more of a friend than sex practice. "
    sa "Thanks, Rin...I appreciate that."
    r "Yeah, don’t mention it. I just figured it would have been a little more exciting for me considering how many times I’ve fantasized about- I’m going to shut up now."
    mo "At least you {i}got{/i} to kiss somebody. Miss Imai rejected me even harder than you did."
    r "Well hey, at least you didn’t force yourself on her. Just look at how much you’ve grown in such a short amount of time."

    scene rinandthegang21
    with dissolve

    mo "As it turns out, you receive quite the XP boost after having your heart broken. So at least you have leveling up to look forward to now, Rin. "
    mo "May your next kiss with a classmate be one that you remember for the rest of your overwhelmingly lesbian life."
    r "And may yours be consensual."

    scene rinandthegang22
    with dissolve

    f "Apart from the breakup and the Christmas party, there isn’t much you’ve missed. Well, other than Miss Imai slowly descending into madness. But we were all kind of doing that, so..."
    sa "Yeah...she’s made it pretty obvious...just how much she likes you lately..."
    f "And she had the...great misfortune of drawing your name for Secret Santa. So I’m sure she’s pretty upset that she wasn’t able to give you anything on account of your...yeah."
    s "You guys still put me on the list despite me being completely MIA for two months?"

    scene rinandthegang23
    with dissolve

    r "Heck yeah, we did. We believed in you the whole time, Sensei. "
    r "We knew you’d be back eventually. The tough part was just waiting out your absence since we’re all {i}way{/i} more dependent on you than we thought!"
    s "Everyone else, maybe. But you seemed to fare pretty well on your own for the...complete duration of your relationship."

    scene rinandthegang24
    with dissolve

    r "But deep down, my heart was screaming, “Sensei! Sensei!”"
    s "Cute. But it doesn’t mean much when your actual voice is screaming someone else’s name."

    scene rinandthegang25
    with dissolve

    r "I will not sit here and be blamed for the specific words that escape my mouth at the peak of this very hormonal time in my life. "
    r "But I {i}will{/i} sit here and inform you that that time is over and that we can now go back to being the best homies who ever homied because I suddenly have way more free time on my hands."
    s "And I suddenly have almost none."
    r "What do you mean you have none? You’re taking a hiatus from school. That should mean you have plenty of extra time on your hands now. "
    r "Unless you’re joining a men’s softball league or something."
    s "Why would...what?"
    r "I don’t know. It’s just the first thing my mind went to in my seemingly endless mental battle to not think about Otoha."
    s "I’m...not joining a softball league. I just can’t imagine being in the mood to do {i}anything{/i} in the near future as just moving my body is a chore right now."
    r "Damn. I guess softball really is out of the question then, huh?"
    sa "I don’t think it’s...a problem if you stay at home, Sensei..."

    scene rinandthegang26
    with dissolve

    sa "I’d just...like to be able to visit you every now and then..."
    f "All of us would. But, given Ami’s current...{i}condition,{/i} maybe it would be best to wait a little while before introducing the idea to her?"
    mo "I’ve got plenty of new games for you to not be interested in, Sir. I’d love to come share them with you."
    s "Again, thank you guys. "

    scene black
    with dissolve2
    stop music fadeout 12.0

    s "But I’ve got bigger fish to add to my hot pot right now."
    f "That’s...That’s not how that phrase normally goes, is it?"
    r "Ooooh hot pot sounds good. Let’s have a hot pot party soon. This place called FoodCo. just opened that-"

    "The rest of our outing carries on normally."
    "My phone continues to burn holes in my pocket."

    $ renpy.end_replay()
    $ rinspring1 = True
    $ rin_love += 10
    $ molly_love += 10
    $ sana_love += 10
    $ futaba_love += 10

    "{i}Rin’s affection has increased by 10!{/i}"
    "{i}Molly’s affection has increased by 10!{/i}"
    "{i}Futaba’s affection has increased by 10!{/i}"
    "{i}Sana’s affection has increased by 10!{/i}"
    "........."
    "......"
    "..."

    jump sanaspring1

label rinspring2:
    stop music
    play sound "static.mp3"
    scene rinsara1 with flash
    stop sound
    play music "cafe.mp3"

    "And our segment focusing on Rin Rokuhara begins."

    r "Yo!"

    "Rin Rokuhara, locally renowned bisexual, had been feeling rather conflicted lately. But I’m less inclined to compare her to an elder beast foraging for berries and {i}more{/i} inclined to just {i}compare{/i} her."
    "She wasn’t as [[successfully] outgoing as Chika Chosokabe. Nor did she possess the unabashed kindness demonstrated on a routine basis by her roommate Futaba Fukuyama."
    "But she {i}did{/i} have something that set her apart from both of them."
    "A cool, skull-shaped hairpin that she bought from a discount store at the mall that she has decorated her many different hairstyles with ever since."
    "It wasn’t perfect. And she wished there could be something a little more impressive about her when compared to everyone else, but she was fine with being mostly unremarkable."
    "She was {i}fine{/i} with taking the backseat, as evidenced quite literally by her claiming the stereotypical “protagonist’s chair” in the back corner of the classroom on the first day of school."
    "If she was going to be ordinary, she would be the most spectacular ordinary person she could be. "
    "Only in short bursts, though, as it didn’t take long as the center of attention for her to start crumbling."
    "And to revisit what I mentioned just moments ago about her currently being {i}conflicted,{/i} conflict as a whole was the whole idea conflicting her. Do you follow?"
    "No? Then allow to me put it in plainer terms."
    "Rin Rokuhara didn’t like what she was currently feeling. And that really pissed her off because it wasn’t every day she got to feel anything at all."
    "She was bitter, but not {i}too{/i} bitter about the break-up. She didn’t mind that the collective mindset of her class was rapidly deteriorating. She just wanted to stop being jealous."
    "Because if {i}she{/i} began to want what everyone else wanted, it would only make things harder. And she was finally in a good spot."
    "But as she stepped into the cafe, she subconsciously scanned the room for someone she knew would not be there."
    "And {i}this{/i} is why she was feeling conflicted."
    "Because it meant what she didn’t want it to mean."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene rinsara2
    with dissolve2

    h "Yeah. Is that okay?"
    h "You know where the keys are, right?"
    r "Sorry to interrupt your call, but I need to-"
    h "Rin, hold on. Sorry, can you say that again? "

    scene rinsara3
    with dissolve

    h "No, they’re next to the stove in a wicker basket."
    r "..."
    h "{i}Wicker.{/i} It's that weird...straw stuff. How do you not know what wicker is? "

    scene rinsara4
    with dissolve

    h "Just look in the basket. You {i}do{/i} remember how to drive, right?"
    r "..."
    h "If you are lying to me right now-"
    r "..."
    h "Yeah. Next Sunday. Got it."

    scene rinsara5
    with dissolve

    h "I’m sending one of my girls to help you right now. "
    r "You’re doing what?"
    h "Can you pick her up here? Or-"
    h "What? Why not?"
    r "Hellooo? Haruka? Your employee of the month would like to clock in now."
    h "Fine. Whatever. Just...hold on. I have to tell Rin."

    scene rinsara6
    with dissolve

    h "Rin, I need your help with something."
    r "Is that something...making coffee? Because my skill-set is pretty limited and that’s all I get paid to do."
    h "No. One of our brewers stopped working and I need you to go with a friend of mine to pick a new one up. And don’t forget to get a receipt or it’s coming out of your paycheck."

    scene rinsara7
    with dissolve

    r "What? Me? Why me? Why can’t your friend just do it if she’s already going?"
    h "Because I don’t trust her to get the right one and you can’t drive yet."

    scene rinsara8
    with dissolve

    h "Hm? Oh, no. You heard that correctly. I said I didn’t trust you."
    r "{i}Hah...{/i}"
    h "Obviously because I don’t trust you. But yeah. I’m sending her now. Just make sure to tell me where you’re picking her up since you refuse to come here for some reason."
    r "..."
    h "Got it. Thanks. Bye."

    play sound "phonebeep.wav"
    scene rinsara9 with dissolve

    h "Okay. Sorry. Crazy night. Let me write down the model number and-"

    scene rinsara10
    with dissolve

    h "What’s wrong? Why do you look so sad? Shouldn’t you be excited to get out of work? We’re slammed tonight."
    r "Hell yeah we are, which means it’s the best time to show you what I’m made of. How am I supposed to fight for a promotion if I’m spending my time {i}away{/i} from the store? Just have Molly do it."
    h "Molly called out. Something about a...{i}Pal-{/i}world? Do you know what that is? Some kind of convention?"

    scene rinsara11
    with dissolve

    r "Oh, that fucking bitch."
    h "Whatever the case, do this and you can have the promotion. Nobody else is qualified anyway. "

    scene rinsara12
    with dissolve

    r "Wait, really?!"
    h "Yeah. I’ll start training you on paperwork later tonight. "
    r "And, just to clarify, this promotion includes a raise, right?"
    h "Obviously. I just have to run some numbers and-"

    scene rinsara13
    with dissolve

    h "Wait, we’ll talk about this later. I need you out of here {i}now.{/i}"
    r "Got it! I still don’t know where I’m going, though."
    h "Neither do I. Just pick a direction and...run that way while I follow up with my friend. Worse comes to worst, you have to turn around."
    r "Choose a direction and run! Got it!"

    scene black
    with dissolve2
    stop music fadeout 15.0

    h "Wait! Leave your bag here. It’ll weigh you down."
    r "Roger!"

    "And so Rin Rokuhara takes off in an undisclosed and random direction..."

    scene nightsky
    with dissolve2

    "Which, of course, winds up being the {i}wrong{/i} direction. And she then has to turn around after two minutes of sprinting."
    "Twenty minutes go by...and the brisk air of a spring night enters her lungs as she breathes a shallow sigh of relief at the prospect of being able to inhale without burning up from the inside out."
    "She was glad summer had reached its end. And she was glad that she could take this season as an opportunity to start over."

    scene rinsara14
    with dissolve2

    r "Hah...hah...hah..."

    play music "justlights.mp3"

    "“But where do I start {i}from?”{/i} she wondered, sweat trickling down her chest as the night air fought to cool her down."
    "“What are my goals? What do I {i}want?{/i}”"
    "The promotion was already a lock unless Haruka changed her mind. So Rin needed to come up with something else or face the fact that, for the first time in her life, she’d have nothing to chase after."

    scene rinsara15
    with dissolve

    "Nothing attainable at least. But it wasn’t all that long ago that she wholeheartedly believed finding a girlfriend was a feat so far out of reach that words like “plausible” would make her laugh."
    "She avoided making eye contact with the stars as she worried it would motivate her to shoot for them."
    "And as a distant voice approached from beyond the darkness, she decided it would be best to keep these thoughts buried in the back of her head for now."
    "Just...she worried that she wouldn’t be able to force them back as far as they’d been before."
    "For they had always been there, but they’d never been this violent. And they’d never been this desperate."
    "Her eyes scan her surroundings once more, but it’s hopeless."

    q "Oh! Okay, I see her. I think. Maybe? "

    scene rinsara16
    with dissolve

    q "Did she bleach her hair? I don’t remember- actually. Hold on. I’ll just ask."

    scene rinsara17
    with dissolve

    sar "Hi! Rin, right?"
    r "Sana’s...mom?"

    scene rinsara18
    with dissolve

    sar "Yup! The eagle has landed, Haru-chan. I will now be hanging up the telephone. "
    sar "And thanks again for letting me borrow your car! A thing I totally did!"
    sar "Nope! Sorry! Going through a tunnel! In your car! Bye!"

    play sound "phonebeep.wav"
    scene rinsara19
    with dissolve

    sar "Whoops. I accidentally hung up."

    scene rinsara20
    with dissolve

    sar "Hi! You can call me Sara, not “Sana’s mom.”"
    r "Heeey. And...you can call me Rin. Because...that is my name. My name is Rin."

    scene rinsara21
    with dissolve

    sar "It sure is."
    r "..."
    sar "..."
    sar "Well, this is awkward. "
    sar "I don’t normally hang out with my daughter’s friends. And whenever I do, my daughter is typically...you know...present."
    r "Y-Yeah...But...we’re not technically {i}hanging out.{/i} This is a business thing. We’ve gotta...go...touch a machine. With our hands."
    sar "Yeah, about that."
    sar "No we don’t."

    scene rinsara22
    with dissolve

    r "I’m sorry, what?"
    sar "Haru-chan said some guy in a purple hat fixed the machine for her, so we don’t need to go and buy a new one now."
    r "So...we came all the way here for nothing?"

    scene rinsara23
    with dissolve

    sar "Hey, at least you ran! I had to take a taxi here and now I’m out like 4,000 yen."
    r "Taxi? I thought Haruka was letting you borrow her car?"
    sar "She was! But she’s also under the impression that I know how to drive when I’ve only been behind the wheel of a car a few times in my life and they’ve all been absolutely terrifying."

    scene rinsara24
    with dissolve

    r "Why didn’t you just tell her that? She would have called us both a taxi if she knew."
    sar "Because now she thinks I’m cooler since I know how to drive. "
    r "But you don’t know how to-"

    scene rinsara25
    with dissolve

    sar "Shhhh...that will be our little secret."
    r "Well...does this mean I have to run all the way back to the cafe? Because I don’t have enough money on me to pay for a taxi and I’m not going to make my friend’s mom buy me one."

    scene rinsara26
    with dissolve

    sar "But what if I buy {i}myself{/i} a taxi over to Koi Cafe and you just happen to...also get inside of it? That would work, right?"
    r "But if we show up in a taxi, Haruka will know that-"
    sar "So we have them stop a block away! You need to learn to start thinking outside of the box if you’re ever going to convince people you’re cooler than you actually are, Rin. Take it from me."

    scene rinsara27
    with dissolve

    r "No, I get it. I keep a skateboard in my dorm and I don’t even know how to ollie."
    sar "And I don’t even know what an ollie is so we’re already on the same page!"

    scene rinsara28
    with dissolve

    r "We’re the same height too and it’s kind of making me uncomfortable. "
    sar "But it’s making {i}me{/i} feel young and that’s all that really matters."
    r "So...I guess we just...go back now? And this whole trip was pointless? And I lose my promotion because Haruka sees it as a loophole and realizes I accomplished nothing tonight?"

    scene rinsara29
    with dissolve

    sar "Oh, stop. Haru-chan wouldn’t do something like that to you. I’ve heard her talk about you plenty of times before and I can assure you that basically all of it has been good."
    r "{i}Basically{/i} all of it?"
    sar "She’s mentioned that you can get a little distracted when cute girls show up but, let’s face it, don’t we {i}all?{/i}"
    r "To be completely honest, it’s taking everything I have to even form complete sentences in front of you right now. "
    sar "Because I’m young and beautiful, right? Say it. Tell me I’m young and beautiful."
    r "I’m not sure I can do that without getting a nosebleed."

    scene black
    with dissolve2

    sar "Booooooo. This way!"
    r "Wait! Sana’s mom!"
    sar "{i}Sara!{/i}"
    r "S-Sara! Where are you going?! I thought we were calling a taxi?"
    sar "It’ll be faster from the park! Trust me! I’ve been pretending to be cool longer than you’ve been alive!"

    "And so two unlikely girls, forced together by the swift hands of a woman with massive breasts, make their way to a nearby park."

    play sound "static.mp3"
    scene rinsara30 with flash
    stop sound

    "It is a park where strange things have occurred on several occasions before. And, believe it or not, these two bear a special connection to the girl those strange things have revolved around."
    "As they sit on a bench and wait for a taxi to arrive, the pressure begins to mount. They know they’re supposed to be talking right now. But what are they supposed to talk {i}about?{/i}"
    "And why is it so difficult when they have so much in common? "
    "Neither one can ollie. Neither one can drive. Even the fantasies that enshroud their minds when they touch themselves are similar. "
    "It wouldn’t be right to talk about those, though. Not during their first meeting on this bench at least. Something like that would have to wait until the third or fourth or fifth time."

    sar "Do I make you uncomfortable, Rin?"

    "One of them was used to breaking awkward silences like this. But despite how many times she’d done it before, she had never gotten {i}good{/i} at it."

    scene rinsara31
    with dissolve

    r "Huh? Not really. Why?"

    "Regardless of that, though, she tried."

    sar "Just wanted to make sure. I’ve been told I can come off a little strong before. And I can imagine it’s already kind of weird to be chatting with your friend’s mom in the first place."
    r "It’s not {i}that{/i} weird. I have like, twice the amount of experience when it comes to talking to moms that most people do. I’d be way more uncomfortable if you were Sana’s dad."

    scene rinsara32
    with dissolve

    sar "Well, that’s reassuring to hear. Because I was about your age when I first met him and I was definitely {i}not{/i} uncomfortable despite the...admittedly massive age gap."
    r "He was older than you? By how much?"

    scene rinsara33
    with dissolve

    sar "A lot. He was my teacher. But I was pretty attention-starved back then, so that didn’t really matter to me."
    r "Your teacher? Really?"
    sar "Mhm. I was a freshman in high school. Just like you now."
    r "Do you...do you regret it? Looking back on it now?"
    sar "Why would I regret it? I got the world’s most adorable little girl out of the deal, so I think it’s pretty safe to say I came out on top. Even {i}if{/i} I had to raise her on my own."

    scene rinsara34
    with dissolve

    r "Was it hard?"
    sar "Oh god, yeah. I still have no idea how I managed. But Sana turned out perfectly, so I guess I didn’t make {i}too{/i} many mistakes. "
    sar "Let’s not talk about {i}me,{/i} though. My story’s long and confusing, and I want to know more about you. Sana doesn’t really open up much when it comes to her friends."
    sar "Ayane’s really the only one I know anything about. And even that’s mostly surface level stuff."

    scene rinsara35
    with dissolve

    r "I don’t mind opening up. You seem like a good person. I’m just-"
    sar "Not sure what you can tell me since it’s the first time we’ve really talked and you don’t fully trust that it’ll stay between us?"
    r "Something...like that."
    sar "I’m sure I’d have said the same thing in your shoes. My experience with adults when I was younger wasn’t exactly great."
    r "It’s not that I have bad experiences with adults or anything. There’s just...a lot of stuff I know that could mess up basically {i}everything{/i} if it gets out."
    r "And it’s gotten to the point where I have to think like, five times more carefully about every single thing I say so nothing is ruined."
    r "I’m going to have to start keeping a notebook soon. I can barely remember who knows what at this point. Like, half the class probably doesn’t even know I kissed Sana yet."

    scene rinsara36
    with dissolve

    sar "You what?"
    r "See?! Fuck! I didn’t last five seconds! There’s no room in my stupid brain for any more secrets! This is getting too hard!"
    sar "You...kissed Sana?"

    scene rinsara37
    with dissolve

    r "No."
    r "That was a lie."
    sar "Why are you lying about lying?"
    r "I have no idea what you’re talking about. Anyway, time to move on."
    sar "Are you two...dating?"

    scene rinsara38
    with dissolve

    r "What?! No no no no no! It’s nothing like that! In fact, it’s nothing at all! But if it was {i}anything{/i} at all, which it’s not, it would have just been...like...a Christmas party thing."

    scene rinsara39
    with dissolve

    sar "Huh."
    r "Uhh...{i}please{/i} don’t mention this to her. I don’t want her to think I...blabbed about anything else."
    sar "I won’t mention anything, don’t worry. I’m just not really sure how I feel about...finding this out from {i}you{/i} instead of her. "
    sar "I’m not sure what I was expecting, though. It’s not like she ever opens up about anything in the first place."
    sar "I swear, between her and Sensei it’s like I’m constantly trying to pry open a locked diary. So hearing you accidentally confess things like that is a breath of fresh air, weirdly enough."
    r "You’re...close with Sensei too?"

    scene rinsara40
    with dissolve

    sar "I like to think so...but I can’t help but question it at times. Especially lately."
    r "We’ve got that in common, then. It’s kind of embarrassing to say this, but...Sensei’s kind of, like...tied for the role of my best friend. "
    r "Like, he knows things about me that even my roommate doesn’t and I’ve been with her since middle school."
    sar "Does {i}he{/i} know you kissed my daughter? Because I can’t fault you for keeping it a secret, but I can sure as heck blame him."
    r "I’m just going to do that thing where I laugh and avoid the question. Hahaha. Ha."
    sar "You’re funny. I can see why my daughter kissed you."
    r "Okay, we can stop bringing that up now."
    sar "Do you like her? Be honest."

    scene rinsara41
    with dissolve

    r "Sana? No! It’s...It’s nothing against her. Like, she’s a great friend and an awesome girl. But I don’t think the two of us..."
    r "I don’t really feel that way about her. She was just one of many casualties in this year’s game of spin the bottle."
    sar "Darn. And here I was hoping for a second daughter. "

    scene rinsara40
    with dissolve

    r "Sorry to disappoint you. I don’t think either of my moms would be happy if I abandoned them for you, though."
    sar "Hey, you’ve already got two. What’s one more?"
    r "Good point. Plus, it’d be four counting my bio-mom. And five if we want to throw Haruka into the mix as my work mom. How many more do you think I need before setting some kind of record?"
    sar "So you’re the...adopted child of two women? I was wondering what you meant by that “double the experience with moms” thing. "
    r "You could’ve just asked, you know. It’s not really a thing I hide. I love my parents."
    sar "Not everyone does, though. And that can be a touchy subject for a lot of people. {i}Especially{/i} people you barely know."

    scene rinsara42
    with dissolve

    r "Good point. But even the touchy stuff like my biological parents doesn’t really get to me the way most people expect it to."
    sar "Then, do you mind if I just come out and blatantly ask what could possibly compel a couple to give up someone as cute as you?"
    r "Beats me. My skull was still all soft and weird back then."
    r "All I know is that my bio-mom was clinically insane and my dad...is a human being who exists. Or {i}existed.{/i} He’s the biggest question mark in my life, to be completely honest."

    scene rinsara43
    with dissolve

    sar "Probably just another jerk like Sana’s dad — some guy who runs off before he ever has the chance to realize how wonderful his daughter is."
    r "Probably. No use in turning over any stones to find out, though. Not when I have a trillion other issues that need addressing first."

    scene rinsara44
    with dissolve

    sar "Well, hey..."
    sar "If your three other good moms are ever busy and you’re in need of a fourth one to accidentally spill more of your secrets to..."
    sar "You know where my bar is. "
    sar "Only if you’re comfortable with it, though. I get that we might be moving a little quickly right now. I’m just a little weak when it comes to Sana and her friends."
    sar "Especially friends that might turn into {i}more than friends{/i} if they keep kissing at Christmas parties."

    scene rinsara45
    with dissolve

    r "Okay. I would like the taxi to arrive now."
    sar "Hahahahaha!"

    scene black
    with dissolve2

    "The night is far from over as Rin and Sara wait for their car to arrive."

    stop music
    play sound "static.mp3"
    scene bedroom_night with flash
    stop sound

    "But that doesn’t stop someone miles away from putting an end to it early."

    s "I hope tomorrow is better than today."

    scene black
    play sound "tackle.mp3"

    "He collapses into the bed."
    "He accepts that it won’t be."
    "{i}Rin and Sara are now friends!{/i}"

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ rinspring2 = True

    if day == 1:
        jump advancetotuesch4
    if day == 2:
        jump advancetowedch4
    if day == 3:
        jump advancetothursch4
    if day == 4:
        jump advancetofrich4
    if day == 5:
        jump advancetosatch4
    if day == 6:
        jump advancetosunch4
    if day == 7:
        jump advancetomonch4

label rinspring3:
    scene sky
    with dissolve2

    "You know — the one I’m {i}not{/i} having sex with."
    "And while I {i}do{/i} patiently await the day that changes, now probably isn’t a good time to see if she wants to head back to her room and permanently modify our relationship."
    "I say, knowing full well that I’ve been more hesitant with her than I am with most. "
    "But in a sense, Rin is kind of like the daughter I had before actually having a daughter. If you ignore the sexual tension at least."
    "What I mean is that if we were anywhere closer to the same age, I wouldn’t hesitate to have called her a best friend in the beginning."
    "Now...not so much."
    "And we both know that. And that’s fine."
    "But the lingering memory of that connection still...well, you know, {i}lingers.{/i} And I feel it most when we’re alone."

    scene rinsenseiwalking1
    with dissolve2
    play music "samhain.mp3"

    "That just doesn’t happen as much as it used to."

    r "The cafe? Really? You seriously thought that was a good idea?"
    s "You should know by now that I don’t always think things through before deciding to engage in sexual intercourse."
    r "Why are you calling it sexual intercourse now? Do you think formal language is going to make me any less mad at you?"
    s "Are you mad at me for endangering your livelihood? Or are you mad at me for endangering your livelihood while you weren’t around to watch?"
    r "The {i}first{/i} one, dweeb. If I wanted to watch you bone anyone, all I’d have to do is ask."
    s "Or hide behind a privacy curtain in the hospital room that Ayane has in her mansion for some reason."

    scene rinsenseiwalking2
    with dissolve

    r "Y..."
    r "You...knew about that?..."
    s "I may have found out after the fact. And I may have just forgotten that I was probably not supposed to tell you I knew? I can’t really remember."

    scene rinsenseiwalking3
    with dissolve

    r "Welp. There goes ever making eye contact with you again."
    s "To be fair, it’s not {i}that{/i} much different from that night in the hotel where we listened to each other have sex in opposite rooms."
    r "I guess not when you put it that way. But that was basically just me listening to Nodoka since you’re quiet as all hell when you’re hooking up with my classmates."

    scene rinsenseiwalking4
    with dissolve

    r "Also, what the hell is going on with Sana?! "
    r "Has she always been like that and just hiding it from us?! Because I am learning many things about her way too quickly and can’t even talk about most of them due to a legally-binding agreement I recently made!"
    s "A what?"
    r "Doesn’t matter! Sana! Horny! Yes or no?!"

    scene rinsenseiwalking5
    with dissolve

    s "I think she was hiding it, but...I’m not really sure. This side of her is new to me. And that time in the hospital room was the first time we ever did {i}anything,{/i} I think."
    s "I just wish I could remember more of it."
    r "That was the {i}first{/i} time? Really?"
    s "Yeah. I don’t even know how it happened."

    scene rinsenseiwalking6
    with dissolve

    r "That’s...a little concerning then. Because you weren’t really all that...{i}stable{/i} just before that happened..."
    r "Did Sana maybe, like...take advantage of you?"
    s "She’s under five feet tall and weighs about the same as a large bag of rice. I’m not sure how much “advantage” she could take even if she wanted to."
    r "Maybe...it just seems kind of weird since-"
    s "Don’t worry about it, Rin. All things considered, I’ve taken advantage of way more people. If she saw an opportunity and took it, good for her."
    s "Besides, it’s not like you had any issue with it in the moment if you were fingering yourself behind a curtain."

    scene rinsenseiwalking7
    with dissolve

    r "Definitely not my proudest moment, that’s for sure...but at least I didn’t get caught having sex in a fucking cafe, you friggin’ idiot."

    scene rinsenseiwalking8
    with dissolve

    r "Ugh! Everything’s so messed up now! Take me back to when I was a lowly coffee-slinger with a creepy teacher only boning like two girls I knew instead of fifty."
    s "Do you even {i}know{/i} fifty girls? In fact, which girls {i}do{/i} you know about?"

    scene rinsenseiwalking9
    with dissolve

    r "Chika and Futaba for sure because I hear about it all the time."
    s "Futaba talks about that kind of stuff with you?"

    scene rinsenseiwalking10
    with dissolve

    r "Of course. We’re practically sisters, remember?"
    r "She doesn’t go into nearly as much {i}detail{/i} as Chika does, though."
    s "That must be hard for you, huh?"
    r "You have no fucking idea."
    s "Anyone else?"

    scene rinsenseiwalking9
    with dissolve

    r "Well...Sana, obviously. Nodoka, obviously. Then there’s Haruka. But they’re the only ones I know {i}for sure.{/i}"
    s "Are you suspicious of anyone else?"
    r "I’m suspicious of {i}everyone{/i} else. But I’d be {i}mega{/i} shocked if you weren’t also having sex with Ayane. And probably Makoto too since those two have been riding you since day one."
    s "Both literally and figuratively. You’re right."
    r "Guess that’s that, then."

    scene rinsenseiwalking10
    with dissolve

    r "Noriko? Kirin?"
    s "Noriko, no. Kirin, yes."

    scene rinsenseiwalking11
    with dissolve

    r "Noriko’s a no?! Really?!"
    s "Are you not surprised about the Kirin part?"
    r "I kind of just assume Kirin has sex with everyone, so not really. Why not Noriko? She’s head over heels for you, man."
    s "That’s kind of {i}why.{/i} Noriko’s brilliant and driven and I feel a little weird about dragging her into the same pit of quicksand I’m dragging everyone else into. Plus, she has her own stuff going on as well."

    scene rinsenseiwalking10
    with dissolve

    r "Huh...interesting. Why are you just coming out and telling me all of this, though? Is the new Sensei trying to be more honest or something?"
    s "It’s more that I just don’t feel the need to hide anything from you anymore. You’ve done more than enough to keep my secrets."

    scene rinsenseiwalking12
    with dissolve

    r "Hell no I haven’t. I totally let the Chika stuff slip to Otoha that one time and I {i}still{/i} feel terrible about it. You’re insane for telling me literally {i}anything{/i} after that."
    s "Maybe. But you haven’t let anything slip to Chika and {i}she’s{/i} the dangerous one."

    scene rinsenseiwalking13
    with dissolve

    r "That’s precisely why I {i}haven’t{/i} let anything slip to her. I don’t want you to end up dead in a ditch somewhere. She’s so in love with you that it’s literally crazy. Like, {i}literally{/i} crazy. Almost Ami level."
    s "She’s not {i}that{/i} bad. But yeah, she can go a little overboard sometimes. Which makes me feel kind of bad since I haven’t really been spending much time with her lately."

    scene rinsenseiwalking10
    with dissolve

    r "I’m supposed to hang out with her later if you want to come. "
    r "I was gonna meet up with her once my shift was over, but I left my phone at the dorm and can’t tell her that I will never have any shift ever again and am free for the rest of my life."
    s "I’m sure the cafe will be fine. Having it closed permanently would be too huge of a plot divergence and the narrative branching would probably start to get out of hand."
    r "Are you boning Molly too? Because that line makes it sound like you’ve been boning Molly."
    s "She may or may not have put my penis in her mouth recently."

    scene rinsenseiwalking14
    with dissolve

    r "Good for you, Molly. You’ve finally made it."
    s "Not the reaction I was expecting, but cool."

    scene rinsenseiwalking15
    with dissolve

    r "Think you’ll ever make a choice, Sensei? Think you’ve got what it takes to just pick one of them and let the rest find someone else to fall for instead of dooming them to the life of regularly banging a gigolo?"
    s "My answer to that’s a little different now than it would have been a year ago..."
    r "I’m still rooting for Chika if that day ever does come. Sorry, Futaba."
    s "You just don’t want me to die."
    r "You’re not wrong."
    s "It’s kind of interesting how far we’ve come, isn’t it? That just a little while ago, we were both gunning for Chika’s affection."

    scene rinsenseiwalking16
    with dissolve

    r "And I was failing miserably to make her look at me while you were sticking your fingers inside of her."
    s "And {i}now{/i} you’re encouraging me to stay with her while I’m putting my fingers inside a bunch of people."
    r "I remember when someone used to put their fingers inside of me. Those were the days."
    s "I could lend you a hand with that if you really need me to."
    r "Tempting. It might spare me the embarrassment of having to do it myself behind a curtain again. But for Chika’s sake, I will abstain. And for {i}everyone’s{/i} sake, so should you."
    s "But what about yours?"

    scene rinsenseiwalking17
    with dissolve

    r "Don’t worry about me. I can keep using the same strategy I’ve been using ever since I first encountered the proper usage of a detachable shower-head."
    s "Guess things will just stay the same then."
    r "Guess so."
    r "But we’re happy that way, aren’t we?"
    s "Are we?"

    scene rinsenseiwalking18
    with dissolve

    r "I’m smiling, aren’t I?"
    s "For now. But I’m sure that smile will begin to fade in twenty minutes when you meet up with Chika and she starts inevitably ranting about my penis again."

    scene rinsenseiwalking17
    with dissolve

    r "I’ve heard so much about your penis by now that I’m starting to see it in my dreams. Can I use your phone?"

    scene rinsenseiwalking19
    with dissolve

    s "What a strange segue. Maybe don’t repeat that to Chika."

    scene rinsenseiwalking20
    with dissolve

    r "Sometimes I dream about your penis {i}inside{/i} of her. "
    s "I’m pretty sure that you’re supposed to involve {i}yourself{/i} in sex dreams. "
    r "Yeah, but my dreams are basically a giant cesspool of depravity now. Sometimes I’m involved. Sometimes, you’re boning Chika in my old bedroom while I’m downstairs playing checkers with my grandma."
    s "I don’t even know what your old bedroom looks like."
    r "I don’t even know what my grandma looks like. Never met her. Why is your wallpaper just Ami a million times?"
    s "I guess because she didn’t like the picture of Makoto."

    scene rinsenseiwalking21
    with fade

    r "What picture of Makoto?"
    s "Ask her about it. I’m sure she’d love to tell you."

    scene rinsenseiwalking22
    with dissolve

    r "I’ll keep that in mind for when I go back to school on Monday. For now, I must give Chika the jumpscare of her life by calling her from your phone and pretending to be another woman."
    s "Please don’t. She knows where I live."

    if nikinudetrade == False:
        scene black
        with dissolve2

        play sound "phonebeep.wav"

        "Rin gives a Chika a call and, {i}without{/i} pretending to be a mysterious lover of mine, quickly explains why she’s calling her from my phone instead of hers."
        "The two of them talk for a minute or two and reaffirm whatever plans they made for this afternoon before I get roped into speaking to my “girlfriend” as well."
        "Chika does her best to try and get me to join them, but...having something else in mind, I decide it’s best to let her and Rin hang out alone instead."
        "I’m still not ready to be the type of person Chika needs me to be, but...that’s fine. Because she has other people who can be there for her in my place."
        "Rin and I part ways after making it back to the dorms, but she promises to try and keep me updated on anything happening with Koi Cafe as soon as she gets an update."
        "As I watch her disappear into the building, I feel a strange sense of relief. Relief that, even with all that’s changed as of late, what I have with her seems mostly the same."
        "And maybe things will stay that way forever. Maybe they won’t."
        "I’m just glad that she’s a part of my life."
        "And I will do my very best to not get caught having sex with her boss in public anymore."

        stop music fadeout 10.0
        $ renpy.end_replay()
        $ rinspring3 = True
        $ rin_love += 1

        "{i}Rin’s affection has increased to [rin_love]!{/i}"
        "........."
        "......"
        "..."

        jump noonch4

    else:
        r "I’ll stop before things get dangerous. I just want to make her morning a little-"

        scene rinsenseiwalking23
        with dissolve

        r "Hey, since when do you have Otoha’s number? I didn’t realize you two were cool now."
        s "Have we ever been {i}uncool?{/i} Because we’ve never been close, but-"

        play sound "phonebeep.wav"
        scene rinsenseiwalking24
        with dissolve

        s "Wait...Actually, can I have my phone back for a second?"
        r "..."

        scene rinsenseiwalking25
        with fade

        s "Rin? Can I have my phone? I just have to check something."
        r "..."
        s "I don’t like that you’re very quiet all of a sudden. It makes me think you might have seen something. Which, if you did, there’s probably a very good explanation for."
        r "..."
        s "Ugh..."
        s "You opened up her messages, didn’t you?"
        r "..."
        s "{i}Why?{/i}"
        r "{i}Why?...{/i}"

        play sound "static.mp3"
        scene rinsenseiwalking26 with flash
        stop sound

        r "Shouldn’t {i}I{/i} be the one asking that question?..."
        s "I...forgot that was in there."
        r "You {i}forgot?...{/i}"
        s "Why did you open up her messages in the first place? I thought you were just going to call Chika."

        scene rinsenseiwalking27
        with dissolve

        r "Because I’m nosy and wanted to see if you were talking about me so I could tease you about it! I had no idea I’d find {i}this!{/i} Why did she send you this?! And why did you send her someone else’s boobs?!"
        s "Is this really a conversation we need to have when you shouldn’t have ever seen that {i}at all?...{/i}"

        scene rinsenseiwalking28
        with dissolve

        r "You’re right...I shouldn’t have seen this {i}at all.{/i} "
        r "But you shouldn’t have gotten it {i}at all.{/i} "
        r "And if we’re really friends, you’ll want to give me an explanation."
        r "Because I can ignore this if I have to...I know I invaded your privacy and I know how messed up that is. But I really hope you’re not going to {i}make{/i} me ignore it...because {i}this{/i} is way worse and you know that."
        r "That’s why you keep looking away."
        s "..."
        r "Talk to me, Sensei."
        s "..."
        r "Why do you have this?..."
        s "..."

        scene rinsenseiwalking29
        with dissolve

        r "..."
        s "We traded."
        r "Whose idea was it?"
        s "Does it really matter?..."
        r "It does."
        s "..."
        r "..."
        s "It was my idea."
        r "So you specifically asked Otoha for this picture?...And she went along with it in exchange for one that you had?..."
        s "That’s right..."
        r "And how do you feel now that you’ve been caught?"
        s "Not great, to be honest. I’m getting caught in things more often than I’d like lately. I’m getting too careless."
        r "Do you jerk off to it?"
        s "What?"
        r "Do you look at this picture of me and jerk off? "
        s "Uhh..."
        r "Just answer the question."
        s "I mean..."
        s "I wouldn’t have asked for it if I wasn’t going to do that."

        scene rinsenseiwalking30
        with dissolve

        r "{i}Hah...{/i}"
        s "..."
        r "Is this really the type of relationship we have?..."
        r "You secretly touching yourself to pictures of me? {i}Me{/i} secretly touching {i}myself{/i} while listening to you hook up with my friends?"
        r "What are we even doing anymore?"
        s "Being...perverts, I guess?"
        r "I guess, yeah..."
        r "I would have sent you one if you just asked, you know..."
        r "Like...you may have had to talk me into it, but..."
        r "Going behind my back and getting this from my ex is just...sleazy. From {i}both{/i} of you. "
        s "I didn’t really think it through, Rin. It was a spur of the moment thing. And I wasn’t going to ask you for something like this when-"

        scene rinsenseiwalking31
        with dissolve

        r "I’m really disappointed in you, Sensei. "

        if rinbetrayed == True:
            r "After all we’ve been through together, you’re {i}still{/i} doing things like this. You’re {i}still{/i} letting me down."
            r "You never change, do you?"

        else:
            r "After all we’ve been through...you turn around and do this? Really? To {i}me?{/i}"

        s "..."
        r "Is this what I get for disappearing on you for so long? For chasing after someone else instead of you? Is this payback?"
        s "It’s nothing like that, Rin...I’ve never blamed you for going after Otoha."
        r "So this decision was based 100%% on lust?"
        s "Lust and the fact that I will always be a terrible person who does terrible things, even to those I care about the most."
        r "You care about me the most?"
        s "You’re definitely up there."

        scene rinsenseiwalking32
        with dissolve

        r "{i}Hah...{/i}"
        r "You could get in serious trouble for having this, you know. Do I really need to be the one to tell you that?"
        s "Then maybe...{i}don’t{/i} stand out here in the open holding it up for anyone who walks by to see?"
        r "I don’t care about other people. I wanted you to see this {i}and{/i} me at the same time so you could think about how fucked up this is."
        s "I’m sorry, Rin. Really. And I know there’s nothing I can do to make it up to you, but-"

        scene rinsenseiwalking33
        with dissolve

        r "Send me one."
        s "...Excuse me?"
        r "Send me a picture."
        s "Like...of myself?"
        r "Tit for tat. If you’re going to have a picture of me, it’s only fair that I get a picture of you as well. That way, you can’t hold it over my head."
        s "Do you really think I’d do something like that to you?"
        r "No. But I didn’t think you’d trade for my nudes either and look where we are now."
        s "..."
        r "..."
        s "I’ve never sent one before."

        scene rinsenseiwalking34
        with dissolve

        r "Wait, really?"
        s "Yeah. I always just {i}get{/i} them. I never send anything back."
        r "And people keep sending them to you regardless?"
        s "Yeah. I’m surprised I’ve gotten away with it for as long as I have, to be honest."

        scene rinsenseiwalking35
        with dissolve

        r "Then I guess I get to be your first!"
        s "Do I...really have to do this?"
        r "Tit for tat, Sensei! "

        scene rinsenseiwalking36
        with dissolve

        r "And I solemnly swear I definitely won’t do anything lewd while looking at it."
        s "I’m not sure if I believe you."
        r "I’m not sure if you {i}should.{/i}"
        s "Is this really the only way to-"
        r "Yes."
        s "And I’ll be completely forgiven once I-"
        r "Yes."
        s "This seems way too easy."
        r "That’s what friends are for."
        s "Masturbating to each other?"
        r "I masturbate to all of my friends. It’s an unsung perk of being bi. The big change now is that I won’t just have to use my imagination for you anymore."
        s "And how often do you think of me exactly?"
        r "How often do you think of me?"
        s "Pretty often."
        r "Same here."
        s "That’s cool."
        r "Yeah. I guess it is."
        s "..."
        r "..."
        s "I’m gonna be honest, I haven’t felt this tempted to touch you since that time I walked in on you changing."
        r "I’m gonna be honest, I touched myself when you left that night."
        s "Why don’t we just...you know..."
        r "Do it?"
        s "Yeah."
        r "Honestly...I’ve been wondering the same thing a lot lately."

        scene rinsenseiwalking37
        with dissolve

        r "I’m single now...and I’m not actively chasing after anyone."
        r "But, at the same time, there are a lot of people who I really love that {i}really love{/i} you. And we’re friends. Which is why I’ve been content with just masturbating."
        r "But I think that one day, I might have to make a decision too. Just like you will. And if we both make the same decision at the same time, then..."
        r "Maybe we’ll finally stop keeping our hands to ourselves?"

        scene rinsenseiwalking38
        with dissolve

        r "But for now...that’s kind of what we have to do if we don’t want to hurt anyone."
        s "We could always just keep it a secret."
        r "You mean like you kept this picture a secret?"
        s "Fair point."
        s "I guess we just...keep our lust for one another confined to the digital world then?"
        r "You gonna ask me directly next time?"
        s "There can be a next time?"
        r "Depends on what {i}you{/i} send {i}me.{/i} Because I’m the type who actually sends things back."
        s "Okay. I think it’s time for you to call Chika for real. I’m getting a little too tempted right now."
        r "Same here, homie."
        s "That word takes on a whole new meaning with you staring at me like that."
        r "That makes sense."

        scene black
        with dissolve2

        r "I think it might have one now."

        "Rin calls Chika and subsequently leaves me behind...but not before telling me to not even {i}think{/i} of sending her anything until later tonight."
        "I can only imagine how Chika would react if Rin just so happened to get an inappropriate picture of me while the two of them were hanging out. Especially when Chika has yet to ever receive one herself."
        "So for now, I guess I’m off the hook — but I’m {i}on{/i} a different one."
        "I can’t just keep denying the way I feel for this girl that I so {i}obviously{/i} want to conquer...but I can’t just {i}do it{/i} either."
        "The time needs to be right...but time is so frequently fucked up here that the sheer concept of that sounds impossible."
        "I don’t know what I’m supposed to do."
        "..."
        "I don’t know anything anymore."
        "..."
        "Just that I need to take care of something right now."

        play sound "zipper.mp3"

        "{i}You masturbate in a public bathroom! Hooray!{/i}"

        $ renpy.end_replay()
        $ rinspring3 = True
        $ rin_love += 5
        stop music fadeout 10.0

        "{i}Rin’s affection has increased to [rin_love]!{/i}"
        "........."
        "......"
        "..."

        jump noonch4

label rinspring4:
    scene clearnightsky
    with dissolve2
    play music "summerwind.mp3"

    "It was a hot January night in spring."
    "Yeah, I know. "
    "I promise, things will get better though. This isn’t one of those events that begins with some sort of transient, melancholic monologue you’d need to lobotomize yourself to understand."
    "This is one of the {i}good{/i} nights."
    "The kind that you look back on and think, “Huh...I guess there {i}was{/i} a time when I was truly happy.” "
    "Because, maybe it’s just me, but you stop forming those memories once you get a little older. "
    "So those moments you spent with your friends back when your hands were smaller sort of linger there forever — eternally locked in the closet of your mind, opened only when you’re looking for an old shirt or keys or-"
    "Sorry. I’ll stop. I promised this wouldn’t get melancholic and I intend to keep my word despite the many other times in which I’ve deceived you."
    "That backstory goes like this — a pipe burst on the 56th floor of the infinite dorm building. Everything flooded. "

    scene dndbath1
    with dissolve2

    "And, not wanting to bathe alongside their cherished possessions and anything that may have floated out of the abyss that is dorm seven, a handful of the girls from Class 1-A decided to come bathe {i}here.{/i}"
    "A certain someone was not very happy about this."

    i "I do not like this at all."

    "That certain someone was Io Ichimonji. Everyone else was fine, though."

    ay "Don’t worry, we won’t bother you. There’s no one in the men’s bath right now, is there? I’d like to rent out the whole section for the rest of the night."
    i "That’ll be 5,000,000 yen."
    ay "Sure. There should be enough money on this."
    i "Sorry. I meant 10,000,000. Weekend price."
    ay "This should still be okay."

    scene dndbath2
    with dissolve

    i "How much fucking money can there be in unpoppable bubble wrap?!"
    r "Are you sure you’re okay paying for all of us, Ayane? I can chip in now that I’m a supervisor. I’m no longer poor Rin. I’ve graduated from that and would like to go by financially stable Rin now."
    ay "Well, financially stable Rin, it’s fine. It’s technically my dad’s money anyway. But hey, if you have your mom’s credit card, we can always make our parents go halfsies! "
    r "I’m pretty sure I make more than my mom. All she does is walk around the school and check on the ropes. That’s all she learned how to do before Sensei left."
    ay "Are they still where they’re supposed to be?"
    r "I sure hope so. That’s 50%% of her job."
    i "Will you guys stop loitering and yapping if I just let you in for free?"

    scene dndbath3
    with dissolve

    ay "Free? Why? My card is right here. "
    i "It’s not like anyone else is going to rent it out. Just think of it as a special discount for coming here {i}without{/i} Sensei this time."
    r "Is...Is Io doing something {i}nice{/i} for us?"
    i "No."
    ay "I think she is, financially stable Rin."
    i "I’m not. It’s just a discount. Now please take your financial stability into the bath and leave me alone."

    scene dndbath4
    with dissolve

    ay "Whatever it is...thank you, Io. That’s really sweet."
    i "It’s really not. You’ve rented out the whole thing enough to know the actual price by now."
    ay "I have, yeah. But, could you do me a favor and run this card anyway? For whatever amount you want. I’m pretty sure my dad forgot I exist, so this is my gentle way of reminding him."
    i "When you put it that way, yes. "

    scene black
    with dissolve

    i "That’ll be 5,000,000 yen. "
    ay "Here you go. I don’t need a receipt."
    i "Good, because we don’t have a printer. "
    r "You must really hate your dad, Ayane. That’s a lot of money. "
    ay "I am {i}so{/i} fucking tired of smooth jazz, Rin. Ami and Maya are the only ones who understand."
    r "Yeah, you’ve already lost me. Where are they, by the way? I thought they were gonna meet us here."
    i "Sorry. I think I broke your card by trying to put 1,000,000,000 on it. It just keeps getting declined now."
    ay "Even better. Thanks, Io. And financially stable Rin, Ami and Maya will be here soon. They’re coming from Sensei’s place, so-"
    r "Sorry. Can you just go back to “Rin” now? All of this “financially stable” stuff is making it feel like I’m bragging."
    i "Can {i}both{/i} of you go back to not being here? I did my part and I would like the yapping to cease now. "
    ay "Yup! Come on, regular Rin! Come on, everybody else! Let’s all get naked and look at each other!"

    play sound "static.mp3"
    scene dndbath5 with flash
    stop sound

    r "Easy for you to say when your body looks like it was sculpted by the gods. "
    ay "We’re all beautiful in our ways, Rin. I just like seeing all of you blossom into lovely young women."
    r "For a straight girl, you sure say a lot of really gay stuff."

    scene dndbath6
    with dissolve

    ay "There’s nothing gay about wanting to see your friends naked."
    r "I’m glad I heard that now and not in middle school or younger Rin would have been even more confused about what was going on in her head."
    ay "All that matters is that you’re perfect {i}now.{/i}"
    r "Mhm. Thanks."

    scene dndbath7
    with dissolve

    r "Futaba, do you have any sort of bath plans?"
    f "..."
    f "What is a “bath plan?”"
    r "Like a plan for what you’re going to do in the bath."
    f "..."
    f "Well, I was really hoping to practice my swimming tonight."

    scene dndbath8
    with dissolve

    r "Damn it. Okay. Never mind then."
    a "Heeey! Sorry we’re late! Maya only chooses to watch weird, avant garde movies and whatever we watched tonight went on way longer than I thought it would. Bath time!"
    m "I regret nothing. Bath time seconded."
    f "Rin...I’m not actually planning on practicing my swimming tonight. What do you want to ask me?"

    scene dndbath9
    with dissolve

    r "Can we talk with, like...just the two of us when we get in? No homo."
    f "For the millionth time, you don’t need to say “no homo” any time you want to talk to me in the bath and/or shower."
    r "But that leaves the possibility for me to homo at you when you’re least expecting it."
    f "I don’t think “homo” is a verb. "
    r "It is when you’re aggressively bisexual and suck at flirting. "
    f "Fair. Either way, yes. We can talk. Something specific on your mind?"

    scene dndbath10
    with dissolve

    r "Poooooossibly?..."
    f "Okay. I think I’ve got a feeling I know what it is then."
    r "Nuh-uh. I’m too cool and mysterious for you to predict something like that."
    f "Yeah, I definitely know what it is."

    scene dndbath11
    with dissolve

    r "No way. You-"

    scene dndbath12
    with dissolve

    r "Dear...{i}God.{/i}"

    scene dndbath13
    with fade

    f "Tsuneyo? She’s beautiful, isn’t she?"
    r "Close my eyes. I’m about to homo."
    t "Feast your eyes upon what can only be referred to as “peak performance,” girls of 1-A."
    mo "Humble as always, Kendo Princess."
    m "Woof."
    a "Ayane...do you ever think-"
    ay "No. "

    scene dndbath14
    with dissolve

    a "I didn’t even say anything yet!"
    ay "I know. But comparing {i}your{/i} body to Tsuneyo’s will only end in pain. You’re two different types of girls and that’s totally okay!"
    m "I repeat. Woof."

    scene dndbath15
    with dissolve

    a "F...Flat girls are good too! Right, Molly?!"
    mo "Precisely, Arborea! We need not the endowment of Hera when Aphrodite exists! Assuming that...Hera was more endowed. Which I assume she was because of the whole “fertility” thing."
    t "Everyone loves small breasts until their children starve to death from lack of milk."
    ay "Breast size has nothing to do with milk production, actually. And you can all borrow some of my books on motherhood and childcare if you’d like to confirm that for yourselves."

    scene clearnightsky
    with dissolve2

    t "Lies. All it takes is common sense to realize there would be no real estate for milk storage in a body like Arborea’s. Xessaxia is clearly the most fit to be a mother here."
    f "Hahah...hah...no, I...think Ayane is still the most fit out of any of us..."
    m "Have I mentioned “woof” recently? Because-"
    mo "We get it! You want the Kendo Princess! We {i}all{/i} do!"
    r "Futaba, carry me to the bath. I can’t look at her or I’ll cum. "
    f "Ew! Rin!"
    r "Just carry me!"

    play sound "water1.mp3"
    scene black
    with dissolve2

    f "No! Carry yourself! With your...legs!"
    r "That’s called “walking,” idiot!"
    t "Never fear, Nithhala. I will carry you. It will be just like when I saved the city from the death ball."
    r "Don’t compare me to the death ball!!!!!"

    "........."
    "......"
    "..."

    scene dndbath16
    with dissolve2

    r "Hah...I needed this. I’ve been so stressed lately, you don’t even know."
    f "So, are we going to talk about how you’re in love with Sensei {i}now?{/i} Or do you want to soak for a little longer first?"

    scene dndbath17
    with dissolve

    r "I am not!"
    f "Oh, sorry. What was it you wanted to talk about then?"
    r "That..."
    r "I..."
    r "I need help with our algebra homework!"

    scene dndbath18
    with dissolve

    f "Rin..."
    r "Okay, fine! I-"
    f "Shh...screaming it at the top of your lungs defeats the purpose of talking alone, doesn’t it?"

    play sound "water1.mp3"
    scene dndbath19
    with dissolve

    r "Mmm..."
    f "Take your time. We’re not getting kicked out any time soon."
    r "I know...it’s just..."
    r "It’s weird when everyone else notices your feelings before {i}you{/i} do. And ever since you guys all accused me of wanting to {i}fuck{/i} him at the Christmas party, I haven’t been able to stop thinking about it."
    f "About...{i}specifically{/i} having sex with him? Or your feelings for him in general?"

    scene dndbath20
    with dissolve

    r "I don’t even {i}know.{/i} That’s the problem."
    r "Like, you’re obviously my {i}best{/i} friend. But Sensei is my “best” friend. My homie. "
    r "He’s been with me through practically everything since high school started and, do I frequently imagine his penis inside of me? Yes. But should I {i}receive{/i} said penis? Absolutely not. No way. Nuh uh."
    r "I just can’t stop thinking about him."
    f "You’ve always done that, Rin."
    r "Get penised? I certainly have not. Not by anyone real, at least. Even Otoha only used her hands and mouth and-"
    f "I...do not need to know the details of that. What I meant was that you always get hung up on whoever you’re currently into. And right now, that person is obviously Sensei."
    r "But it {i}shouldn’t{/i} be. He’s {i}old.{/i} That’s {i}weird.{/i}"
    f "You do realize you’re speaking to someone who has been “penised” by him many times, right?"

    scene dndbath21
    with dissolve

    r "Yeah! So why are you being {i}supportive{/i} of me right now? Isn’t this a major betrayal? And not just to {i}you{/i} either. To Chika. Ayane. Ami. Everyone {i}else{/i} who loves him. "
    r "Why can’t I just like Uta or Kirin or something? That’d be so much easier."
    f "Yeah, but that’s not how it works. And I don’t think of it as a betrayal at all. I’ve never for a second imagined being exclusive with Sensei."
    r "Futaba. Come on."

    scene dndbath22
    with dissolve

    f "Okay, sorry. What I {i}meant{/i} to say was I never imagined such a thing would be {i}possible.{/i} Not with someone like me at least."
    r "I really don’t like it when you say things like that. You’re the most beautiful, amazing person I’ve ever met and Sensei would be lucky to have you."

    scene dndbath23
    with dissolve

    f "He’d be lucky to have {i}you{/i} too. And if you actually have feelings for him, I think you’re better off acting on them rather than just giving everyone else a shot instead."
    r "{i}Maybe.{/i} But there’s the fear of fucking things up too. I don’t want to ruin the relationship I already have with him because it’s...honestly, one of the best things that’s ever happened to me."

    scene dndbath24
    with dissolve

    r "Which is...embarrassing and...weird to say about a guy who’s over twice my age. But it’s the truth. So maybe it’s best if I just...you know...keep waiting. For someone {i}else{/i} to catch my eye."
    f "Well, do you think you’re capable of that now that your feelings are out in the open? Or do you think you’re going to cave and confess to him on the beach like you have with your past two love interests?"
    r "I doubt I’ll last until the beach if a confession is coming. I literally can {i}not{/i} stop thinking about him lately. It’s almost as bad as I was with Chika. My poor vibrator is going to explode."
    f "Again, don’t need details like that."

    scene dndbath25
    with dissolve

    r "Well, you’re getting them because I don’t know who else to talk to about this. So yeah, stress level — infinite. Love sucks. Being a teenager sucks. I can’t wait until I’m older and don’t have to deal with all these hormones."
    f "If you think getting older is going to stop you from being so horny, I’d urge you to take another look at the person you’re falling for this time and see what that’s done for {i}him.{/i}"
    r "Please. The last thing I need is more thoughts about him and being horny. Especially when I’m already surrounded by boobs and ready to explode."
    f "Just fuck him already."

    scene dndbath26
    with dissolve

    r "Futaba! What the heck?! You’re supposed to be my voice of reason, not the horny devil on my shoulder!"
    f "I’m sorry! It’s just...hahah!"

    scene dndbath27
    with dissolve

    f "You’re one of what I can only assume is a very small group of girls in our class who {i}hasn’t{/i} yet. It doesn’t hurt to give it a shot. "
    r "But you specifically told me it {i}did{/i} hurt when he did it with you."
    f "Well...physically, yes. He is...{i}large.{/i} But emotionally, it-"

    scene dndbath28
    with dissolve

    f "Actually...it has the potential to be very emotionally painful too considering that...I imagine you want him all to yourself, so..."
    r "So basically, I’m just fucked. And I’m fucked by literally {i}not{/i} being fucked. Which is like the worst possible way to be fucked out of all the fucking ways to be fucked."

    scene dndbath29
    with dissolve

    f "Yeah, basically."
    f "But hey, at least you have your vibrator."

    play sound "water1.mp3"
    scene dndbath30
    with fade

    r "Mmm..."
    f "At the end of the day, I think it’s important that you act on your feelings rather than trying to hide them for the sake of your friends."
    f "But of course, that’s just {i}my{/i} stance. And I imagine Chika is the one you’re the most terrified of right now given how close you two have become and...how scary she just...naturally {i}is.{/i}"
    r "Pbrlblrblrlblrblrll...."
    f "I have no idea what you just tried to say. But I know you well enough to assume it was something else about how you’re mostly just afraid of ruining something."
    r "Pbrlbrl..."
    f "Well...again, this is just the way I see things...but I don’t think that’s avoidable, Rin. I think you’re going to wind up hurting someone one way or another no matter {i}how{/i} desperately you try to avoid it."
    f "Doing things for yourself isn’t always selfish. Sometimes, it’s what {i}needs{/i} to be done if you want to make any progress. "
    f "And if you ever feel like you’re stuck, it’s fine to chalk that up to being young and indecisive. Like, who knows? Maybe in ten years, this will be something the two of us will look back at and laugh about."
    f "But if, right now, you’re thinking “I hope he’s still with me ten years from now,” that’s never going to happen if you don’t act."
    r "Pblrlblrlblrl........"
    f "I still have no idea what you’re trying to say."

    play sound "water1.mp3"
    scene dndbath31
    with dissolve

    t "Hello. The Emerald Guardian’s weak European body has forced her to flee from the water first. May I join you in drowning Nithhala?"
    r "Pbrlblr!"
    f "Nithhala says “yes please.”"

    scene dndbath32
    with dissolve

    t "Excellent. I am very experienced when it comes to dealing out death. I will make sure her departure from this mortal coil is slow and painful, the way it should be."
    r "{i}Plblrlbr...{/i}"
    f "Nithhala says that all you need to do in order to make that happen is sit right where you are without moving. "

    scene black
    with dissolve2
    play sound "water1.mp3"

    r "....Pah! How’d you manage to translate all of my waterspeak so perfectly?! I’m supposed to be cool and mysterious!"
    t "You are the least cool and perhaps the least mysterious person I know."
    r "And you’re supposed to be- oh fuck. I looked at them again."
    t "You may touch them if you like. I am currently open to sexual experimentation. "
    r "Okay! I’m getting out of the bath now! "

    play sound "water1.mp3"

    r "{i}Molly! Where are you?! It’s not safe in there and I understand why you left! It’s not your European body at all! It’s- oh. She’s passed out.{/i}"

    "And so Nithhala- err...{i}Rin{/i} manages to confront the dark entity that’s been growing inside of {i}her{/i} lately."
    "And while the answers she received were not technically the ones she wanted, they {i}did{/i} help her confirm one thing."

    $ renpy.end_replay()
    $ rinspring4 = True
    $ rin_love += 1
    stop music

    jump rinspring5

label rinspring5:
    play sound "static.mp3"
    scene rinmastbed1 with flash
    stop sound
    play music "lastdailysong.mp3"

    "She {i}really{/i} wanted to fuck her teacher. "

    r "Hah.....ah.....ah......"

    "Yet she tricked herself again by filling her laptop with images and videos of beautiful women, as if to say “remember how you’re supposed to be.”"
    "She was sure these thoughts would cease if he were only slightly younger. If she were only slightly older. But more tabs open up. More women fill the screen."
    "They begin to spill out of the monitor like broth from a pot of over-boiling, unwatched soup — taking turns kissing her and licking her despite the age gap that was somehow {i}now{/i} okay."
    "Why? Because it was happening behind a screen? Because girls like her weren’t {i}allowed{/i} on that screen? Would her stance change if they {i}were?{/i} Would she run if they {i}did{/i} spill out from the monitor?"

    scene rinmastbed2
    with dissolve

    r "Mn....mnn!"

    "Faster and faster her fingers would move — racing toward the finish line like a Kenyan sprinter rather than a confused bisexual trying to cum to make the feelings stop. Or at least that’s how she’d look at it."
    "Unfortunately, these were not feelings that would stop so easily, and this was evidenced by the wear and tear of a computer chair that now creaked uncontrollably every time she took her favored position."
    "Moving softer and slower helped sometimes to mask the noise. But softer and slower wasn’t enough."
    "And bringing the laptop to the bed just made it harder to comfortably witness this incessant, self-inflicted persuasion."

    scene rinmastbed3
    with dissolve

    r "Hah! Hah...hah!...Ah!"

    "Yes...open your eyes. Keep them glued to the lies you feed yourself to prop up the status quo. Forget {i}everything{/i} about the way he looks at you."

    if nikinudetrade == True:
        "{i}Forget{/i} his desire to {i}fuck{/i} you — or how tightly he must have gripped his cock when he’d jerk off to the picture he stole. Forget how many times you’ve thought of it since then. Forget, Rin. {i}Forget.{/i}"

    r "Sen...sei..."

    "But remember his name — or at least what you call him. How the role is what made it all attractive in the first place. How-"
    "No."
    "That was never important to you, was it?"

    scene rinmastbed4
    with dissolve

    r "Aaah...aah!"

    "The truth is you were one of the first. "
    "That you were accidentally picturing a future together {i}long{/i} before he’d gotten to everyone else. But it was wrong..."
    "So you stopped. "
    "No..."
    "You {i}tried{/i} to stop. You just never could!"

    play sound "static.mp3"
    scene rinmastbed5 with flash
    stop sound

    r "Nghh!"

    "Night after night, even when you were with someone else, he’d still find you! Deep in the corners of your mind! Lurking there like your very own shadow! Refusing to ever leave you alone!"

    r "Mm! Mmmnh! Mm!"

    "This is {i}your{/i} fault for taking so long! You could have {i}had{/i} him if you were faster! You’ll only be a number if you act now! Is {i}that{/i} enough to make you cum?"

    scene rinmastbed6
    with dissolve

    r "{i}Hah...{/i}"

    scene rinmastbed7
    with dissolve

    "Or is there something else you need?"

    play sound "vibrate.mp3"
    scene rinmastbed8
    with dissolve

    r "Ahhn...ah....aaah...."

    "A tool to take the pain away. "
    "You’re used to things like that. "
    "We’ve all seen what you do to yourself. How you open up your flesh to let the feelings out."
    "You let him in {i}then.{/i} Would it really be so different to let him in {i}now?{/i}"

    scene rinmastbed9
    with dissolve

    r "Ah...ah...mnh...haah..."

    scene rinmastbed10
    with dissolve

    r "Mmnh..."
    r "..."
    r "I wonder what would happen...if he showed up right now?"

    "No you don’t. You {i}know{/i} what would happen. This is just the way you tell yourself you don’t."
    "By pretending to be someone you’re not. By pretending {i}not{/i} to want things you actually {i}do.{/i}"
    "But the thing is, there’s always a way to change that. "

    scene rinmastbed11
    with dissolve

    r "Mmh..."

    "And sometimes-"

    scene rinmastbed12
    with dissolve2

    "All it takes is a little impulsiveness."
    "An uncontrollable urge to feel better {i}now{/i} and hurt later."
    "The kind you can fit in your pocket."
    "But what you’ll find in yours is better than a god — it's salvation."
    "And you can keep it, so long as you figure out how to charge its battery."

    r "Greetings...homie. Would you like...to fuck?"

    scene rinmastbed13
    with dissolve

    r "No. Ew. Obviously no. Weird."
    r "Maybe just...do you want to come over? Is that {i}too{/i} casual? "

    scene rinmastbed14
    with dissolve

    r "I should make it clear that I {i}want{/i} to do stuff, right? Otherwise he’ll just...not do anything again. But, like...{i}what?{/i}"
    r "How do I boy? How {i}does{/i} boy? Boy sex? Sex boy. Give me...the wiener."

    scene rinmastbed15
    with dissolve

    r "Aaaaaah! Why is this so hard?! I did it with Otoha a zillion times!"

    scene rinmastbed16
    with dissolve

    r "Okay! Calm down, Rin. You can do this."
    r "It’s Sensei, not some random dude. He’ll take care of you. He’ll take...{i}really{/i} good...care of..."
    r "I am so fucking horny. This is a terrible idea. I’m going to regret this. I’m going to regret this. I’m...mm!"

    play sound "phonebeep.wav"

    r "Dear Sensei-"

    stop music
    play sound "static.mp3"
    scene rinmastbed17 with flash
    stop sound
    play music "10c.mp3"

    ri "Bye, you two! Don’t forget to practice safe sex! Babies are loud and I don’t want to watch yours! Even {i}if{/i} it’s a cute biracial one with Imani’s eyes!"
    ima "Thanks, Rika! I’d offer to let you join us, but I don’t want to be graded on my performance again!"
    ri "That’s fine! I already asked Akira and he gave you a D!"
    ima "I really hope that’s just a penis joke!"
    ri "Hahah! See you later!"

    scene rinmastbed18
    with dissolve

    ima "That {i}was{/i} just a penis joke...Right, Senpai?"

    scene rinmastbed19
    with dissolve

    s "{i}Come on. I told Ami I’d be home early tonight.{/i}"
    ima "{i}S-Senpai! Please tell me that was a joke! My self-esteem can’t keep taking blows like this!{/i}"
    s "{i}But if I tell you that, you won’t work extra hard today. And the Imani I want to see in there is the one who tries her best.{/i}"

    play sound "vibrate.mp3"
    scene rinmastbed20
    with dissolve

    ima "{i}{size=-10}Oh, you’re on. We’re doing it Ghana style tonight, Senpai. Prepare to never walk again.{/i}{/size}"

    scene rinmastbed21
    with dissolve

    ri "Wait, Akira! You forgot your-"

    play sound "doorslam.mp3"
    with hpunch

    ri "...phone."
    w "I wonder when this honeymoon phase of theirs is going to come to an end."
    os "Yeah. Imani really might wind up pregnant at this rate and {i}I{/i} don’t want to watch the baby either. "

    play sound "vibrate.mp3"
    scene rinmastbed22
    with dissolve

    ri "..."
    play sound "vibrate.mp3"
    ri "........."
    play sound "vibrate.mp3"
    ri "Jesus. How many texts is this guy going to get?"
    scene rinmastbed23
    with dissolve
    play sound "vibrate.mp3"
    ri "....."
    play sound "vibrate.mp3"
    ri ".........."
    play sound "vibrate.mp3"
    ri "....."
    play sound "vibrate.mp3"
    scene rinmastbed24
    with dissolve

    ri "Fine! I’ll just take it {i}to{/i} him then! And maybe get invited to a threesome in the-"

    scene rinmastbed25
    with dissolve

    ri "Rin?"

    play sound "vibrate.mp3"

    ri "..."

    play sound "vibrate.mp3"

    scene rinmastbed26
    with dissolve

    ri "What a crazy coincidence! That’s my daughter’s name too!"

    play sound "static.mp3"
    scene rinmastbed27 with flash
    stop sound

    ri "Hello...Rin. My name...is Rika! I’m sorry...Akira can’t get to the...phone now...but..."

    play sound "vibrate.mp3"

    scene rinmastbed28
    with dissolve

    ri "Ooh! Picture message! I wonder what she-"

    stop music fadeout 3.0
    scene rinmastbed29
    with dissolve2

    ri "..."
    ri "..."
    ri "..."
    ri "..."
    ri "..."

    play sound "static.mp3"
    scene rinmastbed30 with flash
    stop sound
    play sound "phonebeep.wav"

    r "Aaah! Oh my God! He texted back!"

    scene rinmastbed31
    with dissolve

    r "Okay! Okay, okay, okay! You’ve been rejected before, Rin. You can handle it again. Just open your eyes...and read the message."

    scene rinmastbed32
    with dissolve

    r "Just read the..."

    scene rinmastbed33
    with dissolve2

    r "..."
    r "..."
    r "..."

    scene black
    with dissolve2

    r "He’s..."
    r "Actually coming!"

    "........."
    "......"
    play sound "knock.mp3"
    "..."

    r "O...One second! I just...uhh..."
    r "Hold on!"

    "........."
    play sound "footsteps.mp3"
    "......"
    "..."

    play sound "dooropen.mp3"
    scene rinmastbed34
    with dissolve2

    r "H...Heeeeey! "
    r "Sorry for...sending so many messages, it’s just...you know...how I am and..."
    r "I just..."

    scene rinmastbed35
    with dissolve

    r "It seems kind of surreal that you and me are-"

    scene rinmastbed36
    with dissolve2

    r "...Mom?"
    ri "Were you expecting someone else?"

    play sound "static.mp3"
    scene rinmastbed37 with flash
    stop sound
    play music "thingsthathurt.mp3"

    r "Wha- no! Not at all! I wasn’t expecting anybody! Futaba’s hanging out with Nodoka tonight and-"
    ri "So that whole, “it’s kind of surreal” thing was just...what? Are you rehearsing for a play? Practicing your lines this late at night?"

    scene rinmastbed38
    with dissolve

    r "Uhhhhhhhh...yeah! I guess you...heard from Futaba, but...I’m an actor now! Or...actress. But I’m still not very good, so-"
    ri "Cut the crap, Rin. I know you were waiting for someone."

    scene rinmastbed39
    with dissolve

    r "I..."
    ri "Be honest. I might not be Rie, but I’m still your mother."
    r "..."
    ri "I’ve got all night."

    scene rinmastbed40
    with dissolve

    r "Okay, fine. I {i}was{/i} meeting someone. And they could be here at any moment, so...if we could wrap this up quickly-"
    ri "Who?"

    scene rinmastbed41
    with dissolve

    r "Some...guy from a different school! Why does it matter?"
    ri "{i}What{/i} different school, Rin? There’s only one high school in Kumon-mi now."
    r "Yeah, he...graduated last year. From...Kumon-mi Academy."
    ri "And his name?"
    r "T...Tyler."
    ri "{i}Tyler.{/i}"
    r "He’s...half American."
    ri "Mhm. Got it."
    ri "Just out of curiosity, is there anything you {i}aren’t{/i} going to lie to me about tonight? Or do you just expect me to fucking believe {i}everything{/i} because {i}I’m{/i} not very smart?"

    scene rinmastbed42
    with dissolve

    r "I’m not lying! Really! I-"

    scene rinmastbed43
    with dissolve

    ri "{i}Dear Sensei, I’ve been thinking about it for a really long time now, and have decided that I am ready for you to part my legs like Moses did the Red Sea.{/i}"
    r "Wh..."
    ri "{i}Additionally, I would greatly appreciate the opportunity to prove to you just how willing I am to proceed with this sexual relationship via this digital coupon, redeemable for one hundred blowjobs any time you like.{/i}"
    r "How...do you know all that?..."

    scene rinmastbed44
    with dissolve

    ri "How do I {i}know{/i} all of that?! {i}That’s{/i} what you’re worried about?! Not the fact that I caught you trying to seduce your fucking teacher?! You’re in high school!"
    r "I’m sorry! I’m sorry! I know it looks bad! I know! But-"

    scene rinmastbed45
    with dissolve

    ri "It doesn’t just {i}look{/i} bad, Rin! It {i}is{/i} bad! And it’s the dumbest fucking thing I have ever seen you do!"
    ri "You’re supposed to be better than this! What the fuck is going on?! Is this another depression thing?! Are you just trying to {i}feel{/i} something again?! What is it?!"
    r "Mom! Mom. I know. I fucked up. I knew it was wrong and I did it anyway. But Sensei-"

    scene rinmastbed46
    with dissolve

    ri "He’s a grown fucking man, Rin."
    r "I know that! And I.......like him."
    ri "Yeah. I got that from the five minute video you decided to send him of you fingering yourself."

    scene rinmastbed47
    with dissolve

    r "You {i}watched{/i} that?!"
    ri "Not all of it! But yeah, some! Because I couldn't fucking believe my eyes! You’re my daughter! You’re just a teenager! You shouldn’t be doing things like that!"
    r "But...{i}you{/i} did all sorts of crazy shit when you were my age! "
    ri "With people {i}my age,{/i} yeah! But even if the opposite was true, do you {i}want{/i} to end up like me?! I’m 42 years old and making less money than you! I’m a fucking disgrace! Don’t be like me!"
    r "Okay! Okay, I’m sorry. Just...take my phone. Do whatever you want. I fucked up."

    scene rinmastbed48
    with dissolve

    ri "Oh, I’m taking your phone alright. But first, I want to know more about what the fuck is going on here."
    ri "Has he been {i}trying{/i} to get with you? Has there been any...I don’t know...{i}contact{/i} or-"

    scene rinmastbed49
    with dissolve

    r "None. Zero. I swear. Sensei is 1000%% innocent and this is all on me. There is {i}no{/i} need to get him involved. None."
    ri "How am I supposed to believe that when you lied about literally everything else right to my face, though?"
    r "I know how it looks. And I...I don’t blame you for not believing me. But I {i}really{/i} don’t want to get him in trouble because {i}I{/i} am an idiot. It’s all me. "
    ri "Where did you even learn to talk like that?...Because I’ve seen a lot of vulgar shit in my day, but...western silverbacks? What does that even mean?"

    scene rinmastbed50
    with dissolve

    r "It’s a......type of......gorilla......"
    ri "It’s a type of gorilla..."
    r "Please just...forget...you read any of that..."
    r "This is...embarrassing enough already..."
    ri "Do you have any idea how much danger you’d be putting him in by sending that to his phone? Or putting {i}yourself{/i} in by sending it in the first place?"
    ri "If he actually did show up and wanted to go through with your fucking gorilla shit, what would happen next, Rin?"
    r "Well, I...imagine we’d...you know..."
    ri "And you’re {i}okay{/i} with that? Fucking a grown man? What happened to Chika? Otoha? Girls your age? Even {i}guys{/i} your age? None of them do it for you anymore? You need adults now?"

    scene rinmastbed51
    with dissolve

    r "It’s not {i}adults,{/i} Mom. It’s Sensei. Specifically Sensei. "
    r "And this is obviously some sort of sign or something because I’ve prevented myself from trying to do this for basically forever now and you just {i}happened{/i} to have his phone for some reason the instant I caved."
    ri "I still have it. I left in such a rush that I forgot to give it back."
    r "That stuff I sent...it’s not all...still in there, is it?"
    ri "Of course not. Do you think I’d just hand it back over to him without doing anything? What, so we can watch you fuck yourself together?"
    r "No! And could you please stop bringing that up? This is already the single most embarrassing thing that’s ever happened to me and that’s only making it worse."
    ri "I just need you to understand how wrong-"

    scene rinmastbed52
    with dissolve

    r "I know! I know how fucking wrong it is! That’s why it’s fucking killing me! I don’t {i}want{/i} to like him, but I do!"
    r "And it’s confusing as fuck hearing from my therapist and friends and {i}everyone{/i} else that I need to do what will make {i}me{/i} happy when all of the things that {i}might{/i} are specifically the things I’m supposed to avoid!"
    r "I’m confused! I’m scared! I’m horny! And I want to die, but I don’t! So what am I supposed to do?! Just wait it out?! We already know medication doesn’t work! So what do I do, Mom??! Tell me! Help me!"
    ri "Why do you think I’m here?..."
    ri "To punish you?..."

    scene rinmastbed53
    with dissolve
    play sound "dooropen.mp3"

    r "I mean...yeah, obviously. If you’re going to take my phone away and talk to me about how stupid I am. Because {i}that{/i} doesn’t help at all. "
    ri "Well, I’m sorry, but I don’t possess the magic cure to being a teenager. We {i}all{/i} do stupid shit at your age. I just never thought that {i}this{/i} would be a talk we needed to have."

    scene rinmastbed54
    with dissolve

    c "Hey, uhh...I’ll leave if this is a...family thing. I just...heard some screaming and...wanted to make sure Rin was okay."
    ri "Unfortunately, Rin did some very {i}stupid{/i} shit tonight. But I’ll let her fill you in on it since I’ve {i}embarrassed{/i} her enough already."

    $ renpy.end_replay()
    $ rinspring5 = True
    $ rinphoneblock = True

    scene black
    with dissolve2

    "This is what you get for waiting so long."

    jump rinspring6

label rinspring6:
    play sound "static.mp3"
    scene chikarinnice1 with flash
    stop sound

    "{i}This{/i} is what you get for bathing in indecision while everyone else drowned themselves in the fountain of youth."
    "But that’s okay — because somewhere in the wishing well, there’s a bucket with your name on it."
    "You can climb in whenever you like, but you’ll need to wait for someone or {i}something{/i} else to pull you up."
    "Either that...or just wish harder."
    "There is no room for second guesses here. "
    "That’s why he “suffers” so much."

    ri "Where is your phone?"
    r "..."
    ri "Rin-"
    r "It’s on the desk..."

    scene chikarinnice2
    with dissolve

    r "Can you at least text Sensei and tell him that you’re taking it away, though? If he tries to contact me-"
    ri "I have his phone, remember? I’ll tell him when I go back to the bar."

    scene chikarinnice3
    with dissolve

    r "Oh...right."
    c "Wait, Rin I understand. But why do you have {i}Sensei’s{/i} phone?"
    ri "Again, you can ask Rin. "

    scene chikarinnice4
    with dissolve

    ri "Don’t stick around for long, though. She’s grounded indefinitely starting right now. "
    c "Oh...yeah. I had some stuff to do tonight anyway."
    ri "Yeah...sure."

    scene chikarinnice5
    with dissolve

    ri "Do I need to take your laptop too?"
    r "Please don’t. I need that for school. "
    ri "You know I have to tell Rie about this, right?"
    r "Yes, Mom...I know. "
    ri "Okay..."

    scene black
    with dissolve2

    ri "Goodnight."

    play sound "static.mp3"
    scene chikarinnice6 with flash
    stop sound
    play music "lastdailysong.mp3"
    play sound "doorslam.mp3"
    with hpunch

    r "Mm!"
    c "What the fuck was that about? I’ve never seen your mom look so serious before."
    r "I’m sorry..."

    scene chikarinnice7
    with dissolve

    c "For what? What-"
    r "I’m sorry, I’m sorry, I’m sorry, I’m sorry! I tried to hold it in, but I couldn’t! I really tried, Chika! I’m so sorry!"
    c "Tried...what? What happened?"

    scene chikarinnice8
    with dissolve

    r "If I tell you...you’ll never want to talk to me again. I’m scared. I don’t...want you to leave."

    scene chikarinnice9
    with dissolve2

    c "Just calm down, okay? I’m not going to leave you, Rin. I can assure you I’ve gone through worse than whatever it is you’re about to tell me."
    r "Y...Yes, but..."

    scene chikarinnice10
    with dissolve

    r "That...doesn’t change how you’re never going to look at me the same way again. And I’ll deserve it, too. You trusted me and...and you shouldn’t have. You-"

    scene chikarinnice11
    with dissolve

    r "I...it...I’m...I’m so fucking sorry, Chika! I {i}really{/i} am! I’m just lonely! And confused! And I’m sorry! I’m really, really fucking-"
    c "Wow. You are a {i}wreck{/i} right now. Whatever it is must be pretty bad, huh?"

    scene chikarinnice12
    with dissolve

    r "Chika...I-"
    c "When I was little, my mom used to hold my hand whenever she’d have to give me bad news."
    r "...What?"
    c "It just makes it hurt a little less. And reminds you that there’s someone else you get to experience that pain {i}with.{/i}"
    r "But...I...I’m the one causing it. You’ll want to break my hand off."
    c "Try me."
    r "Chika-"
    c "Just shut up and hold my hand, Rokuhara. Dry those tears too. You’re terrible at delivering bad news."

    scene chikarinnice13
    with dissolve

    r "It feels weird...hearing you call me by my last name."
    c "Will it feel a little less weird if you use mine too?"
    r "Ch..."
    r "Choso...kabe..."
    c "Weird?"
    r "A little."
    c "Rokuhara."
    r "...Chosokabe."

    scene chikarinnice14
    with dissolve

    c "Rokuhara..."
    r "Chosokabe?..."

    scene chikarinnice15
    with dissolve

    c "Pfft! Yeah...it {i}is{/i} weird, isn’t it?"
    r "Hahah......hah...."

    scene black
    with dissolve2

    c "Come on. I feel like I’m gonna want to sit down for this."
    r "Yeah...I think you might..."

    "........."
    "......"
    "..."

    scene chikarinnice16
    with dissolve2

    r "So..."
    r "The reason...my mom took my phone away...is..."
    r "Uhh..."
    r "..."
    r "How do I...where do I..."
    r "Sorry...it’s...um..."
    c "Take your time. I was lying when I told your mom I had stuff to do tonight."
    r "Yeah...I lied to her too..."
    r "About...basically everything..."
    c "So this is all one big misunderstanding then?"

    scene chikarinnice17
    with dissolve

    r "Y...Yeah! A misunderstanding. That’s...exactly what..."

    scene chikarinnice18
    with dissolve

    r "Mm..."
    r "No."

    scene chikarinnice19
    with dissolve2

    r "Chika, I..."
    r "I think I have feelings for Sensei."
    c "...........Oh."
    r "And I...may have been...a little too forward about some of those feelings tonight."
    c ".........{i}Oh.{/i}"
    r "He never...received them, though. I guess my mom...had his phone for some reason? I don’t...really get {i}why?{/i} But I sent him a bunch of texts about it and...{i}she{/i} just showed up instead."
    c "What kind of texts? Like...a confession?"

    scene chikarinnice20
    with dissolve

    r "Um..."
    r "Not...{i}exactly.{/i}"
    c "Come on. Just be honest. We can be mature about this. I’m not going to hurt your hand."

    scene chikarinnice21
    with dissolve

    r "So, like...do you remember how horny you were that time Sensei started kind of avoiding you? And how you’d never shut up about all of the crazy, sexual things you wanted to do with and {i}to{/i} him once he stopped?"
    c "Of course I do. It was literally hell."
    r "Okay, well...that may or may not be how I’ve been feeling lately. And I may or may not have...sent him probably 10 paragraphs about wanting him to do me with the intensity of a western silverback."
    c "The gorilla?"
    r "The gorilla."
    c "Wow."
    r "But Chika, I {i}swear,{/i} I have never actually hooked up with him. It’s all fantasy. And-"
    c "It’s {i}not{/i} fantasy though, Rin. You literally {i}just{/i} said you have feelings for him."
    r "I do! But I’ve never acted on them for...a million reasons. And you’re one of them. One of the {i}biggest{/i} of all. I know how much you love him. And I’d never want to come between you two."
    c "But if he showed up tonight..."

    scene chikarinnice22
    with dissolve

    r "..."
    c "Would you have done it?"
    r "..."
    c "..."
    r "Yeah."
    r "I would have."

    scene chikarinnice23
    with dissolve2

    c "See?...Your hand is fine."
    r "You’re...not mad?"
    c "I’m not {i}mad,{/i} no. Just a little shocked, I guess. I thought you guys were just really close friends."
    r "We {i}are.{/i} That’s the {i}biggest{/i} reason this has been fucking eating away at me. I don’t want to fuck that up, Chika."
    r "At the same time though, I can barely even {i}think{/i} about him without all those feelings bubbling up anymore. It’s like how I used to look at you."
    c "I’m kind of sad you don’t anymore. That was really cute."
    r "Yeah, until you broke my heart into a million pieces. Which you were well within your right to do because you never felt that way about me."
    c "So do you think it’s “love?” Or are you just {i}really{/i} horny?"
    r "I think...I...don’t know what I think."
    r "I {i}do{/i} love him, though. But I love {i}you{/i} too. Which is why this is so fucking hard and so fucking confusing, Chika. I don’t know what to do."
    c "How long have you felt this way about him?"

    scene chikarinnice24
    with fade

    r "That’s...another thing I don’t really get."
    r "Like...I want to say it wasn’t until after Otoha, but...maybe it was way before that? Maybe I’ve had feelings for him this entire time? I don’t know. I really don’t."
    c "Do you want to know what I think?"
    r "So long as you’re not thinking about how you want to cut me into pieces for sending your boyfriend a five minute video of me masturbating."

    scene chikarinnice25
    with dissolve

    c "You sent him a video too?"
    r "Yeah! And my fucking {i}mom{/i} watched it! So that’s a thing I have to live with now!"

    scene chikarinnice26
    with dissolve

    c "Yeah, how’d you explain this to {i}her?{/i} She doesn’t think he’s in on it, does she?"
    r "I told her...mostly the truth about everything once I knew she saw the texts. But I lied to her about everything in the beginning, so I’m not sure if she believed me when I said it was all one-sided."
    c "Still, that really sucks. No phone? How are we supposed to talk while you’re at work now?"
    r "You still...want to talk to me? {i}Why?{/i}"
    c "Because I love you."
    r "But...wasn’t there a whole thing with Yumi before where you flipped out on her for just {i}thinking{/i} she was hooking up with Sensei? You love her way more than me and you almost killed her."
    c "I love both of you equally. That thing with Yumi was a combination of a colossal misunderstanding and me not knowing everything I know today."
    r "Well, what do you know today that you didn’t know then?"

    scene chikarinnice27
    with dissolve

    c "I know that love is {i}way{/i} more confusing and {i}way{/i} more complicated than it appears at first. And that’s saying a lot since it’s {i}already{/i} super intimidating."
    r "Well, maybe I {i}am{/i} in love with him then because confused and intimidated are definitely the most dominant emotions I’m feeling right now if you take away all the horny."
    c "No one takes away the horny. This is who we are now."

    scene chikarinnice28
    with dissolve

    r "Yeah, but {i}one{/i} of us is getting fucked with the intensity of a western silverback and the other has had to charge her vibrator like 10 times this week."
    c "What is it with you and this western silverback thing?"
    r "I really don’t know but I want it to stop."

    scene chikarinnice29
    with dissolve

    c "Rin, everything is going to be okay...Okay?"
    r "What am I supposed to do {i}now,{/i} Chika? Wait for this to all blow over? Just sit around and hope that someone else comes along that I want {i}more?{/i}"
    r "Because that sounds easy, sure. But things are different with Sensei. I {i}know{/i} him. He’s not some girl I saw in middle school or a park and just decided to become obsessed with."
    r "This happened over time. And every day, it feels like it’s only getting stronger."
    c "Rin-"

    scene chikarinnice30
    with dissolve

    r "I fucking hate it, Chika! Why does it have to be {i}him?{/i} Why do I have to compete?!"
    c "Rin-"
    r "I don’t even have a {i}phone{/i} now! And Sensei’s definitely going to find out about this one way or another, so {i}that’s{/i} going to be a thing I need to figure out how to deal with."
    r "Which isn’t even mentioning how my {i}other{/i} mom is going to learn! And I can only imagine how {i}that{/i} is going to go since {i}she’s{/i} the strict one!"
    c "Rin-"

    scene chikarinnice31
    with dissolve

    r "I’m just fucking exploding inside and I don’t know how to handle it! I’m used to feeling {i}nothing,{/i} not this! I hate it! I fucking hate it, Chika! For once in my life, I {i}want{/i} to feel numb! But this just keeps growing it-"
    c "Rin."

    scene chikarinnice32
    with dissolve

    r "What?! I’m not done ranting!"
    c "Lie down."

    scene chikarinnice33
    with dissolve

    r "Huh? Why? You might not hate me right now, but I’m still not going to let you cuddle with a girl who would have fucked your boyfriend if he came here tonight."
    c "That’s fine. I wasn’t planning on cuddling in the first place."
    r "Then what-"

    scene chikarinnice34
    with dissolve

    c "{i}Lie...down...{/i}"
    r "..........what?"

    play sound "static.mp3"
    scene chikarinnice35 with flash
    stop sound
    play sound "tackle.mp3"
    with hpunch

    r "Uhhhhhhhh whaaaaaaaat are you doing???"
    c "You love me, right?"
    r "I...uhh...yeah! But-"
    c "Then just trust me okay?"
    r "Trust you with {i}what?!{/i} What do you-"
    c "Your shirt’s in the way. I’m gonna move it."
    r "You’re going to what?!"

    play sound "static.mp3"
    scene chikarinnice36
    with flash
    stop sound

    c "Chu~"
    r "{i}Ah!{/i} Oh my God...Chika! Hold on! I’m confused!"

    scene chikarinnice37
    with dissolve

    c "About what?..."
    r "{i}This!{/i} You’re with Sensei! We’re just friends! My brain! Ah! Hold on! Stop!"
    c "You have goosebumps."
    r "Of course I have goosebumps! Who {i}wouldn’t{/i} have goosebumps right now?! But this is-"
    c "This is me taking care of you..."
    r "Y-Y-You don’t have to! You shouldn’t! You should punish me! I fucked up!"
    c "Okaaaaaay, then think of it as me punishing you instead. Does that work?"
    r "No! None of this works! Have you lost your-"

    scene chikarinnice38
    with dissolve

    c "Ahn~"
    r "Ooooooh my god! This can’t be happeniiiiiiing!"

    scene chikarinnice39
    with dissolve

    c "Like a dream come true, right?"
    r "Chika...seriously..."
    c "Bear with me, okay? I’ve never done this before."
    r "Chika-"

    play sound "static.mp3"
    scene chikarinnice40 with flash
    stop sound

    r "Aaah!"
    c "Chu...chu...chu~"
    c "Now your panties are in the way too. Excuse me, but I’ll be removing these now."
    r "Hah....oh....okaaay..."

    play sound "static.mp3"
    scene chikarinnice41 with flash
    stop sound

    c "Ahhh......ahhh.....ahnnn....."
    r "Hah...haah...hah...holy shit...hooooooly shit..."

    scene chikarinnice42
    with dissolve

    c "You’re so cute, Rin. I’m glad I get to see this face before Sensei does."
    r "Hah...ah...he’ll probably...never see it...at all! Nothing...is going to change!...I’m too...afraid!"
    c "I’d offer to call him myself so he can take care of you right now...but I think I just want you all to myself this time."
    r "You...what?! Chika, what the fuck are you saying?! None of this makes-"

    scene chikarinnice41
    with dissolve

    c "Ahn~"
    r "AAAH! HAH! CHIKAAAA! STOOOOP!"
    c "Sensei...ahn...and I...ahn...came to an agreement..."
    r "Hah...hah...you and Sensei...what? What...kind of...agreement?..."
    c "That...ahn...he gets to...ahnn...have any girl he wants...nnh...so long as he loves them...so long as...ahnn...he loves {i}me...{/i}the most..."

    scene chikarinnice42
    with dissolve

    c "So it’s only fair if I get to do the same, right?"
    r "Hah...hah...you guys...really...came to an agreement...like that?..."
    c "That’s why I said I changed. I’ve grown since then. And you know what, Rin? I’m happier now..."
    c "Because now I get to be with both of you."
    r "Chika...I’m {i}really{/i} confused right now...and this...I mean...I obviously like it-"
    c "Then enjoy it."
    r "Hah...hah..."
    c "Just turn your brain off...and give me everything."
    c "I promise to make you feel better."

    play sound "static.mp3"
    scene chikarinnice43 with flash
    stop sound

    "Try as she might, Rin Rokuhara couldn’t turn her brain off. She couldn’t even come close."
    "Because Chika was right — this {i}was{/i} like a dream come true. But it was a dream she dreamt long ago, before someone else began to take her place."
    "And yes, there were scattered fantasies here and there that’d pop up out of nowhere. Chika was {i}still{/i} Rin’s type, after all. She was {i}always{/i} going to think things."
    "But she’d settled into her role as a good friend. A potential lover who never struck when the iron was hot enough."
    "But now {i}she{/i} was the one being struck, and she couldn’t tell if she was high on the sensation or delirious from blunt force trauma."

    c "Mnch...mmm...mlm...Rin...you’re so fucking cute...I love you so much...and you taste...so fucking good...mmnh...Rin...Rin!"
    r "....................................."

    "She...{i}was{/i} enjoying it."
    "Wasn’t she?"
    "The fantasies of {i}him{/i} had gone. But despite how desperately she tried to force them away just an hour ago, she was now trying to force them {i}back.{/i} Because {i}this{/i} somehow felt worse. It felt wrong."

    c "Mmh...mnn...mmmmmgh! Mmnmmm...mlm...."

    "Was it {i}supposed{/i} to feel wrong?"

    c "Maybe next time...mmn...you can join us...mnh...Sensei and me..."
    c "I’d love to see...mnh...the look on your face...while he pounds your...cute little pussy...{i}God...{i}you seriously are...so adorable...Rin..."
    r "............."

    "Despite the irrefutable pleasure bubbling up within her, she was unable to find any words."
    "She {i}wanted{/i} to grab Chika’s head...run her fingers through her hair...hold her in place to assist her...but her arms wouldn’t move."
    "{i}Nothing{/i} was working. She just laid there as a girl she {i}really{/i} loved {i}really{/i} loved her back."
    "And it was at that moment when she realized she never really {i}loved{/i} Otoha at all."
    "Only Chika could make her feel this way."
    "Chika and...{i}someone else,{/i} she thought."
    "Someone who wasn’t here."
    "Someone who...shouldn’t come here."
    "Someone wrong. Someone old. Someone unfaithful. Someone lecherous. Someone it was never hard to come up with negative adjectives for because it was someone who took pride in that."
    "Chika was none of those things. At least not at first. But lately, she’d begun to change. And this added one more stick of dynamite to the volcano of confusion incessantly erupting within Rin’s head."
    "Was this Chika at all? Or was it someone she didn’t know?"

    r "........."
    c "Mmnnh...mnh....mlm....mmm!"
    r "........"

    scene chikarinnice44
    with dissolve2

    c "Ahhn....aahhnnn....."
    r "......"

    scene chikarinnice45
    with dissolve

    c "Do...uh..."
    c "Should I stop?"
    r "Huh? What?"
    c "You just...look kind of..."
    c "Am I, like...{i}bad{/i} at it? Because I told you it was my first time and I-"
    r "No! No! You’re not bad. You’re...uhh...it feels...{i}really{/i} good..."
    r "I’m just...I feel like...you don’t...{i}want{/i} to do this and are just...you know..."

    scene chikarinnice46
    with dissolve

    c "I want to."
    r "Because...it’s {i}me?...{/i}"
    r "Or because you...let Sensei do the same?..."

    scene chikarinnice47
    with dissolve

    c "..."
    r "I’m sorry! I...shouldn’t really be asking questions when you’re just...trying to make me feel better. But...you know...it’s just...so {i}much{/i} is going on right now and-"
    c "I wouldn’t do this for anyone else, Rin."
    r "L...Liar...You’d do it for Yumi."

    scene chikarinnice48
    with dissolve

    c "Nch...mnh...nope. Yumi...mnh...doesn’t shave. You’re mhn...much cuter down here than her...."
    r "{i}Ah!{/i} Chika...what...does this {i}mean?...{/i}How do I...take this?..."
    c "You...mnh...shut up and {i}take{/i} it...mnh...that’s how..."
    r "Y-Yes! But for me to finally realize I like someone else and then have the biggest crush of my life go down on me out of nowhere?! My brain isn’t developed enough to process that!"
    c "So...nhn...don’t..."
    r "What?..."
    c "Love...is complicated...mnh...remember?..."
    c "Choose...mnh...both of us..."
    r "I..."
    r "Uh..."

    scene chikarinnice49
    with dissolve

    c "Just be mine for tonight...okay?"
    r "..."
    c "..."

    scene black
    with dissolve2

    r "Okay..."

    play sound "static.mp3"
    scene chikarinnice50 with flash
    stop sound

    "And so she did. So she was."
    "Chika managed to bring Rin to orgasm four times that night."
    "The first three times were with her mouth alone. The fourth required the aid from the index finger on her right hand."
    "Rin sheepishly offered to return the favor once all was said and done, but Chika rejected her."
    "It looked something like this."

    play sound "static.mp3"
    scene chikarinnice51 with flash
    stop sound

    r "Hah...haah...oh my god...I can’t...no more...please...no more..."
    c "That’s it? Sensei and I normally go all night long."
    r "Ahh...ah...well...I’m not...Sensei..."
    c "You’re right. Sensei wouldn’t blueball me like this. He makes sure I cum {i}eeeevery{/i} time."
    r "Mnh...are you...bragging...now?"
    c "Nooooo. Just giving you a little hint."
    r "I..."
    r "Um..."
    c "..."
    r "Chika-"

    scene chikarinnice52
    with dissolve

    c "It’s fine."
    r "No! I’ll do it. I just...um..."
    r "Otoha was normally the...uhh...{i}aggressor...{/i}so I’m...probably...not very good at...at anything you...want me to...that, um..."

    scene chikarinnice53
    with dissolve

    c "Pfft!"
    r "D-Don’t laugh! I am having a...very difficult and...weirdly...good...night...now?"

    scene chikarinnice54
    with dissolve

    c "Me too."
    c "Don’t worry about it, though. I can finish myself off next door. I’m more than happy just getting {i}you{/i} off. Multiple times."
    r "It’s...I mean...I {i}want{/i} to do it. I do. But I-"
    c "Do you feel better?"
    r "Huh?"
    c "I {i}said...{/i}do you feel better?"
    r "That’s...um...one way to...put it..."
    c "But you’re not gonna explode from being overly horny anymore? I helped you get it all out of your system?"
    r "Chika..."
    c "Do you feel better or not? Because I’ll go back down there. I swear. I’m not leaving until you’re okay."
    r "I’m...yeah. I feel better. I just...can I...ask you a question, though?"
    c "Of course. Anything for you."
    r "What..."
    r "{i}Are{/i} we?..."
    r "B-Because...you already have a boyfriend! And I..."

    scene chikarinnice55
    with dissolve

    c "Want the same boyfriend. I know."
    r "Y...Yeah..."
    r "So what does that make {i}us?{/i}"
    c "Best friends?"
    r "But Futaba is my best friend. And Yumi is {i}your{/i} best friend."
    c "Theeeeeeen...secret sex friends?"
    r "You...want to do this...again?"
    c "Of course. You currently owe me about four orgasms if my calculations are correct."
    r "But...we’re not {i}dating.{/i}"
    c "Welcome to the 2000’s, Rokuhara. If I knew you wanted to wait until marriage, I wouldn’t have gone down on you out of nowhere."
    r "I know! I know...I just..."
    r "Things with Otoha didn’t work because I wanted something serious and she didn’t, so..."
    r "If...this is just a...temporary thing, I...that’s fine! You can do...whatever you want. But, for me-"
    c "Whatever we are, let’s make a promise to stay together forever. That way, no matter what happens, we’ll never have to worry about saying goodbye."
    r "..."
    c "Sound good...Rokuhara?"

    scene black
    with dissolve2

    r "S...Sounds good..."
    r "Chosokabe..."

    $ renpy.end_replay()
    $ rinspring6 = True

    "{i}Rin’s affection with Chika hassss{b}ss$$$#&$#*(#$@#))#!!!!THISISNOTHOWTHEGAMEWORKS!!!!!!!{/b}{/i}"

    stop music
    scene colorbars
    play sound "colortone.mp3"
    $ renpy.pause(10, hard=True)
    scene black
    stop sound
    $ renpy.pause(2, hard=True)
    "{b}{size=+20}DEVIATION DETECTED{/b}{/size}"
    "{b}{size=+20}THIS IS NO NIGHT TO REMEMBER{/b}{/size}"

    if day == 1:
        jump advancetotuesch4
    if day == 2:
        jump advancetowedch4
    if day == 3:
        jump advancetothursch4
    if day == 4:
        jump advancetofrich4
    if day == 5:
        jump advancetosatch4
    if day == 6:
        jump advancetosunch4
    if day == 7:
        jump advancetomonch4

label dormwarsfiverin1:
    scene nightsky
    with dissolve2

    "Io and I manage to make our way back out of the tunnel without getting lost or encountering any other suspicious cliffs that lead to perpetual darkness."
    "She wants to stay together. And I do too. "
    "Was it the most conventional “date” I’ve been on? Obviously not. But it fit her well and, by extension, I guess that means it fit {i}me{/i} well too."
    "There’s somewhere else I need to be, though. With {i}someone{/i} else who’s been nothing short of a pillar of my unfortunate existence for as long as I’ve been here."
    "That pillar is on the precipice of crumbling now, unfortunately. "
    "And it’s one that I imagine will {i}have{/i} to come up today if we’re ever going to keep it from collapsing."
    "I just wonder how the conversation is going to go. And I wonder how much of it is {i}real{/i} and not just one more impulse on an ever growing list of things that she regrets."

    scene black
    with dissolve2

    "Io and I say our goodbyes outside of the cafe and she leaves to go meet back up with Uta."
    "She wants to kiss me again, but I deny her — not wanting to be spotted by my second date, who’s likely watching us from the other side of the window."
    "I am sure this will not have any negative effect on Io’s already lackluster self-esteem whatsoever."

    play sound "static.mp3"
    scene rincafehairwoah1 with flash
    stop sound
    play music "cafe.mp3"

    r "Greetings, sir! Welcome to Koi Cafe! Will you be dining in or taking your order to go?"
    s "..."
    r "Excellent! Just so you know, our special for today is “whatever I want to make you.” May I mark you down for one or two?"
    s "..."
    r "And will you be having that hot or iced? "
    s "..."
    r "Got it! Please wait one moment while I get everything ready for you. "
    r "You can go ahead and take a seat if you like. I can promise that if I {i}do{/i} use poison, which I will not confirm or deny, it will not be a lethal dose."
    s "What happened to you?"

    play sound "static.mp3"
    scene rincafehairwoah2 with flash
    stop sound

    r "Hm? Whatever do you mean, cherished customer?"
    s "I mean you were blonde less than 24 hours ago. And now you’re-"
    r "Beautiful? Cute? Awesome? "
    s "Normal."

    scene rincafehairwoah3
    with dissolve

    r "Normal?! I thought I looked pretty good as a blonde!"
    s "You did. You always do. Just {i}this{/i} is how I’m used to seeing you, so it’s the established baseline of what “normal” means to me."

    scene rincafehairwoah4
    with dissolve

    r "Well, that’s good. Because I did it for you."
    s "No you didn’t."
    r "No, I really did. The appointment I was talking about last night was for my hair."
    s "But you don’t-"

    scene rincafehairwoah5
    with dissolve

    r "I know I don’t {i}have{/i} to do anything and that the color of my hair has virtually no bearing whatsoever on our relationship. {i}But,{/i} and hear me out here-"
    r "I think I am tired of changing so much. And I think I am finally ready to commit to one thing for good. And that thing, you may ask?"

    scene rincafehairwoah6
    with dissolve

    r "Being {i}your{/i} homie! Which means returning to my homie roots with homie hair! And {i}you{/i} get to be the first one to witness this transformation!"
    r "Besides Haruka since she is also working right now and I needed her help clocking in earlier."
    s "So, you’re...dedicating yourself to being my friend? And this has nothing to do with your newfound desire to want me to-"
    r "Don’t say it."
    s "{i}Ahem.{/i}"
    r "Don’t do it, Sensei. I know what’s coming."
    s "{i}Pound you with the intensity of a western silverback.{/i}"

    scene rincafehairwoah7
    with dissolve

    r "Can homies not do things like that together?"
    s "They can, I think. They just don’t normally find out about it from their homie’s mother."

    scene rincafehairwoah8
    with dissolve

    r "To be fair — you {i}would{/i} have found out about it from me if you actually kept your phone on you. And {i}I’d{/i} probably be pregnant right now."
    s "So you’re just gonna...roll with it? Not get all embarrassed and weird like you do any time you’re talking to someone else you have a crush on?"
    r "I gain flirty super powers when I’m behind this counter. It’s a barista thing. Earns me more tips. Anyway, yeah. That is a thing that happened. {i}But...{/i}"
    s "But?"
    r "I was {i}very{/i} horny that night. Destructively so. And you know better than most that it is hard to act rationally under such circumstances. Which is why I have a proposal."
    s "I’m listening."
    r "Today, we will both go through this entire date wearing blindfolds. That way, the horny will not reach us."
    s "Proposal rejected."

    scene rincafehairwoah9
    with dissolve

    r "Shit. I guess we’ll just have to hang out like normal then and put the homiedom in jeopardy. "
    s "Well, that’s the whole point of a date, isn’t it? Shouldn’t you {i}want{/i} to be putting the homiedom in jeopardy right now so you can win the war?"

    scene rincafehairwoah10
    with dissolve

    r "War?"

    scene rincafehairwoah11
    with dissolve

    r "Oh! Right, that. "
    r "Yeah, I don’t really care."
    s "What?"

    scene rincafehairwoah12
    with dissolve

    r "I’m mostly just excited to hang out with you and I’m using the pretense of the date war as an excuse to do that since we haven’t just chilled in what feels like forever."
    r "I don’t have anything special planned and don’t mind losing if you don’t wind up choosing me. I just want to spend time with you and make things feel normal again."
    r "You don’t mind, do you?"
    s "Not at all...I think I’d like that too, actually."

    scene rincafehairwoah13
    with dissolve

    r "Cool! I’m gonna go say bye to Haruka and clock out then. She said it’s okay for me to bail whenever. She just wants to know when it happens so she can take over."
    s "Okay, yeah. I guess I’ll just...wait here then."
    r "Mhm! Be back in a sec!"

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Rin disappears into the kitchen and returns with Haruka a minute or two later."
    "Before I have a chance to greet her and feign an apology for stealing her employee, though, Rin races out from behind the counter and grabs my arm, pulling me to the door."

    r "Away, homie! I will not let my work mom’s boobs deprive me of the opportunity for quality time!"
    s "Our time together isn’t in jeopardy at all if we just stare at them {i}together.{/i} "
    r "Ooh, good point. Haruka — could you jump up and down for us really quick?"
    h "What? No. That’s completely objectifying and-"

    if harukasex == True:
        s "Do it."
        h "Yes, [harukamaster]."

        "I use my powers for evil once more and Haruka has no choice but to obey."

        r "Woah. Look at ‘em go."
        s "I have too much power now. This isn’t fair."

        "Rin and I only spend a good thirty seconds watching Haruka objectify herself before turning around and leaving her there to bounce on her own for the rest of eternity."

    else:
        s "Rin, come on. That’s a married woman you’re talking to."
        r "But the boobs! You were on my team just a second ago! They must- aah!"

        "I yank Rin by the arm to prove to her that I’m actually a good guy and that the fact that I’m sleeping with basically all of her classmates does not undermine my moral code."

    scene rincafehairwoah14
    with dissolve2
    play music "thesleepingcity.mp3"

    "Then, before long, we’re right outside of the dorms. And everything feels somewhat normal again, just..."
    "That normalcy is now laced with the open admission that there {i}are{/i} more potent feelings present. Which is something I’ve always had to just assume until now."
    "It’s not changing her, though. At least not in the ways it historically has. Which makes me unsure of whether or not this is some sort of bluff or..."
    "Maybe I {i}am{/i} special?"
    "Because she is to me, right? It’s not just her hair that’s making me nostalgic. It’s all of this. "
    "The cafe banter. That feeling of the air going cold as the lights start to come on outside of the dorms."
    "That infectious smile and the way her ponytail bounces when she walks. "
    "The subtle glances I get of her ears and the subsequent realization that I’m always forgetting they’re pierced. So it’s like I’m {i}always{/i} learning something new about her."
    "Even after all this time — she’s still not boring. She’s still Rin."

    r "Sooooo..."

    "But that doesn’t mean she isn’t changing too. I’m just conditioned to believe that change always comes with negatives now."
    "So this submission and {i}commitment,{/i} if that’s really what it is, puts me on edge and makes me want to grab ahold of her hair to stop it from bouncing and just..."
    "Keep her close to me."

    r "You’re kinda...more quiet than normal."
    r "Is it the hair? Did I go a little overboard in trying to...go back?"
    s "Why {i}do{/i} you want to go back, Rin?"

    scene rincafehairwoah15
    with dissolve

    r "Hm?"
    s "Are you not happy with the way things have been going? Do you think settling on me is going to make them somehow {i}better?{/i}"
    r "Yeah."
    s "...Why?"
    r "Because you’re the only one I feel like I can be myself with."
    s "..."

    scene rincafehairwoah16
    with dissolve

    r "No one else even knows I’ve changed my hair color back yet. "
    r "And I’m sure that’s probably going to make Chika a little sad, but...I realized something yesterday. And I realized it {i}because{/i} of her."
    r "So like, she was in the D&D contest, right? And she didn’t know anything about D&D so, being her friend, she asked me to teach her. And I was like, hell yeah. Let’s go."
    r "So I did. And it went...mostly well. But during the competition, when I was explaining stuff to her, she looked at me and she said “You’re cute.”"
    r "And I blushed. Obviously. I think I’ll always {i}kind of{/i} like her. But, when we got up from the table and went our separate ways, I felt...stupid."

    scene rincafehairwoah17
    with dissolve

    r "I spent {i}years{/i} hiding my nerdy side from Chika because I didn’t want her to think I was uncool. "
    r "But I never {i}had{/i} to do that. Chika’s one of the most accepting people I’ve ever met. And she’s never been anything but nice to me. "
    r "I did it anyway, though. And I did that because, for some reason, I felt like I had to {i}be{/i} someone to be with her."

    scene rincafehairwoah18
    with dissolve

    r "Same with Otoha. I was always thinking, “Oh my God, she’s so much cooler than me. I can’t show her who I really am.”"
    r "Even super personal stuff like my cutting I couldn’t really talk about with her because it just felt...wrong."
    r "But with you — none of that’s ever happened. I don’t feel like I need to change or {i}be{/i} anyone specific. I can just...be Rin."
    r "And I think maybe that’s okay now. Maybe I {i}should{/i} be Rin. And maybe you should be you and we should both just...be together."
    r "As friends...homies...something else...whatever."

    scene rincafehairwoah19
    with dissolve

    r "I’m trying not to think about it since thinking has never really worked out in my favor. "
    r "Mature, right? Am I finally cool now? Do I finally sound like an adult?"
    s "No. You still sound like a confused teenager."

    scene rincafehairwoah20
    with dissolve

    r "Damn. Thought I was finally onto something."
    s "It {i}is{/i} a mature way to look at things, though. Especially by your standards."

    scene rincafehairwoah21
    with dissolve

    r "Yeah?"
    s "Yeah..."
    s "It’s just the person you’re aiming those feelings at that makes me question whether or not I should put any stake in this sudden character growth."
    r "Then be like me. Try not to think about it."

    scene black
    with dissolve2

    r "Lets just...do nothing and see what happens for once."
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene rincafehairwoah22
    with dissolve2

    "We’re back in her room, where so much has happened. And for the first time since the last time I held her blood in place, it feels like I’m {i}supposed{/i} to be here."
    "I’m not a buffer now. Not someone for her to bounce her feelings for someone else off of to see how they’ll land. Just someone to sit with and...experience life with."
    "How long will it stay that way, though?"

    r "See that spot right over there? Where the alarm clock is?"
    r "That’s where I was standing when I got into an argument with my mom about wanting to have sex with you."
    s "Very cool, Rin. "

    scene rincafehairwoah23
    with dissolve

    r "And that chair? That’s where I was sitting when I was thinking about having sex with you. And then sending texts about the sex I wanted to have with you to you."
    s "I’d show you where {i}I{/i} was when I found out about all of this, but we’d need to walk halfway across town in order to do that. And I don’t think your mom would appreciate it."

    scene rincafehairwoah24
    with dissolve

    r "I kinda figured she was going to tell you. "
    r "I’m...really sorry about that. I’m not trying to, like...blow up your spot or anything. I know the last thing you need is people being suspicious about...you know."
    s "She’ll find out even worse eventually. Everyone will. It’s only a matter of time."
    r "Did she, like...like obviously she wouldn’t give you her blessing. But did she want you to like...{i}talk{/i} to me about it? Or..."
    s "I believe I’m supposed to “let you down gently.”"

    scene rincafehairwoah25
    with dissolve

    r "And?"
    s "And...what?"
    r "Will you?"
    r "Let me down gently."
    s "..."
    r "Let’s sit on the bed..."

    scene black
    with dissolve2

    r "Sensei..."

    "........."
    "......"
    "..."

    scene rincafehairwoah26
    with dissolve2

    r "Test failed."
    s "What?"
    r "Asking you to sit on the bed with me just seconds after talking about how I want to bone you was a test on whether or not you’re going to let me down at all. And you’re not."
    r "You love me too much. You’d never hurt your homie."

    if rinbetrayed == True:
        r "At least not nowadays. Not now that the guilt of having {i}already{/i} hurt your homie has eaten away at you."

    s "You’ve had no problem letting {i}me{/i} down gently, though. Multiple times too."
    r "Are you telling me you’ve wanted me this whole time? And that our entire friendship is built upon your desire to one day claim my boy-virginity?"
    s "Not {i}all{/i} of it. But I’d obviously be lying if I said I wasn’t frequently masturbating to you behind the scenes."
    r "That’s okay. It’s not as bad as me masturbating to you behind a curtain while you finger Sana."
    s "You should have joined in."
    r "I prefer my Sensei fully conscious, thank you very much. "
    s "You really are comfortable with me, huh?"
    r "I’d be more comfortable if you’d let me crawl inside of your skin and live there."
    s "Okay. You might be {i}too{/i} comfortable with me when you put it that way."

    scene rincafehairwoah27
    with dissolve

    r "Yeah. I guess my flirting could use a little work. Can’t exactly look up any nice pick-up lines without a phone, though."
    s "Do you know when you’re getting it back?"
    r "Another month or two maybe? I just hope I don’t get the Uta treatment and have mine blocked from sending pictures and stuff."
    r "Wouldn’t want to miss another opportunity to show my family a five minute highlight reel of my masturbation skills."
    s "I’d be willing to accept a live performance in lieu of a video, just FYI."

    scene rincafehairwoah28
    with dissolve

    r "Are homies {i}really{/i} homies if they’re not masturbating in front of each other?"
    s "I’m not doing anything like that. I’m just going to sit there and look cool while you go to town on yourself."
    r "Kinky. We should stop now, though. I’m starting to want you again. "
    s "I thought that was a given now? And what better time than the present?"

    scene rincafehairwoah29
    with dissolve

    s "We both {i}obviously{/i} want this. We’re on a “date.” We’re alone in your room. There’s no reason {i}not{/i} to. "
    s "You said it yourself just a little while ago. Let’s just see what happens. Why hold back at all?"
    r "Sensei, just because I can be myself around you and {i}obviously{/i} want to do stuff with you doesn’t mean I {i}should.{/i}"
    r "I literally {i}just{/i} got lectured on how dumb I am for wanting you in the first place. {i}You{/i} think I’m dumb for wanting you in the first place."
    r "That’s why this whole thing is a little confusing to me. You’re such an important person in my life and I don’t want to change that. I just {i}also{/i} really want to touch you."
    r "And I want you to touch me. Everywhere. Until I am sweaty and crying and convulsing from pleasures I have never felt before."

    scene rincafehairwoah30
    with dissolve

    r "{size=-2}I want that {i}so much,{/i} in fact, that if you were to push me down and have your way with me right now, I would happily oblige and then probably have an orgasm within ten seconds.{/size}"
    r "But don’t {i}you{/i} want something different?"

    stop music fadeout 10.0

    s "What do you mean?"

    scene rincafehairwoah31
    with dissolve

    r "Don’t {i}you{/i} think it’d be nice to have a relationship that doesn’t just flip a switch out of nowhere?"
    r "One that {i}seems{/i} impulsive, but is really just the result of two people with undeniable feelings for one another opening themselves up over time?"
    r "Because it’s easy to look at {i}us{/i} and think, “Oh — another high schooler with the hots for her teacher,” or “Another creepy, predatorial adult.”"
    s "Hey."
    r "But if that happens over a long period of time, it’s no longer impulsive at all. It’s sweet and cute and-"
    s "Grooming. What you are referring to is “grooming.”"

    scene rincafehairwoah32
    with dissolve

    r "Oh. Is that what that means?"
    s "Yes, Rin. And none of it is good. In fact, what you’re suggesting is kind of {i}worse{/i} in a way because {i}all{/i} people are impulsive. "
    s "And not everyone can see someone as wonderful and special as you and slowly corrupt them over a long period of time."
    r "Yeah. Good point."

    play sound "static.mp3"
    scene rincafehairwoah33 with flash
    stop sound
    play music "kimitoakinobouken.mp3"

    r "Guess we can skip all that buildup then and just cut to the part where our tongues are in each other’s mouths."
    s "..."

    scene rincafehairwoah34
    with dissolve2

    r "Why do you look scared? I’m me. And you’re you. Isn’t that enough?"

    if rinkiss == True:
        s "Because..."
        s "Because the last time this happened, you forgot about me."

        scene rincafehairwoah35
        with dissolve2

        s "And I don’t want that to happen a-"
        r "I never {i}forgot{/i} about you. Are you serious?"

        scene rincafehairwoah36
        with dissolve2

        r "There has not been a single day since then where you or {i}that moment{/i} has slipped by."
        r "If anything, I’d say it torments me even {i}more{/i} because {i}I’m{/i} the one who’s had to live with the guilt of depriving us both of something that could have been special."
        s "It’s not like I would have been loyal to you anyway. Which you probably knew back then. And {i}definitely{/i} know now. So calling it something that could have been special-"
        r "You don’t know if that’s the truth, Sensei.  You can’t."
        r "Like {i}yes,{/i} I’d have wanted loyalty. {i}Yes,{/i} I’d want you all for myself. But you can’t just assume that you’d make a mistake like that. "
        r "Like, it’s totally 100%% possible that we’d be a happy, monogamous couple to this day if I just kept focusing on you instead."
        r "If you want to call that a mistake, fine. If you want to call it a {i}regret{/i} even, fine! "
        r "But to say I {i}forgot{/i} about you ignores the fact that it hurt {i}me{/i} too. A lot. And that you will {i}always{/i} be my first kiss."
        r "Now, be my latest too."

    else:
        scene rincafehairwoah37
        with dissolve2

        s "It’s {i}too{/i} much. Too good to be true, even. I haven’t earned it. I don’t deserve it. Nothing about this is fair to you."
        s "And if we kiss here, or do anything else for that matter, all it’ll do is resign you to the same life everyone around you is suffering from."
        r "So you {i}are{/i} letting me down gently then?"
        s "I...don’t know what I’m doing."
        r "But you’re scared...aren’t you?"
        s "...yeah."
        s "I think I might be."
        r "It’s okay if you are. If you were to put your hand on my chest, I’m sure you’d feel it beating a thousand miles an hour right now."
        s "I’m not sure if you can measure a heartbeat in distance."
        r "Well, you’d change your mind if you felt mine. Regardless, this is what I want. {i}You{/i} are what I want."

    scene rincafehairwoah38
    with dissolve

    r "Though, I...{i}should{/i} probably give you the...{i}slight{/i} disclaimer that I, once again, think it would be best if we held off on it leading to...other stuff right now."
    r "I still...want to try and take it slow. You can call it grooming if you want. "
    r "I just think it’ll make for fonder memories if we can look back on this one day and realize how naturally we evolved. From friends to lovers."
    s "Can you actually love me, Rin? Like {i}really{/i} love me? As more than a confidant or homie or teacher or {i}anything{/i} like that?"

    scene rincafehairwoah39
    with dissolve2

    r "Don’t you want to find that out together?"

    scene rincafehairwoah40
    with dissolve2

    r "Sensei?..."
    s "..."

    scene rincafehairwoah41
    with dissolve2

    s "If you leave me for the next pretty girl who catches your eye, I will harvest {i}your{/i} skull and put it on display in my room."
    r "That’s the single most romantic thing anyone has ever said to me."

    scene rincafehairwoah42
    with dissolve2

    "Again, I find myself melting — this time with someone else."
    "But there is no ledge for my existence to slowly drip from this time, so Rin just has to absorb me."
    "And I think that, in a sense, she probably already has. And that the reason she’s so comfortable being with me is because a piece of me has already taken root in her."
    "I just hope it’s a big enough piece that she’s been able to build up an immunity to all of the harm she’ll incur by giving herself to me."
    "I don’t want to think about that right now, though."
    "I just want to sit here and do nothing. The same as her. In a place where we can just be ourselves. "
    "Which means- "
    "And I’m sorry to say this-"

    scene rincafehairwoah43
    with dissolve2

    "I’d like for you to leave us alone."

    r "Mlm...mmnh...mnh!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    r "Sen...sei...mnch...Sen...sei!"

    "Coffee tastes a little sweeter today."
    "I wonder why that is?"

    $ renpy.end_replay()
    $ dormwarsfiverin1 = True
    $ rin_love += 10

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump dormwarsfive11
