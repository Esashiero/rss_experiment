label otohapark:
    if otoha_love >= 0 and otohadorm1 == True and saradate10 == True and otohapark1 == False:
        jump otohapark1
    if otoha_love >= 0 and otohapark1 == True and otohapark5 == False:
        jump otohapark5
    if otoha_love >= 10 and christmastwo20 == True and otohapark10 == False:
        jump otohapark10
    if chap4active == True:
        jump otohaspringparkgen
    if chapthreeactive == True:
        jump otohasummer2streetsgen
    else:
        jump otohaparkgen

label callotohamorning:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I tap on Otoha's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callmorning

label callotohaafternoon:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Otoha's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callafternoon

label callotohanight:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callnight
    else:
        play sound "phonebeep.wav"

        "I tap on Otoha's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callnight

label otohaparkgen:
    scene otohaparkgen
    with dissolve
    play music "brighterdays.mp3"

    "I head to the park first thing in the morning to find Otoha relaxing on a bench and waiting for things to warm up a bit."
    "She invites me to sit next to her and kill time while the rest of Kumon-mi gets out of bed and starts heading wherever it is that all of them need to head over the weekend."
    "Despite not having the {i}best{/i} foot traffic in the area, this park is still located in a relatively convenient place between the[school] and several popular locations."
    "So people {i}do{/i} show up."
    "They show up, watch for several seconds as she starts playing, and then head on their way without so much as even making eye contact with either one of us."
    "Feeling that I may be...detracting from her only source of income, I decide that it's probably best if I just let Otoha do this on her own."

    scene black
    with dissolve

    "She doesn't put up much of a fight because...well, why {i}would{/i} she want me sitting around while she tries to make money?"
    "I reach into my pocket, ready to grab a tip to toss into her guitar case."
    "Her eyes light up...but then immediately go dark as soon as my hand exits my pocket with absolutely nothing in it."
    "I should probably start bringing cash with me if I'm going to keep visiting her while she's performing..."

    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha's affection has increased to [otoha_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label otohapark1:
    scene sky
    with dissolve
    play music "brighterdays.mp3" fadein 5.0

    "I step outside to find that the weather isn’t all that dreadful this morning."
    "I’m sure that will change as the day goes by because nothing good can ever persist for an entire 24 hours-"
    "But right now, things are looking up."
    "Including myself, of course, as the sun stings my eyes for staring at it longer than it wants me to."
    "Which is any amount of time."
    "But fuck it, if the sun wants to come out and say “What’s up? Here’s a little warmth,” in the middle of winter, the courteous thing for me to do is at least acknowledge him."
    "Or her."
    "Or they."
    "The sun can be whatever gender it wants to be and I won’t judge it for its decision."
    "I’m a good guy."

    scene otohapark1
    with dissolve

    "Oh right."
    "Otoha said something about coming to the park in the mornings. "
    "I guess it’s possible that I came here with that in mind, but..."
    "Well, I feel like I somehow would have wound up here regardless of whether or not she’d told me that."
    "It’s just that kind of day."

    s "Otoha? More like Yo-toha."
    s "What’s up?"

    scene otohapark2
    with dissolve

    o "..."
    s "Good morning."
    o "..."
    o "Did you really just greet me with “Yo-toha?”"
    s "No. That never happened."

    scene otohapark3
    with dissolve

    o "Yeah, I didn’t think so either. That would have been super lame."
    s "Almost as lame as hanging out in the park by yourself when there are tons of other girls who’d gladly come with you."

    scene otohapark4
    with dissolve

    o "Well, let’s see..."
    o "Nodoka hates mornings, Noriko hates mornings, and Rin works mornings."
    o "That’s pretty much everybody I’m close with so that leaves...me, myself and I. "
    o "It’s cool, though. I like having alone time and coming here by myself is a good way to relax. "
    o "Especially since it’s actually pretty nice out today."
    s "For now. I’m sure it’ll start snowing in like two hours or something."
    s "Kumon-mi’s weather patterns seem to fluctuate very dramatically from day to day."

    scene otohapark2
    with dissolve

    o "Guess we better make the best of it while we can then, huh?"
    o "Also, the weather really only gets weird during the winter. Every day in the summer is like, just hot and gross and stuff."
    s "Yup. That’s a Japanese summer for you. "
    o "Kinda pumped for the seasons to change again, honestly."
    o "Sure, it might get all humid and whatnot, but it’s a lot easier playing guitar with warm hands than cold ones."
    o "A lot less people come out to watch street performers in the winter too."
    o "Like, just take a look around you. We’re the only two people here and it's not even cold right now."
    s "Then I suppose you’ll just have to serenade me alone."

    scene otohapark5
    with dissolve

    o "Not only would that make me extremely uncomfortable, but I don’t even have my guitar with me."
    o "It wouldn’t be the first time I’ve had to figure out how to deal with just one dude watching me play while everyone passes by but...it’s definitely not something I want to get used to."
    s "Sure, but at least there would be a historically lower probability of him making a move on you than another girl."

    scene otohapark6
    with dissolve

    o "Wait, yeah. That’s a good point."
    o "I guess it's not creepy at all when you put it like that."
    s "No. It's definitely creepy."

    if bonus == True:
        s "Don’t let my bad advice lure you into a false sense of security unless I’m going to personally benefit from it."
    else:
        s "Please ignore anything I ever say to you that doesn't involve flower arranging. That's the only thing I'm really confident about."

    scene otohapark7
    with dissolve

    o "Roger. "
    o "Then, if you ever show up to find me playing by myself, just keep on walking and pretend you never even saw me."
    o "Only after dropping a 1,000 yen note in my guitar case, of course."
    s "How am I supposed to give you money {i}and{/i} pretend I don’t see you at the same time?"
    o "Maybe just accidentally drop it in one very specific location?"
    o "I don’t know man, you do you. A girl’s gotta earn some cash one way or another."
    o "And without a job, I’ve gotta rely on kind souls like you."
    s "Don’t call me a kind soul when I haven’t even tipped you yet."

    scene otohapark8
    with dissolve

    o "I’m just thanking you in advance since I know you’ll take good care of me."
    s "Well if you keep entrapping people like this, I’m sure you’ll be absolutely rolling in money in no time at all."

    scene otohapark2
    with dissolve

    o "Sure hope so."
    o "There would be some days in my old park where I’d be there for like ten hours and not even make 5,000 in total."
    s "Sounds to me like you should have found a different park."
    o "I don’t think it was the park’s fault. And I don’t want to sound cocky, but I don’t think it was mine either."
    o "It’s a lot busier on that side of town than this one. People just don’t really like giving out their money to street performers for whatever reason."
    o "Maybe if I grew up back when my mom did and people actually carried around cash, I would have had an easier time."
    o "She always made it sound so simple."
    s "Your mother was a performer too?"
    o "Once upon a time, yeah. She was in some girl band that toured Japan a few times but never really made it out of the country."
    o "Now she’s just a normal mom with a normal husband and a decently normal daughter."
    s "Didn’t you say something the other day about how she didn’t want you to be a musician, though?"
    o "Yeah, but like, I think it’s one of those things where you regret your own experiences and don’t want someone you care about to do the same thing or whatever."
    o "I don’t know. I don’t really get how old people think."
    o "Do you want to like...sit down, by the way? "
    o "It feels kind of weird carrying on an entire conversation with you just looming over me like some sort of statue."
    s "Oh. Yeah, sure."

    scene otohapark9
    with fade

    "Otoha slides over on the bench to make room for me, wrapping her arms around her legs in what could be interpreted as either a defensive stance or...just a comfortable one, I guess."
    "It’s strange how something as simple as folding your limbs a certain way can mean two completely different things. "

    o "So, speaking of how old people think-"
    s "Don’t do it, Otoha."
    o "Don’t do what?"
    s "Don’t call me old."
    o "Okay, I won’t."
    o "You’re definitely not young, though."
    s "Saying that is just as bad..."
    o "You’re...old by comparison?"
    s "I mean...that’s better. But..."

    scene otohapark10
    with dissolve

    o "I’m just kidding, Sensei. Well...kind of."
    o "You might {i}be{/i} old, but you act kind of like a...cool senpai or something."
    o "Not like the[school] prince or anything, but the broody guy that a really specific clique of girls all pine over."
    s "Right. But that’s only because the[school] prince position was taken over by you once you transferred in."

    scene otohapark11
    with dissolve

    o "That’s only true based on statistics! I’m clearly not princely at all!"
    s "Princess, then?"
    o "That’s just as embarrassing!"
    o "How do I become the dark and broody type like you?"
    s "Easy. Just give up on everything you’ve ever loved and surrender yourself to your impending demise."

    scene otohapark12
    with dissolve

    o "Woah. So lame."
    s "..."

    scene otohapark13
    with dissolve

    o "Pfft...{i}Just give up on everything you’ve ever loved. My name is Sensei and I’m the coolest guy in Kumon-mi.{/i}"
    s "..."
    s "You are making a mockery of my flawlessly flawed personality, Otoha."

    scene otohapark14
    with dissolve

    o "Only cause you’re making it so easy. You’ll never get a girlfriend if you keep acting like that, Sensei."
    s "I already told you I don’t want a girlfriend."
    o "Sure, but you’ll want one eventually."
    o "Like, you won’t just...go the rest of your life without one, right?"
    o "Have you ever even had an actual girlfriend before?"
    s "Yup. Just some idol chick. She’s famous now."
    o "Right, right. You dated a famous idol cause you’re the coolest guy in Kumon-mi."
    o "Which one? Anyone I would be familiar with?"
    s "Very much so."
    o "Oh yeah? Who? Let’s see if I-"
    s "I dated your vocal coach for five years."
    o "..."
    s "..."
    o "Who...do you think my vocal coach is?"
    o "I don’t...remember telling anyone about that."
    s "Niki Nakayama."
    o "..."
    s "She’s actually the one who told me she was coaching you. I’ve known for a little while now."
    o "..."
    s "..."
    o "And you just...decided not to say anything about it?"
    s "It never really came up in conversation."
    o "..."
    o "I don’t believe you."
    o "This is clearly a coordinated prank. Noriko probably heard about it from Niki and then...planned this with you or something."
    s "Call her."
    o "Like...right now?"
    s "Right now."
    o "But...she’s probably busy..."
    s "Call her and say nothing but “Sausage fest.”"
    o "I’m not going to call Niki and say “Sausage fest.” What does that even mean?"
    s "It’s her favorite dish and an inseparable bond the two of us share."
    o "..."
    s "..."
    o "Nah. This is a joke. I’m not falling for it."
    s "Why? Don’t think I’m cool enough?"
    o "Not that. It’s just..."

    if bonus == True:
        o "She’s...an adult."
    else:
        o "She’s...not an accountant."

    s "..."
    o "..."
    s "Okay. That’s fair."

    scene otohapark15
    with dissolve

    o "B-Besides! She’s said all kinds of messed up stuff about her ex before and you don’t really seem like that kind of guy!"
    o "Like yeah you’re...just as weird and stoic as she described, but I highly doubt you’d ever just up and ghost on someone who loves you as much as she loved him!"
    o "Like...don’t mention this to anyone, but she even said some stuff about how she almost killed herself this one time and like..."
    o "There’s no way...that person is..."

    scene otohapark16
    with dissolve

    o "It totally was you...wasn’t it?"
    s "I’m telling you, there are only two words you need to say to her that would answer every question you have right now."
    o "..."
    o "I’m not going to call Niki and say “Sausage fest.”"
    s "..."

    scene otohapark17
    with dissolve
    play sound "phonebeep.wav"

    s "You know, I really wish I didn’t have to keep doing this."
    o "Who...are you calling?"

    "I tap on Niki’s name and set my phone to speaker mode so Otoha can listen to her world shatter into a million pieces."
    "This will show her how cool I am."

    play sound "phonebeep.wav"

    ni "Yeah? What’s up?"

    scene otohapark18
    with dissolve

    s "Sausage fest."
    ni "What, like right now?"
    ni "Uhh...sure. I should have a little time before my lesson. I just have to get dressed."
    s "Actually, forget it. I changed my mind."
    ni "Already?..."
    s "Yup."
    ni "Well you better have a good excuse because I’m already halfway through taking my pajamas-"
    s "I’m actually with Otoha right now."
    ni "...What?"
    o "Hi, Niki..."
    ni "..."
    ni "[nikitemp]..."
    s "Yes?"
    ni "{i}Why{/i} are you with Otoha right now?"

    scene otohapark19
    with dissolve

    o "Your name is [nikitemp]?"
    s "We’re on a date. I was actually just calling you to brag about it."
    ni "Oh, no you are not! Put her on the phone right now!"

    if bonus == True:
        s "Sorry. About to do the sex to each other. Talk to you later."
    else:
        s "CHHHHHHHHH. Going through a tunnel. Talk to you later."

    scene otohapark20
    with dissolve

    ni "HOLD ON ONE SECOND, YOU FUCKING-"

    play sound "phonebeep.wav"

    "I hang up on Niki because I wear the pants in this relationship."
    "I lied about wishing I didn’t have to do this. It’s actually really fun."

    o "Why would you tell her that?!"

    if bonus == True:
        o "Niki and I have a good working relationship and the last thing I want is for her to think I’m sleeping with her ex!"
        o "This is going to be so awkward to have to explain!"
    else:
        o "Niki and I have a good working relationship and the last thing I want is for her to think I'm going through a tunnel!"
        o "You know how she feels about tunnels!"

    s "You brought this on yourself for not believing me."
    o "Don’t pin that on me! No one would ever believe something like that!"
    s "Then each and every one of them shall feel my wrath."
    s "Now, back to our date."
    o "No way! I’m supposed to meet her in less than two hours and now I have to call her and explain myself!"
    s "I see."
    s "Well, it was a nice and productive morning we had together, Otoha. Enjoy your vocal lesson."
    o "I’ll be lucky if I live through it at this rate! You know what she’s like when she gets mad!"
    s "You’re right. The only way out at this point is for us to kill ourselves together."
    o "Sensei! I’m being serious! Don’t mess this up for me!"

    scene otohapark21
    with dissolve

    s "..."
    o "...What?"
    s "I’m just..."
    s "I’m just glad you at least got to experience true freedom for a few days before the end..."

    scene black
    with dissolve2

    "Otoha’s phone goes off before she even has a chance to hop off of the bench. "
    "Without even saying goodbye to me, she answers it and frantically tries to explain that there was no date and that I was simply just trying to prove something."
    "Trying isn’t accurate anymore, though, as I’m clearly drowning in success right now."
    "..."
    "Maybe I should consider putting Niki on speed dial if I’m going to have to keep using her like this?"

    $ renpy.end_replay()
    $ otoha_love += 1
    $ otohapark1 = True
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label otohapark5:
    scene otohacafetrip1
    with fade
    play music "brighterdays.mp3"

    "It doesn’t take long to find Otoha once I make my way over to the park again."
    "In fact, she winds up spotting me first and trots over without me even having to ask."
    "This is good. "
    "If she keeps growing at this rate, she might just wind up walking over to my house in the morning and, eventually, I won’t need to leave at all."

    s "I’ll leave a key for you under the doormat."
    o "Key? What?"
    o "What are you talking about?"
    s "Just the bright future the two of us have together..."
    o "Oh. Uhh, okay. Whatever floats your boat."
    s "No guitar today either?"

    scene otohacafetrip2
    with dissolve

    o "Not really any point until it gets a little warmer."
    o "The other day would have been fine, but it’s back to being chilly again and I don’t want to wind up botching any of my songs when I’m still not known around here."
    s "Just buy hand warmers or something. Problem solved."

    scene otohacafetrip3
    with dissolve

    o "Sure, that’ll solve my finger stiffness...but it’s not like everybody will come flocking to the park as soon as they hear that some random girl bought handwarmers."
    o "There’s more than just one problem, Sensei."
    s "Why not play indoors then?"
    o "What, you mean at that gazebo thing over there? That’s not really going to do much."
    s "I meant something more like an actual business. Like some local venue or a-"

    scene otohacafetrip4
    with dissolve

    sao "Cafe!"
    o "Holy shit! Yeah! That place where Rin works would be great to play at! "
    o "People actually go there in the morning and there’s like...tons of space!"
    s "Also, the manager there really has a thing for [teenage]girls. So you’re basically already locked in."

    scene otohacafetrip5
    with dissolve

    o "You know, maybe we should think of other places just in case. The cafe is cool and all, but-"
    s "Don’t worry. She’s still running a business, so it’s not like she’ll make a move on you mid-set or anything."

    scene otohacafetrip3
    with dissolve

    o "Is that supposed to make me more comfortable?..."
    s "Hey. As a female musician, and a rather attractive one, might I add-"
    o "You really didn’t have to add that."
    s "You should start getting used to being the center of attention. It’s only going to happen more once you start getting popular."
    s "How do you think Niki feels? She’s on actual billboards and she loves the attention."

    if bonus == True:
        o "Sure, yeah. But don’t you feel a little weird being her ex and knowing that there are a bunch of dudes out there who want to get it on with her?"
    else:
        o "Sure, yeah. But don’t you feel a little weird being her ex and knowing that there are a bunch of dudes out there who want to hug her?"

    s "Not really. Because I know I’m the only one who has."
    s "Probably."

    if bonus == True:
        o "If you’re worried about her hooking up with anybody else, I know for a fact that she hasn’t."
        o "She’s really only ever talked about one guy and...that guy somehow wound up being you."
        s "That’s cool. But I meant more that I haven’t exactly confirmed if {i}I{/i} have had sex with her yet."

    o "..."
    o "How...can you not know that?"

    scene otohacafetrip6
    with dissolve

    if bonus == True:
        o "Wait, she didn’t like...do stuff to you in your sleep or something...did she?"
        s "She very well may have done just that, Otoha..."
        o "Oh my God. That’s so messed up."
        o "She’s kind of controlling though, so I guess I could see that."

        "Sorry, Niki. I have tarnished your name once again."
        "Unless you actually {i}did{/i} assault me in my sleep."
        "If that’s the case-"
        "Nice."

        s "But anyway, you should probably get used to people wanting to “get it on” with you."
        o "That’s a little easier said than done, man..."
        s "Well, if you’d like...I could help loosen you up a-"
    else:
        s "I only recently started keeping a log of all my hugs. You're referencing a hug from a date range I didn't keep track of."

    scene otohacafetrip7
    with dissolve

    o "Oh, look. Is that a police officer behind you?"

    if bonus == True:
        s "I could help you learn to deal with any insecurities that may have led to your apparent disdain for unwarranted, romantically-focused attention from others."
    else:
        s "I hope so. I love law enforcement and would like to thank him or her for their service."

    if bonus == True:
        scene otohacafetrip8
        with dissolve

        o "Nah. I’m good."
        o "I’ll take my allowance now, though. I’m still waiting on that 1,000 yen."
        s "Who are you, my [niece]?"

        scene otohacafetrip9
        with dissolve

        o "Hmm...maybe more of a cool big sister."
        o "I guess little sister would also work given our current dynamic, though."
        o "But we should probably stop talking about this before Nodoka shows up out of nowhere and tries to write some doujin about us."

        scene otohacafetrip1
        with dissolve

        o "Since you won't be giving any generous contributions to my music fund, do you want to at least take a trip to the cafe with me?"
        o "It's not like I have anything else going for me this morning since I don't have lessons."
        o "Plus, it will probably be really funny to see Rin’s reaction to the two of us showing up together."
        s "I feel like she will either love it or absolutely hate it."
        o "I’m leaning toward the former. I think she’ll be stoked to know that two of her confirmed “favorite people” have started hanging out."
        s "Just wait until she learns we’re family now as well."

        scene otohacafetrip10
        with dissolve

        o "Come on, big bro! Let’s go torment our favorite barista!"

    scene black
    with dissolve2

    if bonus == True:
        "Otoha and I set off toward the cafe and I feel slightly bad for Molly in not giving her the title of my favorite barista."
        "But, to be fair, Molly is very bad at her job."
        "I can’t even remember if she’s ever actually sold me anything. "
        "At least Rin tries."
        "Tries a little too hard sometimes, sure. But she tries."
        "A short while later, Otoha and I wind up outside the cafe and exchange one final look of platonic sibling love before walking in and ruining (Or making) Rin’s day."
    else:
        "Otoha and I set off toward the cafe after that because our throats get all dry and scratchy and we need milk to make them feel all nice again."

    "........."
    "......"
    "..."

    if rinbetrayed == False:
        scene otohacafetrip11
        with dissolve

        o "Yo! Morning."
        s "One copyrighted frozen beverage please."
        r "..."
        r "Well I definitely don’t like this."
        o "It’s cool. We’re family now."
        r "..."
        r "Does Nodoka know?"
        s "I demand customer service."
        o "Not yet. We’re trying to keep it a secret from her."
        o "You want in as well?"

        scene otohacafetrip12
        with dissolve

        r "Yes. Immediately."
        r "Tell me what I must do."
        o "Nothing {i}that{/i} serious..."
        o "Just...you know. Maybe letting me play here sometime?"
        o "It’s a little too cold out to be playing in the park right now, and Sensei came up with the idea of maybe playing in the cafe."
        o "If that’s cool, I mean. I totally understand if it’s not."

    else:
        scene otohacafetrip13
        with dissolve

        o "Yo! Morning."
        s "One copyrighted frozen beverage please."
        r "..."
        r "Are you fucking kidding me?"
        r "Was the first time not enough? "
        r "You’re really going to do this again?"

        scene otohacafetrip14
        with dissolve

        o "Wait, what? What’s going on?"
        o "Is everything okay? We didn’t come here to mess with you or anything."
        r "Maybe {i}you{/i} didn’t."
        r "It wouldn’t be the first time Sensei decided to start getting close to someone I...am friends with, though."
        s "..."
        s "Yeah. This probably wasn’t a good idea after all."

        scene otohacafetrip15
        with dissolve

        o "Well...I’m really sorry if we upset you..."
        o "But we’re really just here to ask if it would be okay for me to...maybe play in the cafe sometime."
        o "It’s a little too cold out to be playing in the park right now, and Sensei came up with the idea of maybe playing here."
        o "If that’s cool, I mean. I totally understand if it’s not."

    scene otohacafetrip16
    with dissolve

    r "Oh my God, yeah! Totally!"
    r "I mean, it’s not really up to me. But my manager like, really has a thing for [teenage]girls. So you’re basically already locked in."

    scene otohacafetrip17
    with dissolve

    o "Hell yeah! Mission complete! "
    s "Wait, you know about that?"

    if bonus == True:
        r "Dude, why else would she hire exclusively cute girls? We work in a cafe, not a topless bar."
        s "I’m pretty sure Haruka thinks she’s managed to hide it from you."
        r "Then she should probably stop “accidentally” sending pictures of her in her underwear to our group chat and saying they were meant for someone else."
    else:
        r "Dude, why else would she hire exclusively cute girls? We work at a cafe, not Hooters."

    scene otohacafetrip18
    with dissolve

    o "You know, maybe we should think of other places just in case. The cafe is cool and all, but-"
    s "Don’t you dare chicken out after coming this far. "
    s "Think of what Niki would do."
    o "Is like...{i}everyone{/i} on this side of town weird, or?..."
    s "If you think this is bad, you should take a visit to the old district."

    scene otohacafetrip19
    with dissolve

    o "Uhh...I’m good. That place kinda creeps me out."
    r "I’ll try talking to Haruka about it. I’m sure she’ll say it’s fine, but...Hey, you never really know."
    r "Do you guys need anything? I’m in charge today, so I can give you extra shots for free or something."
    s "Two “Rin Specials” please."

    scene otohacafetrip20
    with dissolve

    r "You got it, Sensei."
    r "Go sit down. I’ll bring over something crazy in just a minute."
    o "What did you just order me? "
    s "Don’t worry about it."
    o "But...I’m lactose intolerant. "

    scene black
    with dissolve

    "Otoha and I make our way to a table only slightly touched by the sun and take our respective places at opposite ends."
    "Rin shows up a few moments later with two different drinks and sets one in front of each of us before rushing back to the counter to help another customer..."

    scene otohacafetrip21
    with dissolve

    o "So, I might as well get it out of the way now and say thanks for coming up with this idea."
    s "Don’t thank me until it’s at least been approved."
    o "But you guys said it yourself, I’m basically locked in."
    s "Sure. But what if Haruka thinks you’re so attractive that she won’t be able to contain herself around you?"
    s "That could affect business."
    o "..."
    s "Well?"
    o "Let’s talk about something else."
    s "Sure. Let’s talk about Rin instead."

    scene otohacafetrip22
    with dissolve

    o "Welp, guess the chance for a normal conversation topic is off the table."
    s "How are things going for the two of you now that you don’t live far enough apart to come up with excuses for not hanging out with her?"

    scene otohacafetrip23
    with dissolve

    o "Wait, what? What are you talking about?"
    s "Weren’t the two of you supposed to go on a trip to some arcade in your neck of the woods a while back?"
    s "I wound up going in your place."
    o "Yeah, but that was because my parents wouldn’t let me go. It had nothing to do with me trying to get out of it."
    o "I thought it sounded really fun and we’ve already made new plans to go there together."
    s "Oh, really? I didn’t hear about that."
    o "Yeah. I was never trying to avoid her or anything if that’s what you were thinking."
    s "Well, that’s good. "
    s "She didn’t really let it show, but she was pretty upset that day."

    scene otohacafetrip24
    with dissolve

    o "Oh come on...I like, {i}just{/i} stopped feeling bad about that..."

    if rinbetrayed == False:
        scene otohacafetrip25
        with dissolve

        o "Besides...didn’t getting to go in my place kind of like...work out for you or whatever?"
        s "What do you mean?"
        o "I mean that like...you guys kissed or something, right?"
        s "..."

        "Rin told her that?"
        "Why?"
        "I figured she’d be worried about that ruining her chances with Otoha."
        "Maybe she just...doesn’t want to hide anything from her?..."
        "I don’t know."

        s "Yeah. We did."
        o "Yeah. So like...sorry if it seems like I’m trying to take your place or something. Even if that was only a one time thing."
        s "I don’t think you’re trying to take my place. "
        s "Hell, I don’t even fully understand what my “place” with Rin is."
        s "I just wasn’t sure what to think about how you two were doing specifically now that you’re seeing each other a lot more."

        scene otohacafetrip26
        with dissolve

        o "More or less the same as we were before. "
        o "Just now I don’t have to worry about the pressure of being her first kiss if we {i}do{/i} wind up becoming anything more than what we are now."
        s "Wait, so you’re okay with what happened between us? There’s no lingering resentment or anything?"

        scene otohacafetrip27
        with dissolve

        o "Why would I resent anything about two people who like each other kissing for a few minutes?"
        o "Things like that happen."
        o "It’s not like me and her are dating."

        if bonus == True:
            o "Like, if I made out with Nodoka, I’m sure Rin wouldn’t be upset at all."
            s "I don't think that’s true. She likes you a lot."

        o "She likes {i}you{/i} a lot, too."
        o "It’s like she’s going through some...intense war inside of her head where you and me are duking it out for the upper hand."
        o "Just neither one of us is actually {i}fighting{/i} and it’s all on her."
        o "Pretty good material for a song, now that I think about it."
        s "Stop being so mature and cool or I’m going to start liking you too."

        if bonus == True:
            o "But you’re my brother. What would our parents think?"
            s "Haven’t I been telling you this whole time that they don’t matter anymore?"
            s "All that matters is {i}us{/i}, my dearest Otoha."
            o "..."
            s "..."

            scene otohacafetrip28
            with dissolve

            o "Okay. I’m uncomfortable now. "
            o "Let’s just talk about music or something instead..."

    else:
        s "There’s no need to feel bad. She still really likes you."
        s "The second you texted her that night, she completely stopped paying attention to me."
        s "And I don’t blame her after how I’ve treated her feelings in the past."

        scene otohacafetrip29
        with dissolve

        o "If you’ve messed with her feelings in the past, why do you seem so worried about them now?"
        s "Because I’m naturally a horrible person and you’re not."
        s "Rin still has faith in you. So if {i}you{/i} wind up screwing her over as well, she’s probably just doomed to romantic misfortune for the rest of eternity."

        scene otohacafetrip30
        with dissolve

        o "That’s putting way too much pressure on me, Sensei. That’s not fair."
        o "Rin’s happiness shouldn’t be entirely dependent on either one of us reciprocating her feelings. "
        o "I don’t think you’re a bad guy. I just think you might do bad things every once in a while."
        o "I’m no different."
        o "If someone’s feelings get hurt as the result of my actions, like they did with Rin and the arcade trip, I’m obviously going to be upset."
        o "But I’m not going to give up on everything I want just to make sure they don’t get upset anymore."
        o "I have no idea how I feel about Rin right now. And there’s a good chance I won’t for a while. I just..."
        o "I have no idea."
        o "Everything is all so new to me all of a sudden."
        o "So just let me kinda...take it all in for a little while, okay?"
        s "..."
        o "..."
        s "Yeah. Sure. The way I worded that was pretty bad anyway."
        s "I just meant there’s no need to get down about upsetting her since she still thinks you’re the coolest girl she’s ever met."

        scene otohacafetrip31
        with dissolve

        o "That really seems to be a recurring theme these days, huh?"
        o "Why does everyone think I’m so cool? Does playing guitar and singing really help that much?"
        s "I don’t know. I still think it’s the rings."
        o "Bring up the rings one more time and I’m cutting my fingers off."

    scene black
    with dissolve2

    "Otoha and I wind up talking until an orange glow consumes Kumon-mi and daytime begins to exit stage left. "
    "The cafe stays busy throughout the morning, so Rin never gets a chance to spend any time with us. "
    "I’m a little surprised that she was able to prioritize work over hanging out, though."
    "But I guess she might be trying to prove herself or something since Haruka was confident enough to leave the cafe in her hands for the day."
    "Either that or she’s just starting to realize that Otoha needs her space to thrive."
    "I don’t know if I’d go as far as saying she’s truly “out of the cage” yet-"
    "But Otoha's cage is extremely large. "
    "So I’m sure she still has plenty of room to fly and just...hasn’t found the door yet."

    $ renpy.end_replay()
    $ otoha_love += 1
    $ otohapark5 = True
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label otohapark10:
    scene otohaparkten1
    with fade
    play music "samhain.mp3"

    "I head over to the park first thing in the morning, unsure of whether or not Otoha will be bogged down enough by the Rin situation to show up."
    "And, in the event that you just haven’t been paying attention to what’s in front of you for whatever reason, she has."
    "Or...does?"
    "Did?"
    "She’s here."
    "Albeit a bit more melancholic than I'm used to- but I guess that can be attributed to the early morning winter sun, still fighting its way through a layer of clouds much thicker than normal."

    o "..."

    "She doesn’t say anything. In fact, she probably hasn’t even noticed I’m here yet."
    "Granted, she’s one of the last people to ever notice my presence to begin with- but maybe this new version of her, temporary as it may be, will give me the chance to get closer."
    "I’m sure it sounds cynical, but that’s the great thing about fracturing relationships."
    "The more cracks, the more opportunities you have to fill them."
    "Here’s hoping I’ve learned enough from “fixing” others that I can start repairing this creature as well."

    s "Morning."

    scene otohaparkten2
    with dissolve

    o "Oh. Hey."
    o "How long have you been creepily standing there watching me for?"
    s "A couple minutes. No longer than the typical amount of time I use to stare at you intermittently throughout the school day."
    o "You live an extremely exciting life, don’t you?"
    s "I can sense sarcasm in that response, but I’ll have you know that my life is actually {i}very{/i} exciting. "
    s "I am a time traveler. Kind of."

    scene otohaparkten3
    with dissolve

    o "And I’m Christina Aguilera. Kind of."
    s "I have no idea who that is."
    o "I am not at all surprised by that."
    o "Anyway, are you here to see me? Or are you just passing by on the way to meet up with somebody else?"
    s "You mean somebody like {i}Rin?{/i}"

    scene otohaparkten4
    with dissolve

    o "Uhh...I guess? I was talking more or less about pretty much everyone."
    s "It sounds to me like you want to talk about Rin."
    o "How does it even remotely sound like that?"

    "I’ve gotta say, I think I’m doing a pretty good job of getting Otoha to open up so far."

    scene otohaparkten5
    with dissolve

    o "I guess you’re not wrong, though."

    "Oh. "
    "I was just joking when I said that last thing, but it looks like my backwards method actually worked for some strange reason."
    "Cool."

    o "Figured it was only a matter of time until {i}somebody{/i} tried talking to me about it after what went down at the Christmas party."
    s "There’s no way I’m the first one."
    o "First one other than Rin. Not even Nodoka or Futaba have asked about it."
    o "To be fair, though, Nodoka’s in the middle of another manic episode right now, so she’s not really in the condition to be asking {i}anything{/i} other than...I don’t know. Weird shit."
    s "Well, I’m here if you want to vent."

    scene otohaparkten6
    with dissolve

    o "The hell will venting even do, though? You pretty much already know everything that happened."
    o "Recapping it again is just going to make me feel like shit."
    s "Some people just like talking about what it is that bothers them."
    o "And you think I’m one of those people?"
    s "You were certainly one of those people at the beach. I distinctly remember that occasion on account of the giant banana."

    scene otohaparkten7
    with dissolve

    o "Oh yeah. I wonder how that banana is doing."
    s "Listen, I’m obviously not going to force you to talk to me if you don’t want to. I just get how frustrating it might be to feel like everyone’s against you without looking at the big picture."

    scene otohaparkten8
    with dissolve

    s "Everyone already knows that your parents suck. "
    s "And if I were in your shoes and everyone just conveniently decided to forget that detail when I needed them to remember it most, I’d be pretty pissed."
    o "Do I even have the right to get pissed right now, though?"
    s "Why wouldn’t you? Getting angry is one of the few things we’re allowed to do whenever we want."
    o "Not without consequences, though. And Rin’s already so heated that even a slight raise in {i}my{/i} blood pressure would cause the...thin ice we’re on to melt."
    s "Well, maybe you two aren’t meant to be together then?"

    scene otohaparkten9
    with dissolve

    o "Wow. This suddenly sounds a lot less like me venting and a lot {i}more{/i} like you being a fucking dick."
    o "Why would you say that?"
    s "Probably because I didn’t expect you to react like that."
    o "Of course I’m going to react like that. Even if we’re fighting or whatever right now, Rin’s still my girlfriend. "
    o "Just because things aren’t going perfect doesn’t mean I’m going to pull the plug. "
    s "Then what’s the plan? Because I’m pretty sure we both know she doesn’t want to be kept a secret forever."

    scene otohaparkten10
    with dissolve

    o "Yeah. She’s made that {i}very{/i} clear."
    o "I don’t know, man. I don’t really have a plan. I’m too busy trying to figure out how to make her stop being mad at me to plan out what I’m going to do when it comes to my parents."
    s "Can’t say sulking in a park is how I’d make my significant other stop being mad at me, but if that’s how you want to do things, be my guest."
    o "Well, what would you do then? Since you’re so smart, I mean. How would {i}you{/i} make {i}your{/i} significant other stop being pissed off at you?"
    s "Maybe...buy her flowers or something?"
    o "Uh-huh. But what would you {i}actually{/i} do? Because I refuse to believe you would ever buy anyone flowers."

    if bonus == True:
        s "My real answer is significantly more sexual and I don’t think you and Rin are at that level yet."
    else:
        s "My real answer involves investing in a series of food trucks, but I don’t think you and Rin are at that level yet."

    scene otohaparkten11
    with dissolve

    o "Even if we were, that is absolutely not something I would tell you about."
    s "That’s fine because I imagine Rin would call me and tell me all about it immediately after."

    if bonus == True:
        o "You know, that’s probably true and it feels extremely wrong to me."
    else:
        o "She {i}does{/i} love food trucks."

    s "That’s just the kind of relationship she and I have, I guess."

    scene otohaparkten12
    with dissolve

    o "Then help me, dude. It’s weird saying this, but you probably know her a lot better than I do. How can I fix this?"
    s "You-"

    if bonus == True:
        o "How can I fix this {i}without{/i} using any of your weird, sexual methods?"
    else:
        o "How can I fix this {i}without{/i} using any of your weird food trucks?"

    s "They aren’t weird. They are completely natural."
    s "But if you really want to know, the only thing I can imagine working is backpedaling on what you said at the party and actually introducing her to your parents."
    s "She said she’d be fine being introduced as a friend, didn’t she? Why not just do that?"

    scene otohaparkten13
    with dissolve

    o "Oh, come on. Do you honestly believe {i}Rin...Rin Rokuhara...{/i}would be able to convincingly act like she is not absolutely obsessed with me for even a fraction of a second?"
    s "That is a very good point."
    o "Yeah. I’m caught between like...six rocks and a lesbian right now. Which is why I’m going into like, stasis mode at this park. Because I can’t figure out what to do."
    o "Shit, dude. I haven’t even taken my guitar out of the case yet. "
    o "Barely anyone ever comes here anyway, so it’s not like it’s a really big deal, but still."
    s "Just climb over one of those rocks and go visit her at work or something. It might not make her immediately forgive you, but it will be a start."

    scene otohaparkten10
    with dissolve

    o "It’s a little too late for that now. I’ve got lessons today and don’t really have time to stop at the cafe."
    s "Then I guess your relationship is over and Rin is doomed to hate you forever."
    o "Welp. It was fun while it lasted. Back to dating my guitar, I guess."
    s "Unfortunate. Rin is much cuter than your guitar."

    scene otohaparkten14
    with dissolve

    o "She is. But at least I can bring the guitar home without my parents thinking I’m like, mentally challenged or something."
    s "Are they really that bad? "
    o "I mean...kinda? They’re not {i}bad,{/i} they’re just really fucking old fashioned and want me to be some, like...normal housewife or something when I get older."
    o "Which, of course, is {i}literally impossible{/i} if you’re dating a girl. You know, since there are {i}absolutely no{/i} successful same-sex couples out there."
    s "Here’s a genius idea. I’ll pretend to be your boyfriend as a cover. Then, you can bring Rin home and-"
    o "No."
    s "Wait, you need to let me finish."
    o "Fine. Go."
    s "Then, you can-"
    o "No."
    s "Your loss. It was a great idea, too."

    scene otohaparkten15
    with dissolve

    o "I don’t think there has ever been a great idea that starts with a teacher dating a student."
    s "Tell that to roughly half of your classmates and I’m sure you’ll quickly find that you have an outdated outlook on this topic."
    o "Or...that our class is just fucking weird."
    s "That is also a fair assessment. "

    scene otohaparkten16
    with dissolve

    o "Man, I have no idea how this even turned into as much of a thing as it has."
    o "I figured Rin would kind of understand that this might be an issue for us, but I guess that shit just...doesn’t even occur to you when you grow up with two moms. "
    s "Oh. And why haven’t you met {i}them{/i} exactly? Didn’t Rin say they wanted to meet you?"

    scene otohaparkten17
    with dissolve

    o "Yeah, but..."
    o "I don’t know. I kind of want to. But, at the same time, that makes everything seem so much more...serious? Is that the right word?"
    s "Do you not think things are serious with you two?"
    o "I {i}do{/i}. But it’s like...a different kind of serious."
    o "Like...I want to just enjoy liking each other and...being free and stuff right now. "
    o "If I met Rin’s parents and they liked me, some of that freedom would kind of vanish. "
    o "Because if we {i}do{/i} break up- and this isn’t me saying I want to, but if we {i}do{/i}, knowing them will make things like ten times harder."
    s "So...you think the expectations of her parents would be some kind of intangible jail cell for you?"
    o "That’s not really how I would word it, but...I guess?"

    if bonus == True:
        o "I want things to just be Rin and me and...our friends. I don’t want any adults involved."
        s "But I’m an adult."
    else:
        o "I want things to just be Rin and me and...our friends. I don’t want any food trucks involved."
        s "But I love food trucks."

    scene otohaparkten2
    with dissolve

    o "Yeah. Your point?"
    s "You’re always so mean to me."

    scene otohaparkten15
    with dissolve

    o "It’s all in good fun. I like you more than I let on."
    o "Besides, you barely count as an adult anyway since it seems like you just kind of stopped mentally maturing somewhere along the line."

    if bonus == True:
        s "Yes, because the girl who’s afraid of her parents finding out she wants to bone a girl knows all there is to know about mental maturity."
    else:
        s "Yes, because the girl who’s afraid of her parents finding out she wants to hug a girl knows all there is to know about mental maturity."

    scene otohaparkten18
    with dissolve

    if bonus == True:
        o "I don’t want to “bone” anybody! What bone would I even bone with?!"
    else:
        o "I'll catch on fire if I hug anyone! Stop forgetting that extremely important detail about my character!"

    scene otohaparkten10
    with dissolve

    s "All things considered, I mostly understand how you feel."
    s "I don’t think it’s wrong to want to create a world where things won’t get any more complicated than your relationship with one person- but that sort of thing isn’t realistic."
    s "And I think that you know, even if you won’t admit it, that there would just be a different problem soon enough if this thing with your parents never happened."
    o "I don’t know that. How could someone ever know that?"
    o "The only thing I {i}know{/i} is that they’re the problem right now. And that if it weren’t for them, Rin and I would still be just as happy as we were before the Christmas party."
    o "I want that back."
    o "I don’t like where we are now."
    s "Then go somewhere else. Do something about it. "
    s "How much of what you’ve told me today have you told her?"
    o "To be totally honest...not a lot."
    o "But she’s hard to talk to about stuff like this. I don’t want her to internalize it and think it’s all on her when, in all actuality, it’s my...indecisiveness that’s creating these problems."
    s "{i}Tell her that.{/i}"
    o "Yeah, because the whole, “It’s me, not you” thing always goes over so well in movies."
    s "This isn’t a movie, Otoha."
    o "Good, because this movie would fucking suck."

    scene black
    with dissolve2

    "Otoha doesn’t say anything that I didn’t already expect to hear when I approached her today."
    "And while there was minimal refilling of cracks or fixing of anything, I did manage to learn that at least she doesn’t dislike me as much as she lets on."
    "But of course that’s what I’d jump to since it’s the only detail pertaining to me I was able to siphon out of the entire conversation."
    "I’m not involved in this. It’s not my {i}place{/i} to be involved in this."
    "I’m simply observing what could be either the earliest stages of a potential fallout...or the first of many hurdles in a long and successful relationship."
    "Unfortunately, this world doesn’t have enough long and successful relationships."
    "In fact, I can’t put my finger on a single one- but that’s mostly due to the fact that my fingers belong closer to short term options than ones that will grow old beside me."
    "In that sense, I wish Otoha the best in her pursuit of eternal youth or eternal freedom or whatever it is that she wants to last forever."
    "My wishes fall on deaf ears, but that’s okay-"
    "Because those things might be closer than she’s willing to believe."
    "Those wishes might come true."

    scene otohaparkten19
    with dissolve2

    o "Okay, well...I need to start heading out. But thanks for dropping by and letting me vent."
    o "Didn’t really sound fun at first, but I guess it did kind of help."
    o "I’m gonna text Rin and see if she’s able to talk about this tonight. I probably should be filling her in on some of the stuff I said to you if I really do want this relationship to work out."
    s "I’m glad I was able to help in...whatever way I was able to help."

    scene otohaparkten20
    with dissolve

    o "Cool. So, uhh..."
    o "See you later, then."
    s "..."
    o "..."
    o "You’re not going to ask me for like...a goodbye hug or something, are you?"

    if bonus == True:
        s "I am not."
    else:
        s "I wouldn't {i}refuse{/i} one. But that's not why I'm not leaving."

    o "..."
    o "Then...why are you not leaving?"
    s "Because I’m going to come with you to your lesson."
    o "No. You’re not."
    s "Why not?"
    o "Because I don’t want you to be there."
    s "{i}You{/i} might not want me to be there, but I’m not so sure your vocal coach feels the same way."

    scene otohaparkten21
    with dissolve

    o "Why do you even want to come? It’s going to be totally boring and that basement is cold as shit."
    s "I don’t have anything else to do today. And also, Niki confessed to still being in love with me and I thought it might be nice to drop by unannounced and make her blush."
    s "Besides, it’ll also give you an opportunity to see how a real couple deals with their issues."

    scene otohaparkten22
    with dissolve

    o "Wait, are you two actually back together?"
    s "No. But we act like we are sometimes, and I think that should be good enough."

    scene otohaparkten23
    with dissolve

    o "Ugh...whatever. I know there’s no stopping you once you decide to actually do something, and I’m already running late."
    o "I’m warning you now, though- it really is going to be boring. And if you do anything to mess up the lesson, I’m never talking to you again."
    o "I need this, dude. It’s an amazing opportunity. Please don’t mess it up for me."
    s "Otoha, why would I ever mess {i}anything{/i} up for you?"
    o "That emphasis on {i}anything{/i} is really starting to make me worry, Sensei."

    scene black
    with dissolve2

    s "Don’t worry at all, Otoha."
    s "If there is anything I am good at, it is spending time with Niki without causing her to get flustered or angry at anyone."
    o "I swear to God..."

    $ renpy.end_replay()
    $ otohapark10 = True
    $ otoha_love += 1
    stop music fadeout 10.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump otohaspecial10

