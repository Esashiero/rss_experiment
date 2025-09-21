label oldrwc:
    play sound "static.mp3"

    if bonus == True:
        show happyroom
        with flash
    else:
        show happyroomsafe
        with flash

    play music "amiasleep.mp3"
    stop sound

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
    "I wake up in a room with clocks."
    "I wonder how I got here?"

    s "..."

    "There is a girl in the corner of the room, standing still and staring straight ahead."
    "It’s quiet enough that I can hear her shallow breaths reverberate and bounce off of the walls."
    "She looks vaguely familiar."
    "Where have I seen her before?"

    six "Welcome to the edge of the world."
    six "I’m glad you found the time to visit."
    s "Do...I know you?"
    six "..."

    play sound "static.mp3"

    if bonus == True:
        scene happyroomhang
        with flash
    else:
        scene happyroomhangsafe
        with flash

    stop sound

    "The girl becomes an ornament."
    "The kind you want to hang on a Christmas tree."
    "I try to reach out to her, but my hands are tied to a chair."
    "I struggle to break them free to no avail."

    six "Welcome to the edge of the world."
    six "There is something buried underneath your feet."
    s "Oh, I thought you were dead."
    s "Is it hard to breathe like that?"
    six "No harder than it normally is."
    s "I see."

    "The {s}three{/s} two of us spend the next few minutes getting to know one another."
    "My favorite song comes on."

    play sound "static.mp3"
    play music "sweetvermouth.mp3"
    stop sound
    "///////////////PLAY SWEETVERMOUTH.MP3"

    "That’s more like it."

    six "つかれた。つかれた。つかれた。つかれた。つかれた。つかれた。"

    s "Me too, 61 6d 20 69 20 6f 6b 61 79."

    "A guy I knew in [high_school] suddenly died one day when his teeth melted and slid to the back of his throat."
    "The enamel rehardened, blocking his airway and causing him to suffocate."
    "It happened at summer camp while the rest of us were sleeping."
    "That was the first corpse I ever saw."

    play sound "static.mp3"

    if bonus == True:
        show happyroomsmile
        with flash
    else:
        show happyroomsmilesafe
        with flash

    stop sound

    play music "amiasleep.mp3"

    six "こんばんは。"
    s "You look much nicer up close."
    six "Welcome to the edge of the world."
    six "There is something buried underneath your feet."
    s "Can you tell me what it is?"
    six "笑笑笑笑笑笑笑笑笑笑笑笑笑笑笑笑笑"
    s "You’re going to have to speak a little louder."

    play sound "static.mp3"

    if bonus == True:
        scene happyroomstandonwall
        with flash
    else:
        scene happyroomstandonwallsafe
        with flash

    stop sound

    "Like a spider, the girl swiftly moves across the wall, somehow managing to not knock any of the clocks off."
    "A remarkable talent, that is."

    six "Welcome to {s}sssssssssssssssssssssssss{/s}"
    six "There is something buried underneath your feet."

    "Which door do I want to knock on?"

    menu:
        "God":
            play sound "knock.mp3"

        "Is":
            play sound "knock.mp3"

        "Dead":
            play sound "knock.mp3"

    s "{b}[[Redacted]{/b}, are you in there?"

    "..."
    "There’s no answer."

    scene black
    with dissolve2

    "{i}Congratulations! Your affection with EVERYONE has increased to 100!{/i}"
    "{i}Congratulations! You have discovered HM02!{/i}"
    "{i}You can now teach {b}Fly{/b} to one of the students!{/i}"
    "{i}Who would you like to teach {b}Fly{/b} to?{/i}"

    play sound "static.mp3"

    if bonus == True:
        scene happyroomhang
        with flash
    else:
        scene happyroomhangsafe
        with flash

    stop sound

    "A mysterious hand appears and injects the HM into my thigh."

    if bonus == True:
        "I get an erection for some reason."

    six "There is something buried underneath your feet."
    six "There is something buried underneath your feet."
    six "There is something buried underneath your feet."
    six "There is something buried underneath your feet."
    six "ああああああああああああああああああああああああああああああああああああ"
    s "Shh...It’s going to be okay."
    s "You don’t need to be scared anymore."

    if bonus == True:
        scene happyroomhanggone
        with dissolve
    else:
        scene happyroomhanggonesafe
        with dissolve

    "The body disappears."

    if bonus == True:
        scene happyroomhang
        with dissolve
    else:
        scene happyroomhanggonesafe
        with dissolve

    "Then reappears."

    if bonus == True:
        scene happyroomhanggone
        with dissolve
    else:
        scene happyroomhanggonesafe
        with dissolve

    "Then disappears again."

    if bonus == True:
        scene happyroomhang
        with dissolve
    else:
        scene happyroomhangsafe
        with dissolve

    "Then reappears."

    if bonus == True:
        scene happyroomhanggone
        with dissolve
    else:
        scene happyroomhanggonesafe
        with dissolve

    "This goes on for hours."

    if bonus == True:
        scene happyroomhang
        with dissolve
    else:
        scene happyroomhangsafe
        with dissolve

    "Eventually, I can feel the blood in my body begin to slow down."

    if bonus == True:
        scene happyroomhanggone
        with dissolve
    else:
        scene happyroomhanggonesafe
        with dissolve

    "My teeth melt and slide to the back of my throat."

    scene black
    with dissolve
    stop music fadeout 3.0

    "I suffocate."
    "I die."
    "//////////////REcoorDinating"
    "/////////Please stand by as system reboots"
    "////////////////////////roomwithclocks = False"
    "///////////////totaldays = False"
    "/////////////////Happiness = True"
    play music "sweetvermouth.mp3"
    "///////Play “Sweetvermouth.mp3”"
    "////////////System restart in 10..."
    "///////////9"
    "///////////8"
    "///////////7"
    "///////////6"
    "///////////5"
    "///////////4"
    "///////////3"
    "///////////2"
    "///////////1"
    "{i}Your affection levels have been returned to their normal state.{/i}"
    "{i}Please forget what you saw here.{/i}"

    stop music fadeout 5.0

    "........."
    "......"
    "..."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label thechuscene:
    play sound "dooropen.mp3"

    scene ayanebr1
    with dissolve

    s "..."
    ay "..."

    "That’s odd. I could have sworn I locked the door..."
    "Do locked doors just not register in this world or something?"

    play music "asobeatsex1.mp3" fadein 3.0

    ay "Sensei...What are you doing in here?"
    s "You...know I live here, right?"
    ay "No, well, yes. I mean. Yes, I know that you live here."
    ay "But like-"
    ay "Uhh..."
    s "I was about to take a bath. You’re welcome to join if you’d like."
    ay "I’m- what? Wait, really? You wouldn’t mind?"
    s "I wouldn’t. I can’t really speak for the other two, though."
    ay "Other two?"
    s "Aren’t you having a sleepover with Ami and Maya?"
    ay "...Oooooh. Yeahhh. Those two. Uh-huh..."
    ay "..."
    s "..."

    scene ayanebr2
    with dissolve

    ay "{i}Holy heck...{/i}"
    s "You’re uhh, staring pretty intensely, aren’t you?"
    ay "I’m...what?"

    scene ayanebr5
    with dissolve

    s "You’ve been staring at my dick since you walked in here."
    ay "Oh...Right. I guess I have been."
    ay "..."

    scene ayanebr4

    ay "It’s really big."
    s "Thanks. It gets even bigger, you know."
    ay "Really? How much bigger?"
    s "Probably another couple inches."

    scene ayanebr3

    ay "..."
    ay "Woooow..."
    ay "It’s my first time seeing one in real life."
    s "Yeah. I can tell."
    s "You’re like a deer in headlights right now."

    scene ayanebr4

    ay "Has Ami seen it before?"

    "Do dreams count? Because if they do, she saw quite a bit of it this morning."

menu:
    "Yeah, she has":
        s "She has. We’ve lived together for a number of years. It was bound to happen eventually."
        s "You’re not the only person to ever walk in on me, you know."
        s "Just yesterday, I actually walked in on her while she was in the bath."
        ay "Really? What happened next?"
        s "She, uhh, yelled at me and kicked me out of the room."

        scene ayanebr3

        ay "That’s it? Nothing else happened?"
        s "Nope. That’s it."
        ay "I see..."
        s "..."

        scene ayanebr4

        ay "..."
        ay "I can't stop looking at it."

        jump ayanebr

    "No, she hasn't":
        s "Nope. Wouldn’t really be morally acceptable for me to flash my [niece]."
        ay "So...I’m the first one then?"

        "I guess...in this life, yeah?"

        s "Looks that way."
        ay "Wow...I’m..."

        scene ayanebr5

        ay "..."

        scene ayanebr4

        ay "I can’t stop looking at it..."

        jump ayanebr

