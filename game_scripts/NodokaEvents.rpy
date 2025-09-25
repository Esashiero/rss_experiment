label nodokalibrary:
    if nodokablock == True:
        "I don't really think I want to see Nodoka right now..."
        jump satafternoonmenu
    if nodoka_love >= 0 and otohadorm1 == True and nodokalibrary1 == False:
        jump nodokalibrary1
    if nodoka_love >= 5 and nodokalibrary1 == True and day == 6 and nodokalibrary5 == False:
        jump nodokalibrary5
    if otoha_love >= 1 and yumispring2 == True and otohaspring1 == True and otohaspring2 == False:
        jump otohaspring2
    if chap4active == True:
        jump nodokaspringlibrarygen
    if chapthreeactive == True:
        jump nodokasummer2librarygen
    else:
        jump nodokalibrarygen

label nodokainvite:
    if nodokablock == True:
        "I should probably leave Nodoka alone for now..."
        jump callnight
    if nodokainvite1 == False:
        jump nodokainvite1
    else:
        jump nodokainvitegen

label nodokainvitegen:
    play sound "phonebeep.wav"

    "I tap on Nodoka's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    no "Hello, Father."
    s "Hey. What-"
    no "I'm already on my way."
    s "What? Why? What if I wasn't calling to invite you over?"
    no "Then you wouldn't be calling at all."
    s "That's...fair, I guess."
    no "Shall I bring a {i}whip?{/i} Or will just my body suffice?"
    s "Just your body is fine. I'll see you soon, Nodoka."
    no "Oh, you certainly will."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene nodokainvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    no "So...will you be taking me here? Or would you rather we do it on your {i}daughter's{/i} bed?"

    "How should I spend my time with Nodoka?"
    menu nodokainvmenu:
        "Hang Out (Raise Affection)":
            jump nodokainviteaff
        "Doggystyle (Raise Lust)":
            jump nodokainvitedoggy
        "Headpat":
            jump nodokaheadpat

label nodokainviteaff:
    scene nodokainvitegen
    with fade

    "I decide against {i}taking{/i} Nodoka at all and elect to spend a quiet evening by her side instead."
    "She seizes this rare opportunity of non-physical affection to rest her head on my shoulder and read me poetry despite {i}not caring much{/i} for it herself."
    "I ask her why she feels this way and she's reluctant to answer, stating something along the lines of it not being able to adequately explain certain feelings, but..."
    "I feel like it's more her not understanding them than anything. Which is odd to me, given that she has not only made it apparent that she's familiar with poetry but...decided to read it to me today?"

    scene black
    with dissolve2

    "As always, I find it hard to understand her motivations. But I know she won't outright tell me them, so I don't bother pestering her about it."
    "I just lean into her as well and listen to her voice cut through the silence of the bedroom like a blade into-"

    $ nodoka_love += 3
    stop music

    "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"

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

label callnodokamorning:
    if nodokablock == True:
        "I don't really think I want to see Nodoka right now..."
        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I tap on Nodoka's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callmorning

label callnodokaafternoon:
    if nodokablock == True:
        "I don't really think I want to see Nodoka right now..."
        jump callafternoon
    else:
        "Nodoka should be at the library right now."
        "If I want to see her, I should probably go there."

        jump callafternoon

label callnodokanight:
    if nodokablock == True:
        "I don't really think I want to see Nodoka right now..."
        jump callnight
    if chap4active == True:
        jump nodokaspringnightgen
    if chapthreeactive == True:
        jump nodokasummer2nightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Nodoka's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        no "Hello, Sensei. How are things?"
        s "Things exist."
        no "That they do. All sorts of things, actually."
        no "Would you like to see some together?"
        s "Sure. I was actually just calling to see if you wanted to hang out."
        no "Then hang out we shall."
        no "Come meet me at the dorm."

        play sound "phonebeep.wav"

        "I end the call and start heading over to meet up with Nodoka, curious about what the two of us will wind up getting up to tonight."

        scene black
        with dissolve

        "........."
        "......"
        "..."

        scene nodokanightgen
        with dissolve
        play music "justlights.mp3"

        "Nodoka takes me to a mysterious phonebooth in a small park not far from the dorms."
        "I'm not sure why she wanted to come {i}here{/i} of all places, but I'm not about to argue the idea of being alone in a confined space with an attractive girl."
        "She props herself up on a ledge and kicks at the air with her slender legs, humming a slow and melodic tune I don't think I've ever heard before."
        "But even if the sounds are completely unfamiliar, they feel nostalgic in a way."
        "I could listen to her hum this forever."

        scene black
        with dissolve

        "I don't, of course, because forever is a very long amount of time."
        "And even in this world, where time seems to be infinite, I still fear that all things will come to an end."
        "But I guess that's just what it means to think."
        "No thoughts are free when we pay in time and fear to obtain them."
        "I let Nodoka's song distract me from this."
        "And one more night slips between my fingers-"
        "Dissolving into nothing."

        $ nodoka_love += 1
        stop music fadeout 5.0

        "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label nodokalibrarygen:
    scene nodokalibrarygen
    with dissolve
    play music "morningmoon.mp3"

    "I decide to spend my afternoon at the library, listening to Nodoka rant on and on about poets and playwrights who have been dead for very long amounts of time."
    "But despite my apparent days of loving things like this being long in the past, I don't ever find myself getting bored."
    "She speaks in a way that manages to captivate a side of me that has long since passed, and I can't help but internally thank her for being able to do that."
    "I'd love to thank her on an actual person-to-person basis, but thanking people is tiring. Especially when you can't fully understand what you're thanking them for."
    "What I mean to say is that I manage to enjoy my time in a sun-soaked wooden room with a girl who smells like fresh coffee."
    "I lose myself in the moment and close my eyes."

    scene black
    with dissolve

    "I think Nodoka closes hers as well, since our conversation abruptly halts and we spend the next ten minutes sitting in silence."
    "I can only remain this despondent for so long, however, so I decide to reclaim my consciousness and head out after saying goodbye."
    "She says goodbye as well."
    "Right before diving headfirst into more words from someone who can no longer speak."

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka's affection has increased to [nodoka_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label nodokalibrary1:
    scene nodokafirstlib1
    with fade
    play music "morningmoon.mp3"

    "I make my way to the library a bit later than I normally do and am immediately greeted by a rare sight."
    "Sleeping on the job, Futaba? Really?"
    "What if someone needs a book?"
    "The world will spiral into chaos if you’re not there to check library cards and type names into your outdated computer."
    "I take my phone out of my pocket and begin to file a formal complaint to the[school] when I hear a familiar voice call out to me."

    no "Beautiful, isn’t she?..."

    scene nodokafirstlib2
    with fade

    no "A wild Fukuyama, at rest in her natural habitat...entirely unaware that she is being studied by two of the most practiced researchers in all of Kumon-mi."
    s "Indeed. Let us watch her closely and use this opportunity to educate future generations about her mannerisms and...tendencies or something."
    s "I don’t know. Just throw some smart person lingo into the mix and assume I said that."

    if bonus == True:
        no "Educate future generations? Sensei, are you forgetting that we are here on a mission to discover the mating process of the wild Fukuyama?"
        s "Uhh, yes. I was definitely forgetting that."

        scene nodokafirstlib3
        with dissolve

        no "Look at you, slacking off on our first day in the wilderness. Can you not tell when a creature is in heat simply by looking at them?"
        s "She just looks tired to me. But I’ll keep that in mind for when she wakes up. Have your camera ready."
        no "My camera is always ready, good sir. "
        no "In fact, why bother waiting at all? The Fukuyama is known for its love of copulating with fully-grown human males."
        s "Is there...a secret side of Futaba that I am unaware of?"
        no "Does the thought of her stripping down to her birthday suit and prancing around Kumon-mi in search of the ultimate satisfaction disturb you?"
        s "Yes."
    else:
        no "Just look at the way she breathes. Using both of her lungs. How majestic."
        s "You know, some of the things you say really disturb me sometimes."
        no "I'm going to wear someone else's skin one day."
        s "This is exactly what I'm talking about."

    scene nodokafirstlib4
    with dissolve

    no "Hmm...Yes. Yes, that disturbs me as well."
    no "Return to the Jeep and grab the net. We shall capture this one and keep it as our personal specimen. "
    no "Everyone wins."
    s "I just came from the Jeep and...I’m sorry to say, but it appears that we’ve forgotten our net, Nodoka."
    no "Well that’s no good at all. Without a net, we won’t be able to move into the second phase of any of our seven different strategies, Sensei. That net was extremely important."
    no "Luckily, the Fukuyama is a predictable creature and can be found in this exact location every single weekend."
    no "So I suppose more opportunities will arise as long as we remain vigilant."

    scene nodokafirstlib5
    with dissolve

    no "Now, what would you like to discuss with our daily quota of research out of the way?"
    s "Anything, really. "
    s "I remember you mentioning that you’ll be spending some time here from now on, so...here I am, I guess."
    no "Did you miss me?"
    s "So much that I took up a job as a wildlife researcher just to get closer to you."
    no "But you are my teacher...and I am your student. Think of how immoral this is, Sensei."

    if bonus == True:
        no "Nevermind how primally satisfying it would be to pin me down and take me on the desk of the teacher’s lounge."
        s "The teacher’s lounge actually doesn’t have any desks. It’s just couches."
        no "How unfortunate. I’ve always wanted to be taken on a[school] desk."
        s "If only we knew where to find any of those..."
    else:
        s "You are right. I apologize if it appeared that I was insinuating anything unsavory."
        s "If only we could forget all of that and remain good buddies for the rest of eternity."

    scene nodokafirstlib6
    with dissolve

    no "Yes...if only."

    "Nodoka places her book down on the desk and I try to sneak a peek at whatever it is she’s been reading."

    if bonus == True:
        "I stop caring when I realize it isn’t anything pornographic. But I guess the chances are that she pulled whatever it was from one of the bookshelves here and..."
        "Well, I don’t think this[school] carries much porn."
        "I wonder if there is anything I can do that could change that?"
    else:
        "All of the pages are blank, though, and I quickly go back to thinking she's a big ole weirdo."

    no "Are you thinking what I’m thinking, Sensei?"

    if bonus == True:
        s "You know, I really wouldn’t be surprised if I was."
    else:
        s "I highly doubt it."

    scene nodokafirstlib7
    with dissolve

    no "Excellent. Then let us pick up where we left off before you ran away without saying goodbye the other night."

    "Oh. I guess we weren’t thinking the same thing after all."

    no "I believe I owe you an apology for making you feel uncomfortable. "
    no "I got a little ahead of myself."

    if bonus == True:
        no "I’d like to say it won’t happen again, but saying that would make me a liar. And you seem to be the type to value honesty."
        no "When it’s given to you, I mean. Not when you need to dish it out to others."
        s "That is surprisingly perceptive."
        s "But yes, there’s not really any point in lying to me. "
        no "But there {i}was{/i} a point in lying to me about your...pure intentions. Was there not?"
        no "Why do you think I began to grill you so vigorously about the things you wanted to do to me within earshot of the others?"
        s "Because you’re weird and horny?"
    else:
        no "I just forgot how important top 8's are to some people."
        s "Just stop being such a weenie and it won't be a problem."

    scene nodokafirstlib8
    with dissolve

    no "Wrong!"

    if bonus == True:
        no "I’m weird and horny {i}and{/i} a good girl who just wants to protect all of her companions."
        s "Do you really think I’m leading any of them on or something?"
    else:
        no "Being a weenie is fun. I will be a weenie forever."
        s "Besides, I don't think any of the girls think I would omit them from my top 8."

    scene nodokafirstlib9
    with dissolve

    no "I {i}think{/i} that a particular creature the two of us were sent here to study thinks that. And so I, too, must think that by association."
    s "..."

    if futabalust10 == True:
        "Futaba did mention thinking something was going on between Chika and me at the Christmas party but...I’m pretty sure she’s not equating it to me leading her on, is she?"
        "She just realizes that there are a lot of people who happen to be into me the same way she is."
        "And she didn’t even seem that opposed to it when she told me..."

    else:
        "Would Futaba really think something like that?..."

        if bonus == True:
            "I mean, it would probably make sense if she did given how quickly things progressed between the two of us. "
            "She’s a smart girl...so I get why she would feel that way."
            "But to think those feelings were so apparent that even Nodoka would pick up on them..."

    no "You’re manipulating Futaba, aren’t you?"
    s "It’s a little confusing seeing you ask that question with a smirk on your face."
    no "Apologies. I have a natural smirk. I’m actually very upset with you if that’s what you're doing."
    no "I’m not telling you to drop everything you’re doing and devote yourself to her. She’s mine of course."
    no "But she should at least know that she isn’t the only one you’re seeing."

    if futabalust10 == True:
        if bonus == True:
            s "I think she already {i}does{/i} know that, to tell you the truth."
            s "She voiced her concerns about how one of the girls was acting around me during our Christmas party."
            no "Which one? The tiny, black haired one in the back of the classroom?"
            s "...Sana?"
            s "Why would you assume I was talking about Sana?"
            no "Because that would be the most exciting answer, obviously. "
            no "I mean, think about the size difference."
            s "That’s definitely not the person Futaba was talking about."
            s "But the point is that she’s perceptive enough to...understand the situation at hand here."
            no "So then why get mad at {i}me{/i} for asking what that situation was? "
            no "All you had to do was come out and say, “I’m here to have sex with Nodoka and everyone else and there’s nothing anyone can do to stop me.”"
        else:
            s "I can hug whoever I want and you will never stop me."
            no "Then you need to come out and admit you are a huggy boy so we can all stop pretending you aren't."

    else:
        if bonus == True:
            s "Why does she need to know that?"
            no "Because she deals with enough bullshit from people commenting on her weight and demeanor."
            no "I don’t want her to be slowly crushed by assuming the man she’s yearning for is only using her for her supple, youthful body."
            s "Not to turn the tables or anything, but why flirt with me so openly if you’re worried about her being hurt?"
            no "Obviously because {i}I’m{/i} in heat as well. "
            no "And when push comes to shove and I am forced to choose, I will obviously take care of myself before anyone else."
            no "But that doesn’t mean I will simply abandon her in the springtime of her youth."
            no "This could have all been solved so easily by simply coming out and saying, “I’m here to have sex with Nodoka and everyone else and there’s nothing anyone can do to stop me.” the other night."
        else:
            s "I can hug whoever I want and you will never stop me."
            no "Then you need to come out and admit you are a huggy boy so we can all stop pretending you aren't."

    s "Yeah, that’s definitely not something that I think I’m ready to say yet."
    no "It’s true, though. Isn’t it?"
    s "Nodoka, as someone who appreciates girls as much as I do, I’m sure you understand."
    no "Absolutely. There is not a body in that classroom that I don’t want all up in my business."

    if bonus == True:
        no "But I’m not pushing all of them into different rooms and asking that they keep their schedules open while I take turns individually dishing out orgasms."
    else:
        no "But, unlike you, everyone already knows I am a huggy boy."

    s "Nodoka-"

    scene nodokafirstlib10
    with dissolve

    no "I’m not going to say anything. "
    no "Frankly, I only care about two people out of seventeen right now after excluding myself from the count."
    s "Two? Weren’t you starting to get close to Rin, though?"
    no "Her company is fun and she is a nice girl. But that doesn’t mean I care enough about her to prioritize her in any way."
    no "I make people work to get on my good side. That way, they’re less inclined to abandon me and leave me with nothing."
    s "I feel like {i}I{/i} didn’t have to work very hard to get on your good side."

    scene nodokafirstlib11
    with dissolve

    no "You think you’re on my good side?"
    s "I do."
    no "What gives you that idea?"
    s "The fact that you’re slowly but surely showing me some cracks in your armor."
    no "Cracks are just cracks, Sensei. They’re not really weak points until you bash or stab them a few more times."

    if bonus == True:
        no "If you really want to get my armor off, all you need to do is save up enough Nodoka points."
        no "Unfortunately, you missed out on a large sum of them by not eating my pizza the other night."
        s "I’m pretty sure it wasn’t, but I’m going to interpret “eating my pizza” as a euphemism. "
        no "Do it. That makes the idea of the four girls who remained upstairs eating pizza all night significantly more exciting."
    else:
        no "Also, you missed out on a fuckin' good ass pizza the other night."
        s "Ugh I knew it."

    scene nodokafirstlib12
    with dissolve

    no "And say goodbye for real next time. Making me have to wait to apologize was a real cliffhanger."
    s "I figured someone as well-read as you would {i}like{/i} cliffhangers."
    no "Not when they involve me."

    scene nodokafirstlib13
    with dissolve

    no "Which is why I’m taking countermeasures to prevent that from ever happening again."
    s "Countermeasures? What are you talking about?"

    scene nodokafirstlib14
    with dissolve

    no "Take down my number and let me bother you whenever I want to procrastinate or apologize for more things I’m going to do in the future."
    s "Just how difficult are you planning on making my life?"

    if bonus == True:
        no "As difficult as I can make it without entering into a formal relationship with you."
        s "Wow. Are you rejecting me before I’ve even asked you out?"
        no "A - You will never ask me out without some serious character development on your end."
        no "B - I have to keep myself open for when Futaba becomes a lesbian."
        no "It’s unfair that you get to play with her breasts recreationally and I have to do it by force."
        s "I want to say you should probably stop doing that, but I enjoy the mental image of it, so feel free to continue."
        no "I will do just that."
        no "Oh, and Sensei?"
        s "Hm? "
        no "You {i}are{/i} on my good side."
        no "My distaste for cliffhangers compelled me to let you know that before you wander off to flirt with someone else."
        s "Funny story, I’m about to do that right now."
        s "I’ll be thinking of you the entire way there, though."
        no "And I’ll be watching you very closely as you walk away. "
        no "You have an excellent figure for someone your age. "
        s "I’m not even that old..."
    else:
        no "On a scale of one to ten? Probably like an eight."

    scene black
    with dissolve2

    "I quickly exchange numbers with Nodoka and slide my phone back into my pocket."

    if bonus == True:
        "As I leave the library, I feel the looming gaze of a perverted, semi-sociopath on my back."
        "Just seconds after turning the corner, a noise leaks out of my pocket and the relationship I have with Nodoka grows even stranger."

        play sound "phonebeep.wav"

        "{i}Nodoka has sent you a picture message!{/i}"

    $ renpy.end_replay()
    $ nodokanumber = True
    $ nodoka_love += 1
    $ nodokalibrary1 = True
    stop music fadeout 5.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label nodokalibrary5:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    play music "justlights.mp3"

    "{i}A fool sees not the same tree that a wise man sees.{/i}"
    "{i}He whose face gives no light, shall never become a star.{/i}"
    "{i}Eternity is in love with the productions of time.{/i}"
    "{i}The busy bee has no time for sorrow.{/i}"
    "{i}The hours of folly are measured by the clock, but of wisdom: no clock can measure.{/i}"
    "{i}- William Blake (1757 - Whenever he died)"
    "Some people have danced with tragedy while others do not know how to dance at all."
    "And somewhere between those two dancers, there is a place that resembles ours."
    "You likely won’t ever see it."
    "But some have."
    "And you likely won’t ever see them either."
    "Because their world faces a different direction than ours."
    "I hope you’re happy, wherever you are."
    "........."
    "......"
    "..."

    scene nodokasecondlib1
    with dissolve

    no "Good afternoon, Sensei. "
    no "Your timing is quite good today. I was just starting to get bored."
    s "Well you certainly look relaxed, if not anything else."
    no "This library has no couch, so I needed to create my own out of a metal chair and an annoyingly elevated desk."
    no "I give it a 5/10 for comfort and 7/10 for accessibility."
    s "Is this how bored you are? Resorting to rating the objects of the library?"
    no "Do you want to know {i}your{/i} rating?"
    s "I don't. I’m pretty sure it would make me self-conscious if it was low."
    no "Does my opinion matter that much to you?"
    s "It doesn’t...{i}not{/i} matter?"
    no "Interesting."
    no "So, how should the two of us kill time today without Futaba around to stare at?"
    s "We could just stare at each other, I guess."
    no "Or, alternatively, we could leave this place altogether and find something else to do."
    s "Are you allowed to leave right now? I thought you were taking over for Futaba?"
    no "Yes. I’m taking over for her volunteer position in a[school] library over the weekend, when barely anyone visits."
    no "I think I can get away with leaving a little early if I have prior engagements."
    s "It’s not really a prior engagement if we make it right now."
    no "No, but the books don’t know that."
    s "The books don’t know anything. They are books."

    scene nodokasecondlib2
    with dissolve

    no "Did you hear that, Hamlet? Sensei thinks you’re worthless."
    no "He bites his thumb at you."
    s "Hey. That line isn’t even from Hamlet."

    scene nodokasecondlib3
    with dissolve

    no "It’s not. But the phrase carries the same meaning and was completely comprehensible in context, correct?"
    s "Do you quarrel, Nodoka?"
    no "Quarrel, sir? No sir."
    s "..."
    no "..."
    s "As much as I'd like to continue, I don’t really remember anything else from that play. "
    no "That’s fine. I’m not much of an actor anyway."
    no "I don’t even really like plays. I’m just reading this because it was the first thing I picked up."
    no "This[school] is fine, but the library is small and its selection is entirely generic."
    no "My heart aches for all of those poor books stuck in that sink hole."
    no "Oh, here’s an idea. How would you like to venture to the ruins of my old[school] and throw yourself into an abyss?"
    s "I would not like to do that at all. It sounds horrible and dangerous."
    no "Then tie a rope around me and lower me down so I can at least pick up a few things I haven’t already read."

    if bonus == True:
        s "If I ever tie a rope around you, it will be for significantly less wholesome reasons."
    else:
        s "If I ever tie a rope around you, it will be because we are bungee jumping."

    scene nodokasecondlib4
    with dissolve

    if bonus == True:
        no "Bondage fan?"
        s "Not really, but pretty much everyone is fine with bondage if it’s just rope."
        s "I think."
        s "I don’t really know, actually."
        no "Handcuffs?"
        s "Sure. I know where to buy some, too."
        s "I’m pretty sure I wouldn’t be allowed to actually purchase them, though."
        no "Did you somehow manage to get yourself banned from a sex shop, Sensei? That’s so depressing."
        s "No. I just...know someone who works there."
        no "Someone I can meet?"
        s "Someone you’ve already met."
    else:
        no "I have always wanted to try that."
        s "Unfortunately, I already have a partner."

    no "Is it the tiny girl with the black hair who sits in the back of the classroom?"

    if bonus == True:
        s "Are you just {i}always{/i} going to guess Sana whenever I mention anything remotely sexual involving literally anyone?"
        no "I’m telling you, Sensei. She’s a freak. I can feel it."
    else:
        s "I do not know why you would assume that, but no. It is not Sana."
        no "She seems like she'd be a good bungee jumper."

    if sarasex == True:
        "Well she...definitely would not be the only one in her family like that."

        if bonus == False:
            "Sara loves bungee jumping."

    s "I...don’t think that’s true. But if that’s what you want to think, feel free."
    no "Speaking of “things that I think,” I’d like to reiterate and reintroduce the idea of us getting out of here."
    no "I haven’t seen a non-Sensei soul in hours. There is absolutely no downside to the two of us going on a little adventure."

    if bonus == True:
        s "An adventure to where? I’m fine with going out to lunch or something, but if you’re trying to drag me into a janitor’s closet..."
        s "Well, that’s even better."

        scene nodokasecondlib5
        with dissolve

        no "Hmm...no. Flirting is fun but I think we should limit things to just extremely suggestive talking for now."
        no "Just think of how great the payoff will be if we build up the tension a little more."
        s "And you were accusing {i}me{/i} of leading people on."

        scene nodokasecondlib6
        with dissolve

        no "Here, take a Nodoka point. Does that make you feel any better?"
        s "Just one? I thought they only came in multiples of fives?"
        no "They come in whatever amount I want them to come in. I’m in charge, remember?"
        s "That’s one hell of a double standard, Nodoka."
        no "I’m one hell of a girl, Sensei."
    else:
        s "I agree. It's really stuffy in here anyway and I need to keep my legs stretched for my potato sack race later."

    scene black
    with dissolve2

    "Nodoka grips her skirt as she moves her legs off of the desk and prevents me from being able to look up it because she is evil."
    "She puts Hamlet back on his shelf before the poison ever finds its way into his veins and he proceeds to live a long and happy life with Ophelia."
    "Until someone else decides to open the book, that is."
    "I can’t help but wonder how many other things there are in this world that are better left unfinished or unopened as we make our way out of the library and into the halls of the[school]."

    scene nodokasecondlib7
    with dissolve

    no "It feels like just the other day we were walking on the bridge like this."
    s "That kind of {i}was{/i} just the other day, though."
    no "I suppose that’s true."
    no "Has your opinion of me changed at all within that time frame?"
    s "I’m a little more worried about you as a person than I was back then."
    no "Worried? Why?"
    s "Well, maybe “worried” isn’t the right word. But I’m starting to think you’re capable of doing a lot more than you actually...want to do? Does that make sense?"
    no "Not really, no."
    s "Then let me try explaining it like this-"
    s "I think there are two Nodokas."

    if bonus == True:
        no "That would make an exciting threesome."
        s "It would, yes."
        s "But what I was getting at is that one of those Nodokas wants to be suggestive and flirty all day..."
        s "While the other one cares more about “tension” and...seemingly wants me to create the world’s largest consensual harem."
        no "You’re forgetting about the Nodoka who wants you all to herself."
        no "And the Nodoka who doesn’t want you at all."
    else:
        no "Oh god. Did they escape?"
        s "Wait, is there more than two?"
        no "More than I can even count."

    no "So many Nodokas, so little time."
    s "Which one is real, though?"
    no "All of them? None of them? Who knows?"
    s "I would imagine you do."

    scene nodokasecondlib8
    with dissolve

    no "Nope."
    no "I don’t really care to find out either."
    no "I just want to make memories while I still can."
    no "Good memories, bad memories, sad memories, passionate memories."
    no "Memories of anything and everything."
    no "If I feel every feeling the world has to offer, I’ll have an unlimited library of experiences to pull from and be inspired by."

    if bonus == True:
        no "And I’m not just talking about sexual stuff right now either."
        s "I...didn’t think you were."
        no "Okay, good."
        no "I did have a sex dream about you last night, though, just for the record."
        s "Wait, what?"

    scene nodokasecondlib9
    with dissolve

    no "The point is, you can’t figure out which Nodoka is the “real” Nodoka because she is all of those things."
    no "She’s just a girl. Not some genius or prodigy or anything like that."
    s "Don’t you have the highest test scores in all of Kumon-mi?"
    no "..."

    scene nodokasecondlib10
    with dissolve

    no "Okay, so maybe I {i}am{/i} a genius. But anyone can be a genius if they spend their entire life just...living other lives via literature."
    no "I said before that I’m not an actor, but one of the things I enjoy most of all is imagining how I would feel as someone else...Someone who isn't real."
    no "Or what I would do in their shoes, if only I could fit into them."

    if bonus == True:
        no "And yes, the answer to that question is typically declothing every female character and strapping them to sex machines-"
    else:
        no "Unfortunately, I have an invisible third foot and need to buy a very specific, special pair of shoes or I won't be able to walk at all."

    s "What?"

    scene nodokasecondlib11
    with dissolve

    if bonus == True:
        no "And yes, sometimes I must hook {i}myself{/i} up to those sex machines to truly understand what it means to feel-"
        s "{i}What?{/i}"
    else:
        no "I said that I have an invisible third foot and need to buy a very specific, special pair of shoes or I won't be able to walk at all."
        s "Oh, okay. I misheard you."

    scene nodokasecondlib12
    with dissolve

    no "But the second I close the book, I’m just Nodoka again."
    no "And everything turns gray."
    no "And I have to go out and find new colors to fill everything back in."
    no "Life would have been easier if I wasn’t printed as a picture book."
    s "..."
    no "..."
    no "The main reason so many people fall in love with fiction is because they’re searching for something they can’t obtain on their own."
    no "But there are also people who fall in love with it simply because there isn’t anything else to do."
    no "People who get so bored of not being able to feel anything that they allow themselves to fall into those who can."
    no "I kind of hate reading, actually."
    no "It’s time consuming...you can’t do it in the dark...and the memories you get out of it can barely be called memories at all since they aren’t your own."
    no "But the things I love about it always manage to outweigh those somehow."
    no "Even when I wish they wouldn’t."
    s "You don’t sound like a picture book at all, Nodoka."

    scene nodokasecondlib13
    with dissolve

    no "Huh?"
    s "You’re more like a...and forgive me in advance if this sounds childish-"
    s "But you’re more like a coloring book."
    s "A really advanced one with a lot of difficult drawings that...requires special attention and weird colors like chartreuse and mauve."
    s "And you’re just waiting to be filled in."
    no "..."

    scene nodokasecondlib14
    with dissolve2

    no "Oh..."
    no "It’s back."
    s "Hm? What is?"
    no "The color."
    no "It’s been gone for days."
    s "..."
    no "And there’s no chartreuse or mauve anywhere to be found..."

    scene nodokasecondlib15
    with dissolve

    no "Looks like you were wrong, Sensei."
    s "You just haven’t gotten to the page with all of the weird colors yet. You’re only in the beginning of the book."
    no "So the hardest is yet to come?"
    s "That depends. You’re not battling any really intense trauma or something, are you?"
    no "Is that really something you’re supposed to be asking someone?"
    s "Supposed to? No. Probably not."
    s "But I think we’re already at the level where we can start sharing things like that with one another."

    scene nodokasecondlib16
    with dissolve

    no "Hmm...I suppose we are."
    no "We’re out of the library now, but I think I’m going to carry on with my newfound hobby of rating things and give my personal trauma a solid 5/10."
    no "Nothing unmanageable, but nothing overwhelmingly tragic like witnessing a friend jump to her death or being mauled by a rhino."
    s "What kind of world do you live in where “being mauled by a rhino” is the second thing that comes to mind when measuring trauma?"
    no "One that’s sure to get a lot more colorful from this point on."

    scene nodokasecondlib17
    with dissolve

    no "Or not."
    no "For all we know, the two of us could grow to hate each other over something small like...taking the last piece of garlic bread."
    s "To prevent that hate from ever spawning, I hereby give you permanent permission to finish off any and all bread that we eat together in the future."
    no "Are you sure? Cause I really like bread and eating more of it all the time will make me fat."

    if bonus == True:
        no "I won’t be able to fit into the janitor’s closet anymore."
        s "We can just find a bigger closet, then."
        s "I’m not worried."
    else:
        s "You know, maybe we should just go on a diet instead."

    if bonus == True:
        scene nodokasecondlib18
        with dissolve

        no "Neither am I."
        no "If music be the food of love, play on."
        no "Here’s to the rest of our time together...which is sure to be full of confusion, misunderstandings, and handjobs in the locker room."
        s "I’ve never seen someone say “handjobs” with such a hopeful look on their face before."
        no "Then let us take this moment and lock it away in our collage of colors as just one of many memories the two of us will make together."
        no "Hooray for sinkholes."
        s "..."
        s "Yeah."
        s "Hooray for sinkholes."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ nodoka_love += 3
    $ nodokalibrary5 = True
    stop music fadeout 10.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label nodokadorm15:
    play sound "knock.mp3"

    "I knock on Nodoka’s door and wait for-"

    play sound "glass.mp3"
    with hpunch

    no "FUCK!!!!!!!"

    "You know what? Maybe I should just come back tomorrow."
    "Nodoka isn’t exactly easy to deal with when she’s screaming and knocking things over, and I’ve already had to deal with Yasu at her...Yasu-est recently."

    play sound "glass.mp3"
    with hpunch

    no "AAAAAAAAAAAHHHHHH!!!!"
    s "..."

    "But...then again..."
    "The last time I saw Nodoka in her manic state, she was also without pants. And that is a thing I can both respect and appreciate."
    "Also, I’d feel less bad about her having a spontaneous orgasm on top of me because at least I know she would understand it."
    "So...fuck it."
    "I’m going in."
    "But if I don’t make it out, know that I died in pursuit of something admirable."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene nodokacrazy1
    with dissolve2

    no "AAAAAAAAAAAAAAHHHHHHHHH!!!"
    s "Hey, Nodoka. Nice to see you’re doing well today."

    play sound "glass.mp3"
    scene nodokacrazy2
    with hpunch

    no "I had it again! The same dream!"
    s "What dream?"

    scene nodokacrazy3
    with dissolve

    no "The girl! The one with the eyes! The one with the eyes and the hair!"
    no "She was so fucking hot. But who was she? And why? What is the relevance, Sensei? Why does she so often appear to me without saying a single FUCKING thing?!"
    no "What does she know?! What does she know and why will she not tell me?! "
    no "Is she the same one from the writings on the wall?! The same one who plagues the memories that precede my own?!"
    no "I need to fucking know!"
    s "I mean...do recurring dreams always {i}have{/i} to mean something?"

    scene nodokacrazy4
    with dissolve

    no "Fuck you! "
    s "Please don’t throw anything at me. Especially things that you just...generate out of thin air?"

    scene nodokacrazy5
    with dissolve

    no "The air is not thin. It’s heavy. Heavy with the stench of mystery. Mystery that I, Nodoka Nagasawa, A FUCKING GENIUS DETECTIVE, must uncover."
    no "Do you want any coffee? You look like you want coffee. "
    s "I’m fine, thanks. "
    no "Are you sure? It’s {i}really{/i} good. And if you stare into it beneath the ceiling lights, you can kind of see your reflection."
    no "Reflections carry hints, you know? Like shadows. Hints that we can use to discover the truth about all of this."
    no "What makes the world move? Is it the sun? Or is it the strings of a puppeteer pulling us toward a giant ball of hot fucking lava that will one day consume us all?"
    s "It’s-"
    no "Bzzzzzt. The answer is the sun. You’re a teacher. You should know this. But it would be really fucking cool if it was something else, right?"
    s "Uhh..."
    no "So anyway, reflections. Mirrors. Reflections in mirrors."
    no "If you were to hang yourself upside down and stare into one, would the you that you see be any different from the you that you don’t? Or are you the same in both directions?"

    play sound "glass.mp3"
    scene nodokacrazy6
    with hpunch

    no "Oh! You know what we should do? We should find a mirror. We should find a mirror and go inside of it. We should see what’s inside of it."
    no "It’s technically possible if we pause reality when all of its atoms are aligned. I can probably time it if you have the supernatural ability to stop time."
    no "Is that something you have? That’s something I think you have."
    s "Me? No. But there’s a girl on the first floor who-"
    no "Good! Go get her. Fetch the girl. Bring her here and make her stop time so that I may spend the rest of it searching for the one that I am after."
    s "It doesn’t really work that way. Also, if you spend your days chasing after someone you saw in a dream, chances are you’re going to die alone and unfulfilled."

    scene nodokacrazy7
    with dissolve

    no "That’s why I asked you to stop time, you fucking nuisance! Are you even listening to me?! "

    "So, it’s good that Nodoka’s pants are off. Don’t get me wrong. "
    "But it would be much better if her pants were off {i}and{/i} she was being nice to me- which is very much not the case so far."

    no "Stop thinking to yourself! Share your thoughts with me! "
    s "I was just thinking that I’m glad your pants are off, but that I wish you were nicer to me."

    scene nodokacrazy8
    with dissolve

    no "I can be nice. Nice is not a problem for me."

    scene nodokacrazy9
    with hpunch

    no "Or at least it wouldn’t be if you’d fucking HELP me already! "
    s "With {i}what?{/i} I can barely figure out what you’re even talking about."
    no "Adventure!"
    s "What? "
    no "We have to go on an adventure! We have to uncover the thing in the thing! The one I need for the thing!"
    s "What thing? "
    no "The fucking {i}thing,{/i} Sensei! Do you need me to spell it out for you?!"
    no "Thing! T-H-I-N-G! Thing!"
    no "Come! Now! To the outside world! A large wooden structure awaits us!"
    s "Are you at least going to put on pants first?"
    no "Pants are for the weak! I think better without them! If anything, you should also remove your pants!"
    no "We should go on a pantsless adventure and fuck inside of a mirror!"
    no "If you can figure out how to get in, I’ll let you into {i}me!{/i} I’m serious! It would be a fair trade! A tight fit, sure! But I can handle the pain if it means bringing me one step closer to the other side!"
    s "Nodoka-"
    no "Adventure! Penis! Mirror! Eyes! Now!"
    s "I’m good. You can go without me. I don’t really want to risk being seen out in public with a bottomless teenager who looks like she’s on drugs."

    play sound "static.mp3"
    scene nodokacrazy10
    with flash
    stop sound

    no "You will come and you will like it! I need extra fingers to help me dig! And you have the largest fingers out of anyone I know!"
    s "Uhh...thank you?"
    no "So good for digging! Digging to find what’s buried beneath our feet! "
    no "It is there! I can hear it! I can feel it! It flops around like a fish! A fish with hooks for eyes! A hook with a fish for a mouth!"
    no "Let’s find the fish, Sensei! Let’s catch it and cook it! I’m a detective! I know what I’m talking about!"
    s "Just to confirm, you aren’t {i}actually{/i} on drugs, are you? Because I’m beginning to feel a little skeptical."
    no "No drugs for me! Just thoughts I am infected with! The thoughts of someone else! A second me! One we must collect and dissect!"
    no "Turn around! Face the door! Open it! And walk in a direction you seldom walk in! This is how we find it! This is how we uncover the truth!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "You know, all of that time I’ve spent with Yasu recently is beginning to feel pretty normal by comparison. "
    "It may be {i}consistently{/i} more odd being around her, sure...but the thing with Nodoka is that when she’s off, {i}she is off.{/i}"
    "And as she forces me out of her bedroom by pushing against my back with all of her strength, I can’t help but wonder if she is acting on behalf of some sort of higher power as well."
    "I doubt she is, for she seems far too logical to involve herself with such matters."
    "But whatever is causing this must be far more than the shifting of chemicals inside of her brain."
    "Whatever is causing this worries me."
    "........."
    "......"
    "...."

    scene nodokacrazy11
    with dissolve2
    play music "contemplation.mp3"

    no "..."
    s "..."
    no "Where the fuck are we?"
    s "How should I know? It took all I had to even keep up with you as you stormed your way over here."
    s "I kind of just assumed you know where you were going."
    no "I see. I see, I see, I see, I see."
    no "Then it must be a clue. There must be a reason I came here. There must be a reason I don’t know where I am. And there must be a reason you are here with me."
    s "I’m just here to prevent anything from happening to you as you are a teenage girl wandering around in the middle of the night in her underwear."
    no "Stop fucking lying to me. I know you’re just waiting for me to fall asleep so you can take them for yourself. Is that it? You want my underwear? "
    no "Or do you truly want to help me with my mission?"
    s "And...what’s your mission again? Something about digging?"

    scene nodokacrazy12
    with dissolve

    no "More than just digging! Digging is just one of several means of accomplishing it!"
    no "There is something! I feel it! I must find it! I must snatch up the answers with my own two hands! Wash the dirt off! Return it to the one who needs it most!"
    s "Wait, you’re doing this {i}for{/i} someone? "

    scene nodokacrazy13
    with dissolve

    no "There! That is where we’re meant to go! I remember now! I remember why I came here!"
    no "Follow me to see it all! Such beautiful things! Too beautiful for people like us! Disgusting people! "
    no "People who only live to hurt others! To make memories and pack them away like tools in a box!"
    no "We must dig! We must dig as if our lives depend on it!"

    scene nodokacrazy14
    with dissolve

    no "Dig! Dig dig dig!"

    "Nodoka storms off, but her voice remains all around me as it echoes throughout an old and unfamiliar school yard."
    "Her shirt gets caught on a bush that she decides to walk {i}through{/i} instead of around."
    "I don’t worry about whether or not there were any thorns that may have cut her exposed legs open."
    "I just think about how fortunate I would be if they were to tear her shirt instead and force her into an even greater state of defenselessness. "

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nodokacrazy15
    with dissolve

    no "X! X marks the spot! But this is the spot and there is no X! Just the shadow of a slanted lower case T!"
    no "I will dig anyway! Dig all night! Dig until I can fuck myself with the exposed bones of my fingers rather than the fleshy bits that surround them!"
    no "Why are you not helping?! We have a job to do!"
    s "Oh...you know. Just...observing the scenery."

    scene nodokacrazy16
    with dissolve

    no "The scenery will get you nowhere! "
    no "Why does no one take this seriously but me?! Why am I the one who must endure the brunt of this world’s weight when all I want is to READ!"
    no "There are so many books! So many books and yet I have read them all! We need more books! We need more groceries! Plates of gray food and lavender hair! "
    no "Triangle! Circle! Triangle!"

    "Okay, so Nodoka is officially broken. But at least she is broken in a position that I have imagined her in several times in the past."
    "I kind of always figured I’d be behind her in a different way once her back arched, though."
    "I can’t say many of my sexual fantasies involve a girl filling the space between her fingers and her nails with dirt."
    "I also can’t say that I have any idea how to deal with this. So, at the risk of Nodoka {i}actually{/i} digging until there is no skin left on her fingers, I should probably call on someone for help."
    "Someone who may or may not have experience dealing with this girl in her manic state. And someone not named Otoha since she normally just bails."

    scene nodokacrazy17
    with fade
    play sound "phonebeep.wav"

    "Thankfully, I know someone just like that. And it’s someone I should have invited along from the get go."
    "And while she may not have lavender hair, the perfume she wears will compensate for it. "

    play sound "phonebeep.wav"

    f "{i}Hello?{/i}"
    s "Hey. What are you doing right now?"
    f "{i}Sensei? You’re calling later than normal today.{/i}"
    f "{i}I’m not really doing anything. Is something wrong? Or did you just miss the sound of my-{/i}"
    s "I need your help, actually."
    f "{i}Oh.{/i}"
    f "{i}Umm...{/i}"
    f "{i}Like...THAT kind of help?...{/i}"
    s "What? No. Well, yes. But that can wait until later. "
    s "What I need help with right now is Nodoka."
    f "{i}Nodoka? Is she in...bad condition again or something?{/i}"

    scene nodokacrazy18
    with fade

    s "Well...I guess that really depends on what you mean by “bad condition.”"
    s "Because she {i}looks{/i} pretty fine to me."
    f "{i}Sensei...what I’m asking is if she’s all...“hyperactive” again. I know that sort of thing can happen with her sometimes.{/i}"
    s "Well, she is currently digging a hole in the middle of a random schoolyard. So I’ll let you figure out if that’s bad enough condition or not."
    f "{i}Random schoolyard? Where are you two, exactly?{/i}"
    s "I have no clue. I just followed her here. But if you’d like to switch shifts or come here and help me, I’d be totally fine with that."
    f "{i}Yeah...I’ll head over right away. Can you share your location with me? There should be a button you can press to-{/i}"
    s "I know how to share my location, Futaba. I’m not {i}that{/i} old."
    s "Also, can you bring an extra pair of pants when you come here?"
    f "{i}Um...did something...happen to Nodoka’s pants?{/i}"
    s "It’s more like there were never any pants to begin with-"

    with hpunch

    no "FUCK!!!! WHY IS THE GROUND SO HARD?! WHY DOESN’T IT EVER RAIN?!"
    f "{i}Okay...you know what? I’m going to hang up and get over there as fast I can. Just don’t forget to send me your location, okay?{/i}"

    scene nodokacrazy17
    with fade

    s "Deal. Thanks, Futaba."
    f "{i}Of course. Please keep her safe until I get there. I’ll see you soon.{/i}"

    play sound "phonebeep.wav"
    scene nodokacrazy19
    with dissolve

    "I hang up the phone, send Futaba my location, and stare down at Nodoka- trying my best to avoid having my gaze linger on her ass for longer than it already has."
    "Unfortunately, I am physically incapable of willing myself to do this. So I watch as she waves it back and forth, throwing dirt behind her as she continues to dig."
    "Why am I not helping her, you ask? "
    "Because I don’t want to."
    "Because I’d rather observe."
    "It’s what Nodoka does best, so I think having her on the opposite side of things for once could be good for her."

    no "It’s close! So close! I can feel it! I can smell it! And all without your FUCKING help, you useless piece of meat!"
    s "Good job, Nodoka. Hard work pays off, doesn’t it?"
    no "What do you know about hard work?! What do you know when all you do is stand in the corner of the room and dream of the day when you can make a mountain of our bodies?!"
    s "My fantasies aside, Futaba is on her way over so the two of us can drag you back to the dorm."
    s "I’d likely be able to do it myself if I really wanted to. But, on the off chance anyone sees us, I should probably...not risk that."

    stop music

    q "Oh, don’t you worry about that. No one’s going to see you here."

    play sound "static.mp3"
    scene nodokacrazy20
    with flash
    stop sound
    play music "sidecharacter.mp3"

    q "Hi! "

    if sarasex == True:
        q "You're becoming a bit of a regular here, aren't you?"
        s "What? I’ve never even-"

    q "You’ve sure picked a strange place to take a half naked girl in the middle of the night, huh?"
    q "I get that “the mood” can strike at the most random of times, but somewhere private would probably make a little more sense, no?"
    s "...It’s not what it looks like."

    scene nodokacrazy21
    with dissolve

    q "My, my, my...what would happen to you if I were to report this to the police?"
    q "You know, if I took a picture of this right now, it’d be {i}pretty{/i} hard to weasel your way out of it down at the station, buddy."

    scene nodokacrazy22
    with dissolve

    q "Not to mention the state your companion is in. Chances are she wouldn’t even be able to-"

    scene nodokacrazy23
    with dissolve

    q "Oh."
    q "Uh-oh."
    s "Uh-oh? What do you mean, “uh-oh?”"
    q "Ooooooh, nothing..."
    q "Just the teensy little fact that your friend might have just run off since she isn’t there anymore."
    q "There’s a pretty neat hole, though. I wonder if she found anything cool?"

    "I turn around to find that Nodoka has, in fact, run off- which is doubly concerning because now Futaba is going to think {i}I{/i} let her get away when it was really all this girl’s fault for distracting me."

    scene nodokacrazy24
    with dissolve

    q "So, now what? You wanna hang out here for a little while longer? Maybe chat about the news and such?"
    s "No...I’m going to go look for the girl I just lost."
    q "Why? You’re not going to find her."
    s "She can’t have gone that far. It’s only been a minute."
    q "Sure. Maybe to {i}you{/i} it’s only been a minute. But who’s to say that time moves the same way here as everywhere else?"
    q "For all you know, these could be sacred grounds detached from the construct of time that we let ourselves be gagged and bound by."
    s "Or...it has only been a minute."

    scene nodokacrazy25
    with dissolve

    q "Okaaaaaay. But don’t tell me I didn’t warn you thirty seconds from now when you realize that everything you {i}thought{/i} you knew is wrong."
    s "That-"

    play sound "phonering.mp3"
    scene nodokacrazy26
    with hpunch

    "My phone begins to ring and I look down to see that it’s Futaba calling."
    "And while the most ideal scenario would be that she bumped into Nodoka on the way home and is now escorting her back...I highly doubt that’s going to be the case."

    q "Go on. Answer it and see how right I am and how wrong you are."
    s "..."

    play sound "phonebeep.wav"

    s "Hello?"
    f "{i}Sensei?...Are you sure the location you sent me is correct?{/i}"
    s "You mean...the one I sent you like two minutes ago?"
    f "{i}Uhh...it's...been a lot longer than that...{/i}"
    f "{i}But are you sure it's right? Have you maybe...moved at all?{i}"
    s "No. I haven't moved and I sent you my exact coordinates. Why do you ask?"
    f "{i}Well...it’s just that...{/i}"
    f "{i}I...uhh...{/i}"
    f "{i}I can’t exactly...go where you are right now...{/i}"
    s "What? Why?"
    f "{i}Because...{/i}"
    f "{i}Well...{/i}"
    f "{i}It’s outside the barrier...{/i}"
    s "..."
    f "..."

    play sound "phonebeep.wav"

    "I hang up the phone and slide it back into my pocket, trying to come to terms with whatever that must mean."

    scene nodokacrazy27
    with dissolve

    q "See what I mean? Bet you think I’m pretty neat now, don’t you?"
    s "Who...{i}are{/i} you?"
    q "Who am {i}I?{/i}"
    s "Yeah. And where are we? And why are you acting so familiar with me?"
    q "Lots of questions there, huh? Does your missing friend not matter to you anymore? You’re more concerned with {i}me?{/i}"

    play sound "static.mp3"
    scene nodokacrazy28
    with flash
    stop sound

    q "Well, never fear! For I am also an expert cosplayer and just happened to have a spare pair of that girl’s summer clothes tucked into my socks!"
    s "What-"
    q "You see, I can’t tell you who I am. That would be against the rules."
    q "In fact, {i}we’re{/i} not even supposed to be talking right now. "
    q "But you’ve come to a special place."
    q "I don’t know how you made it here. Or exactly what your intentions in doing that were."
    q "But it’s {i}somewhere{/i} that {i}some{/i} rules become bendable while others stay the same."
    q "You feel me, dawg?"
    s "Your Nodoka impression could use some work."
    q "You feel me...incest guy? "
    q "Feel free to imagine that I just said a bunch of really smart sounding stuff there, too. My impression game is normally pretty on point, but that girl’s hard to do."
    s "You really can’t tell me who you are?..."

    play sound "static.mp3"
    scene nodokacrazy29
    with flash
    stop sound

    q "I really can’t."
    q "And I’m sorry for that. Truly."
    q "But the unfortunate truth is that if you knew who I was, you wouldn’t be able to go back at all."
    s "Why, though?"
    q "Because things have to happen a certain way."
    q "There’s a certain...{i}order{/i} to them, if you will."
    q "Which is probably why you no longer remember even meeting me in the first place."
    s "We’ve met before?"
    q "Oh yeah. A bunch of times."
    q "And we’ll meet a bunch more."

    scene nodokacrazy30
    with dissolve

    q "But, for now...I’ll send you off with a smile! "
    q "It won’t protect you from the dimensions you’ll have to slip through in order to make it back to where you belong, but at least you’ll know that {i}this{/i} is real."
    q "And that we’ll meet again the next time things get tricky."
    s "Wait-"
    q "I can’t."
    q "I’m sorry."
    s "But I just-"

    scene nodokacrazy31
    with dissolve

    q "Sayonara."
    s "Stop. I just have one more-"

    stop music
    play sound "alert.mp3"
    scene colorbars
    $ renpy.pause(4, hard=True)
    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene happy9 with flash
    scene nodokacrazy10 with flash
    stop sound

    no "Turn around! Face the door! Open it! And walk in a direction you seldom walk in!"
    no "This is how we find the truth! "
    no "This is where we can be free!"

    scene black
    with dissolve2

    "Nodoka and I go on a brief adventure through the various uninhabited floors of the dorms."
    "I always forget how many there are."
    "Eventually, she returns home having found nothing."
    "I do the same."
    "Along the way, I see a patch of daisies."
    "And it fills me with an uncomfortable sense of nostalgia."

    $ renpy.end_replay()
    $ nodoka_love += 1
    $ nodokadorm15 = True

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label nodokaspecial15p1:
    scene black
    with dissolve2

    "{i}Sometime after school, in a room full of steam.{/i}"
    "........."
    "......"
    "..."

    scene nodokashower1
    with dissolve2
    play music "icantseeher.mp3"

    mak "..."
    mak "..."
    mak "..."

    scene nodokashower2
    with dissolve

    no "Guess who~"
    mak "Hah..."
    mak "The same person who does this to every single one of us after every single practice?"
    no "Aww, don’t say it like that, Makoto. You know you’re my favorite out of everyone here."
    no "Besides, if you {i}didn’t{/i} want me to latch onto you like this, you’d stop using shampoo with such an enticing scent."

    scene nodokashower3
    with dissolve

    mak "So it’s not even safe for me to use my regular shampoo anymore? I must adapt to a completely new lifestyle just to prevent you from groping me?"
    no "You could always just reciprocate my one-sided lust for you instead. I promise I’ll be both gentle {i}and{/i} discreet. No one here would even know."
    mak "Uhh...{i}I{/i} would know. That’s exactly the problem."
    no "That doesn’t sound like much of a problem to me."

    scene nodokashower4
    with dissolve

    mak "That’s probably because you’re an insatiable lust demon who has seemingly devoted her entire purpose of living to making me feel uncomfortable."
    no "You say that, but we both know how wet you are right now."
    mak "I am literally in the shower."
    no "And I am very glad that you are. "
    no "What better place for the two smartest girls in school to bond than under a steady stream of hot water that we can use as an excuse to explain how flustered we are?"

    scene nodokashower5
    with dissolve

    mak "I was flustered the first three times you did this. By now, I have accepted it as just one more bump in the rocky road that is my life."
    no "Then why not accept what comes next as well? If history repeats itself, you should only be flustered the first three times. After that, I’m sure you’ll look forward to these special meetings just as much as I do."
    mak "Nodoka, you do realize that {i}every{/i} girl isn’t bisexual, correct?"
    no "I do not. "
    no "Girls know better than anyone just how attractive girls are. And the idea of there being some who intentionally deny that to maintain the guise of complete heterosexuality perplexes me."
    no "Why not indulge in these forbidden desires? You surely wouldn’t be the first female to have an orgasm in the shower room, you know. "
    no "Did you know the shower heads are detachable? You just need to move one of the benches over since they’re quite hard to reach with how high up they are."
    mak "I will keep that in mind if I ever feel compelled to pleasure myself in a room full of my friends."
    no "What better time to pleasure one’s self than in that exact scenario?"
    mak "Every time, Nodoka. Every time is better than that."

    scene nodokashower6
    with dissolve

    no "Fair enough. I suppose the urge to pleasure yourself isn’t as strong as it is for the rest of us."
    no "What with you already having an outlet for those desires of yours in our teacher and whatnot."

    scene nodokashower7
    with dissolve

    mak "I-"
    mak "I have no such thing! Where would you even-"
    no "Oh, come on. You think I don’t know?"
    no "I’ve read enough erotica to understand that there are no “pure” relationships between a perverted man in power and his loyal assistant."
    no "So, how long has it been now? How many times has he let it out inside?"

    scene nodokashower8
    with dissolve

    mak "Z...Zero! Even if we {i}did{/i} have that sort of relationship, which we don’t, I’m smart enough to not allow something like that."
    mak "Having a child at this point in life would derail all that I’ve worked for."
    no "Yes...perhaps it would. "

    scene nodokashower9
    with dissolve

    no "{i}But think about how good it would feel...{/i}"
    mak "Nodoka..."
    no "{i}His thick cock, pulsing inside of you...causing your tiny, precious body to overflow with his sweet, hot honey...{/i}"
    mak "This..."
    mak "This is starting to get out of hand, Nodoka. I’d really prefer it if you-"
    no "Oh, my sweet Makoto. Your secret is safe with me. I’d just like to...capitalize on it while I have the chance."
    mak "C...Capitalize...how?"

    scene nodokashower10
    with dissolve

    no "You know, I always thought it a tad unfair how your breasts are bigger than mine despite me being a little taller. Shouldn’t they grow {i}with{/i} our bodies rather than having minds of their own?"
    mak "They...don’t have minds. And it’s not like mine are that big to begin with. But, getting back to the thing about capitalization-"
    no "Those were just {i}words,{/i} Makoto. Words exchanged between two girls several pedestals higher than the rest. No one can hear us from so far below."
    no "But I suppose that has its cons as well for someone as nervous and worried as you."
    mak "This..."
    mak "You’re not intending to...{i}blackmail{/i} me...are you?"

    scene nodokashower11
    with dissolve

    no "Blackmail? {i}You?{/i} What reason would I have to do that?"
    no "I’m actually quite fond of you, you know."
    mak "Yes...you are making that very apparent with the way you’re fondling my breasts right now."
    no "Isn’t that just something girls do in school showers?"
    mak "Umm...n...not usually?"

    scene nodokashower12
    with fade

    no "Really? I thought it was okay for us to explore each others bodies? For educational purposes, of course."
    mak "Um-"
    no "Otherwise, how would we come to understand the ins and outs of sex? Pun not intended."
    no "It’s not like {i}all of us{/i} can have a big...strong...older man teach us... "
    mak "Nodoka, please watch where-"
    no "Say, do you keep this area trimmed? Or have you just not grown much hair yet?"
    mak "Wha-"
    no "Is he the one who asks you to keep it this way? Or is this a conscious decision on your part? "
    no "Again, if you’re still in the early stages of puberty, feel free to disregard that. It’s just-"

    scene nodokashower13
    with dissolve

    mak "Okay. You’re done. "

    scene nodokashower14
    with fade

    no "What’s wrong? Can’t a girl finger her friend in the privacy of the shower room without being stopped by the exact friend she’s trying to finger?"
    mak "Absolutely not! "
    mak "It’s one thing to consistently grope me in here every single day of the week- a thing that I should {i}not{/i} be so accustomed to, by the way."
    mak "But when..."

    scene nodokashower15
    with dissolve

    mak "When you start whispering about...sweet, hot honey and...commenting on my...you know..."
    mak "N-Not to mention the ridiculous accusations you’re throwing around about Sensei and me. "
    mak "You’re just...you’re just crossing way too many lines right now. "
    no "Apologies. I wasn’t trying to offend you. And if it seems that I was setting you up for blackmail, I can assure you that is not the case either."
    mak "It’s...fine. Just...stop groping me. I’m not interested in you that way."
    no "Is it because I don’t have a penis?"

    scene nodokashower16
    with dissolve

    mak "It’s obviously more than that!"
    no "Really?"
    no "Well it can’t be because of my hair. Or my intellect. Or the fact that I wear glasses. Or the fact that I am mildly manipulative and self serving. Or a bit of a narcissist. Or have an overactive imagination and sex drive."
    mak "It’s all of those things!"
    no "Our teacher has all of those things as well. All he has that I do not is a penis."

    scene nodokashower17
    with dissolve

    no "Oh! It’s an {i}age{/i} thing, isn’t it?"
    no "Have you always specifically been into older men? Or is this some sort of...newfound complex you’ve developed as the result of being constantly objectified and mentally abused by the man you like?"
    mak "Sensei doesn’t {i}abuse{/i} me. He just...he doesn’t understand what I need sometimes."
    no "Which is?"
    mak "I don’t know...someone who just...cares?"
    mak "Who will sit with me and...calm me down when my mind starts racing..."
    mak "Who will do little things for me, like...hold my hand or..."
    mak "Or..."
    mak "You know...stuff like that..."

    scene nodokashower18
    with dissolve

    no "I see, I see."
    no "I learned a lot about you today, Makoto."
    no "Right down to every last pubic hair."
    mak "And yet you are still treating my body as if it is some sort of toy."

    scene nodokashower19
    with dissolve

    no "Will you allow me to make it up to you?"
    mak "Are you just creating another opportunity to try and finger me right now?"
    no "Of course not. I, Nodoka Nagasawa, now understand that you, Makoto Miyamura, genuinely {i}do not{/i} want to be fingered by another girl."
    no "Up until a few moments ago, I was still on the fence about what to believe in regard to that. You have changed my life today."
    mak "You..."

    scene nodokashower20
    with dissolve

    mak "You make me really uncomfortable sometimes, you know..."
    no "Then allow me to do the opposite for a change in assisting you with the rest of your shower."
    mak "Showering is something I can do alone. It’s not a two person job."
    no "Can I help wash your hair at least?"
    mak "Nodoka-"
    no "Pleeeeeeease?"
    mak "..."
    no "..."

    scene nodokashower21
    with dissolve

    mak "The hair on my head?"
    no "Of course. Unless you’d rather-"
    mak "No. That much is fine."
    mak "But as soon as you’re done, you’re to leave this stall and never return. Do you understand?"
    no "Heh. Little do you know, I {i}like{/i} being disciplined. Put me in my place more often, Makoto."
    mak "Just...shut up and do your thing already, okay?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nodokashower22
    with dissolve2

    mak "..."
    no "..."
    mak "You’re actually pretty good at this."
    no "Yes, well..."
    no "I guess you could say I have a little experience."
    no "So, tell me more about the forbidden relationship you apparently do not have. When did you first realize that our teacher was the one for you?"
    mak "I didn’t. That never happened and the relationship we have is completely pure in nature."
    no "Okay. Then, {i}hypothetically speaking,{/i} if you {i}were{/i} to ever fall for him...what would be the cause? How would that story go?"
    mak "..."
    no "..."
    mak "Hypothetically speaking?"
    no "Mhm. And don’t worry about this hypothetical scenario extending to outside of this stall. I have no intention of revealing what you say to anyone at all."
    mak "..."
    no "..."
    mak "Well...hypothetically speaking..."
    mak "If I ever fell for Sensei...it would likely be for a number of reasons."
    mak "While he may seem mostly dismissive of me...and entirely unappreciative of all I do for him..."
    mak "I don’t think things are really as...one-sided as that."
    mak "Sure, it annoys me to no end...But when the school year began, I was trying way too hard to impress everyone. Granted, I’m still trying way too hard in a number of ways-"
    mak "But he was the first one to ever really notice that, I think."
    mak "He saw right through my disguise...all the way to the deeply flawed, stressed out, exhausting girl I am. And he treated me in accordance with that."
    mak "Combine that with how handsome and smart he is...and how I was kind of desperate for another male figure in my life after my dad was drafted to the space war...and..."
    mak "Well, it was only a matter of time until my curiosity turned into admiration. And then my admiration into...something else."
    mak "Is it wrong for me to expect more of him when he’s just as broken up on the inside as me? Maybe. "
    mak "But that’s why I’m able to put up with the constant unappreciation and dismissiveness. "
    mak "I like that he’s there for me. "
    mak "I just don’t like the form that takes sometimes."

    scene nodokashower23
    with dissolve

    mak "H-Hypothetically, of course!"
    mak "That’s just how things would be {i}if{/i} I ever started seeing him. Which I am not."
    no "Has anyone ever told you how cute you are, Makoto?"

    scene nodokashower24
    with dissolve

    mak "That’s...not really a word people use to describe me very often. So...thanks, I guess."
    no "No. Thank {i}you{/i} for taking the time out of your busy schedule to let me wash the chlorine out of your hair."
    no "I am truly unworthy."
    mak "Wh..."
    mak "What about you?..."
    no "What {i}about{/i} me?"
    mak "I mean...how do {i}you{/i} feel about Sensei?"
    no "Hypothetically?"
    mak "Yeah...hypothetically."
    no "Hm..."
    mak "..."
    no "He’s kind of like..."
    no "A dad."

    scene nodokashower25
    with dissolve

    mak "Right? He-"
    no "A dad that I want to watch fuck all of my friends."

    scene nodokashower26
    with dissolve

    mak "Heh?"
    no "You know. I’d take them home after school. Leave the room to go make tea or something."
    no "Then hear them crying out in pleasure from downstairs as he makes love to them on my bed."
    no "It’s less romantic than your story, but who says all stories need to be romantic?"
    no "Sometimes, a girl just wants her dad to fuck her friends, you know?"
    mak "..."
    no "..."

    scene nodokashower27
    with dissolve

    mi "Hey! You two almost done in there? The rest of us are goin’ out to eat at some family restaurant and don’t wanna leave ya behind."
    no "I’ll be finished with Makoto in just a second, but don’t feel obligated to wait up for me. "
    no "I have other matters to tend to after this."
    mi "Suit yourself, but it’s half off mozzarella sticks today and I think you’re gonna regret it."
    mi "You hear that, Makoto? Half off mozzarella sticks. You love mozzarella sticks."
    mak "..."
    mi "Makoto?"
    mak "I’ll be out in a minute Miku. I just..."
    mak "I need some time to collect my thoughts..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nodokashower28
    with dissolve2

    no "..."
    y "..."
    no "..."
    y "The fuck you want, Einstein? I can feel you starin’ at me."
    no "I was just wondering if you had any plans after this."
    y "Why? You think I want to hang out with {i}you?{/i}"
    no "Not really. "
    no "I’m just curious. That’s all."
    y "Well, go be curious elsewhere. I ain’t doin’ shit after this. Just goin’ home and goin’ to sleep."
    no "I see."
    no "I suppose I’ll see you tomorrow, then."
    y "Yeah, whatever. Just fuck off."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nodokashower29
    with dissolve2

    no "..."
    no "..."
    no "..."

    scene nodokashower30
    with dissolve

    no "Heh."
    no "I suppose it’s time I fuck off, then."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nodokashower31
    with dissolve2

    y "Huh?"
    y "Did I leave my locker open or something?"

    scene nodokashower32
    with dissolve2

    y "..."

    scene nodokashower33
    with dissolve2

    y "What?..."
    y "Where did..."

    scene nodokashower34
    with dissolve2

    y "Where the fuck did my clothes go?..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ nodokaspecial15p1 = True

    jump nodokaspecial15p2

