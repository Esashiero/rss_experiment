label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
    if futaba_love >= 10 and library10 == False:
        jump library10
    if futaba_love >= 15 and futabadorm10 == True and library15 == False:
        jump library15
    if futaba_love >= 20 and library20 == False:
        jump library20
    if futaba_love >= 25 and futabanew3 == True and library20 == True and library25 == False:
        jump library25
    if futaba_love >= 30 and futabadorm25 == True and beachvacation16 == True and library25 == True and library30 == False:
        jump library30
    if futaba_love >= 35 and rindorm35 == True and futabadorm30 == True and library35 == False:
        jump library35
    if futaba_love >= 40 and futabadorm40 == True and yumicallnight35 == True and kaoridate15p3 == True and library40 == False:
        jump library40
    if futaba_love >= 50 and futabadorm50 == True and library50 == False:
        jump library50
    if futaba_love >= 55 and dormwarsfive14 == True and futabaspring2 == False:
        jump futabaspring2
    if chap4active == True:
        jump futabaspringlibrarygen
    if chapthreeactive == True:
        jump futabasummer2librarygen
    if christmas7 == True:
        jump futabamorninggen2
    else:
        jump library2to4

label futabainvite:
    if futabainvite1 == False:
        jump futabainvite1
    if futabainvite1 == True and futabainvite2 == False:
        jump futabainvite2
    if library50 == True and futabainvite3 == False:
        jump futabainvite3
    else:
        jump futabainvitegen

label futabainvitegen:
    play sound "phonebeep.wav"

    "I tap on Futaba's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    f "Hi, [futabamaster]! How are you doing?"
    s "I'm good. How about you, Futaba?"
    f "I'm...good as well."
    f "Did you need something or were you just...calling to chat?"
    s "Just checking to see if you're up to anything tonight."
    f "Tonight? I don't think so."
    s "Well, you are now. Come over to my place."
    f "Heheh~ That's a pretty rude way of asking, [futabamaster]."
    f "But sure. I'll head over now. I'm just going to take a quick shower first..."
    s "Sure thing. I'll see you soon."
    f "Yeah! See you soon~"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene futabainvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    f "So, umm...what's the plan for tonight, [futabamaster]?"

    "How should I spend my time with Futaba?"
    menu futabainvmenu:
        "Hang Out (Raise Affection)":
            jump futabainviteaff
        "Cunnilingus (Raise Lust)" if bonus == True:
            jump futabaeatout
        "Thigh Job (Raise Lust)" if library40part2 == True and bonus == True:
            jump futabathighjob
        "Missionary Sex (Raise Lust)" if futabainvite3 == True:
            jump futabainvitemissionary
        "Headpat" if bonus == True:
            jump futabaheadpat

label futabainviteaff:
    scene futabainvitegen
    with fade

    "Futaba and I spend the night quietly chatting in my room."
    "She tells me more about some of the things she's been writing and about how she's coming closer and closer to {i}finding her voice.{/i}"
    "I'm proud of her, but I always knew something like this was bound to happen once she got a little push from someone."
    "I'm still not sure why she needed me, of all people, to be the one to push her-"
    "But I'm the one that wound up with the job, so I did what I had to do and I don't regret a second of it."
    "Without any plans or desire to leave this place and actually do something, we wind up resigning ourselves to several hours of history channel documentaries."
    "It's not something I'm particularly interested in, but Futaba seems to enjoy it..."
    "So I take one for the team and proceed to watch a group of strange looking Americans appraise curious objects inside of a dinky old pawn shop."

    scene black
    with dissolve

    "The sun sets and the moon rises, prompting me to see if Futaba wants to order anything for dinner."
    "She thanks me for the offer but insists that she has food back at the dorm and is just going to eat there before going to sleep."
    "Eventually, the marathon of the pawn show comes to an end and we're thrust into a documentary about bees."
    "And, I can't believe I'm saying this, but it's somehow even {i}more{/i} boring than four dudes doing nothing but buying and selling stuff for hours on end."
    "Even Futaba must hate it, as she suddenly begins to pack up her things to head out before Ami gets back."
    "I walk her to the door and see her off with a hug."
    "She smiles as she leaves and the loneliness sets in again."

    $ futaba_love += 3
    stop music fadeout 5.0

    "{i}Futaba's affection has increased to [futaba_love]!{/i}"

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

label futabaeatout:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump futabaeatoutx
    else:
        $ futaba_lust += 3
        stop music fadeout 5.0

        "{i}Futaba's lust has increased to [futaba_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label futabathighjob:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump futabathighjobx
    else:
        $ futaba_lust += 3
        stop music fadeout 5.0

        "{i}Futaba's lust has increased to [futaba_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label futabamorninggen2:
    scene futabamorninggen2
    with dissolve
    play music "morningmoon.mp3"

    "I make my way to the library first thing in the morning to see how Futaba is doing."
    "It's incredibly warm inside but she's bundled up regardless. I honestly have no idea how she isn't burning to death."
    "Without anyone else in the library, which is apparently just how it is this time of year, we spend our time doing something absolutely {i}disgusting.{/i}"
    "That's right, ladies and gentlemen- we speak at a {i}normal{/i} volume."
    "I mean, why keep our voices down when there's no one around to realize how {i}sick{/i} and {i}twisted{/i} we are?"
    "But I digress."
    "Futaba and I leave the library for a few minutes and walk around the halls of the[school] on an off-day, something that will never cease to make me feel odd and out-of-place."
    "In a sense, though, I'm technically out-of-place in[school] to begin with. Just now there are less people around to notice it."

    scene black
    with dissolve

    "We eventually come back to the library to find a couple of girls from a different class trying to get in from the outside."
    "Futaba apologizes profusely for making them wait out in the cold and, after hearing her apologize roughly seven more times, I realize I have overstayed my welcome."
    "I bid goodbye to all three of them and quickly make my way back outside, wondering what I should do next..."

    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba's affection has increased to [futaba_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label futabanoongen2:
    play sound "phonebeep.wav"

    "I tap on Futaba's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    f "Hello?"
    s "Hey, Futaba. What are you up to?"
    f "Hi, [futabamaster]. I'm actually glad you called."
    f "I'm on my way to the bookstore and it would be nice if...you know."
    s "If I came with you?"
    f "Y-Yeah. That."
    f "If you wanted to, I mean. If you're busy, then-"
    s "Sure. Just text me the address and I'll meet you there."
    f "Oh! Okay! Sure!"

    play sound "phonebeep.wav"

    "The two of us hang up and I receive a text with the address just a few seconds later..."

    scene futabanoongen2
    with fade
    play music "love.mp3"

    "I wind up at the bookstore to find Futaba already browsing one of the aisles on the second floor."
    "It's a pretty large store, but the layout is simple enough that I was able to find her without any issue."
    "She stops looking around out of courtesy the second I make my way over to her, but I quickly assure her that she doesn't need to stop herself just because I'm around."
    "As such, she proceeds to sift through a bunch of old-looking fantasy novels and asks me a bunch of questions about which ones she should buy."
    "Not knowing much about that genre of literature, I simply choose the ones with the coolest names and, before long, Futaba is spending an absurd amount of money on books."
    "Having hobbies looks expensive."
    "It's times like this that I'm glad I'm really only interested in girls."

    scene black
    with dissolve

    "But, then again, girls can be expensive, too...so I guess I'm not entirely safe from the evils of commerce."
    "Thankfully, Futaba has a good amount of money that her parents send her from wherever they are overseas, so she's able to do things like this without much issue."
    "I wind up helping her carry everything as we exit the bookstore and, being the gentleman I am, I even accompany her back to the dorm."
    "I'm a little distraught that the entirety of our time together today was spent shopping, but..."
    "Well I guess that, more than anything, I'm just glad we got to spend some time together."

    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba's affection has increased to [futaba_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label callfutabamorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    else:
        "Futaba should be at the library right now."
        "I can probably see her there if I head over now."
        jump callmorning

label callfutabaafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if library30 == True and futabadorm35 == False:
        "Futaba has seemed a little overworked lately..."
        "I should probably leave her alone this afternoon."
        "Maybe I'll go see her later or something?"
        jump callafternoon
    if chap4active == True:
        jump futabaspringnoongen
    if chapthreeactive == True:
        jump futabasummer2noongen
    if christmas7 == True:
        jump futabanoongen2
    else:
        play sound "phonebeep.wav"

        "I tap on Futaba's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        f "Hello?"
        s "Hey, Futaba. What are you up to?"
        f "Oh, hi!"
        f "Umm...I'm not really doing anything."
        f "I just left the library so I'm kind of just...walking around and looking for things to do."
        s "So you're still near the[school]?"
        f "Mhm...I was probably just going to head back to the dorms if-"
        f "Wait, did you want to see me? I forgot to ask why you're calling."
        f "I don't want it to sound like I don't want to see you when I...definitely do."
        s "Well then how about we meet up at the park over there?"
        f "Oh! That sounds good. I actually just passed it a few minutes ago but...I can go back."
        s "Great. I'll see you there then."
        f "Y-Yeah! See you there!"

        scene futabaafternoongen
        with fade
        play music "love.mp3"

        "Futaba and I meet up at the park and spend the afternoon chatting about random things."
        "Several couples walk past us as we sit on the bench and each time, Futaba manages to get lost in thought watching them walk away."
        "In a perfect world, I'm sure she'd want something like that for the two of us."
        "She's always been one to get lost in daydreams, so I'm sure this student-teacher mask we're forced to put on in public can weigh heavily on her at times."
        "But even with the weight of that burden, her smile is able to brighten my day."
        "And who knows? Maybe some day, we'll be able to take that mask off."

        scene black
        with dissolve
        stop music fadeout 5.0

        $ futaba_love += 1

        "{i}Futaba's affection has increased to [futaba_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label callfutabanight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    else:
        play sound "phonebeep.wav"

        "I tap on Futaba's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "No answer. Maybe she's busy?"
        "I might be able to see her if I visit the dorms."

        jump callnight

label firsttimelibrary:
    scene black
    with dissolve2
    play music "morningmoon.mp3"

    "I decide to spend the morning at the library."
    "It’s still a little too early for me to bother getting involved in whatever is going on in the more exciting parts of town, so I figure relaxing in here is probably the best way to avoid that."
    "Besides, the library is attached to the school, which greatly increases my chances of bumping into one of my students and ultimately having sex with them."
    "This calculated move has been brought to you in part by a man with nothing to lose and everything to gain."

    q "Oh! Good morning, Sensei."

    scene blossomredux1
    with dissolve

    s "Good morning, Futaba. What brings you here today?"
    f "The same thing that always brings me here, I suppose...Until someone else volunteers to handle mornings, I'll be right where I always am on Saturday and Sunday."

    "Ah. So Futaba volunteers at the school library over the weekend. I guess that seems pretty in-line with the type of girl she came across as in {i}my{/i} journal."

    f "You’re here early as ever, I see."

    "And...I suppose {i}I{/i} also frequently drop by on the weekends? I guess that's useful to know."
    "I wonder if whoever the last person to possess this body was {i}also{/i} wound up being dragged here by an early morning appetite for immorality?"

    s "You know me. Early bird gets the worm and whatnot."

    "I do my best to feign a slightly pompous teacher-laugh but it sounds pretty terrible and I promise myself to never try that again."

    scene blossomredux2
    with dissolve

    f "Hahaha...right..."

    scene blossomredux3
    with dissolve

    f "Oh! That reminds me...Do you have a moment to go over the homework assignment from last week with me?"
    f "I was going to wait until we were in class again but, seeing as you're here right now...there's not really a need to wait."
    s "Oh. Uhh...sure. You might need to remind me what that assignment actually was, though."
    f "Of course, Sensei. I don't mind at all. Just give me a moment to get my notebook."

    scene black
    with dissolve

    "Futaba retreats behind the front desk and reaches into something on one of the shelves I can't see from where I'm standing."
    "She returns a moment later and pulls up a seat next to me, revealing a bright pink notebook that, based on a few glimpses I'm able to steal of the insides, seems pretty well-used."
    "The scent of her perfume tickles my nostrils as a gust of wind from the open window steers it closer to me."
    "It’s a mix of lemon and lavender- or at least something along those lines."
    "It’s subtle, but enjoyable...The type of scent I wouldn’t mind waking up to every day."

    scene blossomredux4
    with dissolve

    f "The assignment you gave us was another, umm...poetry interpretation thing."
    f "The part I'm having trouble with is this one poem in particular."
    f "I know that all you asked us to do was give you our interpretation of the writer’s words, but...I guess I'm just having trouble actually {i}interpreting{/i} anything."
    s "Not much of a poetry person?"

    scene blossomredux5
    with dissolve

    f "I like it! It's just...harder than what I'm used to."
    f "I...umm...well, I read mostly fantasy. And there's usually a lot less {i}interpreting{/i} to do in books that often overload you on details."
    s "Fair enough. Let's see what we've got here, then."

    "I peer into the notebook and scan the pages for whatever poem Futaba is referencing."
    "Thankfully, her handwriting is both elegant and easy to decipher, so I'm able to find it in no time at all..."

    s "'There are days we live...as if death were nowhere...in the background; from joy to joy to joy..."
    s "From wing to wing...from blossom to blossom...to impossible blossom...to sweet impossible blossom.'"

    f "..."
    s "..."
    f "So...what does all this mean, exactly?"

    menu:
        "Death creeps up on us":
            s "I think this stanza is about how death is much closer than most of us imagine."

            scene blossomredux6
            with dissolve

            f "Really? But that’s in such stark contrast to the rest of the poem."
            s "That’s exactly why this part hits as hard as it does."
            s "Like death itself, this poem embodies the same element of surprise typically associated with it."
            s "The more sudden type of death, of course. Not the drawn-out type we're all subjected to enduring over the course of our lives."
            f "That's...so much darker than I thought. No wonder I couldn't get it."
            s "Of course, we’re all free to create our own interpretations of the work. That’s the entire point of poetry, after all."
            s "I'm just letting you know how I feel about it."
            f "Wow..."
            f "You’re amazing, Sensei..."
            s "I exist."
            s "I might not be a great or attentive teacher, but even I can handle this much."
            jump chosepoem

        "Happiness is fleeting":
            s "The writer is attempting to get across how fleeting happiness can be."

            scene blossomredux7
            with dissolve

            f "That’s actually really close to what I thought at first!"
            f "The use of the ‘impossible blossom’ as a metaphor for happiness shows how unattainable and immature a never-ending state of ecstasy can and would be."
            s "See? It's really not that hard if you just go with your gut feeling."
            s "Overanalyzing things not only serves to break immersion and take you out of a moment, but is often entirely wrong and pointlessly convoluted."
            s "I guess that's just me being a little pretentious, though."

            scene blossomredux8
            with dissolve

            f "Heheh! Maybe..."
            f "Thanks so much for your help, though. I'm a lot more confident in my answer now."
            s "No problem. I expected nothing less from my star student."

            scene blossomredux9
            with dissolve

            f "Oh stop...We both know that role belongs to Makoto..."
            f "She's probably writing up a ten page paper on this as we speak."
            s "Yes, well, Makoto is a monster and that amount of work is entirely unnecessary."
            jump chosepoem

        "He likes blossoms?":
            s "I think the writer just enjoys blossoms."

            scene blossomredux6
            with dissolve

            f "Was it...really that easy? Was I being too analytical?"
            f "I read that stanza at least eight times trying to figure out a meaning, but to think it was as simple as {i}literally{/i} interpreting it-"
            s "Can we talk about something else?"
            s "After reading this, I'm not in the mood for poetry anymore."

            scene blossomredux10
            with dissolve

            f "Oh. Umm...of course. I'm sorry if this-"
            s "It's fine. Just talk about something else."
            f "Then...umm..."
            jump chosepoem

label chosepoem:
    scene blossomredux11
    with dissolve

    f "Oh, Sensei."
    f "I’ve been thinking a lot about your new approach to teaching, and I have a question."
    s "Sure. What’s up?"
    f "So, I understand the informal approach...but I don’t really understand why you want us to treat you more like a friend than an authoritative figure."
    f "Isn’t respect important to you?"
    s "Of course. But you can still respect someone you see as your friend, can’t you?"
    f "You can. It just...seems like a very sudden change of heart to me."
    f "Did something maybe...happen? Is it okay for me to ask that?"
    f "I don't want to...overstep my role as a student, but-"
    s "You're already venturing outside the box again by calling yourself that."
    s "If this relationship is going to work, you're going to need to stay {i}inside{/i} the box and see yourself as a little more than just a student."

    scene blossomredux12
    with dissolve

    f "Y...You're right. And I'm sorry."
    f "This is all just a little embarrassing for me. Being friends, I mean."
    s "And why is that?"
    f "Well, you’re like...so much cooler than all of us. Wouldn’t being our friend make you look bad?"
    s "Look bad in front of who? I don’t talk to anyone else besides all of you girls."

    scene blossomredux13
    with dissolve

    f "So you...don't have a...g...girlfriend or...anything?"
    s "Nope. Just all of you."

    scene blossomredux14
    with dissolve

    f "I see...I think I get it now."
    f "You’re a really...interesting person, Sensei...And I’m really glad that you’re our teacher."
    f "All of the teachers I had before you...never really seemed to care."
    f "But you actually listen to my problems when I come to you for help. And that..."
    f "That means a lot to me."
    s "I'm just doing my job in the least exhausting way possible. And if you ever need help, you know where to find me."
    f "Of course..."

    scene blossomredux15
    with dissolve

    f "On that note, though...maybe I'll start visiting your office again sometime soon?"
    f "I stopped coming because I didn't really want to bother you, but...just...being around you helps sometimes."

    "Futaba's tone changes- like she's admitting something she's been keeping bottled up."
    "The only thing is that the weight of her admission is so light that I can't imagine there was any reason to keep it bottled up in the first place."
    "I'm sure mine would feel that same way to someone else, though."
    "If I could even pinpoint where that weight is coming from, that is."
    "Right now, it all just feels like recycled air."

    s "Anyway...I should probably get going now."
    s "I’ve got a few other things I need to do today."

    "I don't."

    scene blossomredux16
    with dissolve

    f "Oh, right! I’m...sorry for taking up so much of your time. I realize how valuable it is for someone like you."
    s "I came here on my own, remember? You didn't take up anything."

    scene blossomredux17
    with dissolve

    f "Well, I'm sorry anyway. But I'm glad you stopped by again."
    f "I’ll see you in[school], Sensei. And thank you for helping me with my homework."
    s "Any time. I'll see you around, Futaba."

    scene black
    with dissolve2

    "I leave the library and begin to wander the school grounds, hoping that my mind manages to choose a direction to steer me in."
    "It does, but not until I have already lapped the building three times."
    "Futaba and I made eye contact the second time I passed the library window."
    "She still smiled at me, even though she shouldn't have."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ firsttimelibrary = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label library2to4:
    play music "morningmoon.mp3" fadein 2.0
    scene library
    with dissolve

    "I head to the library to hang out with Futaba."
    "When I get there, she waves me over to a table and immediately starts talking about some book she’s been reading."
    "It’s surprisingly cute to see how excited she gets when discussing it."
    "And even as someone who doesn’t particularly like reading, I can feel myself getting wrapped up in her description."
    "She’s so much different alone than she is in class."
    "I hope that some day she's able to act like this around everyone else as well..."

    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label futabafall:
    scene newfall1
    with fade
    play music "morningmoon.mp3"

    "Another morning means another chance to hang around an attractive girl, and so I find myself where I have found myself on several occasions now-"
    "And probably even {i}more{/i} occasions in a life I can’t remember."
    "The only issue this time around is that the girl in question has yet to notice my presence and I have now been standing here for going on five minutes."
    "What’s even worse is that there are other people here. And seeing as Futaba is the only working volunteer, it has fallen on me to help all of the people she has ignored."
    "This may come as a surprise to you, but I am not very good at helping people."
    "So I am sorry to everyone who I have misinformed today, but that is simply how things must be until I am able to snap the regular weekend librarian out of her daydream-induced stupor."

    f "..."
    s "Futaba, for the millionth time, good morning."
    f "..."
    s "..."

    "Whatever is going on inside that head of hers must be pretty interesting if even hearing {i}my{/i} voice, the one she adores so much, is not enough to snap her out of it."
    "But, then again, it might not be very interesting at all seeing as how every time I get caught in a daydream like that, one of my hands ends up inside of my pants."
    "Futaba has yet to make such a move, unfortunately. And as much as it pains me to say this, I’d have to break her out of it if she did."
    "I am all for the idea of watching her pleasure herself in the library, but doing so in a room full of other students would very likely not be a good move for me."

    f "..."
    s "..."
    f "..."
    s "..."

    "So, what are some other things I can think about in the time between now and whenever Futaba wakes up?"
    "Oh. The weather is nice today. Clouds are expected in the afternoon, with the morning being a bit on the colder side compared to the norm as of late."
    "The birds are chirping, the sun is shining, and I am still an incorrigible predator waiting to feast upon the flesh of an overly-developed teenage girl."
    "Good morning, world. I am here."

    s "Futaba. Please snap out of it before my thoughts start spiraling even further into the abyss."
    f "..."
    s "Futaba. I really need-"

    scene newfall2
    with hpunch

    f "Huh? Sensei? What’s wrong?"
    f "And...how long have you been there exactly?"
    s "Probably ten minutes now. I was only a few more away from calling an ambulance."

    scene newfall3
    with dissolve

    f "I’m so sorry, Sensei. I started reading a new book last night and...I suppose I may have started thinking about it while waiting for you to show up."
    s "Why not just...keep reading the book?"

    scene newfall4
    with dissolve

    f "Because I left it at home."
    s "Futaba, this is a library. Just get another copy."

    scene newfall5
    with dissolve

    f "I’m okay with waiting until I get back home. It wouldn’t be right for me to spend my time getting absorbed in something when there are people here who need assistance."
    s "Yeah, about that. A bunch of people {i}have{/i} needed assistance and you kind of just ignored them."

    scene newfall6
    with hpunch

    f "I...what?!"
    s "Futaba, don’t yell. This is a library."

    scene newfall7
    with dissolve

    f "How...How many people have I ignored? "
    s "I stopped counting after three."
    f "Why would you stop counting after such a low number? "
    s "Why would you forsake your responsibility as a librarian and neglect your job? This is on you, not me."
    f "Sensei...you...wouldn’t happen to know what time it is, would you?"
    s "Probably somewhere around 10:00 AM. I stopped keeping track of that as well."

    scene newfall6
    with hpunch

    f "10:00 AM?!"
    s "We’re still in the library, you know. People are trying to study and you have done nothing but make things harder for them today."

    scene newfall7
    with dissolve

    f "I...haven’t even started reorganizing the shelves yet. And I promised I’d have the entire library done by noon..."
    f "Sensei...you...wouldn’t mind helping-"
    s "Oh, no. I’ve already helped over three people today. If I wanted to help more than that, I’d just start volunteering here myself."

    scene newfall8
    with dissolve

    f "Hah...I suppose I’ll just have to stay later then. This is the price I must pay for letting my imagination run wild again."
    s "If it’s any consolation, I’m not opposed to standing around and further preventing you from doing your job with continued conversation about what was going on in your head a few minutes ago."

    scene newfall5
    with dissolve

    f "At this point, I think that would be fine...I’m already going to have to stay late anyway, so having you around might actually make time go by a little faster."
    s "Then, by all means, start organizing your shelves or whatever it is you need to do while I transition back into the unhelpful burden of a man I am meant to be."

    scene black
    with dissolve2

    "Futaba tears herself away from the desk, closing a notebook that only has a small handful of words scribbled into it, before making her way across the library."
    "I think to myself about whether or not she’d only gotten sucked into daydreaming because she was attempting to write, but ultimately ignore the thought as it doesn’t really interest me."

    scene newfall9
    with dissolve2

    "Unfortunately, the thought comes back just a few moments later when I can’t think of anything else to talk to Futaba about."

    s "So...is everything okay, Futaba?"
    f "Hm? Of course. Everything is completely fine, Sensei. I just get caught up in little daydreams like that from time to time. It’s nothing to worry over, really."
    s "I saw you close a notebook before we got up. Were you trying to write something?"

    scene newfall10
    with dissolve

    f "That’s...um...well..."
    f "To be honest, I’m not really sure how to put this..."
    s "Are you...embarrassed to be caught writing or something?"

    scene newfall11
    with dissolve

    f "It’s less embarrassment about being caught writing and...more embarrassment about exactly {i}what{/i} I was writing."
    f "I’ve always had problems...coming up with my own stories, so...I often find myself just adding to stories made by other people."
    s "Like...writing unofficial sequels or something like that?"
    f "Kind of?...Not just sequels, but...side stories and...alternate scenarios and...things like that."
    f "There’s a term for it. {i}Fan fiction.{/i} But a lot of people frown upon it since it’s not entirely original and...the quality of a lot of it is...really, really bad."
    f "I’m...sure that nothing I do really helps to...break that stigma, but...it keeps me occupied when I’m not actually reading."

    scene newfall12
    with dissolve

    f "W...What I’d really like to do is eventually come up with my own stories, though! From the ground up!"

    scene newfall13
    with dissolve

    f "A good friend of mine from my old school does that...and she’s found a lot of success in...umm...{i}certain circles.{/i}"
    f "I can’t imagine I’ll ever be anywhere as good as her since she’s always been a sort of prodigy, but...I think it would be really nice to also be able to do something like that one day."
    s "Interesting."
    s "Well, I don’t know anything about this fan fiction stuff, but I’m sure that you’d be able to write an original story if you actually apply yourself. "
    s "You certainly {i}read{/i} enough to know what would make a good book."

    scene newfall14
    with dissolve

    f "I do...But, as I’m sure you know, reading and writing are two completely different beasts."
    f "And just because I read a lot doesn’t mean that I’ll be able to come up with an interesting story."
    s "That doesn’t, no. But what about whatever daydream you were having when I showed up?"
    f "That...daydream was another one of my...umm...alternate timelines ideas again..."
    s "Are they all like that?"
    f "All of them? No. I have plenty of original ones too. I just-"
    s "Then how about writing one of those? "
    s "If they’re interesting enough to tear you away from reality for ten minutes at a time, I’m sure there are plenty of other people who’d enjoy reading them as well."

    scene newfall15
    with dissolve

    f "Well...yes. They’re interesting to me...But who’s to say that someone else will enjoy them as much as I do?"
    s "Who’s to say literally anything in this life? Caring more about what others think about your work means nothing compared to what {i}you{/i} think about it."
    s "So what if no one else enjoys it? As long as you do, isn’t it worth the effort?"

    scene newfall16
    with dissolve

    "Futaba pauses for a moment as blood begins to pool in her cheeks and I think about how strange it is that words alone can influence the fluids inside of a person’s body."
    "I wonder if her words will ever do that for someone else?"
    "And I wonder what type of words they would be."

    f "You’re..."
    f "You’re so cool..."
    s "Thanks, Futaba. I try."

    scene newfall17
    with dissolve

    f "Oh! Uhh...haha! I didn’t really mean to say that out loud...but I guess it just kind of slipped out."

    scene newfall18
    with dissolve

    f "That was...a really inspiring thing to say, though...But I guess if anyone was going to be able to give me the push I needed, it would be you."
    s "I’m sure it won’t be the last time I push you. In fact, what if I give you a little assignment to push you even further?"

    scene newfall19
    with dissolve

    f "An assignment?"
    s "Yeah. Take one of those original daydreams of yours and try turning it into a full-fledged story. The kind without characters who already exist in properties owned by other people."
    s "I’ll read it and give you my honest thoughts along with any criticism I may have. "
    f "You...would really go out of your way for me like that?"
    s "Sure.  Writing is a mutated reflection of a person’s innermost self."
    s "The more you put on paper, the more I’ll understand you."

    "And the more I understand you, the closer we’ll become."

    scene newfall20
    with dissolve

    f "And if it’s not good?..."
    f "If I can’t write something that...serves as a reflection...will that ruin your chances of ever {i}understanding{/i} me?"
    s "No clue. I can’t predict the future."
    s "I just don’t think it’s fair to hold yourself back from something you want to do just because you’re afraid of what other people would think."
    s "Especially when one of those {i}other people{/i} is standing right in front of you, telling you to go for it."

    scene newfall21
    with dissolve

    "Futaba locks eyes with me in disagreement with what the pools of blood inside her cheeks would have her do."
    "She pushes back, but her words do not influence my bodily fluids the way mine influenced hers."

    f "Okay..."
    f "I’ll do it. I’ll start writing something. Something original."
    f "I..."
    f "I want you to understand me a little better, Sensei."
    f "I want to write something you can be proud of."
    s "I had a feeling you’d say that."
    s "I won’t give you a due date or anything, obviously. You’re free to do this at your own leisure. And if you need any suggestions or help with anything, feel free to ask."
    s "Just don’t tell any of the other girls about this since I am absolutely giving you special treatment right now."
    f "Can I...or...umm..."

    scene newfall22
    with dissolve

    f "Is it okay if I ask...{i}why{/i} you’re giving me special treatment?..."

    "Her blood wins out in the end."
    "She turns away."

    s "I don’t really have a reason for it."
    s "I guess I just have a soft spot for girls who write."

    scene black
    with dissolve2

    f "Then..."
    f "I’ll do my best to become one of those girls."

    "I don’t stay around for much longer as Futaba still has a decent amount of work to do and my presence has all but prevented her from getting {i}anything{/i} done at all."
    "As such, I take my leave and begin to look for something else to do with the rest of my day."
    "I have no idea what Futaba will manage to create...or even if it will be any good."
    "But at least she’s going to try."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ futabafall = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label library6to9:
    scene futabafall1
    with dissolve
    play music "morningmoon.mp3" fadein 2.0

    "I decide to spend my morning in the library with Futaba."
    "Apparently, the senior class has an important exam coming up, so the library
    has been getting a bit more traction than normal lately."
    "Not wanting her to feel overwhelmed by the increased workload, I help her
    clean things up and put away a few books."
    "I’m happy that she finally seems to be getting a little more comfortable with me."

    scene black
    with dissolve

    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    jump saturdayafternoon

label library10:
    scene upsidedownredux1
    with dissolve2
    play music "morningmoon.mp3"

    "I stop by the library first thing this morning."
    "The impending exams that had flipped this place on its head recently have finally ceased to be and Futaba and I can now go back to being normal."
    "Or at least as normal as we can be as a student and the man who is trying to fuck her."

    f "Thanks so much for helping out lately, Sensei. I really don’t know what I would have done without you."
    s "I’m sure you would have managed. It’s just a library after all."

    f "Calling it {i}just{/i} a library really diminishes the work I do, you know."
    f "If I had been doing everything on my own, organizing all of the shelves would have taken twice...or maybe even three times as long."
    f "I wouldn’t have had any time left to write that assignment you gave me."
    s "Oh, right. That's a thing I asked you to do."
    s "How is that coming, by the way? We haven’t really talked much about it since then."

    scene upsidedownredux2
    with dissolve

    f "I, uhh..."
    f "I think...I’m finally ready to show you something."
    f "But it's not done yet, so...you have to promise not to laugh if it doesn’t live up to your expectations..."
    s "Don't worry, Futaba. I won't laugh even if it's the worst thing I've ever read."

    scene upsidedownredux3
    with dissolve

    f "Was that...supposed to make me feel better? Or..."

    "Futaba nervously slides a notebook across the table to me."
    "I quickly flip through the pages to find that her story is the only thing written in it."
    "Why she decided to write it in the {i}middle{/i} of the book instead of where any sane person would write it, I have no idea."
    "But it appears to be only a few pages long, so I should be able to knock it out rather quickly."

    s "Futaba...You know you could have used your normal notebook, right? You didn’t have to buy a new one just for this."

    scene upsidedownredux4
    with dissolve

    "Futaba shakes her head once in disagreement. The long braid draped over her shoulder dances across her chest and quickly catches my eye before settling back in place."

    f "I figured it would be best to buy a new one so you wouldn't go snooping through my notes."
    s "Oh? Are you keeping something in there that I should be worried about?"

    scene upsidedownredux5
    with dissolve

    f "’Worried’ probably isn't the right word...But I’d definitely prefer if you didn’t see anything in there."

    if bonus == True:
        s "I get it. It’s not unusual for a girl your age to want some privacy."
        s "I guess I'll just have to ask one of your classmates what sorts of things you've been writing about me in there."
        f "Umm...please don't."
    else:
        s "Futaba, it's fine. Twilight sold millions of copies and only had like, three adjectives used across four books."
        f "Guh..."

    s "I was kidding. Your notes are {i}your{/i} notes and...all I'll read is whatever you just handed to me."

    scene upsidedownredux4
    with dissolve

    f "Thank you, Sensei...But again, please don't expect too much."
    s "You've already surpassed my expectations with this avant-garde approach of writing in the middle of the book, so I'm already at the edge of my seat."
    f "Well, I-"

    scene upsidedownredux6
    with dissolve

    f "Wait, what? The middle of the book?"

    scene black
    with dissolve

    "I carefully flip back to the start of the story and begin to read..."
    "Futaba quickly gets out of her chair and stands beside me, causing me to think for a moment that maybe she'd given me the wrong notebook on accident."
    "But once I begin reading and she doesn't stop me, I realize that might not be the case at all."

    scene upsidedownredux7
    with dissolve

    f "What is-"
    f "That's not my handwriting..."
    s "{i}Somewhere, in the middle of nowhere, there is a house.{/i}"
    s "{i}This house, which seems ordinary on the outside, is actually anything but.{/i}"
    s "{i}You see, this house is upside down.{/i}"
    s "{i}Normally, if you flip a house on its head, the people inside of it will fall down.{/i}"
    s "{i}But the girls living in this one don’t.{/i}"
    s "{i}In fact, some of them even prefer to live this way.{/i}"

    "I pause for a moment and wait to see if Futaba has anything to say, but she remains as still and silent as a corpse."

    s "{i}You see, this house sits at the edge of the universe.{/i}"
    s "{i}And much like the country we live in, this place has its own set of rules.{/i}"
    s "{i}Don’t stay up too late, don’t eat more food than you require in a day, and don’t question Papa.{/i}"
    s "{i}It’s that easy!{/i}"
    s "{i}As long as the rules are followed, everyone can live a happy life devoid of any negative feelings whatsoever.{/i}"
    s "{i}It’s a truly wonderful place!{/i}"
    f "..."
    s "..."

    s "Umm...Futaba...What exactly am I reading?"

    scene upsidedownredux8
    with dissolve

    f "I have no idea...I've never seen this book in my life."
    s "So...you just happened to give me someone {i}else's{/i} creative writing project instead?"
    s "It's okay to be embarrassed with your work, but denying that you wrote it is just-"

    scene upsidedownredux9
    with dissolve

    f "I really didn't write this, though! I swear!"
    s "Well, did you swap notebooks with someone on accident or something?"
    f "I...I don’t think so? I hadn't even taken this one out of my room until today..."
    f "I don’t understand this at all..."
    s "Should we keep reading? It's not over yet."
    f "I...suppose we can? But this is...really starting to weird me out."

    scene upsidedownredux10
    with dissolve

    "Futaba moves a little closer to me as I try to find where we left off..."

    s "{i}There are so many books here, yet none of them say anything. I wonder why that is?{/i}"
    s "{i}Is it because I’ve already read them, or because I simply cannot see?{/i}"
    f "Whose perspective is this coming from?..."
    s "I don’t know. It was being narrated a minute ago, but...it seems to have swapped storytellers or something."
    f "This is so weird...I have no idea how this happened..."

    "I continue reading."

    s "{i}The smell was horrible coming from the boiler room.{/i}"
    s "{i}It was like burnt rubber mixed with rotting flesh. A truly horrible scent.{/i}"
    s "{i}No matter how hard I try to forget it, it clings to my nostrils and sticks in my hair.{/i}"
    s "{i}It makes me want to shed my skin.{/i}"

    scene black
    with dissolve

    s "Okay. That's enough of that."

    "I abruptly close the notebook and toss it back onto the table."
    "Futaba looks down at it for a moment like she's caught in a daze before sitting back down to regain her composure."

    scene upsidedownredux11
    with dissolve

    f "I don't get this at all...it was a brand new notebook..."
    s "You don’t think...Rin could have a similar notebook or something, do you? Or maybe she's just trying to fuck with you?"
    s "You two share a dorm. I don't think it's impossible that she-"

    scene upsidedownredux12
    with dissolve

    "Futaba starts shaking her head before I can even finish my sentence."

    f "It’s not possible. I’ve read Rin’s writing before and it’s nothing like this. The handwriting is different too."
    f "This is just plain creepy..."
    s "It was definitely weird...but I wouldn't put past someone as weird as her to write something like this."
    f "It wasn't Rin, Sensei...I'm absolutely certain of that."
    s "..."
    f "..."
    s "Well, I guess it would probably be for the best to just throw that thing away or...bring it to the lost and found or something."

    scene upsidedownredux13
    with dissolve

    f "I agree. I'll be sure to do that as soon as I leave here today."
    s "As for {i}your{/i} story, do you think it’s still in your dorm room somewhere?"

    scene upsidedownredux14
    with dissolve

    f "I really hope so! I've been working hard on it and...am not comfortable with anyone other than you reading it just yet."
    s "Well, check when you get back and let me know. It sucks we couldn’t read it today after all the effort you put in."

    scene upsidedownredux15
    with dissolve

    f "It’s fine. If anything, I’m sorry that you had to read something as weird as...whatever {i}that{/i} was just now."
    s "There’s no need to be sorry, Futaba. Well, unless this is some really abstract, confusing prank that you're pulling on me. If that's the case, you can apologize and I will accept."

    scene upsidedownredux16
    with dissolve

    f "I'm not really the type of person to play pranks on others...nor would I understand how this would even count as a prank."
    s "Then I guess we'll just have to live in a state of perpetual mystery in which we never discover why this happened or who was responsible for it."
    f "I'll ask Rin just to be sure, but...again, I really don't think it was her..."
    s "Let's just try to put it behind us for now and...hang out like we always do. Without any weird boiler rooms or indiscernible narrators."
    f "Good idea, Sensei...I know we didn't read much of it, but..."
    f "That story was really starting to make me feel a little uncomfortable..."

    scene black
    with dissolve2

    "Futaba and I continue to talk for the rest of the morning, never once returning to the words found inside of that strange notebook."
    "She wasn't the only one who felt uncomfortable, though."
    "Even now, each time I think about it, it feels like my stomach is tying itself in knots."
    "Or at least something like that."
    "I eventually leave the library."
    "The knots untie themselves."

    stop music fadeout 5.0

    $ renpy.end_replay()
    $ library10 = True
    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label library15:
    scene insertredux1
    with fade
    play music "morningmoon.mp3"

    "I have once again returned to the library to be fawned upon by a busty librarian- a thing that most people in life will, unfortunately, never get to experience."
    "Our last meeting here was a bit...unusual, so I’m hoping today is at least slightly more grounded in reality and doesn't involve any more strange notebooks."
    "Just...what was that thing we read?"
    "I can’t remember much of it on account of how quick I was to just toss it aside, but what I do remember is-"

    play sound "static.mp3"
    scene insertredux2 with flash
    scene insertredux3 with flash
    scene insertredux2 with flash
    scene insertredux3 with flash
    scene insertredux1 with flash
    stop sound

    "I can't remember anything about it."
    "Time for girl."

    f "Good morning, Sensei. You’re here a little early today."
    s "I don't think that's true. I left around the same time as always and checked my phone right before coming in here."

    scene insertredux4
    with dissolve

    f "Wait...really? But there’s no one else here yet and you're never the first person in the library after me."
    f "And I know that for a fact because I always judge the time based on how many people show up before you."
    s "What happens if I don’t show up?"

    scene insertredux5
    with dissolve

    f "Hmm...I guess-"

    stop music
    scene tree3

    "TIME STANDS STILL"

    scene insertredux1
    play music "morningmoon.mp3"

    s "Did you bring your story?"

    scene insertredux6
    with dissolve

    f "Oh! Yes! And I even made sure it was the right one just a few minutes ago, so we don't have to worry about any other...strange stories appearing in its place."
    f "I still have to make a few minor changes here and there...but I think it should be at least partially readable by now."
    s "That's great news. I tend to find that most of the best literary works out there are at least partially readable."

    scene insertredux7
    with dissolve

    f "Well, I'm certain this is nowhere near the best, but...I tried my hardest."
    s "So, give me the run-down of your story. Did you try drawing upon any of those daydreams of yours like we talked about?"
    f "Well...kind of. But I can't really draw upon the ones that have already happened since I've always just...forgotten them once they end."
    f "I’ve started keeping track of some of the newer ones, though...so the story you’ll read today is about one of those. And-"

    "Futaba pauses for a moment as she glances over at what I'm assuming is her bag."

    scene insertredux8
    with dissolve

    f "I'm sorry...I’m just suddenly feeling really nervous all of a sudden..."
    s "There's no need to be nervous. This is no different than handing over an assignment in class...Probably."
    s "I haven't really accepted any assignments {i}lately,{/i} but I imagine this is kind of like that."
    s "All things considered, I'm happy with it just being partially readable. The fact that you're comfortable with it is more than enough for me."
    f "Well...okay."
    f "But just...try not to hate it, please..."

    scene black
    with dissolve2

    "Futaba timidly pulls a notebook from her bag and hands it over to me with trembling fingers."
    "I lean my back against the window and begin to read what seems like a fairly typical story."
    "A girl sits at home alone in a room full of stuffed animals, wondering what it is about life that leaves her so unfulfilled."
    "She doesn’t have many friends- just one. A cat named Pedro who walks with a limp."
    "It’s a minor detail, but it’s little things like this that make the world more believable."

    scene story1
    with dissolve2

    f "..."
    s "..."

    "I can tell that Futaba is nervous simply by the way she’s standing next to me."
    "Every once in a while, she lets out a deep breath, as if she’s counting down from ten in order to calm her nerves."
    "Whatever it is, it doesn't seem to be working as she's done it continuously throughout my entire reading session thus far."

    s "..."
    f "..."

    "I continue reading Futaba’s story and, as expected, it goes exactly where I imagined it would."
    "Eventually, the girl meets a boy who doesn’t see her the way everyone else does."
    "He’s not popular or an athlete or anything like that- just an average guy with no discernible traits or characteristics."
    "Things progress and the two of them start dating."
    "It’s a story that appears to be about overcoming self-perception or...allowing yourself to lean on others when that doesn't seem possible."
    "It’s clearly parallel to how I imagine Futaba feels in real life."
    "I do have one question, though..."

    scene story2
    with dissolve

    s "Why did you kill Pedro?"

    scene story3
    with dissolve

    f "Was that part...bad?"
    s "It wasn’t {i}bad.{/i} It just felt...uncalled for? It didn’t really add anything to the story and felt like it was just...more of a shock value thing."

    scene story4
    with dissolve

    f "It was...supposed to symbolize hardship since...he was her only friend at first."
    s "There were symbols of hardship all over the place and the cat was essentially abandoned as a character as soon as the guy came along."
    f "So...I’m...a failure then?"
    s "You're not a failure. It was actually a pretty solid story apart from that."
    s "Maybe a little basic, but a great first attempt. I’m impressed."

    scene story5
    with dissolve

    f "Wait...You mean that? You liked it?"
    s "Sure. Great job, Futaba. Another A+ in the grade book that I totally keep and am not making up."

    scene story6
    with dissolve

    f "Then...umm...What did you think about the main character?..."
    f "Was she...likeable?"
    f "Is that...the kind of person you'd want to spend time with in real life?"

    "Ahh, there we go. Futaba wants me to grade her self-insert character that ends up alongside the insert-version of me."
    "The honest answer would be that the girl in her notebook is just as unremarkable as the man she ultimately falls for."
    "But I’ll let that slide for today since the one in real life is better and...significantly more tangible."

    s "I think she was really interesting, Futaba."

    scene story7
    with dissolve

    f "Really?! You think so?!"
    s "I do. It's unfortunate the story ended where it did."
    s "I'd really like to learn a little more about her."

    scene story8
    with dissolve

    f "You'd like to...learn more about her, huh?..."
    f "If only...we knew who the writer was...Hahaha...Hah..."
    s "Right. {i}If only.{/i}"

    scene story9
    with dissolve

    f "Umm...Sensei?..."
    f "I just want to say thank you for always being around and...giving me positive encouragement and all that."
    f "I was really nervous about today and...you made me feel really calm..."
    f "So, umm...I wouldn't mind telling you a little more some time..."

    scene story10
    with dissolve

    f "About the character, I mean..."
    s "Oh yeah? I think I might have to take you up on that. I’ve been meaning to stop by your dorm again anyway."
    f "Well...You know which room I’m in, so..."
    f "I'll be there...whenever you want..."

    scene black
    with dissolve2

    "The two of us chat for a few more minutes before it comes time for me to head out."
    "Her story was a lot longer than I expected a first-try to be...but I’m honestly really impressed, all flaws aside."
    "For someone who doesn’t normally write, she definitely has potential."
    "I’m sure all the reading she does helps, but that sort of thing can only carry you so far."
    "Eventually, we part ways- but not before making plans with Futaba to meet up again soon."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ library15 = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    jump saturdayafternoon

label library20:
    scene onlychildredux1
    with fade
    play music "normalday.mp3"

    f "Oh, Sensei! Good timing."
    s "Good timing for what? What's going on?"
    f "I was actually just about to leave, so I’m happy you showed up when you did."
    s "Futaba, I am not going to watch the library for you. Especially because I don't even think you get paid for this."
    f "I don't. But I'm not going to ask you to do that either since I actually {i}don’t{/i} have to volunteer at all today. I just completely forgot and showed up anyway."
    s "Well, I'm glad you did. Because if I showed up here and you weren't around, I have no idea what I would even do."
    f "You could always read?"
    s "Pass."

    scene onlychildredux2
    with dissolve

    f "Regardless...the library is going to be closed for cleaning today, so you wouldn't be able to read even if you wanted to."
    s "Uh-oh. What are you going to do if you can't spend your morning surrounded by books?"

    scene onlychildredux3
    with dissolve

    f "Well...I was kind of hoping...that's where you'd come in."
    f "You know...since you {i}also{/i} don’t have anything to do..."
    s "Sounds good. I’ll hang out with you."

    scene onlychildredux4
    with dissolve

    f "You will?! Outside of the library?!"
    s "Sure. I mean, like you said, what else do I have going on?"
    s "Besides, it might be good for the two of us to get out instead of just hanging around here all the time. And that's doubly true for today since it's actually not extremely hot out."

    scene onlychildredux5
    with dissolve

    f "The weather has been rather unkind lately, hasn't it?"
    s "So, what should we do with our new-found free time? Want to go get lunch or something?"
    f "I would love to...If that’s okay with you, of course."
    f "I can't imagine it would be a...very good look for you being out at some restaurant with someone so much younger..."
    f "Not to mention that some of the other girls from our class could be around here right now..."
    s "I don’t really mind. If we run into someone from class, we can always just tell them I’m helping you study or something."
    s "And if that doesn't work, I'll probably just wind up having to spend some alone time with whoever catches us. So it's really not a big deal."

    scene onlychildredux6
    with dissolve

    f "Heheh...I suppose...that’s one way to handle that situation..."
    s "Hey, if you're jealous about me hanging out with the other girls, just try a little harder to not get us caught today."

    scene onlychildredux7
    with dissolve

    f "I don't...really think that's in my hands, Sensei."

    scene black
    with dissolve

    s "Well, there's only one way to find out. Come on, Futaba."
    f "Wait! Sensei! I still have to pack up my things!"

    "Futaba and I leave the library and begin to head down the same road I normally take home."
    "There are plenty of couples out and about today, but no one that we recognize."
    "Well, at least not yet."
    "After a while, we come to a stop in front of a small restaurant that Ami and Maya eat at often and decide that this is a suitable place to settle down for the time being..."
    "........."
    "......"
    "..."

    scene futabaday1
    with dissolve

    f "Umm...thanks for hanging out with me today, Sensei."
    f "I know you probably have lots of other stuff to do and-"
    s "I'm going to stop you right there, Futaba. I don't want you making it sound like I’m only doing this for you."
    f "But...I'm-"
    s "You know, one of these days, you’re going to have to accept that I might just enjoy your company."

    scene futabaday2
    with dissolve

    f "Yeah...uhh...that might be a little harder than you think."
    f "A girl like me...hanging out with someone as cool and...awesome as you? It just...doesn’t really make sense."
    f "You've noticed how people have been looking at us, haven't you? It’s like they know..."
    s "Yeah, I think there might be other reasons why people have been looking at us strangely."

    scene futabaday3
    with dissolve

    f "What...exactly do you mean by that?"
    s "I mean that even if you don't look as young as someone like Ami or Sana, I'm still noticeably older than you."
    s "I could probably even be your father."

    scene futabaday1
    with dissolve

    f "Don’t be silly, Sensei. My father is way older than you are."
    f "If anything, you'd be more like...my older brother."

    scene futabaday3
    with dissolve

    f "If...you can get past the part where we don't look anything alike."

    "Come to think of it, I don’t really know anything about Futaba’s family."
    "In fact, I barely know anything about Futaba apart from her affinity for both books and me."
    "That said...wouldn't this be a good opportunity to maybe learn about some of that?"
    "It's clear that the two of us are getting closer, but there's a limit to how close we can get without me going out of my way to learn more about her."
    "And I know wording it like that might make it seem like I don't {i}want{/i} to know anything about her, but that's not true."
    "I just think it would be a lot easier {i}not{/i} to."

    s "So...on the topic of family...why don't you tell me about yours?"
    s "I don't really know anything about them."

    scene futabaday4
    with dissolve

    f "My family? Is that...something you're actually interested in hearing about?"
    s "Sure. I mean...they're a part of your life, aren't they? You can't just keep me in the dark about your backstory forever."

    scene futabaday4r
    with dissolve

    f "Heheh...no, I suppose I can't. I can't guarantee you'll be entertained, though, as I don't think we're all that abnormal."
    f "Is there anything in particular you want to know? "
    s "How about...your parents? What do they do? Do they live around here?"
    f "They did. They live overseas now, so I haven't seen them since before Kumon-mi was closed off."
    f "Well, in person. I still video chat with them every once in a while."

    scene futabaday2
    with dissolve

    f "It’s a little sad that they're so far away...but I’m independent enough to function on my own, so it’s not like I {i}have{/i} to see them or anything."
    s "How far overseas are they, exactly?"

    scene futabaday4r
    with dissolve

    f "America. My father is an architect and is working on a bunch of aquariums for some company over there."
    f "And of course my mother followed him since the two of them are pretty much inseparable."

    "It’s good to see that there’s at least one fully functioning family still out there. I was beginning to think that all of my students were from broken homes."

    s "Do you look more like your father or your mother?"
    f "My mom. She’s like a prettier, skinnier, taller version of me."
    s "Prettier than you? I find that hard to believe."

    scene futabaday5
    with dissolve

    f "Sensei, stop! That’s way too embarrassing and...definitely not true."

    if bonus == True:
        s "Sorry, I couldn’t help it. I made a promise to myself many years ago that I would capitalize on every single chance I have to flirt with attractive girls."

        scene futabaday6
        with dissolve

        f "I guess that explains why you're so good at it...It must be all the experience."
        s "It definitely comes in handy during times like this."
    else:
        s "I apologize and will now proceed to talk about something entirely different."

    s "So, what about siblings? Do you have any?"

    scene futabaday4r
    with dissolve

    f "I don’t. I’m an only child."
    f "My mom wanted to have at least one more, but she and my dad decided it wouldn't be a good idea since the two of them travel so much."
    f "It's fine, though. I would have liked having a sibling, but I lucked out and wound up with Rin instead."
    f "She might not look like me, but she's better than any other sister I could have possibly asked for."
    s "Well, she definitely seems like she can be a handful at times...so I guess that having her is more than enough to fulfill your sibling quota."

    scene futabaday2
    with dissolve

    f "Hahah...I suppose so..."
    f "I...wouldn’t mind having a big brother as well, though. I’ve kind of always thought it would be nice to have a person like that."
    s "Any reason why?"
    f "I don’t know...I just think it would be nice to have someone who would always look after me."
    f "Unfortunately...I don't think I'll-"
    s "Don’t worry, Futaba. I’ll look after you."

    scene futabaday6
    with dissolve

    f "Heheh...You promise, Sensei?"
    f "Because I won't let you take something like that back, you know."
    s "Fine by me. I can't imagine wanting to go back on that."
    f "Is it okay if I call you big brother then?"
    s "Of course it is. In fact, please start calling me that right now."

    scene futabaday7
    with dissolve

    f "W-Wait a second! I was only kidding!"
    f "There’s no way I can just...start calling you that right now! It’s way too embarrassing!"
    s "Too late. You’ve already brought it up and it's something I absolutely need to hear now."
    f "It's also something I absolutely can't do!"
    s "How come you can call Rin your sister but not me your brother?"
    f "Because I don't have a c-"

    scene futabaday8
    with hpunch

    f "Cat! I don't have a cat! I definitely wasn't going to say {i}crush!{/i} Nope!"
    s "..."

    scene futabaday9
    with dissolve

    f "A-Anyway! What else do you want to know about my family?! I'll tell you anything you want!"
    s "You don't have to make it sound like I'm shaking you down, you know?"

    scene black
    with dissolve2

    "Futaba and I spend the next hour or so discussing her parents while finishing our meals."
    "As it turns out, she barely even remembers the last time she saw them before they left."
    "She mentions something about how it sometimes feels as if they're fading away, but I have a hard time relating on account of...well, knowing literally {i}nothing{/i} about my parents."
    "Either way, it’s surprising how unfazed she seems in the face of that. But I guess that as long as they’re sending her money, everything will be fine."

    if bonus == True:
        "Some people cherish that level of independence, especially at her age. And Futaba is no exception."
        "I just hope that this part of her doesn't change any time soon."
        "Because, despite what I frequently tell her, I have no idea if I'll always be there for her or not."
        "And being all alone in this world doesn't seem like it would be very fun."
    else:
        "Though, I guess it is kind of weird how her parents are still giving her money even though she's in college."
        "Either way, I'm glad that I learned a little more about her today..."

    $ renpy.end_replay()
    $ library20 = True
    $ futaba_love += 1
    stop music fadeout 3.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label library25:
    scene black
    with dissolve2

    "I decide to spend the morning at the library."

    if bonus == True:
        "Futaba and I haven't done anything exciting together lately, so I’m thinking it might be time to amp things up a bit."
        "Or at least as much as a person like me {i}can{/i} ‘amp things up.’"
        "It’s clear that she’s fond of me. That much I’ve known since the beginning."
        "But if you told me months ago that I’d somehow start developing ‘feelings’ for her, I’d have called you insane."
        "I’m not meant to become attached to anyone."
        "That’s not why I’m here."
        "But there’s something about receiving constant, undeserved affection from someone that sort of flips a switch inside of your head."
        "It makes you think you actually {i}do{/i} deserve it."
        "I wonder if that’s what’s happening to me?"
        "That must be what's happening to me."
    else:
        "Probably because I love reading so much and want to absorb more knowledge so I can become a better teacher."

    "........."
    "......"
    "..."

    scene morningmoon1
    with dissolve2
    play music "gentle.mp3"

    s "..."
    f "..."

    "Sunlight permeates the air of the library, illuminating scattered dust particles trying to sneak their way into my eyes."
    "Amidst my partially-obscured vision stands Futaba Fukuyama, volunteer librarian and full-time student, engrossed in a book I can’t make out from here."
    "I imagine it’s a happy one."
    "Maybe something with dragons or princesses."
    "Something to help distract her from how horrible life really is and how, on average, we consume over fifty pounds of these same dust particles every year."
    "She might not be thinking about that last part, but I am."
    "Anyway, life isn't horrible for her and her alone. It's like that for all of us."
    "And no one who is truly happy with their life spends this much time reading."
    "Reading is an escape mechanism. And if you love where you are, or {i}who{/i} you are-"
    "Well...what is there to escape from?"
    "I imagine you want me to shut up right about now, correct?"
    "Well, I’m sorry, but I won’t."
    "I am here to remind you of how horrible all of this is."
    "Let my words be a floor of daggers, cutting into your feet with every step you take."

    scene morningmoon2
    with dissolve2

    f "Oh, Sensei! I didn’t see you walk in."
    f "How are you this morning?"
    s "I’m pretty good. What are you reading?"
    f "Huh? Oh, just some book about...umm..."

    scene morningmoon3
    with dissolve

    f "Umm..."

    "She looks away in an attempt to escape from her escape mechanism."

    f "I guess it's about...dragons...and stuff...hahah..."

    "Princesses too, I imagine."

    scene morningmoon2
    with dissolve

    f "Things have been pretty slow around here lately, so I was reorganizing the fantasy section."
    f "But...then I came across a book I used to read when I was little and..."

    scene morningmoon3
    with dissolve

    f "Well, one thing kind of led to another..."

    scene morningmoon2
    with dissolve

    f "Did you read a lot when you were younger, Sensei?"
    s "Me?"
    s "Uhh...I-"
    f "..."
    s "..."
    f "Sensei?"
    s "Sorry. I just feel like there's something I want to say here, but I can't quite put my finger on it..."
    f "You...um..."

    scene morningmoon3
    with dissolve

    f "I'm...also having a hard time finding the words I want to say, but...I imagine someone as talented as you read quite a lot when you were a child."
    s "Maybe I did. Maybe I didn't. There's no way to know for sure."
    f "No, I suppose there isn't..."

    scene morningmoon2
    with dissolve

    f "But I don't think it was luck alone that got you here, Sensei."
    f "And I think that...it isn't entirely a bad thing to just...{i}make up{/i} memories if you can't find ones you enjoy on your own."
    s "That's a...relatively uncharacteristic thing for you to say, Futaba."

    scene morningmoon4
    with dissolve

    f "Is it? How so?"
    s "You've just always struck me as the more...honest type."
    f "I don't think what I suggested was dishonest. I see it as...just one more form of creativity?"

    scene morningmoon2
    with dissolve

    f "Like...writing a book! Just the book is {i}you.{/i} And it's highly probable that you just...filled in the pages out of order and have to...go back and make some corrections?"
    s "Nice try. But I'm sure that whatever I have to say about my reading habits as a child isn't anywhere near that...dramatic or serious."
    s "I'm pretty positive I was just a normal person who did normal shit and is now going to work a normal job until he dies."
    f "I think you're amazing, Sensei. I-"
    s "I didn't come here to talk about myself, Futaba. Tell me about what you want to do instead."

    scene morningmoon5
    with dissolve

    f "Oh...I'm...Okay, sure!"
    f "I still don’t...really know what I want to do when I'm done with school..."
    f "But it's probably a safe bet to assume it’ll be something involving books."

    scene morningmoon3
    with dissolve

    f "Maybe I can get a job at a publishing company or...open a book store?"
    f "Would you come visit me if I owned a book store, Sensei?"
    s "Of course. I already come visit you at the library all the time."
    s "Might be nice to get a discount on stuff too. Maybe I'd actually pick up a book for the first time in...well, as long as I can remember."
    f "Everything here is free...isn’t that the biggest discount there is?"
    s "Yeah, but I need to give everything back and that's no fun."

    scene morningmoon6
    with dissolve

    f "Well...you never take anything out in the first place, so..."
    s "That’s just because I’m kind enough to leave the books for people who need them more than me."
    f "How awfully considerate of you..."

    scene morningmoon2
    with dissolve

    f "But, I guess I understand. Book stores are much more fun than libraries."
    f "It’s nice owning the things you care about."
    f "The value of something that’s already been used by someone else is always a little worse, isn’t it?"
    s "Yeah...something like that."

    scene morningmoon7
    with dissolve

    f "Th...That being said..."
    f "I'm glad you showed up today, because..."
    f "Well, there’s actually something I’ve been meaning to ask you for a little while now, but I’m kind of nervous so..."
    f "I’m not really sure if {i}right now{/i} is the best time or...if I'll even be able to follow through with it..."
    s "Is this a confession?"

    scene morningmoon8
    with dissolve

    f "Keh-!"

    "Looks like I might have hit the nail on the head."

    scene morningmoon9
    with dissolve

    f "That's...That’s not it! That comes later!"
    s "So...it {i}is{/i} coming then?"
    f "I...never said that!"
    s "It was {i}very{/i} heavily implied. Besides, do you really think I don’t know by now?"
    s "I’m not some dense harem protagonist- I’m the other kind. The kind that's suspiciously successful with girls despite putting in virtually no effort whatsoever."
    f "That sort of character is entirely unrealistic, Sensei."
    s "Exactly. Nothing is real, Futaba."
    f "Nothing is...real?"
    s "Not you, not me..."
    s "Nothing."

    scene morningmoon4
    with dissolve

    f "That's...an interesting philosophy."
    s "I'm sure there's more to it, but I didn't really have any idea where I was going with it."
    s "Just in a weird mood today, I guess."

    scene morningmoon5
    with dissolve

    f "Well, I'm glad your weird mood landed you here..."
    f "Because what I've been meaning to ask you involves...umm...a yes or a no...And I'd like to know soon so I can stop agonizing over your answer."
    s "But...it's {i}not{/i} a confession?"
    f "It's not a confession."
    s "Because that made it sound a lot like a confession."

    scene morningmoon9
    with dissolve

    f "Stop calling it that! My heart can't take it!"

    scene morningmoon3
    with dissolve

    if bonus == True:
        f "I’d understand if you don’t want to do it since I’m kind of...you know...a {i}little{/i} bit younger than someone you’d want to spend time with outside of school."
        s "I think I’ve made it overwhelmingly clear that our age gap makes zero difference to me."
    else:
        s "If it's about how many spiders human beings consume in their sleep every year, I really don't want to hear it. I think I've made my distate for factoids like that clear enough by now, haven't I?"

    f "This is a little...different, though."
    f "Almost everything we've done has been here...or the dorms...We've barely been to any places where we'd seem...{i}out of{/i} place."
    f "And I'm comfortable with you everywhere, but..."

    scene morningmoon5
    with dissolve

    f "That doesn’t mean it’s not a little nerve-wracking when I think about going somewhere else."
    f "I li-...I really respect you as a person and a teacher and I’m worried that you’ll maybe..."

    scene morningmoon3
    with dissolve

    f "I don’t know...get bored of me or something?..."
    f "It’s hard to explain."
    s "Then don’t explain it. Just ask whatever you want to ask me and we’ll take it from there."
    s "It’s probably just about accompanying you to a new book store or something along those lines, right?"

    scene morningmoon8
    with dissolve

    f "Keh-!"

    "Second nail hit. This fence will be built in no time at all."

    f "H-H-How did you-"
    s "It's the next logical step, isn't it? Something with the potential to pull the two of us closer together."
    s "If we don't start doing things like that, everything will just...stagnate."

    scene morningmoon4
    with dissolve

    f "Stagnate? How so?"
    s "You know that fake Einstein quote about how doing the same thing over and over again is the definition of insanity? Well, that applies to relationships too."
    s "We can't just confine our time together to school or the dorm. Fake Einstein would hate that."
    s "So, if going out there and doing new things together is how we're supposed to keep this alive, sure. I see no problem with that."
    f "Is that really what you think?"

    scene morningmoon7
    with dissolve

    s "Is {i}what{/i} really what I think? I said a lot just now."
    f "That we'll...fizzle out if we don't open up a little more."
    f "Because all this time, I was worried that the exact opposite would be the biggest issue for you."
    s "The world is big, even if the majority of it is closed off to us."
    s "But that doesn't mean we should trap ourselves in an even smaller box because we're afraid of what might be outside."
    f "So..."

    scene morningmoon2
    with dissolve

    f "Wait, does that mean you’ll come?"
    s "..."
    f "..."
    s "Of course. It would be pure evil if I were to build this up like that and then say no."

    scene morningmoon10
    with dissolve

    f "Hahaha! It really would!"
    f "But I never really know with you and...and..."

    scene morningmoon10r
    with dissolve

    f "You...have no idea how excited this makes me, Sensei..."
    f "I didn’t think...you’d ever want to go on a date with someone like me..."

    "To be fair, I never said it was a {i}date{/i}...But I guess that was heavily implied as well."
    "And it's not like I mind. Futaba can probably pass as a college student if the two of us go out together anyway."
    "Plus, if it can get her to smile like that, she can ask me on as many {i}dates{/i} as she wants."

    s "I guess you were wrong, then. But let me ask you this...why aren't {i}you{/i} weirded out by the idea of being seen with me?"
    s "If people {i}do{/i} see us together, they might assume all types of things."

    scene morningmoon10r2
    with dissolve

    f "And...they would probably be right about half of them."
    s "Fair point."

    scene morningmoon2
    with dissolve

    f "Besides, I love the idea of being seen with someone like you!"
    f "I feel like any time I go anywhere, it's with either Rin or one of my friends from my old school...and you're so much...well...{i}cooler{/i} than them."
    s "Don't let Rin hear that. She'll probably cry."

    scene morningmoon10
    with dissolve

    f "Heheh...probably..."
    s "Can I ask you one more question before I head out, Futaba?"

    scene morningmoon2
    with dissolve

    f "Of course, Sensei! Ask anything you-"

    if bonus == True:
        s "Are you absolutely positive you're not asking me out because you’re actually in love with me? Because now would be a good time to just admit it already."
    else:
        s "You’re positive it’s not because you want another hug?"

    scene morningmoon8
    with dissolve

    f "Keh-!"

    "Third nail. Fence complete."

    scene black
    with dissolve2

    "Futaba and I make plans to meet at her dorm room sometime over the
    weekend and she goes over where the store is located."
    "Apparently, it’s not all that far from here and is open relatively late, so we should be
    able to head over at night."
    "It’s strange going on a nighttime ‘date’ to a book store, but I guess it is what it is."
    "I’m just glad that I’ll be getting to spend more time with her."
    "And that, for some strange reason...she continues to give me things I do not deserve."

    $ renpy.end_replay()
    $ bookdate = True
    $ futaba_love += 1
    $ library25 = True
    stop music fadeout 6.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label library30:
    scene nodokafirst1
    with dissolve
    play music "morningmoon.mp3"

    "I walk into the library first thing in the morning to be greeted by a rather unusual sight."
    "And by unusual I mean a sight I have literally never seen before."
    "Typically, Futaba will spend her mornings rearranging books or...picking up books, or..."
    "Well, you get the point."
    "There are a lot of books involved."
    "It’s not often she actually engages with anyone other than me."
    "Is this girl planning on stealing Futaba away from me?"

    s "Who are you and what do you want with my librarian?"
    lt "{i}Your{/i} librarian? Futaba didn’t tell me the two of you were in that sort of relationship."
    lt "Sincerest apologies for what I am about to tell you, but this {i}librarian{/i} has been my property for several years now."
    lt "I’m willing to share her as long as you go through the proper request process. There are several caveats, however."

    scene nodokafirst2
    with dissolve

    lt "No touching, no teasing, no flirting, no talking, no exchanging of gifts (Including those sexual in nature), no staring and, most importantly-"

    scene nodokafirst3
    with dissolve

    lt "No-doka."
    s "I have no idea what that last one even means."
    no "It’s my name. Nodoka Nagasawa, a friend of Futaba’s from another[school]."

    if bonus == True:
        no "I’ve seen her exposed breasts more times than you."
    else:
        no "I can eat more spaghetti than you."

    "I wouldn’t be so sure about that..."

    scene nodokafirst4
    with dissolve

    f "Nodoka was in town on a...business trip, I guess?"
    f "She decided to stop by before heading back to the outer-barrier."
    s "Business trip? How old are you?"

    if bonus == True:
        no "Old enough. You need not concern yourself in my private ordeals."
        s "..."
        no "..."
        s "You’re not some sort of prostitute, are you?"
        no "Not that I am aware of."
        no "Are you the type to hire those sorts of people? If so, would you mind if I asked you some questions?"
    else:
        no "Well, obviously I am in college. Japanese women are just petite by nature."
        s "You are right. I apologize for assuming that was not the case. I just haven't heard much about you from Futaba as of yet, but I am excited to see where your story leads."
        no "Say, do you know anything about genome mapping?"

    no "It’s for research, I swear."
    s "Right. {i}Research{/i}."
    f "No, it really is for research, Sensei. "
    f "Nodoka is a writer and tends to dive into rather...unsightly topics at times."

    if bonus == True:
        no "My favorite is [incest]. It’s truly fascinating in fictional settings. Wouldn’t you agree?"
        s "Futaba is literally in the same class as my [niece]. I’m not going to share my opinion of [incest] with you. Fictional or not. "
    else:
        no "I don't know if I'd call genome mapping unsightly, but I do my best."
        s "..."

    scene nodokafirst5
    with dissolve

    no "Your lack of a response is the only response I need! Thank you very much!"

    if bonus == True:
        "What a strange character..."
    else:
        "Wow, she must be a real genius if that was the only research she needed."

    s "Anyway, were you planning on hanging out with your friend today, Futaba?"
    s "If so, I can just leave you two to it and go figure something else out."

    scene nodokafirst4
    with dissolve

    no "No need. I need to be heading out anyway."
    no "I just wanted to drop by and see if Futaba’s grown anymore since the last time I saw her several weeks ago."

    if bonus == True:
        no "She refused to take her shirt off in the library, though, so I don’t think I’ll be getting an answer today."
    else:
        no "Fortunately, she appears to be the exact same height."

    scene nodokafirst6
    with dissolve

    f "You never change, do you?"
    no "Why would I? I’m perfect the way I am. Just like you’re perfect the way you are."
    f "Well, thanks Nodoka. I’m glad to hear-"
    no "Let’s get married. "
    f "...No."
    no "Damn it. You’ll agree to that one day."
    f "I really won’t..."

    scene nodokafirst7
    with dissolve

    if bonus == True:
        no "You there. Glasses-companion. Let me know if you can figure out Futaba's latest cup-size."
    else:
        no "You there. Glasses-companion. Let me know if you can figure out how many clouds there are."
        s "Like...total? Doesn't the amount change?"
        no "Beats me."

    s "Is that for research as well?"
    no "No. It’s for my own personal records."
    s "I see. That’s good enough for me. I’ll have Futaba send you a message once I find out."
    f "Why are you agreeing to this? And why do I have to be the one to send the message?"
    no "Because I don’t give my number to strangers."

    scene nodokafirst8
    with dissolve

    no "But anyway, thanks for letting me visit for a little bit."
    no "This library is much smaller than the one I’m used to, but it’s cute. It’s got a sort of...rustic charm to it."
    no "Maybe I’ll come back one day?"

    scene nodokafirst9
    with dissolve

    no "Sayonara, Futaba! And you as well, mystery-man!"
    s "My name is Sensei."
    no "No it isn’t!"

    "Nodoka exits the library and leaves Futaba and I sitting there in silence for a little while."

    f "So anyway, that’s Nodoka."
    s "She seems...fun."
    f "She’s a lot. "

    scene nodokafirst10
    with dissolve

    f "She’s one of the smartest people I know, though. You should read some of her work if you ever get the chance."
    s "Where would I find it? Is she online or something?"
    f "I can...umm...maybe send you a few links?"
    s "Do you have my number? Or email address or anything?"

    scene nodokafirst11
    with dissolve

    f "Well, no...But if you wanted to maybe...give it to me or something...that would be okay."
    f "That’s not too weird to say, right?"
    f "I promise I’d only text you if I need something or...have to give you something."
    s "You can text me whenever you want. I don’t care."

    scene nodokafirst12
    with dissolve

    f "Really?! You mean it?!"

    scene nodokafirst13
    with dissolve

    f "Oh! Umm. Sorry. I didn’t expect to react that way."
    f "I don’t know what came over me."
    s "It’s fine. Don’t worry about it."

    "I take my phone and slide it across the table, giving Futaba the go-ahead to enter her contact info."
    "She nervously does so and, before long, both of our phones are back in our respective pockets."

    $ futabanumber = True

    "{i}Congratulations! You now have Futaba’s phone number!{/i}"

    s "So, now that your friend is gone and the two of us are alone, there’s been something I’ve been meaning to ask you."

    scene nodokafirst14
    with dissolve

    if bonus == True:
        f "Umm...it’s nothing...you know...{i}sexual{/i}, is it?"
        f "I’ve accepted that we have that type of relationship now but I still don’t know if I’m comfortable...you know, {i}helping{/i} you out in the library."
        f "There are people around and-"
    else:
        f "I don't know how many clouds there are, Sensei..."

    s "I was actually just going to ask if everything was okay."
    f "..."

    scene nodokafirst15
    with dissolve

    f "Huh?"
    f "What do you mean?"
    s "I mean that we haven’t really talked about what randomly sent you home from the beach."
    s "Molly was pretty upset that you weren’t able to play that game with everyone, and that seemed like something you’d be really into."
    f "..."
    s "..."
    f "..."
    s "..."

    scene nodokafirst16
    with dissolve

    if bonus == True:
        f "On second thought, maybe I could...give you a handjob...under the table or something..."
        s "As much as I love under-the-table handjobs, it sounds to me like you’re trying to hide something."
    else:
        f "On second thought, maybe I do know how many clouds there are."
        s "You bitch."

    scene nodokafirst17
    with dissolve

    if bonus == False:
        s "Apart from that, though, it seems like you're hiding something."
        f "I'm not hiding anything..."
    else:
        f "I’m not hiding anything...I just want to...give you a...h-handjob..."

    s "That doesn’t sound very confident, Futaba."
    f "Why would you even want to know that? I look fine now, don’t I?"

    "I hadn’t noticed before, but now that I’m paying closer attention, Futaba does look a little bit...off."
    "I can’t really pinpoint exactly what’s wrong, but something’s different."
    "And no, I’m not talking about her hair being down. It’s something more than that."

    s "I want to know because I care about you."

    scene nodokafirst18
    with dissolve

    f "S-Sensei...You can’t just come out and say that all of a sudden...it’s embarrassing."
    f "There are people around. Someone might hear you."
    s "What’s so bad about people hearing that I care for one of my students? I care about all of you."
    f "It’s just...someone might get the wrong idea."
    s "Well that’s on them, then. But don’t worry about other people right now."
    s "If something is bugging you, it’s okay to tell me."

    scene nodokafirst19
    with dissolve

    f "Th-thanks...but I’m pretty sure I’d rather keep this thing to myself if that’s okay."
    f "It’s not like...a really big deal or anything. It would only create more problems for you."

    scene nodokafirst20
    with dissolve

    f "But I’ll be better for it in the long run. Just worry about yourself and let me deal with my issues on my own."
    s "...It’s not about Yumi, is it?"
    f "It’s not. She actually hasn’t even said anything to me since the beach."

    "Huh...if Yumi’s not the source of her problems this time, I wonder what is?"
    "I know her family lives overseas so...maybe it’s something that has to do with them?"
    "Either way, it doesn’t look like she’s willing to reveal whatever’s going on right now, so I should probably just talk about something else."

    s "So, Nodoka."

    scene nodokafirst21
    with dissolve

    f "Yes, Nodoka."
    f "She’s cute, isn’t she?"

    if bonus == True:
        s "If there’s anything I’ve learned about girls that I’m {i}involved{/i} with it’s to never talk about how cute other girls are around them."
        f "I don’t see a problem with you thinking she’s cute. {i}I{/i} think she’s cute and I’m not planning on leaving you for her."
        f "Though, I think she'd be quite happy if I did."
        s "If you do decide to do that, please let me know in advance so I can buy a video camera."
    else:
        s "I think she might be in love with you."

    scene nodokafirst22
    with dissolve

    f "Please stay out of my first lesbian relationship. You and I are no longer together."

    if bonus == False:
        s "Wait, when were we ever together?"

    f "What we had was fun, but it was as fleeting as a summer breeze."
    f "You were just an old tooth that happened to be pushed out by a new one."
    s "That first metaphor was a little stronger than the tooth one."

    scene nodokafirst23
    with dissolve

    f "We can’t all be Nodokas, you know? I’m doing my best."
    s "That’s right. You are doing your best. And that’s really all that matters."

    scene nodokafirst15
    with dissolve

    f "Hm? Why are you getting serious all of a sudden?"
    s "I didn’t mean to. It just kind of slipped out, I guess."
    s "Maybe I’m subconsciously worried about you since you’re keeping your first ever secret from me."

    scene nodokafirst10
    with dissolve

    f "Who said this is the first?"
    f "Either way, I think you should {i}subconsciously{/i} stop because it’s harder for me to smile when you’re not smiling."
    f "And yes, I know that line probably needed some work as well."
    s "It was better than the tooth one at least. That one still hits me the wrong way for some reason."
    f "Yes, yes. I know it was bad. I won’t talk about teeth anymore."
    s "I appreciate that."

    "I pull my phone out of my pocket and check the time to find that it’s getting close to lunch."
    "Since the two of us don’t seem to have anything else going on, maybe Futaba will want to come out for a little bit?"
    "No harm in asking, I guess."

    s "Hey, are you doing anything after this?"

    scene nodokafirst15
    with dissolve

    f "Like, after the library? Not really. Why?"
    s "Did you want to come get lunch or something? I’m probably going to head out soon."

    scene nodokafirst21
    with dissolve

    f "That does sound fun, but I need to stay here for pretty much the entire day today."
    f "Thank you for inviting me, though. It makes me happy to hear that...you want to spend more time with me and stuff..."
    s "You have to spend the whole day here? Aren’t you a volunteer?"
    f "I am, but that doesn’t mean I can just leave whenever I want."

    scene nodokafirst24
    with dissolve

    f "I have a responsibility and I can’t walk away from it. That’s what it means to be an adult."
    f "But of course you wouldn’t know that since you’ve given up on teaching and just want to hang out with everybody instead."
    s "Don’t question my methods. Your grades are better than ever."

    scene nodokafirst25
    with dissolve

    f "Grades? We have grades?"
    f "I thought we were just messing around."
    s "We were, but I’m giving you an F now for losing faith in my patented system."

    scene nodokafirst13
    with dissolve

    f "An F?! You can’t do that! I thought we were just joking!"

    scene black
    with dissolve

    "Little does Futaba know, I’m the most serious man in the world."
    "I never joke about anything."
    "Just kidding."
    "But either way, I’m significantly less willing to spend my entire day wasting away in a library than Futaba is."
    "Who cares about responsibility when there are more important, more fulfilling things to be doing?"
    "I offer to buy Futaba something and bring it over in order to make her double-volunteer-shift a bit more bearable, but she shrugs off my act of generosity and tells me she brought something with her."
    "What a bitch."
    "Just kidding again."
    "Not knowing what else to do, I stop at a nearby burger joint and grab a quick lunch before getting on with my day..."

    $ renpy.end_replay()
    $ library30 = True
    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label library35:
    scene futabarinlib1
    with dissolve
    play music "morningmoon.mp3"

    "I walk into the library to find Futaba and Rin caught in a conversation amidst an otherwise empty room."
    "The two of them don’t notice my presence right away so I decide to eavesdrop on their conversation and listen into whatever juicy stuff girls talk about when they’re alone."

    r "Yeah so I basically just kept rolling 5’s the entire night."
    r "I’m thinking of buying new dice, but I can’t figure out which color I want."
    f "I have an extra pair I could give you. I don’t really have a use for two sets and it’s not like I’m going to switch back and forth mid-game or anything."

    "Okay, this conversation is boring. It’s time for me to step in."

    scene futabarinlib2
    with dissolve

    s "Aren’t girls supposed to talk about fun stuff while there aren’t any guys around?"
    r "What do you mean? D&D is tons of fun. Don’t complain just cause you’re a buzzkill."
    s "What are you even doing here? Don’t you have work today?"
    f "Rin took the day off and is going to hang out with me here."

    scene futabarinlib3
    with dissolve

    r "Of course I took the day off. You’re always there to help me out, so who would I be to not be around for you?"
    s "First Nodoka and now Rin. People seem to be flocking to you all of a sudden, Futaba."

    scene futabarinlib4
    with dissolve

    f "It really does seem that way. All I did was let my hair down. "
    f "I had no idea it would make this much of a difference."
    s "Is that just how you’re going to keep it from now on?"
    f "I don’t know...I do like all of the attention I’m getting all of a sudden."
    f "Even if that attention is really only from you two and Nodoka."
    r "Sooo Sensei finally met Nodoka. Any thoughts? Love at first sight?"
    s "Why would I fall in love with her at first sight?"
    r "Because you both wear glasses and...write stuff?"
    s "Makoto and I both wear glasses and write stuff as well."

    scene futabarinlib5
    with dissolve

    r "Oh my God, are you in love with Makoto?!"
    r "I knew something fishy was going on with you two!"
    s "Shh, quiet. She’ll hear you."
    f "She {i}is{/i} rather fond of you..."
    f "I personally wouldn’t be surprised if, well, you know..."
    s "Okay, well let’s not drag her into this and make things any more complicated than they need to be."
    s "Rin."

    scene futabarinlib6
    with dissolve

    r "Me."
    s "You said something about being there for Futaba when she’s always there for you."
    r "I did."
    s "What does that mean?"
    r "It’s cause she hasn’t been feeling well. I thought you knew that?"
    f "Umm...I’m...right here..."
    f "I’d appreciate it if you two wouldn’t talk about me like I’m not..."
    s "I did, but I still don’t know exactly what is wrong."

    scene futabarinlib7
    with dissolve

    r "It’s...a fever. Right?"
    r "I've told her over and over to hold off on working until it breaks, but she seems weirdly adamant about still coming despite having to spend literally the whole day here."

    scene futabarinlib8
    with dissolve

    f "Well...it’s the only time I really get to see you and...you know. Books. And stuff."
    s "As much as I appreciate being next to books in your top interests, it would mean a lot to me if you’d put yourself first for once."
    r "For real. We have books in our dorm. The[school] will understand if you’re not feeling well."

    scene futabarinlib9
    with dissolve

    f "Can we not do this right now?"
    f "It’s not like working in the library is physically exhausting. I just need to stand around and...make sure I enter the returns into the computer."
    r "No one’s even here, though. Can't you just-"

    scene futabarinlib10
    stop music

    f "Just fucking drop it, okay?! "
    f "I appreciate that you’re looking out for me, but I’m fine!"

    "I guess it’s good that no one else is around today as Futaba would clearly be making a scene if anyone was."
    "I think this might be the first time I’ve ever heard her raise her voice and it’s...strange."
    "I can’t say I like it. "
    "Something’s definitely going on with her."
    "And if Rin nor myself is able to get it out, I’m beginning to worry that we really might just have to let her deal with it on her own."
    "I suppose that’s fine, though."
    "I’ve always believed that solving things on your own is the best way to become stronger."
    "And while I’ve definitely been trying to help her to a certain extent, it’s impossible to deny that most of this has been due to my own curiosity rather than a need to make her feel better."

    r "Woah..."
    r "I’m..."

    scene futabarinlib11
    with dissolve
    play music "beyondthewayoftime.mp3" fadein 5.0

    f "Oh- no! {i}I’m{/i} sorry! "
    f "I didn’t mean to yell at you like that. I’ve just been under a lot of stress lately and..."
    f "And I wish you two wouldn’t keep trying to get involved."
    f "It’s nice but it really is just making things...a little harder for me."
    s "We just want you to know that we’re here for you."

    scene futabarinlib12
    with dissolve

    f "I get that...but what help does it do to just keep saying you’re there for someone over and over and over?"
    f "I obviously know that you’re there for me and I’m glad you are...but if I wanted your help, I would have accepted it by now."

    scene futabarinlib13
    with dissolve

    f "With my parents traveling as much as they have my whole life, I’ve never really had anyone to {i}care{/i} for me during times like this."
    f "Until Rin, that is."
    r "Don’t."

    scene futabarinlib14
    with dissolve

    f "Huh?"
    r "Don’t say anything about how you need to deal with certain things on your own."
    r "That’s where you were going, wasn’t it?"
    r "{i}Until I met Rin, I was always alone. But she can’t fix everything.{/i} Blah blah blah independence and responsibility or whatever. Get real."
    r "I wouldn’t be so worried about you if you would actually start taking care of yourself."

    scene futabarinlib15
    with dissolve

    f "Are you saying...I can’t take care of myself?"
    r "No, I’m saying you {i}won’t{/i} take care of yourself. It’s different."
    r "You’re perfectly capable of doing it and you still choose not to."
    r "Then you get all mad when the people who are closest to you start to notice something is going on."
    s "Okay, I’m beginning to think Rin knows a little more about what’s {i}going on{/i} than I do."
    f "I’m beginning to think that, too. And I’d appreciate it if she and I could talk about it {i}alone{/i}, Sensei..."

    scene futabarinlib16
    with dissolve

    r "I want him here."
    r "He’s important to me."
    r "And he’s important to you too."

    "I can’t help but feel like I’ve somehow gotten wrapped up in a rare dispute between best friends when all I wanted to do was hang out with Futaba."
    "But obviously, these are [teenager]s we’re dealing with. Things like this are bound to happen and I should never believe otherwise."
    "This is still Futaba’s call, though. If she doesn’t want me here, I shouldn’t be here."
    "She and Rin can talk about this and I’ll just...avoid confrontation and pick up where we left off once the matter is resolved."

    s "Thanks, Rin. But I’ll step away for a little while and let the two of you talk."
    s "If Futaba wants to keep something secret, she shouldn’t be obligated to share it."

    scene futabarinlib17
    with dissolve

    r "Even if it’s dangerous?..."
    s "It’s still up to her to decide."
    s "I’ll be back in a few minutes."
    r "..."
    f "..."

    scene black
    with dissolve

    "I quietly make my way out of the library and lean up against the wall."
    "No one is around, so it doesn’t look like the two of them will be interrupted any time soon."
    "But, in the event that someone {i}does{/i} show up, I can probably just use my teacher-powers to tell them the library is closed or something."
    "........."
    "......"
    "..."
    "{i}Meanwhile...{/i}"

    scene futabarinlib18
    with dissolve

    r "Futaba..."
    f "What?"
    r "I love you."
    r "Soooooo ‘effing much."
    r "But you need. To. Stop. This."
    r "It’s dangerous."
    f "Stop what, Rin?"
    f "What are you saying?"
    r "You’re really going to make me say it?"
    f "You didn't have any problems making {i}me{/i} say it when I found out you were cutting yourself. So, yeah. I am."
    r "Fine, then. I'll say it."

    scene futabarinlib19
    with dissolve

    r "When was the last time you ate anything?"
    f "Yester-"
    r "{i}Without{/i} fucking...throwing it up right away."
    f "..."
    r "I know that's what's going on..."
    r "You did the same fucking thing in middle[school]."
    r "You don’t want Sensei to know because it’s embarrassing, right?"
    r "You know he’ll just say something about how he thinks you’re beautiful no matter what. "
    r "But you don't think that."
    r "And no compliments mean {i}anything{/i} if you don’t think that...Right?"
    r "It’s just like how I have to lean on hurting myself to feel better sometimes."
    r "I get it. I really do."
    f "..."
    r "Say something."
    f "You don’t get it. It’s not the same thing."
    f "You don’t have actual {i}reasons{/i} to feel the way you do. You’ve said it yourself a million times."
    f "It just happens..."

    scene futabarinlib20
    with dissolve

    f "Rin..."
    f "I love you too. More than anyone."
    f "All I’m doing is trying to feel a little better about myself."
    f "And it’s been working! I’ve...lost a few pounds ever since the beach and...And I’ve even started wearing my hair differently."
    f "I'm reinventing myself!"
    f "Things are getting better!"
    f "I’ll go back to normal soon."
    f "I just want to be a little happier first."
    r "Things like this don’t make you happier! They make it worse! You're literally destroying your body."
    f "Good. This body deserves to be destroyed."
    f "And besides, isn't this the pot calling the kettle black right now?"

    scene futabarinlib21
    with dissolve

    r "Fuck the pot and fuck the kettle!"
    r "This is your best-friend...your {i}sister{/i} begging you to stop killing yourself because you don't like how you look!"
    r "We can go to the gym together! I’ll go on a diet with you! I’ll do whatever you want!"
    r "Just cut it out already!"
    f "Rin..."
    r "I mean it! I’m not kidding!"
    f "..."
    r "..."

    scene futabarinlib22
    with dissolve

    f "You’re..."
    f "You're not going to tell him...are you?"
    r "Of course not! "
    r "We would have wound up in this same conversation today whether he was here or not."
    r "He doesn’t have anything to do with this."
    r "I’m so fucking worried about you. So worried I couldn’t even work."
    r "I get that you’re unhappy, but we can start fixing that together! Just like last time!"
    r "Please...for me."

    scene futabarinlib23
    with dissolve

    f "..."
    r "..."
    f "I’ll try."
    f "For you."
    f "But that's all I can promise."
    f "I don't know if it will work or not."
    f "But I'll try."
    r "I love you so much."
    r "Thank you."
    f "I love you too."
    f "Thank {i}you{/i}."
    f "Even if you’re annoying and won’t let me do things my way."
    r "You never let me do things my way either. This is just me returning the favor."
    f "Hehe...I guess you’re right."
    f "Should we...maybe tell Sensei it’s okay for him to come back in yet?"

    scene futabarinlib24
    with dissolve

    r "Umm...hold on one sec."
    r "My mascara isn’t running down my face right now, is it?"
    r "Don’t want to give away that I was crying or anything."

    scene futabarinlib25
    with dissolve

    f "You look fine..."
    f "More than fine."
    f "You’re beautiful."
    r "No, {i}you’re{/i} beautiful."
    f "No, you."
    r "No, {i}you.{/i}"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play sound "slidedoor.mp3"

    r "Excuse me, is there a teacher available to assist two [young_girls] in the library?"
    r "There are so many hard-to-reach books and our tiny arms simply can not reach any! Whatever shall we do?"
    s "I am a teacher. I can obtain hard-to-reach books."
    r "Wonderful! Come quick!"

    scene futabarinlib26
    with dissolve
    play sound "slidedoor.mp3"

    s "Hey. Glad to see you two didn’t kill each other."
    s "I was worried that Rin needed help burying a body or something just now."
    f "Nope. No bodies to be buried just yet. "
    f "We’re fine now. Thanks for stepping out and letting us talk alone."
    s "Hey, it’s not my responsibility to solve every problem. Some things are better fixed by others."
    s "I’m just here to hang out with [teenage]girls."
    f "Well you get two of them today, so be happy about that while you still can."
    s "Oh, I will be. Don’t worry."

    scene black
    with dissolve2

    "The rest of the morning goes by rather quickly."
    "Futaba remains pretty lethargic throughout, but I chalk it up to whatever mystery-ailment is plaguing her as she seems in good spirits otherwise."
    "I’m not sure what the two of them said to each other to defuse the situation so quickly but, whatever it was, I’m glad. "
    "I didn’t particularly like seeing angry-Futaba, and I’m perfectly content with never having to see that again, if at all possible."

    $ renpy.end_replay()
    $ library35 = True
    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label futabainvite1:
    play sound "phonebeep.wav"

    "I tap on Futaba’s name in my phone and wait for her to answer."
    "This will be the first time I’ve ever tried inviting her over to the house and, if there’s anything I know about that girl by now, I’m pretty sure I’m about to give her a minor heart attack."

    if bonus == True:
        "But hey, if things are ever going to progress to the point where we can actually have sex, events like this are going to need to happen."
    else:
        "But hey, Futaba is part of my official hug club, so events like this are going to need to happen."

    "Plus, having to deal with a possessive and jealous redhead might be a good exercise in self-control and confidence for her."
    "All of us have something to gain out of this."
    "A notch in the belt for me, a new outlook on life for Futaba, and a new rival for Ami."
    "Everyone wins."
    "Except Ami, I guess."
    "But she loses virtually every time I invite someone new over."
    "Sorry, Ami."

    play sound "phonebeep.wav"

    f "Hello? [futabamaster]?"
    f "How are you doing?"
    s "I’m doing fine. Are you busy today?"
    f "Today? Umm...not really. Why?"
    s "I was wondering if you’d want to hang out at my place."
    f "Y-y-your...your house?!"
    f "But...it’s...so sudden! I mean...we haven’t even-"
    f "W-wait...this is...this is to study or something, right?"
    f "Yeah, of course it’s something like that."
    f "You live with Ami and have already...decided to not really {i}teach{/i} as much lately, so..."
    f "You probably just need someone to help her with English, right?"
    f "You definitely don’t want to just {i}hang out{/i} with me, hahahaha~"
    f "Right?..."
    s "I actually did, but the studying thing sounds like a good cover story."
    f "So...wait, what am I doing?"
    f "Do I need to bring my books?"
    s "Bring whatever you want. We’ll deal with it once you get there."
    f "Wait, [futabamaster]!"

    play sound "phonebeep.wav"

    "I hang up the phone and put it back into my pocket. "
    "I guess that call went more or less how I expected it to."

    scene black
    with dissolve
    stop music fadeout 10.0

    "All that matters is that Futaba agreed to show up. "
    "And it’s not like her coming over will be as rattling for Ami as someone like Chika since the two of them are already in a club together."
    "If anything, we can just fall back on the makeshift tutor idea Futaba was smart enough to come up with-"
    "Even if the manner in which she came up with it was the direct result of her poor confidence rearing its ugly head once more."
    "........."
    "......"
    "..."

    scene futabaamistudy1
    with dissolve
    play music "normalday.mp3" fadein 4.0

    f "Wow..."
    f "I can’t believe...I’m actually here..."
    f "I mean...I’ve stopped here once or twice before to lend Ami manga but...this feels so much different..."

    if bonus == True:
        s "I wonder if any of that has to do with how I’ve seen you naked and Ami hasn’t."
    else:
        s "I wonder if any of that has to do with how many times you and I have made card houses together."

    scene futabaamistudy2
    with dissolve

    if bonus == True:
        f "Umm...I’m sorry but, if anything, Ami has probably seen me without clothes on even more than you have..."
    else:
        f "Umm...I’m sorry but...Ami was my original card house partner long before you were, Sensei..."

    s "What?"
    s "Just what the hell is the relationship between you two?"
    f "We’re both girls and share the same locker room for PE..."

    if bonus == True:
        s "Oh right. The promised land that only I am unable to enter."
        f "R-Right..."
        f "But at this rate, you’ll probably find a way to get in eventually, so...yeah."
        s "One can only hope."

        scene futabaamistudy3
        with dissolve

        f "I’ll...put in a good word for you..."
        s "And I will continue to give you straight A’s in return."
        s "Let it be known that this is not a bribe and that I would have done that anyway."
        f "Of course you would have..."
    else:
        s "What the hell does that have to do with card houses?"

    scene futabaamistudy4
    with dissolve

    f "So, umm...I don’t know how serious you were about the studying thing so...I kind of just brought all of my books..."
    s "All of them? Aren’t there like, five?"
    f "There are a lot more than five books, [futabamaster]...and I’m pretty sure you know that."
    s "School has too many subjects."
    f "Yeah...I’m starting to see why you may have given up on teaching all of a sudden..."

    play sound "dooropen.mp3"
    scene futabaamistudy5
    with dissolve

    a "Oh, Futaba. What are you doing here?"
    a "Did I forget to give back some manga or something?"
    f "No...that’s not it."
    f "Sensei just thought it might be a good idea to have someone come and help you with...one of the more than five subjects at our[school]."

    scene futabaamistudy6
    with dissolve

    a "What? Why do you suddenly care about my education?"
    s "Because I am a good [uncle]."
    a "I thought you were gonna let me just steal all of the answers from you for the next couple years."
    s "For the rest of eternity, more likely."
    f "Uhh...[high_school] doesn’t last an eternity, Sensei..."
    s "Are you sure about that, Futaba?"
    f "...Yes?"

    scene futabaamistudy7
    with dissolve

    a "So, where did you want to start? There aren’t really any subjects I’m weak at, so pretty much anywhere would be fine."
    s "What is iambic pentameter, then? Go."

    scene futabaamistudy8
    with dissolve

    if bonus == True:
        a "Huh? No one my age would have any idea what that is."
    else:
        a "Huh? I'm an accountant, not an English major. Get off my back."

    s "Take a guess."
    a "I don’t know...some kind of medical thingy used to measure...blood?"
    s "That’s not even remotely close."
    f "I mean...some iambic pentameter is kind of like a heartbeat. So if you think of blood in that regard...it’s...almost a good guess?"

    scene futabaamistudy9
    with dissolve

    a "Why do you know that? And, better question, why does {i}Sensei{/i} know that?"
    a "He can’t even remember what days we’re supposed to take the garbage out. "
    a "I’ve had to start doing it since he always forgets."
    f "It...appears in a lot of Shakespeare’s work. And it’s easier for me to pay attention in class when we go over things I’m interested in."
    f "Well...when we {i}used to{/i} go over things, I guess..."
    a "Fine then...tell me more about this stupid pentagon thingy since I’m such an {i}idiot.{/i}"
    s "Pentameter."
    a "Shut up."
    f "It’s basically...a type of rhythm you can find in a poem."
    f "It’s a pattern of stressed and unstressed syllables that are measured out in fives."
    f "And some of the ones that directly alternate sound a lot like...heartbeats."
    f "Are you...familiar with Sonnet 18, Ami?"
    a "Uhh...I don’t think so..."
    a "I don’t need to learn the other seventeen first, do I? "

    scene futabaamistudy10
    with dissolve

    f "Hahah...of course not."
    f "Just...listen to me and see if you understand."

    scene futabaamistudy11
    with dissolve

    f "Shall {b}I{/b} com{b}pare{/b} thee {b}to{/b} a {b}su{/b}mmer’s {b}day{/b}?"
    f "Thou {b}art{/b} more {b}love{/b}ly {b}and{/b} more {b}tem{/b}per{b}ate{/b}-"
    f "Do you see what’s happening? How every other syllable is emphasized?"
    a "Yeah. It does sound kinda like a heartbeat when you do it like that."
    a "You remember all that off the top of your head, though?"

    scene futabaamistudy12
    with dissolve

    f "Mhm..."
    f "I have a lot of time to go over little things like that when I’m in the library. "
    f "And when you read something so many times, it starts to stick in your head."

    scene futabaamistudy13
    with dissolve

    f "Plus...that’s the sonnet Sensei used to teach me about the pentameter when I was struggling with it."

    "It’s good to see that whoever the old Sensei was had an appreciation for Shakespeare as well."
    "This is definitely a strange coincidence, though."
    "All I did was break out an advanced term that Ami wouldn’t know and the conversation quickly evolved into something of actual importance to Futaba."

    a "Really? All he ever taught me was how he likes his eggs cooked."
    s "Futaba is my new apprentice. You're in her hands from now on."
    s "Also, please don’t tell Makoto I said that. She’ll kill me."

    scene futabaamistudy14
    with dissolve

    f "Hahaha~ Of course, Sensei..."
    f "I’m kind of worried about what she’d do to me as well if she ever heard that."
    a "Hey...what did I tell you about using the M word in this house?"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene futabaamistudy15
    with dissolve

    "Futaba, having just been declared my new apprentice, spends the evening alternating between tutoring Ami and trying to hold conversations with me."
    "It’s an incredibly normal feeling night, something I didn’t particularly expect when I decided I’d put the two of them in the same room."
    "Sure, they’re both members of the manga club and have spent many hours in the same room before-"
    "But I'm beginning to understand that some of the girls act differently when I’m around."
    "Just like how I act differently when I’m around some of them."
    "I’m glad this worked out, though."
    "Maybe Futaba can start coming here more often."

    f "Sensei, do you have any other good examples of iambic pentameter that I could give to Ami?"
    f "Things that would be easy for her to understand."
    a "I feel like I should be offended by that, but I still barely even understand what’s going on."
    s "Richard III...Winter of our discontent."

    scene futabaamistudy16
    with dissolve

    f "Ah! Another good one!"
    f "Listen closely, Ami. This one starts out like a song and then turns into a heartbeat."
    f "Think of the opening like a...short drumroll or something."
    f "{b}Now{/b} is the {b}win{/b}ter {b}of{/b} our {b}dis{/b}con{b}tent-{/b}"
    f "Made {b}glor{/b}ious {b}sum{/b}mer {b}by{/b} this {b}sun{/b} of {b}York{/b}."
    f "And {b}all{/b} the {b}clouds{/b} that {b}lour{/b}ed up{b}on{/b} our {b}house{/b}-"
    f "In {b}the{/b} deep {b}bo{/b}som {b}of{/b} the {b}o{/b}cean {b}bu{/b}ried."
    a "..."
    a "Yeah, I’m still confused. Maybe I’m just not good at poetry."
    f "There are very few people who are {i}good{/i} at poetry. But there are a lot of people who try to understand it."
    f "What I’m teaching you now is...less of a poetry lesson and more of a science lesson."
    f "It’s the science of what makes things sound the way they do. "
    f "Kind of like...how pop music is created for the sole purpose of getting stuck in your head."

    scene futabaamistudy18
    with dissolve

    a "Woah! I totally understand that part! "
    a "Sometimes, I’ll hear a song I don’t even know on the radio and it will get stuck in my head for pretty much the entire day. It’s crazy!"
    f "Exactly! Because it follows a pattern. Just like most of Shakespeare’s work does."
    a "That Shakespeare guy should have made a rap album. He sounds like he’d be really good at it if he stopped making up weird words all the time."

    scene futabaamistudy19
    with dissolve

    f "Well...umm...he’s...kind of responsible for a lot of the words that exist today, so..."
    f "If he stopped making them up it...probably wouldn’t have worked out as well for him..."
    a "Yeah, whatever. I still don’t really get it."

    scene futabaamistudy20
    with dissolve

    a "But it’s cool that you’re so smart when it comes to this kind of stuff, Futaba! I’m really impressed!"
    a "Sensei should just get rid of his current class-rep and give you the job instead."

    if bonus == True:
        a "At least I know you aren’t the type to perv out on him all the time."
    else:
        a "At least I know you won't hide soup cans everywhere like Makoto does."

    scene futabaamistudy21
    with dissolve

    f "Hahah...right..."
    a "Sensei, how does that sound?"
    s "It sounds like another thing that would get all of us killed if Makoto was here right now."
    a "Oh, stop. The only thing she’d defeat all of us in is like...a sudoku match or something."
    a "Futaba would be much better than her and we’re already friends."
    a "Don’t you want a class-rep who can help people actually learn instead of just yelling at them all the time?"
    a "Didn’t Futaba sound a lot like a teacher today?"
    s "Well, yeah...but-"
    f "I-I’m really only good at teaching subjects I like. Makoto’s a much better leader than I would ever be."
    f "So...I think she should still be the...important one."

    scene futabaamistudy22
    with dissolve

    a "Do you hear this, Sensei? Futaba is saying she isn’t important now!"
    a "Look what you’ve done!"
    f "I didn’t mean it like that..."
    f "I just think we should maybe...keep practicing instead of deciding who should replace Makoto..."

    scene black
    with dissolve2

    "We don’t hang out for much longer after that."
    "Ami gets up after expelling all of her learning-energy for the day and offers to make dinner for the three of us."
    "I guess Futaba feels like she’s overstayed her welcome as she denies the offer and decides to head home instead."
    "She texts me on her way back thanking me for inviting her over again and I contemplate whether or not I should apologize for just throwing her into the deep end with Ami."
    "I decide against it, though. "
    "I feel like this was a good first time for Futaba."
    "She didn’t have to deal with the nervousness that would be sure to come with us being alone in my room- and she even got to rant about one of the things she loves for a while."
    "All in all, I doubt today could have possibly gone any smoother."
    "I’ll have to invite her over again soon and see what happens next..."

    $ renpy.end_replay()
    $ futabainvite1 = True
    $ futaba_love += 3
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label futabainvite2:
    play sound "phonebeep.wav"

    "I tap on Futaba’s name in my phone and wait for her to answer."
    "Considering that her last visit was a resounding success, I’m sure she’ll agree to dropping by again today."
    "Granted, she likely would have agreed to that regardless, but the type of visit I have in mind this time is rather different from the last one."
    "In fact, even if she’d never come over in the first place, I’d have probably wound up in her room looking for the exact same thing tonight."
    "I’m not the type of guy to say that when I put my mind to something, I always accomplish it-"
    "But that trait certainly seems to apply to my outlook concerning girls."
    "And tonight, my sights are set on the resident busty librarian."

    play sound "phonebeep.wav"

    f "Hey! What’s up, Sensei?"
    f "Did you need me to come over and tutor Ami again or something?"
    s "How about you come over here and tutor {i}me{/i} on how to...feel...good?..."

    if bonus == False:
        s "Like...by hugging me. Just to clarify."

    f "..."
    s "I’m sorry."

    "How exactly do I keep succeeding with girls again?"

    f "I’m...going to forget you said that...but I’ll still come over and...see what happens."
    f "Is Ami not home?"
    s "She should be with Ayane tonight, I think. I overheard the two of them talking in class."
    f "Oh, right. I think they were going to the bathhouse or something together. "
    f "You’re not going with them?"
    s "If I was going with them, I wouldn’t have time for you."
    f "Heheh~ You can have time for me whenever you want."
    s "Cool. So right now is good then?"
    f "Of course...I’ll get dressed and head on over. Okay?"
    s "Yup. See you soon, Futaba."

    play sound "phonebeep.wav"

    "I hang up the phone and continue down the road to my house."

    scene black
    with dissolve2
    stop music fadeout 8.0

    if bonus == True:
        "Given that I’ll be {i}alone{/i} with Futaba in my room for the first time ever tonight, perhaps it’s time to try out something we haven’t done yet?"
        "I’m still not sure if she’s ready to lose her virginity, nor am I sure if I’m ready to steal that from her based on any potential blows it may deal to her already-low self confidence..."
        "But there’s definitely something else I can do for her that she may or may not like the idea of..."
        "I guess I’ll just have to wait and see how things play out."

    "........."
    "......"
    "..."

    play music "asobeatsex1.mp3" fadein 5.0
    scene futabacun1
    with dissolve2

    "Futaba makes it to the house shortly after I arrive and follows me into the bedroom, placing her scarf on my desk before sitting down beside me."
    "It’s clear that she’s a little nervous, but it’s not nearly as bad as I imagined it would be."
    "If this were the “beginning of the[school] year” (AKA: My new term for when I was reincarnated into Kumon-mi), she’d probably get those weird, confused swirlies in her eyes she always used to get back then."
    "She’s been a lot more composed lately."
    "I think she’s really trying- which is incredibly respectable given how much shit she's taken from Yumi."

    f "So...this is your room..."
    s "It is."
    f "It’s...not what I expected..."
    s "What do you mean?"

    scene futabacun2
    with dissolve

    f "Ah! Nothing bad, of course!"
    f "I just expected it to be a little more...sophisticated?..."
    f "It’s kind of hard to describe..."
    f "But I’m sure you’d feel the same way about my room back at home if you were to see it today."

    scene futabacun3
    with dissolve

    f "But...I guess I haven’t been in there in years so...it’s probably a lot more immature now than I remember it being..."
    s "Years? But you’ve only been in the dorms for several months, haven’t you?"

    scene futabacun4
    with dissolve

    f "That’s right. But before that, my parents were paying for me to stay in an apartment close to my last[school]."
    s "You mean the one that sunk into the ground out of nowhere?"

    scene futabacun3
    with dissolve

    f "Yup...that’s the one..."
    s "Are your parents rich or something?"
    s "I know that they’re overseas, but it sounds rough having to send you money {i}on top of{/i} renting out an apartment for you."

    scene futabacun4
    with dissolve

    f "I don’t think we’re rich...but we’re definitely not poor."
    f "They didn't like the idea at first...but I got them to cave since I didn’t want to go with them and leave Japan."
    f "Plus, it was only going to be a year before I switched[school]s and moved into the dorms anyway, so it wasn’t a {i}major{/i} commitment."
    s "Any chance they’d be willing to tack on like...five extra phone bills to their plan? Asking for a friend."

    scene futabacun5
    with dissolve

    f "Sensei...are you...paying for five phone bills?"
    s "Semi-reluctantly, yes."
    f "Why? "
    f "You’re not running some sort of...illegal drug operation that requires you to have that many phones, are you?"
    s "Honestly, going with that is easier to explain, so I’m just going to say yes."

    scene futabacun6
    with dissolve

    f "I don’t really get it but...I’m not sure if my parents would be okay adding that many phone lines without a good reason."
    s "And they wouldn’t be okay with that drug story, I’m guessing?"
    f "No...I don’t think they would."
    s "Any idea when they’re coming back?"

    scene futabacun7
    with dissolve

    f "My parents? No clue."
    f "Are they even allowed to come back right now? "
    f "I’ve heard of some people being allowed to return to Kumon-mi in the middle of the war, but I’m pretty sure it’s only the really {i}important{/i} people and...I don’t think architects count."
    s "So it’s just a matter of waiting for the war to end, then?"

    scene futabacun8
    with dissolve

    f "How would I know?..."
    f "Besides...a-a-aren’t there...you know..."
    f "{i}Other{/i} reasons...you called me over today?"

    if bonus == True:
        jump futabacunx
    else:
        s "No."
        f "...Oh."
        s "Yeah."
        f "Huh."
        s "..."
        f "..."
        s "Wanna play Scrabble and listen to the Tarzan soundtrack?"
        f "..."
        f "Sure."

        scene black
        with dissolve

        "Futaba and I have a heated one-on-one Scrabble battle in which I absolutely wipe the floor with her because I am so smart."
        "Phil Collins is great."

        $ renpy.end_replay()
        $ futabainvite2 = True
        $ futaba_lust += 3
        stop music fadeout 8.0

        "{i}Futaba’s lust has increased to [futaba_lust]! She really likes Phil Collins!{/i}"
        "{i}You can now invite her over to the house on nights and choose to raise your affection or hug her!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label futabalust15:
    scene futabanodokahotel1
    with dissolve

    no "Huh. It’s just a normal hotel room. There are no...ropes or shackles or anything."

    if bonus == True:
        s "Yeah, the bondage room was apparently sold out for the night, so I got stuck with this."
        no "Damn. Hate when that happens."
    else:
        s "Do not accuse me of abducting and enslaving people. I am so nice."
        no "Sorry."

    scene futabanodokahotel2
    with dissolve
    play music "acoustic.mp3" fadein 4.0

    no "So, now what?"

    if bonus == True:
        no "You’re alone with two beautiful [young]women. And one of them is allegedly locked into a rather physical relationship with you, Mr. Humbert."
        s "I really can’t tell if you actually believe this is true or not."
    else:
        no "Want to talk about biochemistry or something?"
        s "You are so hard to follow."

    no "Are you saying I’m hard to follow?"

    if bonus == True:
        s "Yes. Very hard, actually."
        no "As hard as Futaba makes you when you sneak into her dorm at night?"
    else:
        s "Pay attention to me for once."

    scene futabanodokahotel3
    with dissolve

    f "I knew telling you was a bad idea..."

    if bonus == True:
        jump futabanodokax
    else:
        no "I would like to propose a contest idea."
        s "You have the floor, Miss Nagasawa."
        no "Let's see who can jump on the bed for the longest without getting tired or hitting their head."
        s "Great idea. I'm sure that's exactly what the two of you came here to do."
        f "You know us so well, Sensei."

        scene black
        with dissolve

        "All three of us take our shoes before getting onto the bed because we wouldn't be able to live with ourselves if we got it dirty."
        "The jumping begins, but I am significantly taller than the average Japanese male, so I quickly wind up hitting my head on the ceiling."
        "Nodoka and Futaba continue jumping for the next hour and it quickly becomes apparent that neither of them will ever stop, so I am forced to make a decision."
        "That decision is to dropkick Nodoka in the ankles, causing her to fall and lose."

        no "Ouch."
        s "This is revenge for being so smart."
        no "If only there was a member of the American Red Cross here."

        "Futaba and I look at each other and giggle (Because that's me) and then we let Nodoka relocate all of the bones in her leg by herself."
        "Futaba wins the thing."

        $ renpy.end_replay()
        $ futaba_lust += 1
        $ dorm1warpoints += 1
        $ futabalust15 = True
        stop music fadeout 5.0

        "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
        "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
        "........."
        "......"
        "..."

        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date
        else:
            "ERROR ADVANCING TO SUNDAY"

        jump dormwar10

label library40:
    scene futabaphonemom1
    with dissolve2
    play music "justlights.mp3"

    "The morning starts off the same as any other."
    "I get out of bed."
    "I get dressed."
    "I leave the house."
    "And I decide to waste my day away with someone who did not ask for me, but will receive me nonetheless."
    "Someone who, just recently, made a minor decision to keep me at arm’s length in favor of temporary comfort, something I simultaneously admire and abhor."
    "I admire it because it shows that Futaba is becoming her own person."
    "That Kumon-mi is a giant eggshell and she’s finally starting to pip her way out of it."
    "But I abhor it because she is supposed to be imprinted on me."

    if bonus == True:
        "And also because I wanted to see those giant “assets” of hers in action as she ran on the treadmill."

    "Combine that with the fact that I’ve been standing here for roughly five minutes now without being noticed and..."
    "Yeah. Forgive me if I wind up harboring some unwarranted, internal resentment for at least a day or two."
    "Basically, everyone is free to do as they want. But everyone else is free to react to those decisions however {i}they{/i} want."
    "Am I making a bigger deal out of this than I should be considering it was just one thing that happened one time? "
    "Yes. Absolutely. There is no question about it."

    if bonus == True:
        "But if you think that is irrational, I implore you to reconsider how much I enjoy the female body and that this is nothing short of a traumatic experience for me."
        "Oh well, though."
        "I’ll just have her take her clothes off in private whenever she’s off the phone."
    else:
        "And so I will do my best to become a better person so this does not happen again in the future."

    f "...Yeah."
    f "No, I’m doing okay. How are you?"
    f "..."
    f "Still?"
    f "..."
    f "I thought you said it would be possible for you to come visit, though? Didn’t you just need some sort of pass?"
    f "..."

    scene futabaphonemom2
    with dissolve

    f "Oh, no. Not at all. I don’t need anything. "
    f "I’ve been saving basically everything you send me anyway since the dorm is free and-"
    f "...Yeah. I’m still with Rin."
    f "..."
    f "Yeah. She’s doing a lot better."
    f "Nodoka is actually here too now."
    f "..."
    f "Yes, she...is still Nodoka."
    f "..."
    f "My teacher?"
    f "He’s-"

    if bonus == True:
        s "Instructing you on how to properly pleasure a man."
    else:
        s "Giving you the good grades that you rightfully deserve."

    scene futabaphonemom3
    with dissolve

    f "HE’S FINE!"
    f "Mom, I’ve gotta go now. Someone just showed up to the library and-"
    f "Yes! I told you, I’m fine!"

    if bonus == True:
        s "Tell her about our “lessons.”"
    else:
        s "Tell her how much you are enjoying college and that everything is okay."

    f "Bye, Mom! Love you!"

    play sound "phonebeep.wav"
    scene futabaphonemom4
    with dissolve

    f "..."
    s "..."
    s "Good morning."
    f "Yes. Good morning."
    s "You should have let me talk to her."

    if bonus == True:
        f "I would have absolutely let you talk to her if the first thing out of your mouth wasn’t about our “lessons.”"
        s "I’m sorry, Futaba. I just can’t look at you without being overcome by lust and excitement."
        f "You can’t look at {i}anything{/i} without being overcome by those feelings..."
        s "And you are no exception to that."
    else:
        f "Maybe next time."

    s "Why were you talking to your mom?"

    scene futabaphonemom5
    with dissolve

    f "Why?"
    f "Because...she’s my mom."
    f "I don’t think I really need a reason other than that, do I?"
    s "I guess not. I’ve just never seen you talking to her before."
    f "Do you not talk to your parents often, Sensei?"
    s "I don’t have any parents."

    scene futabaphonemom6
    with dissolve

    f "Wait, you weren’t...adopted like Rin, were you?"

    if bonus == True:
        s "No. I just have zero recollection of my non-Ami family. So it’s essentially the same thing as not having parents."
        f "That’s...not exactly the same thing."
        f "They might be really worried about you."
        s "Or dead."
    else:
        s "Nah. I think I just kinda showed up one day."
        s "My background isn't ever really explained."

    scene futabaphonemom7
    with dissolve

    f "R-Right..."

    if bonus == True:
        f "Or dead..."

    s "Way I look at it is that I have no need for them, so them not existing isn’t really a big deal."
    s "I’m sure it saves me a lot of time too since I don’t have to talk to them on the phone while other people are waiting for me."
    f "Sensei, I’m not going to apologize for talking to my Mom instead of you."
    s "First the gym, now this?"
    s "Futaba...do you hate me?"

    scene futabaphonemom8
    with dissolve

    f "Of course not...you’re no less important to me at this point than Rin or Nodoka."
    f "Well, actually, you’re a little less important to me than them. But that’s only because I’ve known them for a lot longer and..."
    f "And I...still don’t totally understand what’s going on between us..."

    if bonus == True:
        s "If you take your clothes off, I’d be happy to remind you."
    else:
        s "Huh? Aren't we hug buddies?"

    scene futabaphonemom9
    with dissolve

    f "Uhh...no. I’m okay."

    scene black
    with dissolve

    "Futaba hates me now and our relationship is over."
    "I go home and spend the rest of the day wallowing in sadness and self-pity."

    f "Sensei...can you please open your eyes?"

    scene futabaphonemom9
    with dissolve

    s "Yes. But not because you asked me to. Because it is unsafe to keep them closed when there are wild animals out here that could tear me to shreds at any given moment."
    f "We live in suburban Japan...there isn’t any wild animal that is going to attack you out of nowhere like that."
    s "I’m keeping my eyes open just in case."
    f "R-Right..."

    scene futabaphonemom10
    with dissolve

    f "Umm...anyway...I’m kind of glad that you showed up this morning because I..."
    f "Wanted to tell you a little about how the other night went. Since I...made you leave and stuff."
    s "Sure. What’s there to say, though? "
    s "Figured you three just...did gym stuff for an hour or two and went back home."

    scene futabaphonemom11
    with dissolve

    f "That’s exactly right. We did gym stuff for an hour or two and then went back home."
    f "But...since it was just Rin and Nodoka...I was less worried about...looking like an idiot and..."
    f "I don’t know. I think I maybe even felt a little good afterwards."
    f "Obviously nothing has really changed yet since it was only one day, but...yeah."
    f "I wanted to let you know that...I didn’t just...cry the entire time after you left."
    f "I actually...followed through and tried to make myself better."

    if bookdate == True:
        scene futabaphonemom10
        with dissolve

        f "Do you...remember when the two of us went to the bookstore together?"
        f "And how I...kind of confessed my feelings for you?"
        s "It wasn’t “kind of.” You made it very apparent that you’re falling in love with me."
        f "And you made it very apparent that focusing on things like that isn’t productive if I can’t accept who I am first."
        f "The thing is, though...I don’t want to accept who I am. I want to be somebody else."
    else:
        s "What is “better,” though? What’s so hard about accepting who you are?"
        f "Who I am isn’t who I want to be. That’s the issue."

    scene futabaphonemom11
    with dissolve

    f "If I could wake up in the morning and see someone with Rin’s body...or Chika’s body...or basically anyone else’s body, I’d be a lot more comfortable stepping outside."
    f "But right now, it’s kind of like staring into an abyss. Or...TV static, I guess."
    f "It’s just one huge mess of spare parts that don’t fit together...but it’s still closer to some sort of...indiscernible blur than a monster."
    f "If you saw something like that, you’d try to tune it out too, right?..."
    f "I’m sure you’d do all sorts of...self-destructive things to hide the truth of how you feel, because that’s the easiest thing someone {i}can{/i} do."

    if bonus == True:
        play sound "static.mp3"
        scene imissyou12 with flash
        scene futabaphonemom11 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene frown with flash
        scene futabaphonemom11 with flash
        stop sound

    f "The easiest routes always have downsides, though. They wouldn’t be easy if there wasn’t some sort of risk involved."

    play sound "static.mp3"
    scene imissyou19 with flash
    scene futabaphonemom11 with flash
    stop sound

    f "I...don’t know if you can really understand what I’m talking about since...you seem really comfortable with-"
    s "I know what you’re talking about."

    scene futabaphonemom12
    with dissolve

    f "You do?"
    s "Yes."
    s "I can’t really put my finger on how, but I do."
    s "I think we perceive self-destruction a little differently than one another, though."
    f "Why is that?"
    s "Well, you think it’s something that can be avoided and I think it’s an inevitable fate."
    s "We’re all going to self-destruct one way or another, so pushing it back with hard work and determination is just a waste of energy."

    scene futabaphonemom13
    with dissolve

    f "No..."
    f "You’re wrong about that."
    f "Because even if my destruction is inevitable, I want at least one day where I can see my shadow next to yours and not hate myself for the differences in them."
    f "So I can’t give up until I get at least one day like that."

    scene futabaphonemom11
    with dissolve

    f "Hopefully, it won’t end after just one day, though."
    f "To put it bluntly, I feel rather lonely whenever I see my shadow {i}without{/i} yours next to it."
    f "So you can be as negative and insightful as you want, but I’ve made my decision and I’m going to stick to it."
    f "There’s something I’ve been hiding from you, Sensei...one of the downsides from the easier path I took before deciding to {i}actually{/i} start trying again."
    s "And that downside is?"
    f "That downside {i}was{/i}. It’s not happening anymore."
    f "And I can’t guarantee it won’t ever happen again...but I can at least say I’ll try my best not to-"
    s "Just tell me what it is, Futaba."

    scene futabaphonemom14
    with dissolve

    f "An...eating disorder."
    f "And this isn’t me asking for sympathy. It’s me telling you because I’m tired of keeping it a secret from you for no good reason."
    f "But I’ve been making myself throw up to try and lose weight for a...pretty long time now."
    f "And that’s part of what my Mom and I were talking about today."
    f "She and my dad thought I’d stopped a long time ago, but..."
    f "Well, it’s a lot easier to lie to people when they’re not physically around."
    f "But...I came clean to her as well."

    if bonus == True:
        s "Suddenly, the timing of my sex joke seems a lot worse than it did at first."
    else:
        s "I interrupted such an important phone call? You should have slapped me."

    scene futabaphonemom9
    with dissolve

    if bonus == True:
        f "There...isn’t really any acceptable time for making a sex joke while a [teenage]girl is on the phone with her mom..."
    else:
        f "I will next time..."

    s "You’re okay now, though?"
    s "You’re not doing that whole...vomiting thing anymore?"

    scene futabaphonemom11
    with dissolve

    f "Right...so...if I...start gaining weight from...{i}not{/i} doing that-"
    s "I’ve already told you that I don’t care about-"
    f "You do, though. And it’s fine that you do."
    s "I don’t know how many times I have to say this, but nope. Don’t care at all."

    if bonus == True:
        f "Then...why haven’t we had sex yet?"
        s "Hey, I’m ready whenever you are. I’ve been holding off because you’re clearly uncomfortable with it."
    else:
        f "Then why has the amount of hugs we have on a weekly basis dwindled as of late?"
        s "Hey, I always accept more hugs. Do not blame me for the fact that you are slowly becoming anti-hug."

    scene futabaphonemom15
    with dissolve

    f "Hahaha! Yeah...Yeah, I guess that’s mostly on me..."

    if bonus == True:
        s "Not “mostly.” I will literally have sex with you right now. I don’t care."
    else:
        s "I will hug you right now. I don't even care."

    scene futabaphonemom16
    with dissolve

    f "Okay, so maybe you really {i}don’t{/i} care. But I still do."
    f "Even...being touched by you makes me feel...extremely self-conscious and...yeah."
    f "This isn’t really a thing I want to be talking about outside of the library, now that I think about it."
    s "Then take the day off and...let’s go for a walk or something."
    f "Sensei, I can’t just-"
    s "You’ve made it pretty apparent today that you can do whatever the hell you want."
    s "If you can decide to turn your life around and try to become a version of yourself you like more, I’m pretty sure you can survive a day away from your volunteer librarian position."
    f "..."
    s "Don’t just stand there while I’m taking revenge on you for kicking me out of the gym the other night."
    f "I’m not just standing here. I’m waiting for you to lead the way."
    s "Oh. I expected there to be some sort of verbal agreement."
    s "That’s normally how accepting invitations works."
    f "Since when do we do {i}anything{/i} how we’re supposed to be doing it?"

    if bonus == True:
        f "I’m a freshman and I gave you a boobjob in the nurse’s office."
    else:
        f "The last time we made macaroni and cheese, you used four whole sticks of butter."

    s "Yeah, that was awesome."
    f "It was...fine. But what I’m saying is that we’re so far removed from how things are {i}supposed{/i} to be done that we should just...follow our hearts."
    f "And today, like many other days, my heart wants me beside your shadow."

    scene black
    with dissolve2

    "I don’t find much of a point in responding to Futaba as she is clearly much more determined to speak today than I am."
    "My irrational rage aimed at her refusal to allow me to watch her gym routine has finally subsided, however, and the two of us are now on a journey to-"

    scene futabaphonemom17
    with dissolve

    f "The...other side of the[school]?"
    s "I didn’t know where else to go."
    f "You...were the one who invited me to walk around, though..."
    f "You didn’t even have a plan in store?"
    s "Every plan I’ve ever made has been significantly less wholesome than walking around town with a girl who just opened up about her insecurities to me."
    f "You’re more than welcome to...share a few insecurities of your own, Sensei."
    f "I’m sure there has to be something."

    "There isn’t."
    "I am completely secure in everything."
    "My feet are planted so firmly to the ground that they would not even move in the event of an earthquake."
    "And if an earthquake were to come, and the ground beneath my legs would crack in cartoonish fashion, I would stare directly at it as my appendages are stretched so far apart that I'm torn in half."
    "There are people in this world who want to become better versions of themselves, and there are people who don’t."
    "But whatever those people decide to do is completely up to them."
    "My words don’t matter to Futaba, just as hers don’t matter to me."
    "We’ll keep existing and keep on fighting our own fights regardless of how much unnecessary support we pump into one another."

    if bonus == True:
        "Thankfully, support isn’t the only thing I have the privilege of pumping into her."

    s "Nah. I prefer to keep my problems to myself."
    f "Even after I just opened up about my biggest problem of all?"
    s "Is that really your biggest problem, Futaba?"

    scene futabaphonemom18
    with dissolve

    f "I...I think so?"
    s "You’re not worried about how each and every day we move one step closer to death? Or how the world is becoming less and less habitable with each passing moment?"
    f "I...don’t think I’m...supposed to start thinking about those things until after I graduate..."
    s "Since when do you do what you’re supposed to do? Stop wasting your time and fear them now."
    f "Sensei...you’ve given me a lot of...strange motivational speeches...but this one is just-"
    s "A joke."
    s "Kind of."
    s "Let’s just say I’m only half serious."
    s "If this bulimia issue is your biggest problem, I’m thankful you shared it with me."
    s "I didn’t know and I’m sorry you had to go through something like that."
    s "But there’s nothing I could share with you about myself that would make me feel any better or worse than I do right now."
    s "And there’s not much I know anyway."
    f "What do you mean by that?"
    s "I mean that this world is incredibly complicated."
    s "I can’t risk taking my feet off the ground or it will all just float away."

    if bonus == True:
        scene futabaphonemom19
        with dissolve

        f "I wouldn’t mind holding you down."
        s "I wouldn’t mind holding {i}you{/i} down either, but you want to be more comfortable with yourself first."
        f "Ha ha ha. It’s not like your...thing would fit inside of me anyway."
        s "We’ll never know unless we try."
        f "I can’t believe I agreed to skip out on the library to listen to my teacher make sex jokes all morning."
        s "It’s better than having the sex jokes happen {i}inside{/i} of the library, isn’t it?"
        f "Not...by much."

    "The shadows of the branches of a tree slaughtered by the harsh winter climate spread out and climb the walls of the[school] building, making it resemble some sort of spider web."
    "Shadows seem to be a recurring theme today."
    "Whether it be the shadows of the two of us or of the dying tree, it’s as evident as ever that there is a darker side to everything."
    "Futaba’s dark side managed to emerge today."
    "But instead of ignoring it like a normal person would, she parked it beside mine and reiterated that there is still joy to be found inside of darkness itself."
    "And that the darkest parts of me, which she will likely never come to know, somehow manage to help her feel less lonely."
    "And here, all I wish is to see a shadow as anything more than a shadow."
    "To see anything at all as more than exactly what it is."
    "To live without conflict because life itself is conflict enough."
    "But none of that is possible. Especially not with someone like this beside me."
    "She will follow me into the flames of hell and, instead of pushing her away, I will grab her wrist and pull her into them so I don’t have to die alone."
    "But she is weak and will die before me."
    "So I will die alone anyway."
    "Today is going to be a bad day."

    s "Okay, let’s go somewhere else."
    f "Yeah...I was wondering when you were going to say that."
    f "I like the[school] and everything, but...it’s not exactly fun just hanging out on the side of it. Even if it’s you I’m hanging out with."
    s "Yes, please continue to say nice things about me. It will soften the blow the next time you don’t let me watch you exercise."
    f "Oh, stop. You spent most of your energy on that...scary blonde woman anyway."
    s "Scary blonde- Oh, you mean Yumi’s mom."
    f "Yeah, Yumi’s-"

    scene futabaphonemom20
    with dissolve

    f "Wait, what? Huh?"
    f "That..."
    f "That woman was..."
    s "Anyway, time to go somewhere else."

    scene black
    with dissolve

    s "Kumon-mi awaits, Futaba."
    f "That...was Yumi’s mom?!"
    f "Wait! Sensei!"

    "I start walking away from Futaba, realizing that I have already said too much, and begin to head down the same path I take home every day."
    "I don’t have a specific destination in mind but, if I had to choose-"
    "I’d probably pick somewhere with a lot of shade."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ library40 = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump library40part2

label library40part2:
    if _in_replay:
        play music "justlights.mp3"

    scene futabayumisnow1
    with dissolve2

    "There’s no shade anywhere."
    "Or at least not on the way home, there isn’t."
    "I’m sure there’s shade in some part of the world because...the world is big and whatnot."
    "But, by comparison, my world is rather small."
    "It’s small enough that, if I closed my eyes and didn’t mind wandering into traffic from time to time, I could probably learn to traverse it in complete darkness."
    "Not that I’d want to do that or anything, but I do think it would be nicer at times."
    "I’m sure Futaba would agree as well."
    "If everyone was blind and we all walked around with canes or seeing eye dogs, she’d never have to cope with the fact that her body isn’t what she wants it to be."
    "Think of all of the years in all of the loops where the first look on her face in the morning wasn’t one of disappointment or disgust."
    "And think of all the different iterations of me that have told her not to worry about it."
    "Think of all of the ones that did."
    "Think about me. Think about me. "
    "Think about me."
    "Think about me because it’s easier to resent someone {i}worthy{/i} of resentment than someone who doesn’t believe to be even worthy of themselves."
    "Someone who has harmed absolutely no one, yet feels the weight of the world on her shoulders with each passing moment as if she didn’t already believe she had enough “weight” in the first place."
    "Think of the me’s that told her she wasn’t good enough. Or the her’s that never tried turning things around. Think of how much it must have hurt."
    "Think of how everything hurts. "
    "And that even in this slightly more perfect rendition of a world we’ve been stuck in for {s}God{/s} god knows how long, there is still more pain than we can shovel into our pockets."
    "It tears through the fabric, like an improperly stored pocket knife- slicing our legs open and causing blood to slowly trickle down the insides of our pants."
    "This train of thought makes me think about Noriko."
    "Which leads me into a second train of thought about how I can’t even focus on what’s beside me without my mind wandering off and getting lost."
    "Without running away."
    "I run back."

    s "So...now what?"
    f "What do you mean?"
    s "I mean what do we do now that we’re not at[school]? "
    s "Did you want to get breakfast or something?"
    f "I...had a protein bar this morning."
    s "Oh. Well I guess I’ll just starve then."

    scene futabayumisnow2
    with dissolve

    f "We can still stop somewhere if you’d like. It’s...not like I have anything else to do now that I’m not in the library."
    s "It’s fine. I’m not really that hungry. I just didn’t really know what else to do."
    s "We can go back to your dorm, I guess."
    f "If it’s okay...I think I’d like to stay out here for a little while longer."
    s "Interested in joining the soccer team? We could go see what Miku is up to."

    scene futabayumisnow3
    with dissolve

    f "I think...just the gym is enough for now. "
    f "I should probably wait a little longer before trying to catch up to someone like Miku. "
    f "I’m not really much of a fan of sports in the first place."
    s "That’s fine. I’m not either, to be completely honest."

    scene futabayumisnow4
    with dissolve

    f "Aren’t you the coach of the soccer team, though?"
    s "Yes. But that position sort of came to me on its own and wasn’t something I went out of my way to acquire."
    f "That seems like a pretty serious thing to just...come to you out of nowhere."
    s "Well...wherever there are thighs...there will be me."
    s "It was probably just the universe doing me a favor."

    scene futabayumisnow5
    with dissolve

    f "I’m going to...do everyone a favor and just pretend I never heard that."

    if bonus == True:
        s "No. You {i}did{/i} hear it. I need you to etch this into your memory so you can expand your glossary of sex acts."
        f "I mean...there aren’t really any “sex acts” you can use your thighs for."
        s "Oh, Futaba. You still have so much to learn."

        scene futabayumisnow6
        with dissolve

        f "Wait...is there actually...something like that?"
        s "There is."
        f "But...how does..."
        s "Remember what we did in the nurse’s office? It’s just like that but...with your thighs."
        f "And that feels good?"
        s "I mean, I doubt it would feel good for you."
        f "That just sounds difficult."
        s "It sounds like good exercise to me."

        scene futabayumisnow7
        with dissolve

        f "Oh. So that’s where we’re going with this."
        s "I’m helping you become a better person."
        f "No. You’re just turned on."
        s "That’s a side effect. This is really just to make you happier when you wake up in the morning."
        f "There are a lot of easier ways to make me happier in the morning, Sensei."
        s "And how many of them involve my penis?"

        scene futabayumisnow8
        with dissolve

        f "Maybe like...three?"
        s "Can you name them?"
        f "Not really."
        s "Well then I guess you’ll just have to live your life in misery as I have no idea what else I can do for you."
        f "How many times do I have to tell you that you don’t have to do anything for me? Just let me handle this part of my life on my own."
        s "This makes it sound like you have a portable version of my penis."

        scene futabayumisnow9
        with dissolve

        f "Not everything is about your penis, Sensei!"
        s "You take that back right this instant, [young]lady."
        f "Are you my dad now?!"
        s "Do you normally talk about penises with your dad?"
    else:
        s "I'm sorry. That was uncalled for. I will do my best to refrain from bringing up legs for the indefinite future."

    scene futabayumisnow10
    with dissolve

    f "Hah...I should have stayed in the library..."
    s "Come to think of it, I’m pretty sure I overheard you saying something about your parents coming to visit when you were on the phone earlier."

    scene futabayumisnow4
    with dissolve

    f "Were you really listening for that long?"
    s "I was. And, sorry for asking but, is something like that even possible?"

    scene futabayumisnow11
    with dissolve

    f "I don’t really know...But it seems like that’s exactly the issue."
    f "They were under the impression that they’d be able to get a pass that would allow them to return since they were away on work, but it seems the process isn’t as easy as it sounds."
    s "This city gets more and more confusing with each passing day."
    f "You think so? It seems mostly normal to me."
    f "But...I’ve also never really lived anywhere else for more than a month or two, so I’m probably not the best judge of that."
    s "I just don’t get what the big deal is. "
    s "Like, why block off the city if-"

    scene futabayumisnow12
    with dissolve

    f "Wait...hold on a second."
    s "What’s wrong?"
    f "There’s...someone leaning up against the wall."
    s "Were we talking about something they shouldn’t be listening to?"
    f "No...it’s just..."
    f "Look."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene futabayumisnow13
    with dissolve

    "Futaba and I find Yumi with her back pressed against some sort of anime billboard and I think for a second about how she would look in cosplay."
    "Of course, I realize seconds later that I should probably be thinking about more important things."
    "Like how to explain why I’m out walking around with Futaba at this time of the morning."
    "Then again, I’ve also spent time in the city with Yumi and there’s nothing going on between {i}us{/i} so..."

    if bonus == True:
        "Well, except for that one thing."
        "But yeah, you get what I mean."

    f "Umm...G...Good morning, Yumi..."
    y "Don’t have to stop and fuckin’ greet me, you know. Not really in the mood to talk."
    s "Are you ever in the mood to talk?"
    y "Nope. Now get the fuck away from me. Too early for this shit."
    f "Umm...Sensei and I..."
    y "Don’t fucking care. You ain’t holdin’ hands or anything so I ain’t got a reason to get all pissed."
    y "Just take the fucking hint and keep walking. I’m not starting anything today."
    s "Are you okay?"

    scene futabayumisnow14
    with dissolve

    y "The fuck do you care? I am making this as easy as fuckin’ possible for you! Just leave me alone!"
    s "I just-"
    y "Again, don’t care! "
    y "I’m doin’ that whole “Ain’t got nothin’ nice to say, so don’t say anything” bit and you’re tryin’ to fuck me up!"
    y "Just go hang out or whatever! I’m stayin’ out of your way!"
    s "I’m shocked."
    y "Why?!"
    s "This just...might be the nicest thing I’ve ever seen you do."

    scene futabayumisnow15
    with dissolve

    if bonus == True:
        y "Suck my dick, you [niece]-fucking shitbag. "
    else:
        y "(Airplane noises)"

    f "That’s-"
    s "It’s fine. Baby steps, Futaba. Baby steps."
    s "She’ll get there."
    f "R-Right..."
    s "..."
    y "..."

    "The three of us stand there for a moment, causing the air to get noticeably less comfortable."
    "I start walking away to end the situation and get on with the day, but Futaba keeps her feet planted."
    "I’m not sure what it is she wants to accomplish by doing so, but-"

    f "Yumi..."
    f "Did...did you want to...hang out with us, maybe?"

    "Oh, okay. So that’s what’s going on here."
    "I stop myself from leaving and turn to see how the rest of this...exchange goes."

    scene futabayumisnow16
    with dissolve

    y "No. Get the fuck away from me."
    f "Okay, but...I think it...might be nice actually getting to spend time with you for once..."
    y "Why? All I do is make fun of you and shit. You some kind of masochist?"
    f "No, but...I just...have a hard time accepting that’s the real you."
    y "No idea what the fuck you’re talkin’ about, but the “real me” wants to be left alone. Now beat it before I punch your fucking teeth in."

    scene futabayumisnow17
    with dissolve

    f "Hehehe..."
    y "...The fuck you laughing at?"
    y "If this is some kind of...weird fucking test or something-"
    f "No no no...it’s nothing like that."
    f "I was just thinking that..."
    f "You look a lot like your mom when you start...being intimidating like that..."

    stop music fadeout 5.0
    scene futabayumisnow18
    with dissolve2

    "Uh-oh."
    "Bad move, Futaba."

    y "The fuck did you just say to me?"
    f "I...wait..."
    f "What did I do?"
    y "What the fuck did you just say to me? Say it again."
    y "I want to hear it."

    scene futabayumisnow19
    with dissolve

    f "I...I just thought..."
    s "Futaba, come on. Yumi’s not in the mood to talk right now."
    y "Oh no. I’m in the mood to talk now. I’d {i}love{/i} to talk, actually. "
    y "So go on. Tell me again."
    y "Who did I look like just now?"
    f "You..."
    f "You looked kind of like...your mom..."

    play sound "static.mp3"
    scene futabayumisnow20 with flash
    stop sound
    play music "thingsthathurt.mp3"

    "Yumi grabs Futaba by the shoulders and spins her around, throwing her up against the billboard that she’d been leaning on herself just seconds ago."
    "She rears back her fist and punches the wall, which allows me to breathe a sigh of relief on the way over as I thought she was about to kill a classmate."

    y "Listen here you fat, fucking bitch. I am {i}nothing{/i} like my mother. Nothing."
    y "Got it?"
    f "I...Yumi-"

    scene futabayumisnow21
    with dissolve

    y "Got it?!"
    f "Yes! I’m sorry!"
    y "You been pokin’ around for dirt on me or some shit?! So tired of me picking on you that you have to get involved in my fucking personal life?!"
    f "No! I just...met her and..."
    y "I don’t care what your fucking excuse is! You stay out of my shit and I’ll stay out of yours! "
    y "I told you to just fucking walk away, didn’t I?! I was gonna leave you alone!"
    y "But you must have seen that and decided, “Oh! Yumi looks vulnerable today! Time to hit her where it hurts!”"
    y "Is that right?! Is that what you're doing?!"
    y "Fuck you! Fuck you fuck you fuck you!"
    f "I...really didn’t mean to..."

    scene futabayumisnow22
    with dissolve

    s "Come on. That’s enough."
    y "No! It’s not fucking enough! Do you have any idea who that “mother” of mine actually is?!"
    f "I...didn’t even know it was your mom until a little while ago..."
    y "Of course you didn’t! Just a tiny, little mistake from a big, fucking girl!"
    y "Doesn’t even matter, right?! "
    y "Right?!"
    s "Yumi, let go. Futaba and I were leaving."

    scene futabayumisnow23
    with dissolve

    y "Yeah. Of {i}fucking{/i} course you were."
    y "You gonna go have a good time with the teacher, Futaba?"
    y "Gonna go feel better about yourself while he sits there and tells you your size doesn’t matter or some shit?"
    y "Gonna stuff your fucking face with junk food while looking down on people like me? People who never even got to know their parents?!"

    scene futabayumisnow24
    with dissolve

    y "No! Don’t close your fucking eyes, cunt!"
    y "Look at me and tell me again how acting intimidating makes me look like a fucking junkie who can’t even be bothered to take care of a little girl!"
    y "I should fucking kill you right here!"
    s "Yumi-"
    y "Never talk about my mother again! Got it?!"
    f "Yes! Yes! I won’t!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene futabayumisnow25
    with dissolve

    y "Do you have something to do with this?"
    s "Yes."
    s "It’s my fault. Futaba doesn’t know anything about your relationship with your mother."
    y "Well she certainly knows something now."
    s "It’s all one big misunderstanding."
    y "Was it a misunderstanding when you told me you wouldn’t get involved anymore? "
    y "Am I too fucking dumb to understand what that means, Sensei?"
    s "Yumi-"
    y "I don’t know what the {i}fuck{/i} you are trying to do to me, but {i}stop{/i} getting involved with my family."
    y "Leave me alone. "
    y "And if you’re going to drag other people into it, at least drag in someone who will actually put up a fucking fight so I don’t feel like I’m about to strangle a defenseless little kid."
    s "I’m sorry. It was an accident."
    y "Yeah, and so was I. But I’m fucking here now. And I don’t need my teacher and his walking fucking morale booster to show up out of thin air and remind me of that."
    s "Yumi..."
    y "Just...leave me the fuck alone."

    scene black
    with dissolve

    "........."
    "......"
    "..."


    scene futabayumisnow26
    with dissolve

    s "Are you okay?"
    f "Yeah...but..."
    s "That was just a really bad coincidence. "
    s "I didn’t expect to run into Yumi without warning you to never bring up that...{i}subject{/i} around her."
    f "That...was a pretty important detail to leave out..."
    f "If you weren’t here, I..."
    s "If I wasn’t here, you never would have learned about Yumi’s mother in the first place."
    s "So let’s just call it a day and go back to the dorm. "
    s "I’m sure Yumi wants to forget this even more than the two of us do, so just don’t bring it up again and everything should be okay."
    f "You..."

    scene futabayumisnow27
    with dissolve

    f "You two must be...getting pretty close if you know things about Yumi’s family..."
    f "I thought Chika was the only one who...knew anything about that..."
    s "“Close” definitely isn’t the right word, but I don’t think now is the best time to really deep-dive into such a convoluted relationship."
    f "Yeah...probably not..."
    f "I’m sorry if I managed to...make it even more convoluted, though."
    f "She’s said a lot of mean things to me before, but...I’ve never really seen her get like that."
    s "And, if everything plays out the way it should, you never will again."
    s "Let’s go back for now, though. I’m sorry I didn’t warn you ahead of time."

    scene futabayumisnow28
    with dissolve

    f "It’s okay..."
    f "This is just what I get for...trying to be nice to someone who doesn’t want anything to do with me."

    scene black
    with dissolve2

    "Futaba and I head back to the dorm in almost complete silence."
    "We try making conversation about a few random things along the way, but nothing really sticks. "
    "The air is too uncomfortable and awkward after what we just experienced."
    "It’s strange how quickly things can fall apart just by being in the wrong place at the wrong time."
    "But it’s even crazier that, for some people, every place and every time is always wrong."
    "And there’s nothing we can really do about it."
    "We’ll just keep existing and keep hoping that tomorrow will be more convenient than today."
    "Sometimes it will be."
    "Other times, it would probably be better to not exist at all."

    $ renpy.end_replay()
    $ library40part2 = True
    $ futaba_love += 1
    stop music fadeout 6.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label futabanew1:
    play sound "knock.mp3"
    stop music fadeout 15.0

    "I knock on Futaba’s door and wait for her to answer, knowing full well that she will because she is Futaba and I am the knight in shining armor that she dreams about each night."
    "It’s not a role I ever imagined assuming, and I’m not about to start acting chivalrous now that I’ve come out and acknowledged it."
    "But it {i}is{/i} nice knowing that someone out there is willing to entrust their whole self to me."
    "I say this despite having not yet taken any of the interesting parts of her into my arms."
    "I say this despite not having anything to save her from."

    f "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I steel my nerves in preparation for a late night encounter with a damsel undistressed. "
    "Her room smells of the same lavender perfume she so commonly wears."
    "And my mind sinks to the same depths it so commonly hides away in."
    "........."
    "......"
    "..."

    scene futabarevision1
    with dissolve2
    play music "love.mp3"

    f "Hey...Sorry for looking like this again. I planned on spending the rest of the night writing, so I got changed as soon as I came home."
    f "I hope...that’s okay?"
    s "It will never {i}not{/i} be okay. And I’m glad to see you’re still throwing yourself at this story."

    scene futabarevision2
    with dissolve

    f "I would have had a harder time {i}not{/i} throwing myself at it after all of the encouragement you gave me after reading the first part."

    scene futabarevision3
    with dissolve

    f "In fact, I’ve already made tons of changes! I even brought Pedro back to life!"
    s "Good. He never deserved death in the first place."

    scene futabarevision4
    with dissolve

    f "No...I actually felt really bad when I seriously started thinking about it. Which...I probably shouldn’t since he’s just a character I made up, but..."
    f "It’s kind of hard...{i}not{/i} getting attached to...people and creatures inside of your head, don’t you think?"
    s "Well, I haven’t written anything in...longer than I can remember. But I get what you’re saying."

    scene futabarevision2
    with dissolve

    f "Pedro isn’t...the only character that’s changed either."
    s "Oh? Does my- "
    s "Or, uhh...sorry. {i}Does the male character{/i} have anything interesting about him yet? Or is he still the...blank slate he’s designed to be?"

    scene futabarevision5
    with dissolve

    f "I don’t think he’s a blank slate at all. I actually...really like him for who he is in the beginning of the book. And he’ll develop even more as the story progresses."
    f "All of the biggest changes...actually involve the heroine of the story."
    s "Oh?"

    "Well, that’s unexpected. I was pretty sure that Futaba’s Mary Sue esque protagonist was just her version of a self-insert-"
    "A way to sneak into her story on a more personal level without naming the character “Futaba.”"
    "But apparently, she wasn’t good enough to make the final cut."
    "Take that as you will."

    s "Why did you change her, exactly? The story seemed...completely built around her."

    scene futabarevision6
    with dissolve

    f "And it still is."
    f "But...I read the story again right after you left the library...and something about her just didn’t sit right with me."
    s "Do you know what that {i}something{/i} was?"
    f "Flaws."
    f "All of the best protagonists are flawed. They all have problems...traumas...things that make them feel more human."
    s "Well, the girl in your story was lonely, wasn’t she? I figured her reclusive nature was her biggest flaw."
    f "I don’t...really think that being lonely is a flaw. That’s more of a...result. And the way I had it portrayed made her feel like a victim of sorts."
    f "I never wanted that."
    f "That’s why she didn’t sit right with me. It felt wrong to have her enjoying herself and living her best life without ever revealing her...true colors to anyone. Or any of the things that make her whole."
    s "You have...gotten significantly better at writing since the last time we spoke."

    scene futabarevision7
    with dissolve

    f "D-Don’t just jump the gun and go saying things like that before even reading the changes, Sensei."
    f "This is just my...experience as a reader coming into play. I still have a long way to go before I can create something I’m completely proud of."
    f "Until then, I just have to...keep trying things in different ways and hoping they come out a little more interesting..."

    scene futabarevision8
    with dissolve

    f "After all, I..."
    f "I want the heroine to entertain you. And what’s the point in getting to know someone when all they are can be found on just one small sheet of paper?"

    scene futabarevision9
    with dissolve

    f "A-A-And by “you” I meant the reader! Not {i}you!{/i}"
    f "I want...anyone who reads the story to be interested in the protagonist! Even if...you {i}are{/i} the only person I plan on showing this to!"
    s "This is the same exact “mutated reflection” I was talking to you about."

    scene futabarevision10
    with dissolve

    f "Huh? It is?"
    s "Yeah. It’s only natural for a writer to put a little bit of themself into the main character of a story they’re writing. "
    s "You didn’t like how flawless the heroine of your story was because she didn’t remind you at all of how you see yourself, right?"

    scene futabarevision11
    with dissolve

    f "Well, umm...I...I suppose that’s at least...somewhat true..."
    f "It’s...It’s not as if I was...modeling the main character after myself or anything. That would be...conceited..."
    f "Wouldn’t it?"
    s "If it was, I don’t think you would have spent the whole day trying to make the character worse."

    scene futabarevision12
    with dissolve

    f "Using the word “worse” is...a little hurtful. I think...a person’s flaws are one of the many things that can make that person beautiful."
    f "It’s only when there are...far too many of them that people become ugly..."
    s "And how many {i}flaws{/i} would you say that you have, Futaba?"
    f "..."
    s "Futaba-"
    f "If I tried to write them all down, I’d run out of paper."
    s "..."
    f "..."

    scene futabarevision7
    with dissolve

    f "But, umm...I know that’s not really something you want to hear about and...you’ve already given me {i}one{/i} assignment, so it’s not like I can just tack on another one."
    f "Especially one as silly as that...I’m just...I’m just being a little dramatic. That’s all."
    f "All of this talk about flawed characters and...what heroines are supposed to be like has made me a little self conscious. It’ll pass in no time at all and...I’m sorry for talking so much about it."
    s "It’s fine. I don’t really think you were telling the truth anyway."

    scene futabarevision10
    with dissolve

    f "You...don’t?"
    s "Nope. Because if having too many flaws really made someone undesirable, you’d stop smiling every time you see me."
    f "..."
    s "..."
    f "Was that...a line from a book?"
    s "You think I could have just remembered a specific, relevant quote like that off the top of my head? Of course that wasn’t from a book."
    f "You should...put it in one. You’re so much better at this than I am."
    s "Yeah, well, I’ve probably had a lot more practice than you. I’m a teacher after all. "

    "Even if this isn’t something I would have chosen to do on my own."

    scene futabarevision4
    with dissolve

    f "Umm...do you...maybe want to step outside for a little while?"
    f "I think a...break might be nice. I’ve been kind of going nonstop since I got back and..."
    f "I’d like to talk a little more...if that’s okay."
    s "It’s fine. But I think you might want to get dressed first. I can’t imagine you’d be very happy with the whole world seeing you like that when you’re still embarrassed about {i}me{/i} seeing you in that condition."

    scene futabarevision13
    with dissolve

    f "{size=-10}It’s only a problem because it {i}is{/i} you...{/size}"
    s "Hm? What was that?"

    scene futabarevision7
    with dissolve

    f "Oh! Umm...nothing! "
    f "Just...please go wait in the hall for me."
    f "I’ll get changed and...be back in a moment."

    scene black
    with dissolve2

    "I exit the room, but my mind stays put to watch one of my students undress."
    "She’s thinking about me right now. She has to be."
    "It only makes sense for her to be thinking about me when I’m right here and she is right there, hastily removing her pants so I’m not kept waiting long."
    "I would help her if she’d only ask."
    "Just like with writing, I would teach her all there is to know about love in its most bestial, physical form."
    "I think the same things about her that she thinks about me."
    "But I am different."
    "I would indulge in my desires."
    "And she would rather bring form to her flaws than allow me to peel them back like underwear, stuck to the damp petals of a flower unplucked from its original garden."

    s "..."

    "Hurry up and finish before I return to the depths."

    "........."
    "......"
    "..."

    scene futabarevision14
    with dissolve2

    "We eventually make our way outside and I am able to force away the urge to undress her on my own."
    "I don’t know where her mind ends up, but based on the nonexistent distance between her right arm and my left, I think I may have won the race toward the fleeting purity of this blossoming connection."
    "The petals are mine to pluck as soon as the flower finishes blooming."
    "Oh, if only spring would come tonight."

    f "..."
    s "..."
    f "The..."
    f "The character in my story isn’t...an {i}exact{/i} representation of me, you know..."
    s "I still haven’t met the new version, so I’ll hold my comments until I do."
    f "And I..."
    f "I want you to know that...I don’t think you’re as flawed as you suggested earlier."
    f "I think you’re really amazing, Sensei. And...it probably sounds silly, but...I wouldn’t trade even moments like this one for anything."
    s "I see."
    f "Y...Yeah..."

    scene futabarevision15
    with dissolve

    f "I guess I...just wanted you to know that before the night comes to an end..."
    s "Then I’ll say the same thing to you."
    s "You’re not even half as flawed as you think you are."
    f "Have you stopped to think that...maybe I just haven’t been revised yet?"
    f "You haven’t seen the flaws because...they haven’t been added into my story yet."
    f "Who’s to say if you’ll still be saying things like that when they are?"
    s "Hm."

    scene futabarevision14
    with dissolve

    s "Well, the same goes for me, I guess."
    s "Here’s hoping we don’t wind up hating each other once we learn a little more."
    f "You’d...have to do something {i}really{/i} bad to get me to hate you, Sensei..."
    s "I’m sure I will eventually."
    f "So...until then..."
    f "Is it okay for me to stay with you like this?"
    s "Like what, exactly?"
    f "..."
    s "..."
    f "Don’t worry about it..."
    f "It would just make me sound dumb if I said it out loud."
    s "Then write it down. You’re getting pretty good at that now, aren’t you?"
    f "Maybe, but..."
    f "I think that some thoughts are just better left as daydreams."

    scene black
    with dissolve2

    "Neither one of us speaks another word for the next ten minutes, but there is a silent understanding that we’re both here because we want to be."
    "And that we’re both much uglier than we want to be as well."
    "Somewhere around the eleventh minute, our arms stop touching."
    "Somewhere around the twelfth, Futaba heads back inside."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ futabanew1 = True
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label futabanew2:
    scene futabanewtwo1
    with fade
    play music "phantomthief.mp3"

    "I toss aside a stack of papers that Makoto wanted me to go over after taking one look at them and deciding that I have much better things to do with my time."
    "I can not risk being distracted by clerical work when there are so many girls in my class that could need assistance at any given moment."
    "Now, I understand and acknowledge that most of the girls in my class {i}do not{/i} actively seek out my assistance when it comes to personal issues..."
    "{i}But what if they did?{/i}"
    "I’m sure Makoto will understand my decision to just let her handle all of this instead of doing it on my own when it’s for the sake of her classmates."

    play sound "knock.mp3"

    "Look, here’s one of them now."
    "Unless..."

    s "I’m doing them right now, Makoto. Don’t worry."
    f "Umm...it’s actually Futaba. Is it...okay if I come in?"

    "Woah. I guess someone actually {i}does{/i} need my help today?"
    "I suddenly feel a lot better about neglecting my responsibilities. "

    s "Sure. Just don’t tell the class representative that I’m irresponsible."

    scene futabanewtwo2
    with dissolve
    play sound "dooropen.mp3"

    f "Irresponsible when it comes to what, exactly? I’m not...interrupting something, am I?"
    s "Nothing that I actually wanted to do, so I wouldn’t worry too much about it."
    s "But anyway, is something wrong? Or are you just dropping by because you miss me?"

    scene futabanewtwo3
    with dissolve

    f "I...wouldn’t do that. You’re probably far too busy for me to drop by just because I want to see you."
    s "I find it surprising how you can say that despite the many times I have dropped by your dorm room specifically because I did {i}not{/i} have anything to do."
    f "It’s a little different when you’re the one who comes to me...Especially since you never intend to burden me when you do."
    s "Ahh. So you intend to burden me today?"

    scene futabanewtwo4
    with dissolve

    f "Maybe...just a little bit."
    s "Yumi again?"

    scene futabanewtwo2
    with dissolve

    f "How did you know?"
    s "Because she’s the only thing that ever lands you here. What did she do this time?"

    scene futabanewtwo3
    with dissolve

    f "Thankfully not much since Ayane showed up and...I guess convinced her to leave me alone for the time being. "
    f "But she...umm..."
    f "Well, let’s just say she was a little more assertive than usual and...I was a little more {i}defenseless{/i} than usual as well."

    "It’s nice hearing that Ayane is going out of her way for Futaba as well- but I guess I’m not that surprised to hear it since she seems like the type to step up and intervene in something like that."
    "If I could be everywhere at once, I’d have no issue with becoming a sort of personal bodyguard for Futaba or...whoever else Yumi decides to fuck with on any given day."
    "Unfortunately, sometimes it feels like I’m barely even in {i}one{/i} place at once. So relying on other people to make up for my inability to involve myself is just...something I have to do every once in a while."

    s "What was it that made you more defenseless, if you don’t mind me asking?"
    s "Did she barge into your room or something like that?"

    scene futabanewtwo5
    with dissolve

    f "Well, no...umm..."
    f "This actually happened in...the shower room after gym class one day..."
    s "..."

    "Perhaps I should find a way to make myself more available after all? "
    "If Futaba needs someone to protect her while she is completely naked, I should be the one to step up so Ayane doesn’t have to anymore."
    "That’s simply the right thing for me to do as her teacher."

    s "Are you worried she’s going to do it again? Because if things are progressing to the point where she’s cornering you in the showers-"

    scene futabanewtwo6
    with dissolve

    f "I...well, I {i}know{/i} she’s going to do it again because...she’s Yumi and I’m {i}me.{/i} And I’m not asking you to...discipline her or anything like that since...I don’t know if it’s something she can control."
    f "I just..."

    scene futabanewtwo7
    with dissolve

    f "I guess I...I’m just being selfish and...wanted to hear you console me...and tell me that she’s wrong again."
    s "I feel like I’ve been doing that a lot lately."
    f "You have...Which is why I said I’ll be burdening you a little bit today..."
    s "Futaba, if repeatedly consoling you is actually going to help you here, I’ll do it. But, based on how you’re still coming to my office seeking the same thing-"

    scene futabanewtwo8
    with dissolve

    f "I’m sure it sounds weird to you, but...at the same time...have you ever gone through something like this, Sensei?"
    f "Where...someone you don’t have any problem with has more problems with you than you can count?"

    scene colorbars
    stop music
    $ renpy.pause(5, hard=True)
    scene futabanewtwo8
    play music "phantomthief.mp3"

    s "No."
    f "See? I didn’t think so..."

    scene futabanewtwo3
    with dissolve

    f "You’re...naturally good looking, and..."
    f "I guess what I’m saying is that you’d think that I’d be immune to things like this for as long as I’ve put up with them, but..."
    f "I don’t know. "
    f "The only thing that ever works is being reminded by someone else that the Futaba Fukuyama that Yumi sees..."
    f "That the Futaba Fukuyama that {i}I{/i} see is the one that’s actually twisted."

    scene futabanewtwo8
    with dissolve

    f "So, I’m sorry again for the inconvenience as I really don’t want to trouble you...but today was one of those days where I just wanted to be reassured."
    s "..."
    f "...Sensei?"
    s "Sorry, yeah. I’ll reassure you whenever you want. "
    s "I just wish there was something more I could do."

    scene futabanewtwo9
    with dissolve

    f "Don’t. You’re already doing a great job, Sensei. It’s {i}me{/i} who needs to figure out something else to do."
    f "Positive reinforcement can only carry a person so far..."
    f "Did you know I actually used to be pretty skinny? It was a really long time ago...before I even met Rin...but there was a time where people would say things like, “You need some more meat on your bones.”"
    f "Things like that. Things that I’m sure tons of the girls in our class hear even today."
    f "But...the craziest part was that even back then, I didn’t believe them. Not one bit."
    f "In fact, I still have trouble believing them. And if it weren’t for me being able to look back at those pictures...and see with my own eyes how badly things have changed..."
    f "I think I’d still probably say that I’ve been this way forever."
    s "..."
    f "..."

    "Futaba’s eyes lock on mine but don’t do any amount of justice in showcasing the pain she feels inside."
    "I want to relate- I do. But without even being able to remember anything more than a few months back, how could I possibly do that?"
    "Is positive reinforcement seriously the only thing I can do for her? Because, as it stands, my words are nothing more than bandages over bullet holes."

    s "I don’t really know what to say here, Futaba."
    f "I wasn’t looking for a response this time...I just wanted to share a little more about myself."

    scene futabanewtwo10
    with dissolve

    f "Us writers call that {i}character development.{/i}"
    s "Look at you, calling yourself a writer before even finishing the story I assigned you. That’s the kind of confidence I want to see more of."
    f "Heheh! This confidence was a gift from you, Sensei. Without your help, I wouldn’t even be strong enough to say that yet."
    s "Well, here’s hoping you wind up getting strong enough to look at yourself differently in other areas as well."
    s "Do you really not want me to do anything about Yumi, though? Because as much knight-potential as Ayane has, I still think that role is better suited for someone like me."

    scene futabanewtwo9
    with dissolve

    f "If I become {i}completely{/i} dependent on you, I’ll never get anywhere in life..."
    f "Besides, I like Yumi. I’ve watched her stick up for Chika before when girls from another class were saying mean things about her. There’s definitely a heart in there."
    f "And who knows? Maybe her being mean to me is just...her equivalent of me coming to you for encouragement and motivation?"
    s "That’s certainly one way to look at it. Though, it’s not one I’m really sure I agree with."

    scene futabanewtwo10
    with dissolve

    f "Maybe you could give Yumi some encouragement as well then? If she ever finds herself in your office without being forced in, of course."
    s "Yeah, I have a good feeling that would somehow make things with Yumi and me even worse. So I’ll just keep complimenting you instead and we’ll see where that takes us."

    scene futabanewtwo9
    with dissolve

    f "Thank you, Sensei. And I’m sorry again for taking up so much of your time for something so...unimportant."
    f "Do you...umm..."

    scene futabanewtwo3
    with dissolve

    f "Do you have any plans after this? Or would you maybe want to...walk home together?"

    scene futabanewtwo11
    with dissolve

    f "A-And by “home,” I obviously mean the dorm! I wasn’t asking to come back to your house if...if that’s how it sounded!"
    s "Are you sure? Because I wouldn’t mind bringing you over to my place as long as we can figure out a cover story to give Ami."

    scene futabanewtwo12
    with dissolve

    f "Wh..."
    f "What would we...do at your house, exactly?..."
    s "..."
    f "..."

    scene futabanewtwo11
    with hpunch

    f "F-Forget I asked! That sounded...extremely inappropriate! Please just...walk me back to the dorm!"
    f "If that’s okay, I mean! I completely understand if something like that is-"
    s "I’ll walk you back, don’t worry. It’s about time for me to leave anyway."

    scene futabanewtwo2
    with dissolve

    f "It is?...Did I really take up that much of your time?"
    s "Yes. But, in doing so, you not only prevented me from filling out some paperwork I definitely didn’t want to touch, but allowed me to use my office for its actual purpose."
    s "That doesn’t happen very often around here."

    scene futabanewtwo9
    with dissolve

    f "Well..."
    f "I guess we both got something out of today then..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene futabanewtwo13
    with dissolve2

    "Futaba and I exit my office together and begin to make our way to the lockers so she can switch shoes and gather her things."
    "There’s still a fair amount of girls in the school, likely on their way to club meetings or friendly gatherings, but it’s not like being seen with a student while still on school grounds is going to make {i}me {/i} look bad."
    "In fact, as long as I don’t run into anyone from class who accuses me of favoritism for spending time with Futaba instead of them, I think today may actually end pretty smoothly."

    s "Futaba, I am sorry in advance."
    f "Hm? Sorry for what?"
    s "I believe I may have just jinxed us in one of my inner monologues."
    f "As sad as it is for me to admit this...life isn’t a book, Sensei. You can’t just foreshadow events in real life by just thinking things and-"

    scene futabanewtwo14
    with dissolve

    mi "What the heck is this?! Sensei and Futaba hangin’ out after school?! Without invitin’ me along?!"
    mi "I demand an explanation right now!"

    scene futabanewtwo15
    with fade

    mi "Just kiddin’. I’ve got soccer practice with the gang, so I wouldn’t be able to hang out with you guys anyway."
    s "Hey, you two. Why haven’t you gone home yet?"

    scene futabanewtwo16
    with dissolve

    mi "Are you not payin’ attention to me at all?! I just told ya I have soccer practice!"
    mi "Stop focusin’ on Futaba’s melons and listen to me! Small girls need love too! Ain’t that right, Sana?!"
    sa "I...don’t want to be involved in...that kind of conversation..."
    s "Why haven’t {i}you{/i} gone home, Sana? I already know Miku has a meeting for the home economics club or whatever it is she’s in."
    mi "I am wearin’ my friggin’ uniform! You know darn well what club I’m in, Sensei!"
    sa "I’m just...waiting for Ayane to finish cleaning the classroom."
    sa "What...um...what are...you two doing together?"

    scene futabanewtwo17
    with dissolve

    f "I was just...bothering Sensei in his office with some...personal problems."
    mi "Personal problems? You doin’ okay, Futaba? Wanna rest your head on my shoulder without the fear of whatever the cops would do to Sensei if they saw you doin’ that to him?"
    s "Hey."
    f "Oh, no. I’m fine now. It was...really stupid anyway."
    mi "Well, stupid or not, I-"

    scene futabanewtwo18
    with hpunch

    a "HEY! WHAT’S THE BIG IDEA?! WHY ARE YOU STILL IN SCHOOL WITH GIRLS WHO AREN’T ME?!"
    mi "Hah...uhh...maybe...tone it down a bit before ya just sneak up behind people and start yellin’ stuff, Ami?"

    scene futabanewtwo19
    with dissolve

    a "Was this {i}your{/i} idea, Miku? Are you trying to steal my uncle from me now too?"
    mi "Huh? I was just talkin’ to Sana before soccer practice. Futaba’s the one you’ve gotta be worried about when it comes to stealin’ Sensei away."

    scene futabanewtwo20
    with hpunch

    a "Traitor! How dare you skip our club meeting to start an affair!"
    f "What?! This isn’t like that at all!"
    m "She literally told us she was going to Sensei’s office before the meeting started."
    a "Does this look like an office to you, Maya?! Because it sure as heck doesn’t look like an office to me!"
    f "That’s...I just...needed some help from Sensei about...some personal matters..."

    scene futabanewtwo21
    with dissolve

    a "Personal matters? Is it anything we can help with?"
    m "Well, you sure got over that quickly."
    f "No, it’s..."

    scene futabanewtwo22
    with dissolve
    stop music fadeout 10.0

    f "Um...I’m not really sure how to word it without...making it seem like I’m taking it out on {i}you.{/i}"
    a "On me? Did I do something wrong? Cause if this is about the yelling thing, that was pure instinct and I can’t really help it and I am sorry."
    f "No, no. Not {i}just{/i} you, Ami."
    s "Futaba?"

    scene futabanewtwo23
    with dissolve

    f "{i}All{/i} of you..."

    play sound "static.mp3"
    scene futabanewtwo24 with flash
    scene futabanewtwo23 with flash
    scene futabanewtwo24 with flash
    scene futabanewtwo23 with flash
    scene futabanewtwo24 with flash
    scene futabanewtwo23 with flash
    scene futabanewtwo25 with flash
    stop sound

    f "I’m sorry! I actually forgot I had...something else to do today."
    f "Thank you for your help, Sensei. "
    f "And...I’m sorry to everyone else for having to leave so soon."
    f "Thank you...for your concern."

    play sound "static.mp3"
    scene futabanewtwo24 with flash
    scene futabanewtwo26 with flash
    stop sound

    mi "..."
    sa "..."
    a "..."
    m "..."

    scene black
    with dissolve2

    "Autumn came, and the leaves in the forest turned to orange and gold."
    "Then, as winter approached, the wind caught them as they fell."
    "It is only with the heart that one can see clearly, for the most essential things are invisible to the eye."
    "The scent of chlorine and porcelain has never smelled as beautiful as it does now."
    "The end."

    $ renpy.end_replay()
    $ futabanew2 = True
    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "{i}Her appetite has decreased by 5.{/i}"
    "........."
    "......"
    "..."


    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label futabanew3:
    play sound "knock.mp3"
    stop music

    "I knock on Futaba’s door and the video game breaks."

    play sound "static.mp3"
    scene insertredux3 with flash
    scene futabanewtwo24 with flash
    scene insertredux4 with flash
    scene anotherfutabaevent1 with flash
    stop sound
    play music "icantseeher.mp3"

    "The theme for a girl I have yet to meet slips down the holes inside of my head called “ears” and works its way throughout my body, getting caught on a variety of hairs and other things you typically find in bodies."

    play sound "knock.mp3"

    "I knock again because Futaba is glitched and I must brute force Lessons in Love back into doing what I want it to do. "

    play sound "knock.mp3"

    "No matter how many times I knock, though, she remains tucked in the corner behind a circular shadow, staring at the wall and waiting for its paper to wrap around her."
    "I long to wrap myself around her the way she wishes the paper would but, unfortunately, that will not be an option I have until later."

    play sound "knock.mp3"

    "A GIFT RAINS DOWN UPON YOU"

    play sound "jackpot.mp3"
    scene anotherfutabaevent2
    with flash

    "YOU HAVE RECEIVED AN [[incomplete Futaba]"

    f "Let’s party!"
    s "I don’t want to party. I am here to check on your writing assignment and learn more about why you avoid mirrors."
    f "Leeeeeet’s party!"
    s "Futaba, stop it. And tell your T-posing clone to go away too."

    scene anotherfutabaevent3
    with dissolve

    f "{b}Let’s party!{/b}"
    s "Ugh..."

    "Welp, looks like it’s going to be another hectic night for me."
    "And here I was thinking Futaba was exempt from duplicating or getting caught in glitches."

    f "Let’s-"
    s "Shut the fuck up for a second. I don’t want to party and I’m trying to make the game go back to normal."

    play sound "pop.mp3"
    scene anotherfutabaevent4

    f "Party now! Party now! Party now!"

    "I begrudgingly remove a collapsible party hat from my back pocket and stick it on top of my head, hoping that its juices quickly dissolve into my skull because I really don’t have time for this right now."

    s "Your story-"
    f "YOU WORRY TOO MUCH ABOUT THE STORY. "
    f "WE NEED TO HAVE FUN SOMETIMES TOO, SENSEI!"
    f "ISN’T THE FUN OVERDUE, SENSEI?! "
    f "DON’T YOU WANT TO TOUCH MY FAT FUCKING TITS, SENSEI?"
    s "Futaba, please. Not at the party."
    f "DO IT. DO IT, YOU FUCKING WORM."
    f "I’M NOT SCARED. I’M READY."
    f "MY AFFINITY FOR YOU GROWS LIKE A REDWOOD AND YET YOU SIT IDLY BY AND WATCH."
    f "YOU FAVOR ME. "
    f "YOU FAVOR ME WHEN YOU KNOW I WILL DO ANYTHING TO MAKE YOU LIKE ME."
    f "PEEL AWAY THE THIN LAYERS OF FABRIC THAT COVER THE PARTS OF ME I HAVE SAVED FOR YOU."
    f "PLUCK MY PETALS."

    "My pants suddenly tighten but I’m worried about making any moves due to the extra Futaba still hanging out in the corner of the room, even if her head is now obscured by a fun party banner."

    play sound "static.mp3"
    scene anotherfutabaevent5 with flash
    stop sound
    stop music

    "When I blink, it all disappears and I realize that no time has passed at all."
    "I should probably knock on Futaba’s door because that is why I am here."

    play sound "knock.mp3"

    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."

    scene anotherfutabaevent6
    with dissolve
    play sound "dooropen.mp3"

    f "Sensei?"

    play music "sweetvermouth.mp3"

    s "Hello."
    f "Is...everything okay? I thought I heard someone outside of the door, but...I figured it was just Miku trying to mess with me again."
    f "Were you...about to knock? Or are you just passing by?"
    s "This isn’t really a place I can just “pass by.” And besides, I {i}did{/i} knock. A bunch of times, actually."

    scene anotherfutabaevent7
    with dissolve

    f "You did? I’m so sorry then...I must not have heard."
    s "{s}DON’T LET IT HAPPEN AGAIN, YOU FUCKING CUNT{/s} It’s fine. Don’t worry about it."
    s "Hey, are you doing anything right now?"

    scene anotherfutabaevent6
    with dissolve

    f "Right now? No...I was about to go take a shower, but...I suppose I can wait until you’re gone."
    s "Great. Do you want to go somewhere darker with me?"
    f "Umm...darker?"
    s "Somewhere far away."
    s "I can’t be here right now."

    scene anotherfutabaevent8
    with dissolve

    f "Sensei...if you want to talk about something, I-"
    s "Are you coming or not?"
    f "..."
    s "..."

    "Futaba thinks long and hard about whether or not she wants to put her faith into a man who would trade it all away for a mouth to cum inside of."
    "In several seconds, she will make the wrong decision."
    "And the two of us will embark on a hot, sweaty journey across this make-believe world together. "

    scene anotherfutabaevent9
    with dissolve

    f "We can go wherever you’d like..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "That’s right."
    "We can go wherever I’d like."
    "None of this is real. "
    "Anything that I have convinced myself I’ve felt as of late is nothing short of cowardice."
    "Futaba Fukuyama is a naive teenage girl who is doing her best to appeal to me in ways deeper than her skin, but her skin alone is what I want."
    "I want the scent of lavender to stain my bedsheets."
    "I want my skin underneath her fingernails."
    "I want her."
    "I want her I want her I want her I want her."
    "And that is exactly why I can’t be here right now."
    "Because if the two of us remained here, I would take her with the minimal amount of force I am sure it would require."
    "I lead her out into the night in an attempt to mask my shadow with something darker."
    "She follows suit, blushing and bouncing."
    "........."
    "......"
    "..."

    scene anotherfutabaevent10
    with dissolve2
    play music "merrychristmasmrlawrence.mp3"

    "We end up somewhere not at all familiar to me. "
    "I don’t know how long it took the two of us to get here or the space between where we stand right now and where Futaba will rest her head tonight..."
    "But I’m not too worried."
    "Because the uncertainties inside of me have managed to fade like the dull colors of the traffic lights around us, incessantly cycling between “go” and “stop” and not offering anything in between."
    "It reminds me a little of myself, but not in a good way."
    "Lately, I have found myself getting so caught up in the depths of my mind that, sometimes, I’m shocked I’m able to crawl out at all."
    "I never know when it’s happening."
    "In fact, a lot of the time, I don’t even know when it’s over."
    "But when everything about this life is still a blur to me, even now, I can’t help but come unglued."
    "What is real?"
    "What is not?"
    "And what substance is being used to keep me grounded? Because it is very clearly not working if I’ve managed to make even Futaba uncomfortable tonight."

    scene anotherfutabaevent11
    with dissolve2

    s "Can I ask you something, Futaba?"
    f "Of course. Though...it’s a little worrying to have you {i}ask{/i} to ask me rather than just ask me outright."
    s "Are you scared of me?"
    f "Scared?"
    s "This isn’t normal...Coming to your room in the middle of the night and standing outside your door...Dragging you with me to some part of town I’ve never even seen before..."
    s "And all for nothing, too."
    f "It’s not nothing, Sensei. You didn’t want to be in the dorms, right?"
    f "And I’m assuming...you didn’t want to be at home either."
    f "I don’t know if I’m just the lucky one who managed to open her door and find you first tonight, but..."
    f "I’m not scared of you."
    s "Well, you should be."
    f "Why do you say that?"
    s "I don’t know."
    s "I just think that you’re supposed to be scared of me."
    f "Hmm...Well, I don’t think that’s a very compelling reason. So I think I’ll just remain unafraid, if that’s okay with you."
    s "What will it take to make you scared of me?"
    f "You’re starting to sound like you {i}want{/i} me to be scared of you."
    s "I...don’t think that’s the case. "
    s "I just don’t understand why you...or anyone else for the matter, is just {i}okay{/i} with me doing the things I do when they’re so clearly wrong."
    f "I think...the answer to that might be a little more boring than you expect, Sensei."
    f "We simply...don’t think the things you do are wrong."
    s "Then you’re all just as lost as I am."
    f "Maybe we are..."
    f "But we trust and respect our guide."
    f "And...I may not be able to speak for anyone else...but I don’t think that part of me will ever change."
    s "..."
    f "I might not be the type of heroine you’d enjoy to read about in a story, Sensei..."
    f "But..."
    f "I think I make a pretty good supporting character."
    f "And I’ll support you in any way you want...because {i}that’s{/i} how much I trust you."
    s "You’re making a mistake."
    f "Heheh~"
    f "We’ll see about that..."

    scene black
    with dissolve2

    "We make our way up the incline and disappear down an alleyway because even the light of the moon is too bright for me to properly hide right now."
    "I don’t understand Futaba at all. I don’t understand why she’s okay with me or why she’d even go as far as calling me her {i}guide{/i} when I am merely one dark passage away from stealing something precious to her."
    "There are no cars this late at night. None near us at least."
    "Everything is perfectly silent apart from Futaba’s boots making contact with the ground."
    "It gets colder as we get higher."
    "I haven’t felt a chill like this in a long time."

    scene anotherfutabaevent12
    with dissolve2

    f "Huh...I think we’re actually getting kind of close to one of the edges of Kumon-mi..."
    s "We’re not in some sort of...restricted area or something, are we?"
    f "Have you never seen the barrier up close before, Sensei?"
    f "I went with a friend of mine once. We wrote our given names on the wall just last year...right before I started high school."
    s "Is this the same friend I’ve heard you talk about before?"
    f "It is. And it’s probably safe to assume she’s the one I’m talking about whenever I don’t say “Rin,” since those two are basically my only good friends. "
    f "Unfortunately, the part we wrote on is miles away from here. And, honestly, I don’t even know if I’d be able to find it or if...these walls are ever cleaned."
    s "Should we write our names on the wall as well?"

    scene anotherfutabaevent13
    with dissolve

    f "Maybe. Come to think of it...I don’t even know your real name."
    s "I’d just write “Sensei” anyway. As far as I’m concerned, that {i}is{/i} my name."
    f "Do you really want to go? It’s {i}really{/i} big up close. But I guess that’s to be expected since the whole point is to isolate us in the first place."
    s "Not to be a downer, but a trip to a giant wall doesn’t sound like much fun. I was just kidding about writing our names down anyway."

    scene anotherfutabaevent14
    with dissolve

    f "I guess I’m just a little gullible then."
    f "But, um...if we’re {i}not{/i} going to keep going until we reach the end...would you mind if we took a little break soon?"
    f "It goes without saying, but...I’m not really...um...one of the {i}fittest{/i} girls in the class and...we’ve been walking for a while now."
    s "Sure. We’ll stop at the next bench we see and head back home after that."

    scene anotherfutabaevent13
    with dissolve

    f "Are you okay with that? Going home, I mean."
    s "Of course. I’m completely fine."
    s "I just felt like walking tonight...and what better place to walk than some random, dimly lit area near a giant wall?"
    f "Heheh...right. What better place indeed."

    scene black
    with dissolve2

    "Alley after alley, light after light...our journey continues and somehow manages to grow even colder than I had mentioned it being just moments ago."
    "I guess that even summer has nights like that."
    "Despite the drop in temperature, I am never once tempted to reach for Futaba’s hand and warm it using my own."
    "I’m tempted to do plenty of other things of course...and perhaps I even would if it were not for the infectious smile that she’s yet to abandon even once since setting out into the night with me."
    "Maybe I {i}do{/i} want her to fear me?"
    "Maybe the fear is what compels me to act at all?"
    "And maybe, if I can wipe that smile off of her face-"
    "I can spare her from the agony I am sure she will endure because of me."
    "Maybe not tonight."
    "Maybe not the next."
    "But one day, everything around her will come crashing down."
    "And chances are...when she looks up...I will be towering over her and the remnants of all that she loves."
    "With a hammer in one hand-"
    "And the base of my cock in the other."

    scene anotherfutabaevent15
    with dissolve2

    f "Umm...forgive me for asking this, but...have you been intentionally looking away from me all night? Or is that just...happening on accident?"
    s "I haven’t really been thinking about it."
    f "I see..."
    s "..."
    f "You..."
    f "You can look at me, you know?..."
    s "..."
    f "..."

    scene anotherfutabaevent16
    with dissolve

    s "..."
    f "..."

    "I turn to look at Futaba."

    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene happy5 with flash
    scene anotherfutabaevent17 with flash
    stop sound

    "But she melts into a puddle of goat’s milk that I can’t help but lap up with my clam’s tongue."

    f "There...don’t you think it’s easier to have a conversation when we’re both looking at each other?"

    "No."

    f "Now...is there anything you want to talk to me about, Sensei?"

    "No."

    f "Is there...anything you want {i}me{/i} to talk to {i}you{/i} about?"

    "No. "
    "No no no no no."

    f "Is there..."
    f "Anything you want to me to {i}do{/i} to you?"

    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene happy5 with flash
    scene anotherfutabaevent18 with flash
    stop sound

    "Yes."

    f "..."
    s "..."
    f "Is something wrong?"
    s "I..."
    s "I can’t tell if what I just heard was actually real or not."
    f "What did you hear, exactly?"
    s "Something that if I {i}didn’t{/i} hear and said out loud would cause a lot of problems for both of us."
    f "Then..."
    f "I guess you heard correctly."
    s "..."
    f "..."

    scene anotherfutabaevent19
    with dissolve

    f "U-Unless I...completely misunderstood something!"
    f "Which, knowing me and my...no experience with boys...is extremely possible..."
    f "If that’s the case...please forget that I said anything and...please forget how extremely inappropriate it would be for me to even {i}suggest{/i} that-"
    s "Futaba."

    scene anotherfutabaevent20
    with dissolve

    f "Um...Y...Yeah?"
    s "Are you sure?"
    f "..."
    s "..."

    scene anotherfutabaevent21
    with dissolve

    f "I..."
    f "I want to do everything I can to make you feel better, Sensei..."
    f "And if you’re not the type who wants to talk about problems..."
    f "Maybe I can...make you feel better in other ways?"
    f "After all, it’s...it’s not like I haven’t been thinking about that kind of stuff. "
    f "In fact...ever since you...admitted to being...a...aroused by me in my room...I’ve had trouble...{i}not{/i} thinking about it."
    s "..."
    f "..."

    scene anotherfutabaevent22
    with dissolve

    f "Would...something like that actually make you happy, Sensei?..."
    s "..."
    f "..."

    scene black
    with dissolve2

    s "Yes."

    "I lie as if it’s second nature, disguising my true feelings with yet another glance in the opposite direction."
    "That must be the thousandth tonight."
    "Futaba does not say anything after that. She simply nods- like she’s accepting a task as standard as cleaning the chalkboard or taking out the trash. "
    "She books us a ride back to the dorm on her phone, using money her parents sent her so she can perform a sexual favor for her teacher in the comfort of her own room."
    "I’m sure they would be proud."
    "The car arrives- it’s the first one I’ve seen tonight."
    "When the two of us get inside, I sit closer to her than I did on the bench."
    "I reach for her hand while she’s not looking and place it in my lap."
    "She jumps, but understands what I want."
    "What she doesn’t understand is that it won’t make me happy."
    "It will just make me a little less numb."

    $ renpy.end_replay()
    $ futabanew3 = True
    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump futabadorm15

label futabadorm50:
    play sound "knock.mp3"

    "I knock on Futaba’s door and wait for her to answer."

    no "Whooooo is it?~"

    "But instead, I am greeted by Nodoka- a person I’ve yet to deal with since the Yumi incident. "
    "And while I wasn’t planning on reconciling with her tonight (Nor do I know if “reconciliation” would even be applicable here in the first place), leaving now seems kind of...out of the question."
    "I’ve knocked on this door enough by now that I’m sure Futaba would be able to pick mine out of {i}hundreds{/i} of other knocks."
    "And assuming Nodoka doesn’t have her tied up and nude right now, she’s probably expecting me to come inside and not just fake her out by announcing my presence and immediately running away."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I sigh to myself as I open the door, knowing full well that the type of person I am disallows me from avoiding anyone- particularly girls I want to have sex with."
    "And even though Nodoka’s last showing was, in no way, something I respect or would have done myself, I still do {i}like{/i} her."
    "And Futaba must as well if she’s still letting her get that close."

    scene futabanodokadorm1
    with dissolve2

    "I guess the chances of Futaba knowing what {i}actually{/i} happened are rather slim, though, as I doubt she’d lend her shoulder to a sexual assailant."
    "To her, it just looked like Nodoka was attacked out of the blue."
    "But the blue in this case is just so deep and dark that it’s hard to really decipher what that means. And no one has the time to go digging for something that is already peeking out of the surface."
    "She found her own answer. And even though it is the wrong one, who would I be to take that from her when possessing it allows her to feel as comfortable as this?"
    "Because this is far more comfortable than she ever appeared under the weight of an aggressor. "

    no "Futaba, look. Papa is home."
    no "Do you think he brought any sweets for us to share? Or do you think perhaps we {i}are{/i} the sweets...and he has come to devour us whole?"
    f "I think that...the latter is probably closer to being true. I don’t know if I’d use the word “devour,” though..."
    no "Which one of us will you have first, Sensei? And what will become of the one who’s forced to watch?"
    s "I didn’t realize you’d be here as well, Nodoka. How are you feeling?"

    scene futabanodokadorm2
    with dissolve

    no "Why, I feel closer to Heaven than I’ve ever felt before. If you’d come any earlier, you may have even seen my childhood friend here performing {i}special{/i} services both for and {i}on{/i} me."
    s "Futaba, if you’ve been bisexual this whole time, you should have lent Rin a hand. Getting some of that pent-up energy out of her could have potentially saved her from a bad decision or two."

    scene futabanodokadorm3
    with dissolve

    f "I’m sorry to break it to you, but that’s...not what Nodoka was alluding to..."
    f "I just gave her a little massage. That’s all."
    no "Happy ending and all."
    f "It was just a normal ending. Please don’t listen to her."
    s "Well, I guess it’s good to see you’re both okay. I was a little worried that Nodoka may have lost some of her memories and that {i}you’d{/i} still be in pieces somehow blaming yourself for what happened."

    scene futabanodokadorm4
    with dissolve

    f "I mean...it’s kind of hard {i}not{/i} to. What other common ground do Yumi and Nodoka even share? It pretty much {i}has{/i} to be something involving me, doesn’t it?"
    s "Do you think Yumi would really go that far just to bully someone?"
    f "I..."

    scene futabanodokadorm5
    with dissolve

    no "Of course she would. People like that don’t need a reason for {i}anything{/i} they do. They act on impulse...{i}instinct.{/i} "
    no "And sometimes, those animalistic tendencies wind up showing the best of us. Wouldn’t you agree?"
    s "I’m not sure if I follow."
    no "Then perhaps a little question is in order?"
    no "If an animal is coated in its own blood with its innards splayed out across the forest floor, is {i}it{/i} the one deserving of the blame for its fate to be devoured?"
    no "Or do we shun the ravenous horde that feasts upon the flesh, converting the weak into sustenance? The sustenance into progression."
    s "Do you really think it’s accurate to be comparing yourself to a dying animal?"
    no "Silly Sensei. It appears you’ve gotten my little metaphor backwards."
    f "I don’t really...get any of this stuff about animals and predators, but..."
    f "I don’t think it would be {i}impossible{/i} for Yumi to do something like that..."

    scene futabanodokadorm6
    with dissolve

    f "What do you think, Sensei? You’ve been spending more time with Yumi lately, haven’t you? "
    f "Do you know something that may have...set her off? "

    scene futabanodokadorm7
    with dissolve

    no "Yes...{i}do you{/i} know of something like that, Sensei? Because it would have to be {i}pretty bad{/i} to warrant a beating like the one I received, wouldn’t it?"
    s "Yeah...I imagine it would. But I think you’d know a little better about what that could be than me, wouldn’t you?"
    no "Mmm...I don’t think so? I’m just as confused as you are."
    s "So you {i}haven’t{/i} gone out of your way to provoke her behind Futaba’s back and seek vengeance on her behalf?"

    scene futabanodokadorm8
    with dissolve

    f "You didn’t...actually do anything like that, did you?"
    no "Not that I can recall. But, if you’d like my two cents, I don’t think there’s {i}anything{/i} I could have done to that girl that could make up for all the pain she caused you."
    f "It’s true that Yumi hurt me...a lot...and that I’ve always been really afraid of her...but I wouldn’t want {i}her{/i} to suffer as well just because of that."
    no "Yes, because you’re a genuinely good person amidst a sea of evil ones. A person who would give up her own flotation device to save the life of the man who sunk the ship."
    no "How unfortunate it is that the best among us must suffer the most while the worst are revered for their efforts in bettering themselves. "
    no "What good is planting one tree in a forest you razed yourself?"

    scene futabanodokadorm9
    with dissolve

    no "Unfortunately, Sensei and I can’t relate to that as the two of {i}us{/i} have razed our share of forests as well. "
    f "I don’t...think either of you are anything like that. I can’t imagine you ever doing anything to purposely hurt someone."
    no "But if we did...if we {i}did{/i} hurt others in the same fashion Yumi hurt you...how would your thoughts of us change?"
    no "Would you still invite us into this room with open arms? Lend us your bosom when we long for something to cry into?"
    no "Or would you search for someone a little “better” to hand off your flotation device to?"

    scene futabanodokadorm10
    with dissolve

    no "All things considered, I’d like to remain floating with both of you as this shared company injects life back into this slowly rotting heart of mine. "
    f "Don’t say things like that about yourself, Nodoka...you know I don’t like that."
    no "Apologies, bestie. The day I do something to hurt you is the day I breathe my last."

    scene futabanodokadorm11
    with dissolve

    no "But I suppose I’ve overstayed my welcome tonight as there is a large man hovering over us who very much would like to revel in that bosom I spoke of just seconds ago."
    f "You know that...we don’t always just...{i}you know...{/i}"
    no "Oh, I know. But the fact that it happens at all fills me with a breed of jealousy I have a hard time finding the words to describe."
    no "And I also have some...{i}errands{/i} I must run."
    no "How lucky you are, Sensei. Being able to {i}take{/i} whatever you want without consequence while the rest of us struggle endlessly in pursuit of that same fruit."
    no "You’re truly a role model, you know? And I hope with all of my rotting heart to one day drink from the same overflowing chalice that rests in your hands."

    scene futabanodokadorm12
    with dissolve

    no "Goodnight, Futaba. And goodnight, Da- heh. "
    no "Goodnight, {i}Sensei.{/i}"
    no "Almost let my fantasies get the better of me there."

    play sound "dooropen.mp3"

    "Nodoka leaves the room and I wonder to myself why I continue to let this infected wound fester beneath a layer of adhesive instead of ripping the bandage off and medicating it."
    "But as the door closes and I turn back to Futaba, I remember that part of the reason is that I’m just too interested in how the wound feels when I poke it."
    "The other part is that I worry ripping the bandage off will just create a larger wound."

    scene black
    with dissolve2

    "Nodoka knows too much. "
    "In fact, that’s {i}all{/i} Nodoka does when she’s not busy masterminding plans to strip the girls she dislikes down and offer them up to me like a cat dropping a dead mouse at the feet of its master."
    "I did not ask for this- but it is something I have now."
    "And until I find a way to properly dispose of it, I must continue feeding it and loving it and appreciating it."
    "For despite those that suffer due to the sharp cuts of her canines, I have only felt the opposite-"
    "A never ending influx of new experiences, each more pleasurable yet less believable than the last and only attainable through the deepest depths of my mind."
    "How she made it there, I don’t know."
    "But I am far too afraid to remove her."

    scene futabanodokadorm13
    with dissolve2

    "I take a seat on the bed and redirect my attention to Futaba, who shoots me a glance halfway between apologetic and relieved."
    "I return it with an exasperated sigh and we both silently agree that Nodoka, even when all she’s doing is resting her head on the shoulder of her friend, is very exhausting to be around."
    "But that’s fine...because Futaba is the complete inverse of that- and I struggle to think of a time when being around her did {i}not{/i} fill me with a sense of extreme comfort."
    "But it’s that exact thought that makes me question just how she found herself letting a virus like Nodoka in."
    "And I wonder if it is just one more example of her helping someone who should probably just sink stay afloat instead."

    s "Do you really trust her, Futaba?"

    scene futabanodokadorm14
    with dissolve

    f "Nodoka? Why wouldn’t I?"
    s "I don’t know. She doesn’t seem like she’s always...scheming to you?"

    scene futabanodokadorm15
    with dissolve

    f "Ah...that. Yeah, it does feel like she’s always up to something, doesn’t it?"
    f "Nodoka is...well, as I’m sure you’ve realized, a pretty big personality. But I don’t really think that it’s big in the wrong ways."
    f "There are other big personalities like...like Yumi for example. People who take over conversations and situations just by actively participating in them."
    f "And while Nodoka does make a lot of people uncomfortable...like, {i}very{/i} uncomfortable, I’ve never really seen her make someone feel {i}bad{/i} before."
    f "She’s...umm..."

    scene futabanodokadorm16
    with dissolve

    f "She’s...{i}protective.{/i} I think that’s the best word for it."
    f "She doesn’t connect with very many people, so when she actually {i}does{/i}, she’ll do everything she can think of to keep cultivating that relationship. That’s probably where the...scheming thing comes from."
    f "But...take me, for example. When she stood up for me in class and...when she became Yumi’s {i}new{/i} target...that wasn’t the first time she’s ever done something like that for me."
    f "She’s been sticking up for me for as long as I can remember...and I have nothing but good things to say about her."
    f "But I guess I can understand if she’s a little too much for some people."
    s "Then, to ask the same question she tried asking before...what if you found out she wasn’t actually like that?"

    scene futabanodokadorm17
    with dissolve

    f "You mean...if she actually {i}did{/i} try to get revenge for me behind my back?"
    s "Yeah...How would you feel about her then?"
    f "I’d feel...disappointed. Because she knows better than anyone that’s the exact opposite of what I’d want."
    f "But it would have to be something really bad to seriously impact my relationship with her because, even if it’s something I {i}didn’t{/i} want her to do, she did it because she cares about me."
    s "Are you sure that-"

    scene futabanodokadorm18
    with dissolve

    f "Absolutely."
    f "I’ve never been more sure of anything."
    f "Could personal interest be a factor as well? Of course. This is Nodoka we’re talking about. She’s even more of a narcissist than you are."

    scene futabanodokadorm17
    with dissolve

    f "But she’s also extremely kind..."
    f "She just doesn’t like when people know that."
    s "I’ll...believe that when I see it, I guess."
    f "That’s the thing, though, Sensei. She probably won’t ever {i}let{/i} you see it."
    f "Those “errands” she mentioned before leaving...what do you think they are?"
    f "What do you think she’s doing right now?"
    s "I don’t know. Probably something involving porn."

    scene futabanodokadorm18
    with dissolve

    f "She’s taking care of her mom."
    s "What? "
    f "Nodoka is constantly moving back and forth between the dorms and her home because her mom isn’t..."
    f "Well, she isn’t really able to function on her own. But that’s really all I feel comfortable telling you..."
    s "What happened to her?"

    scene futabanodokadorm19
    with dissolve

    f "I literally just told you that was all I feel comfortable telling you..."
    s "Sure. But I’ve made you feel uncomfortable plenty of times in the past and it’s never really backfired before. Also, I doubt Nodoka will tell me anything about this if I ask."
    f "Please don’t ask. I don’t really want her knowing that I told you. "
    f "I just didn’t want you thinking she was some kind of evil genius when she’s more of an...extremely eccentric, socially awkward genius who has trouble empathizing and...a dysfunctional moral compass."
    s "Huh..."

    scene futabanodokadorm18
    with dissolve

    f "Does knowing {i}that{/i} change your opinion of her?"
    s "I...have to think about it, I guess."
    f "That’s so strange, though. I really thought you liked Nodoka. At the very least, she seems to like you a lot."
    s "I do like Nodoka. I just have a harder time understanding her than...all of the non-Yasu girls, I guess. "

    "Plus, I watched her singlehandedly dismantle both the life and reputation of a girl I worked genuinely hard for and that...does not sit well with me."
    "Hearing that she’s an actual human being instead of a vengeance-robot does help a little in reshaping her inside of my mind, but...I don’t think she’ll be returning to her original form in there any time soon."

    f "I get what you’re saying. Sometimes, I think I’m the only person who {i}does{/i} understand Nodoka. "
    f "I had pretty much this same exact talk with Rin shortly after Nodoka moved into the dorms and I’m sure I’ll have it again with someone else too. I’m used to it."
    f "To be frank, there’s a ton of stuff about her I’m sure I’ll never understand. But I don’t think you need to understand everything about someone to figure out if they’re important to you or not."
    f "After all, there’s even more I don’t understand about {i}you{/i} and I lo-"

    scene futabanodokadorm20
    with hpunch

    f "LIKE YOU."
    s "..."
    f "..."
    s "You-"
    f "NOPE."
    s "Futaba-"
    f "NOPE!"
    s "Were you-"

    scene futabanodokadorm21
    with hpunch

    f "STOP! IT WAS AN ACCIDENT! I WASN’T GOING TO SAY IT!"
    s "Wow. It’s been a while since you’ve yelled at me like this."
    f "I’M NOT YELLING! I’M JUST...INFORMING YOU OF A MISTAKE I MADE! "
    f "THINGS LIKE THIS HAPPEN!"
    s "But what if I was going to say it back?"
    f "YOU-"

    scene futabanodokadorm22
    with dissolve

    f "Wait, what?"
    s "What?"
    f "Did you just-"

    scene black
    with dissolve

    s "Anyway, that’s all the time I have tonight. But it was nice hanging out with you, Futaba. I’ll see you soon."
    f "Oh come on! You can’t just leave after saying that!"
    s "I just don’t feel comfortable with you yelling at me like this. But we can hang out again soon."
    f "Sensei! Come back!"

    play sound "dooropen.mp3"

    "I open the door and exit Futaba’s room."

    stop music

    "I wasn’t going to say it back."

    $ renpy.end_replay()
    $ nodokablock = False
    $ futaba_love += 1
    $ futabadorm50 = True

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label library50:
    scene romancenovels1
    with fade
    play music "morningmoon.mp3"

    "I make my way over to the library hoping to find Futaba but, instead, am greeted by a lone folder occupying the space she normally sits at."
    "And while I’m sure that sparking up a conversation with it wouldn’t be the {i}first{/i} time I’ve gotten locked in a discussion with an inanimate object, it’s not really something I typically {i}seek out.{/i}"
    "Either way, it’s not like I have anything else going on today- so I might as well wait around until Futaba inevitably returns to reclaim her folder."

    scene romancenovels2
    with fade

    "When I take a step closer, I notice a very specific and extremely suspicious warning scribbled along the bottom of a piece of paper."
    "It’s the type of warning that essentially beckons a person to do the opposite of whatever is written- much like a “keep off grass” sign but with more...pinstripes."
    "Obviously, I’m going to move the folder. Not just because I’m being told {i}not to,{/i} but because I have no idea what would compel someone to provide a warning like that in the first place."

    scene romancenovels3
    with dissolve

    s "..."
    f "..."

    "Today is weird."

    s "..."
    f "..."

    "I stare at the back of Futaba’s head for a moment or two, expecting her to realize I’m here and scold me for once again disregarding easily-followed rules."
    "But, as she tends to do, she remains focused on what’s in front of her, not paying any mind to the fact that I have crumbled the barrier between us."
    "Either that or she’s caught in a daydream again but, based on the precedent set by all of the {i}other{/i} times she’s daydreamt, I don’t really think she’d do that on the {i}floor.{/i}"

    s "..."
    f "..."

    "Maybe she’s just dead?"
    "Her head isn’t moving at all. Maybe some angry library-goer decapitated her and left her head on a spike behind a folder and just hoped that someone a little better at following rules would show up in my place?"

    s "..."
    f "..."

    "Or she’s just reading."

    scene romancenovels4
    with fade

    s "..."
    f "..."

    "Yeah, I’m pretty sure she’s just reading. "
    "Why she’s doing that down there when there are plenty of chairs around, I’m not sure. But it is my mission at this point in time to find out or her folder will have died for nothing."

    s "Fu-"
    f "{i}Hah...{/i}"
    s "..."

    "A hushed and...suspiciously aroused sigh escapes her lips as I look down on her in a way much different from how things normally are when I hear her emit noises like that."
    "But while I’d love to stick around and hear her {i}continue{/i} to make these noises, I am stricken with an intense bout of jealousy in knowing that she is getting just as aroused for {i}paper{/i} as she does for me."

    f "{i}Mmh...{/i}"
    s "..."
    f "{i}...ah~{/i}"
    s "Okay. That’s enough."

    scene romancenovels5
    with dissolve

    f "{i}Mnh...it’s almost like...I can hear him...{/i}"
    s "You can. I’m right behind you and capable of satisfying you in ways much greater than a rectangle comprised of slaughtered trees."

    scene romancenovels6
    with dissolve

    f "..."
    s "..."
    f "Did you..."
    f "There was a...a sign..."
    s "Yeah. I took it down because I was curious about what one measly little folder could possibly conceal. Little did I know it was just a horny librarian."

    scene romancenovels7
    with dissolve

    f "I’m...I’m not..."
    f "I’m just...on my lunch break right now..."
    s "Cool. Spend it with me and tell me about whatever weird fantasy book is getting you all riled up in the middle of a public forum."

    scene romancenovels8
    with dissolve

    f "Can I...at least finish this chapter? And can you maybe put the folder back up? I didn’t want anyone watching me while I...you know..."
    s "Masturbate?"

    scene romancenovels9
    with hpunch

    f "Read! I’m not going to masturbate in a library!"
    s "Well, you could’ve fooled me."

    scene black
    with dissolve2

    "Disregarding Futaba’s request to leave her alone until she finishes the next chapter of her book, I move to the opposite side of the counter and take a seat beside her."

    scene romancenovels10
    with dissolve

    "I also steal her book because I am stronger than her and curious about just what she’d choose to read over spending time with me."

    f "H-Hey! Give that back! I wasn’t done with that yet!"
    s "..."
    f "Sensei!"
    s "..."
    f "I...would like my book back, please!"
    s "Huh. "
    s "I didn’t think you read this kind of stuff, Futaba."

    scene romancenovels11
    with dissolve

    f "Oh my God..."
    s "I guess I can see why you were getting so into it, though. It’s {i}very{/i} descriptive."
    s "I always kind of figured Nodoka was the erotica girl, though."

    scene romancenovels12
    with dissolve

    f "It’s not {i}just{/i} erotica, Sensei! There are just...erotic scenes in it. Call it a romance novel! It makes me feel less...lewd!"
    s "If that’s what you want, sure. Is this really something you should be reading while on duty, though?"
    f "I was on my break! "
    s "It’s like 10:30 already. You never take breaks around this time."

    scene romancenovels13
    with dissolve

    f "It’s 10:30 already? "
    s "Yeah...How long have you been reading this?"
    f "..."
    s "..."
    f "I don’t want to talk about it."
    s "Futaba-"

    scene romancenovels14
    with dissolve

    f "I have a problem, okay?! I borrowed a romance novel from Nodoka and ever since, I can’t stop reading them! I’m losing sleep! I didn’t even eat dinner last night!"
    s "I’m kind of upset that you never became this addicted to me."

    scene romancenovels15
    with dissolve

    f "It’s easier in books since...I’m able to separate myself from everything. When things happen in real life and I remember that I’m a part of it, I just..."
    f "It’s harder for me to enjoy things like that."
    s "This just seems like a lot of effort to go to when outlets like porn exist."
    f "I’ve never really...liked porn. It’s always made me feel kind of weird. Plus, it’s not like I could even watch it in the library if I wanted to."
    f "Besides...romance novels aren’t {i}just{/i} sex, you know. They have stories just like any other book. There’s just an additional...window into intimacy in them that many of the other stories I read lack."

    scene romancenovels16
    with dissolve

    s "{i}The cold air hits my chest as his strong hands, like that of marbled sculptures, unbutton my tunic and lay me out on the grass.{/i}"
    s "{i}He shifts my hips and pulls me toward him, his proud length pressing up against me through my undergarments — but when I look into his eyes, the kind, gentle man I have come to know has all but vanished.{/i}"
    s "{i}In his place lurks a hungry tiger...bursting with bestial vigor and unable to hold himself back from pinning my slender wrists to the ground and taking me as his own.{/i}"
    f "Please...stop...I can’t take much more of this..."
    s "{i}He purses his lips and growls, returning his hands to my chest and fondling my breasts before lowering himself down and exploring the rest of me with his tongue.{/i}"
    s "{i}As if it's instinct, I reach for the back of his head, running my fingers through his hair and pressing him further into me as his lips begin to taste the petals of my flower.{/i}"
    f "And then they have sex! The end!"

    scene romancenovels17
    with dissolve

    s "You’re really enjoying this, aren’t you?"
    f "I have never felt more embarrassed in my life...and I once stripped for you in the nurse’s office."
    s "I remember that. We should do that again sometime."
    f "Give my book back and I will let you do whatever you want to me."
    s "I’ll pass. I’m actually having a lot of fun turning you on like this. It’s not often that {i}you’re{/i} the one overcome with lust while I’m completely unfazed."
    f "Unfazed? That didn’t affect you at all?"
    s "Not really. I have no idea who these characters are. Nor do I long for a man to dominate me with bestial vigor."
    f "There are romance novels written from the male perspective too, you know. And...there’s a good chance I could probably help you find one if you’re ever interested in reading any."
    s "That sounds better, but I think sticking to normal sex is probably more my style."

    scene romancenovels18
    with dissolve

    f "I suppose that’s fair...and here I am, still not even knowing what “normal sex” feels like."
    s "Is that just horny Futaba speaking? Or is that something I’m supposed to interpret in my own twisted way?"
    f "It’s probably...horny Futaba speaking..."
    f "But I also don’t think it would be twisted since...you and I are already...you know...{i}involved.{/i}"

    scene romancenovels19
    with dissolve

    s "If only I knew what “bestial vigor” entailed. Maybe then we could be even {i}more{/i} involved."
    f "Sensei...how would you feel if I were to commentate on all of the things {i}you{/i} consume in your free time when you want to...get in the mood?"
    s "Honestly? Not bad. If anything, I think that might even sound kind of fun."

    scene romancenovels20
    with dissolve

    f "Ugh...it must be so great not getting embarrassed about every little thing. "
    s "What do you even have to be embarrassed about around me? Do you think I’m suddenly going to stop seeing you just because you read books about elves getting fucked in your free time?"
    f "They’re not even elves. Stop assuming things when you’ve only read one page."
    s "Question, then. {i}Have{/i} you read a romance novel about elves getting fucked? Because based on everything I know about you, I have a strong feeling you have."
    f "I..."

    scene romancenovels21
    with dissolve

    f "Yes."
    f "I suppose there’s no point in hiding it anymore. You’ve uncovered my biggest secret and my biggest shame."
    s "Hey, I’m happy for you. Leaning into your degeneracy isn’t always a {i}bad{/i} thing. Especially when it leads to you learning things about yourself."
    s "If anything, I feel a little better now knowing that what we have isn’t just a one-sided pursuit of lust on my behalf and that what you really want is a tiger who-"

    scene romancenovels22
    with dissolve

    f "I don’t want a {i}tiger,{/i} Sensei...I want you. All of those books are just excuses for me to step into the shoes of somebody else for a little while..."
    f "To experience the connections {i}those{/i} characters have since I doubt I’ll ever be able to do that on my own."
    s "Why not? What makes you so different from all of the elves you’ve watched get fucked?"
    f "Stop saying that. The key difference, though, is that all of the characters in all of the books I’ve read know who they are while I’m still mostly...unsure about everything."
    f "No one in any of the romance novels I’ve read has had an extensive inner monologue about how unworthy of love they are...or how they struggle to look at themselves in the mirror."
    f "But those are things I think about every day. And even moreso before we get intimate. "

    scene romancenovels23
    with dissolve

    f "If only there was some sort of way for me to...adopt that perspective. Maybe then, I wouldn’t have to hype myself up just to reciprocate your lust..."
    f "Or, at the very least, I wouldn’t constantly find myself mentally switching places with a girl being intimate with a strong, mysterious man when I already have one of my own right here who appreciates me for {i}me.{/i}"
    s "I don’t know if saying this at the height of a personal info dump is a good idea or not, but...maybe try roleplaying? If you can’t get into the right state of mind on your own, I mean."

    scene romancenovels24
    with dissolve

    f "I..."
    f "Are you sure that’s even something you’d be okay with?..."
    s "As long as I don’t have to play any sort of role myself. I’m not much of an actor."
    s "But if you’re asking if I’d be okay “getting intimate” with you while {i}you’re{/i} putting on some sort of show, absolutely. "
    s "I think you should do whatever it is that makes you comfortable and it’s not really my duty to tell you if what you’re doing is okay or not."
    s "Note, though, that I will continue to steal books like this from you if I catch you reading them because it is both fun {i}and{/i} I am curious about what sort of secret fetishes you may have."

    scene romancenovels25
    with dissolve

    f "I think...I might like older men..."
    s "What? No way."
    f "Ha ha ha. Very funny."

    scene romancenovels26
    with dissolve

    f "But...on a completely serious note...I definitely agree with you."
    f "Maybe not in regard to the...roleplay thing, since doing that sexually sounds extremely embarrassing...but I do have to learn to be more comfortable with myself when it comes to moments like that."
    f "And I’ve been trying...really. "
    f "Progress is just slow."
    f "You can change everything about yourself...from your weight to your hair..."
    f "You can change every last bit."
    f "But teaching yourself to look {i}at{/i} those changes instead of directly through them is a lot harder than most people think."
    f "Which is..."
    f "Which is why I think I need to start {i}forcing{/i} myself forward. "
    f "Because if I don’t, it could take decades for me to get to where I want to be."
    f "And if I wait that long, I’ll have wasted my entire life."

    scene romancenovels27
    with dissolve

    s "Futaba-"
    f "Do you think that...maybe I could come over soon?..."
    f "On a day that..."
    f "Ami isn’t around?..."
    s "..."
    f "..."
    s "Are you sure?"
    f "I think so..."
    f "But I guess that could just be horny Futaba speaking. The man I like {i}did{/i} just read me a sex scene, after all."
    s "Would continuing to read it further reinforce this decision? "
    f "I don’t know, but...it would certainly further reinforce my desire to go back home and change my underwear."
    s "I still don’t think we should do this unless you feel better about-"
    f "I don’t want to wait decades, Sensei. "
    f "I don’t even want to wait another day."
    f "Now...either take me back home right now...or keep reading to me..."
    f "Because I don’t want this feeling to go away..."

    scene black
    with dissolve2

    "I wind up reading Futaba another three pages of the book before her arousal becomes too much to bear. "
    "She takes me into the bathroom and sucks me off while fingering herself."
    "But the entire time this is happening, I’m only thinking about what comes next."
    "And how the next time I invite her to my house, I’ll be cementing our relationship as one of even greater value."
    "But that’s okay."
    "I’m always comfortable with her, after all."
    "So I will do my best to keep her comfortable as well."

    $ renpy.end_replay()
    $ library50 = True
    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label futabainvite3:
    play sound "phonebeep.wav"

    "Well, ladies and gentlemen...I think today is finally the day."
    "After much deliberation and a semi-brief conversation about romance novels and Futaba’s need to move forward in life, I have decided to finally take her virginity."
    "Yes, I know. It’s been a long time coming. "
    "And if it weren’t for the fact that she is both half of my age and a student of mine, I’d say something like this would even be cause for celebration."
    "The unfortunate truth, however, is that by the end of the day, she will likely have a hard time walking."
    "Either that or she’s like Chika and just built to be fucked for hours on end without any complaints whatsoever."
    "Something tells me that won’t be the case, though. And that something is probably the fact that Futaba is {i}actually{/i} innocent whereas Chika just likes to pretend she is."
    "Either way, all that remains between Futaba and me at this point is the press of a button and a brief trip across town, where she will ultimately be defiled."

    play sound "phonebeep.wav"

    f "Hello?"

    "And then even that disappears."

    s "Hey. Are you free right now?"
    f "Umm..."
    s "Or are you too busy reading one of those elf-fucking books again?"
    f "Please stop calling them that..."
    s "I can’t. Not when that’s what they are."
    f "I...uhh...{i}was{/i} reading...but..."
    f "I can...put the book down if you want to see me..."
    f "Should I assume that...this is what we talked about in the library, though? I don’t know if I...need to come prepared or not..."
    s "Prepared?"
    f "I, umm..."
    f "I may have bought something..."
    s "Is it a pair of elf ears?"
    f "Do..."
    f "Do you {i}want{/i} it to be a pair of elf ears?"
    s "I’m not sure. I didn’t even know that was an actual possibility until right now."
    f "Well...it’s something else anyway, so...I..."
    f "I’ll just...see you soon. Oh, and Ami’s not going to be there, is she?"
    s "Ami’s actually going to film the whole thing so we can watch it as a family a few years down the line."
    f "Please don’t even joke about that...it’s hard enough having to look at pictures of myself. Watching a video of me...doing those things sounds like a nightmare."
    s "I like how you’re not at all perturbed by the Ami part."
    f "I figured that we all just kind of understood where Ami stands by now. I wouldn’t be {i}completely{/i} surprised if something like that were to happen."
    s "I’m not sure if I like what you said just now."
    f "Heheh...well you have a little while to think about it while I get ready."
    f "Oh...and sorry to ask out of the blue, but...do you have any con-"

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 10.0

    "I hang up the phone before Futaba says the “c” word because I don’t want some thin layer of rubber separating us and ruining her first time."
    "Or at least that’s what I’ll tell her if she asks why I won’t be wearing one when the truth is that I just think they’re horrible."
    "Regardless, I make my way back home...confirm that Ami isn’t going to be back for several hours...and straighten up things in my room in preparation for her arrival."
    "I have no idea how tonight is going to go...but I do know that Futaba is pushing aside a metric ton of insecurities in order to go through with this, so the right thing for me to do is just be gentle and patient."
    "We all know those aren’t my strong suits, though."
    "And I could very well break her if I am not extremely careful..."
    "........."
    "......"
    "..."

    scene futabafinallyfucks1
    with dissolve2
    play sound "dooropen.mp3"
    play music "behindabathroom.mp3"

    f "Um...hey..."
    s "Welcome to the first day of the rest of your life as a non-virgin."
    f "Uhh...you seem very...laid back about this."
    s "I told myself I was going to be gentle and patient on the way over here, but then remembered that I’ve already {i}been{/i} extremely patient and now I’m just excited."

    scene futabafinallyfucks2
    with dissolve

    f "It really has been a long time, hasn’t it? So much has happened..."
    f "It’s crazy to think it’s only been one school year."
    s "It’s not {i}that{/i} crazy to think that. But yeah, kudos to us for sticking it out this long, I guess."

    scene futabafinallyfucks3
    with dissolve

    f "The “sticking it out” part is really all on you, Sensei. I would have gone through with this a long time ago if you’d made any sort of push for it."
    s "That’s exactly {i}why{/i} I didn’t push for it. I didn’t want you jumping into things before you were mentally prepared."
    s "But now that I know you spend your mornings getting horny in the library, I think it’s probably best for both of us if I just set you free already."

    scene futabafinallyfucks4
    with dissolve

    f "Yes, thank you for {i}setting me free.{/i} "

    scene futabafinallyfucks2
    with dissolve

    f "I still don’t think I’m mentally prepared just yet...I’m excited, sure...but this is also really nerve-wracking..."
    f "And...also weirdly casual? "
    f "I always thought my first time would be really romantic...and that it would happen under the stars or...in some fancy hotel..."
    f "But here I am with my school bag slumped over my shoulder, just...walking into my teacher’s house like I’m here to study or something."
    s "I mean...we {i}can{/i} hold off if you want. This doesn’t have to happen today."

    scene futabafinallyfucks5
    with dissolve

    f "Mmm...no. I think I still want it to happen today."

    scene futabafinallyfucks6
    with dissolve

    f "Even though the setting isn’t anything close to what it’s like in my books, I’m still here with you. And that’s far more than I ever thought I’d get...ever thought I’d {i}deserve.{/i}"
    s "You deserve a lot better than me, Futaba. In fact, I think going through with this is a horrible decision on your behalf. So I’ll give you one last chance to walk away with no consequences at all."

    scene futabafinallyfucks7
    with dissolve

    f "Mmm...no thank you."
    f "In fact, I was probably going to call you by the end of the day anyway since all of that reading did a real number on me."

    scene futabafinallyfucks8
    with dissolve

    f "Also, don’t say that sleeping with you is a horrible decision. Do you have any idea just how much you’ve done for me since we met? Because I wouldn’t be {i}half{/i} as confident as I am today without you."
    s "You’ve still got a long way to go if even the thought of doing things like this makes you feel uncomfortable."

    scene futabafinallyfucks9
    with dissolve

    f "Then I guess I’ll just have to think about {i}you{/i} so all of those intrusive thoughts about myself don’t get in the way. "
    f "Unless you’re chickening out, of course. Which it’s starting to sound like you are."
    s "I’m absolutely not chickening out. I’ve wanted this since I first laid eyes on you. "

    scene futabafinallyfucks10
    with dissolve

    f "Oh, stop. You expect me to believe that when the class is full of girls much prettier and smaller than me? There’s no way a...rock like me would catch your eye in a sea full of diamonds."
    s "Diamonds are rocks too, you know."
    s "But you can believe whatever you want."
    s "Just know that when I part your legs and insert myself into your vagina that I am very proud of you."

    scene futabafinallyfucks11
    with dissolve

    f "Aww...thank you, Sensei. That was the sweetest...strangest...most sexual thing anyone’s ever said to me."
    s "Anything for you, Futaba. Except for waiting until a more “romantic” moment since you’re apparently too horny to survive another hour as a virgin."
    f "Sensei, I am going through a life-changing phase right now and I’m going to need you to understand that I’m just going to be...perpetually aroused for a little while as I work through this."
    s "Hey, you can stay in this phase forever for all I care. I like this side of you. "
    f "Well...I hope you still like it after you’ve had all of me...because it’s the last side I have to offer and I’m very worried it’s going to ruin the rest of them."
    s "And to that I say, don’t worry at all. "
    s "Now, if you’d so kindly take my hand and follow me to the bedroom-"

    scene futabafinallyfucks12
    with dissolve

    f "Umm...actually! Do you think I could maybe...go in there alone for a few minutes? To...get ready?..."
    s "If this is just one very elaborate ploy to go through all of my stuff, I’m going to be very disappointed in you."
    f "That’s...obviously not what it is. I just..."
    f "The thing I brought earlier...I didn’t wear it here since I felt too embarrassed...but it’s in my bag, so..."
    f "I just...want to put it on before we...do it..."
    s "So this present of yours is some sort of outfit?"
    f "Can I just...put it on and show you, please?"
    s "Hey, don’t let me keep you. Feel free. Just don’t steal any of my things. "
    f "I...wasn’t planning on it..."

    scene black
    with dissolve2

    "Futaba disappears into my room, leaving me alone in the kitchen with both an erection and an overflowing sense of curiosity."
    "I think to myself if this “outfit” of hers could have something to do with my roleplaying suggestion from the other day, but...is that really something she’d break out for her first time?"

    s "..."

    "Or is what she’s about to show me much simpler than that?..."
    "........."
    "......"
    "..."

    scene futabafinallyfucks13
    with dissolve2

    f "Oh God...Okay..."
    f "I can do this...I can do this..."
    f "Even if I don’t see myself the way I want to...Sensei does...Sensei is attracted to me...I just have to think about that."
    f "I have to think about him so I don’t think about myself. But now I’m {i}talking{/i} about myself and I’m starting to slip and oh my God I can’t do this."
    f "But I can...I will...I have to...I’ve already kept him waiting so long and...and..."
    f "..."

    scene futabafinallyfucks14
    with dissolve
    play sound "phonebeep.wav"

    f "..."
    f "..."
    f "..."

    play sound "phonebeep.wav"

    f "Hi. Talk me back into this. I’m already thinking about backing down."
    no "{i}Oh-ho-ho? I don’t hear any cars. Can I take that as a sign that you made it all the way to his home without turning around?{/i}"
    f "I’m...in his room right now..."
    no "{i}Alone? Check under the bed. I want to know what he’s hiding.{/i}"
    f "Nodoka, seriously. What do I do?"
    no "{i}What do you mean, “What do I do?” You know exactly what to do. I’ve told you many times.{/i}"
    f "I know. It’s just-"
    no "{i}Hah...Are you wearing it yet? Have you made it that far?{/i}"
    f "I was about to put it on when I thought I should call you instead and-"
    no "{i}Put it on. I refuse to carry on with this conversation knowing that you’re in your street clothes just seconds before being deflowered by a remarkably handsome man.{/i}"
    f "But-"
    no "{i}Futaba, you are beautiful.{/i}"
    no "{i}It will be okay.{/i}"
    f "..."
    no "..."
    f "Okay. Hold on."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene futabafinallyfucks15
    with dissolve2

    f "..."
    f "..."
    f "..."
    f "Why do I...feel even more exposed like this than I do when I’m completely naked?..."
    f "Would Sensei even like something like this? He would, right? I’m not cute like the other girls, but...but I can be {i}sexy{/i} because of my curves...can’t I?"
    f "Is that how this works? Do I look like I’m trying too hard? Because...well, I {i}am{/i} kind of trying too hard, aren’t I?"
    f "Who puts on fancy lingerie for their first time? "
    f "This is stupid. I have no idea why I thought this was a good idea. I look like a stripper. "

    scene futabafinallyfucks16
    with fade

    f "I am having a crisis."
    no "{i}An actual crisis? Or an “I’m not good enough” crisis?{/i}"
    f "The second one. "
    no "{i}Do I need to come over there and warm you up myself?{/i}"
    f "I don’t need to be “warmed up.” I need you to say something that will reignite the burning passion I felt on the way over here."
    no "{i}Penis.{/i}"
    f "Something else."
    no "{i}The man you’re in love with invited you into his home so he could make you his. And what you’re about to experience is the first step toward the you you’ve always wanted to be.{/i}"
    f "But what if it’s not? What if this is one big mistake?"
    no "{i}Then you'll learn from it. That’s how mistakes work.{/i}"
    f "But-"
    no "{i}Do you think he’s going to hurt you, Futaba? Emotionally, I mean. Physically, you are about to be put through the wringer.{/i}"
    f "I just don’t want him to think I’m gross or I’m trying too hard even though I technically {i}am{/i} trying too hard and am also probably a little gross."
    no "{i}You are not gross and you are not trying too hard. You’re a beautiful woman with a body that some men would kill for. Some Nodokas, too.{/i}"
    no "{i}I wouldn’t mind getting some blood on my hands for a shot with you.{/i}"
    f "Thank you. I needed that. And please don’t kill anyone for me."
    no "{i}Send me a picture. I want to see how it looks on you.{/i}"
    f "No. You’ll do weird stuff with it."
    no "{i}Oh, Futaba. I have many better pictures of you to do “weird stuff” with.{/i}"
    f "Well, I don’t like that at all."
    no "{i}I just want to see what my best friend looks like on her big day since she won’t let me be there with her. That lingerie is akin to a wedding dress as far as I’m concerned."
    f "You promise you won’t do weird stuff?"
    no "{i}If I must, I will.{/i}"
    f "..."
    no "..."
    f "Okay. I’ll keep you on speaker. Just give me a second."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene futabafinallyfucks17
    with dissolve2

    f "Mmn..."
    no "{i}You can do it. You’re strong. You’re beautiful. You’re the best person I’ve ever met.{/i}"
    f "I can’t find the button..."
    no "{i}What do you mean you- wait, are your eyes closed?{/i}"
    f "Maybe."
    no "{i}Hah...it’s the one that-{/i}"

    play sound "cameraflash.mp3"
    with cumflash

    f "Wait. I think I did it."
    no "{i}Good. Now look at it.{/i}"
    f "I don’t wanna."
    no "{i}You have to.{/i}"
    f "But-"
    no "{i}Futaba-{/i}"

    scene futabafinallyfucks18
    with dissolve

    f "Fine! Jeez!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene futabafinallyfucks19
    with dissolve

    no "{i}Before sending it to me, tell me what you see.{/i}"
    f "I see...a beautiful garment..."
    f "The room of the man that I love..."
    f "I see all of his things...the place he falls asleep at night..."
    f "It’s comfortable here...{i}I’m{/i} comfortable here..."
    f "It’s like home in a way...and when I’m here I...I can be..."
    f "I can be confident..."
    f "I can be...strong..."
    f "I can..."
    f "I..."

    scene futabafinallyfucks20
    with dissolve2

    f "I..."
    no "{i}Futaba? What’s-{/i}"
    f "Sorry, I’ve..."
    f "I’ve gotta go."
    no "{i}Wait just one second, Futaba. Don’t tell me you’re seriously-{/i}"

    play sound "phonebeep.wav"

    f "..."
    f "..."
    f "..."
    f "I just want to like myself..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play sound "knock.mp3"

    s "Futaba? You didn’t climb out of the window, did you? You’ve been in there for a while."
    f "I’m fine, Sensei..."
    f "You can come in..."

    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene futabafinallyfucks21
    with dissolve2

    s "So...I’m obviously not going to complain because you are absolutely beautiful, but...I thought you were going to be wearing something?"
    f "..."
    s "..."
    f "I forgot it."
    s "You-"
    f "Just leave it at that, please."
    s "..."
    f "..."
    s "Okay..."

    scene futabafinallyfucks22
    with dissolve

    f "I still...want to do it, though..."
    s "Are you sure?"
    f "You’re showing a lot of concern for me today, Sensei..."
    f "Are you afraid you’re going to break me?"
    s "I think that’s kind of the goal in a sense, isn’t it?"
    f "Can you be gentle?..."
    f "I’m turned on, but...I’m still really nervous...and you’re not really on the small side, so..."
    s "I’ll be gentle. Don’t worry. And if at any point you want me to stop, just say so."
    f "Okay..."

    scene futabafinallyfucks21
    with dissolve

    f "And, umm...as a special request..."
    f "Can you maybe..."
    f "Not say anything about my body while we’re doing it?..."
    s "..."
    f "..."

    scene black
    with dissolve2

    s "Of course."

    "........."
    "......"
    "..."

    scene futabafinallyfucks23
    with dissolve2

    "I position myself between Futabas legs, grabbing them before pressing my dick down against her."
    "She makes no attempt to move, allowing me to guide her in any way I please. "
    "And while these circumstances would dramatically impact the way I handle several of her peers- for her, I decide it’s best to just keep things simple for now."
    "It’s too early for the stars to show their faces, and I have no patience nor desire to rent out a hotel room for something that can be accomplished right here."
    "Right where I’ve accomplished so much more."
    "One more memory piles onto the tower of them as I stare down at a girl who shows no intent to ever stare at herself."
    "Instead, what she does stare at is a small, unfolded black cloth peeking out of the corner of her school bag."
    "For her sake, I don’t put much thought into what that fabric may be."
    "I just keep looking down at something she’s too blind to see."

    f "You can...put it in whenever you want, [futabamaster]..."
    f "I think I...should be ready...if you know what I mean..."
    s "It’s probably safe to assume I just always know what you mean whenever I have you in this position."

    scene futabafinallyfucks24
    with dissolve

    f "That...makes it sound like we’ll be in this position pretty often from now on..."
    s "Assuming the pain of losing your virginity doesn’t turn you off from sex forever, we probably will."

    scene futabafinallyfucks25
    with dissolve

    f "Maybe, uhh...{i}don’t{/i} bring up the pain thing? "
    f "I’m nervous enough as-is and...I think what would make me the most comfortable is just focusing on the moment itself..."
    s "Whatever you need. Any final requests?"

    scene futabafinallyfucks26
    with dissolve

    f "Just...don’t be rough unless you {i}have{/i} to be. "
    f "I want you to enjoy yourself, but...if you can enjoy yourself while being gentle, I think I’d like that the most."
    f "Other than that...I don’t think there’s anything I want."
    f "Just...finally being with you is enough for me."

    "Futaba lets out a heavy sigh as I begin to pull my waist back, preparing herself for what I’m sure is going to be a rather unpleasant experience on her end."

    scene futabafinallyfucks27
    with dissolve2

    f "Ngh!"

    "On my end, however, the experience is already unforgettable after insertion alone."
    "I grip the base of my cock between my thumb and forefinger and slowly slide it into Futaba, being careful not to move too quickly."
    "Despite what I’d describe as only a mild resistance, her body jerks upward, reluctantly accepting several inches of me while the rest remains in the confines of my hand."
    "I wouldn’t describe what I’m doing right now as thrusting exactly, but moreso shifting my waist in an attempt to find out how much of this she can bear."
    "It’s a little more than I expect, which pleases me greatly, but I’m still hesitant to push my luck any further at the risk of destroying her."
    "Her insides are almost hot enough to burn me and wet enough to make movement easy. "
    "Not like I have to move much in the first place given just how much she’s squirming right now, but still."

    f "Hah...ow...ow, ow, ow..."
    s "How are you feeling?"
    f "Mngh...weird...really weird..."
    f "It’s not really...the kind of pain I expected, but...it’s not...unbearable..."
    f "Just...keep going and...don’t ask me about how I’m feeling..."
    f "I’m sure it’ll...start feeling better...soon enough..."

    scene futabafinallyfucks28
    with dissolve

    "I let go of my dick and return my hands to Futaba’s legs, pressing hard against the skin of her inner thighs and leaving marks in the shape of my thumbs on them."
    "Her body’s acceptance of my cock has shifted from reluctance to curiosity, opening up slightly and letting me push without being tightly squeezed."
    "It’s by no means a loose fit and I can still feel every last bit of her, but the freedom to move as I please begins to excite me more than I want it to while I’m attempting to hold myself back."
    "As I begin to speed up, the bed rocks and causes Futaba’s massive breasts to bounce in unison with my thrusting."
    "Her self consciousness compels her to grab them on occasion and put an end to the movement, but I return every instance of this with a harder push to signal that I {i}want{/i} to see them."
    "She remains mostly silent throughout the process. And if it weren’t for the fact that she’s still extremely wet, I may even think she’s not enjoying this to at least {i}some{/i} extent."
    "The matter of that pleasure outweighing the pain is just something I can’t speak to, though."

    scene futabafinallyfucks29
    with dissolve2

    "Her eyes open at the same time the first traces of blood begin to seep out of her."
    "I’m surprised it took this long to reach the open air, but I suppose the sheer size of my dick played some part in preventing it from leaking out."

    s "How are you feeling?"
    f "I told you...to not ask that..."
    s "Since when do I listen to you?"

    scene futabafinallyfucks30
    with dissolve

    f "Hah...hah...since never...but I figured today might be...a good chance to start..."
    f "I guess I’m...doing a little better now that...the hardest part is over...but it’s still...pretty rough..."
    s "Your body begs to differ. It seems to be quite fond of me so far."

    scene futabafinallyfucks31
    with dissolve

    f "Ah...ahh! "
    f "If only my...mind agreed..."
    f "I want to...enjoy this, but...my stupid brain keeps telling me that I’m...supposed to be in pain..."
    f "You’re not...almost done yet...are you?..."
    s "Honestly, no. It feels so good inside of you that I’ve been trying to savor this. "
    s "But I can just...stop savoring it if you want?"
    f "Hah.....ngh.....I don’t know...I wish I could last longer since you’re liking it that much..."
    f "I want you to...enjoy yourself...as much as you can..."
    f "I just...also...don’t want...to pass out..."
    s "Yeah, that would be a pretty anticlimactic end to this after the wait was so long."
    f "Heheh...hah...I’m glad the...wait is finally over, though...even if...this is really hard..."
    s "Still holding out hope that it might start feeling better soon?"
    f "Fuck...no...I’ve already given up on that..."
    s "Wow. It must really be bad if {i}you’re{/i} going to start cursing."
    f "Ngh...[futabamaster]...I’m not...a little girl anymore..."
    f "You made me a woman and...I can...I can curse if I want..."
    s "Yeah? Then tell me to fuck you."
    f "Is that...not what you’ve been doing?..."
    s "I mean...it {i}is.{/i} But that’s kind of just a thing people say to hype the other person up in bed."
    f "Hahh...ahh...you seem pretty...hyped up already, [futabamaster]...I don’t know if I can...handle any more..."
    s "Just one time. Come on."

    scene futabafinallyfucks30
    with dissolve

    f "Are you...always going to be this...embarrassing?..."
    s "Only if you don’t do what I want."
    f "Then...f..."
    f "Fuck me...[futabamaster]..."

    scene futabafinallyfucks32
    with dissolve

    f "Ahh! See?! I knew I...couldn’t handle any more!"
    f "Don’t fuck me! {i}Don’t{/i} fuck me!"
    s "Are you actually asking me to stop? Or are you just retracting the previous “fuck me?”"
    f "I don’t know what I’m doing! My mind is...all over the place..."

    "I spread Futaba’s legs out a little wider to give myself more room to attack her lower body."
    "Well, “attack” in a way that is still significantly gentler than I am accustomed to, but you get what I mean."
    "Her feet dangle and sway with each thrust- toes curling in the process."
    "Futaba once again presses down on one of her breasts to stop it from bouncing, but leaves the other one to roam free as her right arm finds its way behind her neck for support."
    "I’m sure the blood is playing a lead role in the dance of hot fluids drowning my cock with each passing second, but her nipples indicate to me that it is not a solo act in the fact that they’ve become rock hard."
    "I refuse to reach out and pinch them, though, as I am too enthralled with the fact that this girl’s legs make the perfect handles."
    "I am too enthralled by the sensation of her body's transition from reluctance to curiosity and then, finally, to where we are now-"
    "Pure, unadulterated lust."
    "Her mind may not agree with the rest of her, but I can nearly guarantee that under different circumstances, Futaba would be just minutes (Or even seconds) away from squirting her brains out."
    "In thinking that, though, I’m forced to come to terms with the fact that I am {i}also{/i} just seconds away from erupting- and this much isn’t just a hypothetical."

    s "Futaba...I’m about to cum..."

    scene futabafinallyfucks33
    with dissolve

    f "Thank God! I thought this was never going to end!"
    s "Would it kill you to at least {i}act{/i} like you’re enjoying it?"
    f "I’m not...ready for roleplay yet..."
    s "Well, fortunately for you, it’ll all be over soon..."

    scene futabafinallyfucks34
    with dissolve

    f "Hah...hah! [futabamaster]! Hurry up! I can’t take...much more of this!"

    "Seeing as this is the final stretch, I don’t feel bad about amping up the speed a few notches."
    "Her body disagrees with this decision, however, as it reverts to its original state of reluctance and attempts to remove me from her by force."
    "But that actually works out rather well."

    with sexfade
    with sexfade
    scene futabafinallyfucks35
    with cumflash
    with hpunch

    "Because my eruption comes the moment she refuses to take any more, causing a thick stream of my {i}own{/i} brand of liquid to spray all over her voluptuous body."

    scene futabafinallyfucks36
    with dissolve2

    f "Hah...hah...hah..."
    f "It still hurts..."
    f "Why does it still hurt?..."
    s "It’s probably going to hurt for a few days. I did kind of just heavily damage the inside of your body, you know."
    s "But, on the bright side, it won’t be nearly as bad next time. And once you get used to it, we can do this every week."

    scene futabafinallyfucks37
    with dissolve

    f "H...Hooray..."
    f "That sounds...so..."
    f "So..."
    f "..."
    f "I think I’m gonna...pass out..."

    scene black
    with dissolve2

    "Futaba does pass out, which leaves me to clean the remnants of myself off of her so that it doesn’t dry up and become even harder to clean off."
    "Also, we somehow managed to prevent any fluids other than sweat from dripping onto the bed, and I don’t want that rare feat to be ruined by her unconsciously deciding to roll over."
    "I cover Futaba with the blanket after she’s cleaned up and put my clothes back on, retreating to the kitchen for a glass of water."
    "When she wakes up in roughly an hour, she’s a bit delirious and doesn’t seem to even remember how she got here or {i}what{/i} we did."
    "When she finally returns to reality, though, and the memories flood back into the mind that betrayed her while her body did not-"
    "She smiles at me."
    "And then falls back asleep in my arms."

    $ renpy.end_replay()
    $ futabainvite3 = True
    $ futaba_love += 10
    stop music fadeout 7.0

    "{i}Futaba’s affection has increased by 10!{/i}"
    "{i}Her self-esteem has increased by 1.{/i}"
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

label makotofutabafuntimelustevent:
    stop music
    play sound "static.mp3"
    scene everythingg with flash
    scene christmasyay with flash
    scene threesome1
    stop sound
    $ renpy.pause(7, hard=True)
    scene temp
    play music "sweetervermouth.mp3"
    $ renpy.pause(5, hard=True)
    scene threesome2
    $ renpy.pause(3, hard=True)
    scene threesome3
    $ renpy.pause(3, hard=True)
    scene threesome4
    $ renpy.pause(2, hard=True)
    scene threesome5
    $ renpy.pause(3, hard=True)
    scene threesome6
    $ renpy.pause(2, hard=True)
    scene threesome7
    $ renpy.pause(2, hard=True)
    scene threesome8
    $ renpy.pause(4, hard=True)
    scene threesome9
    $ renpy.pause(2, hard=True)
    scene threesome10
    $ renpy.pause(4, hard=True)
    scene temp
    $ renpy.pause(3, hard=True)
    scene threesome11
    $ renpy.pause(2, hard=True)
    scene threesome12
    $ renpy.pause(4, hard=True)
    scene threesome13
    $ renpy.pause(3, hard=True)
    scene threesome14
    $ renpy.pause(3, hard=True)
    scene threesome15
    $ renpy.pause(2, hard=True)
    scene threesome16
    $ renpy.pause(5, hard=True)
    stop music
    scene black
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene actualthreesome1 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"
    $ renpy.pause(5, hard=True)
    scene actualthreesome2
    with dissolve4

    s "..."
    s "What?..."

    scene actualthreesome3
    with dissolve2

    s "..."

    play sound "static.mp3"
    scene actualthreesome4 with flash
    stop sound

    mak "Mngh...mmff! Mmmphhfttt!!"
    f "Mlem........schlck.......mrlmmff......"
    mak "Mm! Mmf~"
    mak "Ishn’t...it...mzing...Ftba?"
    mak "Dshn’t...Snshei cock...tshte...bttr thn...anyshng in...thholewde wrld?..."
    f "Mmnch...mlm...I don’t know...you keep hogging it..."
    mak "Isshory...Ijsht...cn’thlpit..."
    s "..."

    "This isn’t actually happening, is it?"
    "I remember being on the beach...and I remember talking to them...but I don’t remember what sort of insane transition there would have had to be for us to get {i}here.{/i}"
    "Just knowing that I’m involved with both of them wouldn’t be enough to incentivize {i}this,{/i} right?"
    "Or maybe..."
    "This is just how they show their love?"
    "Maybe, sensing that they’re on the end of some sort of metaphorical rope, they’ve come up with a last line of defense. A means of forcing me to choose {i}both{/i} of them rather than anyone else."
    "They’re sacrificing their own happiness and their own values for a lifetime stranglehold on my cock."

    mak "Mmf! Mmnch! So...good!"
    f "Sensei...mmngh~ "
    f "I want...a turn too!..."
    s "Are you two...really okay with this?"

    play sound "static.mp3"
    scene actualthreesome5 with flash
    stop sound

    mak "Wh...wldn’tw...be?..."
    f "This is what you want...so this is what I want..."
    s "You-"
    mak "Wshwrong? Toomch...plshureat...one time?..."
    f "Mmlngh...are you...going to cum, [futabamaster]?..."
    f "Are you going to cum...in Makoto’s mouth?..."
    s "No, you just..."
    s "You two..."
    f "...?"
    mak "Mmf?..."
    s "..."
    s "Nothing. "
    s "{s}You look more beautiful than ever before.{/s}"

    scene actualthreesome4
    with dissolve

    mak "Hehehngh...yrjst...sayingthat...cshwe’re...shckingyer...cock..."
    f "We can’t stop...we’ve been doing this for...mmf...a whole hour already..."
    s "There’s no way-"
    mak "Crsthere’s a way..."
    f "You’ve already cum four times..."
    mak "Shmeyou...wereashleep...for it..."

    "This is a dream."
    "Just like everything else that’s happened tonight."
    "None of this is real. None of {i}anything{/i} is real. I’m part of a game in a fake world where I can fuck as many girls as I want. "
    "That’s the truth because that’s what I think. And everything I {i}think{/i} is true {i}is{/i} true."
    "This is my world."
    "And if I want to fuck two of my most codependent students at the same time in complete disregard for their mutual disinterest in both women and polygamy, {i}I will.{/i}"

    s "You like my cock that much, huh? You couldn’t even wait until I woke up?"
    f "We tried...to wake you up...but we just couldn’t hold it in anymore..."
    mak "I...ngh! Needed your dick...right away...or I was going to die..."
    f "Don’t worry, Sensei...we took...really good care of you..."
    mak "It’s still...sliding down...the back of my throat..."

    "It all feels amazingly realistic for something inside of a dream."
    "Makoto has maintained all of the skills and techniques she’s picked up throughout our time together...and Futaba, despite trying something new, is just as adaptable and naturally talented as always."
    "It’s the perfect emulation..."
    "It’s exactly how I imagined it in my mind over and over and over again with this specific pair."
    "What will my next dream hold? "
    "And why am I waiting so insanely long to take the next step in {i}this{/i} one?"

    s "Is this enough for you two?"
    f "No...not even close...[futabamaster]..."
    mak "Give us more...make us feel better..."
    f "It’s so hot out here...it’s like my insides are melting..."
    mak "If I was any more wet...I’d be fucking swimming..."
    mak "Mmngh! Give it...to me...[makotomaster]! Give me...your fat cock."

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    s "Your wish is my command."

    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene happy9 with flash
    scene actualthreesome6 with flash
    stop sound

    mak "Hah! Yes! Yes...yes, yes! Oh my......GOD! FUCK!"
    mak "Can...barely...ngh! Breathe, but...gggghhhhh!!!!!!!~~~"
    f "Mlm...mmf.......mm~"

    "I lift Makoto up with ease and lower her down onto my dick as I lean back against some sort of stone structure I can’t be bothered to discern right now."
    "I tightly wrap my hand around her neck and cut off as much of her airway as I can, quickly stripping her of the ability to speak."
    "Every once in a while, to make sure she doesn’t fall unconscious, I will adjust myself. But only to give her enough time to fill her lungs."
    "After that, I make her my puppet once again...and stir her insides in a way much more violent and aggressive than I have ever done with her before."
    "She likes it."
    "I can tell by how hard she squeezes me back."

    f "Mmngh~ mmn....[futabamaster]...how come...Makoto is the only one who...gets to have fun?..."
    f "I want you...to fuck me too..."

    "I stare down at Futaba to find her playing with herself with such fervor that I’m tempted to drop Makoto on the spot just to help put the poor girl out of her misery."
    "But she’ll have her turn soon enough."
    "They’ll both have turns...as many of them as I can muster...for this is not a dream I intend to ever leave if I can do anything about it."
    "Futaba takes my index and middle finger all the way to the back of her throat, but my absentmindedness and inability to think straight entices me to tickle her uvula with my fingernails."
    "She doesn’t like this."
    "She hacks and hacks as spit drips from her mouth and onto the grass below us. But she never removes my filthy fingers from her throat. And she never stops playing with herself."

    mak "Ck...chh!....Ngk!"
    f "Mmf...mmm....mlm...schlck..."

    "They’re both such good girls...such excellent toys."
    "And I am ever so thankful to be the one who gets to use them until they break."

    scene actualthreesome7
    with dissolve

    mak "Nck....hnck...mfffch!...Har...der..."
    mak "Des.......troy........me!"

    "Makoto’s plea makes even Futaba more excited as her fingers, which I hadn’t even noticed were accompanying us until now, spread the lips of her classmate’s pussy apart."
    "She inserts a finger inside of Makoto that goes on to compete with the real estate my dick is currently taking up, but instead of feeling intrusive, it just makes me applaud her ability to multitask."
    "The way she can suck...play with herself...and finger another girl all at once...makes even {i}me{/i} envious of her talent."
    "I wish to see it applied in another way."

    mak "K..................k.............."
    s "Don’t pass out on me, Makoto. Not until I cum."
    mak "........................k................."

    "I can feel her body going limp, but I’m too caught up to remove my hand from her throat."
    "Her face turns a purplish blue and her eyes begin to twitch. "
    "Her grip on my shirt loosens as the lack of oxygen in her coerces her body into kickstarting its shutdown process."

    f "Sensei...you have to...cum soon...or you’ll kill Makoto..."
    s "She likes it. You can feel how wet she is, can’t you?..."
    f "Mmf...mm~"
    f "Mhmm....she really...loves your dick..."
    f "But if she dies tonight...you’ll never be able to do this again...you’ll only have me..."
    s "And everyone else."
    f "Mmm! Mm...no...it’s only...us!"

    with sexfade
    with sexfade
    scene actualthreesome8 with cumflash
    with hpunch

    mak "{b}HAAAH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{/b}"

    "Just before Makoto passes out, I loosen my grip around her throat and fill her shallow hole with my seed."
    "She coughs and coughs and coughs until tears begin to flow from her eyes, joining the spit and the cum and sweat we’ve expelled while indulging ourselves in one more bout of uninhibited lust."
    "Her mother would be proud of her if only she were here."
    "But today, I have someone else to share the fruits of our endeavors with."
    "And even though they’re unrelated, the residual honey of our sins will not lose any of its sweetness when I make her drink it up."

    play sound "static.mp3"
    scene actualthreesome9 with flash
    stop sound

    f "Mm! Mmgh! Mmmmmmhh! "
    mak "Haaaah~"
    mak "Oh God...yes...drink it up, Futaba...Can you taste Sensei all over me?..."
    f "Mmngh!.......MMMMMMMMMMM!!!"

    "It only takes me five minutes to get hard again. "
    "Once I am, I tear off the girls' clothes with so much force that they snap and throw Futaba onto the stone structure that I have now discovered is a well."
    "I grab her waist and pull her forward, sliding myself into her with no hesitation before viciously pounding her wet cunt with so much force that the sounds of our skin slapping carry across a nearby lake."
    "Makoto, who is still regaining her breath at the time of this, needs help climbing up."
    "So I do what any sane man would do and lift her myself, placing her directly over Futaba’s face and demanding that the bookworm drink my seed from the brainiac."
    "She does not resist."
    "But it would have changed nothing if she did."

    f "Hngh! Mmf!.........MNGH! MMM!...........HHMMM!!!"
    mak "Oh...fuck...you’re...surprisingly good with...your tongue..."
    f "Mmnch!....Mmngh!!!"

    "Futaba’s skin ripples like waves in the ocean with each and every violent thrust."
    "My constant need to one-up myself compels me to fuck her harder each time I hear her voice, which leads to several cases where her face peels away from Makoto."
    "Between glances at her breasts and Makoto’s ass, I can make out strands of cloudy, white fluid clinging to the space where the two of them are connected."

    mak "Mmnhh...fuck yeah...fuuuuck...Futaba...ahhh!"
    f "Mmm....mmmnh!!!!"

    play sound "static.mp3"
    scene actualthreesome10 with flash
    stop sound

    mak "Just like...that...lick my pussy...just...be gentle...I’m still recovering from...Sensei..."
    s "You have to do her next, Makoto. It’s only fair."
    mak "Yes, [makotomaster]...I’ll do anything for you...anything you want..."

    play sound "static.mp3"
    scene actualthreesome11 with flash
    stop sound

    f "Mm..........."
    mak "Hah........hah!"

    play sound "static.mp3"
    scene actualthreesome12 with flash
    stop sound

    f "Huh?!"
    mak "No! What do you...think you’re doing?! I’m so close!"
    f "I-"

    play sound "static.mp3"
    scene actualthreesome13
    with flash
    stop sound

    mak "Get back...down there or...I won’t do the same for you!"
    f "Ckh...!....Mnchk!!!!!!!"

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    "We stop for a moment to let Futaba vomit and then make her go wash her mouth out in the lake."

    play sound "static.mp3"
    scene actualthreesome14 with flash
    stop sound

    "But then it’s right back to business."
    "I lose track of how many times I fuck the two of them."
    "And while Makoto may have held the lead in the very beginning for the amount of cum extracted from me, it becomes a bit of a game for us to toy with Futaba following her vomit incident."
    "We tease her..."
    "Force orgasm after orgasm out of her..."
    "And we laugh while doing it."

    scene black
    stop music

    "It’s the best dream I’ve ever had."

    $ futaba_lust += 5
    $ makoto_lust += 5

    "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
    "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
    "........."
    "......"
    "..."

    scene actualthreesome15
    with dissolve4
    $ totaldays += 1
    $ day = 2
    hide monday onlayer date
    show tuesday onlayer date
    $ renpy.pause(4, hard=True)
    scene actualthreesome16
    with dissolve3
    $ renpy.pause(3, hard=True)
    scene actualthreesome17
    with dissolve2
    $ renpy.pause(3, hard=True)
    scene actualthreesome18
    with hpunch
    play music "10c.mp3"

    mak "WHAT THE FUCK?!?!?!"

    scene actualthreesome19
    with dissolve

    s "Hm?..."
    mak "W...Where are my clothes? Where are {i}all{/i} of our clothes?!"
    s "What’s going on?"

    scene actualthreesome20
    with dissolve

    mak "Did...did you drug me?! What the fuck, Sensei?"
    f "Haaaaah......good morning....."
    mak "What do you mean “good morning?!” Were you in on this too?!"
    f "In on what?...Why are you yelling?..."
    mak "Uhh...Because we’re naked in the woods and covered in semen?!"
    f "We’re what?..."

    scene actualthreesome21
    with hpunch

    f "{i}WE’RE WHAT?!{/i}"
    mak "I’m just as confused as you are! Why would you date rape girls you’re already sleeping with?!"
    s "Futaba, why are you shielding my eyes from something I’ve seen a million times before?"
    f "Because this is embarrassing and confusing and I feel gross right now!"
    mak "What did you do?! {i}Why{/i} did you do?! WHY DO?!"
    s "Hey, I’m just as confused as you are. "
    s "But I guess since we’re already naked-"
    mak "GO TO HELL!"

    scene black
    with dissolve2

    f "Oh God! Oh no! I have like twenty missed text messages!"
    mak "And I have-"
    mak "I have...one."
    mak "Seriously? That’s it? What the fuck, Miku?"
    f "We...We can’t ever tell anyone about this. We have to forget it ever- ack. What’s in my mouth? Is this a hai- OH MY GOD. EW! NO! NO, NO, NO!"
    mak "Where did you put our clothes, you date raping bastard?!"
    s "I told you, I have no idea how this happened. I don’t even know where {i}my{/i} clothes are."
    mak "LIKE I’M GOING TO BELIEVE THAT!"

    stop music fadeout 15.0

    "The truth is that I did have an idea."
    "I remember everything from the moment I woke up here the first time to the moment I woke up the second."
    "It’s what comes {i}before{/i} it that I can’t remember."
    "But..."
    "That’s a trade I’m willing to make."
    "Because I’m sure whatever that was wasn’t significant at all."
    "And I’m sure it’s a memory I’m okay with parting with."
    "{i}Futaba and Makoto send Sensei back to the beach first so they can clean themselves off and repair their broken bathing suits.{/i}"
    "{i}He swears to himself along the way to never tell a soul about this.{/i}"
    "{i}And prays to a god he does not believe in that the two of them never remember the details.{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ makotofutabafuntimelustevent = True

    jump beachmas12

label futabaspecial60p1:
    scene black
    with dissolve
    play sound "knock.mp3"
    stop music fadeout 5.0

    "I knock on Futaba’s door and wait for her to answer..."
    "But she never does. "
    "And I go home without accomplishing anything."
    "........."
    "......"
    "..."
    "{i}A few hours later, on the other side of town...{/i}"
    "{i}And roughly one hundred feet underneath the surface...{/i}"

    scene futabalikesbooks1
    with dissolve2
    play music "lifeismostlygood.mp3"

    mo "And so concludes another successful adventure! This time, without anyone being forced out of their comfort zone or..."
    mo "Or up against the door of a crowded train."
    f "You’ve been playing “those games” again, haven’t you?"

    scene futabalikesbooks2
    with dissolve

    mo "Aye! But that has naught to do with my anecdote and {i}everything{/i} to do with why I must still {i}rely{/i} on those games! But I digress!"
    f "Well...I’m glad you had fun, Molly. It was certainly a...productive trip, if not anything else."

    scene futabalikesbooks3
    with dissolve

    mo "Did you wind up getting everything you need for your costume? Because I’m hoping to start work on them Monday and I’m...actually not even sure if I know what you’ll be going as this year."
    f "Yeah...that’s kind of the problem. I’m not really sure what to do this time around. So while you and Yasu were fabric-shopping, I was..."
    f "I was...buying...{i}other{/i} things..."

    scene futabalikesbooks4
    with dissolve

    mo "You went into {i}that{/i} section without me?! How could you?! And...how {i}did{/i} you?! They always stop me whenever I try!"
    ya "If you were shopping for naughty things, God will find out and replace your arms with snakes. He sees all."
    f "What?! No! I was talking about books!"
    mo "Then why would you make it sound like you were doing something so impure?! I know lewd emphasis when I hear it!"
    f "Because I...I was talking about {i}those{/i} kinds of books, Molly. The ones Yasu isn’t allowed to read yet."
    ya "Do they contain inappropriate content?"

    scene futabalikesbooks5
    with dissolve

    f "Hah...yes, Yasu. Yes they do."
    ya "Hmph. I hope you enjoy your snake arms."
    mo "Tch. You should’ve just said that from the start so I didn’t get my hopes up."
    mo "If you need recommendations for a costume, though- I’d be happy to help, Futaba. I started work on a Kafka costume for Tsuneyo but I had to bench the idea because it kept making me {i}feel things.{/i}"
    f "I don’t think I...have the energy or confidence needed to pull that character off."

    scene futabalikesbooks6
    with dissolve

    mo "What are you talking about? You pulled Himeko off just fine and she practically bleeds confidence. "
    f "Yes, but she also has a certain amount of...motherly energy that Kafka lacks. And I don’t want to walk around the Halloween party pretending that I like to...step on people."
    mo "Don’t knock it ‘til you try it, Xessaxia. At the rate you’re consuming those smut novels, you could very well unlock new aspects of your personality that even {i}I{/i} would gawk at."
    f "Shh...we have a child with us, Molly. We can’t exactly talk about the things that “even you would gawk at.”"
    mo "Nonsense. Yasu might be a child {i}now,{/i} but it’s only a matter of time until she has the same secret folders on her laptop that {i}we{/i} do."
    ya "I abstain from using technology as it exposes me to information that has not yet been filtered through Him and opens me up to being falsely guided."
    ya "Also, Touka says I’m not allowed. But I don’t want to anyway."
    f "Like I said...there is a child present."

    scene futabalikesbooks7
    with dissolve

    mo "Hah...at this rate, I’ll be bitin’ the feckin’ bullet and just finishin’ the costume for Tsuneyo. Fantasies be damned."
    mo "You’ve gotta figure something out sooner rather than later though, Futaba. The party’s right around the corner at this rate and if I don’t know what you’re after, I might not be able to help."
    f "It’s fine, Molly. I’m nowhere near your level, but I still know my way around a sewing machine and can always just make my own costume if I really have to."
    f "Besides, my interests are...{i}elsewhere{/i} for the time being."

    scene futabalikesbooks8
    with dissolve

    mo "How many of those books have you even read so far? I feel like that’s all you ever do now. It’s like you’re not even a real otaku anymore."
    f "I still keep up with the things we’re reading in club. But, as far as my personal books go, maybe...fifty this year? "

    scene futabalikesbooks9
    with dissolve

    mo "Friggin’ Christ, that many?! I don’t think I’ve read fifty books in my life."
    f "It’s not as much as it sounds. Just compare that to how much anime you watch. "
    f "I can finish most books in less than a week, so the time commitment isn’t nearly as bad as having to devote three months of my life to another unoriginal harem comedy."
    mo "You leave the bread and butter of the anime industry out of this. Just because you’re becoming a normie doesn’t mean you get to talk down on us now. I won’t allow it."
    f "Trust me, if you knew what I bought today, you would certainly {i}not{/i} be calling me a normie. "

    scene futabalikesbooks10
    with dissolve

    mo "I am suddenly intrigued..."
    ya "And I am suddenly being tested again. But my faith knows no bounds, so your evil books will not tempt me."
    f "Well, let’s put it this way- Nodoka wrote it. And, as I’m sure you know, she’s not exactly the most “wholesome” girl out there."

    scene futabalikesbooks11
    with dissolve

    mo "Nodoka? Like, {i}Nodoka{/i} Nodoka? The Goddess of Impurity herself? I knew she was a writer, but I didn’t realize she was actually {i}published.{/i}"
    f "I’m pretty sure she had her first work published when she was around...ten years old, I think? I’ve lost track of how much she’s put out since then. She never tells me about any of her new releases, though. "
    f "I think she’s, like...trying to “preserve my innocence” or something. But, at this point, all innocence I once had is gone and I am now an all-encompassing ball of impurity that rivals even the Goddess herself."
    ya "There is but one God and He is unrivaled. This is heresy of the highest degree."
    mo "How...{i}long{/i} is this book, exactly?"

    scene futabalikesbooks12
    with dissolve

    f "I’m not sure. Normal novel length, I guess? I don’t really know anything about it. But I’ll let you borrow it once I’m done if you want."
    f "She’s an extremely talented writer, but I don’t think I’ve ever actually finished anything she’s done before as her...{i}raciness{/i} was a little too much for me before I got into romance novels."
    f "I think I’m ready now but, then again, this {i}is{/i} Nodoka we’re talking about- so it’s equally possible that I’m going to put it down within minutes and be overcome by the urge to take a shower."
    mo "If this pseudo-normie book of hers is anything even remotely close to that last thing you said, I would very much like to borrow it."
    ya "And I would very much like to burn it as it sounds like something that should not exist."

    scene futabalikesbooks13
    with dissolve

    f "It’s just a book, Yasu. And even if you disagree with what’s inside of it, burning it won’t do anything. We should be preserving literature of all types, not {i}destroying{/i} it."
    ya "A terrible fate will befall you if you read this book. I can hear it in the screeching of the train upon the tracks. And the voice of my God tells me you must stay away."
    mo "Which reagents did you use to cast Divination just now? I need to make sure they’re worth at least 25 gp."
    ya "The air and all the thoughts within it."
    mo "I’ll allow it."
    f "Yasu, it’s fine. Like I said, it’s just a book. If worse comes to worst and I feel a “terrible fate” creeping up on me, I can just put it down."

    scene futabalikesbooks14
    with hpunch

    ya "You do not understand! You are making the wrong choice! You’re damning us all!"
    mo "N-Nothing to see here, folks! She’s never been on a train before! She doesn’t know how this works!"
    f "Yasu, shh! You can’t do that in here. Yelling is fine, but only if you wait until we get off, okay?"
    ya "But you-"
    f "Shh!"

    scene black
    with dissolve2
    stop music fadeout 15.0

    f "We can talk when we reach our stop..."

    "........."
    "......"
    "..."

    scene futabalikesbooks15
    with dissolve

    f "{i}Hah...{/i}I’m glad {i}that’s{/i} over. Yasu’s always a handful, but I wasn’t expecting her to flip out on me like that."
    f "I guess Molly and I will just have to talk about this in secret if she {i}does{/i} wind up borrowing it."

    scene futabalikesbooks16
    with dissolve

    f "That’s not important right now, though. It’s finally time to read."

    play sound "dooropen.mp3"
    scene futabalikesbooks17
    with dissolve

    ri "Ughhhhh...having a job is hard."
    f "Or not."
    ri "Futabaaaaa...rub my shoulders..."

    scene futabalikesbooks18
    with dissolve
    play music "sleepystreets2.mp3"

    f "Welcome home, Rika. I take it you...had an exhausting day?"
    ri "Exhausting is putting it lightly. I feel like I’m gonna die. "
    f "And...and what did you have to do exactly? Because I was...under the assumption your only responsibility was...being the advisor for the light music club."
    ri "Yeah but nobody ever told me how much advice they’d need. And what’s even worse is I already forgot where the ropes are."
    f "And...what did you need ropes for exactly?"

    scene futabalikesbooks19
    with dissolve

    ri "Putting an end to my misery..."
    f "Please don’t. "
    ri "You want me to be miserable forever?"
    f "No...I want you to remain alive because I love you and Rin loves you. But, if it’s not too much trouble, I’d really like it if-"

    scene futabalikesbooks20
    with dissolve

    ri "Whatcha got there?"
    f "If I could read in peace for a little while."
    ri "The Light of...Last...hey, wait a minute. I know this book."

    scene futabalikesbooks21
    with dissolve

    f "You...you do?"
    ri "Yeah, I was at the signing event for it. Were you there too?"
    f "No, I...I just got it today. And I didn’t even realize you read books, Rika."

    scene futabalikesbooks22
    with dissolve

    ri "I don’t."
    f "..."
    ri "..."
    f "Then...why were you at the signing exactly? And...where even {i}was{/i} this signing? I would have liked to have gone."
    ri "Some book store. I don’t really remember. I just saw a line and got into it thinking there’d be something exciting at the end. And I guess I wasn’t wrong since there were a bunch of single women there, but..."

    scene futabalikesbooks23
    with dissolve

    ri "But all that did was awaken further darkness within me..."
    f "I’m sure you’ll...find someone else soon enough. And...hopefully somewhere else to stay."

    scene futabalikesbooks24
    with dissolve

    ri "What, are {i}you{/i} trying to get rid of me too now? I can’t even count on my second daughter to back me up while I’m homeless?"
    f "I didn’t really mean that. You can stay here as long as you like. I was just kind of hoping I’d be able to read in peace tonight since Rin is working late. "
    ri "Are you calling me loud and unwanted? Does my presence bother you, Princess Futaba?"
    f "Your presence does not “bother me,” Mistress Rika. I simply require some alone time."
    ri "Are you even old enough to be reading this kind of stuff? Do I need to call your parents and tell them their daughter’s starting her “bad girl” phase?"

    scene futabalikesbooks25
    with dissolve

    f "You definitely don’t have to do that. In fact...{i}please{/i} don’t do that. I’d much prefer that the types of books I’ve been reading lately aren’t really divulged to or...known by {i}anyone.{/i}"
    ri "Except your best friend’s mom, who now knows you’re up to no good."
    f "Yes. Except my best friend’s mom, who now knows I’m up to no good."

    scene futabalikesbooks26
    with dissolve

    ri "Well, I {i}was{/i} planning on hitting the hay a little early tonight. But, considering you want your “alone time,” I guess I can see what Wakana and Imani are up to. Maybe Sensei will be there too."
    f "Are you and him getting along well?"

    scene futabalikesbooks27
    with dissolve

    ri "I...think so? Maybe?..."
    f "..."
    ri "I thought we were, but...I’m not really sure how he sees me anymore."
    f "Did...something happen?"

    scene futabalikesbooks28
    with dissolve

    ri "Nothing you need to be worried about, kiddo. Aunt Rika’s just not the best when it comes to the impressions she gives people sometimes."
    f "Well, if it means anything, {i}I{/i} think you’re great. And I’m sure Sensei will see that too. "
    ri "Hope so, kid. Hope so."

    scene black
    with dissolve2

    ri "Anyway, I’m out! Enjoy your book. That author girl was weird as shit. And she looks {i}mad{/i} similar to your friend with the glasses on the second floor."
    f "I’m sure that was just a...coincidence..."

    play sound "dooropen.mp3"

    ri "Night, Futaba! Don’t stay up too late. "
    f "Goodnight, Rika! Take your time coming home. I’m hoping to get at least the first half of this done tonight, and I have absolutely no clue how long that will take."
    ri "Those other girls seemed to like it a lot, so I’m sure it’ll be a good time even if it’s quick. Like that time I fingered the singer of-"
    f "Okay, Rika! Bye!"
    ri "Sorry! Bye! Have fun!"
    f "I’m sure I will."
    f "{i}I’m sure I will...{/i}"

    $ renpy.end_replay()
    $ futabaspecial60p1 = True

    "{i}One hour later...{/i}"

    jump futabaspecial60p2

label futabaspecial60p2:
    stop music
    play sound "static.mp3"
    scene parrotpicture1 with flash
    scene parrotpicture2 with flash
    stop sound
    play sound "doorslam.mp3"
    scene futabanodokabook1 with hpunch

    f "What the fuck is this?"
    o "Uh-oh."
    no "Well, hello Futaba. You’re looking lovely tonight."
    f "Nodoka, what the fuck is this?"
    no "I believe that is called a “book.” "

    play music "pianomelancholy3.mp3"
    scene futabanodokabook2 with hpunch

    f "Nodoka!"
    no "You don’t have to yell. I’m right here. You asked what it was and I told you what it was. I’m not sure what else you want from me."
    f "I want to know what possessed you to write this! That’s what!"

    scene futabanodokabook3
    with dissolve

    no "Artistic vision, I suppose? The endless font of creativity that is my brain? The abundance of hormones flowing through my body like blood due to living in a dorm with nineteen other girls?"
    no "The possibilities are endless. {i}Anything{/i} could have compelled me to write that book. The motivation matters not, though. It’s the story itself that I want people to dissect."
    f "I {i}know{/i} the story already. That’s why I want to know why you’re doing this."
    no "Because it’s interesting, obviously. I wanted to try a new approach to things."

    scene futabanodokabook4
    with dissolve

    no "And, based on the fact that you bought it, it looks like I’ve succeeded. Thank you very much for supporting my work, Futaba. It means a lot to me."
    f "Is this a joke to you? Do you not see how serious I am right now?"
    no "I see exactly how serious you are. But I also know that it’s only a matter of time until everything clicks and you realize that this is, in no way, meant to be malicious or evil."
    no "Tell me, how far into the book did you make it before you stormed over to my room? You’re the first person involved who’s actually {i}read{/i} it, so I’m genuinely curious."
    f "Otoha, get out."

    play sound "dooropen.mp3"
    scene futabanodokabook5
    with dissolve

    o "Yup. Bye."
    f "I can’t believe you...Why would you do something like this? "
    f "Has your creativity dried up? Have you gotten so tired of coming up with your own stories that you had to steal {i}ours{/i} instead?"
    no "Quite the opposite, actually. And it’s not as if my new series is a perfect retelling. I can’t be everywhere at once, of course. "
    no "Some...creative liberties needed to be taken to compensate for things I wasn’t present for."

    scene futabanodokabook6
    with dissolve

    f "I have known you for a {i}very{/i} long time, Nodoka. I’ve seen you make questionable decisions and I, more than anyone, understand what type of person you are."
    no "I am sensing a disconnect between your words and your actions right now. If you understand, what’s there to get so up in arms over?"
    f "I have stuck up for you {i}countless{/i} times. I’ve fought for you when no one else “got it.” And I’ve been calling you one of my biggest inspirations for years."

    scene futabanodokabook7
    with dissolve

    f "But {i}this?...{/i}I don’t understand. {i}Why?{/i} "
    no "I believe “Why not?” is just as valid of a question here if you’re unable to come up with an answer yourself, Futaba. What do you believe is wrong about writing a story based on one’s experiences?"

    scene futabanodokabook8
    with dissolve

    no "Is that not one of the many methods of tackling fiction? "
    no "Drawing parallels between real life and make-believe worlds? Connecting them in new, thought-provoking ways? Teaching people lessons they’d never learn otherwise?"
    no "For what reason would I {i}not{/i} write this book? There’s simply far too much I’m able to teach with its concept for me to just {i}overlook{/i} it or actively decide {i}against{/i} it."
    f "It’s an invasion of privacy, Nodoka. I don’t want my whole life inside one of your books. And that’s not even mentioning how anyone else would feel if they read this..."

    scene futabanodokabook9
    with dissolve

    no "Then I suppose I should be happy that it’s only you and I who regularly read. Besides, I’m sure the unnamed masses will take something from it. It doesn’t need to be {i}us{/i} per se. "
    f "It’s just...it feels so...{i}invasive.{/i} And I’m only three chapters in."
    no "Oh, wow. So you haven’t even gotten to the {i}good{/i} parts yet. I’ll have to put that in my notes."
    f "You’re really going to keep going through with this?"
    no "Of course. You haven’t given me a good reason not to yet."

    scene futabanodokabook10
    with dissolve

    f "Then...if I say I’ll stop talking to you if you follow through with this...is {i}that{/i} a good enough reason? "
    no "Good? No. Threatening? Yes. Losing you is an outcome I’d like to avoid if at all possible. But I also believe I know you well enough by now to ascertain that this is a bluff of sorts."
    no "I believe the whole truth is that you will do absolutely nothing if I continue to publish this book as doing so would go against your character."

    scene futabanodokabook11
    with dissolve

    f "You only know that because I {i}am{/i} just a character to you, aren’t I?! I’m just a pawn you can move around in your book to keep your story interesting!"
    f "If you actually cared about me, you wouldn’t...dehumanize all of us like this!"
    no "You’re likely only saying that because you haven’t reached {i}your{/i} character’s introduction yet. Read that before condemning me as some sort of malicious chess master."

    scene black
    with dissolve2

    f "Fine. Where do I-"
    no "Page 99. Much of the book is a blur to me as it was written while I was mentally exploding, but I remember that one."

    play sound "pageturn.mp3"

    f "{i}Hah...{/i}"
    f "Fubuki was a breath of fresh air — a lone butterfly in an eclipse of moths. But if you asked her, she’d likely tell you she was nothing more than a caterpillar."
    f "Despite that, she wasn’t the type of girl to stand out in a crowd. She didn’t {i}need{/i} to be, though. "
    f "In fact, it was probably better she clung to the background as it meant {i}my{/i} eyes could taint her the most."
    f "But...even with that said...she was so pure and so beautiful that it would take...years of gazing into {i}hers{/i} to make even the slightest change..."
    f "Nodoka, this doesn’t-"
    no "Keep reading. "
    f "{i}Hah...{/i}She had trouble accepting love because she felt it was misdirected. But the only reason she felt that way at all was...was because of the eclipse..."
    f "She’d spent so long among the moths that...each flap of her wings served {i}not{/i} to guide her deeper into the mouth of the sky, but...further away from the light the others flocked to."
    f "The sad reality at play here is that she would have glowed brighter than any of them. That she {i}would{/i} stand out if she only allowed herself to..."
    f "But alas...the scourge of undesired uniqueness makes it harder to break free from refurbished chrysalides. And so the...never-ending cycle of misplaced doubt went down with the moon-"
    f "Only to rise again the following night."

    scene futabanodokabook12
    with dissolve2

    no "{i}How I long to be a new light — one that guides her to the deepest lakes of sugar water so she can drink in me and feel renewed.{/i}"
    no "{i}If only those wings would stop getting caught on themselves...if only I was brighter.{/i}"
    f "..."
    no "That wasn’t all bad, was it?"

    scene futabanodokabook13
    with dissolve

    f "No...it was very sweet. But it changes {i}nothing,{/i} Nodoka. You did this without even talking to any of us. "
    no "Why would I do that? You’d all just refuse to participate and then I wouldn’t have a book at all."

    scene futabanodokabook14
    with dissolve

    f "That’s the whole point! You’re doing something that you {i}know{/i} none of us would agree to, and yet you’re not seeing any sort of issue with it!"
    no "Yes, because it isn’t up to any of you to determine what I do or do not write. If something piques my interest, I’m inclined to dive further into it. I assumed you’d know that by now."
    f "I do, but that doesn’t mean I have to like it!"
    no "I’m confused. No one is asking you to {i}like{/i} it. And it seems as if you’re taking exception to the existence of such a trait all on its own."
    f "That trait is fine when it’s not causing you to spill all of our secrets into a book! This doesn’t do any good for anyone but you!"
    no "It’s not as if I’m exempt from exposing {i}my{/i} secrets as well, Futaba. There’s no author bias here. I’ll be just as naked as the rest of you come the final installment."

    scene futabanodokabook15
    with dissolve

    f "But Nodoka...none of us should {i}be{/i} naked. Our secrets are meant to be {i}secrets.{/i} They’re not building blocks for your fictional exposé."
    no "They quite literally are though."
    f "What?"

    scene futabanodokabook16
    with dissolve

    no "Well, the idea of an exposé is to reveal the true nature of something. So even if you tack a prefix like “fictional” onto it, it’s still fulfilling a key purpose by bringing a certain truth to light."
    no "And truth is determined by history. Which is determined by specific examples and accounts from real life events. "
    no "But I suppose things get muddier when there is an assumption to be made about truth in the context of a fictional world."
    f "What?...I didn’t understand any of that."
    no "Sorry, I’m trying to figure out a way to explain it that would be coherent to someone else."

    scene futabanodokabook17
    with dissolve

    no "But I suppose the gist is that the “secrets” you and everyone else share are the closest I can get to examples and accounts of real life happenings."
    no "Which could then become building blocks to better lay out my fictional reconstruction of our reality so it can be shared and understood by people who aren’t with us to experience it firsthand."
    f "Why do other people have to experience it at all? Why can’t it just be for us?"
    no "Because people like {i}us{/i} live for this. We need stories like this to exist because life isn’t interesting unless we can compare and contrast it with a fabricated version."
    no "Out of the hundreds of books you’ve read, I’d wager at least half of them were someone’s reality at some point. What I do is no different from that. You’re just on the opposite end for once."
    f "Nodoka, {i}I don’t like being on the opposite end.{/i} I don’t want people to know how I feel or what I’m doing. And I’m afraid of what will happen to me if people find out."
    no "Then why are you doing such a piss poor job of hiding it all?"

    scene futabanodokabook18
    with dissolve

    f "{i}Excuse me?{/i}"
    no "I’m just not sure I understand the rationale behind revealing your truths to someone else if you don’t want anyone to {i}know{/i} those truths. It’s no longer a secret once it crosses your tongue, correct?"
    f "So because I shared something with you...something I told you in confidence because you are my {i}friend...{/i}it means that I don’t understand what a secret is? That I want {i}everyone else{/i} to know?"
    no "But...no one else knows. All I did was use {i}your{/i} experiences to create {i}new{/i} ones for {i}someone else.{/i} And if that someone else is a product of my imagination, shouldn’t I be able to share those things?"

    scene futabanodokabook19
    with dissolve

    f "No! Because it’s not someone else! It’s us! It’s me! That’s what I’ve been trying to tell you this whole time! So you’re either trying to manipulate me right now or you just flat out lack common sense!"
    no "Which one of those two do you think it is?"
    f "I don’t care which one it is! I just want it to stop!"
    no "Then stop clutching the book so close to your chest and just burn it or something. No one is forcing you to read it. That’s a decision you made yourself."

    scene futabanodokabook20
    with dissolve

    no "In fact, I’d {i}urge{/i} you to stop reading it if the first three chapters were enough to impact you to this extent. It only gets messier from then on, Futaba. "
    no "I’m sure you know that already, though. But hey, maybe if you {i}do{/i} continue, you’ll enjoy seeing things from someone else’s perspective as it will show you just how everyone else views {i}you.{/i} "
    f "I seriously can’t believe you...you’re not getting it at all. You don’t see {i}any{/i} problem with this."
    no "I see that...{i}you{/i} have a problem with it. And acknowledge that others directly involved may as well."
    no "But I’d also implore all of those people, yourself included, to remember that this book is just, for lack of a better word-"
    no "A rectangle."
    no "And it will remain a rectangle until someone comes along and sees it as anything else. "
    f "Unbelievable...You’re seriously unbelievable."

    scene futabanodokabook21
    with dissolve

    no "See, this is precisely why I never make a big deal out of anything I do. No one else ever looks at things the same way as me. "
    no "It’s incredibly exhausting never getting through to people when that is quite literally my job."
    f "You know what else is exhausting? Having a best friend who cares more about {i}herself{/i} than your feelings."

    scene futabanodokabook22
    with dissolve

    no "Would you not do the same? Just because you prioritize yourself over someone else doesn’t mean that you don’t love them. "

    scene futabanodokabook23
    with dissolve

    no "And I-"
    f "..."
    no "...Futaba?"
    f "..."
    no "Why are you crying? Was it something I said?"
    f "I hope you’re happy, Nodoka."
    f "I really hope you are."

    scene futabanodokabook24
    with dissolve
    play sound "dooropen.mp3"
    stop music fadeout 8.0

    no "Futaba, wait. I don’t think you’re necessarily understanding what-"

    play sound "doorslam.mp3"
    scene futabanodokabook25 with hpunch

    no "..."
    no "..."
    no "..."

    scene futabanodokabook26
    with dissolve2

    no "..."
    no "..."
    no "Huh."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ futabaspecial60p2 = True

    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 1
    hide sunday onlayer date
    show monday onlayer date

    jump futabaspecial60p3

label futabaspecial60p3:
    scene futabatired1
    with dissolve2
    play music "10c.mp3"

    "A wise man once said “Knowledge is power.” "
    "But I'm not very wise. So {i}I{/i} say, “Knowledge is annoying.”"
    "Not just because it eats up a good portion of my daily life now, though. It’s more so the fact that learning about some guys with weird hair who existed a long time ago isn’t going to change anything."
    "Or...at least it wouldn’t change anything in most contexts. Frankly, knowing more about the past iterations of {i}me{/i} might change my behavior in some way, but...in most contexts, history is just history."
    "The past (Again, in most contexts) will only repeat to a certain extent."
    "And learning things like when a castle was seized or some man was executed isn’t going to prevent things like that from happening in the future."
    "Wherever man exists, turmoil will follow."
    "And for that reason, I will continue to zone out as Imani speaks and pay more attention to Kirin slowly unbuttoning her shirt while staring at me."
    "I wonder how far she’ll go?"

    ima "...and while the seizure of Heiankyo, or “Kyoto” as we refer to it today, brought an end to the Warring States period, Nobu-kun still had a bunch of work to do in terms of stabilizing Japan."
    ima "So with this brand new territory added to his ever-growing list of cool hang-out spots, he set his sights on the remaining Ashikaga shogunate, but would not finish the job until five years later."
    ima "Now, for extra credit on the test we aren’t going to take on this, can anyone tell me the {i}name{/i} of the final Ashikaga shogun? "
    mak "Yes! Pick me!"
    ima "Can anyone {i}who hasn’t answered every single other question{/i} tell me the name of the final Ashikaga shogun?"
    ki "I can!"

    scene futabatired2
    with dissolve

    ima "Then, Kirin-"

    scene futabatired3
    with dissolve

    ima "Bitch, what you doin’ over there? Button up yo’ God damn shirt."
    ki "Oh, whoops. "
    ima "“Whoops” my ass. You know better than to strip in class. I bet you don’t even know the name of the shogun, do you? You were just trying to make me lose my job."
    ki "I {i}do{/i} know actually. It’s Ashikaga Yoshiaki. And, if you want his parents’ names as well, they were Ashikaga Yoshiharu and the daughter of Konoe Hisamichi, Keiju-in."

    scene futabatired4
    with dissolve

    ima "Man, see what you’re capable of when you quench your thirst? That was a genuinely good answer. Ten points to the second floor."

    scene futabatired5
    with dissolve
    play sound "slidedoor.mp3"

    mak "Points?! Nobody said there would be points! But surely my floor must have more than the other on account of how many correct answers I’ve had today. "
    ima "Nah. Score’s ten to zip right now. But you’ll have plenty of time to catch up. "
    f "Sensei?"

    scene futabatired6
    with dissolve

    s "Yeah? What-"

    play sound "static.mp3"
    scene futabatired7 with flash
    stop sound

    s "Woah, what the hell happened to {i}you?{/i}"
    f "Can I borrow you for a minute? In private, please."
    ima "Jesus, Futaba. You look like you were hit by a truck. Shouldn’t you go to the nurse’s office instead?"
    f "That won’t be necessary, Miss Imai. I just need to talk to Sensei for a minute. It won’t take very long."
    s "Is...everything alright?"
    ima "Bro, look at her. You really think everything is alright? Hell nah. We’ve gotta find the truck driver who did this. Ain’t nobody messing with my girls during school hours."
    f "Sensei? Now?"

    scene black
    with dissolve2
    stop music fadeout 10.0

    s "Sorry, Imani. I can’t head the class anymore. You’re going to have to take over for me."
    ima "This {i}motherfucker{/i} really just said, “I can’t head the class anymore.” Ain’t no way. While I’ve got the stick in my hand and everything."

    play sound "slidedoor.mp3"

    s "I’m glad you understand. Come on, Futaba."
    ima "Yeah, yeah. Guess I’ll just keep doing the same damn thing I’ve been doing this whole- Kirin! Button your damn uniform! I ain’t telling you again!"
    ki "Booooooo! Free the nipple! Imani’s not progressive enough!"
    ima "Y’all really just ignoring the stick, huh? "

    "........."
    "......"
    "..."

    scene futabatired8
    with dissolve2

    f "..."
    s "..."
    f "..."
    s "W-"

    play music "beyondthewayoftime.mp3"

    f "Just a little tired, that’s all. "
    s "You didn’t even give me a chance to say anything."
    f "I already knew what you were going to say. And also, thanks for letting me talk to you in here outside of your regular office hours. I realize that must be kind of annoying for you."
    s "Well, it’s not like you show up {i}during{/i} office hours anymore...so this is nice. It’ll let us catch up a bit. Which, by the look of it, we kind of {i}need{/i} to."
    f "Yes, I bet you’re wondering why I dragged you away from the class. Or why I didn’t do my hair today. Or anything else you might be wondering because I’m clearly not acting like myself."
    f "And I know that. I’m well aware of it. Rin told me the same exact thing when she got home last night. Minus the hair part because I'd done my hair earlier that day."
    f "But anyway, when I explained to her {i}the reason{/i} I was acting differently, she just went to sleep upstairs instead. I wonder why?"
    s "Did...something happen?"

    play sound "static.mp3"
    scene futabatired9 with flash
    stop sound

    f "Why, yes. What gave it away?"

    "Futaba’s eyes, which are normally so full of life, now appear more like those of a dying fish or a creature from the pages of some sort of horror manga."
    "She stares through me. And, for the first time since I’ve met her, I feel...intimidated. "
    "But I also feel like this doesn’t have anything to do with me. "
    "There’s no murderous intent in those lifeless fish eyes — just a tinge of desperation and..."
    "Hopelessness. "
    "And I {i}know{/i} hopelessness. I’d recognize it from a mile away. Some may even call me an expert. "
    "But what would make {i}this{/i} girl feel that way?"

    f "Wow. You look just as bad as I do right now."
    s "I think that’s on you. I’m not exactly fond of staring at you when you look like this."
    f "Do you not think I’m a butterfly?"
    s "...What?"
    f "Would I stand out in an eclipse? Am I moving too far away from the mouth of the sky?"
    s "Uhh...what-"
    f "It doesn’t matter. But I have news for you. Bad news. News that puts you and everyone else in danger."
    s "It’s not about the end of the world, is-"
    f "I have news for you. Bad news. News that puts you and everyone else in danger."

    "Well...I guess it’s not that."

    s "What’s the news, Futaba?..."
    f "It’s Nodoka. "
    f "She knows everything."
    f "None of our secrets are safe. None of them."
    s "..."
    f "..."
    f "Are you not going to say anything?"
    s "You found out about her book, didn’t you?"

    scene futabatired10
    with dissolve2

    f "..."
    s "..."
    f "You {i}knew?{/i}"
    s "I did. Just like I knew she was trying to keep it from you because “you wouldn’t understand” or something like that."
    f "So...you’re fully aware that Nodoka is {i}publishing a book{/i} where you go around {i}sleeping with your students...{/i}and you’re just...okay with it?"
    s "I mean...{i}okay{/i} isn’t exactly accurate. I think it’s a complete invasion of privacy and it weirds me out, but..."
    s "At the same time, it’s not like I can stop her from writing what she wants to write. I can just...not read it."
    f "..."
    s "..."
    f "Are you out of your mind?"
    s "Futaba?"

    scene futabatired11
    with dissolve

    f "Are you out of your fucking mind?! Are {i}all{/i} of you insane?! Are all of you just {i}okay{/i} with this?!"
    s "Hey, calm down. Someone is going to hear you."
    f "So you care about {i}that{/i} but not a detailed recollection of every single girl you’re involved with?! How does that make sense?!"
    f "What’s in {i}there{/i} is way more damning than anything {i}I{/i} could possibly say to you! I’m just one piece of the puzzle!"
    s "Sure, but it’s still a {i}puzzle.{/i} You have to solve puzzles."
    f "Oh, give me a break! It’s a puzzle with like, twenty pieces max. Anyone in our class with half a brain will be able to figure out what her book really is by the second chapter."
    s "Then I guess we should be thankful that only half of our class is smart."

    play sound "static.mp3"
    scene futabatired12 with flash
    stop sound

    f "You and Nodoka both! How can you make jokes about this?! We’re {i}all{/i} screwed if the truth about this fucking book gets out!"
    s "No, {i}I’m{/i} screwed if the truth about this book gets out. The rest of you will be fine."

    scene futabatired13
    with dissolve

    f "Oh! Will we?! So people like Chika and Ami will just be totally cool with people like {i}me{/i} sleeping with you because {i}you’re{/i} taking the hit for all of us! Okay! I had no idea it worked that way!"
    s "I...I guess I didn’t think of it like that."
    f "Yeah. Of course you didn’t. Because you already know the risks that come with doing what you do and you continue to do it anyway. "
    f "But do you think {i}I{/i} had any idea what I was getting into when I started hanging out with you? All I did was look up to you. I thought you were handsome and interesting."
    f "I had no fucking clue that you wanted me to suck your dick! And I also had no clue that I’d do it so easily, but here we are! Here we are, Sensei!"
    f "Do you seriously think I’m ready for everyone else to find out about this? Do you think they’ll just let me off the hook because I’m {i}nice?{/i}"
    f "Or do you think that {i}maybe{/i} this will make me a target again?! {i}I’m{/i} the outlier! {i}I’m{/i} the easiest one to come after! But we’re {i}all{/i} going to be fucked!"
    f "No one can read this! We have to put an end to it before it gets out of hand! "
    f "There’s still time, though! We’re the only ones who know right now. And Rika. And I guess Molly and Yasu too, but they don’t really know the contents of-"
    s "Rin and Otoha know too, Futaba."
    f "..."
    s "I mean...why else would Rin have just left when you told her what was going on last night?"
    f "..."
    s "..."

    scene futabatired14
    with dissolve2

    f "Hahah..."
    s "..."
    f "Hahahah...hahahah!"

    play sound "static.mp3"
    scene futabatired15 with flash
    stop sound

    f "Hahahaha! HAHAHAHAHA! AaaaaaaaAAAAAAHHHHHHHH! "
    f "We’re all fucked and no one cares but me! Amazing!"
    s "Futaba...how much of the book did you read, exactly? Because I know it’s about all of us, I just don’t really know the...{i}extent{/i} to which our “exploits” are included."
    f "She knows everything. She knows literally everything because she’s a fucking genius and all she does is watch people. "
    f "She knows how I think. She probably knows how {i}you{/i} think. She knows how {i}everyone{/i} thinks because she made it her reality. She can see into our heads, Sensei. "
    f "And you want to know the worst part?"
    s "..."

    scene futabatired16
    with dissolve2

    f "It’s {i}good.{/i}"
    f "It’s really...{i}really{/i} good. "
    f "I couldn’t even put it down. Well, at least not after the first time when I went into her room to yell at her. But after that, it was just straight to the end. And I loved it. But I also felt fucking {i}violated.{/i}"
    f "That’s why I didn’t sleep. I read the whole thing in one night. And I want to read it again. I want to know more about what everyone else thinks because I can...I can feel it changing the way {i}I{/i} do."
    s "Futaba...what if the reason this is affecting you so much is because you’re Nodoka’s favorite?"

    play sound "static.mp3"
    scene futabatired17 with flash
    stop sound

    f "If I was her favorite, she wouldn’t include me at all! She wouldn’t just rewrite the things I told her in confidence! She wouldn’t just {i}give away{/i} my secrets! "
    f "But she did all of those things! And she did them {i}well!{/i}"
    s "But what I’m saying is she probably did them {i}well{/i} because she’s been watching you forever, hasn’t she? She knows how {i}you{/i} think because she knows {i}you.{/i}"
    s "And without knowing how anyone else reacts to this weird alternate reality she cooked up, we can’t know for sure just how accurate her re-tellings are."
    s "There’s no way Nodoka can just {i}know{/i} things she wasn’t there for. So I imagine all of your parts are accurate because...well, you told her."
    f "You should read it, Sensei. You should find out. I only know so much, but you’ll know {i}everything.{/i} You’ll know what’s made up. "
    s "Do you really think I want to read a book about all of the horrible things I’ve done? I’m a narcissist, not a masochist. There’s nothing I could gain from that book but reminders and regrets."
    f "Do you regret me, Sensei? "
    f "Because right now, I’m regretting you."
    f "And if the way you feel about me is at all what it’s like in the book, I..."

    scene futabatired18
    with dissolve

    f "I..."
    s "..."
    f "I don’t even know..."
    s "..."
    f "I knew I didn’t value myself. I’ve {i}never{/i} valued myself. And I gave away too much too early. But it was so much clearer when I was reading the book than it was in real life."
    f "I’m the first one...the first one who caves...and I just...I let you {i}conquer{/i} me because I feel like you’ll leave me if I don’t."
    f "I become so...reliant on your existence that...that..."
    f "That it’s like I’m barely even human by the end of the first volume..."
    f "If the other girls find out...if they see just how much of me I let you have..."

    scene futabatired19
    with dissolve

    f "They’re going to hurt me..."
    s "I won’t let anyone hurt you, Futaba. And I’ll talk to Nodoka about her book. I had no idea it would affect anyone this much. Or that...any of you would even read it."
    f "Thank you...really."
    f "But Sensei...this isn’t something you should wait on. If {i}anyone{/i} else from the class gets their hands on this, {i}everything{/i} is going to unravel. "
    s "Unless a good portion of it is made up, you mean."
    f "But if the others are anything like me...and they can {i}confirm{/i} that what’s in there actually happened...everyone will know it’s real."
    f "All it takes is one person’s confirmation to cast doubt on any part of the story that you or Nodoka or anyone else says is just “made up.”"
    s "I get it. Like I said, I’ll talk to her."

    scene futabatired20
    with dissolve2

    f "That’s great, but...why didn’t you talk to {i}me?{/i}"
    f "Why didn’t {i}any{/i} of you talk to me?..."
    f "You all knew...you all knew that I’d bare everything in this book...that some of the biggest, most important moments of my life would be put on display...{i}highlighted...{/i}for everyone to see..."
    f "Do you really think that’s what a girl like {i}me{/i} wants?...To have {i}more{/i} people look at her when she can’t even look at herself?"
    f "Did any of you even think about that?..."
    s "Honestly?...No. I don’t think any of us did. Because if there was even a glimpse of that, we would have confronted Nodoka then and there."
    s "But this was something that was out before any of us could even do anything about it. Rin, Otoha, and I didn’t find out what was going on until people started mistaking us for cosplayers."
    f "Well...for all of our sakes...I hope you get through to her. Because I thought I would...and I didn’t even come close."
    s "I’ll do my best. It’s Nodoka, though...so I can’t really make any promises."
    s "I do have one question, though."
    f "What is it?...What are you wondering?..."
    s "It’s just...our story is still going. "
    s "So I was kind of wondering how the book ended. "
    s "Like...where did she decide to cut things off?"
    f "That’s the only part I didn’t really understand. "
    f "The book just...{i}ends.{/i}"
    s "But...{i}where{/i} does it end? "
    s "What’s the last thing that happens?"

    stop music
    play sound "static.mp3"
    scene futabatired21 with flash
    stop sound
    play music "sweetvermouth.mp3"

    f "You wake up in a room with clocks."

    $ renpy.end_replay()

    stop music
    scene black

    "FUTABA GOES HOME TO SLEEP AND FEELS A LOT BETTER ONCE SHE WAKES UP"
    "YOU ATTEMPT TO DO THE SAME ONCE SCHOOL ENDS BUT YOUR MISSION BECOMES TANGIBLE AND GETS CAUGHT ON THE CORNER OF YOUR KITCHEN COUNTER"
    "YOU FORGET WHAT IT WAS YOU WERE SUPPOSED TO DO AND WHO YOU WERE SUPPOSED TO TALK TO"
    "FUTABA’S REQUEST IS MARKED FOR DELETION AND THE DAY COMES TO AN END"
    "PRAISE BE"

    $ futaba_love += 1
    $ futabaspecial60p3 = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump advancetotues

label futabalust25:
    play sound "knock.mp3"

    "I knock on Futaba’s door and wait for her to answer. "
    "It’s kind of weird saying that again after so much time away. "
    "In fact, between the constant barrage of divine sexual nightmares and unrequested wake-up calls, I’ve barely been able to keep track of what day it is lately."
    "Each one blurs into the next — but I’m {i}fine{/i} with that because it mirrors this world as a whole and {i}that{/i} is what I’m used to now."

    f "Come in!"

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "The status quo for me at this point is an inescapable loop. "
    "It doesn’t matter if it’s a week, a month, or a semester because I’ll wind up at the start again no matter what I do. The only difference is {i}when.{/i}"

    scene futabadad1
    with dissolve2

    "I’m sure that Futaba and some of the others would prefer I try to shake that cycle up and return to class sooner rather than later, but I’m kind of afraid of doing {i}anything{/i} different at this point."
    "At least anything that would change my daily life, I mean. Especially now that said life includes caring for a girl I’ve come to call my daughter."
    "But apart from that, I have so much more time to play in this sandbox of a city now. "
    "And that’s so much less time to corrupt other girls the way I’ve done to this one."

    f "Hah...guess I’ll try again tomorrow."
    s "Something wrong, Futaba?"

    scene futabadad2
    with dissolve

    f "Oh, Sensei. I thought you were Rin."
    s "Why would Rin knock on her own door?"
    f "We had an incident recently. Let’s not talk about it. What are you doing here?"
    s "I came here to see you. But if you’re in the middle of something, I can come back another time."

    scene futabadad3
    with dissolve

    f "No, it’s fine. You’re barely here at all anymore. It’d be silly of me to let this chance slip through my fingers."

    scene futabadad4
    with dissolve

    f "I’m not really busy anyway. I was just trying to call my parents, but I haven’t been able to get through at all lately. I have no idea why."
    s "When was the last time you talked to them?"

    scene futabadad2
    with dissolve

    f "I think it was around the time you left school. I’m not really sure."
    f "They’re probably fine. It’s just a little unusual for them to not call and check up on me, so I’ve been kind of worried."
    s "Well, on the bright side, at least they’re alive. That’s more than most girls in the class can say."

    scene futabadad3
    with dissolve

    f "Yes, my problem is rather tame by comparison. But that doesn’t mean I’m not going to worry."

    scene futabadad5
    with dissolve

    f "Plus, they still send me an allowance and I need to make sure they’re okay so I can keep buying romance novels."
    s "Look at you doing something selfishly motivated for once. And sticking with a hobby on top of that. I couldn’t be more proud of you, Futaba."

    scene futabadad6
    with dissolve

    f "That was mostly a joke. But I {i}will{/i} admit that things have gotten rather out of control concerning my “hobby” ever since you left."
    s "Meaning what exactly?"

    scene futabadad7
    with dissolve

    f "..."
    s "...?"

    scene futabadad8
    with dissolve

    f "Teehee."

    scene black
    with dissolve

    s "Am I supposed to understand what you mean based on just that laugh alone?"
    f "I’m sure you can if you use your imagination, Sensei."

    "Futaba tosses her phone to the side and stands up to face me, giving me a tight hug and allowing me to confirm two things that I was already pretty confident in."

    scene futabadad9
    with dissolve2

    "The first is that I missed her."
    "The second is that I missed her boobs."

    s "Thank you for not wearing a bra today."
    f "And just like that, it’s like you were never even gone."
    s "Except I was. And I am now just a shell of the man you once knew. But there are {i}some{/i} things that will never change, Futaba."
    f "Well, I’m glad to hear that. And I’m glad you’re finally feeling good enough to start visiting us again. "
    f "How’s Ami doing? Last I heard, she was having a pretty tough go of it as well, wasn’t she?"
    s "A little better. She’ll probably start coming back to school soon. Just don’t act too shocked when you see her."

    scene futabadad10
    with dissolve

    f "Why would I act shocked?"
    s "Because like 95%% of her hair is gone now and she looks kind of like a boy. "

    scene futabadad11
    with dissolve

    f "What?!"
    s "But, like...a cute boy. One that’s somewhat androgynous. The kind that makes you question the type of man you think you are. You know how it goes, right?"

    scene futabadad12
    with dissolve

    f "Maybe you really {i}have{/i} changed since you’ve been gone. "
    s "I think I just have a thing for Ami."

    scene futabadad13
    with dissolve

    f "Maybe you really {i}have{/i} changed since you’ve been gone. "
    s "Okay, don’t just go repeating lines. In fact, ignore everything I said about how she looks now and just...look forward to her return. And try not to get a crush on her. Or tell her I said that."
    f "Weirdly enough, I think she’d be very happy to hear it."
    s "Weirdly enough, I think you’re right. But the relationship between her and I has changed pretty dramatically lately and I’d like things to keep going strong if that’s at all possible."
    f "Maybe you really {i}have{/i} changed since-"
    s "Not like {i}that.{/i}"

    if amifingered == True:
        "That changed way earlier."

    s "What I mean is that...she’s calling me Dad now."
    f "Maybe you-"
    s "In a non-sexual way."

    if amifingered == True:
        "Most of the time."

    scene futabadad14
    with dissolve

    f "Really?"
    s "Yeah."
    f "And...how do {i}you{/i} feel about that?"
    s "Kind of...{i}good.{/i}"

    scene futabadad15
    with dissolve

    s "We had a relatively long talk about it recently and...she told me she’s sort of always looked at me that way anyway. "
    f "I’m surprised you needed her to tell you that. That’s how it’s always seemed to most of us. "
    s "It’s easy to miss things when you’re intentionally looking away from them. And I never thought I was fit to be a guardian or anything like that, so..."
    f "You don’t need to explain it to me, Sensei. I’m happy for you. Ami too. And I’ll try not to get a crush on her whenever she comes back to school."

    scene futabadad16
    with dissolve

    f "Which will be really easy since I already have a crush on someone."
    s "Flirting with me is a dangerous move when you’re standing there looking like {i}that.{/i}"

    scene futabadad17
    with dissolve

    f "Like {i}what,{/i} Sensei? Whatever do you mean?"
    s "Don’t play dumb, Futaba. You know what weapons you possess. "
    f "Weapons?..."

    scene futabadad18
    with dissolve

    f "I don’t have any weapons..."
    s "You sure do. And you’re pointing them right at me too..."

    scene futabadad19
    with dissolve

    f "You know, Sensei...I might have just had a little bit of an idea."
    s "I’m listening..."

    scene futabadad20
    with dissolve

    f "Well...as you saw just a few minutes ago, I’ve been a little beat up lately about not being able to get in touch with my parents."
    f "And {i}you...{/i}well, you just so happen to {i}be{/i} a parent now."
    s "..."

    scene futabadad21
    with dissolve

    f "So, like...do you want to maybe..."

    scene futabadad22
    with dissolve

    f "Be {i}my{/i} daddy for a little while?..."
    s "..."
    f "Please?"
    s "What have you become over these last few months?"

    scene futabadad23
    with dissolve

    f "Neglected...lonely...{i}needy...{/i}"
    f "And without my daddy around, I’ve had no idea what I’m supposed to do...how can I take care of all these feelings?..."
    s "Is this what you meant by your “hobby” getting out of control?"

    scene futabadad24
    with dissolve

    f "Can’t you just play along?! This is really embarrassing for me!"
    s "I can play along. I’m just surprised this is the route you’re taking when both of our current issues stem from {i}actual{/i} parenthood and not your elf books."

    scene futabadad25
    with dissolve

    f "I just...think it’d be a...fun distraction..."
    f "And I’ve kind of...always wanted to try roleplaying with you, so..."

    if futabamaster.lower() in ["daddy", "dad", "father", "papa"]:
        s "I mean...technically speaking, you've kind of {i}already{/i} been calling me [futabamaster] every time we hook up for a while now."
        f "Yeah, but...that's different. And there was never actually any {i}roleplay{/i} involved, so..."

    f "D...Daddy?..."
    s "Am I supposed to call you Ami now?"

    scene futabadad26
    with dissolve

    f "I hate you."
    s "Take your top off."

    scene futabadad27
    with dissolve

    f "Huh?"
    s "Be a good girl and do what you’re told."

    scene futabadad28
    with dissolve
    stop music fadeout 15.0

    f "Oh! R...Right!"

    scene futabadad29
    with dissolve

    f "If that’s what Daddy wants...I’ll do it..."
    f "I’ll do anything Daddy says...{i}anything...{/i}"
    s "All the way."

    scene futabadad30
    with dissolve2

    f "Like this?..."

    "Futaba’s tank-top drops to the floor and I am suddenly thankful for my prolonged absence as she has apparently saved up every drop of lust for this exact moment."
    "Probably."
    "I’m sure there was a bit of masturbation in there if she’s reading as much smut as she made it sound like, but {i}I{/i} am the one who gets to gorge himself on the fruits of her growing depravity."
    "And I will eat my fill tonight."

    play music "asobeatsex2.mp3"

    s "Just like that...You’re getting bigger, aren’t you? It feels like just the other day you were still my little girl."
    f "I’ll always be your little girl, Daddy...that won’t change no matter {i}what{/i} happens to my body..."
    s "Good...because Daddy won’t let anyone else have you. "
    s "Or touch you..."
    s "Or even {i}look{/i} at you."
    s "You will never leave this room...and you will never tell anyone what happens in here...do you understand?"

    scene futabadad31
    with dissolve

    f "Yes, Daddy..."
    s "Daddy’s going to touch you again today...okay?"
    f "Yes...I love it when Daddy touches me..."
    s "And where do you want him to touch you?"
    f "Everywhere..."
    f "I want Daddy inside me..."
    f "I want to make Daddy feel good..."
    s "How are you going to make Daddy feel good?"

    scene futabadad32
    with dissolve

    f "I’ll use my pussy..."
    f "I’ll rock back and forth...just how he likes it...and do all the work...so he can relax after a long day at the factory..."
    s "Uh...yeah. I work at the factory."
    f "Making tires for American vehicles..."
    s "This is taking a weird turn."
    f "Get on the bed, Daddy..."
    f "I’ll take really good care of you..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene futabadad33
    with dissolve2

    f "Hah! Hah! Daddy! Yes! I love it! I love when you’re...inside me!"
    f "Does it feel good, Daddy?!...Do you like...hah...messing up your daughter?! Do you like her pussy, Daddy?!"

    "Futaba (known bottom) rocks back and forth with reckless abandon, causing me to question everything I’ve come to know about her."
    "But yet again, maybe this part of her has always existed and just hasn’t come to light because I’ve been too busy leading the charge in everything."
    "I’m not sure if I should be thanking romance novels or studying their power but, whatever has caused {i}this{/i} side of her to come out, whether it be my fault or theirs, I am grateful."
    "I grip her flesh, hot and moist from freshly formed sweat, and thrust into her as she continues to ride me."
    "The lewd sounds echoing throughout the room serve to only reaffirm my thought that I’ve never experienced her {i}this{/i} wet before. At least prior to squirting — another one of her lovable quirks."

    f "Daddy, Daddy, Daddy! I love you! I love it when you...let me take care of you! I want you...aaaah...to feel good, Daddy! Feel good for me! Feel good, feel good, feel good!"

    "She continues slamming herself down, nearly breaking my pelvis in the process, but I’m not about to try and slow her down since I think it’d be worth it at this point."

    s "You sure do love your daddy’s cock, don’t you?"

    scene futabadad34
    with dissolve

    f "Hah! Yes! I love it! I’m so jealous of Mommy! I want to have Daddy’s babies too! I want to be Daddy’s bride!"
    s "You’ll never be Daddy’s bride...but he’ll still take care of you, okay?"
    f "It’s....aaah! Not....enough! Daddy should.....only touch me! I don’t....want to share!"
    s "You have to learn how to share, baby...that’s part of growing up."
    f "Will Daddy do me more if I grow up?...Doesn’t Daddy like me little?..."
    s "Daddy will love you no matter what..."

    scene futabadad35
    with dissolve

    f "Hah...hah...Daddy is a liar! He likes me like this...he doesn’t want me to grow up! "
    f "I’ve seen...aaah....the way he looks at other little girls...and it makes me so jealous...I know he wants to do it with them too...but that’s {i}my{/i} job...{i}I’m{/i} the one who makes Daddy...feel good!"
    s "Sounds like you don’t want to grow up either, huh?..."
    f "Hah...hah...no! I...don’t! I wanna be little...I want Daddy’s cock...to barely fit inside!"

    scene black
    with dissolve2

    "Futaba milks me for all that I have...collecting every last drop as she continues to bounce up and down."
    "But we don’t stop there."
    "She slides herself off of me, crawls to the foot of the bed, and proceeds to clean me up with her mouth until I’m hard again."
    "Each time, I expect her passion to fade along with her energy, but neither of them do. So either she is {i}very{/i} in character right now...or she’s {i}really{/i} been holding all of this in and is trying to get her money’s worth."

    scene futabadad36
    with dissolve2

    f "Haaah! Haaah! Haaah! Right there! Daddy! Something’s coming...again!"
    s "Again? How many times is that now, baby?"
    f "I don’t know! I don’t even know...what’s happening to me! I just know...it feels so good! It feels so good, Daddy!"
    s "Yeah?..."
    f "Yes! Yes, Daddy! It’s coming...it’s coming...it’s..."

    scene futabadad37
    with hpunch

    f "AAAAAAaaaaAAAaAAaaAAAaaaaAAAAAAAAAAAHHHH!!!!!!!!!!!!!!!!!!"

    "Futaba convulses for the nth time, leaving the juices fleeing from her body nowhere to go but all over me and the sheets."
    "We’re basically fucking on a water-bed now, but I don’t care. I’m not the one who will need to clean up once we're finished."
    "I just hope that the smell of sex permeating the room won’t be pungent enough to keep Rin up at night."
    "And, if it does, I hope it {i}affects{/i} her the same way all those books have affected the girl currently absorbing every drop of cum my body can produce."

    scene futabadad38
    with dissolve

    f "Hah......hah.......more!"
    s "Still? You haven’t had enough yet?"
    f "It’ll never be enough...I won’t stop until Daddy can’t get hard anymore..."
    s "That might a problem then...Because the little girl taking care of Daddy right now is so cute that he’ll probably stay this way forever."
    f "Then I guess...Mommy will have to pull me off of you..."
    s "Mommy can watch..."
    f "Yeah?..."
    s "Yeah...she can play with herself watching me fuck the monster we’ve created..."

    play sound "static.mp3"
    scene futabadad39 with flash
    stop sound

    a "Hah...hahh...you think I’m a monster?..."
    s "It’s a term of endearment..."
    a "Call me what I really am, Daddy...call me your daughter..."
    a "Fuck me...cum in me...and call me your daughter..."
    a "That’s all I’ve ever wanted...just a Daddy...who makes me feel like I’m the only girl in the world..."
    s "You’re the only girl I’ll ever need..."
    a "You don’t mean that..."
    s "I do..."
    a "Then show me...how it feels..."
    a "Do it inside...{i}again...{/i}until I can’t take any more..."

    play sound "static.mp3"
    scene futabadad40 with flash
    stop sound

    f "AAAAAAAAH OH MY GOD! YES! JUST LIKE THAT, DADDY! JUST LIKE THAT!"

    "My thumb finds its way to Futaba’s swollen bud and overtakes a dark corner of my mind in the form of a repetitive circular pattern."
    "She enjoys it, just like they all do, but I’m sure you don’t need {i}me{/i} to tell you that."

    scene futabadad41
    with dissolve

    f "Play with me...make me feel good again...make it come out again...Daddy...Daddy!"
    s "Daddy’s gonna cum any second now...can he do it inside again?"
    f "Yes! He can do anything he wants! He can cum in me as many times as he wants! I exist...to make Daddy happy!"
    s "Are you happy too, baby?"
    f "I’m...so happy, Daddy! I’m so happy...we can do this! I’m so happy...you’ll accept my love! And give me...lots and lots of yours! Lots and lots of-"

    scene futabadad42
    with dissolve

    f "AAAAAaaaaAAAAAH! It’s coming out again! I’m coming! I’m coming, Daddy!"

    "Her motions get clumsier. She’s probably running out of steam. And that’s good, because I am too."

    s "Last one, okay?..."
    f "Haah! Hah! No! We’ll do it more! I don’t want you...going back to Mommy! I’ll keep you to myself...forever!"
    s "You’re going to kill Daddy at this rate. Then the tire factory will go out of business and disrupt the economy until the whole thing falls into a state of disrepair."
    f "Aah! There are...other tire companies!"
    s "Futaba, I’m at my limit."
    f "Hah...hah...then...make this last one a good one! Because I’m...haaah! Mine will...mine will be...aaah!"

    "With one final push, I give my “daughter” everything she wants."

    with sexfade
    with sexfade
    scene futabadad43 with cumflash
    with hpunch

    f "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHH!!!!!!!!!!!!!!!!!!"

    scene black
    with dissolve2

    "And then I disown her."
    "........."
    "......"
    "..."

    scene futabadad44
    with dissolve2

    f "Haaaaaah......."
    s "Satisfied?"
    f "I needed that..."
    s "Yeah, I could tell. You were really into it. I like that side of you."

    scene futabadad45
    with dissolve

    f "Thanks for playing along. I know acting isn’t normally your thing."
    s "I can make exceptions so long as I get to have sex with a cute girl. Seems like a fair trade to me."
    f "I’ll keep that in mind for next time."
    s "Sounds good. But I’m out the second you ask me to roleplay King Elvencock of the Enchanted Forest."

    scene futabadad46
    with dissolve

    f "Noted. Now, please excuse me while I go take a shower and get all of your semen off of me."
    s "At least 90%% of those fluids are yours. All of mine went inside."

    scene futabadad47
    with dissolve

    f "Are you going to hang out here for a little while? Or are you going to be gone once I come back?"
    s "Excuse me. Are you implying that I came here for the sole purpose of having sex with you?"
    f "No. But you normally leave once it happens and I’m not sure if {i}that{/i} part of you is one of the ones that changed during your {i}vacation.{/i}"
    s "I’ll still be here when you get back, Futaba."
    s "Then, we can go for a walk and you can tell me all about how you’ve always wanted to fuck your dad."

    scene black
    with dissolve
    play sound "dooropen.mp3"
    stop music fadeout 15.0

    f "Or you can just go home. That’s fine too."

    "Futaba covers herself up and leaves the room, and I instinctively take a seat on the bed."
    "I regret that decision immediately."
    "It's so wet."

    $ renpy.end_replay()
    $ futabalust25 = True
    $ futaba_love += 1
    $ futaba_lust += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
    "........."
    "......"
    "..."

    jump futabaspring1

label futabaspring1:
    scene clearnightsky
    with dissolve2
    play music "gentle.mp3"

    "To what do I owe this pleasure? That of traipsing down a faintly lit path just blocks away from the dorm as if this is where I’m meant to be..."
    "That of spending my night beside a lovable girl — yet a girl that I {i}can not{/i} love because I haven’t figured out how to yet."
    "Maybe it would be easier if she wasn’t so nice to me."
    "Maybe if she went on long-winded rants about how I’m the most disgusting man on the face of the earth..."
    "Or if she took me on tours of my childhood or...cut her hair in a fit of panicked rage because of my absence-"
    "Maybe then the love would come easier."
    "I don’t know {i}why{/i} I’ve taken it upon myself to disperse my heaviest thoughts and feelings on those shouldering the most weight, but perhaps it has something to do with my affinity for destruction."

    scene futabanighttraipse1
    with dissolve2

    "Just thirty minutes ago, this same girl was calling me “Daddy.” "
    "She was riding my lap as if she was {i}bred{/i} to do that. And while that’s not something I’d encourage other prospective fathers out there to do, I’ll admit that it was quite invigorating."
    "But now comes the silence — that reflective retrospective and all that rides in on its shoulders, but not out of the affinity to destroy."
    "It rides in that way because the weight serves to keep us grounded. It makes it feel as if we’re not floating away when all of the bubbles that exist within us as the result of a thing called “bliss” begin to lift us up."
    "Typically speaking, I’m the one who habitually pops them as I’ve always had a fear of heights."
    "But on some nights when I’m spent, and I can guarantee you that tonight is one of those nights, I just can’t seem to find my needle."
    "I could burst them with my finger, I’m sure. But the idea of getting any of that joy all over my hands does nothing but make me want to wash them."
    "I wonder what we’ll talk about tonight."
    "I wonder if it will make me like her more, or make me like her less."
    "I wonder if it even matters."

    f "Sensei..."

    "Here it comes — that unwanted weight."

    s "Yeah?"
    f "Tell me more about Ami."

    scene futabanighttraipse2
    with dissolve

    s "Huh?"
    f "Are you surprised that’s what I want to talk about?"
    s "Kind of, considering she’s public enemy number one for most people by now."
    f "Love makes us do all sorts of crazy things. That in mind, I don’t really find anything Ami said all that “crazy.”"
    s "She threatened to dismember you."
    f "Yes, but do you really think she’d follow through with it?"
    s "Kind of, yeah."

    scene futabanighttraipse3
    with dissolve

    f "Oh. Well, maybe my self-defense instinct isn’t all that functional then."
    f "But still, she’s the biggest change in your life lately. And I’m interested in hearing more about how things are shaping up now that I’m not distracted by...other things."
    s "You mean how you missed me so much that your body opened itself up to me the moment I showed up in your room?"

    scene futabanighttraipse4
    with dissolve

    f "Exactly. Though, I’d word it in a much less vulgar way since I’m still a good girl whether that’s how you prefer me or not."
    s "I don’t have a preference. Futaba being Futaba is all that matters to me. And you were still Futaba even {i}if{/i} you were screaming and moaning about wanting Daddy’s cock to-"

    scene futabanighttraipse5
    with dissolve

    f "Oh, look! A bench! Why don’t we go sit over there?"
    s "Sure. But I have a shift at the tire factory early tomorrow morning, so we’re going to have to make it quick."

    scene futabanighttraipse6
    with dissolve

    f "Why did I even say that? I have no idea where it came from."
    s "Beats me. But hey, you saved me from having to come up with a backstory and I still got to fuck my daughter. So all’s good on my end."

    scene black
    with dissolve2

    f "Well, hopefully being able to relate to the topic at hand won’t cause you to get as...{i}excited{/i} as I did earlier. "
    s "So you really {i}do{/i} want to fuck your dad, huh?"

    scene futabanighttraipse7
    with dissolve2

    f "Of course not! But in the context of a fictional setting where I am {i}not{/i} Futaba Fukuyama...maybe."
    s "I’m just teasing you, don’t worry. It doesn’t matter to me who you want to sleep with."

    scene futabanighttraipse8
    with dissolve

    f "Well, it should probably matter a {i}little.{/i} Because even if you’re seeing other girls, I’d like you to be {i}kind of{/i} possessive when it comes to me."
    s "What right do I have to be possessive of anyone when I get more action from more girls than basically every other male left in Kumon-mi combined?"
    f "None of this is making me feel good about myself, Sensei. I just think it’d be nice to know that the boy I’m interested in isn’t {i}okay{/i} with me sleeping around."
    s "I know. I’m sorry. And I’m {i}not{/i} okay with that, for the record. I probably wouldn’t have even said that if I had any sort of real competition in this city."

    scene futabanighttraipse9
    with dissolve

    f "That’s a little better...but still."
    f "I promise I’m just as wholesome now as the day you met me."
    s "I came inside of you like ten times tonight."

    scene futabanighttraipse10
    with dissolve

    f "That just means our baby will be very strong and healthy and there’s nothing to worry about at all."
    s "Do you mind if I call the tire factory really quick? I need someone to cover for me tomorrow on account of the fact that I’m going to kill myself tonight."

    scene futabanighttraipse11
    with dissolve

    f "What's wrong, Sensei? Is {i}two{/i} children too many for you?"
    s "..."

    scene futabanighttraipse12
    with dissolve

    f "What spurred this whole thing with Ami anyway? What was it that made you want to take that final step?"

    scene futabanighttraipse13
    with dissolve

    s "..."
    f "..."
    s "I wonder how many people I’m going to have to talk to about this."
    f "Probably most of them. You’ve got a lot of people who really care about you, but you’ve always been a very...specific type of person to all of them. A change this big isn’t something you can just keep hidden."
    s "It’s not like I want to keep it hidden. I wouldn’t have told you in the first place if that was the case. I just don’t really know what it means when it comes to my relationship with everyone else."
    s "Like, Ami calling me “Dad” isn’t going to impact what goes on between you and I unless she walks in on us the next time you need to be {i}distracted.{/i}"
    f "Let’s avoid that at all costs, shall we?"
    s "Agreed."
    s "I don’t know, Futaba. There isn’t really {i}one{/i} reason I decided that now was the best time for me to step up. It was closer to a million reasons and...recent developments in my personal life."
    f "Is this about that “person you lost?” The one you told us about in class?"
    s "..."

    scene futabanighttraipse14
    with dissolve

    f "Losing people is part of life, I think."
    f "I don’t have any experience with that, of course. My parents are still {i}there,{/i} I just can’t contact them at the moment."
    f "And you’re the first person I’ve ever fallen for, so it’s not like I’ve lost anyone in that regard either."
    f "But take Nodoka for example. She’s slowly falling out of my life and doesn’t even seem to care at all. And she’s basically always been there, so...that’s a thing I have to just {i}deal with{/i} now."
    f "And while I don’t really know your circumstances, I can say that having to just {i}look at{/i} that person I’ve lost feels terrible."
    f "It makes me angry...regretful...and I feel like an idiot a lot of the time for not seeing it coming."
    s "..."
    f "But even if I loved her...or {i}love{/i} her, despite all that she’s done...I have other people I care about. Just as I’m sure you do."
    f "So maybe it’s best to just let go. Maybe that old phrase really {i}is{/i} accurate after all."
    s "I think Nodoka’s just stubborn, Futaba."

    scene futabanighttraipse15
    with dissolve

    f "I think so too. "
    f "And deep down, I think she really {i}is{/i} remorseful about this. But she’ll never come out and say that because that’s not the type of person she is."
    f "You and her are a lot alike. You dodge subjects that you don’t want to confront or make things up because you think it’s easier than holding yourself accountable. But that doesn’t mean you don’t {i}feel{/i} accountable."
    s "Then...if you know she feels bad, why are you holding it against her? Why not make it easier on her and just bury the hatchet yourself since you’re actually able to?"
    f "Because doing that doesn’t help people grow. "
    f "Nodoka lives in her own world. But that world just happens to be {i}inside{/i} of ours. Or...{i}outside.{/i} It’s kind of hard to tell with her sometimes. "

    scene futabanighttraipse16
    with dissolve

    f "And who knows? Maybe I’m wrong and she isn’t actually sorry at all? Maybe I just have a habit of looking for the good in people and...making things up if I can’t find any? "
    s "That’s sort of like what Nodoka and I do then, isn’t it? "
    f "Yes. But I’m not making things up because I want to avoid confrontation. I’m making things up because I’m naive and optimistic."
    s "You’d really call yourself an optimist?"

    scene futabanighttraipse17
    with dissolve2

    f "..."
    s "Would you?"
    f "About {i}some{/i} things, yes."
    s "This isn’t about {i}some{/i} things, though. We’re talking about people who dodge confrontation because of certain things they can’t accept. People who hide things because they’re stubborn and habitual."
    s "And out of everyone I know...{i}you{/i} are the most consistently negative person, Futaba."
    f "..."
    s "I’m saying this because I care about you."
    f "You’re saying it because the alternative is that we talk more about you...but you’re right. Maybe I’m doing the same thing."
    s "..."
    f "I’ve been having a really hard time lately."
    s "Because of Nodoka?"
    f "No. Not because of Nodoka."
    f "She certainly isn’t helping, though."
    s "Then what? What’s going on?"

    scene futabanighttraipse18
    with dissolve2

    f "I’m worried."
    s "About your parents?"
    f "About never feeling at home. "
    s "In...what way?"
    f "This body."
    f "This curse."
    f "Like...what if I’m just never content with the way I look?"
    f "Because I’ve done everything I can think of and nothing’s improved, Sensei. I’m still horrified whenever I have to look at myself."
    f "I exercise. I eat well. I take supplements. I’ve even started taking therapy sessions online and done tons of research on how high the recovery rates are for people with body dysmorphia. "
    f "It’s like 80%% or something crazy like that. Did you know that? Am I {i}really{/i} going to be part of the 20%%? Is this just how I’m going to have to live the rest of my life?"
    f "How am I supposed to do that? I’ve barely {i}begun{/i} living."
    s "Well...how do you expect the rest of us to live with the parts of ourselves that we hate?"
    f "This isn’t just “hating” something, Sensei. I wish it was as simple as that. "
    f "It makes me nauseous...seeing myself. It doesn’t matter if it’s a mirror...a picture...hell, even my shadow repulses me. And losing weight was never going to change that. I get that now."
    f "And honestly? I kind of wish I had something terminal sometimes. Because at least {i}then{/i} I’d know where things are headed."
    s "Futaba-"
    f "It’s the truth, Sensei."
    f "Not knowing is what makes all of this so...fucking unbearable. It’s not fair."
    f "I just want it to end."
    f "I just want it to be over."
    f "And so sometimes I imagine what that would be like. Or how I would do it. "
    f "Or what would become of people like Rin or Nodoka or my family or {i}you.{/i} And that calms me down a little."
    f "I love all of you guys. It’s myself that I can’t stomach. "
    f "So please continue to be kind to me, as I am only reluctantly here. "

    play sound "static.mp3"
    scene futabanighttraipse19 with flash
    stop sound

    s "It’s really that bad?..."
    f "I don’t think anything I can say will ever do justice to how bad it actually is. And I’m well aware that I probably sound really immature for even complaining about this right now."
    s "Not at all..."
    f "So yeah, that’s where my mind has been lately. Not very fun."

    scene futabanighttraipse20
    with dissolve

    s "Yeah, it doesn’t sound like it would be..."
    f "There will always be distractions, I guess. And if that’s just how I have to live the rest of my life so I can avoid confronting reality, whatever."
    f "You were right to call me out. I have no place to say that you or Nodoka shouldn’t hide in places that make you comfortable when I’d absolutely do the same if I could only {i}find{/i} one."
    f "The closest I’ve got is you — who won’t ever see the same Futaba that I see. And that makes me happy, really. "
    f "I just wish I knew what it was like. I wish I could understand the way other people see me."
    s "I can relate to you there."
    s "And I wish I could do more, but it doesn’t seem like I can..."

    play sound "static.mp3"
    scene futabanighttraipse21 with flash
    stop sound

    f "I don’t think you can, either."
    s "..."
    f "Ahh...this sucks. We’re together again after so long. I wish I could be happier."
    s "We could always have sex again."
    f "Can we? Don’t you have an early shift at the tire factory tomorrow?"

    scene futabanighttraipse22
    with dissolve

    s "I can call out."
    f "Not because you’re going to kill yourself, I hope."
    s "Are {i}you?{/i}"
    f "Nah. Rin would get mad. "
    s "So would I."
    f "But would you disappear for another three months like you did for the last person? Or am I not {i}that{/i} important to you?"

    scene futabanighttraipse23
    with dissolve

    s "Is that...a serious question?"
    f "Of course not, Sensei."

    scene black
    with dissolve2
    stop music fadeout 15.0

    f "I already know the answer."

    "I take her home and lay her down on the bed."
    "She does not call me “Daddy” this time — she just locks her eyes on mine and doesn’t look away until I feed her once more."
    "They lack the life they once had, but I don’t think it’s my fault this time."
    "I think that sometimes, there are just people who are meant to get lost. "
    "But that’s okay, because..."
    "Huh."
    "{i}Why{/i} is it okay, exactly?"
    "Either way, I leave once Futaba falls asleep. "
    "And while I managed not to get into any of the specifics about why things are the way they are for me now, I found something horrible in the process."
    "But it’s one of those things you can’t change. "
    "And I don’t know if that makes me feel better or worse."

    $ renpy.end_replay()
    $ futabaspring1 = True
    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label beachfive9:
    scene sky
    with dissolve2
    play music "notabluearchivesong.mp3"

    mo "Pay attention, Yasu! For this tutorial is not repeatable!"
    ya "I will do my best to not disappoint you, Master!"

    scene futabatimeyo1
    with dissolve2

    f "Um...Molly? Why is Yasu suddenly calling you “Master?”"
    mo "Because, dearest Xessaxia, I have {i}become{/i} her master! And have decided that it is in the best interest of the manga club if she takes after me in every way imaginable!"
    mo "With the one minor exception that she may continue to believe in her god as it was the one area she was not willing to budge on."
    ya "It was an easy decision when every other aspect of me is unworthy and unlovable."
    f "But...you don’t know how to play volleyball, Molly. You don’t even go outside."

    scene futabatimeyo2
    with dissolve

    mo "Correct, Xessaxia! Which is why my first course of action is teaching Yasu how to adapt when she {i}is{/i} forced to associate with normies!"
    mi "Molly! Just serve the damn ball! How long are ya plannin’ on makin’ us wait!"
    mo "You see, Yasu- sometimes, people will expect things of you that you simply cannot do! And, in moments like that, you must do your best to not let them down!"

    scene futabatimeyo3
    with dissolve

    mo "So the only course of action is to create your {i}own{/i} game! One not bound by the confines of what those unlike us {i}expect!{/i} "
    f "Is that...really the {i}only{/i} course of action?"
    mo "This is not volleyball, Yasu! This is...demon ball!"
    ya "I don’t think I’m allowed to play this game anymore."

    "Futaba Fukuyama was one of just several girls currently engaged (or {i}supposed{/i} to be engaged) in a casual game of beach volleyball."
    "And while athletics were certainly not her strong suit, she didn’t mind participating in things like this as the expectations placed on her were rather low."
    "It was a bit demoralizing, sure. But if there’s anything that anyone knows about volleyball in class-type settings, it’s that there will always be weak links who just try to avoid the ball at all costs."
    "And that was her!"
    "But today, fate had other plans."

    mo "...and that’s how you play demon ball! "
    ya "I understand! May I attempt to expel evil from the ball’s nucleus now?"
    mo "Not before me, Yasu!"
    mi "Someone just serve the damn ball already! I’m freakin’ out over here!"
    mo "In the name of the Tuatha Dé Danann, I serve- no. I exorcise thee! Hah!"
    mi "THAT’S NOT EVEN THE RIGHT DIRECTION!!!"
    sa "F...Futaba! Look out!"

    scene futabatimeyo4
    with dissolve

    f "Huh? "

    scene futabatimeyo5
    with dissolve

    f "UWWWWAAAAAAAH!!!!!"
    ya "May your demons be exorcised!"

    scene futabatimeyo6
    with dissolve

    f "I don’t have any demons! I don’t even like-"

    stop music
    play sound "tackle.mp3"
    scene black

    "Futaba is hit."
    "Futaba dies."

    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene futabatimeyo7 with flash
    stop sound

    "Futaba is reborn."

    f "..."
    f "..."
    f "..."
    f "Did it miss me?..."

    scene futabatimeyo8
    with dissolve2

    f "Am I-"

    scene futabatimeyo9
    with dissolve2
    play music "holyplace.mp3"

    f "..."
    f "{i}What?...{/i}"

    scene futabatimeyo10
    with dissolve2

    f "I didn’t...actually {i}die...{/i}did I?..."
    f "I know I’m not good at volleyball, but..."

    scene futabatimeyo11
    with dissolve2

    f "No...of course I’m not {i}dead.{/i} I’m...probably just unconscious or something. And this is a dream. "
    f "But if it’s a dream...I shouldn’t {i}know{/i} that it’s a dream...so-"
    q "{i}Look around you...{/i}"

    play sound "static.mp3"
    scene futabatimeyo12 with flash
    stop sound

    f "What?! Who’s there?! Who said that?!"
    q "{i}You{/i} did..."

    play sound "static.mp3"
    scene sistersoft1 with flash
    scene sistersoft2 with flash
    play sound "knock.mp3"
    scene sistersoft1 with flash
    scene sistersoft2 with flash
    play sound "broken.mp3"
    scene sistersoft3 with flash
    scene sistersoft4 with flash
    play sound "likepigstopigwater.wav"
    scene sistersoft3 with flash
    scene sistersoft4 with flash
    play sound "seek.mp3"
    scene sistersoft5 with flash
    play sound "static.mp3"
    scene sistersoft4 with flash
    scene sistersoft5 with flash
    scene futabatimeyo13 with flash
    stop sound

    "There is no you in you and me but there is me in you"
    "This normally ends differently, but different isn’t true"
    "So lie until your tongue falls off and scream your favorite song"
    "Then fill your hands with broken glass and squeeze until they’re gone"

    f "It’s upside down..."

    play sound "pabell.mp3"
    $ renpy.pause(2, hard=True)

    vpa "The current time is 11:19 PM. Today’s weather is expected to be complete within the next hour. Your name is Futaba Fukuyama. You are happy here."
    f "How...what...huh? Huh?!?!"
    vpa "There are ghosts inside this building. They will attempt to speak to you. Do not look at them. Do not answer them. Do not pass go. Do not collect $200."
    vpa "Your attendance is requested for the Transpacific Sadness Symposium. Please come to the library for further details."
    vpa "Assistance will be provided if you can not find your egg."

    play sound "static.mp3"
    scene futabatimeyo14 with flash
    stop sound

    f "What egg?! What is this?! What are you talking about?!"
    vpa "The egg that will guarantee your selection. The one that hums in your hand and not in your mouth. Assistance will be provided if you can not find your egg."

    scene futabatimeyo15
    with dissolve

    f "I would like to wake up now..."

    play sound "pabell.mp3"
    $ renpy.pause(2, hard=True)

    no "{i}Hah...haaah....aaah! Yes! I’m cumming...again! Again! A...AAAAaaAAAaahhhh!{/i}"

    scene futabatimeyo16
    with dissolve

    f "Nodoka?..."
    q "{i}Do not...heed the call...{/i}"

    play sound "static.mp3"
    scene futabatimeyo17 with flash
    stop sound

    f "Who is that?! Sh...Show yourself!"
    q "{i}No one...and nothing...{/i}"
    q "{i}Everyone...and everything...{/i}"
    q "{i}You are not safe here...they will claim you...they will complete you...{/i}"

    scene futabatimeyo18
    with dissolve

    f "Wha...what do you mean they’ll...{i}complete{/i} me?"
    q "{i}You are...the unfinished you...the last silken thread...{/i}"
    q "{i}They will take you...tear you apart...learn how your body works...and you will become the model from which all else comes to fruition...{/i}"
    f "I have no idea what that means! What is this place?! Where am I?!"
    q "{i}You know exactly where you are...{/i}"

    scene black
    with dissolve2

    q "{i}A world atop your own...{/i}"
    q "{i}Just facing a new direction...{/i}"

    "........."
    "......"
    "..."

    scene futabatimeyo19
    with dissolve2

    "Futaba Fukuyama manages to complete the maze and eventually makes it to the library...but she broke several rules along the way."
    "The ghosts that followed her and lied to her became entities that she fooled herself into trusting. But each time she spoke back to them, she lost a part of herself."

    play sound "static.mp3"
    scene futabatimeyo20 with flash
    stop sound

    "These parts grew into additional Futaba Fukuyamas. Better ones. Ones that knew how to follow directions and saw themselves not as monsters but as angels."
    "They surrounded her, skin glistening in the anti-sun, and stared through her eyes and into each others."
    "Futaba Fukuyama (the original [[?]) felt intimidated by their presence. But, in a strange way, she found it easier looking at {i}them{/i} than she did her own reflection."
    "These conflicted feelings were subsequently replaced by looming dread as a figure began to sprout in the corner of the room."
    "And while she could not see the figure yet as she fended off her shadows, it saw her. And it cried, for that was all it knew how to do."
    "It had existed in this space in time for as long as time had existed, and all it knew was pain. Scorn. It was the scapegoat the other ghosts would carve their names into. A scorned half-god."
    "And it watched in all its untapped fury as Futaba Fukuyama (the original [[?]) conversed with herself."

    f "What...How?...Why?..."
    f "What does any of this even mean?...When am I going to wake up?..."
    f "{i}Here forever, special girl! No matter what you do!{/i}"
    f "{i}You can change yourself a million times, but you’ll never feel like you!{/i}"

    scene futabatimeyo21
    with dissolve

    f "{i}Each time your fingers find your mouth, you give away a piece-{/i}"
    f "{i}Of sanity! Humanity! A chance to be complete!{/i}"

    "She knew what they were saying because she wasn’t a fucking moron like you. She’d cleaned blood off her roommate, Occam’s, razor before and wasn’t perplexed by neglected complexities."
    "She was part of the codex — an abject auspex practicing breakneck safe sex, slipping objects in the convex annexes of each attic in the narthex. "
    "She didn’t care about the effects. She paid no mind to things like that as she was too busy swimming in doubt and cum and more doubt and more cum and you were-"
    "What {i}were{/i} you doing?"
    "I watched you last night. And I didn’t quite understand. "
    "Please write your actions down on a piece of construction paper and slip it into my PO{s}x{/s} box so I can come closer to replicating you for my next art installment."

    f "{i}X marks the praetor — a letter of love.{/i}"
    f "{i}The most shameful of angels in gardens above.{/i}"
    f "{i}You know the way out, you can still be complete{/i}"
    f "{i}You’re a fat fucking bitch but I’d lick both your feet.{/b}"

    play sound "static.mp3"
    scene futabatimeyo22 with flash
    stop sound

    f "{i}AHHHHAHHAHAHAHAHAH! LOOK AT THE LOOK OF HER LOOK! HER FEELINGS ARE CRAB LEGS INSIDE OF A BOOK!{/i}"
    f "Okay...I think I might need to see a therapist. I am clearly broken. This isn’t normal."

    scene futabatimeyo23
    with dissolve

    f "I’ll just...find this {i}egg{/i} thing and..."

    scene futabatimeyo24
    with dissolve2

    f "..."

    "It was then that she noticed the sprout that had sprouted. The flower of Eden in a forest so shrouded-"

    play sound "static.mp3"
    scene futabatimeyo25 with flash
    stop sound

    "by evil and weevils, such a feeble upheaval! How depressing undressing for the cruelest of peoples!"

    f "Um..."
    q "..."
    f "H..."
    f "Hello?..."
    q "..."

    "Futaba Fukuyama (the original [[?]) broke another rule. She spoke to the unspoken. She had doomed herself to a lifetime worth of unexpected taxes and a low-calcium diet."
    "She would also be brutally violated by at least one animal before leaving this place. But the animals were nice here so she probably wouldn’t mind it."

    q "..."
    f "Maybe it’s just a...statue?"
    q "You-"

    play sound "static.mp3"
    scene futabatimeyo26 with flash
    stop sound
    with hpunch

    f "Ah!"
    q "Oh..."
    q "So you {i}are{/i} terrified of me..."

    scene futabatimeyo27
    with dissolve

    f "What? No! I just...wasn’t expecting you to talk. You were so quiet just a second ago..."
    q "So...you’re not scared?..."
    f "I’m...a little scared of everything right now. I’ve never had a dream like this before. But you...seem nice?..."

    scene futabatimeyo28
    with dissolve2

    q "Nice?..."
    f "Yeah...everyone else is...being cryptic and...{i}mean.{/i} But you’re just...minding your own business. So...thank you?"
    q "You are...thanking me?..."
    f "Yeah...but...it would also...be really nice if you could tell me what I’m supposed to do here?"
    q "Did they give you a job?..."
    f "I...I think so, but...but do you know who {i}they{/i} are? And why I need an egg?"
    q "They’re the ones who put me in here..."
    q "They said my hands were too large. That I don’t look like the others. That I can not be completed..."
    f "Just...because your hands are a little big?"
    q "It’s hard for me to walk...I’ll only slow them down..."
    q "So I’m better off in here...where I won’t be a burden to anyone..."
    f "I like your hands..."

    play sound "static.mp3"
    scene futabatimeyo29 with flash
    stop sound

    q "You do?..."
    f "Of course..."
    q "Why?..."
    f "Because they’re yours...and because there’s nothing wrong with being a little different."
    q "Is that...really how you feel?..."
    f "For everyone but me at least. Frankly, I wish I was a little more “normal” when it comes to the way I look."
    q "Are they going to lock you in here with me?..."

    scene futabatimeyo30
    with dissolve

    f "I hope not..."
    f "It’s nothing against you. I think I just like my world a little bit more."
    q "Can you tell me about it?...What makes your world so special?..."

    scene futabatimeyo31
    with dissolve

    f "The people in it, mostly. "
    f "I have a lot of people I really care about. And they’re really stubborn when it comes to trying to make me feel like I belong sometimes."
    f "It makes things...really hard, actually. But I do appreciate them for it. And I know their hearts are in the right place."
    q "These...{i}people...{/i}they are humans?"

    scene futabatimeyo32
    with dissolve

    f "Yes, they-"

    scene futabatimeyo33
    with dissolve2

    f "..."
    q "..."
    q "Is something wrong?..."
    f "You..."
    f "Look...{i}different...{/i}all of a sudden..."

    scene futabatimeyo34
    with dissolve2

    q "Different?..."
    f "Yeah..."
    q "That’s strange..."
    q "I don’t feel any different..."
    q "My hands are still too heavy to lift..."
    f "..."
    q "..."
    q "Can you...tell me more about the people you love?..."
    q "I wish...to love too...one day...but I...don’t know how..."

    scene black
    with dissolve2

    f "I have a better idea, actually..."

    scene futabatimeyo35
    with dissolve2

    f "Why don’t you come with me? We can look for my egg together."
    q "But I...can’t walk...my hands...they’re too heavy..."
    f "When was the last time you tried?"
    q "Long...long ago..."
    f "You’ve been here a while, huh?..."
    q "I’m not allowed...to leave..."
    q "I’ll scare...the others...I’ll be...the greatest burden known to man..."
    q "These halls...are not meant for those like me...for those...not meant to be here..."
    q "The incomplete...the abandoned...the scorned..."
    f "If you won’t fit in here, all you really have to do is find a place where you {i}will.{/i}"
    q "Do places...like that...exist?..."
    f "Come with me...we can find out together..."
    q "Why?..."
    q "Why are you...so nice to me?..."
    f "Because everyone’s always nice to {i}me.{/i}"

    scene futabatimeyo36
    with dissolve

    f "Well...maybe not {i}everyone.{/i} But most people. And so the least I can do is repay that kindness."
    q "I can’t do it..."
    q "Leaving here...will only hurt you..."
    q "And you...do not deserve...that pain..."

    scene futabatimeyo37
    with fade

    f "What are you talking about? You’re not going to {i}hurt{/i} me. Just take my hand and we can explore this place together."
    q "It is not me...who will hurt you...it is {i}them...{/i}"
    q "They are {i}watching...{/i}they are {i}here...{/i}"
    f "There’s no one here but us. Everything is going to be-"
    six "Hi! What’cha doing?"

    scene futabatimeyo38
    with dissolve

    f "Wha...is that-"
    six "You shouldn’t touch that thing. It’s dangerous and ugly. How did it escape its chains, I wonder?"
    f "...Maya?"

    scene futabatimeyo39
    with dissolve

    six "{i}Maya?...{/i}"
    six "Who’s that?"
    six "But even more importantly, who are {i}you?{/i} You’re not supposed to be here. This area is for members only."

    scene futabatimeyo40
    with dissolve

    f "Well, it’s not like I {i}want{/i} to be here! I got hit by a volleyball and all of a sudden I was-"
    six "了解！家に帰ろう！"

    stop music
    $ renpy.end_replay()
    $ beachfive9 = True

    jump beachfive10

label christmasfutaba1intro:
    play sound "static.mp3"
    scene futabawantsxmasdick1 with flash
    stop sound

    f "H...Heeeeey! Who’s your...friend?"
    s "This is Maisie Belle. She’s an associate of the monks who have been following me around all night. And no. I am not okay."
    f "W-Well...you know what would {i}make{/i} you okay? "
    s "Therapy?"
    f "Yeah. If by therapy you mean...um...doing the...uhh..."
    f "Having the...sex...with me?..."
    s "..."
    f "Together..."
    s "..."
    f "Sorry, could you hold on for one second please?"

    scene futabawantsxmasdick2
    with dissolve

    f "{i}This clearly isn’t the right time to put the moves on him! I don’t even know what the moves are! I’m dying out here!{/i}"
    r "{i}Just say something you read in one of your smut books! Or have Nodoka help!{/i}"
    no "{i}I’d be glad to come along and teach you everything I know, Futaba.{/i}"
    f "{i}Absolutely not! I just have no idea how to-{/i}"
    sa "{i}If you don’t, I’m going to.{/i}"
    f "{i}Wha- Sana?!{/i}"
    ay "{i}Don’t ask questions! Just go! Or all of us will!{/i}"
    f "{i}Aaaaaah! Fine!{/i}"

    scene futabawantsxmasdick1
    with dissolve

    f "H...Hi again..."
    s "Something suspicious is happening right now."

    scene futabawantsxmasdick3
    with dissolve

    f "Pfffffft! {i}No!{/i} I’m here of my own volition and wasn’t put up to it at all!"
    s "Do you want to have sex with me, Futaba?"
    f "I mean...if you {i}really{/i} want to...I guess I {i}could{/i} step away for a minute?"
    s "Sure. I hope you don’t mind the monks watching, though. They won’t leave me alone."

    scene futabawantsxmasdick4
    with dissolve

    f "What {i}monks,{/i} Sensei? Is the mystery surrounding the Tsukioka family even deeper than it seems? Is there a cult here or something?"
    s "No, just regular trauma stuff. But hey, the sooner I get forced back to reality, the better. And I enjoy putting my penis inside of your vagina."
    f "Sorry, could you hold on for one more second please?"

    scene futabawantsxmasdick2
    with dissolve

    f "{i}Someone swap with me. He’s acting kind of weird.{/i}"
    ay "{i}This sounds like a job for Ayane Amamiya! I have plenty of weird sex experience with Sensei by now. I can handle this.{/i}"

    if futaba_lust >= 40:
        f "{i}Weird how? What does that mean?{/i}"
        ay "{i}Like he just kind of jumps into hardcore sex-mode and goes to town on you while saying some weird stuff every now and then. It’s mostly just incoherent.{/i}"
        ay "{i}But yeah, I had a feeling this might happen when he started talking about monks earlier.{/i}"
        ay "{i}Don’t worry, though! Because even if we spent the whole morning going at it together, I can take another beating for- wait, no! Futaba{/i}"

        scene futabawantsxmasdick5
        with dissolve

        f "Okay! I’m ready now. Let’s go."

        scene black
        with dissolve2

        ay "{i}Aaaaah! I made it sound too appealing!{/i}"
        r "{i}How...hard are we talking exactly?{/i}"
        no "{i}It’s like being penetrated by a jackhammer.{/i}"
        sa "{i}Mnh...{/i}"

        stop music

        jump futabalust40

    else:
        r "{i}On second thought, are we sure this isn’t abuse? Because if he’s as weird as I’ve seen him in the past, I don’t know if it would be right to-{/i}"
        r "{i}Wait, where did Nodoka-{/i}"

        scene futabawantsxmasdick6
        with dissolve

        no "Hi. You. Me. Now."
        s "Deal."

        scene futabawantsxmasdick7
        with dissolve

        r "{i}Ahh! Futaba! Look what you’ve done! You missed your chance and now he’s leaving with Nodoka! And who knows what that girl is going to do to him?!{/i}"
        ay "{i}Tch. It should have been me.{/i}"

        scene black
        with dissolve
        stop music fadeout 10.0

        sa "{i}I think...I’m gonna follow them...but I’ll catch up with you guys la- ahh?!{/i}"
        ay "{i}You are not going anywhere. You are going to stay here and be a good girl with the rest of us.{/i}"
        sa "{i}Mnngh...fine...{/i}"
        f "{i}I...can’t tell if I regret anything right now...{/i}"

        $ renpy.end_replay()
        $ futabalust40miss = True
        $ mollylust10miss = True
        $ christmastsubasa1miss = True
        $ nodoka_lust += 1

        "{i}Nodoka’s lust has increased to [nodoka_lust]!{/i}"
        "{i}You buried yourself in her again.{/i}"
        "{i}It felt somewhat nostalgic. Like sinking your cock into that hole you carved in the wall.{/i}"
        "{i}The inside was filled with meat. Just like her.{/i}"
        "{i}You cum inside. She kisses your forehead. The monks dance in circles around you.{/i}"
        "{i}You miss a total of three events.{/i}"

        jump christmasfive6

label futabalust40:
    play sound "static.mp3"
    scene futabawantsxmasdick8 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    f "J...Just to make sure, you...{i}are{/i} okay with this, right?"
    s "Why wouldn’t I be?"
    f "Because of the...monk thing. And because you might not be all “there” right now. Which is fine! I won’t hold it against you if you don’t want-"
    s "Futaba, I’m fine. Today is weird. Like, I’m here...but I’m not. I know you’re you and I know I’m me. "
    f "And...that snowman?"
    s "Forget about Maisie Belle. The point is I’m going to fuck you and {i}you’re{/i} going to like it. Then, after that? I’m probably going to fuck you again. We will then repeat this process until tomorrow comes."
    f "I think people might get suspicious if...we’re gone the whole night. Especially since I...may or may not have been put up to actually taking the initiative this time."
    s "Then what’s there to worry about if everyone already knows you planned on having sex with me?"
    f "The...duration of which...that sex will happen {i}for?{/i}"
    s "Well, let me ask you something. Do {i}you{/i} want to do it? Or are you having-"

    scene futabawantsxmasdick9
    with dissolve

    f "Oh, no. I definitely want to do it. The other girls riled me up, and I need you to fix me."
    s "Oh. Well, yeah. I can do that."
    f "You promise?"
    s "I wouldn’t have come out here if I did not intend to fuck you into oblivion. "
    s "Just to make sure, though...you didn’t see Chika following us, did you?"

    scene futabawantsxmasdick10
    with dissolve

    f "Is...that a thing she does?"
    s "Lately, yeah. But if you didn’t see her, we’re probably in the clear."

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "If she just happens to be in the corner of the room, though, ignore her. "
    f "Wha- you don’t have to pull me! I’m more than willing! But I also won’t be able to just ignore someone if they’re in the corner of the room! It’s hard enough just letting you see-"
    s "Shh. The monks will eat you alive the second you make your vulnerabilities known."

    scene lockit
    play sound "lockit.mp3"
    $ renpy.pause(2, hard=True)

    play sound "static.mp3"
    scene futabawantsxmasdick11 with flash
    stop sound

    "We find our way into a bathroom just slightly smaller than my bedroom. I’d be surprised if that wasn’t the standard here."
    "A dim red glow blankets everything, dissuading either one of us from turning on the lights as we don’t want to disturb the ambiance."
    "It smells...floral. Though, I can’t discern which type of flower. "
    "It isn’t lavender, but lavender is present. I’m always pleasantly surprised by how this girl smells. I just worry that there might be some accidental crossbreeding afoot. It’s a sin that I must stop."
    "There’s an uncomfortable silence. The walls are thick enough that the distant sounds of holiday cheer have been drowned out, leaving naught but our breath reverberating off of marble walls."
    "The brick mixed in tries to dampen it, but it’s of no use. For even if I could not hear it, I’d be able to imagine it."
    "It’s so quiet inside of me now. "
    "I wonder what it’s like inside of her."

    f "Wow...this bathroom is beautiful."
    f "Is it really okay if we-"

    play sound "static.mp3"
    scene futabawantsxmasdick12
    with flash
    stop sound
    play sound "dosex.mp3"

    "Sully it? Yes."
    "Nothing has ever been more okay."
    "Break thousands of dollars worth of toiletries and decorations in the process? Yes."
    "Nothing has ever been more okay."
    "Treat her body like a piece of meat? The kind I keep inside the wall? Yes."
    "Nothing has ever been more okay."

    f "Ngh! Ngh! Aaah!"

    "See?"
    "She likes it."

    scene futabawantsxmasdick13
    with dissolve

    f "Ayane...was right..."
    f "You really...{i}do{/i} go crazy when you’re...in a weird mood..."
    s "You made me like this, Futaba."

    scene futabawantsxmasdick14
    with dissolve

    f "Did I?..."
    f "You like me that much, Sensei?..."
    f "So much that you’d...sneak away from everybody else just to...{i}fuck{/i} me for a little while?..."
    s "Of course...but let’s not think you’re innocent here. I didn’t rope you into this. You’re the one who came to {i}me,{/i} remember?"
    f "Yeah. Just for my...{i}sexual health,{/i} though."
    f "The girls said I need to fuck you or I’ll go insane...I think they’re right."
    s "They really put you up to this, huh?"
    f "Uh-huh...That means, right now, there are four other girls who know you’re in here fucking me. How does that make you feel, Sensei?"
    s "How does that make {i}you{/i} feel, Futaba? You’re the one who-"
    f "Shh. The monks will eat me alive the second you make my vulnerabilities known..."

    scene futabawantsxmasdick15
    with dissolve

    f "Hah...hah! It feels...kind of...nice, though! Liberating...even! "
    f "But if they’re going to be all...open about the things {i}they{/i} do...when I never even asked...it’s only fair if they know...about {i}me{/i} too..."

    scene futabawantsxmasdick16
    with dissolve

    f "How you’re the...only toy I’ll ever need...[futabamaster]..."

    "That’s right. "
    "I am a toy."
    "Yet I have done nothing but convince myself everyone else is."
    "Tonight, I shall fulfill my purpose."
    "I hope you’re watching, Maisie Belle."
    "I hope you touch yourself to this."

    play sound "static.mp3"
    scene futabawantsxmasdick17 with flash
    stop sound

    f "Hyaaah! Aaah! You’re...so deep inside of me, [futabamaster]!..."
    f "It feels...ngaah...{i}amazing...{/i}"
    s "You want me to go even harder, baby?"
    f "Haah...{i}hah...{/i}you never call me that...I like it..."
    f "Yes...fuck me harder, [futabamaster]...even harder than you...fucked Ayane earlier..."

    play sound "static.mp3"
    scene futabawantsxmasdick18 with flash
    stop sound

    s "Are you two competing to see who’s better at taking my dick now?"
    f "No...I just want you to...{i}really{/i} mess me up tonight...we can call it my...Christmas gift since...I know you didn’t go out of your way to {i}buy{/i} me anything..."
    s "Did you buy {i}me{/i} something, Futaba?"
    f "Nooooope. Guess I’ll have to make it up to you some other way then, huh?"
    s "Just keep looking at me like that and your debt will be paid in no time at all."
    f "You like looking at me while {i}fucking me,{/i} [futabamaster]?"
    s "Of course. You’re beautiful. Your eyes alone make me want to ravage you."

    scene futabawantsxmasdick19
    with dissolve

    f "Then {i}do{/i} it..."
    f "I know you’ve got more in you..."
    f "Harder than Ayane got it..."
    f "It’s not a competition...I’m just jealous."

    scene futabawantsxmasdick20
    with dissolve2
    play sound "dosex.mp3"

    f "Mnnh!~"
    s "Like that, baby?"
    f "Harder..."

    scene futabawantsxmasdick21
    with dissolve

    s "How about this? Is that enough for you?..."
    f "{i}Haaah...{/i}"
    f "Harder!"

    scene futabawantsxmasdick22
    with dissolve2

    f "Mmmmnfgh?!??!"

    "I press her up against the wall with all of my strength, violently thrusting into her as if I’m trying to turn her insides into pulp."
    "And again, she likes it."
    "I’m not sure what’s gotten into her tonight...but whatever it is, I want more."

    f "Yes! Just...like that! Fuck me, [futabamaster]! Keep...filling me up!"
    s "Look at {i}you...{/i}this newfound confidence of yours is paying off in spades, huh?"

    scene futabawantsxmasdick23
    with dissolve

    f "Hah...hah...{i}maybe...{/i}Or maybe I’m just getting a little better at turning my brain off when you {i}fuck{/i} me like that, [futabamaster]."
    s "I like what {i}I{/i} said more."
    f "Yeah...you would, wouldn’t you?"
    f "Maybe...try doing the opposite this time, though?"
    s "Meaning what, Futaba?"
    f "Hah...aah...meaning..."
    f "I wonder...how it would feel...if you were to stop being so nice to me right now... "

    scene futabawantsxmasdick24
    with dissolve

    f "And treat me like a stupid, innocent girl who doesn’t realize she’s being used..."

    play sound "static.mp3"
    scene futabawantsxmasdick25
    with flash
    stop sound

    f "MNNGHHGNGHGHG!!!!!!!"
    s "If that’s what you want, fine. I can take advantage of you."
    s "That’s all I was doing at first anyway, so it’ll be like a trip down memory lane."
    f "MNNNFGHH!!!! HAAAAH! LIKE THAT! YES!"
    s "You’ve always been so eager to please me...to impress me..."
    s "I bet I could have bent you over a fucking table in the library before I even knew your name and your only rebuttal would be asking me to not be rough."
    f "MMNGH! MMMF! [futabamaster]! HAAAH!"
    s "Does that turn you on, Futaba? Knowing I used to imagine what it’d be like to just grab your head and fuck your little mouth in the middle of school? Without even caring about you?"

    scene futabawantsxmasdick26
    with dissolve

    f "Haaaah....aaaaAAaahh......mnfaaaah!!!! Cumming! Cumming! Haaaah!"
    s "Yeah...let it all out, you horny bitch."

    scene futabawantsxmasdick27
    with dissolve2
    with hpunch

    f "MMMNGHGHNGNGNGHHH!!!!!!!!!!! MMM! MMMMMNGH!!!!!!!!"
    s "Look at you, squirting all over my cock before I’m even close to finishing. You know exactly what you’re good for, huh? You know the only use I have for you."

    scene futabawantsxmasdick28
    with dissolve

    f "Th...that’s right...I’m just an innocent high school girl...trying to do my best in school...trying to make my teacher happy..."
    f "Will you give me an A now, Sensei?...How about if I...let you cum inside of me?...Will {i}that{/i} make you like me?"
    s "Nope. In fact, just {i}offering{/i} that makes me think you’re even more pathetic than you were a minute ago."
    s "I’m here to fuck you, throw you aside like a piece of trash, then never look at you again."

    scene futabawantsxmasdick29
    with dissolve

    f "N...No! Please...look at me! I need your cock! I need you to...fuck me...forever! [futabamaster]!"

    "Futaba wraps her legs around my waist and tries to thrust back against me, but her movements are sporadic and clumsy, which makes it feel as if I’m genuinely taking advantage of her."
    "That excites me more than it should."

    f "Hah! Hah! Yes! Fuck my ugly, worthless body! I’ll never be good enough for you! I’ll-"

    scene futabawantsxmasdick30
    with dissolve

    f "Why are you slowing down? Are you gonna cum?"
    s "No, I just..."
    s "I didn’t like what you just said."

    scene futabawantsxmasdick31
    with dissolve

    f "We’re just playing...it’s okay."
    s "..."
    f "Keep fucking me...{i}now.{/i} "
    f "Like your life depends on it."

    play sound "static.mp3"
    scene futabawantsxmasdick17 with flash
    stop sound

    s "You mean like {i}this,{/i} Futaba?"
    f "MMMMMNGHYES!!!! Just like that! Mess me up, [futabamaster]! Fuck me like you...hate me! Do it! Haaah!"

    "I imagine the one I hate the most."

    scene black
    stop music

    "I black out for the next ten minutes."
    $ renpy.pause(10, hard=True)
    play sound "static.mp3"
    scene futabawantsxmasdick32 with flash
    stop sound
    play sound "dosex.mp3"

    f "Ngaa...aah...aaaahhhhaaaa......aaaaaaahhhhhh..........."

    "When I zone back in, I can feel myself thrusting into the warm, sticky reservoir of flesh that I had emptied my seed into when the world went black."
    "Futaba appears to have cum again as well. She always leaves more evidence of that than the others."
    "But there’s fluid that falls from her eyes as well now."
    "It somehow makes them even more beautiful."

    f "Mngaaahaahhhaaaaa....aaaahhhh....haaaaaah!"
    s "Did I break you?"
    f "Haaard.......aaaah.......haaarder...."

    if molly_lust >= 10:
        $ renpy.end_replay()
        $ futabalust40 = True
        $ futaba_lust += 1

        jump mollylust10

    else:
        scene black
        with dissolve2

        "I do as she says and fuck her harder."
        "I don’t let up until her voice ceases its marble reverberation."
        "Her insides are flooded with evil."
        "So are mine, I think."
        "Some days, it’s hard to tell."

        $ renpy.end_replay()
        $ futabalust40 = True
        $ futaba_lust += 1
        $ mollylust10miss = True
        $ christmastsubasa1miss = True

        "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
        "........."
        "......"
        "..."

        jump christmasfive6

label futabaspring2:
    scene sky
    with dissolve2
    play music "morningmoon.mp3"

    "A long time ago, I used to visit the library pretty frequently. And one of the key reasons for that was how Futaba was among the most...{i}accepting{/i} of my advances early on. "
    "Of course, I would subsequently learn that a great deal of that was the result of her nearly-absent self-esteem. But it’s not like I knew that {i}immediately.{/i}"
    "It took a few visits first. And {i}in{/i} those first few visits, I learned that there is and {i}was{/i} far more to her than just the flaws she gets hung up on."
    "There’s a girl in there who wants to succeed and wants to be recognized. But the one she wants to be recognized {i}by{/i} is herself rather than me. "
    "Well, she definitely wants to be recognized by {i}me{/i} too. But I have “recognized” her many times by now and she is still unhappy, so I imagine I’m in second place at best."
    "Regardless, I think back on these days as I swallow my pride and return to the halls I used to wander on a daily basis."

    scene futabatree1
    with dissolve2

    "And what I find is that same girl, enduring that same struggle she suffered so long ago in trying to put her feelings onto paper."
    "And I can’t help but wonder if she’s gotten better now that I have forced her into feeling everything one possibly {i}can{/i} before even finishing her first year of high school."
    "Writing is hard, though. Describing how you feel is {i}hard.{/i} And there are only so many words you can do it {i}with,{/i} which makes it even harder."

    f "Mnh..."

    "I guess there’s a good chance she’s just writing smut instead, though. Since that seems to be what she’s most interested in now that she has discovered the joys of elf sex."

    f "This is...much harder than I thought it would be. Maybe I should try a different story instead?"
    s "Talent in the world of writing doesn’t come immediately, Futaba. It’s a skill that’s acquired as time goes on."
    s "{size=-1}For example — Mark Twain didn’t write the Adventures of Huckleberry Finn until he was almost 50 years old. Which means he must have gotten good at writing sometime after that since that book sucked.{/size}"
    f "That doesn’t help me at all, Sensei. Not when the deadline for submissions is-"

    play sound "static.mp3"
    scene futabatree2 with flash
    stop sound

    f "Wait, Sensei? When did {i}you{/i} get here? I didn’t even hear you walk in."
    s "Probably because you’re so absorbed in whatever you’re working on. Which may or may not be smut."

    scene futabatree3
    with dissolve

    f "It’s not {i}smut.{/i} I know better than to write things like that in school."
    s "Didn’t you give me a boob job in the nurse’s office once?"

    scene futabatree4
    with dissolve

    f "She was off that day. Which means I did nothing wrong."
    s "Is she off today too? Want to drop what you’re doing and go relive some happy memories? "

    scene futabatree5
    with dissolve

    f "As {i}nostalgic{/i} as it sounds to help get you off after you went through the trouble of coming all the way over here, I can’t right now. I have to finish this story by tonight or I miss my chance."
    s "Your chance to {i}what?{/i} Is Wakana holding another writing contest or something? "
    f "Miss Watabe isn’t, but there’s a contest I found online to put a creative spin on a children’s book. So I’ve been working on that all week. "
    s "Oh yeah? Can I see what you have done? "

    scene futabatree6
    with dissolve

    s "It might not be as pleasurable as my first suggestion, but grading your unfinished writing is still {i}nostalgic{/i} in its own way, is it not?"
    f "It is...It’s just my first time trying to...parody something, so to speak. And I’m worried that what I {i}do{/i} have will look pretty terrible compared to the original story."
    s "What’s the original story? Which children’s book are you trying to put a spin on?"
    f "The Giving Tree by Shel Silverstein."

    scene futabatree7
    with fade

    s "Well, on the bright side, it’ll be hard for you to write anything even remotely as depressing as {i}that.{/i} "
    f "You think The Giving Tree is depressing, Sensei?"
    s "A tree spends its entire existence catering to an ungrateful boy who ultimately chops it down and turns it into a boat? It’d take a fool to think something like that is happy."

    scene futabatree8
    with fade

    f "Well, I guess you can call me a fool then. Because {i}I{/i} don’t think it’s as sad as you’re making it sound."
    s "Of course you don’t. Because you’re in that bracket of people who don’t mind sacrificing themselves for others even when it means you’re going to wind up hurting."
    f "And {i}you’re{/i} in that bracket of people who don’t mind chopping down a tree you’ve grown up with so long as it benefits you in some way."
    s "You’re right. You don’t need to worry about me turning you into a boat, though. We’d probably just both drown if I tried to do that."

    scene futabatree9
    with dissolve

    f "Well, what {i}would{/i} you try to do, Sensei? Because I think your outlook might be really helpful here since I’m trying to approach this story from the opposite angle."
    s "You mean, like...a “Taking Tree” instead of a “Giving Tree?”"
    f "Exactly. And it’s from the perspective of the boy instead this time, who sees the tree more like a curse than something beneficial to him."
    f "I’ve obviously had to change a few things in order for it to make sense, but the format is the same. And I got Maya to help me draw some of the pictures to keep the kids entertained."
    s "Maya can draw? Since when?"

    scene futabatree10
    with dissolve

    f "Since always, I think. I’m surprised you didn’t know. "
    f "She actually used to draw quite a bit for the manga club until Molly started making too many demands and Maya stopped just to spite her."
    s "Yeah, that tracks. Aren’t you worried a story like this might be too dark for kids, though? Like, what’s the takeaway supposed to be in a book about a cursed tree?"

    stop music
    play sound "static.mp3"
    scene futabatree11 with flash
    stop sound

    f "{i}The takeaway is supposed to be that there are always going to be things out there that want to hurt you.{/i}"
    f "{i}And yeah, I guess that might be a little dark for a children’s book. But it’s an important theme to explore, I think. {/i}"
    f "{i}And it might help some kids understand bullying a little better if they ever have to experience that. Which...they probably will. Most people do.{/i}"
    s "{i}Hm...{/i}"
    f "{i}Were you ever bullied, Sensei?{/i}"

    play sound "static.mp3"
    scene futabatree12 with flash
    stop sound
    play music "morningmoon.mp3"

    s "Not really. But anyway, if that’s the angle you want to go with, I’m sure it’s doable. Especially with your outlook and...{i}experience{/i} in the subject matter. "
    f "Yes, I’m a bit of an expert in the field of being bullied, aren’t I?"
    s "Just means you’re stronger now. "
    f "It doesn’t really. That {i}is{/i} the approach I’m taking from a writer’s perspective, though — showing how years of the tree’s {i}curse{/i} sort of help the boy build up an immunity to it."
    s "How exactly does a tree {i}take{/i} something, though? "
    f "I mean, it’s not like it’s {i}physically{/i} taking anything. But it looms over his house, and every time  he sees its shadow cross into his yard, something bad happens. "
    s "That’s not the {i}tree’s{/i} fault though, is it? It can’t control its own shadow. "
    f "No, but the boy is just a boy. So {i}he{/i} doesn’t know that. Which is why he gives the tree an evil voice whenever he visits it to ask it to leave him alone."
    f "Then, by the time he’s old enough to understand how shadows work, he’s already associated the tree with horrible things happening. Hence the “curse.”"
    s "I see..."

    play sound "static.mp3"
    scene futabatree13 with flash
    stop sound

    f "You hate it, don’t you?"
    s "No, I don’t {i}hate{/i} it. I haven’t even read it yet. It’s just...do you think something like this would have helped you when {i}you{/i} were little?"
    s "Because if it’s from the boy’s perspective and it’s all just cursing this tree that isn’t really {i}doing{/i} anything, it’s sort of just...the Giving Tree {i}again{/i} but with different, sadder narration."

    scene futabatree14
    with dissolve

    f "Yeah...that’s exactly my problem. No matter what I do, I can’t figure out how to actually make the tree {i}evil.{/i} And the boy keeps forgiving it in the end. "
    f "But that’s not what I want. I {i}want{/i} him to hate it. And I {i}want{/i} him to chop it down and...get revenge for all of the terrible things it did but...didn’t {i}really{/i} do..."
    s "But you know that wouldn’t send the message you want to send..."

    scene futabatree15
    with dissolve

    f "Right...Which is why I keep thinking it might be better to just try and use a different story instead. But I really like this one and...I don’t know. "
    f "Maybe it’s just me not being as good of a writer as I {i}want{/i} to be yet? Like, if I can’t get the simplest idea across in the simplest {i}format,{/i} what does that say about my skill?"
    f "Have I learned nothing at all this whole time? How come {i}I{/i} still suck while people like Nodoka can just write whatever they want and make it sound good?"

    scene futabatree16
    with fade

    s "Comparing yourself to gifted people like that will always be a recipe for disaster, Futaba..."
    s "Nodoka’s a very special and very {i}rare{/i} type of person. But it’s important to remember that people like that struggle even {i}harder{/i} sometimes because they don’t have anyone to relate to."

    scene futabatree17
    with dissolve

    s "You and I are lucky we understand one another. We’re lucky we can sit here and identify the cracks in your story when {i}Nodoka{/i} likely wouldn’t even recognize them as cracks at all."

    scene futabatree18
    with fade

    f "That’s...fair."
    f "Do you and I really understand one another, though?"
    s "As much as we can, I think. With plenty of room for error, of course. I don’t know if it’s possible to ever really {i}fully{/i} understand someone."
    s "I just know that if you’re trying to {i}force{/i} an idea across, it’s not going to work. It’ll come off as {i}preachy{/i}...or {i}inauthentic{/i}...or even worse — it could come off as Huckleberry Finn."

    scene futabatree19
    with dissolve

    f "Why am I just learning today that you have such great disdain for Huckleberry Finn?"
    s "Why am {i}I{/i} just learning today that you are trying to {i}write{/i} behind my back when I am supposed to be your writing coach? We had an agreement."
    f "Did we? Why am I learning right now that you actually care about my writing? I figured you gave up on that once we started having sex."
    s "..."
    f "That came out meaner that I wanted it to. I’m sorry."

    scene futabatree20
    with dissolve

    s "Don’t be. You’re clearly not the only one here struggling to get their feelings across. And I’m sure it hasn’t helped at all that I just walked away from school entirely."
    s "I don’t actually blame you for writing “behind my back.” I was just being a facetious douche again."

    scene futabatree21
    with dissolve

    f "Wait, are you okay? Because I suddenly feel {i}really{/i} bad about saying what I said if that’s your response to it."
    s "Are {i}you{/i} okay? Because if you’ve spent the last week wanting to murder a fictional tree for revenge, I can’t imagine you’re the same Futaba I’ve been jerking off to this whole time."

    scene futabatree22
    with dissolve

    f "..."
    s "That came out lewder than I wanted it to. I’m sorry."
    f "Don’t be. I was masturbating to you before we ever even talked."
    s "That makes me feel a lot better. Thank you, Futaba."

    scene futabatree23
    with dissolve

    s "What are we going to do about your story, though? It needs to be done by tonight, doesn’t it?"
    f "{i}You{/i} don’t need to do anything, Sensei. I’ll probably just go with my gut and finish “The Giving Tree Pt. II” and hope no one else submitted anything for the contest."
    f "But maybe soon, I can try writing something...original again. And you can read that and tell me more about how inadequate it is or...what I need to {i}change.{/i}"

    scene futabatree24
    with dissolve

    s "Futaba, you’re a teenager. You don’t need to be {i}perfect.{/i} It would be weird if everything you wrote {i}was{/i} adequate. Having to change things is completely normal. For professionals too."
    f "I know...I know. I just...kind of {i}need{/i} to win this. And that pressure isn’t...meshing well with everything else that’s been going on in my head lately. "
    s "Why do you...{i}need{/i} to win a children’s book writing contest exactly?"
    f "..."
    s "Futaba-"
    f "I need the money."

    scene black
    with dissolve2

    f "I’m trying to go to America. "

    "........."
    "......"
    "..."

    scene futabatree25
    with dissolve2

    s "You really {i}still{/i} haven’t heard anything from your parents? It’s been, like...over a year, hasn’t it?"
    f "That’s why I want to go find them. It’s, like...{i}super{/i} weird. And unnerving. They’ve always trusted me to be independent, but they’ve never just...{i}left me alone{/i} for this long before."
    s "But...money won’t be enough to get you to there. You know that, right? There’s still the matter of the barrier and-"
    f "I just have to figure out how to get through it. {i}You{/i} did once, didn’t you?"
    s "I don’t...really know. I just remember following Nodoka and...that’s pretty much it."
    f "Still, there has to be a way...there {i}has{/i} to."
    f "Don’t you think people are too...accepting of this? Being stuck here? Just...living our lives, completely unsure of when and {i}if{/i} we’ll ever be allowed to leave again?"

    scene futabatree26
    with dissolve

    f "Don’t you want to know what’s out there, Sensei?..."
    f "What we’re missing?..."
    s "I...{i}do.{/i} But there are things about this world that don’t exactly make sense. So I’m hesitant to-"
    f "Don’t you want to know what’s out there, Sensei?..."
    f "What we’re missing?..."

    stop music
    play sound "static.mp3"
    scene futabatree27 with flash
    stop sound

    s "{i}...{/i}"
    f "{i}Sensei?{/i}"
    s "{i}How am I supposed to respond to that when you’ll just ignore anything I have to say?...{/i}"
    f "{i}What? Why would I-{/i}"
    s "{i}I don’t think it’s safe out there, Futaba. I think you should stay here. With me.{/i}"
    f "{i}Sensei...But my parents-{/i}"
    s "{i}What if you can’t find them?{/i}"
    f "{i}...{/i}"
    s "{i}What if something happened?{/i}"
    f "{i}...{/i}"
    s "{i}Then what, Futaba?...{/i}"
    f "{i}Then I find out what it was...{/i}"
    s "{i}...{/i}"
    f "{i}I can’t just keep waiting around, though...{/i}"
    f "{i}I’ve already tried that...and it’s driving me insane.{/i}"
    s "{i}...{/}"
    f "{i}I can’t take it anymore, Sensei...{/i}"
    f "{i}I need something...{/i}"
    f "{i}Anything...{/i}"
    s "{i}...{/i}"
    f "{i}And I’m not going to find any of that in this town.{/i}"

    play sound "static.mp3"
    scene colorbars with flash
    stop sound
    play sound "colortone.mp3"
    $ renpy.pause(10, hard=True)
    scene black
    stop sound
    $ renpy.pause(5, hard=True)
    "/////////////////////////CONNECTION LOST"

    $ renpy.end_replay()
    $ futabaspring2 = True
    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump noonch4

label beachsixfutaba1:
    stop music
    scene abugabug
    play sound "abugabug1.mp3"
    $ renpy.pause(12.5, hard=True)
    play sound "abugabug2.mp3"
    $ renpy.pause(15, hard=True)
    scene black
    $ renpy.pause(2, hard=True)
    scene todd
    $ renpy.pause(5, hard=True)
    scene black
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene futababeachinfection1 with flash
    stop sound
    play music "samhain.mp3"

    ay "...and from that point on, I decided it would be in the best interest of the universe if I just never encountered a live salmon again."

    scene futababeachinfection2
    with dissolve

    ay "Which is fine! I just need to be extra careful if I ever visit the Pacific Northwest in Q4 of any given year. We have enough clown-based fatalities as-is."
    o "Thank God you explained the foundation of this story in the beginning. I can only imagine how confusing it would be for someone to walk in at the tail end of it."
    t "I particularly enjoyed the connections drawn between 70’s shag carpeting and aquatic mating routines. I feel as if I have learned a lot today."
    a "It’s crazy to think about how carpets like that used to be a thing at all. Style today is all about being sleek and clean. I’d {i}hate{/i} having to vacuum something like that so often."

    scene futababeachinfection3
    with dissolve

    r "Speaking of style, Ami — what’s the plan with your hair? "

    scene futababeachinfection4
    with fade

    r "Are you gonna grow it back out again and rejoin me in the OG haircut club? Otoha brought back the top-knot, so I think she’s planning on joining as well."
    o "It was either that or the straight girls club Miku is starting. Which I’m pretty sure neither one of us is  allowed to join based on the fact that we have made out like a million times."
    ay "Oh! Ami and I joined that and we’ve kissed before, so I don’t think the screening process is very thorough."

    scene futababeachinfection5
    with dissolve

    r "If it was {i}just{/i} kissing, maybe. But I’m not sure I’d be able to live with myself if I joined a straight girls club after all of the other stuff you did to me. "
    t "Please explain these things now. My sexual curiosity is at an all-time high and I require assistance in determining whether or not I am attracted to female traits apart from Ami’s legs."
    o "I’m not sure if I’m allowed. Rin’s new guard dog might show up and try to gut me if I talk about that again."

    scene futababeachinfection6
    with fade

    r "Chika’s not a {i}guard dog,{/i} Otoha! She’s just...a friend! A...really {i}close{/i} friend. Who is...certainly more protective than normal lately...but still just a friend!"
    o "Mhm, right. And {i}I{/i} was a good girlfriend."
    r "You were! Best I’ve ever had at least. I’d give you a solid 7/10. Guitar skills translate well to-"
    a "Sorry to interrupt...whatever {i}this{/i} is, but I’m still not really sure about what to do. And I was actually wondering what you guys would suggest."

    scene futababeachinfection7
    with dissolve

    a "Ayane? Tsuneyo? Short hair Ami or long hair Ami? Which one’s better?"
    ay "I like long hair Ami. Short hair Ami is good too, but twintails are lacking proper representation now and Io’s aren’t really as impressive as yours were."
    t "Personally, I am too invested in why characters are always pictured holding food in video games but never actually {i}eating{/i} it."

    scene futababeachinfection8
    with fade

    ay "Hm? Oh, this? I’ll eat it now!"
    t "{i}Hah...{/i}it’s no use. Perhaps it is just impossible to properly depict based on asset restrictions."
    o "Cast my vote for short hair. It’s nice having some competition in the princely department. "
    o "Plus, from what I hear, some of the girls in other classes have already started crushing on you, Ami. "
    r "Girls in other classes don’t exist to me and your new hair makes me want to touch you, so I vote for long hair Ami again so I don’t have to feel conflicted about that anymore."

    scene futababeachinfection9
    with dissolve

    a "What about you, Futaba? Any preference? Or should I maybe try and split the difference and go for, like...medium length or something?"
    o "Futaba’s locked in right now. Don’t think you’ll be getting an answer from her."
    r "You want breakfast or anything, Futaba? I can go grab you something from the shack. Coffee, maybe?"
    f "No thank you."
    r "Kay. Just make sure you eat {i}something{/i} later, alright? You skipped dinner last night too. We need all the energy we can get for D&D later."
    f "Okay."
    ay "What are you writing, Futaba? Another fantasy thing?"
    f "Essay."
    a "Ew, homework? Now? But this is vacation."
    o "Not homework. Looks like an essay on-"

    scene futababeachinfection10
    with dissolve

    o "Western civilization? Why? Are you applying to colleges already?"
    f "Please...shut up."
    r "See — the reason Otoha is so dumbfounded right now is because she’s secretly racist and hates western civilization. It was a real problem for our relationship."

    scene futababeachinfection11
    with fade

    o "{i}It came up literally once!{/i}"
    r "{i}After you struck me! Coincidence? I think not...{/i}"

    scene futababeachinfection12
    with dissolve

    f "{i}PLEASE. SHUT UP.{/i}"
    mak "Oh, Sensei. You’re up early. Good morning."
    s "I’m not awake because I {i}want{/i} to be. Io snuck into my room again and accidentally knocked something over."
    mak "Is that a...thing she does often?"
    s "It’s like that thing people say about not feeding stray animals who wander into your yard. If you do, they’ll keep coming back."

    scene futababeachinfection13
    with dissolve

    s "What’s going on over there? Was that Futaba I just heard raising her voice?"
    mak "Yeah. She was up all night writing. Came here to try and get some peace once the other girls started waking up but, lo and behold, peace is no more."
    s "Knowing that makes it sound like you were up all night as well."

    scene futababeachinfection14
    with dissolve

    mak "{size=-1}I was! Which means I am also very tired. But fortunately, I should be able to ride a caffeine wave for the rest of the day. {i}And{/i} I got a lot done. So I’d say it was an excellent use of my infinite time.{/size}"
    s "A lot done in regard to...what, exactly?"
    mak "{size=-1}Reset stuff. I think I’ve found a way to make the Rooftop Apocalypse Squad’s activities a lot more exciting and fun so we’re not just standing around waiting for something to happen all the time.{/size}"
    mak "I’m gonna talk to Maya and Yumi about it later. Tsuneyo and Nodoka too, but both of them have been acting kind of...off."

    scene futababeachinfection15
    with dissolve

    s "Really? Tsuneyo looks fine to me. Perhaps...{i}too{/i} fine. Is Imani really letting her wear that?"
    mak "Miss Imai’s been drooling over her just as much as you have. Just {i}she{/i} has the tact to not say anything out loud."
    s "She has more underboob than you have regular boob."

    scene futababeachinfection16
    with dissolve

    mak "Okay. Well, {i}that{/i} was just unnecessary."

    scene futababeachinfection17
    with fade

    ay "So, Otoha! How’s my little Sana getting along in the light music club? She’s not causing you guys any problems, is she?"
    o "Honestly? She’s not bad at all. She has some issues with the bass pedal, but her timing is solid and Rika’s been working pretty closely with her after school most days."

    scene futababeachinfection18
    with dissolve

    o "We’re still just in the {i}covers{/i} phase right now since we haven’t been able to decide on a direction for the band. But I think we might actually be able to start working on an original soon."
    o "Thankfully, I’ve got like a million banked already. Just have to find the right one, you know? Like there’s this one that goes-"

    play sound "static.mp3"
    scene futababeachinfection19 with flash
    stop sound

    r "{i}Hey. You good?{/i}"
    f "No."
    r "{i}Wanna go back to the room? Maybe somewhere quieter? I know you’re trying to work.{/i}"

    scene futababeachinfection20
    with dissolve

    f "Yeah. I’d be much happier failing where no one can watch me. Great fucking idea, Rin. Why didn’t I think of that?"
    r "Huh? I just-"

    scene futababeachinfection21
    with dissolve
    stop music fadeout 12.0

    f "Just shut the fuck up and stop checking on me every five minutes! No wonder Otoha hit you when you did the same fucking thing to her!"

    play sound "static.mp3"
    scene futababeachinfection22 with flash
    stop sound

    ay "Woah! Where did {i}that{/i} come from? That’s not like you, Futaba."
    f "Oh, what? So {i}they{/i} can joke about it? But when {i}I{/i} do it, it’s a fucking problem?! Fuck you too, Ayane! Why don’t you mind your own fucking business?!"

    scene futababeachinfection23
    with dissolve

    ay "...What?"

    play sound "static.mp3"
    scene futababeachinfection24 with flash
    stop sound

    mak "Uhh..."
    mak "You didn’t...hear what started this, did you? Because I feel like I stopped paying attention for literally five seconds and now {i}this{/i} is happening."
    s "No...I have no clue."
    s "I...feel like we should probably do something, though."
    mak "Not {i}me.{/i} I’m running on zero hours of sleep and am not particularly well-loved among peers. This has “you” written all over it."

    play sound "static.mp3"
    scene futababeachinfection25 with flash
    stop sound

    f "Just give me some fucking space! It’s infuriating enough that I have to {i}look{/i} at all of you all weekend! But being {i}pitied{/i} as well?! Just let me fucking work!"
    f "I came over here to get away from {i}you!{/i} Remember?! I swear, it’s like all of you exist just to fucking distract me and make my life harder! Just go the fuck away!"
    r "I was just trying to-"

    scene futababeachinfection26
    with dissolve

    f "{i}Oh, waaaaaah! I was just trying to help! Oh, woe is me! I have everything a girl could ever need and don’t understand what it’s like to actually suffer!{/i}"

    scene futababeachinfection27
    with dissolve

    f "Just fucking {i}shut up{/i} already! Oh, and stop reminding me to eat as well! Because Sana skipped dinner too and I don’t see you fucking micro-managing {i}her!{/i}"
    o "Futaba...I know what’s it’s like to-"

    play sound "static.mp3"
    scene futababeachinfection28 with flash
    stop sound
    play music "thingsthathurt.mp3"

    f "You don’t know {i}shit!{/i} "
    f "You’re a fucking prodigy who can write anything she wants {i}whenever{/i} the fuck she wants — with loving parents and a home to return to! "
    f "You think {i}you{/i} understand what I’m going through just because you {i}also{/i} get interrupted sometimes?! Get lost! Go back to your side of the city and stop acting like you belong here! "
    ay "Otoha, she doesn’t mean that. Sensei! Can you come here, please?!"

    play sound "static.mp3"
    scene futababeachinfection29 with flash
    stop sound

    f "Oh, woooow! Ayane’s calling over {i}Sensei{/i} again! What a crazy twist! I haven’t seen her try to get his attention since, what...yesterday? It’s a new fucking record! "
    t "Perhaps I am lacking context here, but I do not understand the cause for such fury from someone who is so typically mind-mannered."
    f "Yeah, well you don’t fucking understand {i}anything{/i} because you somehow have even less personality than {i}me!{/i}"
    f "Like, if it wasn’t for riding fucking Molly’s coattails all day, who would you even be? What would you like? Noodles? Awesome. Good for you! How FUCKING interesting! "
    t "I am confused. It sounds as if I am supposed to be insulted by this. But I merely just feel seen."
    f "BECAUSE YOU’RE A FUCKING MORON! YOU’RE ALL FUCKING MORONS! EVERYONE ONE OF YOU! AND I CAN’T FUCKING STAND IT ANYMORE! THIS PLACE ISN’T REAL! NONE OF YOU ARE REAL!"
    r "Futaba! Where are you going?!"

    play sound "static.mp3"
    scene futababeachinfection30 with flash
    stop sound

    s "I was just about to ask the same thing. Stop."
    f "Get the fuck out of my way! If you’re looking for someone to suck you off, there’s a whole table full of girls twenty feet away practically begging to! Talk to {i}them{/i} instead!"
    s "I don’t {i}want{/i} to talk to them. I want to talk to {i}you.{/i} I need to know what’s going on."

    scene futababeachinfection31
    with dissolve

    f "Why?! So you can pretend to fucking give a shit again?! Because every time you’ve “helped” me with anything, it was always just to {i}get{/i} something!"

    play sound "static.mp3"
    scene futababeachinfection32 with flash
    stop sound

    f "And you’ve sure fucking {i}gotten{/i} it, Sensei! So many times that I need to use {i}three{/i} fingers just to get myself off now! I’m in high school! Do you know how that makes me feel?!"
    r "Futaba! Stop! You’re just making things worse!"
    f "Do you know how fucking shameful it’s going to feel when you ultimately leave me and I have to explain to the {i}next{/i} guy I’m with that his dick is too small to make me feel anything?!"
    s "I-"
    f "And don’t hit me with some fucking bullshit line like, “Oh, Futaba! I won’t leave you,” either! Because despite having fucked me a {i}thousand{/i} times, you still won’t even say you {i}love{/i} me!"
    f "What do I have to do to become more than a convenient fucking cock-sleeve to satisfy the pathetic, adolescent desires you should have grown out of a fucking decade ago?!"

    scene futababeachinfection33
    with dissolve

    f "Because I can’t do {i}that!{/i} And I can’t {i}write!{/i} I’m not good at sports! I’m not particularly smart! So what the fuck do I have to offer?! What makes {i}me{/i} special?!"
    f "No fucking wonder nobody’s acknowledging any of my contest submissions! They’re probably flagged as fucking spam the moment I send them!"
    f "It’s just hopeless to try! So why even bother?! "
    f "Why not just throw myself into the fucking ocean and never come out?! Because I suck at swimming too! At least I’d make a good meal for a fucking shark!"
    r "Futaba, please. You’re scaring me."

    scene futababeachinfection34
    with dissolve

    f "Then that’s just more proof that something is wrong here. "
    f "Because if you’re scared of {i}me...{/i}and not scared of {i}him,{/i} that’s just bad writing. "
    f "Think of the readers, Rin. Think of how it looks to have {i}me{/i} be the bad guy while the lecherous schoolgirl-fucking “hero” swoops in to save the day. The message is lost."

    scene futababeachinfection35
    with dissolve

    f "We are {i}all{/i} lost. And it is {i}your{/i} fault. {i}You{/i} did this. "
    f "{i}You{/i} broke the world. "
    f "And now you’re gonna try and pick up the pieces? Don’t make me laugh."
    f "I hope you fucking choke on the next tongue unfortunate enough to slither into your mouth."

    play sound "static.mp3"
    scene futababeachinfection36 with flash
    stop sound

    r "Jesus fucking Christ, Futaba! What the hell has gotten into you?!"
    s "Woah..."
    s "That was-"

    scene futababeachinfection37
    with dissolve

    r "That was nothing. Forget literally all of that. Something’s clearly wrong and I need to go chase after her to find out what. "
    r "She gets like this when she...well, she...gets like this sometimes. But I could have sworn that-"
    s "I don’t think this is...a regular sort of problem, Rin. I can’t imagine it’s something you’ve dealt with before."
    r "Yeah, well I don’t exactly have the luxury to think about that right now. I’ll talk to you later, Sensei."
    r "And...don’t take any of that too personally, please. She doesn’t actually feel that way."

    scene black
    with dissolve2
    stop music fadeout 10.0

    s "Right..."

    "But while she might not, some will. Some {i}do.{/i}"
    "And so I shout into the void I so routinely dump the rest of my thoughts into, seeking an answer as to why they’ve wrapped their tendrils around {i}her{/i} of all people. "
    "But I shout that without realizing she is far from the first — and that countless others may have already been pulled into the abyss."
    "If you spend long enough in there, you won’t realize how wrong everything is."
    "Maybe I {i}did{/i} break the world if that’s the case."
    "The only questions then becomes..."
    "When?"

    play sound "doorclose.mp3"
    "{i}Futaba and Rin have exited the update!{/i}"

    $ renpy.end_replay()
    $ beachsixfutaba1 = True
    $ futaba_love += 0
    $ rin_love += 0

    "{i}[[REDACTED]’s affection has increased by 0!{/i}"
    "{i}[[REDACTED]’s affection has increased by 0!{/i}"
    "........."
    "......"
    "..."

    jump beachsix4