label otohaspecial10:
    "The two of us make our way across town and, while I {i}think{/i} about asking Otoha if she needs any help carrying her things, I decide against it because the walk is kind of long."
    "Not extremely long, but long enough to make me not want to carry her things. Which I guess would be any amount of distance whatsoever."
    "But that’s beside the point."
    "Either way, she doesn’t seem to mind as she gets caught up in a text conversation with who I imagine is either Rin or a mysterious secret girlfriend she is keeping on the side."
    "Maybe that’s why Otoha doesn’t want Rin to meet her parents? Maybe they’ve already met her {i}real{/i} girlfriend?"
    "I can admire that."
    "I’ll have to ask her about how she manages to effectively keep her primary relationship hidden once we finish descending this suspicious staircase."

    scene otohabasement1
    with dissolve2
    play music "brighterdays.mp3"

    o "..."
    s "..."
    o "Something wrong, bud?"
    s "Do you really sing in here? Because I feel like this sort of environment would just kill the mood."
    o "The acoustics are nice at least."

    "I guess Otoha and Rin really weren’t kidding when they were talking about the sketchy basement Otoha gets her vocal lessons in."
    "To think someone like Niki would willingly spend time in a place like this is a little bizarre to me, though."
    "I get that her whole idol persona isn’t really the true “her,” but I can’t imagine the true her would like something dark and damp either."
    "But hey, if Otoha is fine spending time in a room where someone has probably been murdered, more power to her."

    ni "Oh, good. You’re-"

    scene otohabasement2
    with fade

    ni "Wait, why are {i}you{/i} here?"
    s "I want to learn how to sing."
    ni "Oh, okay. So Otoha tried to come alone and you followed her?"
    s "Stop knowing me so well. It makes my sarcasm less funny."

    scene otohabasement3
    with dissolve

    o "You guessed it. Sorry that he knows where you work now. I understand if you want to relocate and I’m willing to help you find some other sketchy basement if you want."
    ni "It’s fine. If it was anyone else, I’d be a little disappointed. But I’ve gotten pretty good at dealing with this thing over the years."
    s "So I’m just a {i}thing{/i} now?"

    scene otohabasement4
    with dissolve

    ni "Yes, but only just barely."
    ni "You can stay here and watch, but if you do anything to disturb my lesson, I’m...going to be really mad."
    s "I am shaking in my boots."

    scene otohabasement5
    with dissolve

    o "Oh, I brought back all those CDs and DVDs you lent me, and you were totally right. It’s really easy to see how you’ve improved over the years if you check everything out side by side."
    ni "I’m still getting better, too. And before long, I’m sure someone else will be saying the same sort of things about your performances."
    s "This is boring."

    scene otohabasement6
    with dissolve

    ni "Okay, {i}now{/i} you can leave."
    o "What exactly did you expect when you agreed to come to a singing lesson?"
    s "Well, singing for one."
    o "We’ve been here for a grand total of two and a half minutes. I don’t even know what today’s lesson is on yet."

    scene otohabasement7
    with dissolve

    ni "Oh, we’ll be working on your stamina today. The longer you’re able to last, the better and more consistent your performance will be."

    "Wow, maybe I {i}do{/i} want to learn how to sing after all."

    o "You’re not going to make me, like...dance are you? Because I can not fucking dance to save my life. And I’m not really trying to be an idol either."
    ni "I’m not going to make you dance. I’m talking more about vocal stamina anyway. "
    ni "And, while dancing does help to build up cardio and exercise your lungs, there are ways to improve it without going down that path."
    o "Welp, I’m ready whenever you are."

    scene otohabasement8
    with dissolve

    ni "Are you able to behave yourself while I show you how a real teacher does her job? Or are you going to continue annoying us until we pay attention to you?"
    s "I’ll just hang out on the couch until the lesson is over."

    if bonus == True:
        ni "If you’re going to watch porn on your phone, please keep the volume muted."
        o "Or just...don’t watch porn on your phone."
    else:
        ni "If you’re going to play Raid: Shadow Legends on your phone, please keep the volume muted."

    s "You two are really asking a lot of me today."

    if bonus == True:
        o "I think not watching porn on my instructor’s couch is a pretty fair thing to ask in exchange for following me across town."
        s "Fine. But I’m only agreeing to prevent Niki from “getting really mad.” I have no idea how I would survive something as rare and unheard of as {i}that.{/i}"
        ni "Have I told you that I hate you yet today? Because I hate you."

    scene black
    with dissolve2

    "Otoha and Niki move to the other side of the room, but that isn’t really saying much since this basement is only slightly larger than my bedroom."
    "I take a seat on the couch and observe my surroundings but, after running out of things to look at after only twenty seconds, I begin to focus on Otoha and Niki instead."
    "It’s refreshing to see the two of them out here this early in the morning just...doing what they love."
    "Even if what they love is no fun to observe if it’s not on some sort of stage."

    scene otohabasement9
    with dissolve2

    "Otoha takes her position near the stairs, straightening her body out and awaiting Niki’s instructions."
    "It’s the first time I’ve actually seen her interested in learning something but, to be fair, it’s not like I’ve created many opportunities for her to feel that way."
    "Maybe I should, though."
    "I mean, if Niki’s going to go out of her way to-"
    "You know what? Nope. I can’t do it."
    "I seriously contemplated the idea of teaching for a fraction of a second right there and I can already feel myself falling asleep."

    play sound "phonering.mp3"
    scene otohabasement10
    with dissolve

    "Oh, good. Someone probably felt that I was in trouble and is calling to keep me occupied and prevent me from falling asleep."

    o "Please tell me you’re not going to-"

    scene otohabasement11
    with dissolve
    play sound "phonebeep.wav"

    s "Hello?"
    o "...answer that."
    ni "Otoha! Eyes forward. Don’t pay any attention to him."

    scene otohabasement12
    with dissolve

    o "Got it."
    ni "If you’re ever going to make it as a musician, you’re going to have to learn how to avoid distractions."
    ni "Let’s make the most of this opportunity by pretending he’s some asshole in the crowd. "
    ni "Now, deep breaths. Take in as much air as you can and start warming up with the two octave pitch glide tactic I taught you. Whenever you’re ready."
    ni "Without the piano this time. You should be able to remember the notes by now. And I {i}will{/i} call you out if you’re off key."
    o "Understood."

    scene otohabasement13
    with dissolve

    s "Hello? Is anyone there?"
    r "{i}Oh! Yeah. Hey. Sorry, I thought I heard Otoha and- wait, yeah. That’s definitely Otoha.{/i}"

    if rinbetrayed == True and bonus == True:
        r "{i}Is she...is she fucking moaning right now?? What is that noise?? What the fuck are-{/i}"
        s "I’m at her singing lesson..."
    else:
        r "{i}But...what are those noises she’s making? What kind of weird stuff are you two getting up to without me?{/i}"
        s "I’m at her singing lesson."

    r "{i}Oh, right! She had one of those today.{/i}"
    r "{i}I was wondering why you didn’t show up to the cafe this morning. But now that I know you’re at her-{/i}"
    r "{i}Wait. Nope. Still not making any sense to me.{/i}"
    r "{i}Are her parents there too? Am I the only one not invited?{/i}"
    s "Yeah. Her entire extended family is here and we’re all saying bad things about you."
    r "{i}Ha ha ha. Do you guys have any plans after that? Because I have to work a little later today and I wanted you to come keep me company.{/i}"
    r "{i}But if both of you are together, that’s even bet- WAIT. IDEA.{/i}"
    r "{i}Otoha’s instructor is your ex, right? How “ex” is she exactly? Like...if I were to propose that all four of us went out on a double date tonight, would that be weird?{/i}"
    s "For me? No. But I figured you’d be a little hesitant given the current state of things."
    r "{i}Me? Nah. I’m over it.{/i}"
    r "{i}Well, not really. But this sounds fun and I kind of, like...need to get out and do something.{/i}"
    s "I’ll ask them, but-"
    r "{i}Shit! Like six million people just walked in. Gotta go, Sensei! Ask Otoha to check her phone whenever she’s done!{/i}"
    s "Sounds good. Talk to you later, Rin."
    o "AAAAaaaaaaAAAAAaaaa-"

    play sound "phonebeep.wav"
    scene otohabasement14
    with dissolve

    o "Wait, Rin? Why was Rin calling you?"
    ni "Ah-ah-ah! Eyes forward!"

    scene otohabasement15
    with fade

    o "Oh, yeah. Sorry...It’s just that the two of us are kind of fighting right now and-"
    ni "Singing now, drama later. You need to get your head in the game."
    ni "You think the audience would give two shits about what’s happening between you and your girlfriend? No. Because the audience wouldn’t even {i}know{/i} about your girlfriend."
    ni "In fact, the audience {i}is{/i} your girlfriend. As long as you’re up on stage, they are the only thing that matters."
    ni "Now, keep going."

    scene otohabasement16
    with dissolve

    o "Right now? But you’re still holding-"
    ni "Keep. Going."

    scene otohabasement17
    with dissolve

    o "A...AAAAAAaaaaaAAAAAaaaaAAAAAHHH..."

    scene black
    with dissolve2

    "Feeling that I’ve already annoyed Niki and Otoha (But mostly Otoha) enough during this lesson, I decide to remain quiet this time around and focus on the two of them as they get lost in their element."
    "Despite not properly following orders or whatever is going on, Otoha’s voice is both powerful and beautiful- which says a lot since she’s just cycling through one sound at different pitches right now."
    "And Niki...Well, she is just as much of a demon as always. But she clearly knows what she’s doing and is a lot more serious about teaching than I expected her to be."

    o "AAAAAAaaaaaah-"
    ni "Stop. No. What is that? What are you doing?"
    o "Huh? What? I...don’t know. What did I do wrong? It sounded fine in my head."
    ni "Yeah, that’s exactly the problem. Look-"

    scene otohabasement18
    with dissolve2

    o "Woah! Niki?"
    ni "Stop focusing so much on your head. Your voice is fine when you sing with that section of your body. What you’re struggling with is down here."
    ni "If you’re going to drop octaves, keeping everything up in your head is going to sound fucking horrible. You need to focus on your diaphragm more. "
    ni "How does it feel when I press there?"
    o "Uhhhhh...I don’t know?"

    scene otohabasement19
    with dissolve

    ni "Liar. Try singing right now."
    o "I...can’t."
    ni "Exactly. Because if I’m pressing down like this, it’s impairing your ability to not only breathe, but to bend and create sounds."
    o "I mean...yeah, but...that’s not really what I-"
    ni "Learning to use this properly is going to be a major key in controlling your stamina and expanding your range."
    ni "It sucks right now because all you’re doing is singing with your head. It’s no wonder you always sound so strained after a few songs. "

    scene otohabasement20
    with dissolve

    ni "And why the fuck is your face so red right now? Are you embarrassed? Why? There is {i}one{/i} person watching you."
    ni "If you’re this red now, I can only imagine how you’ll be when you’ve got thousands of people watching."
    ni "Assuming you’re ever able to perform for more than ten minutes without your vocal cords giving out and-"

    scene black
    with dissolve2

    o "Sorry, just gotta...run to the bathroom really quick! Be back soon!"

    "Otoha breaks away from Niki and darts up the stairs, leaving the two of us alone in the basement together."
    "........."
    "......"
    "..."

    scene otohabasement21
    with dissolve2

    ni "So...having fun?"
    s "You do realize why she was actually blushing that hard, right?"
    ni "Because I’m hot and famous and I was touching her. Anyone with even half of a brain cell would blush like that."
    ni "But I’m not just going to come out and say that to her when it would embarrass her so badly that she’d never come back."
    s "That just means more free time for you."
    ni "I don’t care about free time for myself. Otoha’s got serious potential, and I’ll be damned if I don’t help her get every last drop of it out."
    s "You-"

    if bonus == True:
        ni "If you make a fucking penis joke right now, I swear to God I’ll fucking kill you."
    else:
        ni "No. I do not want to open a food truck with you."
        s "Ugh."

    s "I was just going to say that I admire how strict and dedicated you are to your students. You’re a real role model, Niki."
    ni "I know I am. But thanks anyway."
    o "Okay! Back."

    scene otohabasement22
    with dissolve

    o "Sorry about that. Just needed to get some fresh air."
    ni "In the bathroom? "
    o "..."
    o "There was a window?"
    ni "Whatever. Just get back into position and we’ll start on some more stamina-"
    s "Oh, before that."

    scene otohabasement23
    with dissolve

    ni "What do you mean {i}before{/i} that? We’re on {i}my{/i} time right now. I don’t have all fucking day."
    s "I know. I just wanted to see if you’d go on a date with me."

    scene otohabasement24
    with dissolve

    ni "Wait...an actual date? Like...just the two of us?"
    s "Yeah."
    s "And Otoha."
    o "I’m sorry. What?"

    scene otohabasement25
    with dissolve

    ni "Oh, you better have a good fucking explanation for this."
    s "You know, I actually do this time. "
    ni "Well, then? Out with it."

    scene black
    with dissolve2

    "I tell Otoha and Niki about Rin’s double date idea and both of them seem to be completely fine with it after a short discussion."
    "Strangely enough, it’s actually Otoha who needs a little prodding in order to agree. But I’m sure that’s just because I’m going to be there."
    "Niki, on the other hand, is all for the idea. "
    "In fact, she likes it so much that she even offers to have one of the drivers from her agency come pick us up after a choreography session she has booked after Otoha’s lesson."
    "Not wanting to impose, however, Otoha rejects the idea and uses the whole “Improving her stamina” thing as an excuse to walk there instead."
    "Eventually, the two of them are able to get back to Otoha’s lesson, while I-"
    "Well..."

    if bonus == True:
        "Let’s just say I wound up watching something on my phone that neither of them wanted me to watch for the next hour."
    else:
        "Let’s just say I spent some time playing the number one mobile game of all time- Raid: Shadow Legends."

    "But..."
    "At least it was muted."

    $ renpy.end_replay()
    $ otoha_love += 1
    $ niki_love += 1
    $ otohaspecial10 = True
    stop music fadeout 10.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    jump otohadorm10

