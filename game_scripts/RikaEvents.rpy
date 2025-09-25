label rikadive:
    if rika_love >= 0 and rikaspecial2 == True and rikadive1 == False:
        jump rikadive1
    if chap4active == True:
        jump rikaspringdivegen
    else:
        jump rikadivegen

label rikadivegen:
    scene rikadivegen
    with fade
    play music "10c.mp3"

    "I make my way over to the dive bar and decide to spend most of the night conversing with Rika since Wakana and Imani are always too mean to me."
    "Thankfully, I'm pretty sure that Rika's brain is incapable of feeling whatever advanced emotions are required to make a person act maliciously, so things flow pretty naturally."
    "And by {i}naturally{/i} I mean that I receive a much-needed ego boost in the form of her thinking I am actually an effective teacher."
    "And while I'm sure that will change given that she's suddenly working in the same building as the rest of us, I can revel in her skewed perception for now-"
    "Because it's only a matter of time until she finds out who I really am."

    scene black
    with dissolve

    "As the night carries on, I allow my other coworkers to join in on my fun and exciting conversation with an apparent ex-activist under the pretense of them telling me how great I am."
    "They take this far too literally and there are very few sentences throughout the rest of my time in the bar that are {i}not{/i} padded with some sort of fake compliment."
    "But of course Rika, still incapable of ever catching onto anything, keeps talking to me the same exact way she always does."
    "And I feel comfortable, the same way I always {i}do.{/i}"
    "I'm hesitant to say it's her age or accompanying wisdom that manages to make me feel this way given that she both looks and acts at least twenty years younger-"
    "But there's something about her that just works for me."
    "And I'm glad I finally met her."

    $ wakana_love += 1
    $ imani_love += 1
    $ rika_love += 3

    "{i}Imani's affection has increased by 1!{/i}"
    "{i}Wakana's affection has increased by 1!{/i}"
    "{i}Rika's affection has increased by 3!{/i}"

    stop music fadeout 7.0

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label callrikamorning:
    play sound "phonebeep.wav"

    "I tap on Rika's name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    "There's no answer."
    "Guess I'll call someone else."

    jump callmorning

label callrikaafternoon:
    play sound "phonebeep.wav"

    "I tap on Rika's name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    "There's no answer."
    "Guess I'll call someone else."

    jump callafternoon

label callrikanight:
    if rika_love >= 0 and nodokaspecial30p4 == True and rikadate1 == False:
        jump rikadate1
    else:
        play sound "phonebeep.wav"

        "I tap on Rika's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "There's no answer."
        "Guess I'll call someone else."

        jump callnight

