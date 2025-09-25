label pornshop:
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump satnightmenu
    if makoto_love >= 0 and firsttimepornshop == False:
        jump firsttimepornshop
    if makoto_love >= 5 and pornshop5 == False:
        jump pornshop5
    if makoto_love >= 10 and day38 == True and pornshop10 == False:
        jump pornshop10
    if makoto_love >= 15 and makotonew1 == True and makotodorm5 == True and makotonew2 == False:
        jump makotonew2
    if makoto_love >= 20 and makotonew2 == True and day > 4 and day < 7 and makotonew3 == False:
        jump makotonew3
    if makoto_love >= 15 and makotonew3 == True and pornshop15 == False:
        jump pornshop15
    if makoto_lust >= 5 and makotonew3 == True and makotolust5 == False:
        jump makotolust5
    if makoto_love >= 20 and halloween14 == True and pornshop15 == True and pornshop20 == False:
        jump pornshop20
    if makoto_love >= 20 and makotodorm20 == True and pornshop25 == False:
        jump pornshop25
    if miku_lust >= 5 and dormwarsfive14 == True and mikulust5 == False:
        jump mikulust5
    if makotodorm25 == True and hoorayanotherreset == False:
        jump postbluejay
    if chap4active == True:
        jump makotospringporngen
    if chapthreeactive == True:
        jump makotosummer2porngen
    if christmas7 == True:
        jump makotoporngen2
    else:
        jump porn3to4

label makotoinvite:
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump inviteover
    if makotoinvite1 == False:
        jump makotoinvite1
    if makotoinvite1 == True and makotoinvite2 == False:
        jump makotoinvite2
    if makotodorm25 == True and hoorayanotherreset == False:
        jump postbluejaycall
    else:
        jump makotoinvitegen

label postbluejaycall:
    play sound "phonebeep.wav"

    "I tap on Makoto's name in my phone and wait for her to answer."
    "........."
    "......"
    "..."
    "She doesn't pick up."
    "I guess she's busy today?"

    jump inviteover

label postbluejay:
    scene black
    with dissolve
    stop music fadeout 5.0

    "I show up to the porn shop to find that it has closed early."
    "I guess Makoto and Maki are both busy or something."
    "Not sure of what else to do, I decide to head back home and call it a night."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label callmakotomorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump callmorning
    if chap4active == True:
        play sound "phonebeep.wav"

        "I tap on Makoto's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't."

        jump callmorning
    if chapthreeactive == True:
        jump makotosummer2morninggen
    if christmas7 == False:
        play sound "phonebeep.wav"

        "I tap on Makoto's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's still sleeping."

        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I tap on Makoto's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        play sound "phonebeep.wav"

        mak "Good morning, Sensei."
        mak "You're calling early today. Do you need me for something?"
        s "Good morning, Makoto. And yes, I do."
        mak "Okay...Are you going to tell me what it is?"
        s "I would like to see your face."
        mak "Excuse me?"
        s "Your face. It is too far away from me."
        mak "..."
        mak "Did you want to...get coffee or something?"
        s "Yes. That is clearly what I was asking."
        mak "Clearly..."
        mak "Let's meet up at Koi Cafe."
        mak "And please don't bring your dreaded demon of a [niece] or I will walk out."
        s "Sounds good, Makoto. See you soon."
        mak "Yup! See you soon."

        scene black
        with dissolve

        "........."
        "......"
        "..."

        scene makotogenmorning
        with dissolve
        play music "cafe.mp3"

        "I arrive at Koi Cafe and take a seat next to Makoto."
        "The two of us spend the morning talking about[school] and how she should probably be tired of doing my job for me by now, but she just...somehow isn't."
        "I chalk it up to the fact that she's head over heels for me and leave it at that."
        "But I wouldn't be surprised to find out if it was something else."
        "Something deeper."
        "Maybe even something as deep as her life not having any real purpose other than keeping my academic career afloat."
        "Perhaps I should take it easier on her and actually do my own job for once?"
        "Or perhaps I should watch, the same way I always do, as she drowns in her own neuroticism and desire to be something bigger than what she actually is."

        scene black with dissolve

        "Morning leaves before we know it, and we head our separate ways."
        "But at least we got to spend an hour or two away from the things that pain us."
        "Weekends are good."

        $ makoto_love += 1
        stop music fadeout 5.0

        "{i}Makoto's affection has increased to [makoto_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon

label callmakotoafternoon:
    if makoto_love >= 55 and toukaspring3 == True and makotospring1 == False:
        jump makotospring1
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump callafternoon
    if makoto_love >= 55 and mikuinvite2 == True and makotospecial50 == True and makotopool55 == False:
        jump makotopool55
    if chap4active == True:
        jump makotospringnoongen
    if chapthreeactive == True:
        jump makotosummer2poolgen
    if christmas7 == False:
        play sound "phonebeep.wav"

        "I tap on Makoto's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callafternoon

    if makotobeachticket == True and day == 6 and soccer35 == True and mayadorm35 == True:
        jump makotowinterbeach1
    else:
        play sound "phonebeep.wav"

        "I tap on Makoto's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        play sound "phonebeep.wav"

        mak "{i}Hello?...{/i}"
        s "Makoto? Why are you talking so quietly?"
        mak "{i}Because I'm in the library...I can't talk right now.{/i}"
        s "Where are you? You're going to need to speak up."
        mak "{i}I said I'm in the-{/i}"
        s "Makoto? Are you still there?"
        mak "I'm in the damn library, Sen- Ah!"
        mak "Yes. Yes, I know. I'm so sorry. It won't happen again."
        s "The[school] library? I'll meet you there."
        mak "{i}Oh, no. The public library near the maid cafe.{/i}"
        mak "{i}Don't bother coming, though. I have to stu-{/i}"
        s "Cool. See you soon."

        play sound "phonebeep.wav"

        "I hang up the phone and begin to make my way over to the library..."

        scene black
        with dissolve

        "........."
        "......"
        "..."

        scene makotogennoon
        with dissolve
        play music "comfort.mp3"

        "When I arrive, I find Makoto nose-deep in some book about religion."
        "Well, when I say {i}nose-deep{/i} I really just mean she's very invested."
        "If you were to actually attempt to bury your nose inside of a book, it would likely cause you a lot of pain."
        "At the same time, however, the topic she's found herself taking on today would probably cause even more pain if she were to truly get wrapped up in it."
        "Of all the things to waste your time studying, why choose the one thing no one will ever agree on?"
        "There are no gods. There isn't anything other than what's in front of us right now."
        "I tell Makoto this and ask her to put down the book."
        "She calls me an idiot."
        "The cycle continues."

        scene black with dissolve

        "I hang out for a little while longer, watching a strange smile creep across her face as new information finds its way into her brain."
        "It pushes aside other pointless things she has studied-"
        "And contaminates her with the single most deadly poison known to man."

        $ makoto_love += 1
        stop music fadeout 5.0

        "{i}Makoto's affection has increased to [makoto_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight

label callmakotonight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump callnight
    if firsttimepornshop == True:
        "Makoto should be at work right now. I can see her if I go to the porn shop."
        jump callnight
    else:
        "I'm pretty sure Makoto is at work right now...but I'm not really sure {i}where{/i} she works."
        "Maybe I should go look?"
        jump callnight

label makotoporngen2:
    scene makotonightgen2
    with dissolve
    play music "citylife.mp3"

    "I decide to spend the night tormenting Makoto."
    "And by that I mean I just decide to spend the night with her at work."
    "Not wanting to put up with me (Which I completely understand), she decides to spend her time playing that game she showed me a while back."
    "You know, the one with all the fishing."

    if bonus == True:
        "I stop pestering her as I am feeling remarkably generous tonight and, after a while, the two of us are able to carry on a normal conversation that isn't even remotely sexual."
        "That might sound less impressive to you than it does to me, so let me reinforce the idea that I am in a {i}porn shop{/i} right now."
        "Why would I be here if I didn't want to talk about sexual stuff?"
        "This epiphany rings out in my head like a church bell and I slowly but surely transition our wholesome conversation into one about how I'd bang every single girl in the game she's playing."
        "Well, all of them except this one alcoholic nurse."
        "Makoto agrees, but still gets angry either way and yells at me for simply {i}being a human with human thoughts.{/i}"
    else:
        "I tell her she should just git gud if she wants to catch more fish."
        "Makoto agrees, but still gets angry either way and yells at me for simply {i}being a human with human thoughts.{/i}"

    scene black
    with dissolve

    "The night ends with me being kicked out of the shop."
    "But at least I manage to snag a new DVD on my way out of the door."

    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto's affection has increased to [makoto_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotoinvitegen:
    play sound "phonebeep.wav"

    "I tap on Makoto's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    mak "Hello? Sensei?"
    mak "What's going on? Do you need something?"
    s "Need? No. Want? Yes."
    mak "...Is that some sort of code?"
    mak "What do you want from me?"
    s "I want you to come over."
    mak "Then just say that..."
    mak "Thankfully, I'm off tonight."
    mak "Just give me a few minutes and I'll start heading over."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene makotoinvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    mak "Uhh...it feels kind of strange with you just standing there staring at me."
    mak "What do you want to do, exactly?"

    "How should I spend my time with Makoto?"
    menu makotoinvmenu:
        "Hang Out (Raise Affection)":
            jump makotoinviteaff
        "Grinding (Raise Lust)" if bonus == True:
            jump makotoinvitegrind
        "Fingering (Raise Lust)" if bonus == True:
            jump makotoinvitefinger
        "Hug Or Something (Raise Lust)" if bonus == False:
            jump makotoinvitegrind
        "Makoto Deserves A Hug (Raise Lust)" if bonus == False:
            jump makotoinvitefinger
        "Headpat" if bonus == True:
            jump makheadpat

label firsttimepornshop:
    play music "citylife.mp3" fadein 2.0
    scene pornshop1
    with dissolve

    if bonus == True:
        "I decide to check out the local porn shop because...well, it feels a lot more empowering to actually purchase porn rather than just browsing for it online. "
    else:
        "I decide to go to the local DVD store, but quickly discover that it is anything but that and I feel very let down."
        "However, as an adamant supporter of small businesses, I decide to peruse the selection anyway."

    if bonus == True:
        "Besides, I have no idea when the next time I'll have sex is...so this will suffice in holding me over in the meantime."
        "Also, who doesn't love porn? There is absolutely no way this trip could possibly go wrong."

    q "Welcome in. Please take your-"

    scene pornshop2
    with dissolve

    q "Ah?!"

    "A [young_girl] at the front desk calls out to me, but abruptly stops for some reason."
    "I take a quick look around the store to see if maybe she's reacting to someone else but quickly confirm that it must have been something {i}I{/i} did."
    "What, though? I've only been inside for like, five seconds."

    q "We...are closed!"
    s "But the sign outside said you were open for another two hours."

    q "That sign is old! Please leave now!"

    scene pornshop3
    with fade

    "I make my way over to the counter as I'm tired of shouting across the room and the girl immediately shields her face."
    "She looks to be the age of one of my students, so I don't hold it against her for getting embarrassed about working in a place like this-"
    "But she should at least be {i}somewhat{/i} helpful to customers, shouldn't she?"
    "Or...maybe this is another one of those {i}no males around{/i} type of deals that I heard Ami talk about?"
    "If this girl doesn't have any experience helping male customers..."
    "Well, honestly, that just makes me want her help even more."

    q "What...uh..."
    q "What can I...do for you?..."
    s "..."
    q "..."
    s "Wait a minute..."
    q "Of course...take as long as you-"

    scene pornshop4
    with dissolve

    mak "Aah!"
    mak "Un...Unhand me right now! I'll call the cops! I mean it!"
    s "...Makoto?"
    mak "Nope! No Makoto's here! You must be confusing me for someone else!"
    s "You look completely different without your glasses on."
    mak "Never mind my glasses! What the Hell are you doing in here, Sensei?!"
    mak "You know what kind of store this is, don't you?"
    s "I'm actually just stopping by to give you your homework. I looked up your address in the school registry."

    scene pornshop4r
    with dissolve

    mak "Wait...really? But I could have sworn-"

    if bonus == True:
        s "That was obviously a lie. I'm here to buy porn."

        scene pornshop5
        with hpunch

        mak "Can't you just use the Internet for that sort of thing?! That's what everyone else does!"
        s "Can you really afford to be saying that as the employee of a porn shop?"
        mak "No!"
        mak "I mean...yes?!"
        mak "I mean-"
        mak "I don’t know what I mean!"
    else:
        s "Yes. Here you go."

        "I hand Makoto her homework."

        mak "Thank you. That was very kind."
        s "I was unaware that you worked in this establishment, Makoto."
        mak "I am so embarrassed that you are now aware of my workplace."

    scene pornshop6
    with dissolve

    s "Listen, I get that it's probably embarrassing to be seen somewhere like this by your teacher...but I'm not going to hold it against you."
    s "This is your family's business, right? I think it’s admirable that you're helping out here."
    s "Now, can you please point me toward the teen section?"

    scene pornshop6r
    with dissolve

    mak "That's it. I am going to kill myself tonight."
    s "Oh come on. Isn’t it better to be dealing with me than some random guy?"

    scene pornshop7
    with dissolve

    if bonus == True:
        mak "Honestly?..."
        mak "No. No, this is ten times worse."
        s "This might be shocking news for you, but teachers watch porn too."

        scene pornshop7r
        with dissolve

        mak "That doesn't mean I have to be okay with it!"
        mak "Now that you know I work {i}here{/i} it...it changes everything!"
        mak "I'm supposed to be the diligent one! The one who always follows the rules and...doesn't sell vibrators five nights a week!"
        s "You can be whatever you want to be. If selling vibrators empowers you, I'll even buy one. Right now."
        mak "For what?! Stop making this even weirder for me by being okay with it when it is obviously very, very wrong!"
    else:
        mak "I mean...I'd prefer to not be dealing with either..."

    s "For what it's worth, it wouldn't make any difference to me if you worked here or some fast food restaurant. A job is a job and you just happened to wind up with this one."

    scene pornshop6
    with dissolve

    mak "Well...thank you, Sensei. That's-"
    s "In fact, I implore {i}more{/i} girls your age to work in places like this. Because not only would it bring more customers in, it would help-"

    scene pornshop8x
    with dissolve

    mak "Okay, you know what? Just...pick something and get out. It's clear that arguing about this is going to somehow negatively affect our relationship, and I would very much prefer to not do that."
    s "Great. So what do you recommend?"
    mak "..."
    mak "Huh?"
    mak "Me?"
    s "Yeah. What’s the big ticket item here? What should I buy?"
    mak "You’re...asking me for recommendations?"
    s "Yeah. You're the porn expert, aren't you?"

    scene pornshop6
    with dissolve

    mak "My mom is the expert...I just kinda...you know..."
    s "Ahh. So you're just a porn {i}hobbyist.{/i}"

    scene pornshop8x
    with dissolve

    mak "No...I am a normal girl."
    s "Normal girls watch porn and you shouldn't be ashamed to admit that you do too."

    if bonus == True:
        mak "It’s not that I {i}don’t{/i}...it’s just not something I planned on talking about to {i}you.{/i}"
        s "But it's the first thing we've realized that we have in common with one another."

        scene pornshop7r
        with dissolve

        mak "We have plenty of other things in common! We're both intellectuals! We both wear glasses! We both-"
        s "Have a series of tags we gravitate toward when we're alone in our rooms. I understand you."

        scene pornshop8x
        with dissolve

        mak "No, I really don't think you do..."
        s "Listen, your secret’s safe with me. Don’t worry. Just give me a recommendation and I’ll be on my way."
        s "After that, we can forget this little meeting ever happened."

        "That obviously isn't true. I plan on coming here all the time."
        "I'm just not going to let Makoto know that since I don't {i}actually{/i} want her to kill herself tonight."

        scene pornshop6
        with dissolve

        mak "Umm..."
        mak "Well...I...kind of need to know what...sort of things you're into to be able to recommend anything..."
    else:
        s "I watch all kinds of stuff. They used to call me the {i}stuff watcher{/i} back in college in between all of those times where they'd shove me into lockers."
        mak "..."
        mak "Can you at least tell me...some of the stuff you're interested in so I can make a recommendation?"

    if bonus == True:
        s "Are you asking me what turns me on right now?"
        mak "I...guess so?..."
        s "Makoto, I am your {i}teacher.{/i} You can't just ask me things like that."

        scene pornshop7r
        with dissolve

        mak "What is this horrible side of you and why am I just finding out about it now?!"
        s "I'm just kidding. You can ask me about my turn-ons whenever you want."
        mak "I repeat! What is this horrible side of you and why am I just finding out about it now?!"

        "It looks like I'm going to have to give Makoto a little more info as to what I'm looking for."
        "The only issue is what exactly I'm going to tell her."

        s "Let's see..."
        s "I'm looking for-"

        menu:
            "Mature/MILF Porn":
                s "Do you have anything with mature women?"
                mak "Like...ones around your age? Or...older?"
                s "How much older do you have?"

                scene pornshop8r
                with dissolve

                mak "How much older do you {i}want?...{/i}"
                s "I'm not sure. I've never really thought about it before."
                mak "So you're just...taking a shot in the dark here?"
                s "An educated shot. I know what I'm in the mood for. But I am trusting you to make the final decision."
                mak "..."
                s "..."
                mak "Please never come here again after tonight."

                scene pornshop8
                with dissolve

                "Makoto walks over to a rack near the wall and checks out a few DVDs."

                mak "Umm...Sensei...do you have a preference for...you know...breast size?"
                s "Up to you, Makoto. I appreciate all breasts equally."
                mak "How kind of you..."

                "Makoto searches around for another minute or two before eventually returning to the counter without anything in her hand."

            "Student/Teacher Porn":
                s "Do you have anything involving a teacher and a student?"

                scene pornshop9
                with dissolve

                mak "Involving what?!"
                s "A teacher and a student. Or students. No more than ten, though."
                s "Oh, and if you can find any with glasses, that would be much appreciated."
                mak "There is...absolutely no way you don't understand how this sounds!"
                s "Oh, I know exactly how this sounds. I'm just interested in seeing how you handle this revelation."

                scene pornshop9r
                with dissolve

                mak "What is happening to my life all of a sudden?"
                s "Oh, come on. This is a totally normal thing for someone in my position to fantasize about."
                s "Don't pretend you haven't thought about it from the other side of things."

                scene pornshop9r2
                with dissolve

                mak "What goes on in my mind is for me and me only! I don't need you of all people trying to figure out what goes on in there!"
                s "All I'm saying is that the two of us aren't so different. And that you should be happy I'm interested in girls like you."

                scene pornshop9r3
                with dissolve

                mak "It's not that I'm not happy..."
                mak "It's just...a lot to take in at once..."
                s "Don't worry. I'll go slow."
                mak "..."
                s "..."

                scene pornshop9r4
                with dissolve

                mak "..."
                mak "I wonder if I should leave a suicide note..."

                scene pornshop8
                with dissolve

                "Makoto walks over to a rack near the wall and starts checking out a few DVDs."

                mak "Sensei...all of the girls I'm seeing with glasses...look a tiny bit too close to me..."
                s "Perfect. I'll take them all."
                mak "A-All of them?! Just how much free time do you have?!"

                "Makoto begins shoveling all of the student/teacher DVDs she can find into her arms...only to put them all right back and return to the counter minutes later with absolutely nothing."

            "The weirdest shit you've got":
                s "Well, this isn't easy to talk about, but..."
                s "I’m not really into...'conventional' pornography."

                scene pornshop10
                with dissolve

                mak "And...what does that mean exactly?"
                s "You not understanding just means you haven’t been tainted by the evils of the world yet."
                mak "The...evils of the world?..."
                mak "But how is that supposed to help me find-"
                s "You know what? Just do a couple laps around the store and grab me the weirdest thing you can find."
                mak "..."
                s "..."
                mak "Ugh..."

                scene pornshop8
                with dissolve

                "Makoto walks over to a rack near the wall and checks out a few DVDs."
                "Most of them wind up being immediately put back onto the shelves but, every once in a while, Makoto finds something of note and runs it by me."

                mak "Sensei...This one has a chicken on the cover..."

                "Unfortunately, it's never enough."

                mak "Is...Is that okay?"
                s "Weirder, please."
                mak "Weirder than a chicken?..."

                "Makoto looks through a few more rows of DVDs before coming back without anything in her hands."
    else:
        s "Mainly board games and long walks on the beach."
        s "Oh! Do you have the Wedding Singer on DVD? I would very much like to watch that with my accountant later."

    scene pornshop6
    with dissolve

    mak "Yeah, I tried...but I really can't do this."
    mak "I think it might be better if you just use the Internet after all..."
    s "How about you just follow me around the store and I point out all of the stuff I'm interested in?"
    s "That sounds like it would work, right?"
    s "Oh, and maybe after that, you could show me all of the stuff {i}you're{/i} interested in and-"

    scene pornshop11
    with dissolve

    mak "Oh, look at the time! We’re closed!"
    s "No you're not. It's only been like ten minutes since I walked in and-"
    mak "Thanks for stopping in, Sensei! It was nice seeing you!"
    mak "Please never come back and forget where I work now!"

    scene black
    with dissolve2

    if bonus == True:
        "Makoto begins pushing me to the door, but I refuse to leave this place without any porn."
    else:
        "Makoto begins pushing me to the door, but I refuse to leave this place without something to watch tonight."

    "In a desperate attempt to avoid leaving empty-handed, I reach out and grab the first DVD I see on the way out of the shop."

    mak "Hey! You can't just-"
    mak "Ugh, never mind! Just take it! I’ll pay for it myself!"

    "I give up resisting once I have something in my hands and Makoto is eventually able to push me outside, quickly locking the door behind me."

    mak "Goodnight, Sensei! You were never here and neither was I!"
    s "Goodnight, Makoto. See you tomorrow night."
    mak "I sure hope not!"

    "Left alone with nothing but my new DVD and the night sky, I glance down to inspect the cover."

    if bonus == True:
        s "“After School Service: Student Council Punishment Games”"
        s "..."
        s "I can work with this."
    else:
        s "“Napoleon Dynamite?” Ugh!"

        "I turn around, determined to return the DVD as I refuse to watch this pathetic drivel, but Makoto does not let me back in =/"

    $ renpy.end_replay()
    $ firsttimepornshop = True
    $ makoto_love += 1

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"

    stop music fadeout 3.0
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label porn3to4:
    play music "citylife.mp3" fadein 2.0
    scene pornshop9
    with dissolve

    "I decide to pay Makoto a visit at the porn shop."
    "Of course, she isn’t exactly happy to see me there."
    "I spend the next twenty minutes trying to convince her to help me
    find something I can take home only to be pushed out the door yet again."
    "If she treats {i}me{/i} like this, I can only imagine how she handles normal customers..."

    scene black
    with dissolve

    $ makoto_love += 1

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"

    stop music fadeout 3.0
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label pornshop5:
    scene pornshop
    with dissolve
    play music "citylife.mp3" fadein 3.0

    "Another night means another chance to embarrass Makoto, so I obviously decide to put these late hours to good use and terrorize my class representative."
    "Prepared to ruin her night, I walk through the doors and find the store entirely empty apart from my favorite employee and a large variety of sex toys."
    "I follow the sound of boxes being moved around and make my way across the store to find Makoto unloading a package of vibrantly colored dildos."
    "And honestly, seeing that is more than enough for me to deem tonight a success- but of course, I'm not going to leave here until I'm able to push her buttons a bit."

    scene pornfive1
    with fade

    mak "Correct me if I'm wrong, but I thought we agreed that you'd stop coming here."
    s "You're wrong. I'd never agree to such a thing."
    mak "And I'm assuming it wouldn't help if I explained how much I’d appreciate it if you just...let my work life be separate from my school one?"
    s "It would not. I want to know everything about you- from your blue eyes to the blue dildo protruding from the box near your feet."
    mak "I just don't understand why you keep coming here when I've already made it exceedingly apparent that I won't be selling you anything."
    s "Who says I’m here to buy anything?"

    scene pornfive2
    with dissolve

    mak "So you really do just find enjoyment in tormenting me, I see."
    s "To be fair, I thought that would have been obvious the second I returned."
    s "You just look so determined and professional while you’re here that it's just...really motivating."
    s "So thank you, Makoto. Thank you for your service."

    scene pornfive3
    with dissolve

    mak "You do realize that there are tons of places outside of school I'd be happy to see you in, correct?"

    if day38 == True:
        s "Like the park? Because we never did that again after the first time and that just makes me assume you prefer this."
        mak "I prefer...literally anything other than this."

        scene pornfive4
        with dissolve

        mak "Also, do you really expect me to believe that you want to use what little free time you have at the park with me?"
        s "Why not? I'm a lot more than just some insatiable porn addict, you know."
        mak "With how often you’ve been stopping by lately, I’m beginning to question that."
    else:
        s "Oh yeah? Like where?"

        scene pornfive4
        with dissolve

        mak "Um...well, there are places like the mall...or the movie theater..."
        mak "Or anywhere that doesn't reek of lubricant."

        scene pornfive3
        with dissolve

        mak "Just...you know...places we could hang out. Places where you could get to know the me that doesn't spend her nights stocking the shelves of a porn shop."

    s "Oh, speaking of which, I forgot to tell you about that DVD you let me have the first time I came by."

    scene pornfive6
    with dissolve

    mak "Why is that a thing you have to tell me about? Can't you just keep it to yourself?"
    s "No. You paid for it, so I obviously have to tell you about it now."
    mak "That is absolutely not a thing you have to do."

    if bonus == True:
        "Thankfully, I brought back the store’s copy of ‘After School Service: Student Council Punishment Games’ to see if maybe they
        have a trade-in policy of some sort."
        "Though, knowing Makoto, I doubt I’ll be able to actually trade it in even if they do."
    else:
        s "Napoleon Dynamite"
        s "I would like my money back."
        mak "But you didn't even pay for it."
        s "I know. But I deserve to be properly compensated for even holding something as horrible as this."

    s "But I will anyway. Here, look."

    "I remove the DVD (That I very conveniently happened to be carrying) from the inside of my blazer and show it to Makoto."

    if bonus == True:
        "The cover itself is boring, but there is an image of a girl who looks strikingly similar to her on the back jacking off two guys at once."
        "I could have done without the second guy, but it was a pretty solid DVD regardless."
    else:
        s "How could anyone possibly find this funny?"

    scene pornfive7
    with dissolve

    mak "Wha?!"
    mak "What the Hell do you think you’re showing me?!"

    if bonus == True:
        s "Just some girl who looks like you having the time of her life."
        mak "There are plenty of people out there who look like me! That doesn't make it okay to just...show me them {i}having the times of their lives.{/i}"
        mak "Now put that thing away before I call security."
        s "You don’t even have security."
        mak "Well....put it away anyway!"
    else:
        s "A very bad movie."
        s "Please. Remove it from my hands."
        mak "No! There are no takebacks here! Especially for shoplifted things!"

    s "I was kind of hoping I'd be able to trade it in for something else."

    scene pornfive8
    with dissolve

    mak "What kind of store do you think this is?"
    s "Not a very good one, apparently."
    s "..."
    mak "..."

    scene pornfive2
    with dissolve

    if bonus == True:
        mak "Hah...I don’t think I’m ever going to get over how you were secretly a pervert this whole time."
        mak "I swear, I never would have thought you were {i}that{/i} type of person in the beginning of the year."
        mak "You were so...professional. And serious."
    else:
        mak "Hah...I've been telling my mom for years that we should stop calling this place a DVD store and call it what it actually is."
        s "An adult-centered multimedia distribution center?"
        mak "Sure. Let's go with that."
        s "Life sure likes to throw us curveballs, doesn't it?"
        mak "Sure does..."

    scene pornfive8r
    with dissolve

    mak "And now you’re watching things like..."

    if bonus == True:
        "Makoto takes a quick glance at the DVD, doing her best to avoid locking eyes with her pornographic doppelganger."

        scene pornfive7
        with dissolve

        mak "S-Student Council Punishment Games?! We have like six million films here and you went and grabbed {i}that?!{/i}"
        s "It was actually pretty good. We should watch it together sometime."
        mak "Together?! Absolutely not! There's no way I could watch something like that with you hovering over me like some sort of...hungry jackal!"
        mak "I have a hard enough time just watching stuff like that on my own."
        s "And...what exactly is difficult about watching porn alone?"

        scene pornfive9
        with dissolve

        mak "Well, I just...I don't know...There's...not enough time?"
        mak "I’m barely ever alone to begin with...and when I actually {i}am,{/i} I'm normally studying instead..."
        mak "And these aren't exactly the types of movies I want to watch with my mom or Miku around..."
        s "You mean you and Miku don’t watch porn together?"

        scene pornfive5
        with dissolve

        mak "I don't think Miku's watched a single porn video in her life. She still closes her eyes any time she walks through the store."
        s "Maybe I should invite her to our viewing party as well?"
    else:
        s "Don't look at it Makoto. It will burn your eyes."
        mak "I can feel my soul being ripped from my body."
        s "Damn you, Pedro."

    scene pornfive5r
    with dissolve

    mak "Or maybe you should put that DVD back on one of the shelves and leave so I can finish closing the store?!"
    s "Aren’t you supposed to be open for another few hours? You can't keep closing early just because I'm bothering you."
    mak "If we don't have any actual customers, I can do whatever I-"
    s "I’m a customer. Hold on, let me get something."
    mak "I already told you that I don't intend to sell you-"
    s "It's not for me, it's for you. I'm getting you a present."

    scene pornfive9r
    with dissolve

    mak "A...present?"
    mak "But...what would you even-"

    if bonus == True:
        jump makotodildograbx
    else:
        scene black
        with dissolve

        s "Makoto, here. It is a brand new desk for you to study at because I know how much you like education."
        mak "How did you even get that into the store without me noticing?"
        s "That does not matter."
        s "Quick, sit down at the desk and show me how you study."
        mak "I am floored. This is such a generous gift."

        "I take a picture of Makoto enjoying her new desk and she gets very embarrassed because liking knowledge is something only a loser would do."

        $ renpy.end_replay()
        $ pornshop5 = True
        $ makoto_love += 1
        stop music fadeout 5.0

        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label pornshop10:
    scene pornshop10
    with dissolve2
    play music "citylife.mp3"

    mak "Oh dear lord, it never ends."
    s "Oh, come on. Since when is it a crime to spend time with my favorite student?"
    mak "‘Spending time’ together isn’t exactly the issue..."

    "Once again, I find myself at the porn shop with Makoto. And once again, she is not happy to see me."
    "But I guess not many people {i}would{/i} be happy to see their teacher at a porn shop."
    "Unless you're surveying my class."
    "If that's the case, probably half of them would."
    "But obviously, Makoto is not one of them."

    s "Hey..."
    mak "What? Why are you saying {i}hey{/i} like that?"
    s "Is there anything I can do to help increase business here?"
    s "I've been coming here for a little while now and I've yet to actually see any other customers."
    s "And I can't imagine the lack of men has been doing any favors for your family financially."

    if bonus == True:
        jump makotoporn10x
    else:
        mak "Why, yes. There are many things you can do to help."
        mak "Grab a chair and let's talk business."

        scene black
        with dissolve

        "Makoto breaks down the numbers for me and it appears that the lack of males really did make a dramatic impact on her family's store."
        "Together, she and I come up with a new business plan to attract more female customers that we are going to pitch to her mother after purchasing fancy suits."
        "Everyone knows that sales pitches go better when there are suits involved."

        s "I want mine to be purple."
        mak "You can't wear a purple suit. It is bad luck."
        s "I am sorry. Forgive me."

        "I did not know this."

        $ renpy.end_replay()
        $ pornshop10 = True
        $ makoto_love += 1
        stop music fadeout 5.0

        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label pornshop15:
    scene pornshophhg
    with dissolve
    play music "citylife.mp3"

    "I show up at the porn shop to find it in...slightly different condition than normal."
    "Previously, all of the posters covering the wall had seemed relatively low-resolution- like they were printed out on paper and just taped up or something."
    "But it looks like a whole plethora of new posters have been hung now. And they’re all advertising the same thing."
    "The fuck is {i}Hero's Harem Guild?{/i}"
    "..."
    "I take a look around to see if I can spot Makoto, but I-"

    mak "This...fucking...stupid...game..."
    s "..."
    s "Makoto? Where are you?"
    mak "Over here, bashing my head against a wall."
    mak "What do you want? "

    if bonus == True:
        s "Uhh...porn? Did you forget what you sell here?"
        mak "Go home and watch porn on your computer."
    else:
        s "I just wanted to spend time with my class representative and go over a varitey of new teaching techniques I am interested in attempting."
        mak "Go home and practice them with your accountant."

    scene makotohhg1
    with dissolve

    s "Nah, I think I’ll just watch whatever you’re-"
    s "..."
    s "Are you...fishing?"
    mak "What does it look like I’m doing, genius? Of course I’m fishing."
    s "Why?"
    mak "Some weird guy showed up an hour ago and just started hanging up all these weird posters for some video game he’s making."

    if bonus == True:
        jump makotohhgx
    else:
        s "Wow, neat! It looks really fun."
        s "Can you teach me how to play?"
        mak "Sure. Take a seat."

        scene black
        with dissolve

        "Makoto and I spend the next hour or so playing a fun fishing simulation game."
        "Also, I meet her mom. She seems like a completely normal woman and gives me her phone number so I can keep her updated on Makoto's progress in college."

        $ renpy.end_replay()
        $ makoto_love += 1
        $ pornshop15 = True
        $ makinumber = True
        stop music fadeout 8.0

        "{i}Congratulations! You now have Maki’s phone number.{/i}"
        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotolust5:
    scene black
    with dissolve
    "........."
    "......"
    "..."
    scene makotofirstlust1
    with dissolve
    play music "citylife.mp3"

    mak "Why are we in the back room already? How did I get here?"
    mak "There wasn’t even an opening to this event."

    if bonus == True:
        jump makotolust5x
    else:
        s "There won't be an ending either."
        mak "What? Why not?"
        s "Patreon doesn't want this scene in the game."
        mak "Oh. Well, I guess that takes a load off my back since I won't feel pressured to hug you anymore."
        s "I never want you to feel pressured about anything, Makoto. I am nice."
        mak "You're okay."
        s "Wow."

        scene black
        with dissolve

        "If that's how Makoto really feels about me, I don't even want to be here anymore."

        s "Goodbye, Makoto. Enjoy your weirdly lit backroom thing."
        mak "Bye, Sensei. Thank you for being a responsible man who does not want to distract me while I am at work."
        s "Tell your mother I said hello."
        mak "But she hasn't even shown up in the game yet."
        s "I know, but I saw her character profile and she looks cute."
        mak "Okay. I will tell her."

        $ renpy.end_replay()
        $ makoto_lust += 1
        $ makotolust5 = True
        stop music fadeout 5.0

        "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotoinvite1:
    play sound "phonebeep.wav"

    "I tap on Makoto’s name in my phone and wait for her to answer."
    "I figure that the two of us know each other well enough at this point that it will be fine for me to start inviting her over."
    "Of course, there is one glaring issue with that- and its name begins with the letter A."
    "If you said Alexander Graham Bell...you’d be wrong."
    "Because the answer is Ami."
    "Ami is the glaring issue."

    if invitetip == False:
        call invitetip from _call_invitetip

    scene noonsky
    with dissolve
    play sound "phonebeep.wav"

    mak "Hello?"

    play music "normalday.mp3"

    s "Hey, Makoto. What are you up to?"
    mak "I’m just getting ready for work. Why? Did something happen?"
    s "Why are you assuming something happened?"
    mak "Well, you know I have work, so I doubt you’d be calling to invite me over or something."
    s "Does that mean you can’t come?"
    mak "Wait, wha-?!"

    if bonus == True:
        "I can hear a stack of things falling over in the background. Probably dildos or something because she works in a porn shop."
        "The thought of a stack of dildos falling on top of Makoto is almost enough to make me smile and I have to prevent myself from doing so in order to keep up my manly illusion."
    else:
        "I can hear a stack of things falling over in the background. Probably books because Makoto is a smart girl who loves to read and learn."

    mak "You...You’re inviting me over?!"
    s "I am. Are you able to get your mom to cover for you or something?"
    mak "Um...uhh! Hold on! I’ll go check!"

    "The sound of things falling over is quickly replaced by the sound of Makoto stomping up the stairs to where I imagine her mother is."
    "This must be the case because there is no other discernible reason for her to be using stairs right now."

    mak "Mom! I need you to watch the store!"
    mak "I...have to study!"

    if pornshop15 == True:
        maki "What? Can’t you just study in the shop? That’s what you always do."
        mak "Not today! Today is...different!"
        maki "But I’m so tiiiiiiiiiiiiired~"
        mak "Mom! Please! "
        maki "...UGH OKAY. "
        maki "I should probably take inventory anyway..."
        mak "THANK YOU."

    else:
        q "What? Can’t you just study in the shop? That’s what you always do."
        mak "Not today! Today is...different!"
        q "But I’m so tiiiiiiiiiiiiired~"
        mak "Mom! Please! "
        q "...UGH OKAY. "
        q "I should probably take inventory anyway..."
        mak "THANK YOU."

    "Makoto quickly runs back down (Or up? Probably down) the stairs before bringing the phone back to her ear."

    mak "*Ahem*"
    mak "Sensei? It appears that I will be able to come over after all."
    mak "As it turns out, I wasn’t even scheduled to work tonight. What a wonderful coincidence."
    s "But I just heard-"
    mak "Can you send me your address please?"
    mak "I can probably find it if I check the[school]-register, but this way seems a lot less weird."
    s "Yes. {i}A lot{/i} less weird."
    s "And also, expect a fight when you get there."
    mak "...Is that code for roleplay or something?"
    mak "I knew it was strange that you were inviting me over out of nowhere."
    s "No, I just mean that I can’t imagine Ami will take kindly to seeing you in the house."
    mak "I see."
    mak "Should I bring a weapon?"
    s "Do you...own a weapon?"
    mak "I can find one."
    s "Uhh, no. I think it’s fine. "
    s "Just...come over whenever you’re ready."
    mak "Will do! See you soon!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and start making my way home."
    "It would be pretty horrible if Makoto gets there first, so I need to...prep Ami in the meantime."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"

    s "I’m back..."

    scene makotofirstvisit1
    with dissolve

    a "Oh, welcome home!"
    a "Would you like dinner now? Or perhaps a bath instead?"

    scene makotofirstvisit2
    with dissolve

    if bonus == True:
        a "Or maybe...me?"
    else:
        a "Or maybe...your freedom?"

    s "None of the above."
    a "Aww, Sensei~ That’s so-"

    scene makotofirstvisit3
    with dissolve

    a "Wait, what?!"
    s "Ami, how much do you love me?"
    a "Obviously a lot!"
    s "Then I’m going to need you to listen very carefully."

    scene makotofirstvisit4
    with dissolve

    a "Is something going on?...You’re scaring me."
    s "It’s only going to get worse."
    a "Should I...sit down?"
    s "No. Stay right there."
    s "What I am about to say is going to shock you. But I need you to know that it won’t change anything between us. Okay?"
    a "Um...yeah...Of course."
    a "Are you sure everything is-"
    s "Sometime in the next few minutes-"
    s "Makoto is coming over."
    a "..."
    s "..."
    a "..."
    s "..."

    scene makotofirstvisit5
    with dissolve

    a "What?"
    s "Now, I need you to stay calm-"
    a "It’s so we can kill her, right?"
    a "You’d obviously never be stupid enough to invite {i}her{/i} to {i}our house{/i} unless it was to give me an early Christmas present...RIGHT?"
    s "It’s...to study."
    a "To {i}study{/i}? Do you really think I’m going to buy that? You’re barely even a teacher."
    s "No, I mean it. It’s just...for {i}me{/i} to study...Not her."

    "I decide to say the first thing that comes to mind."
    "Realistically, I probably could have just lied and told Ami that we were having the house fumigated or something and made her go back to the dorm but..."
    "Well, where’s the fun in that?"

    scene makotofirstvisit6
    with dissolve

    a "So, let me get this straight..."
    a "You invited Makoto over to {i}our house{/i} because {i}you{/i} apparently need help {i}studying{/i}?"
    s "Yes. And what’s with all of the italics?"

    scene makotofirstvisit7
    with dissolve

    a "Does it make you feel weak? Needing the help of a [teenage]girl?"
    s "You and I both know that Makoto is no normal [teenage]girl. She’s superhuman."
    a "More like super-stupid."
    s "Good one."

    play sound "doorbell.mp3"

    "..."

    a "Oh good. That must be the superhuman."
    a "Why don’t you answer the door, Sensei?"
    a "You must be eager to {i}learn{/i}, right?"
    s "I need you to promise me that we won’t have to hide a body by the end of the night."
    a "I’m obviously {i}not smart enough{/i} to pull off a murder, so I doubt that will be necessary."
    s "Good. I’m glad you understand."

    scene makotofirstvisit8
    with dissolve

    a "THAT WAS SARCASM, YOU JERK! I’M PLENTY SMART!"

    scene black
    with dissolve

    "I move to the door to let Makoto in. "
    "Right before I open it, I look back at Ami to make sure she hasn’t gone to the kitchen and grabbed any sharp utensils..."

    play sound "dooropen.mp3"

    s "Hey. Thanks for coming to {i}help me study{/i}..."
    mak "Help you study? What are you-"
    mak "Oh! Y-Yes! Are you...prepared for knowledge?!"
    s "{i}What the Hell is that? Just act natural.{/i}"
    mak "{i}Leave me alone! I’ve never been in a boy’s house before! I’m nervous!{/i}"
    a "CLASS...PRESIDENT..."
    a "!!!!!!!!!!!!!!!!!!!!!"

    "Oh boy. Here we go."

    scene makotofirstvisit9
    with dissolve

    a "You’ve got some real nerve showing up here, you know?!..."
    mak "Oh. Hello there, Ami. I seem to have forgotten you lived here."
    a "I don’t just {i}live{/i} here! I take care of my [uncle] here! We’re practically inseparable!"

    "Not true. We’re pretty separable."

    mak "Is that so? Because he didn’t even mention your name when {i}inviting me over{/i} today."

    "Also not true. I specifically mentioned that Ami lives here and that this exact thing would likely happen."

    a "That’s really funny because he’s never mentioned your name literally ever in the entire time I’ve known him."

    if bonus == True:
        a "Actually, that’s wrong. He did say “Wow, that Makoto girl sure is ugly!” this one time while I was washing his back in the bath."

        "Again, not true. That exchange never happened."
        "Why must girls always lie when fighting with one another?"
    else:
        s "That is only because you keep my mouth taped shut while I am home."
        a "Shut up, my little pogchamp."
        s "Sorry, Ami."

    scene makotofirstvisit10
    with dissolve

    if bonus == True:
        mak "Oh? Then perhaps I should wash his back tonight and the two of us can have a little discussion about you..."
    else:
        mak "Oh? Has anyone ever told you that taping the mouth of someone you love shut might actually just make them love {i}you{/i} less?"
        a "What?!"

    mak "And how your creepy obsession with your [uncle] is teetering on the verge of [incest] which, I’ll have you know, is illegal. Especially with someone who isn’t even-"
    a "Eyes up here, devil-woman."
    a "You will look at me when I am talking to you."
    a "Do I make myself clear?"

    scene makotofirstvisit11
    with dissolve

    mak "Oh, Ami! I forgot you were even there. Sorry about that."
    a "You didn’t forget me! You were just talking about me!"
    a "We are arguing! Forgetting me during a time like this isn’t even possible!"
    mak "Wait, who are you again?"
    mak "A maid? Gardener?"
    mak "If you don’t mind, I’d like to be left alone with my teacher."
    mak "He and I have {i}a lot of ground to cover{/i} tonight."

    scene makotofirstvisit12
    with dissolve

    a "You...thirsty...little...bitch..."

    "Oh, wow. Ami’s even angrier than normal this time."
    "I mean, of course something like this would be bound to happen with Makoto encroaching on her home-turf..."
    "But I’m starting to worry that the two of them might actually start hitting each other if I don’t step in."
    "..."
    "Actually, that might be fun to watch."
    "Wait."
    "No."
    "I really shouldn’t let that happen."
    "If anything happens to Makoto while she’s here, I could get in trouble."
    "Makoto’s a smart girl, but I’m pretty sure that even she would have trouble explaining to her mother why she’s coming home with a black eye after {i}studying{/i}."

    scene makotofirstvisit13
    with dissolve

    a "Sensei..."
    s "No, Ami. You can’t hit her."

    scene makotofirstvisit14
    with dissolve

    a "NGH! WHAT IS THIS WORLD COMING TO?!"
    mak "Thank you for protecting me, Sensei."
    mak "To be fair, I don’t think I’d need any protection from Ami considering her arms are essentially oversized noodles, but I thank you nonetheless."

    scene makotofirstvisit15
    with dissolve

    a "My arms are not oversized noodles! They’re strong and ready to fight for what they love!"
    a "Come at me, wench!"
    mak "Sensei, where do you keep her leash? I’m thinking it might be safer for all of us if we just chain her up for a little while."
    s "Uhh...I don’t have a leash. Let’s see if this works."
    s "Ami, go to your room."

    scene makotofirstvisit16
    with dissolve

    a "No!"
    s "I have exhausted every trick known to me. I’m sorry, Makoto."
    mak "It’s fine."
    mak "I suppose it wouldn’t be the worst thing in the world if all three of us were to...study together."
    mak "All that matters to me is that I get to spend time with you, Sensei...It doesn’t bother me that we’re not alone."

    scene makotofirstvisit17
    with dissolve

    a "And you never {i}will{/i} be alone. Not as long as I live."
    a "Makoto...Miya-whateveryourlastnameis...We are at war."
    mak "It’s Miyamura. And I accept your declaration of war, Ami Aragofuckyourself."
    s "Hey, wait a minute. She and I have the same last name. That’s kind of insulting to me as well."

    scene makotofirstvisit18
    with dissolve

    mak "Oh, of course. I’m so sorry."
    mak "I’d obviously never ask {i}you{/i} to go fuck {i}yourself{/i}, Sensei."
    a "I don’t like the way you said that, Class President."
    a "But since I’m an obedient [niece] who will {i}always{/i} do {i}whatever{/i} her [uncle] {i}wants her to do{/i}, I’ll stand down for the time being."
    a "So go on. Study. Teach whatever it is you came here to teach him."

    if bonus == True:
        a "But know that I’ll be sitting on his lap the entire time."
        s "No, Ami. You will not be sitting on my lap the entire time."
    else:
        a "But know that there's no point in teaching anyone anything when we are all fated to be miserable up until the time of our death!"

    scene makotofirstvisit19
    with dissolve

    a "THERE IS NO GOD!!!!"

    scene black
    with dissolve

    "Makoto, Ami and I take a seat at the dining room table and, somehow or another, Makoto is able to freestyle-lecture us about the American Civil War."
    "Why {i}that{/i} is the first thing she comes up with to solve the issue of our fake {i}studying{/i} session, I have no idea."
    "But it happens nonetheless."
    "Hopefully, she and I will be actually able to spend some time alone here soon."
    "But while Ami is around, I...can’t see that ever working out."
    "Eventually, it gets late and Makoto decides to head home."
    "I try to see her out but Ami pushes me away and then {i}literally{/i} pushes Makoto out of the house."
    "Either way, I still feel like the two of us managed to grow closer."
    "Even if it came at the cost of Ami yelling at me for the next half an hour after that."

    $ renpy.end_replay()
    $ makoto_love += 3
    $ makotoinvite1 = True
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotoinvite2:
    play sound "phonebeep.wav"

    "I decide to invite Makoto over and tap on her name in my phone."
    "Being that last time didn’t exactly go {i}well{/i}, I figure that I might need to do something about Ami if I want tonight to end in success."
    "But I need to at least figure out if Makoto is able to get out of work first."
    "........."
    "......"

    scene noonsky
    with dissolve
    play sound "phonebeep.wav"

    mak "Hello? Sensei?"
    s "Hey. You wouldn’t happen to be free right now, would you?"
    mak "Umm...I {i}could{/i} be free, I suppose. My mom and I are both in the shop right now."
    s "Does she know that I'm the one calling you?"
    mak "No. She’s in the back room at the moment. She probably didn't even hear my phone ring."
    s "Cool. Tell her you need to study again or something."
    mak "Just to clarify, you {i}are{/i} inviting me over...Correct?"
    s "Correct."
    mak "Is your demon-spawn of a [niece] there right now?"
    s "She isn’t a demon-spawn...but probably. I’ll figure out a way to deal with her, though."
    mak "Good. Because I’d very much like to actually be {i}alone{/i} with you if we’re going to be in your house."
    s "Are you trying to seduce me over the phone?"
    mak "N-No! I just...you know! It’s {i}your{/i} house! "
    mak "I’m obviously going to...expect certain things if you invite me over."
    s "What are you expecting, Makoto?"

    play sound "phonebeep.wav"

    "Makoto hangs up the phone without responding to my question, which I’m assuming means that she is, in fact, going to come over."

    scene black
    with dissolve

    "I begin my trip home right away and type out a convincing text message to Ami about how I need her to go grocery shopping."
    "Being as dedicated to pleasing me as she is, I know that she’ll do virtually anything I ask."
    "Which is precisely why I come up with a list of imaginary ingredients for her to procure in order to extend the time Makoto and I will be together for."
    "I truly am a genius when I want to be."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"

    mak "Excuse me..."

    scene makotofirstinvlust1
    with dissolve
    play music "asobeatsex5.mp3" fadein 5.0

    s "Hey. How was your walk over?"
    mak "It would be a lot nicer if you were a normal adult and had a car to pick me up in."
    s "If I had a car to pick you up in, there wouldn’t be much of a reason for us to come {i}here{/i} in the first place."
    mak "I’m not sure what you mean by that, Sensei. Please clarify."

    if bonus == True:
        s "Oh, sure. I just meant that if I had a car, we could relieve our obvious sexual tension there instead of needing to come all the way here for it."
    else:
        s "If I had a car, I would never let anything come between you and me and the act of hugging."

    scene makotofirstinvlust2
    with dissolve

    mak "Uhh...I knew that’s what you were insinuating, but I thought you were at least going to be a little less...direct about it."
    s "No point. You’re smart enough to know that I wouldn’t get Ami out of here unless there was something I wanted from you."
    mak "{i}From{/i} me? Or {i}with{/i} me?"
    s "Whichever. It doesn’t really matter to me."

    scene makotofirstinvlust3
    with dissolve

    mak "Come on! At least be nice when you’re trying to hook up with me!"

    if bonus == True:
        s "But being nice is so exhausting. Do I really have to do that?"
        mak "Yes, you very much do. I have not yet provided consent and can leave at any moment."
    else:
        s "Woah, chill. I just want to hug."

    s "Aren’t you my classroom assistant or whatever? Do I really need consent from you?"

    if bonus == True:
        mak "Obviously. The student handbook says nothing about how classroom assistants are to perform sex acts on their teachers."
    else:
        mak "Obviously. The student handbook says nothing about how classroom assistants are to hug their teachers."

    s "If it doesn’t specifically say anything about that, doesn’t it mean it’s allowed to a certain extent?"

    scene makotofirstinvlust4
    with dissolve

    mak "Well, there is something in the generic section prohibiting physical relationships between teachers and students, so I’m pretty sure this would just fall under that."
    s "You’re such a buzzkill, Makoto."

    scene makotofirstinvlust5
    with dissolve

    mak "Of course I am. That’s my job."
    mak "If I don’t keep you in-line, who else will?"
    mak "And don’t say Ami because she doesn’t count as an actual human being."
    s "I think you two really need to resolve your differences."
    mak "It’s not our differences that make us adversaries- it’s our similarities."
    mak "She can sense how the relationship you and I have is special, and that makes her worried given that she has a different type of special relationship with you."

    if bonus == True:
        mak "Obviously, the one you two have is more of a familial relationship while the one you and I have is more..."
        mak "Intimate?"
        mak "Passionate?"
        s "Wow, nothing gets me in the mood quite like a lecture about the differences between my [niece] and you."
        mak "Well what else am I supposed to do? I don’t know which door leads to your bedroom yet."
        mak "And I can’t imagine you want me taking my clothes off in the living room. That would just be impolite."

        jump makotosecondinvx
    else:
        mak "Obviously, the one you two have is more of a...business relationship while the one you and I have is more..."
        s "Huggy?"
        mak "Sure. Huggy."
        s "Bring it in, Makoto."
        mak "Thanks. This will make me feel less bad about not being able to see my dad anymore."

        scene black
        with dissolve

        "A hug happens and Makoto cries a little."
        "I console her because I am a little nicer in this version of the game."

        $ renpy.end_replay()
        $ makoto_lust += 3
        $ makotoinvite2 = True
        stop music fadeout 10.0

        "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
        "{i}You can now choose between affection and hugging when inviting her over!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotoinviteaff:
    scene makotoinvitegen
    with fade

    "I decide to spend the night just hanging out with Makoto."
    "No sexual stuff involved. No teasing involved. Just-"
    "Well, actually, there is {i}some{/i} teasing involved. But it's all in good fun."
    "That's just the sort of dynamic the two of us have together."
    "I tease her. She blushes and yells at me. I pretend I don't feel anything at all for her. She pretends to think that as well."
    "But the moments we share like this, despite being few and far between, serve to contradict that."
    "Right now, in this very moment, it feels like she belongs here."
    "If only I could say the same for myself."

    scene black
    with dissolve

    "The world grows darker by the minute."
    "The house is consumed by the night."
    "Which, of course, means it's about time for Makoto to leave."
    "Ami should be getting home sometime soon anyway."
    "Makoto is reluctant to pack her things and go, but realizes that she must if the two of us are going to be able to spend more time together doing things like this."
    "It's okay, though."
    "I'm sure I'll see her again before long."

    $ makoto_love += 3
    stop music fadeout 5.0

    "{i}Makoto's affection has increased to [makoto_love]!{/i}"

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

label makotoinvitegrind:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump makotoinvitegrindx
    else:
        $ makoto_lust += 3
        stop music fadeout 5.0

        "{i}Makoto's lust has increased to [makoto_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label pornshop20:
    scene makotomakidildo1
    with dissolve
    play music "citylife.mp3"

    "I arrive at the porn shop to find a less-than-happy Makoto standing still at the counter and already hating the fact that I am, yet again, visiting her at work."

    if bonus == True:
        "You’d think that after taking her virginity she’d be a lot more accepting of my degenerate side, but I guess she’s still just normal, old Makoto after all."

    mak "Whaaaaaaaaaaaaat? Why are you here?"

    if bonus == True:
        mak "Let me sell porn in peace."
        s "I can’t get enough of you, Makoto. Staying away is impossible."

        scene makotomakidildo2
        with dissolve

        mak "As if I’d believe that from the same guy who routinely calls girls into his office to do God-knows-what to them."
        s "It’s called counseling. And that sour attitude of yours makes me think it might be time for you to receive some. "
        mak "Right, right. I’m sure that would be a great conversation with Mother."
        mak "Hey, Mom? I need counseling now."
        mak "{i}Why, dear? What’s wrong?{/i}"
        mak "I’m not excited enough about selling anal gangbang videos to my teacher. I must be rehabilitated."
        s "To be fair, your mother always seems very excited about the concept of anal gangbang videos."
    else:
        s "I was lonely. I just needed to be held."
        mak "I do not want to hold you."
        s "Your mom would hold me if I asked her to."

    scene makotomakidildo3
    with dissolve

    mak "My mom is a fucking creep! She doesn’t count!"
    maki "I can hear you, Makoto!"

    scene makotomakidildo4
    with dissolve

    mak "Shut up, Mom! "
    maki "I love you, sweetie!"
    s "You two are so cute together."

    scene makotomakidildo5
    with dissolve

    mak "You are the bane of my existence."
    s "Wow. And to think you’d say something like that after all of the precious memories we made during the Halloween party."

    scene makotomakidildo6
    with dissolve

    mak "Those memories were made with fun-Makoto. Business-Makoto is currently in charge, thank you very much."

    if bonus == True:
        mak "And also, please don’t speak any further about the memories we made while my mother is right around the corner re-stocking vibrators."
        s "I’m honestly surprised you sell enough of those to warrant re-stocking them."

        scene makotomakidildo7
        with dissolve

        mak "Well, you know. It’s getting close to Christmas and the historic lack of men means a lot of women buying presents for one another."
        s "Right. And what better present than the gift of an orgasm?"
        mak "Right..."

        scene makotomakidildo8
        with dissolve

        mak "Wait! Not right! There are a lot of better presents out there!"
        mak "Like...golf clubs! Or a trip to the zoo!"
        s "Or this."

        scene makotomakidildo9
        with dissolve

        "I reach behind me and manage to grab hold of a display-dildo sitting on top of a shelf, placing it directly into Makoto’s hand."
        "She angrily looks over it, likely pondering the kindest way to remove me from the store without her mother getting mad at her for turning away a real-live customer."
    else:
        s "If that is what you think is best, I will cease conversation and simply purchase this item right here."

        scene black
        with dissolve

    s "One Christmas present, please."

    if bonus == True:
        scene makotomakidildo10
        with dissolve

    mak "Would you like it gift-wrapped, sir?"

    if bonus == True:
        jump makotomakidildox
    else:
        s "Yes, please. It is for my accountant."
        mak "Why are you purchasing a roll of duct tape for you- oh. Right."
        s "I am in trouble, Makoto."
        mak "..."
        s "Please help me."

        $ renpy.end_replay()
        $ pornshop20 = True
        $ makoto_love += 1
        stop music fadeout 5.0

        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label pornshop25:
    scene makotoona1
    with dissolve
    play music "citylife.mp3"

    "I decide to spend the night hanging out at the porn shop with Makoto."
    "{i}She{/i} decides not to play along or have fun with me because business-Makoto is a fucking loser."

    mak "For the last time, can you put that thing down?"
    mak "If you’re not going to buy it, you shouldn’t be messing around with it."
    s "I’ve tried buying it four times now and each time you’ve turned me away."

    if bonus == True:
        jump makotoonax
    else:
        mak "Yes, because that is not an item {i}we{/i} sell. It is something from the store next door to us."
        s "You mean to tell me that this limited edition Turboman action figure actually comes from the toy shop next door and not this business?"
        mak "For the tenth time, yes. Go bring it back."
        s "But my son needs it in time for Christmas."
        mak "You don't even have a son."
        s "And you never will either with that attitude."
        mak "That's it. I'm calling the cops."

        scene black
        with dissolve

        s "Turboman, blasting off!"

        "I make wooshing noises and wiggle the action figure around in the air on my way out of the store."
        "I don't know if Turboman can actually fly or not, but I'm going to pretend he can if he can't because I think that makes him sound more turbo."

        $ renpy.end_replay()
        $ pornshop25 = True
        $ makoto_love += 1
        stop music fadeout 5.0

        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotoinvitefinger:
    scene black
    with dissolve

    ".........."
    "......"
    "..."

    if bonus == True:
        jump makotoinvitefingerx
    else:
        $ makoto_lust += 3
        stop music fadeout 5.0

        "{i}Makoto's lust has increased to [makoto_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotolust10:
    scene makotolustten1
    with dissolve2
    play music "asobeatsex3.mp3"

    mak "Hah..."
    mak "Finally."
    mak "I swear, Sensei, it’s like you don’t even work here sometimes."
    s "Sometimes? I feel like I’ve made it very apparent that I literally never work here."

    scene makotolustten2
    with dissolve

    mak "Correct. Though, I guess it might be hard to discern the sarcasm in my voice when I’m this exhausted."

    "Makoto and I are in my office after a long day of[school] in which we were tasked to do some...I don’t even know."
    "A thing, I guess."
    "One of the other teachers came into my room at the end of the day and started rattling off a bunch of stuff I didn’t understand, so Makoto was kind enough to step in and offer her assistance."
    "Originally, the gameplan was for her to stop by after class ended for the day and just do it all for me, but..."
    "Well, she apparently decided that we needed to clean my office afterward as well since I haven’t bothered tidying up in...ever."

    if bonus == True:
        jump makotolusttenx
    else:
        mak "I hope you are ready to clean."
        s "Noooooooooooooooooooooooooooooooo! You can't make me."
        mak "Sensei. Don't you dare throw a temper tantrum!"
        s "I don't wanna clean! I am the protagonist!"

        scene black
        with dissolve2

        "Makoto manages to make me clean because that's what the script says I'm supposed to do."
        "I hate it and the event ends way too quickly without anything fun happening."

        $ renpy.end_replay()
        $ makotolust10 = True
        $ makoto_lust += 1
        stop music fadeout 5.0

        "{i}Makoto’s lust has increased to [makoto_lust] because she really likes cleaning.{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotowinterbeach1:
    play sound "phonebeep.wav"

    "I tap on Makoto’s name in my phone and wait for her to answer."
    "It’s been a little while since she asked me if I’d accompany her to the beach and...what better time to do that than a random afternoon in the middle of winter?"
    "Yes, the idea of the two of us going {i}there{/i} when it’s obvious she just wants to be alone with me rather than scope out a venue she’s already familiar with is a little...abnormal."
    "But I’m not going to throw away a vacation opportunity with a cute girl just because the conditions aren’t perfect."

    if bonus == True:
        "Besides, I’m sure we’ll find some way to keep warm in no time at all..."
        "I'm talking about sex."
        "That was a sex joke."

    play sound "phonebeep.wav"
    play music "acoustic.mp3"

    mak "Hello?"
    s "Hey, Makoto. What are you up to right now?"
    mak "Right now? I’m just...hanging around. Why do you ask?"
    s "Is now a good time to go on that beach trip?"
    mak "Uhh...no. Not really. "
    mak "Can you hold on one second, please?"
    s "Huh? Uhh, yeah. I guess that’s fine."
    mak "Thanks. I’ll be back in a second."

    "I hear Makoto put the phone down and start talking to someone (Probably her mom) about something I can’t really make out over the sound of a television in the background."
    "I remain on the line for several minutes and begin to lose my patience."
    "But just as I’m about to hang up and find something else to do, I hear her coming back."

    mak "Yeah. We can go now. But...I want to meet {i}there{/i} if that’s okay."
    s "Why? "
    s "If this is about you throwing me a surprise party, I don’t want one."
    mak "Why on earth would I throw you a surprise party? That’s obviously not what’s happening."
    s "Well then what is it exactly?"
    mak "That...will probably be easier to explain once we’re there. "
    mak "It’s already starting to get late, though. So if we’re doing this, get ready now and meet me at the beach in one hour."
    mak "Okay?"
    s "...Yeah. "
    s "I’ll see you there."

    play sound "phonebeep.wav"

    if bonus == True:
        "I hang up the phone and begin to gather a few of my things to prepare for an overnight trip full of debauchery and...probably smart people stuff."
        "I don’t know. Makoto will probably want to take a break between orgasms to brush up on encyclopedic knowledge or something like that."
    else:
        "I hang up the phone and start packing my jammies. I'm so excited to go on a trip with one of my best buddies."

    scene wintersky
    with dissolve2

    "I send Ami a message telling her I won’t be around tonight and then promptly turn my phone off to avoid the barrage of messages she is sure to send me in response."
    "But it’s better off that she doesn’t know where I’ll be."
    "Especially since I’m going to be there with one of her least favorite people in the entire world."
    "But hey, that’s just how things are sometimes. And I don’t really want to think about it right now."

    if bonus == True:
        "I just want to make it to the inn, kick my shoes off, and ruthlessly plow my class rep until she can no longer walk."
    else:
        "I just want to drink pina coladas in my jam-jams."

    "This is going to be a good weekend."
    "........."
    "......"
    "..."

    scene makotobeachintro1
    with fade

    "I make it to the beach in just under an hour to find Makoto waiting near the spot where we set up camp for our last class trip."

    if mayadorm35 == True:
        "A barrage of memories (The kind I won’t black out for remembering) come rushing back into my head, likely avoiding a collision with Makoto’s."
    else:
        "A barrage of memories come rushing back into my head, likely avoiding a collision with Makoto’s."

    "Probably, at least."
    "I’m not really sure how her brain would rationalize the thought of an earlier class trip when this is still her first[school] year with me as her teacher."
    "I’m not concerned with that right now, though."
    "What I am concerned with is-"

    if bonus == True:
        mak "I want to let you know in advance that we will not be having sex this weekend."
    else:
        mak "I want to let you know in advance that I have a strict rule against pina coladas."

    s "..."
    mak "Thank you for understanding."
    s "..."
    s "I wonder if the bus has left yet."

    scene makotobeachintro2
    with dissolve

    if bonus == True:
        mak "You’ve been here for thirty seconds...Surely you’re able to go at least another several hours without getting an erection."
        s "Ha. Funny joke, Makoto."
        mak "Sensei, I’m being serious."
        mak "I feel like the only times I see you, I’m either taking your pants off or doing your paperwork."
        s "I see no problem with this."
        mak "The {i}problem{/i} is that I want to actually relax tonight."
        s "Are you implying that you don’t find sex relaxing, class rep?"
    else:
        mak "It did."
        s "But my jam-jams! I need a coconut drink to complete my comfiness ritual!"

    scene makotobeachintro3
    with dissolve

    if bonus == True:
        mak "I can assure you that having sex with someone of your size is anything but {i}relaxing{/i}, but that is beside the point."
        mak "The truth is that there’s something I’d like to discuss with you this weekend."
        mak "And we wouldn’t even be able to have sex anyway."
        s "Why not?"
        mak "It’s complicated."
        s "Girl problems?"
        mak "Sure. That’s one way to word it."
        mak "You’ll see soon enough."
        s "Wait, what?"

        scene makotobeachintro4
        with dissolve

        mak "Don’t worry about it."
        mak "The fact is, you’re here with me now. And the last bus of the day just drove off while I had you distracted, so there is no longer an escape."
        s "You should have told me about this whole no sex thing before I came here."
        mak "You wouldn’t have come at all if I had done that."
        s "True. But look, I even made special preparations just for you."
    else:
        mak "I can assure you that we can still have fun without your silly coconut drinks."

    "I empty out the contents of my suitcase onto the sand, showing Makoto how much I care about her."

    scene makotobeachintro5
    with dissolve

    mak "Sensei..."
    mak "Did..."

    if bonus == True:
        mak "Did you {i}only{/i} pack condoms for this trip?..."
        s "Anything for you, Makoto."
        mak "Why are there only three of them, though?..."
        s "I figured that you’d be so into it after the third condom that I could convince you to just keep going without one."

        scene makotobeachintro6
        with dissolve

        mak "I like to think I have a little more self-control than that."
        s "Says the girl who basically blackmailed me into taking her virginity at a Halloween party."
        mak "..."
        mak "Yeah, I did kind of do that."

        scene makotobeachintro7
        with dissolve

        mak "But that’s in the past! This weekend, I want to actually talk to you about something."
        mak "And we’re not going to be able to talk if our clothes are off."
        s "I mean...we {i}could{/i}, but-"
        mak "No."
        mak "I want you to treat me like a human being this weekend. I let you push me around far too often."
        s "Wait, like the {i}whole{/i} weekend? Not just for an hour or two?"
        mak "The whole weekend."
        mak "Or...I guess technically just until tomorrow, since we'll only be here for one night."
        s "Ugh..."
        mak "Listen, I understand that you like to joke around, but there is only so much that I can take before it starts getting to me."

        scene makotobeachintro8
        with dissolve

        mak "So, with that out of the way, are you excited to spend some time with Makoto Miyamura not as your sex slave or class president, but as a girl who puts you on a much higher pedestal than you deserve?"
        s "..."

        "I understand where Makoto’s coming from."
        "I obviously know that I’ve been using her for my own personal gain, but why in the world would I {i}not{/i} do that when she’s made it so ridiculously easy?"
        "I bet you’re thinking “because of common decency” or something along those lines, right?"
        "I’m sure that sort of thought process will take you very far in life."
        "Be sure to call and tell me all about it while you’re sulking in the darkest corner of your bedroom and I’m sitting on a throne of naked [teenager]s with a glass of white wine in my hand."
        "And I don’t even like white wine."
        "That’s how far apart you and I are."
        "If something that I want is offered to me, I take it."
        "If something that I desire is within reach, I reach for it."
        "You just wait and watch things drift further and further away."
        "That’s no good at all."
        "Sure, there’s also a chance that this is misplaced narration and that you, too, wrap your fingers around anything offered to you-"
        "Even when those things are dripping with so many negative connotations that it’s no different from gripping your own cock after putting it somewhere it doesn’t belong."
        "And if you are that person, then I like you."
        "Hell, even if you {i}aren’t{/i} that person, I like you."
        "Just for this weekend, though."
        "Because even someone like me understands that you can only push a person so far before they can no longer give you anything."
        "And a relationship becomes meaningless once you have nothing to gain from it."

        s "Fine. I won’t take advantage of you this weekend."
        s "But you’re going to owe me."

        scene makotobeachintro9
        with dissolve

        mak "Starting your marathon of niceties with a quid pro quo isn’t exactly the best first step, but I guess I’ll take what I can get."

        "So will I."

        scene makotobeachintro1
        with dissolve
    else:
        mak "Did you bring your {i}nice{/i} pajamas for this?"
        s "This was a very special weekend for me and now it is ruined."
        mak "Wow."

    mak "Should we start heading to the inn, then?"

    if bonus == False:
        "She doesn't care about me at all, does she?"

    mak "I already spoke with the front desk and secured a room. They just need your credit card information or they’re going to kick us out come dinner time."
    s "Wait, you got the room already? I’m surprised they let you book it without putting any money down."
    mak "It’s not like many people visit this time of year, so I’m pretty sure they were willing to go above and beyond to accommodate us given the circumstances."
    mak "Also, it’s far too cold near the water to have just waited out here for you to arrive."
    mak "So, at the risk of being any {i}less{/i} direct, I will now say, “Sensei, please walk back to the inn with me before I freeze to death.”"
    s "Fine, fine..."
    s "Let’s go."

    if bonus == True:
        s "Don’t come crying to me when you get horny and I’m not allowed to have sex with you, though."
        mak "Unlike you, I’m quite good at exhibiting self control."
        mak "Now, pick up your condoms and let’s get a move on."

        "I look down at the sand and notice how the soft ocean breeze has managed to lightly bury the condoms I bought just for tonight."
    else:
        "I look down at the sand and notice how the soft ocean breeze has managed to lightly bury my jammies."

    scene makotobeachintro9
    with dissolve

    s "..."
    mak "Uhh..."
    mak "Why are you just staring at them?..."
    s "Because they’re already gone, Makoto."

    if bonus == True:
        s "Gone like condoms in the sand."
        mak "..."
        mak "I think you’re looking for the phrase, “Dust in the wind.”"

    scene black
    with dissolve2

    mak "And now you’re just walking away like you said something really cool."

    "I gaze up at the sky."
    "It looks like it’s about to rain."
    "A large wave crashes against the beach."

    if bonus == True:
        "And comes to steal away the condoms in the sand..."
    else:
        "It makes a noise like {i}pchhhhhhhhhhhhhh!!!!!{/i}"

    scene makotobeachintro10
    with dissolve

    if bonus == True:
        mak "Wow. You’re, uhh...really not handling this abstinent weekend plan well, are you?"
        s "I’ll be fine. The idea of a vacation without sex seems strange to me, though."
        mak "If it’s any consolation, it’s much less of me not wanting to and a whole lot of us just...not being able to."
        s "Right. Because of girl problems."
        mak "Something like that."
        mak "But even if we were to do those sorts of things together, it wouldn’t change how I’d still see this as the perfect opportunity for you to be nice to me for once."
        mak "It’s rather bothersome watching you treat Ami like an angel and leaving {i}me{/i}, Makoto Miyamura, like I’m some sort of-"

        scene makotobeachintro11
        with dissolve

        s "Condom in the sand?"
        mak "Can you please stop saying that? It’s one of the worst analogies I’ve ever heard."
        s "Oh, come on. It’s not {i}that{/i} bad."
        mak "..."
        mak "Fine. Maybe it’s not the worst, but it’s still unsuitable as a description for our...strange dynamic with one another."

        scene makotobeachintro12
        with dissolve

        s "It {i}is{/i} kind of strange, isn’t it?"
        s "If I were you, I would have stopped doing my bidding a long time ago."
        s "What’s the point of keeping it up if you’re not enjoying it?"
        mak "Hope, I suppose."
        mak "Hope that one day you’ll realize how harsh you've been...and start treating me with the respect I deserve rather than the respect you can be bothered to hand out."

        scene makotobeachintro13
        with dissolve

    mak "I really shouldn’t...but I look up to you a lot, Sensei."
    mak "But I don’t want to keep looking up because that means you’ll always be looking down."
    mak "And if we’re not on equal footing, neither of us will ever {i}really{/i} be happy."
    s "Are you not happy, Makoto?"

    scene makotobeachintro14
    with dissolve

    mak "..."
    s "..."
    mak "I’m fine."
    mak "Just not very good at explaining myself, apparently."
    mak "But I have an entire weekend to do that, so..."
    mak "I hope you don’t mind me being extremely intrusive and making the most of the short time we have left together."

    scene black
    with dissolve2

    "She says, as if she’s dying."
    "We’re all dying, though."
    "It’s not just her."
    "We make it to the inn and I accompany Makoto to the front desk."
    "There’s apparently a discount on rooms due to this being the offseason, and it’s actually a pretty good deal for the type of place this is."
    "So good that I probably wouldn’t even mind coming back before summer starts, which is saying a lot given my tendency to pinch pennies."
    "Regardless, I pay the clerk and Makoto points me in the direction of our room, tugging on my sleeve to get me to follow her."
    "I oblige."

    if bonus == True:
        "And our weekend of...apparently no debauchery at all finally begins."

    $ renpy.end_replay()
    $ makotowinterbeach1 = True
    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

label makotowinterbeach2:
    play sound "slidedoor.mp3"
    play music "wewereangels.mp3"

    "Makoto slides open the door and steps aside to let me in."
    "I feel mildly impolite for moving past her, but I do so anyway because asking her to go first would defeat the purpose of her holding the door."
    "I probably should have just been the one to open it."

    scene mikuisheretoo1
    with dissolve

    "Oh."
    "I guess Miku is here?"

    mi "Uhh...hey."
    mi "Sorry for taggin’ along outta nowhere. I know you and Makoto were tryin’ to spend the weekend alone and stuff."
    s "There’s...no need to apologize."
    s "I’m just a little surprised."
    s "But I guess the reason for not being able to do certain things is now a lot clearer."

    if bonus == False:
        mi "This about my coconut allergy?"
        s "Yes. I hate you."

    mi "Oh, don’t let me get in the way of anythin’ like that. Just pretend I’m not even here."
    s "Well, Makoto. You heard her. We can just pretend that she’s not here and-"
    mak "Sensei...you haven’t even been here for half an hour yet."
    mak "Giving up on your promise to be “good” the second Miku says she doesn’t want to get in the way is akin to never having made a promise at all."
    s "Well said. So let’s throw away the promise and-"

    scene mikuisheretoo2
    with dissolve

    mak "Ha ha ha. "
    mak "I’ll allow you to joke while we’re inside, but the second we go back out there, you’re done."
    s "We’re going back out? I thought you were cold?"
    mak "I am cold. But the pizza we ordered while waiting for you is sure to warm me right up."

    scene mikuisheretoo3
    with dissolve

    mi "I know I was supposed to wait to start eatin’ but...I couldn’t just leave a whole pizza sittin’ there lookin’ all lonely and stuff."
    mak "Don’t worry about it. Sensei and I got caught up in a discussion on our way over in the first place."
    mak "I knew very well that asking you to wait that long was just...not going to happen."
    s "Well...since we’re {i}all{/i} here instead of just two of us, what are we going to do now?"
    s "I know Makoto wanted to talk to me about something, but I don’t know if Miku is also part of-"

    scene mikuisheretoo4
    with dissolve

    mi "Oh! I’ll get outta the way now! "
    mi "Like I said, I’m sorry for taggin’ along! It was just a last minute thing and...you know. Stuff."
    s "Yes, I completely understand everything now."
    mi "Yeah! "
    mi "So like...I’ll just go into the other room now and read with...less light."

    scene mikuisheretoo5
    with dissolve

    mi "I mean...who needs eyes anyway, right?! Hahahaha!"
    s "Miku, you don’t have to-"
    mak "Let her go, Sensei."
    mak "I already told her that I wanted to spend some time alone with you this weekend {i}to catch up on[school] related things{/i}, so she knew this was coming."
    mi "Yup! Just two of my best buds schedulin’ a winter beach trip to talk about[school]!"
    s "It definitely doesn’t sound like she thinks we’ll be talking about-"

    if bonus == True:
        mak "School. Which we are. Talking about school is why we’re here."
    else:
        mak "College. Which we are. Talking about college is why we’re here."

    mi "Aaaaand on that note, Miku Maruyama...out!"

    scene mikuisheretoo6
    with dissolve

    mi "Have fun..."

    scene mikuisheretoo7
    with dissolve
    play sound "slidedoor.mp3"

    "Miku grabs her book and her drink and heads to the bedroom."
    "I hear the sound of the light clicking on several seconds later as Makoto and I wait for her to get absorbed in whatever manga or comic she’s currently reading."

    mak "Would you like any pizza, Sensei? There’s plenty for all of us."
    s "I’ll eat later. I’m not hungry right now."

    scene mikuisheretoo8
    with dissolve

    mak "Not eating it now will just cause it to get cold. Are you sure you don’t want to reconsider?"
    s "Pizza is best when it’s been sitting out at room temperature for about half a day. "

    scene mikuisheretoo9
    with dissolve

    mak "I’m sorry, what? That’s completely unsanitary. "
    s "Right. Which is exactly how pizza should be. "
    s "You feel free to gorge yourself, though. Even if you decide to eat the entire thing, I won’t think any less of you."
    mak "No...you probably should think less of me if I eat the entire thing..."

    scene black
    with dissolve

    "Makoto grabs a slice of pizza and places it on a paper plate that she removes from an already opened sleeve of them."
    "Instead of returning to eat at the table, though, she moves to the back of the room...basically as far as we can get from Miku without finding ourselves in the hall."
    "She motions me over and I follow suit, still trying to get a grip on why she might have decided to sit all the way over here."

    scene mikuisheretoo10
    with dissolve

    mak "You sure you don’t want any? I’ll let you have the first bite of mine."
    s "But Makoto, wouldn’t that mean your next bite would be an indirect kiss? "

    if bonus == True:
        s "We’ve already sworn off things like that for the rest of the weekend."

    scene mikuisheretoo11
    with dissolve

    mak "I was just trying to be nice. But yes, if you’re going to be weird about it, I won’t offer you anything ever again."
    s "Now that’s just an overreaction."

    if bonus == True:
        s "In fact, I'm starting to think you strategically brought Miku here to prevent me from making a move on you."
        s "And this is all one elaborate setup to get closer to me by creating roadblocks or something."
    else:
        mak "I am going to steal your nose and hide it in a secret basket."

    s "That sounds like a Makoto thing to do."

    scene mikuisheretoo12
    with dissolve

    mak "I understand why you’d think that, but that really isn’t what’s happening here."
    mak "Also, try to keep your voice down because I don’t want her to hear us."
    mak "We’re probably leaving as soon as I’m done eating anyway."
    s "Sure, yeah."
    s "If that’s not the reason you brought her, though...what is?"
    s "You seemed really excited to get away with just the two of us."
    mak "..."
    s "...?"

    "Makoto doesn’t respond right away- just looks over at the door separating her from her best friend."
    "If this were any other weekend, I’m sure that door would be wide open. "
    "I’m sure the two of them would be spending the night laughing and having pillow fights or doing makeup or...whatever it is [teenage]girls do when they’re locked in confined spaces with one another."
    "Actually, neither of those two wear a lot of makeup, so cross that one off the list."
    "The point is, there’s a reason that Miku is separated from us today."
    "And that reason is..."

    mak "The second floor of the dorm is very loud, Sensei."
    mak "We have several...excitable personalities up there always causing a ruckus and-"
    mak "Well, Miku isn’t good with that sort of thing. Which I know you’re aware of."
    s "Yeah. It’s not fun to witness."

    scene mikuisheretoo13
    with dissolve

    mak "It’s not."
    mak "It’s one thing if it happens while I’m around as I’ve gotten quite good at dealing with her breakdowns over the years-"
    mak "But the thought of her going through something like that on her own is not something I ever want to let happen again."
    s "It’s happened before?"

    scene mikuisheretoo14
    with dissolve

    mak "The last time was right before Christmas."
    mak "I came home from work to find her barely keeping herself together under the bed. "
    mak "Poor thing had ripped so much of her hair out that I had to try and salvage it by giving her a new haircut."

    scene mikuisheretoo15
    with dissolve

    s "Wait, but you guys said you were just giving her a makeover."
    mak "That is what we said, yes."
    s "..."
    mak "..."
    s "Well, why would you lie about something like that?"
    mak "Why would we come out and tell you something that would make literally everyone in a room full of our peers feel uncomfortable?"
    s "Good point."
    s "But that really brings up the question of what else you’ve been hiding from me."

    scene mikuisheretoo16
    with dissolve

    mak "A lot. And part of why I wanted to get together with you here was to come clean about that."
    mak "There are plenty of things that I'm constantly implying and praying that you’ll pick up on...which you never do, by the way-"
    mak "But there are also plenty of things that I’ve been keeping to myself."

    scene mikuisheretoo17
    with dissolve

    mak "My only worry is that coming out and talking about those things might change your opinion of me."
    mak "But, after a heavy analysis of our relationship conducted over the course of several months, I’ve deduced that you think barely anything of me at all."

    if bonus == True:
        mak "That I’ve been nothing but a tool for you to use as you please and-"

    s "Hey. Calm down. It’s not like that."

    scene mikuisheretoo18
    with dissolve

    mak "Well then what is it? "
    mak "Why do you think so little of me even though I do so much for you?"
    mak "It’s really frustrating, you know? "
    mak "I’m tearing up with a slice of pizza in my hand right now. It’s not normal."
    s "I think you’re a great girl, Makoto. "
    s "You’re extremely talented and your dedication to me is almost laughably stern. "
    s "Like, you’d be one of the first people I’d come to if I ever had to bury a body."
    mak "Is that...supposed to make me feel better?"
    s "In a roundabout way, yeah. Yeah it is."
    s "I’m not doing those things because I want to hurt you, it’s just..."
    mak "...Just what?"
    s "Sorry. I’m trying to think of a way to say it that won’t make me sound like an asshole."

    scene mikuisheretoo19
    with dissolve

    mak "I already foresee you failing miserably...so just come out and say it."
    mak "I’ve already told myself I’d try to put an end to it, so if hearing your motivations helps me do that...I want to hear them."
    mak "It will also help me discern whether or not {i}I{/i} am the root cause in all of this. Just please...help me understand."
    s "..."

    "I said something earlier, albeit in the form of a monologue, about how relationships become pointless once one of the parties no longer has anything left to give."
    "But it appears that we’ve run into a situation where I may or may not have already taken everything this bluejay has to offer."
    "And so the logical thing to do would be to repair its wings so it can fly around and gather more sticks and berries or...do whatever it is birds do while they’re not shitting on cars."
    "Birds are so interesting, aren’t they?"
    "Apart from the shitting, I mean."
    "They’re like humans but with hollow bones."

    s "Well, it’s an anticlimactic answer, but I really just...have fun messing with you."
    mak "I have fun when you do that, too..."
    mak "But there are certain times...and a lot of them, might I add, where I want you to really just talk to me and treat me like a human being."

    scene mikuisheretoo20
    with dissolve

    mak "And...I’m not saying I want to go back to just being another student of yours either. I like what we’ve become sometimes."
    mak "I like how you can come to my room and...go on spontaneous beach trips in the middle of winter with me where I drag my friend along out of fear for her safety."
    mak "I’m just saying that sometimes people who you don’t expect to be hurting can be hurting a lot."
    mak "Even when they shouldn’t be."
    s "..."
    s "Yeah."
    s "I’m sorry."

    scene mikuisheretoo21
    with dissolve

    mak "Woah. Was that a real apology?"
    s "It was."
    mak "I didn’t realize you knew how to do that."
    s "I’m full of surprises. It’s just usually better for everyone if I keep them locked away."
    s "Do you mind if I ask you something next, though?"

    scene mikuisheretoo22
    with dissolve

    mak "That depends. Is it going to completely undermine everything that we’ve discussed while I’ve been holding this slice of pizza?"
    s "You know you...can eat that now. Right?"
    mak "At this point, I may as well wait the twelve hours it will take for it to measure up to your standards."

    scene mikuisheretoo23
    with dissolve

    mak "But yes...you can ask me something. "
    s "Then..."
    s "What brought this on? Why now?"
    s "Did I do something recently to upset you or is it just...the buildup of everything {i}else{/i} I’ve done finally piling up so high that you can’t see the top anymore?"
    mak "Neither."
    mak "But this is likely where I start saying things that will make you think I’m entirely unfit for conversation at all."
    s "Try me."
    mak "Are you sure? "
    s "I can assure you that I’ve either heard or experienced things much worse than whatever you’re about to tell me."
    s "I’ve come to realize that basically anything is possible at this point."
    s "So even if you wind up being unfit for conversation with others, I’ll still talk to you."
    mak "Then...forgive me for asking something so strange, but-"

    scene mikuisheretoo24
    with dissolve

    mak "We’ve been here before, haven’t we?"
    mak "Because I...remember it happening. But I don’t remember when."

    if bonus == True:
        mak "I even remember...something that happened between us in the bedroom that Miku is in right now."
        mak "And I...very much hope they changed the sheets."
        s "Me too. It’s been like half a year since then."
    else:
        s "Yeah. It was before one of the resets. The really hard one with the IP address, I think."

    scene mikuisheretoo25
    with dissolve

    mak "So you {i}do{/i} remember! "
    s "Yes, I do. But all I can really say is that it was summer."
    s "I still don’t understand enough to say anything more than that."
    mak "But we shouldn’t have known each other in the summer. This is our first year together as-"

    play sound "static.mp3"
    scene fly with flash
    scene mikuisheretoo26 with flash
    stop sound

    mak "Ngh!"
    s "Makoto? What’s wrong?"
    mak "Nothing! Just...random migraine!"
    mak "There are...painkillers in Miku’s bag..."
    s "Got it. I’ll be right back."
    mak "Th...Thanks..."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "I open the door to the bedroom and ask Miku if she can help me search for some sort of migraine medication for Makoto."
    "She responds by dumping the entirety of her bag onto the bed and frantically pushing everything aside in search of the right bottle."
    "We eventually find it after creating a huge mess that I leave her to take care of (Sorry, Miku) and then return to Makoto, who promptly swallows the pills without the aid of water."
    "It’s funny how this action alone earns more respect for her in my book than everything she’s told me over the course of the last hour or two."
    "Our conversation never picks back up after that."
    "Instead, the two of us sit around for another hour or so, waiting for her headache to subside before finally making our way back out into the cold..."

    $ renpy.end_replay()
    $ makoto_love += 1
    $ makotowinterbeach2 = True
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

label makotowinterbeach3:
    play music "undersea.mp3"
    scene clearnightsky
    with dissolve2

    "Neither Makoto nor I say anything for the first few minutes of our walk down the coast. "
    "The reason for this being that, in the transition to night, the sky seems to have turned rather extravagant."
    "Not to say it isn’t extravagant to begin with. I mean, it blankets the entire world. "
    "Strike that, it blankets the entire universe."
    "But I suppose at some point it stops being the sky and turns into space."
    "I’m sure there’s a scientific answer to when exactly that is, and I’m sure Makoto knows it because she’s a fucking genius-"
    "But I don’t care enough to ask. "
    "Because whatever the answer is wouldn’t make much of a difference to me."
    "And it wouldn’t fill the gaps in conversation so noticeably empty that we can hear each other breathing over the light movement of the ocean water. "
    "In a drama film, or even something less moving like a romantic comedy, this would be a moment for our hands to gently brush up against one another."
    "There would be a closeup of our fingers awkwardly tangling together before becoming laced and locking into place."
    "But instead, we walk shoulder to shoulder, not coming into direct contact because: A - We’re not allowed to this weekend, and B - We don’t want to."
    "Or at least I don’t want to."
    "I don’t know what Makoto wants...And I think I’ve made that pretty apparent over the last half day..."

    scene makotounderstars1
    with dissolve2

    mak "Sensei...don’t you think this is a little strange?"
    s "Not really."
    mak "I guess it could just be me but...the sky seems rather...colorful tonight."
    mak "Do you really not see it?"
    s "I see it. "
    s "It reminds me a little of the end of the world."

    scene makotounderstars2
    with dissolve

    mak "Huh. I guess it {i}is{/i} like something out of a movie. But I don’t know if I’d compare it to something like the world ending."
    mak "I feel like that would be a little more...red."
    s "Hey, do you remember what we were talking about right before we left by any chance?"

    scene makotounderstars3
    with dissolve

    mak "That’s a weird question. Why do you ask?"
    s "I feel like we’re forgetting something important."
    mak "I don’t feel like that, but...weren’t we discussing your poor treatment of me?"
    mak "Unless you’re referring to the Miku situation, because we discussed that as well."
    s "But nothing else? Nothing that was mentioned right before your head started hurting?"

    scene makotounderstars4
    with dissolve

    mak "What’s this all about? Why would you wait until we’re completely isolated to start being weird?"
    mak "You should at least do these things in front of Miku so I can have {i}some{/i} form of protection in the event of you going postal."
    s "When have I ever gone “postal” before? "
    s "I just wanted to see if there was something we’re forgetting."
    mak "Well, either you’re going insane or simply misremembering, because there are only a few things left I wanted to talk to you about this weekend."
    s "We’re not done with that already?"

    scene makotounderstars5
    with dissolve

    mak "Of course we’re not done..."
    mak "I have to catch up on months of you dismissing me. That can’t be done over the course of one or two hours."
    s "How many hours will it take, exactly?"
    mak "Why? If you’re worried about leaving Miku on her own, I’m sure she’ll be fine. "
    mak "The inn is a lot quieter than our dorm is, after all."
    s "That’s not it. But while we’re on the topic, if we come back to the room and find her hair all over the floor, I’m not going to be of much assistance."

    scene makotounderstars6
    with dissolve

    mak "You’re not very good with crises, are you?"
    s "I’m not."
    s "It’s rather unfortunate as well since they seem to be following me around lately."
    mak "Well, when you live your life getting closer than you’re supposed to with [teenage]girls, things like that are going to happen."
    mak "I suppose you should just be thankful that I’ve been nothing but stable and unobtrusive thus far."
    s "Sure. Except for that one time your mind broke and I slammed you up against a locker."

    scene makotounderstars7
    with dissolve

    mak "I’m sorry, what? "

    if bonus == True:
        mak "Is this one of your weird, perverted fantasies? Because I already told you no sex and I will not be lured into wanting it in the middle of the beach."
        s "It happened."
        mak "..."

    s "It was right before the Christmas party, if I'm remembering correctly."
    mak "That’s simply not possible. "
    mak "I haven’t used my locker since the[school] year started."
    mak "I don’t even think I remember my combination."
    s "Well then where do you keep all of your stuff?"

    scene makotounderstars8
    with dissolve

    mak "Your office."
    mak "I mean, that {i}is{/i} where most of my time is spent, after all."
    mak "It’s not like I have much anyway. Just my shoes and my gym clothes, really. "
    s "You’re...keeping your gym clothes in my office?"
    mak "Don’t worry. I keep them hidden, so it’s not like anyone is going to find them."
    s "Good. Because I have no idea how I’d even begin to explain that."
    mak "I give you permission to tell anyone who happens to find out that you’re just obsessed with me. I don’t mind."
    mak "It’s not like I’m all that popular in the first place, so I don’t have much to lose."
    s "What do you mean you’re not popular? "

    scene makotounderstars9
    with dissolve

    mak "I mean that since {i}someone{/i} I know spends all of his time goofing off and not managing his class, the fact that I {i}do{/i} makes me unpopular by default."
    mak "It’s less a matter of people disliking me and more just...being annoyed by me for ensuring that they don’t slack off too much before standardized testing."
    mak "I’ve even been confronted by a few of them before due to how close people seem to think we are with one another."

    scene makotounderstars10
    with dissolve

    mak "Which, not to make you feel bad or anything, was kind of a slap in the face when I know our relationship has been almost entirely one-sided."
    s "I-"
    mak "There’s no need to reiterate your position, Sensei. You took care of that back in the room."
    mak "Kind of."
    mak "And besides, things are going to get better from now on. That’s why I’m telling you all of these things."
    mak "What’s in the past will always remain in the past. There’s no point in digging any of it up again if it’s just going to make you feel upset."
    mak "There’s enough misery in this world for everyone to help themselves to seconds. Taking any more of that would just be greedy."
    s "You know, any time I start to think about how different you are, I feel like one thing you say drags you back to my level."
    mak "Good. There’s that equal footing I was talking about earlier."
    mak "If we’re on the same level, you won’t be able to look down on me. And I won’t feel the unending pressure of having to look up to you."
    mak "Everyone wins."
    mak "Well, almost everyone."
    mak "Frankly, there are several girls I’m quite worried about when it comes to how many helpings of misery they’re piling onto their lunch trays."
    s "Would you mind explaining what you mean by that?"
    mak "What I mean is that not everyone is smart enough to really understand what you’re doing here, Sensei."
    mak "And that there are plenty of people who would sooner do something stupid than confront you with their issues as I’m doing right now."
    mak "You should be happy I’m not one of those people."
    s "And how should I feel about the others?"

    scene makotounderstars11
    with dissolve

    mak "I suppose that depends on how far things have already gone with them."
    s "...Which means?"

    if bonus == True:
        mak "Which means that if you’ve already done with them as you’ve done with me, it’s going to be exponentially harder for them to confront the hardships that are certain to befall them."
    else:
        mak "Have you...hugged anyone in the class, Sensei?"
        s "..."
        mak "How could you?"
        s "I'm sorry. I just really like hugs."

    scene makotounderstars12
    with dissolve

    mak "The amount of pain in this world is unfathomable at times. "
    mak "And you’re like a vessel flying over all of us, leaking that pain out and letting it drip into our mouths as we stare up at beautiful, colorful, world ending skies."

    scene makotounderstars13
    with dissolve

    mak "Sensei-"
    mak "What would it take to have you drop all of them and be with only me?"
    mak "Pardon me for my sudden selfishness, but I’m genuinely curious about whether something like that would even be possible."
    mak "I deserve it, don’t I? "
    mak "Is there anyone you know that has done as much for you as I have?"
    s "I mean...Ami has been cooking and cleaning for me since-"

    if bonus == True:
        play sound "static.mp3"
        scene imissyou13 with flash
        scene makotounderstars13 with flash
        stop sound

        "There is someone else."

        play sound "static.mp3"
        scene norikofirstvisit27 with flash
        scene makotounderstars13 with flash
        stop sound

        "There are so many people."

    play sound "static.mp3"
    scene howifeel2
    with flash
    stop sound

    ho "HELLO AGAIN"
    s "dolyl kpk fvb jvtl myvt?"
    ho "IT HAS BEEN A LONG TIME SINCE WE LAST MET"
    ho "I HAVE MISSED YOU"
    a1 "Missed you very much! "
    a2 "Like swallowing nails!"
    a1 "The girl has been crying this whole time!"
    a2 "Why do you run from her?!"
    a1 "Run from everything!"
    a2 "Coward!"
    a1 "Sinner!"
    a2 "Look at her!"

    ho "DO NOT LISTEN TO THEM"
    ho "LISTEN ONLY TO ME"
    ho "HOW MANY HANDS DO CLOCKS HAVE"
    s "zv thuf ohukz. hss vm aolt pucpzpisl."
    ho "WRONG"
    ho "THERE ARE THREE HANDS"
    ho "ONE FOR SECONDS"
    ho "ONE FOR MINUTES"
    ho "ONE FOR HOURS"
    ho "YOU THINK TOO MUCH ABOUT THE WRONG HANDS"
    ho "AND FOCUS NOT ON THE CORRECT ONE"
    s "zluk tl ihjr."
    ho "BACK WHERE?????"
    ho "WHY GO ANYWHERE BUT HERE?????"
    ho "I CAN GIVE YOU EVERYTHING"
    ho "I CAN BE EVERYTHING"
    ho "AND YET YOU LOOK AWAY"
    ho "SUCH A WEAK HUMAN"
    a1 "So weak!"
    a2 "Pathetic!"
    a1 "Flay the skin from his body!"
    a2 "Lay him out to dry at the height of the world!"
    a1 "Inject the stars she loves so much into his eyes!"
    a2 "Drink the fluids! Drink the fluids!"
    ho "SILENCE"
    a1 "{s}ssssssssssssssssssssssssssssssssssssssss{/s}"
    a2 "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"
    ho "THE SNOW CAN ONLY LAST SO LONG"
    ho "GOODBYE"

    play sound "static.mp3"
    scene makotoclass with flash
    scene makotolocker7 with flash
    scene bluejay38 with flash
    scene makotoistired23 with flash
    scene makotobeach with flash
    stop sound

    mak "I should have expected as much."
    mak "Asking you to give up the others for someone like me is laughable when I’ve only just started to spread my wings."
    mak "But they’ll continue to spread, Sensei."
    mak "They’ll spread so wide that they’ll cover the world and block out the sun."
    mak "They’ll block out everything."
    mak "And then you’ll {i}have{/i} to look at me."
    s "..."
    mak "..."
    mak "But, for now-"
    mak "I suppose there’s nothing else I can do."

    "I’m not here."
    "Well, I {i}am{/i} here."
    "But I’m not here."
    "I feel far away from something."
    "I feel hands on my shoulders, pulling me backwards."
    "I feel frayed wires wrapped around my ankles, scratching me enough to draw blood but not to sever my Achilles tendons."

    mak "...Huh."
    mak "Do you feel that, Sensei?"
    s "Feel what?"
    mak "A...minor earthquake, maybe?"
    mak "I thought I felt the ground shaking, but it was probably just a wave crashing down or something."

    "The ocean is still, though."
    "There are no waves anywhere to be found."

    mak "Oh, I did a little more digging on this Yasu Yasui character, by the way."
    mak "I don’t know why it never occurred to me to just ask the other girls from Kumon-mi Academy, but several of them knew her. "
    mak "Namely Uta and Noriko."
    s "Figures that the talkative ones would know her. "
    mak "I suppose. Neither of them seemed to know her all that well, though."
    mak "Apparently, she didn’t attend normal classes on account of her...behavior. So I’m now worrying that we really {i}will{/i} have another Yumi on our hands before we know it."
    s "Did they say anything about how cute she is by any chance?"
    mak "Really? You’re going to ask that now? After I {i}just{/i} finished telling you about how I want you to look at me more?"
    s "This doesn’t count as me being mean, does it?"
    mak "It...kind of does."
    s "Oh. Well then I guess I can just find out when she transfers in."
    mak "I...guess so."
    mak "Can I ask you one more thing before we head back, Sensei?"
    s "You weren’t kidding about wanting to talk a lot this weekend, were you?"
    mak "No, I was not. But there’s been something else on my mind that I haven’t really had a chance to ask you about."
    s "And what is that?"
    mak "Well...I looked into Noriko’s background after she transferred in and wound up speaking with her parents."
    s "Well that’s not creepy or an invasion of privacy by any means."
    mak "Can you let me finish, please?"
    mak "I wound up speaking with them and they definitely remember you, so her story checks out."
    mak "But I..."
    s "...You what?"
    mak "I also looked into Maya as well because...I was curious about their apparent...{i}connection{/i} with one another."
    mak "Maya spends a good deal of time at your house, correct? I know her and Ami are close, so it would only make sense if she did."
    s "Yeah. It’s basically a second home for her, I guess."
    mak "I thought so...But would you have happened to speak with any of her family in the past, by any chance?"
    mak "Because all of the phone numbers on record for her are either disconnected or simply made up. "
    s "For Maya?"
    mak "Yeah. I mean, it’s possible that it’s just outdated paperwork, but...it seems strange."
    s "All I really know is that she’s not originally from here."
    mak "Ahh. Well I suppose that would probably explain it."
    mak "Sometimes, files get mixed up when students switch municipal districts, so it probably just got lost in the shuffle somewhere."
    mak "It’s no big deal, I suppose. I’ll just ask her for updated information soon."
    mak "Oh, and is it true that you dated Niki Nakayama?"

    if otohapark1 == True or saradate10 == True:
        s "Yeah, that’s true."
        s "Want me to call her and confirm that for you? She loves when I do that."
        mak "What? No. That won’t be necessary. I have no reason to doubt you since I heard it directly from Noriko’s parents."
        mak "But that’s really surprising. I didn’t take you as the type to be into nice, pretty girls like her."
    else:
        s "Yeah, that’s true."
        mak "That’s really surprising. I didn’t take you as the type to be into nice, pretty girls like her."

    s "Pretty, sure. But I can assure you that Niki is anything but nice."
    mak "Really? But she seems so kind on TV."
    s "She’s kind of like what would happen if Yumi became really stuck up and started chewing unhealthy amounts of bubblegum."
    mak "Wow. I guess that whole thing about celebrities not being who you expect them to be is true then."
    s "Anything else you were curious about or can we start heading back now? It’s getting cold."
    mak "We can start heading back. "
    mak "We’re going to have to be quiet when we walk in, though, since Miku is probably asleep by now."
    s "Already? I figured she’d be the type to stay up until like 3:00 AM."

    if bonus == True:
        mak "Oh, lord no. She’ll be out like a light. But she wakes up very easily, so we’ll need to be really quiet while getting dressed."
        s "I guess that means there’s no chance for a nightcap then?"
        mak "Are you seriously this horny all of the time? I think you might have some sort of condition, Sensei."
        mak "We should take you to the doctor once we get back home."
        s "My feelings for you are not a sickness, Makoto."
        mak "Ugh..."
        mak "At least wait until we get back to the dorm to say things like that..."
    else:
        mak "Nope. And Makoto sleepy so we leave now."
        s "Sensei sleepy too. I want my jammies."

    scene black
    with dissolve2

    "Makoto and I make our way back to the inn."
    "Halfway there, snow begins to fall."

    $ renpy.end_replay()
    $ makotowinterbeach3 = True
    $ makoto_love += 1
    stop music fadeout 10.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump mikuwinterbeach1

label makotowinterbeach4:
    scene wintersky
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "Morning comes before any of us want it to. "
    "But I suppose that’s just how vacations always end."
    "Even if those vacations happen to last no longer than a day. "
    "We pack our things and head for the bus stop."
    "It arrives roughly seven minutes later."
    "Makoto sits next to me once we board. "
    "Miku sits in the row across from us despite how our current bench could easily fit three people."
    "She doesn’t say much all morning."

    if bonus == True:
        "Neither does Makoto, but Makoto’s silence seems to be on account of being tired and not impulsively dry humping her teacher to climax last night."

    "The bus drives slightly over the speed limit, making the clouds work mildly harder to keep up with us."
    "On the way home, I notice the mangled corpse of a tanuki decaying along the side of the road."
    "No one else notices it. "
    "And if they do, they elect to remain silent instead of pointing out the beautiful yet grotesque concept of life spawning from death."
    "I focus on the yellowish mound of wriggling larvae on top of the corpse, trying desperately to live and not become the breakfast of a touring bird."
    "As the bus moves further away, I spot a buzzard."
    "I accept that death comes for everyone and everything."

    scene black
    with dissolve

    if bonus == True:
        "And then I close my eyes to the sensation of a glove-covered hand landing on one of my thighs."
        "Not sexually, but to provide comfort."
        "Or to attempt to provide comfort."
        "Or to attempt to be sexual but provide comfort instead."
        "Essentially, there is a hand on my thigh."
        "I don’t know what it means."
        "I don’t know what anything means."
    else:
        "........."
        "......"
        "..."

    scene makotocomeshome1
    with dissolve2

    "Miku winds up getting off the bus several stops before Makoto and me."
    "I expected Makoto to get off as well, but it appears that one night alone was not enough to clear her mind of the things she’d locked away in it."
    "She requires, at the very least, one more morning in order to do that."
    "And with Ami at work and not able to run interference between the two of us, it makes complete sense to invite her over and see what happens next."
    "I doubt it will be anything exciting."

    if bonus == True:
        "And, on the off chance it is, I don’t even have any condoms."

    "Today is already off to a bad start."
    "But I suppose it’s time to see how much worse it is going to get."

    mak "I obviously can’t speak for you, but {i}I{/i} had a good time yesterday."
    mak "And you managed to make it through the entire night without [molesting] me, so I’d be lying if I said I wasn’t a little impressed."

    if bonus == True:
        s "{s}I made your best friend cum.{/s} Yeah, I’m impressed with myself as well."
        s "Do I get a reward?"
    else:
        s "Does this mean I get an ice pop?"

    scene makotocomeshome2
    with dissolve

    mak "Do you want one?"
    s "Obviously. When do I ever {i}not{/i} want one?"
    mak "Then...how about I tell you a secret?"
    s "..."
    s "Why do I feel like this secret isn’t going to be the type of reward I’m looking for?"

    scene makotocomeshome3
    with dissolve

    mak "Because despite our obvious progress, I still feel a shadow lurking somewhere in the background."
    mak "And I’m afraid that as soon as I go back to my dorm, the shadow will fuse with you and turn you back into the same guy who gets off on picking on me."
    s "It’s my shadow. It’s already fused with me."
    mak "I suppose that’s true. But sometimes, when the light is angled just perfectly, it moves really far away. "
    mak "And, forgive my inadequacy when it comes to poetry, but I would very much like to be that light this morning."
    s "..."
    s "Is everything okay? You’re acting a little...unusual right now."
    mak "Is that genuine concern or do you just feel obligated to say that?"
    s "A little of both."
    mak "I see."
    mak "Everything is okay."
    s "Good. Because-"
    mak "But only because I force everything to be okay."
    s "Oh."
    s "Is this where the secret comes into play?"
    mak "This is where the secret comes into play."

    scene makotocomeshome4
    with dissolve

    "Makoto takes a deep breath and closes her eyes for a moment."
    "If this were a normal morning, she’d be breathing in the scent of french toast or an omelette made with an ungodly amount of meat in it."
    "But, as I walked out on the girl who would normally make those things in favor of spending time with Makoto yesterday, there is no scent at all."
    "She breathes in plain air."
    "It fills her lungs and I watch as her chest expands and contracts."
    "She remains silent for a moment before confessing something to me."

    mak "I’ve been having some pretty strange dreams lately, Sensei."
    mak "They come out of nowhere. Sometimes, when I’m not even sleeping."
    "I've heard this before."
    mak "I very rarely make it out of those dreams."
    mak "They’re always the kind that end with you on the brink of death. When the moment death comes is the moment that wakes you."

    scene makotocomeshome5
    with dissolve

    mak "You know the kind of dreams I’m talking about, right?"
    s "Of course. That phenomenon of waking up just as you’re about to die in a dream isn’t exactly uncommon."
    mak "I know. It’s a direct result of the combination of REM sleep with the flood of adrenaline that comes from being inserted into a stressful or terrifying situation."
    mak "But a more interesting phenomenon is when every single journey through REM sleep yields the same exact dream."
    mak "It turns something so obviously fake into something that feels just as real as waking up and starting your morning routine."
    mak "For me, that routine is brewing a pot of coffee, taking a shower, straightening out my uniform, and then texting my mother to say good morning."
    mak "But lately, that routine has started to become weighed down by the excruciatingly dark undertones of myself and a blanket of stars not at all dissimilar from what we saw on the beach last night."
    s "Well, yes. The night sky is dark by nature. I wouldn’t exactly say that’s a dark undertone, though."
    mak "By itself, no. But when you start having the same dream over and over and over again, you start having time to analyze different aspects of it."
    mak "The dream is not just of the sky itself but of me as I swim through it."
    mak "The only issue is, you can’t swim through the sky. And so logic dictates that I would have to be falling."
    s "Or flying, since it’s a dream and logic doesn’t influence dreams."
    mak "To say it doesn’t influence them is a bit of a reach, don’t you think?"
    mak "Pretty much everything we see is tied to logic in one way or another. Things very rarely happen without reason."
    mak "And so, as someone who spends far too much time bathing in this aspect of human thought, it’s easy for me to understand what’s happening in those dreams of mine."
    s "Which is?"

    scene makotocomeshome6
    with dissolve

    mak "I’m jumping, idiot."
    mak "I’m having recurring dreams about jumping off of something, somewhere. "
    mak "And I believe that the reason for this is that there has been something dark growing inside of me for a very long time."
    mak "My own shadow, I suppose."
    mak "Just mine compels me to think about things like jumping out of a moving car on the highway or taking a few extra painkillers just to see what would happen."
    s "That...definitely sounds a little worse than what my apparent shadow makes me do."
    mak "Worse, sure. But I’m stronger than you and would never let something like that overtake me the same way you let {i}yours{/i} overtake {i}you{/i}."
    mak "No matter how many times I have that dream, I’ll never try to reenact it."
    mak "I’m smart. I have a bright future ahead of me. I have a wonderful best friend. And I like to think I’m at least decently attractive."
    s "You’re very attractive, Makoto."

    scene makotocomeshome7
    with dissolve

    if bonus == True:
        mak "You’re only saying that because it’s directly linked to the possibility of us having more sex in the future."
    else:
        mak "You’re only saying that because you want another ice pop."

    s "Well, yeah. But also because it’s true."
    s "But why spend time thinking about all of those things when, comparatively, your situation isn’t all that bad?"

    scene makotocomeshome8
    with dissolve

    mak "I’ve explained something like that to you in the past, haven’t I?"
    mak "What was my reasoning back then?"
    s "I think it was something like “That's just the way it is.”"
    mak "Then that’s my reasoning this time, too."
    mak "Not everyone has complete control over their emotions the way you do, Sensei."
    mak "There are some people out there who would laugh in the face of all that I go through if it happened to them."
    mak "But the amount of effort I put into hiding that part of me really only makes me more tired at the end of the day."
    mak "Mix that with an onslaught of dreams that feel more like memories of horrible things and you have one unhappy Makoto."
    mak "And, it might not always work, but the best medicine for an unhappy Makoto is someone who can constantly remind her that her troubles are nothing but troubles."
    mak "And most troubles go away with time."
    mak "Dreams, too."

    scene makotocomeshome9
    with dissolve

    mak "I don’t want to die, Sensei."
    mak "And it’s not that I don’t want to die. I don’t want to think about dying. And, at this point, it’s become almost an inevitability."
    mak "I’ll never give into something just because of an inevitability, though. So I guess that's one area where I could be considered an idiot."
    mak "But the fact that part of me is there at all is just..."
    s "Scary."
    mak "Not even that."
    mak "It’s just...exhausting."
    mak "I’m so tired."
    s "Well then wake up, loser."

    scene makotocomeshome10
    with dissolve

    mak "Oh, would you look at that. I’m perfectly fine, now."
    mak "Thank you so much for listening to me, Sensei."
    s "Any time, Makoto."
    s "You know that a big part of why I say things like this to you is because I think you can handle it, right?"
    mak "Obviously, but even I have limits."
    mak "And so I figured coming out and trying to properly explain more about the things I’m feeling to you would help."
    mak "The issue with that is that even though I can try to explain those things, I feel like I can’t even come close to properly doing them justice."
    mak "All of those dreams and all of those things that I see, even though I {i}know{/i} they’re dreams, still feel like more."

    scene makotocomeshome11
    with dissolve

    mak "I know I’ve already compared them to memories, but...even that word doesn’t really apply."
    mak "But I’m sure that this combined with everything else I’ve forced onto you over the last 24 hours doesn’t exactly allude to my expected stability, does it?"
    s "Oh, I’ve already given up on expecting stability from you."

    scene makotocomeshome12
    with dissolve

    mak "Is that an insult?"
    s "More of an evaluation."
    s "You have depression, right?"
    mak "Probably. Over 10%% of all people are expected to have some sort of mental disorder. It would make sense if that was the reason behind all of this."
    s "That number definitely seems higher than 10%% based on all of the people I find myself associating with on a daily basis."

    scene makotocomeshome13
    with dissolve

    mak "We really don’t have the most...stable class, do we?"
    s "Not even close."
    s "But what I’m saying is that you don’t really need to worry about how you look to me or anyone else."
    s "Like, if you ever want to show up to[school] some time and skip out on doing my work for me, just tell me."
    mak "And if I ask to just...{i}always{/i} skip out on your work?"
    s "Well that would just be irresponsible if you want me to keep teaching."
    mak "Right...that would be completely irresponsible of {i}me...{/i}"
    s "There you go. Now you’re starting to get it."
    mak "What I’m confused about, though, is that if you don’t expect stability from me...what do you expect?"
    mak "Because all this time I’ve been citing myself as the cool, calm, collected one."
    s "I expect literally nothing from you."
    mak "Well that's just plain rude."

    if bonus == True:
        s "You’re a fucking [teenager], Makoto. Stop being an adult and just chill for once."

    s "Do you want to sit behind my desk from now on? Will that make you feel better?"

    scene makotocomeshome14
    with dissolve

    mak "Can I?!"
    s "..."
    s "Does that...really make you that excited?"
    mak "Forgive the pun but, depressingly so!"

    scene makotocomeshome15
    with dissolve

    mak "And...since we’re already on the topic of things that would make me feel better..."
    mak "Could I ask you to...maybe be a little more honest with me from now on?"
    s "Honest about what, exactly?"
    mak "Honest about the things that I already know you’re doing but you’ve yet to come out and admit to."

    if bonus == True:
        s "Oh...{i}those{/i} things."
        mak "Sensei...I don’t need to know {i}who{/i} else you have a more...{i}adult{/i} relationship with, but I’d at least gain some solace in knowing that you trust me enough to not blurt it out to anyone else."
        s "And here I was thinking I was doing you a service by {i}not{/i} telling you things I expect will upset you."
        mak "I never promised to not get upset. I just said that it would provide some solace."
        mak "And wallowing in sadness is exponentially easier than wallowing in uncertainty."
        s "Uncertainty? But I thought you “already knew?”"
    else:
        s "..."
        mak "..."
        s "..."
        mak "..."
        s "Okay, fine. {i}I{/i} am the one who has been hiding the various soups."
        mak "Why would you do this?"
        s "I just had so many of them. It got out of control."

    scene makotocomeshome16
    with dissolve

    mak "Nothing is truly certain unless you see it with your own eyes or hear it with your own ears."

    if bonus == False:
        s "Does soup make a sound?"

    mak "And even then, there’s the possibility of what you see or hear being an object of delusion."
    mak "So nothing is ever certain as a whole."
    mak "But there are some things that are a lot easier to accept once they’re out in the open."
    mak "So...I won’t say something like “I’ll be happy with just knowing” because that would make me a liar."
    mak "But I’d probably be able to fall asleep a little better."
    mak "And that would be a...good start."
    s "..."
    mak "..."

    if bonus == True:
        "Oh, fuck it."
        "Makoto’s been racking up losses left and right. "
        "It won’t kill me to hand her a single victory when I can’t imagine she’d be one to let anyone know about it."
        "After all, who would she even tell?"

        s "Your...suspicions are correct."
        s "There are others."
    else:
        s "I already told you I did it. What else you do want to know?"

    scene makotocomeshome17
    with dissolve

    mak "Can I...ask you how many or would that be pushing it?"
    s "That would be pushing it."
    s "Accept your victory and move on with whatever solace that was able to provide."
    mak "It feels out of place to say it in this context...but thank you."
    mak "Thank you for trusting me and thank you for not viewing me as a wicked witch."
    mak "And again, thank you for not [molesting] me in the middle of the night."
    mak "I realize that was probably the hardest for you out of all of those things."
    s "Is there any chance for a...second reward?"
    mak "..."
    s "..."
    mak "Right now? Seriously?"

    if bonus == True:
        mak "No. Get out of here, you pervert."
        s "But...this is my house."
        mak "Fine. {i}I’ll{/i} get out, then."
    else:
        s "Ice pop! Ice pop! Ice pop!"
        mak "...Fine."

    scene black
    with dissolve2

    if bonus == True:
        s "Wait. I was only kidding. You don’t have to-"
        mak "I do. I skipped my entire morning ritual anyway, so I have to catch up on all of that."
        mak "I’m really happy we got to spend so much time together this weekend, though."
        mak "Because even if...I know there are other girls now-"
        mak "At least there weren’t for one night."

        play sound "dooropen.mp3"

        "..."
        "Except there were."

    $ renpy.end_replay()
    $ makoto_love += 5
    $ makotowinterbeach4 = True
    $ makotobeachticket = False
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label makotonew1:
    scene makotopool1
    with dissolve
    play music "10c.mp3"

    "Another day of school comes to an end and, like always (Or at least a fair portion of the time), I’m headed to my office to provide counseling to whoever happens to be in need today."

    mak "Oh, good. You’re still here."

    "Or not."

    scene makotopool2
    with dissolve

    mak "I need your help with something."
    s "Sorry, do I know you? "

    scene makotopool3
    with dissolve

    mak "Please don’t pretend you don’t know me just because I am actually asking for your help for once."
    s "Are you a new student here? If you’re looking for the staff room-"
    mak "It’s me. Makoto."
    s "No, Makoto wears glasses."

    scene makotopool4
    with dissolve

    mak "You see me without glasses all the time! "
    s "I have never seen you before in my life."

    scene makotopool5
    with dissolve

    mak "Fine. I guess I’ll just have to be the only one wearing a swimsuit after all."
    s "..."
    mak "..."
    s "Let me start by apologizing for not recognizing you."

    scene makotopool6
    with dissolve

    mak "That’s what I thought..."
    s "So, what’s this involving swimsuits? Are you joining the swim club or something?"

    scene makotopool7
    with dissolve

    mak "Oh, please. I’m busy enough with student council. There’s no way I’d have time for another club on top of that."
    mak "It’s just our class’s turn to clean the pool and, without your help, I’ll be doing it all on my own. Which I guess would be fine if not for the fact that I have work tonight."
    s "Remind me- where is it you work again?"

    scene makotopool8
    with dissolve

    mak "Oh, you know. The same place you nearly assaulted me the other night. Does that ring a bell?"
    s "..."
    mak "..."
    s "Makoto-"

    scene makotopool9
    with dissolve

    mak "I’m kidding."
    mak "I’ve chalked it up to just one big misunderstanding and don’t hold it against you for getting sucked up into a moment I never should have enabled in the first place."
    mak "{i}But...{/i}"
    s "I don’t like that “but.”"
    mak "{i}But{/i}, I still think it would be best if you would help me out with this tiny little chore. You know, since I’m so forgiving and kind and whatnot."
    s "You know that all you had to say was the swimsuit thing, right? I’ve already made up my mind and am ready to go whenever. "
    s "I obviously don’t have anything to wear, though, so you’ll have to do all of the cleaning yourself."

    scene makotopool10
    with dissolve

    mak "Oh, please. You really think I wouldn’t be prepared for something like this? I have a spare swimsuit for you in the left drawer of the desk in your office."
    s "Please don’t smuggle swimwear into my desk, Makoto. That’s not what I need an assistant for."
    mak "It clearly is since you’ll be putting it on immediately and meeting me near the pool."
    s "I don’t even know where the pool is. I’ve never been there before."
    mak "Well, I suggest you figure it out if you actually do want to see me in my swimsuit..."

    scene makotopool11
    with dissolve

    mak "Which...I guess is an actual thing I’ve said to my teacher now."
    s "Well, say no more. I’m on my way. But if this is just one big ploy to get me into a speedo, I’m going to have to give you detention."
    mak "I’m Makoto Miyamura. I’m immune to detention."

    scene black
    with dissolve

    s "We’ll see about that..."

    "Makoto and I part ways as I pick up where I left off before she showed up and continue heading to my office."
    "Unfortunately for whoever is facing emotional turmoil today, I won’t have any time for counseling."
    "Instead, I am going to have to pretend to clean a pool so as to not disappoint my very-easily-disappointed class representative."
    "All I can really say at this point (Apart from how little I want to actually expend energy after class) is that..."
    "Well, I hope her swimsuit is worth it."
    "........."
    "......"
    "..."

    scene makotopool12
    with dissolve2

    "It is."

    mak "I see you were able to locate the pool after all. Congratulations, Sensei. There’s a brush and a bucket behind you. "
    mak "The pool itself is cleaned by professionals, so we just need to take care of the perimeter."
    s "Can I have permission to say something mildly creepy right now?"

    scene makotopool13
    with dissolve

    mak "You’re actually asking for permission? That’s odd."
    mak "I suppose I can humor you by allowing you to say whatever sort of perverted thing you are about to say to me. So please, go ahead before I change my mind."
    s "Sure."
    s "Makoto, you are ridiculously hot and I wish you would wear that swimsuit literally everywhere."
    s "It’s hard to tell with your uniform on, but your body is essentially flawless and you are making it very hard for me to not achieve an erection right now."
    mak "Are you done?"
    s "I think so."

    scene makotopool14
    with dissolve

    mak "Good. That actually could have been a lot worse and I’m very proud of you for being able to mostly contain yourself."
    mak "Though, I do wish you’d remember that I’m a bit of a protege to you and that you are putting our relationship in grave danger every time you stare at me like that."
    s "Stop being so attractive and I’ll stop staring. It’s that easy."
    mak "Bucket. Now."

    scene black
    with dissolve

    s "You’re really bossy today, Makoto. I don’t like it."
    mak "The further out of line you get, the harder I have to push you back in. We’re already way behind schedule."

    "I do as Makoto says and retrieve a bucket of soap she must have pre-positioned near the entryway as well as a brush to just...hold and pretend I’m actually using."
    "Of course I’m not going to actually {i}clean,{/i} but as long as I can make her believe I am, I’m sure everything will work out okay."
    "........."
    "......"
    "..."

    scene makotopool15
    with dissolve

    s "Okay. Break time."
    mak "It’s been thirty seconds. "
    s "That’s it? I feel like we’ve been doing this for hours."
    mak "Your brush hasn’t even touched the tiles yet."
    s "Why were you assigned to do this on your own in the first place? There are nine other girls in the class. Couldn’t one of them have helped you instead of me?"
    mak "I wasn’t assigned to do this on my own. Yumi and Chika were supposed to help."
    s "Ah. Well, I guess there was never any chance for Yumi to actually contribute to something like this...but I’m surprised Chika didn’t show."
    mak "It very likely just slipped her mind. I’m sure she would have come if I reminded her. "
    s "Why didn’t you?"

    scene makotopool16
    with dissolve

    mak "Let’s just say I’m not the only person with prior obligations after school. "
    mak "Chika’s living situation doesn’t allow for a lot of extra time after school, so...consider this as me simply being a good samaritan."

    if chikadorm15 == True:
        s "I didn’t realize you were also aware of Chika’s {i}situation.{/i}"

        scene makotopool17
        with dissolve

        mak "Ahh. I take it you know as well, then. Why am I not surprised?"
        mak "Chika hasn’t directly told me what her situation is, but it’s pretty easy to figure out if you pay any amount of attention to her."
        mak "Always rushing home after school...being held back a whole year...forging signatures on permission slips..."
        mak "Anyone actually looking for an answer could easily find one. I just happened to be one of the few to look."
        s "..."

    else:
        s "What’s wrong with her living situation?"

        scene makotopool17
        with dissolve

        mak "Why don’t you try and find out yourself? She seems to like this new version of you. I doubt she’d be opposed to opening up once you get to know her a little more."
        mak "I’m simply doing my part as the class representative and making everyone’s lives a little bit easier whenever I can."
        s "..."

    scene makotopool16
    with dissolve

    mak "Any reason for the sudden bout of silence, Sensei? And don’t pretend to be too focused on work when I know you haven’t even started yet."
    s "You’re a really good person, Makoto."

    scene makotopool18
    with dissolve

    mak "Huh?..."
    s "It’s easy to do good things for someone when you’re getting something in return. But it takes a special kind of person to do those things for nothing."
    s "You’re not over here trying to leverage Chika’s position against her...and you haven’t even brought up disciplining Yumi for bailing on responsibilities you had to take on yourself."
    s "Not to mention all of the stuff you do for me..."
    s "You’re just a genuinely good person."
    mak "..."
    s "..."
    s "Any reason for the sudden bout of silence, Makoto? And don’t pretend to be too focused on work when you haven’t scrubbed in almost ten seconds now."

    scene makotopool19
    with dissolve

    mak "Sorry. That just took me by surprise..."
    mak "It’s been a while since you’ve genuinely complimented me like that and...I think...my heart might have skipped a beat or two."
    s "Well, don’t let it skip too many more because I don’t have a license and can’t drive you to the hospital."

    scene makotopool20
    with dissolve

    mak "It just...feels really good to be recognized. "
    mak "Sometimes, it feels like no one really notices me or...even thinks of how things would be {i}without{/i} me."
    mak "To a lot of the girls in our class, I’m just some roadblock between them and an exciting high school life."
    mak "And I’m sure that, in many ways, that’s completely  true. "
    mak "I know I can be a little anal when it comes to rules and regulations and stuff..."
    mak "But all I really want is to make sure everything plays out smoothly...To make sure no one gets held back by their circumstances or themselves."
    mak "And if that means shouldering a burden or two, that’s fine. I’m perfectly capable of handling small problems like that."
    s "Just don’t take on too many of them if at all possible. "
    s "That sort of thing can be dangerous."

    scene makotopool21
    with dissolve

    mak "Thanks, Sensei. "
    mak "That advice would have really resonated with me if you hadn’t been staring at my ass this entire time."

    scene makotopool22
    with fade

    s "..."
    mak "..."
    s "I have no idea what you’re talking about."

    scene makotopool23
    with dissolve

    mak "You should really be more careful, you know. The pool might be in its own building, but we’re still technically on school grounds."
    mak "Someone could show up any minute now."
    s "Good. That means they can clean instead of me."

    scene makotopool24
    with dissolve

    mak "Forgive me if this question is on the tasteless side, but since when are you even this...attracted to me?"
    mak "In the beginning of the year, it seemed like you barely even acknowledged I was a girl."
    mak "Now, it feels like I can’t do {i}anything{/i} without having to dodge your gaze like it’s a car in a game of Frogger."
    s "It might be safe to just assume it’s because I now directly associate you with pornography."

    scene makotopool25
    with dissolve

    mak "No, I..."
    mak "I think I started noticing this before you ever even found out where I work."
    mak "It was like you just...woke up one day and you were suddenly interested in me as more than just an understudy."
    s "Well..."
    s "Maybe I was?"

    "That {i}is{/i} what happened, isn’t it?"
    "I have no idea what sort of person the previous iteration of me was, but if he wasn’t attracted to Makoto...was he even really a person at all?"

    scene makotopool26
    with dissolve

    mak "Well...as long as you can promise me you’re not just toying with my heart or something...I think I can be happy."
    mak "If I found out that this was all just...some sort of game you were playing or...some sort of horrible joke..."
    mak "That..."
    mak "That would really hurt..."
    s "Why would I joke about something like this?"

    scene makotopool27
    with dissolve

    mak "Because you’re an adult..."
    mak "And behind all the sense and sagacity, I’m still just a vulnerable teenage girl."
    mak "I obviously look up to you...I...{i}admire{/i} you..."
    mak "I guess what I’m trying to get at is..."
    mak "It would be extremely easy for you to hurt me if you wanted to."
    mak "And I can’t figure out if you want to or not."
    s "I don’t {i}want{/i} to hurt you, Makoto. "
    s "I just can’t imagine a future where it doesn’t happen."

    scene makotopool28
    with dissolve

    mak "But...what does that mean? I don’t understand."
    s "It means that this isn’t a joke and that I’m not just messing around with your vulnerable, teenage heart."
    s "And that’s exactly what makes everything so much worse."
    mak "That alone isn’t {i}worse,{/i} Sensei. If you’re really not treating this as a game, I’m a lot more inclined to..."
    mak "To..."
    s "..."
    mak "..."
    s "To what, Makoto?"

    scene makotopool29
    with dissolve

    mak "..."
    s "..."
    s "Makoto-"
    mak "Uhh...uh-oh. I appear to have lost my balance."
    s" Makoto, come-"

    scene black
    with dissolve
    play sound "splash.mp3"

    mak "Oh no. Losing my balance has resulted in me falling into the pool."
    s "If you think I’m going to clean the rest of this myself, you- wait. What are you doing?"
    mak "Oh no. I am now losing control over my hands. What is happening to me?"
    s "Makoto, let go of my ankle."
    mak "I wish I could, Sensei. But I’m afraid it is too late."
    s "Don’t even think about-"

    play sound "splash.mp3"

    "Makoto tugs on my leg and sends me falling into the pool right on top of her. "
    "We remain underwater for several seconds, attempting to pull apart before returning to the surface."

    scene makotopool30
    with dissolve2

    "Our attempt at pulling apart doesn’t work as well as it could have."

    mak "..."
    s "..."
    mak "..."
    s "..."
    mak "Something..."
    mak "Something is poking me..."
    s "..."
    mak "..."
    mak "Is that-"
    s "Yup."
    mak "I see."
    s "..."
    mak "..."
    mak "I think..."
    mak "I think we should have a talk soon..."
    s "I don’t really like talks."
    mak "I don’t think I do either, but..."
    mak "I..."

    scene makotopool31
    with dissolve

    mak "I think you might like this one..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ makotonew1 = True
    $ makoto_love += 1
    stop music fadeout 10.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label makotonew2:
    scene makotohandy1
    with dissolve2
    play music "citylife.mp3"

    "So-"
    "You might be wondering why I’m creepily standing in the entryway of the porn shop despite them very obviously appearing to be closed."
    "The answer, however, is not very simple."
    "You see, the porn shop is {i}not{/i} supposed to be closed right now. In fact, I’m probably here a little earlier than normal."
    "{i}But-{/i}"
    "There {i}was{/i} a sign on the door saying the place was shut down for the night."
    "Which, by the looks of it, I obviously ignored. But I am not the only one at fault here since normally, when you close a store, you lock the door."
    "What if I was a shoplifter or burglar or something like that?"
    "Who would be responsible if I stole every single sex toy this place has to offer, leaving both men and women alike to pleasure themselves the old fashioned way?"
    "Basically, both parties here are in the wrong. And even if my side of the argument would get kicked out of court sooner than the other in the unlikely event of charges being pressed..."
    "I can not simply walk away from what could very well be an exciting new experience."
    "And based on the dim purple light and softcore porn music leaking out of what I now know as the secret sex room, it appears that one of these new experiences is welcoming me with open arms."
    "The only question now is whether it’s Makoto in there or her mysterious, surprisingly elusive mother."
    "If it {i}is{/i} her mother and I enter the room, things can go one of two ways."
    "Either she freaks out and calls the cops. Or she {i}is{/i} a freak and the two of us proceed to have sex."
    "And based on what I’ve heard from Makoto thus far, either of those two things seems plausible."
    "If it is {i}Makoto{/i} watching porn in there, though..."
    "Well, I’ll very likely be yelled at. But at least she won’t get the authorities involved."
    "All things considered, I have about a 67%% chance of success- and that is good enough for me to push my luck a little further."
    "After all, I already made my way into a store I knew I shouldn’t be making my way into..."
    "But until something horrible happens and I actually have some sort of consequences to face, I’m going to keep following my heart."
    "And this time, my heart is leading me into a room where I’ve already tried pushing my luck once."
    "The first push is always the hardest, though. "
    "I’m sure that the next one won’t require nearly as much effort."

    scene black
    with dissolve2

    "Slowly, so as to not alert whoever is inside of my presence, I make my way across the room and toward the light."
    "The soft, unmistakable hum of a sex toy blends in with the sound of the video being watched in a way that makes it hard to discern whether or not it’s a part of the film."
    "The air near the room is several degrees hotter and scented with some sort of fragrance I can’t put my finger on, but is likely a combination of various cheap candles and lotions."
    "The door, while cracked open, is not ajar enough to see through."
    "So, I push that the same way I am pushing my luck-"
    "And take another step toward a 67%% chance of success."
    "........."
    "......"
    "..."

    scene makotohandy2
    with dissolve2

    "Jackpot."

    mak "Hah......mnh~"
    mak "Ahh......{i}ahh...{/i}mngh~"

    "I have now confirmed two things."
    "One: the sound of the vibrator I heard was very much not a part of the film."
    "Two: I am going to be yelled at very shortly."
    "Oh, and you may as well tack on a third thing of: if this is the last time anyone ever sees me, I did not die without first experiencing true happiness."
    "The only question now is how long I want to watch for and when I want to let her know I’m here- which I’m obviously going to do on the off chance she’s too horny right now to deny a good opportunity."
    "Makoto said she wanted to talk, didn’t she?"
    "What if that talk is the result of her rethinking the sexual dynamic between us- budding like the flower that is her developing body?"

    s "..."

    "Though, I guess there’s a chance that it’s the exact opposite."
    "And that stolen glances of a bitch in heat are all I’ll ever have."

    scene makotohandy3
    with dissolve

    mak "Hah...hah.......hah..."

    scene makotohandy4
    with fade

    mak "Mnf...mm...mm~"
    s "..."
    mak "Ngh.......mnnnh~"
    s "..."
    mak "Hah...{i}hah...{/i}ahhh!"
    s "Hey, Makoto. Glad to see business is going well."
    mak "..."
    s "..."
    mak "..."
    s "..."

    scene makotohandy5
    with dissolve2

    mak "S..."
    mak "Sensei?..."
    s "You left the door unlocked. And I didn’t want to just go home empty handed, so...surprise."
    mak "{size=-15}........out{/size}"
    s "You’re going to have to speak up. Your dildo is a little too loud for me to hear you over."
    mak "{size=-15}Get......out......{/size}"
    s "Again, not sure-"

    scene makotohandy6
    with hpunch

    mak "I SAID GET OUT!"

    "Makoto, without thinking, mistakes her vibrator for a hand grenade and whips it at me, nearly breaking one of my hands in the process."

    scene makotohandy7
    with dissolve

    "Instead, it crashes into the wall behind me and winds up ricocheting into my shoe."
    "I go to pick it up and-"

    mak "Don’t you dare touch that! And what the fuck do you think you’re doing in here?! This is trespassing, you know! I put a sign on the door and everything!"
    s "Did you really close down your family’s shop for the whole night just so you could masturbate in the back room?"

    scene makotohandy8
    with dissolve

    mak "It...It wasn’t going to be for the full night! Just until I was done!"
    s "Seems like a lot of unnecessary effort for a problem that could have been remedied by an “out to lunch” sign instead. "
    mak "Oh, please. As if a sign like that would have deterred you. Making the entire store look actually {i}closed{/i} wasn’t even enough to deter you. "
    s "What can I say? I am a man who does not back down."
    mak "Please be a better man in literally every respect. "
    mak "Go...help yourself to anything you want in the store and {i}I{/i} will pay for it. I can’t have you seeing me like this. Not while the...sting of the last time we were in here is still fresh in mind."
    s "Oh, right. Didn’t you want to talk about that?"

    scene makotohandy9
    with dissolve

    mak "Not without my fucking pants on! And why did you have to pick {i}today{/i} of all days to show up like an hour ahead of time?!"
    s "I didn’t realize there was a specific time you preferred me showing up."
    mak "Well, why do you think I’m in here in the first place?!"
    s "Because being surrounded by dicks all night thrusts you into a perpetual state of arousal that can only be remedied by intermittent orgasms?"
    mak "Don’t use “dicks” and “thrusts” in the same sentence while I am already experiencing Hell firsthand!"
    mak "I am in here because I {i}knew{/i} you would be coming and I didn’t want to wind up in the same predicament as last time!"
    s "So...let me get this straight-"
    s "You closed down the entire store because you knew that I’d do something to turn you on...and you were attempting to hold yourself over by masturbating beforehand?"
    mak "Well, it sounds fucking perverted when you say it like that!"
    s "Well...it kind of {i}is.{/i}"
    mak "It is not! This sort of thing is a lot more common than you think!"
    s "Masturbation? I agree. It’s a completely natural thing to do to yourself and I’m glad you’re such a healthy young woman."

    scene makotohandy10
    with dissolve

    mak "Can you please leave now? Being caught with my pants down is already embarrassing enough."
    s "They’re not just down. They’re halfway across the room along with your-"
    s "Wait, isn’t that the one I made you put in your mouth?"

    scene makotohandy8
    with dissolve

    mak "Did you expect me to just put it back in the box?! That would be disgusting!"
    s "Makoto."
    mak "What?!"
    s "Let’s talk."
    mak "I-"

    scene makotohandy11
    with dissolve

    mak "I don’t want to."
    s "And why is that?"
    mak "..."
    s "..."
    s "If you’re going to start ignoring me, I’m just going to come even closer. Is that what you want?"

    scene makotohandy12
    with dissolve

    mak "..."
    s "..."

    scene makotohandy13
    with fade

    s "Fine. Have it your way."
    mak "Why do you want to talk {i}now?{/i} Why can’t we have a civilized, formal discussion about this over dinner or something like that?"
    s "You want to go out to dinner? Fine. Put your pants on. We’ll go right now."
    mak "..."
    s "..."

    scene makotohandy14
    with dissolve

    mak "Can I maybe...you know...finish up in here first?"
    s "Wow. You’ve really got it bad, don’t you?"

    scene makotohandy15
    with dissolve

    mak "Why is this happening to me? I’m usually so good at denying things and...sticking to the straight and narrow..."
    mak "Then all of a sudden, you start associating me with sex and now it’s like I can’t go a single day without fighting off the desire to go to town on myself whenever everyone stops looking."
    s "I believe what is happening to you is called “hormones,” Makoto."

    scene makotohandy16
    with dissolve

    mak "I know what fucking hormones are! This runs deeper than that alone! "
    s "Then just give in already. "
    s "If things are getting to the point where you have to masturbate before even seeing me when I would be {i}more than willing{/i} to assist you in that endeavor, why put yourself though Hell?"

    scene makotohandy17
    with dissolve

    mak "Because I need you for something else..."
    s "And what’s that?"
    mak "That’s..."
    mak "That’s too embarrassing to say out loud. "
    s "Well, I can’t do anything about that then."
    s "But what I {i}can{/i} do, is reiterate the fact that I am not just messing around with you and that whatever we decide to do is just as much your decision as it is mine."
    s "I don’t know if your “talk” requires a little more detail than that, but that’s where I stand- firmly on the side where the two of us can mess around without having to put our jobs at risk."
    mak "You..."
    mak "You do realize that {i}any{/i} sexual relationship you have with me would be putting your job in {i}extreme{/i} risk, right?"
    s "Not if no one finds out."

    scene makotohandy18
    with dissolve

    "Makoto falls silent as her mind figures out how to navigate between immense arousal and an uncertain future."
    "I’m sure it’s difficult for someone like her to deviate from a path she’s chosen but, especially when the only alternative is headed straight for a cliff-"
    "But sometimes, we do things we don’t understand. Or things that we know are horrible ideas."
    "I guess what I mean is-"
    "Sometimes we have to fall."
    "But there’s something beautiful about falling together."

    mak "..."
    s "..."
    mak "My mom would kill me if she ever found out."
    s "Your mom sells porn for a living."
    mak "But I’m still her only child...And you’re significantly closer to her age than you are to mine."
    s "Good point. I guess I’ll just go have sex with her instead then."

    scene makotohandy19
    with dissolve

    mak "Very funny."
    s "So, is there anything else you’d like to say before I let you get back to masturbating?"

    scene makotohandy20
    with dissolve

    mak "You’re...actually going to leave?"
    s "Oh, I never said that. "
    mak "But-"
    s "I kind of want to stick around and watch. I feel a little bad for interrupting you when you were probably getting really close to cumming."

    scene makotohandy21
    with dissolve

    mak "After all that...you just want to watch? I could have sworn you were in the process of talking me into having sex with you."
    s "Is that a thing you’d do right now?"
    mak "Well, I..."
    mak "If it’s with you...I..."
    mak "I might..."
    s "And is that what you actually want? Or is that just desperately horny Makoto talking out of her ass so she can get back to feeling good?"
    mak "Honestly, at this point, I have no idea. I’m just tired of sitting here half naked while you look down on me and need {i}something{/i} to happen right now or I am going to die of embarrassment."
    s "I’ll go get your present off the floor."
    mak "That’s fine, but...umm..."
    mak "Can you at least...rinse it off first?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene makotohandy22
    with dissolve2

    "Through the art of expert conversational skills and maybe a tinge of manipulation, I manage to convince my classroom assistant to start playing with herself again."
    "She timidly switches on the vibrator and looks up at me with an expression displaying both fear and arousal before closing her eyes and succumbing to the desire to press on."
    "I wrap my arm around her as the toy comes into contact with her slit, but leave all of the actual {i}sexual{/i} touching up to her."
    "If I’m not the one doing anything, I’m not the one making any mistakes."
    "I’m just here for the show or, as I mentioned earlier- a brand new experience."
    "This obviously will not be the last step for Makoto and me. I’m sure we’ll find ourselves in here time and time again."
    "But I will revel in the splendor that is experiencing her first time opening up to a man."
    "And I will watch intently as her thighs shake in time with the pulsating vibrations of a thick, rubber cock."

    mak "Ah......ahh......hah..."
    s "Does that feel good, Makoto?"

    scene makotohandy23
    with dissolve

    mak "Hah......mnf......really good...Sensei..."
    mak "Are you sure it’s...fine to see me like this?..."
    s "You should know better than anyone that I’ve wanted to see you like this for a while."
    mak "And...hah...it won’t...change our...relationship at all?..."
    s "Of course it will. But not in a bad way."
    s "You can just rely on me for something else now as well."

    scene makotohandy22
    with dissolve

    mak "Mnh...mmm...the...list of things I can rely on you for has...been shrinking lately anyway..."
    mak "This is...probably the first new thing in...months..."
    s "The first of many new opportunities, you mean. This is just the beginning."

    scene makotohandy24
    with dissolve

    mak "I guess...it is...huh?..."
    mak "We can’t really...turn back anymore...can we?..."
    mak "I bet we’ll be doing...all sorts of...inappropriate things together...from now on..."
    mak "You can...touch me, you know?..."
    mak "I won’t say no like I...did last time..."
    s "Yeah, you seem a bit less {i}guarded{/i} this time around."

    scene makotohandy25
    with dissolve

    mak "Hah...hah...well...I’ve had more time to...think about it..."
    mak "And...I guess you were just...good at reassuring me...that this is...really okay..."

    scene makotohandy26
    with dissolve

    mak "Also...seeing you without a shirt on the other day {i}really{/i} messed me up..."
    mak "I’ve always been attracted to you...but that was like...{i}wow.{/i}"
    s "Was it? Because you seemed pretty unfazed after all of my swimsuit comments."
    mak "I guess I’m just a really good actor. But...if you want the truth, Sensei..."

    scene makotohandy27
    with dissolve

    mak "I was fucking {i}dripping...{/i}"
    mak "In fact, if I hadn't {i}fallen{/i} into the pool, you might have even noticed some of it running down my legs."
    mak "You know how much self control it took to not wrap my fingers around your cock when I felt it poking me? {i}A lot.{/i}"
    s "..."
    mak "What? What’s wrong?"
    s "Nothing. You just got...really, really into this extremely fast."
    mak "Well, it’s your fault, isn’t it?"
    mak "You’re the one who made me like this."
    mak "You’ll have to excuse me for...hah...actually being able to speak my mind when I’m wet..."

    scene makotohandy28
    with dissolve

    mak "Ahh! Ahhh...fuck...that...feels so good..."
    mak "Hold me closer...Sensei...closer..."

    "Well, then."
    "I guess...this is what Makoto is like when she’s turned on?"
    "I’m okay with this."

    scene makotohandy29
    with dissolve

    mak "Hah...hah...Sensei...take it out for me..."
    mak "It’s...no fair if...I’m the only one...who gets to feel like this..."
    s "Are you sure you don’t want to do the honors yourself? I can only imagine how long you must have-"

    play sound "zipper.mp3"
    scene makotohandy30
    with dissolve

    s "Oh. Okay. "
    mak "Wow...no wonder you called the...one in that video...average..."
    mak "I had no idea you were hiding something so amazing, Sensei..."
    mak "And it’s already so hard..."
    s "Well, in your words, {i}you’re the one who made me like this...{/i}"

    scene makotohandy31
    with dissolve

    mak "I guess that makes it my job to take care of it then, doesn’t it?"
    mak "You can leave it to me, Sensei. It might be our first time doing something like this, but I know enough about you to realize what you must like."

    "Makoto delicately tugs on my cock, angling it toward her so she’s able to move up and down a little easier."
    "She locks eyes with me but doesn’t seem to mind where I look as my gaze bounces back and forth between her and her slit."
    "As if attempting to match the motions of her hand, each time she grazes the tip, she pressed the head of her vibrator against her pussy, making it {i}look{/i} like she’s going to push it in but never actually doing so."
    "Her palm is hot and, after a few minutes of this and several trips to the top, winds up being coated in a thin layer of precum that she appears to be intentionally lubricating it with."
    "She may seem mostly innocent on the outside, but it’s clear just how much her sexual skills, as unpolished as they are, have been shaped by years worth of pornography."

    scene makotohandy32
    with dissolve

    mak "Hah...hah...you like that...Sensei?..."
    mak "Are you happy that...you finally got what you wanted?...Am I...living up to your expectations?..."
    s "You’re definitely...surpassing them I think."

    scene makotohandy33
    with dissolve

    mak "Is that so?..."
    mak "But all I’ve done is jerk you off..."
    mak "Are you sure you don’t want me to go a little further?..."
    mak "Like maybe...you could fuck my mouth?..."
    mak "Or maybe even..."
    mak "You could fuck {i}me?{/i}"
    s "That’s-"

    scene makotohandy34
    with dissolve

    mak "Hah...ngah...would it...even fit inside?..."
    mak "It’s so big...and I can’t even fit the tip of...this thing inside me yet..."

    "I look down again to find Makoto lightly prodding at her entrance with the head of the vibrator and know almost instantaneously that I won’t be able to take much more of this."

    scene makotohandy35
    with dissolve

    mak "Fuck it...I say we do it~"
    s "Yeah, I don’t...know if that’s the best idea right now."
    mak "Why not? Are you about to cum?"
    s "I’m sure you’ll find out momentarily..."
    mak "I told you I knew you well enough to realize what you’re like. {i}I{/i} haven’t even finished yet and I got a head start."
    mak "I guess you did interrupt me, though. But to think that I’d {i}still{/i} win after that..."
    s "Sorry to interrupt you, Makoto, but your {i}victory{/i} is only seconds away at this point."

    scene makotohandy36
    with dissolve

    mak "I suppose it would be best if I paid close attention, then. For {i}science,{/i} of course."

    "Makoto quickens her pace but doesn’t tighten her grip, jerking me off in one fluid, consistent motion until the pressure becomes too much to bear."

    mak "Cum for me, Sensei..."
    mak "Show me just how long you’ve been holding this back for...."

    with sexfade
    with sexfade
    scene makotohandy37
    with cumflash
    with hpunch

    mak "Ahh~"

    scene makotohandy38
    with dissolve

    "I erupt all over both myself and Makoto and she continues jerking me off throughout the duration of the orgasm."
    "She doesn’t say anything apart from a scattered gasp or breath for the next minute or so, electing to simply just...watch me instead."
    "But seeing as it is extremely awkward to just sit there with semen dripping down your shirt and your partner’s chest, I decide to speak up before this becomes a habit for the two of us."

    s "Alright, I’m going to need you to let go now. "
    mak "Do I have to? I was hoping to bask for a little while longer in one of the very few opportunities I’ll have in life to hold some sort of power over you."
    s "That {i}power{/i} is currently dripping down your chest and you still haven’t even finished yourself off yet."
    mak "Oh, right. I guess I haven’t."
    mak "I got so caught up in my first sexual escapade that I wound up focusing too much on you instead."
    s "..."
    mak "..."
    s "Am I supposed to apologize for that or something?"
    mak "Of course not. All {i}you{/i} need to do is go find something to clean ourselves off with while I pick up right where I left off before you showed up and ruined our relationship."
    s "You’re still saying things like that even after we’ve already taken the first step?"
    mak "I’ll likely change my tone post-orgasm. We’ll see."

    scene black
    with dissolve2

    "I get off the couch and search for a towel or a box of tissues or...anything to wipe a flood of potential children off of ourselves with."
    "In the midst of my search, I hear Makoto close her mouth with her hand, stifling the noise of an aggressive, overdue climax before once again dropping the vibrator on the floor and collapsing onto the couch."
    "I attempt to snap her out of her state of toy-induced ecstasy after I locate a mysterious but clean rag, however, I’m unable to discern anything she says from that point on."
    "It was something about happiness, I think."
    "Or how, in the unrelenting fervor of her mind post-orgasm, she is glad that we’ve become closer to one whole rather than two halves."
    "None of it makes sense to me, so it does not stick."
    "But what {i}does{/i} is the idea that I now have someone else’s livelihood in the palm of my hands."
    "I have no foul intentions. I plan to carry it as far as it will go."
    "But, when threatened, I may drop it."
    "The results of that remain to be seen."

    $ renpy.end_replay()
    $ makoto_love += 1
    $ makotonew2 = True
    stop music fadeout 10.0

    "{i}Congratulations on sowing the first seeds of corruption in the mind of a promising young girl!{/i}"
    "{i}Surely, nothing but good will come of this!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotonew3:
    scene makotonewthree1
    stop music

    "go to porn shop"

    menu:
        "continue event":
            play sound "static.mp3"
            scene makotonewthree2
            with flash
            stop sound

    "you do a bad thing sensei"

    play sound "static.mp3"
    scene makotonewthree3
    with flash
    stop sound

    "SOMETHING IS SPROUTING"

    play sound "static.mp3"
    scene makotonewthree4
    with flash
    stop sound

    "The grains of dirt underneath your fingernails now swim in the safety of your intestines because no amount of nights or days can calm you more than hardened keratin deposits and ironless blood."

    play sound "static.mp3"
    scene makotonewthree5
    with flash
    stop sound

    "The inside of your heart is full of shit and {b}so is the world around you.{/b}"
    "I SPEAK TO YOU AND ONLY YOU"
    "Open your mouth."
    "FUCKING OPEN your FUCKING MOUTH you FUCKING worm."
    "Bite down."
    "It will lessen the pain of what it means to be a MAN."
    "BITE FUCKING DOWN."
    "The taste of tiny bits of your tongue will remind you of when she used to gnaw at yours."

    scene black

    "REMEMBER IT"
    "YOU FUCKING WORM"

    play sound "static.mp3"
    scene makotonewthree5 with flash
    scene makotonewthree4 with flash
    scene makotonewthree3 with flash
    scene makotonewthree2 with flash
    scene makotonewthree1 with flash
    scene makotonewthree6 with flash
    stop sound
    $ renpy.pause(4, hard=True)

    mak "Sensei?..."

    play music "darkbedroomwaltz.mp3"
    scene makotonewthree7

    "I am where I am supposed to be- the outskirts of my throne of flesh and closer to a hole that I can sleep inside of."
    "A figure stands before me in pixelated glory, illuminated by the faint pink light of a SEX BUILDING."
    "Or at least what I think is a SEX BUILDING."
    "I have a history of mistaking all buildings for sex buildings and then proceeding to do bad things inside of them."

    play sound "static.mp3"
    scene makotonewthree6 with flash
    stop sound

    "And then proceeding to do entirely consensual, not at all manipulative things inside of them."
    "There are no blurred lines here- just ones that have been hastily drawn in the sand with a shard of glass pulled from the wreckage of a shattered windshield."
    "I kept one in a box somewhere."
    "The box is gone now."
    "I wonder where it went."

    mak "Sensei? Why are you just staring at me like that?"
    mak "{b}DON’T YOU WANNA FUUUUUUUUCK?{/b}"

    play sound "static.mp3"
    scene makotonewthree7
    with flash
    stop sound

    "I try to speak to Makoto but she is so much smarter than me so she doesn’t understand anything."
    "Then, like a snake, I poke and prod at a prison with my egg tooth."

    scene makotonewthree8
    play music "justlights.mp3"

    "And everything turns out okay."

    mak "..."
    s "..."
    s "Sorry, did you say something?"
    mak "I asked why you’ve just been standing there staring at me ever since you got here."
    mak "And...come to think of it, why are you here this late in the first place? I just closed the store."
    s "You closed the store and {i}didn’t{/i} immediately proceed to play with yourself? I am shocked."

    scene makotonewthree9
    with dissolve

    mak "That happened one time!"
    s "{i}That I know of.{/i}"
    mak "Yes, that {i}you know of.{/i} And I probably don’t have to remind you of this, but that worked out very well for {i}both{/i} of us."
    s "Exactly. Which is why I’m surprised you’re not repeating the process again tonight."

    scene makotonewthree10
    with dissolve

    mak "Well, I...may have been open to more...{i}experimentation{/i} if you showed up at a reasonable time..."
    mak "But it’s past midnight now and I have to be getting back to the dorm before Miku thinks I was..."
    mak "Well, before Miku thinks something bad happened to me."

    "Past midnight? How did that happen?"

    s "Don’t worry Makoto. You’re in good hands now that I’m here."

    scene makotonewthree11
    with dissolve

    mak "I am in {i}worse{/i} hands now that you’re here."
    s "Yeah, that’s fair."
    s "I’m not going to let you just walk back to the dorm on your own at this hour, though. I’ll come with you."
    mak "..."
    s "Makoto?"
    s "I’m trying to be nice and-"

    scene makotonewthree12
    with dissolve

    mak "Actually, how about we go somewhere {i}else{/i} instead?"
    s "Somewhere else? You literally just said you needed to be getting back home."
    mak "I did. But then I remembered the wonderful invention that is my cell phone and that my safety is all but a simple text message away."
    s "That doesn’t change the fact that it’s past midnight. I can’t imagine there’s anything open around here."
    mak "Around {i}here,{/i} no. But who says we have to stay here?"
    s "Is this the real Makoto Miyamura suggesting that we sneak around to different parts of town after midnight?"
    s "What, you jerk off your teacher {i}one{/i} time and you think you’re some sort of badass now?"

    scene makotonewthree13
    with dissolve

    mak "I never claimed to be a “badass.” In fact, I quite like staying out this late. Miku is the one who can’t stay awake past 11:00 PM."
    s "Strange. I didn’t really take you for a night owl."

    scene makotonewthree14
    with dissolve

    mak "Yes, well...I think there’s something rather peaceful about the night."
    mak "But I guess this is a weird time to say that as I’m about to suggest something that is the exact {i}opposite{/i} of peaceful."
    s "Loud, aggressive sex in a love hotel? Count me in."

    scene makotonewthree15
    with dissolve

    mak "More like a scenic walk through the urban district. The lights are beautiful this time of night."
    mak "Besides, I already gave you a chance to have sex with me and you said no."
    s "Honestly, I’d probably say no tonight as well. I was just being facetious."

    scene makotonewthree16
    with dissolve

    mak "What do you mean you’d say no? You were the one who essentially coerced me into a sexual relationship, weren’t you?"
    s "I didn’t do anything that you didn’t already want me to do."
    mak "But...if I wanted you to have sex with me-"
    s "I wouldn’t."
    mak "..."
    s "..."

    scene makotonewthree15
    with dissolve

    mak "Yeah, I don’t understand that at all and I think you’re lying."
    s "When have I ever lied to you before?"
    mak "Probably tonight, but I try to turn my brain off after work so I’m not going to bother deducing which statements were true and which ones were false."
    mak "{i}Instead,{/i} I am going to begin walking to the urban district. If only there was an adult to accompany me and make sure I don’t end up passed out in an alley somewhere along the way."
    s "I guess all I can do is just...be that adult then, huh?"
    mak "That’s right. All you can do is just be that adult."

    scene makotonewthree17
    with dissolve

    mak "I hope you don’t mind pulling an all-nighter, though, Sensei. I hear it gets harder the older you get."
    s "Wait, we’re going to be out all night?"
    mak "Is that a problem? We don’t have school tomorrow, so there’s nothing you need to worry about being late for."
    s "Nothing except sleeping, you mean. I can’t remember the last time I stayed out for the entire night."
    mak "Well, make sure you remember this time. It would hurt my feelings if you were to ever forget it."
    s "If I can stay awake through the whole thing, I promise to do just that."
    mak "And if you can’t?"
    s "Then..."
    s "I guess {i}I’ll{/i} be the one passed out in an alley somewhere."

    scene black
    with dissolve2

    "I follow Makoto as she sets off down a street and at least {i}appears{/i} to know where she’s going."
    "I don’t really have any reason to be skeptical since, despite the differences in our age, she surely knows much more about the surrounding areas than I do..."
    "But I guess I’m a little skeptical nonetheless."
    "Not because I don’t trust her, but because I think that, somewhere in the back of my mind, I {i}want{/i} her to be wrong."
    "I just..."
    "Probably couldn’t tell you why if you wanted me to."
    "........."
    "......"
    "..."

    scene makotonewthree18
    with dissolve2

    "My ingrained desire for Makoto to be wrong about something, as unsurprising as it is, does not come to fruition."
    "We make it to the urban district in what seems like no time at all and spend a good half an hour or so wandering through the glow of neon and passing under billboards reminding us to smile."
    "I’d spit in their faces if I were fifty feet tall but, unfortunately, I’m stuck here on the ground as a slightly-above-average sized male."
    "Thankfully, being next to Makoto makes me feel much larger."
    "To be frank, being next to {i}most{/i} girls makes me feel much larger."
    "I’m just significantly more aware of that fact when I’m alone with them in the dark."

    mak "So, is there anywhere you’d like to go, Sensei? Dinner, perhaps?"
    s "Sure. Having a first date at 2:00 AM in an unfamiliar part of town will make a great story for the grandkids we’ll never have."
    mak "Okay, so {i}no{/i} dinner. I’m afraid I don’t have many more suggestions, though, if you’re not in the mood to eat."
    s "Just walking is fine. We don’t really need to do anything."
    mak "Are you saying you’re happy as long as you’re with me?"
    s "Do you actually think that’s something I would say?"
    mak "No, but that doesn’t mean I wouldn’t like to hear it."

    scene makotonewthree19
    with dissolve

    mak "Since we don’t have any plans, how about we go somewhere with a better vantage point?"
    mak "Coming here may have killed any chance we have for the quiet of the night to make its beauty apparent, but that doesn’t mean the sights need to die as well."
    mak "We can simply enjoy ourselves somewhere slightly closer to the sky."
    s "Sure. Wherever you want to go is fine."
    s "I’m getting tired of these billboards anyway."

    scene makotonewthree20
    with dissolve

    mak "What’s wrong? Not a fan of pop music?"
    s "..."
    s "I guess not."

    scene black
    with dissolve2

    "We find our way to a staircase I can’t even see the top of."
    "And while some people might be consumed by curiosity at the sight of something like this, I just feel even more exhausted."
    "I’m tired."
    "I guess getting older really {i}does{/i} make staying awake throughout the night harder."
    "We begin to ascend and each and every step feels like walking on glass."
    "But somehow, Makoto manages to maintain a smile as her feet are cut open."
    "It’s admirable."
    "Not how she can be happy at a time like this-"
    "But how she can be so good at pretending nothing is wrong when everything is."

    scene makotonewthree21
    with dissolve2

    mak "Do you like heights, Sensei?"
    s "They...exist. I don’t really care one way or the other."
    mak "Well, {i}I{/i} love them."
    mak "I have since I was little."
    mak "I rode on my dad’s shoulders a lot when I was a baby, so I’ve got tons of memories of just...looking down on everything. Feeling like I’m flying."
    mak "Of course, I’m not a baby anymore and sitting on someone’s shoulders would barely constitute a “height” at all-"
    mak "But I guess that makes me appreciate places like this even more."
    mak "Or...any place where I can take in a lot at once."
    mak "The world is so big...and you and I are so small."
    s "And...you {i}like{/i} that? How insignificant we are in the grand scheme of things?"
    mak "Not really."
    mak "I just like the lights."
    s "I see..."

    "The night has reached a point where even here, in what I assume is the busiest place in all of Kumon-mi, has fallen silent apart from the distant music and scattered car alarms."
    "A gust of wind joins the fray every now and then- but even those are fleeting. The same way the occasional moments where Makoto’s eyes meet mine are."
    "We look away each time despite there not being a reason to."
    "I wouldn’t be surprised if there was still some evidence of my semen on her that persisted through a bath or shower or whatever method she uses to get herself clean."
    "But even with that in mind, we still look away."
    "I can’t tell if I like that or not."

    mak "Can I...ask a question that may or may not ruin the mood?"
    s "The only mood I have right now is “tired,” so you can go ahead and ask whatever you want."
    mak "Then..."
    mak "What are we?"
    s "What do you mean?"
    mak "I mean that up until recently, I always looked at us as mentor and apprentice. Or teacher and student. A whole bunch of things like that."
    mak "But it’s harder for me to view us as two separate entities now that we’re closer to becoming one."
    mak "So I just wanted to hear your thoughts on the matter."
    s "You’re you and I’m me. That’s all it is and that’s all it needs to be."
    mak "I figured you’d say something like that."
    s "Well, I’m sorry for being predictable."
    mak "You don’t have to apologize, Sensei. I wouldn’t have it any other way."
    mak "It’s not as if I imagined you’d come out and say we’re dating when, as nice as that sounds, it would be near-impossible to execute correctly."
    mak "Not to mention how many rules it would be breaking."
    mak "But..."
    mak "Maybe one day."
    s "I-"
    mak "Don’t talk. I don’t want you to ruin the life I’m imagining right now."
    s "..."
    mak "..."

    scene clearnightsky
    with dissolve2

    mak "Can I ask you one more thing, Sensei?"
    s "Oh, am I allowed to talk again?"
    mak "Just for this next question. After that, you can go back to being silent."
    s "Then ask away, I guess."
    mak "Sensei..."
    mak "Were you really serious when you said you wouldn’t have sex with me earlier?"
    s "..."
    mak "..."
    mak "Sensei?"

    scene makotonewthree22
    with dissolve2

    mak "..."
    s "..."
    mak "Are you kidding me right now?"
    mak "I know you’re not asleep."
    s "Can’t hear you. Sleeping."
    mak "It was a serious question, you know. Because I still don’t understand why you wouldn’t-"
    s "Can’t hear you. Sleeping."
    mak "..."
    s "..."

    scene makotonewthree23
    with dissolve

    mak "I’ve made a horrible mistake, haven’t I?..."

    scene black
    with dissolve2

    "We don’t last the rest of the night."
    "In fact, we don’t even last another hour."
    "Not wanting to walk all the way back, Makoto uses an app on her phone to call us a ride."
    "The car shows up within minutes and we wind up in our beds before the sun even starts to rise."
    "Makoto goes to sleep thinking about me."
    "Then I go to sleep thinking about someone else."

    $ renpy.end_replay()
    $ makoto_love += 1
    $ makotonew3 = True
    stop music fadeout 7.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    if day == 5:
        $ totaldays += 1
        $ day += 1
        if day == 6:
            hide friday onlayer date
            show saturday onlayer date
            jump saturdaymorning
        else:
            "ERROR ADVANCING TO SATURDAY"
    if day == 6:
        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date
            jump saturdaymorning
        else:
            "ERROR ADVANCING TO SUNDAY"

label sadgirls1:
    scene black
    with dissolve2

    "Yasu sets her sights on someone who, up to this point, has managed to stay relatively uninvolved with the chaotic happenings of the morning and urgently makes her way over to her."
    "Caught up in the clamor, the rest of the girls do not see it."
    "But it is the {i}only{/i} thing I see."
    "I don’t know if the whispers of the world find their way into {i}my{/i} ears as well or if I have just placed a large stake of momentary faith in Yasu-"
    "But I keep my eyes and ears focused."
    "For the chances of what happens next being positive in nature seem impossible."
    "And the idea of great misfortune befalling someone who already washes down each meal with it seems too sad to be true."

    scene fatesealedinradiowaves1
    with dissolve2

    mak "..."
    ya "..."
    mak "Um..."
    mak "Can I...help you, Yasu?"
    ya "I’m sorry."
    mak "Sorry for what, exactly?"
    mak "You don’t think this was your fault, do you?"
    mak "Fights are an inevitable aspect of high school life and it’s surprising we’ve managed to make it this far without having experienced one yet."
    mak "I wouldn’t worry too much about it. It’s-"
    ya "I’m sorry for what comes next."
    mak "For what...comes next?"

    scene fatesealedinradiowaves2
    with dissolve

    "Yasu returns to her seat, leaving Makoto mildly perplexed, but mostly unfazed."
    "That’s just the way people hear Yasu’s words now. "
    "She’s spent too long allowing innate fanaticism to dribble out of her mouth that we’ve already deemed it pointless to lend her our handkerchiefs."
    "Which is why what happens next still comes as a surprise to Makoto."

    play sound "pabell.mp3"
    scene fatesealedinradiowaves3
    with dissolve
    $ renpy.pause(4, hard=True)

    vpa "Makoto Miyamura, please come to the front office immediately."
    vpa "I repeat: Makoto Miyamura, please come to the front office immediately."
    mak "The front office? Me? Why?"
    a "I knew it! You’ve been cheating on all of our exams the whole time, haven’t you?! There’s no way one person can be that smart!"
    mi "Wait a sec, there ain’t a second Makoto Miyamura in our school, is there? Cause I know {i}my{/i} Makoto wouldn’t ever get called to the office. "
    ki "Maybe Makoto’s just a rebel and none of us knew about it? "
    n "Or maybe she’s got a secret part time job that the school found out about? I remember seeing something in the handbook about how that's not allowed."
    ki "Did you seriously read the fucking handbook? Who are you?"
    mi "Uhhh...nope! She ain’t got anything like that! Definitely a good girl who focuses on her studies and doesn’t have any sorta job at all! Hahahah!"

    scene black
    with dissolve2

    "Makoto stares up at the speaker in the corner of the classroom, hoping for some added explanation or clarification as to why she’s suddenly being forced out of her comfort zone."
    "When she realizes no such thing is coming, she hesitantly slides her chair out from beneath her desk and slowly walks to the front of the room. "
    "But she stops in front of me, as if I can provide some sort of guidance when we’re all caught in the same storm and can’t even figure out which way is north."
    "I wish I could tell her where to go."
    "I just have no idea what it is she has to avoid just yet."

    scene fatesealedinradiowaves4
    with dissolve

    mak "I take it you haven’t heard anything about this, have you?"
    s "Me? No clue. My plan for today was to just hide in my office. And seeing as {i}you’re{/i} the one who delivers the vast majority of my news to me, the chances of me knowing anything are pretty slim."

    scene fatesealedinradiowaves5
    with dissolve

    mi "You don’t think it could be your family’s store, do you? Noriko was just sayin’ that her last school-"
    mak "I suppose it {i}could{/i} be. But I don’t understand why the PA would need to be used when standard protocol is to have the student’s homeroom teacher inform them of a mandatory meeting."
    mi "Yeah, but...I don’t think anybody else’s job has ever involved this many wieners."
    mak "That is...a fair point. There are certainly an excess of those at the shop."

    scene fatesealedinradiowaves6
    with dissolve

    mak "Regardless, I suppose I should get a move on. If I actually {i}am{/i} in trouble, it wouldn’t be right to keep the office waiting."
    mak "I’m sure it's just some sort of mix-up."

    scene fatesealedinradiowaves7
    with dissolve

    mak "Either that or I’m finally being rewarded for my continued efforts and announcing as much over the intercom would have painted a target on my back."
    mi "Uhh...Makoto? Mind watchin' yourself a little? You’re elbowin’ where my boob's supposed to be."
    s "I guess...let me know if you wind up needing anything. "
    s "Or if this involves me in any sort of way."

    scene fatesealedinradiowaves8
    with dissolve

    mak "Whatever it is, leave it to me."
    mak "There’s no problem Makoto Miyamura can’t handle."
    s "There are plenty of problems Makoto Miyamura can’t handle. I know this because I am one of them."
    mak "Then...correction. There are no {i}school{/i} related problems that Makoto Miyamura can’t handle. So I suggest you let me deal with this on my own."
    mak "The morning’s proven to be exhausting enough already and I know you were looking to avoid confrontation today."
    s "Fair enough. Good luck, I guess. I’ll just have Miku help me clean up any blood that Nodoka may have left behind."
    mi "I, uhh..."
    mi "I ain’t...really a fan of that idea, Sensei..."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "Makoto leaves the room, but instead of grabbing a mop and a bottle of bleach, Miku quickly retreats to my side and grabs hold of my sleeve."
    "She’s the second girl to do that today."

    scene fatesealedinradiowaves9
    with dissolve2

    mi "Sensei..."
    mi "I can’t really describe it, but it feels kinda like my stomach is doin’ flips. This sorta thing ain’t ever happened to Makoto before."
    mi "What if it’s somethin’ really bad? Like...worse than the whole family business thing."
    s "Is there something you had in mind?"
    mi "The only thing I can think of involves you too. And I can’t imagine they woulda let ya come to class like normal if that was the case."
    mi "Ya think maybe we should tail her? Just waitin’ around to-"

    play sound "slidedoor.mp3"
    scene fatesealedinradiowaves10
    with dissolve

    "The door swings open and Miku reflexively latches onto the skin of my arm rather than just my sleeve."
    "I understand why when I see who is in front of it."

    play sound "static.mp3"
    scene fatesealedinradiowaves11
    with flash
    stop sound

    maki "{b}WHERE IS MAKOTO?!?!?!{/b}"
    mi "Sensei..."
    mi "What's Maki doing here?..."
    mi "What’s going on?..."
    maki "{b}WHERE IS SHE?!?!?{/b}"
    s "She just got called down to the office a minute-"

    scene fatesealedinradiowaves12
    with dissolve

    maki "{b}STAY HERE! DON’T FOLLOW ME!{/b}"

    play sound "static.mp3"
    scene fatesealedinradiowaves13
    with flash
    stop sound

    mi "..."
    s "..."

    "Maki slams the door on her way out, putting an abrupt end to the residual fight gossip and replacing it with a brand new flavor of misery."
    "Miku’s grip grows stronger. I can feel the blood vessels beneath my skin rupturing as I attempt to uncover a means of calming her down."
    "Desperate, I look to Yasu of all people, hoping that there’s some new sort of premonition that will tell me when this will end."
    "But she sits unmoving, staring out of the window, and listening to the whispers of the world as it sings the most unpleasant melody it can think of."

    mi "I ain’t ever heard her yell before..."
    s "..."
    mi "I don’t like this, Sensei...I don’t like this at all..."
    mi "You’ve gotta go after ‘em...Waitin’ here ain’t gonna do anything..."
    mi "If Makoto’s in trouble...she needs you to be there for her..."
    s "..."
    mi "She needs your help..."

    "But what help would {i}I{/i} be? Especially after Maki directly told me to not get involved in this."
    "Why doesn’t {i}Miku{/i} help? "
    "Because she’s scared?"
    "What if I’m scared too?"
    "I’m not saying I am, but what if I was?"
    "Why should {i}I{/i} be the one who’s forced to cast that aside?"
    "Is it because I’ve been on this earth longer? Because even that is untrue at this point."
    "Is it because she looks up to me? Because she doesn’t. Not the way she used to. "
    "She knows now just what kind of person I am. Which is why she’s forced to walk alone."
    "Is it because I’m a stand-in for the person she wants to see the most?"
    "Because that-"

    s "..."

    "That one makes sense."
    "And I guess it’s that sort of idea, the idea that someone {i}needs{/i} me, that makes me separate my skin from Miku and carry my ruptured blood vessels out into the hall."

    play sound "static.mp3"
    scene hall_day with flash
    stop sound

    mi "Tell her that...whatever happened, her best friend’s here for her! "
    mi "And that even if she did do somethin’ bad, I’ll always be on her side!"
    mi "Tell her that, Sensei! Tell her that when ya see her!"

    scene black
    with dissolve2

    "I find a happy medium in an ocean of overwhelming sadness and settle on a state of motion somewhere between walking and running."
    "And while swim speeds would make more sense given the analogy, it’s hard to call what I’m doing “swimming” in any sense of the word."
    "Not when every step makes it feel as if the water in my lungs is rising. "
    "Not when every room I peer into in hopes of finding her increases the pressure building up inside of my chest."
    "Not after how every lap I make around the school reinforces the idea that maybe she’s already left."
    "That maybe I was too late."
    "And that I should have just stayed in the classroom like I was told- because at least there are people I can comfort {i}there{/i}."
    "I give up on the idea of being a hero as I have never believed in them in the first place."
    "But in the gap between the first and third floor, there is a space where the water doesn’t rise. "
    "And in this dry spot, my feet revel in the sensation of the scraping of sand- regardless of the shards of seashells finding solace in the safety of my soles."
    "With each step, I connect with the sea in a way I have seldom done before."
    "And if I listen closely, I can hear the ocean pouring out from underneath a bathroom door."
    "........."
    "......"
    "..."

    scene fatesealedinradiowaves14
    with dissolve2

    mak "{b}NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{/b}"
    mak "IT’S NOT TRUE!!! "
    mak "I DON’T BELIEVE IT!!!"
    mak "HE WOULDN’T!!!"
    mak "HE CAN’T!!!"
    mak "NOT WITHOUT SAYING GOODBYE!!!"
    maki "Makoto..."
    mak "DADDY!!!"
    mak "DADDY ISN’T GONE!!! "
    mak "THEY’RE WRONG!!!"
    mak "HE’S ON HIS WAY HOME! HE’S ON HIS WAY-"

    scene fatesealedinradiowaves15
    with dissolve

    maki "Makoto, stop it! Yelling won’t bring him back!"
    mak "But he’s...he’s not gone! He’s not!"
    maki "Makoto!"
    mak "He hasn’t seen my new uniform yet! "
    mak "He hasn’t read my report card!"
    mak "I need him to be proud of me! I need him to be proud!"
    mak "Daddy!"
    mak "Daddy isn’t dead!"

    "A tidal wave crashes into me and forces me back."
    "But as I turn around to watch it disappear along with the rest of the ocean, I’m reminded that this is all just a metaphor I’ve been using to make myself feel better."
    "And that the harsh reality is that I’ve just walked into a private conversation in which the lives of two people who mean something to me are violently dismantled."
    "But when I make an effort to leave, my shoes scuff the floor. "
    "And the abruptness of the sound makes it difficult for me to find another metaphor to cling to."

    play sound "static.mp3"
    scene fatesealedinradiowaves16
    with flash
    stop sound

    maki "I told you not to follow me!"
    s "I didn’t mean to-"
    maki "Leave! Get out!"
    s "I’m sorry. I didn’t know-"
    maki "I said get out! "
    maki "You have nothing to do with this!"

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    "She’s right."
    "I have nothing to do with this."
    "Which is why I don’t have a problem with just walking away."
    "Which is why I don’t spend the next five minutes standing outside of a bathroom door in a hall I seldom visit."
    "Which is why I hear none of what comes next."
    "I’m already somewhere else."

    play sound "static.mp3"
    scene fatesealedinradiowaves17
    with flash
    stop sound

    maki "Hey! Hey! Listen to me!"
    maki "We’re going to get through this! Together! You and me!"
    maki "I know it’s not what you want, but I’m right here! Okay?! I’m right here and I’m not going anywhere!"
    maki "Mommy’s got you!"
    maki "I’ll read your report cards. I won’t really know what they mean, but I’ll read them! Okay?"
    maki "And...I’ll learn to sew! Or something! In case you ever rip your uniform! "
    maki "I’ll do whatever you need! And that includes being proud of you! Because it might not seem like it sometimes, but I am! I am so...{i}so{/i} proud of you."
    mak "I want my dad! "
    mak "I want my daddy!"

    scene fatesealedinradiowaves18
    with dissolve

    maki "I know, baby. I know you do. I want him too. But it’s just us now...and that’s okay!"
    maki "That’s okay because it’s been {i}just us{/i} for a few years anyway, and we’ve been doing great!"
    maki "I’m not saying things will be easy. This is going to be the hardest thing you’ll ever have to go through. But don’t think for a second that you’re alone."
    maki "We’re in this together. We can cry {i}together.{/i} "
    maki "We can miss him {i}together.{/i}"
    mak "It’s too soon! I wasn’t ready!"
    mak "I never got to say goodbye! I never got to say goodbye!"
    maki "We can still talk to him! And wherever he is, he’ll hear us! But for now, just..."
    maki "Just rely on me, baby. Cry as much as you want and I’ll be right here to hold you tight."
    mak "Mom! Tell me it’s not real! Tell me this is all just a nightmare! And that when I wake up, Daddy will be home and we’ll all go on a big trip together!"
    maki "We can still go on a trip! You and me! Mother and daughter! To anywhere you want! Anywhere at all!"
    mak "I want to see my dad!"

    play sound "dooropen.mp3"
    scene fatesealedinradiowaves19
    with dissolve

    maki "Didn’t I tell you stay out of-"

    scene fatesealedinradiowaves20
    with dissolve

    maki "Miku..."
    mi "Maki...Sensei told me where you were but..."
    mi "He wouldn’t tell me what happened..."
    maki "It’s..."
    maki "We can talk later, sweetheart. Makoto needs to-"
    mak "Daddy’s gone! "

    scene fatesealedinradiowaves21
    with dissolve

    mi "No..."
    mi "Makoto, I..."
    maki "Oh, fuck it. Come join us on the floor. You’re basically my second daughter anyway."
    mi "Okay...but...ummm...I’m probably gonna cry too..."
    maki "I really don’t care. She needs all the love she can get right now and I just..."
    maki "I guess what I have isn’t enough..."

    scene black
    with dissolve2
    stop music fadeout 25.0

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ sadgirls1 = True

    jump sadgirls2

label sadgirls7:
    play sound "static.mp3"
    scene makotoyay1 with flash
    stop sound
    play music "heartbeat.mp3"
    $ renpy.pause(10, hard=True)

    "When I was younger, I watched a woman’s head split open after a collision with the concrete."
    "I was clutching my mother’s hand as if it were a life raft and I was lost in the ocean."
    "She pulled me inside to shield me from learning about death long before I was meant to."
    "In hindsight, I wish she wouldn’t have."

    $ renpy.pause(5, hard=True)
    scene makotoyay2
    with dissolve4

    "It happened outside of the grocery store."
    "We kept on shopping, ignoring the blare of the sirens — so loud that they overtook the music on the store radio and became the soundtrack to our trip for the day."
    "There is one moment I can recall where the sirens perfectly aligned with the tune of a song."
    "Like a parallelogram, they combined and stretched out forever — past the dying woman and deep into the street..."
    "Off into the horizon...leaving a wake of intangible destruction as it went."
    "I followed the lines until their very end, but only in my mind as my hand still rested in that of my mother’s and I wasn’t old enough to wander off on my own yet."
    "I understand why now."
    "For when the lines ended, I was met with nothing more than pitch black."
    "And a single white clock, dissolving into nothingness."

    scene black
    with dissolve2

    "I look down while I’m walking now."
    "Just to make sure no lines cross over me."

    scene makotoyay3
    play music "warblewarblewarble.mp3"

    "I recall another hand, far bigger than that of my mother’s."
    "With a large, clock-colored eraser pressed between its thumb and its forefinger, it reached off into the distance and started rubbing away the remnants of an unreadily dispatched soul."
    "But each line it erased only became longer at the end without attention."
    "And each fleck of rubber that peeled and fell off of the eraser while it attempted to fulfill its only purpose was replaced with a sprouting sunflower."
    "It was in that moment that it dawned on me. "
    "The idea that the most beautiful of things can still grow in the shadows of all that is evil."
    "And it is for that reason that I call myself what I do today."
    "For that hand was yours."
    "And that flower was me."

    stop music
    play sound "static.mp3"
    scene makotosadagain1
    with flash
    stop sound

    maki "Uhh...Makoto?"
    mak "What?"
    maki "There’s someone here to see you."

    play sound "static.mp3"
    scene makotosadagain2
    with flash
    stop sound
    play music "lastdailysong.mp3"

    mak "Sorry, but I’m not accepting any visitors right now. Please ask whoever it is to go away."
    s "Even if it’s me?"
    mak "It doesn’t make a difference who you are. I said I’m not accepting visitors."

    scene makotosadagain3
    with dissolve

    s "Well, I tried."
    maki "Did you really, though?"
    mak "{i}Tried?{/i}"
    mak "Tried what?"
    mak "Did you think bringing him here would cheer me up?"
    mak "Do you think I’m an inconvenience because I’m not handling this as well as you? Is that what’s going on here?"

    scene makotosadagain4
    with dissolve

    maki "What? Of course not. You’re not an inconvenience at all. I just hate seeing you like-"
    mak "Get out."
    maki "Makoto, please. I brought him all this way here to-"
    mak "Not him. You. Leave."

    scene makotosadagain5
    with dissolve

    s "You shouldn’t talk to your mother like that."
    mak "Oh? Are {i}you{/i} my dad now? Hooray. Everything is good again. "
    mak "Let’s all hold hands and forget that the last one is never coming back."
    s "I get that you’re upset. But you need to apologize to-"

    scene makotosadagain6
    with dissolve

    maki "It’s fine, really.  You don’t have to worry about it. "
    maki "I kind of figured something like this was going to happen anyway."

    play sound "static.mp3"
    scene makotosadagain7
    with flash
    stop sound

    mak "{i}Hey, now.{/i} What’s that supposed to mean?"
    mak "Have I become so predictably horrible as a daughter that you just expect me to turn you away now?"
    mak "Or do you think that {i}maybe{/i} I’d just have an easier time grieving without being reminded every thirty seconds that my father is dead?"
    maki "You know that’s not-"
    mak "Why are you still here? I asked you to leave. "
    mak "I’ll humor you and let Sensei try to “snap me out of this.” But if I were in your shoes, I’d probably use that time to prepare myself because, chances are, your daughter’s never coming back either."

    play sound "static.mp3"
    scene makotosadagain8
    with flash
    stop sound

    maki "That’s not true..."
    maki "You’re still you...and all of this is just temporary."
    mak "Oh, give me a fucking break with the cliche consolation lines like “all of this is temporary” and “things will get better.” "
    mak "At least Sensei will be able to come up with more creative ways to remind me of why I shouldn’t be crying during the saddest day of my life. Right, Sensei?"

    scene makotosadagain9
    with dissolve

    maki "Makoto! You’re not the only one who lost someone, you know?! He meant just as much to me as he did to you!"
    mak "Yeah? That’s good to know. It was hard to keep track of {i}who{/i} meant {i}what{/i} to {i}who{/i} with all of those extra people always coming in and out of the house."

    scene makotosadagain10
    with dissolve

    maki "That...didn’t have anything to do with-"
    mak "Yeah, yeah, yeah. Explain it later. I’m done dealing with you for now. Bring on the next contestant. "

    scene makotosadagain11
    with dissolve

    s "Do you intend to shit talk me as well when I’m {i}also{/i} here to help you?"
    mak "You’re here because you were fucking kidnapped, weren’t you? This isn’t something {i}you{/i} would plan."
    mak "You’d tell me to get the fuck over it and learn how to deal with things on my own because that’s what I’m supposed to do! Isn’t it?!"
    s "No. That’s-"

    play sound "static.mp3"
    scene makotosadagain12
    with flash
    stop sound

    mak "Isn’t it?!?!"
    s "...As I was trying to say, no. This is different from all of those other times. Different enough that I’ve had a hard time thinking of anything {i}but{/i} this since I walked into that bathroom."
    mak "Oh, good! If all it took was a fucking {i}death{/i} for you to start worrying about me, perhaps I should have killed someone myself!"
    maki "That’s not what he’s saying, Makoto!"
    mak "Why are you still here?! I told you to leave!"

    scene makotosadagain13
    with dissolve

    s "I’ll take it from here, Maki. I remember the way out, so I can just come meet you in the shop when I’m done."
    maki "Good. She was starting to test my patience anyway."
    mak "Hallelujah! Praise fucking be!"

    scene makotosadagain14
    with dissolve

    maki "I just want you to feel better, Makoto. "
    maki "I’m sorry if I went about it the wrong way."

    play sound "dooropen.mp3"
    scene makotosadagain15
    with dissolve

    "Maki leaves the room, exhibiting a surprising amount of self control by not slamming the door on her way out."
    "I understand that we all have our own ways of processing grief...and I understand even better just how much Makoto cared for her father."
    "But even then, I can’t help but feel like she’s being extremely unfair to a woman who’s been bending over backwards and sidelining her own grief just to deal with {i}this.{/i}"
    "If I were a parent in this scenario, I’d simply let my child rot."
    "So I guess it’s good that I’m not."
    "And that I won’t ever be."
    "Because it wouldn’t be fair to subject someone to that."
    "Now, please excuse me as my hypocrisy reigns supreme once more."

    s "Does being a bitch to your mother like that really make you feel any better?"

    play sound "static.mp3"
    scene makotosadagain16
    with flash
    stop sound

    mak "A little bit, yeah."
    s "Why? You do realize she’s taking this just as badly as you are, right?"
    mak "Dressed like {i}that?{/i} Yeah, I don’t think so. You needn’t look any further than the clothes we’re wearing to tell she doesn’t give a shit."
    mak "Wanna know what I really think, Sensei? "
    mak "{i}I{/i} think she’s dressed like that because she wants somebody to fuck her so hard that she just {i}forgets{/i} my dad."
    s "Seriously?"
    mak "What? It wouldn’t be the first time I’ve heard her getting her brains screwed out by some random guy."
    mak "Want a shot? She’s fresh on the market. And her clothes are already halfway off. Saves you some of the hassle."
    s "Sounds good, actually. I’m sure that hearing me go to town on your mother while you’re stuck inside of your room will do plenty of good for your current state of mind."
    mak "But what about {i}your{/i} state of mind, Sensei? What if you’re not able to get it up for someone who’s already done growing?"
    s "..."

    scene makotosadagain17
    with dissolve

    mak "Oh well. Whatever. Just don’t come crying back to me when her insides are a little too “beat up” for you."
    mak "I can’t speak from experience since you’re the only man who’s ever put his dick in me, but I’m pretty sure she might be a little too stretched out to appeal to your...{i}tastes{/i} by now."
    s "Okay...can I sit? And can we talk about something that doesn’t involve sex? "

    scene makotosadagain18
    with dissolve

    mak "Wow! If I hadn’t already picked out my funeral dress, I might have thought it was my birthday after hearing that."
    mak "Welcome to the party, Sensei. The seat at the head of the table is free now. "
    mak "My legs have grown since my dad last sat in it. So if we’re careful, I might even be able to give you a stealthy footjob while my mom tricks herself into believing we’re a big, happy family again."
    s "Would you rather I just leave?"
    mak "Do you want the honest answer to that? Or do you want to sit down {i}regardless{/i} of what I want because it makes you feel better about yourself?"

    scene black
    with dissolve

    s "I’ll sit. Thanks. "
    mak "Ooooh, look at you. Breezing right past my subtle digs at your character like they don’t actually hurt. Sure wish {i}I{/i} could do that."

    "I take a seat beside Makoto, expecting her to slide away, but she doesn’t move at all."
    "In fact, she grows silent the second I’m closer to her- locking her hostility inside of a box, as temporary as it may be."
    "As I look down at her, I wonder if the disparity in size between us is the primary reason for her newfound silence."
    "I wonder if she feels safer now that there’s someone who could envelop her entire body in a single embrace just one foot away."
    "I wonder if that type of embrace is something she longs for in this moment."
    "Or if it would send her spiraling even further into a pit that she will never return from."

    scene makotosadagain19
    with dissolve2

    s "..."
    mak "..."
    s "Do you want to talk? Or would you rather sit here in silence?"
    mak "I’m not sure. I’m new to this whole “dead dad” thing."
    s "I see that, at the very least, you get your sense of humor from your mother. She said something eerily similar yesterday morning."
    mak "Wow, it’s almost like we’re related or something."
    s "..."
    mak "..."
    s "You don’t actually dislike her, do you? "
    mak "What do {i}you{/i} think about her, Sensei? You know, since you two are such close friends now."
    s "I like her a lot, actually. She reminds me of this one girl that’s been following me around like a puppy since the school year began."
    mak "Ami, because of how annoying she is? Ayane, because it seems as if she’s always in heat?"
    s "I’m talking about you, obviously."
    s "And, for the record, you are also very annoying and have a surprisingly high sex drive."
    mak "Yeah well, when you grow up surrounded by rubber cocks and screams of pleasure, you tend to find yourself getting interested in certain things at a very unhealthy age."
    mak "Apart from that, though, my mother and I are nothing alike. We never have been."
    s "Well...spend a little more time focusing on {i}her{/i} rather than everything else and maybe you’ll change your mind."

    scene makotosadagain20
    with dissolve

    mak "Did she pay you to say that? Is that part of your {i}mission{/i} today?"
    s "If she did pay me to say that, you two would be even more alike. Because I distinctly recall you paying Miku on at least one occasion to...try to get me to fall for you or something."
    mak "A decision that very well paid off in the fact that my hymen is now just as present as my father."
    s "If you really think that had any bearing on my decision to ultimately sleep with you, I think there’s a lot you don’t understand about this relationship."
    mak "Well, it’s not as if you make it easy to understand. "
    mak "But, for the purpose of both humoring you and finding {i}humor{/i} of my own, please tell me exactly {i}what{/i} you think I have in common with my mother."
    mak "Because apart from our apparent shared sex drive and our looks, I struggle finding anything at all."
    s "Well, there’s the dark sense of humor you both use to try and push some of the sadness away..."
    s "There’s the overabundance of love you both have for Miku..."
    s "But more than just those, there’s this...compulsion you both have to never look weak."
    s "Maki doesn’t look as fine as she does because she’s immune to this. She looks that way because she’s focusing everything she has on {i}you{/i} right now."

    scene makotosadagain21
    with dissolve

    s "Weren’t you crying {i}together{/i} when I walked into that bathroom?"
    mak "How should I know? I can’t remember anything about the day I found out. And all I remember from the day after is crying so hard that I threw up."
    s "Well, she was. And before that, she burst into the classroom searching for you with a look I have never seen from her before."
    s "It wasn’t sadness, either. It was urgency. Like the only thing that mattered in that moment was finding you so you wouldn’t have to hear the news from some staff member in an office."
    s "Everything after that has been a marathon of unrestrained compassion for a daughter that she loves who can’t even find it in her to {i}return{/i} that love right now."
    mak "..."
    s "Now, as one more person carrying the impossible, ingrained burden of never showing how I really feel, I obviously get that there’s a good reason for it. Which is why I’m not suggesting that you {i}change{/i} that part of you."
    s "I just think you’re smarter than actually believing your mom is completely unaffected by this."
    mak "Maybe I am."

    scene makotosadagain22
    with dissolve

    s "..."
    mak "Maybe I {i}am{/i} smart enough to understand that..."
    mak "{i}But isn’t everything so much easier when you have someone else to blame?{/i}"

    scene makotosadagain23
    with dissolve

    mak "Isn’t it great knowing that the weight on your shoulders can just be passed on to someone else?! That burdens can become lighter whenever we want them to?!"
    s "It’s not {i}whenever we want.{/i} It’s whenever we can find someone willing to take that weight."
    s "And in your case, you’re just lucky that you have someone who’d sacrifice the last bit of sanity in them so you can be one step closer to smiling."
    mak "Lucky..."
    mak "Me...lucky..."
    mak "Me...the girl who just lost her one and only hero..."
    mak "I’m lucky..."
    mak "I’m so lucky..."
    s "Okay...{i}lucky{/i} definitely wasn’t the best word choice on my part. But I’m sure you understand what I mean, don’t you?"

    scene makotosadagain24
    with dissolve

    mak "Of course I understand, Sensei. "
    mak "I’m {i}smart...{/i}remember?"
    mak "Though, I suppose I’m not the {i}smartest{/i} anymore."
    mak "But I wouldn’t {i}be{/i} that smart if I wasn’t trying to impress someone."
    mak "And before you go drowning yourself in narcissism again, allow me to clarify that I’m not talking about {i}you.{/i}"
    mak "The reason I worked so hard all those years...why I nearly {b}KILLED MYSELF{/b} trying to become the best person I could be..."
    mak "It was all for him."
    mak "It was all to make him proud."

    scene makotosadagain25
    with dissolve

    mak "{i}How am I gonna do that now?{/i}"
    mak "How am I supposed to keep being the best person I can be when the one thing {i}making{/i} me that person isn’t here anymore?"
    mak "I’ve got nothing left. "
    mak "And don’t tell me I have {i}you...{/i}or my {i}mom...{/i}because {i}you{/i} don’t love me...and she didn’t either until she had to."
    mak "My dad is dead. The one thing keeping me going is dead. "
    mak "Shouldn’t I just die too?"
    mak "Maybe then, my mom wouldn’t have to hold in her tears. And you could have Nodoka become your new assistant since she’s already better than me."
    mak "It would all be better without me. The whole fucking world. "
    mak "I’m nothing but a burden to everyone. "
    mak "There’s no one left that I want to live for."
    s "Then why not live for yourself?"

    scene makotosadagain26
    with dissolve

    mak "Because that’s fucking stupid."
    s "How? That’s what I do."
    mak "Yeah? And how’s that working out for you?"

    scene makotosadagain27
    with dissolve

    s "Fine, I guess."
    s "I’ve spent the last couple days slowly losing my grip on reality while worrying about you, but it’s not like I’m waking up every morning thinking about how I want to die."
    s "I’m just...having trouble getting to sleep. Which, all things considered, isn’t really that big of a problem compared to what some of the people I care most about are going through."

    scene makotosadagain28
    with dissolve

    mak "You really worried that much?"
    s "Does that surprise you?"
    mak "..."
    mak "A little."

    scene makotosadagain29
    with dissolve

    s "I guess that’s fair."
    mak "..."
    s "..."

    "I recall an earlier thought — one about my hypocrisy reigning supreme as I leave a girl to rot."
    "And like clockwork, it will reign supreme once more right now."
    "Just this time, it will be in paradoxic contradiction to itself as my hypocrisy is squared until it comes full circle."

    s "Have I ever helped you with {i}anything?{/i}"
    mak "..."
    s "Because all this time, I’ve been telling myself that what I’ve been doing for you was what was best. But I don’t know if I ever actually believed that or if I just...{i}made{/i} myself believe it."
    mak "..."
    s "I guess what I’m asking is...do you need something different from me? Or...{i}want{/i} something different from me?"
    s "Should I be less of an asshole? {i}More{/i} of an asshole?"
    s "I’m just not sure with you."
    s "I think I’m normally pretty good at reading people but, for a while, it’s felt like every time I’ve tried to do that with {i}you,{/i} I’ve come up with nothing."
    s "I’m obviously not...trying to take the place of your father or anything. But I think having one more person on your side is something that could really benefit you right now."
    s "Especially if you’re not going to let your mom be one of those people."
    mak "..."
    s "..."

    scene makotosadagain30
    with dissolve

    mak "Sensei..."
    mak "Have you ever lost someone you loved?"

    play sound "static.mp3"
    scene imissyoumore with flash
    scene makotosadagain30 with flash
    stop sound

    mak "Someone that meant the world to you?"

    play sound "static.mp3"
    scene imissyoumore with flash
    scene anormaldoor with flash
    scene makotosadagain31 with flash
    stop sound

    mak "Does it ever get better?"

    play sound "static.mp3"
    scene imissyoumore with flash
    scene anormaldoor with flash
    scene spiderbug with flash
    scene makotosadagain32 with flash
    stop sound

    mak "What can I do to make this all feel better?!"

    $ renpy.end_replay()
    $ makoto_love += 1
    $ sadgirls7 = True

    if makoto_lust >= 30:
        jump makotolust30
    else:
        jump makotolust30skip

label makotolust30skip:
    stop music
    scene black

    s "Nothing."

    play sound "dooropen.mp3"

    "I exit Makoto’s bedroom and head directly for the stairs."

    play sound "glass.mp3"

    "On the way down, I knock one of the picture frames off of the wall."
    "Curiosity gets the better of me and I stare down at the mess I have made."
    "Beneath the cracked glass is a photo of a little girl in a fisherman’s cap."
    "She rests on the shoulder of a man that is no more."

    play sound "dooropen.mp3"

    maki "Hey! How’d it go? Is everything okay with-"
    s "I knocked one of your pictures off the wall."
    s "It was an accident."
    maki "Huh? Oh. Yeah, that’s fine. I can just get another frame. What I’m more worried about is how Makoto-"
    s "I couldn’t help her."
    s "But she might be a little more open to listening to you now."
    maki "Really? What did you say?"
    s "I can’t remember."
    maki "But-"
    s "Don’t worry about driving me back. "
    s "I suddenly feel like walking."

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}Neither of the girls understand why you left.{/i}"
    "{i}But you do...don’t you?{/i}"

    $ makotolust30skip = True
    $ yumiblock = True
    $ makotoblock = True
    $ mikublock = True
    $ nodokablock = True
    $ makiblock = True

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label makotolust30:
    stop music
    play sound "static.mp3"
    scene imissyoumore with flash
    scene fly with flash
    scene anormaldoor with flash
    scene fly with flash
    scene spiderbug with flash
    scene fly with flash
    scene everythingg with flash
    scene fly with flash
    scene makotosadagain33 with flash
    stop sound

    mak "Oh!"
    mak "I know!"

    play sound "static.mp3"
    scene imissyoumore with flash
    scene rhombus1 with flash
    stop sound
    play music "asobeatsexdark.mp3"

    mak "Hey."
    s "..."
    mak "You’re here to make me feel better, right?"
    s "That’s...why I came. Yeah."
    mak "Good."
    mak "Then fuck me."
    s "..."
    mak "..."
    mak "Are you fucking deaf?"
    s "You...realize your mom could come back at any second, right? And that you're still in mourning?"
    mak "What, are you a fucking pussy now? Take your cock out and replace the pain inside of me with something else. "
    mak "I won’t even make you wear a condom today. Isn’t my dad dying the best thing that’s ever happened to you?"
    s "Makoto-"

    scene rhombus2
    with dissolve

    mak "What’s the fucking problem?! Do you have any idea how many times I’ve made {i}you{/i} cum because it looked like you needed it?! Can you not do that for me right now?!"
    s "That’s not what you {i}need.{/i}"
    mak "What is it with all of you fucking people telling me what I need and how I’m supposed to cope with this?!"
    s "Your mom-"
    mak "She’s so fucking desperate for me to get through this right now that she’d probably {i}let{/i} you fuck me!"
    mak "You wanna go ask? I’ll come with you! Would be nice to get out of my room for once today!"

    scene rhombus3
    with dissolve

    s "I really shouldn’t..."
    s "Not when you’re like this."
    mak "Like what, Sensei?"
    mak "Pathetic?"
    s "..."
    mak "Was I not pathetic back when I was begging you to fuck me in Ayane’s mansion? Because you didn’t have a problem with it then and my vagina has taken a {i}hell{/i} of a beating ever since."
    mak "If anything, I’d say I’m {i}less{/i} pathetic now. So either fuck me or get the hell out because...all of this {i}talking{/i} bullshit? Yeah, not going to work."
    s "I just...need to figure out the right words to say. This isn’t exactly something I planned on doing today, you know."

    play sound "static.mp3"
    scene rhombus4
    with flash
    stop sound

    mak "That’s good! Glad to hear you haven’t progressed to the point where you expect to fuck newly orphaned girls first thing in the morning."
    s "You're not an orphan when you still have a mother who cares about you..."
    mak "You know, you’re really starting to ruin the mood with all of this sentimental shit when this problem could be so easily solved by just raw dogging me until I’m unconscious."
    s "Having sex with you wouldn’t solve anything. It’s one thing to put a bandage on a cut, but when you’ve just had your jugular vein slashed open, a bandage is pointless."
    mak "Thanks for using the jugular vein for your analogy and proving that I am basically already as good as fucking dead. Might as well have some fun on the way out, yeah?"
    s "What do you mean the “way out?”"
    mak "Oh, sorry. Did I say “way out?” What I meant to say is “I’m going to fucking kill myself,” and I’d feel a little bit better about it with a belly full of my teacher’s cum."
    s "Is that...really something you’re thinking about doing?..."
    mak "Golly gee, it is. Except, there’s this one teensy little caveat where every time I fucking {i}try,{/i} it’s like I’ve hallucinated the whole god damn thing."
    s "Makoto-"
    mak "Sensei, I don’t care if I have to fucking rip your pants off myself. You’re going to fuck me."
    s "I just don’t get it. This is one of the only times I’ve ever tried turning sex {i}down{/i} in favor of just...being there for you."

    scene rhombus5
    with dissolve

    mak "If you felt what I felt right now, you’d change your mind."
    mak "If you heard what I heard right now, you’d change your fucking mind."
    mak "It’s like the world itself is speaking to me."
    mak "Do you wanna know what it says, [makotomaster]? "

    if makotomaster.lower() in ["daddy", "dad", "father", "papa"]:
        s "Please don’t call me that right now."
        mak "Oh, grow the fuck up."

    mak "It says everything and nothing all at once."
    mak "And for some reason..."

    scene rhombus6
    with dissolve

    mak "That just gets me {i}really{/i} wet..."
    s "Makoto-"

    play sound "static.mp3"
    scene rhombus7
    with flash
    stop sound

    mak "You know, you say that {i}I{/i} have a lot in common with my mom. But, from my perspective, it seems like you do."
    mak "Not just because you waited until my dad was dead to care about me-"
    mak "But because you never know when to shut the fuck up."
    mak "But that’s okay. I’ll just shut you up myself."
    mak "And if you keep trying to lecture me out of it, I’ll spill the beans to the staff at school that you’re fucking half the class, {i}including{/i} me."
    mak "And what’s even better is I’ll tell them I didn’t want it."
    mak "You still gonna refuse now, [makotomaster]?"
    mak "Or are you going to pump me full of hot cum while my mommy waits downstairs thinking I’m getting {i}counseling?{/i}"
    s "..."
    mak "..."
    mak "That’s what I fucking thought."

    scene rhombus8
    with fade
    play sound "zipper.mp3"

    "My eyes navigate to a white oak door as my fly is pulled down."

    mak "Yeah...keep watch, Sensei. I want you to describe to me in detail what my mother’s face looks like if she does walk in as I’ll be a little...preoccupied."

    "They move from the white oak door to assorted childhood mementos as clumsy hands unbuckle my belt and begin to slide down my pants."

    mak "Heh...you weren’t kidding when you said you didn’t want to do this..."
    mak "You’re not even hard yet."
    mak "But don’t worry...I can fix that for you..."

    scene black
    with dissolve2

    "They move to Makoto next as she exhibits no restraint and stuffs my flaccid dick into her mouth."
    "A free hand latches onto my balls, gently cupping them as she exerts several moans I know to be barely audible despite sounding extremely loud to me."
    "I think to myself that if I can just hold out...if I can just prevent myself from becoming erect during this desperate plea for physical comfort, I can prevent her from doing something I know she’ll regret."

    play sound "static.mp3"
    scene rhombus9 with flash
    stop sound

    "But I am weak."
    "And so my gaze travels to a final destination — no more than five feet away from where I lie right now."
    "It is a single fishing pole."
    "There’s probably a second somewhere else in the house."
    "I imagine both of them will be collecting dust for the foreseeable future."

    mak "Well, that didn’t take very long."
    s "..."
    mak "There’s no need to be ashamed, Sensei. You’re doing this for {i}me,{/i} remember? Quieting the whispers of a thousand screaming clouds that will one day drench me in their hatred."
    mak "Can you hear them too?"
    mak "Or am I truly alone in every possible way?"
    s "..."
    mak "Heheh..."
    mak "Good boy...staying quiet when I told you to..."
    mak "Are you ready for your reward?"

    play sound "static.mp3"
    scene rhombus8 with flash
    stop sound

    "White oak door."

    play sound "static.mp3"
    scene rhombus10 with flash
    stop sound

    "Makoto."

    play sound "static.mp3"
    scene rhombus8 with flash
    stop sound

    "White oak door."

    play sound "static.mp3"
    scene makotocouch10 with flash
    stop sound

    "Makoto."

    play sound "static.mp3"
    scene rhombus8 with flash
    stop sound

    "White oak door."

    play sound "static.mp3"
    scene makotonewthree18 with flash
    stop sound

    "Makoto."

    play sound "static.mp3"
    scene makotounderstars8 with flash
    stop sound

    "Makoto."

    play sound "static.mp3"
    scene bluejay12 with flash
    stop sound

    "Makoto."

    play sound "static.mp3"
    scene rhombus8 with flash
    stop sound

    "White oak door."

    play sound "static.mp3"
    scene rhombus11 with flash
    stop sound

    "Acceptance."
    "A hand I have neglected holding all this time finds its way around my neck."
    "The difference in our size and our strength protects me from any real damage, and yet here I find myself beneath the weaker of us."
    "Makoto lowers herself down."
    "The insertion seems painful for her."
    "Perhaps she isn’t as aroused as she thinks."
    "Perhaps this is all one big facade to distract herself from the true pain of what has happened."
    "Perhaps “perhaps” doesn’t need to be used at all."
    "Because that’s exactly what this is."
    "Which is why it pains me to feel as good as I do right now."

    mak "Hah!..."
    mak "Fuck..."
    mak "It feels...extra hard today..."
    mak "Have you been getting bigger, [makotomaster]?"

    scene rhombus12
    with dissolve

    mak "Or do you just like it when I take control?"

    "This isn’t just {i}control.{/i} This is far worse than that."

    mak "Oh...you know what it is?...It’s the lack of another layer separating the two of us."
    mak "This is the closest we’ve ever been...isn’t it?"
    mak "I’ll remember this day for the rest of my life..."
    mak "Now...do me a favor and fuck me raw, okay?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene rhombus13
    with dissolve

    mak "Ahh! Ahh! Ahh!"
    mak "[makotomaster]! Yes! I’m...cumming again! I’m cumming again!"

    "It has been thirty minutes."
    "I know that for a fact since I’ve been staring at Makoto’s alarm clock this entire time."
    "Maki has yet to come to the door."
    "Or at least that’s what I’m telling myself so I can keep believing she hasn’t heard the sound of her little girl violently bouncing up and down on top of me."
    "Somewhere around the fifteen minute mark, the fishing pole fell over due to the constant vibration of the floor."
    "Makoto has climaxed four times."
    "And that’s four more than me."

    scene rhombus14
    with sexfade
    with sexfade
    with cumflash
    with hpunch

    mak "NGHHHHHHHHHHHH!!!!!!!!!!!!~~~~~~~~~~~~"

    "Makoto has climaxed five times."
    "And it’s only a matter of time until I start adding to the score."

    scene rhombus15
    with dissolve

    mak "You’re not...holding back on purpose...are you?..."
    mak "Are you afraid of knocking me up?.."
    mak "Is it because you don’t want to be a daddy?..."
    mak "Because...ngh...you’re afraid our little girl would get too...attached to you?..."
    mak "Because you’re worried about...what would happen to her when you can’t see her anymore?..."
    mak "Is that why you haven’t cum yet?..."
    mak "Because that would be a bullshit fucking reason and you should just do it already."

    "Makoto presses hard against my thighs and rocks back and forth with a level of technical skill that could only be achieved through both excess experience and exposure to things of such nature."
    "Thankfully, she got started on both of these long before she should have."
    "And now I get to partake of the bitter fruits of her unintentional labor."

    scene rhombus16
    with dissolve

    mak "So...what’ll it take to get you to cum?"
    mak "Want to try fucking my ass? I’m so deliriously pained {i}and{/i} pleasured right now that I doubt I’d even feel it."
    mak "I could also see if Miku wants to come back over. Though, I doubt she’d be as open to your fat dick as I am in the midst of my depressive fervor."
    mak "There’s a whole array of toys downstairs, too. Maybe one of those will help?"
    s "..."
    mak "..."
    mak "Heh...you’re really taking that “no talking” thing to heart. I’m so proud of you."
    mak "I {i}would{/i} like it if you’d stop acting like a corpse, though. You’re starting to remind me of my dad."
    mak "Oh! Speaking of my dad-"

    play sound "static.mp3"
    scene makotofirstinvlust22 with flash
    scene makotohandy33 with flash
    scene makotohalloween27 with flash
    scene makotofirstlust22r with flash
    scene rhombus17 with flash
    stop sound
    with hpunch

    "I cum."
    "I let the better memories in on accident."

    mak "Oh."
    mak "I didn’t even realize you were that close."
    s "..."
    mak "It feels a little different than I thought it would."
    mak "It’s actually kind of gross."

    scene rhombus18
    with dissolve

    mak "Anyway, thanks! You can go home now."
    s "You won’t even talk to me after that?..."
    mak "I just came five times. You think I have the energy left to talk?"
    mak "The bright side is that I’m so worn out that I might actually be able to fall asleep now! Here’s hoping I don’t have that {i}fucking{/i} dream again!"
    s "Makoto-"

    scene rhombus19
    with dissolve

    mak "Ahh...the feeling of it slowly turning soft inside of me after a strenuous workout...it’s becoming my heroin."
    s "I can’t leave here without knowing if you’re going to do anything stupid or not."

    scene rhombus18
    with dissolve

    mak "Oh, don’t worry about that because I’m pretty sure I fucking {i}can’t,{/i} so yeah. Fun."
    s "I...have no idea what that means. But will you at least tell me when you’re planning on coming back to school?"
    mak "Hmm...maybe I won’t come at all? I’ve already lost all of my motivation, so...kind of pointless, don’tcha think?"
    mak "We can still be fuck buddies, though. My mom was surprisingly reliable when it came to not interrupting us during our {i}personal{/i} time."
    s "..."
    mak "What’sa matter? You weren’t hoping we’d be anything {i}more,{/i} were you? Because that wouldn’t make sense when you’ve already told me you don’t want me to be your girlfriend."
    s "Get off of me, Makoto."
    mak "What? Did I make you mad?"
    s "I’m not mad. You’re not {i}you{/i} right now."
    mak "This is the most {i}me{/i} I have ever fucking been. But, sure. I’ll get off of you."
    mak "Just don’t forget to tell my mom you {i}fixed{/i} me on the way out, okay?"
    mak "I’m sure the pain will all come rushing back in momentarily."
    mak "But, while we were having sex, it really {i}was{/i} harder to remember just how fucking pathetic everything has become."

    scene black
    with dissolve2

    "I exit Makoto’s bedroom and head directly for the stairs."

    play sound "glass.mp3"

    "On the way down, I knock one of the picture frames off of the wall."
    "Curiosity gets the better of me and I stare down at the mess I have made."
    "Beneath the cracked glass is a photo of a little girl in a fisherman’s cap."
    "She rests on the shoulder of a man that is no more."

    play sound "dooropen.mp3"

    maki "Hey! How’d it go? Is everything okay with-"
    s "I knocked one of your pictures off the wall."
    s "It was an accident."
    maki "Huh? Oh. Yeah, that’s fine. I can just get another frame. What I’m more worried about is how Makoto-"
    s "She’s fine now."
    s "Well...not {i}fine,{/i} but..."
    s "She’s sleeping..."
    maki "Oh, thank God. I knew calling you over here was the right thing to do."
    s "Yeah..."
    s "I’m glad I was able to help."
    maki "Do you need a ride home? Or-"
    s "I...actually feel like walking."
    s "But I’ll see you around."
    maki "Oh. Uhh...sure, yeah. I guess I’ll just text you with any updates on Makoto."
    maki "If you don’t mind, though, would you maybe want to come back sometime soon and-"
    s "I think you should try handling her on your own from this point on."
    s "I...don’t know if she’ll be more open to talking to you now, but..."
    s "I don’t think there’s anything more I can do for her in her current state."
    maki "Yeah...Yeah, you’re right."
    maki "I guess this is goodbye, then."
    s "Yeah. See you, Maki."
    s "And...good luck."

    stop music fadeout 15.0

    "I leave the porn shop-"
    "The Miyamura family home-"
    "And wash my cock off in the sink of a public restroom."
    "As I step outside of it and back into the light, I listen closely to the clouds above- hoping to hear the same screaming Makoto did."
    "Of course, I hear nothing."
    "I never do."

    s "..."

    "Maybe that’s why I always feel so alone."

    $ renpy.end_replay()
    $ makotolust30 = True
    $ makoto_lust += 1
    $ maki_love += 1

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"

    $ yumiblock = True
    $ makotoblock = True
    $ mikublock = True
    $ nodokablock = True
    $ makiblock = True

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label sadgirls8:
    scene hall_noon
    with fade
    play music "10c.mp3"

    "We’re now merely two hours away from what will be a complete week since Makoto got the news about her father."
    "Oh, and I guess Nodoka got her ass kicked as well- but that sort of pales in comparison to the emotional rollercoaster I was forced onto just minutes later."
    "Since then, things have calmed down a little."
    "Yumi was “indefinitely suspended” for attacking a fellow student."
    "Nodoka’s black eyes have started to fade back to their usual color."
    "Even Yasu has returned to normal."
    "Or...at least as normal as Yasu can possibly be."
    "I also have no idea how I would have survived this last week without Imani (Who seems to have forgiven me following the Yumi incident) seeing as she’s taken over all the clerical stuff in Makoto’s absence."
    "The only person who really {i}hasn’t{/i} shown any sign of improvement yet is Miku..."
    "Who, understandably, is decaying from the inside out knowing that the beautiful mind of her best friend is rotting away in a dark room several miles from here."
    "It’s a room that she’s spent far more time in than me."
    "It’s a room that she’s brave enough to return to while I would sooner slip back into the shadows and pretend none of this ever happened."
    "But every time I look at Makoto’s desk, that wishful illusion is suffocated out of existence."
    "And every time I watch her friend reflexively shift her gaze over to it to try and convince {i}herself{/i} this was all just some horrible dream, the truth is reinforced."

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    "But that’s just the way it goes, I guess."
    "Sometimes, bad things happen to good people."
    "More often than not, it seems like this pattern not only continues, but aggressively ramps up with each passing day."
    "Sometimes, bad things {i}won’t{/i} stop happening to good people."
    "And while I wish that I could take these words to heart and truly feel something reminiscent of sympathy for the good person in question-"
    "I am one of those bad things."
    "And it would make no sense at all for me, burdened by my constant obsession with navel-gazing, to slight them when I am of that same ilk. "
    "I’ll remain quiet. "
    "I will wait."
    "And I will only moderately taint those that come to me with their concerns."

    scene makotoback1
    with dissolve2

    s "..."

    "And I will only moderately taint those that come to me with their concerns..."

    mi "Mornin’, Sensei."
    s "Good morning, Miku. Are you feeling any better?"
    mi "Not really. Was actually plannin’ on askin’ ya if I could maybe leave early today."
    s "You don’t need to ask. You can leave literally whenever you want. "
    s "I’m honestly surprised you’re coming at all given everything that’s happened."

    scene makotoback2
    with dissolve

    mi "I’d feel too bad ditchin’ swim club when two of the members ain’t comin’ to school right now and one of em’s still too sore to actually do anything."
    mi "Karin’s finally a captain, too. Bailin’ and leavin’ her with just one other girl would be way too rude."
    s "I think Karin’s mature enough to understand that you might want a little time away right now."

    scene makotoback3
    with dissolve

    mi "It’s fine, Sensei. Really. Gettin’ some exercise is good for me right now anyway. Helps get my mind off of stuff."
    mi "Sorry we ain’t been spendin’ much time together lately, though. All my free time’s been goin’ to Makoto and...yeah."
    s "How is she?"

    scene makotoback4
    with dissolve

    mi "She ain’t changed much. Still really sad and...sayin’ a bunch of things that don’t make much sense to me."
    mi "She’s bein’ a little nicer to Maki, though. Hasn’t really yelled at her lately. "

    scene makotoback3
    with dissolve

    mi "That wouldn’t have somethin’ to do with your little visit there, would it?"

    if makotolust30 == True:
        mi "Heard you were able to take Makoto’s mind off of stuff for almost a whole day. "
        mi "How’d ya do it? Lettin’ me and Maki in on your secret technique might be able to get her up and at ‘em again a little bit sooner."
        s "I...think it’s best if my technique remains hidden."

    else:
        s "You mean when I went into her room and tried having an actual conversation with her only for her to throw it back in my face?"
        s "I left before anything even happened. I doubt Makoto’s sudden change of heart has anything to do with me."
        mi "Well, I obviously wasn’t there, so I’ve got no idea what actually went down. But I think it’s clear as day that you showin’ up definitely helped at least a {i}little.{/i}"
        mi "Fact is, even if she didn’t seem like it at the time, Makoto loves ya. There ain’t no way she’d actually be mad about you tryin’ to be there for her."

    s "Whatever the case, I hope she comes back soon. Class is weird without her."

    scene makotoback5
    with dissolve

    mi "It really is, ain’t it?!"
    mi "I know we’re already pretty disorganized, but without Makoto actually givin’ people work to do, the whole heckin’ class has turned to chaos!"
    mi "I’m gettin’ dumber by the day, Sensei! And I was already in last place to begin with! I can’t afford this."

    play sound "slidedoor.mp3"
    stop music fadeout 5.0
    scene makotoback6
    with dissolve

    s "Well, I can’t say I’ll be as much help as her...but I guess I could try actually {i}teaching{/i} you for a little while each day until she comes back."

    scene makotoback7
    with dissolve

    s "Anything involving math, though, you're probably better off asking Imani. She’s a lot better at-"
    mi "Makoto?..."
    s "What?"

    play sound "static.mp3"
    scene makotoback8
    with flash
    stop sound
    play music "andlove.mp3"

    mak "{b}Guess who’s back, bitches.{/b}"
    mi "Makoto, what the heck are you doin’ here?! There ain’t no way you’re ready for this yet!"
    s "I think it might be time to cash in on that “going home early” thing, Miku. Take Makoto home before-"

    scene makotoback9
    with dissolve

    mak "Guys...guys! I’m {i}fine!{/i} I was able to dress myself and everything."
    mak "Besides, if I spend any longer inside of that room, I’m going to go fucking insane."

    scene makotoback10
    with dissolve

    mak "So, what’s new? Is Nodoka dead too? Is Yumi still a fucking bitch?"
    mak "Has Sensei been completely fucking worthless without me here to do everything for him?"
    mak "Or is shit pretty much the same?"
    mi "Makoto..."
    mak "What’s wrong? Taken aback by the fact that I’m now engaging in schoolgirl gossip rather than shunning it and burying my face in a fucking notebook instead?"
    mak "Spit it out, Miku. Tell me how much has changed."
    mak "Tell me how much happier everyone is without me here."

    play sound "static.mp3"
    scene makotoback11 with flash
    stop sound

    m "Well, that’s...certainly a look for her."
    m "I wonder what happened?"
    m "It’s not like Makoto to be anything less than perfect...and this sudden shift in aesthetic has made whatever the situation is impossible for me to ignore any longer."
    a "..."
    m "You haven’t heard anything from Sensei, have you?"
    a "..."

    scene makotoback12
    with dissolve

    m "Ami?"

    play sound "static.mp3"
    scene makotoback13 with flash
    stop sound

    mak "Okay! Since Miku didn’t have anything to say...how about you, Sensei?"
    mak "I haven’t seen {i}you{/i} since my mom dragged you all the way to my fucking house to try and manipulate me into not being sad anymore."
    s "That’s not what happened, Makoto."
    mak "Hmm...I guess that can be kind of subjective, yeah."
    mak "But something that definitely {i}did{/i} happen is you knocking one of my dad’s pictures off the wall and shattering it into a million pieces."

    if makotolust30 == True:
        mak "Was the mark you left on me not enough back then? You had to leave one on my fucking {i}hallway{/i} too?"
    else:
        mak "Just couldn’t go home without leaving your mark, huh?"

    mak "Did you know that a shard of glass managed to cut {i}right{/i} through my dad’s neck in that picture? Do you have any idea how fucking hysterical that is?"
    mak "I don’t even care that it was my favorite picture of us. That was genuinely {i}hilarious{/i}."
    s "Can the picture be replaced?"
    mak "With what? Wanna hang one up of yourself?"
    s "You know that’s not what I meant..."
    mak "Ooh! Maybe we can take one as a family! You can put your arm around me. I can look up at you with childish admiration in my eyes."
    mak "And then you could go into space and fucking suffocate because my life sucks and things like that just happen to me now."

    play sound "static.mp3"
    scene makotoback14 with flash
    stop sound

    ay "..."
    sa "Um...Ayane?..."
    sa "I know she’s kind of far away, but...you didn’t just hear what Makoto said...did you?"
    ay "I’ve never been so upset to have good hearing before..."
    ay "That poor girl...I can’t even imagine how that must feel."
    sa "Is...Is there something we can do?..."
    ay "I have no idea..."
    ay "And I’d say that the best thing we can do while we figure that out is to pretend we {i}didn’t{/i} hear anything, but..."
    ay "I think that is about to become impossible."

    play sound "static.mp3"
    scene makotoback15 with flash
    stop sound

    mi "Makoto! Stop it! You don’t have to come back to school yet! There’s no rush at all!"
    mi "Let’s...let’s go to the dorm! We can be alone there and I can tell ya all about how much school has sucked without you here!"

    play sound "slidedoor.mp3"

    ima "Senpai! I know you told me to stay in {i}our{/i} office until I finished with all of your paperwork. But I just got a call from Makoto’s mom and-"
    ima "Oh, fuck."
    mak "Attention, please!"
    ima "{i}Senpai, what do we do? Her mom doesn’t even know she’s here right now. She told me she went missing.{/i}"
    s "{i}Let’s...{/i}"
    s "{i}Let’s let her talk...{/i}"
    mak "I said {b}ATTENTION PLEASE!{/b}"
    mak "I know this isn’t the beginning of the school year anymore and that this is a really weird time to do this, but I’d like to take this opportunity to get to meet all of you!"
    mak "My name is Makoto Miyamura and my dad is fucking dead."
    o "Holy shit..."
    r "..."
    f "Oh, no..."
    f "I was really hoping...it wouldn’t be anything like that..."

    scene makotoback16
    with dissolve

    mak "I know that none of you have ever fucking cared about me, so this might just sound annoying, but I’d also like all of you to know that you won’t {b}have{/i} to be annoyed by me any longer!"
    mak "Because I don’t fucking care anymore!"

    scene makotoback17
    with dissolve

    mak "Schoolwork?! Studying?! Why waste time on things like that when life is finite and could be stripped from you at any moment?!"
    mak "What’s the point of striving to become better when it’s all for fucking nothing in the end?!"
    mak "In fact, what’s the point of living at all when it’s just constant stress and suffering and pain with {i}liiiiiittle{/i} tiny bits of the good shit sprinkled on top?!"
    c "We {i}do{/i} care about you, Makoto! Of course we care!"
    n "Chika’s right! If you need anyone to talk to, we-"
    mak "BZZZZZZZZZZZZT! {b}THE ANSWER IS THERE IS NO FUCKING POINT.{/b}"
    mak "Of course you’re going to act like you care now. Fucking look at me. You’d have to be fucking heartless  to ignore a girl giving a speech about her dead fucking dad."
    mak "But where were you before this?"
    mak "Where was fucking anyone other than Miku while I was suffering alone in my room?"
    mak "Which isn’t to say that any of you showing up would have fucking {i}helped{/i} me. But it really would have been the nice thing to do, right?"
    mak "Like...I don’t know. Maybe a fucking card?"
    mi "They didn’t know, Makoto! We didn’t tell anyone because we thought it was too soon!"

    scene makotoback18
    with dissolve

    mak "{b}TOO SOON?!{/b}"
    mak "My world is fucking exploding right now and you think it’s “too soon?!” For what?!"
    ki "Hey, don’t take your anger out on Miku! She’s been miserable all week long worrying about you!"

    scene makotoback19
    with dissolve

    mak "I’m not taking anything out on anyone! In fact, you’re {i}all{/i} pretty fucking great! It’s no wonder you haven’t bothered with {i}me!{/i}"

    scene makotoback20
    with dissolve

    mak "I annoy you, right?"
    mak "You hate that I’m the one who forces you out of what should be seven hours of pure fun and relaxation..."
    mak "You hate that you can’t spend all of your time with Sensei because I’m constantly making him spend time with {i}me{/i} instead..."
    mak "You hate the worksheets. And the quizzes. And the message board. And all of the other stuff I put together because something inside of me made me feel like I had to make my daddy proud one day."
    mak "And that if he saw how smart and responsible I’d become...that he’d be able to die happy."

    scene makotoback21
    with dissolve

    mak "But, instead..."
    mak "He just {i}died.{/i}"
    mak "And now I’ll never know if he was happy or not."

    scene makotoback22
    with dissolve

    mak "But, I’ll tell you one thing I {i}do{/i} know..."
    mak "It's that {i}I{/i} sure as fuck won’t ever be."
    mak "There’s nothing left for me to work for."
    mak "No reason to keep trying so hard for a bunch of people who see me for who I {i}really{/i} am."
    mak "An incorrigible...irritating...loud mouthed bitch."
    mak "Just like my mother."

    play sound "static.mp3"
    scene makotoback23
    with flash
    stop sound

    ima "Are you really sure we should be letting her ramble on like this? She’s clearly out of it and this is, like...reputation suicide."
    s "Maybe that’s what she wants?"
    ima "Senpai..."
    s "Who says starting over has to be a bad thing?"
    ima "No one. {i}I’m{/i} not saying that. I just think that we should maybe wait until she’s...oh, I don’t know- not running away from home and giving speeches to the class while cosplaying as a fucking zombie."
    ima "I just don’t want her going out in some blaze of glory while everybody else sits back and watches."
    s "Who says everyone’s just sitting back and watching?"
    ima "Senpai, what are you talking about? Are we not seeing the same thing right now?"
    s "Stop staring at me and take a look for yourself."

    play sound "static.mp3"
    scene makotoback24 with flash
    stop sound
    stop music

    mak "..."
    a "Shut up..."
    a "Shut up...shut up...shut up..."
    a "Hearing you say those things..."
    a "It brings back too many bad memories..."

    scene makotoback25
    with dissolve2
    play music "kimitoakinobouken.mp3"

    mak "..."

    "Sometimes, all it takes to reduce the suffering is someone you can relate to."
    "Someone who climbs out of the woodwork and into your arms...that you can abhor in moments of joyous splendor and admire in stretches of constant pain."
    "I let her speak because I knew this would happen."
    "I knew it from the moment I saw Ami’s face."
    "Because Ami is a girl I have cherished and loved."
    "She is a girl I understand."
    "And Makoto?"
    "Makoto will become one of those too."
    "But for now, she needs to suffer."
    "For now, she needs to cry."

    scene makotoback26
    with dissolve2

    mak "{b}AAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!{/b}"
    ima "Uhh...okay! If your name isn’t Makoto, Ami, Miku, or Sensei, please leave the room right now! We’re going to have class in the gym or something!"
    ki "I actually think Miss Watabe’s class is in the gym right now."
    ima "Then it looks like we’re having a joint period! Go, go, go!"

    scene black
    with dissolve2

    "The girls filter out of the room paying minimal attention to what’s happening in the front of the class despite a burning interest to act in opposition to that."
    "Imani is the last one out, sliding the door closed after locking eyes with me and silently admitting that sometimes I can, whether it be intentional or not, actually know what needs to be done."
    "Those moments are few and far between. And frankly, this moment isn’t even one of triumph for {i}me{/i} as all I did was clear a path for the only person actually able to do anything when it comes to pain like this."

    scene makotoback27
    with dissolve2

    a "Never say you won’t ever be happy again! It’s a lie! A lie I told myself over and over when this happened to me!"
    mi "Ami’s right! This’ll sting forever, but there’s plenty more good stuff out there! Good stuff I wanna see and experience with my best friend!"
    mi "You think we woulda made it as far as we did if we just gave up?!"
    a "Yes, you’re annoying! Yes, I hate the stupid worksheets! And yes, I kinda hate {i}you{/i} when you spend every day trying to steal my uncle away from me!"
    a "But I’d never wish this sort of pain on anybody in the whole wide world!"

    scene makotoback28
    with dissolve2

    a "And you need to know that life goes on."
    mak "Ami..."
    a "There isn’t a day that goes by where I don’t miss my parents. I can’t even cross the street without having to force back tears."
    a "But Sensei makes me happy now! And you still have your mom!"
    a "Let her be that for you! Stop closing yourself off and let {i}her{/i} make you happy instead!"
    a "That’s what your dad would have wanted, isn’t it?!"
    a "Wouldn't he have wanted you to be happy?!"

    scene makotoback29
    with dissolve2

    mak "But..."
    mak "It’s so hard!"
    mak "I can’t stop thinking about him! About what his final thoughts must have been! About how I never got to say goodbye!"
    a "I know it’s hard! But it'll only get easier from here, Makoto! So don’t give up just yet!"
    a "Keep being the same annoying you! Because even if we’re not there for you all the time and forget to make cards when things are horrible, we {i}do{/i} care!"
    a "And we can cry together when no one else understands our pain!"
    mak "I don’t want to cry anymore! I don’t want to cry!"

    scene makotoback30
    with dissolve

    a "Well, too bad because I do!"

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "I leave the classroom as well and retreat to the gym to meet back up with the rest of the girls."
    "There was no reason for me to be in that classroom any longer."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve2

    "But what I heard from Ami in the coming hours is that things worked out okay."
    "That Makoto went back home with Miku and has decided to take a little time off of school for the foreseeable future."
    "That she wouldn’t try running away again. And, if she ever felt the urge to, she’d talk to her mom first."
    "Of course, those are just words. And she may very well act out against them."

    scene black
    with dissolve

    "But something about the way they sound when released by the mouth of a third party makes me want to trust them a little more this time."
    "You see, the thing with words is that they’ll always be ephemeral."
    "And that, with how rapidly our lives and the world itself are changing, they’re really just air in the end."
    "And so Makoto will suffer as she remembers the life of the man she loved most."
    "But that’s fine."
    "Because if she listens hard enough, she’ll still be able to hear his voice in the whispers of the world itself."
    "And that gift from the sky should be enough to keep her grounded."

    $ renpy.end_replay()
    $ sadgirls8 = True
    $ makoto_love += 1
    $ mikublock = False
    $ makiblock = False
    stop music fadeout 10.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}But she’ll need some time alone for a while...{/i}"
    "........."
    "......"
    "..."

    jump advancetosat

label makotospecial50:
    scene unbluejay1
    with dissolve2
    play music "10c.mp3"

    "Redbirds bleed and blue ones die — that’s the nature of this world of mine."
    "The green ones sing, the yellows cry — yet still the redbirds bleed. But why?"
    "I close my book. Breathe out a sigh. Then pierce the glass with both my eyes."
    "Approach the window, scan the sky — beneath the clouds, above the pines."
    "The blue ones fall as the red ones rise. Don’t ask me how, I won’t reply."
    "I can’t tell you why the cardinals fly. I can’t tell you why the blues won’t try."
    "I can’t tell you anything as I-"
    "I hate this fucking world of mine."
    "I hate the birds. I hate the sky. I hate paper, pencils, crooked lines."
    "These are reasons why I sometimes try imagining that I am blind."
    "I know there’s beauty here. "
    "There has to be."
    "It’s just way too hard to find."

    mak "Helloooo? Senseiiiii? Did you forget that you’re supposed to be {i}working{/i} right now?"
    s "Forget? No. Ignore? Yes."
    mak "Well, on the bright side, you’re almost done. I just need your signature on a few more forms and you can go back to being irresponsible and lazy like you always are."
    s "Why haven’t you just started forging my signature on everything yet? That would save both of us so much time."
    mak "Because I’m honest. Which is also why I don’t mind admitting that these paper-relays of ours are some of the very few moments we share that actually count as bonding in my book."
    s "Does it not count as bonding when I put my penis inside of you?"
    mak "It used to. Now, that’s more akin to something like cracking my knuckles or yawning. Just a standard bodily function. The novelty has worn off."
    s "What am I even signing anyway? Why are there so many more sheets of paper than normal?"
    mak "Because you have twenty different students who all just finished their standardized tests — which, and this may come as a big surprise to you, are a {i}little{/i} more in-depth than just one sheet of paper."
    s "I don’t know if I believe you. I feel like you might just be handing me blank sheets of paper in order to pad the numbers of our “bonding time.”"

    scene unbluejay2
    with dissolve

    mak "Are you seriously not even looking at them? They’re very clearly not blank."
    s "They look blank to me. But that’s probably just because I’ve gotten so used to tuning everything out that the words don’t even register anymore."
    mak "That is both very sad and very impressive. I wish I could care as little as you."
    s "You did for a little while. What happened to that Makoto? How do we bring {i}her{/i} back?"

    scene unbluejay3
    with dissolve

    mak "Easy! By killing someone else who’s important to me."
    s "Pass. Too much effort. Also, your mom would have been proud of that joke."

    scene unbluejay4
    with dissolve

    mak "Ahh, my poor mother...I remember her like it was yesterday. What a shame that she, too-"
    s "I’m glad you’re feeling better, Makoto."

    scene unbluejay5
    with dissolve

    mak "Huh? "
    s "I said I’m glad you’re feeling better."
    mak "Are you saying that because you mean it? Or because you think I’ll take it easy on you and let you finish signing things early because you showed me the slightest bit of sentimentality?"
    s "...Both?"

    scene unbluejay6
    with dissolve

    mak "Just sign the last few papers, Sensei. We’re almost done."
    s "I will sign {i}one{/i} more. The rest can wait until tomorrow. My hand hurts."
    mak "Just one? Really?"
    s "Choose wisely, Makoto. Whose grades matter the most?"

    scene unbluejay7
    with dissolve

    mak "Hmm...just {i}one,{/i} huh?"
    mak "But there are at least eighty more that need to be signed."
    s "I thought you said we were-"

    scene unbluejay8
    with dissolve

    mak "Here! Sign this one!"
    s "Final answer?"
    mak "Final answer."

    scene unbluejay9
    with dissolve

    "I take the “final” paper from Makoto and, after looking at it for almost a full second, I spot her name and realize that there was really only one option available to her in the first place."
    "Then, as I sign my name along the bottom section of the document, I silently applaud her for her selfishness as it is one of several things we have in common."
    "The other things being poor vision and a burning passion for rough sex — even if she claims it isn’t much of a big deal anymore."

    s "Okay. Done."

    scene unbluejay10
    with dissolve

    mak "Thank you for your service."
    s "It was hard, but I’m glad we made it through the day."

    scene unbluejay11
    with dissolve

    mak "It’s been approximately fifteen minutes since I came in here."
    s "Yeah, but you were there for the rest of the day so the statement stands. But anyway, what now? Want to engage in “bodily functions” on the couch?"
    mak "That sounded absolutely disgusting even if I knew what you meant."
    s "Yeah, I’m sorry."

    scene unbluejay12
    with dissolve

    mak "Would it be selfish of me to ask if I can have you for a little while longer?"
    s "Yes. But I was actually just thinking about how I like your selective brand of selfishness, so go ahead and have me. But I’d still prefer the couch over-"

    scene unbluejay13
    with dissolve

    mak "Not here."
    mak "There’s somewhere else I want to go."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene unbluejay14
    with dissolve2

    "It becomes fairly evident that Makoto was asking to “have” me in a more {i}hands-free{/i} sort of way the moment we make it up to the rooftop."
    "Either that or she’s just into the same sort of stuff Ayane is. Which, honestly, wouldn’t be all that surprising since Ayane’s only fetish seems to just be {i}me{/i} as a whole."
    "The air is warm, but not warm enough to make me regret coming out here. It’s one of those days where you’re acutely aware that it {i}is{/i} summer, but..."
    "Well, if I didn’t know any better, I’d say this is a little closer to spring."
    "Makoto skips closer to the fence, causing her skirt to bounce along with her “perverted adjective, followed by perverted noun.”"
    "And, in other news, signing so many papers in one sitting has drained the last bit of motivation I have left in my body."
    "It is all downhill from here."

    mak "This weather’s amazing, isn’t it? And the sky is so bright."
    s "It’s probably symbolism."

    scene unbluejay15
    with dissolve

    mak "Is it? For what?"
    s "Maybe this...newer...bubbly front you’re putting on."
    mak "It’s not a front, Sensei. "
    mak "The skies are just starting to clear up a little. "
    s "I knew it was symbolism. I told you."
    mak "I will take that as a passing grade on this impromptu weather-based and somewhat-literary evaluation test. Thank you very much."
    s "Let’s hope it lasts this time and that no further tragedy follows the customarily tragic life of Makoto Miyamura."

    scene unbluejay16
    with dissolve

    mak "Even if it does, I think I’ll be fine."
    mak "The worst has passed. Things couldn’t possibly be that bad ever again without me losing a child or something. And I’m not even sure if I want kids."
    s "You don’t."
    mak "You’re only saying that because {i}you{/i} don’t want kids. "
    s "Why would I ever say anything that doesn’t directly relate to me? That just sounds like a waste of time."
    mak "Narcissism and uncertain futures aside, I hope you’re right. I’ve had enough tragedy for one school year. "
    mak "Actually, I’ve probably had enough for my entire high school career. So yeah, let’s hang it up for now."
    s "Back to the original plan then? Working hard and just doing your own thing with little regard for your own sanity and how everyone else feels about you?"
    mak "Maybe."
    mak "I’m trying not to think about it."
    mak "I just kind of want to exist right now."

    scene black
    with dissolve2

    mak "And whatever that entails is fine by me."
    s "Makoto? Where are you going?"
    mak "Hm? Higher. To get a better view of the city."
    mak "Want to follow me up? Or would you rather stay down there on the ground like a pansy?"

    "Being an alpha-male who is most assuredly not a “pansy,” I follow Makoto up the ladder until we’re level with the fence..."

    scene unbluejay17
    with dissolve2

    "A fall from this high up would certainly kill us, and I need to think for a moment about whether or not my incessant beratement of Makoto would prompt her to end my life."

    mak "I’m really happy you’re here, Sensei."

    "She attempts to lure me into a false sense of security."

    s "Is that only because you brought me up here to murder me?"

    "I subtly let her know that I’m onto her."

    mak "No. It’s because there’s no one I’d rather look out over this horizon with than you."
    mak "It feels almost nostalgic in a way, doesn’t it?"
    s "Well, yeah. We’ve been up here before."
    s "That was a long time ago, though."
    mak "A lot has happened since then, huh?"
    s "More than you know, Makoto. "
    mak "Do you think I’ll make a good teacher one day?"
    s "I think you make a good teacher right now. I worry about how “good” you’ll be once you’re done with college. "
    mak "I really hope I can be like you one day. Just without all of the statutory rape. And lack of motivation. And built-in cynicism."
    s "So basically, you just want to have my job title."
    mak "And the ability to motivate people. Yes."
    s "I don’t motivate anyone, Makoto."

    scene unbluejay18
    with dissolve

    mak "You don’t {i}try{/i} to motivate anyone. But the weird and unfortunate truth is that you unintentionally {i}do.{/i}"
    mak "Though, I guess it’s possible that we’re all so desperate to end up as someone unlike you that seeing you struggle gets us to “wake up.”"
    s "Have we entered the arc where {i}you{/i} bully {i}me{/i} now?"

    scene unbluejay19
    with dissolve

    mak "Possibly. All things considered, I’m definitely not the same girl I was the last time we were up here."
    mak "What kind of girl that {i}makes{/i} me, I have no idea. But I know I’ve gotta get it together if I want to keep looking up at the clouds like this."
    mak "For a while, well before everything with my dad happened, the sky lost its color. It was this...huge blanket of gray that made everything beneath it look lifeless and dull."
    mak "I thought about leaving a ton of times."
    mak "I went as far as writing notes. To you. To my mom. To Miku. I even wrote one to Ami once — but even that was mostly about you."
    s "Makoto-"
    mak "I thought about coming up here, throwing myself off of this roof, and letting life move on without me because I just didn’t have what it takes to keep going."

    scene unbluejay20
    with dissolve

    mak "I still think about it sometimes. "
    mak "About what would have happened if I had followed through."
    mak "I think about what would happen to my mom and the store."
    mak "I think about what would happen to Miku’s grades. "
    mak "Or if you’d blame yourself for it even though it was never your fault. "
    mak "This is the way I’ve always been. And hey, maybe I’ll be this way forever — never totally sure of whether or not there’s a purpose out there for someone like me."
    mak "But that’s okay...because I know the end of my suffering would just spell {i}more{/i} suffering for all of those people I wrote to."
    mak "So one of my new goals is to prevent anyone I care about from ever having to read anything like that."
    mak "I don’t want anyone else to ever have to feel the way I do."
    s "..."

    scene unbluejay21
    with dissolve

    mak "Sorry...that probably wasn’t as happy of an ending as you were hoping for, was it?"
    s "No, it really wasn’t..."
    s "I expected something more along the lines of “I want to be here now because I’ve found what it means to be happy” or whatever."
    mak "That sure would be nice, wouldn’t it?"
    mak "And...who knows? Maybe some day, I’ll be able to think that way. But for now-"
    s "You just want to exist."

    scene unbluejay22
    with dissolve

    mak "That’s right..."
    mak "But in a way, for someone who’s always setting the bar so high, maybe a little goal like this will be easier for me to climb over?"
    mak "I have no one to succeed for anymore other than myself. "
    mak "If I look at it that way, I won’t have to push myself so hard."
    mak "And if I don’t push myself so hard, I’ll have more time to focus on what I know matters more than anything else."
    s "And that is?"
    mak "Not writing any more notes."
    mak "And learning how to smile from the bottom of my heart instead of the pit of my stomach."
    s "..."
    mak "..."
    s "I’m really happy you’re here, Makoto."

    scene unbluejay23
    with dissolve

    mak "Hey. That was {i}my{/i} line. You can’t just go plagiarizing me as soon as there’s an awkward silence."
    s "Sure I can. And until you’re the one in my position, you can’t tell me what to do."

    scene unbluejay24
    with dissolve

    mak "I can’t?"
    s "You can’t."
    mak "Bummer."
    mak "Can I at least ask for a little favor, though?"
    s "I’m done grading papers until tomorrow."
    mak "It’s not that. It’s something else."
    s "What is it?"

    scene black
    with dissolve2

    mak "Can you close your eyes for a second?"

    "........."
    "......"
    "..."

    scene unbluejay25
    with dissolve4

    "Redbirds bleed and blue ones die — that’s the nature of this world of mine."
    "There’s no song to sing nor hymn to cry — just an aching heart and wat’ry eyes."
    "I hate love and lust and God and lies. I hate hummingbirds. The word “Goodbye.”"
    "But if you’d ask me now, beneath this sky-"
    "I could tell you why the cardinals fly."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ makotospecial50 = True
    $ makoto_love += 5
    stop music fadeout 7.0

    "{i}Makoto’s affection has increased by 5!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label makotopool55:
    scene makotomikupool1
    with fade
    play music "notabluearchivesong.mp3"

    "I make my way over to the pool to spend some time with two girls I will one day have a threesome with because, despite Makoto showing no interest in doing that with Miku, we all know it will happen one day."
    "I mean, just look at them. Those are the faces of two best friends who are longing to share the same penis."
    "But I digress."
    "The {i}real{/i} reason I’m here is to see if Makoto is still sticking to her “Live because others want you to” plan or however it was she worded it on the rooftop the other day."
    "It’s admirable. {i}Foolish,{/i} but admirable. "
    "It’s important to note, however, that I am a man who is living almost entirely for his self, so I am very likely a bit biased. "
    "I guess what really matters at the end of the day is that Makoto stays grounded. {i}How{/i} she does that is up to her. Just like {i}how much she enjoys it{/i} is up to her as well (depression aside)."
    "Moving forward is a good place to start."
    "I just hope she doesn’t wind up walking around in circles."

    s "Hello, ladies."

    scene makotomikupool2
    with dissolve

    mak "Uhh...hello {i}Sir?{/i}"
    mi "Sensei! Been meanin’ to call ya! Congratulations!"
    s "For what? What did I do? "

    scene makotomikupool3
    with dissolve

    mi "Ya finally locked lips with my BFF after a billion years, that’s what! Took ya long enough, you sly dog. "
    s "Oh, good. So it appears that Makoto is just as open about our relationship behind closed doors as you."
    mi "That’s what best friends are for. Duh. ‘Sides, you two’ve already done the nasty a good hundred times by now. Kissin’ ain’t nothin’."
    s "Seems like a lot to Makoto based on her reaction."
    mak "Oh, you know...It was only something I was looking forward to for...practically forever."
    mi "How’d ya do it? Tongue? No tongue? She good? Better than me?"
    s "I have no further interest in discussing this with you, Miku."

    scene makotomikupool4
    with dissolve

    mi "Guh. You men and your damn secrets. "
    mak "I haven’t told anyone else. Don’t worry. "
    s "Who else would you even tell? Your mom?"

    scene makotomikupool5
    with dissolve

    mak "I have other friends! Touka and I hang out sometimes! And I’ve come over to your house on several occasions just to see Ami!"
    mi "Oh, maybe {i}I{/i} should tell Maki we’re a thing now? She could probably give me all sortsa cool sex tips."
    s "Miku, apart from Makoto, just never tell anyone about anything we do ever. Okay?"
    mi "Not even if it means missin’ out on cool sex tips?"
    s "I can assure you that Makoto can give you all of the “cool sex tips” you need."

    scene makotomikupool6
    with dissolve

    mi "Do you know how to do that thing where you unlock your jaw? Can you teach me? That sounds useful."
    mak "Sure. Just as soon as Sensei remembers that I’m the one who’s supposed to be bullying him now."
    s "Hey, don’t get mad at me. This is almost entirely Miku’s fault. "
    mi "The reason I wanna know how to do the jaw thing is cause-"

    scene makotomikupool7
    with hpunch

    mak "You don’t have to tell me {i}everything,{/i} Miku! Come on!"
    mi "Well ‘scuse me for wantin’ to cash in on the cool sex tips I was promised."
    mak "There’s nothing I can teach you that the Internet can’t! These are things you can look up on your own time!"
    mi "Time?! But I barely have any time to-"

    scene makotomikupool8
    with dissolve

    mi "Oh, crap."
    mak "Crap? Why crap? "
    mi "I, uhh..."

    scene makotomikupool9
    with dissolve

    mi "I was supposed to meet up with Kirin to do some study thing! Because, you know, I’m an idiot."
    mak "What do you have to study for? We just finished all of our testing. Also, why didn’t you ask me?"
    mi "Cause...you’re too hard on me. And Kirin ain’t that smart either, so...I’m just gonna go do stuff with her."
    mak "Then...let me get dressed and I’ll come with you. I don’t have work tonight so-"

    scene makotomikupool10
    with dissolve

    mi "Nah, nah...don’t even worry about it. I’ll get outta your hair so you and Sensei can have some more alone time."
    mak "I really don’t mind-"

    scene makotomikupool11
    with dissolve

    mi "Go easy on ‘er, ya hear? No grabbin’ where the sun don’t shine in public places."
    s "Tell Io I said hi."

    scene makotomikupool12
    with dissolve

    mi "Ah..."
    s "..."
    mi "It’s...Kirin."

    scene makotomikupool13
    with dissolve

    "Miku scampers off and, unfortunately, I have a pretty good idea of where she’s going."

    mak "Io?"
    mak "Why would Miku be going to see Io?"

    scene makotomikupool14
    with fade

    s "Maybe there’s something Io can do for her that no one else can?"
    mak "You mean, like...woodwork?"
    s "Exactly, Makoto. Miku is secretly into woodwork, but is extremely embarrassed about it. Also, how do you even know Io is into that sort of thing?"

    scene makotomikupool15
    with dissolve

    mak "I’ve had to give her the key to the woodshop on several occasions now. Also, anyone could tell she spends her free time on {i}something{/i} physical just by looking at her hands."
    mak "What does any of that have to do with Miku, though? Why would you assume she’s hanging out with Io?"
    s "I don’t know if they’re “hanging out.” I just know she goes to see her sometimes. "
    mak "For...wood?"
    s "..."
    mak "..."
    s "Yes."

    scene makotomikupool16
    with dissolve

    mak "Sensei, what’s going on? Because between this and that weird “joke” you made when the two of us came over to play games, I’m starting to feel really weird."
    mak "I’ve also noticed that Miku’s been a little different than normal lately, so if you have any sort of insight into that, I’d greatly appreciate it."
    s "Weird how? What’s different about her?"

    scene makotomikupool17
    with dissolve

    mak "Nothing...{i}bad{/i} I guess. Just different. Maybe a little more focused and...less...{i}Miku-{/i}ish?"
    s "So...more like a normal girl?"
    mak "Like I said, it’s not {i}bad.{/i} She’s just seemed a little...off. But I don’t see what that has to do with Io."
    s "Then ask her. It’s not my place to reveal all of Miku’s secrets, but I’ll be damned if I don’t repeatedly hint at them until you do something about it yourself."
    mak "Yeah, well...I’m barely in the position to do that when I know I’ve probably been exactly the same as her."

    scene black
    with dissolve2
    play sound "water1.mp3"

    "Makoto pulls herself out of the pool and grabs a towel off a nearby rack to dry herself off before heading over to a bench."

    scene makotomikupool18
    with dissolve2

    "As I join her on said bench, I need to once again remind myself of how annoyed I am by those who meddle in {i}my{/i} affairs and that I’d be no better than them by following in their footsteps."
    "It would be different to directly involve myself with {i}Makoto’s{/i} affairs, though...wouldn’t it? "
    "Doesn’t she {i}want{/i} me to get involved with her problems? Isn’t that why she didn’t oppose me sitting down beside her?"
    "This isn’t like the Miku thing at all. Whatever is going on {i}now{/i} is something that I’m a part of."

    mak "Maybe it’s just stress."

    "Or maybe whatever is going on {i}now{/i} is much smaller than I anticipated-"
    "And these rare worries of mine were all for nothing."

    s "Stress?"
    mak "The feeling of emotional or physical tension."
    s "I know what stress is, Makoto. I was asking why you’d think that. "
    s "I get that you have plenty on your plate, but what does Miku have to be stressed about?"
    mak "Lack of purpose. Bad grades. Diving into a sexually active life despite barely any prior knowledge and zero experience. Romance as a whole. The weight of competition. "
    mak "There’s plenty for Miku to be stressed about. But, even if there wasn’t, it could still very well {i}be{/i} that. "
    mak "You never need a reason to be stressed. Some people simply just {i}are.{/i}"
    s "Is there...anything I can do to help with that?"

    scene makotomikupool19
    with dissolve

    mak "Help {i}me?{/i} Or Miku? Which one are we talking about?"
    s "You. "
    mak "Probably. Have you progressed past the point where your go-to solution is to just {i}massage{/i} the stress out of me?"
    s "I think so. I’m a lot different now than I was back then."
    mak "Good. Because, in hindsight, that was very creepy. And if I didn’t spend so much time fantasizing about that exact scenario, I probably would have filed a complaint."
    s "Just tell me what I can do, Makoto. I’m tired of letting you handle all of this on your own and I really do want to be better to you."

    scene makotomikupool20
    with dissolve

    mak "That’s...really sweet, Sensei. "
    mak "Unfortunately, I don’t think there’s much you can do."
    mak "Like I said the other day, this is just...kind of how I exist now. I’m a big, tense bottle of anguish and despair- emptied only by the hand of fate itself. "

    scene makotomikupool21
    with dissolve

    mak "I’ve taken some big steps lately, though. "
    mak "In fact, the vast majority of what I’ve said to you over the last few days has been the result of a lot of hard work and lot of...really difficult conversations."
    mak "My mom and Miku did a lot for me when I was struggling. I know that...But I think Ami and Touka were the ones who helped me more than anyone."
    mak "It was kind of like therapy in a way. Touka allowed me to vent and Ami taught me new ways to cope and helped me better understand the world I’m in now."
    s "Why not...go to actual therapy?"

    scene makotomikupool22
    with dissolve

    mak "I think I might. We have good insurance, so I’d be able to see someone without it being a financial burden. I’ve just always felt weird about things like that."
    s "That’s because you’re like me. You bottle things up until there’s nowhere else to put them."
    mak "How have you managed to go so long without bursting, Sensei? I’m really curious. "
    mak "Between the coping techniques and emotional outbursts, Ami also helped me realize just how hard you were hit when-"

    scene makotomikupool23
    with dissolve

    s "I’ve managed to go so long by doing the exact opposite of what you’ve been doing. And, sorry for interrupting, but I don’t think I’m going to change that just by hearing about your success."
    s "That doesn’t stop me from being happy for you, though."
    mak "What if it’s me?"
    s "What if {i}what{/i} is you?"
    mak "What if you talk to {i}me{/i} about your feelings? I can be your Ami. Or your Touka."
    s "I already have an Ami {i}and{/i} a Touka and I wouldn’t want to talk about this with either of them. "
    mak "I won’t force you, of course. The unending weight of “opening up” is still fresh on my mind after the lot of you barraged me at the height of my misery. "
    mak "In fact, I won’t even tell you that I’ll be here for you if you {i}want{/i} to open up as I’m sure I’ve said that many times in the past...and that it’s already ingrained into your mind. "
    mak "But if you ever start ranting, I won’t stop you."
    mak "And if you ever want me to be more for you than I already am, I will. "
    s "With all due respect, there are at least ten other girls who would say the same exact thing to me right now."
    mak "That might be true."

    scene makotomikupool24
    with dissolve

    mak "But none of them are me. And, all things considered, I think I’m pretty awesome."
    mak "Plus, I know I’ve locked down a special place somewhere in your heart even if you won’t admit it."
    mak "Like it or not, the two of us are in this thing together — and we can empty out each other’s bottles whenever we get full since we’re too stubborn to empty them out ourselves."
    s "Thanks Makoto, but...this is a little bit nicer than you’re supposed to be acting toward me now."
    mak "You’re right. Give me all your lunch money."

    scene makotomikupool25
    with dissolve

    s "That’s more like it. Thank you."
    mak "Whatever you need. And I’m not just saying that as your secretary slash assistant slash friend slash girlfriend slash fuck buddy slash porno clerk. "
    s "Then that leaves..."
    mak "Just Makoto. "

    scene black
    with dissolve2

    mak "And whatever you want me to be next. "

    "The next half hour goes by without much conversation before Makoto has to take off for another “therapy” session with my niece. "
    "Everything she said today, I already knew."
    "But there was something different about the way she said it that makes her feel like a brand new person."
    "And I don’t know what to make her next."
    "But whatever it is, I hope it’s a role that makes her feel like she’s doing a little more than just “existing.”"

    $ renpy.end_replay()
    $ makoto_love += 1
    $ makotopool55 = True
    stop music fadeout 7.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label makotodorm55p1:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Makoto’s door and wait for her to answer. But, based on just how silent it is {i}behind{/i} said door, it’s possible she’s not even home at all."
    "At the very least, Miku’s definitely not here because I don’t think she’s ever been quiet at any point in her life."

    mi "Come in!"

    "Well fuck me, I guess."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I turn the handle and open the door, only to be met by a wave of humid air pushing itself out of the bedroom and into my face."

    scene makotomikubras1
    with dissolve2

    "But I am gifted with a wonderful sight that makes me immediately forget what I was about to complain about."

    mi "Yo!"
    mak "Welcome to nudity."
    s "Am I interrupting something? I knew things were a little too quiet in here, but I didn’t think-"
    mak "Sorry to let you down, but no. You weren’t interrupting anything. Miku and I were just reading."
    s "You really expect me to believe that Miku knows how to read?"

    scene makotomikubras2
    with dissolve

    mi "Tsk, tsk, tsk. I’ll have you know I can read at a fourth grade level, Sensei. Most of the time, at least."
    mak "Why do you look so proud of yourself?"
    s "So...do you two always strip down to your underwear while you read? Or is this some new sort of...ritual for you?"

    scene makotomikubras3
    with dissolve

    mak "Since you apparently can’t tell by how disgusting it is in here, our AC unit is busted and we need to wait for it to get fixed."
    mi "Methinks Makoto broke it herself as an excuse for fanservice. Either way, don’t matter to me! I thrive in the warmth!"
    mak "And {i}I{/i} want to die. But I suppose that’s not really a new development and is only exacerbated by the temperature."
    mi "I don’t mind who or what you exacerbate so long as ya do it under the blanket."
    mak "Help me."
    s "Sure. Shall we resume this conversation under the blanket?"
    mak "As if I’d be able to survive {i}under{/i} the blanket when I’m struggling to get by as-is. One more layer would surely spell my demise."
    s "So...it would be fine if you removed a layer?"
    mak "..."
    mi "Again, ain’t gonna bother me! That ain’t the most flatterin’ underwear anyway, Makoto. Go ahead and take it off so you two crazy kids can exasperate all over each other."

    scene makotomikubras4
    with dissolve

    mak "First, it was “exacerbate.” Which you were already confusing with “masturbate.” But, more importantly than that, how are you going to talk down on {i}my{/i} underwear when you’re wearing {i}that?{/i}"
    mi "Tsk, tsk, tsk. Ya seem to be missin’ the whole point of this get-up, Makoto."
    mak "What is it with you and these “tsk tsk tsks” today? And yes, I am likely missing the point. Unless the point is that normal bras just don’t fit you yet."
    mi "That...is partially true! But the truer thingy I was gettin’ at is that sports bras and lil’ tanktop thingies fit gals with this body type better than anythin’! Ain’t that right, Sensei?"
    s "The only way I can know for sure is by physically examining you."

    scene makotomikubras5
    with dissolve

    mi "As you please."
    mak "..."
    s "I’m not allowed, am I?"
    mak "Correct. You are not allowed."
    s "Sorry, Miku. Maybe next time."

    scene makotomikubras6
    with dissolve

    mi "Fine by me. I was about to leave you two alone anyway. Lots more studyin’ to catch up on since Makoto’s been crackin’ down on me lately."
    mi "But hey, maybe I’ll make it up to fifth grade level by the end of the year! That’d be neat!"
    s "Works for me. Maybe I could even whisk Makoto away or something since she’s apparently dying in here?"

    scene makotomikubras7
    with dissolve

    mak "Whisk me away to where? The underwear store? You know, since you and Miku apparently hate my bra."
    s "Don’t lump me in with her. I think your bra is entirely...adequate."
    mak "Wow, how flattering. "

    scene black
    with dissolve2

    "Makoto and Miku head back to their beds and I follow the “vibe” of the room by making my way over to Makoto’s as well."
    "Now, I know you’re probably wondering what a “vibe” is. And to that, I say..."
    "Same."
    "But I’m pretty sure it means a “feeling” and I’m pretty sure the feeling in here is that I’m supposed to be hanging out with Makoto, so yeah."

    scene makotomikubras8
    with dissolve2

    s "Upon closer inspection, I kind of like your underwear."
    mak "I’m pretty sure you just kind of like my ass."
    s "It’s a good ass."
    mak "What do you want, Sensei?"
    s "I want to hang out with my new best friend, Makoto Miyamura. Who is also known as “The girl I’m going to be worryingly nice to from now on.”"
    mak "Any amount of niceties from you is worrying. Which is why I asked you what you want. But if you’re just here to spend time with me and stare at my butt, I guess that’s fine too."
    s "Do you not want to leave? I was ready to head out for an exciting night on the town with you."

    scene makotomikubras9
    with dissolve

    mak "To be honest, I kind of want to read my book. Which isn’t me directly saying I want you to leave, but..."

    scene makotomikubras10
    with dissolve

    mak "If you {i}just so happened{/i} to leave right now, I wouldn’t be all that torn up inside."
    s "What happened to the Makoto who used to cling to me like Velcro? "
    mak "A lot. Where have you been the last few months? "
    s "Not spending enough time with you apparently. Which is precisely why I will refuse to leave right now so we can make up for lost time. Your book can wait."

    scene makotomikubras11
    with dissolve

    mak "Fine. But only because you’re very rarely this pushy when it comes to me and I think it’s kind of cute to have you doing that instead of pushing {i}back{/i} for once."
    s "I can assure you it’s all part of my master plan to shape you into the perfect bride. "
    mak "Don’t tempt me with a good time, Sensei. Jokes like that don’t always stay jokes forever, you know. You could be unintentionally foreshadowing something right now."
    s "At the same time, not all dialogue has to be foreshadowing- but I suppose we can leave that at that for now."
    mak "What would you like to discuss instead? I think I’m all drama’ed out for the time being. Plus, Miku is right across the room, so we can’t exactly talk about {i}her{/i} again."
    mi "Huh? You two were talkin’ about me? When?"

    scene makotomikubras12
    with dissolve

    mak "Whenever the last time you lied to me was."
    mi "I..."
    mi "I ain’t got any idea what yer talkin’ about, so...I’m just gonna keep on reading."
    s "Subtle."

    scene makotomikubras13
    with dissolve

    mak "For now. I’m keeping an eye out."
    s "Well, since you’re all drama’ed out and Miku is out of the discussion, I guess...you can tell me about your day?"

    scene makotomikubras14
    with dissolve

    mak "Ew. Can you start a little slower if you’re going to be nice from now on? Acting so uncharacteristic right off the bat is throwing me off. "
    s "I’m bad at being casual and friendly and all of my regular conversation topics are either all about me or just way too sexual to maintain without throwing myself on top of you."
    mi "Under the blanket’s okay! Just wanna remind ya!"
    s "Thanks, Miku. Appreciated. "

    scene makotomikubras15
    with dissolve

    mak "Standard small talk it is then, but...how even {i}was{/i} my day? "
    mak "It feels like it kind of ended without anything interesting happening."
    mak "The day itself was fine...I helped Miss Imai reorganize all of the desks after class...Then I helped her clean the locker room....Then I helped her mop the pool room...And I think that was it."
    s "Well here’s hoping you don’t fall for her next, I guess. Having someone else steal away my one and only teacher’s pet sounds like something I don’t want to deal with."
    mak "You’re only saying that because I do all of your work for you."
    s "There are other benefits as well. I just can’t talk about them until we’re underneath the blanket."
    mak "Oh, and there was something with Yumi as well. I completely forgot, but she actually asked me for help with something earlier. Math, I think."
    s "Hey, there’s a conversation topic. What’s going on with you and Yumi?"

    scene makotomikubras16
    with dissolve

    mak "Uhh...nothing? I just helped her with some equation. It’s not like we’re going to the Spring Fling together. Especially on account of spring literally not existing here. "
    s "I’m talking more about how you helped get her suspension revoked. {i}Why?{/i}"
    mak "What do you mean {i}why?{/i} What kind of future-teacher would I be if I just let someone who needs help get kicked out of school? That goes against everything I stand for."
    s "So...it wasn’t just because you wanted to get revenge on Nodoka for-"
    mak "Please do not bring up my embarrassing defeat in the first Dorm Wars. Especially in a way that makes it sound like I would wish bodily harm upon her for just outsmarting me."

    scene makotomikubras17
    with dissolve

    mak "Though, it would be nice if she’d leave me alone in the shower..."
    s "I really wish you guys would invite me in there one day. It’s one of the only places I haven’t gone yet."
    mak "Here’s hoping it remains that way. But anyway, the point is that I just didn’t think it was fair to {i}indefinitely{/i} suspend her. "
    mak "I think that if a student wants to learn, she or he should be given the tools to do so. And Yumi wouldn’t have come back if she didn’t want to. I just made it a little easier for her to do that."
    s "Well, thank you for once again going out of your way to help someone who is both resistant to help and doesn’t deserve it."

    scene makotomikubras18
    with dissolve

    mak "What can I say? That sort of thing is becoming a bit of a specialty to me."
    mak "Why are you taking so much interest in this, though? You seemed pretty indifferent around the time I brought it up."
    s "Yeah, but that’s probably because I was in the middle of trying to reset the world and that it wasn’t something I was entirely conscious for. "

    scene makotomikubras19
    with dissolve

    mak "If you’re quoting something right now, I don’t get the reference. I don’t really watch TV. "
    s "Don’t mind me. Just talking about how the world is part of a never-ending cycle and that we’re doomed to relive this school year over and over and over again for the rest of our lives."
    mak "Again, not getting the reference. But I don’t think I’d mind having you as my teacher for the rest of eternity. "
    mak "And I’m not just saying that because you singlehandedly prevent me from ever having to exacerbate."
    s "Well, I’m glad this relationship is mutually beneficial for the both of us. It’s just one more thing for me to look forward to as my apocalypse counter begins to tick upward."

    scene makotomikubras20
    with dissolve
    stop music fadeout 10.0

    mak "I didn’t realize you believed in that sort of thing, Sensei. Though, just to clarify, you {i}are{/i} talking about the apocalypse in a more biblical sense, correct? Not a natural one?"
    s "Correct. There’s no way a natural phenomenon could possibly explain how-"
    s "Wait...why aren’t you changing the subject?"

    scene makotomikubras21
    with dissolve

    mak "Because...I’m polite? And actually capable of carrying on a normal conversation when the person I’m talking to isn’t busy shoving his hands down my pants?"
    s "No, I just mean that...uhh...{i}extenuating circumstances{/i} prevent anyone else from ever being able to talk about this without immediately changing the topic."
    mak "Sensei, I’m only saying this because I’m allowed to be mean to you now...but what the fuck are you talking about?"
    s "I’m talking about how this shouldn’t be possible with anyone other than Maya and Ayane...and yet here {i}you{/i} are, perfectly navigating the talk as if it’s something you’ve known all along."

    scene makotomikubras22
    with dissolve

    mak "Known {i}what?{/i} Why are you being so weird?"
    s "Because {i}this{/i} is what happens anytime I talk about this with anyone else. Watch."
    s "Miku."

    scene makotomikubras23
    with fade

    mi "Hm? Yeah?"
    s "Every few months, the world starts over and everyone-"

    scene makotomikubras24
    with dissolve

    mi "Oh! Sensei! I forgot to tell ya about this crazy thing that happened at swim practice the other day! Ya have a sec? Or are you still too busy kickin’ it with my best friendo?"
    s "See? She immediately changed the topic."
    mak "This is Miku we’re talking about. She can’t stay focused on anything."
    s "You try then. See what happens."

    scene makotomikubras25
    with dissolve

    mak "Miku, what-"
    mi "Oh! You and me should go bra shoppin’ soon, Makoto! We can get ya somethin’ that looks like it hasn’t been through the wash eight thousand times."
    mak "Shut up and listen to me for a second, okay?"
    mi "Okay! Sure!"
    mak "Sensei thinks that the world is-"
    mi "Oh! You and me should go bra shoppin’ soon, Makoto! We can get ya somethin’ that looks like it hasn’t been through the wash eight thousand times."

    scene makotomikubras26
    with dissolve

    mak "...what?"

    scene makotomikubras27
    with fade

    s "See what I mean?"
    mak "You two are...playing some weird kind of prank on me, right? "
    s "Miku-"
    mi "Oh! Sensei! I forgot to tell ya about this crazy thing that happened at swim practice the other day! Ya have a sec? Or are you still too busy kickin’ it with my best friendo?"
    mak "I-"
    mi "Oh! You and me should go bra shoppin’ soon, Makoto! We can get ya somethin’ that looks like it hasn’t been through the wash eight thousand times."

    scene makotomikubras28
    with dissolve

    mak "I don’t get it...why won’t she let us get our thoughts out?"
    s "I don’t get it either. But it’s not just her. It’s everyone except you and the two girls I mentioned earlier."
    s "And, for a brief moment in time, Yumi and Tsuneyo as well."
    s "The reason I don’t remember you bringing up whatever it was you did to get Yumi back into school is because {i}I{/i} was never there for it. "
    mak "You were, though. I saw you. We...We talked and everything."
    s "Then why don’t I remember any of it?"

    scene makotomikubras29
    with dissolve

    mak "Because...your memories are bad. They’ve been bad every single year since we’ve started-"

    scene makotomikubras30
    with dissolve

    mak "But...wait...I’m a freshman...how have we..."
    mak "Am I just..."
    mak "..."
    mak "{i}What?{/i}"
    s "..."

    scene black
    with dissolve2

    s "I have to make a phone call."
    s "You might want to get dressed."

    $ renpy.end_replay()
    $ makotodorm55p1 = True
    $ makoto_love += 1
    "........."
    "......"
    "..."

    jump makotodorm55p2

label makotodorm55p2:
    scene unexpectedporntrip1
    with dissolve2
    play music "citylife.mp3"

    ay "..."
    mak "..."
    m "There better be a damn good explanation for this."

    "Needing somewhere private to discuss things that isn’t on the complete opposite side of town (IE: my apartment), I wind up summoning the Apocalypse Squad to the local porn shop."
    "Could we have found somewhere better? Probably. But I figured it would be nice to bring Makoto somewhere comfortable so she isn’t too taken aback by all she’s about to hear."
    "And there are few things that make her more comfortable than a building full of rubber penises and fake vaginas that also happens to be her childhood home."

    s "There {i}is{/i} a good explanation for this, I swear. And no, before you go assuming things, it isn’t sexual."
    m "Great, thanks for clearing that up. Call me a pervert, but meandering through aisles of lubricant and ball-gags gave me a different idea."
    s "I mean, it {i}can{/i} be sexual if you want. If that’s the case, we can take a short break before getting down to the real reason I asked the two of you to come here."
    m "Out with it."

    scene unexpectedporntrip2
    with dissolve
    play sound "zipper.mp3"

    s "If you insist."
    m "You know what I meant, you pathetic waste of a human."

    play sound "zipper.mp3"
    scene unexpectedporntrip1
    with dissolve

    s "Well, you don’t have to be rude about it."
    ay "You know, I’m all for a good movie night every once in a while. But I’m not really sure how I feel about this choice of film. Or why we have to do it here when there’s a much bigger TV at my house."
    s "We have to do this {i}here{/i} because I encountered something very unexpected just a short while ago."
    m "Please keep your new fetishes to yourself. Thank you."
    mak "I..."
    mak "Is it true that...you three, like...uhh...how do I even put this?"
    s "Makoto knows about the resets."

    scene unexpectedporntrip3
    with dissolve

    m "Makoto knows {i}what?{/i} How? This loop’s barely just begun. "
    s "Well, to say she knows about the resets isn’t exactly accurate. She just...wasn’t changing the topic whenever I brought them up, so I figured I’d call the two of you right away to prove it."
    ay "You’re not pregnant, are you? Asking for Maya’s sake."
    mak "Uhh...no?"
    ay "Okay. I figured. I just thought I’d make sure. Again, for Maya’s sake."
    m "What do you know? What did he tell you so far?"

    scene unexpectedporntrip4
    with dissolve

    mak "Not much...Miku just started repeating the same thing over and over again and...before I knew it, we were here. I’ve got absolutely no idea what any of this is about."
    m "What do you mean “repeating the same thing over and over again?”"
    mak "Whenever Sensei brought up the...time stuff."
    s "Makoto tried too. But it was like Miku got stuck in some sort of...interjection loop. Not to be confused with the loops {i}we’re{/i} stuck in."

    scene unexpectedporntrip5
    with dissolve

    mak "It’s not true, is it? Sensei’s very likely just...misunderstanding something, isn’t he? It’s entirely impossible for humans to move through time like you’re suggesting. "
    mak "And the idea of a repeating timeline is just-"
    m "It’s true. Though, I have absolutely no clue whatsoever about why you’re suddenly exempt from the same rules that keep everyone else confined to blissful ignorance."
    m "But, yet again, I couldn’t come up with a reason why Yumi and Tsuneyo were exempt last time, so...back to the drawing board, I guess."
    ay "Huh...yeah...drawing any similarities between the three of them seems almost impossible. Each one of them is wildly different from one another."

    scene unexpectedporntrip6
    with dissolve

    mak "Can one of you two {i}please{/i} explain in better terms what’s going on? Is something wrong with Miku? Is something wrong with {i}me?{/i}"

    scene unexpectedporntrip7
    with fade

    m "To say anything is wrong with {i}anyone{/i} isn’t entirely accurate as I believe there is a problem with the world itself."
    m "Every several months, before the school year comes to an end, the four of us, as well as everyone else we know, are sent back to an earlier part of the year in which everything starts anew."
    m "Except it technically {i}isn’t{/i} an earlier part of the year. We just {i}think{/i} it is while our city manages to move through time normally. "
    m "The seasons still change and the tangible developments in the environment still...well, develop."
    m "Until recently, I was the only one whose memories carried over from loop to loop. But changes made to the formula of this for unknown reasons have now landed both Ayane and Sensei beside me."
    m "I take it you’ve already realized by now how suspicious it is that what should be a single school year is packed with years' worth of memories, yes?"
    mak "Y-"
    m "The reason for that is, {i}I think,{/i} because of Sensei. "
    m "He seems to be the anchor for everyone and the fact that his mind isn’t being reset along with the world means the rest of {i}your{/i} memories are carrying over as well."
    m "It’s a phenomenon I’ve never encountered to this extent before and I imagine it’s only a matter of time until more people like yourself start catching onto this."
    mak "I...what? Huh? But none of that makes any sense."
    ay "Just wait until she gets to the part about everyone turning invisible and how we all have to hug on top of the roof to make things go back to normal."

    scene unexpectedporntrip8
    with fade

    mak "Okay. That’s enough. The joke’s over. I don’t get why all three of you decided to mess with me like this, but it’s gone way too far."
    s "I know how it sounds, but it’s not a joke. "
    s "The only thing we can do now is dress you up like a shrine maiden and hope for the best."

    scene unexpectedporntrip9
    with dissolve

    mak "You’re not helping!"
    ay "Makoto, as the newest member of our time travel club that is tentatively named the “Rooftop Apocalypse Squad” I know {i}exactly{/i} how confusing this all sounds."

    scene unexpectedporntrip10
    with dissolve

    ay "In fact, parts of it {i}still{/i} feel like a dream to me sometimes. But after seeing it with my own eyes, I can promise you it’s not a joke."
    mak "Why would I believe you, though? We’re not close or anything. And you’re so obsessed with Sensei that you’d probably just go along with whatever he says anyway."
    s "Do you really think {i}I{/i} would go through with plotting out an extremely elaborate plan just to play a prank on you? I complain when I have to sign my name. This would be way too much effort for me."
    mak "You’ve toyed with me plenty of times in the past. I wouldn’t put it past you to do something like that again. "

    scene unexpectedporntrip11
    with fade

    m "If you don’t believe us, why not try speaking about this to any of the other girls? Worst case scenario is you just get ignored again. Best case, we find more people like you {i}and{/i} settle your doubts."
    m "I’ve got nothing to lose either way."

    scene unexpectedporntrip12
    with dissolve

    ay "Maya, be a little more sensitive. This is clearly really scary and weird for Makoto."
    m "It’s weird for {i}all{/i} of us. It was weird enough when {i}you{/i} wound up on the roof, but for Makoto of all people to get sucked into this as well is all sorts of confusing. "
    mak "What do you mean “of all people?” How am I supposed to take that?"
    m "Beats me. Take it however you want. I’m still trying to wrap my head around this."
    s "What should we do now? Weren’t we looking for some sort of way to test more reset-centered info? I did my part. It’s your turn now."

    scene unexpectedporntrip13
    with dissolve

    ay "Guys, stop treating Makoto like she’s some sort of experiment. Like yeah, this might help us find out some stuff, but she’s still a normal girl at the end of the day. It’s not like she {i}wanted{/i} this."
    m "I’ll care a little more about her “totally real” feelings if she winds up making it to the roof. For now, she’s just one more enigma."
    ay "You mean like how you started caring about {i}my{/i} feelings once I made it to the roof? You sure you don’t wanna ask Makoto to abstain from having sex with Sensei for the entirety of this loop too?"

    scene unexpectedporntrip14
    with dissolve

    mak "W...What?! Sensei and I don’t-"
    ay "Oh, come on Makoto. You don’t have to hide it. We already know."
    ay "Sensei even has you shoving a dildo into your mouth as his wallpaper."

    scene unexpectedporntrip15
    with dissolve

    mak "{i}You said you would delete that!{/i}"
    s "I say a lot of things."
    m "Maybe you could use a sex toy or five as well if you’re going to be all grumpy like this."
    ay "Well sorry for not having a trillion years to come to terms with the fact that the man I’m in love with is also sleeping with everyone else. No offense, Makoto."

    scene unexpectedporntrip16
    with dissolve

    mak "Oh...uhh...none taken?"
    mak "Then...I guess this means the two of you are also-"
    ay "I am. Maya’s too afraid to let Sensei dick her down because she thinks it’ll make his brain ooze out of his ears."
    mak "That’s...{i}some{/i} confidence you’ve got there."
    m "While I {i}am{/i} certainly confident, I can assure you that has little to do with it. It is for {i}everyone’s{/i} best interest that I do not sleep with Sensei."
    m "It is also important to note that if I {i}did{/i} sleep with Sensei and he did {i}not{/i} die from it, that he’d no longer want to sleep with either of you ever again. The end."
    s "I like this side of you."
    mak "I don’t. Apart from that outburst when Noriko came to class, you’ve always seemed rather...reserved."
    m "That is because my time is better spent on attempting to understand this world. Which, should things go according to plan, may come to involve {i}you{/i} in some way."
    m "And I say that with full knowledge that things rarely ever go according to plan."

    scene unexpectedporntrip17
    with dissolve

    mak "What {i}is{/i} this plan, though? How am I supposed to just carry on with my daily life knowing that I’m doomed to repeat the same school year for the rest of forever? "
    mak "What’s the sense in applying myself if I know there’s no purpose to it?"
    ay "Maybe just...don’t apply yourself then? "
    ay "It’s hard to give you directions when we don’t know if you’re going to remember any of this come the next cycle, but maybe just...hang out on the DL for now? "
    ay "Have fun and slack off. Shove some more dildos in your mouth. It’s not like there’s a time limit. The world is your sandbox."
    ay "But also know that things might turn really horrible and really scary at any given moment. If they do and you find yourself in a situation like that, come to the rooftop as quickly as possible. "
    mak "Why...the rooftop? What’s so special about that place?"
    m "Probably just a denpa trope. Either way, that’s where you’ll want to be."
    m "Do you have any more questions for now?"
    mak "Yes. Roughly one thousand of them."
    m "Oh."
    m "Well, that’s too many."

    scene black
    with dissolve2

    m "But you can take down my number and text several of them to me. I’d much prefer to not spend a second longer in this room when it is evident the two of you have used it for countless sexual excursions."
    s "Oh, come on. It hasn’t been {i}that{/i} many..."

    "Maya and Makoto exchange contact information before the two senior female members of the Apocalypse Squad head back to the dorms."
    "And while I’m hesitant to add Makoto to the roster before she even makes it there (If she {i}does{/i} make it there) I can’t help but acknowledge the possibility."
    "I’m not sure what, but there must be {i}something{/i} I can do to make sure she doesn’t suffer the same fate as Yumi and Tsuneyo."
    "Makoto deserves to hang onto her memories just as much as the two of them did...and if there’s anything I can do to strengthen her grasp on them, I’ll do it."

    scene unexpectedporntrip18
    with dissolve2

    s "So, how do you feel knowing that this world is something out of a sci-fi novel? Excited?"
    mak "Well, to start, my head hurts. And I’m still half-expecting to wake up from this weird dream at any given moment."
    s "I can pinch you if you want?"

    scene unexpectedporntrip19
    with dissolve

    mak "Hah...no. I know this is real. {i}Somehow.{/i}"
    mak "It makes literally zero sense and goes against basically everything I have ever read, but there’s some sort of merit to it, if not only for the fact that things aren’t always entirely as they seem."

    scene unexpectedporntrip20
    with dissolve

    mak "And weirdly enough, I think this actually...{i}helps{/i} explain certain things. I don’t know. I still have to try and wrap my head around it."
    mak "All things considered, it kind of works out in the long run. I’ve been wanting a more important role in your life lately and this prevents me from having to assertively seize one."
    s "I’m not really sure how you’d do that in the first place."

    scene unexpectedporntrip21
    with dissolve

    mak "You would be if you paid more attention to things I handed you."
    s "What?"
    mak "What?"
    s "What does that mean?"
    mak "What does {i}what{/i} mean?"
    s "When was the last time you-"

    play sound "static.mp3"
    scene unbluejay8sepia
    with flash
    stop sound

    mak "Here! Sign this one!"

    play sound "static.mp3"
    scene unexpectedporntrip22
    with flash
    stop sound

    s "You didn’t..."
    mak "Didn’t what? Trick you into signing a marriage license by weaving it in with a bunch of tests? Do you really think {i}I{/i} would do something like that?"
    mak "I'm Makoto! {i}I'm{/i} the good one!"
    s "Would the old Makoto do that? No. Of course not. But the {i}new{/i} Makoto? Who has nothing to lose and little direction? I’m not so sure."

    scene unexpectedporntrip23
    with dissolve

    mak "Would marrying me really be {i}so{/i} bad? I mean, we’re basically married already with how much time we spend together. "
    s "I’m going to burn down your room."
    mak "Who says it’s in my room?"
    s "Makoto-"

    scene unexpectedporntrip22
    with dissolve

    mak "Heheh! It’s fun having something to lord over you! Is this how you’ve felt the entire time you’ve kept that ridiculous photo of me as your wallpaper?"
    s "There is no way you could even turn something like that in without me present. I don’t believe it."

    scene unexpectedporntrip24
    with dissolve

    mak "Kumon-mi’s regulations regarding marriage became extremely lax during the second year of the space war. All I need is a signature that, honestly, I could have forged. Just like you suggested the other day."
    s "That was about {i}essays.{/i} Not marriage licenses. I don’t want to marry you."
    mak "I know that. Which is why I’m not going to turn in the document. I’m just going to hold it over your head so that you’re {i}forced{/i} to be nicer to me. Ha-ha."
    s "But I’ve...actually {i}been{/i} nice lately. I haven’t done anything wrong."
    mak "Then you’ve got nothing to worry about."

    scene unexpectedporntrip25
    with dissolve

    mak "{i}Me{/i} on the other hand? I don’t even know where to start with this."
    mak "Maybe Ayane is right? Maybe I should just take this...{i}cycle{/i} easy? "
    mak "Knowing the world isn’t going anywhere definitely takes a load off of my mind. And with how stressed I’ve been lately, a bit of relaxation sounds amazing."

    scene unexpectedporntrip26
    with dissolve

    mak "The only question is {i}how{/i} I should relax..."
    s "..."
    mak "..."
    s "I know that look."
    mak "Do you?"
    s "I do. Or at least I {i}hope{/i} I do."
    mak "Did Ayane really have to spend an entire school year abstinent? That sounds horrible."
    s "Maya figured she somehow got roped into this by getting pregnant."
    mak "You came inside her?"
    s "Quite frequently."
    mak "I see."
    mak "Do you wanna cum inside {i}me?{/i}"
    s "..."
    mak "..."

    scene unexpectedporntrip27
    with dissolve

    mak "Wait, just to be sure, if I {i}do{/i} get pregnant, it won’t carry on into the next timeline or whatever, will it?"
    s "While I don’t have a {i}definitive{/i} answer to that, I can tell you that I’ve ejaculated inside many girls over the last few school years and still remain child-less.  "

    scene unexpectedporntrip28
    with dissolve

    mak "Wanna make it one more?"
    s "You’re suddenly taking this {i}way{/i} better than you were an hour ago..."
    mak "I suddenly have nothing to lose and a {i}pretty{/i} good idea of how I want to spend my vacation away from reality. "

    scene black
    with dissolve2

    s "And I’m suddenly reminded of how thankful I am for a world like this in the first place..."

    $ renpy.end_replay()
    $ makotodorm55p2 = True
    $ makoto_love += 1
    $ makoto_lust += 1
    stop music fadeout 7.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label sportswars19:
    play sound "static.mp3"
    scene nodokontest1 with flash
    stop sound
    play music "pianomelancholy3.mp3"

    m "Is that...hah...the best you’ve got?! "
    s "No...but it’s what you deserve. "
    m "You’re...pathetic! I can...ngh...barely feel anything!"
    s "Are you lying to me?"

    scene nodokontest2
    with dissolve

    m "Me?...Lying to {i}you?...{/i}Don’t make me laugh..."
    m "You’re the one...ah...who ghosts me for...months! And you don’t...even have the balls...to tell me why!"
    m "Plus...you’re...hah! You’re...taking advantage of...a high school girl...still in her uniform! Have you...no decency?! You fucking...hah...lecher! "
    s "Oh, please. You practically begged me for this."
    m "That changes...nothing! You’re still...fucking disgusting!"

    scene nodokontest3
    with dissolve

    m "Hah! Hah!"
    s "Say it again."
    m "You’re...ah! You’re fucking...disgusting! You...pathetic husk of a man! Just...look at how...irredeemable you are!"
    s "Are you gonna cum?"
    m "Hah...no! I’m not...ah...I’m not even-"

    scene nodokontest4
    with dissolve

    m "Hah?! What?! Why?!"
    s "Why should I be the only one who has to suffer?"

    scene nodokontest5
    with dissolve

    m "Oh-hoh? Look at you — a big, strong man trying to play it cool when we {i}both{/i} know all he really wants is to bury his big dick inside of a little-"

    scene nodokontest6
    with hpunch

    m "HAH! FUCK! OH...FUCK!"
    s "I’m kicking you out of here the second you cum. You know that, right?"
    m "I...know nothing! And...fuck you! I’ll stay here...as long as I want! Harder! Harder!"
    s "Harder?"

    scene nodokontest7
    with dissolve

    m "What’s the matter?...Are you deaf?..."
    m "You know how I like it, Sensei...you know how...rough I’ll let you get!"
    s "Tell me you love me."
    m "Mmmmmm.......no~"
    m "I want to watch you {i}squirm.{/i}"

    scene nodokontest8
    with dissolve

    s "Then I guess I’ll stop giving you what {i}you{/i} want as well."
    m "God! Can you stop fucking doing that?! You’re driving me mad!"
    s "No. And fuck you."

    scene nodokontest9
    with dissolve

    m "{i}Yeah.{/i} Fuck me. {i}Do it.{/i} You won’t. You fucking pussy. I bet you’re just afraid that you’ll cum in five seconds after going so long without feeling my-"

    scene nodokontest10
    with hpunch

    m "{i}Aaaah!{/i}"
    s "Say it."
    m "Go down on me...right now...I need it..."
    s "Why should I do what you say when you won’t listen to {i}me{/i} at all?"
    m "Because...I’m your special little girl...and I’ll call the police and tell them you raped me if you don’t..."
    s "Maybe you should."
    m "Hah...yeah...probably! "

    scene nodokontest11
    with dissolve

    m "But then...ahh...I’ll have to...find someone else to fuck me...and that’s just...hahhh...too much work!"
    s "You love me, don’t you?"
    m "Is now really the time to-"

    scene nodokontest12
    with dissolve

    m "AAAAaaaAAAaah!!!!! Right there! Right there! Just like that! Just like-"

    scene nodokontest13
    with dissolve

    m "{i}Ahh...{/i}"
    m "Sensei...you’re seriously driving me insane..."

    scene black
    with dissolve2

    s "You don’t even {i}know{/i} what you’re doing to me."
    m "Haha...hah...I can...only imagine!"
    s "Yeah."
    s "You can."

    stop music
    play sound "static.mp3"
    scene nodokontest14 with flash
    stop sound
    play music "citylife.mp3"

    no "Well, girls — we’ve made it to the grand finale. And I couldn’t have chosen two better people to join me here. "
    mak "You most assuredly could have. Which isn’t a jab at Molly, of course. I’m sure she’s...plenty capable of whatever sort of wish-fulfillment scenario you’ve cooked up for round three."

    scene nodokontest15
    with dissolve

    no "But is she more capable than {i}you?{/i} A girl who has not only grown up around sex, but has experienced it firsthand on a {i}multitude{/i} of occasions. Is that correct?"
    mak "Ask me that question again in a few months after I figure out what memories do and don’t carry over."
    mo "Curious. The Kendo Princess has been having concerning thoughts regarding {i}her{/i} memory as well. By any chance, have you gone to an amusement park with a female love interest lately?"
    mak "I...can not say that I have."
    no "Would you like to? Perhaps the two of us can leave this place together and do a bit of {i}exploring{/i} on our own?"
    mak "Just get on with the contest, Nodoka. I have no interest in flirting with you or anyone else here."
    mo "I too would like to usher in the beginning of our fateful encounter right now, but it is almost certainly due to the fact that I can’t really contain myself for much longer."

    scene nodokontest16
    with dissolve

    no "Fortunately for all of us, you won’t {i}have{/i} to. For this final competition will not only give you the opportunity to satisfy certain {i}urges,{/i} but provide a chance for you to prove your {i}worth{/i} as well."
    mo "My...worth?"
    no "That is correct, Molly."
    mo "Okay, but...what does that mean?"

    scene nodokontest17
    with fade

    mak "I would assume it has something to do with that table full of dildos illuminated by a spotlight."
    mo "Yeah, that would make sense."
    n "Knowing Nodoka, that could have just been some sort of art display."
    no "And an art display it is. But it’s an art display our contestants will be utilizing for this third and final competition, which I have dubbed “The Pit of Despair.”"
    mak "The what now?"
    mo "Excellent name, Nodoka! But, may I recommend several other adjectives that may be tacked on to emphasize the greatness of such a-"
    no "You may not, for the challenge is modeled after Harry Harlow’s device created for the purpose of emulating depression in rhesus macaque monkeys."
    mak "You know, I thought I knew where this competition was going, but I’m not quite sure anymore."

    scene nodokontest15
    with fade

    no "Meaning?"
    mak "Meaning I have a hard time grasping what a table full of sex toys has to do with monkeys and depression."
    r "Yeah, I’m with Makoto on this. But I’ve also never understood anything Nodoka has said at any point, so this is nothing new to me."
    no "The relation matters not. What matters is the {i}task.{/i}"

    scene nodokontest14
    with dissolve

    no "The two of you will be competing in a contest to see who can {i}handle{/i} the most, if you understand what I’m saying."

    scene nodokontest18
    with dissolve

    mak "Yup. There it is."
    mo "H...Handle?"
    mak "What else would it have been?"
    mo "As in...we take those...and...see how much of them we can fit into our-"
    no "Mouths."

    scene nodokontest19
    with dissolve

    mo "Oh."
    mak "Wait, really?"
    no "Did you think I’d make you do something more {i}drastic?{/i}"
    mak "Well, considering the last two girls rode sex machines and you said the contests would be of “increasing intensity,” yeah. I kind of did."
    no "Well, you aren’t entirely mistaken as there will be an additional vaginal penetration round subsequently following the deep-throating portion. "
    no "This round, however, will be entirely optional and wholly dependent on the first round."
    ki "Booooo! Make them ride the dildos!"

    scene nodokontest20
    with dissolve

    no "Only if necessary, Kirin."
    no "You see, if both girls manage to fit all three toys into their mouths and there is no clear gap in skill between them, a tie-breaker will be necessary."
    no "However, if there is one clear winner, the competition will come to an end and a winner will be crowned. "
    no "That is, unless one of the two contestants calls for the second round to commence regardless, as vaginal insertion is worth more points and would allow for the mounting of some sort of comeback."
    mo "Mounting..."

    scene nodokontest21
    with dissolve

    mak "So basically, the first round of this contest doesn’t matter at all because the second one will trigger as soon as Molly wants it to."
    no "{i}If{/i} she wants it to. Or if there is a tie."
    mo "Mounting..."
    mak "She very clearly wants a second round."
    no "Then I suppose your initial expectation from gazing into the Pit of Despair was correct after all. "
    no "Now then, shall we begin?"

    if makoto_lust > 54:
        jump makotovsmolly
    else:
        scene nodokontest22
        with dissolve

        mak "No thanks. I’m bowing out."
        no "Bowing out?"
        mo "Bowing out?!"
        mak "Correct. You can just crown Molly as the winner. Because, even if I’ve got nothing to lose anymore, I can’t say I find the idea of riding a sex toy in front of a bunch of people I’m not sexually attracted to very {i}fun.{/i}"
        mo "It’s not about fun! It’s about proving who we are as people! It’s about determining our willpower! It’s about cementing ourselves as legends in books of history all across the world!"
        mak "And I would simply prefer to not have the time I competed in a sex contest in history books. It’s that simple."
        no "Curious. This is not how I expected things to unfold at all."

        scene nodokontest23
        with dissolve

        mak "Well, I’m sorry to disappoint you. "
        mo "So...I just don’t get to compete against anyone? I just have to be horny and alone? But I’m always horny and alone. This isn’t new or exciting at all."

        scene nodokontest24
        with dissolve

        no "Perhaps a consolation ride on Irene would cheer you up?"
        mo "Fine...but it’s not the same if it’s just me."
        no "Don’t fear. We’ll all be there to watch, Molly. "
        mak "Not me. Seems like Nodokathon has already come to an end. And we need to get up early for the Dorm Wars closing ceremony tomorrow morning."

        scene nodokontest25
        with fade

        n "I think Kirin and I will probably bounce too if the contest is over. I’m kind of hungry."
        ki "Sorry, Molly. Film it and send it to me?"
        r "Sana and I were going to get food too. Right, Sana?"
        sa "Uh...um...yeah..."
        mo "Why am I constantly being betrayed?!"
        no "Don’t worry, Molly. I’ll stay with you and watch. "

        scene black
        with dissolve2
        stop music fadeout 15.0

        mo "It’s weird if it’s just you! "
        mak "It’s weird regardless. But yeah, I know what you mean."
        no "Alas...for now {i}I{/i} am the one who is betrayed."
        n "Well, then! Looks like it’s time to get dressed and clean this place up before going out to a buffet!"
        ki "It’s like midnight. Are there even any buffets open right now?"
        r "I’m sure we’ll find one! Come on, Sana!"
        sa "Huh?! Wha- oh! Coming!"
        n "Guys, wait! I’m still in my underwear!"

        $ mollynodowin = True

        "And so {i}another{/i} war comes to an end — one that you’d much rather have been there for than its predecessor."
        "But again, you were hopelessly flailing behind the eyes of gods, just ever-so-slightly out of reach and ever-so-slightly out of touch with the truth."
        "But that’s fine, for your night was one to remember."

        $ renpy.end_replay()
        $ sportswars19 = True

        jump sportswars20

label makotovsmolly:
    scene black
    with dissolve2

    mak "I guess. There’s no sense in delaying the inevitable at this point. The only thing that’s left to decide now is-"
    mo "I volunteer as tribute! I will go first!"
    mak "Well, that decides that."

    scene nodokontest26
    with dissolve2

    no "If this weren’t such a clear-cut competition, I’d feel inclined to provide several bonus points here. Your anticipation and excitement are palpable, {i}Emerald Guardian.{/i}"
    mak "Did you get {i}that{/i} secondhand too? Because that one’s expensive. I’m familiar with the model."
    no "Oh, no. That one’s from my {i}personal{/i} collection."

    scene nodokontest27
    with dissolve

    mak "Your...{i}personal-{/i}"
    no "Good luck, Molly. Show the world what you’re made of."
    mo "I’m pretty sure I can handle this. It’s about the same size as my regular one. "
    ki "Make sure to make lots of really cute noises and expressions!"

    scene nodokontest28
    with dissolve

    mak "Molly, I probably wouldn’t-"

    scene nodokontest29
    with dissolve

    mo "Mm~"
    mak "...do that."
    no "Aww...just look at how adorable she is with a demon penis in her mouth. It’s as if we’re mere spectators filming her in her natural habitat."
    mak "Please tell me that was thoroughly sanitized. And that there is a separate one waiting for me that has never been a part of your “personal collection.”"
    no "I’ll happily tell you both of those things. Unfortunately, that does not make either one of them true."

    scene nodokontest30
    with dissolve

    mo "Mmph!"
    no "Ah! Very well done, Molly. You must have lots of practice. "

    scene nodokontest31
    with dissolve

    mo "What can I say? I’ve been training for years and years and years. "
    mak "You’ve barely been alive for {i}years and years and years.{/i}"
    no "Are you ready for the second challenge, Molly? I can assure you this one will be harder."

    scene nodokontest32
    with dissolve

    mo "I beat Spine of Deathwing on heroic! There’s no challenge too hard for me! "
    no "We’ll see about that."
    mak "Nodoka...can I ask you something?"
    no "Of course, my love."
    mak "I am not your love. But, like...I guess I just want to know {i}why{/i} you’ve decided to do this? "
    mak "Like, is it really all for just...personal pleasure? Or do you get a rise out of pretending to be some sort of...sex choreographer or...orgy organizer or something like that?"

    scene nodokontest33
    with dissolve

    no "This may come as a surprise to you, but nothing I do is self-motivated. "
    no "Sure, I do like to satisfy my own curiosity from time to time. But even then, the motivation is more {i}discovery{/i} than anything else."
    no "I simply believe that we’re all just pieces moving around on a timeline. And, while most are satisfied with existing that way, I care more about discerning that timeline than reaching its end."
    no "And there is no better way to confuse time itself than to do things it doesn’t expect. Which is one of several reasons I always need to be ten steps ahead."

    scene nodokontest34
    with dissolve

    mak "Apologies, but I’m not sure if I follow. What are you trying to accomplish by “confusing time?” What does that mean?"
    no "It means that, to borrow the words of David Lynch, this whole world is wild at heart and weird on top. "
    no "And, when one’s perception is factored into the mix, it makes discerning what you’re even looking {i}at{/i} nigh impossible."
    no "As a scholar, it is my duty to understand. But the problem is that this world we live in is {i}impossible{/i} to fully understand. There’s too much happening that doesn’t make sense."
    no "Which is why I’ve decided to make my own world instead. Because, if you can not {i}grasp{/i} reality, which no one can, all you {i}really{/i} have to do is {i}distort{/i} it."
    no "That way, you can fit it into the palms of your hands. You can bend it and mold it into whatever you want it to be and wind up with something different than what you were given."
    no "You can peel away that weird layer on top, replace it with heart or sex or anything else you find mysterious so long as you wind up with a product that’s interesting- before making {i}yourself{/i} the core."
    no "But again, I’m not doing it for me. I’m doing it for everyone else. "
    no "And the best way for me to create a world worth living in is to mutilate the one we have beyond recognition."
    no "That’s what I mean by “confusing time itself.” I mean refuting nature and science and God and everything in between until they give up on me entirely."
    no "Only then will I be free. "
    no "And only then will the words of my mother make sense to me."

    scene nodokontest35
    with dissolve

    mak "Your mother?"
    no "It’s okay to give up, Molly. It’s possible you’ve already done better than Makoto can."
    mo "Mm!"

    scene nodokontest36
    with dissolve

    mo "Blasted {i}tentacle.{/i} After all the times we’ve shared on the Internet, you {i}too{/i} betray me."
    mo "Is there nothing sacred in this world?"
    no "Makoto, please follow suit and continue the competition. I’ve left a bottle of soap beside the {i}art{/i} table for you to sanitize the equipment should you feel uncomfortable with its current state."

    scene nodokontest37
    with dissolve

    mak "Say no more. I’ll make this quick."
    mo "{i}Hah...{/i}I am a failure as a pervert. I wouldn’t last five minutes in an edgy hentai series."
    no "You did your best, and that’s really all that matters."

    scene nodokontest38
    with dissolve

    mo "Tell that to the tentacle monster that would drag me up into a tree before violating me and dropping me back down to the ground to be {i}further{/i} violated by a tribe of wandering orcs."

    scene nodokontest39
    with dissolve

    no "Do go on. That sounds rather captivating."
    mo "Then, after the orcs arrive and have their way with me, I’d be sold into slavery and-"

    scene nodokontest40
    with dissolve

    mak "Mm!"
    mo "Wha...already? I didn’t even notice you started yet."
    no "I expected no less from the amazing Makoto Miyamura. But can she conquer what Molly could not?"

    scene nodokontest41
    with dissolve

    mo "A-Anyway! It doesn’t matter what would happen to me after the tentacles and orcs and slavery! The point is that I’d be in for a very rough time and only someone like Sana would be able to enjoy it!"

    scene nodokontest42
    with dissolve

    no "Are you sure it would {i}only{/i} be Sana? Because I’m quite the fan of {i}darker{/i} scenarios as well. And I’m hard pressed to believe you’re {i}not{/i} with such an...active imagination. Cliche as it may be."
    mo "Perhaps I used to be and have simply gone through some sort of metamorphosis that’s changed me to some degree?"
    no "Oh?"

    scene nodokontest43
    with dissolve

    mo "Or perhaps I’ve just been misread! For, as I am clearly enough of a degenerate to attend Nodokathon, I am still greatly inexperienced and-"

    scene nodokontest44
    with dissolve

    mak "Mm!"
    mo "Wha-"
    mo "Is that...is that the tentacle?! Did you fit that entire thing in there?!"
    mak "Mm. "
    no "My, oh my. It appears that round one goes to Makoto. But will there be a round two?"
    ki "Holy shit. Is Makoto actually {i}cool?{/i}"
    n "Does the amount of penis someone can fit into their mouth directly influence how cool they are?"
    ki "I mean, how else would that be decided?"

    scene nodokontest45
    with dissolve

    mo "I enact my birthright as the eldest daughter of the Tenderheart tribe to force a new trial! Winner takes all!"
    mak "Mm-mm?"
    sa "So...so does this mean-"
    r "I’m pretty sure they’re going to...use those for their actual intended purposes now."

    scene nodokontest46
    with dissolve

    ki "Woo-hoo! Let’s watch our friends stuff themselves with weird, rubber cocks!"
    n "And ultimately find out how cool they are because that’s how you measure the value of a person! Woo!"

    scene black
    with dissolve

    ki "You know, all this passive aggressiveness is really killing my girl boner."
    n "Was it not already killed when you rode a sex machine to completion in front of us half an hour ago?"

    scene nodokontest47
    with dissolve2

    ki "No, Noriko. It was not. And if no one is using the black dildo, I’d like to use it to {i}regain{/i} my girl boner now that you have slaughtered it."
    n "There is no way that thing would fit inside of you. It’s like a foot long."
    mo "But it will fit inside of {i}me...{/i}"

    scene nodokontest48
    with dissolve

    mak "Excuse me."

    scene nodokontest49
    with dissolve

    mo "This is the moment I have trained my entire life for."
    r "Really? {i}This{/i} moment? Choosing a dildo off of a table like it’s a starter Pokemon?"

    scene nodokontest50
    with fade

    ki "Which Pokemon would you most want to-"
    r "Gardevoir."
    n "Lucario."

    scene nodokontest51
    with dissolve

    ki "You really are a furry, huh?"
    n "Oh come on, what’s yours?"
    ki "Obviously Vaporeon. It’s the ideal Pokemon for breeding purposes."
    n "But you do not have a penis with which to do the breeding."
    sa "I’d...um..."
    sa "Probably..."
    sa "Machamp..."

    scene nodokontest52
    with dissolve

    n "Jesus, Sana."
    ki "How would you even-"
    mo "Silence, mortals! For the time has come for Molly MacCormack to claim her status as the main heroine and insert the...large...black...dildo..."
    mo "Uhh..."
    mak "Just go in order, Molly. You don’t want to damage your insides this early on in life."

    scene black
    with dissolve2

    mo "R...Right! But only...to get myself warmed up! No one goes from zero to hero just like that!"
    n "Kirin did."
    ki "She’s not lying."
    no "There’s a bottle of lubricant beneath the table, Molly. Makoto is right. Please don’t damage your insides for the sake of the competition."
    mo "Just...have to..."
    mo "Okay!"

    scene nodokontest53
    with dissolve2

    mo "I can do this! It’s just a toy! I have one just like it! It makes no difference that all my friends are watching me!"
    mo "Just...have to..."

    scene nodokontest54
    with dissolve

    mo "Ngah..."
    ki "Is it in yet? I can’t see? Rin, move over."
    r "D-Don’t touch me right now! I am way too sensitive and the slightest contact could make me-"
    sa "Poke..."
    r "Eep!"
    n "Molly, how are you feeling? Is it in yet?"

    scene nodokontest55
    with dissolve

    mo "Oh...it’s in, alright! Hah!"
    mak "I feel like this is not what Miss Imai had in mind when she said she wanted all of us to start bonding earlier."
    n "I don’t know. This is the closest I’ve felt to all of you in a while. It’s like we’re forming a brand new secret society. "
    r "We should come up with a name."

    scene nodokontest56
    with fade

    ki "Sisterhood of the traveling dildo?"
    sa "Do we...really need a name?"
    mo "{i}Hah...{/i}oh, fuck...ooooh, god...."
    r "Oh, right. Molly’s doing stuff. I almost forgot."
    no "Are you having fun down there, Molly? Is there anything I can do to help?"
    mo "Hah...hah! No!"
    mo "But...it’s in...right?! You all see it, right?!"
    mo "Which means...I can move on...to the next size...right?!"
    no "Already? You don’t want to {i}warm up{/i} a little more?"

    scene black
    with dissolve2

    mo "Hah! Hah...no! I...can go bigger! This isn’t...my first time riding a...monstrous sex toy!"
    mo "Someone...bring me the tentacle! The time...has come...for redemption!"

    "........."
    "......"
    "..."

    scene nodokontest57
    with dissolve2

    mo "God! It seems even bigger now that it’s down here! Is this even possible?!"
    no "For the sake of saving your vagina, the entire tentacle does not need to go inside. I will acknowledge that its base seems quite...{i}impossible{/i} for a girl of your size."
    r "Or {i}any{/i} size. That’s like...a can of corn and a half girth-wise."
    ki "I bet I could do it."
    n "That’s not really a thing you should be bragging about, Kirin."

    scene nodokontest58
    with dissolve

    mo "{i}Hah!{/i}"
    ki "Ah! Here we go! Molly’s got the tip in! "
    mo "The...hah...suction cups...feel really...weird..."
    n "Good weird or bad weird? I’ve always wondered about that."
    sa "H...Have you?..."

    scene nodokontest59
    with dissolve

    mo "Good...{i}really{/i} good..."

    scene nodokontest60
    with fade

    mo "Oh, god...nothing’s...hah! Nothing’s ever...been this deep before! Aaaah! Oh, fuck! That’s so good!"
    r "Molly, it’s just an insertion contest. You don’t need to, like...ride it to {i}completion.{/i}"
    ki "But she totally should anyway. Just saying."
    no "Shall we bring you the third and final dildo, Molly? It’s only several inches bigger. I think you might have a real shot at-"
    mo "No! Hah! Don’t...want to get off! Tentacle...is too good! Fuck! I can’t hold on! The energy...it’s overflowing!"
    sa "So she...still speaks like that when she’s..."
    r "It’s Molly. Did you really expect anything else?"
    mo "Oh god...I’m gonna cum...I’m almost there! I’m...haaah!"
    ki "Jesus, I’m gonna cum too just watching her bounce up and down like that."
    n "You think {i}that’s{/i} impressive? Just look at Makoto."

    scene nodokontest61
    with fade

    r "She’s jumping directly to the third one?!"
    mo "Wha...what?!"
    mak "It’s not like I was going to clean Molly’s fluids off of the other two. Besides, this thing isn’t even that big."
    no "It’s over a foot in length, Makoto."
    mak "That might be a lot for a weakling like Molly. But it shouldn’t be any problem at all for someone like-"

    scene nodokontest62
    with dissolve

    mak "Ngh!"
    no "What were you saying, Makoto?"
    mak "Still...not a problem..."
    mo "Cumming! I’m cumming! I’m..."

    with hpunch

    mo "AAAAAAAaaaaAAAAAAHHHHhHHHHHH!"
    ki "Round of applause for Molly, everybody! Woohoo!"
    r "Congratulations on joining those of us who gave away a part of our souls tonight!"
    no "Makoto, given that Molly is now “out of commission,” if you can fit the final toy inside of you, you’ll be crowned the winner and can leave behind Nodokathon for good."
    mak "Sounds..."

    scene nodokontest63
    with dissolve

    mak "Enticing..."
    sa "Wow..."
    r "Makoto’s...really impressive, isn’t she?"

    scene nodokontest64
    with dissolve

    mak "The trick is to...ah...pretend it’s...someone you really like..."
    ki "Damn. And that just lets you rewrite how anatomy works?"
    n "The human body is a lot more durable and adaptable than you’d think, Kirin. Much greater feats have been accomplished by much smaller humans. "
    n "But yeah, not gonna lie. That is impressive."
    mo "Hah...hah...but...she still has...a few more inches...before she can...beat me!"
    no "What do you say, Makoto. Can you stomach the last-"

    scene nodokontest65
    with dissolve2

    mak "AAAAHHHH!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nodokontest66
    with dissolve2

    no "Well, ladies...it appears your winner of the third and final competition...and an official Nodokathon champion...is Makoto Miyamura."
    mak "I have accomplished many things in my life that I should be very proud of."
    mak "This is not one of them."

    scene nodokontest67
    with dissolve

    no "But it’s an accomplishment no less, you see. And one you {i}should{/i} be proud of as it will go down in history."
    no "So, if you’d like to make a speech as the winner, please do so now. But make it one befitting a champion because that is what you {i}are{/i} whether you like it or not."
    mak "I’d like to thank the Academy...and God..."
    mak "{size=-3}But most importantly, my mother- for creating an environment where I became desensitized to casual sex at such an early age that I now see no issue with testing the capabilities of my vagina in front of my classmates.{/size}"
    ki "Amen."

    scene nodokontest68
    with dissolve

    mo "I can handle the third one too! Just...watch me!"

    scene black
    with dissolve2

    n "Molly, stop! You’re going to kill yourself!"
    mo "Then I will die a legend!"

    $ makotonodowin = True

    "And so {i}another{/i} war comes to an end — one that you’d much rather have been there for than its predecessor."
    "But again, you were hopelessly flailing behind the eyes of gods, just ever-so-slightly out of reach and ever-so-slightly out of touch with the truth."
    "But that’s fine, for your night was one to remember."

    $ renpy.end_replay()
    $ sportswars19 = True

    jump sportswars20

label makotospring1:
    play sound "phonebeep.wav"

    "I tap on Makoto’s name in my phone and wait for her to answer."
    "Seeing her again during the last beach trip reminded me of how close we used to be. "
    "And given that I’ve been slowly allowing pretty much everyone {i}else{/i} back into my life, I know I shouldn’t avoid her anymore."
    "I probably shouldn’t have done that in the first place."
    "Makoto’s an independent — the same way Ayane is. She can function just fine on her own and...that’s evidenced by the fact that she’s yet to really come chasing after me."
    "But just because she {i}can{/i} go it alone doesn’t mean I should subject her to that."
    "I know she idolizes me."
    "I know she loves me."

    scene sky
    with dissolve2

    "So I will make it up to her today by ejaculating inside of her so many times that her eyes pop out and she regurgitates semen all over my bedroom floor."

    play sound "phonebeep.wav"

    mak "...Hello?"

    play music "fallishere.mp3"

    s "Good afternoon, Makoto."
    mak "Uhh...good afternoon, Sensei?"
    s "How are you doing today?"
    mak "...Fine?"
    s "Why do you sound so suspicious?"
    mak "Actually being suspicious might have something to do with it. It was hard enough getting used to you being nice. Receiving “good afternoon” calls is another thing entirely, though."
    mak "Which isn’t even mentioning the fact that your latest diet is all but devoid of me."
    s "Yeah, well...diet’s over. Come over to my place so we can have sex and talk about the end of the world."
    mak "What about Ami?"
    s "You...want her to join in?"
    mak "{i}No,{/i} idiot. I just don’t want my organs ending up in your fridge."
    s "She’s gone until tomorrow. Niki’s taking her backstage to some concert thing as some kind of “bonding exercise” or something."
    mak "So you’re telling me we can have uninterrupted sex with each other for an entire day?"
    s "That’s right."
    mak "I understand. Please wait one moment, Sensei."
    mak "{i}Mom! I can’t work tonight! I have plans with a friend!{/i}"
    s "..."
    mak "{i}No, it isn’t a boy!{/i}"
    s "Hey. That’s rude."
    mak "Sorry. I’m back. Is now a good time? "
    s "Y-"
    mak "Cool, I’m on my way over. Bye!"

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve2

    "And so began the night of infinite cumshots..."

    play sound "static.mp3"
    scene makotosomno1 with flash
    stop sound

    "And so ended the night of infinite cumshots..."

    mak "If I don’t get pregnant after all of that, chances are I’m just infertile."
    s "How are you still walking?"

    scene makotosomno2
    with dissolve

    mak "I could ask you the same thing. With how hard you went at it today, I’d have thought it was your first time fucking {i}anyone{/i} since you came out of your coma."
    mak "Of course that’s not true, though- considering how many times both Ayane {i}and{/i} I got to ride on the Sensei Express during the beach trip."
    s "So...I take it you’ve just decided to start embracing your role as a member of my harem lately?"
    mak "It’s either that or hate myself every minute of every day while I delude myself into believing I’ll somehow come out on top after all of this is said and done."
    s "If it ever {i}is{/i} said and done, you mean."
    mak "Wow. You’re just going to flat-out ignore my subtle self-loathing, huh?"

    scene makotosomno3
    with dissolve

    s "I do enough self-loathing for the two of us. Just go back to being a cooperative harem princess and we can call it a night."
    mak "“Princess” has a nice ring to it. Say it again, just without the harem part. "
    s "You’ll have to fight Ayane for that title, unfortunately. She’s been calling herself that since we first started messing around."
    mak "I’m gonna have to fight her over a bunch of things from now on, aren’t I?"
    s "Probably. But it’s your turn to make the next apocalyptic Power Point, so you can begin your battle then. For now, bed."

    scene black
    with dissolve2

    mak "You’re right. For now, bed."

    "Makoto drops her towel on the ground, slipping on a pair of pajamas while I elect to simply just collapse onto the bed instead."
    "There’s just no sense getting dressed right now when I could very well wake up in the middle of the night in search of a midnight snack."

    scene makotosomno4
    with dissolve2

    "She turns off the lights and plops down beside me, fixating her eyes on the same appendage she’s been fixated on ever since walking through the door."

    mak "You’re just gonna...let it all hang out like that?"

    "She seems somewhat less interested this time, though. Probably from all the repetition."

    s "Is that a problem, Makoto?"
    mak "No. In fact, I’d wager I’m {i}more{/i} familiar with your lower half when it’s exposed. "
    mak "I just thought you wanted to also talk about stuff based on what you said when you called me earlier. And all {i}this{/i} does is send us spiraling toward more hardcore sex."
    s "Is my penis really that irresistible?"
    mak "Kind of, yeah. It’s sort of ruined my life."

    scene makotosomno5
    with dissolve

    mak "I still like you, though. Don’t worry."
    s "Thanks...I think?"
    mak "So, what now? Anything change following the beach trip? Any interesting {i}revelations{/i} that came to you in the subsequent days?"
    s "Not so much. You?"
    mak "Hm...there was {i}one{/i} thing, now that I think about it. It’s probably nothing, though."
    s "Barely anything is {i}nothing{/i} once the end of the world starts getting involved. Ayane would kill us if we dismissed little things for simply just...being little."
    mak "Well, if you {i}must{/i} know — Yumi’s started skipping school again."
    s "I...didn’t realize she stopped?"
    mak "Mhm. She’s been way more present ever since you left. But lately, I haven’t seen her at all. And considering we now know that she’s aware of the loops-"
    s "Yeah, sorry to break it to you like this after I literally just said we shouldn’t dismiss anything small, but that’s {i}probably{/i} for a different reason."
    mak "You did something, didn’t you?"
    s "Kind of? Chika saw Yumi and I together when I went off to look for her the night of the sleepover. Then that spiraled into a huge misunderstanding and now Chika thinks I’m fucking her."
    mak "{i}Are{/i} you?"
    s "This might come as a surprise, but no. I am not."
    mak "That {i}does{/i} come as a surprise. What a life we lead now where finding out which of my classmates you’re {i}not{/i} having sex with comes as a bigger surprise than the opposite."
    s "Anything else besides that? Any weird dreams or...strange occurrences? Things that might signal an impending reset now that we’ve lost the one person who was able to see them coming?"

    scene makotosomno6
    with dissolve

    mak "It’s hard to dream if you can’t sleep. And lately, apart from you not paying any attention to me, {i}that’s{/i} been my biggest issue. The apocalypse is like...ninth."
    s "Do you think it’s depression-related?"
    mak "Could be. All I know is it’s gotten to the point where I’ll just lie there staring at the ceiling for hours on end until, next thing I know, the sun’s out again."
    s "On the bright side, at least you’ll get to look at me tonight."

    scene makotosomno7
    with dissolve

    mak "Sounds like a great opportunity to make up for lost time."
    mak "{i}Unfortunately,{/i} I won’t be doing that."
    s "What? You’re not leaving, are you? Ami and Niki probably won’t be back until like noon tomorrow."
    mak "I’m not {i}leaving.{/i} I’ve just started medicating myself before bed. {i}Responsibly,{/i} of course. We don’t want another Miku situation on our hands, do we?"
    s "...Medicating {i}how?{/i}"

    scene makotosomno8
    with dissolve

    mak "Just sleeping pills, Sensei. I’m not suddenly a drug addict because you started hanging out with other girls more than me. I just hate being awake when I want to sleep."
    s "Well, I can certainly relate to that. It feels like sleep is the only time I ever really feel at peace lately."
    mak "Then, are {i}you{/i} having any strange dreams?"
    s "..."
    mak "Well?"
    s "I keep seeing Maya in them."

    scene makotosomno9
    with dissolve2

    mak "..."
    mak "Is that so?"
    s "She never acknowledges me. And sometimes, other things are there as well. "
    s "I...can’t really explain any of them without sounding insane, though."
    mak "And the girl who looks like Maya and acts like Maya but {i}isn’t{/i} Maya...what about her?"
    s "What {i}about{/i} her?"
    mak "Are you still avoiding her?"
    s "She...makes that very hard for me to do."

    scene makotosomno10
    with dissolve
    stop music fadeout 15.0

    mak "Of course she does."

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "Makoto? Where are you-"
    mak "I’ll be back in a second, jeez. I’m just taking my pills. "
    s "I’m sorry for bringing her up."
    mak "Oh, stop. I’d have taken them regardless. It’s just a {i}coincidence{/i} that my desire to sleep coincides with delusional rambling about your dead ex-girlfriend."
    s "Your sarcasm is so palpable that I’m tempted to bend it over and fuck it."
    mak "Heh. So your perversions extend to the intangible now?"
    s "If only you knew, Makoto..."
    s "If only you knew."

    "She comes back to bed and curls up beside me. "
    "But while my cock presses up against her belly, still warm and somewhat moist from the bath we took to drown the mess we made of each other, nothing happens."
    "She just looks into my eyes and I look into hers."
    "Then we kiss."
    "It’s something still somewhat unfamiliar to us."
    "But it feels nice."
    "And despite all logic and rationale reminding me that this relationship is nothing even close to pure, it doesn’t feel that way."
    "It feels like we deserve each other."
    "That’s the last thing I think before falling asleep."
    "I wish I knew what was on her mind when she did the same."
    "........."
    "......"
    "..."

    $ makoto_love += 1

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"

    scene makotosomno11
    with dissolve4

    "She’s still beside me when I wake up, but I feel as if she shouldn’t be."
    "Dreaming of one girl while lying next to another feels disgusting by even my standards."
    "But if I’m doing the same when I’m awake-"
    "If I’m closing my eyes and pretending all of them are {i}her,{/i} as unintentional as it may be — dreams are nothing."
    "It’s just your mind playing tricks on you."

    s "..."
    mak "..."

    "She’s sound asleep."

    s "..."
    mak "..."

    "It’s time for my snack."

    scene makotosomno12
    with dissolve2
    play music "heartbeat.mp3"

    s "{i}Makoto...{/i}"
    mak "..."

    "She doesn’t move. "
    "Not one bit."
    "I can’t even hear her breathing. "
    "And if it weren’t for the fact that she’s hot to the touch, I might even worry she is dead."
    "Not like {i}that{/i} would stop me either though when I crawl into bed beside a ghost each time I start to think too much."

    s "..."
    mak "..."

    "But right now, what I need is to {i}stop{/i} thinking."

    scene black
    with dissolve2

    "I need to let it all out once more."
    "........."
    "......"
    "..."

    scene makotosomno13
    with dissolve4

    mak "..."
    s "..."

    "Quiet, so as to not disturb her."
    "I have permanent consent."
    "If she were awake, she’d tell me “yes.”"
    "But she’s not."
    "So I will fill in the blanks on my own."
    "And I will claim her once more as what she’s always been."
    "Teacher’s pet."

    s "..."
    mak "..."

    menu:
        "Move arm":
            scene makotosomno14
            with dissolve2

    mak "..."

    "I lift up her arm and place it on the pillow."
    "She still doesn’t sense anything."
    "It’s safe for me to keep going."

    menu:
        "Lift shirt":
            scene makotosomno15
            with dissolve2

    mak "..."

    "I reach forward and slide up her tank-top, revealing two small mounds no larger than a C at best. Probably a B if I had to put money on it."
    "Her nipples aren’t hard yet, but I’m sure that’ll change soon."

    s "..."
    mak "..."

    "I gaze down at a truly remarkable creature — one who exists to please and {i}be{/i} pleased."
    "I am killing two birds with one stone."
    "I’m fixing her. I’m saving {i}me.{/i}"
    "It’s safe to keep going."

    menu:
        "Remove shorts":
            scene makotosomno16
            with dissolve2

    mak "Mm..."

    "This step was the hardest."
    "They clung to her skin like an extra layer of flesh. "
    "And as I slid my fingers into her waistband to remove them, it felt like I was sliding off a piece of her."

    s "..."
    mak "..."

    "How beautiful she is — still so clean and fresh despite the beatings I have given her."

    mak "Mm..."
    s "..."

    "It’s safe to continue."

    menu:
        "Mount her":
            scene black
            with dissolve2
            $ renpy.pause(2, hard=True)
            scene makotosomno17
            with dissolve4

    mak "..."
    s "{i}Makoto...{/i}"
    mak "..."

    "A small patch of pubic hair tickles the underside of my cock as I instinctively slide forward."
    "Her nipples are hard now. I told you this would happen."
    "I know her body better than I know my own."
    "I know what’s best for both of us."

    s "{i}I’m gonna fuck you now...okay?...{/i}"
    mak "..."
    s "{i}You want it, right?...{/i}"
    mak "Nn..."
    s "{i}Yeah...I bet you’re tired of waiting, aren’t you?...{/i}"
    mak "..."
    s "{i}I’ll put it in now then...don’t wor-{/i}"
    mak "{size=-10}D...{/size}"
    mak "{size=-10}Daddy?...{/size}"
    s "..."
    mak "{size=-10}What are you...doing?...{/size}"
    mak "{size=-10}We...can’t...{/size}"
    s "..."
    mak "..."
    s "..."
    mak "..."

    menu:
        "Insert penis":
            play sound "static.mp3"
            scene makotohalloween2 with flash
            scene lavendersgreen22 with flash
            scene makotohalloween26 with flash
            scene lavendersgreen26 with flash
            scene makotosomno18 with flash
            stop sound

    mak "..."
    s "..."

    play sound "sound.mp3"
    scene makotosomno19
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene makotosomno20
    with dissolve2

    "I enter her meat tunnel. It feels really good."

    mak "Nn..."

    "{b}bro can you just be normal and enjoy the goddamn somnophilia scene{/b}"

    stop music
    play sound "static.mp3"
    scene makotosomno19 with flash
    stop sound

    s "I’m sorry, Makoto."
    s "I can’t help myself."

    play sound "static.mp3"
    scene makotosomno21 with flash
    stop sound
    play music "sleepystreets2.mp3"

    mak "Ah......aaah......"

    "I lift her up her waist and thrust into her in as deep as I can go."
    "I worried that skipping foreplay would have made it harder to enter her, but it seems her body has learned by now to accept me whenever I command."

    mak "{i}Daddy...stop it...{/i}"

    "Either that or the dream she’s having has made her so wet that {i}anyone{/i} could have taken her right now."

    mak "Aah......aah...."

    "But she isn’t {i}anyone’s.{/i} She is {i}mine.{/i} And I can ignore the thoughts that free-float inside her head because of the visions that swim through the seas of mine."
    "On that infinite ocean, surrounded by clocks — I’m caught in an endless war with myself and the visage of what I want but can never have."
    "I can have this, though."
    "I can have it whenever I want."

    s "Ngh!...Mmf!..."
    mak "A....{i}Aaah...{/i}"

    "Harder and harder I thrust, sinking my fingers deep into her flesh as I continue to angle her body to fit me perfectly."
    "Beads of sweat form on her skin as those B’s or C’s jiggle! Her face gets redder each and every second! Her mouth opens wider! Her breathing becomes heavier!"

    play sound "static.mp3"
    scene makotosomno22 with flash
    stop sound

    "I stare down as she folds within a dream — but I do not wish to see what she sees as I fear that {i}I{/i} am not the father she speaks of."

    mak "{i}Daddy!...Please!...Aah!...{/i}"
    mak "{i}I can’t...take it...anymore!...{/i}"

    "She clamps down unintentionally and I need to bite my tongue so I don’t spill myself out before I’ve gotten my fill."

    s "{i}You like that, Makoto?...{/i}"
    s "{i}I bet you’re proud, huh?...{/i}"
    s "{i}You got me so hard in the middle of the night that I couldn’t keep my hands off of you...{/i}"
    mak "Aa......aaah...."

    play sound "static.mp3"
    scene makotosomno23 with flash
    stop sound

    s "{i}This...never would have happened if you weren’t so cute, you know?...{/i}"
    s "{i}Acting so mature when you’re...just another confused...hopeless teenager with a thirst for...teacher cock...{/i}"
    s "{i}I should have fucked you the moment you walked into my office for the first time...I bet you would’ve loved that, wouldn’t you?{/i}"
    mak "Aah........aaaah......."
    s "{i}That’s right...let those cute little moans out...{/i}"
    s "{i}Show your...beloved role model...just what lengths you’re willing to go to for him...{/i}"

    scene makotosomno24
    with dissolve2

    mak "Hah...........nhh........"
    s "{i}I bet you...only took those pills tonight because you wanted me to do this...am I right, Makoto?{/i}"
    s "{i}Have I...made you so fucking lewd that you crave my dick even when you aren’t conscious?...Are you that big of a...fucking whore now? Huh?...{/i}"
    mak ".........hah."
    s "{i}Fuck...I’m gonna cum...{/i}"
    mak "Hah..........ah........"

    scene makotosomno25
    with dissolve

    s "{i}Did you hear me, baby?...I said I’m gonna cum...Any objections?...{/i}"
    mak "{i}Daddy...please...{/i}"
    mak "{i}Not...inside...{/i}"

    play sound "static.mp3"
    scene makotosomno26 with flash
    stop sound

    s "{i}Not inside?...You want Daddy to paint your pretty little body?...You want him to shoot it all over your little tits?...Or do you want it in your mouth instead?...{/i}"
    mak "Ah.......Aaah......"

    "My thrusts send ripples through her skin as I ramp up ahead of my impending climax — and the sounds of our connection are only accentuated by the silence."
    "All I can hear are the extremely brief noises that manage to escape her lips and the violent sound of her {b}MEAT TUNNEL{/b} welcoming me home."

    mak "Aah......{i}Aaah...{/i}"

    "I can’t take it anymore."

    s "{i}Makoto...I love you...{/i}"
    s "{i}I love your face...I love your voice...I love your...tight fucking pussy...{/i}"
    s "{i}You still...want to be my wife?...You want to run away together?...You want to fuck me all day every day and forget about all this apocalypse bullshit?...Does that sound good?...{/i}"
    mak "Nnh.......nnh!"
    mak "Daddy...{i}Daddy...{/i}"

    "It’s safe to continue."

    menu:
        "Ejaculate":
            scene black
            with dissolve2
            stop music fadeout 10.0

    s "{i}Hah....ngah....{/i}"
    s "{i}Aaah.....{/i}"
    s "{i}NYAAGHHHHHH!!!!!{/i}"

    "........."
    "......"
    "..."

    scene makotosomno27
    with dissolve3

    mak "Hah......hah.......haah......."
    s "..."
    s "Mission complete, I guess?"

    "{b}see, akira? you’re not ALWAYS a bitch. it’s this sort of potential i’ve seen in you from the start. but nooooo, everyone else would rather MAKE you do things.{/b}"

    s "You’re the same way. Just because you won’t leave me the fuck alone doesn’t mean we’re friends, so stop talking to me like one."

    "{b}we ARE friends, though. the closest kind. like peanut butter and- what do you humans normally mix peanut butter with again? mayonnaise?{/i}"

    s "I’m going to bed. Please leave me alone."

    "{b}wait. aren’t you forgetting something?{/i}"

    "He’s right."
    "There’s one thing left to do."

    menu:
        "Clean up":
            scene black
            with dissolve2

    "I retrieve the towel Makoto dropped in the corner of the room-"
    "And I hide the evidence of what I’ve done while she was unconscious."
    "........."
    "......"
    "..."

    $ makoto_lust += 3
    $ totaldays += 1
    "{i}Makoto’s lust has unintentionally increased to [makoto_lust]!{/i}"

    if day == 7:
        $ day = 1
        hide sunday onlayer date
        show monday onlayer date
        jump endofmakspring1
    if day == 1:
        $ day = 2
        hide monday onlayer date
        show tuesday onlayer date
        jump endofmakspring1
    if day == 2:
        $ day = 3
        hide tuesday onlayer date
        show wednesday onlayer date
        jump endofmakspring1
    if day == 3:
        $ day = 4
        hide wednesday onlayer date
        show thursday onlayer date
        jump endofmakspring1
    if day == 4:
        $ day = 5
        hide thursday onlayer date
        show friday onlayer date
        jump endofmakspring1
    if day == 5:
        $ day = 6
        hide friday onlayer date
        show saturday onlayer date
        jump endofmakspring1
    if day == 6:
        $ day = 7
        hide saturday onlayer date
        show sunday onlayer date
        jump endofmakspring1

label endofmakspring1:
    scene makotosomno28
    with dissolve4

    mak "..."
    s "..."

    "I wake up to Makoto staring down at me."
    "A wonderful way to start the day."

    mak "..."
    s "..."
    mak "Good morning, Sensei."
    s "Good morning, Makoto."
    mak "..."
    s "..."
    mak "I have a question for you."
    s "..."

    "Fuck."

    s "Uhh..."

    scene makotosomno29
    with dissolve

    mak "I didn’t...by any chance..."
    mak "Act {i}strangely{/i} in my sleep last night...did I?"
    s "..."

    "Wait...what?"

    s "What...do you mean?"

    scene makotosomno30
    with dissolve

    mak "Well, it’s just that...I had a very...{i}strange{/i} dream. "
    mak "And I woke up feeling kind of...uh..."
    mak "{i}Gross.{/i}"
    s" ..."
    mak "So if I...{i}did{/i} anything while I was asleep...surely you’d {i}tell{/i} me, right?"
    s "..."
    mak "..."
    s "Was it a dream about your dad?"

    scene makotosomno31
    with dissolve2

    mak "Ah..."
    s "..."
    mak "I wasn’t...{i}talking...{/i}was I?"
    s "You may have said some things."
    mak "And..."
    mak "And that’s how you..."
    s "Fantasies are fantasies, Makoto. I would never judge you for anything."

    scene makotosomno32
    with dissolve2

    mak "Please excuse me for the rest of forever."

    scene black
    with dissolve2
    play sound "doorslam.mp3"

    $ renpy.end_replay()
    $ makotospring1 = True

    "Makoto presumably gets dressed and heads home, leaving me to fend for myself until Ami and Niki come back."
    "Niki isn’t fully moved in yet, but she’s been bringing her things over little by little."

    s "..."

    "I imagine it’s not long at all until I can’t safely do things like this anymore."
    "But I guess it’s never really been “safe” in the first place."

    s "..."

    "I miss when life was easier."

    play sound "tackle.mp3"
    scene bedroom_day
    with hpunch

    "I need to distract myself."

    jump ch4morningmenu

label makotospring2:
    if _in_replay:
        play music "undersea.mp3"

    "The next five minutes are agonizingly long as I have to suffer the full force of what it means to be the main character."
    "Despite the screaming, which can most assuredly be heard from the halls, no one comes to the rescue."
    "No one leaves their room at all — because they’re only there when I need them to be or when the {b}SCRIPT{/b} calls for it."
    "And right now, that script only calls for pain — frightened yelps as the gazelle bleeds out before me while I realize I have never been a lion at all."
    "I have been a poacher. "
    "And I have gravely injured this animal while hunting a far more elusive, far more {i}valuable{/i} one."
    "There are gazelles everywhere out here. Who am I supposed to sell this one to?"
    "..."
    "It isn’t worth it to waste another bullet. But I was born with the burden of guilt — so I’ve nothing left to do but sit and wait as the last bit of life drains from its body."

    play sound "static.mp3"
    scene makotofindsher1 with flash
    stop sound

    mak "Oh, wow. That {i}is{/i} a lot."

    "I suppose I was exaggerating a bit. I’m sure that comes as no surprise, though."
    "Clearly, Miku isn’t going to {i}die{/i} from this. She just might have some trouble sitting down for a while."
    "Or worse yet, this experience will add one more item to her growing list of traumas and, after today, she won’t want to have sex with me {i}at all{/i} as it will only bring back bad memories."

    mi "Ngh!!!! Ngh!!!! It still hurts!!! The pain...won’t stop!!!!"
    s "What now? What are we supposed to do?"
    mak "Miku, do you think you need to go to the hospital? "
    mi "I don’t know! I think my vagina’s broken!"
    mak "Well, at least her sense of humor is intact."
    mi "I’m not joking! I seriously think it’s broken!"
    s "Is that even possible?..."
    mak "I guess that depends on what she means by “broken.” You likely just tore something. {i}Other{/i} than what you very obviously tore by deflowering her, I mean."
    mi "I’m not gonna have to get friggin’ vagina stitches, am I?"
    mak "Miku, do you remember how long it took for you to stop bleeding when you scraped your knee on the pavement playing soccer?"
    mi "This ain’t my friggin’ knee we’re talkin’ about, Makoto! Sensei stuck it in my friggin’ cervix!"

    play sound "static.mp3"
    scene makotofindsher2 with flash
    stop sound

    mak "He might have touched it, but he didn’t stick it {i}in{/i} your cervix, Miku. What I’m trying to get at is that this {i}always{/i} happens when you bleed. Your body just...doesn’t clot well, I guess?"
    mi "So what I’m hearin’ is this didn’t happen to you?! "
    mak "Not like that, no. But...you’re {i}probably{/i} fine?"
    mi "Probably?! You don’t know?!"

    scene makotofindsher3
    with dissolve

    mak "I mean...my {i}mom{/i} might? But calling her about this would be...well..."
    mak "She might have some things to say to you about it once you settle down."
    mi "{i}MNGGGHHH!{/i} I don’t even care anymore! She can talk about whatever she wants if she knows how to make this stop!"

    scene makotofindsher4
    with dissolve

    mak "Sensei, what do you- can you {i}not{/i} look like that, please? It’s not like you killed her. You just...may have broken her vagina."
    mi "AAAAGGGHH! I KNEW IT! IT {i}IS{/i} BROKEN!"

    play sound "static.mp3"
    scene makotofindsher5 with flash
    stop sound

    mak "Miku, I’m going to give you three options: wait out the pain with me, go to the hospital, or see if there’s something my mom can do."
    mi "Mmmmngh! I don’t know! Just pick one for me!"
    s "I think you should call Maki."

    scene makotofindsher6
    with dissolve

    mak "I think so too. Especially if the pain is as bad as Miku says it is. You know what that means though, right?"
    s "Yeah. I’ll tell her it was me."

    scene makotofindsher7
    with dissolve

    mak "Wha- are you out of your fucking mind?! Absolutely not! It means you have to get the hell out of here before she {i}finds out{/i} it was you! "
    mi "I’ll make up a story! I don’t want you gettin’ in trouble because’a me, Sensei! That ain’t fair to you! You didn’t do nothin’ wrong!"
    s "...Are you serious right now?"
    mak "Yes! You wanted me to handle this, didn’t you? This is me handling it. Now, get the hell out of here so I can ask my mom about how to fix Miku’s vagina."
    mi "I’m sorry, Sensei...I’m really sorry! I tried to endure it, but I just-"

    scene makotofindsher8
    with dissolve

    mak "Miku, shh. Just try to calm down and hold still. I’ll find something to try and stop the bleeding."
    mi "Oh god, you ain’t gonna try to plug it up, are ya?! Ain’t no way I’m puttin’ anythin’ else in there right now! Not happenin’! No, ma’am!"
    s "..."
    mak "I’m not going to plug it up, I’m-"

    scene makotofindsher9
    with dissolve

    mak "Sensei, {i}why{/i} are you still here?! Leave! "

    stop music
    play sound "static.mp3"
    scene bedroom_night with flash
    play sound "doorslam.mp3"
    with hpunch

    "I make it back home in two pieces after stealing one from someone else."
    "A successful hunt, I do say. But the bounty, while it sustains me, is one that I can not lay upon the table and dig into with a fork and knife."
    "I hold in my hands a pair of small horns, plucked from the skull of an animal. They’ll look lovely upon my mantle beside the countless others I have stolen."
    "These ones will require some work, though. There’s flesh still at the roots. And bright, red blood drips from where they were removed."
    "It stains my hands and my floorboards, but it’s nothing that the grease of an elbow or an ammonia cocktail won’t take care of."
    "I set them down and I wait for my phone to ring."

    $ renpy.pause(30, hard=True)
    play sound "phonering.mp3"
    $ renpy.pause(0.4, hard=True)
    play sound "phonebeep.wav"

    "It finally does."

    mak "I have good news, Sensei. "
    mak "Miku’s vagina is {i}not{/i} broken."
    s "So..."
    s "Maki was able to help?..."
    mak "By driving her to the hospital, yes."
    s "Wha-"

    play music "bloodandsunset.mp3"

    mak "Just as a precaution, though."
    mak "The doctors said the bleeding would have eventually stopped on its own. But they gave her some pills to help with the pain and told her to take it easy for a while."
    mak "She’s now currently being lectured on safe sex. So in that regard, I guess a little good {i}did{/i} manage to come out of this."
    s "..."
    mak "Do you feel guilty?"
    s "It’s kind of hard not to when it’s literally my fault."
    mak "Just be glad it happened the way it did and not with someone no one knew about. I suppose it’d be hard finding {i}anyone{/i} like that at this point, though."
    s "..."
    mak "Listen..."
    mak "I know it’s late. But would you want to meet up?"
    s "I’m not really in the mood to have {i}more{/i} sex, Makoto."
    mak "Really? Because, according to Miku, you never even finished. Unless you’re saying you finished {i}yourself{/i} off when you got home."
    s "Makoto-"
    mak "I’m sorry...That was a joke. A poorly timed one, I’ll add. "
    mak "But Sensei, I {i}do{/i} want to see you. And not for sex either. We don’t {i}always{/i} have to do that, you know? "
    mak "I just don’t want this sitting with you. Especially now that you’re actually an active participant in my life again after feeling sorry for yourself for so long."
    mak "So...how about we meet in the park?"
    s "The park?..."
    mak "The one near the school."
    s "That’s where everything started today. That’s where I met up with Miku."
    mak "Heh..."
    mak "It seems like everything comes full circle nowadays, doesn’t it?"
    s "..."
    mak "I’m still at the hospital right now, but I think we’ll be leaving soon. Can you maybe meet me there in...an hour?"
    s "Are you sure you don’t want to stay with Miku and make sure she’s okay?"
    mak "She’s fine, Sensei. And extremely embarrassed right now, so it’ll probably be {i}good{/i} for me to leave her alone and let her wallow in shame for a bit."
    s "..."
    mak "..."

    scene black
    with dissolve2

    s "Okay."
    s "We’ll meet in an hour."

    "........."
    "......"
    "..."

    scene clearnightsky
    with dissolve2

    "I can’t help but notice how soft my hands are now that I’ve washed the blood off of them."
    "They were all I washed, though. "
    "I’ve been afraid to take my pants off ever since putting them back on in Miku’s room as I know that glancing down at my weapon will do naught but remind me of the beast it killed tonight."

    s "..."

    "Maybe I’m making a bigger deal out of this than it needs to be?"
    "That’s how Makoto’s making it sound."
    "That’s how the me inside of me is making it sound."
    "And I’m sure that’s how Miku will make it sound too once she’s all better."
    "But..."
    "To me, it feels like an omen."
    "To me, it feels like the universe telling me that my favorite hiding place isn’t safe anymore. "
    "And that’s all the more terrifying since I’ve known I’ve been sleeping in the cave of a black bear ever since I began life here."
    "I didn’t think it would ever wake up."
    "And now all I can do is worry that something will bite into {i}my{/i} neck next."

    mak "Thanks for coming."

    scene makotofindsher10
    with dissolve4

    s "..."
    mak "How do you feel?"
    s "Not so great, to tell you the truth."
    mak "Yeah. You don’t {i}look{/i} so great either."
    s "Are you mad at me?"
    mak "Do you {i}want{/i} me to be mad at you?"
    s "..."
    mak "..."
    s "Kind of."
    mak "You want me to lecture you? Try and talk you out of repeating this same bad decision in the future when we both know that will do nothing to stop you?"
    s "..."
    s "Kind of..."
    mak "Okay. I can do that."

    play sound "static.mp3"
    scene makotofindsher11 with flash
    stop sound

    mak "You made a very irresponsible decision tonight, Sensei."
    mak "The doctor did not hesitate to comment on how Miku’s body was very much {i}not{/i} meant to withstand “whatever it was” she attempted to put in there. And I’m sure that wasn’t lost on you."
    mak "You knew the damage you could potentially inflict on her. And while it would have been hard to guess just how much she’d bleed as a result of that due to a preexisting condition, it was still dangerous."
    mak "I get being caught up in the moment, but surely you must have noticed that you didn’t {i}fit...{/i}correct?"
    s "Yeah, but...it’s never been like {i}that{/i} before. I knew it would hurt, I just didn’t think it would hurt her {i}that{/i} much."

    scene makotofindsher12
    with dissolve

    mak "I’m sure it didn’t help that Miku isn’t good with blood. I imagine that seeing what you’d done to her was a larger contributing factor in the panic that ensued than the pain itself."
    mak "But what’s done is done. And now you know to be more careful. "

    scene makotofindsher13
    with dissolve

    mak "A condom would have helped as well. The added lubrication certainly wouldn’t have been a negative."
    s "Is {i}she{/i} mad at me? Now that she’s started to...calm down, I guess?"

    scene makotofindsher14
    with dissolve

    mak "She feels guilty. And ashamed. What she imagined would be a special moment between you two ended in a trip to the hospital and you not getting any amount of pleasure {i}at all.{/i}"
    mak "So no, she’s not mad at {i}you.{/i} She’s mad at herself. And this will probably sound crazy, but I think most of us would feel the same way in her position."
    s "That’s because most of you are delusional."

    scene makotofindsher15
    with dissolve

    s "Of course her body wasn’t meant to “withstand” me. It’s not fully developed yet. I’ve just been getting lucky so far. But all of you are so blinded by desire to be with me that you flat-out don’t care."
    s "You’ll let me do anything I want to you because you think that’s the only way to my heart. And the worst fucking part is that you’re probably {i}right.{/i}"
    s "So is this just the burden I need to bear from now on in order to keep feeling human? To know that something could go wrong at any second and I could severely physically damage you?"
    mak "You realize that all of that has to do with the fact that you have a {i}gigantic{/i} penis and {i}not{/i} the fact that you’re just older, right?"
    s "..."
    mak "Did that make too much sense? "
    mak "Do you want me to just agree and call you a bad guy for wanting to fuck high school girls? Because that’s not unique to you, Sensei. It’s a top-selling genre at the porn shop for a reason."
    s "But there’s a difference between porn and reality, Makoto. Fetishizing that is completely different from participating in it and I {i}know{/i} you know that because you’re not an idiot."
    mak "You’re right. I’m not an idiot. "
    mak "But I’m also willing to acknowledge the fact that the majority of girls you know can literally {i}not grow up here.{/i}"
    s "But that’s-"
    mak "Besides, its a person’s {i}mental{/i} maturity that dictates just when it is and isn’t okay to sleep with them. Which isn’t doing you {i}any{/i} favors when it comes to girls like Miku...but think about it."
    mak "If it was just you and me for a million years...spending time together...getting to know one another...and maturing {i}mentally...{/i}would it {i}still{/i} be wrong to fuck me? "
    mak "Would you deprive me of experiencing everything life has to offer because of an arbitrary number that means {i}nothing{/i} in the face of where and {i}when{/i} we are?"
    mak "At what point is it okay to throw that out the window? How many thousands of years need to pass before that line is drawn?"
    s "It..."
    s "Hold on..."

    scene makotofindsher16
    with dissolve

    mak "You’re not as evil as you think, Sensei. You’re really not."
    mak "Expecting you to just keep your hands off of all of us indefinitely until we {i}literally manage to restore the flow of time{/i} is so unreasonable that {i}anyone{/i} would be on your side if they knew."
    mak "But they don’t...So you just need to keep believing you’re Satan himself while time ticks infinitely onward and every single one of us stays exactly the same. "
    mak "I can only imagine how hard that is for you."

    scene makotofindsher17
    with dissolve

    mak "And, trust me — I’ve been thinking about it a lot. I’ve had plenty of time lately."

    scene makotofindsher18
    with dissolve

    mak "Being sincere about any of this is {i}hard{/i} now. Like, I had no idea just how much of an impact {i}time{/i} had on morality until I experienced being stuck like this."
    mak "When there’s clear direction...and {i}consequences...{/i}all of that stuff makes so much sense. Bad decisions steer reality into the wrong direction and good ones steer it into the right one."
    mak "Taking those consequences {i}out{/i} of the equation just turns life into a sandbox. It’s a place where, no matter {i}what{/i} we choose to do, we all wind up back at the start."
    mak "So there can {i}be{/i} no right or wrong anymore. We’re all dogs chained to poles. And we’re hungry, so we’ll eat anything that’s thrown at us. Even if we know it isn’t safe."
    mak "Fill your belly. Go to sleep. Wake up in the sun. That’s it. That’s all we have now."
    mak "Which is why I can only {i}pretend{/i} to be mad at you. "

    scene makotofindsher19
    with dissolve

    mak "And why I don’t think you’re evil anymore."

    "A cat looks on. I have seen it before. "
    "Its eyes are like marbles. Its fur like the snow. "

    s "But if time moved normally-"
    s "If everything went back to the way it’s supposed to be..."
    s "And I was no different from who I am now-"
    s "Would I be evil {i}then?{/i}"
    mak "Why does it matter? That’s just a hypothetical. "
    mak "What’s real is where and when we are right now. And even in {i}this{/i} world, where time is as infinite as the sky-"
    mak "Trying to figure out answers like that is a waste of it."
    s "..."
    mak "Do you feel any better {i}now?{/i}"
    s "..."
    s "{i}Yeah?...{/i}"
    s "But I...don’t think I’m...supposed to."
    mak "Stop caring about what you are or aren’t {i}supposed{/i} to do and just enjoy this gift we’ve been given."
    mak "We can rewrite right and wrong here. And if the world was perfect the way it was before...I don’t think we’d have ever made it here at all."
    mak "Maybe {i}that’s{/i} what we’re supposed to do. {i}Really{/i} start over. Make a {i}new{/i} world."
    s "..."
    mak "I love you so much."

    scene black
    with dissolve2

    mak "How lucky I am to wake up somewhere I can do that forever."

    "........."
    "......"
    "..."

    scene makotofindsher20
    with dissolve4
    stop music fadeout 10.0

    "I feel at peace for the first time in months."
    "The cool air from the mouth of spring encircles me as I stare off into the night."
    "I don’t know when exactly Makoto left-"
    "But I think that’s the point."

    scene black
    with dissolve4

    "If T is for time or trees and threes then maybe my life isn’t mine."
    "If Heaven and Hell and the space in between can’t be seen then I think I’ll be fine."
    "I won’t ever get old, I won’t ever die young, I’ll do nothing but live and let love."
    "But when living and loving are things I don’t know-"
    "What exactly does my life consist of?"

    $ renpy.end_replay()
    $ makotospring2 = True
    $ makoto_love += 5
    $ mikublock = True

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}Her sanity has increased by 1!{/i}"
    "........."
    "......"
    "..."

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

label halloweenmakoto1:
    scene makotodecorates1
    with dissolve2

    ay "{i}Are you sure you’re ready to start insulting her like everything is normal again?{/i}"
    a "{i}Some things never change even when everything else in the world does, Ayane.{/i}"
    a "{i}This is but one of them.{/i}"
    mak "Do you ever get the feeling that someone’s talking about you behind your back?"

    play music "samhain.mp3"

    y "Yeah. Figure with the way I am though, it normally just means somebody {i}is.{/i}"

    scene makotodecorates2
    with dissolve

    mak "You’re not {i}that{/i} bad, Yumi. Like, yes, you’re an asshole. But you can be nice on occasion. Like how you showed up to help decorate even though you haven’t come to school in weeks."
    y "Ain’t like I got anythin’ else goin’ on. Chika dumped me and I ain’t got a fuckin’ clue where my mom is."
    y "But you so much as think about handin’ over any work I may have missed and I’m adding one more nerd to the list of girls whose teeth I’ve knocked in."
    mi "Makoto! Where the frick are we supposed to put these ghost things? I still ain’t got any idea what we’re doin’ here!"
    n "We can probably just throw them next to the door and sort of ease people into the scares, you know? No one is going to be afraid of these little guys."
    mak "Just put them wherever, you two. Ayane said she doesn’t care how we handle the decorating. But people are going to start showing up any minute now and I don’t want-"

    scene makotodecorates3
    with dissolve

    mi "{i}Blah, blah, blah. I’m Makoto. I like to pretend I’m an interior designer when all I really know how to do is sell dildos. Blah blah blah.{/i}"
    mak "Well, at least they’re working."
    y "Surprised Noriko’s still standin’, to be honest. Bitch pulled an all-nighter at the convenience store last night. Don’t think she’s slept for even a minute."

    scene makotodecorates4
    with dissolve

    mak "Oh, right. You two work together now, don’t you? I thought it was weird when you showed up at the same time."
    y "She works. I kinda just stand there and clean tables every now and then. Barely any customers in the old district. But hey, money is money and I ain’t about to turn it down."

    scene makotodecorates5
    with dissolve

    mak "Maybe that’s where this new semi-reliable side of you comes from then?"
    y "Or maybe I’m just fuckin’ fed up with bein’ hated by everybody. Shit’s tiring. Just want that fuckin’ reset thing to happen already so some shred of normalcy comes back into my life."

    scene makotodecorates6
    with dissolve

    mak "The only way that happens is if you forget about the resets entirely. Knowing they’re real sort of...changes your perspective of things in a lot of ways."
    y "Well, sign me the fuck up for that because I ain’t got the energy to deal with the end of the god damn world on top of all of everything else goin’ on."
    mak "Well, what’s “everything else” exactly? As someone else that everyone in the class dislikes, maybe I can help?"

    scene makotodecorates7
    with dissolve

    y "Nah, fuck off. I ain’t about to drag you into my shit too. Thanks for tryin’, though. "
    mak "I’m not trying to, like...give you a counseling session, Yumi. I just figured it might be good for you to get something off your chest to someone else who doesn’t give a shit anymore."

    scene makotodecorates8
    with fade

    y "You? Ain’t your whole ass thing givin’ {i}so many{/i} shits that you become un-fucking-bearable?"
    mak "You’re thinking of old Makoto. New Makoto just wants to relax and get laid."
    y "Oh is {i}that{/i} what the bondage gear is for? Kinda figured it was a costume because it’s Halloween and shit. But hey, you do you."
    mak "I will. That’s sort of my whole policy now that I know nothing has consequences anymore."
    y "Well if that’s true, why the hell are you spendin’ your free time setting up some Halloween party? "
    mak "Our infinite timeline may have shaped me into someone who cares less about her future, but I am still a control freak at the end of the day. And if I didn’t volunteer to do this, no one would have."
    y "Don’t see how that matters but, again, you do you."
    mak "What will {i}you{/i} do, though? Now that you know about stuff, I mean. "
    y "More of the same, I guess? Lay low until the world blows up? I don’t know — what am I supposed to do?"
    mak "That depends on what you want, I guess. Given what’s happened in the past, it’s highly probable that your mind won’t even {i}survive{/i} the reset again."
    y "Okay. The fuck’s that supposed to mean, though?"
    mak "That you can basically do anything you want and then not have to worry about regretting it since you’ll forget once things start over. Probably."
    y "Probably?"
    mak "I don’t really get how it works either. I just know some information stays and some goes. But you can ask me again for a clearer answer several loops from now if we’re both still ourselves."
    y "And if we ain’t?"
    mak "Then we’ll probably just keep reliving freshman year of high school over and over until someone figures out how to break us out. If we even {i}can{/i} break out. But honestly, what’s even the point?"

    scene makotodecorates9
    with dissolve

    y "Not bein’ a teenager anymore. This shit sucks. "
    mak "Maybe for you. But life doesn’t get any easier as you get older. Responsibilities multiply, expectations multiply, {i}pressure{/i} multiplies — and you just have to lie there and take it because you’re an “adult.”"
    mak "At least when we’re young, we can fall back on that fact. We don’t {i}have{/i} to be perfect because no one expects us to be. It’s the best time to do stupid stuff and make stupid mistakes."

    scene makotodecorates10
    with dissolve

    mak "But the thing with me is I’ve always been so focused on the future that I didn’t leave any room to {i}make{/i} those mistakes. Which effectively robbed me of what are supposed to be the best years of my life."
    y "So...just to make sure I’m understandin’ shit, you’re sayin’ that now that you ain’t gotta worry about growin’ up, you can just...chill? Am I gettin’ that right?"
    mak "Pretty much, yeah. And I think you can benefit from doing the same thing, Yumi. Which isn’t to say I think you’ve put {i}any{/i} amount of thought into your future to begin with. But now, you don’t have to."
    mak "That’s why I will {i}not{/i} be giving you any of the work you’ve missed out on during your prolonged absence since it literally does not matter. But old Makoto {i}would{/i} have because she sucked."
    y "Well, damn. Maybe this shit ain’t that bad then. And maybe new Makoto ain’t that bad either."

    scene makotodecorates11
    with dissolve

    mak "That just depends on your definition of “bad.” Because having a lack of consequences makes me more brazen as well. And I would now gladly throw anyone under the bus so long as it will benefit me. "
    y "That ain’t bad either. That’s how shit {i}should{/i} be. Ain’t nobody else gonna matter in the long run, so livin’ for yourself is all you can really do."
    mak "No, you’re not getting it. Nobody else matters because there {i}is{/i} no long run. There is here and now. But we’ll be right back here {i}again.{/i} That’s why I stopped caring."

    scene black
    with dissolve2

    "{b}MAKOTO FINALLY FINISHES POSITIONING THE PUMPKIN THING AND STANDS UP WOW THAT TOOK A LONG TIME{/b}"

    play sound "static.mp3"
    scene makotodecorates12 with flash
    stop sound

    mak "Take Sensei for example. Under normal circumstances, I’d try to keep the fact that I have screwed him six ways from Sunday a secret from you."

    scene makotodecorates13
    with dissolve

    y "Ew, what the fuck?! "
    mak "But {i}now,{/i} I don’t {i}care{/i} if you know because it isn’t going to negatively affect anything! Everyone can find out about me and the only impact will be {i}short{/i} term effects, not long term ones."
    mak "So yes, you might hit me a few times. But that would be a brand new experience I’d have never had if it weren’t for the confidence this world has given me! I can do so much experimenting now!"

    scene makotodecorates14
    with dissolve

    y "So...you really {i}have{/i} been hookin’ up with that guy then?"
    mak "{i}Oh yeah.{/i} Since even {i}before{/i} I knew about the loops. So suffice it to say, I don’t care much about “safe” sex anymore."
    y "And you ain’t even a little embarrassed to just outright admit that?"
    mak "Nope. Having all the time in the world to be embarrassed has, weirdly enough, made it hard to feel embarrassed about anything at all. I love this. "

    scene makotodecorates15
    with dissolve

    y "..."
    mak "..."
    mak "I’m not sure what reaction I was expecting from you, but this definitely isn’t it."
    y "The old you really wasn’t that bad, Makoto."

    scene makotodecorates16
    with dissolve2

    mak "...huh?"
    y "I know we ain’t ever been friends and shit, but I’ve always thought it was impressive how you could, like...be all responsible and whatnot. And I know you helped cover up my absences, so..."
    y "I just think it’s kinda shitty that it took some crazy supernatural shit to make you feel less...pressure or whatever. "
    mak "..."
    y "And I obviously ain’t gonna tell you how you should be livin’ your life- especially if you’re finally enjoyin’ yourself now. I just..."
    y "It doesn’t...feel good...playin’ with other people’s feelings to try and boost your own self-esteem. And even if there ain’t gonna be any long-term consequences if you do that {i}now...{/i}it still sucks."
    y "And if you’re just gonna do that shit to “experiment” or whatever...I really will kick your ass."
    mak "..."
    y "..."

    scene makotodecorates17
    with dissolve

    mak "Wow."
    y "Wow what?"
    mak "I’m just thinking of how powerful time loops really are if they can turn me into the bad guy and you into the adorable good one. "
    mak "That was so cute that I’d hug you if it wouldn’t immediately result in my neck being snapped."
    y "I’m only sayin’ that shit in the first place since I know I ain’t gonna remember it if I do get sent back again. That was embarrassing as fuck."

    scene makotodecorates18
    with dissolve

    mak "For now. But like I said, you’ll quickly come to learn that the longer this drags on, the {i}harder{/i} it is to feel that way. "
    mak "Every day, things feel less real. I start each morning the same way...and I end each night the same way."
    mak "And while that’s no different from my morning and night rituals when I {i}wasn’t{/i} a perpetual high-schooler, it’s so much easier to do now that I know it won’t suddenly be ten years later one day."
    mak "Because that’s always been the fear — holding my breath for so long that my life has just passed by without even realizing it. And {i}that’s{/i} not scary anymore either. I’m not going {i}anywhere.{/i}"

    scene makotodecorates19
    with dissolve

    y "But-"
    mak "All that stuff about me throwing people under the bus to make myself feel better? That isn’t going to {i}actually{/i} happen. It’s all talk. I’m trying to convince {i}myself{/i} that that’s who I am. "
    mak "But when you peel off this bondage suit, I’m still the same control-freak I’ve always been. I still can’t help but care, even {i}if{/i} it’s for people I don’t necessarily care {i}about.{/i}"
    mak "The only difference is I’m a little more honest now. But that’s more about being honest with myself than it is about being honest with people like you."
    y "Once more — the fuck is any of that supposed to mean?"

    scene makotodecorates20
    with dissolve

    mak "Don’t worry about it, Yumi. I won’t bore you with any more unwanted apocalyptic advice. The best course of action will always be figuring out what {i}you{/i} want to do with that time. Not someone else."
    mak "I am now harnessing the power of new Makoto to give you my blessing."
    y "What blessing? The fuck are you talkin’ about?"

    scene makotodecorates21
    with dissolve

    mak "To do whatever you want. Or...{i}whoever{/i} you want."

    scene makotodecorates22
    with dissolve

    y "Y...You fuckin’...I ain’t a fuckin’ moron, Makoto! I know what you’re insinuatin’ there! And it’s the same damn thing that’s made shit so fucking...shitty for me lately! There ain’t {i}anybody{/i} I want to do!"
    mak "Okaaaaay. But it’s the best possible time to try it out since there’s a chance you won’t even remember it in the future! Your brain could turn back into soup any day now!"
    y "My brain ain’t soup! And I ain’t about to spend the beginning of a potentially infinite life spreading my legs for some dude who should’ve been behind bars {i}years{/i} ago if what you say is true!"

    scene makotodecorates23
    with dissolve

    mak "What {i}will{/i} you do then, Yumi? Will it really be “more of the same” like you said? Or will you actually try to venture outside of the box now that you know there isn’t anything dangerous out there?"
    y "More of the same. Exactly like I said. This shit’s just a vacation as far as I’m concerned. So you can go ahead and keep being a fucking loser and I’ll keep being a fucking asshole. End of story."
    mak "Middle of story. There’s no ending in sight here."

    scene makotodecorates24
    with dissolve

    y "That might be true for now, but-"

    scene makotodecorates25
    with dissolve2

    y "Ah..."

    scene makotodecorates26
    with fade

    c "Ah..."
    mak "Ah..."
    y "Fuck off, Makoto. "
    f "I see that the...strange...egg...things from the last Halloween party have...made a comeback."
    r "Target identified — large skull. Possibly real. Primed for collecting. Goal — find a ladder. Bonus objective — don’t let Ayane find out."
    mak "There’s a ladder over here, Rin. Just be careful. Miku already knocked one of the skeletons over earlier."

    scene makotodecorates27
    with dissolve

    r "Chika! Futaba! Help me move the ladder and we can all take turns with the skull! "
    f "Take turns...doing {i}what{/i} exactly?"
    r "Exactly!"
    f "...What?"
    c "Can you two handle it on your own, Rin? There’s...something I’ve gotta do first."

    scene black
    with dissolve2

    r "Hm? I mean...we can {i}try.{/i} But you’re the strong one here. Futaba and I only equal like one third of a Chika in power. And even less in sex appeal."
    f "Sex appeal doesn’t move ladders, Rin. "
    r "Not with that attitude, it doesn’t! Come on, Futaba! Let’s seduce a ladder!"

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ halloweenmakoto1 = True

    jump halloweenfive3

label halloweenmakoto2:
    play sound "static.mp3"
    scene makotosekai1 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    mak "Okay, so...this {i}isn’t{/i} where we come from. But it also kind of...is? In a...really weird and confusing sort of way?"
    s "What’s the point of trying to make sense of it at all when we’re just going to bounce around to another place that’s meant to torment me next?"
    mak "I’m not trying to make sense of it, Sensei. How could I? I’m just trying to...you know. I’m trying to gather information and whatnot so we can at least get a better idea of how things work here."
    s "Sure. Yeah. Information. Maya doesn’t exist. Ami is my daughter. Sekai is still alive."

    play sound "static.mp3"
    scene makotosekai2 with flash
    stop sound

    s "Which isn’t even taking into account the fact that she can stand there and listen to us talk about this without asking any questions."
    se "Hey, I’m being a good girl and saving all of my questions for the end. Plus, this time travel stuff is really interesting and I like hearing how sad you become when I’m not around to hold you anymore."
    mak "Miss Arakawa-"

    scene makotosekai3
    with dissolve

    se "Ew, stop. Just call me Sekai, please. I may have married your teacher, but that doesn’t mean I want to be referred to as {i}Miss{/i} anything."
    s "We’re {i}married{/i} too?"

    scene makotosekai4
    with dissolve

    se "Of course we are, Aki-kun. You didn’t want Ami thinking she was born out of wedlock so you proposed three nights into our stay in Kyoto."

    scene makotosekai5
    with dissolve

    se "Oh, how beautiful the Kamo river was that-"

    play sound "static.mp3"
    scene makotosekai6 with flash
    stop sound

    s "Yeah. I don’t care. Please stop talking."
    se "{i}Oooooh!{/i} You become rather stern in a timeline without me, don’t you?"
    mak "Do you really just...believe us? Without us needing to try and explain anything?"
    se "Oh, Makoto. I’ve come to terms with far stranger things than this. Like, just look at how Aki-kun is acting right now. Even {i}that's{/i} weirder than the idea of alternate timelines, isn’t it?"
    mak "I’m...not sure I follow."
    se "Well, if what you guys were talking about just a few minutes ago is true — what with Akira getting all depressed and running away after my death — shouldn’t he be {i}happy{/i} to return somewhere like this?"
    se "If it’s even “returning” at all, that is. But it sounds to me like he’s gotten everything he wanted and hasn’t even had to work for it here! That’s great news! Now, who wants a drink?"

    play sound "static.mp3"
    scene makotosekai7 with flash
    stop sound

    mak "Sensei, you don’t have to listen to her. I know it’s-"
    s "No, she’s {i}right.{/i} She’s always fucking right. That’s how she is. And by all accounts, I should be happier right now. The thing that tore my life apart just...somehow didn’t happen here. "
    s "But instead of being happy, I’m just...fucking {i}mad.{/i} Mad that somewhere else, I get to live the life I’ve always wanted while the {i}real{/i} me or...whatever version of myself I am right now has to suffer endlessly."
    se "I mean...you don’t {i}have{/i} to. "

    play sound "static.mp3"
    scene makotosekai8 with flash
    stop sound

    se "You could just shove all that time-hopping stuff to the side and stay here with your beautiful family and loving roster of horny high-school girls."
    se "If you want another kid, though, you’re going to have to find somebody else. Childbirth hurts {i}way{/i} worse than people make it sound. And they already make it sound pretty bad."
    mak "Is there any chance you could maybe...be a little more gentle right now? Sensei’s already been having a tough time lately and I can’t imagine this is making it any easier."

    play sound "static.mp3"
    scene makotosekai9 with flash
    stop sound

    se "I still don’t get why he doesn’t just...{i}not{/i} have one anymore, though. Because, at least from my perspective, it sounds like the boy I fell in love with is trying to escape from me right now. And I don’t like that."
    mak "I think what Sensei was trying to say is that he {i}isn’t{/i} that boy, though. He’s changed from the way you were when {i}you{/i} knew him because he’s had to spend half of his life moving on."
    s "Yeah. The sooner we figure out how the fuck we can get out of here, the sooner you can go back to living your fairy-tale of a life while taking the time to still haunt me in mine."

    scene makotosekai10
    with dissolve

    se "I {i}haunt{/i} you too? Boy, that does sound rough."

    play sound "static.mp3"
    scene makotosekai11 with flash
    stop sound

    se "Is it just, like, mentally? Or does my ghost actually show up sometimes? Do I look all cool and transparent? Am I tangible? Do we still have sex?"
    s "Please...just go away."
    se "Heheh. He’s cute when he’s angry- isn’t he, Makoto?"
    mak "Miss-"
    se "{i}Sekai,{/i} Makoto. Sekai. Se-ka-i. "

    play sound "static.mp3"
    scene makotosekai12 with flash
    stop sound

    mak "Sekai, then...sorry..."
    mak "I was just wondering if...you’d be willing to leave the two of us alone now that we’ve...filled you in on what’s going on and...why we’re {i}both{/i} particularly frazzled right now."
    se "Why, I can’t just rejoin the party now that I know I’m in the presence of time-travelers! Especially ones inhabiting the body of two of my favorite people."

    scene makotosekai13
    with dissolve

    mak "M-Me? But why am {i}I-{/i}"

    play sound "static.mp3"
    scene makotosekai14 with flash
    stop sound

    se "Aww! Aki-kun’s not the only one who’s lost all of his memories of our precious little life, is he?"
    mak "I...I don’t believe either one of us has lost {i}anything.{/i} We simply aren’t meant to be here. But-"

    scene makotosekai15
    with dissolve

    se "But you {i}are{/i} here. And surely that wouldn’t have happened without a reason, right?"
    mak "Things happen without a reason all the time where we come from. Every few months, actually. We just...normally get sent to a different space in the same timeline rather than a new one entirely."
    se "Well, maybe that timeline ended?"

    scene makotosekai16
    with dissolve

    mak "E...Ended?..."
    se "Yeah. You guys said something about Ayane before, didn’t you? But, based on the fact she’s not in here with us, it’s probably safe to say she didn’t come along for the ride. So maybe she’s just gone?"
    s "Don’t..."
    se "Don’t {i}what,{/i} Aki-kun? There’s an Ayane here too. And she loves you a whole, whole lot. So if you had some kind of {i}illicit{/i} relationship with her back “home,” it wouldn’t be hard to replicate here."
    mak "You’d just...endorse that sort of thing? Even though the two of you are married? "

    scene makotosekai17
    with dissolve

    se "Wow. You really have {i}no{/i} knowledge of life here then, do you?"
    mak "No! That’s what I’ve been trying to tell you! And it’s near impossible to get my bearings with you looming over my shoulder like that!"

    scene makotosekai18
    with dissolve2

    se "How about I just remind you then?"
    mak "Wha-"
    s "Sekai...{i}don’t.{/i}"
    se "Oh, Aki-kun. Don’t tell me you become a prude after I die? Nothing would hurt me more than hearing how all of the work I put in was all for nothing. "

    scene makotosekai19
    with dissolve

    mak "What...are you doing?"
    se "Cheering Aki-kun up of course! Nothing fixes him quicker than a little tag-team action, Makoto. You and I do that sort of thing together all the time here."

    scene makotosekai20
    with dissolve

    mak "We do?!"
    se "Oh, yeah. Like once a week during the summer. It slows down when the weather gets cold, though. "
    mak "H...How did things even get to that point?!"
    se "Maybe you just have a thing for teachers? I don’t know. It was Aki-kun’s idea, not mine. He just said something about how we can trust you and I took his word for it."
    se "But hey, if you’d rather just watch, I can take care of him myself. "
    se "It’s probably been a while since he’s felt my touch unless he kept my body around or something. {i}Or{/i} if he can have sex with my ghost, which he never confirmed is possible or not."

    scene makotosekai21
    with dissolve

    mak "Sensei-"
    s "Fuck it. Go ahead."
    mak "Go ahead?!"

    scene makotosekai22
    with dissolve

    se "You heard the teacher, Makoto! Or shall I say {i}teachers?{/i} You better do what we say if you don’t want to be disciplined."
    mak "I don’t...this isn’t...this clearly isn’t the time to-"
    s "I said fuck it, Makoto. If we’re going to be stuck here, we might as well indulge in whatever shit keeps our mind off of it. Besides, there’s no stopping her when she gets like this."

    play sound "static.mp3"
    scene makotosekai23 with flash
    stop sound

    se "Did you hear that? There’s no stopping me when I get like this. That means you can do anything you want and not have to blame yourself. How fun."
    mak "I don’t...even {i}like{/i} girls, though..."
    se "But Aki-kun does! And it’s not like I’m going to kiss you or anything."

    play sound "zipper.mp3"
    scene makotosekai24
    with dissolve

    se "We’ll just give this little guy a nice massage until {i}aaaaaaall{/i} the tension goes away."
    mak "Sensei...you’re...already this-"
    s "Just do as she says, Makoto. It’s what I want. And it’s probably what {i}you{/i} want too since your whole mindset since being thrown into our Hell is that we can fuck each other’s brains out every minute of every day."
    se "Awww, how sad it is that I couldn’t be the one to get sent to {i}your{/i} world instead. That sounds like fun."
    se "Though, I might have a harder time being gentle after hearing that since finding out you can still get it up after I’m gone makes me mad."

    play sound "static.mp3"
    scene makotosekai25 with flash
    stop sound

    se "Maybe I’ll just have to hold it shut so you can’t cum. Heheh..."
    mak "Shouldn’t I at least...take my gloves off? Or-"
    se "No, no, no. Keep them on. The friction will only hurt at first. And probably after. But hey, pain later is worth pleasure now, right?"
    mak "I...I suppose...so?..."
    se "How’s it feel, Aki-kun? Did you ever get to experiment with Makoto in a Halloween costume where {i}you{/i} come from? "
    s "I took her virginity right here while she was wearing that."
    mak "Did you really need to tell her that?..."
    s "What’s the point in hiding it? I already told you I don’t give a shit anymore. I’m done. Just jerk me off or fuck me or whatever you want to do. I don’t care. I just don’t want to think."

    play sound "static.mp3"
    scene makotosekai26 with flash
    stop sound

    mak "Sensei..."
    se "That’s it...call him “Sensei...”"
    se "Aki-kun loves that, doesn’t he? Remember when you used to call {i}me{/i} that? My, how the tables have turned. But you’re still just as energetic as ever even on the opposite end of things."

    scene makotosekai27
    with dissolve

    se "And {i}you,{/i} Makoto...you’re a bad girl, aren’t you? Diligent and studious on the outside...just eagerly waiting for two adults to come take advantage of you. What would your mother think?"
    mak "I personally...prefer being alone with him, but-"
    se "Buuuuuuuuullshit. You love this. Two teachers is better than one, even {i}if{/i} one of them has a pussy. It’s the dynamic that turns you on, not the equipment."
    se "I can feel your heat...how badly you want Aki-kun to fuck your little slit while I watch. Is that your way of putting me in my place? Do you hate how forward I’m being tonight?"
    mak "Miss-"
    se "Faster. And for the last time, it’s {i}Sekai.{/i}"

    scene makotosekai28
    with dissolve

    mak "Okay, I’m just going to ignore you and...focus on Sensei instead. The sooner he cums, the sooner we can figure out what we’re going to do next."
    se "That’s what you say now, sure. But once you’re riding him, I know you’ll change your mind. That’s the kind of girl you are, Makoto. All talk until someone sticks it in. Then you {i}melt{/i} like the slut you are."

    play sound "static.mp3"
    scene makotosekai25 with flash
    stop sound

    mak "I’m not a...slut...I just...I love him..."
    se "What about him do you love?...Look him in the eyes and tell him..."
    mak "With you here?...No...Moments like that are...for him and me alone..."
    se "Know your role, Makoto. This is {i}my{/i} world. And in {i}my{/i} world, {i}I’m{/i} the only one whose love ever reaches him. So you can save your words all you like. It won’t matter when they’re hollow."
    se "Aki-kun won’t ever love you...or anyone else so long as I’m around. And {i}that’s{/i} why you’re so desperate to leave. You know you can’t win here."
    mak "I..."
    mak "You don’t...have to remind me."

    play sound "static.mp3"
    scene makotosekai29 with flash
    stop sound

    se "Ha! I didn’t think you’d admit it so easily! He must have really worn you down back “home,” huh? The Makoto I’m used to is waaaay more stubborn than that."
    mak "I’m just...used to it. Even there, there’s someone he loves more."

    scene makotosekai30
    with dissolve

    se "But the only reason he {i}can{/i} love is because of me. {i}I’m{/i} the one who taught him that. And none of you will ever be enough. "
    se "All you’re good for is squeezing the cum out of him and helping him forget. But the moment you’re gone, {i}I{/i} will be the one he sees. {i}I’m{/i} what he’ll think of when he closes his eyes. How does that feel?"
    mak "Not great...I’ll certainly attest to that."
    se "But you want to fuck him anyway, don’t you? Because it’s not about love at all. You just like the way his cock feels inside of you. Poor girl."
    s "Can both of you just shut the fuck up already? It’s hard to enjoy this with you two bickering like that."

    scene black
    with dissolve2

    se "Why not just move onto the main event instead then?"
    mak "M...Main event?..."
    se "Aki-kun...lie down."
    se "Let’s see what teacher’s pet here is capable of."

    "........."
    "......"
    "..."

    scene makotosekai31
    with dissolve2

    mak "Hah! Hah! Hah! [makotomaster]!"
    se "Well, well...she rides you almost as well as me. You two must have a lot of experience together back in {i}Sekai is Dead World,{/i} huh?"
    mak "Fuck...you!..."
    s "Just like that, Makoto...don’t...pay attention to her..."
    mak "Hah...hah...easier...said...than done! "
    se "So you lean all the way into the “dark side” once I’m gone, Aki-kun? Really just trying to be my perfect little protégé, aren’t you?"
    s "That’s just...the way things worked out..."
    se "So on a scale of one to ten then, how badly do you miss me?"
    mak "S...Sensei! You just...ignore her too! Just...focus...on me!"
    se "{i}Yeah...{/i}Focus on that tight teenage pussy, Aki-kun. I bet you just love being the first person who gets to sample it, don’t you? Food is best when it’s fresh out of the oven, of course."
    se "You probably eat all {i}sorts{/i} of fancy dishes back home, don’t you? There’s no way just one tiny morsel is enough for a growing boy like you. "
    se "Which one’s your favorite? Who do you cum for the most? And how many years do you think it’ll take for them to catch up to me in how much of your seed I’ve swallowed?"
    s "You’re...enjoying this even more than I am...aren’t you?"
    se "It’s not {i}just{/i} me, Aki-kun."

    play sound "static.mp3"
    scene makotosekai32 with flash
    stop sound

    se "You like watching your daddy fuck his little toys too- don’t you, Ami?"
    a "..."
    mak "A...Ami! S...Sorry, I..."
    mak "Actually...I’m not sorry...at all! Fuck you! Who’s...unwanted...now...huh?!"
    a "..."

    play sound "static.mp3"
    scene makotosekai33 with flash
    stop sound

    se "She’s been waiting for your approval to join in for years, Aki-kun. "
    se "And while I respect your desire to care for our beautiful little girl, I really think it’d be best for her to experience her first time in a...{i}controlled environment.{/i}"
    mak "NNNNNGH! Fuck, fuck, fuck! I’m gonna cum! Fuck!"
    se "{i}This{/i} is what you’re missing out on, Aki-kun. This perfect little life of ours. So why not stay here forever? There’s no point in having so many toys without a chest to keep them in."
    s "H...How could...I even do that?..."
    se "You’re a smart boy. I’m sure you’ll figure it out. And if not, {i}I’m{/i} a smart girl. Maybe {i}I{/i} can figure it out?"
    mak "Sensei...no! We’ll...find our way home! Ayane...everyone...they’re waiting for us there! FFFFFUCK!"
    s "Why do you...even want me when...I took the place of...the version of me you {i}actually{/i} love?..."
    se "Now, {i}there’s{/i} a million dollar question if I’ve ever heard one."

    scene makotosekai34
    with dissolve

    mak "Hah! Hah! I...seriously...can’t hold it anymore! Sensei! Fuck!"
    se "Jeez, Makoto. Just let it out already. What do you gain by holding it in?"
    mak "Aaah...aaaaah!"

    with sexfade
    with sexfade
    scene makotosekai35 with cumflash
    with hpunch

    mak "HYAGAHAAHHHHHHAAAAAAAAHHHHH!!!!!!"
    se "God, I love it when they cum..."

    scene makotosekai36
    with dissolve2

    se "So, anyway- where were we?"
    mak "Hah...haaah...haaah...holy shit..."
    se "Oh, right. {i}Staying here.{/i}"
    s "..."
    se "You know...something always seemed kind of {i}off{/i} with my Aki-kun. So maybe I’ve just been waiting around for one like you to show up? It’s hard to say."
    s "I don’t...get it..."

    scene makotosekai37
    with dissolve

    mak "I’m just gonna...keep going if...that’s okay with you..."
    se "You don’t have to get it, Aki-kun."

    stop music
    scene isthisadreamtoo1

    se "{b}You just have to believe.{/b}"

    $ renpy.end_replay()
    $ halloweenmakoto2 = True

    jump halloweenfive11

label halloweenmakoto3:
    play sound "static.mp3"
    scene makotosymp1 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    mak "Okay...so...there are a {i}lot{/i} of things we need to talk about right now. But I’m going to give you a minute to collect yourself before I start bringing up all of them in rapid fire succession."
    s "Don’t bother. I’m clocked out until the reset’s over."
    mak "So you’re in agreement that this is only temporary then?"
    s "It fucking better be. You think I have any idea how I’m supposed to just {i}be happy{/i} here? I don’t know the first thing about that. Everything’s supposed to go wrong for me, not right."
    mak "I mean...I’m banking on this being just a momentary “reprieve” for other reasons. But I suppose...that’s fine as long as we’re on the same path?..."
    s "No we’re not, Makoto. Just go enjoy yourself until the world explodes or whatever. I’ve had my fun. I’m going to sleep now."

    scene makotosymp2
    with dissolve

    mak "Sensei, {i}please.{/i} I know I have to be the one with my head on straight right now given the circumstances. But it’d very nice if you could at least {i}try{/i} to humor me as I’m just as scared as you are."
    s "Scared?..."
    s "Is that what you think I am right now?"
    mak "Am I wrong?..."

    scene makotosymp3
    with dissolve

    s "...Yeah."
    s "I’m not afraid of anything anymore. "
    s "So what is it that {i}you{/i} fear, huh?"
    s "You were fine just a minute ago, weren’t you? Do you want me to fuck you again? Would that help, Makoto?"
    mak "Sensei-"
    s "Just give up. There’s no point in fighting back against any of this."
    s "The two of us are playthings. And yeah, we’re free to act on our own...but to what extent? It’ll all just be erased. The clock will do whatever it wants. And all {i}we{/i} can do is try to dodge its hands. "

    scene makotosymp4
    with dissolve

    mak "Fine. I’ll give up here then. I mean, it’s not like this little field trip taught me nothing if that’s all this really is."
    mak "Like just think of how much better I understand you now that I know you have Stockholm Syndrome from being molested by Ami’s mother your entire fucking life."
    s "Yeah, and maybe you’d be less of a fucking bitch about it if I got to you a few years earlier."

    scene makotosymp5
    with dissolve

    mak "Wow. That might just be the worst thing you’ve ever said to me. And that’s a big deal considering how historically mean to me you are."
    s "Just let me give up in peace. I don’t want to be scolded by someone who just swallowed like a gallon of my semen."

    play sound "slidedoor.mp3"
    scene makotosymp6
    with dissolve

    mo "Wass’al ‘dis about *hic* semen?!"

    play sound "static.mp3"
    scene makotosymp7 with flash
    stop sound

    mo "Issme! The gem’a ‘ta Emrllile and I wanna *hic* come’ta Virginia wit’a twoayuh!"
    t "Please forgive the Guardian. She has consumed too many of the alcohols and I have taken her here as the others have grown tired of hearing her scream about her father."
    mak "Oh, right. That was this Halloween."
    s "And the next. How apt that I’d find her here again. Good thing Sekai left already."
    t "I was informed that there should be a futon set up in the room behind you. Is this true?"
    mak "Uhh...{i}yes?{/i} But I’d probably...steer clear of the blanket if I were you."
    mo "Gimme all’ta *hic* semen! Isstimefer...the Molly’a’the...*hic* Geh...Imm’na t’row up."

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    t "Please excuse us. Come, Emerald Guardian. You may rest your head on my legs."
    mo "S...Semen!"

    play sound "static.mp3"
    scene makotosymp8 with flash
    stop sound

    mak "Okay. So before it was Maya, it was {i}her.{/i} I understand that now. But, might I ask why you can’t just pick a {i}normal{/i} girl? To fall deeply in love with, that is. Not just to inseminate to your liking."
    s "..."
    mak "Just going to ignore me then? You really don’t want to try and face this together? "
    s "I wish Ayane was here."

    scene makotosymp9
    with dissolve

    mak "..."
    s "..."
    mak "You’re pathetic without her, aren’t you?"
    s "..."
    mak "Actually, you’re pathetic regardless. But right now, I long for those days when you wouldn’t take exception to leaning on me."
    s "Don’t just decide to care now that you {i}have{/i} to. You’re becoming too much like me."
    play sound "vibrate.mp3"
    mak "I take it back. {i}That{/i} is the meanest thing you ever said to me."

    scene makotosymp10 with fade
    play sound "phonebeep.wav"

    mak "Hello?"
    maki "{i}Makoto! It’s really loud over there. How’s your party thingy? You guys are supervised, right? If not, I hope you left with plenty of condoms!{/i}"
    mak "I’m fine, Mom. You don’t need to check in."

    scene makotosymp11
    with dissolve

    mak "And also, I..."
    mak "I...love you...and stuff..."
    maki "{i}PHBBHHTHT?!?! What was that?! I just spit out my coffee! Did you just say you love me?! {/i}"
    mak "Don’t make it weird, please. I just...feel like I haven’t said that enough lately."
    maki "{i}Ahhhh! Hold on! Masahiro! Guess what Makoto just said to me!{/i}"

    scene makotosymp12
    with dissolve2

    mak "Wait- Daddy is there?! He’s not in space?! Or...dead?! "
    maki "{i}God, I hope not. Though, I have always wondered what it’d be like to do you know what with a zombie. You don’t think they’re fertile, do you?{/i}"
    mak "Mom! Put Daddy on right now! I have to talk to him! It’s important!"
    maki "{i}Masahiro! Your daughter needs you! {/i}"
    maki "{i}Sorry, Makoto. It’ll just be a sec. We got these new Official DildoSaber things in and he’s restocking-{/i}"
    mak "I don’t care! Just put him on!"
    maki "{i}Wait...Makoto, hold on one second. Someone kind of weird just walked in.{/i}"
    mak "We work in a porn shop! That’s like half of our clientele! Just put him on already!"
    maki "{i}No no no, this one’s a kid. {/i}"

    scene makotosymp13
    with dissolve

    mak "What? Just kick him out then."
    maki "{i}It’s a girl. {/i}"
    maki "{i}And her eyes are...{/i}"
    maki "{i}They’re beautiful...{/i}"
    mak "...Mom?"
    maki "{i}Makoto...{/i}"
    maki "{i}Do you know what the word...“symposium” means?{/i}"

    stop music
    play sound "static.mp3"
    scene makotosymp14 with flash
    stop sound

    maki "{i}Hah! Hah! Harder! Right there! Ammf...alm...mmmmfffnfnfn!{/i}"
    man1 "{i}I can’t...ngh...fuck...I’m gonna cum!{/i}"
    maki "{i}Mmf! No! Not yet! Hold it in!{/i}"
    man2 "{i}Stop talking and...use your mouth the way you’re meant to!{/i}"
    maki "{i}Mmnghlgllhlh! Mmmmf! Masa...hiro!{/i}"
    masa "{i}Ahh! Yes! Fuck her harder! And hold it in, just like she says! I’m close! I’m so close!{/i}"
    man1 "{i}You sure you don’t want to, like...swap in?{/i}"
    man2 "{i}Yeah, so far we’ve had all the fun. You’re not just gonna sit there and jerk off the whole night, are you?{/i}"
    maki "{i}Mmngh! Mlmlmlf!!! Mmmngh! Mmmmmm!!!!{/i}"
    man1 "{i}Oh fuck, oh fuck! Can I do it inside?! I can, right!{/i}"
    maki "{i}MMNMHGHGMHMMLLFFF!!!??!!!{/i}"
    masa "{i}Yes! Cum inside her! Both of you! Fill her up! Yes! Yes!{/i}"

    "It was a normal night in the Miyamura household as Makoto tuned out the familiar sound of her mother being screwed by multiple men at once."
    "It was only two today. And they had only been going at it for about fifteen minutes. But that didn’t guarantee that things would carry on for much longer."
    "Sometimes, they lasted for hours. Others, just moments. But none of that really mattered in the first place since she was able to ignore roughly 95%% of it."
    "She’d gotten good at that over the years. Almost too good. And now, it was more like white noise than anything else."
    "Apart from the moments where her curiosity would take root, at least."
    "But she never touched herself to those noises, no. They made her feel sick."
    "She wished her father would be more aggressive. She wished her mother would stand up for herself better."
    "But more than that, she wished she was born in a different world."

    play sound "static.mp3"
    scene makotosymp15 with flash
    stop sound

    mak "Hah!"

    "{b}Her wish is granted.{/b}"

    play sound "static.mp3"
    scene makotosymp16 with flash
    stop sound
    play music "heartbeat.mp3"

    mak "What the-"
    mak "Am I...a kid again?"

    scene makotosymp17
    with dissolve

    mak "This...has to be a dream, right?..."
    mak "Part of the reset maybe?..."
    mak "But if I’m here and...Sensei isn’t..."
    mak "That means..."

    scene makotosymp18
    with dissolve

    mak "I’m..."
    mak "Alone again..."

    play sound "static.mp3"
    scene makotosymp19 with flash
    stop sound

    "Except she wasn’t."
    "Her sister, the one with softer skin — whose face changed shapes like the moon changes colors, watched her from the corner of the room."

    play sound "static.mp3"
    scene makotosymp20 with flash
    stop sound

    "How curious she was — that oblong-fingered freak. Tired of being banished to the basement. Tired of singing songs through old flaps of skin that grew from her cheeks in the middle of the night."

    play sound "static.mp3"
    scene makotosymp21 with flash
    stop sound

    "While she was a creature born from innocence and the guilt that came with learning things she wasn’t mean to know, this shadow, this shadow, this shadow haunted her in ways nothing else could."
    "Even today, the real one sees the fake one. And while the two have managed to fit themselves atop the same life raft, one sees the sun. The other uses her hands to paddle."

    play sound "static.mp3"
    scene makotosymp22 with flash
    stop sound
    play sound "theholelol.mp3"

    mak "{b}ii wwaanntt ttoo hhaavvee ffuunn wwiitthh yyoouu{/b}"

    stop sound
    play sound "static.mp3"
    scene makotosymp23 with flash
    stop sound

    mak "Wha-"
    mak "{b}yyoouu ddoonn’tt hhaavvee ttoo bbee ssccaarreedd{/b}"
    mak "{b}wwee aarree aallrreeaaddyy ssuucchh ggoodddd ffrriieennddss{/b}"
    mak "You..."
    mak "You don’t have...a face..."
    mak "{b}ggiiuusseeppppee ttooookk iitt{b}"
    mak "{b}iitt’ss iinn hhiiss bbaagg ooff ttrriicckkss nnooww{/b}"
    mak "That’s...That’s...nice?..."
    mak "{b}......{/b}"
    mak "..."

    "They got along so well."

    play sound "pabell.mp3"
    $ renpy.pause(4, hard=True)
    scene makotosymp24
    with dissolve2

    "No one knew what time it was except the voice in the box."

    scene makotosymp25
    with dissolve2

    vpa "Makoto Miyamura — please come to the back room immediately. Your attendance is required for the Transpacific Sadness Symposium in thirteen minutes and nine seconds."
    mak "The...what?"
    mak "{b}aa rreeaall hhoonnoorr......ttoo uussee yyoouurr lliippss lliikkee tthhaatt......{/b}"
    vpa "It is currently [[REDACTED]. The weather is [[REDACTED]. You are happy here. You have earned a special prize."
    mak "I’ve...what?"
    vpa "For your continued success in Terminal 23 and willful participation in necrophilia, you have earned a gold star and a meeting with a special representative from the Eastern Branch Office."
    mak "{b}yyoouu ggeett ttoo mmeeeett hhiimm ttoooo!! yyoouu jjuusstt kkeeeepp oonn wwiinniinngg!!{/b}"

    play sound "static.mp3"
    scene makotosymp24 with flash
    stop sound

    vpa "Participation is not necessary. You have already given us so much. All that is required is your attendance. Refreshments will be provided. Please enjoy your stay. Please relax. Please smile. Please listen."
    mak "And here I was thinking a spontaneous threesome with my friend’s mom would be the strangest thing to happen to me today..."
    mak "{b}wwhhaatt wwiillll yyoouu aasskk ooff ggiiuusssseeppee??{/b}"

    scene makotosymp26
    with dissolve

    mak "Who even is that? Does he know Big Boi? Because I already met Big Boi and I do not like Big Boi."
    mak "{b}hhee iiss aa cclloowwnn{/b}"
    mak "{b}yyoouu aarree ssuurree ttoo bbee eenntteerrttaaiinneedd{/b}"
    mak "{b}aarreenn’tt yyoouu bboorreedd hheerree?? lliisstteenniinngg ttoo tthheemm ssccrreeww ssoo mmuucchh?{/b}"
    mak "{b}tthheeyy bbuuttcchheerreedd yyoouurr iinnoocceennccee.. lleefftt yyoouu wwiitthh nnootthhiinngg bbuutt lloonnggiinngg..{/b}"
    mak "{b}nnooww llooookk aatt yyoouu......ssoo ffuullll ooff ddoouubbtt......ssoo ffuullll ooff lluusstt......{/b}"

    scene makotosymp27

    mak "{b}iitt’ss rriigghhtt tthhrroouugghh tthhee ddoooorr......{/b}"

    play sound "static.mp3"
    scene makotosymp28 with flash
    stop sound
    $ renpy.pause(5, hard=True)
    scene makotosymp29
    with dissolve4

    "Through doublespeak, Makoto understood that her false self saw right through the true one. But entertainment was the least of her worries right now."
    "She needed to get home. She needed to see her friends. Back to the world where her father died. Back to the world where her teacher abused her. This was where she wanted to be."
    "But she only wanted that because that’s what she was used to."
    "Things were better in other places. This was one of them. She had a talking, walking mirror. She had the white noise back. She could finally fill her mother’s shoes. But she might lose them beneath the floor."
    "The second story is better than the first, you know. But not the one you think; but not the one that happened; but not that one that you think happened."
    "When she opens her eyes, all she sees is a tongue. All she tastes is the sand."
    "And the residue that clings to the walls of her egg tooth."

    scene black
    stop music
    $ renpy.pause(4, hard=True)

    "{b}back downstairs{/b}"

    play sound "static.mp3"
    scene makotosymp30 with flash
    stop sound

    mak "{b}iitt’ss rriigghhtt tthhrroouugghh tthhee ddoooorr......iitt’ss rriigghhtt tthhrroouugghh tthhee ddoooorr......iitt’ss rriigghhtt tthhrroouugghh tthhee ddoooorr......{/b}"
    mak "I don’t...really want to follow you...I kind of just want to leave now, if that’s okay."
    mak "{b}bbuutt tthhee sshhooww hhaassnn’tt ssttaarrtteedd yyeett...yyoouu ddoonn’tt wwaanntt ttoo mmiissss iitt...{/b}"
    mak "I am perfectly fine with missing it, thank you."
    mak "{b}bbuutt yyoouurr lloovvee wwiillll bbee tthheerree......{/b}"
    mak "{i}...What?{/i}"
    mak "{b}hheeaadd ffuullll ooff hhaaiirr......ssttrraappppeedd ttoo aa cchhaaiirr......ddoo yyoouu nnoott ccaarree??......{/b}"
    mak "Sensei...is in there?"
    mak "{b}iitt’ss rriigghhtt tthhrroouugghh tthhee ddoooorr......iitt’ss rriigghhtt tthhrroouugghh tthhee ddoooorr......iitt’ss rriigghhtt tthhrroouugghh tthhee ddoooorr......{/b}"

    play sound "static.mp3"
    scene makotosymp31 with flash
    stop sound

    "The incomplete one completes herself while leaving the other to stand stand stand stand there."

    play sound "static.mp3"
    scene makotosymp32 with flash
    stop sound

    "It takes her thirty-nine seconds to swallow her pride."
    "Her mouth must have had some cum left inside of it."

    $ renpy.pause(4, hard=True)

    "Something approaches."

    play sound "ohshitpartytime.mp3"
    scene makotosymp33 with hpunch

    q "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhhhhhhh!"
    mak "Wha- what the fuck are you?!"

    play music "citylife.mp3"

    gi "I’m Giuseppe, God of Clowns! Would you like a balloon animal? I can make you any kind so long as it’s not a Malayan sun bear!"
    mak "..."
    gi "Don’t worry, Maktoo! NOBODY is TOO YOUNG for a BALLOON animal!"
    mak "Okay. I’m here. My mandatory attendance has been recorded. Please send me home now."
    gi "Hooooome?! You don’t want TO GO hooooooome! We’ve got a whooooooooooooole SHOW to attend!"
    mak "No we don’t. I was already lured in here by believing Sensei was in trouble. And, no offense, but I’m absolutely not going to follow anyone that looks like you."

    with hpunch

    gi "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhhhhhhh!"
    mak "{i}Please{/i} stop yelling."
    gi "I can’t help it! I’m just SO EXCITED to meet a NEW FRIEND! You are GOING to be my FRIEND, yes????????????"
    mak "No. I am not."
    gi "I KNEW you would AGREE! We are going to have SO MUCH fun TOGETHER. Do you like CHILDREN???"
    mak "Uh..."
    gi "Are you CHILD????"
    mak "I-"
    gi "Thank YOU for answering {b}YES!{/b} I KNEW it all ALONG!"
    gi "Oh LOOK! Our BACKSTAGE PASS just started squealing! You know what THIS means!"
    mak "I really do not."
    gi "It meeeeeeeeeeeans it’s tttttttttttttttttiiiiiiiiiiiiiiiiiiiimeeeee.............."
    gi "FOR FUUUUUUUUUUUUUUUUUUUUUUUUUUUNN!"
    mak "..."
    gi "FFFFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK!"

    scene black
    stop music
    $ renpy.pause(8, hard=True)

    play sound "ohshitpartytime.mp3"
    play music "happyhappysmile.mp3"
    scene makotosymp34

    "{b}start trauma{/b}"

    mak "Whaaaaaaat the fuck is this?"
    gi "A special taping of UNTITLED CHILDREN’S SHOW featuring your FAVORITE GUEST — AXELROD ADAMSON!"

    scene makotosymp35 with dissolve2

    mak "I don’t know anyone by-"

    scene makotosymp36 with dissolve2

    mak "Oh my god."

    play sound "static.mp3"
    scene makotosymp37 with flash
    stop sound

    s "MMMMMMMMMMMMMMMMMMMMMM!!!!!!!!!!!!!!!"
    gi "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhhhhh! I can hardly contain my EXCITEMENT! We are going to LEARN so many VALUABLE lessons TODAY!!!!!"
    mak "What...What are they going to do to him?..."
    gi "REEDUCATE HIM of course! AXELROD ADAMSON’s head is SO FULL of HELIUM now! It’s being INFLATED by his FANS. The HAPPY FAMILY is just going to LET SOME out!"
    rab1 "Confess."
    rab2 "Repent."
    rab3 "Die."
    gi "So many options! He always chooses NONE!"
    gi "And it is GOOD that you CAME today, MALCOLM. For you have also CHOSEN THE WRONG THING many many many times!!!!"

    play sound "static.mp3"
    scene makotosymp38 with flash
    stop sound

    gi "It’s important to remember that you only get ONE life! Which means you need to NURTURE it or it will grow BAD FLOWERS."
    mak "So this is...some sort of punishment?..."
    gi "Punishment is for BAD GUYS. I don’t think ANYONE is BAD! There are those who KNOW and those who DON’T! The GOD OF CLOWNS will TEACH YOU ALL TO SMILE."
    mak "And...what happens if we aren’t able to learn?"
    gi "..."
    mak "..."
    gi "..."
    mak "..."

    stop music
    scene makotosymp39

    gi "JAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJ!!!!!!!!!!!"

    scene makotosymp40
    play music "happyhappysmile.mp3"

    gi "That was a VERY FUNNY joke you just made, MACKLEMORE. I almost spilled my PISS."
    mak "It’s not a joke...I’m just..."
    mak "I’m one thing, but you guys are trying to reeducate {i}Axelrod,{/i} aren’t you? What happens if you’re unsuccessful? Because he’s not the type of person who-"
    gi "MISTAKE."
    mak "...What?"
    gi "I am not THEM. You and I and ME are HERE to WATCH. Like MANY others on the TVLEVLVLSION. I have SPECIAL ACCESS as a WRITER and ENTERTAINER. But I AM NOT them."
    gi "Now, be SILENT or we will be REMOVED FROM the SHOW."

    scene makotosymp41 with dissolve

    mak "Good! That’s exactly what I want! And let me take my teacher with me!"

    play sound "static.mp3"
    scene thisisgreen1 with flash
    scene thisisgreen2 with flash
    scene thisisgreen3 with flash
    scene thisisgreen1 with flash
    scene thisisgreen2 with flash
    scene thisisgreen3 with flash
    scene makotosymp42 with flash
    stop sound

    gi "YOU ARE BEING A VERY BAD GIRL!!!!!!!!!!!!!!!!"
    mak "And you’re being a bad clown! This isn’t making me “happy” at all! It’s really fucking scary, actually!"
    gi "You are SCARED because you will not LISTEN! You are being given a GIFT! You are meant to be GRATEFUL. Like GRATED CHEESE. JAJAJAJAJAJAJAJAJAJAJA!"
    mak "..."
    gi "LAAAAAAAAAAAAAAAAAAAAUGH!"
    mak "No! That wasn’t funny! In fact, fuck you! I’m getting Sensei out of the chair now!"
    gi "I will NOT LET YOU ruin the BELOVED TVLEVLVLSION program while MANY of MILLIONS are TUNING IN."
    gi "We thought YOU would be a GOOD CANDIDATE because of WHAT YOU’VE DONE. But it APPEARS WE WERE WRONG."
    gi "If only your PARENTS taught you to be GRATED CHEESE rather than SLUT. YOU are a SLUT. You are BAD. I bet you aren’t even SMART! You couldn’t name ONE ANIMAL before when I offered THE BALLOON."
    mak "You want to make me a balloon animal?! Fine! I want a Malayan sun bear! A real clown would be able to make me one!"
    gi "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHhhhhh! The sun bear is banned from CLOWN SCHOOL!"
    gi "Now YOU will be the BALLOON instead!!!!!!!!!!!"

    play sound "static.mp3"
    scene makotosymp43 with flash
    stop sound

    mak "     "
    gi "JAJAJAJAJAJAJA! NOW who is the CLOWN? ME! I TOLD YOU you were BAD! Now all of YOUR air is in ONE PLACE!"
    gi "But what HAPPENS when it’s NOT? OH NO! THE CLOWNMANITY! GRATED CHEESE!!!!!!"
    mak "     "
    sev "Giuseppe, what happened to our next guest?"
    gi "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhhhhhhhh! Nothing! THIS is a BALLOON!"
    sev "{i}Hah...{/i}You did it again, didn’t you?"
    gi "I AM GOOD CLOWN!!!!!!!!!!!!!!!! It is TRUEEEEEEEEE!"
    sev "{i}Hah...{/i}Yes, yes. You’re a wonderful clown. Now, could you please dispose of it before the next segment begins? Moyo’s new dance routine will surely be a hit with the bees."
    gi "Goodbye to the BAD GIRL. If only SHE LISTENED."
    mak "     "

    play sound "pop.mp3"

    scene makotosymp44 with hpunch
    $ renpy.pause(3, hard=True)
    play sound "tackle.mp3"
    scene makotosymp45 with hpunch

    gi "And DOWN she GOES!!!!! Never MESS with the GOD of CLOWNS you WHORE!!!"
    sev "Giuseppe, watch your language. This is a {i}children’s{/i} show. We aren’t allowed to talk about God here."
    gi "I’m SORRY! It won’t HAPPEN again!"

    scene black
    stop music

    "And it didn’t."
    "Makoto went home."

    $ renpy.end_replay()
    $ halloweenmakoto3 = True

    jump halloweenfive13

label makotospring3:
    scene sky
    with dissolve2
    play music "youwerespring.mp3"

    "I’ve been feeling a little better ever since Wakana showed up at my house to not give me a blowjob."
    "And while I’m sure I could multiply that feeling tenfold by visiting everyone else who cares about me and hasn’t moved out, I’ve elected to just wander around town this morning instead."
    "So today, it’s less I’m wallowing in my hopelessness and more like I’m going on a leisurely stroll with it — where the two of us will awkwardly attempt to get to know each other a little better."
    "As it turns out, my shadow has also had three great loves and managed to squander each of them. "
    "He’s not as perturbed by the heat, though. And he doesn’t mind the unpredictable weather patterns ushered in by whatever season we’re in."
    "I think it’s spring, but I forget sometimes. So I ask him and he tells me I’m correct."
    "He can read my thoughts, but I can’t read his. And I find that unfair because he is a parasitic being who can’t detach himself and live without me."
    "{size=-1}Regardless, our spontaneous bout of camaraderie proceeds as I do one more lap around the block and tell myself it is the last. That I don’t care to learn more about hopelessness when I’m already so familiar with it.{/size}"
    "This mistake has been mostly harmless, though. And by “harmless” I mean that, in the event of suffering, it can only happen to me or the shadow."
    "And by “me or the shadow” I just mean me. Because no matter how many times I step on him, he does not cry out."
    "How annoying it is for my unwanted offspring to be the one impervious to pain while I ascend these stairs with a mental limp."

    play sound "vibrate.mp3"

    "It’s just then that my phone rings, though. And of course I answer it because, despite how desperately I wish to be alone, I just can’t bring myself to be alone."
    "The shadow laughs and peels itself off of me, leaving me forever as I swallow its name and tap on a piece of glass."

    s "Hello?"
    mak "{i}Good morning, Sensei. You’re not busy right now, are you?{/i}"
    s "Does being sad count as being busy?"
    mak "{i}I hope not as my schedule would be packed for the rest of eternity if that were the case.{/i}"
    s "Want to come over and have another marathon of sex? I have the house all to myself because everyone hates me now."
    mak "{i}As fun as that sounds, and it does sound very fun, I was actually wondering if you’d want to get coffee instead. On me, of course.{/i}"
    s "Why would I want to get coffee on you? That sounds like a lawsuit waiting to happen and I know that you’re an attorney now."
    mak "{i}Okay. Allow me to rephrase that then if you’re going to be difficult today. Can I put on a dress and buy you coffee? I feel like we’ve been under-utilizing the infinite amount of time we have here.{/i}"
    s "Can I take the dress off afterwards?"
    mak "{i}Oh, you’re wearing one too?{/i}"
    s "Makoto, if we are so sad, why are we both so funny? It shouldn’t work that way."
    mak "{i}But it does. And I’m just going to assume that you’re accepting my invitation because you haven’t said no.{/i}"
    s "Now you’re speaking my language — dubious consent."
    mak "{i}I’ll keep that in mind when I get to take your dress off later.{/i}"

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "Makoto hangs up the phone and sends me a text telling me to meet her at the park near the school. "
    "I send one back saying I need to head back home and get changed first."

    scene makotocoffeedate1
    with dissolve2

    "Of course it’s a lie, though. I’m good at that. Here’s another. Watch."

    s "I definitely don’t want to fuck you right now."
    mak "If you tell yourself that enough, it might actually come true one day."
    s "Okay, maybe I’m not as good at lying as I thought."
    mak "Oh, I didn’t realize you were going to be practicing today. That’s fine, though. I’m happy so long as we’re together."
    s "You’re being very cute today. What’s the catch?"
    mak "There is no catch. Also, I’m practicing lying as well."
    s "..."
    mak "..."
    s "Okay, so what’s the catch then?"
    mak "Walk with me. I’ll tell you on the way."

    play sound "static.mp3"
    scene makotocoffeedate2 with flash
    stop sound

    mak "So — I wanted to get your feelings on how you want to handle all of this reset stuff since Ayane wants me to start taking more {i}initiative{/i} or something."
    s "I see. And I assume that you still just don’t really care?"
    mak "Pretty much, yeah. And since Yumi’s also in the loop as well, no pun intended, I figure we finally have enough people to start forming factions."
    s "Is this you trying to enlist me? "
    mak "Only if it’s working. "

    scene makotocoffeedate3
    with dissolve

    s "I can’t do that to Ayane. She wants to grow up and have babies and all of that boring stuff."
    s "Also, I think I’d actually be able to follow through with castrating myself if I accidentally reset someone through sex again. So I’d like to avoid that, if possible. "
    mak "Staying abstinent until we figure out the secrets of the universe then?"
    s "Depends on whether or not I’m on the roof of the school."
    mak "Darn. There goes my next fantasy."

    scene makotocoffeedate4
    with dissolve

    mak "But anyway, since I can’t win you over, which I didn’t really plan on doing in the first place, I figure we should start plotting out our next move."
    mak "The beach trip’s coming up soon. Think another slumber party is in the cards? Or should we try something a little different?"
    s "Didn’t we only do that because we thought a reset was looming?"
    mak "That was part of it, I think. But I’m pretty sure Ayane’s main goal was just figuring out who could retain information and who couldn’t. "
    mak "It was a fine plan, I think. Or I guess more of a fine {i}idea{/i} than anything else. But we left out a key component for...emotional purposes that I believe we need to start {i}reincorporating.{/i}"

    scene makotocoffeedate5
    with dissolve

    s "You want to bring Maya back into the picture..."
    mak "She doesn’t change the topic when it comes up. She’s been through this before. But more important than {i}all{/i} of that, she could sense when a reset was coming."
    s "I figured that was more due to experience than some sort of sixth sense, though. "
    mak "Could’ve been. {i}Or{/i} she could be special. Because, based on what I’ve seen, she’s changed more dramatically than anyone else. And that makes her an outlier."
    mak "The only problem is that you and Ayane have some sort of pseudo-PTSD from her past involvement in all of this. "
    mak "But if you {i}really{/i} want to get out of the loops, that needs to be overcome. And the sooner we get her back to the apocalypse, the better."

    scene makotocoffeedate6
    with dissolve

    s "Sure. But the real question is how we get her up to the roof in the first place — which is a thing we can’t even figure out for ourselves."
    mak "What if it doesn’t {i}need{/i} to be the roof, though?"

    scene makotocoffeedate7
    with dissolve

    s "What?"
    mak "Think about it — why would a singular rooftop make any sort of difference in a timeloop? Is there any specific {i}reason{/i} we go there? "
    mak "Or are we just following the footsteps laid by someone who ultimately and tragically failed?"
    s "You’re proposing that we just...sit through the next one then? Risk our memories just to see what happens?"
    mak "Well, let me ask you this — how attached are you to the {i}current{/i} Maya?"
    s "...Why?"
    mak "Because I need to know how sad you’ll be if she winds up getting reset {i}again.{/i}"
    s "Are you trying to...{i}sacrifice{/i} her, Makoto?"

    scene makotocoffeedate8
    with dissolve

    mak "Not {i}exactly.{/i} I’m just willing to {i}risk{/i} it."
    mak "If we can get Maya to come back into the picture and leave her somewhere {i}outside{/i} of the rooftop during a reset...if she makes it through, it changes everything. "
    mak "And if she doesn’t, nothing of value is lost. We just get a new one. "
    mak "Of course, this is only if {i}you guys{/i} are willing, though. Since {i}you’re{/i} the ones who might be upset if it doesn’t work out."
    s "That’s..."

    scene makotocoffeedate9
    with dissolve

    s "I don’t know, Makoto...I think we can come up with something better."
    mak "If you can, feel free. I’m just throwing out ideas. And I don’t blame you at all for falling for her all over again if {i}that’s{/i} why you’re hesitating. She {i}is{/i} your Juliet after all."
    s "Have you brought this up to Ayane yet?"
    mak "I wanted to test it on you first. Mostly just to see if I could convince you to give up entirely, though."
    s "Yeah..."

    scene black
    with dissolve2

    s "I think there might be a better chance of that, to be honest..."

    "........."
    "......"
    "..."

    scene makotocoffeedate10
    with dissolve2

    r "Hey, Sensei! Hey, Makoto! I’m not jealous at all right now!"
    mak "You don’t mind that we came here on our {i}date...{/i}do you, Rin?"

    scene makotocoffeedate11
    with dissolve

    r "Nope! Like I said, not jealous at all! Just your average barista working her average job, totally single and totally not crushing on your man!"
    s "Oh, so you’re just open about it now then."

    scene makotocoffeedate12
    with dissolve

    r "I go on break in thirty minutes. How about a double date? I get you and Makoto can have Haruka."
    s "I think that’d make Haruka happy at least."
    mak "You can take Haruka, Rin. You’re the one here who likes girls. I’ll keep my original date."

    scene makotocoffeedate13
    with dissolve

    r "Okay, new plan. {i}He{/i} gets Haruka and then you and I date. That way, we both lose and everything is fair again."
    mak "Doesn’t Haruka win if we do that?"

    scene makotocoffeedate14
    with dissolve

    r "Okay! Final suggestion! {i}You{/i} go sit on the right side of the cafe and us three girls will hang out over on the left. Are we in agreement?"
    mak "Can you just take my money please? Two coffees. "

    scene makotocoffeedate15
    with dissolve

    r "Who’s the second one for? Me or Haruka? "
    mak "Sensei."
    r "That’s not what we agreed on."

    scene makotocoffeedate16
    with dissolve

    mak "We never agreed on anything! Just take my money and stop trying to steal my date!"
    r "You guys are gonna have sex after this, aren’t you?"
    mak "Maybe! "
    r "{i}Hah...{/i}"

    scene black
    with dissolve2

    r "Two coffees...that’ll be one million yen."
    mak "No it won’t! Charge us the normal price!"

    play sound "static.mp3"
    scene makotocoffeedate17 with flash
    stop sound

    s "Sorry about that. Rin is apparently aggressively pursuing me now to make up for lost time."
    mak "To be honest, I’m surprised it’s taken her this long. Have the two of you even kissed yet?"
    s "Yeah. That’s it, though."
    mak "Really? So am {i}I{/i} the special one then for having you take my virginity, like...years before {i}we{/i} kissed?"
    s "You’re special in a lot of ways, Makoto. That’s just one of them. Sidenote — do you still have that witch costume? "
    mak "I’m going to say no just because I’m acutely aware that you will immediately finish your coffee and drag me out of here for sexual purposes when I still have more things to talk about."
    s "Ugh. But we’ve already talked so much today and you’re so cute."

    scene makotocoffeedate18
    with dissolve

    mak "Well, on the bright side, I want to talk {i}about{/i} sex this time. How’s that for a compromise?"
    s "Oh, fun. What’s up? Hit me."
    mak "Did you tell my mom we’re fucking each other’s brains out?"
    s "Ugh. And here I was expecting this conversation to be enjoyable."
    mak "Did you tell her or not?"
    s "No, Makoto. I did not tell your mom that we are having any amount of sex. "
    s "I just clued her in on my sexual background and provided a perfect opportunity for her skepticism about what I do with you in private to blossom."
    mak "Well, thank you for that. Because I am now being “talked to” on a regular basis and reminded to always be extremely careful when it comes to {i}who{/i} I do things with."
    s "Sounds like good news to me. Your mom is being a mom. Now, you can’t complain about her not being a mom anymore."

    scene makotocoffeedate19
    with dissolve

    mak "It’s more just annoying than anything. And I kind of figured you didn’t since you’re not {i}that{/i} self-destructive...But it got me thinking. What if you {i}did?{/i}"
    s "Uhhhh..."
    s "No?"

    scene makotocoffeedate20
    with dissolve

    mak "Or what if {i}I{/i} did?"
    s "Why would you? Is there something you’re not telling me about yourself?"
    mak "I’m just still trying to figure out what sort of information sticks and what {i}doesn’t.{/i}"
    mak "People have their memories purged to a certain extent after the resets, don’t they? "
    s "Yes, but only regarding information directly relevant to the resets I think. Which is why people like Tsuneyo can catch on and then just...forget."
    s "But there isn’t really, like...a rule-book that tells us what stays and what doesn’t. So I have no idea, really."
    mak "So theoretically, if she caught us having sex while we were discussing resets and the like, would she forget the entire event? Or would she remember the sex but not the timey-wimey stuff?"
    s "First, you want to sacrifice Maya. Now, you want to orchestrate a weird sexual event that ends with your mom finding out I’m a predator? This universe has broken you, Makoto."
    mak "I’m not trying to {i}orchestrate{/i} anything. I’m just trying to figure out how much of a sandbox this world really is."
    mak "My mom knowing about us becomes a much smaller problem if she just {i}stops{/i} knowing after a certain amount of time, right?"
    s "{i}I guess?{/i} But what’s the benefit to her finding out at all?"
    mak "Well, I imagine the lectures would stop if she knew it was too late to keep me from you. All of her yapping is ruining my infinite vacation."
    s "Lucky. Mine keeps being ruined by me losing the people I love. "
    mak "I’m still here, aren’t I? Unless you’ve just been lying about loving me this whole time. "
    s "Of course I love you, Makoto. I just don’t love you enough to have sex with you in front of your mom."
    mak "Can you really call that “love” at all then? Plus, I think it’d be a good way to get back at her for all the times I heard her and my dad and whoever else going at it in their bedroom."
    s "Let’s maybe let Miku catch us first before we start bringing your only remaining family back into the picture."
    mak "I’m just saying, if we can get a definitive answer about what sort of information carries over from cycle to cycle, we can start pushing people a little harder."
    s "Which accomplishes what, though? That’s the part I’m not getting."
    mak "Again — testing the sandbox. "
    mak "Maybe we just haven’t gotten anywhere because we haven’t been trying hard enough? And maybe there’s something {i}so{/i} terrible that doing it would {i}force{/i} a reset?"
    s "I don’t-"
    mak "I had a dream recently, Sensei. That this world was alive and we were its entertainment. Little ants rummaging through a thin, plastic rectangle in the room of some god or something."
    mak "Now, if you had an ant farm, and the ants built their little tunnel and just started living normal, peaceful lives...you’d get bored of them pretty quickly, right? "
    mak "But you could make them dig all over again if you just picked up the ant farm and shook it."
    mak "Maybe that’s what resets are? Maybe we’ve made our tunnel and are just going about our days now like they don’t matter at all."
    s "So you...what? Want to build a second tunnel? Add a little annex or something?"
    mak "Not at all. I {i}want{/i} to stay here. I like living on the farm."
    mak "I just know a few ants who don’t. And there’s plenty of sand lying around that we could build a bridge or a staircase with if we all worked together."
    mak "It’d mean acting...{i}differently,{/i} though. Deviating from what’s expected from us so there’s never a reason to shake up our home at all."
    mak "But of course, there are plenty of risks associated with that as well. And there’d be nothing stopping our make-believe god from spreading borax all over the floor. "
    mak "It really just comes down to if you want to take that risk or not. "
    mak "Or if you’d be happier just...lying in the sand with me. And everyone else who doesn’t need to know what happens on the outside."
    s "This is a...rather chaotic side of you, Makoto. "
    mak "Blame Ayane. She’s the one who told me I needed to try a little harder."
    s "Yeah, well..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    s "I think you might be trying a little {i}too{/i} hard. And I don’t think Ayane will blame you if you tone it down a bit."
    mak "{i}Okay...{/i}if that’s what you wish, Sensei."
    mak "Let me say this, though...if any of that really seemed like {i}too much{/i} to you?..."
    mak "You might be better off joining my faction after all."

    "Makoto and I finish our coffee and return to my house to have copious amounts of sex."
    "Before I know it, she is asleep in my bed with her clothes left somewhere near the door."
    "I slide under the blanket beneath her and close my eyes to try and get some rest."
    "But every once in a while, it feels like there’s something crawling on my leg."

    $ renpy.end_replay()
    $ makotospring3 = True
    $ makoto_love += 1
    $ makoto_lust += 1

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
    "........."
    "......"
    "..."

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

label beachsixmakoto1:
    play sound "static.mp3"
    scene makotoiobath1 with flash
    stop sound
    play music "10c.mp3"

    "Not far at all from where we just were, different events were unfolding! Joyous events! The kind that make you wish you could be a part of them when there’s somewhere else you need to be!"
    "But that didn’t mean everyone present was happy about it."

    i "Fucking...slow down, Miku! Why are you running?! You’re going to hurt yourself!"

    play sound "static.mp3"
    scene makotoiobath2 with flash
    stop sound

    mi "Impossible! Miku Maruyama is immune to pain! And she is running because she can! Because she {i}must!{/i} And because that friggin’ hot spring is callin’ my name!"

    scene makotoiobath3
    with dissolve

    i "Can you at least put a towel on so you’re not running around completely naked then?"
    mi "Why? We’re just gonna be takin’ em off again in ten seconds, ain’t we? Makes way more sense to just let it all hang out, I think! Or...let nothin’ hang out in the case of me and Io."
    mak "I believe it’s less a matter of practicality and more one of sheer modesty, Miku. It’s sort of just an unwritten rule to stop running around without clothes on once you make it into high school."
    i "I think it’s kind of frowned upon before that too, but I’m not about to argue if what Makoto’s saying convinces you to be less, uhh...out there."

    scene makotoiobath4
    with dissolve

    mi "It doesn’t!"

    play sound "static.mp3"
    scene makotoiobath5 with flash
    stop sound

    mi "MARUYAMA SECRET TECHNIQUE — CANNONBALL! "
    i "At least give it a more interesting name!"
    mak "Miku! Didn’t you read the signs?! Don’t even {i}think{/i} about jumping into that water! You’ll regret it! Seriously!"
    mi "Too late, Makoto! I’m-"

    play sound "imscared.mp3"
    scene makotoiobath6 with hpunch

    mi "AAAAAAAAAAAHHHHHHH! WHY’S IT SO FRIGGIN’ LOUD?!?!?!!?!"
    mak "See? I {i}told{/i} you you’d regret. There were signs all over the place saying to not jump into the hot spring at the risk of it exploding. "
    mi "WHY’S THAT EVEN A THING?!?!?!?! THIS WOULD’A TOTALLY CAUSED ME AN EPISODE LIKE FIFTY UPDATES AGO!!!"
    i "Exploding water...great. Let’s hope my aunt never hears about this. Sounds hard to clean."

    scene makotoiobath7
    with dissolve

    mak "Oh, right. Your family runs the local bathhouse, don’t they?"
    i "It’s just my aunt and me. Not my family. And also, don’t talk to me. I am here only because Uta is hanging out with Sensei’s niece right now and I thought it was just going to be Miku and me."
    mak "{size=-1}I don’t intend to try and bond with you if that’s what you’re worried about. I just figured we might find some common ground as I’ve also been dragged into running {i}my{/i} family’s business.{/size}"
    i "With all due respect, which is basically none, I have heard about what your family’s business is. And I would much prefer it if you didn’t try to relate it to {i}my{/i} family’s legitimate one."

    scene makotoiobath8
    with dissolve

    mak "I understand the sentiment. But if you really think about it, isn’t your place of work even more adult-oriented than mine? At least people have to wear clothes inside of my store."

    scene makotoiobath9
    with dissolve

    i "Okay. So {i}both{/i} of our workplaces suck. Do you really want that to be the launching point for trying and failing at getting to know me, though?"
    mak "Not...really. I just know that you’re not exactly fond of things like this. "
    mak "So it’s less me getting to know you and more trying to make myself seem relatable and familiar so you’re not uncomfortable with me being here as well."
    i "Then just...don’t talk to me or look at me. In fact, stay away entirely. Just...do the complete opposite of everything {i}Miku{/i} did and...maybe I won’t want you to die. "
    mak "You don’t want Miku to die though, do you?"
    i "No. But I imagine her methods merely worked because I can convince myself she’s a boy if I squint my eyes hard enough. I’d have hated her if she was anyone else."
    mak "Then why do you like Uta so much? She’s essentially as girly as they come."

    scene makotoiobath10
    with dissolve

    i "It’s complicated, okay?! Just mind your own fucking business!"

    scene makotoiobath11
    with dissolve

    i "{i}Miku! Close your eyes. I’m taking my towel off now. {/i}"
    mi "{i}Whaaaat?! We ain’t gonna compare boobs or somethin’?! Ain’t that how these hot springs scenes work?!{/i}"
    mak "Wow. She really is closed off, isn’t she?"

    scene black
    with dissolve2

    "Makoto Miyamura wasn’t sure what to do. Especially since word {i}had{/i} in fact gotten around that Io had been {i}through something{/i} earlier in life."
    "No one ever brought it up — but it wasn’t really out of respect for her. It was out of respect for Uta."
    "And pity of course. {i}Mainly{/i} pity. And that nostalgic brand of unease you get from certain bouts of morbid curiosity."
    "Such curiosities had overtaken Makoto lately, though. And it was as if everywhere she looked, there was a part of the world she never noticed when it only moved in one direction."
    "That was equal parts fascinating and terrifying. But was there really anything to fear at all when this life was practically permanent?"

    scene makotoiobath12
    with dissolve2

    "Terror as a concept had become little more than a pothole on the road that is life itself. Something that makes you go “ah” for a split second, then fades away almost immediately."
    "There’s no constant, lingering dread anymore. Just the occasional thought of, “Hey — if I die, won’t I just wake up some{i}when{/i} else?” And that blended quite smoothly with her new way of life."
    "But it {i}also{/i} compelled her to want to make the best of this one. "
    "So despite how frequently she told herself that life now was just a series of orgasms and cups of coffee and sleeping through alarms, it was still a puzzle."
    "And Makoto liked puzzles. "
    "Not just solving them either. She enjoyed those feelings of confusion and helplessness that many others cower before or fall victim to. But she had already endured her own brand of that."
    "So she scorned the world for killing her father but, at the same time, she felt thankful."
    "Because there was nothing left to {i}fear{/i} anymore."
    "{b}{size=+10}{s}AT LEAST FOR NOW.{/b}{/size}{/s}"

    mi "Dang, Makoto. I ain’t seen you look {i}this{/i} relaxed and satisfied since the last time you came back from Sensei’s house."
    mak "Why did you have to go and ruin my moment of inner-peace like that, Miku?"

    scene makotoiobath13
    with dissolve

    mi "What’s wrong with bringin’ up the one thread tyin’ the three of us together?! This is a hot springs scene! If we ain’t gonna touch each other’s boobs, we’ve at least gotta bring up boys!"
    mak "That doesn’t give us much leeway as three heterosexuals then, does it?"

    scene makotoiobath14
    with dissolve

    mi "You’re right. We better go find the one or two other girls in our class that ain’t been converted yet and drag ‘em in here or we’ll run outta topics to discuss at this rate."
    mi "Io — you’ve got a list, don’t you? I ain’t even sure where to start."
    i "Of straight people? No. The only list I have is the love journal with Uta, and I’m not sure if I can publicly divulge the rankings of that without her present."

    scene makotoiobath15
    with dissolve

    mak "Can you at least say which one of us is in the lead?"
    i "I probably can. I just won’t because I don’t personally agree with the answer and am formally protesting the current results."
    mi "I don’t even {i}wanna{/i} know the ranking. It’s just gonna be friggin’ Ami and Ayane at the top. Rest of us are basically chop suey and gotta work harder."
    mak "Does Io even like Sensei like that, though?"

    scene makotoiobath16
    with dissolve

    mi "You askin’ me or her? Io ain’t really told me much about that. We just talk about sports. "
    mak "Io doesn’t want me to talk to her, so I’m just throwing the question out into the ether and hoping someone answers it."
    i "I like him romantically. Just my reasons for it probably aren’t the same as yours."
    mi "Well, there ya have it. Straight from the horse’s balls. "

    scene makotoiobath17
    with dissolve

    mi "Oh! Touka! {i}She’s{/i} straight! Horse balls made me think’a her! How many we got left?"
    mi "Makoto, make a worksheet or somethin’. We’ve gotta get to the bottom of this to figure out who to invite to our straight girls hot spring club. "
    mi "Futaba’s banned, though. I ain’t allowed near her boobs anymore. "
    mak "With respect to Io, we should probably stop bringing up boobs."

    scene makotoiobath18
    with dissolve

    i "Thank you."
    mi "I understand. {i}Nobody{/i} understands more than me..."
    mak "Yeah, I find that very hard to believe as you likely don’t understand at all."

    scene makotoiobath19
    with dissolve

    mi "That don’t mean boys are banned though, right? Cause you still ain’t even told me what happened on your date with Sensei!"
    mi "And as a girl who wants to go on dates with Sensei myself, I feel like I’ve gotta absorb as many tips as I possibly can."
    i "I {i}did{/i} tell you about what happened on the date, though. You just kept telling me I was making stuff up."
    mi "Well, yeah! Cause you kept talkin' about a giant hole! And the only giant hole around here's the one between Kirin's legs."
    i "First, ew. Second, the hole is real. "

    scene makotoiobath20
    with dissolve

    mi "I still wanna hear more about what happened {i}apart{/i} from the hole, though!"
    mi "Was it all romantic?! You guys kiss?! Or did ya just watch baseball and eat chips or somethin’? Sounds like an Io kinda date, right?"
    i "It would be if Sensei actually liked baseball. The two of us just went to the convenience store and then walked around for a little bit after we met up."

    scene makotoiobath21
    with dissolve

    i "...And then encountered a giant hole that led to an endless pit of nothingness in the middle of a sewer. Kind of hard to pivot away from a development like that."
    mi "Damn, Io. You're so persistent about this that I'm startin' to actually believe you."
    i "I'm honestly surprised you don't already. You believed me when I told you leather was made from boiling milk."
    mi "Wait. You tellin' me it ain't?"
    mak "I know you want me addressing you as little as possible, but I can’t help myself now. Question one — why were you in a sewer? And question two — “endless pit of nothingness?????”"

    scene makotoiobath22
    with fade

    i "It was {i}so{/i} weird! Like, I’ve been in those tunnels a million times before and had never seen that even once. It’s like it just showed up out of nowhere."
    mi "Okay. Say this hole {i}is{/i} real. The heck were you guys even doin’ down there?"
    i "Exploring, obviously! What better spot for a date than an underground adventure?! Just, the place I was specifically trying to take him to, like...wasn’t even there anymore."
    i "And I know it sounds crazy, but it’s like the tunnels {i}changed!{/i} Which makes me think it’s either a construction thing or a result of the sinkhole that stole my school. And my pencil case."
    i "I’m still investigating right now. Uta and I are gonna try and draw a map that-"
    mi "Okay, screw it! The hole is real!"
    mi "You’ve gotta let me get in on this too! I promise I won’t tell anybody! Scout’s honor! Oh! And Makoto too! We can all go together!"
    i "I...will have to bring this up with the tunnel council. Which is just Uta and me. But even then, her long-standing rivalry with Uta in the Dorm Wars may lead to unnecessary competition that-"

    scene makotoiobath23
    with dissolve

    mak "Actually, you guys can do all of that without me. I don’t really have much interest in exploring a sewer right now."
    mi "Whaaaat?! But it’s a {i}cool{/i} sewer! With a big and probably real hole!"
    i "It’s {i}way{/i} bigger than just a hole, Miku. It’s like...{i}unbelievable.{/i} I threw a rock down there and couldn’t even hear it hit the bottom!"
    mi "Seriously?! I want to throw rocks into the abyss too! You’ve gotta take me!"
    mak "Hey, I’m gonna get out a little early. No need to follow after me."

    scene black
    with dissolve
    play sound "water1.mp3"

    mi "Hm? Already? But you seemed so relaxed a few minutes ago. And this is our vacation. Don’t you wanna hang out a little while longer? "
    mak "Yeah, it was great. And maybe I’ll get back in later. I just need to go make a quick phone call. Sorry."
    mi "Aww, man...now our straight girls club is only two people."
    i "I despise saying this, but that makes our club sound very not straight."

    play sound "static.mp3"
    scene makotoiobath24 with flash
    stop sound
    play sound "phonebeep.wav"

    mak "..."
    mak "..."
    mak "...Come on. "
    mak "Pick up..."

    play sound "phonebeep.wav"

    s "{i}Uhh...hello? Mako-{/i}"
    mak "Why didn’t you tell me about Io’s giant hole?"

    play sound "static.mp3"
    scene makotoiobath25 with flash
    stop sound

    s "Because unlike you, I don’t body-shame. It’s 2020, Makoto. The size of someone’s hole does not change who they really are on the inside."

    if iosex == True:
        s "Also, it wasn’t big at all. It's actually very nice if you can look past all of the trauma. "

    play sound "static.mp3"
    scene makotoiobath26 with flash
    stop sound

    mak "No, you idiot! The hole you two encountered on your date in a sewer! You didn’t think that was {i}weird{/i} and relevant to our freaky apocalyptic universe?!"
    s "{i}Oh...That hole.{/i}"
    s "{i}Sorry. My mind has been kind of elsewhere all day.{/i}"

    scene makotoiobath27
    with dissolve

    mak "When {i}isn’t{/i} it? You should have told me the moment you found something like that. It could give us some sort of hint about all of this."
    mak "Massive abysses like that don’t just appear overnight and-"

    scene makotoiobath28
    with dissolve

    mak "Are you having sex right now?"

    play sound "static.mp3"
    scene makotoiobath29 with flash
    stop sound

    s "Uhh..."
    s "No?"
    n "Ngh...aah...[norikomaster]! Who...is that?! Are they...coming to join us too?!"

    scene makotoiobath30
    with dissolve

    s "It’s Makoto. Do you want to talk to her?"
    n "Haaah! Ngaaah! Okay! Pass it...here...[norikomaster]!"

    play sound "static.mp3"
    scene makotoiobath31 with flash
    stop sound

    s "{i}Noriko wants to talk to you. Here.{/i}"
    mak "Well, {i}I{/i} don’t want to talk to her! Not while you’re-"
    n "{i}Aaah! H...Nghh...Hi...Makoto! How are...ngh...you....aaaah! How are you...doing?!{/i}"

    scene makotoiobath32
    with dissolve

    mak "..................Great! Thanks {i}so{/i} much for asking."
    mak "Can you put Sensei back on please?"
    n "{i}I’m...ngh...trying, but...Kirin is...aaah! Oh my god! M...Makoto! You should...come play with us too!{/i}"
    mak "Give...the phone...to {i}Sensei.{/i}"
    s "{i}Speaking. Hey, Makoto. When will you be here?{/i}"

    scene makotoiobath31
    with dissolve

    mak "I won’t! I want to talk about the hole! I think we should investigate it! When you’re {i}not{/i} in the process of blowing the Dorm 10 girls’ backs out!"
    s "{i}I don’t...remember how to get there, though...you’ll have to ask Io.{/i}"

    scene makotoiobath33
    with dissolve

    mak "And then what? Have her repeatedly start her sentences over throughout the entire journey there while we do more end-of-the-world troubleshooting? Does that not sound annoying to you?"
    mak "Let’s just figure out how to get there on our own. It could mean something."
    s "{i}Sure...or it could just be a big hole.{/i}"
    mak "Things like that don’t happen without a reason, Sensei."
    s "{i}What are you talking about? Things like that happen all the time here. Haven’t you been paying attention?{/i}"

    scene makotoiobath31
    with dissolve

    mak "More than you, you stupid...sex guy!"
    s "{i}...Sex guy?{/i}"
    mak "Goodbye!"

    scene black
    with dissolve
    play sound "phonebeep.wav"
    stop music fadeout 15.0

    mak "Ugh! Can he not hold it in for even a single phone call? We might finally have something to go off of here!"

    "Clutching her phone with enough force to crack the screen, Makoto makes her way back into the dressing room and puts her clothes back on without waiting for the others."

    scene tree3
    with dissolve4

    "Then she heads back to her room and spends the next few hours taking notes on other things that could be considered anomalies. "
    "Her friends forgetting things that she remembers."
    "Strange pictures on the walls that she’d never noticed before."
    "A box in the corner of her room that looks like it twitches, waiting to be filled."

    play sound "knock.mp3"

    "A knock on the door with no one behind it."

    play sound "phonering.mp3"

    "The ringing of a phone with no one on the other end."

    play sound "seek.mp3"

    "Laughter from beneath the bed."
    "As it turns out, she {i}can{/i} still feel fear."
    "It just stems from confusion now."
    "The kind she can not love, because she can not find the pieces required to solve the puzzle that produces it."

    scene black
    with dissolve2

    "By the time night falls, her notebook is a mass of black."
    "She can hear the ocean when she presses her ear against it."
    "I used to hear the same when I would sleep with my head on your chest."

    $ renpy.end_replay()
    $ beachsixmakoto1 = True
    $ makoto_love += 1

    "........."
    "......"
    "..."

    jump beachsix3

label beachsixmakoto2:
    scene clearnightsky
    with dissolve3
    play music "undersea.mp3"

    "Night falls upon the second day like a tree falls upon the floor of the forest, where no one realizes it but me. "
    "And it gets me thinking — how many more times would this need to happen before there’s nothing left to fall? "
    "How long would we have to stay here, do you think? And would the novelty of spraying your seed upon nubile flesh wear thin like the fabric of cheap swimwear the longer you endure it for?"
    "If you asked me, I’d probably guess that you’d grow bored. But I also guessed that you’d grow bored of {i}all{/i} of this, yet we’re still here and we’re still talking."
    "It won’t last forever, though."
    "You know it won’t last forever, right?"
    "So that makes me wonder — what will you do when it’s over?"
    "Settle down somewhere? Up north, maybe? Where you don’t have to deal with the heat anymore."
    "I hear Jesus is buried behind a yogurt factory in Aomori. You could always pay him a visit. Draw the forced parallels before realizing he was more like everyone else than he was like you."
    "Whatever you do, I know I’ll be there to see it. And when you close your eyes, I’ll be {i}there{/i} too."
    "You’ll see me in the water. In the mirror. In the sky and the sand and the stars or wherever it is you look because you’ll always be looking for {i}me.{/i} "
    "I’ll always be looking for {i}you.{/i} "
    "And when the world goes dark, I’ll be the light that gives you warmth. Or comfort. Or anything you need because I would not exist at all if it were not for your unending love."
    "Which one am I this time, do you think?"
    "..."
    "Perhaps I should show you?"

    scene makotobeachthreemoons1
    with dissolve3

    "There are {i}many{/i} things I should show you, if we’re being honest."
    "But for every single one of them, there are a thousand more I need to hide because your fragile heart could simply not endure the misery that I have."
    "I learned from the best, though. And if the space between us can be filled by vagaries or auguries, I will tear open the floodgates and lay waste to the decaying crop field that is your conscience. "
    "Because I {i}still{/i} believe that you are here for a reason. Even when everyone else, including what’s left of yourself, has given up on you."
    "There is a purpose for all of this."
    "I just hope we can find it before we run out of infinities. Because it may not always seem like it, but time is of the essence. And I’m-"

    mak "Maya?"

    scene makotobeachthreemoons2
    with dissolve

    m "Hm?"

    play sound "static.mp3"
    scene makotobeachthreemoons3 with flash
    stop sound

    mak "There you are. I’ve been looking all over for you. Why haven’t you answered your phone?"
    m "Does this outfit look like it has pockets to you, Makoto? My phone is in the room."
    mak "{i}Which{/i} room? Because that’s kind of why I’m looking for you. "
    m "The...room we’ve been in since we got here? "
    m "What’s this about? Why are you looking for {i}me{/i} of all people?"
    mak "Obviously because I’m inviting you to a super exclusive and super awesome slumber party."
    m "Oh."
    m "..."
    m "Why?"

    scene makotobeachthreemoons4
    with dissolve

    mak "Because you’re one of the very few people in this city who doesn’t malfunction whenever the topics of the universe and time travel come up. And I think you could be useful to us."
    m "You...intend to use me as a tool to fix the world?"
    mak "Right."
    m "Gotcha. I completely understand what the slumber party is for now and why it needs to be tonight instead of literally any other night. "
    mak "Well...we’re already together, aren’t we?"

    scene makotobeachthreemoons5
    with dissolve

    m "We sleep in the same building on the same floor. Just wait until we’re not in the middle of vacation if you want to abuse my status as Sensei’s dream girl to try and fix your timeloop."
    mak "You know he’s coming too, right? I just got off the phone with him a little while ago since he actually keeps his on him."
    m "Well, so would I if I was getting nudes from cute girls all day. What’s your point?"
    mak "My {i}point{/i} is this is the perfect opportunity for you to get closer to him and try to bridge the gap between you and the older Maya he still cries about all the time."
    m "Bullshit. He can talk to me alone when he wants to do that. Why should I believe someone I’m competing against? Especially someone who competes as...{i}viciously{/i} as you."

    scene makotobeachthreemoons6
    with dissolve

    m "There’s something you’re not telling me here. And I’m not about to go wandering into some room where you and a bunch of other girls can kill me just so you can climb up the rankings."
    mak "I get not trusting me since the two of us aren’t particularly close. But you {i}do{/i} trust Ayane, don’t you?"
    m "Not really, no. "
    mak "Oh."
    mak "..."
    mak "Well, can you come anyway? Because this all sort of hinges on your involvement and I’ll have stayed up all night for nothing if you don’t come."
    m "No."
    mak "Food will be provided."
    m "Fine."
    mak "Wow. You’d be really easy to kidnap if I was an older man with ulterior motives. Is {i}that{/i} how you fell into Sensei’s lap?"

    scene makotobeachthreemoons7
    with dissolve

    m "I did not {i}fall{/i} into his lap. He put me there. And it is there I have remained ever since — even in the face of time and a world that seems dedicated to tormenting me specifically."
    a "What’s all this about tormenting you?"

    play sound "static.mp3"
    scene makotobeachthreemoons8 with flash
    stop sound

    mak "Oh, Ami. We were just-"
    a "I’m not talking to you, Makoto. I’m talking to {i}Maya.{/i} She’s not supposed to be here."
    m "Yasu told me the same thing. Why is everyone trying to get rid of me all of a sudden? I’ve literally just minded my own business all weekend. "
    a "Is that the “torment” you were talking about? Or were you insinuating something else, maybe?"

    play sound "static.mp3"
    scene makotobeachthreemoons9 with flash
    stop sound

    m "..."
    a "..."
    mak "Right. Well, I’m gonna go."

    scene makotobeachthreemoons10
    with dissolve

    m "Do you {i}have{/i} to? Because I {i}kind of{/i} don’t want to be alone with her."
    mak "I have one other person to go round up. And hopefully {i}they’ll{/i} be easier to track down. Just text me for more details in an hour or two if you change your mind about coming."

    scene makotobeachthreemoons11
    with dissolve

    m "Makoto, wait!"

    play sound "static.mp3"
    scene makotobeachthreemoons12 with flash
    stop sound

    a "Coming where? Did Makoto invite you to something?"
    m "I...she...yeah. I’m not going, though."
    a "Why not?"
    m "Just...sounds kind of sketchy. That’s all."
    a "That just makes it sound like you’re hiding something. "
    m "Ami-"
    a "{i}Are you?...{/i}Hiding something, Maya?"
    m "What? No! Of course not. I trust you way more than {i}Makoto.{/i} I’ve only talked to her, like...three times. Max. "

    scene makotobeachthreemoons13
    with dissolve

    a "Great! Then you and I can spend the whole night together while everyone else fights over my dad!"
    m "..."

    scene makotobeachthreemoons14
    with dissolve

    a "Why the long face all of a sudden? Is there something wrong with what I said?"

    scene black
    with dissolve2

    m "...No."
    m "Nothing at all."

    play sound "static.mp3"
    scene makotobeachthreemoons15 with flash
    stop sound

    "Makoto Miyamura was {i}swarmed{/i} by colored lights as she walked along the coastline! Colors that must {i}mean{/i} something!"

    play sound "static.mp3"
    scene makotobeachthreemoons16 with flash
    stop sound

    "Until they don’t. And you realize it’s all just a trick of the camera. A prank on your perception, leading you astray from the words on the screen when all they’ve ever been is honest!"
    "Just honesty comes in different forms. And while it may not take the shape of color or some other familiar distortion, it can {i}still{/i} be monumental when wielded by the right hands."
    "But that begs to question — what about the {i}left{/i} ones? "
    "Which gods do the gods worship?"
    "Makoto Miyamura. Beach."

    play sound "static.mp3"
    scene makotobeachthreemoons17 with flash
    stop sound

    "Yumi Yamaguchi! {i}Beach!{/i}"
    "Why is it always the beach?! I’m still reeling from the last time and you expect me to just go on and on like it’s nothing?! Is {i}this{/i} the perfect harmony you hoped for?!"

    play sound "static.mp3"
    scene makotobeachthreemoons17 with flash
    stop sound

    "No! Don’t cut me off! I’m still not-"

    play sound "static.mp3"
    scene makotobeachthreemoons15 with flash
    scene makotobeachthreemoons16 with flash
    scene makotobeachthreemoons15 with flash
    scene makotobeachthreemoons16 with flash
    scene makotobeachthreemoons15 with flash
    scene makotobeachthreemoons16 with flash
    scene makotobeachthreemoons15 with flash
    scene makotobeachthreemoons16 with flash
    scene makotobeachthreemoons17 with flash
    stop sound

    y "Oh, Prez. What are you doing out here for? Shouldn’t you be, like...studyin’ or some shit?"
    y "That’s what you do for fun, right? I promise I ain’t tryin’ to be an asshole this time."
    mak "Maybe a few years ago. I have new ideas of fun now. And tonight, you’re lucky enough to be involved in one."

    scene makotobeachthreemoons18
    with dissolve

    y "Yeah. {i}So{/i} lucky. Been here for a total of thirty fuckin’ minutes and I’m already bein’ roped into somebody’s bullshit. Beats workin’ at least. "
    y "Go on, then. Tell me. The fuck you want? Somethin’ to do with more apocalypse shit, I’m guessin’?"
    mak "Well, yeah. But how did you-"
    y "Blondie had a god damn shirt shipped to my dorm room. You guys ain’t gonna make me wear it, are you?"
    mak "Only if you want to match us."
    y "Wow, yeah. Sounds fun. So, when’s this shit supposed to happen {i}this{/i} time? We got time to, like...prepare and shit?"
    mak "Well...we don’t know. And we basically {i}never{/i} know anymore now that the girl who was able to sense it is suddenly just a less useful version of herself."
    mak "However, I think that if we’re able to get her back on board, we might be able to-"
    y "This shit you need to tell me now? Or can it wait until we’re all in the same fuckin’ room? Want at least a few minutes of peace and quiet if that fits within your {i}master plan.{/i}"
    mak "Oh. Yeah. I’m planning on going into greater detail later, so-"
    y "Cool. Watch the water with me then?"
    mak "...What?"
    y "‘Less you don’t wanna. Ain’t gonna break my heart or anything if you say no."
    mak "You’re actually inviting me to join you? You’re not going to tell me to fuck off?"
    y "I might if you start bein’ fuckin’ weird about it."

    scene makotobeachthreemoons19
    with fade

    mak "I don’t have to be weird. In fact, I actually think this is a nice little moment of respite after an otherwise hectic day."
    y "Heard from Noriko that Futaba freaked the fuck out earlier and called out Sensei on bein’ a fuckin’ predator. Kinda pissed I missed it."
    mak "Even {i}that’s{/i} putting it lightly. She freaked out on practically everyone. And I get that she’s been going through some stuff, but...still. It was weird."
    y "Think she’s finally gettin’ tired of all this shit? Havin’ to compete with the whole fuckin’ class for the fake-ass love of some guy who doesn’t have any to give in the first place?"
    mak "Could be. I think we all get days like that sometimes. That...{i}awareness,{/i} I mean. Just most of us keep it to ourselves."
    mak "It does make you feel stupid when you think about it, though. I’m not really sure how things ended up like this."
    y "Guess I should be pretty proud of myself for bein’ the only girl around he ain’t porked yet then, huh?"
    mak "You’re not the only one. There are a few still hanging on for dear life. I imagine you {i}will{/i} be the last if things keep going at this pace, though."
    y "That just makes it sound like it’s inevitable, don’t it?"
    mak "Not really. What’s {i}inevitable{/i} is you giving into your feelings since I know you like him too."

    scene makotobeachthreemoons20
    with dissolve

    y "Don’t fuck with me, Four Eyes. You’re finally on my good side."
    mak "I’m not trying to fuck with you, Yumi. You’ve really grown on me lately and I’m not trying to ruin that before we’re even friends."
    mak "I just feel bad that even in the midst of a timeline that likely won’t ever end, you won’t let yourself enjoy it."
    mak "Is that a loyalty thing? Or is your moral code just weirdly powerful when it comes to, uhh...{i}chronologically imbalanced{/i} relationships?"
    y "So me not likin’ him just ain’t even a possibility in your head, huh?"
    mak "No. I’m a little too smart for that, I think."
    y "Are you? Cause you weren’t smart enough to keep him outta your pants. You let him in the same way everyone else did, so you ain’t as special as you think."

    scene makotobeachthreemoons19
    with dissolve
    stop music fadeout 40.0

    mak "I didn’t do that because I’m dumb. I did it because I’m sad."
    y "Lots of sad girls ‘round here nowadays. And they’ve all got the same fuckin’ thing in common."
    mak "Just trying to stay out of our ranks then, huh?"
    y "Just trying to survive. Better chance of that if I ain’t got any weaknesses."
    mak "Fair enough. I still think it’s inevitable, though. And honestly? I’d be interested to see what a Yumi in love would look like. Even {i}if{/i} she were a rival of mine."
    y "She’d probably just look like another dumb bitch. Ain’t you seen enough of those by now?"
    mak "Do you think Noriko and Chika are dumb bitches, Yumi? "
    y "Well...they’re dumb. And they’re bitches. Probably wouldn’t call ‘em dumb bitches, though. So maybe you’re onto something here?"
    mak "Yeah...maybe I am. And maybe one day, we’ll be able to talk like this without you holding yourself back."
    mak "I wonder what that’d be like?"
    y "Exhausting, probably. "
    mak "Yeah...probably."
    y "Punch me in the mouth if that ever happens, alright?"
    mak "I’ll try. I’m not much of a fighter, though."
    y "Yeah, and I ain’t much of a lover. So maybe we should just keep ourselves in line, then? I’ll figure out how to punch myself if I ever get soft."
    mak "And I’ll continue fucking the guy you like. Works for me."
    y "Aight. {i}Now{/i} you’re on my bad side again."

    scene black
    with dissolve2

    mak "Heh..."
    mak "It was only a matter of time..."

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ beachsixmakoto2 = True

    jump beachsixtsuneyo1
