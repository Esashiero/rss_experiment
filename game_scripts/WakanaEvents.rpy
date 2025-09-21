label callwakanamorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if wakanadate1 == False:
        jump wakanadate1
    if secondbeach18 == True and christmastwo20 == False:
        "I should probably give Wakana a little space for now."
        jump callmorning
    if wakana_love >= 15 and yumiyukispecial1 == True and wakanadate15 == False:
        jump wakanadate15
    if chap4active == True:
        jump wakanaspringmorninggen
    if chapthreeactive == True:
        jump wakanasummer2morninggen
    else:
        play sound "phonebeep.wav"

        "I tap on Wakana's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        w "What do you want?"
        s "Well, good morning to you as well, Wakana."
        w "Nothing? Okay. Goodbye."
        s "Wait, no. What are you doing right now?"
        w "Working."
        s "Oh."
        s "Yeah, never mind then."
        w "That's what I thought."

        play sound "phonebeep.wav"

        "I hang up the phone and decide to do something else."

        jump callmorning

label callwakanaafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if secondbeach18 == True and christmastwo20 == False:
        "I should probably give Wakana a little space for now."
        jump callafternoon
    if chap4active == True:
        jump wakanaspringnoongen
    else:
        play sound "phonebeep.wav"

        "I tap on Wakana's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        w "Hello?"
        s "Hey. What's up?"
        w "Nothing. Is that all?"
        s "No. I was wondering if you'd want to hang out."
        w "Sure."
        s "Cool. Where did you want to meet up, then?"
        w "Oh."
        w "You meant now."
        w "Yeah, I can't do that."
        s "What? Why not?"
        w "I have things to do."
        w "But feel free to call me later when I...don't have things to do."
        s "Uhh...okay."
        s "I guess I'll talk to you later, then."
        w "I want to fucking die."

        play sound "phonebeep.wav"

        "I hang up the phone and decide to do something else."

        jump callafternoon

label callwakananight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if wakanadate1 == False:
        play sound "phonebeep.wav"

        "I tap on Wakana's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "I guess she's busy tonight."
        jump callnight

    if wakana_love >= 5 and wakanadate1 == True and kaoridate15p3 == True and wakanadate5 == False:
        jump wakanadate5
    if secondbeach18 == True and christmastwo20 == False:
        "I should probably give Wakana a little space for now."
        jump callnight
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Wakana's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "I guess she's busy tonight."
        jump callnight
    if chapthreeactive == True:
        jump wakanasummer2nightgen
    else:
        jump wakananightgen

label wakananightgen:
    play sound "phonebeep.wav"

    "I tap on Wakana's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    w "I want to-"
    s "Wait. Before you go wanting to fucking die, I'd like to offer you a once in a lifetime opportunity to hang out with me."
    w "Once in a lifetime? You have barely let me breathe since the moment we met."
    s "If that were true, you'd probably like me a lot more than I think you do in the first place."
    w "That would be a fair assumption."
    w "I'll allow you to meet me at the local cafe for tea, but the moment you say anything even remotely irritating, I'm leaving."
    s "I'm sure it will be a very fun and fulfilling five minutes, then."

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene wakananightgen
    with fade
    play music "sleepystreets2.mp3"

    "I make my way over to the cafe where I first got Wakana's number and focus most of my energy on not annoying her."
    "This proves to be a bit harder than expected, though, as nearly every single time I open my mouth, she just scowls at me as if she's wishing I was never born."
    "Despite that, however, she does not threaten to leave even once and ultimately winds up downing so many cups of tea that I lose count of them."
    "Osako's confirmed in the past that Wakana definitely enjoys my presence to at least some extent, and I begin to wonder if the whole {i}not leaving{/i} thing is just how that manifests."
    "But, of course, she is notoriously hard to read given that her entire personality seems to be nothing more than a vicious cycle of varying levels of sadness."

    scene black
    with dissolve

    "We hang out for a short while longer before Wakana receives a call from her significant other summoning her home for dinner."
    "Not wanting to prioritize me in any way (Which, frankly, I understand) she pays for all six thousand (Estimated) of her cups of tea before getting up and leaving the table."
    "I remain at the cafe and watch her through the glass as she removes an umbrella from seemingly nowhere, d[raping] it over her head as she begins her walk home."
    "Another hour goes by in complete silence before I decide to leave as well."

    $ wakana_love += 1
    stop music fadeout 5.0

    "{i}Wakana's affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label wakanadive:
    if chap4active == True:
        jump wakanaspringdivegen
    else:
        scene wakanadivegen
        with fade
        play music "10c.mp3"

        "I find some time to meet up with Wakana and the others at the bar after work."
        "And while the two of us spend the majority of the night attempting to navigate the labyrinth that is conversation with Imani and Rika, we {i}do{/i} find a little time to ourselves after a while."
        "I think it's pretty clear that both of us like them. They're just...very different from the way we are in that they actually {i}enjoy{/i} socializing for some reason."
        "Within these small bouts of downtime, Wakana and I figure out a way to maximize our recharge period- discussing things like poetry and the sex acts she performs on her girlfriend."
        "Okay, so she doesn't really discuss that second part. But I spare no effort in trying to {i}get her{/i} to."
        "Eventually the night grows old and the time comes for all of us to leave- but our tradition manages to survive another week."

        scene black
        with dissolve

        "We split into two groups once we're outside of the bar so no one has to walk home alone and I wind up partnering up with Wakana for the night."
        "But seeing as the two of us live much further away from here than Imani and Rika, we wind up splitting the cost of a taxi and heading back together."
        "Our time as a duo is spent in complete silence, but it never feels...awkward."
        "It's more like we've just exhausted every last bit of energy we have...and decide to {i}be{/i} with each other without really {i}acknowledging{/i} each other."
        "I like it because it's easy."
        "And Wakana likes it because I am no longer probing her for hot lesbian details."
        "Either way, the night comes to an end...but we all manage to get a little closer."

        $ wakana_love += 3
        $ imani_love += 1
        $ rika_love += 1

        "{i}Wakana's affection has increased by 3!{/i}"
        "{i}Imani's affection has increased by 1!{/i}"
        "{i}Rika's affection has increased by 1!{/i}"

        stop music fadeout 7.0

        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label wakanadate1:
    play sound "phonebeep.wav"

    "I tap on Wakana’s name in my phone and wait for her to answer."
    "I don’t really understand how things got to this point...but here we are."
    "Granted, I doubt she’ll answer in the first place. But at least it’s worth a shot."
    "Worse comes to worst, I can always just...go find someone else inherently sad to spend time with."
    "That sure sounds like a lot of fun."

    play sound "phonebeep.wav"

    w "I want to fucking die."
    s "I had a feeling you were going to answer the phone like that."
    w "Oh. It’s you."
    s "So, that wasn’t a personalized greeting and is just the way you answer the phone for everyone?"
    w "What do you want?"
    w "Do you have any idea what time it is?"
    s "Early. Let’s hang out."
    w "Okay."
    s "Now, before you say no, let me give you a list of the pros when it comes to spending time with me. I-"
    w "I said okay."
    w "Are you truly this incapable of simply listening to someone when they speak?"
    s "Wait, really? I don’t even have to convince you?"
    w "I’m in my office. Come here."
    s "Your office? Like, at[school]?"
    w "Correct. Now, goodbye. "
    s "But-"

    play sound "phonebeep.wav"

    s "..."

    "Why is Wakana at[school] on the weekend?"
    "And why this early?"
    "Am I really going to spend the little free time I have going back to the same place I’m forced to “teach” five days out of every week?"
    "..."

    scene black
    with dissolve

    "Of course I am- because there is an attractive girl there who wants to see me."
    "Or, at the very least, is {i}okay{/i} with seeing me."
    "And also has a girlfriend who could break my arm in five seconds if she wanted to."

    s "..."

    "I should probably be careful with what I say to Wakana this morning."
    "........."
    "......"
    "..."

    scene wakanafirstvisit1
    with dissolve2
    play music "sleepystreets2.mp3"

    s "Hey, Wakana. You’re looking awfully beautiful this morning."

    "I fail immediately."

    w "Thank you. I appreciate that."
    s "I'm sorry. I know I-"
    w "I said...{i}I appreciate that{/i}."
    s "Wait, you do?"
    w "Do you believe me to be so dead inside that I’m incapable of receiving a compliment?"
    s "Kind of, yeah."

    scene wakanafirstvisit2
    with dissolve

    w "Fair enough."
    w "Any more than that would have been entirely unprofessional and unwarranted, though."
    w "Especially given that my significant other could snap your arm like a toothpick in less than ten seconds."
    s "Less than five, actually. I already confirmed this in my thoughts a little bit earlier."
    w "How exciting."
    w "Anyway, thank you for coming here to do my bidding."
    s "Your...what?"
    w "My bidding."

    if bonus == True:
        s "Is this a sexual thing?"
    else:
        s "Like...on a horse race?"

    w "You’ve been spending too much time with that Nagasawa girl. "

    if bonus == False:
        s "You are confusing her with Touka. Touka is the one who likes horses."
        w "The only student who matters to me is Miyamura."

    s "Hey, your favorite student of mine is no saint either."

    scene wakanafirstvisit3
    with dissolve

    w "You leave Miyamura out of this. She’s as pure as the whitest snow."
    s "Wakana, she works in a porn shop."

    scene wakanafirstvisit4
    with dissolve

    w "Nonsense. The girl her age who works at the local porn shop does not wear glasses. They are entirely different people."
    s "I didn’t realize you were a customer there."

    if bonus == True:
        w "I’m in a lesbian relationship with a girl who likes being handcuffed. Of course I am a customer there."
        w "Now, can we please move this conversation away from territory that should remain completely unknown to one another as coworkers?"
        w "I only agreed to seeing you today as I’m behind on grading papers and need your assistance."
        s "That is something you should have probably informed me of beforehand."
        w "And risk you not coming to help? Absolutely not."
    else:
        w "I walked in once on accident."

    scene wakanafirstvisit5
    with dissolve

    w "Now, take these and make yourself useful."
    s "You know, maybe the reason you always want to die is because you spend so much time-"
    w "Doing my job?"
    s "Being anti-fun."
    w "I don’t have time for fun. I’m responsible for the education of a multitude of [young_girls] who may or may not wind up turning into more Nodoka Nagasawas as they get older."
    w "For the sake of our future generations, I must repeatedly kill myself on a daily basis."
    w "This is the road I must take. "
    s "Some might even say the {i}road less traveled by.{/i}"

    scene wakanafirstvisit6
    with dissolve

    w "Don’t try to appeal to me through overrated literary references. Frost was a hack."
    w "Why spend so much time writing about {i}nature{/i} of all things when essentially every other topic known to man is both far more interesting and far more...not fucking stupid."

    if bonus == True:
        w "The outside world is nothing but a hellish landscape even in the coldest of winters and I will not sit idly by as you quote a man who would probably fuck a tree if given the opportunity."
        s "You...feel pretty strongly about this, don’t you?"
    else:
        w "The outside world is nothing but a hellish landscape even in the coldest of winters and I will not sit idly by as you quote a man who would probably hug a tree if given the opportunity."
        s "I would also hug a tree, but I am the huggy boy so-"

    w "Are you going to help me grade these tests or not?"

    scene wakanafirstvisit7
    with dissolve

    s "This is a pretty nice office you’ve got here, Wakana."
    w "Oh my fucking god. Why do you even work here?"
    s "I think it’s a little smaller than mine overall, though."

    scene wakanafirstvisit8
    with dissolve

    if bonus == True:
        w "Yes. It’s almost as if the Japanese work force values male employees more than it does female ones- even when said males aimlessly wander the halls, sodomizing students with their eyes all day long."
        s "Hey. Don’t lump all males in with me. I’m a special exception."
        w "You sure are."
    else:
        w "Yes. It’s almost as if the Japanese work force values male employees more than it does female ones."
        s "We should work together to change that one day."
        w "I'll add it to my to-do list."

    s "Really, though. You should stop being so serious all the time."

    scene wakanafirstvisit9
    with dissolve

    w "I think you may be misinterpreting how much “time” we have left. "
    w "Every day, we slip further and further into a pit of despair that even the most seasoned of climbers will one day struggle to find their way out of."
    s "So you’re trying to get out by just subjecting yourself to {i}more{/i} despair?"
    s "What’s the strategy here?"
    w "The strategy is that you mind your own fucking business."
    s "Oh, I know- why don't we talk a little more about poetry?"
    w "You? The person who quoted the fucking “Road Not Taken?” "
    w "What’s next? Plums?"
    s "I just want to spend some time with a Wakana Watabe who isn’t killing herself over a job she doesn’t even like."

    scene wakanafirstvisit10
    with dissolve

    w "It’s not as if I don’t {i}like{/i} it. I just...don’t like it?"
    s "Deep."
    w "What I mean to say is that it’s as if there’s no true payoff anymore."
    w "You’re not a teacher, so you likely won’t understand, but the most satisfying part of this job is watching the flowers you've cultivated finally being plucked and stuck into vases all over Japan."
    w "The sense of accomplishment in knowing that you were able to impact the lives of others in some form."
    w "And...for some reason-"
    w "It feels as if that “payoff” is further away than ever before."
    s "..."

    "From out of Wakana’s mouth crawls an invisible spider in the form of a thought."
    "It quickly makes its way over to me and sinks its fangs into my skin, injecting me with the question of what effect the distortion of time has in scenarios like this."
    "If Wakana’s memories carry over from one reset to the next, the same way everyone else’s seem to-"
    "And her outlook on her profession is centered entirely around the relief that is provided once a[school] year comes to an end-"
    "Wouldn’t something like this put her into limbo?"
    "Endlessly chasing after a goal that’s impossible to obtain, yet clinging onto the belief that it’s just around the corner."

    scene wakanafirstvisit11
    with dissolve

    w "What’s this? {i}You{/i}, of all people, turning silent?"
    w "Don’t tell me that...you were able to understand what I was saying after all?"
    s "Do you have a favorite poet, Wakana?"

    scene wakanafirstvisit12
    with dissolve

    w "You’re still going on about that?"
    w "Just help me grade my fucking tests so we can get out of this place."
    s "I just want to know what sorts of things inspire {i}you{/i}- a person who, somehow or another, still gets up in the morning to try and inspire others."

    scene wakanafirstvisit13
    with dissolve

    w "Hah..."
    w "You can probably tell just by looking at me. "

    scene wakanafirstvisit14
    with dissolve

    w "{i}But when within thy wave she looks-\nWhich glistens then, and trembles-{/i}"
    w "{i}Why, then, the prettiest of brooks\nHer worshipper resembles;{/i}"
    w "{i}For in his heart, as in thy stream,\nHer image deeply lies-{/i}"
    w "{i}His heart which trembles at the beam\nOf her soul-searching eyes.{/i}"
    s "Edgar Allan Poe."

    scene wakanafirstvisit15
    with dissolve

    w "Did you actually know that one? Or was it just my choice of clothing after all?"
    s "I knew it."
    s "Just because I vehemently refuse to do my job doesn’t mean I’m not actually smart."
    w "Do you believe there to be a correlation between one’s level of intellect and how many lines of poetry they’ve memorized?"
    s "Not really. But I know stuff and knowing stuff makes me cool."

    scene wakanafirstvisit16
    with dissolve

    w "Hm."
    s "Are you impressed? Have I finally convinced you to take a break from doing your job on your day off?"
    w "Absolutely not."
    w "Though, I suppose it wouldn’t hurt to spare five minutes or so."

    scene black
    with dissolve

    "Wakana makes her way over to a bookshelf on the side of the room and drags her finger across a number of what appear to be anthologies."
    "She eventually stops on one and removes it from the shelf, leaning up against it and popping the book open as if she’s already memorized where a certain poem is located."
    "Either that or she’s just reading a random poem she opened to- but I'd like to believe that there was at least some level of tact or calculation to it."

    scene wakanafirstvisit17
    with dissolve

    w "{i}She walks in beauty, like the night\nOf cloudless climes and starry skies;{/i}"
    w "{i}And all that’s best of dark and bright\nMeet in her aspect and her eyes;{/i}"
    w "{i}Thus mellowed to that tender light\nWhich heaven to gaudy day denies.{/i}"
    s "That’s not Poe. Isn’t that-"

    scene wakanafirstvisit18
    with dissolve

    w "Lord Byron. "
    w "You asked me for a favorite poet, to which the answer was Poe."
    w "But if I were to choose a favorite poem, it would be this one."
    s "Why this one?"
    w "The answer is quite embarrassing, so I’d rather not say."
    s "Why even read it in the first place then? We're supposed to be using this opportunity to deepen our relationship."
    w "Why, I believe we just did."
    w "Now-"
    w "Back to work."

    scene black
    with dissolve

    "As quickly as she had found the book and thus the poem, she slides it back into place and makes her way over to her desk."
    "Without even drawing a breath, she once again holds out a file containing a bunch of tests and...expects me to know what to do with them."

    scene wakanafirstvisit5
    with dissolve

    w "Playtime is over. Either help me or get out."
    s "You are an entirely unexciting friend to have, Wakana."
    w "And you are proving to be an entirely useless one."
    w "Though, I can’t say I’m at all surprised."
    w "Even if you do have surprisingly decent taste in poetry apart from that fucking Robert Frost guy."
    s "What in the world did Robert Frost do to you to make you hate him so much?"
    w "Existed. "
    w "Now, take these fucking tests. My arm is getting tired."

    scene black
    with dissolve2

    "Surprisingly enough, I {i}do{/i} take the tests from Wakana."
    "However, I’m only able to grade three of them before getting bored and deciding to head home."
    "I also just mindlessly marked a few of them off instead of actually paying attention to them, so I apologize in advance to anyone who may have failed because of me."
    "But I’d also like to thank those people for allowing me to get a little closer to Wakana- something I didn’t really ever think I’d be able to do."

    $ renpy.end_replay()
    $ wakanadate1 = True
    $ wakana_love += 1
    stop music fadeout 5.0

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label wakanadate5:
    play sound "phonebeep.wav"

    "I tap on Wakana’s name in my phone and wait for her to answer, hoping that, wherever she is, it isn’t at[school]."
    "I really don’t like the idea of her using my friendship for the sole purpose of grading papers faster, but I have a creeping suspicion that last time was not {i}actually{/i} the last."

    play sound "phonebeep.wav"

    w "I want to fucking die."
    s "Hey, Wakana. I’m glad to hear you’re doing fine."
    w "I need your help."
    s "I’m not grading any more papers for you."
    w "Good. What you did to those papers could barely be called “grading” to begin with."
    s "In my defense, you never told me to grade them {i}correctly{/i}."
    w "I hope you choke and die on the next thing you eat."
    w "When is the soonest you can get here?"
    s "You're not going to feed me, are you? "
    w "Not at this rate."
    s "I’m sorry, what?"
    w "Cooking is difficult. I need help."
    s "From me?"
    w "From anyone. This is an absolute emergency."
    s "Why not ask your girlfriend for help?"
    w "Because I can’t. Are you coming or not?"
    s "..."

    "Well...it’s not like I have anything else to do."

    s "Normally, my [niece] is the one that cooks. I don’t really know-"
    w "Wonderful. I’ll see you in five minutes."
    s "But I don’t even know where you live yet."
    w "Figure it out, imbecile. I don’t have time for these pathetic games of yours."
    s "What does that-"

    play sound "phonebeep.wav"

    s "..."

    "I feel like people have been hanging up on me a lot lately."
    "I am very much not a fan of this."

    scene black
    with dissolve

    "I start walking in a random direction and hope that it’s the right one."
    "Thankfully, I {i}do{/i} receive a text from Wakana several minutes later with the address of her apartment complex and begin to make my way there..."
    "........."
    "......"
    "..."

    scene wakanatriestocook1
    with dissolve
    play music "normalday.mp3"

    s "..."
    s "Well, this is an exciting coincidence."

    "So, as it turns out, my favorite non-me teacher is the next door neighbor of my favorite waitress."
    "I knew the address looked familiar when Wakana sent it to me, but I didn’t really expect it to be {i}this{/i} familiar. "
    "If I had known she lived next to Kaori, I would have just asked {i}her{/i} to help Wakana cook."
    "If...Kaori even knows how to cook and isn’t just strictly a waitress."
    "Also, I’d need to be positive that Wakana wouldn’t be cooking anything with chicken."
    "Even though Kaori eats chicken."
    "You know what? I don’t even know why I’m thinking about this when Kaori isn’t the one I’m here to see."
    "I’ll just knock on Wakana’s door and-"

    play sound "static.mp3"
    scene wakanatriestocook2
    with flash
    stop sound
    stop music

    john "Greater love has no one than this: to lay down one’s life for one’s friends."
    john "You are my friends if you do what I command."
    john "I no longer call you servants, because a servant does not know his master’s business."
    john "Instead, I have called you friends, for everything that I learned from my Father I have made known to you."
    s "..."
    john "..."
    s "Hi, John."
    john "Sup."

    scene wakanatriestocook1
    play sound "knock.mp3"
    play music "justbehappy.mp3"

    "I knock on Wakana’s door and completely ignore my most recent exchange with a chicken."

    w "Come in right now. The door is unlocked."
    s "Can you be a little happier to see me at least?"
    w "No. Open the fucking door."

    scene black
    with dissolve

    "Why is it that I decided to walk across town to help a woman in a committed relationship cook despite having no idea how to do so myself?"
    "And why was John just standing outside underneath a light without Kaori?"
    "Why is tonight so weird by even the standards of my life?"

    scene wakanatriestocook3
    with dissolve

    w "Let’s do this."
    s "..."

    "Am I actually asleep right now?"
    "There’s no way any of this is actually happening, right?"

    s "I need an explanation."
    w "I need a fucking drink."
    s "What is happening right now?"

    scene wakanatriestocook4
    with dissolve

    w "Hah...it’s my anniversary with Osako and I want to do something nice for her since she’s always the one who does...everything."
    w "But I am entirely useless outside of[school] and hope that having someone else equally as useless will not only help in some way, but make me feel better about my shortcomings as a lover."
    s "Well, you called the right guy. If there is anyone who can make other people look better by simply being next to them, it’s me."

    scene wakanatriestocook5
    with dissolve

    w "Wonderful. Except you omitted the detail where {i}you{/i} were the one who called {i}me{/i}."
    w "As if I’d ever stoop so low as to contact you first. Please."
    s "Wakana...you’re not actually a tsundere, are you?"

    scene wakanatriestocook6
    with dissolve

    w "If by “tsundere” you mean “woman who would sooner copulate with a meat cleaver,” then yes. I believe I am."
    s "I feel like you would immensely regret that decision seconds in."
    w "They both seem like incredibly regrettable decisions. Now, help me."
    s "With what? What are you even trying to make?"

    scene wakanatriestocook7
    with dissolve

    w "I don’t know...soup?"
    s "In a frying pan?"
    w "...Cake?"
    s "...In a frying pan?"

    scene wakanatriestocook8
    with dissolve

    w "I told you I don’t normally do this, didn’t I?!"

    "I harness my inner Tsuneyo and tell Wakana everything I know about cooking soup."

    s "Okay, okay."
    s "First, you’re going to need a pot."

    scene wakanatriestocook9
    with dissolve

    w "Okay."
    w "Then what?"
    s "That’s all I’ve got."

    "I’m sorry, Tsuneyo."

    scene wakanatriestocook10
    with dissolve

    w "I was not designed for love."
    s "Same."
    s "Let’s just see what you have in your house and try to go from there."
    s "Worse comes to worst, Osako comes home and you can play up how bad you are at cooking and be all endearing about it or something."

    scene wakanatriestocook11
    with dissolve

    w "Me? Endearing?"
    w "She’s the cute one. I just lie on the bed and have her rub my feet all night."
    s "Why does she like you again?"

    if bonus == True:
        w "I don’t know. Foot fetish, maybe?"

    w "Doesn’t matter. Just...go look around for ingredients or something."
    s "I think you would know better where you keep all of the ingredients in this apartment."
    w "And you’d be greatly mistaken in doing so."

    scene wakanatriestocook12
    with fade

    "I walk past Wakana into the living room slash bedroom to begin my search."

    w "When I said search, I meant the fucking kitchen, you pathetic baboon."

    scene wakanatriestocook3
    with fade

    "I immediately return to Wakana after slightly invading her privacy."

    s "I figured I could cover the bedroom while you handled the kitchen."
    w "I {i}sleep{/i} in that room. And rather frequently, might I add."
    w "Now the entire thing needs to be professionally cleaned before I can even set foot inside."
    w "Thank you for making my night so much more difficult than it already was."
    s "I barely stepped inside."
    w "I’d need it professionally cleaned if you even {i}thought{/i} about stepping inside."
    w "Open some cabinets. Check the freezer. Do something. Anything."
    w "Osako should already be on her way home."
    s "And you waited this long? Are you insane?"

    scene wakanatriestocook8
    with hpunch

    w "Less talking, more scavenging! Go go go!"

    scene black
    with dissolve

    if bonus == True:
        "I do as Wakana says (Not because I believe it will increase my chances of having sex with her, but because she kind of scares me) and start frantically opening cabinets."
    else:
        "I do as Wakana says and start frantically opening cabinets."

    "My search ends with several things that I think might...probably work in soup: salt, chicken stock, and some weird packet with red stuff in it."
    "That last one is a shot in the dark, but it’s not like I have any idea what I’m doing and bringing only two things to the table sounds lame."

    w "Okay...I found some things."
    w "What do you have?"
    s "Salt, chicken stock, and some red stuff."
    w "Red? That sounds spicy. Osako doesn’t like spicy."
    s "Just trust me on this, Wakana."
    w "I..."
    w "Fuck it. Throw it in."

    "Wakana manages to find a pot and we each take turns dumping our hauls into it."
    "Among her ingredients is a full carrot, some instant noodles, half a bottle of mayonnaise, and several soy sauce packets from a take out restaurant."

    scene wakanatriestocook13
    with dissolve

    w "How do you think this will be?"
    s "Horrible."
    w "How hot do we make it? Is it possible to burn soup?"
    s "I say just turn it up as high as it goes if Osako is on her way home. That way, we can make sure it’s completely cooked by the time she gets here."
    w "Fine. But if the soup burns, I’m pouring it down your throat. Wasting food is unacceptable when there are children all over the world dying of starvation."
    s "Sucks to be them."

    scene wakanatriestocook14
    with dissolve

    w "It sucks to be anyone. Life is miserable and we’re all going to die."
    s "You know, food is nice and all, but what I think would make Osako {i}really{/i} happy is if you were able to not hate yourself for a day."
    w "I’m even worse at that than I am at cooking."
    s "I also think she would have appreciated it if you just bought her something instead."

    scene wakanatriestocook15
    with dissolve

    w "No. It has to be handmade."
    w "I can avoid cooking like the plague 364 days out of the year, but on this one, I need to at least {i}try.{/i}"
    w "If I can overcome this hurdle, Osako will see that I am not just a self-loathing blob of hatred with complete control over this apartment’s interior design."
    s "You mean all of that black and purple in the living room wasn’t Osako’s choice?"
    w "Excuse me for wanting to share my somber view of the world and its inhabitants with all who choose to enter my home."
    s "And how many people enter this home, exactly?"
    w "Osako. And now you, I suppose."
    w "While we wait for this to finish cooking, would you mind looking up the price of professional cleaners?"
    s "I’ll just ask Makoto to come here and do it if it’s really that much of an issue. She’ll be here in like five minutes if I ask her to be."
    w "Please don’t bother Miyamura with such a trivial task when she should be burying her nose in a textbook and exercising that prodigious brain."
    w "Also, is it just me, or is the soup turning solid?"
    s "Yeah, I noticed that as well."
    w "That’s not supposed to happen, is it?"
    s "Probably not."

    play sound "dooropen.mp3"
    scene wakanatriestocook16
    with dissolve
    stop music fadeout 5.0

    os "Wakana! Happy anniversary! Sorry I had to spend most of the day working but, I-"

    scene wakanatriestocook17
    with dissolve

    os "I..."
    os "What is he doing here?"
    s "Absolutely nothing."
    w "Hah...I suppose the jig is up."
    os "Jig?...What jig?"
    os "What are you talking about?"

    scene wakanatriestocook18
    with dissolve

    os "What’s going on? Why are you in our apartment?"
    os "I knew Wakana and you were friends, but since when are you two-"

    scene wakanatriestocook19
    with dissolve

    w "I’m sorry, Osako. I truly am."
    os "Sorry for what?...What happened?"

    scene wakanatriestocook20
    with dissolve

    w "I wanted to cook dinner for you to celebrate our anniversary, but I am inherently incapable of doing anything other than teaching."
    w "And so I called the only other person I’m in regular contact with to assist me, but lo and behold, he is inherently capable of even less."

    "Is Wakana actually covering for me right now? Or did she just forget that I’m the one who called her?"
    "Either way, I don’t bother refuting the thing about me being even less capable than her because this is probably something I should stay out of until it cools down a little."

    scene wakanatriestocook21
    with dissolve
    play music "thesleepingcity.mp3"

    os "Wakana...you..."
    os "You did that for me?"
    os "But you hate cooking. This is the first time you’ve even tried since last year, and that time you weren’t even able to figure out how to turn the stove on."
    w "I’m sorry, Osako. I’ll accept gracefully if you want to put me out of my misery."

    scene wakanatriestocook22
    with dissolve

    os "Nonononononono, it’s totally okay. I’m really happy you tried."
    os "I was just a little surprised to see you with someone else when I came home. That’s all."
    os "I...guess I just kind of figured it would be just us tonight."
    s "I was really only dropping by to help Wakana. I’ll leave now."

    scene wakanatriestocook23
    with dissolve

    os "Uhh...sorry if it seemed like I was accusing you of something."
    os "I...get jealous a little too easy, I guess."
    s "I’m sure I’d feel the same way in your shoes."
    s "Also, do you have any idea what that packet of red stuff in the pantry was? Because the soup very clearly came out wrong and I would like to confirm that it was Wakana's fault."

    scene wakanatriestocook24
    with dissolve

    os "Packet of...red stuff?"
    s "Yeah. It was between a packet of blue stuff and a packet of yellow stuff."
    os "Blue stuff...and...yellow-"

    scene wakanatriestocook25
    with dissolve

    os "Jell-O?..."
    w "Oh. You like Jell-O."
    w "Perhaps dinner isn’t ruined after all."

    scene wakanatriestocook26
    with dissolve

    os "How about I just...run to the convenience store really quick and grab some real ingredients for the two of us to make dinner with?"
    os "I can show you how to cook if you really do want to learn for next year."
    w "If you’d be so kind as to do that..."
    os "Of course. Anything for you."
    s "And on that note, I’ll be leaving."
    s "But I’d like to part with saying happy anniversary and-"

    scene wakanatriestocook27
    with dissolve

    os "Actually, why don’t you tag along with me if you’re on your way out?"
    os "There’s something I kind of want to talk to you about anyway."
    s "Please don’t quit the maid cafe just because you got to keep your job at the dojo."
    os "I’m not allowed to quit the maid cafe. Wakana would kill me."
    w "Humanely. But yes."
    s "Are you sure? It seems like I’ve already kind of gotten in the way of things by turning your soup into a sugary dessert."
    os "Yeah, I’m sure. It won’t take long anyway since it’s only right down the road."

    scene wakanatriestocook28
    with dissolve

    os "Babe, could I ask you to maybe clean out the pot for me while I’m gone?"
    w "You want me to throw away the dinner I worked so hard on?"
    os "I...uhh..."
    os "I mean, I guess we could {i}try{/i} eating it if that’s-"
    w "I’m joking."
    w "Of course I’ll clean out the pot for you."
    w "Hurry home, though."

    if bonus == True:
        w "I bought a new rope that should be a little easier on-"
    else:
        w "I learned one of the Fortnite dances to impress you and-"

    scene wakanatriestocook29
    with hpunch

    os "JUST...T-TELL ME ABOUT IT LATER!"
    w "So cute. Please do hurry back."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ wakana_love += 1
    $ wakanadate5 = True

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"

    jump osakodate1