label otohadorm10:
    scene noonsky
    with dissolve2
    play music "icantseeher.mp3"

    o "What? Seriously?"
    o "Well, what are we supposed to do in the meantime then?"
    o "..."

    "Otoha and I are making our way to the cafe following her lesson, but I’m sure that’s about to change based on the apparent urgency of this phone call."

    o "But what if he like, kidnaps me or something?"
    s "Otoha, this way. I know a shortcut through a dark alley."
    o "Oh my God, it’s literally about to happen. Help."
    o "..."
    o "Yeah, I know. It’s fine. We’ll just kill some time or whatever until you’re off."
    o "..."
    o "Okay. Talk to you later."

    play sound "phonebeep.wav"

    s "I’m going to go out on a limb here and assume that was Rin."
    o "Yup. The cafe’s gotten way too busy for her to be able to chill with us, so she told us to “Save ourselves” and not bother coming."
    s "Looks like you and I will have to use this opportunity to bond, then."
    o "Guess so. But can we maybe cut back on the Rin stuff this time and talk about something more...fun?"
    s "I’m telling Rin you don’t think she’s fun."
    o "That’s obviously not what I mean. There’s just only so much drama I can handle before it becomes a burden."
    o "So if I have a chance to break away from that...I’m probably going to take it."

    scene black
    with dissolve2

    "We’ve reached the time of day where the sun begins to migrate to the opposite side of the globe."
    "We follow its light, for it always sets behind the dorms."
    "And, before we know it, we’re there."
    "We move away from the orange glow into a lobby brought to life by the welcome sensation of air conditioning, something that hasn’t been present here in quite some time."
    "The lack of windows makes it hard for air to properly circulate in here, so the difference in climate is noticed by both of us immediately."
    "We inhale deeply in unison, filling our lungs with the start of something we hope is wonderful."
    "Our eyes meet for a moment. "
    "Otoha smirks."
    "We go upstairs."

    scene otohaworkshard1
    with dissolve2

    o "Okay, so...remember earlier when I said that Nodoka was going through another manic phase?"
    s "Yes."

    play sound "glass.mp3"

    no "FUCK! NO! EVERYTHING IS WRONG!"
    s "She sounds pretty normal to me."
    o "Uh-huh. I guess destroying everything on her side of the room isn’t exactly {i}off brand{/i} for her, but we should still kinda tread lightly, you know?"
    o "Don’t ignore her existence because then she’ll think she’s like, turned invisible or something. But don’t spend too much time staring at her either."
    s "Otoha, if you want me to pay more attention to you, all you have to do is ask."

    scene otohaworkshard2
    with dissolve

    o "Noted. Opening the door now. Brace for impact."

    scene black
    with dissolve2

    no "Nononononono, bad! Bad marker! You stay alive while I’m spreading your guts out all over the board! That is an order!"
    o "Nodoka, I’m back. And I brought Sensei for some reason."

    scene otohaworkshard3
    with dissolve

    no "Why the fuck are you here?! Can’t you see I’m working?! Can’t you see?!"
    s "Where are your pants?"
    no "Pants??? Those things??? They inhibit the movement of my legs. Of course I’m not wearing pants. Why would anyone wear pants???"
    no "Get the fuck out of my room if you’re just going to talk about pants. Or help me. Yes, help me. I could use the help. Just don’t mention pants again. "

    scene otohaworkshard4
    with dissolve

    o "What do you need help with, Nodoka?"
    no "Something grey. And edible. I need you to find this. Find an item like that for me. Bring it to me. I need to look at it. It’s extremely FUCKING important."
    s "Nodoka, what are you writing on your board right now?"
    no "Secrets. Secrets, secrets, secrets. For me to know and you to find out. "
    no "The only problem is I DON’T FUCKING KNOW THEM EITHER. Get me something grey. Go. Shoo. Fetch. "
    o "I can’t think of anything grey and edible off the top off my head, so I’m going to take Sensei over to my side of the room and-"
    no "No. Bad. Bring him here. I need to see something. I need to stare at something. I need to stare into something so I can see it. And I can’t see him from all the way over here."
    no "Quickly. The marker is dying. It is the last one. The last one before a new one. You don’t want the new one. The new one is bad."

    scene otohaworkshard5
    with dissolve

    o "Uhh...have fun? I’ll be at my desk."

    scene black
    with dissolve2

    "I stare through Nodoka, trying to piece together the words haphazardly scribbled all over her dry erase board, but nothing comes to mind."
    "Carefully, I step over all of the things she’s pushed off of her desk and make my way over to her. "
    "The carpet is damp from spilled cups of old coffee and makes an interesting squishing noise the closer I get to the desk."

    scene otohaworkshard6
    with dissolve2

    "It was hard to notice from halfway across the room, but both her head and hands are shaking rather violently and her skin is an even paler shade of white than normal."
    "She locks eyes with me, pupils transitioning to colorlessness, and doesn’t say a word for roughly twenty seconds."
    "In the background, I can hear Otoha logging into her computer, followed by the sound of keys on a keyboard being pressed down."
    "Everything becomes apparent all at once."
    "Everything except why I’m here in front of Nodoka."

    no "They’re the same as hers."
    s "I’m sorry?"
    no "Deep. Black. Everything and nothing, shaped into a tiny little circle you can fit in your mouth."
    no "Yes. Yes. But...no. Wait. What? I thought I understood, but I don’t understand anything. Come closer."
    s "But I don’t-"

    play sound "static.mp3"
    scene otohaworkshard7
    with flash
    stop sound

    no "A girl with blue eyes. She came to me in a dream."
    no "She opened up her palm and showed me what she was holding. It was a little toy car."
    no "Her mouth opened thereafter and she swallowed it like it was a pill. She washed it down with a glass of orange juice."
    no "I can picture it driving around in the caves of her intestines- stopping at stomach ulcers to refill its gas tank before continuing on with its journey."
    no "What else resembles intestines, Sensei? List all of the long, tubular objects you know."

    "I list some things."

    no "Do you think I am something to love?"
    no "Do you think I am anything like her?"

    "I think."

    play sound "static.mp3"
    scene otohaworkshard8 with flash
    stop sound
    play sound "seek.mp3"

    "The world turns into a negative thing and my hands begin to feel kind of like the tongue of a clam but with more glass and less sand."
    play sound "seek.mp3"
    "I approach the girl who isn’t the other girl and get ready to raise my affection points with her."
    play sound "seek.mp3"
    "I wonder how many living things there are inside of us right now."

    play sound "static.mp3"
    scene otohaworkshard9
    with flash
    stop sound

    o "What did Nodoka want? Couldn’t really hear whatever was going on over there on account of all the whispering."
    s "To be honest, I’m not really sure."
    o "Yeah. I guess I can’t fault you for not understanding her when she’s...in that state."
    o "Seems quieter now, though. So whatever you two talked about must have helped in some way."
    s "Now, I just have to figure out how to help {i}you.{/i}"

    scene otohaworkshard10
    with dissolve

    o "Me? What do I need help with?"
    s "Well, judging by the mass amount of notebooks spread out all over your desk, I assume you’re having your own little bout of mania. Albeit one significantly less interesting than Nodoka’s."

    scene otohaworkshard11
    with dissolve

    o "Oh...hahah. Yeah. That."
    o "Uhh...I’m not really sure if I’d call it {i}mania{/i}...but I’ve been getting my ass kicked by some song I’ve been trying to write lately."
    s "What are you writing about?"
    o "Do you think I’d have this many notebooks out if I had any idea what the answer to that question was?"
    s "I have no idea. I’m not really familiar with your...creative process."

    scene otohaworkshard12
    with dissolve

    o "Okay. So, like...every notebook serves its own purpose. I keep them organized by a combination of genre, lyrical style, and the mood or tone of whatever the song I’m writing is."
    o "But, sometimes, when I can’t figure out what I’m trying to say, I have to hop between notebooks."
    s "You know you could just invest in those divider things, right? That way, you wouldn’t have to use a different notebook for literally everything you do."

    scene otohaworkshard13
    with dissolve

    o "Uh-huh. But then I’d also have to keep track of all of the dividers on top of all of the notebooks and that just sounds like too much of a hassle."
    s "I mean, the whole point of getting dividers would be to get rid of the notebooks."
    o "I hear you, and I’m glad you’re trying to help out, but there’s kind of a way I need to do things and I don’t really intend to change that any time soon."
    s "I just think that-"

    play sound "thump.mp3"
    scene otohaworkshard14
    with hpunch

    o "Back the fuck off! I’m not going to-"

    scene otohaworkshard15
    with dissolve

    o "Mm!"
    s "Woah."
    o "I’m so sorry. I didn’t mean to yell."

    scene otohaworkshard16
    with dissolve

    o "I’ve just been under a lot of stress lately...trying to balance everything out and whatnot."
    o "That’s why I’m hoping I can at least get this song right since everything else has been turning to shit. It’s nothing against you."
    s "That’s fine. Everyone gets overwhelmed from time to time."
    s "Don’t you think it might be best to focus on something a little more serious if you’re just trying to make {i}one{/i} thing right, though?"

    scene otohaworkshard17
    with dissolve

    o "Oh, come on. I thought we weren’t going to talk about her?"
    s "If your organizational skills were a little better, we probably weren’t."
    o "Dude, come on. I’m trying to write a song {i}for{/i} Rin. That’s why my shit is everywhere. I can’t risk fucking this up too."
    o "Am I going a little overboard? Sure. But it’ll pay out in the long run."
    o "I’ve got no problem killing myself like this so long as I’m able to get my point across."
    s "And what is your point, exactly?"
    o "No clue. See: desk."
    o "If I can just come up with like, a clear message or a clear point I want to get across...I can avoid having to blindly throw darts at a dart board like this."
    s "I’m starting to understand why you’re so unfazed by Nodoka’s apparent psychotic breaks."

    scene otohaworkshard18
    with dissolve

    o "Oh, please. Me overworking myself is {i}way{/i} different from whatever the hell is going on in Nodoka’s super-brain."
    o "I’ve got this under control, man. It’ll all be worth it in the long run."
    s "Famous last words, Otoha."
    o "What? What are you talking about?"
    s "Just that you should know more about the dangers of what you’re doing. Plenty of people have thought the same way only to end up in boxes."

    scene otohaworkshard19
    with dissolve

    o "You’re worrying about the wrong person, Sensei. I’ve got way too much shit to do. I don’t have time to die."
    s "Well, I hope that’s true. Because I kind of like you."

    scene otohaworkshard20
    with dissolve

    o "Huh?..."
    s "And I mean that in the least creepy way possible."
    o "Yeah. That didn’t sound creepy at all that time. That’s why I probably look so shocked."
    o "Like, it sounded like you actually being a decent person for once."
    o "I’m not really sure what to say."
    s "You can say you like me too. Nodoka is too out of it to remember, so it will be like no one ever heard anything."

    scene otohaworkshard21
    with dissolve

    o "I don’t...{i}not{/i} like you."
    s "I’ll take the double negative. I know what it really means."

    scene otohaworkshard22
    with dissolve

    o "You know...I know we’ve joked about it before. But today, you really {i}have{/i} felt kind of like an older brother or something to me."
    o "Annoying, yeah. And way too close to my personal space. But mostly full of advice and actually like, genuinely looking out for me. Kind of."
    o "I’m sure there are some horrible intentions mixed in that are the cause of that, but I’m going to ignore them for the time being since it’s actually been pretty nice so far."
    o "I always wanted someone like that. Someone to kind of...counterbalance how suffocated I always felt by my parents. Someone who would, at the very least, understand that..."
    o "And I’m not saying you do just yet.. But you’re closer to it than most people. That’s nice."

    if bonus == True:
        "I’m glad she’s able to look past my “horrible intentions,” because the way Otoha is blushing right now is certainly reinforcing them."
        "It’s no time to dwell on the sexual fantasies of a surrogate little sister, though. Not when it’s becoming clear that whatever hinges keep Otoha functional are slowly coming unscrewed."
        "It’s possible you might be thinking that {i}I’m{/i} thinking too deeply into this, but I’d like you to consider the countless other cases in which creative minds rotted from the inside out in pursuit of...anything."
        "There’s that old saying “A mind is a terrible thing to waste.”"
        "But, if that’s the case- why do we waste so many?"
        "And why is the beauty created by those minds only truly appreciated once they’re lowered into the soil?"
        "Some things can be beautiful above ground."
        "Before me is one of them."

    s "Just take it easy. Don’t get lost in whatever you’re doing and I’m sure everything will turn out...okay-ish."

    scene otohaworkshard23
    with dissolve

    o "Okay-ish is all I ask. So thanks."
    s "Also, if you ever want to call me “Big bro” or “Onii-chan” I am more than okay with it."
    o "I’ll think about it."
    s "That’s honestly more than I thought I would get. So thank {i}you{/i}, Otoha."

    scene otohaworkshard24
    with dissolve

    o "No problem, man. Just don’t go snooping around in my closet and always knock before coming into the room. We’ve gotta set some ground rules if we really want this to work out."
    s "I think this is the part where I tell some joke about having to check your closet to make sure you’re growing properly."
    o "Rad. Cause that means it’s also the time for me to punch you in the face and send you flying into orbit."
    s "At least I’ll die happy."

    scene black
    with dissolve2

    "Otoha and I spend the next hour or so hanging out in her room, swapping back and forth between casual conversation and observing her roommate’s manic episode."
    "And while I’d like to say that I’m glad she used this opportunity to take her mind off of working, I caught her jotting several things into several notebooks while we waited for night to come."
    "I guess some people just can’t stop even when you make it incredibly apparent that they should."
    "More power to her, I guess."
    "If Otoha thinks she’s able to just avoid being overwhelmed for the rest of eternity, she has every right to try and prove that."
    "But-"
    "That also gives us (Or just me, I guess) the right to tell her “I told you so” when she can’t do it anymore."
    "That day will most assuredly come. And, when it does, I’ll be somewhere beside her."
    "Close, but not too close."
    "Probably going through her closet."

    play sound "phonebeep.wav"

    o "Oh. Niki’s choreography thing just ended. She wants to know if we’re ready to head over to the restaurant yet."
    s "Is that what we’re doing? I remember agreeing to the double date thing, but I didn’t know we already chose a place."
    o "I guess so. It’s close-ish to the cafe, too, so Rin can probably come straight over after getting out of work in an hour."
    s "Are you going to be able to stay away from your ten thousand notebooks for the rest of the night?"
    o "Yeah. I’ve got a pocket-sized one that I keep on me at all times in case inspiration strikes while my babies are away."
    s "You have a problem, Otoha."
    o "Don’t we all, man? Don’t we all..."

    $ renpy.end_replay()
    $ otohadorm10 = True
    $ otoha_love += 2
    stop music fadeout 25.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump otohadorm10p2