label ayanebr:
    scene ayanebr4

    s "It’s okay. I really don’t mind. We’re both mature, right? Being naked like this isn’t much of a problem."

    scene ayanebr5

    ay "Mature..."

    scene ayanebr7

    ay "I mean, uh, of course we’re both mature. I don’t mind this at all."

    scene ayanebr6

    ay "Yup...Just a totally normal...really big...penis..."

    scene ayanebr7

    ay "Sooo...do you like, come here often and stuff?"
    s "Several times a day, actually."
    ay "I see, I see. Cool."

    "This has gotten so awkward that I can’t even form an erection."

    scene ayanebr6

    ay "Do you like...you know...touch it and stuff?"
    s "It would be pretty impossible to not touch it since it’s part of my body and whatnot."

    scene ayanebr8

    ay "Ahh, right. That would be kind of hard, wouldn’t it?"

    scene ayanebr9

    ay "You poor thing...having to carry something that big around all day."
    s "I’ve learned to live with it."

    scene ayanebr10

    ay "Heh~ I bet. I mean, of course I didn’t expect it to be small or anything."
    ay "But like-"

    scene ayanebr11

    ay "..."
    ay "Wow..."
    ay "Is it, uhh, getting kind of hot in here?"

    "This almost hurts to watch."

    s "Sure. Maybe a little, I guess."

    scene ayanebr12

    ay "You know, Sensei..."
    ay "I wouldn’t really mind...{i}giving you a hand{/i} from time to time..."
    ay "I mean, I’ve never really done anything before...but if it’s with you, I wouldn’t really mind."
    ay "In fact, I’ve been wanting to get closer to you for a while now."
    ay "And since we’re, uhh, both so {i}mature{/i} and stuff...I think it would be fine."
    s "Really? That would be a big help. Thanks, Ayane."
    s "I wouldn’t mind helping you out either."

    scene ayanebr7

    ay "Helping me out?"
    ay "...You mean?"
    s "I’m sure you know what I mean."
    s "After all, it wouldn’t be fair if I was the only person getting something out of this deal, would it?"

    scene ayanebr11

    ay "That’s right...Yeah. That wouldn’t be fair at all..."
    ay "..."
    ay "Mm..."
    s "You’re staring again."

    scene ayanebr13
    with dissolve

    ay "{i}There’s no way in hell that thing would fit inside of me...I can barely even fit two fingers in...{/i}"
    ay "{i}Mmn~ Just thinking about it is...{/i}"

    scene ayanebr14
    with dissolve

    ay "So umm...Yeah...You can help me out whenever you want."

    scene ayanebr16

    ay "Like I said, I’ve kind of liked you for a while now and..."
    s "We’d need to keep it a secret, though. Would that be okay with you?"

    scene ayanebr19

    ay "A secret? How come?"
    s "You really need to ask?"
    s "You’re best friends with my [niece], you’re one of my students, and not to mention-"

    scene ayanebr10

    ay "Right, right. Yeah, of course. I get it."
    ay "I’d feel horrible if anything happened to you because of me."
    s "I’m glad you understand."

    scene ayanebr11

    ay "A secret relationship with Sensei..."

    scene ayanebr18

    ay "I hope he’s okay with someone like me..."
    s "Ayane, you’re speaking out loud when I'm pretty sure you’re trying to have an inner monologue."

    scene ayanebr20

    ay "Huh? What? Oh, yeahhh. I knew that. Hahahah~"
    s "Whatever you say..."
    ay "Hey, umm, Sensei..."
    s "Yes?"
    ay "Would you mind if I like..."
    ay "You know..."

    scene ayanebr21

    ay "Touched it?"
    s "Go right ahead. Like I said, I don’t mind at all."
    s "You’re going to have to take responsibility if it gets any bigger, though."
    ay "Heh~ Right, right. Of course! I’ll gladly take...responsibility of..."

    scene ayanebr11

    ay "..."
    ay "Ngh~"

    scene ayanebr22
    with dissolve

    "Ayane slowly walks up to me and kneels down."
    "After observing my dick for a few moments, she carefully places her index finger on the head."

    s "You know you can do more than that, right?"

    scene ayanebr23

    ay "I know. I’m just warming myself up..."
    ay "Like I said, I’ve never seen one in real life before...let alone one this big."

    scene ayanebr22

    ay "And it’s even bigger up close..."
    ay "{i}It's actually kind of scary...{/i}"
    s "Well I’m glad you seem to be enjoying it."
    ay "It’s like...as big as my head..."

    scene ayanebr23

    ay "Hey, Sensei, do you feel weird knowing that one of your students is touching your penis right now?"
    s "I certainly feel something..."
    ay "Hehe~ I feel really naughty..."

    scene ayanebr26

    ay "Hey, umm...It might help me out a little if you were to like..."

    scene ayanebr24

    ay "Tell me what to do...and stuff..."

    "No surprise that Ayane is the submissive type. I’ve had her pegged that way since the moment we met."
    "This should be fun..."

    scene ayanebr25

    s "Okay. I’ll give you a few orders and you can do your best to act them out."
    s "If you need help, I can give you a few pointers, but I’ll expect you to get the hang of things quickly."

    scene ayanebr30

    ay "Sir, yes sir."
    s "Okay, so first, I’ll need you to-"

    play sound "knock.mp3"
    scene ayanebr26

    a "Ayane? You’ve been in there for a while. Is everything okay?"

    scene ayanebr27

    ay "Uhh, yeah! Everything is fine! I’ll be out in a minute!"
    a "Okay, if you say so!"
    a "Also, have you seen Sensei by chance? His shoes are here so I thought he might be-"
    ay "Nope! Maybe he went...out for a walk??"
    a "Without his shoes?..."
    ay "Uhhhh, men are strange!! What do you want me to tell you?!"
    a "Right...Well, we’ll be in my room whenever you’re done."
    ay "Okay! Thank you!"

    "..."

    ay "..."

    scene ayanebr28

    ay "Why must life be so miserable?"
    s "That’s just the way things are, I’m afraid..."

    scene ayanebr29

    ay "I...should probably get going then, huh?"

    "As much as I want her to stay, we’d be at risk of being discovered if she kept herself in here any longer."

    s "Unfortunately...I think so."

    scene ayanebr28

    ay "Ugh...We just got to the good part too..."
    s "It’s fine. I’m sure there will be other good parts."

    scene ayanebr30

    ay "I sure hope so. I want to see how much bigger this thing can get..."
    ay "Also, since we’re getting cut off early and stuff, I guess it wouldn’t hurt to give you a goodbye present."
    s "A goodbye present? What do you-"

    scene ayanebrx2
    with dissolve

    ay "Chu~"

    "Ayane’s soft lips press against the head of my cock."
    "I can feel myself beginning to get hard from the surprise attack."
    "Her hot breath provides a sensation I haven’t felt in god-knows-how long."

    scene ayanebrx3

    ay "I’m sorry I couldn’t do more to help you today...Will you ever forgive me?"
    s "...I suppose so. I’m going to need you to do that a few more times, though."
    ay "Sir, yes sir."

    scene ayanebrx2

    ay "Chu~ Ngh...Chu~"
    ay "Mmf..."
    ay "Chu~ Chu~ Chu~"

    "She batters my dick with kisses, keeping her eyes closed the entire time."
    "She’s surprisingly obedient for a girl who’s never seen a penis before."
    "Just how much does she like me?"

    scene ayanebrx3

    ay "Sensei, are you going to jerk off to this later?"
    s "Most likely, yes."
    ay "Heh~ Good..."
    ay "That makes me really happy..."
    ay "I...already think of you when I touch myself so..."

    scene ayanebrx2

    ay "Chu~"

    "Ayane kisses my dick one last time before getting off of the ground and shakily walking out of the bathroom."
    "I hope the other two don’t notice how red she’s gotten..."

    scene black
    with dissolve2
    stop music fadeout 3.0

    "........."
    "......"
    "..."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label day16old:
    scene black
    with dissolve

    "Time: 11:30 AM \n
    Location: Soccer Field \n
    Mission: Operation Fallen Angel"

    play music "happyandplotting.mp3"

    "..."

    scene ayanehurtadetermined
    with dissolve

    ay "Okay, Sana! Just like we practiced! Are you ready to do this?"

    scene ayanehurtsworried

    sa "Umm...I don’t really know if this is a good idea..."
    sa "Are you sure he isn’t going to notice?"

    scene ayanehurtadetermined

    ay "Of course I’m sure! We’ve rehearsed it plenty of times in the dorm room."
    ay "You’ve just gotta be really convincing with your acting and there’s NO WAY we can fail!"

    scene ayanehurtsworried

    sa "That sounds easier said than done..."

    scene ayanehurtadetermined

    ay "It’ll be fine! Don’t worry about it."

    play sound "whistle.mp3"

    scene soccerfield
    with dissolve

    s "Okay girls...Time to do that running thing or whatever it is you’re supposed to do for the next half hour."
    s "On my mark! Three...two-"

    sa "UHHH...OH NOOO! AYANE HAS FALLEN! THIS IS A TRULY TRAGIC EVENT!"
    s "...?"

    scene ayanehurtsact1
    with fade

    ay "Ow! It hurts so bad! I don’t think I can move it!"

    scene ayanehurtsact2
    with hpunch

    sa "SHE WILL NEVER WALK AGAIN!"

    scene ayanehurtsact1

    s "What’s going on? Are you okay, Ayane?"

    scene ayanehurtsact3

    ay "Sensei?...Is that you...Your voice sounds so...distant..."

    scene ayanehurtsact2
    with hpunch

    sa "THE LIGHT IS FADING FROM HER EYES!"
    s "Okay Sana, I’m going to need you to step aside for a moment."

    scene ayanehurtsact4

    sa "Oh...I’m sorry...I..."
    sa "Um..."
    sa "Bye, then..."

    scene ayanehurtsact5
    with dissolve

    s "What happened? You weren’t even supposed to start running yet."
    ay "I...I don’t know...One moment I was talking about the decline of our current economy and..."
    ay "The next thing I know...I can’t feel my legs..."
    ay "Sensei...am I going to die?"
    s "You’re not going to die."
    s "Here. I’ll carry you to the nurse’s office."
    ay "If...that is what you feel must be done...I suppose I have no choice..."

    scene ayanehurtsact6

    ay "I will...be in your hands..."

    scene ayanecarry
    with fade

    ay "Thank you Sensei...I know how heavy I must be..."
    s "You’re like 80lbs. You’re not heavy at all."
    ay "Of course you would say that...You’re a big strong man and I am but a frail [young]woman."
    s "Right..."
    ay "Sensei...what will I do if I can never walk again?"
    ay "Will you carry me everywhere for the rest of your life?"
    s "Uhh, I mean...I could push you around in a wheelchair from time to time."
    ay "I see...You truly are every bit as caring as I thought you were."

label fallenangelrep:
    scene black
    with dissolve

    play sound "dooropen.mp3"
    stop music fadeout 3.0

    scene nurseoffice
    with dissolve

    s "Hello? Is there a nurse around?"
    ay "Sensei...I’m afraid the nurse is not in on Fridays..."
    s "What kind of weird schedule is that? People can still get hurt on Fridays."
    ay "I think...you might need to take care of me yourself..."
    s "..."

    "Ah. So that's what’s going on here."

    s "Yup. It looks that way..."
    ay "Th-thank you, Sensei...I’ll be in your care..."

    play music "asobeatsex1.mp3" fadein 3.0

    scene black
    with dissolve

    "I carry Ayane through the curtains and lay her down on the bed."

    jump ayanenursex