label wakanadate15:
    play sound "phonebeep.wav"

    "I tap on Wakana’s name in my phone and wait for her to answer-"
    "Because, despite everything about her appearance screaming “I am going to stay in bed for the rest of forever,” she’s one of the only people I know who seems to always be doing something around this time."
    "So, based on prior experience, it’s probably safe to assume she’s either getting extra work done at school or...watching over the archery club (Again, at school.)"
    "You know, she should probably just move closer to the school if she’s going to be spending practically all of her time there."

    play sound "phonebeep.wav"
    play music "wewereangels.mp3"

    w "Good morning, Arakawa. What do you want?"
    s "Just wanted to see what my favorite goth was up to."
    w "If that section of your rolodex is comprised of more than just one person, please forward me their contact details. Talking to you and Imani is tiring. I need more people interested in incense."
    s "There’s always Nodoka."
    w "I said incense, not {i}incest.{/i}"
    s "Sorry. Only one of those words is in my dictionary."
    w "Then I believe it may be time for an upgrade. Fortunately for you, I’m currently surrounded by around a hundred of them. "
    w "I’ll make sure to grab one on the way out so your wealth of knowledge can expand beyond the reach of whatever it is you do to your niece in your spare time."
    s "You too? I feel like I can’t talk to anyone nowadays without them suggesting something going on between Ami and me."
    w "And whose fault is that, Arakawa? "
    s "Hers. Also, why not try spending a little time away from school every once in a while?"
    s "I get that you’re an intellectual and that libraries are like candy stores for you, but it’s still way too early in the morning to be going over there if you don’t {i}have{/i} to."
    w "Are you done?"
    s "I think so."
    w "Good. Then I guess this is the part where I tell you {i}I am not at school, you incorrigible half-wit.{/i} I’m at the {i}public{/i} library. And you just lost your chance to obtain a new dictionary for free. I hope you’re happy."
    s "What are you doing at the library?"
    w "Fucking reading, Arakawa. Do you even understand how libraries work?"
    s "But why {i}there?{/i} It’s nowhere near your apartment."
    w "Hah...I’m doing research. And quite disheartened by the fact that you now know I am in a library and you refuse to hang up the phone."
    s "You haven’t hung up either. I just want to know-"
    w "If there’s something you want to know, you know where to find me. I don’t have time to “shoot the breeze” with you like this. I have work to do."
    s "Waka-"

    play sound "phonebeep.wav"

    s "...na."

    scene black
    with dissolve2

    "Wakana hangs up the phone and I...guess I’m heading over to the public library to continue the conversation."
    "Not that I expect it to be exciting when she’s apparently just “researching” things, but at least deciding on this path for the day is easier than trying to uncover another one."
    "I throw on my clothes and head over to the bus stop, patting myself on the back for deciding to visit a real adult woman."
    "A real adult woman with no inclination to have sex with me, yes. But a real adult woman nonetheless."

    scene wakanalibrary1
    with dissolve2

    "It takes me a few minutes to find Wakana once I get to the library, but I manage to spot her during my second lap around the place in what should have {i}probably{/i} been the first section I checked."
    "I make my way through a narrow aisle walled by the names of dead poets and wind up in front of one still clinging to life by a few black threads dangling off the fingers of her gloves."

    w "Interesting. I didn’t think you were actually going to show up."
    s "We weren’t done “shooting the breeze” yet."
    w "Unfortunately for you, I don’t have time to do much “shooting” at all. This is proving to be a bit more difficult than I expected."
    s "What are you doing exactly? More...research or whatever?"

    scene wakanalibrary2
    with dissolve

    w "That is correct. Though, I suppose it’s less general research and more...brushing up on things I have forgotten."
    s "Care to explain?"

    scene wakanalibrary3
    with dissolve

    w "Not really, no."
    s "Wakana-"
    w "Fine. If you {i}must{/i} know, I have taken it upon myself to take on {i}even more{/i} work- as the work I had already was apparently not enough for my masochistic brain."
    s "I thought Osako was the masochist?"
    w "Physically, yes. But the amount of pain I insist on putting myself through makes me feel as if I am some sort of mental masochist."
    s "And this additional work is?"

    scene wakanalibrary4
    with dissolve

    w "I thought it might be fun to start an annual poetry contest for the girls at our school...as several of them have expressed interest in that sort of thing."
    w "But, me being me, simply agreeing to judge their work was not enough. "
    w "And so I find myself here, attempting to decipher several of the submitted works while brushing up on the fundamentals of what I’m trusted to be educating our students on."
    w "I’d say something along the lines of, “The life of a teacher, right?” But I know that you wouldn’t be able to relate and I don’t want to confuse that tiny, pea-shaped brain of yours."
    s "Interesting. I guess if anyone is going to judge something like that, it should be you."

    scene wakanalibrary5
    with dissolve

    w "I’d say you’re just as qualified, but I suppose actually {i}caring{/i} about the assignment is important too."
    s "Is there some sort of theme everyone has to use?"

    scene wakanalibrary6
    with dissolve

    w "Why? Are you thinking of entering?"
    s "Absolutely not. Just a little curious, that’s all."
    w "Worried you’ll lose to a bunch of teenagers? "
    s "You got me. That’s exactly it."

    scene wakanalibrary7
    with dissolve

    w "The theme is Kumon-mi. Though, I’d implore you to use a pseudonym if you actually intend to submit anything."
    w "How that would work if you actually {i}won,{/i} I have no clue. But I suppose that’s a bridge we don’t have to worry about crossing just yet."
    s "Would you actually let me enter? Doesn’t that seem a little unfair?"
    w "Perhaps. But I am rather curious about what sort of poem {i}you’d{/i} be able to write, Arakawa. "
    s "I doubt it would be anything good. There’s not much I really have to say about Kumon-mi other than it’s been really fucking hot lately."
    w "Several of your students seem to have quite a bit to say, on the other hand. I’ve gotten more submissions from your class than my own, and I even offered extra credit for writing something."
    s "From my class? Who?"

    scene wakanalibrary6
    with dissolve

    w "Would you like to read them together? You can...help me {i}judge{/i} them."
    s "The way you said “judge” there makes me worry they aren’t going to be any good."
    w "I wouldn’t worry too much. But I suppose I’ll let you get the final say. "

    scene black
    with dissolve2

    "Wakana bends down and removes a notebook from a large, purple bag. "
    "For anyone else, I’d use this opportunity to try and look up their skirt, but...yeah. "
    "Not really possible when the girl I’m with insists on wearing a dress that reaches the floor on a day where you could cook an {b}EGG{/b} by just cracking it open on the pavement."

    play sound "static.mp3"
    scene tree3 with flash
    scene wakanalibrary8 with flash
    stop sound

    w "So far, I’ve received submissions from a total of four of your girls. Though I believe there may be several others still working on theirs."
    w "It’s unfortunate that Miyamura won’t be participating. I feel like she’d be good at this. "
    s "She seems like more of an intellectual than an artist to me."
    w "Fair point. What we do have so far isn’t all that bad, however. Well, with the exception of one poem that I believe was created just to irritate me."
    s "Why? Does it talk about how life is awesome and totally worth living?"
    w "No. But it does mention an ungodly desire to strip the clothes from my body and “taste every inch of me,” but it’s disguised as a poem about dragonfruit. "
    w "I’d actually be quite impressed if I wasn’t so appalled by the subject matter- which has absolutely {i}nothing{/i} to do with Kumon-mi, by the way."
    s "Nodoka?"
    w "Who else would write a poem about tasting every inch of me?"
    s "Honestly? Probably a few more of my girls."

    scene wakanalibrary9
    with dissolve

    w "Really? Huh."
    w "And here I was beginning to think I had already lost my girlish charm."
    s "I’m not sure if your “girlish charm” is what they admire."

    scene wakanalibrary8
    with dissolve

    w "Regardless, that was Nagasawa’s disqualified submission. But the three that remain are much better. "
    w "This one comes from...Fukuyama."
    w "{i}The town that I grew up in;\nWhere I still grow today.{/i}"
    w "{i}Where skies are blue and grass is green and everything’s okay.{/i}"
    w "{i}The town where all my friends live;\nAnd where I fell in love.{/i}"
    w "{i}It may not be exciting, but it’s the only town I love.{/i}"
    s "She rhymed “love” with “love.”"
    w "She rhymed “love” with “love...”"
    w "And while that’s not unheard of and {i}could{/i} be intentional, I’m almost certain it was an accident and that she’s going to realize her mistake and try to correct it."
    w "Unfortunately, the rules state that as soon as something is submitted, you can’t get it back."
    s "Who’s next? There are two more, right?"
    w "Up next is...oh. The one I tried to pawn off on you only to find that she’s been “in love” with you since she was a child- Nakayama. How fun."
    w "{i}No blindeyes bloom on paths I walk, but I found a shepherd’s purse;{/i}"
    w "{i}With pockets full of buttercups, I returned it to the earth.{/i}"
    w "{i}Now in its place, a pasture- cross the homes of hyacinth.{/i}"
    w "{i}Near a suckling clover fountain and its bitter orange drip.{/i}"
    s "That one doesn’t seem to have anything to do with Kumon-mi either."

    scene wakanalibrary9
    with dissolve

    w "Ah, but that’s where you’re wrong."
    w "Nakayama comes from the old district, doesn’t she?"
    s "She does, but I don’t really understand how that’s relevant here."
    w "It’s a poem about the Hamori River...and all of the flowers that bloom there."
    w "I needed to do a little research to confirm, but I thought I understood it after my first read as Osako and I have walked along that path before. It’s beautiful."

    scene wakanalibrary10
    with dissolve

    w "Or {i}was.{/i} I hear that area’s all but abandoned now. Shame."
    w "It used to be so lively there."
    s "Huh..."
    s "I didn’t realize Noriko could write like that."

    scene wakanalibrary11
    with dissolve

    w "I agree. Her submission is probably my favorite of what I’ve received so far. But the biggest surprise of all is this next one."
    w "From Ami Arakawa..."
    w "{i}Summer. Winter. Paradox. No autumn, nor a spring;{/i}"
    w "{i}At night, I watch the sakura peel themselves off thick, red strings.{/i}"
    w "{i}Why can I see what isn’t there? Why can’t I feel the sting?{/i}"
    w "{i}Of the town that took the world away and the evil song it sings.{/i}"
    s "..."
    w "I don’t believe I’ve grasped the full meaning of the poem yet, but this...longing for pain and how it ties in with our missing seasons..."
    w "It reminds me of another poet I used to follow when I was younger."
    w "One that, if what I’ve heard is true...was also born and raised here."
    s "..."
    w "It’s impossible to tell for sure, though, as she always used a pseudonym."
    w "The girl who cannot breathe..."
    w "Infamous for her self-destructive thoughts on what it means to {i}be{/i} and the use of themes that most others would-"

    stop music
    play sound "thump.mp3"
    scene wakanalibrary12
    with hpunch

    "{i}Uh-oh!{/i}"
    "{i}It looks like you might have remembered something!{/i}"
    "{i}Remembering things is bad! Remember to remember that!{/i}"
    "{i}If you remember too much, you won’t be able to put your meat stick inside of tight meat holes anymore.{/i}"
    "{i}And that’s the point! Remember? Remember? Remember?{/i}"
    "{i}This is all just a game! It’s all part of a game!{/i}"
    "{i}It’s not real at all! Nothing is real! Nothing is real!{/i}"

    scene black

    "but if that’s true, why is everything so much bigger than you?"

    play sound "static.mp3"
    scene wakanalibrary12 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    w "Ara...kawa?..."
    s "Let’s get out of here."
    w "What?..."
    s "You. Me. Let’s leave."
    s "Do something else."
    s "Something better than this."
    s "Bigger."
    s "Let’s leave."
    w "Arakawa..."
    w "Your eyes..."
    s "Don’t look at me."

    scene wakanalibrary13
    with dissolve

    w "You’re making that quite hard with how close you’ve decided to come all of a sudden..."
    w "I’m flattered, really. Though, I’m not quite sure this is the type of relationship where you’re allowed to pin me against the wall and tell me to “get out of here” with you."
    w "Let alone in broad daylight...in the middle of a public library."

    scene wakanalibrary14
    with dissolve

    libp "Um...Miss, are you okay? Do you need me to...call for help?"
    w "Just a minor lover’s quarrel. Apologies for the commotion."
    libp "Oh...Okay..."
    libp "Well...uhh...I guess let me know if you need anything?..."
    w "Understood. Thank you very much."
    s "..."

    scene wakanalibrary15
    with dissolve

    w "..."
    s "..."
    w "..."
    s "..."
    w "..."
    s "..."
    w "If you have something to say, say it. This isn’t exactly a comfortable position for me."
    s "I can make it more comfortable if you want."
    w "Oh?"
    w "Is that what we’d do if I left with you?"
    s "..."
    w "Do you want to have sex with me, Arakawa?"
    w "Is {i}that{/i} why you’re cornering me like this?"
    s "..."
    w "Or is there perhaps another reason?"
    w "One you’re not telling me about, maybe?"
    s "You-"
    w "If you expect me to be afraid of you, it’s not going to happen. You look fucking pathetic right now."
    s "Don’t..."
    s "Don’t talk..."
    s "About..."
    s "..."
    w "Don’t talk about what? I don’t know what to do if-"

    scene wakanalibrary16
    with dissolve

    w "Wait..."
    w "Arakawa, what was the last thing I said before you decided to be a big, scary man and pin me to the wall?"
    s "..."
    w "Tell me."
    s "..."
    w "You can’t...can you?"
    w "You know-"
    s "I don’t know anything."
    w "Your eyes say otherwise."
    s "I told you to stop looking at them."

    scene wakanalibrary17
    with dissolve

    w "Fine. But if you seize this opportunity to stick your tongue down my throat, I have a hard time seeing how this friendship is going to work out."
    w "You can stay like this for as long as you need to...until you start to collect yourself, but..."

    scene wakanalibrary18
    with dissolve

    w "Just watch your fucking step, okay?"
    w "This little...{i}show{/i} you’re putting on right now? Not a fan."
    w "I doubt my {i}girlfriend{/i} would be much of a fan either."
    s "..."
    w "..."
    s "..."
    w "..."
    s "..."
    w "..."
    w "Arakawa..."
    s "What?..."

    scene wakanalibrary19
    with dissolve

    w "Just thought I’d say..."
    w "You’re a lot uglier up close."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "{i}The rest of the day disappears once you let her go...along with the three poems and the words uttered thereafter.{/i}"
    "{i}But you know they’re still in there somewhere.{/i}"
    "{i}Hiding somewhere you can’t see.{/i}"
    "{i}Waiting for the chance to suffocate you.{/i}"
    "{b}{i}You try to masturbate when you get into bed, but it doesn’t get hard.{/i}{/b}"

    $ renpy.end_replay()
    $ wakanadate15 = True

    "{i}Wakana’s affection does not rise.{/i}"
    "{i}But she saw who you really are today.{/i}"

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

