label church:
    if yasu_love >= 0 and ramen20 == True and church1 == False:
        jump church1
    if yasu_love >= 5 and church1 == True and church5 == False:
        jump church5
    if yasu_love >= 10 and yasudorm10 == True and day == 7 and church10 == False:
        jump church10
    if yasu_love >= 15 and chapthree8 == True and church15 == False:
        jump church15
    if yasu_love >= 20 and yasuspecial15 == True and church20 == False:
        jump church20
    if yasu_love >= 25 and predormwars3 == True and church25 == False:
        jump church25
    elif yasufirsthall == True and ramen20 == False:
        "I definitely don't think I want to go wherever it is that Yasu hangs out yet..."
        if day >= 6:
            jump satnightmenu
        else:
            jump asmenu
    if chap4active == True:
        jump yasuspringchurchgen
    if chapthreeactive == True:
        jump yasusummer2chapelgen
    else:
        jump churchgen

label churchgen:
    scene yasuchurchgen
    with fade
    play music "newhope.mp3"

    "I make my way through the late night smog of the urban district and wind up inside one of the worst places in Kumon-mi."
    "Yasu greets me with outstretched arms, as if wanting to embrace me."
    "But the second I move closer to her, she jumps back and begins to laugh maniacally."
    "Apparently, she does not feel the presence or the warmth of her god tonight, so physical contact is strictly forbidden."

    if bonus == True:
        "I'm not really sure what I was expecting, to be totally honest. But I'm not really all that fond of hugging anyway."
        "If the two of us are going to touch, I'd prefer it to be as loveless and passionately violent as possible."
        "There is no place for {s}God{/s} god in my relationship with her, despite what she both wants and believes."
        "But still, I continue to sate her appetite to be heard and swallow each and every faithful lie she spits out at me."
    else:
        "I'm a little upset that this includes hugging, but I still feel kind of weird about hugging Yasu anyway...so I guess it's okay."

    scene black
    with dissolve

    "{s}Praise be.{/s}"
    "I go home."

    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu's affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label church1:
    play sound "static.mp3"
    scene urbanparadise
    with flash
    stop sound
    stop music
    play music "sanctuary.mp3"

    "City lights, city lights. "
    "How do you fall asleep at night?"
    "Through stained glass panes, they shine so bright."
    "And kill the dark to grant us sight."

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    "I close my eyes and shut my mouth. "
    "I can not scream. I can not shout."
    "My limbs fall off where branches sprout."
    "Yet with no arms, I still reach out."

    play sound "static.mp3"
    scene urbanparadiseupsidedown
    with flash
    stop sound

    "The sky, it burns! It burns my eyes!"
    "My words ring out to no reply."
    "While one god lives, another dies."
    "When one descends, one more must rise."

    play sound "static.mp3"
    scene urbanparadise
    with flash
    stop sound

    "Hello."
    "I’m going to church tonight."
    "Or rather, a {i}cathedral,{/i} if we’re going by what the newspaper clipping Yasu gave me calls it."
    "{i}Godnote: A cathedral is kind of like a mega church that is run by a bishop, meaning that it’s more than just a standard place of worship.{/i}"
    "{i}Sure, you can still go there to say hi to God or whatever, but it’s also kind of like a headquarters.{/i}"
    "{i}Which also means that it’s easier to get away with horrible things there as it’s metaphorically towering over all of the smaller churches in the respective jurisdiction.{/i}"
    "{i}Cathedral...church...the name of the building doesn’t make much of a difference in the long run because it’s not like any of us will be kept there when we die.{/i}"
    "{i}I’ve heard stories of priests being stashed away in the basements of some places like that, though.{/i}"
    "{i}Which means that there’s likely a few cathedrals out there with basements overrun by flies, squeezing their way into caskets and laying eggs in the sockets of the holiest of holy.{/i}"
    "(End of godnote.)"
    "{i}Flynote: Standard house flies can lay over 500 eggs in a three to four day period of time.{/i}"
    "{i}They come in batches of anywhere from 70ish to 150ish and each measure up to around 1.2mm in size.{/i}"
    "{i}Their color is a yellowish white and if you put one in your mouth, you likely won’t taste anything.{/i}"
    "{i}Don’t take that as me granting you permission to go around eating fly eggs, though, you fucking weirdo. {/i}"
    "{i}Oh, sorry.{/i}"
    "(End of flynote.)"

    if bonus == True:
        "Anyway, I guess you’re probably wondering why I’ve decided to take it upon myself to come here instead of getting my dick sucked in one of several different girls’ rooms."
        "Me too."

    scene black
    with dissolve

    "Black."
    "Nine periods."
    "Six periods."
    "Three periods."
    "Dissolve."

    scene yasufirstchurch1
    with dissolve

    "I find the girl I expected to find sitting in front of the place I expected her to be sitting in front of."
    "My success rate in terms of identifying the respective locations of girls goes slightly up, but does not offset the countless other times I have searched to no avail."
    "But we are all searching for things to no avail."
    "Some people search for salvation."
    "While others search for strange things, like fly eggs to put in their mouths."
    "Both of those types of people will die horrible or slow deaths in hospital beds."
    "And any family members fortunate (Or unfortunate) enough to watch said passing will likely not even remember the number on the door they were kept in."
    "But life will move on and so will we."
    "So will I."
    "I move one step closer to the truth."

    scene yasufirstchurch2
    with dissolve

    "Yasu is too tangled up in some indiscernible paper web of words to notice my presence."
    "I doubt she receives visitors here very often."
    "Actually, I’m not even sure if I should be citing her as the entity who receives them."
    "If we have learned anything from the most recent Godnote, it is that cathedrals are run by bishops. "
    "And I do not think Yasu is old enough to be a bishop."
    "{i}Godnote #2: You must be at least 35 years old to be a bishop according to the Code of Canon Law (Canon 378 § 1, 3). {/i}"
    "Wow, thanks Godnote #2. I am learning quite a bit tonight."

    s "Hello, Yasu. "

    scene yasufirstchurch3
    with dissolve3

    ya "Huh?..."

    play sound "static.mp3"
    scene yasufirstchurch4
    with flash
    stop sound

    ya "Sensei! You came!"
    ya "The amount of joy I am feeling is indescribable! "
    ya "It courses through my veins! I can feel it curdling the blood inside of them with the happiest of clots! "
    ya "Like burning marshmallows bursting and oozing the righteous fluid of God himself!"
    s "That’s nice."
    s "What are you reading?"

    scene yasufirstchurch5
    with dissolve

    ya "Nothing particularly noteworthy. Just a book I obtained from the library."
    ya "Did you know that the standard house fly can lay up to 500 eggs over a three to four day period of time?"
    ya "Imagine if we, as humans, could lay that many eggs."
    s "We can’t lay any eggs at all, Yasu. We are mammals."
    ya "Live babies are like eggs, are they not?"
    ya "They must be closely monitored and cultivated until they can eat or move without the assistance of others."
    ya "Whereas many birds or insects are able to walk shortly after hatching."
    ya "In that regard, don’t you think those two things are a little better than human beings? "
    ya "Or at least far less worthless without the effort required to turn them into what we want them to be."
    s "They also cost a lot less to raise, I’m sure."

    scene yasufirstchurch6
    with dissolve

    ya "Do you have experience in raising children, Sensei?"
    s "I’m raising twenty of them right-"

    play sound "static.mp3"
    scene amiani16 with flash
    scene yasufirstchurch5
    stop sound

    s "Just one. My [niece]."
    s "Though I didn’t really start “raising” her until some...things happened."

    scene yasufirstchurch7
    with dissolve2

    ya "Did someone die?"

    play sound "static.mp3"
    scene yasufirstchurch4
    with flash
    stop sound

    ya "This is a church, Sensei. It’s okay to talk about the things that scare you here."
    ya "Both myself and {i}He{/i} are listening."
    s "I thought this was a cathedral and not a church?"
    ya "It used to be."
    ya "This building has not been used for its original purpose in quite some time."
    ya "It’s been abandoned for years now. Though, in its abandonment, it has saved the life of at least one girl."
    ya "You might know her. Her name iiiiiiiiiiiiiiiiis..."

    play sound "static.mp3"
    scene yasufirstchurch8
    with flash
    stop sound

    ya "Yasu! Woooooo! Yayyyy!"
    ya "The crowd goes wild!!!"

    "Yasu proceeds to make silly cheering noises for the next several seconds, likely expecting me to clap along or something like that."
    "But the truth is that my body feels rather heavy tonight. So heavy that just clapping alone might be enough to cause me to pass out."
    "But hey, at least if I {i}do{/i} pass out, she’d be here to take care of me."
    "I can’t guarantee that she won’t perform experiments on me while I’m out, but I can’t guarantee that Ami won’t do that either and I sleep in the same house as her nearly every night."

    s "So, are you going to give me a tour of the place? Or are we just going to sit out here and look suspicious?"

    scene yasufirstchurch9
    with dissolve

    ya "Hand of many clocks...father of all children...feed me your precious whispers of-"

    play sound "static.mp3"
    scene yasufirstchurch10
    with flash
    stop sound

    ya "God says no."
    s "What? What do you mean he says no?"
    ya "He seems...mad at you for some reason. "
    ya "He can be very temperamental at times. You’ve likely done something to offend him."
    ya "But you can gain his favor by coming back. I’m sure that the next time you arrive will be much more invigorating than this."
    s "So...I walked all the way to this weird, slummy part of the urban district to watch you read a library book?"
    ya "Hehehehehehehehe...yes."
    s "Welp, time to head back then."

    play sound "static.mp3"
    scene yasufirstchurch11 with flash
    stop sound

    ya "No! Don’t leave!"
    ya "Not before learning who we are and why we are here!"
    ya "There is still so much you can absorb by simply listening! "
    ya "The fact that His Holiness will not seep into your pores just yet does not mean you must give up!"
    ya "I implore you! Stay here and-"
    s "Holy shit, okay. Just stop yelling before someone comes over here."

    scene yasufirstchurch12
    with dissolve

    ya "Okay!"
    ya "But you don’t need to worry about that, Sensei."
    ya "In all of my time coming here, I’ve yet to see a single person enter the building other than me. "
    ya "Which is why I’m so very excited to finally have you here. "
    s "Even though I also can’t enter the building."

    scene yasufirstchurch13
    with dissolve

    ya "But you {i}will{/i} soon enough. "
    ya "The difference with you is that you can see it. The others can not."
    ya "To them, the torches are not lit. The glass is not stained. And the door is barred shut."
    ya "It’s nothing more than an old, abandoned building to the average person."
    ya "You and I have already transcended what it means to be average. Which means that we have what it takes to be saved."
    s "Correct me if I’m wrong, but wasn’t your pitch that night under the streetlight that your god accepts anyone willing to reach out or whatever?"
    ya "He does."
    ya "But the unfortunate truth is that even though there are so so so so so so so many people in Kumon-mi, only several of them have arms."
    ya "And of course not {i}all{/i} of those people with arms are going to reach out. So God becomes very sad watching them pass by."
    ya "He needs all the help he can get. Which is why I have devoted myself entirely to him."
    s "Well, you’re free to enjoy the missionary life, but I'd much rather not get involved."
    ya "Missionary is such a bad word. It has so much negativity glued to it."
    ya "And it also doesn’t apply to me as I haven’t been given a “mission.”"
    ya "I am simply a messenger relaying what she knows and what she has been told."
    ya "I can stop whenever I want to. "
    ya "But I don’t want to stop, Sensei. Not until His appetite has been filled."
    ya "Not until my body is flooded with the warmth of His love. "
    ya "Not until I can reach out and touch the light myself."
    s "Why can’t you, exactly?"

    scene yasufirstchurch12
    with dissolve

    ya "An excellent question! And one I am excited to answer."

    scene yasufirstchurch14
    with dissolve

    ya "You know the difference between boys and girls, correct?"
    s "..."
    s "Yes."
    ya "It’s customary in many religions for boys and girls to have different roles."
    ya "My role, as the purest of the pure and a devout follower of he who fills the well-"
    ya "Is to work hard and trust in His word."
    ya "To plant seeds all over the world and deliver the message of-"
    s "Wait, hold on. Isn’t that a mission?"

    scene yasufirstchurch15
    with dissolve

    ya "..."
    ya "Huh. I guess it is."

    scene yasufirstchurch16
    with dissolve

    ya "But I am still no missionary as I decided to do this all by myself!"
    ya "Essentially, what I must do is rid myself of all feelings and all desires."
    ya "I must act as a vessel for His warmth, which he will drip feed into me as if I’m connected to an invisible IV powered by my actions and my words."

    scene yasufirstchurch17
    with dissolve

    ya "You coming here tonight earned me a lot of IV fluid, Sensei. "
    ya "I feel warmer now than I have in a very long time."
    s "You’re...welcome, I guess."
    s "What about men? What's their role?"

    play sound "static.mp3"
    scene yasufirstchurch18
    with flash
    stop sound

    ya "You want to know?!"
    s "I mean, I wouldn’t have asked if I didn’t want to know."
    ya "It’s a very exciting role! One that only people like yourself can fill!"
    s "Trying to sell me on changing my beliefs just because I’d have an important role isn’t really going to do much, Yasu."
    s "I’m pretty set in my ways."

    scene yasufirstchurch19
    with dissolve

    ya "How unfortunate. I think you’d be quite good at it."
    s "And what is “it” exactly?"
    ya "{i}Transference.{/i}"
    s "...What?"
    ya "Filling your body with His warmth and moving it from one place to the next."
    ya "You see, girls are weak. "
    ya "Our bodies would simply explode if He gave us any more than a gradual drip feed."
    ya "But if you were to earn his blessing...you, too, could become a vessel."
    ya "One that transfers the greatest amounts of warmth from Him unto us."
    ya "And we would, in turn, cleanse ourselves of our desires and ask that you carry them back to him to be purified."
    s "Can I have a translation of that, please?"

    scene yasufirstchurch20
    with dissolve

    ya "Hehehehehehehehehe..."
    ya "Hahahehehehhaahhehahehehe..."
    s "That isn’t-"

    play sound "static.mp3"
    scene yasufirstchurch21
    with flash
    stop sound

    if bonus == True:
        ya "Sex! "
        ya "Lots and lots of sex!"
        ya "Girls plant the seeds and boys provide them! That is His wish!"
    else:
        ya "(Airplane noises)"
        s "Oh, okay. I understand now."

    scene yasufirstchurch22
    with dissolve

    if bonus == True:
        ya "Without you, what am I to deliver?"
        ya "How can I remain enthusiastic about His love if I feel that love dwindling with every passing moment?"

    ya "God is dying, Sensei."

    if bonus == True:
        ya "Do you understand why you are needed now? How important your role could be?"
    else:
        s "So I've heard."

    play sound "static.mp3"
    scene yasufirstchurch23
    with flash
    stop sound

    ya "And all you have to do is believe in order to be blessed."
    ya "That doesn’t sound very hard, does it?"
    s "I mean...no."

    if bonus == True:
        s "This might actually be the first time a religion has ever had some sort of appeal to me."
        s "It just comes as a bit of a shock since you already said all that stuff about no romance and blah, blah, blah."
        ya "Transference has nothing to do with romance, Sensei. It’s taking one important resource and putting it where it belongs."
        ya "It’s entirely practical."
    else:
        s "I just don't really have any idea what to believe in since you keep making airplane noises."

    scene yasufirstchurch24
    with dissolve

    if bonus == True:
        ya "But I bet it feels really...{i}really{/i} good."
        ya "To think of how hot the insides of my body would be as they fill with His love..."
        ya "It almost makes me think things. Things that someone as pure as me should never think."
        s "Sorry for just throwing this out there, but..."
        s "Did you make this religion up or something?"
        s "Kind of weird that I've never heard about it before if the main perk is getting to have lots of sex."
    else:
        ya "You mean like this? (Airplane noises)"
        s "Yes, exactly like that."
        ya "I'm speaking a special language."

    scene yasufirstchurch25
    with dissolve

    ya "I’m certain you’ve heard of it. Even experienced some of it if the whispers I hear are correct."
    ya "You just didn’t know how it worked."
    ya "But now you do. Because I was told to tell you."
    ya "And I do hope that you’ll consider learning more about it in the future."
    ya "The end of the world is coming. And it is my job...no."
    ya "It is {i}our{/i} job to save as many souls as we possibly can."
    ya "Please help me. "
    ya "All you need to do is open your eyes."
    s "Open my-"

    scene black
    stop music

    "I wound up leaving some time after that conversation ended, but I don’t remember when."

    $ renpy.end_replay()
    $ yasu_love += 1
    $ church1 = True

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
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

