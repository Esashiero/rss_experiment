label callimanimorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if imanidate1 == True and chap4active == False:
        jump imanimorninggen
    else:
        play sound "phonebeep.wav"

        "I tap on Imani's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't pick up."
        "I guess I'll call someone else instead."

        jump callmorning

label callimaniafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if chap4active == True and cafeclosed == False:
        jump imanispringnoongen
    else:
        play sound "phonebeep.wav"

        "I tap on Imani's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't pick up."
        "I guess I'll call someone else instead."

        jump callafternoon

label callimaninight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if imani_love > 0 and wakanaspecial15 == True and imanidate1 == False:
        jump imanidate1
    if imani_love >= 5 and imanidate1 == True and imanidate5 == False:
        jump imanidate5
    if chap4active == True:
        jump imanispringnightgen
    else:
        play sound "phonebeep.wav"

        "I tap on Imani's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't pick up."
        "I guess I'll call someone else instead."

        jump callnight

label imanidive:
    if chap4active == True:
        jump imanispringdivegen
    else:
        scene imanidivegen
        with fade
        play music "10c.mp3"

        "I head over to the bar to meet up with Imani and others and find myself spending the entire night focusing on her- though, not intentionally."
        "You see, Imani was feeling particularly bored today and decided to come here a solid hour before the rest of us. Which means that she was already pretty drunk by the time we arrived."
        "And when Imani is drunk, Imani is..."
        "Well, take normal Imani and just multiply her by five."
        "It doesn't happen all the time as she's normally pretty good at holding herself back. But when it {i}does{/i} happen, it's basically the only thing any of us can focus on. "
        "Or...are {i}allowed{/i} to focus on."
        "As you may have guessed, she talks my ear off and seemingly forgets that there are other people with us as well. Which is fine by me as it provides a great deal of attention-"
        "But is also annoying- as it provides a great deal of attention."

        scene black
        with dissolve

        "Eventually, Imani accepts that she has had enough and elects me as the person responsible for bringing her home."
        "As such, the two of us depart from the bar a bit earlier than Wakana and Rika and make our way out into the streets, barely managing to stay upright on account of one of us being dead weight."
        "Imani needs to completely rely on the support of my arm to even walk and stays latched onto it the whole way back to her apartment."
        "Thankfully, the walk isn't all that long...so I'm able to get her up the stairs and into bed without a hitch."
        "As I turn around to leave, she thanks me and informs me that I can crash here as well if I want."
        "But seeing as her apartment is the size of my torso and her blood alcohol level is 300%%, I decide to just head back home instead..."

        $ wakana_love += 1
        $ imani_love += 3
        $ rika_love += 1

        "{i}Imani's affection has increased by 3!{/i}"
        "{i}Wakana's affection has increased by 1!{/i}"
        "{i}Rika's affection has increased by 1!{/i}"

        stop music fadeout 7.0

        "........."
        "......"
        "..."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label imanidate1:
    play sound "phonebeep.wav"

    "I tap on Imani’s name in my phone and wait for her to answer, hoping that her constant, overly-friendly banter with me isn’t just her brand of fucking around."
    "We’ve hung out after work several times before, but never without the company of someone else. So I guess tonight is the night I find out if she’s cool with that or not."
    "If not, I’ll just...find something else to do instead."
    "But if she {i}is,{/i} I can finally begin the process of figuring out how to sleep with her."
    "Watch out, Imani. I’m coming for you."

    play sound "phonebeep.wav"
    play music "summerwind.mp3"

    ima "Yo, Senpai! What’s goin’ on?"
    s "Hey. What are you doing tonight?"
    ima "Well, right now, I’m busy grading papers for the work {i}I{/i} assigned to everyone while you were sleeping in your office the other day."
    s "What kind of work are you giving our students behind my back?"
    ima "I just told them to write two pages about shit they think is cool. "
    ima "Did you know both Ami {i}and{/i} Ayane wrote about you? I’m worried they may have copied each other’s work."
    s "Stop doing that and hang out with me instead."
    ima "{i}Just{/i} you?"
    ima "Is this a booty call? "
    s "...Could it be?"
    ima "Mmm...we probably shouldn’t. I like whatever we have going on right now."
    ima "Best to keep stuff professional in the least professional way possible, you know?"
    ima "Plus, I don’t want you holding my job hostage in exchange for being at the beck and call of your endless libido."
    s "It’s not {i}endless.{/i} I have a recharge period."
    ima "Well, don’t count on me to drain that battery of yours. "
    ima "If you {i}do{/i} want to come over and get comfortable, though, I’d probably open the door for you."
    s "I’m getting mixed signals here. People don’t normally invite me over unless they want to have sex with me."
    s "Or...need help making soup."
    ima "I like soup."
    s "Just send me your address, I guess."
    ima "Right-o. Comin’ at you, brother. "
    s "Don’t call me that."
    ima "Nii-chan?"
    s "Slightly better."
    ima "Daddy?"
    s "Again with the mixed signals."
    ima "Don’t keep me waiting, Senpai-Niichan-Daddy. It’s sooooo lonely over here."

    scene black
    with dissolve
    play sound "phonebeep.wav"

    "I hang up the phone before I fall victim to the never-ending games of my student teacher and patiently await her address so I can be led on some more."
    "I half expect it to be similar to Wakana’s or Kaori’s address based on how regular convenient coincidences have become in my life, but am sorely disappointed when I see that it’s not."
    "In fact, it’s an address I don’t recognize at all. And after plugging it into my phone, I realize it’s on the outskirts of the old district, not far from the bar we went to the other day."
    "That’s...good for her, I guess. She can kill time getting drunk and stumbling home while I am forced to kill time by walking all over town."
    "And occasionally fucking a teenager or two."
    "But unless Imani is keeping one as a prisoner, I can’t imagine anything like that is going to happen tonight..."
    "........."
    "......"
    play sound "doorbell.mp3"
    "..."

    ima "Yo! Is that you, Senpai? Or is that an assassin sent by the government to eliminate me?"
    s "Both."
    ima "Shit, what a twist."
    ima "Come on in. Door’s unlocked."

    play sound "dooropen.mp3"
    scene imaniapt1
    with dissolve2

    "I make my way into Imani’s apartment, which feels more like a large closet than an actual living space."
    "It’s situated in a two story building with about twenty other rooms and is clearly meant to be some sort of affordable housing unit."
    "But I guess it’s better to have something like this than it is to be sleeping on the streets or...in the changing room of a spa."

    ima "Heya. Congrats on being my first ever visitor. I’d say we should christen the place, but I’m afraid I’d find out I’m a 6/10 lay as well."
    s "You’re still not over that?"
    ima "How would {i}you{/i} feel if somebody gave you a 6/10 when it comes to kissing?"
    s "I think I’d be more curious about their prior experience and grading scale than whatever my score is."
    ima "Fair enough. Pull up a seat, I guess. Not like there are many of them in here, though."

    scene imaniapt2
    with fade

    s "I think my bedroom is larger than your apartment."
    ima "Did you come here to brag?"
    s "No. But I’m pretty sure that it’s something that’s going to just naturally happen at several points tonight."
    ima "I know it’s small, but I don’t mind. All that really matters is just having a place to sleep and work and, as you can see, both of those things are entirely possible within these walls."
    s "Where’s your cat?"
    ima "Cat?"
    s "And your parrot?"
    ima "Parrot?"
    s "Didn’t you-"

    scene imaniapt3
    with dissolve

    ima "Did I mention having either of those things?"
    s "Unless I’m going insane, I’m pretty sure you did."
    ima "I was probably just fucking with you. I don’t have any pets. "
    ima "Well, except for the cockroach who keeps trying to get into bed with me at night. But I think he’s just got the wrong idea about the two of us."
    s "Why would you lie about owning a cat? Who does that?"
    ima "Me, I guess. I probably thought it was funny. Just do yourself a favor and never believe anything I say unless it makes me look cooler."
    s "I think a parrot would make you look a little cooler."

    scene imaniapt4
    with dissolve

    ima "Hey, if I start saving up for one now, I might finally be able to afford one by the time I retire. "
    s "It’ll be before that. Just think of how much money you’re saving by living here."
    ima "Lay off the slander and sit down. It’s starting to feel like you’re only here to observe me and not to actually chill."

    scene imaniapt5
    with fade

    s "You’re not going to make me help you grade things, are you? Because Wakana has tried to do that before and I still get a little nervous every time I go to see her now."
    ima "Sure you’re not getting nervous because you want to bang her?"
    s "That’s not really something I’d ever get nervous about. "
    ima "Look at me, my name is Sensei. I’m confident and sexually active. I don’t feel {i}feelings{/i} the way “normal” humans do."
    s "Look at me, I’m Imani. I’m a huge fucking bitch."

    scene imaniapt6
    with dissolve

    ima "You offend me. I’m a medium-sized bitch at most."
    ima "But no, I’m not going to make you help me grade anything because I am awesome and have already finished."
    ima "I also know {i}much{/i} more about what everyone in the class is actually into now."

    scene imaniapt7
    with dissolve

    ima "For example, did you know that the role of women in Yasu’s religion is to basically just lie there and let a dude spray his baby batter inside of her?"
    s "I did. And, just for the record, these assignments of yours aren’t things that need to be filed away or...scanned in, are they? "
    s "Because that and the ones written about me aren’t things I want anyone other than you getting their hands on."
    ima "Aww, are we close enough now that you don’t mind {i}me{/i} knowing how creepy you are?"
    s "Like you’ve said before, we make a good team. And I think a lot of that is due to how easy it is for me to talk to you without feeling like I’m being judged."
    ima "Oh, I judge you all the time. I’ve just also judged everyone else and have somehow, after several loops and twists, reached the conclusion that you're not out to hurt anybody."
    ima "Except me, that is. I’m pretty sure being mean to me gets you hard. But, in order to keep this professional, I promise to not bring up your penis again for the rest of the night."
    s "Thanks, Imani. I understand how difficult that must be for you since I figured you're almost always fantasizing about it."
    ima "Not always. Just whenever you leave the room. Gotta keep my guard up when you’re around, you know? Don’t wanna get pregnant and feel the wrathful gazes of nineteen jealous teens. "
    s "Anyway, if you’re not grading anything right now, what are the notebooks for?"

    scene imaniapt8
    with dissolve

    ima "These? A little independent studying."
    s "What’s the point of studying if you’re already a teacher?"
    ima "{i}Student{/i} teacher, technically. I’ve gotta put in a certain amount of work before I’m able to become a full-on teacher. They {i}should{/i} be counting what I do for you as overtime, though."
    s "Yeah, I feel like I’ve all but taken the backseat at this point."
    ima "Works for me. I get to do what I like to do and you get to do what {i}you{/i} like to do."
    ima "Just maybe toss in a platonic massage every once in a while to keep me loose and ready to go."
    s "Sure. How does right now sound?"
    ima "Bad. I’m not done studying yet and we both know that any sort of massage in a room as small as this would end with one of us on top of the other."
    s "Oh no. Whatever would we do in a situation like that?"
    ima "Back on track, Senpai. I will not allow you to seduce me while I’m already being ruthlessly penetrated by the intangible dick that is academia. And two dicks at once? Noooo thank you!"
    s "Must be some pretty intense studying if there’s an intangible penis inside of you right now."
    ima "It’s gotta be if I’m ever going to teach in college. Don’t want some punk who’s only a little younger than me getting snippy and acting like he knows more than I do."
    ima "Of course I say that now, still years away from any job like that...but still."
    s "You want to be a college professor?"

    scene imaniapt9
    with dissolve

    ima "Mhm. Mainly for transfer students, I think. People who don’t natively speak Japanese and stuff like that."
    s "What do they speak in Ghana?"
    ima "English."
    s "Really?"
    ima "What did you expect? German?"
    s "I’m not sure. I’ve just heard there were a bunch of languages in Africa and figured it would be something I hadn’t heard of before."
    ima "English is the official language, but I can speak Twi as well."
    ima "Which means there are three languages I’m fluent in. Which is nothing compared to the, like...ten that Touka’s mom can speak, but hey. Still pretty impressive."
    s "Can you say something in Twi?"
    ima "Medɔ wo."
    s "What does that mean?"
    ima "It means learn the fucking language, Senpai."
    s "Is Twi a naturally rude dialect or are you just an asshole?"
    ima "I’m just an asshole. But I’m {i}your{/i} asshole, Senpai. At least until someone else is willing to hire me."
    s "So if you were offered a college job, you’d leave right now?"
    ima "Of course. "
    s "Wow."
    ima "What? You think I’d throw away my dreams just because I met you? Come on, you know me better than that. "
    s "You could have let me down a little softer, at least."

    scene imaniapt10
    with dissolve

    ima "I’d keep in touch, obviously. It’s not like I’d just erase you from my mind the second I’m not your underling anymore."
    ima "This is probably going to sound really depressing since this is the first time you’re coming over and we’ve only known each other for a little while, but..."
    ima "You’re kind of my best friend. "
    s "Really? Me? Not Wakana? "
    ima "I like Wakana a lot. "
    ima "I just like you more."

    scene imaniapt11
    with dissolve

    ima "Plus, I get to see you for almost seven hours, five days out of every week."
    ima "And you’re easier to talk to. {i}And{/i} you wouldn’t abandon me at a table to go bang your girlfriend in the bathroom. Probably."
    s "Not going to lie, I probably would. "
    ima "Okay, sure. But you’d probably invite me as well and it’s the thought that counts."

    scene imaniapt12
    with dissolve

    ima "Point is, it would take a lot more than just losing a best friend for me to start rethinking my future. Even if we were like, lovers or something...I’d still probably choose myself over you if it came down to it."
    ima "This is a goal I’ve had for myself since I was a kid, you know. It’s not something that’ll be so easily shaken."
    s "What made you want to become a teacher?"

    scene imaniapt13
    with dissolve

    ima "Honestly...the money. "
    s "Rough. "
    ima "Yuuuuup. Mini-Imani figured that teachers, as important as they are, were paid handsomely and able to live on their own without any financial problems at all."
    ima "Boy, do I wish I could travel back and time slap that little girl upside the head."
    ima "Would’ve tried becoming a doctor or something if I knew I’d be living in a box at my age."
    s "It’s interesting that money’s what led you down this path in the first place. I feel like most people become teachers to, like...help children or something."

    scene imaniapt14
    with dissolve

    ima "I don’t even like kids. They’re loud...obnoxious...and always {i}sticky{/i} for some reason. "
    ima "Teenagers are fine because the stickiness kind of wears off after a while. But they’re still not {i}ideal{/i} as looking at them reminds me that I’m getting older and getting older fucking suuuuucks."
    ima "Plus, being the youngest of seven, I never really had many chances to play with or talk to anybody {i}younger{/i} than me. So I'm just not used to it."
    s "I’m sorry, {i}seven?{/i}"

    scene imaniapt5
    with dissolve

    ima "Three brothers, three sisters. All older. All in Ghana."
    s "Why aren’t any of them here with you?"
    ima "They can’t be."
    s "What do you mean they {i}can’t{/i} be?"
    ima "I mean I’m the only one with Japanese blood."
    s "You-"

    scene imaniapt15
    with dissolve

    ima "They’re all technically {i}half-{/i}siblings. "
    ima "I have a different biological father. But my {i}actual{/i} father was a good man and insisted I was just as much {i}his{/i} child as the rest of them- even knowing where I really came from. "
    ima "So I got to grow up in a house with a bunch of people I was only {i}half-{/i}related to, still feeling like a bit of an outcast even though I was welcome there."
    ima "Having seven kids is hard to afford, though...so we scraped by, but never had {i}much{/i} money."
    ima "I don’t know. I thought that maybe striking it rich one day would help me {i}buy{/i} my rightful place in the family. But somewhere along the way, I started actually liking the idea of teaching."
    ima "No one else in my family has ever made it to college, so the fact that I have is just-"

    scene imaniapt16
    with dissolve

    ima "Oh, crap. I’m like, hardcore unloading on you right now, aren’t I? "
    s "It’s fine. I had no idea about literally...any of that."
    ima "The condensed version is that I’m always going to feel out of place and that I want to prove to both my family and myself that I belong. The end. Imani backstory complete."
    s "I’m sure there’s a lot more to you than just that, Imani."

    scene imaniapt17
    with dissolve

    ima "Of course there is. But there’s no reason I should be unpacking my entire childhood right now when I’ve yet to even unpack my boxes."
    ima "You’ll learn more as time goes by...naturally. Without it coming in the form of some spontaneous info-dump only partially relating to a question you asked. "
    ima "There are over seven billion people on this planet and somehow, we were lucky enough to wind up with each other."
    ima "That should be enough for now."

    scene imaniapt18
    with dissolve

    ima "Let’s just enjoy the fact that we-"
    s "You know you’re blushing, right?"

    scene imaniapt19
    with dissolve

    ima "I’m what? No, I-"
    ima "Shit."
    ima "You’re right."

    scene imaniapt20
    with dissolve

    ima "Mind looking away for a minute or two while I repeatedly remind myself that we’re just friends and that anything more than that could jeopardize the first real relationship I’ve ever had in this country?"
    s "I think you might be unloading again."
    ima "You know, I knew this was gonna happen too. I’m going over to your place next time."
    s "You think you’ll be any safer there?"
    ima "Than in an oversized shoebox where our knees have been touching this entire time? Probably."
    s "Didn’t realize your knees were your weak spot."
    ima "Probs because I figured it was something you didn’t {i}kneed{/i} to know."

    scene black
    with dissolve2

    s "Okay, I’m leaving."
    ima "Hey, you don’t have to {i}completely{/i} bail! I just want my face to go back to its normal, beautiful color! The color that {i}doesn’t{/i} make it look like I want to bang my boss!"

    "Imani settles down and prevents me from leaving. "
    "Thankfully (For her, at least. I still don’t really care), she figures out how to restrain herself from exposing any additional info and the rest of the night passes by filled with our typical, mindless banter."
    "I learned a lot about her tonight- intentional or not...but there’s still plenty I don’t understand yet."
    "And I can’t help but wonder if I'll be able to fill in the blanks before she inevitably leaves me."

    $ renpy.end_replay()
    $ imanidate1 = True
    $ imani_love += 1
    stop music fadeout 6.0

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label imanidate5:
    play sound "phonebeep.wav"

    "I tap on Imani’s name in my phone and wait for her to answer."
    "Despite the amount of time we’ve been spending together lately and the amount I have learned as a result of that, I don’t feel like things between us have really {i}changed{/i} at all."
    "So maybe today, something will happen to make me reevaluate that."

    play sound "phonebeep.wav"

    ima "Yoooo, Senpai! What’s going on?"

    "Or maybe nothing new will happen at all."

    s "Nothing much. What are you doing?"
    ima "Dying. What’s your address?"

    "Or...maybe something {i}will{/i} happen after all?"

    s "Why do you need my address?"
    ima "Because I’m coming over, obviously."
    s "I mean, I’m fine with that. But after hearing that you’re “dying” and how you immediately decided to come over without asking, I can’t help but be mildly concerned."
    ima "Be concerned on your own time, you’re wasting my minutes."
    s "Who doesn’t have unlimited phone time in this day and age?"
    ima "People like me who are still using prepaid plans. Now, address please. I’ll explain when I get there."
    s "Fine. See you soon, I guess."

    play sound "phonebeep.wav"
    stop music fadeout 10.0
    scene black
    with dissolve

    "I hang up the phone and send Imani my address."
    "Considering how far away she lives, I think I {i}should{/i} be able to make it back in time. But I have no idea what Ami is up to today, so..."
    "Well, I guess I’ll just have to wait and see if the day will end in tragedy, or if it will end with the defilement of my underling’s body."
    "Probably tragedy."
    "It’s almost always tragedy."
    "........."
    "......"
    "..."

    scene imanicomesover1
    with dissolve2
    play music "lifeismostlygood.mp3"

    ima "Pardon the intrusion. And thanks for having me over. You’re a real life saver."
    s "Uhh...why do you have so many bags?"
    ima "Because I live here now."
    s "That is not what we discussed over the phone."

    scene imanicomesover2
    with dissolve

    ima "It’s not?"
    s "All you told me is that you were running low on minutes and that you’d explain things when you got here. Not that you’d move in."
    ima "I don’t know, Senpai. I’m pretty sure I filled you in on all of the necessary details. But if you {i}really{/i} don’t want me to live here, I guess I can go home."
    s "Cool. See you later, then."

    scene imanicomesover3
    with dissolve

    ima "Fight for me, Senpai! Hold me tight and never let go! Don’t let me just walk out of your life that easy!"
    s "Imani, what’s really going on here?"

    scene imanicomesover4
    with dissolve

    ima "My AC unit busted and turned my apartment into a hotbox. "
    ima "I was actually already planning on calling you and asking if I could crash at your place for the night. But then {i}you{/i} called {i}me{/i} and I figured you’d have a harder time saying no if I was already here."
    s "If it’s just for tonight, why do you have three bags?"

    scene imanicomesover5
    with dissolve

    ima "In case you wanted me to stay longer. As it turns out, my cockroach buddy’s got a whole ass family, so I figured it might be cool to let them have the place for a few days."
    ima "Or for the indefinite future so I can become one of those people who overstays her welcome for so long that she just starts living here without ever having to sign a lease."
    s "If you can convince Ami, sure. You can move in."

    scene imanicomesover6
    with dissolve

    ima "Seriously?"
    s "That depends on if you’re actually serious."
    ima "I mean...I wouldn’t {i}not{/i} be serious about this if you were cool with it."
    ima "Not gonna lie, having an actual kitchen and an actual bathroom sounds a hell of a lot better than having to use the community ones at my apartment."
    ima "Fine. I accept. And for rent, I will let you choose between the 50,000 yen I’m paying for my current place or one sexual favor per week. No mouth. "
    s "No mouth, no deal. I’ll take the money. "

    scene imanicomesover7
    with dissolve

    ima "Understood. Pleasure doing business with you, Senpai. Assuming this isn’t just one big joke, of course. Which I kind of hope it isn’t, but will understand if it is."
    ima "Anyway, where can I put my stuff?"
    s "Wherever. I’ll make Ami take care of it once she gets back."

    scene black
    with dissolve2

    "Imani places all of her bags on the dining room table before returning to me, empty-handed and several minutes away from being forced to fight for her life."
    "Of course, I already know for a fact that she {i}won’t{/i} be living here any time soon, but I doubt one night will be a problem so long as she sleeps in the living room."
    "Either that or I get extremely lucky and Ami just doesn’t come home at all, leaving Imani the option of staying in my room instead- something with roughly a 50%% chance of success based on my calculations."

    scene imanicomesover8
    with dissolve2

    ima "No wonder you talked mad shit on my place, Senpai. Your house is actually pretty nice. Sweet neighborhood, too."
    ima "Can see myself settling down here fifteen years from now when we accidentally reunite at a local museum and decide to go out for one last drink. You know, for old time’s sake."
    ima "But then one drink would turn into ten and we’d wind up finally banging after all that time of {i}knowing{/i} we want to, but never following through with it because reasons."
    ima "Anyway, what’s for dinner? You cooking?"
    s "I don’t think you want to eat anything I make. "
    ima "Same. Guess we’re a takeout family now."
    s "If Ami comes home, I’m sure she’ll throw something together. I just can’t guarantee that your portion will be free of rat poison."
    ima "And if Ami {i}doesn’t{/i} come home?"
    s "We’ll probably order a pizza and continue not having sex for some reason."
    ima "Sounds like my kind of night."

    play sound "dooropen.mp3"
    scene imanicomesover9
    with dissolve

    a "I knew I sensed an intruder."
    ima "Welp, there that goes."
    ay "Imani? What are you doing here?"

    scene imanicomesover10
    with dissolve

    ima "I live here now. I’ll take my steak medium-rare, Ami. Thanks. "
    a "Sure, Miss Imai. Would you also like a side of {i}murder?{/i}"
    ay "Don’t be mean, Ami. She can give you detention. "
    s "Imani’s air conditioner broke. She’ll be staying here for the night."

    scene imanicomesover11
    with dissolve

    a "What?! But you already told me Ayane and Maya could sleep over!"
    s "I don't remember that at all."
    ima "Ooh! Slumber party! That sounds way more fun than not hooking up with your uncle!"

    scene imanicomesover12
    with dissolve

    a "You’re not invited! You can continue not hooking up with my uncle all by yourself in the corner of the room! "
    ima "She loves you so much. It’s adorable."
    s "Don’t piss her off {i}too{/i} much. Remember that she’s the one making your dinner."

    scene imanicomesover13
    with dissolve

    a "Tch! When did my precious house become a brothel?"
    ay "Where will Imani be sleeping? If there’s a lack of room for her, I wouldn’t mind volunteering to sleep with you, Sensei. "
    s "I think there’s plenty of room for her, but I’ll keep that in mind. "
    ima "I was probably just gonna crash on the couch. Joke’s aside, Sensei and I aren’t like that. You guys have nothing to worry about."
    ima "My place is just mad hot and I didn’t want to die. I’ll bounce as soon as the AC repair guy leaves."
    ima "Oh, and ignore all of the bags. I brought those just in case he wants to keep me for whatever reason. But now I just feel weird since my students are watching me."
    a "We are {i}Sensei’s{/i} students. You do not own the original Sensei Love Squad."
    m "Minus Maya. Not a member of the Love Squad. "

    "Lies."

    ay "Lies."

    "Thank you, Ayane."

    scene imanicomesover14
    with dissolve

    m "Hah..."
    ima "So...now what? Wanna play truth or dare again?"
    s "Depends. Which of the girls are you going to make out with this time?"
    ima "I guess that hinges on the dare."
    s "Truth or dare."
    ima "Truth."
    s "Not what I wanted."
    ima "I can not accept a dare in an environment like this. I am not you."
    ay "They’re playing games with each other...and excluding us. "
    ay "I don’t like this."
    a "Why do you think I never want anyone older to come here? It’s a slippery slope, Ayane. And right now, there’s nobody more...slippery than Miss Imai. How could I have been so blind?"
    m "Okay. I’m going to get changed now. I’m tired and haven’t worn this shirt in yet. It's uncomfortable."

    scene imanicomesover15
    with dissolve

    ay "I think it’s the bra. You’ve always worn those tank-top style ones and switching from that to an {i}actual{/i} bra is obviously going to- why are you looking at me like that?"
    m "I wonder."

    scene imanicomesover16
    with dissolve

    s "Ayane, truth or dare."
    ay "Dare!"
    s "Kiss Maya."

    scene imanicomesover17
    with dissolve

    ay "Your wish is my com- wait, where did she go?"

    scene imanicomesover18
    with dissolve

    ay "Maya, come back! Sensei wants us to kiss!"
    m "Don’t come anywhere near me!"
    a "I’m watching you, Miss Imai..."
    a "One wrong move and you will feel the wrath of Ami. A wrath that few have felt before..."

    scene black
    with dissolve2

    "The girls (Minus Imani) retreat into Ami’s room to get changed into their pajamas and formulate some sort of battle plan to kill my student teacher."
    "Thankfully (For her, not so much me), Imani takes the hint and distances herself, unpacking a few of her things before going into the bathroom to get out of her casual clothes. "

    scene nightsky
    with dissolve2

    "The next couple hours go by rather...naturally, believe it or not."
    "All four of the girls return around the same time and Ami and Ayane prepare dinner together while the rest of us sit on the couch and watch TV."
    "Imani gets to eat a hot meal free of poison and I get to somehow sit next to her without incurring the apparently rare “wrath of Ami” at any point."
    "Dinner is the closest we come, though...and once it’s over, she and the two girls who prepared dinner lay out a futon on the floor before sitting down on it and forgetting I even exist."

    scene imanicomesover19
    with dissolve2

    "I don’t have a problem with that, though. "
    "It’s better for all of us if everyone manages to get along. And I guess the amount of exposure the girls already have to Imani is enough to get them to feel more...comfortable around her."
    "In just a short time, she’s managed to win almost everyone over- and I think a lot of that is due to the fact that, unlike me, she’s able to care about them without ever getting anything in return. "
    "She may say things about how being around girls their age isn’t good for her psyche and that looming fear of mortality hidden in the back of our minds but, to be honest, she looks content when they’re around."
    "She’s good at what she does...good at being a teacher."
    "But the fact that she seems even more comfortable with {i}me{/i} makes me question exactly what type of person she is underneath it all."

    ay "College? That’s so cool. I think you’ll be a great professor. You always seem really smart whenever you start getting into it about things."
    ima "I’m still a ways off, but I’ll get there. Thanks for the blessing, Ayane. You were always my favorite."
    a "Hey."
    ima "You’re also my favorite, Ami."
    ima "Everybody’s my favorite. "
    ima "Well, except Kirin. She keeps trying to have sex with me and I don’t like it."

    if ayanelust10 == True:
        ay "Oh, don’t worry. She does that with everyone. Something is seriously fucked up with her brain and we all just have to fucking deal with it, I guess."

        scene imanicomesover20
        with dissolve

        ima "Uhh..."
        ima "Did something-"
        ay "Nope."
    else:
        ay "Sounds like Kirin, alright. "

    ay "But anyway, do you think you’ll at least finish the school year with us? Or should we try not getting {i}too{/i} attached?"

    scene imanicomesover21
    with dissolve

    ima "Attached to me already? Come on, I don’t deserve that. I’m just doing what any other teacher would do. Minus Sensei, of course. But he’s a special case."
    ay "Neither Ami nor I have any older women to look up to, really. And I don’t want to speak for her, but having you around makes us kind of...happy."
    a "I do like you, Miss Imai. I’m just not very good with...uhh...{i}change.{/i}"

    scene imanicomesover22
    with dissolve

    ima "Aww, you guys! You don’t have to go getting sentimental on me!"
    ima "I know doing that is a cornerstone of slumber parties and I’m not about to tell you to stop because hearing that was a major dopamine hit, but...{i}you guys!{/i}"
    ima "I like you too. And I’ll be happy to stay around as long as I can. But I can’t predict the future, and getting attached to {i}anything{/i} can be really dangerous."
    ima "Just be smart and don’t cry too much if I’m suddenly gone one day, okay?"

    scene imanicomesover23
    with fade

    m "I hope you’re happy, starting this festival of {i}feelings.{/i} Something we all know you don’t actually have."
    s "You’re one to talk. I don’t think either of us can really speak to what it’s like to openly discuss our emotions with others."

    scene imanicomesover24
    with dissolve

    m "Yes. Well, I suppose there’s a reason the two of us are standing off to the side while everyone else sits in a circle and carves out little pieces of their heart."
    s "Can’t really make a circle with three people."
    m "I suppose not. But you {i}can{/i} make a triangle, which bears its own form of significance in the fact that-"
    s "Oh no. We’re the philosophical group, aren’t we? And everyone else is part of the fun group."
    m "..."
    s "..."

    scene imanicomesover25
    with dissolve

    m "Philosophy can be fun..."
    m "It’s not my fault you suck at it."

    scene imanicomesover26
    with dissolve

    s "How do {i}you{/i} feel about Imani, Maya?"
    m "Me? In what way?"
    s "In general. Do you like her?"
    m "She’s...fine. "
    m "I have a hard time “liking” anyone. But is there a reason you’re suddenly asking {i}me?{/i} Why do my feelings in regard to someone else matter at all?"

    scene imanicomesover27
    with dissolve

    s "Just...thinking you guys might be better off with her as your full-time teacher rather than me."
    m "I see."

    scene imanicomesover28
    with dissolve

    m "Well, we definitely would. You’re the actual worst person for the job you wound up with."
    m "But I guess I can’t complain as I, too, wound up in a position I never asked for. Never fit. "
    m "Sometimes, life itself chooses what we’re meant to consume. And all we’re able to do is choke down what it serves us and pretend it’s what we wanted."
    m "For the rest of eternity...or until “eternity” breaks."
    s "Philosophy group rules. Who needs fun when we can create metaphors all night?"

    scene imanicomesover29
    with dissolve

    m "Even that is fun in its own way."
    ima "Uhh, Ami? Is it cool if I use your bath? I feel kind of gross from the air conditioning fiasco earlier and don’t think I’ll be able to sleep like this."
    ima "Was gonna try to tough it out because, you know, unfamiliar bath...but yeah. Don’t think that’s gonna be possible."
    a "Oh, sure. I can fill the tub for you right now."
    ima "It’s fine, it’s fine. You stay out here with Ayane. I’m sure I can figure out how a bath works."

    scene black
    with dissolve2

    ay "What if we all went in together? I kind of want to take a bath now too."
    a "This is something you should have said before we put on our pajamas. "
    ay "Sue me. I’m a free woman. I say things when I want."
    a "Also, all three of us? There’s no way we’d even fit."
    ay "But we do it with Maya all the time."
    a "I think Miss Imai is a little bigger than Maya."
    ima "Just a {i}little.{/i} But I’m not much of a “group bather” anyway, so I’ll be quick and then you guys can get in after me."
    ay "Are you sure? We could save time if we-"
    ima "I’ll be {i}super{/i} quick! Don’t even worry. It’ll be like I never even left in the first place!"
    ay "But-"
    a "Just let her go, Ayane. You’re in the swim club now. You’ll have plenty of opportunities to see her naked."
    ay "I just wanted to bond! "

    "........."
    "......"
    "..."
    "{i}The festivities continue on for the rest of the night.{/i}"

    $ renpy.end_replay()

    stop music
    play sound "static.mp3"
    scene imanicomesover30 with flash
    stop sound

    "{i}But for a brief moment, there is a fracture.{/i}"
    "{i}It goes unnoticed by the majority, but the part of the group that does recognize it sees nothing else until the night comes to an end.{/i}"

    scene black

    "{i}Until she closes her eyes and finds comfort in where she is and not who she is.{/i}"
    "{i}Until she wakes up the next day and leaves it all behind.{/i}"
    "{i}Oh, how easy it is to ignore our flaws when we cannot see them.{/i}"
    "{i}Oh, how easy it is to remember them once we can.{/i}"
    "{s}SLIP{/s} sleep"

    $ imani_love += 1
    $ imanidate5 = True

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
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