label otohadorm10p2:
    "Niki once again offers to call a driver from her agency to pick us up, but Otoha remains adamant about not wanting to impose and decides to just charter her own ride off of a ride sharing app."
    "She asks me to chip in, which is mildly infuriating because it means she’s fine with imposing on {i}me-{/i} "

    if bonus == True:
        "But I guess it makes sense because she probably also wants to sleep with Niki more than she wants to sleep with me right now. Which I don’t blame her for."
        "Either way, I do my good deed for the week in an attempt to tip the scales by paying for the entire ride."
        "Now, Niki and I should be on equal footing when it comes to seducing our shared student."
        "Eventually, we make it to the restaurant and head inside."
        "Otoha informs the staff that we’re here to meet someone and, as if they're expecting us, they lead us over to Niki’s table, which has already been sectioned off from the others."
        "Niki is obviously no stranger to flexing her “famous” muscle, but she normally doesn’t do it like this."
        "I guess it’s a little different impressing [young]girls than it is impressing me, though."
        "And I’m not about to argue with additional privacy when that sort of thing has been becoming harder and harder to come by lately."
        "Anyway, Otoha and I take a seat at opposite sides of the table, and the wait for our final dinner guest begins..."
    else:
        "But, since I am such a nice and wholesome guy, I decide to pay for the entire ride and rate our driver with a perfect score of five stars so he can hopefully get a bonus and feed his family."

    "........."
    "......"
    "..."

    scene otohadinner1
    with dissolve2
    play music "love.mp3"

    o "So, uhh...Rin said she’s on her way."
    o "She also says that she is sorry in advance for, and this is a direct quote, “The overwhelming scent of vanilla bean [[COPYRIGHTED FROZEN BEVERAGE]s.”"
    ni "That bitch. Why would she not offer to bring us any? I love [[COPYRIGHTED FROZEN BEVERAGE]s."
    s "Is anyone else having a hard time comprehending the ends of sentences right now? Or is it just me?"

    scene otohadinner2
    with dissolve

    o "So...have you two, like...been here before? Because I’m starting to think this might be a little out of my price range."
    ni "Oh, don’t worry about that. I wouldn’t make you pay for your own dinner."
    s "You make {i}me{/i} pay for my own dinner almost every time we go out."
    s "Sometimes, you even make me pay for you."

    scene otohadinner3
    with fade

    ni "Yeah. And? "
    s "I just don’t think it’s very fair that Otoha gets treated better than me when I have brought you a much greater deal of joy in your life."
    ni "You bring me nothing but anger and fury."

    scene otohadinner4
    with dissolve

    ni "But we’re not here to talk about you. We’re here to talk about Otoha."
    o "Wait, we are? I thought this was just, like...a double date thing. Why do we have to talk about me?"
    ni "You just don’t normally bring your girlfriend around me. Rin, right? Is she the one you were with at the diner during your...dorm war whatever?"
    o "Yeah...and the reason I don’t bring her around you is because I only see you one day a week."
    ni "That didn’t stop you from bringing the man who simultaneously ruined my life and made it better all at once, though."

    scene otohadinner5
    with fade

    o "I mean...he kind of just came along. It’s not like I made the conscious decision to bring him there."
    s "We should do that more often. That basement is surprisingly homey for one of the most suspicious places I’ve ever set foot in."
    ni "I can’t tell if that's a compliment or not."
    s "I guess it's closer to being a compliment than {i}not{/i} being a compliment."
    ni "Your face is closer to being fucking stupid than {i}not{/i} being stupid."
    o "So, like...are you two getting back together or something?"
    ni "Yeah, {i}are{/i} we getting back together or something? Answer her question."
    s "I’m just here for the free food and cute girls."
    ni "{i}Girl.{/i} You mean me. It’s rude to call the other couple cute when you’re on a double date unless you’re trying to swing."

    scene otohadinner6
    with dissolve

    o "Well, it’s...still kind of a single date until Rin gets here. So if you two want to keep flirting or whatever, don’t mind me."
    o "I’ll just chill until I’m actually allowed to, like...cooperate and stuff."

    scene otohadinner7
    with fade

    ni "Hmm...you’ve never actually been on a double date before, have you?"
    s "Have {i}you{/i}?"
    ni "Shut the fuck up."
    o "I mean...no? This is the first relationship I’ve ever had. And I {i}definitely{/i} can’t say I envisioned my first double date also involving my teacher and a famous musician."
    ni "Are you nervous? Is that what’s going on? Because you seem less...Otoha than usual."
    o "I can assure you that I am the regular amount of Otoha. "
    ni "I guess I’ll hold off on passing final judgement until Rin shows up."
    o "Why am I being judged at all? What does my aptitude for conversing at a strange double date have to do with literally anything?"

    scene otohadinner8
    with dissolve

    ni "You’d be surprised."
    o "..."
    o "By {i}what?{/i}"
    s "I’m pretty sure Niki is just trying to sound like she knows what she’s talking about when it comes to relationships."
    ni "And I’m pretty sure that I may {i}accidentally{/i} walk out of this restaurant and leave you to pay for everything if you don’t humor me right now."
    s "So much for tonight being about Otoha."

    scene otohadinner9
    with dissolve

    ni "You fucking-"
    r "Hey! I’m here! Sorry for being so late!"

    scene otohadinner10
    with dissolve

    ni "Oh my God, hi! You must be Rin!"
    s "Finish your sentence, Niki."
    ni "{i}Die in a fire.{/i}"
    ni "It’s so nice to meet you! Otoha talks about you literally {i}all{/i} the time."
    o "I do? Oh...Oh, yeah! I definitely do. That’s a...true thing she just said."

    scene black
    with dissolve2

    "Rin shoves her bag under the table and takes a seat beside Otoha."
    "The overwhelming scent of whatever vanilla thing was alluded to earlier is immediately apparent, but not necessarily unpleasant in any sense."
    "I wonder if Otoha is sick of it by now."
    "I wonder if that’s something you can get sick {i}of.{/i}"
    "And I wonder how the rest of tonight is going to go now that what I view as a fracturing relationship is seated straight across from one that’s already finished breaking."

    scene otohadinner11
    with dissolve2

    r "Hey. I’d give you a hug and stuff, but I’m not really sure what the rules of double dates are or if you’d even be cool with that."
    r "So I’ll just say I’m hugging you in my mind right now and we can ignore how much I actually want to hug you."

    "Well, I guess Rin really is over the whole thing with Otoha’s parents."
    "Or just that she’s so in love that no amount of uncertainty could detract from her limited inhibition that causes her to constantly speak before thinking."

    scene otohadinner12
    with dissolve

    r "That aside, though...holy shit. I’m on a date with Niki Nakayama. "
    r "Well, not {i}with{/i} Niki Nakayama. But you’re here. And I’m here. At the date."
    r "We’re at the same place at the same time. Which is a date. But not the same date. "
    r "Wow."
    o "..."
    r "Wow."

    scene otohadinner13
    with dissolve

    o "So that’s Rin. Glad we’re all acquainted now."
    r "Hahah...sorry. I’m not around famous people all that often..."
    ni "{i}I{/i}, for one, see no issue at all with how you greeted me, Rin."
    ni "In fact, I think your reaction to me was completely within the bounds of how I expect {i}all{/i} people to react when meeting me."
    s "That’s because you’re a narcissist. "
    ni "Oh. And {i}you’re{/i} not? Please. I don’t want to hear it."

    scene otohadinner14
    with dissolve

    s "Everyone already knows the real me. How many people know the real you, though?"
    ni "What does that have to do with narcissism? What are you even trying to argue here?"
    ni "You know what, you really are paying for your own dinner. I was just joking when I talked about that before, but now I’m serious."
    r "Have they been like this the entire time?"
    o "Yuuuuuuuup."

    scene otohadinner15
    with dissolve

    r "Then I’m really sorry for not getting here earlier. I tried, but it was like, {i}crazy{/i} busy."
    r "You get one warm-ish day and people just frickin’ show up in flocks for [[COPYRIGHTED FROZEN BEVERAGE]s."
    o "It’s fine. Just try not to leave me alone with other couples anymore because I have learned tonight that I definitely do not like it."
    r "I’ll do my best."
    r "..."
    o "..."
    r "I missed you."
    o "I missed you too, Rin."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadinner16
    with dissolve2

    ni "Right?! Like, it should be up to {i}me{/i} if I want to take my music in a different direction! Not the stupid agency!"
    ni "People love {i}Niki.{/i} They don’t give {i}any amount of shits{/i} about 567 Productions. "
    ni "But nope! The money machine must churn! And I’m the only one fucking strong enough to push down the lever thingy!"
    r "It’s not fair! Like, you’re clearly {i}miles{/i} ahead of pretty much everyone else in your industry. And the fact that your talent is being suppressed like this is just...I can’t even."

    scene otohadinner17
    with dissolve

    ni "Otoha. I like this girl. You can bring her around whenever you want."

    scene otohadinner18
    with fade

    o "Wouldn’t that...you know...kind of get in the way of my singing lessons? I don’t really think I'll be able to focus if Rin is there."
    r "Do you...like giving lessons, Niki? Like, it must be some sort of passion project, right? Because I can’t imagine you’re making a lot of money off of them."
    ni "It’s 100%% a passion thing. Otoha’s got serious potential and I want to help her bring that out."

    scene otohadinner19
    with dissolve

    r "Right?! She’s absolutely amazing! I can definitely see her becoming like, mega famous one day if she keeps it up."
    r "That’s why I offered to start paying for her lessons if her parents decided to stop. I really think she has what it takes."

    scene otohadinner20
    with fade

    o "Rin, come on. Don’t bring them up right-"
    ni "Wait, are they seriously considering taking you out of vocal lessons? Why?"
    o "Great. I guess we’re talking about this now."
    ni "Of course we’re talking about this now. This is something you should have told me about immediately. "
    ni "What’s the issue? Why would they do something like that?"
    r "Oh...I don’t really think Otoha wants me to keep going. I already said too much."
    o "Thank you, Rin."
    ni "No, if they’re seriously considering this, {i}I{/i} need to speak with them. Because I can not allow that to happen."
    o "Niki-"
    ni "Is it a money thing? Because I will literally do this on spec. That’s how much faith I have in you, Otoha."

    scene otohadinner21
    with fade

    r "On spec? So like...you wouldn’t get paid until after Otoha starts making money off of her singing?"
    ni "Yeah. And even then, I wouldn’t really care. I’d be doing a disservice to the music industry if I didn’t help her hone that talent of hers."
    ni "I will literally give Otoha lessons for free if her parents are going to be fucking cunts about this."

    scene otohadinner22
    with dissolve

    r "For real?! That’s amazing! And so nice!"

    scene otohadinner23
    with dissolve

    r "Did you hear that, Otoha?! "
    r "You don’t have to worry about money anymore! Niki’s fine with giving you lessons for free!"
    r "Which means we don’t have to worry about-"

    scene otohadinner24
    with dissolve

    r "..."
    r "We...don't..."
    o "..."
    r "..."
    r "Otoha?"
    r "Why aren’t you freaking out? This is great news. "
    r "Isn’t it?"
    s "..."
    ni "Oh...no."

    "Niki instinctively reaches for the sleeve of my shirt, knowing that, somehow, she managed to do something wrong by simply being nice."
    "And, in a moment of rare self-gratitude, I feel a little better about never going out of my way for anyone."
    "Peoples’ true colors come out when you show them too much kindness."
    "And, it could just be the light-"
    "But Otoha looks very colorful right now."

    scene otohadinner25
    with dissolve

    r "..."
    o "..."
    r "It..."
    r "It wasn’t just about the money, was it?..."
    o "..."
    r "..."
    ni "..."
    s "..."

    "None of us say anything, and it becomes clear that Rin isn’t going to let silence answer this question either."
    "We just sit and wait for Otoha to do something."

    r "..."
    o "..."

    scene otohadinner26
    with dissolve

    o "..."
    r "..."

    scene otohadinner27
    with dissolve
    stop music fadeout 7.0

    r "Okay."
    r "Okay..."
    o "Rin-"

    scene otohadinner28
    with dissolve

    r "Thanks for coming tonight. I was really looking forward to it."
    r "I’m sorry I couldn’t stay any longer."
    o "Wait...Rin. Hold on."

    scene otohadinner29
    with dissolve

    r "I’ll call you later, Sensei."
    o "Hey! I said hold on!"
    r "For what?"
    o "I..."
    o "I don’t know."
    r "Well, let me know when you do."

    scene black
    with dissolve2

    "Rin grabs her bag from underneath the table."
    "The scent of vanilla bean vanishes with her."

    scene otohadinner30
    with dissolve2
    play music "thingsthathurt.mp3"

    ni "What the fuck are you waiting for?! Chase after her! "
    o "I-"
    ni "Don’t tell {i}me,{/i} idiot! Tell her! She’s the one who needs to hear it!"
    o "I..."
    o "Okay. Yeah."
    o "I’ll be right back!"

    scene otohadinner31
    with dissolve

    "Otoha runs out of the restaurant, nearly knocking over the waiter who I assume is carrying everything we ordered."
    "I breathe a sigh of relief for the expensive dinner Niki is about to buy for me-"
    "And another sigh for a girl who keeps gluing her heart to the wrong things."

    ni "Girls can be so fucking dumb sometimes. Just {i}talk.{/i} It’s that easy."
    s "Some things aren’t easy to talk about, I guess."
    ni "Ugh. Whatever. Guess it’ll have to just be a single date."
    s "Uh-oh. What happens if we fall in love?"
    ni "Not funny."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadinner32
    with dissolve

    o "Yo! Hold on!"
    r "Oh, you followed me out. What a surprise."
    o "I’m sorry, okay?!"
    o "It's just...this is all still new to me!"
    r "You mean dating in general? Or dating a girl?"

    scene otohadinner33
    with dissolve

    o "Both..."
    o "Would it be easier to tell my parents about us if you were a boy? Yes. Absolutely. "
    o "What’s normal for {i}us{/i} isn’t what’s normal for everyone else. But that doesn’t mean I don’t {i}like{/i} it."
    o "You think I would have willingly hung out with our teacher all day if we {i}weren’t{/i} going on this double date thing tonight?"
    r "I know you’d find it {i}easier{/i}. "

    scene otohadinner34
    with dissolve

    o "That’s not what I meant..."
    o "I just..."
    o "My parents aren’t like yours. {i}Most{/i} parents aren’t like yours."
    o "And we can’t just pretend they are because that’s more...convenient for us."
    r "Are you embarrassed to be dating a girl, Otoha?"
    o "That’s not-"
    r "Just give me a yes or no answer, Otoha."

    scene otohadinner35
    with dissolve

    o "..."
    r "..."
    o "Yes."
    o "I am."
    r "I’m so fucking stupid."
    o "You’re not, Rin..."
    o "You didn’t do anything wrong."
    r "Yeah, well..."
    r "That’s not entirely true either."

    scene otohadinner36
    with dissolve

    o "What?"
    r "..."
    o "What is that supposed to mean?"
    r "It {i}means{/i} that you’re not the only one who’s been hiding something for the sake of not making the other person uncomfortable."
    o "What...have you been hiding?"
    r "Take my shirt off and you’ll find out."
    r "Unless you’re too embarrassed to undress your girlfriend, of course."

    scene otohadinner37
    with dissolve

    o "Rin..."
    o "For real?..."
    r "You came clean about your thing, so it’s only fair that I come clean about mine."
    o "Stop walking."
    r "I don’t want to look at you."
    o "Why?"
    r "Because you’re too cute and it’s annoying and I won’t be able to be mad anymore."
    o "Stop walking, Rin."
    r "..."
    r "Fine. But we aren’t done fighting yet."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadinner38
    with dissolve2

    o "Why didn’t you tell me?..."
    r "Why didn’t you tell {i}me{/i} that you haven’t fully accepted your sexuality yet?"
    r "Unless you’re treating this like some sort of phase and that...you don’t {i}actually{/i} like me at all."
    o "You want to save the cutting thing for later? Fine."
    o "I wouldn’t treat this like a phase, Rin."
    o "I might be an asshole, but I'm not {i}that{/i} much of an asshole."
    r "Good. Because this definitely isn’t a phase for me, Otoha. "
    r "I like girls. I like {i}you.{/i} And yeah, there are people out there who think that’s disgusting or wrong or sinful or...do you think I haven’t heard all of that before?"
    r "I’m not even fully out yet because I can understand all of that. There are still plenty of people who don’t know that I’m bisexual."
    o "Rin, everyone knows you’re bisexual. You’re horrible at hiding it. But they don’t look at you any differently."
    o "In fact, {i}who{/i} do you care about that has looked at you differently for this? "
    o "Because the two people who raised me not accepting it seems like a pretty good reason for me to be wary about just announcing it to everyone."

    scene otohadinner39
    with dissolve

    r "I am {i}not{/i} a part of {i}everyone,{/i} Otoha! I am your {i}girlfriend!{/i} Whether you’re comfortable with that or not!"
    r "I need to know about things like this!"

    scene otohadinner40
    with dissolve

    o "And {i}I{/i} need to know when you’re fucking hurting yourself, Rin!"
    r "Then pay more attention..."

    scene otohadinner41
    with dissolve

    o "..."
    r "You’re always working. And I respect that. I really do."
    r "I just figured that, since I'm someone who’s apparently so bad at hiding things...my girlfriend would have maybe caught on about something being...wrong with me."
    o "There’s nothing “wrong” with you. And I will {i}try{/i} to pay more attention, but I don’t want you {i}trying{/i} to hide things like that from me."

    scene otohadinner42
    with dissolve

    r "Are {i}we{/i} even right together, Otoha?"
    r "Is {i}this{/i} right?"
    o "Why...wouldn’t it be?"
    r "Because you’re not comfortable being with another girl...and I’m too worried that I’ll wind up doing something that makes you think less of me."

    scene otohadinner43
    with dissolve

    o "It’s not that I’m uncomfortable! And I’m not going to think less of you for doing something like that!"
    o "I’m just overwhelmed, okay?! "
    o "I want my parents to accept us! {i}I{/i} want to accept us! I {i}like{/i} us! "
    o "I just need some more time getting adjusted, that’s all!"
    o "You’ve had your whole life to deal with these feelings, haven’t you? I’ve only had a few months."
    o "I’ve never felt this way about {i}anyone{/i} before, let alone another girl. So yeah, I’d be lying if I said it wasn’t embarrassing."
    o "But I don’t want to lie anymore. I want to try and make this work. But if you’re going to keep hurting yourself and not telling me about it, I-"

    scene otohadinner44
    with dissolve

    r "I never wanted to hide it from you..."
    r "I was just afraid you wouldn’t like me anymore..."
    o "Don’t be afraid of that."
    o "Please."

    scene otohadinner45
    with dissolve

    r "{i}*Sniff*{/i}"
    r "Are we breaking up?"
    o "Is that what you want?"
    r "{i}*Sniff*{/i}"
    r "No..."

    scene otohadinner46
    with dissolve

    o "Me neither."
    r "Are you going to keep me hidden forever?"
    o "Of course not..."
    o "Just..."
    o "For a little while longer. While I figure things out."
    r "{i}*Sniff*{/i}"
    o "Do you have any other demands, my queen?"
    r "{i}*Sniff*{/i}"
    o "..."
    r "Can we make out?"
    o "..."
    r "..."
    o "Like..."
    o "Like, literally right now?"
    r "{i}*Sniff*{/i}"
    r "Only if you want to..."
    o "..."
    o "Sure, Rin."
    o "We can make out."

    scene otohadinner47
    with dissolve2

    o "Mnh~ Mm..."
    r "Chu...hmnn...mm...Otoha..."
    o "Mn~ Mmm...Rin..."

    scene otohadinner48
    with dissolve

    ni "Are you two done making u- oh. "
    ni "They are making {i}out.{/i}"
    s "They certainly are."
    ni "Girls are fucking exhausting. I’m glad I never dated one."
    s "They certainly are."
    ni "..."
    s "..."

    scene otohadinner49
    with dissolve

    ni "..."
    s "..."
    ni "Wanna go make out in the bathroom?"
    s "I certainly do."

    scene black
    with dissolve2

    "And everyone lived happily ever after..."

    $ renpy.end_replay()
    $ otohadorm10p2 = True
    $ otoha_love += 1
    $ niki_lust += 1
    $ niki_love += 1
    $ rin_love += 1
    stop music fadeout 10.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "{i}Niki’s lust has increased to [niki_lust]!{/i}"
    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohaspecial15p1:
    scene otohasnewhair1
    with fade

    if _in_replay:
        play music "sweetvermouth.mp3"

    "I make my way into the dorm and, before I even have the chance to knock on anyone’s door, I find Rin hesitantly standing outside of room eight. "

    play sound "glass.mp3"
    with hpunch

    "And I now understand why."

    s "Is Nodoka broken again?"
    r "It’s been going on for like five minutes. I just want to kiss my girlfriend. "
    s "Let's hope it ends soon because I want to watch you kiss your girlfriend."
    r "You might have to hide outside the door and just peek in. I’ll leave it cracked for you. Otoha doesn’t like being watched, I don’t think. Or, I don’t know. Maybe she does. But I’m too scared to ask right now."
    s "I’ll go fill up a bucket of water that we can dump on her or something."

    scene otohasnewhair2
    with dissolve

    r "Are you trying to tell me I can’t get my girlfriend wet?"
    s "I was talking about Nodoka. But I can grab a second bucket for Otoha if you aren’t feeling very confident in yourself. "
    r "Better to err on the side of caution. Grab three buckets just in case something goes wrong with me as well."
    s "On it."

    play sound "dooropen.mp3"
    scene otohasnewhair3
    with dissolve

    no "What’s this about buckets?"
    r "Woah. You look pretty good for someone who was having a manic breakdown like, five seconds ago."

    scene otohasnewhair4
    with dissolve

    no "Breakdown?"

    play sound "glass.mp3"
    with hpunch

    no "I’m afraid I have no idea what you’re talking about."
    r "Sensei...she’s got telekinesis now...don’t make any sudden movements."
    s "Is that...Otoha throwing shit around in there?"

    scene otohasnewhair3
    with dissolve

    no "There comes a time in the spring of youth when we must {i}all{/i} throw something against the wall. Natsume Soseki said that."
    s "No he didn’t. "

    play sound "glass.mp3"
    with hpunch

    no "Okay. Maybe he didn’t. But I did just now and, let's face it- he wasn't {i}that{/i} much better than me. "

    scene otohasnewhair5
    with dissolve

    r "That’s...Otoha doing that? Why? She seemed fine when we were texting a few hours ago."
    no "Oh. That was me. Surprise."
    r "But I...told you I love you."
    no "And I love you too, Rin. If it were not for your relationship with my roommate, I’d have my tongue so far up your-"
    r "Please don’t finish that sentence."
    s "Please finish that sentence. "
    no "...vagina that I would be able to lick your tonsils."
    r "Are you...an eldritch horror now?"
    no "You can call me Azathoth. Azzie for short. Now, I believe we were about to make out?"
    r "No...I {i}believe{/i} you were about to tell me what’s going on with my girlfriend."
    no "There’s nothing going on with your girlfriend."

    play sound "glass.mp3"
    with hpunch

    r "..."
    no "Okay. There may be something going on with your girlfriend."
    no "But it’s no more than a standard case of the plight of the artist."
    no "In times like these, it is best to leave people like Otoha alone until they finish what they started."
    s "Now, despite how much experience I’ve gained throughout the undisclosed amount of time I’ve been here, I am no expert when it comes to the woes of an ailing female."
    s "However...I have a hard time believing it’s best to leave Otoha to her own devices if she is currently breaking glass all over your bedroom."

    scene otohasnewhair6
    with dissolve

    no "I break glass all over my bedroom all the time and you never come to {i}my{/i} rescue. And to think that I’ve been looking up to you as a father figure this whole time."
    s "I {i}do{/i} come to your rescue. You’re just beyond saving."

    scene otohasnewhair7
    with dissolve

    no "Aww...Daddy..."
    r "I won’t stay long...I just want to check up on her and make sure she’s doing okay."

    scene otohasnewhair8
    with dissolve

    no "Okay. But it won’t be pretty and you can’t say I didn’t try to warn you."
    no "Now, if you two will please excuse me, I have several prior engagements to tend to."

    scene otohasnewhair9
    with dissolve

    no "Oh, and under no circumstance should you attempt to touch her. I made that same mistake once just to see what would happen and it did {i}not{/i} go very well."
    no "Have fun!"
    r "..."
    s "..."
    s "So, it looks like it wasn’t Nodoka after all. "
    r "I didn’t even realize Otoha had a side like this..."
    r "Is it really okay to go in there? Shouldn't we just...leave?"
    s "Well...was it good for you those times I walked in on you at {i}your{/i} darkest?"
    r "I don’t know. Maybe? But if I didn’t know about this side of her, it means she’s probably been keeping it a secret on purpose, right?"
    r "What if she doesn’t want me to see her like that?"
    s "Only one way to find out."
    r "..."
    s "..."

    scene black
    with dissolve2
    stop music fadeout 5.0
    play sound "dooropen.mp3"

    r "Yeah...I’m just here to check on her. And if she wants us to leave, we’ll leave. "
    r "It’s that simple..."

    play sound "static.mp3"
    scene otohasnewhair10 with flash
    stop sound
    play music "allofthesounds.mp3"

    "{s}Except it isn’t.{/s}"

    o "Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad.
    Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad."
    r "Uhh...Otoha?"

    scene otohasnewhair11
    with dissolve

    o "Otoha isn’t here. Go away."
    r "I just...wanted to see if you were doing okay. It was pretty loud out in the hall-"

    scene otohasnewhair12
    with hpunch

    o "{b}WHAT FUCKING PART OF “GO AWAY” DO YOU NOT UNDERSTAND?! I’M WORKING!{/b}"
    r "Y-Yeah! Okay...Okay. That’s fine."

    scene otohasnewhair13
    with dissolve

    o "Oh. Crescendo. I don’t need words to get it across if everything the words are built {i}around{/i} starts spinning. Spinning and climbing."
    o "I will reach the top one way or another. It doesn’t matter how it happens, it just matters that I get there. If I get there, things will be good again. I have to make them good. I have to be good."
    o "I’m amazing. A prodigy. Everything I touch turns to gold."
    o "King Midas! Metaphor! Speak through symbols when nothing else can show how you feel! I will be heard. You will hear me."
    r "Uh..."
    s "Are you ready to leave yet?"
    r "I don’t really know...my mind is telling me no, but-"
    s "But your body is telling you yes?"
    r "This really isn’t the time for early 90’s pop culture references, Sensei. And you know things are bad when even I’m saying that."
    s "I couldn’t help myself and I’m sorry."
    r "What I was saying is that my mind is telling me no, but my heart is telling me that Otoha might need me right now."

    scene otohasnewhair15
    with hpunch

    o "{b}OTOHA, THIS! OTOHA, THAT! CAN’T YOU SEE I DON’T NEED ANYONE?! I CAN FUNCTION ON MY OWN! NOW LET ME WRITE IN FUCKING PEACE!{/b}"
    s "I’m starting to think Nodoka was right. Which is annoying because she’s kind of always right and there’s no way things can stay that way forever."

    scene otohasnewhair16
    with dissolve

    o "That way forever...something-something...clever?...In the...something...December...something remember! That’s it! The bridge is finished! I’ll fill in the blanks later! I’m a genius."
    s "Maybe the bucket would have been a good idea after all?"
    r "Otoha...can you at least look at me? Your hair’s a mess. Do you need anything to eat? A...shower maybe?"
    o "There needs to be something else...something different...a cello? Theremin? Something that will pop! To draw attention away from the parts that aren’t meant to stick the way the chorus is."
    o "But it can’t be too distracting. If it’s too distracting, {i}nothing{/i} will stick. And if nothing sticks, everything falls. Everything falls but me. I stay on top. Where I belong."
    o "{i}Somewhere I belooooong.{/i} Fucking Linkin Park, man. So good. I bet they wouldn’t struggle with fucking {i}bullshit{/i} like this. I’m a fake. I’m pathetic. Fuck you, Otoha. Fuck you. Piece of shit. You’re disgusting."

    scene otohasnewhair17
    with dissolve

    r "Hey...I’ll run to the convenience store and grab you dinner or something. After that, I’ll be out of your hair. Okay? Is there anything you want?"
    o "Dadadadaaa......dada.......daaaaa.....fuck. No. Again. From the top. Dadadaaaa-"
    s "Rin, I don’t know if that’s a good-"

    scene otohasnewhair18
    with dissolve

    r "Otoha, look at me. You don’t have to be perfect all the time if it’s weighing on you. You could always-"

    stop music
    play sound "slap.mp3"
    scene otohasnewhair19
    with hpunch

    r "Ngh-!?"
    o "{b}I TOLD YOU TO GET THE FUCK AWAY FROM ME, YOU ANNOYING PIECE OF SHIT! I’M TRYING TO WORK!{/b}"
    s "Woah. You can’t just-"

    play sound "static.mp3"
    scene otohasnewhair20 with flash
    stop sound

    o "Ah! Oh my god! Rin! I didn’t mean that! Are you okay?!"
    r "You just..."
    r "You just {i}hit{/i} me..."
    o "It was an accident! You surprised me! I’m so so sorry! Really! I get...jumpy when people sneak up on me like that!"
    r "Yeah...Yeah, I understand..."
    r "I was warned to not touch you anyway and..."
    r "I kind of just forgot...in the heat of the moment..."

    scene black
    with dissolve2

    "I take a step back and let the two of them figure this out."
    "I have no place here anyway."
    "........."
    "......"
    "..."

    scene otohasnewhair21
    with dissolve2
    play music "pianomelancholy3.mp3"

    o "Does it hurt? Are you okay? We should put something cold on your cheek so it doesn’t swell up. Holy shit, I can’t believe I just did that. Oh my god. Oh my fucking god."
    r "I’m fine...it wasn’t that hard. You just surprised me, that’s all."
    o "Rin, I’m so sorry. Hit me back to make up for it. As many times you want. I deserve it."
    r "I’m not going to hit you, Otoha..."
    o "You should! I just hit you! You’re my precious girlfriend who I’d do anything for and I {i}hit{/i} you! "
    r "Well, now you’re just making me blush."
    o "I’m so sorry. What can I do to make it up to you? Name it. I’ll do anything you want. Anything at all."

    scene otohasnewhair22
    with dissolve

    r "Did you dye your hair back?"
    o "Huh?"
    r "Your highlights are gone. When did that happen?"
    o "Uh..."
    o "I don’t...I don’t really remember...but why is {i}that{/i} what-"

    scene otohasnewhair23
    with dissolve

    r "You look...kinda {i}hot{/i} like this."
    o "..."
    o "What?"

    scene otohasnewhair24
    with dissolve

    r "Oh! Sorry. Just...one surprise after the other today."
    r "Otoha, if you want to make it up to me, just take care of yourself."
    r "I’m no stranger to locking myself away until {i}I{/i} find what it takes to move forward again. So I get it. And I’m not trying to change you or anything."
    r "This is...a new side of you, yeah. And I’m not sure why you hid it from me, but...that doesn’t matter right now. "
    r "What matters is that you eat...and maybe get some sleep...and {i}then{/i} finish your work. I’m sure the song you’re writing isn’t going to just run away on you."
    o "..."
    r "Okay?"
    o "Why are you being so nice to me?"

    scene otohasnewhair25
    with dissolve

    r "Because I fuck up all the time...You’re allowed to make a few mistakes as well."
    r "Just don’t go cheating on me or anything."
    o "You really don’t want to hit me back?"
    r "And risk damaging that beautiful face? I’ll pass. "
    r "Plus, now that it’s behind us, I actually think getting slapped was kind of kinky. I think I might be into it."
    o "..."
    r "..."
    o "Rin, I’m so sorry. I really am. It’ll never happen again."
    r "I told you. It's fine."

    scene otohasnewhair26
    with dissolve

    r "Also, Sensei is here. Say hi."
    o "..."
    s "..."
    o "Hi..."
    s "Hey, Otoha. You look fucking miserable."
    o "I’ve...had better days..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohasnewhair27
    with dissolve

    o "So, uhh...you saw all that?"
    s "I did."
    o "And...what did you think?"
    s "I think that your girlfriend is a little too forgiving and that you have a lot of work to do if you’re going to make up for slapping her across the face when all she was doing was making sure you were okay."

    scene otohasnewhair28
    with dissolve

    o "You and I might not agree on much, but...I can’t argue with any of that."
    s "On a somewhat brighter note, I now believe that you may be able to dethrone your floormates across the hall in the race for “messiest dorm room” seeing as both you {i}and{/i} Nodoka are like this."
    o "In my defense, even though I probably shouldn’t be trying to defend anything right now...she is much worse than I am."
    s "I don’t know. She’s never hit an actual person before."

    scene otohasnewhair29
    with dissolve

    o "I meant, like...in terms of...actual destruction..."
    r "Can we maybe just forget about the slap for now and try to make things normal again? I’m really not that bothered by it."
    o "There’s no way I can just forget that..."

    scene otohasnewhair30
    with dissolve

    o "I’m so embarrassed...and disappointed in myself...and so, so fucking stupid. I seriously can’t believe that just happened."
    o "And on top of that, I look like a serial killer and haven’t changed my clothes since Friday. So yeah, life’s not really coming up Otoha right now."
    r "When did this start?...And, better question, what {i}is{/i} this?"
    o "I don’t know...fucking...this just happens when I get too many...feelings, sometimes."
    o "It’s like...all I can think of is trying to write them down accurately, but then nothing ever makes sense and it drives me insane and I’ve always just...locked myself up until it was over."
    o "Just...can’t really do that anymore now that I live in a dorm with nineteen other girls. One of which I’m dating."
    o "I’m sorry you had to see me like this. Both of you. I know it’s not pretty."
    s "Well...you seem a little better now. But maybe it’d be for the best if you took a little break from writing to just...cool down or something?"

    scene otohasnewhair31
    with dissolve

    o "Cool down?! Now?! But I’m so fucking close to-"
    r "Otoha."

    scene otohasnewhair32
    with dissolve

    o "Yeah...you’re right. Sorry. I’m still kind of...caught up in the...colors...Uhh...no...No, thats not the right way to word it. Uhh...fuck. Give me a second."

    scene otohasnewhair33
    with dissolve

    r "This new song you’re writing..."
    r "It’s not about me...is it?"

    scene otohasnewhair34
    with dissolve

    o "Uhh..."
    o "I don’t...I don’t really like talking about my songs until they’re done, so..."
    r "Will you let me hear it once it’s finished?"
    o "..."
    o "Y-Yeah. Totally. You can...hear it...when it’s done. That’s fine."
    r "I’m looking forward to it..."
    o "..."
    r "..."
    s "Well...I should probably leave you two alone now that Rin is no longer at risk of being mutilated by her lover."

    scene otohasnewhair35
    with dissolve

    r "I wouldn’t mind having a bodyguard for the rest of the night now that it looks like Otoha doesn’t need to be alone anymore."
    o "I’d still...kind of like to be alone..."

    scene otohasnewhair36
    with dissolve

    r "But it would make me {i}reeeeeeeally{/i} happy if we could all go to the cafe together. And I could definitely use the pick me up after all I’ve been through tonight."

    scene otohasnewhair37
    with dissolve

    o "That’s mean...you know I can’t say no to you right now."
    r "Just for a little while? I’ve wanted to see you all weekend and I’d hate for this to be the way that ended."
    o "Are you...okay with me looking like this, though? Because I don’t really think I can do my makeup right now. My hands are all {i}blah{/i} from writing and erasing things all day."

    scene otohasnewhair38
    with dissolve

    r "Leave it to me! Years of self-mutilation have made me into a wizard with makeup and I have been practicing to one day apply my girlfriend’s since elementary school!"
    s "Welp, once again, I’ll leave you to it and-"

    scene otohasnewhair39
    with dissolve

    r "Nonsense! You’re coming too!"
    s "{i}Why?{/i}"

    scene otohasnewhair40
    with dissolve

    r "Because I don’t want this to be {i}your{/i} final memory of the weekend either. Let’s just all have some fun the way we normally do and put all of this drama behind us. Cool?"
    r "Barring Futaba, all my favorite people are here with me right now. And nothing would make it easier to put this all behind us than overpriced, caffeinated beverages I will receive at a discounted rate."
    o "I can’t have dairy..."

    scene otohasnewhair41
    with dissolve

    r "Soy milk exists. Now stop trying to make up excuses and go sit on the bed so I can make you look presentable. "

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I wind up walking around the room as Rin “fixes” Otoha to collect the shards of broken glass from things  that she and Nodoka have decided weren’t important enough to preserve."
    "I can’t help but contort my worldview until pieces of Rin are scooped into my hands alongside the shards. "
    "Is {i}she{/i} worth preserving in the eyes of someone who nearly shattered her just moments ago?"
    "Or will she eventually slip through Otoha’s fingers as part of another unfortunate “accident?”"
    "That remains to be seen."
    "And hopefully next time, I won’t be around for it."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ otohaspecial15p1 = True

    jump otohaspecial15p2