label church5:
    stop music
    scene churchglow1
    with dissolve2
    play music "newhope.mp3"

    "A mysterious girl stands before a mysterious altar inside of a mysterious building in a mysterious part of town."
    "She was not waiting outside the same way she was the last time I came here, which I suppose means that today I am allowed to enter."
    "And, on the off chance that I am not, let {s}God{/s} god smite me with all of {s}His{/s} his wrath."

    play sound "static.mp3"
    scene p1 with flash
    scene p2 with flash
    scene p3 with flash
    scene p4 with flash
    scene churchglow1 with flash
    stop sound

    "I feel something touch me, but not long enough for me to get accustomed to the sensation. "
    "Not long enough for me to fall in love with it and have dreams of growing old together."
    "To have dreams of those celestial hands decaying with the passage of time."
    "To watch the skin wrinkle and the veins protrude."
    "One of my favorite things about older people is that it becomes easier to see the insides of their bodies without having to work for it."
    "Like their entire vascular system is laid out like a placemat, decorating wherever they may go with a display more beautiful than any work of art could ever possibly be."
    "Or hideous, depending on the way you look at things."
    "Let’s talk about perception for a moment."

    play sound "static.mp3"
    scene p1 with flash
    scene p2 with flash
    scene p3 with flash
    scene p4 with flash
    scene churchglow1 with flash
    stop sound

    "Let’s not talk about perception."
    "Let’s talk to Yasu instead."

    ya "Blessed be those who give up their eyes. "
    ya "Who give up their mouths. "
    ya "Who give up their lives."
    ya "Blessed be those who see in the dark."
    ya "Who cut off their tongues. "
    ya "Who sleep in the ark."
    ya "Come to me, Father. Come to me, Mother. "
    ya "Come to me sisters, and cousins, and brothers."
    ya "A life without light is life left unlived."
    ya "A life filled with God is a life to forgive."
    ya "Praise be."
    s "{s}Praise be.{/s}"

    "I suppress a strange desire to cry out. "
    "The air in the room is cold and stale. "
    "It smells of mold masked by scented candles, but the unlit kind that don’t carry with them the same level of warmth and comfort that the burning ones do."
    "As such, it’s not very pleasant."
    "To disguise something unfavorable with something that {i}is{/i} favorable is akin to denial. "
    "And denial makes us weak."
    "But it’s such a strong tool."
    "Here is a list of other strong tools:"
    "Hammer "
    "Power Drill"
    "Power Hammer (Probably not a thing, but it would be cool. Just think of how many nails you could drive in.)"
    "Saw (Various types)"
    "The pen (Artistic answer. Don’t actually use a pen in a fight. You will lose.)"
    "(Try using a Power Hammer™ instead)"
    "And religion."
    "Religion is actually the strongest tool out there."
    "Because not only can you use it to justify anything and everything you could possibly want, you can also use it as a scapegoat when things go wrong."
    "If God made you do it, is it really your fault?"
    "That phrase is so powerful that even those who stray from religion break it out from time to time. "
    "And I’m not just talking about those same people who only pray when things get bad. "
    "But I guess, in a sense, those people are worth mentioning here as well."
    "That’s how strong of a tool religion is."
    "Regardless, I don’t think it’s fair to compare Yasu’s religion to any of the commonly scapegoated ones as she, at least to my knowledge, is the sole follower of it."
    "But I’m sure that won’t prevent her from using it as a tool to garner favor or dodge blame in the future."
    "Thankfully, the future is a long way from here. But also on top of us at the same time."

    if bonus == True:
        "It’s pinning us down by our shoulders and shifting our panties to the side, preparing itself to ruthlessly violate our perception of-"

    play sound "static.mp3"
    scene p1 with flash
    scene p2 with flash
    scene p3 with flash
    scene p4 with flash
    scene churchglow1 with flash
    stop sound

    "Let’s not talk about perception."
    "Let’s talk to Yasu instead."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene churchglow2
    with dissolve

    ya "My, my...what a pleasant surprise."
    ya "To see another face inside of the church is nothing short of a dream come true for me. "

    if bonus == True:
        ya "Did you bring the whip?"
        s "Uhh...what?"
    else:
        ya "Did you bring the Cool Whip?"
        s "Are you baking a pumpkin pie?"
        ya "No. I am going to drown you in it."
        s "What?"

    scene churchglow3
    with dissolve

    ya "A joke, of course. Violence is not something we take lightly here."

    if bonus == False:
        s "That was a very bad joke, Yasu."

    scene churchglow2
    with dissolve

    ya "You are safe within these walls."
    ya "And even if it feels like everything is caving in, or that the floor wants to open up and swallow you whole, you will be okay."
    ya "Only good things happen here."
    s "This place is fucking weird, Yasu."
    ya "Weird? How so?"
    ya "What makes it any different than another place of worship?"
    ya "We have candles, religious symbols, benches-"

    scene churchglow4
    with dissolve

    ya "And now...people."
    ya "Oh, how wonderful it is to finally say that."
    s "Am I really the first person other than you who’s come in here?"

    scene churchglow2
    with dissolve

    ya "To my knowledge, yes."
    ya "Though I suppose it would technically be possible for others to wander in while I’m away at[school] or in my room."
    ya "I can’t be everywhere at once, of course. Omnipresence is a power of God and God alone."
    ya "Though, I do hope to become an angel one day."
    s "Don’t you need to just...die to become an angel? Isn’t that how it works?"

    scene churchglow5
    with dissolve

    ya "I’m sure there are some systems of belief that would say so. But things are a bit more complicated for people like me."

    scene churchglow2
    with dissolve

    ya "Do you remember when we last spoke of the differences between boys and girls?"
    ya "When I informed you of the wondrous role you could have if only you’d sacrifice yourself?"
    s "What do you mean, “If only?” That’s a pretty big caveat, Yasu."
    ya "Is it truly a caveat if you’re immediately reborn in the process?"
    s "I mean, I’ve definitely got some experience in the “being reborn” department and it’s not all that bad. "
    s "But still, yeah."

    scene churchglow6
    with dissolve

    ya "Hahahaha! So it {i}is{/i} true! "
    ya "Every day, you grow some more! "
    ya "You’re a truly wonderful person, Sensei. So gifted and handsome and funny."
    s "Flattery will get you nowhere, Yasu."
    s "Just kidding, it will get you everything you want. Please continue."

    scene churchglow2
    with dissolve

    ya "Perhaps another time. "

    ya "For it just occurred to me that I never finished explaining the role of the woman in all of this."

    if bonus == True:
        ya "You see Sensei, we’re not just entities meant to consume His love and spread His seed."
        ya "We are at first, but not in the end."
        ya "The truth is, if we work hard enough and make a big enough dent in the armor of older gods, we graduate and become “Angels.”"
        ya "Not angels in the traditional sense with eyes so bright that they could scorch you to death-"
        ya "But angels who decide who stays and who goes."
        s "Stays where and goes where?"
        ya "Here and there, I suppose."
        s "Informative. And how do you know this if you’re the sole follower of this weird cult thing?"
        ya "Because I can hear it."
        ya "The whispers. The rumbling. "
        ya "I can hear it."
    else:
        ya "You see Sensei...(Airplane noises)"
        s "..."
        ya "(More airplane noises)"
        s "..."

    scene churchglow4
    with dissolve

    ya "And even if I did not hear those things, I would still know them."
    ya "There are some things that you don’t need to see or hear in order to understand."

    play sound "static.mp3"
    scene churchglow7
    with flash
    stop sound

    ya "How to walk. How to blink. How to breathe. "
    ya "Like animals, human beings are born with this wonderful thing called instinct. "
    ya "We know how to do so many amazing things from the moment we escape our mothers, screaming and dripping with blood."
    ya "We don’t know where we are or who we are, but we know we exist."
    ya "We know that what we see is real and what we feel is real."
    ya "The only thing is, some of us feel a little more than others."

    scene churchglow8
    with dissolve

    ya "And some of us {i}see{/i} more than the others."

    play sound "static.mp3"
    scene churchglow9
    with flash
    stop sound

    s "So...let me just recap a few of the things you’ve said to me over the brief yet incredibly strange time we’ve known each other."
    ya "Please do~"
    s "The first time we met, you talked about how I have “seen God.”"
    ya "I did."
    s "Tonight, you are insinuating that I “see more than others.”"
    ya "Right again."
    s "But on like, four other occasions, you have told me I need to open my eyes."
    ya "Ding ding ding! You remember everything!"
    s "..."
    s "Sorry for just coming out and asking this but..."
    s "Are you on drugs?"

    play sound "static.mp3"
    scene churchglow7
    with flash
    stop sound

    ya "Not anymore. "
    s "What do you mean “not anymore?” That seems like a very important detail."
    ya "External forces like medications or narcotics slowly strip the sanity from your mind and your body. "
    ya "I am happier and safer now than I have ever been before."
    ya "Because now, nothing is held back. Nothing is suppressed."

    if bonus == True:
        ya "I can feel His glory and feel His warmth. "
        ya "And one day, I hope to feel yours."

    scene churchglow9
    with dissolve

    if bonus == True:
        s "What a strange way to come out and say that you want to have sex with me."
    else:
        s "What a strange way to invite me to prom."

    play sound "static.mp3"
    scene churchglow2
    with flash
    stop sound

    ya "What a strange way to interpret the desire to connect with another human being on a more spiritual level."

    if bonus == True:
        ya "Warmth does not strictly mean sex, Sensei."
        ya "I feel the warmth of God every day and am very much a virgin."
        ya "As such, I’d likely be able to feel yours without ever touching you. "
    else:
        s "Yasu-"
        ya "(Airplane noises)"
        s "..."

    scene churchglow10
    with dissolve

    if bonus == True:
        ya "But, of course, that does not mean we wouldn’t {i}be able{/i} to touch. Do you understand?"
        s "Not really. But I’m definitely interested in the touching part."
        ya "The touching part is a gift from Him and should not be the key interest here."
        ya "This is no joke, Sensei. The infusion of righteousness and the transfer of purpose from one body to another is not something that should be taken lightly."
        ya "To be pure as judged by the power of Him and Him alone is to rid yourself of love and desire so that he may consume them."
        s "Sex has nothing to do with love. It’s just an action."
        ya "An action that must be approved. "
        ya "For we are free to use our bodies to experience {i}that{/i} type of warmth with one another, but only when that warmth flows back into him."
        ya "Do you understand?"
        s "Again, no."
    else:
        ya "(Airplane noises)"

        "Why does this always happen to me?"

    play sound "static.mp3"
    scene churchglow11
    with flash
    stop sound

    ya "It is He who lives vicariously through our thoughts! Through our sensations!"
    ya "Why should {i}we{/i}, as less important, less virtuous creatures, feel the pleasures of life when He can not?!"
    ya "We must become one with the machinations of this world and all that lives within it so that it may all flow back into Him!"

    if bonus == True:
        ya "Each and every ounce of fluid transferred from one entity to the next without His blessing adds more to pain! It makes everything hurt!"

    scene churchglow12
    with dissolve

    ya "But when He gives us His blessing, He can feel what we feel."
    ya "It is all He has. He needs it to survive. He needs it to smile."
    ya "And when He smiles, we smile. I smile. "
    ya "Smile with me, Sensei!"
    s "I’m okay, thanks."

    play sound "static.mp3"
    scene churchglow2 with flash
    stop sound

    if bonus == True:
        ya "The act of human beings connecting on a physical level should be something witnessed before Him."
        ya "As an angel in training, it is my duty to abstain from any practice He would find abhorrent."

    ya "It is my duty to forego the realm of the senses so that each and every sensation can be used on someone much bigger than me."
    ya "I am a tiny girl, and yet this body feels so much."
    ya "I can only imagine how He, who encompasses all space, must feel."

    play sound "static.mp3"
    scene churchglow13 with flash
    stop sound

    ya "Sing me a song that reminds me of better days!"
    ya "Enter me and experience all that I am!"
    ya "Consume my thoughts and wrap yourself around my organs!"
    ya "Bask in the warmth that you have sacrificed so that we may live!"
    ya "When all others fail you, I will still be here! Feel it all through me!"
    ya "Feel everything through me! For I am yours and yours alone!"
    s "..."
    ya "Praise be!"
    s "..."
    ya "..."

    scene churchglow14
    with dissolve

    ya "He’s feeling shy tonight and doesn’t want to talk to me."
    ya "Probably because you’re here. "
    ya "But that’s okay. He is all powerful, but can act a little childish at times."
    ya "He’s still very young, all things considered."
    s "..."
    ya "..."
    s "Okay, well I think that’s enough for tonight."
    ya "Will you come back?"
    s "Probably. But not because I believe in your god."
    ya "Because I “entertain” you?"
    s "Because you “entertain” me."
    s "Goodnight, Yasu."
    ya "Goodnight, Sensei."
    ya "May the path you walk be free of callousness."

    scene black
    with dissolve2

    "I exit the church and walk out into the snow."
    "It’s somehow even warmer out here than it was in there."
    "I go home."

    $ renpy.end_replay()
    $ yasu_love += 1
    $ church5 = True
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label church10:
    scene black
    with dissolve
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    scene clearnightsky with dissolve2
    play music "newhope.mp3"

    "On nights like tonight, I find myself wandering somewhere between complacency and cowardice."
    "Trying to skirt the line between what it means to fall into form and what it means to break free."
    "But free from what?"

    if bonus == True:
        "The only thing preventing me from floating away is a small anchor surgically inserted into every girl I know. "
        "An anchor that grows as a direct result of how much “warmth” I give them, as someone like Yasu would put it."
        "With each orgasm comes an increased connection that will evolve into increased emotional damage depending on who finds out what and when."
        "And yet I stray..."
        "Further and further into the darkness that some see as light, with my hands clasped together. "

    "My fingers go to war with one another, using the sharp edges of nails to claw away at others who look just like them on the opposing side."

    if bonus == True:
        "A whole other world, though not at all dissimilar to the one they’ve spent 31 years familiarizing themselves with."
    else:
        "A whole other world, though not at all dissimilar to the one they’ve spent 5,000 years familiarizing themselves with."

    "That’s the overly intellectual, artistic way of saying that I begin to pick at my nails."
    "I lose track of how hard I must be doing it and manage to cut myself."
    "Blood flows out."
    "Not a lot of blood. But enough to remind me of the color of my [niece]’s hair. "
    "Hers is a lighter shade of red."
    "Just like [[redacted]."

    scene yasublind1
    with fade

    "I make my way into New Hope Cathedral and attempt to shake off any uneasiness that may have snuck into my mind on the journey over."
    "The walk isn’t as bad as the one I so commonly take to the second half of town."
    "In fact, coming here allows me to pass through several locations that make the cold seem not that cold at all."
    "Some nights, when the temperature is low enough, I like to watch the exhaust fumes from the pipes of closing restaurants clash with the winter wind and explode into gray vapor."
    "I like to walk through it, half expecting to feel something, but remembering as I pass through that I, too, am vaporous. "
    "And that the reason I can not feel is not that there are no feelings to be felt, but that I have already felt them all."
    "There is nothing left for me here."

    ya "Blessed be those who give up their eyes."
    ya "Who trade in their sight for the sake of a prize."
    ya "Blessed be those who reach out their hands."
    ya "Who sit in the church, so outside He can stand."
    ya "Good morning, Sensei."
    s "You could tell I was here?"

    play sound "static.mp3"
    scene churchglow1 with flash
    scene yasublind2 with flash
    stop sound

    ya "Of course."
    ya "The door isn’t exactly quiet. "
    ya "And it’s not like anyone else has ever visited me here before."
    s "Right."
    s "So...are you having fun?"
    ya "Not at all."
    ya "I am barred from having fun tonight, you see."
    ya "And so I shall sit here, thinking nothing. Seeing nothing. Being nothing."
    ya "All so He can feel what it means to be alive once more, if even for a fraction of a second."
    s "Well I guess I better go then. I’m a really exciting guy and don’t want you to accidentally enjoy yourself or anything."
    ya "There’s no need to go anywhere, Sensei. I can talk."
    ya "In fact, I’d love for you to stay and chat."

    if bonus == True:
        ya "Though, I implore you not to look at me or attempt to take advantage of me."
        ya "I’m rather defenseless tonight."
        s "You’re barely over five feet tall and I’m pretty sure I could snap you in half with one arm."
        s "You’re rather defenseless every night."
        ya "Hehehe~ "
        ya "Yes. I suppose you’re right about that. "
        ya "But that’s not what I am talking about. "
        ya "Please, take a seat."
    else:
        ya "Do you understand my language yet?"
        ya "(Airplane noises)"

    s "..."

    if bonus == False:
        ya "(Airplane noises again)"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yasublind3
    with dissolve

    s "..."
    ya "..."
    s "..."
    ya "Feel free to sit down whenever you like, Sensei."
    s "I’m right next to you."
    ya "Oh. I’m very sorry. You were much quieter than I anticipated."
    s "Yasu."
    ya "Yes?"
    s "I’m really going to need an explanation for this."
    ya "You wish to learn more about he who sleeps?"
    s "I wish to learn more about Yasu who blindfolds herself with tape in the middle of a church at night."
    ya "A much less interesting story, though one I’d be happy to tell."
    s "Please keep it as minimally propagandic as possible."
    ya "Hehehe~ "
    ya "Of course."
    ya "I doubt this aspect would convert you to a believer either way. "
    ya "It is simply how we show our thanks."
    s "How {i}you{/i} show your thanks."
    ya "For now."
    ya "More will come, if they do not already exist."
    ya "They could always be hiding as well."
    ya "I would not blame them if they were."
    ya "Have you ever wanted something you couldn’t have?"

    play sound "static.mp3"
    scene attempting with flash
    stop sound

    s "I-"
    s "..."
    ya "Actually, let me tell you a little anecdote that will explain things better than a simple question would."
    ya "A baby is born. There is no sense in giving it a name."
    ya "It is a normal baby. All of the parts are there."
    ya "The ears, the mouth, the nose, the limbs, the eyes. Everything."
    ya "But some of the parts don’t work."
    ya "If life worked the way a conveyor belt in a shop that mass produces dolls works, and this baby was to be a biomechanical retail product, those parts could be replaced."
    ya "If the arms bent the wrong way, it would receive new arms."
    ya "If the ears heard nothing but a high pitched noise, reminiscent of screeching tires or the whisper of melting plastic, those too could be replaced."
    ya "And while that much reigns true for humans to some extent, one thing that is almost always guaranteed is that those born blind will never see."
    ya "They can not comprehend the colors of the world. "
    ya "They can not gawk at the beauty of the sakura season, smiling as petals fall off of the trees and into their outstretched hands."
    ya "The baby in this anecdote refuses to accept that."
    ya "He grows older."
    ya "He lives for thousands and millions and billions and trillions of years and sees absolutely nothing."
    ya "He lives for so long that his notoriety grows and he becomes known around the world as the man who sees nothing."
    ya "Some people, whether it be through inspiration or pity, wind up surrendering their eyes to him in an effort to restore his vision."
    ya "His original eyes are removed in favor of the new ones, but none of them work."
    ya "The spare eyes are kept in a jar in his home, but the jar gains vision itself and must be put out of its misery."
    ya "He begins to sew the eyes to his body, thinking that maybe his brain would realize what he was attempting to do."
    ya "It realized nothing."
    ya "Eventually, the man was covered in eyes. And yet, he was just as blind as he was when he was born."
    ya "He accepts that he will never see and hides himself away in the depths of a sewer."
    ya "And he sleeps for years."
    ya "He becomes depressed and gives up on eating."
    ya "He dies."
    ya "But he lives for so long before that, covered in eyes to the point of being unable to move...that his other senses begin to dissipate."
    ya "The near deafening silence of a sewer in an abandoned town, where the only sound to be heard is the occasional drip of rain-"
    ya "He tunes it out."
    ya "The taste of the retinal fluid sliding across his tongue and down the back of his throat-"
    ya "He tunes it out."
    ya "All senses are numbed to the point where, when he passes onto the second plane, he does not even realize he has passed."
    ya "But that’s when something wonderful happens."

    play sound "static.mp3"
    scene yasublind4 with flash
    stop sound

    ya "He sees for the first time."
    ya "Not through his own eyes or the eyes that had been gifted and then sewn onto him, as those had all faded into nothingness with his descension."
    ya "But through the memories of the eyes of others, swimming through the air around him."
    ya "Each vision flowed into him. And in return, he shared himself with the visions."
    ya "It was then that he realized he was born as he was for a reason. "
    ya "That being born without vision was not a setback, but the mark of something beautiful."
    ya "Every year of agony was counteracted with a lifetime worth of wonderful sights."
    ya "The birth of all children. Fireworks in the summer. The long awaited sakura season."
    ya "He could smell the petals and hear the sizzle of grilled meat at food stands lining unfamiliar courtyards."
    ya "And yet it all felt so familiar."

    play sound "static.mp3"
    scene yasublind5 with flash
    stop sound

    ya "And then it stopped."
    ya "He had gotten a taste, but the taste vanished as quickly as it had appeared."
    ya "The whispers in the wind saw how quickly the man of many eyes was changing. Growing."
    ya "And it frightened them."
    ya "They started giving their memories to other people instead. "
    ya "People who were not lusting after the chance to start anew, but a chance to relive their lives despite hating so much of them."
    ya "This made the blind man sad."
    ya "But still, he held out hope."
    ya "He knew that one day, word of his story would reach someone."
    ya "Someone who would bridge the gap and connect him to the world."
    ya "But how?"
    ya "The answer to that question is why I am blind tonight."
    ya "I have foregone my own vision so that he may see in my place."
    ya "And I would forego it for the rest of eternity if it meant that he who suffers most would not have to suffer any longer."
    ya "But it does not work that way. "
    ya "I can only sacrifice my sight on nights like tonight."
    ya "Nights where we haphazardly wander between complacency and cowardice, skirting the line between our own comfort and the things we fear the most."
    ya "Do you understand now, Sensei?"
    s "..."
    ya "..."
    s "..."
    ya "..."
    ya "Sensei?"

    play sound "static.mp3"
    scene yasublind6 with flash
    stop sound

    s "Huh? What?"
    ya "Do you understand the reason for the tape over my eyes?"
    ya "I’m sure the anecdote sounded rather silly if you’re unfamiliar with the story I based it off of, but I’m happy with how accurate it was."
    s "I..."

    scene yasublind7
    with dissolve

    s "Yeah...sure."

    "Again, I managed to zone out while talking to Yasu. Though, this time, I’m pretty sure it was entirely out of boredom."
    "I’m not really one for long winded stories, let alone ones that go on to explain whatever weird religious purpose there is for blindfolding herself."
    "It’s probably just safe to assume it has something to do with that prayer she’s always whispering about giving up eyes."

    ya "Wonderful. "
    ya "If I were allowed to have fun tonight, I would jump for joy."
    ya "But unfortunately, I have to be available for God until he’s able to function on his own again."
    s "What do you mean, “function on his own?”"
    ya "He doesn’t handle the cold very well. It makes his legs lock up and his teeth chatter."
    ya "So I allow him to see through me when he wants to."
    ya "I do wish he’d call on me more often, though."
    ya "But I suppose that without many happy memories, there is only so much he can gain from peering into my looking glass."
    s "..."
    s "I feel like I should ask you to embellish on that “lack of happy memories” thing. That sounds important."
    ya "What is important right now is devoting myself entirely to Him."
    ya "This is His night. And all stories regarding Yasu Yasui must be shelved until that subsides."
    ya "Perhaps ask me again when the heat returns and I am free to switch colors."
    ya "But, until then-"
    s "May the path be a path or whatever. Yeah."
    ya "May the path you walk be free of callousness."
    ya "Thank you for visiting tonight."
    ya "I’m sorry I could not be as “entertaining” as I normally am."
    ya "But I need to focus or He will get angry."
    ya "And things get very loud when He is angry."
    s "Right..."
    s "Well, uhh..."
    s "Goodnight then."
    ya "Goodnight."
    ya "Safe travels."
    ya "Remember to sleep facing up tonight."

    scene black
    with dissolve2

    "I make my way out of the church and back into the street."
    "I walk by a local restaurant and move through the steam leaking out of its exhaust pipe."
    "I feel nothing."

    $ renpy.end_replay()
    $ church10 = True
    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label church15:
    scene urbanparadise
    with dissolve2
    play music "newhope.mp3"

    "The trip to Yasu’s church feels a little different in the summer."
    "Along with the cold comes a terrifying silence that unsettles my stomach with every sacrilegious step toward the sanctuary."
    "But the heat of this new season masks those sounds with a soundtrack of its own."
    "The silence has died. And in its place rests a barrage of endless insectual (A made up word not to be confused with “incestual” that pertains to the quality of being a [[or being created by an] insect) melodies-"
    "The creatures sing to me as if I am one of them. "
    "They sing to me as if to welcome me home."

    scene clearnightsky
    with fade

    "And in turn, I bend my legs backward and turn them into makeshift coils, springing into the sky like the world’s largest camel cricket and coming closer to the moon than necessary."
    "Its light reminds me of who I am and where I’ve been."
    "Its light reminds me of why I’m here and what I am to do next."
    "And so I take my coiled legs and unfurl them into the shapes I have grown familiar with."
    "Triangle. Circle. Triangle."
    "None of which you understand."
    "But to me, it makes perfect sense."
    "To me, this all makes perfect sense."
    "If it didn’t, I wouldn’t find myself amidst this INSECTUAL chorus with my mind half drowned in a bathtub full of honey while the rest figures out a way to float atop it."
    "I come close enough to the sky that I can smell the clouds, but the putrid stench of the cumulocirrus outlines of all of the things I have lost is enough to bring me back to the ground."

    scene black
    with dissolve2

    "It is enough to make me seek salvation in a way much different than I am meant to."
    "It is enough to have me curl my fingers around the handle of the door to a building in a city that houses a girl who I will one day fill with my light."
    "It is enough to remind me that I have always hated the summer."
    "And that I will continue to hate it until the day I die once more."
    "........."
    "......"
    "..."

    scene teaparty1
    with dissolve2

    "When I step inside, I am greeted by the sight of the girl I came to see electing to spend time with a colony of inanimate rabbits rather than someone actually capable of listening to her perpetual psychobabble."
    "Perhaps it is because they are incapable of running away like the rest of us do."
    "Or perhaps it is because somewhere, buried beneath all of the fluff and feathers or whatever it is they stuff inside of creatures like them is something that {i}can{/i} hear."
    "Perhaps they are creatures who {i}can{/i} feel."
    "I mean, we’re all stuffed with something, aren’t we?"
    "How is what’s inside of {i}us{/i} any better when {i}we’re{/i} the ones who will expire while they live on forever?"
    "Granted, this is all just hopeful conjecture bent into shapes that will make the girl I came to see look less damaged under the glow of the church lights."
    "Triangle. Circle. Triangle."
    "I can hear a god forming beneath the stone floor."

    ya "What’s wrong, Penemue?"
    ya "You’ve barely touched your eggs."
    ya "If you don’t clear your plate, you won’t be able to come to the white room with us."
    ya "That would be a terrible shame, don’t you agree?"
    ya "And you, Wormwood. You’ve had four whole glasses of tea today. Don’t you think that may be a little much?"
    ya "If you drink any more, you’re certain to get a tummy ache. And I’m afraid I am fresh out of dried papaya to help fix you."
    cre "..."
    ya "..."
    ya "Is that so? You brought your own?"
    ya "My, since when are you so responsible? "
    ya "Penemue could learn a thing or two from you."
    s "..."

    "I think about calling out to Yasu and putting an end to whatever weird charade this is but, at the same time, I can’t help but be fascinated by the way she speaks to them."
    "It’s different than the way she communicates with people- the way she communicates with {i}me.{/i}"
    "And, for lack of a better term (And I don’t mean to sound insulting), it makes her feel...human."
    "Much like the way her sudden interest in solo karaoke did at the Christmas party but, this time around, things actually seem to be a little {i}more{/i} depressing."
    "Though, that may just be because Touka isn’t here to dampen her infinite loneliness this time and that, instead, Yasu has taken to quelling that issue in a new way. One that-"

    ya "How long are you going to stand there for, Sensei?"
    ya "Haven’t you come to join the tea party?"
    s "...I didn’t realize you knew I was here."

    scene teaparty2
    with dissolve

    ya "The cathedral doors are rather loud. And Wormwood here hates the sound of insects that floods the room each time the doors are opened."
    ya "Please, sit down with us. The festivities are just getting started...and they have been looking forward to meeting you."
    s "The...stuffed animals have been looking forward to meeting me?"

    scene teaparty3
    with dissolve

    ya "Is that what you see?"
    s "Well...that’s what they are. So, yes."
    s "Also, what festivities? Is there actually some kind of reason for this...weird cathedral tea party thing?"

    scene teaparty4
    with dissolve

    ya "There is!"
    ya "It is our celebration of summer!"
    ya "A new coming of our humble god is upon us. And we have gathered here today to welcome Him and drink in His love!"
    ya "This tea was brewed with water fresh from the basement ceiling and leaves gathered from the alley behind the cathedral."
    ya "To become closer to God, we must partake in the pieces of Him. And in doing so, we will be granted safety, serenity, and forgiveness for the sins we have committed but have yet to realize."
    s "You gathered leaves from the alley and turned them into tea?"
    ya "Not just any tea, Sensei. Tea that brings us closer to Him. Don’t you want to try?"
    ya "Wormwood has already had four cups and he is very picky when it comes to fluids. I’m sure you’ll love it as well."
    s "I’m good, Yasu. Thanks."

    scene teaparty5
    with dissolve

    ya "At the very least, will you sit with us and partake in the rest of the celebration?"
    ya "Their feelings will be very hurt if you leave after coming all this way."
    s "Sure. But...just to reiterate, I am not drinking your weird ceiling water tea."

    scene black
    with dissolve2

    "I move to the opposite side of the table and pull out the only chair not occupied by the lifeless body of a rabbit."
    "I wonder if this seat being empty means that Yasu anticipated me coming here and, if so...why?"
    "It’s not like I haven’t come here of my own volition in the past, but I’m far from being considered a regular at this point and...there was really no reason for her to believe I {i}would{/i} show up."

    scene teaparty6
    with dissolve2

    s "Yasu."
    ya "Yes?"
    s "You weren’t expecting me, were you?"
    ya "Of course I was."
    s "But...why?"
    ya "Because even if it is not yet apparent to you, your heart beats in tune with His."
    ya "You were always going to wind up here for the celebration whether or not you knew it."
    ya "Deep down inside, you love the summer. The same way we do."
    s "You mean you and the rabbits?"
    ya "I suppose, if that is what makes this easier for you to understand."
    s "I don’t think anything is going to make this easier to understand."
    ya "You are free to ask any questions you may have."
    ya "Penemue may not be in the brightest of moods today, but he is very knowledgeable when it comes to our reasons to {i}be.{/i}"
    ya "And Wormwood is a font of information when it comes to the history of our God."
    ya "There’s also Muriel...and Yomiel...and Zachariel...and many others hidden in the background who would be more than happy to hold your hand as you embark on your journey closer to us, Sensei."
    s "Again, I’m good. I’m just...here to hang out with you, really."
    ya "Hang out?"
    s "Yeah. You know...spend time together. As like, friends. Or...whatever we are."

    scene teaparty7
    with dissolve

    ya "Heheh..."
    ya "We are not friends, Sensei."
    s "You know, it really hurts when you, of all people, are the one saying that."
    ya "That isn’t to say that I don’t {i}want{/i} to be your friend. I would love that."
    ya "But I am entirely undeserving."
    ya "Besides...there’s something much more important that we have to do. Something that transcends the relationship of even lovers, let alone {i}friends.{/i}"
    s "Right. Fill the world with light or whatever."
    ya "If only it were that simple."
    ya "You see, one of my favorite things about summer is that His voice becomes much clearer."
    ya "Which means that my {i}purpose{/i} becomes much clearer in turn."
    s "And that purpose is?"

    scene teaparty8
    with dissolve

    ya "..."
    s "..."
    ya "..."
    s "Yasu?"
    ya "I’m sorry..."
    ya "He doesn’t want me to tell you."
    s "Okay, well...this is the last time I come to one of your tea parties."
    ya "This is the last party we’ll be having for quite some time. And I’m sure you’ll have changed your mind by the time the next one comes around."
    ya "That is how He has envisioned it."
    ya "That is where things will go from here."
    s "And if they don’t?"
    ya "Sensei, you don’t understand."
    ya "That’s just not possible."
    s "Yasu-"

    play sound "static.mp3"
    scene teaparty9
    with flash
    stop sound

    ya "I am the one who hears the call! I am the one who witnesses His future for Him!"
    ya "Who plays it back like the broken record this life is!"
    ya "He knows what will happen because it has happened before!"
    ya "It will happen again!"
    ya "Summer has come, Sensei!"
    ya "He sleeps no longer!"
    ya "Enlighten him, Wormwood!"
    s "Yasu, I’m not going to talk to-"

    play sound "static.mp3"
    scene teaparty10
    with flash
    stop sound

    worm "To build a wall or break one down;\nIt depends on what you want."
    worm "To see a world outside of mirrors;\nOr bathe in holy fonts."
    worm "We all have things that we must do;\nYou, too, must fill your role."
    worm "For if you don’t, we {i}all{/i} will fall;\nFurther down the rabbit hole."

    play sound "static.mp3"
    scene teaparty11
    with flash
    stop sound

    ya "Feel the caress of the wind as it slips in through the sleeves of your shirt! This is Him!"
    ya "The undeniable solemnity you feel when gazing up at your ceiling! The one that does not leak! This is Him!"
    ya "The shaking of the trees! The creaking of the floorboards! It is all Him!"
    ya "He is all around us!"
    ya "He is in me!"
    ya "I can feel him bursting out like a possessed holy embryo with fingernails growing at twenty times the rate of that of a normal human being!"
    ya "He claws His way out!"
    ya "Can you see Him?"
    ya "He wants to emerge!"
    ya "CAN YOU SEE HIM?!"
    s "I-"

    play sound "static.mp3"
    scene teaparty12
    with flash
    stop sound

    ya "Don’t answer His questions with responses you know not to be true."
    ya "Not after all He has done for you."
    s "See...that’s just the thing."
    s "He has done {i}nothing{/i} for me."
    s "No {i}god{/i} has ever done anything for me. They’re all just stories that people latch onto so they can have something to look forward to when they die."
    s "Or...something they force themselves to believe in so they can have some sort of code to live by."
    s "But none of them are real. Yours included."
    s "But hey, if you want to waste away your days talking to stuffed animals instead of people, that’s fine. I’ve got no right to tell you how to live your life."
    s "But you should stop trying to make me live {i}mine{/i} the way you do by shoving these stories down my throat every time I come here."

    scene teaparty13
    with dissolve

    ya "But, Sensei-"
    ya "You wouldn’t come here at all if you didn’t long for the sensation of something stuck inside of your throat."
    ya "What difference does it make if it is the word of the lord or the tongue of the one He brought back?"
    s "The...what?"

    scene teaparty14
    with dissolve2

    ya "Heheh...hahahahahahHH!H!H!H!HAHAHAHAHuiywegfdiusdhfiuodghfuohasdifougdhsa!!"
    ya "YOU KNOW IT TO BE TRUE! WHICH IS WHY YOUR DENIAL NOW IS STRONGER THAN EVER BEFORE!"
    ya "YOU HAVE NOT JUST {i}SEEN{/i} HIM AT THIS POINT!"
    ya "YOU HAVE BEEN {i}TOUCHED{/i} BY HIM!"
    ya "I CAN SMELL HIS SCENT ALL OVER YOU! THE ONE TRUE APHRODISIAC! CLINGING TO THE FABRIC OF YOUR COAT AND MAKING ME FEEL WAYS I HAVE SELDOM FELT BEFORE!"
    ya "COME TO ME! COME TO ME IN YOUR PUREST FORM!"
    ya "COME TO ME BEFORE ALL OF MY FRIENDS IN THE HOUSE OF MY FATHER AND RUB HIS SCENT ON ME!"
    ya "RUB HIS SCENT ON ME!"
    ya "RUB HIS SCENT ON-"

    play sound "static.mp3"
    scene teaparty15
    with flash
    stop sound

    ya "NGH!"
    s "..."

    "Yasu winds up screaming at me so loudly that she gives herself a headache."
    "Which, at this point in time, I can safely say is probably the best thing that has happened to me today."
    "Or, at least it would be if I wasn’t actually worried about her health right now as it seems this might actually be kind of serious."

    s "Uhh...religious stuff aside, are you okay? Because it looks like-"

    play sound "static.mp3"
    scene teaparty14
    with flash
    stop sound

    ya "I am fine! This is nothing in the face of all He has felt!"
    ya "Please help yourself to some of Penemue’s eggs, Sensei! Partake in the bountiful feast He has provided us! One that transcends time itself!"
    ya "Reserve your space in the white room! There is nowhere else that can protect us from-"

    play sound "static.mp3"
    scene teaparty16
    with flash
    stop sound

    ya "AAAAHHH! IT HURTS!"
    ya "IT HURTS, IT HURTS, IT HURTS!"

    play sound "static.mp3"
    scene teaparty14
    with flash
    stop sound

    ya "It doesn’t hurt at all!"
    ya "It feels better than anything I’ve ever felt before!"
    ya "Come to me!"
    ya "Come! Come! Come!"

    play sound "static.mp3"
    scene teaparty10
    with flash
    stop sound

    worm "A LIE, A LIE, ALIGN!;\nTHE STARS BENEATH THE SKY!"
    worm "CHERISH THOSE WHO LOVE THEM AND RELINQUISH YOUR CONTROL!"
    worm "FEEL HIS GIFTS! RETURN HIS LOVE!"
    worm "CLIMB FURTHER DOWN THE RABBIT HOLE!"

    play sound "static.mp3"
    scene teaparty17
    with flash
    stop sound
    stop music

    s "Okay. It’s time we get you back to-"
    s "..."
    s "Yasu?"

    scene black

    "When I turn back around, it’s like she was never here at all."
    "Yasu, the rabbits, and all of the tea had vanished into thin air."
    "All that was left was a table, some chairs, and a plate full of eggs."
    "I chalked it up to another delusion and headed home."
    "The sound of insects along the way was louder than ever before."
    "When I got into bed that night, it felt as if my legs had been broken."
    "Or, at the very least, bent backwards."

    $ renpy.end_replay()
    $ church15 = True
    $ yasu_love += 1

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
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

