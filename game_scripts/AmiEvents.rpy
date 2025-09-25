label amisroom:
    if ami_love >= 0 and firsttimeamisroom == False:
        jump firsttimeamisroom
    if ami_love >= 5 and amisroom5 == False:
        jump amisroom5
    if ami_love >= 10 and amisroom10 == False:
        jump amisroom10
    if ami_love >= 15 and amidorm15 == True and amisroom15 == False:
        jump amisroom15
    if ami_love >= 20 and beachvacation16 == True and mayadorm25 == True and amisroom20 == False:
        jump amisroom20
    if ami_love >= 25 and ami_virgin == False and amidorm20 == True and amisroom25 == False:
        jump amisroom25
    else:
        jump amisroom3to4

label amiinvite:
    if amiblock == True:
        "I don't think Ami wants to see me right now..."
        jump callnight
    if amiinvite1 == False:
        jump amiinvite1
    if amiinvite1 == True and amiinvite2 == False and amiinvite2miss == False:
        jump amiinvite2
    if amiinvite3 == False and shrine35 == True:
        jump amiinvite3
    if ami_love >= 50 and kaorispecial40 == True and amimaid50 == True and amiinvite4 == False:
        jump amiinvite4
    else:
        jump amiinvitegen

label amiinvitegen:
    play sound "phonebeep.wav"

    "I tap on Ami's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    a "Hey, [amimaster]! I was just thinking about you."
    s "You're literally always thinking about me, though."
    a "I see no problem with this."
    a "What's up?"
    a "Gonna invite me to my own house again?"
    s "Yes. Would you like to come hang out at the place you are inside of right now?"
    a "I was gonna go hang out with Maya, but I can stay here as long as you're coming home~"
    s "In that case, I'll be there shortly."
    a "Yay!"
    a "I'll see you soon, [amimaster]!"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    if halloweenfive17 == False:
        scene amiinvitehub
        with dissolve
    else:
        scene amiinvitehub2
        with dissolve

    play music "acoustic.mp3" fadein 3.0

    a "So, what did you want to do today?"

    "How should I spend my time with Ami?"
    menu amiinvmenu:
        "Hang Out (Raise Affection)":
            jump amiinviteaff
        "Thighjob (Raise Lust)" if amiinvite2 == True and bonus == True:
            jump amiinvitethighjob
        "Reverse Cowgirl (Raise Lust)" if ami_virgin == False and bonus == True:
            jump amiinvitereverse
        "Hug (Raise Lust)" if amiinvite2 == True and bonus == False:
            jump amiinvitethighjob
        "Hold Hands (Raise Lust)" if ami_virgin == False and bonus == False:
            jump amiinvitereverse
        "Headpat" if ami_virgin == False and bonus == True:
            jump amiheadpat

label amiinviteaff:
    if halloweenfive17 == False:
        scene amiinvitegen
        with dissolve
    else:
        scene amiinvitegen2
        with dissolve

    "I decide to spend the night hanging out in my room with Ami."
    "No matter what I suggest doing, she playfully refuses and beckons me into the bed to lie with her and hold her hand."
    "The next few hours pass by with her reciting memories that I wish I could have inherited when I arrived here."
    "Unfortunately, her relationship with me is much more than mine will ever be with her."
    "And all of those memories that mean all of those things are more like anecdotes or poems."
    "One thing that means the world to one person might make absolutely no sense to someone else."
    "I'm caught somewhere in between."
    "I absorb the things she tells me, racking my brain and trying to connect any dots that someone else may have left behind."
    "But I come up with nothing."
    "I think Ami notices this at some point since she carefully tiptoes away from anything involving the past and makes her way into the present."
    "We talk about[school]. We talk about the dorms."
    "We talk about everything up until our eyes close."

    scene black
    with dissolve

    "Ami falls asleep before I do- the same way she always does when the two of us are in this position."
    "I stare at her face as she sleeps on my shoulder, her mouth slightly drooped open and exerting soft, sweet breaths."
    "She doesn't talk in her sleep, but she doesn't need to."
    "I can understand everything she's thinking and everything she's feeling just by keeping my eyes on her."
    "And so I do that until I, too, pass out..."

    $ ami_love += 3
    stop music fadeout 5.0

    "{i}Ami's affection has increased to [ami_love]!{/i}"

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

label amiinvitethighjob:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump amiinvitethighjobx
    else:
        $ ami_lust += 3
        stop music fadeout 5.0

        "{i}Ami's lust has increased to [ami_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label amiinvitereverse:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump amiinvitereversex
    else:
        $ ami_lust += 3
        stop music fadeout 5.0

        "{i}Ami's lust has increased to [ami_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label amimaidhub:
    if ami_love >= 30 and utadorm10 == True and bar35 == True and amimaid30 == False:
        jump amimaid30
    if ami_love >= 50 and treasureisland == True and makotodorm55p2 == True and norikoinvite3 == True and amimaid50 == False:
        jump amimaid50
    if chap4active == True:
        jump amispringmaidgen
    if chapthreeactive == True:
        jump amisummer2maidgen
    else:
        jump amimaidgen

label callamimorning:
    if amiblock == True:
        "Ami isn't going to answer her phone right now..."
        jump callmorning
    if christmas7 == False:
        "There's no point in calling Ami when I can just go to her room."
    else:
        "Ami should be at work right now. If I want to see her, I should visit the maid cafe."
    jump callmorning

label callamiafternoon:
    if amiblock == True:
        "Ami isn't going to answer her phone right now..."
        jump callafternoon
    if ami_love >= 35 and amimaid30 == True and shrine35 == True and amidate35 == False:
        jump amidate35
    if chap4active == True:
        jump amispringnoongen
    if chapthreeactive == True:
        jump amisummer2noongen
    else:
        play sound "phonebeep.wav"

        "I tap on Ami's name in my phone and wait for her to answer."

        "........."
        "......"

        play sound "phonebeep.wav"

        a "[amimaster]? What's up?"
        s "Hey. What are you doing right now?"

        if bonus == True:
            a "Right now? I'm reading some romance manga about two characters who totally aren't related to one another."
        else:
            a "Oh, you know. Just...accountant stuff."

        s "That's...Well, okay then."
        a "Mhm! Did you want to maybe come hang out with me instead?"

        menu:
            "Spend time with Ami":
                s "Sure. Are you at home?"
                a "Yup yup!"
                s "Gotcha. I'll come over there now."
                a "Yay! I'll see you soon then~"
                s "Yup. See you soon."

                play sound "phonebeep.wav"

                "I hang up the phone and begin to make my way over."

                scene black
                with dissolve

                "........."
                "......"
                "..."

                jump amigenafternoon

            "Call someone else":
                s "Actually, on second thought, I think I'm going to go do something else."
                a "Wait, what the heck is this? Did you call me just to get my hopes up?"
                s "Of course not."
                a "I don't believe you. That sounds exactly like what's-"

                play sound "phonebeep.wav"

                "I hang up the phone and decide to call someone else."
                jump callafternoon

label callaminight:
    if amiblock == True:
        "Ami isn't going to answer her phone right now..."
        jump callnight
    if chap4active == True:
        jump amispringnightgen
    if chapthreeactive == True:
        jump amisummer2nightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Ami's name in my phone and wait for her to answer."

        "........."
        "......"

        play sound "phonebeep.wav"

        a "[amimaster]? What's up?"
        s "Hey. What are you doing right now?"
        a "Me? I'm cooking dinner. Are you coming home early?"
        a "Did you want me to make you something?"
        s "Hmm..."

        menu:
            "Spend time with Ami":
                s "Yeah. I'll be right there."
                a "Okay! I'll see you soon~"

                play sound "phonebeep.wav"

                "I hang up the phone and begin to make my way back home."
                "........."
                "......"
                "..."

                stop music fadeout 3.0

                if christmas7 == False:
                    jump amigennight
                else:
                    jump amigennight2

            "Call someone else":
                s "Actually, on second thought, I think I'm going to go do something else tonight."
                a "Whaaaat? No fair! You can't just get my hopes up like that! I'll have you know I-"

                play sound "phonebeep.wav"

                "I hang up the phone and decide to call someone else."
                jump callnight

label amimaidgen:
    scene amimorninggen2
    with fade
    play music "normalday.mp3"

    "I arrive at the maid cafe and am promptly greeted by my [niece], who also happens to be the only maid working right now."
    "And while this should probably worry me since she hasn't been doing this as long as someone like Uta, her confidence (And the fact that no one else is around) puts me at ease."
    "Not having anything else to do at the moment, Ami stays at the table with me and talks a bit about how work has been going."
    "Apparently, she's only had a few male customers so far and every single one of them has shown more interest in Uta-chan than her, so of course I have to deal with those complaints for a little while."
    "How a maid cafe manages to stay open with predominantly female customers, I don't know. But it's nice knowing that no one's tried to take advantage of her."
    "In fact, with the way she talks about it, I think she might even genuinely like this place."
    "Other than the whole {i}being apart from me{/i} thing, that is."
    "But hey, she had to leave the nest sometime. And now she's even making money by doing it."

    scene black
    with dissolve

    "I decide to call it quits before I wind up spending all of my money."
    "As it turns out, I am not only weak to Uta-chan, but to all maids in general."
    "Ami was right. I may have an addiction."
    "How did I make it this far into life without realizing that?"
    "Before I'm able to make it out of the door, Ami hugs me from behind and tells me to come back soon-"
    "Which would have been very cute if it weren't for the fact that she immediately followed that up with asking me to spend more money on her."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami's affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label amigenafternoon:
    scene amiafternoongen
    with dissolve
    play music "normalday.mp3"

    "I decide to spend the afternoon with Ami."
    "The two of us hang out in her bedroom and she proceeds to rant about the drop rates in some video game she's playing for the next half hour."
    "Knowing absolutely nothing about whatever she's saying, I simply nod my head and try to appease her."
    "Eventually, she realizes that I'm not exactly interested and winds up giving me a shoulder massage instead."
    "If you don't have a [niece], I highly recommend that you somehow procure one."
    "I can't guarantee she'll be as good as Ami...but if she's even anywhere {i}close{/i}, I can guarantee that your life will never be the same..."

    scene black
    with dissolve

    "Ami winds up cutting our hang-out session short when she realizes she still has to go run some errands."
    "Not knowing what else to do, I decide to head back out and walk around for a few hours..."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami's affection has increased to [ami_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label amigennight2:
    scene aminightgen2
    with dissolve
    play music "love.mp3"

    "I head home early to spend some time with Ami."
    "She's already in her pajamas by the time I get back and immediately summons me into her room to lie on the bed with her."
    "We don't talk much but instead just lie there looking at the ceiling for an uncomfortable amount of time."
    "Frankly, I think it's a little boring. But each time I go to strike up a conversation and notice her happily smiling to herself with her eyes closed-"
    "Well, I kind of forget that I was ever bored to begin with and instead just...continue to lie there."
    "Doing nothing. Saying nothing."
    "But it's the most comfortable form of nothingness I've ever felt."

    scene black
    with dissolve

    "The two of us eventually pass out, but I wake up several hours later and decide to get back into my own bed."
    "I always hate sleeping in unfamiliar beds."
    "Before I leave, I make sure Ami is tucked into her blanket and that her alarm is turned on so she can wake up on time and, you know, make me breakfast and whatnot."
    "I guess that all it takes for me to be a little considerate is knowing I'll get something out of it."
    "Thank you for the breakfast, Future-Ami."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami's affection has increased to [ami_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amigennight:
    scene aminightgen
    with dissolve
    play music "love.mp3"

    "I head home early to spend some time with Ami."
    "She's already in her pajamas when I get back, so the two of us spend the night eating pizza and watching movies on the couch."
    "And when I say 'watching movies,' I really mean that {i}I{/i} am the one watching movies. Or trying to, at least."
    "Ami sits there and playfully squeezes my arm, trying to get me to pay attention to her the entire time."
    "Having a weakness for cute girls, I obviously wind up focusing on her instead and completely neglect whatever movie we were 'watching' in the first place."

    scene black
    with dissolve

    "Ami eventually falls asleep on my shoulder and I have to carry her to her bedroom."
    "As I lay her down and begin to walk away, she unconsciously reaches out and grabs my hand to prevent me from leaving."
    "After a while, she becomes too tired to hang on and I'm left with no other option but to call it a night..."

    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami's affection has increased to [ami_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat


label firsttimeamisroom:
    scene lr_day
    with dissolve
    play music "normalday.mp3"

    "I step out into a living room that I’ve yet to fully familiarize myself with and think for a moment about who I am and why I am here."
    "But then I remember that there is a cute girl sleeping in the room right next to mine and that any thought I could possibly have apart from that is essentially pointless."
    "I still don’t know much about Kumon-mi...but what’s even more bizarre is that, somehow, I know even less about the girl who’s been guiding me through it thus far."
    "Well, I guess {i}guiding{/i} might be a bit too generous of a word when all she’s really done is provide baseline hints and...vaguely generic information I would have likely figured out on my own."
    "But I guess now is as good a time as any to try and change that."

    play sound "knock.mp3"

    "I knock on Ami’s door, hoping that she hasn’t gone out for the morning as that would leave me alone with nothing but my thoughts- and my thoughts have been rather...intense these last few nights."
    "In a good way, of course. But it’s kind of hard to {i}not{/i} have thoughts like that when you wake up in what I’m pretty sure is the early stages of a harem."

    a "Come in, Sensei! The door is open."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Good. It looks like my unofficial tour guide and slightly-official niece hasn’t gone out yet."
    "Now, all I have to do is figure out how to talk to her without sounding like a complete creep. And how hard could that possibly be?"

    scene aminewfirstevent1
    with dissolve2

    s "Good morning, Ami. You smell nice."

    "Fuck."

    a "Oh! Umm...thank you! "
    a "Are you sure it’s me and not my room, though? Because I was doing some cleaning a little earlier and sprayed way too much Cleaning Juice all over the place."
    s "Please don’t call it cleaning juice. I don’t like that at all."
    a "Hm? That’s just the name of the brand. It’s some kind of deodorizer or something...Which isn’t me saying that my room normally smells bad. I just...want it to smell better?"
    a "Anyway, if you’re wondering why there’s still stuff all over the place, I’m just taking a little break before I get back to business. I promise it’ll all be gone soon."
    s "Oh, I don’t really care. You can leave your room a mess indefinitely and it really won’t make much of a difference to me."

    scene aminewfirstevent2
    with dissolve

    a "Well, it will make a difference to me since keeping things clean is a good quality and I want you to love me even more than you already do. "

    "Any amount of love at all would be more than what I currently have for this girl..."
    "But I will keep that to myself for the time being as it’s still way too early for me to do something with the potential to ruin this prospective harem."

    scene aminewfirstevent3
    with dissolve

    a "But yeah...I should be done with my room by the afternoon. And I handled the living room and the bathroom yesterday, so that really just leaves the attic after this."
    s "So is cleaning just...what you do as a hobby or something? "

    scene aminewfirstevent4
    with dissolve

    a "Wait a second...is your memory still all weird from when I woke you up from your nap the other day?"
    s "...Yes. That is what is happening."
    a "Should we maybe take you to the doctor or something? Because if you’re still feeling weird all this time later, you might be, like...really really sick or something."
    s "I’m sure I’ll be fine. I just need to get my bearings a little."

    scene aminewfirstevent5
    with dissolve

    a "Never worry, Sensei. Your beloved niece and favorite girl in the entire world, Ami Arakawa, can help you with that."
    a "To start off...no. Cleaning isn’t a {i}hobby{/i} of mine. It’s just something I do because I know you never will."

    "Well, at least that’s one thing the original Sensei and I have in common."

    a "In fact, I handle basically all the chores around here so you can relax to your heart’s content. It’s the least I can do after all you’ve done for me."
    s "I see. So...there’s nothing I need to do to like, repay you for all of your work around here? "
    a "Sensei, all you need to do is repay me with love."
    s "Is there anything {i}else{/i} I can repay you with?"

    scene aminewfirstevent6
    with dissolve

    a "Love is like the easiest thing I could have possibly asked for! Can you at least go back in time to when you remembered you cared about me?!"
    s "Yeah, I don’t really think time works like that. But I do thank you for...all of the work that you apparently do around here while I..."
    s "I..."

    scene aminewfirstevent7
    with dissolve

    a "You can’t even remember what to do with your free time?"
    s "Honestly, it would probably be easier for both of us if you just pretend I know literally nothing about this place."
    a "Hah...I’m starting to feel like one of those NPCs that guides the protagonist in the beginning of an RPG."
    s "I think I know what those acronyms mean, but I’m not sure. So I’m just going to nod in agreement and hope you tell me more about how to live my life."

    scene aminewfirstevent1
    with dissolve

    a "Of course. But only because I’m so used to helping you out when you’re at your lowest point."
    a "Now, I don’t know {i}exactly{/i} how you spend every day...but I do know that you normally try to ration your time so you’re not spending all of it on just one person. {size=15}But if you do, that person should be me.{/size}"

    scene aminewfirstevent8
    with dissolve

    a "Now, let’s see...What are some things to do in the morning?"
    a "Oh. There’s a place called Koi Cafe just a few miles away from here that opened up a couple months ago that you might like."
    a "And the school library is also open on weekends if you ever want to go check out a book or something, so...there’s always that!"
    a "Also, I’m pretty sure the soccer team is looking for a coach as well. But you’ve never really been into sports so I can’t really see you ever going there."
    s "And what about things to do in the afternoon? Anything notable? Or..."

    scene aminewfirstevent1
    with dissolve

    a "Well...there’s the shrine or the dojo, but...again, I have no idea why you’d go to either one of those places."
    a "There’s the mall as well, but..."
    s "I’m going to take a wild guess here and say that you’re assuming I wouldn’t like hanging out in a place like that."

    scene aminewfirstevent9
    with dissolve

    a "Yeah. That’s exactly what I was assuming."
    a "You’re not a very exciting person, Sensei."

    "It’s true that none of those options sound particularly appealing to me...but I am not about to allow myself to be ridiculed by a pubescent redhead in bunny pajamas."
    "But I am also not about to fight back because Ami really is going out on a limb for me here and I don’t want to risk her just...not cooking or cleaning anymore."

    s "There has to be {i}something{/i} else for me to do around noon, right?"
    a "You...could always just walk around and look for something to do, I guess? Most people are busy in the afternoon, so I have no idea if you’ll find anything you’re interested in, though."

    scene aminewfirstevent10
    with dissolve

    a "Oh! You could always come hang out with me! I-"
    s "And what about night? What are some things to do around then?"
    a "..."
    s "..."

    scene aminewfirstevent11
    with dissolve

    a "I’m not sure if I want to tell you anymore if you’re just going to be mean and neglect me."
    s "I’m not neglecting you at all. I came to you first thing in the morning, didn’t I?"
    a "You did...but I’m starting to think you would have just left if I kept a pile of travel brochures near the door."
    s "Hey, if you want to run a travel agency out of your bedroom, that’s fine by me. I’ll be your first customer and everything."
    a "..."
    s "..."

    scene aminewfirstevent12
    with dissolve

    a "Hah...I really hope your memories come back soon, Sensei. I’m kind of tempted to feed you false information just to confuse you at this point."
    s "Please don’t. You’re all I have right now."

    scene aminewfirstevent2
    with dissolve

    a "I’m all you’ll ever have because I’m also all you’ll ever need."

    scene aminewfirstevent1
    with dissolve

    a "But, when it comes to night time...all I can really think of is the school dorms."
    a "Pretty much all of us gather there so, if you’re ever looking to kill some time or come see your adorable niece, that’s where you should go."
    a "I’m sure there’s also some {i}nightlife{/i} stuff you can find if you really want to..."

    scene aminewfirstevent13
    with dissolve

    a "But I’d really prefer you didn’t! "
    s "What? Why not?"
    a "Because that’s where I imagine older girls would be. And if you ever get a girlfriend, I will burn this house to the ground."
    s "..."
    a "..."

    "Okay. I’m beginning to think that Ami may like her uncle a little too much."

    scene aminewfirstevent14
    with dissolve

    a "Did you hear me, Sensei? I said I would-"
    s "Burn this house to the ground. I know. Which, by the way, is completely irrational."
    a "You would think it’s rational if you understood how much I love you."
    s "I can’t imagine that’s true. But I doubt you’d have to worry about something like that in the first place since...relationships aren’t really my type of thing."
    s "Besides, I already have ten girls I need to worry about on a daily basis. I don’t have time for romance."

    "Seduction, however, is another story entirely. But I’m fine with keeping that contained to my students for the time being."

    scene aminewfirstevent1
    with dissolve

    a "This is the best news I have ever heard."
    s "Because you’re not going to be abandoned?"
    a "If you abandoned me, what would happen if I needed to get something off of the top shelf? "
    s "What would happen if you needed to pay rent? Or...the mortgage? "
    s "You don’t happen to know how all of the bills here are handled, do you?"

    scene aminewfirstevent15
    with dissolve

    a "I’m pretty sure that all of our bills are automated since I’ve only seen you use your checkbook like one or two times."
    a "Either that or we’re way behind on every bill we have and will have to go live in an Internet cafe soon."
    s "I’d like to avoid that if at all possible, so I guess I’ll just...look into it on my own or something."
    a "Okay. And I’ll go back to being a teenage girl who doesn’t fully understand what a mortgage is yet."
    s "Sounds good. And thanks for all your help today, Ami."

    scene aminewfirstevent5
    with dissolve

    a "You don’t have to thank me, Sensei. I do this because I love you. Even {i}if{/i} you’d rather spend your free time aimlessly wandering around Kumon-mi instead of calling me pretty and buying me clothes."
    s "Sorry. I’d offer to take you to the mall but, like you implied, that’s just not really a place that a guy like me would hang out at."

    scene aminewfirstevent11
    with dissolve

    a "How the heck did you manage to forget literally everything except how to be sarcastic?"
    s "Luck maybe? I’m not really sure."
    s "But I should probably be heading out. There are a series of places I wouldn’t normally go to calling my name right now, and you need to get back to cleaning anyway."

    scene aminewfirstevent7
    with dissolve

    a "Yeah...I guess I should probably finish up as soon as possible if I’m going to make it back to the dorm by dinner time."
    a "And I haven’t even {i}looked{/i} at the attic yet, so I have no idea how long that’s going to take."
    s "Well...good luck, I guess. "

    scene aminewfirstevent1
    with dissolve

    a "Thanks, Sensei. Have fun taking advantage of your free time and remember to text me every thirty minutes so I know you’re okay."
    s "No."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    a "At least pretend that you’re going to! I deserve at least that much!"

    "I exit Ami’s room and make my way to the front door to see what else this city has to offer."
    "And while I didn’t learn much about my niece herself (Apart from her...extreme affinity for “me”), I do feel a little more at home now."
    "I’m still a fish out of water at the end of the day- but I’m one of those fish that can breathe on land for an extended period of time and won’t just flat out die within the first few minutes."
    "Either way, I’m glad Ami is as helpful and reliable as she’s been so far."
    "I can’t see any way at all that the two of us don’t wind up even closer."
    "It’s just {i}how{/i} close that remains to be seen."

    $ renpy.end_replay()
    $ firsttimeamisroom = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label amisroom3to4:
    play music "Normalday.mp3" fadein 2.0
    scene amiroom_day
    with dissolve

    "I decide to spend the morning hanging out with Ami."
    "She tells me a little about some Korean drama show she’s been watching
    while the two of us make breakfast together."
    "It feels strange being involved in a relationship like this out of virtually nowhere, but I'm getting used to it."
    "She seems rather comfortable with me as well..."

    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label amisroom5:
    scene black
    with dissolve
    play sound "dooropen.mp3"
    play music "normalday.mp3"

    "I guess I’ll see if Ami has any plans today."
    "I woke up feeling a lot more exhausted than normal for some reason, so the idea of going anywhere right now sounds like nothing more than...unnecessary pain."
    "Combine that with the fact that all I'd be doing is searching for another cute girl to hang out with and there's really no reason for me to ever leave at all."
    "Everything I could ever want is right here at home."
    "........"
    "......"
    "..."

    scene amidineredux1
    with dissolve2

    a "Oh, Sensei! Good morning. I was just going to come wake you up and see if you wanted to go out."

    "God damn it."

    s "Nope. I'll just stay here and be miserable."
    a "You're not allowed to be miserable while I'm here. That's one of our house rules, remember?"
    s "I remember no such thing. Where could you possibly want to go this early in the morning?"

    scene amidineredux2
    with dissolve

    a "Some new diner thingy just opened up the other day and I figured the two of us could go together since going to a diner by myself would make me look really lame."
    s "Are Ayane and Maya busy today or something?"

    scene amidineredux3
    with dissolve

    a "I don't think they're {i}busy...{/i}but chances are that both of them are still sleeping."
    s "You...don't want to call them and find out?"

    scene amidineredux4
    with dissolve

    a "Sensei...can you look down, please?"
    s "What? Why?"
    a "It's just that I've dropped so many hints about {i}wanting to do this alone with you{/i} over the last two minutes that they are now making the house look messy."
    s "Don't drop hints. It's best to just speak your mind, Ami."

    scene amidineredux5
    with dissolve

    a "I literally did that and you just said you'd stay here and be miserable!"
    a "Prove that you love me and come have breakfast at the new diner with me or I will throw myself off a bridge and leave a note saying you made me do it!"
    s "It was nice knowing you, Ami."
    a "Sensei!"
    s "I'm obviously kidding. I'll come. Just...give me a minute to get dressed since I was really planning on spending the whole morning here."

    scene amidineredux6
    with dissolve

    a "Really?! You'll go on a date with me?!"
    s "I'll come to the diner with you. I don't think I'm allowed to date my niece."
    a "Says who? There's no rule like that {i}I've{/i} ever heard about before."
    s "Then you haven't been paying much attention to societal norms or values. This place isn't far, is it?"

    scene amidineredux2
    with dissolve

    a "Not super far. Maybe like...a mile or two?"
    s "You're really going to make me walk a whole mile as soon as I wake up?..."
    a "You walk to other places all the time. What's the harm in walking somewhere with a cute relative at your side?"
    a "Besides, the two of us could use a little exercise, don't you think?"
    a "Unless there's some {i}other{/i} sort of physical activity that the two of us could do together in the comfort and privacy of our own home."
    s "Isn't that being a little too suggestive this early in the morning?"

    scene amidineredux3
    with dissolve

    a "I have no idea what you're talking about. I just want to spend some quality time with my uncle."
    s "I am sure you do..."

    scene black
    with dissolve2

    "I head back to the bedroom and change my clothes, wondering how serious Ami was about the whole {i}physical activities{/i} thing and...whether or not {i}I'd{/i} be serious about that as well."
    "But seeing as I don't want to walk one or two miles with an erection pressing up against the inside of my jeans, I decide to abandon the thought and simply think of nothing instead."
    "........."
    "......"
    "..."

    scene amidiner1
    with dissolve2

    "After a decently long walk, we make our way into a relatively old-fashioned, American style diner."
    "The air conditioner in here is turned on full-blast, making it an extremely welcome escape from the sweltering summer heat we were forced to battle on the way over."
    "For being what Ami claims is a new business, the diner is surprisingly empty."
    "Only a few tables are occupied by customers while a single waitress makes her way around the room, checking on each and every table while Ami and I figure out what we want to eat."

    a "Sensei, do you know what you’re gonna get yet?"
    s "I have no clue."
    a "Do you want something sweet? Or do you want something savory? Because I heard online that the doughnuts here are crazy good."
    a "But also, you shouldn't get the doughnuts because that's what I'm getting."
    a "You know what? I'll just choose for you. Get something savory and we can share with each other if it really comes down to it."
    s "Well, that certainly makes things easier for me."
    s "A little more freedom would be nice, though."

    scene amidiner2
    with dissolve

    a "You're free to do whatever you want! As long as what you want to do is love me."
    s "..."

    scene amidiner3
    with dissolve

    a "Kidding."
    a "Maybe."

    "I think my niece might be obsessed with me."

    scene amidiner4
    with dissolve

    wa "Hello, humans! And welcome to food! My name is Kaori Kadowaki and I will now write down the objects you wish to consume on this rectangular book of slaughtered trees."

    if day65 == True:
        "Isn't this the same girl that was working at the bistro where I met up with Sara and Haruka?"
        "Isn't she a little young to be working multiple jobs?"

    scene amidiner5
    with dissolve

    a "That's funny. I don't remember seeing anything online about this diner being themed."
    k "Yes! Themed! The theme here is hunger! And the characters are you and the large, intimidating man with circles of glass in front of his vision balls."
    a "You...said your name was Kaori?"
    k "Yes! That is what I am called. But you may also address me as the Mistress of the Dark or the Queen of Spiders. All of these things are true! I think!"

    scene amidiner7
    with dissolve

    k "Have you been inside of this building before?"
    a "Not yet. I've seen a lot of people talking about it online, though."
    k "On which line?"
    a "The...The Internet?"

    scene amidiner8
    with dissolve

    k "Did you also bring a net? Or did your girlfriend just require moral support for all of the flavors she is going to catch?"

    scene amidiner9
    with dissolve

    a "G-G-G-G-G-Girlfriend?! Is that who you think I am?! Does it really look that way?!"
    k "Was my assumption incorrect? I smelt a heavy dose of romantic pheromones shortly after the two of you entered the store."
    a "Pheromones?!"
    k "So strong that they are almost pulsating! I can feel them surrounding my body and squeezing me the way I long to squeeze small dogs."

    scene amidiner11
    with dissolve

    k "Treat her well or face the consequences."
    s "..."

    scene amidiner9
    with dissolve

    k "What would you like to eat, small girl?"
    a "I-"

    scene amidiner11
    with dissolve

    k "I am serious. Protect this tiny human."

    "Am I wrong for feeling mildly intimidated right now?"

    scene amidiner9
    with dissolve

    k "What is your name and how many muffins have you eaten in your life?"
    k "Please also inform me on the object on our menu that you most want to put inside of your mouth."

    scene amidiner12
    with dissolve

    a "Well, umm..."
    a "My name is Ami..."
    k "An adorable name for an adorable girl. Tell me what your desired food is called, Ami."
    a "Uhh...there's a...doughnut platter thingy, right?"
    k "That is a thing that exists. Yes."

    scene amidiner13
    with dissolve

    k "And for you, mystery man? Please list the objects you are most interested in at this very moment."

    "I'm beginning to think that Ami is right in assuming that this is some sort of themed diner, but...I can't really tell what the theme is by the way the waitress is speaking."

    s "I’ll just have a burger. Thanks."
    k "I understand. One order of fried zeros and a hot meat sandwich coming right up for the cute Ami and her human boyfriend."
    k "Please remain at this specific rectangle and I will return right away."

    scene amidiner15
    with dissolve

    "Kaori or...the mistress of whatever disappears from the table, prompting Ami and I to awkwardly resume where we left off moments ago."

    a "She’s...umm..."
    a "A little-"

    scene amidiner16
    with hpunch
    play sound "thump.mp3"

    k "I have returned with the things you wanted!"
    s "How the hell did you do that so quickly?"
    k "Do not ask questions that you are not yet prepared to hear the answers to!"
    k "For there is one nickname I did not mention when I first introduced myself..."

    scene amidiner17
    with dissolve

    k "You see before you, Kaori...the Goddess of Gluttony...the world’s greatest waitress..."
    a "How...what?..."
    s "If anything, I’m more impressed with the cooks. All you really did was carry everything over."
    s "And we didn’t even order the coffee you gave to Ami."

    scene amidiner18
    with dissolve

    k "The Ami needs the hot bean water to grow strong and develop larger bones!"
    s "I think there might be some misunderstanding on your end about the nutritional value of coffee."
    k "Do not tempt me to return your meat to the cooking zone! I will do it!"

    "Kaori quickly snatches back the burger she had placed in front of me before I’m even able to take a bite."

    s "I am so confused."

    scene amidiner19
    with dissolve

    k "You will eat when I deem you worthy."

    scene amidiner20
    with dissolve

    a "Umm...Miss Kaori?"

    scene amidiner21
    with dissolve

    k "What is wrong? Will your tiny body reject the strength of the hot bean water?"
    a "No, I just...was wondering if that spider on your chest was a real tattoo or not?"
    k "It is. Would you like to touch it?"
    a "I...don't know if I should with where it's located."
    k "I understand. Human customs say that a spider on one's body must not be touched until the seventh date."
    s "I didn’t realize there was a custom for something that specific."
    k "May I ask you a question now, Ami?"
    a "Of course. What do you want to know?"
    k "What is your favorite animal?"
    a "..."
    a "Is that...really what you want to ask?"
    k "Do you not have one?"
    a "Um...I guess...I think cats are really cute?"
    k "I see, I see."
    k "I will remember this."
    a "Okay...umm..."
    a "Thank you?"
    k "You are very welcome."

    scene amidiner22
    with dissolve

    k "As for you..."
    s "What did {i}I{/i} do?"
    k "I will allow you to eat this hot meat sandwich under one condition."
    s "And what condition would that be?"
    k "You must say one nice thing about me."
    s "What? Why?"
    k "Because you have jammed an invisible knife into my feelings and they are now deflating."
    k "Please patch me up immediately."
    s "Uhh..."
    s "You're...really attractive?"

    scene amidiner26
    with dissolve

    k "GUH!"
    k "That...That is not the type of nice thing I thought you would say, boyfriend-man!"
    a "Yeah...me neither."

    scene amidiner27
    with dissolve

    a "And I'm extra annoyed because I actually agree."
    a "You look kinda like a...rock idol or something. And you're super cool and now I'm jealous."
    k "The Ami thinks that too?! Is this what they call a gangbang?!"
    s "Uhh...no. No it's not."

    scene amidiner28
    with dissolve

    k "All I wanted was my role as the greatest waitress in the world to be validated by a large man and his miniature girlfriend!"
    k "Now, I must deal with the extra blood in my face! And all because of you two!"
    a "We...weren't trying to offend you, Miss Kaori. We just-"
    k "I will now depart! The weight of these comments has become too much for me to bear!"
    k "Please remember to like, comment, and subscribe!"

    scene amidiner29
    with dissolve

    "Kaori vanishes into the kitchen, leaving both Ami and me in a state of mild shock."
    "But, on the bright side, the room quickly grows much quieter."

    a "..."
    s "..."
    a "So, uhh...I guess we just...eat breakfast now?"
    s "What just happened?"
    a "I’m not really sure..."
    a "I kind of like her, though."
    s "What? Why?"
    a "I...don't really know."
    a "I just kind of...do."

    scene black
    with dissolve2

    "Ami and I finish up our meals without any further interruption from the diner staff..."
    "Something tells me this isn’t the last we’ve seen of Kaori, though..."

    $ renpy.end_replay()
    $ ami_love += 1
    $ amisroom5 = True
    stop music fadeout 3.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label amisroom10:
    scene lr_day
    with dissolve
    play music "shiningstarvocals.mp3" fadein 4.0

    s "..."

    "I walk into the living room to be greeted by an unfamiliar, ear-piercing sound..."
    "Apparently, Ami has decided that it is acceptable to blast music in her room at 9:00 in the morning."
    "I’m already awake, so it’s not really as big of a deal as it {i}could{/i} have been...but it’s still too early to deal with something like this."

    play sound "knock.mp3"

    s "Ami...can you turn that down a little please?"
    a "Mmm mmm hmmm...mmm hmmm hmmmmmm..."

    "She either ignores or simply doesn't hear my request as she happily hums away at whatever song is playing behind the door."

    play sound "knock.mp3"

    s "Ami, come on. It's way too early for this."
    a "Hmmm hmmm hmmmm...mmm mm mm mmm mmm..."
    s "..."

    if bonus == True:
        "Is this what it means to be the guardian of a [teenage]girl?"
        "It pains me to know that there are families out there with more than one of these things."
        "Ami’s well-behaved and cute and all that, but even I don’t know if I’d be able to deal with waking up to {i}two{/i} of her."
        "Though...I guess it wouldn't be right to ignore the prospective {i}benefits{/i} of something like that as well."

        s "..."

        "You know what? Fuck it."
        "This is my house and I have the right to barge into her room if she's not going to respond to me."
        "And if the worst (or best) case scenario happens and I end up walking in on something I shouldn't see, I can always just ask for forgiveness."
        "Especially considering that asking for {i}permission{/i} was entirely fruitless."
    else:
        "Is this what it means to be a pogchamp?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    if bonus == True:
        jump amibrax
    else:
        "I walk into Ami's room to find that she is not just humming along with some song she likes, she is the vocalist of what she refers to as the {i}best Smashmouth cover band in Kumon-mi{/i}."
        "Despite how impressed I am, I ask her to keep it down and she agrees before introducing me to all of her bandmates."
        "The next thing I know, I am decked out in their merchandise and jumping on Ami's bed."
        "Having an accountant is so fun."

        $ renpy.end_replay()
        $ amisroom10 = True
        $ ami_love += 1
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon

label amisroom15:
    scene lr_day
    with dissolve
    play music "normalday.mp3"

    "I decide to spend the morning with Ami, and not just because I don’t feel like going anywhere else this time."
    "I admit that this seemingly small factor may sometimes play a large role in determining whether I spend time with her or not, but it’s not like I don’t want to see her or anything like that."

    if bonus == True:
        "Ami and I have gotten close enough that I have basically accepted her as family at this point."
    else:
        "Ami and I have gotten close enough that I basically consider her family at this point. Which she definitely is not."

    if bonus == True:
        if amifingered == True:
            "Just...family with the added bonus of providing sexual favors for one another every now and then."
            "But whatever. Sue us. It's not like no family has ever done this sort of stuff together before."
        else:
            "The only thing is...it’s kind of hard to avoid that she might be feeling a little more than that."
            "It’s weird...When I first woke up here, I had every intention of just using any chance I had to get physically closer with her."
            "But now look at me."
            "I’m about to walk into her room and I don’t even {i}almost{/i} have an erection."
            "In fact, if I didn’t spend half of every day perving out on other [teenage]girls, I might even consider myself starting to change."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "I make my way over to Ami’s door and, as is becoming customary, decide to push it open without knocking like the true gentleman I am."
    "........."
    "......"
    "..."

    scene amisroomonefive1
    with dissolve2

    a "Hmmm hmmm hmmm~"
    a "Hmmmmm hmm hmmmmm hmmm~"

    "Ami happily hums a song to herself while sorting through her manga collection."
    "I’m surprised to see that she’s already dressed for the day when weekend-Ami has become all but synonymous with lounging around the house in her pajamas and waiting for me to talk to her."

    s "Morning. What are you doing?"

    scene amisroomonefive2
    with dissolve

    a "Ah?!"
    a "What the heck, [amimaster]? Why are you just sneaking up on me like that?!"
    a "Even if I never get mad at you for not doing it, you should still remember to knock, you know?"
    s "I don’t remember how to knock."

    scene amisroomonefive3
    with dissolve

    a "You...don't remember how?..."
    s "Yeah. I don't think my hands work that way. You'll just have to deal with this from now on. Sorry."
    a "Can you at least try to remember when it comes to knocking on other girls' doors? Because I don't want you walking in on {i}them{/i} when they're vulnerable."
    s "But with you, it's fine?"

    scene amisroomonefive4
    with dissolve

    a "Mhm. With me it's fine. But I really wish you'd at least warn me before coming in so I don't have a heart attack next time I turn around and see you there."
    a "So, does you being here mean that...you maybe want to hang out with me? Cause I was just going to spend the morning reading, but-"
    s "What were you going to read?"

    scene amisroomonefive5
    with dissolve

    a "Uhh...nothing you’d be interested in. "
    s "Try me."
    a "Okay, well...the series I’ve been reading is about this one girl with magical powers and-"
    s "Yup. Not interested."

    scene amisroomonefive6
    with dissolve

    a "I'm honestly a little surprised you even made it that far."
    s "I’m just kidding. You can keep going with your description."

    scene amisroomonefive5
    with dissolve

    a "Okay...So, she’s got magical powers and she needs to save the world from all these villains that keep showing up. "
    a "But the thing is, the biggest villain of them all is actually her childhood friend and love interest."
    s "Wow. Do you immediately spoil major details like that for everyone who asks you about something you're reading? Or am I just the lucky one?"
    a "Is it really even a spoiler if I know for a fact that you're never going to read it?"

    scene amisroomonefive7
    with dissolve

    a "Besides, you really don’t need to ask me about stuff I know you’re not interested in, [amimaster]."
    a "The fact that you’re willing to {i}pretend{/i} to be interested is enough for me."

    if bonus == True:
        s "Pretending? Who’s pretending? For all you know, I could be a huge otaku who just keeps his hobbies a secret from everyone else."
    else:
        s "Pretending? Who’s pretending? I'm a cool boy who likes cool boy things."
        s "In fact, they used to call me Cooly McCoolguy when I was in college. That's just how cool I was."

    a "Lies. You can't earn the title of {i}otaku{/i} unless you annoy other people about your hobbies and try to force them into liking the things you like."
    s "I feel like that's not true. But anyway, did you want to do something today?"
    s "It’s been a little while since the two of us just spent the whole day hanging around the house, so I figured we could do that if you don't have any better ideas?"

    scene amisroomonefive8
    with dissolve

    a "Wait, the whole day day? You mean like...morning, afternoon, and night?"
    s "Yes, Ami. Those are the three key parts of the day."
    a "So...I get to spend the entire day with you?"
    s "You do."
    a "And you’re not gonna go anywhere else?"
    s "I’m not."
    a "And you’re going to hold my hand the whole time?"
    s "Do you really think I'd fall for that?"

    scene amisroomonefive9
    with dissolve

    a "Heheh...I thought I might be able to fit that in there without you noticing."
    s "Holding hands for an entire day sounds a little too cute for my liking. I'm not sure if my mind or body would even allow it. "
    a "Are hugs too cute for your liking as well? Because I haven't gotten one of those yet and I'm starting to think you woke up anti-Ami today."
    s "I have literally been in here for five minutes and, within that time, already devoted my entire day to you. What more do you want?"
    a "An amount of hugs that is...bigger than zero?"
    s "Pass."

    scene amisroomonefive10
    with dissolve

    a "What’s even the point of spending the whole day together if I'm not allowed to hug you?! What else do you wanna do, Sensei?! Talk about the economy?!"
    s "What? No. Why would you even assume that?"
    a "Because it's the most boring thing I can think of and you are clearly only here to play with my feelings by not hugging me!"
    s "How about we just watch TV or something? That’s a thing we can both enjoy, right?"
    s "And hey, if you let me choose what we watch, I think I can be kind enough to let you hug my arm for a few minutes at a time so long as you don't squeeze too tightly."
    a "I don’t need permission to hug my [uncle]’s arm!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    a "Hey! Where are you going?! You can't just leave like that without saying anything!"
    s "I'm going to the living room before I wind up being assaulted by a five-foot redhead."
    a "I’m five-foot-two! This is a thing you should know!"
    a "Pay more attention to me!"

    "I exit Ami’s room and take a seat on the couch, waiting for her to join me."
    "I obviously have no problem hugging her or holding her hand or any of the other annoyingly adorable things she’s somehow able to say without blushing in the comfort of our home-"
    "It’s just really fun to tease her."
    "And I intend to continue doing that for the rest of our time together."
    "........."
    "......"
    "..."

    scene amisroomonefive11
    with dissolve

    a "..."
    s "..."
    a "You don’t love me anymore."
    s "You got me. All of the love inside of me has faded into nothingness."
    a "That’s fine. I just won’t cook you dinner anymore."
    s "Nevermind. I love you again. Please don't stop cooking for me. I will die."

    scene amisroomonefive12
    with dissolve

    a "Yay! You told me you loved me and I didn't even have to ask!"
    s "Yup. That is definitely what happened."
    s "This means you'll keep making me dinner, right?"

    scene amisroomonefive13
    with dissolve

    a "Heheh...we’ll see. Dinner’s not until much later in the day, so you’re going to have to be extra nice to me if you want to eat."
    s "I’m a prisoner in my own home."
    a "That’s right. And I, Ami Arakawa, am the true protagonist of this story."
    s "Does that mean I’m your childhood friend-slash-villain of the story like in that manga you were talking about earlier?"

    scene amisroomonefive14
    with dissolve

    a "I wish...It would be so much easier if the two of us were childhood friends."

    if bonus == True:
        a "Why did you have to go and be born like a million years earlier than me? And also be related to my dad?"
        a "You’re just putting roadblocks all over this relationship, [amimaster]."
    else:
        a "Why did you have to go and be born with brown hair? My parents would never approve of this relationship if they were still alive."
        s "Is my hair really such a problem?"
        a "Between that and all of your incredibly unkind opinions on revolving doors, it's like you're intentionally just putting roadblocks all over this relationship."

    if amifingered == True:
        s "I don’t know. I kind of like you the way you are."

        scene amisroomonefive15
        with dissolve

        a "Huh?"
        s "Yeah. I don’t know if the two of us ever would have gotten close if it wasn’t for our relationship."
        a "Can you...tell me you like me the way I am again, please?"
        s "No. That was your one compliment for the morning. You’ll get another in the afternoon. Please look forward to it."

        scene amisroomonefive16
        with dissolve

        a "Guess I’ll take what I can get, then..."

        scene amisroomonefive17
        with dissolve

        a "Besides, I...also like the way things are now. And even though you’re a big dummy jerk-pants who won’t hold my hand, I know I can rely on you."

        if bonus == True:
            a "I’d still probably feel safe with you if we were the same age but...I don’t know."
            a "I..."
            a "I’m probably gonna start ranting about weird stuff if you don’t stop me."

        "I wait for a moment to see if Ami continues."

        a "Sensei, this is the point where you’re supposed to stop me."

        "Damn it."

        s "Fine. Stop."

    else:
        s "What am I putting roadblocks over exactly? We’re just [uncle] and [niece]. The way things are now is fine."

        if bonus == False:
            s "Besides, if they're going to call them {i}revolving{/i} doors, they should at least be ensuring that they revolve 100%% of the time and that I don't have to physically push them in order to get through."

        scene amisroomonefive17
        with dissolve

        a "Uhh...yeah. I know. I was just...making a joke or something."
        a "Of course I know that...all we are is [uncle] and [niece]..."
        a "And that's...probably all we'll ever be."

    "Ami reaches out and grabs the remote for the TV, switching it on and turning it to some early-morning kids anime."

    s "I'm fine with you putting on whatever, but I didn't think you'd just waive your right to hugging my arm in short bursts throughout the rest of the morning so easily."

    scene amisroomonefive18
    with dissolve

    a "You say that like you have any influence over when and where I hug you."
    a "Also, why would I give up control of the remote when you’d just put on something lame like the news?"
    s "When have I literally ever put on the news before?"
    a "You used to put the news on all the time to try and get me to go to sleep when I was younger."
    s "Did it work?"
    a "Yeah, cause the news is boring."
    s "Cool. Then let's put the news on. You've had a long day and deserve the rest."

    scene amisroomonefive18r
    with dissolve

    a "I've been awake for half an hour!"
    s "Wow, it's been that long already?"

    scene amisroomonefive19
    with hpunch

    a "That's it! I'm hugging you now and you can't do anything about it!"

    "Ami lunges at me and latches onto my arm, digging her fingers into my skin and squeezing me so hard that there's honestly a chance I could bruise from it."

    s "I guess I kind of asked for this by teasing you, didn't I?"

    scene amisroomonefive20
    with dissolve

    a "That's right. The meaner you are, the nicer I have to be to make up for it. Sorry not sorry."
    s "What exactly is “Sorry not sorry?”"
    a "A thing that you would know if you weren't a dinosaur."
    s "Me being a dinosaur implies that you're part-dinosaur, doesn't it?"
    a "Nuh-uh. I didn’t get the dino gene. I’m a purebred cute girl who must be protected."
    s "Protected from what? We’re the only two people in the house."

    scene amisroomonefive21
    stop music

    a "You don’t know that."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."

    scene amisroomonefive22
    play music "normalday.mp3"

    a "Just kidding! Hahahahaha..."
    s "..."

    scene amisroomonefive23
    with dissolve

    a "Oh! [amimaster]! I’ve actually seen this episode before!"
    a "This is the part where two childhood friends have to fight each other to prove who’s strongest!"
    s "What is it with anime and this childhood friend trope? How often do people even keep friends from their childhood around?"
    a "Shhh, don’t ask questions about anime! Just accept it! Now watch."

    "The TV begins to flash as one of two unbelievably muscular characters start...charging up or something like that."
    "I'm probably wrong due to being a {i}dinosaur,{/i} but it's at least worth a guess."

    scene amisroomonefive24
    with dissolve

    a "Guh...I can’t remember who wins this fight. I’m getting nervous."
    a "You don’t mind if I squeeze you a little harder, right? Cause I’m gonna do that."
    s "I do mind, actually. But I accept that I lack the power or the resolve to stop you."

    scene amisroomonefive25
    with dissolve

    a "Oh. Wait. I remember who wins now. It’s the protagonist."
    s "Are you just going to spoil everything today?"
    a "Watch this, [amimaster]. The guy with the black hair is going to have his arms ripped off."
    s "Is that really a thing they can put on TV so early? It’s like 9 AM. "
    a "They got rid of censorship laws here years ago, don’t you remember? You’re allowed to show anything you want on TV now as long as it’s not a penis."
    s "What’s with this bias against penises? That's just plain unfair."
    a "Stop talking about penises and focus. {i}Shit's about to get real.{/i}"
    s "..."

    "You know, if you asked me to make a list of all of the things that would ever be said to me-"
    "I don’t think that last thing would have made it on there."
    "..."
    "I stop talking about penises and focus because shit is about to get real."

    scene amisroomonefive26
    with dissolve

    a "YEAAAAH! FUCK HIM UP!"
    a "TEAR HIS STUPID FUCKING ARMS OFF!"
    s "I have learned today that I really don't like the person you become when you watch anime."
    s "I think you’re changing and it worries me."

    scene amisroomonefive27
    with dissolve

    a "Too bad, [amimaster]. Because we’re gonna watch this all day."
    s "..."
    a "..."
    s "Are you sure you don't want to put the news on?"

    scene black
    with dissolve2

    "Ami, once again, refuses to change the channel and the two of us spend almost the entire day sitting on the couch and watching anime."
    "And despite me not understanding literally anything that is going on at any point, it’s still kind of fun, I guess."
    "Sure, my arm may have fallen asleep two or three hundred times over the last couple hours alone, but that’s beside the point."
    "Eventually, the show’s marathon comes to an end and the two of us get up to stretch out our limbs."
    "I never understood how broken your body can feel after just sitting in one place for an extended period of time."

    scene importantredux1
    with dissolve2

    a "Sensei, do you want to go ahead and take a bath while I start making dinner?"
    s "Oh, sure. What are you going to make?"
    a "Hmm...would beef be okay? Or maybe hamburger steak?"
    a "I’m kind of in the mood for something hearty and I don’t think we have a lot of ingredients left for other stuff anyway."
    s "Works for me. You’re sure it’s okay if I go in first?"
    a "Of course. We skipped lunch today, so I know you’re probably excited to eat."
    a "Having dinner ready by the time you get out will be my special present in exchange for you spending the whole day with me today."

    "It’s moments like this that truly make me realize just how good I have it right now."
    "I’ve got a job I don't inherently hate."
    "A home."
    "And someone willing to look after me even when I don't deserve it."
    "Life can’t get any better than this, right?"
    "..."
    "Life can't get any better..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."
    "I open the bathroom door and begin to fill the tub with water."
    "I take my clothes off, leaving them on top of the sink in the corner of the room, and get in once it’s full."

    play sound "water1.mp3"

    "..."

    scene senseibath
    with dissolve
    stop music fadeout 15.0

    s "..."

    "I let the water soak into my skin and wash away the exhaustion that comes from watching shonen fight scenes all day. "
    "I’m glad that Ami and I got to spend a whole day together for a change."
    "More often than not, I find myself just moving from one place to the next without thinking much of it."
    "But every once in a while, it really is nice to slow things down."
    "I should do things like this more often."
    "Hell, maybe I should even quit teaching and just stay at home full-time. "
    "NEET-life sounds pretty good now that I have a [niece] who waits on my every beck and call."
    "But, then again...that would mean forcing Ami to work. And for the time being, I just can’t envision that."
    "Call me selfish, but..."
    "I'd like to keep her as my own for a little while longer."

    s "..."

    "Oh well. "
    "It is what it is. I guess."

    scene black
    with dissolve2

    "I close my eyes and give in to the comfort that comes with warm water and heated porcelain. "
    "And..."
    "Within a matter of minutes..."

    if amifingered == False:
        "I can feel myself dozing off."

        $ renpy.end_replay()
        $ ami_love += 1
        $ amisroom15 = True
        stop music fadeout 7.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        scene bedroom_night
        with dissolve

        "The stew Ami made wound up being absolutely delicious. "
        "The two of us cleaned out the entire pot and Ami went into a food-coma shortly after."
        "Left with nothing else to do for the night, I decide to go to sleep a little earlier than normal."

        scene black
        with dissolve2

        if day == 6:
            jump advancetosun
        else:
            jump advancetomon

    else:
        "........."
        "......"
        "..."
        play sound "slidedoor.mp3"

        s "...?"

label amisfirsttime:
    if bonus == True:
        jump amisfirsttimex
    else:
        scene black
        with dissolve

        "A ghost opens the door and I need to fight it off to protect my home."
        "I emerge victorious."
        "No ghost can defeat me."

        $ renpy.end_replay()
        $ ami_love += 1
        $ ami_virgin = False
        $ amisroom15 = True
        $ specialclassroom = True

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        if day == 6:
            jump advancetosun
        else:
            jump advancetomon

label amisroom20:
    scene cutegirlredux1
    with dissolve
    play music "amiamiami.mp3"

    "I step out into the living room after deciding to spend the morning with Ami."
    "I feel like it’s been quite a while since the two of us have done anything other than just lounge around the house together, so maybe she’ll actually want to get out today?"
    "There’s only so much I can take of being stuck inside the house with a cute girl who will cook and clean for me and-"
    "..."
    "Wait, why am I complaining again?"

    a "Good morning, [amimaster]. Are you done narrating your thoughts inside of your head and ready to pay attention to me?"
    s "I guess so."
    a "Did you sleep well?"
    s "Well enough. How about you?"
    a "Really good, actually! And I’m glad you’re finally up because I was just thinking that it’s been a while since the two of us did anything fun together."
    s "Ami, are you able to read my mind? Because this is starting to get weird."
    a "Yup! I'm a mind reader. And right now, you're thinking that you want to take me shopping."
    s "On second thought, why don't I just sit on the couch and have you cater to me for the rest of the day? "

    scene cutegirlredux2
    with dissolve

    a "That’s what I always do, though!"
    s "And you're very good at it."

    scene cutegirlredux3
    with dissolve

    a "Flattery will get you nowhere, [amimaster]."
    s "Oh, come on. We both know that's not true."

    scene cutegirlredux4
    with dissolve

    a "Are we really not going to do anything today?"
    s "What exactly do you even need to go shopping for? "
    s "Please explain to me in detail why I must use my hard-earned money on things that you require."

    if bonus == True:
        a "Because...you’re my legal guardian and I don’t have a job?"
    else:
        a "Because I am your accountant and I'm telling you that it is the right move financially."

    a "I can’t just stay in the same clothes forever, you know."
    s "Well, it hasn’t seemed like a problem so far."

    scene cutegirlredux2
    with dissolve

    a "It’s a huge problem! A colossal one!"
    a "How am I supposed to know you love me if you never pamper me?!"
    a "And also, your money isn’t hard-earned at all! You never even do anything!"
    a "You’re the worst teacher ever!"

    if bonus == False:
        s "How {i}dare{/i} you?"

    s "Are you throwing a temper tantrum right now?"
    a "Are YOU throwing a temper tantrum right now?!"
    s "I just want to eat breakfast."

    scene cutegirlredux3
    with dissolve

    a "No. You just want to hate me and take advantage of my undying love for you."
    s "I'm not {i}taking advantage of you,{/i} Ami."
    a "You only like me because I’m a good cook and I do your laundry."

    if ami_lust > 10 and bonus == True:
        a "And also because I touch your penis sometimes."

    s "Well...I mean, that’s not {i}entirely{/i} inaccurate."

    scene cutegirlredux5
    with dissolve

    a "So, what better way to make it up to me than by taking me to the mall and letting me look at a few things?"
    a "We don’t actually need to {i}buy{/i} anything. "
    a "I can just stare at all of the cute clothes I {i}could{/i} be wearing if my [uncle] actually cared about me."
    s "Can you at least make breakfast first?"
    a "Yes, but only if you promise to go with me right now and not wait until after you're done eating to change your mind."
    s "Stop being so perceptive. I don't like it."

    scene cutegirlredux6
    with dissolve

    a "Yay! You didn't say no, which means that you're okay with it!"
    s "Those words would not hold up in court, you know."
    a "Sure they would! Now go get dressed while I make you breakfast."
    s "Ugh, fine. I’ve already accepted that I’m not going to be able to talk you out of this anyway."

    scene black
    with dissolve

    "I head back into my bedroom and put on the same outfit I put on every day, wondering if maybe {i}I{/i} should splurge on some new clothes as well."
    "I ultimately decide against it, though, because if either one of us is going to actually benefit from some new clothes it's Ami."
    "Say what you want about the lack of variety in my wardrobe, but I am a young-ish adult male who has already won over a multitude of girls without having to do much-"
    "And Ami is one of those girls, who I'm sure wants to look even prettier for a better chance at coming out of love-gauntlet in first place."
    "Unfortunately, things like that don't come without a cost. And in this case, that cost is going to be my money."

    scene sky
    with dissolve

    "Unless...I use today to convince her that it might be time to get a job of her own."
    "I remember her telling me in the past that she had a secret source of income, but I subsequently found out that source of income was one of my credit cards when the bill showed up in the mail."
    "That source of funding has been cut off, leaving her with nothing to her name except the clothes on her back and the various manga she acquired through low level identity theft."
    "The only issue I can think of when it comes to her getting a job is the whole part where she'd need to separate from me."
    "So I'll just have to figure out how to spin things in a way that makes it sound like this would be good for both of us."
    "If I'm able to do that, then-"

    a "Sensei! Are you ready yet? Or are you thinking stuff again?"
    s "I am always thinking stuff. That is what it means to have a brain."
    a "Well, use your brain to finish putting your clothes on because breakfast is ready and I want clothes!"
    s "..."

    scene black
    with dissolve2

    "I sigh to myself while sliding off my shirt, wondering if a day will ever come where I need to start doing things for myself."
    "..."
    "I hope not."
    "That would suck."
    "........."
    "......"
    "..."

    scene amimall1
    with dissolve2

    "Ami hangs her arm over the railing, overlooking a surprisingly low amount of people for a weekend morning."
    "She smiles as I take my place next to her, but doesn’t pay much attention to me right away."

    a "You know I was only half-messing around with you this morning, right?"
    a "I know you would have caved and brought me here anyway if all I did was ask nicely. "
    a "Sure, you might be a freeloader who never really does anything around the house, but you care about me and buy me food and that’s all that matters."
    s "I have no idea whether that's a compliment or an insult."

    scene amimall2
    with dissolve

    a "Can it not be both?"
    a "I kind of like how lazy you are. It gives me more excuses to spend time with you and validates my purpose in this world as a caring and attentive [niece]."
    s "That’s right, Ami. Which is why I’ve decided to do something very special for you today."

    scene amimall3
    with dissolve

    a "Special? What do you mean?"

    "I reach into my pocket and pull out a wrinkled 1,000 Yen note and hold it out toward her."

    s "This is yours. Don’t spend it all in one place."

    scene amimall4
    with dissolve

    a "Wow! Sensei! I didn’t think you’d actually-"

    scene amimall5
    with hpunch

    a "Hey, wait a second! That's only 1,000! What the heck am I supposed to buy with that?!"
    a "I can’t even get a skirt with that much!"
    s "You can buy socks. Those are cheap, right?"
    a "I don’t need socks! I have a million socks!"
    s "This is literally all I have on me."

    scene amimall6
    with dissolve

    a "Nuh-uh! I know from past experience that you have a credit card."
    s "What happened to the whole “You don’t need to actually buy me anything” bit from earlier? Can we go back to that?"
    a "I was obviously just being polite when I said that. You need to get me at least {i}something{/i}."
    s "Why don’t you just get a job if you’re so concerned about money?"

    scene amimall7
    with dissolve

    a "Umm...Aren’t {i}you{/i} my job?"
    s "I guess I kind of am. But why not get a second one, then?"

    scene amimall8
    with dissolve

    a "Hmm..."

    "Ami looks over the railing as a trace of concern spreads across her face."
    "If I know her well enough (Which I’m pretty sure I do), she’s probably thinking about whether or not it’s worth sacrificing her time with me in exchange for material goods."
    "And if I know her even better than that (Which I’m pretty sure I do), I expect her to come out and say that she’d rather stay with me than-"

    scene amimall9
    with dissolve

    a "What kind of job do you think I should look for?"
    s "Wait, what?"
    a "What? You said I should get a second job, so the least you can do is help me think of one."
    s "I thought your love for me was going to trump your desire for material goods. That's how this played out in my head."
    a "Obviously, my love for you will always come first."
    a "But I’m still a girl who wants cute stuff and tickets to concerts and blah blah blah and you won’t give me more than 1,000 Yen because you hate me."

    if bonus == True:
        s "I don’t hate you, I just...don’t know the standard cost of clothing for a girl your age."
        a "You’d think that years of buying clothes for a girl my age would have ingrained that into your memory by now."
    else:
        s "I don't hate you. I just feel as if you might be taking advantage of my lack of knowledge in the economic space."
        a "..."
        a "But I make you breakfast and stuff."
        s "Good point."

    s "Ami, if you get a second job, who is going to make me breakfast in the morning?"
    a "Who said I’m going to work mornings?"
    a "You can’t go making my schedule for me when I don’t even have a job yet."
    a "Especially when we don’t even know what my job is going to be."

    "A job for Ami, huh?..."
    "There is {i}one{/i} thing that pops into my mind, but I’m not really sure if she’d go for it or not."
    "In fact, the only reason it popped into my mind at all is that I kind of just want to see how she’d look in the uniform."

    s "What about a maid cafe? "
    s "There’s one nearby, isn’t there?"

    scene amimall10
    with dissolve

    a "There is but...why do {i}you{/i} know about it?"
    a "That place is still kind of new and I thought Maya, Ayane and me were the only ones who went there."

    "What I can’t tell Ami is that Maya {i}is{/i} the reason I know about it."
    "I’ll just let her assume it was Ayane that told me or something."

    s "How I know about it doesn’t matter."

    scene amimall11
    with dissolve

    a "Hey, hold on a second, dearest [uncle]."
    a "You disappear for most of the day on weekends and I never really ask where you go."
    a "Combine that with how you don’t want to give me money and..."
    s "...And what?"

    scene amimall12
    with dissolve

    a "You’re addicted to maid cafes, aren’t you?!"
    s "..."
    s "Excuse me?"

    scene amimall13
    with dissolve

    a "I mean...I guess that would make sense given how much you like cute girls and stuff. But I didn’t think you’d be spending {i}every waking moment{/i} there."
    s "I think there’s some sort of misunderstanding. I’ve only been there-"

    scene amimall14
    with dissolve

    a "Wait...but if you spend every waking moment there..."

    scene amimall15
    with dissolve

    a "If I was hired at the maid cafe, I’d get to spend every waking moment with you!"
    s "..."
    a "And I already know everything you like! So your service would be amazing and you’d be forced to give me all of your money!"
    a "I love this idea!"

    if bonus == True:
        a "I love it so much that I’m going to ignore your newly-discovered maid fetish!"
    else:
        a "I love it so much that I’m going to ignore how much you apparently like maids!"

    s "I mean...I don't know if I'd call it a {i}fetish...{/i}"

    scene amimall16
    with dissolve

    a "Any fetish you have is fine with me, Sensei."
    s "I really don't like how nonchalantly you said that."
    a "Would you want to come with me soon and see if they’re hiring or something?"
    a "I’d feel a lot more confident about applying if you’re there with me."
    s "Aren’t you worried that I’m going to spend all of my money on the other maids while we’re there?"
    a "No. Because if you even talk to them, I will cut your fingers off and feed them to ducks."
    s "Joke's on you, ducks are primarily herbivores and probably wouldn’t even eat human fingers."
    a "Joke's on you, I raised an army of carnivorous ducks and have been hiding them behind the dorms. "
    a "They’re ready to eat your fingers at a moment’s notice."

    if bonus == True:
        s "I have several questions but I’m going to ignore them and replace them all with the thought of you calling me Master."
    else:
        s "I knew there was something weird about those ducks."

    if bonus == True:
        scene amimall17
        with dissolve

        if amimaster == "Master" or amimaster == "master":
            a "That’s exactly what I’ve been calling you for a while now. "
            a "Don’t tell me you’re thinking of things like {i}that{/i} in the middle of the mall...are you, Master?"
            s "I plead the fifth. This conversation is supposed to be about you getting a job."

        else:
            a "You know I’d be okay with calling you that regardless, right?"
            a "If that's really your end-goal, we can just skip the job part if you want~"
            s "If we skip that part, you’ll be unemployed forever."

    scene amimall18
    with dissolve

    a "What if I’m not good, though?"
    a "I really only know how to take care of you, not other men."
    s "There aren’t even that many men left in Kumon-mi. "
    s "If any of them hit on you, just...say you’re into girls and tell them to go away or something."
    a "I’m pretty sure that sort of thing would get me fired from a maid cafe."
    s "Probably. But there’s always a chance they could just think that’s your archetype or something."

    scene amimall19
    with dissolve

    a "Oh! You mean like a...tsundere maid?"
    s "Sure. Let's go with that."

    scene amimall20
    with dissolve

    a "I-Idiot...It’s not like I even want to be a maid or anything..."
    s "See? You'll be just fine. You've already got the character down better than Yumi and she's been doing this for years."

    scene amimall21
    with dissolve

    a "You better not be implying that Yumi actually likes you or something, [amimaster]..."
    s "Of course not. Yumi doesn't like anyone. That's why I said you have the character down {i}better{/i} than her."

    scene black
    with dissolve2

    a "Likely story...Now I have to add another name to my list."
    s "List? What list?"
    a "Don't you worry about it, Sensei."
    a "Don't you worry at all..."

    "Ami and I walk around the mall for a little while longer as we go over other possible scenarios that might occur if she actually gets a job at a maid cafe."

    if bonus == True:
        "The one that sticks out in my head amongst the others, however, is that she could walk around the house wearing the costume."
        "Is this something a typical adult male should be excited about when concerning his [teenage][niece]? Probably not."
        "But I am no typical adult male. "
        "Trading away my morals has allowed more space within me think about things others would not dare think of."
        "And it’s that exact thought process that makes me go from worrying about a distinct lack of Ami around the house to eagerly awaiting her prospective future in the workforce..."
    else:
        "It sounds like a rather lucrative business, which would allow her to grow her income exponentially and provide a more comfortable retirement for her."
        "And, as her pogchamp, I should be respectful and understanding of that."


    $ renpy.end_replay()
    $ amisroom20 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label amisroom25:
    scene lr_day
    with dissolve
    play music "normalday.mp3"

    "I step out into the living room ready to start the day."
    "I’m immediately discouraged when I do not see breakfast on the table and decide to go back to sleep instead."

    scene black
    with dissolve

    "........."
    "......"

    scene lr_day
    with dissolve

    "Just kidding."
    "That never happens."
    "Instead, I go into the fridge and pull out a half-gallon of milk, taking a few sips directly from it because I am a man who simply can not be controlled."
    "That and I just don’t feel like making breakfast for myself."
    "Where is Ami, anyway? "
    "It’s rare that I’m up before her."
    "Could this be another opportunity to walk directly into her room without any concern for her privacy?"

    scene black
    with dissolve

    "Yes. I believe it can."

    play sound "dooropen.mp3"

    s "Ami, are you awake?"
    a "Oh, Sensei! Good morning!"

    scene amimaidsex1
    with dissolve2

    if bonus == True:
        "When I open Ami’s door, I'm hoping to find her in her underwear or something along those lines, but what I actually find is much greater."
    else:
        "I open Ami's door and prepare to hug her."

    s "Did I die and go to wherever that place people go when they die is?"
    a "There are lots of different places people think they go when they die, but you’re just in my room."
    s "I didn't even know you brought that outfit home with you."
    a "Uta found me one in my size that I stuffed into my bag before we left."
    a "What do you think? Am I adorable?"
    s "Adorable is a bit of an understatement. I’d actually appreciate it if you’d just never take this off again. "
    s "Thank you in advance for your cooperation."

    scene amimaidsex2
    with dissolve

    a "And I assume you’ll be wanting me to call you Master, too?"
    a "You know, just for practice obviously. Since I’m going to have to do a lot of that in the near future."
    s "You are forbidden from calling anyone else that name."

    scene amimaidsex3
    with dissolve

    a "Hey! {i}You’re{/i} the one who convinced me that this wasn’t a totally horrible idea, so I at least have to follow through and do it correctly."
    a "We can’t have two slackers in the house, now can we?"
    s "I guess not. Just try not to get too attached to any of the few male customers you’ll get in the future."
    s "I don’t want to wake up one day and find out that you’re moving into some random guy’s house instead of living here."

    scene amimaidsex4
    with dissolve

    a "I’d rather die than do something like that. Don’t worry."
    a "Besides, you need me in order to survive. So much so that I’m kinda worried about starting this {i}second{/i} job in the first place. "
    s "It’s fine. Like you said, I’m not normally home for most of the weekend anyway."
    s "And if I get to see you in your uniform whenever I want, this job is just as beneficial for me as it is for you."
    s "Any idea what you’re going to buy with your first paycheck?"

    scene amimaidsex5
    with dissolve

    a "Not a clue. I don’t even know what I’m getting paid yet. "
    a "Uta hasn’t told me when I’m starting either so I’m kinda just trying on the costume to see how I look and stuff today."
    a "She was definitely right about it making me feel prettier than I actually am."
    s "I mean, you’re pretty adorable to begin with. But yeah, this costume is good. I support this look."

    scene amimaidsex6
    with dissolve
    with dissolve

    a "Of course {i}you{/i} support it, Master. You and your unhealthy maid addiction."
    s "I can assure you this addiction is completely healthy for both of us. "
    a "Healthy for me? I’m gonna need you to explain why, dearest [uncle]."
    s "Why do I need to explain anything? I think our relationship has progressed enough for you to understand what that means."
    a "I have no idea what you’re talking about."
    a "I need to be a tsundere maid now, remember? I don't even like you that much."
    s "Tsundere Ami makes me feel weird. Dote on me more."

    scene amimaidsex7
    with dissolve

    a "Now why on earth would I do that? I have the upper hand here, Sensei~"
    a "I know how much you want to hug me and coddle me and keep me all to yourself right now and I-"

    if bonus == True:
        jump amisroom25x
    else:
        scene black
        with dissolve2

        "I seize the opporunity to hug Ami."
        "She enjoys the hug because hugs are good. The end."

        $ renpy.end_replay()
        $ amisroom25 = True
        $ ami_love += 3
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdayafternoon

label amiinvite1:
    play sound "phonebeep.wav"

    "I tap on Ami’s name in my phone and wait for her to answer."
    "I’m feeling a bit out of it today, so it would probably be nice to just lounge around the house with her."
    "Plus, something like this is definitely easier and significantly less risky than inviting anyone else over."
    "Slightly strange, considering that she lives {i}with{/i} me and inviting her to her own house is conceptually weird-"
    "But yeah, definitely easier."

    if invitetip == False:
        call invitetip from _call_invitetip_3

    play sound "phonebeep.wav"

    a "Hello? [amimaster]? What’s up?"
    a "Did you need something?"
    s "Hey, Ami. Are you doing anything today?"
    a "Hm? I’m just making dinner right now. Are you coming home early?"
    a "Want me to save you some?"
    s "Actually, I was wondering if you’d want to come over today."
    a "..."
    s "..."
    a "Come over where?"
    s "Come over our house."
    a "You’re...inviting me to...our house?"
    a "But I...just told you I'm here."
    a "Are you okay? Did you hit your head somewhere?!"
    a "Hold on, [amimaster]! I’ll call an ambulance!"
    s "No ambulance needed. "
    s "I just wanted to make sure you were okay with visiting your own house."
    a "The ambulance is on the way, [amimaster]! Just hold on!"

    scene black
    with dissolve

    "I manage to convince Ami to call off the ambulance as I walk home."
    "Thankfully, we don’t live in the US and thus incur no additional fees after she has one dispatched."

    play sound "phonebeep.wav"

    "I end the phone call as I make my way to the door, sliding my cell back into my pocket as I turn the handle."

    play sound "dooropen.mp3"
    stop music fadeout 15.0

    "Ami greets me with a hug and sets out a plate for me on the table that I promptly devour."
    "Once she finishes hers (Which takes exponentially longer- that girl eats very slowly), we make our way into {i}my{/i} room for once."
    "Typically, if the two of us were going to hang out, it would be in either the living room or, in some rare cases, her room."
    "So having her in here is actually kind of odd now that I think about it."

    scene amifirstinvite1
    with dissolve2
    play music "acoustic.mp3" fadein 5.0

    a "Wow...I can’t even remember the last time I was in here."
    s "Probably the last time you had to come wake me up or clean my room."
    a "Besides those times, obviously. "
    a "I mean just...hanging out in here."
    a "You’ve been getting better at waking up when I call out to you anyway. There’s barely a reason for me to actually come in anymore."
    a "So...why are we in here today?"

    if ami_virgin == False:
        a "Sexy stuff?"
        s "Surprisingly, no."

    s "I’ve been feeling really tired all day, so I kind of wanted to just relax and hang out with my one and only [niece]."
    a "Why are you specifying that I’m your one and only [niece]? Wording it like that makes me think you’re hiding something."
    a "[amimaster], if you’re hiding any extra [niece]s from me, I {i}will{/i} destroy them. I want you to know that."
    s "Yeah, that’s...not a thing you need to worry about."

    scene amifirstinvite2
    with dissolve

    if ami_virgin == False:
        a "Hooray! Now I know your [incest] fetish is specific to me and me only!"
    else:
        a "Hooray! Now I don’t have to worry about anyone taking you from me!"

    s "Calm down, Ami."
    s "What you and I have together is special."
    s "There's no one who could ever take your place."

    scene amifirstinvite3
    with dissolve

    a "Okay, something’s going on, isn’t it?"
    a "First, you come home on time. Then you take me into your room...and {i}now{/i} you’re saying adorable stuff to me."
    a "Is everything okay, [amimaster]? I don’t know if the ambulance made it back to the hospital yet, but-"
    s "Again, I’m okay. Stop threatening to call ambulances each time I act out of character."
    a "Sorry. I’ve just gotten so used to you neglecting me lately that the sudden increase in attention is making me nervous."
    a "Like you’re about to break some bad news to me or something."
    s "Actually, now that you mention it, I do have some bad news."

    scene amifirstinvite4
    with dissolve

    a "Ah! Here it comes! I thought I was ready but I’m really not!"
    s "You, see Ami...I-"

    if bonus == True:
        a "You {i}do{/i} have hidden family members you never told me about, don’t you?!"
    else:
        a "You {i}do{/i} have other accountants, don’t you?!"

    a "How many of them have twintails?! "
    a "Tell me or I’ll kill myself!"
    s "I was just going to say my legs are tired from walking all the way home and that I want to sit down."

    scene amifirstinvite5
    with dissolve

    a "Oh."
    a "Your definition of “bad news” is a lot different from mine."
    s "I can see that."

    scene amifirstinvite6
    with dissolve

    a "How’s that even bad, [amimaster]? "
    s "You had just gotten so into voicing your concern for me that I felt a little bad about having to interrupt you."
    s "But if you’d like to keep talking about how awesome I am, feel free. I’m just going to sit down for it."

    scene amifirstinvite2
    with dissolve

    a "Then I’ll sit down with you! I’m not just gonna stand here and keep shouting across the room. That would be weird."
    a "In fact, I’m gonna get all up in your space and rub up against you to mark my territory."
    s "Are you an animal now?"

    scene amifirstinvite7
    with dissolve

    a "Do you have a purrrrrroblem with that, [amimaster]?~"
    s "Not as long as I can feed you out of a bowl and keep you up to date on your shots."
    a "Heheh, I knew you’d li-"

    scene amifirstinvite8
    with dissolve

    a "Wait, why is {i}that{/i} the first thing your mind went to? Don’t you wanna pet me or scratch my chin or something?"
    s "Once I confirm you’re properly vaccinated, of course."
    a "..."
    s "..."
    a "Just go sit down, already. Clearly the cat thing isn’t something you’re interested in right now."

    scene black
    with dissolve

    "Ami follows me as I make my way to the bed, waiting for me to sit down before-"

    a "Move your legs a little."
    s "What, why?"
    a "I said move ‘em, mister!"
    a "Here, I’ll do it for you-"
    "........."
    "......"
    "..."

    scene amifirstinvite9
    with dissolve

    a "Welp, this is better than nothing, I guess."
    a "So, where were we?"
    a "You were talking about how much you love me, right?"
    s "That is not a thing I have said even once today."
    a "Are you sure? I distinctly heard an “I love you, Ami” as soon as you came home tonight."
    s "Probably just the voices inside of your head or something."
    a "I don’t think so. Those are a lot less reserved."
    s "Wait, you don’t actually have-"
    a "Hey, [amimaster]...do you remember how this room used to look before I moved in?"

    "I can’t even remember my name, let alone something that happened before I “existed” here."

    s "I can’t say I do."
    a "Really? "
    a "I guess that makes sense, though. "
    a "You were a lot different back then. A lot more...spacious?"
    s "Are you calling me fat?"
    a "No, no. What’s the word for when somebody like, wanders around and doesn’t really have any idea what they’re doing and stuff?"
    s "Oh. I think you’re thinking of “spaced out.”"

    scene amifirstinvite10
    with dissolve

    a "Yeah, yeah! That!"
    a "You were always super spaced out. To the point where you’d have food from like, weeks ago still out on your desk and bottles all over the floor and stuff."

    scene amifirstinvite11
    with dissolve

    a "But you weren’t exactly in the best state of mind back then. And, to be fair, neither was I."
    a "We were both really lazy for way longer than we ever should have been."
    a "I guess it’s kind of good that we wound up breaking each other out of it, huh?"
    a "Imagine how things would be if the house was still like that?"
    a "Filled with rotting food and discarded tissues from all of our tears..."
    a "Well, my tissues were from tears. Yours were probably from a few things."
    s "This conversation went from sentimental and cute to mildly disturbing within a matter of seconds."

    scene amifirstinvite12
    with dissolve

    a "Heheh~ You’re a growing boy, [amimaster]. Things like that are natural."

    if ami_virgin == False:
        a "You never would have needed all of those tissues if you’d have just pounced on me earlier, though."
        a "That would have snapped me out of my slump, {i}really{/i} quick. Like pressing a reset button."

    s "Okay, well, on a slightly different note, I’m glad that things aren’t like that anymore."
    s "I don’t think I’d be able to live if the house was that filthy."

    scene amifirstinvite13
    with dissolve

    a "What we were doing back then could barely be called “living” anyway. "
    a "We were kinda just drifting along from one day to the next, surviving off of garlic bread and soda."
    s "So I {i}was{/i} spacious after all..."

    scene amifirstinvite12
    with dissolve

    a "Hahaha~ Maybe a teensy bit."
    a "But now you’re big and strong and can protect me if I ever get attacked by a rottweiler."
    s "You say some really strange things sometimes, you know?"

    scene amifirstinvite14
    stop music

    a "61 6c 62 61 74 72 6f 73 73"

    "///////////////////////////////////////////CONNECTION WEAK"
    "///////////////////////////////////////////PLEASE MAKE SURE ALL WIRES ARE PROPERLY CONNECTED"
    "///////////////////////////////////////////................................."
    "///////////////////////////////////////////ATTEMPTING TO RESTORE CONNECTION"
    "///////////////////////////////////////////................................."
    "///////////////////////////////////////////................................."
    "///////////////////////////////////////////TESTING CONNECTION"
    "///////////////////////////////////////////3"
    "///////////////////////////////////////////2"
    "///////////////////////////////////////////1"
    "///////////////////////////////////////////................................."
    "///////////////////////////////////////////CONNECTION RESTORED"

    scene amifirstinvite13
    play music "acoustic.mp3"

    a "I’m not the only one who says strange things, [amimaster]."
    a "Like, remember how you fell asleep in the classroom a few months ago and didn’t even know who I was when you woke up?"
    a "What was up with that?"
    a "It’s like you were a different person all of a sudden."

    "What Ami still doesn’t understand is that I {i}was{/i} a different person all of a sudden."
    "My life changed dramatically that day."
    "Just as hers did when her parents were turned into a roadside sculpture of steel and shattered bones."
    "Life changes for everyone."
    "Sometimes, you grow fat and pace around your room for months on end as a result."
    "You leave food out on your desk."
    "Flies find it and lay eggs."
    "The eggs hatch."

    if bonus == True:
        "Then, before long, maggots consume everything as your traumatized [niece] finds new ways to please herself on the opposite end of the house."
        "Anything to distract from the pain."
        "That is all life is and that is all we are."
    else:
        "But surprise! Chickens come out! There were never any fleas at all!"

    scene amifirstinvite15
    with dissolve

    a "Mm..."
    a "I’m feeling really tired now that I get to lay like this, [amimaster]."
    s "Really? It doesn’t seem like a very comfortable position."
    a "Any position is fine as long as you’re with me."
    a "I could probably sleep standing up as long as you’re in the same room."
    a "But, then again, I’m also kind of crazy for you, so that might just be a special thing only I would be able to do."
    a "Do I make you comfortable as well, [amimaster]?"
    s "Of course."
    a "Really?"

    if ami_virgin == True:
        if bonus == True:
            a "Then how come you won’t finger me?"
            a "Is it because we’re family?"
            a "Does that make it a problem for you?"
            a "I think it’s okay for family members to help each other out like that, [amimaster]."
            a "In fact, I don’t think there’s anyone else in the world who I’d rather have fuck me from dawn ‘til dusk."
            s "...Ami, I-"
        else:
            a "Then how come you won’t hug me?"
            a "Is it because we have a mature business relationship?"
            s "...Ami, I-"

        scene amifirstinvite16
        with dissolve

        a "Ahhh~ I’m feeling really tired all of a sudden."
        a "It’s okay if I sleep here, right?"
        a "Wake me up in a few hours if you want dessert or something."
        a "I picked up a cake on the way home today."
        a "Goodnight, [amimaster]~ "
        a "I love you~"

        scene black
        with dissolve2

        s "..."
        s "I love you too..."

        if bonus == True:
            "I’m not sure what that little outburst was about, but-"
            "Well, actually-"
            "Correction: I {i}am{/i} sure of what that little outburst was about."
            "But I’ve already decided that I won’t be pursuing a relationship like that with Ami."
            "And even if that’s what she wants, I can’t possibly bring myself to defile her that way."
            "So, it will probably be best for everyone if she continues to keep her feelings for me private."
            "There’s no way it would ever work out between us if others caught wind of anything more than how we’re {i}supposed{/i} to be..."
        else:
            "{i}As an accountant...{/i}"

        $ renpy.end_replay()
        $ amiinvite1 = True
        $ ami_love += 3
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "{i}You can now invite her over to her own house every night if you’d like!{/i}"

        if bonus == True:
            "{i}Normally, you’d also get the option to do all kinds of sexual stuff with her, but it appears you made a mistake somewhere, so that part won’t happen!{/i}"
            "{i}Imagine having morals in a place like this.{/i}"

        $ amiinvite2miss = True

        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

    else:
        a "That makes me really happy."
        a "The fact that the two of us can be ourselves together now..."
        a "It’s unlike anything I would have ever wished for."
        a "I’ll admit, even though it was super weird, my heart skipped a beat when you “invited me over” today."
        a "It was almost like being asked out on a date- just the date was to your room and all we did was talk."
        a "But I got to lay on my favorite bed in the whole wide world with my favorite man in the whole wide world."
        a "And there’s nothing else that I’d have rather done."
        a "Stay with me forever, [amimaster]."
        a "Stay with me forever and I’ll make you happier than anyone has ever made anyone in the history of the universe."

        scene black
        with dissolve2

        "Ami falls asleep several minutes later."
        "Her hand drops to the side and hangs just an inch or two off of the floor."
        "I think more about how she said that floor used to be, covered in trash from neglect, and I wonder what it must have been like for her and the old Sensei during those dark, hopeless times. "
        "I imagine it must have been hard."
        "And in imagining that-"
        "I wonder if it would ever be possible for me to feel that much all at once."

        $ renpy.end_replay()
        $ amiinvite1 = True
        $ ami_love += 3
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label amiinvite2:
    play sound "phonebeep.wav"

    "I tap on Ami’s name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    a "Helloooo~ What’s up, [amimaster]?"
    s "Hey. Do you have some free time tonight?"
    a "I always have free time for you. Is there something you had in mind?"
    s "Why don’t we just hang out in my room and see where that takes us?"

    if bonus == True:
        a "So you want to have sex?"
        s "I mean, I don’t {i}not{/i} want to have sex."
    else:
        a "I bet it's toward a hug."
        s "Hugs are even better than elephants."

    a "Saying it that way is confusing. You should be more honest about what you want."
    s "I’m hanging up now, Ami."

    if bonus == True:
        a "Okay! I’ll go take a bath and get myself ready!"
    else:
        a "You're so weird!"

    a "Love you, [amimaster]!"

    play sound "phonebeep.wav"

    s "..."

    "Well, she definitely wasn’t holding anything back just now."

    scene black
    with dissolve2
    stop music fadeout 10.0

    if bonus == True:
        jump amithighx
    else:
        s "But neither was I..."
        s "I am prepared to hug."

        "I go home and hug Ami a few times."

        $ renpy.end_replay()
        $ amiinvite2 = True
        $ ami_lust += 1
        stop music fadeout 8.0

        "{i}Ami’s lust has increased to [ami_lust]!{/i}"
        "{i}You can now invite her over on nights and choose to raise either your affection or hug her!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label amiinvite3:
    play sound "phonebeep.wav"

    "I tap on Ami’s name in my phone and wait for her to answer."
    "I’m not really feeling like doing anything exciting tonight and, not to say that Ami isn’t exciting or anything, but I kind of just want to hang out at home."
    "And considering that inviting anyone else over would likely result in more stress than relaxation, my [niece] is the first person that comes to mind for a quiet night in."

    play sound "phonebeep.wav"

    ay "Sensei! Did you know there is a heart next to your name in Ami’s phone?"

    "The chance for a quiet night dies immediately after being born."

    a "{i}Ayane! Give me my phone back!{/i}"
    ay "Whoops! Sorry, Sensei! Here’s Ami~"

    "A minor scuffle bleeds through the receiving end of the telephone and Ami eventually finds her correct place in the conversation."

    a "Hey. What’s up?"
    a "If you’re just calling to let me know that you’re going to be out late, that’s fine. Ayane is sleeping over anyway."
    s "I was actually going to see if you wanted to hang out with me tonight."
    a "Ayane! Something came up and you have to go home!"
    s "Ayane can stay. It’s fine."
    a "Is it really, though?"
    ay "{i}Hey! I heard that!{/i}"
    s "Just hang out there and I’ll come meet up with you guys."
    a "Wait! Sensei..."
    s "What? What’s wrong?"
    a "Um..."
    a "I was just wondering if..."
    a "Can you buy us ice cream on the way home?"
    s "..."
    s "Are you kidding?"
    a "I love you! Bye!"
    ay "{i}Me too! I love-{/i}"

    play sound "phonebeep.wav"

    "Ami hangs up the phone and my quiet night in has suddenly turned into one more rollercoaster in the amusement park that is life."

    scene black
    with dissolve
    stop music fadeout 5.0

    "I slide my phone into my pocket, replacing it with my wallet before checking how much cash I have on me."
    "And, before I know it, I find myself in the check out line of a convenience store with several pints of ice cream in my hands."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    play music "thesleepingcity.mp3"

    s "I’m home..."

    "I don’t know how I managed to go from “cool guy breezing his way through a brand new life” to “generic [uncle] buying ice cream for girls,” but here we are."

    if bonus == True:
        if ami_virgin == False:
            "Granted, I’m also having sex with both of these girls, so I guess I’m not entirely normal."
        else:
            "Granted, I’m also having sex with one of these girls, so I guess I’m not entirely normal."

    "Either way, I toss the bag directly into the freezer and make my way into the living room to find Ami and Ayane already in their pajamas."

    scene amiayanesleepover1
    with dissolve2

    a "Welcome home, Sensei!"
    ay "Where are our goodnight kisses?"
    s "Are you two already going to sleep?"
    ay "Will you kiss me if I say yes?"
    s "..."
    s "Any response to that, Ami? "

    if ami_virgin == False:
        a "Will you kiss {i}me{/i} if I say yes?"
    else:
        a "Yes. Even think about it and I will sew your mouth shut for the rest of eternity."

    s "I’m not kissing anyone."
    s "In fact, the only reason I came back at all was to unwind."
    a "And to spend time with your beloved [niece]."
    ay "And her best friend. Me."
    s "Yes. I’m here to spend time with both of you."
    s "I’m pretty sure the ice cream delivers that message pretty well in the event of my words somehow managing to fall flat."
    a "Thank you! I thought for sure you were gonna be like, “Bahhh ice cream is exhausting” and then just come home without any."

    scene amiayanesleepover2
    with dissolve

    a "Ayane’s been freakin’ out about ice cream all day so we were probably just gonna go get some ourselves if that happened."
    ay "Not {i}all day{/i}...Just for the last ten hours or so."
    a "Yeah. All day."
    s "How come it’s just you two tonight?"

    scene amiayanesleepover3
    with dissolve

    a "What do you mean?"
    ay "Are Ami and I not allowed to hang out alone anymore?"
    ay "Is it because you’ve seen us kiss?"

    if bonus == True:
        a "Please don’t bring up the kiss, Ayane."
        ay "Ami has very soft lips. They’re like two little lemon-flavored pillows."
    else:
        s "Ew, no."

    scene amiayanesleepover4
    with dissolve

    a "Can you cut it out, please?!"
    ay "I love you, Ami! Let's kiss again for Sensei! "

    if bonus == True:
        s "What I was getting at is that there’s normally a third girl with you. "
        s "The one with the hair and the...weight of the entire universe on her shoulders."
    else:
        s "Staaaaaaaaahhhhhhhp."

    scene amiayanesleepover5
    with dissolve

    a "Oh, Ayane and I just wanted it to be the two of us tonight. "
    a "It’s not like we didn’t {i}want{/i} Maya here or anything, but sometimes it’s good for it to just be us two so we can talk about old times and stuff."
    s "You’re [teenager]s. There are no “old times” for you."

    scene amiayanesleepover6
    with dissolve

    a "Maybe not {i}old{/i} times...but times the two of us spent together that no one else knows about."
    a "Isn’t it fun to have secrets like that with someone, Sensei?"
    s "I wouldn’t really know. "
    s "Besides, I’m sure that any “secret” I have would be found out by you two almost immediately."

    scene amiayanesleepover7
    with dissolve

    a "That’s right. So don’t even think about hiding stuff from the original Sensei Love Squad."
    ay "I wouldn’t say “immediately...” but yeah. We’d find out eventually."

    if sarabar20 == True:
        s "Oh, right. Didn’t you have something you wanted to talk to me about, Ayane?"

        scene amiayanesleepover8
        with dissolve

        ay "Oh! Uhh...yeah! Soon!"
        ay "Not right now, though! This isn’t really the best time..."
        a "What did you have to talk to Sensei about? You never said anything to me."
    else:
        ay "Oh, and...umm...Sensei?"
        s "Yes, Ayane?"
        ay "If it's okay with you...there's something I'd like to talk about with you soon."
        ay "Obviously not tonight, but...yeah."
        s "Sure. Can I ask what this is about?"

    scene amiayanesleepover9
    with dissolve

    ay "Just...some stuff..."
    a "About?"

    if bonus == True:
        ay "About..."
        ay "Boobs."
        a "..."
        ay "..."
        a "Please don’t talk to my [uncle] about boobs. Even if you are an honorary member of the original Sensei Love Squad."
        s "Okay, I didn’t want to ask the first time I heard it, but this is the second time it’s been mentioned within sixty seconds."
    else:
        ay "Necklaces made out of-"
        s "So, anyway-"

    s "What exactly is the “Sensei Love Squad?”"

    scene amiayanesleepover10
    with dissolve

    a "A two person organization me and Ayane formed to put all of the followers in their places!"
    ay "That’s right! "
    ay "Ami and I have spent years fighting for your affection and we will not stand for random pink haired girls walking into your life and trying to take you from us!"
    ay "Even if you’ve technically known those random pink haired girls longer than you’ve known me!"
    a "And even if those girls happen to be extremely nice!"
    ay "And pretty!"
    a "But with horrible taste in clothes!"
    ay "But still very pretty!"
    s "No one is going to {i}take{/i} me from anyone. I’m not property."

    scene amiayanesleepover11
    with dissolve

    ay "Not {i}yet{/i}..."
    a "Ayane..."

    scene amiayanesleepover12
    with dissolve

    ay "But really, though! I have no idea what her deal is!"
    ay "I’ve known Ami since elementary[school] and I’d never even heard of that Noriko girl until she walked into class."
    a "My memory from all the way back then isn’t really good...so I can’t really think of when I would have seen her either."
    s "She remembers you, though. And so does her sister."

    scene amiayanesleepover13
    with dissolve

    a "Niki remembers {i}me{/i}?!"
    s "Well, she remembers that you exist. I don’t know if you two ever met."
    ay "Isn’t it weird that I’ve never met her if you’ve known her for that long, though?"
    ay "I spent almost every night here once my mom left and...if you two really go back that far..."
    ay "I just don’t get it."
    s "It’s a confusing situation. I don’t really think I fully understand it yet either, to be completely honest."

    scene amiayanesleepover14
    with dissolve

    a "I remember when he used to tutor and stuff, and he definitely started doing it more around the time we became friends."
    a "What I'm confused about is how someone can just happen to {i}lose{/i} somebody they claim to care about for as long as she {i}lost{/i} Sensei."
    a "Wouldn’t that mean like, she doesn’t love him at all? It’s not like we’ve lived anywhere other than here and the old district."
    a "Do {i}you{/i} think you’d ever lose Sensei for that long? Because I know {i}I{/i} wouldn’t."
    ay "Well...circumstances are different for everyone, but..."

    scene amiayanesleepover16
    with dissolve

    ay "No."
    ay "I don’t think that would ever happen with me. I wouldn't let it."
    a "Exactly. Which is why I’ve decided that Noriko doesn’t love you at all and only I do."
    ay "And me."
    a "And Ayane by default, I guess. But she’s too needy and you’ll never pick her."

    scene amiayanesleepover15
    with dissolve

    ay "You’re being a lot meaner than normal about this today..."
    a "You think so? Cause it seems kinda like you’re just not fighting back as hard as you normally do."

    scene amiayanesleepover16
    with dissolve

    a "Either way, Noriko might be nice and related to one of my favorite pop stars, but that doesn’t mean that I think she’s at all deserving of your time, Sensei."
    a "I don’t know when you “disappeared” on her, but I know that you’ve been here for me for as long as I’ve needed you."
    a "So I am obviously your favorite and everything I say goes."
    s "Is that how this works?"
    a "Yup! I {i}worked{/i} for the love you give me. It’s not fair if you give the same amount to people just because they want it."
    ay "I don’t think “love” is something you should have to work for, but I do know I love you."

    scene amiayanesleepover17
    with dissolve

    a "Ayane! I-"
    ay "And you too, Ami."
    ay "I love both of you guys. You’re pretty much the only family I have now."

    scene amiayanesleepover18
    with dissolve

    ay "And sure, you might have a few extra years on me in time spent with him."
    ay "And sure, you might get to wake up in the same house as him every day while I have to wake up on the other side of town."

    scene amiayanesleepover19
    with dissolve

    if bonus == True:
        ay "And sure, he might get to see you walk around the house naked all the time and force you to cook him breakfast in nothing but an apron!"

        "Oh, that’s a good idea. I should do that."

        ay "But I am a better cook with nicer boobs and just as much, if not even more love to give!"
        ay "And sure, I-"
        a "Please don’t keep going. That’s more than enough, Ayane."
    else:
        ay "And sure, he might get to eat your french toast more often than he eats mine!"
        a "Ayane, stop. Nobody likes your french toast. You use low quality bread and not enough cinnamon."

    scene amiayanesleepover20
    with dissolve

    ay "Fine. But you have to tell me you love me too."

    if bonus == True:
        a "After you literally just made the one comparison that no growing girl should ever make to another one?"
        ay "Want me to massage them for you? I heard it helps them grow."

    scene amiayanesleepover21
    with dissolve

    a "I love you too, okay?! Just keep your hands off of me and my boyf-[uncle]!"
    ay "Boyf[uncle]?"
    a "You know what I mean!"
    ay "I don’t. Please explain, Ami."
    s "This love squad or whatever really knows what it wants, huh?"

    scene amiayanesleepover22
    with dissolve

    a "Of course. And no matter what it is you might think, there is no one that wants your approval more than the two of us."
    ay "We even formed a whole organization to prove it. The first board meeting is next Saturday."
    a "Some stuff has clearly happened with your past that you either can’t share with us or just...don’t want to-"
    ay "And we’re okay with that. Kind of."
    ay "It really depends on what kind of stuff happened and what you’re willing to do to make it up to us."
    a "But at the end of the day, you’re {i}my{/i} Sensei. "
    ay "{i}Our{/i} Sensei."
    a "I said what I said."
    ay "Fine. But then I get to be {i}his{/i} Ayane."
    s "..."
    a "..."
    ay "..."
    s "Why are you two just staring at me? I told you I’m not going anywhere and that all I wanted to do was relax tonight."
    s "I did not sign up for a longform discussion on who wants or deserves me the most."
    s "Also, your ice cream is getting cold. Go eat it."
    ay "That is literally the point of ice cream, Sensei. Are you so far removed from happy things that you can’t even remember that?"

    scene black
    with dissolve2

    "The short answer: Yes."
    "The slightly longer answer: Yes. But it’s a little more complicated than that."
    "It’s not that I am entirely devoid of joy or “far removed from happy things.”"
    "It’s that I’ve come to associate them with the subsequent misery that so standardly follows them soon after."
    "Without joy, there can be no sorrow. And without sorrow, there can be no joy."
    "It’s a multi-tool of a saying that coerces you into either thinking “Things will get better” or “Things will get worse.”"
    "But what help does a cycle like that do?"
    "The first of those two things makes sense and is likely why the damn idea was ever brought up in the first place."
    "But if you hold those lines of text up to a mirror, the opposite side of that mirror fills up with the concept of perpetual joy being nothing short of impossible."
    "And so there is no need to look forward to those happier moments in life-"
    "Because things can only get worse from that point on."
    "Think nothing, but feel everything."
    "Distract yourself with sensations when emotions will not do the trick anymore."
    "For there are several sensations in this world that are worth any amount of pain they cause in result."
    "Praise be."

    scene amiayanesleepover23
    with dissolve

    a "Oh good...You’re still awake."
    s "I’m happy to see the love squad continued bonding after I retired for the night."
    a "Ha ha ha."
    a "She just sort of passed out like this."
    a "Do you think you could go get my blanket for me? I don’t want to wake her."
    s "Aww, look at my [niece] being such a caring and adorable best friend."

    scene amiayanesleepover24
    with dissolve

    a "Yeah..."
    a "Ayane’s been pretty stressed out lately."
    a "You already know she’s not the type to talk about her feelings and I think it’s starting to catch up to her."
    s "Is she going to be okay?"
    a "Are you worried?"
    s "Of course. I’d worry about you the same way."
    a "She’ll be okay. "
    a "She just needs some rest."

    scene black
    with dissolve2

    "I grab Ami’s blanket out of her room and bring it to her moments later."
    "Not wanting to move, she asks me to drape it over her and tuck the two of them in, to which I oblige because, as I mentioned earlier, I’m now nothing more than a generic [uncle]."

    if bonus == True:
        if ami_virgin == False:
            "A generic [uncle] who routinely fucks both his [niece] and her best friend, and wants nothing more than their unending happiness."
            "Their unending happiness and the chance to screw them both at once eventually."
            "I go to sleep."
        else:
            "A generic [uncle] who routinely fucks his [niece]’s best friend and proceeds to smile and act like nothing ever happened while tucking the two of them in."
            "I love Ami. I really do."
            "But a part of me hopes that she dreams of what I do to Ayane when she falls asleep tonight."
            "I go back to my room and pass out to the idea of her waking up from that dream."

    $ renpy.end_replay()
    $ amiinvite3 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
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

label amimaid30:
    scene amimaidthirty1
    with fade
    play music "maidcafe.mp3"

    "I arrive at the maid cafe bright and early to see how Ami’s doing."

    a "Wow! You’re here bright and early!"

    "See?"

    scene amimaidthirty2
    with dissolve

    a "Did you wind up skipping the breakfast I made for you this morning or something?"
    s "You made me breakfast this morning?"
    a "Yeah, I wrapped it up and left it on the table for you. "
    a "I didn’t really have time to write a note or anything because I was running late for work, but I figured you’d have just...understood that it was there for you and not somebody else."
    s "Honestly, I didn’t even notice."

    scene amimaidthirty3
    with dissolve

    a "Oh well! I’ll just assume that since you’re here, it meant you missed me so much that you ran right over as soon as you woke up!"
    s "Yeah, let’s go with that. "
    s "Is Uta-chan working now?"

    scene amimaidthirty4
    with dissolve

    a "Or you only came here to toy with my feelings!"
    a "Am I not good enough for you all of a sudden? Why Uta-chan and not your beloved [niece]?"
    s "Because Uta-chan would never put on a face like that while she’s at work. "
    s "And here I was thinking you were finally beginning to get the hang of your new job..."

    scene amimaidthirty5
    with dissolve

    a "I {i}am{/i} getting the hang of my new job! I’m really good at this!"
    s "Great. Then you can start chipping in on bills soon. The one for our phones has been getting pretty high lately."

    "Though, there is a very good reason for that."

    scene amimaidthirty6
    with dissolve

    a "What? How? I thought we had unlimited data and all that stuff?"
    s "Long story. Point is, now that I know you have a stable job that you’re doing well at, it’s time to start growing up financially as well."

    scene amimaidthirty7
    with dissolve

    a "Ooooooooor you can keep paying all the bills and I can use the money I make at work to do all sorts of fun things with you."

    if ami_virgin == False and bonus == True:
        a "Or {i}to{/i} you, depending on the mood we’re in."
        s "I am both intrigued and scared at the same time now."
        s "I guess there’s no harm in letting you use your money how you please."
    else:
        s "...I guess that’s also a fine way to spend your money."

    s "I’m a little surprised you don’t want to spend it on yourself, though. Wasn’t that the whole reason you got a job in the first place?"

    if bonus == True:
        a "Kind of. It’s been an interesting change of pace and I’d be lying if I said I wouldn’t rather spend my time pleasing you and you only-"
    else:
        a "Kind of. But I've been dumping all of my earnings into non-profit organizations in an effort to make the world a better place."
        s "Awwwww."

    a "But being able to buy clothes is nice too. "

    scene amimaidthirty1
    with dissolve

    a "And so I was kinda wondering if you’d wanna maybe come to the mall with me soon and...help me pick out a new swimsuit for the next time we go to the beach."
    s "Ami, it’s the middle of winter."
    a "So what? Even if it’s freezing cold out when we go to the ocean, we’re still going to wind up swimming."
    a "What’s the point of having a vacation at the beach if you’re not going to go swimming?"

    if bonus == True:
        a "Plus, the swimsuit I have now is really...childish anyway."
        a "And if I’m gonna start doing grown-up stuff like working and living at the dorm, I’m gonna need to look the part."
        a "The days of the one piece are over, Sensei! The days of bikini Ami are about to begin!"
        s "Are you sure you’re going to be able to find one that...you know...{i}fits?{/i}"
        a "..."
        s "Because I think the one piece might actually be a better bet until you...grow in a little more."
        a "..."
    else:
        a "Sometimes, the sound of the ocean helps me stay focused while filing your returns."
        s "In that case, I support the trip. Thank you for explaining your position to me."

    scene amimaidthirty8
    with dissolve

    os "Hey, is there anything I can be doing to help out while there are no customers here? I feel weird just standing around."
    a "..."
    s "I’m a customer."

    scene amimaidthirty9
    with dissolve

    os "Please don’t look at me."
    os "Also, did you say something mean to Ami? She looks kinda...frozen."
    s "How am I supposed to talk to you if I’m not allowed to look at you?"
    os "Just look the other way or something, I don’t know."

    scene amimaidthirty10
    with dissolve

    a "Hah..."
    a "Even {i}those{/i} would be a gift from God right now."
    os "...?"
    s "Think, Osako."
    os "..."

    if bonus == True:
        scene amimaidthirty11
        with dissolve

        os "You didn't say what I think you did to her...did you?"
        a "You can just hang out, Osako-chan...I don’t really know what to do when it’s dead either."
        a "And no one ever really comes until the afternoon anyway..."

        scene amimaidthirty12
        with dissolve

        os "Okay...sounds good, I guess."
        os "And, uhh...hang in there? Mine didn’t start showing up until senior year of [high_school] and..."
        os "Why am I even telling you this? I’m just going to go...re-wash dishes or something."
    else:
        os "No clue."
        os "Anyway, bye. My appearance in this event is over now."

    scene amimaidthirty13
    with dissolve

    "Osako leaves the table and I suddenly have to figure out a way to make Ami feel better."
    "Thankfully, this is the easiest possible task that could ever fall into my lap."

    s "I love you and you’re adorable."

    scene amimaidthirty14
    with dissolve

    a "Ah! I love you too!"
    a "What were we just talking about? Did Osako-chan need help with something?"
    s "Nah, she’ll be fine."

    play sound "dishes.mp3"
    scene amimaidthirty14
    with hpunch

    os "Shit!"
    s "See?"
    a "Oh well. Uta drops stuff all the time so we can just add it to the list. Our manager is really forgiving about that kind of stuff."
    s "Well that’s reassuring. Having a manager that gets on your case all the time doesn’t sound like a thing I’d be able to handle."

    scene amimaidthirty15
    with dissolve

    a "You handle {i}me{/i} just fine, though. And I kinda feel like your manager sometimes, you know?"
    a "Sure, that bitch Makoto is the one always making sure you do your work and stuff-"
    s "You can’t just casually call her a-"
    a "But {i}I’m{/i} the one making sure you get up on time and make it to[school]."
    a "And I’m the one who gets to hold your hand and help you make all the correct decisions for things that actually matter."
    a "We’ve got a special bond that no one else could ever hope to replicate! So I’m not just a manager, I’m a...super manager!"
    s "I’m sure that will look great on future job applications."

    scene amimaidthirty16
    with dissolve

    a "Future applications?"
    s "Yeah. You can’t just stay at the maid cafe forever, right?"

    "I mean, it’s not like she can ever really get a “real” job at this rate, though. So I guess technically she can stay here forever."
    "But still, I should at least {i}try{/i} to push her in the right direction every once in a while."

    a "I wasn’t planning on staying here forever."
    s "Well then what’s your goal once you get out of [high_school]?"

    scene amimaidthirty17
    with dissolve

    a "To wait on your every beck and call."
    s "Why did I expect for even a moment that you were going to say something else?"

    if ami_virgin == False:
        a "I have no idea. I’ve done nothing but force myself on you from the get-go and that’s just a thing you’re going to have to deal with for the rest of forever."
    else:
        if bonus == True:
            a "I have no idea. I’ve done nothing but try to get you to notice me as more than a [niece] from the get-go and you still think you can avoid my love."
        else:
            a "I have no idea. Maybe I'll try expanding my accounting firm internationally? Of course, I'd remain local myself, though."

        s "Ami-"
        a "Don’t {i}Ami{/i} me, Mister. "
        a "I’ll be with you forever, even if you don’t want me there."

    scene amimaidthirty18
    with dissolve

    a "But right now, I’m Ami-chan! Third most popular maid in the entire cafe!"
    s "I’m assuming Uta is one of those two but...has Osako already overtaken you in the rankings?"
    a "Oh, no. I’m talking about someone completely different. But I’ve vowed to not speak of who number one is at the risk of losing my job."
    s "You can’t just say something that interesting and not follow up on it."
    a "Sure I can!"
    a "Besides, I don’t know if she’s ever coming back anyway, so we’ll just kinda have to wait and see I guess."
    s "..."
    s "Is it someone I know at least?"

    scene amimaidthirty19
    with dissolve

    a "Maybe! But do you really think I would tell you-"

    if amipatgasm == True:
        s "If you tell me, I’ll pat your head."

        scene amimaidthirty20
        with dissolve

        a "Wait, no! You can’t pat my head! We found out last time that weird things happen when you pat my head!"
        a "If you’re going to do that again, we need to at least go home or-"
        s "Are you sure? Because I’ll do it right here."
        a "Sensei!"
        a "If you really want to know, just...keep coming back!"

    else:
        s "If you tell me, I’ll pat your head."

        scene amimaidthirty21
        with dissolve

        a "Hmm...that does seem like a fair trade, but still. I can’t do it."
        a "You’ll just have to...keep coming back until you find out for yourself."

    s "Are you challenging me to come to the maid cafe every day for the rest of my life?"

    scene amimaidthirty22
    with dissolve

    a "Perhaps I am."
    a "And yes, I know that this means you might go broke. But that’s okay! "
    a "The two of us could move into some strange abandoned building and live out the rest of our days taking donations from strangers or waiting for government assistance!"
    s "Well I definitely don't need to know who the secret maid is {i}that{/i} much."

    scene amimaidthirty23
    with dissolve

    a "Of course you don’t, because I’m the only maid you’ll ever need anyway."
    a "I will admit that I was very jealous when I found out you wanted to marry Uta-chan-"
    s "Want. Not wanted. The desire is still there. "
    s "She will be mine."
    s "Oh, yes."
    s "She will be mine..."
    a "No. Because {i}I{/i} will be yours. "
    a "You haven’t spent as much time with me here as you have with her yet, but I’m like a walking trash receptacle for your love!"
    s "Please be a little kinder with the things you say about yourself. You are a reflection of me and-"
    s "Actually, yeah. That much is fine if you’re a reflection of me."
    a "...As I was saying! I spent years and years and years and years turning into Mega Ami so you wouldn’t look at people like Uta-chan."

    if bonus == True:
        a "And if I find out it’s just because of her stupid boobs I’m skipping out on a new bathing suit and saving up for implants!"
    else:
        a "But if Uta's vigorous treadmill routine has made her attractive enough for you to ackowledge her over your dear CPA, maybe I'll get a treadmill too?"

    s "Please don’t do that. I like you just the way you are."

    scene amimaidthirty18
    with dissolve

    a "Exactly!"

    if bonus == True:
        a "So, with that out of the way, come with me to the mall and appreciate my depressingly tiny chest as I try on new bathing suits for you!"
        s "No more one piece?"
        a "No more one piece."
        s "Well, I’ve seen you naked before, so that’s not too drastic of a change."
        a "Exactly! It’ll be just like me walking around the house in my underwear. Just if you get excited, everyone around you will notice and not just me!"
        s "I still think it’s insane you’re even considering doing something like this when it is literally snowing out."
        a "The snow can only last so long! And youth is not eternal!"
        a "Appreciate me while you can, Sensei. Because you never know when I’m gonna hit my growth spurt and become a sultry, sexy [niece] rather than a cute one."
        s "Doubtful. Right now, I think sultry and sexy are the two words I would literally never describe you with."

        scene amimaidthirty24
        with dissolve

        a "I can be sexy if I want to be! Just look at my costume!"
        s "Again, that’s more “cute” than it is sexy. "
        a "What do I have to wear to be sexy?!"

        scene amimaidthirty25
        with dissolve

        os "Ami, what are you freaking out about? Isn’t he your [uncle]?"
        os "Why do you have to look-"
        a "Shut up, Osako-chan! Tell him I’m sexy!"
        os "...No?"

        scene amimaidthirty24
        with dissolve

        a "Well...maybe I’m not sexy {i}yet!{/i} But you just wait!"
        a "You’ve got a long time left with me, Mister! And I’m not gonna be your little girl forever!"
        a "Well, I will always be your little girl! But I’ll eventually be a...big little girl! With boobs and...allure!"
        a "And you will love me!"
        os "...Okay, I’m gonna step outside for a bit."
        os "Let me know if you need help or anything..."

    scene black
    with dissolve2

    if bonus == True:
        "Instead of bringing me anything to eat, Ami spends the next twenty minutes lecturing me about things I should and should not say to her."
        "Of course, Ami’s entire thing is that she’ll accept me unconditionally no matter what I do, so it goes in one ear and out the other."
        "But hey, even when she’s incessantly ranting about her inferiority complex, she still manages to be cute about it."
        "Is she annoying? Sure. "
        "But she’s family."
        "And I don’t really have a problem saying that now."
        "It’s family’s job to be annoying, so I can’t really foresee that ever going away."
        "Granted, I can’t see her ever “growing up” either but, chances are, I won’t ever have to."
        "So I should just accept my [niece] in all of her current, non-sexy perpetual glory."
        "For she is but a trash receptacle-"
        "And I am a man walking down the streets of a busy neighborhood, clutching an empty can and waiting for a place to toss it out."
        "Also, even though I’ve seen her naked around the house before, I’m weirdly excited to see Ami try on new swimsuits."
        "But if she winds up getting a cold as a result of stripping down to that much bare skin in the middle of winter, I’m having her pay for her own medical bills."
    else:
        "The meeting is cut short when a group of electricians shows up to rewire some stuff."
        "They try telling me about it since I am a man and appear to be knowledgable about wires, but I really have no idea what they're talking about and just nod at them a bunch of times to try and hide that."
        "Eventually, I wind up paying for the necessary repairs because I am a good guy."
        "Everyone thanks me and tries to lift me in the air to celebrate, but I don't like how their hands feel, so I make them stop."

    $ renpy.end_replay()
    $ amimaid30 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label amidate35:
    play sound "phonebeep.wav"

    "I tap on Ami’s name in my phone and wait for her to answer."
    "I’ve yet to see her come home with a new bathing suit, so unless she’s been hiding it from me for some reason, I doubt she’s gone to the mall yet."
    "I’m also aware that roughly half of the reason she’s been abstaining is due to the fact that I have not yet invited her."
    "So, without really knowing what else to do with my day, I decide to take Ami on a little trip."
    "It’s amazing how easily you can get me to actually do things when I know I won’t have to pay for them."

    play sound "phonebeep.wav"

    a "Sensei! I was just thinking about you."
    s "What? No way. What a strange turn of events."
    a "Ha ha ha. That was so funny I forgot to laugh."
    s "But...you just-"
    a "So, what’s up? Are you just calling to hear my voice or are you looking for some Ami-time?"

    if bonus == True:
        s "Ami-time sounds exhausting. I was just going to see if you wanted to take off your clothes in a dressing room for me."
        a "In public?! But that’s-"
        a "Oh wait, is this about the swimsuit?"
        s "You bet."
        a "{i}Tch...{/i}"
        s "Was that frustration I just heard?"
        a "Nope! No frustration at all!"
        a "I’m actually on the bus headed home right now, but I can just get off at the mall instead if you want to meet there!"
        a "I’m really sorry we don’t get to travel together but-"
        s "Sure, I’ll see you there."
        a "Wait. I was about to say something really cute and-"
    else:
        s "Kind of. I want to do something nice for you to reward you for always going above and beyond when it comes to accounting, and I know you have wanted a new swimsuit as of late."
        s "Would you be able to find the time to accompany me to the mall today?"
        a "Of course! Thank you for finally acknowledging all of my hard work and-"

    play sound "phonebeep.wav"

    "I hang up the phone after I finish making plans with Ami and start heading over to the bus stop."

    scene black
    with dissolve

    "The bus schedule is pretty packed around this time of day, so I imagine I won’t have to wait long."
    "And since Ami’s already on one heading back from work, I doubt that the one I get on will just so happen to have her sitting there acting all surprised once I reach the top step."
    "Yeah. Nothing convenient like that would ever happen to someone like me."
    "........."
    "......"
    "..."

    scene mall2
    with dissolve
    play music "shiningstarinstrumental.mp3"

    "Huh. I thought for sure that narrating a line like that was an omen for things to come, but apparently not."

    if bonus == True:
        "I make it to the mall after a decently quick bus ride in which an older woman (So old that I didn’t even contemplate the idea of having sex with her as more than just a passing thought) fell asleep on my shoulder."
        "I didn’t bother waking her up, though, considering she will likely die in the next several years and needs all the rest she can get until then."
        "To sleep before the big sleep."
        "Oh, what a sleep that must be."

    if amimaster.lower() in ["sensei"]:
        a "About time you showed up, Sensei!"

        scene amimalltwo1
        with dissolve

    else:
        a "About time, [amimaster]!"

        scene amimalltwo1
        with dissolve

        s "What do you think you’re doing, calling me that in public?"
        a "What’s wrong? It’s not like anybody else is paying attention."
        a "And I like calling you that. It reminds me of how close we are."
        s "I mean, I don’t care. I just don’t want someone getting the wrong idea."
        a "Blah blah blah. Who cares what people think? We’re here to get our love all over each other and stuff. I’m gonna call you what I want to call you."
        s "Can you define exactly what you mean by “getting our love all over each other?”"
        a "Nope!"

    a "How was the bus ride over?"
    a "I thought for a second that you were going to mysteriously appear on the same bus as me after our call, but it just didn’t happen."
    s "Screw the bus, what happened to your hair?"

    scene amimalltwo2
    with dissolve

    a "Huh? What do you mean?"
    a "Are you talking about my bangs?"
    s "Yeah. Aren’t they normally straight? How did you get them to...not be straight anymore?"

    scene amimalltwo3
    with dissolve

    a "The same way Maya can eat more than her body weight in food and Ayane can materialize guns and giant bananas out of thin air."
    a "Cute girl magic!"
    s "Oh, okay."
    s "Well that explains everything."

    scene amimalltwo4
    with dissolve

    a "Yup! Cute girls are special creatures who normal laws and rules don’t apply to!"
    a "So you should never question things like that because it won’t make any difference whatsoever."
    s "Hey, if you want to have magical bangs, that’s your right. You can have whatever kind of bangs you want, Ami."

    scene amimalltwo5
    with dissolve

    a "So, anyway!"
    a "I wanted to check Le Vetefrenchwordstore where Chika works because they normally have a small selection of off-season stuff."
    a "But I don’t like the way Chika looks at you, so you can just wait in the corridor while I pop in and out really quick."
    s "I am not waiting outside while you talk to Chika."

    scene amimalltwo6
    with dissolve

    if bonus == True:
        a "But what if she tries to steal your penis like Sada Abe?!"
        s "Who?"

        scene amimalltwo7
        with dissolve

        mo "Weebnote...kind of!"
        mo "Sada Abe was a geisha and prostitute who lived from 1905 - 1971 and ultimately became famous for suffocating her lover to death!"
        mo "Well, the suffocating part wasn’t what made her famous. But what came after did!"
        mo "You see, Sada Abe took it upon herself to sever the penis of the man she loved more than anything else in the world and then carried it around for weeks afterward!"
        mo "Not all good things last forever, though. Abe was eventually sentenced and spent five years in prison."
        mo "If someone did something like that today, they’d likely spend much longer in jail. So don’t go cutting any penises off, kids!"

        scene amimalltwo8
        with dissolve

        "Molly proceeds to walk away from us without saying another word and disappears into some video game store."

        a "Well, that was weird."
        s "Yes, but I feel like we learned a valuable lesson."

        scene amimalltwo9
        with dissolve

        a "Did you really need an Irish girl to show up and tell you that cutting off penises is wrong?"
        s "Not that. The lesson we learned is cute girl magic is real and can also cause people to show up exactly when they’re needed."
        a "But...then the buses-"
        s "Never mind that, Ami. Let’s just start heading over to Le Vetefrenchwordstore and get your clothes off."

        scene amimalltwo10
        with dissolve

        a "Yeah! Stripping in a public dressing room with my [uncle]!"
        s "Please don’t yell things like that..."
    else:
        a "Okay, fine! But don't come crawling back to me when I find a {i}new{/i} client and I'm not willing to do your taxes anymore!"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene amimalltwo11
    with dissolve

    c "Ah! Sensei! I had no idea you were going to show up today!"
    s "Hey, Chika. It is for my safety and yours that I think you should only minimally acknowledge my existence today."
    c "Understood!"

    scene amimalltwo12
    with dissolve

    c "Hey, Ami! Out on a date with your [uncle] today?"
    s "It’s not a-"
    a "Yes. We are on a date. That is what is happening."
    c "Fun! Making him buy you something nice?"

    scene amimalltwo13
    with dissolve

    a "Actually...I was kind of hoping you still had some stuff from summer in stock."

    if bonus == True:
        s "She’s also using her own money. I would never force my [niece] to wear a swimsuit in the winter just for the fun of it."

        scene amimalltwo14
        with dissolve

        a "Why would you say something that suspicious when that isn’t even close to what’s actually happening?"
        c "Yeah, that just makes me think that’s a thing you {i}would{/i} do, Sensei."
        s "You know, I’m really not sure why I said that."
        s "Please continue minimally acknowledging my existence."
        c "...Okay."

    scene amimalltwo15
    with dissolve

    if bonus == True:
        c "Anyway, yeah. We’ve still got some summer stuff. It’s all on clearance right now too since no one’s buying swimsuits."
    else:
        c "Yeah. We’ve still got some summer stuff. It’s all on clearance right now too since no one’s buying swimsuits."

    c "So as long as you think you’ll be able to maintain your figure or...size until beach season rolls back around, buying one now is totally fine."

    if bonus == True:
        a "Oh, the last thing I’m worried about is growing out of it. That won’t be happening."

        "So much for holding out hope on becoming “sultry and sexy...”"
    else:
        a "I am fully grown and have a fast metabolism. This will allow me to remain the same exact size indefinitely."

    c "Cool! Then yeah, come to the back with me and I’ll show you where everything is."
    a "Great!"
    a "Oh, would you mind if Sensei came into the dressing room with me, though?"

    scene amimalltwo16
    with dissolve

    c "Uhh..."

    if bonus == True:
        s "Ami, why? Why would you say this?"
        a "What’s wrong, Sensei? We’re family. You’ve seen me in my underwear tons of times."
        a "Don’t tell me you’ve been looking at me strangely, have you?"

        "This fucking demon."

        c "I mean...there have definitely been dads who have helped their kid daughters in the dressing room before but..."

        scene amimalltwo17
        with dissolve

        a "Oh...I understand..."
        a "Sensei’s raised me since I was a little girl, but...since he isn’t technically related to me that way..."

        "{i}This fucking demon...{/i}"

        c "Wait, no! I didn’t mean it like that! It’s totally fine if that’s...what you need!"
        c "But it’s...kind of...definitely a little weird since he’s an adult and...you’re a [teenage]girl..."

        scene amimalltwo18
        with dissolve

        a "Yay! Thank you, Chika!"
        c "Uhh...yeah..."
        c "Just...probably don’t say anything about this to anybody else."

        scene black
        with dissolve

        "Chika leads Ami to the back of the store and directs her to a bin full of items that no one picked up during summer."
        "I’m sure they would have had a chance to sell if the seasons didn’t abruptly change, but that’s beside the point."
        "Ami grabs a few swimsuits, holding them up to her tiny body and closely judging whether or not she will embarrass herself by attempting to put them on."
        "Suffice it to say, most of the swimsuits wind up right back in the bin."
        "But, eventually, she finds a few she likes and heads into the dressing room."
        "I don’t follow right away because, even though Chika gave us permission, it still feels fucking weird."
        "But the second Chika is distracted by another customer, I seize the opportunity to join Ami and see what she looks like in a “less childish” bathing suit..."

        scene amimalltwo19
        with dissolve

        a "Finally..."

        "The answer: Still pretty childish."

        s "Yes, sorry for not being brazen enough to do the thing that one of your classmates said right to our faces is weird and socially unacceptable."
        a "Why do you always care so much about what is “socially acceptable?”"
        s "Ami, I am one of the last people who should ever be aligned with social acceptance."
        s "But when you’re an adult male in my position, you need to be a little careful when it comes to certain things."
        a "Like following your [niece] into a dressing room?"
        s "Like following my [niece] into a dressing room."
        s "You look really cute, though."

        scene amimalltwo20
        with dissolve

        a "Really?! I don’t look like I’m trying too hard?!"

        "I will never get over how convenient it is to just dodge difficult conversations by telling Ami she is cute."
        "If I had a dollar for every time I’ve taken advantage of that, I could probably buy her every single swimsuit in her cart right now."
        "Also, it definitely helps that I’m not even lying in telling her that."

        if ami_virgin == False:
            "In fact, if Chika wasn’t working right now, I’d probably even toy with the idea of taking things a little further with Ami for a few minutes."
            "Obviously, I’m not going to do that, though."
            "Because not only would that be socially unacceptable, I’m pretty sure having sex in the mall is entirely illegal."
            "And I refuse to live the rest of my alternate but also potentially not alternate (?) life in jail."
        else:
            "Sure, I {i}try{/i} not to view Ami in a sexual light because of...reasons. But it’s absolutely undeniable that she appeals to me in a multitude of ways."
            "There are just certain things you should always be able to say no to, though."
            "I just wish those things weren’t so hard all of the time."

        scene amimalltwo21
        with dissolve

        a "Um...I’ll probably just wind up buying this one, then..."
        s "Did you even try the other ones on yet?"
        a "Yeah. I tried a few of the other ones while you were waiting outside, but this is the one I thought looked the best."
        a "And having you call me cute is...kind of all the validation I need anyway."
        s "I mean, I always think you’re cute, so my word should probably be taken with a grain of salt."

        scene amimalltwo22
        with dissolve

        a "And...And the ponytail? Is that good too?"
        a "My hair goes all over the place in the water and having it bundled up in one tail instead of two might not {i}look{/i} as good, but-"
        s "It looks great."

        scene amimalltwo23
        with dissolve

        a "Okay...then yeah...I’m gonna get this one..."
        s "What’s with you acting all bashful all of a sudden?"
        s "Like five minutes ago, you were manipulating Chika into just letting me in here."
        s "What’s going on?"

        if ami_virgin == True:
            scene amimalltwo24
            with dissolve

            a "Just...feeling a little strange now that you’re in here is all."
            a "Trying to make sure I don’t say or do anything that might get us in trouble."
            s "..."
            a "..."
            s "You know, there was a thing out there I kind of wanted to check out."
            a "That’s fine...I’ll...start putting my normal clothes back on now and we can head out..."

        else:
            scene amimalltwo25
            with dissolve

            a "I wasn’t horny five minutes ago..."
            s "Why are you always getting horny in inconvenient locations?"
            a "Why are you always making me horny in inconvenient locations?"
            s "I have done literally nothing. You need to learn self-control."
            a "{i}I{/i} need to learn self-control? You have sex with your [niece]."
            a "Not that I think that's a problem or anything, obviously."
            s "Okay, we could {i}both{/i} do with learning a little self control. But you are the culprit here and I am an innocent man trying to not sully the workplace of one of your peers."
            a "We can’t even sully it a little bit?"
            s "No, Ami."
            a "Not even hand stuff?"

            scene black
            with dissolve

            a "Wait, Sensei!"
            s "If I stay in there any longer, there will be no turning back."
            a "I don’t wanna turn back! I want you!"

        "I step into the front room again and wait for Ami to finish changing back into her normal clothes."
        "Chika is still stuck tending to the same customer as before, so I don’t have to awkwardly talk about “how things were in there” or whatever it was that she was definitely going to ask me."
        "Ami returns a few minutes later with her new swimsuit in her hands and ultimately winds up getting rung up by one of the other employees."
        "Neither of us say goodbye to Chika, but it’s not like we really had a chance to anyway."
    else:
        s "I would mind. That is not something I have any interest in doing. I just wanted to reward you and make sure you are adequately dressed for the beach."
        a "Oh, I apologize for misunderstanding. Please wait out here, if that is the case."
        s "I will do just that."

        scene black
        with dissolve

    if ami_virgin == True:
        scene black
        with dissolve2

        "Eventually, we board the bus and start heading home."
        "Ami brings up the prospect of the two of us going out to eat or something along those lines, but I refuse as there is something else I want to do with my day instead."
        "Thankfully, we manage to get back into town shortly before nightfall and the two of us wind up amicably parting ways."
        "It wasn’t the most exciting or action packed of days I’ve spent with Ami, but it was still a fun one regardless."
        "Plus, she even got a new swimsuit out of it."

        if bonus == True:
            "And I’m excited for not only that, but the prospect of everyone else who decides to buy swimsuits prior to our next trip to the beach...whenever that may be."

        $ renpy.end_replay()
        $ ami_love += 1
        $ amidate35 = True
        $ amidorm40miss = True
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        jump saturdaynight


    else:
        "Eventually, we board a bus and start heading home, but Ami decides that the day is not yet complete and that she wants to go out to eat with me."
        "I refuse at first but completely cave once she informs me that she’ll be paying for this as well."
        "Listening to her happily hum the tune to one of Niki’s songs as it plays on the radio, I close my eyes and wait for whatever stop we're supposed to get off at to approach."
        "........."
        "......"
        "..."

        scene amimalltwo26
        with dissolve

        s "You know, you should probably eat more than just french fries, Ami."
        a "But I love french fries."
        a "And I bought them with my own money, so it’s not like you can even say something like “Bahhh you’ll eat right under my roof!”"
        a "Also, this isn’t even your roof. Back off of my french fries."
        s "I was...unaware that you felt so strongly about them."

        scene amimalltwo27
        with dissolve

        a "Did you have fun today, Sensei?"
        a "I know it wasn’t like an {i}actual{/i} date since we’re always spending time together and stuff...but I really like getting to do things like this with you."

        if bonus == True:
            a "You know...being out in public. Trying on clothes for you. Eating stuff together."
            a "It’s kind of like we’re in a real relationship. Or at least what I imagine a real relationship feels like."
            s "I guess it does kind of feel like a relationship when you put it that way."
        else:
            s "It made me feel like a little boy again."

        scene amimalltwo28
        with dissolve

        a "Right?! And wasn’t it lots of fun?!"
        s "Sure. It was a lot of fun. I won’t deny that."

        scene amimalltwo29
        with dissolve

        if bonus == True:
            a "Then make it official and start dating me for real."
            s "..."
            a "...?"
            s "You know I can’t do that."
            a "Why not?"
            s "Do you really need to ask? There are hundreds of reasons."
            a "And there are hundreds of reasons you {i}should{/i} do it."
            a "If you’re worried about everyone thinking it’s weird because we’re related, I don’t think you have to."
            a "Sure, people will probably think it’s weird {i}at first,{/i} but once they see how happy we are, I’m sure they’ll be fine with it."
            s "You think just seeing two people happy together is enough to support them?"
            a "Sure? Why not."
            s "So if I started dating someone else and looked happy with them, you’d support it?"

            scene amimalltwo30
            with dissolve

            a "Nope!"
            s "See what I mean?"
            a "Nope! Cause I also know you can’t be happy with anyone else."
            a "You and me are gonna be together forever cause that’s how things are meant to be."
            a "And we’re gonna buy tons more bathing suits and eat tons more french fries because we both think those things are fun and we love each other very, very much."

            scene amimalltwo31
            with dissolve

            a "And if anyone ever tries to ruin that, I will do horrible things to them."
            s "You do realize that if “anyone tries to ruin that” it will be me, right?"
            a "You want to ruin me? Your adorable [niece]? Who cooks you breakfast every morning and lets you cum on her face?"
            s "I don’t know what I want. But I know that a relationship isn’t anywhere near the top of the list."
            a "But it will be one day, right?"
            s "I have no idea."
            a "It will be one day."
            s "Ami-"
            a "It will be one day."
            s "..."
            a "..."
        else:
            a "Did you just tell me I looked fat?"
            s "What? No?"
            a "Is it because of the french fries?"
            s "You can eat as many french fries as you want. You deserve them."
            a "I'm watching you, Sensei."
            a "{i}I'm watching you.{/i}"

        "I want to say something like “the restaurant goes quiet and an uncomfortable silence finds its way between us,” but Niki is on the radio in here as well."
        "It’s like her voice has been following me all fucking day."
        "Like it’s just seeping into my ears and criticizing me for going on a date with my [niece] and not pushing her away the same way I would with anyone else."
        "For not telling her that “It {i}won’t{/i} be one day.”"
        "And for being afraid to steal away her smile just because I know why it looks the way it does- held together by Scotch tape and glue."

        a "Do you want a french fry? They’re extra salty today."
        s "French fries only exist when they’re extra salty. Any other time they’re just-"
        a "Rectangular potato strings. I know. Do you want one or not?"
        s "..."
        s "Fine."

        scene black
        with dissolve

        "I take the fry from Ami."
        "And then ten more."
        "And then an entire order because apparently she knew I was going to do this."

        if bonus == True:
            "I might not want a relationship with her-"
            "But my god, would it be easy to have one."

        $ renpy.end_replay()
        $ ami_love += 1
        $ amidate35 = True
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label amilust15:
    "{i}At my side the Demon writhes forever,{/i}"
    "{i}Swimming around me like impalpable air;{/i}"
    "{i}As I breathe, he burns my lungs like fever{/i}"
    "{i}And fills me with an eternal guilty desire.{/i}"
    "We’re all impulsive, orgasm loving, God fearing creatures moving from one area to the next in search of anything to make us feel like air."
    "But all we feel is fire."
    "And yet...even then, we rarely ever ignite as human flesh tends to peel and blister before giving us the chance to run around and turn our legacies into light shows."
    "We flail mindlessly instead."
    "Waiting."
    "Then time goes by, and our skin survives long enough to crack and leak out rendered fat."
    "And we become light."
    "As light as air?"
    "That’s hard to say."
    "But we become something. "
    "And something is more than nothing."

    if bonus == True:
        jump amilust15x
    else:
        "That's it. This entire event was a poem."
        "Nothing else happens, but I do go and give Ami a hug once I get up."

        $ renpy.end_replay()
        $ amilust15 = True
        $ ami_lust += 2

        "{i}Ami’s lust has increased to [ami_lust]!{/i}"
        "........."
        "......"
        "..."

        jump afterschoolevent

label amidate50:
    $ totaldays += 1
    $ day = 7

    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
    else:
        "ERROR ADVANCING TO SUNDAY"

    play music "beginningoftheend.mp3"

    "To see a World in a Grain of Sand\nAnd a Heaven in a Wild Flower"
    "Hold Infinity in the palm of your hand\nAnd Eternity in an hour"
    "A Robin Red breast in a Cage\nPuts all Heaven in a Rage"
    "A Dove house filld with Doves & Pigeons\nShudders Hell thr' all its regions "
    "A dog starvd at his Masters Gate\nPredicts the ruin of the State "
    "A Horse misusd upon the Road\nCalls to Heaven for Human blood"
    "Each outcry of the hunted Hare\nA fibre from the Brain does tear "
    "I wind up being swallowed by the bed sometime in the middle of the night."
    "My skin fuses to the fabric of the sheets and I need to peel it off each time I roll over to get a dose of colder air."
    "I hear the door open at several points but never have the resolve to open my eyes and see who it is."
    "Nor do I {i}need{/i} to because it could only be one person."
    "I hear it close just as often as I hear it open- but I guess it wouldn’t really be possible to hear one without the other now that I think about it."
    "I clutch the sheets and focus on the threads of fabric, fraying from being constantly used and abused over the years."
    "I wonder if these too are wiped clean each time I come down from the rooftop under a starlit sky."
    "And, if not, perhaps it’s time for new ones."
    "I poke a hole in them with my index finger and proceed to sink the tip of it into the mattress."
    "It’s soft."
    "Not like the flesh of a [young]girl, but like a mattress."
    "The door opens again. It is the same girl."
    "This time, she makes it to the foot of the bed and crouches down to whisper something into my ear."

    q "{i}I can’t sleep.{/i}"

    "The words register, but mean close to nothing as I’m unable to react or respond."
    "In fact, these thoughts likely aren’t even my own."
    "I am asleep."
    "I’ve been swallowed."
    "And there is nothing left for me here. "
    "The rest of the night or the day disappears."
    "I can’t tell which it was or is."

    scene her1
    with dissolve4

    s "..."
    te "..."
    te "Good morning."
    s "..."
    te "What? Aren’t you glad to see me?"
    s "..."

    "I am asleep."
    "I’ve been swallowed."
    "And there is nothing left for me anywhere."

    te "You’re late, you know."
    te "And look at you- sleeping in on the lord’s day. You need to wake up or God will cut your hands off and feed them to his angels. It’s true because I said so."
    s "..."
    te "Room for one more in there? If you’re so insistent on going to Hell, I may as well come with you. "
    s "..."
    te "..."
    te "Fine."
    te "But, you know..."
    te "Sooner or later, you’re going to have to come out of there."

    play sound "static.mp3"
    scene her2 with flash
    stop sound

    a "..."
    s "..."

    "I awaken regurgitated, covered in acids and fluids I carried with me out of some sort of celestial esophagus. "
    "And before me stands one of the only things that I have come to terms with loving."

    a "..."
    s "..."
    s "Is that-"
    a "Yeah."
    s "..."
    a "Does it...look okay?"
    s "..."

    "I remember that dress."
    "I-"

    play sound "static.mp3"
    scene her3 with flash
    stop sound

    a "Sensei?..."
    a "Should I...have not worn this?..."
    a "I know I said I’d never touch any of the things we locked away, but..."
    s "Good morning, Ami."
    a "..."
    s "..."

    scene her4
    with dissolve2

    a "Good morning, Sensei..."
    s "..."
    a "I had a bad dream."
    s "..."
    a "..."
    s "You can tell me about it on the way there."

    scene black
    with dissolve2

    "Ami nods through a half-broken smile and the sound of suppressed delight crosses her teeth as if it’s a point of no return."
    "In some ways, I think it might be."
    "But just like the morning’s first moments of joy, I suppress them enough to crawl out of bed and hug my [niece]."
    "She cries into my shoulder without saying a word."
    "She grows stronger by the day."
    "I fade into the background."

    scene sky
    with dissolve2

    "The two of us make our way to the bus stop and Ami talks a bit about how she spent the majority of last night filtering through boxes in the attic that once belonged to her mother."
    "She tells me about how much she’s been missing her lately and how the recent increase of exposure to the sun has reminded her of her youth."
    "She says this as if her youth has already vanished."
    "In a sense, I can see why she would think that."
    "The world was stripped away from her, leaving nothing but a melancholic deadbeat to care for her when he can’t even properly care for himself."
    "Only now, in this second shot at life, are the traces of her youth resurfacing- and even those are plagued by an unending misery in which she’ll never be able to truly overcome them for she can never grow old."
    "We’re all trapped in cages resembling personal hells, and I often forget how cramped hers is sometimes."
    "It wouldn’t have to be that way if she’d only stop leaving so much room for me."
    "We get on the bus and sit near the back. No one else rides with us."
    "The sun sneaks higher than the trees and the clouds and blinds me to the point where I need to give up a hand just to block its rays for the duration of the trip."
    "It makes it harder to pay attention to Ami’s recollection of her nightmare, but I do what I can because I know how hard it must be for her to tell me about it."
    "It goes something like this:"
    "She got to dance with her mom."

    scene her5
    with dissolve2

    "O world-"
    "Where have you gone?"

    a "..."
    s "..."

    "Ami stands before the resting place of her parents in complete silence, trying to find the words to summarize all of the anguish she’s felt without them."
    "I’m sure she’ll counteract it with tinges of good things, but are there truly enough of them to offset the underlying misery in what it means to be eternally alone?"
    "Are those fleeting moments of joy joyous enough to quell even a fraction of the pain she must have felt tying a sash around her mother’s dress?"
    "What about the feelings that spilled from whatever mirror she glanced into to make sure it fit right?"
    "What sort of things will she say to quiet the rumbling beneath us?"
    "And what should I say to her when they all fall flat?"

    a "..."
    s "..."

    "Ten more minutes of silence."
    "Then words."

    a "You looked better in this than I do."
    a "I don’t think I’ll ever be as tall as you, so I made a few adjustments to keep it from dragging."
    a "You always got upset with me when I got my dresses dirty...so I didn’t want to disappoint you...because I know you’re always watching."
    a "I wonder if you’d still seem as tall if I got to stand next to you today?"
    a "When I was little, it kind of felt like you were the biggest thing of all."
    a "But with a name like yours, I guess that was kind of bound to happen, huh?"
    a "Um..."
    a "So...let’s see..."
    a "Oh! We had another Christmas party recently."
    a "There was a little bit of drama, but I think most of us had fun overall."
    a "I sang in front of everyone, too! And, just so you know, I’m a lot better now than I used to be when we would sing together."
    a "You had such a beautiful voice."
    a "I still get that old song you’d sing to me in bed stuck in my head every now and then."
    a "Daisy...Daisy...Give me your answer do...and look! My hairpin even has one in it! Nice touch, right?"
    a "..."
    a "I miss you, Mom."
    a "More than anything in the world."
    a "Sensei misses you too, but he’s too afraid of looking weak around me to admit it."

    play sound "static.mp3"
    scene her6
    with flash
    stop sound

    a "Um...I’m doing okay in school, I think..."
    a "It’s kind of hard to tell with how Sensei grades stuff. When there...{i}is{/i} stuff to grade. Which...isn’t very often."
    a "And...um...the manga club is going well. We’re all reading this one series I think that you’d like a lot."
    a "The plants from our old house are still alive somehow. I’ve been taking good care of them since you’ve been gone and they’ve lasted way longer than I ever thought they would."
    a "Um...I’m a maid now. But not like a real maid. I just work at a cafe. I’d show you the dress if I could."

    scene her7
    with dissolve

    a "I still eat right before bed sometimes, which is a thing I probably shouldn’t be telling you since you’ll get mad at me- but I kind of promised I’d tell you everything, so..."
    a "I...uhh..."
    a "I miss you? Which I think I’ve said already but I really miss you so I’m just going to say it again."
    a "Daddy, too. Can you tell him that? Sensei’s been doing an okay job as my new dad, but he doesn’t pay enough attention to me sometimes and...uhh..."
    a "Did I...mention I...really miss you, Mom?..."

    play sound "static.mp3"
    scene her8
    with flash
    stop sound

    se "I miss you too, my sweet girl."
    se "There’s not a single day that goes by where I don’t think of you."
    se "I’m sorry I can’t be there to watch you grow."
    se "I’m sorry I can’t be there to help you fix up my old dresses- which you look beautiful in, by the way. Much better than I ever did."
    se "But most of all-"
    se "I’m sorry you feel so alone."
    se "I do too."
    a "..."
    se "I’m always here, though."
    se "Even if you can’t see me."
    se "Even if you can’t feel me."
    se "I can still feel you, Ami."
    se "You’re as warm as ever."
    a "Do you think she’s here, Sensei?"
    s "..."
    se "..."
    a "Do you...think she’s listening?"
    a "I hope I look okay...I really wanted to be pretty for her today."
    s "You are..."
    s "I’m sure she’d be proud."
    a "..."
    se "Can you look at me, Ami?"
    a "..."
    s "..."
    se "..."
    se "I didn’t think so."
    se "I have to go now. I have things to do."
    se "But take care of yourself, okay?"
    se "And your uncle too. He’s helpless on his own."
    se "I love you, Ami."
    a "I love you, Mom."

    play sound "static.mp3"
    scene her9
    with flash
    stop sound

    a "..."
    s "..."
    a "She was here..."
    a "I know she was..."

    scene black
    with dissolve2

    "A gust of wind tears thousands of cherry blossoms away from their home and off to someplace new."
    "My eyes follow them because there’s somewhere else they’d rather not look."
    "Ami falls to her knees and begins to sob uncontrollably."
    "It was only a matter of time."
    "But, all things considered, she’s been a lot more composed this time around than the last."
    "I won’t pretend to know why or even search my mind for clues, for I know the second I find any that they’ll pour out from my mouth even faster than the tears in Ami’s eyes."
    "This is a moment for her and her only."
    "I can not allow my constant need to involve myself in every facet of everyone’s lives to get in the way of that."
    "She must cry."
    "She must cry until her eyes swell shut."
    "And then she must get off the ground-"
    "Wipe the dirt from her mother’s dress-"
    "And smile."

    scene her10
    with dissolve2

    a "Okay...now it’s your turn."
    s "My turn?"
    a "They were important to you too, Sensei. You can’t just {i}not{/i} speak to them."
    s "Ami, I don’t really want to ruin a good moment by expressing my thoughts on talking to the deceased."
    a "I bet {i}they{/i} would talk to you if you were the one who died. I know I would."
    a "You’re not allowed to die, though. I love you too much."
    s "I will do my best to continue...indefinitely living."
    a "Um...can I ask for something selfish?"
    s "I already told you that I’m not giving you an allowance anymore. Stop trying to revive that when you already have a job."

    scene her11
    with dissolve

    a "The only reason I have a job is because you think all of the things I do for you aren’t worth new clothes and manga and stuff."
    s "And I will remain steadfast in that belief, but please carry on with your selfish request, whatever that may be."

    scene her12
    with dissolve

    a "I don’t want to go home just yet."
    a "I want you to spend the entire day with me."
    a "I want it to be a real date."

    if amifingered == True:
        s "A real date sounds fine. Especially since I very likely know how it will end with you."

        scene her13
        with dissolve

        a "Sensei! My parents are literally right there! You can’t say that!"
        s "Say what? It’s not like I said {i}how{/i} it will end. I just-"
        a "They were adults when they died! They will obviously know what you mean by that!"
        s "Again, I technically didn’t do anything wrong just now."

    else:
        s "What do you mean by a “real” date, Ami? Because I’ve already told you that-"

        scene her10
        with dissolve

        a "I know what you’ve told me. And I’m not expecting you to change that or do anything you think is weird that {i}really isn’t that weird{/i}, but I understand."
        a "Even if nothing comes of it, I want to go on a date."
        a "I want to spend the entire day with the person I love more than anything else in the world."
        a "I deserve it every once in a while if you’re really not going to give me an allowance."
        s "..."
        a "..."
        s "You know you’re really annoying sometimes, right?"
        a "I’m supposed to be annoying. I’m your [niece]."
        s "I don’t really think it works that way..."

    s "But fine. I’ll go on a date with you."

    scene her14
    with dissolve

    a "Yay! A whole day with Sensei that I only kind of had to force out of him!"
    s "Here’s hoping the next part of it is significantly less painful and tear-filled than the first."

    scene her10
    with dissolve

    a "Oh, it will be. I already know where we’re going. And it’s somewhere I think you’ll like a lot."
    s "That is a bold claim. There are not many things I like."
    a "Well, you just wait, Sensei. Because this place is going to knock your socks off."
    a "I just..."
    a "I just wanna talk to my mom one more time before we leave, okay?"
    s "..."

    scene black
    with dissolve2
    stop music fadeout 25.0

    s "Obviously. Even I wouldn't say no to that."
    a "Heheh~ You know you can talk too if-"
    s "I’ll be waiting at the entrance. Take your time."
    a "Sensei! At least stay here if you’re not going to talk to them!"

    "Ami lowers herself to her knees and places both hands upon her parents’ grave."
    "There are no gusts of wind or homeless cherry blossoms to distract me from the sight this time."
    "I watch her break down once again, knowing full well that it will likely not prepare me for the many more times I’ll have to watch her do this exact thing."
    "Some things, you can never get used to."
    "And the pain of someone you genuinely love is one of them."
    "I press my hands together and attempt to pray {i}for{/i} something {i}to{/i} happen."
    "Nothing happens."
    "Not even a gust of wind."

    $ renpy.end_replay()
    $ ami_love += 3
    $ amidate50 = True

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump amidate50p2

label amidate50p2:
    scene sky
    with dissolve2
    play music "amiamiami.mp3"

    s "Ami, where are you taking me?"
    a "I told you the first ten times you asked! Somewhere you’re going to like! The answer hasn’t changed!"
    s "I just can’t help but feel like you are lying to me considering every single building I can see from here sells nothing but anime and nerd stuff."
    a "Okay, first off, Sensei...anime isn’t just for nerds and I know you’re better than thinking that."
    s "Am I really, though?"
    a "We used to watch Sailor Moon all the time when I was little!"
    s "So obviously I would still love it years later."
    a "Exactly."
    s "That was sarcasm."
    a "Your face is sarcasm. Now stop asking where we’re going and let me lead the way!"

    "Ami pulls me through the streets of the red-ish light entertainment district after a mildly long bus ride back from the cemetery."
    "Is this where I expected to come immediately succeeding one of the most emotional moments I have witnessed in the last...forever? No."
    "But I guess it will, to some extent, numb some of the pain she must be feeling right now."
    "Besides, indulging in her interests every now and again might not be the worst thing ever in exchange for a guaranteed life worth of smooth sailing and even smoother omelets."
    "I just hope we don’t have to spend the entire day here. I don’t like that a place as loud and bright as this is on the brink of becoming another regular location for me."
    "And I also don’t like that we are now walking into a nerd store."

    scene amianime1
    with dissolve2

    a "..."
    s "..."
    a "So, as you can see, I lied to you."
    s "Betrayed by my own [niece]."
    s "Aren’t you the one who is supposed to always be on my side?"
    a "I {i}am{/i} on your side! I just knew that you wouldn’t come here with me if I told you the truth about where we were going, and the new volume of a manga I like came out today."
    a "There’s no [incest] in it at all."
    a "I mean, what? Who said that?"
    s "..."

    scene amianime2
    with dissolve

    a "Oh, look! New figures!"
    s "Did you really have to come here {i}today?{/i} Shouldn’t we have done something at least partially enjoyable for me?"

    scene amianime3
    with dissolve

    a "Oh, come on! We won’t be here long. I’m using my own money and everything. "
    a "I just need to pick this up before all the new copies sell out and {i}then{/i} we can go out and have our cute family date that I’m definitely not pretending is a real date and that we’re going to get married."
    a "I mean, what? Who keeps saying all of these weird things out of literally nowhere?"
    s "Ami, I think you have a problem."

    scene amianime1
    with dissolve

    a "It’s not me who’s wrong. It’s society."
    a "Now, come with me and don’t look at the back section of the store. "
    s "Why can’t I look at the back section of the store?"
    a "I will tell you when you’re older."

    scene amianime4
    with dissolve

    a "Over here, Sensei!"

    if bonus == True:
        s "I’m more than twice your age. I think."
        s "How old are you again, Ami?"
        a "Old enough! But that’s not a thing we should be yelling about in the store and you should probably come over here now!"

    s "..."

    scene black
    with dissolve2

    "I swallow the last few shreds of pride in my body (If that’s where pride is stored) and make my way over to Ami as she sifts through a bunch of brightly colored boxes and books."
    "And, despite apparently knowing exactly what she is here for, she sure takes her time in picking up and observing a lot of different items. "
    "Have I been lied to {i}again{/i} in such quick succession?"
    "Is this the so-called “rebellious phase” I have heard of?"
    "Is there a cut-off for when you can put someone up for adoption? Is that still a possibility if this keeps up?"

    a "You know, Sensei, I can probably find something here for you if you want me to."

    scene amianime5
    with dissolve2

    s "And why would I want you to do that, exactly?"
    a "Because...manga is more interesting than standing around and doing nothing all day?"
    s "I don’t do “nothing” all day. You clearly don’t understand the first thing about how exciting my life is."
    a "If it’s so exciting how come you haven’t smiled in like six million years?"
    s "I’m just waiting for the right moment."
    a "Uh-huh. Sure you are."

    scene amianime6
    with dissolve

    a "Really, though! There’s tons of stuff here I think you would like! And I’m not just saying that because I think it would be nice to share a hobby with you."
    a "Niki told me about how you two used to watch anime together, so what if we got you something...retro? Like something you guys watched way back when?"
    a "They even remake more popular series that have been out of style for a while sometimes. I’m sure I can find-"
    s "I’m going to stop you right there at the risk of you making me feel even older than I constantly feel around you."
    a "If it makes you feel any better, I probably wouldn’t like you as much if you weren’t so much older and bigger than me."
    a "I mean, what? Really, where are all of these comments coming from?"
    s "..."

    scene amianime7
    with dissolve

    a "I’m gonna get you something. I’ve decided."
    s "And I’ve decided that you’re not going to do that."
    a "But it’s a present! I never got you anything for Christmas. Are you really going to turn away a free thing that your [niece] lovingly selected for you?"
    s "Yes."
    a "What kind of genre do you want? Action? Drama? BL?"
    s "What is BL?"
    a "BL is-"

    scene amianime8
    with dissolve

    mo "What’s this?! Time for another weebnote?!"
    a "Oh. Molly’s here."
    a "That makes sense."
    mo "BL, or “boys love” is a wildly underappreciated genre in the anime and manga world where, get this- boys love each other!"
    s "Why would you even suggest that for me?"

    scene amianime9
    with dissolve

    a "Because I think it’d be hot."
    s "{i}What?{/i}"
    mo "Did you know that BL manga dates all the way back to the mid-70’s? It hasn’t changed much since then and is still aimed primarily at young girls, but the origins were actually much darker!"
    mo "Kaze to Ki no Uta, which is commonly referred to as the first instance of the BL genre, features stuff like prostitution, drug usage, and ra-"

    scene amianime10
    with dissolve

    mo "Uhh...actually, that’s it for today’s weebnote. I don’t really have anything else to say."
    a "What brings you here, Molly? I thought you and Tsuneyo were supposed to hang out today."
    t "I am Tsuneyo."

    scene amianime11
    with fade

    t "Surprise. I am also here."
    s "I’m assuming you were dragged along unwillingly as well?"

    scene amianime12
    with dissolve

    mo "Not at all, Sir. It was actually Tsuneyo’s idea to come here, not mine. I spent everything I currently have on gacha games, so I’m only here to act as a consult today."
    a "Tsuneyo’s finally getting into manga?"
    t "I received a Christmas bonus from my father and feel the need to spend it on things I am supposed to appreciate before it is too late and he asks for it back."
    s "I don’t think employers ever ask for bonuses back, but I guess I don’t know your dad all that well."

    scene amianime13
    with dissolve

    t "He does not like summer very much. I will not squander this opportunity to buy a brightly colored rectangle."
    mo "How about you, Ami? What are you doing here?"
    a "The new volume of My Sweet Prince came out today and I wanted to make sure I got it before it was sold out."

    if bonus == True:
        mo "My Sweet Prince? Isn’t that the one where the girl and her uncle-"
    else:
        mo "My Sweet Prince? Isn’t that the one where the accountant and her-"

    scene amianime14
    with dissolve

    mo "Oh my god."
    a "Hmm hm hmmmm~"
    s "..."

    "In a strange twist of fate, it looks like Ami lied {i}again{/i} and that the book she’s buying very much has the one thing she told me it {i}didn’t{/i} have."

    scene amianime15
    with dissolve

    mo "Well I guess that confirms {i}that{/i} suspicion."
    a "Just liking a certain trope in manga doesn’t mean you like it in real life, Molly. Everybody knows that."
    a "It normally does, though."
    mo "..."
    a "I won’t confirm nor deny anything."
    mo "I take it that means you two are...on a...{i}date{/i} then?"
    s "No."

    scene amianime16
    with dissolve

    a "Mm!"
    mo "Wait. Now I’m confused. Is this {i}not{/i} a meeting of secret, forbidden love? A taste testing of the most bitter fruit of all?"
    t "I believe that would be the “bitter melon,” which is famous for its medicinal properties."
    s "We’re just stopping by on our way back from...a place."

    scene amianime17
    with dissolve

    mo "That..."
    mo "You know that makes it sound even sketchier...don’t you, Sir?"
    s "I don’t know where your depraved mind goes after just hearing the word “place,” but I can assure you it’s not whatever you’re thinking."
    s "I doubt Ami wants to talk about it, though, so let’s just move on and-"
    a "I wanted to see my mom."

    scene amianime18
    with dissolve

    mo "Oh...{i}oh...{/i}"
    a "I’ve just missed her a lot lately. That’s all."
    a "Which is why we’re now...counteracting that with some place happy and..."
    mo "May I hug you?"

    scene amianime19
    with dissolve

    a "..."
    a "Yes, please."

    scene black
    with dissolve2

    "Molly wraps her arms around Ami and pulls her close, pressing their heads together."
    "They gaze into each other’s eyes and, if this weren’t such a heartfelt moment, I’d probably say something to emphasize just how much I’d appreciate it if the two of them would kiss right now."

    scene amianime20
    with dissolve2

    "Which is obviously not a thing I’m going to talk about."
    "I mean, how could anyone think that at a time like this? "
    "Nope. I don’t want that to happen at all."
    "Not even a little."

    s "..."

    "Not even a little."

    mo "I lost my mom when I was little, too. I know what it’s like."
    a "I know...I always wanted to ask you about how you managed to...talk about it so easily, but...it’s hard, you know?"
    mo "I do. But you know what’s easier? Hugging. So I hereby give you permission to hug me any time you want as a free action."

    scene amianime21
    with dissolve

    a "Thank you, Molly. I’ll be here for you if you ever need me, too."
    mo "I’ll remember that. "
    a "Hey, how come we never do anything with just the two of us?"
    mo "Probably because you already have Ayane and Maya and I would just be getting in the way."
    a "Let’s hang out soon. Just us."
    mo "I’d like that a lot..."
    s "..."

    "{i}Not even a little.{/i}"

    t "It appears everyone has forgotten that I lack a mother as well."

    scene amianime22
    with fade

    mo "Ah! I’m sorry, Kendo Princess! I just know that...your affinity for hugs is not as high as mine! And that you wouldn’t want to get involved in something like this..."
    a "And I just...wasn’t even thinking. Sorry, Tsuneyo."
    t "Abandoned by my own party members. I truly am an outcast."
    s "I’ll hug you, Tsuneyo. We don’t need them."

    scene amianime23
    with dissolve

    t "I would rather die."
    s "That...seems like an exaggeration."
    t "It is not."
    s "Didn’t we hug on Halloween that one time?"
    t "I have no idea what you are talking about."
    s "When-"
    t "I would never hug a man as horrible as you."
    s "It was after we went outside and-"
    t "Never."
    s "And Molly was-"
    t "It would simply not happen."
    s "But-"
    mo "Just give it a rest, Sir. Your charisma isn’t high enough to break through to Tsuneyo yet."
    s "That’s fine, but..."
    s "How long are you two going to stay like that for?"

    scene amianime24
    with dissolve

    mo "..."
    a "..."
    mo "Maybe just a little bit longer."
    t "Ahh, youth..."
    s "Tsuneyo, you’re the same age as them."
    t "Then why will no one hug me?"
    s "I literally just offered-"
    t "No thank you."
    mo "..."
    a "..."
    a "You smell really nice."
    mo "I was actually just about to say the same thing to you."

    scene black
    with dissolve2

    if bonus == True:
        "I guess Ami winds up mistaking Molly for a relative or something since it seems she has a hard time separating from her, but I’m sure it’s probably closer to the fact that she just has someone she can relate to."
        "Even if Ayane’s mom isn’t around anymore, I can’t imagine Ami being able to confide in her in the way that she could with someone who’s actually felt the same sort of pain she has."
        "But pain is not something I intend to dwell on any longer when its abundance is one of many things in this life that neither myself nor anyone else is able to avoid."
        "I will focus on the brighter things and what it is that illuminates them."
        "Ami finds her manga (Which may or may not contain [incest], but probably does) and pays for it at the register after separating from the others."
        "She clutches it to her chest as the two of us exit the store together and make our way out into the street, bustling with foot traffic due to the sudden increase in temperature."
        "Then, before long, she’s pulling me around once again."
        "Just..."
        "Hopefully to somewhere I won’t feel out of place in this time."
    else:
        "Not even a little."

    $ renpy.end_replay()
    $ ami_love += 1
    $ amidate50p2 = True
    stop music fadeout 8.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump amidate50p3

label amidate50p3:
    scene amidatecafe1
    with dissolve2
    play music "lifeismostlygood.mp3"

    "The portion of the day we spend in the entertainment district is mostly negligible, so I guess I can find solace in the fact that Ami isn’t suddenly lying to me about {i}everything.{/i}"
    "I can also find solace in the fact that she has offered to pay for me despite me telling her multiple times that it isn’t necessary."
    "But hey, who am I to refuse free food when it’s so kindly offered up?"
    "I’ve humored her enough to wind up beside her at some random cafe. Turning down an act of kindness now would make it appear like I have no desire to be here at all."
    "And, you know what? Now that the sad portion of the day is over, I really don’t hate this."
    "It’s nice being able to focus on what’s directly in front of me without needing to wrap my mind around any obnoxious subtext or deflect all of the horrible things I’ve done as they’re thrown back at my face."

    a "So...I guess you and Molly made up?"

    "At least I had a decent thirty minutes or so."

    s "Forget what happened between Molly and {i}me.{/i} For a second back there, I thought you two were going to run away together."

    scene amidatecafe2
    with dissolve

    a "Huh? What gave you that idea?"
    s "Probably the part where your faces were touching and you were gazing into each other’s eyes."

    scene amidatecafe3
    with dissolve

    a "Were you even listening to that conversation?! It was really sad! We were just having a cute bonding moment!"
    s "It would have been cuter if you two kissed."
    a "You...don’t mean that! And stop deflecting! I still need to know what happened between you two since you never tell me anything anymore!"

    scene amidatecafe4
    with dissolve

    s "You know I don’t {i}have{/i} to tell you everything, right?"
    a "Yeah, but I tell {i}you{/i} everything so it only seems fair if you maybe tell me {i}some{/i} things every once in a while."
    s "Nah. I'm good."

    scene amidatecafe5
    with dissolve

    a "Fine. I’ll just ask {i}her{/i} then since we’re making plans to hang out soon. {i}She’ll{/i} tell me."
    s "Just leave it alone, Ami. Please."

    scene amidatecafe6
    with dissolve

    a "Please? But you never say please. Is it really that serious? Because you made it sound kinda unimportant the last time I asked you about it."
    s "It’s just a personal matter that the two of us decided to handle on our own instead of enlisting the help of everyone else. "

    scene amidatecafe7
    with dissolve

    a "Personal?"
    s "That’s what I said."
    a "..."
    s "Now, since we’re done talking about-"
    a "How personal, Sensei?"
    s "Excuse me?"
    a "What do you mean by “personal?” That makes it sound like you two have a relationship deeper than just teacher and student."
    s "Maybe we do?"
    a "Are you friends now?"
    s "Sure. I guess so."
    a "Then how come you were avoiding her so much when it seemed like she needed you most? That doesn’t sound very friend-like."
    s "Here’s a better idea- how about we eat and get back to our {i}date?{/i} Doesn’t that sound good, Ami?"
    a "No. You two stopped talking for two months and are now back to acting like nothing ever happened. I want to know what caused it."
    s "And I want you to mind your own business."
    a "But your business {i}is{/i} my business. I can’t make you happy if I don’t know how to get rid of what’s making you sad."
    s "Molly was never {i}making me sad.{/i} I just...needed time to think about some things."
    a "..."
    s "..."

    scene amidatecafe1
    with dissolve

    a "Molly’s so pretty. Isn’t she, Sensei?"
    a "Her skin is so pale and soft...and her eyes are so blue that you can get lost in them if you stare for too long."
    s "What are you getting at?"
    a "Nothing~ Just thinking about running away with her and stuff."
    s "Well, make sure to write if you do. I’ll be renting out your room for extra money."

    scene amidatecafe3
    with dissolve

    a "Just like that?! You’re not even going to try and get me to stay?!"
    a "Also, never joke about renting out my room! I can hear Ayane unzipping her wallet as we speak!"
    s "Is it safe to say we’re moving on now? Or are you going to keep trying to ruin the date you literally forced me to come on?"

    scene amidatecafe8
    with dissolve

    a "We can move on...I don’t want to ruin anything."
    a "I just get kinda jealous when I’m not in the loop and it feels like there have been a lot more loops than normal lately."
    a "But you can talk to me about stuff if you ever need advice, Sensei."

    scene amidatecafe9
    with dissolve

    a "If it’s something involving you, you can pretty much guarantee that I’m the number one person to come to! I’d put more care into advice for you than I would for even myself!"
    s "That’s bad and you should always prioritize yourself over other people."
    a "I refuse!"
    a "You need to be happy or my entire existence is meaningless!"
    s "I can’t imagine your parents would have been very happy to hear that while you were talking to them earlier."

    scene amidatecafe10
    with dissolve

    a "Oh. Uhh...Can you maybe...stop joking about them like that?"
    a "I’m obviously trying to be a little more open about what happened, but...I’d prefer if we could still be kind of sensitive about it."
    a "Today was a big step for me. And even though you were there to hold my hand, I’m going to keep working at it so I can maybe walk on my own some day."
    s "Sure. I didn’t really mean it as a joke. I-"
    a "I know, I know. Sudden mentions of them just throw me off."
    a "Like, it doesn’t completely register that they’re gone until {i}after{/i} the sentence registers. "
    a "It’s like there’s another mini accident inside of my mind each time I- nope. Nope. Don’t want to think about this anymore."
    s "Then think about something else. Like how you haven’t even touched your food yet and I’m already finished eating."

    scene amidatecafe11
    with dissolve

    a "Oh my God, already? Who are you, Maya?"
    s "It’s not like we just sat down. We’ve been here for a while. In fact, I wouldn’t be surprised if your food was already cold."

    scene amidatecafe12
    with dissolve

    a "Has it really been that long?..."
    a "Sorry, I’m just..."
    a "I’m a little nervous because there’s something I’ve been wanting to show you...and I don’t think I’m really gonna get a better time than this date to do that."

    "Ami curls her fingers around the base of her ponytail and begins to bob it up and down."
    "I’ve seen her do this in the past when she gets nervous- which is strange since she’s been twintailed for the majority of the time I’ve spent with her and I’ve never seen her do it then."
    "Either way, I can tell that she’s being honest again. I just don’t know what it is that she’d get so nervous about telling me when, if anything, she’s one of the most commonly open people I know."

    s "Is the thing you’ve been wanting to show me the next stop on our trip?"
    a "No...it’s actually...something I have on me now."
    s "So...a present?"
    a "Not really...but...also kind of?"
    a "I don’t know. It’s probably dumb. "
    s "You’re right. It probably is."

    scene amidatecafe13
    with dissolve

    a "Hey! "
    a "You’re supposed to say, “It won’t be dumb if it comes from you, Ami! You’re amazing and pretty!”"
    s "You’re pretty, yeah. But you’re also kind of an idiot."

    scene amidatecafe14
    with dissolve

    a "But...I..."
    s "You’re my idiot, though."

    if bonus == True:
        s "Which is a weird thing to say since I’m technically claiming ownership of you and I don’t technically enjoy being a legal guardian-"
        s "But it is what it is."

    scene amidatecafe15
    with dissolve

    a "How did you manage to turn calling me an idiot into one of the sweetest things you’ve ever said to me?"
    s "I’ve always had a way with words, I guess."
    a "Yeah..."
    a "And that’s exactly why I’m so nervous about this."
    s "What do you-"

    scene amidatecafe16
    with dissolve

    "Ami slides a sheet of paper out of the bag she’d been keeping by her feet and holds it out in front of her."
    "Her eyes scan the page for an excuse to back down, but I guess they aren’t able to uncover any as she remains silent apart from the audible tapping of her feet underneath the table."

    a "So..."
    a "Believe it or not, I’ve never been very good at expressing my feelings."
    s "I don’t believe that at all. All you do is express your feelings."

    scene amidatecafe17
    with dissolve

    a "I know that. But it...never feels like I can properly get everything that I’m trying to say out."
    a "And I don’t think I will today either, but...I remember you telling me something a long time ago about how poems were how people like that could find a way to survive in this world."
    a "It didn’t make much sense at the time since I was just a kid...but I think I kind of understand it now."
    a "So I thought I’d give it a try."
    a "It’s just kinda nerve wracking since I know you were like...a poetry expert a long time ago."
    s "You...wrote me a poem?"

    scene amidatecafe18
    with dissolve

    a "I...tried to."
    a "I don’t know if it’s any good, though."
    s "Well, that’s...unexpected."
    a "How come?"
    s "You’ve just never seemed like the “writer” type to me."
    a "Right. I’m the “idiot” type to you."
    a "But I tried really hard, so..."

    scene amidatecafe19
    with dissolve

    a "Here goes nothing."
    s "..."
    a "..."

    "Ami stops tapping her feet and focuses whatever energy she was using on that to stabilize her hands."
    "It’s easy to spot her nerves with how much the paper she wrote this on is trembling, and I’m sure she notices this as well as she needs to readjust her fingers a few times just to be able to read it."
    "I’m not sure what to expect, but I know now that however bad it is, I’m going to have to make sure that she thinks it’s good."
    "Such is the job of an [uncle]. And such is the job of-"

    a "I named this poem “My Life With You.”"
    a "..."
    s "..."
    a "A room full of sunshine, blacked out by a sheet.\nIt was there you and I were destined to meet."
    a "Not for the first time, you’ve been there from the start.\nBut that room full of sunshine filled a hole in my heart."
    a "We both couldn’t see it, but we knew it was there.\nSo with holes in our clothing and knots in our hair-"
    a "We’d get out of bed for just minutes each day.\nWe didn’t speak much, there was nothing to say."
    a "But one day that changed and the dark disappeared.\nWe took down that sheet and we faced what we feared."
    a "You became my world, since the old one was gone.\nThen one day it hit me, like I’d known all along."
    a "No sheet can contain the light from the sun.\nAnd all darkness must die once daylight’s begun."
    a "I guess it sounds silly, but I know that it’s true."
    a "A room full of sunshine- that’s my life with you."
    s "..."
    a "..."

    scene amidatecafe20
    with dissolve

    a "Ta-da. I love you."
    s "That was..."

    scene amidatecafe21
    with dissolve

    a "Wait. I don’t know if I’m ready to be made fun of yet. I know it was bad, but I worked really hard and-"
    s "No, Ami. That was way better than I expected."

    scene amidatecafe22
    with dissolve

    a "It...was?"
    a "But you’re only saying that because you expected literally nothing, right? Like I could have said {i}anything{/i} and it would have been better than what you were expecting."
    s "No, I mean I genuinely liked it and I’m really impressed you were able to write that."

    scene amidatecafe23
    with dissolve

    "I just wish that I could bask a little longer in the relevancy it has pertaining to my relationship with Ami."
    "I’m sure that day will come eventually, and I’m sure those memories may find a way to sneak back into my mind."
    "But for now, I’ll have to take her words for nothing more than their face value and the connotations tied to them."
    "And even though it all still seems a little surreal-"
    "I think I better understand why Ami feels the way she does about me now."
    "It’s just not a very good reason."

    a "You really liked it?! You don’t think I’m a failure and that I should give up on poetry immediately?!"
    s "I don’t."
    s "In fact, I think you should write more."

    scene amidatecafe24
    with dissolve

    a "Oh my God, Sensei...you have no idea how much of a relief it is to hear that."
    s "Did you really think I was going to just tell you to quit after hearing that?"

    scene amidatecafe25
    with dissolve

    a "A little..."
    a "I wrote this a little while ago, but...when I was going through some of Mom’s stuff last night, I found a bunch of her old poetry and remembered how much you liked it."
    a "I never really understood what the appeal of poems was back then, but reading them now...I think I finally get it."
    a "She had such an...um...eloquent way of writing? Is eloquent the right word?"
    s "..."

    scene amidatecafe26
    with dissolve

    a "You know what? I’ll just read one that I took a picture of and you can let me know if I’m on the right track."
    a "I’m sure that it’ll make my poem sound like, {i}really{/i} bad since she was basically a pro, but-"

    stop music
    play sound "static.mp3"
    scene spiderbug with flash
    scene amidatecafe27 with flash
    play sound "glass.mp3"

    a "Ah."

    "Ami drops her phone and it bounces off the table into the side of an empty glass."
    "The glass once held water, but it will never hold anything again."
    "I watch the shattering as if my world is plunged into slow motion."
    "Each shard moves in a different direction, some moving more distance than others without rhyme or reason as to why."
    "I am sure there is a scientific explanation for it, but I’d prefer to imagine it’s just random chance."
    "A nearby table joins in on the action and watches on, mesmerized as well."
    "There is something beautiful about being broken that attracts all sorts of onlookers."
    "I am glad the glass is what attracted most when there is so much that is broken all around me."

    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."

    scene amidatecafe28
    play music "lifeismostlygood.mp3"

    a "Huh? What happened to my phone? I was just-"

    scene amidatecafe29
    with dissolve

    a "Wait, what happened to that glass?! "
    s "Do you really not remember?"

    scene amidatecafe30
    with dissolve

    a "Remember what? What are you talking about?"
    s "You...literally dropped your phone into the glass just a few seconds ago."
    a "I...did?"
    s "Yeah...are you feeling okay?"

    scene amidatecafe31
    with dissolve

    a "Yeah. I feel totally fine. I...I have to clean that up, though. Somebody could get hurt."
    s "I’ll just flag down our waitress. I’m sure they have someone who-"
    a "No! That’s not fair to them."
    a "It’s my fault this happened. Besides, I’ve cleaned up a lot worse than this."

    scene amidatecafe32
    with dissolve

    a "But I guess I probably don’t have to explain that since my poem probably...reminded you of...anyway, yeah. I’m going to clean up the glass now."
    a "I’m sorry for causing a scene, Sensei. I know how much you hate being the center of attention."
    s "It’s fine..."
    s "Are you really sure you’re okay, though?"
    a "I’m..."
    a "I have to clean up the glass."

    scene black
    stop music

    "Ami bends down and begins to scoop the shards of glass into her hands."
    "I wonder if she, too, appreciates the beauty in how each and every one of them is unique."
    "I wonder if she, too, acknowledges how tragic it is that the object is now devoid of all purpose."
    "She cuts her hands as she cleans up the accident."
    "It reminds me of something."

    $ renpy.end_replay()
    $ ami_love += 1
    $ amidate50p3 = True

    "........."
    "......"
    "..."

    jump amidate50p4

label amidate50p4:
    "..."
    "......"
    "........."

    scene tree3
    play music "newhope.mp3"

    "We board a bus that’s moving backwards and all I can think about is the sound the tires make."
    "It’s a low pitched hum, not far dissimilar to the sound of a hummingbird’s wings as they defy what we’ve come to expect of some of the creatures living in the same world as us."
    "Soon, the night will come. "
    "It will replace the sun and shift the tide, dragging many creatures back into the shallowest parts of the ocean- some willing, some not."
    "We take a seat in the back and look into each other’s eyes."
    "I take Ami’s hands in my own and observe the minor gashes she obtained while trying to do something good."
    "They open back up and leak out the only fluid meant to be kept in."
    "I press my tongue to them and drink in her existence."
    "A warmth floods over me like a ray of sunlight made weaker by a bedsheet."

    play sound "static.mp3"
    scene amibus1
    with flash
    stop sound

    a "Do you believe in God, Sensei?"
    s "Do you?"
    a "I do."
    a "Maya makes fun of me for it sometimes, but I think that he’s real."
    a "I don’t know if he’s watching every second of every day, but I think he’s there."
    a "And I think that all of the suffering that you and I have endured is just his way of testing us."
    s "Testing us for what?"
    a "..."
    s "Testing us for wh-"
    a "It is a test to see if we are worthy of Heaven."
    a "To see if we can endure the harshness of reality and overcome adversity in order to gain one of the many limited seats in the giant sky castle all good boys and girls go to when they die."
    a "Will you sit with me, Sensei?"
    a "Will you come to the sky castle with me?"

    play sound "static.mp3"
    scene amibus2
    with flash
    stop sound

    "We talk at length about the afterlife while swapping seats in the classroom."
    "Ami breathes in a sequence that is easily decoded. She is trying to communicate with me in a secret language we devised when we weren’t as tattered."
    "One. Two. One. Four. Eight."
    "The amount of seconds between breaths. It moves from side to side, neglecting all that is in the middle."
    "It’s like an abacus, in that sense."
    "I’m like an abacus in that sense."
    "The parts of me furthest away from the center are the ones that do the most work."
    "Everything in the middle is just blank."

    a "Do you ever wonder where we go when we die?"
    s "Is it not the sky castle you were alluding to in the sentences prior to this?"
    a "Do you ever wonder anything at all?"
    s "I wonder about all sorts of things."
    a "Tell me."
    a "Tell me the things you think about on bus rides backwards."

    "I remove a list from my pocket that I always keep on hand in the event that someone asks me this question."
    "I begin to read from it."

    s "When I was younger, I used to take the tips of my thumb and my index finger and make a ring out of them. "
    s "I’d wrap the ring around my ankle and, as the years went by, I stopped being able to fit all of it inside."
    s "I think it was when I could no longer close the ring anymore that I realized I was unhappy."
    s "It was good to be growing, but what if I was growing too much?"
    s "Tell me the things you think about, Ami."

    play sound "static.mp3"
    scene amibus3
    with flash
    stop sound

    a "On bus rides backwards, I like to think about us."
    s "Us?"

    "I ask her, “Us?”"

    a "Us."

    if amifingered == False:
        a "Like...“is this really working?”"
        s "Is what working?"
        a "You and me at arm’s distance. "
        a "I’ve done almost all I can and yet you’re still so far away."
        a "Is that really going to work?"
        s "Why wouldn’t it?"
        a "Because neither of us are happy."
        s "Would changing the proximity of our physical distance truly work in adjusting that?"
        a "It would bring us closer. Literally."
        a "We’re not meant to be apart."
        a "We’re meant to sit in the sky castle together."
        s "I see."

    else:
        s "I see."

    "One. Two. One. Four. Eight."
    "The pattern stays the same."
    "An onslaught of footsteps approaches from directly behind me, but there’s not enough room in here to move my head."
    "I also fear that it would fall off of my shoulders if I were to try."

    av "Next stop: Somewhere else."

    play sound "static.mp3"
    scene amibus4
    with flash
    stop sound

    a "If I asked you to start reading me bedtime stories before I go to sleep, would you?"
    s "Of course."
    a "Thank you, Sensei."
    a "The sound of your voice always puts me at ease."
    a "I particularly enjoy the way you enunciate わ and how it always sounds as if you are breathing a sigh of relief when saying my name."
    a "Like you are glad that I still exist in a form that you can talk about without slipping your hands into your pockets."
    a "When you grasp at the fabric inside of them, do you ever find holes? "
    a "Does anything ever fall through?"

    "The bus ride continues and I watch the clouds through the windows of a well lit church."
    "I can smell candles scented with something reminiscent of the earliest years of my life, though it could just be dying wax."
    "Ami’s hands open up again, but she smears the blood onto a pew built of concrete before sending signals to her brain that cause her eyes to tilt in the direction of mine."

    scene amibus5
    with dissolve2

    a "I can feel it, Sensei."
    a "I can feel His light."
    a "And though it isn’t mine to hold, I want nothing more than to wrap my arms around it. I want nothing more than to be swallowed by it."
    a "I love you so much."

    play sound "static.mp3"
    scene amibus1 with flash
    scene amibus5 with flash
    stop sound

    a "Will you tell me you love me too?"
    s "Of course. I love you, Ami."
    a "Thank you, Sensei."

    play sound "static.mp3"
    scene amibus6 with flash
    stop sound

    a "Thank you, Sensei."
    a "That was a really random time to say that, but I love you too."
    a "Are you feeling any better now?"
    s "What do you mean?"

    play sound "static.mp3"
    scene amibus7 with flash
    stop sound

    a "What do you mean, “What do you mean?”"
    s "I mean what do you mean?"
    a "I don’t know what you mean."

    "Ami lovingly caresses a giant chicken as the bus begins to move faster."
    "It stops at so many different places and I can’t help but applaud the constant advancement in modern transportation technology."
    "One. Two. One. Four. Eight. Yet the middle parts drop out again as she points me to a chair."

    scene white
    with flash

    "I sit down on it and can’t help but feel like I’m usurping the role of king from an invisible entity who doesn’t want me to sit here."
    "Ami brings herself down to her knees and kisses my feet."

    a "This will help you walk."

    "Her tongue slips out like a clam searching for salt."

    play sound "static.mp3"
    scene amibus8 with flash
    stop sound

    "She laps up the effort I place into tainting sacred grounds and dirties herself in the process, but at least my feet are clean now."
    "Her tongue dissolves into a sludge that seeps back into her throat only to ooze out of every pore and, in that moment, looks more beautiful than I have ever seen before."

    play sound "static.mp3"
    scene amibus9 with flash
    stop sound

    "The ooze seeps back into her flesh before it seizes the opportunity to drip onto the ground of an area undiscovered before its ultimate absorption provokes the budding of a thousand eyes."

    a "Do you believe in God, Sensei?"

    "She asks again, but the beauty before me eliminates any chance I have to deny it once more."
    "I am condemned by an entity unseen- the same one who granted her an ever-abundance of vision."
    "The condemnation carries with it a single letter carved out of wood that fuses to my back the same way my bed in the early morning had been."
    "I fall as I am unable to bear its weight but encounter a moment of tranquility when my path intertwines with that of a REAL HUMAN FEMALE."

    play sound "static.mp3"
    scene amibus10 with flash
    stop sound


    saki "Greetings, you who are highly favored! The Lord is with you."
    s "Where? I can’t see him."
    saki "Greetings, you who are highly favored! The Lord is with you."
    saki "Greetings, you who are highly favored! The Lord is with you."
    saki "Greetings, you who are highly favored! The Lord is with you."

    "The REAL HUMAN FEMALE gets caught on repeat and my journey comes to an untimely demise."

    play sound "static.mp3"
    scene amibus1 with flash
    stop sound

    "We board a bus that’s moving backwards and all I can think about is a spot on the window where the guts of a bug we crashed into are smeared."
    "Dried by the sun and picked partially clean by whatever predators dared to crawl upon an invisible barrier, the spot casts a small shadow upon Ami’s arm."
    "In between the miniature hair follicles covering it, I imagine the bug springing back to life."
    "It’s blurred out, however, as I can not imagine what type of insect it was from just a stain alone."
    "The bus continues on (Or off) and I drift in and out of consciousness at the command of violent glares brought on by the god in the sky."
    "Oh."
    "So I do believe after all."

    a "Sometimes, I wish you knew how to drive."
    a "I think it would be nice to kind of just...drive around with you sometimes. "
    a "We wouldn’t have to go anywhere. Just being with you and taking in the sights would be enough."
    a "We could listen to music on the radio and talk about the things we’re afraid of admitting in front of others."
    a "Sometimes, I wish you knew how to drive."
    a "Because it would give us something to do when everything else disappears."
    s "What do you mean, “When everything else disappears?”"

    scene amibus6
    with dissolve

    a "Hm?"
    a "Did you just wake up?"
    s "If you thought I was asleep, who were you talking to just now?"

    scene amibus11
    with dissolve

    a "Sensei, I haven’t said anything this entire ride. You passed out the second we got on."
    s "What?"
    a "It’s obviously my fault for dragging you around all day, so I’m sorry if it was a little too much."
    s "And your hand?"
    a "What about it?"
    s "Is it okay?"

    play sound "static.mp3"
    scene amibus12 with flash
    stop sound

    a "It's totally fine!"
    a "I guess the cuts from the glass weren’t really that deep since you can barely even see them anymore."

    scene amibus6
    with dissolve

    s "I...see..."
    a "It still stings a little, but I’m sure I’ll feel totally normal by tomorrow."
    a "Oh, which reminds me-"
    s "Ami, I don’t think I have the energy required to go on an outing like this two days in a row."
    a "{i}Actually{/i}, what I was about to tell you is that I’ll be working all day tomorrow and that you won’t need to put up with me {i}at all.{/i}"
    s "All day? Did Uta call out or something?"

    scene amibus13
    with dissolve

    a "That’s the weird part. I got a text from Osako-chan while you were asleep saying that Uta hadn’t answered her phone all day."
    a "She was supposed to work today, too, but she just kinda...didn’t show up. "
    a "So if that happens again tomorrow night and nobody is there to cover for her, the cafe will have to close early or something and that would probably be pretty bad for business."
    a "I really hope she’s okay. She’s never done anything like this before."
    s "Should we maybe go check on her?"

    scene amibus14
    with dissolve

    a "If she’s not in school tomorrow, I think you should. I won’t have time, though, since I’ll have to go straight to work."
    s "It’s fine. I’ll just text Io to- oh."
    s "I guess I don’t get any service here."

    scene amibus11
    with dissolve

    a "Io? Since when do you have {i}her{/i} number? I thought she didn’t talk to anybody except Uta?"
    s "I am one of the very rare exceptions, I guess. But it looks like I’ll have to just ask her when we get home."

    scene amibus1
    with dissolve

    a "I guess so..."
    s "..."
    a "..."
    a "Sensei. Can I ask you something?"
    s "Sure. What’s up?"
    a "..."
    a "Do you believe in God?"

    scene black
    with dissolve2
    stop music fadeout 15.0

    "The bus continues on (Or off) and I drift in and out of consciousness at the command of violent glares brought on by the sky."
    "Ami does the same, collapsing onto my shoulder at several points following a question that would have been better suited for someone else."
    "Her skin feels much colder than normal and I wrap my arm around her to distribute some of my warmth."
    "Her breaths are unsteady. One. Two. One. Four. Eight."
    "Her lungs can’t seem to decide what it is they should be doing."
    "And my mind can’t seem to decide where it is that it should wander."
    "We get off the bus that’s moving backwards."

    stop sound

    "And we bend ourselves until we wind up at our door."

    "///////////////////////USER1 HAS SUCCESSFULLY LOGGED IN"

    $ renpy.end_replay()
    $ amidate50p4 = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump returntosummer1

label aminew1:
    scene aminewone1
    with fade
    play music "10c.mp3"

    a "And that’s exactly why I don’t think we should have gym class anymore."
    s "This breast envy of yours is really starting to get out of hand if you’re thinking of rebuilding the education system to cope with it."

    scene aminewone2
    with dissolve

    a "Breast envy is something that millions of girls struggle with every day, Sensei! We all know that it’s not just me who feels this way. Right, Maya?"
    m "Please refrain from including both me and my breasts in any conversation our teacher is a part of. "
    m "In fact, please don’t include my breasts in {i}any{/i} conversation. Especially when I don’t feel the same sort of envy you do."

    "I somehow wind up walking  back from school with Ami and two other girls who could probably pass for residents of my home on a census test if things really came down to it."
    "Why I was forcibly dragged along when the smallest of the bunch seems to almost always stray from anything that I’m a part of, I’m not sure. "
    "But here we are, talking about breasts or the lack thereof on the way to..."
    "To..."

    s "Where exactly are we going again?"

    scene aminewone3
    with dissolve

    ay "Excellent question, future husband! We’re on our way to a cafe not far from here so we can take advantage of the couple’s discount they’re offering."
    a "We tried going as a trio last time but...things didn’t really work out the way I expected them to. "

    scene aminewone4
    with dissolve

    ay "It’s not a {i}trio,{/i} Ami. It’s called a {i}throuple.{/i} And the fact that the cafe would not offer us a discount proves that they are bad people who don’t care about inclusivity."
    a "Then...why are we going back exactly?"

    scene aminewone5
    with dissolve

    ay "Because we’re hungry and you kept looking at pictures of the parfaits they’ve been posting on Instagram all day saying, “Wow. I want to go there.”"
    ay "Oh. And we also have four people now."
    s "So, which one of you am I dating today?"
    ay "All of us. We are a quadrouple- a real type of thing that actually exists. And if the cafe doesn’t like that, they will be met with destruction."

    "As you can see, it’s a pretty normal day for me. "
    "I’m not sure how I’m going to deal with walking into a cafe for a couple’s discount with three girls who could pass for my daughters but I guess that’s a problem I’ll have to figure out how to handle later."
    "And, as much as I’d like to say that the cafe will probably just assume I’m their teacher, I can’t really see how that would be any better than a parent."
    "In fact, that would probably be even worse."
    "Honestly, I think I’m kind of screwed either way. But at least I also get to screw three girls in the process."
    "Just in the less fun way."

    scene aminewone6
    with dissolve

    a "Are you sure you’re okay with tagging along, Sensei? You...didn’t have anything else to do tonight?"
    s "Since when do you care about whether or not I’m free? Isn’t wanting to be with me every waking hour of the day like, half of your personality?"

    scene aminewone7
    with dissolve

    a "Is the other half being lovable and fun and nice and cute and kind and cute? And also cute?"
    s "No. It’s being annoying."

    scene aminewone8
    with dissolve

    a "Mm!"
    ay "Don’t worry, Ami! I think you’re all of those things. But I think you may have forgotten to mention your best quality which is, in my opinion, how cute you are."

    scene aminewone9
    with dissolve

    a "How come you can’t be more like Ayane?"
    s "I don’t really have the self-confidence to be hitting on myself all day long."
    a "Not that part. The part with how much she appreciates me and how she calls me cute even when I don’t have to tell her to."
    s "Probably because walking around school and talking to people about how cute my niece is would likely put me on some sort of list somewhere."
    m "I think that might be the most reasonable thing I’ve ever heard you say."
    ay "I’m not related to you, Sensei. You can call me cute as many times as you want and you won’t even have to worry about any lists since I am rich and can get you out of trouble if I have to."
    s "Is {i}that{/i} really what you want me to be, Ami? Are you sure?"
    ay "You’d think I’d be offended by getting called {i}that,{/i} but it really just made me super excited instead."

    scene aminewone10
    with dissolve

    m "Ew."
    a "Okay, so maybe {i}don’t{/i} be more like Ayane. But you are allowed to dote on me {i}a little{/i} bit, you know."
    a "Everybody already knows we’re close, so no one is going to put you on any list if you just remind them every once in a while that I am your entire world and that you are mine."
    ay "Ami’s right, Sensei. You should really cherish her more."
    a "See what I mean? If-"
    ay "Especially since you’ll be running away with me and never looking back as soon as I graduate. If you’re not nice to Ami now, how will she remember you when that happens?"

    scene aminewone11
    with dissolve

    a "Just go home if you’re going to say things like that, damn it!"

    scene black
    with dissolve2

    "Of course, Ayane doesn’t wind up going home since she is apparently the only one who remembers how to get to the cafe."
    "I highly doubt Ami is being serious when she says things like that anyway, though."
    "Even with how relentless Ayane’s flirting can be, it’s clear that she and Ami are extremely close and that it’s {i}probably{/i} just all in good fun."
    "Do I think Ami would cause physical harm to {i}someone else{/i} for doing what Ayane does? Absolutely."
    "At the bare minimum, I think she’d try."
    "But I think that, for whatever reason, Ayane gets a free pass."

    scene aminewone12
    with dissolve2

    "Eventually, we make it to what seems like less of a cafe and more of a hole in the wall that just happens to have a dessert menu."
    "It must be relatively new since there are still barely any decorations on the walls and the entire back half of the store is blocked off for some reason."
    "I can’t say I’m really looking forward to spending my night here on account of the entire menu being full of things I wouldn’t typically consume, but..."
    "At the very least, I have enabled the couple’s discount the girls were after."
    "Unless Ayane proceeds to ruin everything again by saying that we are a “quadrouple.”"

    barista "Welcome in! Table for four?"
    ay "Two tables for two, actually! We’re here for the couple’s discount."
    barista "Oh, sure! I take it you two girls are a couple then?"
    ay "We are!"
    m "I have never seen this girl in my life."

    scene aminewone13
    with dissolve

    ay "{i}Maya, what are you doing?{/i}"
    m "What? It’s only a 10%% discount. I’m going to be spending basically the same amount of money either way."
    ay "{i}Okay, but that’s not why we’re doing this, remember?{/i}"
    m "..."
    barista "Um..."
    ay "Just go along with it and {i}I’ll{/i} pay for you, okay?"

    scene aminewone14
    with dissolve

    m "I am in love with this woman."
    ay "Hahah...hah..."
    barista "Oh! Well...that would certainly make the two of you a couple then."
    barista "Follow me right this way. I’ll take you to a table in the back where you two won’t be interrupted."
    m "Good. I would not want someone to overhear me talking about all of the love that I have for this person."

    scene aminewone15
    with dissolve

    barista "And you two near the door, will you also be-"
    barista "Wait...I’m sorry, Sir. But you seem a little too old to be-"
    a "I consent to a romantic relationship with this man and am not being taken here against my will."
    s "..."
    barista "..."
    a "..."
    s "I’m her uncle and we don’t need the discount."

    scene aminewone16
    with dissolve

    a "Sensei, what the heck?! We were so close."
    s "It’s fine. I’m going to be paying anyway and a 10%% discount is not worth what little pride I have left."
    s "If it were 20%%, that would be a different story."
    barista "A...table near the window it is, then."
    barista "Please wait one moment."

    scene black
    with dissolve2

    "Ayane and Maya are taken to a table in the back to make out or something while Ami and I wait near the door for the barista-slash-waitress or whatever she is to return."
    "We’re seated shortly after and Ami, who apparently does not care at all about how much money I am willing to spend today, orders way too much food."
    "Surprisingly, it’s all taken over to us within five minutes- along with a complimentary pot of hot tea that I {i}will{/i} consume, unlike all of the other brightly colored desserts that have now joined us at the table."

    scene aminewone17
    with dissolve2

    a "You know, Sensei...I really wouldn’t have minded if you just decided to go along with the couples thing."
    a "I have done my research and know what I have to say to avoid getting you into trouble with anyone who does not understand the way we feel about one another."
    s "What way? We’re literally just related and haven’t done anything romantic together."
    a "Right, yeah. I obviously know that. But what I’m saying is that we {i}could{/i} and it would be okay because I’ve done my research."
    s "Is there something you’d like to admit to me, Ami? Like...perhaps something about your feelings for me?"

    scene aminewone18
    with dissolve

    a "Boy! This cake sure looks good, doesn’t it?!"
    s "..."
    a "I’m so glad that my uncle, who I’m not romantically involved with, is buying it for me today on this totally normal day of no importance whatsoever!"
    s "You should be glad. I’m spending probably an entire day’s worth of pay at this place for you."

    scene aminewone19
    with dissolve

    a "Yeah, but that’s your fault. You could have afforded another parfait if you just swallowed {i}what little is left of your pride{/i} and pretended to be in love with me."
    s "I’m not even going to eat {i}this{/i} parfait. Parfaits are not currency and mean nothing to me."
    a "Why would you even order it then?"
    s "Because the alternative would have been sitting here without any food. And there is nothing more disconcerting than an older man bringing a young girl to a cafe and just...watching her eat."

    scene aminewone20
    with dissolve

    a "Yeah...I guess it does sound kinda weird when I think of that happening with any other couple."

    scene aminewone21
    with dissolve

    a "But you and me are different, I think."
    a "I think that we look like the type of couple who could do pretty much anything normal couples do."
    a "Because even if we might seem mismatched on the outside at first...the way we feel about each other shines brighter than a sea of diamonds and cuts through the outside entirely."
    a "I think that anyone who takes a look at us...a {i}real{/i} look and not just a quick one...I think that anyone who does that will understand that what we have isn’t that abnormal at all."
    s "..."
    a "..."
    s "And I think you’re insane."

    scene aminewone22
    with dissolve

    a "Hahahah! Maybe I am!"

    scene aminewone23
    with dissolve

    a "But I know that if I were to change...and if I were to stop being as annoying as you say I am...that you’d change too."
    a "And that’s the last thing I want."
    a "I love you exactly the way you are, Sensei. Flaws and all."
    a "And I’m happy you came here with me today."

    scene aminewone24
    with dissolve

    a "Even if we didn’t manage to get the couple's discount."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene aminewone25
    with dissolve2

    ay "Say {i}aaaaahhh...{/i}my sweet, little princess."
    m "How dare you take advantage of my one and only weakness like this. You will rue the day, Ayane."

    scene aminewone26
    with dissolve

    ay "You say that, and yet I’ve already fed you an entire parfait. Don’t pretend you’re not enjoying this, Maya. Because if you weren’t, you wouldn’t keep opening your mouth for me."
    m "Please don’t say such revolting things while there is food on the table."
    ay "You really think it’s revolting?"

    scene aminewone27
    with dissolve

    m "Well..."
    m "Maybe not as revolting as it {i}could{/i} be..."
    ay "..."
    m "..."
    ay "When do you think he’ll remember it’s her birthday?"
    m "Hopefully soon. I even flat-out reminded him the other day."
    ay "Oh? When did that happen?"
    m "When he decided to be annoying and stop by the shrine for literally no reason other than to bother me."
    ay "..."
    m "I don’t get it at all. What do you two even see in him? He has literally zero good qualities."
    ay "Probably the same thing you do."

    scene aminewone28
    with dissolve

    m "Huh? Me?"
    m "Are you confusing me with someone else? Because I do everything I possibly can to stay {i}away{/i} from him."
    ay "I guess I’m confusing you with someone else then."
    m "..."
    ay "..."

    scene aminewone29
    with dissolve

    m "He’s not..."
    m "He’s not going to remember at all, is he?"
    ay "..."
    m "..."
    ay "There’s always next year."

    scene black
    with dissolve2

    "We stay at the cafe for a little over an hour before we decide to head home."
    "And, in case you were wondering, I did wind up eating the parfait."
    "It was just okay."

    $ renpy.end_replay()
    $ ami_love += 1
    $ aminew1 = True
    stop music fadeout 6.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label aminew2:
    scene lr_day
    with pixellate

    "Somewhere between my room and the next, I am reminded of what it is like to be alone."
    "I am not sure who it is that is carrying the intangible bucket of plaster, but I would greatly appreciate it if they would allow my thoughts to exist, even if only for a moment, while I wake myself back into reality."

    play sound "static.mp3"
    scene warble1 with flash
    scene lr_day with flash
    stop sound

    "I am going to spend the morning with my niece because she is cute and I love her."
    "And even if we are related, it does not prevent us from pressing our genitals up against one another and moving them around until it feels good."

    play sound "static.mp3"
    scene warble1 with flash
    scene lr_day with flash
    stop sound
    play music "normalday.mp3"

    "There are all types of things you can rub your genitals against to feel good."
    "But there are also all types of things you can rub your genitals against and get in trouble for."
    "Bed sheets? Okay!"
    "The soft fur of a cat? Bad!"
    "The inside of the faucet in your tub? Okay! But dangerous!"
    "The closed eyelids of a sleeping woman on the bus? Bad! Go to jail!"

    play sound "static.mp3"
    scene warble1 with flash
    scene lr_day with flash
    stop sound

    "I think for another moment about all of the things in this house that I want to rub my genitals against and my niece comes out on top of the list without much competition."
    "At least for the time being. "
    "If you were to fill the home with the other {s}characters{/s} girls I normally see on a daily basis, I’m not sure if Ami would be the first one to receive my hard, throbbing AFFECTION."
    "The best course of action would be to remove at least one appendage from everyone I know and sew them together into the world’s greatest sex toy."

    play sound "laugh1.mp3"

    s "The only problem is I don’t know how to sew!"

    "Laughter erupts from behind the counter as there is a group of people I pay to be there at all times when Ami isn’t around."

    play sound "static.mp3"
    scene warble1 with flash
    scene lr_day with flash
    stop sound

    "But Ami is around. She is inside of her bedroom. So why is the gallery of laughter laughing now when their laughs aren’t meant to be laughed until laughter? I mean later. Not alughter. Laughter*"
    "Fuck."

    play sound "laugh2.mp3"

    s "Today is really going to be one of those days, isn’t it?..."

    scene black
    stop music
    play sound "dooropen.mp3"

    "I say goodbye to my live studio audience and exit stage right to make my way into Ami’s room. "
    "But what I find there isn’t Ami at all."

    play sound "pop.mp3"
    scene warble2

    "It is everything I have ever wanted and more."

    play music "warblewarblewarble.mp3"

    "Now, I know what you’re thinking."
    "It {i}should{/i} be okay to rub your penis against the closed eyelids of a sleeping woman on the bus in this world because she isn’t actually a real woman."
    "She is a character in a video game that I have somehow found myself inside of. "
    "A game where the capabilities are about as limited as the amount of fingers on the hard stub of flesh at the end of your arm."
    "Limited by me and no one else. Limited by me because despite this world being one that is entirely mine and no one else’s, I still manage to do what is right sometimes."
    "Sure, I do plenty of things that are wrong as well, but I have yet to fiercely penetrate any unwilling vagina that has presented itself before me because, for some reason, I want to play this game correctly."
    "Perhaps it is because I think I will be rewarded for all of the good I do when it finally comes time for it to end."
    "Or perhaps it is because the sensation of an unwilling, dry flesh opening just isn’t anywhere close to the one that is ready to get fucked and covered in DIY girl juice."

    a1 "Congratulations! You have made it to one of many landmarks in the fantastic journey that is Lessons in Love!"
    a2 "Yes! Yes! And the fact that you have not yet closed the application means that you are ready to accept the word of our Father!"
    a1 "Praise be!"
    a2 "Praise be!"

    "Two strange figures cloaked in black-"
    "Actually, they’re not really cloaked in black at all. They just {i}are{/i} black. But like, literally the color black and not the race. "
    "I have to tell you this instead of letting your eyes do the work because your eyes are bad and I do not trust them."

    s "Where Ami."
    a1 "Away! Away she goes in preparation!"
    a2 "Sad day! So very sad!"
    s "Bring Ami back so I can touch her."

    "The two figures hiss at me, probably because they don’t think it would be right for an uncle to touch his niece or something like that."

    scene warble3
    with fade

    "I move closer to give them a piece of my mind."

    s "The marsh warbler lives off of a diet of insects and also occasionally eats things like spiders and snails."
    s "While most of its diet is plucked from vegetation, it sometimes snatches bugs out of thin air or off the ground when it is feeling less acrobatic."
    s "It is a medium sized warbler who mimics the calls of many other birds, hoping to lure them into its general vicinity so it can use its narrow, pointed beak to prod at their respective cloacae."
    s "There are estimated to be between 10 and 27 million marsh warblers in existence. Their eggs are not normally eaten by humans, but they could be if a human decided to eat them."

    "I wind up giving them an incorrect piece of mind, which is actually even better for me because it means that they will now be incapable of completing the puzzle that is my very existence."

    a1 "So many bird facts!"
    a2 "Warble warble warble!"

    "The figure on the right begins to gyrate different parts of his body at different intervals, creating a sort of jiggling effect that reminds me a little bit of Jell-O and causes me to get hungry."

    scene black
    with dissolve2

    "I take a step back and try to jiggle myself, but I wind up just wiggling my penis around and looking like a complete fool."
    "I’m glad that Ami’s not here to see this..."
    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene warble4 with flash
    stop sound
    play music "10c.mp3"

    mo "I’m serious, though! I’m tired of wasting my friggin’ battle res on people who refuse to turn projected textures on! All it does is drag the rest of the group down!"
    r "Not everybody can afford the same setup you have, Molly. "
    r "I didn’t play for long, but there was one girl in my own guild who had to literally stare at the floor for this one fight because her PC just couldn’t handle the graphics on even the lowest settings."

    scene warble5
    with dissolve

    mo "Well, maybe it’s time for that girl to find another hobby because it’s casuals like that who are ruining the game for the rest of us who actually {i}care{/i}."
    r "Wack. You’re always so inclusive when it comes to people getting into the same stuff we’re into. What makes World of Warcraft any different?"

    scene warble6
    with dissolve

    mo "It just is, okay? I can’t really explain it."
    mo "Anyway, I’m sorry for going on a rant like that. It’s just that nobody in my class ever understands what I’m talking about, so you two must now feel the brunt of my fury."
    a "I don’t really mind. I haven’t played that game, but it’s kinda fun hearing you get really into things that you’re passionate about. "
    a "I...kinda needed that today."

    scene warble7
    with dissolve

    r "Hey! Appreciate me too, please! I’m the one who called out of work on like, zero notice to come out with you this morning! All Molly had to do was wake up!"
    mo "You say that as if “waking up” is an easy thing to do."
    a "I appreciate {i}both{/i} of you. And I’m sorry for asking you to hang out this early. "

    scene warble8
    with dissolve

    a "It’s just that...Well, Ayane and Maya worry a little too much about me during times like this and..."
    a "I’m sure Sensei will be dealing with it in his own way as well. So I didn’t want to...bother him any more than I already do basically every day ever."
    r "Dude, no worries. Besides, it gave us an opportunity to plan out our costumes and shit like, {i}way{/i} before we actually need them. So we all benefited from this and not just you."
    a "I guess that’s...a good way of looking at it."

    scene warble9
    with dissolve

    mo "AAAAAAAHHHHHHH!!!!!"
    r "Molly, it’s like 7:00 AM. Why are you screaming?"
    mo "Because I want to be in the same class as you two! I want to be with people who need me and appreciate me and don’t think I am just some loser chuuni weeb!"
    r "That is...literally what you are, though."

    scene warble10
    with dissolve

    mo "And proud of it!"
    r "{i}Are you really, though?...{/i}"
    a "Maybe you could talk to Sensei about it? I don’t really think he’d say no to you joining our class."
    a "He’s actually a really good teacher in...a really weird sort of way."

    scene warble11
    with dissolve

    r "He’s also hot in a...really weird sort of way."
    a "Hey."
    mo "I...have seen him around before and...wouldn’t disagree with that statement."
    a "{i}Hey.{/i}"

    scene warble12
    with dissolve

    r "Not gonna lie, Ami. Your uncle could get it if he wanted."
    mo "He’s...rather large, though...isn’t he?"
    a "..."
    r "..."
    mo "..."

    scene warble13
    with hpunch

    a "Stop daydreaming about my uncle and continue saying things that will make me happy instead of just mad!"
    mo "..."
    r "I..."
    r "I mean, I’d invite you in on the action too. We’re friends, right?"
    mo "I think I watched a hentai like this once."
    a "Shut up! Shut up! Shut up! This really isn’t the day to be talking about that!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene warble14
    with flash
    stop sound
    play music "warblewarblewarble.mp3"

    "I talked to the black figures for so long that my legs grew weak and I couldn’t help but collapse onto the ground near a small pile of Ami’s discarded clothes."
    "After lifting them to both inspect them and take in her scent because I miss her so much, I wind up rubbing my genitals on them since they were also on the list from earlier."
    "It is not as pleasurable as flesh would be and causes me to get a few friction burns, but it is a wonderful use of my time as it allows me to feel whole again."
    "I just wish her house plant would stop watching me."

    plant7 "You’ve got a huge fucking cock, bro. Like, holy shit."
    s "Why didn’t you say anything the whole time I was jerking off into one of my niece’s socks?"
    plant7 "Bro, I was just in awe. It’s seriously fucking gigantic."
    plant7 "No wonder your niece fingers the shit out of herself like every single night."
    plant7 "Like...bro, if {i}I{/i} had a pussy, I’d be going to town on myself right now too. Holy fuck."
    s "Thank you. I guess it is kind of unfortunate that plants aren’t really able to masturbate."
    plant7 "Fucking {i}tell me about it,{/i} bro. I’m dry as a motherfucker up in here. Finna get wet if you know what I’m saying."
    s "I’m sorry, but I don’t think I do. Everyone is always talking about how old I am, so I’m probably just not up to date on young person slang."
    plant7 "Nah, bro. You ain’t that old. I’m guessing low 30’s tops. Young enough that I don’t really think any less of you for trying to get it in all those girls who hang around here."
    plant7 "Yo, what’s that blonde one’s name again?"
    s "Ayane. She is a good girl."
    plant7 "Ayo, she got dressed in here the other day...And {i}bro,{/i} I kid you not, she’s got the nicest fuckin’ pussy I have {i}ever{/i} seen. Top of the line shit right there."
    s "As a plant, I doubt you have seen very many of them."
    plant7 "Bro, I’d give my left tap root to germinate that shit. You feel me?"

    "I reach out and feel the plant. It feels like a plant."

    s "Yes."
    plant7 "So now what, man? Your niece ain’t here and you’re all fuckin’ naked and shit. Shouldn’t you just go back to sleep?"
    s "I’m not tired. I don’t want to go back to sleep."
    plant7 "Aight, man. You do you. I’m just sayin’ that if she comes home and finds your fuckin’ baby batter all over her socks, you’re gonna have some explaining to do."
    s "You are right. There is only one thing I can do at a time like this."

    "I pick up the sock and begin squeezing it to get the cum out, but I forget that it is a sock, so all of the cum is absorbed."

    s "Oh no."
    plant7 "Bro. Bro. Fuck. Okay, here’s what you’ve gotta do."
    s "I have made a horrible mistake."
    plant7 "No, bro, it’s okay. You’ve just gotta bury the sock inside of me."
    s "But what if you get pregnant? I can’t afford to take care of a sapling."
    plant7 "Bro, don’t worry. You think this is the first time you’ve buried a cum sock inside of me? I guarantee you there are at least like five more down there right now."
    s "Are you sure it is okay?"
    plant7 "Bro, {i}yes.{/i} Socks disappear all the fucking time. Where the hell you think they go?"
    s "I’ve never really thought about it."
    plant7 "Good. Stop thinking altogether."
    plant7 "Erase your mind and wipe the residual cum from a bad decision off of your hands. Life goes on."
    plant7 "Bury the fucking sock, bro."
    s "Okay. But only because I trust you."

    scene black
    with dissolve2

    "I slide my fingers into the dirt."
    "It gets inside of my fingernails and reminds me of something I don’t like very much."
    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene warble15 with flash
    stop sound
    play music "10c.mp3"

    a "Thanks again for meeting up with me so early, you two. I’ll make it up to you at the next manga club meeting."
    mo "Your debt matters not, moonchild! For it falls upon the party to lighten the burden of its leader."
    r "As the president of the manga club, wouldn’t {i}you{/i} be the leader, Molly?"
    mo "I am the leader of the {i}guild.{/i} Ami is the one who formed today’s party."
    mo "What we did here today was no different from carrying her through Ragefire Chasm a few times."
    r "Is that another WoW thing?"
    mo "Guh. You are so lucky I can’t vote to kick in real life."

    scene warble16
    with dissolve

    a "{i}Hmm...hmmm...hmmmm~{/i}"
    a "I wonder if I should bother making breakfast today?"
    a "I’m not really hungry and Sensei will probably be asleep for another hour or two, so..."
    a "Mmmm...yeah. I’ll make it anyway. And if he’s not hungry when he wakes up, we can just eat it for dinner or something."

    play sound "dooropen.mp3"
    scene black
    with dissolve2

    a "{i}I’m home...{/i}"

    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene warble17
    with flash
    stop sound
    play music "warblewarblewarble.mp3"

    s "..."
    q "..."
    s "..."
    q "..."
    s "Who are you?"
    q "..."
    s "Can you speak?"
    q "..."
    s "What is your favorite bug?"
    q "..."
    s "The marsh warbler lives off of a diet of insects and also occasionally eats things like spiders and snails."
    s "While most of its diet is plucked from vegetation, it sometimes snatches bugs out of thin air or off the ground when it is feeling less acrobatic."
    s "It is a medium sized warbler who mimics the calls of many other birds, hoping to lure them into its general vicinity so it can use its narrow, pointed beak to prod at their respective cloacae."
    s "There are estimated to be between 10 and 27 million marsh warblers in existence. Their eggs are not normally eaten by humans, but they could be if a human decided to eat them."
    q "..."
    s "..."

    "This is pointless."
    "No one ever cares that I am a marsh warbler."
    "No one ever cares that I am not the real me."
    "I am just a player in a game."
    "A game with both limited and unlimited possibilities, that will never truly end until I have decided that I have either won or lost."
    "I have so much more to do."
    "So many birds I have to be."
    "So many cloacae I need to poke at with my beak."
    "And yet I stand here under a vent blasting out cold air and shrinking my scrotum, remembering what it is like to be alone."
    "Being surrounded by familiar faces means absolutely nothing when all of those faces are warped into the shapes I most want them to resemble."
    "This combination of cloth standing before me is the closest I have come to feeling whole since this life began."
    "I can not win."
    "I can only lose."
    "I feel like I am going to be sick."
    "I want to wear the dress and look at myself in the mirror."
    "I want to feel it again."
    "I want to feel it again."

    stop music
    scene black

    "I want to feel it again."
    "I want to feel it again."
    "I want to fall in love."

    play sound "static.mp3"
    scene warble18 with flash
    stop sound

    a "..."
    s "I want to feel it again."
    s "I want to feel it again."
    s "I want to feel it again."
    s "I want to feel it again."
    s "I want to feel it again."


    scene black
    with dissolve2
    play sound "dooropen.mp3"

    a "Sensei...I'm home..."

    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene maggotgod1 with flash
    scene maggotgod2 with flash
    scene maggotgod1 with flash
    scene maggotgod2 with flash
    scene warble19 with flash
    stop sound
    play music "beyondthewayoftime.mp3"

    s "I want to feel it again. I want to feel it again. I want to feel it again. I want to feel it again. I want to feel it again."
    a "Sensei...I said I’m home."
    s "..."
    a "Are..."
    a "Are you okay?"
    a "Are you tired?"
    a "Can you stand up?...Or do you need me to help you?"
    s "I want to feel it again."
    s "I want to feel it again."
    s "I want to feel it again."

    scene warble20
    with dissolve

    a "Did you have a bad dream?"
    s "..."
    a "Are you...{i}still{/i} having a bad dream?"
    s "..."

    scene warble21
    with dissolve

    a "Come on..."
    a "Let’s get you back to bed..."
    s "..."

    scene black
    with dissolve2

    "I cannot see what flowers are at my feet,\n
    Nor what soft incense hangs upon the boughs,"

    "But, in embalmed darkness, guess each sweet\n
    Wherewith the seasonable month endows"

    "The grass, the thicket, and the fruit-tree wild;\n
    White hawthorn, and the pastoral eglantine;"

    "Fast fading violets cover'd up in leaves;\n
    And mid-May's eldest child,"

    "The coming musk-rose, full of dewy wine,\n
    The murmurous haunt of flies on summer eves."

    "..."

    "Do I wake or sleep?"

    "........."
    "......"
    "..."

    scene warble22
    with dissolve2

    a "Come on...we’re almost there."
    s "I want to feel it again. I want to feel it again. I want to feel it again."
    a "I know."
    a "Today is hard for me too."
    a "But you’ll feel better soon."
    a "I’ve got you."

    scene warble23
    with dissolve

    s "Ami?..."
    a "Mhm. I’m right here."
    a "Just keep walking, okay?"
    a "Only a few more steps to go."
    s "..."

    scene warble24
    with dissolve

    a "{i}Only a few more steps to go...{/i}"
    s "..."
    a "I’ve got you...{i}I’ve got you...{/i}"
    a "And I’ll always protect you...okay?"
    a "No matter what."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene amiani1
    with dissolve2

    "My heart aches, and a drowsy numbness pains\n
    My sense, as though of hemlock I had drunk,"

    "Or emptied some dull opiate to the drains\n
    One minute past, and Lethe-wards had sunk:"

    "'Tis not through envy of thy happy lot,\n
    But being too happy in thine happiness,—"

    "That thou, light-winged Dryad of the trees\n
    In some melodious plot"

    "Of beechen green, and shadows numberless,\n
    Singest of summer in full-throated ease."

    a "Close your eyes, Sensei."
    a "When you wake up, I’ll be right here."
    a "And the two of us will go out together."
    a "The same way we’ve done so many times before."
    a "I’ll cry...and you’ll stand tall."
    a "And when tomorrow comes, it will be like none of this ever happened."
    a "We’ll forget together."
    a "We’ll survive together."
    a "We’ll grow together."

    scene amiani2
    with dissolve

    a "I love you so much."
    a "Now..."
    a "Sleep."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ aminew2 = True
    $ ami_love += 1

    jump day60

label amilust35skip:
    scene amisauna1
    with dissolve2
    play music "asobeatsex8.mp3"

    s "A sauna?..."
    a "Why do you sound so shocked?"
    s "I just didn’t realize there was one of these here. Especially one that’s in pretty decent condition considering all of the trees collapsed on top of it."
    a "No one else knows about it, so I figured it would be the best place for the two of us to spend time away from everyone else."
    s "Do we really-"
    a "You said you would do this to make up for disappearing. It’s only fair if you follow through."
    s "Yes, but {i}how long{/i} do you intend to stay in here? Because we run the risk of bumping into someone in the baths the moment we get out."
    a "What would happen then, Sensei?"
    a "What if we {i}did{/i} bump into somebody in the baths?"
    a "Would you look at them differently from how you look at me? Would they {i}tempt{/i} you?"
    s "Ami-"
    a "Are you okay with teenage girls so long as you’re not {i}related{/i} to them? Is that what makes it wrong?"
    s "Don’t do this right-"
    a "This is the best time to do it. "
    a "We’re alone. No one can hear us. {i}No one can see us.{/i}"
    a "And, I’m going to be blunt, I will have sex with you {i}right now{/i} if you’re okay with it."
    s "But I’m {i}not.{/i}"
    a "Why?"
    s "Because you’re my niece."
    a "So?"
    s "Ami, I’m supposed to protect you."
    a "Can lovers not protect one another?"
    s "It wouldn’t work."
    a "You don’t know that."
    s "Yeah, and neither do you. So go back to poorly hiding your feelings so I can hang onto the last shred of dignity I have left. "
    a "The {i}last{/i} shred? So you {i}are{/i} okay with other girls? It’s my {i}blood{/i} that’s the problem?"
    s "If that’s how you want to word it, sure. It’s your blood."
    a "Then boy, do I have bad news for you. "
    s "What is that supposed to mean?"
    a "Fuck me and I’ll tell you."
    a "I’ll slip the answer to every question you could ever have in between moans...whisper them into your ears in between pleas for you to do me harder."
    a "You have no idea what you’re missing, Sensei. I can be everything you’ve ever wanted. The perfect disposal for all of that lust and rage."
    a "I’m a doll. So do your thing and just play with me already, okay?"
    s "..."
    a "..."
    a "I love you, Sensei."
    s "And I-"
    a "It’s not the same."
    a "The kind of love I have for you is- well, let’s just say I’m thankful for swimsuits being waterproof."
    s "..."
    a "I’m not going to hide it anymore."
    s "You have to."
    a "I don’t {i}have{/i} to do anything you tell me to do. I just normally {i}want{/i} to."
    a "But I’m done being an accepting and loving niece who is just {i}okay{/i} with her uncle not reciprocating her feelings."
    a "Now, I’m going to remind you of what you’re missing every single chance I get. "
    a "Until it torments you...and you wind up jerking off underneath your blanket while I press my ear to the wall and fuck myself while listening."
    a "Because even if you won’t have sex with me, I know you {i}want{/i} to. And I’m always just one room away."
    s "..."
    a "I hope the temptation drives you insane."
    a "I hope you feel what I do."

    scene black
    with dissolve2

    "Ami and I sit in silence for the next hour. "
    "She never takes her eyes off of me. "
    "I spend the whole time wondering if the path I’ve chosen is correct."
    "..."
    "I don’t think it is."

    stop music

    "{i}WARNING: You are playing Lessons in Love incorrectly. Please start a new game and have sex with Ami Arakawa immediately. Failure to do so may result in unexpected errors, game crashes, or worse.{/i}"
    "{i}If you are disturbed by the idea of incest or are worried about the prospect of inbreeding, don’t be! It is okay. Ami Arakawa will love your children regardless of how they are born.{/i}"
    "{i}And she’ll love you regardless of whether or not you put your penis inside of her.{/i}"
    "{i}It would just be in everyone’s best interest if you actually did.{/i}"

    play music "strawberry.mp3"
    scene theend
    $ renpy.pause(60, hard=True)
    $ renpy.end_replay()
    $ amilust35skip = True

    jump beachmas13

label amilust35intro:
    scene amisauna1
    with dissolve2
    play music "asobeatsex8.mp3"

    s "A sauna?..."
    a "Mhm! This place has been here for a while. Nobody knows about it but me, though."
    s "Oh, good. That’s not suspicious at all."
    a "It’s not like I’m keeping it a secret! Just no one’s really gone out of their way to look or...go exploring or anything."
    a "But you know about it now too! Which makes it {i}our{/i} secret. "
    s "We already have a secret. And it’s one much bigger than this, might I add."
    a "Mmm...I’m not sure if you understand the definition of “secret,” Sensei. "
    s "..."
    a "A secret is a thing that you keep hidden from people. Something you don’t go around talking about."
    s "..."
    a "..."

    "She didn’t..."

    a "Why’d you tell Ayane? "
    s "I had to. She-"

    scene amisauna2
    with dissolve

    a "Oh, I’m not mad! So don’t worry about that. If anything, I’m actually really happy! And excited!"
    a "The fact that Ayane knows means I don’t have to hide it from her anymore. And that you were comfortable enough to open up to her about how our love really isn’t that weird!"
    s "I mean...it kind of {i}is{/i} though, Ami. There’s a reason people don’t go around widely celebrating incest."
    a "Nodoka does."
    s "Nodoka is not a role model."
    a "But she’s the smartest girl in class. So clearly there’s something {i}she’s{/i} getting that not everybody else is yet."
    s "I’m...obviously on your side here. But just because Ayane knows doesn’t mean that {i}everyone{/i} can know. This can’t be a thing that gets out."

    scene amisauna3
    with dissolve

    a "So...what you’re saying is I can’t tell anybody else about it yet?"
    s "You can’t tell anyone about it ever."
    a "But you {i}can?{/i} How is that fair? There are two halves of this relationship, you know. I should have some kind of freedom to talk about us too if I know you are."
    s "Ayane was a special case. She-"
    a "Why is she special?"
    a "Because you’ve known her a really long time?"
    a "Or because you’re having sex with {i}her{/i} too?"
    s "..."
    a "..."

    scene amisauna4
    with dissolve

    a "Kidding! Of course you’d never have sex with Ayane when you have someone like me, right?"

    play sound "static.mp3"
    scene amisauna5 with flash
    stop sound

    a "Right?"
    s "..."
    a "Because Ayane is everything I am, but worse. "
    a "You like red hair. My hair is red."
    a "You like tiny girls. I’m tiny."
    a "You like how the blood that gets your dick hard matches the blood inside of my body. "
    a "You like me. You like everything about me. So there’s no reason to ever waste any of that energy on Ayane...right?"
    s "..."
    a "..."

    scene amisauna6
    with dissolve

    a "Right?..."

    play sound "static.mp3"
    scene karate5 with flash
    scene newfallen24 with flash
    scene ayanefirst13 with flash
    scene nevermind22 with flash
    scene ayanecantbone14 with flash
    scene endofthefourth23 with flash
    scene amisauna6 with flash
    stop sound

    s "What if..."
    s "What if I said I was?"

    scene amisauna7
    with dissolve2

    a "Then..."
    a "I’d...say you’re joking."
    s "And if I wasn’t?"
    a "I wouldn’t believe you."
    s "So then what does what I have to say even matter when you’re going to reject the possibility of me ever having feelings for anyone but you?"

    scene amisauna8
    with dissolve

    a "It helps me feel validated."
    a "Like all of the horrible things I went through by your side weren’t just stepping stones you had to take to get to somebody else."
    a "I am the only thing you will ever need. And if everyone else vanished from your life right now, there would be no hole left that I could not fill myself."

    play sound "static.mp3"
    scene amisauna9 with flash
    stop sound

    a "But of course you know that already! I mean, why else would you have told Ayane? Why else would you still fuck me all the time? And eat my dinners? And pat my head? And {i}fuck me{/i} all the time?"

    scene amisauna10
    with dissolve

    a "Wow. We really do it a lot, don’t we? I wonder if high sex drives run in the family? "
    s "Ami-"
    a "There’s no way Ayane could ever keep up with me even if you {i}were{/i} having sex with her. Which you’re not. I’m like a...machine! A machine meant to crumble every time her uncle’s cock comes out!"
    a "Isn’t it great having someone who can keep up with you, Sensei? Somebody you could fuck a hundred times a day if you wanted to?!"
    s "That’s...not a realistic-"

    play sound "static.mp3"
    scene amisauna11
    with flash
    stop sound

    a "But it {i}can{/i} be if you try hard enough. Even when you think you’ve run out of juice, your little girl can get it hard again. She knows everything you want. Everything you {i}need.{/i}"
    a "Hey, is it hot in here, or is just me? "
    s "No, it’s...definitely..."

    play sound "static.mp3"
    scene amisauna12
    with flash
    stop sound

    a "Oh God...I’m really..."
    a "{i}Hah...{/i}"

    "I’m not sure if it’s the air or...Ami’s unrelenting, somewhat violent obsessiveness that gets to me, but I find myself moving from worried to aroused in a matter of seconds."
    "And the fact that {b}MY ADORABLE NIECE{/b} is standing in front of me, dripping with sweat and flushed cherry red is only making me feel...more..."

    scene amisauna13
    with dissolve

    a "Uhh...haha...hi..."
    a "What were we...talking about again?..."
    s "Something about...sex with Ayane?..."

    scene amisauna14
    with dissolve

    a "Not...allowed...and...not...necessary..."
    a "But if you really want to...get her involved...we can let her watch..."
    a "It...excites me just knowing...that somebody out there knows what we do..."
    a "If she could see...how far gone we are up close...hah...{i}Sensei...{/i}"

    "I can barely breathe in here...but that’s somehow a good thing."
    "The steam and heat are causing my vision to blur and my body to grow weak...and...and..."

    scene amisauna13
    with dissolve

    a "Sensei...aren’t you overheating...dressed like that?..."
    a "You should...take your clothes off..."
    a "All of them..."
    a "Right...now..."

    "It isn’t until Ami points it out that I realize I’m still fully clothed. And she’s right. I {i}should{/i} take everything off. Right now."

    scene amisauna14
    with dissolve

    a "Hah.......hah.......ahhh...."

    "My body is so hot and so covered in sweat that I can barely remove any of my clothing."
    "But I need to. If I wait any longer, I-"

    if ami_lust >= 35:
        jump amilust35
    else:
        stop music
        play sound "thump.mp3"
        scene black
        with hpunch

        a "Hah...oh God...I can’t.......huh?"
        a "Sensei?..."
        a "..."
        a "Sensei!!!"

        $ renpy.end_replay()
        $ amilust35skip = True

        "........."
        "......"
        "..."

        jump beachmas13

label amilust35:
    play sound "thump.mp3"
    scene black
    with hpunch

    a "{i}Hah!{/i} Let me...help you...with those...[amimaster]!"

    "Ami notices me struggling and pushes me to the ground, slipping her hands into my shirt and running them across my chest."
    "My head smacks against one of the benches and causes what little vision I currently have to blur even more. "
    "And even if this is an early stage on the way to falling unconscious, I can’t help but dive deeper into it as I begin to help Ami out of her clothes as well."

    a "Hah...oh God...do you see...just how much we...love each other?..."
    a "We can’t even...have a...serious conversation...without......aah!"

    scene amisauna15
    with dissolve2

    a "Mmph......mmngh...mlmm.......hnnn~"

    "I forget what we were talking about just moments ago."
    "It takes every bit of energy I have left to just raise my neck...but it’s something I feel like I have to do. Like it’s more important than staying conscious in the first place."
    "I place a hand on my niece’s ass, lowering her down to an angle where I’m able to easily brush her clit with the tip of my tongue, causing her body to shake and her teeth to lightly bite down on my cock."
    "I hope Ami is right...and I hope that this place really is hidden from everyone else. "
    "Because if any of the other girls were to walk in right now..."

    a "Mhm...mmm! I bet Ayane...could never do this...as good as I can..."
    a "I bet she doesn’t...mmnf...taste as good as me either..."
    a "Do you...hah...like it...[amimaster]?...My young...{i}smooth{/i} little pussy?...I bet you do..."
    a "You’re so hard...mmf! And you taste...amazing..."

    "The truth is that all I can taste is salt...the sweat dripping down her body and onto my tongue...sliding off her skin and onto my face..."
    "But it’s sensational — like I’m drowning in a sea of lust. "
    "And all it does is make my fight to survive more violent."

    scene amisauna16
    with dissolve

    a "Haaah! [amimaster]...you’re so...amazing...the best in the world...there’s no one...who could ever make me feel...even half as good as you do..."
    a "Keep me...all to yourself...forever and ever...hah...never.......never share me.....and never give....your big cock....to anyone but me!"

    scene amisauna17
    with dissolve

    a "Mmmmngh! Hmm...hm...mlm...hmmnch!"

    "Ami dives right back down and begins aggressively bobbing her head on my dick, opening as wide as she can while loosely jerking me off into her mouth."
    "I can tell that she’s trying to get me to cum before she does, but I know her body just as well as she knows mine. "
    "And I know that she’s only seconds away from losing herself completely and grinding against my mouth until she collapses on the floor."

    a "[amimaster]...slow...down! I can’t....mf...keep...mlm...up!"
    s "Go ahead...cum..."
    a "I want...to do it together!..."
    s "No...I want to cum inside you today..."

    scene amisauna18
    with dissolve

    a "Hah....hah!....{i}Inside-{/i}inside?...Not...inside...my mouth?..."
    s "You know what I mean..."
    a "Tell me! Tell me...you want to cum in your...little girl’s pussy!"
    s "...I want..."
    s "I want to cum...in your pussy..."
    a "Say it...like I did! Call me...your little girl!"
    s "I want to cum...in my little girl’s pussy..."

    scene amisauna19
    with dissolve

    a "Ohhh.....{i}god{/i} that’s good..."
    a "I love...hearing you...admit it...[amimaster]...that you’re just...as messed up as me..."

    scene amisauna20
    with dissolve

    a "Hah......hah....tell me...you’re gonna breed me..."
    s "I’m going to breed you..."
    a "Tell me...you’re gonna put a baby in me..."
    s "I’m..."
    s "I’m going to...put a baby in you..."

    scene amisauna21
    with dissolve

    a "Hah! Yeah...yeah...yeah! Right there, right there, right-"

    with sexfade
    with sexfade
    scene amisauna22
    with cumflash
    with hpunch

    a "NGGGGHH!!!!!!!!!!!!~~~~~~~"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene amisauna23
    with dissolve

    "Ami, still trembling from her orgasm just seconds ago, brings her body forward and lowers herself down onto my cock, letting me pick up right where I left off without even ten seconds of break time."
    "That said, I’m already close to cumming...but am equally close to passing out as I can barely even see at this point."
    "I close my eyes and focus only on the sensation. I’ve seen her body enough at this point that I’m able to imagine exactly how it looks."
    "The curves and contours of her developing frame...her pale skin and slender waistline..."
    "Everything from her red hair to her feet has been engraved into my eyes so deeply that I don’t even need to open them in order to see her anymore."
    "Were we talking about someone else earlier?..."
    "And if so, who was it?..."

    a "Ohhh...{i}yeah.{/i} Fuck me with that...big dick I love so much...[amimaster]..."
    a "Grab my hips...and slam me down...over and over and over and over..."
    a "Give me the baby you promised...give it to me..."
    a "I won’t...be able to hide that...you know?...Everyone...will know it’s yours..."
    a "It’s the perfect way...to tell them all...without having to speak a word..."
    a "Let them know...let them...{i}all{/i} know...just how special we are..."
    a "How you’ll never love anybody...or {i}fuck{/i} anybody...the same way you do with me!"

    scene amisauna24
    with dissolve

    a "HAAAAAaaaAAAaaaAAAaaahhh!!! Yes! Fuck......yes!"
    a "You’re a god, [amimaster]! You’re so good! So amazing! You fuck me so hard...I want to die! I’m gonna die!"
    a "Kill me! Kill me with your huge dick!"
    a "Wrap it around my insides! I can feel it splintering! Breaking off inside of me!"

    play sound "static.mp3"
    scene amisauna25 with flash
    stop sound

    a "I CAN FEEL THE LIGHT OF LAST SUMMER RE-ENTERING MY BODY THROUGH MY FLESH CREVICE"
    a "I CAN FEEL YOUR LOVE LIKE THE RAYS OF THE SUN AND SMELL THE BLOOM OF A BURNING SPRING"
    a "I CAN FEEL YOUR HEART THROUGH YOUR PHALLUS"
    a "I CAN FEEL THE BEATINGS YOU ENDURE"
    a "POUND ME WITH YOUR HARDEST, MOST VISIBLE TENDRIL UNTIL LIQUID KIN DRIPS FROM OUT OF MY BODY"

    "I keep doing the sex to Ami probably idk I might be unconscious now cause world is back. Black*"
    "Feels good though so that’s all that matters lol."

    play sound "static.mp3"
    scene amisauna23 with flash
    stop sound

    a "Hahahhha........I’m......getting dizzy......"
    a "Having...sex in a sauna...is amazing...but also...bad....because........haaah..."
    a "You’re close...right, [amimaster]?...I can feel it...but also...my feelings might be wrong because..."
    a "Breathing is.......not that.....hah.......easy......right....."

    "Time for liquid kin!"

    with sexfade
    with sexfade
    scene amisauna26 with cumflash
    with hpunch

    a "Haaah......aaah....ahh!"
    a "So........"
    a "So warm......."

    scene black
    with dissolve2

    a "So............"
    a "Bright............."

    stop music

    $ renpy.end_replay()
    $ amilust35 = True
    $ ami_lust += 1
    $ god_love += 1

    "{i}Ami’s lust has increased to [ami_lust]!{/i}"
    "........."
    "......"
    "..."

    jump beachmas13

label amimaid50:
    scene amilockerroom1
    with dissolve2
    play music "amiamiami.mp3"

    a "Ahh! Boy am I glad to be out of that stuffy maid outfit. Looking cute sure can be exhausting sometimes. "
    s "Ami, I don’t think I’m supposed to be in here."

    scene amilockerroom2
    with dissolve

    a "You can be wherever I want you to be! Plus, it’s not like you wandered in on your own. I dragged you in myself, which I am allowed to do since I work here!"
    a "It’s the exact type of situation we were shooting for when you decided I was allowed to work at the maid cafe!"
    s "I decided you were allowed to work at the maid cafe so you could make more money. {i}Not{/i} so you could strip down to your underwear in a locker room while everyone else is clothed and working."
    a "Huh. Guess I’m just misremembering then."

    "As you can see, Ami is mostly naked. Which means {i}I{/i} am mostly in danger."
    "But it’s not just because the only thing that gets her blood pumping is blood of a similar type and that she could very well attack me at any given moment-"
    "It’s because, as I just mentioned to her, {i}we are not alone.{/i}"
    "Unfortunately, her head is so empty that anything apart from compliments or words of affirmation goes in one ear, out the other, and then ultimately falls to its death on the floor."
    "But hey, on the bright side, she really {i}does{/i} seem to be on at least...{i}mostly{/i} good behavior today. And it’s not like she’s putting on an act about the whole “stuffy costume” thing."
    "I’ve never dressed in a maid outfit before, nor do I intend to, but just being in {i}these{/i} clothes in this weather is enough to make me start questioning my decision to go out today."
    "Damn the sun and damn my love for maids."

    scene amilockerroom3
    with dissolve

    a "You know, even if we don’t see eye to eye on why you let me get a job here, I’ve gotta say that life has gotten pretty interesting ever since then-"
    a "Which is super great since being stuck inside of that house all the time was starting to get really boring."
    s "I want to stop you for a second there and just throw out the fact that you can’t just say we don’t see eye to eye on {i}my reasons for doing things.{/i} Only I know what I think."

    scene amilockerroom4
    with dissolve

    a "But what if I have super awesome mind-reading powers like Anya Forger and just never told you about them?"
    s "That would certainly explain a lot of things, for sure. But I know it can’t be true based on the fact that you haven’t stabbed any of your classmates yet."

    scene amilockerroom5
    with dissolve

    a "Stabbed?! Why would I stab any of them?! Do I really look like the stabbing type to you? With these scrawny arms? You know me better than that."
    s "I know you very well. Which means I also know how...{i}protective{/i} you are over me."

    play sound "static.mp3"
    scene norikotime23 with flash
    scene amilockerroom6 with flash
    stop sound

    s "And by “protective” I mean terrifyingly attached to the point where it is almost intimidating."
    s "And by “almost” I mean it can be very intimidating."
    a "I mean...sure. I get it. But that still doesn’t mean I’d {i}hurt{/i} anybody. Ayane’s been in love with you forever and I haven’t stabbed her yet."
    s "Good. Continue not doing that for the rest of forever and we won’t have a problem."

    scene amilockerroom7
    with dissolve

    a "Hey, is something going on? You seem a little weird today. "
    s "As the only one fully clothed in this room, I beg to differ."

    scene amilockerroom8
    with dissolve

    a "Technically, it isn’t weird to be undressed in a locker room. So you can go ahead and get naked too if that makes you feel better, Sensei. It’s only natural."
    s "I’m good. It’s risky enough being in here like this...and I doubt I’d be able to talk myself out of anyone walking in if I wasn’t wearing anything."

    if amifingered == True:
        a "So don’t talk your way out of it! No harm in Uta-chan or Osako-chan knowing how much you love your niece."
        s "There is when the way I love you transcends the way I’m {i}supposed{/i} to."
        a "Nuh-uh. You love me {i}exactly{/i} how you’re supposed to. And anyone who has a problem with that just doesn’t understand."
        a "To be honest, if you {i}didn’t{/i} love me the right way after all this time, I’d probably go insane! So be happy that you do!"
        s "Wow, awesome. That’s so reassuring. Thanks, Ami."

        scene amilockerroom14
        with dissolve

    else:
        a "You could always grow a backbone and just have sex with me already. {i}Then{/i} you wouldn’t have anything to hide at all."
        s "Please don’t do that."
        a "Do what? Remind you that I want you to fuck my tight, virgin pussy while I wrap my legs around your waist and dig my nails into your back? Doesn’t that sound hot?"

        scene amilockerroom9
        with dissolve

        s "..."
        a "Just you and me...and whoever else decides to walk in. But of course, they’d be forced to watch since you’d never even think about giving any of {i}our{/i} DNA to somebody else, right?"
        s "You need to stop."

        scene amilockerroom10
        with dissolve

        a "No."
        s "Ami-"
        a "Why would I stop? I’m in the midst of puberty and have so many feelings I need help understanding. If only there was {i}someone{/i} who could help me learn."
        a "Preferably someone who’s familiar with my body so I know I’d be in good hands. And is also related to me and has glasses and is named Sensei. "

        scene amilockerroom11
        with dissolve

        a "Basically, you should fuck me or I am going to go crazy. Like, for real."
        s "..."
        a "Like...{i}for real.{/i}"
        s "..."

        stop music
        scene amilockerroom13

        a "Like, for real."
        a "I’m going fucking insane."
        s "..."
        a "..."

        play sound "static.mp3"
        scene amilockerroom14 with flash
        stop sound
        play music "amiamiami.mp3"

    a "Anyway, regardless of how risky you think this is, I don’t see it as a bad idea at all."
    s "Yeah, of course {i}you{/i} don’t. I’m 99%% sure the only reason you became a maid in the first place was because you knew I had a thing for them."
    a "Sounds pretty considerate if I do say so myself. Which I do because I am very considerate and am always putting {i}your{/i} needs ahead of mine."

    scene amilockerroom15
    with dissolve

    a "This really was a nice change, though. "
    a "I didn’t realize just how much I’d enjoy it until I started working here."
    a "Now, I don’t know if I’ll ever be able to stop. "
    a "I might just stay a maid for the rest of eternity."
    a "Do you think I could live like that, Sensei?"
    s "I think you might reach a point age-wise where it isn’t really feasible anymore. But hey, follow your dreams and all that. "

    scene amilockerroom16
    with dissolve
    play sound "dooropen.mp3"

    s "And if you’re lucky, you might even grow into a new uniform one day."
    a "Now, that was just plain rude."
    u "And in here you’ll find-"

    scene amilockerroom17
    with fade

    u "Something that is...totally not safe for work..."
    c "Uhh..."
    a "Oh, hey! Don’t mind me. It was just a little too hot in the uniform, so I decided to take it off for my break since Sensei was cool with it. Right, Sensei?"
    s "I had nothing to do with this."
    a "See? This is totally normal for him. It doesn’t even register as inappropriate."
    a "Anyway, did you guys need something? Because you’re kind of interrupting our conversation right now."

    scene amilockerroom18
    with dissolve

    c "Uhh...Uta was giving me a tour of the place since I’ve been thinking about coming to work here. "
    a "You probably shouldn’t bother. It’s a lot of really hard work and we have enough employees already."

    scene amilockerroom19
    with fade

    c "Yeah, I can decide for myself...but thanks for the heads up."
    u "So, uhh...this probably wasn’t the most {i}normal{/i} thing to walk into, but I swear that nothing like this has ever happened before and, if it {i}has,{/i} I totally don’t know about it."

    scene amilockerroom20
    with dissolve

    c "It’s whatever. I’m not even surprised given that she drags him into dressing rooms with her as well. Besides, it’s not like Sensei thinks anything of it. Just look at him."
    u "I don’t know, Chika. It might not be official, but Ami’s held the number one spot in the Sensei love ranking ever since it was established."

    scene amilockerroom21
    with dissolve

    c "Wait, {i}Ami{/i} is number one?! And I’m only in the top five?! Are you fucking kidding me?!"
    u "I...I see you’re already familiar with the ranking! That’s good! "
    c "How much did she pay you for that spot?! I’ll pay double!"
    s "Chika, you’re poor. {i}And also shouldn’t be fighting for this right now.{/i}"

    scene amilockerroom22
    with dissolve

    c "Oh. Uh...yeah. I mean, it’s just a stupid ranking after all. I don’t even need to be on it or whatever. Plus, it’s, like...not even official."
    u "R...Right! "
    u "So, umm...anyway, this is the locker room. And when Ami isn’t busy trying to get weird with her uncle, it’s where we stash our stuff and change into our uniforms and whatnot."
    u "If you {i}do{/i} decide that this might be the place for you, you’ll get a locker along the wall and-"

    scene amilockerroom23
    with dissolve

    a "And that’s it! Locker room tour over! Bye, guys! Sensei and I were talking about important family business and, I don’t want to be rude, but you’re {i}kind of{/i} still in the way."
    c "Oh. Sorry, Ami. I’m used to important family conversations being held with clothes {i}on.{/i} I didn’t realize it was different for other families."
    a "That’s fine. I understand. Bye."
    u "Huh. My family didn’t have many talks like that, but I’m pretty sure we would’ve kept our clothes on too. But hey, different strokes for different folks, I guess."
    c "Ugh, whatever. Let’s just go."
    u "Wait! Don’t you want to try on the uniform first?! I have an extra! And if it sounds like I’m excited to see you in it, it’s probably just because I really like maids!"
    a "That would be a bad idea since Sensei is in here and it would be like, totally weird for a teenager he’s {i}not{/i} related to to get undressed in front of him."
    c "Right, yeah. And it’s not weird at all for his niece to do that."
    a "Exactly."
    c "Do you seriously just not understand sarcasm at all?"
    a "Guess not. See you in school, Chika! "

    play sound "dooropen.mp3"

    c "Whatever. Come on, Uta."
    u "Wait! Noooooo!"
    s "..."
    a "The nerve of some people. Not realizing when they should both knock {i}and{/i} mind their own business. We’re {i}clearly{/i} in the middle of something here."
    s "..."

    scene amilockerroom24
    with dissolve

    a "..."
    s "..."
    a "What? Why are you looking at me like that?"
    s "There was no reason for you to act that way toward them, Ami. "
    s "It would be one thing for Uta since the two of you see each other all the time and she can just laugh it off...But Chika doesn’t know you that well. And you don’t want {i}her{/i} to be your enemy."
    a "Why would she be my enemy? All I did was ask for some alone time with my uncle. If she takes that the wrong way, that’s on her."
    a "This might be the locker room, but it’s also the {i}break{/i} room. And I’m on break right now, which means I shouldn’t have to worry about work-related stuff."
    s "You just could have been a little nicer. That’s all I’m saying."

    scene amilockerroom25
    with dissolve

    a "Mm...you’re right. Maybe I {i}was{/i} a little too pushy just now?..."
    a "I should probably go and apologize..."
    s "You should probably get dressed first. Because as happy as the {i}customers{/i} might be to see a maid in her underwear, I can’t imagine your coworkers would feel the same."
    a "I can’t imagine I’d {i}have{/i} any coworkers after pulling a stunt like that. "
    a "I’ll just apologize whenever I see Chika next. I don’t have anything against her. In fact, I kinda look up to her in a bunch of ways."

    scene amilockerroom26
    with dissolve

    a "She’s gorgeous...and cool...and popular...and can pull off, like...any outfit ever. {i}Plus,{/i} she’s smart and has really nice boobs that I am only kind of jealous of. "
    a "And by “kind of” I mean I want her boobs."
    a "Or any boobs."
    a "But alas...Ami is a washboard..."
    s "I’m not going to weigh in on the whole apologizing thing since this doesn’t {i}really{/i} have to do with me, but I’m glad to hear you’re considering it."

    scene amilockerroom27
    with dissolve

    a "Of course. I’m one of the good guys. "
    a "But you’re wrong about this not having anything to do with you. "
    a "I thought it was pretty clear Chika was jealous back there. And that’s probably why I acted the way I did. I doubt I would have snapped if it was someone who {i}didn’t{/i} like the same person as me."
    s "Have you ever considered maybe...not caring about how other girls feel about me? People can’t help who they fall for. You shouldn’t resent them for that."

    scene amilockerroom28
    with dissolve

    a "I don’t resent anybody. Like I said, I admire Chika. "
    a "I just get a little irked when I think about the two of you together and go into protective mode. But it’s not like that’s a {i}new{/i} thing."
    a "I just want you to be safe. That’s all."
    s "And you don’t think I’d be safe with Chika?"
    a "Right."
    s "Why?"
    a "Because she’s a teenager."
    s "And you’re not?"
    a "I’m different. I’m your niece. We live together. If you lived with Chika, it would raise some eyebrows."
    s "So when Chika graduates high school- "
    s "Actually, when {i}all{/i} of the girls graduate high school, you’ll be okay with me dating them?"

    scene amilockerroom29
    with dissolve

    a "Hmm..."
    s "..."
    a "..."
    s "Are you actually thinking about it?"
    a "Of course. You asked me a serious question, so it’s my responsibility to give you a serious answer."

    scene amilockerroom28
    with dissolve

    a "And that serious answer is no. "
    a "I won’t ever be okay with you dating anyone other than me because I am the one you love the most and we are meant to be together. The end."
    a "You almost got me, though. "
    s "I wasn’t trying to {i}get{/i} you, Ami. I was trying to help you understand that I can be safe with other people. It doesn’t have to be you."
    a "What are you talking about? Of course it does."
    s "No, it doesn’t. And to be honest, you’ve been getting way too clingy lately. Which is crazy since you were already clingy to start with."

    scene amilockerroom30
    with dissolve
    stop music fadeout 5.0

    a "Huh?..."
    s "I’m serious. You need to start letting me breathe."
    s "I love you. But my world doesn’t revolve around you."
    a "Yes it does..."
    a "I do everything for you. You’d...be nowhere without me. "
    a "You’d have no clean clothes and live off of instant noodles. The trash would pile up and the house would start smelling weird."
    a "You’d have to warm the bath all by yourself and you always complain when you have to do that. And that’s not even counting all of the times you’ve asked for help with-"
    s "How can I get better at {i}anything{/i} if you’re always just...going to do everything {i}for{/i} me?"
    a "...What?"
    a "Why would you need to get better? "
    a "Who told you that you need to get better?"
    s "No one. "
    s "I just...do."
    a "But...no."
    a "No."
    a "You’re already...the best you can be. "
    a "You don’t need to grow any more."
    a "You’ve done enough."
    s "I haven’t."
    s "And I’d appreciate it if you’d stop suffocating me."
    a "..."
    s "..."

    scene amilockerroom31
    with dissolve

    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."
    a "..."
    s "..."

    scene black

    a "No."

    $ renpy.end_replay()
    $ amimaid50 = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........"
    "......"
    "..."

    jump saturdayafternoon

label amiinvite4:
    stop music
    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene happy1 with flash
    scene happy3 with flash
    scene happy1 with flash
    scene happy2 with flash
    scene amimakesyoudinner1 with flash
    stop sound
    play music "comfort.mp3"

    "I love my niece."
    "She’s the only thing I’ll ever need."
    "When I’m with her, I feel happy. And when I’m {i}not{/i} with her, I can’t stop thinking about her."
    "It doesn’t matter if she wants me all to herself. Or that she fights away anyone else who wants to see me."
    "She’s doing it all for good reason — because she needs me in order to function."
    "It’s the same way I feel about her."
    "If that’s not true love, I don’t know what is."
    "She’s such a good girl."
    "If she cut her finger slicing carrots, I would put it in my mouth and suck on it until the blood clotted."
    "If I watched her empty rat poison into my supper, I would still eat it because I know she’d never do anything to hurt me and that it’s probably just for flavor."
    "You have no idea how much I love my niece."
    "You have no idea how much she loves me."
    "No one can and no one ever will."
    "The Ami scene will begin now."

    a "What do you think you’re doing?! I told you I don’t need any help!"
    s "Who says I’m helping and not just standing around? This is my house and I’m allowed to stand wherever I want."
    a "It’s my house too, mister. And if I say you’re getting in the way, it means you’re getting in the way!"
    s "Are you trying to tell me you don’t care about my company anymore?"

    scene amimakesyoudinner2
    with dissolve

    a "{i}No.{/i} I’m trying to tell you that tonight’s dinner is a surprise and that you’re going to ruin it if you keep watching me. "
    s "It’s not much of a surprise if you’re going to be waving the cookbook around in front of my face like that."

    scene amimakesyoudinner3
    with dissolve

    a "Hey! Stop looking and go sit down! I’m doing this for {i}you,{/i} you big meanie!"
    s "You’re absolutely {i}sure{/i} you don’t want any help? I know I’m normally useless, but I can at least mix stuff if I try hard enough."
    s "And surprises aren’t really my thing in general, so if that’s what’s keeping you from-"

    scene amimakesyoudinner4
    with dissolve

    a "I’m fine. I’m sure you had a long day and that you want to relax now. There’s no need for you to interfere with {i}my{/i} job when I never interfere with yours."
    s "To be fair, I’m not so sure your intellect would {i}allow{/i} you to effectively interfere with my job. Leave things like that to Makoto."

    scene amimakesyoudinner2
    with dissolve

    a "You shut your mouth or I really {i}will{/i} pour rat poison into your dinner."

    scene black
    with dissolve2

    "I love my niece."
    "She reminds me a lot of someone else I used to know."
    "It’s someone I try not to think about because it hurts when I do."
    "But it hurts even more to not think about her."
    "Damned either way, I blank everything out and take a seat at the living room table."
    "I eagerly await the dinner my wonderful niece is making me."
    "I’m sure it will be delicious because she understands the things I like and the textures and the colors and the food and the food and niece and did I mention I love her?"
    "I love her so much."
    "My niece, I mean."
    "Not the other person I mentioned a moment ago because she isn’t real and you can’t love what isn’t real and oh look Ami is back."

    play sound "static.mp3"
    scene amimakesyoudinner5 with flash
    stop sound

    s "Curry?"
    a "And lots of it. Good thing we bought that second rice pot, right?"
    s "Ami, this is too much food."
    a "Then we’ll have leftovers. Who cares? Curry is always better on the second day anyway. "
    s "Fair enough. Is this really so special that I had to step away from the kitchen, though? Anyone can make curry."
    a "This isn’t just any curry, Sensei. It’s Ami’s special curry — made with real Ami. "
    s "Real Ami?"
    a "It’s full of my blood. I used it in place of salt. I hope you like it."
    s "As long as it’s not rat poison."

    "I spoon a spoonful of curry into my spoon and then spoon it into my mouth. I can’t even taste the blood."
    "Ami’s special curry is way better than anything you can buy from the store and I’m glad she made it for me tonight."

    s "I love your blood."

    scene amimakesyoudinner6
    with dissolve

    a "Thanks! I love it too."
    a "I was just kidding, though. This is normal curry without any Ami in it. But I’m glad to know you would have eaten it if there was!"
    s "If there is no Ami in the curry how can it be called Ami’s special curry?"

    scene amimakesyoudinner7
    with dissolve

    a "It’s special because it’s rare! "
    a "I’ve only made it a few times since I started high school. Which means you should savor it since you have {i}no idea{/i} when the next time you’ll get any is."
    s "Probably the next time I ask. I can’t imagine a world where you’d ever say no to something I want."

    scene amimakesyoudinner8
    with dissolve

    a "Nuh-uh. There are plenty of things I’d say no to. You just don’t normally ask for any of them because you love me so much. Right, Sensei?"
    s "Yes."

    "I love my niece so much that I am not opposed to consuming her bodily fluids when she uses them to cook."
    "I am also not opposed to consuming her and if she shrunk herself down to the size of a pill I would take her with a glass of water, swallow her, and allow her to expand in size inside of me."
    "You have no idea how much I love my niece."

    a "Thank you, thank you. "
    a "It’s always so much fun whenever you think out loud. You don’t share your feelings enough and hearing them straight from the source is like heroin for me!"
    a "But of course, I say that as a good girl who has never done and never {i}will{/i} do drugs. Because the only drug I need is you."

    "Awwwwww."

    a "Teehee!"
    a "You’re lucky I don’t take {i}real{/i} advantage of you when you’re like this, Sensei. It would be so easy."
    s "Like what? What am I doing wrong?"

    scene amimakesyoudinner9
    with dissolve

    a "You’re not doing anything {i}wrong.{/i} You’re just probably not doing what you think you’re doing."
    a "There’s a disconnect between your mind and what’s actually happening that makes things seem normal to you when they’re not like, {i}actually{/i} normal."
    a "It’s a coping thingy."
    a "For example, you’re totally naked right now and you probably didn’t even realize."

    "I look down and confirm that I am, in fact, naked. "
    "Whoopsie."

    s "That’s so weird. Most of my thoughts are entirely coherent right now. "
    s "There have been plenty of times where I’ve blacked out, but this is kind of like a halfway point where I’m still {i}sentient.{/i} "
    s "How curious."
    a "It’s probably because of what I mentioned earlier."
    s "What did you mention earlier?"
    a "My parents."

    stop music
    scene amimakesyoudinner10
    play sound "glass.mp3"

    s "..."
    a "I said something in passing about how you’ve slipped into the dad role perfectly and I guess your brain just kinda kicked itself into self-defense mode."
    a "It’s my fault for letting it slip. I understand by now that this can happen since the same thing happens to me sometimes."
    a "It’s true, though. And there’s no harm in saying that now since you’re already like this."
    a "I don’t want to say you’re more of a dad to me than my real dad ever was, but I definitely like you more."

    play sound "static.mp3"
    scene amimakesyoudinner11 with flash
    stop sound
    play music "hometown.mp3"

    a "Granted, I was always more of a mama’s girl in the first place. "
    a "I didn’t {i}dislike{/i} my dad or anything. He was totally...normal. "
    a "But next to Mom, he just..."
    s "..."
    a "..."
    a "No one could ever look good next to her. It wasn’t his fault."
    a "She was beautiful. Creative. Funny. Smart. "
    a "And the way she treated me..."
    a "It was like nothing else mattered to her."
    s "..."
    a "..."

    scene amimakesyoudinner12
    with dissolve

    a "Sorry. I know I’m getting emotional when we haven’t even started eating yet, but..."
    a "Honestly, my mind’s been kind of all over the place lately."
    a "What with those standardized test thingies and...with Maya and Ayane starting to...treat me like I’m some kind of..."

    scene amimakesyoudinner13
    with dissolve

    a "Never mind. We don’t have to get into that right now. I’m more interested in hearing what {i}you{/i} have to say about my parents."
    a "You miss them too, right?"
    s "..."
    a "..."
    a "Of course you do...How could you not when you were hit just as hard by their passing as me?"
    a "But it’s fine. Well...no. It’s not fine. Nothing like that can ever {i}be{/i} fine."
    a "But they’re in a better place now. Or at least I hope they are."
    a "I know Mom never believed in God."
    a "She pretended to around me because it was the “right” thing to do, but even when I was little, I could tell she was just going along with it for my sake."
    s "..."
    a "You feel the same as her, don’t you?"
    a "That there is no afterlife. Or reincarnation. Or...anything at all."
    s "..."
    a "I don’t like that."
    a "I can’t stand the idea of the two of them just...covered in dirt for the rest of forever. "
    a "I want them to go somewhere else. And I want to go somewhere else when {i}I{/i} die too."
    s "..."
    a "..."
    a "I know you loved her, Sensei."

    scene amimakesyoudinner14
    with dissolve

    a "And I’m not just saying that because {i}everybody{/i} loved her. I know she was important to you in a way my dad never was."
    a "And even if you and him never saw eye to eye on stuff, I know you must at least {i}kind of{/i} miss him too."
    a "But he’d be proud of you if he could see you now. And so would my mom."
    a "You’re doing an amazing job. We both are."

    scene amimakesyoudinner15
    with dissolve

    a "Which is why I’m going to try harder to be like her."
    a "To be someone everyone loves and admires. But, more importantly than that..."
    a "To be someone {i}you{/i} love and admire. Because what you think matters more to me than every other thought in every other world squished into one giant ball."
    s "You don’t want that."

    scene amimakesyoudinner16
    with dissolve

    a "Huh?"
    s "You don’t..."
    s "Want...to..."
    a "..."
    s "Don’t..."
    a "Why not? Why would I {i}not{/i} aspire to be someone that important to you? And don’t go saying it’s because you already love me a lot since we both know you can always love me {i}more.{/i}"

    "I reach into the back of my mind, unsure of whether or not I’ll be able to latch onto anything and, if I {i}do{/i}, if Ami will be able to catch a glimpse of it."
    "She’s seen almost everything so far. The things I thought were private wound up not being private at all. "
    "I do not know the shape I’m in or the state of my mind. But as someone so accustomed to seeing me this way and at least {i}attempting{/i} to fix me up, I hope she’ll understand."
    "Goodbye thoughts of blood...dismembered carrots. "
    "Goodbye colors, textures, wan’dring rabbits."
    "{size=-3}In this desperate plea for a voice to speak I clap my hands and stomp my feet but it’s not a tantrum I repeat I’m doing this because I’m weak my throat is hoarse from lack of sleep and this run on sentence hurts to read but-{/size}"
    "I can not punctuate something that is meant to look broken. "
    "And I can not place a period in a sentence that is never meant to end."
    "All I can do is split myself open and hope that some of my guts spill onto Ami."
    "She’s chasing after something she doesn’t want to find."
    "And should she ever spot a period...or another ending mark-"
    "I pray she just ignores it."
    "Thus begins another arc."

    s "She..."
    a "..."
    s "You..."

    scene amimakesyoudinner17
    with dissolve

    a "Uhh...l...let’s move on! "
    a "We should talk more about how...uhh..."

    scene amimakesyoudinner18
    with dissolve

    a "Uhh..."
    a "Um..."

    scene amimakesyoudinner19
    with dissolve

    a "Right! Maya and Ayane have been really mean to me lately! Do you want to hear more about that?"

    stop music
    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene amimakesyoudinner20 with flash
    stop sound
    play music "normalday.mp3"

    s "Sure."
    a "..."
    s "..."
    a "..."
    s "Are you crying?"

    scene amimakesyoudinner21
    with dissolve

    a "What do you mean “Am I crying?!” Things just got really intense and sad all of a sudden and now you’re just going back to normal?! What the heck?!"
    s "What are you talking about? And why am I naked?"

    stop music
    scene amimakesyoudinner22 with hpunch
    play sound "thump.mp3"

    a "You’re naked because you have a problem! And only I know how to take care of it! Okay?!"
    s "A problem? Are you talking about-"
    a "Maya and Ayane are trying to get rid of me!"
    s "What?"
    s "What do you mean they’re trying to get rid of you?"

    scene amimakesyoudinner23
    with dissolve
    play music "hometown.mp3"

    a "I mean they’ve been hanging out without me and...excluding me from stuff and...it’s kind of like they don’t want to be my friends anymore."
    a "It’s been really, really hurtful. "
    a "I’m just happy I have you still...I know you’d never leave me..."
    s "They’re not trying to get rid of you, Ami. The two of them are just...going through something that you wouldn’t really understand."
    a "Try me. I’m not as dumb as I look. Or act."
    s "I’ve been given specific instructions to not do that."
    a "So it {i}is{/i} a secret after all..."
    s "I’m sorry. I just can’t-"

    stop music

    a "Does it have something to do with “the end of the world?”"
    s "..."
    a "..."
    s "How do you-"
    a "Makoto texted me about it."
    a "Something about the world being a...loopy thing? She used a bunch of big words I didn’t really get."
    s "I see..."

    "I guess no one told Makoto to keep Ami out of this."
    "But, then again, I don’t really understand why we were supposed to in the first place, so..."

    a "Would you mind explaining what all of this is about, Sensei?"
    s "..."
    a "..."
    s "Fine."

    scene amimakesyoudinner24
    with dissolve

    s "Your first year of high school is never going to end."
    s "You and everyone else are caught in a timeloop that causes it to start over every few months."
    s "You retain most of your memories and progress in relationships, but certain information is conveniently omitted from what you carry on from one iteration to the next."
    s "And seeing as you haven’t interjected yet, I should also inform you that if you try to talk about this to anyone else, that they’ll continuously interrupt you until you change topics."
    s "Also, everybody disappears, the sky turns red, and pregnancy is probably not the cause. "
    a "..."
    s "..."
    a "..."
    s "..."
    a "Sensei..."
    s "...Yeah?"

    scene amimakesyoudinner25
    with dissolve
    play music "normalday.mp3"

    a "That is the dumbest thing I have ever heard."
    s "What?"
    a "Did you seriously think I was going to fall for that?"
    s "Ami, it’s not-"
    a "I know I said I’m not as dumb as I look, but to think you thought I was {i}that{/i} dumb? Come on! That’s insulting!"
    a "Also, somebody should {i}really{/i} give Makoto the memo that this is all just a prank because it {i}really{/i} seemed like she was taking this seriously. How can she be so smart and yet so gullible?"
    s "Ami-"

    scene amimakesyoudinner26
    with dissolve

    a "Just eat your dinner, Sensei. It’s getting cold."
    a "And stop believing everything Maya tells you. She reads too many weird manga and they’re clearly going to her head."
    s "It’s not just her. It’s-"
    a "And stop believing everything Maya tells you. She reads too many weird manga and they’re clearly going to her head."
    s "Ami, listen...I have seen-"
    a "And stop believing everything Maya tells you. She reads too many weird manga and they’re clearly going to her head."
    s "..."
    a "..."

    scene black
    with dissolve2

    s "Curry? "
    s "You never make curry."
    a "It’s Ami’s special curry! Made with real Ami."
    s "I’m suddenly not hungry anymore."

    $ renpy.end_replay()
    $ amiinvite4 = True
    $ ami_love += 1
    stop music fadeout 7.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label amispecial50:
    scene clearnightsky
    with dissolve2

    if _in_replay:
        play music "undersea.mp3"

    "I have a history of chasing my tail but a track record clean of having ever caught it."
    "What this means is that when something larger and scarier than me {i}does{/i} appear and ultimately scoop me up with its endless, half-transparent arms that I will not yet be accustomed to how it feels to be held."
    "There are many things in life I do not understand."
    "Like dust particles. Or the romanticization of death. Or even myself at times as this jar I’m trapped inside reflects not the me that {i}I{/i} see but the one that {i}you{/i} do."
    "Yet, what sleeps inside it is a mystery to all of us."
    "When I was younger and the ring still fit my ankle, I worried not of what it meant to die but simply that of dying."
    "But as my bones expanded, my worries flipped and now I think the opposite."
    "At this stage in my life, it is not the act of dying that keeps me up at night, but the fear of what comes after."
    "My hands grace the glass of my infinite jar, staring back at someone I can only view as the protagonist of this story while the only thing that {i}truly{/i} matters is the glass itself."
    "If that shatters, what comes next?"
    "How will the creature (Me) inside of it (The jar) appear to the untrained eye when filled with shards of my former home and other assorted shrapnel and foreign objects?"
    "For even if my breathing were to continue after such a tragic event, I’d not be seen as who I am but who I {i}was.{/i}"
    "There is no moral to this untimely, rhetorical passing- but I don’t think there needs to be."
    "So long as you can imagine what it feels like walking mile after mile in these shoes filled with tacks, my words will have worked."
    "So long as you can relate, it will have all been worth it."
    "That’s likely what I’d think as the light drains from my eyes."
    "I lied about the lying. Things {i}have{/i} been looking up."
    "Feelings are good and I am supposed to have them."
    "There’s nothing I need to fix because the world will fix it for me. All I have to do is live my life and smile and forget but also accept the things I forgot and couldn’t accept but that’s hard when my brain is a brain and-"
    "Slow down."
    "Deep breaths."
    "Expel your worries from the depths of your lungs."
    "You are you."
    "I am me."
    "And neither one of us knows which is which and when."
    "Warble, warble, warble."

    play sound "phonering.mp3"

    "My phone goes off roughly thirteen feet from the next streetlight."
    "I make sure to stand beneath it when I answer."

    play sound "phonebeep.wav"
    stop music

    s "Hel-"

    with hpunch

    a "{size=+20}{b}SENSEI!!!!!!!{/b}{/size}"
    s "Ami?...What’s wrong?"

    play music "itsingsinitssleep.mp3"

    a "Everything! Everything is wrong!"
    s "Slow down. Start from the-"
    a "I don’t know where I am!"
    s "How can you not know where you are? You weren’t kidnapped, were you?"
    a "No, you idiot! I came here myself! But I don’t know how to get back and I’m too scared to move!"
    s "Have you tried your GPS-"
    a "Of course! Stop thinking I’m such an idiot! It’s just not working and it won’t tell me where I am and I need you to come get me!"
    s "But how am I supposed to do that if you don’t know where you are? Kumon-mi is huge. I need a hint or...{i}something{/i} at the very least."
    a "I’m...uhh..."
    a "I think this is...the old district?"
    a "No, I’m sure it is. That’s where I am. But I don’t know how to leave and I’m too scared to even walk right now. My legs are shaking so much. Can you please come help me? Please?"
    s "What are you even doing all the way over there?"
    a "I don’t know! I was just doing what I was told!"
    s "By who? Who would ask you to go all the way over there and why would you listen to them in the-"
    with hpunch
    a "{size=+15}{b}ARE YOU COMING OR NOT?!{/b}{/size}"

    "Her voice sounds different than normal, and not just because it’s panicked."
    "It’s like her mouth was stuffed with worms and all of the worms are screaming at the same time but when they open their worm-mouths more worms come out and basically it just sounds like worms."
    "This is a job for the worm-man."

    s "Yeah, I’ll head over now. Just try and figure out where you are in the meantime, okay?"

    "I’m glad my worms still come out normal despite being the word-man."
    "Wait, no. I got that backwards."
    "Hold on. I will fix."

    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene happy5 with flash
    scene happy4 with flash
    scene happy3 with flash
    scene amibus1 with flash
    stop sound

    "The only way to bring life back to normal is with a bus ride backwards."
    "It’s a poem again, but a lack of rhyming words has forced in blackbirds."
    "But birds are all I talk about, so let’s try discussing...placards?"
    "No! That’s not exciting either! Here! Just take the fucking password!"

    play sound "static.mp3"
    scene lostinaplace1 with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene amibus1 with flash
    stop sound

    a "Do you believe in God?"
    s "Of course. How else would we have gotten here?"
    a "How do you think He feels when we defy Him?"
    s "Technically speaking, God would likely be genderless. God is an entity who exists on a plane so far detached from human life that merely comparing It to us is disrespectful."
    a "But weren’t we all created in His image?"
    s "{i}Its{/i} image. And I think not."
    s "I think God is so wonderful that looking at It would blind us. It is so bright and so powerful that we can not even comprehend It."
    a "Is Mom with God now?"

    play sound "static.mp3"
    scene lostinaplace2 with flash
    stop sound

    "{i}She is.{/i}"

    se "Jeez, you’re really going through it tonight, aren’t you?"
    se "Any reason why? Something I can help with?"
    s "Why?..."
    se "Why what?"
    s "{i}Why do I keep seeing you?{/i}"

    play sound "static.mp3"
    scene lostinaplace3 with flash
    stop sound

    se "Because you’re lucky."
    se "Not everybody gets regular chances to spend time with their dead girlfriend, you know. You should be savoring moments like these."

    play sound "static.mp3"
    scene lostinaplace4 with flash
    stop sound

    s "How could I?!"
    se "Oh my. You {i}never{/i} raise your voice — especially at {i}me.{/i} You must feel pretty strongly about this."

    play sound "static.mp3"
    scene lostinaplace5 with flash
    stop sound

    se "Here, maybe this will cheer you up! You still like costumes, don’t you? There’s no way such a cute-"

    scene lostinaplace6
    with dissolve

    se "Actually, wait. Isn’t this costume kinda...half-assed?"

    scene lostinaplace7
    with dissolve

    se "Whatever! Screw it! Come at me with all you’ve got, big guy!"
    s "Leave..."
    s "Please..."

    scene lostinaplace8
    with dissolve

    se "Meow?"
    s "I don’t...want to see you anymore..."

    scene lostinaplace9
    with dissolve

    se "{i}Hissssssssssssss...{/i}"
    s "..."
    se "..."
    s "..."

    scene lostinaplace10
    with dissolve

    se "{i}Hah...{/i}fine. I’ll go back to my never-ending pool of darkness. Left to float there forever and ever and ever and ever, totally unfulfilled. "
    se "I always knew Heaven was a joke, but it would have been really cool if there was at least {i}something{/i} after death."

    scene lostinaplace11
    with dissolve

    se "Here’s the thing though, Aki-kun. You can’t just ignore me forever. Especially now that you’re literally {i}seeing{/i} me."
    se "Does this really look like moving on to you? All you’re doing is making things harder for yourself."
    s "Well, what else am I supposed to do?!"
    se "How should I know? I’m a cat. Meow."
    se "Whatever it is, though, you’re not going to find it here."
    s "Then where?..."
    s "Where will I find it?..."

    play sound "static.mp3"
    scene frown with flash
    scene anormaldoor with flash
    stop sound
    play sound "dooropen.mp3"

    se "{b}I think you already know that.{/b}"

    play sound "static.mp3"
    scene l with flash
    scene e with flash
    scene t with flash
    scene m with flash
    scene e with flash
    scene o with flash
    scene u with flash
    scene t with flash
    scene lostinaplace12 with flash
    stop sound

    a "Ah..."
    s "..."
    a "..."

    scene lostinaplace13
    with dissolve

    a "You found me..."
    a "And I didn’t even give you any hints..."
    s "Ami...what are you doing out here? It’s the middle of the night and we’re miles away from home. You know this place isn’t safe."

    scene lostinaplace14
    with dissolve

    a "I didn’t come here on my own, though! This wasn’t my idea!"
    s "Then whose idea was it?"
    a "Maya and Ayane’s!"
    s "...What?"

    scene lostinaplace15
    with dissolve

    a "They asked me to hang out tonight and told me to meet up with them here...but when I showed up, there was no one there."

    scene lostinaplace13
    with dissolve

    a "So I called them and they didn’t answer...."
    a "And when I looked at my GPS it wouldn’t work..."
    a "And I forgot where I was and couldn’t find my way back, so I got even {i}more{/i} lost! And then people were staring at me, so I got scared! And I still don’t know where they are and-"
    a "And why did they do this to me?! Weren’t they supposed to be my friends?!"
    s "I’m sure it’s just some sort of misunderstanding."
    a "It’s not! I tried to tell you the other day, but they’ve been all kinds of mean to me lately! "
    a "They’re bullying me! Leaving me out of things I’d always be included in! And neither of them is telling me why! So why?! Why are they doing this?!"
    s "Ami-"

    scene lostinaplace16
    with dissolve

    a "I just want my friends back!!!!!!!!! Waaaahhhhhhhhahahahh!!!!!!!"
    s "Give me a minute. I’ll call them and see what’s going on. I’m sure it’s-"
    s "It’s..."

    scene lostinaplace17
    with dissolve

    a "What’s wrong?..."
    s "..."
    s "My phone’s dead."
    a "Really?..."
    s "It was fine when I left Kaori’s apartment. I don’t get how-"
    a "What were you doing at Kaori’s apartment?"
    s "Does that really matter right now?"
    a "Were you having sex with her?"
    s "What? "

    if amifingered == True:
        a "Do you and Kaori have sex together? Are you going to leave me for her?"
        s "I don’t see how that’s relevant at all, but no. We don’t. And I’d appreciate it if you wouldn’t ask me questions like that anymore."
    else:
        a "Is that why you won’t have sex with me? Because you’re too busy having sex with Kaori?"
        a "Did you know she used to post pictures of herself on the Internet? I bet she’s had sex with lots of people. You shouldn’t do that kind of thing with her. It’s not safe."
        s "Kaori’s an...interesting character. But if you think {i}that’s{/i} the type of person she is, you’re way off."
        a "Did she tell you that? Is that how she got you to have sex with her?"
        s "Ami, I’ve never done anything like that with Kaori. And I’d appreciate it if you wouldn’t ask me questions like that anymore."

    a "I only ask things like that because I love you."
    s "Well, please love me in a less intrusive way."
    a "Do you think I’m a burden, Sensei?"
    a "Do you think Maya and Ayane are leaving me behind because I’m slowing them down? Or keeping them from doing the things they like?"
    a "You’re not going to do that too...are you? You’re not going to leave me?"
    s "I’m not going to leave you. You’re a part of me."
    a "Your organs are a part of you. And if one of them stops doing its job, it can kill you."
    a "So you can either get a new organ to replace the failing one or, in some cases, have it removed altogether."
    a "Is that what I am to you? An organ you can just give up? A body part you can just {i}cut off?{/i}"
    s "No...you’re not like that at all."
    a "So you’re saying you can’t live without me?"
    s "If that’s what makes you happy, sure."
    a "Say it."
    a "Say you can’t live without me."
    s "..."
    a "..."
    s "I can’t live without you."

    scene lostinaplace18
    with dissolve2

    a "..."
    s "..."
    a "Really?..."
    s "Of course..."
    a "..."
    s "..."
    a "I can’t live without you either."
    s "Yeah...I can see that."
    a "I, umm...I know you don’t like when I ask things like this, but...can you maybe...give me a piggyback ride home? I’m not sure how well my legs will work right now."
    s "You really can’t walk on your own?"
    a "I probably can, just...it’ll be really slow and I don’t want to annoy you. Plus, having a shoulder to dry my tears on would be a really big help."
    s "Then...fine. But only because you look pathetic right now and I feel kind of bad for you."

    scene black
    with dissolve2

    a "I’ll take what I can get..."

    "........."
    "......"
    "..."

    scene lostinaplace19
    with dissolve4

    a "Thank you, Sensei...I know you hate doing stuff like this."
    a "I hope I’m not too heavy."

    "Ami rests atop my shoulders and, just as the tongue of the accused did mere hours (or less) ago, steals away the unrest that I’ve been feeling."
    "It’s as if her body is a dam — and all of the worries in all of the world have once again been liquefied only to get caught up behind this brand new barrier."
    "I wonder if that’s why we’re in here."
    "Maybe it doesn’t have anything to do with the war at all."
    "Maybe the walls of Kumon-mi are {i}our{/i} dam, and the world outside of them is simply too full of horrible things to warrant letting any of them in."
    "While this thought softens the beat of my heart, I know it’s not a good thought to have. And I know it can’t be true."
    "Things aren’t always exactly as they seem. I’ve lost track of how many times I’ve had to tell you that."
    "But there are certain things I can’t help but feel like {i}are{/i} exactly as they seem."
    "The walls."
    "The sky. The moon. The earth."
    "But more importantly than all of that-"
    "How much I love my niece."
    "Just look at her."
    "Isn’t she the cutest?"
    "Isn’t she the cutest?"
    "Isn’t she the cutest?"

    play sound "static.mp3"
    scene lostinaplace2 with flash
    scene lostinaplace19 with flash
    stop sound

    "{i}She is.{/i}"

    a "Heheh..."
    a "This reminds me a lot of when I was younger..."
    s "Did you ride on my shoulders a lot like this back then?"
    a "Not really. "
    a "My dad would hold me like this when we were going on walks in the park, but that’s not really something I ever got to experience with you."

    play sound "static.mp3"
    scene lostinaplace20 with flash
    stop sound

    a "It would have been nice if I did. But that would also mean my parents would have been taken away earlier than they were and..."
    a "And..."
    a "B-But that didn’t mean I never fantasized about it! I always looked forward to seeing you when you came over! And I still think about, like...riding on your shoulders and stuff now."
    a "We just never had a chance to when we were finally put together."

    play sound "static.mp3"
    scene lostinaplace21 with flash
    stop sound

    a "But you’d still hold me tight sometimes..."
    a "And I’d fall asleep in your arms..."

    play sound "static.mp3"
    scene lostinaplace20 with flash
    stop sound

    a "But then it was right back to normal. "

    play sound "static.mp3"
    scene lostinaplace21 with flash
    stop sound

    a "But normal was never normal."

    play sound "static.mp3"
    scene lostinaplace20 with flash
    stop sound

    a "And it isn’t normal today either."

    play sound "static.mp3"
    scene lostinaplace22 with flash
    stop sound

    a "I tried to change things sometimes."
    a "I thought I knew what you wanted."

    play sound "static.mp3"
    scene lostinaplace20 with flash
    stop sound

    a "But I was a stupid little girl."

    play sound "static.mp3"
    scene lostinaplace21 with flash
    stop sound

    a "I didn’t understand what you wanted at all."

    play sound "static.mp3"
    scene lostinaplace19 with flash
    stop sound

    a "But now I do."
    a "Now, I know that all you really want is to feel safe."
    a "So I built a world where you could."
    a "I made our house into a home. I filled it to the brim with your favorite foods and activities. And all I’ve ever asked for in exchange for all of that is your attention."
    a "And I know it might seem like I ask for a little {i}too{/i} much attention sometimes. And I’m sorry for that. "
    a "I’m a very needy girl."
    a "And that’s why I’m so scared now. Because, sometimes...it feels like you’re trying to run away."
    a "How come?"
    a "Did what you want change?"
    a "Do I not understand you as much as I used to?"
    a "If there’s something I’m missing, tell me."
    a "I’d do anything for you, Sensei."
    a "And I mean {i}anything.{/i}"
    s "You do more than enough, Ami."
    s "But for now, I want to go home and sleep. So just stay put and try not to move around too much. It makes walking hard."
    a "Okay...I’m tired too."
    a "Besides, who needs friends anyway? All I’ve ever {i}really{/i} needed is you."
    a "And I’m sure you feel the same about me. Don’t you, Sensei?"
    s "Yeah, sure. Whatever."
    a "Say it with a little more sincerity, please. Repeat after me, “Ami is the ultimate niece-“"
    s "Ami is the ultimate niece..."
    a "“And the only one I’ll ever love.”"
    s "And...the only one I’ll ever love."

    play sound "static.mp3"
    scene lostinaplace23 with flash
    stop sound

    a "Heh..."

    scene lostinaplace24
    with dissolve2

    a "Heheheh..."

    scene lostinaplace25
    with dissolve2

    a "Hahah! Hahahahahaha! Hahaha!"
    s "What are you cracking up about up there?"

    play sound "static.mp3"
    scene clearnightsky with flash
    stop sound

    a "Hahahahahah! "
    a "It’s just...hahahahahahah! It's just so crazy how much I love you!"
    a "How are you {i}not{/i} laughing?! I’m so obsessed it’s kind of hilarious!"
    s "Yeah, well..."
    s "It’s a little {i}less{/i} funny when you’re the one being obsessed over..."
    a "Heheh...heh..."
    a "I don’t know about that, Sensei..."

    $ renpy.end_replay()
    $ amispecial50 = True
    $ ami_love += 1

    jump amispecial50mainp1

label amilust50intro:
    play sound "static.mp3"
    scene karaokeami1 with flash
    stop sound

    a "Actually! Never mind! I don’t feel like singing right now!"

    "My feelings are cut short when my amazing, beautiful, wonderful, loving, kind niece approaches me."

    a "Hey, Sensei! Since {i}I{/i} don’t feel like singing and {i}you{/i} don’t feel like talking, would you want to come with me for a minute and help me carry some stuff?"

    if ami_lust >= 50:
        "My lust level with Ami is high enough to trigger this event, so I take it upon myself to telepathically communicate to her that I am willing to proceed."
    else:
        "My lust level with Ami isn’t high enough to trigger this event, so I decide to just sit still and platonically stare at her gorgeous face instead. "

    ay "Hey, Ami! This was supposed to be a duet!"
    m "I wouldn’t mind helping you if-"
    a "That’s not necessary, Maya. I want Sensei to help me. His arms are bigger and stronger and he can hold more things than you."

    "It’s true. My arms are very big and strong. I bet I could break Ami’s legs if I tried hard enough, but there is no reason for me to do that so I won’t."

    a "So, what do you say? Will you come with me? "
    s "What do you need help carrying?"
    sa "Ah...he speaks..."
    a "I don’t know yet! But I guess we’ll find out soon!"
    a "Actually, come to think of it, maybe I don’t need to carry anything at all? Maybe I just want to speak to you in private for a minute about personal, {i}family{/i} matters!"
    m "You should have just opened with that."
    ay "Ami, you’re disrespecting your queen! Return to the microphone!"
    a "I’m not disrespecting her at all. I love Niki. So much that I think we should invite her into the Love Squad as well! Especially if we’re taking in people like Sana now. No offense, Sana."
    sa "Um...that’s...okay..."
    a "Sensei? A word? In {i}private?{/i}"

    menu:
        "Go with Ami" if ami_lust >= 50:
            s "Anything for you, Ami."

            scene karaokeami2
            with dissolve

            a "Yay! You must love me {i}so{/i} much! Way more than anyone else in this room!"
            ay "I would take offense to that if I was not already busy singing your parts!"
            s "You’re the best niece a man could ever want."
            m "Sensei-"

            scene karaokeami3
            with dissolve

            a "He already made a choice, Maya. What more could you possibly add to this? "
            m "Relax. I just wanted him to get me a drink."

            scene karaokeami2
            with dissolve

            a "Okay! I’ll make sure he does that! Just don’t come looking for us if we take a little too long, okay?!"

            "I crack my knuckles."
            "It’s time to put these strong, man arms to good use."

            jump amilust50

        "Stay here and party":
            s "I think I’d rather just stay here and party. I like this song and it’s nice and toasty in this room."

            play sound "static.mp3"
            scene karaokeami4 with flash
            stop sound

            a "And {i}I{/i} think that’s the wrong idea! You’re going to come with me whether you like it or not because, if you {i}don’t,{/i} you’re going to regret it for the rest of your life!"
            sa "That sounds...kind of serious for..."
            a "Shut your {i}fucking{/i} mouth, Sana. I know what you’re doing. You’re trying to take Sensei away from me. You’re just like everybody else. But Sensei is going to choose me. He always chooses me. Right, Sensei?"
            s "I don’t see you that way, Ami."
            a "Wrong answer again! Hahah!"
            ay "Ami! Apologize to Sana right now!"
            a "Sure! Right after she apologizes for seducing my uncle while I wasn’t around to gorge myself on the hot cum she squeezed out of his massive adult cock!"

            play sound "static.mp3"
            scene karaokeami5 with flash
            stop sound

            sa "Huh?!"
            a "Oh, don’t pretend you don’t know what I’m talking about. You’ve been in heat all summer long. It was only a matter of time until you couldn’t hold it in anymore, thirsty bitch."
            sa "I...um..."
            ay "Sana? That’s not true, is it?"
            sa "I...uhh..."

            scene karaokeami6
            with dissolve

            sa "Would you be willing to share?"

            $ renpy.end_replay()
            $ amilust50skip = True

            stop music
            scene colorbars
            play sound "colortone.mp3"
            $ renpy.pause(5, hard=True)
            jump halloweenfour15

label amilust50:
    stop music
    play sound "static.mp3"
    scene karaokeami7 with flash
    stop sound
    play sound "doorslam.mp3"
    with hpunch

    s "Hey, this looks just like the other room we were just in. And there are already a few songs queued up."
    s "Grab a mic, Ami. Let’s get this bread."
    a "I can smell her on you."

    play music "asobeatsexdark.mp3"

    s "What?"
    a "Sana."
    a "What did she do?"
    s "..."
    a "Did she {i}touch{/i} you?"
    s "..."
    a "How do you feel right now, Sensei?"
    a "Are you still “out of it?” "
    a "Are you still confusing girls for {i}other{/i} girls? "
    s "..."
    a "Did you mistakenly believe she was me? Is that what happened?"
    s "..."
    a "You know I’m the only girl who can take care of you, right?"
    a "You know we’re meant to be together, right?"
    a "You know I love you, right?"
    s "Of course."
    a "Then why do you keep letting others in? Is what I have not enough anymore? "
    a "Do I need to try something {i}different?{/i}"
    s "Different?"
    a "Look at me."
    s "..."
    a "Now."

    play sound "static.mp3"
    scene karaokeami8 with flash
    stop sound

    m "You’re seriously disgusting, you know. Men like you would be better off locking themselves in their rooms for the rest of their lives so that the rest of us can breathe a little easier."
    m "I swear, you’re like some sort of...pollutant. Something that makes the air toxic just by setting foot outside. It’s a miracle you can sleep at night knowing this."
    s "..."

    play sound "static.mp3"
    scene karaokeami9 with flash
    stop sound

    a "I wonder what that makes me, then?"
    a "An accomplice? Melatonin? The girl who needs to bear your burden so no one else has to? "

    scene karaokeami10
    with dissolve

    a "Or perhaps I’m just unlucky?"

    play sound "static.mp3"
    scene karaokeami11 with flash
    stop sound

    m "Perhaps I’m the most unlucky girl in the entire world...because I wound up falling for {i}you.{/i}"
    s "..."
    m "This is what you want to hear, right? For me to say those words to you after all this time? Did that make your heart skip a beat? Because it should, you know. I’m kind of a catch."
    s "What are you doing?..."

    play sound "static.mp3"
    scene karaokeami12 with flash
    stop sound

    a "Flirting, I think?"
    a "It’s been so long that I’ve kind of forgotten how. Though, I suppose there’s never been any need for me to learn as you’ve always just come to {i}me.{/i} Regardless of whether I want you to or not."
    a "Which I usually don’t. But it is what it is. "
    a "Fate can be so unkind at times, don’t you think? If only we were somewhere else. And if only there wasn’t a gap in our ages so large that you could pass as my grandfather."
    s "Ami-"

    play sound "static.mp3"
    scene karaokeami13 with flash
    stop sound

    m "{i}Ami?{/i} Are you seriously thinking about your {i}niece{/i} at a time like this? Just how despicable are you? "
    s "You’re not...this...this isn’t..."
    m "Isn’t what? Spit it out already. I don’t have all day to listen to you whine about your uncontrollable erection."
    s "..."

    scene karaokeami14
    with dissolve

    m "{i}Hah...{/i}Are we going to do this or not? Because if you absolutely {i}need{/i} to sneak away from the others to fuck me, I’d prefer you do it quickly. "
    m "Getting caught with {i}you{/i} is the last thing I’d ever want. For more than just the obvious reasons, of course. "

    "I no longer care who is real and who is make-believe."
    "All I want is a pair of arms to throw myself into."
    "And a tight hole in which I can ejaculate."

    play sound "static.mp3"
    scene karaokeami15 with flash
    stop sound

    m "Go on then. "
    m "Take it out."
    m "You don’t need me to get you started, do you? Because if you had the gall to throw me into this room before even {i}getting{/i} hard, I’m going to be both shocked and impressed at the same time."
    s "..."
    m "Pathetic. "
    m "Making me do all the work {i}again.{/i}"

    scene black
    with dissolve2

    m "I guess it can’t be helped, though..."
    m "Lay down, Sensei..."
    m "I’ll take good care of you."

    "........."
    "......"
    "..."

    scene karaokeami16
    with dissolve4

    a "Look at you — lost in ecstasy while a teenage girl plays with your cock. How cute."
    s "It’s...because it’s you..."
    a "Pfft, as if you actually expect me to believe that. We both know you’d do this with anyone that gives you the time of day. Pervert."
    s "I’m gonna cum...I’m gonna cum..."
    a "Already? Are you serious? I’ve barely even touched you. I told you to be quick, not {i}embarrassing.{/i} Bite your tongue or something. That’s supposed to help, isn’t it?"
    s "I...I don’t..."
    a "Want {i}me{/i} to bite it for you? "

    scene karaokeami17
    with dissolve

    a "Or would you rather shut my mouth in a {i}different{/i} way? Because I’m sure you’re tired of hearing me speak by now, aren’t you? "
    a "Unless you {i}enjoy{/i} being ridiculed by little girls, that is. Which, by the looks of it, you might. Disgusting."
    s "You’re disgusting too, Maya..."

    scene karaokeami18
    with dissolve

    a "Am I?"
    s "Your friends are...one room over...and you’re doing {i}this...{/i}"
    a "Only because I {i}have{/i} to. I was more than capable of waiting until we’re alone. But I was beginning to feel bad for you since I knew you wanted it so bad."
    s "You want it too...don’t lie to me..."
    a "Maybe I do. Maybe I don’t. Not like you have any chance of finding out so long as my pants are on."
    s "Take them off..."
    a "Then what? Let you cum inside of me the second you put it in? Not worth the effort, to be honest. Just finish here so we can go back to barely knowing each other."
    s "Maya...please..."
    a "Please what?"

    "She begins to speed up."

    s "Let me fuck you..."
    a "I love that look of {i}desperation{/i} you get in your eyes whenever I hold something you want over your head. It’s probably the only time you look attractive, if I’m being honest."
    s "I can’t...hold out much longer..."

    scene karaokeami19
    with dissolve

    a "Good. This angle is hurting my wrist and being this close to you for this long as is more draining than you think."
    s "Is that why...you’re crying?..."

    scene karaokeami20
    with dissolve

    a "I’m not crying."
    s "But-"
    a "Just fucking cum already. Jesus."

    "Her eyes lock onto mine and, for a brief moment, I imagine her as someone else."
    "But this is Maya. "
    "This is how we are. "
    "This is what we do."

    scene karaokeami21
    with dissolve

    a "Ahh...finally...here it comes...I can feel it..."
    s "Ah......hah......"
    a "Are you gonna cum for me?...Yeah?...How much?..."
    a "Do it...do it, do it, do it...{i}do it...{/i}"

    with sexfade
    with sexfade
    scene karaokeami22 with dissolve2

    a "Ah..."

    scene black
    with dissolve2

    a "That was barely anything..."
    a "How pathetic."
    s "Maya..."
    a "Shh..."
    a "That just means I know you have some more..."

    scene karaokeami23
    with dissolve2

    a "Hah! Hah! Hah! Nngh...fuck! I hate how...good you are at this...you fucking pervert!...Why can’t you...be useful for anything else?..."
    s "You...wanted it...Don’t lie..."
    a "Of course I...hah...wanted it, you...fucking idiot...I have...needs...just like you and...as much as I hate to admit it...your cock...can’t be beaten..."

    scene karaokeami24
    with dissolve

    a "Guess I should be thankful I...met somebody as...disgusting as you...shouldn’t I?...What a waste you’d be on...anyone else when...you’re the perfect fit for {i}me...{/i}"
    s "It...barely fits at all..."
    a "Just how...you like it...right?...Creep..."
    s "Maya...you’re amazing...you’re so amazing..."

    scene karaokeami25
    with dissolve2

    a "Hah...ahh...I know...I know I am...and...you’re not so...bad yourself when...aah...you’re not being...so gross...hah!"
    s "Quiet down...someone will hear you next door..."
    a "Hah!...Ngah! It’s...okay! They’re...too busy...singing! No one...will hear us! Just...keep fucking me!"
    s "And to think...a few minutes ago...you were saying this wasn’t worth the effort..."
    a "That was...aah...before you...came the first time! I think...ngah! It’s...pretty obvious...how much I want it now!"

    "My grip is tight around Maya’s waist, and she doesn’t even attempt to resist as I repeatedly push and pull at her body."
    "I can feel her juices trickling down my leg as her pussy clamps down on the first few inches of my cock. But I’m careful not to push any further as I don’t want to break her. "
    "It’s difficult holding myself back, but I’ve gotten used to it over the years."
    "I have plenty of practice by now."
    "So much, in fact, that I can already tell she’s about to cum."

    a "Aaah! Hah!...Aaah! Fuck! Like that! Just...like that!"
    s "Does that feel good, Maya?..."

    scene karaokeami26
    with fade

    a "So good...Sensei! So good! I feel like...I could die! I love your cock...so much! So much! Mess me up! Cum inside me!"
    s "Your voice...be careful..."

    scene karaokeami27
    with dissolve

    a "I already told you...no one’s going to hear us! And I...can’t help it! Aah! Sensei! You feel so good!"
    s "You’re a lot...cuter when...you’re submitting, you know..."

    scene karaokeami28
    with dissolve

    a "What was that, Sensei? I couldn’t hear you. Could you say it again please?"

    play sound "static.mp3"
    scene karaokeami29 with flash
    stop sound

    s "I said...you’re a lot cuter...when you’re submitting..."
    a "Ngh...mmf...I bet! It probably gets...really exhausting...hearing me {i}bitch{/i} all the time...doesn’t it? I bet that just...makes you want to fuck me...ten times harder...huh?"
    s "It sure does..."

    scene karaokeami30
    with dissolve
    play sound "dosex.mp3"

    a "Ah! Ah! Ah! Ah! Ah! Ah! Ah!"

    "I ramp up the pace and begin to catch up to Maya at the finish line. "
    "It’s been a long time since the two of us have raced, but it’s heartwarming to see she’s still willing to wait up for me when I want her to. And I didn’t even have to say anything."
    "That’s just what love is like, I guess."
    "You don’t always need to {i}do{/i} what the other person wants, so long as you understand one another and are willing to back each other up when push comes to shove."
    "Right now, this is one of those moments — and it’s not an unfamiliar one. Just partially chewed-up and slightly forgotten."
    "But that will all change soon. For this may be the last time I ever have sexual intercourse with {i}anyone-{/i} not just my niece’s best friend."

    scene black
    with dissolve2

    "In the disappearing of my dilapidated psyche, a final thought rushes in."
    "It’s that Maya smells a lot like Ami today."
    "She feels like her too."
    "And she sounds like her and breathes like her and-"

    a "Aah! [amimaster]! Aaah! Yes! Cum inside me! Cum inside me!"

    "And it happened again."

    stop music

    "I did a bad thing."

    $ renpy.end_replay()
    $ amilust50 = True
    $ ami_lust += 1

    "{i}Ami’s lust has increased to [ami_lust]!{/i}"
    "........."
    "......"
    "..."

    jump halloweenfour15

label amilust60intro:
    play sound "dooropen.mp3"
    scene anothercollector1
    with dissolve2

    a "Hi! Sorry I disappeared for so long, Sensei. A few of the girls decided to show up unannounced and I had to make sure they weren’t here to hurt you. "
    a "But, on the bright side, Niki and Noriko dropped by as well! And they left you a bunch of presents on the dining room table!"

    scene anothercollector2
    with dissolve

    a "I had to go through them to make sure there wasn’t anything dangerous inside, but I re-wrapped them pretty perfectly if I do say so myself. And I can help you open them later once we’re done with your checkup."

    scene anothercollector3
    with dissolve
    play music "painisreal.mp3"

    a "Oh! And since you haven’t been able to visit the maid cafe in so long, I decided to make you my famous omurice! Complete with my own brand of flavor beam that I can guarantee you is better than Uta’s!"
    a "Don’t worry, though! I’m sure you’ll be strong enough to leave the house and go visit there soon if you keep improving at the rate you {i}have{/i} been! "
    a "Not that there’s any reason you’d {i}want{/i} to leave, though. Right, Sensei?"
    s "..."
    a "..."

    scene anothercollector4
    with dissolve

    a "Exactly!"
    a "Things are so simple and easy when it’s just the two of us! I’m really happy you think the same way as me!"
    a "Because, between the way everyone keeps trying to harass me to get inside your room and the fact that they all think I’m not doing this for your sake, I’ve been starting to feel a little depressed lately."
    a "You don’t have to worry about me, though. I’m not letting it get in the way of your care. And I’ll continue doing everything I can to make sure you stay 100%% healthy, okay?"

    if ami_lust >= 60:
        jump amilust60
    else:
        scene black
        with dissolve2
        stop music fadeout 15.0

        a "Now, show me how you say “Aaaaah!” "
        a "Here comes the airplane, Sensei! "
        a "Ah! Oh no! It looks like some of the ketchup spilled on your chest! Ami to the rescue!"
        a "{i}Ahm...mn...{/i}"
        a "Mmm! That was delicious! "
        a "I think some of your flavor might have gotten mixed in with it on accident. Do you mind if I have a little more? I put so much love into this dish that I’m feeling a little lethargic all of a sudden! Hahah!"
        s "..."
        a "..."
        a "Oh yeah?..."
        a "Then I guess I’ll just have to wait until {i}after{/i} dinner to get a second taste..."

        $ renpy.end_replay()
        $ ami_love += 10
        $ amilust60skip = True

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "........."
        "......"
        "..."

        jump springtime6

label amilust60:
    if _in_replay:
        scene anothercollector4
        with dissolve
        play music "painisreal.mp3"

    s "..."
    a "..."

    scene anothercollector5
    with dissolve

    a "Of course, you silly goose! Everything I do is for your own good! It’s just an added benefit that it’s been so enjoyable for the two of us."

    scene anothercollector6
    with dissolve

    a "You’ve gotta make sure you eat the entire omelet though, got it? Broccoli too, mister. Don’t think for a second that I haven’t been keeping track of your fiber intake!"
    s "..."
    a "..."

    scene anothercollector7
    with dissolve

    a "Really? {i}Now?{/i}"
    a "But Sensei, your food will get cold. And I heard on TV that microwaves cause cancer, so I wouldn’t recommend reheating it and I’d probably just have to make your dinner all over again."
    s "..."
    a "..."

    scene anothercollector8
    with dissolve

    a "Hmm...if that really {i}is{/i} the case...then I guess it can’t be helped. "
    a "But this is the {i}last{/i} time I give you your check-up {i}before{/i} you eat dinner, okay? No exceptions!"

    scene black
    with dissolve2

    "Ami Arakawa places the omelet on the shelf next to the EnviroKids Organic Gorilla Munch Cereal before sanitizing her hands and climbing onto the bed beside her uncle."

    scene anothercollector9
    with dissolve2

    "He was a kind uncle. And it was unfortunate that he had come down with such a serious illness out of nowhere. "
    "But there was no illness too serious for Ami Arakawa. And she was determined to exorcise her uncle’s demons before they ever got the best of him."
    "She’d been making excellent progress so far. This was evidenced by the amount of semen she was able to extract from him on a daily basis."
    "Not extracting this semen would result in her uncle’s penis exploding — a tragedy that would likely result in his death. And so she was doing both him {i}and{/i} the world a favor by routinely milking him."
    "It was a lot of work. Especially since her hands were so small and his phallus was so large. But again, there was nothing Ami Arakawa couldn’t handle."
    "And so she curled her fingers around his member, tugging gently while gazing into his eyes, glazed over from the illness."
    "The air conditioner hummed in the background, still left on from the season that had just passed, making his nipples hard and leaving goosebumps all over his body."
    "Ami Arakawa was cold too. But she was not about to let her weakness show when it was pivotal for her to remain calm and composed during the milking process."
    "The slightest hiccup could result in his penis becoming soft, which would disrupt her healing practices and leave the demons trapped inside of her uncle to further corrupt him."
    "This would be bad for many reasons, but the most important of all of them would be that it could result in his death."
    "Having already lost the rest of her family, this was not something Ami Arakawa wanted to happen. It would be the worst possible outcome."
    "She steels her gaze, piercing further through the gloss in her uncle’s diseased eyes, and hones in on the shine in his pupils."
    "Within them, she sees a future with a swollen belly and a creature taking residence in her uterus. {i}His{/i} creature. And it would grow and grow until she was able to puke it out of her beautiful vagina."
    "It was so beautiful. It was a perfect vagina. It was the envy of Kumon-mi."
    "And only he and his preconceived creature were allowed to feast their eyes upon it."

    a "Does that feel good, [amimaster]?"
    s "..."
    a "..."
    a "All day? Really? "
    a "Then I’m sorry I kept you waiting just now. But you can go ahead and blame it on everybody else if it keeps me brighter in those pretty doe-eyes of yours."
    a "Is there anything in particular you want me doing to help you cum today? Any costume or role you want me to play? A certain speed or sensation you’re thirsting for?"
    s "..."
    a "..."
    a "But I don’t {i}have{/i} anything I want to do. I’m happy enough just getting to spend time with you."
    a "Just being allowed to pleasure you like this is more than I ever thought I’d get. And I thought of that {i}a lot,{/i} you know. Since long before you ever wanted to touch me."

    scene anothercollector10
    with dissolve

    a "Or maybe you always {i}did{/i} want to touch me. But you were just holding yourself back because I was too little...or because you just felt like you should have been “looking out for me” instead. "
    a "You were so silly back then, [amimaster]. And you’re silly now too. But “looking out for me?” That’s just crazy talk."

    scene anothercollector11
    with dissolve

    a "I’m way stronger than you give me credit for. And the mere {i}idea{/i} of needing somebody to look after me makes me chuckle. It’s {i}me{/i} who is the caretaker. It’s {i}me{/i} who lives to serve."
    a "All you need to do is lay there and let me do what I was born to do, okay? I’ll jerk those demons out of you in no time at all."

    play sound "static.mp3"
    scene anothercollector12 with flash
    stop sound

    "And so Ami Arakawa proceeded to milk her uncle, stopping every several minutes to dry his drool with her sleeve. "
    "It was a kind gesture — both the milking and the drying of the drool. And it was further evidence to reestablish the fact that she was perfect for this role."
    "She really {i}was{/i} “The Caretaker.” And anyone else who laid claim to the title only did so because they did not understand her worth. "
    "These good deeds of hers, hidden behind closed doors, would only be witnessed through the eyes of her uncle and the gods that watched over the Wishing Well."
    "Throughout the course of this story, you have decided who some of those gods are. But you have made those decisions based on what you believe you know rather than what is actually true."
    "In a place far from here, the Xoanon plucks a body from the water, drying it off with a towel made of sheepskin, before scribbling something down in a notebook."
    "It writes the following-"
    "“Blessed be those who live to protect. Who live selflessly, helplessly, and full of regret.”"
    "“What is it they long for? Why can’t they forget?”"
    "Then it puts its pen down and awaits the next reset."

    a "You’re getting close, [amimaster]. I can feel it throbbing in my hand. "
    a "Do you want me to slow down a little so you can savor the moment some more? Or should I work harder and help you finish up so you can eat?"
    s "..."
    a "..."

    scene anothercollector13
    with dissolve

    a "Nuh-uh. Edging isn’t good for your health. And while it may help you exercise your penis so you can last longer in bed, it does evil things to your mind. And your mind is what I love the most about you!"
    a "It really just comes down to what type of orgasm feels best for you, [amimaster]. Do you want a slow, sensual one? Or do you want a fast, aggressive one? Just tell me and I’ll make it happen."
    s "..."
    a "..."
    a "Really? You’ll let me choose {i}again?{/i} "
    a "What did I do to deserve such kindness today?"
    s "..."
    a "..."

    scene anothercollector14
    with dissolve

    a "Aww! That’s so sweet of you, [amimaster]! Thank you so much for recognizing how hard I’ve been working these last few weeks."
    a "And don’t worry about “Christmas being ruined” because I can promise you it’s not. Just knowing we can celebrate it together is the best gift I could ever-"
    s "e"

    scene anothercollector15
    with dissolve

    a "Ah! You’re about to cum, aren’t you?"
    s "..."
    a "That’s okay, [amimaster]. Just hold it in for one more second while I get the jar."

    scene black
    with dissolve2

    "Ami Arakawa dashes to the shelf she previously placed her famous omurice on and begins to frantically search for the second object she entered the room with."

    play sound "static.mp3"
    scene anothercollector16 with flash
    stop sound

    "It was a mason jar. But it wasn’t just {i}any{/i} mason jar. It was a {i}special{/i} mason jar. "
    "You see, Ami Arakawa had been collecting her uncle’s semen in jars just like this one since he was hospitalized on the night of November 1st."
    "This was the third jar. There were two more, half-full or half-empty, inside the freezer and beside the carrots. "
    "She was saving them for a special occasion and had the intent to use their contents for various purposes ranging from baking to recreation on days where she didn’t have much going on."
    "There were several more important reasons to keep such a specific item in her freezer, but Ami Arakawa has requested that they not be included in dialogue constructed by “AUTO-PILOT.”"
    "She gripped her uncle’s penis harder than before, aiming it at the upper section of the glass as she was amused by the way his semen looked when it shot out and made contact with it."
    "The way it dripped down to the lower section always made her giggle, but it was less because of the visual aspect and more because it elicited a sense of satisfaction over a job well done."
    "These jars, in addition to their more practical uses, served as trophies. And she hoped to collect so many that she’d have to either eat those frozen carrots or let them thaw and rot out on the kitchen counter."
    "Her butt swayed in front of her uncle’s face, but she knew better than to expect his tongue to exit his mouth and make contact with her in any form. "
    "Regardless, such a desire did not matter."
    "Ami Arakawa was the caretaker — and she was here to perfectly perform her role in the grand scheme of the universe."
    "She was here to milk her family."

    a "Come on, [amimaster]. Let it all out. "
    s "..."
    a "..."
    a "I know the jar is cold, I’m sorry. You’re just so big that it’s hard to keep everything straight without having you brush up against it every once in a while."
    a "I’d get a bigger jar, but I’m not sure if I’d be able to fit it inside the-"

    with sexfade
    with sexfade
    scene anothercollector17 with cumflash
    with hpunch

    a "Ah! There you go!"

    scene anothercollector18
    with dissolve

    a "Good boy, [amimaster]! You let out a whole lot today! "
    a "Maybe I’ll have to start milking you even {i}more{/i} often if your body is producing this much? How does that sound? Good?"
    s "..."
    a "..."
    a "Good!"

    scene black
    with dissolve2

    a "I’ll go put this on ice so it doesn’t go bad and I’ll be {i}right{/i} back to clean you up, okay?"
    a "Then, after that, I’ll remake your dinner and we can take a bath and watch Christmas movies! Yay!"
    s "..."
    a "I love you too, [amimaster]! Be back soon!"

    "Ami Arakawa leaves the room."

    stop music

    "The music stops."
    "And her uncle, Akira, remains on the bed having just been milked to completion."
    "His phallus twitches as his nipples harden once more from the cool air of the forgotten machine in the corner of the room."
    "The door of the freezer is opened."
    "The carrots are left out to thaw."

    $ renpy.end_replay()
    $ amilust60 = True
    $ ami_lust += 1

    "{i}Ami’s lust has increased to [ami_lust]!{/i}"
    "........."
    "......"
    "..."

    jump springtime6

label amispring1:
    play sound "static.mp3"
    scene amihair1 with flash
    stop sound
    play music "isingforyou.mp3"
    $ renpy.pause(20, hard=True)

    "The average human body’s chest cavity can withstand a little over 400 lbs of weight before being crushed, but there are several factors that could cause this number to fluctuate."
    "On September 18th of 1692, a man by the name of Giles Corey was executed by Captain John Gardner of Nantucket after being accused of and charged with witchcraft."
    "But what various historical texts and the acclaimed play adaptation “The Crucible” will not tell you is that there is a very specific reason Mr. Corey was able to withstand a number likely larger than 400 lbs."
    "Inside his chest cavity was a special worm."
    "The worm did not have a name, but it fed on the residue that seeped through Giles’ body until, after consuming enough, it began to grow teeth."
    "Giles Corey was an old man. An old man with a young worm. And the young worm wanted to be old one day."
    "So, while Mr. Corey was being pressed to death, it came up with a plan."
    "The worm hardened its body with the help of God as it had been saving up the religious power inadvertently stored by Giles Corey each time he prayed at night."
    "And while this allowed the young worm and the old man to survive slightly longer, it meant nothing in the face of the determined Captain John Gardner of Nantucket."
    "Eventually, the worm and Giles Corey would be crushed to death. And their bodies, still conjoined, would be dumped into a nearby river when their skin refused to burn."
    "But that isn’t the end of the story."
    "In fact, the story is still going on right now."
    "Because when the body of Giles Corey decomposed, so did the worm. And the leftover power of God that allowed the worm to harden its body was dispersed throughout the water."
    "By the time we found out, it was already too late."
    "We have all drunk from the water."
    "Now, we all have worms inside of us."
    "And every time we talk to God, we’re only making them stronger."
    "{i}- The true story of how we came to be{/i}"

    play sound "dooropen.mp3"
    scene amihair2

    s "..."

    "I am house."

    a "{i}Daaaaisy, Daaaaisy, give me your answer doooooooo~{/i}"
    a "{i}I’m haaaaalf craaaaazy, all for the love of youuuuuuu~{/i}"

    scene amihair3
    with dissolve

    s "?..."
    a "{i}It won’t be a styyyylish marriage~{/i}"
    a "{i}I caaaan’t affoooord a carriage~{/i}"
    a "{i}But youuuu’ll look sweet upoooon the seat of a bicycle built for twoooooo~{/i}"

    scene amihair4
    with dissolve

    s "..."
    a "{i}Daaaaisy, Daaaaisy, give me your answer doooooooo~{/i}"
    a "{i}I’m haaaaalf craaaaazy, all for the love of youuuuuuu~{/i}"
    a "{i}It won’t be a styyyylish marriage~{/i}"
    a "{i}I caaaan’t affoooord a carriage~{/i}"
    a "{i}But youuuu’ll look sweet upoooon the seat of a bicycle built for twoooooo~{/i}"
    s "Ami?"

    stop music

    a "_"
    s "What..."
    s "What are you doing?..."
    a "_"
    s "..."

    play music "isingforyou.mp3"

    a "{i}Daaaaisy, Daaaaisy, give me your answer doooooooo~{/i}"

    "Ami only looks at me for a moment before going back to singing her wretched song."

    a "{i}I’m haaaaalf craaaaazy, all for the love of youuuuuuu~{/i}"

    "Her voice has never been polished, and she’s no stranger to slowly navigating away from the proper key-"

    a "{i}It won’t be a styyyylish marriage~{/i}"
    a "{i}I caaaan’t affoooord a carriage~{/i}"

    "But she sounds much worse than normal right now."

    a "{i}But youuuu’ll look sweet upoooon the seat of a bicycle built for twoooooo~{/i}"

    "And she looks even worse."

    stop music
    play sound "static.mp3"
    scene amihair5 with flash
    stop sound

    a "{i}Daaaaisy, Daaaaisy, give me your answer doooooooo~{/i}"
    a "{i}I’m haaaaalf craaaaazy, all for the love of youuuuuuu~{/i}"
    s "Ami..."
    s "What have you done?..."
    a "Cut it off and sold it."
    s "What?..."
    a "Don’t you like me now? "
    a "I’m me, Jim."
    s "..."
    a "It’s sold, I tell you— sold and gone, too. It’s the night before Christmas, boy. Be good to me, because I sold it for you."
    s "..."

    play sound "static.mp3"
    scene amihair6 with flash
    stop sound
    play music "glasswalker.mp3"

    a "My hair will grow again. You won’t care, will you? My hair grows very fast. "
    a "It’s Christmas, Jim. Let’s be happy. You don’t know what a nice—what a beautiful nice gift I got for you."

    "Locks of thick, red hair cover the floor like the blood of a lamb who’d just been slaughtered. And in this dark room, where the only light we have is what bleeds through black curtains, I can tell you I’m scared."
    "It’ll be our little secret. And I’ll become a butcher myself if you give in and let it out."
    "But in the meantime, I will present myself to my caretaker so that she may hoist me up and attach me to a cold metal device that will hang me upside down- so she can drain the juice from my neck and drink it."

    a "Don’t you like me now? "
    a "I’m me, Jim."
    s "Ami...put the scissors down."
    a "About time! Do you have any idea how much trouble you'd get into if the principal showed up and caught you sleeping right now?"
    s "What?..."
    a "Class ended ten minutes ago. It's time to get up."
    s "Ami, listen to me...you’re not thinking clearly. And I have no idea what’s going on, but I’m here for you now. So give me the scissors and-"

    play sound "static.mp3"
    scene amihair7 with flash
    stop sound

    a "Allow me to {i}re-{/i}introduce you to Kumon-mi! A super normal town just outside of Tokyo."
    a "Rule number one is keep your hands off all of your students! But that should probably be a rule that goes without saying since...you know."
    a "That's the part where you were supposed to say, “You're the only girl for me, Ami! I don't care about any of the other ones!”"
    a "Enough about that, how 'bout we get back to some of those rules you were just talking about?"
    a "Rule number one is keep your hands off all of your students!"
    a "Rule number two is keep your hands off all of your students!"
    a "Rules number three and four and five and six are keep your hands off all of your students BUT YOU DIDN’T FOLLOW THE RULES, JIM! {size=+7}YOU NEVER FOLLOW THE RULES!{/size}"
    s "I know. I’m very bad at that, and I’m {i}sorry.{/i} Now, {i}please{/i} give me the scissors before you wind up hurting yourself."
    a "やだ。"
    s "Ami, please."
    a "やだやだやだやだやだやだやだやだやだやだやだやだやだやだ。"
    s "Then...what do you want me to do? What {i}can{/i} I do?"

    play sound "static.mp3"
    scene amihair8 with flash
    stop sound

    a "{b}YOU COULD HAVE LISTENED!{/b}"
    a "YOU COULD HAVE FOLLOWED ME LIKE YOU SAID YOU WOULD! COULD HAVE LOVED ME! BUT YOU DON’T LOVE ME AT ALL, JIM! YOU DON’T CARE THAT I SOLD MY HAIR!"

    play sound "static.mp3"
    scene amihair9 with flash
    stop sound

    a "It’s so pretty, isn’t it? I’ve been growing it forever. You always said you liked twintails. And my hair looks just like mom’s. "
    a "You loved her hair too. Loved it a lot. You picked some off a piece of her scalp when it was all we had left. You tasted it. You chewed on the little bits of dead flesh. You wanted to feed your worm. "
    s "Give me...the scissors..."

    play sound "static.mp3"
    scene amihair8 with flash
    stop sound

    a "{b}{size=+15}I HAVE ALREADY GIVEN YOU EVERYTHING!{/b}{/size}"
    a "WHAT HAVE I GOTTEN IN RETURN, JIM?! THERE IS NOTHING LEFT! YOU’VE TAKEN ALL OF ME! "

    if amifingered == False:
        a "ALL OF ME BUT THE ONE THING I WANT YOU TO HAVE! WHAT ARE YOU SO AFRAID OF?!"
    else:
        a "MY INNOCENCE! MY PURITY! MY BLOOD! MY BLOOD AND SWEAT AND BLOOD! "

    scene amihair9
    with dissolve

    a "Oh!"
    a "I know."
    a "It’s the worm, isn’t it? The worm is making you do the things you do, so I just have to get it out of you! If I get it out of you, you’ll go back to normal!"
    s "What worm?! What are you talking about?!"
    a "The one inside you who blocks the path between you and God! The one that kept Giles Corey alive when Captain John Gardner kept increasing the weight! You know the worm I’m talking about! "
    s "I have no idea what you’re talking about because nothing you’re saying makes any sense!"

    play sound "static.mp3"
    scene amihair8 with flash
    stop sound

    a "{b}NOTHING MAKES SENSE HERE! IT’S NOT SUPPOSED TO!{/b}"
    a "{b}YOU’RE SUPPOSED TO TREAT THIS LIKE A GAME! YOU’RE SUPPOSED TO GET ME PREGNANT! YOU’RE SUPPOSED TO REACH THE EPILOGUE!{/b}"

    scene amihair11
    with dissolve

    a "But all you ever do is lie. You hide the truth because the truth would hurt me. And Ami is fragile! Ami can’t handle it! Ami’s a joke! Ami’s too clingy! Ami is a bad girl!"

    scene amihair12
    with dissolve

    a "{b}AMI’S NOT A BAD GIRL! AMI’S A GOOD GIRL! AMI’S THE ULTIMATE NIECE! AMI IS CUTE! LOVE AMI MORE! LOVE LOVE LOVE LOVE LOVE LOVE AMI!{/b}"

    play sound "static.mp3"
    scene aminewfirstevent2 with flash
    scene amiani12 with flash
    scene amibus12 with flash
    scene amidatecafe6 with flash
    scene amidormten9 with flash
    scene amihair13 with flash
    stop sound

    s "I do love you!"
    a "{size=+15}{b}LIAR!{/size}{/b}"
    a "I called you over and over and over and over and over and over and you never answered! You left me alone! I was worried about you! I thought someone raped and murdered you! You don’t love me at all! "
    a "You think Ami is a bad girl! But you’re wrong! Wrong wrong wrong wrong wrong! Ami is good! I cut off my hair and sold it! I did it for you!"
    s "You didn’t sell anything, Ami. It’s all over the ground. It’s {i}everywhere.{/i} And I’m sorry I didn’t pick up the phone, I just...didn’t know how to handle this. I was...scared."

    scene amihair14
    with dissolve

    a "Scared?..."
    s "Yeah..."
    s "I don’t know what to do for you. I don’t know how to help you the way you help me. And you’ve been acting so strangely the last couple days, that I...ran away. Because I always run away."
    s "But I’m here now. And I’m going to help you. "
    a "Ami doesn’t need help. Ami is normal. She’s a good niece who can do everything you need her to. "
    s "Then I need you to stop going crazy and give me the scissors. You’ve already ruined your hair. I don’t want you...ruining your face as well."
    a "It’s the worm, Jim. The worm is making me do things. I can feel it squirming around in there. I can feel its teeth."

    scene amihair15
    with dissolve

    s "Give-"
    a "{b}{size=+15}I’M NOT DONE YET! YOU CAN’T HAVE THEM!{/b}{/size}"
    s "I will take them if I have to, Ami. I’m much stronger than you are."
    a "You’re {i}weak!{/i} A crybaby! You tear up when I read you bedtime stories! Your eyes glaze over in sakura season! You are {i}nothing{/i} without me! Nothing!"

    scene amihair16
    with dissolve

    s "You think I don’t know that?! You really think I don’t understand everything you’ve done for me?!"
    a "Get away from me! You’re a fake! A liar! A half-eaten replica! You just want to feed the worm!"
    s "Give me the fucking-"

    play sound "stab.mp3"
    scene amihair17
    with hpunch

    s "Ngh!"
    a "LET GO LET GO LET GO LET GO LET GO LET GO LET GO I NEED TO CUT THE WORM OUT LET GO LET GO I NEED TO KILL IT LET GO NEED TO KILL THE WORM LET GO LET GO I HAVE TO SAVE MY INSIDES LET GO!"

    "Twin blades sink into the sensitive flesh of my palm as I pull Ami’s hand closer. "
    "She struggles, as I expect her to, causing the scissors to dig deeper into my skin as I frantically attempt to figure out what I’m going to do when I have {i}control{/i} of them."
    "She’s a danger to herself and anyone she encounters in this state. And while that’s not something I’m prepared to handle, I knew it was only a matter of time until something like this happened."
    "But why now? "
    "What about waking up from my two months of “rest” ignited this wildfire within her mind? And why does {i}her{/i} shattering coincide with mine when {i}I’m{/i} the one who lost something?"
    "Does she really think she’s losing me?"
    "Is going through my phone and exposing the truth all it took to break her?"

    scene amihair18
    with dissolve2

    a "..."
    a "Huh?"
    s "Let...go..."

    play sound "static.mp3"
    scene amihair19 with flash
    stop sound

    a "Huh? What? How? Huh? Why? Why? How? What?"
    a "Did I...no no no no no no. No! No, it wasn’t me! I wouldn’t do that! It was the worm! The worm did it!"
    a "Sensei, it was the worm! It wasn’t me! I’m a good girl! Ami is a good girl!"

    "Somehow, this feels familiar. "
    "There was someone just like her who used to lick my wounds."
    "She would dress them before dressing me, and she would numb the pain of existing with her hands and her mouth."
    "But in hindsight, I sometimes believe she only did this because she liked the taste of blood. "

    a "Sensei! It wasn’t me! It was an accident! I would never...no! I didn’t do that!"
    s "It’s fine. It’ll heal on its own. It’s not like you pierced all the way through my hand or anything."

    play sound "static.mp3"
    scene amihair20 with flash
    stop sound

    a "Ah.......ah.........hah! No! No, I didn’t...No no no no no. No! No, no, no! No!"
    s "Ami, look at me. "

    scene amihair21
    with dissolve2

    a "..."
    s "What is going on with you?"
    a "..."
    s "Is it all because of me?"
    a "..."
    s "Did I make it worse? Or is it my fault entirely? Be honest."
    a "..."
    s "Would you rather just go to your room like I did?"
    a "..."
    s "Do you want to stay in bed for the next two months while I sponge-bathe you and read {i}you{/i} bedtime stories? Will {i}that{/i} help?"
    a "I..."
    s "You what?..."
    a "..."

    scene black
    with dissolve2

    a "I just want to be pure."

    "........."
    "......"
    "..."

    scene amihair22
    with dissolve2

    "Ami collapses to the floor when I retreat to the kitchen for some paper towels to wrap my hand in."
    "Within seconds, she begins to hyperventilate. And it looks to me as if she’s lost all will to live."
    "Like hurting me, even if it was in accident brought on by this fit of hysteria, signified to her that she is a failure."
    "But she’s not a failure."
    "She’s like this because {i}I{/i} have failed her — and not just because I’ve been absent during the last twenty-four hours in which she needed me most."
    "I’ve been absent her entire life."
    "And even when I was present, it was more like {i}I{/i} was a ghost."
    "I can feel the one that’s been following me put her hands on my shoulders."
    "I hear her whisper into my ear."

    se "{i}What have you done to my darling little girl?{/i}"

    "I can’t bring myself to respond. But she doesn’t go away."
    "She pulls up a chair at the dining room table and watches as I stand here, useless and confused."
    "All the while, Ami’s humanity slowly drifts away."
    "What’s left is just a worm."
    "But the worm inside {i}me{/i} senses its presence. "

    scene amihair23
    with dissolve2

    a "{b}WAAAAAAAAAAAAAaaaaaAAAAAAAaaaaAAAAaahhhhaahhhha!!!!!!!!!!!!{/b}"
    a "{b}I’M SO SORRY!!!!!!! I’M SO SORRY!!!!!!!!!! IT WAS AN ACCIDENT!!!!!!!!! AAAAAAAAaaaaaahhhhaaaaaa!!!!!!!!!!!{/b}"
    a "{b}I’M A BAD GIRL!!!!!!!!!!!!!!!!!!!!!!!!!!{/b}"

    scene amihair24
    with dissolve2

    "The worms need to be together."
    "It’s the only way they’ll ever feel like they belong."

    scene black
    with dissolve2

    "I know now what the scissor angel warned me of, but this accident brings me no closer to God nor Heaven’s Web."
    "It brings me closer to ruin — and the idea that this world may have {i}already{/i} come to an end. And this is all that’s left."

    if amifingered == True:
        "But now that the one that I love the most is gone, it creates an opening."
        "A {i}new{/i} love can take its place."
        "And what better candidate than the girl who’s been beside me all along?"
        "What better candidate than the one who will take care of me when I can no longer move? "
        "What better candidate than the one who can’t survive without me?"
        "Maybe what I felt before wasn’t love at all as it was seldom accompanied by this level of fear."
        "And maybe acknowledging that is what it will take for me to finally be happy."

        scene bedroom_night
        with dissolve2
        stop music fadeout 15.0

        "I put Ami to bed. "
        "She’s yet to stop crying. "
        "I left our doors open so I can hear her from all the way in here."
        "But her voice is not that of a siren’s."
        "I will go to her when she needs me. "
        "But I can sense that it will be quite some time before she comes to me."

    else:
        "But is that enough to keep me here?"
        "Is there any amount of time that I can wait before a new love takes the place of the one that I have lost?"
        "I have so many options, but none of them feel {i}right.{/i}"
        "Should I just give in and be with Ami after all?"
        "Should I cast aside the one virtue I’ve managed to keep clasped inside my hands and just...find something else to hold instead?"
        "I don’t know."
        "..."
        "Maybe this fear...this {i}uncertainty{/i} is just another part of growing up."
        "But if that’s the case, I wonder why it’s taken me over thirty years to start."
        "Even more than that, though..."
        "I wonder how long it will take to finish."
        "Because, between you and me?"
        "This is hell. "
        "But it’s right where I belong."

        scene bedroom_night
        with dissolve2
        stop music fadeout 15.0

        "I put Ami to bed. "
        "She’s yet to stop crying. "
        "I left our doors open so I can hear her, but it’s only getting worse. "
        "She screams for hours about how sorry she is. "
        "She screams about a worm."

    scene black
    with dissolve2

    "Tomorrow, a new stage of my life will begin."
    "But will it be better than all the ones before it?"
    "I don’t know. "
    "But there’s only one way to find out."
    "I close my eyes."
    "And when I dream that night, I see the same clockwater bed that I always do."
    "But there’s no one on it this time."
    "There’s just a box."

    $ renpy.end_replay()
    $ amispring1 = True
    $ amiblock = True
    $ senseisad = True

    "{i}Ami Arakawa has obtained the status effect [[BEDRIDDEN]!{/i}"
    "........."
    "......"
    "..."

    $ day = 3
    $ totaldays += 1
    hide tuesday onlayer date
    show wednesday onlayer date

    scene bedroom_day
    with dissolve2

    "I wake up to sunlight pouring in through the window."
    "But there’s nothing I want to do."

    scene black
    with dissolve2

    "So I spend the morning watching Ami sleep. "
    "I have a feeling I’ll be doing that a lot now."

    "{i}Akira Arakawa has obtained the status effect [[DEPRESSED]!{/i}"
    "{i}When Akira is inflicted by [[DEPRESSED], the things he once enjoyed no longer sound appealing to him!{/i}"
    "{i}Some options may no longer be available to him as a result of this.{/i}"
    "{i}But don’t worry!{/i}"
    "{i}All he has to do is get over it!{/i}"
    "{i}Once he does that, everything will go back to normal.{/i}"
    "{i}And the worm will feed once more.{/i}"

    jump dellaslump

label amicamp1:
    scene nightsky
    with dissolve2

    "I leave Makoto behind and start making my way home, equal parts exasperated and concerned."
    "For one, it’s relatively late and I have no idea whether or not Ami is even going to be awake by the time I get home. "
    "On top of that, though, how is this going to make me sound? And why am I even concerned about how I’m going to sound in the first place when all that should {i}really{/i} matter is the effect it will have on her?"
    "She’ll know right away that this isn’t my idea. And I know {i}her,{/i} so I know it will make {i}her{/i} concerned about how I landed on this. And she knows {i}me{/i} so she’ll know {i}I’ll{/i} be concerned as a result of that."
    "Then, we can all be concerned together because that’s an important adjective beginning with the letter C (which rhymes with T) and I just want this day to be over."

    scene black
    with dissolve2

    "Unfortunately, nothing ever ends when I want it to. It’s either long before or long after. Which means that either this night is going to last an extra several hours-"
    "Or I am going to be hit by a car on the way home and Ami will be left with no one but a girl who only wants her because she shares my blood."
    "........."
    "......"
    "..."

    scene knockknockami1
    with dissolve2
    play music "lastdailysong.mp3"

    "I used to buy books for Ami when she was much smaller."
    "I don’t know why I’m just now remembering that- but perhaps it has something to do with this door."
    "Come to think of it, there’s a verse that sticks out in my head when I look at it. But I can’t remember all of it, so I hope this much will do."
    "The hallway of life is door upon door."
    "Each door has a doorknob. Each opens to secrets."
    "One secret. One doorknob. "
    "Daily, I choose a doorway to walk through. "
    "At times I’m confused for I know that each door is a new day to live, a new way to struggle, a new way to give."
    "I stand in this hall lined with doors, doors galore, knowing each doorway will open to more-"
    "Seeking the one that will make me feel free-"
    "And turning a doorknob to find a new me..."
    "That’s what I hope to get out of this, isn’t it?"
    "Maybe not right away, but I wouldn’t be putting the effort in at all if I wasn’t in search of a change, right?"
    "Is there a new me behind this door? "
    "Is she playing patty-cake with him? Or dressing him up in women’s clothes as he scoffs and pretends he isn’t enjoying it?"

    scene black
    with dissolve2
    play sound "knock.mp3"

    "Or is it simply locked?"

    s "Ami?"

    "Maybe I’ll get lucky."
    "Maybe it will be empty."

    a "Come in..."

    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene knockknockami2
    with dissolve2

    s "Hey...sorry for bothering you so late."
    a "If you’re going to apologize to anyone, it should probably be Niki...I just got off the phone with her and she’s still mad about you leaving me alone. "
    a "And besides, you don’t ever have to apologize to me, Sensei. Especially now that I’ve hurt you. "
    s "It was barely a scratch, Ami. It healed within a few days."
    a "Do you want to hurt me to make up for it? Because you can if you want. I deserve it."
    s "I’m good. Do you have a few minutes to talk, though?"
    a "I have all the time in the world. But what is it you want to talk about?"
    s "A few things, actually. And one of them involves Niki. But chances are I’ll tuck my tail between my legs and escape before I can even get to that part."
    a "I’m...confused."

    scene knockknockami3
    with dissolve

    s "Yeah...me too. "
    s "But I’ve been confused a lot lately. And that’s not fair to you."
    a "...Sensei?"
    s "How long have you been stuck in here now?"
    a "I...haven’t really been keeping track..."
    s "Me neither. And that’s just one of the many pieces of evidence you can use to explain how absent I’ve been when you need me the most."
    a "But...that’s not true. You’ve been cleaning...kind of. And you’re cooking for me and-"
    s "Microwaving food and picking up things from the convenience store doesn’t count as cooking. And despite you dedicating your entire life to caring for me, I’ve put in virtually no effort at all to return the favor."
    a "I’m not expecting you to return the favor, Sensei. I-"
    s "Shut up and let me finish."

    scene knockknockami4
    with dissolve

    s "I want to be a better guardian. But just {i}wanting{/i} that is all I’ve been able to do so far. And each day I spend without taking another step in the right direction is another day in a hallway lined with locked doors."
    a "In a...hallway lined with...what? I don’t get it."
    s "You don’t have to get it. The point is, I need to do something. Something more than just {i}wanting{/i} to do something or you’ll never leave this room."
    a "..."
    s "Is that what you want? "
    a "Only if you’re stuck in here with me..."
    s "I think I’ve made it pretty apparent with my actions in recent days that that’s not how things are going to be. "
    s "I can’t sit still. I like ruining things too much."
    a "That’s just how it is for {i}now...{/i}"
    a "But one day, we’ll be in this same position again. And you won’t want to leave then."
    a "When that time comes, you’ll stay right here with me. "
    a "We’ll grow old and die inside of this house, and no one will find us until we’re both decayed and covered in maggots."
    s "Sounds delightful. No thanks."
    a "I don’t want you to change, Sensei."
    s "Not even if it means being better?"
    a "You can’t get any better than you are now. You’re perfect for me and I am perfect for you."
    s "I can get a {i}lot{/i} better, Ami. I just...might need a little assistance in order to do that."
    a "Getting assistance from anyone else will just make you worse."
    s "Would it be worse if I could actually cook for you? If I knew what to buy you from the store and you didn’t have to call Niki because you don’t have any faith in me? Would {i}that{/i} be worse, Ami?"
    a "That alone? Of course not..."
    a "But that’s not how it would go."
    a "Small changes lead to bigger changes. Then bigger changes lead to colossal ones. Then...something, something, butterfly effect. "
    a "I don’t want that..."
    a "I want my uncle..."

    scene knockknockami2
    with dissolve

    s "Would a father not be better?"
    a "A-"
    s "Move over. This isn’t a conversation we should have with me just standing here."
    a "Sensei..."

    scene black
    with dissolve2

    s "Move."

    "........."
    "......"
    "..."

    scene knockknockami5
    with dissolve2

    s "I know you think you’ve failed me, but it’s the other way around. And I’m sorry I ever let things get to that point in the first place."
    s "I want you to be able to count on me. But I also know that counting on me in my current state would be nothing short of idiotic. And even {i}you’re{/i} smarter than that."
    a "Are you...making fun of me?"
    s "Yes. And I’m doing that because I {i}can{/i} make fun of you and everything will be fine because that’s how strong our connection is. But even so, there’s something about it that needs to change."
    s "If I’m ever going to {i}really{/i} be there for you, I need to figure out a place to start. And what better place than the middle of the woods?"

    scene knockknockami6
    with dissolve

    a "...heh?"
    s "Let’s go on a trip. A camping trip, specifically."
    a "You...want to go...camping?..."
    s "Yeah. I think it’ll be good for us to get out of the house for a little while. And your friends won’t be around to see you looking like a drowned rat in the middle of the woods."
    a "I...don’t understand."
    s "I want to be more like a parent to you, Ami. You’ve been deprived of a relationship like that for half of your life and that just isn’t fair. "
    s "It’s no wonder you act so fucking insane all of the time. You never learned how to be normal because I was never there to teach you that. "
    a "So you’re...going to teach me how to...put up a tent instead?"
    s "Honestly, I have no idea how to do that myself."

    scene knockknockami7
    with dissolve

    a "Then where the heck are we going to sleep in the middle of the woods?!"
    s "We’ll figure it out. I just think we need a fresh start — and I think doing things we wouldn’t normally do otherwise is a...good way to commence that process."

    scene knockknockami8
    with dissolve

    a "I mean...I don’t {i}dislike{/i} the idea. It just...doesn’t seem like something you’d come up with on your own."
    s "What difference does it make if I’m the one who came up with it or not? The fact remains that I want to do this {i}for you.{/i} And, to a lesser extent...myself, I guess. "
    a "But, Sensei...I never went camping with my dad. How does doing that make you more like-"
    s "Again, it doesn’t matter {i}what{/i} it is. I’m sure an uncle could take his niece on a camping trip too. But I don’t think that’s what you want. "
    s "And it might not even be how you look at me in the first place. I just know that, whatever I am to you, it’s not enough anymore."
    s "So, call me a jerk and interpret this however you like, but I want to fix you. And I want you to fix me. And we can’t do that if we stay the way we are now."
    s "We both need help, Ami. A lot of it. And we’re too stubborn to ever truly take that from someone else, so we need to rely on each other. Do you think you can do that?"
    a "Of course I can do that. I’ve been doing that for half of my life. But why would you want to get any closer to me when you know how dangerous I am?"
    s "You’re not dangerous, Ami."

    scene knockknockami9
    with dissolve

    a "I cut your hand! I threatened all of the other girls at school! I went through your phone! I used it to blackmail people! I’m a bad girl, Sensei! And now you want to {i}reward{/i} me for that?! Why?!"
    s "Do you really think you’re the only person who’s “bad” here? Because I’ve done my fair share of terrible things as well. So how about we just say they cancel each other out and we can be horrible together?"

    scene knockknockami10
    with dissolve

    a "Would you really accept me as a daughter after how hard I’ve made everything for you?..."
    s "Would you really accept me as a father after I waited for you to go bat-shit crazy before finally deciding to step up?"

    scene knockknockami11
    with dissolve

    a "This...is all really surprising to me, Sensei. I’m not sure how to react."
    s "Do you want to go camping or not? I have to know if I should pack your bag, because we’d be leaving in the morning."
    a "I’d go anywhere with you. I just...can’t help but shake the feeling that you just want to drop me off in the woods and leave me there to die."
    a "And if that’s what you want, fine. I’ll die. I just don’t want to get my hopes up and then immediately find out that none of this is real."
    s "Ami, look at me."

    scene knockknockami12
    with dissolve2

    a "..."
    s "I want you to have a happy life."
    s "And I will do whatever it takes to make that happen."
    a "I don’t need much, Sensei. Just you."
    s "Then you can have me. And I will build you a world where nothing can hurt you anymore."
    s "I’ll protect you with all I have, and keep you on the right path even though I can’t ever seem to travel down it myself."
    s "I will be exactly what I was {i}meant{/i} to be all this time, and you’ll be able to breathe easy knowing that nothing you do will ever make me leave."
    a "You don’t mean that."
    s "I do."
    a "But what if it’s something really bad?"
    s "We’ll cross that bridge when we come to it."
    a "What if I hurt you again?"
    s "It’ll heal. "
    a "What if it doesn’t?"
    s "Then I’ll have a scar."
    a "But I don’t want you to have any more scars when you already have a million on the inside."
    s "And the same goes for how I feel about you. But that’s the point of this fresh start and why I’m going to try and be better."
    s "Just...please forgive me if I start proposing more things like this as I’ve become desperate enough to start taking suggestions since thinking is hard and I have lost all will to live."
    a "Will you really accept me, Sensei?"
    s "Is that even a question? Of course."
    a "For better or for worse?"
    s "I don’t think things can get much worse than this."
    a "In sickness and in health?"
    s "Mostly sickness, I assume. But again, yes."
    s "I accept you, flaws and all. And I promise that, even when I can’t help but ruin things again in the future, I’ll remain by your side no matter what. "
    a "You really mean that?"
    s "I do."
    s "You deserve a proper home. And a proper home has more in it than one little girl and the space that I take up. A proper home has a {i}family.{/i}"
    a "But we’ve been family all along...that’s what I’m so confused about."
    s "In nothing but blood. You’ve carried the rest of this “family” on your back. And all I’m trying to do now is take a little of that weight off."
    s "You deserve to rest. "
    s "So I will ask again-"
    a "Yes."

    scene knockknockami13
    with dissolve

    s "Yes?"
    a "Yeah...I’ll go."
    a "But, fair warning...I have no idea what to do. And I’d kind of like to know who gave you this idea in the first place.."
    s "I’ll tell you tomorrow. I have to pack our stuff, and you need to be getting to sleep as well."

    scene knockknockami14
    with dissolve

    a "But, wait...wasn’t there something else that you wanted to-"
    s "Yeah. "
    s "I don’t have the energy for more than one step at a time, though. "

    scene black
    with dissolve2

    s "And I’m pretty sure that this one would make her proud enough to forgive me for forgoing the next."

    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene knockknockami15
    with dissolve2

    a "..."
    a "..."
    a "..."
    a "Camping, huh?..."
    a "And who was he talking about just now?"
    a "..."
    a "No, I don’t think it was you."
    a "..."

    scene knockknockami16
    with dissolve

    a "But it could be fun. And he’s never called himself that before."
    a "..."
    a "You think so?"
    a "..."
    a "And if it doesn’t work?..."
    a "..."

    scene knockknockami17
    with dissolve

    a "That’s easy."

    scene black
    with dissolve2

    a "I can chop it off."

    $ renpy.end_replay()
    $ amicamp1 = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"

    jump saracamp1

label amicamp2:
    scene black
    with dissolve2

    "You know...I think I’ve killed enough time wandering around the forest. "
    "I’ve gone fishing with Maki...I sat by the river with Yuki...I’ve even [[REDACTED] with Kaori and [[TEMPLATE9]."
    "And in the event that Sara is still not done “bonding” with Ami, I’m just going to have to make her my temporary wife in order to reinsert myself into Ami’s day."
    "This trip was meant to strengthen {i}our{/i} bond, after all. And as appreciative as I am to have someone like Sara who is going {i}way{/i} out of her way to bring some maternal influence back into Ami’s life, I-"

    play sound "static.mp3"
    scene camphair1 with flash
    stop sound

    ni "{i}Let me move in with you. Let me be her mom.{/i}"

    play sound "glass.mp3"
    scene camphair2

    "I suddenly remember that there is someone else I was supposed to give that role to."

    play sound "glass.mp3"
    scene camphair3

    "I suddenly remember that I had the building blocks to form a real family firmly in my hands and all I’ve done with them is build another wall."

    play sound "glass.mp3"
    scene camphair4

    "But this one was made specially for Niki — a girl I’ve known forever who wants nothing more than to be a bigger player in the game that I call life."

    play sound "glass.mp3"
    scene camphair5

    "But for some reason, I still struggle with the thought of putting her through that."

    scene black
    play sound "window.mp3"

    "I swear, this game would be so much easier if that family would just fuck off already."

    scene camphair6
    $ renpy.pause(3, hard=True)
    scene white
    $ renpy.pause(1, hard=True)
    scene camphair7
    play music "gentle.mp3"

    s "I’m back from where I was before."
    maki "I feel like I literally just saw you."
    yu "Yeah, same."
    h "I know I make things about myself a lot, but I just want to say I’m quite offended that you’ve hung out with literally everyone but me."
    s "Not everyone. I’ve still barely seen Sara and Ami. But, now that I mention it-"

    scene camphair8
    with dissolve

    maki "Don’t worry. She’s not {i}stealing{/i} her or trying to take your place or anything. I’m sure they’ll be done soon."
    maki "But, then again, I could be wrong since I wasn’t allowed in there either."
    s "Probably because you would have made things weird and gotten some sort of animal penis involved."

    scene camphair9
    with dissolve

    maki "We’re in nature, Sensei. There are animal penises {i}everywhere.{/i}"
    maki "I can’t make them any more involved than they already are."
    h "I don’t like the way you look at nature, Maki. "
    yu "Sara’s got some weird fuckin’ friends, huh?"

    scene camphair10
    with dissolve

    h "We weren’t always this bad. But things have really gone to shit over the last few years and now this is sort of just where we’re at. "
    yu "Wack. Feel like it’s the complete opposite for me."
    maki "If you’re that worried, why not just head over to their tent? I feel like you could have been with them this entire time if you really wanted. Neither one of them is going to deny {i}you.{/i}"
    s "Wasn’t I kind of denied already? Like, the only reason I wandered around at all is because Sara made it sound like this was something only she and Ami were-"
    sar "What’s this about Sara and Ami?"

    scene camphair11
    with dissolve2

    s "..."
    maki "Oh, wow. That’s certainly a drastic change."
    s "Ami?..."

    scene camphair12
    with dissolve2

    sar "That’s right! Surprise!"
    s "You...cut that much off?..."

    scene camphair13
    with dissolve

    sar "I kind of had to. Like, maybe I could have gotten away with leaving it a little longer. But it was so uneven that I figured it’d make the most sense to just completely clean it up and start fresh."
    s "But..."
    a "Do you hate it?..."
    s "..."
    a "I know you’ve always preferred longer hair, but...it’s like Sara said. It was just...too messed up to really {i}save.{/i}"

    scene camphair14
    with dissolve

    a "It...It’ll grow back, though! So you only have to deal with having someone who looks more like a nephew for a little while and...I can wear even girlier clothes to try and make up for-"
    s "No."

    scene camphair15
    with dissolve

    a "...No?"
    s "I still think you’re adorable. It’s just...really different."

    scene camphair16
    with dissolve

    a "Y...Yeah..."
    a "I don’t even want to think of what the other girls will say if...any of them are still willing to talk to me."
    sar "I know this isn’t the best time, but I’m going to need at least 8,000 yen for the haircut. You can just Venmo me if you don’t have cash."

    scene camphair17
    with dissolve

    a "Sara...come on."
    sar "Kidding, kidding. Your uncle’s given me more than enough money with all the booze he’s bought over the last few years. This is the least I can do."

    scene camphair18
    with dissolve

    sar "Which means, now it’s {i}his{/i} turn!"
    a "..."
    s "My turn to what?"
    sar "Spend some time with Ami, of course! That’s what you’ve been waiting for ever since we got here, is it not? Because I know for sure that’s what {i}Ami’s{/i} been looking forward to."
    sar "And now she gets to do that without feeling super self-conscious about the way she looks!"
    a "I mean...don’t get me wrong...I think you did a great job, but...I wouldn’t say I’m not self-conscious anymore. This is the first time I’ve ever even {i}had{/i} short hair. It’ll take a little while to...get used to."
    s "Sara..."
    sar "Sarasaki86."
    s "What?"
    sar "My Venmo name. "
    s "I don’t even know what that is."

    scene camphair19
    with dissolve

    a "Please forgive my uncle...he’s kind of illiterate when it comes to technology."
    s "And you’re kind of illiterate when it comes to literacy, but I love you anyway."

    scene camphair20
    with dissolve

    a "You’re...saying that in front of other people now?!"
    sar "That was the single cutest thing I have ever heard come out of your mouth and I would like you to say it again right now. "
    s "No."
    sar "I’ll waive the haircut fee."
    s "I love you, Ami."

    scene camphair21
    with dissolve

    sar "Kyaaaah! My heart!"
    a "I...love you too. More than anything in the whole wide world."
    s "That’s good to hear."

    scene black
    with dissolve2

    s "I guess...shall we go for a walk then?"
    a "Y...Yeah! "
    maki "Have fun, you two! But remember that there are bears around here! "
    h "And remember that Maki is probably thinking about their penises!"
    maki "Well I am {i}now.{/i} Thanks a lot, Haru-kun."
    yu "Aight. That’s enough of this shit. I’m takin’ a smoke break."
    sar "You’re literally smoking right now, Yuki."
    yu "I can handle two at once."
    maki "Ahh, another woman of culture."
    sar "I’m more than content with one so long as it belongs to the man that I love."
    a "Can we...maybe start walking now? So we don’t have to listen to this anymore?..."
    s "Yeah, I don’t want to be around another second of this either."

    scene sky
    with dissolve2

    "And so the two of us set off toward the middle of nowhere."

    play sound "static.mp3"
    scene noonsky with flash
    stop sound

    "And we keep walking until the sun sets."
    "Ami fills me in on all of the things she talked about with Sara."
    "As you may have guessed, I was a hot topic when it came to conversation. But Ami assured me that she managed to keep her most {i}impure{/i} feelings out of the equation for my sake."

    if amifingered == False:
        "And while that’s nice and all, I wish she’d keep them out of her head entirely as they’re going to be even less acceptable once I fit better into the role I was meant to inhabit years ago."
    else:
        "Which is great because after commanding me to cum inside of her probably over a hundred times now, I think it’s safe to say those feelings are pretty impure."
        "Such comments probably shouldn’t sprout up on a trip where I’ve pledged to become more of a father though."
        "A good father doesn’t cum inside his daughter. A good father cums on her face. Or into a ball of napkins she presses against the head of his cock when the time comes for him to let loose."
        "But again, that doesn’t matter right now."

    "I can’t avoid this any longer. And I certainly can’t afford to let her break again because she barely has any hair to cut off now and I’m worried about what she’d lose next."

    scene black
    with dissolve2

    "I’m worried about a lot of things, really."
    "I’m worried about whether she even {i}wants{/i} to look at me any differently than a worthless uncle she needs to take care of."
    "I’m worried about her feeling worthless in her own regard if I start to do more things around the house on my own."
    "I’m worried of whether or not her friends are still her friends or if she’ll need to find new ones. And I’m worried about whether she even {i}wants{/i} friends in the first place when all she ever thinks about is me."

    scene camphair22
    with dissolve2

    "But most of all, I’m worried about her growing up."
    "Which is irrational given the type of world we live in, yes. And further exacerbated by the fact that I’ve been both subtly and not-so-subtly prompting her to grow up for years now."
    "Was all of that just me lying to myself?"
    "Do I really want an Ami who can avoid clinging to me? Who lets me stay out late and do whatever I want without so much as a care in the world?"
    "Or do I want someone who will keep me in her heart at all hours of the day?"
    "Who will call me over and over and over again, hundreds or thousands of times until I’m feeling brave enough to pick up the phone."
    "Does the type of Ami I’ll have even matter? Or is it just her I want in general?"
    "I have no way of knowing, really. And I think for a moment that this just might be what being a parent feels like."
    "But then I remember how it felt to be a child."
    "And how I’m probably just being delusional again."

    a "Do you believe in God, Sensei?"
    s "Do you?"
    a "I do."
    a "Maya makes fun of me for it sometimes, but I think that He’s real."
    a "I don’t know if He’s watching every second of every day, but I think He’s there."
    a "And I think that all of the suffering that you and I have endured is just His way of testing us."
    s "Testing us for what?"
    a "To see if we are worthy of Heaven."
    a "To see if we can endure the harshness of reality and overcome adversity in order to gain one of the many limited seats in the giant sky castle all good boys and girls go to when they die."
    s "{i}Adversity{/i} is a pretty big word for you, Ami."
    a "Well, God’s a pretty big thing. He deserves bigger words."

    scene camphair23
    with dissolve

    s "To be honest, I don’t really know what I believe. "
    s "I want to say I don’t. But sometimes I feel like that might just be me lying to myself since there’s rarely a time where things are going terribly that I’m not either blaming or talking to {s}god{/s} God."
    s "I still instinctively want to pray when something bad happens. I just typically decide against it because it feels like...submitting."
    a "What’s wrong with submitting to something you believe in?"
    s "The fact that I don’t know if I actually believe it. Because there’s a chance I only want to pray in the first place because I was conditioned to want that."
    a "If I’m conditioned to hug a teddy bear every time I’m feeling sad just because someone gave me one when I was little, does that make wanting to hug a teddy bear wrong now that I’m older and can buy my own?"
    s "Not...necessarily."
    s "Also, is it just me, or have we had this conversation before?"

    scene camphair24
    with dissolve

    a "We’ve probably had it before."
    a "In fact, there are probably {i}tons{/i} of conversations we’ve had before that we’re going to forget about and then have again."
    a "That’s kind of just what happens when you spend so much time with somebody, I think."
    s "Do you think our answers will ever change?"

    scene camphair25
    with dissolve

    a "I don’t think there’s {i}anything{/i} off limits for change now that my hair is completely gone."
    a "The dark circles might take a little longer to get rid of, though. But Sara gave me a few tips on how to treat them."
    s "I don’t mind those sticking around. They make you look like a...cute zombie or something."
    a "I didn’t know you were into that sort of thing, Sensei."

    scene camphair26
    with dissolve

    s "It was an earlier talking point."
    s "Besides, there are probably a lot of things you don’t know about me."
    a "Probably. "
    a "And the same goes for me."
    a "But if there’s anything you ever {i}want{/i} to know-"
    s "Ami...am I on the right track right now?"

    scene camphair27
    with dissolve

    a "The right track? What do you mean?"
    s "With this...parenting thing. "
    s "Like, is this something you actually {i}want?{/i} Or is it something I’ve just decided you {i}need?{/i}"

    scene camphair28
    with dissolve

    s "I’ve been your uncle forever. You’ve been my niece forever. And I’ve been all sorts of fucked up lately, so it’s highly plausible that this is just some sort of delusion I cooked up and..."
    s "And I don’t want to change anything if that’s going to fuck with your head since I know the two of us are pretty against change to begin with."
    a "Is it really changing anything, though?"
    s "What do you mean?"

    scene camphair29
    with dissolve

    if amimaster.lower() in ["daddy", "dad", "papa"]:
        a "I mean...you basically {i}are{/i} my dad already. I’ve just never really called you that outside of sex because I didn’t want to put any pressure on you."
    else:
        a "I mean...you basically {i}are{/i} my dad already. I’ve just never really called you that because I didn’t want to put any pressure on you."

    scene camphair30
    with dissolve

    s "..."
    a "Like, don’t get me wrong. I love things like this and nothing would make me happier than to experience more special outings with you to make more special memories, but..."

    scene camphair31
    with dissolve

    a "You don’t need to do this kind of stuff to make me look at you that way."
    a "You don’t need to change anything at all."
    a "You’re doing great."
    a "And I’m excited for you to keep being my dad for the rest of our lives."
    s "..."

    scene camphair32
    with dissolve

    a "..."
    s "..."
    a "Is it...okay if I call you that now?..."
    a "Dad?..."
    s "..."
    a "..."
    s "Yeah..."
    a "Do you..."
    a "Do you think my first dad would be okay with it?..."
    a "Because I’ve tried asking him, but...I never really get a response."
    s "I..."
    s "I have no idea..."
    a "I think he would..."
    a "And...besides-"

    scene camphair33
    with dissolve

    a "Besides! There’s always the chance that I could be, like...your {i}actual{/i} daughter anyway, right?"

    scene camphair34
    with dissolve2

    s "..."
    s "What?"
    a "Like...I already know you loved my mom, so..."
    a "It wouldn’t be crazy if you guys might have...you know..."

    scene camphair35
    with dissolve

    a "It wouldn’t be crazy if I was your real daughter anyway! Right?!"
    s "..."
    a "Right?..."

    scene camphair36
    with dissolve

    s "..."
    a "Uh..."
    a "Are..."
    a "Is...everything okay?"
    s "I..."
    s "I just don’t really know what to say to that, Ami."
    a "Should I...not have said that?"
    s "How long has that thought been in your head?"

    scene camphair37
    with dissolve

    a "Um..."
    a "Kind of...{i}loooooong...{/i}"
    s "And...that hasn’t changed the way you {i}look{/i} at me?"

    if amifingered == True:
        scene camphair38
        with dissolve

        a "Honestly?..."
        a "I think it makes it more exciting."
        s "..."
        a "And significantly less legal, probably."

    else:
        scene camphair39
        with dissolve

        a "Oh, not at all."
        a "If anything, it just makes me want to carry your incest babies even more. And my hope in telling you this is that you will now revisit your stance when it comes to having sex with me."
        s "You think you being my {i}actual daughter{/i} would {i}increase{/i} the chance of that?"
        a "I’ll take any chance I can get at this point."

    scene camphair40
    with dissolve

    s "You know what? Let’s just...shelve that thought for now and...revisit it one day when I’m feeling a little less broken."
    a "Sure. Of course, if that’s what makes you happy."
    a "Can I...still call you Dad though?"

    scene camphair41
    with dissolve

    s "Yeah."
    a "Like...in front of other people, though?"
    s "Wherever and whenever you want."
    a "And...you’re not worried about what they might think?"
    s "You’re my number one priority now, Ami."

    scene camphair42
    with dissolve

    a "{i}Now?{/i}"
    s "Did I say “now?” I meant “always.”"
    a "Mhm. Nice cover."

    scene camphair43
    with dissolve
    stop music fadeout 15.0

    a "I just hope this doesn’t mean Ayane is going to try and call you Dad as well. She hates when I have things that she doesn’t and I’ve never once complained that {i}her{/i} allegedly biological father is alive."
    s "I’m pretty sure Ayane’s father isn’t just “alleged,” Ami."
    a "I know that. But {i}mine{/i} is and I’m trying to draw parallels here."

    scene noonsky
    with dissolve2

    s "Okay. I think that’s enough sitting around for now. Let’s head back to the camp."
    a "But Daaaaaaaaaad!"
    s "You’re going to do that all the time now, aren’t you?"
    a "Of course!"

    scene black
    with dissolve2

    a "I have to make up for lost time."

    play sound "winner.mp3"
    "{i}Congratulations! Your status effect [[DEPRESSION] has weakened!{/i}"
    play sound "winner.mp3"
    "{i}Congratulations! Your status effect [[PARANOIA] has weakened!{/i}"

    if amifingered == True:
        play sound "winner.mp3"
        "{i}Congratulations! You have earned the title [[(ALLEGED) DAUGHTER-FUCKER]!{/i}"

    $ renpy.end_replay()
    $ amicamp2 = True
    $ ami_love += 10

    "{i}Ami’s affection has increased by 10!{/i}"
    "{i}Things are finally starting to look up!{/i}"
    "{i}If only you would stop looking down.{/i}"

    play sound "static.mp3"
    scene clearnightsky with flash
    stop sound

    "Darkness falls several hours later."
    "Ami has run off somewhere and everyone else seems to be doing something."
    "What should {i}I{/i} do?"

    jump campmenu2

menu campmenu2:
    "Bond with Haruka" if harukacamp1 == False:
        jump harukacamp1
    "See what Nao is up to" if naocamp2 == False:
        jump naocamp2
    "Play games with Kaori" if kaoricamp2 == False and naocamp2 == True:
        jump kaoricamp2
    "Call someone" if toukacamp1 == False:
        jump toukacamp1
    "Call it a night" if toukacamp1 == True and kaoricamp2 == True and naocamp2 == True and harukacamp1 == True:
        jump saracamp2

label halloweenami1:
    play sound "static.mp3"
    scene chikayumihallow6 with flash
    stop sound
    play music "shrinesong.mp3"

    "And on that note, we return to the tragic tale of Maya Makinami (or the one who wears her skin)."
    "Hurt and betrayed by the one she loves the most, the skinwalker skin-walked herself all the way over to the {i}place{/i} she loves the most."
    "It was a random vending machine somewhere near the halfway point between the home she had and the home she wanted. But that’s not where she is right now. {b}Right now,{/b} she’s at the shrine."
    "And she doesn’t care much for that place. She doesn’t care much for gods or sweeping. Even the miko dress she normally wore here pissed her off on days when it didn’t agree with the heat."
    "But that was fine, because there was normally someone more than willing to help her take it off. Right now, though, he could be taking off some idol’s Kagome costume and she wouldn’t even know it!"
    "Her blood boiled! Her hands shook! How could such a terrible thing happen to her?! But if only she knew the horrors she had already seen — and the others that have yet to befall her."

    play sound "static.mp3"
    scene amitotherescue1 with flash
    stop sound

    "Into the frame walks her best friend! "
    "She’s a magical girl who goes by the name Ami Arakawa during the day and Sakura Sunlight at night! Her secret power was always being seven and a half steps ahead."

    if amifingered == True:
        "But her {i}other{/i} secret power was cum absorption! She was almost 50%% cum now! Good job, Sakura Sunlight!"
    else:
        "But her {i}other{/i} secret power was cum absorption! Just no one knew about that yet since there was no cum for her to absorb!"

    "Regardless, she was here now! And she wasn’t about to let her best friend feel lonely anymore. "

    a "Maya? Are you anywhere around here? Can you hear me?"

    "She could! But her lips remained shut while she pictured those of a pink-haired girl slowly opening and welcoming a dick into her mouth. How lewd, this imaginary cuckoldry! Bad Maya!"

    scene amitotherescue2
    with dissolve

    a "I sure hope she’s okay...she seemed really upset back there. But at least I get where she’s coming from."

    "The hero spoke to herself. She did that a lot when she wasn’t speaking to others. Or things that she thought were there but weren’t actually there even though they were still kind of there."
    "Right now, Maya Makinami actually {i}was{/i} there, though. And sensing that Ami was just seven and a half steps away from kicking dirt into her shoes, she finally decided to speak up."

    m "How did you know I was here?..."

    play sound "static.mp3"
    scene amitotherescue3 with flash
    stop sound

    a "Oh! There you are. I’ve been looking all over for- are you crying?"
    m "It’s...allergy season."

    scene amitotherescue4
    with dissolve

    a "You can tell me if you are, Maya. It’s okay to cry. It’s not like I’m going to tell anyone."

    "Ami Arakawa was so nice! Only a good person would say good things to a bad person. And that’s what’s happening right now! It’s a remarkable show of kindness. She’s so great! "

    m "Why...aren’t you at the party?"
    a "You think I was just going to let you dramatically storm off like that without chasing after you? The party can wait. Your feelings can not."

    "So kind! "

    scene amitotherescue5
    with dissolve

    m "Feelings are stupid. I just thought it would be more fun to spend Halloween on my own this year. That’s all."

    "So mean, rejecting Ami’s kindness like that! And such a liar too!"

    a "And how exactly were you going to have fun at the shrine? You hate this place."

    "That’s a fact Ami Arakawa remembers because she’s a good friend who always pays attention to what the people she loves say or do."

    m "I just...left something here. That’s all."
    a "Well, I hope it was your honesty since you’re being a big ole liar-pants right now."

    "Fact 1: honesty is not tangible. Fact 2: Ami Arakawa knew Maya would never find hers even if it was. Fact 3: Ami looks super cute in her costume this year! Her thighs look so soft! I bet she moisturizes!"

    m "Just leave me alone, please...I’m really not in the mood today."
    a "I can’t just {i}leave you alone,{/i} Maya. Not when you’re like this. What kind of friend would that make me?"

    scene amitotherescue6
    with dissolve

    a "How about...we spend Halloween {i}together{/i} this year? Just you and me. Nobody else really wants me at the party anyway. And the people who {i}do{/i} probably just want to beat me up."
    m "No one wants to beat you up. They all just think you’re batshit insane. Hitting people like that is normally frowned upon."

    scene amitotherescue7
    with dissolve

    a "Well, at least it’s nice to know that being looked down on {i}can{/i} have perks from time to time. But what do you say, Maya? Are you really gonna keep rejecting me? Or can we have some fun together?"

    play sound "static.mp3"
    scene amitotherescue8 with flash
    stop sound

    m "Ami...did you come after me on your own? Or did...somebody put you up to this?"
    a "Hm? That’s a weird question to ask your best friend. Why would anyone send me after you? I love you more than anybody in the world."
    m "Anybody more than Sensei, you mean. "
    a "He doesn’t count. "
    m "Then...Niki?"
    a "..."
    m "{i}You{/i} would still choose me over her, right? Just because she’s moving in doesn’t mean you don’t need me anymore, does it? Otherwise, you wouldn’t be here. Right?"
    a "Maya..."
    a "I think we should sit down and take a break for a little while, okay?"

    play sound "static.mp3"
    scene amitotherescue9 with flash
    stop sound

    "So sit they did but break they didn’t! At least not in a bad way. Because breaking can be good sometimes! This doesn’t have to be a sad day!"
    "Relax and breathe and celebrate! Friendship makes the dream work. Then team work makes the other thing and...something makes the...cream...jerk."
    "It’s rhyming time! It’s time to rhyme! It’s time to build a fifth ark! The third is full of bullet holes, the fourth is made of pine bark! "
    "So anyway, just look at this. Lock eyes with screen, put dick in fist. Then squeeze until it’s purple while you wait for them to kiss! "
    "{s}ABCDEFG, HIJKL. ELLENELEMENOPEE, IT’S HOT DOWN HERE IN HELL. {/s}"
    "Ami is a good girl and her best friend is a bad one. She’s an uncle-stealing piece of shit who controls what Ami’s dad’s done."
    "Or does or did-slash-doing, these eyes don’t span for miles. Just escalators, elevators, while Ami sprints for MILES-"
    "To FIND that fucking BAD GIRL she’s evil evil fuck! I hate her hate her oh my god she really really sucks!"
    "Ami Ami Ami Ami Ami Ami Ami. Ami Ami, Ami Ami, Ami Ami Ami?"
    "The needle goes in to suck out the truth."

    a "You’ve always had pretty harsh feelings when it comes to Niki, haven’t you?"
    m "I don’t know what you’re talking about."
    a "Oh, come on. I know your feelings toward her and Noriko aren’t just because of a distaste for pink. You don’t like them because of how important they are to Sensei. "
    a "It’s the same reason you stormed out today. But that’s nothing to be embarrassed about, Maya. I get it. And honestly, it makes me feel a little weird too."
    m "..."
    a "You just gonna stay silent until I change topics? Is that what we’re doing?"
    m "No..."
    m "I cracked and made how I really feel way too obvious today. I realize there’s no getting out of it now. But..."
    m "What really confuses me is why you’re treating me like nothing happened instead of ripping my guts out since this is obviously more than a stupid crush."

    scene amitotherescue10
    with dissolve

    a "If I wanted to rip your guts out, I would have done it one of the other millions of times you’ve lied right to my face. "

    scene amitotherescue11
    with dissolve2

    a "Do you really think I’m that gullible? That I wouldn’t catch on to my best friend in the whole wide world fucking my uncle {i}while I’m home{/i} sometimes? Do you really think I’m {i}that{/i} dumb? "
    m "I...am suddenly having second thoughts about the position I chose to have this conversation in."
    a "..."
    m "..."

    scene amitotherescue12
    with dissolve

    a "Pfft!"
    m "Or...not?"

    scene amitotherescue13
    with dissolve

    a "Why did you lie to me, Maya? Why don’t you ever tell the truth?"
    m "What do you mean “why did I lie?” My entire relationship with him was supposed to be confidential. And you were the {i}last{/i} person who was ever supposed to know about it."
    a "Because I love him more?"
    m "Because you’re a fucking psychopath who would cut his dick off if it was the only way you knew how to keep him close to you."
    a "There are other ways to keep him close. And I would never intentionally hurt Sensei like that. He isn’t Sensei without his dick and I think it should stay attached."

    scene amitotherescue14
    with dissolve

    m "Whatever...it’s not like it even matters anymore now that Niki’s come back into the picture. We’re both fucked. Like, what does either one of {i}us{/i} have that she doesn’t?"
    a "We’re...closer to Sensei’s preferred age group?"
    m "Yippee. "
    a "Are you giving up then?"
    m "I don’t {i}want{/i} to...but it feels like he’s been trying to {i}get{/i} me to for months now."
    a "Is that so?"
    m "All I’ve done lately is chase after him. And it’s made me stop and think about how all of this got started in the first place. "
    m "In the beginning, all we were doing was just...hiding our pain inside one another. And we worked because {i}that{/i} worked. But if it’s not working anymore..."
    m "If chasing after him is only going to hurt me when it’s {i}supposed{/i} to be making me feel better...what the fuck am I doing, Ami?"
    a "Can I let you in on a little secret, Maya?"
    m "Please don’t tell me who else he’s fucking. I really don’t want to know. "
    a "I was just going to say that {i}I’m{/i} worried about this Niki thing too."
    m "Bullshit. There’s no way Sensei would have let her move in without you signing off on it. All you’re doing right now is pitying me."
    a "No, I’m telling you the truth. Scout’s honor."

    scene amitotherescue15
    with dissolve

    m "Then how the fuck were you acting so composed around her earlier?"
    a "I’m not sure if I’ve ever been “composed” a second in my life."
    m "Well, at least you’re aware of it. But still. The way she spoke to you alone made it feel like you two were mother and daughter. So much so that I was convinced it was just a nightmare at first."
    a "It really feels that way sometimes, doesn’t it? Like the universe is playing pranks on us...making things harder than they have to be just so somebody looking down on us can have a little fun. "
    m "Bad news is there’s no one looking down on us ever."
    a "You don’t know that for sure, Maya. No one does. So it all comes down to faith. Which is why I ask you this-"
    a "Do you have faith in Sensei? "
    a "Do you think he’ll find his way back to you?"
    m "I..."
    m "I’m not really..."
    a "Or do you want to {i}drag{/i} him back?"

    stop music fadeout 12.0
    scene amitotherescue16
    with dissolve2

    m "D...Drag him?..."
    a "That’s right..."

    scene amitotherescue17
    with dissolve2

    a "If you’re tired of chasing after him, all you {i}really{/i} need to do is keep him on a leash. That way, he won’t ever get too far away."
    a "Wouldn’t that be the answer to all of your problems?..."

    scene amitotherescue18
    with dissolve2

    a "Or perhaps there’s another answer? One even closer..."
    m "...Ami?"
    a "All this time, the three of us could have been having fun together...but you always made me wait outside."

    scene amitotherescue19
    with dissolve2

    m "W...What?"
    a "I remember the first time...I didn’t really understand what I was hearing. So I stood there with my ear up against the door for what seemed like an eternity, just...{i}listening.{/i}"
    a "You sounded so happy...I’d never heard you make noises like that before. It was almost...intoxicating. And I don’t even {i}like{/i} girls. Or at least I didn’t {i}think{/i} I did. But with {i}you...{/i}"
    a "I don’t know..."
    m "You..."
    m "You...{i}listened{/i} to us?..."
    a "Mhm...But that’s not {i}all{/i} I did."

    scene amitotherescue20
    with dissolve2

    m "{i}What the fuck?...{/i}"
    a "Do you have any idea what it feels like to listen to your best friend and your {i}father{/i} fuck each other’s brains out every week for years?"
    a "Because it’s annoying at first. But you start to look forward to it after a while. And you tell yourself every time, {i}soon.{/i} Soon, they’ll remember me. {i}Soon,{/i} they’ll let me in. Just for a peek. "
    a "And when that day never comes, you get frustrated. You start pretending you’re in there with them. You time your fingers with the creaking of the bed. Time your {i}orgasm{/i} with theirs."
    a "You and I have cum together so many times and you didn’t even know it..."
    a "Isn’t that romantic, Maya?"
    m "Is..."
    m "Is this..."
    a "Another nightmare?..."
    m "Is this...really happening?..."
    a "That all depends on whether or not you want it to..."

    play sound "static.mp3"
    scene amitotherescue21 with flash
    stop sound

    a "What’s gonna happen if Sensei really does leave you for Niki? How are you going to make yourself feel whole then?"
    a "Because {i}I{/i} can still listen...but you’ll be all alone."
    a "Maybe you can still come over...and we can {i}both{/i} play pretend. "
    a "I’m a good actor, Maya. I can play a very convincing Sensei if I have to."
    m "..."
    a "Or..."
    a "We could do that {i}other{/i} thing I mentioned. "
    a "We could drag him back..."
    a "But here’s the catch..."
    a "If that’s the route you want to take...It will never be {i}only you{/i} again. "
    a "Not for the rest of our lives. "
    a "It’ll be all three of us..."
    a "Because how could anyone ever say no to that?"
    m "Ami..."
    a "Maya..."

    scene black
    with dissolve4

    m "{i}I’m in.{/i}"

    $ renpy.end_replay()
    $ halloweenami1 = True

    jump halloweenfive4

label amispring2:
    play sound "static.mp3"
    scene nakayamaslimotrip1 with flash
    stop sound

    a "Come to think of it, why is everyone always taking me on trips to bond with me? Can I not be bonded with from the comfort of my own home?"
    ni "No. Because that is where your father lives. And so long as he is present, you are unbondable."
    n "Unless it’s bond-{i}age.{/i} I’ve found that that’s {i}best{/i} done from the comfort of one’s own home as it’s an inherently safer environment that’s easier to establish boundaries in."
    a "See, Aunt Niki? If you want to tie me up and do things to me, at least let me stay in bed for it. How do you expect me to accept you as a mother if you can’t even do that much?"

    scene nakayamaslimotrip2
    with dissolve

    ni "Thank you, Noriko. Now Ami completely understands what this trip is all about. And here I was worried all the ropes and shackles would intimidate her."
    a "They might at first, but only because all of my experience with stuff like that is on the opposite end."
    n "Who was the person you tied up, Ami?"
    a "Maya. "

    scene nakayamaslimotrip3
    with dissolve

    n "Lucky! I want to do that! Then she’d be forced to like me or she’d have to stay my prisoner forever."
    ni "Maya’s that girl who has a crush on Akira, right?"
    a "You could say that about literally everyone I know and you’d still be correct."
    ni "No, I mean the one who threw a temper tantrum and stormed out of the house on Halloween. She was dressed up as Haruhi Suzumiya, wasn’t she?"

    play sound "static.mp3"
    scene nakayamaslimotrip4 with flash
    stop sound

    a "Oh, yeah. That’s Maya alright. Leave it to her to pick someone as dated as Haruhi Suzumiya. She’s like one Halloween off from going as Kagome or something."
    ni "Are you {i}trying{/i} to start a fight with me, child?"

    play sound "static.mp3"
    scene nakayamaslimotrip5 with flash
    stop sound

    n "Don’t feel bad, Nee-chan! I personally {i}love{/i} how you’re stuck in the era you grew up in. "
    n "It makes me feel less weird about the dramatic gap in time between the unprotected sex our parents had when they were creating us."
    ni "Thank you, Noriko. I’m very glad you reminded me of our parents having unprotected sex. Make that {i}two{/i} times today I have had to think of our father in that context now."

    scene nakayamaslimotrip6
    with dissolve

    n "Well jeez, Nee-chan. I know you love our dad, I just didn’t realize you loved him {i}that{/i} much."

    play sound "static.mp3"
    scene nakayamaslimotrip7 with flash
    stop sound

    ni "THAT’S NOT WHAT I MEANT!"

    play sound "static.mp3"
    scene nakayamaslimotrip8 with flash
    stop sound

    a "Sex with dads and how okay it is aside, I’m excited for this trip! I had a ton of fun with Sara when I went camping last time, so maybe this’ll be just as good?"

    scene nakayamaslimotrip9
    with dissolve

    ni "Sara? Who is Sara? What is Sara? {i}Why{/i} is Sara? Why did you go camping with her? "
    a "A friend’s mom. She’s the one who cut my hair. Super nice lady. Loves my dad maybe just as much as you do, Aunt Niki."

    scene nakayamaslimotrip10
    with dissolve

    ni "..............Oh! "
    ni "{size=-15}Well I’m sure she’s a very nice lady.{/size}"
    n "Ooooh, Nee-chan’s jealous now."
    a "Really? But why would Niki be jealous of a super nice and motherly woman who has already spent time bonding with me and reminding me of how a mother’s touch feels?"

    scene nakayamaslimotrip11
    with dissolve

    ni "I’m not jealous at all! I mean...{i}I’m{/i} a famous idol. And she’s your friend’s mother, so of course she’s already spoken for. There’s nothing for me {i}to{/i} be jealous of."
    a "Actually, Sara’s husband walked out on her a long time ago. She’s single now. And desperately looking for a new man to take care of her daughter. "
    ni "................Oh!"
    n "..."
    a "..."
    ni "Is she fat?"

    scene nakayamaslimotrip12
    with dissolve

    n "Nee-chan! That’s mean!"
    ni "What?! I’m allowed to ask! "
    a "She’s not! She’s actually really small and {i}super{/i} pretty! She could probably pass as a teenager if she really wanted to."

    scene nakayamaslimotrip13
    with dissolve

    ni "{b}{size=+5}FUCK!{/size}{/b}"
    ni "Patrice! Pull over! "
    pat "I can’t. There’s no shoulder. And I’m not going to just let you go out of the car to throw a tantrum. We’re on a highway. That’s a PR disaster waiting to happen."
    ni "You’re only saying that because you’ve never been in love, you fucking whore! Drive us off a cliff then! That’ll teach that bastard to bring other moms into the picture!"

    scene black
    with dissolve2

    n "Uhh...Nee-chan? When you say “other moms,” could it be that you’re forgetting you’re {i}not{/i} one of those? Unless- ah! You’re pregante!"
    a "Aunt Niki’s prangent?! Since when?!"
    ni "I am {i}not{/i} pergenat! I’m just leaving open the possibility that one day, I {i}might{/i} be?"
    pat "Why can’t any of you pronounce the word “pregnant?”"
    ni "Have you never been on the fucking Internet before, Patrice?! Pull over!"
    pat "To use the Internet?"
    ni "No! To throw yourself into the ocean, you slimy cunt!"

    scene sky
    with dissolve2
    stop music fadeout 12.0

    "And so the car was ultimately brought to a stop just five minutes from the girls’ final destination."
    "{size=-2}With her manager hovering over her and shielding her from the passing cars, dashcams, and prying eyes, Niki then proceeded to curse her childhood friend to a lifetime worth of erectile dysfunction whenever she wasn’t around.{/size}"
    "Of course, this would very much not be the case. And he would proceed to have erections around basically everyone because that’s just the kind of guy he was."
    "On the inside of the limo, though, an awkward silence took the place of the girl who occupied the middle seat just seconds ago."
    "Because, while Noriko was brought along to cultivate a more bond-friendly environment, the truth was she still didn’t know how to feel about Ami."
    "But Ami knew how to feel about her."
    "And what Noriko did not yet understand is that, for perhaps the first time ever, she’d be on the receiving end of what could only be called “faith.” "
    "Not faith in a god. Not faith in a friend. Not even faith in what was now essentially family."
    "Just faith that she’d fulfill the role she needed to fill to keep the wheels of time spinning while everything else has stopped. "

    scene black
    with dissolve4

    "A pencil in the hand of God is as good as a pen in the hand of the Pope."
    "But when both of those tools are taken away, only one can write in blood."
    "The other must simply watch."

    play music "acoustic.mp3" fadein 3.0
    scene nakayamaslimotrip14
    with dissolve3

    ni "Having some trouble there, Patrice?"
    pat "I’m honestly just surprised you only brought one bag."
    ni "There are ten more in the car."
    pat "Niki, we’re here for {i}one{/i} weekend..."

    scene nakayamaslimotrip15
    with dissolve

    ni "I know. I just thought you could use the exercise. Aren’t I the nicest client you’ve ever had?"
    pat "{i}Hah...{/i}I’ll be back with everything else in a minute. But remember, we have a meeting with the photographer in-"
    ni "Yeah, yeah. Fuck off. Thanks!"

    scene nakayamaslimotrip16
    with dissolve

    a "Poor Patrice. What did she ever do to anybody?"
    ni "Didn’t you threaten to kill her the last time you guys met?"

    scene nakayamaslimotrip17
    with dissolve

    a "Oh, yeah...I guess I did."
    n "You have a meeting already, Nee-chan? You don’t even get to settle in first?"
    ni "It shouldn’t take long. I just have to go sign off on a few swimsuits. Make sure nothing’s {i}too{/u} revealing or we might sell too many calendars and I’ll suddenly be drowning in money."

    scene nakayamaslimotrip18
    with dissolve

    a "This might be a weird question, but have you ever imagined how much you’d make if you did porn?"
    ni "Not really. I’m too successful to have ever considered pivoting to that. I’m sure the offers will start rolling in once I’m retired, though."
    n "I’m already getting them."

    scene nakayamaslimotrip19
    with dissolve

    ni "What? From {i}who?{/i}"
    n "Probably a bunch of companies who want to hire you and don’t realize how old I am. Social media’s a cesspool nowadays, Onee-chan."
    ni "Give me your phone. I don’t want those weirdos contacting you anymore."
    n "I can’t. There are too many nudes of Kirin in there and I don’t want you seeing them despite how badly she probably wants you to."

    scene nakayamaslimotrip20
    with fade

    ni "Ugh...fine. Whatever. Just don’t fucking respond to any of those people, okay? I’ll have failed as a sister if you start doing porn. Which isn’t even mentioning how it could impact {i}my{/i} career."
    n "That was such a good opportunity to remind me how much you love me and you squandered it. Who am I to you, Nee-chan? Patrice?"
    ni "No. But you {i}are{/i} a babysitter until I get back. Now, watch Ami and make sure she doesn’t contact Akira. "

    play sound "slidedoor.mp3"
    scene nakayamaslimotrip21
    with dissolve

    n "Okay!"
    a "Noriko’s not even that much older than me!"
    ni "{i}True! But Noriko doesn’t want to fuck her dad, so she’s clearly the more mature out of you! Be back soon!"

    scene nakayamaslimotrip22
    with dissolve

    a "It’s 2020. How are there still girls out there who {i}don’t{/i} want to fuck their dad?"
    n "I want to fuck {i}your{/i} dad. Does that count?"

    scene nakayamaslimotrip23
    with dissolve

    a "Close enough, I guess. I’m sure you will sooner or later too. I’m done trying to stop people from doing it."

    scene nakayamaslimotrip24
    with dissolve

    n "Wait, you are? Since when? How did that happen? This wasn’t just some extremely long, extremely creepy phase, was it?"
    a "Of course not. There’s just no way for me to get what I want by interfering anymore. "
    n "And...{i}what{/i} is it you want, Ami?"
    a "Well, for one, I’d like Niki to stop trying to be my new mother when I already have a perfectly good one. "
    n "You mean...Sara? Is {i}that{/i} why you brought her up earlier? Cause it...did seem like you were trying to make her jealous. But I just thought-"
    a "I’m not talking about Sara. I’m talking about my mom. The same one I’ve always had."

    scene nakayamaslimotrip25
    with dissolve

    n "..."
    a "..."
    n "Uhh...Ami? I don’t know how to break this to you, but-"

    scene nakayamaslimotrip26
    with dissolve

    a "I know she’s dead, okay? But that doesn’t mean I’m okay with just replacing her. There are things she can still teach me from wherever she is now."

    scene nakayamaslimotrip27
    with dissolve

    a "She left a lot behind. Myself included, obviously. Someone trying to fill her shoes will only distract me from that."
    n "Nee-chan would never try to {i}replace{/i} her though, Ami. She-"
    a "I know. She said that herself. But it still doesn’t change the fact that she’s poking her nose where she shouldn’t. And she keeps trying to {i}change{/i} me when my mom never would."
    n "I mean...l was still super little when your mom was around, but I’m pretty sure she wouldn’t be okay with her daughter trying to fuck her brother-in-law."

    scene nakayamaslimotrip28
    with dissolve

    a "She was taken away too soon, so I guess we’ll never really know. But I {i}do{/i} know that the thought alone wouldn’t disturb her the way it does Niki."
    a "My mom understood the strange, sometimes {i}carnal{/i} bonds two people who don’t belong together can have. {i}She{/i} wouldn’t think I’m broken. Niki does."
    a "But what Niki doesn’t understand is that being “broken” is just an Arakawa family trait. We’re {i}all{/i} like that. "
    n "She does understand that, though. That’s why she tries so hard to make things better for you {i}and{/i} Nii-chan."
    a "But that’s {i}her{/i} idea of better. Not ours. And forcing that on us the way she does isn’t going to do anything but hurt her in the long run."
    n "..."
    a "..."
    n "Is it just me...or are you, like...way smarter all of a sudden?"

    scene nakayamaslimotrip29
    with dissolve

    a "It’s just you! The only thing inside {i}my{/i} head is spending time with my dad. So of course I’ll sound smarter when the conversation is centered around that."
    a "I still need Makoto’s help for math and stuff, though. So don’t worry, Noriko! You’re still smarter than me!"
    n "Hm..."

    scene nakayamaslimotrip30
    with dissolve

    a "Hm?..."
    n "Are you...happy, Ami?"
    a "Sometimes. Sometimes, not. How about you?"

    scene nakayamaslimotrip31
    with dissolve

    n "Sometimes..."
    n "I doubt you actually care though...and you’re only just asking {i}me{/i} because I asked {i}you.{/i}"
    a "Well, on that note, do you actually care about {i}me?{/i}"

    scene nakayamaslimotrip32
    with dissolve

    a "Or do you only {i}have{/i} to care about me because your “Nii-chan” does?"
    n "..."
    a "..."
    n "I wouldn’t have asked you if you were happy if I didn’t care."
    n "I do."
    n "I shouldn’t, but I do."

    scene nakayamaslimotrip33
    with dissolve

    n "And I want you as a sister just as badly as Nee-chan wants you as a daughter, but I feel like there’s nothing either one of us can do to ever have you let us into your life that way."
    a "Why...would you want me as a sister? What do I bring to the table besides my dad?"
    n "Well, for one, it would be nice not secretly thinking you want to disembowel me all the time. But more than that...I don’t know."
    n "I just feel like we’re supposed to be closer than we are. Like it’s weird that we’re the same age and Akira is the one I’m attached to."
    n "Like, maybe if we met each other more when we were little, things would be different now? And I wouldn’t be as afraid of you as...as I am."
    a "..."
    n "See? That. That...blank stare. I never know what you’re thinking. I never know if things are going well when I talk to you anymore. You’re just...I can’t tell what’s real and what’s not."
    a "That’s not your fault, Noriko. "

    play sound "slidedoor.mp3"

    a "I’ve just made too many mistakes to ever give away what I’m really feeling anymore. "

    scene nakayamaslimotrip34
    with dissolve

    a "But I’m glad you- wait."
    a "Dad?"

    scene nakayamaslimotrip36
    with fade

    s "Hello."
    n "..."
    a "..."

    scene nakayamaslimotrip35
    with hpunch

    n "N-N-NII-CHAN?!?!?! WHAT ARE YOU DOING HERE?! I TOLD YOU THAT THIS NEEDED TO BE A STEALTH OPERATION AND YOU’RE JUST BARGING IN?!"
    s "Yeah. I’m not good at stealth."
    n "SO YOU OPEN UP THE POSSIBILITY FOR ME TO BE SACRIFICED TO A DEMON?!"
    s "Oh, right. I forgot that was the penalty for this."
    a "Wait, I’m confused. Noriko, did you invite him? Because {i}I{/i} was going to invite him as soon as I had a chance. But-"
    ni "{i}I TOLD YOU, PATRICE! NO ICE! THERE’S LESS DRINK IF THERE’S ICE! SERIOUSLY, WHAT ARE YOU EVEN GOOD FOR?!{/i}"
    n "SAVE YOUR QUESTIONS! IT’S TIME TO HIDE!"

    play sound "doorslam.mp3"
    scene nakayamaslimotrip37 with flash

    n "AND NOW IT’S TIME TO DESTROY!"
    a "Yeah! How dare you accept Noriko’s invitation and not the one I wanted to make but haven't had the chance to yet!"
    a "Now it’s going to look like {i}she’s{/i} the one who wanted you here more and that’s simply not true!"
    s "Okay, sorry. But do you guys really need to pin me up against the wall to yell at me?"
    n "Of course we do! There’s no room in here!"

    play sound "static.mp3"
    scene nakayamaslimotrip38 with flash
    stop sound

    s "There’s tons of room. Just look. You don’t need to-"
    a "It’s so cramped in here!"
    n "Yeah! I can barely move!"
    s "{i}Seriously?{/i}"

    play sound "static.mp3"
    scene nakayamaslimotrip39 with flash
    stop sound

    n "Wait — shh. I don’t know how familiar you are with Nakayama Sister Law. But 19A-B-42L states-"
    a "Demon sacrifice. I know."
    n "You’ve been studying. I like it."
    a "{size=-1}Yeah, no problem. Now, can somebody explain to me what’s going on? Because it’s starting to look like you invited my dad here so you wouldn’t have to be the third wheel while Aunt Niki tries to bond with me.{/size}"
    n "No! I-"

    scene nakayamaslimotrip40
    with dissolve

    n "Oh. Actually, yeah. That’s exactly what happened."
    a "What the heck, Noriko?! There’s no way I’m going to be able to escape from your sister once she gets back! How am I supposed to live knowing my dad is so close but I can’t reach him?!"
    n "The same way you live knowing he’s boning my sister every night while you do your homework."
    a "By masturbating and wishing it was me instead?! Also, it's very bold of you to assume I do my homework!"

    scene nakayamaslimotrip41
    with dissolve

    n "I had to masturbate to them for {i}years,{/i} damn it! Don’t tell me you’re throwing in the towel already, weakling!"
    a "Aaaaah but it’s so hard! I can’t take it anymore!"
    n "Well, take it for a little while longer because now is {i}my{/i} time to shine, sister!"

    play sound "knock.mp3"
    scene nakayamaslimotrip42 with hpunch

    ni "{i}Noriko? Ami? Are you...both in there?{/i}"
    n "J...Just a second?! "
    a "Yeah! We’re...almost done!"
    ni "{i}.............{/i}"
    ni "{i}With what?{/i}"
    s "{i}Now look what you two have done.{/i}"

    scene nakayamaslimotrip43
    with dissolve

    n "{i}Us?! This is all your fault, Nii-chan! If you had only waited another ten minutes, you wouldn’t be getting assaulted right now and I wouldn’t be a sacrifice!{/i}"
    a "{i}Hah...{/i}I have an idea."
    a "All I ask..."

    scene black
    with dissolve2

    a "Is that you do not forget this sacrifice..."
    n "{i}Ami? Where are you-{/i}"
    a "The time has come...for Ami Arakawa..."
    a "To do something {i}good...{/i}"

    $ renpy.end_replay()
    $ amispring2 = True
    $ ami_love += 1
    $ noriko_love += 1

    "........."
    "......"
    "..."

    jump norikospring3

label amispring3:
    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    scene sky
    with dissolve3
    play music "youwerespring.mp3"

    "The next morning, Niki called off her photo-shoot."
    "The reason she gave to her manager and producers was, of course, something along the lines of just “not feeling well” since a breakup would likely be in violation of her contract."
    "So it’s rescheduled to next weekend instead now. And it’ll be the last calendar shoot she does before making an announcement that her career is coming to an end."
    "“Graduating” I think they call it in the idol world. So hey, at least {i}someone{/i} gets to since it’s not like any of the other girls I know will be doing that any time soon."
    "Ami and Noriko don’t know yet. In fact, I don’t think Noriko’s exchanged a single word with her sister since she walked in on us last night."

    scene amiridehome1
    with dissolve2

    "Which is probably why the ride back to town is so awkward. And why I’d probably jump out of this moving car right now if it weren’t for the fact that it would further traumatize Ami."
    "At least {i}she’s{/i} in a good mood. "
    "Though, I can’t imagine she will be for long as I fully intend to ruin that by pulling her aside once we’re home and asking her why she’d orchestrate such a dramatic takedown of a girl I thought she loved."
    "I imagine she’ll tell me it was for {i}my{/i} sake. Or that she wasn’t {i}trying{/i} to search for us last night — she just couldn’t come up with an excuse to stop {i}Niki{/i} from doing it."
    "Whatever the case, I’m mad at {i}her{/i} in addition to myself for playing some sort of role in this."
    "And, you know what? Fuck it. I’m mad at Niki too because she won’t even {i}look{/i} at me today. Which is entirely fair and {i}I{/i} wouldn’t look at me either, but I’m still mad."
    "She could at least have the courtesy to tell me to fuck off or something. But instead, the only one here I’m {i}not{/i} mad at is Noriko because {i}she{/i} didn’t do anything wrong."
    "I just also feel terrible for dragging her into this mess. But I’m sure if you asked her, she wouldn’t tell you she regrets it. Just that she regrets getting caught."
    "So...like me. Just not nearly as bad for obvious reasons."

    scene amiridehome2
    with dissolve

    a "So! How about we play a game to make this ride a little less quiet and a lot more fun? Anyone up for Shiritori? I’ll go first! Maguro!"
    s "Ami-"

    scene amiridehome3
    with dissolve

    a "Bzzzzzt! You needed to come up with a word that started with “ro,” Dad! Now, you’ve already been eliminated and it’s just us girls left."
    s "No, Ami. I just don’t think anyone wants to play Shiri-"
    n "Romaji."

    scene amiridehome4
    with dissolve

    a "Jitensha! "
    s "Okay. Fuck me, I guess."

    scene amiridehome5
    with dissolve

    a "Again? But you guys went at it for so long last night."
    n "Oh, cool. Ami broke the pattern so I win."

    scene amiridehome6
    with dissolve

    a "Ah, crap. "
    a "Way to go, Dad. She beats me in love. She beats me in boobs. And {i}now{/i} she beats me in Shiritori. I have literally nothing left."
    n "We can play again if you want. Beats sitting in awkward silence. "

    scene amiridehome7
    with dissolve

    a "Mame."
    n "Megami."
    a "Minato."
    n "Tomato."
    a "Toma- "

    scene amiridehome8
    with dissolve

    a "Crap!"
    n "I think you just suck at this game, Ami. Want to play something else instead?"

    scene amiridehome9
    with dissolve

    a "Sure! What do you have in mind?"
    n "Hmm...let’s see...{i}let’s see...{/i}"

    scene black
    with dissolve2

    n "Oh! I brought Karuta! Nii-chan, can you slide over? I need to get my bag."
    a "Karuta? I haven’t played that in forever. I’m not even sure I remember how."
    n "Nee-chan taught me, so I will pass down the mystic art to you! Onii-chan, do you want to-"
    s "No..."
    s "But you two have fun..."

    "........."
    "......"
    "..."

    scene amiridehome10
    with dissolve2

    "After what can only be described as the longest drive of my life, we make it back to the house and Niki-"

    ni "I’m taking the bed. Don’t come in."

    scene amiridehome11
    with dissolve

    "...Avoids me, as expected."
    "That’s fine, though. I can sleep on the couch instead. And besides, it’s not like I got even a minute of sleep last night, so anywhere is fine right now."
    "I’ll just...leave her alone."
    "I can do that, right?"

    n "{i}Yikes...{/i}"
    s "Yeah. Turns out girls don’t like it very much when you have sex with their sister instead of them."

    play sound "static.mp3"
    scene amiridehome12 with flash
    stop sound

    a "I mean, I {i}also{/i} don’t like that you had sex with Noriko. But you don’t see {i}me{/i} avoiding you because of it. Maybe Aunt Niki’s just in a bad mood today?"
    s "Shut up, Ami. Just...please shut up."
    a "Wow. Maybe {i}you’re{/i} in a bad mood too, Dad."
    n "Hahah...hah...I, uhh..."

    scene amiridehome13
    with dissolve

    n "I should probably {i}go.{/i} I imagine you guys, uhh...want some space today."
    n "But, uhh...call me? Is it...weird for me to say that now? I am in a...rather unique and new situation all of a sudden."
    a "Later, Noriko. Thanks for fucking my dad and teaching me how to play Karuta."

    scene amiridehome14
    with dissolve

    n "Chk, chk! Any time, sis!"
    a "Okay. Tone it down, please."

    scene amiridehome15
    with dissolve
    play sound "dooropen.mp3"

    n "I am so sorry you had to see that."
    a "It’s okay! Bye, Noriko!"
    n "Bye, Ami! Bye, Nii-chan! Thanks for...all the sex!"

    play sound "doorslam.mp3"
    with hpunch

    n "{i}GYAAAAAAAH! WHAT AM I DOING?! BE NORMAL, NORIKO! JUST BE NORMAL!{/i}"
    a "Hahah! Oh, Noriko. Look at how happy she is now that she’s finally gotten what she-"

    stop music fadeout 10.0

    s "Ami. A word, please? In private."

    scene amiridehome16
    with dissolve

    a "But we’re already {i}in{/i} private, Dad. This is our house. It’s the only the place in the world where the two of us can-"
    s "In your room. Now."
    a "My room? But-"
    s "Ami...{i}now.{/i}"

    scene black
    with dissolve2

    a "Jeez, Dad. All you had to do was say “please.” You know I can’t say no to you when you do that."

    play sound "static.mp3"
    scene amiridehome17 with flash
    stop sound

    a "Not like I’d ever want to anyway, though. You always know what’s best for me after all! And I mean, of {i}course{/i} that’s the case given how long we-"
    s "Did you help Niki come find us last night?"

    scene amiridehome18
    with dissolve

    a "Hm? Yeah. "
    s "Ami-"
    a "But {i}she’s{/i} the one who figured out you were there. And I can imagine you saw it coming since I’m clearly not the type to engage in lesbian sex with anyone."
    a "It was a terrible lie. But I saw it through to the end for your sake, Dad. I could only hold her off for so long."
    s "But you helped her...You knew I was alone with Noriko, and you helped Niki find us."
    a "...{i}Right.{/i} But how was {i}I{/i} supposed to know you two were having sex? Wasn’t that the first time?"
    s "Ami-"
    a "Sorry, why am {i}I{/i} somehow in trouble for you having sex with your girlfriend’s little sister? Is this some kind of roleplay thing? Did you put your dad-pants on this morning?"
    s "Why are you not upset?...You {i}see{/i} how much she’s hurting, don’t you? Do you have any idea what this means for me and her? Don’t you {i}like{/i} her?"

    scene amiridehome19
    with dissolve

    a "Of course I like her, Dad! Aunt Niki’s done so much for both of us. I love her with all of my heart. "
    a "But at the same time, don’t you guys think you might be overreacting a little bit? Like, is it really so bad that she just saw you being yourself? She was gonna find out eventually."
    s "Yes, {i}eventually.{/i} Organically. Not at the behest of my jealous daughter and her need to always be involved in every facet of my life."

    scene amiridehome20
    with dissolve

    if amifingered == True:
        a "You seem quite mad at me, Father. Perhaps a blowjob is in order?"
        s "No, Ami. I don’t want a fucking {i}blowjob.{/i} I want you to stay out of my private affairs and-"
    else:
        a "You seem quite mad at me, Father. Come closer. I will hug you until you’re feeling better."
        s "I don’t want a fucking hug, Ami. I want you to stay out of my private affairs and-"

    a "And what? Let you torpedo your life all on your own? Got it. It’s not {i}my{/i} fault you fucked Noriko and broke Niki’s heart. Don’t blame {i}me{/i} for that."
    s "You {i}helped{/i} her! And I don’t know what you two were talking about before you found us, but something tells me it wasn’t exactly wholesome."

    scene amiridehome21
    with dissolve

    a "It was {i}very{/i} wholesome, actually. Aunt Niki and I had a really long heart-to-heart in the bath about how much we love you and how we’re both so desperate to make you happy."
    a "I even got to talk about my mom. "
    a "And for a second, it almost felt like she was there with us, giving Niki her blessing while patting me on the head and thanking me for taking such good care of you."

    scene amiridehome22
    with dissolve

    a "Which...makes it so much sadder that Aunt Niki’s going to move out now. I was just starting to really like having her around too. This trip was a turning point for us I think. And now that she’s-"
    s "Niki isn’t moving out."

    scene amiridehome23
    $ renpy.pause(5, hard=True)

    s "..."
    a "What?"
    s "..."

    scene amiridehome24
    with dissolve

    a "What do you mean she isn’t moving out?"
    s "I mean she’s going to stay here. We’re just...not going to be spending much time together."
    a "Then...why is she staying here?"
    s "Convenience? Maybe for {i}you?{/i}"
    a "For me."
    s "Maybe. She didn’t give me a reason. {i}I{/i} thought she was moving out too. But she told me she was going to stay."
    a "So..."
    a "You fuck her little sister right in front of her...for {i}five{/i} hours..."
    a "And she’s still going to live with us?"
    s "That’s right...she’s not leaving just yet."
    a "Is she a fucking idiot?"
    s "Ami...that’s-"

    scene amiridehome25
    with dissolve

    a "You FUCK her little sister..."

    scene amiridehome26
    with dissolve

    a "For FIVE fucking hours..."
    a "And {i}you’re{/i} telling {i}me{/i} that she’s just going to {i}stay.{/i}"
    s "Is there a problem with that, Ami?"

    scene amiridehome27
    with dissolve

    a "Oh, no! Not at all, Dad! "
    a "In fact, I think it’s {i}great{/i} living under the same roof as someone so open-minded! It makes me so extremely curious about which one of my classmates you’re going to fuck in front of her next!"
    a "Boy, I sure do hope it’s me!"

    scene black
    with dissolve2
    $ renpy.pause(1, hard=True)
    scene amiridehome28
    with dissolve2

    s "So {i}that’s{/i} why you were smiling all morning...You thought she was leaving."
    a "Oh, {i}forgive me{/i} for wanting my life back! {i}You’re{/i} the one who invited her here! Not me!"
    s "You were smiling when you interrupted Maya and me the other night as well."
    a "Mhm! I {i}did{/i} offer to watch, though. So it’s not like I’m {i}evil,{/i} is it?"
    s "..."

    play sound "static.mp3"
    scene amiridehome29 with flash
    stop sound
    play music "itsingsinitssleep.mp3"

    a "{i}Is it?...{/i}"

    "I look down at her, but I do not see my daughter."
    "I see someone who looks like her...talks like her...smells like her...but {i}my{/i} daughter wishes for nothing but my happiness. "
    "And this girl wants to hurt me."

    s "..."
    a "You have no idea how much I do for you...do you, Dad?"
    s "You’ve always done everything for me, Ami...but that doesn’t give you the right to toy with the people I love and-"
    a "Oh, no. No, no, no. I’m not talking about cooking...or {i}cleaning...{/i}or filing your fucking {i}taxes.{/i} I am talking about everything {i}else.{/i} The things I do that you don’t see."
    s "Well, then how the fuck would I know about them, Ami?"

    play sound "static.mp3"
    scene amiridehome30 with flash
    stop sound

    a "YOU WOULDN’T! THAT’S THE FUCKING POINT!"
    a "So when I ask you if you have any idea how much I do for you, the answer is obviously no! “No, Ami! I don’t know what you do! But thank you! I love you! Yours truly, Father!”"
    s "Fine! Sure! But either way, the fact that you’re running around and praying for the downfall of the people I love-"
    a "Don’t fucking talk to {i}me{/i} about praying, Dad! Not even as a figure of speech! I will not lose {i}you{/i} to some fucking worthless God as well!"

    play sound "static.mp3"
    scene amiridehome31 with flash
    stop sound

    s "What the fuck is {i}that{/i} supposed to mean?! Who else have you lost to-"

    play sound "static.mp3"
    scene amiridehome32 with flash
    stop sound

    a "YOU KNOW EXACTLY WHO I LOST! "
    a "YOU SAW WHAT WAS HAPPENING TO HER AND YOU IGNORED IT! YOU WERE THE ONLY ONE SHE TRUSTED AND YOU DIDN’T FUCKING LISTEN! YOU LET IT CONSUME HER!"

    play sound "static.mp3"
    scene hydrangeafield2 with flash
    scene imissyoumore with flash
    scene amiridehome33 with flash
    stop sound

    a "POEM AFTER POEM AFTER POEM! VOICES, VOICES, VOICES! IT’S NO WONDER SHE COULDN’T BREATHE WITH A NOOSE LIKE THAT AROUND HER NECK!!"
    s "Your mom...died in an accident, Ami..."
    s "She didn’t-"

    play sound "static.mp3"
    scene amiridehome34 with flash
    stop sound

    a "I know how she fucking died! But she was {i}practically{/i} dead for a whole fucking year before that while her mind was being overrun by who the fuck {i}knows{/i} what!"
    a "And {i}you{/i} could have done something! {i}You{/i} could have listened! Because I know you read the poems! But you didn’t understand them! You didn’t believe them! No one did!"
    s "..............."

    scene amiridehome35
    with dissolve2

    a "And I...how am I supposed to think you’ll believe {i}me{/i} then? "
    a "I don’t {i}blame{/i} you for the fact that she’s gone. I just...when I think about how {i}scared{/i} she must have been that last year...I can’t take it..."
    a "I can’t take it..."

    play sound "static.mp3"
    scene yourname with flash
    scene smileex with flash
    scene anormaldoor with flash
    scene amiridehome36 with flash
    stop sound

    a "AAAAAAAAHHHHH! I CAN’T TAKE IT! IT HURTS TOO MUCH! "

    play sound "static.mp3"
    scene amiridehome37 with flash
    stop sound

    a "AND NOW YOU HATE ME TOO?! I HAVE NO HAIR LEFT TO CUT OFF! I WAS ONLY DOING WHAT I HAD TO!"
    s "So what?...You {i}had{/i} to get Niki out of the house? "
    s "Will {i}that{/i} bring your mom back, Ami? Is {i}that{/i} what you want?"

    play sound "static.mp3"
    scene amiridehome38 with flash
    stop sound

    a "Don’t fucking talk to me like that..."

    scene amiridehome39
    with dissolve

    a "{b}I will NOT let you TALK to me like THAT! Not with everything I have to endure for YOUR SAKE!{/b} "
    s "Ami..."

    play sound "static.mp3"
    scene amiridehome40 with flash
    stop sound

    s "What {i}happened{/i} to you?..."
    a "What {i}HAPPENED{/i} to me?!"

    play sound "static.mp3"
    scene amiridehome41 with flash
    stop sound

    a "{b}{i}YOU{/i} DID! {i}YOU{/i} happened to me! I’m like this because of {i}YOU!{/i}{/b}"

    play sound "static.mp3"
    scene amiridehome42 with flash
    stop sound

    a "And you fucking KNOW it because it’s the only GOD DAMN FUCKING REASON you will let me call you “Dad” now!"
    a "Do you have ANY idea how fucking HARD it is for a seven year old to raise TWO PEOPLE when you’re in your fucking THIRTIES and can’t even raise YOURSELF?!"
    a "But now I’M the bad guy because you lost something you never deserved and need someone to BLAME?! I DID NOTHING! "
    s "You wanted her gone..."
    a "{b}{size=+10}YOU’RE DAMN FUCKING RIGHT I DID!{/size}{/b}"
    a "BECAUSE DESPITE ALL OF THAT! DESPITE THE PAIN AND TORTURE AND NEVER KNOWING IF YOU WILL EVER TRULY UNDERSTAND THE SHEER GRAVITY OF WHAT I DO FOR YOU..."
    a "DESPITE KNOWING THAT THE LAST YEAR OF MY MOM’S LIFE IS THE ONE THING YOU’LL NEVER STOP SUPPRESSING..."

    scene amiridehome43
    with dissolve2

    a "Despite all of that..."
    a "I have never stopped living for {i}you.{/i}"
    a "The one thing I have left."
    a "But sometimes?..."
    a "I feel like you’d be happier if I died too."
    s "....................."
    a "And there’s only one way to find out if that’s true or not."
    s "Ami-"
    a "Don’t follow me."
    a "I want to be alone."

    scene amiridehome44
    with dissolve
    play sound "footsteps.mp3"

    s "Can you at least tell me where you’re going?"
    a "Somewhere I won’t be a fucking {i}burden{/i} anymore!"
    s "Ami-"

    play sound "doorslam.mp3"
    scene amiridehome45 with hpunch
    $ renpy.pause(10, hard=True)

    "I kept thinking to myself — as I stood there in a room a little girl decorated without my help — that there was no way Niki could hear all of this and not come in to tell me things will be okay."
    "But she didn’t."
    "So I stood there for the next half hour, wondering how to make love stay. But there was nothing I came up with that didn’t immediately make things worse."
    "Now she’s gone. And Ami’s gone. And not even the ghost is here to poke fun at how badly I’ve fucked everything up this time."
    "And sure, there are places for me to go..."

    stop music fadeout 10.0

    "Other people who’d be happy to {i}help{/i} me right now..."
    "But I’m too scared to call them."
    "I just miss my daughter."
    "I miss my childhood friend."
    "And I’ve only been alone for thirty minutes."

    scene black
    with dissolve2

    "I lie down in Ami’s bed. And when I close my eyes, I can almost trick myself into believing she’s still here."
    "But despite having stayed awake all night, I’m unable to fall asleep. I feel like I don’t deserve this bed. "
    "Or her."
    "Or any of this."
    "But there is a closet-"
    "Propped open by a school bag with a notebook sticking out."
    "And for some reason-"
    "I think I’ll be able to sleep in there."

    $ renpy.end_replay()
    $ amispring3 = True
    $ amiblock = True
    $ noriko_love += 1

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "{i}Everyone else has abandoned you...{/i}"
    "........."
    "......"
    "..."

    jump yukispring5