label nodokaspecial15p2:
    scene street_noon
    with dissolve2
    play sound "phonebeep.wav"

    s "Hello?"
    no "{i}Sensei, good evening.{/i}"
    no "{i}I was just having a bit of a chat with your beautiful, four-eyed assistant and felt compelled to call after realizing just how frequently the two of you make passionate love to one another.{/i}"
    s "Uhh...that’s not really-"
    no "{i}Anyway, how are things? Are you doing well? Any plans for the rest of the night?{/i}"
    s "Can we maybe get back to the thing you just said about Makoto?"
    no "{i}Perhaps another time. We need not involve her in our personal affairs when she is but a mere gateway to their introduction.{/i}"
    s "I’m not sure if I follow, but no. I don’t have any plans for the rest of the night. I’m just...walking around. The same way I always do after school."
    no "{i}Would you be opposed to coming back to school?{/i}"
    s "Depends on what I’d be coming back for."
    no "{i}Ahh. So my presence alone is not enough to intrigue you? What a shame. I’m freshly showered and everything.{/i}"
    no "{i}Plus, the conversation and stark realization of your lecherous tendencies with a dear friend of mine has awakened something in me that I would very much like to share with you...as soon as possible.{/i}"
    no "{i}I guess the simplest way of putting it is that I have a bit of a present for you.{/i}"
    s "You..."
    s "Am I hearing that correctly? Because that sounds-"
    no "{i}How quickly can you make it to the pool? It wouldn’t be very kind to keep me waiting when I’m utterly quaking with anticipation, you know.{/i}"
    s "I am on my way right now."
    no "{i}Heh...I knew you would be.{/i}"
    no "{i}Oh, and I’m sure it goes without saying, but don’t tell anyone about this. Do you understand?{/i}"
    no "{i}I’d like to keep as many eyes off of me as possible. I am still a lady, you know? Even if I’m about to do very...unladylike things.{/i}"
    s "You have my word. "
    no "{i}Excellent.{/i}"
    no "{i}I’ve left the door unlocked for you, so feel free to wander right in and storm up to me with no restraint at all.{/i}"
    s "Got it. I’ll see you soon."
    no "{i}Oh, you sure will...{/i}"

    play sound "phonebeep.wav"

    "I hang up the phone and figure there is about a 50%% chance of there being some sort of catch to this, but I’m honestly too excited at this point to even worry about that."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "I’m also too excited to worry about the fact that Nodoka just...also knows about Makoto and me now for some reason. "
    "But hey, if believing that Makoto has finally one-upped her in some way is what Nodoka needed to just give in and finally sleep with me, that’s totally fine."
    "It was only a matter of time anyway. "
    "Did I think that time would come after a random school day when I was minding my own business and not even {i}thinking{/i} about Nodoka? Of course not."
    "But, given the type of person she is...and the type of person {i}I{/i} am...of course it would happen like this."
    "I turn off my inner monologue and focus on one thing- "
    "Getting to the school as quickly as possible."
    "........."
    "......"
    "..."

    scene nodokaspresent1
    with dissolve2

    "When I arrive, all of the lights in the pool room are off."
    "And since the sun has already begun to set, the amount of natural light in here is practically non-existent."
    "It’s replaced by the faint blue glow of dim fluorescent light reflecting off of the water and onto the glass-based tiles, which then reflect the light {i}again{/i} until it roams around infinitely."
    "But amidst the infinite light, the one thing I do {i}not{/i} see is the one thing I {i}came{/i} here to see, proving that my intuition in believing this to be a setup was likely true."
    "Either that or Nodoka is just...fucking with me and is still planning on giving me her virginity. Which seems like a pretty {i}Nodoka{/i} thing to do."

    s "..."

    "I should call her and find out."

    play sound "phonebeep.wav"

    "I tap on her name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    no "{i}Hellooooo?{/i}"
    s "Hey. Where are you?"
    no "{i}Wow. That was quick.{/i}"
    no "{i}If you’re that excited about defiling my body, I’m surprised you haven’t just taken it for yourself already. We’ve been alone enough and it’s not as if I would really fight you off.{/i}"
    s "That’s..."
    s "That’s not really something I would do."
    no "{i}Well, I suppose it doesn’t matter as I am very much a willing candidate today.{/i}"
    no "{i}There lies just one more barrier between you and my genitals, Sensei. And it is that of the locker room door.{/i}"
    no "{i}Would you kindly survey your surroundings one final time to make sure no one followed you in?{/i}"
    no "{i}Once you’ve confirmed that all is safe, simply pass through that door and make me yours.{/i}"

    scene black
    with dissolve2
    play sound "phonebeep.wav"

    "I hang up the phone and look around once more to make sure I’m alone, checking for security cameras as well since...my presence here would be hard to explain."
    "But after confirming that the coast is clear, I head to the only other door I can see and move one step closer to what I imagine will be the smuggest sexual encounter I ever have."
    "........."
    "......"
    "..."

    scene nodokaspresent2
    with dissolve4

    "But what I find is not that."
    "What I find is a mirror to my past misdeeds, magnifying them tenfold and beckoning me forward to repeat them with a fervor much greater and much more destructive."

    scene nodokaspresent3
    with dissolve2

    y "..."
    s "..."

    scene nodokaspresent4
    with dissolve2

    y "Huh?..."
    s "..."
    y "What..."

    play sound "static.mp3"
    scene nodokaspresent5
    with flash
    stop sound
    play music "thingsthathurt.mp3"

    y "Stop. "
    y "No."
    y "Don’t-"
    y "Don’t come any closer."
    s "Yumi-"
    y "Why?"
    y "Why are you-"

    scene nodokaspresent6
    with dissolve

    y "Why are you even here?! Did you fucking plan this?! "
    y "Did you and that fucking freak Nodoka seriously {i}plan{/i} this?! Was me apologizing for all that shit I did to Futaba not enough?! You need to fucking violate me now?! Is that what this is?!"
    s "That’s not what-"
    y "I thought you were changing! It was starting to seem like maybe you actually gave a shit about me! But if this was your plan all along, then..."
    y "Then you’re even worse than I thought!"
    s "I’m telling you that’s not what’s going on here. I thought I was-"

    scene nodokaspresent7
    with dissolve2

    y "Thought you were what? Just walking into the fucking girl’s locker room to {i}hang out?{/i} Do you really fucking expect me to believe that?"
    s "I...obviously know what it looks like. But I genuinely thought I was coming here to meet someone else."

    if yumiknows == True:
        scene nodokaspresent8
        with dissolve2

        y "Someone else?..."
        s "Yeah. I-"
        y "Aren’t you supposed to be dating Chika?"
        s "..."
        y "Hey."
        y "Aren’t you supposed to be dating my best fucking friend?"
        s "..."
        y "Who were you coming to meet, Sensei?"
        y "Because it sure as hell wasn’t her. "
        s "That-"
        y "Didn’t I tell you what I would do to you if you ever hurt her?"
        y "You think you can just fuck somebody else behind her back and get away with it? Is she not fucking good enough for you?"
        s "Okay...I know that what I’m doing is wrong. But...the thing with Chika and me isn’t exactly as simple as you think and-"
        y "Who is it?"
        y "Makoto? "
        y "Ayane?"

        scene nodokaspresent9
        with dissolve

        y "Did your fucking {i}niece{/i} reserve the pool after practice so you could come fuck {i}her?!{/i}"
        s "Yumi-"
        y "Don’t “Yumi” me! And stop fucking looking at me! The last person I want to see me like this is you!"

    else:
        scene nodokaspresent10
        with dissolve2

        y "Someone...else?..."
        y "Who?..."
        y "Who the fuck were you going to meet here?..."
        s "Does that really make a difference?"

        scene nodokaspresent11
        with dissolve

        y "I don’t fucking know! This came out of nowhere! "
        s "I get that. And I didn’t mean to scare you, I just-"
        y "If you don’t want to scare me, fucking look somewhere else! Your eyes have been on me this whole fucking time and I can’t fucking take it anymore!"

    scene nodokaspresent12
    with fade

    s "Yeah...sorry."
    s "I just..."
    s "Yeah."
    y "Just what?..."
    y "Saw a piece of meat that whet your appetite?"
    y "The same one you’ve already forced yourself on once before?"
    y "You just couldn’t get enough, could you?"
    y "You couldn’t fucking contain the person you are on the inside...so you waited for an opportunity like this...for my guard to be completely down."
    y "For no one to be around...no one able to help me...no one able to {i}hear{/i} me..."
    y "What did I ever do to you?..."
    s "Why...are you even here in the first place? Why didn’t you leave after practice?"
    y "..."
    s "..."
    y "She took my clothes..."

    scene nodokaspresent13
    with dissolve

    s "What? Who did?"
    y "Nodoka! And I already told you to stop fucking looking at me!"

    scene nodokaspresent12
    with dissolve

    s "My bad...just..."
    s "That...That was a reflex."
    y "Yeah...likely fucking story, asshole."
    s "Why would Nodoka take your clothes?"
    y "Figured it was the same reason {i}you{/i} showed up..."
    y "Revenge or some shit..."
    y "I...I know I’ve been a fucking douche in the past! I get that! But this is going way too far! You know I don’t deserve this, right?!"
    s "Again...I don’t have anything to do with this. I had no idea you were going to be here, and I wouldn’t have walked in if I knew you were."
    s "I’m just as much of a victim here as you."
    y "Oh, yeah. That’s fucking rich. The guy who gets to stand with a hard-on while a teenage girl is fucking naked and crying is just as much of a victim as she is."
    s "Okay...so that was poor wording on my part. But what I mean is that I...didn’t want this to happen either."
    y "And why the fuck would I ever believe that?"
    s "I...don’t have an answer for that. But if there’s anything I can do to fix this, I will."
    y "Yeah? Then find me a fucking pair of clothes. Bitch took everything in here. Ain’t even a fuckin’ towel left."
    s "I...yeah. Okay. "
    y "And...if you {i}really{/i} don’t have anything to do with this..."
    y "Can you maybe...call Chika?..."
    y "Tell her I...spilled something on my clothes or some shit and I...I need her to bring me new ones."

    scene nodokaspresent13
    with dissolve

    s "Do you want my-"
    y "STOP FUCKING LOOKING AT ME!"

    scene nodokaspresent12
    with dissolve

    s "Do you want my shirt in the meantime? I should probably keep my pants on for...reasons. But {i}me{/i} being shirtless is a lot better than you being...completely exposed like that."
    y "..."
    s "Yumi?"
    y "I’m fucking thinking, okay?! "
    y "I ain’t exactly comfortable with the idea of wearin’ your clothes, but..."
    y "I guess that it's better than...not wearing anything."
    y "Only until Chika gets here, though. After that, take your fucking stupid ass shirt back and burn it. Seeing it again will just bring back shitty memories."
    s "I...can’t burn this shirt. It was a gift. But I’ll...wash it thoroughly."
    y "{i}Really{/i} thoroughly. Like...a thousand fucking times."
    s "I’ll see what I can do."

    scene black
    with dissolve2

    "As I remove my jacket, I finally take notice out of the corner of my eye exactly how beautiful Yumi really is."
    "It’s hard to tell with the baggy clothes and...the way she typically presents herself, but her body looks less like one that belongs to a teenager and..."
    "And..."
    "And I realize how despicable I am in not being able to prevent myself from thinking things like this even when she’s at her most vulnerable."
    "As I’m removing the t-shirt Molly made for me, I discover that it is thin enough for me to see through."
    "In the brief period of time I have to avoid suspicion, I take additional notice of the size of her breasts."
    "The thickness of her thighs..."
    "And curves and contours that would fill most other girls her age with envy."
    "..."
    "Why do I have to feel this way?"
    "Why must I be so tempted to break her down even further?"

    play sound "cameraflash.mp3"

    no "Aaaaand...perfect."

    scene nodokaspresent14
    with dissolve2

    s "Nodoka? What-"
    y "You fucking bitch! Who the hell do you think you are?!"
    no "Right now? An expert photographer who just happened to sneak a candid shot of an adult male getting undressed with an already nude teenager."
    no "And a pretty good one at that. Perhaps I have a knack for this?"
    s "..."
    y "I...will fucking...murder you..."

    scene nodokaspresent15
    with dissolve

    no "You’re suspiciously silent, Sensei. I figured you’d be delighted to receive {i}Yumi{/i} as a present since you’ve undoubtedly wanted to sleep with her for much longer than you wanted to sleep with {i}me.{/i}"
    y "Delete that picture! And give me my fucking clothes back!"
    no "Tell me, was it hard holding yourself back? Was there a part of you that considered {i}indulging{/i} in my gift on account of its flawless execution and the fact we {i}all{/i} know we’re alone in here?"
    y "Don’t fucking answer that! You don’t have to answer that! I don’t want to hear it!"
    s "I’m not going to answer that. I’m just..."
    no "Just what? "
    no "Speak your mind. We’re all friends here."
    s "A little shocked, I guess..."
    no "Shocked? Why?"
    s "I just..."
    s "Don’t you...feel even a {i}little{/i} bad right now?"

    scene nodokaspresent16
    with dissolve

    no "Bad? I feel a number of things right now, but I wouldn’t call {i}any{/i} of them bad."
    no "There was a speck of remorse that appeared in having to drag {i}you{/i} into this, but..."

    scene nodokaspresent17
    with dissolve

    no "Well...then I realized that you’d like this just as much as I do. Even if you’ve evolved past the need to {i}admit{/i} that at this point."
    s "This is way too far for revenge, though. Yumi might be a total bitch, but she’s still a human being. "
    no "And that’s reason enough to feel {i}bad{/i} for her?"
    s "Kind of...yeah."
    no "Hmm...I can’t say I agree with that. But I suppose that you and I don’t have to agree on {i}everything.{/i}"
    no "The picture really is beautiful, though. Your erection is {i}quite{/i} pronounced. You can tell just how badly you want to fuck her."

    play sound "static.mp3"
    scene nodokaspresent18
    with flash
    stop sound

    y "Give me the fucking phone or I seriously {i}will{/i} kill you!"
    no "Ah-ah-ah. I implore you to reconsider your assault if you don’t want your beloved and treasured best friend to receive a copy of this image right now."

    scene nodokaspresent19
    with dissolve

    y "You..."
    y "You wouldn’t..."
    no "Oh, please. I stole your clothes and got our teacher to trounce over here for the sole purpose of enacting this little plan of mine. You really think I’d bail out at the last second?"
    no "I’ve had my finger hovering over “send” since the moment I took the shot. It was obvious you were going to come after me sooner or later. I needed to be prepared."

    scene nodokaspresent20
    with dissolve

    s "Why are you dragging Chika into this? She has nothing to do with it."
    no "I suppose the same reason Yumi felt compelled to drag my beloved Futaba through miles and miles of mud and shit."
    no "Because I’m a bad girl. And because making {i}other{/i} people feel bad makes my heart beat a little bit faster."
    no "But not as fast as those tits make it beat. Dear god. "
    no "To think something so lovely could be attached to something so utterly hideous on the inside."

    scene nodokaspresent21
    with dissolve

    y "So...what?"
    y "What do you want?"
    y "You wouldn’t take a fucking picture like that without intending to cash it in for something, right? I know how this shit goes."
    y "Is it {i}protection{/i} for your fucking friend? Because I already told her I ain’t gonna fuckin’ bother her anymore."
    y "And if it’s something like money, I ain’t got shit. So just tell me whatever the fuck you want from me to make that shit go away and I’ll do it."
    no "My, my. You’re smarter than you look."
    no "Fortunately for you, what I desire is something much...{i}shorter term{/i} than perpetual protection. But also much more valuable than money."
    y "Yeah? Then spit it the fuck out."

    scene black
    with dissolve2

    no "Sensei, please take this phone off of my hands. You’re much bigger than me and Yumi won’t be able to physically pry it off of you."
    no "Oh, and if you’re thinking of deleting it, don’t. It’s saved in a password protected folder, and your failure to follow directions will only make things worse for Yumi in the long run."
    s "..."

    "Not knowing what else to do, I take the phone and keep my mouth shut. "
    "I don’t like that Nodoka is doing this."
    "But..."
    "The part of me that shouldn’t exist is overflowing with the curiosity of what she’ll do {i}next.{/i}"
    "All this time, I’ve been aware of the connection I’ve felt to her."
    "At first, I couldn’t understand it."
    "But now?"
    "Now I understand that the connection is more than just our overly open sexual desires, forbidden interests, and the belief that all girls are just meat meant for fucking."
    "The connection is that we are two people who sit on separate thrones, looking down upon everyone else."
    "But my throne is too small for me."
    "And hers is far too large."

    scene nodokaspresent22
    with dissolve2

    no "First and foremost, I’d like to thank you for the wonderful show you’ve put on today. "
    no "The probability of tears was only around 30%% in my book, but I’m truly glad that you {i}did{/i} wind up crying- for I’ve always thought that young girls are at their most beautiful at the height of their sorrow."
    no "Now, to address what I, Nodoka Nagasawa, would like to exchange my {i}fantastic{/i} portrait of debauchery for."
    no "Keep in mind that complying with my demands will result in the picture and any copies of it being immediately wiped from my phone...and {i}failure{/i} to comply will result in it being sent to a local gyaru."
    y "Just fucking tell me what it is already so we can get this over with."
    no "There are {i}two{/i} options I will give you. But they both revolve around knocking you down several pedestals and putting you back on the level you belong."

    scene nodokaspresent23
    with dissolve

    no "Option one."
    no "You put on {i}another{/i} show for us."
    y "What kind of fucking show are you talking about?"
    no "Without beating around the bush, pun not intended, you are to pleasure yourself to completion on the bench directly behind you."

    scene nodokaspresent24
    with dissolve

    y "I’m...to {i}what?{/i}"
    no "I don’t care {i}how{/i} you do it. In fact, I’d even be willing to provide some sort of assistance. I just care that it gets done."
    no "And don’t tell me something like “You don’t know how” or “You’ve never done it before” because I just flat out won’t believe that."
    s "..."
    y "What..."
    y "What’s...the second option?"

    scene nodokaspresent25
    with dissolve

    no "Option two."
    no "In the event that you’re unable to bring yourself to performing such a heinous act in front of the two of us-"

    scene nodokaspresent26
    with dissolve

    no "You will watch as I, Nodoka Nagasawa, perform a one-sided sexual favor for our teacher. "
    y "Wha-"
    no "Once again, to completion. Because, let’s face it, he deserves it at this point for holding himself back so well."
    y "You..."
    y "But...why...{i}that?...{/i}"
    no "Why {i}that?{/i}"

    scene nodokaspresent27
    with dissolve2

    no "The answer is simple, really..."
    no "Because I think {i}that{/i} would hurt you even more."
    y "That’s...no..."
    y "No! Why would that hurt me?!"

    scene nodokaspresent28
    with dissolve

    y "Why would something like that hurt me?! Why do you think that?!"
    no "Obviously because you’re falling for this handsome sculpture of a man, no?"
    no "I can’t think of any easier way to knock you off of your high horse than to pleasure him myself while you’re forced to sit there and watch."

    scene nodokaspresent29
    with dissolve

    no "Also, I’m beginning to get a little tired of people thinking I’m all talk when I normally just {i}prefer{/i} to sit back and watch."
    no "I have needs too, you know? And I woke up {i}particularly{/i} aroused this morning knowing what awaited me after school."

    scene nodokaspresent30
    with dissolve

    no "So, what do you say? Will you take the plunge, swallow your pride, and masturbate in front of the man you hope to give yourself to one day?"
    no "Or will you watch as someone {i}else{/i} takes him right in front of you?"
    y "..."
    s "Are you serious about this, Nodoka?.."
    no "Do I look like I’m joking?"
    s "No...it just seems so-"
    no "Honestly, Sensei. The best thing you can do right now is keep quiet. Say anymore and you’re just going to paint yourself as a target as well."
    no "Right now, I’m the matador. And this hot piece of meat is the bull. She sees red because I’m the one waving the flag in front of her."
    no "And if she knows what’s good for her, she’ll make a choice in the thirty seconds or-"

    if yumiknows == True:
        scene nodokaspresent31
        with dissolve

        y "Fuck off! No I won’t! "
        y "If you seriously thought I’d do either one of those things, then...you obviously should have thought this through more!"
        y "Send Chika the fucking picture for all I care! She’ll understand! She’ll know that I would never do anything like that to her!"
        s "Yumi-"

        scene nodokaspresent32
        with dissolve

        y "And fuck you too! I’m {i}less{/i} mad at you after realizing this was all just Nodoka being a fucking cunt, but I’m..."
        y "I’m still mad that you keep looking at me so much! Fuck off!"
        y "And all that shit she said just now! About {i}me{/i} falling for {i}you?!{/i} That ain’t fuckin’ true!"
        y "That ain’t even close to the truth!"
        y "So...keep that shit to yourself and don’t believe her! In fact, stay the fuck away from her for good! Or I seriously {i}will{/i} tell Chika! Got it?!"
        s "Yeah...just..."

        scene nodokaspresent33
        with dissolve

        y "No! Fuck you both! I’m out of here! I’ll just...rip a fuckin’ flag up and walk home with that around myself or some shit!"
        s "At least take my-"
        y "I said fuck you!"

        "Yumi exits the locker room, still completely naked, and storms off toward what I imagine will be a very uncomfortable rest of the night."
        "But it’s not like I’m comfortable right now either."
        "Even knowing that Nodoka may potentially perform some sort of sexual act on me at any moment."

        no "..."
        s "..."
        no "Well, that was unexpected."
        no "I didn’t think she’d...actually storm off naked..."
        s "Yeah, well...you just don’t understand Yumi, I guess."
        no "No...I guess I don’t..."

        scene nodokaspresent34
        with dissolve

        s "Is this...really who you are, Nodoka?"
        no "My answer really depends on what you mean by that."
        s "I mean that I didn’t think you’d go that far just to get revenge on someone."
        no "It’s not {i}just{/i} for revenge, Sensei. It’s to push limits and satisfy my curiosity- which is {i}precisely{/i} the type of person I am."
        no "That said, I’m going to take a rain check on fellating you. I’m simply just not in the mood for it anymore after that abrupt and unfulfilling ending."
        no "But if you’d like to masturbate to the image of a girl in denial with herself about the things she wants you to do to her, let me know and I will send it to you."
        s "I...don’t need that."
        s "I’m more worried about whether or not you’re still going to send it to Chika as...that would create a world of problems for me."
        no "Then I suppose for your sake I can abstain."

        scene nodokaspresent35
        with dissolve

        no "It’s been fun, though."
        no "It’s no janitor’s closet, sure. But I do hope that we can do this again sometimes."
        s "And I..."
        no "..."
        s "I’m..."
        s "Going to go look for Yumi..."

        scene black
        with dissolve2

        "I put my shirt back on and leave the locker room. "
        "At first, a trail of tears on the tile floor lead me down the path she must have taken."
        "But the trail disappears and so does my motivation to find her."
        "Regardless, I keep trying for the next thirty minutes before finally deciding to call it quits and head home."
        "And while I may not have found her-"
        "Or done anything to quell the storm that I’m sure is raging within her right now-"
        "I hope that Yumi made it home okay."
        "And I hope that she doesn’t dwell on this for too long."
        "As for Nodoka-"
        "..."
        "As for Nodoka..."
        "I don’t even know."

        $ renpy.end_replay()
        $ nodoka_love += 5
        $ nodokaspecial15p2 = True
        $ nodokaspecial15p3skip = True
        stop music fadeout 10.0

        "{i}Nodoka’s affection has been increased by 5!{/i}"
        "........."
        "......"
        "..."

        $ day = 5
        $ totaldays += 1

        hide thursday onlayer date
        show friday onlayer date

        jump yasuspecial20

    else:
        y "I’ll do it."
        s "...What?"

        scene nodokaspresent36
        with dissolve

        y "I’ll...do it..."
        no "Oh? How unfortunate for you, Sensei. You were this close to finding out what the inside of my mouth feels like."
        s "Are...you sure about this, Yumi?"
        y "What fucking choice do I have? "
        y "It’s either  that or...she..."
        y "She..."
        y "And...And I can’t...let Chika see..."
        y "It would...totally ruin our friendship. And I can’t lose that. She’s the only one who-"
        no "Yes, yes. Less talking, more masturbating. "

        scene nodokaspresent37
        with dissolve

        y "Can you at least...close your eyes?"
        s "If that’s-"
        no "Oh, I forgot to mention- no. Neither one of us will be doing that."
        no "Where’s the fun in a show if you can only {i}listen{/i} to it and not watch?"
        no "I {i}am{/i} feeling a little generous, though. So I’ll let you face away from us if that helps get you in the mood."
        s "{i}This{/i} is generous?"
        no "Chances are she’ll want to face you anyway. It’ll help prime her body for-"
        y "Do me a favor and shut the fuck up."
        y "I won’t be able to do this if I have to listen to your voice. "
        y "It’s like nails on a fucking chalkboard."

        scene black
        with dissolve2

        "Yumi brings herself back to the bench she was sitting on when I first came in and lays down on her side."
        "Nodoka pulls on my abdomen and creates some space between us and her."
        "Yumi faces away before parting her thighs. "
        "I had a feeling she would."

        $ renpy.end_replay()
        $ nodoka_love += 5
        $ nodokaspecial15p2 = True

        jump nodokaspecial15p3