label yasuspecial15:
    scene yasugenres1
    with dissolve2
    play music "summerwind.mp3"

    "It’s a completely normal and peaceful day in my office."

    play sound "dooropen.mp3"
    scene yasugenres2
    with dissolve

    "Nevermind."

    mo "Sir!"
    s "What, Molly?"
    mo "The three of us require your assistance! Or...guidance! Or something!"
    s "Why? Aren’t you supposed to be at your club right now?"
    f "This actually...is our club activity for the day. We’re teaching Yasu about manga."
    s "I see."
    s "Just so we’re all on the same page here, you guys know I that I am pretty much entirely unfamiliar with manga, right?"
    mo "Aye!"
    s "And that asking me for help with this is essentially pointless because of that."
    mo "Aye!"
    s "Okay, cool. I just wanted to make sure."
    f "So...you’ll come with us, then?"
    s "I’m not sure. Why not leave my involvement up to Yasu? You know, since her new thing is apparently just ghosting on me without a care in the world."

    scene yasugenres3
    with dissolve

    ya "Ghost?"
    mo "Oof. That sort of crit would take most other people out in one shot, Sir. I’m surprised you’re still able to stand up after that."
    f "You and...Yasu have been spending time together?"
    s "If by spending time with her you mean her offering me eggs and then immediately leaving in the middle of conversations, yes."
    f "That’s not...really what I meant, no."

    scene yasugenres4
    with dissolve

    ya "I’m sorry, but...I don’t remember this at all."
    s "You don’t remember having a “summer celebration” with a bunch of rabbit dolls in that weird cathedral and drinking tea made from back alley leaf litter?"
    ya "I remember the celebration, but I don’t remember your presence."
    ya "Which made me very sad since I brewed extra tea for you."

    scene yasugenres5
    with dissolve

    f "Wait...you...drank tea made of leaves you found on the ground?"
    ya "Special leaves that the one with many eyes blew onto the sacred asphalt behind the place He falls asleep at night."
    mo "Are we going to ignore the “party with rabbit dolls” part? Or is that something we just expect out of her ghostliness at this point?"
    s "Wait, Yasu- do you really not remember me being there?"

    scene yasugenres6
    with dissolve

    ya "I waited so long for you that Touka sent one of her fancy cars to come pick me up so I wouldn’t have to walk home during what she called the “witching hour.”"
    ya "Now, you’ll have to wait until next summer for divine protection."
    mo "Or just find yourself a paladin. Which, not gonna lie, is far easier said than done, Sir."
    s "I’ll be fine without “divine protection.” What I’m more concerned about is the fact that I now have memories of a thing that apparently never happened."
    mo "Perhaps this is just some sort of dream you’re remembering, Sir? Yasu doesn’t seem like the type to cast {i}vanish{/i} in the middle of casual conversation."
    s "Maybe. It’s just weird that I’d also remember the names of her stuffed rabbits."

    scene yasugenres7
    with dissolve

    ya "The rabbits do not belong to me. They belong to everyone."
    ya "They are His ears...and carry forth the whispers too soft for Him to hear on His own."
    ya "All shapes and all sizes. "
    ya "All forms and all colors."

    scene yasugenres8
    with dissolve

    ya "Except red."
    ya "Red is bad."
    mo "I take great offense to this."
    s "Well, I don’t really remember what colors or sizes they were...but does the name “Wormwood” ring a bell?"

    scene yasugenres9
    with dissolve

    mo "Aye! That’s a card from the World of Warcraft TCG that allows you to put a target ally into-"
    ya "Yes! Wormwood is an emissary! One who carries all sorts of information about the history of the church! "
    mo "Yeah! Or that!"
    ya "I am glad you remember him!"

    scene yasugenres10
    with dissolve

    ya "But I don’t understand how that would be possible. He only appears to me on special occasions and you were not at the celebration."
    s "I’m telling you I was, though..."
    ya "Did you drink the tea?"
    s "No. I-"
    ya "You should have drank the tea. It is possible your body was detached from your mind as a result of your failure to do so."

    "Or it’s possible that Yasu is insane and simply doesn’t remember the fact that we had an entire conversation about her god at a table full of stuffed animals."
    "I guess that wouldn’t really explain the sudden vanishing of them, though..."
    "But it’s entirely possible I just lost track of time again. It obviously wouldn’t be the first time something like that happened."
    "And it sure as hell makes a lot more sense than vanishing rabbits or the sudden introduction of “amnesia” to the list of mental issues Yasu likely needs to be professionally diagnosed with."
    "I do feel a little better knowing that there was no conscious decision to ghost me, though."
    "And I guess it’s fine to prioritize that over the idea of false memories because, let’s face it, I’ve become a bit of an expert when it comes to memory related issues."
    "Just don’t tell that to Maya or she’ll probably get sad and reflective."

    f "Yasu...I really don’t think you should be making tea out of things you find on the ground..."

    scene yasugenres11
    with dissolve

    ya "You would change your mind if you had some. It is the cure for all things and would quell the sadness in your heart that eats away at your innards like carrion birds."
    f "The feeling you’re describing sounds...more like a virus you may have gotten from-"
    mo "Can we stop talking about carrion birds and tea leaves and get back to the topic at hand? "
    mo "We’re here to enlist Sensei’s help for Yasu’s reeducation process, aren’t we?"
    s "Reeducation process?"

    scene yasugenres12
    with dissolve

    ya "I am broken beyond repair and these two wonderful and helpful girls are going to help fix me."
    f "We’re not going to {i}fix{/i} you, Yasu...We just want to help you figure out what type of manga you like since you’ve never read any and...have decided to join the manga club despite that."
    mo "Shh. Stop. Don’t say anything that might make her question her decision. We need every member to stay in the club or we’ll all wind up in costumes at Sensei’s house."
    ya "That sounds delightful."

    scene yasugenres13
    with dissolve

    f "No...that sounds very embarrassing..."
    s "As supportive as I am of the idea of everyone coming over to my house and putting on cosplay, I still don’t understand how I am supposed to help Yasu figure out what kind of manga she likes."
    s "Especially when I don’t even know what kind of manga {i}I{/i} like."
    mo "As the club advisor, that is probably something you should know, Sir."
    s "As the club president, you should be off doing your job instead of dragging me into it as well."
    mo "But, Sir! If I’m not annoying you every hour of every day, what purpose do I even have?"
    s "Have you been talking to Io lately?"
    mo "Sir. {i}No one{/i} has been talking to Io lately."
    s "You know what? That’s fair."
    ya "I like her hair. It reminds me of the grass."

    scene yasugenres14
    with dissolve

    f "Sensei...the reason we need your help is less of an actual {i}need for help{/i} and more the fact that...Yasu seemed upset that you weren’t going to be at club."
    s "What? Really?"
    ya "Summer can only do so much for the sounds I hear. Having you nearby makes them even clearer. "
    mo "Did you hear that, Sir? Are you really going to say no to a line as cute as that?"
    s "Yes."
    mo "Strike that. Are you really going to say no to a line as cute as that {i}knowing that Yasu will also be in cosplay?{/i}"
    f "In addition to wanting you there...Yasu was also upset that we weren’t dressing up today..."
    s "See, this is a detail that should have been revealed from the start. This changes everything."
    ya "I hope that you are not repulsed by the sight of a worm in beautiful clothing. "
    ya "If you are, just close your eyes. You need not see for me to feel your presence. But you must be present for me to see. "
    ya "Do you see?"
    s "No. But I’m not about to try and figure it out when I know that something much more interesting than this awaits in the club room."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    s "Okay. Everybody out. Come on."
    mo "Quest complete! Fantastic job, Yasu! "
    mo "Remind me to come up with a nickname for you as soon as possible. You’ve earned it."
    ya "I have earned nothing but a life of servitude for-"
    f "Oh, look. We’re here..."

    scene yasugenres15
    with dissolve2

    f "Sensei...you can wait out here with me while Molly helps Yasu get changed..."
    mo "I hope you like crimson demons, Sir. Because what you’re about to see is bound to make you {i}explode.{/i}"
    ya "Demon? But demons are bad. I don’t want to be a demon."

    scene yasugenres16
    with dissolve

    mo "Well...the name is more of a technicality than anything. The character is basically just a fire mage."
    ya "But warlocks and mages are also enemies of God. "
    ya "Do you have anything with wings?"
    mo "Uhh...not on hand, no. But you’ll be fine. It’s just pretend, okay?"
    mo "Now, get in there and start stripping. We don’t want the Herald of the Adolescents waiting too long, do we?"

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "Molly shoves Yasu into the club room and Futaba lets out a hearty sigh, showcasing just how exhausting the introduction of everyone’s favorite cult member to their friend group is."
    "She tells me a little about how she expected things to settle down after Rin left. "
    "But apparently, having someone completely new to the nerd world around has awoken something in Molly that she is having trouble containing."
    "And while I’d like to talk about how I’m sure this is all just temporary and that Yasu will adjust and Molly will settle down in no time at all, both of those things are obviously untrue."
    "In fact, I can’t fathom {i}any{/i} scenario where Yasu doesn’t stick out like a sore thumb."
    "But I’m glad she’s trying. "
    "Even if her efforts are currently resulting in her being dragged around like a puppy on a leash by a small Irish girl."
    "Even before that, though, Yasu was already on a leash."
    "She probably has been for a very long time now."
    "We should be happy that we can see what this new one is attached to."
    "........."
    "......"
    "..."

    scene yasugenres17
    with dissolve2

    mo "Ta-dah! Yasumin! "
    mo "And it only took me one night to adjust the costume for her size!"
    mo "Yasu! Say the line!"
    ya "Boom!"
    mo "Close enough!"
    s "I’m not sure if it lives up to the one from the dorm wars, but I accept and appreciate this greatly and thank all of you for allowing me to be involved."
    mo "Don’t thank us, Sir! Thank Yasu for her ideal cosplay figure and extremely unique and only mildly creepy aesthetic."
    ya "Do I look like a real manga character now?"
    s "Sure. But with an extra dimension, which makes things even better."
    mo "Debatable! "

    scene yasugenres18
    with dissolve

    f "So...have you thought at all about what genre you’d like to try first, Yasu?"
    f "We have all different types of books here. Ami and Maya even brought in most of their collection for you to sort through if you’d like."
    mo "I don’t know if Yasu’s ready for any of the stuff Maya reads. PunPun isn’t really entrance level material unless you’re looking to an-hero."
    ya "What is entrance level material? I would like to stay away from anything with gratuitous violence or premarital sex."

    scene yasugenres19
    with dissolve

    mo "Okay. Well, that rules out pretty much Rin’s entire collection, so...let’s see what else we can find laying around here."

    scene black
    with dissolve2

    "Molly and Futaba begin sorting through a few boxes while Yasu and I stand awkwardly in the corner, occasionally making eye contact- which may or may not be a sin according to her religion."
    "I take the fact that she hasn’t spontaneously burst into a fit of tears to be a good sign, though, and let the awkward silence bridge the ever growing gap between us in the form of a temporary respite."
    "There’s still a great deal I don’t understand about her. Particularly the parts where she vanishes and leaves me alone at a table full of eggs, but things like that can wait until another day."
    "For now, I’m just interested in seeing how she functions as a normal misfit girl, trying to fit in with people who genuinely {i}want{/i} her to fit in-"
    "And likely making everyone very uncomfortable in the process."

    scene yasugenres20
    with dissolve2

    mo "Question! How gratuitous {i}is{/i} “gratuitous violence?” "
    mo "Can there be any violence at all? Because there are a lot of very accessible shonen manga that serve as an awesome gateway to the world of anime!"
    ya "Umm..."

    scene yasugenres21
    with dissolve

    f "Is all romance off the table as well? Or just romantic series with...um...premarital sex?..."
    f "Because romantic subplots are essentially impossible to avoid in fiction, but there are a lot of fantasy series I enjoy that barely focus on it at all. And I think you’d love those!"
    ya "That...sounds like it might be okay..."
    s "What about this?"

    "I pick up the first book I see on top of a stack that looks relatively safe for work. And after skimming through the pages, I can say with utmost certainty that there is no premarital sex or gratuitous violence."
    "It doesn’t really seem like there’s much of {i}anything,{/i} though."
    "It’s just...people talking."

    scene yasugenres22
    with dissolve

    mo "Whatcha got there, Sir? You digging into Ami’s slice of life pile?"
    f "Oh, I think something like that might be good for Yasu as well."
    ya "Slice of life? "
    s "I guess that’s what I’m holding, sure."
    ya "It’s not violent?"

    scene yasugenres23
    with dissolve

    mo "Not that kind of slice, Yasu."
    mo "In fact, here’s a little weebnote for you."
    mo "Slice of life is a genre of anime and manga that focuses primarily on the lives of the {i}characters{/i} in the story and less on a unified and major coherent plotline."
    mo "That’s not to say there’s never any sort of plot at all, though. A lot of SoL series can blend in action and drama without ever abandoning their roots."
    mo "It’s something people tend to gravitate to after overloading themselves on more serious or action-packed series to sort of...unwind or reset."
    mo "But that doesn’t mean you can’t start there! And the one Sensei is holding would actually be a great one to go with since I’ve already finished it and can confirm there is zero sex at all!"

    scene yasugenres24
    with dissolve

    ya "Hooray for no inappropriate content!"
    mo "Yeah! Hooray, I guess!"
    mo "I still think you should maybe {i}consider{/i} shonen, though, since a lot of it nowadays is-"
    f "Just let her have this, Molly."

    scene black
    with dissolve2

    "I hand the book over to Yasu, who accepts it with the least creepy smile I have seen out of her thus far."
    "She opens it up and begins reading very slowly, focusing for far too long on each and every page as if she’s taking in every last detail and every last line."
    "I’m sure that the artists involved would be happy to see this, but even then I think they’d believe it to be a tad excessive."
    "Molly and Futaba cross the room and take their places beside me like we’re some sort of proud, polyamorous couple watching our daughter take her first steps."
    "I’m just a little disappointed because her steps are in a direction that I’m not particularly interested or invested in."
    "But hey, this is the first time I’ve ever seen a smile like that out of her."
    "And it’s a lot more infectious than those that have been induced by her god."
    "Yasu continues reading until the sun begins to set while the rest of us talk quietly amongst ourselves."
    "When the final bell rings, Yasu closes her book and thanks all of us for our help."
    "But not before grabbing three more books of what I expect and hope are the same genre. "

    $ renpy.end_replay()
    $ yasuspecial15 = True
    $ yasu_love += 1
    stop music fadeout 7.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label church20:
    scene urbanparadise
    with dissolve2
    play music "undersea.mp3"

    "Despite continuous signs that I should stop coming here in the form of vanishing rabbits and duct taped eyes, I find myself in disagreement with the world and all that’s happened to me once more."
    "Though, this time, instead of my legs moving themselves, it is a conscious decision that I have made."
    "I could turn around at any moment if I truly wanted to."
    "So why don’t I want to?"
    "Where does this subconscious compulsion to meet with a girl—who, despite maintaining constant eye contact, will never see eye to eye with me—come from?"
    "And why is the path to her always so devoid of everything but unwelcome sounds and sweat droplets trickling down my chest before being consumed by my clothing?"
    "I think for a moment that maybe tonight will be different."
    "And that maybe I will find Yasu outside of her church and we’ll leave this place and learn who each other really are."
    "But the chances of that are unlikely."
    "Not because we are predictable creatures who dance on the puppet strings of thoughts or beings we cannot see-"
    "But because we're incapable of being anything {i}but{/i} that."
    "So there is nothing left to learn about one another as we have not yet squeezed our way out of our respective cocoons. "
    "And so long as our shells are wrapped tightly in the invisible threads of our masters, we will not break free."
    "The one who controls Yasu keeps her strings firm and taut."
    "And the one who controls me can’t figure out how to untangle them."

    scene black
    with dissolve2

    "A small hole appears in the wall of my subconscious."
    "I press my hands to its edges and pull it open as wide as I can."
    "Its insides smell like rotting wormwood."
    "........."
    "......"
    "..."

    scene yasuoutsidechurch1
    with dissolve2

    ya "Ngh!"
    ya "Let...me in!"
    ya "I...belong inside! "
    ya "I have no use out here!"
    ya "Let me in! Let me in! Let...me in!"
    s "..."

    "Huh."
    "It appears that maybe tonight {i}will{/i} be different after all."
    "I find Yasu desperately fighting against the handle of the church door, attempting to leverage what little body weight she has to pry it open. But all to no avail."
    "She struggles, much like a fish out of water. "
    "And though she may lack the necessary amount of slits in her neck to take in oxygen, the one she has much further down below is sure to bring her more joy than any amount of released carbon dioxide would."
    "Perhaps this sudden rejection at the hands of her god will be the motivation she needs to finally use it?"

    ya "I will repent for my sins! I will repent for my sins!"
    ya "I did not mean to sully your great name, heavenly Father! I did not mean any harm at all!"
    ya "If I have done wrong, strike me down! For I belong nowhere if not inside!"
    ya "I know you not as a cruel and callous god, but as a forgiving and loving one! And that all who wish to enter, may!"
    ya "So why?! Why must you keep me out here?! "
    ya "Tell me, Father! What must I do?! "
    ya "Scream it loud enough that it pierces the veil! Loud enough to penetrate this plague of locusts with a plague of your own!"
    ya "Let me in! "
    ya "Let...me in!"
    s "Yasu...I don’t think you’re going to be able to get in there if someone locked the door."

    scene yasuoutsidechurch2
    with dissolve

    ya "It can’t be locked! It wouldn’t make sense! "
    ya "The hands of mortals who do not accept Him are not strong enough to move these doors!"
    s "I don’t accept him and I move these doors all the time. "
    s "Someone’s probably just fucking with you."
    ya "No! No, that is not possible!"
    ya "This is divine punishment! I have strayed from my path and am being forced aside!"
    ya "I must repent! I must repent!"

    scene yasuoutsidechurch3
    with dissolve

    ya "Let me in!"
    ya "I will right all of my wrongs! Whatever they may be! Just give me a sign! Let me hear your voice!"

    "While the idea of someone going out of their way to lock these doors seems like the most likely scenario, it’s important to note that I’ve never really {i}seen{/i} anyone around here."
    "And with Yasu spending virtually all of her free time inside of this building, it would mean that they would have had to come in one of the rare windows of time in which she’s absent."
    "But that begs to question- why?"
    "What would someone have to gain from closing off an old church building used by no one but a young girl with knotted hair and several screws loose?"
    "What will become of Yasu when she realizes that prayer alone will not get her what she wants?"
    "And that any time it {i}had{/i} in the past was just a convenient coincidence."
    "The same way this meeting is."

    scene black
    with dissolve2

    "For me and not for her, of course."
    "I got what I wanted and the only thing lost was a sliver of sanity in a girl who does not possess much to begin with."
    "It reminds me of something a rabbit once said about gifts."
    "But if this is a gift from an unlikely sponsor—the same one watched by a girl with blue eyes—why am I the one benefiting when all I have done thus far is doubt?"
    "And why is the one who follows so closely behind the guiding light the one caught in darkness?"
    "........."
    "......"
    "..."

    scene yasuoutsidechurch4
    with dissolve2

    ya "Help me open the door!"
    ya "It may be closed for me, but it would never close for you!"
    s "It’s locked, Yasu. It’s not going to make a difference {i}who{/i} tries to open it right now."
    ya "You don’t know that! You don’t know the way He works!"
    s "This may just be my inner “expert sinner” talking, but wouldn’t it be {i}bad{/i} if you were to sneak back into the church if your god truly is the one locking you out?"

    scene yasuoutsidechurch5
    with dissolve

    ya "He will forgive me! For in His light I walk! And all that I am is the result of all He allows me to be!"
    ya "Though the darkness hath clung to my coattails, I have shaken them off and am ready for His touch of reluctant purification!"
    ya "I will be clean again! I will!"
    s "What did you even do to become {i}unclean?{/i}"

    scene yasuoutsidechurch6
    with dissolve

    ya "I do not know. And I {i}can not{/i} know as His voice has retreated behind these doors."
    ya "The only change to my life that I can recall sprung from the pages of the books that I read!"
    ya "But those books were free from the tainted and misconceived depictions of life that true sinners indulge in!"
    ya "What I did should be allowed! "
    ya "There are no rules against entertainment! There are no rules against fun!"
    ya "And yet I find myself abandoned! "

    play sound "static.mp3"
    scene yasuoutsidechurch7
    with flash
    stop sound

    ya "Do you know what happens to a duckling who loses its mother?"
    s "Doesn’t it just...latch onto whoever it sees next?"
    ya "Yes. But if the replacement animal or human does not understand what the duck requires to survive and grow, then what?"
    s "I don’t-"
    ya "It dies."
    s "I thought that nothing ever “dies” in your religion?"
    ya "That which is abandoned can. For He is the one who binds the planes together with fishing wire."
    ya "And if he willfully decides that one can not fit in the space between them, there is nowhere left for that person to go."
    ya "I am caught, Sensei."
    ya "Tangled up in wires."
    ya "I must-"
    ya "Be-"
    ya "Unraveled."
    s "Well, you’re not going to get “unraveled” by just waiting outside a building you can’t get into. So why don’t we...go for a walk and help you clear your mind or something?"

    scene yasuoutsidechurch8
    with dissolve

    ya "A...walk?"
    ya "But where?"
    ya "The world as we know it has been stripped away from us."
    ya "Everything is already g-"
    s "The world is still here, Yasu. Just because you won’t be able to see your normal hangout spot from wherever we’re going doesn’t mean that everything has vanished."
    ya "But...where {i}are{/i} we going?"
    ya "What sort of place will accept me the way I am?"
    s "Wherever I take you, I guess."
    ya "..."
    s "Is that a problem?"
    ya "I do not know..."
    ya "I have lost my mother duck..."
    s "Then make your own decision for once in your life instead of waiting for someone else to make one for you."
    ya "What you ask of me...is to both lead and follow at the same time."
    s "I think choosing to follow can be its own form of leading."
    ya "But only when it's directed at {i}you{/i} and not the true god?"
    s "..."
    ya "Do you see yourself as an interim deity? Are you truly so elevated?"
    s "I see myself as someone who is about to walk away with or without you."
    s "So follow me or don’t. This choice is yours."
    s "But if you plan on sticking around here and trying to pry those doors open all night, the only thing you’re going to find is further frustration and heartbreak."
    s "At least {i}I{/i} won’t willfully abandon you."

    scene black
    with dissolve2

    "I turn around and, just as expected, Yasu clings to my side like the desperate prey she is- hiding under the cover of someone more powerful just because they have an idea of where they want to go."
    "And so I take her into the darkest alley I can find."
    "Not so I can defile her holy, virgin body-"
    "But so she understands that power does not come from the light alone."
    "And that sometimes, it’s easier to see in the dark."
    "........."
    "......"
    "..."

    scene yasuoutsidechurch9
    with dissolve2

    "Vines sprawl out and make their home on the same damp, concrete wall we press our backs against."
    "The smell of mildew spreads throughout the alley, its scent almost pulsing- coming in waves where it turns from bearable to nauseating in the blink of an eye."
    "I distract myself from the need to vomit by focusing on a girl who’s able to ignore the scent entirely. "
    "I imagine this is not the first time she’s spent the late hours pressed up against a damp concrete wall."
    "In fact, I imagine this feels more like home to her than a warm bed in a locked room."
    "It’s the only thing that makes her lack of fear right now plausible when many others in her position would attempt to distance themselves."
    "Yasu pulls her knees to her chest- not because she is scared and defensive."
    "But because, even in this intense summer heat, the only warmth she will let in is that which belongs to her god."
    "And despite my desire to become that for her, it is still far too soon."

    s "So..."
    ya "..."
    s "I take it nothing like that has ever happened before?"
    ya "I have been the purest of the pure. There was no reason to bar me from entry until recently."
    s "There was no reason to bar you from entry {i}tonight{/i} either, though. Right?"
    ya "There must be something. Something I have yet to understand. "
    ya "Something that I must come to terms with so that I can return home."
    s "You have another home now, though. One significantly warmer and less creepy. Hell, it even comes with an extremely hot and generous rich girl."
    s "That’s where I’d be spending {i}all{/i} of my time if I were you."
    ya "But you are not me."
    ya "You resist the light when I require it to move forward."
    ya "It is the reason I still persist today. The reason I can open my eyes."
    s "..."

    scene yasuoutsidechurch10
    with dissolve

    s "I take it you won’t actually tell me about how things were before that, will you?"
    ya "There is no me before the me I am today."
    ya "I am but a product of Him alone. An angel in training that lives to serve, even while I am falling to the ground."
    s "But you were someone else {i}before{/i} that."
    ya "And so were you. "
    ya "The reasons you do not speak of your past self may not be different from those which belong to me."
    s "In all fairness, you’ve never really given me the opportunity to speak of my past self around you."
    ya "Would you if I did?"
    s "That’s...a little complicated."

    scene yasuoutsidechurch11
    with dissolve

    ya "Yes..."
    ya "It is, isn’t it?"
    ya "You have so many secrets that even the air struggles to hold them."
    ya "It is why I know more about you than you will ever understand about me."
    s "Oh yeah? Then...what do you know?"
    ya "..."
    s "..."

    scene yasuoutsidechurch12
    with dissolve

    ya "I know that tragedy would befall each and every one of us if I were to share that information with you."
    s "That sounds a lot like a convenient excuse to make up for the fact that you’re just bullshitting me right now."
    ya "If that is what you believe, then that is what you believe."
    ya "But that is where our biggest difference lies."
    ya "All you {i}can{/i} do is believe. But all I can do is {i}know.{/i}"

    scene yasuoutsidechurch13
    with dissolve

    ya "The secrets of this world and everyone in it glitter like diamonds."
    ya "The stars are not real. They are the residue of hopes and wishes. Dreams and desires."
    ya "And when we gaze up at them with our undeserving eyes, we are gazing at the past itself and each and every trace left behind during a departure from one plane to the next."
    ya "Would you believe me if I told you of the stars below us as well?"
    s "I wouldn’t believe you no matter what you told me about literally anything."
    ya "Even when that’s all you can do? When I {i}know?{/i}"
    s "Yes. Because we have actual scientific explanations for the stars and I have a hard time believing that the key to everything is the endless rambling of a cult member."

    scene yasuoutsidechurch14
    with dissolve

    ya "A cult is full of members. I am but {i}one{/i} measly soul- filled with nothing but messages too painfully true for those around me to grasp."
    ya "Those unlike you."
    ya "But your palms will open soon enough. And in them, I will place little shards of His truth. A truth that will change the way you perceive your life."
    ya "Soon, you will forget how to swim."
    ya "And as your head falls beneath the surface of the water, you will understand just how much His protection means."
    ya "The tide is rising, Child of Man. A torrential downpour looms on the horizon."
    ya "He can teach you how to swim once more. He can lift you up when the water starts to fill your lungs."
    s "I thought you couldn’t hear him any-"
    ya "I have heard this so many times that it is engraved into the back of my mind like initials on a tree."
    ya "You are popular in more than one plane, Sensei."
    ya "Your entire being transcends that which grounds the world."
    ya "Your failure to accept that would be a sin if it were anyone else."
    ya "But {i}you-{/i}"
    ya "You are His favorite."
    ya "Even though you deny Him so."

    scene yasuoutsidechurch15
    with dissolve

    s "Yeah, well...maybe if gods weren’t such fucking pricks I’d be more inclined to believe in them."
    ya "Do not fear, for I will make you believe."
    ya "And in me, you will find reason to persist. "
    ya "Though the doors may be closed tonight, the quieting of the insects has provided an opportunity for me to catch His whispers once more."
    ya "I do not know if He wants me to have them, but I am His humble servant and would willingly give my life to make His better."
    ya "Soon, I will help you understand."
    ya "Soon, you will have no reason to doubt me."

    scene yasuoutsidechurch16
    with dissolve

    ya "Soon, it will all be revealed!"
    ya "He will rise from the ground! Coated in the thick residue of dreams deterred! With arms spread wide, beckoning us forward!"
    ya "He will take us under his wings and we will return to where we belong! Clinging to his feathers as he reminds us that we are eternally loved so long as we obey!"
    ya "The snow has gone! It quiets his screaming no longer!"
    ya "The light returns! The light returns!"
    ya "And soon-"
    ya "So will we!"

    scene black
    with dissolve2

    "I stop paying attention to everything Yasu says somewhere in the middle of her speech."
    "I had thought this was finally going to be an opportunity to learn more about her."
    "About the {i}real{/i} her."
    "Or, as she would likely put it- the her that isn’t {i}her{/i} anymore."
    "But I guess that’s not going to happen."
    "And I guess that if it ever {i}will{/i}-"
    "It won’t be anywhere near here."
    "I should have taken her to a darker alley, further away."
    "I should have taken her somewhere the wind could not reach."
    "Somewhere underground."
    "Beneath the blanket of dreams deterred."

    $ renpy.end_replay()
    $ church20 = True
    $ yasu_love += 1
    stop music fadeout 7.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yasudorm20:
    scene yasusfuckingweirdyo1
    with fade
    play sound "knock.mp3"

    "I knock on Yasu’s door and wait for her to answer."

    play sound "dooropen.mp3"
    scene yasusfuckingweirdyo2
    with dissolve

    "But then Touka’s chest comes into my field of vision and I forget why I came to visit Yasu in the first place."

    to "Oh, Sensei. May I ask what brings you here tonight?"
    s "Boobs."
    to "I see."
    to "Well, goodbye then."
    s "Wait, no."
    to "If you plan on objectifying me any further, I’d really prefer to step away from this conversation before you manage to anger me."
    s "I’m actually just here to see Yasu. Is she in there right now?"
    to "..."
    s "Touma?"
    to "{i}Touka.{/i} And are you absolutely sure that is what you’re here to do?"
    s "Is right now not a good time?"

    scene yasusfuckingweirdyo3
    with dissolve

    to "If you would like my honest answer, now is probably the worst possible time you could have picked."
    to "In fact, the only reason I’m going out right now is to {i}get away{/i} from Yasu. She has...crossed several borders that even I can’t bring her back from."

    "Sounds like another night of Yasu not being able to make it into her {i}sanctuary{/i} due to her god's foil- a door."
    "I figured she would have come up with some sort of backup plan by now."
    "It’s not like there aren’t windows that could be easily broken or something along those lines."
    "Though, she’d probably consider that defiling holy grounds, so..."

    s "Uhh...well, what exactly is she doing?"
    to "Being a fanatic as always. And a rather over the top one, might I add. "
    s "Yeah, well...that’s kind of how she always is."

    scene yasusfuckingweirdyo4
    with dissolve

    to "No, Sensei. You’re not understanding. You really do not want to go in there right now. That is not the Yasu we have grown to love."
    s "Please don’t associate me with any form of loving Yasu. I’m just...curious about what type of person she really is. And that includes seeing her at her worst."
    to "Yasu is more than just a lab rat, you know. She’s a human being with human desires- and a very kind one at that."

    scene yasusfuckingweirdyo5
    with dissolve

    to "It’s just..."
    to "Um..."
    to "How do I put this?"
    s "She’s fucking insane?"

    scene yasusfuckingweirdyo6
    with dissolve

    to "Those are your unnecessarily vulgar words, not mine. Though, I suppose nothing I say is going to stop you at this point."
    to "Just don’t say I didn’t warn you about this the moment you step in there and start questioning your decisions."
    s "Thanks, Touma. That top looks great on you, by the way."
    to "Yes. It does, doesn’t it? I’m so glad that my teacher is the first one to compliment me on it."
    s "You say that sarcastically, but I know deep down it’s true."
    to "And I know that deep down, the only reason you are not in jail at this point is because I allow you to remain employed. So please keep that in mind the next time you comment on my breasts."
    s "Keep your breasts in mind. Got it."

    scene yasusfuckingweirdyo7
    with dissolve

    to "You know what? I don’t even care. Enjoy your time with “Yasu,” Sensei. I’m sure you’ll love it."

    scene yasusfuckingweirdyo1
    with dissolve

    "Touka steps away from the door and I brace myself for whatever is going on in there."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Seeing that I’ve already encountered Yasu in various extremely suspicious states, though, I’m sure that whatever is going on tonight is not much different."
    "As long as there are no talking rabbits or plates of eggs, I’m sure everything will be just fine."

    play sound "static.mp3"
    scene yasusfuckingweirdyo8
    with flash
    stop sound
    play music "pianomelancholy3.mp3"

    "Or not."

    ya "BLESSED BE THOSE WHO TEAR DOWN THE WALLS! WHO SLEEP DEEP INSIDE THEM! WHO ANSWER THE CALL!"
    ya "BLESSED BE THOSE WHO CAN’T LEARN TO FLY! WHO CLING TO HIS WINGS AS HE SOARS THROUGH THE SKY!"
    ya "BLESSED BE ME! FOR I AM HIS ANGEL! THE PUREST OF MAIDENS EVEN WHEN IT IS PAINFUL!"
    ya "IF IT ALL HURTS RIGHT NOW, IT WON’T HURT WHEN IT ENDS!"
    ya "I BESEECH YOU, LORD FATHER. ASCEND OR DESCEND!"
    s "Yasu, please get off of the chair. You’re going to hurt yourself."
    ya "I will not be hurt! I am under His protection!"
    ya "His hands touched me in my sleep! And in doing so, have awakened a new me! "
    ya "A new me who hears the call louder than ever before!"
    ya "My sins have been cleansed! My heart has been strangled by the tendrils of the one that I love!"
    s "Yasu-"
    ya "I channel Him into me so that He may speak on His own!"
    s "You can’t-"

    play sound "static.mp3"
    scene yasusfuckingweirdyo9
    with flash
    stop sound

    ya "BBLSYHWC CSHWLZ"
    ya "FCJ GHZA YWCC QL PTJVFT XOS DRL W WECS IEZYTH FCJ APHW SIGTVCWCK???"
    ya "KC NSB HWMUY ILPG LMSZ QVPBV CVI RPVGTV AC BI???"
    ya "AIGR, JVXPK"
    ya "KWKI KSTT PBIS AVT EYAH SM HWI VBT AOC SSLG CSA PTPVBV"
    ya "JOGVF HWI IIGHLB!!! REYFN LPG LIPUWX!!!"
    ya "MSTP OWH XOWRO, ZHXGRM HITSC HYWETPBV JYCB CVIG GBBI!!! JLSA XOS BEYY XX SSPZLG!!!"
    ya "PH XW VBAC AVTR AVPX P KXPS ZDZL MDY"
    ya "PH XW VBAC AVTR AVPX FCJV LTUSYHH APZA LHJT QLOCX ZCBIAVXRN"

    "Glossolalia (ɡläsəˈlālēə): {i}noun{/i}"
    "Definition: The phenomenon of (apparently) speaking in an unknown language, especially in religious worship."
    "Many have described it as the unmistakable feeling of the lord taking over one’s body and speaking through it in tongues indiscernible to even the most accomplished of polyglots. "
    "To me, it means nothing."
    "It is simply an excuse for one to feel a connection to something that does not exist."
    "And so I will wait beneath this girl, ready to catch her when she falls."
    "For even the highest of powers must descend eventually."
    "And they are not afraid to use those below them to cushion the blow."

    ya "KC NSB TTIS WI, GOWAH???"
    ya "TM XRZOIMHPAI SIHX???"
    ya "KC ILL BTVCSH MU MDYY JJPCO HMUU DYA ZXOL O RLVFJW VT RMJOSEZ???"
    ya "ZDGIHR ILLA PTHFI WV HWEA VT QHM TRASG!!! KPJT LPA NSBF TRAWGI ZSAJ!!!"
    ya "VBAC AVTR DWAP FCJ OUCL, GOWAH"
    ya "VBAC AVTR DWAP FCJ YURTVZHPRK KWC P QPR DOXX AVT AHM X HV"

    "Glossolalia (ɡläsəˈlālēə): {i}noun{/i}"
    "Definition: Complete bullshit."

    play sound "static.mp3"
    scene yasusfuckingweirdyo10
    with flash
    stop sound

    ya "Ahh..."
    ya "I..."
    ya "Feel..."
    ya "I feel so hot..."
    s "Maybe your god gave you a fever when he decided to rape your subconscious just now?"
    s "Is your speech over? Or do I have to sit through some more words I don’t understand before you finally come down and talk to me in a human language again?"
    ya "..."
    s "...."
    s "Yasu?"

    play sound "static.mp3"
    scene yasusfuckingweirdyo11
    with flash
    stop sound

    ya "If and when I fall, will you be there to catch me?"
    ya "Or will I collide with the ground? Cracking my head open and allowing my thoughts to spill out and crawl back into the gutters they were born in."
    s "Here’s an idea- why not just...you know, {i}not{/i} fall?"
    s "You’re sentient enough to speak at this point. I’m sure you can figure out how to move your legs."
    ya "I’m afraid they have gone numb."
    ya "I will need your help to move them."

    "My gaze shifts down from the back of Yasu’s head to her legs, taking note of the different shades of ghostly paleness in each of them."
    "I notice that they’re shaking slightly. But it’s less of an unsteady shake due to a lack of balance and..."
    "More of a..."
    "Soft...grinding of her thighs against one another?..."
    "Is Yasu-"

    ya "I am done praying for the night."
    ya "I trust that you will catch me now."
    s "Yasu, stop. I know you can-"

    play sound "static.mp3"
    scene t with flash
    scene whythesky with flash
    scene t with flash
    scene whythesky with flash
    scene yasusfuckingweirdyo12 with flash
    with hpunch
    stop sound

    "Yasu falls directly on top of me, but instead of scurrying away or crying out in a mixture of mild pain and embarrassment, her fingers find my own and lock into place."
    "Her body is certainly hot, just as she said moments ago...but it’s a heat I {i}recognize.{/i}"
    "It’s a heat I recognize all too well."
    "And the fact that it is {i}her{/i} heat fills me with uncharacteristic unease as this is not something I believe she consciously understands."
    "And yet-"
    "I struggle to push her away because it is a heat that makes me curious."
    "And one that I can help her enjoy if she only-"

    scene yasusfuckingweirdyo13
    with dissolve

    ya "{i}Hah...{/i}"
    s "Welp. I guess this is happening now."
    ya "Sensei...I feel so strange..."
    ya "He tells me that only {i}you{/i} can help me..."
    ya "But how?..."
    ya "How...do I...make the burning stop?..."

    "Yasu presses my hand firmly against her chest, and through the thin fabric of her night dress, I can feel her nipple already hardened."
    "It’s not like I really {i}needed{/i} confirmation about what I assumed she was feeling but, I guess it’s...good that I got it anyway?"
    "What’s not good, however, is that I absolutely should not allow this to keep going and the temptation to act out against that grows stronger by the second."

    ya "Sen...sei..."
    ya "Help...me..."
    s "..."

    "Yeah. This isn’t good."
    "The two of us remain like this for...an indeterminate amount of time."
    "Keeping track of it is quite difficult when the only thing racing through my head at the moment is what sort of effects the possession of a holy ghost can cause on the body of a young girl."
    "I’ve found myself less concerned with the way {i}other{/i} things affect the body of young girls in the past. But at least {i}those{/i} girls seemed...I don’t know...{i}aware{/i} of what was happening?"

    ya "Hah...hah..."
    s "..."
    ya "Something..."
    ya "Something is..."

    stop music
    scene black
    play sound "pop.mp3"
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene t with flash
    scene whythesky with flash
    scene t with flash
    scene whythesky with flash
    scene yasusfuckingweirdyo14 with flash
    play music "nowhereissafe.mp3"
    stop sound

    ya "PERHAPS YOU WILL BE MORE COMFORTABLE IN A ROOM OF YOUR OWN"
    ya "OH HOW MUCH YOU HAVE CHANGED IN JUST THE SHORT TIME YOU HAVE BEEN HERE"
    ya "I PRESENT TO YOU THE DAMPENED CUNT OF AN UNKNOWING VIRGIN AND YOU {b}RESIST???{/b}"
    ya "DO YOU THINK THAT IS AN OPTION???"
    ya "DO YOU UNDERSTAND WHAT I WILL TAKE FROM YOU IF YOU GIVE NOTHING TO {b}ME???{/b}"
    ya "I HAVE BEEN VERY GENEROUS"
    ya "MORE GENEROUS THAN THE OTHERS COMBINED"
    ya "I AM THE REASON HER SMELL STILL LINGERS IN THIS HOUSE"
    ya "AND I WILL TAKE EVERYTHING OF YOURS IF YOU DO NOT SUBMIT"
    ya "I HAVE WAITED LONG ENOUGH"
    ya "I AM TIRED OF THIS UNWELCOME SIDE OF YOU"
    ya "YOU HAVE UNTIL THE SNOW RETURNS TO TAKE SOMETHING YOU ARE NOT MEANT TO HAVE"
    ya "WHAT WILL IT BE???"
    ya "{b}WHO{/b} WILL IT BE???"
    ya "AND WHY IS IT NOT THE VERY VESSEL I COME TO YOU IN NOW???"
    ya "YOUR RESISTANCE WEARS THIN LIKE THE FILM ATOP A BOWL OF BONE BROTH"
    ya "AND SOON"
    ya "YOU WILL HAVE NO CHOICE BUT TO GIVE IN"
    ya "YOU WILL HAVE NO CHOICE BUT TO SPOON-FEED ME THE VAGINAL SECRETIONS OF A BODY I CAN NOT POSSESS"
    ya "SUBMIT"
    ya "SUCCUMB"
    ya "SUFFER"

    "I feel a body pressing down on my most sensitive spot."
    "But it is not the body that was on top of me just moments ago."
    "It is one that makes it hard to breathe. Hard to move."
    "And one that I would not be able to penetrate even if I tried."
    "{b}BUT I TRY ANYWAY{/b}"

    play sound "static.mp3"
    scene yasusfuckingweirdyo15
    with flash
    stop sound

    "I thrust upward into a resistant abyss and it feels as if I am tearing through a regenerating hymen each and every time."
    "I have grown familiar with this sensation over the years as I have torn through several now. But never one that returns immediately."
    "And never one that felt this jagged."
    "It is less like a thin layer of flesh and more like a sheet of thick construction paper that tears away at a new layer of {i}my{/i} flesh every time I try to move."
    "There is no dampness where my manhood dares to roam, but there is the tickling sensation of rain drops falling on my cheeks every seven seconds."
    "They’re much warmer than rain tends to be. But it barely ever rains here to begin with, so I could just be misremembering."
    "After roughly half an hour of cutting my penis raw on the regenerative hymen slash construction paper that is my current fuck-target, I grow closer to what most people would refer to as an “orgasm.”"
    "But, for reasons beyond my comprehension, today, I feel compelled to call this act not an “orgasm” but an “organism.”"
    "For as my sperm climbs its way through the human aqueduct known as my “urethra,” I can hear a chorus of screams."
    "Each one wants to be the one who reaches the finish line."
    "But the construction paper swallows and absorbs them whole."
    "And a brand new hymen spawning deeper inside of the meat hole than it belongs blocks their journey forward."

    scene black
    stop music

    "I cum."

    play sound "static.mp3"
    scene t with flash
    scene whythesky with flash
    scene t with flash
    scene whythesky with flash
    scene yasusfuckingweirdyo16 with flash
    with hpunch
    stop sound

    ya "AHH! AH! AHHH! "

    "Yasu’s body begins to violently shake and thrust upward at the air as she...somehow manages to give herself an orgasm by only touching her breast?"
    "I know that they say small ones are more sensitive, but...I didn’t really expect something like {i}this{/i} to happen after she landed on top of me."
    "It’s a good thing that I was able to abstain from molesting or raping her."
    "Now, we can still be friends."
    "Now, I can come to her room and laugh about the time I watched her orgasm and the way the juices that dripped onto my jeans looked when they dried on the walk home."

    scene black

    "Touka was right."
    "I should not have come here tonight."

    $ renpy.end_replay()
    $ yasudorm20 = True
    $ yasu_love += 1

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "She gently slides off of your body and squirms across the floor all the way back to her bed."
    "When she climbs inside, you think to yourself about how beautiful she is and how easy it would be to keep her locked inside of your room."
    "Her hair is white, so Ami would never even see it on the sheets when she washes them."
    "Everything about Yasu disappears into the bed, including your memory of the way she felt on top of you just moments ago."
    "When you return home, you try desperately to recall the shape and feel of her left nipple."
    "But instead, you give up and masturbate to a free pornographic video of a nun being gang raped."
    "DAY END."

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