label otohaspecial15p2:
    scene otohapostcafe1
    with dissolve2
    play music "cafe.mp3"

    "After a long and mostly awkward walk, the three of us make it to the cafe to find things significantly busier than I have ever seen before."
    "What’s even worse is that Molly appears to be the only person working."
    "I’ll give you a few seconds to think about that."
    $ renpy.pause(3, hard=True)
    "Yeah. I know."

    mo "Uhh...okay! So, the line starts at the left and-"
    cussy1 "What’s a caramel macchiato? "
    mo "Well, it’s an espresso beverage with-"
    cussy2 "This line is taking forever. I want to speak to the manager."
    r "Oh man. I’ve seen this once before. Tourist bus."
    r "Good thing Molly’s working. She’s the only person on staff who even speaks English."
    o "Oh, right. Sometimes I forget that we’ve been speaking in Japanese this whole time."
    mo "Uhh...I’m actually the only person working right now. But if you’ll just be patient-"
    cussy3 "Did you just tell my wife to be patient?! How dare you! Now I would like to speak to the manager as well!"
    mo "Do you people even listen? I’m trying-"
    cussy4 "You people?! What is that supposed to mean?! The racism in this country is absurd!"
    mo "I’m not even Japanese! I’m European, just like you!"
    s "Why do we even have tourists? The city’s been closed for years."
    r "They all live in one giant hotel building in the Entertainment District and only leave a few times per year. Always in packs."
    s "Is this going to be a new subplot?"
    o "Can Molly really handle all of those people by herself?"
    r "Molly can barely handle one customer by herself, let alone an entire bus worth. But hey, at least they’re speaking her native tongue."
    mo "Okay! Everybody line up! I have no idea who to help first if you’re gonna come at me like this is some sort of gauntlet!"
    r "Hah..."
    cussy1 "The temperature in here is too high! Can we turn it down? "
    cussy2 "My son wants to watch TV! "
    cussy3 "I’m allergic to whipped cream!"
    mo "No, no, and...don’t get it then? Uhh...let’s see..."

    scene otohapostcafe2
    with dissolve

    r "Guys, I’m sorry. I know we came over here to cool things down and show Otoha that she {i}doesn’t{/i} have to work until her body gives out...but I’ve gotta help Molly. "
    o "Do you know enough English {i}to{/i} help? "
    r "Not really, but I’ll figure something out. I can’t just leave her hanging like this."

    scene otohapostcafe3
    with dissolve

    r "Is that okay? I’ll try and be quick. I promise."
    o "It’s fine. I’ve been alone with Sensei before and I’m somehow still alive. "
    o "Plus, I doubt he’ll try anything weird in a cafe full of white people. They {i}love{/i} calling the police."
    r "Okay. Come get me if you need me, alright?"
    s "Are we just going to ignore Otoha’s casual racism right there?"

    scene otohapostcafe4
    with dissolve

    r "Otoha, do you promise you’ll be nice to the white people while I’m gone?"
    o "As long as Sensei promises to not do anything that will make them call the police."
    s "There it is again. You can’t keep getting away with this."
    r "{i}Both{/i} of you be good. I have to go save Molly’s life. "

    scene black
    with dissolve2

    "Otoha (Who may or may not be mildly racist?) and I make our way through the labyrinth of Europeans to an unoccupied table not far from the end of the line."
    "Ideally, I would have liked sitting a little further away as it’s excruciatingly loud where we are, but it seems that every other table has yet to be cleaned —likely on account of the whole one employee thing."
    "But hey, if anyone can get Molly out of this rut, it’s Rin. "
    "Because even if she doesn’t speak the same language as all of the customers in the store right now, she {i}does{/i} know how to make a beverage."
    "It just...might not be the beverage any of those customers actually order."
    "........."
    "......"
    "..."

    scene otohapostcafe5
    with dissolve2

    o "..."
    s "..."
    s "I can’t tell if I like this new look or not."
    o "Are you physically attracted to girls who look like they just crawled out of the sewer?"
    s "Maybe?"
    o "Then you probably like this new look."

    scene otohapostcafe6
    with dissolve

    o "It’s not staying, though. I’ll be going back to normal in the morning."
    s "How come?"

    scene otohapostcafe7
    with dissolve

    o "Uhh...because this is the result of neglecting my personal health and hygiene for an entire weekend and is not indicative of a healthy lifestyle?"
    o "Also, having my bangs drop down in front of my eyes obscures my vision. I need to be able to see so I don’t...accidentally kiss the wrong girl or something."
    s "Or me."

    scene otohapostcafe8
    with dissolve

    o "Honestly, that would probably be more forgivable. "
    s "Cool, come here while she’s not looking."

    scene otohapostcafe9
    with dissolve

    o "Dude, come on. Not the time."
    s "I can’t think of a better time. I’ve barely seen you at all ever since the Dorm Wars ended. Though, that is for reasons I can’t really bring up without sounding clinically insane."
    o "Acknowledging the fact that I’ve been a complete dick to you for months wouldn’t make you sound clinically insane. It would make {i}me{/i} sound like a bitch, though."
    o "But that’s fine because I’m starting to realize that’s precisely what I am."
    s "Well, you did just slap your biggest fan in the entire world across the face with absolutely no consequences whatsoever."
    s "And you did throw a bit of a tantrum after Rin lost her trivia competition. Which is significantly more forgivable, but...still not a good look for you."
    s "And you {i}did{/i} skip out on the Christmas party for-"

    scene otohapostcafe10
    with dissolve

    o "I get it, okay? You don’t have to go and name every single thing."
    o "I’m in...this weird headspace lately that I’ve been having a lot of trouble pulling myself out of and I’ve been...kind of taking that out on the people who are around me."

    scene otohapostcafe11
    with dissolve

    o "I really {i}am{/i} sorry, though. I {i}have{/i} been wanting to say that, I’ve just had no idea how to approach you about it."
    o "I want shit to go back to normal. Or...at least whatever “normal” was for us since you’ve always been kind of a huge creep. Who has also seen my girlfriend’s boobs."
    s "They’re really nice. I won’t lie to you."

    scene otohapostcafe12
    with dissolve

    o "Right? They’re so much bigger than they look when she has her clothes on."
    s "Oh, good. I didn’t realize you two had actually made it that far yet."

    scene otohapostcafe13
    with dissolve

    o "There...have been pictures exchanged. As far as real life goes, though-"

    scene otohapostcafe14
    with hpunch

    o "Wait, why am I telling you this?! You’re my teacher! Stop me next time I go too far!"
    s "I’m not just your teacher, Otoha. I’m your {i}friend.{/i}"

    scene otohapostcafe15
    with dissolve

    o "Eww...gross."
    s "Isn’t that kind of what I was at the peak of our “normal,” though? "
    s "That’s what you want to go back to, right?"

    scene otohapostcafe16
    with dissolve

    o "I...guess. I don’t know. It just feels like things kind of shifted with us around Halloween and..."
    o "It pains me to admit this, but I’m kind of...jealous of you."
    s "Jealous? Of {i}me?{/i} Why? "
    s "You’re a hot, talented prodigy with a girlfriend who would do anything for you, a vocal coach who thinks you’re going to be a star, and attentive parents. Why would you be jealous of {i}me?{/i}"
    o "Because..."
    o "Because of Rin."
    s "..."
    o "You guys have this kind of chemistry that I can’t really figure out how to replicate. I don’t know."
    o "Maybe it’s because we weren’t ever really {i}friends{/i} the way you guys were since she’s been pining after me from the get-go."
    o "It’s not just with you either. I’ve been jealous of everyone that comes near her. Even Futaba sometimes, who is literally zero percent lesbian and not a threat at all."
    s "I don’t think Rin is going to leave you for anyone else if that’s what you’re worried about, Otoha."
    o "That’s the worst part. You’re probably {i}right.{/i} I just can’t seem to get a handle on that and keep lashing out at everyone regardless."
    o "Like, Chika fucking hates me now because she can see through that. But instead of appreciating her for caring that much about Rin, I automatically interpret it as “Chika wants to fuck her.”"
    o "And {i}you{/i} would hate me as well if you weren’t waiting to pick me up on the rebound or something because I’ve been nothing but cold to you for months."
    s "That is {i}why{/i} I like you."

    scene otohapostcafe17
    with dissolve

    o "What?"
    s "You and Yumi are pretty much the only girls in the class who see through all of the shit I do while not being afraid to point out how wrong all of it is. "
    s "I’m not going to hate you for seeing me as who I really am. "
    s "In fact, I wouldn’t hate you even if you went around and told everyone I’m having sex with Chika."

    scene otohapostcafe18
    with dissolve

    o "..."
    s "I know you know. Rin told me she accidentally spilled the details. You don’t have to play dumb. We can talk about it."

    scene otohapostcafe19
    with dissolve

    o "Gotcha..."
    s "Does it disgust you?"
    o "I need to be careful to not say the wrong thing right now because it will turn what was supposed to be an apology into...something else I’d have to apologize for."
    s "We’ve fucked probably a hundred times by now. And I have no intention of stopping — even if she’s half my age and half my size. "
    s "{i}Does that disgust you?{/i}"
    o "..."
    s "..."
    o "Do you love her?"
    s "Does it matter?"

    scene otohapostcafe20
    with dissolve

    o "{i}What are you doing, man? {/i}"
    o "If you know it’s wrong, why don’t you stop?"
    o "Dragging innocent girls down with you isn’t going to make you feel good at the end of the day. It’s just going to hurt them as well."
    s "And you want to protect Rin from that...don’t you?"
    o "I just don’t understand, Sensei. It’s not abnormal for people to {i}feel{/i} immoral shit like that from time to time, but once you start acting on those feelings...can you ever really be forgiven?"
    s "What do you think?"
    o "I think you can do better than this."
    o "In fact, I {i}know{/i} you can do better than this."

    scene otohapostcafe21
    with dissolve

    o "You’re...back together with Niki, aren’t you? Why don’t you just stay with her? "
    s "..."
    s "How did-"
    o "Because she’s happy. Like {i}really{/i} happy."
    o "She hasn’t said anything about it to me because why would she? But I can hear it in her voice. "
    s "Niki and I..."
    o "..."
    s "It’s complicated. "

    scene otohapostcafe22
    with dissolve

    o "{i}It’s only complicated because you keep running around and fucking teenage girls! It doesn’t have to be that way!{/i}"
    o "Chika’s the only one I know of, but who’s to say there’s not more?"
    s "There are."
    o "{i}Why?...{/i} "
    o "Why are you not trying to get a handle on this when it’s well within your power to do that? I don’t get it."
    s "You sound just like her sometimes, you know."
    o "Who?"
    s "Niki."

    scene otohapostcafe23
    with dissolve

    o "Oh, great. Just what I needed to hear."
    s "I mean it. I had a similar conversation with her recently and it all boiled down to the fact that I’m just...probably beyond saving at this point."
    o "You’re not beyond it, you don’t {i}want{/i} to be saved. Which is...really fucking annoying."
    o "There are tons of us out there who are struggling to keep the shitty parts of ourselves locked away and you’re just running around and flashing those parts of yourself for the whole world to see."
    o "That’s not the example you need to be setting."
    s "Am I a bad influence on you, Otoha?"

    scene otohapostcafe24
    with dissolve

    o "I think...you {i}are.{/i}"
    o "I can keep you out better than the other girls, sure- but when you’re around someone every single day, parts of that person are going to naturally start rubbing off on you after a while."
    o "Sensei, I want things to go back to normal with us...I want to be able to laugh and call you a creep the next time you barge into my room because I {i}know{/i} my girlfriend loves you. And I want to as well."
    o "But I’m afraid of what will happen to me if you stay the way you are."
    s "You don’t think...your freakout thing today was because of {i}me,{/i} do-"

    scene otohapostcafe25
    with dissolve

    o "No! No, no, no! That was a totally different thing! That’s more of the Otoha who can’t get her thoughts in order right now!"
    o "But there’s an Otoha somewhere underneath that who {i}isn’t{/i} drowning yet...and she needs someone to throw her a lifejacket instead of holding her head underwater."
    o "{i}I need help.{/i}"
    o "I really need help..."
    s "With...what? What do you need?"

    scene otohapostcafe26
    with dissolve

    o "Uhh..."
    o "So..."
    o "I know you already said you wouldn’t care if I went around telling everyone about you and Chika, but...I’m gonna pretend you {i}didn’t{/i} say that to try and like...use it as a bargaining chip for a sec?"
    s "Uhh...okay?"
    o "So, uhh..."
    o "You remember how I didn’t come to the Christmas party?"
    s "I do. And I also remember how torn up Rin was the whole time."
    o "Yeah, well..."
    o "There was a good reason for that. And by “good” I mean bad. There was a {i}bad{/i} reason."
    o "You, see..."
    o "Uhh..."
    o "While you guys were off having fun and doing...holiday stuff, I was-"

    scene otohapostcafe27 with dissolve
    with hpunch

    o "Ah!"
    r "Hi! We’re almost done. My English sucks. I just wanted to take a five second break to tell you how much I miss you and appreciate your existence on this planet."
    r "Also, I love you. And I know you don’t want to say it back yet and that’s totally cool. Also, you’re hot."
    r "Anyway, bye. "

    scene otohapostcafe28
    with dissolve

    r "Love you too, Dad. You don’t have to say it back either."

    scene otohapostcafe29
    with dissolve

    "Rin walks back up to the counter and I’m suddenly left with a significantly quieter Otoha now that our conversation has been interrupted."

    o "..."
    s "..."
    o "Hah..."
    s "What were you saying just now?"
    s "About what happened on Christmas..."
    o "..."
    s "..."

    scene otohapostcafe30
    with dissolve
    stop music fadeout 3.0

    o "It doesn’t matter."
    o "Just...stop being such a weirdo all the time, okay?"
    o "Let’s be...{i}friends.{/i}"
    o "I have to get along with you if she does. And it’s not like I think you’re the worst or anything as-is."
    s "Otoha-"
    o "I can’t handle any more today. "
    o "Please leave it at that."

    scene black
    with dissolve2

    "I leave it at that..."
    "And the day comes to an end without me ever discovering what it is she has to hide from me."

    $ renpy.end_replay()
    $ otohaspecial15p2 = True
    $ rin_love += 1
    $ otoha_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label otohadate20:
    scene otohadarkness1
    with fade
    play music "brighterdays.mp3"

    "In my efforts to head over to the cafe for another randomized beverage, I encounter a familiar face at the counter — one not presently obscured by a new, alternative haircut that would be subsequently discarded."
    "That person’s name is Otoha Okakura and she is hiding something from me."
    "But at least she’s smiling today and not hitting anyone. "
    "One step at a time."

    s "Hello. One order of lesbians, please."

    scene otohadarkness2
    with dissolve

    r "Hot and with cream?"
    s "Y-"
    o "Don’t even think about answering that question."
    s "Just black, please."

    scene otohadarkness3
    with dissolve

    r "I’ll keep an eye out for you."
    o "Here to hit on my girlfriend again?"
    s "Or you. Are you having trouble holding that guitar with your fragile girl muscles? Would you like a big, strong man like myself to take over?"

    scene otohadarkness4
    with dissolve

    o "I think my fragile girl muscles can take it. You can pay for my drink though if you want me to ignore your blatant sexism."
    s "You never bought anything for all of those Europeans. "
    o "There were too many of them and I didn’t have any cash on me. Now, fork it over. You owe me."
    s "For {i}what?{/i} You’ve done literally nothing for me."
    o "No, but Rin probably has. Which means that {i}I{/i} kind of have by extension since we’re a package deal now."
    r "Just without the package."
    s "That-"
    r "Because we’re girls."
    s "That is-"
    r "Girls don’t have dicks."
    s "Yes. Thank you, Rin. That is not how that works, Otoha."
    o "Yeah, you’re right. I just feel bad getting free stuff all the time and thought it would be nice if I stopped inadvertently draining Haruka’s bank account."
    s "Please don’t solicit me for items you would otherwise receive for free. Thanks."

    scene otohadarkness5
    with dissolve

    r "Speaking of Haruka, I’ve been talking to her more about setting up that open mic thing we discussed if you’re still interested."
    r "I figure something like that might be good for the band too whenever we, like...actually have music."
    r "But you could always do your solo stuff. My mom wants to play too now that I’m no longer capable of hiding this place."
    s "Rika plays guitar?"

    scene otohadarkness6
    with dissolve

    o "Dude, Rin’s mom can play {i}everything.{/i} She’s like a grown up Noriko with boobs and additional talent in place of all the rebellious little sister energy."
    r "She’s okay. I’ve heard better."
    s "Be nice to your mom, Rin."

    scene otohadarkness7
    with dissolve

    r "Shut up, Dad! If you need me, I’ll be in my room!"
    s "I take it she’s still hanging around the dorm then?"
    o "That...would be an understatement. Rin and I barely ever get to be alone in her room anymore so we’ve had to chill in mine. "
    s "That doesn’t sound so bad."
    o "Yeah, until you remember that my roommate wants to have sex with anything that moves. Including but not limited to both Rin {i}and{/i} me."
    s "I...can come keep her busy?"

    scene otohadarkness8
    with dissolve

    o "I think we’re good. Right, R- why did I even ask?"
    r "It’s probably best if I don’t say anything right now. I might squeak. "
    o "Keep it in your pants, okay? You’re at work."
    s "So, what? You’re just hanging out here instead of the park today? Aren’t you missing out on...money or exposure or whatever it is you’re normally shooting for over there?"

    scene otohadarkness9
    with dissolve

    o "I’ve got lessons today. In fact, I should probably start heading over to them now. I just wanted to drop by and see how Rin was doing first."
    o "You two can have fun without me, though. I’ll be-"
    s "Nah, I’ll come with you."
    o "Nah, you won’t."
    s "No, I will."
    o "Mmmm...no thanks. I’m good."
    s "I insist."
    o "Wow, you really just don’t know how to take no for an answer, do you?"
    s "If you start crying, I can probably hold myself back."
    o "Oh, okay. That’s not a creepy thing to just slip in there out of the blue. Cool."
    r "Want something for the walk over, Sensei? Latte? Cappuccino? Copyrighted frozen beverage?"
    s "Just mix a bunch of random syrups into one cup and give me that. That is what I want."
    r "One black coffee, coming right up."

    scene otohadarkness10
    with dissolve

    o "Interesting order."
    s "I think I discovered just now that the only way to get what I want at this store is to ask for the exact opposite. This is a major breakthrough and you should be happy for me."
    o "Are you really coming to my lessons again?"
    s "Yeah. I want to bang your teacher when you guys are done."
    o "Thank you for sharing that absolutely vital information with me. I don’t know what I would have done if I had to leave practice {i}without{/i} knowing you two were about to have sex on the couch I eat lunch on."
    s "Just trying to be the best friend I can, Otoha. You know I’d {i}never{/i} hide anything from {i}you{/i}, right?"

    scene otohadarkness11
    with dissolve

    o "Hahah...hah..."
    o "Time to go."

    scene otohadarkness12
    with dissolve

    r "Ah, wait! Otoha! Are you still coming over later? Futaba’s parents sent her a Ouija board and I want to communicate with the ghost of the fifth floor."
    s "The what?"
    o "Yeah! I’ll be there. Is it still cool if Nodoka tags along?"
    s "What ghost of the fifth floor?"
    r "Cool! See you later, then! Have fun at practice!"

    scene black
    with dissolve2

    s "Stop introducing new subplots. There are already too many."
    r "Sensei! Your coffee. Here."
    r "Take care of my woman, you hear me?"
    r "Just not in a sexual way because I would cry and I’m on a solid no-crying streak right now."

    "I take the cup from Rin and have to break into a mild jog to catch up with Otoha who, of course, is attempting to lose me."
    "Despite my desire to have sex with her teacher, though...there {i}is{/i} also the desire to find out more about what’s going on in that prodigious head of hers."
    "If she’s working herself to the bone...and coming within inches of asking {i}me{/i} for advice when she has plenty of other people to fall back on..."
    "I assume that things are either very bad or..."
    "Or I’m the only person who would be able to help her for some reason?..."
    "........."
    "......"
    "..."

    scene otohadarkness13
    with dissolve2

    "We make it to the sketchy basement to find that Niki is not yet here."
    "And while this does delay the amount of time before my penis will be inside of her, it gives me a solid opportunity to relate to Otoha instead."

    s "You know, I was a teenager once too."

    scene otohadarkness14
    with dissolve

    o "Woooooooow. You don’t say."

    "I have successfully related to Otoha. "
    "I will now press her for secrets."

    s "What did you try to tell me at the cafe the other day?"
    o "Stop having sex with people half your age."
    s "The other thing."
    o "You’re a bad influence."
    s "Keep going. You’ll get there eventually."
    o "Rin has nice boobs."
    s "Not what I was aiming for but we can stick with that topic. That sounds good."
    o "Don’t take this the wrong way, but I think it would be best for both of us if we didn’t use our time alone in this sketchy basement to talk about boobs."
    s "And you say {i}I’m{/i} the lame one."

    scene otohadarkness15
    with dissolve

    o "It’s weird Niki’s not here yet. She’s never late."
    s "She probably got called into work or something. I’ll give you your lessons today. Open your mouth."

    scene otohadarkness16
    with dissolve

    o "Please never tell me to open my mouth again."
    s "I can’t teach those who are unwilling to learn."
    o "I’m going to sit on the couch and wait for my actual teacher now. Not the guy she’s boning."
    s "I will join you on that couch because it will bring us closer together."
    o "On second thought, maybe I’ll stand."
    s "Me too. Standing sounds better."
    o "..."
    s "..."

    scene otohadarkness17
    with dissolve

    o "Ugh...I hate it when you come here."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadarkness18
    with dissolve2

    "An awkward [[yet expected] silence fills the room as both of us struggle to think up any conversation topics and are probably still thinking about Rin’s boobs."
    "What I want to do is probe Otoha more about whatever this thing she needs help with is but, unfortunately, it’s starting to seem like time will be the only thing to squeeze that out of her."
    "That’s fine, though. I doubt whatever it is is eating her alive and she seems way better today than she did the last time I saw her."
    "In fact, the only notable change at all is the reduced amount of red highlights in her hair. "
    "Why she didn’t remove them all, I don’t know. Because to me, it feels like she’s just caught in the middle of a transition like this-"
    "Like she got halfway through changing up her look and hesitated. "
    "I’m probably overthinking it. That happens sometimes. "
    "I just hope that, whenever the rest of her hypothetical transition ensues, it’s painless."
    "It would be a real shame if she had to take {i}more{/i} out on someone just trying to help."

    s "Otoha."
    o "Don’t do it."
    s "I was wondering-"
    o "I’m telling you, Sensei. Don’t do it. "
    s "What was that thing you-"

    scene otohadarkness19
    with dissolve

    o "Listen, man. I should have never said anything in the first place. I was sleep deprived when I said I needed your help and..."
    o "I thought more about it and you’re definitely the {i}last{/i} person who’d be able to help me. Talking to you would only make things worse."
    s "So things are bad?"

    scene otohadarkness20
    with dissolve

    o "..."
    o "Yeah."
    s "Do you think they’re going to get better on their own?"
    o "I don’t know..."
    o "I just wish people would let me breathe sometimes."
    o "I feel like my entire life right now is as Otoha of “Otoha & Rin.” And that’s {i}fine.{/i} Rin’s a great girl. Really great. I just want to feel more like...an individual sometimes. Not half of something bigger."
    s "That does sound kind of suffocating. I have no idea how you want me to help you, though."
    o "That’s not what I needed help with. It’s just kind of...how things got started, I guess."
    o "But ever since they {i}did{/i}, I-"

    stop music
    play sound "imscared.mp3"
    scene otohadarkness21
    with hpunch

    o "KYAH!"
    s "..."
    o "..."
    s "Kyah?"

    scene otohadarkness22
    with dissolve

    o "Leave me alone! That was super loud! I’m allowed to get scared!"
    s "Sounded like something might have exploded."
    o "Like...are we under attack? Is this space war stuff? Are we finally going to die?"
    s "Probably just one of those transformer things outside. I’m sure the power will come back on as soon as it’s repaired."
    s "On the bright side, pun not intended, we’ve still got Niki’s collection of tacky neon anime sign things. "

    scene otohadarkness23
    with dissolve

    o "I can barely see anything, though. "
    o "Can’t you, like...be a man and go fix it yourself or something?"
    s "Way to perpetuate gender roles by assuming I just know how to fix electrical stuff, Otoha. I have no idea how to do something like that."
    o "I don’t like the dark...it creeps me out."
    s "Yeah. I can tell on account of you willingly touching me. That has never happened before."
    s "It’s also incredibly out of character and very adorable. Which is why I am enjoying this thoroughly right now."

    scene otohadarkness24
    with dissolve

    o "Well, congratulations on taking pleasure in my suffering! I really appreciate that!"
    s "Any time. And if you’d like to come closer, I will welcome you with open arms."
    o "Can’t you just go and take a look at the breaker thingy? There’s one on the other side of the room. "

    scene otohadarkness25
    with dissolve

    s "Where it’s even darker than it is over here? And with zero knowledge of what I’d even have to look {i}for?{/i} This isn’t a good plan."
    o "Do you have a better one?"
    s "Yeah. We sit here and wait for the power to come back on."
    o "What if it doesn’t?"
    s "Then this is where we die."

    scene otohadarkness26
    with dissolve

    o "I don’t want to die with you! I don’t even like you that much!"
    s "Wow, okay. Why don’t you let go, then?"
    o "Because if I let go, you’ll disappear and I’ll be all alone and I will cry and scream and it will suck! Go try and do electrical stuff. If you die, at least it will be as a hero."
    s "And what are you going to do while I cross the abyss that is this basement, Otoha? Aren’t you afraid I’ll disappear?"
    o "Not if...I come with you? I can just hold your sleeve like this. That works, right?"
    s "That is a horrible idea."
    o "Why?"
    s "Because the only way that scenario could end would be with one of us tripping and then the other one falling on top in what would become a cliche anime-style almost-kiss moment. "
    s "Then, to complicate things even further, the power would come back on as soon as that happens and Niki would walk in to find us still laying on the ground together."
    o "That is ridiculous. There’s no way that will happen."
    s "Otoha, I am positive that will happen. I have protagonist powers."
    o "No, you’re just a selfish wannabe loner who bangs teenagers. "
    s "Teenagers who like me for no discernible reason. Even you’re cozying up right now and we were at odds just a short while ago."
    o "I’m not “cozying up!” I’m scared! Go make the lights come back!"
    s "Okay. But I am telling you that there is literally only one way this scenario can possibly end."
    o "Whatever! Just go!"

    scene black
    with dissolve2

    s "Okay. But don’t say I didn’t-"
    o "Ahh!"

    play sound "tackle.mp3"
    scene otohadarkness27
    with hpunch

    o "Ngh..."
    s "See? Not even two seconds. I told you this would happen."

    scene otohadarkness28
    with dissolve

    o "My legs weren’t working! If I had known that before trying to get up, I would have just made you carry me!"
    s "How are you {i}that{/i} scared of the dark? You’re in high school. Grow up."

    scene otohadarkness29
    with dissolve

    o "At least if I grew up, you wouldn’t be attracted to me anymore!"
    s "Don’t argue, Otoha. It will lead to us making out. "
    o "No it won’t! Just because you got lucky with guessing {i}one{/i} thing doesn’t mean another is going to happen when-"

    play sound "imscared.mp3"
    scene otohadarkness30 with hpunch

    o "KYAH! WE REALLY ARE UNDER ATTACK!"
    s "Make that two things."
    ni "Otoha..."

    scene otohadarkness31
    with dissolve

    o "How is that even possible?! We would have heard you coming down the stairs!"
    ni "Would you like to explain to me why you’re on the floor with my ex-or-maybe-not-ex-boyfriend? And then, would you like to explain to me why it looks like you’re trying to take his pants off?"

    scene otohadarkness32
    with dissolve

    o "Okay, the falling part is one thing, but there’s no way this coincidence would get even worse than-"
    o "..."
    ni "I’m waiting..."

    scene otohadarkness33
    with dissolve

    o "Just kill me..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadarkness34
    with dissolve2
    play music "brighterdays.mp3"

    ni "So...let me get this straight."
    ni "The power went out...and you’re a fucking pussy...so you made a dude with no technical know-how waltz across a dark room to play with an electrical panel...and then you fell on him because, again, pussy."
    o "..."
    ni "..."
    o "Yes."
    ni "Otoha-"

    scene otohadarkness35
    with dissolve

    o "I...I know how it must look! And I...know that recent events may have also led you to believe that is the type of person I am! But this was totally different from that! This was an accident!"

    scene otohadarkness36
    with dissolve

    s "Recent events?"
    o "Nothing! Go wait outside!"
    s "Niki?"
    ni "No clue. I’ve already purged whatever Otoha is referring to from my memory. You’ll have to hear it from her."
    s "Otoha?"
    o "I..."
    o "Uhh..."

    scene otohadarkness37
    with dissolve

    o "Practice time?..."
    ni "..."
    o "..."
    ni "..."

    scene otohadarkness38
    with dissolve

    ni "Bad girl."
    o "Niki, wait! It really wasn’t like that!"
    ni "You keep your hands off of my man. Got it? You are here to {i}learn,{/i} not fornicate."
    ni "I know firsthand how hard it is to keep hormones in check at your age, which is why I am being so lenient with you. "
    ni "But if you touch him again, I will cut your fingers off. Rings and all."

    scene otohadarkness39
    with dissolve

    s "Not the rings. That’s where she gets her powers."
    ni "Akira..."

    scene otohadarkness40
    with dissolve

    o "Akira?..."
    s "Hah...great. Now Otoha has {i}another{/i} secret of mine while I still don’t have any of hers. Thanks, Niki."
    o "Your name is Akira?"
    ni "Why are you keeping your name a secret from your students?"
    o "Yeah, why are you keeping your name a secret from your students?"
    o "I'm not the only one who knows, am I?"
    s "That...is a good question. Let me get back to you on it."
    o "Your name..."
    o "Is kind of cool."

    scene otohadarkness41
    with dissolve

    s "You’re only saying that because you want to get in my pants."
    o "Aaaaand you ruined it."
    ni "Otoha. Practice is cancelled today. "

    scene otohadarkness42
    with dissolve

    o "What? Why? "
    ni "Because I have a sudden urge to remind your teacher that there is only one female in his life that he should be putting his hands on and that female is me."
    ni "Now scram or you will see something you may never forget."
    o "Niki-"

    scene otohadarkness43
    with dissolve

    ni "Mm~"
    o "Wha- seriously?! I’m still in the room!"
    s "Mm...Niki...I don’t..."

    scene otohadarkness44
    with dissolve

    ni "Mnch...shut the fuck up and kiss me..."
    o "..."
    s "But..."

    scene otohadarkness45
    with dissolve
    play sound "dooropen.mp3"

    ni "Mngh.....hmnn......mm~"
    s "..."

    "Welp, now that Otoha’s gone, I see no reason to not keep doing this."

    scene otohadarkness46
    with dissolve

    ni "Mnh! Mm...Akira......mmnh!"

    scene black
    with dissolve2
    play sound "zipper.mp3"

    ni "Lay down on the couch..."
    "........."
    "......"
    "..."

    scene otohadarkness47
    with dissolve
    play sound "phonebeep.wav"

    r "{i}Hello? Otoha? Is everything okay? I thought you’d be practicing right now.{/i}"
    o "Yeaaaaaah...about that. Practice is cancelled today and I suddenly don’t have anything to do."
    r "{i}What? What about Sensei? Weren’t you with him?{/i}"

    scene otohadarkness48
    with dissolve

    o "He is...currently having sex with my teacher."
    r "{i}Oh...{/i}"
    r "{i}Yeah, I guess that tracks.{/i}"
    r "{i}What are you gonna do, then? Go home? Come back to the cafe? I can go on break early if you want.{/i}"

    scene otohadarkness49
    with dissolve

    o "No, it’s fine. Don’t worry about it. I’ll just go home and take a nap or something."
    r "{i}Okay! I’ll get back to work then. Text me if you get bored or whatever.{/i}"
    o "I will."
    o "And...Rin?"
    r "{i}Yeah? What’s up?{/i}"
    o "..."
    r "{i}Otoha?{/i}"

    scene otohadarkness50
    with dissolve2

    o "I love you."

    scene black
    with dissolve2
    stop music fadeout 10.0

    $ renpy.end_replay()
    $ otohadate20 = True
    $ otoha_love += 1
    $ niki_lust += 1

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "{i}Niki’s lust has increased to [niki_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label otohaspring1:
    scene otohamaya1
    with dissolve2

    "A silent walk through a long corridor was exactly what Otoha Okakura needed after another exhausting day at school."
    "And while she was no stranger to hard work as she’d been working hard her whole life, she’d grown quite accustomed to her time under the wing of a predatory bird."
    "She awaited his return with less fervor than the others, as she felt her emotions came across better when reserved for the spaces between blue lines on white paper."
    "But there was fervor nonetheless. And she didn’t want to accept a future in which she’d need to hunt for her own scraps rather than feasting on the leftovers not consumed by her vulture."
    "That’s really all he was at the end of the day — a man who swooped down and plucked the meat off of teenage girls who failed to realize they’ve been dead all along."
    "But here {i}she{/i} was — brimming with half a life that felt more like a script and another half that felt like torn up shreds of paper strewn across the floor of a well-furnished living room."
    "How she wished for the chance and the time to tape them all together and recall what it was she wanted."
    "But as the sun poured in through the glass and played hell upon her irises, she focused more on the sound of her own footsteps than the beating of her heart."

    play music "insicknessandhealth.mp3"

    "Until something else caught her attention."

    scene otohamaya2
    with dissolve2

    o "..."

    "The bright sound of a violin bleeding into that long corridor executed the silence that brought her comfort moments ago and, instead, replaced it with an array of feelings she struggled to immediately comprehend."
    "So she listened closely. Music was her {i}thing,{/i} of course. And, as an artist herself, she felt more inclined to identify with abstract ideas rather than specific dialogues or pesky conversations."
    "Those were never strong suits of hers. But {i}this...{/i}"
    "This was something she could follow. "
    "Not just into the classroom, where she would ultimately move anyway- but on a plane somewhere between the one we know and the one we only {i}sort of{/i} know."
    "And, for the first time since her lips touched those she’d never claim again, her heart skipped a beat. "
    "In fact, it skipped {i}harder{/i} than it did that time before because, unlike then, {i}this{/i} was real."
    "This was a moment she’d stolen due to coincidence rather than calculation. Which made stealing it okay, she thought. So she listened for a little while longer."

    o "..."

    "Until just listening alone was not enough."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohamaya3
    with dissolve2

    "She needed to {i}see{/i} the girl. She wanted to observe the look on her face to get a better idea of what these sweet sounds meant."
    "Because, as bright as they were and as {i}warm{/i} as they made her heart, she could tell there was something else."
    "Complacency, perhaps? Loneliness? She wasn’t sure, as both of these things were things she never felt. "
    "But whatever it was, she wanted to know."
    "She wanted to reach out and touch the girl in a way unlike she’d touched any other before- though her experience with such a thing was admittedly limited."
    "This wasn’t sexual, though. But it probably {i}could{/i} be if the offer arose, as she was so currently entranced that she’d comply with any of the girl’s desires at the moment if it meant acquiring a taste of her world."
    "That was all she wanted — a taste. Of whatever this artist felt."
    "Because it was closer to {i}authentic{/i} than anything {i}she’d{/i} ever done before. And again, this was her {i}thing.{/i}"

    o "..."

    "She wasn’t sure how long she watched her for."
    "It could have been minutes...hours...days...but probably not {i}days{/i} because the bell would certainly have interrupted them. "
    "Right?"
    "Or was this one of those moments she’d heard about in movies — where time comes to a standstill and nothing exists outside of one singular moment."
    "She wished this would be like that."
    "The violinist, however-"
    "Did not."

    scene otohamaya4
    with dissolve2

    "She opened her eyes and looked out the window, but wore an expression so {i}normal{/i} that it worked in contrast to the sound of her instrument and racked Otoha’s mind."
    "{i}Does she feel anything at all?{/i}"
    "{i}Is this just some well-rehearsed classical piece she’d never heard before?{/i}"
    "{i}Or is it something she simply can not fathom yet?{/i}"
    "With so many feelings left unfelt and so many probable precious moments that had flown over her head during those late hours where she’d sit at her desk, she acknowledged this possibility."
    "She acknowledged how, unlike her, this girl had likely {i}seen{/i} things. {i}Done{/i} things. But {i}what{/i} things? And with {i}whom?{/i}"
    "And the fact that she’d been right there, just several desks down this whole time, was terrifying."
    "She thought, “If there’s been this much untapped beauty right in front of my face, just what else have I been missing out on?”"

    scene otohamaya5
    with dissolve2

    "But that’s the last thing she’s able to think before the girl with the violin notices {i}her.{/i}"

    stop music

    m "..."
    o "..."
    m "I apologize. "
    m "You’ve seen something rather inappropriate just now."
    o "{i}Inappropriate?...{/i}"
    o "Maya...that was beautiful."

    scene otohamaya6
    with dissolve

    m "It was muddy."
    o "{i}Muddy?{/i}"
    m "Confused, even. "
    m "I’m not sure what it was trying to say."
    o "I...I had no idea you even played the violin."
    m "That’s not much of a surprise to me. Neither one of us knows anything about the other. And why {i}would{/i} we? Why {i}should{/i} we?"
    m "After today, we’ll likely never speak again."
    m "You’ll go back to your friends and I’ll go back to mine. And we’ll both go back to feeling things that neither one of us will ever be able to understand."
    o "..."
    m "..."
    m "I’m sorry again. That was quite gloomy, wasn’t it?"
    o "Do you..."
    o "Do you want to talk?"

    scene otohamaya7
    with dissolve

    m "About what?"
    o "Anything. "
    o "There’s no club today, so I kind of just...came here to do what you’re doing."
    m "Oh, right. I forgot there was a light music club at all."
    m "I’m sorry for commandeering your room. There just wasn’t anywhere else that felt right. "
    o "Don’t worry about it. In fact, I’m...kind of happy you did. Whatever you were just playing was...way more moving than anything else that’s come out of this room so far."
    m "I take it that means your band isn’t very good."
    o "Do you want to sit?"
    m "..."

    scene otohamaya8
    with dissolve

    m "I suppose it wouldn’t hurt."
    m "If we’re never going to talk again, we may as well make {i}this{/i} meeting somewhat special."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohamaya9
    with dissolve2
    play music "encounter.mp3"

    o "So...how long have you been playing?"
    m "I...can’t really remember."
    o "Is it just violin? Can you play piano as well?"
    m "Not very well. "
    o "Do you want me to teach you?"
    m "I appreciate the offer, but I’m fine with the way things are now."
    o "Just figured I’d ask. "
    m "..."
    o "You know...I don’t think it’s weird. You coming here to play, I mean."
    m "Why do you think that {i}I{/i} would think that you think that is weird?"
    o "Just the...being alone thing. Like, I know what it’s like to feel like you have to hide your music. I kick Nodoka out of the room all the time for that. And I was always quiet about it back at home."
    o "Some stuff’s just kind of personal, you know?"
    m "I think you might be misunderstanding why I’m here. "
    m "I have no qualms with anyone hearing me play the violin. If anything, it’s probably the safest way for me to talk about my feelings."
    m "The problem is that I {i}have{/i} them. And now I’ve inadvertently dragged an innocent bystander into them after being unable to control whatever impulses made me do this."

    scene otohamaya10
    with dissolve

    o "Why wouldn’t it be okay for you to feel? "
    m "It’s less that it’s “not okay” and more that I just hate it. But I suppose feelings are an inevitable part of this curse called {i}youth.{/i}"

    scene otohamaya11
    with dissolve

    o "You’ve got {i}that{/i} right. "
    o "I often find myself wishing that this shit would just be over with already so I can get on with my life {i}without{/i} all the necessary drama that comes with just being a teenager."
    m "And here I thought you were all feeding off of such a thing."

    scene otohamaya12
    with dissolve

    o "I’m sure that’s how it looked...what with the Rin situation and all of that. But I was never really cut out for that to begin with."
    o "In fact, I don’t think I’m cut out for {i}any{/i} of this. And any time I encounter one of those quintessential {i}teen{/i} moments, I can’t help but think, “Wow. I’m really excited for this to end.”"
    o "It’s kind of weird, you know? Like, on one hand, I want to {i}enjoy{/i} my youth. But, on the other, it’s all so fucking frustrating."
    o "Nothing’s as fun as I want it to be and I still find those moments where I’m just...alone writing music to be the most enjoyable of all. "
    o "But then I do that and I feel like I’m wasting away my high school years and it becomes this confusing, shitty paradox I don’t know how to escape from."

    scene otohamaya13
    with dissolve

    o "But you helped me with that just now. So thanks."
    o "Listening to you play was the first time in a while that I’ve felt any peace."

    scene otohamaya14
    with dissolve

    m "It’s the opposite for me, unfortunately."
    o "What do you mean?"
    m "I mean that I feel no peace at all right now. And, without divulging any of the specifics to you, this is the most conflicted I’ve felt in a long time."
    o "Is that what you were trying to get across with the violin?"
    m "Maybe. I’m not really sure. "
    m "I think I was just hoping a certain someone would hear it. But of course that would have been too cliché to actually happen and now I’ve gone and wasted the big, emotional moment on another heroine instead."
    o "Well, your sacrifice won’t go unappreciated. I kind of needed something like this. I just didn’t really expect you of all people to be at the forefront of that."

    scene otohamaya15
    with dissolve

    m "And I can’t say having {i}you{/i} walk in on me was anywhere on my bingo card."
    o "You must not be very good at bingo, then. I come here more often than anyone, you know. "
    m "I’ll keep that in mind the next time I have an overwhelming urge to play the violin."
    o "I’ll be sure to come by even {i}more{/i} often then. I wouldn’t want to miss another chance to hear you."
    m "Interesting..."
    o "Interesting?"
    m "It's just, if I didn’t know any better...I’d think you were {i}flirting{/i} with me right now, Otoha."
    o "Hey, nobody said two heroines can’t end up together. Maybe your big, emotional moment wasn’t wasted at all?"
    m "Ahh, I see. So apparently I {i}don’t{/i} know any better and you {i}are{/i} flirting with me right now. "
    o "Only if it’s working."
    m "If there wasn’t already a vice grip latched onto my heart, it might be. I {i}do{/i} like the cool, asshole type after all."

    scene otohamaya16
    with dissolve

    o "Alas! ’Twas not a fateful encounter at all, but one more fleeting moment of anguish in this curse called youth..."

    scene otohamaya17
    with dissolve

    o "I get it, though. I also have a thing for the cool, asshole type. But I imagine I’m chasing after a different one than you."

    scene otohamaya18
    with dissolve

    m "I find that hard to believe given the general disposition of literally every single girl in our class."
    m "But also, don’t read into that statement because this is kind of a part of me that I’m supposed to keep secret and I’m only giving you a glimpse of it because you happen to be here when I’m most vulnerable."
    o "I get it. And don’t worry, I’m not going to say anything. "
    o "You’ve got your work cut out for you, though. Especially given {i}recent developments.{/i}"

    scene otohamaya19
    with dissolve

    m "It’s everyone else who has their work cut out for them. I have a natural advantage given the fact that I’m the cutest and the smartest. "
    o "And great at violin too. Anyone would be lucky to have you."
    m "If only {i}anyone{/i} would suffice. Vice grips are a terrible thing."
    o "They really are...aren’t they?"

    scene otohamaya20
    with dissolve

    m "So, if {i}you’re{/i} not chasing after the same person as everyone else...who {i}are{/i} you chasing after? It’s not still Rin, is it? Because I certainly wouldn’t describe her as “cool.” {i}Or{/i} an asshole, really."
    o "Secret, right?"
    m "Of course. Everything we say and do in this room will be erased once we leave today."
    o "Does that mean we can make out?"

    scene otohamaya21
    with dissolve

    m "So it’s been {i}me{/i} all along. Poor Rin. But I suppose she deserves this for getting my character killed."
    o "Hahah...no, it’s not you."

    scene otohamaya22
    with dissolve

    o "It’s some jerk with pink hair."

    scene otohamaya23
    with dissolve

    m "{i}Noriko?{/i} Seriously? You’re a trillion leagues above her."
    o "Try older."
    m "Older? But that’s-"

    scene otohamaya24
    with dissolve

    m "Wait...you don’t mean..."
    o "Kumon-mi’s very own sweetheart. The idol who holds dominion over the hearts of all. "
    o "Spoiler alert. She’s kind of an asshole in real life."
    m "You have the actual worst taste in women {i}ever{/i} and I am kind of offended that you want to make out with me now."
    o "I take it you’re not a fan of hers then?"

    scene otohamaya25
    with dissolve

    m "I sometimes have dreams where I strap her to a rocket and launch it into the sun."
    o "That seems...a little excessive. But the heart wants what the heart wants, I guess."
    o "Point is, though...I get where you’re coming from."

    scene otohamaya26
    with dissolve

    o "And in a roundabout way, this means we can sort of root for one another."
    o "Just your goal seems a lot more obtainable than mine. "

    scene otohamaya27
    with dissolve

    m "It’s those damn vice grips again. I’m telling you, they ruin everything. "
    o "Mhm..."
    o "But in the event that all else fails-"
    m "If you ask me to make out again, I’m pretty sure it will count as sexual harassment and I will be forced to report this to the authorities. "
    o "Doesn’t mean I can’t {i}think{/i} it."

    scene otohamaya28
    with dissolve

    m "Okay. For {i}your{/i} sake, I think it’s about time we leave. I don’t want you doing anything {i}stupid.{/i}"
    o "But then I’ll have to go back to not knowing you."

    scene otohamaya29
    with dissolve

    m "It’s for the best, I assure you. I’m not the type of person you should want to associate with."
    o "Oh yeah? And why’s that?"

    scene black
    with dissolve2
    stop music fadeout 10.0

    m "Because it’ll make everyone else seem so much worse."

    "{i}The day ends.{/i}"
    "{i}But at least something good happened along the way.{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ otohaspring1 = True

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label otohaspring2:
    scene noonsky
    with dissolve2
    play music "icantseeher.mp3"

    "There’s someone I want to see."
    "Someone I’ve been mostly neglecting since waking up from my makeshift coma."
    "It’s someone who always manages to take the pain away, replacing it with an ever-growing darkness that, strangely enough, makes me feel like I’m home."
    "Maybe it’s because the darkness she fills me with blends in nicely with the kind I’ve created myself but, regardless-"
    "There’s someone I want to see."

    stop music
    scene buddybug

    "There’s someone I want to see."
    "She’s someone who should not exist, but she does anyway."
    "She’s someone who eats rumors and turns their tiny bones to special lines we can make ladders with."
    "She sleeps in a box in a place beneath the subway and masturbates furiously to the sounds a stepson makes."
    "I want to hold her hand and see if I can find any pink or black hairs. The smell of propane. That dim, auburn glow."
    "We met one another inside of a beaker."
    "She spat in my mouth and made me eat last week’s supper."
    "I often think about ripping her hair out and stapling it onto the scalp of someone who needs it more."
    "Can you hear this, Kyoko?"
    "Your daughter is a nightmare."
    "She has my eyes."

    scene noonsky
    play music "icantseeher.mp3"

    "Ignore that."
    "Anyway, there’s someone I want to see."
    "Her name is Nodoka Nagasawa, and I’m going to fuck her mouth until her teeth fall out."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohanodokalibrary1
    with dissolve2

    "When I make it to the library, I find that Nodoka is accompanied by someone rather strange today."
    "Well...not strange in the sense that these two aren’t often seen together. But the sense where Otoha doesn’t typically- ah, fuck it. You know what I mean."
    "Either way, both of them are here — which means there will be no mouth-fucking unless Otoha’s looking to broaden her horizons so wide that I can sort of just sneak my way into her sex-life."
    "That would be neat. She has nice legs. They both do."

    s "You guys have nice legs."

    scene otohanodokalibrary2
    with dissolve

    o "..."
    no "..."

    scene otohanodokalibrary1
    with dissolve

    o "Thanks."
    s "No problem, Otoha. Just here to provide some encouragement so you two can study more effectively."

    scene otohanodokalibrary3
    with dissolve

    o "Wait, yeah. What {i}are{/i} you doing here? "
    s "I just told you."
    o "No, I mean like...I thought you were trying to stay away from this place? Does this mean you’re coming back to school now?"
    s "Absolutely not. I’m here to see Nodoka."

    scene otohanodokalibrary4
    with dissolve

    no "I’m Nodoka."
    s "Are you free right now?"
    no "That depends. Is this your way of subtly asking me to have sex with you without directly revealing the nature of our extremely passionate relationship to my roommate?"
    s "Your words, not mine."
    o "Not to mention your roommate already knows about your “extremely passionate relationship.” I heard it {i}loud{/i} and clear, remember?"

    scene otohanodokalibrary5
    with dissolve

    no "Oh, right. I took quite a beating that night and must only {i}now{/i} be experiencing the adverse effects of having my head pressed up against the wall for so long."
    o "No. I think you’re just being a douche."

    scene otohanodokalibrary6
    with dissolve

    no "Perhaps. I think the more likely explanation, though, is that I’m just a bit preoccupied at the moment. My mind can only handle so much at once, you know."
    s "That’s news to me."
    o "Nodoka’s been caught up in some weird research loop lately. And I’m pretty sure it’s about you, so if you could just spill your heart out to her or whatever, it might save all of us some time and trouble."
    no "I’m afraid there’s nothing Akira could tell me that would aid in my research, but yes. That is a thing I am currently doing. Which means I must regretfully deny your invitation to “Pound Town.”"
    s "I can be quick."
    o "Wow. You’re really just shameless now, aren’t you?"
    no "If it’s quick, I’m sure Otoha can handle it. She might ask you to call her “Onee-chan,” though."

    scene otohanodokalibrary7
    with dissolve

    o "Hah..."
    s "Alright, Otoha. Let’s do this. We don’t have to look at each other if you don’t want to."

    scene otohanodokalibrary8
    with dissolve

    o "Come on, man. I’ve actually kind of missed you. Please don’t go making things weird just a few seconds into our reunion."
    s "Hey, get mad at Nodoka, not me. She’s the one who volunteered you. And she works here, so I was under the impression her word was law."
    o "{i}Akira,{/i} I know your brain’s all scrambled and shit right now, but I’d like to remind you that this is a library, not a brothel."
    s "A library is just a brothel for knowledge."

    scene otohanodokalibrary9
    with dissolve

    no "He raises a fair point."
    o "No he doesn’t! And even if he did, wouldn’t that imply I can just, like...{i}educate{/i} him?!"
    no "Stop yelling in the knowledge brothel. It’s against the rules."
    o "Can you put a leash on your pet, please?"
    s "That’s the whole reason I came here and now it’s starting to sound like I’m going to have to fuck a book."

    scene otohanodokalibrary10
    with dissolve

    no "Well, fuck whatever you want so long as it’s not me. I have work to do, and it’s imperative that I finish this section before I lose my train of thought."
    o "I have work to do {i}too{/i}, you know? I’ve been working on this song non-stop and it’s still all...not good and shit."
    no "Then perhaps you can find inspiration in the arms of an older man? That’s what Tchaikovsky would have done."
    s "I don’t know how to play piano, but I can assure you I am still very good with my-"

    scene otohanodokalibrary11
    with dissolve

    o "Do not, under any circumstance, finish that sentence. "
    o "If you’re okay with just {i}hanging out and talking,{/i} I’ll take a break with you for a little while. And, before you ask, no. “Hanging out and talking” is not Zoomer slang for hooking up."
    s "You actually want to hang out with me? "
    o "When has what I want to do ever mattered to you before? Your favorite pastime is barging into my room and pretending to watch porn while I’m on the phone with my parents."
    s "True. But don’t let my infallible comedic senses fool you, Otoha. I’m just a step or two away from breaking into a million pieces right now and things could get pretty messy {i}really{/i} quickly."
    no "Then please go elsewhere {i}now{/i} as I do not want little bits of Akira all over my notebook. That is what my {i}face{/i} is for."
    o "Come on, Sensei. Let’s let the genius do her {i}research.{/i}"

    scene black
    with dissolve2

    "Otoha gets up from the table and closes her notebook, throwing it on top of a stack of about ten others as I’m reminded that Nodoka isn’t the only imperfect perfectionist around."
    "As we make our way to the opposite end of the library, I can’t help but worry that the man I’ve become will make the wrong impression on Otoha and taint the sapling of a relationship we’ve formed so far."

    play sound "static.mp3"
    scene yuminightfrog1 with flash
    scene black with flash
    stop sound

    "But then I remember Yumi."
    "And I remember that she and I barely have a relationship at all."
    "And that this broken part of me somehow brought her {i}closer.{/i}"
    "Has that been the key all along?"
    "Do these stupid, unknowing teenagers eat up vulnerability the same way {i}I{/i} do?"
    "Are they trying to take advantage of {i}me{/i} now?"
    "Does Otoha want my COCK? "
    "Does she want my BIG, THROBBING COCK?"

    play sound "static.mp3"
    scene otohanodokalibrary12 with flash
    stop sound

    "No. "
    "No she doesn’t."
    "And I need to calm down."

    o "..."

    "I need to remember where I am and {i}who{/i} I am."
    "What pieces I have left and the ones I need to find."
    "And none of them are inside of her."

    o "So...how are you holding up?"

    "But I suppose if they are, I can just pull them out of her stomach once she’s sleeping."

    scene otohanodokalibrary13
    with dissolve

    s "I almost jumped off a bridge the other day. That was fun."

    scene otohanodokalibrary14
    with dissolve

    o "You...{i}what?{/i}"
    s "I don’t know if I should say it again based on that expression."
    o "Are you a fucking idiot? Why would you do that?"
    s "I don’t know. It kind of just happened. "
    s "I’m pretty much just running on auto-pilot now. I don’t really have anything left to lose."
    o "You have fucking {i}tons{/i} to lose, man. I know a handful of girls who’d straight up just crumble if anything bad ever happened to you. Just think of Niki."
    s "I’ve been trying not to."
    o "{i}Why?{/i} She loves you."
    s "{i}That’s{/i} why."

    scene otohanodokalibrary15
    with dissolve

    o "..."
    s "Niki’s too good to be true. "
    s "And not only do I not deserve her, but she {i}confuses{/i} me. Or maybe I just don’t actually want to feel better. I don’t know."
    s "That’s why I’m here to see Nodoka. I {i}get{/i} her."
    o "Nobody {i}gets{/i} Nodoka, Sensei."
    s "I just mean I “get” what our relationship is. "
    s "I can hide inside of her when what I’m feeling becomes too much to bear. "
    o "Can you not do that with Niki?"
    s "I can. But what Nodoka takes away is different. "
    s "Niki walks away with {i}love{/i} when I’m done with her. All Nodoka gets is a chance to feel human for a little while. Or maybe, like...research or something. I don’t know."
    s "But whatever it is, it’s not love. Just a little escapism. And I think the only reason it works for the two of us is because we’re not great at feeling things the way other people are."

    scene otohanodokalibrary16
    with dissolve

    o "Well, call me crazy, but you seem more relatable than ever right now. And that’s {i}because{/i} you’re feeling all this shit."
    s "I don’t want to be relatable. I just want to be complacent."
    s "I don’t need happiness or love or anything like that — just a moment or two of silence and a cute girl I can bury myself in when porn won’t do the trick anymore."
    o "I can’t...really tell if you’re just messing with me right now or if all of this is actually legit."
    s "What’s confusing you?"
    o "Well, the fact that you’ve never been this open for one."
    s "Like I said, I have nothing to lose now."
    o "Yeah, but second thing is just...how fucking dumb all of this is."
    s "Dumb?"

    scene otohanodokalibrary17
    with dissolve

    o "{i}Just a moment or two of silence and a cute girl I can bury myself in when porn won’t do the trick anymore...{/i}"
    o "No offense, but you sound like some twelve-year old edgelord who just got rejected by a girl for the first time ever."
    s "..."

    scene otohanodokalibrary18
    with dissolve

    o "Which...is fine. If that’s how you really feel. But I don’t think it is. I think you’re just...having trouble articulating what’s actually going on or...or something like that."
    s "I will admit that it’s been very long since I’ve attempted to properly {i}articulate{/i} my feelings."

    scene otohanodokalibrary19
    with dissolve

    o "Then try that instead of wandering all the way across town to have sex with a teenager! "
    o "You can make yourself feel better from the comfort of your own home {i}without{/i} having to worry about accidentally plaguing the world with another Nodoka-spawn."
    s "Two Nodokas sounds horrible in terms of daily life. Sexually, though-"
    o "I don’t need to hear about that part! Just stop being a downer and pull yourself together, dude. I’m sure you’ll find whatever it is that you apparently lost and, if you don’t-"

    scene otohanodokalibrary20
    with dissolve

    o "There are a million other things out there that’ll fill the void once you stop crying."
    s "And if there aren’t?"
    o "Then you’re probably holding yourself back on purpose."
    s "..."
    o "You good now, little bro?"
    s "I forget how much I like you sometimes."
    o "You’d remember if I tried harder. I’m pretty good at minding my own business when I’m not destroying relationships and whatnot."
    s "You haven’t destroyed ours yet. I’m still hesitant to call you {i}Onee-chan,{/i} though, given that you’re only half my age."
    o "Yeah, definitely...don’t do that. The “little bro” thing was just a joke. Nodoka’s only fucking around when she says all that stuff about me."
    s "I don’t know. Nodoka has accurately predicted the sexual behavior of at least one other person that I did not see coming, so I’m inclined to believe her intuition when it comes to this stuff."
    o "Please don’t."

    scene otohanodokalibrary21
    with dissolve

    s "If only I had experience being sexually attracted to people younger than me. Maybe then I would be able to understand your outlook on this."
    o "Really don’t."

    scene otohanodokalibrary22
    with fade

    s "You seem a little persistent, Otoha. Why?"
    o "I just don’t want you to get distracted from the topic at hand. This is a conversation where I lend you a shoulder and you get some tears on it or something. It has nothing to do with me."
    s "Thankfully, your wise words have led to an immediate full recovery on my end. Thank you for saving my life, Otoha. Now, it is time to discuss your sexual preferences."
    o "Why do you always have to ruin literally everything?"
    s "Isn’t that what little brothers do?"

    scene otohanodokalibrary23
    with dissolve

    o "I mean...{i}yeah.{/i} But you’re like six feet tall and-"
    s "You’re blushing now. This really is a thing for you, huh?"

    scene otohanodokalibrary24
    with dissolve

    o "No! It’s...I..."
    o "I like somebody! A girl! Well...woman. So I clearly don’t-"
    s "Niki, right?"
    o "No, it’s-"

    scene otohanodokalibrary25
    with dissolve

    o "Wait, how do you know that? What’d she tell you? How much do you know?"
    s "Well, now I know that {i}she{/i} knows. So that’s new information to me."

    scene otohanodokalibrary26
    with dissolve

    o "Oh, god damn it!"
    s "It was your terrible beach confession speech that was very clearly not written for me that clued me in. "
    s "And also the fact that she had a very abrupt non-answer on the phone when I told her about you and Rin breaking up."

    scene otohanodokalibrary27
    with dissolve

    o "But that speech was bullet-proof. How did you {i}ever{/i} see through it?"
    s "You wanted me to see through it even earlier, didn’t you?"
    o "I may have been in desperate need of some advice in regard to whether or not this would ever be a plausible scenario for me. "

    scene otohanodokalibrary28
    with dissolve

    o "But...I get now that it’s not. And that you probably wouldn’t give me any advice on how to hook up with your girlfriend anyway."

    scene otohanodokalibrary29
    with dissolve

    o "Or, shall I say- {i}one{/i} of your girlfriends. "
    s "..."
    o "This would be a good time to blackmail you if I was one of the bad guys."
    s "Do you want to both be bad guys for a second while I propose a trade?"

    scene otohanodokalibrary30
    with dissolve

    o "You have my attention."
    s "I think we both have something that the other person wants."
    o "You give me Niki, I give you Nodoka? Deal. Take her. As far away as you can."
    s "I give you a {i}picture{/i} of Niki..."
    s "And you-"

    scene otohanodokalibrary31
    with dissolve

    o "And I give you one of Rin!"
    s "Bingo."
    o "Wow! This is really fucked up! I’m in!"
    s "And I’m..."

    menu:
        "Just kidding":
            s "...not being serious. Sorry, Otoha."

            scene otohanodokalibrary32
            with dissolve

            o "Bruh..."
            o "You’re really gonna do me like that?"
            s "Yeah. I’ve screwed over enough people already. And even if I don’t have anything to lose, I don’t think I’m ready to stoop low enough to trade nudes of the girls I know like they’re currency."

            scene otohanodokalibrary33
            with dissolve

            o "Are you {i}sure?{/i} I’ve got some pretty {i}spicy{/i} ones, Akira. No one ever has to knooooow."
            s "Wow. You really want these, don’t you?"
            o "My imagination can only take me so far."
            s "Aren’t you a writer?"

            scene otohanodokalibrary34
            with dissolve

            o "For the sake of this conversation, let’s say...no. I am not."
            s "Let’s just...keep what’s in our phones to ourselves for now and...forget I ever made this proposition. Niki would kill me for even joking about it."
            o "And Rin-"

            scene otohanodokalibrary35
            with dissolve

            o "Actually, I’m not sure how Rin would feel. She might be into it. But I was admittedly never in-tune with her feelings, soooo...maybe not."
            s "I say we just seize this rare opportunity to be good people and do that for once. Even if it leads to not experiencing things we would very much like to experience."
            o "I agree. Reluctantly, of course. But I agree."

            scene black
            with dissolve2
            stop music fadeout 10.0

            o "And I thank you for your time, but I must now go back to...not being a writer."
            s "And I must now go home and jerk off to nudes of a famous idol that you won’t ever see naked."
            o "You are the worst brother I’ve ever had."

            "I exit the library and..."
            "I feel a little better."
            "Today was okay."

            $ renpy.end_replay()
            $ otohaspring2 = True
            $ otoha_love += 1
            $ nikinudetrade = False

            "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
            "........."
            "......"
            "..."

            jump nightch4

        "Sending it now":
            s "Sending it right now."

            scene otohanodokalibrary36
            with dissolve

            o "Holy shit. This is fucked up even for you."
            s "Hey, you agreed to go along with it. You’re no better than I am."
            s "I still don't have your number th-"
            o "81262289632!"

            $ otohanumber = True
            play sound "winner.mp3"
            "{i}You have obtained Otoha Okakura's phone number!{/i}"

            s "Well, that was way too easy."
            o "You're {i}positive{/i} this is cool?"
            s "We're in too deep now, aren't we? You gave me your phone number and everything. There's no turning back."
            o "Yeah, but {i}I’m{/i} getting a picture of a famous idol I have no shot with and you’re getting a picture of some random high school girl who you’re probably going to fuck one day anyway."
            s "Fair point. Send me {i}your{/i} nudes as well."
            o "Ew, no. You can have Rin and that’s it. My body is a temple and only one person is allowed to enter it at this moment in time."
            s "I bet that number would go up if I were twenty years younger."
            o "And I’m going to pretend you didn’t just say that. Are we doing this or not?"
            s "We’re doing this. But no one can ever know. "
            o "Got it."
            s "Seriously. I’m trusting you. Niki’s career could be in serious jeopardy if this gets into the wrong hands."
            o "I will not tell you what I am going to do with this picture, but I can confirm that it will definitely not be “destroying her career.”"
            s "Promise?"
            o "Yes. And if I go back on my word, I’ll let you do anything you want to me for ten whole minutes. That’s how serious I am."
            s "That’s barely enough time to do anything."

            scene otohanodokalibrary37
            with dissolve

            o "How much time do you need?! "
            s "Twenty or I walk."

            scene otohanodokalibrary38
            with dissolve

            o "Deal."
            s "Pleasure doing business with you, Otoha."
            o "You as well, Akira. Now, please excuse me while I go somewhere private."

            scene black
            with dissolve2
            stop music fadeout 10.0

            "Otoha runs off to...probably the bathroom while Nodoka remains blissfully unaware about all that’s happening behind her."
            "Is this a terrible, disgusting idea? Probably. And it jeopardizes not one, but {i}two{/i} of my closest relationships. "
            "Like I said earlier, though...I have nothing to lose anymore."
            "So as I scroll through the pictures in my phone (That I had to restore from my computer after Ami deleted all of them), I sigh to myself, knowing that I’m a terrible person."
            "But that’s nothing new. "
            "I’ve known it all along."

            play sound "phonebeep.wav"

            "And the sudden beep of my phone is just the newest symbol of that."
            "I’m sorry, Rin."
            "I’m sorry, Niki."

            $ renpy.end_replay()

            play sound "phonebeep.wav"

            $ nikinudetrade = True

            "{i}You’ve received a picture message from Otoha Okakura!{/i}"

            $ otohaspring2 = True
            $ otoha_love += 1

            "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
            "........."
            "......"
            "..."

            jump nightch4