label nodokaspecial15p3:
    if _in_replay:
        play music "thingsthathurt.mp3"

    scene thematador1
    with dissolve2

    no "Oh, how the mighty Yumi Yamaguchi has fallen...Reduced to a desperate mess of tears and hormones as she gently rubs herself for a small group of lascivious spectators."
    no "I imagine you didn’t expect your first sexual experience with her to be like {i}this,{/i} did you? "
    no "Assuming this is your first. But based on how much our unpaid talent is nervously quivering, I’m pretty sure it is."
    no "I was hoping she’d face us, though. From this angle, it’s hard to tell if there’s been any insertion yet."
    no "Perhaps she’s saving that part for you, Sensei? Perhaps she {i}wants{/i} you to make your way over there and help her get the job done?"
    no "I know {i}I{/i} would love to see that. "
    no "I’d just ask that you rough her up a bit. We don’t want her enjoying herself too much, do we?"
    s "..."
    y "..."

    scene thematador2
    with dissolve

    no "No commentary at all?"
    no "It could take her {i}ages{/i} to climax without the sound of your voice. If you feel that bad for her, why not cheer her on?"
    y "Don’t..."
    y "Don’t say anything..."
    y "I just...I just want this...to be over..."

    scene thematador3
    with dissolve

    no "This is nothing compared to a lifetime worth of doubting yourself and thinking you’re not worthy of even stepping into the same room as your peers."
    no "This is nothing compared to the strain your words have caused on the mind of my friend. Nothing compared to the acid burns and scar tissue now coating her esophagus."
    no "Do you know what it’s like to be scarred on the inside, Yumi? To have all of your ailments hidden so deep inside of yourself that no one even knows they’re there? "
    no "So you have to masturbate in front of a couple people. Boo fucking hoo. "
    no "If you weren’t such a tsundere, you’d already be doing this for one of us on a nearly weekly basis anyway. "
    no "If anything, you should be {i}thankful{/i} that my perversion has created such a lenient and {i}simple{/i} way for you to repent for all the damage you have caused."
    y "I’m sorry...I’m sorry..."
    y "Can I please stop now? Can I-"
    no "It’s been two minutes. Don’t tell me you’re so turned on by this that that’s all it took?"
    y "Mm...no...that’s not..."
    y "I just...I can’t..."
    s "Just let her stop, Nodoka. This has gone on long enough."

    scene thematador4
    with dissolve

    no "See, that’s where I disagree."
    no "Set aside your feelings and objectively approach this situation as if it’s a scene in a book."
    no "What half-assed, incompetent writer would set up such a dramatic and heart wrenching scenario only to backtrack on it once things become too painful?"
    no "Things that hurt are what provide the incentive for us to push through as readers and progress the story. Things that hurt are why we gorge ourselves on words in the first place."
    no "I suppose you could argue that the opposite side of things can be just as fulfilling, and that pain alone is not what brings us satisfaction."
    no "But to that I’d say- remember what you’re reading."
    no "We’re not worthy of happy endings."
    no "We’re the ones who opened up this book knowing what was inside of it. "
    no "And the idea of us changing our minds just because the immersion is becoming too much to bear would make us so weak that it would be utterly sickening."
    no "Are you weak, Sensei? Are you afraid of how real things can become at the drop of a hat?"
    no "Or is this a story you want to stick out until the end?"
    no "Before you answer, though, you should be reminded that closing a book doesn’t mean the story stops."
    no "It will keep going with or without you."
    no "The key is whether or not you’ll let it carry you to somewhere amazing...or drown you in a sea of letters."
    no "I’d say the choice is yours, but that choice has already been made."
    no "It was made a long time ago."
    no "So, would you kindly finish this chapter with me?"
    no "Or would you rather drown?"
    s "..."
    no "..."
    y "I can’t..."

    scene thematador5
    with dissolve

    no "You can’t? What do you mean you {i}can’t?{/i}"
    y "I can’t do this...I really can’t...it’s..."
    y "I can’t do it..."
    no "Do you need a hand? There are four extras right behind you."
    no "Or perhaps you’d like to try turning around? Maybe setting your sights on something you love will help get you off?"
    y "I can’t do it...I really can’t..."
    y "I tried, but...I’m sorry...I’m sorry, I just...I can’t...keep going..."
    no "Hm. "
    s "The chapter’s over, Nodoka. Just give her back her clothes."
    no "Oh, come on. Do you really think I’d let this chapter have such an anticlimactic ending?"

    scene thematador6
    with dissolve

    no "Welp, time to get this show on the road. Nodoka Nagasawa is about to make her blowjob debut."
    y "Huh? No..."
    s "Are you serious?"
    no "Of course I’m serious. I gave Yumi two options. She chose the first but couldn’t complete it. Which means that we’re now defaulting to the second."
    no "And, unlike her, I’ll actually complete my job."
    s "Nodoka-"

    scene black
    with dissolve
    play sound "zipper.mp3"

    no "Yes, yes. You can thank me later."

    "Nodoka brings herself to her knees and unzips my pants as Yumi props herself up on the bench, still caught in a daze over how quickly all of this is happening."
    "She tries to make eye contact with me, but I can’t bring myself to look back at her."
    "I just look away as a set of overly confident hands crawl into the opening in my pants and unsheathe my cock."
    "And, as if that wasn’t shameful enough-"
    "Witnessing all I have in this locker room has brought me within seconds of climaxing before my skin is even touched."

    scene thematador7
    with dissolve2

    no "It’s good to know I wasn’t the only one quaking with anticipation."
    no "Your insistence on putting an end to this was beginning to make me worry that you actually {i}weren’t{/i} enjoying yourself. Which I see now is very much not the case."
    s "..."
    no "I hope you’ll forgive me if I’m not very good at this. It {i}is{/i} my first time and all. But I’ve read enough erotica to have an idea of what to do here."

    scene thematador8
    with dissolve

    no "Oh, and Yumi?"
    y "..."
    no "Make sure you get a good look at his face while I let him fuck my mouth."
    no "If you remember it well enough, maybe you’ll actually be able to finish yourself off next time?"
    s "Nodoka-"

    scene thematador9
    with dissolve

    no "Mmnh..."
    no "Mmf...hngh.......mlem...amf...mmh..."
    no "Mmf...mmm...Sensei..."
    no "Is...she watching?..."
    s "..."
    y "..."
    s "Yes..."

    "Nodoka coats the underside of my shaft with hot, sticky saliva. "
    "Her hair brushes against my skin each time she moves to the base of my cock and winds up getting stuck to it on several occasions."
    "She deftly moves it away with her fingers before curling them back around me and devoting every bit of her attention to pleasing me."
    "It’s not {i}just{/i} me who’s feeling the heat, though, as Nodoka’s noises grow increasingly louder the more time she spends on my cock."

    scene thematador10
    with dissolve

    no "Ahm...mmm...hmm!"
    no "Sensei...you’re so big...you’re so big and hard...and you got this way just for me..."

    scene thematador11
    with dissolve

    no "Do you like that?..."
    no "Do you like the way I lick your cock in front of another girl?..."
    no "Is she still looking?..."
    s "Y-"
    no "You’re a fucking liar...mmh~"
    no "There’s no way she’d...watch this unless she was a true degenerate...a true degenerate like me...like {i}us...{/i}"
    no "Do you have any idea how wet I am, Sensei? How desperately I longed for this taste?..."
    no "A taste that’s better than I ever imagined...and I get to have it all to myself while Yumi waits in the corner..."
    s "Stop...saying things like that..."
    no "Mmf...mmh~"
    no "Do you think...if we gave her a third option...for {i}her{/i} to do this instead of me...that she would have taken it?..."
    s "..."

    scene thematador10
    with dissolve

    no "Because I do..."
    no "Mmf...ngh...mlem.......mm~"
    no "And that’s why I didn’t give her one..."

    scene thematador12
    with dissolve

    no "Mmn!~"
    no "It’s...so hard to fit it all in my mouth..."
    no "But I’ll...do my best...for you, Sensei..."
    no "For you...the only man I would ever do this for..."
    no "Does it feel good?..."
    no "Does my mouth make you want to cum?..."
    no "Do you want to cum {i}in{/i} my mouth?..."
    no "Amf...mlem...or maybe..."
    no "Do you want to cum...on my face?..."
    no "Do it wherever you like..."
    no "For tonight only...all I care about is you...all I care about is your huge...huge cock...that I get to have...while Yumi gets {i}nothing...{/i}"

    "I still can’t find it in myself to look at Yumi, but I don’t need to."
    "Her sobbing at this point has grown loud enough to compete with Nodoka’s cock-sucking noises, alerting me to exactly how she feels right now."
    "And knowing her, that probably makes her feel even worse."

    no" Sensei...Sensei..."
    no "Sensei!~"

    "I..."
    "I can’t hold back anymore."

    play sound "static.mp3"
    scene thematador13
    with flash
    stop sound

    y "Wha-"
    s "I’m sorry...I couldn’t...I...had to..."
    no "Mmf! Mmngh! Mmf! "
    no "Yes...Yes...Yes! Fuck...my mouth...harder...harder!"
    y "..."

    "I lose control of my limbs and give into the desire to shove as much down Nodoka’s throat as she’s able to take."
    "Which, I won’t lie, is a lot more than I expected for her first time."
    "Her tongue presses against my dick not out of tactic or strategy, but out of desperation as it tries to find a new home in its host’s mouth."
    "But despite being practically suffocated at this point, Nodoka makes no effort to get away- letting me do what I please with her head as I grab the back of it and pull it forward like an oversized fleshlight."
    "All the while, Yumi looks on in extreme terror and awe."
    "I know this because I finally made eye contact with her."
    "I’m just too enveloped in pleasure to regret that right now."

    s "Nodoka..."
    no "Sensei...mmmf...mmm!~"
    no "I’m sorry to ask this in the heat of our passion, but...could...I come up for air for a moment?..."

    scene thematador14
    with dissolve

    no "Pah! Hah...hah...wow..."
    no "This...is amazing..."
    no "I’ve even stopped hamming it up for more fun..."
    no "You didn’t slip me some sort of aphrodisiac, did you?"
    s "I...didn’t do anything..."

    scene thematador15
    with dissolve

    no "You didn’t?"
    no "Then I guess I just really love your cock!~"
    no "I’m so thankful that I get to do these sorts of things with you, Sensei..."
    y "Die..."
    y "Fucking die..."
    no "Yumi, if you’d like to get a closer look, there is plenty of space on either side of me right now."
    no "I’m sure Sensei wouldn’t mind either..."
    s "I...wouldn’t...but..."
    no "I’m even willing to share some of his semen with you. We can bond over that instead of some sort of peace treaty. Great idea, wouldn’t you agree?"
    s "Nodoka...I kind of..."

    scene thematador16
    with dissolve

    no "Kind of what? Can’t wait any longer?"
    no "Did I come up for air at a bad time? I could have held out a few more seconds if I knew that-"

    scene thematador17
    with dissolve

    no "Ah-"

    scene thematador18
    with dissolve2

    no "Oh."
    no "I suddenly understand what the urgency was."
    no "Of all the times to do that, you wait until I {i}stop?{/i} How am I supposed to interpret that in regard to my skill?"
    no "I suppose there will be other opportunities to {i}really{/i} put that to the test, but-"
    y "Shut the fuck up."

    scene thematador19
    with dissolve

    no "Oh, right. For a moment, I forgot you were even here."
    no "I suppose you’re eagerly awaiting the wrap up, huh?"
    no "Would you mind if I took a moment to clean all of our teacher’s semen off of my face first? It would be a shame to go out in public looking as...unpresentable as this."
    y "Delete..."
    y "The fucking..."
    y "Picture..."
    no "Yes, yes. I’ll hold up my end of the bargain. I just need to run to the restroom first."
    no "Until then, the two of you are free to mingle and talk all about the wonderful bonding experience we all shared today."
    no "I know I’ll be remembering this for years to come."

    scene black
    with dissolve2

    "Nodoka leaves the room and Yumi and I stand there in silence for the entire duration of her departure."
    "When she returns, she brings Yumi’s clothes with her and tosses them back to her before reaching into my pocket and grabbing her phone."
    "It isn’t until that moment that I realize I never bothered putting my dick away."
    "And that I’d been hanging it in front of Yumi’s face like a carrot on a stick ever since cumming on another girl’s face right in front of her."
    "The same girl who forced her into this mess."
    "Who forced {i}me{/i} into this mess alongside her."
    "..."
    "And yet, I somehow still came out on top."
    "........."
    "......"
    "..."

    scene thematador20
    with dissolve2

    no "Aaaaaand...done."
    no "All copies of the picture have been destroyed and no one, including me, will ever see it again."
    no "How sad."
    y "It’s really gone?..."
    no "It really is. But if you’d like me to take another just to commemorate the occasion, feel free to remove your clothes once more and-"

    scene thematador21
    with dissolve

    y "Like {i}hell{/i} I want to “commemorate the occasion!”"
    no "Wait. Don’t take that. I need-"

    scene thematador22
    with hpunch
    play sound "glass.mp3"

    no "Hah..."
    no "I was really hoping that wouldn’t happen. But I guess it’s fair."

    scene thematador23
    with dissolve2

    y "The next time I see you, you are going to die."
    no "I’m looking forward to it."
    s "Yumi, I-"

    scene thematador24
    with dissolve2

    y "..."
    s "..."
    y "..."
    s "..."

    scene thematador25
    with dissolve

    "Yumi leaves the room without saying anything to me."
    "She doesn’t need to."
    "The way she looked made her feelings clear enough."
    "When I turn around to watch her leave, I step on the shards of a broken cellphone and almost slip because of it."
    "I kind of wish I did."
    "For even though I did not intend to hurt anyone tonight, my inaction spoke volumes in reminding her of who I really am at the end of the day."
    "I’m not someone who cares."
    "I’m not someone who’s here to help her succeed."
    "I’m just {i}someone.{/i}"
    "And she deserves a little more than that."

    scene thematador26
    with dissolve

    no "Why the solemn gaze? You’re the first person to ever ejaculate on me. You should be smiling."
    s "Why did you do that?..."
    s "Since when are you the type of person who blackmails someone?"
    no "Since when do you care?"
    no "You got what you wanted. I got what I wanted. Isn’t that really all that matters?"
    no "You know better than anyone that sometimes people need to be hurt in order for others to benefit. Today, {i}we{/i} are those beneficiaries."
    no "So what if {i}Yumi{/i} suffers after all the suffering she’s put other people through? This is sure to do more for her future cooperation than any detention or stern lecturing would."
    s "She was already {i}changing,{/i} though. She’s come a long way since I’ve met her. And she’s already apologized to Futaba and-"
    no "That’s not good enough."
    s "What?"
    no "I said that’s not good enough."
    no "This likely won’t come as a surprise, but there aren’t many people I care about in this world."
    no "And while one of the main reasons for that is that there just aren’t many people who {i}interest{/i} me, a {i}second{/i} main reason is that it’s just far too exhausting."
    no "You see, I {i}protect{/i} the people I care about. And sometimes, protecting someone means cutting down the person they must be protected {i}from.{/i}"
    no "And other times, if that person doesn’t {i}need{/i} protection anymore, I simply...avenge them instead."
    s "I don’t think Futaba wanted revenge."
    no "She didn’t."
    no "But I did."
    no "And so I got it...because I am a freethinking, powerful girl who takes what she wants {i}when{/i} she wants it."
    no "If doing that means hurting someone that matters less to me than the dirt I walk on, I really don’t care."
    no "All I have to lose is the favor of others. "
    no "That said, do {i}you{/i} think any less of me now?"
    s "Would you care if I did?"
    no "Of course. If I didn’t like you, I wouldn’t have let you cum on my face. "
    s "I..."
    s "I don’t really know how I feel."
    no "I think the fact that you {i}don’t{/i} know just confirms that your opinion of me hasn’t changed at all."
    no "If you can watch me engage in something as morally reprehensible as blackmailing someone into masturbating and then fellating the person they like in front of them...and {i}not{/i} be mad about it-"
    no "Well, let’s just say most traditionally “good” people would put their foot down then and there."
    no "But you let it happen. Albeit with a few “No, stop”s sprinkled in. But I think that was just you doing your best impression of someone with a moral compass."
    no "The truth is that you only feel bad about certain things because you think that you’re {i}supposed{/i} to feel bad."
    no "Why not just live your life surrounded by the people you care about? Why not build a moat to keep everyone else out?"
    s "..."
    no "..."
    s "Isn’t it lonely keeping everyone else out?"

    scene thematador27
    with dissolve

    no "Not to me."
    no "But I suppose we should end things there for today. Especially since I now need to take a {i}second{/i} shower when I just took one a couple hours ago."
    no "Hopefully, your relationship with Yumi isn’t {i}too{/i} badly damaged based on what just happened. It would be a crying shame if you had to live the rest of your life without seeing her tits again."
    no "Fortunately, I believe all of her anger is directed at me right now. And that you should be okay for the immediate future."
    s "What about you, then? Aren’t you worried about what she’ll do to get back at you?"
    no "Right now? Not really."
    no "Right now, all of my serious thoughts are blocked by the intoxicating scent of your cum. "
    no "Thank you for that, Sensei. I’m sure my dreams tonight will be spectacular."
    s "I think the fact that you can sleep at all is something to be proud of."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Nodoka and I walk out of the locker room together."
    "We walk back to the dorms together. "
    "And all the while, we somehow manage to not despise each other’s presence despite the constant entanglement of our shadows and our thoughts."
    "When she returns to her room, she takes a piece of me with her."
    "When I return to mine, I take a handful of sleeping pills. "

    $ renpy.end_replay()
    $ nodokaspecial15p3 = True

    "{i}Nodoka’s affection has increased by 5!{/i}"
    "........."
    "......"
    "..."

    $ day = 5
    $ totaldays += 1

    hide thursday onlayer date
    show friday onlayer date

    jump yasuspecial20

label nodokaspecial20:
    scene stillcalm1
    with fade

    ya "You...want to know about the tendrils of the sky?"
    no "I’d like to know anything and everything. {i}Knowing{/i} is kind of what I do."
    s "What a surprise. Knowing is what Yasu does as well. Maybe you’d like to lend her your arm so she can get off of mine?"
    no "I’m happy to lend my arm to just about anybody."
    s "Could’ve fooled me."
    no "Ha. Funny."
    ya "The tightness in my chest tells me that I should not switch arms...and that any arm apart from this one has the potential to infect me with feelings I do not deserve to feel."
    no "Are you certain that’s what the {i}tightness{/i} is telling you? Because, based on my experience-"
    s "So anyway, tendrils."

    scene stillcalm2
    with dissolve

    ya "Right! It is my duty to be the font of information undocumented, so I will tell you all about the opening of the sky and the tendrils that extend beyond man’s wildest imagination."
    ya "There is only one god. A god of infinite eyes. But there are forces in this world that would have people believe otherwise."
    ya "Forces of great power, but poor intent. And often times, these powers are used to both intimidate and scare those who walk His holy grounds."
    ya "The tendrils of the sky are one of many examples of this. And while their tangibility is not the same as if you were to reach out and touch me, the impact they would have on you would be much greater."
    ya "Your mind would turn to dust. Your organs to ash. And all of your thoughts congealed into a twisting mass of ivy that feeds into the dirt and goes on to stretch from building to building."
    no "So...the sky would have us returned to the ground?"

    scene stillcalm3
    with dissolve

    ya "You hear my words, but misjudge their meaning. This world is not as simple as one above and one below."
    ya "It is an endless labyrinth of layers invisible to the naked eye...each with its own steady stream of waste."
    ya "They all flow into one pool that we are forced to bathe in. "
    ya "The dirty runoff is collected and returned to the sky."
    ya "And so the ground mixes with the air...and rains down upon the ivy, cannibalizing itself as it recycles energy and becomes stronger in a way much more difficult than simply asking Him for power."
    ya "We all become water. We all become dirt. It is the cycle of everything that is and everything that wants to be. And only He can pull us from the vines and save us from this never ending circling of the drain."
    s "I couldn’t have said it better myself."
    no "Interesting."
    no "Why haven’t I heard of this...fascinating religion before?"

    scene stillcalm4
    with dissolve

    ya "Because I am the only one who speaks of it! Are you interested? Do you seek salvation? For if you do, I can show you the light. "
    ya "And before you know it, you will be bathing in its warmth rather than a puddle of human excrement."
    no "I think I’ll stick to bathhouses and showers. But I thank you for taking the time to explain a bit about your religion to me. I won’t lie in saying I’ve been very curious since the moment you walked in."
    f "I...was worried you were going to say something mean to her."

    scene stillcalm5
    with dissolve

    no "You were? Why?"
    f "Well...you’ve always been very quick to debate people when it comes to religion."
    no "Futaba, as an atheist, I am obligated to do just that. But there is a certain fundamental basis to what Yasu preaches that I see no reason to speak out against."
    no "She speaks of a cycle. And while it is essentially just a rehashed and painted version of the {i}water{/i} cycle, it’s not as if she’s telling us about stone tablets that dictate the way we live our lives..."
    s "She did talk about giant invisible sky tentacles, though."

    scene stillcalm6
    with dissolve

    no "And I hope she is right about them for that is the single most enticing thing I have ever heard about any religion."
    s "Just wait until you learn what my supposed duty would be if I were a devout follower."
    no "Oh? Would you care to educate me?"
    s "I don’t want to say it in front of Futaba. She’s still too pure."

    scene stillcalm7
    with dissolve

    f "I...I am?! "
    f "Still? "
    f "I would have figured that...you know..."
    no "Yes, Futaba...share the juicy details of what whisked away your purity out loud. Loud enough for the whole class to hear. "
    s "Or don’t. "
    s "In fact, definitely don’t. It’s been over five minutes and I have officially overstayed my welcome."

    scene black
    with dissolve

    no "What welcome? You know you’re welcome here any time, Sensei."
    s "I am honoring Yasu’s premonition and only sticking around for a little while today. After that, you’re all on your own. Or...at least under Imani’s supervision."
    s "That said, Yasu- back to your seat."
    ya "Okay. Thank you for being with me, Sensei. I was entirely unworthy of your protection, yet received it anyway."
    ya "I can hardly even hear any whispers about the bad thing anymore."
    s "That’s great news. Anyway, goodbye everyone. It’s been-"
    no "Wait one second, Sensei. Don’t you think {i}I{/i} need a little protection too? It’s not fair if only Yasu gets some, is it?"
    f "What would you need protection for? "
    f "You haven't been groping Makoto again, have you?"
    s "Okay, I’m suddenly interested in staying."

    "I follow Nodoka and Futaba over to their seats on the side of the room, both surprised and {i}un{/i}surprised to hear about Nodoka’s {i}second{/i} sexual violation over the last 24 hours."
    "The two of them pick up exactly where they left off before I wandered into class late and proceed with the conversation as if I’m not extremely turned on by the thought of it."

    scene stillcalm8
    with dissolve2

    no "I’ll try to keep this short seeing as Sensei is likely extremely turned on by the thought of it-"

    "Yeah, I should have seen that coming."

    no "But yes. I {i}have{/i} been groping Makoto again and it has been very fun for both of us."
    s "It has?"
    f "I...don’t think it has. I’m pretty sure Makoto isn’t bisexual."
    no "You don’t need to be bisexual in order to enjoy the sensation of the sex you’re not interested in exploring your body."
    f "I’m pretty sure...that’s exactly what you need to be bisexual for."
    no "Well, either way, Makoto isn’t the type to put a hit out on me over something as trivial as a little bit of dubiously consensual rubbing."

    scene stillcalm9
    with dissolve

    mak "It wasn’t {i}dubious!{/i} I told you to stop repeatedly!"
    no "Ignore her. She doesn’t know what she’s talking about."

    scene stillcalm10
    with dissolve

    no "The fact of the matter is, I have no idea who would have something against me. I just couldn’t handle the idea of being apart from Sensei for an entire day."
    no "And seeing as you always have a much better time when he’s around as well, I figured I’d try keeping him here for as long as he’s able to stay interested."

    scene stillcalm11
    with dissolve

    no "Quick, Futaba. Remove your blouse. That will keep him grounded."
    f "I am not removing anything, Nodoka. "
    no "Not even for me?"
    f "{i}Especially{/i} not for you. Stop assuming everyone is bi."
    no "I bet {i}Rin{/i} would take off her blouse for me."
    f "She has. You have literally worn her clothes."

    scene stillcalm12
    with dissolve

    no "Oh, you’re right."
    no "..."
    no "I should probably return her underwear."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene stillcalm13
    with dissolve2

    c "...and that’s exactly why I think you guys should have matching outfits! "
    c "They obviously don’t need to be, like...{i}identical{/i} or anything. But tons of girl-bands do it and it’s a great way to rope in fans."
    n "Yeah, but like..."
    n "We haven’t even written a song yet."
    c "So what? It doesn’t need to be {i}now.{/i} I just mean eventually."
    n "Yeah, but like..."
    n "Sana can’t even reach the bass pedal yet."

    scene stillcalm14
    with dissolve

    c "Hm..."
    c "..."
    n "..."
    c "I guess my first course of action should be finding a shorter stool then."

    play sound "slidedoor.mp3"
    scene stillcalm15
    with dissolve

    c "Oh, Yumi! You’re here earlier than normal today. How was spending the night with Chinami?"
    c "She texted me saying you were acting a little weird and-"
    y "It was great."
    y "I had a good time."

    scene stillcalm16
    with dissolve

    c "Uhh...did you? Because you seem a little out of it."
    c "If you didn’t sleep well, maybe you should head back home and get some rest. It’s not like Sensei is going to mark you absent or anything."

    scene stillcalm17
    with dissolve

    c "Besides, Imani has been fending off Kirin all day, so she probably won’t even notice you’re-"
    y "Sorry. Hold that thought."

    scene stillcalm18
    with dissolve

    c "Umm...Yumi?"
    n "Uhh..."
    n "Chika?..."
    n "I’ve got a really bad feeling about this."

    scene stillcalm19
    with fade

    f "And...what about for this one? Is it the same thing?"
    no "Correct. You have to figure out the values to make the denominator equal to zero. After that, it’s just rewriting the fraction and canceling out any like factors."
    no "Did Sensei really never teach you this? What has he been doing the whole year?"
    f "Sleeping..."
    f "And flirting..."
    f "And sleeping..."
    no "Wow. What a life."
    y "Good morning, Einstein."

    scene stillcalm20
    with dissolve

    no "Uh-oh."
    f "Oh. Good morning, Yumi. Do you need any help with the math homework that-"

    scene stillcalm21
    with dissolve

    y "Sure! Could you give me just one second, though? There’s something I’ve gotta take care of first."
    f "What?..."
    f "Why are you-"
    no "It’s been nice knowing you, Futaba. Please remember me as the girl who taught you how to properly handle rational expressions."

    stop music
    play sound "static.mp3"
    scene stillcalm22
    with flash
    stop sound
    with hpunch
    play music "thingsthathurt.mp3"

    y "You think this is a fucking joke?!"
    y "You think you can just walk all over people like that?! "
    f "Yumi, stop! Leave her alone!"
    y "You happy you took shit into your own hands?! Was it worth it?! Was it fucking worth it?!"
    o "What’s...wait, is that Nodoka down there?! What the fuck happened?!"
    ima "Senpai! We’ve got a bit of a situation over here! "
    s "..."
    y "You think I’m a fucking joke?! That I deserve shit like that because of what I’ve done in the past?!"
    y "You think I don’t fucking regret it?!"
    y "Fuck you! Fuck you, fuck you, fuck you!"
    mo "Kendo Princess! Attack formation! The only one who can defeat the demon lord is you!"
    c "Yumi?!?! What the fuck are you doing?! Get off of her!"
    y "Eat shit and fucking die! No one embarrasses me like that! No one!"

    play sound "static.mp3"
    scene stillcalm23
    with flash
    stop sound

    f "Oh my God...Oh my God..."
    r "What happened?! I didn’t even realize Yumi walked in!"
    o "This..."
    o "This isn't because Nodoka stood up for Futaba in class a while back, is it?..."
    o "Is that seriously all it takes to set this girl off?"
    ima "Senpai! Why are you just standing there?! What are you doing?!"

    play sound "static.mp3"
    scene stillcalm24
    with flash
    stop sound
    with hpunch

    y "I told you I’d fucking kill you, didn’t I?! I fucking...told you!"
    mi "Jesus, Yumi! Give the damn girl a break! Ain’t she had enough?!"
    y "No! There’s never...too much for...people like her!"
    y "People who...get a rise out of...hurting others!"
    r "Oh, yeah. That’s rich. Yumi calling people out for hurting others. "
    o "What the fuck has Nodoka ever done to anyone?"
    f "Yumi! Stop it! Please!"
    ki "Is she unconscious? It doesn’t even look like she’s moving anymore."
    mi "Hang in there, Nodoka! We’re all rootin’ for ya! Even if...ya might be dead already!"
    y "I fucking hope she is! She deserves it! She fucking deserves it! She fucking deserves-"

    play sound "static.mp3"
    scene stillcalm25
    with flash
    stop sound

    ima "Okay! That’s enough of that! You’re done!"
    t "Bullying will not be tolerated. You are lucky you are leaving here with your life."
    y "Let me go! Let me go! I ain’t fuckin’ done yet! "
    mak "I’m so disappointed in you, Yumi...it really seemed like you were getting better..."
    y "Fight me back, you cunt! Fight me the fuck back! Now’s your fucking chance!"
    ki "Now {i}would{/i} be her chance if you didn’t knock her the fuck out already. That was barely even a fight."
    mi "Yeah...Yumi just straight up tried to kill Nodoka when all she was doin’ was helpin’ Futaba study. I saw the whole thing."
    a "If only Ayane was here today. She could have taken Yumi. Right, Maya?"
    m "Please don’t get me involved in this. I would very much like to avoid saying anything that may paint a target on {i}my{/i} back as well."
    y "Get the fuck up, you bitch! We’re not done! We’re not even close to done, you hear me?!"
    y "I’ll fucking kill you! "
    y "{b}I will fucking kill you!{/b}"

    scene black
    with dissolve2

    "Imani and Tsuneyo manage to pull Yumi back to her feet and lock her arms behind her back so she can’t wreak any further havoc."
    "As for why I remained inactive..."
    "Well, you probably already know."
    "I {i}understand{/i} what Nodoka did."
    "I was {i}there{/i} for it."
    "But it’s not like I can come out and say anything about it because that would make me complicit."
    "The fact that I was there and didn’t do anything to stop it makes me almost as bad as her."
    "It’s just a shame that it won’t look that way to anyone but the three of us..."
    "And that Yumi’s delinquent persona, which she’d been slowly chipping away at over time, is suddenly covered with a {i}new{/i} layer of stone, even harder than the one before it."
    "I remain unmoving, experiencing the secondhand fallout of lecherous misdeeds, still in disbelief that something like this will ever happen to me."
    "Not because I don’t deserve it, though."
    "But because I’m far too powerful to be brought down by a single teenage girl-"
    "And much more used to bringing them to their knees instead."
    "........."
    "......"
    "..."

    scene stillcalm26
    with dissolve2

    s "..."
    y "..."
    ima "You really weren’t kidding when you said you were leaving the class to {i}me{/i} today, huh?"
    ima "We’re lucky Tsuneyo was around. Because with you deciding to turn into a statue at the worst possible time, I would have been left to fend for myself without her. And this girl is fucking strong, dude."
    ima "Why didn’t you help? You could have pulled her off by yourself."
    s "I-"
    y "Does it fucking matter? You got me off of her. Now just take me down to the principal’s office so I can get expelled or whatever."
    y "I’m done with this shit anyway."

    scene stillcalm27
    with dissolve

    ima "Hah...yeah. I guess now probably isn’t the best time to talk about this. "
    ima "I don’t know if you’re going to get {i}expelled{/i} for this, Yumi...But, at the very least, I doubt you’ll be coming here for a while."
    y "Best news I’ve heard all fuckin’ year."
    t "How many more people will be hurt under your supervision?"
    t "You should be ashamed of yourself."
    s "That’s-"

    scene stillcalm28
    with dissolve

    c "Yumi! What the fuck was that?!"
    c "You were doing so well! You apologized to Futaba! You joined a club on your own! I was so proud of you!"
    c "But...this?!"
    c "How can I be proud of {i}this?!{/i}"
    c "What if something like this happens around Chinami?! What if you decide to snap when I’m not around?! Then what?!"

    scene stillcalm29
    with dissolve

    y "Please..."
    y "Just take me to the fucking office already..."
    c "Yumi..."
    ima "You heard her, Tsuneyo. Let’s get our little prisoner to the principal’s office and hope Sensei has a damn good excuse when we make it back to the classroom."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene stillcalm30
    with dissolve2

    n "Nodoka...you doing okay? I’ve got a whole stash of painkillers in my bag and you look like you could use...a few hundred of them."
    mi "Get up slowly. And if ya feel like yer fallin’ asleep, do your best to...not do that. Wouldn’t be surprised if ya had a concussion at this rate."
    ki "Straight up, I seriously thought you were going to die. So kudos to you for actually living through that."
    no "Heh..."
    no "Heheheh..."
    ki "..."
    ki "Is she seriously laughing right now?"
    mi "Could be brain damage. Wouldn’t be surprised with how many times she got clocked on the head."
    n "I don’t have any pills for that, but ibuprofen works for pretty much anything, so who even knows?"

    scene stillcalm31
    with fade

    o "Sensei, Rin and I are gonna take Nodoka to the nurse’s office."
    r "And, uhh...if you see Futaba...maybe try cheering her up a little? "
    r "She ran out of the room really shaken up once Nodoka started waking up and...probably went back to the dorm. But, just in case she didn’t...you know what to do."
    s "Sure, yeah."
    s "And, uhh...how are you holding up, Nodoka?"
    no "Heheh..."
    no "Heheheheh..."
    no "Sensei..."
    no "It was worth every last punch..."
    s "..."
    no "If getting hit like that...allows me to be the meat of a lesbian sandwich...I should get into fights more often..."

    scene stillcalm32
    with dissolve

    o "Okay. Tell it to the nurse, Rocky. "
    r "The nurse is actually out on Fridays, Otoha. You and I are going to have to take care of Nodoka ourselves."
    no "Wow...today keeps getting better and better..."

    scene black
    with dissolve2

    "Otoha and Rin walk Nodoka out of the classroom, leaving all of their possessions (Including one very bent pair of glasses) behind."
    "The class erupts into a fit of chatter once the door slides closed again as they all begin to discuss what could have caused this."
    "The general consensus is, unsurprisingly, that Yumi is just unhinged."
    "And that this was bound to happen sooner or later."
    "And that they’d be shocked if she’s ever allowed back in school."
    "About how no one ever really liked her anyway."
    "And about how she’s a terrible person with a fetish for tearing others down..."
    "And does what she wants whenever she wants to do it..."
    "And thinks so highly of herself that she won’t even bother showing up to school..."
    "But it’s all wrong."
    "They don’t understand her like I have begun to."
    "And the only person beside me who can actually tell them about her is too busy blocking the incessant chatter out with her hands pressed to her ears and tears streaming down her cheeks."
    "Out of my peripheral vision, I manage to find the only other silent observer in the room right now."
    "And it is at that moment when I realize just how accurate her premonition was."

    scene stillcalm33
    with dissolve2

    s "Well..."
    s "Looks like the “whispers of the world” weren’t lying."
    s "Something bad happened after all."
    s "I’m sorry for doubting you. I just didn’t-"
    ya "That wasn’t it."

    scene stillcalm34
    with dissolve

    s "What?"
    ya "That wasn’t it."

    $ renpy.end_replay()
    $ nodokaspecial20 = True

    scene black
    jump sadgirls1