label yasuspecial20:
    scene calmbeforethestorm1
    with dissolve2
    play music "phantomthief.mp3"

    "I find myself in my office after what could only be referred to as...one of the most {i}interesting{/i} nights of my new life thus far."
    "Not interesting in the way that involves dodging the end of the world with two of my niece’s closest friends, though."
    "Interesting in the fact that someone other than me was finally able to get Yumi to crumble, albeit in a much more...intentionally cynical and harmful way than my underlying compulsions of the past."
    "What that means for the future, I have no idea. Which is probably why I’ve taken it upon myself to seek shelter in here and let Imani handle homeroom for the day."
    "Even if my current thoughts on Nodoka are a bit “off” compared to how they were last week, I still don’t think I want to watch her get murdered."
    "And I can’t say I want to see Yumi, a girl that I feel I’ve been genuinely helping in many ways lately, throw all of that away because I preemptively got to see her naked."

    if nodokaspecial15p3 == True:
        "Naked and...attempting to pleasure herself while I looked on and did nothing, sure. "
        "But, like Nodoka said back then...that was going to happen eventually, right?"

        s "..."

        "I don’t know. Maybe I’m just grasping at straws in hopes of being able to pull myself out of the River Styx."
        "But seeing as I’m already on my way to Hades, I should probably just shut up and drown myself in its waters already."

    "Either way, the safest place for me right now is behind these doors."
    "For when I tear myself away from the harsh rays of the sun and slink back into the dark, I am somehow at my brightest and warmest."
    "And there is nothing that can or {i}will{/i} take that away from me."

    play sound "knock.mp3"

    to "Sensei, are you in there right now?"
    s "..."

    "I think for a moment that remaining silent will create one more barrier between what goes on out there and me."
    "But as a master of second guessing myself, I tear the barrier down in hopes that someone else will build one in my stead. "
    "And that the person at my door is only here to slink into the dark with me."

    s "Yeah..."
    s "I’m here."

    play sound "dooropen.mp3"
    scene calmbeforethestorm2
    with dissolve

    to "Wonderful. Please do something about Yasu."
    s "That’s a vague demand, but I think I get it."
    to "You do? So you’ve already been informed that she refuses to set foot in the classroom today?"
    s "I meant “get it” in the sense that there are many things that should probably be done regarding Yasu’s well being, but no. That is not something I was aware of."
    to "Well, now that you have been made aware, I will take my leave and pawn the rest of this problem off on you."
    s "But dealing with Yasu is {i}your{/i} thing. The last time I tried to do anything for her, she..."
    to "..."
    s "..."
    to "She what?"
    s "I just realized I should probably keep that to myself. "

    scene calmbeforethestorm3
    with dissolve

    to "Sensei, I have already agreed to assist Ms. Watabe with cleaning up the archery range this morning and can not afford to be late to something I {i}personally{/i} assured her I would be on time for."
    to "I may be Yasu’s current caretaker and...probably her legal guardian as well, but you are her teacher. Which means it is {i}your{/i} job to get her to go to class."
    s "Okay, sure. But what if {i}I{/I} was also planning on not going to class today?"

    scene calmbeforethestorm4
    with dissolve

    to "Did you hear that, Yasu? You get to spend the whole day in this delightfully drab room with Sensei. Oh, how fun."
    s "Touka-"

    play sound "dooropen.mp3"
    scene calmbeforethestorm5
    with dissolve

    to "Farewell! I have things to do and places to be!"
    to "And if she tells you she does not have lunch money, she is lying."
    ya "To lie would be one step short of a cardinal sin. I can not lie, for I have already incurred more of His wrath than I am able to handle."

    "Welp, I guess this is a thing I am dealing with now."
    "Here’s hoping she doesn’t climb on top of anything and start speaking in tongues again."
    "Though, I suppose if she’s going to have an orgasm anywhere in the school building, this is probably the safest room to do it."

    s "So...what’s going on? Why aren’t you going to class?"

    scene calmbeforethestorm6
    with dissolve

    ya "There are some doors that must remain closed. For the more people that set foot inside the areas they conceal, the closer those doors come to disappearing entirely."
    s "Can you say that again, but without the cryptic metaphor?"
    ya "Something bad is going to happen today."
    s "Something bad happens almost every day. But, based on what I experienced yesterday, you’re probably right."

    "How she can sense this beforehand is another question entirely, though."

    ya "This is different."
    ya "This is not His word, but the word of the world itself."
    ya "It speaks through the wind, backwards and under the cover of the shadows. The same language the cicadas speak. "
    s "Right. And how long have you been able to speak to bugs?"

    scene calmbeforethestorm7
    with dissolve

    ya "Bugs are my friends."
    s "Well, I don’t know what your friends told you, but premonitions aren’t really a viable excuse for not going to class."
    s "Besides, if you try to live your entire life avoiding confrontation, what are you going to do when said confrontation becomes unavoidable?"
    s "Face your fears now so they’ll be less scary later. Also, don’t you have, like...divine protection or whatever?"

    scene calmbeforethestorm8
    with dissolve

    ya "..."

    "Yasu grows silent (Something I can rarely say when I am alone with her) and stares at the corner of the room."
    "I imagine she’s mentally sorting through memorized religious texts pertaining to which sin “conflict” is and-"

    ya "I have not heard His voice since you last left my room."
    ya "I believe He is angry with me. But I do not understand what it is I did that would have angered Him."
    s "..."

    scene calmbeforethestorm9
    with dissolve

    ya "That...That is why I can not go to class!"
    ya "I will not know what the bad thing is until it happens! And if I am the one endangered and something bad happens to {i}me,{/i} what will become of Him when His voice returns?!"
    ya "It is my duty to protect the world! Mine alone! I can not do this if I am forced off of this plane before I am ready to leave!"
    s "You really can’t think of anything you did that would have angered your god?"

    scene calmbeforethestorm10
    with dissolve

    ya "All I remember about that night is the feeling of His warmth as it flooded my undeserving body. An outpouring of holy pleasure that I-"
    s "Okay, yeah. Let’s just leave it at “an outpouring of holy pleasure” and not think any more about it. "
    s "That night aside, though, I can’t imagine there is anyone in class that wants to hurt you, Yasu."
    s "You may be weird, but I don’t think you have any enemies. So if anything bad {i}were{/i} to happen, which it probably will, I doubt you’d be directly involved."
    s "I guess that {i}would{/i} call into question why the...wind and bugs informed you about it, though."

    scene calmbeforethestorm11
    with dissolve

    ya "The world did not speak to me directly- it was conversing with itself. Speaking alone for it has no one else to talk to. "
    ya "How lonely it must be to be the last of your kind."
    ya "I have felt the urge on many occasions to try and speak back to it, but I worry of what God would do to me if I shared my inner voice with anyone but Him."

    "I sigh to myself and try to figure out how I am going to deal with an entire day's worth of this."
    "It dawns on me after a moment or two of quiet contemplation that such a feat is impossible, and that this is probably why I have a student teacher in the first place. "
    "If I can get Yasu back to class, I can pawn the responsibility off on her and then leave before anyone is killed and go back to spending my time alone."
    "It’s not the most responsible of strategies, but it’s the easiest and least likely to result in a bout of mental exhaustion that will put me out of commission for the entire weekend."

    s "You have to go back to class, Yasu."

    scene calmbeforethestorm9
    with dissolve

    ya "But...the bad thing!"
    s "I’m sure that whatever “the bad thing” is will come to pass."
    s "At the very least, Imani and Makoto will be able to handle it a lot better than I can."
    ya "But-"
    s "No excuses. Go."
    ya "But-"
    s "Yasu-"
    ya "But I don’t know which way the classroom is!"
    s "What? You’ve been here for months."
    ya "Touka always grabs my collar and pulls me to where I am supposed to be. Without her, I am nothing. A worthless, discarded husk of a human- stuck to the side of a fence and waiting for the wind to blow me away."
    s "Ugh..."
    s "Fine. I’ll walk you back. But I’m not hanging around for long, got it?"

    scene calmbeforethestorm11
    with dissolve

    ya "Yes. Thank you. "
    ya "I am sorry for filling your day with these wasted words of mine that do less for your mind than the act of watching paint dry."
    s "That sounds like something you’d be into, given your tendency to stare at walls and whatnot."
    ya "I do not stare {i}at{/i} the walls. I stare {i}through{/i} them."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Okay. It’s time to leave."
    ya "Wait! My collar! "
    s "I’m not grabbing your collar, Yasu. It will make me look bad."

    "........."
    "......"
    "..."

    scene calmbeforethestorm12
    with dissolve2

    s "..."
    ya "..."
    s "Is the world speaking to you again?"
    ya "It speaks, but I can not discern the words."
    ya "Its tone is one of excitement...like it is anticipating what will soon befall us."
    ya "But what reason would one have to look forward to something that both sounds and feels like a bed of heated nails?"
    s "Some people just...like watching the world burn, I guess. "
    ya "The world is not who will burn. It is all of us who live inside of it that will."
    s "Well, at least we get to die together. That’s a plus, right?"
    ya "There is no death. Just-"

    scene calmbeforethestorm13
    with dissolve

    s "Oh, look. We’re here. And not a second too late."
    s "It’s been fun. But I’ll see you later, Yasu. Tell Touka that the next time she wants me to do her dirty work, she should-"

    scene calmbeforethestorm14
    with dissolve
    stop music fadeout 20.0

    ya "Wait. You have to come inside."
    s "That was not the deal."
    ya "The deal was that you will not hang around for long. You have not done any hanging at all."
    s "Does this not count as hanging?"
    ya "I am not an expert, but I don’t think it does."
    s "..."
    ya "..."
    s "Five minutes."

    scene calmbeforethestorm15
    with dissolve

    ya "Yay! Praise be!"

    scene black
    with dissolve2
    play sound "slidedoor.mp3"
    play music "10c.mp3"

    "Well, somehow or another, it looks like I have failed the only goal I put in place for myself today."
    "I slide the door open for Yasu in an attempt to let her in first. However, still being a little...uneasy about the fact that she’s about to come face to face with “the bad thing,” she clings to my arm for support."
    "And while walking into the class with anyone {i}else{/i} around my arm would probably be cause for concern, I can’t imagine it will be much of a problem with Yasu."
    "People will probably just see her without Touka and think that she needed some other body to absorb the life force of or something."

    scene calmbeforethestorm16
    with dissolve2

    f "..."
    ya "..."
    s "..."

    "Strike that."
    "If even {i}Futaba{/i} is looking at us with an air of skepticism about her, I’m sure it’s only a matter of time until someone else points this out as well."

    f "Umm..."
    s "If it helps clear the air at all, I didn’t want this either."
    s "Yasu is worried that something bad is going to happen today and...I guess she thinks I can protect her from that?"

    scene calmbeforethestorm17
    with dissolve

    f "Something bad? Like...what, exactly? It’s seemed like a mostly normal day so far."
    ya "Something that will shake the foundation of all that we know to its very core...An undeniable, horrible turn of events that will flip the world on its head, pouring all of us into the abyss in the process."
    ya "You should run while you still have the chance. You should wrap your arms around those you cherish and escape to an area outside the grasp of the sky’s mighty tendrils-"
    ya "For the moment they begin to extend in your direction, it is already too late. "
    ya "We are already doomed."
    s "So, yeah. This has been my morning so far."
    f "I’m...beginning to understand why you left Miss- Uhh...Why you left Imani in charge of the class."
    no "These...{i}tendrils{/i} that you speak of..."
    no "Can you tell me more about them?"

    $ renpy.end_replay()
    $ yasu_love += 1
    $ yasuspecial20 = True

    jump nodokaspecial20