label imanidate15p1:
    scene imanibardate1
    with dissolve2
    play music "10c.mp3"

    "I find myself alongside my slightly wonderful (but mostly annoying) kouhai on the way back from another uneventful day at school."
    "Or at least what {i}was{/i} an uneventful day up until the very end of it, when I was somehow suckered into assisting Imani and some of the other girls in cleaning the pool."
    "But {i}that{/i} isn’t what I’ve decided to share with you today. "
    "What I {i}have{/i} decided to share is the tail end of a long walk to the bar after a hard day’s work because it’s moments like these where my mind begins to wander."
    "And as it detaches itself from the inside of my skull and saunters off down alleys unexplored, I must summon the me who once was to take over in its stead."
    "But that “me” overcomplicates things. "
    "It turns otherwise pleasant moments upside down when it remembers that it and {i}we{/i} are undeserving of quiet moments like this."
    "We’re undeserving of long walks to the bar or bubble tea or the pruning of our hands after soaking them in soap and water for hours on end."
    "But no one cares what we do or don’t deserve. No one cares if things are complicated or not."
    "All that we want is to watch one thing transform into something else. That’s what keeps life fresh. {i}That’s{/i} what keeps our interactions notable."
    "So I will disguise myself as a passable human being and communicate with this girl in a way that is mostly normal, but {i}fractionally{/i} strange based on an unwanted substitute..."
    "It’ll be fine, though. "
    "Everything will be fine."
    "She’ll laugh and smile and flirt and laugh again because {i}that{/i} is what she does as a slightly wonderful (but mostly annoying) kouhai. Which is, again, {i}fine.{/i}"
    "But it’s not what anyone wants to see."
    "What we want is the closing of a gap between two people who would be better off remaining three feet apart in perpetuity, because that closure breaks the silence."
    "It interrupts our walk."
    "And it lays down the foundation of the {i}real{/i} story here. Not just the one we got conned into watching after pressing the wrong button on a metaphorical TV remote."
    "Why can I not just walk home in peace?"
    "Why does everything have to be an event?"

    ima "Senpai. Tell me a joke."
    s "Knock knock."
    ima "Who’s there?"
    s "No."
    ima "No who?"
    s "..."
    ima "..."
    ima "That was it, wasn’t it?"
    s "Funny, right?"

    scene imanibardate2
    with dissolve

    ima "No! And why did you make me knock if you were just going to turn me away?"
    s "Because your disappointment is funny to {i}me{/i} and comedy is subjective. It’s not my fault if you don’t laugh."

    scene imanibardate3
    with dissolve

    ima "Mm."
    s "Knock knock. "
    ima "I’m not falling for it again, Senpai. We can just go back to talking about boring {i}normal{/i} stuff since that’s apparently all you’re capable of."
    s "Well, it’s not as if we can make idle chit-chat about how our day was when we spent the entire thing together. "
    ima "Correct me if I’m wrong here, but I’m pretty sure that falls into “boring normal stuff.” Tell me something interesting. As my elder, isn’t it your job to keep me entertained on long walks like this?"
    s "Uhh...no? As the younger, more energetic teacher here, shouldn’t {i}you{/i} be the one keeping things “entertaining” while I just...nod and say something mildly sexual every once in a while?"
    ima "Maybe. But you haven’t even done {i}that.{/i} And if you bring that attitude to the bar, the rest of the girls are going to wind up kicking you out of the friend group no matter how hard I try to stop them."
    s "I think I’ll be okay. Despite what little time we’ve all shared together, I think we’re a pretty tight-knit group by now. Besides, my role as the token male would be hard to just outright replace."

    scene imanibardate4
    with dissolve

    ima "Ooh! Then that means my role as the token “young one” will be hard to outright replace too! Hooray for us! We’re both-"

    scene imanibardate5
    with dissolve

    ima "Wait. You thought I was going to say something else just now, didn’t you?"
    s "I literally didn’t even move my mouth."

    scene imanibardate6
    with dissolve

    ima "Likely story! Now, either tell me a joke or I’m quitting Kumon-mi High and getting a job in the sinkhole."
    s "It was nice working with you, Imani. Sorry we never got to make out."

    scene imanibardate7
    with dissolve

    ima "Don’t be. You’re not missing much if Rika’s scale is anywhere near the same as yours."
    s "I’m not sure if it’s rude to say this or not, but I’m pretty sure her scale is a lot...{i}larger{/i} than mine."
    ima "It would have been a little less rude without the awkward pause and emphasis placed on {i}larger.{/i} But yeah...you’re probably not wrong."

    scene imanibardate8
    with dissolve

    ima "Just don’t repeat that to her, okay? She’s a little sensitive when it comes to people pointing out her past and...you’re looking away from me."
    s "..."
    ima "You already did that, didn’t you?"
    s "Not...purposely."

    scene imanibardate9
    with dissolve

    ima "Hah...what am I going to do with you?"
    ima "As if taking over in school isn’t already enough, it’s like you want me to take over in-"

    play sound "vibrate.mp3"
    scene imanibardate10
    with dissolve

    ima "Wait, hold that thought. That’s probably one of the girls right now."
    s "How can I hold {i}your{/i} thought? That’s not how that works."

    scene imanibardate11
    with dissolve
    play sound "phonebeep.wav"

    ima "Hello?..."
    ima "Oh, hey! I was actually just talking about you..."
    ima "No...It wasn’t about how much you like pizza. And I’m not sure why you would have assumed that, but...what’s up?"
    ima "..."

    scene imanibardate12
    with dissolve

    ima "Wait, really?..."
    s "..."
    ima "Like...not at {i}all?{/i}"
    s "...?"

    play sound "vibrate.mp3"

    "As Imani converses with who I can only imagine is Rika, my phone begins to ring as well..."

    scene imanibardate13
    with dissolve
    play sound "phonebeep.wav"

    s "Hello?"
    w "Arakawa — I need you to listen carefully. "
    w "You are being set up."
    s "...What?"
    w "I am a good friend who has not revealed any of the things you said to me the other night about your childhood friend or your feelings concerning Imani, so I want you to know this has nothing to do with me."
    w "And also that I am sorry. I tried."
    s "I’m not really sure what-"
    w "No one else is coming to the bar. It is a calculated effort coordinated by Osako and Rika to get you and Imani alone together. I had no part in this."
    ima "...Uh-huh."
    s "Ah. So {i}that’s{/i} what’s going on."
    w "It won’t be a problem, will it? The two of you being alone together."
    s "Not at all. But thanks for letting me know you had nothing to do with it, I guess. "
    w "Of course. "
    w "Just also know that I am not opposed to the idea of you having sex with her. In fact, if it were not for your “feelings,” I would say that would be the best outcome possible."
    s "I’ll keep that in mind, Wakana. Goodnight."
    w "Wait, Arakawa — there’s one more thing."
    s "There always is. What is it this time?"
    w "Nothing important. Just that-"
    w "I want to fucking die."

    play sound "phonebeep.wav"
    scene imanibardate14
    with dissolve

    "Both of us hang up the phone and...I accept that tonight’s “silence” is going to be broken in even more ways than I initially expected."

    ima "So, uhh...looks like it’s just gonna be you and me tonight."

    scene imanibardate15
    with dissolve

    ima "Still down?"
    s "We’ve been alone a million times before. Why should this be any different?"
    ima "Exactly! This is just another night. Just two friends going out to the bar for drinks. Nothing weird about it unless we make it weird, right?"
    s "You’re starting to get close to making it weird, Imani."
    ima "No. {i}You’re{/i} making things weird by saying that {i}I’m{/i} starting to make things weird. Come on, Senpai. You should know better than that."
    s "..."
    ima "..."

    scene black
    with dissolve2

    ima "How about just...neither one of us talks until we have a drink in our hand. Cool?"
    s "Deal."

    "I take up Imani’s offer to remain quiet until we’re equipped with vials of liquid courage and revel in the return of a hastily departed silence."
    "It doesn’t last long, however, as we know these roads like the backs of our hands and have navigated to this exact bar time and time again."
    "Just never without anyone else."
    "And confronting that will be fine for me-"

    play sound "static.mp3"
    scene imanibardate16 with flash
    stop sound

    "But will it be fine for {i}Imani?{/i}"
    "Will {i}she{/i} be able to overlook her innate desire to fuck me in the same way that {i}I{/i} have taught myself how to bypass those urges and feelings in regard to her?"
    "Judging by her current demeanor, I’d say the answer is yes. I’d say that she {i}can{/i} do that."
    "But I may very well just be giving her the benefit of the doubt because she’s smarter and older than the majority of girls I deal with on a daily basis."
    "It’s easy to look at people like them and predict their next moves because the majority of them are just as predictable as girls that age are {i}meant{/i} to be."
    "But I still don’t know much about {i}Imani.{/i}"
    "I don’t know anything about the {i}way{/i} she thinks because I’ve yet to learn {i}what{/i} she thinks at all. "
    "And all signs point to this being a good opportunity to learn, but..."

    ima "Senpai..."

    "But I feel like we’re just going to wind up talking about {i}me{/i} again."

    s "What’s up?"
    ima "This isn’t so bad...is it? Just you and me here, I mean."
    s "Did you {i}expect{/i} it to be bad?"

    scene imanibardate17
    with dissolve

    ima "No! It’s just, like...this is different. You know? We see each other all the time, but...the context of {i}how{/i} we’re seeing each other makes things kind of...different. Ish."

    scene imanibardate18
    with dissolve

    s "I feel the same as always, pretty much."
    ima "..."
    ima "Is that because...you’ve already got someone who kind of...twists your world into a giant knot?"

    scene imanibardate19
    with dissolve

    s "A little clarification would probably be nice right now. I'm not sure how to interpret that."
    ima "I just mean, like..."
    ima "Well, look at it this way. A lot of the time, when people talk about knots, it’s with some kind of...{i}negative{/i} connotation."
    ima "Like...oh. My stomach is “in knots.” Or...I feel all “knotted up” inside. But what about all of the times where knots are {i}good?{/i}"
    s "Imani, how drunk are you right now?"

    scene imanibardate20
    with dissolve

    ima "I am {i}zero{/i} drunk, Senpai. We just got here. But, like...think about shoelaces. Or...shibari or something like that. There are a ton of situations where knots are a good thing."
    ima "They’re something that provides safety or security and...keeps shit in place."

    scene imanibardate21
    with dissolve

    ima "And, you know...frankly..."
    ima "I can’t think of anything more “secure” than dating an idol. "

    "Here we go..."

    ima "Niki Nakayama...{i}impressive.{/i}"
    ima "And here I thought you were going to marry her {i}sister{/i} one day."
    s "Her sister is a teenage girl. Did you actually think I was planning on marrying her?"
    ima "No. I’m just not great at talking about heavy subjects and wind up using sarcasm as a backbone sometimes. Please forgive me, Senpai. I’m still learning."

    scene imanibardate22
    with dissolve

    s "Well, at least we’ve got that in common."
    ima "We’ve got a lot in common. Just I’m the one who winds up having to do all of the heavy lifting since {i}I’m{/i} the extrovert here. "
    ima "The reality is though, Senpai...deep down, I don’t really {i}want{/i} to be."
    ima "It’d be nice just relaxing and not having to worry about how everyone looks at me or...what everyone is thinking all the time, but I haven’t really figured out how to make that happen just yet."
    ima "So instead, I keep things moving. Keep my expectations in line with the direction things are already flowing in and...just kind of...give things a push when they need to be pushed."
    s "Is this you telling me I need a “push?”"
    ima "Not at all. I like you the way you are. I don’t think people have to be perfect or...even {i}good{/i} for that matter."
    ima "Like, don’t get me wrong- I’d be much quicker to tie myself to someone who doesn’t go around ruining everyone’s lives than someone who {i}does-{/i}"
    ima "But I also think that reducing people to something as simplistic as the...history of their decisions concerning all things “morality” doesn’t paint the full picture."
    s "So...that wasn’t even remotely {i}close{/i} to you telling me I need a push. You’re either just demonstrably bad at explaining things or {i}I’m{/i} demonstrably bad at getting the point."

    scene imanibardate23
    with dissolve

    ima "It’s probably me. What I’m really saying is that if I vibe with somebody, I’m more inclined to overlook any disagreements we have concerning moral alignments or...anything like that."
    s "Sure, but...what does that have to do with Niki exactly? How did we get from {i}her{/i} to this?"

    scene imanibardate24
    with dissolve

    ima "..."
    s "..."
    ima "I don’t know."
    ima "I’ve got no fucking clue what I’m doing, Senpai."
    ima "It’s not even like I’m running in circles either. It’s like I’m lost somewhere in the middle of the track and I can’t even figure out how to get back onto it or...what direction I’m supposed to be running in."
    ima "But everyone seems to think it’ll just...click or something. Or they don’t realize I’m lost and assume I’m just pretending to be because it’ll make everyone laugh when..."
    ima "When the truth is...I want someone to take my hand and show me where to go or...or get lost {i}with{/i} me."
    ima "I just haven’t figured out how to stop...reflexively pulling away any time someone tries to reach out just yet."
    s "..."
    ima "If any of that sounded weird, you can just assume I’m already drunk."
    s "All of it sounded a little weird, but I’m not going to do that. Especially since you haven't taken a single sip of your drink since you last told me you {i}weren't{/i} drunk."
    s "Instead, I’m just going to ask if you’re okay."
    ima "I think so. I’ve probably just thrown myself into rant-mode because we don’t ever really do things like this alone and I’m excited to finally get to...{i}connect{/i} with you."
    ima "I’m just not sure if we’re really...{i}connecting{/i} the way I want. You know?..."
    s "..."

    play sound "static.mp3"
    scene imanibardate25 with flash
    stop sound

    ima "This...uh..."
    ima "Mm..."
    ima "Niki Nakayama...are you guys, like..."
    ima "What’s the deal?"

    "Imani begins to play with the tab on her beer can, flicking it and bending it to compensate for the lack of sound inside the bar or to just...soothe some sort of mental craving she’s having right now."
    "I can’t say for sure as, again, I have no clue what her deal is. But, of course, we’re talking about me again."
    "We’re talking about me because that’s all that ever happens and...and 99%% of the time, it’s all I want."
    "But despite these tinted glasses that I’ve been peering through in order to see her, I want to know {i}why{/i} she spends so much time agonizing over me when there is no reason to at all."
    "She doesn’t have to worry about Niki — she should worry about herself. About her dreams of helping children or the time she could spend on someone who {i}doesn’t{/i} mind sacrificing a friendship."

    s "The deal is that I love her."

    scene imanibardate26
    with dissolve

    ima "Mm..."

    "Her motions with the tab become more rapid...anxious. And I can sense that it’s only a few hard pulls from being snapped clean off of the aluminum."

    s "Do you want to hear more? Or does that suffice?"
    ima "Is she good to you? She seemed a little...bossy."
    s "She is. On both counts. Her bossiness is just a side effect of her archetype. In all actuality, she’s a very good person. And she cares about me more than I deserve."
    ima "Mm..."
    s "That’s not the answer you wanted to hear, was it?"
    ima "I’m just happy you’re happy, Senpai. It sounds like you two are a good match."
    ima "I’m probably just not really understanding her yet. Maybe in time. I don’t know."
    s "Do you {i}want{/i} to understand her? Because she might be open to coming to the bar sometime, you know. I could always invite her."
    ima "I..."
    ima "Yeah, I...don’t really want to get to know her."
    ima "Idols aren’t really my thing."
    ima "I’m glad you’re happy, though. Seriously. You deserve it."
    s "Do I really, though?"

    scene imanibardate27
    with dissolve

    ima "Yes...{i}of course{/i} you do. Even {i}if{/i} you’re corrupting the denizens of our poor classroom every single day, you’re still a human being. And we all deserve to feel loved in one way or another."
    s "Do you have anyone like that, Imani? Someone who makes you feel loved? And no, I’m not just speaking romantically. I mean in general."

    scene imanibardate28
    with dissolve

    ima "Come on, Senpai. Do you really think I’d be acting like this if I {i}did?{/i}"
    ima "I haven’t had anyone like that in...years. And even then, I'm pretty sure I only {i}believed{/i} I was loved and that...I’ve never really felt it the way you have."
    ima "I’m sorry for prying and...making you talk about stuff like your love life when we’re not really supposed to be doing that, but-"
    s "Do you really think I care about what we’re “supposed to be doing?” "
    s "I told you because I wanted to tell you. I wanted to share a piece of myself with you because I want you to do the same for me. That’s what friends do. Probably. "
    s "Honestly, I don’t have very many- so I can’t confirm that."
    ima "You and me both, Senpai. "
    ima "That’s just one more reason I...like being with you so much."
    s "..."
    ima "..."
    s "..."
    ima "..."
    s "Are you...going to say anything else?"
    ima "No..."
    ima "I was waiting to see what you’d do next. "
    ima "But I think I get it now."

    scene black
    with dissolve2
    stop music fadeout 8.0

    ima "And I think I need another drink."

    "The tab on her beer can finally breaks off."
    "And just as it does, the silence returns."
    "And the knots in my stomach protect me from nothing."

    $ renpy.end_replay()
    $ imanidate15p1 = True
    $ imani_love += 1

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    jump imanidate15p2