label ayanenursex:
    scene ayanenurse1
    with dissolve

    ay "..."
    s "..."
    ay "Are you going to touch me?"
    s "Of course."
    s "Could you point out where it hurts?"
    ay "..."

    scene ayanenurse2
    with dissolve

    "Ayane points toward her legs. They tremble as she focuses everything she has on trying to remain calm."

    scene ayanenurse3
    with dissolve

    "She flinches slightly as my hand comes into contact with her skin."
    "It’s strange how she can insert herself into these situations without any
    hesitation at all but still acts nervous when they play out according to plan."

    s "Here? Is this where it hurts?"
    ay "..."
    ay "I think it’s a little higher..."
    s "Hmm."

    scene ayanenurse4
    with dissolve

    s "Here then?"
    ay "That’s closer...I think it still might be a {i}little{/i} higher up, though..."

    "I graze the soft skin of the inner thigh, tracing upward with the tips
    of my fingers until my hand rests just one layer above her most delicate spot."

    scene ayanenurse5
    with hpunch

    ay "Ah! Sensei!"
    s "This must be it based on how you jumped just now, right?"
    ay "R-Right...It hurts really bad...You’re going to need to do something about it..."
    ay "I don’t know how much more of this I can take..."
    s "Don’t worry, I’ll take care of it."

    "Gently, I begin tracing the outline of her slit with my index finger."
    "The entirety of her lower body shakes each time I move."

    s "Seems like you managed to get hurt in a very strange place."
    ay "Y-yes...What an...ahh...odd coincidence..."
    ay "What you’re doing...s-seems to be working, though..."
    ay "I’m...ahhh...starting to feel really good..."
    s "Then I guess I’ll keep going until you feel better."
    ay "P-please do..."

    scene ayanenurse6
    with dissolve

    "Carefully, I continue toying with her through the fabric of her gym bottoms."
    "I can feel a slight dampness begin to seep through them. "
    "I press down slightly harder in response, pushing my finger as close to entering
    her as I can through her shorts."

    ay "Ahn...Sensei...This...mmm...feels really good..."
    ay "It doesn't hurt at all anymore."
    s "Oh? Then should I stop?"

    scene ayanenurse7

    ay "What?!"
    ay "No way! Please keep going!"
    ay "If you stop right now, I really will die!"
    s "Hmm...Well, I definitely don’t want that."
    s "I’m not sure what else I can do while you have these on, though."

    scene ayanenurse8

    ay "...Huh?"
    s "What I'm saying is that it would probably feel a little better if we took your shorts off."
    ay "Um..."
    ay "Uhh..."
    ay "..."

    scene ayanenurse9

    ay "...Okay."
    s "Then..."

    scene ayanenurse10
    with dissolve

    "I slowly slide Ayane’s gym bottoms off of her and place them on the floor beside me."
    "Her pale skin, illuminated by the fluorescent light of the infirmary, is equal parts erotic
    and stunningly beautiful."
    "I want to corrupt her and protect her all at once."
    "Knowing that the rest of the students are just minutes away from us right now excites me even more."

    ay "Sensei...you can touch me more..."
    ay "If you want to, I mean..."

    "Heeding her call, I begin to trace her opening once again."

    scene ayanenurse11

    ay "AHNN! Oh my god...It’s...so different feeling it directly..."
    s "Good different or bad different?"
    ay "Good different! Very good different!"
    ay "I’m about to explode just thinking about it..."
    s "Wait, are you going to cum already? I’ve barely even done anything."

    "Testing her limits, I brush my finger against her clit and gauge her reaction."

    scene ayanenurse12
    with hpunch

    ay "AHHHHHHHMMMMNNN!!!!~~"

    "Ayane erupts in a brief fit of pleasure before losing control and convulsing in front of me."

    scene ayanenurse13

    ay "Hah...hah...I’m...so...sorry..."
    ay "I...didn’t think I would lose myself that quickly..."
    s "There’s no need to apologize."

    "Before she has a chance to recover, I begin to prod at her with one of my fingertips."

    scene ayanenurse14

    ay "...Huh? We're still going?"
    s "Maybe."

    "As soon as I finish my answer, I slide the rest inside of her and start exploring her pussy."

    scene ayanenurse14r
    with dissolve

    ay "Ah! Sensei! You...you put it inside!"
    s "Did you not want me to do that?"
    ay "N-no! I wanted it a lot!"
    ay "I’ve wanted it for a really long time!"
    ay "You’re really...inside of me right now..."
    s "It’s just a finger, you know."

    scene ayanenurse15

    ay "That’s right...But it’s {i}your{/i} finger. That’s why I’m so happy..."

    "What an awkward and strangely adorable line..."
    "Ayane really is cute, even if she’s a little weird and obnoxious at times."

    ay "I...mmm...didn’t think...you would ever do...AHH...something like this...to me..."
    ay "Hah...Hey...Sensei?..."
    ay "Sometimes...when I get really lonely...ahhh-"

    scene ayanenurse16

    ay "I close my eyes and..."
    ay "Touch myself down there...and..."
    ay "I kind of...you know...pretend it's you...or whatever..."
    s "Oh yeah? And how does that measure up to the real thing?"

    scene ayanenurse17

    ay "Not even close~ Hehehe..."

    "I gently start sliding my middle finger in and out of Ayane."
    "Knowing she’s still new to this (And very small), I decide to take it kind of easy on her."

    scene ayanenurse17r

    ay "Ah!! Oh god..."
    ay "I’m gonna...again...Mmm..."
    ay "Sensei!...Sen...sei!...SENSEI!! AHHHHH!!"

    scene ayanenurse18
    with hpunch

    ay "AHHHHHHHHHHH!!!!!!!!!!!~~~~~~~~~"

    "Ayane squeezes my wrist as tightly as she can and once again erupts under my spell."
    "And just like the last time, she nearly loses consciousness."

    scene ayanenurse18r

    ay "Hah...hah...ha...mmm...ahhh...huh...phew..."
    s "You’re looking a little exhausted, Ayane."
    ay "Hahaha...you...noticed?"

    scene ayanenurse19
    play sound "dooropen.mp3"
    "..."

    a "Sensei? Ayane? Is everything okay in there?"
    a "I was in the bathroom so I didn’t see it happen, but I heard from the other girls that Ayane fell down or something."
    a "Is that true? Is she gonna die?"
    ay "Ahh...I’m okay, Ami! Sensei is-"

    scene ayanenurse19r
    with hpunch

    "Curious to see how this situation plays out, I start fingering her even faster."

    ay "AHHH!!~"
    a "Oh my god, are you really okay? It sounds like you’re in a lot of pain."
    ay "I’m...AHHHH...I’m okay! I swear! I’ll be fine! Really!"
    a "...Are you sure?"
    a "Do you need me to come in there?"
    ay "AHHH! AHHH! No! No, please don’t!!"
    s "She’ll be okay. I’ve got it under control, Ami. Don’t worry."
    a "If you say so..."
    a "Alright well, I’ll be outside so just come back whenever things are better and stuff."

    play sound "dooropen.mp3"

    "..."

    scene ayanenurse17r
    with hpunch

    ay "AHHH!~~ SENSEI~~ MMMMNNNN!~~~"

    scene ayanenurse18

    ay "Hah......"

    "For the third time, Ayane falls victim to an intense orgasm. She’s so
    easy to please that it feels almost criminal."

    scene ayanenurse20

    ay "That was mean..."
    ay "What if she came in?"
    s "Then I guess we’d both have a lot of explaining to do."

    scene ayanenurse17

    ay "Heheh~ I guess we would..."

    scene black
    with dissolve
    stop music fadeout 5.0

    "Ayane basks in the afterglow of her pleasure for another minute or
    two before asking for her shorts back."
    "Honestly, I was hoping to have gotten something out of this as well, but I guess it can’t be helped."
    "We’ve already been away from the class for the majority of
    the period, and neither of us want to risk anyone else coming in here again."
    "So, the two of us get up, and I’m forced to fold my dick up into
    the waistband of my shorts to avoid everyone noticing my erection..."

    "........."
    "......"
    "..."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label amibathx:
    scene amibath1
    with dissolve

    play music "happyandplotting.mp3"
    a "..."
    a "{i}*Sigh...*{/i}"
    a "I wonder what’s going on with him..."

    play sound "knock.mp3"

    s "Ami? Are you almost done in there? It’s been a while."
    a "Could he really just be tired?"
    a "No...That can’t be it."
    a "He’d never forget me, no matter how tired he is."

    play sound "knock.mp3"

    s "Hey, are you okay? Did you drown?"
    a "Maybe he’ll be fine in the morning, then?"
    a "Yeah...That’s it. I’m sure everything will go back to normal soon."

    play sound "dooropen.mp3"

    "..."
    s "Oh. You’re alive."

    scene amibath2
    with dissolve

    a "Huh?..."

    "I stand in the doorway and stare at Ami. Her small, practically non-existent
    breasts peer over the water. I can’t help but focus on them."
    "Does she not realize I’m here or something?"
    "I mean, she and Sensei were technically family, so maybe
    something like this isn’t all that abnormal around here?"

    a "Weird...A hallucination?"
    a "Did I stay in the bath too long?"

    "Or maybe that’s not the case at all..."

    s "Yeah. You’ve been in here for almost an hour. I thought you died."
    a "Huh...Do hallucinations always talk?"
    s "I’m not a hallucination."
    a "Ooooooh...I see."

    scene amibath1
    with dissolve

    a "..."
    s "..."
    a "..."
    s "..."

    scene amibath3

    a "Wait-"
    a "Does that mean..."

    "Ami stares back at me for a moment before realizing that I’ve been
    fixated on her underdeveloped, naked body for going on several minutes now."

    scene amibath4

    a "W-WHAT ARE YOU DOING IN HERE?! CAN’T YOU SEE I’M BUSY?!"
    s "Like I said, I thought you died or something."
    a "HOW WOULD I DIE IN THE BATH?!"
    s "I don’t know. Maybe you slipped and cracked your head open or something."
    a "I DIDN’T! I’M TOTALLY FINE! NOW GET OUT!!"
    s "Okay...If you say so. Just hurry up in here."
    a "I WILL! JUST PLEASE LEAVE!!"

    scene black
    with dissolve

    scene lr_noon
    with dissolve

    "I move out of the bathroom and close the door behind me."
    "The image of Ami in the tub lingers in my mind for a moment
    and I can feel myself starting to get hard."
    "I wonder if it would technically qualify as [incest] if the two of us were to hook up?"
    "I mean, it's not like I'm {i}really{/i} her [uncle]..."
    "Sure, she might not exactly know that yet, but still."

    show amipshy
    with dissolve

    a "..."
    a "I thought I told you no peeking..."
    s "I knocked on the door but you didn’t answer. I thought something might have happened to you."
    a "Wait, you knocked?"
    s "Yeah, a few times actually."

    show amipembarrassed
    hide amipshy

    a "Oh...I see...I guess it’s not really your fault then..."
    s "Why do you seem so embarrassed? We’re family aren’t we?"

    show amipshy
    hide amipembarrassed

    a "Well, yeah...but..."

    show amipupset
    hide amipshy

    a "{i}I guess he wouldn’t think much of my stupid body anyway...{/i}"
    s "It’s fine. You can even walk around the house naked for all I care."

    "In fact, I more than welcome that idea."

    show amipxyell
    hide amipupset

    a "N-No way! I’d never do that! Not in a gazillion years!"

    show amipshy
    hide amipxyell

    a "Plus, wouldn’t that mean you'd be doing the same thing?...I don't know how I feel about that..."
    s "Not particularly. What if one of your friends or a staff member showed up at the house?"
    s "I could theoretically get in a lot of trouble being seen like that."

    show amipembarrassed
    hide amipshy

    a "Yeah...I guess that would be pretty bad, wouldn’t it?"

    show amipshy
    hide amipembarrassed

    a "But either way! I don’t want you seeing me like that! It makes me feel weird..."
    s "Weird? How so?"
    a "Like, my chest gets all tight and I’m suddenly super self-conscious and it makes me want to die and stuff..."
    s "Well, if it makes you feel any better, I think you’re absolutely adorable."

    show amipx
    hide amipshy

    a "That makes me feel even worse!"

    hide amipx
    with dissolve

    "Ami storms off into her room and slams the door behind her."

    a "I-I’ll make dinner while you’re in the bath! I just need to cool off for a few minutes!"

    "She’s clearly flustered. I’m assuming that’s the first time a boy has seen her naked since she was little."
    "I guess that teaches me something about her relationship with Sensei, though."
    "Even if the two of them were close, they weren’t up to anything unsavory."
    "That actually makes me feel kind of good, in a way. "
    "Ami’s innocence is one of the cutest things she has going for her, right next to the twintails."
    "It would be disheartening to
    find out that she’s secretly some sort of nymphomaniac."
    "Though, I can’t say I wouldn’t accept any advances...I’m only human, after all."

    scene bathroom_home
    with fade

    "I remove my clothes and get into the water Ami had been soaking in just moments ago."
    "Now...what am I going to do about this erection?"

    scene black
    with dissolve
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label day23:
    scene hall_day
    with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "It’s Friday and the girls are in the library for some study hall thing."
    "I was supposed to be in there with them about ten minutes ago, but I was a little
    preoccupied searching for a vending machine."
    "Did you know that even though this[school] has around four hundred
    students, there are only three vending machines here?"
    "How ridiculous is that?"
    "I’m going to have to put in a complaint letter or something."

    scene black
    with dissolve

    play sound "dooropen.mp3"

    s "Okay, I’m here. Sorry for being late again."
    r "Oh, Sensei! Over here."

    scene studytime1
    with dissolve

    s "Hey. Where did everybody else go?"
    f "They left when you didn’t show up..."
    r "Forget about them, Sensei. We need your help."
    s "With what?"
    r "Okay, so-"

    scene studytime2
    with dissolve

    jump maleanatx

label maleanatx:
    r "We need you to tell us everything you know about the male anatomy."
    s "..."
    s "Everything?"
    r "Well, everything that’s going to be on the anatomy test."
    f "Rin...I don’t know if Sensei is comfortable with-"
    s "Sure. Where do you want me to start?"

    scene studytime3
    with dissolve

    r "I knew we could count on you!"
    r "Since you’re the only guy in the entire[school], I figured that studying
    the topic with you would give us a serious leg up on the competition."

    scene studytime4
    with dissolve

    f "Oh god...I’m feeling really light-headed all of a sudden..."

    scene studytime5
    with dissolve

    r "Dude, chill. You’re going to be fine."
    r "Plus, now you can ask Sensei anything you want about male bodies and stuff!"

    scene studytime6
    with dissolve

    r "Sensei, you’re not going to be weird or anything, right? As you can see, Futaba
    is a little shy when it comes to this stuff."
    f "I think I’m going to pass out..."
    s "I won’t be weird at all. I’m your teacher, so it’s totally fine to ask things like this."

    scene studytime7
    with dissolve

    f "Th-then...I guess...that’s okay..."
    r "Okay! So, first question..."

    "Rin points her finger down at a diagram of the male genitalia in her textbook."

    r "Is this bigger or smaller than a normal one?"
    s "That question can’t possibly be on the test, can it?"
    r "Who knows?"

    scene studytime8
    with dissolve

    f "Rin! You asked Sensei if he was going to be weird but now you’re the one being weird!"

    scene studytime9
    with dissolve

    r "What do you mean? You literally just said you wanted to know if-"

    scene studytime10
    with dissolve

    f "I said nothing of the sort!"

    scene studytime7
    with dissolve

    f "S-Sensei! What we really need to know is the...umm...layout...of all the parts and stuff."
    r "Right. Yeah, that. For some reason, somebody scribbled out the names of
    everything in both of our textbooks!"
    r "How weird is that?"
    s "Very weird."
    s "Here, let me have a look."

    scene studytime11
    with dissolve

    "Futaba hesitantly slides her textbook over to me and I begin pointing out the different sections of the male genitalia."

    s "Well, this thing here is obviously the penis."
    f "R-right...The...p-p-penis...What we’re confused about is-"
    r "We basically have no idea what all the inside parts are called."
    r "Like all the stuff connected to the balls or whatever."
    s "Rin, you are surprisingly casual about all of this."
    "I slide Futaba's textbook back to her"

    scene studytime12
    with dissolve

    r "Why wouldn’t I be? It’s just a drawing. It’s not like it’s a real person or whatever."

    scene studytime13
    with dissolve

    f "R-real..."
    s "I guess that’s a fair point."
    s "Here, I’ll go through each part’s name and function with you..."

    scene studytime7
    with dissolve

    "I spend the next ten minutes describing the male reproductive system to Rin and Futaba."
    "Rin pays noticeably more attention to this topic than she does in normal class
    while, Futaba on the other hand..."
    "I think she’s having a hard enough time just staying conscious."

    s "And that’s basically everything you need to know. Any questions?"
    r "Hmm...Nope! I think I’m good!"

    scene studytime9
    with dissolve

    r "How about you, Futaba? Are you also a master of the male body now?"
    f "M-master?..."
    s "Like I said, if you have any questions at all, I’m happy to help."

    "{i}I also wouldn’t mind giving you a more visual demonstration.{/i}"

    scene studytime13
    with dissolve

    f "Umm...I...think that’s about everything I need to know..."

    scene studytime14
    with dissolve

    r "Really? Because before you were saying-"

    scene studytime15
    with dissolve

    f "THAT'S EVERYTHING! THANK YOU FOR YOUR HELP, SENSEI!"
    f "I’m...going to go to the restroom now!"

    scene studytime16
    with dissolve

    "..."

    r "Woah...She normally doesn’t yell like that."
    s "Yeah, that was a little surprising. I get it, though."
    s "Learning about this stuff can definitely be a little awkward for people who
    haven’t really been exposed to it."
    r "Nahh. It’s only awkward if you make it awkward."

    scene studytime17
    with dissolve

    r "Look at me! I’m totally cool right now."

    scene studytime18
    with dissolve

    r "I...should probably go make sure Futaba is okay, though."

    scene studytime17
    with dissolve

    r "But thanks again for all your help, Sensei! You’re a real lifesaver."
    r "Next drink at the cafe is on me, okay?"

    if firsttimecafe == True:
        s "Oh, awesome. Hopefully you’ll actually make my order this time."
        r "Heheh~ We’ll see!"

    if firsttimecafe == False:
        s "Oh really? I’ll have to drop by sometime. Thanks, Rin."
        r "Any time~!"

    scene studytime0
    with dissolve

    "Rin leaves as well and suddenly I’m all alone in the library..."

    scene black
    with dissolve
    stop music fadeout 5.0

    "The two of them don’t come back for the rest of the period and the
    [school] day ends without much else happening..."

    "........."
    "......"
    "..."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label makotodorm10:
    scene black
    with dissolve
    play sound "knock.mp3"

    "I knock on Makoto’s door, hoping she’s still awake."
    "I’m not really sure what her sleeping schedule is, but I’m here later than
    normal and she seems like the type to go to bed early."
    "Miku, on the other hand, I can imagine being up all night long."
    "So I guess I can just hang out with her if Makoto’s in bed already."

    mak "The door’s open! Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

    scene makotodorm
    with dissolve
    show makotopsmile
    with dissolve

    mak "So, to what do I owe this-"

    show makotopembarrassed
    hide makotopsmile

    mak "Wait, Sensei?! What are you doing here so late?"
    s "I was wondering why you just let me walk in."
    mak "I thought you were one of the girls..."
    s "Yeah, I figured as much. You look really cute in your pajamas."

    show makotopshysmile
    hide makotopembarrassed

    mak "Really?...You think s-"

    show makotopembarrassed
    hide makotopshysmile

    mak "Hey, wait a second! Don’t try to distract me like that! You need to get out of here!"
    s "Why?"
    mak "Because it’s late...and someone might get the wrong idea if they saw you come in."

    jump makotomassx