label nodokaspecial30p1:
    scene sky
    with dissolve2
    play music "icantseeher.mp3"

    "It’s a perfectly normal morning."

    play sound "phonering.mp3"

    "But it isn’t perfectly normal for long as the first thing I see when I step outside (Apart from an obnoxiously blue sky) is a name on my caller ID I am not yet prepared to deal with this early in the morning."

    play sound "phonebeep.wav"

    "And yet I tap on the answer button as my breakfast today was small and gorging myself on attention might assist in making up for that."

    s "Good morning, Nodoka."
    no "And good morning to you as well, Father. "
    s "I am not your father."
    no "But wouldn’t it be great if you were?"
    s "Not really, no. One semi-daughter is enough for me. And I'm sure Ami is a much better cook than you anyway."
    no "Unfortunate. But tell me, do you have anything planned for the rest of the day? And perhaps tomorrow as well?"
    s "Am I being invited to something?"
    no "You are. And I solemnly swear it will not be a locker room this time."
    s "Is this another set-up? "
    no "Why, yes. But it’s also not what you’re thinking."
    no "You see, I’ve decided to play matchmaker this morning and set up my roommate with Rin as it has been far too long without the two of them engaging in coitus and the lesbian energy is burning a hole in my brain."
    no "And, this may come as a surprise to you, but I just so happen to need my brain for brain stuff."
    s "You realize you aren’t exactly playing “matchmaker” if the two of them are already together, right?"
    no "I suppose. But I’ll take it as a win so long as one of the two winds up with a tongue inside of them tonight. And no, I am not referring to the one that already lives inside of their mouths. "
    s "Weird. But why do you need {i}me?{/i}"
    no "So I don’t wind up as a third wheel of course."
    no "Additionally, there’s a bit of a detour we need to take on the way to hopeful lesbian intercourse and it’s one I’d thoroughly enjoy having you there for. "
    no "How quickly can you make it to the station near our school?"
    s "I haven’t even said yes yet. "
    no "Then I will say it for you. {i}Yes.{/i} Now, how quickly can you make it to the station near our school?"
    s "Nodoka-"
    no "Excellent. We’ll wait there, then."
    no "I look forward to seeing you, Sensei. "
    no "Just as you should look forward to what {i}you{/i} will see."

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve2

    "Nodoka hangs up the phone and...it looks like I don’t have much of a say in what I’m going to do today."
    "As I make my way to the station, I wonder what sort of push is necessary to get Rin and Otoha to finally take the next step in their relationship."
    "There’s a tinge of jealousy of course as I, regretfully, won’t be involved. But more than anything, there’s an overflowing curiosity of what Nodoka plans to do in order to enable this."
    "Being a male, I’m obviously no expert when it comes to lesbian relationships, but I’m pretty sure most of them don’t require a team of onlookers in order to kick off."
    "There’s really no point in thinking about any of this. These are all just thoughts I use to occupy the blank space in time between places A and B."
    "Not just because the world will move regardless of whether or not I want it to-"
    "But because Nodoka is always so many steps ahead of me that I can never figure out what she’s plotting to begin with."
    "........."
    "......"
    "..."

    scene nodokatrain1
    with dissolve2

    "Upon arriving at the station, I am greeted by two surprised expressions and one oozing a disturbing sense of both pride and accomplishment."

    o "Sensei? What are you doing here?"
    s "Good question, Otoha. Ask your roommate."

    scene nodokatrain2
    with dissolve

    o "Nodoka, what-"
    no "I invited him, of course. Three is such an odd number, don’t you think? And quite literally at that."
    no "Four is much more balanced. {i}Plus{/i} it prevents me from becoming a third wheel."
    r "How would you be the third wheel when you’re the one who invited us? Otoha and I are only coming along because we want to support you."
    s "Support her in what? I still don’t know what we’re doing."

    scene nodokatrain3
    with dissolve

    r "Nodoka’s new book just came out a week ago and she’s doing a signing downtown today. "
    o "Neither one of us have read it, but we were promised free food and didn’t have anything else to do, so...yeah."
    s "So I take it this “detour” she mentioned on the phone is the main event after all?"
    no "Well, excuse me for being humble. You wouldn’t have come along if I’d done nothing but toot my own horn over the phone and, as my surrogate father, I wanted you to be here for this."
    no "I think you’ll come to be quite proud of me by the end of the day, Sensei."
    s "So, the goal was to make me proud and {i}not{/i} that other thing you said on the phone?"

    scene nodokatrain4
    with dissolve

    no "Can it not be both?"
    r "I’m confused. What did you tell Sensei on the phone?"
    s "It’s probably best for everyone if we didn’t talk about that."
    o "Welp, that about answers that question. I suddenly know where this is going. "
    o "I just kind of figured with today being, you know, an actual big event for you that you had a different {i}motivation{/i} in mind this time."

    scene nodokatrain5
    with dissolve

    r "Am I seriously the only person who doesn’t know what’s going on right now?"
    o "It doesn’t matter at the end of the day. We already signed up for this and I’d feel weird backing down on supporting Nodoka just because she is {i}once again{/i} thinking...Nodoka things."
    r "We’re still getting free food, though...right? Because if that was a lie, I’m going to punch someone. And process of elimination says that person would have to be Sensei."
    s "How? Why? No."
    o "Don’t even worry about it, Rin. Look at it this way — Sensei being here means that the two of us can hang out more and that the two of {i}them{/i} can keep having their weird...father-daughter thing. "
    s "Why is everyone so set on making me Nodoka’s dad?"
    no "Don’t I look cute in this suit, Papa? Don’t you want to just tear it off and play with me before Mommy comes home?"
    s "Yes, but that is beside the point."

    scene nodokatrain6
    with dissolve

    no "It doesn’t {i}have{/i} to be..."
    o "And on that note, I’m walking over to the platform. Rin, if you’d be so kind as to accompany me?"
    r "Sorry, Sensei...Duty calls. Enjoy your daughter, though."

    scene nodokatrain7
    with dissolve

    no "Shall we head out as well? Or do you want to wait for the next train and give the two of them some breathing room?"
    s "Don’t you have a book signing to get to? I figured you’d be in a rush."
    no "It’s {i}my{/i} signing. It’s not as if they can do it without me. Besides, I have plenty of readers who’d sit there for days while waiting for me. I’m kind of a big deal."

    scene nodokatrain8
    with dissolve

    no "Look- I’ve got a purse and everything. There isn’t even anything in it. I am literally only carrying this because it makes me look the part."
    s "Nodoka, be honest. Why did you want me here for this? You’ve never shown me {i}any{/i} of your writing before. Why do you {i}just now{/i} want me to be “proud” of you? That can’t be it, right?"

    scene nodokatrain9
    with dissolve

    no "Maybe I’ve fallen for you?"
    s "Are you even capable of that?"
    no "Who knows? Maybe we’ll find out today."
    s "Nodoka-"
    no "A good author won’t just explain the plot, Sensei. A good author lets the reader find out on their own."
    no "If you want to know what it is I want...or what I’m hoping to gain by dragging you along with me, why not just spend a little more time reading?"
    no "You might like what you find."
    s "You and these damn book metaphors."
    no "The train is here. Are we leaving or not? "

    scene black
    with dissolve2

    s "Fine, come on. But I can’t guarantee I’ll like whatever it is you’re trying to get me to {i}read.{/i}"
    no "You don’t have to like it. "
    no "You don’t even have to {i}get{/i} it."
    no "You just have to be there."

    "........."
    "......"
    "..."

    scene nodokatrain10
    with dissolve2

    "Despite being pressed for time, Nodoka takes it upon herself to grab a quick cup of coffee from a kiosk near the platform and the two of us just barely make it onto the train before it departs."
    "Thankfully, there’s enough room for us to grab seats almost directly across from Rin and Otoha, but neither one of us pay them any mind as we don’t want to interrupt anything. "
    "Even if the “detour” I was advised of is today’s primary objective, it would still be nice if we’d be able to force the two of them a little bit closer together."
    "I say {i}we{/i} as if I play any part in this when, in all actuality, I know I’m only here to keep Nodoka entertained."
    "But, I suppose that goes both ways."
    "Because even if she occasionally does things that shock and appall me, I’m no different."
    "If anything, I’m worse."
    "She knows this."
    "She knows this, yet she still smiles at me like that."

    no "Would you like a sip of my coffee, Sensei? Act now and you’ll be able to steal a bit of my saliva before it dries up."
    s "I’m good. There are better and less caffeinated ways to obtain your saliva if I really want to."
    no "Do you think you’ve saved up enough points for that?"
    s "Depends. How many do I get for joining you today?"

    scene nodokatrain11
    with dissolve

    no "I wonder. It’s been so long since I awarded any that I’m not quite sure what their value is anymore."

    scene nodokatrain12
    with dissolve

    no "Let’s just say you’ve earned enough for either a kiss or some light groping and we can call it a day?"
    s "Is that redeemable on the train?"
    no "It’s redeemable anywhere you please. Though, I can’t guarantee your reward won’t be cut short by angry passengers if you make a redemption right now."
    s "I’ll hang on to this intangible coupon for the time being then. I’m looking forward to finding out that it expires roughly thirty seconds from now."

    scene nodokatrain13
    with dissolve

    no "Unfortunately, it expired in the middle of that sentence. Too bad. And here I was starting to get a little turned on."
    s "So, this book you just released-"
    no "Changing the subject as soon as I admit my arousal? How rude. "
    s "You’re always aroused. I’ll have plenty of more opportunities to ask about that in the future."

    scene nodokatrain14
    with dissolve

    no "You’ve had plenty of time to ask about my writing as well. And yet, here we are — violently penetrating a series of underground tunnels until we’re spewed out on the other side."
    s "Leave it to you to sexualize trains, I guess."
    no "Anything can be sexualized if one tries hard enough. And any hole can be penetrated with enough persistence and force. Which isn’t to say one {i}should{/i} penetrate all holes, but-"
    s "Tell me more about your writing. What’s this book about?"

    scene nodokatrain15
    with dissolve

    no "That’s a good question. What {i}is{/i} this book about?"
    s "I feel like that’s something you should probably know as the author."
    no "By conventional means, sure. But when one literary work contains so many different ideas, it’s near impossible to simply {i}explain{/i} what it’s about, isn’t it? It’s something that must be experienced."
    s "That is probably one of the most pretentious things I’ve ever heard."

    scene nodokatrain16
    with dissolve

    no "Let’s just say it’s about the folly of man. Or the pleasures in struggling."
    s "Sounds boring."
    no "You don’t read much anymore, do you? "
    s "I don’t read {i}at all.{/i} Though, I can’t quite remember when I ever did in the first place."
    no "I imagine you stopped around the same time you stopped writing. To which I’d say, “how sad.”"
    no "There’s a great deal you’re missing out on by living the life you lead, Sensei. But, at the same time, I know there must be plenty you experience that you’d {i}never{/i} be able to pull from the pages of a book."
    no "Perhaps learning about my latest work will be the call to action you need to get back into the literary world? It’d be wonderful to have a partner there, you know."
    s "Is Futaba not enough of a partner for you?"
    no "Futaba is a darling and I would kill for her. But we both know she’s nowhere remotely close to the level {i}we{/i} are."
    s "How do you even know my level? You’ve never read anything I’ve written. In fact, I don't think {i}I’ve{/i} ever read anything I’ve written."
    no "Hmm...intuition, perhaps?"
    no "Or maybe I’m secretly a beloved fan of yours who’s been following you ever since I was a little girl? Desperately awaiting the day her favorite writer returns to the game?"
    s "That would...actually explain a lot. But I doubt that’s the case."

    scene nodokatrain17
    with dissolve

    no "It would have been interesting if it were, though."
    no "Unfortunately, life is far too mundane to be filled with fun coincidences like that."
    s "Is that why you got into writing in the first place? You were too...bored with life or whatever?"
    no "Mmm...no. No, I don’t believe that’s what it was."
    no "While it may be true that my days lack in color, they’ve always made up for that in...hmm...how should I put this?"

    scene nodokatrain18
    with dissolve

    no "Incontrovertible peculiarity?"
    s "I’m going to need you to elaborate."

    scene nodokatrain19
    with dissolve

    no "Let’s just say I’ve lived a life that not many would understand..."
    no "And that the reason I’m so obsessed with books is that there was someone before me who may have inadvertently caused me to...inherit that interest."
    s "I’m going to need you to continue to elaborate."
    no "Would you believe me if I told you I came from nothing?"
    s "As in...you were poor?"
    no "Perhaps it’s better if I don’t attempt to explain things at all. It’ll only make me appear insane."
    s "Nodoka, essentially everything you do makes you appear insane. An explanation of your childhood won’t tip the scales."

    scene nodokatrain20
    with dissolve

    no "Then why don’t you go ahead and picture younger Nodoka as a little amoeba — feasting on tiny aquatic plants to keep herself sustained and protected from the big, scary world?"
    no "Or a cute little tardigrade — clinging to a patch of grease in your kitchen sink that you’ve neglected to clean over the past several weeks?"
    s "I’m going to picture you as neither of those things because you are a human being."
    no "That I am. And an interesting one at that. "
    no "But before I was human, I hadn’t even been a thought."
    no "To this {i}day,{/i} I am not a thought. I am a girl who simply {i}is.{/i} And I will continue to {i}be{/i} because I can’t {i}not.{/i} Do you understand?"
    s "No."

    scene nodokatrain21
    with dissolve

    no "Exactly. "
    no "There are things in this world that are beyond comprehension. "
    no "But what if I told you there was another one outside of it?"
    s "Another...what? Another world?"
    no "An infinite amount of them. Each one remarkably different from the next. And that some things are only impossible to comprehend because we’re not {i}meant{/i} to comprehend them."
    no "What if we’re meant to be somewhere else?"
    no "What if {i}this{/i} world is just a mistake?"
    s "Then...we live with it, I guess. There’s not really anything else we can do, is there?"

    scene nodokatrain22
    with dissolve2

    no "But what if there {i}is?{/i}"
    no "What if we {i}can{/i} go somewhere else? "
    no "What if someone has {i}been{/i} somewhere else but everyone thinks they’re crazy and no one believes them because the idea of another world layered on top of this one is absurd? It’s insane. It’s impossible."
    no "If we found it, would they believe us then? "
    no "If we could replicate or emulate or simulate another world, would they believe us {i}then?{/i}"
    no "Or would we be forced to suffer in silence because it’s all too {i}incomprehensible?{/i} What happens if we find it? What happens if we go there? How do we get there?"
    s "..."
    no "How."
    no "Do."
    no "We."
    no "Get."
    no "There?"
    s "..."
    no "..."

    scene nodokatrain23
    with dissolve

    no "So yeah. That’s basically why I started writing."
    s "That..."
    s "That didn’t tell me anything at all."

    scene nodokatrain24
    with dissolve

    no "Sure it did."
    no "You’re just not meant to get it yet."

    scene black
    with dissolve2

    s "It seems to me like that was just an overly-convoluted way to dodge the question. But hey, if you don’t want me to know, that’s fine. I like keeping my affairs private too."
    no "That’s just the thing, Sensei...I {i}do{/i} want you to know. "
    no "It’s just impossible to believe as none of it is based in logic. It’s just something that {i}is{/i} because it {i}is.{/i}"
    no "It’s a {i}feeling.{/i}"
    no "But it’s a feeling that moves me."
    no "It’s the {i}only{/i} thing that moves me."
    no "And that’s exactly why I need to figure out how to make you understand."
    no "I need to figure out how to make {i}all{/i} of you understand. "
    no "If I can’t, my existence means nothing."
    no "And I will return to what I was in the beginning."
    no "I won’t even be a thought."

    "I lean back in my seat and let the rest of the ride go by in silence — but it’s not because I’m confused or shocked. "
    "It’s because, for some reason beyond {i}my{/i} comprehension as well-"
    "I believe her."
    "I wish I could tell you why."

    $ renpy.end_replay()
    $ nodokaspecial30p1 = True
    $ nodoka_love += 1

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump nodokaspecial30p2

label nodokaspecial30p2:
    if _in_replay:
        play music "icantseeher.mp3"

    scene noonsky
    with dissolve2

    r "So, how far away is this book store thingy?"
    r "Wait...your signing {i}is{/i} at a book store, right? Because I have a library book I’ve been holding onto for five years now and I get nervous any time I have to go inside one."
    r "They’re onto me. I know they are."
    o "Does...Futaba know about this?"
    r "No. And she never will, so keep your mouth closed."
    no "Hmm...I believe the venue is about a quarter mile away. But if it’s alright with you, I’d like to make another quick detour for more coffee."
    s "You are literally holding a cup of coffee right now."
    no "That I am. And if my calculations are correct, which they always are, I’ll be finished with that coffee by the time we arrive at the next shop."
    s "You have an addiction and you need help."
    no "As do you and no one ever tries to rehabilitate {i}you.{/i}"
    r "That’s because Sensei’s addiction keeps a bunch of girls from going crazy and rubbing up against stuff. Yours just keeps you awake."
    o "Ew. To the girls part. Not the awake part."
    r "I’m a girl. You’re a girl. Nodoka’s probably a girl. Are you saying we’re all gross as well?"
    o "I’m saying I don’t want to have a casual conversation about our teacher’s sex addiction. Are we getting coffee or not?"
    no "We are. But I must first take another detour to {i}rub up against stuff{/i} as Sensei’s sickness hasn’t spread to me yet and I’m beginning to get a little crazy. "
    r "Beginning? You’re already batshit insane. Sensei, I don’t want to take another detour. Can you just, infect Nodoka really quick or something? Thanks."
    s "No thanks. I’m sure I {i}could,{/i} but I’m afraid of what I’d catch from her."
    no "You’d catch nothing but a good time. Come to me, Father. Infect me with your desire. Make me {i}sick.{/i}"
    o "Pretty sure the only one getting sick here is me..."

    scene black
    with dissolve2

    "No one becomes infected, but Nodoka does manage to obtain another cup of liquid courage that she carries along with her to the venue (Which, luckily for Rin, is {i}not{/i} a library but a very large bookstore.)"
    "Upon entering, I’m shocked to see just how many people turned up. And, while I’d love to be able to tell you that many of them are just here to shop...that doesn’t seem like the case."
    "Nodoka is recognized immediately and pulled away from our group so that she can get set-up at a table on the second floor of the shop, leaving the rest of us to awkwardly look around for something to do."
    "Carefully and slowly, we make our way through the crowd and manage to scope out a small space of unoccupied standing room that we quickly claim as our own."
    "Thanks to my height, I’m able to see over the crowd, but the same can’t be said for Rin and Otoha who struggle to stare between the gaps in onlookers."
    "There’s something bothering me, though. "
    "I can’t seem to go five seconds without someone looking at me and whispering to their friends or partner about something."
    "Rin and Otoha catch onto this well, but don’t appear to understand why either."
    "It makes me very uncomfortable."
    "I never fit in anywhere to begin with, but drowning in this sea of inaudible gossip is starting to drive me-"

    anno "Attention, please. Today’s Q&A panel is about to begin."
    anno "Please keep all questions brief and do not interrupt one another while someone is speaking. "
    anno "We understand just how many of you are passionate about the first installment of this new series, but we urge you to remain calm and collected as Miss Nagahara speaks."
    anno "Repeat offenders will be escorted out of the venue and banned from attending any future events both related to and {i}unrelated{/i} to today’s author."
    anno "With that said, on behalf of the Kumon-mi Literary Committee, I’d like to thank today's guest for appearing and urge all of you to provide a very warm welcome...to S.A. Nagahara!"

    play sound "cheer1.mp3"
    scene nodokabooksign1
    with dissolve2

    "The crowd erupts into a fit of applause as Nodoka- or, excuse me, {i}S.A. Nagahara{/i} takes her seat at a table stacked with copies of what I can only imagine is her latest book."
    "Her composure and refusal to stop the crowd from applauding signals to me that she’s done this before, and I’m surprised to see just how well-established she is for her age."
    "Though, if she’s going to lie about her name, I’m sure that most of the people in this crowd are unaware of how old she really is in the first place."

    stop sound fadeout 5.0

    "The applause slowly dies down and, as it does, Nodoka’s eyes open."

    scene nodokabooksign2
    with dissolve2

    no "Wooooow...quite the turn-out we have today, isn’t it?"
    no "I suppose trying something a little different was worth it after all."
    no "You flatter me. You really do."

    scene nodokabooksign3
    with dissolve

    no "Now, let’s see..."
    no "Normally, this is the part where I’d give a brief synopsis of the book. Maybe a little background information about how it came to be or {i}why{/i} it came to be, but..."
    no "Frankly, I don’t see why that would be necessary given that you’re already {i}here,{/i} aren’t you?"

    scene nodokabooksign4
    with dissolve

    no "You would not {i}be{/i} here if you didn’t already know what this book was about."
    no "You would not {i}be{/i} here if you weren’t already curious about the characters or the story...or what will come next."
    no "And so, perhaps it would be in everyone’s best interests if we skipped right over the formalities and just opened the floor."

    play sound "cheer1.mp3" fadein 2.0

    no "What do you say?"

    "The crowd erupts again and, while it’s certainly loud and obnoxious, it takes some of the focus off of me."
    "And I’m thankful for that."

    no "Go on. Raise your hands. You know how this works."

    scene nodokabooksign5
    with dissolve
    stop sound fadeout 4.0

    "The hands go up and the volume goes down."
    "Then, almost mechanically, Nodoka begins moving through the audience one by one."

    no "Hmm...you. In the shirt. What would you like to know?"
    nf1 "Well, first off, I’d like to thank you for deviating from your typical formula and branching out into something far surpassing what the typical reader would call “taboo.”"
    nf1 "Which is saying a lot for an author who hasn’t shied away from including sex scenes containing literal farm animals."
    no "We all know what really happens on farms. I’m not one to shy away from the truth. But what is the question?"
    nf1 "The question is...why a school?"
    nf1 "There are so many other books and media series focusing on schools and, up until now, you’ve always seemed to challenge standard conventions and cliches."
    no "Are you calling my latest work cliche?"
    nf1 "Not at all! I-"

    scene nodokabooksign6
    with dissolve

    no "I’m kidding. There’s no need to get flustered. It’s a good question."

    scene nodokabooksign7
    with dissolve

    no "I suppose the easiest answer would be...that a school simply is the perfect setting to facilitate the type of story I wanted to tell and the themes I wanted to explore."
    no "Anyone could mimic Nabokov. There are more “Lolita” clones than one can count — and it was not my goal to follow the same steps that many before me have tripped over."

    scene nodokabooksign8
    with dissolve

    no "But when you want to create an entire well of debauchery — a haven for misdeeds even, there is no better place to look than where the innocent gather most."

    scene nodokabooksign9
    with fade

    no "Next question...You. In the other shirt."
    nf2 "Th-Thank you! Huge fan! I’ve been following you since “Every Day I Grow Some More!”"
    no "Aww, you flatter me. What’s your question?"
    nf2 "M-My question is...how confident are you in ending a series with so many prospective love interests?!"
    nf2 "Up...Up until now, you’ve always cited “Why choose?” as a lazy, uninspired book trope! Have...Have you changed your opinion?!"
    no "I have not. And, to be quite honest, I’m not too concerned with how the story will end at this point in time."
    no "What we have in “The Light of Last Summer” is not a run of the mill romance. In fact, I struggle to call it {i}romance{/i} at all."
    no "It’s an in-depth character study of a large group of flawed and misguided individuals who, for the most part, do not {i}deserve{/i} love."
    no "I’m sure you’d all agree that I am {i}very{/i} good at what I do. But there is no conceivable way for {i}any{/i} author to believably end a series with {i}this{/i} many pairings in a way that is good for all of them."
    no "Some of the students will have to suffer for others to prosper. And in the prospering of those others, the sorrow in the background is sure to leak into everything else."
    no "No one can win, and I believe that is evident even this early on in the series."
    r "Is it just me or...does Nodoka’s new book sound a lot like..."
    o "It’s not just you."
    o "That’s exactly what it is."
    s "..."

    scene nodokabooksign10
    with fade

    no "You. In the third shirt. Question?"
    nf3 "Yes! Hi! Uhh...let’s see..."
    nf3 "I actually have two questions."
    no "No you don’t. Pick one."
    nf3 "Just one? Uhh...okay...umm..."
    nf3 "Is there a reason the main character seems so...closed off? He’s written well, but without any background information {i}at all{/i} in the first book, he seems like more of an...afterthought than anything?"
    no "Does he? Because {i}I{/i} think he’s plenty interesting even without any of that."
    no "It takes a very special type of person to groom and manipulate an entire class of underage girls. It takes someone {i}sick.{/i} And most people catch their sicknesses from someone else."
    nf3 "Are you saying...the protagonist is only like this because someone else corrupted him?"
    no "I’m saying you should spend more time thinking about the implications of a character’s actions rather than their motivations for doing so. Unless you want to be bored, that is."
    no "Any wannabe-psychologist could sit down with a pen and paper and try to tell you about {i}why{/i} people act the way they do."
    no "But with so many of our decisions not based in science or logic but a spontaneous impulse or thought, what matter does motivation carry? If you ask me, none."
    no "It matters not {i}why{/i} someone does the things they do. What matters is what spawns from that. And to me, it’s far more fun to predict the future than to analyze the past."
    nf3 "T-Thank you, Miss Nagahara! But if you wouldn’t mind-"
    no "Fine, fine. What’s your next question?"
    nf3 "There’s, umm..."
    nf3 "There’s a lot less...{i}girl on girl{/i} action in your new book. I just wanted to know if-"
    no "It’s coming. Don’t worry."
    no "And it’ll be sooner than you think."

    scene nodokabooksign11
    with fade

    nf3 "Thank you so much! I’m looking forward to reading it!"
    no "Not as much as I’m looking forward to {i}writing{/i} it."
    r "Heheh...heh..."
    o "{i}Hah...{/i}"
    o "You know, this is what we get for not reading her book. We could have avoided this."
    r "Heh...heheh..."
    no "You. In the shirt without sleeves."

    scene nodokabooksign12
    with fade

    ri "Aren’t you the girl who hit on me at the bar on Halloween?"
    no "Hmm...did I do something like that? That doesn’t sound like me. I’m very reclusive."
    ri "No, I’m pretty sure it was you. Also, aren’t you in high school? I’m pretty positive I’ve seen you around the dorms."
    nf1 "Aren’t you a grown woman? What are you doing hanging out in high school dorms?"
    nf2 "Oh my God! It’s just like the book!"

    scene nodokabooksign13
    with dissolve

    ri "Hey, it’s not that weird! I live there! Of course I’m going to see some girls hanging around!"
    nf1 "Talk about being a fanatic. This woman’s literally trying to become the main character of the book. She’s missing the point entirely."
    ri "I don’t even know this book! I just saw a line and got into it! I do that sometimes!"

    scene nodokabooksign14
    with fade

    r "Why is my mom here?! I barely saw her at all these last couple years and now it’s like I can’t even get away!"
    o "On the bright side...at least she’s not reading Nodoka’s books?"
    r "Mom! Go home!"
    ri "Rin! Hey, Rin! Tell everyone how it’s not weird for me to live in the dorms with you!"
    r "It totally {i}is{/i} weird! You should leave! I want my life back!"

    scene nodokabooksign15
    with fade

    nf4 "Hey, wait...is that group cosplaying?"
    nf5 "Oh my God! I think they are! That’s almost exactly how I pictured Sensei in the book!"
    nf4 "We have to take his pants off to know for sure...I look kind of like Haruhi, don’t I? Do you think he’ll do it with me? I can pretend I have a husband and everything."
    nf5 "Oh! And those girls with him must be Ren and Otoka! Do you think they’re his daughters?"
    nf4 "I don’t know, but I suddenly want them to kiss!"
    nf6 "Kiss! Kiss! Kiss! Kiss! Kiss! Kiss!"
    no "I had a feeling something like this might happen..."

    scene nodokabooksign16
    with dissolve

    no "Now, now. Settle down, everyone. Leave the {i}cosplayers{/i} alone."
    no "I’m sure there are plenty more questions that need to be answered and I don’t have all day..."

    scene black
    with dissolve2

    "The Q&A carries on, getting more and more disturbing with each and every question."
    "This isn’t just a book."
    "This is {i}us.{/i}"
    "This is {i}our{/i} story."
    "And she’s putting the entire thing on display for everyone..."
    "She’s showing them all who I really am..."
    "She’s showing them everything..."
    "And..."
    "And they..."
    "And they {i}like{/i} me..."
    "..."
    "{i}Why?...{/i}"

    scene nodokabooksign17
    with dissolve2

    ri "Hey! Bar buddy! Long time, no see. Didn’t realize you read this kind of stuff. That’s not weird or anything. I’m not judging you."
    s "I don’t read {i}this kind of stuff,{/i} Rika. That girl is one of my students."

    scene nodokabooksign18
    with dissolve

    ri "Okay. That’s a relief because I was totally judging you."
    s "Haven’t you jerked someone off under the bleachers before? Why are {i}you{/i} judging {i}me?{/i}"
    ri "Dude, that was the 90’s. If you weren’t jerking someone off under the bleachers, what were you even doing?"

    scene nodokabooksign19
    with dissolve

    ri "Also, that’s not even the part I was judging you for. I got laid watching Cannibal Holocaust once. Disturbing content or whatever doesn’t bother me. But super smart people like that?"
    ri "That stuff creeps me the fuck out. That girl’s, like...the head of a cult already. And I’m not looking to get sucked into another one of those things."
    ri "Knew there had to be an ulterior motive for her hitting on me. No one wants a single 42 year-old woman covered in tattoos."
    r "You’re 43! Stop lying to everyone!"

    scene nodokabooksign20
    with hpunch

    ri "No, {i}you{/i} stop lying to everyone! I’m going through enough!"
    s "Are you really still in the dorms? It’s been months."

    scene nodokabooksign21
    with dissolve

    ri "Like I said, I’m going through enough. But things might take a turn for the better soon. We’ll see."
    ri "You got anything planned for the rest of the day? I was gonna go grab dinner if you wanted to tag along."
    s "I have plans with a cult leader already, but maybe next time."

    scene nodokabooksign22
    with dissolve

    ri "Suit yourself. You might want to be careful around that girl, though. She denied it, but I totally know she was the one who hit on me. You might be next. Some girls are just into age gaps like that."
    s "I will remain vigilant and oppose any and all sexual contact with her."
    ri "Cool, cool. Cool."
    s "..."
    ri "..."
    ri "I’m gonna give you my phone number."
    s "You are?"
    ri "Yeah. I tried to think of a cool lead-in to that or a way to sound smooth or whatever, but I couldn’t come up with anything. So I’m just gonna give it to you."
    s "Are you hitting on me right now? Your daughter is like ten feet away."

    scene nodokabooksign23
    with dissolve

    ri "I’m not hitting on you. I just desperately need friends to distract me from the darkness that is consuming all that I am and Rin keeps telling me I’m 43 and making things even darker."
    s "Are you {i}sure{/i} you’re not hitting on me? Because you can be and I won’t mind."

    scene nodokabooksign24
    with dissolve

    ri "Aren’t you dating Imani?"
    s "Imani? No. We just work together. Same with Wakana. And I’m pretty sure we told you that."
    ri "Yeah, but my ex told me she loved me and that was clearly a lie, so."
    s "I’m not dating Imani. And if I was, I probably would have said something about it when the two of you made out."

    scene nodokabooksign25
    with dissolve

    ri "Ohhhhh...yeah. She was so average that I guess I forgot about it already."

    "Oh, poor Imani..."
    "I can’t wait to tease her more about this."

    scene nodokabooksign26
    with dissolve

    ri "Anyway, I’m gonna head out. But you should call me sometime when you’re not busy joining a cult."
    ri "Also, if they try to brand you, don’t let them. It hurts when it happens and then it hurts again when you have to tattoo over it."
    ri "Later."

    scene black
    with dissolve2
    $ rikanumber = True
    stop music fadeout 15.0

    "Rika heads out and I return to Rin and Otoha just before our semi-famous author friend rejoins the fray."
    "Not wanting the crowd to swarm her, the four of us take shelter in the store’s employee lounge for an hour or two as Rin and Otoha give Nodoka a stern lecture on the value of privacy."
    "I elect to not chime in, despite being perhaps the most violated out of everyone, but it’s not because I’m not upset with her."
    "In fact, she was {i}right{/i} earlier when she said this was something I’d want to see."
    "I {i}am{/i} proud of her — but it’s for all the wrong reasons."
    "And, disturbed as I may be, I can’t help but feel shocked about how closely she’s watched me."
    "And just how well she seems to understand."
    "My curiosity grows stronger, causing several uncertain uncertainties to dissipate."
    "All the while, she continues to hollow out a segment of my heart to live in."
    "And I continue to hold my breath so I can feel more of her existence."
    "It’s the closest I can ever come to feeling one with her."

    $ renpy.end_replay()
    $ nodokaspecial30p2 = True
    $ nodoka_love += 1

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump nodokaspecial30p3