label imanidate15p2:
    scene imaniyumiapt1
    with dissolve2
    play music "thesleepingcity.mp3"

    "Neither one of us gets particularly inebriated tonight, but I still walk Imani home because I am a good person who does good things."
    "Just sometimes, the good things I do disguise themselves as bad ones. "
    "But not in the fact that I’ve necessarily done something {i}wrong.{/i} Just that I’ve done {i}something{/i} that’s led to some sort of unfortunate consequence. "
    "Like a good friend doubting herself or the...many people I’ve made inadvertently miserable by virtue of just existing in the way I have to."
    "As an icon of all things tempting."
    "An unworthy god among a congregation of blindly loyal servants."
    "Or a lecherous shepherd guiding a herd of prized sheep."
    "I doubt Imani sees me as any of those specifically-"
    "But when I’m face to face with her in a manner in which I {i}know{/i} she wants to invite me inside, I can’t help but open myself up to these self-aggrandizing approximations."

    ima "Sorry that nobody else was able to make it, Senpai. I...honestly had no idea that was going to happen. If I did, I wouldn’t have invited you."
    s "Why not?"
    ima "Well...you know, like...it’s just not a thing we normally do alone. "
    s "I’ve been to your house alone before and I think, if anything, {i}that{/i} would be even weirder. Going out to drink is completely normal."

    scene imaniyumiapt2
    with dissolve

    ima "Yeah...Yeah. You’re right. I don’t know what I’m saying. "
    ima "I just didn’t want you to assume that this was some kind of date or anything since you’re already, like...you know...{i}dating{/i} a superstar. And I kind of suck by comparison. "
    ima "In the least self-loathing way possible, though. Like, it’s less that I actually {i}suck{/i} and more that just...I’m not a famous idol. Or something."
    s "Imani, I’m not seeing Niki because she’s famous. I’m seeing her because she gets me. In a way that I don’t think anyone else really does yet. "
    ima "Well, it’s...not like you make it easy, Senpai. So kudos to her for that. Girl really did put the work in, I guess."
    s "She did. And a lot of it. But it’s exactly {i}that{/i} that makes me not worth whatever you’re beating yourself up over right now."
    ima "What are you talking about? I’m not beating myself up over anything, Senpai. You’re just imagining things."
    s "If {i}I’m{/i} just imagining things, that means {i}everyone{/i} is imagining things. You know that tonight wasn’t just an accident. Everyone bailed on purpose so the two of us would be alone."
    s "And if you want to keep pretending like that’s not the case and forcing yourself to not say anything that might make things weird between us, don’t. That’s not the kind of relationship I-"

    scene imaniyumiapt3
    with dissolve

    ima "Do you want to come inside?"
    s "..."

    scene imaniyumiapt4
    with dissolve

    ima "Never mind. Forget I said that."
    s "I’ve been inside before, Imani."
    ima "Not...like this, you haven’t. This is different."
    s "Imani...can I ask you something?"

    scene imaniyumiapt5
    with dissolve

    ima "Sure...yeah. "
    s "Do you think there’s something wrong with the way things are between us right now?"

    scene imaniyumiapt6
    with dissolve

    ima "What? No. That’s not it at all."
    s "Then...are you just not worried about that dynamic changing or something? "
    s "I’m just trying to figure out why {i}I’m{/i} the one who’s worried about ruining our relationship when I’m essentially always of the mindset that sex makes everything better."
    ima "I don’t...I don’t want to ruin our relationship, Senpai. You’re my best friend. Wakana too, of course. But I see you way more than her and the mere...{i}thought{/i} of that gets me out of bed some mornings."
    ima "And, to be totally honest, I {i}am{/i} worried about ruining that. I’ve been worried about it for a while. Why else would I have been so hesitant to have this discussion?"

    scene imaniyumiapt7
    with dissolve

    ima "The jig is up. I like you. We both know it. And there’s no reason to hide it anymore, so...I’m not going to bother trying. But if you don’t like me-"
    s "I do like you. Isn’t that obvious?"

    scene imaniyumiapt8
    with dissolve

    ima "What?! {i}No!{/i} I could have sworn you were signposting the exact opposite of that all night! "
    s "Yeah, that’s fair. I guess I’m kind of hard to understand at times."
    ima "You think?! Change your facial expression every once in a while or something! Leaving your feelings all up to guesswork can mess with a person’s head!"
    s "Yeah, but so can feelings as a whole. "
    ima "Don’t change the topic! Tell me more about how and why you like me!"
    s "You’re funny. And weird — but in a way that’s more entertaining than off-putting."
    s "You do virtually all of my work for me and, despite complaining about it, I know you kind of enjoy it. Plus, the way you pester me all the time is actually a little heartwarming now that I’ve gotten used to it."
    s "Or at least it {i}would{/i} be heartwarming if I actually had a...well, heart."

    scene imaniyumiapt9
    with dissolve

    s "You keep my life at a good level of chaotic, but counteract it by helping me organize things I’d never bother with on my own. And all of the girls seem to love you as well."
    s "I think you’re smart and driven and I respect that you don’t normally take shit from me. And that you’re not afraid to call me out on things I don’t apply myself to."
    s "You and Niki are a lot alike in that regard. She’s just a little more brutally honest and less {i}fun{/i} than you."
    s "Also, you’re extremely attractive and I masturbate to fantasies of you almost regularly."
    s "And I probably could have left that part out if I wanted, but I felt like this semi-rant was missing an element that did justice to your physical traits and that was just the first thing I thought of."
    ima "But Senpai, if you really feel that way about me, what is there to gain from just...keeping things the way they are?"

    scene imaniyumiapt10
    with dissolve

    s "It’s not about {i}gaining{/i} anything. It’s about not losing something."
    s "I understand that I’m in a unique position when I say this, but I can have almost {i}anyone{/i} as a partner if I want. "
    s "But there aren’t many people I can have as friends. "
    s "Let alone people like you, who I just...can’t really seem to find any issues with."
    s "Which is why I want to keep things the way they are. "
    s "I want to keep silently looking forward to seeing you in school without worrying about betraying you or hurting you which I know I {i}would{/i} if we were together. I can’t resist that."
    s "Keeping you at arm’s length is for the benefit of both of us in the long run as there’s just way too much to lose if we take the opposite route. And I don’t want to lose you."
    ima "..."
    s "Did any of that make sense?"
    ima "Yeah. This is just the first time I’ve ever been friend-zoned, so I’m not really sure how to respond."

    scene imaniyumiapt11
    with dissolve

    s "It’s also the first time I’ve ever friend-zoned anyone. So you can take solace in the fact that you’re not alone right now. And that you were also a first for me in a very roundabout, non-ideal way."
    ima "..."
    s "..."
    ima "..."
    s "How long do you plan on just looking at me without saying anything?"

    scene imaniyumiapt12
    with dissolve

    ima "Until I can figure out a way to ask you if you want to come inside and have friend-sex with me."

    scene imaniyumiapt13
    with dissolve

    y "Ew. You too?"
    ima "Y-Yumi! Hi! Whaaaaat are you doing here?!"
    y "Getting sick. And questioning what the fuck I must have done this time to make {i}both{/i} of my teachers come after me this late at night."
    ima "Nothing! Nothing at all! In fact...I was just talking about how we should be giving you extra credit since you’re such an amazing girl who would never repeat anything she just heard to anyone!"
    y "This another trap? Cause I already fell for the poem thing and I ain’t about to let a third teacher walk all over me."
    ima "Nonsense! I would never! In fact, why don’t all {i}three{/i} of us take a load off in my apartment so none of my neighbors assume I’m speaking inappropriately to teenagers?!"
    s "Imani, I don’t think Yumi wants to have friend-sex with us."
    y "For the first time in my life, I actually agree with him."

    scene imaniyumiapt14
    with dissolve
    play sound "dooropen.mp3"

    ima "Haha! Funny joke, you two! Come on in! The extra credit’s in here!"
    y "That’d be more convincing if it didn’t sound like somebody was tryin’ to lure me into a van with candy."
    s "Visiting your mom again?"
    y "She ain’t home. I just wanted something to eat. "
    s "Are you sure you don’t want to come inside with us?"
    y "That a joke? I ain’t ever been more sure of anything in my life."
    s "Please come inside, Yumi."

    scene imaniyumiapt15
    with dissolve

    y "What? {i}Why?{/i} All that’ll do is prevent you from addin’ one more notch to your belt. Assumin’ it ain’t already frayed to shit from all the other ones, that is."
    s "Please. As a favor to me."

    scene imaniyumiapt16
    with dissolve

    y "..."
    s "..."
    y "You actually...{i}don’t{/i} want to go in there. Do you?"
    s "It’ll only take a little while. Think of it as payment for the phone you’ve had all these years that is still, somehow, not paid off."
    y "Throw in another IC card and you’ve got a deal. I already used up the one the goth teacher gave me."
    s "Done."

    scene black
    with dissolve2

    y "{i}Hah...{/i}should’ve asked for more. That was too easy."

    "Yumi resignedly walks into Imani’s apartment and I dig deeper into the depths of my mind to figure out what’s going on with me as it’s...unlike anything I’ve felt before."

    scene imaniyumiapt17
    with dissolve2

    "By all accounts, Imani is one of the most morally correct people for me to {i}have{/i} a physical relationship with."
    "Our ages aren’t all that far apart...she’s not seeing anyone....we both {i}like{/i} each other. And, apart from the same romantic consequences that would befall {i}any{/i} relationship I enter, no one would get hurt."
    "Is it {i}because{/i} of the moral correctness that I feel so wrong about this?"
    "Is it {i}because{/i} there is no daughter, son, or distant relative that I’d be leading on in the process of fucking her?"
    "Or am I really just that desperate for someone to love me in a way different from the others?"
    "And if so...why?"
    "I don’t get it."
    "..."
    "I don’t get it."

    ima "So...we good? You’re not gonna, like...tweet about this or anything?"
    s "I’m pretty sure Yumi’s in the same social media boat as me. IE: she doesn’t give a shit."
    y "Yo, why the fuck does your place look all nice-ish while Yuki’s straight up sucks? Ain’t no cigarette smell or anything."
    ima "That’s...probably on account of me not smoking. But yeah! Your mom’s my neighbor! You should come visit more often or...or something."

    scene imaniyumiapt18
    with dissolve

    y "Chill. I ain’t gonna tell anybody shit. And  you don’t gotta worry about bein’ all nice to me to keep me from stickin’ my hands where they don’t belong."
    ima "Oh, thank God. Because having two secrets of mine under your belt is far too much power for me to just ignore."
    s "Two? What’s the first one?"

    scene imaniyumiapt19
    with dissolve

    ima "Nothing you need to be concerned about! Or {i}will{/i} be concerned about any time soon if our current rate of progress is at all indicative of the future!"

    scene imaniyumiapt20
    with dissolve

    ima "{i}Instead,{/i} why don’t we talk about you?! What’s new in the life of Yumi Yamaguchi? You...beat up anyone good lately? Or..."
    y "You say that as if I just go around pickin’ fights with whoever the fuck I want."
    ima "To be fair, I have significantly less experience with you than literally everyone else in the class on account of how frequently absent you are...So please forgive me if I’ve mischaracterized you."
    y "Ehh. You ain’t too far off, I guess. But I haven’t laid a finger on anybody since the Nodoka shit went down. Kinda just tryin’ to lay low at this point."
    ima "And how’s your mom? Is she doing well? "
    y "Fuck if I know. She can get hit by a car for all I care."

    scene imaniyumiapt21
    with dissolve

    ima "Jesus, girl. You ain’t gotta talk about your momma like that. That shit ain’t cool."
    y "Cooler than abandoning your daughter so you can go suck dick for heroin or whatever it was she did all those years away. I ain’t bitter, though. Shit happens."
    ima "I don’t know, Yumi. You sound pretty bitter. But I guess I might be too if those...circumstances are at all accurate."

    scene imaniyumiapt22
    with dissolve

    ima "There’s gotta be something-"
    y "Don’t touch me."

    scene imaniyumiapt23
    with dissolve

    ima "There’s gotta be something, though! Something you’re looking forward to, I mean. "
    ima "Like, yeah. Maybe the Dorm Wars weren’t a personal highlight for you on account of how you were a pawn in the second floor’s chess game...but Halloween’s right around the corner!"
    ima "Are you looking forward to that at all?"
    y "Why are you asking me so many questions when I already told you you don’t have to do this to get me to keep your secrets?"
    ima "I’m just trying to get to know you better! And also, Senpai and I are in a weird spot right now that we can totally ignore thanks to your presence and participation in this conversation."
    y "Halloween sucks. Christmas sucks. New Year's sucks. All of the holidays suck and I ain’t lookin’ forward to anything. That do the trick? Are your weird, adult problems solved now?"

    scene imaniyumiapt24
    with dissolve

    ima "Do you just {i}hate{/i} fun? Is that what your deal is?"
    y "Part of it, probably."
    s "She left out the part where Halloween is also her birthday. So I imagine she hates that one the most of all."

    scene imaniyumiapt25
    with dissolve

    y "Would it kill you to just, like...{i}not{/i} remember things about me? Cause that’d be doin’ me a huge favor, asshat."
    ima "Wait, is it really? How did I not know that?"
    y "{i}Nobody{/i} is supposed to know that because-"
    ima "We should do something to celebrate. We could get an extra cake for the Halloween party or something. "

    scene imaniyumiapt26
    with dissolve

    y "Because {i}that{/i} always happens. I don’t want to fucking celebrate my stupid ass birthday. It’s just a day. And the further away I am from the center of attention, the better."
    ima "Well damn, girl. Tell us how you really feel."
    y "Listen, can I leave now? I’m still hungry and I really didn’t wanna waste away my night in a creepy apartment with two creepy adults."
    ima "Senpai being creepy, I understand. {i}Me{/i} being creepy? That’s just wrong. I’m the lovable student teacher that everybody gets along with. I’m not allowed to be creepy."
    y "Nah, you’re pretty fuckin’ creepy. Just not nearly as bad as the guy next to you."
    s "Would you mind if I came with you? I left something in Yuki’s apartment last time I went over there."
    y "What is it? Just fuckin’ tell me and I’ll-"

    scene imaniyumiapt27
    with dissolve

    y "Wait. Yes. That thing. I remember now."
    y "You may come with me."
    s "Thanks. I should probably start heading home now anyway, so..."
    ima "You can just tell me if you don’t want to be here, Senpai. You don’t have to lie about it."

    scene imaniyumiapt28
    with dissolve

    s "Imani-"

    if day <= 4:
        ima "Actually, don’t even worry about it. I’ll see you in school tomorrow. "
    else:
        ima "Actually, don’t even worry about it. I’ll see you in school on Monday."

    ima "I had fun tonight. Sorry nobody else was able to turn up. Even if it was a...calculated absence on all of their behalves."
    ima "I’ll make sure it doesn’t happen again."
    s "You don’t-"
    ima "Just...go get your “thing.” And have a safe trip home. I’ll be back to normal the next time you see me. Promise."
    s "..."
    y "..."

    scene black
    with dissolve2

    s "{i}Hah...{/i}"
    s "Have a good night, Imani. "

    play sound "dooropen.mp3"

    "I leave the room with Yumi."
    "There are no parting words or anything like that."
    "But before she opens the door and heads into her mother’s apartment, she makes eye contact with me."
    "Her expression is complicated...and I can’t really tell what it means."
    "But if I had to take a guess-"
    "I think it was pity."

    scene bedroom_night
    with dissolve2

    "When I get home, I look in the mirror."
    "And I confirm that it was."
    "Then I..."
    "I just go to sleep."

    scene black
    with dissolve2
    stop music fadeout 8.0

    "That’s all I do."

    $ renpy.end_replay()
    $ imanidate15p2 = True
    $ imani_love += 1
    $ yumi_love += 1

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
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