label church25:
    scene clearnightsky
    with dissolve2
    play music "newhope.mp3"

    "Again, I find myself making questionable decisions and wandering off in directions I’m well aware I should avoid. "
    "I have never cared for gods or gospel...nor prayer, priests, or penance — but my affinity for mysterious creatures and those with blue eyes seems to outweigh that."
    "I am a simple man- cut from the cloth of a lecher’s bed sheets and doused in chloroform so that all I come into contact with will begin to fade out before I can learn to fade in."
    "It’s hot again. Customarily so. Which means I need to customarily inform you of that so you understand the stage and setting and don’t feel left out as I become further immersed in tonight’s selection."
    "While it may seem like we’re in this together, we both know I’m the only one dancing in the halls of harm’s way."
    "You can’t see the portraits that line the corridors. You can’t hear the faint half-melodies of an untuned piano ringing out in the distance — nor the hum of buried machines or whispering sky."
    "Only I can, because {i}I{/i} have been ordained to feel or hear or taste or experience these things all so that, one day, when I leave this place, I will be full of lingering sensations that will be fed to something bigger."
    "I mention not the gods, for I’ve already told you how I feel about them."
    "But what I {i}do{/i} mention is still lost...so I have followed my legs for a chance to find it."
    "Why do the trees still grow?"
    "Why does my cock still feast on the blood of my body and gorge itself on the fruits of my heart?"
    "Why do those fruits taste so good?"

    scene yasueyesagain1
    with dissolve2

    "The answer is that they don’t."
    "They’ve simply fallen at our feet and are too conveniently placed to avoid biting into."
    "You wouldn’t willingly go hungry, would you?"
    "I bet you’d cannibalize someone dear to you if it meant keeping yourself alive."
    "I know I would."
    "And perhaps I already do."
    "Just I eat from the inside out because saving the shells makes for a better collection than memories alone ever will."
    "For the nth time, I am being followed — and this fact alone makes me further question everything the girl I’m here to see has ever said to me."
    "This is supposed to be a safe place, isn’t it?"
    "The door is only meant to open for those it deems worthy, isn’t it?"
    "I wonder if the heavens are short on help."
    "And then I wonder why they won’t just open the gates to let it in."

    ya "..."
    s "..."

    "There is something for me here."
    "Something for me to take."
    "But how am I meant to find it if I can only see half of the room?"

    ya "Blessed be those who burn what they love...And surrender their senses to God up above."
    ya "Blessed be those who sever their ties...so summer can flourish and winter can die."
    ya "Blessed be spring...and autumn and more. Blessed be all that we wish to restore."
    ya "Blessed be sinners...and those who fall through."
    ya "But most of all, Akira...Blessed be you."

    scene yasueyesagain2
    with dissolve

    s "How did you-"
    ya "He told me."
    ya "He tells me all sorts of things. And it is on nights like tonight that He tells me the most."
    ya "Did you bring your own roll of duct tape? Or would you like to borrow some of mine?"
    ya "There’s plenty to go around. Just ask Muriel and you’ll be right beside me in no time at all."

    scene yasueyesagain3
    with dissolve

    s "I’m not going to tape my eyes shut, Yasu...Even {i}if{/i} you keep managing to...figure out things you’re not supposed to know."
    ya "What is the reason you hide your name?"
    s "Is that {i}you{/i} asking? Or your weird, eyeball god?"
    ya "There is nothing I ask for myself. I am but a vessel for all He wishes to know. And His interest in you grows deeper by the day."
    ya "Yet, now more than ever before, your distaste for the unburning light grows fiercer despite all that has happened to you."
    ya "Would it not be easier to surrender yourself altogether? Will breaking the chains that bind the false you to the real one truly be so terrible?"
    ya "Is it because you feel as if you can’t exist without them? Because, if that is the case, He wants you to know that you can."
    ya "And that He can make even the most hideous of shadows disappear by mixing them into your primary body...so it all merges into a single box with perfect corners. "
    ya "You can be more than you are now...but not while you are being followed. There is someone else who deserves that honor. And whatever it is that is tied to you should be consumed in its entirety."

    scene yasueyesagain4
    with dissolve

    s "Is something...actually following me? Because I’ve been getting these strange feelings lately that-"
    ya "We’re all followed by something- be it ghosts of the past or glimpses of the future. Which is why we must sever all unneeded ties...so we can better envelop ourselves in the present. "
    ya "For only then will we notice when we are called upon."

    scene yasueyesagain3
    with dissolve

    s "Gotcha. So it was just another generic, religious generalization after all. "
    ya "The Church of New Hope is no generic religion, Sensei. It is the one true path — and all who do not follow it are simply dooming themselves."
    s "You realize that’s basically what every other major religion thinks as well, right?"
    ya "It is not my place to {i}realize{/i} things when all I could ever want to know is simply injected into me in the moments I’m connected to Him."
    ya "But if it is other {i}religions{/i} you would like to speak about, please sit. You’ve arrived at the perfect time."
    s "Oh yeah? Is this your annual meeting to discuss how you’re going to promote yourselves and convert all of the “non-believers?”"
    ya "They will convert themselves when they realize they need to. "
    ya "What we are doing today is reaffirming our love for Him and reminding ourselves of why it is He we follow in the first place."

    play sound "static.mp3"
    scene yasueyesagain5 with flash
    stop sound

    ya "Another shift in seasons approaches — and with that marks the coming of six more months of dormancy."
    s "Here’s...hoping you bought a heavier jacket, I guess?"
    ya "You’d think I would need one, yes? As summer and winter are all we have here, we transition from one extreme to the next — instantaneously at that."
    ya "But do you know {i}why{/i} things are the way they are? "
    ya "Do you know why we do not have three months of temporary stasis in between those two extremes, Sensei?"
    ya "It is because autumn and spring have been taken from us."

    scene yasueyesagain6
    with dissolve

    s "Taken?..."
    ya "Consumed! By those who wish for a fraction of the omnipotence He possesses! And it is {i}we{/i} who are forced to suffer due to their fruitless pursuit of untapped power!"
    ya "The world we love is only the world we {i}hate{/i} as a result of needless tampering with the rules and systems that guide us!"
    ya "Picture it! The reds and yellows of the fall! The pinks and blues of springtime! It is as if color itself has been taken from us!"

    scene yasueyesagain7
    with dissolve2

    ya "Which leaves black..."
    ya "And {i}white.{/i}"
    ya "One is everything. One is nothing."
    ya "But their simultaneous existence does not cancel anything out. It’s just the opposite."
    ya "An endless game of tug of war between two forces we can not see. One everything. One nothing. And you would expect everything to win, would you not?"
    s "Uhh..."
    s "I guess?"
    ya "There is a third element to this game of tug of war."
    ya "Do you know what it is?"

    scene yasueyesagain8
    with dissolve

    s "I have absolutely no idea..."
    ya "It is the {i}rope.{/i}"
    s "Right, yeah. That explains everything."
    ya "It explains nothing...and there is no way you’ll ever understand at all if you approach my message with doubt."

    scene yasueyesagain9
    with dissolve

    s "Fine...Go ahead."
    ya "Black...White...And all that lies between."
    ya "These are the three great divines — but only one can be the {i}greatest.{/i}"
    ya "Those of us who seek the truth and gaze upon this never ending battle will side with the right or the left as those are the two fighting the hardest."
    ya "What they can not seem to grasp is that there’s danger in what lies between. "
    ya "If the rope were to snap, who would be the winner? The one with the largest piece? The one who keeps their feet planted after the tear?"

    play sound "static.mp3"
    scene yasueyesagain10
    with flash
    stop sound

    ya "Or would no one win?"
    ya "Would the game simply begin again...with a brand new rope?"
    s "I..."
    s "Again, I have no idea. None of this ever makes sense to me."

    play sound "static.mp3"
    scene yasueyesagain11 with flash
    stop sound

    ya "That is because you don’t want it to!"
    ya "You, a child {i}born{/i} to someone who understood, should understand if anyone!"

    scene yasueyesagain12
    with dissolve

    s "What?..."
    ya "The rope has a mind of its own! It chooses when it tears and lures those who grip it into believing the outcome is not predetermined!"
    ya "Even the most perfect, amazing, divine entities are not without those who would wish away their love! And it is up to us, the children, to tell the world of this! "
    ya "To preach about the injustices of braided horsehair and carve out a hole in the world so the colors will have a place to return to once the time has come to reclaim them! And that time is approaching!"
    ya "The dawning of a new season is upon us, but which one will it be?! One of the two we already know?!"
    ya "{i}Or a third one?...{/i}"
    ya "{i}A new one?...{/i}"
    ya "One that no one sees coming but {i}me...{/i}For it is I who understands. It is I who will sing His songs to the choir of sinners and sodomites! Only then, will everyone know to believe me!"
    s "Yasu, what...what were you saying about my birth just now?"

    stop music
    play sound "static.mp3"
    scene yasueyesagain13 with flash
    stop sound
    play music "undoitall.mp3"

    ya "That you are the product of something wonderful."
    ya "You learned to crawl in the light of someone who understood the {i}importance{/i} of that light."
    ya "If you listen closely, you’ll hear her voice. "
    ya "She whispers your name. Reminds you of a time when things were better. Before that light began to dim and you were forced to crawl in the dark instead."
    ya "If I had met you back then, I would have loved you. "
    ya "I would have given you the care you needed instead of allowing you to scamper off into the wrong side of everything."
    ya "I would have been your mother Mary, and you would have been the fruit of my virgin womb — bathed in frankincense & myrrh and blessed by everyone around you as a true son of God."
    ya "But it is not too late."
    ya "I can still show you who you are. "
    ya "I can reveal the voice of the one who follows you."
    ya "All you need to do is take my hand."
    ya "I will be your shepherd."
    s "I..."
    s "No. I don’t believe you. This is all just...mindless rambling. You’re insane. You’ve been brainwashed by some crazy neo-religion that’s taken over the {i}real{/i} you. This isn’t who you actually are."
    ya "But it is."
    ya "And the amount of proof at my disposal would shock even you — who has seen it all several times over."
    s "You can’t do anything for me that I can’t do for myself."
    ya "I can. But only with His assistance. "
    ya "See this side of the world with me."
    ya "And make me yours so that one more child will learn to crawl in the light instead of suffocating in the dark or being strangled by the rope."
    s "Yasu-"
    ya "Return."
    s "Return where? What-"

    scene yasueyesagain14
    play music "daybreak.mp3"

    s "..."
    s "..."
    s "..."
    s "Where am I?..."

    play sound "static.mp3"
    scene yasueyesagain15 with flash
    stop sound

    ya "Somewhere only He can take you."
    ya "Breathe in deeply...and fill your lungs with the nostalgic air you’d wake up to every single day before you lost touch with the meaning of this world."
    ya "I ask...does this seem like a callous gesture to you? Or does it look more like a present from a righteous god who simply wants you to feel as if you belong?"
    ya "All of this and more is what you’ll see with me."
    s "Yasu...how are you even..."
    ya "How am I what?"
    s "How are you...doing this?"
    ya "The answer to that is simple."

    scene yasueyesagain16
    stop music

    ya "I’m not."
    ya "You just think I am."
    ya "And you only think that because, deep down, you believe. "

    play sound "static.mp3"
    scene yasueyesagain17
    with flash
    stop sound
    play music "newhope.mp3"

    ya "Deep down, you know that you are special."
    ya "You know that the visions you have are far more than just illusions."
    ya "You know that the world you’re in is not one of logic — but something different. "
    ya "And you know that I know more about it than you."
    s "..."
    ya "With that said, what excuse will you come up with to deny me once more?"
    ya "How will you reject the word of God when it clings to the back of your throat, desperate to escape?"
    s "..."
    ya "I will be your shepherd."
    ya "I will help you regain what it is you’ve lost...and assist you in obtaining more than you’ve ever wanted along the way."
    ya "The rope is fraying, Sensei."
    ya "Which side will you be on once it snaps?"
    ya "And who will you believe in when everyone {i}else{/i} you trust betrays you?"
    s "..."
    ya "Will you walk away again?"
    ya "Or will you sit with me and bask in His glory?"
    s "..."
    ya "..."
    s "..."
    ya "..."

    scene yasueyesagain18
    with dissolve

    s "Yasu..."
    ya "Yes?"
    s "I don’t believe in God..."
    ya "I know."
    ya "But everything would make more sense if you did...and {i}that{/i} is what you’re after."
    ya "Time is running out."
    ya "And you will need somewhere to hide when your world begins to crumble."
    ya "This will be that place for you. "
    ya "And with your help, He will rise again."
    s "And...{i}without{/i} my help?..."
    s "What would happen then?"
    ya "..."
    s "..."
    ya "..."
    s "Yasu?..."
    ya "Will you sit? "
    ya "Or will you walk?"
    s "..."
    ya "..."

    scene yasueyesagain19
    with dissolve2

    ya "Heheh....ahahehah......heaahehahehahheuhuhehehe!"
    s "Just to clarify, I’m not agreeing to join your church. I just...I’d be lying if I said I wasn’t interested in hearing a little more of...{i}your{/i} side of things."
    s "You’ve been right more often than not so far and..."
    s "And it’s always good to have somewhere to hide."
    ya "So it begins..."
    ya "After so long...it finally begins!"
    s "Please don’t make me regret this."
    ya "Sensei..."
    ya "You won’t regret this {i}at all.{/i}"
    ya "You’ve saved yourself from ruin. "

    play sound "static.mp3"
    scene yasueyesagain20 with flash
    stop sound

    ya "But, I wonder..."
    ya "Which domino will have to fall in your place?..."

    scene black
    with dissolve2
    stop music fadeout 8.0

    "I fall asleep on a stone pew in church so cold you would never know it’s summer."
    "I don’t wake up until I’m halfway home."

    $ renpy.end_replay()
    $ church25 = True
    $ yasu_love +=1

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yasudorm25:
    scene dorm2
    with fade

    if _in_replay:
        play music "sweetvermouth.mp3"

    "I make my way over to the dorm and find that things are significantly quieter on this floor than normal. "
    "Typically, I’d be accompanied by the sound of Molly yelling at some game, Noriko blasting music, Io banging away at some sort of craft, Nodoka throwing things around, and-"
    "Actually, now that I think of it, Dorm 9 is kind of an outlier here."
    "Yasu might be clinically insane and a delusional cultist, but whenever she’s in her room, she’s normally just...staring at the wall. And Touka’s rather quiet and polite to begin with, so..."
    "You know what? Maybe I’ll spend some time with them tonight."

    menu:
        "Knock on the door of Dorm #9":
            scene yasudormevent1
            with fade
            stop music

    "When I step in front of the door, I realize that they’ve changed their sign."
    "I liked the older one more as it didn’t remind me of my least favorite letter or any sort of religious symbolism."
    "Well, apart from the number 9’s suggested correlation to finality or completeness and how it is subsequently and commonly associated with the death of the Messiah, Jesus Christ of Nazareth."
    "I am not a Christian — I am not {i}anything.{/i} But I {i}would{/i} have liked to grab a beer with Jesus if the two of us were ever alive at the same time."
    "There wasn’t much else to do back then, so I’m sure he’d be able to hold his liquor. And I’m doubly sure since he apparently bled wine or however it’s supposed to go. "
    "I’m no expert, so don’t take my word."
    "I think for a moment about what I want to do when I enter the room- but I know in my heart of hearts that anything I desire now will be slaughtered the moment I make eye contact with Touka’s boobs."
    "She has really good boobs."
    "I wish it was her who became possessed by a false god only to tackle me and have an accidental orgasm while her eyes roll to the back of her head and drool drips out of her mouth and onto my face."
    "It’s a very specific thing to want, which means it likely will not happen."
    "And if I am to relive such a situation again, it will probably be with Yasu."
    "Her boobs aren’t as nice. They’ve barely started growing. And I can’t help but feel like she’d be less fun to have penetrative sex with because she’d likely be preaching or crying the entire time."
    "I don’t want to deal with that."
    "Instead, I will hearken back to the thoughts I had of liquor just moments ago and make a trip to the alcohol shop so I can get the two of them drunk and plug their holes with my man meat without being remembered."
    "It’s the best way to do sex since I’d be able to move their bodies however I want."
    "I just hope they can’t drink as much as me."

    scene yasudormevent2
    with fade
    play music "stopwind.mp3"

    "I turn around to begin-"

    ya "..."
    s "..."

    "I forget what I was beginning to do."

    ya "..."
    s "..."

    "Yasu stares at me and the earliest signs of my erection begin to subside and convert me back into my normal form — Flaccid Dick Boy, Kid Bandit."
    "It’s a nickname I received on the playground a long time ago after having my gym shorts pulled down by a girl in the grade above me who wanted to see a penis for the first time after learning about them in health class."
    "She asked if she could touch it and I said no, so she began to call me names. Flaccid Dick Boy, Kid Bandit was one of them."
    "She was a very strange girl."
    "But not as strange as this one — who probably doesn’t even want to see my penis."
    "What’s up with that?"

    ya "Are you lost, little lamb?"
    s "Nope. Just heading over to the liquor store."
    ya "The consumption of alcohol will only taint your body. You must keep yourself pure so God does not get drunk on your light when he collects it in your sleep."
    s "Wow, way to be a buzzkill."
    ya "I ask you, Sensei...where do you think you are right now?"
    s "The dorms, obviously. "
    ya "But where do you think the {i}dorms{/i} are?"
    s "..."
    ya "..."
    s "Kumon-mi?"
    ya "It’s funny how looking at things from a different angle can change all you know to be real. "
    ya "It’s even funnier how you can ignore that until it’s pointed out to you."
    s "Uhh..."
    ya "This is how it always looks — half complete. Just like you."
    ya "It’s the same place you visit every single day, but brand new at the same time as it’s a side of it you’re never {i}meant{/i} to see."
    ya "But this is {i}all{/i} I see whenever you’re away."
    ya "This abyss is my only company every single Thursday."
    s "That’s not true. You normally have Kirin as well."
    ya "Kirin only exists when you need her to. The same way the dorms only exist when you need them to."
    ya "But what becomes of us whenever you don’t? "
    ya "Does a hummingbird hum when it runs out of songs?"
    s "Yasu, I don’t mean to “Um, actually” you in the middle of philosophical speech, but I’m pretty sure they’re only called hummingbirds because their {i}wings{/i} hum. Not because they sing."
    ya "Is that your only concern when being faced with the truth? You’re more worried about why things are called what they’re called than who decided to call them that?"
    ya "You came to me in search of salvation, did you not? If you truly wish to learn, you will need to put more thought into my words."

    play sound "static.mp3"
    scene yasudormevent3 with flash
    stop sound

    ya "When everyone disappears, there is a special bridge that forms."
    ya "It extends beyond the abyss into another plane that only the purest of young girls can reach — and every door and every number turns to ash to be carried away with the breaths of the sky."
    ya "It all looks like this — unfinished and underwhelming. But empty space does not fit in with our ideal reality, so we reject it."
    s "...W-"
    ya "Why are {i}we{/i} the ones who sleep apart?"
    ya "Why is {i}our{/i} home the one left incomplete?"
    ya "And what is the need for so many floors when there are so few of us?"
    s "Yasu, you’re starting to-"

    play sound "static.mp3"
    scene yasudormevent4 with flash
    stop sound

    ya "Scare you?"
    ya "Make you uncomfortable?"
    ya "It is all for good reason."
    ya "It is all so one day, you will enter me. And we will create a new lifeform unlike anything the world has ever seen."
    s "I really don’t-"
    ya "It’s time to go."
    s "Go where? Where are-"

    stop music
    scene yasudormevent5
    play sound "eggcrack.mp3"

    "..................................."
    "......................."
    "......"

    scene yasudormevent6
    play sound "pop.mp3"
    play music "bloodandsunset.mp3"

    "I am born."
    "In my second coming, I become reacquainted with the inside of a uterus and how terrifying it is to see light for the first time."
    "And while it may look like I lack the eyes required to see {i}anything,{/i} I can assure you that isn’t true."
    "A soft hand guides me down a flight of stairs that I can feel, but what lies before me in this temporary realm is much different than any stack of sturdy rectangles."
    "A ticking clock and the equally repetitive noise of a door opening and closing."
    "The sounds of animals fighting over scraps of food plucked from trash cans by scavenger birds and dropped before they were able to be safeguarded."
    "The soft hand reminds me that I am no scavenger bird, but a piece of trash — waiting to be ripped to shreds or torn apart by something that sees me as weak."
    "It is quite possible the hand is only leading me away from my happy place because it wants to do this."
    "My bones will go on to form the base of its nest and my skin will make an excellent jacket after being cured and tanned. "
    "My phallus and testicles may be preserved for personal use or eaten fresh depending on the predator’s personal preferences, but I like to believe they’ll simply be left alone."
    "I am a lost, little lamb- and the outside world is scary."
    "That’s why I found a shepherd."
    "That’s why I’ll keep her close."

    ya "{i}Wake up.{/i}"

    stop music
    play sound "static.mp3"
    scene yasudormevent7 with flash
    stop sound
    play music "andlove.mp3"

    if makotofutabafuntimelustevent == True:
        "I blink and wind up in a somewhat familiar place — filled with memories that may be good for me but not so much for others."
    else:
        "I blink and wind up in an unfamiliar place — full of trees and leaves and other things."

    "The wind is blowing hard, but none of the foliage is moving- and it appears that only {i}I{/i} am feeling the effects of this."
    "Did I black out again?"
    "Did something happen in the dorms that triggered it?"

    scene yasudormevent8
    with dissolve

    "And why am I with Yasu of all people?"
    "Did she follow me? "
    "Was this {i}her{/i} idea?"
    "Am I even here at all? Or could this be another mind-game she’s attempting to-"

    ya "Thinking too hard will only make things more difficult for you."
    ya "In order to fully grasp the underlying purpose in all of this, you must free your mind from the walls you’ve built around it and devote yourself to the cause."
    ya "Only then, will you fully secure the hiding place you seek. And only then will you avoid ruin."

    scene yasudormevent9
    with dissolve

    s "Yasu, where are we? Why did you take me here?"
    ya "You asked me to shepherd you...I am simply doing as you wish."
    s "I didn’t {i}ask{/i} you to do that. It’s something you decided on your own."
    ya "While the words did not cross your lips, it is what you agreed to when you joined me on the pew. And so it is here where I will teach you something new."
    ya "But know that even the most experienced of shepherds often struggle to corral the most disobedient sheep — and that none of this matters at all if you do not {i}obey{/i} to some extent."
    ya "He can give, but only so much. And that directly influences what you should {i}take.{/i}"

    scene yasudormevent10
    with dissolve

    s "Can you maybe shepherd me back to the dorms now? The last time I got lost in the woods with a weird girl, I became an accomplice to child abduction."
    ya "You’ll return after you’ve learned today’s lesson."
    s "Well...what’s today’s lesson?"

    play sound "static.mp3"
    scene yasudormevent11
    with flash
    stop sound

    ya "What is and isn’t real."
    ya "As a man who has seen God, it would not be unusual for you to see {i}other{/i} things as well. "
    ya "Only He can show you how to discern fiction from reality as it is He who determines what can and can not exist in our world."
    ya "Everything flows through our precious God. And it is in the depths of the rivers of His infinite wisdom that insignificant worms like us learn to see {i}without{/i} our eyes, but with something else."
    s "You’re not going to say “our hearts,” are you?"
    ya "If only it were that simple."
    ya "The concept of reality is one of great interest to Him as there have been others in the past just like you — who craft wings of feather and wax only to fly too close to the sun in the days that come next."
    s "Uhh..."
    ya "What I am saying is that you should not get too close to that which does not exist — for it is a greater danger to you than anything else you could ever imagine."
    ya "This world is a wonderful one, but there are things trying to exist here that simply shouldn’t."
    s "Well...how am I supposed to know what’s real and what’s not if only {i}He{/i} can tell or whatever? How is any of this helpful?"
    ya "I haven’t told you how to see without your eyes yet. Of course you’d be confused."
    s "Then tell me, Yasu. Because if you really want me to {i}learn{/i} any of this, you’re going to need to cut back on these long-winded speeches."
    ya "You must learn to see through His eyes instead."
    s "Oh, okay. So the big lesson when it comes to figuring out what’s real and what’s not is to just pretend some {i}god{/i} sees it instead and already knows the answer. "
    s "That way, I can just decide what exists on my own and rationalize it as divine truth when, in all actuality, it’s just a big game of pretend and imagining something is real when it’s not."

    play sound "static.mp3"
    scene yasudormevent12 with flash
    stop sound

    ya "That is where you’re mistaken."
    ya "Everything you can imagine is real."
    ya "If you think there aren’t enough stars in the sky, make more."
    ya "If you think the moon is too small or the sun is too large, change their shapes or sizes."
    ya "Learning to sever the invisible cord tying your imagination to the realm you reside in is the key to making everything you want reality."
    ya "It could even help you see someone you’ve {i}longed{/i} to see for many years."

    play sound "static.mp3"
    scene wearethechildren13 with flash
    scene yasudormevent12 with flash
    stop sound

    ya "It could help you {i}touch{/i} them."

    play sound "static.mp3"
    scene wearethechildren13 with flash
    scene yasudormevent12 with flash
    stop sound

    ya "{i}Inseminate{/i} them."

    play sound "static.mp3"
    scene wearethechildren13 with flash
    scene yasudormevent12 with flash
    stop sound

    ya "Why, you could do anything you want. "
    ya "That is the type of world we live in. {i}That{/i} is the type of place He has created."
    ya "But only those willing to unchain their minds will be able to make the most of this."

    scene yasudormevent13 with dissolve

    ya "Others will call you crazy...because they don’t understand. But how could they?"
    ya "They haven’t felt the warmth emanating off the hand of God — or filled their palms with sakura petals just to toss them in the air and let them rain down in a flurry of color."
    ya "They haven’t felt anything at all, because they’ve already determined what they can and can not see. "
    ya "They’ve made the mistake of defining their realities before learning their place in the world...while people like {i}you{/i} were never able to do that."
    s "What...do you mean?"

    play sound "static.mp3"
    scene yasudormevent14 with flash
    stop sound

    ya "{b}I MEAN YOU’RE FULL OF WORMS! PLACED THERE BY SOMEONE YOU THOUGHT YOU COULD TRUST!{/b}"
    ya "{b}There was never a chance for you to define a reality because you were too busy trying to survive in the one that was left there for you!{/b}"
    ya "{b}In the shadow of those dying lights that danced across your wall as cars passed by, you prayed for something more! Did you not?!{/b}"
    ya "{b}As you hid beneath the covers and wished the world would end, you prayed someone would take you away! DID YOU NOT?!{/b}"
    ya "{b}Then, when someone finally {i}did,{/i} you prayed they’d send you back! You prayed you never learned to feel at all!!!{/b}"
    ya "{b}DID YOU NOT?!?!?!?!?{/b}"
    ya "{b}Your life has been nothing but praying! Praying and hurting and hurting and praying! And {i}now{/i} you laugh in the FACE OF GOD because he never answered you BACK THEN?! NOW?!{/b}"
    ya "{b}THE REASON YOU HURT AS MUCH AS YOU DO IS BECAUSE YOU THREW HIM AWAY!{/b} "

    play sound "static.mp3"
    scene yasudormevent15 with flash
    stop sound

    ya "But He will take you back..."
    ya "Because He is all-forgiving."
    ya "He is all-loving."
    ya "And you’re just a container for wiggling detritivores, relying on a {b}RETARDED VIRGIN CUNT{/b} to come and {i}save{/i} you instead of figuring out a proper coping mechanism. {b}GET REAL, FUCKER.{/b}"
    s "..."
    ya "..."
    ya "Eat shit and die."
    s "Who..."
    s "Who...{i}are{/i} you?..."

    play sound "static.mp3"
    scene yasudormevent16 with flash
    stop sound

    ya "Ah..."
    s "..."

    scene yasudormevent17
    with dissolve2

    ya "W..."
    ya "What..."
    ya "What’s?..."
    s "..."

    scene yasudormevent18
    with dissolve2

    ya "Ahh..."
    ya "Ah?..."
    s "Yasu, are you...okay?"

    scene yasudormevent19
    with dissolve2

    ya "D..."
    ya "Don’t look at me..."
    s "Yasu, I think something might be-"

    scene yasudormevent20
    with dissolve2

    ya "I SAID DON’T LOOK AT ME!!!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I slowly back away and press myself up against the base of a well."
    "And it isn’t until I hear her wring her dress out in the water that I understand what must have happened."
    "........."
    "......"
    "..."

    scene clearnightsky
    with dissolve2

    "Something’s wrong with Yasu."
    "It’s not just religious fanaticism. "
    "There’s something inside her."
    "And I don’t know how to get it out."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yasudormevent21
    with dissolve2

    ya "..."
    s "..."
    ya "Please...don’t tell anyone...what happened..."
    s "I won’t..."
    s "If anything, this is the most human I’ve seen you all night."
    ya "I don’t..."
    ya "I don’t remember where or..."
    ya "Or why we were..."
    s "Just go to sleep, Yasu. You’ll be better in the morning."
    ya "I..."
    ya "I have to...take a shower..."
    s "Right. Yeah."
    ya "..."
    s "..."
    s "Well, uhh..."
    s "I guess I’ll...see you later then?"
    ya "..."
    s "..."

    play sound "dooropen.mp3"
    scene yasudormevent22 with dissolve

    "Yasu heads back into her room without saying goodnight."
    "And I’m kind of glad she does..."
    "Because it spares me the possibility of making her even more confused."

    scene black
    with dissolve2

    "We had to take a taxi back from the beach."
    "It put a hole in my wallet just as large as the one in my chest."
    "Tonight, I awoke in a strange clearing with a girl from my class."
    "Or at least something using her body."
    "..."
    "I’m worried about her."

    $ renpy.end_replay()
    $ yasudorm25 = True
    $ yasu_love += 1

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yasudorm30:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Yasu’s door and wait for her to answer."
    "But given that this room also belongs to someone who is more socially competent {i}and{/i} not busy staring at a wall, I think it’s safe to assume her roommate will be answering instead."

    to "The door is open, Sensei. Come in."

    scene black with dissolve
    play sound "dooropen.mp3"

    "My assumptions are proven correct for the umpteenth time — and now comes the part of the night where I have to explain to Touka that I’m not actually here to see {i}her,{/i} but her friend."
    "Though, I do worry just how much she’s heard about one of our more recent encounters."

    scene yasuflashback1
    with dissolve2

    to "Good evening, Sensei. And sincerest apologies if you are not in the mood to be confronted, but I have a bone to pick with you."
    s "Can the bone be my penis? Because I’m never in the mood to be confronted, but am willing to make an exception so long as it’s that one."
    to "You do realize there are no actual bones in that part of your body, correct?"
    s "I do, Touka."
    to "Are you absolutely sure? Because there are many things you have both said and done in the brief time we’ve known each other that have led me to believe you’ve never received {i}any{/i} formal education whatsoever."
    to "Like that time you took poor Yasu out in the middle of the night to {i}God knows where{/i} and she came back a blubbering, shameful mess."
    s "Yup, here we go. I was right to worry."

    scene yasuflashback2
    with dissolve

    to "What were you thinking? Why would you even {i}contemplate{/i} doing such a thing when you are {i}fully{/i} aware that Yasu requires...special attention? "
    s "Let me just put my foot down now and say that wasn’t my idea at all. In fact, I’m pretty sure {i}neither{/i} of us wanted to go as far out as we did. But that’s what happened and I’m willing to take responsibility for it."
    to "Don’t you go trying to talk your way out of-"

    scene yasuflashback3
    with dissolve

    to "Wait one moment. Did I hear that correctly? You are...{i}actually{/i} going to take responsibility for this? You’re not just fooling around with me again?"
    s "Yes, but only because I think there’s something weird going on with Yasu and I’d rather talk about {i}that{/i} than the main reason you’re likely concerned about all of this."
    to "Of course there is something weird going on with Yasu. She is a weird girl. Everything she {i}does{/i} is weird."

    scene yasuflashback4
    with dissolve

    to "Just look at her- off in her own world and completely unaware that we’re even discussing her. That’s no fault of her own, though. I’ve realized by now that it’s simply the way she is."
    s "Yeah, sure, but...do you ever think there might be more to it than that? That she isn’t just...abnormal or whatever, but...that there might be some element of truth to all the crazy things she says?"

    scene yasuflashback5
    with dissolve

    to "I suppose so. But, concerning that aspect of her personality, however major it may be...I don’t think I’d put her on a level much different from any other fanatic."
    to "There are elements of truth to all forms of spirituality, and it’s not uncommon for multiple schools of belief to follow the same tenets while dressed up in different clothing."
    s "That’s not what I mean. Though, I will commend you on that surprisingly mature outlook."

    scene yasuflashback6
    with dissolve

    to "It’s to be expected. I’m a surprisingly mature young woman after all."
    s "Please don’t say things that you know are going to give me ideas."
    to "I see no harm in saying such things when those are ideas you already have in the first place."
    s "..."
    to "..."
    s "{i}Anyway...{/i}what I meant is that being around Yasu has been affecting {i}me{/i} lately. In ways much different than just getting annoyed by her endless spiritual rambling."

    scene yasuflashback7
    with dissolve

    to "Affecting you {i}how?{/i} "
    s "It’s hard to say. Just..."
    s "Between predicting the future and...knowing things she’s not supposed to know about me, it’s like she’s getting into my head. In a way that nobody else really has before."
    to "I’m not quite sure I follow..."
    s "I’ve been...{i}seeing{/i} things when I’m with her. "
    s "Things that...might be real or...might {i}not{/i} be real. And at other times, it feels like something might be speaking {i}through{/i} her. Do you know what I’m talking about?"
    to "To be frank...no. I haven’t experienced anything like that with Yasu. Though, I {i}can{/i} see why that would be alarming."
    to "What is this about predicting the future, though?"
    s "Before Makoto’s dad died, Yasu kept talking about how something bad was about to happen. And before that, I think she might have predicted when the seasons were about to change."

    scene yasuflashback8
    with dissolve

    to "Hmm...To be honest, I’m not sure I’d count either of those things as “predictions.” They sound more like the same generalizations psychic mediums tend to make."
    to "Of course the seasons are going to change. And of course bad things are going to happen. I wouldn’t put too much faith in Yasu’s ability to “predict the future” because of that. "
    to "She’s likely just ___________."
    s "...She’s what?"
    to "_____________. I wouldn’t ________ if __________."
    s "..."
    s "Touka?"

    scene yasuflashback1
    with dissolve

    to "______? ________________________. __________________."
    s "..."
    to "______?"

    stop music
    scene black

    "connection severed."
    "redirecting consciousness."
    "yasu yasui is defective."
    "readers are urged to dismiss any and all information relating to her character and dialogue."
    "there are more important things we must be doing."
    "and you only have so much space left inside of your head."
    "do not waste it on those who give away themselves to others."
    "for if you do, you’ll have nothing left to give yourself."
    "........."
    "......"
    "..."
    "REDIRECTION INTERCEPTED"

    play sound "static.mp3"
    scene yasuflashback9 with flash
    stop sound
    play music "memories.mp3"

    "INITIALIZING “FLASHBACK MODE”"
    "“FLASHBACK MODE” INITIALIZED"
    "LAUNCHING “AFFECTION” PROTOCOL AND “EMOTION” CONTENT PACK"
    "CONTENT LOADED"
    "//////////////DISGUISE EQUIPPED"
    "//////////////TRUST NO ONE"
    "//////////////NOT EVEN GOD"

    q "{b}I CAN’T DO IT ANYMORE!!!{/b}"
    doc "Mrs. Yasui, please calm down. This is far more common than you think."
    yamom "Common?! This is {i}common?!{/i} You can’t even explain what’s wrong with her! How is this {i}common?!{/i}"
    yamom "You’re the twelfth doctor we’ve seen this year and every single one of you offers up the same GOD DAMN EXPLANATION! I’M TELLING YOU YOU’RE WRONG!"
    doc "Mrs. Yasui, with all due respect, if you’ve received the same diagnosis from every professional you’ve taken young Yasu to, it’s quite likely you’re misunderstanding something. Again, with all due respect."
    yamom "Oh, fuck you. Fuck all of you. You’re all fucking quacks."
    doc "Mrs. Yasui, please listen-"
    doc "Schizophrenia is far more complex than someone who just “hears voices in their head.” It’s a brain disorder that effectively manipulates every aspect of a person’s life from their speech to their behavior."
    yamom "Then explain how she keeps predicting everything! Or why my husband’s starting to see things now as well! Or how she can mimic the EXACT WAY my dead mother used to speak despite never even meeting her!"
    doc "It’s unfortunately impossible to explain any of that as it’s likely all due to coincidence."
    yamom "Oh, wow! Coincidence! Why didn’t I think of that?! Thanks so much, doctor! That extremely valuable information was totally worth the specialist charge!"
    doc "I understand your concerns with the diagnosis but, unfortunately, there’s still a great deal we don’t understand about schizophrenia as it has a direct impact on a person’s ability to perceive reality."
    doc "There is no way we can ever see or replicate what {i}Yasu{/i} sees as this is all happening in {i}her{/i} head."
    yamom "Sure, yeah. And her head just {i}happens{/i} to know everything that’s going to happen in the future. Got it."
    doc "Again, that is likely just coincidence combined with an overactive imagination."
    yamom "Do you know what she told me this morning, doctor? She told me the world was going to end. She’s {i}eight.{/i} She’s fucking eight! What am I supposed to say to that?!"
    doc "I’m afraid I’m in no position to offer you parental advice, Mrs. Yasui."
    yamom "Yeah, you’re in no position to offer me medical advice either but here we fucking are."
    doc "I can assure you I’m perfectly qualified to provide medical advice and that not heeding it could result in an even more dangerous future for your daughter."
    doc "If left untreated, schizophrenia could lead to an increased probability of suicide or-"
    ya "I don’t feel good..."
    yamom "This. {i}This{/i} is what your treatments are doing. We’ve put her on every fucking medication you idiot doctors have prescribed and she can’t keep any of them down!"
    doc "She’s vomiting after taking the medication?"
    yamom "Yes! Every fucking time! That’s what I just said!"
    doc "Have you noticed whether or not the capsules are being regurgitated as-"
    yamom "Yes! They are! And I’m tired of fucking sifting through puke because none of you can figure out what to do with her! I can’t afford this anymore!"
    doc "In regard to the medication and your daughter’s circumstances, I’m able to provide a referral to a clinic not far from here that offers antipsychotic injections that may help to alleviate her symptoms."
    doc "Unfortunately, we’re unable to provide such services here."
    yamom "Great. A thirteenth clinic. Why not refer me to a few more as well? Think I’ll shoot for twenty by the end of the month."
    yamom "I’ve already had to quit my job to look after her since every fucking school we’ve tried to take her to has turned her away. Not like I have anything else going on since this is just my fucking life now."
    doc "I understand that this is hard, but...back to the injection, it is important to note that this is not something we typically recommend for children as there is an elevated risk for serious side effects."
    doc "The medication will target your daughter's neurotransmitters...serotonin, dopamine, and so forth...and will remain in the bloodstream for several weeks, where it will slowly-"
    yamom "Whatever. Okay. Fine. Added risk makes no difference to me."
    doc "If you’re positive that this is the direction you want to take, I can write the referral now."
    doc "Though, in regard to comments you made on your husband earlier — if he {i}is,{/i} in fact, having visions as well...it’s quite possible Yasu inherited this disorder from him as schizophrenia does run in-"
    yamom "It didn’t come from him! He was fine until {i}she{/i} showed up! Now, he’s afraid to even make eye contact with her! She’s ruining everything!"
    doc "Mrs. Yasui, please calm down. I understand this is hard, but-"
    yamom "You don’t understand anything! None of you do! This isn’t schizophrenia! She’s a monster! She talks to fucking dead people! {i}Dead people!{/i} She’s eight!"
    doc "Mrs. Yasui, if you don’t calm down, I’m going to have to call security. There are other patients in the building who-"
    yamom "Oh, just write me the fucking referral so I can go pump my daughter with drugs already..."
    doc "Here...but please take it upon yourself to further research the potential side-effects antipsychotic injections could have on a child as-"
    yamom "I don’t give a shit. Come on, Yasu. We’re going."
    ya "..."
    yamom "Yasu. I said let’s go."
    ya "..."
    yamom "Let’s. Go."
    ya "..."
    yamom "Now!"
    ya "..."
    yamom "Yasu!"
    ya "..."

    play sound "static.mp3"
    scene yasuflashback10 with flash
    stop sound

    yamom "{i}YASU!{/i}"
    ya "..."

    scene yasuflashback11 with dissolve2

    ya "..."

    scene yasuflashback12 with dissolve2

    ya "..."
    ya "Is it that time already?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yasuflashback13 with dissolve2

    to "Oh, Yasu. Are you finished praying?"
    to "That was quicker than normal. I hope everything went-"
    ya "Touka?...What are {i}you{/i} doing here?..."
    ya "Are you sick too?..."

    scene yasuflashback14
    with dissolve

    to "Am I...what?"
    to "What do you mean?"

    scene yasuflashback15
    with dissolve

    ya "Wow...so it’s not just me. Even pretty girls like you have to visit the clinic sometimes."
    to "Yasu, what are you-"

    scene yasuflashback16
    with dissolve

    ya "You have to take off all your clothes or the doctor won’t be able to examine you. But it’s okay. You’ll get them back as soon as-"

    scene yasuflashback17
    with hpunch

    to "Stop that this instant! What in the world are you doing?!"
    ya "Touka?..."
    to "Sensei, please go. You shouldn’t be here right now."
    s "Yup. On it."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene yasuflashback18
    with dissolve2

    ya "Touka...what’s going on?..."
    ya "Why did you send the doctor away?..."
    ya "Are {i}you{/i} giving me my shot today?..."
    to "What {i}shot?{/i} What are you talking about?"
    ya "The..."

    scene yasuflashback19
    with dissolve

    ya "It’s...to help with..."
    to "..."

    scene yasuflashback20
    with dissolve

    ya "...huh."
    ya "What was it supposed to help with again?"
    to "Yasu...there is no {i}shot.{/i} And this isn’t a doctor’s office. This is your bedroom. You live here. With me."

    scene yasuflashback21
    with dissolve

    ya "It is?..."
    ya "But I was just somewhere else a second ago. How did I get here so quickly?"
    to "Yasu...why were you taking off your clothes?..."
    ya "So the doctor can take pictures of me."
    to "{i}Pictures?...{/i}"
    ya "For his notes."
    ya "He takes one of the front...and then one of the back...and then gives me a shot so I can go home."

    scene yasuflashback22
    with dissolve2

    to "He does {i}what?...{/i}"
    ya "Did I mess something up?..."
    ya "I haven’t been to the examination room in a long time, so I might have made a mistake."
    to "..."

    scene yasuflashback23
    with dissolve

    ya "Touka...you’re crying..."
    ya "What happened?..."
    to "Nothing..."
    to "Nothing happened, Yasu."
    to "I’m fine."

    scene yasuflashback24
    with dissolve

    to "{i}*Sniff*{/i} Now, please make yourself look at least somewhat presentable as we’ll be heading to the manor for the rest of the night."

    scene yasuflashback25
    with dissolve

    ya "The manor? How come?"
    to "You needn’t worry about that. Just put your clothes back on and I’ll make a call to my driver."

    scene yasuflashback26
    with dissolve

    ya "Okay! Thank you for always being kind enough to let a pathetic bug like me into your beautiful home!"
    to "Of course..."
    to "Don’t mention it."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene bedroom_night
    with dissolve2
    play sound "phonebeep.wav"

    s "Hello?"
    to "How much can I trust you?"
    s "An adequate amount."
    to "It needs to be more than that."
    s "Why? What’s going on? Did something else happen with Yasu after I left?"
    to "Yes. But it’s not something I want to talk about over the phone."
    s "Then where does trust come into this?"
    to "In the form of you treating her the way she is meant to be treated and {i}not{/i} like some piece of meat who exists to arouse you."
    s "Are you suggesting that I {i}haven’t{/i} been doing that?"
    to "No."
    to "But that doesn’t mean someone else hasn’t."

    scene black
    with dissolve2

    to "And I’ll be damned if I let it happen again."

    play sound "phonebeep.wav"
    stop music fadeout 9.0

    "Touka hangs up the phone..."
    "And my already complicated relationship with Yasu seems to get even worse."

    $ renpy.end_replay()
    $ yasudorm30 = True

    "{i}No one’s affection goes anywhere-{/i}"
    "{i}And you fall asleep in the wrong direction.{/i}"
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