label otohaspring3:
    scene otohamcds1
    with dissolve2
    play music "fallishere.mp3"

    s "..."
    o "..."
    s "..."
    o "..."
    s "..."
    o "..."
    s "So, are we going to talk about what just happened?"
    o "Nope."
    s "I feel like we should probably talk about what just happened."
    o "Nope."
    s "I also feel like you probably should have washed your hands sometime between leaving the basement and now."

    scene otohamcds2
    with dissolve

    o "..."
    s "Just saying."

    scene otohamcds3
    with dissolve

    o "Okay. I think it’s my turn to be suicidal."
    s "Wait, stop. That’s the only thing I have going for me right now."

    scene otohamcds4
    with dissolve

    o "The {i}only{/i} thing? You just plowed the heart of Kumon-mi into unconsciousness and you think your defining characteristic is how much you currently want to jump off of a bridge?"
    s "I think the sex part’s become so normal in my everyday life that I often just omit it."
    o "I see now why you’ve become such a depressing mess over the last few months. I can only imagine how miserable {i}I{/i} would be if I got to bone Niki Nakayama whenever I wanted. Sounds like hell."

    if nikinudetrade == True:
        s "Hey, at least you’ve got a picture now. That was more than you had before."
    else:
        s "I won’t rest until I have sexual intercourse with everyone you know. This is my mission."

    o "The hell were you two getting it on down {i}there{/i} for anyway? Do you have any idea what you’ve done? I’m never going to be able to take another lesson without having Vietnam-style flashbacks now."
    s "Hey, you could have left whenever you wanted. Don’t blame me for your voyeuristic compulsion to spy on couples clearly engaging in a very private act with one another."

    scene otohamcds5
    with dissolve

    o "That-"

    scene otohamcds6
    with dissolve

    o "Well..."

    scene otohamcds7
    with dissolve

    o "...Shut up."
    s "Good one."
    o "Well, what would {i}you{/i} have done in my shoes? I might never get another opportunity to see Niki in a position like that for as long as I live. I wasn’t just gonna {i}walk away.{/i}"
    s "Yeah, it makes a lot more sense to just masturbate in front of your teacher instead."

    scene otohamcds8
    with dissolve

    o "{i}Former{/i} teacher. I never would have done that if you were still employed and pretending to be responsible for my education."
    s "I mean, I {i}am{/i} still employed if you want to get technical about this."
    o "Nope. Doesn’t count. What I did back there was no different than just watching porn and I hereby reclaim any innocence I may have lost in doing so. Thank you."
    s "So, when you were fingering yourself, were you thinking more about {i}her{/i} or-"

    scene otohamcds9
    with hpunch

    o "Obviously her! If it was {i}you{/i} I was interested in, I would have invited you along for Rin’s maiden voyage to climax city. "
    s "You should have. You’ve now witnessed my powers firsthand and must accept that you’ve missed out on something potentially very special by {i}not{/i} inviting me."
    o "Sorry, Akira. I was too busy listening to you pork my psycho roommate and wound up boarding the ship alone. But I’ll give you a call the next time I’m coerced into a private room with a {i}different{/i} classmate."
    s "I see now that we share a common goal in collecting the bodies of our mutual acquaintances."

    scene otohamcds10
    with dissolve

    o "{i}Hah...{/i}"
    s "You shouldn’t be doing that. You still haven’t washed your hands."
    o "I used my other hand for that. And it’s not my goal to {i}collect bodies.{/i} If that’s what I cared about, I wouldn’t have rejected ten million people at my last school."
    s "Oh, right. Sometimes I forget how popular you were back then since the only person you ever hang out with {i}now{/i} is Nodoka."

    scene otohamcds11
    with dissolve

    o "That’s not true. {i}You{/i} exist. Even if I don’t really want you to."
    s "That’s fair. I don’t really want me to exist either. But I {i}do{/i} hope you know that I’m going to hold this over your head for the rest of your life."
    o "Yeah, I figured as much. But I wouldn’t get {i}too{/i} comfortable with that since I’m still acutely aware that you’re screwing multiple girls and could use that to sabotage all of your relationships."
    s "Joke’s on you, I’ll probably wind up sabotaging them on my own before you even have a chance to."

    scene otohamcds12
    with dissolve

    o "Yeah, that’s why it isn’t worth it. That and the fact that I’m kind of starting to get attached to you now for whatever reason."
    s "Thanks, Otoha. I feel like this would be a really cute moment for us if I hadn’t watched you discreetly finger yourself twenty minutes ago."
    o "Silly me for thinking you’d keep your eyes on, oh- I don’t know, the girl you were having sex with?"
    s "It’s like you said about Niki, I might never get to see you in another position like that for as long as I live."
    o "Yeah, but you haven’t had a crush on me for years like I have with her."
    s "What if I had, though? But I’m just really bad at expressing myself and could never figure out how to tell you that {i}you’re{/i} the one I want out of everyone in Kumon-mi?"

    scene otohamcds13
    with dissolve

    o "Uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh no. "
    s "Man, I really hope you let down those millions of girls a lot gentler than that."
    o "And I really hope that we can figure out a way to put this behind us and file it in whatever drawer we’re keeping the hotel sex-fest in."
    s "Unfortunately for you, I keep all of my secrets in a single drawer that doesn’t even lock. And it’s only a matter of time until someone else finds out whether we want them to or not."
    o "Can you, maybe...I don’t know, {i}lock it{/i} then? Because I don’t really think I want anyone else finding out I touched myself in front of two of my teachers. "
    s "I know a solution to this."
    o "You definitely don’t."
    s "You have to complete the trifecta and touch yourself in front of Imani next. That way, all of your teachers will know and we’ll all be on equal footing. Your problem will be solved."

    scene otohamcds14
    with dissolve

    o "Sure. Just let me know when you fuck her and I’ll be right there to do that."
    s "..."
    o "Oh, {i}wait a minute.{/i} Imani is one of the few people you’re {i}not{/i} having sex with, isn’t she?"
    s "Why do you know that?"

    scene otohamcds15
    with dissolve

    o "Probably because her situation isn’t all that different from mine."
    o "And also the fact that your disappearance made her start acting super weird and cranky all the time."
    o "And also the part where I overheard her tell Miss Watabe that she, and I quote — “Needs to get laid like, yesterday.”"
    s "Is this just what you do now? Go around spying on people?"

    scene otohamcds16
    with dissolve

    o "No, but it’s seriously starting to feel like that. I keep walking in on shit I’m not supposed to see or hear."
    o "Like, just the other day, I-"

    play sound "static.mp3"
    scene otohamcds17 with flash
    stop sound

    o "And like, I’m not {i}that{/i} much younger, am I? Like, I’m in high school. She doesn’t have to make me feel like some kind of {i}kid.{/i}"
    s "Uhh...what just happened?"

    scene otohamcds18
    with dissolve

    o "Huh? What do you mean?"
    s "Weren’t we just outside? Did I black out again?"
    o "Uhh...I don’t think so? You’ve seemed pretty normal to me. But we’ve been in here for like fifteen minutes, dude."
    s "Wasn’t your tie just black as well?"

    scene otohamcds19
    with dissolve

    o "Oh, yeah. It’s a special color-changing tie. Now, you won’t ever have to ask about it again."
    s "Works for me. "

    "Well, it appears that I have, once again, lost a chunk of the day to whatever higher power decided to extract it from me this time."
    "And while that’s fine and all considering it brings me one step closer to pulling the covers over my head again, I’d like for them to stop screwing around and just take me back to nighttime already."
    "Oh but, going forward, they can leave in the parts where girls show up and touch themselves to me as well. I’d like if I can still experience those."
    "Everything else, though? Fuck it. Like, not literally. Okay, maybe a little literally. But not like literally a little literally. You know? Fuck it. Literally. Just not because I can’t even control when I get hard anymore."
    "It either happens or it doesn’t. And when it does, it’s violent. But when it doesn’t, it’s nothing. It’s like, numb. It’s like, I can’t even describe it. It’s just numb. It’s either violent or it’s numb. Sex. You know?"

    s "So...what were we talking about just now?"

    scene otohamcds20
    with dissolve

    o "Oh, I was just ranting about Niki again. Which I’m sure is annoying as shit, so you can just tell me to knock it off and I will."
    s "Otoha, if you like Niki as much as you obviously do, why did you ever agree to date Rin in the first place?"
    s "You said this has been going on for years, didn’t you? What’s the point of going into a relationship you’re not fully on board with?"
    o "I don’t know. Why did you go into a relationship with Niki while you were already boning Chika? Hearts and brains are stupid. They don’t always make sense."
    s "So it’s...sexually motivated then?"

    scene otohamcds21
    with dissolve

    o "No...it wasn’t like that. It was more, like...curiosity, I guess? And...submission, maybe?"
    o "Like, I don’t want to say I was just {i}settling{/i} for Rin because anything with Niki seemed like such a long shot. But that’s also...{i}kind of{/i} what it was?"
    o "But not in the sense where it, like...makes {i}her{/i} look bad. Because she was great. And I {i}do{/i} like her, just...not {i}like{/i} that."
    o "It was more like...trying to bring myself back to reality or...whatever. Shooting for something achievable for once instead of always keeping my eyes on the clouds like I was raised to do."

    scene otohamcds22
    with dissolve

    o "But reality is just so fucking {i}boring,{/i} man. Like, my very limited experience with dating is no different from anything you’d see in some shitty Netflix movie. It was just drama and crying and making out."
    s "Well, what {i}do{/i} you want?"

    scene otohamcds23
    with dissolve

    o "Something {i}real.{/i} Something...I don’t know...{i}exciting.{/i} But not {i}too{/i} exciting because then it becomes {i}exhausting.{/i}  "
    o "I just want it to, like...{i}feel{/i} right. But nothing {i}ever{/i} feels right. With {i}anyone.{/i}"

    scene otohamcds24
    with dissolve

    o "I don’t know. Maybe this whole dating thing just isn’t for me. That’s kind of what I figured from the get-go. But then Niki went and activated all of my hormones and now I just feel {i}weird.{/i}"
    o "It’s just, like...there are so many songs about true love and...{i}falling{/i} in love...{i}being{/i} in love...the things that {i}love{/i} can make you do...and I, like...{i}can’t{/i} write those. And that {i}sucks.{/i}"
    o "There’s this whole aspect of life and music that I {i}want{/i} to understand. But every time I {i}try{/i} to understand it, I want to rip my fucking hair out. "
    o "But Niki gets that. And despite what the Internet might say about idol culture and shit, she’s a {i}real{/i} artist. She writes her own music...lyrics...and it’s all so {i}personal,{/i} but...{i}accessible{/i} too."
    s "And you figure she’d be able to show you more of that world?"

    scene otohamcds25
    with dissolve

    o "I {i}think{/i} so? But I also can’t look at her without wanting her to push me to the ground and have her way with me. So that’s a world I want to be a part of too, I guess."
    s "Yeah, I like that world a little more."

    scene otohamcds26
    with dissolve

    o "Do you really, though? Because, and this is older-sister Otoha speaking now, what if you’re only {i}this{/i} fucked up {i}because{/i} that’s the world you’re living in?"
    o "What if you’re like me in that regard? Aware that there’s this extra dimension that could make your life so much better, and you’re just...infinitely stumbling while trying to make it there?"
    s "I think that’s just what living is."
    o "This isn’t living. What {i}we’re{/i} doing isn’t living. Look at Niki. Look at Rin. They {i}know{/i} who they are. And yeah, they’ve got their problems as well, but do you think {i}they’re{/i} worried about this shit?"
    o "Hell no. They’ve got their own values and...people they care about and...there’s no fear of what lies {i}beyond{/i} any invisible forcefield since they’ve already passed through them all. "
    o "Can we really say we’re {i}living{/i} before we have the faintest idea what our lives even {i}are?{/i}"
    s "I know what {i}my{/i} life is, Otoha. You-"

    scene otohamcds27
    with dissolve

    o "No! That’s- ugh! See, this is why you’re so annoying. "
    o "It’s that, like...fatalist mindset of yours. That “I’ve fallen too far and can’t possibly climb back up” bullshit that people who {i}give up{/i} cling to."
    o "It’d be so fucking easy for me to do the same god damn thing. To just be, like “{i}Oh, I’m a bad person. I guess I’m just going to suck forever,{/i}” and then live out the rest of my life as a loser-douche hybrid."

    scene otohamcds28
    with dissolve

    o "But I want to be more than that. And {i}you{/i} should want to be more than that. "
    o "Because if we don’t get our shit together, we’re {i}both{/i} going to wind up masturbating in front of people we care about. And not in a good way!"
    s "That took a weird turn."
    o "I’m trying!"
    s "Did you wash your hands?"
    o "Yes!"
    s "Otoha..."
    o "Akira."
    s "I really do like you, you know."

    scene otohamcds29
    with dissolve

    o "No matter how nicely you ask, I will not let you watch me again. And no, I am not sorry."
    s "That’s not what I’m getting at. I just appreciate that you can still find the time to talk to me like this despite having no clue what’s going on in your own life."

    scene otohamcds30
    with dissolve

    o "You don’t have to thank me. Just...reciprocate it. Because that’s all I’ve ever wanted from you."

    scene otohamcds31
    with dissolve

    o "I don’t feel comfortable talking to my parents about shit like this. And it’s not like I can vent to Niki about how badly I want her to tackle me. "
    o "So for the most part, I’ve always just figured shit out on my own. But I’ve always wanted someone to, like...{i}be there.{/i} You know? Whether it be trading advice or...just {i}listening.{/i}"
    o "And a teacher made the most sense. Like...I don’t have any siblings...and everyone {i}my{/i} age just wants to fuck me."

    scene otohamcds32
    with dissolve

    o "Which, to be fair, you do as well. But I’m willing to overlook that if it means being able to come to you when I need something. "
    s "T-"
    o "Something that {i}isn’t{/i} sex."
    s "You’ve had other teachers before, Otoha. Were none of them up to your {i}standards?{/i} Or are you just {i}settling{/i} for me now like you did with Rin?"

    scene otohamcds33
    with dissolve

    o "I’ve never had a teacher like {i}you{/i} before. And that’s both a good and a bad thing."
    o "It’s {i}bad{/i} because, like I just mentioned, you want to fuck me. {i}And{/i} everyone else. And I’m sure I don’t have to tell you why that is wrong."
    o "But it’s {i}good{/i} because you’re the first person who isn’t constantly reminding me that I can do better. "
    o "And yeah, that might be sort of counterintuitive to the whole “being a teacher” thing. But at the end of the day, your job is to {i}inspire.{/i} And being reminded of how talented I am isn’t inspiring. It’s {i}tiring.{/i}"
    o "You look at me like a person, not a student. So maybe what I wanted wasn’t a teacher at all."
    o "It was a friend."
    s "..."
    o "..."
    s "That was really fucking lame, Otoha."

    scene otohamcds34
    with dissolve

    o "Yeah, I’m cringing pretty hard right now, not gonna lie."
    s "No, I just mean you missed another good opportunity to call me your brother."
    o "That was on purpose. I didn’t want you to make things sexual again."
    s "A-hah. So you admit you’re what the kids would call a “brocon.”"

    scene otohamcds35
    with dissolve

    o "I don’t like that you know that word."
    s "Good. Because, while I’ll always be here for you to {i}trade advice{/i} with, I’m going to make it even more of a point to make your life a living hell from now on."
    o "Meaning what, exactly?"

    scene black
    with dissolve2

    s "Meaning we’ll figure this shit out together."
    o "That...what does that have to do with the “living hell” part? What are you going to do to me?"
    s "I’m not sure. But it looks like we’ll have to find out next time since the scene has already faded to black."
    o "Wha- what scene?! We’re in fucking McDonald’s! Stop being weird!"
    s "{i}At the time, we had no idea...but that conversation would change everything. It was truly the beginning...of something wonderful.{/i}"
    o "Stop narrating our conversation! And eat your fucking French fries!"

    "Otoha begins throwing food at my head. "
    "And I open up some more space in my decaying heart for her."

    stop music fadeout 10.0
    $ renpy.end_replay()
    $ otohaspring3 = True
    $ otoha_love +=1

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label christmasotoha1:
    scene otohapresent1
    with dissolve2
    play music "tsukiokamanor.mp3"

    c "I am so full of love...and so full of cum."
    s "Yeah. Well, I hope you’re very proud of yourself for probably ruining Kirin’s night."

    scene otohapresent2
    with dissolve

    c "Hey. It takes two to tango, Sensei. Unless you’re me alone in my bed, thinking about you. Then you can tango alone. But you need to wait until Chinami is asleep or she’ll ask questions."
    s "How long were you even watching us for? And...from where?"
    c "I followed you. "

    scene otohapresent3
    with dissolve

    s "{i}Why?{/i}"
    c "Love, of course! I didn’t want Kirin luring you into a dark room and taking advantage of you. It wasn’t until {i}after{/i} that I learned you {i}love{/i} her too. Which made it okay!"

    scene otohapresent4
    with dissolve

    c "Why do you think she left, though? She’s been joking about getting into {i}my{/i} pants lately too. I figured she’d be super excited to watch {i}me{/i} watch {i}her.{/i}"
    s "Well, how would {i}you{/i} feel if people started showing up to watch {i}us?{/i} And one of them just happened to be someone claiming to be the cuckquean ringleader of my harem?"
    c "I’d just go along with it and let them think whatever they want to think because I know I’m the only one who matters in the end and I love dick."
    s "Can you please just...leave me alone next time? Or find a way to ask {i}me{/i} without potentially traumatizing another girl who’s just trying to have a moment?"

    scene otohapresent5
    with dissolve

    c "So let them think {i}they’re{/i} winning. Got it! I’ll be more careful next time. "

    scene otohapresent6
    with dissolve

    c "For now, I’ll just be happy we got to have a lot of hot Christmas sex. Apparently, I’ve seemed kind of crazy today- and I imagine that will now begin to fade since I am low on energy."
    s "I know you, so I know damn well you are assuredly {i}not{/i} low on energy after only three orgasms."

    scene otohapresent7
    with dissolve

    c "You’re right! Let’s go back and do it again!"
    o "Do what again?"

    play sound "static.mp3"
    scene otohapresent8 with flash
    stop sound

    o "What are you guys talking about?"
    c "Sensei, do you “love” Otoha too?"
    s "Of course not."
    o "Wow. Okay, man. Merry Christmas to you too."
    c "I’ll just keep my mouth shut and continue to hate her then."

    scene otohapresent9
    with dissolve

    o "Wouldn’t it make more sense for you to just...{i}stop{/i} hating me since I barely even talk to Rin anymore and we’re in a club together?"
    c "Yeah. But nothing makes sense anymore, so you’re just going to have to deal with it."
    no "Merry Christmas, Sensei."

    play sound "static.mp3"
    scene okayitsgametimeagain1 with flash
    scene otohapresent9 with flash
    stop sound

    s "..."
    no "Is something wrong? You look like you’ve just seen a ghost."
    s "Is it weird for me to want to hug you really hard right now?"

    scene otohapresent10
    with dissolve

    no "Not at all. I was actually just picturing what a passionate night in your arms would feel like. So please, have at this body like a father claiming his daughter’s innocence in the dead of night."
    c "What the heck, Sensei? You didn’t even try to hug me once we finished {i}doing all of those chores together{/i} a few minutes ago."
    o "What a believable story. Is this really the place to be {i}doing chores,{/i} though?"
    s "Chika, since you’re not effectively and immediately coming up with a coping mechanism this time, just tell yourself it’s because the two of you are wearing the same outfit and I...mistook her for you or something."

    scene otohapresent11
    with dissolve

    c "Hey, yeah! Who do you think you are showing up in that? I’m supposed to be the hot Santa girl. You’re not allowed to wear that unless I ask you to like I did with Rin."
    no "Oh, this? I merely walked into the first discount costume store I could find and grabbed something I believed would be appealing to Daddy dearest. I sincerely apologize if you employed the same strategy."
    c "That-"

    scene otohapresent12
    with dissolve

    c "I don’t really...have the..."
    s "I like the costume, Chika. "

    scene otohapresent13
    with dissolve

    c "Aah! Thank you, Sensei! I-"
    s "Now go head back to the Christmas party before me so {i}no one gets the wrong idea.{/i} Okay?"

    scene otohapresent14
    with dissolve

    c "Done. I read you loud and clear, Sensei. Always thinking ahead of the game. This is why you’re my {i}best friend.{/i}"
    s "Mhm. I’ll see you later, Chika. Have fun at the party. And tell Kirin to come talk to me if you see her."
    c "I’ll think about it."

    scene otohapresent15
    with dissolve

    "Chika leaves."
    "I never really wanted her to show up in the first place, to be honest."

    o "You know it’s frowned upon to screw those who aren’t mentally stable enough to consent, right?"
    s "I do a lot of things that are frowned upon, Otoha."
    no "Something, something, laws. Something, something, who cares? None of {i}us{/i} do. That’s for sure."
    s "Are you two just showing up now? "
    o "Yeah. I had to stop somewhere first. And Nodoka was weirdly insistent on getting a slutty Christmas outfit for whatever reason."

    scene otohapresent16
    with dissolve

    no "Do I {i}need{/i} a reason to want to look my best for a reunion with my beloved? "
    o "So, Sensei is your “beloved” now?"
    s "She could be talking about Jesus. He is technically supposed to be everywhere and today is kind of his unofficial birthday."
    no "He’s right, you know. And I can think of no better pair to tie me up and spitroast me until I can no longer see or breathe."
    s "That sounds fun, but I’m pretty sure it would be a sin."

    scene otohapresent17
    with dissolve

    no "The greatest joys in life typically are."
    o "Should I just leave so you can claim {i}her{/i} next? Because I feel like that’s the direction we’re headed in right now and I’m not sure I want to stick around to see it."
    no "There’s no need, Otoha. I was actually just leaving."

    scene otohapresent18
    with dissolve

    o "What? We literally just got here."
    no "And my job is {i}already{/i} done. I’m so good at this."
    o "Good at what? You’ve been-"
    s "Nodoka."

    scene otohapresent19
    with dissolve2

    no "Yes, Father?"
    s "..."
    no "..."
    s "Are you okay?"

    scene otohapresent20
    with dissolve2

    no "...heh."
    no "Never better."

    play sound "footsteps.mp3"
    scene black
    with dissolve2

    "Nodoka leaves and suddenly it’s just Otoha and me."
    "She briefly flashes me a look that says something along the lines of, “What the fuck was that about?” And, you know what? I wish I had an answer for her."
    "Maybe it’s because I’ve been talking to monks. Maybe having that space between Nodoka’s legs as a failsafe to hide in if things get {i}really{/i} bad is what’s making me thankful for her right now."
    "Maybe it’s a whole slew of things — memories from lives unlived or dreams of days that shan’t ever come. "
    "Or maybe it’s just love for {i}her{/i} too. "
    "Who even knows at this point?"
    "That dam I call restraint is wearing thin...and each mask on the wall is cracked or chipped."
    "Something about the way she’s shaped just lets her slip right through."

    play sound "static.mp3"
    scene otohapresent21 with flash
    stop sound

    "I should probably be thinking about Otoha right now, though, since she’s the one standing before me."

    o "You and her make a weird pair."
    s "Which one? Chika or Nodoka?"
    o "Yes."
    s "Fair enough. I make a weird pair with basically everyone."
    o "Probably because you’re like six times everyone else’s age."
    s "I can always count on you to make me feel even older than I actually am, Otoha. Thank you."
    o "Don’t sweat it, man. Can you use all those years of wisdom and your allegedly superior intellect to figure out what the hell’s going on with her, though? "
    s "Who accused me of having superior intellect? I need to have a word with them."
    o "You don’t know then?"
    s "About what? Nodoka? Sorry, but no. I haven’t spent any actual time with her in months. But if she’s being weird, I think it’s probably safe to assume that she’s just...you know. Literally being weird."

    scene otohapresent22
    with dissolve

    o "Yeah...maybe. I guess trying to pull any logic out of that black box of a mind is kind of pointless. If you, me, or Futaba have no idea what’s going on, it’s probably just safe to say no one ever will."
    s "Probably. But hey, if you want to try and psychoanalyze {i}me{/i} instead, have at it. You’ve got your work cut out for you today."

    scene otohapresent23
    with dissolve

    o "And I don’t on a normal day?"
    s "On normal days, I’m not hallucinating chipmunks."
    o "And...that is a thing you’re doing today?"
    s "Sure is. Any guesses as to what’s wrong with me this time?"

    scene otohapresent24
    with dissolve

    o "It’s clearly a sign that you want to stop sleeping with teenage girls and start doing the right thing. And also that you want to buy me a new amp. And whatever else I want. Maybe dinner if the buffet here isn’t good?"
    s "No {i}actual{/i} guesses then?"
    o "Man, you {i}really{/i} want to keep sleeping with all those teenagers then, huh? Not going to heed the advice of your holiday guardian angel, Otoha Okakura?"
    s "You’re a terrible guardian angel if you only show up on holidays. Especially since my tragedy rate seems to skyrocket whenever they roll around."
    o "I do what I can."
    s "You historically do not."

    scene otohapresent25
    with dissolve

    o "These chipmunks — what are their names?"
    s "Malvin, Diamond, and Spork."
    o "Spork?"
    s "A glutton, he is."
    o "You have a weird fucking mind, Sensei. Especially since I know at this point that you’re almost definitely {i}not{/i} lying to me right now."
    s "I feel like...having Ami around would at least kind of keep me grounded. But she’s-"
    o "Out with Niki. I know. I stopped getting invited after trying to kiss her in a locker room."
    s "You can kiss me instead if you want. I promise I won’t tell anyone."
    o "Smooth. That line will go over really well in jail one day."
    s "I take it that’s a no then?"
    o "It’s definitely a no."

    scene otohapresent26
    with dissolve

    o "Here’s a consolation prize, though."
    s "A present? Where were you even keeping-"
    o "Don’t worry about it. Just take it."

    scene otohapresent27
    with dissolve

    "I swipe the gift from Otoha’s hands. It feels light. So light, in fact, that I’m doubtful there’s anything in it at all."

    s "Can I open it now?"
    o "You actually can’t open it at all."
    s "It’s just the wrapping paper, isn’t it?"
    o "No. I just mean that isn’t actually for you. It’s for Niki. I want you to give it to her for me since I’m not seeing her until after the holidays are over."
    s "Ahh, okay. So you just {i}lied{/i} to me about this being a consolation prize then."
    o "Not technically. For a second, I bet you were thinking something like, “Wow! Otoha must really care about me if she bought me a present. What a kind and thoughtful girl she is.” "
    o "That moment of bliss was a prize on its own, wasn’t it?"
    s "Yeah. Only for a moment, though. Now, I just think you’re evil."
    o "I’m evil for not buying you a present? Or for leading you into {i}believing{/i} I got you a present just to send your dreams crashing back down to earth?"
    s "The latter."

    scene otohapresent26
    with dissolve

    o "Well, I guess it’s time to {i}really{/i} rock your world then. Because {i}this{/i} one is for you, Sensei."
    s "..."
    o "Go on. Take it. I promise I’m not fucking with you this time."
    s "I can really have that?"
    o "Did my five-second prank really scar you so badly that you’re afraid to even take a gift out of my hands now?"

    scene otohapresent27
    with dissolve

    "I swipe {i}this{/i} gift from Otoha too, and it feels exponentially heavier than the last one."

    s "..."
    o "Something wrong?"
    s "No, I just...didn’t get {i}you{/i} anything."
    o "I guess I’m just a better person than you, then."
    s "All I have to repay you with is my body."
    o "Why don’t we just call it even? "

    "I tear open the gift."

    scene otohapresent28
    with dissolve

    "Oh my fucking god."

    s "Is this some kind of inside joke or something?"
    o "Do you not like it? "
    s "Imani just got me this exact same pocket knife. What kind of man do you people think I am?"
    o "One who’s really hard to shop for. Noriko actually helped me pick that out. So if you don’t like it, take it up with her."
    s "That clever bitch is using me as an excuse for free pocket knives, isn’t she?"
    o "She {i}is{/i} basically your little sister, isn’t she? Seems like a very “little sister” thing to do. Now, can you stop pointing that at me?"

    scene otohapresent29
    with dissolve

    s "Yeah, sorry. Thank you anyway, Otoha. You’re one of the last people I expected to get me anything. So-"
    o "Why?"
    s "Why what?"
    o "Why am I one of the last people you expected to get you something?"
    s "Because...you’re arguably less interested in sleeping with me than basically everyone else I know? Apart from a full-blown lesbian, that is."
    o "So I can’t buy you a present?"
    s "It’s not that. I just-"
    o "Sensei, if I can offer you a piece of advice that isn’t just “stop fucking teenagers,” can I say that...thinking about things in that way is just {i}really{/i} fucking sad? Even for you."

    scene otohapresent30
    with dissolve

    o "Correlating ulterior motives like whether or not someone wants to screw you to whether or not they care enough to buy you a present is a major fucking bummer, dude."
    o "I get that everyone and their mother, quite literally at times, is throwing themselves at you. But just because it’s what you’re used to doesn’t mean it’s what’s {i}normal.{/i}"
    o "I bought you a gift because I had money and I was thinking about you. And because you’re my friend. And because I thought it might make you feel good or whatever. "
    o "I’m not asking for anything in return either. I just...you know. "
    o "You’ve changed my life. "

    scene otohapresent31
    with dissolve

    o "Mostly in bad ways. But still. If that sort of impact doesn’t earn you a present, I don’t know what does."
    s "I’ll get you something too. "
    o "Fine. Just don’t get Noriko to help you pick something out or she’s just going to wind up with {i}another{/i} present."
    s "Well, what {i}do{/i} you want? How much do those amp things cost?"
    o "Way more than that knife. You don’t have to worry about it, though. Just come hang out with me sometime. That’ll suffice, I guess."
    s "You’re actually asking {i}me{/i} to hang out? You’re not just going to begrudgingly let me in when I show up at your dorm room unannounced?"
    o "Again with the “Otoha doesn’t actually like me” crap. I do. I really do."

    scene otohapresent32
    with dissolve

    o "And honestly, I’ve...felt kind of shitty lately. Maybe putting up with your bullshit will help distract me from all that."
    s "Well, I can certainly relate there. What kind of “shitty” are we talking about, though? As your “friend,” I feel as if I am obligated to ask."
    o "General loneliness maybe? "
    o "Feeling shitty about myself? "
    o "Feeling stuck?"

    scene otohapresent33
    with dissolve

    o "The kind of stuff having a little brother around might help fix."
    s "And what better person to pick for a little brother than a man in his thirties who is also technically still your teacher on paper?"
    o "Options are limited in Kumon-mi nowadays. I’ll take what I can get."
    s "And if I start using you as an excuse to trick people into buying {i}me{/i} things?"
    o "Honestly?..."
    o "Some days, I think I’d kill for something like that."
    s "Well, you’re in luck. Because I just happen to have a matching pair of pocket knives that we can cut this city into pieces with."
    o "Works for me. Can we wait until Christmas is over, though? I want to see how Niki reacts to my gift."
    s "Oh, sure. I got so caught up in self-deprecation and murder that I forgot you even got her something. "
    s "Still trying to win her over?"
    o "Maybe."

    stop music fadeout 10.0
    scene black
    with dissolve2

    o "Maybe not."

    "Otoha peels herself off of a column that probably costs more than my house and heads for the door."
    "It quickly becomes apparent she has no idea where she’s going, though. So she winds up downloading the Tsukioka Manor navigation app while I-"
    "I...try to wrap my head around the act of caring for someone."
    "I know I can do that. I know I’ve {i}done{/i} that. Look at Osako. Look at Imani (at first — not so much anymore)."
    "I’ve proven to myself I can think of them in contexts that don’t require my penis."
    "I just wonder how much longer it will take to do the same when it comes to me."
    "We make our way back to the party together, mostly in silence."
    "My fingers curl around the handle of a blade I never asked for."
    "But one I wanted nonetheless."

    $ renpy.end_replay()
    $ christmasotoha1 = True
    $ otoha_love += 1

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmastsukasa1