label imanispecial15:
    scene black
    with dissolve2

    "{i}Somewhere in the urban district, beneath a shining star...{/i}"
    ".........."
    "......"
    "..."

    scene imaniwakarin1
    with dissolve2
    play music "summerwind.mp3"

    w "Hey, sorry I’m late. I ran into an issue with a pair of handcuffs."
    ima "No worries. Any time your punctuality takes a hit I kind of just assume it’s due to some BDSM-related mishap. Also, I invited Karin. Hope that’s cool."
    ka "Heeeey. That’s me. I’m the other girl from the swimsuit contest thing who also felt like it should have been canceled but wasn’t able to speak up because I want my sister to like me. Nice to meet you."
    w "Nice to meet you as well. Now go home. My quota for human contact today caps out at one person and Imani already counts as at least four."

    scene imaniwakarin2
    with dissolve

    ima "Yo, chill. Karin isn’t going anywhere. She still needs a Halloween costume too and she’s part of the “I know Imani is a monster underneath her clothes” club. "
    w "I actually like your scars. They add personality. But I suppose that is a double-edged sword as you already have too much of that to begin with."
    ka "You could have just introduced me as a member of the swim club too...that would have worked."
    ima "Yeah, maybe in the context of a situation where I’d be keeping my clothes on. But it’s not like I can just throw a hat on and go to this year’s party as “Hat Imani.”"
    ka "I think Hat Imani sounds cute. It’s like normal Imani just...there’s a hat. And it’s..."
    ka "The hat is on her."
    w "Is this what you wanted? If we needed someone awkward, we could have just invited Rika. At least she’s of age."

    scene imaniwakarin3
    with dissolve

    ka "I’m sorry. I’ll try to be better."
    ima "Damn it, Wakana. Now look what you’ve done. You’ve made the only wholesome girl in all of Kumon-mi sad. And if {i}you{/i} wind up being the one to lead her down a dark path, I won’t ever forgive you."
    w "Forgiveness be damned. I will not follow in the footsteps of you and Arakawa by spending what little free time I have with students. I have better things to do."
    ima "Bro, we’re just buying costumes. It’s not like we’re inviting her out to the bar."

    scene imaniwakarin4
    with dissolve

    ima "But hey, even if we were, she’d probably just bail on me last minute anyway since that is apparently what you guys do now."
    w "..."
    ima "Yeah, I’m looking at you."

    scene imaniwakarin5
    with dissolve

    w "I had nothing to do with that. It was Rika’s idea."
    ima "Mmmmmhm. Well, thanks. I’m sure it went down {i}exactly{/i} how she wanted it to."
    ka "Was there...some sort of issue recently? Is it something I’m allowed to know?"

    scene imaniwakarin6
    with dissolve

    ima "{i}Hah.{/i} There’s a guy I like, but the guy doesn’t like me. Or...{i}does{/i} like me, but also likes someone else. "
    ima "So he doesn’t want to like me any harder than he {i}currently{/i} likes me because it might make us like each other less. Even though I currently want him to like me so hard that it shatters my pelvis."
    ka "Adult relationships sound complicated. I didn’t even know that you {i}could{/i} like someone with...that amount of force."
    ima "Because, again, you are the only wholesome girl in this entire city. So make sure you don’t listen to anything Wakana says as her world view may accidentally gothify you."

    scene imaniwakarin7
    with dissolve

    w "Everything I do is for the greater good. Which is why the first place on our list today is one of my favorite shops."
    w "If I am going to gothify {i}anyone{/i} I would prefer it happens early before my medication begins to wear off."
    ima "Good. The sooner I can get away from these nine million Niki posters, the better."

    scene imaniwakarin8
    with dissolve

    ima "You hear that, Niki?! Just because you’re hot and talented doesn’t mean I have to like you! Get bent!"
    w "Oh, good. She has a rival now. Cute."
    ka "Wow. I had no idea Miss Imai hated pop music this much."
    w "I'm glad she does. It will make it easier to convert her into one of my people."

    scene black
    with dissolve

    w "Now, come. Both of you."
    ima "You haven’t seen the last of me, Niki! I’ll be back! "
    ka "Come on, Miss Imai. If you yell at the billboards any longer, people will think you’re crazy. Then no one will want to like you as hard as you apparently want to be liked."
    w "What was your name again? Karin?"
    ka "Yes! Hello!"
    w "Grab her."
    ka "What?"
    w "{i}Grab her.{/i} You’re tall and...powerful looking. And I am not about to be delayed by a woman too busy yelling at signs to remember we are here on a mission."
    ima "I’m coming, damn it! I just needed to get my midday fury out of the way first."

    "........."
    "......"
    "..."

    scene imaniwakarin9
    with dissolve2

    ka "Wow...everything here is so...{i}scary...{/i}"
    ima "It looks like a normal gothic lolita place to me."
    w "Yes, isn’t it wonderful?"
    ima "Now, I’m {i}all for{/i} trying on a bunch of random shit and looking horrible in like 99%% of it, but I’m not sure if I like the idea of people thinking my Halloween costume is just “Black Wakana.”"
    w "Why not? It’s better than “Hat Imani.”"

    scene imaniwakarin10
    with dissolve

    ka "I like Hat Imani! It’s like normal Imani, just-"
    w "With a hat. We know. Now, go run along and look at all of the dresses. "

    scene imaniwakarin11
    with dissolve

    ka "Okay!"
    w "And whatever you do, don’t go into the back room. That is for adults only. "
    ka "Got it! I like rules!"
    ima "Wakana, what kind of place did you take me to that has an “adults only” back room? I thought we were costume shopping."

    scene imaniwakarin12
    with dissolve

    w "We are. It just also happens to be in the same place where I shop for chains and lingerie for Osako’s secret boudoir photo shoots. "
    ima "And which one of you is the photographer?"
    w "Yes."
    ima "..."
    w "..."

    scene imaniwakarin13
    with dissolve

    ima "God damn I need to get laid."
    w "Well, that’s on you for not taking your new rival up on her offer. You had your chance and squandered it."
    ima "Yeah, I know. The six hours of listening to the two of them go at it is etched so deep into my memory at this point that I can pretty much replay the whole night in my head."
    w "Lucky."
    ima "Wakana, is it weird to ask somebody to have friend-sex with you?"
    w "Well, you’ve certainly chosen a strange time to start hitting on me."

    scene imaniwakarin14
    with dissolve

    ima "Not {i}you.{/i} Senpai."
    w "You asked Arakawa to have sex with you?"
    ima "I’m not {i}proud{/i} of it, okay? I just wanted to...test how much he’s actually {i}into{/i} this idol friend of his. "
    w "But...you would have followed through with it if he’d agreed, yes?"

    scene imaniwakarin15
    with dissolve

    ima "Oh {i}God{/i} yeah. I ain’t no baby-back bitch. "
    w "Then...I take it you’ve already revealed your {i}body{/i} to him?"

    scene imaniwakarin16
    with dissolve

    ima "I...have not."
    w "Were you hoping he’d just...keep his eyes closed the entire time, then? Or are you so desperate for sex at this point that you’re willing to just overlook your self-image issues if it means relieving your tension?"

    scene imaniwakarin17
    with dissolve

    ima "The former. And if he did not agree, I would have blindfolded him. I have several bandanas I have been saving for such an occasion."
    w "You’re really deep into this, aren’t you?"

    scene imaniwakarin18
    with dissolve

    ima "Yeah, but it’s not like I {i}want{/i} to be. I love what he and I have right now. You know that. I just...fucking..."

    scene imaniwakarin19
    with dissolve

    ima "Ughhhhhhhhhhh! Why did I ask him that?! I made everything wooooooorse!"
    w "I’m sure Arakawa didn’t mind...If anything, I imagine he took it as a compliment."

    scene imaniwakarin20
    with dissolve

    w "Just...keep in mind that you aren’t the problem. He {i}did{/i} say he likes you, didn’t he?"
    ima "Yeah...just not hard enough."
    w "The timing is just wrong, Imani. That happens sometimes. It’s not as if your life is over."

    scene imaniwakarin19
    with dissolve

    ima "Ughhhhhhhh but it feels like it iiiiiiiiiis."
    w "Moaning and groaning will get you nowhere. But do you know what {i}will?{/i}"

    scene imaniwakarin21
    with dissolve

    ima "Putting on a dress that’s way too big for me and then having you repeatedly tell me that I’d make a good goth when we all know I wouldn’t?"
    w "{i}Exactly.{/i}"

    scene black
    with dissolve2

    ima "{i}Hah...{/i}"
    ima "Black Wakana here I come..."

    "........."
    "......"
    "..."

    scene imaniwakarin22
    with dissolve2

    ima "You know what? It’s probably {i}good{/i} that Senpai turned down the friend-sex. "
    w "Christ, are we still on this? I thought we were done."
    ima "Think about it, though. Like, he’s boning an {i}idol.{/i} And he’s not {i}just{/i} boning her, he’s boning her {i}a lot.{/i} I don’t have that kind of stamina. No way I’d be able to go that long."
    ima "So, all things considered, if he {i}did{/i} screw me, he’d probably just think, “Ehh. I’ve had better. Also, what’s with the blindfold?” and then it would just end."
    ima "At least this way, we get to stay friends. And I can just keep hoping they break up or something and I can get him on the rebound when his standards are lower."
    w "Are you done? Can we move on now?"

    scene imaniwakarin23
    with dissolve

    ima "Well, {i}excuse me,{/i} princess. I didn’t realize there was a limit on how long I was allowed to talk about my {i}feelings{/i} for."
    w "There’s no strict limit. But a time must come when you think to yourself, “You know what? I’ve been speaking for 75%% of the day and it is possible my friend might have something to say as well.”"

    scene imaniwakarin24
    with dissolve

    ima "Well, do you?"
    w "Do you not wear underwear with that outfit?"
    ima "That’s what you want to talk about? When I do and don’t wear underwear?"
    w "It wasn’t originally. But I can’t help but bring it up now that you’re exposing your genitals to me."
    ima "Well, ignoring my genitals, what was it you had to say?"
    w "..."
    w "I can’t remember."

    scene imaniwakarin25
    with dissolve

    ima "That feeling when I’m closer to friend-sex with you than I am with Senpai."
    w "Wait, I remember now. And it should still pique your interest to some extent as Arakawa {i}is{/i} still a part of it."

    scene imaniwakarin26
    with fade

    ima "If it has anything to do with him having sex with anyone other than me, I don’t want to hear it. I know too much already. "
    w "Rest assured, it does not. In fact, it has more to do with his niece than it does with him."
    ima "Ami? Why do you want to talk about Ami? "
    w "You’re aware that she won my poetry contest, correct?"
    ima "I am. I’m {i}shocked{/i} as well given how she fares in every subject {i}other{/i} than creative writing, but still. I’m aware."
    w "And are you familiar with a poet who goes by the name “The Girl Who Cannot Breathe?”"
    ima "That, I am not. Poetry isn’t really one of my areas of expertise the way it is for you. But why do you ask? Do you think Ami may have been plagiarizing or something?"

    scene imaniwakarin27
    with dissolve

    w "It’s hard to say. The situation is...complicated."
    ima "Complicated? "
    w "Before I say any more, I need you to promise that you won’t repeat any of this to Arakawa. He’s rather...touchy when it comes to this subject."

    scene imaniwakarin28
    with fade

    ima "Senpai is {i}touchy{/i} with something? But his whole thing is never being able to show any emotion about {i}anything.{/i}"
    w "Yes, well...I seem to have found the one area where that is not the case."
    ima "Then, yeah. I won’t say anything to him. What’s up?"
    w "Well, Ami’s work is {i}remarkably{/i} similar to that of The Girl Who Cannot Breathe. So much so that I {i}did{/i} initially worry that plagiarism could be at play."
    ima "But now you think it’s not?"
    ka "Miss Imai? Miss Watabe? Can I come in?"

    scene imaniwakarin29
    with dissolve

    ima "Yeah, you’re good."

    scene imaniwakarin30
    with dissolve

    ka "Thanks. And sorry to be a Debbie Downer, but I don’t think I’m going to find anything here. It seems like everything is mostly tailored to more...petite girls. "
    ima "I haven’t even tried anything on yet. But go on, Wakana. Finish what you wanted to say."
    w "Thank you. What I was in the process of saying is that I haven’t exactly {i}ruled out{/i} plagiarism just yet, but I’m beginning to believe that this poet might actually be her mother."
    ima "And that’s...an issue?"
    w "It wouldn’t be an issue if it was just {i}any{/i} poet. But the one in question had a remarkably grim view of the world that I fear may be...tainting one of your students. In an unhealthy way."
    ima "Unhealthy how? Because if this is actually as dangerous as you’re making it sound, I should probably talk to her."
    w "I’m glad you’re of the same mindset as me while Arakawa couldn’t be more opposed if he tried."
    w "But what I mean by “unhealthy” is that The Girl Who Cannot Breathe makes Poe’s {i}tastes{/i} seem tame by comparison."

    scene imaniwakarin31
    with dissolve

    ima "Oh damn. That guy was into some weird shit too."
    w "He was. But his tastes were not toxic, whereas the poet in question wanted people to feel the way she felt and empathize with these...disgusting, horrific ideals that just..."
    w "They’re things that are okay to admire from afar and through a critical lens where we can sit back and cherry pick where the flaws in her manner of thinking were."
    w "But if these thoughts, ideals, and mannerisms are being replicated, which I {i}believe{/i} seems to be the case, there’s cause for concern in the spread of this parasitic mindset as a whole."
    w "And I think we need to get to her before it becomes too much to bear. "
    ima "Got it. I’ll read some of her stuff when I get home tonight to get a better idea of what you’re talking about. Then, we can figure out where to go from there."
    ima "You’re absolutely positive this is serious though, right? Because {i}anything{/i} involving her parents isn't something we should bring up unless we absolutely {i}have{/i} to."
    w "I think it {i}could{/i} be. But that’s all we should need in order to intervene if Arakawa would rather let his niece just fall into a bottomless pit of debauchery without actually trying to stop it."

    scene imaniwakarin32
    with dissolve

    ka "Wait, have you guys been talking about {i}Ami’s{/i} mom this whole time?"
    ima "Why? You don’t know something, do you?"

    play sound "static.mp3"
    scene imaniwakarin33 with flash
    stop sound

    ka "I don’t, but my dad might. He went to school with her."
    w "{i}What?{/i}"

    scene imaniwakarin34
    with dissolve

    ka "Is Ami okay? All that stuff about unhealthy ideals and...parasitic mindsets and stuff doesn’t really sound like-"
    w "Karin, how sure are you about this? How do you know?"

    scene imaniwakarin35
    with dissolve

    ka "I was showing my family pictures from the beach trip and my dad said Ami looked almost identical to a girl that used to be in his class."
    ka "They didn’t have the same last name, so there was no way of being 100%% sure. But he seemed pretty adamant that she might be her daughter."
    ka "I was planning on just leaving it at that since Ami’s really sensitive about stuff involving her parents, but if you really think she’s in trouble, I can try to-"

    scene imaniwakarin36
    with dissolve

    ima "Don’t worry about Ami for now. Let’s leave her out of this until we have a little more to go off of."

    scene imaniwakarin37
    with dissolve

    w "Karin, can you provide me with your father’s phone number? I’d like to speak with him about this if that’s okay."
    ka "Yeah...if that will help, sure. I’ll do anything I can."

    scene black
    with dissolve2
    stop music fadeout 10.0

    ima "That’s all you need to worry about for now, Karin. Wakana and I will take it from here."
    w "Imani is correct. But please, his number. "
    ka "Oh, right. It’s-"

    $ renpy.end_replay()
    $ imanispecial15 = True

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label imanispring1:
    scene imanionthebeach1
    with dissolve3

    "We move closer to the water, but not close enough for it to catch us too."
    "Part of me wishes that it would — but that the water would bend in a way that spares the girl beside me so I can witness its tidal wrath in a manner that renders me permanently breathless."
    "Suffice it to say, I’d take that over her and everyone else always emptying out my lungs."
    "Even when it’s quiet like this, when our minds are both so obviously elsewhere, I’m always {i}aware.{/i}"
    "Of how easily she could suffocate me..."
    "Of how her hands, clasped tightly around her knees, feel more like they’re curled around my neck. And how fighting a war against myself has made me too exhausted to even ask her to stop."

    play music "hometown.mp3"

    ima "Well...looks like it’s just you and me again."
    s "Guess so."
    ima "You worried too?"
    s "They’ll figure it out."
    ima "I think so too. "
    ima "I’m sure it’ll happen if we just keep telling ourselves that."
    s "It’s typically the opposite in my experience."
    ima "Yeah...same."
    ima "Maybe we should keep telling ourselves that they’re going to break up then? If fate and hope and all those other vague, optimistic adjectives are so commonly in disagreement with us, I mean."
    s "I think doing that would just make us bad friends."
    ima "True..."
    ima "Guess we’re kind of fucked either way then, huh?"
    s "Guess so. But at the end of the day, it’s those two who are way more fucked than either of us right now. We’re only fucked by-proxy."
    ima "Well, hey. I’d take that over not getting fucked at all, if you know what I mean."
    s "..."

    scene imanionthebeach2
    with dissolve

    ima "Uhh...just to clarify, that was supposed to be more of a joke than one more act of pressuring you into screwing me. Just...trying to lighten the mood."
    s "I know. Plus, even if I {i}did{/i} take that the wrong way, you’d get to fall back on the excuse of being drunk. You can’t lose."

    scene imanionthebeach3
    with dissolve

    ima "Mm..."
    ima "I guess I am a little tipsy, yeah. I was kind of just hamming it up for Wakana’s sake, though."

    scene imanionthebeach4
    with dissolve

    ima "You felt it too, right? How...I don’t know...{i}fragile{/i} she seemed? "
    s "I’m not sure I would have if you didn’t point something out when we first got here. She’s even better at hiding her feelings than I am and I’ve essentially built my entire character around that."
    ima "Well, yeah. You two are really similar."

    scene imanionthebeach5
    with dissolve

    ima "Talented, gloomy intellectuals who make it hard for you to get close to them...but also the type of people who will silently cherish you for the rest of your life whether you want them to or not."
    ima "I wish I met you sooner. Both of you. I’d have loved having people like that growing up."

    scene imanionthebeach6
    with dissolve

    s "..."
    ima "..."
    ima "How are you doing, Senpai? Like...{i}really{/i} doing?"
    s "I’m not really sure."
    s "“Confused” is probably the best word right now."

    scene imanionthebeach7
    with dissolve

    ima "About what?"
    s "It’s hard to say. Leaving the house is like playing a game of roulette at this point."
    s "Sometimes, something good will happen. Sometimes, something terrible. But it’s those terrible days I focus on the most because there’s like a...voice in the back of my mind telling me that’s what I deserve."
    s "At the same time, though, I’m trying to change for Ami’s sake. And that’s...hard. I’m not good when it comes to changing. "
    ima "For what it’s worth, Senpai...I think you’ve changed a lot since you left school. It’s not normal for you to just tell me things without putting up some sort of fight first."
    s "I don’t have the energy to fight anymore. All I want to do is sleep."
    ima "Senpai. Look at me for a second."

    scene imanionthebeach8
    with dissolve

    s "..."
    ima "I got you."
    ima "Okay?"
    s "I know..."
    s "Everyone does. "
    ima "Yeah, but I’m not everyone. I’m your loyal kouhai and best friend who can be anything you need her to be. Just say the word and I’ll do it. "
    s "Imani-"
    ima "Need some cash for dinner? I got you. Someone to walk the dog you don’t have? Again, I got you."
    s "Imani-"
    ima "Quickie in the closet before class? {i}I got you, man.{/i}"
    s "Imani, can I ask you something?"
    ima "Of course, Senpai. You can ask me anything."
    s "Why don’t you ever wear a swimsuit?"

    scene imanionthebeach9
    with dissolve2

    ima "Uh..."
    ima "Is...{i}that{/i} really relevant right now? I thought you were in the process of like, telling me about your feelings and stuff? "

    scene imanionthebeach10
    with dissolve

    s "Then I {i}feel{/i} like there’s a part of you I’m still missing — something you’re not telling me because you’re worried of how I’ll react. And I don’t think that’s really fair."
    ima "I mean...how is it unfair? You do the same shit, Senpai."
    s "I know...I have a lot to work on. "
    s "But I {i}want{/i} to tell you all of those things because I want you to understand the type of person you are to me. I want to be a better friend. I just...haven’t figured out {i}how{/i} yet."

    scene imanionthebeach11
    with dissolve

    ima "Well, it’s the same for me...Just {i}my{/i} thing doesn’t really have anything to do with our friendship. "
    s "Of course it does. Not telling me shows that you don’t fully trust me."
    ima "Trust doesn’t have anything to do with it, okay? I know you won’t think any differently of me. I’m just...embarrassed, I guess. Or maybe, like...ashamed? I don’t know. "
    ima "I don’t like swimsuits. I don’t like...revealing myself. "
    s "And I don’t like voicing my problems to people but that’s practically all I’ve been doing lately."
    s "Also, you’d kind of {i}have{/i} to reveal your body to me if we ever had sex. So...there’s that."

    scene imanionthebeach12
    with dissolve

    ima "Not if we keep the lights off!~"
    ima "But also, if we kept the lights off, you might not be able to find me at all and would wind up fucking my couch or something. Which would be wild since I don’t even have a couch."
    s "..."
    ima "..."

    scene imanionthebeach13
    with dissolve

    ima "{i}Hah...{/i}"
    ima "Okay...I’ll tell you."
    ima "But I have a condition."
    s "And what’s that?"

    scene black
    with dissolve2

    ima "You can’t say anything."
    s "I’m not going to tell anyone, Imani. I-"
    ima "No- I don’t mean it like that, Senpai. I mean...I want you to just...sit there and listen. No sympathy or...encouragement or...anything like that. I just want to get it over with. "

    "Imani gets up and heads over to where the water meets the land."

    scene imanionthebeach14
    with dissolve2

    "The moonlight accentuates her beauty, but I know it’s fleeting as I can tell that she is about to do everything in her power to cast one more shadow on it."

    ima "I’ll also be expecting at least one deep, dark secret from you in return. Got it?"
    s "You mean one you {i}haven’t{/i} probably already heard from Wakana and Osako?"

    scene imanionthebeach15
    with dissolve

    ima "Senpai, I-"
    s "No. If I’m not going to comment on your thing, you’re not going to comment on mine. That’s {i}my{/i} condition."

    scene imanionthebeach16
    with dissolve

    ima "Mm...okay. Fair enough. "
    ima "Welcome to Imani Imai’s impromptu story time...she says, pretending to have not rehearsed this conversation a hundred times already."

    scene imanionthebeach17
    with dissolve

    ima "So, you may not have noticed this as it’s really hard to pick up on, but I’m actually black."
    s "What? Really?"
    ima "Shush. No jokes either. Let me use them all to clear the air."
    ima "So yes, in a shocking turn of events, I {i}am{/i} black. But, as I’ve mentioned in the past, I’m half-Japanese as well."
    ima "A bastard child, if you will. A product of my mother’s infidelity and the insatiable lust of a foreign tourist who didn’t know how to pull out on time."

    scene imanionthebeach18
    with dissolve

    ima "Despite all of that, though...despite knowing that {i}none{/i} of his blood flowed within me, my father raised me as if I was his own."
    ima "He taught me about God....How all men and women are created equal and how each and every one of them is deserving of love. And that really stuck with me. Sans the God part. "
    ima "I just wish it stuck with his other children."

    scene imanionthebeach19
    with dissolve

    ima "You see...they never saw me the way he did. And they spared no effort at all in reminding me of that every chance they got. All behind the scenes, though. At least at first."
    ima "It was only a matter of time until everyone in school knew what I really was. Which meant it was only a matter of time until my mother started getting shit as well. And rightly so, might I add."

    scene imanionthebeach20
    with dissolve

    ima "You know, the only way I’ve ever really related to her at all was in the fact that we were both relentlessly trashed by our peers over a one night stand she made. "
    ima "Just {i}I{/i} wasn’t really there to do anything about it on account of still being a little Japanese tadpole at the time."
    ima "But regardless, I was bullied. She was bullied. And every day, my father would pull me aside and reassure me that this was only temporary."
    ima "That I was the same as everyone else and that they would all see that one day."
    ima "So I’d smile. Tell him I love him — which I did. I loved him {i}so{/i} much. And in hindsight, he’s probably the only thing that kept me going. "

    scene imanionthebeach19
    with dissolve

    ima "It started off with just name calling. Sansa ni...idiot. Ko’hweni...useless. Ahbwah...animal. Ashawo...whore."
    ima "And my personal favorite, ching chong fuo, which is a Twi slur for the Chinese. Fucking morons didn’t even know what type of Asian I was. "

    scene imanionthebeach20
    with dissolve

    ima "Ignoring insults is easy, though. So I focused more on educating myself than giving into all of the bullying since I wanted to make my father proud. "
    ima "But, here’s a thing I wish I knew sooner."

    scene imanionthebeach21
    with dissolve

    ima "Bullies {i}really{/i} don’t like it when you’re smart."

    scene imanionthebeach22
    with dissolve

    ima "One day, a bunch of kids from my school got together for a party to celebrate the end of the year. And, being the stupid and fearless specimen I am, I decided to go check it out."
    ima "I mean, it wasn’t like I didn’t have {i}any{/i} friends. There were a handful who’d stick up for me from time to time before tapering off from the consequent ostracization they’d receive in return."
    ima "So I found a few of them, got some food, got some drinks...started talking. And then there was this boy who came up to me. "
    ima "His name was Kwesi — popular kid. Some relation to the mayor or...some other comparable noteworthy position like that. And we started talking."
    ima "He told me how beautiful my eyes were...refilled my drinks and wound up buying me dessert from some stall not far from where all of us were hanging out."
    ima "He seemed nice. And it was a party, so I thought...what the hell? I’m gonna let this guy run some bases."
    ima "I’d already messed around with some other boys by then, so it’s not like I was totally inexperienced or anything."
    ima "So he takes me back to his place, right? Really nice house up on a hill that overlooked the rest of the village. I still remember how beautiful the lights were from the window of his bedroom."

    scene imanionthebeach23
    with dissolve

    ima "Unfortunately, that memory is somewhat soiled for me by what comes after."

    scene imanionthebeach24
    with dissolve

    ima "Which brings us back to the main question. {i}Why don’t I ever wear a swimsuit?{/i} And unfortunately, the answer kind of sucks."

    scene imanionthebeach25
    with dissolve

    ima "Kwesi tied me up. I agreed, thinking it might be fun. But I probably {i}wouldn’t{/i} have agreed had I known that he would subsequently invite another six of his friends into the room."
    ima "One of them was my brother."
    ima "And so I immediately looked at him with tears welling up in my eyes, knowing that there was {i}no way in hell{/i} that this wasn’t going to end horribly for me. But that motherfucker just {i}looked away...{/i}"

    scene imanionthebeach26
    with dissolve

    ima "They used scissors to cut off my clothes...wrote some things on my body I never bothered looking at since I’d already heard every insult possible by then. But that was just the beginning."
    ima "And leaving out the middle part, which I’m not going to burden you with, all that’s left is the grand finale."

    scene imanionthebeach27
    with dissolve

    ima "And the reason I like it best in the dark. "
    ima "One of Kwesi’s friends boiled some water. A lot of it. Can’t remember why specifically, but I think it had something to do with not being able to get the writing off."
    ima "They threw it at me. Several pots worth, to be exact. One boy even used an electric kettle. Like, for real man?"

    scene imanionthebeach18
    with dissolve

    ima "And yeah! Turns out the human body handles boiling water just as well as you’d expect it to. And the evidence of that is written all over me. "

    scene imanionthebeach26
    with dissolve

    ima "It wasn’t until the damage had already been done that they realized they’d gone too far. Well...one of them, at least."
    ima "Maybe the words of my father just took a little longer to reach him than they should have, but my brother eventually ran off to call for help."
    ima "I spent three weeks in the hospital after that. And while I don’t look nearly as bad now as I did the first few years, I still can’t look at myself without thinking of what happened that night."

    scene imanionthebeach27
    with dissolve

    ima "At least {i}one{/i} good thing came of it, though."
    ima "When school started the next year...no one ever bullied me again."
    s "..."
    ima "Thank you for remaining quiet and not battering me with sympathy. I appreciate it."
    s "May I speak now?"

    scene imanionthebeach16
    with dissolve

    ima "Yes, Senpai. You may speak."
    s "Did you bring it with you?"
    ima "..."
    s "..."
    ima "{i}Yes...{/i}"

    scene black
    with dissolve2

    s "Can you show me?"
    ima "..."
    s "..."
    ima "{i}Yes...{/i}"

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ imanispring1 = True

    jump imanispring2