label rikadate1:
    play sound "phonebeep.wav"

    "I tap on Rika’s name in my phone after remembering that she told me to call just several hours before I took Nodoka’s virginity."
    "Does that technically relate to Rika in any way? No. But I can’t help but correlate certain things when they happen in pairs."
    "Because, according to that butterfly thing, it’s possible I never would have had sex with Nodoka at all if Rika hadn’t given me her number. I think."
    "I don’t know. I’m probably fucking up the butterfly thing since I can’t even remember what it’s called right now, but I’m sure there’s someone out there who knows what I’m talking about."
    "And hey, maybe that person is Rika? She’s certainly wise beyond her years."

    play sound "phonebeep.wav"
    play music "ame.mp3"

    ri "Hey! Good timing. How fast do you think you need to run in order to dodge the rain?"

    "I was being facetious, if you couldn’t tell."

    s "Why? You’re not planning on trying, are you?"
    ri "I’m in an argument with Rin and Futaba. They say it’s not possible but I am going to prove them wrong."
    s "They’re right and you’re smarter than this."
    ri "Fuck."
    ri "Anyway, what’s up? You don’t usually call me. "
    s "That’s because I didn’t have your number until you desperately thrust it upon me in an effort to counteract your loneliness. But seeing as you’re already busy arguing with Rin and Futaba-"
    ri "You can come argue {i}with{/i} me! I need someone on my side!"
    s "Well, I don’t believe in your cause, but I’m a pretty good liar when I want to be. So I guess I can swing by."
    s "Are you in your room? Or rather, are you still squatting in Rin’s room?"
    ri "I am at the gym! All three of us are. That writer girl was supposed to come as well, but she started ranting about some shit I didn’t understand and then ran away. "
    s "Yeah, that sounds about right. Only thing is, if you’re at the gym, there’s someone I need to talk to first in order to make sure I’m not yelled at again."
    ri "Relatable. I’ve been banned from several public spaces as well, but that was mostly cause of protests and stuff. Need me to find the manager?"
    s "No, just put Futaba on."
    ri "Futaba manages the gym? What the fuck?"
    s "Just put her on, Rika."
    ri "Futaba! Phone!"
    f "{i}Huh? What? For me? Why?{/i}"
    s "..."
    f "Uhh...hello?"
    s "Hey."
    f "Sensei? Why are you calling Rin’s mom? And...why are you asking for me?"
    s "So that I don’t further breach any sort of agreement we had regarding me not showing up at the gym while you’re there."
    f "Heh...thank you for the warning this time. "
    f "It’s fine. You can come. I just won’t have much time to spend with you if you do, but...considering you called Rika, I’m...pretty sure she’s the one who..."
    f "A-Anyway! I...I’ll see you soon! Bye!"

    play sound "phonebeep.wav"

    "Instead of handing the phone back to Rika, Futaba hangs up. And even though I’m not there, I can tell she immediately regrets it."
    "Regardless, I set off toward the gym after quickly refreshing my memory on where it’s located."
    "Halfway there, I realize why Rika and the others were arguing about rain."
    "Call it a lack of willpower or a heavy dose of self-doubt, but I don’t test her theory about dodging anything, electing to simply let myself get drenched instead. "

    scene rikagym1
    with dissolve

    "Which, based on everyone’s reactions, seems like it was the wrong idea."

    ri "What the heck?! No one told me there was a pool here!"
    r "Do you not believe in umbrellas? Or are you just {i}really{/i} out of shape?"
    f "I can...get you a towel if you want?"
    s "No, I’ll just suffer. What’s going on? How are things?"
    r "Dry."

    scene rikagym2
    with dissolve

    ri "Great! Just enjoying some overdue quality time with my daughter and her best friend! "
    r "Yes. {i}Overdue.{/i} As if she does not literally sleep in my bed."
    ri "I slept in Futaba’s once too. But it wasn’t intentional and I’m not a predator. I was just really drunk."
    s "Good excuse, but I doubt that would hold up in court."
    r "Sensei, I know the separation has a lot to do with it, but it’s really not a good look that my mom developed a drinking problem as soon as she started hanging out with you."
    s "If anything, it’s miraculous that the rest of you {i}haven’t.{/i} "
    f "I’m sure that being unable to actually buy alcohol is...a big part of it."
    ri "You come here often, Sensei? I can use a new gym buddy for when Rin is fed up with me. Which is pretty much all the time now. "
    s "Just come with Nodoka when she’s not busy running away. I don’t like places like this."

    scene rikagym3
    with dissolve

    ri "Really? How do you stay in shape, then?"
    r "I have an idea."
    f "I...don’t. Hahah...hah..."
    ri "Why do they sound like they’re hiding something from me? Are you, like...secretly a ballet dancer or something?"
    s "Why is {i}that{/i} your first assumption? That’s weird."
    ri "I don’t know. Your limbs are long and I think you’d look good in tights. Is {i}that{/i} weird too?"
    r "Yes, Mom. It is."

    scene rikagym4
    with dissolve

    r "Honestly, though? I agree. And I kind of want to see that now."
    f "I...also wouldn’t mind..."
    ri "I brought an extra pair of leggings you can try on if you want? Might have to {i}tuck it in{/i} if you know what I’m saying, though."
    s "I know what-"
    ri "{i}It{/i} means your dick."
    s "..."
    ri "I'm saying you'd have to tuck your dick in so you don't get arrested for indecent exposure."
    ri "That's a real charge, you know. And don't worry, I thought it sounded fake too."
    s "Oh, would you look at the time? I just remembered I have things to do today. Things that don’t involve wearing women’s clothes or exposing my penis in a gym."
    ri "Want me to walk you out? I was about to go get some fresh air anyway."
    s "I was actually just being sarcastic about leaving, but sure. I’ll go outside with you. Futaba doesn’t like when I watch her anyway and she makes it hard for me to {i}not{/i} stare at her in places like this."

    scene rikagym5
    with dissolve

    r "Mood."
    f "Th...That’s not my fault! If I could make them smaller, I would!"
    ri "You look great just the way you are, Futaba! Never feel pressured to change! But know that I would completely understand if you did anyway because your back is {i}fucked{/i} when you get older."

    scene rikagym6
    with dissolve

    f "Was that...supposed to be encouraging?"
    ri "Ready? We can stop in the lounge along the way and grab you a towel so you can dry off. "
    s "Before going right back into the rain? Great idea."
    ri "There’s, like...a thingy. A thingy we can stand under. A rain-blocking thingy."
    s "You mean an “awning?”"
    ri "Yeah. A rain-blocking thingy."

    scene rikagym7
    with dissolve

    f "Rin, stop staring at me."
    r "I can’t. My eyes are all locked up from all the...eye exercise I’ve been doing."
    ri "{i}Eye{/i}xercise."

    scene rikagym8
    with dissolve

    r "Weren’t you leaving?!"

    scene black
    with dissolve2

    "Rika and I head across the hall so I can make myself look slightly presentable and stop tracking water everywhere I go. "
    "She takes it upon herself to dry my back once I’m done with my hair and, while I wasn’t expecting this and would have likely rejected it if I knew it was coming, it’s...fine, I guess."
    "It’s not like she’s doing it because she wants to fuck me. Even if she probably {i}would{/i} fuck me. I think. "
    "I’m not sure."

    scene rikagym9
    with dissolve2

    "But I guess trying to find out right now would ruin the mood. "
    "I should be happy to just...spend some time with someone like her — who won’t just {i}not{/i} judge me for things, but is likely {i}incapable{/i} of judging me for anything in the first place."
    "Whether that’s due to blissful, forced ignorance or her head being completely empty is another question entirely."
    "But this is the part of the conversation where I probe her for background information, so I will leave any prior thoughts at the door (Just like an umbrella) and forge forward without them."

    s "Motherhood. Am I right?"

    "I come out swinging with another flawless attempt to appear human."

    ri "It has its ups and downs. Mostly ups. But then your daughter decides she’s too cool for you and that you’d be better off wandering aimlessly through the country with all of your belongings in a shopping cart."
    ri "I’ve already lived that life, man. I’m not ready to go back."
    s "Based on what little information I’ve gotten out of you, it seems like your past is {i}full{/i} of...odd things like that. So I won’t pretend to be surprised right now."

    scene rikagym10
    with dissolve

    ri "What can I say? I’m pretty cool, aren’t I? Rin should be happy she has a mom with so much life experience. "

    scene rikagym11
    with dissolve

    ri "But instead, she just yells at me for embarrassing her. Life is pain."
    s "It is. But that doesn’t mean she isn’t happy to have you. I heard nothing but good things prior to you showing up and confirming your existence."

    scene rikagym12
    with dissolve

    ri "Really? Like what?"
    s "..."
    ri "..."
    s "Okay, so I didn’t really hear much at all. But you can go ahead and pretend I said a bunch of really flattering things right here if that makes you happy. "

    scene rikagym13
    with dissolve

    ri "Hah...figures. I’m sure that even {i}if{/i} she said anything good, it would have been about her other mom. She was always closer to her than she was to me. The pain continues."
    s "She still likes you. I obviously haven’t been around her as much as you, but the way she treats you is unlike how she is with literally everyone else."

    scene rikagym14
    with dissolve

    ri "I know. I’m just being a pain."
    ri "I never had a great relationship with my mom and she wound up passing away before I was able to, like...see eye-to-eye with her and stuff. "
    ri "So I’ve always tried to stay on good terms with Rin to avoid something like that. Cause, you know...in twenty years when I’m dead, I’m sure she’ll be happy I crashed in her dorm room for a couple months."
    s "I...don’t know if I’d go that far or...word things exactly like that. But I do know she appreciates you."

    scene rikagym12
    with dissolve

    ri "So, I’m not embarrassing?"
    s "No, you definitely are. "

    scene rikagym11
    with dissolve

    ri "Frick."
    s "Being embarrassing isn’t necessarily a bad thing, though. And I’m sure she’d take that over rotting in an orphanage somewhere."

    scene rikagym15
    with dissolve

    ri "Yeah..."
    ri "You know, I’ve been with her for so long that I forget she’s adopted and not just a lesbian miracle-baby sometimes. "
    ri "Just...{i}thinking{/i} about her in a place like that gives me the creeps. I seriously couldn’t have asked for a better daughter."

    scene rikagym16
    with dissolve

    ri "Wasn’t without its hardships, though. And even if she’s come to accept it as normal now, it wasn’t {i}always{/i} like that. "
    ri "Which I guess is part of the reason she gravitated to my partner instead of me since {i}she{/i} was the one who was good at explaining all that kind of stuff. I didn’t really know what I was doing."
    ri "To be honest, I never really even thought of being a mom when I was younger. Life just kind of worked out that way."
    s "Was it your partner who decided to adopt then?"

    scene rikagym17
    with dissolve

    ri "I mean, that’s not really a decision someone can make on their own. There are a lot of steps involved and I knew it was coming. I didn’t just come home one day and...boom, child. I knew and I helped."
    ri "It just wasn’t my idea. "

    scene rikagym18
    with dissolve

    ri "Just kinda sucks it had to come to that in the first place. And I can’t help but think about how all of the kids we {i}didn’t{/i} choose wound up."
    s "As someone who has never and {i}will{/i} never adopt, I’m sure that line of thinking isn’t exactly abnormal. I’d probably be caught up in the same thoughts in your position."
    s "Which, again, is not a position I will ever be in as I hate children."

    scene rikagym19
    with dissolve

    ri "If it helps persuade you at all, Rin was far from an average kid. But I totally get that adoption isn’t for everyone when people like you can, like...go out and just recreationally {i}make{/i} babies and shit."
    ri "Just, whatever you do, don’t go on some crazy impregnation spree or something. Orphanages are crowded enough as-is and the last thing we need is more kids with no place to call home."
    ri "Or even worse, a place {i}to{/i} call home but, like...not a good place. Because while {i}I{/i} did a decently bang-up job as a mom in hindsight, same thing can’t be said for everyone."
    s "Which one of those two was Rin? Someone with no home or someone with a shitty one?"
    ri "I want to say that’s something you should talk to her about, but I’m not really sure how much she even remembers. So I’ll just tell you what I know."
    ri "Her bio-mom was a fucking psycho. "
    ri "I don’t think she was ever, like...{i}abusive{/i} or anything like that, but the girl was straight up deranged. Like, {i}genuinely{/i} insane."
    ri "The case-worker explained the situation in much greater detail way back when we adopted her and I don’t remember {i}everything,{/i} but..."
    ri "I {i}do{/i} remember she was way too young to be having a kid. And that she had, like...intense brain trauma or some shit. Just straight up the exact type of person who can’t raise a little girl alone."
    s "Alone? So her father was never in the picture either?"

    scene rikagym20
    with dissolve

    ri "Nah. Douchebag ran off before she was even born. Wouldn’t be surprised if he already had a family or something like that. Even the case-worker didn’t know what his deal was."
    ri "Sure didn’t help that Rin’s bio-mom wasn’t exactly in the state to open up about him either. "

    scene rikagym19
    with dissolve

    ri "But, hey- that’s one more reason you shouldn’t go around making babies you aren’t ready to take care of. "
    ri "Because yeah, some of them might end up with actual parents in good families or something, but most of them don’t. "
    s "If it comforts you, I don’t intend to ever reproduce."
    ri "Don’t need to {i}intend{/i} anything. Accidents happen. What matters is what comes next."
    ri "Say you {i}did{/i} knock some girl up. Doesn’t have to be on purpose. Would you man-up and accept responsibility? Or would you get the fuck out of there because you’re not ready to be a dad?"

    scene rikagym21
    with dissolve

    s "Let’s change topics."
    ri "Hard choice, right? Neither one of them is what you want. And because of that, somebody is gonna suffer no matter what- whether it be you, the person carrying the baby, or the baby itself."
    ri "It’s easy enough to avoid that ultimatum if you’re careful. But as a woman who once boned a bassist for backstage passes, I understand that we’re not always our {i}best{/i} selves."
    ri "It’s tough to judge what’s right and wrong when you get caught up in the moment."

    scene rikagym22
    with dissolve

    ri "Just don’t run away from the consequences if things get all fucked up. You hear me? Cause if you disrespect your elders, I’ll hit you. "

    scene rikagym23
    with dissolve

    ri "And I’m clearly ripped. So you’d be {i}done{/i} for, punk. Don’t mess with Rika."
    s "I think Rika should spend some more time at the gym before calling herself ripped. I would defeat you in your current state."

    scene rikagym24
    with dissolve

    ri "Hey! Don’t be mean! If I was still in my prime, I could totally take you down!"
    s "If you were still in your {i}prime,{/i} we’d probably be having sex in a tour bus."

    scene rikagym25
    with dissolve

    ri "Why? Do you play bass?"
    s "I can learn."
    ri "..."
    s "..."

    scene rikagym26
    with dissolve

    ri "I get why Rin likes you."
    s "Because...I make sexual passes at her mom?"
    ri "Because you’re a goober. Like her."
    s "..."
    ri "..."
    s "Did you just call me a “goober?”"
    ri "Yeah. Cause you {i}are{/i} one."
    s "..."
    ri "..."
    s "Rika, I don’t like that."
    ri "Tough cookies, goober. Be less of a goober and I won’t call you a goober anymore."
    s "..."
    s "I’m going home."

    scene rikagym27
    with dissolve

    ri "Without an umbrella? That’s a real goober move, buddy. You sure you don’t wanna come back-"
    s "Yes. Goodbye forever."

    scene rikagym28
    with dissolve

    ri "{i}Heh...{/i}"
    ri "{i}I hope not.{/i}"

    scene black
    with dissolve2

    "The night ends the same way it began."
    "Wet."
    "I say this as someone who is decidedly ungooberish."

    $ renpy.end_replay()
    $ rikadate1 = True
    $ rika_love +=1
    stop music fadeout 7.0

    "{i}Rika’s affection has increased to [rika_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label rikaspecial2:
    scene rikaschool1
    with dissolve2
    play music "10c.mp3"

    s "..."
    ima "..."
    s "Okay. What are you scheming today?"
    ima "Senpai! You say that as if I have a {i}history{/i} of scheming. And I’ve been almost entirely scheme-free the whole time you’ve known me."
    s "{i}Almost{/i} implies that there has been at least one. And that face is leading me to believe I am currently in the midst of it. So...out with it, subordinate."

    scene rikaschool2
    with dissolve

    ima "Hey! All that “subordinate” stuff really hurts, you know! I do just as much around here as you! You’d be nowhere without me."
    s "That’s probably true. Things would definitely be a lot quieter, though."

    scene rikaschool3
    with dissolve

    ima "Apology accepted."

    "There was no apology."

    ima "To show your forgiveness, I will allow you to take me out to a fancy restaurant of {i}your{/i} choice where I will proceed to-"
    s "That is not what you came here for. Tell me what you want."

    scene rikaschool4
    with dissolve

    ima "Some respect would be nice."
    s "Anything else?"

    scene rikaschool5
    with dissolve

    ima "Yeah. I have a secret for you."
    ima "To be honest, things are about to get {i}really{/i} crazy up in here, Sensei. You might wanna buckle up for this one."
    s "Uh-oh. Is today the day we finally cross the line of boss and semi-useful employee and wind up sleeping together on the couch?"

    scene rikaschool6
    with dissolve

    ima "No! And for the millionth time, you are not my boss! I report only to those at the top of the educational ladder and I will not be reduced to mere nothingness by a man who can barely climb it!"
    s "Sorry, can’t hear you from all the way above you on some ladder-thing."
    ima "Newest employee of Kumon-mi High! Please enter the room!"
    s "Newest employee?"

    play sound "dooropen.mp3"
    scene rikaschool7
    with dissolve

    ima "Ta-dah!"
    ri "Hey. I’m here now."
    s "What?"
    ima "Please give a warm welcome to the new light music club advisor, Rika Rokuhara!"
    s "You’re...a teacher now?"

    scene rikaschool8
    with dissolve

    ri "I hope not. I never even finished high school. I’m kind of just here to chaperone Rin’s band."
    ima "And to refrain from nepotism by addressing them as the light music club and not “Rin’s band.”"
    s "There was a job listing for just advising a club? You don’t have to, like...you know, teach as well?"
    ri "Yeah, I guess."
    s "What the fuck? I want that job."

    scene rikaschool9
    with dissolve

    ima "I mean...you kind of already have it, Senpai. You’re just not really good at that part either if what I’ve heard from the manga club is true."
    s "Stop talking to the girls in my club. Go hang out with your own."
    ima "No can do, buddy. I need to hang on to every last bit of youth I’m able to wrap my hands around."
    s "Ignoring the slow disintegration of your psyche and how unhealthy your desire to be young again is, why are you making a show out of this? Rika could have just come in here without you."

    scene rikaschool10
    with dissolve

    ima "{i}Because,{/i} jerk, you never answer your emails. "
    s "I have emails?"
    ima "How do you still work here?"
    s "Probably tenure. I’m not really sure."

    scene rikaschool11
    with dissolve

    ima "Hah...regardless, I’m here to save the day once again and let you know that it’s {i}your{/i} responsibility to show Rika the ropes. "
    ima "I would have gladly done it, but the two of us have {i}history.{/i}"
    s "I’m surprised you have enough pride left to bring that “history” up."

    scene rikaschool12
    with dissolve

    ima "I must have been drunk. Either that or Rika just doesn’t have much experience when it comes to tonsil hockey."
    ri "No comment."
    s "So I just have to show her the ropes?"

    scene rikaschool13
    with dissolve

    ima "Yeah. Think you can handle it?"
    s "Of course. Shouldn’t be a problem at all."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene rikaschool14
    with dissolve2

    s "Alright. Here they are."
    ri "Cool. Thanks for showing me."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene rikaschool15
    with dissolve

    s "So, now what?"
    ri "I’m not really sure. In fact, I barely even know what I’m supposed to be doing here. "
    ri "How did your orientation thingy go? Maybe you can just try and do that to me? Or...with me?"
    ri "On me?"

    scene rikaschool16
    with dissolve

    s "{i}Orientation...{/i}"

    "Come to think of it...I never had anything like that."
    "Sure, that’s most likely because I was thrust into this new (But confusingly {i}not{/i} new) life in the middle of the school year where everyone already knew who I was and how I taught-"
    "But that doesn’t take away from how confusing I know things must be for Rika right now. And how most other people in her shoes would just abuse their power to consensually molest a bunch of girls."
    "Actually, that’s probably just me and a handful of other horrible individuals who shouldn’t be allowed in a place like this. But I should ask just to make sure."

    s "How interested are you in pursuing a physical relationship with teenage girls?"
    ri "Like...in phys-ed? I can probably teach phys-ed if I have to. That wasn’t in the job description, but how hard could it possibly be?"

    "Okay, so it seems like that sort of thing doesn’t even occur to Rika and I really am just the scum of the earth. That’s good."
    "But I should probably at least show her around so she doesn’t get lost and wind up like Yasu — desperately clinging to those she trusts and leaving her well-being entirely in their hands."

    s "I don’t think you’ll have to teach phys-ed. The girls normally just hang out on their phones for that period. But I can give you a tour at least."

    scene rikaschool17
    with dissolve

    ri "Cool. Works for me."
    ri "I know we’re friends outside of work and whatnot, but I kind of need this job thing to go well so I can finally get out of Rin’s hair."
    ri "I’m sure I don’t have to tell you this since you’re already familiar with the place, but let’s keep it professional while we’re here. Cool?"
    s "Yeah...I don’t know if I can do that."

    scene rikaschool18
    with dissolve

    ri "Why? Do you have a crush on me?"
    s "Why are your first assumptions for things always so strange?"
    ri "{i}Is{/i} that strange? Because I don’t think I’ve ever had a job where my boss didn’t immediately try to hook up with me before, so I’m kind of just used to it by now."
    s "And how many times-"
    ri "No comment."
    s "..."
    ri "..."

    scene rikaschool19
    with dissolve

    ri "I’m kidding. "
    ri "Well, kind of. "
    ri "The boss thing is true, but I haven’t really had many jobs in the first place so the numbers probably aren’t all that impressive or whatever."
    s "..."
    ri "..."
    s "Why don’t we start with the gym?"

    scene black
    with dissolve2

    "For the next half-hour or so, I walk Rika around the school- pointing out the various rooms and offices she’ll {i}probably{/i} have to familiarize herself with in the coming weeks."
    "But, to be honest, I have no idea if this will be valuable at all as I did not imagine the school would ever stoop to hiring someone for just {i}one{/i} thing as the rest of us follow our classes {i}everywhere.{/i}"
    "Well, almost everywhere. "
    "I’ve yet to make my way inside of the shower room in the gym yet, but I {i}did{/i} come close that one time when Nodoka decided to try and ruin Yumi’s life."
    "..."
    "Nodoka."

    play sound "static.mp3"
    scene nodokascene35sepia with flash
    stop sound

    "I keep forgetting what happened — but in different ways from how I normally forget."
    "That night in the hotel is all still a blur, but there’s something inside of me I cannot identify that doesn’t make me uncomfortable with it."
    "If anything, it makes me feel {i}good.{/i}"
    "The lingering satisfaction of unsheathing my cock from her virgin hole vaporizes the resentment and disdain I know I’m meant to have over what she’s done to Yumi and...anyone else she’s toyed with."
    "So basically...all of us."
    "But I can’t bring myself to hate her."
    "I can’t even bring myself to {i}dislike{/i} her."
    "All I can think of is how safe she makes me feel."
    "Or perhaps it would be better described as numbness."
    "..."
    "I want to feel it again."
    "I want to devour her."

    ri "Helloooo? Anyone home?"

    play sound "static.mp3"
    scene rikaschool20 with flash
    stop sound

    s "Huh? What?"
    ri "Caught you staring off into the distance. But I guess we can just chalk it up to you being a goober again."
    s "I don’t like whatever sort of “vibe” we’re creating here —which I’m pretty sure is what relationship dynamics are referred to as by young people now."
    ri "Really? I think we mesh kinda well. But I’m saying that as professional Rika — not “make out with coworkers at a dive bar” Rika."
    s "As long as I’m next and not Wakana I’ll be happy."

    scene rikaschool21
    with dissolve

    ri "See?! I told you. Every single boss I’ve ever had has tried to get into my pants on day one. I can’t escape."
    s "I mean, if you want to get technical, I was trying to get into your mouth."
    ri "That’s easier, but still. Come on, man. I’m too old to hang out under the bleachers at this point in life. I’m just trying to make some money so Rin doesn’t have to do my laundry anymore."

    scene rikaschool22
    with dissolve

    ri "Wait! Are we allowed to do our laundry here? Does the teacher’s lounge have a bed? Also, why is there a boy’s locker room? This is an all-girl school."
    s "No, no, and no clue. And before you ask, you can’t live here."

    scene rikaschool23
    with dissolve

    ri "Not even for, like...a weekend so Rin and Otoha can make out on her bed?"

    scene rikaschool24
    with dissolve

    o "Rika! What are you doing here? And what were you just saying about Rin and me?"
    ri "I work here now! I’m your new club advisor thing! "

    scene rikaschool25
    with dissolve

    o "Wait, seriously? Like, you officially work here? That’s awesome."
    ri "It is! But do you know what’s even more awesome? The fact that you and Rin are sexually active n-"

    scene rikaschool26
    with dissolve

    ri "...ow."
    s "Wow."

    scene rikaschool27
    with dissolve

    ri "Otoha! Come back! I just wanted to congratulate you guys!"
    s "Rika, I get that you’re kind of...and forgive me for lack of a better term...a {i}goober-{/i} "
    s "But there are some things you just shouldn’t say to your daughter’s significant other and almost all of them are exactly what you just said."

    scene rikaschool28
    with dissolve

    ri "Damn it. I thought girls today were more open about that kind of stuff?"
    s "Ignoring any thoughts or experience I have regarding that, I don’t think it really changes a girl not wanting to talk to her girlfriend’s mother about how many fingers she put inside of her daughter."

    scene rikaschool29
    with dissolve

    ri "I just wanted to express my appreciation. You have any idea how long Rin’s been hormonal for?"
    ri "Because that girl’s been spending way too long in the shower ever since she turned twelve and as someone who experienced that same burst of energy at that age, I know what's really going on in there."
    s "And that is...just one more thing a parent should just never reveal to anyone. So I am going to do my best to keep that little factoid away from Rin for the indefinite future. "

    scene rikaschool30
    with dissolve

    ri "Oh, come on. She’s a kid. It’s not like I’m telling you about a grown woman’s habits. I bet you were the same exact way when you were that age."
    s "Maybe just...try to have a little more tact in the future."

    scene rikaschool31
    with dissolve

    ri "{i}What{/i} future? I’m 42. "
    ri "And even if I {i}look{/i} okay for my age, no one’s going to stick around when they find that out."
    ri "People want families and whatnot and my time’s kind of limited, you know?"
    ri "Tact or no tact, it’s not gonna make a difference. So why not just “mom” it up while I still can?"
    s "First off, you’re wrong and you have plenty of time left. Second, you can still “mom” it up and embarrass your daughter while keeping things like {i}that{/i} a secret. And third-"
    ri "Is third something about how I’m a catch even with all of my “flaws?”"
    s "..."

    scene rikaschool32
    with dissolve

    ri "Heh..."
    ri "You know, everybody always likes to say things like that. "
    ri "About how “perfection” isn’t real and that it’s those little “imperfections” that make us beautiful. "

    scene rikaschool33
    with dissolve

    ri "And while that {i}sounds{/i} nice and all...and makes us look like better people than we actually are, it’s all fake at the end of the day."
    ri "Imperfections and flaws can be cute when they come in small doses, sure. But when you start paying close attention to little things like that, you don’t see “cute” at all."
    ri "You see flaws as exactly what they are. {i}Flaws.{/i} Flaws that pile up and weigh down how much you care about someone. "
    ri "If it’s one or two things, you can learn to deal with it. "
    ri "But then you start looking for more. And they start getting easier to find."

    scene rikaschool34
    with dissolve

    ri "Then, the next thing you know, you've collected so many of those “imperfections” that it becomes almost impossible to see anything good at all."
    s "No one has to be perfect, Rika."
    ri "I agree. No one has to be perfect. No one {i}can{/i} be perfect. Which is why we fall for people who ignore our flaws. And hey, for some, that kind of thing works out. "
    ri "There are plenty of successful couples who can live like that forever. And some who cherish those little quirks for the rest of their lives."
    ri "But it’s impossible to know if you’re with someone like that beforehand. "
    ri "And by the time you figure it out, it might already be too late."
    s "I see...You’re not just worried you’re not good enough-"
    ri "I’m afraid of being wrong again."

    scene rikaschool35
    with dissolve

    ri "But, on the bright side, I’m not crying anymore. Now, it’s mostly just feeling like an idiot."

    scene rikaschool36
    with dissolve

    ri "I wasn’t always like this, though. "
    s "Did you suffer some...traumatic brain injury or something?"
    ri "No, {i}goober.{/i} I’ve never been book-smart or anything like that. Me and school were mortal enemies."

    scene rikaschool37
    with dissolve

    ri "But there were three things I was great at back before I spent all of my free time feeling sorry for myself."
    ri "Thing number one was music. "
    ri "I might not be able to {i}read{/i} it as well as a lot of famous composers and stuff, but that never really mattered to me."
    ri "I made noise that made people feel good. Or sad. Or angry. Or whatever I wanted them to feel because I {i}wanted{/i} to feel something too."
    ri "I made money doing what I loved...and now I can make money doing that again. Just in a totally uncool, corporate kind of way. But hey, if Metallica can sell out, so can I."
    s "What’s number two?"

    scene rikaschool38
    with dissolve

    ri "Protesting."
    s "Is that...a thing you can be good at?"
    ri "It got me thrown in jail a bunch of times. But like half of the shit teen Rika and company campaigned against wound up getting changed eventually, so hey. That’s a win in my book."
    ri "It’s also how I met my ex. "
    s "You two protested together?"

    scene rikaschool39
    with dissolve

    ri "We were actually on opposite sides."
    ri "She was always really straight-laced and {i}traditional{/i} when it came to her values. But a lot of that was due to the environment she was brought up in."
    ri "I was lucky enough to come from a more progressive household who let me form my own opinions instead of guiding me toward theirs."
    ri "Which was really great on account of the whole “liking girls” thing."
    ri "But yeah, if it weren’t for number two and number three, I never would have wound up with her in the first place."
    s "And what was number three exactly?"

    scene rikaschool40
    with dissolve

    ri "Eating pussy."
    s "I expected nothing less from you."

    scene rikaschool41
    with dissolve

    ri "What can I say? Girls always like to think they’re straight until they meet someone who {i}knows{/i} how to please them."
    ri "So, yeah. I’m basically the savior of humanity — a woman so skilled that she has straight up eaten the homophobia out of someone."
    s "I’m curious as to how you got her in that position in the first place."

    scene rikaschool42
    with dissolve

    ri "I am just {i}that{/i} good."

    scene rikaschool43
    with dissolve

    ri "But again, those days are over. I’m 100%% embarrassing mom now. "
    s "Are you sure? Don’t you have a duty to the world you need to carry out? Not many were born with your power."
    ri "The only duty I have now is getting my life back on track and making sure Rin stays on hers. "
    ri "Hopefully, I’ll be able to accomplish both of those by being here."

    scene rikaschool44
    with dissolve

    ri "And maybe..."

    scene black
    with dissolve2
    stop music fadeout 7.0

    ri "Maybe, I’ll find something else as well."
    ri "Or maybe I won’t?"
    ri "There’s art in never knowing."
    ri "And I don’t mind appreciating that for a little longer this time."

    $ renpy.end_replay()
    $ rikaspecial2 = True
    $ rika_love += 1

    "{i}Rika’s affection has increased to [rika_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label rikadive1:
    scene bartrivia1
    with dissolve2
    play music "letsfuckingo.mp3"

    anno "Okay, everyone! Due to a sudden shortage in paper, we’ll be playing tonight’s game of bar trivia the old-fashioned way! By yelling out the answers for points!"
    anno "The game will begin in five minutes, so finalize your strategies now! And remember- teams of two {i}only!{/i}"
    s "How did things come to this?"

    scene bartrivia2
    with dissolve

    w "Seeing as your fake-amnesia is acting up again, I will now recap the last hour of your life. Buckle up, Arakawa. This is going to be good."
    s "I have a very strong feeling it won’t be."
    w "The day started normally- when you woke up and decided to go at least another twenty-four hours as the unlovable degenerate you are. "
    w "Things proceeded as normal until Imani, also a degenerate, decided tonight would be a good night for the four of us girls to hang out here for a game of bar trivia."
    w "You, someone who was not invited, showed up shortly after. And while this would be a tragedy under most circumstances, it wound up working out due to her sudden bout of food poisoning."
    w "Now, we are enemies and my lover and I will defeat you. Only to subsequently force some form of punishment on the two of you that you will rue for the rest of your lives."
    w "I hope you are ready to be completely and utterly decimated."
    s "Thanks, Wakana. You should just handle all of my inner monologues from now on. That was more fun than any recap I could have given."
    w "It is painful enough being stuck in my own mind. The last thing I want is to be stuck inside of yours as well."
    s "Are you sure you’re up for this, Rika?"
    ri "Up for it? I was {i}born{/i} for this."
    ri "I might not seem like it, but I’m a god damn expert at useless trivia. Those dykes next to us don’t stand a chance."

    scene bartrivia3
    with dissolve

    os "Woah. I’m all about the competitive spirit and shit, but isn’t it kind of messed up to throw slurs at your own people?"
    ri "Love no one. Everyone is your enemy, dick or no dick. Hail Satan."
    w "Arakawa, tame your partner before my beloved kicks her head off. "

    scene bartrivia4
    with dissolve

    s "Rika, calm down."
    ri "Fuck you, goober. Do you have any idea what I had to do the last time I lost a punishment game?"
    s "No, but I feel like I’m obligated to ask now."
    ri "Let’s just say it involves a remote-controlled device and me being hunched over an apple display at the grocery store, trying to keep my mouth closed."
    ri "Or maybe it was potatoes. I don’t remember. I was too busy regretting everything I’d ever done."
    w "That just sounds like a Wednesday for Osako."

    scene bartrivia5
    with dissolve

    os "Shh!"

    play sound "vibrate.mp3"
    scene bartrivia6
    with hpunch

    w "Zap."
    os "Mm! {i}Ahem...ahem...{/i}"
    ri "Shh. Did anyone else just hear that? "
    s "Ignore the exhibitionists for a moment. We need to listen to the announcer and figure out our strategy for the game."
    anno "Okay! It’s time to start!"
    s "Nevermind. Just try not to get anything wrong."

    scene bartrivia7
    with dissolve

    ri "Same goes for you. Don’t hold me back, Sensei. Me and Imani are undefeated so far."
    ri "Granted, we’ve only played one game, but still! I’m not going to lose to a loving, affectionate, and hypersexual couple while being fresh off a long-term relationship! It would be too painful!"
    anno "Question one..."
    anno "In “Game of Thrones,” what is the translation of the High Valyrian term “valar dohaeris?”"

    scene bartrivia8
    with fade

    os "Do you know this? You read those books, right?"
    w "No. But we did keep the television series on while we were having sex several Sundays out of every year. You just likely don’t remember it since you were always tied up and robbed of your senses."
    ri "All men must serve!"

    scene bartrivia9
    with fade

    ri "I have also had sex with that show on in the background! "
    anno "That...information was not necessary. But you are correct!"

    scene bartrivia10
    with dissolve

    ri "LET’S FUCKING GOOOOOOO!"
    os "Oh, calm down. You got one question right."
    s "You know, this is a side of you I don’t particularly dislike. Especially since it means we’ll be able to punish our lesbian friends."

    scene bartrivia11
    with dissolve

    ri "Oh, yeah! I got so caught up in how great at trivia I am that I completely forgot we can mess with them. Is there anything we-"
    anno "Question two!"

    scene bartrivia12
    with dissolve

    ri "Fuck it! We’ll figure that out later! Just shut up and let me think!"
    s "I haven’t even said anything. Also, please don’t attack me unless our clothes are off. Thank you."

    scene bartrivia13
    with fade

    os "Jesus. Rika’s even more aggressive today than she was last time."
    ri "Shut it, carpet muncher!"
    s "Wasn’t it just the other day you were commenting on how good you are at-"
    ri "Shh! Question two!"
    anno "“Spiker” and “Sponge” are the antagonists of which Roald Dahl children’s book?"
    w "Oh, I actually know this one."

    scene bartrivia14
    with dissolve

    os "What? Then say it. We’re supposed to yell stuff out. Don’t just let Rika and Sensei win."
    w "Why not?"
    os "Uhh...because you said you were going to decimate him? And because winning is awesome?"
    w "That is true. But with each passing question, I’m becoming more aware that our punishment will likely be sexual in nature and now I’m just curious about what they’d have us do."

    scene bartrivia15
    with dissolve

    os "There have...been two questions."
    w "I’m afraid I don’t see your point, my love. "
    os "Wakana, we can have sex literally any time we want. "
    w "Yes, but how many opportunities do we have to be {i}punished{/i} by other people?"
    s "I volunteer to do that exact thing literally any time you want."

    scene bartrivia16
    with dissolve

    os "Shut it! "

    scene bartrivia17
    with dissolve

    os "The two of us are going to beat you guys fair and square and you’ll both regret ever making us-"

    play sound "vibrate.mp3"
    scene bartrivia18
    with hpunch

    w "Zap."
    os "Eep!"

    scene bartrivia19
    with dissolve
    play sound "vibrate.mp3"

    w "Zap."

    play sound "vibrate.mp3"

    w "Zap."

    play sound "vibrate.mp3"

    w "Zap."

    os "Mm...mm! "
    w "It’s never too late to concede, my dear. There will be other trivia games."

    scene bartrivia20
    with dissolve

    os "{i}Wakana! We’re with our friends! Stop!{/i}"
    w "Question three: How many times can I make you cum before you swallow your pride and follow me into the bathroom?"
    ri "Hey! No quitting! Just cross your legs really tightly and tough it out like a real woman!"
    os "{i}Wakana!{/i}"
    w "Z-"

    scene bartrivia21
    with dissolve

    os "Oh my fucking God! Fine!"
    w "One punishment please, opposing team. "
    ri "Fine. Help me paint a wardrobe I found on the side of the road. Rin won’t let me use hers anymore."
    w "Arakawa, I can’t believe I am saying this, but please think up a punishment for my lover and me."
    s "Paint Rika’s wardrobe, but do it {i}naked.{/i}"
    ri "Ooooh, good one. "
    w "You two are worthless. "

    scene bartrivia22
    with fade

    w "Come now, Osako. I’ll think up my own way to punish you."
    os "Wakanaaaa! Turn the...{i}thing{/i} off!"
    s "Does...this mean we win?"
    anno "I’d...at least like someone to answer the second question so I don’t have to just stand around anymore."

    scene bartrivia23
    with dissolve

    ri "Oh, sorry. James and the Giant Peach. "
    anno "That is correct! "

    scene bartrivia24
    with dissolve
    stop music fadeout 15.0

    anno "But...seeing as you two are now the only team left, I suppose we’ll take a quick intermission and wait for your friends to return from...yeah."
    ri "You can keep asking trivia questions if you want. This is a hidden power of mine and I feel like I’ve barely even gotten to show it off on account of us only making it two rounds in before sex happened."
    anno "No...I think I need a smoke break. But you two have fun for now."

    scene bartrivia25
    with dissolve

    ri "Oh man...I was looking forward to this."
    s "If it’s any consolation, I’m impressed by that last answer. Especially since it was based on a piece of 1960’s literature and not a popular 2000’s television series."
    ri "It was one of the first books Rin ever read. Took it right from my collection. "
    s "Didn’t take you as much of a reader."

    scene bartrivia27
    with dissolve
    play music "love.mp3"

    ri "Used to be. Not so much anymore. "
    ri "Just fell out of love with it one day. But it’s not like I was ever reading any of that advanced stuff anyway. It was mainly just children’s books and stuff."
    s "Then where exactly does all of this trivia knowledge that I am {i}definitely{/i} sure you possess come from?"

    scene bartrivia28
    with dissolve

    ri "Hey, what’s with the sarcasm? I’ve got a 100%% correct answer rate so far. You have no reason to doubt me."
    s "Sure, apart from the sample size being two. It’s just a little weird that you know so much when you claimed yourself to not be very “book smart.” Yet here you are answering questions from two books."

    scene bartrivia29
    with dissolve

    ri "Game of Thrones was a book?"
    s "Rika-"

    scene bartrivia30
    with dissolve

    ri "I don’t have a fun or exciting answer for you, man. I’m just good at remembering useless information and I used to watch Jeopardy with Rie back in the day."
    s "Rie being...Rin’s other mom, I’m assuming?"
    ri "Yeah. Sorry. Wasn’t aware you didn’t know her name."
    ri "We were always super competitive about it. But she was {i}way{/i} smarter than I was, so she had an upper hand and-"

    scene bartrivia31
    with dissolve

    ri "Actually, let’s talk about something else. I don’t want to waste this whole intermission thing reminiscing about stuff that is probably going to make me cry into my beer."
    s "I thought you were done with crying?"
    ri "Yeah, me too. Which is why I think we should stop and do something else."
    s "Like?"

    scene bartrivia32
    with dissolve

    ri "How about you pick? I feel bad sucking you into this game thing when you probably just came here to drink and relax."
    s "I can pick?"
    ri "Sure. Yeah. Pick whatever you want and we can do that."
    s "I mean..."
    ri "You mean?"

    scene bartrivia33
    with dissolve

    s "There are {i}two{/i} bathrooms here, you know."

    scene bartrivia34
    with dissolve

    ri "Do you have to go? I can wait."
    s "Not what I was saying."
    ri "Then what-"

    scene bartrivia35
    with dissolve

    ri "Oh."
    ri "That’s what you meant."
    s "..."
    ri "..."
    s "I was just-"
    ri "Do you think I’m a slut?"
    s "..."
    ri "..."

    scene bartrivia36
    with dissolve

    ri "I’m not trying to be confrontational and I won’t blame you if you do. I just want to know."
    s "I mean...you definitely have a lot of {i}stories.{/i} And I have seen you make out with Imani on a dare."

    scene bartrivia37
    with dissolve

    ri "Yeah. That’s fair. "
    ri "I won’t pretend like my younger years weren’t a little...all over the place. I was far from innocent and...definitely...{i}experimented{/i} a lot. "
    ri "But it’s not like that lifestyle followed me when I met Rie. That was me, like...genuinely settling down. "
    ri "And the Imani thing was a combination of break-up pain and not really thinking kissing is a big deal. But, then again, that’s probably just because I’ve...with a lot of...yeah..."

    scene bartrivia38
    with dissolve

    ri "Besides, {i}she’s{/i} the one you want anyway, right? And I’m just the spontaneous, easy backup plan."
    s "You think I want Imani?"

    scene bartrivia39
    with dissolve

    ri "Yeah, I mean...even if you're not dating, aren't you guys kind of, like...together-{i}ish?{/i}"
    ri "Like...there’s definitely some kind of “will they, won’t they” thing going on with you two and I just kind of figured there was some...tension."
    s "Didn’t you also think something similar about Wakana and me during our first meeting?"
    ri "Lowkey, I still kind of think that. But Wakana is a friend and I know she loves Osako. "
    ri "You and Imani, though...I’m surprised you’re, like...{i}not{/i} together-ish if that’s what you’re trying to tell me right now."
    s "That is what I’m trying to tell you right now. Weirdly enough, absolutely nothing has happened between the two of us yet."
    ri "Okay, but like...{i}why?{/i}"
    s "What do you mean {i}why?{/i}"
    ri "I mean she obviously likes you. You know that, right?"
    ri "Whenever you’re not around, she’s always checking her phone and asking us if she should invite you or not. It’s super noticeable. And you’ve got crazy good chemistry when you {i}are{/i} together."
    ri "Like, frankly, it feels kind of weird hanging out with you when she’s {i}not{/i} around because I keep thinking of how jealous she’d be and stuff."

    scene bartrivia40
    with dissolve

    s "Does she really do all of that?"
    ri "Yeah. She’s down bad for you, dude. I don’t get why you don’t just go for it."
    ri "Are you, like...{i}with{/i} someone else already? "
    s "If I was, would I have invited you to the bathroom a few minutes ago?"
    ri "You think that’s ever stopped anyone from inviting me into {i}other{/i} bathrooms?"
    s "Good point."
    s "You know, I probably shouldn’t be telling you this, but I {i}am{/i} seeing someone else. Several people actually. "
    ri "Why shouldn’t you be telling me that? I’m not going to blurt it out to anyone."
    s "You mean like how you blurted out that thing about Rin taking too long in the shower because of teenage hormones?"
    ri "This is different. This is serious. Your secret’s safe with me, goober."
    s "Stop calling me that."
    ri "No. It’s a term of endearment now. So tell me what’s up. "
    ri "If you’re seeing so many other people, what’s stopping you from getting with Imani when literally everyone ever knows she wants it?"
    s "..."
    ri "Come on. I know you know the answer."
    s "That’s...kind of the thing. I {i}don’t.{/i}"
    s "We joke about our relationship all the time. And I definitely {i}want{/i} to have sex with her because she’s extremely attractive."
    s "But I also..."
    s "Think I might...actually {i}care{/i} about her?"

    scene bartrivia41
    with dissolve

    ri "You say that like it’s a bad thing."
    s "It is, though. That sort of thing normally doesn’t happen until {i}after{/i} I’ve already started “progressing” things with someone."
    s "But with Imani, everything feels a little too natural already. Like we’re already-"

    scene bartrivia42
    with dissolve

    ri "Together-ish?"
    s "Together-ish."
    s "I just like the way things are right now and don’t want to ruin what we have going. "
    ri "So you won’t hook up with her because you care about her."
    s "Right."
    ri "But you’ll hook up with {i}me{/i} because you {i}don’t{/i} care."

    scene bartrivia43
    with dissolve

    s "That’s not what I-"
    ri "..."
    s "I didn’t...mean it like that."
    ri "You did. "
    ri "And it’s {i}fine{/i} that you did. I get it."
    ri "I’d probably have a hard time taking me seriously too."
    ri "I’m sad. Alone. Open. Friendly. Gullible. Dumb. Old. Have a hard time saying no."
    ri "All signs point to me being an easy target. I’m not gonna blame you for trying to take a shot."
    s "..."
    ri "I just don’t want to be that kind of person anymore. "

    scene bartrivia44
    with dissolve

    ri "Uhh...I’m gonna head home for the night. Sorry for flaking. It’s not your fault, it’s mine."
    s "You can’t leave yet. I need a partner for the rest of the game."

    scene bartrivia45
    with dissolve

    ri "Those two won’t be back for at least an hour. And I don’t want to wind up giving you even more reasons to not care about me, so...yeah."
    ri "I’ll see you next time, though. And again, this is a me thing. Not a {i}you{/i} thing. You didn’t do anything wrong and-"
    ri "Yeah. I just...fucked up the vibes. That’s my bad, man. See you next- yeah. Already said that."

    scene bartrivia46
    with dissolve

    ri "Later! Sorry!"
    s "..."

    scene black
    with dissolve2

    "The MC comes back into the bar a few minutes later and notices that everyone else has left."
    "I solemnly answer his trivia questions on my own."
    "And even though I win, it feels like I lose."

    $ renpy.end_replay()
    $ rikadive1 = True
    $ rika_love += 3
    stop music fadeout 7.0

    "{i}Rika’s affection has increased by 3!{/i}"
    "{i}You have unsuccessfully attempted to seduce a woman!{/i}"
    "{i}Maybe you should stick to children!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label sportswars1:
    scene sky
    with dissolve2
    play music "10c.mp3"

    "Let’s talk about “responsibility!”"

    ri "Aaaaaaaaah!!!"

    "Rika Rokuhara was a normal middle-aged woman. And sure, she’d been arrested on several occasions for protesting and things of that nature. {i}Sure,{/i} she wasn’t the brightest tool in the shed."
    "{i}Sure,{/i} she’d give the occasional backroom handjob in exchange for concert tickets or VIP passes or, on one occasion, a large pizza. But none of that meant she didn’t understand responsibility!"

    ri "Why do I have to be responsible today?!"

    "But that didn’t mean she couldn’t question when and why it would become relevant to her in day-to-day life."

    scene sportwarintro1
    with dissolve2

    ri "I’m not even a teacher. Why am I suddenly being given teacher-like responsibilities? Does this mean I can ask for a raise? Is this what it means to have a normal job? Why do I have so many questions?"

    scene sportwarintro2
    with dissolve

    ri "Why am I holding this clipboard? Why do I have to cover up my tattoos? Who killed Laura Palmer? Why won’t Rie answer any of my calls? These are all important things, Rika."

    scene sportwarintro3
    with dissolve

    ri "But no, Rika! You have to {i}read,{/i} Rika! You must {i}teach!{/i}"

    "She didn’t have to teach. In fact, all she had to do was head over to the soccer field and read off a list of contests that the girls of Class A would be competing in for this year’s Dorm Wars."
    "But she was such a mess that even this proved somewhat difficult. After all, where even {i}was{/i} the soccer field? And why was it only called “soccer” in some countries? "

    scene sportwarintro4
    with dissolve

    "She manages to steel herself, knowing full well that, despite how confused she was at the moment, she’d overcome this obstacle like she’d overcome so many things before."
    "Because yes, she was a {i}normal{/i} middle-aged woman. She knew what it was like to raise a little girl and she knew the purpose of responsibility as a whole in the grand scheme of things. "
    "But apart from this baseline understanding of one quality and “Ten Tips and Tricks to Make Even Straight Girls Want to Fuck You,” she wasn’t good at thinking of multiple things at once. And that made this hard."
    "Harder than it had to be. Because while she was tasked with opening up this year’s “ceremony,” she was also tasked with never doing anything to embarrass that same little girl she raised."
    "This was one more thing that added to her normalcy. Plenty of children out there want their parents to be as uninvolved as possible. And while that disappointed Rika, she understood it."
    "She just hoped that little girl would be able to forgive her for crossing paths with her before the final bell rang. And she would. For that little girl loved her mother too, after all."
    "But right — responsibility. Or, like they used to call it where I’m from, “weighing what you want to do against what you’re expected to do.”"
    "When the weight of the world becomes too heavy, you’re often forced to shed some. So Rika’s choices at this point in time were “Do my job” or “Don’t interfere with Rin’s life.”"

    ri "What the hell is “death ball?”"

    "But of course, she quickly forgot all of that the moment something else piqued her interest, eliminating both options entirely."
    "But that’s okay. Because responsibility only matters when there are people who expect something from you. But sometimes, different people expect different things."
    "Sometimes, you have to do something that’s going to upset someone."
    "Sometimes, there’s no right choice to make. "
    "Sometimes, you have to take something that doesn’t belong to you."
    "But you stall and you cry and you stall some more until you throw yourself (or {i}get{/i} thrown) on top of your niece’s friend on a roof somewhere and have to fuck her until she pops."
    "Sometimes, she goes away and it makes you sad. So you do sad things like wander around the city in hopes that there will be something that {i}doesn’t{/i} remind you of her."
    "But everything does."
    "And nowhere is safe."
    "So while a normal middle-aged woman takes that one quality she can hold in her heart even deeper than the fingers of a bassist under some bleachers somewhere, {i}you’re{/i} absent."
    "{i}You{/i} have never cared about responsibility."
    "You are a failure."
    "And just because I can’t see you right now doesn’t make it any less true."

    n "No, really! The new stuff is great!"

    scene sportwarintro5
    with dissolve

    ri "Huh?"

    scene sportwarintro6
    with fade

    n "It’s got the same vibe as the older stuff,  but the polish really shines and the production value as a whole is just way better. It’s super impressive, really."

    scene sportwarintro7
    with dissolve

    n "{i}But anyway, here are the lockers! And right out there is the courtyard where I eat lunch sometimes. Oh,  and this over here is the gym!{/i}"
    ri "..."
    ri "What the hell?"
    ri "Why is Noriko hanging out with a bunch of nerdy white guys?"

    scene black
    with dissolve2

    ri "Noriko, don’t go in the gym! I’ve made this same mistake before! You’re better than this!"
    n "{i}Oh, and that crazy, hot lady is Rika. She’s my friend’s mom. She’ll go away if you don’t make eye contact with her.{/i}"

    play sound "static.mp3"
    scene sportwarintro8 with flash
    stop sound

    "After a brief off-screen explanation detailing why Noriko is giving a small group of white people a tour of the school, Rika makes her way to the soccer field."
    "Her clipboard also expands in size by roughly 50%%, but that’s an unimportant detail that you probably didn’t even realize until I pointed it out just now."

    ri "So, uhh...hi!"
    ri "I know most of you have never talked to me before and probably don’t know who I am but, if you want to know who I’m definitely {i}not,{/i} it’s Rin’s mom. "
    r "Oh my fucking God."
    c "Looking good, Rika!"

    scene sportwarintro9
    with dissolve

    ri "Thanks, girl I definitely don’t know!"
    ki "Is it just me or does Rin’s mom have a really nice ass?"
    mi "Hm? Didn’t she just specifically say she {i}ain’t{/i} Rin’s mom? "
    ki "Oh, Miku. Never change."
    r "Why are you here?! Where’s Imani?!"

    scene sportwarintro10
    with dissolve

    ri "Hello, other girl I don’t know! You are very pretty and probably very smart! Imani’s setting up the obstacle course right now, so she asked me to read off this year’s Dorm Wars thingy to everybody."
    r "Just drop it on the ground and one of us will read it. Thanks!"

    scene sportwarintro11
    with fade

    ri "But this part specifically states “Despite what Rin says, under no circumstances should you drop this on the ground and let anyone else read it.”"
    r "Why?! "
    ri "I don’t know. Maybe there are some super secret details in it you’re not allowed to know?"
    f "You...haven’t read it yet?"

    scene sportwarintro12
    with dissolve

    ri" Hi, Futaba! I love you! Nice to meet you!"
    f "{i}Hah...{/i}Nice to {i}meet{/i} you too, Rika..."
    mak "Miss Rokuhara, if you need any assistance regarding the reading of this year’s briefing, I’d be happy to lend a hand. "
    mi "Rokuhara? Ain’t that Rin’s last name too? No wonder she had to warn everybody they ain’t related. That’d confuse me too if I didn’t already know the truth."

    scene sportwarintro13
    with dissolve

    ri "Nah, I’m good. Imani expects nothing but greatness from me, especially after learning how good I am at kissing. I will not let her down and have promised to read her words verbatim."
    r "Oh my God, stop!"

    scene sportwarintro14
    with dissolve

    ri "I will now read words to you!"
    ri "Ladies and other ladies, thank you for coming to this year’s annual Dorm Wars event! Even {i}if{/i} it’s taking place during a school day that you were all obligated to attend."
    ri "Given the lack of testosterone this year and the absence of the man you’d normally call the prize, I’ve decided to make things function a little differently."
    ri "From what I understand, the Dorm Wars have been synonymous with individual competition over the last few years. With some minor exceptions like Makoto’s weird Sensei-guarding game."
    mak "It wasn’t that-"
    ri "It is at this point that Makoto will interject about how it {i}wasn’t that weird{/i} and you should say, “Shut up, Makoto.” "

    scene sportwarintro15
    with dissolve

    ri "Shut up, Makoto! I’m saying this because I have to, not because I {i}want{/i} to!"

    scene sportwarintro16
    with dissolve

    ri "Now, direct your attention back to the clipboard and continue reading. "
    ri "While individual competition is fine and good, it’s {i}counterintuitive{/i} to the entire point of sports day. Which is why, this year, a greater emphasis will be placed on teamwork."
    ri "As such, I will {i}not{/i} be assigning specific people to specific competitions and, instead, allow you girls to choose who will be competing in each event yourselves!"
    u "Ourselves? But that means-"

    scene sportwarintro17
    with dissolve

    ri "Someone else will interject here and you will tell them there are caveats before an uprising takes place!"
    ri "Despite giving you the freedom to choose combatants yourselves, bear in mind that {i}all{/i} students must participate in at least one competition! With the exception of Ami as her absence is already noted."
    ri "Failure to adhere to this rule will result in a penalty of minus one point for each girl who does not participate."
    i "Oh, cool. This means I can abstain so long as we win a bunch of contests early. Good luck, Uta."
    c "Yumi’s not even here yet. So at this rate, you two might just cancel each other out."

    scene sportwarintro18
    with fade

    ri "Let’s see, where was...right. As always, there will be a total of ten competitions for a total of ten points. But the majority of these competitions will be team-focused and require multiple participants."
    ri "But seeing as not all of you are athletic, I’ve decided to throw a couple competitions into the mix that focus on {i}other{/i} strengths so everyone will have an opportunity to compete."
    ri "Additionally, the final two competitions of the SMUS-DDW: NBA - TEAaOKoSSEfBaB will {i}not{/i} require you to choose your competitors. "
    ri "One of these will involve names being chosen from a hat and the other will be a special showdown between yours truly and the evil Wakana Watabe of Class B, who will be representing the first floor."
    ki "Hell yeah! This means Imani is on our team! She likes us the most!"
    mak "It’s likely more due to the fact that Miss Watabe has been around for longer. Just as the first floor has-"
    ki "Blah, blah, blah. Imani is hot. Floor two wins."
    no "While Imani is, indeed, attractive, there is no one in this school more alluring than Miss Watabe. I would like to join the opposing team if possible, Miss Rokuhara. "
    no "I’m willing to provide a physical bribe if need be."

    scene sportwarintro19
    with dissolve

    ri "Hard pass. "
    o "Are we going to learn what the competitions are ahead of time? Or is this a thing we’re just going to have to figure out once they come up?"

    scene sportwarintro18
    with dissolve

    ri "I think I can tell you them now. I just needed to get her “preamble” thingy out of the way since she says you guys are all really resistant to change. "
    mo "Wait! There’s a vital piece of information that’s yet to be revealed! The light at the end of the tunnel! The loot inside of the chest that is sports day!"
    r "Translation: what’s the prize this year?"
    ri "She wrote “TBD.”"
    mi "One of these days, we’re gonna get an actual prize again."
    ki "She says, not yet knowing she is going to be crushed under the weight that is the second floor."
    mi "Your floor only weighs that much because of Touka’s boobs!"

    scene sportwarintro20
    with dissolve

    to "That was entirely uncalled for, Miku!"
    to "Besides, you have Futaba."
    mi "And Ami and Sana and Maya and me! We’ve got a severe disadvantage here and I ain’t about to lose to boob weight!"
    ri "Can I read the competitions now or do we want to talk more about boobs?"
    ki "There’s only one way to truly discover which floor is the most boobalicious and it’s for all of us to-"
    c "Ignore the whore and get back to the task at hand! "
    ki "I love it when you talk dirty to me, Chika."

    scene sportwarintro21
    with fade

    ri "Man. You’re all horny as hell, aren’t you?"
    f "Not all of us..."
    mo "Just the good ones."
    no "I couldn’t have said it better myself."
    o "No, but you could have made it way wordier and harder to understand."
    no "Yes, but so could Yasu and we all seem to love her."
    ya "Love is but a delusional state of mind in relation to all but He who-"
    ri "Once Yasu begins to preach, things have gone too far. At that point, please read out the competitions regardless of the current conversational status. {i}Roger.{/i}"
    ri "Competition one — egg toss. Two girls from each floor face off against one another to see who can keep their egg alive the longest."
    ri "Competition two — trivia. A one-on-one return of everyone’s favorite knowledge-based competition that’ll serve as an opportunity to get non-athletes involved again."
    ri "Competition three — obstacle course. Another one-on-one competition that’s sure to get the hearts of {i}everybody{/i} pumping due to its crazy and quirky nature. Bring a weapon."
    u "Well, we’ve found Ayane’s competition."
    sa "And...Tsuneyo’s..."
    t "My entire body is a weapon. I will prove this once more today. "
    ri "Competition four — cheerleading. Two girls from each floor will team up to see who can form the best cheer. Please remember you are at school and keep most of your clothes on."
    ki "{i}Tch.{/i}"
    ri "Competition five — scavenger hunt. A sports day classic and the last one-on-one competition prior to the teacher showdown at the end. "
    ri "Competition six — relay race. "
    mi "Heck yeah! It’s finally my time to shine! No more of that fashion show nonsense!"
    c "Awww but gyaru Miku was adorable and I miss her!"
    mi "Fast Miku is better! Y’all ain’t got a chance! Ya hear me?!"
    ri "I see you guys already understand what a relay race is, but I should probably let you know that one is going to be three-on-three."
    ri "But, moving onto competition seven — death ball. There are currently no details about what death ball is. Please check back later."
    mo "Well, that’s not worrying at all."
    ya "Death is-"
    ri "Competition eight — the five-legged race."
    ay "Five? Are you sure it’s not supposed to be the three-legged race?"
    ri "It says, “Not three!” in parentheses, so probably. "
    sa "Where...are we supposed to get the extra legs?..."
    r "I’ll call my skull guy. He’ll know what to do."
    ri "Competition nine — the newly-newlywed game."
    u "Wait, is {i}that{/i} the game being randomly assigned to us? "
    i "And what time is that starting exactly? I want to know when I should head back to the dorm."
    f "What even...{i}is{/i} a newly-newlywed?"
    mi "Beats me, but it’ll sure make somebody happy with the amount’a bisexuals we’ve got up in here."
    ki "Present. "
    c "Present."
    ki "Doing anything later, Chika?"
    c "Yes, avoiding you."
    ri "And competition ten — a very special teacher showdown featuring a classic party game while the night comes to an end."
    ri "The following morning, we’ll reconvene and read out the results of the competition. But please be advised that there will be no unapproved “bonus contests” this year. There will be no exceptions."
    ri "That is all."

    scene sportwarintro22
    with fade

    ay "{i}Hah...{/i}I love sports day, but this just feels wrong without Sensei. What good is a competition if we don’t have a handsome older man to choose which one of us is the winner?"
    m "Yeah, I’m not doing this."

    scene sportwarintro23
    with dissolve

    ay "What do you mean you’re not doing this? Didn’t you hear Rika? We’ll lose a point for every girl who doesn’t compete."
    m "Didn’t you hear the annoying, anti-social green-haired girl? She’s not going to compete either. Which means that even if Yumi {i}and{/i} I don’t compete, we’ll only have a one-point disadvantage. "
    ay "But...we’re already down one girl with Ami being absent. And even if she’s excused, expecting seven of us to handle the rest of the competitions is putting way too much weight on our shoulders."
    m "Are you saying you aren’t up to the challenge?"
    ay "No, I’m saying I don’t understand why you’re trying to drop out before we’ve even distributed roles. "
    m "Oh. Because I’m leaving."

    scene sportwarintro24
    with dissolve

    ay "{i}Leaving?{/i}"
    m "Yeah. This sucks. I don’t want to be here anymore."
    ay "Maya...you can’t just {i}leave.{/i} The whole point of sports day is to work as a team. You’re really going to just...give us a handicap like that?"
    m "That’s the plan, yeah. Besides, there’s something else I want to do instead."
    ay "And what’s that? What’s more important than-"

    scene sportwarintro25
    with dissolve

    ay "..."
    m "..."
    ay "You’re tired of waiting, aren’t you?"

    scene sportwarintro26
    with dissolve

    m "..."
    ay "Why {i}now?{/i}"
    ay "Why would you wait until we’re all together to break off and {i}follow your heart?{/i}"
    m "I’m afraid I don’t know what you’re talking about."
    ay "Maya, you know what I’m talking about. You can’t fool me."
    m "Right. Because...Past-Maya already explained to you how she felt or something, correct? And you’ve transplanted those feelings into Real-Maya. IE: me. "

    scene sportwarintro27
    with dissolve

    ay "I just don’t understand why it has to be {i}now.{/i} You’ve had so many other chances."
    m "You don’t have to understand. You just have to cover for me and do your best to win all of the competitions while I go “follow my heart” as you so aptly put it."
    ay "Because that’s what it is and you know it."
    m "Do I?"
    ay "What will you do if you find him?"
    m "Who?"

    scene sportwarintro28
    with dissolve

    ay "..."
    m "..."
    ay "What will you do if you find him?"
    m "Would you believe me if I said I was going to ride him like a mechanical bull?"

    scene sportwarintro29
    with dissolve

    ay "Woah."
    m "You want honesty? There you go. Were you hoping for a different answer?"
    ay "I’m just...not used to hearing you be so open like that."
    m "And I’m not used to you prying personal details out of me like this. "
    m "You’ve been acting weird lately, Ayane. And all of this gaslighting about how I’m {i}not who I think I am{/i} and that you {i}know so much about me{/i} is starting to get on my nerves. "
    m "So please excuse me while I go confront a grown man and ultimately allow him to use my body like a sex toy."

    scene sportwarintro30
    with dissolve

    m "Peace."

    scene sportwarintro31
    with dissolve

    ay "..."
    m "Oh, and good luck or whatever. "
    m "Have fun."
    ay "..."
    ay "Well, I don’t like this one bit."

    scene sportwarintro32
    with fade

    o "..."
    no "..."
    o "Nodoka."
    no "Yes, my love?"
    o "You’re staring at me an awful lot today."
    no "Am I?"
    o "You sure are. And it’s starting to creep me out."
    no "You just seem...{i}different.{/i} That’s all. More...depraved."

    scene sportwarintro33
    with dissolve

    r "..."

    scene sportwarintro34
    with dissolve

    no "Ah, thank you."

    scene sportwarintro35
    with dissolve

    no "Did something happen? A chance encounter on a long walk home? A secret rendezvous with a boy you met on the Internet? A girl perhaps?"
    o "Why would I tell you even if any of that was true? It would just end up in a book. "
    no "And that doesn’t excite you?"

    scene sportwarintro36
    with dissolve

    ki "..."

    scene sportwarintro37
    with dissolve

    no "Thank you very much."

    scene sportwarintro38
    with dissolve

    no "Otoha, from one {i}creator{/i} to another, doesn’t the idea of being a part of something greater have some sort of appeal to you? I assumed you’d {i}love{/i} simply being a character."
    no "For all you know, a young boy could stumble across my work accidentally and take great {i}pleasure{/i} in your {i}exploits.{/i} "
    o "Mhm. Right. Or {i}you{/i} could. "
    no "And that’s a bad thing? "

    scene sportwarintro39
    with dissolve

    mo "..."

    scene sportwarintro40
    with dissolve

    no "Thank you very much."

    scene sportwarintro41
    with dissolve

    no "Anyway. As I was saying-"
    o "Yeah, forget what you were saying. Why do people keep coming over here and handing you a sheet of paper?"

    scene sportwarintro42
    with dissolve

    no "Whatever do you mean?"
    o "You’re literally holding onto them. They’re {i}right{/i} there."
    no "Otoha, you’re going to have to speak up. I can’t quite hear you."

    scene sportwarintro43
    with dissolve

    o "Nodoka, what are you planning this time? What is this?"
    no "I’m not {i}planning{/i} anything, Otoha."

    scene black
    with dissolve2

    no "I’m just trying to give back to the community. "

    $ renpy.end_replay()
    $ sportswars1 = True

    jump sportswars2