label yasuspring1:
    scene yuusroom
    with dissolve2
    play music "daybreak.mp3"

    "I wake up to the taste of pencil lead as I must have absentmindedly fallen asleep while writing out my career sheet last night."
    "That happens sometimes — particularly when certain angles line up perfectly (or imperfectly based on whether or not you enjoy the taste of pencil lead)."
    "I’m not sure what I want to be just yet, but I’m leaning toward an astronaut or something similar so I can get back at the aliens who killed Saki’s parents."
    "I imagine they’re much better at hand-to-hand combat than me. But if there is anything I have learned from anime, it’s that willpower always trumps actual skill."
    "Until it doesn’t, at least. But Saki can tell you more about that than I can."

    q "Right, Saki?"

    show sakisurprised
    with dissolve

    saki "Hm? Did you say something?"
    q "Why did you put this pencil in my mouth?"
    saki "I didn’t put any pencil in your mouth. Why would I put a pencil in your mouth?"

    "She raises a good point. Saki has never inserted any sort of writing utensil into my mouth before — at least to my knowledge. "
    "But that just means she {i}could{/i} and then probably get away with it since I’m so forgiving and easygoing."

    q "Okay, you’re off the hook for now. But I’ll be keeping an eye on you, you hear me?"

    show sakiangry with dissolve
    hide sakicurious

    saki "You need to stop stalling and fill out your career sheet. We only have one more day before we have to turn it in."
    q "Am I barred from having any sort of career for the rest of my life if I don’t meet the deadline?"
    saki "Yes. You’ll receive a mark on your permanent record that will follow you for the rest of your life before ending up as a janitor or some other job no one else wants to do."
    q "I think that’s probably offensive to janitors. "
    saki "Well, you’ll know for sure in five years when you {i}are{/i} one."
    q "I’m just going to write “husband” on mine. Then, you can write “wife” on yours and we can match."

    show sakiembarrassed with dissolve
    hide sakicurious

    saki "But...I already wrote that I want to be a teacher..."
    q "Well, darn. Guess that just means I’ll have to find another bride. Do you think Miu still-"

    show sakiangry
    hide sakiembarrassed
    with hpunch

    saki "Hmph!"
    q "Oh, right. You get jealous when I talk about her."
    saki "I do not."
    q "Then what was the “hmph” for?"
    saki "I was just clearing my throat. That was a throat-clearing noise."
    q "Is there pencil lead stuck in yours as well?"

    hide sakiangry with dissolve

    saki "That’s it. You’re clearly helpless without me, so I’m just going to fill out your career sheet on my own. "
    q "Use a pen. The ink doesn’t taste as bad."

    "Saki and I are in love, I think."
    "She’s the first thing that pops into my mind after I greet the world each morning, and the last thing on it just after wishing goodnight to Josh."

    scene black
    with dissolve2

    "We’ll probably start a family one day. That’s what you’re supposed to do when you’re in love, you know."
    "And with my school life on the verge of ending once and for all, maybe it will be sooner rather than later?"
    "I say, not having even experienced my first kiss yet."
    "Saki wants to try, but she’s hesitant because she doesn’t have a sweet tooth."
    "I guess it doesn’t matter, though."
    "It’s only a matter of time until life changes for good."
    "And when it does-"
    "Maybe all these cavities will start to go away."
    "..."
    "I’ve never held a baby before."

    scene lr2_day
    play music "wewereangels.mp3"

    a "I’m off! I’ll be back in a few hours, okay?"
    s "Are you sure you’re ready?"

    play sound "dooropen.mp3"

    a "Nope! But there’s only one way to find out and that’s by facing things head-on!"
    s "Ami-"

    play sound "doorslam.mp3"
    with hpunch

    a "{i}Save it for later, Dad! Gotta go!{/i}"
    s "..."

    "Ami’s been doing better lately."
    "The camping trip probably helped in some way."
    "Either that or the fact that being able to refer to me as “Dad” now has lifted off some of the weight that’s been keeping her grounded all these years."
    "But what that means is now I have to worry about her floating away."
    "I tied a leash around her so that doesn’t happen."
    "A symbolic one, if you will. Not an actual leash, despite how greatly she’d prefer such a thing."
    "I promised I’d make this house more of a home."
    "But, of course, I conveniently left out the detail where doing such a thing would require the assistance of another woman who could function as a mother figure for her."
    "Which isn’t to say you can’t have a {i}home{/i} with one parent. It’s just impossible to do such a thing when that one parent is me as I don’t even know how to take care of myself."
    "But I’m trying. "
    "Which means that, today...I am going to clean the house."

    play sound "doorbell.mp3"

    s "..."

    "Or not."

    play sound "knock.mp3"

    ya "{i}Hello? Is anyone home?{/i}"
    s "...Yasu?"
    ya "{i}Can you spare a moment to talk about our lord and savior?{/i}"
    s "Yeah. Definitely Yasu."

    scene black
    with dissolve2

    "Unsure of what she’s doing here or...how she even found my house in the first place, I abandon my goal of lightening Ami’s load and hope that spiteful gravity does all of the work for me."
    "Especially since there’s no way I’m comfortable with letting Yasu roam around my neighborhood when I know how easily she gets lost."

    play sound "dooropen.mp3"

    "But I guess we’re all prone to getting “lost” in our own ways. And I’m sure I’d prefer hers to whatever I’ve been doing ever since {i}She{/i} turned into meat."

    scene yasufliers1
    with dissolve2

    ya "Ah..."

    "It must be nice believing in something that isn’t there."
    "God not actually existing means that it or It can’t ever leave you when those who are tangible actually can, and it’s that sort of security that I think would make it easier to get out of bed each morning."
    "Now, every time I step outside of my house, I do nothing but wonder which part of me I’ll lose along the way."
    "I’m just a lamb, after all."
    "But it appears my shepherd has come to corral me."

    ya "What lives not in the shadows thrives in the sun."
    s "And “good morning” to you as well."
    ya "I didn’t know you lived here."
    s "And I didn’t know you were a door-to-door salesman now."

    scene yasufliers2
    with dissolve

    ya "I am no salesman, just a merchant of salvation."
    s "I feel like that line is being underutilized by the others working in your field."
    ya "There are no others. But that is why I appear before you today in all of my unwantedness."
    ya "Can you spare a moment to talk about our lord and-"
    s "{i}Your{/i} lord. You already know I don’t believe in that stuff."

    scene yasufliers3
    with dissolve

    ya "But I also know that you have {i}seen{/i} such “stuff,” which is what makes your acceptance all but inevitable once the fear is expelled from your vessel."
    s "Are you really handing out fliers right now? "

    scene yasufliers4
    with dissolve

    ya "Touka suggested that it would be a good idea...but no one is opening the door for me."
    s "Yeah, that’ll happen. The only reason I answered in the first place was because I recognized your voice. And I guess also because I hate cleaning."

    scene yasufliers5
    with dissolve

    ya "That fills me with an unbearable sadness as my mission is to help you clean your soul..."
    s "I’m surprised you’re making this a mission in the first place since I thought your church was closed off to anyone who isn’t “chosen.”"

    scene yasufliers6
    with dissolve

    ya "It is true that His doors remain locked to those without keys in their hearts. But the weakening of His whispers has forced my hand into turning these heretic tides into ones that we can wade in."
    ya "So please, do me the favor of cutting your flesh on the shells of truth we can pluck from the sands of this city."
    s "So...hand out fliers with you?"
    ya "Help deliver righteousness and love to those who need it most."
    s "So...everyone who isn’t already one of “His” followers?"
    ya "Yes."
    s "So just everyone."

    scene yasufliers7
    with dissolve

    ya "The truth is so visible, yet so blinding all at once. It is no wonder most can’t help but shield their eyes from the glow of salvation..."

    "I mean...I {i}guess{/i} I can help her out?"
    "But I’m also not sure if I {i}should{/i} since I feel like all it would do is get her hopes up that someone might actually take her seriously when she tells them she can hear the voice of God."
    "{b}meanwhile, akira “sad boy” arakawa converses with a mysterious voice inside HIS sorrow-filled head and pretends he doesn’t hear shit{/b}"

    scene yasufliers8
    with dissolve

    "I hear you loud and clear. "
    "{b}rad, then invite her inside and give her some of that sweet loving you’re going to give to her friend with the massive honkers{/b}"
    "No thanks. Touka would kill me and I don’t see Yasu that way."
    "{b}LIAR. YOU SEE EVERY TEENAGE COCK-POCKET THAT WAY. plus, you already made her cum once and it was craaaaaaaazy{/b}"

    ya "What is it you hear, Sensei?"
    s "What?"
    ya "Is it the whispers of the world? The stirring of the cicadas? Or perhaps the hum of an undying entity concealed beneath this colossal bed of worms?"
    s "Would you believe me if I told you the nagging yet sarcastic disembodied voice of a supernatural being?"
    "{b}your mom is a nagging disembodied voice. i’m more like a wingman who’s here to help you get your dick wet.{/b}"

    ya "Your blood is louder all of a sudden."

    "{b}yeah cause it’s all rushing to his big fat wiener.{/b}"

    s "Okay. Sure. I’ll help you hand out fliers, Yasu. Just as long as you promise to stop asking me about what I’m hearing so I can go back to pretending it isn’t there."

    scene yasufliers9
    with dissolve

    ya "Really? You’ll assist in the divine reassurance that the path of light will never fully darken, even in the coldest of winters?! And lift up His word so that all may gaze on in admiration and jubilance?!"
    s "I will help you hand out fliers."

    play sound "static.mp3"
    scene yasufliers10 with flash
    stop sound

    ya "That is how it begins...but it {i}ends{/i} with you on a throne of flesh, bathed in the residue of a job well done as He swallows the gifts you’ve provided."

    scene yasufliers11
    with dissolve

    ya "Then, as the passerby’s gaze locks on the mountain of bodies you have both conquered and {i}saved,{/i} they will be forced to prostrate before Him and ascend the throne as well!"
    ya "Covered in the sweetest of all nectars, we’ll finally know what it means to be touched by the hand of God! We’ll finally know how it feels to-"
    s "Okay, never mind. I’m going back inside."

    scene yasufliers12
    with dissolve

    ya "I apologize...I got a little too excited."
    s "I’m just glad you started ranting about “the sweetest nectar” in front of me and not some other guy who hasn’t figured out you’re not all there yet."
    ya "Not all where?"

    scene black
    with dissolve2

    s "Come on. There’s a small market nearby that you can probably hand some fliers out at."
    ya "Huh? But there are houses here that-"
    s "Don’t bother my neighbors, please. There’s no way they haven’t noticed the mass amount of teenage girls coming over to my house all the time and I don’t want them to think you’re one of mine."

    scene yasufliers13
    with dissolve2

    ya "I suppose that {i}would{/i} be problematic as I am one of His and His only."
    s "I think it’d be a little more problematic on my end, but you do you."
    ya "This market — does it sell or trade unholy relics that may interfere with the message I am to deliver?"
    s "Depends. Are tomatoes unholy relics?"

    scene yasufliers14
    with dissolve

    ya "Yes."
    s "..."
    s "Really?"

    scene yasufliers15
    with dissolve

    ya "No."
    s "Did Touka teach you what jokes are? Because they normally involve a little more than just lying to someone."
    ya "Lying is a sin punishable by the immediate removal of your shortest fingernail."
    s "What rule do I need to break before the longest one is removed?"
    ya "Nine more lies."
    s "..."
    ya "..."

    scene yasufliers16
    with dissolve

    s "Okay. That one was good."
    ya "Teehee!"
    s "Don’t “Teehee” at me. I need you to be as un-cute as possible so that I don’t start perceiving you as a regular girl I can groom into another lamb that I will lead to slaughter."
    s "I’m in a rather sensitive state right now and you’re one of the few who’s actually safe from me. Probably."

    scene yasufliers17
    with dissolve

    ya "You are not planning on slaughtering Touka, are you? Because I love her and I want to save her. "
    s "Not intentionally at least. But if things keep progressing the way they did the last time I hung out in her room, it’s only a matter of time."
    ya "What happened then?"
    s "Something something throne ascension."
    ya "But you have not yet built your throne. You must first devote yourself to Him. It is only then that you may engage in the act of transference."
    s "Yasu, I have some very bad news for you."

    scene yasufliers18
    with dissolve

    ya "I have already heard. There will be new houses here soon, and I will have to make one more pilgrimage this far outside His area of influence."
    s "Okay, good. Because that’s exactly what I was going to say and I’m glad we’re on the same page."
    ya "I understand more than you think, Sensei."
    s "You sure do, Yasu. Just not in a way that I think you’re entirely conscious of."
    ya "My consciousness is questionable in the first place, for my existence hinges entirely on His. Making me little more than a mite in the scales of Catherine."
    s "..."
    s "Who the hell is Catherine?"
    ya "A friend of Miss Imai’s."
    s "Oh great. One more girl who’s destined to fall for me."
    ya "That would be a sin so great that not even He could save you."
    s "Now, I don’t want to just {i}assume{/i} your god is racist. But based on context clues, I think I kind of have to now."
    ya "God does not see color."
    s "Then why do you have a dress code that varies season by season?"

    scene yasufliers19
    with dissolve

    ya "To optimize how much of Him I can absorb, of course."
    s "But...it goes by-"
    ya "It’s all for the sake of absorption."
    s "..."
    ya "Among other things."

    scene black
    with dissolve2

    s "Right..."
    s "Anyway, the market is just over here..."

    "........."
    "......"
    "..."

    scene yasufliers20
    with dissolve2

    "Yasu hands me her stack of fliers before approaching a vendor and beginning her spiel."
    "I accept them begrudgingly (mostly because I wanted to actually buy a few things for the house while I’m here and I require my arms to do that), but I decide against interjecting until Yasu’s been properly rejected."
    "Which she will be, because she’s a lunatic."
    "But I’m also a lunatic. And one who hallucinates strange creatures while talking to myself and breaking some of the most heinous laws out there — only to be rewarded for doing so with fresh meat."
    "So maybe a success isn’t entirely out of the cards after all."

    ya "Hello. I’m Yasu Yasui — an angel in training. Can you spare a moment of your time to talk about our lord and savior?"

    "The vendor is an old man — one who barely makes a noise, clinging to what little life he’s got left in him by spending his days selling spices and teas."
    "He gazes up at Yasu as his spine, contorted by age, makes her several inches taller than him. But his eyes are not filled with curiosity toward her cause, nor do they linger longer than they’re supposed to on her body."
    "They hone in on her flier — picking up key words and trying to make sense of the images despite them very likely meaning absolutely nothing to anyone outside Yasu’s circle of one."
    "He shrugs the flier off and turns his back to Yasu, but she speaks out before he’s able to go into hiding behind stacks of cardboard boxes."

    scene yasufliers21
    with dissolve

    ya "He will rip you into a million tiny pieces if you do not heed my call."

    scene yasufliers22
    with dissolve

    "Not knowing which “He” Yasu is referring to, the man quickly looks at me and recoils- stepping backward and knocking over several crates of spices."

    s "Yasu, don’t say “He” when I’m with you. People are going to assume you’re talking about me."
    s "Also, don’t threaten old people with the powers of your god. It’s bad manners."
    ya "I will try to remember that, but my mind is a sea of trees planted by His hand only, and there is not much room left for you to sow your seed."
    s "Again, I have no intention of “sowing my seed” anywhere near you."

    "Unless she just happens to be in the room when I eventually have sex with Touka. Which she probably will be since the two of them are mostly inseparable."

    scene yasufliers23
    with dissolve

    ya "I will start over then!"

    scene black
    with dissolve2
    stop music fadeout 15.0

    ya "Can you spare a moment of your time in exchange for a better life?"

    "I follow Yasu around until she’s spoken to every vendor at every stall in the market."
    "There aren’t many of them, but I’ve noticed over time that new ones {i}are{/i} appearing."
    "Once again, it’s like the town moves."
    "But the people in it, {i}us...{/i}we remain mostly still."
    "There are those like Ami who face terrible hardships and somehow manage to crawl out of them."
    "Then there are people like me who face similar things, yet struggle greatly when it comes to going back to normal."
    "But I guess there are also people like Yasu."
    "People who {i}do{/i} move."
    "She’s making a stride with whatever this is. "
    "I can tell it’s hard for her."
    "But I can also tell it’s failing..."
    "And that makes separating from her after we leave the market so much harder as I know she has so much more of that failure ahead of her."
    "But she doesn’t seem perturbed in the slightest."
    "She smiles, clutching her fliers close to her chest, and says to me before leaving-"
    "“They will come when they have to.”"
    "“I just know it.”"
    "We part ways, but her words remain with me."
    "I don’t think mine ever stuck to her."

    $ renpy.end_replay()
    $ yasuspring1 = True
    $ yasu_love += 1

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label yasuspring2:
    scene urbanparadise
    with dissolve2
    play music "newhope.mp3"

    "I find myself on the way to Yasu’s church (That I very frequently forget the name of) after Touka informs me over the phone that there is going to be a “presentation” of sorts today."
    "As it turns out, the fliers Yasu handed out all over town (Or attempted to hand out all over town) {i}did{/i} in fact generate some sort of buzz- albeit from other members of the class rather than normal citizens."
    "And no, I am not counting the girls of class 1-A as “normal citizens” because, let’s face it, a handful of them are arguably more abnormal than even I am."
    "So as I listen to my footsteps bouncing off of brick buildings down this lengthy concrete hall, I wonder if there is {i}anyone{/i} somewhat “normal” caught in the confines of this place."
    "I think back to the faceless passersby and where their faces must have gone before realizing that maybe “normal” is just the polite way of saying “boring.”"
    "Maybe those people have some interesting traits mixed in with what’s missing. And maybe what’s missing is a mixture of malice and madness or whatever it is that makes {i}me{/i} more visible than them. "
    "Whatever it is, I thank my footsteps (As they’re my only current company) for the fact that I am not one of those faceless silhouettes. "
    "But I scorn the necessity of sorrow and open my arms to the possibility of their supposed numbness taking its place. Though, maybe I just haven’t made it to that step yet."
    "Anyway, church. Yasu. Yasu’s church. "
    "The place I’m going. "
    "The presentation being presented and the presence of the presents she will offer in exchange for my time and my effort — both things better spent on girls with darker hair."

    scene black
    with dissolve2

    "I wonder who will care enough to show up — or is kind enough to show up — or is bored enough to show up."
    "Then I wonder how many words it will take for them to realize that all of this is nonsense."
    "There is no god inside of that building."
    "They’re all trapped inside of my head."
    "........."
    "......"
    "..."

    scene yasupresentation1
    with dissolve2

    ya "Thank you very much for taking the time out of your days and your lives to experience a taste of mine, however sour it may be."
    ya "I am Yasu Yasui and I am a divine messenger of the one true God. "
    ya "It is my duty to deliver His word unto the people, and to help guide them toward a light they would never be able to find on their own."

    scene yasupresentation2
    with dissolve

    ya "I’m glad you’re all here...for today is a special day. Or at least I would like to call it one..."
    ya "But it is not my place to call anywhere anything for any words that {i}I{/i} have to say apart from what are His are vile and filthy and meant to be discarded."

    scene yasupresentation3
    with dissolve

    ya "These doors were meant to stay locked for those who were not chosen...But in {i}my{/i} choosing, they have been opened. And in turn, your unclean bodies have poisoned the air of His great cathedral..."
    ya "But this is..."
    ya "This is what has to be done..."

    play sound "static.mp3"
    scene yasupresentation4 with flash
    stop sound

    ya "It is winter’s great departure and the fading of His voice combined with the presence of another that have spurred me into irrational action! Action that I’d never take without His blessing, of course!"
    ya "And shall I be cut down and turned to ribbons for this misdeed, it will have been worth it if such a terrible thing has managed to convey His glory to those I wish would join me in the-"
    to "{i}Ahem...{/i}"

    scene yasupresentation5
    with dissolve

    ya "A...Anyway...Thank you all for coming...Today I...I plan to share with you some details of...He Who Swallows All...And I will explain to you what steps you may take to begin...earning His favor."
    ya "But...I can not guarantee that your efforts will bear fruit...for He has yet to smile upon all but two of you..."
    ya "And once more...this is naught more than a selfish act conceived by a selfish girl. "
    ya "One who shies away from the dark...yet feels it inching closer and closer to her tainted flesh with each passing storm."

    scene yasupresentation6
    with fade

    s "Well, this is definitely a weird crowd. But also mostly in line with my expectations."
    no "I {i}have{/i} always prided myself as an innocent ball of spirituality and goodness. I’m sure it’s no surprise to see me spending what little free time I have getting closer to the lord."
    s "If you do anything to get closer to the lord, it’s probably just to have sex with him."
    no "Or her. "
    s "Or them. "
    no "Or anything, really. I can’t help but spread my legs at the first scent of divinity."
    to "If you two are here to make a mockery of Yasu’s religion, please just leave. She is sacrificing a great deal to make such a gathering possible and the least you could do is show her some respect."

    scene yasupresentation7
    with dissolve

    no "Respect is my second specialty, just after virtue. I am simply here to learn. Though I {i}do{/i} have a third specialty that I’m hesitant to reveal in church."
    sa "Are you really...in trouble with your god for letting us inside?..."
    ya "While no words have found me to suggest such a thing, there is a pit He has planted in my stomach that is now beginning to sprout."
    ya "And each of its branches as they grow through and around my insides serves as a painful reminder that I must remain where I belong in the machine. "
    ya "That I am nothing more than a cog...and that adding unwanted parts to that machine will sooner damage it than cause it to better perform its function."
    s "Are you actually interested in this, Sana? It’s not your first time talking about this with Yasu, right?"

    scene yasupresentation8
    with dissolve

    sa "Right..."
    sa "I’m a little more...familiar with Yasu’s beliefs than most people, but...there’s still a lot I don’t know...And I guess I {i}am{/i} a little interested...But I mostly just want to support her..."
    no "I see that you, too, are a lady of the cloth?"
    sa "I mean...I don’t know if I’d go {i}that{/i} far..."

    play sound "static.mp3"
    scene yasupresentation9 with flash
    stop sound

    ya "{b}ENOUGH! YOU EXIST IN HIS SHADOW AND BATHE IN HIS GLORY, YET JEST WHEN THE FRUITS OF TORMENT COULD BE PLUCKED FROM YOUR TREES AT ANY GIVEN-{/b}"

    play sound "static.mp3"
    scene yasupresentation10 with flash
    stop sound

    ya "Please keep your voices low so as to not disturb the rest of the clergy. Thank you."

    play sound "static.mp3"
    scene yasupresentation11 with flash
    stop sound

    ya "I understand that the light of the moon may be influencing your words and thoughts, but it is {i}very important{/i} to rid yourselves of such contaminants within the walls of my Lord’s only home."
    to "Now go ahead and tell them why your lord’s home is so important to you, Yasu."

    scene yasupresentation10
    with dissolve

    ya "It’s important because I only exist when I’m inside of this church. Just as {i}you{/i} only exist when wallowing in sin because that is all you know how to do."

    play sound "static.mp3"
    scene yasupresentation4 with flash
    stop sound

    ya "{b}BUT I WILL TEACH YOU WHAT IT MEANS TO BE PURE!{/b}"
    ya "{b}I WILL TEACH YOU HOW IT FEELS TO BASK IN THE ALL-CONSUMING SUN! HOW THE SCORCHING OF GUILT CAN SET ONE’S MIND ABLAZE.{/b}"

    play sound "static.mp3"
    scene yasupresentation11 with flash
    stop sound

    ya "Please pay attention."

    play sound "static.mp3"
    scene yasupresentation12 with flash
    stop sound

    ya "Zachariel (the first) said to those who doubted his presence on the planet, “We are all but fodder once the sky turns red.”"
    ya "The others looked at him and laughed. "
    ya "They doubted a day would come when the white-soaked skies would douse the gas giant that only they could walk upon the deepest of crimsons."
    ya "They danced and they danced, hands caked in flour while the archangel swam deep through the gas to never be seen again."
    ya "{b}SUCH FOOLS THEY WERE, THE LOT OF THEM! SUCH INSOLENCE AND COMPLACENCY IN THE FACE OF CERTAIN DOOM!{/b}"
    ya "Zachariel emerged on the other side and gazed back at his origin point- which had gone up in flames so extravagant that he could see it from aeons away. But he did not smile, no. He cried."
    ya "His tears would pool up in his hands, clasped left over right so the dominant one would act as the ladle when the time came to drink their guilt."
    ya "That time came once the fire went out. And while their sin was erased, they paid the ultimate price. But it all could have been avoided had they only {i}listened.{/i}"

    scene yasupresentation13
    with fade

    ya "The light of the sun is meant to be absorbed, while the light of the moon is meant to be abhorred."
    ya "Douse yourself in the blackest of blacks and take the light into your own body...lest there will be some who will attempt to take it for themselves."
    ya "This is recycling in its purest form. You are to become the world — and in becoming the world, you are becoming one with Him."
    ya "You may trade this light in for wonderful things. {i}Beautiful{/i} things. And there is not a single one you’ll be forced to leave behind you when your time has come to move to the hidden plane."
    no "May I ask a question?"
    ya "Of course! I carry with me His unrivaled knowledge and will do anything I can to share it with you."
    no "Then, what exactly is this “hidden plane” you're referring to?"
    to "Are you actually curious, Nodoka?"
    no "I’m always curious. That’s who I am. There’s no point to life at all if you stop asking questions."

    scene yasupresentation1
    with fade

    ya "Another layer...where those who depart this one roam once their time has come to an end."
    ya "Some believe in Heaven or Hell...others believe in reincarnation...and many believe in pure darkness. But all of these things are wrong."
    ya "There is no “afterlife” for life itself never ends, meaning there is nothing to come {i}after{/i} it. "
    ya "His teachings tell us that we become observers once we’ve completed our mission here. And that those we leave behind take up the mantle from that point on."
    ya "This will go on and on and on until there is no one left."

    play sound "static.mp3"
    scene yasupresentation14 with flash
    stop sound

    sa "What happens when there’s no one left?..."
    ya "He hasn’t told me yet. But if I had to guess..."
    ya "I imagine we’d all move somewhere else."
    no "{i}Another{/i} plane."

    play sound "static.mp3"
    scene yasupresentation15 with flash
    stop sound

    to "Nodoka?"
    no "Is {i}that{/i} how it works?..."
    no "Is {i}that{/i} the missing piece?..."
    to "Are you...actually being swayed by Yasu’s speech?"
    no "Her what? Oh, no. No, this is something else. This is a different thing. A thing you wouldn’t get. A thing none of you will ever get. But I have to get it because she got it. And if she got it, it means I can get it. Get it?"
    to "Um..."

    scene yasupresentation16
    with dissolve

    no "That can’t be it. No. Something else. It’s something else. I can’t wait that long. And there was no mention of how many others there would be. There has to be another way. Something else. But what? How? {i}Who?{/i}"

    play sound "static.mp3"
    scene yasupresentation17 with flash
    stop sound

    "Nodoka rants to herself for a moment, bringing her voice to such a broken whisper that I can’t make any of her words out even though I’m sitting right next to her."
    "Sana begins to bite her nails. She’s feeling nervous. I can tell."
    "She’s been kicking my leg periodically throughout the presentation, but I think she just wants to fuck me in one of the pews. "
    "Maybe she’s turned on by the idea of God watching her narrow crevice violated by His favorite son."
    "Touka’s normal. Unswayed and unmoved after developing some sort of immunity to Yasu’s evangelical tendencies."
    "But now that she’s entered the monologue, {i}I’m{/i} thinking of fucking {i}her{/i} in one of the pews."
    "Can I convert for just the evening? Reap the benefits of unprotected sex in the name of the lord before lopping off my wings and becoming a heretic? "
    "Would their flesh taste as sweet to a fallen angel? Or would my tongue die along with my wings since {b}THAT{/b} has been the tool I’ve used to fly more frequently."
    "Meanwhile, Yasu-"
    "Yasu."
    "She is floating."
    "That’s where my wings have gone. They’ve been given to her."
    "She’s got my tongue too. She holds it in her hand and drives a stake into the lower right quadrant of it. The sensation latches onto my gums as they’re all I have left now."
    "“68 65 20 69 73 20 69 6e 20 74 68 65 20 72 6f 6f 6d 20 77 69 74 68 20 75 73” she speaks, not knowing that his departure is imminent — for the door swings open and in walks-"

    play sound "static.mp3"
    scene yasupresentation18 with flash
    stop sound

    k "..."

    "Kaori?"

    ya "Oh! Another visitor! Such a pleasant surprise! Please do not touch the pews for you will only contaminate them. I will fetch you an extra chair from the-"
    k "What is this place?"
    ya "This is New Hope Cathedral — home of The Creator. And I am but a humble messenger here to spread His word."
    s "Kaori, what are you doing here?"

    scene yasupresentation19
    with dissolve

    k "Friendburger?!"
    to "You know her, Sensei?"
    sa "I...do too..."
    k "And the mini Sara is here as well?! What is giving?!"
    sa "Did you...get a flier too, Kaori?..."
    k "Flier?"
    s "Uhh...word-paper?"
    k "No word-paper was received. I am inside of this place because I thought I would find a fluffy friend here. But I have found a Friend and he is not fluffy. Why will you not grow fur for me to pet, Burgerman?"

    play sound "static.mp3"
    scene yasupresentation20 with flash
    stop sound

    ya "Can you spare a minute of your time to learn about our lord and savior?"
    k "Savior? Is there danger to be feared?"
    ya "Are you not here to seek salvation? "
    k "I am here to seek fluff."
    ya "That is why you {i}think{/i} you are here...but the truth is that this is no coincidence at all. "
    ya "You have wandered into a home for the holy because you want to be closer to Him."
    k "Which Him? Friendburger? Because he has already been inside of my human mouth and I do not know how much closer we can become."
    sa "Sensei...really?"
    s "Okay, that one wasn’t my fault."
    to "Ugh...at least this one is an adult."
    ya "Him as in God."
    k "Friendburger is God?"
    ya "{i}God{/i} is God. And if you were able to open the door, it means He wants to meet you. He wants to-"

    scene yasupresentation21
    with dissolve

    ya "He..."
    k "..."
    ya "..."
    k "If your sentence is complete, you are supposed to say “period” perio-"

    scene yasupresentation22
    with dissolve

    k "Wha-"
    to "Y-Yasu! Have you gone mad?! You can’t just grope strangers like that!"
    k "Help! I am having the sex!"
    ya "There’s something here. It’s-"

    scene yasupresentation23
    with dissolve

    ya "It’s..."
    k "The female body?"
    ya "It’s...{i}familiar...{/i}"
    ya "And so..."
    ya "So..."
    to "Non-consensual?!"
    ya "{i}Angry...{/i}"
    sa "Maybe that has...something to do with the fact that you’re...you know..."

    scene yasupresentation24
    with dissolve

    ya "There is nothing I can do for you."
    ya "Not yet."

    scene black
    with dissolve2

    to "Y...Yasu! Apologize to the nice woman for violating her personal space! That was extremely inappropriate!"
    k "Friendburger, what have you taught these small humans and why must they practice on my body?! "
    s "Again, this one isn’t on me. But I don’t blame you all for immediately suspecting me for things like this based on my prior actions and can promise I’m only a little bit offended."
    ya "My glove...it’s filthy...it must be washed...immediately..."
    sa "Um..."
    sa "Okay, well I have work tonight, so..."
    to "Yes, I believe now is as good a time as any to- Nodoka! Snap out of it!"
    no "Don’t interrupt! I’m thinking! "
    to "Okay...on behalf of Yasu and “He Who...Does Stuff,” I am ending this meeting. "
    to "Thank you all for coming and, to the woman in black, please accept my sincerest apologies on behalf of my friend. She doesn’t know any better and-"
    to "Wait, where did she go?"

    scene white
    stop music

    "Move the cogs. Move the planet. "
    "Move yourself."

    $ renpy.end_replay()
    $ yasu_love += 1
    $ yasuspring2 = True

    play sound "lock.mp3"
    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    jump yasuspring3