label imanispring2:
    scene fourscompany1
    with dissolve2

    ima "Uhh...Senpai?"
    s "Yeah?"
    ima "So, remember how I got wrapped up in the emotional dialogue back on the beach and agreed to show you my swimsuit? Is it too late to take that back?"
    s "You’ve come this far. What will you gain by keeping things the same way they have been?"
    ima "I mean, it’s less about {i}gaining{/i} and more about just not losing anything. I’ve still got a little bit of dignity left, you know? Like, do I {i}really{/i} want to be stripping for my superior?"
    s "I’m just a friend right now, Imani. And I’m a friend who wants to see you the way you really are."
    ima "But who we {i}really{/i} are is all about what’s on the inside, right? Which means I get to keep my clothes on."
    s "Just come out, Imani. "
    ima "Ugghhhh...give me another minute. I’ve got matching earrings I have to find first."

    "So, we’re back."
    "Wakana and Osako haven’t returned yet. And based on whatever the result of their talk may be, I’m not sure if they {i}will.{/i}"
    "I don’t have much to say about Imani’s story. "
    "I mean...what {i}could{/i} I say that wouldn’t just make it seem like I’m jumping through hoops to be able to relate to her?"
    "And since I can’t even begin to imagine what she went through back then...I won’t."
    "I’ll keep doing what I’ve been doing from the start in seeing her not as an animal, but as one of the most driven and beautiful people I’ve ever come across."
    "Nothing changes after today."
    "Well..."
    "Something might."
    "But it’s something I’ve been silently agonizing over for the last several hours and there’s no point in telling you when you’ll find out soon enough."

    play sound "slidedoor.mp3"

    ima "..."

    "She exits the bedroom...but she asked me to face the entrance while she got changed so I wouldn’t wind up seeing her before she’s ready."
    "But knowing Imani, she might just stand behind me for the rest of the night."
    "I really hope she won’t, though. I want to see with my own two eyes what haunts her more than anything."
    "Our true colors come out when we have to face our fears, you know. And tonight I learned that the reason she’s so vibrant is because she carries hers with her every minute of every day. But never in their purest form."
    "So while one door opened behind me just a few seconds ago, another one opened in the back of my mind."
    "I can’t see what’s inside. I need a light to guide me."

    ima "Okay...here I come."

    "So I will carry her with me — to places I have only dreamt of reaching — in hopes that one day, I will be vibrant too."

    scene fourscompany2
    with dissolve2

    ima "Y...Yo."
    s "I’m proud of you, Imani."

    scene fourscompany3
    with dissolve

    ima "Oh, shut up...If I wanted you to get all sappy on me, I’d have let you speak when I was force-feeding you my  sob story on the beach."
    s "I won’t say any more...just that I’m proud."

    scene fourscompany4
    with dissolve

    ima "Th...Thank you, Senpai..."
    ima "If only I’d have had the guts to show you sooner. Maybe then we could have gone swimming today? We sure had enough time to kill."
    s "I’m not much of a swimmer. I wouldn’t mind watching you, though."

    scene fourscompany5
    with dissolve

    ima "No thanks. It’s a little worse from behind. This is...more than enough for now."
    s "I’m not the first to know, am I?"

    scene fourscompany6
    with dissolve

    ima "The rest of our friend group knows since we’ve gone to the bathhouse together. Other than you guys, though...there’s Futaba, Yumi, and Ayane."
    s "One of those things is not like the other."

    scene fourscompany4
    with dissolve

    ima "If you’re referring to Yumi, she walked in on me getting changed a while back. Ayane found out the same way in the locker room a few months ago, but...she didn’t even react so...I don’t know if she really {i}saw?{/i}"
    s "Nah, she’s just the type of girl who wouldn’t react even if she {i}did.{/i} What about Futaba, though? What’d she have to say?"

    scene fourscompany7
    with dissolve

    ima "You’re worried about her too, huh?"
    s "I never said that. "
    ima "Yeah, but I can already tell you’re thinking, “Hey! Two girls with body issues. They can probably get along.” And to that...you’re right. Kind of."
    ima "Our issues are a little different, but we did share a sentimental and very nude moment together in which we reassured one another of our respective beauty."
    ima "Oh, and also, we held a scavenger hunt for the Dorm Wars this year and she chose me when her card had “something beautiful” on it. I died a little. I love her."
    s "Keep looking out for her, please. I’ve been trying to help her with that forever and I’ve made virtually no progress whatsoever."
    ima "Don’t worry, Senpai. I’m looking after everyone. Everyone who will {i}let{/i} me, that is."
    s "What kind of man would I be if I let you look after me on {i}top{/i} of everyone else? You’ve got enough on your plate."
    ima "Stop that."
    s "Stop what?"
    ima "That whole “I don’t want to burden you” crap. I told you I got you, didn’t I?"
    s "Yeah..."
    s "I’ve got you too."

    scene fourscompany8
    with dissolve

    ima "Thanks..."
    s "..."
    ima "..."

    scene fourscompany9
    with dissolve
    stop music fadeout 10.0

    ima "Oh! I got so wrapped up in sentimentality that I almost forgot to ask. How do you like the swimsuit? "
    s "It’s beautiful. Now, take it off."
    ima "Thanks! I actually found this business downtown that-"

    scene fourscompany10
    with dissolve

    ima "Wait, what?"

    play sound "slidedoor.mp3"
    scene fourscompany11
    with dissolve

    w "The man said “take it off,” damn it!"
    ima "Wakana?!"
    os "Wakana, don’t interrupt them! Things were finally going somewhere!"
    ima "Wha- where did you two even come from?!"

    scene fourscompany12
    with dissolve
    play music "asobeatsex4.mp3"

    w "Like hell things were going somewhere! These two are so destined for abstinence that they’d have talked themselves right out of it! Strip!"
    ima "Wha...no?!?! I heard what he said too, but...Senpai clearly meant something else! He probably just wants a better look at my body since it’s like...fifty percent art project!"
    s "I can get a better look at it while going down on you."

    scene fourscompany13
    with dissolve

    ima "While doing {i}what?!?!{/i}"
    w "Yes, Arakawa! You’ve finally chosen the correct moment to be a depraved son of a bitch!"
    ima "Senpai, seriously?! Isn’t this too soon?!"

    scene fourscompany14
    with dissolve

    w "Too soon?! You’ve been fantasizing about this moment since you first met! And you’ve been complaining about him not screwing you for even longer!"
    ima "That’s not even possible! That was also before he agreed and now I’m all nervous!"

    scene black
    with dissolve2

    w "Be nervous another time! Because I’ll be damned if I let you miss out on this opportunity and have to listen to you bitch about it for the {i}next{/i} seven years!"
    ima "Wha- where are you pushing me?!"
    w "The bedroom! Arakawa, come!"
    s "I feel like this is getting a little too close to-"
    w "Shut the fuck up and get over here!"
    s "Sorry, coming."
    os "Ugh...do we have anything left to drink?"

    scene fourscompany15
    with dissolve2

    "Osako and I follow Wakana as she somehow manages to force Imani into the bedroom, but I’m not quite sure if she’s accomplished this thanks to her new painkillers or the power of friendship."
    "I’m leaning toward the latter, to be honest. Because I’m sure some of it was just diversionary, but Wakana’s been more gung-ho about me hooking up with Imani than {i}Imani{/i} has today."
    "And I just don’t have it in me to refuse her anymore."
    "Yes, I wanted a friend. Yes, I wanted someone to be by my side {i}without{/i} having to fall back on sex. And yes, I wanted Imani to be that person because I think she’s capable of so much more {i}without{/i} me."
    "But that sort of multi-leveled thinking has never even come {i}close{/i} to working for me since distancing myself from {i}anyone{/i} seems nigh fucking impossible."
    "So I think back to Ayane...I think back to Chika...I think back to Makoto and Futaba and realize that some of the most important relationships in my life have {i}stemmed{/i} from diving headfirst into sex."
    "Did I really fool myself into thinking I could do things differently with her? It was never going to work that way."
    "{i}This{/i} is what I’m good for and {i}this{/i} is what I know how to do. Neglecting that by thinking I know what’s better for her or that I’m an actual person with person-like needs is pointless."
    "It’s {i}all{/i} pointless."
    "So I will now spread her legs and bring her to orgasm with my mouth in act of apologetic submission."
    "It’s only right, you know."

    ima "Chill the fuck out, yo! You’re gonna rip it!"
    w "I wouldn’t have to rip it at all if you’d just take it off! "
    ima "You’re messin’ with the wrong girl, Wakana! HR will hear about this!"
    w "Well, we’ll see if you still want to call them {i}after{/i} Arakawa puts his filthy, God-forsaken hands on you!"
    s "Hey, I just washed them a few minutes ago."

    scene fourscompany16
    with dissolve

    ima "Osako! A little help here?! You’re strong! Get this woman off of me!"

    scene fourscompany17
    with fade

    os "Are you sure you {i}want{/i} me to, Imani?"
    ima "I don’t know what I want! This is all happening so fast!"
    w "NO IT’S FUCKING NOT! THIS IS WHAT WE’VE BEEN BUILDING TOWARD!"
    ima "STOP YELLING AT ME! I HAVE SENSITIVE EARS!"

    scene fourscompany18
    with dissolve

    s "Hey. Now wouldn’t be the best time for me to ask about how your “walk” went, would it?"
    os "Are you kidding? Absolutely not. "
    s "Yeah, I thought so. But can you at least give me a thumbs up or thumbs down to summarize it?"
    os "..."
    s "..."

    scene fourscompany19
    with dissolve

    os "I guess like this?"
    s "Well, that doesn’t help me at all."

    scene fourscompany20
    with dissolve

    os "Help with {i}what?{/i} This is our issue, not yours."
    s "Oh, I know. But you two have had no qualms whatsoever with trying to wrap yourselves up in {i}my{/i} issues, so I figured it would be okay if I maybe worried about your relationship. If that’s okay with you, I mean."

    scene fourscompany21
    with dissolve

    os "Oh, shit..."
    s "Yeah, I haven't forgotten about that."
    os "I'm sorry, man...So much has been going on lately that I've just..."
    os "I'm sorry. I shouldn't have said anything."
    s "Apology accepted. Now, leave it alone. And also tell me if you two are going to be okay because it’s messing with my head."

    scene fourscompany22
    with dissolve

    os "It’s bothering you that much?..."
    s "{i}Everything{/i} is bothering me now and I honestly can’t stand it. Since when do I have so many feelings? And how come all of them fucking suck?"
    os "I don’t have the answer to that, but...if you want my advice-"

    play sound "tackle.mp3"
    scene fourscompany23 with hpunch

    w "Ah-hah!"

    scene fourscompany24
    with fade

    ima "Wakana! Give me back my swimsuit!"
    w "Never!"
    ima "How did you even manage to get my top and {i}bottom{/i} off?! What kind of sex wizard are you?!"
    w "Never underestimate my ability to get a woman’s clothes off!"

    scene fourscompany25
    with dissolve

    w "Arakawa. Seize her."
    ima "Aaaaah! What a terrible time to come full circle! Don’t seize me!"
    s "Imani. Look at me."

    scene fourscompany26
    with dissolve

    ima "..."
    s "{i}I’m{/i} the captain now."

    scene fourscompany27
    with dissolve

    ima "No shot. Boutta finally get some action after almost a decade and he hits me with a quote from a Tom Hanks movie. Ain’t no way."
    w "Seriously, Arakawa? Am I going to have to strip you next?"
    s "Sorry. What I meant to say is-"

    scene fourscompany28
    with dissolve

    s "Everything’s fine. There’s no need to pause and try to wrap your head around why I’ve changed my mind when I did."
    s "It isn’t out of pity and it isn’t going to change what we are."
    ima "I mean...can it change it a {i}little{/i} bit? Cause I don’t want this to be one of those things we look back on and be like, “Wow! Wasn’t that crazy?”"
    s "Imani, I care about you. And I’m glad you shared your story with me."
    s "Now please allow me to repay your constant kindness in the most carnal way possible."
    ima "No more quotes from Tom Hanks movies?"
    s "No more quotes from Tom Hanks movies."
    w "Is this what the lead-in to heterosexual sex is {i}always{/i} like? Because this is fucking depressing."

    scene black
    with dissolve2

    s "Wakana, get out of the way."
    ima "Ah...Senpai! Wait! Why are you...you’re not just gonna...keep all of your clothes on, are you?"
    s "There’s no need to take any of them off if all I’m doing is taking care of you."
    ima "But- aah!"

    scene fourscompany29
    with dissolve2

    ima "But...aah...what if I {i}want{/i} you take your clothes off? Don’t I...mn...get a say in this?..."
    s "Maybe next time. Just let me do this tonight. It’s my way of saying sorry."
    ima "Don’t get me wrong, Senpai....I- ahh...I appreciate this {i}greatly.{/i} But I’d also appreciate it if you’d fuck me like once or twice or...maybe a hundred times tonight? Go big or...ngh!...go home...that’s what I always...ngh..."
    ima "Fuck...either you’re good at this or I’m...way more sensitive than I remember."
    w "I’d bet money on the latter. Only women know how to eat pussy correctly and you haven’t been touched at all in nearly five millennia."

    scene fourscompany30
    with dissolve

    ima "Are you two just...going to watch?!"
    w "Of course. I have to make sure you don’t run away."
    ima "Kinda...late for that now, isn’t it?!"
    s "Just ignore them. They can watch if they want."

    scene fourscompany31
    with dissolve

    ima "Hah...aah...easy for you to say...you’re not the one whose...body is on display right now..."
    s "Yes, but...they’ve already seen you before...it shouldn’t be a problem..."
    ima "I don’t...oh, fuck...I don’t know if...going to the bathhouse is in the...hah...same ballpark as...watching you go down on me..."
    s "You’re right. This is much better, isn’t it?"

    scene fourscompany32
    with dissolve

    ima "Oh...{i}fuck...{/i}yeah...I definitely...prefer this..."

    "Imani settles down after a minute or two, but never really stops squirming. And while it does feel somewhat demoralizing doing this with spectators, I’m able to tune them out for the most part."
    "I drag her body toward me, sinking my face deeper between her legs as I devote myself to pleasuring her. And I’m not sure if {i}she{/i} figures out how to tune the others out as well, but I can sense her getting more into it."
    "She slowly thrusts at me, begging for more than just my mouth as her breathing gets louder and her moans become pained."
    "All the while, she never stops whispering {i}Senpai{/i} — a word that carries its own charm as {i}she’s{/i} the only one who calls me that."
    "And it makes me want to take better care of her."

    ima "{i}Senpai...that feels...so good...{/i}"
    s "Then cum for me."
    ima "If I cum...does that mean you’ll fuck me next?..."
    s "Do you want me to?..."
    ima "{i}God, yes...fuck!{/i}"
    s "Tell me what you want me to do to you..."

    scene fourscompany33
    with fade

    ima "{i}Hah! Haaah...Oh God...I want your cock...so deep inside of me that...I won’t be able to feel anything else...{/i}"
    ima "{i}I want you to...ngh!...I want you to...fuck me so hard that...I forget my name! I want you to...oh, fuck.....aaah~{/i}"
    ima "{i}I...ngh!{/i}"
    ima "{i}Senpai...just...haaah...right there...just like....aaaaah!{/i}"
    ima "{i}Cumming! I’m...ngh!.......Aaaaaah!{/i}"
    os "Wakana..."
    os "Are you, like...{i}into{/i} this?"

    scene fourscompany34
    with dissolve

    w "It looks fun, doesn’t it? Are you {i}not?{/i} into it?"
    os "I mean...I’m not...{i}not{/i} into it? But I thought your medication was-"

    scene fourscompany35
    with dissolve

    w "See- that’s your problem, Osako. You always {i}think{/i} too much."
    os "I mean...that’s correct in regard to a lot of things. But I think {i}this{/i} is kind of serious since it concerns your health and you don’t exactly have a spotless history when it comes to-"

    scene fourscompany36
    with dissolve

    w "All these words are making me bored...don’t you want to have fun with me?..."
    os "I...{i}yeah...{/i}but aren’t we-"
    w "{i}Stop...thinking...{/i}"

    scene fourscompany37
    with dissolve

    os "..."
    w "..."

    scene fourscompany38
    with dissolve

    os "..."
    w "Osako..."

    scene fourscompany39
    with dissolve

    os "Take your clothes off and get on the bed."

    scene fourscompany40
    with dissolve

    w "Hm."
    os "Now..."

    scene black
    with dissolve2

    w "As you wish, my kitten..."

    "........."
    "......"
    "..."

    scene fourscompany41
    with dissolve2

    ima "Aaah! Hah! Senpai! Fuck!"
    w "Haaah....haaah......aaah!"

    "So yeah, this is a thing that’s happening now. "
    "Not exactly how I envisioned my night coming to an end when Wakana and Imani showed up at my house to kidnap me today, but certainly a good one."
    "Hell, if there’s more of this in store, maybe I’ll even find it in me to come back to school soon?"
    "That was a joke. I think. But this probably isn’t the right time to be telling jokes since two of the hottest girls I’ve ever met are simultaneously climaxing while holding hands."

    ima "Oh my...{i}fucking{/i} God...Senpai...Sen...pai! "
    w "Right......there......Osa.....ko......"
    os "Mlm......mnch......mmf!......Mlm!"

    "One of us is clearly working a lot harder than the other right now and, if you haven’t guessed, that person is not me."
    "That said, I’m certainly experiencing better results as the score is currently four to one."
    "Yes, I’ve been keeping track."
    "But no, I don’t think I’ll be asking if we’ll be switching up the pairs any time soon."

    scene fourscompany42
    with dissolve

    "Mainly because Imani and Wakana keep looking at each other like that and I don’t think Osako will ever look at me with such lust in her eyes."

    scene fourscompany43
    with fade

    os "Mlm.....mnh.....mnch...."
    s "..."
    os "...What?"
    ima "Hah!...Senpai!...keep...going! Why...did you stop?..."
    s "Is it weird for you to be doing this beside a guy?"
    os "Uhh...mlm...well it’s not like...mnch...I’m going down on you?..."
    w "Less talking...more licking..."
    s "Yeah. But I know I’d feel a little uncomfortable if {i}you{/i} were a dude."
    ima "Is this...really the time...for that?! I was...so close!"
    os "I think...mlem...Imani...wants you...mnsk...to keep going..."
    s "Do you-"
    os "Don’t...mlm...you dare...mnch...fucking say...mhhn...what I know...mnhh...you’re about to say..."
    s "When in Rome, you know?"
    ima "Fuck...Rome! Eat...my pussy!"

    scene fourscompany44
    with fade

    ima "Aaaaah! Yes, yes, yes! Right there...Senpai! Oh, I’m gonna cum again...Ooooh my fucking God....aaah!"
    w "Ahh...look at {i}you...{/i}cumming over and over...and {i}over...{/i}when you were trying to get out of this..."
    w "Aren’t you glad...ahh...you’ve got a...friend like me?..."

    scene fourscompany45
    with dissolve

    ima "Haah...oh my God...yes, but...can’t say I...expected you to hold my hand...while it was...finally happening..."
    w "May this night...strengthen our bond in...ways that can not be easily quantified..."

    scene fourscompany46
    with dissolve

    ima "Hah...aaah...our poor...partners, though...I feel bad that...we’re not doing anything for {i}them...{/i}"
    w "Forget...them...let it be about...{i}us{/i} this time...let’s...envelop ourselves in...ecstasy and...haaah..."

    scene fourscompany47
    with dissolve

    w "Aaah......Osako.....yes.....I’m close...."
    os "Mm! Mmlmf.....mlm....mnch....hnmfff...mmmm!"
    ima "Senpai......Sen......pai!"

    scene black
    with dissolve2

    imawaka "AAAAaaaaAAAAaaaaAAAAaaaaaAAAHHHHHHHHHHHH!!!!!!!!!!"

    stop music
    play sound "static.mp3"
    scene fourscompany48 with flash
    stop sound
    play music "normalday.mp3"

    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    "{i}The following morning...{/i}"

    w "{i}Ahem.{/i}"

    scene fourscompany49
    with dissolve

    w "Let it be known that literally all of this is Imani’s fault."
    ima "I begin this day...a new woman."
    os "Did you get...{i}any{/i} sleep last night? Or did Akira just...eat you out for like ten hours straight?"
    ima "A neeeeeeeew woman."
    s "I’m so tired."

    scene fourscompany50
    with dissolve

    w "Me too. I haven’t drunk that much since Halloween."
    os "And you probably shouldn’t ever again because it was extremely dangerous mixing all of that alcohol with your new medication."
    ima "So, what now? When’s the next foursome? Do I actually get to have sex next time? Who’s free next weekend?"

    scene fourscompany51
    with dissolve

    os "Hey, does anyone else feel kind of bad about leaving Rika out?"

    scene fourscompany52
    with dissolve

    ima "Oh, right."
    w "She’s going to be so upset when she finds out we have forever altered the dynamic of our friend group."
    s "..."
    s "We can just, like...{i}not{/i} tell her."

    scene fourscompany53
    with dissolve

    os "..."
    w "..."
    ima "..."

    scene black
    with dissolve2
    stop music fadeout 13.0

    "And on that day...a new promise was formed."

    $ renpy.end_replay()
    $ imani_love += 5
    $ wakana_love += 5
    $ osako_love += 5
    $ imanispring2 = True

    "{i}Imani’s affection has increased by 5!{/i}"
    "{i}Wakana’s affection has increased by 5!{/i}"
    "{i}Osako’s affection has increased by 5!{/i}"
    "{i}The dive bar is no longer blocked!{/i}"
    "{i}But you leave the inn still uncertain of several things — each of which eats away at you on the bus ride home.{/i}"
    "{i}And each bite becomes infected every time your gaze lingers on someone who sat in the wrong seat.{/i}"
    "{i}How long until sepsis sinks in, do you think?{/i}"

    $ renpy.pause(2, hard=True)

    "{i}Hey...Aki-kun.{/i}"
    "{i}What do you think it takes to rewrite what’s already happened?{/i}"

    play sound "static.mp3"
    scene noonsky with flash
    stop sound

    jump noonch4

label christmasimani1:
    "{i}Several hours later...{/i}"

    scene nightsky
    with dissolve2
    play music "wewereangels.mp3"

    "Imani and I decide to meet up in the urban district since it’s the closest place (within reasonable distance) that the two of us can go without fear of being caught by some of the other girls I am most likely sleeping with."
    "She didn’t word it like that. That’s all me. In fact, I’m not sure she even knows that I {i}am{/i} sleeping with any of {s}our{/i} her students yet. And I doubt she’d like me nearly as much if she did."
    "But, then again, I thought that with Chika too and we all know how things currently stand on that end."
    "I think it’s best to probably keep Imani out of it, though. She’s cuter when she lives in whatever world allows her to believe I’m not even half as terrible as I am. "
    "She’s bound to be pulled out of it one day, I’m sure. She’s friends with Osako, after all — and {i}she’s{/i} essentially known about Ayane and me for quite some time now without revealing as much to Wakana."
    "The only question is how long Imani {i}and{/i} Wakana (if she’s still oblivious) can remain untainted by my misdeeds. Because I assume the red flags are piling up."
    "And we’re but one strong gust of wind away from that pile being strewn across their respective living places."
    "Will they still smile at me even then? "
    "Or will the looks on their faces be one I can not comprehend? Halfway between disappointed and...whatever else a normal person would think about the man (or child) I present myself as."
    "I suppose that, if all else fails, and my adventurous assistant teacher simply {i}can’t{/i} let go of me even when she needs to, I can sever the ties with a knife I’ll call “truth.”"
    "It’s one I only taste the sting of when I can feel nothing else."
    "And oh, how I wish that were still the case."

    ima "Senpai! Over here!"

    scene imanixmasdate1
    with dissolve2

    ima "Perfect timing! I just got here myself."
    s "I was worried I was going to be late. I had to wait for a different train since the first one was full of that huge group of Europeans who only show up every now and then."

    scene imanixmasdate2
    with dissolve

    ima "The...huge group of {i}who?{/i} "
    s "Europeans. Otoha hates them. Anyway, doesn’t matter now. It’s boner time."
    ima "Boner time? But I thought it was Christmas date time."
    s "Those two things aren’t mutually exclusive. It can be boner date time."
    ima "It’s kind of a bad time for me right now. Biological functions and whatnot."
    s "That’s okay. You have a mouth."

    scene imanixmasdate3
    with dissolve

    ima "Damn, Senpai! You’re really coming out swingin’ today, huh?!"
    s "Sorry. I’ve never been good at “dates” so I normally just try and steer them to the primary objective as soon as I possibly can."

    scene imanixmasdate4
    with dissolve

    ima "I didn’t invite you out because I was trying to get laid, Senpai. I like, genuinely just wanted to spend time with you and stuff."
    s "..."

    scene imanixmasdate5
    with dissolve

    ima "But if you {i}reeeeeally{/i} want me to suck your dick, I guess we can find an alleyway or something. I’m charging you the holiday rate, though."
    s "No, it’s fine. We can just...{i}genuinely spend time together{/i} or whatever."
    ima "For {i}my{/i} sake? Nooooooo. It’s {i}clear{/i} you’re not going to calm down until {i}somebody{/i} sucks your dick. And since nobody {i}else{/i} is around, I guess it just {i}haaaas{/i} to be me."
    s "Imani, I’m fine. Really."
    ima "No, no! It’s {i}clear{/i} you need this. I insist. But just so you know, I’m doing it for {i}you,{/i} not me."
    s "Pass."

    scene imanixmasdate6
    with dissolve

    ima "Question — are you saying “pass” for my sake? Or am I meant to interpret those three consecutive rejections as a sign that you no longer wish to be sexually involved with me {i}despite{/i} bringing up boner time?"
    s "Boner time is just my catchphrase at this point. And I do wish to be sexually involved with you. Just not right now since you clearly have other things planned."
    ima "Cool. Because I also wish to continue being sexually involved with you. But I also respect your decision to not put your penis in my mouth right now. "
    s "Rad."
    ima "Even if you totally can if you {i}really{/i} want to."
    s "Again, rad."
    ima "Like, if you were to just {i}go for it,{/i} I totally wouldn’t say no. "
    s "How long are you going to keep this up for?"

    scene imanixmasdate7
    with dissolve

    ima "I don’t know. I am also very bad at dates. Including but not limited to asking people out on them, as I am sure you experienced earlier."
    s "We have so much in common."

    scene imanixmasdate8
    with dissolve

    ima "Right! And you know what {i}else{/i} we have in common, Senpai?"
    s "We’ve had at least one sexual encounter with a fruit?"
    ima "No, we-"

    scene imanixmasdate9
    with dissolve

    ima "Wait, {i}what?{/i}"
    s "We’re both teachers?"
    ima "Hell nah. You’re telling me about this fruit thing."
    s "Okay. But you have to go first."

    scene imanixmasdate10
    with dissolve

    ima "I’ve never done that with a fruit!"
    s "Really? But there are so many phallically shaped ones."
    ima "I know! Which is why I’ve {i}thought{/i} about it! But I’ve never actually {i}done{/i} it! Now, your turn! Which produce aisle do I need to keep you away from?!"
    s "None. I just wanted to get you to admit something funny."

    scene imanixmasdate11
    with dissolve

    ima "You know, it’s good we got this out of the way now. Because if my idea for this date involved introducing you to my parents, I’m not sure they’d appreciate our dialogue."
    s "They better if you’re flying me all the way to Ghana to meet them."
    ima "..."
    s "..."
    ima "Are you thinking what I’m thinking, Senpai?"
    s "Definitely not. I’m still on the fruit thing."
    ima "Well, {i}I’m{/i} thinking we should start a comedy duo."
    s "That would never work, Imani."
    ima "Why not?"
    s "Racism."

    scene imanixmasdate12
    with dissolve

    ima "Damn. Foiled again."
    s "Also, I get stage fright. "
    ima "Tch, of course. I knew there had to be a reason you wouldn’t put your penis in my mouth."
    s "Okay. I’m starting to think we should go somewhere else because I’m worried standing here and bantering like this will lead to us sucking up the rest of the time we have tonight."
    ima "I’m sure there’s some sort of fellatio-related joke to be made there, but now {i}I’m{/i} stuck on the fruit thing again too."

    scene black
    with dissolve2

    s "Come. We need to break free from our perpetual state of being hilarious."
    ima "Huh? Oh! Okay. Yeah."

    scene imanixmasdate13
    with dissolve

    ima "Do you have somewhere in mind? I don’t really come over here that often. I was okay with doing basically whatever tonight so long as we’re together."
    s "You’re being way cuter than normal today and I’m going to need you to tone it down before I really {i}do{/i} squeeze the life out of you."
    ima "Am I normally {i}not{/i} cute? Or is today just a really good day?"
    s "Today is just a really good day, I think."
    ima "It’s probably the hat. Or some kind of Christmas miracle. But the second you start singing, I’m outta here. There are lines that even I must draw, Senpai."
    s "..."

    scene imanixmasdate14
    with dissolve

    ima "Senpai?"
    s "I looked up what that thing you said meant."
    ima "Hm?"
    ima "I’ve said a lot of things. What are you talking about, exactly?"
    s "The Twi thing. Medɔ wo."

    scene imanixmasdate15
    with dissolve

    ima "Eh?! Ah!? Huh?! What!? When?! Why?!"
    s "After that beach trip. It sounded nice, so I wanted to know what it meant."

    scene imanixmasdate16
    with dissolve

    ima "Oooooooooh God. Oh no. Forget it. Forget I said that. Forget what it means. Forget everything ever and don’t look at me for at least the next...ten years? Twenty years? Sound good? Good."
    s "I thought you {i}wanted{/i} me to look up what it meant?"
    ima "Not like {i}this!{/i}"
    s "Is it true, Imani?"

    scene imanixmasdate17
    with dissolve

    ima "I didn’t think you’d {i}actually{/i} look it up! I was just saying things! I do that sometimes!"
    s "So it’s {i}not{/i} true then?"
    ima "No! Of course not!"

    scene imanixmasdate18
    with dissolve

    ima "I was just...you know..."
    ima "I get...caught up in the mood sometimes and...and {i}words{/i} happen."
    ima "But they’re just words, Senpai. You know {i}words.{/i} You’re a...{i}writer{/i} guy. Surely {i}you{/i} can understand, like...context and........stuff."
    s "So if I told you I love you, you wouldn’t be able to say it back?"

    scene imanixmasdate19
    with dissolve

    ima "Huh?"
    s "What would you do?"
    ima "I..."
    s "..."
    ima "It’s..."

    scene imanixmasdate20
    with dissolve

    ima "It’s not nice to mess with girls like this, Senpai. I’m already embarrassed enough."
    s "..."
    ima "..."

    scene black
    with dissolve2

    "I thought about saying it."
    "Really, I did."
    "There’s just no language I could do it in that she wouldn’t understand."
    "........."
    "......"
    "..."

    scene imanixmasdate21
    with dissolve2

    "It took Imani roughly twenty minutes to calm down, and thirty to be able to look me in the eyes again."
    "I try not to spend too much time thinking about exactly what she meant by those words as, despite not knowing much about love, even I can understand that it has different levels."
    "And I think in some regard, she really {i}does{/i} love me. And in that regard, {i}I{/i} probably love her too. But I probably love Wakana as well if we’re going to water down the word like that."
    "What I don’t understand is when it’s okay to say it. When you’re {i}allowed{/i} to love someone. And if I used those words on people like them, what would it mean for girls like Ayane?"
    "I guess it doesn’t matter now. She’s over it, so I should be too. "
    "And I should focus on making this night memorable for {i}her.{/i}"
    "I can’t do that if I’m only thinking about myself."

    ima "This is a nice place, Senpai. Festive. And with enough alcohol, I might even be able to forget how insanely embarrassed I am to look you in the eyes again."
    s "You were able to look me in the eyes without any trouble at all the night I ate you out for several hours straight."

    scene imanixmasdate22
    with dissolve

    ima "Because {i}that{/i} was less embarrassing. There’s no shame to be had when it comes to sex. {i}Feelings,{/i} though? That’s the stuff that gets you."
    s "I don’t think I’ve ever related to you as much as I do right now, Imani."

    scene imanixmasdate23
    with dissolve

    ima "We have so much in common, remember? We both haven’t had sex with any fruit yet. "
    s "“Yet” implies the possibility that it may still happen. "
    ima "Let’s hope neither one of us ever reaches that level of loneliness, okay?"
    s "..."
    ima "..."
    s "Imani, I have something to confess."

    scene imanixmasdate24
    with dissolve

    ima "I knew it! You {i}have!{/i} Haven’t you?! "
    s "It was an accident. Probably."
    ima "Yeah, sure. And Timothee Chalamet just tripped and fell into that peach in Call Me By Your Name. I need details. Now."
    s "I...don’t even know how to provide them. I just know that I have several vague memories of using a watermelon to-"

    scene imanixmasdate25
    with dissolve

    ima "Wait, a {i}watermelon?{/i} Aren’t they a little, like...huge? And hard? And...watery?"
    s "You are asking the wrong person."
    ima "Is...Is there a {i}right{/i} person to ask?"
    s "..."
    ima "Did...someone {i}make{/i} you fuck a watermelon, Senpai?"

    scene imanixmasdate26
    with dissolve

    s "You know what? Let’s just talk about Christmas instead. We’ve both embarrassed ourselves enough for tonight."
    ima "..."
    s "..."

    scene imanixmasdate27
    with dissolve

    ima "I may have practiced sucking dick with a zucchini once."

    "I knew it."

    s "Who are we, Imani?"

    scene imanixmasdate28
    with dissolve

    ima "A couple of weirdos apparently. But it’s that sorta thing that makes us fun, don’t you think?"
    s "Fun is certainly {i}one{/i} word for it."
    ima "What- are you {i}not{/i} having fun tonight?"

    scene imanixmasdate29
    with dissolve

    ima "Walking around...making fun of each other...taking in all the lights...the decorations..."
    ima "It’s exactly what I wanted out of a Christmas date. And there’s no one I’d rather be here with than you, Senpai."
    ima "I’m really glad you said yes."

    scene imanixmasdate30
    with dissolve

    ima "You know, Christmas actually used to be a pretty huge part of my life. Have I ever told you that?"
    s "I don’t think so. But I can feel a flashback coming on, so I’m sure that means you’re going to now."

    play sound "static.mp3"
    scene imanixmasdate31 with flash
    stop sound

    ima "{i}Well, I told you my father was a pastor right?{/i}"
    s "{i}That sounds familiar, so probably.{/i}"
    ima "{i}Well, I don’t know how much you know about all that religious mumbo-jumbo, and I’m sure you don’t care either, but my dad looooved Christmas.{/i}"
    ima "{i}And, as you know, I loved my dad. Which meant that I tried to make him happy any way I could.{/i}"
    ima "{i}And sometimes, that meant sitting around and listening to him read from the Book of Luke even when all of my brothers and sisters had gotten too old or too bored to bother with that.{/i}"
    iss "When the angels had left them and gone into heaven, the shepherds said to one another, “Let’s go to Bethlehem and see this thing that has happened, which the Lord has told us about.”"
    iss "So they hurried off and found Mary and Joseph, and the baby, who was lying in the manger. "
    iss "When they had seen him, they spread the word concerning what had been told them about this child, and all who heard it were amazed at what the shepherds said to them."
    iss "But Mary treasured up all these things and pondered them in her heart."
    iss "The shepherds returned, glorifying and praising God for all the things they had heard and seen, which were just as they had been told."
    iss "On the eighth day, when it was time to circumcise the child, he was named Jesus, the name the angel had given him before he was conceived."
    ima "Dad, I have a question."
    iss "And I have an answer."
    ima "Why does Jesus have so many names? "
    ima "Joshua. Jesus. Yeshua. Son of Man...You’re always referring to him differently. But if he was actually named Jesus-"
    iss "They are {i}all{/i} his names, Imani. "
    iss "The Bible has been adapted more times than one can count. And depending on who is adapting or translating the text, different names are used."
    iss "The name “Yehoshua” or “Yeshua” is mostly used in Hebrew texts. And before we had “Jesus,” we had “Iesus.”"
    iss "But it does not matter how his name is spelled, my daughter. What matters is-"
    ima "What he stands for and the lessons he can teach us. I know, Dad. I was just confused, that’s all. "
    iss "Then how about we take a break for today? You can come with me to the market and help me deliver the banku your mother cooked for-"
    ima "I have one more question. "
    iss "Of course. What is it?"
    ima "What does it mean to “circumcise” a child?"

    play sound "static.mp3"
    scene imanixmasdate32 with flash
    stop sound

    ima "And that was the first and last time I ever talked to my dad about penises. The end."
    s "That story took a weird turn near the end."

    scene imanixmasdate33
    with dissolve

    ima "It did. But the point is this-"
    ima "This holiday, to me, has always been about spending time with the people I care about. "
    ima "Not just this year either. The last couple — getting to spend it with you and the girls...it’s been amazing. And I’m truly grateful to have finally found somewhere it feels like I belong."

    scene imanixmasdate34
    with dissolve

    ima "But what’s it like for you, Senpai? Do {i}you{/i} have anything you always think about when the holidays roll around? Or are you too Japanese for that?"
    s "Christmas is getting pretty popular here, if you haven’t already noticed."
    ima "I have. But what does that mean for {i}you?{/i}"
    s "Lately...just Christmas parties. "
    s "Seeing everyone together. Getting roped into both joyous {i}and{/i} tragic events one after the other. Letting some people down. Lifting some others up."
    ima "Just another day then?"
    s "Pretty much...yeah."
    ima "Mm..."
    s "..."
    ima "..."

    scene imanixmasdate35
    with dissolve

    ima "I did...mean it, you know."
    ima "That thing I said."

    scene imanixmasdate36
    with dissolve

    ima "Like...it might not be {i}love-{/i}love yet. "
    ima "And...I know you get weird when I talk about this, so I’ll try and keep it brief and...painless, but..."
    ima "I’d be really happy if..."
    ima "If the rest of my Christmases were just like this one."
    s "..."
    ima "..."
    s "Well, the night’s not over yet."

    scene imanixmasdate37
    with dissolve
    play sound "zipper.mp3"

    ima "I knew you’d come around. But if anybody sees me going down on you, this was {i}your{/i} idea, not mine."
    s "Imani, no. I meant there’s some other sappy, quintessential place the two of us need to go if you {i}really{/i} want to call this a Christmas date."

    scene imanixmasdate38
    with dissolve

    ima "KFC?"

    $ renpy.end_replay()
    $ christmasimani1 = True
    $ imani_love += 1

    jump christmasimani2