label rikaspring1:
    scene nightsky
    with dissolve2
    play music "fallishere.mp3"

    "It’s Saturday night and I’m ready to party."
    "Just kidding. I hate myself and I’m ready to die."
    "But it {i}is{/i} Saturday night, and that means something to most people. So I will stand here in the middle of the sidewalk and wait for someone to drag me into whatever they’re doing right now."

    s "..."
    s "..."
    s "..."
    s "I’m bored."

    play sound "phonering.mp3"
    with hpunch

    "Upon voicing my boredom, my phone immediately begins to ring, proving once more that there probably {i}is{/i} a god out there watching over me and toying with my every emotion."
    "Now please excuse me as I continue to ignore it in favor of whoever’s on the other end of the phone."

    play sound "phonebeep.wav"

    s "Hello?"
    ri "Yo! Happy Saturday. Are you ready to party?"
    s "You know it, Rika."
    ri "Okay, never mind then. I needed help with something."
    s "Oh."
    s "Well...I’m ready for that too, I guess. What do you need help with?"
    ri "I’m officially moving into my new place today and need some extra hands. Imani’s coming too. So I’ll buy you guys pizza or beer since the Internet said that’s how I’m supposed to pay friends who help me."
    s "I could have sworn you already had a place of your own. Have you really been with Rin this entire time?"
    ri "I’ve been moving around. Long story. But this place should be cool! I think. I hope. Maybe. Anyway! Are you in or out? Speak now or I will forever hold this pizza."
    s "I’m in. Just send me the address."
    ri "Oh, shit. I forgot to get the address. Let me call you back!"
    s "Just text it to me, Rika."
    ri "No can do, bud! The government is watching. They read every single one of our texts."
    ri "Anyway, BRB. I have to text the landlord my kojin bangō so they know I’m legit and can send me the address. But then I’ll call you back! Promise!"
    s "..."
    ri "You still there?"
    s "Yeah."
    ri "Well, stop! Do some stretches or something! And start heading over! Bye!"

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "Rika hangs up the phone and I am once again very worried about how she is ever supposed to survive on her own."
    "At least when she was rooming with Rin, she had {i}her{/i} to rein her in and...probably teach her how to do laundry and whatnot. But now, I fear that person is going to wind up being me."
    "And that’s very worrying since I only kind of know how to do laundry. Or anything really."
    "Oh well. I’ll just hope that she finds another girlfriend soon. Or that all of my school-friends adopt polyamory so she can just join the Wakana/Osako relationship."
    "And hey, if those two are still struggling, maybe Rika can be the missing link that binds their chain back together?"

    play sound "static.mp3"
    scene rikasnewplace1 with flash
    stop sound

    "Or maybe that would make life way too convenient for everyone involved and only serve to tear down the barrier between all of them and my penis. So hey, a man can dream."
    "And a man can also help move stuff around in exchange for pizza and beer, so excuse me as I graduate to a level past “confused adolescent boy in a grown man’s body” for an hour or two."

    ri "Hey! Thanks for showing up. I decided to keep Imani outside so the two of you could see how awesome and cool my new apartment is at the same time."
    ima "Hey, Senpai! Were you able to find the place okay?"
    s "Yeah. Really easily, actually. "
    ima "Oh yeah?"

    play sound "static.mp3"
    scene rikasnewplace2 with flash
    stop sound

    ima "Was it because {i}my{/i} apartment is literally right there?!?!?!"
    s "You know, I thought this place looked familiar."
    ri "What’s the problem, Imani? Now we can stay up all night and talk about when we were young. You can even teach me how to do laundry!"
    ima "Don’t remind me that I’m not young anymore! I am very sensitive when it comes to that subject!"
    ri "Then why are you going around making out with people in their forties?"

    scene rikasnewplace3
    with dissolve

    ima "That was {i}one{/i} time."
    ri "And a totally forgettable one at that! So yeah, now it’ll be easier for you to find me. Which you’ve never attempted to do before. But now you can! If you want. Which you probably don’t."
    s "I’m already over here a decent amount since Imani’s two doors down and the girl in the room next to yours is another one of my friends."

    scene rikasnewplace4
    with dissolve

    ri "You’re friends with the cool biker bartender lady? What’s her name? I forgot. Is she a lesbian? Because my gay-dar didn’t ring at all, but I’m getting conflicting vibes from all the leather and denim."
    ima "You’ve lived here for three minutes and you’re already planning on hooking up with your neighbor?"
    ri "You know what they say, Imani. If the shoe fits, go fuck a girl."

    scene rikasnewplace5
    with dissolve

    ima "Since when do they say that?..."
    s "Yuki is, to my knowledge, very straight. But you’ve {i}turned{/i} women before, so maybe you can work your magic on her as well."
    ri "Do you know her age? Is she older than me?"
    s "Late thirties, I believe."

    scene rikasnewplace6
    with dissolve

    ima "Damn, really? Could’ve fooled me. She looks way older than Rika."
    s "Yeah, but Rika also looks way too young for her age and Yuki had a drug problem for a while. I’m sure that plays some role in her appearance."
    ri "I’m starting to worry that I’m the oldest woman in Kumon-mi...No one is ever going to love me again and Rin is going to have to find a third mom when the garbage men accidentally collect my body."

    scene rikasnewplace7
    with dissolve

    ri "Oh well, though. If all else fails, I guess there’s you. I can subject myself to a life of 6/10 makeout sessions if you’re above average when it comes to hand stuff."
    ima "Rika, this better be a fuckin’ {i}damn{/i} good pizza."

    scene rikasnewplace8
    with dissolve

    ri "Fuck! I forgot the pizza!"

    scene black
    with dissolve

    s "Weren’t you literally holding it when you called me? "
    ri "I must have dropped it somewhere! Why does this keep happening to me every time I buy a pizza?!"
    ima "This has happened more than once?!?"
    ri "Oh! You know what, maybe I left it inside before you guys got here. There’s only one way to find out! Onward, gang!"

    play sound "dooropen.mp3"

    "Rika pushes her way through the door and pridefully marches to the center of a room that looks a lot like Imani’s and Yuki’s."
    "Just...with one glaring difference."

    play sound "static.mp3"
    scene rikasnewplace9 with flash
    stop sound

    ri "Isn’t it just beautiful?! I bet Rie’s shaking in her boots now. Rika’s back on the market and back out in the world! "

    scene rikasnewplace10
    with dissolve

    ri "Wait, when did Rie get boots? Rie never wore boots. Are they {i}mine?{/i} Do they still fit?"
    ima "Rika, question. What the fuck is going on in here?"

    scene rikasnewplace11
    with dissolve

    ri "Huh? What do you mean?"
    s "I think she’s talking about how the place is completely empty. Both Imani and Yuki’s places came furnished."
    ima "I mean, I’m not sure if I’d say {i}completely{/i} empty. "

    play sound "static.mp3"
    scene rikasnewplace12 with flash
    stop sound

    ima "There’s certainly...{i}some{/i} stuff in it."
    s "Yeah, I feel like this might be one of those cases where less would actually be more."
    ri "It’s a work in progress, sure! But I got a hefty discount after the last couple in here was murdered. They wouldn’t let me keep any of their stuff, though. Dumb rule."
    ima "You actually {i}wanted{/i} it?"
    ri "You really think I’m in the position to turn down a free couch, Imani? Plus, those girls had a damn Macbook. A {i}Macbook!{/i} I’ve always wanted to read one of those."

    scene rikasnewplace13
    with fade

    s "Does she think a Macbook is an actual-"
    ima "Would it really surprise you if she did? Rika, this is an active crime scene. You can’t live here."
    s "There’s also a rat eating an entire cheese wheel on the ground."
    ri "Oh, yeah. I gave him that. He’s my son now. And soon, he’ll be off to rat college where he’ll live in his little rat dorm and-"
    ima "Rats live for like three years max."

    play sound "static.mp3"
    scene rikasnewplace14 with flash
    stop sound

    ri "Nooooo! My son!"
    ima "I’m never going to get another minute of peace in this apartment complex again, am I?"
    s "Rika, why are we even here?"

    scene rikasnewplace15
    with dissolve

    ri "You really think {i}I’m{/i} the person you should be asking that question to? I only just learned where the ropes are a couple months ago. Give me a break, man."

    scene rikasnewplace16
    with dissolve

    ima "No, Rika. He’s obviously talking about how you called us over here for the sole purpose of helping you move. But you have nothing {i}to{/i} move."
    ri "{i}Technically,{/i} I never said I needed help moving — just that I needed extra hands."

    scene rikasnewplace17
    with dissolve

    ri "Which I {i}do{/i} for all the high fives I should be getting! Put her there, homie!"
    ima "Rika-"

    play sound "slap.mp3"
    scene rikasnewplace18 with hpunch
    scene rikasnewplace19 with dissolve

    ima "Don’t encourage her! She just wasted hours worth of time that we could have spent having sex with each other!"

    scene rikasnewplace20
    with dissolve

    ri "Yeah, except for the part where you guys don’t even {i}have{/i} sex. Remember how I almost paid the taco guy to bone you? That like literally {i}just{/i} happened."
    s "Taco guy? You mean Taco {i}Man?{/i} The one who works in the subway? "
    ima "Probably. He sell tacos?"
    s "I’m not sure he knows how to do anything else."
    ri "Yeah well you might be right because he didn’t seem all that excited about boning Imani either. Maybe she’s just cursed."
    ima "Rika, you are right. We haven’t had sex."
    ri "Duuuuuh. If that happened, you guys-"

    scene rikasnewplace21
    with dissolve

    ima "But Senpai {i}may{/i} have eaten me out for over three hours in one sitting. So sex is clearly the next step."

    scene rikasnewplace22
    with dissolve

    ri "{i}Haaaaaaaaaaaaaah!!!??!?!!{/i}"
    ima "You look...{i}way{/i} too happy about this. "
    s "Are you sure it’s okay to just come out and tell her like that?"
    ri "Okay?! Why would it not be okay?! This is the greatest news I’ve ever heard in my life!"

    scene rikasnewplace23
    with dissolve

    ri "Two of my best friends engaging in a healthy session of consensual cunnilingus for {i}three{/i} whole hours?! KYAAAAAH!"

    scene rikasnewplace24
    with dissolve

    ri "Wait. It {i}was{/i} consensual, right? She didn’t just force you down there?"
    s "It was consensual, yes."

    scene rikasnewplace23
    with dissolve

    ri "{i}Haaaaaaaaaaaaaah!!!!!!!!!{/i}"
    ima "Bruh. "

    scene rikasnewplace25
    with dissolve

    ri "Hey, you can’t blame me for thinking you might have gone a little stir crazy the moment you saw him. A decade-long dry spell could {i}kill{/i} a girl. I start feeling faint after like one month."
    s "But it’s been way longer than a month since you’ve broken up with Rie hasn’t it?"

    scene rikasnewplace26
    with dissolve

    ri "Yes."
    s "..."
    ri "..."

    scene rikasnewplace27
    with dissolve

    ima "..."

    scene rikasnewplace28
    with dissolve

    ima "..."

    scene rikasnewplace29
    with dissolve

    ima "If you fuck Rika before me...I swear to God, Senpai."
    s "Well, considering that we now have an entire night to {i}not{/i} help Rika move-"

    scene rikasnewplace30
    with dissolve

    ri "Hell no, we don’t! The hands part might be over after the singular high five I received, but now we’ve gotta celebrate the two of you finally tying the labial knot!"
    ima "Can you please never call it that again?"
    ri "Fine. Then we’ve gotta celebrate how this nonstop game of “will they, won’t they” has turned into a {i}completed{/i} game of “they will!”"

    scene rikasnewplace31
    with dissolve

    ri "I’m like, {i}super{/i} happy for you guys. No joke. You deserve nothing but happiness and multiple orgasms every night for the rest of your life. "
    ima "Well...thanks, Rika. I...{i}we{/i} really appreciate that. "
    ima "But it’s not like we have to {i}celebrate{/i} it. Let’s just...head over to a furniture shop and try to find you...a futon or something so you don’t have to crash at my place again."
    s "This late at night? Nothing’s going to be open."

    scene rikasnewplace32
    with dissolve

    ri "Yeah, but I can’t go back to {i}your{/i} place either if you’re about to invite me since you’re Imani’s crush and probably my daughter’s too."
    s "I’m not inviting you to my place. I’m {i}agreeing{/i} that we should go out and celebrate. Even...if it feels kind of strange to throw a party over me putting my mouth on Imani’s vagina."
    ima "Low key, Wakana and I already threw a mini-party about that. But that party was pretty much just the two of us getting shit-faced and binging all of Wednesday on Netflix. Her choice, obviously."

    scene rikasnewplace33
    with dissolve

    ri "Then it’s {i}definitely{/i} my turn! {i}And{/i} it will give me the excuse to use some of the money I saved from this apartment on repaying {i}you{/i} guys! Everyone wins!"

    scene rikasnewplace34
    with dissolve

    ri "Except the Yamazaki family. God rest their souls."
    ima "..."
    s "..."

    scene rikasnewplace35
    with dissolve

    ri "Okay! Resting done! Let’s go get drunk and talk about all the sex you two are gonna have from now on!"

    scene black
    with dissolve2
    stop music fadeout 15.0

    ima "{i}Hah...{/i}fiiiiine. But I swear, if you bail before we get the check, I {i}will{/i} find you. I know where you live now."
    ri "Have I ever done that before?"
    ima "Yes. Several times."
    ri "Wait, really? Also, can I crash at your place again tonight? Because the alternative is Sensei’s place and you saw the way we looked at each other a couple minutes ago. There’s tension there."
    ima "Yeah, I noticed and I hate it! So yes, you can sleep at my place! And you are now banned from making eye contact with Senpai for the rest of the night."
    ri "But his eyes are so pretty! Look! Look at ‘em!"

    "Rika grabs my face and aims it at Imani while pushing the two of us outdoors. "
    "But just as we turn the corner to head over to our regular dive bar, Rika proclaims that she wants something more {i}special{/i} tonight."
    "My suggestion of a love hotel is promptly denied by both of them (which is honestly surprising, but whatever) so I suggest another bar instead."
    "And seeing as I only know one other bar, you can probably guess where we’re headed..."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ rikaspring1 = True

    jump rikaspring2