label wakanaspecial15:
    if _in_replay:
        play music "10c.mp3"

    scene yuritime1
    with fade

    os "Hey, everybody! Sorry I’m late!"
    w "Oh, thank god."
    os "It’s been crazy busy at work lately and I wound up having to stay after closing so we could-"

    scene yuritime2
    with dissolve

    os "Mmphpphphphfff?!"
    ima "Big oof."
    ima "Sucks to be you, Senpai. Thought we had her for a second. Guess it’s good that no homes were wrecked during tonight’s festivities, though."
    s "Me too. I’m pretty sure Osako could kill me just by looking at me if she really wanted to."
    ri "Ahh..."
    ima "Shh, Rika. Don’t cry. It’s okay."
    ri "It’s coming again! I can’t hold back!"
    ima "And...probably don’t say anything that’ll get our male companion here excited either."
    s "I’ve seen two lesbian couples make out in less than five minutes. It’s a little too late for that."
    ima "{i}Technically,{/i} I’m bisexual. And Rika and I aren’t a couple. "
    s "Shut up, Imani. You’re ruining the moment."

    os "Mmf...mmnch...Wa...kana?..."
    os "Everyone is...mnch...watching..."

    scene yuritime3
    with dissolve

    w "Apologies, my sweet. I just couldn’t help myself anymore."
    os "You don’t...have to apologize...I just...you know...it’s a little...embarrassing? And...sudden?"
    w "Can it really be called sudden if you’ve kept me waiting all night?"
    os "Uhh...umm..."

    scene yuritime4
    with fade

    ima "Okay, so...either those “adverse effects” that Wakana was talking about {i}really{/i} get to her...or she’s just mad turned on from the two of us fulfilling her dare."
    ri "I need another drink."

    scene yuritime5
    with dissolve

    ima "Rika, your beer is full."
    ri "Not full enough to make me {i}forget.{/i}"

    scene yuritime4
    with dissolve

    ima "Is it weird, Senpai? You know, being the only person who {i}hasn’t{/i} kissed someone tonight?"
    s "Yes. But the night isn’t over yet."
    ima "Holdin’ out hope that those two might let you join in on the action?"
    s "Right now, I’m just trying to enjoy the show. And your commentary isn’t helping."

    scene yuritime6
    with fade

    os "Mmf........mlm.......mm~"
    ri "You know, the fact that they’re doing this without even being dared is very offensive and not how this game is supposed to work. I would like a refund, please."
    ima "I think Wakana just needs to get the horny out of her system. Better to do that with her girlfriend than some random guy off the street."
    ri "Woah, you found him on the street? What a crazy coincidence that he wound up being a teacher too."
    ima "That aside, can we talk about how Osako just radiates bottom energy for a second?"
    ima "You’d think that being a fucking martial arts god or whatever that she might feel a little more...I don’t know, powerful when it comes to this stuff?"
    s "I think things work well this way and I wouldn’t change their dynamic at all."
    ima "Yeah, but you’re pitching a tent the size of Fujisan right now. You’d be happy with anything."
    os "Wakana...mmf...Wakana~"

    scene yuritime7
    with dissolve

    os "I love you..."
    w "And I you. "
    os "What’s...gotten into you all of a sudden?..."
    w "It’s hard to say, my kitten."
    w "But perhaps I could show you?"
    os "Show...me?..."
    os "But...we’re-"

    scene yuritime8
    with dissolve

    w "I know you’ve all been anxiously awaiting her arrival, but I’m afraid that I will be whisking this one away for a short while. "
    w "Please continue on with your game without paying much mind to what the two of us are doing."
    w "Oh...and best of luck, Arakawa. "
    w "I can only imagine how hard it must be for you right now."

    scene yuritime9
    with dissolve

    w "Come, Osako. We’ll have more {i}privacy{/i} in the restroom."
    os "Yes...ma’am..."

    scene yuritime10
    with fade

    ri "Why can’t it be me having hot, kinky bathroom sex with my partner?! I like hot, kinky bathroom sex too!"
    ima "You doing okay, Senpai? Looks like the cable went out without you ever getting to see the ending of your show. "
    ima "Well, assuming you don’t follow the two of them into the bathroom. Which I wouldn’t really blame you for at this point."
    s "I think I’m {i}slightly{/i} above doing something like that, Imani. Just slightly, though."

    scene yuritime11
    with dissolve

    ima "Really? Cause I’ve been wrong before, but I'm gonna agree with Rika. I felt some mad tension right there. "
    s "Between those two? Yes. Between anyone else, I don’t think so."
    ima "Dude, did you see the way she smirked at you? Because I’ll be damned if that wasn’t a “Hahah, look what you can’t have” smirk."
    ima "And if there's anything I know about “Hahah, look what you can’t have” smirks, it's that you can {i}totally{/i} have whatever it is you want."
    s "She’s just fucking with me like she always does. There’s no way she’d actually go through with something like that."
    ima "Listen, man. I like Osako, so I’m not going to say something like “You should have sex with her girlfriend and ruin her life.”"
    ima "But straight up, I’m pretty sure you could have sex with her girlfriend and ruin her life."
    ri "Sex ruins everyone’s lives and no one should ever have it because it only ends in pain and misery and trips to a bar with a bunch of people you’ve never seen before and don’t fit in with."

    scene yuritime12
    with dissolve

    ima "Hey, don’t say that! I think you fit in just fine! Even with the whole “ruining my self-esteem” part since Senpai does that to me every day."
    ri "I don’t. I never fit in with young people anymore."
    ri "This is exactly why my daughter says I embarrass her. Because I’m stupid and dumb and embarrassing and stupid."
    ima "Young people?..."
    ima "Daughter?..."
    ima "How..."
    ima "How old are you, Rika?..."
    ri "I’m 42."

    scene yuritime13
    with dissolve

    ima "You’re {i}what?!{/i}"
    s "Honestly, you look younger than 30. Good for you."
    ima "I made out with a 42 year old?!"
    ima "You could be my mom!"
    ri "Yeah, but then I’d just embarrass {i}you{/i} too."
    s "I think you’re officially the oldest person I know."
    ri "Yeah. Rub it in, why don’t you?"
    ima "No wonder you gave me a 6/10! You’ve got decades worth of experience under your belt and I’m just a mere caterpillar in the world of girl on girl contact!"
    ri "I wish I was with the other two in the bathroom right now. I bet no one is making {i}them{/i} feel like a fucking loser."

    scene black
    with dissolve2

    "{i}Meanwhile...in the bathroom...{/i}"
    "........."
    "......"
    "..."

    scene yuritime14
    with dissolve2

    os "Mmnch...ahm...mmm!"
    os "Mmm........mmm...........mmm!~"

    scene yuritime15
    with dissolve

    w "I’ll never tire of those adorable, little noises you make."
    os "More..."
    os "Kiss me...more..."
    w "You’re lucky I kissed you at all with how long you kept me waiting tonight."
    w "You know what happens when you keep me waiting, don’t you?"
    os "I’m sorry, Wakana...I’ve been a bad girl...I’ve been so bad..."
    w "And what happens when you’re bad, my sweet?"
    os "You...get to punish me..."
    w "That’s right...I get to punish you..."
    w "I get to do {i}whatever I want{/i} to you..."
    w "But fortunately for you, I seem to have left my handcuffs at home..."
    os "Wakana...I want more..."
    w "I bet you do, little girl."
    w "And as your master...it’s up to me to give you more...so you don’t go {i}crazy...{/i}"
    w "But what to give you, I wonder..."

    scene yuritime16
    with dissolve

    os "I’m...unworthy...of anything you do to me..."
    os "I’m already going crazy...just thinking about it..."
    w "You know what, my kitten?"
    w "What if I let you off with just a warning this time?"
    w "I {i}did{/i} miss you, after all..."
    w "And your tardiness was unintentional..."
    w "But, then again..."
    w "I do like it when you squirm."
    os "Wakana..."

    scene yuritime17
    with dissolve

    w "Call me “Master,” you little bitch."
    os "Master...I can’t...stand this..."
    os "I want you...I want you so bad..."
    w "Is that so?"
    os "I love you...I love you so much..."
    w "{i}Show me{/i} how much, kitten..."
    os "How?...What can I do?..."
    w "You can take your fucking pants off before I’m forced to {i}rip{/i} them off myself."
    os "Yes...Master..."

    scene yuritime18
    with dissolve2

    w "There you go...Doesn’t that feel much better?"
    os "Much...better...Master..."
    w "With how damp you’ve gotten, you’d think that {i}I{/i} was the one keeping {i}you{/i} waiting."
    os "I should be the one...pleasing you...I don’t...deserve this..."
    w "I’m a wonderful owner, aren’t I? There aren’t many of us who’d help alleviate some of the tension when our pets go into heat."
    os "Oh God.......it’s so good.......It’s.......so good!"
    w "Oh...What’s this?..."
    w "I think I may be beginning to tear a hole in your precious underwear, my kitten. "
    w "That would be the third pair just this month."
    w "At this rate, we may even wear down everything you own. "
    w "Should we maybe stop putting ourselves in situations like this? Or will you continue to be disobedient and needy instead?"
    os "I’ll do...anything you want...just...please don’t stop...please don’t stop..."
    w "You say that now, but what about the next time you don’t show up when I want you to?"
    w "The little black vibrator in my bedside drawer has been getting quite the extra workout lately thanks to you."

    scene yuritime19
    with dissolve

    os "It should...be me! I should be the one...satisfying you!"
    w "Are you jealous of a toy now? Pathetic."
    os "I...hate it! I...want to be...the only one for you!"
    w "Could you even please me as much as {i}it{/i} does? Or will I have to tie you up and make you watch again?"
    os "I don’t...want to watch...I want to...satisfy you...Wakana!"
    w "Oh my. You forgot my name {i}again.{/i}"
    w "Now, I’m angry..."
    os "I'm sorry! I-"
    w "Bra, up. Now."

    scene yuritime20
    with dissolve2

    os "Ahh! M...Master!"
    w "That’s right...hold those little panties back so we don’t ruin them..."
    w "And stop moving your fucking hips. It makes you look weak."
    os "I can’t...help it! It’s so...good!"
    w "Do it again and I’ll stop."
    os "M...Master!"
    w "I mean it. I’ll walk right out of here without ever letting you finish. And you know damn well you’re not allowed to touch {i}yourself,{/i} so you’d be left rather hopeless, wouldn't you?"
    os "I’ll stop! I’ll stop moving!"
    w "Look at you...becoming more and more obedient with every passing day."
    w "It’s only a matter of time before I can start calling you a slave, isn’t it?"
    os "You can call me anything you want! I’m yours! Only yours! No one else...could ever...make me feel like this!"
    w "Stop squeezing my fingers like that. You’re going to break them."
    os "But...I...I..."
    w "You what?"
    w "Don’t tell me you’re thinking of cumming already? We’ve barely gotten started."
    os "I...can’t help it!"
    w "Look at you...pathetic as ever. All it takes to make that tough girl facade crumble is a tiny flick of the clit and a finger or two inside of your pussy. What a joke."
    os "Hah...hah! Fuck!"
    w "Ah-ah-ah. Language. I have no use for a pet that doesn’t know how to keep its mouth shut."

    scene yuritime21
    with dissolve

    os "Ngh! "
    w "Ha. You really {i}are{/i} about to cum, aren’t you? And in a public bathroom, no less. Shameful. Despicable."
    os "Y...You were...the one who..."
    w "Shut your fucking mouth."

    scene yuritime22
    with fade

    w "Mm~"
    os "Hah! Oh...fuck!"
    w "Mm...mm~"
    w "See...my kitten?...You can fit a third finger no problem...There was no need to...mm...squeeze so hard before..."
    os "W...M...Master..."
    os "I don’t...deserve this..."

    scene yuritime23
    with dissolve

    w "Ahm~"
    os "Hyah! Don’t...bite it like that! "
    w "Mmf...mmm...but it looks so delicious..."
    w "Tastes so delicious..."
    os "Hah! Oh god...Wakana! I...seriously...can’t anymore!"
    w "Mmf...mm...then what are you waiting for?..."
    w "I don’t have all day..."
    os "Oh...fuck...Oh god...how are you...so good at this?..."

    scene yuritime24
    with dissolve

    w "I said it earlier...I like watching you squirm..."
    w "It motivates me..."
    w "Now...mmf...cum for me, my kitten..."
    w "That is an order..."
    os "Hah.........ahh........"

    scene black
    with dissolve2

    os "........AAAAAAAAAAAAAAAAAAAAAAAHHHHHH!!!!!!!!"

    "........."
    "......"
    "..."

    scene yuritime25
    with dissolve2

    w "{i}Ahem...{/i}"
    w "I have returned. Or I suppose I should say {i}we{/i} have returned."
    ima "You sure about that? Osako doesn’t really look...{i}all there{/i} to me."
    os "Ah...........hah.........."

    scene yuritime26
    with dissolve

    w "Hm."
    w "I wonder why that could be?"
    w "No matter, I’m sure she’ll return to normal in no time at all."

    scene yuritime27
    with dissolve

    w "Anyway, did the two of you watch my drink while I was gone? I’m worried that Arakawa may have slipped something into it."
    ima "Uhh...which one? You have five cans here and-"
    w "Oh well. I suppose I’ll just have to buy five more."
    w "The next round is on me. Consider it an apology for the incredibly rude and inappropriate display I put on just moments ago."
    s "I think we’re all in agreement when we say that it wasn’t rude at all and that we wish you’d do that more often."
    ri "Do you see that face, Imani? {i}That’s{/i} the kind of face you should be shooting for when you make out with somebody. Do you think that screams 6/10?"
    ima "That’s it! I’m starting a formal vote to remove Rika from the group! All in favor, say aye! Aye!"
    ri "Ay- wait, no! Don’t do things like that! I have this weird compulsion to just always go along with stuff and that includes chiming in on every group vote."

    scene yuritime28
    with dissolve

    w "Osako, I’m sorry to tear you from the afterglow, but it would both make me happy {i}and{/i} help in dismantling Imani’s sense of pride if you would rate my kissing on a scale of one to ten right now."
    ima "Oh, come on! You don’t have to rub it in!"
    os "Kissing..."
    os "A million..."

    scene yuritime29
    with dissolve

    w "Excellent. That makes me roughly 166,665 times better than Imani. Which is also coincidentally how much better I am at teaching than she is."
    ima "Starting a new vote! Anyone who wants to remove Wakana from the group, say aye! Aye! "
    ri "Aye!"
    ri "Wait, fuck!"

    scene black
    with dissolve2

    "Wakana and Osako sit down at the table, but it’s more like only one of them is actually there."
    "And while she agreed earlier that she’d be nice to me for the rest of the night, Wakana doesn’t really...pay any attention to me at all after she returns from the bathroom."
    "Which is fine, I guess. It’s not like I {i}expected{/i} her to when she has someone better and...less male to focus on than me. "
    "Plus, just ignoring me isn’t really being {i}mean{/i} either.  I just..."
    "I don’t know."
    "It feels different all of a sudden."
    "And it distracts me for the rest of the night."

    $ renpy.end_replay()
    $ wakanaspecial15 = True
    $ wakana_love += 1
    $ imani_love += 1
    stop music fadeout 10.0

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label wakanadate25p1:
    scene wakanaastrip1
    with dissolve2
    play music "phantomthief.mp3"

    "As I sit behind a desk I feel myself spending less and less time with as life ticks on, I take a moment to understand and appreciate just how far I’ve come and what I’ve accomplished so far."
    "I’ve witnessed the end of days."

    play sound "static.mp3"
    scene reset4 with flash
    scene wakanaastrip1 with flash
    stop sound

    "I’ve learned my name and begun the process of accepting who I am."

    play sound "static.mp3"
    scene memorylane25 with flash
    scene wakanaastrip1 with flash
    stop sound

    "I’ve even fallen in love."

    if amifingered == True:
        play sound "static.mp3"
        scene makotobeach with flash
        scene amiani13 with flash
        scene endofthefourth27 with flash
        scene nikilovesyou7 with flash
        scene fireflies16 with flash
        scene wakanaastrip1 with flash
        stop sound

    else:
        play sound "static.mp3"
        scene makotobeach with flash
        scene endofthefourth27 with flash
        scene nikilovesyou7 with flash
        scene fireflies16 with flash
        scene wakanaastrip1 with flash
        stop sound

    "And through it all, of course I’ve had my fair share of problems."
    "In fact, there have been {i}so many{/i} problems that it would take me a whole cycle just to recount them."
    "But I’ve not been without support."
    "Throughout this entire journey, there’s been someone right beside me the whole time."
    "Someone who has kept me grounded, and knows me better than almost anyone."
    "That someone is this desk."

    s "I love you, desk. "
    desk "(Is a desk)"

    "Unfortunately, some things in life just aren’t fair. And the things we want to speak to the most completely ignore us."

    play sound "knock.mp3"

    s "..."

    "But that’s okay. Because sometimes, other things or creatures show up to keep us company."

    s "Come in."

    scene wakanaastrip2
    with dissolve
    play sound "dooropen.mp3"

    w "Did I just hear you...tell your desk that you {i}love{/i} it?"

    "And sometimes they call you out on things you’d really wish they didn’t hear and weren’t actually able to call you out on."

    s "No."
    w "Arakawa."
    s "What?"
    w "Do you want to fuck your desk?"
    s "I don’t want to fuck my desk, Wakana. I was just recalling how long it’s been with me and how much we’ve been through together."
    w "Oh my god. You want to fuck your desk."
    s "Wakana, why are you here?"

    scene wakanaastrip3
    with dissolve

    w "I came to ask if you’d like to accompany me out to the city if you didn’t have any plans tonight. But seeing as you do and they involve fucking your desk, I will just wait until tomorrow."
    s "You know, this is exactly why I never speak when no one’s around. Someone always shows up exactly when they’re not supposed to."
    w "Yes, I apologize for interrupting your...{i}confession.{/i} I will take my leave now."
    s "Wait, no. You don’t have to go."
    w "I’m aware. I wasn’t actually planning on leaving. I just wanted to make it seem as if I was so you’d have less of a desire to fuck your desk and-"
    s "Wakana, why are you inviting me to the city? Are Osako and Imani busy?"

    scene wakanaastrip4
    with dissolve

    w "No. I’d just rather go with you instead."
    s "Right. And what’s the catch, exactly?"
    w "Can the catch be that you don’t slam me up against another wall and act all tough? That wasn’t particularly enjoyable for me last time. I’m sure it’s a precious memory for you, though."
    s "I promise not to slam you up against anything. But I still don’t get why it has to be {i}me{/i} instead of one of them."
    w "You really want to fuck that desk, don’t you?"
    s "I don’t want to fuck the desk, Wakana."
    w "Arakawa, despite me not owing you an explanation for literally anything ever, I’m asking you to come with me because you are my friend and I value you as a person."
    s "Do you value me as a coworker as well?"
    w "Absolutely fucking not. You should have been fired years ago."
    s "This is going to be a really fun trip, isn’t it?"
    w "We shall see when we arrive at our destination."
    s "And that destination is?"

    scene black
    with dissolve2

    w "A secret. Now, come. Unless you need a moment to say goodbye to the desk."
    s "Please don’t make this a thing."
    w "It is far too late for that, I’m afraid."

    stop music fadeout 20.0

    "Despite having thirty minutes left of my “counseling” session, I decide to leave early so Wakana can reap whatever benefits of our {i}friendship{/i} she’s after today."
    "Unfortunately for me, I highly doubt one of those benefits will be my penis. So I will remain blissfully ignorant for the next hour or so as she drags me to an unknown location to {i}not{/i} have sex with me."
    "........."
    "......"
    play sound "trainbell.mp3"
    "..."

    scene noonsky
    with dissolve2

    "It becomes evident that by “the city,” Wakana literally meant {i}the city{/i} as we get off the train at the first stop in the urban district."
    "With most people getting out of work around this time, navigating through the station becomes a chore."
    "But, as if she’s an expert when it comes to this exact pathway, Wakana quickly guides me to the nearest exit and the two of us make our way out into the street."
    "It’s nice out today, but it’s also not."
    "I like that I get to be here with her, but I also don’t."
    "I’m conflicted in a number of ways and long for the one who has always been there for me."

    play sound "static.mp3"
    scene wakanaastrip5 with flash
    stop sound
    play music "asobeatsex6.mp3"

    "My beautiful desk."

    stop music
    play sound "static.mp3"
    scene wakanaastrip6 with flash
    stop sound

    "Just kidding."

    play music "comfort.mp3"

    "As it turns out, the “secret” place Wakana wanted to bring me was a third location of that same bookstore I’ve gone to with Futaba in the past."
    "You know, the one she tried to confess her feelings for me in."
    "Or the one we were kicked out of during the second Dorm Wars for...huh. Why {i}were{/i} we kicked out again?"
    "Either way, I’m here now with someone else. And today’s someone is not only significantly more well-versed in the world of literature, but a better writer as well. Probably."
    "Come to think of it, I haven’t read or heard any of Wakana’s poetry. But I’m sure it exists since she’s always going off the rails about the art form as a whole."
    "Come to think of something else, there’s not really much I know about Wakana to begin with."
    "But her wanting me here is all I really {i}need{/i} to know right now."
    "Maybe we {i}are{/i} the kind of friends who can just “hang out” without there needing to be some sort of ulterior motive or {i}purpose{/i} for it."
    "Maybe she’s believed that this whole time and {i}I{/i} have been the weird one for expecting there to be more to it."
    "And maybe today will be the day I {i}do{/i} learn more about her."
    "I think I’d like that."
    "..."
    "I think I’m lonely."

    w "Have you figured out why we’re here yet, Arakawa?"
    s "To hang out?"
    w "Yes and no. We {i}are{/i} “hanging out.” This much is true. But more than that, I need your help with something."
    s "Oh..."
    w "Just {i}“oh?”{/i} No snide remark or sexual innuendo in regard to what it is I {i}need?{/i}"
    s "Not today."

    scene wakanaastrip7
    with dissolve

    w "Is something the matter?"
    s "No. Just tell me whatever it is you need help with."
    w "Okay. But, in doing so, I’d like to invoke the “catch” you had me add earlier and ask that you do not sexually assault me after I tell you."
    s "I’ll do my best."

    scene wakanaastrip8
    with dissolve

    w "I’m conducting some independent research on a woman who may have been close to you. And by {i}may,{/i} I mean you were reduced to a hulking manchild the last time I brought her up in a scenario like this."
    s "I don’t know what you’re talking about."
    w "So {i}The Girl Who Cannot Breathe{/i} rings {i}no{/i} bells whatsoever?"
    s "..."
    w "Nothing at all? Not a peep?"
    s "..."

    scene wakanaastrip9
    with dissolve

    w "{i}Hah...{/i}"
    w "Arakawa, listen...if it makes you feel any better, I’m not doing this for {i}you.{/i} You’re an adult and it is well within your right to keep whatever secrets you’ve bottled up over the years to yourself."
    w "Would I hear them out should you wish to {i}un{/i}bottle them? Sure. But I will not force it out of you, nor belittle you for your reluctance in opening up to me."
    s "Then why are you doing this?"

    scene wakanaastrip10
    with dissolve

    w "Because either your niece has a remarkable gift or she has plagiarized her work for my poetry contest and must be punished. Though, I am leaning toward the former given {i}your{/i} background as well."
    w "Either way, I know you {i}know{/i} something. And that even if you’ve given up on ever telling anyone {i}anything{/i} about the way you’re feeling, you value your niece."
    s "What good will getting involved do if she has a “gift?” It’s poetry. It’s not like she needs an athletic coach or anything like that. She can just write and that’ll be it."
    w "A gift is not always a good thing, Arakawa. A wrong message in the right hands can change the world for the worse."
    s "And you think you can swoop in and prevent that from happening by...what? Finding more work from a writer you supposedly know all about already?"

    scene wakanaastrip11
    with dissolve

    w "There would be no need for {i}research{/i} if I already knew everything, Arakawa. But the hint that I was given at the beach was enough to prompt this investigation."
    w "It could be anything. A second pen name. The title of an anthology more of her work was published in. It’s like I’m trying to put together a puzzle right now and I only have half of the pieces."
    w "If you know something, help me. Because if your niece {i}did{/i} write that poem, it could mean she’s following in the footsteps of someone who got lost in the dark long before you and I did."
    w "You’re her guardian, are you not? Isn’t it {i}your{/i} responsibility to make sure she stays on the right path? Because she’s veering off, Arakawa. We are {i}teachers.{/i} We must {i}help{/i} her."
    s "It’s just a poem, Wakana."

    play sound "static.mp3"
    scene mm1 with flash
    scene mm2 with flash
    scene mm3 with flash
    scene mm4 with flash
    scene mm5 with flash
    scene wakanaastrip12 with flash
    stop sound

    w "You know damn well that nothing is “just a poem,” Arakawa! I don’t understand why you keep saying that!"
    s "You said just the other day that “The Road Not Taken” is {i}just a poem.{/i} Are you changing your mind already?"
    w "That was me being biased and pretentious! So if it gets you to open your fucking eyes, yes. I {i}am{/i} changing my mind."
    w "Your niece is mimicking the writing style of one of the most talented, yet utterly {i}sickening{/i} artists to ever find their way onto my shelf."
    w "And yes, her work was emotionally evocative and brimming with a level of creativity few others have ever been able to match. But what she {i}preached{/i} was {i}madness.{/i}"
    w "You have a {i}responsibility.{/i} As a {i}teacher.{/i} As a {i}parent.{/i} As {i}whatever{/i} the fuck you want to call yourself. And if you want to mope on your own time, have at it!"

    scene wakanaastrip13
    with dissolve

    w "But right now, there is a girl who is on the brink of walking down a {i}very{/i} dark path. And she needs our help."
    s "You got all of that from one poem?"
    w "Arakawa...it wasn't one poem."
    w "She submitted {i}twenty{/i} of them."
    w "And {i}all{/i} of them could have won the competition."
    w "So either she really {i}is{/i} mass plagiarizing, or there is {i}something{/i} going on in her head that you need to be worried about. Because if her mother is who I think she is-"
    s "Thank you for your concern."

    scene wakanaastrip14
    with dissolve

    s "I don’t know anything and Ami will be fine."
    w "There’s that look again...The same one you gave me last time. And the same one you probably {i}would{/i} have given me if you didn’t just walk away on the beach."
    w "Just {i}how much{/i} do you know about all of this?"
    s "I told you. I don’t know anything."
    w "But you’re lying, Arakawa. You {i}do.{/i}"
    s "Even if that’s true, I wouldn’t have to tell you about it. And you should be minding your own business when it comes to my niece. There’s no need for you to get involved over a contest."
    w "Why did you stop writing?..."
    s "..."
    w "What {i}are{/i} you to her?..."

    scene black
    with dissolve2

    s "Nothing anymore."

    "I step outside while Wakana finishes conducting whatever “research” she needs to do in the bookstore."
    "Frankly, I don’t really care."
    "And I was foolish for ever hoping that I wouldn’t be {i}needed{/i} for something today."

    $ renpy.end_replay()
    $ wakanadate25p1 = True
    $ wakana_love += 1
    stop music fadeout 15.0

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    jump wakanadate25p2