label christmasimani2:
    if _in_replay:
        play music "wewereangels.mp3"

    play sound "static.mp3"
    scene imanitree1 with flash
    stop sound

    s "No, idiot. A huge, lit-up tree."
    ima "Oh, neat. But did you really have to stay silent the whole way here just so you could clap back at me with that response?"
    s "Anything for the bit, Imani. Our fans would love this."
    ima "The fact that we have fans at all is kind of impressive given that nothing we’ve ever done has been televised or publicly available anywhere."
    s "That’d be crazy, though. Right? If we were just part of some TV show or movie this entire time and didn’t even know about it."
    ima "Oh, like the Truman Show! That sounds fun. I hope they censored the foursome scene, though. I wouldn’t want Kirin masturbating to it."
    s "You know, I feel like that would actually explain a lot about being here. The barriers...the space war...the fact that there {i}always{/i} needs to be something tragic happening. This really does feel like the setup to a film."
    ima "Does that make me the love interest then?"
    s "Why not the protagonist?"
    ima "Me? A biracial, bisexual woman? Are you kidding? Just think of what Twitter would say."
    s "Yeah, you’re right. I hesitate to call myself a safer bet concerning anything other than ratings, though. But maybe one day- when the writer in charge of us no longer feels beholden to the masses."
    ima "So that’s it then? We’re just accepting the Truman Show as our new reality?"
    s "Yeah. Start looking for a door built into the sky or something. I’m about ready for the credits to roll."

    "That huge, lit-up tree smiles down at us in all of its Christmassy glory, but we’re too focused on feeding off one another to realize it."
    "I know it’s only been a couple hours at this point, but I’m having fun. Imani’s great when it comes to adapting to whatever mood I’m in. And that makes it easier to find comfort in borderline nothingness."
    "But maybe that’s {i}because{/i} she’s my co-star in this new rom-com of a life. They wouldn’t have cast someone who didn’t have good chemistry with me. "
    "It all feels too real to be {i}just that,{/i} though. Which is why I can joke about things like doors in the sky and ratings and whatnot as a staged reality would be far too convenient to ever be true."
    "Imagine it {i}was,{/i} though."
    "Imagine we did find a door. And the moment I passed through it, everyone I’ve ever come to know just smiled and collected their paycheck — leaving me to fend for myself outside my lifelong bassinet. "
    "I’d be helpless out there. It’d be hilarious. But still...I think I’d be open to giving it a shot."
    "A world where no one loves me sounds nice. I’m sure I’d be saying the opposite if the tables were turned, though."
    "It’s easy to want what you don’t have when there’s a permanent baseline of misery stretched across the metaphorical floor of your metaphorical existence. "
    "And I think I’d spend a little less time tripping over it if I could be distracted by the need to {i}find{/i} a companion rather than just waiting for one to come to me."
    "I wonder how someone like Imani {i}would{/i} view me outside of Kumon-mi. Would all those red flags I mentioned earlier push her away? Or would they obscure me {i}just enough{/i} to make me look approachable?"

    scene imanitree2
    with dissolve2

    "If they did...I think she’d have a better shot out there."
    "I think I’d be more inclined to latch onto this feeling and never let it go than I am in this world. Because on the outside, I’m not saying I wouldn’t have seven billion choices."
    "I’m saying I’d lack the patience to sift through them all with the looming threat of mortality weighing me down."
    "She’s the easiest way for me to start over. "
    "I’ve just come so far here that doing so would feel like one sin I could never pray away."

    ima "I think this is the part where you say that clichéd line about how “the moon is beautiful” or whatever."
    s "Nah. If this really is a movie, I’m sure that’s already been used by now."

    scene imanitree3
    with dissolve2

    ima "Maybe hit me with the good ole’ Casablanca then? {i}Here’s looking at you, kid...{/i}or however it goes."
    s "I’m not even sure that would fit the context of this scene since there’s no pressing threat of me leaving you behind."
    ima "Well, that’s comforting. Because finding another guy in Kumon-mi sounds way too hard and I don’t think I could settle for Rika given the age gap."
    s "There’s a bit of an age gap between us too, you know."
    ima "Naaah. Ours is realistic. And by the time I hit menopause, you’ll probably already have a bad back and won’t be able to screw me as hard anyway."
    s "So what I’m hearing is that we belong together because we’re both going to start physically decaying around the same time?"
    ima "Yeah, pretty much. But I think there’s a lot more than just that that makes us work. Assuming you ever want to actually go out with me and not just hit it all the time."
    s "Sorry, Imani. Kumon-mi High prohibits me from dating a coworker. Probably."
    ima "He says, despite having not been my co-worker since prior to last Christmas."
    s "I’m still your superior on paper, though. And that paper may very well be shredded the moment the principal finds out we come into contact with one another’s genitals on occasion."
    ima "You have such a way with words, Senpai. Staring up at the moon while hearing you talk about genitals is really making my heart flutter."
    s "I’d say that just looking at you is making mine do that, but I feel like I wouldn’t be able to see you at all if it weren’t for the bright yellow outfit you’re wearing."

    scene imanitree4
    with dissolve

    ima "I strategically chose this so you wouldn’t lose me. Seems it’s paying off in spades, huh?"
    s "Seems so. Are you still having a good time now that I’ve pulled you all the way over here to talk about movies and age gaps, though? "
    s "Or should we start winding this down because I get progressively more unlikable with every passing minute?"

    scene imanitree5
    with dissolve

    ima "That ain’t true, Senpai. My feelings for you are kind of peaking right now if we’re being honest. Which we probably shouldn’t since I know you want to keep me as a friend. But yeah. You’re great."
    s "If you really want me to date you, you’re going to have to stop complimenting me. The quickest way to my heart seems to be just bossing me around and reminding me of how much I suck all the time."
    ima "You like Wakana that much, huh?"
    s "That’s...not who I was thinking of. But yeah, I guess it does apply to her too. She’d also be a good match for me if she hadn’t spent her whole life banging a would-be Olympian."
    ima "Now’s the best chance you have to steal her, you know."
    s "Imani, come on."
    ima "What? I’m not {i}endorsing{/i} it. I love Osako. "
    ima "I’m just saying, if you {i}really{/i} think she’d be a good match for you...and you think screwing {i}her{/i} for the rest of forever would bring you happiness...what are you waiting for? "
    s "Are you telling me you’d betray your friends if it brought {i}you{/i} closer to happiness?"
    ima "It’s not about {i}betraying{/i} them, Senpai. It’s about doing what’s best for you. "
    ima "No one {i}likes{/i} letting other people down. But it still happens every day because it kind of {i}has{/i} to for anyone to ever get what they want. "
    ima "Otherwise, we’d have a bunch of people running around with unfulfilled wishes — dwelling on “what ifs” and “what could have beens” instead of focusing on where they are now. And with whom. "
    s "I guess that explains why you’ve always been so open about your feelings for me then."

    scene imanitree6
    with dissolve

    ima "Not {i}always.{/i} It took me a while to summon the courage to confess to you — if you even want to call it that. I’m just better at reasoning than I am at {i}acting.{/i} "
    s "Then I guess we’ve found one thing we {i}don’t{/i} have in common since I’m the exact opposite. Acting, I can do. But rationalizing even the simplest things feels like a mental obstacle course some days."

    scene imanitree7
    with dissolve

    ima "Maybe you need a change of pace then?"
    s "Is this the part where you proclaim that {i}you{/i} can be that change of pace? Because it would be a good time for that."
    ima "Yeah."
    ima "Just not in the way you’re probably thinking."

    scene imanitree8
    with dissolve

    s "Hm?"
    ima "What would you say if I told you I had a solution to like a million of your problems in the palm of my hands, but I was intentionally not revealing it because I didn’t want to {i}betray{/i} anyone?"
    s "I’d say that’s a convenient turn of events and extremely topical given what we were discussing one minute ago. And also that it is likely not true."
    ima "Are you happier now that you’re not teaching anymore, Senpai?"

    scene imanitree9
    with dissolve

    s "Not...really? But there are also several other factors contributing to that. And it certainly doesn’t help always worrying about having to come back."
    ima "Wakana gave you a deadline, right? The...beginning of the next school year or something?"
    s "It’s not really the deadline I’m worried about. It’s that {i}I’m{/i} constantly letting everyone down by postponing my return over and over again."
    s "It’s not just Wakana either. You add to it. The girls add to it. And then {i}I{/i} add to it on those early mornings where I just wander around town remembering where I’m {i}supposed{/i} to be."
    s "But I’m afraid of coming back because I don’t think it will {i}fix{/i} that creeping dread of never going anywhere...Or the repetition of living through the same days over and over again."
    s "Which isn’t even mentioning how you’re a better teacher than I ever was. "
    s "I don’t know. There’s a lot wrong with my life right now, and even more is changing. And I probably would’ve come back to school already if I thought that was the key to changing that."
    ima "Why not just rip the Band-aid off then?"
    ima "Why not quit?"

    scene imanitree10
    with fade

    s "You don’t actually-"
    ima "I think you should do what’s best for {i}you.{/i} And I think that Wakana and I have both been way too selfish in pushing you to come back because that’s what {i}we{/i} want."
    ima "We miss you. You know that. But, and I know you’re going to disagree with this, neither one of us knows you as well as {i}you{/i} do."
    ima "We can tell ourselves we know what’s best for you, sure. So can all of the girls. But if you’re living with the constant pressure of having to return to school...and that’s {i}killing{/i} you?"
    ima "Just stop. "
    ima "It’s okay to walk away, Senpai. Responsibility is one thing, yeah. But an even {i}bigger{/i} thing is figuring out what the hell you want to do with your life. "
    ima "And, being someone who actually {i}likes{/i} teaching, I’m not sure that {i}this{/i} is right for you."

    scene imanitree11
    with dissolve

    s "You’re just saying that because you’re gunning for my job."
    ima "No, Senpai. I’m not."
    s "Then...you’re just saying it because it cancels out that thing I said earlier about not dating coworkers."
    ima "No, Senpai. I’m-"
    ima "Well, actually, that one’s true."

    scene imanitree12
    with dissolve

    ima "But that’s still not the point!"
    ima "At the end of the day, all I really want is for you to {i}not{/i} feel like every day is just a repeat of the one before it."
    s "Well, I’ve got very bad news for you."
    ima "Like 40%% of your personality is having bad news. You’re constantly talking yourself out of {i}everything{/i} that could potentially bring you joy."
    ima "But school seems to be like the one thing you talk yourself {i}into{/i} that doesn’t bring you joy. And it feels like you’re only there because you believe that’s where you’re meant to be. "

    scene imanitree13
    with dissolve

    ima "Wakana would kill me for saying this and...I kind of hate {i}myself{/i} for it since it feels like I’m convincing you to spend {i}less{/i} time with me..."
    ima "But maybe the time we spend together will be {i}more{/i} fulfilling without that creeping dread latching onto your ankles the whole time?"
    s "..."
    ima "I don’t really get {i}religious{/i} often, but there’s a quote from the Bible that’s like..."
    ima "“When times are good, be happy; but when times are bad, consider — God has made the one as well as the other. Therefore, a man cannot discover anything about his future.”"
    ima "“In this meaningless life of mine I have seen both of these: a righteous man perishing in his righteousness, and a wicked man living long in his wickedness.”"
    ima "“Do not be overrighteous, neither be overwise-- why destroy yourself? Do not be overwicked, and do not be a fool-- why die before your time?”"
    s "That’s a really long quote to remember for someone who doesn’t get religious very often."

    scene imanitree14
    with dissolve

    ima "Yeah, well...I’ve heard it a thousand times, so..."
    ima "Either way, I don’t want you to dwell on this shit for so long that you turn into some giant ball of uncertainty and negativity. I want you to {i}live.{/i} And I want you to {i}let{/i} yourself live."
    ima "So if that means cutting certain cords...even {i}if{/i} those cords are connected to all of us who care about you...maybe that’s what needs to be done? Do you see what I mean?"
    s "I do. But, question — is this one of those things you’ve been thinking about for longer than you let on? Or did all of this {i}really{/i} just come to you now?"

    scene imanitree15
    with dissolve

    ima "Beats me! Anyway, here’s a present."
    s "Where were you even keeping this? And why do I suddenly not feel the need to further press you about that thing I just asked?"

    scene imanitree16
    with dissolve

    ima "Probably because you’ve already come up with an answer. Don’t worry, though. I’m not going to make you reveal it tonight. Take as much time as you need."
    s "Can I open this now or are you going to make me wait until I get home?"
    ima "You can open it now. Fair warning, though — I am just as bad at gift-giving as I am asking people out on dates. Please see it as “endearing” rather than “careless.”"
    s "I’m sure it’s fine. I understand that I’m a hard person to shop for."
    ima "Also, in lieu of giving {i}me{/i} a present, you can just fuck me or whatever. Rain check, though. "

    scene imanitree17
    with dissolve

    s "Imani."
    ima "I know, I know. Your balls must be blue as hell having to suffer through my apparent “peak cuteness.” But I cannot control the clock, Senpai. This is merely a side-effect of the cruel joke that is {i}humanity.{/i}"

    scene imanitree18
    with dissolve

    s "No, Imani. This is a pocketknife. "
    ima "Yeah. Cool, right?"
    s "I mean...{i}sure?{/i} But this is more of a Noriko gift than one for {i}me.{/i}"
    ima "Noriko’s the one who helped me pick it out, actually."
    s "{i}Why?{/i}"
    ima "Bro, you said it yourself. You ain’t easy to shop for. And the Internet says dudes in their thirties like pocketknives. "
    ima "It was either that or craft soap, and I wasn’t about to drop 5,000 yen on showers I ain’t allowed to join you for."

    scene imanitree19
    with dissolve

    s "What am I going to do with it?..."
    ima "Give it to Ami! She was having a {i}damn{/i} good time cutting through some meat earlier. She’ll know what to do with it."

    play sound "static.mp3"
    scene amisfunpartynight38 with flash
    scene imanitree20 with flash
    stop sound

    s "..."
    ima "You good, Senpai? Should I have gotten the soap instead?"
    s "I’m good."

    scene black
    with dissolve2

    s "Just..."
    s "Felt like I was about to remember something..."

    "........."
    "......"
    "..."

    scene clearnightsky
    with dissolve2

    "We stayed there and stared at the tree for another thirty minutes or so, talking more about whether or not I should come back to school."
    "And honestly, I don’t know yet."
    "Imani brought up a lot of good points, but..."
    "If {i}that’s{/i} not what I want to spend my life doing, what {i}should{/i} I do?"
    "What else {i}could{/i} I do? "
    "If what I’ve learned is true, which I’m pretty sure it is, teaching is essentially all I’ve ever done. "
    "Granted, I {i}do{/i} currently have an eternity to take up something else, so..."
    "I don’t know. I’ll think more about it later. And I’ll have plenty of time to do so, seeing as Imani is too biologically impaired to invite me back to her place to {i}really{/i} end our date tonight."
    "She seemed fine with it, though."

    play sound "static.mp3"
    scene imanitree21 with flash
    stop sound

    ima "{i}{b}AAAAAAAAAAAAAAAAAAAHHHHHHHHHHH!!!!!{/i}{/b}"
    ima "{i}{b}TONIGHT TOTALLY WOULD HAVE BEEN THE NIGHT!!!!!! CURSE THIS BODY!!!! CURSE THIS WORLD!!!! HOW LONG MUST I REMAIN UNFUCKED FOR?!?!?!{/b}"

    play sound "knock.mp3"

    ri "{i}Uhh, Imani? Everything okay in there?{/i}"
    ima "{i}{b}NO!!!!!!!!!!!!!!{/b}{/i}"

    "And I’m sure she’s already over it by now as there will be plenty more opportunities for me to annihilate her lower body in the future."

    stop music
    $ renpy.end_replay()
    $ christmasimani2 = True
    $ imani_love += 1

    jump christmasfive2