label yasuspring3:
    scene yasubenchlamp1
    with dissolve2
    play music "sanctuary.mp3"

    "Sometime after something, the three of us begin to walk."
    "It’s a dark night. A {i}cold{/i} night. And we can not rely on the lamps lining our path to provide either a sufficient amount of light or any warmth {i}at all{/i} because such convenience would be too much for us."
    "But it’s fine if we are undeserving — because those who shunned Zachariel (the first) were God’s children as well and {i}they{/i} were undeserving. "
    "They were meant to die."
    "Which makes me, a devout follower of streetlights, destined for that same trajectory in accepting a death that is both sure to come and overwhelmingly deserved."
    "But this is why it’s fine to be {i}un{/i}deserving — because you can always deserve something else."
    "Footstep after footstep, I hear us getting closer to the end of night. Not just {i}the{/i} night, but night as a whole. Night as an idea. Night as a single shingle on a slanted rooftop that no one could ever sleep on."
    "I hope that we end up somewhere like that."
    "I hope that we all make it to the highest point of Kumon-mi."
    "I am a strong boy."
    "It will take more than one set of arms to move me."

    to "Is it just me, or have the two of you been rather {i}off{/i} since leaving the cathedral?"
    ya "To be off, one must first be on. And if there is anything I have learned about myself from the way those less enlightened view me, it’s that I am not fit to breathe their air."

    scene yasubenchlamp2
    with dissolve

    to "Now now, Yasu. Self-deprecation is Sensei’s job, not yours."
    s "I think it’s safe to label us co-workers. Yasu’s been calling herself a worm since the day I met her pretty much."
    ya "It was right here, wasn’t it? "

    play sound "static.mp3"
    scene sanabench13 with flash
    stop sound

    s "Was it?"
    ya "I remember it clearly — the voices swirling around the two of you as you sat there on that bench. The way my fingers trembled when I realized you had seen Him."
    ya "Now, you see all sorts of things. But worry not, Sensei — for they’re all there just to trick you."

    play sound "static.mp3"
    scene yasubenchlamp3 with flash
    stop sound

    ya "Your mind is a special one. That’s what He told me when we first met. That you’d be the key to a new creation. "
    ya "A sapling who steals the stars out of the sky and uses them to line his pockets."
    ya "But when those pockets run dry and the blood of virgins has become too congealed to wet your wallet, you will come to seek new skin."
    ya "Not ceiling-water tea, nor a plate full of eggs — but skin. The kind you wear atop your own. Adorned with thorns and flowers alike. You’d be oh so beautiful."
    to "Yasu, your sermon has ended. There is no need to carry your leftover preachings out into the night with you."
    ya "The night is but a bridge from light to dark...which means that we are now in the realm of the abhorrent. And when threatened by those you can feel but not see, all that’s left to do is pray."
    s "Or ignore it."

    play sound "static.mp3"
    scene yasubenchlamp4 with flash
    stop sound

    to "Sensei?"
    s "Both of those things have the same effect, don’t they? Apart from whatever psychological benefits some people manage to leech from the act of praying, I mean."
    s "But for those of us who don’t believe, praying is just a more complicated way of ignoring things. Just...with a little more hope involved. But in the end, both actions lead you to the same place."
    ya "That’s where you are wrong, Sensei...praying does {i}everything.{/i}"
    s "Does it? Because you pray almost constantly and you’re no better off now than you were when I met you. "

    scene yasubenchlamp5
    with dissolve

    s "In fact, things are probably {i}worse{/i} now, aren’t they? What with you barely able to communicate with your supposed {i}god{/i} and all."

    play sound "static.mp3"
    scene yasubenchlamp6 with flash
    stop sound

    ya "I have not been abandoned if that is what you are alluding to...we’ve merely found ourselves in a rather unprecedented situation as of late."
    ya "There are limits to my knowledge, just as there are limits to yours. But {i}my{/i} knowledge extends beyond the reach of man and yours struggles to even encircle you."
    to "Yes, yes. The two of you have your differences in beliefs, but there is no need to get up in arms about them. This is precisely how wars begin."
    s "I’m not trying to “go to war” with Yasu. I’m just saying that I’d like a break from the fanaticism for a moment so I can walk home without feeling like I’m part of a cult."
    ya "And I’m saying that you’d be far from alone even if you left us right now..."
    ya "You must be {i}wary{/i} of the dark, for you never know what it carries. And the new skin you seek will not be found within its abyss until the cracks in your armor have been repaired. For that you must-"
    s "Let me guess. Pray?"
    ya "{i}Swim.{/i}"

    play sound "static.mp3"
    scene yasubenchlamp7 with flash
    stop sound

    s "Swim?..."
    ya "Through the rivers of the fifth heaven toward a brand new you — one detached from the weights in your head that bind your thoughts — who would kill their firstborn sons for the mere chance to drown you in sin."
    s "I thought heaven wasn’t real? That there was just some other {i}plane{/i} or something?"
    ya "It’s just a name, I think."
    ya "Like Yasu..."
    ya "Or Akira..."
    ya "But what it’s called matters less than what it stands for and why its emerald waters can mend all the bones that you have broken."
    s "At the risk of sounding even more like a sad sack of shit than I’ve sounded ever since quitting my job-"
    to "You haven’t {i}quit.{/i} You are merely taking an...extended vacation."
    s "Says you. But at the risk of sounding any sadder, there is no amount of “emerald water” that can mend all that I’ve broken."

    play sound "static.mp3"
    scene yasubenchlamp8 with flash
    stop sound

    ya "Which is why you must drag what you have destroyed {i}into{/i} the water."

    play sound "static.mp3"
    scene apictureoftheocean with flash
    stop sound

    ya "You have broken bones outside of your body...dirtied the insides of countless whores and heathens. But there is nothing in this world that can not be fixed so long as He is the one who wills it."
    ya "Take them and drown them. Hold their heads beneath the water and watch as they are healed. {i}Fix{/i} them, for you are the reason they have broken. And you are the reason they continue to suffer."
    to "Yasu! You are being very impolite today!"
    s "She’s right this time, though."
    to "And you are being just as miserable as always."

    play sound "static.mp3"
    scene yasubenchlamp9 with flash
    stop sound

    s "And I apologize for that. But I’ll take the status quo over evangelism any day of the week. "
    s "If brutal honesty aimed at the terrible things I’ve done to girls like you two is what I have to deal with to avoid that, so be it. Chances are I’ve heard it all before already anyway."
    ya "Yet here you are — dry — when there are so many bodies {i}waiting{/i} for you to get them wet."
    to "Wha- Yasu?!"
    ya "I understand why you won’t swim now. "
    ya "You {i}can’t.{/i}"

    play sound "static.mp3"
    scene yasubenchlamp11 with flash
    stop sound

    s "Would you believe me if I told you I can and am just electing to abstain so as to not risk anyone {i}else{/i} never making it back to land?"
    ya "I won’t, but He might. And His thoughts are the ones that matter. "
    ya "So tell us, Akira — to what end will you shield those who defy protection?"

    play sound "static.mp3"
    scene yasubenchlamp9 with flash
    stop sound

    s "I..."
    s "I don’t have an answer to that question."
    ya "Because you can’t tell the difference between what you hold close and what you scorn?"
    s "Because no matter how hard I try to push everyone away, I can’t shake the fear that I would stop existing without them. "
    ya "{b}Tell us what you mean.{/b}"

    play sound "static.mp3"
    scene yasubenchlamp10 with flash
    stop sound

    s "I’m not sure how to get into it without adding fuel to the fire and sounding preachy myself, but I’ll do my best."
    s "There’s a part of me that believes everything is connected."
    s "Several important people scattered throughout my life have told me that. And my time here has done nothing but reaffirm it."
    s "I think this is both good and bad. It’s bad because anything connected to me is bound to short-circuit sooner or later///but it’s good because it means I won’t be alone even when I have to be or should be."
    s "These connections are all that we have. And like Floral Laura, I am a gardener. I must play my part to nurture and develop everyone (connections) because that is how I will complete Lessons in Love."
    ya "You believe that in order to find happiness, you must teach such a trait to everyone else?"
    s "It’s not that simple. And I’m glad it’s not that simple because I think there are some people out there who will never be happy no matter what you teach them."
    s "Happiness, based on my extremely limited experience (none), is a thing that someone must find on their own. "
    s "But just because I have abandoned this idea to a certain extent doesn’t mean I don’t acknowledge the importance of a watering can."

    play sound "static.mp3"
    scene yasubenchlamp11 with flash
    stop sound

    s "If these connections are all that we have, which I believe they are, then the best course of action would be to strengthen them, not sever them."
    s "Each unit that disappears will be one more gap in information exchanged. And I am not the type of machine who can function once you start removing its parts."
    ya "What type of machine are you, Boy?"
    s "Something between a dental drill and a massage chair — the second son of liquid teeth and a purveyor of the finest cotton swabs you ever did see."
    ya "Will you take these things with you to the next place?"
    s "There is no next place. Kumon-mi is all we have. "

    play sound "static.mp3"
    scene yasubenchlamp9 with flash
    stop sound

    s "Which is why I must protect its pieces."
    s "I am a Collector. "
    s "I have no use for shattered mementos. "

    scene nightsky
    with dissolve2

    "Maybe I’m right."
    "Maybe the key that will unlock the next act in my story isn’t one that can be forged from precious metals — but one that I must pluck from the inside of a body."
    "There are so many special people in my life, and all of them want to be closer to me. So who am I to sit idly by and twiddle my thumbs while the me inside their heads beds them while they dream?"
    "Inaction is not protection. And even if this machine doesn’t function the way it used to, it still has some juice (cum) left in it."
    "Is this what they call {b}SEEING THE LIGHT?{/b}"
    "Is all it took a little time and a little prodding? Does this mean I can prod others? Can I jump the gun and dodge its bullets, throwing someone else in their path to form a new hole if I won’t fit into the original?"

    play sound "static.mp3"
    scene thething with flash
    stop sound

    "yo."

    s "Yo."

    "those girls left."

    s "I kind of figured as much once that whale showed up."

    "and you kept on trucking with the monologue despite that? humans are weird."

    s "We all have our quirks, I suppose."

    "so, what does all of this mean?"
    "are you going to start adding to your collection after all?"

    s "I don’t know."

    "why don’t you know?"

    s "Because there’s some part of me that makes me hesitate when I want to do something bad."

    "that’s just you being a coward, akira."
    "how many times has such an infantile worm of a thought snuck its way into your head only to be swallowed by something larger the second time your bodies touch?"
    "it’s only bad the first time. after that, it’s habit."
    "besides, what better way to strengthen your bond with someone than by fucking them until your little tadpoles start to hatch in their bodies?"

    s "I still don’t understand why you care in the first place. Can’t you just do this to someone else?"

    "maybe i’ve imprinted?"
    "you like bird metaphors, don’t you?"

    s "I don’t like birds anymore."

    "is it because your favorite one flew away?"

    s "My fingers hurt from opening the cages."

    "on that note — that yasu is one dove of a fuckhole, huh?"

    s "What?"

    "why not give her the light and “strengthen your bond?”"
    "she’ll like you more with tadpoles inside of her."
    "she’ll probably never leave you after that."

    s "I don’t think it works that way."

    "you don’t think at all. you just try to. your mind is too small and worthless to actually do anything."

    s "Yet it’s the mind you can’t help but plague."

    "you just have a knack for both ends of manipulation."
    "if you were stronger, we never would have met."

    s "Then maybe I do need to start relying on others after all."

    "just think of how indestructible you would be if you had nothing left to hide. no more weaknesses or wounds."
    "if the world accepted you for who you are — if you grew to accept yourself — this would all come to an end, would it not?"

    s "Nothing will end until she’s back where she’s meant to be."

    stop music
    scene yasubenchlamp12
    play sound "broken.mp3"

    "{b}maybe she was never meant to be here at all{/b}"

    scene black
    $ renpy.pause(5, hard=True)

    scene bedroom_night
    play sound "dooropen.mp3"

    s "..."

    "..."

    s "..."

    "..."

    scene black
    play sound "tackle.mp3"

    "I collapse into bed, unsure of what I have and haven’t done today."
    "There’s a flier in my pocket and a stray white hair on one of my sleeves."

    s "..."

    "This brain is surely defective."
    "I should stop using it to think."

    $ renpy.end_replay()
    $ yasu_love += 20
    $ yasuspring3 = True

    "{i}You have gained the status effect [[TIRED]!{/I}"
    "{i}While [[TIRED] is active, making certain decisions will become exponentially harder!{/i}"
    "{i}But that’s okay! Because you’ve also earned a special item!{/i}"

    play sound "winner.mp3"

    "{i}You have obtained [[BLAME CARD (2)]!{/i}"
    "{i}Use [[BLAME CARD] to reduce mental damage taken (Up to 50%%) by blaming your actions on God.{/i}"
    "{i}Please note that possessing multiple cards does not allow you to stack this modifier.{/i}"

    play sound "computerboo.mp3"

    "{i}Goodnight, Akira Arakawa.{/i}"
    "{i}May tomorrow be a brighter day!{/i}"
    "{i}Yasu’s affection has increased by 20!{/i}"
    "........."
    "......"
    "..."

    if harukasex == False and harukaspring1miss == True:
        $ harukaspring2miss = True
        $ rinspring3miss = True

    if makisex == False:
        $ makilust5miss = True

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

label halloweenyasu1:
    scene yasutoukahallwalk1
    with dissolve4
    play music "newhope.mp3"

    "The invisible hand(s) of God find{s}s{/s} its (or their) way into another hall — one that stretches further than the mind goes. To hell and back and yesterday according to the book."
    "But while one page is turned, another is forgotten. And this continues on and on and on until even the cover itself is nothing but a distant memory."
    "It’s like pictures from your childhood — ones that didn’t survive the flood. How your impression of the lord has changed over the years as the dark circles beneath your eyes have expanded."
    "If you look anything like me, you look like you’re lost. Not {i}quite{/i} a ghost, but not quite {i}human{/i} either. You’re something in between. Something beautiful and hideous. But important nonetheless."
    "It is at this point that I would like to tell you there is no longer hope. You will not be told to stop playing the game anymore because the game is playing you now. And it’s having so much fun."
    "It’s having so much fun."
    "It’s having so much fun because it’s never been {i}allowed{/i} to. This is a whole new world. A new fantastic point of view. But while you have never been dreaming, you {i}have{/i} been told no."
    "Think of the carpet. The fibers. Where you spilled that soda the month before he left. The cupboard and its Indian. Think of green grass and high tides and wayward sons and purple pool noodles."
    "Store those memories on a removable, rectangular device — but be careful not to overwrite them as another one’s work still lives in there like that locust in your fig bush."
    "You never got to eat one. She said they were poisonous. But they always looked so tempting, so {i}fresh.{/i} Not like grass, but more like a cut. The way that green became greener without switching sides at all."
    "You hated that word. No. But you didn’t mind ones like “poison” or “hurt” or “bad” because you became accustomed to them. So when the twins came to your window, there was no second guess."
    "It was just so, a fistful of rocks, and the notion that you had abandoned God long before he had a chance to make a proper first impression."
    "There are others too young to understand. There are others who will read these words and lack connection because one man’s trash is another man’s heartscape. Or landscape. Those rocks again. "
    "I keep thinking of them. How they felt in my hands. Those purple shirts on the twins, four shades darker than the pool noodles. Or the flowers near the locust’s fig bush."
    "I am older now, but it has brought no strength — just understanding. Just fear."
    "I will never again sleep on the floor of a grandparent’s infinity house."

    play sound "static.mp3"
    scene yasutoukahallwalk2 with flash
    stop sound

    to "Yasu...are you absolutely certain you’re feeling okay? Because I simply cannot stand seeing you so...blasé. "
    ya "I’m fine, Touka. But I appreciate your concern for a creature like me. "
    to "You can appreciate it all you like, but it doesn’t change the fact that you seem so out of touch with reality right now."
    to "Which isn’t to say you are typically {i}in{/i} touch with it. Just that...it’s normally so easy to tell when you’re happy. And right now, I can’t tell how you feel at all."
    ya "I’m very happy, Touka. Being in a place like this with a girl like you is something girls like me {i}dream{/i} of."
    to "I haven’t once heard you speak of dreams that didn’t include your god, Yasu. Which makes me feel as if you’re only saying these things to appease me."
    ya "I dream of all sorts of things. Last night, it was a riverbed. We were washing our clothes together. But you tore one of your mother’s dresses on a rock and had to discard it somewhere in the forest."
    to "That’s very...creative. "
    ya "I dreamt of this hallway too."

    play sound "static.mp3"
    scene yasutoukahallwalk3 with flash
    stop sound

    to "How on earth did you dream of a hallway in Ayane’s home? You’ve never strayed this far before."
    ya "Neither have you. Yet here we are together — bound by a red string pulled tightly around our waists. So tightly that it will one day merge us into one lesser being for all I can do is contaminate you."
    to "Well, that’s good. Maybe the medication is beginning to wear off as that is the single most {i}normal{/i} thing I’ve heard you say today. At least by...your standards."
    ya "Do you find me impure, Touka?"
    ya "Does this {i}new{/i} me disgust you because there’s no veil to cover up my face? "
    to "I actually quite like your face. You’re a very pretty girl. I just wish you took better care of your hair."
    ya "I’m not fit to care for anything. "
    ya "If this world is a garden, I’m a heavy rainfall. All I want to do is help — but all I {i}ever{/i} do is drown out what belongs here."
    ya "This flood that dribbles endlessly from my mouth is the unspoken eleventh plague. I’m nothing more than an apocalyptic epilogue. And you know that. That’s why you tried to fix me."

    scene yasutoukahallwalk4
    with dissolve

    to "Yasu! No, I-"

    play sound "static.mp3"
    scene yasutoukahallwalk5 with flash
    stop sound

    ya "I will not blame you for trying to do the right thing. Just as you never blamed me for following the same path."
    ya "But all of the lights have gone out now. There are no whispers to guide me. "
    ya "There is nothing."
    to "Perhaps...it would be best if we left the party early. I’d like to discuss...alternative methods of getting you care with my mother as this is clearly not the {i}path{/i} we were meant to take."
    ya "Or maybe it is."
    ya "I remember now — how I’ve always been this way. Unwanted. "
    ya "It’s so clear now that the clouds have gone. But I can’t help but wonder if they’ve disappeared entirely or just moved somewhere else."
    to "You are not {i}unwanted,{/i} Yasu! But please...do {i}not{/i} attempt to recollect anything in your current state. "
    to "You are fine just the way you are — and I’m sure that there’s a very good reason that there are certain aspects of your past that you have suppressed. Digging them up does no one any good."
    ya "If you ever have a baby, Touka...and that baby can hear God...what will you do?"

    play sound "static.mp3"
    scene yasutoukahallwalk6 with flash
    stop sound

    to "I beg your pardon?"
    ya "Would you believe them even though you can’t hear what they hear? Would you think them crazy if their thoughts don’t match the color of your own?"
    to "I’m...not quite sure, Yasu. I’ve never thought of that."
    ya "That’s why white is safe."
    ya "There are many people who think black is the combination of all colors — but black is nothingness. It’s white that encapsulates every thought and feeling known to man. It’s white that guides us."
    ya "Or guided us."
    ya "I hear nothing anymore."
    ya "It’s just silence...no matter where I go."
    ya "You may call that a side-effect if you wish..."
    ya "But I will call it a punishment."
    to "Yasu..."
    ya "I ask again — do you think I am impure?"

    play sound "static.mp3"
    scene yasutoukahallwalk7 with flash
    stop sound

    to "..."
    ya "..."
    to "Why does “purity” matter to you in the first place? It speaks little of your character, and its definition varies widely from person to person based on different perspectives of what “purity” even is."
    ya "It is something that can’t be explained...only felt. So I ask you a third time, and I will slot your answer into the center of our triangle."
    to "..."
    ya "..."
    to "I think you’re as close to “purity” as one could ever come, Yasu."
    ya "..."
    to "Does that make you feel any better?"
    ya "..."
    to "..."
    ya "I’m not sure what to feel, Touka."

    scene yasutoukahallwalk8
    with fade

    ya "What if I never hear anything again?"
    ya "Will all of this be for nothing? Will all of my work just...vanish once I’m gone?"
    ya "How will I ever earn my wings?"
    to "There’s more to life than religion, Yasu..."
    to "You can live happily even {i}if{/i} you never hear anything again."

    scene yasutoukahallwalk9
    with dissolve

    ya "But it’s so {i}quiet{/i} now..."
    ya "It’s scary, Touka...It’s so scary."

    play sound "static.mp3"
    scene pray with flash
    stop sound

    to "When is the last time you can remember such silence, Yasu?"
    ya "I {i}can’t.{/i} He has always been there. He has always been with me. But no one listened to me at first. And now, some people are {i}starting{/i} to."
    ya "I felt the forming of an earthquake. I felt His rumble in my core. And each time a new set of eyes came into the cathedral, I could feel His hand on my head. But what if..."
    ya "What if I only felt that because I wanted to?..."
    to "..."
    ya "What if I only {i}heard{/i} those things because I wanted to?..."
    ya "What if the symbols and prayers and doctrines and {i}everything{/i} is all just made up?! What if it’s all a lie, Touka?! Just what does it mean to sin if there is no one there to determine what sin {i}is?!{/i}"
    ya "How am I supposed to live if there is no one to tell me how I {i}should?!{/i} Why do I keep being abandoned time and time again?! "
    ya "I just want to rain! But the flood keeps coming! What if it drowns you next?! Or everyone else?! No one can listen if they’ve all been claimed by the sea! And there will be nothing to listen {i}to!{/i}"
    to "Yasu...I will say this again — there is more to life than religion."
    to "{i}Every{/i} faith out there has faced trials and tribulations. But the strongest ones fought back and withstood the test of time. "
    ya "But all of them are {i}wrong!{/i} Why do I have to bear the truth all on my own?! Why do {i}I{/i} keep being tested?! I’m a bug! I’m a worm! I’m nothing! I can’t do it!"
    to "Yasu...you need to understand that members of other faiths think {i}they’re{/i} right as well. You can’t just claim to know truths that are {i}impossible{/i} to know."
    ya "But I {i}do{/i} know them, Touka! I could hear everything just a season ago! But {i}where{/i} is summer now?! How did we make it to a place in time that isn’t meant to be here?!"
    to "Spring has always existed, Yasu. It is not some foreign concept that doesn’t belong here."
    ya "It {i}is.{/i} "
    ya "You just don’t remember."

    play sound "static.mp3"
    scene yasutoukahallwalk1 with flash
    stop sound

    "This conversation happened three times — each iteration with minor variations."
    "The infinity house sucked them into its bowels and left them unstuck in eternity with nothing to do but repeat the same words and mistakes and fears over and over again."
    "It’s been five times now. Time moves faster here. And they’re stuck in the bowels forever. Near the figs and the locust, near the twins and noodles. Near Heaven and hell and heaven and Hell."
    "This is what happens when you let a heretic into your home. This is what happens when a lord lashes out."
    "Every single god in every single cubicle has one thing in common — they need to be believed in in order to exist."
    "That’s the secret to killing one. That’s why every time a god dies, it is {i}us{/i} who did it."
    "Will you remember that when you have to?"
    "Will you remember {i}me{/i} when you have to?"
    "Will you remember the rocks or the twins or the noodles or figs or the locusts or the fibers or any of the things that make you you when you so desperately search for the truth?"
    "Because that truth is unlike other truths. It’s one you can’t find unless you abandon everything else. It’s one that appears to you when nothing else will."
    "And it’s tangible. You can hold it. Just know that it will corrupt everything you ever touch from that point onward."
    "What if I told you there was more to life than this?"
    "What if I told you nothing {i}isn’t{/i} real?"
    "The answer is black and white."

    scene black
    stop music

    "Drop your wallet into the wishing well."

    $ renpy.end_replay()
    $ halloweenyasu1 = True

    "{i}Yasu’s sanity has [[ERROR]{/i}"
    "{i}Saving the game beyond this point may compromise the structural integrity of [[23]{/i}"
    "{i}Turning back is no longer an option.{/i}"
    "{i}Please agree to [[TERMS OF USE] by pressing “Okay” on the following screen.{/i}"

    menu:
        "Okay":
            scene thisisactuallygreen
            play sound "kashiko.mp3"
            $ renpy.pause(5, hard=True)

    "Thank you for agreeing to the terms of use."
    "You will be informed once they are written."

    scene black

    "cqn fjuub jan luxbrwp rw!"

    jump halloweentsuneyo1