label otohaspring4:
    play sound "knock.mp3"

    "I knock on Otoha’s door and wait for her to answer."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "But I get tired of waiting after approximately half a second and decide to just let myself in since it’s probably the only chance I’ll ever get to see her without her clothes on."

    scene otohasreallyhotdude1
    with dissolve2

    "Damn. She isn’t naked."

    o "Um...hi?"
    s "Hey."
    o "..."
    s "..."
    o "Can I...help you?"
    s "Yes, actually. If I go back outside, can you get undressed really quickly so I can walk in on you changing?"
    o "Sure."
    s "Yeah, I didn’t think s- what?"
    o "Go for it. I’ll give you thirty seconds."

    scene black
    play sound "doorslam.mp3"

    "One, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, that’s enough."

    play sound "doorslam.mp3"
    scene otohasreallyhotdude1
    with hpunch

    s "Thank you for-"
    o "You really thought I was gonna do it, huh?"
    s "Rin would have done it. In fact, I wouldn’t have even had to {i}ask{/i} her."
    o "I think that would just literally be walking in on someone while they’re getting changed."
    s "That’s correct. But she’d get over it in like five seconds and I know this for a fact because it has already happened."
    o "Well, yeah. Rin wants to fuck you."
    s "And you don’t?"
    o "Not really."
    s "Not even a little?"
    o "Okay, maybe a little. But in that quintessential teenage sort of way where I just kind of want to fuck everything."
    s "That never goes away."
    o "I think it does for most people. You’re just special."
    s "Thank you, Otoha."
    o "Special doesn’t always mean “good.” Also, why did you even knock if you were just going to come in?"
    s "Obviously because of the changing thing. I decided that was important after the fact. Are you telling me the knock ruined my chances?"

    scene otohasreallyhotdude2
    with dissolve

    o "What? No. I came home right after school and have been wearing these for like five hours now. If you want to catch me getting changed, you’ll need to be way earlier next time."
    s "Noted. I’ll be waiting."
    o "Hey, this whole hangout session isn’t just going to be about me and the state of undress you want me in, is it? Because that’s not what I had in mind when I asked you to come over on Christmas."
    s "Well, what {i}did{/i} you have in mind? Because it sounds a lot like you’re trying to seduce me based on how much you’re bringing up getting dressed."

    scene otohasreallyhotdude3
    with dissolve

    o "But {i}you’re{/i} the one who fucking-"

    scene otohasreallyhotdude4
    with dissolve

    o "Ugh. What’s even the point? {i}I’m sorry for trying to seduce you, Sensei. Please see past these impure impulses and have a normal conversation with me.{/i}"
    s "Otoha, you’re really hot."
    o "Or don’t."
    s "I didn’t mean that in a creepy way."

    scene otohasreallyhotdude5
    with dissolve

    o "There’s no {i}non-{/i}creepy way to say that when you’re in your thirties and I’m-"
    s "Special too? You sure are, Otoha."

    scene otohasreallyhotdude6
    with dissolve

    o "Just out of curiosity, does shielding yourself from the truth make it easier to pretend you’re a good guy? Or nah."
    s "Nah. So anyway, are we going to make out now?"
    o "Depends."
    s "If you say something like, “on whether or not I force you to,” I’m going to be sad."
    o "No. It depends on whether or not you gave Niki my present like I asked you to."
    s "Present?"
    o "You motherfucker."
    s "Hey, if you’re going to call me names, please try and use ones that don’t cut so deep. That’s a sensitive topic, Otoha."
    o "Know what else is a sensitive topic, Sensei? My incessant pursuit of something I will never have. "
    s "I get it. That’s like me and being happy."
    o "That is extremely sad. "
    s "I know. That’s the whole point."
    o "Bed?"
    s "Yes. And I know you’re just asking me to sit. But for the record, I {i}am{/i} going to imagine you’re inviting me to do something else."
    o "I’m well aware. I’ve gotten used to that risk and tie it to essentially everything I ever say to you now."

    scene black
    with dissolve2

    "Otoha and I make our way across the room, but the trip is so short that I don’t really have any time to think about anything other than her ass and oh look, we’re here now."

    play sound "static.mp3"
    scene otohasreallyhotdude7 with flash
    stop sound

    o "So — why do you hate me?"
    s "Can I be like everyone else and just blame it on hormones or something?"
    o "That wouldn’t be a thing everyone would be blaming everything on if you actually hung out with people your own age."
    s "True. I guess we can just say I’m...lovably forgetful then?"
    o "Sensei, that present was really important. You didn’t, like...lose it. Did you?"
    s "No...I’m pretty sure it’s in my room somewhere. Which means it’s well within Niki’s reach. I just haven’t handed it over yet."
    s "She saw the pocket knife, though. Both of them. She was very confused."
    o "I really don’t care how she felt about your matching knives. I just want to be able to contact her without feeling weird as hell anymore."
    s "And you think your present is going to fix that? You tried to make out with her."

    play sound "static.mp3"
    scene otohasreallyhotdude8 with flash
    stop sound

    o "I did {i}not{/i} try to make out with her! It was an {i}innocent{/i} kiss! Even {i}if{/i} I wanted to shove her down and make her cry out my name in a fit of ecstasy."
    s "Yeah, what’s more innocent than sexually fantasizing about someone while forcing yourself on them?"

    scene otohasreallyhotdude9
    with dissolve

    o "There was no force involved! It was a misunderstanding, okay?! I thought she was telling me to go for it! Which is a thing I might {i}not{/i} have thought if I wasn’t so used to adults who want to fuck me! Thanks for that!"
    s "Hey, yeah. How come you’re totally into the idea of boning Niki but {i}I{/i} am an ancient dinosaur in your book?"

    scene otohasreallyhotdude10
    with dissolve

    o "In my defense, everyone thinks she’s almost like a decade younger than she actually is. But even so, she possesses a youthful vigor that you have forgone in exchange for monk-related hallucinations and weird glasses."
    s "Wait, what’s weird about my glasses?"
    o "Present. When give?"
    s "Give soon. Why glasses?"
    o "Why anything? World big. We small."
    s "I’ll give it to her the next time I see her. Which, presumably, will be tonight since she is addicted to my penis and sleeps in my bed."
    o "Okay, well can you maybe {i}not{/i} put your penis in her tonight so she can actually process my gift?"
    s "Otoha, if you were in my shoes, do you {i}really{/i} think you’d be able to just {i}not{/i} put your penis inside of that girl?"

    play sound "static.mp3"
    scene otohasreallyhotdude11
    with flash
    stop sound

    o "Oh, absolutely not. I wouldn’t even let her breathe. But that’s probably because {i}I{/i} like her more than you."
    s "That’s a bold claim. "
    o "Is it though? Because you’ve got like every opportunity in the world to just live a perfect life with her. Yet you’re {i}here{/i} trying to fuck a girl who’s still in high school."
    s "Can I not live a perfect life with Niki while still fucking high school girls?"

    scene otohasreallyhotdude12
    with dissolve

    o "No! Obviously, no! How stupid are you?!"
    s "Relax. I already know I’m a fucking moron. You don’t need to remind me."

    scene otohasreallyhotdude13
    with dissolve

    s "It’s just...complicated, okay? "
    s "Niki absolutely {i}should{/i} be the one I fully devote myself to. She’s not only perfect for me, but she’s {i}earned{/i} it by being at my side for as long as I can remember and...helping me remember who I even {i}am.{/i}"
    s "There’s just...I don’t know. There’s something different about her when I compare her to everyone else that I can’t quite put my finger on. "
    s "And I feel like if I {i}were{/i} to devote myself to her, if I’m even capable of doing such a thing, all it would do is damn her to a life of uncertain mediocrity and...having to clean up after some hopeless douchebag."
    o "You’re not a {i}hopeless{/i} douchebag, Sensei. You’re just a regular douchebag."
    s "Thanks, Otoha. That’s the nicest thing you’ve ever said to me."
    o "Look at me."

    play sound "static.mp3"
    scene otohasreallyhotdude14 with flash
    stop sound

    s "Fine..."
    o "Up here."

    play sound "static.mp3"
    scene otohasreallyhotdude15 with flash
    stop sound

    s "All I want is to be free."
    o "Have you stopped to think that maybe you only feel that way about her because you are {i}actually{/i} in love with her?"
    s "Of course. But then I have to take into account the millions of horrible things I’ve done {i}while{/i} feeling that way about Niki and it really waters down the whole point of {i}actually{/i} being “in love.”"
    s "If I was {i}actually{/i} in love with her, don’t you think I’d just...{i}not{/i} do all of those horrible things?"
    o "Not if you’re a regular douchebag, no."

    scene otohasreallyhotdude16
    with dissolve

    o "But, then again, what the hell do {i}I{/i} know about love? I’ve had a grand total of one relationship, and even that was just me being...curious about stuff and wanting to experiment."
    s "I think that...for me, it’s kind of like that too. Like yes, I {i}love{/i} Niki. But-"
    o "But you can’t help wondering if there’s someone you’d feel even {i}better{/i} with...right?"
    s "I...guess?"

    scene otohasreallyhotdude17
    with dissolve

    o "So you’re just gonna fuck everyone you meet until you know for sure? Is {i}that{/i} the plan?"
    s "That’s {i}been{/i} the plan so far."
    o "And how’s that working out for you?"
    s "Great until I remember how many people I’m using and hurting along the way. But there are a lot of moments, where like...I feel like there’s a future with {i}everyone.{/i}"
    s "It’s not always a good one. But I can see it and feel it and...I can’t figure out which one would bring me the closest to some sort of finale that I’d be okay with."
    o "I get it. I fell in love with Maya for a few minutes recently and pictured a whole life with her that was just...gone the moment I got home."
    s "Yeah, she does that to people."
    o "The heart wants what the heart wants, I guess. Do you really think we’re bad people for not fully understanding ourselves, though?"
    s "That is most assuredly not what makes me a bad person. {i}You’re{/i} fine. You’re just a teenager. You haven’t had enough time to become a bad person yet."

    scene otohasreallyhotdude18
    with dissolve

    o "Teenagers can be bad too. Like, for all you know, I’m even more messed up than {i}you{/i} are."
    s "I’m trying to picture what an evil Otoha would even look like and now I’m worried that you’re going to start stealing girls out of my harem."
    o "First, Rin. Next, Maya. You’re cooked."
    s "Yeah, just dismantle the foundation and everything else will crumble soon after."
    o "Oh, so {i}Maya{/i} is the foundation? Not Niki?"
    s "..."
    o "..."

    scene otohasreallyhotdude19
    with dissolve

    o "Wait, seriously?"
    s "Let’s...not talk about her. Just..."
    s "I obviously won’t tell you {i}not{/i} to try and “steal” anyone from me. But-"

    scene otohasreallyhotdude20
    with dissolve

    o "I’m not going to {i}steal{/i} anyone, Sensei. I doubt I even could if I tried. I’m not exactly adored around here."
    s "...but I won’t blame you or even put you in the same category as me for just wanting to experiment since now is the time of your life to actually {i}do{/i} that."
    s "You don’t want to reach your thirties without knowing what you’re after. So figure everything out now while you still can."
    o "Just so you know, the last time someone started talking like this to me, I kissed them."
    s "You can kiss me if you want."

    scene otohasreallyhotdude21
    with dissolve

    o "I know. I’m just not sure if I even want to {i}risk{/i} you being the person I wind up wanting the most. Being into older people has been nothing but a headache so far."
    s "Well, I’m definitely not going to recommend following in my footsteps and corrupting the younger demographic when doing that for you would {i}literally{/i} involve robbing cradles."
    o "I mean, they wouldn’t have to be {i}that{/i} much younger. But going down even a few grades when you’re my age will make people talk."
    s "Well, Otoha, that’s because your bodies are going through changes right now and-"
    o "If I do kiss you, will you shut the fuck up about whatever you’re about to say?"
    s "Yes, but it will probably be out of shock since I didn’t think you’d graduated past simply masturbating in front of me yet."

    play sound "static.mp3"
    scene otohasreallyhotdude22 with flash
    stop sound

    o "I told you to stop bringing that up."
    s "Wait...you’re not {i}actually{/i} going to kiss me, are you?"
    o "You’re not gonna, like...grab my ass if I do, are you?"
    s "Uhh...nooooo?"
    o "That’s the least convincing “noooooo” I’ve ever heard."
    s "Sorry. I’m just getting a million different signals right now and I’m not sure how many them are only there to fuck with me."
    o "You said it’s time for me to experiment, right? I’ve never kissed a boy. You’ve never kissed me. We’re both lonely. All signs say we should do this."
    s "I...mean..."

    scene otohasreallyhotdude23
    with dissolve

    o "...is what I {i}would{/i} have said if you’d given my present to Niki and provided me {i}any{/i} amount of closure on that chapter in my life."
    s "I’ve never been more regretful to be forgetful than I am right now."

    play sound "dooropen.mp3"

    o "You’re lucky you don’t have that pocketknife on you or I’d use it to chop your balls off."
    s "I’ve never been more thankful to be forgetful than I am right now."
    o "The funniest part, though? I’m actually {i}serious.{/i}"
    s "You...actually would have tried? But just a minute ago, you were all like “I’m Otoha. I don’t even {i}want{/i} to want you.”"
    o "Yeah. I’m {i}like{/i} a lot of things. But I {i}do{/i} get to blame it on hormones because, unlike you, I-"

    scene otohasreallyhotdude24
    with dissolve

    o ".........ah."

    play sound "static.mp3"
    scene otohasreallyhotdude25 with flash
    stop sound

    no ".........."
    o "N-Nodoka! Heeeeey! "
    no "This...was not on my bingo card so early. "
    o "It’s not what it looks like!"
    s "Yeah. Otoha was just telling me that she’ll only fuck me after I close the door on her chances of fucking my girlfriend."
    o "That- no! There is no “fucking!” "
    s "Ass grabbing, then. Sorry."
    o "None of that either! You don’t-"

    play sound "window.mp3"
    scene otohasreallyhotdude26
    with hpunch

    o "KYAH!"
    s "Your boob just touched me. Look at you, trying to seduce me when you could just have me whenever you want."
    o "I got scared, okay?! How was I supposed to know that Nodoka’s fucking Starbucks cup would sound like a broken window after being dropped?! There’s no way that was the correct sound effect!"
    no "Shut up. Wait. I have to..."
    no "Something is..."

    scene otohasreallyhotdude27
    with dissolve

    no "Something is...{i}coming!{/i}"
    s "Is Nodoka really about to have an orgasm in the middle of the doorway?"
    o "No, I think-"

    scene otohasreallyhotdude28
    with dissolve

    no "INSPIRATION!"
    o "Yeah. I think it’s that."
    no "Once more, from the top! Spare no detail! I need to see everything about how the two of you made it to this point!"
    s "Well..."

    stop music fadeout 10.0
    scene black
    with dissolve2

    s "It all started when I walked in on Otoha changing..."
    o "Don’t go changing the story right from the start!"

    $ renpy.end_replay()
    $ otohaspring4 = True
    $ otoha_love += 1

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label beachsixotoha1:
    scene sky
    with dissolve2

    "The familiar scents of salt water and sunscreen flood my senses as I look to the sky in search of respite from the expected accompanying visual stimulation."
    "There is only so much my senses can take at once, and that is precisely why I need to be careful in places like this."
    "The girls of class 1-A now are not the same girls they were in the past. "
    "And seeing as a good portion of that (if not all of it) is my fault, I must remain vigilant. I must remain {i}abstinent{/i} so as not to further contaminate them."

    scene beachsixotoha1
    with dissolve2
    play music "youwerespring.mp3"

    "...is what I {i}would{/i} be saying if I had not already given up and succumbed to the incessant lust that governs this [[comparably] hulking body."
    "I am going to have so much weird and impure sex this weekend. I sure hope there’s no god present to smite me."

    ay "Wow! The weather’s so great today that it might even lessen the impact of whatever impending drama currently hangs over us like clouds!"
    s "Couldn’t have said it better myself, Ayane."

    scene beachsixotoha2
    with dissolve

    ay "Woah! We’ve even got an ominous floating caption that potentially foreshadows our impending doom! So fun!"
    s "I’m just glad I’m not the only one who can see it."
    ima "Senpai! Senpai!~"

    play sound "static.mp3"
    scene beachsixotoha3 with flash
    stop sound

    ima "You actually came! Not that I was worried you {i}wouldn’t{/i} or anything. But now that you’re here, I’m definitely way less nervous and flighty! Probably just a coincidence."
    ay "Hi, Miss Imai. I am here as well, and I am extending my need for attention to you too since you are just girl-Sensei. "

    scene beachsixotoha4
    with dissolve

    ima "Dude, what have I ever done to deserve that sort of slander?"
    s "Imani, I don’t think you’re allowed to like me and also say things like that at the same time."

    scene beachsixotoha5
    with dissolve

    ima "Racism! You think you can tell me what I can and can’t do just because I’m black, don’t you?!"
    s "How many times are you going to play that card? You know that makes literally zero difference to me."

    scene beachsixotoha6
    with dissolve

    ima "Oh, sorry. My b. Let me try again."

    scene beachsixotoha5
    with dissolve

    ima "Sexism! You think you can tell me what I can and can’t do just because I’m a woman, don’t you?!"
    s "{i}Hah...{/i}"
    ay "You should really be more accepting of girl-Sensei, boy-Sensei. Your species might even die out at this rate. I only know three of you with character models."

    scene beachsixotoha7
    with dissolve

    ima "Is that a caption I see floating away over there?"
    s "No, just the last remaining segment of the fourth wall. Status report, Imani."

    scene beachsixotoha8
    with dissolve

    ima "Only if I get to subsequently debrief you at the end of the day! And Ayane — you didn’t hear that! "
    ay "Can I help?"
    ima "No. You already have Makoto."
    s "Oh, right. I want to hear more about Ayane’s sudden lesbian side before this conversation proceeds. "
    ima "No! Status report is as follows: we are on the beach! {i}Most{/i} of us, at least! "
    ima "And later, we will be in our respective bedrooms! Which we are {i}not{/i} sharing despite how much I tried to make that happen this year."
    ima "And again, Ayane — you didn’t hear that!"
    ay "We all know about you and Sensei already, Miss Imai. You don’t need to hide it."

    scene beachsixotoha9
    with dissolve

    ima "Aww!~ They’ve already given us their blessing, Senpai! We should stage a fake announcement in front of the class and have one of the girls film it so we can go viral."
    ay "Now, I never said I was giving you my- ahh! Sensei?! Did you just {i}push{/i} me?!"
    s "No, that was the caption."
    ay "It wasn’t the- oh my God, it is! Ah! Back! Back, I say! I have a gun!"

    "The caption chases Ayane down the beach, leaving just Imani and me. And everyone in the background. Mostly Imani and me."

    scene beachsixotoha10
    with dissolve

    ima "Anyway, I’d love to stay and chat more, but I’m organizing a volleyball thing with Karin later and I’ve gotta go help her with that. Come find me tonight, maybe? "
    s "Like, sexually?"
    ima "Well, yeah. If I’m gonna debrief you, it sure as hell ain’t gonna be platonic."
    c "Sensei!"
    r "Dad!"

    play sound "static.mp3"
    scene beachsixotoha11 with flash
    stop sound

    s "Oh, okay. I guess it’s your turn now."
    c "Hi! Yes. Come hang out with us. Preferably without your shirt on. But only because I am worried about you overheating."
    s "Imani already left if that’s what you’re worried about right now."
    c "Then, please take your shirt off because you are hot and I want to touch you. "
    r "I have also always secretly wanted to touch your abs, so let the record show that I support Chika’s suggestion."

    scene beachsixotoha12
    with dissolve

    c "Didn’t you just call him your dad?"
    r "Yes. But let the record show that this doesn’t make things weird because I’ve never actually had a dad, so calling {i}Sensei{/i} “Dad” isn’t taboo at all and is actually just fun."

    scene beachsixotoha13
    with dissolve

    c "Woo! No dad club! "
    s "That’s like half of the class, I think."

    scene beachsixotoha14
    with dissolve

    c "Right! Which means we need to find an advisor if we want to make things formal. Which we do! Right now! So come shirtlessly resolve our respective daddy issues!"
    s "Can I at least finish greeting everyone at the beach first? I literally just got here."
    c "Fine. But only since doing so is your moral obligation."

    scene beachsixotoha15
    with dissolve

    s "Great. Then I’ll start with Otoha, who is currently approaching us."
    c "What?"

    play sound "static.mp3"
    scene beachsixotoha16 with flash
    stop sound

    o "Hey. "

    play sound "static.mp3"
    scene beachsixotoha17 with flash
    stop sound

    o "Am I...interrupting something?"
    c "Yes."
    s "{i}No,{/i} Otoha. You are not interrupting anything. And thank you for saving me the steps required to come say hello to you."
    r "Do you need something from Sensei, Otoha? I’ve never seen you go out of your way just to say hi to him before."

    play sound "static.mp3"
    scene beachsixotoha18 with flash
    stop sound

    c "Don’t talk to her, Rin. She’ll destroy you again."
    o "You’re still being weird about that? That was like, forever ago."
    c "Yet the wounds still remain."
    o "Do they? Because Rin seems pretty cool with me. And, if I remember correctly, at least {i}I{/i} gave her a shot when she confessed. "

    scene beachsixotoha19
    with dissolve

    r "She’s got a point, Chika. And the wound you left probably {i}did{/i} sting a little harder since I liked you for so long. Not that it was actually your fault or anything, though."
    c "That was different! I already had somebody!"
    o "Wooooah, really? Who could it have possibly been? "

    scene beachsixotoha20
    with dissolve

    o "Do {i}you{/i} know, Sensei? Because I have absolutely nooooo idea who Chika might have feelings for if not my ex-girlfriend. I am in a state of complete and utter cluelessness."
    s "Before Chika kills you, is there {i}actually{/i} something you need, Otoha? Or are you really just saying hi?"

    scene beachsixotoha21
    with dissolve

    o "Yeah. I’m invoking my privilege as your cool older sister to rescue you from these two girls who clearly want to use your body for their own nefarious purposes."
    s "But I like it when my body is used for nefarious purposes."
    o "Then kindly ask them to hold it in for like thirty minutes while I yell at you for being such an idiot. Which is {i}another{/i} privilege I have as your cool older sister."
    c "So are you just going to cozy up to {i}everyone{/i} I love, or what?"

    scene beachsixotoha22
    with dissolve

    o "Maybe. I can’t find Yumi, though. Have you seen her anywhere? I’ve decided to date her next. "
    r "So that’s...the path you’re taking, Otoha?"
    o "What- dating Yumi? That was a joke. There are only like two girls in our class I’d consider dating and I’ve already tried that with one of them."

    scene beachsixotoha23
    with dissolve

    r "Wait. Who’s the other one then?"
    c "Don’t {i}ask{/i} her, Rin! That makes it sound like you’re interested!"
    o "Maya."

    scene beachsixotoha24
    with dissolve

    r "Ohhhh! Yeah, I get it."
    c "Don’t “get it” either! What is that supposed to mean?!"
    r "I can just totally see those two together."
    s "Just what the hell is going on with you and Maya behind my back? "

    scene beachsixotoha25
    with dissolve

    o "Nothing, unfortunately. At least outside of my dreams. "

    scene beachsixotoha26
    with dissolve

    o "Enough chit-chat, though! You’re coming with me."

    scene sky
    with dissolve2

    c "H-Hey! Otoha! Who do you think are just stealing people away from...other people all the time! Bring Sensei back here! Rin and I have daddy issues that need to be resolved!"
    s "Yeah, and I need to go resolve them."
    o "Maybe trying to resolve your {i}own{/i} issues first would be a better idea, hm?"
    s "Ugh, but that’s so {i}hard.{/i}"
    o "The best things in life normally are."
    s "Ahh. You mean like a penis."
    o "Yup. The best thing in life is definitely the penis. That’s why I’ve only had romantic feelings for girls."
    s "There’s a spark between us, Otoha. I know you can feel it too."
    o "Mhm. And I can’t control it anymore! Please! Take me, Sensei! Right now!"
    r "Chika, as a fellow Sensei-liker, do you ever find yourself fantasizing about Sensei with other girls?"
    r "Specifically girls you have dated before? And that, instead of actively participating in said fantasy, you’re sort of just off to the side watching and touching yourself?"
    c "{i}See!{/i} I told you she was going to destroy you again! Keep that whore out of your fantasies and just...put some other girl in there instead! One you like more! Who won’t hurt you!"
    r "You mean, like...Futaba?"
    c "Not like Futaba!"

    play sound "static.mp3"
    scene beachsixotoha27 with flash
    stop sound

    s "Otoha — we’ve been walking for five minutes and I haven’t “taken” you yet. When do we get to that part?"
    o "Whenever my last ounce of self-respect has faded away. So, I don’t know — another month or two, maybe?"
    s "Fine. I’ll wait. But I’m formally requesting that you wear that swimsuit when I {i}do{/i} get to take you because it does a great job of accentuating your surprisingly hot body."
    o "Why is my hotness surprising to you?"
    s "I think it’s mostly just because you’re always wearing pants. Which is probably another reason I like your pajamas so much. "
    o "Really laying it on thick today, huh? Has not having your childhood girlfriend around to {i}relieve{/i} you every morning finally driven you mad?"

    scene beachsixotoha28
    with dissolve

    s "Tch. I was worried that’s where we were heading. "
    s "She told you, didn’t she?"
    o "She told me {i}a lot.{/i} Way more than I’d expect her to given our...history. But, you’ll be proud to know that I did not attempt to kiss her while she was at her most vulnerable this time."
    s "Yeah, you’re too busy liking {i}Maya{/i} instead now."

    scene beachsixotoha29
    with dissolve

    o "Not at all. Niki will always be my number one. She’s the perfect girl, after all. "
    s "Wow. I feel a lot better now, Otoha. Thank you."
    o "I think you’re misunderstanding something, Sensei. I don’t {i}want{/i} to make you feel better."

    scene beachsixotoha30
    with dissolve

    o "I want you to know that you’re the biggest idiot in the whole wide world for letting a girl like that get away! Were you dropped on your head as a child? Because it sure seems like it!"
    s "..."

    scene beachsixotoha31
    with dissolve

    o "Oh, look! We’re finally here!"

    scene black
    with dissolve2

    s "Finally where? I don’t see-"

    play sound "tackle.mp3"

    o "Sit."

    "Otoha darts behind me and pushes me onto..."

    scene beachsixotoha32
    with dissolve

    "A fucking banana boat."

    s "Did we really walk all the way over here just to talk on a giant banana again?"
    o "I figured that being called an idiot on top of a giant, buoyant fruit would lessen the impact on your already minuscule self-esteem."
    s "Yeah, I might as well replace my couch with one at this point. Now, go on. Hit me. Say all you need to say about how much I fucked things up."

    scene beachsixotoha33
    with dissolve

    o "I will! But first, let me congratulate you! "
    o "I truly believed it was {i}impossible{/i} to disappoint so many people at once. But you managed to disappoint {i}millions{/i} by breaking a famous idol and essentially forcing her into retirement!"
    o "It’s a new high score! You finally did it! You just {i}now{/i} have to live with the weight of never being able to surpass it. So it’s all downhill from here, buddy."
    s "Yeah, well...if it makes you feel better, I’m definitely not happy with myself."
    o "Now, why the ever-loving {i}fuck{/i} would that make me feel better?"
    s "Beats me. But you’re smiling pretty fucking aggressively right now, so I can only imagine you’re enjoying this."
    o "I am smiling out of sheer disbelief, not {i}joy.{/i} "
    o "Like, I always knew you’d manage to fuck things up with her, sure. But having her walk in on you fucking her little sister is, like...{i}what?{/i} Really? You’re {i}starting{/i} with the killing blow?"
    o "{size=-1}So not only is the love of her life cheating on her, but he’s cheating on her with a teenager. And not {i}only{/i} is she a teenager, it’s her little sister. You couldn’t write a soap opera more dramatic than that.{/size}"
    o "Wouldn’t it have made more sense to cheat on her with an adult first? You know? Sort of {i}ease{/i} her into the fact that you’re an insatiable pervert who’ll fuck anything that moves?"
    s "Otoha, I don’t know what you want me to say here. I can’t justify it. I can’t even {i}explain{/i} it. But it happened, and now I’m paying the price."

    scene beachsixotoha34
    with dissolve

    s "It’s not {i}just{/i} Niki who left either. Ami’s gone too. She’s been staying at the dorms ever since it happened."
    o "So Niki’s just not coming to your place {i}at all{/i} anymore? Because she told me she was."
    s "She stops by to pick things up and do laundry, but she doesn’t talk to me. She doesn’t even {i}look{/i} at me. I’ve been entirely alone in there, and it’s driving me insane."
    s "Or...{i}more{/i} insane, I guess. There’s sort of a baseline level of insanity that can be assumed in regard to me since my track record shows me doing shit like this all the time."
    o "Well, if it makes {i}you{/i} feel any better, you are definitely not the only one suffering. In fact, if anything, I’d say Niki has it like ten times worse than you."
    o "Because {i}you’re{/i} still out here having fun and flirting with girls. {i}She{/i} hasn’t even been able to practice lately. So her entire album is on hold right now while she “recovers.”"
    s "Still has time to meet with you, though."
    o "Yeah. But my singing lessons have essentially turned into “Otoha’s counseling hour” where I just watch her cry and internally debate whether or not I should pat her on the back or something."
    o "You have {i}fucked that girl up.{/i} And I don’t think time alone is going to fix that, Sensei."

    scene beachsixotoha35
    with dissolve

    o "But, {i}at the same time,{/i} I don’t think I’ve ever seen Noriko {i}happier.{/i} Just that happiness comes at the cost of the rift you sowed between her and Niki. So, like...{i}what the fuck?{/i}"
    o "{i}I{/i} don’t want to be in the middle of this. But I feel like I {i}have{/i} to at this point or Niki will essentially just remain invisible to you and things will {i}never{/i} get better."
    s "What now, then?"

    scene beachsixotoha36
    with dissolve

    o "Dude, you tell me. {i}I{/i} can’t fix this for you. But I don’t want to just sit around while my favorite lopsided power couple breaks up either. "
    o "Can’t you just...{i}talk{/i} to her?"
    s "And disregard her wishes? Sure. But she told me she wants space, so that’s what I’ll give her."
    o "Isn’t fucking her sister sort of “disregarding her wishes” as well? Or is that a wish you were just {i}okay{/i} with disregarding because you got something out of it?"
    s "It wasn’t just...{i}something,{/i} Otoha. I wasn’t thinking about Niki when it happened. Just Noriko. And Noriko’s been silently suffering {i}forever{/i} because of me. "
    s "She’s {i}actually{/i} like a sister to me. She didn’t just start pretending to be one like you are now."

    scene beachsixotoha37
    with dissolve

    o "..."
    s "..."
    o "Was that really necessary?..."
    s "I don’t know...I’ve got no fucking clue."
    o "You really think I’d spend this much time and energy on you if I was just {i}pretending?...{/i}"
    o "{size=-1}I’m an only child, Sensei. I don’t have the {i}luxury{/i} of actually knowing what it’s like to be a sibling. Or the {i}history{/i} of growing up beside you. So are my feelings just invalid because of that?{/size}"
    s "No...they’re not."
    s "I just have a hard time figuring out who’s being authentic and who isn’t. So I sort of assume everyone {i}isn’t{/i} by default."
    o "{i}Why{/i} though? Who do you actually know that {i}isn’t{/i} inauthentic? Because everyone {i}I{/i} know that {i}you{/i} know genuinely cares. {i}Too{/i} much even."
    s "Nowadays, no one. But this outlook isn’t exactly {i}new.{/i} A lot of shit happened to me well before you were even {i}born,{/i} Otoha."
    o "{i}Okay.{/i} But are you really going to let that define you for the rest of your pathetic existence? Just fucking grow up, dude. The past is the past. Niki’s here {i}now.{/i} And she needs you."
    s "No, I need her."

    scene beachsixotoha38
    with dissolve

    o "{i}No.{/i} She needs {i}you.{/i} "
    s "She was fine without me for-"

    scene beachsixotoha39
    with dissolve

    o "She was absolutely {i}not{/i} fine without you for {i}years.{/i} She was an obsessive loner who became engulfed in her work out of sheer spite toward you. "
    o "She was {i}never{/i} happy. {i}Never{/i} comfortable. And she drifted from hotel room to hotel room every single night, waiting for the {i}slightest{/i} hint that you still gave a shit."
    o "And even now, after you have done the {i}worst{/i} possible thing to her, she is {i}still{/i} obsessed and {i}still{/i} wants to figure out how to make something that will never work {i}work.{/i}"
    o "{i}That{/i} is true codependency. Not this “moping around and helping teenage girls resolve their daddy issues” bullshit you’re already on after being here for twenty minutes."
    s "..."
    o "Just {i}go{/i} to her. Show her that you still care. "
    s "And then what? Hurt her again?"
    o "{size=-2}{i}Yeah.{/i} Hurt her again. As many times as you have to. Because it might not seem like it, but that’s better for her than just being indefinitely neglected when she has sworn to be {i}yours{/i} for the rest of her life.{/size}"
    s "I just don’t want her to {i}be{/i} like that anymore, Otoha. I want her to move on and find someone who {i}won’t{/i} hurt her. Then I can just...hurt in her place."
    o "Well, tough fucking shit because that’s not how her stupid obsessive idol brain works. Niki will die with a body-count of one if you never see her again. "
    o "How's she supposed to find someone else when her taste in men is just “the worst man on earth?” Because there can only {i}be{/i} one worst man on earth, and that man is clearly you."
    s "You really do know exactly what to say to make all of my troubles fade away, Otoha."
    o "Sensei. You are making a {i}mistake.{/i}"
    o "You don’t like being away from her. {i}She{/i} doesn’t like being away from {i}you.{/i} Fuck her space. Fuck {i}your{/i} moping. Just...tell her you’re sorry and fuck her sister in private from now on."
    s "Is..."
    s "Do you really think she’s that dependent on me?"
    o "{size=-1}A thousand times yes. And I’m low-key worried that something in the water is causing it because your fucking weirdo niece is the same exact way and everyone {i}else{/i} is slowly becoming like that too.{/size}"
    a "Daughter."

    $ renpy.end_replay()
    $ beachsixotoha1 = True
    $ otoha_love +=1

    jump beachsix2