label christmasimani3:
    if _in_replay:
        play music "hallelujah.mp3"

    scene imanixmaspenis1
    with dissolve2

    "As I glance around the room, I find the only gift I could ever ask for. I’ll be leaving the second half of that statement open-ended, though, as you can likely come up with something better than I can."
    "We both know that sounding compassionate has never been my strong suit. And we both know that, if I {i}were{/i} to say something sappy right now, you’d probably think I don’t mean it."
    "And you might be right. Actions speak louder than words, after all. And that’s even more true when those words are only thought and never spoken in the first place."
    "Thankfully, standing next to someone who’s always been better at openly caring for these girls helps take some of the stress of needing to {i}feel{/i} away."
    "Imani’s an exceptional teacher. I know that much without having set foot in the classroom in...when {i}was{/i} the last time I was there? I can’t even remember."
    "But what I {i}do{/i} remember is what she told me right around the time I received my first pocket knife. That maybe things would be better for me if I stopped worrying about ever going back at all."
    "If I did, would I still be able to come to things like this? "
    "I’m sure the girls wouldn’t mind. They love me. Some probably love me {i}too{/i} much. But then again, if we want to get even more depressing for a second, any amount of love is too much for someone like me."
    "But the question then is how would I justify it? How would I justify {i}this?{/i}"
    "Up until now, it’s been easy dragging myself to holiday parties and class-wide contests because {i}I{/i} have been a part of them."
    "Without my job, I’m just a man. A boy. Someone putting himself into situations that he knows are dangerous {i}without{/i} something to fall back on mentally. "
    "I’m not saying that doing the latter makes me good — it makes me anything but. "
    "Without that reason, though..."
    "Without that {i}connection...{/i}"
    "What am I?"
    "These are the things I have to think about when the monks go away. "
    "I imagine they’re exchanging gifts with each other right now — or spitroasting Maisie Belle beside the yule log."
    "Whatever it is, I hope they’re having fun. I hope they’re not getting into trouble. Malvin {i}always{/i} gets into trouble. "
    "But that’s why he was my favorite. He was something I wanted to be. "
    "Someone ambitious. Someone who wasn’t afraid of consequences and would put his safety on the line every time he left the house, all in pursuit of entertainment."
    "You wouldn’t be proud if you saw me today...would you, [[REDACTED]?"
    "You’d probably think I’m just some predator trying to look cool. Trying to kill time. But you’d miss out on the dreams. The darkness. The things that make me {i}different{/i} from Malvin because Malvin was never {i}raped.{/i}"
    "He was just a kid."
    "And so was I."
    "But things were different where I grew up."
    "Instead of having two brothers, I only had one."
    "A glutton, he was. The kind to take, but never give."
    "The kind to-"

    s "Imani, start talking to me or I am going to go insane."

    scene imanixmaspenis2
    with dissolve

    ima "Huh? Sure. You good, Senpai?"
    s "No. I’m remembering things in the worst context imaginable. The last time this happened, I sexed someone into dust."
    ima "You did what now?"
    s "Doesn’t matter. Just talk to me. The monks are gone and I need a distraction."
    ima "And I need another drink if you’re going to be talking about monks and shit. "

    scene imanixmaspenis3
    with dissolve

    ima "You want one? Beer? Something harder?"
    s "I think I want to have sex."

    scene imanixmaspenis4
    with hpunch

    ima "PFFFTFTFTTT?!??!!!"

    scene imanixmaspenis5
    with dissolve

    ima "Now?!"
    s "Oh, right. You’re still biologically impaired."
    ima "I-"

    scene imanixmaspenis6
    with dissolve

    ima "I mean...today should be okay...if you {i}really{/i} want to..."
    s "You’re not going to bleed on me, are you?"

    scene imanixmaspenis7
    with dissolve

    ima "Don’t be gross, Senpai! Yesterday probably would have been fine too! I just...wanted to be sure I was in the clear!"
    s "Meaning?..."
    ima "Don’t ask questions you don’t want to hear the answer to! And don’t say you want to have sex before immediately pivoting to saying stuff that makes me {i}not{/i} want to!"
    s "So you {i}do{/i} want to then?"

    scene imanixmaspenis8
    with dissolve

    ima "{i}Fuck yeah,{/i} I do. You know how long I’ve been trying to get a piece of that."

    scene imanixmaspenis9
    with dissolve

    ima "We’re at a Goddamn Christmas party right now, though. If we snuck away to get laid, don’t you think everybody would catch on?"
    s "Would it be a problem if they did?"
    ima "You seen these girls, Senpai? My head would end up on a pike by New Years."
    s "Is that something you’re willing to risk to receive the penis?"

    scene imanixmaspenis10
    with dissolve

    ima "{i}Receive the penis?{/i} You really are trying to turn me off, aren’t you? "
    s "I don’t think so. Is that what’s happening?"
    ima "No. I want you so fucking badly right now that I’m like one more dick reference away from humping you beneath that huge ass Christmas tree."
    s "Cool."

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "You’re coming with me then."
    ima "S-Senpai! Someone will notice!"
    s "Probably Chika. "
    ima "That’s one of the worst ones {i}to{/i} notice!"
    to "Miss Imai? Sensei? Where are you-"
    ima "B-Bathroom! Senpai is just showing me the way since I don’t have the Tsukioka Manor navigation app!"
    to "You don’t have the app yet? But we put so much time and money into developing it and-"
    s "Don’t worry, Touka. I’ve got it covered. And if anyone asks where we went-"
    to "{i}Hah.{/i} Yes, I will advise them it is not sexual."
    s "See? We’re in the clear."
    ima "{i}Senpai! You fucking...aaah!{/i}"

    play sound "static.mp3"
    scene imanixmaspenis11 with flash
    stop sound

    ima "You don’t have to {i}drag{/i} me! I want this even more than you do!"
    s "You don’t know where we’re going."
    ima "And you do?! Does this place have a secret sex dungeon or something?! Because I really wouldn’t put it past that Tsubasa lady!"

    if christmastsubasa1 == True:
        "I wouldn’t be surprised at this point either — especially since she {i}did{/i} just command me to jerk off in front of her as a form of punishment."
        "I guess she’ll have to punish me again soon, though, as I’m about to break the new rule she gave me just a short while ago."
        "She’ll know too. She knows everything that happens here."
        "That said...I wonder what the punishment will be this time?"

        if tsukasaspring3 == True and tsukasarefused == False:
            s "It’s not a sex dungeon — just a room. With nothing particularly special about it."
        else:
            s "To be honest, I don’t know where we’re going either. I’m sort of just winging it."

    else:
        s "Neither would I. But no, I don’t know about any secret sex dungeon."

        if tsukasaspring3 == True and tsukasarefused == False:
            s "It’s not a sex dungeon — just a room. With nothing particularly special about it."
        else:
            s "In fact, {i}I{/i} don’t know where we’re going either. I’m sort of just winging it."

    ima "Well...do I get a say in this?!"
    s "Sure. Do you have a preference? Any special requests?"
    ima "How about a-"
    s "Denied. You haven’t submitted the correct forms to HR yet."
    ima "S-Senpai! Slow down!"

    if tsukasaspring3 == True and tsukasarefused == False:
        "To be {i}more{/i} honest with you, I’m only {i}half{/i} telling the truth. Because the place I have in mind {i}is{/i} just a room."

        if christmastsubasa1 == True:
            "But it’s a room that might help me get around Tsubasa’s newest rule. And a place that might help me remind myself of who I {i}really{/i} am once I’m in there."
            "Not some man who’s reluctantly remembering his roots. Not some coward who could never speak or act up."
            "But a demon — the kind that haunts others. Who will show up in delusions when someone {i}else{/i} needs something to overcome. "
            "This is how I become a ghost."
        else:
            "But it’s a room that, whether I like it or not, I find comfort in."
            "Unfortunately, it’s somewhere I should be {i}less{/i} comfortable than anywhere else in the manor. "
            "But if not today, then..."
            "Well, to echo someone else — things can only go down from here."

    else:
        s "There’s no slowing down once I’ve set my sights on something, Imani. And right now, I have set my sights on fucking you until it’s December 26th."
        ima "That’s only like thirty minutes from now! Can’t you last longer?!"
        s "Probably not. You’re really fucking hot."
        ima "Thanks! You too! And, for the record, thirty minutes is plenty! I’ll probably finish before you do!"
        s "Thanks, Imani. I needed that."
        ima "Any time, Senpai! "

    scene black
    with dissolve2

    "We eventually make it to a rather unassuming door."
    "One that, from the outside, seems entirely unspectacular."

    play sound "static.mp3"
    scene imanixmaspenis12 with flash
    stop sound

    if tsukasaspring3 == True and tsukasarefused == False:
        "But those of us who have been here before know it’s anything but."
        "The moment we blast through the door, I push Imani up against the wall and press my mouth against hers so she doesn’t see the golden plaque labeled “Tsukasa” near the lightswitch."
        "I don’t know if she’s still in here. I don’t even know if this was the room she was mentioning when she said she needed to go “clean” hers since I’m sure she has plenty."
        "But even if it’s not, and even if {i}she’s{/i} not, this is where I want to be. "
        "It’s somewhere those voices who haunt me won’t ever find. A place where I can trick myself into believing I’m not broken by holding someone else’s livelihood off the edge of a cliff."
        "And sure, it’s not the nicest of options. Sure, it risks traumatizing a girl who, like me, has really only ever wanted to belong to something or someone."
        "But it might open {i}another{/i} door — to a world where she can both understand that such a future is improbable and not really necessary to begin with."
        "We don’t need to {i}be{/i} wanted so long as we can {i}feel{/i} wanted. "
        "And I want to show her what love looks like, even if it’s merely a facade."

    else:
        "That changes today, though — as something spectacular is going to happen inside."
        "Two friends, who might be better for one another than they’ll ever really understand, will become more than that."
        "And for a moment, before I have time to go back to hating myself, I will be a part of something beautiful."
        "The memories of one more woman I will never deserve."

    ima "Mm! Mm...Senpai! Mmm!"

    if tsukasaspring3 == True and tsukasarefused == False:
        "Assuming she’s here, that is."

    ima "I can’t believe...you’re finally gonna...{i}fuck{/i} me..."
    s "You’ve been dreaming of this day, haven’t you?"
    ima "Mm! Mmm...ever since...we met...I’ve wanted you inside of me...I’m gonna make you feel...so good...{i}Senpai!{/i}"

    "I hold her close, squeezing one of her breasts with so much strength that I’m positive it can’t feel good. But she remains unfazed, aggressively and passionately stroking my cock through my jeans."

    ima "Take your fucking dick out...{i}right now...{/i}"

    play sound "zipper.mp3"
    scene imanixmaspenis13 with dissolve

    "Before I have a chance to act, {i}she{/i} finishes the job for me. It’s like school all over again. Just {i}this{/i} time, I get to revel in the sensation of a thumb on the underside of my shaft and a tongue in my mouth."

    ima "Mm...mmm! Senpai...you’re so hard already...Did you get like this for {i}me?...{/i}"

    if tsukasaspring3 == True and tsukasarefused == False:
        "I decide against answering her question since half-truths are lies and I don’t want to disappoint her moments before using her to get off."
    else:
        s "Who else...could do this to me?..."
        ima "Mnch...idols...goths...ahmn...basically everyone else..."
        s "Are you implying {i}you{/i} only have eyes for me now?"
        ima "That depends...aaahn...let’s see how hard you fuck me first..."

    "She begins to move faster, tightening her grip on my cock while biting my lip. And while I want {i}very{/i} badly to undress her, my subconscious seems to want to remain in this moment for now."
    "Maybe forever, really. Or at least until I cum all over that bright yellow sweatshirt of hers. "
    "That sounds far less intriguing than the prospect of emptying myself inside her when it’s safest to do so, though. So I remain like this for several minutes before taking charge and keeping the pattern alive."

    s "Take your clothes off..."
    ima "Yes, sir...Senpai, sir..."
    ima "Where do you want me?..."
    s "You’re going to bend over the table...and I am going fuck you so hard that you’ll forget you were raised as a Christian..."
    ima "Mm! Mm...holy fuck...{i}yes...{/i}God, that’s so fucking hot...God, I want you..."
    s "Then stop jerking me off and do as I say..."
    ima "Mhm...mmh...yeah? Am I actually gonna get to be Senpai’s assistant again today? Will it be like old times? You bossing me around?...Making me...mmm...do stuff for you?..."
    s "Unless you want me to cum on your shirt right now, yeah. That’s how this will go."
    ima "Maybe I {i}do{/i} want you to cum? I can go back to the party with a trophy from my {i}superior.{/i}"
    s "Strip...{i}now...{/i}"

    scene black
    with dissolve2

    ima "Mmm! Mm...yes..."
    ima "{i}Senpai...{/i}"

    "........."
    "......"
    "..."

    scene imanixmaspenis14
    with dissolve2

    s "You realize keeping your underwear on is a form of insubordination, right? When I said strip, I meant everything."
    ima "Uh-oh. Sounds like you might need to discipline me, then. Show me what happens when I go against my boss’s orders."
    s "I see you’re going to be difficult in bed too. Just like at school."
    ima "Now imagine how fucking me {i}at{/i} school would be. Endearing, right?"
    s "We’ll see how endearing you are once you’re cumming your brains out."

    scene imanixmaspenis15
    with dissolve

    ima "Good call. Best way to make me follow orders is to show me the {i}right{/i} way to do things, Senpai. How will I ever know otherwise?"

    scene imanixmaspenis16
    with dissolve

    s "I hope you’re enjoying your last minutes of being a pain in my ass before I put you in your place."
    ima "I am, Senpai. Just feeling the tip pressed up against me like that is making me-"

    scene imanixmaspenis17
    with hpunch

    ima "AAAH!!~~"

    "Without warning, I sink my cock inside of Imani, who welcomes me with ease despite the intense jolt that’s sent through her body...causing me to sink my fingers deeper into her ass to stabilize her."

    ima "Aaah! Hah...it’s inside...Senpai is inside of me..."
    s "You’re not going to do this in third-person, are you?"
    ima "Senpai...don’t..."
    ima "Don’t...move yet...I’m..."

    scene imanixmaspenis18
    with dissolve
    play sound "dosex.mp3"

    ima "Haaah! No! Stop! Wait!"
    s "No can do, Imani. I’ve gotta fuck you back into obedience since you’re so set on being a little brat right now."
    ima "Aah! Aah! Seriously! Wait! I’m...aah!"

    scene imanixmaspenis19
    with dissolve

    ima "IYAAAHHHH! I’M CUMMING, I’M CUMMING, I’M CUMMING, I’M CUMMING! HYAAAAAHHH!!!!"

    with sexfade
    with sexfade
    scene imanixmaspenis20 with cumflash
    with hpunch

    ima "Haaaah.......aaaah.......Sen......paiiiii~"
    s "........Already?"

    scene imanixmaspenis21
    with dissolve

    ima "It’s been years, okay?! Plus, you’re grossly underestimating just how badly I’ve wanted you to fuck-"

    scene imanixmaspenis22
    with hpunch

    ima "MEEEEeeeEEeeEEE?!? YAAAAAAAHHH!!! AAAAHHHH!"
    s "Give me your fucking arm."

    scene imanixmaspenis23
    with dissolve2

    ima "Yeshhh...Shenpaiiii~~~~~"

    if tsukasaspring3 == True and tsukasarefused == False:
        play sound "static.mp3"
        scene imanixmaspenis24 with flash
        stop sound

        ima "AaaaAaah! Aaaaah FUCK! You’re so big, Senpai! I’m sorry I was annoying! Please...fuuuUUUck meeEEEE harder!!!! YESSSSS!"
        s "See what happens when you do as I tell you, Imani? That feels good, doesn’t it?"
        ima "Yess! Yeshhhh! NGAAAAaaaaaahhhahhahhhh!!!!"
        s "You’re not crying, are you?"
        ima "Nnoooooo! It just...feeeells shooo gooooooddd!!!! Eyahaaahhhhh!!!!! Haaaaaah!"

        "With my cock fully submerged inside of her, I become so lost in the moment that I truly {i}am{/i} lost for a moment."

        scene imanixmaspenis25 with dissolve2

        "But I’m dragged back by my peripheral vision when I remember why I chose this room in the first place."

        tk "{i}Ah!{/i}"

        scene imanixmaspenis26
        with hpunch

        ima "Aaah! Aah! Fuck! Yes! Sen...pai! So hard...so fucking hard! Oh my God! Ooohh my fucking God, YES!"

        scene imanixmaspenis27
        with dissolve2

        s "..."

        scene black
        with dissolve2

        "So you {i}are{/i} here, then."
        "Go on."
        "{i}Watch{/i} me."

        play sound "static.mp3"
        scene imanixmaspenis28 with flash
        stop sound

        "I don’t care if you do."
        "I don’t care if that {i}curiosity{/i} reaches its boiling point because I know what it’s like on the opposite end. "
        "And if there are more people like me in this world, maybe it’ll be harder for me to realize just how far I’ve fallen."
        "Maybe you’ll fall too. Maybe you already have. And maybe you want me to catch you."
        "I will. Just like she caught me. And I will ruin you. Just like she ruined me."
        "But it will be a lesson in love — one that you take to the grave and look back on both fondly {i}and{/i} sickly when things don’t work out. Because, let’s face it — there’s no way they ever could."
        "The two of us have nothing in common apart from a desire to escape the endless torment that is feeling out of place even when you know you’re {i}not.{/i}"
        "Or, you know...maybe there’s something else we have in common too. Because {i}you’re{/i} the one who’s choosing to watch right now. {i}I’m{/i} not making you do anything."
        "I have learned nothing from these mistakes. And some of them have brought the happiest days of my life."
        "And while that doesn’t say much in a life of tragedy after tragedy, maybe it will say something for you."
        "Maybe one more mistake won’t cause {i}my{/i} world to end — but {i}yours{/i} did the moment you decided to keep your eyes open."
        "The floodgates have opened."
        "But if the water is too violent, I won’t worry. "
        "I’ll just wait for it all to reset."

        ima "Senpai! Sen...pai! I’m...cumming again! Harder! Deeper! Fuck my...little hole! Cum inside me! Cum...inside...me!"
        s "Imani...aah...fuck..."
        tk "..."
        ima "HAAAHHHH! DO IT! CUM FOR ME! FUCKING...CUM FOR ME, SENPAI!"

        with sexfade
        with sexfade
        with cumflash
        with hpunch
        stop music fadeout 12.0

        ima "HYAYYAAHHHH!!!! AAAAaaaAAaaAAAAHHHhhhh!!!! HaaaaAAAAhhhh!!!!!!"

        "I cum...but I’m not sure if it was for her or not."

        tk ".........."

        ima "Haaah...aaah...wow...."
        ima "Great...timing too...Now we can...get back to the party before things are {i}super{/i} suspicious, can't we?"
        s "...Yeah. Let’s go back to the party."
        ima "Phew...damn. That was even better than I expected, Senpai. You {i}sure{/i} taught me a lesson tonight, didn’t you?"
        ima "It was only a few minutes, but...you really picked things up at the end. Do you {i}always{/i} start going crazy like that when you’re about to cum? Or did all of my begging just-"
        s "I just..."

        scene black
        with dissolve2

        s "I don’t..."
        s "I think I just..."
        s "Felt too alive."

        $ renpy.end_replay()
        $ christmasimani3 = True
        $ imani_love += 1
        $ tsukasacurious = True

        "{i}Imani’s affection has increased to [imani_love]!{/i}"
        "........."
        "......"
        "..."

        jump christmasfive8

    else:
        play sound "static.mp3"
        scene imanixmaspenis29 with flash
        stop sound

        ima "AaaaAaah! Aaaaah FUCK! You’re so big, Senpai! I’m sorry I was annoying! Please...fuuuUUUck meeEEEE harder!!!! YESSSSS!"
        s "See what happens when you do as I tell you, Imani? That feels good, doesn’t it?"
        ima "Yess! Yeshhhh! NGAAAAaaaaaahhhahhahhhh!!!!"
        s "You’re not crying, are you?"
        ima "Nnoooooo! It just...feeeells shooo gooooooddd!!!! Eyahaaahhhhh!!!!! Haaaaaah!"

        "With one hand wrapped tightly around her forearm and the other sinking its nails into her flesh, I thrust into Imani more like I’m trying to hurt her than I’m trying to pleasure her. But I think it kind of works."
        "She’s so wet that I can feel her juices seeping in through the small gap in my pants that I opened up to give her what she wanted. And I already know she’s going to at least temporarily {i}stain{/i} them, but..."
        "I neglect to remove them entirely because not only do I want {i}her{/i} to know that I’m in control, but I want to convince {i}myself{/i} that I’m in control. "

        if christmastsubasa1 == True:
            "Tsubasa took that from me. And while I might be betraying her latest rule right now, I can reclaim {i}some{/i} part of myself in cumming for {i}this{/i} girl instead of one of them."

        "I’m tried of feeling like a spectator despite knowing I’m the main character. I’m tired of having to take the backseat to monks. Smiles. Voices. Faces. Ghosts. {i}Everything.{/i}"
        "All I want is to feel whole, but with pieces of me spread out all over Kumon-mi, that seems nigh impossible most days."
        "So here I am, hoping to find one of them buried somewhere deep inside of her. But realistically, all I know that I’m going to pull out of this is one more connection I’ll never be able to follow through with."
        "Just for tonight, though — maybe she can feel like a main character too."
        "And maybe she won’t have all of those downsides that come with it."

        s "Cum for me...again..."
        ima "HaaaAAAaaaahHhhh! Aaaahhh! Sen...pai! You’re so...hard! You...cum too!"

        scene imanixmaspenis30
        with fade

        s "You want me to do it inside?"
        ima "Yes! Yessss! I want it all! Everything...you’ve got! Now and...forever!"
        s "Are you proposing to me mid-orgasm?"
        ima "Haah! Haaah! Is it working?!"
        s "I don’t think so."
        ima "Then no! "
        s "I {i}am{/i} about to cum, though. "
        ima "First person to cum...gets to make the other person do anything they want!"
        s "You came like three seconds in."
        ima "Oh! Hah! Would you look at that?! I guess...I did! And I would like...aah...to redeem...my command...on...the complete extraction...of every last drop of semen you have inside of you! Thanks!!!"
        s "Look at you, thinking you can give {i}me{/i} orders now just because I’m about to finish."
        ima "I’m sorry...Senpai! Please...fuck the...insubordination...right out of me!"
        s "Sure thing, Imani. Then, you can go back to all of the girls and pretend that I {i}didn’t{/i} just fuck your brains out while all of them were busy pining over me."
        ima "I’m...gonna die! Aaaah!"
        s "Don’t worry. Chika’s scary, but she’s not {i}that{/i} scary."
        ima "No, I’m...gonna cum myself to death! I can...feel it! I don’t...know if I’ll make it back, Senpai!"
        s "Only one way to find out, I guess..."

        play sound "dosex.mp3"

        ima "HAH! HAH! HAH! YES! FUCK! OH MY GOD! SO GOOD! SO...BIG! SENPAI! DEEPER! DEEPER! FUCK ME! FUCK ME, FUCK ME, FUCK ME!"

        "Unable to control myself any longer, I try to hurt her once more. "

        with sexfade
        with sexfade
        scene imanixmaspenis31 with cumflash
        with hpunch
        stop music fadeout 12.0

        ima "EYAHAAAHHHHH!!!!!???!!!!~~~~~~~~ SENPAI! SEN...PAAAAIIIIIII!"

        scene black
        with dissolve2

        "But I only manage to hurt myself in the process. Because soon, December 26th is going to be here."
        "And soon, when I’m alone in bed, I’ll have to think about the sparing moments in which I {i}did{/i} feel like I loved her before someone else crawls her way into my head and reminds me why I wake up at all nowadays."
        "Imagine a world where things weren’t like that, though."
        "Imagine a world where I {i}didn’t{/i} repeatedly fall for the worst possible people. "
        "Now, imagine Imani is there with me."
        "Doesn’t it all look so...{i}so{/i} beautiful?"

        ima "Senpai..."
        ima "{i}Senpai...{/i}"
        ima "{i}Medɔ wo.{/i}"

        $ renpy.end_replay()
        $ christmasimani3 = True
        $ imani_love += 1

        "{i}Imani’s affection has increased to [imani_love]!{/i}"
        "........."
        "......"
        "..."

        jump christmasfive8

label imanilust5:
    if _in_replay:
        play music "ame.mp3"

    scene imanilustnaming1
    with dissolve

    s "Oh. Hi."
    ima "Hi. Wanna make out?"

    scene imanilustnaming2
    with dissolve

    s "Is it that time of night already?"
    ima "It {i}can{/i} be. Unless you have plans with {i}Nodoka,{/i} of course. Just, if that’s the case, I should probably call the cops."
    s "She just wanted to know if I would hug her."
    ima "Maybe I should just call them anyway?"

    scene imanilustnaming3
    with dissolve

    s "I don’t really get it either. But it’s Nodoka, so there’s probably no point in trying to make sense of it. "
    s "Alright then. Take your clothes off. Let’s get this over with."
    ima "Don’t sound {i}too{/i} excited there, buddy. "
    ima "I just wanted to spend some time alone with you since I doubt we’ll be able to talk much at all tomorrow with everyone else vying for your attention."

    scene imanilustnaming4
    with dissolve

    ima "And also because of your hot idol girlfriend at home who I’m definitely not jealous of."
    s "What about the others?"
    ima "Well, Rika started cheering Wakana up because she started feeling down. But that made {i}Rika{/i} start feeling down, so now Osako is cheering {i}her{/i} up."
    s "So who’s helping Wakana now then?"
    ima "Alcohol."

    scene imanilustnaming5
    with dissolve

    s "Oh, okay. So she’ll be fine then."
    ima "Yup! Which meeeaaaaaans..."
    s "You’re still clothed."
    ima "That’s never stopped you before. But hey, if you want to shake things up a bit, we could always head back to my place. "
    ima "Just have to be a {i}little{/i} quiet so we don’t bother Yuki. That lady’s been {i}pissed{/i} lately."

    scene imanilustnaming6
    with dissolve

    s "You’ve seen her?"
    ima "Hm? Of course I’ve seen her. I live next door."
    s "And she...hasn’t said anything?"
    ima "Just “keep it down in there or I’ll break the fuckin’ door down and beat you so hard that you’ll go deaf,” which feels highly improbable."
    ima "And was particularly odd because I wasn’t even making any noise that night. But hey, I know she’s got shit goin’ on."
    s "I see..."
    ima "Why? Something going on with her that you know about but I don’t?"
    s "Yeah...I don’t think it’s my place to say anything though. Just maybe don’t mention her around Yumi. "

    scene imanilustnaming7
    with dissolve

    ima "Oh yeah, Yumi! She’s actually been, like...weirdly present lately. Like she didn’t even put up a fight when we mentioned the Dorm Wars this year. And-"
    s "Sorry, I’m sad now. Can we have sex?"

    scene imanilustnaming8
    with dissolve

    ima "I mean...yeah. I {i}am{/i} the one who invited you over after all. But if this is something you seriously want to talk about, we can...you know...{i}talk.{/i}"
    ima "You know I don’t like when you just bottle stuff up, Senpai."
    s "I know. That’s where the sex comes in."

    scene imanilustnaming9
    with dissolve

    ima "Oh well! Can’t be helped, I guess. ‘Tis a kouhai’s job to please her beloved senpai, after all."
    s "Thanks, Imani. This is me giving you an imaginary coupon you can redeem at any moment you like for one free round of intercourse, no questions asked."

    play sound "winner.mp3"

    "{i}Imani has received [[1 FREE SEX COUPON].{/i}"

    scene imanilustnaming10
    with dissolve

    ima "Yay! New item! Time to start brainstorming the worst possible time to redeem it. "

    play sound "rainloop.wav" fadein 2.0
    scene raincheck
    with dissolve2

    ima "But for now, we must away! This body grows tired of bathroom sex! It’s time to let Senpai hit it where I fall asleep at night!"
    s "It’s still raining out there, isn’t it? Why don’t we just-"
    ima "I swear to fucking God that if you have some sort of complaint about not wanting to get underneath {i}my{/i} umbrella either, I’m going to curse you for all eternity."

    stop music fadeout 15.0
    stop sound fadeout 10.0

    "I sigh to myself and get beneath the umbrella with Imani. And while I expect to have to hold it, that winds up not being the case at all."
    "It’s somewhat surprising how often I forget how close to my height she is, though I can’t say if that’s due to her demeanor or the fact that everyone {i}else{/i} is just so small."
    "Regardless, I’m sure she feels cool right now. And I’m sure it wouldn’t be unwelcome for me to ask to hold it in her place. "
    "But I don’t — for I find it reasonable to allow her this rare opportunity to feel as if she is at the higher end of our power dynamic before I remind her physically that she isn’t."

    scene black
    with dissolve2

    "Though, who’s to say there’s that sort of dynamic at all anymore?"
    "For all we both know, I’m never coming back to school for more than just one day at a time at this point."
    "In a sense though, I guess that’s kind of how it {i}always{/i} was. "
    "Just a never ending sequence of toeing the line between wanting to be somewhere and wanting to be {i}nowhere{/i} at all."
    "I hope she enjoys it, at least."
    "And I think she does."
    "But it’s only a matter of time until someone ruins it for her."
    "Will that someone be me? "

    play sound "dooropen.mp3"

    "Or is it one more thing I can blame on God?"

    scene imanilustnaming11
    with dissolve2
    play music "asobeatsex2.mp3"

    "I’m reminded of Christmas in the way we enter her room. Just this time, it’s far less passionate and steamy and a lot more...{i}cute.{/i} At least for now."
    "Once the door is closed, she rests her head on my shoulder and looks up at me with those bright blue eyes I’ve found myself unintentionally falling into many times before."
    "But there’s a brief of moment of respite before the thoughts roll in of how they'd look filled with tears and squinting as I pump her full of fluids."
    "Maybe I am growing? Or maybe I am just permanently sick."

    ima "Soooooooo...I have an idea."
    s "You do, do you?"
    ima "Mhmmm. You wanna hear it?"
    s "Would you not rather just {i}show{/i} me, Imani?"

    scene imanilustnaming12
    with dissolve

    ima "I {i}will{/i} show you, Senpai. I just feel like I should {i}inform{/i} you first since I’ll be being a {i}very{/i} bad girl."

    scene imanilustnaming13
    with dissolve

    ima "You see...you’re always the one in control when we do it. And I love that about you. I love being...{i}under{/i} you."

    scene imanilustnaming14
    with dissolve

    ima "But I {i}also{/i} feel like, as your kouhai, it’s my job to support {i}you{/i} sometimes. Which is why all {i}you{/i} need to do today is lie down."
    s "So your “idea” is just being on top?"
    ima "There’s a second part. {i}That{/i} one is a surprise, though."
    s "Okay, Imani. You have convinced me. And it wasn’t very hard."
    ima "Oh, it {i}will{/i} be. I’ll make sure of it."
    s "I have an idea as well, though."

    play sound "static.mp3"
    scene imanilustnaming15 with flash
    stop sound

    ima "You do?"
    s "I do. Imani — you’re a woman who appreciates {i}shaking things up,{/i} aren’t you?"
    ima "Yeah, but I’ve never pegged anybody before so-"
    s "No. What? No. That’s not-"
    ima "There’s no need to be ashamed, Senpai. I’m sorry if you thought that’s what I was suggesting when I mentioned wanting to take care of you, but-"
    s "Imani, no. I just want you to call me something else while we’re sleeping together."

    scene imanilustnaming16
    with dissolve

    ima "Oh! "
    ima "Well, don’t I look like a filthy pervert then?"
    s "You are forgiven, don’t worry. I have heard much worse from the proprietor of a local porn shop."

    scene imanilustnaming17
    with dissolve

    ima "What do you want me to call you, then? I’m excited to hear it."

    jump imaninaming