label makotomassx:
    s "So what? It doesn’t really bother me if people think we’re up to something."

    s "Besides, you’ve already given me a handjob so it’s not like you have anything to
    be embarrassed about at this point."

    show makotopangry
    hide makotopembarrassed

    mak "Wait..."
    mak "Don’t tell me that’s why you’re here tonight?..."
    mak "You don’t think you can just ask me to do something like that whenever you want, do you?"
    s "Of course not. I haven’t even unlocked your Lust stat yet."

    show makotopconfused
    hide makotopangry

    mak "My...what?"
    s "Never mind that. I just wanted to see what you were up
    to. I was kind of worried you’d be asleep already."
    s "Also, where’s Miku at? Should we be worried?"

    show makotopsmile
    hide makotopconfused

    mak "No need to be worried. Miku is staying with some girls
    from her team tonight. She won’t be home until tomorrow."
    s "So the two of us have the entire night together?"

    show makotopwink
    hide makotopsmile

    mak "We most certainly do not. But I guess it wouldn’t hurt
    if you wanted to stick around for a {i}little{/i} while."

    show makotopshysmile
    hide makotopwink

    mak "No one...saw you come in, did they?"

    if day == 6 or day == 7:
        s "Nope. We’re in the clear."
        mak "Okay...just making sure."
    else:
        s "..."

        show makotopembarrassed
        hide makotopshysmile

        mak "..."
        s "..."

        show makotopexhausted
        hide makotopembarrassed

        mak "Ugh...how am I going to explain this?"
        s "Just tell them we were going over[school] stuff."
        mak "It’s so late, though...they’ll never believe that..."

    show makotopnormal
    hide makotopexhausted
    hide makotopshysmile

    mak "Anyway, do you want some coffee or anything? I just made a fresh pot."
    s "Why are you making coffee this late? Aren’t you going to bed soon?"
    mak "Bed? No, not yet. I was thinking about diving into quantum theory tonight. It’s something
    I haven’t really explored before."
    s "That sounds...incredibly boring."

    show makotopsurprised
    hide makotopnormal

    mak "Boring? What do you mean? Learning is never boring."
    s "Idea rejected. Think up something else."

    show makotopembarrassed
    hide makotopsurprised

    mak "What?...Why?"
    s "Because I don’t want to learn about quantum
    theory. Think of something the two of us can do together."

    show makotopembarrassedla
    hide makotopembarrassed

    mak "T-together?..."
    mak "I mean, there’s not really much the two of us can do this late..."
    s "How about I pay you back for your excellent treatment of me in your family’s
    store the other day?"

    show makotopangry
    hide makotopembarrassedla

    mak "Okay, first off...Calling it my family’s store makes me feel a lot guiltier
    about what happened there."
    mak "And secondly, don’t worry about paying me back. Thankfully, Miku
    has been gone for several hours, so I’ve already taken care of-"
    s "..."
    mak "..."
    s "Taken care of what, Makoto?"
    mak "Nothing!"
    s "You were touching yourself earlier, weren’t you?"
    mak "..."
    s "..."
    mak "I already told you I never get the chance to do stuff like that! Excuse me for seizing a valuable opportunity!"
    s "Wow, the dependable and responsible class rep Makoto Miyamura, getting herself off while her best friend is out of the room."
    s "That’s almost as nice of an image as that handjob I got."
    mak "Can you stop talking about that?! It never would have happened if you didn’t just take your pants off out of nowhere!"
    s "Well I’m glad I did. The way you cuddled up against me was adorable. I always had a feeling you could be that cute."

    show makotopexhausted
    hide makotopangry

    mak "Ugh...I knew this was going to happen...Time to add one more
    thing to list of stuff stressing me out every day."
    s "Jeez, if only we knew some sort of way to reduce stress."

    stop music fadeout 10.0

    show makotopdeadpan
    hide makotopexhausted

    mak "..."
    s "..."

    show makotopexhausted
    hide makotopdeadpan

    mak "Okay, fine. I’ll let you massage me since you seem so dead-set on it."
    mak "But nothing more!"
    mak "{size=-15}I’m kind of sensitive after I've already done it once, so...{/size}"
    s "I’m sorry, what was that? I didn’t hear you."

    show makotopangry
    hide makotopexhausted

    mak "Nothing! Please refrain from listening to my thoughts!"

    scene black
    with dissolve

    "Makoto begrudgingly wanders over to her bed and takes a
    seat on the edge of it, patting the spot behind her and signaling me to sit down as well..."

    scene makotomassage1
    with dissolve2
    play music "asobeatsex1.mp3" fadein 8.0

    mak "Guh...I forgot how good this feels..."
    s "See? Don’t you feel mean for talking to me with such a poor attitude now?"
    mak "Yes...I...apologize for my treatment of you, Sensei..."
    mak "I know you just want to help me relax..."

    scene makotomassage2

    mak "I just get too wrapped up in myself that I forget how other people feel sometimes."
    s "..."
    mak "I know I try to present myself like some unwavering intellectual
    all the time, but you probably just think of me as some stupid kid, don’t you?"
    mak "Some girl trying way too hard to be proper when she
    should be out having fun and...listening to pop music..."
    mak "Or whatever it is normal [teenage]girls do."

    "I don’t respond to Makoto. I figure it’s probably
    better to just let her vent at this point than to provide any advice."
    "My fingers trace the outlines of her shoulder blades, searching for knots
    and kneading them out of her soft skin once found."

    scene makotomassage1

    mak "Hah...wow...you’re like...some kind of expert at this..."
    mak "Maybe I’ll...give up on teaching and become a massage the[rapist]..."
    s "I don’t think that’s a good idea."

    "I break my two minute no-advice streak to chime in on the idea of her ruining her future."

    scene makotomassage3

    mak "How come? I hear they make good money. Even more than teachers in some cases."
    mak "Well, being a teacher isn’t exactly a high paying job either, as I’m sure you know already..."
    s "Being a massage the[rapist] comes with its own set of difficulties."
    s "For example, what would you do if you had a male client who got a little too handsy with you?"
    mak "Aim for the balls."
    s "...I’m sorry, what?"
    mak "You know what I’m talking about. That’s a male’s most sensitive area."
    mak "If anyone ever got too handsy with me, I’d simply utilize their weak point to my advantage."
    s "..."
    mak "...What? Why are you silent all of a sudden?"
    s "You’re strangely intimidating at times, did you know that?"
    mak "Really? I don’t think so at all."
    s "Follow up question, what if I were the one to get handsy with you?"

    scene makotomassage4

    mak "You already know how I respond to that situation."
    s "Do I?"
    mak "Yes. In fact, you ended up with a ruined shirt the last
    time you tried to take things up a level."
    s "True. Well worth it, though."
    mak "I’m sure. And now that you’ve learned your lesson, we don’t ever have to worry about-"

    scene makotomassage5
    with dissolve

    mak "Ah-! Hey! Where do you think you’re touching?!"
    s "Relax. It’s just part of the massage."
    mak "Like I’d believe th-"

    scene makotomassage6

    mak "Ah-!"

    "Makoto lets out a high pitched gasp as I begin to lightly massage her breasts."
    "Even through her bra, I can feel her nipples beginning to harden."
    "Compelled by
    the sudden pleasure, she pushes her back up against me."

    mak "Hah...this...isn’t a normal massage..."
    mak "I told you...you weren’t allowed to touch me like this..."

    scene makotomassage7

    mak "Don’t pretend...you didn’t hear me..."
    s "These are a little bigger than I thought they’d be..."
    mak "What...do you mean...you {i}thought{/i}?"
    mak "How often...do you think about me like that?..."
    s "Pretty often, actually."
    mak "That’s...inappropriate..."
    s "No. {i}This{i} is inappropriate."

    scene makotomassage8
    with dissolve

    "With expert precision and unbridled skill, I peel off Makoto’s shirt
    and toss it across the room."
    "She jolts up in response, pressing even harder against me
    as one of her legs begins to curl upward."
    "My right hand finds its way to her crotch and I begin the next step of the massage..."

    mak "Hah! S-Sensei! S-Stop that! I told you I’m sensitive after I’ve already done it once!"
    mak "And how the heck did you get my shirt off so quickly?!"
    s "I know you're sensitive right now. I’ll be gentle."
    mak "That’s...not the only issue!..."

    "Lightly and carefully, I press my fingers through her leggings and work my way up and down her slit."
    "She shivers and twitches each time I graze her clit through the...one layer of clothing?"

    s "Are you not wearing underwear?"
    mak "I don’t...like wearing underwear with leggings..."
    mak "Is that a...crime?..."
    s "Of course not. I’m just a little surprised."
    s "It’s also easier to tell how wet you are already."
    mak "That’s from...before..."
    s "I think you’re lying to me, Makoto."
    s "Do I need to see you after class?"
    mak "This is...after class...and I’m already being punished..."
    s "You think this is punishment?"

    "I hasten my movements and press harder against her
    virgin pussy. Her toes curl and more high-pitched gasps escape her mouth."
    "It’s erotic and adorable at the same time. I didn’t realize Makoto had something like this in her."

    mak "Ahhh...ahhh! Oh...my god...Sensei...please be careful...it hurts when you...do it too hard..."

    "I decide to comply this time and go back to being gentle. Makoto
    melts in my arms and surrenders to the pleasure of being toyed with by her teacher."

    scene makotomassage9

    mak "S-sensei..."
    mak "There’s..."
    mak "Something...I have to confess..."
    s "Oh? What is it?"
    mak "Remember that...vibrator...from the store the other day?..."
    s "I remember it well."
    mak "I might have...brought it home with me..."
    s "Really?"
    mak "Ah...uh-huh..."
    s "Is that what you used to play with yourself earlier?"
    mak "Uh-huh..."
    mak "Does that make me...a bad girl?..."
    s "Very bad. Aren’t you supposed to be the responsible one?"
    s "What would people think if they knew you liked being fingered by your teacher?"
    mak "What would they...think if they knew...you came all over your student’s hand?"
    s "Seems to me like we might have to keep our relationship a secret, huh?"
    mak "Mmf...hah...seems...so..."

    scene makotomassage11
    with dissolve

    "I pull Makoto backwards and she needs to prop her leg up on the bed to prevent herself
    from losing her balance."
    "I lift her bra up and squeeze the only breast I can reach, rolling it through my
    hand as her nipples harden even more."
    "Her breathing is rapid at this point. It’s almost like her lungs are collapsing."
    "I can sense that she’s going to cum any second now."

    scene makotomassage12

    mak "Ahh...ah...AHHH...S-Sensei..."
    mak "Do you...maybe wanna..."
    mak "You know..."
    mak "...Fuck me?"
    s "Are you sure that's what you want?"
    mak "Hah...mmm...yeah...I..."
    mak "I think so..."
    mak "Yeah...I want it...really...{i}really{/i} badly..."
    mak "Please..."
    mak "Give it to me already..."
    mak "I've wanted you...since we first met..."
    mak "And b-besides...it's not like I'm...ahhnn..."
    mak "It's not like I’m...going to orgasm...from just..."

    scene makotomassage11

    mak "Ah..."

    "Knowing that she absolutely {i}will{/i} cum from just this, I press harder."
    "Two of my fingers come close to entering her, but I'm held back by the layer of fabric separating me from her pussy."

    mak "Hah..."
    mak "Oh god...yes...S-Sensei..."
    mak "Right...there..."
    mak "I...hah...I...OH MY GOD...AHHH...Yeah~"
    mak "Just..like..."
    mak "..."

    "Makoto pauses for a moment, shuddering and digging into her thigh with her nails."
    "Her neck digs deep into my shoulder as she prepares for an intense wave of pleasure."
    "Then-"

    scene makotomassage14
    with cumflash
    with cumflash
    with hpunch

    mak "AHHHHHHHH!!!!!!~~~~~ <33333333333"

    "Makoto explodes into a fit of pleasure, convulsing in my arms as she reaches out and pulls my hair in desperation."
    "It’s a violent orgasm, one in complete contrast to her normal cool demeanor."
    "After a moment of shivering and crying out goes by, her body finally relaxes once again..."

    scene makotomassage13
    with dissolve

    mak "Hah...hah...hah..."
    mak "I’m...sorry..."
    mak "I said...some strange things...near the end there..."
    s "Do you still want me to fuck you?..."
    mak "Umm...I think...I’ll die...if I...do it again tonight..."
    s "Are you sure?"
    mak "Yes..."
    s "Like, really sure?"
    mak "I’m sorry..."
    mak "I would...jerk you off again but...I can’t move..."
    mak "Goodbye, Sensei..."
    mak "Please don’t...forget me..."

    scene makotomassage15
    with dissolve

    mak "..."
    s "Makoto?"
    mak "{i}Zzzzz...{/i}"
    s "..."
    s "God damnit."

    scene black
    with dissolve2
    stop music fadeout 5.0

    "I lay Makoto down on her bed and throw the blanket over her."
    "I hope that she is able to recover from the...exhausting night she had tomorrow morning."
    "I also hope that we can follow up on those commands she gave me mid-orgasm..."
    "Makoto might try to act cool and composed all the time, but
    it’s clear to see that she cracks under pressure and lets out an entirely different side of her."
    "I wonder how she’d handle losing her virginity?..."

    "........."
    "......"
    "..."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label makotodorm15:
    scene black
    with dissolve
    play sound "knock.mp3"
    stop music fadeout 5.0

    s "Makoto, are you in there?"

    "..."
    "..."
    "..."
    "Silence. "
    "Strange. She’s normally in her dorm room around this time."
    "I guess maybe she had work tonight?"

    jump makotomastx