label wakanadate25p2:
    scene noonsky
    with dissolve2

    "My coworker or friend or whatever she’s supposed to be shows up not long after I step outside and I notice that she’s completely empty-handed."
    "So either she’s given up on pursuing something she thought was important just moments ago or my inability to help her forced her out of the shop without so much as a free bookmark."
    "Either way, I manage to come out on top this time — which mirrors the exact position I always end up taking in my fantasies of her."
    "I wouldn’t be surprised if those stopped for a little while now."
    "There’s a right time and a wrong time to pressure people into revealing their troubles to you, and I like to believe I’m a lot better when it comes to eying the clock than Wakana is."
    "That could very well just be something {i}I{/i} believe though. When, in all actuality, I may have been on the exact opposite end of things in the past."
    "It’s possible I pressure everyone all the time by just being me."
    "It’s possible that every single interaction I’ve ever had with someone younger and more naive than me involved me pressuring them in some way because that’s just how these sorts of relationships work."
    "Being on the other end of that isn’t fun."
    "It’s scary."
    "And I’d much prefer not being pressured into things anymore."
    "I have been good all day."
    "I do not deserve to be punished like this."

    w "Arakawa."

    play sound "static.mp3"
    scene wakanawalk1 with flash
    stop sound
    play music "thesleepingcity.mp3"

    w "It is clear that I have overstepped a boundary of yours, and I apologize for that."
    w "It wasn’t my intention to trap you into assisting me in what is sure to be another fruitless endeavor. But my endless thirst for all things dark and disturbing drives me to act inappropriately at times."
    w "I have, once again, let that get the better of me and cornered you in a way that I do not feel good about."
    s "Do you ever feel good about {i}anything?{/i}"

    scene wakanawalk2
    with dissolve

    w "Not really, no. Which likely contributes to my interest in all things black and dreary. "
    s "It is what it is. There’s no need to formally apologize when I never gave you something this professional after literally pushing you up against a wall."
    w "That is true. But I am a much better person than you are and clearly value this friendship a whole lot more. So please do not hold this apology against me in any form."
    w "I will stop pestering you about it for now and attempt to learn more on my own. But there {i}is{/i} one more thing I’d like to say first. "
    s "Me too. And I’d like to say my piece before you say yours."

    scene wakanawalk3
    with dissolve

    w "Feel free."
    s "Stop trying to “learn” more on your own."
    w "..."
    s "This whole thing...just give up. It’s probably just some sort of coincidence in the first place."
    w "Is that really something you expect me to believe given the reaction you’ve had on multiple occasions now? This is no {i}coincidence,{/i} Arakawa."
    w "If you want to refuse to divulge information to me, fine. But don’t just outright lie to me. That’s rude."
    s "I just think you’d be happier if you remained ignorant. That’s all."
    s "Getting involved in another family’s affairs is meaningless when you have your own troubles to worry about."
    w "I wouldn’t have chosen this line of work if I wanted to remain invested in naught but my own issues. And I would not be wasting my time with {i}you{/i} if that was a factor either."

    scene wakanawalk4
    with dissolve

    w "I’m a gleeful woman, full of joy and rainbows, who simply wants to spread happiness all across the land. "
    s "How hard was that to say on a scale of one to ten?"

    scene wakanawalk5
    with dissolve

    w "Fifty. But if straightforward compassion will not reach you, I figured sarcasm might. That’s more your speed, isn’t it?"
    s "If you want to be {i}compassionate,{/i} stay out of this. For me."
    w "So you can keep sulking and pretending you don’t love the things I know you do? "
    s "So I don’t revert to something even worse."
    s "It might not seem like it to you, but I’ve made some major strides lately. In a lot of different ways. "
    s "But there are things I’m not ready to deal with yet and this is one of them. And I’m sure it’s the same for Ami. So if you really want to be {i}compassionate,{/i} mind your own business. Please."

    scene wakanawalk6
    with dissolve

    w "Is that really what you want? To go it alone rather than lean on someone who cares about you?"
    s "You expect me to think you care about me after inviting me out just to satisfy your own curiosity? And then questioning me about a thing you {i}know{/i} sets me off? "

    scene wakanawalk7
    with dissolve

    w "That might have been how it seemed, but-"
    s "I was actually looking forward to hanging out with you without there being some ulterior motive for once. Then this happened. But I guess that’s on me for agreeing to come in the first place."
    w "Arakawa-"
    s "What did {i}you{/i} want to say? Sorry for interrupting. Mine took a little longer than I thought it would."

    scene wakanawalk8
    with dissolve

    w "..."
    s "..."
    w "Do you know why I wanted you to write something for the contest? And why I was so furious when you didn’t?"
    s "Because poetry turns you on."
    w "No, you fucking imbecile. It’s because I have to see your disgusting, expressionless face every single day while knowing {i}damn{/i} well that you are suppressing something and making yourself even uglier."

    scene wakanawalk9
    with dissolve

    w "Even if you don’t share it with anyone, writing can help you with your feelings. You can let them out without dragging anyone else down in the process. And that’s something you’re afraid of, isn’t it?"
    s "Have you stopped to think that maybe I just don’t like writing anymore?"
    w "No, because that’s stupid and you’re lying when you say that. "
    w "I’m proud that you’re allegedly making these alleged {i}strides{/i} and that you’re allegedly not as bad as you allegedly used to be. But if you want to make a {i}real{/i} stride...{i}write.{/i}"
    w "That’s all I wanted to tell you before we drop this altogether."
    s "I’ll think about it, Wakana. But I’m kind of mad at you right now."

    scene wakanawalk10
    with dissolve

    w "{i}Hah...{/i}again, I apologize. You’re not the only one who struggles to properly convey their thoughts and feelings, you know."
    w "Yes. I may despise every fiber of your being. But it’s not as if I actually {i}dislike{/i} you."
    s "Wow, you really are bad at conveying your thoughts and feelings if {i}that{/i} is the pitch you’re going to use to highlight our apparent friendship."
    w "Arakawa, I despise every fiber of {i}every{/i} person’s being. And I wish humanity as a whole would just fall into a sinkhole and die sometimes."
    s "Don’t wish for that too hard or it might just happen again."
    w "Sometimes I believe that my constant wishing for that is why it happened to our rival school in the first place. But that is beside the point."
    w "Yes, I hate everyone. And {i}everyone{/i} includes you. "

    scene wakanawalk11
    with dissolve

    w "But I am glad you are a part of my life. And the reason I’m so hard on you all the time is because I know you can be so much more than you are now. You just {i}won’t.{/i} And that pisses me off."
    s "Again, I’m trying to get better. It’s just taking a really long time."
    w "Well, there will always be an option there to speed it up should your backbone ever regrow."
    s "I’ll keep that in mind. Thanks."

    scene wakanawalk12
    with dissolve

    w "Fine. I suppose that’s all I can ask for."
    s "..."
    w "..."
    s "I’m still mad at you, though."
    w "Are you ten years old? "
    s "No. Just betrayed."
    w "Would carrying me around help you feel better?"
    s "I can’t imagine it would, Wakana."
    w "Are you absolutely sure?"
    s "I am absolutely sure, yes."

    scene wakanawalk13
    with dissolve

    w "You’re {i}positive?{/i}"
    s "I’m positive."
    w "There’s not a question in your mind?"
    s "..."
    w "100%%?"
    s "Wakana, what is this?"

    scene wakanawalk14
    with dissolve

    w "Arakawa, I’m well aware this is probably the worst possible time for this, but I need you to carry me."
    s "Excuse me?"
    w "It’s a long story. But I’m in excruciating pain right now and I am probably going to collapse if we keep walking. "
    s "Did you really try to trick me into thinking I {i}wanted{/i} to do this instead of just asking?"

    scene wakanawalk15
    with dissolve

    w "Yes. Because ideally, you would have agreed and I wouldn’t have had to explain myself. It would have looked like me giving you a reward."
    s "You really can’t walk?"
    w "I can not. And in a perfect world, I’d have pills with me to help for cases like this. But I have proven to be irresponsible with them and will no longer carry them when I don’t expect to be going places."
    s "I guess that’s something you should have thought about before inviting me miles away from school and then proceeding to make me mad."
    w "As fun and peppy as your grumpy side can be, Arakawa- my legs are starting to shake and you are an able-bodied man who has recently proven to have a great deal of stamina."
    s "I’m never going to let you live this down, you know."
    w "Oh, I’m well aware of that. But the alternative in this case is lying on the sidewalk until Osako can come pick me up. "
    s "There’s {i}no{/i} other option?"
    w "There’s no other option."
    s "..."
    w "..."
    s "Buy me dinner."
    w "Deal."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene wakanawalk16
    with dissolve2

    "It’s a lot harder to be mad at someone with their legs wrapped around you and their chin resting on your shoulder. I learned that today."
    "It’s actually {i}easier{/i} to be mad at someone while you’re having sex with them than this. This is just...uncomfortable."
    "But strangely enough, it doesn’t seem that way for Wakana."
    "Which tricks me into believing, once again, that maybe she does value me. And maybe she {i}wasn’t{/i} just trying to use me for her own benefit today."
    "But I have a hard time believing that when it comes to people who aren’t naive. And Wakana is anything but."
    "I {i}know{/i} she sees through me. And I feel that, at often times, I {i}let{/i} her because I {i}want{/i} her to realize how broken I am."
    "But then she does...and I don’t like it. So I backtrack and try to make things normal again, only to realize that it’s far too late. "
    "And now here she is...defenseless and just inches away from my face. But I have no desire to walk her down a dark alley and seize the day."
    "Instead...I just want to look at her."
    "To peer into the eyes of someone who doesn’t care for my shiny coat of paint or my polychromatic mask."
    "And to get lost in {i}her{/i} when I know with all of my decaying heart that I shouldn’t."

    s "..."
    w "..."
    s "Is this weird for you?"
    w "A little. But I’ve gotten used to it over the years."
    s "Is this a common occurrence for you or was that more sarcasm?"
    w "It’s a relatively common occurrence, unfortunately. But modern medicine has made it mostly manageable. And my partner can carry me across all of Japan without so much as breaking a sweat."
    w "It’s really only an issue when I find myself miles from home with strange men. Which, needless to say, has happened a grand total of one time in recent memory."
    s "Is this, like...the result of some kind of accident or something? Or were you just born weak?"

    scene wakanawalk17
    with dissolve

    w "I suppose it would be a little bit of both. "
    w "It’s not a very interesting story, but I believe I owe you at least {i}some{/i} amount of uninhibited chatter on account of how unmistakably {i}unfriendly{/i} I’ve been today."
    s "That was a lot of “uns” for one sentence."

    scene wakanawalk18
    with dissolve

    w "Do you want to hear why I’m making you do this or not?"
    s "My bad. Go ahead."
    w "Okay. But again, it’s not very interesting. "
    s "Then maybe I don’t want to hear it after all."
    w "Well, too bad because here it comes."

    scene wakanawalk19
    with dissolve

    w "I was born well before I was meant to be — which resulted in a slew of health issues that I’ve been dealing with for my entire life. Some more severe than others."
    w "Among those issues was the malformation of my spine."
    w "Thankfully, I was born to a wealthy family that was able to afford the corrective surgery needed to repair it."
    w "{i}Un{/i}thankfully, even the most experienced of surgeons in the most prestigious of hospitals can’t help but make mistakes sometimes. They’re human, after all. That sort of thing is inevitable."
    w "I’m sure I don’t have to tell you this, but the spine is a fragile thing. One wrong move or injury to that part of the body could leave you paralyzed for life. So I’m lucky I got off with just this."
    w "I was {i}not{/i} lucky enough to be gifted an entirely {i}normal{/i} life, though — and I’ve been mildly useless in all things physical ever since."

    scene wakanawalk20
    with dissolve

    w "Well...{i}almost{/i} all things. I still excel in a few...{i}select{/i} areas."
    s "I’m happy for Osako."

    scene wakanawalk21
    with dissolve

    w "As you should be. But there are a few more {i}appropriate{/i} areas I was able to manage in as well. Like kyudo."
    s "Isn’t that really taxing on a person’s back, though? "
    w "Very. And when I was going to Higashigaoka, my doctors advised that I pursue something else instead at the risk of further harming myself. "
    s "But you disregarded their opinions and kept doing kyudo anyway?"
    w "Yes. But also no. I was never able to compete in tournaments, but I could still shoot two days out of the week. But that was enough for me back then."
    w "And {i}more{/i} than enough for me {i}now{/i} to become the instructor of a bunch of public school girls without any experience. And also Ushibori, who is just...very good, for some reason."
    s "She’s from Nara. They're probably more interested in boring stuff like archery out there."
    w "That explains a few things. Also, fuck you."
    s "What other health issues do you have as a result of your...early birth thing? You said there were more, right?"
    w "A few. But I think one is enough for today. It’s not as if hearing any of the others will assist in explaining why I’m making you carry me."
    s "Is your back okay in that position? Do I need to, like...adjust you or anything?"
    w "This is plenty, Arakawa. Thank you."
    s "Don’t worry about it. You could have just told me this earlier instead of trying to trick me into carrying you, though."
    w "Excuse me, are {i}you{/i} telling {i}me{/i} to be more open about my insecurities and the things that hold me back in life?"
    s "Touché."
    w "Touché indeed."
    s "..."
    w "..."

    scene wakanawalk22
    with dissolve

    s "I wonder what Osako would say if she saw us like this."
    w "..."
    s "..."

    scene black
    with dissolve2

    w "Don’t."

    $ renpy.end_replay()
    $ wakanadate25p2 = True
    $ wakana_love += 1
    stop music fadeout 10.0

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    jump wakanadate25p3