label imaninaming:
    $ imanimaster = renpy.input("Enter a name for Imani to call you...")
    $ imanimaster = imanimaster.strip()

    if imanimaster.lower() in ["senpai"]:
        s "I want you to call me Senpai."

        scene imanilustnaming18
        with dissolve

        ima "But you just said-"
        s "I changed my mind. I realized there’s nothing better than what you already call me."
        ima "Not even, like...{i}Daddy{/i} or {i}Master{/i} or-"
        s "No. And I feel as if forcing you to call me those things would be disrespectful to you. So just keep calling me Senpai."

        scene imanilustnaming19
        with dissolve

        ima "I mean...okay. Feel like this whole conversation kinda just blue-balled me, though."
        s "I apologize for that as well."

        jump endofimaninaming

    if imanimaster.lower() in ["imani"]:
        s "I would like for you to call me Imani from now on."

        scene imanilustnaming20
        with dissolve

        ima "Senpai, do I look like a joke to you?"
        s "No. You look like an Akira. Which is why that is what I will call you from now on while you are calling me Imani."
        ima "I knew it. You {i}do{/i} want to be pegged."
        s "No. I just want to experience what life and sex are like as a person named Imani Imai."
        ima "So you’re taking my last name too?"
        s "That’s right. And you’re taking mine."
        ima "Not gonna lie, I’ve envisioned taking your last name before. Never quite like this, though."
        s "You’re also going to be Ami’s dad from now on. And I am going to live here. I hope you’re ready for Niki’s sex drive."

        scene imanilustnaming21
        with dissolve

        ima "I’m too horny for all of this nonsense! Can you stop fucking {i}around{/i} and just {i}fuck{/i} me if you don’t have anything you actually want me to call you?!"
        s "Hold on. I just came up with something else."

        jump imaninaming

    if imanimaster.lower() in ["wakana"]:
        s "I would like for you to call me Wakana while we’re having sex."

        scene imanilustnaming22
        with dissolve

        ima "Uhh...{i}why?{/i}"
        s "It’s just such a beautiful name, isn’t it?"
        ima "Yeah. I’ve said that same exact thing to our friend who already has it."
        s "Since when do we have a friend named Wakana?"

        scene imanilustnaming21
        with dissolve

        ima "We were literally just with her! She has purple hair! You know! The one who’s probably even better at pleasing women than you are!"
        s "Impossible. I’m willing to put money on having more sexual experience than anyone in Kumon-mi. Except maybe Rika."
        ima "Why do you remember Rika and not Wakana?! You guys are way less close and haven’t known each other nearly as long!"
        s "Imani, I think you’re just making this Wakana person up. We don’t know anyone with that name."
        ima "I’m too horny for all of this nonsense! Can you stop fucking {i}around{/i} and just {i}fuck{/i} me if you don’t have anything you actually want me to call you?!"
        s "Hold on. I just came up with something else."

        jump imaninaming

    if imanimaster.lower() in ["osako"]:
        s "Can you call me Osako from now on? Just during sex, of course."

        scene imanilustnaming22
        with dissolve

        ima "Uhh...{i}why?{/i}"
        s "Frankly speaking, she makes me feel insignificant as both a male and a partner. And I feel as if using her name during sex will allow me to reclaim a bit of my pride."

        scene imanilustnaming23
        with dissolve

        ima "That...actually kind of makes sense."
        s "It does?"
        ima "Yeah. I mean, Osako is stronger than you. Cooler than you. {i}And{/i} she gets to bang Wakana, which you have definitely wanted to do for a very long time."
        ima "It makes sense that you’d want to be her. I just don’t know if I can call you that without thinking about it."
        s "So you think calling me Osako while having sex with me will just make you think of having sex with Osako?"
        ima "Right. Which I believe would really only {i}add{/i} to your problem at the end of the day if you feel inferior to her."
        s "That’s a good point."
        s "But maybe if I call {i}you{/i} Osako-"
        ima "Not really a fan of that either, Senpai."
        s "Ugh...fine. I’ll think of something else."

        jump imaninaming

    if imanimaster.lower() in ["rika"]:
        s "How about you call me Rika from now on?"

        scene imanilustnaming24
        with dissolve

        ima "And give you the opportunity to rank my performance in the middle of sex? Hard pass."
        s "Technically, I could already rank your performance in the middle of sex. Just now, I’d be doing it while playing the role of one of our friends."

        scene imanilustnaming25
        with dissolve

        ima "Wait, you want to {i}act{/i} like her too?"
        s "Yeah. I figure it’ll help me get closer to Rin if I learn how to effectively mimic the behaviors and speech patterns of one of her moms."
        ima "And you believe that the best way to do this is by specifically only acting like and being addressed as Rika {i}while{/i} having sex with me."
        s "I’m a method actor and Rika has just had a lot of sex in her life. Trust me, it makes sense."
        ima "I’m not sure it does, Senpai. Nor do I like the idea of my body being some sort of rehearsal for you so you can get closer to a teenager."
        s "Fine then. I guess I’ll just make {i}Rin{/i} call me Rika, then. I hope you’re happy, Imani. You’ve put her in a very uncomfortable position."
        ima "I think I can relate. But if you don’t have anything else-"
        s "I do. Something just came to me."

        jump imaninaming

    if imanimaster.lower() in ["selebus"]:
        s "I would like for you to call me Selebus from now on."

        scene imanilustnaming15
        with dissolve

        ima "Selebus? Is that, like...your secret online handle or something?"
        s "No. It’s actually the handle that belongs to the guy responsible for creating us."
        ima "{i}Creating{/i} us? What do you mean?"
        s "I mean that we’re characters in a video game that are beholden to his whims. And if you call me by his name, I imagine it will appease him and he’ll make our lives better."
        ima "My life is already pretty good, though."
        s "Well, mine isn’t. And I need all the help I can get."
        ima "Well, if it’s just a video game...maybe you don’t really need help at all? Because you’d be fake, right? Which would mean you don’t have real feelings."
        s "But they {i}feel{/i} real and I have so many of them. So just call me Selebus, please."
        ima "And if I don’t?"
        s "He could delete you at any moment."

        scene imanilustnaming26
        with dissolve

        ima "Oh, please. As if he’d actually delete something he created for the sole purpose of-"

        play sound "broken.mp3"
        scene imanilustnaming27 with flash
        scene imanilustnaming28 with flash
        scene imanilustnaming27 with flash
        scene imanilustnaming28 with flash
        scene imanilustnaming29 with flash
        scene imanilustnaming28 with flash
        scene imanilustnaming29 with flash
        scene imanilustnaming30 with flash
        stop sound

        ima "I have seen the eyes of God."
        s "So you’ll call me Selebus then?"

        scene imanilustnaming31
        with dissolve

        ima "Yes! But only because I fear death! Keep that in mind!"
        s "Awesome."

        jump endofimaninaming

    if imanimaster.lower() in ["kwesi"]:
        s "You might hate this, but I’d like for you to call me Kwesi from now on."

        scene imanilustnaming32
        with dissolve

        ima "{i}Might{/i} hate it?"
        ima "You want me to address you by the same name of the boy who ruined my life and my body and you think I only {i}might{/i} hate it? What the fuck, Senpai?"
        ima "Is this some kind of fetish thing?"
        ima "Because I’m normally not against kink-shaming. But if you derive sexual pleasure from making me relive my greatest trauma, I think I might have to call this off."
        s "Hear me out, though. What if it helps you get {i}over{/i} that trauma?"
        ima "Then it crosses the line into cultural appropriation. Find me one Japanese dude named Kwesi and I’ll reconsider reconsidering."
        s "Right here. Kwesi Arakawa."
        ima "Please stop."
        s "Ugh...you never let me have any fun."
        s "I’ll just think of something else."

        jump imaninaming

    if imanimaster.lower() in ["sensei"]:
        s "I would like for you to call me Sensei."

        scene imanilustnaming33
        with dissolve

        ima "No!"
        s "What?"
        ima "I said no! Senpai is Senpai and Imani is his kouhai. And she will not call him Sensei no matter how badly he may want her to."
        s "I...don’t think I understand."

        scene imanilustnaming34
        with dissolve

        ima "It’s just important to your identity, that’s all. And, this may sound a lot less believable in roughly five minutes, but I don’t want to blur the line that separates us."
        ima "I fell for you despite the clear divide between our respective roles. To erase that line would be to erase the bridge that brought us together."
        ima "And I don’t want to live in a world where I have to shout at you from across a bridge. I want to be with you for as long as you’ll let me. As your precious underling."
        s "Imani, I think you’re making too big of a deal out of this. Just fucking call me Sensei. Everyone else does."
        ima "Imani Imai is not {i}everyone else.{/i} Imani Imai will always remember who we are to one another."
        ima "Just again, forget I ever said this in five minutes."
        s "Ugh, fine. I’ll just think of something else."

        jump imaninaming

    if imanimaster.lower() in ["oniichan", "onii-chan", "big bro", "big brother", "onii", "niichan", "nii-chan"]:
        s "I’d like for you to call me [imanimaster] from now on."

        scene imanilustnaming34
        with dissolve

        ima "Aww! Do you see me as a little sister now? Of the adopted variety that you can sexually experiment with while our parents are away from home?"
        s "That’s right. And that reaction tells me you’re probably going to be okay with this."

        scene imanilustnaming35
        with dissolve

        ima "Mhm! Honestly, I think it’s mega hot. And I may or may not already have a fair amount of experience in this field."
        s "Are you...are you trying to tell me something right now, Imani?"
        ima "Hm? What are-"

        scene imanilustnaming36
        with dissolve

        ima "Wait, no! Not like, {i}with{/i} my siblings! Ew! I can’t believe you interpreted it like that!"

        scene imanilustnaming37
        with dissolve

        ima "I just...kind of wrote a lot of smut in college. For fun. And the whole adopted siblings thing, just...you know...it really did it for me."
        s "So what I’m hearing is that you’re {i}really{/i} into this. And {i}haven’t{/i} ever actually experimented sexually with a sibling."
        ima "Not willingly at least."
        s "Oh. Fuck."

        scene imanilustnaming38
        with dissolve

        ima "Just...yeah! If that’s what you want me to call you, I’m all for it! Probably...{i}too{/i} for it. And I hope I don’t wind up creeping you out."
        s "..."
        ima "What? Why are you just looking at me like that?"
        s "I just think you’re really cute, Imani."

        scene imanilustnaming39
        with dissolve

        ima "And I...think the same thing about you...[imanimaster]."

        jump endofimaninaming

    else:
        s "I want you to call me [imanimaster]."
        ima "Then it shall be done. Let us commence the sex-having."

        jump endofimaninaming

label endofimaninaming:
    s "So, what was this {i}other{/i} surprise you wanted to show me?"

    scene imanilustnaming40
    with dissolve

    ima "Okay! So, you know how you’re a teacher, right? Or {i}were{/i} a teacher and are currently in a state of limbo?"
    s "I’m aware of these things, yes."
    ima "Cool. Lie down and close your eyes."
    s "What?"
    ima "Just close them! I want to do something."

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "Alright. I’ve learned by now that, when someone tells me to close my eyes, it’s {i}usually{/i} a good thing."
    s "And it’s not like you’re able to break into my daughter’s room right now in the midst of my vulnerability, so I have no reason to be worried."
    ima "I suddenly have a lot of questions, but I’m too busy getting changed and trying to look pretty to ask any of them."
    s "So this thing you want to do is a {i}costume change{/i} then."
    ima "{i}And{/i} a little bit of roleplay, I suppose. Maybe help fulfill some {i}twisted fantasy{/i} of yours."
    s "Not {i}yours{/i} of course, though. Because it was {i}my{/i} idea to have you do this and you’re only doing it {i}for{/i} me."
    ima "Mmm...it’s a fantasy of mine too. Just in the more submissive way and not the kind that would make me {i}evil{/i} if it were to ever come true."
    s "I’m suddenly confused, but I think I know where you’re headed with this."
    ima "Great. Because I am now done and you may open your eyes."

    scene imanilustnaming41
    with dissolve3

    "What I see before me is exactly what I expected."
    "I knew Imani had this outfit from a prior Halloween, and when it comes to teacher-based fantasies, there are only so many one can come up with."
    "Combine that with her ever-present desire to remain {i}youthful{/i} and you get this."

    ima "All of the student, none of the shame. What do you think?"
    s "Wow. You even changed your earrings."
    ima "I stand before you decked out in a student uniform and you comment on my {i}earrings?{/i} Impressive."
    s "Yeah well, commenting on every little thing would take up the rest of the day and I kind of can’t wait to fuck you right now. So that’s all you’re getting."

    scene imanilustnaming42
    with dissolve

    ima "Anything I could do for a little...extra credit? Maybe something that would...get you in trouble if anyone were to ever find out?"
    s "Are you coming onto your teacher right now, Imani?"
    ima "I just know my grade in algebra has been a little lacking lately and...I was hoping there was something I could do to...{i}get it up.{/i}"
    ima "And surely a man as busy as you could use a little...{i}release...{/i}don’t you think?"
    s "How long have you wanted to do this for?"
    ima "Is that in-character or out-of-character?"
    s "Out-of-character."
    ima "From the moment I first put this on."
    s "Knew it."

    scene imanilustnaming43
    with dissolve

    ima "Yeah, Imani Imai, turned on by a kinky power dynamic. Who would’ve thought?"
    ima "None of my teachers growing up were attractive, so {i}I{/i} never got to fantasize about getting pounded by one like all of {i}our{/i} girls totally do with you."

    scene imanilustnaming44
    with dissolve

    ima "Unfortunately, they’re all still too young to see that to fruition. But {i}I’m{/i} not. So you can do anything you want to {i}me.{/i}"
    ima "And I mean {i}anything.{/i} There’s nothing I’m not willing to do for a little extra credit, [imanimaster]."
    s "Except for letting me be on top, which you have already claimed today."

    scene imanilustnaming45
    with dissolve

    ima "Technically speaking, there are probably a lot of things I wouldn’t let you do. It just sounds way less sexy when I say that and I’m trying to be a seductive student right now."
    s "With nipple piercings."

    scene imanilustnaming46
    with dissolve

    ima "What can I say? I’m a {i}bad girl.{/i}"
    s "Well, {i}bad girl...{/i}I’m waiting. But feel free to stand there and strip for me a little while longer if you like."

    scene imanilustnaming47
    with dissolve

    ima "Ahh, but there’d be no point in wearing this uniform at all if I was just going to take it off, [imanimaster]."
    ima "Tonight, you’re gonna see me as a student. And you’re going to give it to me in a way you’ve never given it to anyone else before. Okay?"
    s "Imani-"
    ima "It’s fine. It doesn’t mean anything."
    ima "It’s all just fantasy."

    scene black
    with dissolve2

    ima "Now take your clothes off and let me {i}work{/i} for a better grade..."

    "I do as Imani says as she moves to the light, switching it off and immediately changing the atmosphere of the room into one a lot more...serious."

    ima "Mnh..."

    "She gets onto the futon beside me and begins to bite my ear."
    "Her hands wander along my body until one lands in my lap."
    "Her fingers curl around my cock, gently tugging it and getting it harder as she continues to bite me."
    "The sound of each and every whisper and moan is amplified tenfold by our proximity."
    "It’s deafening, almost — held back by nothing more than the fact that I have already been here before."
    "I have felt this in the most impure context imaginable."
    "But the fact that it {i}isn’t{/i} this time..."
    "Feels...better somehow?"

    scene imanilustnaming48
    with dissolve2

    "She climbs into my lap and straddles my waist, gripping my cock and guiding it to her entrance as she locks eyes with me."

    ima "So big, [imanimaster]...I wonder if I can take it all?"
    s "You’ve taken it tons of times, Imani."
    ima "Shh...{i}nooooo.{/i} I’m a virgin, [imanimaster]. I’ve been saving my first time for when I {i}really{/i} need a better grade."
    s "Just how bad are you at algebra?"
    ima "Bad enough to let a man so much older than me claim my innocence. Aah..."

    "She winces as the tip of my cock slides into her pussy, then hovers there for a moment, stroking me gently as she revels in the sensation."

    ima "It’s in...I can’t believe I’m...letting you do this to me..."
    ima "But more than that...I can’t believe...how badly I {i}want it...{/i}"
    s "Yeah...not as badly as me. Get over here."
    ima "[imanimaster]? Wha-"

    play sound "static.mp3"
    scene imanilustnaming49 with flash
    stop sound

    ima "MNGH?!!?"
    s "You have no idea how this roleplay works...do you, Imani?"
    s "The whole point of this fantasy isn’t for the student to seduce the teacher. It’s the other way around."
    s "You’re playing a high school girl, right? Do you think they just do things like this on their own?"

    scene imanilustnaming50
    with dissolve

    ima "I’ve...met Kirin...so yes!"
    s "Okay...well, maybe {i}some{/i} of them do. But that’s not where the {i}allure{/i} lies. That comes from the act of {i}making{/i} them want you."
    s "It’s no fun if it just happens on its own."
    ima "Mngh...then what...do you want me to do?!"
    s "I want you to fall for me."
    ima "But I’ve already-"

    play sound "dosex.mp3"
    scene imanilustnaming51
    with hpunch

    ima "MNGHHGH!??!"
    s "I want you to become obsessed with me. I want to be the sole entity guiding the principles of your maturation. And I want {i}most{/i} of it done behind the scenes."
    s "I want you staying up late, fingering yourself to thoughts of me while every girl in every other room that lines your hall does the same thing."
    s "Only {i}sometimes{/i} will I call on you. When I’m lost. Lonely. Maybe even just hard. And I expect you to spread your legs on demand."
    s "Because if {i}you{/i} don’t, there are nineteen other girls who will."
    s "{i}That{/i} is what this fantasy is."

    scene imanilustnaming52
    with dissolve

    ima "Mnngh! [imanimaster]! You’re fucking me...too hard! How am I...supposed to focus on...pleasing {i}you{/i} like this?!"
    s "You’re doing your job by just being there, Imani. That’s all I need from you."

    scene imanilustnaming53
    with dissolve

    ima "That’s not...enough!"
    s "...I’m sorry?"
    ima "You’re not the only one...who gets to fantasize!"
    ima "The...chase! The...drive to be claimed by someone with experience! To lose yourself in pleasures you...can’t yet comprehend!"
    ima "To explore and...haah...{i}learn{/i} things about yourself! To make mistakes! To do...the opposite of what your parents want!"
    ima "It happens...to all of us! We’re just...trying to find our place in the world! And sometimes...that place is...in bed with the devil!"

    "Imani slams her waist down, consuming all of me and reminding me through both this {i}and{/i} her words that she is, without a doubt, a fully formed human."
    "But again...I like it. And I find that strange."

    scene imanilustnaming54
    with dissolve

    ima "Yeah...you love my little pussy, don’t you [imanimaster]? Are you adequately {i}immersed?{/i} Confuse me for a real-life high-schooler?"
    ima "Are you {i}actually{/i} sick? Is THAT why you’re fucking me so hard right now?! Pervert! I bet you’ll cum {i}before{/i} me at this rate!"
    ima "And that’s exactly what I want, so go right ahead! Think about whatever the fuck you {i}want{/i} to think about!"

    scene imanilustnaming55
    with dissolve2

    ima "Just don’t force it on me. I don’t need your help to sin."

    "My grip, which was never really {i}tight,{/i} loosens around Imani’s throat as she somehow manages to climb over one of my walls to take her place back on top of me."
    "I assumed she’d left as I once again forgot what I was dealing with."
    "But what I feel now is the frantic bouncing and grinding of another girl who, by all accounts, I could find some semblance of happiness with if I were to never leave this room."
    "Unfortunately, there will always be that curiosity. That desire to see this uniform on other humans. Which will inevitably turn into something else."

    ima "Fucking cum in me...cum in me, [imanimaster]! Do it, do it, do it! Cum inside my tight, schoolgirl pussy! Be bad for me! Be bad for me! Like I’m bad for you! Do it!"
    s "Im...ani..."

    scene imanilustnaming56
    with dissolve2

    ima "Aaah! Aah! [imanimaster]! Yes! I’m gonna cum too! You’re too big! It’s so deep! It’s so deep inside my needy, pervy, wet fucking pussy! Oh FUCK yes! Yes, yes, yes!"

    play sound "knock.mp3"
    yu "{i}FUCKING SHUT UP! JESUS CHRIST!{/i}"
    ima "AAAH! AAAH! SORRY, YUKI! HOPE...EVERYTHING IS...AAAH! SENPAI!"
    s "Look at me...now..."

    scene imanilustnaming57
    with dissolve

    ima "Aah...aaaaah....aaaaaah!~"
    s "What if this was real?"
    ima "Haaah...haaha! Aaaghhh! It’s...not...though!"
    s "But what if it was, Imani?"
    s "Would you still be riding me like you’re fucking addicted?"
    s "Or would you be another girl just playing with herself while thinking about me?"
    ima "You are...seriously...the most conceited man...I have ever met!"
    s "You pulled this out of me, you know. {i}I{/i} just wanted to be your friend."

    scene imanilustnaming58
    with dissolve

    ima "I...regret...nothing! Just fucking cum in me! Cum for me! Cum inside my needy fucking-"

    with sexfade
    with sexfade
    scene imanilustnaming59 with cumflash
    with hpunch

    ima "HAAAH! AAAH! AAAAAAH....AAAAAH...."
    s "Ngh!...Mngh!...Mmmf!"

    scene imanilustnaming60
    with dissolve2

    ima "Aah...haah...[imanimaster]...yes...let it all out...every...last...drop..."
    s "Mmnghhh! You’re...fucking..."
    ima "Amazing? Beautiful?"
    ima "Full of {i}youth?{/i}"

    scene black
    with dissolve2

    s "So...hot!"
    ima "Hehehahah!!! I’ll take it! And don’t mind me if I...keep going!"
    s "There’s...no way...I can-"
    ima "Never...say never!"

    "Imani goes right back to riding me and I..."
    "I’m not really sure...what to take away from all of this."
    "Does she...{i}understand{/i} what I am now?"
    "Is she still just playing?"

    stop music fadeout 10.0

    "It’s like I barely have a chance to think with how intense she is tonight."
    "But is that {i}my{/i} doing?"
    "Or is it just something about that fucking uniform?..."

    $ renpy.end_replay()
    $ imanilust5 = True
    $ imani_lust += 1

    "{i}Imani’s lust has increased to [imani_lust]!{/i}"

    "........."
    "......"
    "..."

    hide friday onlayer date
    show saturday onlayer date

    $ day = 6
    $ totaldays += 1

    jump dormwarsfive3