label makotomastx:
    "I really don’t feel like going all the way to the porn shop, so maybe I should just head back and-"

    mak "{i}Mm...{/i}"
    s "..."

    "Considering my ear is essentially pressed against the door (Like the totally normal guy I am), a soft, lewd
    sound manages to find its way to me. "
    "I’m guessing Makoto heard me knock and didn’t respond because she’s...{i}in the middle of something.{/i}"
    "But I know how to handle situations like this. "
    "I’ll simply wait for her to be done and then knock again, like a true gentleman."

    "..."
    "..."
    "..."

    mak "Ah...hah..."

    "Never mind. Time to visit the class president."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I push the door open to find that this closet pervert had left it open for anyone to walk in on her."
    "Therefore, it is not my fault if she yells at me. This is her doing and I am simply blissfully unaware..."

    scene makotomast1
    with dissolve
    play music "asobeatsex4.mp3" fadein 5.0

    mak "What?! Sensei?! What...What are you doing in here?! I didn’t say you could come in!"
    s "Correct. But I wasn’t going to simply walk away after hearing all of those cute masturbation noises of yours."

    scene makotomast2

    mak "Was...Was I really that loud? I was trying to keep my voice down..."
    mak "And why was the door unlocked? You don’t have a key, do you?"
    s "No key here, just determination."

    scene makotomast3

    mak "Determination doesn’t unlock doors, idiot!"
    s "Says the girl fingering herself in front of her teacher."

    scene makotomast4

    mak "Well...I can’t just stop in the middle of it..."
    mak "So can you please just...leave for a few minutes and let me-"
    s "Nope. I’m here for the show now."

    scene makotomast5

    mak "Yeah...I had a feeling you were going to say that."
    s "You know me so well."
    mak "Unfortunately, it appears that I do..."

    scene makotomast4

    mak "I am thankful it was you and not anyone else, though. A look like this
    isn’t really fitting for the class president, is it?"
    s "I think a look like this is perfect for you."

    scene makotomast6

    mak "Huh?...Why do you say that?"
    s "Because this is the real you, isn’t it? "
    mak "The real me?"
    s "Yeah. A closet pervert who can’t help but leave doors unlocked while she [masturbate]s."

    scene makotomast7

    mak "No! You’re misunderstanding! The door thing really was just a coincidence!"

    scene makotomast8

    mak "It’s true that I have been...pleasuring myself a lot more than normal lately...but it’s all for a good reason."

    scene makotomast9

    mak "So...if you maybe wanted to...help me out a little bit-"
    s "Nope. Not tonight."

    scene makotomast7

    mak "What?! You’re rejecting me?! Why?!"
    mak "Since when do you have that kind of self-control?!"
    s "I normally don’t. But I’m particularly enjoying watching you play with yourself right now."
    s "So please continue for the time being or I’ll set {i}this{/i} as my new phone background next."

    scene makotomast3

    mak "You wouldn’t dare."
    s "Try me."

    "I begin to reach for the phone in my pocket and Makoto quickly goes back to pleasuring herself."

    scene makotomast10
    with dissolve

    mak "Hah...ah...fine...you...you win..."
    mak "You can...watch me...if you want..."
    mak "Not like...I care anyway..."
    mak "You’ve already...seen it before...so it’s not like...this is new to you or anything..."
    mak "Though...hah...I will admit...you’re...definitely...much better at it...than I am..."
    mak "Maybe it’s because...your fingers are bigger?..."
    s "I’m sure that helps."

    scene makotomast11

    mak "Would it be weird...if I told you I wanted something even {i}bigger{/i}, though?"

    scene makotomast12

    mak "Wait. No. Forget I said that. My brain is doing the talking again."
    s "Are you trying to seduce me, Makoto?"
    mak "I’m not...doing anything...of the sort..."
    mak "Just...fantasizing out loud...that’s all..."
    s "Don’t worry, you won’t have to fantasize for much longer. Hell, if I didn’t
    walk in on you already in the middle of this, I might have even taken your first time tonight."

    scene makotomast13

    mak "Really? You would have...fucked me...Sensei?"
    s "I would have."

    scene makotomast14

    mak "Hah...oh god...that...turns me on...a lot more than it should..."
    mak "Are you sure...you don’t want to...touch me?..."
    s "Right now, yes. Consider this a detention."
    mak "Hah...my first detention..."
    mak "I don’t...like it very much..."
    mak "It’s kind of degrading..."
    s "If you don’t want to get in trouble, don’t get caught doing inappropriate things."
    mak "You’re the...{i}fuck{/i}...you’re the one who walked into my room...this is...a breach of privacy..."
    mak "You should...pay me back...by...fucking me...right now..."
    s "I’m good, thanks."

    scene makotomast11

    mak "I...hate you..."
    mak "What kind of...man turns down...a virgin when she’s...giving herself up...like this..."
    s "A man who derives great pleasure in watching how horny you get by just thinking about that..."

    scene makotomast14

    mak "I’m not...horny...I’m stressed...it’s different..."
    mak "I’m just...relieving tension...since you won’t do it for me..."

    scene makotomast15
    with dissolve

    mak "Ngh~!"

    "Makoto suddenly begins to rub herself more aggressively, sliding the tips of two of her fingers inside her virgin slit every few seconds."
    "She’s essentially (And literally) begging to be fucked right now."
    "And while I’ve already decided to not take her virginity tonight, I never said I’m not open to other things."

    mak "Oh my god...I’m...going to cum...while you just stand there...watching me..."
    mak "I feel like...such a slut...I’m...filthy..."
    mak "Sensei...please...I don’t know how many times I need to ask you..."
    mak "Just...put it inside of me...so I can get this all out of my system..."
    mak "I don’t...want to keep doing this every night...it’s...really...{i}really{/i}...tiring after a while..."
    s "Makoto."

    scene makotomast16

    mak "Y-Yeah?...What?..."
    s "Keep your eyes closed."

    scene makotomast15

    mak "Yes...[makotomaster]..."
    mak "Do...whatever you want to me...I won’t say no...to anything..."

    scene black
    with dissolve

    "Those are dangerous words."
    "Words that should never be uttered to any man, especially
    one approaching you with a raging hard-on."
    "I’m sure that part of Makoto thinks I’m going to push her down right now."
    "And part of me wants to."
    "But I want to use her as a toy in another way- while she’s still at her most vulnerable."

    play sound "zipper.mp3"

    mak "..."
    mak "Please...be-"

    scene makotomast17
    with dissolve

    mak "MNGH!"
    mak "MMF! WHT...SSS...HPPNING...???!!!"
    s "Keep touching yourself."

    scene makotomast18
    with dissolve

    mak "Mmmm...hmmm...ngh...yes...[makotomaster]..."

    "I grab the back of Makoto’s head and begin to pull it down on my cock."
    "She can’t take more than a few inches of it, but she takes them without issues, never
    gagging and even wrapping her tongue around it."
    "She’s gotten so wet that the sounds of her playing with herself now fill
    the room along with the mumbled gasps escaping the slight openings of her mouth when she tries to catch her breath."

    mak "Nghhh~ Mmf...Sensei...Sensei~"
    mak "Are you...nff...watching...me?..."
    s "How could I not?"
    mak "Are you...mmm...sure...you don’t...want to...put it in?..."
    s "I am."
    mak "Are you...{i}really{/i}...sure?..."
    mak "There’s never...been one...inside..."
    mak "I bet it...will feel really good for you..."
    s "This already feels good."
    s "Now go back to focusing on my dick before I take that away too."
    mak "Mmm...such...mmf...a jerk..."

    "Her fingers begin to slip in and out of her even faster as her legs continue to spread."
    "It’s taking every ounce of self control I have to {i}not{/i} fuck her right now. "
    "In fact, I’d be filled with regret if keeping my word didn’t matter more to me than cumming inside of my classroom assistant a little earlier than anticipated."
    "I’ve always been stubborn like that. Once I say something, there’s no backing down."
    "And if I cave in now, she’ll just think she can get anything she wants from me whenever she wants it."
    "The only way to avoid that-"

    scene makotomast19
    with dissolve

    mak "MMMMMMNNNNNNNNN~~~~!!!!!"

    "Is by doing anything else I want with her."

    mak "MMMGNHHH!! MMMBBBPPHH...HNGH..."

    "Makoto tries to come up for air several times, but I hold her head down and decide against letting her."
    "If she’s that desperate to breathe, she’ll use her nose."
    "Though, by the way she’s begun to furiously finger-fuck herself, I imagine
    focusing on any other process might be a little difficult right now."

    s "Hurry up and make me cum, Makoto. I’ll let you breathe as soon as you do."
    mak "MMMFHHH! MMM...MMM...MNGHH!!~"

    "She obliges and continues to desperately wrap her tongue around my cock in an
    effort to force the cum out of me and into her throat."
    "And it works."

    s "Makoto..."
    mak "MMMM!!! MMGNNNHHH! HHNNNGG...!"

    with sexfade
    with sexfade
    scene makotomast20
    with cumflash
    with hpunch

    mak "MMMMMMMMMMMMMMMMMMMMMMMMMMMMM~~~!!!!"

    "I can feel air rapidly escaping Makoto’s nose as her body tries to figure out what’s going on."
    "The orgasm subsides in a matter of seconds and Makoto quickly gulps down every last drop of
    cum before collapsing onto her back."

    scene makotomast21
    with dissolve

    mak "AHHH...HAH...FUCK...OH GOD...I’M...CUMMING..."
    mak "HAH...ANH...AHHH..."
    mak "Ahh...hah..."
    mak "..."

    scene makotomast22
    with dissolve

    mak "AAAAAAAAAAAAAAAAAaaaaaaaaaaahhhhhhh~~~!!!!"

    "Makoto lifts herself up for a moment as she convulses from her orgasm. "
    "I’m guessing it was the deepthroat that sent her over the edge."
    "She really is a pervert, isn’t she?"

    scene makotomast23
    with dissolve

    mak "Hah...hah...hah..."
    mak "Oh...my god..."

    scene makotomast24

    mak "You...almost killed me..."
    s "I did no such thing. I was just having fun."
    mak "Fun...?"
    mak "Did you...feel good, then?..."
    s "Yeah. Not sure if you've realized this but you kind of {i}have{/i} to be feeling good in order to cum."
    mak "Then...do you want to...have sex now?"
    s "You still want to keep going after that intense orgasm?"
    mak "Yeah...I want you...to...treat my pussy...like you treated my throat..."
    s "You’re fucking insane."
    mak "Am...not..."

    scene makotomast25

    mak "Just...a...reliable...diligent...girl..."
    mak "And...and..."
    mak "..."

    scene makotomast26
    with dissolve

    mak "Zzzz..."
    s "..."
    s "Makoto?"
    mak "Mm...zzzzzzzz..."
    s "..."

    "Well, I guess that’s all she’s got in her for tonight."

    scene black
    with dissolve
    stop music fadeout 5.0

    "I think about putting Makoto into a slightly better position for when Miku comes home..."
    "But I decide against it because I think it would be funny for someone as innocent as the star of the soccer team to
    walk in on such an uncharacteristic sight."
    "If you can even call that uncharacteristic..."
    "Makoto is..."
    "Well, I’m starting to think she might be a bit of a freak."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label day34:
    scene office
    with dissolve2

    "Another day of[school] passes by with barely any problems."
    "There {i}was{/i} one strange thing that happened, though."
    "Ayane, of all people, asked me if she could come to my office after[school] today."

    if bonus == True:
        "Normally, I’d think there was some sort of perverted motivation behind this, but something about the way she asked today actually sounded kind of serious."

    "I hope she’s doing okay..."

    play sound "knock.mp3"

    ay "Sensei? Can I come in?"
    s "Yup. The door is open."

    play sound "dooropen.mp3"

    show ayaneupset
    with dissolve

    ay "Thanks for seeing me today..."
    s "No problem. Is something going on? You don’t normally ask to see me in here."
    s "In fact, I don’t think you’ve ever asked to see me in here."

    show ayanenormal
    hide ayaneupset

    ay "Well, there was that one time in the beginning of the year when
    I was feeling down about my dad, but that’s not the issue this time."

    "Huh. I guess she’s talking about a conversation she had with the real Sensei before I took over."
    "I didn’t realize Ayane was actually dealing with problems like that."

    s "If it’s not that, then what’s going on?"

    show ayaneupset
    hide ayanenormal

    ay "Do you promise not to laugh when I tell you?"
    s "Of course."
    ay "...Okay."
    ay "But if you make fun of me, I’m going to be really mad. Okay?"
    s "Yup. Just tell me what’s going on."
    ay "Then..."

    "..."

    show ayanenormal
    hide ayaneupset
    play music "asobeatsex3.mp3" fadein 6.0

    jump officebjx