label rikaspring2:
    scene nightsky
    with dissolve2
    play music "calmbar.mp3"

    "Sakaki-bar-a — a place where everyone knows your name. Unless your name is Akira. "
    "If {i}that’s{/i} the case, chances are {i}you{/i} didn’t even know your name until recently. And also, you have a terrible hobby/addiction and need to find a new one ASAP."
    "Anyway, a quick taxi ride takes us right up to the doors, but I notice right away that things don’t seem as...hectic as they’ve been lately."
    "The streets are quiet and empty, and the only sound that can be heard apart from my two friends bickering is the electric hum of a new sign Sara bought with some of the bar’s profits."

    scene black
    with dissolve2

    "I push open the doors and guide the two of them to my normal seat, which isn’t entirely necessary as it’s not their first time here, but it {i}does{/i} make me feel cool."
    "But what makes me feel even cooler is that Sana, who appears to be the only one working tonight, quickly brings all three of us beers without me even needing to part my lips."

    scene rikaspringbar1
    with dissolve2

    "Which brings us to now, roughly thirty minutes and three beers deep into the night as smooth jazz drones on in the background."

    ri "Say, why don’t we come {i}here{/i} more often? I didn’t even realize this place was open for non-events and shit."
    ima "Do you think it might have something to do with the fact that our regular bar is only a couple blocks away from my apartment?"
    ri "I have no clue. That’s why I asked."
    ima "Okay. Well, I think it has something to do with the fact that our regular bar is only a couple blocks away from my apartment. "
    s "Wakana and Osako don’t live that close by, though. "

    scene rikaspringbar2
    with dissolve

    ima "Yeah, but you {i}know{/i} the two of them are getting up to no good on the train. Wouldn’t put it past either of them to stakeout the busiest cars during rush hour just so they can live out some fantasies."
    ri "I fingered Rie on the train once. But I’m a ninja so no one noticed."

    scene rikaspringbar3
    with dissolve

    ima "Very nice, Rika. But you might want to watch what you’re saying in front of one of the girls who is {i}literally in the club you advise.{/i}"

    scene rikaspringbar4
    with fade

    ri "Oh, right. Hi Sana. Please don’t report me to upper management. They’re scary and I need money for rat college."
    sa "You don’t have to worry about that...I’ve heard much worse from my mom’s friends and-"
    sa "Did you say “rat college?”"
    ima "It’s for her son."
    ri "Yup! But I just found out he doesn’t have much time left..."
    sa "I’m sure...Rin will be happy to...not be an only child anymore...even if it’s only for a little while..."
    s "Can you get me another beer, Sana? Whenever you have a second."

    scene rikaspringbar5
    with dissolve

    sa "Mhm. I just need to...finish putting away the wine glasses...I’m running behind since...I’m working alone again tonight..."

    scene rikaspringbar6
    with fade

    ri "Yeah, the hot biker girl was here last time! "
    ri "Where’s she tonight? I have to get her number and find out how she feels about the female body. Or how she feels the female body. Whatever comes first. Probably her. I’m a ninja."
    sa "I...actually don’t know..."
    sa "She was supposed to work tonight, but...she just...hasn’t shown up, so...I’m just glad we’re slow..."
    s "Has that happened before? I thought Yuki had been really good when it came to work stuff?"

    scene rikaspringbar7
    with dissolve

    ri "New boyfriend maybe? Girlfriend? Did I manifest her into being gay? If so, I’m sorry. Just not really."
    ima "Bitch, you two have talked like one time. Keep yo’ damn pants on."
    ri "Well gee, Imani. Sorry. Not all of us can just willingly be abstinent for seven years."
    sa "She’s...never done this before, but...I’m sure she just...made a mistake when she...looked at the schedule or something..."
    sa "It’s not a...big deal..."

    scene rikaspringbar4
    with fade

    sa "Do you...actually have a crush on her?... "
    ima "No, she just has a crush on everyone."
    s "Perpetual loneliness will do that to a person."
    ri "Ninjas do not know emotion. I’m a lone wolf who stalks the shadows. I just think it’d be cool to make out with her. "
    sa "Yeah...I’m pretty sure my mom does too..."

    scene rikaspringbar8
    with fade

    ri "Man! Isn’t there anyone around here who {i}isn’t{/i} already interested in somebody else? Am I really gonna have to date that Nodoka girl who keeps trying to pull me into the storage room?"
    ima "Yeah, you’re gonna want to stay as far away from her as possible. And I ain’t just saying that because of the age gap."
    ri "{i}I know.{/i} Shit’s just hard, man."

    scene rikaspringbar9
    with dissolve

    ri "You go from thinking you’re gonna be spending the rest of your life with one girl...raising a kid together...buyin’ a damn house...and then it’s just over? That’s it? "
    ri "Like...I’m not trying to bring down the mood since this is supposed to be a celebration and all, I just wish I had somebody to share happy moments with, you know?"

    scene rikaspringbar10
    with dissolve

    ri "And now, to top things off, I might have to watch Wakana and Osako go through the same song and dance I had with Rie. There’s just misery and lesbian sadness everywhere I look. Rin and Otoha too."
    s "Rin will be fine. It seems like she’s basically over Otoha already. "
    ri "Yeah, but that probably means she’s just gonna fall for Chika again and get a third dose of heartbreak before I even get a shot at a second."
    ima "Rika, as someone who’s...already been through a tough breakup...what do {i}you{/i} think is going to happen to Wakana and Osako?"

    scene rikaspringbar11
    with dissolve

    ri "That’s...tough. Nobody on the outside can ever really understand what’s going on in somebody else’s relationship."
    ri "My gut instinct is that they’ll be able to work through it. But my gut’s not always right since I thought I’d be able to work stuff out with my partner too."
    ri "Neither of them really, like...{i}talk{/i} to me the way you guys do. So it’s not like I really know what’s going on in the first place. I just...feel the tension. The bad kind. Not the kind you guys have."

    scene rikaspringbar12
    with dissolve

    ri "But I guess the bright side to all of this sad stuff is that you two are actually hooking up now! "

    play sound "glass.mp3"
    scene rikaspringbar13 with hpunch

    sa "..."

    play sound "static.mp3"
    scene rikaspringbar14 with flash
    stop sound

    s "..."
    ima "Uh...you okay, Sana?"

    play sound "static.mp3"
    scene rikaspringbar15 with flash
    stop sound

    sa "I’m fine. "
    sa "That glass was just a little slippery, that’s all."
    ri "You...need us to help clean it up or anything? "
    sa "No, that’s okay. But I think I might have cut my hand."

    scene rikaspringbar16
    with dissolve

    sa "Sensei, could you come to the kitchen and help me wrap it up please?"
    s "Uh...sure. "
    s "I’ll be...right back, I guess."

    scene rikaspringbar17
    with fade

    ri "..."
    ima "..."
    ri "Are those two fucking?"

    scene rikaspringbar18
    with dissolve

    ima "Rika, ew! What the fuck?!"
    ri "What?! That felt weird as hell, didn’t it?!"
    ima "So your gut instinct is to think they’re having sex?!"
    ri "I already told you my gut’s been wrong before! I’m just calling it like I see it! I hope it’s not true either! That’s gross {i}and{/i} bad news for you!"

    scene rikaspringbar19
    with dissolve

    ima "{i}Hah...{/i}that was just a one time thing, unfortunately. It’s not like we’re actually dating. "
    ri "True. But, speaking from experience, you don’t go down on somebody for hours at a time if you {i}don’t{/i} want to date them. "
    ri "Once you pass the sixty-minute mark, it {i}means{/i} something. So at least you’ve got that, buddy."

    scene rikaspringbar20
    with dissolve

    ima "You really think that’s true?..."
    ri "Absolutely. Not a doubt in my mind."
    ima "..."
    ri "..."
    ima "..."
    ri "..."

    scene rikaspringbar21 with hpunch

    imarika "AAAAAAAAAAAAHHHHH!!!!!!"

    scene rikaspringbar22
    with dissolve

    ri "You’ve gotta tell me all about it. How’d it happen? Did he actually know what he was doing? Was it really just oral? Spare no detail. I must know."
    ima "It was {i}amazing.{/i} And so unexpected too. I had no idea it was even coming. "
    ri "Was it at your place? His place? Love hotel? Where?"

    scene rikaspringbar23
    with dissolve

    ima "A room at an inn on the beach. The place we use for all the class beach trips. "
    ri "You did it during the class beach trip?! You frisky little freaks, you!"
    ima "It was right before the class trip, actually. We went there on...our own. With nobody else. "

    scene rikaspringbar24
    with dissolve

    ima "We spent the whole day together...I told him some stuff about my past..."
    ima "Then, when we went back to the room, I showed him my swimsuit and he was just like “{i}take it off!{/i}” So of course I was nervous as hell but...{i}oh my god.{/i}"

    scene rikaspringbar25
    with dissolve

    ima "I kid you not, I had no idea it was even physically possible to cum so many times in one- are you crying?"
    ri "I’m just...so happy for you..."

    scene rikaspringbar26
    with dissolve

    ima "Me too, man! But don’t cry! You’re killing the vibe and I want to tell you more about how friggin’ awesome it was."
    ri "I’m sorry, I’m sorry! I’d just given up on the possibility of the two of you ever getting together, so this is all so crazy to me."

    scene rikaspringbar27
    with dissolve

    ima "Well, don’t just...count me out, yo. Senpai and I have been close since day one. I wouldn’t have been able to hold out as long as I have if I didn’t think it was possible."
    ri "Of course it’s possible! It’s obviously possible. It basically happened. I just figured it was going to be Wakana before you."

    scene rikaspringbar28
    with dissolve

    ima "But...Wakana’s with Osako. The two of them have been together since college. We literally just talked about this. "
    ri "I mean, yeah. But you see the way she and Akira look at each other sometimes, right? "
    ri "Are you really gonna look at me and tell me those two don’t want to fuck each other into a coma? We all know it. Hell, Osako probably knows it too. That might be why they’re fighting. "

    scene rikaspringbar29
    with dissolve

    ima "Wait, wait, wait, wait, wait. There’s no way Senpai would be the reason they’re fighting. And just because they might want to take each other’s clothes off doesn’t mean Wakana actually {i}would.{/i}"
    ima "She {i}loves{/i} Osako. She tells me about it all the time. She’s loyal as all hell."
    ri "I’m not saying she would actually cheat. Just that if {i}I{/i} were in Osako’s shoes and I had a feeling my partner wanted to screw somebody else, I’d probably say or do some pretty stupid shit."
    ima "Yeah, but you say and do pretty stupid shit all the time {i}without{/i} being in that very specific scenario, so that’s just...not a good sample."

    scene rikaspringbar30
    with dissolve

    ri "And that’s a totally fair counterpoint thingy! I probably {i}am{/i} wrong. {i}You’re{/i} the one he actually hooked up with in the end, so {i}you’re{/i} the one who’s winning now."
    ima "Saying I’m winning makes it sound like a contest, though..."
    ri "Love {i}is{/i} a contest, Imani. And it’s one that never ends, so you’ve {i}always{/i} gotta be competing. "
    ri "There are like ten million people on this planet, and any {i}one{/i} of them could snatch away the person you’re after if you let your guard down. You gotta remember that."
    ima "Rika, there are almost eight {i}billion{/i} people on earth."

    scene rikaspringbar31
    with dissolve

    ri "Wha- well, that’s like five times worse, damn it!"
    ima "How did you get a job at a school?"
    ri "How did {i}you{/i} get a job at being eaten out by a hot young stud?!"

    scene rikaspringbar32
    with dissolve

    ima "That isn’t my job, you friggin’ weirdo!"
    ri "Yeah, but it {i}should{/i} be!"

    scene rikaspringbar33
    with dissolve

    ri "I know Akira’s type, Imani. I hooked up with plenty of dudes like that in my teens who probably went on to bang like a hundred girls. Which is why I’m telling you you’ve gotta lock that dude down."
    ri "Sex might be the goal right now, but that’s not all you {i}really{/i} want in the end, is it? You want somebody to share happy moments with too. You’re like me. New me. Not old me. "
    ri "Well, technically old me. But old me is the new me. "
    ima "..."
    ri "Old like age. Like, new me is old of age. And old me is-"
    ima "Yeah, I get what you’re trying to say. And..."

    scene rikaspringbar34
    with dissolve

    ima "And...you’re right. Maybe this {i}is{/i} one big contest. But could you really say I’m {i}winning{/i} right now when we’ve only done shit one time? "
    ima "As a matter of fact, I’m almost positive I’m {i}losing{/i} since he fucked some other girl like crazy in the room right next door to me once. I just can’t say who since I signed an NDA."
    ri "Then that’s all the more reason to {i}fight,{/i} girl. You’ve come this far, haven’t you? Go give that dude the ride of his life. So long as that’s not what Sana’s doing as we speak."

    scene rikaspringbar35
    with dissolve

    ima "Wait, yeah. Those two have been gone for a while."
    ri "I said what I said and I won’t say it again."
    ima "Do you..."
    ima "Do you think we should, like...go check on them?"
    ri "I don’t know. I kinda want to stay out here and keep talking about sex since, depressingly, you are now defeating me in that area of my life."

    scene rikaspringbar36
    with dissolve

    ima "Well, hopefully you’ll be able to convert the neighbor soon."
    ri "Hopefully. Because other than that, my best option seems to be becoming the third member of a threesome with you and Akira. And I can’t do that without disrupting the dynamic of our friend group."

    scene rikaspringbar37
    with dissolve

    ima "..."
    ri "..."
    ima "I mean...would it {i}reeeeeeally{/i} disrupt anything? "
    ri "..."
    ima "Can’t some friends just have a one-off night of...sexual exploration without completely changing the dynamic of-"
    ri "You {i}motherfucker.{/i}"
    ima "..."

    scene rikaspringbar38
    with dissolve

    ima "It wasn’t my idea! I wanted a nice, old-fashioned one-on-one encounter! They pressured me!"
    ri "Unforgivable! You participated in a night of platonic passion while I was feeding a cheese wheel to a rat?!?! How could you do this to me?!"
    ima "It was before you ever met the rat! I swear!"

    scene black
    with dissolve2
    stop music fadeout 15.0

    s "Hey. What’s going on? What happened with the-"
    ri "You! Both of you! Let me smell you! I need to make sure nothing inappropriate happened!"
    sa "Wha- Sensei?!"
    s "{i}Run.{/i}"
    sa "I...aah! The wound on my...hand reopened! I must...dress it!"
    ri "Get back here or I’ll never teach you paradiddles, damn it!"
    sa "I don’t even know what that means!!!!!"

    "Sana manages to escape, and I manage to go undetected as Rika thoroughly inspects my body and finds nothing. Probably because I never laid a finger on Sana the entire time I was in the kitchen."
    "That does not mean, however, that she did not lay a finger on me. "
    "Or a mouth."
    "On my penis."
    "But that is beside the point."
    "I sit back down at the counter and quickly find that I still have not received the new beer I asked for earlier. Probably because the bartender was going down on me. "
    "That’s fine, though. It’s getting late anyway."
    "Imani and Rika finish their drinks a short while later. But, before we leave, there’s a moment of silence where the three of us just...sit there."
    "The jazz music continues to drone on and Rika closes her eyes. But I’m unsure of whether or not she’s just tired or absorbed in the song."
    "Regardless, it gives me the chance for one more bout of prolonged eye contact with Imani...and she smiles that same smile she always does."
    "But the light blue in her eyes seems a little bit darker and I can’t tell quite why."
    "We leave the bar. All three of us. And I never get to say goodbye to Sana. Nor do I get to see Imani and Rika off as it makes more sense for me to just head home from here."
    "I had a good time, though."
    "..."
    "I hope they did too."

    $ renpy.end_replay()
    $ imani_love += 1
    $ rika_love += 2
    $ sana_love += 1
    $ rikaspring2 = True

    "{i}Rika’s affection has increased to [rika_love]!{/i}"
    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label rikaspring3:
    scene nightsky
    with dissolve2
    play music "love.mp3"

    "There’s this tree I walk past some nights when I don’t know what to do with myself."
    "I guess you can probably surmise I’ve visited it a lot with that in mind."
    "For the first few years, it was merely coincidental."
    "Just a thing I’d pass by on my way from one place to the next."
    "But it’s changing now — and so am I."
    "It’s started to blossom. "
    "This {i}is{/i} spring, after all. It was only a matter of time until that scent and those colors found their way back to me."
    "Just like she did."
    "I keep thinking I’ll see her beneath it — standing there with her palm outstretched, hoping the wind sodomizes the branches and delivers a petal or two to her fingers."
    "There’s nothing ever there, though. Because she only visits me when I don’t want her to."
    "Sometimes I’m just lonely, though."
    "Sometimes, I just miss her."
    "..."
    "That’s okay, right?"

    play sound "vibrate.mp3"

    "My phone goes off in my pocket."
    "It’s like a portable, hand-held god."

    play sound "phonebeep.wav"

    s "Hello?"
    ri "{i}Hey, Akira. Any chance you could meet up tonight? There’s something I want to talk to you about.{/i}"
    s "Am I allowed to know what it is beforehand? Or is this one of those things where I get blindsided by drama and thrown into a lake of sorrow where I must either sink or swim?"
    ri "{i}Lake of Sorrow is an album by Sins of Thy Beloved.{/i}"
    s "Cool. That doesn’t answer my question, though."
    ri "{i}It’s about Rin. Just come over and I’ll tell you more, okay?{/i}"
    s "Rin? Did something happen to her? Is everything-"
    ri "{i}Just come over...and I will tell you more. Okay?{/i}"
    s "Oh...yeah. I’ll head over now."
    ri "{i}Bring cheese, if you can. It’s important.{/i}"
    s "You don’t...still have that rat. Do-"
    ri "{i}Bye, Akira! See you soon!{/i}"

    play sound "phonebeep.wav"

    "Rika hangs up the phone and I have no intention to deliver cheese to her house."

    scene black
    with dissolve2

    "Not because I’m evil, though. My evilness has no relation to the amount of cheese I am capable of transporting."
    "I’m just a little worried, that’s all."
    "But I guess there’s a baseline of permanent worry when it comes to Rin since I’ve seen firsthand what she’s done to herself in the past."
    "So...I hope this has nothing to do with that."
    "And I hope that, whatever it is, both she and Rika will be okay."
    "........."
    "......"
    "..."
    play sound "doorbell.mp3"

    "I ring the bell once I get to Rika’s place. The lights above the doors that belong to Yuki and Imani are both out, so I guess she’s the only one around tonight."

    ri "{i}Come in! It’s open!{/i}"

    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene rikarattalk1
    with dissolve2

    ri "Hey! Thanks for coming to me. People don’t really like it when I bring Frankenstein out in public."
    s "So you really kept it, huh?"

    scene rikarattalk2
    with dissolve

    ri "Of course! Just look at him. Who could ever turn away an adorable face like this? "
    ri "Besides, if that thing Imani said about rats only living for three years is true, I want to make sure the last...however many years he has left are as good as they can be."
    s "Well, I’m glad you and your son are happy together. And I’m also glad to see you actually have some furniture now."

    scene rikarattalk3
    with dissolve

    ri "It’s a work in progress. But all I really {i}need{/i} is a futon and a table to eat stuff at. "
    s "I see you kept the chalk outlines too. "
    ri "They make good decorations. And I figured that if I ever have a heart attack or die of old age or something, I could just lie down on top of them and make life easier for whoever finds my body."
    s "I think they only do the outlining thing for homicide investigations."
    ri "I guess I just have to hope my potential murderer is as kind as me then, huh?"
    s "Guess so, Rika."

    scene rikarattalk4
    with dissolve

    ri "..."
    s "..."
    s "So...that thing you wanted to talk about."
    ri "Mhm?"
    s "Mind filling me in now? Or were you only luring me over with your daughter’s name because you thought it would get me here quicker?"
    ri "Why would I think that, Akira?"
    s "Because I’ve known her longer and care about her more than you."

    scene rikarattalk5
    with dissolve

    ri "Wow. Harsh. "
    s "I’m sure you’ll work your way up the rankings. But, as it stands, I’ve just been through way more with her."

    scene rikarattalk6
    with dissolve

    ri "It’s fine, I get it. I obviously also care about her more than you too. "
    ri "Rin is, to put it plainly...the greatest thing that’s ever happened to me. More than Rie. More than Frankenstein. Even more than that time I made out with Robert Plant when he played in Fukuoka in ‘96."
    s "Well, I am very glad you like your daughter more than some rockstar’s tongue."

    scene rikarattalk4
    with dissolve

    ri "And I’m glad to hear you do too. Though, your opinion is obviously skewed since you’ve never made out with a rockstar."
    s "I’ve boned an idol, though. That has to count for something."
    ri "It does. That Niki girl’s super cute. But the point is, we both care about Rin and we both want what’s best for her. Right?"
    s "Right."
    ri "Good. Then let’s make a deal to be as blunt as possible from this point on so there are no misunderstandings at all about what we’re dealing with. Okay?"
    s "Uhh...okay. I still don’t really get what’s happening, though."
    ri "Do you remember the night when I took your phone?"
    s "Of course I remember. I could hardly walk the next day after learning what it meant to do it “Ghana style.”"
    s "Which isn’t even mentioning how hard it was for me to calm Ami down when I got home. I had to explain like ten times that I couldn’t answer her calls because of you."


    scene rikarattalk7
    with dissolve

    ri "And I’m sorry for that, okay? I went into rabid mom mode and wasn’t thinking clearly."
    s "You told me you were using it as a flashlight to find a key you dropped in the sewer outside."

    scene rikarattalk8
    with dissolve

    ri "Which was {i}not{/i} a lie, actually. I {i}did{/i} do that when I got back. But only for a couple minutes before I realized I could just use my own phone for that and yours was dying from Ami calling it so many times."
    ri "The {i}full{/i} truth, though..."

    scene rikarattalk9
    with dissolve

    ri "Is that..."
    ri "Rin texted you."
    ri "Many times, actually. Which is the only reason I picked your phone up in the first place since it wouldn’t stop going off and was really annoying me."
    s "Did she? I don’t remember seeing anything. "
    ri "That’s because I deleted everything."
    s "You...went through my messages?"
    ri "Not all of them. I {i}do{/i} respect your privacy despite the whole...thievery thing. It was only the stuff Rin sent that night that I got rid of. That’s all I saw."
    s "Rika, I get why you’d be worried about that, and...you know, I guess it {i}is{/i} technically inappropriate for me to have her number. But it’s not like I’m using it for {i}nefarious purposes{/i} or anything."
    s "You already know I hang out at the dorms sometimes. And-"
    ri "Akira, she..."

    scene rikarattalk10
    with dissolve2

    ri "The stuff she sent to you that night was so graphic that I don’t even want to repeat it."

    scene rikarattalk11
    with fade

    s "..."
    s "What?"
    ri "Be honest with me. As a parent, not a friend. Or...maybe as a friend if you find it easier to talk that way? Has Rin ever-"
    s "Graphic how, Rika? What does that mean?"
    ri "{i}Hah.{/i} Fine. I told you we should be blunt, so I’m going to be blunt. We can be mature about this."
    ri "She sent you basically an entire essay about wanting to have sex with you, complete with a five minute video of her...you know."

    scene rikarattalk12
    with dissolve2

    s "{i}Rin{/i} did? You’re sure it was her?"
    ri "Yeah. I think I know my daughter when I see her."
    s "{i}Why?{/i}"
    ri "You’ve really...never gotten anything like that from her before?"
    s "No...never."

    if nikinudetrade == True:
        "Not directly, at least. "

    scene rikarattalk13
    with fade

    ri "I see..."
    ri "I guess she wasn’t lying about literally {i}everything{/i} then."
    s "So you just...believe me then? That’s it?"
    ri "You don’t get expressive often. So when you do, it’s easy to tell exactly how you’re feeling. And I know confusion when I see it. I own a mirror."
    s "What...happened after that?"

    scene rikarattalk14
    with dissolve

    ri "{i}Well,{/i} after she invited you over to pound her with the intensity of a western silverback, which is a type of gorilla, I sent her a text from your phone saying I was on the way."
    ri "Once I got there, she opened the door and...it was like a flip switched inside of me."

    scene rikarattalk15
    with dissolve

    ri "I don’t get serious often. It hurts my head. But this girl, a girl I have nurtured and supported and {i}admired{/i} for so many years...turned me into, like...a discipline robot with the snap of her fingers."
    ri "I took her phone...tried to warn her about what she was doing and how much trouble she could get {i}you{/i} in by sending that stuff, but I don’t even know if I got through in the end."

    scene rikarattalk16
    with dissolve

    ri "It’s scary, you know? Like, I’m not going to think less of her for having a crush on her teacher. We’ve all done that. But never in a million years did I think she’d go out of her way to, like...try and rope you into it."
    ri "Like, where the hell did she get {i}that{/i} from? "
    s "I..."
    s "I have no idea..."

    scene rikarattalk17
    with dissolve

    ri "Anyway, please don’t bring this up to her. I’ve embarrassed her enough and she’d straight up kill me if she found out I told you about this. I just need to know for sure that nothing’s going on."

    scene rikarattalk18
    with fade

    s "Yeah...of course..."
    s "I’ve never even touched her."

    if rinkiss == True:
        "A lie, of course. But one worth telling as the single kiss I shared with her amounted to little more than false hope and a few bundles of tissues."
        "Rika can’t know I’ll never forget it, though. Not when she’s already suspicious."
        "That was so long ago, now. "
        "I doubt it even crosses her mind."

    ri "Did you even know she felt this way about you?"
    s "I thought she felt the exact {i}opposite{/i} way about me. She’s been obsessed with girls the entire time I’ve known her."
    ri "Well, I guess it’s {i}your{/i} turn then. Because I doubt this is going to just go away overnight. Rin has so much love to give, that’s why it always, like...overflows whenever she finds somebody."

    scene rikarattalk19
    with dissolve

    ri "At the very least, she knows it’s wrong. {i}You{/i} know it’s wrong. That’s not going to stop the way she feels, though. She needs...I don’t know. She needs {i}something.{/i}"
    ri "Like, I don’t want to tell you go break the girl’s heart or anything because I don’t want her, like...romantically traumatized or stunted by a grown man telling her to back off. She doesn’t even know you {i}know{/i} yet."

    scene rikarattalk20
    with fade

    ri "So my only idea is, like...wait for it to blow over? But that sounds too passive and her other mom agrees. Just neither of us knows what the best course of action is right now, so..."
    ri "At least you’re in the know now. So if she ever comes at you again, just...let her down gently, okay? That’s my baby girl. She’s just...being a little dumb right now."
    ri "She gets it from me, I guess."
    s "You’re a great mom, Rika. Don’t let yourself think otherwise."
    ri "You should see Rie. She’s like a...mom magician. A momgician. A...mom..."

    scene rikarattalk21
    with dissolve

    ri "Aaah! Now I want to cry again!"
    s "You still really miss her, don’t you?"

    scene rikarattalk22
    with dissolve

    ri "Yeah, but..."
    ri "More than that, I think I just miss being loved all together."
    ri "Wakana has Osako. Imani has you. Who does that leave {i}me{/i} with? A rat? Who’s going to love me this late in life, Akira? Nobody. "
    s "Question — have you tried witchcraft?"
    ri "Of course I’ve tried witchcraft. They’d have revoked my lesbian license by now if I hadn’t. Still nothing, though. "
    s "You’ll find someone, I’m sure. "
    ri "How do you know that, though?"
    s "Because you’re extremely fucking hot, Rika. Like, disturbingly so."

    scene rikarattalk23
    with dissolve

    ri "Aww, thank you! Now I’m in a good mood again."

    scene rikarattalk24
    with dissolve

    ri "Mmm but now I’m sad again because I’m remembering my daughter wants to fuck old people."
    s "Could be worse. My daughter specifically only wants to have sex with me."

    scene rikarattalk25
    with dissolve

    ri "Rin wanted to marry Rie when she was younger. Maybe it’s just a daughter thing?"
    s "Did you ever want to have sex with either of your parents?"
    ri "No. But my uncle grabbed my boob once. He said it was an accident, but I never believed him. He’s dead now though, so my boobs are finally safe."

    scene rikarattalk26
    with fade

    s "I’m happy for you, Rika. I’m happy for your boobs too."
    ri "Awww! Are you actually {i}smiling?!{/i} "
    s "Trying to. I’m still learning."
    ri "Hahah..."
    ri "We never really stop learning, do we?"
    ri "Even now, at 42 years old, I’m learning things about my daughter. About how to deal with new...{i}weird{/i} problems I never expected. And I’ve already dealt with so much for her, you know?"
    ri "Depression’s no joke, dude. It took us so long to find a therapist that she actually clicked with. It was like one of those...what do you call it, again? Oh! Noodle in a haystack."
    s "Needle."
    ri "Needle? No. A noodle would be harder to find. It won’t poke you. "

    scene rikarattalk27
    with dissolve

    s "You’re...not wrong?"
    ri "Oh no! I killed the smile. Bring it back!"
    s "I can only manage it for a few seconds at a time. Don’t take it personally. "
    ri "Oh, I won’t. Not taking things personally is my specialty when I am the legal guardian of a hormonal gremlin who keeps adding a year to my age. The joys of parenting, am I right?"
    s "I’m still new to that too. I wouldn’t really know."
    ri "Yeah..."
    ri "You’re doing a great job though, Akira."
    s "How would you even know? You’ve never seen me in action."
    ri "Ami called you like five hundred times the night I had your phone. I’m lucky if Rin calls me once per week."
    s "Ami’s different."
    ri "Ami loves you. "

    play sound "static.mp3"
    scene rikarattalk28 with flash
    stop sound

    ri "For good reason, too. Deep beneath all that anguish and torment in that lake of sorrow you call your heart, there’s a caring, gentle little boy who just wants the people he loves to be happy."
    s "Lake of Sorrow is an album by Sins of Thy Beloved."
    ri "You remember."
    s "I remember all sorts of things. But I forget even more."
    ri "Those sound like lyrics. Are you trying to start a band right now? "
    s "I’m not sure either one of us has the time between dealing with our respective daughters and how horny they are for me."
    ri "I’m horny for you too, Akira."
    s "..."
    ri "..."
    s "I’m sorry, what?"
    ri "What?"
    s "Did you just-"
    ri "Yeah."
    s "And was that-"
    ri "Yeah."
    s "..."
    ri "..."
    s "Uhhhhh..."
    ri "I’ve won over like twenty girls with that move. Blatant admission and direct eye contact. "
    s "Yeah, you haven’t blinked once."
    ri "That’s how you know I’m serious."
    s "{i}Are{/i} you serious? "
    ri "If I said yes, what would you do? "
    s "Fuck you."

    scene rikarattalk29
    with dissolve

    ri "Bzzzt! You’re torn between my best friend and a famous pop star. Both of which are much smarter and cuter than me. Do not be tricked by my vast experience and feminine wiles."

    scene rikarattalk30
    with dissolve

    ri "Also, do you have any idea how much it would fuck Rin up if she found out her mom had sex with the boy she likes? "
    s "She actually told me to have sex with you once."

    scene rikarattalk31
    with dissolve

    ri "What? Why?"
    s "To fix you, I think?"

    scene rikarattalk32
    with dissolve

    ri "Good reason. It would definitely help."
    s "..."
    ri "..."
    s "You’re doing the eye thing again."
    ri "Oh, you don’t need to tell me. I’m well aware of what I’m doing."

    play sound "bustdoor.mp3"
    scene rikarattalk33
    with hpunch

    ri "I-Imani! It’s not what it looks like! We were just-"

    $ renpy.end_replay()
    $ rikaspring3 = True
    $ rika_love += 1
    stop music

    jump rikaspring4