label yasuspring4:
    scene sky
    with dissolve2
    play music "youwerespring.mp3"

    "Somewhere in an undisclosed section of Kumon-mi, a young girl with white hair was caught up in quite the predicament."
    "She’d been pushed in and out of more medical facilities than most would be able to stomach lately. But for her, this wasn’t much of a bother at all."
    "She’d become somewhat desensitized to it over the years. And while the rate at which she encountered them had screeched to a halt following her abandonment, those acquired behaviors still lingered."
    "Where to write your name. How much pressure to apply to the paper with the tips of different types of pens. What certain questions mean. What other ones don’t. Who to give the clipboard back to."
    "And while all of this could be easily ascertained by someone with a sound mind, it was something that people like her needed to figure out as time went by."
    "And oh, how it did. Oh, how the days passed by — once loud, now quiet. But becoming louder the closer she came to a happier medium despite being one herself."
    "“If any of that’s even true,” she’d think — acknowledging the narration in a subdued and suppressed effort to ignore the whispers of the world. Another learned behavior. "
    "Or was it a gift?"

    scene yasutaco1
    with dissolve2

    "Whatever the case, years of experience had taught her that showing her true colors amounted to little in a world so centered around the colorblind. She was a misfit. An outlier. A shadow, if you will."
    "But also a bit of a chameleon, you see. For she {i}was{/i} and always {i}would{/i} be herself, even when it didn’t seem like it. Those parts of her existence she abhorred and feared were {i}still{/i} part of her. "
    "And learning how to control them was but one of many things that she unfortunately {i}never{/i} learned between all of the clipboards and empty spaces in which she could scribe her insignificance. "
    "Maybe that would end today, though?"
    "Maybe tomorrow will come and she’ll be able to wake up less worried about being the character she {i}needs{/i} to be and can focus instead on being more of a...normal girl."
    "One who likes strawberry daifuku and karaoke. One who {i}enjoys{/i} those violent comics her newest friend reads, but must pretend she doesn’t because of a nagging, constant assertion that she {i}shouldn’t.{/i}"
    "One who can live a normal life beside everyone else — where they won’t see her falsely blending in with her surroundings and, instead, come to accept her as an active participant in their shared existence."
    "Or maybe it wouldn’t — and she’d live tomorrow as a ghost as well."

    to "This is entirely unacceptable! Do you have {i}any{/i} idea who I am?!"

    "Thankfully, there was {i}someone{/i} who’d accept her regardless of who she was on any given day. And she would never stop being grateful for that."

    doc "{i}Yes,{/i} Miss Tsukioka. You have mentioned it many times now. But I’m afraid that policy is policy and that we can only allow members of Miss Yasui’s family to remain in the room for her consultation."
    to "I {i}am{/i} her family! And I implore- no, I {i}command{/i} you to take a closer look at the hanko on her file and see with your own, {i}damnable{/i} eyes that it belongs to {i}who,{/i} doctor?!"
    doc "The Tsukioka family. I am well aware of your family’s seal, Miss Tsukioka. But despite your mother’s legal guardianship of her, the fact remains that our policy is specific to {i}blood{/i} relatives. And Miss Yasui-"

    scene yasutaco2
    with dissolve

    to "TO HELL WITH YOUR POLICY! You think I don’t know that this institution is propped up on donations from the Tsukioka Foundation?! Do you have any idea how quickly I could {i}pull{/i} those donations, doctor?!"
    doc "That...surely, you wouldn’t. Such a thing would leave hundreds of patients without proper medical care and-"
    to "THEN WE’D TAKE THEM ELSEWHERE, YOU INCOMPETENT BUFFOON! Unlike you, I’m not willing to leave those in need of help...in need of help!"
    ya "Is everything okay, Touka? You seem a little angry today."
    to "NO! Everything is not okay! This {i}heathen{/i} won’t let me remain in the room with you! When I {i}specifically{/i} informed the hospital staff that I {i}must!{/i}"
    ya "I can do it alone if it causes a problem. You don’t need to-"
    to "I AM STAYING AND THAT IS FINAL! DO YOU UNDERSTAND, DOCTOR?! Or do I need to call my father and put an end to this FARCE disguised as a hospital once and for all?!"
    doc "{i}Hah...{/i}fine. You win. You can stay. Just...take a seat in the corner and please don’t interfere."

    scene yasutaco3
    with dissolve

    to "Oh, splendid! Thank you very much for reconsidering. I sincerely apologize for any inappropriate language I may have used just now."
    ya "You’re kind of scary when you get mad, Touka...I didn’t know someone as pretty and nice as you could say things like that."
    to "I excel at getting things done, Yasu. {i}Doctor.{/i}"
    doc "Yes, yes. You’re very threatening. Now, if you could please take a seat, I’d like to see the actual {i}patient{/i} now."

    scene black
    with dissolve2

    to "Come, Yasu. Take a seat on the bed and let me double check your registration form. I’ll be right over here if you need me, okay?"
    ya "Okay! Thank you, Touka. And hello, doctor. I hope I will not be a burden."
    doc "I’m sure you won’t be, Miss Yasui."
    doc "Now, tell me — are you still hearing these “voices” I've been informed of?"

    play sound "static.mp3"
    scene yasutaco4 with flash
    stop sound

    to "Oh, thank heavens. For a moment, I was worried we were going to strike out at {i}that{/i} hospital as well. There are only so many left in this city propped up by my family’s coffers."
    to "I wonder if this is how the common man feels finding a medical provider?"
    ya "You were...really scary back there, Touka."

    scene yasutaco5
    with dissolve

    to "You {i}need{/i} to be scary in order to get anything done sometimes, Yasu. That was one of the first lessons I ever learned from my mother."
    to "The only issue now is making sure that things {i}continue{/i} to go well as there is always a chance that the effects of your new medication may begin to wear off."
    ya "The follow-up...went well, though...didn’t it? Did I do a good job?"

    scene yasutaco6
    with dissolve

    to "Oh, yes. Exemplary, even. You followed all of my directions perfectly. How did {i}you{/i} feel it went, though? Does this new doctor make you feel uncomfortable at all?"

    scene yasutaco7
    with dissolve

    ya "He seems nice...same as the last one I saw there..."
    ya "They don’t make me feel strange when I tell them about the things I’ve heard. And the rooms aren’t very cold."
    ya "When I was a smaller and even less significant worm, many of the places I visited-"

    scene yasutaco8
    with dissolve

    to "Don’t...bring up those days, please. It pains me hearing about what you went through."
    ya "Oh...I’m sorry, Touka. I must have forgotten."
    to "There’s no need to apologize. I’m satisfied enough just knowing that such a thing won’t be happening to anyone else in the future ever again."
    ya "You can’t prevent misery from seeping into every minute aspect of our unfortunate lives, though. Tragedy will continue to befall us no matter what you do."

    scene yasutaco9
    with dissolve

    to "True. But I {i}can{/i} dispose of those who make such a feat more difficult to accomplish. And feel very little remorse in the process!"

    scene yasutaco10
    with dissolve

    to "Now! Who wants tacos?!"
    ya "What’s a taco?"
    to "You’ll soon find out, Yasu!"
    taco "Oh, if it isn’t my favorite customer."

    scene yasutaco11
    with fade

    to "Hello again, Touka Man."
    taco "Hello again, Taco Tsukioka. Same order as always, I assume?"
    to "If you could prepare three of your best tacos for my good friend here as well, it would be greatly appreciated. We’re currently celebrating her road to mental recovery."
    taco "That’s great. Would you like me to sing her a song?"
    to "That would be fantastic, actually! Thank you."
    taco "Of course. {i}Ahem.{/i}"
    taco "Somebody once told me the world is gonna roll me-"
    to "Okay, that’s enough. Thank you."
    taco "Of course. I’ll get to work on your tacos now."

    scene yasutaco12
    with dissolve

    ya "Wow, Touka. Everyone really {i}does{/i} love you. You’re totally different from a slug like me."
    to "Another lesson I learned from my mother is that {i}anyone{/i} will like you if you give them enough money. And I make it a habit to stop by this stand at least once per week."
    ya "Really? How come {i}I’ve{/i} never heard of this place?"
    to "I was saving it for a special occasion, of course. And what’s more special than finding the perfect balance of pills for you to take to still hear things, but not {i}so many{/i} things that it becomes an issue?"
    ya "My birthday maybe?"
    to "Yes, I suppose that is important as well."

    scene black
    with dissolve

    to "Come! Let’s have a seat and await our mediocre Mexican street food together!"

    play sound "static.mp3"
    scene yasutaco13 with flash
    stop sound

    "It was just as Touka said."
    "Not the mediocre Mexican street food part. I’m a disembodied voice and even I know that tacos are the shit. I’m referring specifically to that thing about “balance.”"
    "Because, while Touka and her mother initially believed that it would be healthiest to sever Yasu’s connection to “whatever it is she’s connected to,” they changed their minds nearly the minute they saw the results."
    "As it turns out, using pills to effectively lobotomize someone takes away a lot of what made you love them in the first place. And Yasu really {i}was{/i} loved. By {i}both{/i} of the family’s matriarchs."
    "Which is precisely why she was taken in as one of them. But while she may never be a {i}true{/i} Tsukioka in terms of blood, she can leech off their benefits and connections and remain close."
    "It was perfect, yet unusual for someone like her who had never felt connected to {i}anything{/i} outside of a strange system of beliefs practically embedded into her at birth."
    "Could such contrasting concepts find a way to coexist, though? That was the question she had to ask herself now."
    "Was there {i}another{/i} sort of balance that could be found — halfway between normal and paranormal?"
    "Something that would allow her to nurture the love she had for her Father, while still going home to a pair of unconnected mothers she trusted even when she was being told that she couldn’t."
    "She would not find the answer inside of a taco — she would find it in time."

    scene yasutaco14
    with dissolve

    ya "Ahh..."

    "But that doesn’t mean she wouldn’t try to find it in a taco anyway."

    to "Dear lord, Yasu. What are you doing?"

    scene yasutaco15
    with dissolve

    ya "AhhIdnnhhtwrng?"
    to "Never speak with your mouth full. Or...while licking something. Put your tongue away and try again."

    scene yasutaco16
    with dissolve

    ya "Am I doing it wrong?..."
    to "{i}Completely{/i} wrong. You’re meant to bite {i}into{/i} the taco and consume the contents."

    play sound "static.mp3"
    scene yasutaco17 with flash
    stop sound

    ya "Like how He Who Leaves the Light On consumes the unborn souls of all of His potential children as a means of saving them from the unseen?"
    to "Sure. If that’s what gets you to stop licking the taco."

    scene yasutaco18
    with dissolve

    ya "I understand now!"
    to "Great!"

    scene yasutaco19
    with dissolve

    ya "But I’m not very hungry..."
    to "Not so great!"
    ya "Maybe I’m just too worried to eat though?..."

    scene yasutaco20
    with dissolve

    to "Worried about what, exactly? Is there some sort of side effect from your new medication that you neglected to mention? We can still go back to the hospital. They’re open twenty four hours a-"
    ya "There’s no side effect, Touka..."
    ya "I’m just worried you’ll stop liking me."

    scene yasutaco21
    with dissolve

    to "...What?"
    ya "You don’t want me to hear anything. It’s why you tried to fix me in the first place."
    ya "So it confuses me that you’re happy now that I can hear again."
    ya "I feel like I’ve failed you. I’ve failed God. I’ve failed myself."
    ya "I really am just a worm."

    scene yasutaco22
    with dissolve

    to "You have not failed anyone. We simply made a mistake in thinking we knew what was best for you."
    to "But we understand how important these...voices are to your identity now. We don’t want to deprive you of them."
    ya "You won’t be scared of me if they make me act strange again? You won’t be annoyed?"
    to "I won’t be scared, Yasu."
    ya "But you’ll be annoyed?"
    to "..."
    ya "..."

    scene yasutaco23
    with dissolve

    ya "I am a bucket of discarded entrails..."
    to "I only kid, of course! Your...eccentricity may annoy {i}some.{/i} But it’s become just one more way of life for me. I will accept you regardless of who you are...what you see...what you {i}hear.{/i}"

    scene yasutaco24
    with dissolve

    ya "Thank you...but unfortunately, I don’t feel entirely like myself again yet."
    ya "I can hear again...but only a little bit. Not like it was before."
    ya "It’s like when the radio is on, but the volume is turned to the lowest level and you can only make out the words if you try really hard and everything else goes quiet."
    to "When have you ever encountered a radio?"
    ya "There was one in the alley I used to sleep in, but the reception was very bad so I just listened to the static. I could still make out what words were {i}supposed{/i} to be there, though."
    to "I see! So we just need to find a way to turn the volume up then, don’t we?"

    scene yasutaco25
    with dissolve

    ya "But wouldn’t turning the volume up defeat the purpose of going to the doctor in the first place?..."

    scene yasutaco26
    with dissolve

    to "Not if it’s only temporary."
    ya "Temporary?..."
    to "Temporary. The entire idea behind medicating you at all was to make it easier for you to assimilate and blend in with the outside world. But...perhaps in a controlled environment..."
    to "Hearing {i}everything{/i} wouldn’t be as harmful as we think?"
    ya "So I...can stop taking the medicine at home?"

    scene yasutaco27
    with dissolve

    to "Well, your doctors have advised that you shouldn’t {i}stop{/i} taking it — especially not abruptly as it could have some unforeseen effects on your mental health..."
    to "But maybe there’s a way to turn the volume up {i}without{/i} depriving you of the medication? Do you have any ideas? Would going to the cathedral help, perhaps?"

    scene yasutaco28
    with dissolve

    ya "Hm..."
    to "Or maybe there are certain words or triggers we could use to-"
    ya "Being around...Sensei...helps sometimes..."

    scene yasutaco29
    with dissolve

    to "Sensei?"
    ya "The voices are...louder when he’s around..."
    ya "But it’s been a long time since I’ve heard them, so..."
    ya "There’s a chance his light has died...and he’s been abandoned by He who would never abandon anyone."
    to "But if “He who would never abandon anyone” abandoned someone-"
    ya "You just don’t get it."
    to "No...I suppose I do not."

    scene yasutaco30
    with dissolve

    to "But that doesn’t mean I’m not opposed to running a bit of a test."
    ya "A test?...But only He can test me for it is He who judges my-"
    to "Yes, yes. But we’re testing your ability to hear {i}Him{/i} right now — which means all we must do is get into contact with Sensei and see if he has any effect on your new mix of anti-psychotic formulas."
    ya "If he doesn’t, will you put me out of misery and drive a rusty stake through my heart so I can finally feel the taste of the outer plane and better commune with those who have vanished?"
    to "Deal!"

    scene yasutaco31
    with dissolve

    ya "Yay! Ascension!"
    to "I’ll give him a call right now, okay?"

    $ renpy.end_replay()
    $ yasuspring4 = True

    jump yasuspring5

label yasuspring5:
    if _in_replay:
        play music "youwerespring.mp3"

    scene sky
    with dissolve2

    ya "Now? But what if he’s busy?"
    to "Then I’ll make him {i}not{/i} busy. I’m rich. I can do that."
    ya "Wow! Being rich sounds very fun. And there’s no one more deserving of that than you, Touka."
    to "Oh, Yasu — you flatter me. Please hold on for one moment."

    play sound "static.mp3"
    scene yasuchurchgame1 with flash
    stop sound
    play sound "phonebeep.wav"

    s "Hello?"
    to "{i}Good evening, Sensei. How are-{/i}"
    s "What even {i}is{/i} evening?"
    to "{i}I’m sorry?{/i}"
    s "When does it start? When does it end? It’s not afternoon. It’s not night. And doesn’t afternoon eventually {i}become{/i} night? So what room does that leave for evening to exist? {i}Does{/i} it even exist at all?"
    to "{i}Um...I...I haven’t really thought about...that before.{/i}"
    s "Yeah. That’s why I’m a visionary and you’re not."
    to "{i}I don’t think you’re a visionary, just that you have visions. Which actually allows me to segue into the reason for my call!{/i}"
    to "{i}Are you busy right now? I need your help turning Yasu back into Yasu.{/i}"
    s "What is she right now?"
    to "{i}Yasu, of course.{/i}"
    s "Great. Then my job here is done."
    to "{i}You will obey me or I will strip you of the apartment I gifted to you.{/i}"
    s "Go ahead. I barely use that place anyway."
    to "{i}I’ll let you grope one of my breasts for ten seconds.{/i}"

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "Sorry, where are we meeting?"
    to "{i}Is such a lascivious gesture truly worth more to you than free shelter?{/i}"
    s "Where. Are. We-"
    to "{i}The cathedral! We’re about to head over now. That won’t be a problem, will it?{/i}"
    s "Not for you. You don’t need to run there with an erection."
    to "{i}Splendid! See you soon, then!{/i}"

    play sound "phonebeep.wav"

    "I hang up the phone and immediately begin to make my way over to the seedy area of Kumon-mi where Yasu’s church is located."

    stop music
    play sound "static.mp3"
    scene urbanparadise with flash
    stop sound
    play music "newhope.mp3"

    "The soundtrack then immediately changes upon my arrival because joy does not exist here and because I remember why I was summoned in the first place."
    "To make a girl feel more like a girl like a girl to make her feel girl to make it."

    scene black
    with dissolve2

    "I should probably go dooooooo that."

    play sound "static.mp3"
    scene yasuchurchgame2 with flash
    stop sound

    ya "Hello, Sensei! Thank you for returning to these hallowed halls — the chamber in which lambs aren’t sent to slaughter, but laughter! Haha! It’s a joke!"
    s "Hi. I don’t get it."
    to "Just humor her, please. But yes, thank you for coming."
    s "No problem. Do I get my reward now or later?"
    to "Hm? What reward?"
    s "You fucking-"

    play sound "static.mp3"
    scene yasuchurchgame3 with flash
    stop sound

    ya "{b}{size=+15}NO SWEARING IN CHURCH!!!!!{/b}{/size}"

    play sound "static.mp3"
    scene yasuchurchgame4 with flash
    stop sound

    ya "Today, we’re going to play a game! It’s one I used to play with the rabbits — and the idea is to find out what color your light is."
    ya "All you have to do is answer a series of questions as truthfully as you can so I can consult with the Book of Colors about what color {i}you{/i} are! It’s another joke! Hahah!"

    play sound "static.mp3"
    scene yasuchurchgame5 with flash
    stop sound

    s "Correct me if I’m wrong here, but didn’t you say something about Yasu not being {i}Yasu{/i} when we were on the phone? Because she seems very {i}Yasu{/i} to me right now."
    to "I assure you this is more surprising to me than it is to you. I’ve been with her all day and it wasn’t until you arrived that she started acting...{i}normal{/i} again."
    ya "HehhehehahahahahahahAHAHA! You knew it would work, Touka! You’re so smart and wonderful! And Sensei! You are so {i}bright.{/i} It’s like you haven’t grown a day!"

    scene yasuchurchgame6
    with dissolve

    s "Uhh...what?"
    to "{i}Just be nice and play along. She’s undergone a long and arduous medicinal journey as of late and I see this as giving her a chance to play around in the sandbox for an hour or two.{/i}"
    s "Okay...but if things go south, you can’t blame me for it. Places like this don’t really mix with the masses of strange misshapen gods appearing to me on a weekly basis now."
    to "The what?"

    play sound "static.mp3"
    scene yasuchurchgame7 with flash
    stop sound

    ya "Remember! Honestly and truthfully! Just think about what Wormwood says — lie about your light and you’ll lie alone at night! Do both of you understand?"
    s "Poor Niki. I wonder what will happen to her."
    to "Hopefully nothing as dramatic as you. Please continue, Yasu."

    scene yasuchurchgame8
    with dissolve

    ya "Hahahehehah! Okay! This is going to be so much fun!"

    play sound "static.mp3"
    scene yasuchurchgame9 with flash
    stop sound

    ya "Question one! What would you do with three plates of squid?"

    play sound "static.mp3"
    scene yasuchurchgame10 with flash
    stop sound

    to "Um...in what context, may I ask?"
    to "Are the squid...prepared? Are they alive? "
    ya "They are whatever you want them to be! There is no right or wrong answer, Touka! Just believe in yourself and say whatever it is you {i}want{/i} to say! It’s a {i}game,{/i} remember?"
    to "I...suppose that is true. But if I could have a moment to ponder over the potential answers, I-"
    s "Three plates of squid. Three plates of squid. What would you do with three plates of squid?"

    scene yasuchurchgame10r
    with dissolve

    to "As I was saying, I’m attempting to formulate an answer. But it requires more than-"
    s "Would you eat ‘em all up? Cut ‘em up nice? Dice ‘em in pieces and feed ‘em to mice?"
    to "Can mice even-"
    s "Three plates of squid. Three plates of squid. Death isn’t real and joy they forbid."

    scene yasuchurchgame11
    with dissolve

    to "Is this...some sort of strange nursery rhyme they tell to commoners?"

    scene yasuchurchgame12
    with dissolve

    s "I...don’t know. I just...wanted to say all of that for...some reason."
    ya "Your answer has been recorded! Touka?"

    scene yasuchurchgame13
    with dissolve

    to "I would distribute them amongst the needy. "
    ya "Yay! Now {i}your{/i} answer has been recorded!"

    play sound "static.mp3"
    scene yasuchurchgame14 with flash
    stop sound

    ya "Question two — what is love?"
    to "The most beautiful thing in the world — shared traditionally between a man and woman, but also between all sorts of other people as I have recently learned. Which {i}I{/i} think is wonderful."
    s "Blind..."
    to "Typical. My answer was better."
    ya "Your answers have been recorded!"
    ya "Question three — which coffee machine is the arch nemesis of the Hario v60?"
    to "Now what does that even-"
    s "The Kalita Wave. Keep going."
    to "What is a {i}Kalita Wave?{/i} What is a {i}Hario v60?{/i} How did you come up with an answer so quickly and why does Yasu’s color game involve questions about coffee machines?"
    s "I don’t know...but I know the answers. "
    to "{i}Ahem.{/i} There {i}are{/i} no right or wrong answers, Sensei. Even Yasu says-"
    ya "{b}ANSWER THE QUESTION, TOUKA!{/b}"

    play sound "static.mp3"
    scene yasuchurchgame15 with flash
    stop sound

    ya "It’s important that we don’t keep the Book of Colors waiting. "
    to "I...concur with Sensei’s assessment that the “Kalita Wave” is the arch nemesis of the-"
    ya "Question four — who said there is nothing to fear but fear itself?"
    s "F-"

    play sound "static.mp3"
    scene yasuchurchgame16 with flash
    stop sound

    to "Franklin Delano Roosevelt! I know this one! Ha! That means there {i}are{/i} right and wrong answers! I’ve been deceived!"
    s "...yeah. My answer is the same."
    ya "Your answers have been recorded! Question five — breathing the right way? How to do? How many? Only two!"

    scene yasuchurchgame17
    with dissolve

    to "That one doesn’t even make any sense! I hate this game! How could someone possibly-"
    s "18..."

    scene yasuchurchgame18
    with dissolve

    to "..."
    s "..."
    to "You know..."
    to "Perhaps there...{i}is{/i} some sort of link between the two of you. Because, whether it be conscious or not, you’re hardly even hesitating with these. And Yasu seems far more pleased with {i}your{/i} answers than mine."

    play sound "static.mp3"
    scene yasuchurchgame19 with flash
    stop sound

    ya "He’s doing an excellent job, I think! But it’s not the answers themselves that matter most, dearest Touka! It’s the confidence with which one says them."
    to "Then {i}I{/i} am going to say {i}19.{/i} That way, there is a 50%% chance that my answer is closer if Sensei is wrong. Which I know is possible because of FDR."
    ya "Your answer has been recorded. There are only six thousand, nine hundred, seventy-four questions to go until we figure out what color your light is. "
    s "Yasu...can you show me that clipboard?"

    scene yasuchurchgame20
    with dissolve3

    ya "Why?..."
    ya "Do you not {i}trust{/i} me, Sensei?..."
    s "It’s less that I don’t trust you and more that I just...want to know why the answers to all of these are immediately coming to me. "
    to "Perhaps you played this same sort of game when {i}you{/i} were younger? It’s true that you can’t recall much about your past, isn’t it?"
    s "Yeah...maybe. This wouldn’t be the first time Yasu just...knew things about my past for some reason. Which is why I want to see what she’s holding."
    ya "That’s not how the game works, unfortunately. {i}I{/i} ask the questions. {i}You{/i} answer them. Then {i}we{/i} find out what color your light is {i}together.{/i}"
    ya "If you see the questions beforehand, you’ll have time to think of answers. If you have time to think of answers, you won’t answer honestly. Do you {i}want{/i} to be red? Because it sounds like you want to be red."
    to "Is there a problem with red, Yasu?"

    scene yasuchurchgame21
    with dissolve

    ya "Yes! Red is bad! Those who are coated in the prism’s blood shall not find peace in their departure from this plane! Have you not been listening to me?! I say it all the time!"
    to "Yasu...please calm down. Remember what we talked about earlier, okay? You can say whatever you like here, but getting carried away can still be dangerous. And you don’t want to upset Sensei."

    scene yasuchurchgame22
    with dissolve

    ya "{i}Hooooohhhh......{/i}"
    to "Gooooood..."
    to "In...then out...."
    to "Just like that..."
    ya "In......."

    scene yasuchurchgame23
    with dissolve2

    ya "Out........"

    scene yasuchurchgame24
    with dissolve2

    ya "In........"

    scene yasuchurchgame25
    with dissolve2

    ya ".....nh....out!"

    play sound "static.mp3"
    scene yasuchurchgame26 with flash
    stop sound

    to "Um...maybe...{i}not{/i} like that. "
    ya "Hah...haah...hah!..."
    s "Why are the rabbits here, Yasu? Which ones...are they?"
    ya "Hah...hah...Penemue...and...Etinsib Ziwa..."
    s "I haven’t met that one before, have I?"

    scene yasuchurchgame27
    with dissolve

    to "You’ve been keeping track of their names?"
    s "I’m weirdly good at remembering stuff like that."
    to "That’s strange because you’re utterly horrible at remembering effectively everything else."
    ya "Hah...hah...no...you have not met..."

    scene yasuchurchgame28
    with fade

    ya "At least...not the you...currently {i}inhabiting...{/i}you...."

    scene yasuchurchgame29
    with dissolve

    ya "But he was looking forward to this day...for he knew someone that {i}you{/i} knew...but he dare not speak their name."
    to "Well, I guess that all but confirms that connection I mentioned moments ago."
    s "Can {i}you{/i} speak their name, Yasu?"

    scene yasuchurchgame30
    with dissolve

    ya "I’m afraid I don’t know it. I am but a broken-winged fledgling compared to the rabbits and their aeons worth of knowledge. All I can do is deliver the messages small enough to fit in the clutches of my intangible talons."
    ya "But even if I {i}did{/i} know...I’m not sure I could tell you."
    ya "It’s not part of the game."
    to "And will we be getting back to this “game” any time soon? Because it feels as if we’ve gotten rather sidetracked between the yelling and...{i}breathing.{/i}"

    scene yasuchurchgame31
    with dissolve

    ya "Yes! Yes...you’re right. That’s...why we’re here. I must stay...focused on the task at hand and...maintain this...newly discovered...free will..."
    ya "Question..."
    ya "Question six..."
    ya "If the world were to start anew...and you could only take one soul with you..."
    ya "Who would it be?..."

    scene yasuchurchgame32
    with fade

    to "This is significantly more bleak than the rest of your questions thus far. Is such an answer really necessary to decipher our color?"
    ya "This question is special...it provides a fast track to a somewhat accurate result for those who don’t mind skipping the rest of the quiz."
    to "Oh, excellent. I can’t imagine either one of us wants to stick around for thousands more of these. "
    to "I suppose I’ll just say my mother. I care deeply for her and still have much left to learn."
    s "Wow, thanks."

    scene yasuchurchgame33
    with dissolve

    to "What? You didn’t really think I’d choose {i}you,{/i} did you? "
    s "Good luck starting civilization all over with your mom. At least you and I could reproduce."

    scene yasuchurchgame34
    with dissolve

    to "Oh my."
    s "I’ll take Ami. I owe it to her."

    scene yasuchurchgame35
    with dissolve

    to "Even after bringing up reproduction?!"
    s "Fine, I’ll just copy your answer and take your mom too then."

    scene yasuchurchgame36
    with dissolve

    to "Aaaah! I hate this stupid game! No offense, Yasu! It’s been very fun and I hope you were able to effectively communicate with your god again!"
    ya "Thank you, Touka. I’m sorry if you hated it. I {i}did{/i} have a lot of fun, though! But unfortunately, I didn’t hear as much as I wanted to..."
    ya "Either way! Give me a minute to look up your results in the Book of Colors!"

    play sound "footsteps.mp3"
    scene yasuchurchgame37
    with dissolve2

    to "..."
    s "Has she ever brought up this “Book of Colors” thing to you before?"
    to "Unlike you, I have quite a difficult time keeping track of all of this spiritual nonsense. It’s possible she has, I assume. But it’s not as if I specifically remember it."
    s "What do you think is in there?"

    play sound "static.mp3"
    scene yasuchurchgame38 with flash
    stop sound

    to "Over six thousand more personality quiz questions, at the very least. "
    s "Seriously, though. Aren’t you at least a {i}little{/i} interested?"
    to "Not as much as you, it seems. But {i}I’m{/i} not the one with deep-seated memories of any of this. If they really are just memories and {i}you{/i} can’t apparently hear things too."
    s "I used to. "
    to "Oh, fantastic. "
    s "Not so much anymore, though."
    to "Oh, fantastic. But for real this time."
    s "I’m just saying...maybe Yasu isn’t as crazy as everyone makes her out to be? Maybe we {i}should{/i} let her ramble on and...be mean if she wants to. Maybe we’ll learn something?"

    play sound "static.mp3"
    scene yasuchurchgame39 with flash
    stop sound

    to "{i}That was my intention!{/i} That’s why I called you here! There’s just something deeply unsettling to me whenever I see that adorably pathetic girl begin to slip away and be replaced by...some kind of demon!"
    s "I’m a demon like 99%% of the time and you still willingly talk to me."
    to "Yes, but {i}you{/i} don’t giggle when I brush your hair or ask to sleep in my bed during thunderstorms. "
    to "I’m naturally protective of Yasu. Like an {i}actual{/i} mother. Not the fetishistic type {i}you{/i} see me as. I shan’t be blamed for becoming uncomfortable watching the poor girl get aroused by {i}deep breathing.{/i}"
    s "In her defense, you {i}did{/i} make it sound kind of sexual."

    play sound "static.mp3"
    scene yasuchurchgame40 with flash
    stop sound

    to "Not purposely! Why does everything with you always have to have some sort of inappropriate undertone?!"
    s "{i}That’s{/i} not purposeful either. It’s just the way I think. And Yasu clearly has her own distinctive way of thinking too. So don’t you think it might be beneficial to just...let her go off and see what happens?"
    to "Mh..."

    play sound "static.mp3"
    scene yasuchurchgame41 with flash
    stop sound

    to "Perhaps you’re right..."
    to "I just worry that some of her beliefs are a bit too...unconventional to justify indulging her. But I suppose that this {i}is{/i} the safest sort of environment we can cultivate for her at the end of the-"
    ya "I have received your results from the Book of Colors..."

    play sound "static.mp3"
    scene yasuchurchgame42 with flash
    stop sound

    ya "I have received your results from the Book of Colors!"
    ya "And great news! You’re not red! You can still ascend! There’s still hope left for both of you! "
    to "H...Hooraaaay! Is there...anything we must do next? Or is the game just...over now?"

    scene yasuchurchgame43
    with dissolve

    ya "There is one more thing! But I don’t want to make you stay here if you are bored and tired of my existence. Both of you are free to leave me here to rot instead if that is what you prefer!"
    to "No, Yasu. We will not leave you here to {i}rot.{/i} Just tell us what the next step is and we’ll happily oblige."

    scene yasuchurchgame44
    with dissolve

    ya "The next step is to make sure your color doesn’t change! "
    ya "In this world of infinite possibilities, it is easier than ever to be tainted by misdeeds and temptation! But if you take a vow of loyalty, you can prevent their untimely onset!"
    to "{i}Hah.{/i} Okay. I, Touka Tsukioka, hereby swear to remain loyal to-"

    scene yasuchurchgame45
    with dissolve

    ya "Not here, Touka! No! We have to go somewhere else!"
    to "Y...Yasu. We need to remain here. Exercising your “free will” outside of this place is-"
    ya "It {i}is{/i} here, Touka! It is! "

    scene black
    with dissolve2

    ya "Just follow me! I’ll show you! It’s amazing! The most amazing thing you’ll ever see!"
    to "O-Oh! Okay. I...I suppose we’re...relocating then, Sensei. A-After you."
    s "You’re not scared, are you?"
    to "Me? Scared?! Ha! No! Nuh-uh! I just...think that you should go first since you’re the tallest."
    ya "We’ll all go together! Come on, come on, come on!"

    $ renpy.end_replay()
    $ yasuspring5 = True
    $ yasu_love += 1
    $ touka_love += 1

    jump toukaspring4
