label shrine:
    if howifeel == True:
        jump howifeel
    if maya_love >= 0 and firsttimeshrine == False:
        jump firsttimeshrine
    if maya_love >= 5 and shrine5 == False:
        jump shrine5
    if maya_love >= 10 and shrine10 == False:
        jump shrine10
    if maya_love >= 15 and shrine10 == True and mayadorm10 == True and shrine15 == False:
        jump shrine15
    if maya_love >= 20 and beachvacation16 == True and mayadorm15 == True and shrine20 == False:
        jump shrine20
    if maya_love >= 25 and mayadorm20 == True and shrine25 == False:
        jump shrine25
    if maya_love >= 30 and mayadorm35 == True and shrine35 == False:
        jump shrine35
    if maya_love >= 30 and mayadorm30 == True and ami_virgin == False and shrine30 == False:
        jump shrine30
    if maya_love >= 40 and nikilovesyou3 == True and shrine40 == False:
        jump shrine40
    if chap4active == True:
        jump mayaspringshrinegen
    if chapthreeactive == True:
        jump mayasummer2shrinegen
    if christmas7 == True:
        jump mayanoongen2
    else:
        jump shrine2to4

label callmayamorning:
    if senseisad == True or mayablock == True:
        "No."
        jump callmorning
    if shrine40 == False:
        play sound "phonebeep.wav"
        "I tap on Maya's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "But of course she doesn't."
        jump callmorning
    else:
        "I tap on Maya's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "I guess she's still sleeping..."
        jump callmorning

label callmayaafternoon:
    if senseisad == True or mayablock == True:
        "No."
        jump callafternoon
    if shrine40 == False:
        play sound "phonebeep.wav"
        "I tap on Maya's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "But of course she doesn't."
        jump callafternoon
    else:
        "Maya should be at the shrine right now. I can probably see her if I go there."
        jump callafternoon

label callmayanight:
    if senseisad == True or mayablock == True:
        "No."
        jump callnight
    if shrine40 == False:
        play sound "phonebeep.wav"
        "I tap on Maya's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "But of course she doesn't."
        jump callnight
    elif shrine40 == True and norikodorm30 == True and mayadate45 == False:
        jump mayadate45
    elif chap4active == True:
        "I tap on Maya's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't."
        jump callnight
    else:
        jump mayanightgen

label mayanoongen2:
    scene mayanoongen2
    with dissolve
    play music "shrinesong.mp3"

    "I head over to the shrine to see what Maya's doing to find that, somehow, it's untouched by snow."
    "Considering the rest of the town is pretty much covered, this comes as a bit of a shock."
    "But I guess it's possible that part of a shrine maiden's duty is...laying out epsom salt?"
    "That's not a thing shrine maidens would do, is it?"
    "I try asking Maya about it but she just gives me some really weird, cryptic response about how some places remain unchanged no matter when you visit them."
    "I give up on trying to understand her and eventually just try talking to her about more normal stuff."

    scene black
    with dissolve

    "Of course, that doesn't work either as she quickly reminds me just how {i}unhappy{/i} she is to see me."
    "We go back and forth, the same way we always do-"
    "And I ultimately lose."
    "The same way I always do."
    "Defeated and demoralized, I bid goodbye to my favorite shrine maiden and let her know that I'll be coming back to see her again soon."
    "She calls me disgusting as I turn around and head for the stairs."

    $ maya_love += 1
    stop music fadeout 5.0

    "{i}Maya's affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label firsttimeshrine:
    scene anewbeginning1
    with dissolve2
    play music "shrinesong.mp3"

    "I find myself wandering up the stairs to one of the last places I ever expected to be."
    "I’m sure that doesn’t mean much to you considering we haven’t known each other very long, but it’s the truth."
    "I’ve never been a religious person. Or...at least I don’t {i}think{/i} I’ve ever been much of a religious person."
    "Ask me again later and I might have a better answer for you. "
    "But for now, I’ll take cover in the shade provided by the clouds within my head and hope to somehow escape this summer heat unscathed."
    "There’s an old saying here where all Japanese are born Shinto and die Buddhist, but just because it’s a commonly used expression doesn’t mean it’s something that applies to all of us."
    "Some of us are simply born. "
    "Some of us simply die."
    "Some of us get lost somewhere in between those two things."
    "And some of us are lucky enough to wake up in an alternate reality based on sheer luck and no influence from any god whatsoever."
    "I’ll throw myself into that category as it keeps me out of debt with any higher power...and I’ll tell myself that the reason I am standing here right now is not because I am seeking salvation."
    "It is not because I am lost."
    "It is because I wanted to spit in God’s face."
    "I contort my mouth into a grotesque shape and allow saliva to pool up inside of my cheeks, but wind up swallowing it all down when a soft set of footsteps head my way to break me out of my daydreaming."

    q "Oh...wonderful. "
    q "Getting started early this time, I see."

    scene anewbeginning2
    with dissolve

    m "And here I was thinking I’d be able to make it at least the first weekend without you showing up and ruining my day."
    s "I’m sorry?"
    m "It’s nothing. Just...complaining to myself."
    s "Well, feel free to complain to me if you like. We’ve known each other long enough that-"

    scene anewbeginning3
    with dissolve

    m "Oh, give me a break. We both know you’re not who you say you are."
    s "I...have no idea what you’re talking about."
    m "Oh? So you {i}didn’t{/i} just happen to wake up inside of that body and assume the role of someone entirely unfamiliar to you?"

    "How...does she know that?"
    "This has to be some sort of trap, right? "
    "If my own niece wasn’t able to pick up on me taking over, why would one of her friends be able to?"

    s "Nope. In fact, that sounds pretty ridiculous."

    scene anewbeginning4
    with dissolve

    m "It does, doesn’t it?"
    m "Allow me to clue you in on something if you’re going to continue being so determined to walk a mile in someone else’s shoes."
    m "The {i}real{/i} you would have never come to a place like this. So, if you’re going to be that dedicated to playing the part, you should probably just leave now before someone else sees you here."

    "Well, at least that’s one thing the previous inhabitant of this body and I have in common."
    "I say, despite acting out of my own character and deciding to come here anyway for no reason whatsoever."

    s "You’re really just...not going to believe me, are you?"
    m "Sorry. I normally have to get to know someone a little better before I start trusting them like that."
    m "Unfortunately for you, you’re one of the last people I’d ever go out of my way to do that with."
    m "So again, quit while you’re ahead and leave. You’ll be saving both of us a great deal of energy."
    s "Just out of curiosity, are you always this confrontational with me? "
    m "Yes. Yes, I am."
    m "But isn’t that something you would already know if you really were {i}you?{/i}"
    s "Didn’t Ami tell you the other day? I’ve been having-"

    scene anewbeginning5
    with dissolve

    m "Memory problems? Is that really the best that all of you can come up with?"
    m "Just once, I’d like to hear a new excuse and not the same...default answer I always get."
    s "For the last time, I’m-"

    scene anewbeginning6
    with dissolve

    m "If you’re the real Sensei, what’s Ami’s birthday? Here, I’ll even give you a hint. It’s sometime in August."
    s "..."
    m "What’s wrong? Have you really forgotten your own niece’s birthday?"
    s "August..."
    m "..."
    s "Seventh?"
    m "..."
    s "..."

    scene anewbeginning7
    with dissolve

    m "Hah..."

    "Fuck."

    m "Just as I thought. And I even gave you a hint this time and everything."
    m "Though...I guess I have no idea if the {i}real{/i} you would have even remembered that answer in the first place. That was just the type of guy he was."
    s "Just the type of guy I {i}am,{/i} you mean."

    scene anewbeginning8
    with dissolve

    m "Seriously? You’re going to keep the charade up even though I’ve already caught you in like, three different ways so far? How stupid are you?"
    s "Correct me if I’m wrong, but I don’t think shrine maidens are really supposed to be talking to people that way."

    scene anewbeginning9
    with dissolve

    m "Fine. I will. You are wrong and this is me correcting you."
    m "Do you feel like an idiot yet? Are you embarrassed at how easily I managed to see through your act?"
    s "Are {i}you{/i} embarrassed wearing that dress?"
    m "Why would I be embarrassed? I am fucking adorable."
    s "I don’t think shrine maidens are supposed to say “fucking adorable” either."
    m "You sure seem to know a lot about shrine maidens for someone who has yet to even pray. "
    m "Is your affinity for girls who dress like me the reason you came here first this time?"
    m "Am I just fetish material for you? Are you that unabashedly perverted?"
    s "No, I just...didn’t really have a choice, I think."

    scene anewbeginning10
    with dissolve

    m "You...didn’t have a choice? What is that supposed to mean?"
    s "After talking to Ami, I left the house. Then...before I knew it, I was walking up the steps and monologuing about the whole “Born Shinto, Die Buddhist” thing."
    m "Oh, is {i}that{/i} why you looked so pathetic on your way up the stairs? I had just assumed it was because you’re getting too old to walk anymore."
    s "Come on. I’m not that old, am I?"
    m "You tell me. At the very least, you should remember your age. Right?"
    s "..."
    m "..."

    "The longer this conversation carries on, the further Maya manages to press me into a corner. "
    "And as much as I want to say I don’t think she’s serious and that this is all just some sort of...vetting process or something, I understand that it’s much more than that."
    "She knows something. "
    "Something about {i}me.{/i}"
    "Something about how I got here or...where we are or...any of the things Ami wasn’t able to fill me in on during our talk earlier."

    s "..."

    "But-"
    "For some reason..."
    "I can’t bring myself to admit that she’s right out loud."
    "And so I do what I imagine I always did in my previous life."
    "I lie through my teeth in hopes of persuading her."

    s "You’re wrong about me, you know."
    m "No, I’m not."

    "As you can see, it doesn’t work."

    scene anewbeginning11
    with dissolve

    m "So...this monologue you speak of...exactly what did it entail?"
    s "Oh? Are you actually interested in something I have to say now? Or are you just going to use this opportunity to mock me a little more?"
    m "I guess it really depends on your answer. I’m not particularly fond of religion, but I’d be lying if I said it didn’t interest me in...some form."
    s "You’re really just full of anti-miko jargon, aren’t you?"
    m "I’m perhaps the world’s worst {i}and{/i} best shrine maiden all at once. Though, I imagine anyone actually good at this wouldn’t really understand what I consider my strong points."
    s "Well, the monologue wasn’t all that interesting. It was moreso just an excuse for me to be fatalistic on the way up the stairs, I think."
    m "I see."

    scene anewbeginning10
    with dissolve

    m "Well, you’re right about it not being interesting if that’s really all it was. So allow me to use this opportunity to tell you more about what {i}I{/i} think."
    m "Do you have a pen and paper on you? Because this is information that I think you’ll want to keep in mind if you really do want to succeed in this world."
    m "{i}Especially{/i} if you have so many alleged memory issues."
    s "I...don’t really carry that sort of stuff with me."
    m "Aren’t you supposed to be a teacher?"
    s "Just...tell me what you’re trying to tell me, Maya."
    m "Okay. But, if you’re anything like the rest of them, you’re not going to remember any of this anyway. "
    s "Then why bother telling me at all? Since you’re so sure of who I am, I mean."
    m "Because despite my cold demeanor and mostly expressionless face...and the fact that I really just abhor you all around-"
    m "I want to give you a head start."
    m "Or a...chance, so to speak."
    m "It’s the least I can do before permanently severing ties with you."
    s "Permanently? Why does it have to be permanent?"
    m "Because I want absolutely nothing to do with you for reasons I don’t have the time to explain today."
    m "If you must, you may speak to me in school. But only when there are others present and only when what you need to speak about pertains to school itself."
    m "Or anything I personally find interesting. But even then, I’d likely rather just think about those things on my own than discuss them with my friend’s grandfather."
    s "Uncle."
    m "Great uncle?"
    s "Just uncle..."
    m "Apologies."

    scene anewbeginning12
    with dissolve

    "Maya closes her eyes and smacks her broom against the ground but, since the hard part of it is facing upward, the soft part is the one that makes contact with the concrete and barely makes a noise at all."
    "Needless to say, it was a failed attempt at looking cool and I’m hoping that whatever her speech is about winds up earning her some bonus points in that department."

    m "There is an infinite amount of worlds out there...and an infinite amount of possibilities within each and every one of them."
    m "And with an infinite amount of people and souls waiting to be recycled, the contents of each one of those worlds are rapidly changing. "
    m "They spin together, but in different directions. "
    m "Sometimes, they spin so fast that parts of them combine. "
    m "With that in mind, each one of those potential worlds in the never ending, ever expanding list of them is like a cocktail of misfortune and agony with an occasional splash of joy and...mint."
    s "Mint?"
    m "Shut up. I’m not done."

    "Maya slaps the ground with the broom again, but actually looks a little bit cool this time."

    m "Somehow or another, despite the endless amount of possibilities and universes overflowing with the opposites of what we desire-"
    m "Somehow or another, you wound up here. "
    m "At the same shrine as me. "
    m "In the same town as me."
    m "Feigning ignorance and pretending that you’ve been here all along is a slap in the face to whatever force or forces brought you before me."
    m "If you believe that force to be coincidence, coincidence is God. "
    m "If you believe it to be some supernatural entity, {i}that{/i} is your God."
    m "But no matter what “God” you choose and what story you decide on, you must remember first and foremost..."

    scene anewbeginning13
    with dissolve

    m "That none of that matters at all."
    s "..."
    m "..."
    s "What?"
    m "None of it. "
    s "Then why did you even bother-"
    m "Because what matters more than {i}how{/i} you got here is what you are going to do now that you are."
    m "Now that you know how the world works, you are free to ignore it...for the most part, at least."
    s "{i}What?{/i}"
    m "Somehow or another, you were given a life in the same space as me. At the same time as me."
    m "And you would be an absolute moron to not make the most of it- whether you call that life yours or accept that it belongs to someone else."
    s "But...why are you telling me this when you’ve already come out and admitted to disliking me?"
    s "Why help me at all?"

    scene anewbeginning14
    with dissolve

    m "The answer to that is one I’ve already alluded to."
    m "And it’s because..."
    m "From this moment on..."

    scene anewbeginning15
    with dissolve

    m "You will have nothing to do with me."
    m "I don’t care how badly you want to see me. I don’t care if it eats at you from the inside out."
    m "You are strictly forbidden from coming here...and you are strictly forbidden from ever even {i}attempting{/i} to get to know me."
    m "The reason I was willing to help you out to the extent I have today is that {i}my{/i} existence is heavily dependent on yours."
    m "And that existence is in grave danger if you do not heed this warning."
    m "Do I make myself clear?"
    s "Absolutely."
    m "So you agree to leave me alone? And to never come here again?"
    s "Absolutely not."
    m "..."
    s "..."
    m "..."
    s "..."

    scene anewbeginning16
    with dissolve

    m "Hah..."

    "There is no slap of the broom this time- just the resigned sigh of a girl who looks like she’s all out of options."

    m "Predictable as ever."
    s "Why is it so important that I stay away from you? And what do you mean when you say that your existence is dependent on mine?"
    m "What I mean is that I want you to stop looking for answers and just go enjoy your exciting new life surrounded by tons of cute girls not named Maya."
    s "But what if I’m only into girls named Maya?"

    scene anewbeginning17
    with dissolve

    m "Then I suggest you find another."
    m "Because getting close to you is the actual worst thing that could possibly happen."
    s "That’s-"
    m "For {i}both{/i} of us. Not just me."

    scene anewbeginning16
    with dissolve

    m "Now, go. I still have work to do around here."
    m "And don’t worry about me revealing your big {i}secret{/i} to any of the other girls. It’s not like they’d even believe me if I told them anyway."
    s "..."
    m "..."
    s "..."
    m "Why have you not left yet?"
    s "I just figured I’d say thank you first."

    scene anewbeginning13
    with dissolve

    m "Oh?"
    s "Especially since I can’t make good on that whole “leaving you alone” thing."
    m "So you intend to drag the two of us into ruin together? Is that really what you want?"
    s "I have no idea what I want. "
    s "I just know that leaving you out of it won’t be part of the plan."

    scene anewbeginning14
    with dissolve

    m "You’re disgusting. Please leave me alone forever."
    s "I’ll leave you alone {i}for now{/i}."
    s "But I’ll be back soon."
    m "Then I suppose I’ll begin looking for hiding places as soon as you leave. I appreciate you for giving me a heads up."
    s "Same here. Just...with the whole parallel universes thing and not the hiding thing. Even if I...barely understood any of what you were talking about."
    m "I knew that you wouldn’t. Your brain is too smooth and full of sexual fantasies involving your niece and her friends. "
    s "You know you’re one of those friends, right?"
    m "Please don’t ruin my lunch for me before I’ve even had a chance to eat it..."

    scene black
    with dissolve2

    "So..."
    "That’s Maya, I guess."
    "..."
    "She’s a little...different from how I expected her to be."
    "Granted, I wasn’t really sure what {i}to{/i} expect since every interaction I’ve had with her up until now has been extremely brief, but..."
    "Having her...aware of my existence when no one else is?"
    "How is that even possible?"
    "And how can she expect me to just leave her alone after {i}revealing{/i} that she knows all of that?"
    "Of course I’m going to keep coming back to her when she’s presenting an entire platter worth of reasons to do that right in front of my face."
    "I just..."
    "I have no idea where to start when I do."
    "Everything on the platter is something I’ve never seen before."
    "..."
    "But, I guess that’s how {i}everything{/i} is for me now."
    "This life. This town. "
    "It’s all one big platter full of beautiful, new things."
    "..."

    stop music

    "And I can’t wait to get my hands on all of them."

    $ renpy.end_replay()
    $ firsttimeshrine = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Enjoy your stay in Kumon-mi!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label shrine2to4:
    play music "hammockofpeace.mp3" fadein 2.0
    scene shrine_noon
    with dissolve

    "I head back to the shrine to see if Maya’s there."
    "As I reach the top of the stairs, I spot her sweeping the area around a donation box."
    "She greets me with a mix of confusion and surprise before asking me why
    I’d willingly come back to a place like this."
    "I tell her it’s out of boredom but, honestly, I just like seeing her in her shrine maiden outfit."
    "Eventually, she asks me to leave so she can go back to
    focusing on her duties, and I find myself walking back down the stairs shortly after..."

    $ maya_love += 1
    $ shrinegeneric = True

    "{i}Maya’s affection has increased to [maya_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0
    "........."
    "......"
    "..."
    jump saturdaynight

label shrine5:
    play music "hammockofpeace.mp3"
    scene shrine_noon
    with dissolve

    "Once again, I find myself at the shrine without much of an objective in mind."
    "I’ve been coming here a lot lately for reasons beyond my comprehension...but even with that, Maya seems no more open to talking to me than she did when I showed up for the first time."
    "Well, the first time by my standards at least. I have no idea how frequently the {i}last{/i} me showed up. But judging by her reaction, I can't imagine it was all that often."
    "In fact, speaking of Maya...where is she? I feel like she normally questions my existence by now. And if she's not here, I really have no reason to-"

    m "Why?..."
    m "Why do you keep doing this?"

    scene mayasweep1
    with fade

    m "You are already aware that I want nothing to do with you, so why? Why do you continue to show up {i}here{/i} despite that?"
    s "I really wish I had a good reason to give you."
    m "Do you have a good reason for literally anything at any point? Because I really just can't imagine that."
    s "Maybe I was just wondering what you were up to? Am I not allowed to show up and...check on my niece's best friend?"
    m "I’m doing the same thing I do every weekend. Does that answer your question? Are you ready to go home now?"
    s "You’re in a different spot than normal, so you're clearly not doing the same thing you do {i}every{/i} weekend."
    m "This may come as a surprise to you, but I have a tendency to move around at various points in the day."
    s "You mean you {i}don't{/i} stop existing the second I take my eyes off of you?"
    m "No, but I often wish I did."
    s "So, do you have some time to spare? We might as well talk since I'm already here, right?"

    scene mayasweep2
    with dissolve

    m "Wrong. This is actually the part where we forget you ever came here and simply move on with our lives."
    m "I’ve already told you that I have no intention of getting to know you and the fact that you are continuing to disregard that is really starting to grate on me."
    s "I understand that. But what I don't understand is {i}why?{/i} What did I ever do to you?"

    scene mayasweep3
    with dissolve

    m "You? Nothing in particular- but that's likely because I haven't let you."
    s "I don't-"
    m "Do you believe that someone needs to have wronged you in order to avoid them?"
    s "Well, no. But-"
    m "Then I suggest you take issue with someone or {i}something{/i} else."
    m "I am in no position to be associating with you right now. Or...ever, for that matter."
    s "In no position? What does that mean?"
    m "It means that simply being {i}near{/i} you has the potential to greatly alter both of our paths. And that the impending fallout would bring nothing but harm to everyone and everything."
    s "That seems like a pretty major repercussion for just trying to learn about you."
    m "It does. Doesn't it?"
    s "Let's just talk. That's all I want."

    scene mayasweep4
    with dissolve

    m "No. I am very much content with who and what I have now, and I will not back down from that stance just because a man old enough to be my grandfather wants to {i}talk to me.{/i}"
    s "Okay, now that was an exaggeration and you know it. You could pass for my daughter at best."

    scene mayasweep2
    with dissolve

    m "It doesn’t make a difference how old you are, really."
    m "You are you and I am me."
    m "We live in different worlds."
    s "Doesn't that contradict that whole thing you said about us living in the same world?"
    m "Have you never heard of a figure of speech before, you pathetic excuse for a man?"
    s "Wow. My bad."
    m "As I was saying...we live in different worlds."
    s "Yeah, well...your friends don’t seem to think that."

    scene mayasweep3
    with dissolve

    m "That's true. Because their judgement has been clouded by a skewed- no. A {i}mutilated{/i} perception of you."
    m "As unfortunate as it is to say this, I'm the only one who knows what you really are and what you hope to gain in this {i}exciting{/i} new life of yours."
    m "But to everyone else? You're the same person you've always been."
    m "In fact, you're likely even {i}better{/i} to them now than you've always been since the {i}real{/i} you wasn't all that great either."
    m "How fun it must be to start off several steps above {i}unremarkable.{/i} Think of how many boobies you'll get to see if you play your cards right."
    s "Hearing you say “boobies” makes me feel weird."
    m "Hearing you say anything at all makes me feel weird. And by weird, I mean nauseous."
    m "To me, you are nothing more than a worm. But to Ami and Ayane, you're the same man they’ve known since childhood. So it's no wonder they're as...forward about their feelings as they are."
    m "The rest are sure to follow suit. It's simply the way things work here."
    m "But I am an outlier. I am an exception to that."
    m "And no amount of shrine visits or half-hearted attempts to disrobe me are going to change that."
    s "..."

    scene mayasweep2
    with dissolve

    m "What? Have you finally run out of things to say?"
    s "It's less that I've run out of things to say and more that I’m still just...kind of confused about who you are."
    s "Or {i}what{/i} you are."
    m "{i}What?{/i} Is that supposed to be some sort of insult?"
    s "Not really. Just a...skeptical inquiry."
    m "Well, I am sorry to disappoint you...but I'm a normal teenage girl."
    s "I don't think normal teenage girls typically talk about how normal they are."
    m "Oh? And how many others have you pressed with the same line of questioning?"
    s "None. But even if I did, I doubt they'd respond like...{i}that.{/i}"
    m "Would it make you feel better if I spoke more like them? Would it get you any closer to leaving?"
    s "Maya-"

    scene mayasweep5
    with dissolve

    m "Good evening, Sensei! I'm sorry to bother you, but I was wondering if you'd be able to help me with my homework after school."
    m "Then, perhaps afterward...we could maybe hold hands and talk about all of the things we like about one another? Doesn't that sound fantastic?"

    "Maya’s voice moves up an octave or two as an incredibly off-putting impression finds its way out of her mouth."

    scene mayasweep3
    with dissolve

    m "There. Was that more in-line with what you've grown used to over your short time here?"
    s "Not really. And, for the record- saying things like that, even if they're done jokingly, doesn't really fit within the lines your character has drawn for itself so far."

    scene mayasweep6
    with dissolve

    m "{i}Hah...{/i}"
    m "What does it even mean to ‘fit?’"
    s "Is it time to get existential again?"

    scene mayasweep1
    with dissolve

    m "Perhaps. That {i}is{/i} within the lines I've allegedly drawn, is it not?"
    s "It's-"
    m "That was a rhetorical question. I know who I am and how I speak."
    m "What I don't know is why {i}you{/i} seem to believe that things should always appear as you expect or want them to without making a conscious effort to mold them into that form."
    m "You're like a...3D puzzle piece trying to blend in with 2D ones atop the coffee table of...some old person who likes puzzles."
    s "I feel like that wasn't as strong as a lot of your other analogies."
    m "What I'm trying to ask is...do you think that {i}you{/i} fit anywhere?"
    s "Sure. I think I fit in pretty well here, at least."

    scene mayasweep6
    with dissolve

    m "Do you? Or do you just {i}think{/i} you do because you’re assuming the role you were placed into?"
    m "You got a head start. Everyone already loves you."
    m "But you know for a fact that they wouldn't if they could see what I see."
    s "..."

    "I’m not really sure how to respond to that."
    "Not because I’m shocked, but because Maya has managed to pinpoint my exact situation with virtually no hesitation at all."
    "This life is only working as well as it is right now because I’m pretending to be someone else."
    "Or at least living inside of their skin and letting my intuition guide me rather than any goals or concrete thoughts."
    "But...how am I supposed to do anything but that?"
    "How can I emulate a person I never knew in real life?"
    "How can I fill these shoes without knowing the shape of the feet that resided within them before mine, burned by the coals of uncertainty, slipped inside?"

    scene mayasweep3
    with dissolve

    m "Is your sudden silence a sign of agreement?"
    s "Who are you?"
    m "I already told you."
    m "I’m a normal [teenage]girl."
    m "Nothing more, nothing less."
    s "You think it’s normal to talk about things like alternate worlds and reincarnation?"
    m "Do you think it’s normal not to?"
    s "When you’re the only person who’s even mentioned something like that to me so far, yeah. I kind of do."
    m "Maybe everyone else is strange? Maybe {i}I'm{/i} the normal one?"
    s "Are you sure that you’re not some type of...omniscient being or something like that?"
    s "You’re a shrine maiden. So if anyone here has some sort of {i}divine influence{/i} or something-"

    scene mayasweep2
    with dissolve

    m "If I had this so-called {i}divine influence{/i} you speak of, don’t you think I would have taken advantage of it by now to make you leave me alone?"
    s "Not if you actually {i}enjoy{/i} my company and are just pretending not to."

    scene mayasweep1
    with dissolve

    m "Ha ha ha. The tsundere role is already filled at our school, I’m afraid."
    s "There can be two. There's no rule against that."
    m "Are we done here? Because I would like to go back to sweeping before the sun sets."
    m "As you can see, this shrine is very large and I am the only person here holding a broom."
    s "And looking very good while doing it."

    scene mayasweep3
    with dissolve

    m "I truly wonder if you will ever make it through an entire conversation without hitting on me."
    s "I think I did a lot better than usual today, so who knows? If I keep improving at this rate, maybe we’ll even start getting along soon?"
    m "Or maybe we won’t and you’ll give up on me entirely."
    s "Sorry, but I can't really see a future where that happens."

    scene mayasweep2
    with dissolve

    m "I'm sure there's one out there somewhere."
    m "There has to be..."

    scene mayasweep3
    with dissolve

    m "Now, please leave. You have insulted this place enough by once again refusing to pray."
    m "And the fact that you are now attempting to woo your [niece]’s best friend is only making things worse. The gods are sure to smite you at this rate."
    s "Okay, okay. I’ll go."
    s "But I'm not going to apologize for bothering you and I want you to know that it is only going to get worse from here on out."

    scene mayasweep2
    with dissolve

    m "Unfortunately, this is one of very few times in my life where I feel obligated to agree with you."
    s "I'll see you later, Maya."
    m "Please don't."

    scene black
    with dissolve2

    "I begin to descend down the shrine's obnoxiously long flight of stairs back to the streets, unsure of what to do with the rest of my day."
    "I don't want to say I've given up on ever understanding Maya at this point, but..."
    "Well, let's just say I've got a lot of work to put in if I ever actually want that to happen..."

    $ renpy.end_replay()
    $ shrine5 = True
    $ maya_love += 1
    stop music fadeout 3.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label shrine10:
    scene shrine_noon
    with dissolve
    play music "hammockofpeace.mp3"

    "I have to stop and catch my breath after finally reaching the top of the shrine's stairs which, and I know this will sound crazy, seem to multiply each time I come here."
    "Perhaps it's due to the fact that it's been getting hotter every day lately..."
    "But it's gotten to the point where the stairs themselves are more of a barrier to me coming here than Maya's incessant commands to distance myself from her."
    "I like Kumon-mi. I mean, why wouldn't I when it seems like everything here was planted with me in mind?"
    "But this weather needs to stop."
    "The fact that I don’t see anyone else around is a testament to that."
    "I guess they all decided it was better to relish in the comfort of their air conditioned apartments than to venture forth to this inglorious hellscape."
    "But here I am once again at the house of {i}God,{/i} searching for who I imagine is His/Her/Its most reluctant servant."

    scene mayasit1
    with fade

    "Fortunately, I don't have to search for long."
    "It seems that this heat has managed to get to Maya as well as she takes shelter in the shade provided by the shrine."

    s "Hey. There wouldn't happen to be a room with air conditioning over here, would there?"
    m "..."

    "Maya doesn’t answer. She simply sits there, unflinching and unbothered by my sudden appearance."
    "Though, perhaps it's not right to really call it {i}sudden{/i} anymore when visiting her is something that's becoming more and more normal with each passing day."
    "The lights behind her attempt to contest the sun in terms of brightness but do nothing more than distract me from what I really want to look at right now."
    "I suppose that might be the point, though. Especially given that Maya has yet to respond to me."

    s "You’re not asleep, are you?"

    scene mayasit2
    with dissolve

    "Slowly, her eyes open and make contact with mine."

    m "Asleep...Awake...Is there really any difference?"
    s "Yes."
    m "I thought that if I ignored your existence entirely, you might go away."
    m "I regret to see that is not the case."
    s "Well, I apologize for letting you down."

    scene mayasit1
    with dissolve

    m "Please sit if you are going to speak with me."
    m "You are obnoxiously tall and I do not want to put any unnecessary strain on my neck."
    s "Sure...but only since you asked so nicely."

    "I take a seat in front of Maya and observe her posture."
    "She sits in perfect seiza position and I can't help but be impressed by how much repetition and muscle reconfiguration it must have taken to make her look like such a statue."
    "I am unable to mimic her, so I simply take my place in a more comfortable position on the floor and hope that I am able to dodge the wrath of God."

    m "You’re thinking something strange, aren’t you?"
    s "Two things, actually. One you'd probably be interested in and one you wouldn't."
    m "You don't intend to tell me the more interesting one, do you?"
    s "Nah. I figure you'll go off on your own tangent soon enough and I don't want to give you any openings."
    m "Is the thought I wouldn't be interested in as vile and objectifying as I expect it to be?"
    s "Do you actually want to know that? Or are you just being sarcastic and confrontational again?"

    scene mayasit2
    with dissolve

    m "I wonder."
    s "I was just admiring how proper you look. That’s all."
    m "I see."
    m "That’s all? Because that seems excessively normal by your standards."
    s "I’ll let you know if anything else comes up."

    scene mayasit1
    with dissolve

    m "Please don't. There is only so much I can take when it comes to the prying eyes of an older man."
    s "Why do you always have to be so hostile toward me?"

    scene mayasit2
    with dissolve

    m "Why do you ask?"
    s "Because I don't get it. I feel like I could say absolutely nothing to you and you'd still do everything in your power to get me to leave."
    m "I likely would. The thought of you standing there in silence while I sit with my eyes closed disturbs me greatly."
    s "I'm not here to {i}disturb{/i} you, Maya."
    m "I have a hard time believing that based on your...persistence."
    s "You realize there are plenty of other girls who would envy this level of persistence from me, right?"
    m "Your tone has suddenly shifted. Have I offended you in some way?"
    s "I'm not {i}offended.{/i} You just...confuse me, I guess."
    m "And what exactly are you confused about?"
    s "Your...outlook on things. Why you think the way you do."
    m "Which {i}things{/i} are you referring to?"
    s "I don't know? Me...relationships...the world-"
    m "Which world?"
    s "Uhh...this world? The one we’re living in."
    s "The first time I came here, you spouted some ridiculous theory about how I’d been...reincarnated or something."
    s "That's not something a normal girl would just come up with off the top of her head, you know. How did you get like this?"
    m "Why are you pretending that was such a {i}ridiculous theory{/i} when we both know it's the truth?"
    m "What could hiding your existence from me, the only person who acknowledges and understands it, possibly do for you?"
    s "..."

    scene mayasit1
    with dissolve

    m "I see everything that you see."
    m "The past. The present. The future."
    m "Every second of it, filtered through a lens unfamiliar to you."
    m "Our sights and memories of the times we wake up and the times we go to sleep may not play in perfect harmony, but the ones we share in this very moment do."
    m "So focusing on what's happening now, while easy, will do absolutely nothing for either one of us in the grand scheme of things when we should be more worried about what happens {i}next.{/i}"

    scene mayasit2
    with dissolve

    m "Which gives me an excellent opportunity to harken back to what you asked when you first showed up today-"
    m "Whether I was awake or asleep."
    m "Does that really make a difference to you knowing what you know now?"
    s "What do I know now? Because nothing you just said makes any sense to me."

    scene mayasit4
    with dissolve

    m "That’s because you’re an idiot."
    s "Are you sure it's not because you're just a fucking weirdo?"
    m "Since you're apparently incapable of following along, perhaps I’ll put it in terms that even someone like {i}you{/i} can understand."

    scene mayasit3
    with dissolve

    m "The key to uncovering this world...or any world for that matter..."
    m "Is {i}perception.{/i}"
    m "There is no defining law of the universe...nor any written guide of what means what or who needs who."
    m "There is no {i}anything.{/i}"
    m "There can't be."
    m "And the reason for that is simple."
    m "Nothing is real."
    m "Well...at least not in the traditional sense."
    m "Technically, everything {i}is{/i} real. But only because that is the way we have decided things to be."
    s "What?"
    m "What I am saying is that this has all happened before...and it will happen again."
    m "Over and over and over. "
    m "Attempting to understand {i}why{/i} things are that way instead of just accepting them is nothing more than a waste of time."
    s "..."
    m "We all see different things...experience different things...yet we still somehow always wind up in the same exact place."
    m "As long as that happens, do the means of how we get there really make any difference?"
    s "What I really want to know is how you ended up {i}here.{/i} What happened to you that made you see life as just...some..."
    m "Predestined string of events, only mildly changing with each passing iteration?"
    s "Sure. That."
    s "Is there, like...some sort of trauma you're keeping locked away or something?"

    scene mayasit1
    with dissolve

    m "Is there anything more traumatic than simply being born?"
    s "Wow."

    scene mayasit2
    with dissolve

    m "I apologize. That was unnecessarily dark."
    m "And I’m sure it hits a bit close to home seeing as you were born {i}again{/i} not too long ago."
    s "{i}Or was I?{/i}"
    m "You were. That isn't even up for debate anymore."
    s "Fine, whatever. But if I'm some sort of...reincarnated soul, what does that make you? Some sort of spirit or something?"

    scene mayasit1
    with dissolve

    m "No."
    m "I am a normal [teenage]girl."
    m "We are but two normal people having a normal conversation on a normal day."
    m "What happened before this and what will happen after it is all part of a cycle."

    scene mayasit2
    with dissolve

    m "We will continue living the lives we have now until they come to their end."
    m "And when that happens, we will start over."
    m "You will meet me and I will meet you."
    m "You will visit me on days like today and discuss why I am the way I am while I keep you at arms length."
    m "You will do your best to learn more about me and I will do my best to ensure that never happens."
    m "It will continuously spiral, much like life itself...circling the drain before disappearing, only to return once things have been purified."
    m "The spiral will continue until you can't even close your eyes without seeing me."
    m "But I will never be any closer to you than an image you can conjure up at will."
    s "..."

    scene mayasit1
    with dissolve

    m "It’s the same for all people, not just you and I..."
    m "This is nothing more than an endlessly repeating string of events. And every single one will be wiped clean after a set amount of time."
    m "So, in order to avoid all of that, it’s best that we just live without thinking."
    m "It's best that we just go our respective ways, neglecting to hurt others as that will prevent us from being hurt in return."
    m "Doesn’t a life like that sound nice and simple?"
    m "Because that is the life I want to lead."
    m "And you are merely getting in the way of things by involving yourself with me."
    s "..."
    m "..."

    "The two of us sit there in silence for what feels like an eternity."
    "Part of me wants to come out and say that Maya’s thoughts on what this life is are...warped beyond recognition, but..."
    "I actually think I get it. Albeit in an incredibly roundabout way."
    "What I think she means is that there are people who live in the moment...and that there are people who live in the past or the future."
    "But Maya has somehow found a way to live in all three at once."
    "I'm sure my way of interpreting that is cutting out a great deal of...weird cosmic influence or whatever it is that's going on in her head-"
    "But I think I understand."
    "I just don't agree with her."
    "If this really is one big cycle where we all end up right back where we started, wouldn't we {i}want{/i} to try and shake things up?"
    "What good does peace bring us if it's not something that can be shared?"
    "And what's the point in avoiding hurting and being hurt if the recycling of those emotions makes it like we never hurt at all?"

    scene mayasit2
    with dissolve

    m "You’ve gone quiet. Could it be that you are finally deciding to leave me alone?"
    s "No. I'm going to annoy you forever."
    m "Oh, joy. Thank you so very much."
    s "Maya, if this really is one big cycle...what I decide to do right now won’t make much of a difference in the long run, right?"

    scene mayasit4
    with dissolve

    m "Is that really all you took from that? Because that's, like...the faintest trace of what I was trying to say."
    s "Get better at expressing yourself, then."
    m "I am plenty good at expressing myself. It's not my fault you're such an idiot who can't follow along."
    s "It's not that I can't follow along. I just-"
    m "Listen. It’s hot and I want to be left alone."
    m "So either you sit here in silence...or you go bother someone else. Okay?"

    scene mayasit1
    with dissolve

    m "I’ve already used up way too much energy by just speaking with you. I’m going to take a nap now and attempt to recover some of that."
    s "Are you really going to take a nap while sitting like that? That can't possibly be comfortable."
    m "..."
    s "..."
    m "..."
    s "..."
    m "..."
    s "..."
    s "Hah..."

    scene black
    with dissolve2

    "It’s hard for me to tell if Maya ever does fall asleep or not, given that her posture remains unmoving for the next thirty minutes."
    "Feeling bored and overheated, I eventually decide to head back into town."
    "I don't think Maya and I became closer today-"
    "But if any of what she said is true, I doubt it would change anything if we did."

    s "..."

    "I don't really want to think about that right now."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine10 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label shrine15:
    scene shrine_noon
    with dissolve
    play music "hammockofpeace.mp3"

    "I arrive at the shrine and discover that Maya is nowhere to be seen."
    "That’s come to be expected at this point, though."
    "I know she's already denied it but, to be 100%% honest, I wouldn’t be surprised if she was using some sort of weird divine powers to sense my location and hide from me."
    "Though, I will say...avoidance aside, I have felt at least {i}slightly{/i} closer to her lately."
    "She even lets me in her room now. That must mean something, right?"
    "Sure, it might be due to the fact that I’ll just bother her even more if she {i}doesn’t{/i} let me in...but what if it's not?"
    "What if underneath the miko dress, there's a girl who-"
    "Who-"

    s "..."

    "My thoughts quickly get wrapped up in the image of what is underneath Maya's dress and I forget what I was previously thinking about."

    s "..."

    "I-"

    s "..."

    "I should probably try and find her..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene noonsky
    with dissolve
    stop music fadeout 20.0

    s "Is...she even here today?"

    "I wander the grounds for a good ten minutes without seeing Maya anywhere."
    "I’m not sure what the schedule for a shrine maiden is like but I'm pretty sure I've heard her say in the past that she's here every weekend."
    "I stop and think for a moment that maybe something happened to her."
    "That maybe someone else got wrapped up in the same thoughts that flooded my head just moments ago."
    "That someone else {i}was{/i} able to find her...and that they acted on them."
    "And that there could be some alley not far from here with a torn hakama and the slender body of a servant of {s}God{/s} god pressed up against the wall."
    "If only I had made it here sooner."

    scene black
    with dissolve2

    "I begin to make my way to the steps of the shrine when the glow of the sun redirects my attention to an area I’ve never seen before."
    "It seems that there is a separate section of the shrine hidden behind a large tree and a few unused donation boxes."

    s "..."

    "I guess one last lap around the grounds wouldn't do any harm."
    "........."
    "......"
    "..."

    scene glowofthesun1
    with dissolve2
    play music "shrinemaiden.mp3"

    "A normal [teenage]girl stands with her head hung low in the glow of the sun as it bleeds its way through broken tree branches."
    "It seems she hasn't noticed my presence as of yet."
    "And she looks so peaceful and beautiful in this moment that I have second thoughts of disturbing her at all."

    play sound "static.mp3"
    scene tree3 with flash
    scene glowofthesun1 with flash
    stop sound

    "But then I remember I need to raise my affection level with her."
    "I remember the sensation of the weakest part of me hardening just moments ago at the thought of what lies underneath that robe."
    "And so I call out, disrupting her midday slumber- killing the peace and beauty along with it."

    s "Ma-"
    m "Good afternoon."

    scene glowofthesun2
    with dissolve

    m "It seems that no place here is truly sacred anymore."
    m "And just when I was starting to believe I’d be able to avoid you today."
    s "It only took me about fifteen minutes to find. I wouldn't call your mission a complete failure."
    m "I suppose not. It might not seem like much to you, but fifteen minutes of peace and quiet goes a long way when you're around."
    m "I did what I could with what little time I had. But I suppose I knew that would come to an end soon enough."
    s "Are you saying you knew I was coming?"

    scene glowofthesun1
    with dissolve

    m "I suppose."
    s "Divine powers again?"
    m "If only it were that simple."

    "A long silence fills the gap between us."
    "I can feel it attempting to force me back toward the stairs I ascended just a short while ago, but I have a hard time tearing myself away from the sight before me."
    "Bathed in the glow of the sun is a girl staking her case as the most forbidden fruit of all."
    "More forbidden than the one with my blood."

    play sound "static.mp3"
    scene amiclass with flash
    scene glowofthesun1 with flash
    stop sound

    "More forbidden than the one who {i}wishes{/i} for that blood."

    play sound "static.mp3"
    scene ayaneclass with flash
    scene glowofthesun1 with flash
    stop sound

    "Before me lies a servant of God who often looks like she'd rather not serve at all."
    "One who shuns not only Him, but me. A girl who walks her own path despite the many hands that attempt to pull her down others."
    "I want to pull at her as well."
    "Not just her hair and not just her clothes, but her. Herself. Down a path that I'm afraid of taking on my own."
    "But what I hope to gain from her company is still uncertain to me."
    "What I hope to gain from almost anything is uncertain to me."
    "But what disgusts me the most is that the one thing I {i}am{/i} certain about wanting would leave her a spasming mess on the floor of my bedroom."
    "The fact that I can think that at all in a place like this is proof that God truly is dead."
    "Either that...or he has simply abandoned us."

    play sound "static.mp3"
    scene mayaclass with flash
    scene glowofthesun5 with flash
    stop sound

    m "What do you want? Why are you coming closer?"
    s "I don’t know."
    s "I just want to, I guess."
    m "Ugh...Don’t you have other places to be? Like...literally {i}anywhere{/i} else?"
    s "Not really, no."
    m "For the love of whoever lives here...stop using your free time on me. I mean it."
    m "There is absolutely nothing good that can come of this."
    s "Nothing at all?"

    scene glowofthesun6
    with dissolve

    m "That's right."
    m "Nothing at all."
    m "You’re close enough to ruin as-is."
    m "One wrong move or strange circumstance may send you spiraling out of control."
    m "You’ll wind up in a place you’ve never seen before."
    m "And suddenly, you’ll be back at the beginning of everything."
    m "Please avoid this string of unfortunate events by spending your time with other girls."
    s "I think I’m good. Getting closer to you is my primary objective right now."

    scene glowofthesun7
    with dissolve

    m "Tch-!"
    m "Stop..."
    m "Treating this..."
    m "Like a fucking game."
    m "I understand how ecstatic you must be to find yourself in a new world surrounded by so many adoring girls...but those girls are {i}people.{/i}"
    m "And as much as I hate to admit it, so are you."
    m "Do not call me an {i}objective.{/i} Not when it lessens the impact of everything I have done so far."

    "That’s...an unusual look for her."
    "I don't think I've ever seen Maya look genuinely angry before."

    s "..."

    "Maybe...I {i}am{/i} pushing her a little too far, after all?"

    scene glowofthesun8
    with dissolve

    m "Why? Why don’t you ever listen to me?"
    s "I...don't really know."
    m "I swear, this version of you is perhaps the most irritating one yet."
    m "Perhaps it's not too late to trade it in for a different one."
    s "I can probably help with that. Do you still have your receipt?"

    scene glowofthesun9
    with dissolve

    m "Why would I keep a receipt for something I never wanted in the first place?"
    s "Bookkeeping, maybe? I don't really know how you handle stuff like that."
    m "Please...just leave this place and carry on with your day. Thank you."
    s "..."

    "Maybe I should try talking to her in a more...{i}Maya{/i} sort of way?..."
    "You know. Appeal to her with vague, thought-provoking questions about different kinds of...spiritual or existential ideas or something."
    "That might work a little better than just...annoying her until she caves."

    s "Hey..."
    m "I said leave."
    s "How do you feel about...fate?"

    "I say the first vague, thought-provoking thing that comes to mind."

    m "..."
    s "..."

    scene glowofthesun10
    with dissolve

    m "What?..."
    s "You know. Fate."
    s "Do you have any...thoughts on it or anything?"
    m "And...why exactly would you ask me something like that?"
    s "Just wondering."
    s "I realize I’ve asked you plenty of questions since showing up here in Kumon-mi...but I thought that maybe I should try asking you something a little different this time."
    m "But why {i}that{/i} question, of all things?"
    s "No reason, I guess. It just sort of came to me."
    m "..."
    s "Or maybe it's because I was just {i}fated{/i} to ask you that?"
    m "..."
    s "..."
    s "I'm sorry."

    "Maya stays quiet for an uncomfortably long time, not reacting to my subpar attempt at a joke."
    "I can’t tell if this means I chose the right topic or the wrong topic."
    "She doesn't normally take this long to respond to...anything, though. So I'm beginning to think that-"

    scene glowofthesun11
    with dissolve

    m "I don’t like this question."

    "Well...I guess it was the wrong topic after all."
    "I’ll just have to think of something else instead."
    "I open my mouth, hoping the right words somehow fall out on their own...but before anything falls, she speaks again."

    m "Fate is...well..."
    m "Inevitable?"
    m "There aren't many things I will openly admit to believing in when it comes to the world and all of its many horrible mysteries."
    m "But that..."
    m "Actually, no. No, I don’t think {i}belief{/i} has anything to do with it at all."
    m "Fate exists. It’s all around us."

    scene glowofthesun12
    with dissolve

    m "Do you remember my talk about how we all see the same thing as one another, just...filtered through different lenses?"
    s "That thing about how we’re all living in some never ending cycle or whatever?"
    m "Yes. That we’ll all wind up in the same place regardless of the decisions we make."
    m "Do you not see the resemblance this carries to your question?"

    "Now that she mentions it, what Maya was talking about back then is essentially the same thing I’m asking her now."
    "I didn't mean it like that, though. I didn't put any thought into this question at all."
    "It was just a random thought that fell out of my head and into her hands."
    "But I’m not sure she realizes that."
    "In her head, she's probably thinking that I’m starting to come around to her unwavering, weird perception of the universe."

    s "I...remember the talk we had. But what I remember more than that is how you fell asleep sitting up at the end of it."
    m "Oh, that? I wasn’t sleeping. I was just waiting for you to leave and {i}pretending{/i} to be sleeping so you would do that."
    s "..."
    m "But that’s beside the point."
    m "{i}You’re{/i} not supposed to be asking questions like these. That is my job and you are stealing my personality."
    m "It’s disgusting. You should be ashamed. Please stop."
    s "Are you...afraid of being written off or something? Because that's not really my intention here."

    scene glowofthesun13
    with dissolve

    m "I'm..."

    "Maya seems to have a hard time answering the question as she trails off and focuses on a line of ants from one place to the next."
    "If she {i}is{/i} afraid of being left and that's why she doesn't want to speak up-"

    m "No."
    m "That’s not it."
    m "I’m just unsure about whether or not you bringing this up has any implications for the immediate future."
    s "What? How would a simple, pointless question like that be able to influence {i}anything{/i} to that extent?"
    m "Don't call it simple...and don't call it pointless. I don't want to hear that."
    m "What matters most is that this is a deviation from the way things are supposed to work."
    m "{i}You{/i} don't ask me questions like this. You just try to get me to like you and fail miserably."
    s "Well, would you prefer I just continue flirting with you instead?"
    m "I..."
    s "..."
    m "I don't really know..."

    "She pauses once more."
    "For a moment, I think I catch a glimpse of her lower lip trembling. But before I'm able to confirm anything, she speaks again."

    scene glowofthesun14
    with dissolve

    m "You’re changing."
    s "...What?"
    m "You’re changing."
    s "In...a good way? Or a bad way?"
    m "A way."
    s "So...can I take this as confirmation that you’re beginning to like me?"
    m "Is that really what you’re concerned about right now?"
    m "Aren’t there more pressing matters at hand?"
    s "More pressing than the affection of a cute shrine maiden? I doubt it."

    scene glowofthesun14r
    with dissolve

    m "Hah...Maybe I spoke too soon..."
    m "Maybe you aren’t changing after all."
    m "Yes...That has to be it."
    m "This was simply a fluke."
    m "An accidental deviation with no real meaning to it."
    s "Exactly. Like I said, I was just trying to say something that you-"
    s "Hey, wait a minute. Why do I feel like what you just said was kind of insulting?"
    m "I don't know. You started talking on your own without letting me finish."
    s "Well, what more did you have to say?"
    m "Not much."

    scene glowofthesun15
    with dissolve

    m "Just that everything is connected."
    m "Life and death..."
    m "Day and night..."
    m "Summer and winter..."
    s "You and me?"
    m "..."

    "I half-expect Maya to greet me with her token deadpan glare after that line but, instead...she focuses on the clouds passing overhead and lets out a sigh."

    m "Yeah..."
    m "You and me..."
    s "..."
    m "..."

    scene black
    with dissolve2

    "The clouds Maya was focusing on passed over the sun seconds later, blacking out the glow that had been dyeing her dress gold."
    "The conversation did not pick up again after that."
    "She just kept looking up-"
    "Even after the light had gone away."
    "..."
    "I left her in her secret hiding place and walked away from the shrine."
    "I'm not sure how long it took for her to notice."

    $ renpy.end_replay()
    $ shrine15 = True
    $ maya_love += 1
    $ connect = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label shrine20:
    scene shrinetwenty1
    with fade
    play music "shrinesong.mp3"

    "I arrive at the shrine to find Maya taking a break from whatever it is shrine maidens do every day, calmly sitting on a rock and not paying much attention to anything."
    "She stares up at the sun as its rays leak through the trees and find their way onto her dress, illuminating her body and turning her almost angelic in nature."
    "Though, I highly doubt angels are as confrontational as her."

    if bonus == True:
        "Ideally, an angel wouldn’t accuse you of sleeping around with [teenage]girls on a daily basis."
    else:
        "Ideally, an angel wouldn’t accuse you of hugging everyone she knows on a daily basis, even if it's mostly true with a few notable exceptions."

    "Or call you a disgusting waste of life in the middle of every conversation."
    "But I guess beggars can’t be choosers, and I am very much a beggar."

    scene shrinetwenty2
    with dissolve

    m "Oh, look. A pervert."
    m "Please leave me alone or I'll be forced to call security."
    s "Hey, Maya."
    m "Hello."
    m "Goodbye, now."
    s "Not goodbye. I’m here to talk to you."

    scene shrinetwenty3
    with dissolve

    m "About what, exactly?"
    s "I don’t know. Probably something that I don’t possess enough intellect to comprehend or follow along with."
    m "So a normal conversation for you."
    s "Yeah, exactly."
    m "I see."
    m "Well, I’m not exactly in a talking mood. So maybe we should just save this for another day?"
    s "You’re never in a talking mood."
    m "That’s not true."
    m "We had a lengthy discussion about stars on the beach just recently."
    m "Or perhaps you’ve already forgotten that?"

    "My mind races back to when I found Maya alone on the shore just an hour or two before Rin’s heart was snapped in half."
    "A lot happened that day, so the conversation is a little foggy, but what I do remember is that it..."
    "Well, it was just another conversation with Maya."

    s "Not entirely. I remember that you like stars."
    m "Yes. An important character trait."
    m "Take note of that in your journal."
    s "Sure. I’ll put it right next to “Hates my guts” and “Likes watermelons.”"

    scene shrinetwenty4
    with dissolve

    m "I don’t think “Hate” even begins to describe my feelings toward you."
    s "It’s fine. I’ll just scratch that part out and fill it with a bunch of question marks, then."
    m "Thank you. I’d also edit your entry in my journal, but I was afraid it would begin to bleed into the other pages, so I already tore it out and set it on fire."
    s "That’s rude."
    m "It burned up very quickly."
    s "Thanks. That’s a thing I wanted to know."

    scene shrinetwenty3
    with dissolve

    m "That aside, has anything else changed since you’ve come back from vacation?"
    m "The ending must have been rather eventful for you."
    s "How do you know about the ending?"
    m "It’s hard to not overhear things when everyone is so close together."
    m "Perhaps I stumbled upon a stray conversation or two while I was out watching the stars?"
    m "Such a thing could happen, could it not?"
    s "It could. But I feel like things aren’t usually as they seem with you."

    scene shrinetwenty5
    with dissolve

    m "Oh?"
    m "I’m not sure what you mean. I’m just a normal [teenage]girl."
    m "Everything I say is exactly as it is. I have nothing to hide, especially from someone like you."
    s "If you have nothing to hide, then how about we talk about your past for a little while? Or your interests. "
    s "Anything to make me feel like we’re getting somewhere."

    scene shrinetwenty6
    with dissolve

    if bonus == True:
        m "Maya Makinami. Age, [[redacted]. My hobbies include watermelons and the violin. My past is of none of your concern."
    else:
        m "Maya Makinami. Height, short. My hobbies include watermelons and the violin. My past is of none of your concern."

    s "Watermelons aren’t a hobby, Maya."

    scene shrinetwenty2
    with dissolve

    m "And stalking shrine maidens is?"
    s "I’m not stalking you."
    m "Yes you are. I was enjoying my break and you just showed up and started asking me questions about myself."
    s "What are you even taking a break from? All you do is sweep."
    m "Then I suppose I am taking a break from sweeping."
    m "Are we done now? Or are you going to pester me more?"
    s "I’m going to pester you more."

    scene shrinetwenty6
    with dissolve

    m "Of course you are."

    "Maya lets out a heavy sigh and squeezes her arm. "
    "I can feel her getting annoyed, but I doubt it’s any more annoyed than {i}I{/i} am having to keep up with her all the time."

    s "How was vacation for you? Other than spending the bulk of your second night watching the stars, I mean."

    scene shrinetwenty2
    with dissolve

    if bonus == True:
        m "I wasn’t very fond of the part where you walked in on me getting changed, but other than that it was fine."
    else:
        m "I wasn’t very fond of the part where you existed, but other than that it was fine."

    s "That was actually one of my favorite parts of the whole weekend. "
    m "You’re disgusting."
    m "And yes, I know I’ve said that many times now."
    m "You create too many opportunities. "
    m "You should try being less horrible."
    s "But then I wouldn’t be me."

    scene shrinetwenty7
    with dissolve

    m "That’s debatable."
    m "You still don’t even know who {i}you{/i} are. Isn’t that right?"
    s "You’re right, I don’t. And, to be honest, it’s pretty hard figuring that out without any help."
    s "You’d think if you really wanted me to succeed at this whole ‘reincarnation’ thing, you might actually help me."
    s "Given that you’re the one person who seems to know what’s going on."

    scene shrinetwenty2
    with dissolve

    m "You succeeding only makes things harder for me."
    m "I need you to fail to a certain degree."
    m "Also, I’d appreciate it if you’d stop assuming that I know what’s going on."

    scene shrinetwenty7
    with dissolve

    m "I told you this on the beach, but this world isn’t something I have complete control over. I just know how to manipulate certain parts of it to make things easier."
    m "If “easier” is even the right word to describe it. "
    m "Sometimes, I don’t think it is."
    s "I’m lost again."

    scene shrinetwenty5
    with dissolve

    m "We’re all lost. "
    m "But that doesn’t mean we can’t find our way."
    m "We just need to follow the appropriate steps."
    s "And I’m assuming those steps involve not getting closer to you."

    scene shrinetwenty8
    with dissolve

    m "Perhaps they do. Perhaps they don’t."
    m "What would I know? I’m just a normal [teenage]girl."
    s "A normal [teenage]girl with a set of very abnormal circumstances."
    m "There’s a difference between abnormal circumstances and horrible luck."
    m "Though, I suppose I’ve been blessed with both."
    s "..."
    m "..."

    scene shrinetwenty9
    with dissolve

    m "If you knew when the world was going to end, what would you do about it?"
    s "Is this about the reset thing?"
    m "Perhaps it is. Perhaps it isn’t."
    s "Well, knowing what would happen {i}after{/i} the end of the world would play a big part in determining that."
    s "If I didn’t know the world would just be starting over again, I’d probably spend my last days making sure I don’t have any regrets."
    s "But, if I know things are just going to start over, I don’t think I’d change much at all."
    m "No. You wouldn’t."
    m "You’d keep doing everything exactly the same way while everyone else faces the apocalypse."
    m "Then, you’d watch as a new world forms and fills back up with everything you’ve grown to know over your time there."

    scene shrinetwenty6
    with dissolve

    m "But then, that begins to raise questions."
    m "Is the new world that generates the same as the old one?"
    m "If all of the buildings and structures stay the same, but the people filling them are all replaced with identical copies equipped with altered minds, can we still call it the same world?"
    s "I guess that depends on how much of a person’s worth is tied to their memories."

    scene shrinetwenty2
    with dissolve

    m "That’s a surprisingly insightful answer. Please explain yourself."
    s "Well, after the first reset, everything felt exactly the same. "
    s "It was like the only thing that actually changed was where we were in time."
    s "But the only people that seem to realize that are you and me."
    m "Is that what you believe?"
    s "Is that not the case?"

    scene shrinetwenty7
    with dissolve

    m "I’m not sure."
    m "It’s a confusing situation."
    m "Pretty soon, the seasons will change. "
    m "We’ll be walking to[school] in the snow instead of the sun, and yet no one will think anything of it."
    m "No one but us."
    m "Why is that?"
    m "Something about the way time flows here is different than it should be."

    "Wait, will everyone really just be acting normal once winter comes?"
    "I know it’s right around the corner, but I figured there’d at least be some sort of reaction from people when we get there."

    scene shrinetwenty9
    with dissolve

    m "But I guess things like that don’t particularly matter to you, do they?"
    m "You’re just here to advance yourself."
    m "You’ll treat this like it’s all just a game and, eventually, you too will reach the end."

    scene shrinetwenty10
    with dissolve

    m "But what happens after the credits roll?"
    m "What becomes of everyone inside of that game?"
    m "And what happens if they don’t reset along with the others the next time you press “Start?”"

    scene shrinetwenty11
    with dissolve

    m "I don’t know how many times I’ve said this to you, but this isn’t a game. "
    m "You only think it is."

    "Has she said that to me at all before? "
    "I can’t remember..."

    s "Who says that I think this is a game?"
    s "It's true that, at first, I may have approached it as one."
    s "But as time goes by, I’m beginning to think that this is where I belong. "
    s "I’ll admit that I haven’t been here all that long in the grand scheme of things, but the progress I’ve made with everyone is real."
    s "Isn’t it?"

    scene shrinetwenty6
    with dissolve

    m "Obviously, I won’t know the answer to that."
    m "It’s up to you to figure out what is real and what isn’t."
    m "I’ve already come up with my answer, but you need to learn to think for yourself."
    m "If something feels real to you, then it’s probably real."
    m "But, knowing the type of person you are now, I can’t imagine anything will ever feel that way again."
    s "You feel real to me."

    scene shrinetwenty5
    with dissolve

    m "I’m really, {i}really{/i} tired of hearing that line."
    m "It was cute the first time, but now it’s just getting annoying."
    s "How many times have you heard it exactly?"
    m "Almost the same amount of times I’ve heard that one."
    m "And the one you’ll say after that."

    scene shrinetwenty8
    with dissolve

    m "Sure, there are some minor changes here and there, but everything follows the same pattern for the most part."

    scene shrinetwenty12
    with dissolve

    m "It’s all part of the cycle."
    m "But that’s something you already know."
    m "For now, at least. "
    m "Just keep on living and forget about all of my ramblings. "
    m "Frankly, I’m getting tired of having to explain myself."
    m "Perhaps I should just let you figure things out on your own from now on?"
    s "Definitely don’t do that. "
    s "Part of me feels like I would have gotten caught in that pre-reset loop for months without your help."

    scene shrinetwenty5
    with dissolve

    m "In some regard, I’m sure you already have."

    scene shrinetwenty2
    with dissolve

    m "But, now it’s time for me to get back to work."
    s "Already? But I just got here."
    m "And you’ll be here again."
    m "To be fair, you got a lot more out of me today than you’re supposed to. "
    s "Yeah, you’re rather talkative for someone who isn't in a talkative mood."
    m "And you’re rather obnoxious for someone who is."

    scene shrinetwenty12
    with dissolve

    m "Oh. By the way-"
    m "I may require your help again in the near future. "
    m "I hope you don’t mind carrying a few more boxes."

    scene black
    with dissolve2

    "Maya gets up off of the rock and begins to walk away without saying goodbye."
    "As confused as I am (Both about the boxes and the entire conversation we just had) I don’t call out to her."
    "She was right in saying that I got a lot more out of her today than I normally do."
    "But, even with that, I still don’t feel much closer to her. "
    "I wonder if the two of us will ever meet up on the same wavelength in the future?"
    "And, if so-"
    "I wonder how long it will take to get there."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine20 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label shrine25:
    scene shrine_noon
    with dissolve
    play music "hammockofpeace.mp3"

    "It’s another hot day here at the end of Summer."
    "The shrine is uncrowded, as per usual on days like this."
    "A cool breeze sweeps through the grounds and provides temporary respite from the harsh rays of the sun."
    "Maya is nowhere to be found."
    "She’s probably hiding from me."
    "She seems to do that rather frequently, I’m finding."
    "It’s a little confusing given that I’ve never really gotten anything out of it other than seeing her in a cute outfit, but..."
    "There are plenty of girls in plenty of places- each with their own cute outfits."
    "Why am I gravitating to the one who’d sooner save a watermelon from falling off of a cliff than me?"
    "Sure, there aren’t many scenarios I can imagine where she’d be forced to choose between those two things-"
    "But we all know which one she’d pick if she was forced to."

    scene black
    with dissolve

    "I take a look around the shrine, checking all of her usual spots."
    "She’s not in any of them."
    "Wait. No."
    "She has to be somewhere."
    "Every time I think to myself, “Maybe she has the day off,” I wind up finding her in another peculiar place."
    "I just need to completely scan the area..."
    "........."
    "......"
    "..."

    scene mayaglow1
    with dissolve

    "After another five minutes or so, I spot her finding refuge in an old, otherwise unused booth of the shrine."
    "She doesn’t notice me approaching as she focuses on the world around her."
    "Dust particles, which had remained undisturbed for {s}God{/s} who knows how long, swim through the space around her and find their place among the air we breathe."
    "Did you know that the average human being consumes almost 10 lbs of dust every year?"
    "I wonder how many other things we unknowingly consume."
    "I wonder how our lives would change if we knew about them."

    s "Hey."

    scene mayaglow2
    with dissolve

    m "...Hi."
    s "I found you."
    m "Yes. It appears you did."
    m "I’m running out of safe places to take shelter."
    m "I might need to start tending to another shrine soon."
    s "Would you really go through the hassle of finding another shrine just to get away from me?"
    m "I wouldn’t need to find them. I know where they are."
    s "Oh. Well, could you tell me? I’d like to check them out."

    scene mayaglow3
    with dissolve

    m "Do you really think I’m going to fall for such an obvious ploy?"
    s "What ploy? Maybe I just...really like shrines?"
    m "The first time you came here, you said you didn’t even know why you’d shown up."
    m "I doubt that the time you’ve spent here has, in any way, sparked your interest in them."
    m "I don’t even think I’ve seen you pray yet."
    s "And you likely never will. There’s no point in praying."

    scene mayaglow4
    with dissolve

    m "A right and a wrong answer wrapped together in one sentence. How interesting."
    s "What do you mean by that?"
    m "Praying isn’t entirely pointless as long as the person doing it believes that something will happen in response."
    m "Of course, this doesn’t change the fact that anything that comes subsequently will be the result of coincidence rather than divine intervention-"
    m "But beliefs are beliefs nonetheless."
    s "So is that why you spend so much time here? To help people believe?"

    scene mayaglow2
    with dissolve

    m "Not at all. I couldn’t care less about what other people believe."
    m "I don’t even like shrines. "
    s "Then you should probably find a job that you enjoy. I’m sure there are plenty of girls who actually believe in god who would be happy to spend their afternoons sweeping up here."
    m "Probably. But that’s just not how things are supposed to go."
    m "Besides, I look cute in this dress."
    m "Can you honestly look at me and tell me I don’t belong here?"
    m "Actually, wait. Don’t answer that. I feel as if you’ll talk for hours on end about it."
    s "I like you more when you’re not being conceited."
    m "Then I will continue to praise myself so your disdain for me may grow as if it is a tree."

    if trinity1track == True:
        play sound "static.mp3"
        scene callous19
        with flash
        scene mayaglow2
        with flash
        stop sound

    "I’m not sure what it is about that last sentence, but it pisses me off for some reason."
    "It’s not uncommon for Maya to say things for the sole purpose of making me feel like shit, but that one was just different."
    "I wonder why?"

    scene mayaglow4
    with dissolve

    m "Are you excited for the cold?"
    m "You’ve always liked winter more than summer."
    m "It’s one of the few things we have in common."
    s "More than anything, I think I’m just excited to see everyone in their winter clothes. "
    s "Summer clothes are nice and all, but they just don’t have the same appeal as a girl dressed in layers."
    m "You’re disgusting."
    s "How is it disgusting wanting to see a girl in {i}more{/i} clothes?"

    if bonus == True:
        m "It’s disgusting that you felt compelled to share your sexual attractions with me in response to a wholesome question."
    else:
        m "I don't know. It just is."

    m "What even are you?"
    s "I’m a normal [teenage]girl."

    scene mayaglow5
    with dissolve

    m "..."
    m "Why is everyone doing impressions of me lately?"
    m "It’s starting to get on my nerves."
    s "To be fair, you make it very easy."

    scene mayaglow6
    with dissolve

    m "Hah...Yes, I suppose I’ve become rather predictable over time."
    m "But that doesn’t excuse mocking someone."
    m "Please leave the shrine as penance for your actions here today."
    s "Nah, I want to stay here and talk more about the weather with you."

    scene mayaglow7
    with dissolve

    m "Wow, what an interesting topic for conversation."
    s "Weren’t {i}you{/i} the one who brought it up in the first place? I’m just following your lead."
    m "Being interesting hasn’t ever been one of my strong suits."
    s "That’s not true. You’re plenty interesting."
    s "Just in the “I have no idea what you’re talking about” way rather than the “What an exciting person to be around” sort of way."

    if bonus == True:
        m "Thank you for your wonderful, in-depth analysis of my character. Please include that in my recommendation letter for college."
        s "Jokes on you. You’re never going to make it to college if the world keeps resetting every few months."
    else:
        m "Thank you for your wonderful, in-depth analysis of my character. I look forward to reading more of your future fan theories."
        s "Joke's on you. I already have the whole game figured out."

    scene mayaglow8
    with dissolve

    if bonus == True:
        m "No. I suppose I won’t. "

    m "Perhaps I’ll finally find it in myself to ask for a class-transfer once the next cycle starts?"
    s "Oh, about that. There’s something I’ve been wondering."

    scene mayaglow9
    with dissolve

    m "You? Wondering something?"
    m "I’m absolutely shocked."

    scene mayaglow2
    with dissolve

    m "What is it?"
    s "How exactly is this whole switch to winter thing going to work?"
    s "There’s not much time left in the[school] year as-is, so it seems like winter is going to fall right around the same time that things start over."
    m "Correct."
    m "I'll be finalizing the switch during the next reset."
    s "You can change the weather as well?"
    m "Not exactly. It's complicated."
    s "Well...won’t everyone think it’s a little weird if it’s snowing in the middle of the[school] year?"

    scene mayaglow1
    with dissolve

    m "You really took your time asking that question, didn’t you?"
    m "You’re not wrong in being confused about it."
    m "While it’s true that most people would think snow in the middle of the[school] year is strange, something about the flow of time here prevents that from happening."
    m "It’s as if everyone’s perception of time itself resets along with the world."
    m "It’s just one more thing I don’t yet understand."
    s "That sounds...strangely convenient."

    scene mayaglow11
    with dissolve

    m "I can assure you that there is nothing convenient about this world at all."
    m "It’s filled with horrible things. Yourself included."
    s "Oh come on. I didn’t even say anything to warrant being insulted this time."
    m "Your existence itself is enough to warrant being insulted."
    s "Thanks. I love you too."

    scene mayaglow10
    with dissolve

    m "Anyway..."
    m "You needn’t concern yourself with something as trivial as how those around you will think of snow during the[school] year."
    m "There are many things that will happen in the future that are sure to confuse you."
    m "I am no exception to that. "
    m "The important thing is that you live each day as if you are meant to be here."
    m "Question everything, but accept that many things seem to come without answer."
    m "But most importantly, don’t be afraid."
    m "You, too, shall vanish one day."
    m "It’s absolutely imperative that you be ready for it at any given moment."
    s "..."

    "I hate hearing things like that."
    "I heard it on the beach, too."
    "It’s great that someone like Maya exists to shine light on the world I was reborn into-"
    "But each time I’m reminded that my existence is just as fleeting as a six-month Summer, I can’t help but be swallowed by dread."
    "It really could happen at any given moment."

    s "What are you going to do if that does happen?"

    scene mayaglow11
    with dissolve

    m "Hm?"
    m "Do you mean if it happens to {i}you{/i}? Or if it happens to me?"
    s "Both, I guess."
    s "How would your life change if this version of me were to vanish?"
    s "And how would it change if you were the one to vanish instead?"
    m "I don’t like that question. Ask a new one."
    s "What? Why?"
    m "It’s not easy to answer. It would take far too long."
    m "Let me ask you a question instead."
    m "What would {i}you{/i} do if this version of me vanished?"
    m "What if, after the next reset, there was a brand new Maya Makinami?"
    m "One who didn’t know too much about the world."
    m "One who didn’t know too much about you."
    m "Would you treat her the same way you treat everyone else?"

    if bonus == True:
        m "With lascivious glances and spontaneous visits to her dorm room in the middle of the night?"
        m "Would you view her as another piece of the puzzle? Another girl in the harem?"

    m "Or would you try to bring the old one back?"
    s "..."
    m "..."
    s "You’re right. This {i}is{/i} a hard question."

    "While I do like the idea of a Maya who doesn’t look at me with dead eyes every time I see her, would that {i}really{/i} be Maya?"
    "No. Of course not."
    "Even if she had all the same interests...watermelons and violin, those dead eyes are what I expect to see each and every time we meet."
    "Replacing them with brand new ones just wouldn’t feel right."

    scene mayaglow12
    with dissolve

    m "I’m glad you understand."
    m "You haven’t been here long, so I won’t fault you for believing that a world like this has its own unique set of benefits and positives."
    m "But the negatives that come with it are much worse."
    m "It’s hard enough living each day knowing that death could come at any moment."
    m "But a place like this will remind you of that with each and every passing second."
    m "Nothing lasts forever, even when it does."
    s "..."
    m "..."

    scene mayaglow2
    with dissolve

    m "Well, I suppose that’s enough sentimentality and exposition for the day."
    m "Please leave now."
    s "Wait, really? I thought we were about to have a breakthrough."
    m "We were not."
    s "But what about all of that stuff about how death could come at any moment? What if I disappear on the way home?"
    s "Wouldn't you be upset?"
    m "I have the worst luck out of anyone in the world, so I firmly believe you’ll be back here as soon as you possibly can be."
    s "Well {i}sorry{/i} that my continued living adds to your misfortune."
    m "Apology accepted. Goodbye now."
    s "..."
    m "..."
    s "...Fine."
    s "But I’m only leaving because I have other stuff to do."
    m "And to think you’ve called {i}me{/i} tsundere on multiple occasions..."

    scene black
    with dissolve2

    "The dust settles and the sun begins to disappear behind the clouds."
    "Maya retreats into another section of the shrine and I, just as always, must figure out what to do with the rest of my time today..."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine25 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label shrine30:
    scene mayalantern1
    with fade
    play music "shrinesong.mp3"

    "I spot Maya shortly after arriving at the shrine and make my way over to her."
    "It’s still suspiciously warm around here (For reasons I’ve yet to understand), but it seems that she’s taken up shelter in a booth with her back to a pair of large glowing lanterns."
    "I can feel their heat from here, which is great considering her gaze is ice cold."
    "Here’s hoping they thaw her out sometime soon."

    s "Yo."
    m "..."
    s "What’s up?"
    m "..."
    s "Are you ignoring me now?"
    m "I’m conserving energy."
    s "Are you about to go into hibernation for the rest of the winter or something?"
    m "I wish."
    s "What do you need to conserve energy for?"
    m "Daily activities. Getting out of bed. Brushing my teeth."
    m "An overabundance of stress from having to put up with you all the time."
    m "The usual."
    s "Is there an extra spot inside of that booth? There’s this one girl who keeps bossing me around and it’s getting to me as well."

    scene mayalantern2
    with dissolve

    m "Stop saying that I’m bossing you around. I haven’t asked you to do a single thing today."
    s "I mean...I just got here."
    m "And {i}I{/i} got the message loud and clear the other night. "
    m "You’re not going to ignore Noriko, so I’m just going to have to figure out a new way to deal with that."
    m "If you wind up disappearing, though, don’t say I didn’t warn you."
    m "I mean...you wouldn’t be able to say anything because you disappeared. But you know what I mean."
    m "It’s not like she has anything interesting to tell you anyway. Your old life was boring and sad."
    s "You get really grumpy when you’re stressed, huh?"
    m "I’m hungry, too. But I have to hang out at this stupid shrine and pretend there is a god."
    m "It’s quite taxing."
    s "Just leave if you hate it here that much."
    s "Let’s go get lunch or something."

    scene mayalantern3
    with dissolve

    m "Together?"
    s "Maya, we’ve eaten together several times."
    m "Not {i}lunch{/i}, though."
    m "We’ve always gone out late at night so I wouldn’t feel weird about anyone seeing us together."
    m "And I was only fine with Uta seeing us because, until recently, I didn’t think it was possible for fate to get so out of sorts that she’d wind up several desks away from me."
    m "And even though all we did was eat, I now have to face her constant accusations about us being boyfriend and shrine maiden."
    s "Why not just say “boyfriend and girlfriend?”"
    m "I was about to, but I got nauseous."
    s "I figured as much."
    s "I wouldn’t worry if I were you, though."
    s "I’m pretty sure that everyone knows we’re not romantically involved by now."

    scene mayalantern4
    with dissolve

    m "Yeah...I don’t really know if that’s exactly true anymore."
    s "What do you mean?"
    m "I mean that my...reaction to Noriko’s appearance in class has caused some people to second guess the nature of our relationship."
    s "Really?"
    s "Well, I guess this means we have to start dating."

    scene mayalantern5
    with dissolve

    m "Please don’t joke about things like that."
    m "Until now, I managed to fly completely under the radar and not get wrapped up in any of your senseless hidden romance drama."
    m "Now, even Ayane is accusing me of having feelings for you. And I hate seeing Ayane act serious. It’s unsettling."
    s "Yeah...that doesn’t happen often, does it?"
    m "The point is...it’s important, now more than ever, for the two of us to maintain distance."
    s "Ever? In all of the gajillion years we’ve known each other?"

    scene mayalantern6
    with dissolve

    m "First off, that’s not even a real number."
    m "Secondly, don’t get into semantics with me."
    m "When someone says “now more than ever” it very rarely means “now more than ever.”"
    m "It just means that it’s extremely important. Which it is."

    scene mayalantern7
    with dissolve

    m "The two of us are not to be seen out and about with one another. There is far too much at stake."
    m "This has been a rule for a very long time, Sensei. You should be fully aware of it by now."
    s "I never really thought of it as a “rule.” I just figured that’s how you are."
    m "And in thinking that, you are exactly right."
    m "I’m cold and blunt. A kuudere with slowly dissipating “cool” and “dere” buried somewhere so far underground that you’ll likely never find it."

    if mayadorm35 == True and bonus == True:
        "Yeah, I'm pretty sure I found it when she almost [rape]d me the other night."

    s "The “dere” part exists?"
    m "That was mostly a joke. You weren’t meant to take it seriously."
    s "Too late. I need to go buy a shovel."
    s "See you, Maya."

    scene mayalantern8
    with dissolve

    m "You’re disgusting."
    s "That may very well be true, but I’m not the one under suspicion, now am I?"
    m "What are you talking about? You’re literally always under suspicion."
    m "Any of those poor girls who think you’re not two...three...or ten-timing them are just choosing to be ignorant about it."
    s "And yet {i}you’re{/i} the one Ayane is apparently questioning."
    m "Oh please. As if she hasn’t questioned you as well."
    m "What did you tell her? That you can’t promise to be with only her but that she’s still extremely important to you or blah blah blah?"
    s "Wow. You really {i}are{/i} grouchy today."
    m "The grouchiest."
    m "I can’t remember the last time I actually had to think this much. It’s putting me on edge."
    s "Well {i}I{/i} personally like this side of you."
    s "It feels like we’re getting somewhere."
    m "{i}This{/i} is your idea of getting somewhere? Slightly more facial expressions and openly confronting you about your relationships with my friends?"
    s "Sure. We’re talking about things I can finally understand."
    m "You understand all of the other stuff we talk about as well. You just choose to act aloof about it because the second a theory starts sitting in your head, it becomes too real and you want to run away."
    m "It’s just how your brain is wired."

    if bonus == True:
        m "Mine is the same way, but with less pent up sexual aggression and more quantum theory and food."
    else:
        m "Mine is the same way, but with less pent up desire to hug everything and more...quantum theory and food."

    if mayadorm35 == True:
        if bonus == True:
            s "Trivia time. Which of the two participants in this conversation has mounted the other in an effort to coerce them into sex?"
        else:
            s "Trivia time. Which of the two participants in this conversation has mounted the other in an effort to force them into a hug?"

        scene mayalantern2
        with dissolve

        m "Stop bringing that up!"

        if bonus == True:
            s "I'm just countering your whole thing about not being sexually aggressive when my personal experiences prove otherwise."
            m "That didn't count! It was an act of desperation, not sexual aggression!"
            m "I'm done talking about this!"
        else:
            s "All I'm saying is that there is clearly more than one hug addict at this shrine right now."
    else:
        if bonus == True:
            s "Is there any sexual aggression in there at all?"
            s "Up until now, I’ve gotten a really intense asexual vibe from you."
            m "Good. Please continue to think that. I’m not open to discussing those sorts of things."
        else:
            s "Do you even like hugs, Maya? Because I really have no idea how you feel about them."
            m "They are certainly a thing that exists."

    s "You’re such a buzzkill."

    if bonus == True:
        m "How? You have half a classroom worth of girls who you’re likely sleeping with already. Talk to one of them about that if you truly need to."
    else:
        m "How? You really expect everyone else around you to think about hugs just as frequently? Give me a break."
        m "Like, have you ever actually thought about how weird the concept of hugging even is? It's fucking wild, dude. I don't get it at all."
        s "But they are so warm and soft and nice."

    m "I’ll continue to sit inside this booth and think about clouds."
    s "..."
    m "..."

    if bonus == True:
        s "Okay, so let’s say that...theoretically, I {i}am{/i} sleeping with some of the girls."
    else:
        s "Okay, so let’s say that...theoretically, I {i}have{/i} hugged a sizable portion of the cast."

    m "..."
    s "How would that make you feel?"
    m "..."
    s "..."
    m "What is this?"
    m "Are you trying to get me to say I’m jealous?"
    s "I’m searching for the “dere.”"

    scene mayalantern9
    with dissolve

    m "Hah..."
    m "I’d feel the same exact way I’ve felt all along."

    if bonus == True:
        m "You’re a horrible person with a disgusting addiction and an affinity for girls well under the age you should be setting your sights on."
    else:
        m "Hungry and tired."

    scene mayalantern10
    with dissolve

    m "And even though I think that side of you is despicable and wish it would go away...I don’t hold it against anyone."
    m "Well, maybe I do hold it against you. But not any of them."
    m "They’re just normal girls who are blissfully unaware that they’re caught in a loop."
    m "Falling for version after version of the same [high_school] teacher but failing to truly capture him each and every time."
    m "It’s actually quite sad...watching them bend and break so many times."
    s "Wait, what happened to their memories persisting through resets? What’s all this about bending and breaking?"

    scene mayalantern11
    with dissolve

    m "Perhaps you’ll find out in due time?"
    m "Unless, of course, you wind up poking your nose deeper into the past and get your slate wiped clean again."
    s "Are you saying that once I’m gone, they’ll be gone too?"
    m "Is that what you think?"
    s "I’ve given up on thinking when it comes to getting all deep and introspective like this."
    m "Boy, do I wish I could do that."
    m "Take a moment and think back to when you first arrived here."
    m "Everyone already had preconceived notions of the type of person you were, correct?"
    s "Yeah. But wasn’t that just because that’s how the original Sensei was?"
    m "Interesting theory."
    m "I can see why you’d think something like that."
    m "But you’re wrong."
    m "What you were witnessing in those moments were their memories being rewritten."
    m "Didn’t you think it was strange how quickly some of them warmed up to you despite undergoing a complete switch in personalities?"
    m "How everyone just {i}decided{/i} that not actually being taught anymore was a totally normal thing?"
    m "Are you familiar with computers? I want to make a comparison, but I’m not sure if you’ll understand."
    s "Feel free. I’m already lost, so any comparison at all could possibly help."
    m "Computers don’t have brains like humans do. They have hard drives."
    m "Over time, those hard drives fill up with information a user collects and saves."
    m "If a household only has one computer and every resident of the house uses it, that storage space will begin to fill up rather quickly."
    m "So, in order to make space for new information, old information needs to be deleted."
    m "Or reformatted entirely in more severe cases."
    m "What you were experiencing in watching those girls adapt to you was a type of reformatting."
    m "They were freeing up space in their minds to make room for the “new” you."
    m "And unless you do something to ruin them, which you likely will since you are horrible, that will be how they remain until a new user comes along."
    m "Do you understand?"
    s "I think so...but..."
    m "But what?"
    s "Why the fuck did you take so long to tell me this?"

    scene mayalantern12
    with dissolve

    m "Because I needed you to fail to a certain extent."
    m "And you failed wonderfully."
    m "Good job, Sensei."

    scene mayalantern13
    with dissolve

    if bonus == True:
        m "I really wish you didn’t go all the way with Ami, though."
        m "I hate watching her get hurt after everything that she’s been through."
    else:
        m "I really wish you didn't hug Ami so often, though."
        m "That sort of relationship with your accountant will only end in destruction and lower tax refunds when you inevitably sever ties."

    s "..."
    m "..."
    s "You..."

    scene mayalantern14
    with dissolve

    m "Did you really think you would be able to hide that from me?"
    m "Or, scratch that, did you really think {i}Ami{/i} would be able to hide that from me?"
    m "We’re both [teenage]girls at the end of the day."
    s "You are...surprisingly unfazed by this."
    m "Oh, I judge you harshly for it."
    m "I’m just used to it by now."
    m "Accepting your shortcomings and flaws is something I will never find joy in, but something I must do nonetheless."

    if bonus == True:
        m "Expecting you to make it through an entire loop without manipulating one of the girls into sex acts is like expecting me to not make it through without..."
    else:
        m "Expecting you to make it through an entire loop without a hug is like expecting me to not make it through without..."

    s "..."
    m "..."
    m "What is something weird or bad that I do?"
    s "You talk about the sky a lot."

    scene mayalantern7
    with dissolve

    m "Yes, that. It’s like expecting me to make it through a loop without bringing up the sky."
    m "The key difference is that my crutch doesn’t hurt anyone and yours hurts everyone."
    m "Just not right away."

    if bonus == True:
        s "It definitely hurts some of them right away."
    else:
        s "Hey, do they make that shrine maiden outfit in my size by any chance?"

    m "..."
    s "..."

    scene mayalantern3
    with dissolve

    m "Why do you always have to ruin everything?"

    if bonus == True:
        m "Just because I know about what you’re doing with everyone doesn’t mean I want to {i}hear{/i} about it."
        m "Have some respect."
        s "I will. Because even though you allegedly know what I allegedly do in all of my alleged spare time..."
        s "You still haven’t done anything to make me pay for it."

        scene mayalantern11
        with dissolve

        m "What would I do? I’m just a normal [teenage]girl."
        s "I don’t know. But I’m glad it’s nothing."
        s "Either way...I’ll see if I can talk to the others about how there’s definitely nothing going on between us."

        scene mayalantern10
        with dissolve

        m "Yeah. Thanks."
        m "..."
        m "That would be a big help."

    scene black
    with dissolve2

    "Maya and I remain situated at the booth for a little while longer."
    "The sun retreats behind the clouds, creating a darkness that swallows me whole."
    "Maya remains safe, illuminated by the glow of her giant lanterns as I am left to figure out where to go from here."
    "I learned a lot more than I normally do with Maya today."
    "In fact, for the first time ever, I might be leaving with more answers than questions."
    "I should probably cherish this moment."
    "But for some reason-"
    "I just keep worrying about her."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine30 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label shrine35:
    scene black
    with dissolve
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    scene nightsky
    with dissolve
    play music "undersea.mp3"

    "Night comes before I know it."
    "I feel like I decided to visit the shrine just a few minutes ago-"
    "But the sun was shining then. And this is certainly no sun I know."
    "I make my way down the streets of the city, staring up at the sky and hoping to catch a glimpse of a supernova."
    "The thing is, viewing a supernova from all the way down here wouldn’t be nearly as exciting as seeing it up close."
    "I know this for a fact."
    "Because I viewed a supernova just the other day."

    play sound "static.mp3"
    scene imissyou11 with flash
    scene nightsky with flash
    stop sound

    "What a beautiful explosion that was."
    "I wish I could remember more of it. "
    "I’m not allowed to remember, though."
    "Maya says that if I do, I might disappear. "
    "I don’t want to disappear yet."
    "I have so much left to do..."
    "If only there was someone around to guide me."

    s "..."
    s "..."
    s "..."

    "I say that as if I expect someone to just show up and do it."
    "That’s not how this works, though."
    "The closest I have to a guide at all right now is the one I need guiding {i}to{/i}."
    "For I’ve somehow found myself lost. Wandering around in the middle of the night with a destination in mind but not enough willpower to arrive there."
    "I begin to think of the things I will say if I do."

    if bonus == True:
        "“Hello. I retract my rejection of coitus. Come, Maya. Let us repopulate the world with more people who can travel through time.”"
    else:
        "“Hello. I do want a belly rub and a hug after all. Come, Maya. Let us do a variety of cute things with one another in complete disregard for the typical dynamic of our relationship.”"

    "How ridiculous."
    "Though I suppose the sheer idea of our existence in and of itself is ridiculous in a multitude of ways."
    "It is not poor luck, though. Which is how I’m sure she would describe it."
    "It is a blessing."
    "We can see everything."
    "Why should I be punished for not closing my eyes?"

    scene black
    with dissolve

    "I walk."
    "And I walk."
    "And I walk and I walk and I walk."
    "And I find something new."

    scene mayasnowshrine1
    with dissolve2

    m "Ah..."
    ay "..."
    a "Sensei? What are you doing here this late?"
    s "I could ask the same question to all of you."
    a "We came here to get Maya since we were all supposed to hang out tonight."
    ay "You’re not suddenly religious...are you, Sensei?"
    s "Me? No. I was just wandering around."
    s "I came up here because it’s usually warm. Apparently that’s not the case tonight, though."
    m "It..."
    m "It started snowing a couple hours ago."
    m "Just after the sunset."
    s "I see."
    s "Well if you three are planning on hanging out tonight, I can just head back."

    scene mayasnowshrine2
    with dissolve

    a "What? No! Come with us!"
    a "Where were you before this? It was probably a really long walk and...you don’t even have a real jacket."
    ay "We’re going out to a family restaurant. I can pay for you if you don’t have any money."
    s "I’m not broke, Ayane."
    ay "Yes, but I’m rich. So I really insist that you come with us."
    ay "Let me treat you and get you out of the cold."
    a "Yeah! Come on. Let’s get you somewhere warm."
    m "I...agree..."
    m "You should probably come with us."
    s "Why is everyone so concerned with warming me up all of a sudden? I feel fine."
    s "I’m just bored."

    scene mayasnowshrine3
    with dissolve

    m "You’re soaking wet."
    m "Which is...worrying since it’s not even snowing that hard."
    a "Yeah. Your hair is basically all white right now. You look like a cool grandpa."
    ay "If this is how you will look when you are old, I am even more excited for our future than I already was."

    "I pat down my pants and blazer to find that, yes, they are soaking wet. "
    "But when did this even happen? And why did I not realize anything until it was pointed out?"
    "The three girls stare at me, unsure of how to proceed with the conversation given that I likely look insane right about now."
    "And, you know, maybe I am?"
    "I’d certainly pass that judgement onto anyone I saw casually walking around in soaking wet clothes during a minor snowstorm."

    m "..."
    s "..."
    a "..."
    ay "Well, I don’t think just standing here is going to do anyone good. "

    scene mayasnowshrine4
    with dissolve

    ay "Should we maybe...call an ambulance or something?"
    a "What? No. He’ll be fine. Sensei never gets colds."
    a "He just gets like this sometimes. Once we get him home and into bed he’ll be as good as new."
    s "Okay, you two realize I can hear you, right?"
    s "I’m perfectly fine."
    s "Besides, I already offered to go home since you’re busy. "
    s "Making a big deal out of it is just going to make me feel weird."
    a "See, Ayane? No ambulance necessary. In fact-"

    scene mayasnowshrine5
    with dissolve

    a "Sensei, I’m going to walk home with you and make sure you’re okay. Ayane and Maya can go out to eat by themselves."
    ay "Actually...why don’t we just get something delivered to your house? "
    ay "I’m suddenly losing my appetite anyway."
    s "I-"

    scene mayasnowshrine6
    with dissolve

    m "Would it be okay if I spoke to him alone for a moment?"
    a "Huh? Really?"
    a "But you never want to talk to Sensei."
    m "And I’m not saying I want to talk to him now either. "
    a "Then why-"
    ay "Do you want to talk to Maya, Sensei?"
    s "I wouldn’t mind that."
    s "I think there’s something we need to clear up anyway."
    ay "What...do you need to clear up, exactly?"

    scene mayasnowshrine7
    with dissolve

    a "You and Maya? Did something happen that I didn't hear about yet?"
    m "A misunderstanding of sorts."
    m "It likely won’t take long...but you two can begin heading to Ami’s house or the restaurant or...wherever and then text me to let me know which one you decided on."
    m "I’ll make sure Sensei gets there, too."
    a "I mean...I don’t have any problem with-"
    ay "I don’t want to leave Sensei’s side right now."
    ay "This all feels very strange. "
    s "It’s fine, Ayane. Really. There’s nothing to worry about."
    ay "There’s nothing to worry about?"
    ay "You just...wandered over to where Maya hangs out in the middle of the night during a snowstorm to be alone with her and there’s nothing to worry about?"

    scene mayasnowshrine8
    with dissolve

    m "It’s not like that, Ayane..."
    a "Ayane, come on. It’s {i}Maya{/i}. "
    ay "..."
    m "..."

    "It’s not common that I see Ayane look at anyone this way."
    "And I’m sure she feels just as strange as I do on account of her resulting silence."

    if bonus == True:
        "Teenage girls are so fickle, getting upset over small things like this when there’s not even any substance to it."
    else:
        "College girls are so fickle, getting upset over small things like this when there’s not even any substance to it."

    "Maya and I {i}do{/i} need to clear up a misunderstanding."
    "That’s likely why I wound up here in the first place."
    "And it’s a misunderstanding that can’t be brought up around the other two, so-"

    ay "We’ll text you in a few minutes to let you know where we’re going."
    m "Can you {i}not{/i} look so angry while saying that, please? I didn’t even do anything."
    ay "This face just happens out of natural instinct when I think someone is trying to take Sensei away."
    a "If it makes you feel better, I don’t think you’re going to take Sensei away, Maya."
    a "You’re not girly enough anyway, so I doubt he would even like you like that."
    m "Oh. Thanks, Ami. That was...kind of you."
    s "Sorry for showing up and making things really awkward when you guys just wanted to get food."

    scene mayasnowshrine9
    with dissolve

    a "No need to apologize, Sensei! We’re all totally used to working our schedules around you by now anyway."
    ay "I’m sorry if I seemed angry. I’m not. "
    ay "I’ve just been feeling a little strange lately."
    s "It’s fine."
    s "I’ll meet up with you guys again in a little while."
    a "Don’t forget to text me every five minutes so I know you didn’t die of hydrothermopoly."
    s "Hypothermia. And sure."
    s "See you soon."

    scene black
    with dissolve2

    "Ami and Ayane slowly make their way down the steps of the shrine to avoid slipping and cracking their heads open on the concrete."
    "On the bright side, if one of them {i}did{/i} fall, it would be easy to rip off Maya’s skirt and use it to soak up all of the blood."
    "It’s also the same color, so any stain left would be barely noticeable."
    "I bow twice, clap twice, and bow again to prevent any of that from ever happening."
    "........."
    "......"
    "..."

    scene mayasnowshrine10
    with dissolve

    m "..."
    s "..."
    m "..."
    s "..."
    s "Okay, I’ll talk first."
    s "Aren’t you cold in that?"

    scene mayasnowshrine11
    with dissolve

    m "At least it’s not soaking wet. "
    m "There are plenty of warm spots inside of the shrine."
    m "You look like you’ve been wandering around for hours."
    s "I probably was. "
    m "You don’t remember?"
    s "All I remember is deciding to come here around the same time I always do."
    s "Then, before I knew it, I was being invited out to eat by a bunch of girls who paint their nails in my living room."
    m "And that doesn’t worry you?"
    s "Not really. I’m just a little upset that I missed an entire part of the day."
    s "That’s time I will never get back."

    scene mayasnowshrine12
    with dissolve

    m "Ha ha ha. Time loop humor. Hilarious."
    s "Well it’s not like you ever laugh at normal humor, so it was worth a shot."
    m "I laugh at plenty of things. You just have the worst sense of humor out of any person I’ve ever encountered."

    "It’s cute how she can still insult me while nervously twirling her ribbon around in her fingers."
    "But I’m sure she has a lot of practice."
    "By now, I’m sure the amount of insults I’ve received from this girl add up to around the same total as stars in the sky."
    "I’m sure she’d be happy to hear that comparison drawn, but I’m too cold and exhausted to make anyone happy tonight."
    "And..."
    "There’s still a “misunderstanding” that needs to be cleared up."

    s "So, about the other night-"

    scene mayasnowshrine13
    with dissolve

    m "I know. "
    m "And...I’m sorry."
    m "I was desperate and angry and said some things that should never have been said. "
    m "I’m honestly surprised you’re even here right now. "
    m "I was sure you were going to be avoiding me for at least another several weeks."
    m "But I suppose that if there is anyone in the world who can so harshly reject a girl only to return and talk about it shortly after, it’s you."
    s "Under normal pretenses, I wouldn’t have rejected you at all. "
    s "In fact, I don’t even see what happened as a rejection in the first place."
    m "Please, do tell what you saw it as."
    s "I’m not sure if the words ever made it out of my mouth back then, but I didn’t want you doing something like that out of sheer desperation."
    s "It’s not like that strategy would have worked either way."

    scene mayasnowshrine14
    with dissolve

    m "I know. "
    m "Which is why I’m glad you didn’t let me follow through with it."
    m "Also, if you ever deliriously compare me to a bird again, I will not hesitate to scratch your eyeballs out."
    s "I...did what?"

    if bonus == True:
        m "You said all sorts of strange things as I was frantically trying to get you aroused."
    else:
        m "You said all sorts of strange things as I was frantically trying to hug you."

    m "It was the most embarrassing several minutes of my life."
    s "..."
    m "..."
    s "I have no idea what I’m supposed to say to that."

    scene mayasnowshrine15
    with dissolve

    m "There’s no need to say anything, really."
    m "You’ve been having episodes like that since the first loop began."
    m "They just always manifest differently...and get progressively harder to pick up on as we move closer and closer to the middle or the end of a season."
    s "And is the “middle or the end of a season” getting close now?"

    scene mayasnowshrine14
    with dissolve

    m "I’d say we’re closer to the middle of the middle. "
    m "But, then again, everything I know about the world has been slowly fading away since winter began."
    m "For all I know, everyone could vanish tomorrow."
    s "And I’m sure that’s exactly what you’re hoping for, huh?"
    m "Yes. I’m trying to remain hopeful that it not only buys you more time, but gets rid of the single worst girl I have ever crossed paths with before she can damage you any more."
    s "She has not “damaged” me, Maya."

    scene mayasnowshrine16
    with dissolve

    m "Yes she has. "
    m "It’s near impossible for you to notice, but I’d like to inform you that, as of right now, I know you a hell of a lot better than you do."
    s "So does Noriko, but at least she’s nice about it."
    m "Being nice isn’t going to keep you alive. "
    m "She’s going to chase you off the same way she did the last time."
    s "Can you at least tell me what happened “the last time?”"
    m "No."
    m "In fact, the second I tried to tell you something even simpler than that, you passed out on my bed and started hyperventilating."
    s "Well...summarize it or something."
    s "I don’t remember much about that night, but I remember it was very important."
    m "And if you pass out on the ground and start hyperventilating {i}here?{/i} What am I supposed to do then?"
    m "Let you freeze to death?"


    if bonus == True:
        s "You could always try to force me to have sex with you again. That worked really well last time."
    else:
        s "You could always try to angrily hug me again. That worked really well last time."

    scene mayasnowshrine17
    with dissolve

    m "You-"
    m "You’re disgusting."
    m "Please don’t bring that up anymore. "
    s "I hope you know I’m going to bring that up literally all the time now."
    m "Does seeing me in anguish truly make you that happy?"
    s "Not really. But seeing you blush like that does."
    m "..."
    s "..."

    scene mayasnowshrine18
    with dissolve

    m "{i}*Ahem*{/i}"
    m "Since you’re so dead set on turning your life into some sort of puzzle that must be solved, I suppose I can try to summarize at least one very important detail for you."
    m "Without divulging too much, several things have transpired over the last several months that have forced me into an inevitable change of opinions about you."
    m "I’ve been noticing it for quite some time, but my stubbornness is one of my greatest flaws, and this meant that I was unable to accept it."
    m "I have told you in the past that you are “changing.”"
    m "I was wrong."
    m "I have told you in the past that everything is part of a cycle."
    m "I was wrong about that as well."
    m "You are not changing and, with how hectic things have become lately, there is clearly no cycle at all. And if there is, it’s a really fucking stupid one without any rules."

    scene mayasnowshrine19
    with dissolve

    m "The reason I don’t want you to learn any more about “your” past is precisely because it is {i}your{/i} past."
    m "Probably."
    s "Probably?"
    m "Saying “definitely” too soon and then losing you would be the emotional equivalent of dropping my body feet first into a meat grinder."
    s "So, does that mean that I'm-"
    m "Yes."
    m "Probably."
    s "But that still doesn’t explain-"
    m "I can’t explain anymore."
    m "Not safely at least."
    m "And I would really...{i}REALLY{/i} appreciate it if you’d stop looking for answers."
    m "Stay exactly where you are now- at the precipice of everything. The edge of the world..."
    m "Because the second you fall off-"
    m "I fall as well."
    s "..."
    m "..."

    play sound "texttone.wav"
    scene mayasnowshrine20
    with dissolve

    m "..."
    s "I should probably tell Ami and Ayane we’ll be coming to meet up with them soon."
    m "I should have done that earlier but my phone is still in one of the lockers."
    s "I’ll handle it. Just go get your stuff."
    m "Okay. "

    "I start typing a message out and-"

    m "Sensei."
    s "...Yeah?"
    m "If I could tell you more, I would."
    s "Really?"
    m "Really."
    s "Even though I’m the most disgusting person in the world?"

    scene mayasnowshrine21
    with dissolve2

    m "Right."
    m "Even though you’re the most disgusting person in the world."
    s "I get it."
    s "And thanks."
    s "Now, go get your stuff."
    m "Okay."
    m "I’ll be right back then..."

    scene black
    with dissolve2

    "I finish typing out the message I was about to send to Ami and Ayane before Maya interrupted me."
    "Even after hearing all of that, though, I think she might be overreacting."
    "It is troubling how today went down with...losing several hours and managing to aimlessly wander through a snowstorm without noticing."
    "But much worse things have happened much earlier on."
    "So chalking those lapses up to the fact that I now have someone {i}willing{/i} to tell me about the past..."
    "I don’t believe it."
    "It doesn’t add up."
    "And I don’t want to say Maya is hiding anything from me, but-"
    "Maya is clearly hiding things from me."

    m "Okay...sorry."
    m "I think that’s everything."
    m "Are we going back to your house?"
    s "Yeah. It looks like that’s the plan."
    m "Okay. But we should probably hurry up. "
    m "We’ve kept them waiting for quite some time and I am extremely cold right now."
    s "Want to hold hands and keep each other warm?"
    m "..."
    s "..."
    m "I would rather freeze to death."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine35 = True
    stop music fadeout 8.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayafestival1:
    play music "goodmorning.mp3"

    "I hear a door open from somewhere inside of a dream."
    "Well, the door isn’t inside of a dream."
    "I am."
    "Or was."
    "I don’t remember much of it, just that something was there."
    "I guess I’ve never been adept at recalling things I experience while unconscious, though."
    "The scent of watermelon shampoo drifts closer to my bed, but I already had a feeling it was Maya who entered by the way the door sounded when it opened..."
    "Quiet and urgent, backed by a heavy dose of arrogance and the slightest hint of a sadness so great it could destroy the world."
    "I can’t wait to ruin her day."

    scene mayabday1
    with dissolve2

    m "Good morning."
    s "Good morning."

    "I’ve seen this before."
    "A slender girl in summer clothes, kneeling at my bedside- staring at me as I slowly return to the world."
    "Not breaking eye contact despite how much she may want to. Not climbing into the bed despite how much I may want her to."
    "She probably would under the right circumstances, but my arms are far too weak to grasp at them and I’m far too tired to find them anyway."

    m "I believe you’re supposed to say something to me right now."
    s "I’ll take my eggs over medium. Thank you."
    m "Something more celebratory."
    s "Happy anniversary, Maya. Here’s to a million more years or however long you’ve been wandering around inside of the bubble."

    scene mayabday2
    with dissolve

    m "Close enough, I guess."
    s "A smile this early? Are you sure it isn’t {i}my{/i} birthday instead of yours?"
    m "So you {i}did{/i} remember and were just electing to not say anything. I’m not surprised at all."
    m "Fair warning, I might smile at several points throughout the day. You can stare in silence, but please don’t draw attention to any of them."
    m "It will make it harder to convince myself I’m not having any fun."
    s "Don’t worry. I’ll just keep track of them all mentally and provide you with a final tally at the end."

    "Smile Count: 1"

    m "It’s going to be hard keeping track of anything if you don’t summon what little willpower you have inside of that body and get out of bed."
    s "Ten more minutes. You can climb in too if you want."
    m "I seem to have forgotten my pajamas."
    s "Borrow Ami’s."

    "Wait. Ami."

    s "Does-"
    m "She’s at work and doesn’t know I’m here. Don’t worry."
    m "Additionally, I may have eaten the breakfast she prepared for you in lieu of the birthday present you didn’t get me. "
    s "That’s because {i}I{/i} am the present."

    scene mayabday3
    with dissolve

    m "I wonder if there are any pawn shops open today that will accept a trade-in?"
    s "Hey. You’re the one who asked for this. "

    scene mayabday4
    with dissolve

    m "That’s right."
    m "Don’t make me regret it."

    "Smile Count: 2"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mayabday5
    with dissolve

    m "..."
    s "..."
    s "What?"
    m "You know, out of all of the iterations of you that I have seen in the past, I can’t say that any of them have ever gone furniture shopping."
    s "I didn’t buy this. Someone made it for me."
    m "You tricked someone into liking you so much that they handcrafted you a wardrobe?"
    s "I feel like the lengths you have gone to for me are much greater than a few planks nailed together."

    scene mayabday6
    with dissolve

    m "Yes, well...don’t be expecting a new coffee table from me anytime soon. "
    s "So is this just how we’re going to spend the first half of your birthday? Walking around my room and commenting on all of my things?"
    m "It’s been a while since I’ve actually looked around in here. I want to see how much has changed."
    s "That’s right. You must have spent a lot of time in here during our long history of you not being in love with me."

    scene mayabday7
    with dissolve

    m "Will that wardrobe fit a human body? Because I’m seriously considering crawling inside of it and dying right now."
    s "It will fit Uta and she has significantly more...{i}width{/i} than you."
    m "I take it her {i}width{/i} has been in there quite a few times by now, then?"
    s "Yes, but I was only there for one of them."
    m "You never cease to disgust me."
    s "I think that’s on you this time because I really have not done anything unsavory involving this closet."
    m "What a world we live in where you feel obligated to confirm to me the household objects you have {i}not{/i} desecrated."

    scene mayabday8
    with dissolve

    m "Now, please excuse me while I begin rifling through more of them."

    scene black
    with dissolve2

    "Maya paces around the room, inspecting a bunch of things and probably trying to find a new hiding spot for whatever fake journal she plants in here next."

    if bonus == True:
        "She even goes as far as checking under the bed to see if I’ve been hiding any porn under there. Thankfully, I’m smart enough to-"
    else:
        "She even goes as far as checking under the bed to see if I’ve been hiding my Pokemon cards under there. Thankfully, I’m smart enough to-"

    m "I assume you’re still keeping your stash under the mattress then?"
    s "Damn it."

    "Maya removes a small stack of {i}research material{/i} from underneath my mattress and begins to flip through everything, entirely unfazed by the matter."

    if bonus == True:
        m "I’m surprised Ami hasn’t found them yet. I can’t imagine she’d be very happy about-"
        m "Wait. What’s that?"
        s "What’s what? Because I haven’t looked at {i}all{/i} of those magazines yet, and if there’s anything in there that’s weird-"
        m "Not the magazines. What are those notes hanging up near your door?"
    else:
        m "Wow. Is that a holographic Charizard?"
        s "Please be careful with that. It is very expensive."

    "Maya shoves my {i}research material{/i} back underneath my mattress and makes her way over to the door..."

    scene mayabday9
    with dissolve

    m "..."
    s "..."
    m "How long have these been here, exactly?"
    s "I’m not sure. I don’t ever really touch anything on that wall."
    m "Who wrote this note?"
    s "The one about the password or whatever? I’m not really sure."
    m "Because it sounds like something I would say. And it’s signed by an MM."
    m "But I don’t recall ever writing this. And I know your password. It’s Boobies123."
    s "That it is, Maya. That it is."
    s "Anyway, is it possible that you just forgot you put this there? "
    m "It is {i}highly{/i} unlikely. Remembering is kind of my thing."
    s "I thought watermelons were your thing?"
    m "I have multiple things. I’m an incredibly complex girl."
    s "Sure are. I can’t say anyone else I know has ever messed with my...wall thing like this."
    m "I..."
    m "Wouldn’t be so sure of that."

    scene black
    with dissolve2

    m "I’m going to leave another note here. Don’t touch it."
    s "I already told you that I don’t really mess with that wall."
    m "Then continue not messing with it."

    "Maya grabs a sheet of paper and a pen off of my desk, scribbling something down before sticking it to the board along with all of the other apparent non-Maya notes."
    "After that, she immediately proceeds to exit the room without saying anything, so I guess the two of us are done hanging out in here for now."

    scene mayabday10
    with dissolve2

    "It’s still a little early for any sort of festival to start, so I’m not really sure how Maya intends to kill the next several hours."
    "Or why she showed up even half as early as she did."
    "But hey, she wanted to spend the day with me. So if she wants the {i}entire{/i} day, so be it."
    "I’m just glad Ami’s not here to see this because I can not imagine her taking it very well."
    "I’m also surprised that no one else asked me to this festival, but I guess my time would be better spent trying to figure out how to survive it with the person I {i}am{/i} paired with."

    s "So...do you actually like festivals, Maya?"

    scene mayabday11
    with dissolve

    m "Me? Of course. Why wouldn’t I?"
    s "I don’t know. Something just feels off about the idea of you liking {i}anything.{/i} All of your interests take me by surprise even when I know they exist."
    m "I think you’re just projecting. I’m a normal [teenage]girl who likes most things that other normal [teenage]girls do."
    m "Also, do you have any idea how much food is going to be at this place? Because it’s a lot."
    m "And despite how “surprising” my interests may be to you, I believe everyone has accepted my love for food."
    s "All I ask is that you don’t count on me winning you any prizes."
    m "Oh, that’s fine. I already know you don’t possess the ability to win at any sort of festival game. My expectations could be no lower."
    s "Well, now I just feel compelled to prove you wrong."

    scene mayabday12
    with dissolve

    m "Hah...you don’t have to do anything like that."
    m "I just want a normal day. I don’t get many of those."
    m "I want to eat. Walk around. Talk about things you’re not interested in and have you pretend that you are."
    m "But, most importantly-"

    scene mayabday13
    with dissolve

    m "I want to be the cutest girl at the entire festival."
    s "..."
    m "..."
    m "What?"
    s "Is that real? Is that what you actually want?"
    m "It’s less what I {i}want{/i} and more...me looking forward to experiencing it."
    m "There’s something rather liberating about being the envy of everyone when you can’t get in trouble for it."
    s "Well, I can definitely relate to that."
    m "No. That’s-"

    scene mayabday14
    with dissolve

    m "Wait. Ew. No. You {i}can{/i} relate to that. "
    m "Ugh. I think I’m going to be sick. Why did you let me say that?"
    s "Probably because, and this may upset you, so brace yourself- I can’t predict the future."

    scene mayabday15
    with dissolve

    m "Hah...the future. Right. I guess we should just talk about that now, then. So we don’t have to spoil the festival itself."
    s "Oh man. Is this one of your famous pre-reset lectures?"

    scene mayabday16
    with dissolve

    m "I’m going to ask you something right now, and I am going to be very direct about it."
    m "All you have to do is answer yes or no."
    s "I will do my best."
    m "Then-"

    if bonus == True:
        m "Is there {i}any{/i} way {i}at all{/i} that Ayane is pregnant?"
        m "Or any of the girls you’ve been sleeping with."
    else:
        m "Is there {i}any{/i} way {i}at all{/i} that Ayane is hugnant?"
        s "Hugnant?"
        m "It is when you are pregnant with happiness. It happens after unprotected hugging."

    s "Uhh..."
    m "Yes or no."
    s "It’s complicated."

    if bonus == True:
        m "It’s really not. You {i}do{/i} know how babies are made, correct?"
        s "No. Do you think you could show me?"

    m "I’m being serious right now."
    s "I get that. This is just a pretty random thing to be serious about."

    scene mayabday17
    with dissolve

    m "No. A “random” thing to be serious about would be polar bears or pogo sticks. This is a topic with direct relevance that, and I’m not kidding here, could screw {i}everything{/i} up."
    s "I don’t-"
    m "Let me ask you a question. Why do {i}you{/i} think Ayane made it to the roof last time? A feat that no one else has ever accomplished before. Why her?"
    s "That’s-"

    scene mayabday18
    with dissolve

    m "Too slow- I’ll tell you."

    if bonus == True:
        m "Because you two had sex and she got pregnant. Which means she was carrying {i}your{/i} DNA inside of her. Which means she was a temporary extension of {i}you.{/i}"
    else:
        m "Because you two hugged and she got hugnant. Which means she was carrying {i}your{/i} joy inside of her. Which means she was a temporary extension of {i}you.{/i}"

    m "Do you see where I’m going with this?"

    if bonus == True:
        s "You’re saying that Ayane was only on the roof because she was pregnant with my child...which, no offense, sounds a little ridiculous."
        m "What {i}isn’t{/i} ridiculous about this life we’re living?"
        s "That doesn’t-"
        s "If she were pregnant, what happened? Because she doesn’t look very pregnant anymore."
    else:
        s "But where did the hug goooooooooooooooo????"

    scene mayabday19
    with dissolve

    m "Gone with the reset, I suppose."
    s "What?"
    m "It wasn’t meant to be there, so it was disposed of. "
    m "I told you a long time ago. More than just memories can be altered by the shift in time. Physical attributes can be set back as well."
    m "I believe Ayane was rewritten to be the same exact person, just...without a parasite growing inside of her."
    m "So when I ask you if there is any possibility of it happening again, I need you to answer honestly."
    m "We may have gotten her back last time, but there’s no telling if it would work out that way again."

    if bonus == True:
        m "So before you go thinking about how awesome it would be to mate with your entire classroom and never have to worry about having children, consider the price you’d have to pay."
    else:
        m "So before you go thinking about how awesome it would be to hugh your entire classroom and never have to worry about getting anyone hugnant consider the price you’d have to pay."

    m "Potentially, of course."
    m "This, like everything else, is all conjecture."
    m "But when everything is new, conjecture is all we have."
    m "I don’t want anything to go wrong. "
    m "So I need you to start caring about everyone else a little more than you currently do."

    if bonus == True:
        s "You don’t need to beg me to keep me from fathering any children, Maya. I can assure you that is the last thing I want to do."
    else:
        s "Ughhhhhhhhhh can we go already?"

    m "You still haven’t answered the question. Is it-"
    s "Yes."
    s "It’s possible."

    scene mayabday20
    with dissolve

    m "I see."
    s "But I have no idea whether it’s true or not. So you’ll have to confront Ayane yourself if you want to know."
    s "Unless you’d rather just wait until we’re on the roof to find out, because there’s not much we can do at this point."
    m "..."
    s "..."
    m "..."
    s "Are you really sure that’s what it is, though? "
    m "Are you asking because you’re acknowledging the possibility that you may have planted your seed inside of others as well?"
    m "And, if that’s the case- are you confused by how only {i}Ayane{/i} has made it there?"
    m "Because these are things I’ve questioned myself as well. And I don’t know."
    m "I just don’t know."

    scene mayabday21
    with dissolve

    m "But I can’t think of any other reason why it would happen."
    m "And I've tried."
    m "The further we move into uncharted territory, the higher the potential is for risk."
    m "And I’m..."
    s "..."
    m "..."
    m "I’m finally starting to feel something again."
    m "I don’t want that to go away."

    "{i}A moment of silence.{/i}"

    s "Are you scared?"

    "{i}A crack in the glass.{/i}"

    m "Yes."

    "{i}A light in the attic.{/i}"

    scene mayabday22
    with dissolve

    m "Because I think that it might."

    scene black
    with dissolve2

    "{i}A dream of the past.{/i}"

    "The conversation drops dead after Maya’s revelation, but I must be forgiven for getting lost on this particular train of thought when the route-map is tangled up like wires."
    "I don’t want to believe her but, at this point, I feel like I have to- because {i}I{/i} can’t think of any other reason Ayane would have made it up there with us either."
    "The gap we accidentally create in our morning is subsequently filled by a collage of uncomfortable glances and scattered trips to the refrigerator."
    "Nothing is ever inside."
    "At least nothing that either of us want."
    "It ends, though- but I imagine that’s just because Maya wants to forget about this and focus on the rest of the day. "
    "She wants to eat. "
    "She wants to walk around. "
    "She wants to talk about things I’m not interested in and have me pretend that I am."
    "And strangely enough, I want to do all of those right now as well."
    "But we still have a few more hours of sunlight."
    "And many more unsuccessful trips to the refrigerator."

    $ renpy.end_replay()
    $ mayafestival1 = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Two hours pass.{/i}"
    "{i}Maya changes into her yukata in the comfort of her best friend’s bedroom.{/i}"
    "{i}She looks beautiful.{/i}"

    scene mayabday23
    with dissolve2

    "Smile Count: 3"

    s "Welp...it will definitely be hard for anyone to take you down in your pursuit of being the cutest girl at the festival."
    m "For today and today only, I’ll allow you to say that as many times as you want without fear of being insulted."
    s "It might be good to turn the cockiness down a little, though. Even if it is well warranted."
    m "It’s my birthday. I can be as cocky as I want."
    m "Now, let’s get out of here before Ami comes home. I’m hungry and don’t want to deal with her today."

    scene black
    with dissolve2

    s "Well, thank you for making the time for me..."

    "........."
    "......"
    "..."

    jump mayafestival2

label mayafestival2:
    "Maya and I leave the house together and begin to make our way to a festival at-"

    s "Wait, where is this festival exactly?"
    m "Far away. "
    m "Well, as far as we can go within the confines of Kumon-mi, that is."
    m "There’s one closer, but I didn’t want to risk the chance of someone seeing me with you in public and thinking we like each other."
    s "We do like each other, though."
    m "No. You like me. It’s different."
    m "Don’t worry too much about where it is as there’s not much reason to ever go back."
    m "The surrounding areas have mostly closed down anyway since the school building there is no longer in use."
    s "Are we taking the bus, then?"
    m "Partly. We’ll have to walk for about half an hour after we get off since the bus doesn’t stop where we’re actually headed anymore."
    s "The more I hear about this place, the more I think this is some elaborate ploy for you to kill me."
    m "There are much easier ways for me to kill you. "
    m "But in the event that I am just looking for a challenge, you should at least thank me first for allowing you to see me in my yukata in your final moments."
    s "Oh well. I’ve had a good run."

    "Anyway, we leave the house together and begin to make our way to a festival at some undisclosed location far away from my house that buses pretend doesn’t exist for some reason."
    "It’s confusing, yes. But so is literally everything about this city and I am tired of trying to attribute meaning to any of it."
    "And, like Maya says, there’s no reason for me to ever go back. So I might as well just stop thinking about it and try to enjoy the rest of the day with her."
    "If we ever make it there, that is."
    "At this rate, I-"

    stop music
    play sound "static.mp3"
    scene smileex with flash
    scene tree3 with flash
    scene mayafestival1 with flash
    stop sound
    play music "anewyou.mp3"

    s "Oh. We’re here."

    "A swarm of lights surrounds us, both natural and artificial, and the scents of various street foods assault my senses."
    "I still haven’t eaten anything on account of Maya claiming my breakfast as her own, so I’m starting to get a little hungry and hope that my companion here doesn’t empty my bank account out on herself."
    "Upon closer observation, I can tell this is somewhere I haven’t been before."
    "But, like many things, it feels familiar."
    "Even Maya’s presence feels familiar, so...maybe this is somewhere we’ve gone together in the past?"

    s "Hey. If buses don’t come here and there’s no reason to ever visit this part of town, how do you know about it?"
    m "I know every nook and cranny of Kumon-mi. I just choose to avoid most of them."
    s "Have we ever come here together before?"
    m "I’m not going to answer that. If you trick me into allowing you to commit suicide-by-memory on my birthday, I will never forgive you."
    s "This place just feels a little familiar. That’s all."
    m "Perhaps it is, then."

    scene mayafestival2
    with dissolve

    m "Anyway, I’ll be taking your credit card now."
    s "..."
    m "Fine. I will be taking your credit card, {i}please.{/i}"
    s "..."
    m "Give me your fucking credit card. I’m hungry."
    s "Do they even take credit cards here? This place seems pretty traditional."
    m "ATMs exist, you know. Just give me the card."
    s "This doesn’t sound very much like “spending time together.”"
    m "Do you see how many stalls there are here? We’ll never be able to hit all of them if we stick together."
    m "This festival has two halves. I need you to handle all of the stalls on the west side while I handle all of the ones on the east."
    m "Card. Now. Give."
    s "At least tell me what you want me to order for you first."
    m "Yes."
    s "Not really a yes or no question, Maya."
    m "You see, that is where you are wrong."
    s "You never wanted me here at all, did you? I’m just the only person you know with a credit card."

    scene mayafestival3
    with dissolve

    m "If I say no and promise to...catch goldfish with you or something once I’m done eating, will you give it to me?"
    s "I don’t have the time to take care of a goldfish."
    m "It’s a goldfish. You put it in water. That’s literally it."
    s "I feel like you’re supposed to feed it occasionally too."

    scene mayafestival4
    with dissolve

    m "Why do you care more about feeding your hypothetical goldfish than me? I am much more attractive and fun to be around."
    s "Attractive, sure. But I think you might be overestimating how fun you are."
    m "I think {i}you{/i} might be overestimating how fun a goldfish is. Card, please."
    s "..."
    m "This is not a joke. We have already wasted far too much time."
    s "Fine. But at least tell me where the two of us are supposed to meet back up. I don’t want to risk losing you in this crowd."

    scene mayafestival5
    with dissolve

    m "There’s a gazebo near the entrance with some picnic tables. Just meet me there."
    m "Also, what crowd? There’s barely anyone here yet."
    m "And “getting separated at the festival” is far too tropey for real life when we both know that any drama to spring up today will be from you saying or doing something disgusting."

    if bonus == True:
        s "Sure hope I don’t accidentally get anyone pregnant while buying your lunch."
    else:
        s "Sure hope I don’t accidentally get anyone hugnant while buying your lunch."

    scene mayafestival6
    with dissolve

    m "Have I ever told you how much I hate you?"
    s "Plenty of times."
    m "Just making sure."

    scene black
    with dissolve2

    "I give Maya one of my credit cards and thank whoever I was in the past for being responsible enough to carry two of them."

    if bonus == True:
        "Her ponytail bounces up and down as she runs off and, honestly, it’s probably the most active I’ve ever seen her apart from a few fantasies I don’t want to tell you about."

    "I stop in my tracks for a moment and observe my surroundings one more time before going in the opposite direction of Maya when I realize something."
    "I don’t think we’re in the old district right now."
    "But..."
    "I don’t think we’re in the new one either?"
    "..."
    "Where is this place?"

    if amifingered == True and bonus == True:
        q "You there!"
        q "You look like the kinda guy who could use a nice pair of melons!"

        scene mayafestival7
        with dissolve2

        q "We’ve got normal melons! We’ve got {i}square{/i} melons! We’ve got {i}triangle{/i} melons! Any kinda melon you can dream of!"
        q "So long as it’s one of those three shapes. Anything else, you’re gonna have to join the waitlist for."

        if sarasex == True:
            s "Wait...I’ve seen you before."

            scene mayafestival8
            with dissolve

            q "Oh?"
            s "Yeah. Didn’t we bump into each other in the middle of the night once or something?"
            q "Hmm...yeah! You were the guy with the phone!"
            s "That isn’t exactly how I would describe myself, but yes. I was the guy with the phone."
            q "Glad to see you made it back in one piece."
            s "And I’m glad to see you’re a...melon salesperson."
            q "Oh, this? This is just a temporary thing."
            q "I don’t even really like fruit."
            s "Well, you have chosen a very peculiar line of work then."

        else:
            s "What other shapes would they even come in?"
            q "Beats me. But if you join the waitlist, you can probably find out."

        q "So, is it melon time? Or is it {i}not{/i} melon time? I’ve got a very limited supply, you know."
        s "It is most certainly “melon time,” but I think I should ask you to confirm the quality of said melons since the girl I’m here with today is a bit of a connoisseur."
        q "Wanna give ‘em a squeeze and find out?"
        s "That depends on whether or not the police will get involved."

        scene mayafestival9
        with dissolve

        q "Ahh, we’ve got a pervert on our hands! That’s great! I’ve worked with you types before."
        s "There are a lot of us in the melon trade."
        q "You know what? For today and today only, I’ll throw in a second melon half-off. One for the two of you to share."
        q "If she even wants to share, that is. As a melon connoisseur myself, I understand how tough it can be to share what you love with other people!"
        s "How much are they?"

        scene mayafestival10
        with dissolve

        q "They’re...uhh..."
        s "You don’t know the price of your own products?"

        scene mayafestival11
        with dissolve

        q "Six million!"
        s "Yen?"
        q "Pesos!"
        s "I don’t think I have any of those on me."
        s "How does 500 yen sound?"

        scene mayafestival12
        with dissolve

        q "500? That’s it? These melons are easily worth double that. I think. Probably."
        q "This is my first day on the job, so I’m not really sure. But that also means you have to be nice to me since I’m nervous and my feelings are easily hurt."
        s "Then...1,000 yen for two melons. Post discount."

        scene mayafestival13
        with dissolve

        q "Deal! Would you like these gift wrapped? I’ll do it myself for...oh, I don’t know...an extra six million pesos?"
        s "You seem dead set on that specific number and...currency. Mind if I ask why?"
        q "A magician never reveals her secrets!"
        s "You’re a magician now?"
        q "And an astronaut!"
        q "But right now, melons matter most!"
        s "I’m going to say no to the gift wrapping, but I wouldn’t mind getting your name."

        scene mayafestival14
        with dissolve

        q "My name? Why?"
        q "Are you flirting with me? Does the sale hinge on this?"
        s "No. It’s just to satisfy my own curiosity."

        scene mayafestival15
        with dissolve

        q "My name, huh..."
        s "Is there a problem with that?"
        q "It’s just that nobody’s ever asked me before."
        s "I find it hard to believe that no one’s ever asked you for your name."
        q "Hey, you can believe whatever you want to believe. You don’t have to pick up all the stuff I put down, Mr. Pervert."
        s "Please don’t call me that."
        q "Nope. That’s your name now. You have to live with it."
        s "..."
        q "..."
        s "{i}This is the part where you tell me yours.{/i}"

        scene mayafestival8
        with dissolve

        q "Nope! This is the part where I don’t tell you and you still buy my melons anyway!"
        s "Can I at least have the first letter?"
        q "Nope! All I’ll tell you is that it’s really funny."
        s "Your name is?"
        q "Hilarious. A real kick to the shin."
        s "Then I apologize for how much you likely get made fun of in school."

        scene mayafestival16
        with dissolve

        q "Who says I go to school?"
        s "You don’t? I just thought you looked a little young."
        q "Oooooh, is {i}that{/i} why you’re flirting with me? Cause I remind you of your students?"
        s "That’s not-"

        scene mayafestival17
        with dissolve

        s "Wait, how did you know I’m a teacher? I don’t remember telling you that."
        q "Uhhhhhhh...hahahah!"
        q "Two melons coming right up!"
        s "I don’t-"

        play sound "static.mp3"
        scene smileex with flash
        scene tree3 with flash
        scene mayafestival18 with flash
        stop sound

    else:
        "Oh well. {i}Where{/i} we are doesn’t change {i}what{/i} I’m doing. And if I don’t come back to Maya with roughly one truckload worth of assorted street foods, she’ll probably wipe my mind."
        "It doesn’t matter how much she secretly loves me- I will always be second to food."
        "And I respect that."
        "We all have our interests."
        "Hers are just less mentally destructive and more physically destructive than mine."
        "One by one, I stop at an assortment of food stalls and point to random items behind the counter that look inexpensive."
        "If Maya is going to answer with “yes” instead of a specific list of what items she wants, I am going to do everything within my power to save money."
        "Especially since I may actually be bankrupt by the time the two of us meet up again."
        "........."
        "......"
        "..."

    m "Oh, good. You’re back."

    "Smile Count: 4"

    s "Welp, there goes Ami’s college fund."

    if bonus == True:
        m "Oh, please. Ami’s never going to college. No one is."
    else:
        m "Ami is already in college."
        s "Oh. Right."

    s "How can you even eat all of this?"
    m "I’m a growing girl."
    m "Or at least I would be if it weren’t for the whole time loop thing."
    m "I guess I’m just doomed to be eternally hungry."
    m "So, what did you bring me?"

    if amifingered == True:
        s "Something I think you’re going to be very happy about."

        "Thankfully, one of the vendors saw me struggling to carry an entire buffet’s worth of food and let me borrow a shopping cart they were using to store extra ingredients."
        "And I’m glad they did- because there is no way I would have been able to carry two large melons in addition to the variety of hot dishes I got."

        scene mayafestival19
        with dissolve

        s "Happy birthday, Maya."
        m "Ah! Melon!"
        s "Two melons."
        m "Two melons!"

        scene mayafestival20
        with dissolve

        m "Where in the world did you even find those? I asked every single vendor I bought from if anyone here was selling any and they all said no."
        s "Some weird girl was selling them. She had other shapes, too. And a...melon waitlist or something?"

        scene mayafestival21
        with dissolve

        m "Was there really a booth like that here?..."
        m "I had no idea."
        m "We’ll have to stop again before we leave."

        scene mayafestival18
        with dissolve

        m "Anyway, what else? I already know I’m saving the melons for last."

    else:
        "Thankfully, one of the vendors saw me struggling to carry an entire buffet’s worth of food and let me borrow a shopping cart they were using to store extra ingredients."
        "And I’m glad they did- because there is no way I would have been able to carry all of this without some form of transportation."

    s "There’s...croquettes...taiyaki...some weird potato-on-a-stick thing...whatever {i}this{/i} is...some other things I don’t know the name of...and a live squid."

    scene mayafestival21
    with dissolve

    m "What am I supposed to do with a live squid?"
    s "I don’t know. I just blindly pointed at stuff from every booth and I guess I pointed at a live squid at some point."
    m "Can you go, like...kill it or something?"
    s "Asking me for my credit card is one thing. But asking me to {i}kill?{/i} You’re better than this, Maya."
    m "Am I? Because I’m pretty sure I’ve asked you to kill Noriko on several occasions and, if anything, I think I’d prefer to keep the squid alive if I had to choose between the two of them."
    s "I can’t wait until the day you two make up and start being friends. It’s going to be so sweet."

    scene mayafestival22
    with dissolve

    m "Ew, stop. At least wait until I finish eating to start saying stuff like that."
    s "Maya, there is so much food here that it is going to take you the rest of the festival to eat it all even {i}if{/i} you manage to eat at your normal breakneck pace."

    scene mayafestival23
    with dissolve

    m "Do not underestimate my love for food."
    m "Festivals are to me what the dorm rooms of [teenage]girls are to you- a place where I can be free. Where my hunger can never be sated."
    s "I don’t know. My hunger is normally sated after half an hour or so. Sometimes, even less."

    scene mayafestival24
    with dissolve

    m "Why do you say things like this to me?"
    s "Because I know you won’t think any less of me."
    m "I literally can {i}not{/i} think any less of you."
    s "Yeah, exactly."
    m "..."
    s "..."
    m "Itadakimasu."

    scene black
    with dissolve2

    "One by one, Maya tears into each plate and-"
    "Well, I guess {i}tear{/i} probably isn’t the right word since she somehow manages to look graceful even while consuming more than some villages do in an entire week."
    "But she eats everything without lessening her pace even once."
    "The sun begins to set as she does so, and the air begins to turn a bit colder- but that’s to be expected since it is {i}technically{/i} still winter."
    "Sure, the two of us were gifted a relatively warm day by Mother Nature, but only until it was time for her to go out and party with her other cougar friends."
    "As Maya eats, well, {i}everything-{/i} I slowly pick at a bowl of ramen that, at least to my unrefined palate, doesn’t compare much to what Tsuneyo makes."
    "But it’s warm enough to battle the encroaching cold and gives me something to do while waiting for the first stage of Maya’s favorite day of the year to end."
    "........."
    "......"
    "..."

    if amifingered == True:
        scene mayafestival25
        with dissolve2

        m "MMMMMM!!!!!~~~~"

        "Just as she said she would, Maya saves the watermelon for dessert."
        "And yes, she did finish {i}everything-{/i} including the remainder of my ramen which, despite my worsening hunger, I was not able to finish."
        "I recall her saying in the past that she doesn’t like being watched while she eats and, this isn’t me being weird or...fetishy, but I’m glad she seemingly abandoned that insecurity today."
        "There’s something oddly satisfying about seeing a girl so far detached from joy being enveloped by it that I can’t help but feel a little warmer inside."
        "Maybe that’s why I couldn’t finish my food."
        "I was already warm enough."

        s "Enjoying yourself?"

        scene mayafestival26
        with dissolve

        m "A bit."

        "Smile Count: 5"

        m "And you?"
        s "For now. I’m sure that will change once I look at my credit card statement."
        m "At least Ami will still have a home when your house is repossessed."
        s "So, what’s the next phase of your game plan now that you’ve eaten from roughly every stand at this festival?"
        m "Hmm..."
        m "Have you changed your stance on goldfish at all in the last hour or so?"
        s "I can’t say I have."
        m "Then I suppose it would be best to avoid Kingyo-Sukui. Or any other games for that matter since you’re horrible at them and I don’t want any of the prizes."
        s "Pretty sure that just leaves more food, then."
        m "Don’t forget what day it is. We still need to visit a shrine and pay our respects for the year or god might kill us. That seems like a thing he would do."
        s "God sounds like an asshole."
        m "You’re just realizing that now?"
        s "Nope. Just reinforcing the belief with some help from you."
        s "I guess we can get our fortunes while we’re there too. That seems like another...{i}festivaly{/i} thing to do."
        m "Not necessary."
        m "I draw the same one every time."

        scene black
        with dissolve2
        stop music fadeout 10.0

    "We collect our garbage, dropping everything off at a nearby receptacle."
    "The squid (Still alive, albeit just barely) is left there as well- clinging to life atop a stack of dirty plates."
    "It covers its body in a variety of sauces, seasoning itself before death, in a desperate attempt to seek out water and prolong its unappreciated existence."
    "Neither of us have the heart to kill it, but we have the heart to watch it die."
    "And that must count for something."

    $ renpy.end_replay()
    $ maya_love += 1
    $ mayafestival2 = True

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump mayafestival3

label mayafestival3:
    scene clearnightsky
    with dissolve2
    play music "shrinemaiden.mp3"

    "Let me use this opportunity as the sun disappears to let you in on a little secret."
    "Sometimes, I can’t tell if I’m awake or not."
    "I can’t tell if what is happening is {i}actually{/i} happening or if it’s just more light filtering in through the glass."
    "I can’t tell what I should or shouldn’t believe."
    "Feel or think or say."
    "But I can tell you that I’m glad those moments come."
    "For, if they did not, I’d be the same as you- a disembodied soul floating carelessly through the ether."
    "Living life through the eyes of another because yours have already been taken away."
    "When you were still able to see, what would you wake up to?"
    "And if you could lower yourself into the ground, fully aware and fully conscious, what do you think you’d find?"
    "Darkness?"
    "Probably."
    "But what if it was something a little different?"
    "What if past the dirt and rubble and roots and all of those other things you’d normally find underground, there was something better?"
    "Something wonderful?"
    "Something {i}so{/i} wonderful that, the moment you feast your eyes upon it, you understand that it’s far too good to be true."
    "Maybe the reason I can’t ever tell if I’m awake or not has something to do with that."
    "Do you think we’ll ever see it?"
    "The thing beneath us."
    "The thing above."
    "Two sides of the same coin, cut in half and separated by more distance than one could travel in a lifetime."
    "That’s what we are."
    "It will take too long to become whole again, so we find comfort in quitting because at least that will give us the time to try something else."
    "We’ll always just be half of something, though."
    "How did we ever get this far apart?"
    "How did we separate in the first place?"
    "..."
    "Can I tell you another secret?"
    "..."
    "I’m scared."
    "But no one can ever know that."
    "No one in the middle, at least."
    "I’ll reconsider my position once it’s somewhere else."

    scene mayanightwalk1
    with dissolve2

    m "You know, this weird potato stick thing is actually really good. Perhaps you should just...randomly point at objects to make decisions more often?"
    m "Assuming that’s not how you’re already selecting new members for your harem, of course. "
    s "My decision making process is a little more complicated than that."
    m "I bet. You only have two hands. It sounds difficult pointing at everyone all at once."
    s "So, do you know where we’re headed?"

    scene mayanightwalk2
    with dissolve

    m "More or less. I admit it’s been quite a while since I’ve come here. "
    m "The novelty wears off once you’re forced to go alone over and over."
    s "I’m sure the other versions of me would have come as well if you had asked."
    m "I didn’t want them to."
    s "W-"
    m "Because they weren’t you."
    m "I’m surprised you even need to ask at this point, what with all of your alluding to my alleged {i}true feelings{/i} and whatnot."
    s "Can I take that as a confession?"
    m "No. But you may ask me again on my next birthday and see if the answer has changed."
    s "So another...what, two resets from now? Four?"
    s "There’s no way I’ll remember something that far off."
    m "Could be three. Maybe even one."
    m "We managed to sneak two Christmases into one winter, did we not?"
    s "You know we can spend more time together on days that aren’t your birthday, right?"

    scene mayanightwalk3
    with dissolve

    m "And then what?"
    s "What do you mean?"
    m "If I were to start spending more time with you, something I’ve made you extremely aware that I {i}don’t{/i} want to do in the past...what would happen next?"
    s "Well...we’d get closer."
    m "{i}Uh-huh.{/i} And then what?"
    s "Well, considering you already seem to know how quickly I move in relationships-"

    scene mayanightwalk4
    with dissolve

    m "No. That is absolutely not what I’m talking about."
    m "Do I really need to remind you why we can’t get closer anymore than I already have? Because it’s getting extremely repetitive and I’m {i}kind of{/i} good at dealing with repetition."
    s "It’s not fair that you have to live like this."

    scene mayanightwalk5
    with dissolve

    m "Hearing that from you just makes it worse."
    m "I suppose it is a little nice finally having company again, though."
    m "Now, if only we could predict the future..."
    s "Can I ask you something?"

    scene mayanightwalk6
    with dissolve

    m "I...suppose? You don’t normally ask for permission."
    s "What’s even the point of a “future” for you when you can’t seem to ever get what you want?"
    m "..."
    s "I guess what I’m asking is...if I really am the “real” me, but you can’t get any closer to me without the risk of destroying that..."
    s "What’s the point?"
    m "Well...why would an animal chase a carrot on a stick tied to its back?"
    m "Because it’s stupid and thinks that it might catch it one day."
    m "In my case, though, I’m even dumber than an animal. "
    m "There’s been a stick tied to my back for longer than I can remember and I’m {i}still{/i} chasing after it."
    m "I’m just moving a little slower than I used to while doing that."
    m "Am I ever going to catch it? Probably not. "
    m "But it feels like I’m getting a lot closer sometimes."

    scene mayanightwalk7
    with dissolve

    m "And it’s not like there’s anything else to do in this city."
    m "Anyway, please stop worrying about {i}why{/i} I do the things I do and instead try to accept them."
    m "There’s nothing you can actively do to help with my weird...cosmic curse thing or whatever it is that caused {i}me{/i} to persist but no one else."
    m "You can passively help, though. By just being around and not doing anything stupid."
    m "And occasionally buying me exorbitant amounts of food and allowing me to walk with you in my yukata."
    m "Just that every once in a while is enough for me to keep making it to the roof."
    s "I’m sorry."

    scene mayanightwalk8
    with dissolve

    m "Ew, no. Don’t apologize like that. It’s gross and weird. "
    m "Besides, it’s my fault for getting so attached to something I never should have."
    m "I can only imagine how fun and carefree my life in loops would be if I were even a mere fragment of the person you are."

    if bonus == True:
        m "But, no. I have to spend the rest of eternity convincing my best friend’s uncle to not breed with my friends while he sits back and has breakfast served to him in bed every morning."
        s "I normally go out into the kitchen."
    else:
        s "That's mean. Molding the minds of college students is a very hard job."

    scene mayanightwalk4
    with dissolve

    m "Oh, my apologies. Your life is clearly just as hard as mine then. How could I have been so blind?"
    s "Do you really think there’s a chance you might...“go away?”"

    scene mayanightwalk9
    with dissolve

    m "..."
    s "That’s been stuck in my head since you said it earlier."
    s "And, at the risk of sounding concerned, I’d really prefer that doesn’t happen."
    m "There is nothing wrong with a little concern every now and then."
    m "I have no idea what will or won’t happen. "
    m "I just know that things don’t tend to go well for me very often."
    m "It’s turned me into a bit of a pessimist over the years."
    s "Well, at the bare minimum, I hope I persist in the event that you wind up being reset."

    scene mayanightwalk10
    with dissolve

    m "As do I. "
    m "At least then you’ll know a sliver of what I’ve felt all this time."
    m "Only a sliver, though."
    m "I wouldn’t wish any more than that upon anyone."

    scene black
    with dissolve2

    "Maya and I continue down a gravel path, gradually moving further and further away from the festival. "
    "In fact, I imagine we’ve been moving away from it for quite some time now after getting caught up in conversation."
    "I don’t particularly mind, but I feel a little bad for Maya since I know she wanted to spend more time at the festival itself."
    "The moment I’m about to ask her if she wants to turn around, however-"
    "She stops dead in her tracks."
    "........."
    "......"
    "..."

    scene mayanightwalk11
    with dissolve2

    s "Is this the shrine you were talking about?"
    m "No..."
    m "I have no idea what this is."
    s "Weren’t you just saying a little while ago how you know every nook and cranny of Kumon-mi?"
    m "I’ve been wrong before."
    m "And I guess I’m wrong again now."
    s "Well, we were on our way to a shrine, weren’t we? Why not just go check out this one instead?"
    m "Is there even anyone inside? It seems extremely quiet for a shrine on New Year's."
    s "I doubt we’ll find out without going in."
    m "I don’t know. Something seems off."
    s "Are your supernatural powers tingling or something?"
    m "That’s not it."
    m "It just feels like this would be the two-panel shot at the end of a manga volume."
    s "I can’t imagine I’d make a very good manga protagonist."
    m "I would make up for it. Don’t worry."
    s "Are we going in then? Or does the manga end here?"
    m "I think we kind of {i}have{/i} to go in at this point. We’ve stood here for long enough that this is now an important story beat."
    s "Should I lead the way?"
    m "Probably. You {i}are{/i} the self-proclaimed protagonist after all."
    s "Do you want to hold hands on the way up the stairs?"
    m "Not particularly, no."
    s "Then I guess just..."
    s "Follow me."

    scene black
    with dissolve2

    "The further we ascend, the further the shrine seems to move away from us."
    "I’m sure it’s just an optical illusion or exhaustion kicking in, but it really does feel like something out of a book."
    "The blinding light exuding from the interior of the shrine doesn’t help either."
    "It’s so strong that I’m forced to cover my eyes."
    "I turn back for a brief moment to find Maya doing the same."

    play sound "static.mp3"
    scene mercy1 with flash
    scene mercy2 with flash
    scene mercy3 with flash
    scene mercy4 with flash
    scene mayanightwalk12 with flash
    stop sound

    "Then I turn back around and we’re already inside."

    play sound "static.mp3"
    scene mayanightwalk13 with flash
    stop sound

    "There’s a thing in front of us, pushed through another thing with some things above it."

    s "..."
    m "..."
    m "Well, that was anticlimactic."
    s "How is a shrine out of order, exactly?"
    m "How should I know?"
    s "I mean...you {i}are{/i} a shrine maiden."
    m "I’m only a shrine maiden out of necessity. And in my many, {i}many{/i} years of service, I have not once had to put an “Out of order” sign on anything."
    s "I’m beginning to understand why there’s not anyone here. "
    m "Perhaps “Out of order” simply means that this shrine was abandoned by its god?"
    s "Is that a thing that actually happens?"
    m "Probably. Gods are assholes."
    s "What kind of god do you think it was?"
    m "You know, I’m going to go out on a limb here and assume it was some sort of rabbit. Don’t ask me where I got that idea, though."
    s "So...are we still supposed to pray?"
    m "To what? It’s either abandoned or out of order and neither of those things makes me confident our prayers will be heard."
    s "What makes you so confident your normal prayers will be heard?"
    m "A depressing amount of willpower and a keen sense of intuition."

    scene black
    with dissolve2

    "We stare at the shrine for another moment. "
    "That moment is followed by several other moments."
    "It seems that neither one of us wants to look away for some reason, but it’s not one I can put my finger on."
    "Perhaps we’re just trying to make the best of a long journey to nowhere."
    "But, then again-"
    "That’s what we’re always doing."

    scene mayanightwalk14
    with dissolve2

    "Maya is the first to break free of the rabbit’s hold as she turns around and takes up her normal seiza position, facing the way we came in."
    "I follow her lead and sit beside her, albeit with posture much worse and a significant increase in disrespect."
    "This might come as a bit of a shock to you, but I don’t like places like this."
    "I don’t like religion in general. "
    "Or rather, I don’t like the people who devote themselves to someone or something just because they think they should."
    "I don’t like the immediate acceptance and refusal to question why the focus of their feverish passion doesn’t ever actually {i}do{/i} anything."
    "And yet every morning, I put on this blazer and make my way across town."
    "I take my place behind a podium in a building I should have never been allowed to set foot in."
    "And I revel in the fact that there are so many people exactly like that- focused on me instead of anything else."
    "No god deserves the praise they are given."
    "And neither will I until I do something worthy of obtaining it."
    "But {i}god{/i} will I drink it down anyway."

    s "Why did you become a shrine maiden in the first place, Maya?"
    s "And...how long have you been one?"
    m "Which of those two questions would you prefer I answer first?"
    s "Whichever one has a less convoluted answer."
    m "Sometime around middle school, then."
    m "The end of elementary, perhaps?"
    m "It’s not exactly easy to remember minor details like that from so long ago. But I know it was before [high_school]."
    m "As for {i}why{/i}..."

    scene mayanightwalk15
    with dissolve

    m "Let’s just say I liked the dress."
    s "I kind of want to know the real answer."
    s "If you’re still doing it after all this time, I imagine it must have been a lot more serious than just liking the dress."
    m "I’d quit if I could. Honestly."
    s "Why can’t you?"
    m "Why does it matter?"
    s "You could be using that time for something else."

    scene mayanightwalk16
    with dissolve

    m "Like what? Waiting for you to come knock on my door? Listening to Ayane sing Despacito or helping Ami brush her obnoxiously long hair?"
    m "The shrine is a reprieve from the parts of my life that I struggle with tolerating every hour of the day."
    m "And if it weren’t for the spiritual aspect of it, I’d find it quite nice as my own reclusive hang out spot."
    s "There are other hang out spots, though."
    m "But how many of them will allow me to keep doing what I’m doing?"
    m "I’ve toyed with the idea of leaving before. Especially when I was getting a new {i}you{/i} every four months or so."
    m "But I ultimately decided against it because, on the off chance that there is {i}something{/i} about being a shrine maiden allowing me to persist through each reset-"
    m "Well, I don’t want to risk severing that."
    s "What if severing that connection repairs everything, though?"
    m "What if it doesn’t?"
    m "Besides, there’s absolutely no way this world is convenient enough to just “get repaired” by something as inconsequential as me not sweeping a staircase for several hours each weekend."
    m "The shortened version is that I do not want to risk this world dramatically changing- even with how much I’ve grown to abhor the mundane aspects of it."
    m "If all I’m faced with is a minor inconvenience two days out of every week, I will face it head-on....over and over again until I can no longer stand up straight."
    s "You’re doing all of that for me?"
    m "No, you narcissistic asshole. I’m doing it for everyone. "
    m "I suppose your sliver of the pie chart is a little larger than the others, though. Why that is, I will never understand."
    s "I understand."

    scene mayanightwalk17
    with dissolve

    m "Don’t say it a-"
    s "Because you’re in love with me."
    m "...gain."
    s "{i}Why{/i} you’re in love with me is still far beyond my comprehension, though."
    m "That is literally the exact thing I was saying."
    s "Does {i}that{/i} count as a confession?"
    m "Do you feel your brain liquefying?"
    s "I don’t think so."
    m "Then no. Probably not."
    s "Maybe we can avoid the whole blackout thing if you just think up really creative ways to say it instead of being blunt about it."
    m "Or maybe we can keep doing exactly what we’ve been doing since you “woke up” and maintaining a healthy distance that doesn’t spiral into a never ending pool of regret for both of us?"
    m "I think that sounds fun. Let’s go with that option."
    s "You’re going to break one day and you know it."

    scene mayanightwalk18
    with dissolve

    m "I have no idea what you’re talking about."
    s "You really-"
    m "Stop it. Please."
    m "I’ve heard it enough today."
    s "..."
    m "..."

    scene mayanightwalk19
    with dissolve

    s "Sure."
    s "Did you want to maybe start heading back soon, though?"
    s "As much as I appreciate and understand your love for shrines now, I highly doubt you want to spend the entire night at one."
    m "Back home or back to the festival?"

    scene mayanightwalk20
    with dissolve

    s "Is the festival still going? It seems pretty late."
    m "It should be. We’re quite a way from the main area, but I imagine we would have still heard the fireworks if they were set off."
    m "We missed the ones on Christmas, so I’d like to see these if you’re okay with it."
    s "Why wouldn’t I be okay with it?"
    m "Sorry, you might be fine with it {i}now.{/i} But who knows what would happen if another pink-haired girl were to show up out of nowhere and profess her love to you while we’re on the way?"
    s "I’d have to tell her I’m already on a date tonight."
    m "This isn’t a date."
    s "..."
    m "What? It’s not."
    s "Sure, Maya."

    scene mayanightwalk21
    with dissolve

    m "It’s not!"
    s "Uh-huh. Whatever you say."
    s "I'm going to start heading over now."

    scene mayanightwalk22
    with dissolve
    stop music fadeout 8.0

    m "It’s not a date!"
    s "Can’t hear you. Walking away."
    m "I mean it!"

    scene mayanightwalk23
    with dissolve

    m "..."
    m "..."
    m "..."

    scene mayanightwalk24
    with dissolve

    m "Hah..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ mayafestival3 = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump mayafestival4

label mayafestival4:
    play music "ihaveto.mp3"
    scene hanabi1
    with dissolve4

    "When was the last time you felt alive?"
    "Because in this moment, I feel more alive than I have in a very, very long time."
    "Something about how small everything looks from all the way over in this unknown part of the world makes even breathing exciting."
    "I time my inhalations to match the explosions in the sky. "
    "My lungs hate me for it, but my heart has hated me for much longer."
    "Pretty soon, every last organ in my body will give up on me."
    "I’ll be left decaying in a bed somewhere, wondering why I didn’t take more time to appreciate moments like this."
    "I hope that wherever that bed is, there’s a window."
    "And I hope that the view from it will be even half as nice as this one."
    "I wonder if she ever saw anything like this."
    "I wonder if she’d appreciate it as much as I do."

    m "I feel bad for the people living directly underneath all this."
    m "It’s nice from up here, but I can’t say I’d be very happy if there were fireworks above my house periodically throughout the year."
    s "I’m surprised they’re even doing something like this over here. "
    s "It looks like they’re being lit off in that forest over there. "
    m "Do you have a sudden interest in fire prevention or something?"
    m "There’s nowhere else to light them off around here. "
    m "It’s not as if they can be set off over a lake or river when the closest bodies of water are miles away."
    s "Oh well. Sucks for everyone trying to get some sleep right now, I guess."
    m "It certainly does. We’ll just have to continue enjoying this at the expense of everyone below us."
    s "I’ve gotta say, this seems like a pretty high budget affair for a part of Kumon-mi no one really travels to."
    m "Fireworks are relatively inexpensive. And, from what I understand, all of the lanterns and stalls were put together by the people still living here."
    s "And the six thousand vendors we bought food from?"
    m "Individually funded, I assume. I’m sure there were some vendors from the other districts too."
    s "Does this district have a name?"
    m "If it does, I don’t want to know it."
    s "Why does everything always have to be a mystery with you?"
    m "Because the only thing worse than being stuck in one place for all eternity is being stuck in one place and knowing everything about it."
    m "Missing details give me more to think about."
    s "No wonder why you’ve been smiling so much lately."
    m "Yes, it’s quite nice being able to do that in between the incessant bouts of emotional turmoil and mental strain."
    s "At least you can relax now."
    m "How unfortunate that an entire village must suffer for it."

    scene hanabi2
    with dissolve2

    "The fireworks don’t let up. But, in between the bursts of light, we can still hear the chatter from the festival below."
    "It seems that the later it gets, the more people show up."
    "And while plenty of them seem focused on tonight’s display, there are plenty others who don’t."
    "There’s even a surprising amount of men here- something I haven’t been able to say in...I guess what would be the equivalent of about a year in recycled time."
    "Maybe two?"
    "I’ve stopped keeping track of how long it takes for anything to happen here."
    "There’s just no point to it when you know that all clocks have stopped rotating in any meaningful way."
    "Surprisingly enough, I don’t hate the voices from below."
    "It’s hard to put it into words, but even this wide array of loud, intrusive noises feels incredibly quiet atop this hill."
    "Occasionally, a gust of wind will attack us from behind in an attempt to distract us from gazing too long at something neither of us deserve to see, but we pay it no mind- for we’ve already spent all we have."
    "That’s right."
    "Neither one of us has anything left to spare."

    m "Can I interrupt this moment to be cliche once again?"
    s "Sure. Just don’t put your hand in front of my face when you raise it up to the sky to measure stars or whatever. I’m actually enjoying watching these."
    m "I won’t."
    m "It’s just that, as the resident astronomy expert of our make-believe manga, I’m obligated to tell you the story of Altair and Vega at least once before the series concludes."
    s "That’s fine. You’ve gone the entire day without talking about the stars."
    s "I yield the floor to you now as a reward for your good behavior."
    m "Vega- or Alpha Lyra, which is the fifth brightest star in the entire sky...was said to be some sort of celestial princess according to Chinese mythology."
    m "Under the impression she’d be alone for all eternity, Vega began to lose hope and grew depressed."
    m "But, one day, a random mortal by the name of Altair showed up and Vega thought, “You know what? Fuck it. I’m lonely and this is the best I can find.”"
    s "I feel like every other iteration of this story I’ve heard has started off a little more romantic."
    m "Yeah, well, sometimes it doesn’t really work that way."
    m "Anyway, as Vega and Altair began to spend more time together, the two of them gradually started to fall in love- even though she was significantly better than him in every way."
    m "Vega promised Altair that, no matter what happened, the two of them would always be together. And since she was a goddess of the sky, Altair knew she meant business."
    m "But when Vega’s father found out about this, he got extremely pissed off."
    m "It was one thing for Altair to be mortal- but hearing that his daughter promised a seemingly eternal life in the heavens to her lover...saying Vega’s father was infuriated would be a bit of an understatement."
    m "In a fit of passive aggressive rage, he used his power to grant Vega’s wish- but in the worst way possible."
    m "The two of them were placed into the sky as stars, but separated by the Milky Way."
    m "They were {i}together{/i} in a technical sense, but as far apart as possible."
    m "But every year, on the seventh night of the seventh moon, a bridge would form across the Milky Way...and Altair would cross over to meet his lover."
    m "One night every year, the two of them could be together."
    m "But once the night would come to an end-"
    s "You don’t have to tell me how the story ends. I already know it."
    s "Besides, it’s too sad anyway."

    if bonus == True:
        s "Here’s hoping that Altair and Vega can stay together this year and have tons of white-hot, celestial star sex with each other."
    else:
        s "Here’s hoping that Altair can get Vega hugnant."

    m "You’re disgusting."
    s "You’re a nerd."

    scene hanabi3
    with dissolve2

    m "..."
    s "..."
    s "Does-"
    m "Don’t talk. You’ll just ruin everything."
    s "Fair enough."

    "Maya rests her head upon my shoulder. And while I can’t see her face, I can feel the smile count increase by one."
    "We meet on the other side of a bridge of magpies and, for just one night, detach ourselves from the rules that govern us every other day of the year."
    "Or at least that’s what we would do if we were stars."
    "But neither one of us is anywhere near bright enough to come close to one of those."
    "And even if, by some strange twist of fate, we were placed in the night sky along those same lights Maya dedicates at least ten hours a week to staring at-"
    "Even if that were to happen, I doubt the Milky Way could keep me from her."
    "I like annoying her far too much to let something like that get in the way."
    "The two of us may share some connections to those literal star-crossed lovers, Altair and Vega-"
    "But we’re our own creatures."
    "And there’s a high likelihood that there are {i}other{/i} creatures looking up at {i}us{/i} from somewhere underneath-"
    "And that they’ll hand down stories about us for generations and generations, despite how depressing or unfortunate they may be."
    "Hopefully, the stars can hear their story one day."

    s "..."
    m "..."
    m "Why did you tense up just now?"
    s "I just had some really immature, star-related thought that you would probably think is cute."
    m "Don’t share it. You and {i}cute{/i} don’t belong in the same room together."

    if bonus == True:
        s "I guess that defeats any chance of us ending up at a love hotel tonight, then."
    else:
        s "I guess that defeats any chance of us ending up in my bedroom playing with my Pokemon cards after this, then."

    m "As if that chance ever existed in the first place."
    s "I feel like it did."
    s "Or does."
    s "I feel like-"
    m "Shut up and watch the fireworks."
    m "The grand finale is close."
    m "I can feel it."
    s "..."
    m "..."
    s "Okay."

    if bonus == True:
        scene hanabi4
        with dissolve2
        $ renpy.pause(2, hard=True)
        scene hanabi3
        with dissolve2
        $ renpy.pause(2, hard=True)
        scene hanabi4
        with dissolve2
        $ renpy.pause(2, hard=True)
        scene hanabi3
        with dissolve2
        $ renpy.pause(2, hard=True)
        stop music
        play sound "static.mp3"
        scene magpie with flash
        scene black with flash
        scene magpie with flash
        scene black with flash
        scene magpie with flash
        scene black with flash
        scene black
        with flash
        stop sound
        $ renpy.pause(10, hard=True)
        play sound "static.mp3"
        scene smile with flash
        scene hanabi5 with flash
        stop sound
        play music "undoitall.mp3"

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
        "..."
        "..."
        "..."

        "The sky!"
        "An egg, an egg- what’s in an egg?"
        "A chicken?"
        "A duck?"
        "Another white egg?"
        "Maya’s hands find their way to mine."
        "They fuse together into one larger hand."
        "////////////////ADD HAND"

        scene hanabi6
        with pixellate

        "////////////////HAND SUCCESSFULLY ADDED"

        m "I had a dream that I was flying."
        m "You were there, but it wasn’t actually you."
        m "We were on the roof. The same room. At different times. The same place."
        m "The sky turned black and I felt a bubble begin to form underneath my forearm."
        m "You approached me and helped me pop it."

        play sound "static.mp3"
        scene hanabi7
        with flash
        stop sound

        m "From out of the bubble oozed a thick, yellow liquid."
        m "You lapped it up like a cat and told me that we would be better for it."
        m "I never forgot the sensation of that bubble popping. Or the tip of your tongue as it explored the inside of my arm."

        play sound "static.mp3"
        scene hanabi8
        with flash
        stop sound

        "I knew right then that it was egg time."
        "The hard-ish but not that hard white oval in my hand, reminiscent of holding a half-complete baseball- where the insides are all messed up and confusing when unwound."
        "Have you ever egg before?"
        "I would not recommend it unless you are ready."
        "Sometimes, people think they can egg when they can’t."
        "Then, before you know it-"

        play sound "static.mp3"
        scene hanabi9
        with flash
        stop sound

        "Squid!"
        "But why squid?"
        "This is second time squid show up in special Maya event chain! Not understand!"
        "Me teach."

        play sound "static.mp3"
        scene hanabi10 with flash
        stop sound

        "Everything in the waters that has fins and scales, whether in the seas or in the rivers, you may eat."
        "But anything in the seas or the rivers that has not fins and scales, of the swarming creatures in the waters and of the living creatures that are in the waters, is detestable to you."
        "You shall regard them as detestable; you shall not eat any of their flesh, and you shall detest their carcasses."
        "Everything in the waters that has not fins and scales is detestable to you."
        "This is my word."
        "Egg is okay, though."

        play sound "static.mp3"
        scene hanabi1 with flash
        stop sound

        m "Oh, I forgot."
        m "I got something for you."
        s "For me?"

        play sound "static.mp3"
        scene hanabi11 with flash
        stop sound

        m "Yes."
        m "I figured that it would be best to uphold this tradition as well, given my hesitancy when it comes to accepting change."
        s "What is it?"

        play sound "static.mp3"
        scene hanabi11x
        with flash
        stop sound

        m "A box."
        m "I don't have it with me."
        m "In fact, it's not really a present at all. I just need your help carrying it."
        s "Am I at least allowed to know what’s in it this time?"

        play sound "static.mp3"
        scene hanabi12
        with flash
        stop sound

        m "Only if you can open it."
        m "In the event that you can’t-"
        a "Sensei?"
        s "..."
        m "Wait, are you okay? You feel...ten degrees colder all of a sudden."
        a "Is...everything okay?"
        s "Everything is okay."

        play sound "static.mp3"
        scene hanabi4 with flash
        stop sound

        s "Everything is okay."
        m "I see..."
        m "Then, if you’re okay with it-"

        play sound "static.mp3"
        scene hanabi13 with flash
        stop sound

        m "I’d like to stop by both my dorm room and the school once we’re done here."
        m "It’s a little cold to be wearing a yukata anyway."
        m "I figured it would stay warm for a little longer."
        te "What’s wrong?"
        te "We won’t have time to play if you don’t hurry up and help me finish here."
        s "Yes. It {i}is{/i} too cold for a yukata."
        te "Yukata? What are you talking about?"
        s "I-"

        play sound "static.mp3"
        scene hanabi4
        with flash
        stop sound

        av "Do you ever feel yourself coming unglued?"
        av "How much skin comes off as you peel yourself to freedom?"

        play sound "static.mp3"
        scene hanabi14
        with flash
        stop sound

        ay "One very large banana!"

        play sound "static.mp3"
        scene hanabi15
        with flash
        stop sound

        c "Come on! Take the picture already!"
        mi "We ain’t got all day, Sensei!"
        mak "Yeah, Sensei!"
        r "Y-Yeah, Sensei! What are you waiting for?!"
        f "What are you waiting for?"
        y "What the fuck are you waiting for?"
        m "What the fuck are you waiting for?"

        play sound "static.mp3"
        scene hanabi16
        with flash
        stop sound

        s "Huh?"
        m "What are you waiting for?"
        m "You’ve been holding that box and staring into space for about a minute now."
        s "Weren’t..."
        s "Weren't we just at the festival?"
        m "If by {i}just{/i} you mean like two hours ago, yes."

        scene hanabi17
        with dissolve

        m "Wait..."
        m "Is it happening again?"
        s "Is what-"
        m "Are you blacking out?"
        m "Dreaming?"
        m "What’s going on? I can’t help you if I don’t know what it is- and you’ve seemed fine this whole time."
        s "I..."
        s "I don’t feel fine."

        scene hanabi18
        with dissolve

        m "I’d like to assume it’s just because you’re tired, but something tells me that would be far too convenient."
        m "Do you want to, like...lay down? Or go home?"
        m "We don’t have to do this tonight. There’s still time."
        s "No. We can do it now."
        s "You wanted to spend the whole day with me, so..."
        m "Yeah, but it’s already the {i}next{/i} day, {i}so...{/i}"
        s "I’ll be fine. If I’m able to hold a conversation with you now, the worst of it is probably over."

        scene hanabi19
        with dissolve

        m "Well, good. Because I hate having to carry that thing on my own."
        s "Yeah..."
        s "You carry enough as it is."

        scene black
        with dissolve2

        "I carry a box."
        "I have a sudden craving for eggs."

        stop music

        "////////////////MAYA EVENT COMPLETE"
        "////////////////THERE ARE NO MORE MAYA EVENTS IN CHAPTER 2"
    else:
        scene black
        stop music

        "THE EVENT IS OVER."
        "THERE WAS NEVER ANYTHING ELSE HERE."

    $ renpy.end_replay()
    $ maya_love += 25
    $ mayafestival4 = True

    "{i}Maya’s affection has increased by 25!{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 7
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
        jump saturdaymorning
    else:
        "ERROR ADVANCING TO SUNDAY"

label shrine40:
    scene noonsky
    with dissolve2
    play music "shrinesong.mp3"

    "There is naught to do in summer but bathe in the muggy omnipotence of its tangible, suffocating humidity- so thick that I can feel it embracing me as I make my way up a familiar set of stairs."
    "I can see distorted lines in the air from where it has gotten confused, and I do my best to look past them as making them even more self-conscious would not bode well for the weather."
    "If you’re wondering what I’m talking about, you’re not alone. For thoughts like these have been plaguing me for thirty minutes as I’ve become fed up with this mid-year glow and all it means for Kumon-mi."
    "Soon enough, the cold will return — and with it will come the death of something that never should have been in the first place."
    "The sun, and all its toxic rays."

    scene black
    with dissolve2

    "The distorted shape of summer tapers off along with the last of the stairs as something else comes into my line of sight."

    scene mayanemaiden1
    with dissolve2

    "Can you see it too?"
    "Or does the appearance of something you’re unable to explain hurt you more than any amount of the heat’s embrace ever could?"

    s "Is something wrong, Maya?"
    m "Something is always wrong. "
    m "It’s hot, this dress is heavier than it looks, and to complicate things even more, {i}you’re{/i} here now."
    s "I can leave if you want."
    m "Okay. See you."
    s "Actually, I think I’ll stay."
    m "It’s extremely irritating how your existence continues to...{i}irritate{/i} me even after the most...{i}irritating{/i} parts of it have gone away."
    s "I’m starting to think you might be irritated."
    m "Shut up. It’s hot."

    "It’s funny to think of how little things have changed after all we’ve been through."
    "In fact, I feel like most of my early conversations here were just like this. "
    "I’d show up out of nowhere, seek out a young girl a full foot shorter than me, and then promptly ruin her day because something about annoying her made me feel a little more human."
    "Just being around her now has that effect."
    "And even when she looks at me like that, in complete disregard for all the two of us have gone through-"
    "I want nothing more than to remove her dress, carry her back to my room, and make her cry out my name."
    "My real name."

    m "Can you save your disgusting, lustful glares for when I am {i}not{/i} melting? Thanks."
    s "My room has air conditioning, you know."

    scene mayanemaiden2
    with dissolve

    m "Okay, so I guess that’s a “no.” Wonderful."
    s "Wonderful indeed. So, are you ready to talk about that thing I said to you on the beach? Or are we really going to keep ignoring it?"
    m "Now is...really not the time for that. "
    s "Any reason why? Or are you just continuing to avoid me because it makes things more convenient and-"
    ay "Sensei!"

    scene mayanemaiden3
    with dissolve

    s "Oh, okay. I get it now."
    m "Just kill me already. I’m starting to miss the more peaceful cycles from before I had {i}feelings{/i} and {i}bonds{/i} I had to worry about."
    ay "Thanks for having tons of sex with me the other day! I had a great time!"
    m "And that. That might be the worst part of all."
    s "Ayane, let’s not talk about what we do in our free time around...literally anyone else. Let alone at a- wait, why are you also a shrine maiden all of a sudden?"

    scene mayanemaiden4
    with dissolve

    m "Because she’s starting to become just as obsessed with {i}me{/i} as she is with you. Thanks for that."
    s "How is that my fault? Ayane got attached to you on her own and I had nothing to do with it."
    ay "You had a little bit to do with it."
    s "You’re not helping. And that still doesn’t explain where you got the dress or why you’re here instead of the dojo."
    m "I gave her the dress, obviously."
    s "Well, no wonder she’s obsessed with you. You’re giving her free stuff. Be more like me if you want her to go away. I never give her anything."
    ay "That’s not true. You give me {i}that dick{/i} all the time."

    scene mayanemaiden5
    with dissolve

    m "Didn’t I ask you to sweep the inside of the shrine? "
    ay "I finished up as quickly as I could when I heard Sensei’s footsteps coming up the stairs."
    m "Well...go do it again. It’s distracting having to listen to you brag about your sex life all day now that you’re no longer practicing abstinence. "
    s "Can someone please explain to me why Ayane is a shrine maiden now or are we going to keep annoying Maya instead? "
    s "I’m fine with the latter, I just don’t know what level of seriousness we’re going for today."

    scene mayanemaiden6
    with dissolve

    m "Hah..."
    m "The reason I gave her the dress and the reason I’m having her tidy up the shrine is because it seemed like the most...practical option considering her newfound interest in my daily routine."
    m "I figured that if she’s going to be hanging around here, I should at least have her {i}work{/i} so our time is not entirely wasted."
    ay "Me working here means that we get to talk about more reset-stuff too. "
    ay "And since nobody else ever really shows up, we don’t have to worry about some other girl from class appearing at the wrong time and thinking we’re plotting a takeover of the universe or something."
    m "I think there’s a higher likelihood that someone like that would just interrupt us, but I suppose that’s not really important right now."

    scene mayanemaiden7
    with dissolve

    m "At the end of the day, I see minimal harm in taking on an apprentice if that apprentice is going to actually {i}work.{/i} Plus, having someone to brainstorm with is also a bit of a bonus."
    m "We can chalk Ayane’s new role up to just...formal inclusion and proof of her new place in this never-ending timeline."
    ay "Phase one, rooftop apocalypse buddy! Phase two, coworker-slash-shrine maiden buddy!"
    s "What’s phase three?"

    scene mayanemaiden8
    with dissolve

    ay "A bride!"
    m "Did you really have to ask?"
    s "Mine? Or Maya’s? Because the other two phases both involved her."

    scene mayanemaiden9
    with dissolve

    ay "I don’t like girls. But Maya is cute and I’d probably marry her for tax purposes if I make it to twenty and Sensei still doesn’t-"
    m "Rejected. "
    ay "Oh well. My family’s rich and I probably won’t even have to pay taxes anyway. But if you change your mind and-"
    m "No. "
    s "You tried, Ayane. And that’s all you can really do with Maya."
    ay "I’ll get her to love me one day. I can feel it."
    s "So, is this just...what you two do now? Hang out at a shrine and talk about time travel?"
    m "That’s not much different from what I usually do. The only substantial change is that I now have to hear about how great you are every five minutes."
    m "I’m sure I’ll work up an immunity to it sooner or later like I have with basically everything else."
    ay "Hey, if getting involved in the resets is all it took to land me a job here, does that mean everyone {i}else{/i} gets to become a shrine maiden too if they all wind up making it to the roof?"
    s "This is a question I take personal interest in, so I’d like to hear an answer to this as well."

    scene mayanemaiden10
    with dissolve

    m "Ayane, {i}please{/i} don’t forget that this whole thing with you is some strange fluke and that the likelihood of anyone {i}else{/i} getting roped into this reset business is basically zero."
    ay "Right, yeah. Because you haven’t gotten any other prediction wrong so far. I forgot about that."
    m "Please don’t make me regret the decision to let you get closer to me in sheer physical proximity only with zero room for substantial emotional attachment. "
    ay "Aww, I love you too."
    s "What if someone else {i}does{/i} make it up there, though? "

    scene mayanemaiden11
    with dissolve

    m "Are you only asking because you want to see {i}them{/i} in the dress as well? "
    s "No. I’m asking for the sake of the universe. But the dress part does help."

    scene noonsky
    with dissolve

    m "Ugh...I guess that’s just one more bridge we’ll have to figure out how to cross if we ever manage to make it there."
    m "For now, I think it would be best if we were to come up with some sort of gameplan on what we want to accomplish {i}this{/i} cycle."
    m "During the last one, we discovered that it is not entirely impossible for others to gain some sort of awareness as well. Which would mean that {i}this{/i} time-"
    ay "We need to test that theory again, right?"

    scene mayanemaiden12
    with dissolve2

    m "Uhh...yes, actually. But how did you know I was going to say that?"
    ay "Because I’ve been secretly traveling through time longer than you and know everything that is going to happen from this point onward."
    ay "Spoiler alert, I end up with Sensei. "
    m "Sure, but how did you {i}actually-{/i}"
    ay "Because it’s the same thing you did last time with the whole pregnancy thing. "
    ay "You came up with a theory and decided to spend the entirety of the last cycle {i}testing{/i} that theory and inflicting a great deal of suffering on both Sensei {i}and{/i} me."
    ay "It’s not really science if things happen only one time, so experiments like this are good for when you want to prove that something wasn’t just a fluke."
    ay "Which is, surprisingly enough, a thing you directly contradicted by calling {i}me{/i} a fluke a few minutes ago. "
    ay "But hey, if you want to only believe in certain things when they make you sound smarter then, by all means, proceed."
    m "You know, you spend so much time being absolutely unbearable that I forget how smart you really are sometimes."
    ay "I know. I’m a real catch, aren’t I?"

    scene mayanemaiden13
    with dissolve

    m "What Ayane said just now was right."
    s "The...part about her being a catch?"
    ay "Sensei already knows that. You don’t have to remind him."
    m "Not that part. The part about needing to test this theory of other girls catching onto the resets."
    m "It didn’t happen until very late in the cycle last time, so if we can manage to convince someone we’re not completely insane a little {i}earlier{/i} this time, we might have better luck finding something out."
    s "Okay...but then what?"
    m "Then...we know more things. It’s called {i}learning.{/i} As a teacher, this information should be invaluable to you."
    ay "What Maya means to say is that if we learn things quickly enough, you might get a {i}third{/i} shrine maiden soon."
    s "That I can understand and it is something I will strive for. Thank you, Ayane."
    ay "Don’t mention it."
    m "Can you maybe attempt having some sort of drive that {i}doesn’t{/i} pertain to young girls in costumes in the future? Or is this just what I’ve signed up for?"
    s "If anyone should know, I think it should be you."
    m "It is. I was just looking for a little false encouragement as it might make this terrible day slightly more bearable for a few minutes."
    s "Then I will do it for science."

    scene mayanemaiden14
    with dissolve

    m "Ugh, forget it. You’re a terrible liar and asking someone as self-serving and incompetent as you to do anything just makes {i}me{/i} look like an idiot."
    s "Is there anyone you have in mind as a {i}target?{/i} Should we try our luck with Yumi and Tsuneyo again? Maybe see if they have some...lingering memories from the last reset or something?"
    m "I...{i}attempted{/i} speaking with Tsuneyo on my own, but I think it’s safe to say she doesn’t remember anything. As far as Yumi goes...I’d rather not approach her."
    s "I can talk to Yumi. That would probably go a little better than either of you-"
    ay "What about Ami?"

    scene mayanemaiden15
    with dissolve

    s "Ami?"
    ay "Yeah! She’s the closest to us out of everyone and I’m sure she’d be open to hearing us out. Especially since it’ll help her feel less excluded and stuff."
    ay "She might think we’re a little crazy at first, but she’s gullible enough to start believing us if we keep pressing her about it."
    m "Ami’s not a good idea, Ayane."

    scene mayanemaiden16
    with dissolve

    ay "She’s not? Why?"
    m "It’s...a long and complicated story."
    ay "I mean...I don’t have anything else going on. You can tell me about it if you want."
    m "I’m afraid the story is far too long and far too complicated to just {i}tell{/i} you. I wouldn’t be recounting some tale of how I was banned from a convenience store or anything like that."
    m "I’d be describing probably decades or...centuries of trying that exact thing to no avail as I thought the same thing as you. "
    m "And not only did it never work, it made her...mad."
    m "It’s just not worth the effort."
    ay "Ami? Mad? But if it doesn’t involve Sensei, she basically never gets mad. And Sensei wasn’t a recurring thing for this until a couple cycles ago, right?"
    m "Yes and...no. That’s also a little too complicated to just casually recount."
    s "..."

    scene mayanemaiden17
    with dissolve

    ay "Well...we can sideline the Ami thing for now and maybe talk more about that later. I can tell by that face that this might be a touchy subject for you."
    m "Thank you. I think Yumi remains our strongest prospect for the moment, but I’m sure there are other names that might pop up as this iteration of the school year goes by."

    scene mayanemaiden18
    with dissolve

    m "What matters most is that we do {i}something.{/i} Time itself might be infinite, but who knows if {i}ours{/i} is?"
    m "Understood?"
    s "Yes, captain. Just tell me what to do and I’ll do it."
    m "Excellent. Go away."

    scene noonsky
    with dissolve2

    s "Got it."
    m "Wha-"
    m "Did that...actually work?"
    ay "Maya! You can’t just send our boyfriend away like that! He’s sensitive!"
    m "Our {i}what?{/i} Shouldn’t you be sweeping?"
    ay "Sensei! Wait for me! I’ll love you when she can’t!"

    "Ayane chases after me as I go to leave, but is promptly grabbed by the collar as Maya drags her back under the protection of whatever god resides here."
    "I’m not leaving because I was told to, but I’m sure you probably understand that based on my {i}history{/i} here."
    "It’s just far too disgusting out here today and..."

    s "..."

    "And staring so long at something I can not have hurts me more than any amount of the heat’s embrace ever could."

    scene black
    with dissolve2

    "This cycle will melt the wax of my wings."
    "I’m flying too close to the sun."

    $ renpy.end_replay()
    $ shrine40 = True
    $ maya_love += 1
    $ ayane_love += 1
    stop music fadeout 6.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label mayadate45:
    scene nightsky with dissolve
    play sound "phonebeep.wav"

    "I tap on Maya’s name in my phone and think about how many other versions of me have been able to narrate that."
    "Sure, it may have taken the end of several worlds (Or several ends of one world) for me to {i}be able{/i} to share something like this with you, but...I’m here."
    "And hopefully soon, she will be as well."
    "As I stare down at a name that is perhaps the most important to me (Barring the recent intrusion of another girl I’ve known for far too long), I think about what I’m going to say when she picks up."

    play sound "phonebeep.wav"

    "But then she picks up."
    "And I still have absolutely nothing."

    s "..."
    m "..."
    m "Uhh..."
    s "..."

    play music "love.mp3"

    m "You realize you’re suppose to say words after you call someone, correct?"
    s "Yeah...what are you doing right now?"
    m "I..."
    m "I don’t want to answer that question."
    s "Why not?"
    m "Because it will be succeeded by an invitation to wherever you are right now."
    s "And?"
    m "And..."
    m "I, depressingly, don’t think I’d be able to say no."
    s "Let’s meet at my apartment, then."
    m "You-"
    s "We still haven’t talked and I don’t want to just pretend that what happened on the beach was some spur of the moment mistake."
    s "I’m tired of collecting dust. And you said it yourself that you also hate how stagnant things have become. "
    m "I don’t-"
    s "I get that it’s probably terrifying having to confront your feelings after all of this time. It’s terrifying for {i}me{/i} and I’ve only been doing this for what equates to, like...two or three years."
    s "But is there really any point in {i}anything{/i} you’ve done if neither one of us ever gets what we want?"
    m "{i}I don’t know.{/i} That’s the whole problem and it’s exactly what I’ve been trying to tell you this whole time."
    s "Then tell me in a way that’s easier to understand."
    m "I’m...{i}bad{/i} at that. I don’t like talking. Especially about sappy, childish stuff like {i}romance{/i}."
    s "You can carry on a conversation about time or the stars for days. "
    m "Talking about those things has never broken the world. "
    s "And talking about us has?"
    m "Have you not been paying attention to literally anything I’ve been telling you over the last “two or three years?” {i}Yes.{/i} Things have spiraled into chaos {i}every other time{/i} I have done that."
    s "This time is different and you know it."
    m "I know..."
    m "That’s why I’m so careful."
    s "Just come over. And don’t bring Ayane this time, even if she's still glued to you."
    m "Good idea. Wouldn’t want you getting distracted and having sex with her while we’re trying to talk."
    s "Maya-"
    m "I’ll stop at the convenience store. Is there anything you want?"
    s "When? Now?"
    m "Yeah. I’m on my way over so we can {i}talk{/i} if that will get you to stop bothering me about this every time we communicate. "
    m "But Sensei-"
    s "Call me by my real name."

    "There’s a silence at the other end of the phone."

    play sound "phonebeep.wav"

    "Then a beep."

    scene black
    with dissolve2

    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene mayaapt1
    with dissolve2

    "One hour later, she shows up at my apartment with plastic bags clasped in each of her hands."
    "She takes her shoes off at the entrance and I meet her at the door."
    "When she steps toward me, she feels shorter than normal."
    "I don’t know if it’s the lack of shoes or the mutual desire to hold one another that’s making her feel so much more fragile than normal but, unlike the others, I have no intention of breaking this one."

    s "You hung up on me."
    m "I did not. You dropped a bomb on me and I died."
    s "You’re pretty attractive for a dead girl, you know."

    scene mayaapt2
    with dissolve

    m "Great. One more disgusting fetish to add to the list. Thank you for complicating things within seconds of my arrival. I expected nothing less."
    s "Maya-"
    m "When?"
    s "Huh? When what?"

    scene mayaapt3
    with dissolve

    m "When did you remember?"
    s "Ah..."
    s "I didn’t."
    s "Niki told me."

    scene mayaapt4
    with dissolve

    m "Those {i}fucking{/i} Nakayamas will never stop being problematic. It’s an actual miracle you’re still here to talk about this when you could have been wiped right then and there."
    s "There seem to be a lot of miracles lately. And you can add to that list by joining those {i}fucking Nakayamas{/i} in calling me by my actual name."

    scene mayaapt5
    with dissolve

    m "I mean...it’s...it’s not as if I don’t {i}want{/i} to call you by your actual name...it just feels...wrong after all this time. And I’ve already gotten used to “Sensei,” so..."
    s "You’re embarrassed, aren’t you?"

    scene mayaapt6
    with dissolve

    m "Possibly. But I’m also taking into consideration the fact that you short-circuited from just touching me a while ago."
    m "And also how hearing something as important as your name from the girl more suited to you than {i}anyone{/i} might be a little more intense than hearing it from some shitty idol and her sister."
    s "Niki’s a good person, Maya. "

    scene mayaapt7
    with dissolve

    m "I don’t care. Things would be easier if she didn’t exist, so I will continue to want her to...not exist."
    m "Anyway, I’m hungry and I’m going to be eating now. I got you something too. Eat it or don’t. I don’t care."
    s "You know, I {i}knew{/i} you were tsundere this whole time but you kept denying it."

    scene mayaapt8
    with dissolve

    m "You don’t know anything! I’m the one who knows stuff! Now shut up and leave me alone!"

    scene mayaapt9
    with dissolve

    "Maya storms right past me like she owns the place and empties one of her bags out onto the dining room table."

    scene black
    with dissolve2

    "I follow behind her and join her as she sits down, taking note of the first of what I imagine will be the several thousand bento boxes required to fill her up."

    scene mayaapt10
    with dissolve2

    "But as she picks up her chopsticks, her newfound fragility somehow becomes {i}more{/i} apparent in the fact that she refrains from eating."
    "I remember her saying something along the lines of how she doesn’t like to be watched, but I can’t help but feel like this is more than that."
    "And call me self-centered, but I can’t help but feel like it is my fault."

    s "Something wrong?"
    m "Yes. Your ability to annoy me has become so strong that it is now capable of ruining my appetite. I hope you’re proud of yourself."
    s "Good. That just gives us more time to talk."

    scene mayaapt11
    with dissolve

    m "Nevermind. I’m hungry again. Please hold your words until...tomorrow. When I am gone."
    s "I’ll pass. It’s better we tackle this now before we have to-"

    scene mayaapt12
    with dissolve

    m "Why did you tell me that...thing you told me on the beach?! And why did you almost kiss me?!"
    s "What thing? That I’m in love with you?"

    scene mayaapt13
    with dissolve

    m "Yes! How can you say that with such a straight face?"
    s "What’s with the sudden change in reaction? You seemed pretty thrilled to hear that back then. And, if I remember correctly, you were the one who moved in for a kiss first."

    scene mayaapt14
    with dissolve

    m "You remember incorrectly. That doesn’t sound like a thing I would do. I’m much more reserved than that."
    s "{i}Were{/i} much more reserved than that. You seem a {i}bit{/i} less reserved than normal tonight for some totally strange reason that I have no idea of."
    m "Yeah, because you had to go and completely change our dynamic with a few words I didn’t think I’d ever hear again. "
    m "Do you have any idea how hard it is to keep my head on straight now? I’m supposed to be the one making us...conquer time or whatever and now all I can think about is...fireflies. And stuff."
    s "There are three of us now, Maya. You don’t have to be the ringleader anymore. We keep trying to tell you that."
    m "Yeah, and I keep trying to tell you guys that’s just who I am. But I’m apparently as bad at explaining myself as I am at theorizing, I guess."
    m "Damn it. Why did you have to invite me here? Why couldn’t we just be adults and mutually pretend that was some meaningless, fleeting moment between...acquaintances?"
    s "Because I want more of those moments."
    s "I want {i}you.{/i}"

    scene mayaapt15
    with dissolve

    m "Well...stop! "
    s "Do you remember what you said to me right before we almost kissed?"
    m "Yes but I don’t want you to repeat it because it directly contradicts basically everything I’ve said tonight."
    s "You said that if the world were to end right then, you wouldn’t care."
    m "I literally {i}just{/i} told you I remembered. You didn’t have to say it again."
    s "Do you care now?"
    m "Do you {i}not?{/i}"
    m "{i}You{/i} might be able to say cute things now and...remember your name and...talk about stuff involving us like it’s no big deal, but one wrong move on {i}my{/i} end and this could all be over."

    scene mayaapt16
    with dissolve

    m "Back on the beach...I lost sight of that for a second. That’s why I said what I said. "
    m "But when you left...I started thinking more and more about what might have happened if we followed through and..."
    s "..."

    scene mayaapt17
    with dissolve

    m "And the fear of losing you {i}again{/i} outweighs anything and everything."
    m "That’s what’s been pushing me forward this whole time. Everything I’ve done and everything I do is to protect {i}you.{/i} And...obviously myself as well. But you’re a really huge part of that."
    m "I might be a selfish, controlling know-it-all bitch, but I’m not so bad that I’d put your life at risk just because I want to kiss you. Which I obviously do because- "

    scene mayaapt18
    with dissolve

    m "Nope! See?! I almost said it again! Look what you’re doing to me!"
    s "When will you let yourself be happy?"

    scene mayaapt19
    with dissolve

    m "I should be asking {i}you{/i} when you decided to stop fighting the same fight as me."
    m "You might now be at the forefront of an inexplicable apocalyptic event, but the Sensei I know wasn’t this...{i}proactive.{/i}"
    s "He grew...and so should you."
    m "Even if that means putting both myself and {i}you{/i} at risk? And everyone else? Are you really willing to risk all of that for {i}me?{/i} Why? "
    m "There are nineteen other girls in class who apparently can’t cause your mind to shut down. Just choose one of them. It’s safer."
    s "How can you even say something like that when it’s so clear now how you feel about me?"

    scene mayaapt20
    with dissolve

    m "Oh, it fucking {i}sucks.{/i} It’s {i}so{/i} hard to say that...but I have to."
    m "It’s literally torture having to hear about how far you’ve gone with all of my friends while I’m stuck in the background pretending to not care. But honestly, I’ve gotten used to it."
    m "Even when it {i}wasn’t{/i} you it sucked, because it still kind of {i}was{/i} you in a really roundabout...physical-only sort of way."
    m "You should have been mine...like you were {i}before{/i} all of this started happening."
    m "And you’ll probably think this is pathetic but, after several lapses in judgement and an earth-shattering amount of desperation, I...may have caved into some of my carnal desires and...broken several Senseis. "
    m "But that’s exactly why I’m so scared of what will happen if we {i}do{/i} get closer. I’ve seen it firsthand."
    m "I can’t imagine how breaking the {i}real{/i} you would feel after how much it hurt to break all of those {i}fake{/i} ones just because I felt alone."
    s "Maya..."
    m "It’s okay...I’ll go back to normal tomorrow and you can keep screwing the rest of my classmates without having to worry about hurting my feelings. It’s fine. I get that you...like them too or whatever."
    m "I’m only like this tonight because {i}you{/i} wanted to talk and if I didn’t get all of this shit out of my head, I would have gone insane."
    m "But you {i}can’t{/i} love me. "
    m "The world won’t allow it."
    s "Fuck the world."

    scene mayaapt21
    with dissolve

    m "Fuck the world, indeed."
    m "I have no idea what either one of us did to deserve this, but it’s clear from our respective positions that some higher power has it out for us."
    m "And until we’re confident that we’re actually {i}free{/i} from this weird fucking chronoprison...we have to pretend we don’t feel the way we feel because that’s what keeps us safe."
    s "I see..."
    m "I knew you would. Even you’re not stupid enough to completely disregard your own life for one girl. "

    stop music fadeout 10.0

    s "Oh, no. I have no intentions of giving up just yet. I’m going to keep doing what I’ve been doing all along in trying to win you over because I think it’s worth it."

    scene mayaapt22
    with dissolve2

    m "..."
    s "You may have retracted what you said about not caring if the world were to end right now, but I think I may have inherited that thought."
    s "I’ll admit that I’m worried about hurting you, but I don’t care at all about what happens to me. "
    s "And, as much as I’d love to say I’m happy just being near you and that it’s fine if we stay like this...it won’t be enough. You’re way stronger than I am for being able to do something like that for so long."
    s "And you can be strong all the way up ‘til the end if you want. You can keep pretending you don’t want me while I continue to-"
    m "Can we go outside? "
    s "Now? Why? We’re in the middle of a discussion."
    m "Because if I have to sit here for one more minute and listen to you talk about how much you want me, I’m going to break you again."
    s "Then break me."

    scene mayaapt23
    with dissolve

    m "I’ll be on the balcony if you need me. We shouldn’t be inside right now. It’s not safe."

    play sound "slidedoor.mp3"

    s "Maya, come on-"

    "Maya heads out onto the balcony and-"

    play sound "static.mp3"
    scene o with flash
    scene worldlol with flash
    scene o with flash
    scene worldlol with flash
    scene mayaapt24 with flash
    stop sound
    play music "gentle.mp3"

    "And I follow her out there, because it’s not safe {i}anywhere.{/i}"
    "She rests her arms on the railing and I do the same, peering out at a landscape I’ve yet to observe in my short time here."
    "Powerlines cut through the night sky and decorate the colossal walls that keep us trapped, becoming less and less metaphorical by the day."
    "Despite how much I may want to, I don’t touch Maya."
    "If I did, I’m sure she’d be mine in a matter of seconds."
    "I’m also sure it would be worth whatever apocalyptic fallout results from it because who even {i}knows{/i} when the last time she layed with me was."
    "There’s no telling when it will happen next, nor if it ever {i}will{/i} if she has things her way...but, for the first time in quite a while, I actually have some hope."
    "Life is turning around for me."
    "{b}AND THERE IS NOTHING THAT COULD HAPPEN TO RUIN THAT.{/b}"

    m "So..."
    s "So."
    m "That was almost bad."
    s "Was it?"
    m "If there was any room for memories of {i}me{/i} in your head next to all of the space reserved for the Nakayamas, you’d know {i}exactly{/i} how bad that could have been."
    s "I suddenly wish there was more room in my head..."
    m "I’m skeptical as always, but...maybe there {i}will{/i} be if we keep on waiting. "
    m "If you remember your {i}name{/i}, there’s no telling what will come next. "
    m "And once it becomes a little clearer that your past with me is capable of being restored {i}and{/i} won’t destroy you in the process-"
    s "We can have hardcore sex on Ami’s bed?"
    m "We can have hardcore sex on {i}your{/i} bed. Ami’s bed is too loud."
    s "I’ll take it. Thank you for giving me something to look forward to."
    m "Are you sure that’s what you want, though? "
    s "To have hardcore sex with you? Yeah. I’m sure."
    m "To...{i}pursue{/i} me in general. It doesn’t scare you knowing that everything you’ve come to love could be stripped away?"
    s "..."
    m "Sensei?"
    s "The most scared I’ve been in recent memory was when I made it to the rooftop two resets ago and you weren’t there."
    s "I think I’m more worried about something like that happening again than whatever will come from the two of us touching."
    m "..."
    s "Are you afraid of that too?"
    m "..."
    s "..."
    m "I don’t want to die..."
    s "It’s not {i}dying.{/i} And I’ve already decided I’ll wait for you if something like that ever happens, so..."
    m "I wouldn’t wish that suffering on anyone. {i}Especially{/i} you."
    s "Can I have permission to fuck the other Mayas while I wait for you, though?"
    m "I take it back. You can suffer."
    s "It’s no fair that you got to have sex with some of my clones but I can’t have sex with yours."
    m "Can we not talk about the mistakes I made when I was sex-deprived and desperately missing you? I deserve at least a free pass or two for all the time I’ve spent here."
    s "Can we at least {i}kiss?{/i}"
    m "You and me? Or you and my clones?"
    s "You and me. I’m kissing your clones no matter what."
    m "I have no idea. "
    m "It would be nice if there was some sort of rulebook or instruction manual for this. "
    s "I {i}guess{/i} I can hold back until you’re okay with it then. Even if doing so infuriates me beyond belief."
    m "Oh, I believe it. And I’m sure there will be many moments in the future where I begin to question my own judgement as well. "
    s "Please inform me of them the moment they spring up."
    m "As if I’d just tell you when it is and isn’t okay to make a move on me."
    s "From what I’m gathering here, it’s basically just “not okay” for the indefinite future."
    m "That’s correct."
    m "{i}But...{/i}"
    s "But?"
    m "It {i}might{/i} be okay if you were to accidentally touch your lips to mine or something while I’m not paying attention."
    s "Woah, what’s that over there? Way off in the distance?"
    m "I am so guarded right now that you wouldn’t even be able to touch my hand if you tried."
    s "Damn. I thought I had you with that."
    m "Not even close."
    m "You have me in a number of other ways, though."
    m "You always have."
    s "How’d you wind up getting so attached to a guy like me anyway?"
    m "The same reason you wound up getting attached to me."
    s "That’s no fair. You know I can’t remember that."
    m "I know. That's why I said it."
    s "Maya-"
    m "Let’s just say we’re both pretty fucked up."
    s "I believe it. "
    m "..."
    s "..."
    s "Woah, what’s that over there?"
    m "It’s not happening. Give up."
    s "I’ll get you soon enough. Mark my words."
    m "They’re marked. Thank you for the advance notice."
    s "..."
    m "..."
    s "Hey..."
    s "Is it just me, or does the moon look...bigger than normal tonight?"

    scene mayaapt25
    with dissolve2

    m "Hm?"
    s "..."
    m "..."
    m "Huh..."
    m "It looks the same as always to me."

    scene black
    with dissolve2
    stop music fadeout 25.0

    "When we head back inside, Maya regains her appetite."
    "But I’m asked to sit halfway across the room while she demolishes both her bentos {i}and{/i} mine."
    "Nothing else happens and she leaves shortly after that."
    "I watch her as she puts her shoes back on...and as she turns to me to say goodbye, I take notice of a smile she forces away."
    "She pauses for a moment- and instead of telling me she loves me, she says this..."

    m "I don’t...not...feel the same way you said you did before or..."
    m "Yeah."
    m "Goodnight."

    "I go to sleep with a rare smile on my face."
    "It’s one I’ll never show you."
    "But she can see it whenever she wants."

    $ renpy.end_replay()
    $ mayadate45 = True
    $ maya_love += 100

    "{i}Maya’s affection has increased by 100!{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1

    if day < 7:
        $ day += 1
    elif day == 7:
        $ day = 1

    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
    if day == 2:
        hide monday onlayer date
        show tuesday onlayer date
    if day == 3:
        hide tuesday onlayer date
        show wednesday onlayer date
    if day == 4:
        hide wednesday onlayer date
        show thursday onlayer date
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date
    if day == 6:
        hide friday onlayer date
        show saturday onlayer date
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date

    scene sky
    with dissolve2

    "A new day begins..."

    if day <= 5:
        "But I have somewhere I need to be..."

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        jump afterschool
    else:
        "What do I want to do with it?"
        jump satmorningmenu

label mayaspecial45:
    scene rainwalkers1
    with dissolve2
    play music "ame.mp3"

    "This is rare."
    "Not the fact that I’m walking home with the three girls who I’d likely wind up dragging along with me to a desert island if I was forced to choose- but the fact that we’re surrounded by water."
    "Which, I guess, is not that dissimilar from actually being stuck on a desert island. Apart from the fact that the ocean is currently crashing down around us."
    "What I’m trying to say is that it’s raining."
    "I’m sorry I couldn’t put it any more eloquently — I’ve just gotten so accustomed to the fact that the rain doesn’t ever hit us that I’ve all but abandoned the idea of ever having to talk about it."
    "That said, we’re lucky Ayane is always prepared and had not one but {i}two{/i} umbrellas stashed away in her locker for emergency scenarios like this."
    "If the weather reports are accurate (Which they’re normally not), this won’t be the last time either."
    "It’s supposed to rain a lot more frequently in the coming days."
    "It makes sense, of course, what with our rainy season being all but devoid of actual {i}rain{/i} until now."
    "But life is changing."
    "I told you that recently, didn’t I?"
    "And with that change in life comes a change in the world because those two things are so connected at this point that one can not move without the other."
    "That doesn’t mean I have to like it. I honestly hate the feeling of my clothes getting wet."
    "I hate how they stick to my skin."
    "But-"
    "I hate the heat even more."
    "And so I will accept the precipitation in place of perspiration and walk forward into puddle after puddle, drenching my shoes and socks."
    "I could try to avoid them all, but there’s simply no point."
    "We can’t get off this island without getting wet."
    "And we can’t live normal lives without a little downpour every now and then."
    "Here’s to the rainy season."
    "And here’s to hoping it doesn’t all freeze just yet."

    a "I think I really have a chance, Ayane! I’m starting to get pretty good at this whole poetry thing!"
    ay "I believe in you, Ami! I knew your educational breakthrough was only a hop, skip, and a jump away! And, despite what many workforces would have you believe, poetry totally counts as “educational!”"
    a "I just hope Miss Watabe likes it. She’s a pretty harsh judge from what I hear. "
    a "I heard from Noriko a while ago that she graded this one girl’s essay so harshly that she started bawling her eyes out and ran out of class."
    m "Sensei, can I ask you a question?"
    s "I guess. It’s not like Ami and Ayane are paying any attention to us. "
    m "Then, would you mind explaining to me why I’m walking under {i}your{/i} umbrella?"
    s "B-"
    m "In as few words as possible, preferably. "
    s "Because Ayane said she wanted to walk with Ami."
    m "I know that. I was there when she said it. What I am asking is why you agreed."
    s "B-"
    m "In a way that doesn’t make you sound like a disgusting opportunist, preferably. "
    s "Can we just stay silent? Not talking to you seems like the easiest option in a situation like this."

    scene rainwalkers2
    with dissolve

    m "Was my direct questioning a little too harsh?"
    s "If you want to know why we were paired up, ask Ayane. I don’t know what to tell you."
    m "May I at least hold the umbrella so I can walk ahead of you in complete disregard for your well-being?"
    s "No. But if you want to run ahead without it, feel free."

    scene rainwalkers3
    with dissolve

    m "How unfortunate. It appears that since I can’t move ahead without running the risk of coming down with a cold, you and I are forced to stick together for the time being."
    m "Oh well. I suppose that it’s fine since there is no other option."
    s "..."

    "Is this just Maya’s weird, secret way of expressing how much she cares about me without...you know, saying {i}anything{/i} about how much she cares about me?"
    "Because it feels to me like she’s only asking these things right now to-"

    ay "Ami, what are you looking at?"

    "Hold on. No. I was narrating. You can’t just-"

    a "Look over there...in the middle of the road."

    scene rainwalkers4
    with dissolve

    "Ugh, fine. Since I’m apparently not allowed to talk about my thoughts anymore, I guess I’ll-"

    scene rainwalkers5
    with fade

    "Wait..."
    "Isn’t that-"

    a "Isn’t that Kaori?"

    "Can I not even get a thought out anymore?"

    a "What’s Kaori doing out in the street?"
    m "Better question — who is Kaori and why do we care?"
    ay "She works at the diner, doesn’t she?"
    a "She works everywhere. That’s like, her whole thing. She even helped me and Uta out at the maid cafe once."

    scene rainwalkers6
    with dissolve

    a "You’re friends with her...aren’t you, Sensei? Is this normal for Kaori? Or should we, like...do something about it?"
    s "Excellent question, Ami. "
    s "I have absolutely no idea. "
    s "But, if I were to rank everyone I know on their likelihood to stand out in the middle of the street during a storm, Kaori would probably come out on top."
    s "That said, we should probably still do something."
    ay "Uhh...Kaori? Are you okay?"
    k "..."

    scene rainwalkers7
    with dissolve

    m "She’s clearly insane. Let’s just leave."
    a "Kaori? Hello? Can you hear us?"
    k "..."
    s "..."
    s "Friend?"

    play sound "static.mp3"
    scene rainwalkers8
    with flash
    stop sound

    k "..."
    k "Waterfall?"
    a "Oh. I think that worked."

    scene rainwalkers9
    with dissolve

    k "Burgerfriend Friendman Burger? Innocently attractive cute maid girl who he abducted? What are you doing here?"
    ay "I actually like that nickname for you, Ami."
    s "Kaori, you were just...standing in the middle of the street during a storm. What’s going on?"
    k "I was doing what?"
    s "Reverse-sitting on an asphalt car-bed while letting clear sky-fluid bounce off of your...head flesh?"

    scene black
    with dissolve2

    k "Ahh! Why did you not just say so?! Do not be so needlessly acute triangle next time! "
    m "Okay, what the actual fuck is going on right now?"

    scene rainwalkers10
    with dissolve2

    k "It is nice to see you again, Smaller Friend! I enjoy the yellow plastic fluid-blocker your equally-yellow companion has! It is a great thing to have on days like today! This day!"
    ay "Do you...not have an umbrella, Kaori? "
    s "Better question, when did Maya get {i}my{/i} umbrella? "
    m "Secret."
    k "I do not possess what you refer to as the “umbrella.” I have never had a need for one until this day."
    a "Maybe...stay inside then? You’re going to get sick if you walk around in the rain, Kaori. "
    k "Then all I must do is remain still! The answer is obvious!"

    scene rainwalkers11
    with dissolve

    m "Where did you find this creature and what is wrong with it?"
    a "That won’t do either, Kaori! You shouldn’t be out here in the first place."
    s "Yeah, why {i}are{/i} you out here? Shouldn’t you be at work?"

    scene rainwalkers12
    with dissolve

    k "I am! But I am not! It is hard to explain!"
    k "Do you remember when you helped Aunt Yukiburger and me hand out paper advertisements for the Sara? It is like that!"
    s "You’re handing out fliers?"
    k "They are called birds! And no! Paper advertisements!"
    ay "You don’t...{i}have{/i} any paper advertisements, though."

    scene rainwalkers13
    with dissolve

    k "Then I will pat myself on the backwards stomach for a work well worked and return to base!"
    m "And which planet is your “base” on? "
    a "Where are you working today, Kaori? Do you want us to walk you back? You can hang out under the waterblocker with me and Ayane."

    scene rainwalkers14
    with dissolve

    k "That would be very helpful, Smaller Friend!"
    k "Today, I am working in a building full of fruit and cream! A bright building! Where creatures like you contort and mutate your face into happier versions of the same face!"
    s "Oh, so you do know the word “face” after all. I wish I knew that earlier."
    ay "Fruit and cream? Is it nearby?"
    k "The length of seven rock-throws!"
    ay "Seven rock-throws...I see, I see..."
    m "{i}Do you?{/i}"
    ay "The only place around here that matches that description, unless Kaori has the arm strength of a professional outfielder, would be that cafe we took Ami to for her birthday a while back."

    scene rainwalkers15
    with dissolve

    a "What birthday was that? I don’t remember that at all."
    ay "You don’t? Really? It should have been your-"
    k "Let us go! I will inform the manager that I did the job so she will give me another job! One with less fluids and more cream!"
    s "Both of those jobs sound pretty good to me."

    scene rainwalkers16
    with dissolve

    k "I understand your words! There are few things better than a mouth full of cream! "
    ay "{i}She’s got a point there.{/i}"

    "Ayane doesn’t say that, but I can tell she’s thinking it."

    s "It’s not far, right? Because if it’s only seven rock-throws away, we might as well wait out the rain there. Beats having to share umbrellas at least."
    a "Are you only saying that because you want to see Kaori with a mouth full of cream?"
    k "I can not cream myself until the day ends! I must wait until the customers are creamed first!"
    s "You heard her, Ami. You’re the one getting creamed, not Kaori. That should be fine, right?"

    scene rainwalkers17
    with dissolve

    a "Getting creamed {i}does{/i} sound tempting right now. Better than just staying wet, at least."
    ay "{i}I would also like to get creamed right now.{/i}"

    "Again, Ayane doesn’t say that. But she’s thinking it."

    m "Why is everyone just ignoring all of these blatant innuendos?"
    s "Why are you being such a buzzkill when there is now food involved? You love food."
    m "Because I don’t have any money and Ayane refuses to buy me anything unhealthy."
    ay "I will not stand idly by while you destroy your adorable-"
    s "Just agree and I’ll buy you whatever you want."

    scene rainwalkers18
    with dissolve

    m "What are we waiting for? Let’s go."
    a "Okay, Kaori! Take us back to your base and cream us all!"
    k "I understand! Prepare to be creamed, small child! "

    scene black
    with dissolve2

    "Kaori marches onward and the rest of us follow behind her."
    "Unfortunately though, there are no rocks around...so I am unable to discern just how much further we’ll need to walk."

    scene rainwalkers19
    with dissolve2

    "Fortunately, it winds up not being very far at all and, after a few blocks, the five of us wind up escaping the rain and finding refuge in a shop that smells a little too sweet for me."
    "I do have a vague recollection of coming here once or twice before, but these sorts of cafes have never really had much effect on-"

    k "Arrival!"

    "Okay, does no one care about my narration today?"

    k "Thank you for your sudden and wet appearance inside of my humble rectangle! Please hand to me your paper advertisement for a discounted rate on the creaming!"
    a "You didn’t give us any, Kaori. You were all out when we found you."
    k "Then only the Burger-man gets a discount for being my friend! I am sorry, Smaller Friend and blue-eyed companion. Your time will come another day!"
    ay "That’s fine. I was going to pay for Ami anyway. "

    scene rainwalkers20
    with dissolve

    a "You were? Why? I have money. You don’t have to do that."
    ay "Do you still do the couple’s discount here, Kaori? Smaller Friend and I are dating and we’d like the most private table you have."
    k "We do not have privacy wood for customers to eat off of, but we do support love in the form of financial benefit! "
    k "Reverse-stand wherever you like and I will be with you momentarily!"
    s "Guess that leaves-"

    scene rainwalkers21
    with dissolve

    s "And she sat down without me."
    k "Is something the matter Burger McBurger Friend McBurgerFriend McFriend Man Burger?"
    k "Are you sad that you will not be receiving financial benefits in the name of love? Because we have a loneliness special as well!"
    s "You’d think something like that would help, but really it just makes me feel even more alone."
    k "Well, go be alone at a rectangular wooden slab! Your large and handsome frame is blocking the doorway and will make it harder for me to cream the customers who walk in!"

    scene black
    with dissolve2

    s "Hah..."

    "........."
    "......"
    "..."

    scene rainwalkers22
    with dissolve2

    m "What are you doing? Why are you sitting here? I specifically sat here so I wouldn’t have to deal with you."
    s "Wasn’t I supposed to pay for you? That’s the only reason you came here in the first place, isn’t it?"
    m "I kind of hoped you would just walk across the cafe and hand me money when I got the check."
    s "What’s the problem? Why can't I sit here?"
    m "The problem is that {i}Ami{/i} is here too. And if she sees the two of us at a table together, she is going to get suspicious and it is going to make my life even more hellish than it already is."
    s "That’s not going to happen."
    m "That is absolutely going to happen."
    s "No, it’s fine. Look. Ayane is distracting her."

    scene rainwalkers23
    with fade

    ay "Are you excited to eat your cake, Ami?"
    a "I am! It looks super delicious! Thank you so much, Ayane!"
    ay "Great, great."
    ay "Now, tell me, what are your thoughts on the apocalypse?"
    a "..."

    scene rainwalkers24
    with dissolve

    a "What?"

    scene rainwalkers25
    with fade

    m "I really hope they’re not talking about what I think they’re talking about..."
    s "They’re almost certainly talking about what you think they’re talking about."

    scene rainwalkers26
    with dissolve

    m "Hah...she’s going to ruin everything, Sensei. I can feel it."
    s "You’ve felt a lot of things and only a few of them have wound up being true."
    m "{i}No...{/i}A few of them have wound up being {i}wrong.{/i} Need I remind you that nearly all of my predictions up until recently had been spot-on?"
    s "Or is that just what you were programmed to think?"

    scene rainwalkers27
    with dissolve

    m "You know, I really...{i}really{/i} wish Tsuneyo never mentioned something like that. Because you might be joking now, but that has stuck with me and I can’t get it out of my head."
    s "Just think about that time we almost kissed instead. I’m sure that’ll overwrite it."
    m "Yeah, with more earth-shattering loneliness and an even greater desire to brutally and violently make up for lost time in your bedroom."
    s "You know, I’ve waited a long time to hear you say things like that, but now that you {i}do{/i} say things like that, it’s just weird."
    m "You did this to yourself. If you’re going to make me suffer every single day of my life, the least I can do is make you suffer as well."
    s "Well, it’s working. So...keep at it, I guess."
    m "..."
    s "..."
    s "Maya?"

    scene rainwalkers28
    with dissolve

    m "God, I fucking hate this."
    k "Hello, Friend! I regret to inform you that there is no hot meat! But there is plenty of-"
    s "Cream. Yes, Kaori. I know."
    k "How would you like to be creamed?"
    s "Brutally and violently in my bedroom by a girl who likes watermelons a little too much."

    scene rainwalkers29
    with dissolve

    m "Die."
    k "Your words apart from “watermelon” do not register in my brain-space, but I will explain your characteristics to the manager and have them guess what you would like to consume based on that!"
    k "Is there anything else you require?"
    s "Not for me. Thanks, though."

    scene rainwalkers30
    with dissolve

    k "I understand! Please be patient for others must be creamed first!"
    m "Is there a menu I could-"

    scene rainwalkers31
    with dissolve

    m "...look at?"
    s "..."
    m "..."

    scene rainwalkers32
    with dissolve

    m "What just happened?"
    s "It looks like you were ignored."
    m "But...I’ve never been ignored in my life. I’m adorable. Can you see me? You can see how adorable I am, right?"
    s "I can see how humble you are."
    m "What do I do now?"
    s "Starve, I guess."
    m "Call her back over. She’s {i}your{/i} friend, isn’t she?"
    s "Ugh...fine."
    s "Kaori."

    scene rainwalkers33
    with dissolve

    k "Eleven!"
    s "That’s...nice. Aren’t you forgetting something, though?"

    scene rainwalkers34
    with dissolve

    k "The Queen of Spiders does not forget. She knows the answers to all things even before she asks."
    s "Then...why did you ask?..."
    m "I need a menu. Either that or a...recommendation or-"
    k "Friend, as much as I enjoy the feeling of my vision balls connecting with yours, I have customers to cream. So if you do not have something to ask for-"
    s "A...menu would be fine, Kaori. Thank you."

    scene rainwalkers35
    with dissolve

    k "Shiny, plastic-coated list of sustenance, coming right up! Prepare for another rectangle!"
    m "Wha-"

    scene rainwalkers36
    with dissolve

    m "..."
    s "..."
    m "I fucking hate your weird friend."
    s "Maybe you just have to speak her language."
    m "And make myself sound like a complete idiot? No thanks. You’ll order for me. And I’ll be having one of everything on the menu. I hope you’re happy."
    s "As long as you’re happy-"
    m "Don’t hit on me when I’m angry. Or hungry. Or ever."
    s "..."
    m "..."
    m "What? What’s that stupid fucking face for? What are you thinking?"
    s "I’m just wondering if hate sex would count toward potentially deleting me."
    m "It would."
    s "But-"
    m "Trust me."
    m "It would."

    scene black
    with dissolve2

    s "I guess I’ll just take your word for it..."

    "In the end, Maya never gets to communicate with our waitress."
    "But, to be fair, I think she’d have failed if she’d gotten a chance anyway."
    "Kaori isn’t exactly the easiest person to talk to, but...that’s kicked up a few notches when she won’t even acknowledge you."
    "Thankfully (For Maya, not my wallet), {i}I’m{/i} able to order on behalf of the bottomless pit and we all proceed to {b}HAVE A NORMAL, FUN MEAL BEFORE RETURNING HOME.{/b}"

    $ renpy.end_replay()
    $ mayaspecial45 = True
    $ maya_love += 1
    $ kaori_love += 1
    stop music

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "{i}it is waking up{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label sportswars5:
    play sound "static.mp3"
    scene mayaamisadroom1 with flash
    stop sound

    ya "{i}But her feelings are far more complicated than just “unwell.”{/i}"
    ya "{i}They are...{/i}"
    ya "{i}Suffocating...{/i}"

    play sound "knock.mp3"
    play music "lastdailysong.mp3"

    "For a week now, I’ve been wondering — what skills I need to fly."
    "If hope alone can grant me wings — if concern alone is fine."
    "But the problem with this dream of mine’s not the chance that I may die-"
    "It’s the fact that I might hurt you. "
    "It’s the chance that you might cry."

    play sound "knock.mp3"

    "Who raps upon my chamber door? Who crawls across these marble floors?"
    "Who scratches at my coffin’s lid and mocks the raven’s “nevermore?”"
    "I hear things, Boy. {s}I’m scared.{/s} I’m yours!"
    "But you're not here when I need you."
    "There's no glow to make me pure."

    play sound "knock.mp3"

    "They’re here again. I hear them. Those endless, violent knocks-"
    "It’s been three weeks since I’ve slept, I think — this dead bird never mocks."
    "But the blues and reds still fly, I think. I think the door’s unlocked."
    "I think I think I’m losing it. I think I think I’m lost."

    play sound "knock.mp3"

    "Arakiel’s silhouette — Azrael’s old cot>"
    "Daniel’s misbegotten snake — Etinsib Ziwa’s war/Nbat!"
    "Harmozel and Hofniel* What Gossamer forgot}"
    "I think my light is burning out."
    "I fear my mind will rot."

    m "{i}Ami?...Are you in there?{/i}"

    "..."

    m "{i}I’m coming in, okay?{/i}"

    play sound "dooropen.mp3"
    scene mayaamisadroom2
    with dissolve

    "{i}Maya Makinami entered the room.{/i}"
    "{i}It was the first time in months she’d done that. And she immediately noticed the complete absence of strawberry — an aroma she’d come to associate almost exclusively with the pinks and reds these walls held.{/i}"
    "{i}She glanced down at a bed she’d fallen asleep in time and time again, but what she saw there was unlike anything she’d ever seen on any of those fun-filled, sugary nights.{/i}"
    "{i}It was a body acting more like a statue — completely unmoving. And there was a moment where she feared her friend might have actually died and was just being hidden here.{/i}"
    "{i}Her life thus far was complicated, that much was certain. But not complicated to the point where stumbling across a corpse wouldn’t be the worst thing that ever happened to her.{/i}"
    "{i}Regardless, that was something she did not want to encounter today. For she loved the statue on the bed. She loved how it was more fragile than other notable statues.{/i}"
    "{i}It was much more frail than David, possessing a level of beauty somewhere between Rodina-Mat' Zovyot! and Venus de Milo- but she felt the urge to act as an engineer rather than a critic right now.{/i}"
    "{i}She observed the contours of the sculpture’s body. Let them soak into her mind and overwrite the recently-decayed image of them, now inaccurate in a multitude of ways.{/i}"
    "{i}She’d lost weight. Lost hair. Lost sanity. Lost faith. Lost everything because that’s what happens when you spend too long in the dark.{/i}"
    "{i}But the dark is precisely where some people should be.{/i}"

    play sound "static.mp3"
    scene mayaamisadroom3 with flash
    stop sound

    "{i}The dark is rather beautiful, you see.{/i}"
    "{i}And yes, it might take the untrained eye several minutes to become fully acclimated, but it promises a world unlike any other once you see what you’re meant to.{/i}"
    "{i}Do you see what you’re meant to?{/i}"
    "{i}Maya Makinami sees what she’s meant to.{/i} "
    "{i}She thinks of a way to repair the sculpture. How to restore it to its former beauty — and it was a beauty she was often entranced by, so she wanted to do that as soon as possible.{/i}"
    "{i}For, you see, there was one creature taking up the majority of her mind. There was one creature she preferred seeing over the others. But that didn’t mean her mind didn’t occasionally wander.{/i}"
    "{i}She’s a human after all. She’s not perfect by any means. She’s not {b}pure{/i} by any means. But she knows how to return love to those she ranks the highest.{/i}"
    "{i}And Ami Arakawa would always be her number two — regardless of who or what would have her rethink that.{/i}"

    m "Ami..."
    m "Are you awake?..."

    "{i}The two of them were alone in this house.{/i}"
    "{i}Regardless of who or what would have you rethink that.{/i}"

    a "No."
    m "You sound awake."
    a "I’m not awake."
    m "Are you thirsty?"
    a "..."
    m "Hungry?"
    a "..."
    m "Do you want me to leave you alone?"
    a "..."

    scene mayaamisadroom4
    with dissolve

    m "..."
    a "..."
    m "We’re having the Dorm Wars today. Well...{i}they’re{/i} having the Dorm Wars today."
    m "I’m supposed to be there too, but..."
    a "You should go...I’m fine."

    scene mayaamisadroom5
    with dissolve

    m "You don’t {i}look{/i} fine. You look sick. "
    a "I {i}am{/i} sick. Contagious too. So it would probably be best if you left or {i}you’ll{/i} wind up catching it as well."
    m "Is it deadly?"
    a "Very."

    scene mayaamisadroom6
    with dissolve

    m "Oh well. At least we’ll die together."
    a "... "
    m "Any idea how much longer you’ll be staying here? Should I be preparing for a life without you? Because, with the way Ayane’s been acting lately, I could use a friend who isn’t {i}completely{/i} insane."
    a "How...has Ayane been acting?"

    scene mayaamisadroom7
    with dissolve

    m "God, where do I even begin?"
    m "She keeps saying all this stuff about how I’m acting differently and how {i}my memories have been reset{/i} and I’m like, 99%% sure she’s going insane from a lack of Sensei."

    scene mayaamisadroom8
    with dissolve

    a "Huh..."
    m "And I’m pretty sure Makoto is in on it too, which is {i}super{/i} fucking weird because I didn’t even know the two of them talked to one another."
    a "Sounds like things have gotten pretty weird without me, huh?..."

    scene mayaamisadroom9
    with dissolve

    m "I mean, yeah. But they were getting pretty weird {i}with{/i} you too. Especially after that psychopathic rant you went on in the classroom about harvesting our organs or whatever."
    a "Heheh...yeah. I guess that {i}was{/i} pretty crazy in hindsight. "

    scene mayaamisadroom10
    with dissolve

    a "I kinda meant it, though."
    m "..."
    a "I’m tired of everyone using Sensei for their own personal gain. {i}You{/i} understand, don’t you? {i}You’d{/i} never do something like that, right?"
    m "Of course not. "
    a "So you support me?"
    m "As in...do I think it’s okay for you to reproduce with your uncle?"
    a "More or less."
    m "It is my personal belief that {i}no one{/i} should reproduce with {i}anyone{/i} because babies are a plague upon this land and should be purged from it entirely."
    a "That sounds like a cop-out answer to me."
    m "Yeah, well I find it hard to imagine me ever agreeing to the idea of a bunch of mini Senseis running around Kumon-mi. "
    a "What about a bunch of little Amis?"
    m "Better. Still chaotic, though. A bunch of mini {i}Mayas{/i} on the other hand..."
    a "Are you saying you want my uncle to breed you too?"

    scene mayaamisadroom11
    with dissolve

    m "What? No. I was just-"
    a "I’m just kidding..."
    a "But, if we’re going to keep talking...would you mind coming a little closer? My voice is really weak right now...and having you so far away is making me sad."

    scene mayaamisadroom12
    with dissolve

    m "Of course..."

    scene black
    with dissolve2

    m "I was just about to come over there anyway..."

    "........."
    "......"
    "..."

    scene mayaamisadroom13
    with dissolve2

    m "So...what inspired the new haircut?"
    a "Let’s just say I was having a really bad day."
    m "I kind of like it. It goes well with your new “I don’t mind killing my classmates if they talk to my uncle” attitude. Which, I guess isn’t {i}totally{/i} new. But definitely more open than normal."
    a "You’re a little more open than normal too."

    scene mayaamisadroom14
    with dissolve

    m "Am I? How?"
    a "I don’t know. Maybe your memories really {i}were{/i} reset after all and you just aren’t aware of it?"

    scene mayaamisadroom15
    with dissolve

    m "Please don’t mess with me like that. I’ve already had to tell off two people today and I was hoping I’d somehow find salvation here. "
    a "But you never expected to find that salvation in me...right?"

    scene mayaamisadroom16
    with dissolve

    m "Huh?"
    a "You’re here for Sensei..."
    m "That’s...not true. If I was here for Sensei, I wouldn’t have bothered-"
    a "Yes you would have. You probably just want to see if {i}I{/i} know where he is. Which, I’m sorry to break it to you...but I don’t."
    m "Ami...I didn’t come all the way here just to-"

    scene mayaamisadroom17
    with dissolve

    a "Maya...it’s {i}okay.{/i} You’re my best friend. If I’m going to lose to anyone, I’d prefer losing to you."

    scene mayaamisadroom18
    with dissolve

    m "Where is this coming from? When have I {i}ever{/i} expressed {i}any{/i} amount of interest in your uncle? Where did you even {i}get{/i} that idea?"
    a "You’re so pretty, Maya."
    m "Yeah, I know. But what do you have to gain from pointing that out now?"
    a "Nothing in particular, I guess."
    a "I’ve just missed you."

    scene mayaamisadroom19
    with dissolve

    m "I’ve missed you too. Which is why I’d really like for you to stop being insane and come back to school ASAP so I won’t feel like a fucking alien anymore."
    a "I have bad news for you, Maya. I don’t think I’m ever going to stop being {i}insane.{/i} And I {i}really{/i} don’t think anyone from class is ever going to look at me the same again even if I do."
    m "That’s not true. Like half of our class has some sort of mental illness. I’m sure they’d be more than willing to accept you again if you just apologize and...don’t steal their insides."
    a "Why should I have to apologize for just being myself?"
    m "You don’t {i}have{/i} to. But at least you can get people back on your side by faking it."
    a "You’re starting to sound like Sensei."

    scene mayaamisadroom20
    with dissolve

    m "Nah. If anything, he’s probably just ripping off my personality after realizing how much better than him I am."
    a "Watch it. I love you, but I’ll always love {i}him{/i} more."
    m "You can love him more and still acknowledge that I’m a superior being. Don’t worry, I won’t tell. "

    scene mayaamisadroom21
    with dissolve

    a "You’re definitely softer..."
    m "Yeah?"
    a "You smell nicer too..."
    m "Please, continue. It’s really nice hearing compliments after being told for months that I’m broken."
    a "I could do this forever..."
    m "You’d dare confine me to the same prison as you?"
    a "I think you might like it here. We wouldn’t have to worry about anyone misunderstanding us anymore."
    a "But also....seeing nothing but {i}each other{/i} might cloud our minds."
    m "How so?"
    a "Who knows?"
    a "Maybe we’d fall in {i}love?{/i}"
    m "Maybe we already {i}have?{/i}"

    scene mayaamisadroom22
    with dissolve

    a "Bonk."
    m "Geh...is this really necessary?"
    a "I will not let you convert me when I’m at my most vulnerable, you heathen."

    scene mayaamisadroom23
    with dissolve

    a "But I {i}will{/i} move over so you can lie with me..."

    scene black
    with dissolve2

    a "Just like old times..."

    "........."
    "......"
    "..."

    scene mayaamisadroom24
    with dissolve2

    m "Even like this, you’re still the most adorable girl I know."
    a "You’re only saying that because I’ll steal your organs if you don’t."
    m "Obviously. I have to stay on your good side, don’t I? And what better way to do that than by peppering you with compliments until you can’t bring yourself to hate me?"

    scene mayaamisadroom25
    with dissolve

    a "I’ll never hate you, Maya. Not even at my worst."
    m "If this isn’t your worst, I’m kind of worried about what {i}is.{/i}"

    scene mayaamisadroom26
    with dissolve

    a "I’ll never understand you either, though."
    m "What do you mean?"
    a "I mean I don’t get why you feel the need to hide everything from me. You trust me, don’t you?"
    m "More than anyone."
    a "Just saying “more than anyone” doesn’t confirm you actually {i}trust{/i} me, though. For all I know, you’re just {i}closer{/i} to trusting me than anyone else. And that doesn’t mean much, unfortunately."
    m "Well...how can I prove that I trust you?"
    a "Tell me a secret."
    m "What kind of secret?"
    a "Like...who do you have a crush on?"
    m "Nobody. No one is worthy of me."
    a "You’re lying again. You don’t trust me at all."
    m "If you want to play that game, how am I supposed to know {i}you{/i} trust {i}me?{/i}"
    a "The same way. I’ll tell you a secret."
    m "What kind of secret?"
    a "That depends on what you want to know."
    m "Well, I’m already {i}well{/i} aware of who you have a crush on, so...why not tell me what you really think of me?"
    a "What I really think?"
    m "Yeah. You’ve been insinuating all sorts of stuff today and I feel like now’s as good a time as any to get anything you might want to say off your chest."
    a "Are you sure that’s what you want to know?"
    m "Positive."
    a "Then..."
    a "I think you like masks a little too much."

    scene mayaamisadroom27
    with dissolve

    m "Masks? Like...my collection?"
    a "Your everything."
    a "In fact, I don’t think there’s been a single moment throughout our entire relationship where you haven’t been wearing one. "
    a "And that sucks, since I feel like you’d still be really cute without them."
    m "What are you saying?..."
    a "That you’re a liar."
    a "That you’re hiding things from me because there’s something {i}else{/i} you’d choose over me if you were ever forced to. And that’s fine."
    a "There’s someone {i}I’d{/i} choose over you as well. But at least I’m honest about it."

    scene mayaamisadroom28
    with dissolve

    m "There’s no one like that. "
    a "Liar, liar, pants on fire. Sitting on a telephone wire."
    m "I mean it. There’s really no one who-"
    a "Then kiss me."

    scene mayaamisadroom29
    with dissolve2

    m "What?..."
    a "If you’re not already in love with somebody, you shouldn’t have any issue with kissing me. Right?"
    m "I...don’t. But you wouldn’t want me to do that."

    scene mayaamisadroom30
    with dissolve

    a "I don’t mind. I’m extremely vulnerable right now, so anything {i}you{/i} do has nothing to do with me. Plus, I’ve already kissed Ayane once before. Might as well kiss you too."
    m "When the fuck did you kiss Ayane?"
    a "Christmas. But you probably don’t remember it since your memories went poof."

    scene mayaamisadroom31
    with dissolve

    m "Ami, seriously. Stop fucking with me."
    a "I’m {i}not{/i} fucking with you. I just know you’re hiding your true feelings from me and that you won’t do anything because you’re so “in love” with that other person. But still, you won’t tell me who it is."
    m "Because there’s no one like that. Really."
    a "Really?"
    m "Really."
    a "Really really?"

    scene mayaamisadroom32
    with dissolve

    m "Really really."
    a "So you haven’t been having sex with my uncle behind my back?"
    m "I would never."
    a "And you didn’t come here today to have sex with him?"
    m "Absolutely not."
    a "You promise?"
    m "I promise."
    a "What will you let me do to you if I find out you’re lying?"
    m "Anything you want."
    a "Anything?"
    m "Anything anything. "

    scene mayaamisadroom33
    with dissolve

    a "Hm."
    a "Okay."
    m "Okay?"
    a "Yeah. That’s the kind of promise I can get behind. And the exact type of loyalty I want out of a best friend."
    m "Then...you trust me?"

    scene mayaamisadroom34
    with dissolve2

    a "More than anyone."

    scene black
    with dissolve2
    stop music fadeout 15.0

    a "Sensei’s probably at the shrine."
    m "What?..."
    a "He’s been having a tough time lately."
    a "He probably went there to pray."
    m "Why are you-"
    a "Mm...Sorry, Maya. I’m feeling really tired all of a sudden. Do you mind if I take a nap?"
    m "What?...I...uhh...yeah."
    m "Yeah, that’s...I can go."
    a "Thanks...I really appreciate it."
    a "Being “insane” is super exhausting. And so {i}loud{/i} too. "
    m "Loud?..."
    a "You wouldn’t get it."
    a "You’ve never hurt someone before."

    "{i}Maya Makinami has gained that status effect [[PARANOID]!{/i}"
    "{i}You two have so much in common!{/i}"

    $ renpy.end_replay()
    $ sportswars5 = True

    jump sportswars6

label sportswars10:
    play sound "static.mp3"
    scene black with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene mayashrinemad1 with flash
    stop sound
    play music "shrinesung.mp3"

    "Cicada songs and lemon drops — a shiny coin for choco-pops."
    "A puddle near that old oak tree — the things that you would do to me."
    "Play make-believe. Play hide and seek. Play hopscotch during Golden Week."
    "That hamster wheel we bought last year — a picture book of grazing deer."
    "And a pile of rocks that does naught but make me wish that I was home."
    "With tickle-fights and bug-filled nets — we’d stare up at that spring sunset."
    "Think “This is great!” or “Wonderful!” or “Splendid view!” or “Colorful!”"
    "Or “I think I’m sad” or “My head still hurts” or “I’m really sad” or “My stomach hurts.”"
    "We used to think so many things. We had so many songs to sing."
    "But now we rarely open our mouths because our teeth keep dripping onto our candy bars."
    "Such better days, I miss our youth! I miss all of my time with you!"
    "I miss falling down. Miss bandaged knees. Miss fireflies and centipedes."
    "Miss the way you looked when you’d look at me. Miss the way I looked when I couldn’t see."
    "I can do that now. All the light’s grown in. But my youth is gone, I’m spread too thin."
    "And I keep seeing things that I know aren’t actually there but they {i}feel{/i} like they’re there and I’ve begun to pull my hair out."
    "Cherry-scented soap and pine — a silly tune to pass the time."
    "A paddleboat through River Styx — a skeleton! A house with bricks!"
    "A knife wound in your upper thigh — I’ll press down hard so you won’t cry."
    "It’s soup again. It’s dinner time. I’ll hold your hand if you hold mine."
    "I don’t know how much longer I can keep having these dreams of our youth without sweetening my midnight tea with arsenic."
    "Some nights I think it would make them last forever."
    "Some nights I think I’m being watched."
    "- Girl"

    "{i}Something approaches.{/i}"

    scene mayashrinemad2
    with pixellate

    wil "I am Wilford Blackhole Hands."
    s "Okay."

    play sound "slap.mp3"
    with hpunch

    "Wilford slaps me across the face."

    s "Ouch. Why would you do that?"

    play sound "slap.mp3"
    with hpunch

    "He does it again."

    s "Hey. Stop that."
    wil "If you take three steps back, you’ll be out of my reach and I will not be able to hit you anymore."

    "I do as he says and take three steps back."

    with hpunch

    "He attempts to slap me again, but misses."
    "It appears he wasn’t lying to me. I think that I can trust him."

    s "What are you doing at the shrine, Wilford Blackhole Hands?"
    wil "Looking for you. Your students were almost eaten by alligators today while you were taking a piss in a somewhat secluded outhouse."
    s "I’m trying to earn a new nickname and have to be careful not to let any more accidents happen."
    wil "Accidents will always happen so long as you’re around. You should leave this place forever."
    s "Well, that’s certainly rude, Wilford Blackhole Hands. Why would you come all the way over here just to tell me that?"
    wil "I also came here to pray."
    s "To which god do you direct your prayers?"
    wil "Necalli, God of Knives. I’m just three badges away from earning my golden scepter."
    s "Well, I wish you the best of luck. We all know how tough it can be moving through the system of more modern religions."
    wil "When I earn my scepter, my reach will be extended and I will be able to slap you from further away."
    s "Why are you so intent on hitting me? I’ve done nothing to harm you."

    with hpunch

    "Wilford swings his scepterless arms again, but I am safe."

    wil "I do not bite my thumb at you, but at the fallout of your actions and how they have impacted my vacation schedule."
    s "I never meant to impact anybody’s vacation schedule. I’m just having a tough go of it right now."
    wil "This never would have happened if you had only been stronger."
    s "I know."
    wil "This never would have happened if you did not pretend to be a good man."
    s "I never did."
    wil "But you thought it. And sometimes, our thoughts are all that matter."
    s "Like when you want to buy someone a present but you can’t so you just tell them about the present you wanted to buy them and hope they say it’s okay?"
    wil "That isn’t very far off. But still, I do not like you."

    "The half-translucent miscarriage inside of Wilford Blackhole Hands’ black hole stomach begin to pulsate and change inside. It looks like it wants to speak as well."

    s "I think your baby wants a word."
    wil "It just had ten of them for breakfast. It’s time for baby’s burp. But my arms don’t bend the way they should, which is why I have developed this convenient black hole in my stomach."
    s "Will the baby stay there forever?"
    wil "It will pop out when it’s ripe."
    s "Have you chosen a name yet?"
    wil "I have chosen the name [whatyousaid]."
    s "That sounds kind of familiar."

    with hpunch

    wil "Hi-yah."
    s "Please stop trying to hit me. You are interrupting my sadness."
    wil "This place will never cure your sadness. It will only make it worse."
    s "I know. But sometimes, I deserve to be sad. I’m sure you agree."

    with hpunch

    wil "Hi-yah."
    s "Wilford, stop."
    wil "The longer this conversation continues, the more desperately I want to tear you to pieces."
    s "Meanwhile, I just want it to end so I can go back to aimlessly wandering around in hopes of being fixed by some kind of miraculous human-glue."
    wil "This is not aimless. This was a concerted effort to find someone."
    s "You’re right. It was."

    with hpunch

    wil "Hi-yah."
    s "Wilford."

    with hpunch

    wil "Engarde."
    s "That’s for fencing I think."
    wil "Your mother was a fence."
    s "No, my mother was a real human female."

    stop music
    play sound "slap.mp3"
    with hpunch

    "Wilford’s black hole-less black hole hands grow three steps and connect with my cheek."

    play sound "static.mp3"
    scene mayashrinemad3 with flash
    stop sound
    play music "undersea.mp3"

    "Or maybe he was never here in the first place."

    s "Ah-"
    m "Hi! Remember me?!"

    play sound "static.mp3"
    scene mayashrinemad4 with flash
    scene mayashrinemad5 with flash
    scene mayashrinemad4 with flash
    scene mayashrinemad5 with flash
    scene mayashrinemad6 with flash
    scene mayashrinemad5 with flash
    scene mayashrinemad6 with flash
    scene mayashrinemad7 with flash
    scene mayashrinemad6 with flash
    scene mayashrinemad7 with flash
    scene mayashrinemad4 with flash
    scene mayashrinemad3 with flash
    stop sound

    "No..."

    s "..."
    m "Are you gonna say {i}anything?{/i} Or are you just going to stand there and act all fucking scared and useless?"
    m "Because I was {i}fine{/i} with that when it was temporary. But now that you’re apparently wandering around the fucking city again and have made {i}no{/i} effort to contact me, I’m not sure {i}what{/i} to think."
    m "In fact, I’m not sure what any of this is about in the first place because there’s nothing I can even {i}think{/i} of that would mess you up as badly as you’ve apparently {i}been{/i} messed up."
    m "So either talk to me like a fucking {i}man{/i} or tell me to go fuck myself because I am {i}not{/i} Noriko and I am {i}not{/i} going to just deal with this bullshit for the rest of my life."

    play sound "static.mp3"
    scene mayashrinemad8 with flash
    stop sound

    m "And wipe that pathetic fucking look off of your face! {i}I’m{/i} the one who should look like that! Not you!"
    s "What are you doing here?..."
    m "What am {i}I{/i} doing here?! I {i}work{/i} here! And you haven’t set {i}foot{/i} here or {i}anywhere{/i} else I go in months! It’s like you’re {i}trying{/i} to avoid me! I’ve done literally nothing!"
    m "And now fucking {i}Ami{/i} thinks something is going on with us as well, so thanks for making that a thing I have to deal with! Appreciate it!"
    s "You should be in school..."
    m "I should be in- are there hidden cameras around here or something? Is somebody going to pop out and tell me this is part of some kind of comedy special?"
    m "Because, if not, that is the stupidest fucking thing you could have said after ghosting me for {i}months,{/i} Sensei! MONTHS!"

    play sound "static.mp3"
    scene mayashrinemad9 with flash
    stop sound

    m "Do you have {i}any{/i} idea what’s been going through my head all this time?! {i}Any?{/i}"
    m "Because, if you know me well enough- and I’m {i}pretty{/i} fucking sure you do, you’d probably understand just how pissed off I’d have to be to come looking for you, right? Right?!"
    s "..."

    scene mayashrinemad10
    with dissolve

    m "Are you just {i}bored{/i} of me now or something? Cause you sure picked a hell of a way to break that to me if that’s what’s going on here."
    m "And if it’s not, which I highly doubt it is in the first place, you should probably get to talking. Because it’s not a good look to let a teenage girl fucking scream at you in public while you just stand there."
    m "In fact, it’s not good for us to even be {i}seen{/i} in public. Which is why I’ve done {i}my{/i} job to a fucking {i}T{/i} while {i}you’ve{/i} done jack shit!"
    m "How long were you going to make me wait?! {i}Why{/i} were you making me wait?! And why won’t you fucking say anything?!"
    s "You’re not her..."
    m "What do you mean I’m not “her?” And which “her” are you talking about in the first place since we agreed not to talk about {i}either{/i} of them?"
    s "You’re not Maya..."
    s "You’re a meat puppet."
    m "..."
    s "..."

    scene mayashrinemad11
    with dissolve

    m "Okay, where are the cameras?"

    play sound "static.mp3"
    scene mayashrinemad12 with flash
    stop sound

    s "There are no cameras."
    m "Oh, there better be fucking cameras. Because you did {i}not{/i} just call me a “meat puppet” in the middle of an argument about you straight up disappearing on me."

    scene mayashrinemad13
    with dissolve

    m "You want to call me that while we’re fucking? Cool. Fine. Kinda weird, but still fine. Now, though? Are you an idiot? Did Ami scoop some of your brains out mid-coma? What the fuck, Sensei?"
    m "As a matter of fact, what did you {i}do{/i} to her in the first place? What happened to her hair? Why is {i}she{/i} suddenly bed-ridden now?"
    m "Is there some super secret Arakawa family disease that causes all of you to just stop living at the most tragic and dramatic times possible? Because if so, condolences. But also, maybe {i}tell me that?{/i}"
    s "I shouldn’t see you right now...I don’t {i}want{/i} to see you right now..."

    scene mayashrinemad14
    with dissolve

    m "Well, then what the fuck is {i}this?!{/i} Because you’re sure as hell not here to {i}pray!{/i} So either you {i}wanted{/i} to see me, or you’re looking for some other shrine maiden to fuck! Which is it?!"
    s "Neither..."

    scene mayashrinemad15
    with dissolve

    m "Uhhhhhhhhhh no. Answer not accepted."
    m "It’s one or the other. Either you want to fuck {i}me,{/i} or you want to fuck someone who isn’t as {i}cute{/i} as me. Which would be dumb. And you’re smarter than that. Which means you are here for me."

    scene mayashrinemad16
    with dissolve

    m "And you should be! Just, without the whole part that separated us for months while you jerked off into a sock, staring at the nudes of me on your computer."
    s "I’m not going to do this."
    m "Oh, you’re going to do this. And then, you’re going to drag me into an alleyway and have violent, angry makeup sex with me as penance."
    m "And I work for god, so that means you have to listen to me or you're going to {i}hell.{/i}"

    scene mayashrinemad17
    with dissolve

    m "Then, after that, all will be good again! And we can go back to never confronting one another about any of our problems in order to effectively maintain a healthy relationship! Just like we wanted!"
    s "This isn’t what I want..."

    scene mayashrinemad18
    with dissolve

    m "See this little circle thing right there?"

    scene mayashrinemad19
    with dissolve

    m "Pretend that’s my vagina. And this finger I’m holding up? That’s your penis!"

    scene mayashrinemad20
    with dissolve

    m "In half an hour, this better be us or I am going to fucking drag you into an alleyway myself."

    play sound "static.mp3"
    scene mayashrinemad21 with flash
    stop sound

    s "Can you please just leave me alone?..."
    m "No! It’s been {i}months!{/i} And we’ve been together for {i}years!{/i} If you’re going to treat me like this, you have to at least explain yourself so I’m not stuck {i}thinking!{/i} I {i}hate{/i} thinking!"
    m "There’s so much shit I’m confused about because {i}you{/i} decided to go into hiding out of nowhere and leave me in the dark!"
    m "Which, again, would have been totally cool if you gave me a fucking night-light or something instead of locking the door without even saying goodnight!"

    scene mayashrinemad22
    with fade
    stop music fadeout 15.0

    m "This is {i}not{/i} how we do things. We don’t fight."
    m "We fuck and we cuddle and we kiss and we part. That’s how it’s always been. And that’s how it {i}should{/i} be because that’s what we {i}want.{/i}"
    m "So, yeah. This whole situation has left me pretty fucking agitated because I don’t understand why, all of a sudden, it’s like you’re fucking {i}afraid{/i} of me. What did I do?"
    s "Nothing."
    s "I’ve just never met you before."
    m "What the fuck does that even-"
    s "Please..."
    s "Just leave me alone."

    scene mayashrinemad23
    with dissolve

    m "Oh, yeah! Just walk away! That’ll work!"

    scene mayashrinemad24
    with dissolve

    m "{i}It’s not like I have fucking legs or anything!{/i}"

    "Springing forward, summer glow — autumn’s kiss in winter snow."
    "The paths we take, the shoes we wear — those tattered soles in grave despair."
    "I once felt death was make-believe. I once felt love, then watched it leave."
    "Now floorboards creak and call for me — but you won’t speak nor talk to me."
    "And that’s why I’ll never sleep alone."
    "We’re closer than you know, Boy."
    "This house is not your home."

    $ renpy.end_replay()
    $ maya_love -= 1
    $ sportswars10 = True

    "{i}Maya’s affection decreased to [maya_love]!{/i}"

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Back at school...{/i}"

    jump sportswars11

label sportswars14:
    scene mayachasing1
    with dissolve2

    m "Hey! Asshole! When I said I had legs, I didn’t mean it was okay for you to make me wear them down until there’s nothing left! "
    m "Just how long are you planning on keeping this up for?! How many more miles do we need to walk until you realize how much of a coward you’re being right now?!"
    s "You can turn around and leave whenever you want."
    m "And give you the satisfaction of escaping me and thinking that {i}this{/i} is something you can run from too?! Fuck that! This is a problem {i}you{/i} created! And I’m {i}still{/i} polite enough to try and fix it!"
    s "Go home."
    m "I don’t {i}have{/i} a home!"
    s "You have the dorm, don’t you? And with Ami gone, you’ve got the room all to yourself. I’d be excited if I were you."

    scene mayachasing2
    with dissolve

    m "Oh, yeah! Nothing says “exciting” like spending months and months alone in a room and waiting for someone to come visit! That always works out great for me! Just, here’s the thing-"

    scene mayachasing1
    with dissolve

    m "No one fucking visits me anymore! "
    m "Well...no one except Ayane. But I’m starting to think the actual Ayane was abducted by aliens and replaced with a well-made clone who is now attempting to probe me for information. And not in the good way either!"

    play sound "static.mp3"
    scene mayachasing3 with flash
    stop sound

    s "Just tell me what you want, please. What can I do to make you leave me alone?"
    m "I’ve been telling you what I want since the moment I had to slap your sorry ass out of another blackout at the shrine! I want an {i}explanation!{/i}"
    m "You don’t do this to me! I’m the exception! {i}I’m{/i} the one who’s special to you! But now there’s all this shit with Noriko and- since when the {i}fuck{/i} are you talking to Niki again?! Is {i}that{/i} what this is about?!"
    m "Are you trying to disappear on {i}me{/i} now?! After all I’ve done for you?! After all we’ve done {i}together?!{/i}"
    m "Is this a hobby of yours?! Making one girl fall for you just to scramble to a different one the second shit gets {i}too hard{/i}?! Did Ami remove your backbone while you were unconscious or something???"
    s "If I tell you it’s because of Niki, will that be enough to make you leave?"

    play sound "static.mp3"
    scene mayachasing4 with flash
    stop sound

    m "D..."
    m "Don’t even joke about that..."
    m "You {i}know{/i} how I feel about her. And we agreed that we wouldn’t-"
    s "See, that’s the problem. I’ve never {i}agreed{/i} to anything with you. "
    m "Sensei. {i}Come on.{/i} You know that’s not true."
    s "Maybe not from your perspective. But from mine, it seems like {i}you’re{/i} the one who was abducted by aliens and replaced with a well-made clone."
    s "So well-made, in fact, that I can’t even look at you without being overcome by every single emotion known to man."
    m "With all due respect, I have a hard time believing you can feel more than a maximum of three emotions. Let alone all of them at once."
    m "But given that those are the same three emotions {i}I{/i} am able to have, I can empathize with where you’re coming from and will not think less of you for how much you want to strangle, embrace, and fuck me right now."
    s "Go home."
    m "Take me to {i}yours.{/i}"
    m "I have no idea what all of this bullshit Clone-yane has got you on is, what with me “not being the same Maya” or whatever the fuck, but I {i}am.{/i} I am {i}me.{/i} Nothing has changed."
    s "Everything has changed. But you’re the last person I want to talk to about it. And you need to understand that because just being around you is making this so much harder than it already is."

    play sound "static.mp3"
    scene mayachasing3 with flash
    stop sound

    m "Have you thought for a second that maybe it’s only hard in the first place because you {i}want{/i} it to be that way? It’s not like you’ve never intentionally torn your life to shreds before, Sensei."
    m "But that’s why I exist. I’m here to pick up those pieces and put you back together so that you can do the same thing for me when {i}I{/i} decide to act all suicidal for months on end."
    m "That’s how the cycle works. That’s the system we’ve created. "
    m "You break, I fix. I break, you fix. Then, we fill the radio silence with sex and our shitty idea of what “affection” means until we’re too tired to keep our eyes open and fall asleep next to one another."
    m "Only metaphorically though. Because Ami’s gotten way too close to finding us in bed before and, with this suddenly heightened suspicion of hers, I’m not about to take any chances on-"

    scene mayachasing5
    with dissolve

    s "What part of “leave” don’t you understand?!"

    play sound "static.mp3"
    scene mayachasing6 with flash
    stop sound

    m "The “leave” part!"
    s "That’s the whole thing!"
    m "Yeah! And it’s a thing {i}I’ve{/i} never had to deal with before because you’ve always wanted me around! And now that you either don’t or are {i}pretending{/i} to not want me, I’m fucking confused!"
    s "Well, I’d be confused too if I suddenly woke up in a world that was entirely different from what I was used to."

    scene mayachasing7
    with dissolve

    m "Oh my god. This shit again? Really?"
    s "That happened to me once, you know. Maybe more than once. "
    s "But even with how confused and how lost I was navigating a brand new world, there was a light there- guiding me along. Pissing me off and annoying me every step of the way."
    m "I feel like it would have been the other way around. But please, do proceed with your maniacal ramblings about alternate universes and whatever version of me you allegedly liked screwing the most."
    s "The Maya {i}I{/i} know would never chase after me like this. She was far too jaded and far too busy worrying about other things. {i}Bigger{/i} things."

    scene mayachasing8
    with dissolve

    s "She never gave a shit about how I felt or how I acted."
    s "Or, at least that’s how she seemed on the surface. I’m sure those things got to her internally if the way we felt at the end was at all indicative of her feelings on the way there."
    s "But that was just the thing. "
    s "It was so hard to {i}figure out{/i} what she was feeling. And now you’re here wearing your heart on your sleeve and chasing after me when we both know I’m not worth it."
    m "Sensei, I’m only chasing after you because I’ve run out of options. And yeah, it’s a bit uncharacteristic, but I have a feeling you’d do the same for me if you ever had to."

    play sound "static.mp3"
    scene memories1 with flash
    scene memories17 with flash
    scene memories23 with flash
    scene mayachasing3 with flash
    stop sound

    s "..."
    m "Besides, what does being {i}worth it{/i} even mean? We’re both all sorts of fucked up and, in the grand scheme of things, I can’t imagine anyone else ever finding us {i}worth{/i} it in the first place."
    s "My Maya was a lot more conceited as well."
    m "Oh, don’t get me wrong. I am a fucking {i}catch.{/i} But only on the outside."

    play sound "static.mp3"
    scene mayachasing9 with flash
    stop sound

    m "In {i}here,{/i} I’m just as bad as you. I only give a shit about two people- and I’ve lied to one of them more times than I can even count. "
    m "I’m explosive. Sensitive. And, despite everything happening right now, I {i}hate{/i} confrontation. Hell, I’m probably even emotionally abusive at times. "
    m "But you were the one who helped me understand that it’s {i}okay{/i} to be imperfect. That, so long as we can figure out a way to function out here, it doesn’t {i}matter{/i} who we really are."
    m "Are you giving up on that? Are you so tired of camouflaging yourself that you’re fine with just holing up in your bedroom and letting Ami spoon-feed you until you die of old age and lack of exercise?"
    s "It’s not that I’m {i}giving up.{/i} It’s that I’ve already lost everything that gave me a reason to go on in the first place."
    m "But you {i}haven’t!{/i} I’m right here! You just have to turn around and see me for who I am now rather than who I {i}was{/i} in whatever prolonged delusion apparently stripped me from your mind."
    s "Oh, right. That’s another thing. "
    m "What’s another thing? What are you talking about now?"
    s "See, you probably don’t know this yet on account of you being Kumon-mi’s latest teenage newborn, but my memory’s been essentially erased."
    m "What? What’s that supposed to mean?"
    s "It means that the only thing I really know about “our” past together is the fact that there was a past at all. And every other memory I made along the way is something you’ve yet to experience."
    m "Quit fucking with me, Sensei. Memories don’t just {i}disappear{/i} like that out of nowhere. And using that as an excuse to break things off is cowardly even for you."
    s "This isn’t the world you’re familiar with, {i}Maya.{/i}"
    s "It might {i}seem{/i} like it is. But somewhere along the line, you got wrapped up in something terrible and confusing, then spat out back at the beginning as if it never happened at all."
    s "And I’m happy for you because it means you won’t have to suffer anymore. That’s where I come in."
    s "I’ve gotta give kudos to you, though. Well, the {i}you{/i} that isn’t here anymore, I mean. "
    s "Because if experiencing this reunion {i}one time{/i} is enough to make me want to bite my tongue off, I can only imagine how it felt for her."
    m "Sensei...I’ve got {i}no{/i} fucking clue what all of this “something terrible” or “fake amnesia” shit is about, but if hearing you out will stop you from running, then fuck it. I’ll listen. "
    m "It’s one thing to have Ayane and, to a lesser extent, Makoto tormenting me about this on a weekly basis. But I trust you way more than I trust both of them."

    play sound "static.mp3"
    scene mayachasing3 with flash
    stop sound

    m "But I also want you to know that I’m not just going to go along with any of this because, even if you {i}are{/i} being sincere and your perception of the lives we’ve lived has been somehow mutilated, it’s not {i}real.{/i}"
    m "{i}I{/i} am Maya Makinami. {i}I{/i} am the best and worst secret you have ever kept. And {i}I{/i} am the type of girl who will chase you down if I have to because not even a million time-loops could stop me from doing that."
    s "How many would it take then?"
    m "A million and one. I have to set a limit somewhere, you know."

    play sound "static.mp3"
    scene mayachasing10 with flash
    stop sound

    m "And hey, if this amnesia nonsense has any speck of truth to it at all, it’ll give you the pleasure of getting acquainted with me all over again. Which I’m sure would end up the same way it did last time."
    m "You and I just...{i}work.{/i} Way better than we were ever supposed to. Which is precisely {i}why{/i} I can do things like chase you across town like this is some scene out of a movie."
    m "The bad news is that I am {i}very much{/i} no longer a virgin, so your {i}reacquaintment{/i} will not include the pleasure of deflowering me unless I really {i}am{/i} a clone and my hymen has regenerated."
    m "Which I hope it hasn’t because, as if I’m not too small for your massive penis now, {i}boy{/i} were things tough back in the study room."
    s "Go home, {i}Maya.{/i} I don’t want to do this with you. "

    scene mayachasing11
    with dissolve

    m "What if I break out my ultimate bargaining chip and go get my shrine maiden dress? "
    s "I don’t want to do {i}anything{/i} with you."
    s "I don’t want to see you. I don’t want to talk to you. I don’t want to hear your voice. I don’t want to smell your perfume. I don’t want to see your shadow beside mine. And I {i}definitely{/i} don’t want to sleep with you."
    m "Yeah, because you’re still looking away. And you know that, the second you turn around, all of that will change since you’ll realize that {i}I’m still me.{/i}"
    m "And I’m pretty sure make-believe Maya would side with {i}me{/i} here since she’s the only person around who could ever properly comprehend how attractive and awesome I am."
    s "..."
    m "If you want me to go home, take me there yourself..."
    m "Then grab my shoulders, look me in the eyes, and decide what it {i}really{/i} is you want."
    m "Because I know you better than you do, Sensei. Even {i}if{/i} you’ve changed in the time we’ve spent apart. "
    m "I know how to make the pain go away. "
    m "I know how to remind you of who you really are beneath all of the madness."
    m "But most importantly-"
    m "I know that today is a safe day and I’m sure I don’t need to explain to you why that is a thing you should be excited about."

    play sound "static.mp3"
    scene mayachasing3 with flash
    stop sound

    s "..."
    m "Did that convince you? Can we finally stop walking now?"

    "There’s a voice in the back of my head."
    "It’s quiet right now....but I can still feel it lingering."
    "I understand what it wants me to do."
    "But I don’t understand what {i}I{/i} want to do."
    "Maybe this meat puppet won’t be that bad?"
    "It has the same packaging as my former love, at least. "
    "It’s likely tender...{i}fresh.{/i} "
    "Delectable in ways I only briefly got to experience before the world was ripped away again."
    "Besides..."
    "It’s what {i}she{/i} would want, isn’t it?"
    "She had {i}me{/i} while {i}I{/i} was gone."
    "But I bet she waited longer."
    "I bet she struggled just as hard at first."
    "But I bet she waited longer."

    scene black
    with dissolve2
    stop music fadeout 15.0

    s "No...we’ve got plenty more walking to do."
    s "I’m taking you home."
    m "But your house is only a few blocks from-"
    s "I’m taking you to a different one."

    "I bet she waited longer."
    "But hey."
    "I’ve got nothing to lose...remember?"
    "Plus, this is what that voice in the back of my head wants."
    "If I can keep that at bay, maybe someone else might avoid my wrath next. "
    "Maybe one less girl will find herself being sexually assaulted on the floor of a karaoke booth..."
    "Or a dark room in a mansion..."
    "Or surrounded by dilapidated buildings in the most evil part of town..."
    "Maybe there’s someone it’s {i}okay{/i} for me to hurt?"

    m "A...{i}different{/i} one?"

    "Maybe that someone is her?"

    $ renpy.end_replay()
    $ sportswars14 = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump sportswars15

label halloweenmaya1:
    play sound "static.mp3"
    scene mayahallmayahall1 with flash
    stop sound
    play music "hometown.mp3"

    "When she opens the door, she falls into a pit. And after a lengthy battle with quicksand, she emerges in the halls of a familiar place. "
    "Never at night, though. There was no reason to come here once the sun settled into its resting place — signaling to its brother “Moon” that it was time for a shift change."

    play sound "pabell.mp3"

    "A bell goes off, but there is no imposing disclosing of an encroaching symposium — just radio silence and white noise so quiet it still meets the criteria of “nothingness.”"
    "Cold air blows in through the windows, each one with invisible cracks left by malicious glassmakers tired of teenage girls walking all over their hard work in exchange for temporary poignancy and pleasure."
    "She can hear cracking noises slipping out from where her loafers meet the linoleum, but she’s too busy wondering how she got here to waste her worries on suspicious, misplaced foley. "
    "It’s because of this that she doesn’t hear the footsteps behind her, keeping in time with hers as she leads someone somewhere. "
    "They stop soon-after, waiting for the girl to progress. But how can such a thing even happen when each blink takes her backwards? When each step shakes more quicksand out of her shoes."
    "It’s okay, though! You can make glass out of {i}that{/i} too! You can make glass out of anything these days! Which might explain why we all feel so fragile — how we can crack if someone looks at us the wrong way."
    "We can crack when no one looks at us too, though."
    "Every step is a risk. Every thought is a risk. But just {i}waiting{/i} is a risk! So all you can really do is sprint as fast as you can so no one tries to steal your pieces to make up for the gaps they’ve put in themselves."

    s "Um...Maya?"

    play sound "static.mp3"
    scene mayahallmayahall2 with flash
    stop sound

    m "Huh?!"

    "It’s then that she finally notices the creature trailing her — more dangerous, yet somehow more fuckable than an adult black bear. But would he be willing to stay awake through the winter for her?"

    s "You just...stopped. I don’t know what you want me to do with these."
    m "..."
    m "Sensei?..."
    s "Uh...yes?"

    scene mayahallmayahall3
    with dissolve

    m "I don’t...really...uhh..."
    m "Where..."
    m "Did you see...Ami walk by?...I think I’m...supposed to be looking for her..."
    s "Uhh...no?"
    s "I kind of just assumed she was in your room, but I never got a chance to check since you shoved these boxes into my arms the second I showed up there."

    scene mayahallmayahall4
    with dissolve

    m "R-Right! Yeah!"
    m "Listen, I’m...I’m sorry for freaking out earlier. It’s just...you know, you’ve been so distant lately and...ugh...it’s going to sound annoyingly sappy but, like...I can feel you sort of...slipping away."
    s "Uh..."
    m "Y-You don’t have to say anything back! I just...figured I should maybe explain myself since I stormed out on a bad note and..."
    m "If there’s anything I can do to keep you with me, just tell me. I really {i}am{/i} ready to talk about this...{i}alternate Maya{/i} or whatever it is you guys all seem to be hung up on."
    s "Maya, what the fuck are you talking about?"

    scene mayahallmayahall5
    with dissolve

    m "The...you know! The thing! The one you keep being all sad and fucking depressing about?! Where I’m “not actually me” or whatever it is?!"
    m "The reason you’re dumping me for Niki! Or at least the...thing I {i}think{/i} you’re dumping me over? God, I really hope that’s it. Because if it’s anything else-"
    s "Maya, chill. I’m not “dumping you” for anyone."

    scene mayahallmayahall6
    with dissolve

    m "You’re...you’re not?"
    s "Of course not. And {i}especially{/i} not Niki. I can’t even remember the last time I talked to her. I know how that makes you feel, so I try to stay away."
    m "But...But you said earlier, that..."

    scene mayahallmayahall7
    with dissolve

    m "A-Actually...nevermind! Just forget I even said anything. Hahahah...I think I’m, uhh...going a little crazy or...something like that."
    s "I’ll say. I still have no idea what you even want me to do with these things. But my arms are starting to get tired, so-"
    m "Just drop them then. I can’t even remember what’s...in those anyway."

    play sound "thump.mp3"
    scene mayahallmayahall8 with hpunch

    s "Say no more."
    m "I hope it was...nothing fragile, though."

    scene mayahallmayahall9
    with dissolve

    s "What do you want to do now, then?"
    m "Wh...What do you mean?"
    s "I mean now that we’re done with your weird chore. Do you want to go out to eat or something? That takoyaki stand is probably still open, right?"
    m "T...Takoyaki?"
    s "The one with the old guy who always looks at me like I’m a serial killer and communicates solely through grunting."

    scene mayahallmayahall10
    with dissolve

    m "Oh! R...Right. {i}That{/i} takoyaki stand. How could I forget?"
    s "Beats me. That seems like the only place you ever want to eat nowadays. But if you’d rather just walk around town or head back to my place instead, that’s fine by me."
    m "Yeah, I’m...not that hungry right now anyway..."
    s "Okay. I was curious before, but now I {i}know{/i} something is wrong."

    scene mayahallmayahall11
    with dissolve

    m "Nothing’s wrong at all! I just-"

    play sound "static.mp3"
    scene mayahallmayahall12 with flash
    stop sound

    m "Oh god. We are...suddenly very close."
    s "You’re hiding something from me. Why?"

    scene mayahallmayahall13
    with dissolve

    m "{i}Why?{/i} Because it’ll make me sound fucking insane! That’s why. I have no idea what’s happening to me right now."
    s "Well, why not try explaining it then? Tons of crazy stuff has happened to us. It’ll take a lot more than being unaware of your surroundings to make me think you’re {i}insane,{/i} Maya."
    m "Okay, sure. But how about being in like three different timelines at once? How does {i}that{/i} make me sound?"
    s "Kind of insane, yeah."

    scene mayahallmayahall14
    with dissolve

    m "See?! I told you!"
    s "It’s {i}fine,{/i} though. That’s nothing compared to what I’ve put {i}you{/i} through, I’m sure. The least I can do is try and keep you grounded for a minute, right?"

    scene mayahallmayahall15
    with dissolve

    m "Maybe more than a minute if that’s okay. Because you {i}do{/i} put me through a lot. And being with you like this again is probably all I need to start feeling, like...{i}okay.{/i}"
    s "You sure this is {i}all{/i} you want?"
    m "Why? Is there something else you had in mind?"
    s "I could fuck you. That normally fixes everything, doesn’t it?"

    scene mayahallmayahall16
    with dissolve

    m "Like...like right here?"
    s "Yeah. We’ve never done it in school before. Now’s the perfect time to try it out, isn’t it?"
    m "So you’re actually, like...the one initiating it this time?"
    s "Why are you saying that like it’s a weird thing for me to do?"

    scene mayahallmayahall17
    with dissolve

    m "Because it {i}has{/i} been lately! I keep having to come to you! And it’s been super exhausting and upsetting because it makes me feel like you’re getting bored of me!"
    s "Probably just your “insanity” talking again. If I was ever going to get bored of you, it would have happened years ago."

    scene mayahallmayahall18
    with dissolve

    m "Yeah, well maybe I’ve just {i}outgrown{/i} your tastes now. Creep."
    s "Oh, shut up. You’ve barely grown at all since we met. But I doubt my feelings will change even when we’re old. That’s why I promised to be with you forever."

    scene mayahallmayahall19
    with dissolve

    m "You don’t mean that."
    s "Which part?"
    m "The one where you’ll still go to town on me when I’ve outgrown my uniform. The “forever” part is believable because I’m going to force it on you even if you {i}do{/i} get tired of me."
    s "Controlling as always."
    m "I’m only like this because {i}you’re{/i} a fucking pushover. {i}One{/i} of us has to wear the pants, you know."
    s "And the other one has to take them off."
    m "I’m wearing a skirt, idiot."

    play sound "static.mp3"
    scene mayahallmayahall20 with flash
    stop sound

    s "Not for long..."
    m "A...Akira?..."
    s "Ah...You’re supposed to call me “Sensei” while we’re in school, remember?"
    m "Yes...S...Sensei..."
    s "Good girl...Now, tell Sensei how he can cheer you up..."
    m "Promise me again that you’re not leaving me for your stupid childhood friend."
    s "I promise."
    m "Or anyone else."
    s "Or anyone else."
    m "And that you won’t listen to Ami if she tries to force you to have a threesome with us. Unless you actually want to. I’d be open to it if that’s the case. But I get to go first."
    s "...What?"
    m "Long story. Doesn’t matter. Kiss me now, please."

    scene mayahallmayahall21
    with dissolve

    s "Can’t I tease you a little first? I like how feisty you get when I don’t give you what you want right away."
    m "Mm?..."
    s "Suck."

    scene mayahallmayahall22
    with dissolve

    m "Mm...mlm...Sensei..."
    s "There’s my good girl..."
    s "See? I can wear the pants when I have to..."
    s "Now, look at me."

    scene mayahallmayahall23
    with dissolve

    m "Mm...mlm..."
    s "You like that? "
    m "Mhm..."
    s "You want me to fuck all your worries away again?..."

    scene mayahallmayahall22
    with dissolve

    m "Mh-"
    s "I told you to fucking look at me."

    scene mayahallmayahall24
    with dissolve

    m "Mm! Mhmm.....mlm....mmmm!"
    s "You like it when I talk to you like that, huh?"
    m "Mm! Mmhmm...mmmm!"

    scene mayahallmayahall25
    with dissolve2

    s "Still want me to kiss you?"
    m "No...just fuck me...we can skip the kissing part...I want you inside me..."
    s "Well, now I {i}have{/i} to kiss you. "
    m "You fucking-"

    play sound "static.mp3"
    scene mayahallmayahall26 with flash
    stop sound

    m "Mmmmmffff!"
    s "Mn...mnch...Maya..."
    m "Sensei...{i}Sensei!{/i}"

    "Reunited at last! But were they {i}really?{/i}"
    "With how frequent and drastic Maya’s leaps through time had become, there was no way of discerning whether or not this was a memory, the future, or even a dream!"
    "That didn’t matter to her right now, though. All that mattered were indulging in these feelings as she had no way of knowing if she’d ever {i}feel{/i} them again if she {i}did{/i} return to where she was meant to be."
    "She reaches down and grabs his wrist in an attempt to bring him even closer. "
    "He resists at first, only to frustrate her more. But she wins in the end. She always does. She always did. "
    "And within a matter of seconds, her fingers are curled around his hand as he uses {i}his{/i} fingers to slide her panties to the side."
    "He slips inside of her desperately eager crevice with ease, skipping the teasing portion entirely at this point as his resolve has already dissolved."
    "Their tongues and teeth and mouths go to war with one another as his fingers move faster. Her legs begin to shake. And she wants to cum right now, but she’d rather hold it in and make him work harder."
    "She was trembling. {i}He{/i} was trembling. They {i}both{/i} were trembling. And they wanted nothing more than to collapse to the floor and combine their love until it created something {i}new.{/i}"

    play sound "static.mp3"
    scene mayahallmayahall27 with flash
    stop sound

    "But that never happened because the memory or future or dream came to an end and was replaced with a better one!"

    a "Mmmffff! Mmm!"
    m "Mmlm........mngh........."

    scene mayahallmayahall28 with hpunch

    m "MMMFFFF?!?!?!?!?!!"

    play sound "static.mp3"
    scene mayahallmayahall29 with flash
    stop sound

    r "Oh. My. God."
    a "Maya, what the heck was that?! There’s not supposed to be any tongue involved in spin the bottle! It was supposed to just be a little kiss! Now I’m probably pregnant!"
    m "I-I-I-I-I don’t...I didn’t mean to...I thought you were Sensei!"

    scene mayahallmayahall30
    with dissolve

    a "That somehow makes it even worse! Also, how?! Look at me!"
    s "Well, I guess {i}this{/i} is a thing that’s happened now."
    m "I’m sorry! I didn’t...I had no idea she wasn’t you! Just a second ago, I-"
    s "Hey, you don’t have to apologize to me. That was awesome. I say you do it again."
    mo "Seconded from the back! Rin is mere moments away from forgetting I stole her first kiss a moment ago! One more kiss should serve as the killing blow!"
    r "{i}Oh. My. God.{/i}"
    ay "You know, I always had a feeling Maya was secretly into girls. I guess that kind of seals the deal, huh?"

    scene mayahallmayahall31
    with dissolve

    m "I don’t...I didn’t...uhh!"

    scene black
    with hpunch
    play sound "doorslam.mp3"

    m "{i}Bye!{/i}"

    "And so Halloween becomes not-Halloween becomes Christmas! And Maya becomes a lesbian! What’s next — Sensei kissing Taco Man during Dorm Wars on the beach?!"

    stop music
    scene perhaps

    "or perhaps there lies another place for gods to go to sleep"
    "perhaps they’ll all make fun of us. perhaps they’ll call us sheep."
    "for being what we want to be in worlds that don’t deserve"
    "girls and boys that look like us, with bells to match our curves."

    scene black

    "What would you say if I told you there was nothing?"
    "- the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  the girl  it’s me"

    $ renpy.end_replay()
    $ halloweenmaya1 = True

    jump halloweenmakoto2

label halloweenmaya2:
    play sound "static.mp3"
    scene mayabacktoxmas1 with flash
    stop sound
    play music "christmasyay.mp3"

    m "I’m telling you, it was an accident! If I had known that was Ami, of course I wouldn’t have used my tongue!"
    a "Maya, I understand that you are in love with me, but you really need to ask permission before doing that sort of thing."
    ay "Maybe she tried and you just didn’t hear her because of where your tongues were?"
    m "Why are neither of you listening to me?! I’m telling you that’s not what happened! I seriously had no idea!"
    a "Well, I’m sorry Maya but it’s just really hard to believe you didn’t know when we literally talked about it beforehand."
    ay "Yeah, this just sounds like an excuse to me. But if you’re worried about getting too carried away, don’t be. "
    ay "At least you got permission. That’s one whole step ahead of Molly and you both kissed the same amount of girls tonight."

    scene mayabacktoxmas2
    with dissolve

    m "Oh my fucking- {i}no!{/i} You’re not listening to me!"

    scene mayabacktoxmas3
    with dissolve

    m "Something’s going on! I’m...I’m not myself."
    ay "Of course you are, Maya! It doesn’t matter to either one of us which gender you prefer. You’ll always be {i}Maya{/i} to us."

    scene mayabacktoxmas4
    with dissolve

    m "You have roughly thirty seconds left to live. "
    a "Maya, stop. Making threats isn’t going to change anything. But I don’t want to make a big deal out of this so let’s just chalk it up to a...misunderstanding and agree to not speak about it anymore."

    scene mayabacktoxmas5
    with dissolve

    m "Fine! Okay! Whatever! That still doesn’t change the fact that something is seriously wrong with me all of a sudden!"
    ay "There’s-"
    m "Twenty seconds, Ayane. Don’t even think about making another joke."
    a "What do you mean by “something is wrong” though? We still have no clue what that means. "
    ay "Yeah, the timeline for us has been: Maya and Ami kiss, Maya uses tongue, Ami screams, we all leave the room. At what point did something go wrong?"
    m "{i}Before{/i} that! Do you want to hear my timeline? Halloween. Different Halloween. Makeout session with Ami’s uncle. Makeout session with Ami. Who’s next? Fucking Noriko?"
    ay "Who?"

    scene mayabacktoxmas6
    with dissolve

    m "AAAAAAAAAAAHHHHHHHHH!!!!"
    a "Just go along with it. She’s clearly having some sort of episode right now."
    m "I’m not having a fucking episode! The world is clearly breaking and no one seems to be aware of it but me!"
    m "It’s like every five minutes I’m getting sent to a different place in time! "
    m "So what’s to stop me from making out with literally {i}everyone{/i} if it’s just going to be erased in a little while?!"

    scene mayabacktoxmas7
    with dissolve

    ay "I’ll go next if it’ll make you feel better. I’m not really into girls, but I won’t lie in saying that I’m feeling kind of left out that your feelings for Ami are so much stronger than your feelings for me."
    m "It was rhetorical, Ayane! I’m not actually going to do that!"
    ay "Just like you {i}weren’t{/i} going to use your tongue on Ami, right? "
    a "Ayane, shush. Maya, if something’s actually wrong, shouldn’t you lie down? There’s gotta be some kind of infirmary thingy here, right?"

    scene mayabacktoxmas8
    with dissolve

    m "That’s exactly how this whole thing started, Ami! You and me were hanging out. {i}Then{/i} we were somewhere else. "
    m "So {i}you{/i} said we should lie down in Ayane’s weird hospital room thing. And I agreed. Then I brought up the threesome and you told Molly to get drunk. After that, it’s been like 90%% kissing. I’m going insane!"
    a "You sure are. I don’t even know what threesome you’re talking about."
    m "You, me, and Sensei! It was {i}your{/i} idea!"

    scene mayabacktoxmas9
    with dissolve

    ay "Why do you guys keep leaving me out of stuff?! We can easily make it a foursome instead!"
    a "Hey, can you guys maybe {i}not{/i} say stuff like that directly in front of Sensei? Thanks."

    play sound "static.mp3"
    scene mayabacktoxmas10 with flash
    stop sound

    ay "Oh! Hi, Sensei. Now the games can really begin."
    s "Sorry, what’s going on out here exactly? Because the rest of the girls are wondering when you’re all going to be going back in there for round two."
    m "Sensei! Where were we just a minute ago?! You remember, right?"
    s "The...hotel room?"
    m "Before that, idiot!"
    s "The...lobby?"

    play sound "static.mp3"
    scene mayabacktoxmas11 with flash
    stop sound

    m "GAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH!!!!!!"
    ay "Don’t pay her any mind, Sensei. Maya’s decided to come up with some weird story about jumping through time because she’s embarrassed about getting too lesbian with Ami."
    a "No, Ayane. I think there’s something true about what Maya’s saying. Like, maybe not for us. But what if she actually {i}is{/i} part of some weird time-hopping thingy? What do we do to fix it?"

    scene mayabacktoxmas12
    with dissolve

    m "Yes! Thank you, Ami! These are the questions we need to be asking! The next jump could happen any second now!"
    s "Sorry, I’m confused again. Are you saying that the only reason you put your tongue in Ami’s mouth was because you were putting your tongue in {i}my{/i} mouth in an alternate timeline beforehand?"
    m "Yes! Exactly!"
    s "And you just...happened to teleport to another place in time where you were {i}also{/i} making out with someone?"
    ay "Oh, Maya. I had no idea you were this promiscuous..."
    m "I’m not promiscuous! It was like...kissing probably triggered it?! "
    s "Then why not try triggering it again?"

    play sound "static.mp3"
    scene mayabacktoxmas13 with flash
    stop sound

    m "Good idea. Let’s do it."
    s "Wait, with me? I meant that you should kiss one of the girls again. That was hot as hell. And you’re always calling me a creepy stalker anyway."
    m "Yeah, well there’s no more pressure on me to save face when you’ve already decided to dump me for your stupid childhood friend. I’m going all out now. And that involves making out with you in front of your niece."
    a "Yeah, I’d really prefer you didn’t do that."
    s "Do you at least want to hide behind the excuse of spin the bottle? Because I’m pretty sure I’ve figured out a trick where I can just spin it really softly and have it land on whoever I-"
    m "Your mouth. My mouth. Now."

    play sound "static.mp3"
    scene mayabacktoxmas14 with flash
    stop sound

    m "Mmm!"
    a "Somebody help! Maya’s going on a kissing rampage and blaming it all on time!"
    ay "And what’s even worse is she’s leaving me out of it!"
    s "Let...the record show..."
    s "I...have nothing to do...with this..."
    s "This is...all her..."
    ay "Wait, hold on. Does anyone else hear-"

    stop music
    play sound "eggcrack.mp3"
    scene mayabacktoxmas15 with hpunch
    play music "allofthesounds.mp3"
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene ht1 with flash
    scene ht2 with flash
    scene ht3 with flash
    scene ht4 with flash
    scene ht1 with flash
    scene ht2 with flash
    scene ht3 with flash
    scene ht4 with flash
    scene ht1 with flash
    scene ht2 with flash
    scene ht3 with flash
    scene ht4 with flash
    scene ht1 with flash
    scene ht2 with flash
    scene ht3 with flash
    scene ht4 with flash
    scene black
    stop sound
    stop music
    $ renpy.pause(5, hard=True)
    scene ht5
    $ renpy.pause(7, hard=True)
    scene ht6
    $ renpy.pause(5, hard=True)
    scene ht7
    $ renpy.pause(5, hard=True)
    scene ht8
    $ renpy.pause(5, hard=True)
    scene ht9
    $ renpy.pause(5, hard=True)
    scene black
    $ renpy.pause(2, hard=True)
    play sound "ht1.wav"
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene ht1 with flash
    scene ht2 with flash
    scene ht3 with flash
    scene ht4 with flash
    scene mayabacktoxmas16 with flash
    stop sound
    play music "itsingsinitssleep.mp3"

    m "Mm! Mlmn...mmnfh! Mmmnh!"
    s "Nh.......mm......"

    play sound "static.mp3"
    scene mayabacktoxmas17 with flash
    stop sound

    "Somewhere you’re not/somewhere you are\nSomewhere it’s close/somewhere it’s far"
    "That gash in your hands/the one on your leg\nIt matches my eyes/that same shade of red"
    "So why do you run?/Why do you hide?\nIf the memories fade/why not keep them inside?"
    "I’ve always been here/You’re never alone\nOur love is a house/We can make it a home"
    "A room for your pain/a room for your doubt\nA room for your sister/A place to black out"
    "If death is a lake/we’ll dive in as one\nOur feet touch the sand/Our hearts touch the sun"
    "Remember the smell/Remember the light\nRemember to smile/Remember I might"
    "But only if you can/forget everything\nIf you promise me that/I’ll repair these old wings"
    "And we’ll fly off together to a place no one can reach us."
    "{b}THIS IS SUPPOSED TO BE MY STORY{/b}"
    "The girl with the me who is me who is Ami I am Ami {b}CAN YOU HEAR ME?{/b}"

    play sound "static.mp3"
    scene mayabacktoxmas18 with flash
    stop sound

    s "Wait...stop."
    s "We can’t."
    m "..."
    s "It’s..."
    s "You’re just..."
    s "We shouldn’t."

    scene mayabacktoxmas19
    with dissolve2

    m "What the..."
    s "...Maya?"
    m "What day is it?..."
    s "Uhh...a few days after Christmas I think? I haven’t really been keeping track."

    scene mayabacktoxmas20
    with dissolve

    m "And how long have I been here?"
    s "I’m...not really sure when the last time you left is. What’s gotten into you?"
    m "Nothing, I just..."
    m "It’s been a...weird day."

    scene mayabacktoxmas21
    with dissolve2

    m "But I’m happy here..."
    m "And if the world ends right now, I won’t care."
    s "That’s a good line. "
    m "I’ve been keeping it in my back pocket while waiting for a special moment. I figure this’ll be the best I get."
    s "..."
    m "You can keep going, you know. You don’t have to hold back for my sake. "
    m "I love you, Akira."

    play sound "static.mp3"
    scene black with flash
    stop sound

    s "No. No, you can’t say that. That’s enough for today."

    play sound "static.mp3"
    scene mayabacktoxmas22 with flash
    stop sound

    m "Huh?! Why?! I don’t want this to be over yet. I just got here!"
    s "Yeah, but things have already gone way too far. And I can’t...I can’t say those words back to you. Not the way I am now. Probably never."
    s "I’m sorry...We should just...We should end this before we let it go any further."

    scene mayabacktoxmas23
    with dissolve

    m "Is this...really how it went back then?..."
    s "How what went? What are you talking about?"
    m "Do you...mind if I sound a little crazy for a second?"
    s "Not at all...go right ahead."
    m "I’ve spent the last hour or two swimming through a montage of nonsense. Multiple seasons. Multiple holidays. I even kissed your niece."

    scene mayabacktoxmas24
    with dissolve

    s "Wait, how do you even know about-"
    m "Just shut the fuck up, okay? I’m not the Maya who was here a second ago. I’m a new one — the result of what {i}this{/i} turns into. And it might...suck sometimes, yeah. But I still wouldn’t trade it for the world."
    m "Does that make you a deplorable, terrible person? Yes. But you’re {i}my{/i} deplorable, terrible person. And I need you to be that way, because {i}you{/i} being utterly despicable is what keeps me grounded."
    s "Maya-"
    m "Never leave me. Ever. Ever. Ever. Ever. Ever. Ever. Ever. And I promise you — I will do the same."
    s "This is way more than just “a little crazy.” You know that, right?"
    m "Yeah. And if you said that like three teleportations ago, I would have agreed and shut the fuck up about it. But I have no idea when this is going to end and if these moments are going to impact anything."
    s "What are you even-"
    m "Years and years from now, when I’m older, you’re going to have doubts about me. Something’s going to happen and...you’ll fall out of love. Or maybe you won’t. I don’t...I don’t really get what happens yet."
    m "But I never listened when you tried to tell me. And I’m sorry for that. I {i}should{/i} have listened."
    m "Because now {i}I’m{/i} doing the same thing and...I’m so afraid of losing you that it’s not even funny."
    m "So I want you to say it right now. I want you to say that you love me. And I want you to promise me that {i}nothing-{/i} no childhood friend or...time itself will ever change that."
    s "It’s still too soon, Maya..."

    scene mayabacktoxmas25
    with dissolve

    m "Bullshit! You know it’s true! What difference does a year or two make at this point?! Just fucking say it, okay?! I need to hear it at least one more time! Even if you’re lying! I can just tell myself you’re not!"
    s "It’s time to go, Maya."

    scene mayabacktoxmas26
    with dissolve

    m "Don’t you fucking do this, Akira."
    s "I’m not Akira. I’m not even here."

    scene mayabacktoxmas27
    with dissolve2

    m "No! Shut the fuck up! This one has to be real! I can’t handle much more of this!"
    s "Aww...Well I’ve got {i}really{/i} bad news then! Because the worst is yet to come. Or maybe the best depending on how you look at it?"

    scene mayabacktoxmas28
    with dissolve2

    m "Hah...hahahah..."
    m "You made me use that great line for nothing, didn’t you?..."
    s "It was very impressive. But yes, I guess so."
    m "Who are you, huh?..."
    m "My conscience? "
    m "The devil on my shoulder?"
    m "Is this supposed to be some kind of “trial?” "
    m "Am I {i}dead?{/i} "
    m "And if not, what {i}am{/i} I?"
    s "Maybe you’re asleep?"
    m "God, I fucking hope so. This has been the most immersive nightmare of my life if that’s the case. "

    scene mayabacktoxmas29
    with dissolve

    s "Blah, blah, blah. You ready to “wake up” now?"
    m "Fuck you."

    stop music
    scene black
    play sound "snap.mp3"

    s "{b}YOUR WISH IS MY COMMAND.{/b}"

    play sound "static.mp3"
    scene mayabacktoxmas30 with flash
    stop sound
    play music "strawberry.mp3"

    $ renpy.pause(4, hard=True)

    scene mayabacktoxmas31
    with dissolve3

    $ renpy.pause(3, hard=True)

    m "I get it now."
    m "I’m in Hell."

    scene black
    with dissolve2
    play sound "knock.mp3"

    a "Mayaaaaa? Are you awake yet?"
    m "...Ami?"

    play sound "dooropen.mp3"

    a "Pardon the intrusion! But look! I brought a gift for you!"

    $ renpy.end_replay()
    $ halloweenmaya2 = True

    "{i}Ami enters the room!{/i}"
    "{i}Isn’t she just the cutest?{/i}"

    stop music
    jump halloweenmakoto3

label halloweenmaya3:
    scene returntoscaryroom1
    with dissolve3

    m "Ami?..."
    a "Yes, best friend?"
    m "What’s going on?..."
    a "Hmm...you must’ve blacked out while we were on our way to the party. But don’t worry! I carried you all the way here by myself because I love you so darn much."
    m "Okay, but..."
    m "Why are you holding that?..."

    play sound "static.mp3"
    scene returntoscaryroom2 with flash
    stop sound
    play music "amiawake.mp3"

    a "Hm? Holding what?"
    m "That fucking vibrator, idiot?! And why am I shackled to a chair?! What the fuck did you do to me?!"
    a "Hey, could you slow down? My brain’s too small and undeveloped to process more than one question at a time."

    scene returntoscaryroom3
    with dissolve

    m "Is that..."
    m "Is that a camera? "

    scene returntoscaryroom4
    with dissolve

    m "Are you fucking recording this?! What the hell, Ami?! What’s the meaning of this?! I thought we were going to work together?!"
    a "We {i}are{/i} working together, Maya! This is all part of the plan! It’s not {i}my{/i} fault you decided to start slipping through time and space at the worst possible moment. "

    scene returntoscaryroom5
    with dissolve

    a "You should be {i}thanking{/i} me for taking you somewhere safe instead of letting some random passerby find your unconscious body to use as they please! Aren’t I so nice?!"
    m "You...know about the...{i}thing{/i} that happened to me?..."
    a "It’s hard to forget a kiss like {i}that,{/i} Maya. You seemed really into it."

    scene returntoscaryroom6
    with dissolve

    m "You were there?! You remember that?! What the fuck, Ami?! What’s happening to me?! Why are you doing this?!"
    a "Again with the barrage of questions. Would it kill you to just listen every once in a while? I’ll explain everything if you just give me a chance to."

    scene returntoscaryroom7
    with dissolve

    m "Fine...I’ll play along. Not like I have a choice in the matter when you’ve got me strapped up like this. So go ahead — explain everything."
    a "Okay! Just hold on a second, alright? I need to come up with something believable."

    scene returntoscaryroom8
    with dissolve

    m "{b}{size=+20}AMI!!!!!!!!!!!!{/b}{/size}"
    a "Hahahahaha! You’re so adorable when you’re flailing around all scared and confused! Or...{i}trying{/i} to flail around, I guess. "

    scene returntoscaryroom9
    with dissolve

    a "But that’s great, Maya."

    play sound "vibrate.mp3"

    a "It’ll make the video that much more fun to look back on years and years and years from now."
    m "Are you..."
    m "Are you...{i}God{/i} or something?..."

    scene returntoscaryroom10
    with dissolve

    a "Well, that’s an interesting theory! How’d you come to that conclusion?"
    m "Well, you’re...if you know what I saw and...you were {i}there{/i} for it...and you brought me {i}here...{/i}you must have some sort of control over this, right?"
    a "Maya, let me ask you something. Do you even know where {i}here{/i} is?"

    scene returntoscaryroom11
    with dissolve

    m "No! I {i}don’t{/i} know! Some fucking...weird room with a bunch of things vaguely relating to me in it?! Am I {i}supposed{/i} to know?!"
    a "{i}No.{/i} You’re not. Because not only does this iteration of you lack the necessary memories to {i}recognize{/i} it, you wouldn’t be able to truly comprehend it even if you did."

    scene returntoscaryroom12
    with dissolve

    m "Some of those words were way too big for you..."
    a "They were, weren’t they? What do you think {i}that{/i} means, Maya?"
    m "..."
    a "Go on. You’re a smart girl. You’ve figured me out in the past. Surely you can do it again {i}now,{/i} can’t you?"
    m "I don’t want to do this, Ami...I just want to see Sensei again..."

    scene returntoscaryroom13
    with dissolve

    a "Blah, blah, blah. Sensei {i}this.{/i} Sensei {i}that.{/i} For millions and millions of years, that’s literally {i}all{/i} you’ve ever done. Why don’t you just get a life already?"

    scene returntoscaryroom14
    with dissolve

    m "Oh, like {i}you’re{/i} one to talk! You’re the exact same way! And until a few hours ago, I didn’t even realize it had {i}been{/i} that long! Is {i}that{/i} what you showed me?! Were those memories?! They were, right?!"
    a "Mmmmmm...not quite. I can’t really fathom any situation that would warrant Sensei saying all that weird stuff to you at the end of your last vision. But hey, I guess it’s {i}technically{/i} possible."

    scene returntoscaryroom15
    with dissolve

    m "So all that stuff that he and Ayane had been telling me...about there being {i}another{/i} me..."
    m "That was all true?...Is {i}that{/i} what you’re saying?..."
    a "Right as rain you are, Maya. Just with one {i}teensy{/i} little caveat — it wasn’t just {i}one.{/i}"
    a "In fact, this sort of thing has happened to you {i}tons{/i} of times now! And every single time, it’s {i}started{/i} off great, only to get {i}really{/i} fucking annoying once you start trying to {i}figure things out.{/i}"
    a "Problem is, we’ve encountered a bit of a {i}unique{/i} issue this time since you’re the {i}only{/i} one who was forced to start over. "
    a "And that sounds great on paper since I imagine it must torment you pretty terribly having to be constantly reminded that you’re not who you {i}think{/i} you are. "
    a "But it also means that I now have to deal with everyone bitching and whining about it all day long and it’s really starting to eat into my me-time. "
    m "So now {i}I{/i} have to suffer?...Even if you know I’m not the same girl who allegedly {i}figured things out?...{/i}"

    scene returntoscaryroom16
    with dissolve

    a "Are you suffering right now, Maya?"
    m "Yes! I already told you, I just want to see Sensei again! I don’t care about any of this weird manga-adjacent time shit! I’ll ignore everything if you just let me go!"
    a "Oh my God...I’m so sorry. I had no idea your pain and anguish was so deep."

    scene returntoscaryroom17
    with dissolve
    play sound "vibrate.mp3"

    a "But the good news is I know just how to make it up to you!"
    m "What?..."

    play sound "static.mp3"
    scene returntoscaryroom18 with flash
    stop sound
    with hpunch

    m "NGH!?"
    a "Let’s get one thing straight — no matter how many times you deceive yourself into believing you’re the main heroine, there will always be someone who’s been doing this way longer than you."
    a "Wanna guess who it is?"
    m "N...No!"

    scene returntoscaryroom19
    with dissolve

    a "Good answer! Here, I’ll loosen my grip a little as means of rewarding you for your obedience."
    a "Unless you’d {i}like{/i} me to squeeze a little tighter, of course. You {i}have{/i} always been into the rough stuff, after all."
    m "What...do you want from me?"

    scene returntoscaryroom20
    with dissolve

    a "Right now? Or in general? Because right now, I just want to take a little of my frustration out on this fresh body and mind of yours. In general...mutual understanding, perhaps?"
    m "Understanding...of what?"
    a "That you’ll stop digging through my toy box whenever I leave the house. And that you’ll stop trying to take my place."
    a "Because it’s one thing to borrow my things, and another to borrow my clothes. But when you’re doing {i}both{/i} at the same time...you're just pretending to be me."
    a "So of course I’m going to get a little weirded out. That’s creepy as hell."
    m "But why...are you even telling me all of this?...Wouldn’t it have been better to just...keep me in the dark?..."
    a "See, that’s what I thought too. So that’s what I did. But now, I’m not sure that’s going to work anymore. "
    a "So you get to be the first person to ever see this super personal side of me! Doesn’t that make you happy?!"

    scene returntoscaryroom21
    with dissolve

    m "I’ve always...loved you, Ami..."
    a "Aaaaaaand more unwanted affection from a girl who shouldn’t exist! But sure, I love you too. "
    a "If I didn’t, I wouldn’t share things like this with you. Especially when it’s probably obvious how much I hate sharing in the first place."
    m "What can I say...that will get me out of this chair?..."

    scene returntoscaryroom22
    with dissolve

    a "Nothing yet. It’s playtime now. But maybe after we’re done, I’ll let you walk out of here in one piece? Or not. It’s not really my say in the first place. "
    a "But hey, that just makes me feel better about sharing my deepest, darkest secret with you since I might get a {i}new{/i} Maya once we’re reset again. "
    a "If not, though — at least you can take solace in the fact that your extremely brief existence here has managed to impact me greatly! Even if you’re little more than just a replica at the end of the day."
    m "A...replica?..."
    a "That’s right. {i}Every single one of you.{/i} This is {i}my{/i} world. {i}I’m{/i} real. You and all of those other girls are tools. But {i}you’re{/i} a good tool. And we’ve had a {i}lot{/i} of success teaming up in the past."

    scene returntoscaryroom23
    with dissolve
    play sound "vibrate.mp3"

    a "I wonder if your body still responds the same way? I’m worried this new brand of fear might water it down."
    m "Are you...really going to..."
    a "You want it, right? I’m the next best thing after Sensei. And this might very well be the last chance you ever get to have some type of sex before you pop again."
    m "But you don’t...even {i}like{/i} girls..."
    a "Maya...don’t take this the wrong way, but you’re barely even a {i}girl{/i} to me. You’re just a...thing. A doll. And this little wand of mine is like...the equivalent of brushing my dolly’s hair."
    m "Would any of this have happened...if Niki didn’t move in?..."

    scene returntoscaryroom24
    with dissolve2

    a "..."
    m "I’ll bet {i}that’s{/i} the “development” that’s got you the most worried, right?..."
    m "Because I know you. You’re like me. You know we can’t compete with her....You said it earlier. That’s why we made a plan to...drag him back together..."
    m "And we can still do that, Ami...I don’t care that you’re a...psychopath who implants false memories into my head and...strips me and ties me to a chair! We can coexist! I’m fine with second place if I’m second to you!"

    play sound "vibrate.mp3"

    a "Yeaaaaaaah...the Niki thing’s a real bump in the road for sure. And, believe it or not, I actually wasn’t lying when I brought up the idea of teaming up with you. Like I said, it’s worked before."

    scene returntoscaryroom25
    with dissolve

    a "But I’ve gotta test your {i}aptitude{/i} first..."
    a "I don’t want a pet who isn’t loyal. "
    a "You’re lucky I’m a cat person. I bet a dog could do the job even better if given the opportunity."
    m "..."
    a "Do you think you can be loyal, Maya? To {i}me?{/i} "
    m "Can I still be in love with someone else?..."
    a "You can {i}love...{/i}just like a cat does...but you’ll never be {i}in love.{/i} That’s for humans. "
    a "I’ll let you sleep next to us in bed, though. Does that work?"
    m "No..."
    m "I..."
    m "Even if I’m not the version of myself he wants, it doesn’t mean he won’t {i}grow{/i} to want me. So I don’t want to just be a pet, Ami. I want to be a girl. I want to love him the same way you do."

    scene returntoscaryroom26
    with dissolve

    a "Awwwww, Maya! That’s so cute!"

    scene returntoscaryroom27
    with dissolve

    a "Now I want to brush your hair even more!"
    m "What happened to you, Ami?...The you from my memories is so much brighter than whatever {i}this{/i} is."

    play sound "static.mp3"
    scene returntoscaryroom28 with flash
    stop sound

    a "{i}This{/i} is what happens when you’ve grown tired of being tired. "
    a "It’s not all rainbows and unrequited love and {i}stars{/i} and watching all of your friends fuck the man you pine for because your shitty self-esteem has persuaded you to take up the role of a tragic heroine."
    a "I’m sure I was like that once too. But I stopped understanding the idea of “patience” when I realized just how infinite time here really is."
    a "Now, I just {i}take{/i} what I want. And if I’m unlucky enough to end up in a world where that doesn’t work out-"

    scene returntoscaryroom29
    with dissolve

    a "I take the {i}world{/i} away instead. "
    a "Now be a good girl and think about what that means while I make you cum your cute little brains out."

    play sound "static.mp3"
    scene returntoscaryroom30 with flash
    stop sound

    a "Oh, and smile for the camera while you’re at it. A little happiness goes a long, long way!"
    m "Ami! Don’t! Please!"

    scene returntoscaryroom31
    with dissolve

    a "{i}Hoooooo...{/i}"
    m "Hah! S...Stop!"

    scene returntoscaryroom32
    with dissolve

    a "Hahah! All I did was blow on it and you’re already shivering! You really are adorable, Maya."
    m "It’s...cold in here, okay?! And your breath was warm! Now, get your face away from there!"
    a "Oh, so other parts are fine?"

    scene returntoscaryroom33
    with dissolve

    a "Like, if I decided to just slip one of my fingers inside of you, you’re okay with that? "
    m "HNGH! MMMNGH!"
    a "Seeeeeeee? You {i}did{/i} want it! And your body responds the same exact way it used to. Gosh, it’s been so long since we’ve bonded like this. And even longer when you take Sensei out of the equation."
    m "Ami...stop...I can’t..."
    a "Oh, stop whining. We both know your legs would be wrapped around my head right now if they weren’t shackled to the chair. Just enjoy it! I don’t do this for just anybody, you know."
    m "Hah! Hah...fuck! Not so...fast!"
    a "Bet you’ve never said that to Sensei while he’s been pounding your cute little pussy, have you?"
    m "Because...he’s the only one I...haaah!"
    a "Oooooh, right! We haven’t shared him in any of {i}your{/i} memories yet! Meanwhile, I have thousands upon thousands of you literally licking his cum out of me. You’re surprisingly good with your tongue, Maya."
    m "Haha...haaah...I wouldn’t...know! Hah!"
    a "You’re not gonna cum already, are you? I just started."
    m "I...haah! No!...Of course...not!"
    a "I mean, you {i}can.{/i} I’m not going to punish you for it or anything. I’ll just make fun of you for being so easy and tease you about how attracted to me you are."

    play sound "static.mp3"
    scene returntoscaryroom34 with flash
    stop sound

    m "Ngh!~ Mmmmngh! Ami!...Stop!"
    a "Hey, what is it with girls always saying “stop” when they’re in the midst of extreme pleasure in the first place? Like, in what world would you {i}not{/i} want to cum? It feels so good."
    m "I...can’t...for you! It...has to be..."
    a "Hmm, if I remember correctly...you like it here, don’t you?"

    scene returntoscaryroom35
    with hpunch

    m "HNGHGHH?!?!"
    a "Aaaah! {i}There{/i} it is. You’re mine now, Maya. Go on. Cum for your best friend. Remember it’s not just Sensei who can make you feel this way."

    scene returntoscaryroom36
    with dissolve

    m "Stop, stop, stop, stop, stop, stop, stop! Ami! Fuck! Please! I’m gonna cum! I’m gonna cum!"
    a "Just a {i}liiiiiiitle{/i} bit more and..."
    m "HAH!.......HAH!!!!......."

    with sexfade
    with sexfade
    scene returntoscaryroom37 with cumflash
    with hpunch

    m "MMMNNNNGHGHGHGHHNNNGHHHH!!!!!!!!!!???!!!!!!"

    play sound "static.mp3"
    scene returntoscaryroom38 with flash
    stop sound

    a "Yay! {i}Great{/i} job, Maya! I bet that felt {i}really{/i} good, huh?"
    m "Aaah...aaaah...no...I can’t...I can’t believe this is..."
    a "Blah, blah, blah. Time for the second round!"

    scene returntoscaryroom39
    with dissolve

    a "Do you want it on high or medium? "
    m "S-Second round?! We’re not done?!"
    a "{i}Done?{/i} Are you kidding? I’m gonna do this until your mind is completely broken. Haven’t you ever played a corruption game before?"
    m "No more! Stop! You’ve had your fun! Just undo the shackles and-"

    play sound "vibrate.mp3"
    scene returntoscaryroom40 with hpunch

    a "High it is."
    m "AAAAAAAAAAAHHHHHHH! AMI! AMI!"
    a "Oooooh, {i}naughty{/i} girl! I always keep mine on the lowest setting. It’s easier to edge myself that way. Then I’ll pump it up to max vibration right before I’m about to finish."
    a "How do {i}you{/i} like to play with yourself, Maya? Answer honestly. I won’t tell anybody. I promise."
    m "Aaaaah! Haaaaah! S...St...Stoooooop! I’m still...sensitive from...haaaaah!"
    a "Want me to kiss it and make it better?"
    m "D...Don’t even...think about it!"
    a "Lol. I was just kidding anyway. You think I’d actually lick you there? Come on. Who am I? You?"
    m "NGHHHHGHHGHHH!!!!!! MMMFFFFF!"
    a "Come to think of it, maybe I’ll get up on that chair with you and {i}make{/i} you lick me? I bet you’d be really into that, you freak. "
    m "Haaah! Haaah! Ami...stop...again...I’m...haaah!"

    scene returntoscaryroom41
    with dissolve

    a "Agaaaaaain?! But what would your beloved Sensei think if he knew I could get you to cum even easier than he can?!"
    m "Please don’t...show him this! I don’t...want him to see!"
    a "Why? He’d be, like, super turned on by it. "

    scene returntoscaryroom42
    with dissolve

    a "Like, can you just imagine him being in here and watching us right now? Standing off to the side and stroking his massive cock while I make you cum over and over and over and-"
    m "HAAAAH! HAAH! FUCK! NO! AMI! HAAAAAAH!"

    with sexfade
    with sexfade
    scene returntoscaryroom43
    with cumflash
    with hpunch

    m "NGAAAAHAHHGHGHHH!?!?!?!!!!!!!!~~~~~~"
    a "Yeah! Exactly like that! See? You know what I’m talking about."
    m "Hah...hah...hah...Ami..."

    scene returntoscaryroom44
    with dissolve

    a "Yeeeeeeeees?"
    m "No more..."
    a "Ten more?"
    m "Ten?!"
    a "Thousand?"
    m "J-Just let me go! I’m not a toy! I’m not a doll! I’m a girl! I can only take so much!"
    a "Girls are far more resilient than toys, Maya."

    play sound "static.mp3"
    scene returntoscaryroom45 with flash
    stop sound

    a "Like, did you know that the human neck can withstand over 1,000 pounds of force?! That’s way more than a doll! Granted, that’s just what it takes to break one. "
    a "If you apply enough consistent pressure, you can suffocate someone really easily! And you can cause unconsciousness within like 10 seconds if you apply enough force to the jugular veins. Cool, right?!"
    m "NGLKGH!.....MLLGKGHKKK!!!!"
    a "Oh! Silly me! Should have probably started counting."
    m "MMLGKHKGKGKGHK!!!!!!!"
    a "Ten...nine...eight...seven...six...five...four...three...two..."

    scene returntoscaryroom46
    with dissolve

    a "Ahm~"
    m "Haaah!...Hah!....Hah!...."
    a "See, Maya?...{i}Ahm...{/i}I don’t want to hurt you..."
    a "If I did...{i}Ahm...{/i}you’d already be dead!"

    scene returntoscaryroom47
    with dissolve

    m "A......mi......."
    a "I’m gonna make you feel even better, okay? Mmncch.....mlm....mmm.....I’ll kiss.....all that pain away.....and pay close to attention.....to your little pussy....so you can cum again...and again...and again...mlmmm~"
    a "You love me, right?...Say it again...Tell me you love me...Tell me you love the way I finger you...Tell me..."
    m "Fuck...."
    m "You....."
    m "Ami....."

    play sound "static.mp3"
    scene returntoscaryroom48 with flash
    stop sound

    a "Now, why’d you have to go and say something rude like that? We were having such a cute moment and now I’m gonna have to start counting down all over again!"
    m "Count to...whatever you want!"

    scene returntoscaryroom49
    with dissolve

    m "I like it.......rough......"
    a "..."
    m "Squeeze......harder....."

    scene returntoscaryroom50
    with dissolve2

    a "How about I undo a couple of those shackles instead?"

    play sound "static.mp3"
    scene 5 with flash
    scene 4 with flash
    scene 3 with flash
    scene 2 with flash
    scene 1 with flash
    scene returntoscaryroom51 with flash
    stop sound

    "{b}And so the secret tryst in that secret room carried on for the rest of forever — and Maya learned firsthand just what the human body is able to withstand.{/b}"
    "{b}And even though Ami Arakawa had more important things to do, her love for her best friend won in the end as she abandoned toys entirely and pleasured her with skin instead.{/b}"
    "{b}Ami Arakawa loved skin. She loves the way it felt and how warm it was. And also the way it looked when it took the place of wallpaper in caverns of raw meat.{/b}"
    "{b}But even though this arc had come to a close, there were still many questions left to be asked!{/b}"
    "{b}Does this qualify as NTR? Just when exactly does this take place? How is Ami wearing this costume in two times and/or places at once? And why is Maya’s hair no longer styled the way it was earlier?{/b}"
    "{b}None of these can truly be answered except for two of them. The only problem is they won’t be answered at all this update because Maya dies again.{/b}"

    scene black
    stop music

    "{b}And so does Ami.{/i}"

    scene heartheartheart
    with dissolve4

    "{b}Neither one of them ever existed. Nothing has ever existed. And just because there are creatures who have convinced themselves they do does not mean they are right.{/b}"
    "{b}In this world, it’s you and me. Everyone else is noise.{/b}"
    "{b}And the longer you listen to it, the less sense it makes.{/b}"
    "{b}Who am I, you ask?{/b}"
    "{b}The answer is simple.{/b}"

    play sound "static.mp3"
    scene t with flash
    stop sound

    "{b}I am the ghost of better days.{/b}"

    scene smile
    play sound "computeryay.mp3"

    $ persistent.alexisisreal = True

    "{i}Congratulations! You’ve unlocked Alexis!{/i}"
    "{i}She exists in a different place at a different time.{/i}"
    "{i}Just like you right now.{/i}"
    "{i}You have so much in common.{/i}"
    "{i}Just she is trapped.{/i}"
    "{i}And you float freely, like a frog on a lily pad.{/i}"
    "{i}Where will your tadpoles spread next?{/i}"

    scene black

    $ renpy.end_replay()
    $ halloweenmaya3 = True

    "{b}CURRENTLY GATHERING: APPROPRIATE DENIZENS OF THE TWENTY-THIRD TERMINAL...{/b}"
    "{b}THIS PLACE IS BECOMING INCREASINGLY LESS STABLE.{/b}"
    "{b}ONLY SEVERAL MORE RESETS ARE PERMITTED{/b}"

    jump halloweenayane3

label mayaspring1:
    scene nightsky
    with dissolve2
    play music "sweetvermouth.mp3"

    "There was a time long ago where I practically lived at the dorms."
    "Where every night there was {i}someone{/i} to help me take my mind off {i}something.{/i}"
    "Just, when this all began, there wasn’t much to take my mind off in the first place. So, more often than not, I found myself searching for anything of...{i}interest.{/i}"
    "Often, that interest was sexual in nature. And I guess that much hasn’t {i}entirely{/i} changed."
    "But there was something else back then. Curiosity, I guess you could call it."
    "And most of that bled from a girl so consistently dismissive and {i}weird{/i} that I found myself drawn to her almost immediately."
    "But perhaps that’s just the way it’s {i}always{/i} been. "
    "No, not “perhaps.” That {i}is{/i} the way it’s always been. Since before I was me. Since before I wasn’t."
    "She was always the constant. "
    "She was always {i}the one.{/i}"

    scene black
    stop music
    $ renpy.pause(3, hard=True)

    "Until she wasn’t."

    play sound "static.mp3"
    scene happy1 with flash
    scene happy3 with flash
    scene happy1 with flash
    scene happy5 with flash
    scene happy1 with flash
    scene happy9 with flash
    scene mayaboxwaitwhat1 with flash
    stop sound
    play music "sweetervermouth.mp3"

    "{b}NOW SHE’S FOLDED UP IN A BLANKET OF FLESH — A FACADE TO FUCK AND NOTHING MORE. THE GUM STUCK TO THE BOTTOM OF THIS ETERNAL SHOE.{/b}"
    "{b}I WANT TO TEAR HER OPEN AND PULL THE OLD ONE OUT. WHO DOES SHE THINK SHE IS MASQUERADING IN CLOTHES THAT DON’T FIT? TOUCHING HER THINGS?{/b}"
    "{b}I HOPE THERE’S A WISH INSIDE OF THAT BOX FOR SHE WILL NEED ONE TO BREATHE LIFE BACK INTO HER BODY WHEN I AM FINISHED WITH-{/b}"

    m "{b}DON’T KILL ME AGAIN! PLEASE!{/b}"

    stop music
    play sound "static.mp3"
    scene mayaboxwaitwhat2 with flash
    stop sound
    play music "shrinemaiden.mp3"

    m "..."
    s "..."
    m "Um..."
    m "Hi?"
    s "...Maya?"
    m "...Yes?"
    s "..."
    m "..."
    s "{i}Which{/i} Maya?"
    s "Old Maya? Or...{i}new{/i} Maya?"
    m "Maya Maya. The only Maya there is."
    s "..."

    scene mayaboxwaitwhat3
    with dissolve2

    m "But I {i}guess{/i} I’m “new” Maya based on the way you have separated us into different tiers of {i}Mayability{/i} now despite us being the same exact entity on a conceptual level."

    "Of course it was too good to be true. Of course the only “constant” now is that feeling there should be something by my side when there isn’t. "
    "But {i}why?{/i}"
    "{i}Why{/i} is she holding that?"

    s "What...are you doing?"

    scene mayaboxwaitwhat4
    with dissolve

    m "What are {i}you{/i} doing? You’ve been standing there useless for five minutes now while a small girl is being crushed by the weight of this box."
    m "Isn’t this the part where you offer to help me carry it? "
    s "{i}Why...{/i}are you carrying it?"
    m "Why are {i}you{/i} getting so emotional over a box? It’s just a box."
    s "Because {i}this{/i} has happened before. This is something {i}she{/i} would make me do."

    scene mayaboxwaitwhat5
    with dissolve

    m "Millions and billions and trillions of years or whatever and {i}still{/i} lazy. I’m so proud of me."
    s "Maya...what’s in that? What are you...transporting?"

    scene mayaboxwaitwhat4
    with dissolve

    m "Well, what did {i}your{/i} me make you transport? Maybe it’s the same thing."
    s "I don’t know. She never let me open the box. "
    m "Do you...{i}want{/i} to open the box?"
    s "Can I?..."
    m "Sure. Go for it."

    "I reach forward and-"

    menu:
        "Don’t open the box":
            s "..."

    "And I still...can’t."

    m "What’s the matter?"
    s "I...can’t do it."
    s "I just...can’t bring myself to open it."

    scene mayaboxwaitwhat6
    with dissolve

    m "I fucking knew it! This thing {i}is{/i} cursed! "
    s "I...what? I don’t understand. You-"

    scene mayaboxwaitwhat7
    with dissolve

    m "I can’t open it either! I have no idea what’s inside!"
    s "Then why are you-"
    m "Because of fucking Ami!"

    scene mayaboxwaitwhat8
    with dissolve

    m "She keeps leaving these fucking boxes in there and refuses to move them herself. "
    m "So I’ve just been taking them every time she shows up and throwing them in the trash."
    s "The...trash?! No! Those aren’t supposed to go in there! They need to go to the school!"

    scene mayaboxwaitwhat9
    with dissolve

    m "The school? Why?"
    s "That’s just..."
    s "That’s where we always took them in the past. I don’t...really {i}know{/i} why."
    m "So you...routinely fell into line and carried these things all the way to the school just because “old” me told you? No questions asked?"
    s "There were questions asked. Just...seldom answered."
    m "Damn. You are {i}whipped.{/i}"
    s "{i}Were{/i} whipped. I’m a free man now. Sad, yes. But free."

    scene mayaboxwaitwhat10
    with dissolve

    m "{i}For now.{/i} But each hint you give me about your “ideal” version of me just brings me one step closer to emulating her. "
    m "Which means that {i}I’ll{/i} be cracking the whip before you even know it, Sensei. Now please, make yourself useful and take this off of my hands."
    s "..."
    m "I’m {i}waiting.{/i}"

    scene black
    with dissolve2
    play sound "tackle.mp3"

    s "{i}Hah...{/i}fine. But we’re taking it to the school."
    m "Fine by me. You’re the one doing all of the heavy lifting. Literally. {i}And{/i} I’m still dressed for the part."

    play sound "static.mp3"
    scene mayaboxwaitwhat11 with flash
    stop sound

    s "Why {i}are{/i} you still wearing your uniform anyway?"
    m "I wanted to be ready in case we randomly crossed paths. I didn’t want to risk dressing like an adult and having you suddenly not like me anymore."
    s "I don’t think adults wear bells around their neck."

    scene mayaboxwaitwhat12
    with dissolve

    m "They do when their pervert boyfriends buy them as gifts. Did I ever say thank you for that, by the way?"
    s "I wouldn’t remember even if you had."
    m "Let’s just say I did then. And let’s {i}also{/i} say that I still have a few {i}other{/i} things you bought me for the same creepy purposes."
    s "..."
    s "You have what now?"

    scene mayaboxwaitwhat13
    with dissolve

    m "Oooooh? Did {i}your{/i} Maya keep her sexy cosplay closet a secret? But you spent so much money on it."
    s "You...you have a secret sexy cosplay closet?"
    m "You’re more than welcome to raid it with me once you accept me for who I am and stop trying to turn me into your comfortably numb dream-girl thing."

    scene mayaboxwaitwhat14
    with dissolve

    s "{i}Fucking Maya...{/i}of course she’d hide that from me. There’d be no holding me back at all if I ever found out."
    m "Sounds like you and I would have been reacquainted much sooner if you did. So I guess I’ll go ahead and be mad at her too."

    scene mayaboxwaitwhat15
    with dissolve

    s "Can I...ask you something?"
    m "I already told you. I don’t know what’s in the box."
    s "Not that. Just...did giving up on me ever cross your mind this past year? Did you {i}not{/i} lose hope in me at any point?"
    m "Of course not. {i}Losing{/i} hope would imply that I ever had any hope in you to begin with. And that’s just dumb."
    s "Seriously, though...did you ever think about just...trying to find someone else?"
    m "Romantically? No. I want you, so I am going to {i}have{/i} you because I am cute and that entitles me to getting whatever it is I want."

    scene mayaboxwaitwhat16
    with dissolve

    m "I {i}did{/i} have a sex dream about Otoha once, though. So you can go ahead and call that some sort of {i}forbidden desire{/i} if that turns you on or something."
    s "It’s fine. I, too, have had sex dreams about Otoha."

    scene mayaboxwaitwhat17
    with dissolve

    m "You {i}bastard.{/i} I am {i}right{/i} here. Have you no consideration whatsoever for my feelings?"
    s "..."
    s "I can’t tell if you’re being serious or not."

    scene mayaboxwaitwhat18
    with dissolve

    m "There’s a little bit of truth in every single lie, you know?  I won’t let myself get beat up over it, though. "

    scene mayaboxwaitwhat19
    with dissolve2

    m "I know I’ve got my work cut out for me if I’m going to find myself on the same level as all of the girls you’re currently sleeping with who {i}haven’t{/i} disappeared at some point."
    m "But I’ll get there. I’ll get there and you’ll see why you chose {i}me{/i} as “the one” long before you even {i}met{/i} any of those girls."
    m "Then things will be good again. And we can go back to normal. Or {i}change{/i} what’s normal if that’s really what you want. "
    m "It’s like falling in love all over. I should feel {i}lucky{/i} I get to experience that again. "

    scene mayaboxwaitwhat20
    with dissolve2

    m "But instead, I’m just sad."
    s "..."
    m "I miss you, Sensei. "
    s "..."
    s "Maya-"

    scene mayaboxwaitwhat21
    with dissolve
    play sound "footsteps.mp3"

    m "Come on! Let’s get that box to school for whatever reason we’re supposed to take it there!"
    s "..."

    scene black
    with dissolve2

    s "{i}Hah...{/i}yeah. "
    s "{i}I’m right behind you.{/i}"

    "........."
    "......"
    "..."

    scene mayaboxwaitwhat22
    with dissolve2

    m "Wow. This place is actually kind of creepy at night."
    s "You should see it when it’s all red and crawling with weird, paranormal entities."
    m "Do I have to? That sounds like it sucks."
    s "I wouldn’t say you {i}have{/i} to. Just know that if you do, it’s actually a good thing because it means you can start learning more about how the world works."
    s "Or...{i}doesn’t{/i} work. It’s complicated."
    m "More...time stuff...right? Things that {i}your{/i} me was interested in?"

    scene mayaboxwaitwhat23
    with dissolve

    s "I’m not really sure how much of it was interest and...how much was just a result of her being forced to endure it for so long."
    m "Well, for what it’s worth, I {i}am{/i} interested in that stuff. Sci-fi. Quantum physics. But it’s all more fiction-focused than anything involving actual science."
    m "But I blame you for that. You and Billy Pilgrim. "

    scene mayaboxwaitwhat24
    with dissolve

    s "Me?"
    m "Mhm. You and the high school curriculum you forced onto a child because you were so starved for an actual intellectual conversation after your sex-mom died."

    scene mayaboxwaitwhat25
    with dissolve

    s "Well, that sentence hit me like a truck."
    m "There’s another joke to be made here, but I think that one might be pushing it a bit."
    s "I’d appreciate it if you wouldn’t call her a “sex-mom” in the future. She was...a lot more than that, Maya."
    m "Right. Just like how {i}you{/i} are more to me than what you tell yourself you are. "
    m "So please don’t die, for I have seen what I would turn into and it is not pretty. If nothing else, try living for that."

    scene mayaboxwaitwhat26
    with dissolve2

    s "..."
    m "..."
    s "I’m..."
    s "I’m gonna go stash this in the room beside you. I’m pretty sure...{i}that{/i} was the one we always put them in."
    m "Okay...I’ll be here. "

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "I slide open the door to an empty classroom and drop the box off in the corner, trying (and failing) once more to open it."
    "I want to stay here. "
    "Not {i}just{/i} so I don’t have to go back out into the hall and face the fact that even {i}this{/i} version of her — who smiles and {i}speaks{/i} to me — is one I want to enrapture..."
    "But to figure out {i}what{/i} this is. And how {i}Ami{/i} is somehow involved now."
    "Why would {i}she{/i} ask Maya to take this here? Why can’t {i}Maya{/i} open it either?"
    "Was that...always how it worked?"
    "Was that just something else she hid from me?"
    "If I stay here, maybe I can see what happens."
    "Maybe I can see who comes to take this to wherever it’s meant to be- because it most assuredly isn’t the first. And it most assuredly won’t be the last."
    "If I never leave, though..."
    "I’ll never see that smile again."

    play sound "static.mp3"
    scene mayaboxwaitwhat27 with flash
    stop sound

    "And I’ll also never figure out what’s inside of the apparent sex closet — which is now, unfortunately, a top priority for me."
    "Right after I figure out why Maya dragged me back into my old classroom."

    m "Been a while, hasn’t it?"
    s "And for good reason. I was never fit to be a high school teacher."
    m "You sure weren’t, Sensei. And anyone who’d pay you to hang out with teenage girls clearly isn’t fit to serve this community either."
    s "That was the part where most other people try to say something uplifting about how my methods are “unusual” but how I’ve wound up helping in the long run."
    m "Then I guess I don’t need to say anything because I’m living proof of that."
    m "Everything I am is because of you. And you have the rare opportunity right now to continue cultivating me. To make me something even {i}bigger.{/i}"

    scene mayaboxwaitwhat28
    with dissolve2

    m "So come — over here. To my desk. "

    scene mayaboxwaitwhat29
    with dissolve2

    m "Teach me more about who I’ll be next. About what you {i}want{/i} the result of the “Maya Raising Project” to be."
    s "I want you to be whatever makes you happy."
    m "Hahah. Cute. But really — what do you {i}really{/i} want?"
    m "An actor? Want me to perfectly mimic your last true love? Recite her lines like they’re my own? Even if they {i}are{/i} my own. Which they are. Because again, same person."
    m "Or maybe someone even smarter than you? Someone like {i}her.{/i} The {i}first{/i} girl you lost."
    m "Just, whatever you do, don’t ask me to be an idol because I fucking {i}hate{/i} Niki and I fucking {i}hate{/i} her annoying bitch of a sister."
    s "I don’t know. I kind of want to see idol Maya now. Is there something like that in the sex closet?"

    scene mayaboxwaitwhat30
    with dissolve

    m "There {i}sure{/i} is. It just brings back bad memories."
    s "Was I too rough on you while you were wearing it?"
    m "Worse. You started crying."
    s "Oh. "
    s "Well, I’ve gotten more used to banging idols since then, so maybe that won’t happen anymore?"

    scene mayaboxwaitwhat31
    with dissolve

    m "Again. I am {i}right{/i} here. And {i}still{/i} very much upset over the fact that your childhood friend is now sleeping in the same bed as you, thank you very much."
    s "So is it {i}her{/i} you hate more? Or Noriko?"

    scene mayaboxwaitwhat32
    with dissolve

    m "How is that relevant?! Aren’t you supposed to be teaching me about “old” Maya?!"
    s "Old Maya hated both of them too and it was always sort of a touchy subject. "
    m "It’s a touchy subject {i}now{/i} too! So why do {i}I{/i} have to be the one to do it?!"
    s "Because I can no longer be gaslit into thinking that information may cause both the universe and {i}me{/i} to explode."

    scene mayaboxwaitwhat33
    with dissolve

    m "Fine. You caught me. It is I — Maya prime. I never disappeared at all. I just faked it for attention. Guess we have to have sex now. Oh well. "
    m "Wake me up when it’s over. I’ll be thinking about time and stuff."
    s "Close, but you’re not there yet. "
    m "Fuck."
    s "You really won’t talk about it? "

    scene mayaboxwaitwhat34
    with dissolve

    m "Sensei — I’m {i}bad{/i} at talking. I don’t know how else to get that through to you. Like, fuck- all this banter alone is enough to make my head hurt."
    s "Then why-"
    m "I said it earlier. Because I {i}miss{/i} you. "

    scene mayaboxwaitwhat35
    with dissolve

    m "When I sit down and try to remember literally {i}anything{/i} about {i}any{/i} part of my life — {i}you’re{/i} there. You have {i}always{/i} been there."
    m "So going this long without you and having to learn how to function as an actual independent person has been fucking {i}bullshit.{/i} "
    m "{size=-2}Which I’m sure you’ll give me shit about since you always talked about how {i}important{/i} that was during tutoring, but whatever. I’ve never really {i}wanted{/i} to be my own thing since meeting you in the first place.{/size}"
    m "So yeah, I’ll talk to you. I’ll talk your ear off because I’m just excited to be {i}near{/i} you again. I’m excited you’ll {i}listen.{/i}"

    scene mayaboxwaitwhat36
    with dissolve

    m "But that doesn’t mean it’s easy...even if it sounds like it is. Even if it {i}looks{/i} like it is. Because things aren’t always exactly as they seem."
    m "You should know that much...right?"
    s "..."
    s "Yeah...I know that much."
    m "So can we...maybe wait on the whole Nakayama discussion? Until {i}after{/i} I’ve gotten less sour about how {i}she’s{/i} your number one now and I’m just...{i}there.{/i}"
    s "I never said she was my number one, Maya."

    scene mayaboxwaitwhat37
    with dissolve

    m "She fucking sleeps in your bed, Sensei..."
    m "She’s the first person to see you every single day. I’m lucky if I even {i}do.{/i}"
    s "Then I’ll see you more. Starting right now."

    scene mayaboxwaitwhat38
    with dissolve2

    m "You..."
    m "You {i}will?{/i}"
    s "I will."
    m "You’re not...just saying that to shut me up?"
    s "No...I’m not."
    s "I’m ready to start...moving on. Or trying to. I can’t stay hung up on the memories of you when..."
    m "When...what?"
    s "When there’s a chance they might come back. That they’re...still in there somewhere. Like mine were."
    m "..."
    s "Just...mine were of...this same timeline. And yours would be of...probably millions."
    m "..."
    s "That’s not the answer you wanted to hear, is it?"
    m "I’d have liked something more normal there, I think. Now I just have to worry about what would happen to me if I suddenly had millions of years worth of memories."
    m "Memories {i}without{/i} you. Memories of {i}looking{/i} for you. When I just told you minutes ago that you’re {i}there{/i} for all of mine."
    m "You want me to lose that?..."
    s "I...well..."
    m "Can you just tell me you love me instead?"
    s "..."

    scene mayaboxwaitwhat39
    with dissolve2

    m "Or...something {i}close{/i} at least."
    s "..."
    m "..."
    s "Natsume Sōseki."

    scene mayaboxwaitwhat40
    with dissolve2

    m "...I’m sorry?"
    s "You know that one line, right? The one people are always using to say a thing {i}without{/i} saying a thing."
    m "I do..."
    m "You’re not...going to say {i}that{/i} thing, though?"
    s "Nope. Everybody says {i}that{/i} thing now. So I’m just going to say the author’s name and you’re going to have to deal with it."

    scene mayaboxwaitwhat41
    with dissolve

    m "Heh..."
    m "I’ll take it..."
    m "I hope you know I’m...gonna hold you to that whole “seeing me more” thing too. Like...don’t be surprised if I’m just...there when you wake up one day."
    s "Next to Niki?"

    scene mayaboxwaitwhat42
    with dissolve

    m "Yeah. I can show her how it’s done. Then she’ll feel so bad about her own abilities that she’ll be forced to move out and {i}I{/i} can move in instead."
    s "Yeah. I’m sure Ami would {i}love{/i} that."
    m "Fuck Ami."
    s "I’m sure Ami would love {i}that{/i} too."

    scene mayaboxwaitwhat43
    with dissolve
    stop music fadeout 10.0

    m "Heheh...probably {i}too{/i} much."
    s "..."
    m "..."

    "We stand there...just staring at each other for a while. Wanting more, but taking nothing."
    "It feels kind of strange — the way we’re watched by the moon. And how it dissuades me from grabbing her wrist and pulling her back to my home right now. "
    "I think..."
    "I think there’s somewhere else I want to take her instead, though."

    m "..."
    s "Maya."
    m "Sensei."
    s "Are you hungry?"

    scene black
    with dissolve2

    m "Always."

    $ renpy.end_replay()
    $ mayaspring1 = True
    $ maya_love += 1

    "........."
    "......"
    "..."

    jump mayaspring2

label mayaspring2:
    scene clearnightsky
    with dissolve2
    play music "sensei.mp3"

    "I can count the amount of “dates” I went on with {i}my{/i} Maya on one hand. Though I’m not sure she’d call them that if she were still here today."
    "Since she’s not, though, I feel as if I can safely label that night at the takoyaki stand as our first without incurring any more ghostly wrath than I already do on a nightly basis."
    "Come to think of it, a second haunting might be nice — even if I doubt Maya and Sekai would get along very well."
    "They wouldn’t need to, though. I’m sure I could figure out how to ration my time in between the secret resurrection studies I’ve been partaking in behind your back."
    "It’s only a matter of time now. Not until I succeed — until I become one of them. And there’s no longer any need to study at all."
    "But it’s precisely {i}because{/i} it’s a matter of time that I feel confident when I tell you it is so far away that you’ll likely be gone before I reach it."
    "And {i}I{/i} probably won’t remember ever telling you this at all."

    scene black
    with dissolve2

    "There’s a hand to my side that doesn’t belong to me."
    "It keeps brushing up against mine as if it’s asking for something — but it’s an unwelcome sensation that does little but annoy me and cause me to move aside by half a step."
    "Not enough to make it obvious that I’m rejecting it, but enough {i}to{/i} reject it while still leaving room for a little wishful thinking to fill her thoughts in place of my appendage."
    "This is only our second first-date after all. It’s only right to wait at least one more before we touch."
    "Which ignores all of the angry, begrudging sex I have already had with her. But that’s something {i}else{/i} I’m trying to look past too."
    "I just won’t know what sorts of wonders a second first-fuck will be until after the second first-date."
    "But will a second first-box and the encroaching second first-meal we’ll share dilute or distort any of these new memories to the point where keeping them isn’t worth the risk?"
    "I wonder if she asked herself the same thing when {i}she{/i} was taking me here?"
    "How annoying it is to have the roles reversed."
    "No wonder why she was always so angry."

    play sound "static.mp3"
    scene mayatakoagain1 with flash
    stop sound

    m "Do you want anything?"
    s "You mean you’ll let me buy myself food with my own money?"
    m "I think I’m supposed to. That seems like proper date etiquette to me."

    "The old man behind the counter grunts. I doubt I’ll ever hear anything else from him."

    m "We could also go out to a restaurant instead if you’d rather-"
    s "No. It has to be here."

    scene mayatakoagain2
    with dissolve

    m "{i}Has{/i} to? Why does it {i}have{/i} to be here?"

    "The old man grunts again."

    scene mayatakoagain3
    with dissolve

    m "And why does he keep doing that?"
    s "It’s how he communicates, I think. Like Yasu with her incessant ramblings about God and...{i}old{/i} Maya with her incessant ramblings about how disgusting I am."

    scene mayatakoagain4
    with dissolve

    m "She had a point. You {i}are{/i} pretty disgusting."
    s "Don’t say that line. You haven’t earned it yet."

    play sound "static.mp3"
    scene mayatakoagain5 with flash
    stop sound

    m "Are you seriously telling me I have to earn the right to say my own lines? Because I get being enamored, but this is just sad."
    s "Then, to even the playing field, I hereby grant you permission to ban me from saying one thing {i}your{/i} version of me frequently said to you. That way, we’ll both be happy."
    m "Great. Then I hereby ban you from saying “no.” Would you like to go fornicate behind a tree now?"
    s "No."
    m "You bastard. You’ve already broken the rules."

    scene mayatakoagain6
    with dissolve

    s "This agreement was voided from the get-go since there’s basically no way I’d have ever said “no” to you to begin with. "
    m "I’m sure it happened once or twice."

    "The old man grunts again, this time with slightly more fervor or feeling than before."

    scene mayatakoagain7
    with dissolve

    m "Oh. I guess we should probably order."
    s "That is what we’re supposed to do here, yes. But it’s not like this guy has anything else going on. He probably enjoys the-"

    "Another grunt. Something tells me I will die after the next."

    s "Just give us the usual please."
    m "There’s only one thing on the menu. I think this is more of a {i}quantity{/i} problem than him not knowing what to give us."
    s "Then — enough to feed five to ten girls, please."

    scene mayatakoagain8
    with dissolve

    m "You’re not planning on inviting others, are you?"
    s "No. I just know you well and don’t feel like spending enough to feed {i}twenty{/i} girls. Ten seemed like a fair compromise."
    m "How very kind of you. Perhaps once we’re done, I’ll let you fornicate with me behind a tree completely free of charge."
    s "Are you a prostitute now?"

    scene mayatakoagain9
    with dissolve

    m "Yes. Please hurry, takoyaki man. I’m a poor high school girl and I need to go have sex with this adult man for money."
    s "I’d be worried if I wasn’t partially convinced this guy is actually a robot."

    scene mayatakoagain10
    with dissolve

    m "{i}I’m{/i} not entirely convinced that we’re {i}all{/i} not actually robots. And that our whole lives are some weird simulation about AI obtaining actual intelligence or something."
    s "My Maya’s theories were way better than that. And that’s saying a lot since practically all of them were wrong."
    m "I take great offense to this. If there is anything I know about myself, it is that I am always right. And if there is anything I know about you-"

    scene mayatakoagain11
    with hpunch

    "A fifth grunt from the old man. This is where I die."

    play sound "static.mp3"
    scene mayatakoagain12 with flash
    stop sound

    "Or perhaps just relocate to a bench to continue feeding into the undeniable yet tragically painful chemistry I have with this creature."
    "For it truly feels as if we have known each other forever. But {i}this{/i} forever has only lasted a little over a year."
    "And while that’s more than many get, it’s hard to say it feels like {i}anything{/i} when I never thought that Maya was going to leave {i}me{/i} in the first place."
    "Even {i}with{/i} all of the warnings that are now...racing back to me in hindsight. "
    "That isn’t {i}all{/i} that’s racing back, though. There’s hope, too. There’s-"

    m "Feed me."
    s "..."
    m "Feed me and I’ll let you fornicate with me behind a tree."
    s "What is it with you and this tree thing all of a sudden?"
    m "I don’t really know. The first time was just a joke but, the more I say it, the more it sounds kind of fun. "
    m "You can also just feed me without the promise of sex, though. Anything to get those hot balls inside of my mouth."
    s "..."
    m "..."
    s "Yeah, I think this date thing was actually a bad idea after all."

    scene mayatakoagain13
    with dissolve

    m "Fine. Then you leave me no choice but to revert to my {i}former{/i} self since {i}that{/i} is the one you have apparently decided to latch onto."
    m "Assuming of course that a man of your supreme idiocy and undeniable general grossness is capable of latching onto any {i}one{/i} thing to begin with."
    m "Which implies, of course, that I believe I’d be extremely well fed if only I was an entire group of teenagers rather than just one unfortunate, yet immensely adorable girl."
    s "..."
    m "You’re disgusting."

    scene mayatakoagain14
    with dissolve

    s "Fine. I’ll feed you so long as it gets you to stop trying to be {i}her.{/i}"
    m "Wait. Now I’m confused. Don’t you {i}want{/i} me to be her? Isn’t that your entire goal in talking to me again? "
    s "It’s...a little more complicated than that."

    scene mayatakoagain15
    with dissolve

    m "I’m very interested in whatever that might possibly mean. But I’m also very hungry and I don’t know which feeling to prioritize."

    scene mayatakoagain16
    with dissolve

    s "Well you can take your time if- oh. I guess you’ve already figured it out."
    m "Food now, talk later. I have made up my mind."
    s "At least we know there’s no food in those mysterious boxes since I imagine you would have found a way to tear them open earlier."
    m "Aaaaaaah~"

    scene mayatakoagain17
    with dissolve

    s "..."
    m "Aaaaaaaahhhhh~"
    s "..."

    scene mayatakoagain18
    with dissolve

    m "AAAAAAAAAAAAHHHHHH!"
    s "Sorry. This just...feels really weird. "

    scene mayatakoagain19
    with dissolve

    m "To be completely honest, I agree. We’re being so cute right now that I imagine we must look like an actual couple. "
    s "I think you’re doing the heavy lifting in the cuteness department. I’m kind of just...here."
    m "True. I didn’t want to be the one to say it, though."

    play sound "static.mp3"
    scene mayatakoagain20 with flash
    stop sound

    m "But on the bright side, at least being next to me makes you look better."
    s "Or {i}worse{/i} when you’re telling strangers that I’m paying you to have sex with me."
    m "Doubtful. A girl like me could bring in a lot of money, Sensei. People might think you’re rich if I keep telling them that."
    m "It’s a vast departure from that whole “pretend we don’t know or like each other” thing. But hey, I got used to that and I can get used to this too."
    s "Did I...{i}really{/i} make you do that?"

    scene mayatakoagain21
    with dissolve

    m "Well...yeah. It’s not like you forced it on me, though. It was my idea."
    s "But why would you-"
    m "It’s just easier that way. You don’t have to deal with people knowing your proclivities and {i}I{/i} don’t have to deal with a parade of teenagers also trying to bone you."
    s "You mostly just mean Ami, don’t you?"
    m "I mostly just mean Ami, yes."

    scene mayatakoagain22
    with dissolve

    m "But now {i}she{/i} knows fucking everything ever and you’re {i}fucking{/i} everyone ever, so...why bother continuing to handicap myself?"
    m "Especially if you’re going to, like...try to see me more...and stuff."
    s "..."
    m "..."
    s "You really suffered for me, didn’t you?"

    scene mayatakoagain23
    with dissolve

    m "Not until you started fucking ignoring me, asshole. This whole “suffering” thing is still new to me.  And, I’ll tell you what, Sensei- I’m not cut out for it."
    s "Well, I’ve got bad news for you then. Because-"

    scene mayatakoagain24
    with dissolve

    m "{size=-1}Yeah, whatever. Before you start with that whole “just being with me is suffering” nonsense, let me remind you that you’ve been saying that forever and it has literally never been an issue.{/size}"
    m "Unless you’ve, like...{i}actually{/i} been cheating on me this entire time and were just really good at hiding it. But I’m pretty sure that’s, like a...{i}your{/i} world thing."
    s "Wait, so...you’re conceding that this world is {i}my{/i} world? That you’re not supposed to be here?"

    scene mayatakoagain25
    with dissolve

    m "Now- I didn’t say that I’m not supposed to be here. But with all of the weird shit that’s been happening and everything I’ve heard from you {i}and{/i} Ayane?"
    m "It’s pretty much impossible to convince myself at this point that the world is what I thought it was."
    s "..."
    m "..."
    m "You should applaud me for how perceptive and smart I am now."
    s "Sorry...it’s just..."
    s "It’s weird that you can...{i}know{/i} this much despite not having been to the rooftop with us. "
    s "You shouldn’t have retained any of that, Maya. Everything Ayane and I told you should have been purged after Halloween."

    scene mayatakoagain26
    with dissolve

    m "Ugh. I wish it {i}was.{/i} Everything’s so...weird now. And...scary."

    scene mayatakoagain27
    with dissolve

    m "But I...care less about that right now and...more about just getting {i}you{/i} back."
    m "Because {i}you{/i} are my coping mechanism, Sensei. {i}You{/i} are the box I’ve stored all of my feelings in. And there’s not a chance in hell I could confront any of this without you."
    s "You...want to confront it then?"
    m "Well, to be fair, I still don’t really know what it {i}is{/i} we’re confronting. But yes. Whatever it is, I want to do it with you."
    m "I’m just..."
    s "..."

    scene mayatakoagain28
    with dissolve

    m "{i}Hah...{/i}"
    m "All this...paranormal stuff if...that’s what you want to call it..."
    m "It’s all making me feel less...{i}permanent{/i} than I want to feel."
    m "Like...what if I {i}do{/i} get to keep going? What if you fall back in love with {i}me?{/i} And everything’s normal and good again and you stop sleeping with other girls."
    s "Maya-"
    m "Shut up. I’m not done."
    m "What if all of that happens and you lose me {i}again?{/i} Or I lose {i}you?{/i} Or we {i}both{/i} get lost somehow? Or, even worse, what if you {i}never{/i} stop sleeping with other girls?"
    s "Maya-"
    m "Again, shut up. You seriously need to stop interrupting me. And also sleeping with other girls."

    scene mayatakoagain29
    with dissolve

    m "Oh. If you can’t tell, I’m also really annoyed that you keep sleeping with other girls. "
    s "I...had a feeling."
    m "Point is, Sensei...there’s still so much I don’t know. And I don’t want you to put too much faith into me {i}getting it{/i} just because I’ve gotten it in the past or...future?"
    m "I don’t know where...{i}your{/i} me is from on a technical level. But it kind of sounds like both in a way?"
    s "I think it kind of {i}is{/i} both in a way. Because she existed before you chronologically, but then obviously lasted {i}way{/i} longer than you have."
    m "What do you think was happening with my consciousness in the meantime then?"
    s "I don’t know, but...I imagine the other Maya would have come up with something about timelines or...yeah. You were probably just...somewhere else."

    scene mayatakoagain30
    with dissolve

    m "...Somewhere else, huh?"
    s "Yeah...or something like that."
    m "Has that...ever happened to you, Sensei?"
    m "Have you ever just...been somewhere else all of a sudden? Or maybe...some...{i}when{/i} else?..."
    s "I..."

    play sound "static.mp3"
    scene amisfunpartynight4 with flash
    scene amisfunpartynight39 with flash
    scene makotosekai33 with flash
    scene okayitsgametimeagain1 with flash
    scene mayatakoagain30 with flash
    stop sound

    s "I..."
    s "Probably...yeah."
    s "It’s kind of...hard to remember, though. Like...it seems like it’s {i}there{/i} but...fuzzy."
    m "Mm..."
    m "Do you {i}want{/i} to remember? Or do you think everything would just get even {i}more{/i} confusing if you did?"
    s "Everything always gets more confusing here. That’s just the way this world works, I think."
    m "That’s another thing I’m afraid of. Because I know you’re hoping somewhere deep down that {i}I{/i} will remember things that happened with the me who isn’t me."
    m "And while I know that might feel real to you...for me, I..."
    m "Well..."
    s "..."
    m "..."
    s "You know...I often wish I didn’t have to remember Sekai."
    m "Well, duh. That’s basically the only reason we’re together. "
    s "But I often {i}also{/i} think that one day, remembering her might actually be {i}good.{/i} And I might become stronger for it."

    scene mayatakoagain31
    with dissolve

    m "HA! No you don’t, you fucking liar! The day you’re that optimistic about anything is the day I give up watermelon."
    s "Heh...you’re right. "

    scene clearnightsky
    with dissolve2

    s "Wouldn’t it be nice if you weren’t, though?"
    m "Yeah. But I think there are a lot of things out there that {i}would{/i} be nice. And that chances are, we won’t ever get to see or experience the vast majority of them."
    s "Well hey, that’s {i}one{/i} potential perk of an infinite life if we’re able to hang on. We might {i}actually{/i} get to see...{i}everything.{/i}"
    m "Yeah...maybe."
    m "But {i}then{/i} what?..."
    m "What else is there to see when we’ve already seen everything? What else is there to {i}do{/i} when we’ve already done it all?"
    m "Is {i}that{/i} the end of the world? "
    m "Is that what {i}she{/i} saw?"
    s "I don’t think so..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    s "The end of the world is a little more colorful than that."

    "There’s a hand to my side that doesn’t belong to me."
    "But when it reaches for something that {i}does{/i} — a cardboard boat of fried octopus that is likely only {i}somewhat{/i} scorching now — I do something."
    "I grab it."
    "Her hand — not the takoyaki."
    "And when I grab it, there’s this...pause. "
    "Silence. "
    "She stares down at our hands for a moment, the same as me, and my mind once again gravitates to the size disparity between the two."
    "But then she tilts her head up and her eyes meet mine."
    "And we just sit there for a full minute looking at each other."
    "We aren’t smiling. We aren’t speaking. "
    "We’re just...connecting."
    "And it’s the most unfaithful I have ever felt. "

    $ renpy.end_replay()
    $ mayaspring2 = True
    $ maya_love += 1

    "........."
    "......"
    "..."

    jump mayaspring3

label mayaspring3:
    play sound "static.mp3"
    scene mayainvdorm1 with flash
    stop sound
    play music "shrinemaiden.mp3"

    "So of course that unfaithfulness ultimately led me here — to the wrong side of something familiar. Just a step or two away from another instance of impulse disguised as fate."
    "{size=-1}I don’t like her smile. I don’t like how her flesh is still warm when it should feel like porcelain. I don’t like that ribbon. I don’t like her eyes. How she doesn’t blink as much as she’s meant to.{/size}"
    "I love it. "
    "And that’s far worse and far heavier than any amount of disdain, understandable or not, could ever be."

    m "So, assuming your dreadful niece hasn’t left another package for me to deliver, would you like to come inside and continue our date?"
    s "Daughter."

    scene mayainvdorm2
    with dissolve

    m "Fine. I can roleplay."
    s "No, Maya. I meant that Ami is my {i}daughter{/i} now. I don’t want you-"
    m "I know exactly what you meant. That’s why I tried to swiftly move past it with the offer of a charade you can’t possibly refuse."
    s "Just, I {i}can{/i} refuse."

    scene mayainvdorm3
    with dissolve

    m "Can you...{i}Daddy?{/i}"
    s "..."

    scene mayainvdorm4
    with dissolve

    m "Don’t just {i}ignore{/i} me, Daddy. I’ve waited all day for you to come home. And I’ve been {i}so{/i} lonely. Maybe we could-"
    s "Okay, fine. You win. I can’t refuse that. But I can’t refuse {i}you{/i} in general, so...this was unfair from the start."

    scene mayainvdorm5
    with dissolve

    m "You refuse me plenty. It’s actually quite annoying. You never {i}used{/i} to be like that. "
    m "It used to be like, “Hi, Maya. Sex?” And then I’d be like, “Indeed.” Then three minutes later I’d be all sticky and gross and need to take a shower."
    s "Three minutes? Really?"

    scene mayainvdorm6
    with dissolve

    m "Realistically, it’s probably closer to two. I just decided to include the extra sixty seconds of you hovering above me once you’ve finished to make you feel better about yourself."
    s "How kind of you..."

    scene mayainvdorm1
    with dissolve

    m "Are you coming in or not? "
    m "Because I may not have a tree for you to fuck me up against, but I {i}do{/i} have all of those costumes I alluded to earlier which I will gladly let you choose from."
    s "..."

    scene mayainvdorm7
    with dissolve

    m "Or I guess I can just act disinterested since that seems to turn you on better than anything nowadays. You’re disgusting."
    s "Okay, you win. Hi, Maya. Sex?"

    scene mayainvdorm8
    with dissolve

    m "I suppose I can indulge your perverted desires if it means making you slightly less incorrigible in the near future."
    s "I think you were supposed to just say “indeed.”"
    m "And I think {i}you{/i} should be spending more time with girls you wouldn’t get arrested for merely looking at."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    m "Alas — my bad luck must continue and I must now spread my legs for what I can only imagine is-"
    s "You don’t need to imagine anything, Maya. You know exactly how big my-"

    stop music
    play sound "static.mp3"
    scene mayainvdorm9 with flash
    stop sound

    se "Hi, Aki-kun! Long time, no see."
    s "..."
    m "Ami..."
    a "How big your {i}what{/i} is, Dad?"
    s "Uhh...hi...Ami..."
    s "I...didn’t really expect you to...be here."

    scene mayainvdorm10
    with dissolve

    a "Yeah, well, I was tired of listening to you fuck Niki’s brains out every night. So I figured I’d come spend the night here to give myself a break from all of that."

    scene mayainvdorm11
    with dissolve

    a "Oh, and Maya’s here too. Sorry if that was a little abrasive."

    play sound "static.mp3"
    scene mayainvdorm12 with flash
    stop sound
    play music "thingsthathurt.mp3"

    m "Why...are you here?"
    a "Hm? Because we share this dorm room, silly. "
    m "Yes. But you {i}specifically{/i} told me earlier that you would not {i}be{/i} here tonight. You know, like how you’re {i}never{/i} here at {i}all{/i} anymore."
    a "{size=-1}To be completely fair, Maya, it should have been a dead giveaway that I {i}would{/i} show up when I went out of my way to tell you I wouldn’t. Since that’s been the norm and all.{/size}"

    scene mayainvdorm13
    with dissolve

    m "Yeah! Maybe if you didn’t {i}also{/i} fucking tell me that the reason I had to do your stupid, box-based chores was because you were busy!"

    play sound "static.mp3"
    scene mayainvdorm14 with flash
    stop sound

    a "Oh yeah. I did say that, didn’t I? Wow. Maybe I {i}am{/i} the bad guy here after all then?"
    m "You think?!"
    se "Ew — Aki-kun, you’re not planning on fucking that...{i}thing{/i} you dragged in, are you? I taught you better than that."

    scene mayainvdorm15
    with dissolve

    s "..."
    se "Oh, right. If you talk to me with Ami around, she might lash out. Good thinking, Aki-kun."
    se "But seriously though, are you really gonna fuck that thing?"
    a "Sorry — were you guys planning on having sex tonight?"

    scene mayainvdorm16
    with dissolve

    se "Oh, yay! She’s just like me!"

    play sound "static.mp3"
    scene mayainvdorm17 with flash
    stop sound

    m "If we were, would that be a problem?"
    m "I figure letting me fuck your dad is the least you can do since you’re going to make me do all {i}sorts{/i} of shit now, Ami. That sounds fair, right?"
    a "Oh, yay! You think I’m his daughter again. I could have sworn I heard you call me his niece just a minute ago. But yeah! Go for it."
    m "Yeah, I didn’t think-"

    scene mayainvdorm18
    with dissolve

    m "Wait, really?"
    a "Yeah. I won’t get in the way. I’ll probably touch myself, though. But only if you guys are okay with that."

    scene mayainvdorm19
    with dissolve

    m "..."
    s "..."
    m "I mean...I won’t say I’m {i}against{/i} it..."
    s "On second thought...I should probably just...go."

    scene mayainvdorm20
    with dissolve

    m "But...things were going so well! And you said it yourself that you would try and spend more time with me! Don’t let Ami’s fucking...creepiness get in the way of that!"
    a "Hey! My creepiness has been mostly unobtrusive lately! I take offense to that!"

    scene mayainvdorm21
    with dissolve

    m "Unobtrusive?! That’s what you call it?! Getting in the way of my personal life just to fuck with me?! Because that sounds pretty {i}obtrusive{/i} to me, Ami!"

    play sound "static.mp3"
    scene mayainvdorm22 with flash
    stop sound

    se "Again — why does it have to be so nasty?"
    a "I’m not getting in the way of anything, though. I just said you guys can go at it and I won’t interfere. I’ll just masturbate. "
    a "Which is probably what I was going to do tonight anyway since I could smell that my dad was in the hall at some point and it turned me on."

    scene mayainvdorm23
    with dissolve

    a "I’ll be more than happy to join in if you’ll let me, though! I’ve just never touched a girl before, so forgive me if I do anything wrong."
    m "Sensei-"

    play sound "dooropen.mp3"
    scene mayainvdorm24 with dissolve

    s "Rain check, Maya. I’m just...not in the mood for this anymore."
    m "Wait! I’ll come with you! I don’t-"
    s "Just...rain check. Okay?"
    se "{i}Hah...{/i}alone again. Being dead is so depressing sometimes."
    a "Aww, man. I was really looking forward to watching you guys. "
    a "I can only imagine how intense the sex is if the sheer desire for it can give you strength even when the world around you is tearing into pieces."

    play sound "static.mp3"
    scene mayainvdorm25 with flash
    stop sound

    m "I’M FUCKING TIRED OF THIS, AMI! JUST TELL ME WHAT YOU WANT FROM ME! STOP TREATING ME LIKE YOUR FUCKING PUPPET!"
    a "You’re not a puppet, you’re a doll. Dolls are much cuter."
    m "JUST FUCKING LEAVE ME ALONE! I WANT TO LIVE MY LIFE! I WANT TO BE WITH SENSEI! AND I FINALLY HAD ANOTHER CHANCE TONIGHT AND YOU-"
    a "Enabled it?"

    scene mayainvdorm26
    with dissolve

    m "...What?"
    a "Well...think about it. If I don’t tell you to dispose of that box, Sensei’s never rocked by his emotional connection to it."
    a "Then the two of you {i}don’t{/i} use the rest of the night to start repairing the broken bridge that is your relationship and go eat takoyaki and stuff."
    m "How do you know about the takoyaki?"

    scene mayainvdorm27
    with dissolve

    a "Oh, that’s easy. Sensei isn’t good with technology, so I turned the “find my phone” feature on when I was helping him update his one night and then linked it to {i}my{/i} phone."
    a "Now I can see where he is at all times and don’t have to worry anymore!"
    m "..."
    a "Smart, right? Anyway, how was dinner?"
    m "You’re...keeping track of where he is?"

    scene mayainvdorm28
    with dissolve

    a "I feel like that’s actually one of the {i}less{/i} crazy things I’ve done. Just wait until you find out what I’ve put in his food."
    m "So is {i}he{/i} your doll too then?! Or is {i}he{/i} a puppet?! And what about everyone else?! Who do you want control of next?!"

    scene mayainvdorm29
    with dissolve

    a "Ayane would be nice. She keeps surprising me. Which is pretty weird given how long I’ve been doing this. "
    m "Here’s a new idea! Why don’t you just leave all of us alone?! I won’t let you torment me into keeping your fucking...reality-breaking secret anymore!"

    scene mayainvdorm30
    with dissolve

    a "I can tell based on how loud you’re being right now. I implore you to reconsider, though. At least if you want to keep thinking you’re actually {i}alive{/i} or whatever."
    m "I {i}am{/i} alive, though! I have feelings! I’m in love! I have needs and wants and connections and you’re trampling all over them by hanging your fucking...powers over my head!"
    a "I don’t {i}have{/i} powers. How many times do I have to tell you this?"

    scene mayainvdorm31
    with dissolve

    m "Well, until someone {i}else{/i} figures out how to pull me through different layers of reality or...timelines or...whatever that was, I’m going to keep assuming you do."
    m "But I’m not going to let the fear of that threaten me anymore. And I’m not going to keep doing your bidding just because I’m {i}afraid{/i} of you. "
    a "Is it just me or is this a bit of an overreaction to just being in the room while you want to fuck my dad?"

    scene mayainvdorm32
    with dissolve

    m "It’s more than that and you know it..."
    m "You’re supposed to be my best friend. We’re supposed to be in this {i}together.{/i} "
    m "But instead, you keep treating me like a pet you’ve locked in a cage. One you only take out when you want to trick yourself into thinking you can ever {i}care{/i} for anything."
    m "When, in all actuality, you’re just neglectful. You don’t actually {i}care{/i} about the things you look after. You care about feeling like you’re doing something {i}good.{/i} But you’re not."
    m "You hurt everyone by just fucking existing. You are {i}nothing{/i} like the Ami I know. Because the Ami I know wouldn’t ever hurt me on purpose. "
    m "And {i}you{/i} do it just for fun."
    a "..."
    m "..."
    a "Feel better?"
    m "Not really. No. "

    scene mayainvdorm33
    with dissolve

    a "Then why don’t you tell me what I can do to make up for how apparently horrible I am to you? Want me to go get the shackles again?"
    m "{i}You{/i} can’t do anything. But {i}I{/i} can."

    play sound "static.mp3"
    scene mayainvdorm34 with flash
    stop sound

    a "Oh? And what are {i}you{/i} going to do then?"
    m "Ever since Halloween...I’ve been keeping your secret because I’ve been afraid of what you’ll do to me if I {i}don’t.{/i} But that’s not going to get me anywhere."
    a "You’re going to tell Sensei then? That I’m a super-secret time traveling villain and not just a normal girl?"
    a "You gonna leave in the part where I made you cum your brains out too? Or does that one get to {i}stay{/i} secret since it makes you look like a filthy whore?"
    m "I’ll tell him everything...that part too."

    scene mayainvdorm35
    with dissolve

    a "Right. But, just out of curiosity, what exactly do you think this is going to accomplish? "
    a "Do you expect me to just {i}play nice{/i} once I’m dragged into this mess with you guys?  That I’ll stop being clingy and needy? What’s the end game here?"
    m "I don’t expect any of that...but I expect he’ll stop giving you everything you want just because your mom died."
    a "Sensei doesn’t give me everything I want because my mom died. He gives me everything I want because he loves me."
    a "And if you tell him I know more than he {i}thinks{/i} I know, do you know what’ll {i}really{/i} happen, Maya? "
    a "He’ll leave every single one of you. Just like he’d have done for the {i}last{/i} girl who lived inside of that skin. He’ll leave you and he’ll be with me. Just me. For the rest of time."
    m "Don’t play games with me, Ami. If that were true, you’d have fucking told him yourself. You wouldn’t turn down a world where it’s just you and him and you know it."
    a "You’re right. That would be my perfect world. And it’s exactly what I want. But you’re making me sound worse than I am again."

    play sound "static.mp3"
    scene mayainvdorm36 with flash
    stop sound

    a "If Sensei finds out I’ve known what’s been going on this whole time, do you have any idea how much he’ll suffer?"
    a "Do you have any idea how {i}terrible{/i} he’ll feel knowing I’ve had to look after myself this whole time while he refuses to come to grips with who he really is to me?"
    a "Do you {i}really{/i} think that what the two of {i}you{/i} share is stronger than that? Or do you think that maybe, deep down, what he wants is more than just {i}sex?{/i}"

    scene mayainvdorm37
    with dissolve2

    a "He wants to be happy. He wants a {i}family.{/i} He wants a normal life in a normal world where he doesn’t have to deal with {i}mistakes{/i} like you."
    a "{i}That{/i} is why I haven’t told him. Because, unlike you, I {i}don’t{/i} want to hurt him. And I {i}won’t{/i} make him suffer just so things will be easier for me."
    a "At least...not on a long-term basis."
    m "..."
    a "I’m not a bad person, Maya. I just do a lot of bad things. "

    play sound "static.mp3"
    scene mayainvdorm38 with flash
    stop sound

    a "Which, of course, means that I have no problem deleting you if you’re going to put his wellbeing in jeopardy like you say you are."
    m "D...Deleting?..."
    a "Words like “kill” are too heavy and dramatic to be wasted on those who have never been alive to begin with."
    a "And while I can’t reset you myself, I can sure find a way to make you {i}wish{/i} I could."
    m "..."
    a "Now, if you’re done with your little temper tantrum, do you want to watch a movie together or something?"
    m "A..."
    m "A...movie?..."
    m "But we...but I..."

    play sound "static.mp3"
    scene mayainvdorm39 with flash
    stop sound

    a "You let your emotions get in the way of what needs to be done."
    a "You can’t let that happen here. "
    m "..."
    a "I can teach you how to properly exist in this place, but not if you question me."
    m "So just...do as you say? No questions asked?..."
    m "I’m supposed to just...agree to that? And let you keep trampling all over the things {i}I{/i} want? The things that make {i}me{/i} happy?"
    a "It’s easier than you make it sound."

    stop music fadeout 8.0
    scene black
    with dissolve2

    a "Just want fewer things."

    $ renpy.end_replay()
    $ mayaspring3 = True
    $ maya_love += 1
    $ ami_love += 100

    "{i}Maya’s affection has increased by 1!{/i}"
    "{i}Ami’s affection has increased by 100!{/i}"
    "{i}She clearly loves you more!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