label nodokaspecial30p3:
    scene nodokashotengai1
    with dissolve2
    play music "samhain.mp3"

    r "Okay, so, now that that’s over and done with and you’ve made everybody uncomfortable, what now? You promised us food and I have yet to see so much as a snack."
    r "Empty the purse, Nodoka. I know you’re holding out on us."
    no "Apologies. That ran longer than I expected. Guess my newest book is a bit of a hit, isn’t it?"
    s "Yeah, I wonder where you got the story from?"

    scene nodokashotengai2
    with dissolve

    no "What can I say? I can find inspiration in anything. I shan’t be blamed for simply drawing upon my own experiences."
    no "If you’d take the time to read it yourself, I’m sure you’d come to like it. It’s not as if I know {i}everything.{/i} There’s plenty in there I was forced to make up."
    r "Hi. Rin here. Still hungry. Please feed."
    o "It’s late, but I don’t think anything around here closes down until a few hours from now. Did you get, like...some sort of allowance from your publishing company or whatever? How does this work?"

    scene nodokashotengai3
    with dissolve

    no "It works via the combination of digital deposit and the magic, rectangular card in my pocket that I use to pay for everything. "
    o "Oh, okay. So it’s not free. You’re just paying for it."
    no "It’s free for you, which we all know is the only thing that matters. "
    s "I’d normally offer to pay, but I’ll accept an expensive dinner as compensation for using my likeness in your novel."

    scene nodokashotengai4
    with dissolve

    o "What do you mean you’d {i}offer to pay?{/i} Aren’t you cheap as hell? When have you ever offered to buy me anything?"
    s "I’ll start offering you things once you start being nicer to me and stop tackling me in dark rooms."
    r "Totally ignoring that I just heard any of that and getting back to the food thing- where are we going? There was this street we passed on the way here that I think should have a bunch of food trucks."
    r "It didn’t have any on the way over, but I’ve got a feeling they’re there now. And you can trust me. I have special food truck senses."
    no "I was thinking we could celebrate my success by doing something a bit more upscale. Perhaps a nice sushi bar or some other comparable restaurant?"

    scene nodokashotengai5
    with dissolve

    r "Uhh, actually, Otoha and I kind of have a 0%% success rate when it comes to restaurant dates, so if we could choose somewhere that’s like, not inside...that would be cool."
    o "The sample size is only one, but...yeah. What Rin said. "
    s "I remember that day. I made out with Otoha’s teacher in the bathroom. "

    scene nodokashotengai6
    with dissolve

    r "You made out with yourself in the bathroom? How is that even possible?"
    no "Do tell. And don’t mind if you see me reach into my pocket to press a button while you’re speaking. I can promise you I’m not recording any of this. You have my word."
    s "Your word means nothing to me, Nodoka. And I should probably stop talking about this since I’m finally on decent terms with your roommate again."
    o "Decent might be a bit of an overstatement, but thank you."

    scene nodokashotengai7
    with dissolve

    r "Is there anything that...fits our {i}criteria{/i} around here? Because I’m not trying to be pushy but, if you can’t think of anything, I’m just going to start walking towards Schroedinger’s food truck alley. "
    no "Hmm...I believe there’s a shotengai not far from here with a varied assortment of foods. I remember passing by during my last signing. "

    play sound "static.mp3"
    scene nodokashotengai8
    with flash
    stop sound

    mo "Time for another weebnote! A “shotengai” is a shopping street in Japan that is closed to car traffic! They’re typically stocked with local goods sold by local vendors at cheaper-than-average prices!"
    mo "If there’s something you’re looking for, whether it be croquettes, sandals, okonomiyaki, or other household items, the local shotengai is always a safe bet!"
    mo "Plus, shopping at them is great for stimulating the local economy! And many of them partner up with other vendors in the area for exclusive deals! I highly recommend them! "

    scene nodokashotengai9
    with dissolve

    r "..."
    no "..."
    o "Why did Molly just show up and lecture Sensei about shotengai?"
    s "She does that sometimes. She’s probably just one of Nodoka’s fans and was already in the area."
    no "What a shame. I never even got to sign a copy of my book for her. I wonder if she was too embarrassed?"
    r "Molly? Embarrassed? Sure. And I prefer men."
    s "Let’s do this shotengai thing before everything closes down. I’d like to get as far away from here as possible as {i}soon{/i} as possible before more people think I’m in costume."

    scene nodokashotengai10
    with dissolve

    no "I’m surprised they recognized you at all. That shirt looks significantly thinner than the one my book describes."
    r "Not hard to recognize a huge dude with a huge dick!"

    scene nodokashotengai11
    with dissolve

    o "Bro."
    r "Otoha, I have absolutely no idea why I said that. I’ve never even seen it before. Unless you count the one time at the gym, but that was through the pants for like five seconds and it doesn’t count."
    r "Also my mom grabbed it and Futaba told me and you need to kiss me or I’m just going to keep ranting about this."
    o "Yeah...how about we eat first and make out later? I’d prefer if you’re not thinking about dicks while we’re kissing."

    scene nodokashotengai12
    with dissolve

    r "I understand and apologize. I will try harder to keep all phallic commentary to myself. My lips are sealed. Until you unseal them, I mean. At that point, they will come unsealed."
    no "Will you do me the honors of carrying my display-purse, Sensei? My hand is beginning to cramp."
    s "I will not and that sucks for you."
    no "Not even if I let you be my boyfriend for the rest of the night? It seems only fair that we couple ourselves together if our companions are going to be doing the same."
    s "Does it come with all of the standard benefits being a boyfriend entails?"
    no "You mean like taking my pants off and gently nibbling on my-"

    scene nodokashotengai13
    with dissolve

    o "Okay, come on. That’s enough of them for now."
    r "What?! But we were just about to get to the good part!"

    scene nodokashotengai14
    with dissolve

    r "Otohaaaaa!"
    s "..."
    no "..."
    s "Please continue. You didn’t get to finish your sentence."
    no "I don’t know. I quite like the idea of leaving a cliffhanger there."
    no "In fact...I think I’ll let you sweat for a little while longer."
    s "How {i}much{/i} longer exactly? Because I don’t have all night."
    no "Of course you do. I advised you in the very beginning that this could run until tomorrow. And I need you here to make sure my plan pans out. "
    no "It’ll be significantly harder achieving the result I want all by myself, you know."
    s "And that result is still...getting Otoha and Rin to fuck?"

    scene nodokashotengai15
    with dissolve

    no "If it doesn’t happen tonight, I’m not sure it ever will. "
    no "So I {i}suppose{/i} you can walk away now if your end goal is sleeping with each of them quicker..."
    no "But, if you’d like to take your time and focus on the {i}others{/i} for now...and let the two of {i}them{/i} explore one another's bodies on their way to makeshift happiness..."

    scene black
    with dissolve2

    no "Stay with me. "
    no "Until the sun rises once more."

    "........."
    "......"
    "..."

    scene nodokashotengai16
    with dissolve2

    "She didn’t need to try and convince me."
    "As much as I’d enjoy having sex with all three of the girls I’m with tonight, I know it would be wrong to insert myself both in between and {i}inside{/i} of the two furthest away from me."
    "All things considered, it would be wrong to insert myself inside of Nodoka as well — but that is a different sort of unacceptable that I’ve made overwhelmingly apparent to be unimportant to me."
    "What I’m trying to say is I want Rin to be happy. And to a real, yet relatively lesser extent, Otoha as well."
    "And if that means sidelining myself and going along with the plan of someone who may very well be a sociopath, so be it."
    "Because at least she’s being a sociopath in a nice way tonight and not locking the two of them in a room together and disallowing them to leave until they sixty-nine."
    "If that winds up happening, I’ll cut the cord with Nodoka for good."
    "Involve me in borderline sexual assault one time, shame on you. Involve me in that same thing twice...and we should probably both be in jail."
    "I still don’t know what her plan is- nor how I can help her with it."
    "But I know that, until the sun rises once more, I’ll be right here beside her."

    r "You guys ever just think about tacos? What an amazing invention these things are. They’re like little boats that you can eat."
    o "Very nice, Rin. Is that really all you’re having, Nodoka? Just...a single croquette? Rin and I have stopped at like seven stalls so far and I’m starting to feel bad."
    no "I’m not very hungry. But don’t let my poor appetite spoil dinner for either one of you. Stop wherever you like. The night is just getting started after all."

    scene nodokashotengai17
    with dissolve

    r "{i}Started?{/i} Are we doing something after this? Because the answer to that question greatly influences the amount of tacos I am about to eat."
    no "I just figured it would be nice to wander through the streets with a group of people I’m close to. If only my dear Futaba was here to join us as well."
    o "You’re...the one who explicitly decided to not invite her. You can’t do that and then just wish she was here. "
    no "I neglected to invite Futaba for her own well-being as discussing my latest work with her might prove to be a bit...difficult. "
    no "Besides, I’m {i}fun{/i} Nodoka right now. I don’t want to {i}explain{/i} things. I explained things all day."

    scene nodokashotengai18
    with dissolve

    no "Right now, what I want more than anything is to enjoy my free time with you. "
    no "Because who knows when the next time I’ll see either of you is after you discover how nice it feels to scissor later tonight?"

    scene nodokashotengai19
    with dissolve

    o "..."
    r "..."
    no "Did I say something wrong? I meant that sincerely. "

    scene nodokashotengai20
    with fade

    r "Nodoka, it’s {i}because{/i} you meant it sincerely that it’s weird. Stop trying to rush us. Otoha wants to move slow."
    o "Seriously. Like, why do you have to be so involved in our personal...{i}stuff{/i} anyway? It has nothing to do with you."
    no "My dearest Otoha, I’m writing a series based on our lives. {i}Everything{/i} has to do with me now. If you delay any longer, I’ll just wind up having to make something else up. And where’s the fun in that?"
    o "The fun is {i}not{/i} getting in between us."
    no "I can’t say I agree. I think I’d have plenty fun in between you. But I understand that may be a little too much for {i}all{/i} of us right off the bat."
    r "Otoha- permission to throw a taco at your roommate? "
    o "Permission granted."

    scene nodokashotengai21
    with fade

    no "Wait, wait, wait. There’s no need to throw anything at me. "
    no "All that will do is dirty this suit and force my boyfriend here to help me undress right in the middle of this shotengai. And I’m sure {i}no one{/i} wants to see that."
    r "Taco attaaaaaaack!"
    o "Rin, wait. No taco attack."
    r "No taco attaaaaack!"
    o "Nodoka, I’m gonna be real with you. It’d be super cool if you stopped trying to start problems just so you could get some exciting material for your book or whatever. We’re not...{i}playthings.{/i}"

    scene nodokashotengai22
    with dissolve

    no "Otoha, thank you for “being real” with me. But you’re wrong. "
    no "I’m not trying to start problems at all."
    no "Have I done that in the past? Maybe. Will I do it in the future? Another maybe. But right now, I’m just being eaten alive by curiosity."
    no "Your youth only comes once. Shouldn’t the two of you be making the most of it by engaging in constant lesbian sex with one another? That’s what {i}I{/i} would be doing if {i}I{/i} had a girlfriend. "
    no "But alas, my desired female partner is but one more who has fallen victim to our teacher’s phallus."

    scene nodokashotengai23
    with fade

    o "Oh, and that’s another thing! Sensei, why are you not saying anything when Nodoka’s basically putting your whole ass creepy lifestyle on blast?! You saw yourself how many weird looks you were getting tonight!"
    r "Otoha’s right. Couldn’t this book start like, major problems for you if the wrong person finds out about it?"
    no "The two of you are overreacting. Fiction is fiction at the end of the day. And even novels that are based on real life events are often exaggerated beyond recognition. This is no different from that."
    no "I’ve even gone so far as to change the names of everyone involved. "
    r "I don’t know. Rin to Ren doesn’t sound like that big of a change. "
    o "Neither does Otoha to Otoka..."
    no "If the two of you would just take the time to actually {i}read{/i} the book before critiquing it to this extent, you’d have much more room to talk."
    no "But for now, I’d like to get back to the topic at hand and ask you when the two of you will be bringing each other to orgasm. Which, for the record, Sensei is also curious about."
    s "She’s not wrong. But also for the record, I have no part in this and haven’t really figured out how I feel about her book yet. "
    o "Stop being curious about...stuff you shouldn’t be curious about! If you’re that horny, just fuck Nodoka or something! At the very least, it’ll get her off our backs!"
    r "Or...{i}don’t{/i} do that. Because you already have other people who...actually love you."
    no "Are you implying I don’t love my very own father-slash-boyfriend?"
    r "Not in a way that sounds legal or socially acceptable..."
    s "Otoha, like I said, I’m not involved in this- nor am I going to try and force you two into doing anything you don’t want to."
    o "Yeah, but you have no issue helping {i}Nodoka{/i} do that, which is no different. Man up, dude."

    scene nodokashotengai24
    with dissolve

    no "You know I love you...don’t you, Papa? Or should I whisper it in your ear again tonight while we’re cuddled up in bed?"
    s "Maybe...tone it down a little, Nodoka. I get that you have a difficult time noticing things like this, but Otoha’s actually starting to get kind of heated. "
    o "Yeah, because I’m sick of people trying to tell me who I’m supposed to be or what I’m supposed to do or how I’m supposed to feel. "
    o "Also, I’ve been holding onto this burger for so long without biting it that it’s probably bad now. So thanks, guys."
    r "Yeah...and my tacos have gotten so soggy that I’m not sure they’re even throwable anymore. Can we go back so I can get more?"
    no "Psst...Papa."
    s "What do you want, fake-daughter?"
    no "Ask them when they plan on fingering one another and I’ll do things to you in the closet later. "
    s "Nodoka..."
    no "Come on...The only way we’ll get them is through repetition."
    s "I-"
    o "Sensei’s name is Akira and he’s been hiding it from everyone for reasons I don’t understand."

    scene nodokashotengai25
    with dissolve

    s "Hah..."
    r "You have a name?!"
    no "Akira?..."
    o "You want to be on Nodoka’s side? Fine. I can throw dirt back at you. That was just the beginning."
    s "I was literally about to refuse Nodoka’s offer. But you were so trigger happy and determined to spill that information that you fired as soon as I opened my mouth."

    scene nodokashotengai26
    with dissolve

    o "Oh."
    o "Whoops."
    r "YOU HAVE A NAME?!"
    o "I’m so used to you doing everything in the completely incorrect way that I kind of just figured that’s what you were going to do again. I’m sorry."
    o "In my defense, though, normal Sensei would never say no to having things done to him in the closet. So this is also kind of your fault for growing a spine out of literally nowhere."
    o "Also, your name is rad. What’s there to even be embarrassed about?"

    scene nodokashotengai27
    with fade

    no "Akira...Arakawa..."
    r "YOU-"
    o "Rin, shh. Eat this burger."
    r "Mmffffghfhfissssocold!"
    no "May I ask why you were keeping that name a secret?"
    s "I technically {i}wasn’t,{/i} but...it’s a long story."
    no "Is it...one you’d be willing to share?"

    scene nodokashotengai28
    with dissolve

    s "Any reason why you’re so interested all of a sudden?"
    no "No...not particularly."
    no "Just wondering..."
    s "..."
    no "..."
    s "You’re significantly less wordy and pretentious all of a sudden. "
    no "What do you mean? I’m the same person as always."
    s "..."

    scene nodokashotengai29
    with dissolve

    no "Ithnkyrjust........."
    no "Imgningthngs..."
    s "..."
    no "Mmf......mm....."
    s "Nodoka?"

    scene black
    with dissolve2

    no "Mmg......mglp..."
    no "Cold..."

    $ renpy.end_replay()
    $ nodokaspecial30p3 = True
    $ nodoka_love += 1

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump nodokaspecial30p4

label nodokaspecial30p4:
    scene nodokahotel1
    with dissolve2

    no "Here — a gift from me to you. See it not as a perverted gesture, but a token of apology for being overly assertive in regard to your coital status."
    o "Our...what?"

    "After wandering around the city for a bit, we make our way back to the same hotel we typically visit for large gatherings like the Dorm Wars and Christmas."
    "Based on the reactions of Rin and Otoha, however, I don’t think they anticipated being in a room {i}without{/i} Nodoka present to annoy them."
    "Nor did {i}I{/i} anticipate the two of us being alone together, which I’m pretty confident is what’s happening right now."

    r "What’s that? What are you handing us?"
    no "The key to your room. Have fun and don’t stay up too late. Or do. I am not your guardian — just a lone entity a bit more invested in your personal affairs than you’d prefer."
    o "You...got a room for just...the two of us?"
    no "It only has one bed. I hope that’s okay."

    scene nodokahotel3
    with dissolve

    o "Of course there’s only one bed. I should have figured this out the moment you dragged Sensei along."
    r "But...if Otoha and I are supposed to sleep in the bed, where are you and Sensei going to sleep?"
    no "In our own bed, in our own room. Pay attention."
    no "We’re right next door to you two. Which also means we’ll be listening {i}very{/i} closely to anything you two get up to in there."
    r "Are...you sure you don’t want to stay in the same room as us and Sensei can sleep all by himself?"
    no "Getting cold feet, Rin? This could be your chance to finally take things to the next level."
    r "Or ruin everything. Which is probably what is going to happen if I don’t have someone there to prevent me from exploding."
    o "As if Nodoka would {i}prevent{/i} anything. We both know that all she’d do in there is cheer on your demise. "
    r "Yeah, but she’d do it in that same irritating way she’s always doing things which would offset all of the hormones and distract me from the things I want to do to you."
    no "I’m fine sleeping in the same room as you. All I ask is that Sensei comes along as well as the two of us are a package deal until tomorrow morning."
    r "Deal."

    scene nodokahotel4
    with dissolve

    o "What? No deal. Don’t go deciding things like that without me. "
    r "Otoha, I don’t think you understand the gravity of the situation here. I am a time bomb waiting to detonate."
    o "I understand that whatever that {i}gravity{/i} leads to would be better with just us rather than these two perverts. Also, there is no way I’d be able to fall asleep in a bed with four people. Just take the keycard, Rin."
    r "Are you {i}sure?{/i}"

    scene nodokahotel5
    with dissolve

    o "Yeah...it’s cool. "
    o "We’ve been dating for a while now. We should...take opportunities like this when they’re handed to us."
    r "You’re 100%% sure?"
    o "Yeah...it’s fine."
    r "You’re {i}1000%%{/i} sure?"
    o "Rin, just take the card."

    scene nodokahotel6
    with dissolve

    r "{i}Thank you.{/i}"
    no "Room 25. Enjoy."

    scene nodokahotel7
    with dissolve

    "Rin and Otoha scurry off to their room, leaving Nodoka and me to...do whatever the next step in Nodoka’s plan is. Assuming “waiting” counts as part of the plan as things seem mostly out of our hands now."

    no "They grow up so quickly, don’t they? It appears that our nest is empty once more."
    s "Mission complete?"

    scene nodokahotel8
    with dissolve

    no "Does this seem like a satisfactory ending to you? Nothing has even happened yet."
    s "I wouldn’t say that. You just locked Otoha in a room with a self-proclaimed time bomb. Even if all they do is sit there, Rin is probably going to orgasm at least three times. Just take the win and call it a night."
    no "{i}Call it a night?{/i} Don’t tell me that libido of yours vanishes when it’s needed the most?"
    s "Is it needed? Or is this going to be one of those situations where you make me {i}think{/i} it’s needed only for me to find out moments later that it’s not? "
    no "You all make me out to be far more evil and far more calculating than I actually am, Akira. Not {i}everything{/i} has to be part of some plan."
    s "No, but it usually {i}is.{/i}"

    scene nodokahotel9
    with dissolve
    stop music fadeout 15.0

    no "Well, {i}someone{/i} has to write the script. And, correct me if I’m wrong, but you’re opposed to that now, aren’t you?"
    s "..."
    no "Our chamber awaits, Papa. If we delay any longer, I’m worried we might {i}miss{/i} something..."

    scene black
    with dissolve2

    "Nodoka turns around and walks down the same path Rin and Otoha followed just moments ago, not stopping until the two of us are outside Room 24."

    play sound "dooropen.mp3"
    scene nodokahotel10
    with dissolve2

    "She doesn’t bother turning the light on as we walk in."
    "I take that as the first sign of what’s to come while preparing for the foil to follow."
    "There can be no causation without manipulation. And nothing will ever happen if there is, for lack of a better term or any creativity whatsoever, no one to script it."
    "I’ve followed her screenplay perfectly."
    "I let her drag me along...make an example of all that I am in front of hundreds of people...all for a goal {i}she{/i} has that I only partially care about."
    "But it’s the smallest part of all."
    "The truth is that I hate what is bound to happen next door."
    "I hate that I will be on {i}this{/i} side of the wall while a girl who reminds me too much of my ideal self chuckles at the thought that this is all because of her."
    "I look down on her, but the hidden truth is that I’m looking up."
    "The hidden truth is that I’m drowning in envy watching someone sculpt a world in which they’ll never care."
    "Not one where they just pretend not to."

    play music "bloodandsunset.mp3"

    no "Can you hear anything, Akira? "
    no "From the other side of the wall?"

    scene nodokahotel11
    with dissolve

    s "Not yet...no."
    no "I imagine they’re both quite nervous. It might take an hour or two before things really {i}kick off.{/i}"
    s "Why...do you want this so badly in the first place? I don’t get it. It can’t {i}all{/i} be for just {i}research...{/i}can it?"
    no "Why do the sands sing? Or the mountains moan? "
    no "No one knows."
    no "It has something to do with vibrations. That much is certain. That is how sound {i}works{/i} of course. "
    no "But the melodies created by air alone could not possibly sound that...beautifully ominous, could they?"
    no "There is something else at play. Something we don’t understand. "

    scene nodokahotel12
    with dissolve

    no "Let me be the thing you can’t explain."
    no "The one piece of reality that is so far detached from what is actually {i}real{/i} that it makes you question your place in all of this."
    s "All of...{i}what?{/i}"
    no "Who knows?"
    no "Who {i}wants{/i} to know?"

    scene nodokahotel13
    with dissolve

    no "You asked me earlier why I started writing. My response was to confuse you. "
    no "And while the reasoning for that may have bordered somewhere between a want for you to {i}get it{/i} and the desire to {i}reflect,{/i} the truth is much simpler than that."
    no "There’s someone I know who loves books. "
    no "For years and years, they were all she had."
    no "Fiction was her favorite. And from a creaky chair in the middle of a mostly-empty living room, she’d throw herself into story after story because her world was far too drab."
    no "More often than not, while waiting for the shelves to repopulate, she’d read the same things over and over. "
    no "Taking them in. Memorizing them."
    no "She’d read until her eyes dried up...skin cracking from the dryness of the air and the constant scratch of paper on her fingertips."
    no "But all the while, even as it was slowly killing her, she continued to do what she loved. She continued to seek solace in the pages of books when there was no solace anywhere else to seek."

    play sound "static.mp3"
    scene house2 with flash
    stop sound

    no "She had several friends, each with their own vices and virtues, but they too were so busy with said vices that they seldom touched her hands. "
    no "And no one knew how broken she was but the girl who would fill those shelves with new books."
    no "Strands of lavender-colored hair, decorating the spaces between words would be plucked up by those cracking fingers and lifted up under the warm light of dimming bulbs. "
    no "She would observe them for hours when the words stopped making sense. And she loved that color more than life itself, but it meant little when life to her was nothing."

    play sound "static.mp3"
    scene house3 with flash
    stop sound

    no "Regardless, the days carried on. "
    no "And as they did, her fingers never healed. Her heart never wavered. And all that kept her sane were those same lavender hairs and those same recycled words."
    no "The air was thick with pheromones...and the cracks in her skin would occasionally be filled by the slow, sexual absorption of her own fluids coating her own skin as she tied those hairs around her fingers."
    no "She’d put them inside of her."
    no "She’d cum until she cried under those warm, dim lights — a communal blanket haphazardly draped over her, still keeping her upper body exposed because she was desperate to be seen."
    no "And she’d whisper the name of the one she loved the most under her breath, hoping that breathing would become too hard and that the girl would hear her and rush downstairs to {i}save{/i} her."
    no "But she never did."
    no "She was always too busy saving someone else."

    play sound "static.mp3"
    scene house4 with flash
    stop sound

    no "{i}Yuko...Yuko...{/i}she moaned, tenderly plugging herself up with the metastasized aeons of repressed lust and a desire to be free! But freedom wasn’t possible! The world was already over!"
    no "The scent of rotten flesh filled her nostrils with regret and shame! Why didn’t she know?! Why did it take so long to find out?! "
    no "The screams, still fresh in her mind as the one in the second half of my uninspired moniker discovered the remains of the first half sodomized her eardrums! She was bleeding! But she couldn’t stop!"
    no "Yuko! Come downstairs!"
    no "Repopulate the shelves!"
    no "Put dinner on the table and your fist inside my mouth! Eat this long forgotten body and drink in the memories of when things were happier! When they were better than this!"
    no "There were games back then! We didn’t mind the lack of natural light! We didn’t mind this single blanket, now stained with piss and blood and the excretions of untapped resentment!"

    play sound "static.mp3"
    scene nodokahotel14 with flash
    stop sound

    no "You asked me earlier why I started writing. My response was to confuse you."
    no "Now, all I’m doing is confusing myself."
    no "I write because I have to."
    no "Because I am gifted."
    no "It is not my fault others don’t understand this gift."
    no "It just means I have to {i}make{/i} them."
    s "You can’t make anyone do anything by just copying down the lives of others into a book. "
    no "You don’t think that’s {i}all{/i} I do, do you? "
    no "I’m no one trick pony, Akira. I write all sorts of things in all sorts of genres."
    no "It’s not my fault that the one people seem to be the most interested in is the one about a grown man having his way with little girls."
    no "That’s just human nature, I suppose — obsessively curious and demonstrably sick."
    s "..."
    no "..."
    s "That thing about the girl you were just talking about...the one who liked to read..."
    no "What about her?"
    s "You started off by saying you knew someone like that, but...that was really just part of something you’re writing, right?"

    scene nodokahotel15
    with dissolve

    no "Is that what you think?"
    s "If I had to guess...yeah. That’s probably what I’d go with."
    no "I see."
    no "Well, that’s a fine interpretation."
    no "But I’m hesitant to tell you the ending to a story that’s still playing out. "
    no "Especially when there’s another story I’m slightly more interested in at the moment."
    s "You mean {i}my{/i} story."

    scene nodokahotel16
    with dissolve

    no "It’s {i}my{/i} story too, Akira. It just focuses more on you as I’m better suited as a background character."
    no "Can you imagine an entire book about {i}me?{/i} I’m exhausted just thinking about it."

    scene nodokahotel17
    with dissolve

    no "{i}But...{/i}"

    scene nodokahotel18
    with dissolve

    no "That doesn’t mean I don’t crave the spotlight every now and then..."
    no "And do you know what the quickest way for a background character to step into the spotlight is?"
    s "To...spend time with the protagonist."
    no "Akira, this is a {i}smut{/i} novel."

    scene nodokahotel19
    with dissolve

    no "The answer is fucking him."
    s "..."
    no "..."
    s "You really are just doing this for your book, aren’t you?"

    scene nodokahotel20
    with dissolve

    no "Ah! I’m shocked! You think a lady like {i}me{/i} would throw away her precious virginity for a {i}book?{/i} Sensei, how could you? That hurts."
    s "There’s just...something weird about all of this. "
    s "Between the maniacal, anecdotal rambling and the sudden proclamation that we’re going to have sex, you can’t blame me for not immediately understanding what’s going on here."

    scene nodokahotel21
    with dissolve

    no "Hmm..."
    no "When you put it that way, you do make a good point."

    scene nodokahotel22
    with dissolve

    no "So, how are we going to do this? I think I’d prefer to be totally nude for my first time."
    s "Nodoka, come on."

    scene nodokahotel23
    with dissolve

    if nodokaspecial15p3 == True:
        no "What’s the matter? You’ve already put it in my mouth. This is barely any different."
    else:
        no "What’s the matter? We both want it. It’s not like I’m an unwilling participant."

    s "The {i}matter{/i} is that it feels like there’s more to this that you’re not telling me. And that even {i}if{/i} I want to have sex with you-"
    no "Which you do. "
    s "Even {i}if{/i} I do, it feels...risky knowing that this could all be part of some kind of scheme."

    scene nodokahotel24
    with dissolve

    no "I see."

    scene nodokahotel25
    with dissolve

    no "I understand the rationale. And I don’t blame you for being skeptical of me based on prior experiences."
    no "Until now, I’ve been content as an observer. And I was having plenty of fun watching you defile everyone else while I remained pure and chaste."
    no "But that was just me fooling myself — separating the art from the artist. "
    no "Only those who have {i}seen{/i} a cat can draw one. "
    no "And while there are plenty of talented artists who could work off of one’s {i}description{/i} of a cat alone, touching one with your own hands...{i}feeling{/i} it and {i}understanding{/i} it...that would be easier. Yes?"
    no "Why does it matter if this ends up in a book or not? Are we not allowed to feel things just because there are little clones of us jumping around between pages somewhere?"
    s "It’s more that I struggle to believe you {i}feel{/i} anything."

    scene nodokahotel26
    with dissolve

    no "Oh."
    no "So {i}that’s{/i} the problem."
    s "It’s not just {i}one{/i} problem. It’s a whole mix of problems, but all of those things revolve around me not being able to trust you."
    s "For all I know, you could be...recording this or something. It’s bad enough that you’re already publishing it. You’ve given me no reason to believe that this is a good idea."
    no "..."
    s "..."
    no "I suppose I was unaware that you needed one."

    scene nodokahotel27
    with dissolve

    no "Forgive me as I’m about to say several very rude things, but I can assure you they come from a place of love."
    s "..."
    no "I’ve written many characters like you before, but I’ve never had the gall to give any of them such a {i}ridiculous{/i} caveat. "
    no "{i}You{/i} can’t trust {i}me?{/i} "
    no "What kind of moral paragon are you pretending to be? "
    no "You’re an adult having sex with teenagers. Lots of them. Does adding ridiculous clauses like “I have to trust them” and “they need to have feelings” to that make you feel better about yourself?"
    s "You’re one to talk. You-"

    scene nodokahotel28
    with dissolve

    no "I’m not trying to make you feel bad. "
    no "I said this was coming from a place of love, remember?"
    no "The point I’m getting at is that it is {i}okay{/i} to be a horrible person with horrible vices and that things like that should be {i}embraced.{/i}"
    no "What matters most is not what is right or what is wrong. "
    no "What matters most is staying true to yourself because it is individuality that spins the gears of this planet, not {i}righteousness.{/i}"
    no "Be corrupt. Be immoral. Be the scum of the earth and indulge in the pleasures of the freshest, untouched skin because that is what matters to {i}you.{/i}"
    s "..."
    no "..."
    s "That’s a horrible, disgusting lesson and an even more disgusting mindset."

    scene nodokahotel29
    with dissolve

    no "I know...Isn’t it great?"
    s "No, it’s not..."
    s "It’s one thing to internalize thoughts like that and...hide them from everyone else, but to outright {i}say{/i} them and talk about how it’s {i}okay?{/i} That’s..."
    s "It’s not..."

    scene nodokahotel30
    with dissolve

    no "{i}Embrace{/i} it."
    no "Harness those feelings and give them to me."
    no "Show me the {i}real{/i} you — not the facade who beds the rest."
    no "I want something that no one else has. A part of you that you don’t {i}have{/i} to deny because I will accept it all."
    no "And as you feast upon my flesh, I want you to remember how disgusting you are and how the world would scorn you for the things you’re doing to me."

    play sound "static.mp3"
    scene nodokahotel31
    with flash
    stop sound

    se "I like her."

    play sound "static.mp3"
    scene nodokahotel32
    with flash
    stop sound

    se "She’s like me but less pretty."

    play sound "static.mp3"
    scene nodokahotel30 with flash
    stop sound

    no "What do you say, Akira?"
    no "Would you like to write a new chapter with me?"
    no "Or will those pointless, fraudulent morals of yours spoil the mood once more?"
    s "..."
    no "..."
    no "Come here."

    $ renpy.end_replay()
    $ nodokaspecial30p4 = True
    $ nodoka_love += 1

    jump postnodokachain1