label officebjx:
    ay "I want to have sex."

    "Well then...I guess it was something perverted after all."

    s "Like...right now? In the office?"
    ay "Well, yes. But also no."
    s "I’m not sure I follow..."

    show ayaneupset
    hide ayanenormal

    ay "I mean...It’s no secret that I really, {i}really{/i} like you...But that doesn’t
    mean I don’t want my first time to be special."

    show ayaneembarrassed
    hide ayaneupset

    ay "Like, your office is nice and everything...but it’s not {i}that{/i} nice."
    ay "But anyway, I just wanted you to know that like...I’m ready and stuff..."
    s "Are you sure?"

    show ayanenormal
    hide ayaneembarrassed

    ay "I am. I can’t be alone with you without my mind going crazy."
    ay "I even came up with that stupid plan to pretend I hurt myself just to get you to bring
    me to the nurse’s office."

    show ayaneembarrassed
    hide ayanenormal

    ay "You probably think I’m crazy now, don’t you?"
    s "Crazy?...Hm..."
    s "Maybe a little."

    show ayanepout
    hide ayaneembarrassed

    ay "Agh! Rude!"

    show ayaneembarrassed
    hide ayanepout

    ay "But I guess that’s only fair...I know I’m acting really weird. I promise
    I’ll try to tone it down if it means making you like me more."
    s "You don’t need to change anything. I like you just the way you are."

    show ayanenormal
    hide ayaneembarrassed

    ay "Wait, really? But you just called me crazy."
    s "I called you {i}a little{/i} crazy, which isn’t necessarily a bad thing."
    s "Sure, you might be a little neurotic. And it’s kind of weird that Despacito is the only song you know-"

    show ayaneangry
    hide ayanenormal

    ay "Despacito is a great song!"
    s "Hey, let me finish."

    show ayaneupset
    hide ayaneangry

    ay "Oh, right. Sorry..."
    s "Anyway, what I’m trying to say is I don’t think you should change. You’re great
    in your own...weird kind of way."

    show ayaneembarrassed
    hide ayaneupset

    ay "Do you really mean that? You won’t get bored of me or anything?"
    s "Of course not."
    ay "Okay, good. Because you’re pretty much the only guy in my life that actually means
    anything to me at this point."

    show ayanelookaway
    hide ayaneembarrassed

    ay "Well, there’s Geoffrey too, but..."
    s "...Geoffrey? Who the hell is that?"

    show ayanesmile
    hide ayanelookaway

    ay "He doesn’t matter right now. We’re talking about my virginity. Leave Geoffrey out of it."
    s "...Right."
    ay "So...When are we gonna do it?"
    s "Are you saying we should...schedule it?"

    show ayanecurious
    hide ayanesmile

    ay "Sure. I can’t see why not."
    s "Well, I can see why not. That’s weird."

    show ayanewink
    hide ayanecurious

    ay "Awe, but I thought you liked weird!"

    "This girl is ridiculous..."

    show ayanesmile
    hide ayanewink

    ay "Hey, so like..."

    show ayaneembarrassedsmile
    hide ayanesmile

    ay "Do you want me to like...give you a blowjob right now? Because I totally will."
    ay "All this sex-talk is getting me kind of excited..."
    s "Right now? I thought you were against doing stuff in the office?"

    show ayanenormal
    hide ayaneembarrassed

    ay "No, no. I’m against losing my virginity in the office. I’m totally open to doing all kinds of other stuff."

    "{i}All kinds?{/i}"

    show ayanewink
    hide ayanenormal

    ay "I mean, we’ve already knocked the nurse’s office off the list. We might as well hit up the rest
    of the[school] while we’re at it."
    s "But what if one of the other girls shows up? Ami’s nearly walked in on us twice now."
    s "And if I know anything about how all this goes, it’s bound to happen again today."

    show ayaneembarrassed
    hide ayanewink

    ay "I mean...{i}I{/i} don’t really care..."
    ay "It’s only a problem if she sees us, right?"
    s "Well unless you can turn yourself invisible, I don’t think-"

    show ayanewink
    hide ayaneembarrassed

    ay "Don’t worry! I’ve already got it figured out!"
    s "...?"

    scene black
    with dissolve

    "Ayane takes my hand and pulls me over to my desk."
    "She brings herself to her knees and slides underneath it, almost perfectly fitting inside."

    ay "Wow, it’s really dark under here. I can barely see anything..."
    s "You don’t really have to {i}see{/i} to give a blowjob."
    ay "Awe, but where’s the fun in that?...Your penis is so cute!"
    s "Never call a man’s penis cute, Ayane. That’s rule #1 of penises."
    ay "Is it really?"

    play sound "zipper.mp3"

    ay "I’ll have to remember that...*chu*"

    scene officebj1
    with dissolve

    "Ayane opens up her first-ever blowjob with a quick kiss on my shaft before bringing
    her tongue to the head and lightly glazing over it."

    scene officebj2

    ay "Hey, am I allowed to touch myself while I do this?"
    s "I mean...I guess so. Make sure not to let it distract you though, okay?"

    scene officebj3

    ay "Mmph...Sir, yes sir..."

    "Ayane goes back to licking me, sometimes stopping for a
    moment to try and fit the tip in her mouth."
    "This never lasts more than just a second or two. Every time it goes in, she quickly
    gives up and goes back to licking..."
    "It’s actually kind of frustrating in a way."

    s "Ayane, are you not comfortable actually putting it in your mouth?"
    ay "*Amf*...It’s...*shcleck*...too big..."
    ay "It won’t fit."
    s "Well, keep trying. That’s an order."
    ay "*Schlurp* If...you say soo...*Umf*"

    scene officebj4
    with dissolve

    ay "Amf...Mmm...mmm...schlip...mlem..."
    ay "Snsss...ifff...lrrrly...wwnnnt...ft..."
    s "Ayane, use words please."

    scene officebj2
    with dissolve

    ay "*Gasp* I...was saying...It literally won’t fit..."
    ay "My mouth doesn’t open any more than that..."

    "Curse this large penis..."

    s "Well, whatever. Just keep doing your best."

    scene officebj3

    ay "Ahh...I...*schleck*...will..."

    "Ayane goes back to mostly licking, with a few scattered attempts
    at trying to fit my dick inside of her mouth. None of which succeed."
    "Her tongue dances back and forth across the head, lapping up precum between hushed and panicked breaths."

    ay "Mmf...anf...hah...mmm..."

    scene officebj2

    ay "Sensei...will it be...bad if I...cum before you?"
    s "Very bad, actually."
    s "You’re not allowed to cum before me."

    scene officebj5

    ay "Huh?! Why not?!"
    s "Because I said so. Are you really about to cum from just a few minutes of touching yourself?"

    scene officebj4
    with dissolve

    ay "Mmf...iffff...feeee...sss...gddd..."
    s "...What?"

    scene officebj6
    with dissolve

    ay "Paaaah..."
    ay "I was trying to say it feels so good!"
    ay "I’m about to back down on my no-office rule!"
    ay "Please let me cum, Sensei! I’m going to die if I don’t!"
    s "Not until I do. Got it?"

    scene officebj4
    with dissolve

    ay "AMF...SSSS...UNFRRR..."

    "I’m pretty sure that one was supposed to be ‘so unfair.’"

    play sound "knock.mp3"

    a "Sensei? Are you in there?"

    scene officebj7
    with dissolve

    ay "Ah-"
    s "I am. Come on in, Ami."

    play sound "dooropen.mp3"

    "It’s almost like this has happened before..."

    scene officebj8
    with dissolve2

    s "What’s up? Is something wrong?"
    a "Ummm...Nothing in particular...Just feeling kind of lonely, I guess..."
    a "I was wondering if maybe you...wanted to walk home with me?"
    s "I can after my counseling hours are over."

    scene officebj9

    a "But...no one’s here?"
    s "No one’s here {i}right now{/i}. But I can’t leave early in case someone comes in here for help."

    scene officebj10

    a "You picked a stupid day to follow the rules..."

    scene officebj1
    with dissolve

    ay "{i}*mmf...mmf...schlurp...lick...mlem...*{/i}"
    ay "{i}Mmm...hurry up and cum already...{/i}"

    scene officebj11
    with dissolve

    a "Did you...hear something just now?"
    s "Hear what?"
    a "I’m...not really sure..."
    s "Huh...No. I don’t think I heard anything."

    scene officebj3
    with dissolve

    ay "{i}*Ahm...ahmm...mlem...schlick...chu...mmm...*{/i}"

    "Ayane begins quickening her pace, likely panicking due to the fact her best friend
    is inches away right now."
    "The added layer of excitement is causing me to reach the end of my rope as well."
    "I don’t know how much longer I’ll last at this point..."

    scene officebj4
    with dissolve

    ay "*AMMFFF*"

    a "There it is again...I swear I heard something just now."
    s "You must be tired...maybe I {i}should{/i} leave a little early to make sure you’re okay."

    "Ayane tries, yet again, to fit the entire head of my penis into her mouth."
    "This time, though, she winds up using her tongue in tandem with it, rolling the length
    of it around my dick and essentially beckoning me toward orgasm."

    scene officebj12
    with dissolve

    "I can feel her fingers trembling along my shaft. She’s probably climaxing as we speak..."
    "Stricken by the realization that my {i}[niece]{/i} is going to watch me ejaculate any second now, I fall
    victim to the assault of Ayane’s touch and unload all over her face..."

    scene white
    with cumflash
    scene officebj13
    with cumflash and hpunch

    ay "{i}*Mmmmmmmmm!!!*{/i}"

    "I start coughing to mask the noise of Ayane’s revelry in our mutual orgasm."

    scene officebj11
    with dissolve

    a "Woah, are you okay? You’re not coming down with a cold, are you?"
    s "No...No, I’ll be fine."
    s "Hey, Ami. Why don’t you wait out in the hallway for a second. I’m just gonna clean up
    a few things in here and then we can walk home together. Deal?"

    scene officebj8

    a "Yeah...Deal. Sorry for being such a baby today. Just wanted to spend a little time with you, that’s all."
    s "Don’t worry about it. I’ll be out in a second, okay?"
    a "Okay..."

    scene officebj14
    with dissolve
    play sound "dooropen.mp3"

    "..."

    scene officebj15
    with dissolve

    ay "..."

    "Ayane pauses for a moment, loosening her grip on my cock."

    ay "We’re horrible people, aren’t we?"
    s "...Probably."

    scene black
    with dissolve2

    "I wind up convincing Ayane to wait in the office until Ami and I are gone."
    "I have to give her my key, which is mildly terrifying given her infatuation with me, but
    it’s the price I must pay for enabling what just went on."
    "I also have no idea how she’s going to clean herself up given that there
    are no tissues in my office...but I guess that problem is out of my hands now..."

    stop music fadeout 3.0
    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label day42:
    scene gym
    with dissolve
    play music "happyandplotting.mp3"

    "Gym class has ended for the day and I’m staying after with Makoto and Ami to clean the place up."
    "Normally, I would have been able to do it all myself while they take their showers, but there was an...’incident’ today..."

    show amisurprised at left
    with dissolve

    a "Do you think the janitor is going to be okay?..."

    show makotosurprised at right
    with dissolve

    mak "I honestly don’t know...Ayane hit him pretty hard."
    s "That girl has a hell of an arm on her..."

    "While dropping by the gym to get something out of the storage room, one of the[school]’s janitors was pelted in the head by a dodgeball."
    "Normally, a grown man would be able to shrug something like this off and just get on with his day after a minute or two."
    "However-"
    "What I failed to mention is that this dodgeball had been moving at what seemed to me like a major league player’s fastball."
    "As such, the janitor was knocked unconscious and may or may not have cracked his head open on the floor."
    "There was blood everywhere."
    "And of course I had to be the one to clean it up on the account of us now being down one janitor."

    show aminormal at left
    hide amisurprised

    a "Sensei, are we being sent home early today?"
    s "I think so. If we actually did just witness a death, that would only make sense."

    show makotonormal at right
    hide makotosurprised

    mak "Precisely. The[school]’s code states that in the event of any sort of
    traumatic incident, whether it be a shooting, suicide, or dodgeball accident, that all students are to be sent home."
    s "Well at least one good thing came out of this."

    show amitongue at left
    hide aminormal

    a "You’re lucky you have two students as dedicated as me and Makoto."
    s "{i}Makoto and I{/i}, Ami..."

    show makotoembarrassedla at right
    hide makotonormal

    mak "Um...actually...and forgive me for interjecting, Sensei, but {i}Makoto and me{/i} would probably be better there."
    s "What? Why?"

    show amiconfused at left
    hide amitongue

    a "Ahh! I thought we were done learning for today!"
    mak "The best way to check which wording is correct is to remove the secondary subject from the sentence entirely."
    mak "In Sensei’s example, Makoto and I, Ami’s finished sentence would have been: You’re lucky you have a student as dedicated as I..."
    mak "And while that sentence isn’t {i}entirely{/i} flawed, it’s still not the most accepted nor modern phrasing of it."

    show makotowink at right
    hide makotonormal

    mak "But I’m sure Sensei already knew that and was just having a memory lapse."
    s "Yup. That is exactly what happened. Thanks for the explanation, Makoto."

    show aminormal at left
    hide amiconfused

    a "Umm, guys, sorry to interrupt, but did either of you see Futaba and Miku leave the locker room?"

    show makotonormal at right
    hide makotowink

    mak "..."
    a "..."
    mak "Oh dear god no."
    s "Is that a problem? Do those two not have a good relationship or something?"

    "Makoto and Ami look at each other, completely ignoring me."

    show makotoexhausted at right
    hide makotonormal

    mak "How could we have let this happen again?"

    show amigiveup at left
    hide aminormal

    a "I was about to ask you the same thing! Aren’t you supposed to be the responsible one here?"
    mak "Ami, as the class president, it would have been improper for me to allow Sensei to clean the gym on his own."

    if bonus == True:
        a "Yes, but I’m his [niece] and family takes priority in these situations..."
    else:
        a "Yes, but I'm his {i}accountant{/i} and we need to go over very important financial documents."

    s "Guys?"

    if bonus == True:
        mak "No, no. That’s not the case at all. You were simply born into your position while I worked for mine and can be removed at any moment."
        a "Yes, yes. But Sensei loves me and thinks that girls who wear glasses are gross."
        s "Hello?"
        mak "No, no, Ami. You have it all wrong. Sensei actually-"

        "The two of them proceed to argue like this for the rest of the gym period while I scour the room for bone fragments..."
    else:
        s "Someone just died. This really isn't the time to argue."

    scene black
    with dissolve2

    jump showertimex