label wakanadate25p3:
    scene wakanatreatsyou1
    with dissolve2
    play music "hallelujah.mp3"

    "After a fair bit of walking and a great deal of being told where to go, the two of us make it to a rather...{i}purple{/i} looking restaurant."
    "And not a moment too late, as I was only a block or two from tossing Wakana into the river to never be heard from again."
    "In fact, the only reason I {i}didn’t{/i} do such a thing is that I didn’t want to be bothered actually navigating to it. "
    "Though, I suppose there’s the element of a free dinner that I was looking forward to as well."
    "But either way, we’re here now and I no longer have to deal with the tyranny that is backseat driver, Wakana Watabe. "
    "And yes, it is possible to be a backseat driver when the seat is literally someone’s back."
    "And yes, it is just as annoying as it sounds."

    w "Is something wrong {i}again,{/i} Arakawa? What did I do to piss you off this time?"
    s "This time isn’t serious. I just think you need to be a little more considerate when someone is carrying you around. You were very bossy back there."
    w "Aww...did I hurt your feelings? Does it make you feel weak not being in charge of every facet of everyone’s life at every point ever?"
    s "Wakana, I was literally carrying you."
    w "And you could have done a better job. That is all I’m saying."

    scene wakanatreatsyou2
    with dissolve

    w "But we made it here. And I suppose that’s all that really matters."
    s "Until you have to find another human taxi once we’re done eating. Also, where is {i}here?{/i} And since when does something like this exist in Kumon-mi?"
    w "This place has existed forever. You likely just haven’t stumbled upon it because you’re an overly-sensitive manchild who spends his free time eating at maid cafes and hitting on teenagers."
    s "Only because it’s impossible to do that first thing without doing the second thing in the process."
    w "It is very much possible to visit a maid cafe without being a pervert, Arakawa."
    s "Well, it isn’t possible for me. And the food there is surprisingly good."
    w "That’s just not the reason you go."
    s "Exactly."

    scene wakanatreatsyou3
    with dissolve

    w "This place has been a favorite spot of mine since college. I’ve come here with Osako on many occasions. We even had our first date here."
    s "And now {i}I{/i} get to have the pleasure of being wined and dined by you in the same building where you formed a lifelong partnership? Wow. Maybe we really {i}are{/i} friends after all?"
    w "I’m glad to see my decision to share a bit of sentimentality with you is paying off in spades. Just don’t mention we came here to Osako or she’ll likely assume we’re sleeping together."
    s "That said, is it actually okay for me {i}to{/i} be here? You could have just taken me to a McDonald’s or something."

    scene wakanatreatsyou4
    with dissolve

    w "We’re here because {i}I{/i} want to be here. Not because you actually mean something to me."
    s "That’s fine. Just make sure to give me a five-star review for the ride. It’ll look good on my profile."
    w "Did you know you’re the first person I’ve ever brought here {i}besides{/i} Osako? "
    s "No. But that’s mostly due to the fact that the only things I know about you are that you’re into BDSM and that your back is fucked up. Which, thinking about it now, isn’t the safest combination of things."
    w "I’ve managed so far. Albeit with a great deal of help from the medical field. "
    w "But what I’m trying to allude to in telling you this seemingly unimportant fact is that this gesture is meant to make you smile."
    w "If you even know how, that is."
    s "I don’t."
    s "I’m glad to see you do, though."
    s "You’ve been doing that a lot lately, come to think of it."

    scene wakanatreatsyou5
    with dissolve

    w "It’s almost like getting to know someone means you can show them sides of yourself you don’t typically show others."
    s "Yeah. But only {i}almost.{/i} I’m still going to keep everything hidden forever because it makes life easier."
    w "If your life is so easy, why do your eyes begin to glisten each time I bring up a certain extremely controversial poet?"
    s "My eyes are always glistening. I am simply that beautiful. But not nearly as beautiful as-"
    w "Don’t even think about it."
    s "My bad. The whole “being out on a date at an important restaurant” thing must be getting to me."
    w "This is not a {i}date,{/i} Arakawa. This is two gloomy and sarcastic friends escaping the grind that is a life dedicated to sculpting the minds of youth. Or, in your case, destroying them."
    s "Hey, that’s still {i}sculpting.{/i} Just in reverse."
    w "You disgust me."
    s "Then why are you still smiling?"
    w "Because you’ve forgiven me. And I’m glad that we’re back on track."
    s "Who says I’ve forgiven you?"
    w "You do. Just not directly. But your actions and your attitude tell me that I have crawled my way out of the doghouse and back into your top eight."
    s "Top eight?"

    scene wakanatreatsyou6
    with dissolve

    w "Wait, Arakawa — how old are you again?"
    s "I’m 31."
    w "Did you...{i}not{/i} have a Myspace account growing up? "
    s "Is that a social media thing?"
    w "It is, yes. Or...was. Or technically still {i}is.{/i} But mostly just {i}was.{/i}"
    s "Then, no. I was never into that sort of thing."
    w "Wow, you really are the most dull person to ever walk the face of the Earth, aren’t you?"
    s "I guess so. But it’s not like you’re all that far ahead of me, little Miss “Private school.”"

    scene wakanatreatsyou7
    with dissolve

    w "Woe is me. I’m being teased for receiving a proper education and coming from an affluent background. Oh, how will I ever recover from this?"
    s "Actually, yeah. Hold on. If you come from an affluent background, why are you living in a one bedroom apartment with a girl who works two jobs?"

    scene wakanatreatsyou8
    with dissolve

    w "Arakawa, this may come as a big surprise to you, so brace yourself- but there are people in this world who are too proud to accept aid from others and would much rather get by on their own terms."
    w "When Osako and I first decided to start living together, we agreed to be among those people. We agreed that we’d survive off of our {i}own{/i} money rather than rely on my parents."
    s "W-"
    w "Because life is more fulfilling that way. "
    w "Additionally, relying on someone to that extent means you have the potential to be monumentally {i}fucked{/i} if they pull the rug out from underneath you."
    w "And if I am going to be monumentally {i}fucked{/i} by {i}anyone,{/i} I’d prefer it to be my partner rather than my parents."
    s "That’s kind of admirable, actually. I wish I had that kind of willpower."
    w "I wish you had {i}any{/i} amount of willpower so you could come to understand that your insistence on nibbling at forbidden fruit is completely asinine and that you are squandering a wonderful opportunity."
    s "Wait, what? Are we changing topics?"
    w "No. At the moment, we are on the topic of love. And seeing as my love is strong and my loyalty is unflappable, it is time for me to, once again, take a moment or two to ridicule you."
    s "What happened to smiley Wakana? I want her back."
    w "No. You asked me a question about my personal life, so it’s only fair that I now pry into yours as if my words are the jaws of life and your thoughts are-"
    s "Choose a different simile."

    scene wakanatreatsyou9
    with dissolve

    w "..."
    s "..."

    scene wakanatreatsyou10
    with dissolve

    w "Apologies. I...didn’t realize that was-"
    w "Anyway, what I meant to say is that this dinner means nothing if all we discuss is {i}me.{/i} Relationships go both ways and-"
    s "Yours doesn’t."

    scene wakanatreatsyou11
    with dissolve

    w "Was...Was that a lesbian joke?"
    s "Yeah. Just moving right along. No time for any more depressing stuff right now."
    w "You {i}do{/i} know I’m attracted to men as well, correct?"
    s "Yeah. But I also know that Osako {i}isn’t.{/i} Which makes my joke both valid and hilarious."
    w "While it’s cute to see your sense of humor is no more mature than the girls who fill your classroom, I would like to move on now."
    s "My bad. Go ahead."

    scene wakanatreatsyou12
    with dissolve

    w "Arakawa, I am going to be straight with you right now."
    s "Get your facts in order, Wakana. You were bi just a second ago."

    scene wakanatreatsyou13
    with dissolve

    w "Pfft!"
    s "Are...Are you actually-"

    scene wakanatreatsyou14
    with dissolve

    w "No."
    w "I am going to be {i}direct{/i} with you right now because this matter concerns me on a number of levels and, as the most successful person you know in the world of romance, you should follow my lead."
    s "By doing what exactly?"
    w "By cutting down the hopes and dreams of twenty hormonal teenagers who think they’re in love with you because you’re the only creature within a fifty mile radius who has a penis."
    s "Wakana-"
    w "And by opening your god damn eyes and seeing what’s right in front of you."
    s "What’s right in front of me is a woman who’s already in a committed relationship. And Osako would-"

    scene wakanatreatsyou15
    with dissolve

    w "Not {i}me,{/i} you fucking idiot. Imani. "
    s "You too?"
    w "What do you mean, “me too?” Who else have you talked to about this?"
    s "Rika. And I’ll tell you the same thing I told her. I care about Imani. Like...way more than I ever expected to. "

    scene wakanatreatsyou16
    with dissolve

    w "Then why-"
    s "That {i}is{/i} why. "
    w "I’m not following, Arakawa. Please channel all of the primitive power in your simian brain and explain this to me in a way that a normal human being would be able to understand."

    scene wakanatreatsyou17
    with dissolve

    s "Imani is a {i}great{/i} match for me. Everyone knows that. And if I were a normal person, I’d jump at the opportunity to be with her. "
    s "But I’m {i}not{/i} a normal person."
    s "And I {i}can’t{/i} be with her in a way that would make her happy. "
    s "She’d grow to resent me when she realizes that I’m not who she thinks I am. And eventually, she’d start blaming herself for not seeing that in the first place."
    s "She’s strong and independent and all that, so I don’t want to say it would screw her up for good when I think she’d be fine after a little while. "
    s "But {i}I{/i} wouldn’t. I don’t have anyone else like her in my life. "
    s "There’s you, yeah. But you’re different. Imani’s like...a little sister or something. Just she’s a completely different race than me and I also want to have earth-shattering sex with her."
    s "I’m just not the right person for her. If it was purely physical, I’d be able to look past it. But I think that ship has sailed. And I don’t want to lead her on."
    w "..."
    s "Is that enough? Can we go back to talking about you and your sexual orientation again?"

    scene wakanatreatsyou18
    with dissolve

    w "{i}Hah...{/i}Of course the {i}one{/i} thing you’d be mature about is the one thing that will wind up hurting someone else who’s close to me."
    s "I’d only hurt her more if I took your advice."
    w "I know. You’re right. Which is why I’m not arguing with you and why I am hereby retiring as her wingwoman. I just feel bad for the poor girl as she’s quite smitten for {i}some{/i} ungodly reason."
    s "Yeah. People just kind of fall for me like that. Maybe it really is the penis thing after all?"

    scene wakanatreatsyou19
    with dissolve

    w "On that note, how the absolute {i}fuck{/i} did you wind up bagging an idol? And Kumon-mi’s darling, no less."
    s "She’s my childhood friend. And the first girlfriend I ever had. And also maybe the last? It’s kind of complicated."
    w "So...wait. I know I just said I’d drop this, but now I’m confused."
    w "You won’t be with Imani because you care too much about the prospect of harming her. But you {i}will{/i} be with your childhood friend and ex-girlfriend, who plays a {i}much more{/i} significant role in your life?"
    w "Are you just...{i}okay{/i} with hurting her?"
    s "No."
    s "I’m just in love with her."

    scene wakanatreatsyou20
    with dissolve

    w "{i}Hah...{/i}"
    w "This is why I’ve never dated a man. You’re all stupid. You could have just said that and put an immediate end to the Imani situation without having to go into such detail."
    s "You wanted me to talk, so I talked. This is your fault."

    scene wakanatreatsyou1
    with dissolve

    w "So the beast {i}can{/i} feel love after all."
    s "I’m not sure how I feel about being called a “beast.”"
    w "Apologies for my hesitance in calling you “human.” I just have a hard time believing you actually {i}are{/i} one after how long I had to listen to your childhood friend cry out in pleasure the other night."
    s "Yeah...sorry about that. And also, sorry for her trying to rope you two into it."

    scene wakanatreatsyou20
    with dissolve

    w "My one chance to sleep with a celebrity...squandered by moral obligations and my previously mentioned unflappable loyalty."
    s "You do realize I would have been involved too, right?"

    scene wakanatreatsyou3
    with dissolve

    w "It’s not unusual for there to be a little suffering on the way to making your dreams come true. Your inclusion would simply be me “taking one for the team.”"
    w "Unfortunately for {i}all{/i} of us, Osako matters to me far too much to do something like that. So I will put her best interests at heart and just pretend none of it ever happened."
    s "But...just to clarify, {i}you’d{/i} be okay with it?"

    scene wakanatreatsyou9
    with dissolve

    w "With what? Having a threesome with an extraordinarily attractive celebrity? Of course I’d be okay with it. That’s a once in a lifetime opportunity. "
    s "You don’t think that interferes with your {i}love{/i} or anything?"
    w "I am of the opinion that true love {i}is{/i} letting your significant other have sex with a celebrity because, again, come on."

    scene wakanatreatsyou7
    with dissolve

    w "But...that is {i}not{/i} how Osako thinks. And her thoughts and feelings are just as important as mine. If not even {i}more{/i} important."
    w "Regardless — I thank your childhood friend for the offer, congratulate you on being human enough to love someone, and pity Imani more than I already {i}have{/i} been for her despicable taste in men."
    s "Busy night for you, huh? This is probably the most you’ve had to think since college."
    w "That’s not true at all. My mind was absolutely {i}flooded{/i} by complicated thoughts after that one time I overdosed and wound up in the hospital while you completely ignored my existence."
    s "Wakana, it’s been years. It’s time to move past that."
    w "It’s not been {i}years,{/i} Arakawa. Years would imply that-"

    play sound "static.mp3"
    scene wakanatreatsyou21 with flash
    stop sound

    w "..."
    s "..."
    s "Wakana?"
    w "..."
    s "Are you-"
    w "Shh. I’m thinking."
    s "..."
    w "..."
    s "..."
    w "..."

    play sound "static.mp3"
    scene wakanatreatsyou22
    with flash
    stop sound

    w "Are you familiar with Ecclesiastes 3:1-8?"

    stop music
    scene black

    $ renpy.end_replay()
    $ wakanadate25p3 = True
    $ wakana_love += 1

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label wakanaspring1:
    scene bedroom_day
    with dissolve2
    play music "daybreak.mp3"

    "It was a normal day, just like any other."

    stop music
    play sound "static.mp3"
    scene wakanaseizehim1 with flash
    stop sound
    play music "rapid.mp3"

    "Until it wasn’t."

    s "This is really not the BGM track I want to hear this early in the morning. "
    w "Imani. Seize him."
    ima "Wakana, don’t you think we should maybe {i}talk{/i} about this first? Senpai clearly just woke up and-"
    w "Absolutely not. Seize him now."
    a "Uhh...Dad? What’s going on?"

    scene wakanaseizehim2
    with dissolve

    ima "What?! Shouldn’t we be asking {i}you{/i} that question?! Why you callin’ this man “Dad” all of a sudden?! The hell happened while you two’ve been cooped up in here?!"
    a "A lot, actually."
    w "Arakawa Junior, stop that. This man is not your father and has likely just brainwashed you into believing he is."
    s "Don’t listen to them, Ami. They won’t get it."
    w "See? He’s doing it right now."

    scene wakanaseizehim3
    with dissolve

    a "Actually, Sensei’s been standing in for my dad for a really long time now and the two of us decided it would be best if we finally took our relationship to the next level because of our undying love for one another."
    s "Did you really have to word it like that?"
    w "Imani, seize him before I gag."
    ima "Oh! So like, normal dad. Not sex dad."
    a "He can be any kind of dad he wants and I would never think to refuse him because I am a good girl."
    s "Can we forget about all of the fatherhood stuff and get to the bottom of why you two have stormed into my house trying to “seize me?”"

    scene wakanaseizehim4
    with dissolve

    w "Not until you have been properly seized. Doing so beforehand gives you the opportunity to refuse. "
    a "I think you’re being kidnapped."
    ima "You are. And I’m the muscle. But seeing as you definitely don’t want to come...let’s go, Wakana! Time to leave!"
    s "Go {i}where?{/i} Because if you’re here to drag me back to school, you should probably do it on a day where there actually {i}is{/i} school."
    w "The only {i}school{/i} you need to be concerned about right now is a school of fish. "
    s "...What?"
    w "Get in the car, you pathetic excuse for a man. We’re going to the beach."

    scene wakanaseizehim5
    with dissolve

    a "Wait, is it really time for the class beach trip already? Have I been gone that long?"
    w "No. {i}Your{/i} trip isn’t for another few weeks. This trip is for staff members only. And also Osako because she is my plus-one. "
    ima "By “staff members” she really means just us. No one else from the school is coming."
    s "Well...can Ami be {i}my{/i} plus-one then?"
    w "No. She’ll ruin everything."

    scene wakanaseizehim6
    with dissolve

    a "It’s sad because it’s true."
    ima "Hey! Cheer up, Ami! At least you have a dad again. That’s more than like half the class can say."
    s "Please don’t joke with her like that. And please leave if you’re not going to let me bring her along. "
    w "Please stop your moaning and be seized already. I don’t have the energy for this."
    s "Wakana-"
    a "Dad, it’s fine. You can go without me, I won’t be jealous."

    scene wakanaseizehim7
    with dissolve

    a "Well, actually, I {i}will.{/i} But there’s not really anything I can do about it and I feel bad that you’ll be staying back just for me."
    s "Stop growing up so quickly. I’ve only been a dad for a couple weeks."

    scene wakanaseizehim8
    with dissolve

    a "But you’ll still be one for the rest of forever so it doesn’t even matter!"
    w "What now, Arakawa Senior? You no longer have a reason to refuse."
    s "Wakana-"

    scene wakanaseizehim7
    with dissolve

    a "Just go. It’ll be fun."
    a "Only for one night, though. Any longer than that and you might come back to a bald daughter."

    scene black
    with dissolve2
    stop music fadeout 15.0

    s "Ugh...fine."
    w "Imani, seize him."
    ima "Is the seizing really necessary if he agrees to come quietly?..."

    "Somehow or another, I wind up getting roped into a second spontaneous and adult-focused outing after just having gone camping with Sara and company a little while ago."
    "However, that trip featured a lot of “building me up” since that group of friends has always been extremely supportive of me for some reason."
    "This trip, I imagine, will involve a heavy dose of Wakana belittling me while Imani secretly prays for me to fuck her once everyone else goes to sleep. So suffice it to say, I think it’ll be a little less poignant."
    "But...it {i}has{/i} been a while since I’ve spent time with them. And humoring them with my presence (which shouldn’t be wanted in the first place), is the least I can do."
    "Also, in case you were wondering, the “car” Wakana referenced winds up being a taxi since none of us actually possess a vehicle."

    stop music
    play sound "static.mp3"
    scene wakanaseizehim9 with flash
    stop sound
    play sound "broken.mp3"

    "{b}WHICH IS GREAT BECAUSE I’LL NEVER BE ABLE TO DRIVE ONE{/b}"

    play sound "static.mp3"
    scene wakanaseizehim10 with flash
    stop sound
    play music "acoustic.mp3"

    s "So are all of the rooms at this inn just identical or?..."
    ima "We bought the “plus package” so the room came with alcohol this time."
    w "And if all goes according to plan you’ll {i}also{/i} be getting a “plus package” by the end of the night."

    scene wakanaseizehim11
    with dissolve

    ima "Hahaha! I’m going to kill you!"
    os "Is it even okay for you to be drinking with your new medication? "
    w "I doubt there will be any side effects from drinking just a little. And it doesn’t seem like the inn gave us much in the first place."

    scene wakanaseizehim12
    with dissolve

    os "Wakana, there are like thirty beers and a bottle of champagne there. "
    w "Yes, and that’s only seven beers and about a glass or two for each of us."
    s "We’ll still have two beers left over at that rate. "

    scene wakanaseizehim13
    with dissolve

    w "Wonderful job, Arakawa. At this rate, you’ll be ready to start teaching again in no time at all and Imani won’t have to break her back cleaning up after you anymore."
    ima "Don’t mind her, Senpai. I’m doing fine and you can take all the time you need. "
    ima "Though...it wouldn’t be a lie to say that I’d like you to hurry up if possible. Not because of work specifically, though. Just because I miss having you around."
    w "Now kiss."
    ima "{i}Please{/i} don’t mind her. I know you don’t see me like that and I’m seriously not trying to pressure you. In fact, this is kind of why I didn’t want you to come {i}at all{/i} and-"
    s "You don’t want me here?"

    scene wakanaseizehim14
    with dissolve

    ima "Wha- no! I just meant that, like...cause you are......and I am......and sex........soooooo yeah!"

    scene wakanaseizehim15
    with dissolve

    ima "Who wants a drink?!"
    w "You two go ahead, but do not even think of putting your hands on my seven. Or eight. "
    w "Fifteen or sixteen counting Osako’s, as she’ll be coming to the shower with me right after putting our luggage away. "
    os "Do you guys need anything from the lobby? Any snacks or...additional drinks if seven beers and one to two glasses of champagne isn’t enough for you?"
    w "They sell contraception as well. Not that I’m sure either of you would bother using it."

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    os "Wakana, leave those two alone. If they want to have heterosexual sex together, let them have heterosexual sex together on their own terms."
    ima "{i}Thank you,{/i} Osako! But...why did you have to be so specific?"
    w "Pay no mind to my cat. She’s been thinking quite a bit about heterosexual sex lately. Haven’t you, kitty?"
    os "Wakana...{i}don’t do this....{/i}"

    "Wakana and Osako don’t stay in the room much longer."

    play sound "static.mp3"
    scene wakanaseizehim16 with flash
    stop sound

    "After grabbing their things, they exit the main hall and head to the showers, leaving Imani and me alone when I’m {i}pretty sure{/i} Wakana directly told me she’d stop doing this."
    "But at least Imani doesn’t seem to be completely taken off guard by it, so...I imagine she kind of knew this was coming."
    "And I imagine that’s what this whole trip is {i}for{/i} based on how we were immediately left alone next to a bottle of champagne with a huge heart on it."

    s "So..."
    ima "I’m...sorry about Wakana. She’s been kind of...{i}off{/i} lately. "
    s "Off how?"

    scene wakanaseizehim17
    with dissolve

    ima "Uh...we kind of said we weren’t going to talk about that this weekend. But all you really need to know is she’s been...working kind of hard."
    ima "Like...really hard. And not just at school."
    s "So {i}that’s{/i} why she’s decided to start trying to hook us up again? Because she’s...{i}off?{/i}"

    scene wakanaseizehim16
    with dissolve

    ima "Oh, I don’t think that’s it. I think that’s kind of just a...thing she’s doing to distract herself from the real reason we came all the way out here. You know...to like, keep the mood light and whatnot."
    s "Isn’t the reason we came all the way out here to enable one more situation for the two of us to finally sleep together?"

    scene wakanaseizehim18
    with dissolve

    ima "What? No, that’s not it at all. And frankly, I didn’t really want to come either."
    s "I’m...not sure I follow."

    play sound "static.mp3"
    scene wakanaseizehim19 with flash
    stop sound
    play sound "shower.mp3"
    stop sound fadeout 10.0

    ima "{i}Wakana and Osako are kinda, like...fighting lately. And Osako threw this trip together to try and, like...put an end to that or something.{/i}"
    ima "{i}Which is why I’m thankful you’re here since I didn’t want to be the third wheel. But I also feel bad about you getting dragged into it, so...{/i}"
    ima "{i}I guess let’s just...try and have some fun, okay? And not get in their way too much...{/i}"
    os "Do you really need to keep laying the pressure on Imani like that? I thought the whole thing with her and Akira was, like...a sensitive topic?"
    w "It’s only sensitive because Arakawa is a fucking coward who’s been habitually abused for so long that he wouldn’t know a “good” partner if they slapped him across the face."
    os "Do good partners hit each other now?"

    scene wakanaseizehim20
    with dissolve

    w "Sometimes. When the mood is right. Is {i}that{/i} what we should try to get me off next? Or do you still prefer the idea of me fucking someone else?"
    os "Wakana, I said I was sorry about that. I really don’t know what else I can do. But you haven’t been great either lately and you know it. "

    scene wakanaseizehim21
    with dissolve

    w "Yes, it appears we’ve both been rather unpleasant as of late. Here’s hoping that fifteen or sixteen beers collectively can fix it."
    os "It’s less about the beer and more just about being here. It’s...weird going from having sex multiple times a day to barely ever at all. "
    w "Which is why we should focus our efforts on getting our friends to sleep together instead. They can prosper while the two of us only get wet while we’re showering together."

    scene wakanaseizehim22
    with dissolve

    os "We could maybe, like...do it {i}here?{/i}"
    w "With people around? This is no train station bathroom, Osako. Getting caught here could put my career in jeopardy."

    scene wakanaseizehim23
    with dissolve

    os "I mean...so could fooling around in your office and we used to do that like every single week."
    w "I can lock my office. I can {i}not{/i} lock the outside world. "
    os "If you don’t want to do it, just say so. You don’t have to beat around the bush."
    w "What bush? You shaved just yesterday, did you not? "
    os "Wakana-"
    w "I don’t want to do it."

    scene wakanaseizehim24
    with dissolve

    os "Is it...still because you’re mad at me?"
    w "It’s nothing that exciting. My new medication is likely just sodomizing my libido. But in the less fun sort of way."
    os "Can you maybe stop taking it then?"

    scene wakanaseizehim25
    with dissolve

    w "I’ll have to find a new one. I {i}could{/i} stop. But sexual disinterest is preferable over “excruciating back pain while also being horny.”"
    w "Besides, it’s not as if we can just {i}fuck{/i} away our issues. We’re not in college anymore."

    scene wakanaseizehim26
    with dissolve

    os "I know...that’s why I’m trying to figure this out. I love you, Wakana. And it’s {i}weird{/i} fighting. Especially over something so small..."

    scene wakanaseizehim27
    with dissolve

    w "{i}Small?{/i}"
    os "I didn’t mean it like that..."
    w "Would it be {i}small{/i} if I were to suggest you go and fuck Imani since I’m not feeling up to it today? Or do you think that maybe suggesting infidelity {i}isn’t{/i} the best way to handle that?"

    scene wakanaseizehim28
    with dissolve

    os "Babe! You {i}never{/i} cum! Like, {i}ever!{/i} And that seriously {i}fucks{/i} with me. I just don’t want you being unhappy! That’s the whole reason I suggested it. It’s not like I actually {i}want{/i} that."
    w "And it’s not like I actually want you to fuck Imani. But she could use the relief since Arakawa’s a pussy and you need the morale boost. "
    os "What do you want me to do, Wakana? Just tell me."

    scene wakanaseizehim29
    with dissolve

    w "I don’t {i}know...{/i}It’s not as if I’m holding that information hostage. I seriously {i}don’t know.{/i}"
    w "I’ve become more present for you, have I not? "
    w "Like...yes, I’m still not {i}as{/i} present as I once was. But my mind is wrapped up in something at the moment and it involves the well-being of a dear friend. So, I apologize for that..."
    w "But Osako...{i}really?{/i} Did you really think {i}that{/i} would be the solution to the ridiculous notion you concocted that you’re somehow not enough for me? {i}Giving me up?{/i} Really?"
    os "I just want you to be happy-"

    scene wakanaseizehim30
    with hpunch

    w "Then grow a fucking spine! Jesus Christ!"
    w "This bullshit, unwarranted insecurity of yours needs to fucking end, Osako! Be a God damn woman for Christ’s sake!"

    scene wakanaseizehim31
    with dissolve

    w "All I have {i}ever{/i} done is love you. All I’ve ever done is try to make you feel like you’re enough, because you {i}are.{/i} "
    w "But no matter what I do, you still don’t see it."
    w "And if after all this time, I can’t make you feel complete..."

    scene wakanaseizehim32
    with dissolve2

    w "Maybe {i}you’re{/i} the one who needs someone else?..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ wakanaspring1 = True

    jump wakanaspring2