label sportswars17:
    scene clearnightsky
    with dissolve2

    "And so one more war comes to an end...but you weren’t there to see any of it this time."
    "Because you were fighting your own battle."
    "You were neck deep in wanting something, trying to keep your chin up so you wouldn’t accidentally let too much of that desire in to change the way your organs work."
    "But you were failing."
    "Even now, you’re failing — sitting at a kitchen table with someone whose existence you ignored just yesterday because she reminds you too much of someone else."
    "But what if it was always like that?"
    "What if that’s how she looked at first too? A reminder of someone else you were forced to let go of while you were still trying to figure out how to use your hands."
    "Will every girl you meet and every girl you fall for follow the same trajectory? Just one more step on a never-ending staircase, leading somewhere you don’t even {i}know{/i} yet?"
    "Does what’s at the top even matter?"
    "Do you hate the way your choices are judged like this?"
    "See, that’s the problem with things like stairs — it’s that things like stares will always make you trip."
    "You might {i}want{/i} to know what’s at the top, but you also might be content with just walking up and down until your knees buckle and your descent becomes less of a choice and more of a result."
    "Each step is a reminder of the one before it."
    "And every time you grip that railing to pull yourself up, all you’re really doing is delaying the inevitable."
    "There is nothing at the top."
    "There is nothing at the bottom."
    "You’ll be trapped in here forever until there’s a reason for you to leave."

    play sound "static.mp3"
    scene meetandfuck1 with flash
    stop sound
    play music "citylife.mp3"

    "And now for something completely different."

    no "First and foremost, I’d like to thank you all for taking the time out of your {i}very{/i} busy schedules to attend the first annual Nodokathon. "
    no "I’m your host, Nodoka Nagasawa. But, before we get into the details of exactly what this event will entail, please allow me to apologize for the way I conducted myself earlier."
    no "It appears that I have said something that may have made several people uncomfortable. And, while it’s been pointed out to me that this happens rather often, I assure you that my intentions have never been to {i}harm.{/i}"
    no "You see, I pride myself as a-"
    ki "Yeah, yeah, yeah. We don’t care what you said. Just get on with the fun part."

    scene meetandfuck2
    with fade

    r "Speak for yourself, Kirin. You weren’t even there."
    ki "Yeah, which is exactly why I don’t care. Nodoka says weird shit all the time. It’s the fact that she’s apologizing for it that’s {i}really{/i} weird."
    n "Wait, so {i}what{/i} happened exactly? What did Nodoka say?"
    mak "I’m sure you’ll hear about it sooner or later. What I really want to know is why the six of us were chosen for this “Nodokathon” thing. "
    ki "Is it really just the six of us? I was under the impression everybody got one of those forms since Noriko and I both did."
    no "Several other students were invited, but the six of you were the only ones who submitted their forms — which I am very thankful for as it keeps things even. "
    mo "There is no level too difficult for the Emerald Guardian of the Crystal Forest! And my presence here is naught but a testament to such a decree!"

    scene meetandfuck3
    with dissolve

    r "So it {i}wasn’t{/i} the disclaimer regarding “depravity and lasciviousness” that made you submit your application? It was the “challenge” part?"
    mo "Hey, you’re no better than me! We’re both perverts and everyone here is aware of that!"
    mak "Sana’s the one we should be concerned about, if anything. She’s the last girl I expected to turn up here."
    sa "I still don’t really...understand what’s happening, so..."
    no "Then, allow me to clarify."

    scene meetandfuck4
    with fade

    no "In an effort to give back to the community and pay thanks for all of the kind things you’ve done for me, I’ve taken it upon myself to organize this very special event. "
    no "By appearing here and submitting your participation forms, you have consented to keep {i}all{/i} that happens within this room a secret from anyone who did {i}not{/i} attend. Is that clear?"
    mak "Nodoka, we still don’t know what we’re doing. It’s hard to consent to something if you don’t know what it is."
    ki "Yeah, that’s what makes it exciting."
    no "And exciting it shall be, Kirin- for the six of you were invited as I believe you’ll be capable of keeping this contest classified from those who would not understand it."

    scene meetandfuck5
    with fade

    no "Additionally, I feel as if the six of you are those who will {i}enjoy{/i} it the most. It’s just a shame that our beloved Sensei is not here to compete as well."
    mak "So it’s a competition? "
    n "And probably some sort of lewd one based on the language the application used. And also the fact that Nodoka is the host."
    ki "And {i}Sana{/i} is participating?..."
    sa "I’m just...I’m here because Rin wanted me to come!"
    r "What? But I never- oh! Oh, yes. I need Sana here for moral support. This is a thing I asked her to do."
    no "It {i}is{/i} a competition, Makoto. Which is precisely why you, the only straight woman here, were invited as it appeals to your competitive nature. "
    ki "Sana’s not straight either? How does tonight keep getting more awesome?"

    scene meetandfuck6
    with fade

    sa "I don’t...I don’t really know what..."
    r "Oh my God, I made Sana bi!"

    scene meetandfuck7
    with dissolve

    sa "You didn’t do anything! This is...I..."
    sa "You just didn’t do anything!"
    mo "Details, great progenitor! For the sake of the competition! Not the sake of my perversion and how the environment we’ve been placed in is already making me feel a certain way!"

    scene meetandfuck8
    with fade

    r "You literally always feel {i}a certain way.{/i} "
    mo "The way I feel concerns you not, Nithhala! You’ve made that abundantly clear!"
    no "You have asked for details, and details I shall provide."
    no "Inside of this box, there are six names torn directly from the applications you submitted earlier. "
    no "These names will be drawn to see who among you will be competing in three separate competitions, each one of increasing intensity."
    mak "{i}Increasing intensity?{/i}"
    ki "Just let it be a surprise, Makoto! The last thing we need is you spilling your weird heterosexuality all over Nodoka’s sex contest."
    no "This is far more than a {i}sex contest,{/i} Kirin. It’s an {i}opportunity.{/i}"
    n "Oh, boy. Here comes the motivational speech."
    no "You see, every one of you here has something to prove. And every one of you here has something they wish to experience."
    no "The entire purpose of Nodokathon is to create an environment where your inhibitions can be erased for one night and one night only."
    no "Anything that happens here will simply...stop existing once the competition comes to an end. And any memories that have been made along the way are yours to keep."
    r "Is anyone else getting really nervous now? Or is it just me?"
    no "Would you like to back out, Rin? I can not begin to draw names until I receive confirmation that all of you are still up to the challenge now that it’s been more specifically explained to you."
    r "I...uh..."
    sa "Rin...will stay! This is me...providing moral support!"
    r "Aaaaaah fine! Okay!"
    no "And everyone else?"
    ki "Do you even need to ask?"
    no "Legally, yes."
    ki "Oh. Then yeah."
    mo "Affirmative!"
    sa "I...guess so..."
    mak "{i}Hah...{/i}I suppose."
    n "I am here to encourage sex positivity, so it’s a yes!"
    ki "Thanks for being the most sex-positive virgin I know, Noriko."
    mak "What’s the first contest then, Nodoka? I’d hope it’s something somewhat tame if they’re going to be {i}increasing in intensity{/i} like you mentioned."
    no "How about we start with a little...gravure modeling competition? "

    scene meetandfuck9
    with dissolve

    no "With our first contestant being..."

    scene meetandfuck10
    with fade

    no "Noriko Nakayama. "
    n "What percentage of my clothes do I have to keep on?"
    no "You can take off whatever you like. We’ve all agreed to keep this confidential, haven’t we?"
    mak "Are you just...are you the judge? Are you the one who decides the winners or is this a thing we have to vote on?"
    no "The second and third competitions will be more clear-cut, but I will be choosing the winner of the first round personally. So please do your best to leave a positive impression on {i}me,{/i} as selfish as that may sound."
    n "Kudos to Nodoka for figuring out a way to create her own sexy game show! And best of luck to whoever my opponent in the first round is!"
    no "Ah, yes. And that opponent will be..."

    scene meetandfuck11
    with fade

    no "The adorable Sana Sakakibara — here for {i}moral support{/i} only."
    sa "What does...{i}gravure{/i} mean exactly?"
    no "Technically, it refers to images created and printed through an intaglio etching process. But it’s become synonymous in the world of modeling with more...provocative posing and costuming."
    r "So...Sana is gonna...do sexy modeling? In front of all of us? Here? In the same room? And we’re just...we’re just gonna watch?"

    scene meetandfuck12
    with dissolve

    sa "It’s not...much different from...just being in the locker room...right?"
    r "It’s extremely different."
    mo "Context means everything, Zagull. This is something we’ve only fantasized about before, and now it’s coming to life in front of our very eyes!"
    sa "You’ve.......about me?........"
    r "Oh yeah."
    mo "Many times. I may be an elf, but I am only human."
    ki "Also guilty. "
    n "In a dream once, yeah."
    mak "You can take solace in the fact that I haven’t, Sana."
    ki "{i}Oooh, my name’s Makoto. I only like boys. I’m so cool.{/i}"

    scene black
    with dissolve2

    n "So, am I starting? What do I do? Where do I stand? Are there, like...costumes I can choose from? Or-"
    no "Here, you may take my place on the stage as I comb through my list of premade questions. As far as costumes go, I have not prepared any as I assumed you would simply model your underwear for us."
    n "Questions?"
    sa "Underwear?..."
    n "What kind of questions do you have? Are they going to impact our score?"
    no "Of course. Just think of the way the gravure swimsuit contest on the beach worked. I’ve used Kirin’s role as the commentator to draw inspiration from."
    ki "Aww, thank you!"
    n "Okay! In that case, bring it on! "

    scene meetandfuck13
    with dissolve2

    n "What’s up, world?! I’m Noriko Nakayama, and I’m here to objectify myself in front of a group of peers who will all be doing the same thing! All in the name of sport and making Nodoka horny!"
    ki "You’re really going to keep all of your accessories on?"
    n "Duh. They add {i}flavor.{/i}"
    no "Noriko, question one — if you were to {i}make love{/i} to anyone in this room, who would it be and why?"

    scene meetandfuck14
    with dissolve

    n "Oh, Rin. Easy."
    r "PFFFFBPFFFFBFBFFFBFFBT?! ME?!"
    ki "Wooooooow. Thanks, Noriko. Appreciate it."
    n "Hey, I’m just trying to be honest. There are a lot of reasons I’d choose Rin over anybody else here."
    r "There are?!"
    no "Please, explain your outlook for us."
    n "Well, for one, she’s the closest to my type. And the way that new bra makes her boobs look does things to me. "
    n "But, additionally, I’d like to see how I stack up compared to Otoha when it comes to making her cum since I think I could do better. Which I am only saying because it has to remain confidential under penalty of law."
    r "Nodoka, can I take a bathroom break? "
    ki "Can I go with her?"
    no "Unfortunately, there will be no breaks for the duration of this competition and I will now move onto question two."

    scene meetandfuck15
    with fade

    no "Noriko — how much sexual experience do you have? You may wish to reveal {i}or{/i} hide the person or {i}people{/i} you have this experience {i}with.{/i}"
    n "Good! Because that’s not a thing I’d reveal even if I was told to."

    scene meetandfuck16
    with dissolve

    n "Unfortunately, I’ve only been fingered one time and that’s as far as I’ve gotten. But I did some light dry-humping too and came from that if you want to count that as...almost-sex or something."
    r "Petition to remove the “no bathroom breaks” rule?"
    mo "Signed! "
    no "Denied. Noriko, what do you believe the root cause is as to why you’ve yet to take a {i}deeper{/i} plunge?"

    scene meetandfuck17
    with dissolve

    n "Probably a cross between bad timing, bad luck, and being a pushover. I will elaborate no further."
    no "Understood. Then, question three-"

    scene meetandfuck18
    with fade

    n "Before that, boom! Can’t spell “sex and body positivity” without “free the nipple!”"
    mak "You most certainly can."
    no "Oh my. It appears our first contestant has elected to shed her bra. Will this give her a leg up on the competition? Or will Sana follow suit?"
    sa "Hahah...hah..."
    mo "{i}Please follow suit.{/i}"
    n "Sorry, Nodoka. What was question three? I didn’t mean to interrupt you with my {i}sexiness.{/i} "
    no "Ah, yes."
    no "Question three — what is your most secret and {i}forbidden{/i} fetish?"
    n "Pass."
    no "There will be no passes."
    mak "How bad can it be if you’ve already openly discussed being sexually active and the fact that you’d sleep with Rin?"

    scene meetandfuck19
    with dissolve

    n "I mean...it’s not {i}bad...{/i}I just don’t think anybody else here other than maybe Molly would {i}get{/i} it. And that’s not really a discussion I think I’m...prepared to have?"
    mo "It’s all confidential, psion! And remember that anything you’ve fetishized is likely no worse than many of the visual novels I have played!"
    n "You guys promise you won’t say anything?"
    mak "I think we’re legally bound at this point."
    n "Then..."

    scene meetandfuck20
    with dissolve

    n "I’m kinda, like..."
    n "Okay, so I go through these phases where like..."
    n "Uhh..."
    ki "Just fucking say it! Jesus!"
    n "I’m kind of into, like...ponies?"
    r "You and Touka both."
    n "No, like...cartoons. Cause there are these games where you can have sex with the My Little Pony characters. And, I know it sounds weird, but like...there’s just something about it."

    if brony == True:
        ki "Is {i}everyone{/i} I'm attracted to into fucking cartoon ponies?! What is this?!"
        ki "I bet you and Sensei play those games together, don't you?"
        n "God, I wish."

    ki "Oh god. My roommate’s a fucking furry."

    scene meetandfuck21
    with dissolve

    n "That’s a different category entirely!"
    ki "Yeah, but there’s no way you’re not into that too if you’re already screwing Rainbow Dash on your laptop."
    mo "There’s nothing wrong with being a furry! In fact, Beastars has made me feel things that-"
    n "I understand and relate, Molly! But this is my fight and not a hole that you should be digging for yourself!"
    no "Relax, relax. I’m sure we can all agree in saying that there is {i}no{/i} fetish that would not be accepted here, Noriko. "
    no "I’d think no less of you even if you were attracted to {i}real{/i} animals. "
    n "You probably should! There are lines that need to be drawn and that is definitely one of them! But as far as cartoons go-"

    scene black
    with dissolve

    no "Yes, yes. You’ve said enough. But unfortunately, your time has run out and it now falls on Sana to take the stage."
    sa "I..."
    sa "So...about the...underwear thing..."
    r "{i}Psst...Sana.{/i}"
    sa "Huh?"
    r "{i}You don’t need to answer everything truthfully.{/i}"
    r "{i}In fact...please DON’T answer everything truthfully. There are things people don’t have to know about and-{/i}"
    ki "Nodoka! Rin and Sana are conspiring! And I want Noriko to win this round, so I demand you put a stop to it."
    no "Oh? Perhaps the two of them are just...getting more acquainted and making arrangements for {i}after{/i} the competition?"
    mo "Are we allowed to do that?"
    no "You can do anything you want so long as it stays in this room. I wouldn’t even mind if you pleasured yourself while watching. This {i}is{/i} for fun and all."
    n "Don’t tempt Kirin. She’ll do it. "
    ki "I’m really thinking about it and- ooooooh shit, Sana’s already topless."

    scene meetandfuck22
    with dissolve2

    sa "I...don’t normally wear a bra when I have a sweater on, so..."
    no "My, my, my. What a precious little thing you are."
    sa "..."
    no "You’ve barely started growing yet, have you?"
    r "They’re bigger than Ami’s at least."
    mo "Now, that’s just rude."
    no "You seem a bit embarrassed, Sana. Do you not intend to pose for us as well?"
    sa "I’ll...pose, but...I don’t know how I can beat Noriko when...I look like {i}this.{/i}"
    n "Oh no. She’s going to play up the innocent act, isn’t she? Am I screwed? Kirin, is this the end?"
    ki "If it is, can we go home and increase your fingering-count to two?"
    no "Sana, are you ready for your first question?"
    sa "I’ll...do my best..."
    no "Then, question one — what’s the strangest place you’ve ever touched yourself?"

    scene meetandfuck23
    with dissolve

    sa "Isn’t that...a little more personal than Noriko’s questions?..."
    n "No way! I talked about my experience {i}and{/i} the fact that I play brony games. That question is way easier than both of those."
    no "Noriko’s right, Sana. Don’t tell me you’re stalling, are you?"

    scene meetandfuck24
    with dissolve

    sa "Of course not...but, umm..."
    sa "I don’t really understand what you mean by “strange...”"
    no "Anywhere {i}socially unacceptable.{/i} Or flat out weird, I suppose. For example, I once pleasured myself in a graveyard. "
    mak "Why?"
    no "I’d be happy to lend you the short story that inspired it. "
    mak "No thanks."
    sa "Um...I guess...it would have to be..."
    sa "The...park near the school..."
    ki "Like...out in the open?"
    sa "Well...it was at night, so..."
    mak "This is somehow even more unbelievable than when I found out the world is-"
    n "Are you...an exhibitionist?"
    sa "I don’t...think so?...I just...I couldn’t help it, so..."
    no "I understand, Sana. Harkening back to the graveyard-"

    scene black
    with dissolve

    mo "Forget the field of the dead! We want more Zagull facts!"
    sa "M-More?!"
    n "You’ve only answered one! I won’t rest until you’ve also exposed something embarrassing and hard to understand!"
    no "In that case-"

    scene meetandfuck25
    with dissolve2

    no "Question two — my {i}lord,{/i} I have forgotten what I was about to ask."
    mo "Oh God, is that a cat pose?! Are those her paws?!"
    sa "I think...poses like this are...better suited to me, so..."
    n "She knows exactly what she’s doing! This is all calculated! She’s not supposed to be this strong!"
    no "{i}Ahem.{/i} Question two — what is your favorite sex position and why?"

    scene meetandfuck26
    with dissolve

    sa "But...I’m a virgin..."
    mo "AAAAAAH I CAN’T DO THIS! "
    no "That changes nothing, Sana. I’m sure there’s at least {i}one{/i} you’re mostly curious about. "
    sa "Then...um..."
    sa "I’ve...always...liked the idea of...being lifted up...and you know..."
    sa "What’s...what’s that...called again?"
    n "I am doomed. "
    no "I will admit that the ekiben is a perfect choice for a girl of your size, Sana. I’d pay good money to witness such an act."
    sa "You’d...pay money...to see that happen to me?..."
    ki "This is the greatest day of my life."
    n "You were on my team a second ago!"

    scene black
    with dissolve

    no "I’d pay {i}a lot{/i} of money for that, Sana. But, unfortunately, the show must go on. Which means that-"
    sa "Do you mind if I just...mnh..."

    scene meetandfuck27
    with dissolve2

    sa "Sliding my leggings down is...okay, right?...Because I don’t think I can beat Noriko unless I...do something like this..."
    mak "{i}Who are you?{/i}"
    ki "For real! Since when is she like this?!"
    no "You’d be surprised how many would show their true colors when placed in a situation where everything will remain confidential. Why do you think I invited Sana in the first place?"
    no "This side of her has always existed, but I was the only one who believed enough to create a reality in which it was revealed."
    no "Isn’t that right, Sana? You’ve always been a little {i}deviant,{/i} haven’t you?"
    sa "Is that...the third question?"
    no "No...my third question is one I don’t already have the answer to."
    no "Question three — what is your single greatest sexual fantasy?"
    sa "You...promise you won’t tell?..."
    no "We all do. That’s part of the agreement."

    scene meetandfuck28
    with dissolve

    sa "Then..."
    sa "I’ve always..."
    sa "Kind of imagined what it would be like to..."
    sa "To maybe...maybe be...assaulted...on the way home from work..."
    r "Assaulted?..."
    r "You don’t mean..."
    no "It means we’ve got a little non-con fetishist here, don’t we?"
    mak "It’s not as uncommon as you’d expect. There are plenty of people who routinely shop for such a genre."
    mak "Just fantasizing about such a thing doesn’t mean you want it to become a {i}reality,{/i} though. Right, Sana?"
    sa "I...don’t really..."
    no "For bonus points — tell us more. How would you like this {i}assault{/i} to happen?"
    n "I never got an opportunity for bonus points!"
    no "You never had an interesting enough answer."
    sa "Well...in my head..."
    sa "There’s a man who comes up behind me..."
    sa "And covers my mouth with his hand...then drags me into an alleyway..."
    sa "He rips open my dress...presses me up against the wall...puts one of his hands around my neck..."
    sa "Then...he tells me he’s going to rape me..."
    sa "But there’s nothing I can do since...he’s too strong...and I can’t speak..."
    r "Ooooookay. I think we’ve heard enough. Thanks, Sana. "
    no "I think not. Please, continue."

    scene meetandfuck29
    with dissolve
    stop music fadeout 15.0

    sa "He slaps me...and I’m crying..."
    sa "Then...he pushes me onto the ground..."
    sa "He spits in his hand...uses it to...ah..."
    sa "But he doesn’t have to...because I’m already..."
    sa "Then he puts it in...and it hurts...and I’m screaming..."
    sa "And kicking...and crying...but he keeps hitting me..."
    sa "He keeps...violating me..."

    scene meetandfuck30
    with dissolve

    sa "Then...finally...it seems like someone is coming to rescue me..."
    sa "But it’s actually just a group of his friends and-"
    no "Shh..."
    no "I think that’s as good a place as any to stop."

    scene black
    with dissolve2

    ki "Are you kidding?! {i}That’s{/i} where we’re going to stop?! That was like the worst place to stop! We didn’t even get to hear the end!"
    no "Yes, but this just means we get to come up with our {i}own{/i} ending. "
    no "Besides, we have two other games to play. And, should you be chosen, you’ll soon find that {i}indulging{/i} any further may just work against you..."

    "{i}Nodokathon Round 1: Complete{/i}"
    "{i}Winner: Sana Sakakibara{/i}"
    "........."
    "......"
    "..."
    "{i}Meanwhile...{/i}"

    $ renpy.end_replay()
    $ sportswars17 = True

    jump sportswars18

label beachfive6:
    scene nodokaattacks1
    with dissolve2
    play music "icantseeher.mp3"

    "I’ve never longed for silken things, nor greener grass or wedding rings.\nJust sex and sleep and songs to sing; a golden crown for silver kings."
    "For on their heads, each strand of hair/each fleck of skin on royal chairs\ndoes naught but argue ‘gainst repair of better things in worsened care."
    "To doubt is not to match the tone of songbirds, strong birds, murdered crows-\nThe point is to reflect and hone the brilliance in each broken home. "
    "I dreamt a dream again last night; against that never-ending light\nEach bright and blinding flash to spite these eyes all but devoid of sight-"
    "And in that dream, as pure as snow. As beautiful as autumn’s glow\nA boy appeared from down below, with skin as smooth as fine merlot-"
    "I spread my arms and then my legs. I welcomed him, he found my eggs\nBut at this point I must separate myself from the scheme that I’ve created because I-"
    "..."
    "Ahh."
    "Mother won’t like this one bit."

    play sound "static.mp3"
    scene nodokaattacks2 with flash
    stop sound

    "Noriko, the good person she is, leaves the room to go find Kirin and I quickly find myself alone."
    "But I’m sure Ayane will show up any minute now to give me a rundown on exactly...what I’m supposed to do?"
    "I know she said she’d handle “recruiting” everyone else that will be coming to our apparent {i}slumber party,{/i} but I’m pretty much free until then, right?"
    "Should I go and track down Chika? Follow Noriko and attempt to smooth things over with Kirin so she no longer feels uncomfortable when the two of us are being terrible together?"
    "Or should I just bite the bullet and drown myself in the ocean before the sleepover ever happens and hope for a brand new start with a brand new mind?"
    "I think that’s the scariest part of learning more about this world right now — how the closer I come to understanding it, the closer I come to finding a way {i}out.{/i}"
    "I just worry that the method I choose will abandon someone else. "
    "And that {i}they{/i} will be forced to suffer several lifetimes worth of anguish while I’m parting legs like Moses did the red sea."

    play sound "knock.mp3"

    "..."

    s "Well, that’s a strange sounding knock for a paper door. "

    play sound "slidedoor.mp3"
    scene nodokaattacks3 with dissolve

    no "I suppose my hands are the only part of my body stronger than my mind."
    s "Nodoka?"
    no "Akira?"
    s "What are you doing here? In fact...how do you even know I’m here at all? I only got here, like...thirty minutes ago."
    no "Word travels fast in this city — and even faster when you already expect the arrival of it."
    s "And you just couldn’t wait to come say hello, huh?"
    no "That’s right. I’ve missed you quite dearly, Father. And I’ve been such a good girl while you’ve been gone. "
    s "No offense, but I very highly doubt that."

    scene nodokaattacks4
    with dissolve

    no "You only doubt it because you’re still stuck on that infantile description of what “good” means while I’ve been painstakingly rewriting it."
    s "That’s a really cute way to admit you completely lack empathy and morals."

    scene nodokaattacks5
    with dissolve

    no "The gods of old never cared for morals, did they? Why should you and I be expected to act any differently when we’re {i}all{/i} gods in our own respect?"
    no "Besides, to say I lack empathy is wildly incorrect when I understand {i}you{/i} better than even {i}you{/i} do."
    s "I understand myself very well. I just also understand that I suck. "
    no "I can suck as well. Would you like to see?"
    s "Nodoka, do you actually want something? Or are you just here because no one else knows how to talk to you for more than three minutes at once?"
    no "I’m very glad you asked, Akira. I’m here because I require your assistance for a little...experiment. "
    s "Experiment?"

    scene nodokaattacks6
    with dissolve

    no "Basically, I need you to make passionate love to me until you’re no longer able to move your limbs. "
    s "Sounds easy enough. But usually “love” is involved in the act of making love. "

    scene nodokaattacks7
    with dissolve

    no "Your harsh words wound me, Father."
    s "You don’t look very wounded, {i}Daughter.{/i}"
    no "Are you up to the task? Or am I going to have to do something to {i}entice{/i} you?"
    s "Nodoka, if {i}you{/i} know I’m here, other people are going to know I’m here. In fact, a few people {i}already{/i} know."
    no "Yes — but they’re all the type who know how to keep secrets, aren’t they?"
    s "Maybe, but-"
    no "Akira, I think you may be underestimating just how “ahead of the curve” I am when it comes to “knowing things.”"
    s "Speaking of which, has Ayane talked to you yet? "
    no "Was she intending to?"
    s "I’m not sure. I can’t remember if you’re invited to our super secret slumber party."
    no "I sense a hint of truth in that wildly uncharacteristic declaration. Would you like to make love to me {i}then{/i} instead? Perhaps let the others {i}watch?{/i}"
    s "What’s going on with you? You’re not typically the type who comes to {i}me{/i} for this."
    no "Of course not. I normally have more important things to do."
    s "So the fact that you want to do this {i}now{/i} means that’s no longer the truth?"
    no "Maybe. Maybe not."
    s "Nodoka-"
    no "My, oh my. It appears that I’m going to have to entice you after all."

    scene black
    with dissolve

    "Nodoka takes a step forward, but I take one back."

    scene nodokaattacks8
    with dissolve2

    "Of course I’m not opposed to having sex with her given that we’ve already done that on numerous occasions- "
    "But this is really {i}not{/i} the time considering that there are a ton of other girls who are going to rush over here the moment they find out I showed up."

    no "So, what’s the quickest way to turn you on? Will showing you my student ID do the trick?"
    s "As someone who apparently “understands” me as well as you claim, shouldn’t that be a thing you already know?"
    no "Perhaps it is {i}because{/i} I understand you that I asked at all?"
    s "Just how horny are you right now? "
    no "I’m not. That’s the problem."
    s "...What?"

    scene nodokaattacks9
    with dissolve2

    no "Could it be that I simply require a distraction from the growing madness within my head? "
    s "I think that’s why masturbation was invented."

    scene nodokaattacks10
    with dissolve

    no "Yes, but what’s the point of {i}that{/i} when people like you exist to satisfy the forbidden desires of people like me?"
    s "Is that why I’m here? Have you finally uncovered the meaning of life after all this time?"

    scene nodokaattacks11
    with dissolve

    no "I’ve uncovered many things, {i}Akira...{/i}but there are so many that I can’t seem to...line up just yet."

    "Successfully enticed, I stop retreating as Nodoka makes her way over to me, grabbing my arm and pulling it toward her crotch."
    "Her fingertips dance across my wrist, teasing me and silently pleading for me to play with her — which I promptly do because she is extremely attractive in that swimsuit."

    s "..."
    no "Will you help me?..."
    s "If you want me to fuck you, just admit it. You don’t have to be all wordy and weird about it."
    no "But that’s precisely what I did earlier. You were the one who asked for an explanation, silly."
    s "Don’t call me silly either."

    scene nodokaattacks12
    with dissolve2

    no "Silly Akira...asking me to stop teasing him when he’s already this hard..."

    "Nodoka reaches forward and begins to massage my cock through my pants, locking eyes with me as her face begins to turn a darker shade of red."

    no "I’m not going to hold back today...are you prepared for that?"
    s "Why now?..."
    no "I simply can’t wait anymore, Father. I’ve been consumed by insatiable lust and must feel you inside of me before I go insane. "
    no "Surely you’ll give me what I want when I’ve allowed you permanent access to my body whenever your heart desires?"
    s "Yeah, but the only times I’ve wanted {i}your{/i} body have been when I’m feeling mentally cornered. And right now-"
    no "{i}Save it...{/i}"

    scene black
    with dissolve2

    no "Take me to the bed...{i}Akira...{/i}"

    "........."
    "......"
    "..."

    scene nodokaattacks13
    with dissolve2

    no "Haah...aah...yes...just like that...{i}Akira...{/i}split me open...give me...your worst..."

    "All things considered, Nodoka is being...kind of normal right now."
    "Like yeah, she’s still {i}Nodoka,{/i} but this really seems like she more or less just wanted me to satisfy her sexual impulses. And that’s fine."
    "But, based on prior experiences, I can’t help but feel like there’s more to this that she isn’t telling me."

    no "Aaaah......{i}aah.....{/i}that feels.....amazing....."

    "I’m gentle with her this time, embracing her from behind as she pushes herself closer to me, forcing me in deeper."
    "The bed gently rocks, but the creaking of it is kept to a minimum by our pace. "
    "I can feel her more vividly than ever before — each curve and contour of her body etches itself into my mind and paints a picture so perfect that I don’t even need to open my eyes to see her."
    "And I’m glad that I don’t, because I fear that it would shake how she’s almost a different girl right now."

    no "Do you like that, {i}Akira?...{/i}Do you like fucking my little pussy?..."
    s "Yes...I love it..."
    no "Yeah?..."
    s "Yeah..."

    scene nodokaattacks14
    with dissolve

    no "Then...would you like to play a little game with me?"
    s "A game?..."
    no "That’s right...and if you can get me to cum before you do...I’ll tell you {i}anything{/i} you want..."
    s "What makes you think there’s something I want you to tell me?..."
    no "The fact that I know more than you...curiosity is...haah...man’s greatest foil...is it not?..."
    no "Surely there must be...{i}something{/i} you want to ask me?..."
    s "And what happens if I lose?...What do {i}you{/i} get?"
    no "I get to cut off your cock and keep it in my purse..."
    s "I feel like the stakes of me losing are significantly higher. "
    no "Then don’t lose..."

    scene nodokaattacks15
    with dissolve

    no "You have a...clear advantage right now...I’m so...{i}so{/i} close...haah....aaah...."

    "I’m fully enveloped by her...I can feel her right hand trembling as I clasp it."
    "Her breathing is labored and sporadic, unlike anything I’ve ever heard cross her lips in the past. And all it does is further the notion that {i}this{/i} Nodoka is somehow different."

    no "{i}Aaah...{/i}Akira...fuck me harder...{i}deeper...{/i}before someone finds us..."
    no "Before I...{i}aah...{/i}cum all over your...massive cock..."
    s "You sure you want to play this game, Nodoka?...You’re like two pumps away from losing..."
    no "Hah....haaah...maybe I just....really want you to ask me something?....Did you ever....ngh....think of that?..."
    s "Yeah, but..."
    no "Stop talking or...you’ll...ruin-"

    scene nodokaattacks16
    with dissolve

    no "HaAaaaAAAaah! Ngaaah!"

    "I thrust harder, finally changing the pace as her body shivers and twitches from the sudden sensation."

    no "Haaah! Aaaah! AAaaaaAAAaaah! Ngh! Right...there! Ravish and...ravage me! Make me...yours! Only...yours!"

    scene nodokaattacks17
    with dissolve

    no "Nghhhhhh!!!!~ Aki...raaaaaa!!!!~"
    s "You’re really cute when you’re like this, Nodoka...I like it..."

    scene nodokaattacks18
    with dissolve

    no "You think...I’m cute?...A girl like me?...You mean it?..."
    s "Yeah...this is way different from how it normally is with us..."
    no "Is that...so?..."

    "She attempts to lock eyes with me, but barely manages to do so on account of the angle. So she tries to shift her body, but I force her right back to where she is and continue to thrust into her."

    no "You...fiend...you’re gonna...make me cum...{i}Akira...{/i}"
    s "At this rate, you’ll do that multiple times before I even get close."
    no "Then...let me work harder for you..."
    s "Hm? Did you say “harder” just now?"

    scene nodokaattacks19
    with dissolve
    play sound "dosex.mp3"

    no "AAAAAAAAAaaaaaaaaAAAAH!!!! It’s so...deep inside me! I can feel...every inch of you!...I’m going...crazy...Akira! Akira!!!"
    s "Cum for me...{i}now...{/i}"
    no "Haaaah....t.....ngaaaah!.....Top!...."
    s "Hm?"
    no "Top! T...Top!..."

    scene nodokaattacks20
    with dissolve

    no "Let me...haaah...get...on top..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nodokaattacks21
    with dissolve2

    no "Haah...aaah...nnfh...I’ve got you now..."
    s "Yeah? Think you’ll have better luck now that you get to take control?"
    no "Of...course I do...{i}silly...{/i}you’ve fallen right into my trap..."

    "Nodoka rides me almost expertly as I grab the back of her head and pull it toward me."
    "It’s the first time I’ve ever felt tempted to kiss her...so my gaze lingers on her lips as her panicked breaths assault my face."

    no "Getting...ngh...close?...."
    s "I’m okay for now...you?..."
    no "I’d have...come...fifty times by now if...I didn’t want a new {i}accessory{/i} so badly..."
    s "Please tell me you’re not {i}actually{/i} going to cut it off if you manage to win this thing."
    no "Maybe I will...maybe I won’t...what’s it matter to you...{i}Aki-kun?...{/i}"

    play sound "static.mp3"
    scene nodokaattacks22 with flash
    stop sound

    s "Ngh!"
    no "Ah! Did that do the trick?"
    s "Nodoka-"
    no "You’re so much harder all of a sudden...I wonder why?"
    s "Please don’t...call me that anymore..."
    no "Why not, Aki-kun?..."

    play sound "static.mp3"
    scene nodokaattacks23 with flash
    stop sound

    s "NGGH!"
    no "Is it because {i}someone else{/i} used to call you that?"
    s "Hah...how...do you..."
    no "{i}I know who you are...Aki-kun!...{/i}"

    play sound "static.mp3"
    scene nodokaattacks24 with flash
    stop sound

    no "You fucked the Girl Who Cannot Breathe!..."

    play sound "static.mp3"
    scene nodokaattacks25 with flash
    stop sound

    no "But that’s not {i}it...{/i}"
    no "You {i}loved{/i} her...and {i}she{/i} loved you..."

    play sound "static.mp3"
    scene nodokaattacks24 with flash
    stop sound

    no "But you feel guilty! You feel {i}sick{/i} because you know you aren’t meant to feel those things!"
    s "N...Nodoka...stop...p...please...."
    no "Shhhhhhhh..."
    no "I’m only saying it because I have to."
    s "But {i}why{/i} would-"

    scene nodokaattacks25
    with dissolve

    no "Akira...look deep into my eyes..."
    s "Hahh......hah.........ngaah...."

    stop music
    play sound "static.mp3"
    scene nodokaattacks26 with flash
    stop sound

    no "{i}Slip.{/i}"

    scene colorbars
    play sound "colortone.mp3"
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene nodokaattacks27 with flash
    stop sound
    play sound "dosex.mp3"

    no "Haaah! Hah! Hah! Yes...fuck!....Fuuuuck!"

    scene nodokaattacks28
    with dissolve

    no "Oh, you {i}wretched{/i} man...you actually almost {i}beat{/i} me..."
    no "But it’s okay...I forgive you, Akira...and I’m sorry..."

    scene black
    with dissolve2

    no "But now the fun {i}really{/i} begins..."

    $ renpy.end_replay()
    $ beachfive6 = True
    $ nodoka_love += 1

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump beachfive7