label rikaspring4:
    play sound "static.mp3"
    scene yukibustsin1 with flash
    stop sound
    play music "hometown.mp3"

    ri "Wait, Yuki? What are you doing here?"
    yu "What am {i}I{/i} doing here?..."
    yu "What...are {i}you{/i} doing here?..."

    scene yukibustsin2
    with dissolve

    yu "And what the fuck happened...to all of my shit?"
    ri "I...live here. With my rat son. And this is his rat father, Akira. "
    s "Oh good. Another animal to co-parent. Just what I wanted."

    scene yukibustsin3
    with dissolve

    yu "Hey...I know that guy..."
    s "I know you too, Yuki. Would you like to explain what’s going on right now?"
    yu "Nnnnnnnnnnnope."

    play sound "thump.mp3"
    scene yukibustsin4
    with hpunch

    ri "Yup. Saw that coming."

    play sound "static.mp3"
    scene yukibustsin5 with flash
    stop sound

    yu "Mnh...the fuck happened to my rug?..."
    s "She hasn’t done this before, has she?"
    ri "Never. "
    yu "Get the...fuck outta my...apartment......I’m trying to.....go...mnh......sleep...."
    ri "Yuki, do I need to call an ambulance?"
    yu "You ain’t...gotta call shit..."
    ri "What did you take?"
    yu "Fuckin...nothing...okay? Now...fuck off..."
    ri "Akira?"
    s "Don’t look at me. I’ve been here the whole time. "
    ri "Yeah, but you know her way better than I do. "

    play sound "static.mp3"
    scene yukibustsin6 with flash
    stop sound

    ri "I just need to know if this is going to be a “hold her shoulders while she vomits into the toilet” night or an “I should have bought that NARCAN” night."

    scene yukibustsin7
    with dissolve

    ri "Probably the former if she’s still somewhat coherent right now. But you never know how this stuff will progress and-"
    yu "Just...let me fuckin’ die, okay?! Mnh! Mblmm...mmnh..."
    ri "If you’re going to die, can you please crawl into one of the pre-drawn outlines? I was just talking about this a few minutes ago."
    s "I wish I had something more to say than I did the last time I saw you like this."

    scene yukibustsin8
    with dissolve

    yu "What’d.....last time......say?....."
    yu "I can’t....mn.....g....night....."
    s "Unbelievable."
    ri "..."
    s "..."

    scene yukibustsin9
    with dissolve

    ri "Why don’t you go home, Akira?"

    scene yukibustsin10
    with dissolve

    s "And let you deal with this on your own?"
    ri "What, you think I’ve never had to nurse a junkie back to health before? Come on."
    ri "I’ll get her into bed and watch her for a few hours to make sure she’s okay. It’s clear you don’t want to see her like this, so just leave it to me."
    s "At least let me help you carry her back to her apartment."
    ri "No need. I’ll just keep her here. I bought a second futon in case Rin ever wanted to stay over. I’ll just sleep in that."
    ri "If Yuki wakes up in the middle of the night and wants to go back, she can. You really don’t have to worry about it."
    s "But-"

    scene yukibustsin11
    with dissolve

    ri "I’ve got this. Okay? You’ve already fulfilled your manly duties for the day by listening to what an old woman had to say about her daughter’s safety and how it relates to your penis."

    scene yukibustsin12
    with dissolve

    s "..."
    ri "Okay?"
    s "I just don’t get it..."
    s "She was doing so well."
    ri "It’s impossible to get it unless you’ve been there. "
    ri "We’re all addicted to something, Akira. I’m sure you’ve got your vice as well."
    s "..."
    s "Yeah."
    s "Are you really sure you’ll be okay?"

    scene yukibustsin13
    with dissolve

    ri "Hey, Yuki! Want to have a sleepover? Stay silent for yes!"
    yu ".................."

    scene yukibustsin14
    with dissolve

    ri "See? She’s totally excited."
    s "Or dead."
    ri "We’ll be fine either way. I know people. How do you think Rin gets her skulls?"
    s "Call me if anything goes wrong or gets worse. "

    scene yukibustsin15
    with dissolve2

    ri "Of course. "
    ri "She probably just needs to sleep it off. I’ll talk to her in the morning."

    scene black
    with dissolve2

    ri "And I won’t take no for an answer this time."

    play sound "dooropen.mp3"
    "........."
    "......"
    "..."

    scene yukibustsin16
    with dissolve2

    ri "Ooookay! Come on, junkie. Let’s get you into bed."
    yu "Get your......hands......off’a me.......I’m.........fine......"
    ri "Oh, you are? So I guess you just barged into my apartment because you changed your mind about hooking up with me then?"
    yu "I.................."
    ri "You?"
    yu "................."
    yu "What?........"
    ri "Mhm. That’s what I thought."

    stop music fadeout 10.0
    scene black
    with dissolve2

    ri "I’m gonna take your shoes off. Continue to be high if you consent!"
    yu "Mm......."
    ri "Got it. Jacket stays on. Just gonna check your arms first. "
    yu "Don’t......you.....fucking....."

    play sound "tackle.mp3"
    ri "There! All done. I’d check your thighs too, but I don’t think we’re at that level yet and I’m sure you’ll be okay."
    ri "Here. Water."
    yu "Mm..."
    yu "I..."
    ri "Shh..."
    ri "Sleep now, okay? "
    ri "I’ll keep an eye on you for as long as I can..."

    "........."
    "........"
    "......."
    "......"
    "....."
    "...."
    "..."
    ".."
    "."

    if day == 1:
        $ totaldays += 1
        $ day += 1
        if day == 2:
            hide monday onlayer date
            show tuesday onlayer date
    elif day == 2:
        $ totaldays += 1
        $ day += 1
        if day == 3:
            hide tuesday onlayer date
            show wednesday onlayer date
    elif day == 3:
        $ totaldays += 1
        $ day += 1
        if day == 4:
            hide wednesday onlayer date
            show thursday onlayer date
    elif day == 4:
        $ totaldays += 1
        $ day += 1
        if day == 5:
            hide thursday onlayer date
            show friday onlayer date
    elif day == 5:
        $ totaldays += 1
        $ day += 1
        if day == 6:
            hide friday onlayer date
            show saturday onlayer date
    elif day == 6:
        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date
    elif day == 7:
        $ totaldays += 1
        $ day -= 6
        if day == 1:
            hide sunday onlayer date
            show monday onlayer date

    scene yukibustsin17
    with dissolve3

    "Four hours, thirteen minutes, and eleven seconds."
    "That was how long Rika Rokuhara watched an addict that night."
    "It wasn’t her first time. Nor was it her second, third, fourth, or fifth."
    "Come to think of it, she didn’t know {i}how{/i} many times she’d done something like this now."
    "It was sort of nostalgic in a way. But much worse than nostalgia normally is because there were no pleasant memories that clung to it in an effort to offset the bad ones."

    scene yukibustsin18
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "When morning came, Yuki Yamaguchi awoke to an unfamiliar scent."
    "Strangely enough, however, this sort of unfamiliarity was familiar to her."
    "She’d also lost count of something — how many times she’s betrayed herself."
    "How many relapses, rebounds, and {i}restarts{/i} she’d made over the course of a life that had tacked at least two or three decades onto her age."
    "It was catching up to her now, just not in the ways she expected."
    "And that was particularly strange to her, because she always expected the worst."
    "Who knew the worst would look like this?"

    yu "...huh?"

    scene yukibustsin19
    with dissolve2

    yu "Where the...fuck?"

    scene yukibustsin20
    with dissolve2

    yu "..."

    "She noticed something."
    "This something was strange too."

    play sound "static.mp3"
    scene yukibustsin21 with flash
    stop sound

    "Someone had spent the night by her side. And this time, they didn’t have their way with her in the midst of her unconsciousness. Or at least she didn’t {i}think{/i} she did."
    "Why was she here, though?"

    ri "..."
    yu "..."

    "Zero hours, five minutes, and forty-three seconds."
    "That was how long Yuki Yamaguchi watched someone she didn’t know what to say to."

    ri "I can feel you staring at me."

    scene yukibustsin22
    with dissolve2

    ri "Aren’t you going to say good morning?"
    yu "What am I doing here?"
    ri "More important question — how do you feel? You were zonked out of your mind when you busted in last night."

    scene yukibustsin23
    with dissolve

    yu "{i}Hah...{/i}fuck."
    yu "Sorry to get you involved. I’ll fuck off back to my place now."
    ri "No, stay."
    ri "Let’s talk."

    scene yukibustsin24
    with dissolve

    yu "I...appreciate the...gesture and shit...I ain’t really the talkin’ type, though."
    ri "Hmm..."
    ri "What time is it right now?"
    yu "Think the alarm clock over there says...5:25, but I can’t really tell since there’s a...is that a fuckin’ rat in the way?"
    ri "That’s Frankenstein. He’s a good boy."

    scene yukibustsin25
    with dissolve

    yu "Cool name...I guess..."
    ri "Yuki...Do you have any plans today, by any chance?"
    yu "Just...being a sack of shit. Same as always."
    ri "Let’s go somewhere."
    yu "What, like...together? I know you let me crash here last night, but I ain’t really got the cash right now if you want me to, like...buy you breakfast or-"
    ri "I’ll buy {i}you{/i} breakfast."
    ri "There’s somewhere else I want to go first, though."

    play sound "static.mp3"
    scene yukibustsin26 with flash
    stop sound

    yu "The gym?..."
    ri "Not a fan of working out? Need help learning how to use the machines?"
    yu "No, I...used to come here. Stopped, though."
    ri "Free trial run out?"
    yu "Something like that, yeah."

    scene yukibustsin27
    with dissolve

    ri "Well, I just so happen to come here every day. And I’m allowed to bring a guest, so...if you’re ever looking for something to do that {i}doesn’t{/i} involve getting high, feel free to tag along."
    yu "Man. You must {i}really{/i} want to fuck me if you’re going to be my nurse {i}and{/i} my personal trainer."

    scene yukibustsin28
    with dissolve

    ri "You forgot about breakfast. My addict-coddling spree has only just begun."

    scene yukibustsin29
    with dissolve

    yu "..."
    ri "What are you doing, Yuki?"
    yu "Just...being a sack of shit. Same as always."
    ri "How old are you? Thirties, right?"
    yu "Thirty-eight..."
    ri "Thirty-eight years old, and still running around like you’re invincible. Come on. We’ve gotta be more conscious about our bodies at this age. You know that, don’t you?"
    yu "You ain’t got the faintest fuckin’ idea."
    ri "Then talk to me. Why are you doing this to yourself? To your daughter? Do you have any idea how she’d feel if she found out?"
    yu "Yumi? Like she’d give a shit about that. No one knows better than her that I ain’t nothin’ but a lost cause."

    play sound "static.mp3"
    scene yukibustsin30 with flash
    stop sound

    ri "There’s no such thing as a lost cause. Even the worst people in the world have a chance to make things right if they try."
    yu "The fuck is {i}right,{/i} though? The hell does that even mean? I ain’t hurtin’ anybody. Least not anymore. That ship’s already sailed. Then crashed into the goddamn dock and exploded into a million pieces."
    ri "So find another ship."

    play sound "static.mp3"
    scene yukibustsin31 with flash
    stop sound

    yu "I {i}did.{/i}"
    yu "I finally fucking did this time. And, you know...I really thought this was the one."
    yu "I really thought I could just fuckin’...live my life after all these years. That all the horrible shit was behind me and I could become someone {i}worthy.{/i}"
    yu "Of Yumi...Sara...{i}everybody{/i} who keeps givin’ me a chance when I ain’t done shit to earn one. But of course that was all a fuckin’ dream. Of {i}course{/i} it wouldn’t actually work like that."
    ri "What happened then?"
    yu "The fuck do you think happened, Rika? Gimme your best fuckin’ guess, because you ain’t gonna get it."

    play sound "static.mp3"
    scene yukibustsin32 with flash
    stop sound

    ri "That’s why I’m asking. I know better than to ever expect an actual {i}answer{/i} out of people like you. If you had one, things like this would never happen in the first place."
    yu "Why even fucking ask then?"
    ri "Because it gets you talking. And talking makes you think. Talking makes you {i}sad.{/i} Sadness is a spark."
    yu "So what, you’re trying to fuckin’ set me on fire now? Think I’m gonna pull myself together out of pure sorrow? What’s the plan?"
    ri "To make you fucking miserable. That’s the plan."
    yu "Well, you ain’t gotta work hard at all then. Mission complete."
    ri "Oh, shut up. It’s not like I actually {i}want{/i} you to be miserable. I just know that you need to hit rock bottom before you can find the strength to climb back up."
    yu "I’m outta fuckin’ strength, Rika. I can’t do this shit anymore."
    ri "Can I give you a little anecdote?"
    yu "Please. Anything to keep me from talkin’ about my fucking self."
    ri "My daughter is adopted. My ex-partner and I both have vaginas, so we weren’t able to make a baby on our own."
    yu "Great story. Have you sold the movie rights yet?"
    ri "Shush. I’m not done."

    scene yukibustsin33
    with dissolve

    ri "Her biological mom had her when she was just a kid. Probably close to the same age my daughter is right now."
    ri "She was fucked up beyond belief. Not from drugs, I don’t think. Just, like...trauma in general? Weird brain stuff? But she could barely even speak apparently."
    ri "She was the definition of “rock bottom.” But even then...even though she was a fucking psycho, {i}she{/i} managed to find the strength to do what was best for a baby and give her up to someone else."

    scene yukibustsin34
    with dissolve

    ri "And if a deranged, psychotic, borderline-mute lady can find it in herself to put others first, I think a conscious, drug addict Yakuza lady can definitely do the same."
    yu "So...is the moral there...what? How does that relate to me exactly?"
    ri "You know. Rock bottom. Good decisions. Do things for your daughter, not yourself."
    ri "I guess it probably would have made more sense to talk about my dad being an addict too, huh?"

    play sound "static.mp3"
    scene yukibustsin35 with flash
    stop sound

    yu "That probably would have been better, yeah..."
    ri "Point is, {i}tons{/i} of other people out there have crawled out from the bottom of the barrel and turned their lives around. {i}You{/i} could be the next one. You’ve just gotta wake the fuck up."
    ri "Your daughter’s {i}still{/i} your daughter, Yuki. She visits you. I’ve seen her outside. I’ve {i}heard{/i} you guys watching wrestling through the walls. And I was only a little sad I wasn’t invited."
    yu "Didn’t...realize you were into that sorta thing."
    ri "Don’t do this to {i}her.{/i} Or that {i}Sara{/i} person I am now jealous of. Or any of the other people like Akira who love you."
    yu "You still ain’t gettin’ it, Rika. I’ve heard this all before...and it ain’t changed shit."

    scene yukibustsin36
    with dissolve

    ri "Have you ever heard from your cool onee-san, though? That changes everything, doesn’t it?"
    yu "Heh...no. I guess I haven’t."
    yu "It doesn’t change anything, though."

    scene yukibustsin37
    with dissolve2

    yu "It’s too late, Rika."
    yu "I can’t keep crawlin’ up from rock bottom."
    yu "Maybe...if I were more like you."
    yu "Maybe if I was actually {i}there{/i} for my daughter when she was little, I might’ve changed sooner. Gone to the gym more. Stayed away from shit everybody {i}knows{/i} is bad for you...but {i}feels{/i} so fucking good."
    yu "{i}Now,{/i} though?..."
    yu "The hell am I supposed to do when I’m {i}not{/i} with Yumi, huh? When I’m {i}not{/i} working? Just sit around and fucking...be alone with myself? You have any idea what I {i}think{/i} of when I’m alone, Rika?"
    yu "Do you have any idea how bad the temptation is to just fucking...ruin everything {i}again{/i} so that something’s {i}happening?{/i} So that I’m not just reaping the benefits of a life I haven’t {i}earned?{/i}"
    yu "Combine those truths with the fact that the world just straight up doesn’t want people like me here and you get..."
    yu "Well..."
    yu "You get a fuckin’ death sentence."
    ri "I want you here, Yuki."
    yu "You barely know me."
    ri "I barely knew my daughter at first too. Or my ex. Or all of my friends. But every one of them is extremely important to me now. And there’s no reason you can’t be too."
    yu "..."
    ri "..."
    yu "Sorry, I..."
    yu "I just don’t...swing that way."

    scene yukibustsin38
    with dissolve

    ri "This isn’t about that! I’m not going to hit on you just a couple hours after you woke up from a drug-addled episode of breaking and entering! I want to be your friend!"
    yu "{i}Why,{/i} though?...I don’t get it."
    ri "Because I-"

    scene yukibustsin39
    with dissolve2

    ri "I..."
    yu "..."

    scene yukibustsin40
    with dissolve

    ri "Because I’m selfish."
    yu "...huh?"
    ri "You...wouldn’t get it."
    yu "..."
    ri "..."

    scene yukibustsin41
    with dissolve

    ri "Right! Anyway! Let’s work out!"

    scene black
    with dissolve2
    stop music fadeout 12.0

    yu "Yeah. We stand around any longer, more people might start showin’ up and I won’t be able to talk about half of this shit anymore."
    ri "We could always continue back at my place! Platonically, of course. {i}Unless...{/i}"
    yu "Ugh...why do I feel like you’re about to become a huge pain in my ass all of a sudden?"
    ri "Probably because I am. I’ve never had a little sister before."
    yu "And you don’t have one now. ‘Specially since I still see you as like, a...twenty-something."
    ri "It’s all that time on the elliptical! Oh, here. I’ll show you how to use it. Just come over here and- Yuki?"
    yu "Sorry. I’m a punching bag only sorta girl. And I’ve got a lot of anger I need to get out right now."

    $ renpy.end_replay()
    $ rikaspring4 = True

    "{i}Rika and Yuki have formed a bond!{/i}"
    "{i}Yay?{/i}"
    "........."
    "......"
    "..."

    scene noonsky
    with dissolve2

    "It’s noon again."

    jump noonch4