label wakanaspring2:
    scene clearnightsky
    with dissolve2

    "The rest of the day dies off without putting up much of a fight."
    "I spent most of it lounging around with Imani, talking about how school has been for her and how misery has been for me."
    "Not much has changed on either end."
    "It’s kind of funny, really — how all of the girls in class like to tell me about how {i}different{/i} things are without me but, at least according to her, everyone’s more or less the same."
    "The loud ones are still loud, the quiet ones are still quiet. The smart ones are still smart and the weird ones are still weird."
    "I guess that word encompasses most of the class, though."
    "I miss them sometimes. But it’s diluted by the fact that I can visit them whenever I want {i}outside{/i} of school."
    "It’s a terrible dilution, really — like mixing ammonia into bleach, where it’s hard to realize just how dangerous it really is until it’s already too late."

    scene wakanabeachdrunk1
    with dissolve3
    play music "hallelujah.mp3"

    "Something’s up with Wakana and Osako. "
    "I can see it now that it’s been pointed out."
    "They’re good at hiding it, though. Which is why I’m thankful for Imani since she swooped in and told me before I had to force it out of Wakana."
    "She might look strong, but it’s all a facade. I realized that the day she broke down in my arms just minutes before I told the girls I’d be leaving them for a little while."
    "All things considered, I probably could have noticed sooner. And I probably should have listened when everyone told me she actually {i}likes{/i} me."
    "I’m not sure why she is the way she is, but there’s still a {i}lot{/i} I don’t know about her. And that’s fine. I don’t need to know everything."
    "But I can’t stop looking at her tonight — and it’s not because of her bathing suit. "
    "I just don’t want her to be sad."
    "She’s too good for such feelings, though. And it’s doubtful they’ll ever reach her in the first place when the pedestal I’ve placed her on is so high up that I’d need a rocket just to get there."
    "They’ll work it out, I think."
    "They’re adults."
    "They’re adults and they’re in love. Or at least what we all see as love when I’m sure it’s more complicated than that."
    "The way each of them struggles to hold eye contact with one another for more than a second is the only hint I need right now."
    "But again, that’s fine — because {i}my{/i} eyes are on her, even if they aren’t meant to be. And she won’t go unnoticed."
    "For tonight, though, the way I’ll stare is different."
    "For tonight, I’ll silently acknowledge how important to me she is. "
    "But in the morning, I’ll forget..."
    "Because this is the most miserable I’ve ever seen her — and I don’t want that memory to remain. Nor do I want the image of that fake smile ingrained into my mind because I {i}know{/i} it’s all just hope and booze."
    "And yes, Osako looks sad too...but more defeated than anything."
    "Wakana, though-"

    ima "Hey...has anybody ever told you guys how fuckin’ {i}HOT{/i} you are?"

    "I feel like Wakana might get lost at sea the second I stop looking at her."

    w "All the time...Osako and I were actually voted the most attractive couple in college....Isn’t that right, Osako?"
    os "It’s not. Senior superlatives aren’t really a thing once you get out of high school."

    scene wakanabeachdrunk2
    with dissolve

    ima "I ever tell you guys I actually won one of those things?"
    w "Not that I can remember. Which is good, because the people who brag about those things years later are the same ones who peaked in high school and have to live the rest of their lives in a constant decline."

    scene wakanabeachdrunk3
    with dissolve

    ima "Girl, why you gotta do me like that?..."
    os "I won a few of those actually. {i}Most likely to win an Olympic medal...Most likely to travel the world...{/i}"
    os "And also {i}best smile.{/i}"
    s "Best smile? Really?"

    scene wakanabeachdrunk4
    with dissolve

    os "Why do you sound so surprised?"
    w "Osako used to get these cute little dimples in her cheeks when she was younger. Now, they only come out once in a blue moon. How sad."
    s "That one just...didn’t fit in with the other two, I guess."
    ima "The fuck, man? I just won class clown."

    scene wakanabeachdrunk5
    with dissolve

    w "And I won {i}absolutely{/i} nothing because I went to a prestigious private school where only the best of the best were enrolled."
    ima "So what you’re saying is that you’re the...worst of the best?"

    scene wakanabeachdrunk6
    with fade

    w "Uhhhhhhhh fuck you. I’d rather win nothing at all than be voted a clown by a jury of peers. Also, fuck you again. "
    ima "Damn, I just got fucked twice in the same line."
    w "First two times in seven years, {i}bitch.{/i} You can thank me later."
    s "Wakana, how drunk are you? I’ve never seen you speak like this before."
    w "I’m not drunk, I’m {i}high.{/i} Alcohol has no effect on me. But apparently taking it with this new medication {i}does.{/i}"
    os "I {i}did{/i} tell you not to do that."
    w "Now we know for next time. And hey, if I wind up in the hospital again, maybe Arakawa will actually come visit me this time, you fucking {i}douche.{/i}"

    scene wakanabeachdrunk7
    with fade

    ima "Ay! Don’t go calling my senpai a douche! He’s awesome and great and kind and I’m only sorta mad that he hasn’t boned me yet!"
    w "Arakawa, you had all day and you {i}still{/i} haven’t screwed Imani? What were you even doing? Playing cards?"

    scene wakanabeachdrunk8
    with dissolve

    ima "Oh! We should play cards! We should play a drinking game!"

    scene wakanabeachdrunk9
    with dissolve

    ima "We should play the King’s Game!"

    scene wakanabeachdrunk10
    with fade

    os "That game...does not involve cards, Imani."
    w "{i}And{/i} there’s no point in playing it when we already know I’m the fucking {i}queen.{/i}"
    ima "Don’t care! Let’s play!"
    os "How? We don’t have chopsticks either."
    ima "Beats the fuck outta me. Senpai, let’s go collect seashells and then you can, like...hold them in your hand or something and let us try to pick the big one. I don’t know! I want to play!"
    s "I never should have given you two half of my beers. "

    scene wakanabeachdrunk11
    with dissolve

    w "I vehemently disagree."
    os "Wait a second — half of the first batch or half of the batch we went and picked up afterwards? Because I gave Wakana a couple of mine the first time but then quickly learned my lesson and stopped."
    s "Yes. Well, you’re a much better learner than I am. And I also didn’t realize it was even possible for her to get like this."
    ima "King’s Game! King’s Game! King’s Game!"

    play sound "static.mp3"
    scene wakanabeachdrunk12 with flash
    stop sound

    s "Why do you want to play the King’s Game so badly? Why not play something we actually have the materials for?"
    ima "Because even though I’m half-Japanese, I’ve never gotten to play! I was deprived of all the quirky and fun Japanese drinking games and had to play shit like {i}Stump{/i} instead! It’s not fair!"
    os "What the hell is {i}Stump?{/i}"

    scene wakanabeachdrunk13
    with dissolve

    ima "Okay. So there’s this stump, right? And everybody gets a nail. And there’s a hammer, right? So you, like, flip the hammer, okay? But the hammer’s gotta hit somebody else’s nail. And if it does, boom. Take a shot."
    ima "But then you’ve {i}also{/i} gotta drink if you try to flip the hammer and you miss it, so your hand-eye shit’s gotta be {i}on,{/i} you hear me? Oh, and if the nail gets fully hammered in-"

    scene wakanabeachdrunk14
    with dissolve

    w "I want to play truth or dare!"
    ima "Hey! I ain’t done talkin’ about {i}Stump!{/i}"
    w "I dare Akira to kiss Imani!"

    scene wakanabeachdrunk15
    with dissolve

    ima "I am now done talking about {i}Stump!{/i}"
    os "Wakana...you can’t just keep pressuring them like this."
    w "Fine! Then I dare {i}Osako{/i} to kiss {i}me!{/i}"

    scene wakanabeachdrunk16
    with dissolve

    os "You...do?"
    w "Yeah. Why? You {i}scared?{/i}"

    scene wakanabeachdrunk17
    with fade

    os "We’ve kissed probably ten trillion times. Of course I’m not scared. It’s just a little unlike you to not-"
    w "Drag you into the bathroom first?"
    os "Yeah, exactly."
    w "Nuh-uh! We’ve kissed at the bar before. They’ve seen us. And we can kiss here because they can’t {i}stop{/i} us."

    scene wakanabeachdrunk18
    with dissolve

    ima "I like Wakana’s idea now! I also dare Osako to kiss her! And I’m the king, so you have to do it!"
    w "We’re not playing the God damn King’s Game, Imani! But she’s right. We should make out. Like, together."

    scene wakanabeachdrunk19
    with fade

    os "It would be hard to do that alone, wouldn’t it?"
    w "I don’t know, but Imani might since the man she likes refuses to touch her."
    ima "As the king, I demand that you take that back!"
    s "And as the man, I am also not opposed to seeing the two of you make out."
    w "Waiting on you, kitten. "
    os "Is it really okay?...You’re not still mad?"

    scene wakanabeachdrunk20
    with dissolve

    w "Mad about what? Whatever did you do, Osako? "
    w "Have you been {i}disloyal?{/i} Have you {i}slighted{/i} me?"
    os "Never...and I don’t know if you’re just way more drunk than I thought, but...earlier in the shower, you said-"
    w "For tonight, we shall live in the moment — lest the troubles of the daytime grind these weathered bones to dust."
    os "Uh...is that, like...{i}from{/i} something?"
    w "My mouth. You might be familiar with it from “that place your tongue is supposed to be.”"
    os "You’re ridiculous..."

    scene wakanabeachdrunk21
    with dissolve2

    os "Chu..."
    w "Mm..."
    ima "Boooooo! That ain’t a kiss! That’s-"

    scene wakanabeachdrunk22
    with dissolve

    w "Ahn~"
    ima "Oh, okay. That’s better."

    scene wakanabeachdrunk23
    with dissolve

    ima "That’s worse."

    scene wakanabeachdrunk24
    with fade

    w "Mmf...mlm...mmnh~"
    os "Mmnch.......Wakana.....I love you....."
    w "Shut the...fuck up...and keep kissing me!"
    ima "..."
    s "..."
    s "Should we maybe, like...leave them alone for a little while to get whatever this is out of their system?"
    ima "..."
    s "..."
    s "Imani?"

    scene wakanabeachdrunk25
    with dissolve

    ima "..."
    s "Uhh..."
    ima "Medɔ wo."
    s "..."

    scene wakanabeachdrunk26
    with dissolve

    ima "..."
    s "I still don’t know what that means."
    ima "Look it up...jerk..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene wakanabeachdrunk27
    with dissolve2

    w "And with that, my dare has been completed. Hopefully Arakawa has learned something."
    s "I’ve learned that both of you are very...{i}passionate{/i} kissers but, other than that, not really."
    w "We used to do other things very passionately as well. But alas, this poor broken body just doesn’t do it for Osako anymore."

    scene wakanabeachdrunk28
    with dissolve

    os "Now, hold on. You know damn well that’s not-"
    w "I’m not sure {i}what{/i} I know anymore. Both due to the confusion stemming from words we’ve exchanged privately and the fact that I am fucking {i}tweaking{/i} right now."

    play sound "static.mp3"
    scene wakanabeachdrunk29 with flash
    stop sound

    w "So hey, let’s keep daring these two to get it on instead of worrying about me or {i}us.{/i} They won’t be able to refuse if we join together in our verbal assault."
    os "I’d prefer {i}not{/i} to? I kind of want to talk more about what you just said."
    w "All we’ve fucking done is {i}talk{/i} lately. You’ll have to {i}do{/i} something if your goal here is to {i}sway{/i} me. Especially since words are hard. How many beers do we have left?"
    ima "Wakana, it’s time to face the facts! Senpai’s {i}never{/i} gonna screw me. I’ve got more of a chance of joining you and Osako for a hot lesbian threesome at this rate."
    w "Hahah! It’s funny you mention that, because earlier-"

    scene wakanabeachdrunk30
    with dissolve

    os "Wakana!"
    w "..."

    scene wakanabeachdrunk31
    with dissolve2

    os "..."

    "There’s a moment of silence, but all I can hope is that it’s not the type that succeeds the death of someone or something."
    "There are only so many cracks a bowl can handle, you know."

    os "Let’s go for a walk."
    w "..."

    scene wakanabeachdrunk32
    with dissolve2

    w "Yes..."
    w "Let’s do that..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "I think I saw tears in her eyes, but I can’t be sure. She was gone too quickly."
    "That’s how it always works, doesn’t it?"

    ima "{i}Hah...{/i}"

    "Imani and I remain behind on a beach full of beer cans — a bonfire blazing before us. And as we gaze into it in an attempt to find the right words to break the silence, I wonder if we see the same thing."
    "We probably do. We {i}normally{/i} do."
    "But she’ll interpret it one way, and I’ll interpret it incorrectly."
    "As I detach my eyes from the fire, I remember something...and I immediately hate myself for it."
    "I let my friend get lost at sea. "
    "The current reeled her in."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ wakanaspring2 = True

    jump imanispring1

label wakanaspring3:
    scene sky
    with dissolve2
    play music "comfort.mp3"

    "I’m wide awake, it’s morning — and while the clouds are here to greet me, joined by the light and the wind, I fight them away and embrace my role as everyone’s favorite half-tangible parasite."
    "Today, I will find a host. I will burrow into their flesh and take up residence in some hard-to-reach place, living off of {i}their{/i} blood instead of my own because mine scares me sometimes."
    "Sometimes, I feel like there’s more to it than its color. Its viscosity. How I can’t live without it and yet, how knowing it’s there makes my skin try to crawl away."
    "But such a feat is impossible as only ghosts can escape themselves. So while I long for the day where I can roam the halls of the dead, for now I have the clouds."
    "The light."
    "The wind."

    play sound "vibrate.mp3"

    "And a phone call from a good friend."

    scene bedroom_day
    with dissolve2
    play sound "phonebeep.wav"

    s "Hello?"
    w "..."
    s "..."
    w "..."
    s "Wakana? Are you there?"
    w "Arakawa..."
    w "You’re not busy today, are you?"
    s "I mean...{i}I’m{/i} rarely busy at all these days. Aren’t {i}you{/i} normally in school around this time, though?"
    w "It’s Saturday. But I suppose you wouldn’t know that if the days of your prolonged absence have begun to congeal into some indiscernible blob."
    s "I know it’s Saturday. But you’re normally still over there, like...watering your plants or grading papers. Stuff like that."
    w "I don’t have anything to grade right now...and I watered my plants before I left the building yesterday. I can leave them alone until tomorrow."
    s "Okay. So...why are you calling, then? You don’t normally do that unless you need my help with something."
    w "..."
    s "..."
    w "Can you come over?"
    s "To your place?"
    w "That is correct."
    s "You don’t need my help cooking again, do you?"
    w "It’s not like that, I-"
    w "..."
    w "I could just really use the company."
    s "..."
    w "But if you already have plans, it’s-"
    s "No, I’ll head over now. Does that work?"
    w "It doesn’t have to be {i}now.{/i} Any time you-"

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "Nope. Getting dressed and coming over now. You can deal with me when I get there."
    w "Arakawa-"

    play sound "phonebeep.wav"

    "I hang up the phone and throw on the same outfit as always, but I grab an umbrella out of the closet as well since I’d be crazy to not expect rain when the clouds have already turned grey."
    "Surely, that was Wakana’s doing. And surely I shouldn’t question {i}why{/i} when I’ve already learned the reason for the cracks in her sky."
    "But if I’m to keep her out of the rain, which is surely why she needs me now, it’s best that I stay dry."
    "I can’t imagine she’d take kindly to me tracking mud all over her floors."
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene wakanasadapt1
    with dissolve2

    w "Thanks for coming. I can make tea to repay you, if you’d like."
    s "I’m good. But I {i}do{/i} take exception to the implication that you’d only offer me a drink if you owe me something."
    w "I only keep the expensive stuff in here. The kind that would be lost on someone like you. So forgive me for keeping it to myself on most occasions."
    s "You are forgiven. Now, what’s going on?"
    w "I need you to clean my shower. "
    s "Ahh, okay."
    w "And it would be great if you could wash the floors while you’re at it."
    s "Anything else?"
    w "If you could get inside the oven, that would be greatly appreciated as well."
    s "As in...cleaning it? Or literally getting inside of the oven so you can kill me?"
    w "I suppose the former as burning you to a crisp would surely make the oven even harder to clean."
    s "Your wish is my command, Wakana."

    scene wakanasadapt2
    with dissolve

    w "You’re being awfully obedient today."
    s "Yeah, well you’re looking awfully pathetic."
    w "You always look awfully pathetic."
    s "You’re right. Which is precisely why I know to go along with anything you say right now as it probably feels nice to have some power back, doesn’t it?"

    scene wakanasadapt3
    with dissolve

    w "..."
    s "Are you okay?"
    w "No."
    w "And since you’ve managed to figure that out all on your own, I suppose you can forgo all of the cleaning and just...sit with me for a little while."

    scene black
    with dissolve2

    s "Lead the way, princess."
    w "Please don’t ever call me “princess” again — even in the midst of my most miserable days."
    s "Are any of your days better than “miserable?” Because my understanding was that was just the baseline."
    w "And it normally is..."

    scene wakanasadapt4
    with dissolve2

    w "But things have been exponentially worse lately and I...may be having a difficult time getting adjusted to that."

    "Wakana and I take a seat on the couch and she immediately pulls her knees up to her chest."
    "And while this may make it a little harder for me to find a soft spot to burrow into and start living off of her blood, I have faith I’ll figure it out soon enough."
    "But who knows? Maybe if I can get a strong enough taste of whatever she’s feeling from a few inches away, I won’t have to do that at all."

    s "Osako, I’m guessing?"
    w "I heard the two of you went out the other night..."
    s "Wait. You’re not...jealous, are you?"

    scene wakanasadapt5
    with dissolve

    w "What? Don’t be ridiculous. Osako wouldn’t fall for you even {i}if{/i} you had the correct genitalia."
    s "Then why did you sound so forlorn when you mentioned the two of us meeting just now?"

    scene wakanasadapt6
    with dissolve

    w "I wasn’t trying to sound {i}forlorn.{/i} I was just using that as a bridge to...acknowledge that you likely understand what the two of us are going through right now."
    s "I’ve known since the beach trip that things haven’t been perfect. I just don’t fully understand {i}why.{/i} But I guess that’s between you two and not me."
    w "Things have been...{i}imperfect{/i} for several months now. But it wasn’t until after that trip that they...really started to change."
    w "And I guess I’m just...so used to the way they’ve always {i}been{/i} that seeing her trying to better herself has set off something in my brain that’s making me think all of this is wrong."
    s "Well...she made it sound like she was the issue in the first place. Which is why she’s doing all of this to begin with, right?"
    w "She’s not the {i}only{/i} issue. I have my fair share of faults as well. I just worry that...I may have been a little too harsh on her. "
    s "So that’s what this is? Just...general worrying? No earth-shattering revelations or drama for me to help you with?"
    w "Does that come as a disappointment?"
    s "I’d say it’s a relief, if anything."
    w "Yes, well...I wouldn’t be {i}too{/i} relieved if I were you. "
    w "From the outside, I’m sure it’s easy to look at this as the two of us “trying to work through something,” but we’ve worked through plenty of things in the past and it’s never felt like this..."
    w "So...perhaps it’s just the eternal pessimist in me that’s perceiving it as some sort of omen. I hope that’s the case. Regardless, I needed someone to steel my heart for me, so...here you are."
    s "I get it. I’m just surprised you’d trust {i}me{/i} with something like that over Imani."

    scene wakanasadapt7
    with dissolve

    w "Imani has her strengths, and she’s better than you in more ways than I can count. "
    w "But {i}you’re{/i} the one I’m more comfortable with, Arakawa."
    s "Uhh...{i}why?{/i}"
    w "I suppose you just feel like a brother to me. A cousin, perhaps? But I can rest my head on your shoulder like this and feel absolutely nothing."
    s "You have a real gift for accidentally insulting people, Wakana."

    scene wakanasadapt8
    with dissolve

    w "It was a joke, idiot. I don’t feel {i}nothing.{/i} I feel...secure. And as great of a friend Imani is, it never really feels as if she’s {i}watching over{/i} me, you know?"
    s "..."
    w "I’m sorry for being the way I am. You’re extremely special to me."
    s "Maybe be a little {i}less{/i} sorry if possible, though. Because if I have to deal with you {i}and{/i} Osako going through monumental personality changes at once, I’m not sure how I’m going to process it."
    w "I’ll go back to normal shortly. I just wanted to be vulnerable for a little while. And while all logic says I should do that as far away from you as possible, I decided to challenge it."
    s "Okay. But if your girlfriend comes through that door and sees you cozying up to me, you have to explain everything in five seconds or I am very likely going to die."

    scene wakanasadapt9
    with dissolve

    w "I’ll see what I can do."
    s "That doesn’t bode well for my future. But I’ll take it, I guess."

    scene black
    with dissolve2

    w "Arakawa...can I ask you something?"
    s "Nope. I just came over here to eat your food and watch your TV."
    s "I guess I can humor you if you keep it brief, though."
    w "Then..."
    w "I just wanted to know if you’d think any less of me if I forced you to hold me so I can cry into your chest for a little while."
    s "Do I even have the right to refuse? Because you’re already changing positions and-"
    w "Nope. Here I come. Move your legs."
    s "Where? There’s nowhere to go."
    w "Well, figure it out because I’m only a few seconds away from a full-on breakdown and I’d like you to close your eyes for it so you can preserve your image of me."
    s "But the image I have of you sucks."
    w "Then maybe you’ll just have to hate me after today..."

    scene wakanasadapt10
    with dissolve3

    "Wakana quite literally crawls into my lap and finds a place to nestle herself between my legs."
    "When she presses her head against my shoulder, I don’t hesitate to hold her close and stroke her hair."
    "And yes, it...feels a little odd doing this for someone who, for the most part, has always seemed rather stoic. But there have been breaks in that that I’ve experienced over the years."
    "And I know what it’s like to bottle things up for so long that the pressure just becomes too much. So I won’t think any less of her for being a little more human than normal now."
    "I’m just thankful and...{i}surprised{/i} that she’s willing to break in front of me. "
    "For while I might not be good at collecting and reassembling the pieces, I love the way they look when the light hits them just right."
    "For each tear that dribbles down her cheek, I make a wish on her behalf. "
    "I wish for her happiness. I wish that her love survives. I wish that one day, if we can ever make it out of this place, that we can hold each other again somewhere closer to our deaths."
    "But most of all, I just wish for her to stop crying so I can stop coming up with wishes that might never come true."

    w "You’re not holding me tight enough..."
    s "Yeah well, look at how you’re sitting. What do you want me to do?"

    scene wakanasadapt11
    with dissolve

    w "Hold me tighter, idiot! Squeeze the life out of me! I need it!"
    s "You need to be squeezed to death?"
    w "Yes! Haven’t you ever been sad before?! "
    s "Of course. But normally when I wish for death, I do it in a less cute way."
    w "Yeah, well I’m a cute girl and you’re a stupid, terrible, horrible man! Hug me harder!"

    scene wakanasadapt12
    with dissolve

    s "You get really needy when you cry, huh?"
    w "I’m really needy all the time. I just never ask for anything because everyone other than me is incompetent."
    s "Does that mean I have the green light to just hug you whenever I want then?"
    w "Maybe...Not if anyone else is around, though. I don’t want anybody to know I actually really like you."
    s "Yeah, why {i}do{/i} you like me anyway?"
    w "Shut up, Arakawa. This is my time to be sad. We’re talking about me right now. So shower me in compliments until I stop crying. That’s an order."
    s "Uhh..."
    s "You’re...really smart."
    w "More."
    s "You’ve...got a really nice figure?"
    w "More. But less creepy."

    scene black
    with dissolve2

    s "You...smell nice?"
    w "I {i}just{/i} told you to be less creepy! How can you be {i}this{/i} bad at simply hugging someone?!"

    "........."
    "......"
    "..."

    scene wakanasadapt13
    with dissolve3

    "Things carry on that way for another thirty minutes or so before Wakana swiftly tears herself away from me and-"

    w "That never happened."

    "And goes back to being Wakana."

    s "Feel any better now?"

    "Instead of pressing her about it and capitalizing on my free hug pass, though, I skip right to the point. Because, the quicker she feels normal, the quicker things {i}become{/i} normal."
    "And if I’m going to be following Osako on her path to self-acceptance, I don’t want any commentary to lead me down some road less traveled. "

    w "Maybe."
    s "Maybe?"
    w "How have you made it this far into adulthood without knowing how to properly hug someone?"
    s "Probably because my brand of physical affection is best received by people who aren’t already in committed relationships."

    if harukasex == True:
        "Except for Haruka. But I’m pretty sure she wouldn’t have it any other way at this point."

    w "Save it for Imani, you devious disgrace of a man."
    s "Sure. Will you be there to hold her hand again, though? Because that made it really fun last time, didn’t it?"

    scene wakanasadapt14
    with dissolve

    w "I can’t believe I allowed you to see my naked body — even in the throes of a foursome. "
    s "I can’t believe {i}Osako{/i} allowed me to see your naked body. That’s the real surprise here."

    scene wakanasadapt15
    with dissolve

    w "Yeah, that was...{i}odd.{/i} But I suppose it...might have been her first step?"
    s "Not gonna lie, that is one hell of a “first step.” Usually it’s haircut first, foursome second."
    w "Yeah...but that’s another reason why I’m..."

    scene wakanasadapt16
    with dissolve

    w "No, fuck it. No more of this depressing stuff. There’s enough of that to go around already. What {i}we{/i} need is food and alcohol."
    s "Have we already reached that point of the recovery process?"
    w "I demand sustenance, Arakawa. If I am going to spend my day off with the likes of you, I am going to need all the energy I can get."
    s "Fine by me. I skipped breakfast to come here. Is there anywhere you have in mind, though?"
    w "You choose. I’m too hungry to think."

    scene black
    with dissolve2

    s "Okay...I’ve got somewhere in mind."
    s "It’s a bit of a trip, though."

    $ renpy.end_replay()
    $ wakanaspring3 = True
    $ wakana_love += 1

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    jump wakanaspring4