label beachfive10:
    play sound "static.mp3"
    scene nodokapostnutclarity1 with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene nodokapostnutclarity2 with flash
    stop sound
    play sound "dosex.mp3"

    no "Hah! Hah! Hah! Yes! More! Yes! Fuck! So good! Yes! Shit! Hah! More! "
    no "More! Yes! Hah! Yes! Fuck! So good! Yes! Shit! Hah! Yes! More! Fuck!"
    no "Yes! Hah! Hah! Fuck! So good! Yes! Shit! Hah! More! Fuck! Yes! More!"

    scene nodokapostnutclarity3
    with dissolve4

    no "Yes! Hah! More! So good! Fuck! Yes! Shit! Hah! Hah! Hah! More! Fuck!"
    no "Yes! Hah! So good! So good! Fuck! Yes! Shit! Hah! So good! More! More!"

    play sound "pop.mp3"
    scene nodokapostnutclarity4 with hpunch

    f "..."
    no "..."

    scene nodokapostnutclarity5
    with dissolve

    f "..."
    no "..."

    play music "itsingsinitssleep.mp3"
    scene nodokapostnutclarity6
    with hpunch

    futano "AAAAAAAAAAAAHHHHHHHHHHH!!!!!!!!!!!!!!!!!"

    play sound "static.mp3"
    scene nodokapostnutclarity7 with flash
    stop sound

    f "How did I get here?! {i}When{/i} did I get here?! And what do you think you’re doing?!"
    no "A mysterious pop! Just now! Having sex with...the teacher!"
    no "I am so FUCKING STICKY! Come feel me! Words can not properly describe it! And I’m the word girl so you know I’m telling the truth!"

    scene nodokapostnutclarity8
    with dissolve

    f "Is he unconscious?!"
    no "Yes. I did that. It was for a thing. But no! You have to wait until I’m done to have a turn!"

    play sound "static.mp3"
    scene nodokapostnutclarity9 with flash
    stop sound

    f "I don’t want a turn! I want to know how I got here! I went from playing volleyball to wandering through an upside down school to watching {i}you{/i} guys in a matter of like twenty minutes!"
    no "You jumped! From one world to the next!"
    f "I did what?!"
    no "They’re all on top of one another, you see! And we can move through them!"
    no "You did that! That is what you did! And I knew you would! Or someone would! But it was louder than expected. And I didn’t know when. How are you?"

    scene nodokapostnutclarity10
    with dissolve

    f "Bad! Very, very bad! And confused! And you should probably stop having sex with Sensei while he is asleep!"
    no "He’s not just {i}asleep,{/i} Futaba. He is {i}wandering.{/i} Ethereal! I did that to him with my vagina. My vagina and words. Mostly words. But he was already in the vagina when I used the words. But yes, he’s gone. And also here."

    scene nodokapostnutclarity11
    with dissolve

    f "Can you explain that in a slightly more comprehensible way maybe? I’m seriously freaking out right now."
    no "You look fine to me. Stripes look good on you. Can I watch when you take your turn next? Trick question- I’m going to watch whether you want me to or not. I have extra eyes right now."
    f "Nodoka, {i}please.{/i}"
    no "Sensei is special. He can do what {i}you{/i} did over and over and over and over again. Or at least kind of? His mind leaves. His body stays. But {i}your{/i} body moved. How did you do that? Are {i}you{/i} special too?"
    f "I-"

    scene nodokapostnutclarity12
    with dissolve

    no "Trick question again! Of course you are!"
    no "You are because {i}she{/i} was! And {i}she{/i} had the key to the attic! She was the one who collected the groceries! That supple body, mangled by the cock of time! So special she was!"
    no "What was there?! What did you see?!"

    play sound "static.mp3"
    scene nodokapostnutclarity7 with flash
    stop sound

    f "I-"

    play sound "static.mp3"
    scene futabatimeyo20 with flash
    scene futabatimeyo15 with flash
    scene futabatimeyo13 with flash
    scene futabatimeyo40 with flash
    scene futabatimeyo33 with flash
    scene futabatimeyo28 with flash
    scene nodokapostnutclarity13 with flash
    stop sound

    no "You mentioned it was upside down, yes? Were you? Did you walk on the ceiling or the floor? Was Kyoko there? Did you see her too? What did she say? What did she look like?"
    f "I...don’t even know if it was real..."
    f "But...why would your mom be there?"

    scene nodokapostnutclarity14
    with dissolve

    no "That’s what I’m trying to figure out, damn it! Do you think I’m on here on vacation?! This is work! So don’t burden me with this “real” or “not real” bullshit! It’s all real, Futaba! Some things are just {i}somewhere else!{/i}"
    f "Nodoka...please calm down...you’re scaring me..."

    scene nodokapostnutclarity15
    with dissolve

    no "Hm. You know, maybe you {i}do{/i} look different? Paler."
    no "How do I know you’re the real Futaba? What’s my favorite number? Hint — it’s the same number as my vaginal depth in inches. You should know. A friend would know."
    no "Actually, forget my vagina. It’s full of Sensei’s milk right now anyway. You don’t like milk. You’re lactose intol- wait, no. That’s Otoha. Do you like milk? What kind of milk do you like?"
    f "I-"

    scene nodokapostnutclarity16
    with dissolve

    no "Forget the milk! I’ll explain everything!"

    play sound "static.mp3"
    scene nodokapostnutclarity15 with flash
    stop sound

    no "What you experienced was no illusion. You wandered through a gate. Or perhaps a gate was opened for you. Either way, gate. And that gate took you from {i}there{/i} to {i}there{/i} to {i}here.{/i}"
    no "But here’s the rub, Futaba — I can’t go through those things. I can’t find any. But I know they’re there because she {i}says{/i} they’re there."

    scene nodokapostnutclarity16
    with dissolve

    no "And she isn’t crazy! Neither am I! They exist! We can go anywhere we want! We just have to figure out how and when!"
    no "And with people like you and the guy who just came in me five hundred times, that should be doable!"
    f "But, Nodoka...I didn’t even do anything..."
    f "I seriously just...got tossed around a few times...are you sure I didn’t just...walk in here? You were clearly very busy, so...it’s possible you didn’t notice?"

    scene nodokapostnutclarity17
    with dissolve

    no "That’s not possible at all. I see everything. You went “pop.” I heard it myself. And then we screamed. Do you remember that? Why would you scream if you walked in? You wouldn’t. That’s dumb."
    f "Maybe I...blacked out like Sensei does?...And {i}that’s{/i} why I can’t remember? Let me ask Molly and Yasu. They’ll know what-"

    scene nodokapostnutclarity18
    with dissolve

    no "Leave that damn fanatic out of this! Her fucking sermon is what pushed me into this rabbit hole in the first place and now I can’t fucking climb out of it, Futaba!"
    no "She only knows a part of the truth! But this hole is deeper than that!"
    no "We’re talking thousands- no, millions! {i}Billions{/i} of universes smushed together like a fucking mille crepe and she has the audacity to claim there are only {i}two?!{/i} TWO?!?!?!?!"

    scene nodokapostnutclarity19
    with dissolve

    no "She did help a little bit, though. Albeit mostly unintentionally. But that’s just because I’m a fucking genius and decided to go through some older notes. They took a while to find, but they were there."
    no "And I’m really glad they were because the only ground I’ve broken lately has been all about Akira’s sexual history and that is only relevant in regard to {i}this{/i} world. Probably. That’s why I fucked him into a coma."
    f "Akira?..."
    s "Well, I guess Futaba knows my name now too..."

    scene nodokapostnutclarity20
    with dissolve

    no "Ah! Welcome back. Where did you go? What’d you see? Futaba went too. That one wasn’t my fault, though. She managed to do it on her own. She’s so very, very, very very very very very smart!"
    s "I didn’t {i}go{/i} anywhere. And I’d really appreciate it if you could never say any of that stuff to me again."
    no "Yeah, I can’t make that promise. But if it’s any consolation, I took very good care of you while you were unconscious!"
    no "I even licked the drool off. It wasn’t very flavorful. Also, I might be pregnant now. Let’s come up with a name together!"

    scene black
    play sound "tackle.mp3"

    no "I’ll go get my notebook! Please hold!"

    play sound "slidedoor.mp3"

    f "Nodoka, wait-"

    play sound "static.mp3"
    scene nodokapostnutclarity21 with flash
    stop sound

    "Futaba tries her best to fill me in on exactly what I’ve woken up to, but...I’m not sure I understand."
    "And so I find myself now in the midst of another one of Nodoka’s manic rants as she rattles off a bunch of baby names with my cum still smeared all over her lower body."
    "I have no idea how {i}long{/i} I was out, but I imagine it was at least an hour based on how exhausted I feel and...how gross she looks."

    f "Are you really going to...list baby names instead of talking more about how I mysteriously just...appeared in this room with you two?"

    play sound "static.mp3"
    scene nodokapostnutclarity22 with flash
    stop sound

    no "Yes. I’ll begin with the first names of some famous writers since Akira and I both enjoy writing and so will our child. Isaac. Orson. Octavia. Mary. Alastair. Philip. Kurt. Margaret. Jules. Douglas. Samuel."
    no "Out of that list, I’d recommend Orson since it would cover both Welles and Scott Card."
    no "But I’m also willing to land on Philip if we can tack on the middle name Kurt since we already got the Dick part out of the way. Fun times, right?"
    s "Nodoka...if you know something, please tell us. Because the whole reason I even came to the beach in the first place is to investigate weird time stuff."

    scene nodokapostnutclarity23
    with dissolve

    no "Are you no longer mad at me for forcing you to recollect all of the sex you had with one of my favorite poets?"
    f "{i}What?{/i}"

    scene nodokapostnutclarity24
    with dissolve

    no "And are {i}you{/i} no longer mad at me for forcing you to recollect all of the sex you had with our teacher?"
    f "Of course I’m mad! I’ve just never had to deal with teleportation before, so excuse me if I’m prioritizing that over our friendship right now!"
    s "Lucky. I have to deal with that at least once per week."

    scene nodokapostnutclarity25
    with dissolve

    no "Wrong! You do not {i}teleport,{/i} Akira! You slip into a mental state somewhere between {i}conscious{/i} and {i}unconscious{/i} and act on impulse and instinct rather than interest!"

    scene nodokapostnutclarity26
    with dissolve

    no "Or at least that’s what {i}most{/i} would believe. But {i}most{/i} are not Nodoka Nagasawa. And Nodoka Nagasawa thinks she knows what’s {i}really{/i} going on here."
    s "So if I’m not just on auto-pilot when I black out...what do {i}you{/i} think is actually happening?"
    no "It’s still auto-pilot in a sense. Just it isn’t instinct or impulse guiding you."
    no "It’s {i}memory.{/i}"

    scene nodokapostnutclarity27
    with dissolve

    no "December 28th — I found it. A letter from another me, tucked away in a place that God himself could never find."
    no "I didn’t know where to look until I wrote it. But the moment I did, and the moment I left, I felt a presence within me as if it had emptied everything else out."
    no "I was following myself. I had carried this cross before. And it did not matter how many times my knees would buckle along the way as I had already reached the end once."
    no "But when the new end finally came, it was the beginning — for the words were the same..."

    scene nodokapostnutclarity28
    with dissolve

    no "But the crescent-moon shaped coffee stain in the upper right corner was now in the bottom left."
    f "Um..."
    s "So-"
    no "{i}Don’t you idiots get it?{/i}"
    no "It’s all a broken record. We’re {i}repeating.{/i}"
    no "Everything we do, and everything we think is not the result of conscious thought, but a predetermined script that we’re simply-"

    play sound "static.mp3"
    scene nodokapostnutclarity29 with flash
    stop sound

    no "NGH!!!!"

    play sound "static.mp3"
    scene nodokapostnutclarity30 with flash
    stop sound

    f "N-Nodoka? Are you okay? What’s going on?"
    no "These...fucking headaches! Every day! They won’t stop! I can’t...think! Or rather...{i}something{/i}...doesn’t {i}want{/i} me to think!"

    "She...figured all that out?"
    "All on her own?..."

    no "NGH.....GAAAAAH!!!!! FUCK!!!!!!"

    play sound "window.mp3"
    scene nodokapostnutclarity31 with hpunch

    f "Nodoka?!"
    no "FUCK! FUCK FUCK FUCK!"
    f "Do you...need an ambulance?!"

    "She knocks something over but I don’t care to look at what it is right now since I know this is bigger than that. And that...worries me."
    "She’s so close...but {i}something{/i} really is trying to stop her from figuring things out. And I’ve never..."
    "I don’t..."
    "I have no idea what will happen if she keeps fighting back against it."

    no "I don’t...need an ambulance! I need answers!"
    no "I can’t...end up like her! I can’t! I won’t! I...NGAAAAH! FUCK YOU, BRAIN! FUCK YOU, GOD! YOU CAN’T...HIDE...FOREVER!!!!"
    f "I have to...do something about this. She’s clearly not well."

    scene nodokapostnutclarity32
    with dissolve

    no "I’m...fine! It’s everyone else who’s unwell! You’re all...still whole! You walk so...unburdened by the weight of your other selves! You think you’re free, but you’re not! You’re actors! Characters! It’s all happened before!"
    f "Come on...let’s get you dressed and back to your room, okay? Your...research or whatever it is can wait until tomorrow."
    no "A...Akira! You know too! I...can tell! You know...I’m not insane! But she...she never had that! She never had...someone like you!"

    scene nodokapostnutclarity33
    with dissolve

    s "..."
    no "Everything...I do...NGAAAAAH! It’s all...to break the mold!...To liberate us!"
    no "You believe me!!! I know you do!!!!"
    f "Nodoka, come on. You have to get cleaned up before you put your swimsuit back on."

    play sound "slidedoor.mp3"

    no "{i}Don’t...touch me! I’m not done with him! He needs to tell me what he saw! Where he WENT!{/i}"
    f "{i}I’ll tell you MY story again, okay? Tomorrow. You need to rest right now.{/i}"
    no "{i}Akira!!! Let me stay!!! Let me stay!!!{/i}"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I really didn’t go anywhere."
    "When I passed out, it was all just dark."
    "And the sound of a creaking bed, just as it had done so many times in the past, kept me suspended somewhere between conscious and unconscious."
    "I felt every twitch..."
    "Every scratch..."
    "Every ejaculation..."
    "..."
    "Or maybe I didn’t."
    "Maybe I just remember them."
    "..."
    "I have to talk to Ayane."

    $ renpy.end_replay()
    $ beachfive10 = True
    $ nodoka_love += 1

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump beachfive11

label halloweennodoka1:
    scene otohanodokaphone1
    with dissolve2

    "On the other end of the room, which was more accurately the center of the room, which was more accurately the center of the world right now, something was happening."
    "A girl who had spent most of the day alone after dropping pipe bombs all over every bridge she could find was calling a girl she was genuinely worried about."
    "Knowing that Nodoka Nagasawa had more than just a few screws loose, Otoha Okakura was presently afraid that her head might have fallen off of her shoulders and been picked up by a horny straggler somewhere."
    "And while the two of them had made promises in the past to never bother one another, Otoha had a built track record of intentionally breaking promises, so that didn’t really matter to her right now."
    "All that {i}really{/i} mattered was checking on her friend and making sure she wasn’t about to jump off of a roof."

    play sound "static.mp3"
    scene otohanodokaphone2 with flash
    stop sound
    play music "itsingsinitssleep.mp3"

    "And she wasn’t! "
    "But that guess wasn’t too far off."

    no "It’s here, it’s here, it must be here. That’s what the letter said. Which polyrhythmic arbiter paints pickled plums in red?"

    "Nodoka Nagasawa hated poetry just like she hated the sound of chalk on a chalkboard. She reveled in the nails instead — that familiar screech that brought her back to now sepia-tinted days full of spoons."
    "She was currently (but not blissfully) unaware that someone was trying to get in contact with her. Just like she had been unaware on her walk to the highest place in Kumon-mi."
    "If this even {i}was{/i} the highest. If anyone even {i}was{/i} trying to contact her. If this even {i}was{/i} Nodoka Nagasawa and not a different girl wearing her clothes."
    "With each step, she comes closer to an inconvenient truth — one that she was not built to house as there were houses built for {i}her.{/i} "
    "No. That wasn’t right. They weren’t for her. But they could be {i}shared{/i} with her under the right pretext."
    "Somehow, {i}some{/i} way, she would set foot inside this metaphor dressed as a simile — personifying its intangibility through unconventional means like dream sequences and unintelligible anecdotes."
    "But before that, she had things she needed to learn. She had truths she needed to pluck from the dirt before acting as a mother bird to a mother-bird."
    "Yet she’d rather {i}smother{/i} birds because {i}other{/i} words pushed her so far in the opposite direction of her predecessor that she’d sidelined one story and wound up in another."
    "As the light of last summer shone down on an upside down house, she questioned whether her feet kissed the floor or the ceiling. That’s the funny thing about roofs, you see."
    "They’re two things at the same time, serving different purposes for different people. "
    "That’s what Nodoka Nagasawa was here to do as well. It wasn’t enough to just choose one anymore. She cared too much now. If she didn’t, she wouldn’t be here. Right? "
    "No one person can be {i}that{/i} curious, don’t you think? That makes {i}me{/i} curious, though."
    "I wonder what face she’ll make when she realizes her fountain pen has run out of ink."
    "Perhaps there is more in a well somewhere."

    play sound "static.mp3"
    scene otohanodokaphone1 with flash
    stop sound

    "To Otoha again."

    play sound "static.mp3"
    scene otohanodokaphone3 with flash
    stop sound

    no "What?!"

    "To {i}both{/i} of them this time — two sides of one coin, just one of them was blank and the other was rusted."

    o "I’m doing great. And you?"
    no "Do you have any idea how much of a thorn in my paw you’ve been today?! I’d be better off letting you infect me and amputating myself at this point!"
    o "Yeah, I love you too. I’m really happy to hear you finally admit it."
    no "What the fuck do you want?! I’m busy trying to save your fucking life!"
    o "That’s gonna be hard to do with you...wherever the fuck you are right now as you’re most definitely not with me."
    no "I’m at school! I’m learning! That’s what people do here, motherfucker! Now either come here and help or delete my number! "

    scene otohanodokaphone4
    with dissolve

    o "What do you mean you’re “at school?” School ended hours ago. I thought you were in your room?"
    no "Yes! And then I figured something out because my worthless but extremely hot roommate stopped pestering me for the sole purpose of making it seem like she isn’t feeling utterly alone!"
    o "Damn, yo. You’re just gonna call me out like that?"

    scene otohanodokaphone5
    with dissolve

    no "That’s right. Now go lure some other unsuspecting lesbian into a relationship and leave me out of it. At least emotionally. I can fuck you when I get home tonight. Just keep your mouth shut."
    o "Why are you really at school, Nodoka? What are you planning on doing there? Because every time you wander off in the middle of these episodes-"

    scene otohanodokaphone6
    with dissolve

    no "They aren’t “episodes!” They’re moments of heightened brilliance! I’m transcending! I can see everything, damn it! Don’t call me insane just because everyone else is blind!"
    o "Well then...what do you see this time?"

    scene otohanodokaphone5
    with dissolve

    no "Nothing yet because you can’t listen to fucking directions. I think...something is going to happen, though."
    o "Something as in...{i}what{/i} exactly?"

    scene otohanodokaphone7
    with dissolve

    no "I’m still working on that part. All I know is I told myself to come here, I’m just not sure {i}when.{/i}"
    o "Does alternate timeline Nodoka not believe in dating her notes or something?"
    no "Give me a fucking break. If this was as simple as reading my own notes I wouldn’t be five minutes away from throwing myself off of the fucking roof."
    no "There’s a code. One that I’ve figured out because I’m a fucking genius. And also probably because it was me who made it. But even finding where I hid them is-"
    o "Yeah, yeah. {i}Outside{/i} the barrier, right?"

    scene otohanodokaphone8
    with dissolve

    no "Do not {i}mock{/i} me, whore! Just because I can reach places you can’t even comprehend does not mean those places do not {i}exist!{/i}"
    no "And also, please allow me to add that I {i}do{/i} date my notes, BUT THAT DOESN’T FUCKING MATTER WHEN THE DATE IS THE SAME AS TODAY!"

    scene otohanodokaphone9
    with dissolve

    o "Listen, Nodoka...I’m glad that you’re not getting those headaches anymore, but if you’re going to keep putting yourself in danger like this, maybe you should...you know...{i}see someone.{/i}"
    no "I’m already {i}seeing{/i} Akira. And I’m pretty sure his precum contains some sort of divine aphrodisiac as he gets me even wetter than you’d be during recess at an elementary school for boys."
    o "I meant a {i}doctor,{/i} idiot. Because I’m all about letting you “do your thing,” but not if it means hearing you’re five minutes away from “throwing yourself off the fucking roof.”"
    o "Like, you’d come after me if I started writing music while tightrope walking, wouldn’t you?"
    no "No. That would be fucking awesome. And even if it wasn’t, you can die for all I care. Maybe then I’d be able to get some peace and fucking quiet."
    o "You don’t mean that, Nodoka. Just...go home, okay? You need some sleep. You’ll think better in the morning."

    play sound "static.mp3"
    scene otohanodokaphone10 with flash
    stop sound

    no "I don’t {i}have{/i} until the morning! When I said that something is going to happen, I meant something is going to happen {i}tonight!{/i} Something I need to get to the bottom of before I fucking {i}forget!{/i}"
    o "Nodoka..."
    no "Don’t “Nodoka” me you angel-voiced idol fucker! You haven’t the {i}faintest{/i} idea how many of times I’ve done this and failed! And neither do I! That’s the whole fucking point!"
    o "Then why keep trying?! It’s driving you insane! And no one has any idea what you’re trying to do in the first place!"
    no "Neither do I! That’s why I haven’t succeeded yet!"
    o "Okay, correction — it’s not {i}driving{/i} you insane. You {i}are{/i} insane. And now, you’re making things even worse for yourself by sneaking off to school in the middle of the night presumably naked."
    no "I’m not naked this time! I didn’t want to risk getting sexually assaulted by someone who doesn’t excrete an aphrodisiac from their genitals! I don’t have time for that! Or...maybe I do?!"

    scene otohanodokaphone11
    with dissolve

    no "I have no fucking idea anymore! What even {i}is{/i} time?! Because it’s entirely possible we’ve fucking had this conversation already and we’ve just been forced to forget it!"
    o "Nodoka!"

    scene otohanodokaphone12
    with dissolve

    no "Maggots."
    o "...What?!"
    no "Shiori was dead for {i}a full week{/i} before they found her. And by the time they did, maggots had already eaten their way into her stomach. Can you ignore {i}that,{/i} Otoha?"
    o "I have no fucking clue what you’re talking about right now."
    no "Because {i}you{/i} have never smelt the dead! She was loved! There’s no way they didn’t know! Something- {i}someone{/i} rewrote them! The same thing is probably happening to us!"
    o "Nodoka...maybe it’s time to put your mom in a home. Because I’m starting to think that being around her-"
    no "A home for who?..."
    no "Those who are misunderstood?..."
    no "Those who are only {i}called{/i} insane because no one believes them?! What they’ve been through?!"
    no "Do {i}I{/i} need to be put into a “home” as well then, Otoha?! "

    scene otohanodokaphone13
    with dissolve

    no "Do {i}I{/i} need to suffer because no one else can keep up?! You are supposed to be on my side! You’re supposed to see the world through my eyes! That’s why I share them with you!"
    no "But now you just want to spit on them and roll them through the mud and fucking shit on them, Otoha?! You’re shitting on my eyes! You’re going to make me blind!"
    o "Nodoka-"
    no "No! I’m tired of it! I’m tired of being the only person with a chance to break the mold! I wish nothing more than for the rest of you to be geniuses too! But I guess I’m just {i}fucked,{/i} huh?!"
    o "Nodoka!"
    no "I guess this burden is {i}mine{/i} to bear just like hers! I guess I have to fix two worlds instead of one! And I guess if I {i}don’t{/i} I’m just gonna fuck my teacher forever! {i}Forever!{/i} That’s so much fucking!"
    o "Nodoka! Listen to me!"
    no "Don’t get me wrong — he makes me cum harder than any toy and smut combination ever could! But {i}forever?!{/i} I will {i}obviously{/i} get bored! That’s probably why I’m trying to contact myself in the first place!"
    o "Nodoka!"

    scene otohanodokaphone14
    with dissolve

    no "{size=+20}WHAT?!?!?!{/size}"

    play sound "static.mp3"
    scene otohanodokaphone15 with flash
    stop sound

    o "..."
    no "..."
    no "Woah, what the fuck?"
    o "What do you mean “what the fuck?” You’re freaking me the hell out. {i}That’s{/i} “what the fuck.”"
    no "How...long have you been there exactly?"

    scene otohanodokaphone16
    with dissolve

    o "I’ve been here the whole fucking time! We came here {i}together!{/i} I literally helped you jump the gate!"
    no "Wait, really? Then who was I just talking to on the phone just now?"
    o "No one! Yet you keep on doing it and {i}that{/i} is freaking me the fuck out too! "

    scene otohanodokaphone17
    with dissolve

    o "Listen, I know you brought me here because you have, like...some super genius plan you’re trying to take care of or whatever, but I {i}can’t{/i} let you keep doing this."
    o "I’ve barely even {i}slept{/i} lately because you keep fucking waking me up in the middle of the night, dude. "
    o "And I get that you’re against it and everything, but I {i}really{/i} think you need to see a shrink or something, Nodoka. This shit’s gone way too far. "
    o "You’re losing yourself, man. And if you keep this up, you’re gonna lose {i}me{/i} too. "
    o "I know that’s not what you want. I know you think you’re doing this {i}for{/i} me or...{i}us{/i} or...whoever you say you’re doing it for. But this isn’t what we want."
    o "Maybe...time {i}is{/i} repeating. Maybe you {i}are{/i} right. But none of {i}us{/i} know that. So isn’t it better if we all just...stay in the dark?"
    no "..."
    o "..."
    o "Well?"
    no "Holy shit."
    no "I really am fucking insane, aren’t I?"

    scene otohanodokaphone18
    with dissolve

    o "Maybe not if you’re actually willing to admit it now..."
    o "But either way, can we go home? Because now I’m just tired and {i}confused{/i} and...know what? How about I buy you dinner or some shit on the way back? As...thanks for trying to...{i}save us.{/i}"
    no "..."
    o "Anything you want. Just name it."
    no "I want a whole fucking rotisserie chicken. "
    o "...Really?"
    o "{i}That’s{/i} what-"
    no "And lemonade. "
    o "T-"
    no "{i}Two{/i} lemonades."
    o "..."
    no "And JagaRico."

    scene black
    with dissolve2

    o "Sure, Nodoka. "
    o "You can have an entire rotisserie chicken, two lemonades, and some JagaRico."

    "........."
    "......"
    "..."

    scene otohanodokaphone19
    with dissolve2

    o "You know, maybe we should look into getting you micro-chipped or something? Because if you ran off on your own tonight and I {i}wasn’t{/i} here to talk you down, who knows what could have went wrong?"
    no "I’d probably be naked. Or mostly naked. I like being naked when I hear things. And the rest of the time. I wish we were all naked, all the time. That’s the world I really want."
    o "Well, do you want to know what world {i}I{/i} really want? One where my roommate isn’t a fucking lunatic and doesn’t force me to skip out on parties just to watch her talk to herself on a roof."
    no "I’m...sorry, Otoha. This is...kind of weird for me."
    no "I’ve never really contemplated the fact that I’ve been actually {i}seeing{/i} things before. This is a huge fucking curveball, huh? Why didn’t past me say anything?"
    o "Because “past you” probably doesn’t even exist. This could all be one huge fucking hallucination that-"
    q "Ahem."

    scene otohanodokaphone20
    with dissolve2

    stop music fadeout 3.0

    o "That..."

    scene otohanodokaphone21
    with dissolve2

    no "..."
    o "..."

    play sound "static.mp3"
    scene otohanodokaphone22 with flash
    stop sound

    q "Ah, crap. "
    no "{i}You...{/i}"
    no "You’re...the one she..."

    scene otohanodokaphone23
    with dissolve

    q "I’m sorry, Nodoka. "
    q "I tried."
    no "...What?"

    play sound "pop.mp3"
    scene otohanodokaphone24 with hpunch

    "{i}[[REDACTED] has left the chat!{/i}"

    no "...What?!"
    q "{i}Ahem!{/i}"

    scene otohanodokaphone25
    with dissolve2

    no "..."

    play sound "static.mp3"
    scene otohanodokaphone26 with flash
    stop sound

    k "Nyaa~"

    $ renpy.end_replay()
    $ halloweennodoka1 = True

    jump halloweenfive6

label nodokainvite1:
    play music "broken.mp3"
    scene pfb

    "have you ever wanted a perfect face well now you can have one with the all new perfect face boy face sold separately"
    "now whenever you walk into a room all everyone will think about is how perfect your face is and they will ignore the rest of you it’s just like what you want isn’t that awesome i think it is"
    "anyway do you remember that time you got rug-burn from wrestling on the rug i don’t think you do but i do that was a really fun day i guess it wasn’t really wrestling though"
    "if you and i were perfect face boy what do you think we’d see when we look at each other"
    "i want to remember all those other things we said and thought and did"
    "i still want perfect hair forever"

    scene nods1
    stop music

    "I tap on Nodoka’s name in my phone and think about blowing my brains out."

    play sound "phonebeep.wav"

    no "Rain King."

    play music "memories2.mp3"

    s "When do you think we’ll be able to go home today?"
    no "Not until the well runs dry. "
    no "You know what they say about leaving before we’re supposed to."
    s "Do I?"
    no "I hope so. That’s the only reason we know each other."
    s "I can remember {i}that{/i} at least. But I still don’t get why we always have to close our eyes."
    s "What do you think they do while we can’t see each other?"
    no "I can always see you. Even when I close my eyes."
    s "Really?"
    no "There’s a computer monitor in my childhood home. It never turns off."
    no "She insists on keeping her eyes glued to it in a way that only someone with alogia could. You’d feel terrible to see her."
    s "I bet she’s beautiful, though — if she has anything to do with you."
    no "I’ve seen pieces of her scalp come off with the brush before. It’s such a sad thing. She can barely even eat, that old dame."
    s "Is it still growing?"
    no "It shrinks. Day by day. Her hair is turning gray. Yet all I can do is pray I don’t end up that way."
    s "I’ve been thinking about buying Perfect Face Boy."
    no "For who?"
    s "For me."
    no "Why?"
    no "You don’t have to do that."
    s "My mom said it might make me better."
    no "You’re already as good as you can be."
    s "It isn’t enough."
    no "It’s enough for me."
    s "...."
    no "Say..."
    no "If I ever break, will you be the one to look after me?"
    s "Me?"
    no "I can think of no one better to comb the scalp out of my hair."
    s "Of course, Nodoka."

    scene black
    with dissolve2

    s "Anything for my little sister."

    scene nods2
    stop music
    play sound "hummmm.mp3"
    $ renpy.pause(19, hard=True)
    scene mall2
    stop sound
    play music "mall.mp3"

    "I tap on my left hand instead of my phone and it activates phonebeep.wav anyway because nothing is real."

    show chikachappy
    with dissolve

    c "Sensei! Hi! What are you doing here?"
    s "Hi, outdated Chika sprite. I'm trying to contact Nodoka."
    s "How did we even get inside of the mall? Isn’t it supposed to be closed for renovations?"
    c "Not that I know of. But I’m Chika from the {i}past.{/i} You know! Like, {i}before{/i} you took advantage of my desire for love and stability and let me think we were a couple for years."
    s "How does Chika from the past have knowledge of the present?"

    play sound "static.mp3"
    hide chikachappy
    scene nods3 with flash
    stop sound
    play sound "theholelol.mp3"

    c "{b}{size=+15}STOP ASKING STUPID QUESTIONS!{/b}{/size}"

    play sound "static.mp3"
    scene mall2 with flash
    show chikachappy
    stop sound

    c "Anyway, if you came here for Perfect Face Boy, we’re all sold out. Some girl with a flower in her hair just bought the last one. Something about “market research” I think?"
    s "Damn. I’m going to have to figure out a different birthday present for Nodoka, then."

    show chikacsurprised with dissolve
    hide chikachappy

    c "Who’s this Nodoka girl you keep talking about? Is she from Ms. Matsubara’s class?"
    s "Who?"
    c "Oh. Sorry. Who’s this Nodoka girl you keep talking about? Is she from Ms. Watabe’s class?"
    s "No, she’s from that other school that hasn’t sunken into the ground yet. She’s a bit of an enigma, but I think her heart is in the right place most of the time."
    c "Where is it the rest of the time?"
    s "Probably Ami’s underwear drawer. Where would {i}you{/i} hide human remains, Chika?"

    show chikacveryhappy with dissolve
    hide chikacsurprised

    c "Hahah! Wouldn’t {i}you{/i} like to know?"

    show chikachappy with dissolve
    hide chikacveryhappy

    c "Anyway! I’ve gotta run, Sensei. My break is almost over. "
    c "But if you ever feel like luring someone into a false sense of romantic security before entirely shattering their world view by fucking all of their friends, feel free to drop by again!"
    s "Thanks, Chika. I think I will. Good luck with Perfect Face Boy."
    c "Thanks, Sensei! Good luck with contacting that Nodoka girl!"

    scene black
    with dissolve2

    "I manage to leave the mall through a meat-filled crack in the wall before returning home for a quick change of clothes and starting over."

    stop music
    scene bedroom_noon
    play sound "phonebeep.wav"

    "I tap on Nodoka’s name in my phone and wait for her to answer."
    "........."
    "......"
    "..."
    play sound "phonebeep.wav"

    no "{i}Ahem.{/i}"

    play music "icantseeher.mp3"

    no "I would like to sleep like a cat."
    s "..."
    s "What? Like, now? Did I wake you up?"
    no "With all the fur of time...and a tongue rough as flint."
    s "Uh..."
    no "With the dry sex of fire...and after speaking to no one, stretch myself over the world. Over roofs and landscapes...with a passionate desire to hunt the rats in my dreams."
    s "Well, I’m glad to hear you’re doing fine."
    no "And I’m surprised to hear you didn’t recognize that poem, Akira. Not a fan of Chilean diplomats? "
    s "Yeah, can’t say that’s a major area of expertise for me. What are you up to right now? Besides being weird, I mean."
    no "A bit of this...a bit of that. All in an effort to make the world a better place, of course."
    s "Well, how about putting that on hold and coming over to my place for a little while?"
    no "Oh?"
    s "So long as you promise not to coax me into a state of unconsciousness via sex again."
    no "Aww...But I took such good care of you while you were out. "
    s "That doesn’t change the fact that it was {i}kind of{/i} weird and creepy."
    no "Then, how about I make it up to you by letting you bed {i}me{/i} the next time I slip into a state of unconsciousness?"
    s "Or we could just have normal, conscious sex together. That works too."
    no "Does it?"
    s "Does...Does that just not do it for you? Or..."
    no "It just sounds to me that this is a...{i}recreational{/i} booty call, rather than the type I’ve grown accustomed to from you."

    if beachwars17 == True:
        s "What about that time I summoned you for an encounter with the proprietor of a local cafe?"
        no "What about it?"
        s "Well, {i}that{/i} was recreational, wasn’t it?"
        no "Was it?"
        s "I...uhh..."

    s "Are you coming or not? I can also come to you if-"
    no "I’ll be there shortly, Akira. I’ve already hailed a cab. "
    no "Now, please describe in vivid detail the things you plan on doing to me as I place you on speaker from the backseat of this car."
    s "I hope you’re ready to study, because that’s all we’re going to be doing today."
    no "Heh..."
    no "I’ll see you soon."

    scene black
    with dissolve2
    play sound "phonebeep.wav"

    "........."
    "......"
    "..."

    scene nods4
    with dissolve2

    "Nodoka arrives about ten minutes later, prompting me to question why more people don’t just take taxis after I invite them over."
    "That question is quickly answered when I remember the type of crowd I typically invite over and how they likely don’t have much pocket money."
    "Now, {i}relatively famous authors,{/i} on the other hand..."

    no "I have to say...I’m quite intrigued by whatever is going on here, Akira. I didn’t believe I was on the list of girls you were willing to see {i}casually.{/i}"
    s "You’re going to be even more surprised when you find out I called you over to ask for your hand in marriage. "
    no "Ahh, I see. And in lieu of a ring, I presume you’re going to offer up your body instead?"
    s "Would you rather the ring?"
    no "You can give that to Otoha instead. She can add it to the collection. Your warm embrace is all {i}I{/i} care for, Akira."
    s "Then-"

    scene nods5
    with dissolve

    no "But {i}first,{/i} I have a...surprise for you."
    s "What...kind of surprise? You didn’t bring a bag. And I don’t see any-"
    no "Perhaps it’s something I have on beneath my clothes? Perhaps it’s an...{i}act of service?{/i} Perhaps both. Perhaps neither."
    no "The allure is in not knowing. Don’t you want to find out?"
    s "..."
    no "Unless you want to just have {i}boring{/i} old, consensual missionary sex."
    s "I actually think that would be really hot with you."

    scene nods6
    with dissolve

    no "I suppose it would, wouldn’t it? It’d be very uncharacteristic without one of us forcing the other into a state of delirium. "

    scene black
    with dissolve

    s "Yeah. But I don’t get to experience “surprises” very often, so I’ll go along with it this time. "
    s "Just so you’re aware, though, we {i}will{/i} be having consensual missionary sex the next time you come over. Whether you like it or not."
    no "{i}Ahh, yes. Spoken just like a man who doesn’t know the meaning of the word “consent.” This is why I keep you so close to my heart, Akira.{/i}"
    s "Wait, why do you sound so far away all of a sudden?"
    no "{i}Hm? You’ll have to speak up. I can’t hear you from your daughter’s room.{/i}"

    scene nods7 with hpunch

    s "What?"
    no "{i}Wow. It’s quite...feminine in here, isn’t it?{/i}"

    play sound "static.mp3"
    scene nods8 with flash
    stop sound
    play sound "doorslam.mp3"
    with hpunch

    s "Nodoka — I’d really prefer it if you {i}don’t{/i} go exploring inside of Ami’s room. Especially if you’re going to lock me out of it."
    no "{i}Why is that, Akira? There’s not something you’re trying to hide from me in here, is there?{/i}"
    s "What? No. It’s just weird and Ami has been particularly creepy lately. I wouldn’t want her coming home and-"
    no "{i}Hurting me? A cute little thing like her? Do you think she could manage it?{/i}"
    s "I’m thinking a lot of things right now. And almost all of them have to do with the fact that you came over and immediately tricked me into closing my eyes so you could invade Ami’s privacy."

    play sound "static.mp3"
    scene nods9 with flash
    stop sound

    no "But I’m doing this for {i}you.{/i} This is the surprise I was talking about. You just need to let me prepare first."
    s "{i}Prepare what? Because that implies some level of intent and I highly doubt you’ve been plotting this out for longer than five minutes total.{/i}"
    no "And why would you think that?"
    s "{i}Because if you’d been plotting it any longer, you’d have accomplished it already.{/i}"

    scene nods10
    with dissolve

    no "Heh. You give me too much credit."
    no "Sometimes, I really {i}am{/i} just a curious little girl."

    play sound "static.mp3"
    scene nods11 with flash
    stop sound

    no "{i}And who is better at showing “curious little girls” the...ins and outs of life than their daddy?{/i}"
    s "I’m beginning to think this isn’t for {i}me{/i} at all."
    no "{i}It’s for both of us, Akira. But only one of us is willing to openly admit it.{/i}"
    s "Nodoka-"
    no "{i}Just be patient. I’ll unlock the door in a moment.{/i}"

    scene black
    with dissolve2

    no "{i}But when I do...please don’t assault me immediately.{/i}"
    no "{i}It may take me a moment or two to...get fully in character.{/i}"

    "I keep my ear pressed against the door, listening to Nodoka rummage through Ami’s closet and drawers and...anything else she can get her hands on, I imagine."
    "And while my initial instinct is to break the door down, I’m a bit reluctant to do that as it would be much harder to explain away than just...some of Ami’s belongings being shifted around."
    "If she wants to play games, that’s fine. She can mess with {i}me{/i} all she wants. But dragging my {i}daughter{/i} into her nonsense just to satisfy her curiosity isn’t...something I can let happen anymore."
    "I promised to really protect Ami when I decided to take up the title of “father.” And knowing Nodoka’s history, it’s...hard for me to imagine she doesn’t have some sort of ulterior motive to what she’s doing right now."

    no "{i}Okay...that should do it.{/i}"

    play sound "lock.mp3"

    no "{i}You may enter, Akira. But again, please do not assault me as soon as you-{/i}"

    play sound "static.mp3"
    scene nods12 with flash
    stop sound
    play sound "doorslam.mp3"
    with hpunch

    no "Welcome home, Dad! I’ve been waiting for you all day! "

    scene nods13
    with dissolve

    no "And now that you’re here, it means we get to cuddle and watch movies and cuddle and eat ice cream and cuddle and-"
    s "What..."
    s "The fuck..."
    s "Do you think you’re doing?..."

    scene nods14
    with dissolve

    no "Cosplay! Aren’t I adorable, {i}Dad?{/i}"
    s "Take her clothes off. Now."

    scene nods15
    with dissolve

    no "You want to touch your little girl that badly? Was it hard being away from me all day?"

    scene nods16
    with dissolve

    no "How about we get in the bath together and I wash your back?! And anything else that needs washing! Maybe your penis? With my mouth? That sounds fun, right?"
    s "Why?..."
    no "Because I love you, of course!"
    s "No, Nodoka. Why are you doing this?"

    scene nods17
    with dissolve

    no "Because I love you, of course!"
    s "..."

    scene nods18
    with dissolve

    no "Did that make your heart skip a beat?"
    s "..."
    no "Is it because I look like her? Because I sound like her? Or am I still obviously {i}me?{/i}"
    s "You’re...better at impersonating her than you should be. But she isn’t exactly hard to mimic. Like, even the hair is-"
    no "Spot-on, right? "
    no "And to think {i}I{/i} barely even have any acting experience. Can you imagine how effective this ruse would be if I had {i}practice?{/i}"
    s "Sure. But I still don’t get {i}why.{/i} And just pretending you love me doesn’t answer it."

    scene nods19
    with dissolve

    no "Maybe I’m just a super big Ami fan?! Her style...her eyes...her poetry...those cute little A-cups you can’t help but wanna grab and squeeze and make her blush and cum and wet herself!"

    scene nods20
    with dissolve

    no "That wholesome, incestuous desire to be bred by her father because her love is so pure and uninfluenced by the many evils of this universe..."
    no "Isn’t Ami just the greatest?..."
    s "..."
    no "{i}Isn’t she?{/i}"
    s "Are you acting again?"

    scene nods21
    with dissolve

    no "Of course not, Dad. This is just who I want to {i}be.{/i} So I’m making my bestest effort to be the perfect daughter for you. That way, you’ll never need anyone else and can stay with me always."
    s "Are you making fun of her right now?"
    no "Does it {i}sound{/i} like I’m making fun of her? Is any of what I said untrue? Were some of the words {i}not{/i} words Ami would use?"
    s "Nodoka-"
    no "Those are all serious questions, by the way. I really want to know."
    s "Then ask {i}her.{/i} You don’t have to sneak into her room and put on her clothes if you want to learn more about her. Just talk to her."
    s "Assuming any of that is actually true and this isn’t just some sexual fantasy of yours where you can satisfy the need to fuck the father you no longer have."
    no "What makes you think I ever had a father at all and wasn’t just made in a tube?"
    s "Sometimes, not much. "
    no "Would you still fuck me if I really {i}was{/i} your daughter?"
    s "Nodoka-"
    no "Do you fuck Ami even though she’s {i}not?{/i} Is it even true that she’s {i}not?{/i} What’s it like? How does she taste? How different am I? How can I be more like her?"
    s "Is this really for my sake, Nodoka?"
    no "Call me Ami."
    s "Absolutely not. "
    no "Then how about Nodokami? It combines both of our names {i}and{/i} makes me feel like a god. Everyone wins."
    s "Everyone except the actual Ami, who just had her closet raided by a psychopath who wants to pretend she’s fucking her dad."

    scene nods22
    with dissolve

    no "My intentions aren’t {i}always{/i} evil genius levels of malicious, Akira. I figured you’d know that about me by now."
    s "You figured I’d be happy to have an Ami who isn’t {i}actually{/i} Ami?"
    no "Yes. Because, the way I see it, if you {i}aren’t{/i} already fucking her, this would give you the chance to do it guilt-free. "
    no "And if you {i}are,{/i} this could be a fun new flavor of fake incest you can compare and contrast with the real thing."
    s "But you’re getting something out of it. You wouldn’t do this if you didn’t have something to gain."
    no "Sometimes, I just want to understand things."
    no "And I have a hard time doing that if the things I {i}want{/i} to understand don’t make any sense."
    s "Nodo-"
    no "I had a dream last night..."

    scene nods23
    with dissolve

    no "That we were closer than we thought."
    no "But there was a dark cloud looming over us. And it wouldn’t let us be what we {i}needed{/i} to be in order to be happy."
    no "That cloud was jealous. But it was jealous because it wanted the same thing. "
    no "It had been waiting to rain for centuries, but was too afraid to open itself up because it was worried it might flood the world and drown {i}you.{/i} Beautiful you."
    no "Everyone else could be washed away for all it cared. And despite my wanting to lock you inside and protect you...I couldn’t help but feel the need to give you up when I compared myself to that darkness."
    s "But you won’t ever {i}be{/i} that darkness, Nodoka."
    no "No...I suppose I won’t."

    scene nods24
    with dissolve

    no "But I can still aspire to understand it. And if I spend long enough inside its mindset, maybe I’ll be able to feel what {i}it{/i} feels."
    no "There is something special about Ami. And I don’t want to wait for the rain anymore. I want to feel it. I want to feel {i}her.{/i} I want to feel the way {i}she{/i} feels {i}you.{/i}"

    play sound "dooropen.mp3"
    scene nods25
    with dissolve

    no "It’s but one of many missing pieces in many of my unsolved puzzles..."
    no "All on the way to perfect hair forever."

    $ renpy.end_replay()
    $ nodokainvite1 = True
    $ nodoka_love += 1

    jump nodokainvite2