label showertimex:
    "{i}Meanwhile...{/i}"

    scene showertime1
    with dissolve2

    f "..."
    f "..."
    f "..."

    scene showertime2
    with dissolve

    mi "..."
    f "..."
    mi "Ngh..."

    scene showertime3
    with dissolve

    mi "..."
    f "...huh?"
    mi "You think you’re queen of the whole frickin’ world, don’t you?"
    f "W-What?..."

    scene showertime4
    with dissolve and hpunch

    f "Ah?!"
    mi "You think you’re so darn great just because your bazongas are the size of my head!"
    mi "You know there are plenty of people who like small ones too, dontcha?!"

    scene showertime5
    with dissolve

    f "Ahn~ Miku, stop it! Those are...ahh...sensitive!"
    mi "Yeah, yeah, I bet you’d love it if I believed that!"
    mi "These things are so big you probably can’t even feel this!"
    f "Ahhh~ No! I definitely feel it! And I don’t like it at all!"

    scene showertime6
    with dissolve

    mi "Hey! You’re not allowed to complain! Do you have any idea how girls like me feel when
    they see these big ol’ honkers and then look down and realize we ain’t got squat?!"
    mi "It’s criminal, I tell ya! Criminal!"
    mi "I should call the police!"

    scene showertime7
    with dissolve

    f "Mmm~! Miku please...I just want to take a shower! I wasn’t doing anything wrong!"

    scene showertime8
    with dissolve

    mi "Your entire existence is wrong! The whole world is wrong! There is no justice!"
    f "Ahhh...This...is...bad..."

    scene showertime9
    with dissolve

    mi "Though...now that I’m touchin’ em...this is kinda fun."
    mi "They’re really heavy...And they’d probably slow me down on the soccer field."
    mi "I can just imagine em slappin’ me in the face when I’m tryin to run and that sounds like a nightmare."
    mi "Plus I can get away with not wearin’ a bra most of the time."

    scene showertime10
    with dissolve

    f "Miku...please...let go..."
    mi "Why?"
    f "Because...it feels strange...and I’m embarrassed..."
    mi "Embarrassed of these things? How come? If mine were this big I’d be showin’ everybody."
    f "That’s...ahh...illegal..."
    mi "To heck with the law and to heck with your big, stupid boobs!"
    mi "I’m gonna find someone who cares about smaller girls like me and then you’ll see that you’re not that much of a big shot!"
    f "I’m...not a big shot! I can’t help how large they are..."

    scene showertime11
    with dissolve

    mi "Likely story..."
    mi "What’s your workout routine? You drink a lot of milk, don’t ya?"
    mi "How come mine don’t grow no matter how much milk I drink?"

    scene showertime8
    with dissolve and hpunch

    mi "TELL ME, DAMNIT!"
    f "AHH~! Miku, don’t squeeze them like that! It hurts!"
    mi "AAAAAAGGGHHHH!!!!! THERE IS NO GOD!!!!!!!"

    scene black
    with dissolve2

    "{i}And on that day...{/i}"
    "{i}Help never came...{/i}"

    stop music fadeout 3.0
    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label dojo15:
    scene ayanesit1
    with dissolve
    play music "sakuya4.mp3" fadein 3.0

    "I walk into the dojo to find none other than the one
    and only Ayane Amamiya sitting straight up on the instructor’s bench."
    "I’ve seen her be scolded for sitting here a number of times now, so I’m not sure
    what the reason for this sudden bravery is..."

    ay "So..."
    ay "I see you’ve found your way back, Arakawa-san..."
    s "Are we starting this already? And don’t call me Arakawa-san, it’s weird."
    ay "Tell me...why are you here?"
    s "I came here to chew bubble gum and kick ass..."
    s "And I’m all out of ass..."
    s "Wait, I messed that-"
    ay "No, no. Why are you {i}really{/i} here?"
    s "...To take back Kumon-mi?"

    scene ayanesit2

    ay "I see..."
    ay "So it is too late after all..."
    s "Too late for what? And where is everyone else? You know you’re not allowed to sit there."

    scene ayanesit3

    ay "I rented the place out so we could be alone today."
    s "You rented out the entire dojo? How much did that cost?"
    ay "Mmmmm, I don’t really remember. I’ve got one of those fancy black credit
    cards that you can just put anything you want on."
    s "Is the bubble wrap business really that lucrative?"

    scene ayanesit4

    ay "I mean, what safer and more affordable way is there to pad the
    inside of cardboard boxes for shipping?"
    s "That’s...a good point, I guess?"

    scene ayanesit2

    ay "Either way, that is not why we’re here today..."
    ay "We are here to settle our differences not with violence, but with words..."
    s "If I recall correctly, you pulled a gun on me the last time we ‘sparred.’"
    s "Could it be that the legendary Ayane Amamiya is running from a fight?"

    scene ayanesit5

    ay "Of course not. I would never flee from battle."
    ay "The fact of the matter is, though..."

    "Ayane pauses for a moment and holds her breath. I can feel the aura of
    a warrior radiating throughout the room."

    scene ayanesit6

    ay "I refuse to fight the man I love."
    s "Woah, hold on a second-"

    scene ayanesit5

    ay "So, as the two of us are decidedly in love with one another..."
    s "Hold on, I never said-"
    ay "The only thing we can do is rule this world together."

    scene ayanesit6

    ay "And since so many of mine and your men perished on the battlefield, it
    seems we are left with no other option but to repopulate the world ourselves..."

    jump ayanesitx