label wakanaspring4:
    if _in_replay:
        play music "comfort.mp3"

    scene wakanaresto1
    with dissolve2

    w "I’m going to be frank with you, Arakawa. Never in a million years did I think you were going to remember this place — let alone take me here of your volition."
    s "Yeah, well...you said it was one of your favorite spots and today is all about {i}you.{/i} I can be surprising every once in a while."

    scene wakanaresto2
    with dissolve

    w "I suppose you can. Color me impressed. So long as that color is black, of course."

    "Wakana seemed rather skeptical when I insisted that we make our way to the train station, but she more or less figured out where we were going once we got off at the Urban District."
    "So yeah, I guess you can say this is me finally being a good Samaritan- {i}especially{/i} when it’s the second time today that I’ve done something positive without asking for anything in return."
    "I imagine most people would just call that something along the lines of “being a good friend,” and to that I’d agree. But here’s the thing — that’s normally not me."
    "I only vaguely remembered where this place was and needed assistance along the final stretch. And even then, I didn’t recognize the shop at first glance."
    "Once we set foot inside, though, it all came rushing back. Which is why I can tell you we’re sitting at the same table we were the {i}first{/i} time we came here."
    "I’m sure this is where she sits with Osako as well. And I’m sure that’s who she’d {i}rather{/i} be sitting with at this very moment."
    "But she’s stuck with me...so I at least owe her a dinner she can stomach in an atmosphere she loves. "
    "And even if I feel out of place, it’s worth it just to see her smile."

    s "Ever think of changing your look up? Maybe trying on something that {i}isn’t{/i} black?"
    w "I have that grey jacket I wear to work. Does that not suffice?"
    s "Grey is just light black."
    w "I’ve always looked at it as more of a dark white."
    s "Either way, I’m talking about light colors. Maybe a nice pink or red."
    w "Sorry, are you a fashion designer now? Because, if you are, I believe you may need to head back to school to learn a thing or two about color matching. "
    s "I think those colors would look just fine on you. I think {i}anything{/i} would look fine on you, really. You’re a beautiful girl."
    w "{i}Woman,{/i} Arakawa. I am a beautiful {i}woman.{/i} The miniature devils I {i}teach{/i} are girls."
    s "Some of those miniature devils are taller than you. "

    scene wakanaresto3
    with dissolve

    w "Yes, but that does naught to fix their elegance for I meant miniature in aura, not height."
    s "Damn. Guess I’ll just have to throw away the bright yellow dress I bought you for your birthday then."
    w "Oh, please. I doubt you even know when my birthday {i}is.{/i}"
    s "No. But if I had to take a guess, I’d imagine it’s just Halloween or something equally fitting."

    scene wakanaresto4
    with dissolve

    w "Close enough. October 10th."
    s "Oh, so right around the corner."
    w "But not {i}so{/i} soon that you don’t have time to exchange your hypothetical dress for something more befitting a goth queen."
    s "Do you actually want a birthday present?"
    w "Would you actually buy me one if I did?"
    s "Depends. Will you buy me one for mine?"
    w "Depends on if I remember. When is it?"
    s "It’s-"
    s "Uh..."

    scene wakanaresto5
    with dissolve

    w "Do you...not remember your own birthday?"
    s "I...don’t think I do."
    w "Just...look at your ID, Arakawa."
    s "I don’t keep it on me."
    w "What? What if you’re stopped by the police?"
    s "I guess I’m going to jail."
    w "I mean, knowing you, you’d be very likely going to jail regardless. But having your ID on you would at least save some time and-"
    s "You know what? Forget the ID and forget my birthday. I’m buying you a present. What do you want?"

    scene wakanaresto6
    with dissolve

    w "Someone else to talk to at work would be nice."
    s "So a set of walkie-talkies for you, Imani, and Rika. Got it."

    scene wakanaresto7
    with dissolve

    w "Arakawa."
    s "Please don’t lecture me. I’ve been so good today."
    w "You have, which is why I’m going to be as gentle as I possibly can."
    w "Either you come back to school by the end of the year, or I butcher you and bury you in your own backyard."
    s "{i}That’s{/i} as gentle as you can be?"
    w "I’m a very violent woman when I’m not in crippling pain. And while I understand that you may have personal issues you need to sort out, I imagine an entire school year should suffice. Should it not?"
    s "..."
    w "Ara-"
    s "It just has to be by the end of the school year?"
    w "If you want to keep your life, yes."
    s "And if I don’t?"
    w "Then I will lace your drink with cyanide and kill you now so I don’t have to worry about you anymore."
    s "You’d have your work cut out for you having to carry me from here all the way to my backyard."

    scene wakanaresto3
    with dissolve

    w "Which is why you should be a dear and just do as you’re told. Love, Wakana Watabe."
    s "Did you just end a sentence like you’d end a letter?"
    w "PS: Fuck you."
    s "You really want me back there, don’t you?"

    scene wakanaresto8
    with dissolve

    w "Complaining to the other girls just isn’t as fun."
    s "I thought you were {i}women?{/i}"
    w "Can you look away for a moment? And also slide your drink a tad closer to me?"

    "I manage to get off easy concerning Wakana’s ultimatum. "
    "Of course I have no problem agreeing to come back by the end of the school year when I know the school year {i}won’t ever end.{/i}"
    "But it’s not like I can just say that since if she {i}doesn’t{/i} interrupt me, she’ll push forward the date instead."
    "So I keep up the pattern-"

    s "Fine."

    "Make a promise I have no intention of keeping-"

    s "I’ll come back by the end of the school year."

    "And narrowly avoid a sin by convincing myself that hiding the truth from someone is different from lying."

    w "Good boy."

    play sound "static.mp3"
    scene imissyoumore with flash
    scene wakanaresto3 with flash
    stop sound

    w "And now to drink myself into a stupor in hopes that I’ll be able to make it home without you carrying me. "
    w "You drink as well, Arakawa. It’s on me. A reward for your rare and repeated excellence today."
    s "Wakana...can I ask {i}you{/i} something now?"

    scene wakanaresto9
    with dissolve

    w "Hm?"
    s "It’s kind of...random, though."
    w "You’re not going to crawl into my lap like I did yours, are you? Because this is hardly the place for that."
    s "Can you tell me about your childhood?"
    w "My childhood? May I at least ask what spurred such curiosity?"
    s "It’s just that..."
    s "I kind of block mine out. And there are certain things that remind me of it that make me want to know if others are-"

    scene wakanaresto6
    with dissolve

    w "Say no more."
    w "It all started when I was in elementary school."

    play sound "static.mp3"
    scene wakanaresto10 with flash
    stop sound

    s "That’s when it {i}started?{/i}"
    w "Is there a problem with that?"
    s "It’s just that...most people’s lives normally start {i}before{/i} then."
    w "Yes, well, you don’t want to sit here for hours as I feverishly recant the memories of my back being cut open and meticulously fiddled with, do you?"
    s "You were {i}awake{/i} for all that?"
    w "No, I- ugh. Can I just start where I intended to start? Or would you prefer I begin writing my memoirs early for the sole purpose of appeasing you?"
    s "Start wherever you want. I’ll stop getting in the way. "
    s "I just want to know if you were happy back then."
    w "Hm..."
    w "I can’t quite remember...but I don’t imagine I was. "
    w "I’ve been rather “gloomy” my whole life, you see. And I imagine it was for that reason no one ever paid much attention to me."
    w "I imagine the Sakakibara girl from your former class would be an apt comparison. But she seems to have found her footing and begun to associate with others in a way {i}I{/i} never really did."
    w "There were those who tried to tease me for the way I dressed...the things I read and wrote...but they gave up and left once they realized it didn’t particularly bother me."
    s "Were you just...too focused on something else back then?"
    w "I believe it would be more accurate to say I just...wasn’t focused on anything?"
    w "I was assuredly an outcast. But I believe at least half of that was due to an overwhelming disinterest in practically everything — with the second half being my inability to physically act as others my age did."
    w "I was, by all accounts, the “weird” girl. But I was one who was mostly left to her own devices so...perhaps {i}that{/i} is why I blossomed into the poetic genius you see before you today."
    s "You don’t have any pictures you can show me, do you?"
    w "Of course not. Who just carries around pictures of their younger self all day?"
    s "Well...you’re all on social media, aren’t you? You don’t have anything there?"
    w "Every picture I have ever posted has been a flower. If anyone would like to see my face, they are free to do so in real life."
    s "You know, maybe you weren’t just the “weird girl” back then because you kept to yourself. Maybe you’re just...genuinely weird."

    play sound "static.mp3"
    scene wakanaresto11 with flash
    stop sound

    w "Maybe. For it was all the same throughout high school and most of college as well."
    w "But again, that never bothered me. People are just...irritating. Especially when they’re that young."
    w "They’re always whining about a need to “connect” with someone...and how it’s {i}so hard{/i} to find people who actually “understand” them."
    w "But when their entire evaluation of a person is decided within the first ten seconds of meeting them, of {i}course{/i} they’re not going to be understood. Connections take time."
    w "Those sorts of relationships where everything just clicks right away without any effort on {i}anyone’s{/i} end just...don’t exist. They’re all made up. Mostly by terrible writers looking to cash in on romance."
    w "Or...at least that’s what I {i}thought.{/i}"
    prof "Next — Osako Osaka, reading “To the River” by Edgar Allan Poe."

    scene wakanaresto12
    with dissolve

    w "Mm?"

    play sound "static.mp3"
    scene wakanaresto13 with flash
    stop sound

    os "Uhh...hi..."
    os "That part’s...not in the poem..."
    os "Just..."
    os "Uh..."
    os "Hi..."

    scene wakanaresto14
    with dissolve

    femstud1 "Hahahaha! Classic Osako! Awkward as always!"
    femstud2 "You got this, Osako! Just do it like you did in the locker room!"
    prof "Miss Osaka...if you’re unprepared for the assignment, please just say so instead of wasting everyone’s time."
    os "I can do it! I can do it."
    prof "Then put the notebook down..."
    os "Can I just...hold onto it for comfort, please? I promise I won’t look."

    scene wakanaresto15
    with fade

    prof "{i}No.{/i} If you’re unwilling to do the assignment as instructed-"
    os "Aaah! Fine! "
    os "Fair river! in thy bright, clear flow...Of crystal, wandering water...Thou art an emblem of the glow...Of beauty—the unhidden heart...The playful maziness of art...In old Alberto’s daughter..."

    scene wakanaresto16
    with dissolve2

    os "B-But when within thy wave she looks...Which glistens then, and trembles...Why, then, the prettiest of brooks...Her worshipper resembles..."
    os "For in my heart, as in thy stream...Her image deeply lies...His heart which trembles at the beam...Of her soul-searching eyes..."
    w "..."

    scene wakanaresto17
    with fade

    os "..."
    prof "..."
    femstud1 "{i}Is she looking at somebody? Why’s she still just standing there?{/i}"
    femstud2 "{i}Watabe, probably. She’s always looking at her. Have you seriously never noticed before?{/i}"
    femstud1 "{i}What? Really? The creepy girl? Why? They’re totally different types.{/i}"
    prof "Miss Osaka, well done. But if that will be all...please take your seat."

    scene wakanaresto18
    with dissolve

    os "S...Sorry! Bye!"

    play sound "static.mp3"
    scene wakanaresto19 with flash
    stop sound

    w "Perhaps there {i}is{/i} some truth to immediately knowing whether or not you’ll “click” with a person..."
    w "Because from that point on, my life has been {i}full{/i} of color thanks to a bashful, yet sensitive jock with a secret affinity for sage and lace. And if I could go back and do it all again, I would."
    w "They can cut me open as many times as they want and I’ll keep looking forward to it because I know what lies ahead. And it’s something unlike anything else in the world."

    scene wakanaresto20
    with dissolve

    w "I apologize if that wasn’t the sort of nostalgic retelling you were hoping for, Arakawa. I have no traumatic tale of neglect or abuse or anything else you could have hopefully connected with."
    w "But I hope with this shriveled, blackened heart of mine that, one day, you will have a moment like I did — where you see someone or something for the first time and think “this is why I’m here.”"
    w "Perhaps you already have and simply haven’t told me. There {i}is{/i} that childhood friend of yours, after all. And many others too. "
    w "I’m not looking to know everything — just what you’re willing to share. "
    w "And I may not have enough happiness for the two of us right now..."
    w "But if I ever do, I hope you’ll take some of it off my hands. "
    w "I can only smile for so long until my face begins to hurt."
    s "..."
    w "..."
    s "Maybe one day."
    w "Maybe, indeed."

    scene black
    with dissolve2
    stop music fadeout 11.0

    "Wakana and I finish our respective meals before she takes out her phone and begins to scroll through every photo she has ever posted to social media."
    "Each one is just as she said — a flower. "
    "But there’s only one that brings me hope. Or joy, if you could call it that."
    "I ask her if she’ll send it to me and she smiles."
    "Then, we take the train back to the first half of town."
    "I carry her for the last block on the way to her apartment, but I probably didn’t have to."
    "When we get to her door, I exercise a brand new right of mine."
    "I imagine it will happen again."
    "Then, I gaze at that photo all the way home."
    "It isn’t why I’m here."
    "But it’s close."
    "I can feel it."

    $ renpy.end_replay()
    $ wakana_love += 1
    $ wakanaspring4 = True

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label wakanaspring5:
    "I can’t show you what I look like. I can’t mimic how she speaks."
    "But I’ll hold your hand and weep with you when tragedy repeats."
    "Because time is sure to take me next — and when it does, don’t fret."
    "Just leave my ashes on display somewhere you won’t forget."

    play sound "static.mp3"
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene wakanathefriend1 with flash
    stop sound
    play sound "imscared.mp3"
    play music "allofthesounds.mp3"

    "{b}{size=+30}I AM VERY SAD{/b}{/size}"
    "But I’m sure you probably get that already since I’ve always been sad and have gone through various phases in which that sadness is heavier then normal. Like when I raped Molly or killed Maya."

    play sound "ohshitpartytime.mp3"
    scene wakanathefriend2

    "{b}{size=+10}THIS IS ANOTHER ONE OF THOSE TIMES{/b}{/size}"
    "Just this time probably won’t last as long because I’ve got battle-hardened skin now and could stop a truck with my cock-flesh if it approached me at top speed during sex."
    "{b}{size=+20}TODAY, I TAKE THE TRASH OUT{/b}{/size}"
    "It’s why I got out of bed. They call it “responsibility” in other parts of the world (the ones I will never see) ///Weebnote/Godnote: “World” in this context is in relation to the world not the World."

    play sound "rimshot.mp3"
    scene wakanathefriend3

    "it looked something like this (get it haha wrong image still relevant so DEEP)"
    "The takeout menus are still on the table from when Niki left for the beach and one of Ami’s socks is in the dryer. I can’t bring myself to move either."
    "{b}{size=+20}THERE IS NOTHING ON TV{/b}{/size}"


    stop music
    play sound "static.mp3"
    scene lr_day with flash
    stop sound
    play music "lifeismostlygood.mp3"

    "Okay, I’m good now. "
    "Just needed to get that out of the way really quickly before I make a phone call to redeem a friendship coupon."
    "The bright side of everyone leaving me is that I can pretty much bring anyone I want over here now without risking getting in trouble. Maybe."
    "Technically, Niki {i}could{/i} come back at any moment and pretend she still loves me as more than just a stray dog she made the mistake of taking in. "
    "Just she hasn’t yet. She’s been gone for a while. And I’d be really worried about her fucking some other guy if she knew any and all of them weren’t up in space dying from asphyxiation or whatever."

    play sound "phonebeep.wav"

    "Anyway, phone time."
    "I tap on Wakana’s name in my phone and-"

    play sound "phonebeep.wav"

    w "{i}Hello?{/i}"

    "Oh thank god."

    s "Hey. So remember that time you were really miserable and needed me to come over so you could cry into my shoulder and make me buy you dinner?"
    w "{i}I’m sorry, but I think you have the wrong number. Please don’t call here again. Goodbye.{/i}"
    s "Wakana, I could really use your company. "
    s "I’ve been standing in the middle of my living room staring at the floor for I think thirty minutes now. And I imagine that is what I will do for the rest of the day if you don’t come snap me out of it."
    w "{i}Oh good. We can be miserable together then. I’ll shower and head over in twenty minutes.{/i}"
    s "Great. But I get to be the more miserable one today since you had your turn already."
    w "{i}Okay. But that doesn’t mean I won’t be silently competing with you in my own head.{/i}"
    s "I also expect a hug."
    w "{i}Jesus, Arakawa. Are you fucking dying?{/i}"
    s "No. I just miss you and you smell nice and no one touches me in this house anymore."
    w "{i}Perhaps I’ll bring a ball-gag as well if it’ll get you to stop this infantile whimpering.{/i}"
    s "Can I make you wear it instead? "
    w "{i}Will that make you feel better?{/i}"
    s "Probably, yeah."
    w "{i}Then no. See you in half an hour.{/i}"

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "Wakana hangs up the phone and I know that these thirty minutes will pass by in no time at all since I’ve already been standing here for that long."

    play sound "static.mp3"
    scene wakanathefriend4 with flash
    stop sound

    "See? She’s already here and I didn’t even have to let her inside. Not locking the door worked out in my favor for once."

    w "Wow, Arakawa. You look terrible."
    s "Do I really? I took a bath this morning and thought I looked mostly normal."
    w "You do. That’s exactly the problem."
    s "Oh. So you’re just being mean again. Got it."

    scene wakanathefriend5
    with dissolve

    w "I didn’t want to shock you by caring so much as soon as I walked in. But, now that I’m here, you can cry if you want and I’ll only make fun of you a little bit."
    s "I don’t need to cry. Or {i}want{/i} to. In fact, I’m not sure I even remember {i}how.{/i} I just knew that being alone wasn’t going to be good for me and-"
    w "And you didn’t have the energy to go visit any of your many fan-clubs popping up throughout the city?"
    s "I can’t tell if that’s in reference to the students or if Nodoka’s book is suddenly getting even more popular."

    scene wakanathefriend4
    with dissolve

    w "I’ve been meaning to read that. Nagasawa is quite talented despite being utterly unbearable in practically every other way."
    s "Don’t. Just hug me instead. I am ready."

    scene wakanathefriend5
    with dissolve

    w "Why stop at a hug when you can have something even better than that, Arakawa?"

    scene wakanathefriend6
    with fade

    s "..........."
    s "What?"
    w "After all you’ve done for me in {i}my{/i} times of need, I think it’s only fair that I go the extra mile for you today. Don’t you agree?"
    s "Uhhhhhhh...yes? "
    s "But..."

    scene wakanathefriend7
    with fade

    w "But what?"
    s "Saying that while you’re tying your hair back makes it {i}kind{/i} of look like you’re about to steer this “friendship” in a whole new direction that I was not expecting to happen so suddenly."
    w "I am. But as you know, I have very little experience doing this, so I can’t imagine I’ll do very well. "
    w "I suppose all that matters is that {i}you{/i} enjoy it, though. So I’ll try my best even if I hate every second of it."
    s "What...What about Osako? Is she, like...{i}okay{/i} with this?"
    w "She doesn’t know I’m here. And I’d prefer you keep it a secret as well since things are already somewhat confusing between us."
    s ".........."

    scene wakanathefriend8
    with dissolve

    w "Why the fuck are you acting so weird? Just let it happen."

    scene wakanathefriend9
    with dissolve

    s "I mean...if you say so."
    w "Arakawa? What are-"

    play sound "zipper.mp3"
    scene wakanathefriend10
    with dissolve

    w "Oh, for fucking- no! Put it away. I’m going to {i}cook{/i} for you, you devious piece of shit. Not do {i}that.{/i}"
    s "Oh..."

    play sound "zipper.mp3"
    scene wakanathefriend11
    with fade

    s "{i}Hah...{/i}"
    s "I knew it was too good to be true."
    w "You’re a filthy, pathetic degenerate. But at least your misery isn’t great enough to kill your libido. I’d say that’s a step forward."

    scene wakanathefriend12
    with dissolve

    s "In my defense, you almost word-for-word recreated one of the best dreams I’ve ever had there. I can’t be blamed for giving into the fantasy when I’ve wanted it for so long."

    play sound "static.mp3"
    scene wakanathefriend13 with flash
    stop sound

    w "Is that really something you should be telling me while I’m holding multiple knives?"
    s "No. But you weren’t holding them one CG ago, so I don’t think I can be blamed for that either."
    s "Also, when did you learn how to cook? Because I’m pretty sure you burned soup the last time I watched you try."
    w "Only because your instructions were horrendous. And also because I can’t cook."
    s "I feel like one of those things implies that you probably {i}shouldn’t{/i} cook today either then. Especially since you didn’t even bring any ingredients."
    w "I just planned on using whatever you had available. And if I couldn’t find anything, I figured I’d just shave off a piece of you instead and throw that over an open flame."
    s "I may be disgustingly self-absorbed, but I don’t think it goes as far as wanting to eat myself."
    w "Then fetch me three ingredients of your choosing. No more than that. Less is okay, though. I need to start small if I am ever going to improve."
    s "Wakana, I appreciate the sentiment. But, as miserable as I am, I don’t think I want to die today. And for that reason, I am unable to try your cooking."

    scene wakanathefriend14
    with dissolve

    w "It wasn’t so much the food that I was expecting you to enjoy, but the act of watching me fail at something since it is so exceedingly rare as I am already better than you at everything."
    s "Now that you mention it, that {i}does{/i} sound exciting. I’m not really sure it’s going to cheer me up, though."
    w "Well, what do {i}you{/i} suggest then? And don’t take that as an opportunity to unzip yourself again as I will not be found liable if I accidentally cut it off."

    stop music
    play sound "static.mp3"
    scene wakanathefriend15 with flash
    stop sound
    play music "samhain.mp3"

    w "A movie and junk food — what an {i}ordinary{/i} suggestion from someone I nearly had to castrate just a short while ago."
    s "This is what I’d normally do with Ami and Niki when they didn’t hate my guts. I’m just trying to breathe some sort of normalcy back into this place."

    scene wakanathefriend16
    with dissolve

    w "Since when does Arakawa Jr. hate you? The two of you have always been {i}sickeningly{/i} close from what I’ve seen."
    s "I like how you don’t question Niki suddenly hating me. Just Ami."
    w "Well, yeah. That one makes a little more sense to me with how frequently you’re screwing our co-worker in public bathrooms."
    s "If it’s okay, I’d rather not get into the specifics of it. All you really need to know is that Ami left and Niki broke up with me."
    w "I see..."
    w "{size=-1}Now, is this a situation where you’d like me to be on {i}your{/i} side and trash-talk the two of them? Or would you rather, in true Arakawa fashion, have me belittle you instead and tell you it’s all your fault?{/i}"
    s "Is there a third option of just silently watching a movie together and maybe falling asleep on the couch?"
    w "There {i}could{/i} be if I didn’t actually care. But knowing you went out of your way to ask me here makes me think just sitting in silence together isn’t going to be very helpful in the long run."

    scene wakanathefriend17
    with dissolve2

    s "..."
    w "I won’t think you’re “weak” if that’s what you’re concerned about. Which I imagine it is since I was concerned about the same thing."
    s "I already know I’m weak...I can talk about that no problem. It’s everything {i}else{/i} that trips me up."
    s "It’s hard telling someone a story when there are a million details you need to omit and the ones left over make everything sound way too simple."
    w "You’re a writer. I’m sure you can figure it out."
    s "See...that’s the thing, though. I {i}can’t.{/i} "
    s "{size=-1}And that’s just one more reason I chose poetry as my field of expertise since you don’t always {i}need{/i} to tell a full story with that. You can normally just throw out a bunch of dots and have people connect them {i}for{/i} you.{/size}"
    w "You do know I’m quite adept at connecting those dots, don’t you? And still very interested in reading something of yours."
    w "Just explain things to me in the simplest way {i}for you{/i} and I can assure you I will only judge you a {i}little{/i} bit."
    s "You’re {i}always{/i} trying to get me to write, Wakana...no matter {i}what{/i} the situation is."
    w "Indeed. I am. And I’d be lying if I said I wasn’t annoyed by the fact you’ve never {i}budged{/i} on that and have elected instead to just do nothing whenever you’re feeling down instead."
    w "You’ve got a perfectly good outlet waiting for you that you won’t even {i}attempt{/i} to use. It’s like you’re some sort of mental masochist or something."
    w "Writers {i}need{/i} to write. That’s how we’ve learned to feel. You {i}not{/i} doing that even when I’m pushing you to is like making me watch you set yourself on fire. "
    w "And I really hate that, Arakawa. I don’t want you to suffer more than you already have."
    s "Writing {i}is{/i} suffering though, Wakana. How am I supposed to do that when all it does is remind me of what I’ve lost?"

    scene wakanathefriend18
    with dissolve2

    w "..."
    s "..."
    w "..."
    s "Are you gonna say something? Or is that the end of this conversation?"
    w "Frankly, Arakawa — I’m not sure what I’m {i}allowed{/i} to say at this point when you’ve already threatened our friendship over this subject before."
    w "Like I said, I’m good at connecting the dots. But when I’m told to {i}stop{/i} doing that and you try to {i}push{/i} me to, I can’t help but feel a little trapped."
    s "Then, if I lift the embargo on talking about what I’m sure you’ve {i}already{/i} figured out...will {i}that{/i} get you to stop trying to make me write?"

    scene wakanathefriend19
    with dissolve2

    w "No..."
    w "But it’ll make {i}me{/i} happy knowing you trust me enough to talk to me about it."
    s "It’s never been about {i}trust.{/i} It’s about not wanting to feel like there’s a bomb inside of me just waiting to go off."
    w "And it’s really the way you felt about {i}her{/i} that’s causing that? Not...what {i}happened?{/i}"
    s "You wouldn’t understand."
    w "Arakawa, barring your niece or daughter or whatever you want to call her, I’ve read the Girl Who Cannot Breathe more than probably anyone you know. Do you know {i}why?{/i}"
    s "Because you’re nosy and obsessed with weird poets?"
    w "Because it’s the only way I can learn more about you when you won’t {i}tell{/i} me anything. "

    scene wakanathefriend20
    with fade

    w "And I guess maybe I’m a little nosy too...but only because I care."
    w "And I imagine you’d do the same thing if you found out I had a secret romance with an older man as a child."
    s "You concede that it was romance, then?"

    scene wakanathefriend21
    with dissolve2

    w "..."
    s "..."
    w "From a moral standpoint, no..."
    w "But I’m willing to acknowledge that no third party can {i}ever{/i} truly understand the feelings two other people have for each other."
    w "And between what I’ve read from her work and how greatly her existence impacted you...it’d be foolish to not acknowledge the existence of some form of love there."
    w "It makes me a little sick to my stomach, though...the Boy, or...{i}you,{/i} since I guess we’re finally addressing this is..."
    w "Well...he always appears so...{i}helpless...{/i}and innocent in her poetry. Like he didn’t fully understand what was going on. Which, given how old you must have been..."
    s "It was true at first."

    scene wakanathefriend22
    with dissolve2

    s "I idolized her...Thought she must have been some sort of angel. So when she wanted to spend more time with me, I happily obliged."
    s "I’d have accepted anyone back then...and I’m just lucky it was someone who {i}really{/i} seemed to care about me."
    s "So when it got sexual, I never really...tried to stop her. Not seriously, at least. Especially knowing that doing so would likely form a rift in the only {i}good{/i} relationship I ever had."
    s "I just didn’t want to lose her. And the more time we spent together, the more I realized just {i}how{/i} important she was to me. Or...{i}is.{/i}"
    s "I can still see her sometimes. Smell her. And...you know, it’ll sound weird, but I can almost feel her hanging over my shoulder every time I pick up a pen. Correcting me...making suggestions."
    s "I just...I want to avoid that because it hurts too much. And I thought that might change when I stopped holding back the memories, but...no luck."
    s "So now here I am, miserable again with no way to express it, and the ones I’ve held closest suddenly giving up on me. "
    w "I haven’t given up on you, Arakawa. "
    s "I could make you if I wanted to...and it’d be really easy."
    w "Try me."
    s "No...That’s how easy I know it would be."
    w "What would make you feel better then? Right {i}now.{/i} Apart from a blowjob."
    s "I don’t know...handjob, maybe?"

    scene wakanathefriend23
    with dissolve

    w "Arakawa, be serious. I came here to try and help you and I feel like all I’ve done is make things worse. "
    s "You haven’t made anything worse. I’ve been trying to be more open about stuff and...I know how badly you wanted to talk about this, so I kind of expected it to happen soon enough."
    s "But right now, I..."
    w "...You, what?"
    s "Don’t make fun of me, okay?"
    w "I’ll do my best."
    s "..."
    w "..."
    s "I just want Ami to come home."

    scene wakanathefriend24
    with dissolve2

    w "..."
    s "I’ve really fucked her up, Wakana. "
    s "I’m sure I don’t need to tell you how hard it would be growing up with {i}me{/i} as a father. "
    w "Probably not as bad as you think if you feel that strongly about her. That was the most human thing I’ve ever heard you say."
    s "You’ve seen her in school, right? Does she seem normal?"
    w "I’ve seen her in the halls, but I haven’t {i}talked{/i} to her."
    w "I {i}could,{/i} though...I should be able to free up some time in my schedule."
    w "And, in the event that I do, is there anything you’d like me say? Any sort of {i}message{/i} you’d like to convey?"
    s "Just tell her I’m sorry."
    w "{i}Are{/i} you sorry? For whatever it is that happened and forced the two of you apart?"
    s "Not really. But I’m not above lying if it makes my life a little easier."

    scene wakanathefriend25
    with dissolve

    w "Oh? Do you ever lie to {i}me?{/i}"
    s "Probably. I can’t really think of any examples off the top of my head though."
    w "Guess I’ll have to look out then. "
    s "How about you, Wakana? Do you ever lie to {i}me?{/i}"

    scene wakanathefriend26
    with dissolve

    w "Mhm. All the time."

    scene wakanathefriend27
    with dissolve

    w "Like you said...makes life easier."
    s "Guess I’ll have to look out too, then."
    w "Don’t look {i}too{/i} hard. You might not like what you see."
    s "I don’t know...I feel like I could look at you all day and like every second of it."
    w "Suspicious thing to say right after telling me you habitually lie to me all the time."
    s "Did I say “habitually?” Because I’d like you to think my lies are much more rare than that."
    w "And I’d like you to stop staring at me..."
    w "It’s making me sick."

    scene black
    with dissolve2
    stop music fadeout 10.0

    s "Fine. Guess I’ll finally put a movie on now that my sob story is over."
    w "And with a lot less crying than mine. Color me impressed, Arakawa. I brought a handkerchief for you and everything. I was really hoping for tears."
    s "Maybe next time. Any Netflix suggestions?"
    w "Mmm...don’t hate me. Dead Poets Society."
    s "Get out of my house."

    $ renpy.end_replay()
    $ wakanaspring5 = True
    $ wakana_love += 10

    "{i}Wakana’s affection has increased by 10!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label wakanaspring6:
    scene wakanaamioffice1
    with dissolve2
    play music "10c.mp3"

    "It was lunchtime at Kumon-mi High, which meant Ami Arakawa was going to go sit in the classroom and wait for it to be over."
    "She didn’t {i}need{/i} to. No one really {i}hated{/i} her and her friends still existed. But she was going to anyway because it just never felt right being around them anymore."
    "And while her definition of “right” is clearly different from ours as evidenced by her place on the forced orgasm leaderboard, it’s still important that we respect her outlook and decisions."
    "Even when those decisions wind up pushing more people away. "
    "But does she get that from her father? Or does {i}he{/i} get it from her?"
    "It’s an interesting question, I think. But one that won’t be answered today as there is a new elephant in the room."
    "And this one smells like earl grey."

    w "Oh, Arakawa Jr."

    scene wakanaamioffice2
    with dissolve

    a "Hm?"

    scene wakanaamioffice3
    with fade

    w "How convenient. I just stepped out my office to come look for you and I’ve barely made it ten feet. Perhaps god is real after all?"
    a "You’re looking for {i}me?{/i} Why? Did I do something wrong?"

    scene wakanaamioffice4
    with dissolve

    a "Wait — I’m not being transferred, am I? Because I know I’ve failed my last three quizzes, but I can promise you that there is a perfectly reasonable explanation for that. "
    a "I am dumb."
    w "You’re not being transferred, Arakawa Jr. Though, this information will help me once again assert my superiority over Miss Imai, so thank you for that."
    a "Well, if I’m not being transferred and I’m not in trouble-"
    w "Technically, I never said you’re not in trouble."

    scene wakanaamioffice5
    with dissolve

    a "Well, what did I do then?! You never come up to me and it’s scaring me based on what I’ve heard about you as a teacher! "
    w "Just come with me to my office and we can talk more about that, okay? I promise I won’t inflict any harm upon you."

    scene wakanaamioffice6
    with dissolve

    a "I don’t know if I believe you after the whole janitor murder court case thing, since it wasn’t very clear if that was actually a real thing that happened or not."
    w "Well, if it {i}was,{/i} it’s not as if we actually {i}need{/i} them since all of you are perfectly capable of cleaning the school yourselves."
    a "You don’t have to remind me. I’m on cleaning duty today. "
    w "I can get you out of it...for a price."

    scene wakanaamioffice7
    with dissolve

    a ".......Oh. "
    w "Why are you blushing? Don’t blush. Stop that."

    scene wakanaamioffice8
    with dissolve

    a "I should have known the moment you asked me to come to your office. I just never realized you thought of me that way...but I guess it’s fine so long as it gets me out of cleaning duty."
    w "I swear, both you {i}and{/i} your father are the same brand of infuriatingly suggestive. What a terrible combination the two of you make."

    scene wakanaamioffice9
    with dissolve

    a "You can do whatever you want to me in your office, but can we please not talk about him? It’s kind of a sore spot right now."
    w "I know. That’s specifically {i}what{/i} I want to talk to you about."

    scene wakanaamioffice10
    with dissolve

    a "Oh!.......So you {i}don’t{/i} want to tie me up then?"
    w "No! And just joking about such things could cost me my job, so shut your delinquent mouth and just follow me to my office already!"

    scene black
    with dissolve2
    play sound "footsteps.mp3"

    a "I doubt it could cost you your job, Miss Watabe. Far worse things have been both said {i}and{/i} done in this school."
    w "What do you mean “done?” What do you know that I don’t?"
    a "A lot, I imagine. But I’m not trying to get anybody in trouble, so- woah!"

    scene wakanaamioffice11
    with dissolve2

    a "Your office is so much nicer than my dad’s...I mean Sensei’s. I never know what to call him in school."
    w "You can call him your husband for all I care. Titles hardly make a difference now that no one can listen in on our conversation."

    scene wakanaamioffice12
    with dissolve

    a "Okay. Well, since you insist, I guess I’ll just have to call him my husband for the duration of this talk. "
    w "I assumed you wouldn’t take that literally given your relationship with him is that of family, but I understand this one might be on me as I deluded myself into thinking you would know better."
    a "If it makes you happy, you can also refer to him as your husband, Ms. Watabe. Or shall I say — Mrs. Arakawa?"
    w "You shall not. Ever again."

    scene wakanaamioffice13
    with dissolve

    a "Oh, come on. You know you’ve thought about it. {i}Everybody{/i} has."
    w "That’s because everyone but me is an idiot. "
    a "You don’t like him even a little? Really?"
    w "I didn’t bring you here to solicit a date with your father-uncle-thing, Arakawa Jr. I’m more than capable of asking him out myself if I ever give up on the idea of happiness. "
    a "Well, why {i}did{/i} you ask me here then? Because you said it was about him. And normally, when someone says that to me, it’s because they want to sleep with him."
    w "I want to talk about {i}both{/i} of you. As a...{i}singular unit.{/i} And try to better understand the situation at home. "
    a "You mean like a guidance counselor?"
    w "That {i}is{/i} technically part of my job here. Though, I imagine I’m supposed to be filling that role for {i}my{/i} students rather than Imaikawa’s."
    a "Did you just combine Imani’s last name into mine? Does this mean I’m interracial now?"

    scene wakanaamioffice14
    with dissolve

    w "No. It means you should take a seat before I need to open a secret drawer in my desk for something to strap you down with. "

    scene black
    with dissolve

    a "Hey, I have one of those too! "
    w "And I’m very happy for you, Arakawa Jr. But again, I am not here to allow you to keep deviating from the topic by tossing disgusting perversions at me."

    scene wakanaamioffice15
    with dissolve2

    a "They’re hardly disgusting if you have a secret handcuff drawer."
    w "That’s not {i}why{/i} they’re disgusting. But I imagine the {i}age difference{/i} between us just doesn’t factor into your head at all seeing as your mother was the Girl Who Cannot Breathe."

    scene wakanaamioffice16
    with dissolve

    a "Oh."
    a "So you’re just {i}saying{/i} it now. Directly to me."
    w "I understand that it’s a touchy subject, but I’m not here to debate the morality of her actions if that’s what you’re worried about. "
    w "She was extremely talented regardless of the things that she did. And she passed that talent down to both your {i}husband{/i} and you. "

    scene wakanaamioffice17
    with dissolve

    a "Oh, please...I’m nothing compared to her. Winning your contest was a fluke."
    a "I wrote a million poems for that and Noriko’s was better than every single one. You only chose {i}me{/i} because you wanted to learn more about my mom."
    w "That may have played some part in it. But I was under the impression you were unable to talk about her. "
    w "Which isn’t even factoring in how Arakawa Sr. told me to stop poking my nose where it doesn’t belong and just stay out of it entirely."

    scene wakanaamioffice18
    with dissolve

    a "But you didn’t...and I’m supposed to believe you went through all of that effort just so you can tell me I’m {i}talented?{/i} What do you {i}really{/i} want, Ms. Watabe?"

    scene wakanaamioffice19
    with dissolve

    w "Heh...that’s a good question. "
    w "I spent so long trying to uncover the relationship between the three of you that hearing it straight from the horse’s mouth felt somewhat...anticlimactic when all was said and done."
    w "I’m not really sure {i}what{/i} to do anymore. "
    a "So am {i}I{/i} the horse? Or is my {i}dad{/i} the horse? Because I assume you talked to him and I assume he’s the one who put you up to this."

    scene wakanaamioffice20
    with dissolve

    w "Is {i}this{/i} what you’re like when the charade drops? The two of you really {i}do{/i} have so much in common, don’t you?"
    a "There is no “charade.” I just try to limit the amount of people who know the specifics of my upbringing since all it does is garner pity and misunderstandings."
    w "Like I said — I’m not here to talk about morality. And I don’t need to read a dead woman’s non-existent autobiography to pity the girl she left behind."
    w "I’m here to remind you that you’re the only piece left of your mother. And that every second you spend away from your “father” is like her leaving all over again."

    scene wakanaamioffice21
    with dissolve2

    a "He...told you to say that?"
    w "Those are my words, not his. We both know how unwilling he is to put actual thought into any of what he says."
    w "I can tell you he’s hurting, though. That he’s {i}sorry.{/i} And that he wants you to come home. Even {i}if{/i} you’re a terror."

    scene wakanaamioffice22
    with fade

    a "{i}Hah...{/i}"
    w "Why did you run out anyway? Just trying to make him feel bad? Did you two get into a fight?"
    a "Is this what {i}you’re{/i} like when the charade drops? {i}Nice?{/i}"
    w "I have my moments, I suppose. And quite frankly, I think your family is rather disgusting. "
    w "But Arakawa Sr. has taken up residence somewhere inside of my heart. And it’d feel wrong to just evict him when he’s already struggling so much."

    scene wakanaamioffice23
    with dissolve

    a "Do you pity him?"
    w "Arakawa? Why? Because he was sleeping with your mother? Or because he’s a completely and utterly helpless excuse for a man?"
    a "The mom thing. Like...there was another older woman who also found out about this recently and her reaction was way different than yours. "
    w "You’re talking about that idol, aren’t you? Niki?"

    scene wakanaamioffice24
    with dissolve

    a "Jesus. How close {i}are{/i} you guys? Just how much did he tell you?"
    w "He mentioned her leaving as well. But I knew the two of them were “together” before that. "
    w "And yes, I {i}do{/i} pity him. For {i}both{/i} of the reasons I mentioned. And I pity {i}you{/i} as well, regardless of how much you apparently want to avoid incurring such a feeling."

    scene wakanaamioffice25
    with dissolve

    a "It’s not even that I want to {i}avoid{/i} it. It’s just...such a {i}normal{/i} thing to me that it’s kind of annoying at this point."
    a "{size=-1}What I want more than anything is to just enjoy what’s left of my life with my dad. That’s all. And how am I supposed to enjoy {i}anything{/i} with people reminding me of how sad we are all the time?{/size}"
    w "You say that like you’re going to die soon."
    a "No, I say that knowing I {i}can.{/i}"

    scene wakanaamioffice26
    with dissolve

    a "Everything can end at {i}any{/i} moment. A meteor could crash into this school right now and we’d all be burnt to a crisp. I could get an aneurysm. I could be {i}murdered.{/i} "
    a "{i}Anything{/i} can happen. So when you spend every waking moment miserable, you’re taking away time from a very {i}finite{/i} amount of happiness available."
    a "Life doesn’t just {i}start over{/i} when you die. That’s {i}it.{/i} You’re done. No more. "
    a "And that’s {i}exactly{/i} what happened to my mom. Before she ever had a chance to show {i}everyone{/i} how amazing she was instead of just the people who met her."
    a "So tell me, Ms. Watabe — if she was so evil like you and all of your pretentious poetry friends think, why did {i}everyone{/i} in her life love her {i}so{/i} much?"
    w "You overestimate the amount of “pretentious poetry friends” I have. Or that I’d want to discuss your mother’s works with them in general."
    a "They’re {i}amazing{/i} though, aren’t they? You said it yourself. She was talented."
    w "Extremely. But there are certain truths in this world that are accepted inevitably, and your mother challenged nearly all of them. Which is precisely what she {i}wanted{/i} to do, so-"
    a "No, she didn’t {i}want{/i} to do that. That’s just who she {i}was.{/i} "
    a "She was {i}never{/i} afraid of being herself and {i}I{/i} can’t even figure out who or what I’m supposed to be yet. "
    a "So no, I didn’t inherit her {i}talent.{/i} I inherited her scorn for a world that didn’t want her here, the infinite blame that accompanies it, and a pair of shoes I can’t ever fill."
    a "Me going home won’t make my dad happy again. It’ll just be more charades. A bandage on a wound that’s bleeding out."
    w "You know...you wouldn’t have to eat alone if you’d just show this side to other people. "
    a "Stop pretending to care about {i}me{/i} just because you care about {i}him.{/i} Everyone always does that and I seriously {i}hate{/i} it."

    scene wakanaamioffice27
    with dissolve

    w "But if I don’t care about you, I won’t get paid. That’s part of my job."
    a "Sure, but...it’s not {i}everybody’s{/i} job and they all do it {i}too,{/i} so..."
    w "Do you think that Niki woman was only {i}pretending{/i} to care about you too, then? Is {i}that{/i} what you two got into a fight over?"
    a "I don’t know..."
    a "She just..."
    a "Being around her causes him pain. And that causes {i}me{/i} pain. So it’d be better if she just left."
    w "You think you two would be happier just ignoring everything then?"
    a "Right...Yeah."
    w "Arakawa told me the same thing essentially. Just {i}he’s{/i} not writing anything down like you are. So I’m sure you understand just how much he’s keeping inside."
    a "He will eventually..."
    a "He just needs time."
    w "But until then, don’t you think it would help him having the one he loves the most by his side?"
    a "Maybe..."
    a "I just doubt if that person’s actually {i}me{/i} sometimes."

    scene wakanaamioffice28
    with dissolve

    w "I know how you feel. Trust me. "
    w "But I also know that Arakawa would not have asked me to try and bring you home if he did not literally {i}need{/i} my help. And I {i}want{/i} to help him because {i}he{/i} helps me. So please-"
    w "Go home. Make him happy. Or...try and fail, I suppose. Just {i}be{/i} there for him."
    a "You know...you’d make a good mom, Miss Watabe."

    scene wakanaamioffice29
    with dissolve

    w "I go this far out of my way to help you and you say {i}that?{/i} I’ve never felt so insulted in my life."
    a "It’s not an insult, I promise. If anything, someone like you might be {i}nice{/i} to have around the house. "

    scene wakanaamioffice30
    with dissolve

    a "A kind-hearted poet who just wants to get the best out of my dad...who won’t judge me for the things I feel or...try to change me into something else."
    w "I will judge you heavily for the things you feel. And I can almost guarantee I’d try to change you as well as I can not even fathom living with a creature like you."

    scene wakanaamioffice31
    with dissolve

    a "Just saying...you’re the closest to my real mom that my dad can get. At least...among those {i}his{/i} age."
    a "And I think you guys would make a really sweet couple if you weren’t already a lesbian."
    w "Uh..."
    w "I’m...bisexual, technically."
    a "Oh. "
    a "Well, maybe there’s hope after all then?"

    scene wakanaamioffice32
    with dissolve
    play sound "footsteps.mp3"

    w "Hope for {i}what?{/i} This is absolutely not how this conversation is supposed to end. I didn’t drag you here to ask for your blessing. Plus, I’m already {i}in{/i} a relationship. Mostly."
    a "Just saying! I might not have ever left at all if you were the one in Niki’s place! "
    w "So you’ll go back then? To Arakawa’s-"

    play sound "dooropen.mp3"

    a "Maybe! Later, Miss Watabe! This was actually a pretty productive talk!"
    w "Wait! Ami-"

    stop music fadeout 10.0
    play sound "doorclose.mp3"
    scene wakanaamioffice33
    with dissolve

    w "..."
    w "Fucking Arakawas..."

    scene black
    with dissolve2

    w "Ending every single conversation by just making me more confused..."
    w "..."
    w "Ugh..."
    w "I want to fucking die."

    "{i}Ami is now {b}PENDING{/b}!{/i}"

    $ renpy.end_replay()
    $ wakanaspring6 = True
    $ wakana_love += 1

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    "{i}You've received a picture message from Karin Kanda!{/i}"

    jump nightch4