label nodokainvite2:
    if _in_replay:
        play music "icantseeher.mp3"

    play sound "static.mp3"
    scene amiandkami1 with flash
    stop sound

    a "..."
    s "..."
    no "..."
    a "Oh, this should be good."

    scene amiandkami2
    with dissolve

    s "Okay, hold on. Before you freak out, let me try to explain. Nodoka is-"
    no "Adorable, isn’t she? I had no idea being cute felt so good."
    a "That’s...That’s Nodoka? "
    s "Yes. But I’ve already told her that raiding your things is fucked up and weird and I never would have-"
    no "Tried to hide it from you unless he was forced to."

    scene amiandkami3
    with dissolve

    s "What?"
    a "Yeah, {i}what?{/i}"
    no "Okay, okay. Since I’ve been caught, I might as well come clean. "
    no "I’ve been sneaking into your house and dressing up in your clothes for months now. But it appears I became a bit too immersed in my games today and didn’t hear your father come home."

    scene amiandkami4
    with dissolve

    no "I tried to get away with it by convincing him I was the {i}real{/i} you, but I guess he just loves you way too much to fall for a silly trick like that. He saw through me right away."
    a "I’m not buying it."
    s "I can handle this, Nodoka. Just go home. "

    scene amiandkami5
    with dissolve

    no "If that’s what you think is best, Daddy..."
    a "Do...not...FUCKING...call him that."

    play sound "static.mp3"
    scene amiandkami6 with flash
    stop sound

    no "But that’s what the {i}real{/i} Ami would call him. And if I’m going to pretend to be you, I’m going to give it my all! Ami Arakawa never-"
    a "You. Are. Not. Me. You do not get to call him that."
    no "But I {i}am{/i} you, Ami. "

    scene amiandkami7
    with dissolve

    a "Hahah! You’re going to die now!"
    s "Ami, wait. Just because Nodoka is being fucking weird again doesn’t mean we need to escalate things. She was just leaving. {i}Right,{/i} Nodoka?"
    no "Yes, Da-"
    a "Sensei."
    no "Yes, {i}Sensei.{/i} Let me just gather my boring old regular outfit and-"
    a "No, no! You leaving will just make it harder for me to kill you. Please! Take a seat. Get comfortable. And let me know what you’d like to have for your last meal so I can try to throw it together really quickly."

    play sound "static.mp3"
    scene amiandkami8 with flash
    stop sound

    no "I’ll take a deluxe strawberry parfait, some rosé tteokbokki, a small serving of hamburger steak, some zarusoba aaaaand...a bowl of cranberries."
    a "Those are all of my favorite foods!"
    s "A bowl of cranberries?"
    a "I heard they make your boobs grow! But it was clearly a lie!"
    no "I’ll also take a white peach flavored Calpico if I’m allowed to have a drink."
    a "Why do you know all of my favorite things?! This is beyond creepy! And I know a thing or two about creepy!"

    scene amiandkami9
    with dissolve

    no "I’m obviously just a huge fan! Do you really think I’d pretend to be you otherwise?"

    play sound "static.mp3"
    scene amiandkami10 with flash
    stop sound

    a "Yes! If you think it would bring you closer to having sex with my dad, I imagine you {i}would{/i} pretend to be me!"
    no "That does sound rather intriguing, I won’t lie."

    scene amiandkami11
    with dissolve

    a "Dad, will you please let go of me if I promise to dispose of her body without a trace?"
    s "Ami, let’s just go to my room and wait until she’s gone. Okay?"

    scene amiandkami12
    with dissolve

    a "And just let her get away with this?! "
    a "So Nodoka breaks into the house and sets up this whole thing where I walk in on her pretending to be me, {i}clearly{/i} mocking me to {i}your{/i} face, and you just want to let her go?! Doesn’t that make you mad?!"
    s "Yes. Very mad. She didn’t break in, though. That was a lie. I invited her here."

    scene amiandkami13
    with dissolve

    no "Tch. Even after I tried to cover for you and everything. The fact that you’re suddenly so honest with her is something I hadn’t factored into my take on the character. I’ll have to refine my craft."
    a "You {i}knew{/i} she was going to do this?..."
    s "No. She tricked me and locked me out. Then, when she finally unlocked the door, she was...{i}this.{/i}"
    a "Why did you invite her over?"
    s "To-"
    no "To fuck me, of course."

    play sound "static.mp3"
    scene amiandkami14 with flash
    stop sound

    a ".............."
    s "Nodoka, just out of curiosity, do you {i}want{/i} to die? Because I’m starting to think this is some kind of “suicide by cop” situation. "
    a "I don’t even have any words right now. "
    no "You could always compliment my outfit? Or tell me more about how badly {i}you{/i} want to lie with your father. The possibilities are essentially endless."
    a "Everyone knows exactly how badly I want to “lie with my father.” Wasting more words on someone playing dress-up would do nothing but turn me on. "
    no "Excellent. Then we can be turned on together. Because seeing just how dearly the two of you love one another has set this borrowed body ablaze with lust and curiosity."
    a "I’m listening."
    no "What more do you want to hear?"
    a "Whatever else you have to add to that thing about how dearly my dad and I love each other."

    scene amiandkami15
    with dissolve

    s "Is that really more important than just getting her out of here? Everybody already knows Nodoka is the incest girl."
    a "Yeah, but we’ve never seen what she does in a situation where it could actually happen."

    if amifingered == False:
        scene amiandkami16
        with dissolve

        s "Ami...you know I won’t do those things with you."
        a "But you have no problem doing them with girls who look like me and dress like me and literally {i}pretend to be me,{/i} huh? "
        s "..."
        a "If I didn’t come home, you’d have done it with her...wouldn’t you?"
        a "Sure, you might resist at first because it {i}feels{/i} wrong. But you’re weak and cowardly...and you crumble when it comes to everyone {i}but{/i} me. "
        a "She’d have talked you into it. And honestly, Dad? I’m feeling a little tempted to let her now just because I know you’d think of me when you close your eyes."
        s "I would never..."

        scene amiandkami17
        with dissolve2

        a "Admit it..."
        a "You want to fuck me harder than you’ve ever fucked {i}anything{/i} in your life."
        a "Does pretending you’re above that make you feel good, Dad? Wouldn’t you rather be above me, listening to me cry out your name as you pump me full of cum? "
        s "Are you done yet?"
        a "Why does everyone always ask me if I’m “done?” Do I {i}seem{/i} done? Wouldn’t I have finished years ago when you {i}first{/i} rejected me? Do you think I’m so dumb that I’d let this go on forever for no reason at all?"
        a "Just do it. Right here. Right in front of Nodoka. Show her you {i}really{/i} love me...Because we both know the way you love, Dad. And if you won’t fuck me...you don’t really love me at all."
        no "I like this. And I agree with Ami. You {i}should{/i} fuck her."

        scene amiandkami18
        with dissolve

        a "Right?! "
        s "Thanks, Nodoka. You’re really making my life very easy today."
        a "Like, seriously! What the hell is his problem with a little bit of incest? He does {i}way{/i} worse shit all the time. But having sex with a girl who might be his daughter is like “the end of the world” or something."
        no "Sorry, could you repeat that last part for me? I want to make sure I heard you correctly."

        scene amiandkami19
        with dissolve

        a "Now, let’s get one thing straight. Just because I agree with you on your stance of whether or not it is morally justifiable for a father to fuck his daughter doesn’t mean that I {i}trust{/i} you."
        a "And if you’re going to say things like that, I am going to be skeptical. Why should it make any difference to you whether or not my dad is {i}actually{/i} my dad, Nodoka?"
        no "Why, it’s for my book of course. "
        a "What book? I only read manga. So if you’re trying to give me some sort of message, you’ll have to do it through that."
        no "Would you read it if I told you it was a book about a man like him falling for a girl like you?"
        a "Are there a lot of really graphic sex scenes?"
        no "Possibly."

        scene amiandkami20
        with dissolve

        a "Yeah, I’d probably read it then since my dad is too much of a pussy to ever actually screw me here."
        no "“Here” implies that there’s somewhere he {i}would.{/i}"
        a "Yeah."

        scene black
        with dissolve2
        stop music fadeout 10.0

        a "It does. Doesn’t it?"

        "{i}Uh-oh! It looks like you’re once again missing out on content due to an incorrect choice you made!{/i}"
        "{i}At what point will you undo your mistakes and start all over?{/i}"
        "{i}You’re going to have to, you know. How do you expect to find out what happens next in a world you keep pressing the pause button on?{/i}"

        play sound "computeryay.mp3"

        "{i}Either way, coward or not, you’re now allowed to invite Nodoka over whenever you want!{/i}"
        "{i}Just know that she probably won’t ever dress like your daughter again because doing so made you look pathetic.{/i}"
        "{i}She goes home and fingers herself to Ami instead.{/i}"
        "{i}She wishes she got to keep her clothes.{/i}"

        $ renpy.end_replay()
        $ nodoka_lust += 1
        $ nodokainvite2 = True
        $ nodokainvite3miss = True

        "{i}Nodoka’s lust has increased to [nodoka_lust]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsatch4
        else:
            jump endofweekdaych4

    else:
        scene amiandkami21
        with dissolve

        no "What an astute observation, Ami! My status as the “incest girl” is naught but hearsay until it’s proven that I’m not merely putting on an act. We really {i}should{/i} test this out, shouldn’t we?"
        a "So...just to clarify — you’re saying you really {i}do{/i} want to watch my dad fuck me?"

        scene amiandkami22
        with dissolve

        no "I want whatever it is {i}you{/i} want, Ami! "
        no "Right now, I don’t want you to think of me as Nodoka at all! I want you to see me as a...reflection. Just the type you’d find in a funhouse that makes you look far less cute than you truly are."
        a "So you admit you’re just a cheap knockoff, then?"

        scene amiandkami23
        with dissolve

        no "As cheap as they come. "
        no "Besides, if you want the honest truth, I’d rather watch him have his way with you than experience it myself to begin with."
        a "Okay. I’m being successfully convinced."
        s "Yeah, because you’ve never met anyone willing to watch us fuck before."
        a "I can guarantee you there are at least five girls in the class who would not only {i}watch{/i} that, but aggressively touch themselves to it. Nodoka’s just the first to actively seek it out."
        no "I’ll do anything so long as it brings us closer together, Ami. I’ve always admired you."
        a "You have literally never said or indicated that to me at any point."
        no "I’m not very good at socializing. Please accept this cosplay {i}and{/i} my body in lieu of a formal friend request."
        s "I don’t really think Ami wants your body, Nodoka."

        scene amiandkami24
        with dissolve

        a "Hmmmmm......."
        s "Uh...or...maybe I’m wrong?"
        a "I {i}do{/i} like dolls. And my clothes {i}do{/i} look surprisingly good on her."
        a "A live mannequin sounds kind of interesting...doesn’t it, Dad?"
        no "I can be more than just a mannequin too. I’ll follow orders. And if you want to put anything inside of me, I won’t even complain about it."

        scene amiandkami25
        with dissolve

        no "Unless you want me to, of course. Because, while I may have {i}come{/i} here to let your father fuck me, my real goal has always been to learn more about you. "
        a "{i}Why, though?{/i}"
        no "So I can be the best Ami I {i}can{/i} be, of course. "
        a "Step one — tragically lose your parents. "

        scene amiandkami26
        with dissolve

        no "Essentially complete."
        a "Step two — twintails."
        no "Also complete."
        s "Step two is a major regression from the first one."
        a "You underestimate how long it took me to grow my hair out. Step three — buy into the idea that the purest {size=-15}and hottest{/size} form of love that exists is that which occurs between father and daughter."
        s "And now we’re right back to 100."
        no "Oh, joy. I’m three-for-three so far. How many more steps are there before I see the two of you engage in...{i}purity?{/i}"
        a "Are you going to tell anyone about this?"
        no "Do you {i}want{/i} me to tell anyone about this?"
        a "Kind of. I don’t think it would be good for Sensei, though."
        s "I feel like I’m kind of just here as an afterthought in this negotiation, so don’t factor me in {i}too{/i} much."
        s "But yeah, the fewer people who know I’m the worst parent in the world, the better."

        scene amiandkami27
        with dissolve

        a "One last question. Do you think my dad is a bad parent?"
        no "Of course not. How would such a thing even be {i}possible{/i} with a daughter as perfect as you?"

        scene amiandkami28
        with dissolve

        a "Okay! Application accepted! You get to watch!"
        s "{i}Hah...{/i}"
        a "But first, to make sure you’re not armed or recording this, and also because I hate it, I’m going to need you to take my clothes off."
        no "Of your body? I can do that."
        a "Noooo, I need you to take my clothes off of {i}your{/i} body."

        scene amiandkami29
        with dissolve

        no "I have to be naked?"
        a "Getting cold feet? Or maybe...you {i}really{/i} are up to something if-"

        scene amiandkami30
        with dissolve

        no "Is here okay?"
        a "Oh. Yeah. There is fine."
        s "Ami...what are you doing?"
        a "What do you mean “what am I doing?” You invited a girl over to have sex and the first thing she did when she got here was put on my clothes. She’s lucky she’s still breathing."
        s "Shouldn’t {i}I{/i} be the one in trouble then? Since I’m the one who invited her?"

        scene amiandkami31
        with dissolve

        a "Nope! Because you were so disturbed by the sheer sight of her pretending to be me that you felt sick to your stomach and couldn’t proceed. Poor thing. I’ll have to take {i}really{/i} good care of you today."
        a "Especially since we’ll have an audience."
        s "You sure you’re...okay with this, though? Nodoka’s pretty much always up to something and...you accepted her explanation of things a bit easier than I expected."

        scene amiandkami32
        with dissolve

        a "Sure. You’re right. But the way I look at this is really simple. "
        a "You and I are going to make love like we always do. And there isn’t a thing in the world that can ruin that even {i}if{/i} Nodoka is up to something. "
        s "What about another {i}Ami,{/i} though?"
        a "Another Ami will just make you cum harder. And I’ve never gotten to have a threesome with myself before."
        s "You’ve never gotten to have a threesome with {i}anyone{/i} before."

        scene amiandkami33
        with dissolve

        a "That’s just what {i}you{/i} think."
        s "..."
        s "I {i}hope{/i} you haven’t had a threesome with anyone before."
        a "And {i}I{/i} hope you brought your A-game today since we’re gonna need to go all out to impress Nodoka."
        no "While I feel bad about interrupting the two of you as you flirt, I’ve finished getting undressed and would like to proceed now."

        scene black
        with dissolve2

        a "And proceed we shall! "
        a "After a brief inspection..."

        "Ami, somehow slightly {i}less{/i} terrifying than normal, makes her way across the room and stands beside Nodoka’s naked body."

        $ renpy.end_replay()
        $ nodokainvite2 = True

        jump nodokainvite3

label nodokainvite3:
    if _in_replay:
        play music "icantseeher.mp3"

    scene nodokamithree1
    with dissolve2

    "And while I absolutely can not deny the rapidly forming erection that resides within my pants, I still feel somewhat uncomfortable about all of this."
    "It’s one thing to develop a sexual relationship with your niece-turned-daughter, but when there’s someone on the outside witnessing it and...essentially {i}parodying{/i} it, it just feels sort of surreal."
    "It’s like Ami and I, for the time being, really {i}are{/i} just some characters in a story that Nodoka’s writing or...{i}trying{/i} to write."
    "Which makes me feel like whatever I do next will be exactly what she wants me to do. "
    "All the while, though, Ami appears to feel and act like {i}she{/i} is the one holding the reins. But Nodoka is so nonchalant about the whole thing that I can’t figure out which one of them actually {i}is.{/i}"
    "Maybe it’s both? Maybe I’m the horse pulling their carriage? And maybe the two of them are about to lean back and push me to my limits while- yup. Erection fully formed. There’s no turning back now."

    a "Hm..."
    no "..."

    scene nodokamithree2
    with dissolve

    a "Hmmm......."
    no "I’m only slightly larger than you, Ami. But I solemnly swear that I would shrink them down if I could."

    scene nodokamithree3
    with dissolve

    a "You don’t wish you were a little bigger?"
    no "Don’t you think your father would be less attracted to you if you were fully developed?"
    s "Wow. Okay."
    a "I do think that sometimes. But I {i}still{/i} can’t help but feel a little less...{i}womanly{/i} when I see girls my age with bigger ones."
    no "So effectively {i}all{/i} of them."

    scene nodokamithree4
    with dissolve

    a "For now. I just need to eat more cranberries."
    no "What are your thoughts, Akira? Do you-"

    scene nodokamithree5
    with dissolve

    a "No."
    no "Hm? No what?"
    a "You will speak and answer only to me. So no asking my dad what he thinks about X or how Y compares to Z."
    no "May I ask why? I just want to understand the methodology behind a decision so paramount in constructing the rest of this event."
    s "It’s to prevent her from getting jealous."

    scene nodokamithree6
    with dissolve

    no "I see, I see."
    a "Hey! You’re not allowed to speak to her either. This is {i}my{/i} room and Nodoka is posing as {i}me,{/i} so I get to make the rules. Either that or she goes home and we have sex {i}without{/i} a spectator."
    s "Sure, but I feel like you want a spectator more than me at this point."

    scene nodokamithree7
    with dissolve

    a "I just want someone to see how well I take care of my daddy and all of his socially unacceptable urges."
    no "I agree to your terms, Ami Prime. Now, will you please provide a directive for me, Ami Junior?"

    scene nodokamithree8
    with dissolve

    a "Hoooold your horses. We’ve still got a few more rules to set before we begin. But if you follow them perfectly, I might even let you {i}participate{/i} later."
    s "There is no way that is true."
    a "Of course it’s true, Dad. I just can’t give her my stamp of approval until she’s able to step her Ami game up. "
    a "And the last thing I want is for you to think about having sex with {i}Nodoka{/i} while you’re having sex with Nodoka. You should be thinking about Ami instead. Right, Ami?"

    scene nodokamithree9
    with dissolve

    no "Right! Daddy’s huge and perfect cock would be wasted on anyone else!"
    a "Ha! I actually kind of love this."
    no "Me too! Any chance I get to show Daddy how much I love him is the most perfectest chance ever. I’m getting super turned on just thinking about it!"

    scene nodokamithree10
    with dissolve

    a "Same here, Ami!"

    scene black
    with dissolve

    a "I should hurry up and get undressed too! Daddy’s probably super turned on right now, and making him wait is something Ami does {i}not{/i} do. Do you understand, Ami?"
    no "Yes, Ami. The most important thing is to help Daddy feel all better as soon as possible!"
    a "Ding ding ding!"

    "Ami undresses slower than normal — likely because she takes a moment after removing each article of clothing to hold it up against Nodoka’s body and see how it would look on her."
    "It really {i}is{/i} like she just has a living doll all of a sudden — one that {i}isn’t{/i} me. But the type of doll I {i}am{/i} for her serves a different purpose."

    scene nodokamithree11
    with dissolve2

    "I’m the only outlet for her lust. So if I don’t give myself up to her, she’ll likely explode."
    "This is a form of maintenance, if you will. Which isn’t to say I don’t enjoy it. There are plenty of mechanics out there who are overcome with joy every time they pop open the hood of a car."
    "At the end of the day, though, they still know they’re serving a purpose. They’re fixing something. "
    "This is how I fix her. And it’s how she fixes me too. "
    "Nodoka’s merely receiving some on-the-job training right now."

    a "How to fuck your father, step one — make sure he’s ready. "
    a "Sometimes, on days like today, this step isn’t entirely necessary. Because, as you may have noticed, he’s already super hard — which means he might want to put it in as soon as possible. "
    a "But if you aren’t pressed for time, it’s great to show him how much you care by using your mouth and hands to service him first. "

    scene nodokamithree12
    with dissolve

    a "The way he looks down on you while you suck him off is one of the most satisfying looks a girl could ever get."
    a "And, as if that wasn’t big enough of a reward on its own, making him cum before he fucks you makes him last longer too."
    s "I am truly “blessed” to have a daughter like you, Ami."

    scene nodokamithree13
    with dissolve

    a "Sometimes...ahm...Dad can get a little...mlm...sarcastic..."
    a "But he normally quiets down...ahhn...once you start licking him a little bit..."
    no "It seems like you’re really good at that, Ami. I can see it getting harder right in front of me."
    a "Ahm...of course I’m...aaahn...good at it, Ami..."
    a "I have lots...and lots...of practice..."

    scene nodokamithree14
    with dissolve

    a "Daddy is...mmm....a very needy man...so I need to always be ready...ahnnn...to please him..."
    no "He looks really cute when you lick him like that, Ami. I’ve never seen a face so perfect before."
    a "Does that feel good, Daddy?..."
    a "Doesn’t your little girl look cute when she’s so focused on taking care of you?..."
    s "A...Ami..."

    scene nodokamithree15
    with dissolve

    a "Mm!...Once his...mmnlnh...voice starts...mmff...getting quieter...it’s safe to...mm...put it in your mouth!..."
    no "Wow...I’m surprised you were able to fit it, Ami. I was worried you were too little to handle it."
    a "Thish...ish...nothing...jssht wait until...he puts it in...my pussy...{i}thass when...{/i}the gameshh...rlly begin..."

    "Ami begins to pay less attention to Nodoka as she focuses on sucking my cock."

    scene nodokamithree16
    with dissolve

    "So of course Nodoka seizes the opportunity to redirect her attention to me in the meantime. And...honestly, it looks like she’s actually into it."
    "I didn’t doubt she {i}would{/i} be. It’s just somewhat surprising seeing someone treating me so normally as I lightly thrust my dick into the mouth of a girl I raised."

    a "Mmm...mmm...Daddy...{i}Daddy...{/i}"
    no "How do you stop yourself from getting so wet when you look at him during times like this, Ami?"
    a "Sometimesh I...need to keep my eyes closed so...I don’t get too turned on..."
    a "Ishh really hard...right?...Not jumping...mlm...right into his lap and...riding him until he fills you up..."
    no "Yeah..."

    scene nodokamithree17
    with dissolve

    no "There’s nothing quite like Daddy’s cock...is there?"
    a "Mm?..."
    no "You look so cute right now..."
    no "Like you were born for this..."
    s "Probably...don’t touch her, Nodoka..."

    scene nodokamithree18
    with dissolve

    a "Mm...mmm...I told you...not to addressh her...Dad..."
    a "Ishh okay, though...amnh...she can touch...sinshh I know...mlm....thss what...you want..."
    no "Can I really, Ami?..."
    no "You’ll let me help Daddy cum?..."
    a "Mm...mngh...mmhmmm...making Daddy cum ishh...Ami’s job, after all..."
    no "Then..."

    scene nodokamithree19
    with dissolve2

    no "Can I speak to him too?..."

    "Nodoka grabs my cock and begins to jerk me off into Ami’s mouth."
    "I am going to die."

    a "Mmm...mmmnch...fine...but only say...thingshh...that Ami would...say..."
    no "You’re so handsome, Daddy...I’m so happy we...can be together like this now..."
    no "I can’t even imagine a world where...you’d let someone else...care for you like this..."

    "She moves faster and...and I..."
    "Ah...I can’t...focus..."

    scene nodokamithree20
    with dissolve2

    no "The...thought alone...makes me...so mad..."
    no "But I...aah...I’m so...wet for you, Daddy...I want you {i}so{/i} bad..."
    no "Please...{i}please...{/i} hurry and cum for your...little girl...so I can...feel {i}more{/i} of you...more...{i}more...{/i}more!"

    scene nodokamithree21
    with dissolve

    no "Mnnh! Mm...cum...cum for Ami...only...Ami!"
    a "Mm! Mmmnh! Mm! Dad...Daddy!"
    s "Hah...fuck...I...I..."

    with sexfade
    with sexfade
    scene nodokamithree22 with cumflash
    with hpunch

    a "Mmm! Mmm~ MmmmM!!!!!!"
    no "Hah! Hah..."
    no "Just like that...Daddy..."
    no "Let it all out..."

    scene nodokamithree23
    with dissolve

    a "Mm...mlm...mnch..."
    a "Always...be sure to...drink every...last drop..."

    scene black
    with dissolve2

    a "We...have to make sure that...Daddy’s cum..."
    a "Is never wasted..."

    play sound "static.mp3"
    scene nodokamithree24 with flash
    stop sound

    "Ami cleans me off using nothing more than her tongue as Nodoka takes a moment to collect herself. "
    "Once the redness fades from her cheeks and she’s able to force herself back into character, she sits beside me on the bed while Ami climbs on top."

    a "How to fuck your dad, step two..."
    a "Fuck your dad."
    no "This sounds far more appealing than step one."

    scene nodokamithree25
    with dissolve

    a "They both have their perks, but...aaah...yeaaaah..."
    a "There’s nothing quite like...riding the cock that...might have created you..."
    s "Should you really be saying things like that to-"
    a "Shh...Shut up...That isn’t Nodoka...That’s...one more Ami..."
    no "If that’s the case, don’t you feel a little strange knowing you’re having sex with someone who used to bed your mother?"
    s "Nodoka-"

    scene nodokamithree26
    with dissolve

    a "Remember to...stay in character. But no...I don’t think it’s weird at all..."
    a "My mom was amazing...so I’m not going to blame my Dad for...hah...falling in love with her...and I won’t blame her for...falling for {i}him{/i} either..."
    no "But what about our real daddy?"

    play sound "static.mp3"
    scene nodokamithree27 with flash
    stop sound

    a "Hah...Daddy doesn’t...want to hear about..."
    a "Just...aah...let’s...move on...haah...fuck..."
    no "You’re surprisingly good at riding him too, Ami. The way his cock protrudes from your belly on the way down is arguably the most alluring thing I’ve ever seen."
    a "Oh...god...I want to cum already...I haven’t done this...nearly enough lately..."
    no "What are you waiting for exactly? Why not just cum now if you want to so badly?"
    a "Daddy likes it...when {i}he{/i} decides...so I...hah...always try to...wait until...he starts-"

    play sound "dosex.mp3"
    scene nodokamithree28
    with hpunch

    a "Haaah!"
    no "Ooooooh, I see. He’s moving a lot faster now."
    a "Aah! Ah! Aaah!"
    s "You don’t...need to wait for me, Ami...you can...cum whenever...you want..."
    a "Hah! Hah! N...No! If I can help it, I’ll...always wait for you! But...hah...haah...sometimes...haah! Daddy! Yes! Harder! Harder, harder, harder!"
    no "Does Daddy always take the bottom? Wouldn’t it be better for him to take control of our fragile, nubile bodies and pound us from above or behind?"
    a "Hah! Hah! He does! Sometimes! But sometimes! I! Hah! Want to! Hah! Take Care! Of! Him!"
    no "Mmm...it appears more like he is taking care of you right now, though. Yes?"
    a "Oh god! Oh god! I’m...hah! Daddy! Daddy!"

    with sexfade
    with sexfade
    scene nodokamithree29 with cumflash
    with hpunch

    a "AaaaaAAAaAaah! AAaaah! Aaaah! AAAAaaaah! Hah!...Hah.......Aaah...."

    scene nodokamithree30
    with dissolve2

    a "Haah...mmf..."
    no "Mmf indeed..."
    a "S...Step three...after...you cum...don’t...give up!"
    a "It’s...never over until...Daddy says it’s...over!"

    scene nodokamithree31
    with dissolve

    a "So we have to...make him cum again...as many times as...he wants!"

    "Ami goes right back to riding me and Nodoka goes right back to staring as if it’s any other night watching porn in her room."
    "And while I’d like nothing more than to fuck that smug smile off of her face right now, I’m not about to ask my daughter to hop off so I can thrust my cock into the girl that’s currently emulating her."

    a "How is it...Dad?..."
    a "Two Amis is...way better than one...right?..."
    s "This will...certainly be something I remember...yeah..."
    a "Anything...you want to add...Ami Junior?..."
    no "Just that I’m eternally jealous of your ability to please our daddy, Ami Prime. I could never even {i}hope{/i} to extract that much pleasure out of him."
    a "It’s...easier than...it looks! You’ve just gotta...give your body...time to...adapt!"
    a "But you’ve already...fucked him before...haven’t you?! That’s why...he...invited you!"
    no "Not in this form, I haven’t. And in the few times I {i}have,{/i} it always felt to me as if he was wishing I were you."
    a "Hah...hah...a-hah! It suddenly...makes a lot more sense why...you’d want to dress up like me then! "
    a "How does she...compare...Dad?! You like my...pussy more...right?!"
    s "Hah...Ami..."
    no "Of course he likes yours more, Ami. I can tell from here how {i}snugly{/i} he fits inside. Like you’re perfect matches for one another. And again...I simply can’t compete."
    a "Hah...hah...but you want to...right?..."
    a "You want to fuck your Daddy...don’t you, Ami? You want to...have him...use your little body...however he wants...You want him to...cum inside you...You want to...have his babies! And love him..forever...right?!"
    no "Mm..."

    scene nodokamithree32
    with dissolve

    no "We want a baby?"
    a "Why stop at...one when...we could have...hundreds!"
    no "Have you thought up any names for them in the event such a thing {i}did{/i} happen?"
    a "Hah...hah...well...let’s see what...{i}you{/i} think..."
    a "What would...you name...your baby...Ami Junior?..."
    no "Somethiiiiiing...floral, perhaps?"
    a "Bzzzzzzzt. Not...even...close!"
    s "I surely have to...get some say in this...right?..."

    scene nodokamithree33
    with dissolve

    a "You can get all the say you want...once you fill me up and...get me pregnant..."
    s "You’d have definitely gotten pregnant already by now if such a thing was fated to happen."
    a "That just means...we aren’t trying...hard enough! We clearly...need to...have more sex!"
    a "But...don’t worry...Dad! There are...two of us...now! And Ami Junior...is next!"

    scene nodokamithree34
    with dissolve

    no "I am? I’ve passed your tests?"
    a "You still...have a lot of work to do! But...I’m feeling generous...today and...it’s okay...so long as...you’re me!"
    no "Thank you, Ami! I’ll do my bestest to make you proud. I just hope our Daddy’s massive cock doesn’t stretch me out too much."
    a "Hah! Hah! You’ll...be fine! Just...start slow!"

    scene nodokamithree35
    with dissolve

    no "What if Daddy doesn’t want the fake Ami, though? Knockoffs are never better than the real thing."
    a "Hah...hah...right! But they’re cheaper...and fun to break! And I think Daddy wants to...try since...he’s getting harder at the very thought of it!"

    scene nodokamithree36
    with dissolve

    no "{i}Is{/i} he now?..."
    a "I knew it...Two Amis...really {i}does{/i} drive you crazy...doesn’t it, Dad?..."
    a "I wonder what will happen...if I turn the whole class...into an Ami army! Imagine fucking...twenty of your daughters...at once!"
    s "Hah...haah...Ami...I can’t...I-"
    a "Cum for Ami, Daddy! Cum for Ami! Cum for your little girl!"

    with sexfade
    with sexfade
    scene nodokamithree37 with cumflash
    with hpunch

    a "NNNNNNHHHHH!!!~~~~~"
    no "So..."
    no "Jealous..."

    scene nodokamithree38
    with dissolve

    a "Hehehe..."
    a "Well, you won’t be for long. "
    no "Thank you, Ami. I’m not deserving of-"
    a "Shut the fuck up and put my clothes back on."

    play sound "static.mp3"
    scene nodokamithree39 with flash
    stop sound

    "So anyway, this is happening now. But I’m too high off of the many emotions I’m feeling at the moment to provide any decent commentary, so I’m just going to let Ami take it away."

    a "Yes...good girl, Ami! Drink up every last drop of Daddy’s cum! Just like you were told to!"
    no "Anhh...mnch...mlm...the taste is...exquisite..."
    a "Ami wouldn’t...say “exquisite!” Talk...more like Ami!"
    no "Mmnh! Mmmh! Daddy’s cummy-wummies are the most bestest in the whole wide world!"
    a "That...was {i}too{/i} Ami! You need to...tone it down!"
    no "Mlm...mlm...yes, Ami...I’ll be better...I’ll be a good girl...I’ll be a you...that you can be proud of!"
    s "Are you actually enjoying this, Ami?..."
    no "Yes, Daddy! I love it!"
    s "Other Ami. Not you. She’s supposed to be straight."
    a "I {i}am{/i} straight. This is just masturbation as far as I’m concerned. And Ami Junior is surprisingly good with her tongue."
    no "Mlm...mmn...thank you, Ami Prime! I’ve dreamed of...drinking Daddy’s cum from your perfect...pink pussy since...the moment I saw you two together!"
    no "You’re the perfect couple! I can never compete! I’m only good as a spare hole! "
    a "Ami...doesn’t self-deprecate like that! She needs to be confident so...Daddy can see she’s growing up!"

    scene nodokamithree40
    with dissolve

    no "Mm! Mm! But Ami...doesn’t want to grow up! Ami...wants to stay a little girl...forever!"
    a "Hah...aah...keep...going...Ami!"
    no "Mmm! Mm! Ami can’t focus! She feels too good! Her Daddy’s cock...makes her forget everything else!"
    a "Yes! Right there! Oh god! Oh fuck!"
    a "...Is what I {i}would{/i} be saying if I was actually enjoying this. I just think it’s really hot watching my Daddy fuck someone pretending to be me."
    no "Mm! Mm! I knew it! I’ll never be good enough for you, Ami! I’m just...a knockoff!"
    a "Exactly, Ami Junior! Know your place! And never sneak into my room again!"
    no "I’m...sowwyyyyy!!!!"
    a "AGAIN! THAT’S TOO MUCH AMI! Just shut up and give my Daddy a new hole to fuck!"
    s "You’re both weirding me out right now, so I’m just going to go ahead and pound {i}Ami Junior{/i} until she’s been reduced to a puddle of various fluids on the floor."
    a "Good call, Daddy. I can only last so long with a filthy imposter between my legs anyway."

    play sound "dosex.mp3"
    scene nodokamithree41
    with dissolve2

    no "Haah! Haaah! Ohh...fuck! Oh...fuck, yes...Daddy! Daddy! Harder!"
    a "Ha! Look at her, feeling the full force of your massive dick. She’ll cum any second now. "
    a "How does she feel, Daddy? Does it look like you’re fucking me from behind? Should we dye her hair? Maybe saw her feet and ankles off so we’re closer to the same height?"
    s "No, you freak. Can’t we just have a threesome without you turning murderous?"
    a "I want to! I’m just way angrier than I thought I’d be watching a {i}fake{/i} me fuck you while the {i}real{/i} me is right here!"
    no "Haaah...haaaAAaaaaaAaahhh...aaaahhh..."
    a "Keep licking! I didn’t tell you to stop!"

    scene nodokamithree42
    with dissolve

    no "Aaahhhnnn~~~~~~"
    no "A....mi......"
    no "You’re so......cute......."
    a "Okay, now I’m enjoying it again."
    s "Great. So why don’t we all just keep quiet for a minute and lose ourselves in the moment? Since I can’t imagine we’ll ever be doing this again."
    no "Mmm...mmmnln...I want more...every day..."
    no "Adopt me...make me...a {i}real{/i} Ami..."
    no "I just want to be...as pure as you two! Not the...depraved...filthy mess I really am! I’m so lonely! So...ahmm...lonely! I just...want a Daddy...I can take care of!"

    play sound "dosex.mp3"
    scene nodokamithree43
    with dissolve

    no "Nyaaah! Ahhh! HAaahhhAAA!! Aki- hah! I mean! Daddy! Fuck me! Fuck...AmI! Fuck Ami, fuck Ami, fuck Ami, fuck Ami! Haaaah!"
    a "Are you gonna cum inside of her?"
    s "Will you get mad at me if I do?"
    a "A little. But I’d understand. "
    a "I suppose she’s earned it, if anything. She’s called me cute more times today than you have in the last month."
    no "So cute! The cutest! Even your little pussy is cute! I’m so glad you’ll let me drink your Daddy’s love juice out of it!"
    a "“Love juice?” What is it with these weird dialogue choices? Just what kind of girl do you think I am?"
    no "The...best...kind!"
    no "Ami!...Daddy!...I love you both...so, so much!!!!!"

    with sexfade
    with sexfade
    scene nodokamithree44 with cumflash
    with hpunch

    no "AAAAAAAAAaaAahhahahhAAaaaaAAAAaaAA!!!!!!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nodokamithree45
    with dissolve2

    a "Whoo boy...Can’t say I expected {i}that{/i} to happen when I walked in here today."
    no "The happiest ending...for everyone involved..."
    a "You’ve got that right, Ami Junior. Now please...excuse me as I...pass out..."
    no "Mm...yes...a nap...sounds...wonderful..."
    a "..."
    no "..."
    s "..."

    scene nodokamithree46
    with dissolve

    no "Okay. I’m done here."

    play sound "static.mp3"
    scene nodokamithree47 with flash
    stop sound

    s "Just...Just like that? You’re just going to leave?"

    scene nodokamithree48
    with dissolve

    no "Of course. What would I gain from staying? Assuming there won’t be another phase to our threesome, I mean."

    scene nodokamithree49
    with dissolve

    s "No, it’s just...it seems weird that you’d swap back to normal immediately after we’re done. Like you’re still up to something or-"
    no "If it’ll help you feel as if you’re not being deceived by your own intuition, feel free to chalk my actions here up to “research” or something of the like. That sounds rather Nodoka-esque, doesn’t it?"

    scene nodokamithree50
    with dissolve

    no "Ami, thank you for today. You accepted me even better than I’d hoped. It was truly a pleasure getting to suck your father’s cum out of you. I support your relationship wholeheartedly."

    scene nodokamithree51
    with dissolve

    a "Uhh...you’re...welcome?"
    s "{i}What are you doing, Nodoka?{/i}"
    no "Who is Nodoka? My name is Ami Junior. I love my Daddy and his cummy-wummies."

    scene nodokamithree52
    with dissolve

    a "Stop saying that! I’ve never-"

    scene black
    with dissolve
    stop music fadeout 15.0

    no "I’ll be awaiting your next call..."
    no "Aki-kun."

    play sound "dooropen.mp3"

    "In the mirror on Ami’s wall, I see three things."
    "The first is the smiling face of a girl who, once again, I don’t think I’ll ever understand."
    "The second is the face of someone else — my daughter. And the scowl it dons as she hears something she doesn’t like."
    "The third is me — confused and naked, somewhere between flaccid and erect as the fluids of two separate girls dry upon my flesh."
    "My face looks closer to Ami’s than it did to Ami Junior. Not just in its shape and features that accentuate the closeness of our DNA, but the emotions too."
    "I’m also scowling."
    "But I can’t tell if it’s because I hate that she left..."
    "Or because I hate that she exists."

    $ renpy.end_replay()
    $ nodokainvite3 = True
    $ nodoka_lust += 1

    a "Come here, Dad..."
    a "Let’s take a nap."

    "{i}Nodoka’s lust has increased to [nodoka_lust]!{/i}"
    "{i}You can now invite her over to the house!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