label ayanesitx:
    s "The {i}world{/i}, or just Kumon-mi?"

    scene ayanesit5

    ay "The entire world."
    s "We, uhh, might have a problem then."

    scene ayanesit6

    ay "A problem? Am I not good enough for you anymore? We
    shared a really special moment together, so I thought-"
    s "Not because I’m getting rid of you, because you’re physically incapable of having more than
    one child per year."

    scene ayanesit7

    ay "Oh...I didn’t even think of that."
    s "Well, I mean, you could always have twins or something like that, but yeah."
    s "I don’t really think getting pregnant while you’re a student is a good idea anyway, so..."

    scene ayanesit1

    ay "Valid argument, loyal husband."
    s "I’m not your-"

    scene ayanesit7

    ay "There is another problem as well. And I’m afraid this one is specific to me."
    s "And what could that possibly be...?"

    scene ayanesit1

    ay "I am still in a significant amount of pain from when you took my virginity."
    s "Still? How is that even possible?"

    scene ayanesit6

    ay "Do you have any idea how big that thing you put inside of me is? It’s like
    you tried to fit an entire arm in there."
    s "Well, thanks, but it’s definitely not as big as an arm."

    scene ayanesit1

    ay "That may very well be true, but it does not change the fact that
    I am beginning to believe my body has forever been altered."
    s "Your body {i}has{/i} been altered. That’s what happens when a girl loses her virginity."

    scene ayanesit4

    ay "Oh well. I guess you’ll just have to take care of me from now on since you’ve damaged me beyond repair."
    s "That’s not how that works..."

    "There’s really no point in arguing with Ayane when it comes to things like this, so I’ll give up on pushing back."
    "Besides, it’s not exactly torture being subjected to a life of having sex with a cute, rich girl."

    scene ayanesit8

    ay "But anyway, all that aside, what did you want to do today?"
    ay "I originally rented the place out because I thought it would be fun to have sex here, but you’re clearly
    not in the mood and I’m still in pain so-"
    s "Who said I’m not in the mood? I’m pretty much always in the mood. That’s what it means to be a guy, isn’t it?"

    scene ayanesit3

    ay "Huh? But that one time when I wanted to make out in my room you were all
    like ‘Blah blah blah, I’m a big, mean teacher so no,’ or whatever it was you said."
    s "That’s not even remotely close to what I said."
    s "I just said that we don’t {i}always{/i} have to get sexual when we’re alone. Which is true."

    scene ayanesit6

    ay "But I like doing all that stuff with you. It feels really good and touching
    your penis makes my heart beat super fast."
    ay "In fact, even thinking about your penis makes my heart beat super fast."

    stop music fadeout 6.0

    ay "It’s happening right now. Here, come feel it."
    s "..."
    s "Okay, fine."

    scene black
    with dissolve

    "{i}Roughly 10 seconds later...{/i}"

    scene ayanesit9
    with dissolve
    play music "asobeatsex3.mp3"

    ay "There...aren’t you much happier now? It certainly looks like you are."
    s "How did this happen? I was just supposed to feel your heartbeat."
    ay "Yeah, but isn’t this more fun? Look how hard it is already."

    "Ayane wraps her hand around my dick and begins skillfully stroking it."
    "Her innocent smile mixed with her eyes as they fixate on mine bring me closer to ejaculating than I’d like to admit after just a few seconds."
    "The truth is, I’ve wanted to get her in this position since I first saw her in her karate uniform."
    "And, like she said, there’s really no better time than now to indulge in that..."
    "I do wish we could have had sex, though."

    s "Ayane..."
    ay "Yes, Sensei?"
    s "Open your shirt."
    ay "Yes, Sensei..."

    scene ayanesit10
    with dissolve

    ay "Like this?"
    s "Exactly like that."
    ay "Hehe~ I’m happy to please you!"
    ay "You think I look cute in my karate outfit, don’t you?"
    s "Wow, it’s like you were reading my mind."
    ay "Duhh. My life revolves around you. Of course I can read your mind."
    ay "Plus, I also think I look pretty cute in this outfit, so I can’t really
    blame you for wanting to see me like this."
    ay "It feels really naughty, don’t you think, Sensei?"
    ay "Imagine if all those other cute karate-girls were here right now?"
    ay "Do you think they’d get off to watching us?"
    s "You seem strangely aggressive right now..."

    scene ayanesit11

    ay "Hehe~ You think so?"

    "Ayane tightens her grip on my cock and starts moving faster."

    ay "I think they’d get off to us, Sensei. I see them undressing you with their eyes whenever you’re here."
    ay "They probably go home at night and play with themselves while thinking about you."
    ay "So seeing me do this would be a win-win for everyone."
    ay "They win because they get to see your giant penis, and I win because now they know it’s all mine."

    "I continue to get harder as Ayane narrates her rhetorically exhibitionist handjob."
    "It pains me to say this, but I honestly don’t think I’ll last much longer at this point..."

    s "Bold of you to claim it's 'all yours,' Ayane..."
    ay "Really? But look how hard it got for me after just a little touching."
    ay "And it's so hot, too..."
    ay "Are you going to cum soon, Sensei?"
    s "I am...You’re getting really good at this..."

    scene ayanesit10

    ay "You think so? Are you sure it’s not because I’m so cute that you just
    want to explode whenever you see me?"
    s "I mean...that’s definitely part of it..."

    "I subconsciously begin moving my hips closer to Ayane to get a
    better shot at her chest for when I cum."

    scene ayanesit12

    ay "Mmm...mm...ngh...come on..."
    ay "Go on and cum, Sensei. Prove to me that you think I’m the cutest."

    "Her hand traces the entirety of my shaft over and over, occasionally stopping to adjust her grip."
    "As her speed increases, her breaths quicken and become hotter. I can feel them on my skin."

    s "Ayane, I..."
    ay "Cum on me, Sensei. Come on. Do it. I wanna watch."
    s "I..."

    "I feel a pressure building up inside of me and succumb to it, unleashing
    my load all over Ayane’s chest..."

    scene ayanesit13
    with flash
    scene ayanesit14
    with flash

    ay "Mmm-!"

    "Ayane sits there with her eyes closed for a few seconds. She gradually
    loosens her grip around my cock and semen begins to drip down her."

    scene ayanesit15

    ay "Hehe~"
    ay "Don’t you feel all better now that you’ve gotten that out of your system, Sensei?"
    s "I do. But now I’m worried about how you’re going to-"

    scene ayanesit16
    with dissolve

    ay "Hm? Going to what?"
    s "..."
    s "Did you just-"
    ay "I don’t mind. Sure, it feels a little weird and slightly uncomfortable, but
    it’s also kinda like a trophy."
    ay "It’s proof that I was able to make you feel really good."
    ay "Plus it's kind of hot thinking of other people seeing me and not knowing what I'm hiding."

    "I don’t know if I should be enamored or disgusted right now."

    s "Well, you’re free to do as you like. Just don’t bank on me giving you a hug before you leave."

    scene ayanesit17

    ay "What?! You should have told me that beforehand!"

    scene black
    with dissolve
    stop music fadeout 5.0

    "Ayane and I hang out in the dojo before deciding to pack up and leave."
    "As it turns out, she was less comfortable covered in semen than she thought she’d be and wanted
    to go home to take a shower."
    "Being a man of my word, I refuse to hug her as she heads back to the dorms."
    "I do give her a pat on the head, though, so at least there’s that..."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu

label futabadorm20:
    scene black
    with dissolve
    play sound "knock.mp3"

    s "Futaba, are you in there?"
    f "I am! Please come in, Sensei!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

    scene futabadorm
    with dissolve
    show futabaphappy
    with dissolve

    f "Good evening, Sensei. How are you?"
    s "Pretty good, thanks for asking."
    s "You’re not freaking out about being in your pajamas this time?"

    show futabapembarrassedsmile
    hide futabaphappy

    f "Well...I mean...It {i}is{/i} still a little embarrassing..."

    jump futababjx

label futababjx:
    f "But it’s not like we haven’t done anything, umm, {i}more{/i} embarrassing, so..."
    s "More embarrassing? I’m not sure if I know what you’re talking about."

    show futabapembarrassed
    hide futabapembarrassedsmile

    f "S-Sensei! You know exactly what I’m talking about!"
    f "The...h-ha..."
    s "Handjob?"

    show futabapexhausted
    hide futabapembarrassed

    f "Ugh...It sounds so dirty when you say it like that..."
    s "Are you implying that it wasn’t?"

    show futabapwink
    hide futabapexhausted

    f "Of course not. I was just helping you out so you wouldn’t have to be uncomfortable."
    s "Right, right. It was just a generous gesture between friends."
    f "Right."
    s "So if I wanted you to do it again, you would without hesitation."
    f "Ri-"

    show futabapembarrassed
    hide futabapwink

    f "Wait, what?"
    s "You won’t, then?"
    f "I mean...I didn’t say I {i}won’t{/i} but...are you sure?"
    f "Is it...you know..."
    s "It is."
    s "In fact, here’s a tip...I can almost guarantee you that every time you wear those pajamas
    around me, I will be turned-on."
    s "Which, naturally, would mean..."
    f "...Would mean, what?"
    s "...That I expect you to help me feel ‘comfortable’ again."

    show futabapexhausted
    hide futabapembarrassed

    f "Ahhhh...of course this would happen..."
    f "I feel kind of stupid for not expecting it..."
    s "There’s no need to feel stupid. It’s just a simple biological function."
    s "For example, how did you feel while you were jerking me off last time?"

    stop music fadeout 8.0

    show futabapembarrassed
    hide futabapexhausted

    f "Umm...confused?"
    f "Intimidated?"
    s "Not turned on?"

    show futabapembarrassedsmile
    hide futabapembarrassed

    f "That’s...embarrassing to say, though..."
    s "You know I’d be open to helping you ‘feel more comfortable’ as well, right?"

    show futabapembarrassed
    hide futabapembarrassedsmile

    f "Ah! No! That is very much not necessary!"
    f "It’s one thing for me to do something like that to you, but..."
    f "There’s no way {i}I’m{/i} ready to be...t-touched...like that..."
    s "Are you sure? I’m pretty confident in my ability to-"

    show futabapyelling
    hide futabapembarrassedsmile

    f "Very sure! Please remove your pants now so that I may proceed!"
    s "..."
    s "Well, if that’s what must be done..."

    scene black
    with dissolve

    "..."

    scene futababj1
    with dissolve2
    play music "asobeatsex5.mp3" fadein 5.0

    f "Wow...It’s already like this?"
    f "Just from seeing me?"

    scene futababj2

    f "I didn’t realize you were so naughty, Sensei..."
    f "You always seem so laid back and professional..."

    scene futababj3

    f "I guess it would only make sense for you to have so much pent up energy..."

    scene futababj4

    f "But don’t worry...I’ll take good care of you..."

    "Where is this coming from?"
    "The first time we did something like this, she was flustered and confused-"
    "Now she’s telling me she’ll take good care of me and massaging my balls..."

    f "Why do you look so surprised, Sensei?"
    s "It just...seems like you’re really into this today..."

    scene futababj3

    f "Oh? Well, maybe I am."
    f "Like you said, I need to take responsibility for things like this happening."
    f "I’m very sorry you had to experience such discomfort because of me."

    scene futababj2

    f "Just...don’t do it on my face again, okay? That was really mean."
    s "Well, if you want to prevent that from happening, there’s always another way..."

    scene futababj5

    f "Another way? You’re not lying to me again, are you?"
    s "No, no...I’m just saying you could always try using your mouth instead."

    scene futababj6

    f "My mouth? But I was just starting to get comfortable doing it like this..."
    s "Then it’s only natural you’d want to advance to the next level, right?"

    scene futababj1

    f "Maybe if I just...go really fast..."

    "Wanting to avoid learning something different, Futaba starts jerking me off more aggressively."
    "I don’t think she realizes how sensitive certain parts of the male anatomy are, so her
    treatment of my balls actually winds up causing me to be {i}less{/i} aroused..."

    scene futababj7

    f "Huh? What am I doing wrong? Why is it starting to get softer?"
    s "Quick, use your tongue to revive it."

    scene futababj6

    f "My tongue?"
    s "I promise you’ll see an instant improvement."
    f "Ahhhhh...Well, I don’t want to fail, so..."

    scene futababj8
    with dissolve

    f "*lick*"

    "Futaba’s tongue slowly traces its way up the underside of my cock, stopping
    at the tip before circling it several times."

    scene futababj9

    f "*lick* Wow! It really...*chu* is getting hard again!"
    f "I had...mm...no idea this worked that well..."

    scene futababj8

    f "Maybe...*shlick* I’m a natural at this, too, Sensei..."
    f "What do you *mlem* think?"

    "Futaba continues slowly jerking my cock as her tongue dances back and forth across it."
    "I’m not going to lie, she’s somehow phenomenal at this."
    "She pays close attention to every one of my movements and traces back over the head
    each time precum begins to seep out."

    s "You’re...really good at this, Futaba..."

    scene futababj10

    f "Mmm...mmf...mmm...*lick*"

    "Stricken with a new level of self-confidence, she starts stroking
    me harder and licking more aggressively..."

    f "Mmmf...it’s...starting to...*chu* get really hot, Sensei..."
    f "Remember...*lick*...not to go on my face again..."
    s "As long as you let me use your mouth, that won’t be an issue..."
    f "*lick* Then..."

    scene futababj11
    with dissolve

    f "Mmf...mmm...mmm...ngh..."

    "Futaba manages to fit a few inches of my cock into her mouth and begins wrapping her tongue around it."
    "The warmth of her breath and saliva bring me closer to cumming every second."

    scene futababj12

    f "Mmff...am I...doing a good job...*slurp* Sensei?"
    s "Keep going just like that, Futaba...I’m almost there..."

    scene futababj11

    "She closes her eyes again, focusing entirely on pleasuring me."
    "I’m surprised that she’s so open to letting me finish in her mouth, especially for her first time."
    "But I guess it’s better than the alternative in her mind..."

    scene futababj13

    f "Mmf...mm...Sensei...Sensei..."
    s "Keep going..."
    f "Mm...mmm...pah...nfff..."

    "Futaba moves faster, taking more of my cock into her mouth as she tightens her grip around it."
    "Feeling myself being pushed closer to the edge with every stroke, I finally give in..."

    with cumflash
    with cumflash
    scene futababj14
    with cumflash
    with hpunch

    f "Mmmmmmm!!!~~"

    "Surprised by the sudden sensation, Futaba grabs onto my leg and hold her head
    steady, catching every drop of semen she’s able to."
    "Not being able to keep up, however, some of it spills from her mouth..."

    scene futababj15

    f "Mffsssalttttt..."
    s "...What?"

    scene futababj14

    f "Mmm...*gulp*"

    "Futaba swallows what she can, still being kind enough to clean the
    rest off with her tongue shortly after."

    scene futababj16
    with dissolve

    f "Pah..."
    f "I was trying to say that was a lot..."
    s "You think so? I don’t think it was any more than last time."

    scene futababj17

    f "Well it felt like a lot more...but at least none of it got on me."
    s "You were surprisingly good for that being your first time."

    scene futababj18

    f "Heheh~ Well I’m glad I was able to make you feel comfortable again."
    s "And great job swallowing everything too. Not a lot of girls are willing to do that."

    scene futababj19

    f "Do you...have a lot of experience with things like this, Sensei?..."

    "..."

    s "Huh? Oh, uhh. No. Not at all. I just know that from...what I’ve researched...or something."
    f "..."
    f "I hope you’re not lying to me again..."

    scene black
    with dissolve2
    stop music fadeout 5.0

    "I wind up leaving shortly after that exchange."
    "I tried, once again, bringing up the idea of pleasuring Futaba but she shot me down with no hesitation."
    "I wonder why she’s so resistant to have something sexual done to her as well?..."

    scene bedroom_day
    with dissolve

    jump deletedscenemenu
