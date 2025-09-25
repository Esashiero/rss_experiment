label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
    if sana_love >= 10 and sanafirsthall == True and bar10 == False:
        jump bar10
    if sana_love >= 15 and bar10 == True and bar15 == False:
        jump bar15
    if sana_love >= 20 and day65 == True and bar15 == True and amisroom5 == True and bar20 == False:
        jump bar20
    if sana_love >= 25 and sanadorm20 == True and makidate1 == True and bar25 == False:
        jump bar25
    if sana_love >= 30 and sanadorm25 == True and day120 == True and bar30 == False:
        jump bar30
    if sana_love >= 35 and utamaid5 == True and christmas7 == True and bar35 == False:
        jump bar35
    if sana_love >= 40 and sanadorm35 == True and bar40 == False:
        jump bar40
    if sana_love >= 45 and thirdreset3 == True and futabadorm45 == True and bar45 == False:
        jump bar45
    if sana_love >= 50 and day351 == True and sarasex == True and sanadorm50 == True and bar50miss == False and bar50 == False:
        jump bar50
    if sana_love >= 55 and imanispecial1 == True and day < 5 and bar55 == False:
        jump bar55
    if saraspring3 == True and saraspring4 == False:
        jump saraspring4
    if chap4active == True:
        jump sanaspringbargen
    if chapthreeactive == True:
        jump sanasummer2bargen
    if christmas7 == True:
        jump bargen2
    else:
        jump bar2to4

label callsanamorning:
    play sound "phonebeep.wav"
    "I tap on Sana's name in my phone and wait for her to answer..."
    "........."
    "......"
    "..."
    "She doesn't."
    jump callmorning

label callsanaafternoon:
    play sound "phonebeep.wav"
    "I tap on Sana's name in my phone and wait for her to answer..."
    "........."
    "......"
    "..."
    "She doesn't."
    jump callafternoon

label callsananight:
    play sound "phonebeep.wav"
    "I tap on Sana's name in my phone and wait for her to answer..."
    "........."
    "......"
    "..."
    "She doesn't."
    jump callnight

label sanainvite:
    if sanainvite1 == False:
        jump sanainvite1
    else:
        jump sanainvitegen

label sanainvitegen:
    play sound "phonebeep.wav"

    "I tap on Sana's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    sa "Hello?..."
    s "Hey. Are you busy right now?"
    sa "Uh...I can...{i}not{/i} be busy right now if...you want to see me?"
    s "Works for me."

    scene black
    with dissolve

    s "Come on over."

    "........."
    "......"
    "..."

    scene sanainvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    sa "So...um...what do you want to do?..."

    "How should I spend my time with Sana?"
    menu sanainvmenu:
        "Hang Out (Raise Affection)":
            jump sanainviteaff
        "Thighjob (Raise Lust)":
            jump sanainvitethighjob
        "Headpat":
            jump sanaheadpat

label sanainviteaff:
    scene sanainvitegen
    with fade

    "Sana and I decide to take it easy and {i}not{/i} engage in anything sexual today."
    "But seeing as I'm boring and she still needs a way to stay occupied, she pulls out her Switch and crawls into my lap."
    "I watch her play games as I hold her from behind, responding sparingly every time she glances back to see if I'm still paying attention."
    "And I am. But I spend less time focusing on the game itself and more time observing the size of her fingers and the ways she's able to move them."
    "It's interesting...knowing that she's a living being inhabiting the same space as me. That I'd already done so much before she was even conceived."

    scene black
    with dissolve2

    "But even more interesting than that is that despite this, she seems more comfortable with me than I've ever seen her with anyone else."
    "Even Ayane seems to be falling victim to my hold on Sana now. And while it may not be her heart in my hands, whatever it is seems very important to her."
    "So small. So fragile. So...{i}mine.{/i} And why? Because I'm here? Because of coincidence?"
    "I stare more at her fingers and try to forget, admiring the slender fleshworms that guide her on-screen body."
    "I silently thank the beings that brought her into existence."
    "I can name one of them. But for the other, all I can do is understand."

    $ sana_love += 3
    stop music fadeout 5.0

    "{i}Sana's affection has increased to [sana_love]!{/i}"

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

label bargen2:
    scene sananightgen2
    with dissolve
    play music "calmbar.mp3"

    "I walk for quite a while in the snow and wind up at the bar with Sana."
    "She's in a much better mood than usual, but still displays a sense of uneasiness about my health when she realizes that I'll just be walking back after this."
    "This is the part where most other girls I know would offer to walk with me or even let me stay over but-"
    "Well, Sana doesn't do either of those things."
    "She just cracks me open a bottle of the same beer I always buy and spends the next hour or so whispering back about whatever topics I bring up."
    "But even if she's just as quiet and slightly-detached as she always is, it's an enjoyable night."
    "I just wish she'd show a little more initiative in sparking conversation rather than just going along with whatever I say."

    scene black
    with dissolve

    "I stay until closing and then offer to walk Sana back to the dorm since she never personally brought up the prospect of us leaving together."
    "She gets embarrassed and ultimately refuses, to which I oblige."
    "I obviously don't want her to walk back alone, especially on a night as cold as this, but there's not much I can do about it at this point."
    "Let's just hope she isn't carried off by the wind and thrown into some nearby body of water to develop hypothermia and die."

    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana's affection has increased to [sana_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label firsttimebar:
    play music "calmbar.mp3" fadein 2.0
    scene firstbar1
    with dissolve

    "I decide to close out the night with a trip to the bar."
    "I’ve yet to have a drink since the whole reincarnation thing, and I’m sure Ami won’t mind if I stay out a little late every once in a while."

    s "..."

    "Look at me, thinking some teenage girl has some amount of influence over my behavior."
    "I must be getting soft."
    "The bar looks decently upscale for the area it’s in, but there aren’t any customers apart from a few old women smoking cigarettes in the corner."

    scene black
    with dissolve

    "I walk past them and take a seat at the bar, not noticing until now that the bartender looks exceedingly familiar..."

    scene firstbar2
    with dissolve

    sa "Uh..."
    s "...Sana?"
    sa "Um..."
    sa "Uh..."
    sa "H..."
    sa "Hello..."
    s "I had no idea you worked at a bar."

    scene firstbar3
    with dissolve

    sa "I...know it’s against the rules..."

    scene firstbar4
    with dissolve

    sa "Am I...going to get in trouble?..."
    s "With me? No. I’m not here to tell you how to live your life."
    s "Just try and keep it a secret from anyone more important than me and I'm sure you'll be fine."

    scene firstbar5
    with dissolve

    sa "You...really mean that?..."
    sa "Because...when you walked in, I-"
    s "I mean it. I {i}am{/i} a little surprised you work somewhere like this, though."

    scene firstbar6
    with dissolve

    sa "How come?"
    s "You just...don’t really seem like the bartender type, I guess?"
    sa "What is the...bartender type?..."
    s "Probably someone old enough to legally drink. But I'm sure you hear enough of that from your customers."

    scene firstbar7
    with dissolve

    sa "Umm...not really..."
    sa "Most of the people who come here have been coming here for years...so I've known them for a really long time..."
    s "How long have you been working here, exactly?"
    sa "I haven't been...{i}working{/i} here for long...but my mom lives upstairs, so...I...kind of grew up here...or something."
    s "You live above a bar? That's amazing."
    sa "Well...{i}I{/i} live in the dorms now, so..."
    s "Shame. Though, I guess that probably helps with you not becoming an alcoholic at an early age. Not that I imagine you drink much to begin with."
    sa "R-Right..."

    "Sana doesn’t seem much different than she does in class. She’s still just as quiet as ever."

    if bonus == True:
        "Well- scratch that. She {i}does{/i} seem different. But only in the fact that she is significantly more adorable in her work clothes than she is in her school uniform."
        "Which is a weird thing to admit since my attraction to school girls has been slapping me across the face ever since {i}waking up.{/i}"
        "Either way, I am now obligated to test the waters and compliment her appearance because that is just the type of guy I am."
    else:
        "I have also noticed that her clothes are the perfect size for her based on my years of experience in fashion design."

    s "Those clothes fit you well, Sana."
    sa "..."
    s "Sana?"
    sa "Oh...sorry...Thank you..."
    sa "It's just...they were my brother’s."
    s "Were? Does he not work here anymore?"

    scene firstbar8
    with dissolve

    sa "I..."
    sa "That's not...really something I want to talk about right now...if that's okay..."

    scene firstbar9
    with dissolve

    s "That's fine. I'm not going to push you out of your comfort zone until the second or third time we hang out after class..."
    sa "I...don't think that's...a thing we should do..."
    s "That aside, do you think you could pour me a drink? That's kind of the whole reason I'm here, after all."

    scene firstbar5
    with dissolve

    sa "You drink, Sensei?"
    s "What other reason would I have to come to a bar?"

    scene firstbar7
    with dissolve

    sa "Oh...yeah...hahah..."
    sa "R-Right..."

    scene firstbar9r
    with dissolve

    sa "Well, what can I get for you then?..."
    s "Just a beer, thanks. I'm not really a liquor person."

    scene firstbar10
    with dissolve

    sa "Okay...Coming right up."

    scene firstbarnone
    with dissolve

    "Sana moves to the opposite end of the bar and opens up a cooler that must be at least twenty years old."
    "She pushes aside a few half-empty syrup bottles and grabs me a can of some beer I don't recognize."

    scene firstbar10
    with dissolve

    sa "Um...here you go..."
    s "What is this exactly?"
    sa "It's...umm..."
    sa "You...{i}did{/i} say you wanted a beer...right?..."
    s "Yeah, I just don't recognize this kind."

    scene firstbar7
    with dissolve

    sa "We...only carry alcohol from the local brewery, so...I'm sorry if it's not to your liking..."
    s "There’s a brewery in Kumon-mi?"

    scene firstbar10
    with dissolve

    sa "If there wasn't...we'd have a problem..."
    s "Well hey, beer is beer and I got what I asked for."

    "Sana pulls the tab of the can open and slides it over to me as if she's doing it from muscle memory but, well, I guess that's to be expected given the environment she's apparently grown up in."
    "Assuming she's not done {i}growing up,{/i} that is."
    "It’s still strange seeing someone so [young]doing a job like this, though."

    s "So how long has your family been running this place, exactly?"

    scene firstbar7
    with dissolve

    sa "Since...way before I was born..."
    sa "My grandma and grandpa opened the bar a long time ago..."

    scene firstbar10
    with dissolve

    sa "My...mom told me it used to be really popular when she was a little girl..."

    scene firstbar11
    with dissolve

    sa "But...now, it's..."

    "Sana's eyes navigate to the corner of the room, where the group of old women sit."
    "Now that she's redirected her attention over there, I become acutely aware that they've been mysteriously quiet ever since I showed up."
    "They're old, though. They probably just ran out of energy or something. That seems like an old-person thing to do."

    s "So I guess this place is pretty much the shell of its former self then?"
    sa "Yeah..."
    sa "That's a...good way to describe it..."

    scene firstbar12
    with dissolve

    sa "You don't...think it's because of me...do you?..."
    s "I mean, I’ve only been here once, so I can’t say for sure...but I highly doubt that’s it."
    s "If anything, I’d think having a bartender as cute as you would reel even more customers in."

    scene firstbar3
    with dissolve

    sa "That’s...uhh..."
    s "You could probably work on your social skills a bit, though."

    scene firstbar2
    with dissolve

    sa "Huh?"
    s "What I mean is that {i}I{/i} know you’re naturally this quiet, but newer customers might not get that right away."

    scene firstbar7
    with dissolve

    sa "I was...kind of worried that might be the case..."

    scene firstbar9
    with dissolve

    sa "Sensei...do you know any tricks to...you know..."
    s "Get better at having conversations with strangers?"

    scene firstbar3
    with dissolve

    sa "Y-Yeah..."
    s "Hm...Not really."

    scene firstbar12r
    with dissolve

    sa "I see..."
    s "It’s just something you sort of have to do if you ever want to make it through life."
    s "Look at me- I don’t like talking to strangers 99%% of the time, but I still do it because that’s just how life works."
    s "You can’t just avoid everything forever. If life were that simple, we wouldn’t need jobs or[school] or anything like that."

    scene firstbar7
    with dissolve

    sa "I...guess you’re right."
    s "You seem to be talking to me just fine, though."

    scene firstbar9r
    with dissolve

    sa "Well...I’ve talked to you before, so..."
    s "Maybe we just need to talk a little more, then?"

    scene firstbar2
    with dissolve

    sa "Talk...more?..."
    s "By opening up more to me, you might get better at opening up to others. Right?"

    scene firstbar7
    with dissolve

    sa "Um...I don’t really know about that..."
    s "That settles it, then."

    scene firstbar4
    with dissolve

    sa "Wait, settles what?...I'm...suddenly confused..."
    s "I’m going to help teach you some social skills whenever I drop by the bar."

    "It's not like I plan on teaching her anything in school, so this is just my way to make up for that."

    scene firstbar7
    with dissolve

    sa "Sensei, I...don’t really have time for extra classes..."
    s "Is it really an extra class if you're on the clock for it?"
    sa "Is that...really okay, though?...Isn’t this place...a little far from your home?..."
    s "It’s not that bad. Plus, if it’s for you, I don’t mind at all."

    scene firstbar4
    with dissolve

    sa "You really mean that?...You’ll go out of your way for me?..."
    s "Of course. You’re one of my students. Plus, it will give you an incentive to reward me with free drinks and that is always a plus."

    scene firstbar13
    with dissolve

    sa "Heheh...well...we'll...have to see about that part..."
    sa "Because...I don't really think we're in the position right now to...be able to do that..."
    s "Well, lucky for you, I'm paying tonight."

    "I chug the remainder of my beer and slide the can back to Sana."

    sa "That's...not exactly {i}lucky{/i} for me...That's just...kind of how...buying things works..."
    s "Then you're lucky I decided to stop by here instead of some other bar."

    scene firstbar10
    with dissolve

    sa "Heheh...that, I...can't argue with..."
    sa "Are you ready for another?"
    s "I’m fine for tonight, actually. I think I’m going to head out."

    scene firstbar9
    with dissolve

    sa "O-Oh...I see..."
    s "I’ll be back soon, though. Just keep trying to improve on your own in the meantime."

    scene firstbar3
    with dissolve

    sa "I’ll try but...I’m pretty bad...I can't really promise that...there will be any progress..."
    s "Well, I'm passable. So I'm sure everything will all work out in the long run."

    scene firstbar10
    with dissolve

    sa "Okay...I trust you..."
    sa "Goodnight, Sensei...I’ll see you soon."
    s "I'm sure you will."
    s "Goodnight, Sana."

    scene black
    with dissolve2

    "I take a handful of coins out of my pocket and leave them on the counter without ever asking for a bill."
    "I'm sure it's a lot more than necessary, but it's not like I have anything I'm saving up for. And spending that money on Sana might be a good tool to get her to open up to me."
    "Is that technically a form of bribery? Sure. I guess you could say that."
    "But if there's anyone bribery works on, it's a family in financial turmoil."
    "I start my journey home with slightly lighter pockets, but a slightly more optimistic outlook for the future."
    "And that's a fair trade to me."

    $ renpy.end_replay()
    $ firsttimebar = True
    $ sana_love += 1

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar2to4:
    play music "calmbar.mp3" fadein 2.0
    scene firstbar10
    with dissolve

    "I decide to visit Sana at the bar again."
    "We work on the basics of public speaking but she shows little to no signs of improvement."
    "I might need to figure out an alternative method of teaching soon."
    "Even though she’s still hesitant to converse with others, I can feel the two of us becoming slightly closer..."

    scene black
    with dissolve

    $ sana_love += 1

    stop music fadeout 3.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar5:
    scene bareredux1
    with fade
    play music "calmbar.mp3"

    "I walk into the bar to find absolutely no one- a small but noticeable change from last time."
    "I'm not really sure if this can be chalked up purely to me showing up late, either, considering Sana's already informed me of the struggling state of this business-"
    "But maybe it's even worse off than I thought?"
    "At the bare minimum, there should be at least one customer half-passed out behind the counter, silently drinking to him- or, sorry, {i}her{/i}self."
    "I'm still not fully used to the idea of there not really being any men around here yet, I guess."

    scene bareredux2
    with dissolve

    sa "Umm...Hi, Sensei..."
    s "Hey, Sana. Where is everybody?"
    sa "This...{i}is{/i} everybody..."

    if day < 6:
        sa "Weekdays...aren’t really that busy for us..."
    else:
        sa "Weekends...aren’t really that busy for us..."

    s "Yeah...I can see that."
    s "Would you mind if I took a seat? I’ve been walking for a while and I’m pretty exhausted."

    scene bareredux3
    with dissolve

    sa "O-Oh! Right! I’m...so sorry...I shouldn't have stopped you as soon as you walked in..."
    s "It’s fine. You were probably just so excited to see another human lifeform in here that you couldn't help but approach me as soon as the door opened."

    scene bareredux4
    with dissolve

    sa "What's...really sad is that...you're probably not wrong..."
    sa "Is it...okay if I sit next to you, though?..."
    s "What if another customer shows up, though?"

    scene bareredux5
    with dissolve

    sa "I...don’t really think we have to worry about that..."
    sa "I was...probably just going to close down soon anyway, so..."
    s "Then, sure. I don’t mind at all."
    s "It might be a good time to start your {i}lessons{/i} anyway."

    scene black
    with dissolve

    sa "As...good a time as any, I guess..."

    "Sana leads me over to the bar and politely pulls out a stool for me despite it being larger than her and probably weighing twice as much."
    "She may not have much faith in the business, but at least she's attentive when it comes to customers."
    "Or at least me."
    "To be fair, though, there haven’t been many opportunities to see how she acts around others."

    scene barfive1
    with dissolve

    sa "..."
    s "..."

    "I kick off the lesson by remaining completely silent and just observing how Sana acts around me."
    "And, if she had the confidence in herself to even look my way, she'd be made immediately aware of how creepy and unacceptable this method is."
    "Unfortunately for her, her inability to make eye contact has already resulted in her missing out on a valuable lesson."
    "Here's hoping she's at least {i}tried{/i} practicing in some way during my absence."

    s "So, any progress on your end lately? Have you been able to hold any conversations with anyone you're not directly related to?"

    scene barfive2
    with dissolve

    sa "Well...there's Ayane too, but...other than that...not really..."
    sa "I’ve been trying...but..."

    "Sana drifts off, as if she's expecting me to fill in the blanks of her inadequacies."
    "Which, to be fair, I probably could. But me doing the legwork isn't going to help her in any way."
    "If she's going to improve herself, she first needs to confront her problems head on."

    s "But what?"
    sa "It’s just...kind of hard without anyone to talk to..."
    s "I guess that's fair."
    s "Maybe try practicing in the mirror or something? Isn't that what actors do when they're first starting out?"

    scene barfive3
    with dissolve

    sa "Does that...actually work?..."
    s "Maybe. I've never tried. Just...pretend you’re someone else and try to strike up a conversation while...playing both sides?"

    scene barfive1
    with dissolve

    sa "That sounds...way too complicated..."
    sa "Plus...I don’t really like mirrors...so..."
    s "Why not?"
    sa "It's...kind of personal, so...if you don't mind..."
    s "Don't worry about it, then. We can just keep going like this."

    "I can't blame Sana for not wanting to just freely divulge personal information to me now that we're talking somewhat regularly."
    "No one should trust anyone until they're given a reason to- and I am no exception to that."
    "Sana needs time to grow."
    "Mentally, at least. Because, to be quite honest, I hope she stays her current size forever."

    s "Here's an idea, Sana. How about we try a little roleplay?"

    scene barfive3
    with dissolve

    sa "Roleplay?...You mean like...a game?"
    s "Sure. You can call it a game if you want. Just pretend I’m a customer and-"
    s "Well, actually, I {i}am{/i} a customer. But I’m sure you know where I’m going with this."

    scene barfive4
    with dissolve

    sa "Uh...yeah...if...if it's just a game...I can...probably do it..."
    s "Just to mix things up, though, I’m going to try and be difficult. Got it?"

    scene barfive3
    with dissolve

    sa "Difficult? How so?"
    s "I mean that I’m going to give you problems that might arise at the bar and you’re going to need to figure out what to do about them."

    scene barfive5
    with dissolve

    sa "You’re not...going to break anything...are you?"
    sa "Because...it comes out of my paycheck if you do..."
    s "First off, no. Second, do you really have to pay for things that break on your shift here?"
    sa "Well...no...But I’d...feel really bad if I didn’t..."

    scene barfive2
    with dissolve

    sa "Not having customers means my mom doesn't have much money, and...I wouldn't want her to pay for all of that out of pocket..."
    sa "So...if I can help by...paying for a few broken glasses...I don't really mind..."

    "I guess this means I can assume Sana’s dad isn’t in the picture either."
    "Is it really just Sana and her mom trying to keep this place afloat on their own? No wonder why they're going under."
    "There's only so much two people can do- especially when it comes to maintaining a place like this."

    s "Okay. Well, I promise to not break anything. I’ll just act kind of rude toward you or something. "
    s "Will you be able to handle that?"

    scene barfive5
    with dissolve

    sa "Well...can you tell me how rude you’re going to be?"
    s "Nope."
    sa "..."
    sa "But-"
    s "Sana, hurry up and get behind the bar. This is a trial by fire."
    sa "But...our extinguisher is...really old and...I don't know if it still works..."
    s "I'm going to ignore that extreme safety hazard for now and say it again. Get behind the bar."
    sa "Okay, but...I can already tell...I'm going to fail whatever this is..."

    scene black
    with dissolve2

    "Sana gets out of her seat and nervously rounds the corner into the bar area..."
    "She closes her eyes and takes a deep breath, though I'm not sure how much benefit it will have since I don't intend to pull any punches with this."

    scene firstbar4
    with dissolve

    sa "Umm...Hello, sir...What can I-"
    s "Yeah, whatever. Give me a beer and a plate of spaghetti."

    scene barfive6
    with dissolve

    sa "A plate of...spaghetti?..."
    s "Did I stutter? Or are you just really fucking bad at your job?"
    sa "Well...I don't think so...but..."

    scene barfive7
    with dissolve

    s "Listen kid, I’m in a hurry. So if you don’t have my spaghetti in five minutes, I’m gonna have to-"
    s "Wait, Sana, are you crying? We literally just started."
    sa "W...w...we...d...don’t...have any...s...sp...spaghetti..."

    "This is even worse than I thought."

    s "Sana, if this is too hard-"

    scene barfive8
    with hpunch

    sa "I’LLGOGETYOURBEER!!!"

    scene firstbarnone
    with dissolve

    "Sana sprints over to the opposite side of the bar and trips over one of the mats on the
    ground, knocking a few things off the counter."
    "She scrambles to pick them all up and quickly pulls the first bottle she sees out of the cooler."

    scene barfive9
    with dissolve

    sa "H...Here it is...your..."

    scene barfive9r
    with dissolve

    sa "Your..."
    s "..."
    sa "..."

    scene barfive10
    with hpunch

    sa "Ah!"
    s "..."

    scene barfive11
    with dissolve

    sa "I’LLBERIGHTBACK!!!"

    scene firstbarnone
    with dissolve

    "This is hard to watch."

    scene barfive12
    with dissolve

    sa "..."
    s "..."
    sa "Don’t laugh at me..."
    s "I’m not laughing. In fact, I feel like I owe you an apology."

    scene barfive13
    with dissolve

    sa "No...You don’t...I’m just not really used to...dealing with pressure..."
    sa "No one has ever asked for spaghetti before...I didn’t know how to handle it..."
    s "Well, if it makes you feel any better, I don't think a real customer will ever ask for spaghetti. Especially considering you don't have a menu."
    s "But, in the event that someone does, it’s always okay to just tell them that you don’t have any."

    scene barfive12
    with dissolve

    sa "B...But when I tried that and you...said..."
    s "What I said doesn't matter."
    s "I’m sure you’ve heard that whole thing about how the customer is always correct, right?"
    sa "Y...Yes..."
    s "Well, that’s not true. In fact, the customer is pretty much always wrong."
    s "You know this place better than they do, so be assertive and tell me that you don’t have any spaghetti."
    sa "..."
    sa "Like...Like right now?..."
    s "Right now."
    sa "..."
    s "Deny me the spaghetti, Sana."
    sa "We..."
    sa "We don’t have any spaghetti..."
    s "Perfect. That concludes our lesson for the day."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene barfive14
    with dissolve

    sa "I’m...so confused..."
    sa "Was that...really supposed to help?..."
    s "It probably could have gone a little better on both of our ends. But don't be surprised if you wake up tomorrow and you're suddenly an expert at talking to people."

    scene barfive15
    with dissolve

    sa "Well...at least it was...a little fun?..."
    s "Are you still crying?"
    sa "..."
    s "Sana."
    sa "I’ll...try not to freak out next time! I promise!"
    s "And I will try not to make you cry. But, honestly, I'm not sure how much good that's going to do when all it took was spaghetti."
    sa "It was...more the...context of the spaghetti that...made me cry..."
    s "I'm sure it was, Sana."

    scene black
    with dissolve2

    s "I'm sure it was."

    "Sana and I say our goodbyes and she walks me to the door so she can lock it behind me."
    "Was today actually successful in teaching her anything?"
    "No."
    "But, like she said-"
    "At least it was a little fun."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar5 = True

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    stop music fadeout 3.0
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar10:
    scene sarabar1
    with dissolve2
    play music "calmbar.mp3" fadein 2.0

    "I enter the bar to be greeted by a tragic sight."
    "It seems that Sana has aged fifteen years or so since the last time I've seen her."
    "I contemplate to myself the possibility of her concealing a tragic hormonal disease from me, but then remember the key detail of her being a human being."
    "Which means that, more than likely, this is the original owner of her DNA."
    "In other words, it looks like Sana's mom is working tonight."

    q "Well...hi!"
    q "Can't say I've seen you around before."
    q "Come on over. I don't bite."

    scene sarabar2
    with fade

    q "What can I get you? As a heads up, we're pretty low on...a lot of things right now."
    s "Just a beer is fine, thanks."
    q "Coming right up."

    scene sarabar0
    with dissolve

    "The woman heads over to the cooler and grabs the same beer I always have when I'm here."
    "Not like there are any options to begin with, but at least it's one that I've come around to enjoying."

    scene sarabar3
    with dissolve

    q "Aaaand one beer. Want me to leave your tab open or are you gonna be a loser and abandon me after one drink?"
    s "Well, I {i}was{/i} thinking about being a loser tonight, but with words like {i}abandon{/i} sneaking into the conversation, I don't know if I should anymore."

    scene sarabar4
    with dissolve

    q "That’s the spirit! Plus, now you get to hang out with me free of charge. And that's something I make everyone else pay extra for, you know."

    "Add that to the list of reasons this bar is failing, I guess."

    s "Thanks a lot for the discount. I feel even less inclined to abandon you now."

    scene sarabar3
    with dissolve

    q "Don’t mention it. It's not every day somebody like you walks in."
    s "You mean a customer?"

    scene sarabar4r
    with dissolve

    q "Well, uhh...I was {i}going{/i} to say somebody handsome. But...yeah. I guess what you said is...just as accurate."
    q "At least we're known for {i}something,{/i} I guess. I would have preferred it didn't involve how dead the place is, but I guess beggars can't be choosers."
    s "I only know because I've become sort of a regular here. There's no word on the street about the place or anything like that."

    "Though, I can't imagine it wouldn't help if there was."

    scene sarabar5
    with dissolve

    q "Wait, you're a regular {i}here{/i}? At this bar? The one we're currently inside of?"
    q "Are you sure you don’t have us confused with some other place?"
    s "It's definitely this place. I'm sure."
    q "It’s just weird that I’ve never seen you before if you’re a regular..."
    s "That's probably because the younger version of you is typically the one who helps me."

    scene sarabar4
    with dissolve

    q "Aww! My sweet little girl Sana is- wait. You're not saying I look old, are you?"
    s "You look very young. Just...also understandably older than the smallest girl I know."
    q "She's doing okay, then? I had no idea she'd been actually helping anybody lately."
    s "She’s...doing her best. She needs a little work still, but I’m helping her get there."

    scene sarabar5
    with dissolve

    q "Helping her get there? What do you mean?"
    s "I mean that, as her teacher, I can't let her permanently struggle when it comes to common social skills."

    scene sarabar6
    with dissolve

    q "Oh my god, {i}you're{/i} Sana's teacher?! It’s so nice to finally meet you!"
    sar "I’m Sara! I always figured our first meeting would be, like...not inside of my bar."
    s "Life can be unpredictable at times, I guess. Meeting here is much more interesting than in my office, at the very least."

    scene sarabar5
    with dissolve

    sar "I’m really surprised, though. All this time, I was under the impression you were a woman. You're so young, too."
    sar "How old are you? If you don’t mind me asking, I mean."
    s "Uhh..."

    "...How old {i}am{/i} I?"

    if bonus == True:
        s "I’m...34."
    else:
        s "I have lived for countless millennia. I am eternal."

    "I spit out the first number that comes to mind."
    "I should probably ask Ami if I have an ID tucked away anywhere, since I don't think I've seen it since starting my new life."

    scene sarabar6
    with dissolve

    sar "Wow! That means you and me are almost the same age! I can’t believe Sana never told me!"
    s "What {i}I{/i} can’t believe is that you're a mother. You could probably pass as one of my students if you wanted to."

    scene sarabar3
    with dissolve

    sar "Well, I {i}do{/i} still fit in my old uniform if you ever wanna test that theory out a little more..."
    s "..."
    sar "...is what I {i}would{/i} be saying if I was not such a dedicated mother who always puts her daughter first!"
    s "Oh, sorry. The only reason I went silent is because I was fantasizing."

    scene sarabar6r
    with dissolve

    sar "Oh, thank god. I thought I set a new record for the time between an introduction and a fallout for a second."

    "Did Sana really come out of this woman? The two of them couldn't be any further apart."

    scene sarabar7
    with dissolve

    sa "Mom, I finished cleaning the glasses. Did you want me to-"
    s "Hi, Sana."

    scene sarabar8
    with dissolve

    sa "Ah-"
    sa "Oh...I...I see that..."
    s "I finally met your mom, yes."

    scene sarabar9
    with dissolve

    sar "Hey! You let me think your teacher was a woman this whole time and never even bothered correcting me! How come?!"
    sa "I...just...I don't know..."
    sar "Any other mom would totally ground you right now, you know. You’re lucky I'm the best."
    sa "R-Right..."

    scene sarabar10
    with dissolve

    sar "So, are there any good stories about Sana from[school]? Please tell me if there are."

    scene sarabar11
    with dissolve

    sa "Mom! Stop! I already told you...I don’t really talk to anyone..."

    scene sarabar12
    with dissolve

    sar "Well, that's not true! What about that cute blonde girl that comes over sometimes?"
    sar "Oh! Ayane! That was her name. I think."
    sar "Or...Ayaka?"
    sar "Anya?..."

    scene sarabar13
    with dissolve

    sa "It's...Ayane..."

    "Poor Sana. It seems like even she has trouble dealing with how outgoing her mother is."
    "Luckily for her, I'm going to decide {i}against{/i} embarrassing her in front of her mother as I believe it will increase the chances of her eventually sleeping with me."
    "Ulterior motives reign supreme once again."

    s "I’m afraid I don’t have any interesting stories to share, unfortunately."

    scene sarabar14
    with dissolve

    sar "Awe! Darn it! If anything happens, though, you have to let me know. That's a new rule starting right now."

    scene sarabar15
    with dissolve

    sar "Oh! I know! I’ll give you my number so you don't have any excuse not to!"
    sa "Mom! Stop! Sensei doesn’t want your number!"
    sar "Doesn't he need it, though? I'm your emergency contact and I need to know if something bad ever happens."
    sar "Being able to hear embarrassing stories with the push of a button is just an unfortunate side effect, I'm afraid."

    "Sara swiftly scribbles her number on a sheet of receipt paper and somehow slides it over to me without Sana noticing."
    "Despite what her daughter says, I gladly accept it."

    sa "Mom!"
    sar "What’s the problem, dear? I’m just trying to keep tabs on my precious little girl."
    sa "I can...take care of myself!"

    scene sarabar16
    with dissolve

    sa "Besides...Sensei...would...never let anything bad happen to me...so..."
    sar "..."
    sa "..."

    scene sarabar17
    with dissolve

    sar "Well, well, well..."
    sar "What do we have here?"

    "Sara shoots me a slightly suggestive glance as Sana looks away from us."
    "And, without beating around the bush, I'm pretty sure it's her insinuating that her daughter might have a little crush on me."
    "I doubt it's true, but I'm not going to argue it because I want it to be."

    sar "So...{i}Sensei...{/i}my little girl seems to believe that you’ll protect her from the evils of life. Is this true?"
    s "More or less."
    sa "Sensei...I’m sorry my mom talks so much..."
    sa "Her...brain is...um..."
    sa "She has an...illness that makes her...say things and..."
    sar "Oh, stop. I do not."

    scene sarabar18
    with dissolve

    sar "Sensei, you know I'm not sick, right?"
    s "I mean...I don't {i}know{/i} that...but based on my experiences tonight, I have no reason to assume you are?..."
    sar "Exactly!"
    sar "I'm just a totally normal super cool, super young, supermom."
    sar "And if my daughter trusts you with her well-being, I guess I do too."
    sar "Welcome to the bar, Sensei."
    sar "I imagine we'll be seeing each other quite often from now on."
    sa "I...really hope not..."

    scene black
    with dissolve2

    "I wind up staying for a few more drinks and chatting with Sara about all sorts of things."
    "She’s the first person my age that I’ve felt some sort of connection with. And she {i}does{/i} genuinely seem to care about Sana in that ‘overbearing mom’ sort of way."
    "The two of them are like oil and water. You know they won't work well together, but the immense curiosity of combining two incompatible components is enough to pique your curiosity."
    "The night moves on and I observe as their respective spills combine."
    "I feel no need to clean anything up."
    "I simply enjoy a few more drinks and then head home."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar10 = True

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    stop music fadeout 5.0
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar15:
    play music "calmbar.mp3"
    scene carryredux1
    with fade

    "I show up to the bar around the usual time and, just as always, there are no customers anywhere in sight."
    "I wonder how much longer the Sakakibaras will be able to keep this up before just calling it quits and trying something else?"
    "I can't imagine it would be easy since Sara lives upstairs, but I just...can't imagine this being sustainable at all."

    scene carryredux2
    with dissolve

    sa "Oh, Sensei...good...good evening..."
    s "Hey, Sana. How is work going?"
    sa "Oh, you know...more of the same...there’s...{i}hic{/i}...not really anything happening, so..."
    sa "We're just........{i}hic{/i}...hangin' out..."
    s "..."
    sa "What? Why're...ya...lookin' at me like that..."
    s "Sana, are you drunk right now?"
    sa "{i}Hic...{/i}"
    sa "Nahh."
    sar "She's fiiiiiine~"
    sar "Sana, get Sensei a beer and lock the door."
    s "You should probably-"
    sa "One...{i}hic{/i}...spaghetti...coming up..."
    s "..."

    scene black
    with dissolve2

    "Yeah, this definitely isn't sustainable."
    "Sana gets me a beer from behind the counter and I guess...completely forgets it's meant for me as she walks it over to the couch and cracks it open herself."
    "It's clear that the two of them have been going at it for at least {i}some{/i} amount of time given how far gone Sana already is, but..."
    "Well, Sana also weighs the same amount as a large brick, so I can't imagine she holds alcohol very well."
    "Her mother, on the other hand..."

    scene drunk1
    with dissolve2

    "Is not much different."

    sar "{i}You're hot.{/i}"
    sa "{i}Hic...{/i}"
    sa "{i}I can't even...taste anything anymore...{/i}"

    "I begin to go over the possible scenarios that may have led to this in my head and all of them fall back on Sara being the one to blame."
    "Now, is it wrong for me to be assuming this despite our relationship still being in its earliest stages? Maybe."
    "But I can't really think of many scenarios in which it would be okay for a guardian to encourage this sort of behavior."
    "That being said, I don't really intend to stop it because I think it's funny and has created an opportunity for me to flirt with a hot mom."
    "Sorry, Sana. Please don't become an alcoholic."

    s "Thanks, Sara. Are you sure it’s okay to let Sana drink, though? She seems pretty out of it."
    sar "Whaaaat? Of course it’s okay. We live above a bar. She's in good hands."
    s "Is she? Because I'm not convinced you'd really be able to carry her in your condition."

    scene drunk2
    with dissolve

    sar "Sensei, she's {i}fine.{/i} There's no problem doing something like this every once in a while, is there?"
    s "How often is {i}once in a while{/i} exactly?"
    sar "What? You think I keep track? Come on, Sensei. Be like Sana and live a little."

    scene drunk3
    with dissolve

    s "I didn't realize your idea of {i}living{/i} was so...depressingly mature."
    sa "I am a...{i}hic{/i}...victim of...peer pressure..."
    sa "This...{i}hic{/i}...was all...my mom's...idea..."
    sa "{i}Hic{/i}........Who are you again?..."

    scene drunk3r
    with dissolve

    s "She's so drunk that she's forgotten who I am."
    sar "Oh, stop. She's just playing around. There's no way Sana would forget about {i}you{/i} with how much she's been looking forward to your visits lately."
    sar "Sana, be a dear and tell your teacher how you really feel. You hurt his feelings by pretending to forget about him."
    sa "How I...really feel?..."
    sa "Was there...something I wanted to tell him?"
    sar "I don't know, dear. Was there?"
    sar "We won't know if you don't share it with us."

    "Correct me if I’m wrong here, but isn’t it normally the mother who talks their kid {i}out{/i} of doing things like this?"
    "I mean, Sana isn’t in any danger since she can sleep upstairs if she winds up passing out, but this is still kind of weird."

    scene drunk4
    with dissolve

    sa "{i}Hic...{/i}S-Sensei..."
    sa "You’re...a really...cool guy...you know that?..."
    s "Thanks, Sana."
    sa "No, like...{i}really{/i} cool...youknowwhatI’msayin’?"
    s "..."

    scene drunk5
    with dissolve

    sar "I think that’s her code for saying she likes you."

    scene drunk6
    with hpunch

    sa "Ayy! You stay outta this, {i}Mom!{/i} Stop...{i}hic...{/i}stop puttin’ words in my mouth!"

    scene drunk7
    with dissolve

    sa "Sensei...you don’t...gotta listen to her...she's {i}clearly{/i} drunk..."
    s "You are {i}both{/i} clearly drunk and I haven't really figured out how to handle it yet."
    sa "{i}Whatareyatalkinabout?{/i} I’ve only had like, one beer..."
    s "There is no way that's true. And I'd be honestly surprised if that wasn't all it took to knock out a girl your size in the first place."
    s "Are you even going to be able to make it back to the dorm?"

    scene drunk8
    with dissolve

    sa "The wha?"
    s "The dorm. Where you live."
    sa "Ooooohhhh...the {i}dorm...{/i}"
    sa "You're right...I gotta...{i}hic{/i}...tell Ayane I'm...not gonna make it back..."
    sa "I think...I’m just...gonna sleep here tonight..."
    sar "Maybe if you ask nicely, your teacher will volunteer to carry you upstairs and put you to bed?"

    scene drunk6
    with dissolve

    sa "Ayy! Whatareyou still doin’ here?! Take a...{i}hic...{/i}hint forcryinoutloud!"
    sar "I live here, dear. Remember?"
    sa "I don’t care {i}where{/i} you live...{i}hic{/i}...I’m tryina’ have a...conversation with my...teacher and...you're just...{i}hic{/i}...gettinintheway..."

    scene drunk7
    with dissolve

    sa "Sensei, you don’t...have to carry me upstairs...I can do it myself..."
    s "I mean, I really don’t mind. I've carried bags of rice that weigh more than you."

    scene drunk7r
    with dissolve

    sar "You can always carry {i}me{/i} upstairs instead...."

    scene drunk6
    with dissolve

    sa "Mom! Stop tryina’ seduce my teacher! Sensei is...{i}hic...{/i}a good guy who doesn’tevenlike girls!"
    s "What? No, I definitely like girls."
    sa "Shuddup! Don’tgiveheranyideas! She’ll {i}hic...{/i}drink your blood and {i}hic{/i} throw ya to the curb!"
    sar "Sana, dear, I only bite when I'm {i}asked{/i} to. I'd never just-"

    scene drunk9
    with hpunch

    sa "AHHHHHHH!!!!!!!"
    sa "WHOWANTSANOTHERBEER?!"

    scene black
    with dissolve2

    "Sana winds up passing out and falling into my lap roughly five minutes later."
    "She had a good run, though. I just hope that this isn't something that happens as regularly as Sara made it sound."
    "Drinking away your worries is one thing when it's adults doing it, but for someone like Sana-"
    "Well, what would she even have to worry about at her age to begin with?"
    "Anyway, sensing that the collapse of the world's shortest bartender is a good stopping point for the night, I take Sana into my arms and princess carry her to her old room upstairs."

    play sound "dooropen.mp3"

    "I lay her down on the bed, feeling too awkward to bother covering her with a blanket, before turning around and walking into Sara's living room."
    "It's a relatively sparse apartment. Nothing lavish by any means. And Sara is busy-"
    "Wait. Where {i}is{/i} Sara?"
    "Wasn't she just here a second ago?"
    "I pace around the apartment, checking behind corners and curtains, thinking maybe she's playing some drunken prank on me, before realizing that she's probably passed out in her own-"

    sar "Sensei! Help! There's a spider in here!"

    "Or, she is fighting for her life."

    s "I'm coming..."

    "You know, I really dislike dealing with drunk people."

    play sound "dooropen.mp3"
    scene drunk10
    with dissolve
    stop music fadeout 3.0

    "It's like every time you say something to them, they just-"

    sar "Lock the door."
    s "..."

    "What was I saying just now?"

    if bonus == True:
        jump sarabarfirstx
    else:
        s "Why would I do that? It insinuates that there would be adult content and things like that are strictly forbidden."
        sar "I just wanted to know if it would be okay for the two of us to hug."
        s "But Sana is asleep in this very building."
        sar "Hug me anyway, Sensei."

        "What should I do?"

        menu:
            "Hug Sana's mom":
                s "I will now hug you."
                sar "Rejoice. The hug approaches."

                scene black
                with dissolve

                $ renpy.end_replay()
                $ sana_love += 1
                $ bar15 = True
                $ sarasex = True

                "{i}Despite having hugging her mom, Sana’s affection has increased to [sana_love]!{/i}"

                stop music fadeout 3.0

                "........."
                "......"
                "..."

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat

            "Hugs are icky":
                s "I can not, for I am an educational professional in charge of your daughter's well-being."
                s "Hugging you here would put that at risk."
                sar "I understand and thank you for considering my daughter's education. Thank you, Sensei."

                scene black
                with dissolve

                $ renpy.end_replay()
                $ sana_love += 1
                $ bar15 = True

                "{i}Sana’s affection has increased to [sana_love]!{/i}"

                stop music fadeout 3.0
                "........."
                "......"
                "..."

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat

label saramissionaryanim:
    scene barnight
    with dissolve
    play music "calmbar.mp3"

    "I show up at the bar to find that Sana isn't working tonight."
    "Instead, Sara and I hang out and talk about different ways for her to start attracting business."
    "Well, to be concise, we talk about that for roughly five minutes before we turn to just flirting with each other."

    if bonus == True:
        "It quickly becomes apparent how horny both of us are and-"
    else:
        "It quickly becomes apparent how much we want to hug, and-"

    "Well..."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump saramissionaryanimx
    else:
        $ sara_lust += 1
        stop music fadeout 4.0

        "We do that."
        "{i}Sara's lust has increased to [sara_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label bar20:
    scene scoutredux1
    with dissolve
    play music "calmbar.mp3"

    "I walk into the bar and immediately put my head down as Sara and Sana are locked in a mildly heated argument behind the counter."
    "I worry for a moment that something like this could potentially drive customers away, but then I remember where I am and decide it's best to not worry at all."
    "I am a little offended, however, seeing as my presence has not put a stop to whatever debate those two are having."
    "Granted, I'm probably not even viewed as a customer anymore to them."

    if sarasex == True and bonus == True:
        "Now, I’m just a dude who shows up, has a beer or two, and then proceeds to either lecture or have sex with one of them."
    else:
        "Now I’m just a dude who shows up every once in a while to give public speaking
        lessons to one of them."
        "If you can even call our talks ‘lessons’ I mean..."

    scene scoutredux2
    with dissolve

    sa "Um...h-hi..."
    sa "You didn’t...hear anything just now did you?"
    s "Hey, Sana. "
    s "I didn't hear what it was about, but I could definitely tell it was some sort of argument."
    s "Is everything okay?"
    sa "Mhm...Everything is fine...I...umm..."
    sa "I don’t have to work tonight..."
    s "Sara’s going to take care of the bar on her own?"
    sa "I...guess so..."
    sa "I have...an...umm...important mission to take care of..."
    s "A mission this late?"

    scene scoutredux3
    with dissolve

    sa "And, um...it's...a mission for you too, actually..."
    s "Wait, what? Why? I just wanted to relax. Why do I have a mission now?"
    sa "Because that's just...how things worked out..."
    s "Well, can you tell me what it is? Or are you just going to stay cryptic about it?"

    scene scoutredux4
    with dissolve

    sa "I-I’ll tell you! I just need to go get dressed first!"
    sa "Please...wait a moment! My clothes are...upstairs..."

    scene scoutredux1
    with dissolve

    s "..."

    "Sana quickly dashes past me and up the stairs to her mother’s apartment."
    "It’s quiet enough in here that even the faint tapping of her footsteps manages to bring life to this dying bar."

    scene scoutredux5
    with fade

    sar "Hiya, stranger~"
    s "What the hell was that all about?"
    sar "Are you talking about our argument? Or about the mission?"
    s "Both, I guess?"
    sar "Well, the two of them are connected, so I'll just go ahead explain the whole thing to you."
    sar "This ‘mission’ involves checking out another bar in the area that’s been doing...admittedly better than this one."
    sar "Like, much better."
    sar "Like it's not even close."
    s "So it’s a...scouting mission?"

    scene scoutredux6
    with dissolve

    sar "Yeah, exactly! You two are going to go check out that bar and see what {i}they’re{/i} doing that we’re not."
    sar "Not sure if you’ve realized this, but my livelihood kinda depends on this place."
    sar "Unless a certain someone wants to start taking care of me, of course."
    s "I'm good, thanks."

    scene scoutredux7
    with dissolve

    sar "At least pretend to think about it, jerk!"
    s "That aside, are you sure it’s okay to send Sana to a rival bar?"

    if bonus == False:
        s "Doesn’t she look a little...young, but not so young that you would mistake her for someone who is not old enough to consent and can live entirely independently?"
    else:
        s "Doesn’t she look a little young? I can’t imagine there’s any place that would actually serve her."

    scene scoutredux8
    with dissolve

    sar "That’s exactly what we were arguing about! I was supposed to go with you instead!"
    sar "The two of {i}us{/i} going to a bar together would make a lot more sense than you going with my daughter! {i}And{/i} it would give us the chance to get to know one another better!"
    s "This wasn’t a scouting mission at all, was it? You just wanted to get drunk with me."

    scene scoutredux6
    with dissolve

    sar "I mean...that's not {i}all{/i} I wanted to do."
    s "That sentence makes the idea of you allowing your daughter to go in your place significantly more disturbing."

    scene scoutredux8
    with dissolve

    sar "It’s not like I {i}wanted{/i} to! She just seemed weirdly devoted to not letting me follow you out tonight for some reason!"
    s "That’s...interesting."

    scene scoutredux9
    with dissolve

    sar "{i}I{/i} think she's just jealous."
    s "I think it’s less jealousy and more feeling weird about the situation."
    s "Wouldn’t you feel odd if your teacher in [high_school] started dating your mom?"
    sar "Well, yeah. It would have been weird if we were {i}both{/i} dating him."
    s "I'm sorry, what?"

    scene scoutredux10
    with dissolve

    sar "Oh, it's not really a big deal."
    sar "It was one of those secret relationship things. No one ever found out about it."
    sar "Well, at least...not right away..."
    sar "But it was inevitable that someone eventually would and-"

    scene scoutredux5
    with dissolve

    sar "Wait, why are we even talking about this? That's definitely not something I want to discuss with you yet."
    sar "If only we were able to go out for drinks..."
    s "..."

    "Sara pauses for a moment and reflects on her past, but the reflection doesn't last long as the same faint tapping of footsteps from earlier makes its way back down the stairs."

    s "I’ll see you later, Sara. I’ll be sure to let you know how your rival bar is."
    sar "Be good to my daughter. Don't let her drink {i}too{/i} much."
    s "..."
    sar "It was a joke. You can laugh."

    scene scoutredux2r
    with fade

    sa "Um...I’m sorry it took me so long...I couldn’t find my socks..."
    s "It’s fine. I got the details from your mom. Do you know where this place is?"
    sa "Mhm...It’s not that far from here..."
    sa "You can just...follow me..."

    scene black
    with dissolve2

    "Sana and I exit the bar."
    "I turn around to look at Sara as we make our way through the door-"
    "But the smile she wore just moments ago has vanished."
    "And all I can do is imagine why."
    "........."
    "......"
    "..."

    scene sanabartwenty1
    with dissolve

    sa "..."
    s "..."

    "Sana and I take a seat at a table after being led over by a hostess around her mother’s age."
    "Right off the bat, you can tell this place has a much...{i}warmer{/i} atmosphere."
    "In fact, I don't even know if I'd call this place a {i}bar{/i} considering everyone seems to be eating as well."
    "I pick up a menu to confirm my suspicions and don't see the word {i}bar{/i} anywhere, so I ascertain that Sara's source of intel is just as bad as her management skills and toss away my gameplan for the night."
    "Sorry, Sara. Your mission was inherently flawed."

    sa "Um..."
    s "What’s up?"
    sa "Nothing’s up...I just...wanted to say...thanks for coming with me..."
    sa "I’ve never gone to another bar before..."
    s "You know this isn't a bar, right?"
    sa "..."
    s "Sana, it's clearly a full service restaurant. There are waiters and everything."
    sa "But...my mom said-"
    s "Your mom says a lot of things and it would probably be best to disregard most of them."
    sa "Well...either way...thank you..."

    scene sanabartwenty2
    with dissolve

    sa "I guess it’s...pretty easy to see why this place is better...right?"
    sa "It’s...really nice in here..."
    sa "I bet our...waitress will be really nice too..."

    "A moment of silence passes by as Sana begins to observe the layout of the place."

    scene sanabartwenty2r
    with dissolve

    "But unfortunately, before she's able to take in all of it, someone unexpected shows up."

    scene sanabartwenty3
    with dissolve

    k "..."
    s "..."

    if bonus == True:
        k "You brought a {i}child{/i}?"
    else:
        k "You brought a {i}health inspector{/i}?"

    scene sanabartwenty4
    with dissolve

    if bonus == True:
        sa "Ch...Child? No...I’m-"
    else:
        sa "My secret identity has been discovered."

    s "Sana, I’ll handle this."
    s "Talking to her is beyond your current skill level, I’m afraid."

    scene sanabartwenty5
    with dissolve

    sa "Wh-What?..."
    k "Explain yourself, Hamburger Man."
    sa "Um...do you...know this girl, Sensei?"
    s "I do. Her name is Kaori, but she also goes by the Mistress of the Queen of the Spider Dark or something."
    sa "The...what?..."
    k "Hamburger Man, I can not provide dizzy drinks to this undersized human."

    if bonus == True:
        s "That’s fine because this is a restaurant and not a bar. Not everyone has to drink."
        k "All of the other human customers order the dizzy drinks. I can not make special exceptions just because this human is not fully grown."

    scene sanabartwenty4
    with dissolve

    sa "Um...would I be able to...maybe have a glass of water?"
    sa "Does...that count as a..."

    scene sanabartwenty6
    with hpunch

    sa "OKAY NEVER MIND! SORRY I ASKED!"
    k "You are a strange creature. Perhaps...{i}a cyclops?{/i}...How do you know the Hamburger Man?"
    k "Tell me immediately, miniature human cyclops girl!"
    sa "I D-D-D-DON’T KNOW ANY HAMBURGER MAN! I SAID I’M SORRY! PLEASE DON'T HURT ME!"
    s "Kaori, it’s probably best to leave her alone until I progress further into her story."

    scene sanabartwenty7
    with dissolve

    k "What is this ‘story’ you speak of? Can it fit in a box?"
    k "Do {i}I{/i} have a story? What color is it?"
    s "Everyone has a story. Yours just hasn’t started yet."
    k "..."
    s "..."
    k "..."
    s "..."
    k "Order something now, please."
    s "I’ll have a-"
    k "No hamburgers."
    s "But I-"
    k "Absolutely no hamburgers, Hamburger Man. You will become one if you continue to live purely off of them."
    s "..."
    k "..."
    s "Just get me whatever dish you recommend. And a beer."
    k "Understood."
    k "Or, as I have learned to say from the cooking-man in the shiny back room, “heard.”"

    if bonus == True:
        k "I will retrieve your items now. Please do not allow your human daughter to consume any dizzy drinks in the meantime."
    else:
        k "I will retrieve your items now. Please do not allow the health inspector to look under the table."
        s "What? Why not?"

    scene sanabartwenty8
    with dissolve

    "Kaori leaves as quickly as she appeared and I’m alone with my human daughter again."

    sa "..."
    s "It’s okay, Sana. She’s gone now."

    scene sanabartwenty9
    with dissolve

    sa "Who was she?! {i}What{/i} was she?! Why did she talk like that?!"
    s "There are many questions in life that I am unable to answer. This is one of those questions."
    sa "Why do you know her? Are you...secretly a...weird person?"

    "Yes."
    "Probably not in...whatever way Sana is insinuating, but saying my habits are {i}not{/i} weird would be flat out lying."

    s "She’s just a waitress at some diner I’ve been to. And also at some bistro near the[school]."
    s "And...also here now I guess?..."

    "Just how many jobs does this girl have?"

    sa "People...{i}hired{/i} her? But...she’s so scary..."
    s "You’re not talking about the tattoo, are you? I don’t think it’s that bad."
    sa "She has a...tattoo?...I didn’t even see it...I had my eyes closed the whole time..."
    s "Yeah, she’s got a huge spider on her chest. Which makes it even stranger to me why so many places are hiring her."
    sa "Maybe she’s...in the Yakuza?..."
    s "Yeah...I don’t really think Kaori is the Yakuza type."

    scene sanabartwenty10
    with dissolve

    if bonus == True:
        sa "Um...you don’t...also think I’m...a {i}child{/i}...do you?"
        s "Of course not. I mean, obviously you’re younger than me. But you’re
        old enough to make your own decisions."
        s "Kind of like you did tonight."
    else:
        sa "Um...about me being a...health inspector..."
        s "Don't worry, Sana. I have strong feelings when it comes to health inspectors."

    scene sanabartwenty11
    with dissolve

    sa "Huh?...What do you mean by that?"

    if bonus == True:
        s "Like how you didn’t want me spending time alone with your mom and decided to volunteer yourself instead."
    else:
        s "I will tell you if you tell me why you didn’t want me spending time alone with your mom tonight."

    scene sanabartwenty12
    with dissolve

    sa "She...She told you that?!"
    s "Was she not supposed to?"
    sa "I...didn’t mean anything weird by it! I swear! I’ve just been meaning to visit this place for a while now!"
    sa "I hear the...water is really good!"
    sa "I’m totally not afraid of you being alone with my mom! Why would I be?!"
    s "Sana, I'm going to need you to calm down. People are starting to look over-"

    scene sanabartwenty13
    with dissolve

    sa "YOU TWO CAN BE ALONE WHENEVER YOU WANT AND I CAN’T STOP YOU!"
    s "Sana...please just-"
    sa "YOU ARE...BOTH ADULTS!"
    sa "YOUCANMAKEYOUROWNDECISIONS!"
    s "Sana, you really need to-"

    scene sanabartwenty14
    with dissolve

    k "..."
    s "..."
    k "...!"
    s "..."
    s "Okay, fine. We’re leaving."
    s "Sorry for causing a disturbance."
    k "I will remember this moment for all eternity."
    s "I’m sure you will. Come on, Sana."
    sa "I’MSOSORRY!"

    scene black
    with dissolve2

    "Sana and I exit the rival {i}bar{/i} and begin to make our way back to Sara’s."
    "Not wanting to explain the situation, I drop Sana off at the entrance and immediately begin to make my way home."
    "Here's hoping nothing like this ever happens again."
    "And here's to that hope being nothing short of a pipe dream."

    $ renpy.end_replay()
    $ bar20 = True
    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar25:
    scene bartwofive1
    with fade
    play music "calmbar.mp3"

    "I decide to spend yet another night at the bar killing time with Sana."
    "Without me even having to ask, she grabs a beer from the cooler and slides it over to me with an uncharacteristic smile on her face."

    s "In a good mood tonight?"
    sa "Hm?"
    sa "Why do you ask?..."
    s "You seem a lot less nervous than usual."
    sa "Do I?"
    sa "I’m just...a little relieved that my mom isn’t around...That’s all."
    s "Ahh. Yeah, I can imagine it probably takes a load off of your mind knowing that she can’t show up and randomly embarrass you."

    scene bartwofive2
    with dissolve

    sa "You don’t get the half of it..."
    sa "It’s only been getting worse lately too..."
    s "Really? Did something happen?"

    scene bartwofive3
    with dissolve

    sa "Yes."
    s "...Explain?"
    sa "{i}You{/i} happened."
    s "Saying it with that sort of expression makes you seem more like Yumi and less like Sana."
    s "Give me back my favorite bartender."

    scene bartwofive2
    with dissolve

    sa "I’m only kidding..."
    sa "Though...it is true that my mom has been {i}really{/i} annoying ever since you started coming around..."
    sa "She keeps asking me questions about you and...I have no idea how to answer even half of them..."
    s "Well, what kind of questions? Maybe I can help?"

    scene bartwofive4
    with dissolve

    sa "Huh?...Well...it’s not like I’ve...kept track of them or anything..."
    sa "They’re mostly just random things like what kind of food you like or...what you do for fun."

    scene bartwofive2
    with dissolve

    sa "I think...she thinks we might be closer than we actually are..."
    s "Well, aren’t we?"
    s "I like to think that we’ve at least sort of transcended the teacher/student thing by now, right?"
    sa "Well...I don’t think I’ve ever had another teacher who routinely shows up in my room...so I guess so."
    sa "But I still don’t know much about you either..."

    "To be fair, even {i}I{/i} don’t know much about myself."
    "This version of me, at least."
    "It’s not like I can just sit down with Ami and ask something like, “Hey, what was I into a couple years ago? How different did I act?”"
    "It’s a confusing situation. "
    "And it definitely doesn’t help that there isn’t really anything I find appealing other than..."
    "Well, having conversations with [younger_girls] in the middle of the night."
    "But hey, at least it feels a little more normal talking to one in a bar rather than a porn shop..."

    s "Well how about this-"
    s "Do {i}you{/i} have any questions for me, Sana?"

    scene bartwofive4
    with dissolve

    sa "Are you...going to answer them?"
    s "I believe that was implied, yes."
    sa "And...are you going to ask me any?"
    s "...Do you want me to?"

    scene bartwofive1
    with dissolve

    sa "Sure...We can make it a sort of...game. Or something..."

    scene bartwofive5
    with dissolve

    sa "Like...we could take turns getting to know more about each other..."
    sa "Something like that might be easier for me since I can’t really...steer conversations myself."
    maki "What’s all this about steering conversations?"

    scene bartwofive6
    with dissolve

    s "..."
    maki "...?"
    s "Maki?"
    maki "Yes! That is me. Maki."
    s "What are you doing here?"
    maki "Drinking, I hope."

    scene bartwofive7
    with dissolve

    maki "Is your mom around tonight, Sana?"
    sa "Huh?...Oh, umm...No. She had plans with a friend tonight."
    maki "And I wasn’t invited? Damn that tramp."

    scene bartwofive2
    with dissolve

    s "Do you know who that woman is?"
    maki "Maki! Do I need to say it even louder?"
    sa "That’s umm...the..."

    scene bartwofive5
    with dissolve

    sa "That’s the...porn-lady..."

    scene bartwofive8
    with fade

    "Maki walks up to the bar and takes her place on the stool directly beside me."
    "What sort of woman gets dressed up like that to come to the bar all by herself?"
    "She realizes this place doesn't ever have any customers, right?"

    maki "Porn-lady isn't really the best nickname I could have asked for. But I guess I can take it."

    if bonus == True:
        scene bartwofive9
        with dissolve

        maki "Heh...Take it."
        maki "Like a dick."
        maki "Get it?"
        s "Yes, Maki. I get it."

    scene bartwofive10
    with dissolve

    maki "Were you two in the middle of something? I could have sworn I overheard a chat about the question-game."
    sa "Y-Yes...We were going to do...something like that..."
    sa "But I don’t think we were going to ask the sort of questions you’d be interested in..."
    sa "At least I hope not..."
    maki "Hmm okay, okay. Well don’t let me interrupt you. "
    maki "Could I bother you for a glass of wine, though?"
    sa "Oh...umm...Sure. "
    sa "I’ll be right back..."

    scene bartwofive11
    with dissolve

    "Sana walks to the other end of the counter and opens a brand new bottle of red wine, pouring it carefully into a glass."

    maki "Another student of yours?"
    s "Another student of mine."

    if bonus == True:
        maki "Do you have any girls who {i}don’t{/i} work in businesses not suited for their age group?"
        s "A few. None as impressive as a porn shop, though."
        maki "I think that’s the first time anyone’s referred to my shop as impressive."
        maki "Thank you for your kind words. I’ll knock 500 yen off of your next fleshlight in order to thank you for them."
    else:
        maki "Radical."
        maki "Hey, want to go jet-skiing sometime?"

    s "You truly know the way to a man’s heart, don’t you?"

    scene bartwofive12
    with dissolve

    "Sana comes back a minute or two later and places a glass in front of Maki, who immediately picks it up and begins sipping away."

    sa "I...take it you two know each other?..."
    maki "Know each other? We’re practically inseparable."
    s "We’ve hung out a couple times."
    sa "That’s...worrying."
    maki "What’s truly worrying is your mother, dear."
    maki "Is she okay?"

    scene bartwofive13
    with dissolve

    sa "I...think so? Why do you ask?"
    maki "Well, because she was one of my regular customers and I haven’t been seeing her much at all lately."
    s "Sara is a regular at the porn shop?"

    scene bartwofive14
    with dissolve

    if bonus == True:
        maki "Oh, please. If I had a dollar for every dildo I’ve sold that woman, I’d have enough to open two more stores."
        s "I’d hope that you’re profiting at least a dollar from every sex toy you sell."
        s "You might need to raise your prices if that’s not the case."
    else:
        maki "She never buys anything. She just likes to run in circles around the store screaming about how her love life is falling apart."

    sa "Umm...can we...talk about something else?..."
    sa "I don’t really..."

    scene bartwofive15
    with dissolve

    if bonus == True:
        maki "Oh gosh. Of course! I forgot how innocent and untainted you are. So different from your perverted mother."
    else:
        maki "The only other thing I have any knowledge about is the North American Free Trade Agreement."

    s "This is probably why you weren’t invited out tonight, Maki."

    scene bartwofive16
    with dissolve

    maki "Rude!"
    sa "Umm...to get things back on track...maybe we should do the question thing...another time?"

    if bonus == True:
        s "I think we’re still fine as long as Maki agrees to not make things perverted."
        maki "You overestimate me, good sir. Of course I'm going to make things perverted."
    else:
        s "I think we're fine as long as Maki promises to not bring up NAFTA."
        maki "You understimate my power."

    scene bartwofive17
    with dissolve

    maki "But go ahead and play your game, dear. I have a daughter, too, so I know when I need to take the back seat."
    sa "You...have a daughter?..."
    s "That’s Makoto’s mom."
    sa "..."
    maki "..."
    s "..."

    scene bartwofive18
    with hpunch

    sa "What?!"
    sa "Like...class president Makoto?"
    maki "Yes, yes. Please tell me more about how impressive my daughter is. I live for it."

    scene bartwofive19
    with dissolve

    sa "Well...I guess that explains why you know her a little better then..."
    sa "For a second, I was worried you were also a...regular customer..."
    maki "What are you talking about? Of course he’s-"
    s "Okay, Sana. Question game starts now."
    s "Ask me whatever you like."

    scene bartwofive20
    with dissolve

    maki "Mm!"
    sa "Um...uhh...it’s kind of hard when you put me on the spot like that..."
    maki "Hard like a-"
    s "Maki."

    scene bartwofive21
    with dissolve

    maki "MMM!!!!"
    sa "Umm...okay...how about this..."
    sa "If you had to...describe your outlook on life with...a vegetable...what vegetable would it be?"
    s "...That’s your question?"
    sa "Yeah. That’s the question I chose and you need to answer it or...I’ll kick you out of the bar."
    s "But then you’d be alone with the porn lady."

    scene bartwofive22
    with dissolve

    maki "I don’t think your mother would like that very much. I'm a bad influence."
    sa "Answer the question...or else."
    s "Wow, Sana. Maybe you {i}are{/i} improving your social skills? It’s not like you to put your foot down. Especially in front of other people."
    sa "Vegetable. Tell me."
    s "Maybe...a tomato?"

    scene bartwofive23
    with dissolve

    sa "Wait...isn’t the tomato a fruit?"
    s "Oh, don’t even start. That’s a whole other game."
    maki "Why a tomato?"
    s "Probably because...On the outside, it pretty much always looks fine."
    s "But sometimes, you’ll bite into one and it'll be outright rotten."
    s "That’s kind of how I look at life, I guess."
    s "Approach everything normally, but don’t be surprised if things turn out horrible all of a sudden."
    sa "..."
    maki "..."
    s "..."

    if bonus == True:
        maki "You need to get laid."
    else:
        maki "You need a hug."

    scene bartwofive24
    with dissolve

    sa "When you put it that way...I kind of agree..."

    if bonus == True:
        sa "Not about the...l-laid part, though..."
    else:
        sa "Not about the...hug, though..."
        sa "Hugs are immoral..."

    sa "There’s not really any way to tell when things will go bad..."
    sa "Which is...one of the reasons I don’t like tomatoes."
    s "Is one of the other reasons that they’re a key ingredient in-"
    sa "Don’t...even think about it, Sensei..."
    maki "Don’t think about what? Am I missing out on an inside joke here?"
    s "Didn’t you come here to drink?"
    s "What happened to taking the back seat and letting us have our conversation?"
    s "This could be a breakthrough moment for Sana."

    scene bartwofive25
    with dissolve

    if bonus == True:
        maki "Good luck breaking through {i}anything{/i} with that attitude."
        s "..."
        sa "Um...what does she mean by...breaking through {i}anything{/i}?..."
        sa "Did I do something wrong?..."
        maki "Yes. Tell her, Sensei. Tell her all about what you want to break through."
        s "It’s just some...adult humor. Don’t pay any mind to her."
    else:
        maki "That girl couldn't break her way out of a paper bag. Look at those weak, little arms of hers."
        s "Leave her alone. She is a health inspector."
        sa "I am...confused about the relevance of my occupation in regard to-"
        s "It’s just some off brand humor. Don't worry about it, Sana."

    scene bartwofive26
    with dissolve

    sa "Well...no matter what type of humor it is...I’m glad we have the same vegetable answer..."
    s "Have you adopted the way of the tomato as well, Sana?"
    sa "Um...I guess so?"
    sa "I wouldn’t really call it the way of the tomato, though...that sounds kind of silly."
    s "Yeah. We’ll think up a better name for it in the future."

    scene bartwofive27
    with dissolve

    sa "Did you...maybe want to ask me something now...Sensei?"
    sa "It’s not much of a game if we just...stop after the vegetable..."

    "Hmm..."
    "A question for Sana."
    "Is there anything I’ve been wanting to ask her? "
    "It could be something as simple as just asking her what kind of music she likes."
    "But I feel like now might be a good opportunity to pry a little further into her past."
    "Sana’s never really elaborated on her personal life or any problems but..."
    "Well, Maki is right next to us and serving as a sort of ‘block’ right now."
    "So maybe sticking with a simple question would be good for the time being?"
    "I can always ask her more personal things some other time."

    s "How about this..."
    s "If you were magically granted the ability to play any instrument what would it be?"

    if bonus == True:
        maki "Skin flute."
    else:
        maki "Horseradish."

    s "Maki."

    scene bartwofive28
    with dissolve

    sa "I’m kind of...relieved that you chose something like that and not anything weird..."
    s "No weird questions until at least Round-3. That’s the rule."
    sa "Well...I don’t understand what rule you’re talking about...but I think it would be fun to play the drums."
    s "The drums? Really? You seem like more of a...keyboard player than a drummer."

    scene bartwofive29
    with dissolve

    sa "Heheh...I can see why you’d say that..."
    sa "But who we are on the outside doesn’t always match who we are on the inside..."
    sa "Maybe there’s a...drummer inside of me that’s just dying to come out some day?"

    scene bartwofive27
    with dissolve

    sa "Obviously...something like that won’t ever happen..."
    sa "But if magic were involved and...I could make the choice myself..."
    sa "Definitely drums..."

    scene bartwofive30
    with dissolve

    sa "I’d also look super awesome and...badass behind a drum set...Right, Sensei?"
    s "..."
    sa "..."
    s "..."

    scene bartwofive31
    with dissolve

    sa "Why aren’t you saying anything?..."

    scene black
    with dissolve2

    "The conversation carries on for a full hour after that."
    "We go back and forth asking each other seemingly pointless things and slowly but surely chipping away at what makes each of us tick."
    "One thing I realize is that almost every single one of Sana’s answers is something I don’t expect to hear."
    "It, once again, reminds me that there really might be a lot more to her than she lets on."
    "And hiding somewhere deep within that tiny frame of hers-"
    "Lies a super awesome, badass drummer just waiting to escape."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar25 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar30:
    scene sanadrunkagain1
    with fade
    play music "calmbar.mp3"

    sa "Hey...*hic* you..."
    sa "Whatchadoin’here?"

    "I arrive at the bar to find an unexpectedly inebriated Sana."

    if bonus == True:
        "Typically, things like drinking in your own workplace are frowned upon, especially for a [high_school]er..."
    else:
        "Typically, things like drinking in your own workplace are frowned upon, especially for a college student..."

    "But I guess given the nature of this establishment, it’s not too unusual."
    "I’m sure her mother was doing the exact same thing at her age."

    scene sanadrunkagain2
    with dissolve

    sar "Sensei! How dare you get my daughter drunk while I wasn’t watching!"
    s "Wait, what? I literally just got here."

    scene sanadrunkagain3

    sar "I know that, silly. I’m just messing with you."
    sar "We closed early tonight because Sana wasn’t feeling great."
    sar "Sooooo I gave her the only medicine that’s ever worked for me."
    s "You medicated your daughter with alcohol?"

    scene sanadrunkagain2

    sar "Well it worked, didn’t it? Look at her! She’s just peachy!"

    scene sanadrunkagain4
    with dissolve

    sa "Hey...ya ever think’ that...there’s more to life than just...all the things you do in life?"
    s "What does that even mean?"
    sa "Itmeanseverything."

    scene sanadrunkagain3
    with dissolve

    s "Are you positive that all she’s had is alcohol? She seems a little too far gone for that to be true."
    sar "She just needs to build up her tolerance. She might be my daughter but it’s not like she was born with an iron stomach."
    s "Is it even your stomach that processes alcohol?"
    sar "Beats me. You’re the teacher here."

    scene sanadrunkagain4
    with dissolve

    sa "Sensei...I’vebeendoin’somethinking..."
    sa "And I think...it’s about time I...cameouttamyshell..."
    sa "*Hic* ya know? Sometimes ya just gotta get out there and do the thing."
    s "What “thing” are you trying to do exactly, Sana? "
    sa "Idunno...issa...thing Rin says all the time..."
    sa "I’m just...doing what the Romans do..."

    scene sanadrunkagain2
    with dissolve

    sar "And on that note, I’m going to head upstairs."
    s "Wait, really?"
    s "I was under the impression you’d be joining us."
    sar "Not tonight, I’m afraid. There’s a glass of wine and a romance novel waiting for me in my bedroom."
    s "Why is there already a glass of wine poured in your bedroom?"

    scene sanadrunkagain5
    with dissolve

    sar "Stop asking questions and comfort my daughter."
    sar "She’s been down all day and I think you’re the one she needs to see."
    sar "I love her, but I’m not exactly the best when it comes to cheering people up. Hence alcohol."

    scene sanadrunkagain4
    with dissolve

    sa "Yeah...*hic* stay and...talk to me...Sensei..."
    sa "We’ll be all alone...we can do...{i}whateverwewant{/i}..."
    sar "Remember Sensei, even if girls say that while they’re drunk, they don’t necessarily mean it."
    s "You’re one to talk, Sara."
    sar "Heheh~ I sure am."
    sar "Have a good night, you two!"

    "I can hear Sara’s footsteps trail up the stairs and stop in the room above us."
    "I can even hear the bed squeak as she hops onto it."

    if sarasex == True and bonus == True:
        "That’s...mildly concerning for a number of reasons."

    else:
        "I feel like that would be cause for concern if the two of us were to ever...you know."

    scene sanadrunkagain1
    with dissolve

    sa "Hehehe...now I’ve gotcha...alltomyself..."
    s "How much have you had to drink, exactly?"
    sa "A million..."
    s "I think we need to get you into an ambulance if that’s the case."

    scene sanadrunkagain6
    with dissolve

    sa "I’m just kidding...I’m drunk but not...a million drunk."
    s "Wow, you really had me going there for a second. I sincerely believed you were a million drunk."
    sa "Heheh~ It’s all that...role playing experience from...vacation."
    s "Well, whatever you do, please don’t cut me in half like that mushroom monster or whatever it was."
    sa "You don’t have to worry...Orc Sana is much stronger than normal Sana..."
    sa "Normal Sana probably couldn’t even hold a battle axe..."

    "Sana sprawls out further so her leg doesn’t wind up falling off of the table."
    "She looks very different from how she normally is. And no, it's not because she’s drunk."
    "Well, I'm sure that's part of it."
    "But it’s the first time I’ve seen her in an actual relaxed position. "
    "It’s like she’s lounging around her bedroom right now."
    "Which, to be fair, is at least partially true since her mother is right upstairs."
    "But still."

    sa "Aren’t you...gonna ask me what was bothering me, Sensei?"
    sa "My mom just told ya I was down and you haven’t even...asked me why yet..."
    sa "If I was Ayane, you probably would’ve asked right away...right?"
    s "I was getting there."
    s "You’re still not great at conversation yet, so you haven’t realized that there are some steps involved when you want to get someone to open up."

    scene sanadrunkagain7
    with dissolve

    sa "What kind of steps?..."

    if bonus == True:
        s "Small talk. Prodding."
        sa "Prodding sounds lewd...Is that really one of the steps?..."
        s "Not that kind of prodding. That comes later."
    else:
        s "You know like when you're playing Monopoly and you have to go backwards?"
        sa "Not...really..."
        s "Oh. Well, shit."

    s "But yeah...what’s bothering you exactly?"
    sa "Woah...I’m glad you asked without...me having to force you to..."
    s "Sana..."

    scene sanadrunkagain8
    with dissolve

    sa "Remember that girl from the other night?"
    s "What, you mean the creepy, white-haired one?"
    sa "Yeah, that’s the one."
    sa "She said some strange things, didn’t she?"
    s "Pretty much everything she said was strange."
    sa "She said you saw God..."
    sa "Is that true, Sensei?"
    s "Not to my knowledge. I’m pretty sure I’d remember something like that."

    scene sanadrunkagain6
    with dissolve

    sa "Would you?"
    sa "Maybe God has like...crazy mind control powers or something...like in a movie."
    sa "He’s God, so he can do whatever he wants, right?"
    s "Is that why you’re feeling down? You’re thinking about God?"

    scene sanadrunkagain9
    with dissolve

    sa "Nah...It’s nothing that interesting..."
    sa "It’s something else she said that’s been bugging me."

    "I think back to the other things the white-haired girl said during our very brief but extraordinarily creepy meeting."
    "The ones that stick out among them are...something about the path I walk...seeing the end of the world and..."
    "That someone Sana knows is happy."

    s "Who was the girl talking about when she looked at you?"
    sa "Could be anyone...she was...kind of weird..."
    sa "But, if I had to take a guess-"
    sa "Probably my brother."
    s "You have a brother?"

    scene sanadrunkagain10
    with dissolve

    sa "You don’t pay much attention...do you?"
    sa "I told you that the first time you came to the bar...and you never even asked about it."

    scene sanadrunkagain6
    with dissolve

    sa "How long have you been coming here now?..."
    sa "Long enough to start asking me more personal questions...right?"

    "I try to think back to my first meeting with Sana at the bar, but it seems so long ago now."
    "But somewhere, buried deep beneath almost every other memory I’ve made with her, there is {i}something{/i}."

    s "That’s his uniform, isn’t it?"

    scene sanadrunkagain8
    with dissolve

    sa "Was..."
    sa "He’s gone now."
    sa "Which is probably why...that crazy girl’s words went straight to my head..."
    sa "Chances are she was just...off her medication like you said..but what if she wasn’t?"
    sa "What if she can...talk to the dead...or something?"
    sa "Sooo, yeah...That’s what I’ve been thinking about."
    s "And I’m guessing that’s also why you couldn’t bring your mom into it?"

    scene sanadrunkagain11
    with dissolve

    sa "Sensei..."
    sa "It’s really hard, you know?..."
    sa "She changes the subject any time it comes up..."
    sa "We’ve never even really talked about it before..."

    scene sanadrunkagain12
    with dissolve

    sa "You’d think me wearing his clothes to work every day would at least start a conversation with her but...nope."

    scene sanadrunkagain13
    with dissolve

    sa "Who knows, though? Maybe I’m just crazy and he never existed in the first place..."
    sa "Maybe it’s all just a dream."
    s "..."
    sa "..."

    scene sanadrunkagain14
    with fade

    sa "Um...A-Anyway! H-How about we talk about something...fun instead?"
    sa "I...don’t want to be one of those people who just...rambles on and on about her feelings when she’s drunk so..."
    sa "Maybe we could play the question game again?..."
    sa "Makoto’s mom isn’t here to interrupt us this time so...we can ask whatever we want..."

    scene sanadrunkagain15
    with dissolve

    if bonus == True:
        sa "I’d...still prefer nothing perverted, though..."
        sa "Even if we’re closer than we were before...you’re still my teacher and...there’s the thing with Ayane too and..."
        sa "And my mom is right upstairs."
        s "Okay. Well, here’s a question..."
    else:
        sa "We should probably...not bring up my secret identity, though..."
        s "As a health inspector?"
        sa "Y-Yeah..."
        sa "I know I'm...not like Ayane or my mom, but..."

    s "Why does everyone you associate with like me so much? It's odd."

    scene sanadrunkagain16
    with dissolve

    sa "Right?! "
    sa "I have no idea!"
    sa "Do you have any idea how weird that is for me?!"
    s "It’s weirder for me. I don’t even think I’ve done anything to warrant that sort of admiration."
    sa "You really haven’t!"
    s "..."
    s "You could have at least tried to pretend that wasn’t true."

    scene sanadrunkagain17
    with dissolve

    sa "Sorry...I’m drunk and...don’t have control over myself right now..."
    sa "You know I think you’re cool..."
    sa "I’m sure everyone else sees you the same way..."
    sa "Also, umm, this might sound a little weird...but I think you have really pretty eyes as well..."
    sa "It’s even...kind of hard to look at them sometimes."
    s "Thanks Sana. I think you have a really pretty eye as well."

    scene sanadrunkagain18
    with dissolve

    sa "The second one actually has special powers..."
    sa "The reason I was holding my hair back for most of this conversation was to...hypnotize you..."
    s "Into doing what, exactly?"
    sa "Into being a normal teacher again. One that can help me with history..."
    sa "And also one that doesn’t think my mom is cute."
    s "Okay, come on, though. We both know your mom is cute."

    scene sanadrunkagain19
    with dissolve

    sa "Ugh! Don't remind me! It's annoying!"
    sa "She’s pure evil, I tell you! She’d do anything to be the center of attention!"
    s "..."
    sa "I’m gonna go get another drink!"

    scene sanadrunkagain20
    with dissolve

    sa "Do you want anything?!"
    s "...I’ll have a beer."
    sa "Okay!"

    "Sana storms off toward the bar and throws open the doors of the cooler, grabbing a drink for both herself and me."
    "I’m surprised she had such a...passionate reaction to my mention of Sara this time."
    "Maybe it’s just the alcohol, but I feel like she’d typically get embarrassed and down on herself instead of walking away in a fit of rage."
    "The dynamic between those two is confusing."

    scene sanadrunkagain21
    with dissolve

    sa "..."

    "Sana returns moments later with two cans- one for me and one for her."

    sa "..."

    "She also doesn’t say a single word and elects to just stare at me instead."

    s "...What?"
    sa "You realize...that if I finish this beer...I may not be able to walk."
    s "Then why drink it?..."
    sa "I...do not give you permission to carry me upstairs again."
    sa "I am still dealing with the embarrassment from the last time that happened."
    s "So...just leave you on the couch?"
    sa "It’s a good couch. "
    s "Sure, whatever. Just don’t look at me like that anymore. It’s weird."
    sa "You’re weird."
    s "Okay, Sana."
    sa "..."
    s "..."

    scene sanadrunkagain22
    with dissolve

    sa "Heheh..."
    sa "I’m glad you came tonight, Sensei..."
    sa "I’m already feeling a little better..."

    scene sanadrunkagain23
    with dissolve

    sa "Maybe my mom’s method of medicating...works after all?..."
    s "Yeah, let’s not have you fall down the path to alcoholism at such a [young]age."

    scene black
    with dissolve2

    "Sana does, in fact, finish the beer."
    "And her legs do, in fact, give out."
    "I walk up the stairs into Sara’s apartment to find her already passed out."
    "So much for her romance novel, I guess."
    "I take a spare pillow and blanket from a couch in the living room and bring them downstairs, setting Sana up with them before I leave."
    "..."
    "It was another interesting night at the bar, if not anything else."
    "Hopefully, this time I can find it within myself to not forget such an important detail about her life."
    "But, for some reason, I already feel like something along those lines won’t happen again."
    "It’s safe to say that Sana’s become pretty important to me."
    "Sure, she might be more like a daughter than anything else at this moment, but-"
    "But I’m sure that still has room to change..."
    "I mean, who knows?"
    "This is Kumon-mi, after all."
    "Anything can happen here."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar30 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar35:
    scene barwakaosako1
    with fade
    play music "calmbar.mp3"

    "I make my way to the bar to be immediately greeted by not only a warm atmosphere, but the warm smile of a girl under five feet tall."

    s "{i}You’re so adorable.{/i}"
    sa "Hm?...What was that?"
    s "Just saying hello. "
    s "How’s the bar doing?"

    scene barwakaosako2
    with dissolve

    sa "Umm...the same as always, I guess."
    sa "My mom isn’t feeling well tonight so I’ve...gotta do everything on my own again."
    s "Really? What happened?"
    sa "She may have...sampled too many of the products."
    s "Oh. {i}That{/i} kind of not feeling well."
    sa "Right..."
    s "Well, thankfully, it’s not like this place is busy or anything."
    s "I’m pretty sure roughly half of your sales are just...me."

    scene barwakaosako3
    with dissolve

    sa "Well...while that’s normally true...there’s someone here tonight that’s drinking a lot more than I’ve ever...seen {i}you{/i} drink before."

    "Sana redirects her gaze to a table in the back of the room that I must have overlooked upon entering."
    "I guess I’ve gotten so used to this place being completely dead that I’ve just stopped observing my surroundings. "
    "But knowing that it’s the back of the room, there’s a good chance that it’s the same old women who-"

    scene barwakaosako4
    with fade

    s "Wait, what?"
    s "Those two know each other?"
    sa "Do you...know them, Sensei?"

    scene barwakaosako5
    with fade

    s "I’m surprised you don’t. Well, the one on the right, at least."
    sa "Why would I know her? This is her first time coming in."
    sa "She’s not...some kind of celebrity, is she?"
    s "That’s Ms. Watabe- The teacher in the classroom next to ours."
    sa "..."
    s "Does that not ring a bell?"
    sa "Sensei...I don’t know if you’ve realized this, but..."
    sa "I kind of keep my head down all day in[school]."
    sa "I don’t even think I can...name another teacher."
    s "I literally just told you the name of one. "

    scene barwakaosako6
    with dissolve

    sa "Ms...Watanabe?"
    s "Watabe. You did that on purpose."

    scene barwakaosako7
    with dissolve

    sa "Sorry...but there’s only enough room in my head for one teacher."
    s "{i}You’re so adorable.{/i}"
    sa "You need to speak up...You’re being really quiet tonight, Sensei..."
    s "Yeah, well, you’re really quiet all the time. I’m just giving you a taste of your own medicine."
    sa "Well I need to...go give those girls a taste of more...medicine...so..."
    s "Just because your mother uses it to medicate both herself and you does not make it medicine, Sana..."
    s "But fine. Why don’t I help you?"
    sa "Help me?"
    sa "You mean like...you’ll carry the-"
    s "I won’t be carrying anything."

    scene barwakaosako8
    with dissolve

    sa "Of course you won’t..."
    s "I just want to see how you interact with other adults. "
    s "We’ve practiced your public speaking enough that it’s time for us to conduct our first field test."
    sa "You kind of...stopped teaching me about speaking altogether...you just sit there and drink now."
    s "True, but my intentions are pure."

    "No they aren’t."

    sa "So...you’re going to follow me to their table and just...watch me?"
    sa "Doesn’t that sound...a little weird for...pretty much everyone involved?"
    s "Ms. Watabe is dead inside so it will only be weird for three of us."
    s "It gives me an excuse to go say hi to them anyway."
    sa "Umm...okay, but...can you just...try not to be awkward?"
    s "..."
    sa "..."
    s "You’re the one telling {i}me{/i} not to be awkward? "
    s "Do you have any idea how popular I am?"
    sa "With [teenage]girls or...regular people?"

    if bonus == True:
        s "Mostly the former. But there are plenty of adults who love me as well. "
    else:
        s "How do they not count as regular people? A large portion of the population is in college."

    s "Just ask your mom."
    sa "Uhh...I’d really rather not..."
    sa "Anytime she talks about you I...kind of want to slap her in the face..."
    s "Getting jealous that she might steal me away from you?"

    scene barwakaosako9
    with dissolve

    sa "Jealous? Me? "
    sa "You really think I’d get jealous from...my mom and my best friend talking about you all the time?"

    "Clearly. I didn't even mention Ayane and she brought her up anyway."

    sa "Hahaha...Sensei, that’s so crazy...hahaha..."
    sa "I love listening to all of the things they say about you and...not being able to contribute to the conversation at all."
    s "What do you mean you can’t contribute to the conversation? I’m here for {i}you{/i} tonight, aren’t I? Just...brag about that."
    s "It means I'm choosing you over them."

    "Well, at least for right now."

    scene barwakaosako10
    with dissolve

    sa "Are you really, though?"

    scene barwakaosako7
    with dissolve

    sa "A-Anyway...I guess...feel free to follow me to the table and...see how much I’ve improved thanks to your...pure intentions."

    scene black
    with dissolve

    "Sana comes out from behind the bar and I get out of my chair to follow her."
    "The girls in the back of the room notice this and begin to tone down their conversation in preparation for more booze."
    "They also finally notice my presence, which makes me feel a little bit better about overlooking {i}them{/i} when I first came in tonight."

    scene barwakaosako11
    with dissolve

    os "Woah. When did you get here?"
    s "A little while ago. I didn’t realize you two were friends."
    w "Is it really such a surprise to you that I have a life outside of the[school]?"
    s "Kind of, yeah."

    scene barwakaosako12
    with dissolve

    sa "Um...can I...help you two with anything else?"
    w "Speak louder. You’re too quiet. "
    os "Another beer for me. Probably four more for my {i}friend{/i} here."
    w "Five."
    w "I can still feel things. It’s troublesome."
    os "Also, do you guys have like, some taxi service you’re partnered with or anything?"
    os "She drove tonight and I definitely don’t want to get into the car with her."
    w "If I’m lucky, maybe I’ll drive off of a cliff."
    s "Good luck finding a cliff in Kumon-mi."
    sa "We, umm...don’t really have anything like that, but...I can check on my phone if that will help you..."

    scene barwakaosako13
    with dissolve

    w "Would you like anything, {i}Sensei{/i}?"
    s "Are you...offering to buy me a drink?"
    w "No. I was going to order the rest of whatever you wanted so you wouldn’t be able to have any."
    w "Of course I was offering to buy you a drink."
    w "I’m extremely drunk. Can’t you tell?"
    s "Not really, no."
    w "Well, whatever. You missed your chance."
    sa "Okay, so...six more beers total..."
    sa "Is there anything else?..."

    scene barwakaosako14
    with dissolve

    s "You should order the spaghetti. It’s really good here."
    os "Huh? This place has a food menu? I had no idea."
    sa "It...doesn’t..."
    sa "Sensei is just being...a big jerk...and tormenting me..."
    os "Ooooooh okay, okay. So this guy’s your teacher."

    if bonus == True:
        os "Here I was thinking he was just getting himself involved in a {i}second{/i} relationship with a girl your age."
    else:
        os "Here I was thinking he was just getting himself involved with a {i}second{/i} college chick."

    scene barwakaosako15
    with dissolve

    sa "S...Second?"
    sa "There’s a first?"
    os "Yeah. Some loud blonde girl that trains at my dojo with him."
    s "Sana, meet my karate instructor, Osako. "
    s "She also works at a local ma-"

    scene barwakaosako16
    with dissolve

    os "Hey! You’re not forgetting that I can kick your ass, are you?!"
    os "You said you wouldn’t tell anyone!"
    s "I said I wouldn’t tell anyone {i}at the dojo{/i}."
    os "Life’s a fuckin’ dojo. Tell ANYONE-anyone and I’ll break your fucking arms."

    scene barwakaosako17
    with dissolve

    sa "So it’s just...karate and not...an actual relationship."
    sa "I knew Ayane went but...I didn’t know you were going there too, Sensei..."
    s "Really? It’s weird that she never told you given how much she apparently talks about me."
    sa "All of the things she says about you are a lot...um...more {i}romantic{/i}."
    w "So the rumors were true."
    s "Stop bringing up those {i}entirely baseless{/i} rumors and finish your beer, Wakana."
    w "I’ve been finished with this one for five minutes."
    w "I’m still waiting on another but you’re distracting this poor girl from doing her job."

    scene barwakaosako18
    with dissolve

    sa "O-Oh! I’m...s-sorry! I-"
    w "Don’t worry about it. There’s no way I’m going to remember any of this in the morning, anyway."
    s "You’re way too competent for how drunk you apparently are."
    sa "I...umm...I’ll be right back..."

    scene barwakaosako19
    with dissolve

    "Sana suddenly scurries off to the counter and begins to stack a bunch of cans on a tray to bring over, leaving me alone with Osako and Wakana."

    w "You know it’s prohibited for students to have part-time jobs, correct?"
    s "Are you telling me none of your students have jobs?"
    w "Not anymore. You took the three that did."
    s "You don’t plan on doing anything about it, though, right?"

    if bonus == True:
        w "What would I even do? Get them all fired and force them to sell their bodies to put themselves through college?"
    else:
        w "What would I even do? I don't have the energy to get involved in this."

    w "Or are they so far behind in their education thanks to your genius teaching strategies that college isn’t an option in the first place?"
    os "Wow. You two are a lot closer than I thought."

    scene barwakaosako20
    with dissolve

    w "We’re very good friends."

    "We are?"

    s "Our relationship aside, how do you two know each other?"

    scene barwakaosako19
    with dissolve

    os "Figured you’d know since you guys are so close."
    os "Wakana and I live together."
    os "Have for a few years now."
    w "We met in college."
    w "I would die for her if the need arose."
    s "You would die for anyone or anything at this point."
    w "Not you, you fucking buffoon. "

    scene barwakaosako21
    with dissolve

    os "Hahaha! I haven’t seen her get along this well with somebody in years. "
    os "I’m actually kind of impressed."

    "{i}This{/i} is getting along with Wakana?..."

    scene black
    with dissolve

    "Sana comes back moments later and bashfully places an entire six pack on the table, telling Osako and Wakana they can just help themselves and let her know if they need anything else."
    "I decide to leave the two of them alone and retreat back to the counter with Sana to recap the {i}incredibly purposeful{/i} experiment we just had."

    scene barwakaosako22
    with dissolve

    s "You didn’t cry when I said “spaghetti.” Great job, Sana."
    sa "I’d...appreciate it if you’d stop bringing that up all the time..."
    s "It’s one of my fondest memories of you."
    sa "Why is me getting so flustered that I started crying a...good memory for you?"
    s "To be fair, I don’t have much to work with. Our relationship has been limited to pretty much the bar and your room."
    sa "And[school], but..."

    scene barwakaosako23
    with dissolve

    sa "Y-Yeah...I’m not really like Ayane and...the two of us don’t have the kind of relationship that is able to make memories like that..."
    s "Are you being jealous again now, Sana?"
    sa "I..."
    sa "..."

    "Instead of refuting that immediately like I expect her to, Sana hesitates."
    "She plays with the knot of her tie, undoing it slightly with her fingers and drawing attention to how slender her neck is."
    "If that outfit really did belong to her brother (Which I’m sure it did because why would she lie?), he must have been very small as well."
    "I guess being short is just...a Sakakibara gene or something."

    sa "I..."
    sa "I’d like...to try karate too, Sensei..."
    s "..."
    s "{i}You’re so adorable.{/i}"

    scene barwakaosako24
    with dissolve

    sa "Again?! Why are you so quiet today?!"
    s "Why not ask Ayane if you want to get into karate? She’s been going there longer than I have. "
    s "You said that you knew she did it, so why wait until now to come out and talk about wanting to try?"

    "Obviously, the answer is because now she knows I’m involved and she’s worried about things progressing any further with Ayane and me."
    "But {i}also{/i} obviously, there’s no way I’d actually come out and tell her I know that."
    "It’s my job to feign density for the sake of her comfort."
    "And not just hers, but the comfort of everyone around her as well."
    "Sana still needs to come out of her shell, and for that-"

    scene barwakaosako23
    with dissolve

    sa "Because I want to...do it with you..."

    "And there it is."
    "I’m surprised she put it so bluntly, though."

    scene barwakaosako25
    with dissolve

    sa "Ah! W-w-w-w-wait! By “do it” I meant karate! Not the other thing!"
    s "I’m aware that you meant karate, Sana."
    sa "You are?!"
    s "Of course."
    sa "So...so now me freaking out makes it seem like I w-w-was thinking about the other thing?!"
    s "A little bit, yes."
    s "You should calm down before your other customers in the back of the room take notice."
    sa "N-n-n-n-notice what?! That I want to do karate?!"
    sa "I love karate! Please teach me karate, Sensei!"
    os "Hm? You guys talkin’ about karate over there?"

    scene barwakaosako26
    with dissolve

    sa "Oh! Uhh...look at the time!"
    sa "I’ve gotta go...take care of something in the back!"
    sa "Uhhhhhh bye!"

    scene black
    with dissolve2

    "Sana runs away and trips over a rubber mat in front of the door to the back room, banging her head before letting out a high pitched shriek and tumbling inside."
    "I think about getting up to help her but realize that she’d likely rather be alone right now- at least until she’s able to calm herself down."
    "And, of course, that happens several minutes later."
    "She returns to the bar and everything goes back to normal."
    "With her being shy and me being me."
    "But progress was made today."
    "If Sana is ever going to get anywhere, she needs to start being honest with herself...and start being honest {i}to{/i} others."
    "And I don’t mean just me."
    "I mean to Ayane and Sara as well."
    "If she’s so bothered by their incessant need to bring me up in conversation, the least she can do is find a way to “contribute” as well."
    "That won’t ever happen if she doesn’t change."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar35 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar40:
    scene barwalkhome1
    with fade
    play music "love.mp3"

    sa "Oh...Sensei."
    sa "Um...you have...pretty bad timing tonight..."

    "I show up at the bar a little later than normal to find Sana already prepared to leave."
    "I slide my phone out of my pocket to check the time and, even though it's late, it’s nowhere near closing time yet."
    "Well, actually, I guess closing time in a place like this is whenever the person running it wants it to be, so..."
    "I’m sure Sara has something to do with this."

    s "Leaving already?"
    s "Isn’t it a little too early?"
    sa "Normally...yes."
    sa "But we closed half an hour ago..."
    sar "You should learn to read signs, Sensei. "
    sar "Those big letters on the door that say “closed” mean we’re not open."
    s "I blame you for changing the hours so suddenly and throwing me off."
    s "What’s the reason you're closing so early tonight?"

    scene barwalkhome2
    with dissolve

    sa "I...don’t really know either, to be honest..."
    sa "I think my mom isn’t feeling well, but...that doesn’t mean I couldn’t look after the place myself..."
    sar "Don’t listen to her. I’m fine."
    sar "Just figured it would be good for the two of us to get some time off."
    sar "Ideally, Sana would have come upstairs to hang out with me, but she keeps talking about how tired she is."
    sa "The walk back is kind of long, so...if I can start heading back earlier I...probably should."

    scene barwalkhome3
    with dissolve

    sar "Yeah, yeah. Go home and sleep. "
    sar "I’ll just sit upstairs and do my best Haru-chan impression by watching movies and eating ice cream until I pass out."
    s "Better habit than drinking until you pass out, at least."
    sar "Is it really, though?"
    sa "Um...S-Sensei?"
    sa "You wouldn’t want to...maybe..."

    scene barwalkhome4
    with dissolve

    sa "W...Walk back with me...would you?"
    sar "He’s got no choice. We’re closed for the night."
    s "Wow. You’re not offering to keep the place open as a special favor to me?"
    s "You really aren’t feeling well, are-"
    sar "I said I’m fine."
    s "...Okay."
    sa "Um...is that a...no?"
    s "Not at all. Of course I’ll walk back with you."
    s "I came here to see you again, so it’s not like there’s anything else I have planned for tonight."

    scene barwalkhome5
    with dissolve

    sa "Really?..."
    sa "I...walk kind of slow since my legs are really small, so...I hope that’s not a bother..."
    s "I could always just carry you home instead if you want. "
    s "I can’t imagine you weigh more than a six pack of beer."

    scene barwalkhome6
    with dissolve

    sa "Uhh...n...no..."
    sa "You don’t have to carry me..."
    sa "And I...definitely weigh more than...a six pack of beer..."
    s "Jump into my arms and prove it."
    sa "..."
    sa "Maybe I should walk home alone after all?..."
    s "I’m kidding..."

    "I really wasn’t, though."

    if bonus == False:
        "I could really use a hug right now."

    scene barwalkhome7
    with dissolve

    sa "Hahah...y-yeah...I figured as much..."
    sa "But, umm...I guess we should head out so...my mom can start doing her...Haruka impression."
    sar "For real. I gave you both the green light to abandon little ole’ me and you’re still standing there talking."
    sar "Am I really that irresistible?"
    sa "{i}It certainly feels that way sometimes...{/i}"

    scene barwalkhome8
    with dissolve

    sa "A-Anyway...let’s start walking, Sensei..."
    sa "I know a...pretty quick way back, so...we’ll get there in no time."

    scene black
    with dissolve2

    "I follow Sana out of the bar, taking a look over my shoulder to see if Sara has changed expressions now that we’re finally leaving."
    "She had a pretty...interesting moment when I saw her in Sana’s room recently, so I wouldn’t be surprised if this somehow had something to do with that."
    "Perhaps more interesting, though, is how Sana has finally agreed to walk home with me."
    "I feel like I’ve offered this countless times in the past, so I figured the first time it actually happened would be the result of yet another one of my invites."
    "But, strangely enough, she’s the one who invited me."
    "Here’s hoping her “really small legs” don’t provide much of a hindrance to what I imagine will be a relatively peaceful walk back."
    "........."
    "......"
    "..."

    scene barwalkhome9
    with dissolve2

    "As expected, we don’t have the easiest time thinking up conversation topics as we wander down the streets toward the dorms."
    "I hate having to take the lead in situations like this. It’s exhausting. "
    "Putting two people together who struggle with that same exact thing turns what could be a sweet event in a romantic comedy into a night that will be easy to look back on and cringe."
    "{i}Why did it take so long for us to break the silence?{/i}"
    "{i}There were so many other things we could have talked about.{/i}"
    "Things like that."
    "Things you think but never say."
    "So, in layman’s terms- "
    "Most things."

    scene barwalkhome10
    with dissolve

    sa "How...tall do you feel right now?"
    s "Like a giant."
    s "I always forget how short you are until you’re standing right next to me."
    sa "It probably helps that I...don’t get to stand next to you all that often..."
    sa "I’m happy I...got to tonight, though..."
    s "I’m surprised you were feeling up to this all of a sudden."
    s "I feel like I’ve tried to do this with you a bunch of times now."

    scene barwalkhome11
    with dissolve

    sa "Y-Yeah...even though I’m happy, it...still feels really weird..."
    sa "Who would have thought that...someone who has so much trouble making friends would...wind up having a guy {i}your{/i} age as one?..."
    s "Are you calling me old, Sana?"

    scene barwalkhome12
    with dissolve

    if bonus == True:
        sa "Super old...old enough to be my dad, probably..."
    else:
        sa "Not...that old...but like...closer to my mom's age than mine..."
        sa "Like...you guys could be married..."

    s "I’m sure your mother would love that."

    scene barwalkhome13
    with dissolve

    sa "Yeah...she definitely would..."
    sa "I’m pretty sure...that might be what she’s trying to do..."
    sa "It would be nice if...she picked someone I didn’t know, though..."

    if bonus == True:
        s "First, you say I’m old. Now, you’re saying you wouldn’t want me as a father?"

    s "Sana, do you actually hate me?"

    if bonus == False:
        s "I know it's kind of random, but I am very sensitive and worried about what everyone thinks of me at all times."

    sa "What? No...of course not..."

    if bonus == False:
        sa "You're kind of like the weird dad I never wanted...but also not really?..."
        s "Okay. That is fine."

    sa "I just...can’t really ever think of you as...being that kind of person to me..."
    sa "But...then again...it’s not like I really...understand what that kind of person would feel like in the first place..."

    scene barwalkhome14
    with dissolve

    sa "You’re actually...kind of the closest thing I’ve ever had to...someone like that, Sensei."
    s "Already? I feel like we still barely even know each other."
    sa "Y...yeah...I know that..."
    sa "But all I really know about my dad is...what I’ve heard from my mom..."
    sa "And I think you’ve realized by now, but...she doesn’t really open up a lot..."
    s "Well, what kind of things {i}has{/i} she told you?"

    scene barwalkhome15
    with dissolve

    sa "Do you want...the good things or the bad things?..."
    s "Just a general synopsis would be fine, I guess."
    sa "Then..."
    sa "He wasn’t very loyal..."

    if bonus == True:
        sa "My mom has always been...kind of naive...and I think he was stringing her along..."
        sa "She said he always seemed nice to her in[school], but...he was also a lot older than her, so...he was probably just...good at manipulating her..."
        sa "It wasn’t until after I was born that...she found out he’d been seeing other girls..."
        s "I see."
    else:
        sa "He...never stood on the payload..."

    "And of course her father is the mirror image of me. Great."
    "I’m sure there’s no way that’s going to bite me in the ass eventually."

    sa "So...when I say you’re the closest thing I’ve had to someone like that...it’s not because I think we’re close yet..."
    sa "There’s just...not any competition..."
    sa "You win by default..."
    s "..."
    s "So, Sara really raised you by herself then, huh?"

    scene barwalkhome16
    with dissolve

    sa "Yeah but...not just me...My brother, too."
    sa "She raised both of us all by herself..."
    sa "It was probably...really hard..."
    sa "That’s why...I don’t like trying to get her to talk about the past..."

    scene barwalkhome13
    with dissolve

    sa "And when I brought up something that reminded her of my brother the other night..."
    sa "It made me feel like it was my fault she...started to break down..."
    s "I had a feeling it was something like that."
    sa "I had a feeling that...you had a feeling about that..."
    sa "I’m sorry for not saying goodbye, by the way..."
    sa "I just...don’t normally see my mom like that and...I needed to make sure she didn’t get any worse..."
    sa "It was my fault for bringing something nostalgic up anyway..."
    s "I don’t think you should blame yourself for that. Avoiding the past is impossible."

    scene barwalkhome17
    with dissolve

    sa "No...it’s really not..."
    sa "If there’s anything I’ve learned from my mom, it’s that...denial can be a really good tool sometimes..."
    sa "It’s hard for me since...I loved my brother a lot, but..."
    sa "Can you imagine how much harder it was for her?..."
    sa "She...made him...and watched him grow up..."
    sa "Which of these two things sounds easier, Sensei?..."
    sa "Learning to cope with...the person you love more than anything in the world suddenly going away-"
    sa "Or just...ignoring that it ever happened."
    s "The second one sounds easier, absolutely."
    sa "Right...so-"
    s "Something being easy doesn’t mean it’s the right thing to do, though."

    scene barwalkhome18
    with dissolve

    sa "Huh? What do you mean?"
    s "I mean that bottling things like that up can literally kill people."
    sa "But...so can grief."
    sa "No matter what we do, we’re going to...keep hurting."
    sa "A third of our family was taken away from us..."
    sa "All we can do is...help each other deal with that any way we can..."
    s "..."

    if sarasex == True:
        s "Didn’t you tell me when you were drunk that you wished Sara {i}would{/i} talk about it, though?"

        scene barwalkhome19
        with dissolve

        sa "..."
        sa "Things you do or say when...you’re drunk...don’t count..."
        s "That’s an incredibly dangerous thing for someone working in a bar to be saying."
        sa "Yes, but...it’s something I need to think or...everything will get even worse than it already is..."
        s "..."
        sa "..."

    scene barwalkhome20
    with dissolve

    sa "Oh no! I...I made this a really awkward walk all of a sudden!"
    sa "Wh-what were we talking about at first?"
    s "How I’m the closest you’ve ever had to a father figure."
    sa "Th-that’s awkward, too! Wh-wh-what was our last {i}normal{/i} conversation about? Let’s go back to that!"
    s "I think that was just about how tall I am."
    sa "So tall! The tallest!"
    s "Sana, calm down. It’s okay that things got awkward for a few minutes."
    s "If you’re embarrassed about it, just look at it as another exercise in public speaking."
    s "You were able to talk at length about something that makes you uncomfortable, and now I know more about you as a result."

    scene barwalkhome21
    with dissolve

    sa "Uh...uh-huh..."
    sa "But now it will probably be a little bit harder for me to...spend time with you when you could just...go hang out with Ayane instead and...avoid my awkwardness..."
    sa "At least when...she compares you to a dad, she...knows what she’s talking about..."
    s "Good point."

    if bonus == True:
        s "Maybe I should just adopt the two of you and get it over with?"
        sa "I think you’d...have to marry my mom to be able to adopt me..."
        s "I feel like there are several people who would be very unhappy with me if that were to happen."
        sa "And...one of them is right next to you..."
        sa "But it’s okay..."
        sa "Like I said...I don’t view you that way..."

    sa "I’m...perfectly fine if things just...stay like this..."
    sa "That would be...the easiest thing for everyone..."
    s "..."
    sa "..."
    s "You’re really fine with things never changing?"

    scene barwalkhome22
    with dissolve

    sa "..."
    sa "Actually..."
    sa "When I say this would be the easiest thing for everyone...I really just mean me..."
    sa "If you get any closer to Ayane...you’ll get further away from me."
    sa "If you get any closer to my mom...you’ll get further away from me."
    sa "And if..."
    sa "You get any closer to me..."
    s "..."
    sa "..."

    "Sana never finishes that thought but, through context clues and my unparalleled wisdom in the world of [teenage]girls, I’m able to ascertain what she means."
    "She’s afraid of her feelings for me growing."
    "{s}Growing like a tree.{/s}"
    "She’s afraid of what she’ll have to do and what she’ll have to go through if she, too, falls victim to my suspicious gravitational pull on all of these girls."
    "Take Ayane, Sara, and me and arrange us so we form a triangle."
    "Right now, Sana is in the middle of the triangle- and she wants to get out."
    "The only way to do that is by breaking one of the lines."
    "Breaking a line means the triangle would crumble."
    "So, just like her mother-"
    "She doesn’t try to change anything."
    "She stays exactly where she is and waits for everything else to resolve on its own."
    "It’s a horrible way to live."
    "A horrible, impassive way to live-"
    "That I, too, am guilty of in more ways than one."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar40 = True
    stop music fadeout 100.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."
    "{i}A short while later...{/i}"

    jump sanadorm40

label bar45:
    scene sanayukitrain1
    with dissolve
    play music "calmbar.mp3"

    "I decide to spend the night hanging out at the bar with Sana."

    sa "You...didn’t really pick the best night to...hang out here..."

    scene black
    with dissolve

    "I go home because Sana hates me."

    scene sanayukitrain1
    with dissolve

    s "Sana, I don’t really think you should be picking and choosing your customers when your mother’s store is about to go under."
    sa "I...don’t really have much to pick and choose from either way..."
    sa "I just meant that...I might be a little busier than normal tonight..."
    s "Oh? Did someone accidentally book a birthday party here thinking it was some other bar?"

    scene sanayukitrain2
    with dissolve

    sa "Um...no..."
    sa "It’s just that...our new employee is here tonight and...I have to show her how to make drinks..."
    s "How many customers do you actually have to make drinks for? "
    s "Because the friendly neighborhood lesbian couple and myself are the only people who seem to come here and all three of us just get beer."
    sa "Well...we don’t really...ever make them, but...it’s an important thing for a bartender to know..."
    s "Well, good luck. I can’t imagine your new employee is very easy to train."
    yu "Hey. You talkin’ shit over there?"

    scene sanayukitrain3
    with fade

    s "Please don’t hit me."
    yu "You think I’d actually hit you while I'm workin’?"
    s "No. But I’m afraid you’d follow me home and beat me up on the way there."

    scene sanayukitrain4
    with dissolve

    yu "Hah...not worth the effort..."
    yu "Just havin’ a job is tiring enough. "
    sa "Yuki...you’ve only been working for...half an hour..."
    yu "Jesus, is that all? I feel like I’ve been here all night."
    yu "No wonder Yumi started her own business. "
    s "Again, she..."
    s "Ah, fuck it. Sure. "

    "I resign myself to the concept of Yumi Yamaguchi being a successful entrepreneur and allow Yuki to believe whatever it is her shriveled heart desires."

    scene sanayukitrain5
    with fade

    yu "So, now what? What’s step two in becoming a successful barmaid or whatever?"
    sa "Um...well...you can start by...taking Sensei’s order..."

    scene sanayukitrain6
    with dissolve

    yu "Cool. What do you want?"
    sa "Sensei...for the sake of...Yuki’s training...can you order something different from what you usually order?..."
    s "Uhhhh..."
    s "I’ll take...a Manhattan?"
    yu "A Manhattan? Are you a fucking prissy boy?"
    yu "There’s a perfectly good beer in front of you. Drink that."

    scene sanayukitrain7
    with dissolve

    sa "Y...Yuki! You can’t...talk to customers that way!"
    yu "Really?"
    yu "But I thought your mom said to play up my “rough exterior” or whatever it is she thought would bring new people in."
    sa "It’s okay to be mean to Sensei normally-"
    s "Wait, it is?"
    sa "But for right now...you have to look at Sensei like...not Sensei...and...and treat him like a normal person..."

    scene sanayukitrain8
    with dissolve

    yu "You want me to treat {i}this guy{/i} like a normal customer? Dude’s far from normal if he’s comin’ here to chat with a four foot tall [teenager]."
    s "I take great offense to this entire exchange. I just want to drink."
    s "Where is Sara? I need to speak to the owner."
    sa "She’s...in the urban district, passing out fliers right now..."

    scene sanayukitrain9
    with dissolve

    sa "Also...I’m...almost five feet tall..."
    yu "Same shit. "
    yu "But if we’ve gotta do this the normal way...what are you drinking, bud?"
    s "Bud?"
    yu "What're you ordering, pal?"
    s "Why do I need a weird nickname?"
    yu "What’re you havin’, champ?"
    s "How about “master” or “my prince?”"
    yu "How about you suck my fucking dick and order your stupid ass Manhattan already?"

    scene sanayukitrain10
    with dissolve

    s "Well, when you put it that way- one Manhattan, please."
    sa "Hah...this is...proving to be even harder than I thought it would be..."
    yu "Comin’ right up."

    scene sanayukitrain11
    with dissolve

    yu "So, now what?"
    yu "You’re the genius bartender girl and I don’t have any idea what the fuck goes into a Manhattan."
    sa "Well...the ingredients for a Manhattan are...bourbon...orange and Angostura bitters...and...um...sweet vermouth..."
    s "I love sweet vermouth."
    sa "And...it’s...garnished with a brandied cherry on top..."

    scene sanayukitrain12
    with dissolve

    sa "So...um...you’ll want to add the bourbon, vermouth and bitters to a mixing glass with ice and...stir it until it’s chilled..."
    sa "Then you just...strain it into a glass and...add the garnish..."
    sa "And then it’s done..."
    yu "Got it. Now, where can I find all that stuff?"
    sa "We...um..."
    sa "We...don’t have any in stock right now..."
    yu "..."
    sa "..."
    yu "Your mom's gonna need a lot of fuckin' fliers."

    scene black
    with dissolve2

    "Sana goes over the ingredients to a bunch of popular cocktails that the bar is currently incapable of making and I imagine that Yuki forgets all of them instantaneously."
    "I’m a little surprised to see that Sana has everything memorized, though. Especially when no one ever orders anything like that here."
    "But I guess things haven’t always been like that at the bar."
    "If I’m remembering correctly, the place has been in Sana and Sara’s family for a while now and was actually relatively popular before the space war."
    "It kind of sucks that everything went downhill after that, but...maybe there really {i}is{/i} a chance for them to turn things around?"
    "Though...I imagine that will be pretty hard without actual ingredients."
    "Anyway, Sana winds up sending Yuki home after another hour of training and pulls a few bills out of their register to pay her for the night."

    if bonus == True:
        "I notice that it’s nowhere near the amount that she’s likely owed, but...I don’t think Yuki’s really in the position to ask for more with zero work experience in her late thirties."
    else:
        "I notice that it’s nowhere near the amount that she’s likely owed, but...I don’t think Yuki’s really in the position to ask for more with zero work experience."

    "I also doubt that she’s even familiar with what minimum wage is."
    "But regardless, she accepts the money and exits the bar...leaving Sana and I alone once again."
    "........."
    "......"
    "..."

    scene sanayukitrain13
    with dissolve2

    sa "I...um...I’m sorry you...couldn’t get the Manhattan you ordered..."
    s "I never would have ordered that if I wasn’t asked to order something...fancier."
    s "Frankly, I didn’t even remember what a Manhattan was. It’s just the first cocktail that came to mind."
    s "Also, you should probably restock the bar some day."

    scene sanayukitrain14
    with dissolve

    sa "I agree...and...so does my mom..."
    sa "There just...hasn’t really been any reason to with our current...clientele."
    s "Is Sara really passing out fliers in the urban district right now? "

    scene sanayukitrain15
    with dissolve

    sa "Mhm. It’s the first time in a while that I’ve seen her go out of her way to try and bring people in."
    sa "So...I’m doing my part and training our new employee while she’s out doing that."
    s "Speaking of which, you handled Yuki surprisingly well."
    s "I figured that she was the exact type of person who’d cause you to cower in fear by simply looking at her."

    scene sanayukitrain16
    with dissolve

    sa "If she was in her normal clothes...I probably would have been a lot more scared..."
    sa "It was just a little easier since...we were dressed in pretty much the same outfit..."
    sa "And...I think it’s also because...I might...kind of be getting used to people now..."
    s "Well you’ve certainly increased your friend count by a sizable margin."

    scene sanayukitrain17
    with dissolve

    sa "Heheh...yeah..."
    sa "I was...even able to sleep over your house without Ayane recently..."
    s "Yeah. I was kind of surprised about that-"

    "Wait..."
    "I thought the last reset made it so that sleepover never happened?"
    "At least that’s what Ayane said and...Sana {i}was{/i} at the dorm when I got back from the rooftop."

    s "..."
    sa "..."

    scene sanayukitrain18
    with dissolve

    sa "Um...Sensei?..."
    sa "Is...there a reason you’re just...staring at me?"
    s "When did you sleep over my house without Ayane?"

    scene sanayukitrain19
    with dissolve

    sa "Um...it was...recently, wasn’t it?"
    s "For me, yes. But Ayane was under the impression that it never even happened."
    sa "That’s...weird. I could have sworn I talked to her about it..."
    sa "And I...still remember the dinner that...Tsuneyo made for us..."
    sa "But...um..."
    sa "There’s...something else I kind of wanted to say as long as we’re done talking about that..."
    s "..."
    sa "..."
    sa "Is that...okay?"

    scene sanayukitrain20
    with dissolve

    s "Yeah."
    s "Sorry for getting distracted. Time is just kind of weird sometimes."
    sa "Yeah..."
    sa "It’s crazy how...quickly it can go by when you stop paying attention..."
    sa "But...the time we’ve spent together...if anything...has seemed kind of slow for me..."
    sa "Which is weird because...it also feels like so much has happened..."
    sa "And if it weren’t for you, I...probably wouldn’t be able to do stuff like...train really intimidating employees or...sleep places I’ve never slept before."
    s "Congratulations on the character growth."
    sa "Hehe...that’s a good way of putting it..."
    sa "My mom...didn’t put any of my stat points into speech, so...I’ve been kind of...soft locked progression-wise for a little while."
    sa "But...now I’ve got...another party member who...can help me train in that field..."
    s "I think you’ve been spending a little too much time with Molly."

    scene sanayukitrain21
    with dissolve

    sa "Probably...but...spending time with other people isn’t really always a bad thing..."
    sa "I know that now."
    sa "Not that I...ever thought it {i}was{/i} bad. It just seemed kind of hard."
    s "Well, you still have the rest of the class to work up to befriending. And I want to warn you now that if you think getting closer to Yuki will help win over Yumi, it most certainly will not."

    scene sanayukitrain22
    with dissolve

    sa "Yeah...I already heard about that..."
    sa "Yumi is...not really near the top of my...potential friends list right now..."
    sa "She’s still...really scary..."
    sa "But..."
    sa "I don’t think it’s impossible anymore."
    sa "In fact...I’m starting to think that there isn’t really anything that’s impossible."
    sa "I don’t know how you did it, but...you kind of just walked into my life and opened up a bunch of doors that I...didn’t think I’d ever be able to open."
    s "Were the handles too high up?"

    scene sanayukitrain23
    with dissolve

    sa "Is everyone going to pick on my size tonight or something?"
    s "Hey. I, for one, appreciate how small you are."

    if bonus == True:
        s "I want you to stay this size forever."

    scene sanayukitrain24
    with dissolve

    if bonus == True:
        sa "You do?"
        sa "Why?"
        s "..."
        sa "..."
    else:
        sa "Is it because you are raising a horse that you require a jockey for?"
        s "..."
        sa "That's it, isn't it"

    scene sanayukitrain25
    with dissolve

    if bonus == True:
        s "No reason."
    else:
        s "Nope."

    sa "I...highly doubt that...but I’m going to...go ahead and assume you're just joking..."
    sa "I might be growing as a person, but...I also think I shouldn't really count on growing any more as a {i}person.{/i}"
    sa "My mom is...really small for her age, too...so I doubt I have many inches left."

    if bonus == True:
        s "Don’t worry. I’ll let you borrow several of mine as soon as you’re ready."
        sa "I...don’t really think that’s how height works..."

        "Even if Sana does wind up growing a little more, I hope her level of wholesomeness stays about the same."
        "I don’t want to think about a time where I can say things like that and have her immediately comprehend the unreal amount of ulterior motives I have."
    else:
        s "Don't give up, Sana. You will one day be a giant."
        sa "I hope so..."

    s "Anyway, I’m proud of you or whatever."

    scene sanayukitrain26
    with dissolve

    sa "Or whatever?..."
    s "Fine. I’m proud of you, okay?"
    s "I thought it would take a lot longer for you to stop acting like a scared little bunny rabbit- and that you’d wind up leaning on me a little more than you actually had to."
    sa "That’s funny, cause...all this time...I felt like I might have been leaning on you a little too much..."
    sa "Ayane, too."
    sa "Both of you believed in me when...I had trouble believing in myself..."

    scene sanayukitrain27
    with dissolve

    sa "And I...don’t want to agree that I’m a...bunny or anything..."
    sa "But I’d like it if...I could still maybe...lean on you a little bit once I start having to...do harder things..."
    sa "Like...ordering food over the phone or...making a withdrawal at the bank..."
    s "Just use an ATM. No one actually goes inside of banks anymore unless it’s something really important."

    scene sanayukitrain28
    with dissolve

    sa "It was just an example, Sensei."
    sa "What I mean is that...just because I’m doing a little better doesn’t mean I don’t still need you."
    s "Well, thanks. But, just to remind you, I’m a highly sought after individual and it might not always be as easy as this to get my attention."
    sa "Is that...the next phase of my training? Having to...force you to spend time with me so others can’t?"
    s "Maybe not the {i}next{/i} step, but it feels like that one is definitely on the way to whatever your final goal may be."
    sa "I need a final goal? I can’t just...enjoy my time with you and everyone else?"
    s "Sure you can."
    s "I just don’t think complacency is really as fulfilling as you’re making it sound."
    sa "But...isn’t that exactly how you live {i}your{/i} life, Sensei?"
    sa "I thought you just...wanted things to stay the way they are now..."
    sa "Or..."
    sa "Or do you maybe...have something you actually want?..."
    s "..."
    sa "..."

    scene black
    with dissolve2

    "The two of us sit there in silence for a little while longer as I attempt to think of all of the things I want."
    "Within a matter of moments, I find myself stranded on a desert island filled with blurry thoughts and the idea that there {i}are{/i} things that I want."
    "So many of them that I feel surrounded."
    "But they lurk in the shadows of large trees-"
    "And I can’t make out what they look like."
    "So I decide they aren’t there at all."
    "And I go to sleep in a shelter someone else built and abandoned."
    "I leave the bar."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar45 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar50:
    scene funnydildoscene1
    with dissolve
    play music "calmbar.mp3"

    "I make my way over to the bar to hang out with Sana for a bit."
    "She’s cleaning off the counter when I arrive...which, thanks to my above average deductive reasoning, I know means there were likely {i}real{/i} customers tonight."
    "Could it be that handing out a few fliers and hiring an ex Yakuza wife actually increased business somehow?"

    s "You certainly look happy tonight."
    sa "Do I?"
    s "Unless you’re smiling for no apparent reason. "
    s "If that's the case, allow me to change that last sentence to, “You certainly look menacing tonight.”"

    scene funnydildoscene2
    with dissolve

    sa "I...think happy is closer to the right answer."
    s "But not {i}entirely{/i} the right answer."

    scene funnydildoscene3
    with dissolve

    sa "I think that maybe...relieved is the word you’re looking for."
    sa "It’s been a while since we had actual customers."
    sa "Even those two old ladies who used to hang out in the back of the room stopped showing up a while ago."

    scene funnydildoscene1
    with dissolve

    sa "But...tonight, we had a handful of people that I’ve never even seen before."
    s "And how many of them ordered drinks that you didn’t have the ingredients for?"
    sa "..."

    scene funnydildoscene4
    with dissolve

    sa "Um..."
    sa "All of them..."

    scene funnydildoscene1
    with dissolve

    sa "But...they were understanding when I told them we could only serve beer and wine for the night."
    sa "And...now I guess I have...more ammunition in...getting my mom to order actual liquor."
    s "Does Sara even have the money to get actual liquor?"
    sar "Does Sara what now?"

    scene funnydildoscene5
    with fade

    "Sara and Yuki come out of the back room and make their way over to Sana and me."
    "Sara stands defiantly behind the counter and Yuki-"
    "Well...Yuki just stands, I guess."

    yu "Yo."
    sar "Good evening, Sensei. "
    sar "Now, what were you saying about having enough money to buy {i}actual{/i} liquor?"
    s "Oh. I was just asking if you had enough money to buy actual liquor."
    yu "Reasonable question."

    scene funnydildoscene6
    with dissolve

    sar "Hmph."
    sar "I do recall a time where that may have been a worry of mine."
    sar "But I’ll have you know that the one and only Sakaki-Bar-A is back on top."
    s "Please tell me the name of this place isn’t actually the “Sakaki-Bar-A.”"

    scene funnydildoscene7
    with dissolve

    sar "Wait, you really didn’t know that?"
    sar "You’ve been coming here for how long now?"
    s "Good question, Sara. Why don't you answer it for me?"

    scene funnydildoscene8
    with dissolve

    sa "Um...I know we...had a good night, but...I don’t think we should let {i}one{/i} good night go to our heads..."
    sa "We...still have a lot of work to do..."
    sar "I know, I know. "
    sar "But, since all three of us did wonderfully tonight, I was thinking that maybe we could all go out for a little celebration."
    s "Okay. Guess I’ll just go fuck myself then."

    scene funnydildoscene9
    with dissolve

    sar "Okay, the {i}four{/i} of us can go out for a little celebration."
    s "Is that really the best course of action?"
    sar "Why wouldn’t it be?"
    s "I mean, I take it that you finally generated some sort of profit tonight. It would be a bit of a shame to just blow that all on a post work celebration, wouldn’t it?"
    sa "Sensei is...actually giving good advice for a change..."
    s "Hey, what happened to all of that stuff about how I helped you face your fear of people and pasta?"

    scene funnydildoscene10
    with dissolve

    sa "Guh..."
    sar "It’s not like I was planning on going out to some fancy restaurant or anything..."
    sar "Yuki told me about some place she normally goes to in the old district, so I was thinking that maybe we could all grab dinner there before heading home."
    s "Tojo Ramen?"
    yu "You know it."

    scene funnydildoscene11
    with dissolve

    sa "The old district is...a little too far for me, I think..."
    sa "I’m...kind of tired from working all night and...I don’t even think the buses are running right now..."

    scene funnydildoscene12
    with dissolve

    sar "But we were all gonna ride on Yuki’s motorcycle together and it was gonna be fuuuuun..."
    sa "I...don’t even know if that’s legal?..."
    yu "It’s not, but no one’s gonna fuckin’ care."
    s "And I’m assuming I’d just be walking."

    scene funnydildoscene13
    with dissolve

    sar "Of course not! You’d be riding with us!"
    s "Four people on one motorcycle? I’ll pass."
    yu "You passed when it was just two as well, ya fuckin' pussy."
    s "Yuki, come on. Not in front of one of my students."
    sa "It’s okay, Sensei...I’m...a little afraid of motorcycles as well..."
    s "I’m not-"
    sar "Yeah, yeah. We all know how brave and strong you are."
    s "Sara, not you too. You’re supposed to always be on my side."

    scene funnydildoscene14
    with dissolve

    sar "Put a ring on it and maybe I will be~"
    sa "..."
    s "Pass."

    scene funnydildoscene15
    with dissolve

    sar "At least hesitate a little, jerk!"
    yu "Brutal."
    sa "Um...if Sensei and I...both don’t really want to go..."
    sa "I guess we could stay here and...close up..."
    s "As long as I don’t have to actually do anything."
    sa "I’ve...already handled most of it, so..."

    scene funnydildoscene16
    with dissolve

    sar "You’re really sure you don’t want to come, Sana?"
    sar "It’s been a while since the two of us have gone out to dinner together."
    sa "We could always go another time. I just...don’t really want to right now..."
    sar "If...that’s what you really want...okay..."

    scene funnydildoscene17
    with dissolve

    sar "I’m leaving her in your hands then, got it?"

    if bonus == True:
        sar "It will be good practice for when you decide to settle down with me and become Sana’s new daddy."
        s "I really wish all of you mothers would stop trying to get me to be your daughter’s new father."
    else:
        s "Leave her in Yuki's hands. She is in a gang that kills people."

    scene funnydildoscene18
    with dissolve

    if bonus == True:
        yu "Yo! Don’t fuckin’ lump me in with that shit. I ain’t ever asked for that."
    else:
        yu "Yo! Don’t fuckin’ lump me in with that shit. I ain’t ever killed anybody!"

    s "Not {i}yet{/i} you haven’t."
    yu "Ain’t gonna fuckin’ happen, man. Quit while you’re ahead."
    s "How am I-"
    sar "As much as I’d love to hang around and listen to you two “not flirt” with each other, I’d also love to eat before it’s time for me to pass out for the night."

    scene funnydildoscene19
    with dissolve

    yu "You good to go then?"
    yu "Should probably put on a jacket if you don’t wanna get cold. Body heat’s not good for shit when you’ve got the wind blowin’ right at you."
    sar "It’s near the door. I’m ready whenever."

    scene funnydildoscene20
    with dissolve

    sar "Be good."
    sa "Uhh...okay?"
    yu "Night, man. See you around or whatever."

    scene funnydildoscene21
    with dissolve

    "Sara and Yuki make their way out of the store, leaving Sana and me alone in the bar for what I imagine is the millionth time."
    "Tonight feels a little different, though."
    "For one, it’s the first time I’ve ever had to watch her really clean anything."
    "But not only that, we’re still coming off of a relatively awkward and uncomfortable exchange about her brother that I really hope doesn’t come up again any time soon."

    scene funnydildoscene22
    with dissolve

    sa "So...I guess it’s just us again..."
    s "I guess it is."
    s "What else do you have to do before we can get out of here?"
    sa "Are we...going somewhere?"
    sa "Because I wasn’t really lying about being tired..."
    s "Well, if you’re closing, there’s not really any point in hanging around, is there?"
    s "I figured I’d just walk you back to the dorm or something like-"

    "I inadvertently pause when I remember an important detail about the thing I literally {i}just{/i} thought about {i}not{/i} thinking about."
    "If her brother was killed while walking home, is something like that some sort of trigger for her?"
    "Is the sheer idea of walking home enough to evoke the same negative memories a lock of hair can?"
    "These are the things I’m forced to think about for her sake now."
    "All because she wanted to make something of hers mine."

    sa "...Sensei?"
    s "Oh, sorry."
    s "I just figured we’d walk back to the dorm or something."

    "It wouldn’t be the first time anyway."
    "I’m likely just overthinking things at this point."

    scene funnydildoscene23
    with dissolve

    sa "Sure..."
    sa "I’m just going to run up to my mom’s room to grab a few DVDs before we leave..."
    sa "Ayane’s been looking for a lot of...lighthearted romantic comedies lately and...I’m pretty sure my mom has a ton of those..."
    s "Don’t you need to finish cleaning first?"
    sa "I think it’s...clean enough, right?"
    sa "It’s not like we were...{i}extremely{/i} busy..."
    sa "Just...busier than normal..."
    s "Hey, you’re the employee. I’m just some guy who hangs out here and talks to you every once in a while."

    scene funnydildoscene24
    with dissolve

    sa "Then...in that case...wait here."
    sa "I’ll be right back."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Sana tosses the rag she’d been using to wipe down the counter into a large blue bin and quietly makes her way up the stairs."
    "I scan the room to see if maybe she missed a chair to push in or something like that. "
    "I don’t really know how nice this place is supposed to look when it closes."
    "And it’s not like I’d actually {i}help{/i} either since I’m not being paid."
    "But I could at least tell her about it when she comes back..."
    "........."
    "......"
    "..."
    "{i}Ten minutes later...{/i}"

    scene barnight
    with dissolve2

    s "..."

    "Sana still hasn’t come downstairs."
    "I was hoping things wouldn’t come to this as I am {i}also{/i} tired and really don’t want to summon the energy to go up there."
    "But I guess a real concern with her is that if a dresser fell down or something like that, she could be stuck beneath it for life."
    "I will save you, Sana."
    "Granted, I probably would have heard something if a dresser fell down or..."

    s "..."

    "Ugh."
    "Fuck it."
    "I sigh to myself and tap into my energy reserves and head for the stairs."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    if bonus == True:
        jump funnydildox
    else:
        "I go upstairs and Sana yells at me for not thinking she would be able to defeat a dresser in melee combat."
        "It is a very intense situation for the two of us and she cries a lot because of all of the dressers that have previously defeated her."
        "I think it is dumb that she would yell at me for her own weakness and tell her that her mom could probably defeat one."
        "Sana hates that even more and forces me to go home."
        "Dang it."

        $ renpy.end_replay()
        $ sana_love += 1
        $ bar50 = True
        stop music fadeout 5.0

        "{i}Sana’s affection has increased to [sana_love]!{/i}"
        "{i}Sana has defeated a dresser!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label bar55:
    scene sanakaoribar1
    with fade
    play music "calmbar.mp3"

    "I make my way over to the bar (The regular one, not the second bar that I secretly visit on Fridays now) and find that, for some reason, Kaori is working here again."
    "I’m not sure why, considering that today is, at least to my knowledge, not a special occasion or holiday.  But I’m also not about to put any amount of thought into why Kaori does...well, anything."
    "Instead, I’ll just focus on the small girl beside her."

    k "Welcome once again, Friendburger! The special dizzy drink of the day is-"
    s "Hey, Sana. Working alone again tonight?"
    sa "So far...not really..."
    sa "Kaori keeps helping the customers before I...even have a chance to..."
    s "Kaori? Is she here right now?"

    scene sanakaoribar2
    with dissolve

    k "Do not give into the foul temptations of your sight balls’ endless longing for the dark! The Queen of Spiders stands before you! In the same place as always!"
    s "Always? You’ve worked here like three times."

    scene sanakaoribar3
    with dissolve

    k "So you {i}can{/i} see. "
    k "That was not a very funny human joke, Friend. Invisibility is a terrifying sickness that comes to claim us all one day. I was worried my time may have expired for a sixtieth of a minute."
    sa "That...would be called a “second...”"
    s "Thank you, Sana- for taking up my role as Kaori’s unofficial human tutor. It feels like just yesterday that I was coming here to teach {i}you{/i} how to be human."

    scene sanakaoribar4
    with dissolve

    sa "Is that...why you were coming here? It wasn’t...to teach me how to be more...umm...confident when it comes to...speaking?"
    k "If you want my human opinion, I think your speaking is nice. Your voice reminds me of glass and the color periwinkle."
    s "Confidence...humanity...they’re kind of interchangeable at this point, I think. That’s why it’s okay for people like Kaori to breathe the same air as us. "
    s "She never makes any sense, but her confidence in the act of {i}making{/i} no sense helps her blend in pretty well."
    s "On the other end of the spectrum, you have zero confidence, but are also one of the most unremarkable and exceedingly average human beings I have ever encountered."
    s "You don’t have to blend in at all since you’re already a part of the background. "
    s "So I guess that, in a sense, my job here is done. You’re as human as you’ll ever be."

    scene sanakaoribar5
    with dissolve

    sa "Un...remarkable?..."
    sa "Exceedingly...average?..."
    sa "Are you...calling me...boring?..."
    s "Yes."

    scene sanakaoribar6
    with dissolve

    sa "W...Why?! Did you come here just to...hurt me?!"
    s "Hey, being boring isn’t bad. I like being with you because it’s relaxing and I never have to worry about you drugging me or threatening to tie me up and do things to my body."
    sa "Who are you spending your time with that makes you worry about those things?!"
    s "Pretty much everyone. Which is why I like you. It’s a nice change of pace."

    scene sanakaoribar7
    with dissolve

    sa "This is the strangest...compliment I’ve ever received..."
    k "And you say that I am bad at human conversation, Friend. Can you not see that you are making the tiny human uncomfortable?"
    sa "I’m not...uncomfortable...I..."
    sa "I think I am...offended..."
    s "Offended? "

    scene sanakaoribar8
    with dissolve

    sa "Y...Yes."
    sa "You made me mad...and..."
    sa "And for that...you will pay."
    s "..."
    sa "..."

    scene sanakaoribar9
    with dissolve

    sa "Hah...I tried...being intimidating to...change things up, but...I...just sounded stupid...didn’t I?"
    k "You did not sound like yourself. The mini Sara spawn that I know of is never intimidating. Like a tiny gerbil but with marshmallows for teeth and only one eyeball."
    sa "I’ll just accept that...my test of “humanity” is finally complete and...that Sensei has no use for me anymore..."
    s "To be completely honest, though...you have improved a lot. In terms of speaking, I mean. Which I will now clarify as the {i}actual{/i} purpose of all of these visits."
    s "And in a sense...I think your test {i}is{/i} complete. But that doesn’t mean I don’t have any more use for you."

    scene sanakaoribar10
    with dissolve

    sa "C...Complete?..."
    sa "But I still..."
    sa "Keep...pausing...in the middle of...sentences..."
    s "Yeah, but I think that just might be how you talk. When you look at the amount you’ve {i}accomplished{/i} since we’ve met one another, it’s a lot more than most."
    s "You’ve made a bunch of friends...you can stand next to Kaori without getting scared...Hell, you’ve even joined the light music club. "
    s "That’s a lot, Sana. I’m really proud of-"
    sar "Light music club?! "

    scene sanakaoribar11
    with fade

    sar "Since when are you in the light music club?! Since when are you in any club at all?! Why didn’t you tell me?!"
    sa "I didn’t tell you b...because I knew you would...act like this..."
    sar "Like what?! Excited that my little girl is finally finding her place in the world?!"
    sa "Um...yes?..."

    scene sanakaoribar12
    with dissolve

    sar "Why have you been hiding my daughter’s character growth from me?"
    s "Why is it up to me to relay her growth to you?"
    sa "Why are we...still talking about {i}me?...{/i}I would like to...go back to being...unremarkable now..."

    scene sanakaoribar13
    with dissolve

    sar "Absolutely not! You are {i}my{/i} daughter and the world will know of your adorableness! I don’t care if I have to burn down all of Kumon-mi to show them."
    sa "Please don’t...burn down the city for me...This summer is already...hot enough..."

    scene sanakaoribar14
    with dissolve

    yu "Sara, I get that you like your daughter and that’s totally chill. But I ain’t afraid of kickin’ your ass if you burn down both my job and apartment. I ain’t goin’ back to the streets, you hear me?"
    sar "Shut up. If you can be proud of your daughter for putting some girl into a coma, I can be proud of my baby for becoming a rock star. "
    sa "M...Mom! I...don’t even know how to...play anything yet..."

    scene sanakaoribar15
    with dissolve

    sar "{i}Yet!{/i} Which means you {i}will!{/i} And I don’t care if I have to burn down all of Kumon-mi to ensure that!"
    s "Where did this sudden fascination with arson come from? "
    sar "From the burning love I feel for my mini Sara spawn."
    sa "I have a name! And can we stop talking about me now?!"

    scene sanakaoribar16
    with fade

    "Sara decides to give her daughter a break and retreats to the corner of the bar with Yuki after she finishes dealing with a table full of customers."
    "It’s not much being just {i}one{/i} table, but it’s more than usual for a random school night. "
    "And if Sara can afford having four people on shift at once, I think it’s safe to say things might actually be turning around for the Sakakibaras."
    "With the youngest of them managing to turn things around for herself as well, I can’t help but feel something reminiscent of what normal people would call “happiness” bubbling up inside of me."
    "But then again, I could just be lightheaded from having so many attractive girls in matching outfits standing in close proximity to me. "
    "You’d think the novelty of that would have worn off by now, but...nope. "

    k "If you do not want us to talk about you, what do you suggest we speak of, mini Sara spawn? "
    k "The lack of patrons in this establishment signals to me that this would be a good opportunity to become close to one another as I will be standing in this spot more frequently going forward."
    s "You will?"

    scene sanakaoribar17
    with dissolve

    k "The time has come for a new companion! One that I must acquire additional moneys for! And also because being around Aunt Yukiburger makes me happy!"
    sa "I’m also...going to have to spend more time with my club, so...I won’t be able to help out around here as much anymore..."
    sa "Having Kaori help is...well...it’s a lot of things...but I...think it will be for the best..."
    s "Think you’ll be able to survive a room full of loud, energetic girls playing what I assume will be loud, energetic music?"
    sa "The music...I don’t mind...but it might be...hard fitting in with everyone at first since...they’re all so cool and I’m...umm...what was it again?..."
    s "Unremarkable and exceedingly average?"

    scene sanakaoribar18
    with dissolve

    sa "R...Right..."
    k "You seem to care a lot for the mini Sara spawn, Friend. Is this what humans call love?"

    scene sanakaoribar19
    with dissolve

    sa "Wh-What?! No! Of...Of course not!"
    k "Then why is the temperature of your tiny human body steadily rising? "
    k "Size has naught to do with reaching sexual maturity, mini Sara. Not when cats are primed and ready to reproduce at only four months old!"
    sa "That’s...way too young!"
    s "Yeah, that just made me uncomfortable."

    scene sanakaoribar20
    with dissolve

    k "There is no reason to feel discomfort, Friend! Intercourse creates more fluffy animals and if you want to create more animals with the Sara spawn, I think you should! "
    s "Sana-"
    sa "No! Absolutely not! I am not...looking for a...mate!"
    s "I was just going to ask if you loved me like Kaori suggested."
    sa "I don’t even {i}like{/i} you!"
    s "Well, that’s just rude."

    scene sanakaoribar21
    with dissolve

    sa "That’s...not what I..."
    sa "Uh..."

    scene sanakaoribar22
    with dissolve

    sa "So, uhh...animals! Right?"
    k "Would you like to learn more about the rituals of mating and-"
    sa "Nope! Something...entirely unrelated to that!"
    k "Baby animals?"
    sa" Uhh...closer...but still not what I had in-"

    scene sanakaoribar23
    with dissolve

    k "What is your favorite baby animal, Friend? They are all good and there are no wrong answers. So please answer correctly!"
    s "But-"
    k "Too slow! The correct answer is the baby sea turtle!"
    k "Did you know that in a single nesting season, sea turtles can lay over one thousand eggs?!"
    k "That is so much egg! Glorious egg!"
    sa "I wonder if...Koi Cafe is hiring?..."
    s "My favorite baby animal is the lamb because all of the bad things you do in life can be forgiven by ritualistically sacrificing one."

    scene sanakaoribar24
    with dissolve

    s "Without the shedding of blood, there is no forgiveness of sin. And while sacrifices at the behest of  gods run deeper than the rivers of our ancestry, our ability to accept and embrace them does not."
    s "A long time ago, a group of men in suits showed up at my doorstep. We took them in and fed them after wiping the blood from our hands and were swiftly rewarded with eternal life."
    s "That is why I can still smile today. Why I can drink and be merry. Why I can stand before you two in my purest form. "
    s "I am eternal. All of this exists for me. "
    s "And none of it would be possible without a pile of lifeless baby sheep and blood smeared over the door of my home to attract more visitors."
    s "I can’t wait to have sex with both of you at the same time."
    sa "..."
    k "..."

    scene black
    stop music

    "INCORRECT RESPONSE PROVIDED."
    "THE EVENT WILL NOW REVERT TO ITS PREVIOUS STATE."
    "PLEASE BE ADVISED THAT THIS PROCESS IS STILL UNDERGOING TESTING AND THAT ADDITIONAL ABNORMALITIES MAY OCCUR."

    scene sanakaoribar24
    play music "calmbar.mp3"

    sa "I wonder if...Koi Cafe is-"
    s "I concur that the ideal baby animal is the sea turtle. Oh, glorious egg."

    scene sanakaoribar25
    with dissolve

    k "You did it! You got it right! Congratulations!"
    sa "I...really don’t like when you two...speak...like that..."
    s "Like what?"
    sa "Like...saying things that don’t really make sense..."
    sa "It makes me...a little uncomfortable...like...like something...weird is..."

    scene sanakaoribar26
    with dissolve

    sa "Is...going on..."
    k "There is nothing weird about the baby sea turtle, mini Sara! They are at their most adorable when they have to flip-flap flip-flap across black sandy beaches, dodging talons of predators along the way."

    scene sanakaoribar27
    with dissolve

    k "In a sense, that is what we all do every day in this human life!"
    k "We wake up and slide our fleshy motion tubes out of our soft rectangle, hoping that the giant welcome box we live in does not dissolve into the earth!"
    k "Then, we pour ourselves a deep ceramic plate of sugar squares coated in cow juice to ward off the evil as we make our way into the world itself!"
    k "But before we can leave, we have to stare back at ourselves! "
    k "Thank our organs and remember to smile! "
    k "For the moment we forget to do those things, the welcome box becomes an {i}unwelcome{/i} box."

    stop music
    play sound "static.mp3"
    scene sanakaoribar28
    with flash
    stop sound

    k "And it all decays from there."

    play sound "static.mp3"
    scene sanakaoribar29
    with flash
    stop sound
    play music "calmbar.mp3"

    yu "What are you doing?"
    sar "Who, me? Oh, you know...Just being irresponsible with my money and buying Sana a drum set as an early Christmas present."
    yu "Oh, shit. "
    yu "Here’s hoping she ain’t a piece of shit like my daughter and doesn’t toss it off a bridge."
    sar "I doubt she’ll be strong enough to lift it. Us Sakakibaras aren’t exactly known for our {i}strength.{/i}"
    yu "What {i}are{/i} you known for, then? Apart from running the least popular bar in all of Kumon-mi."

    scene sanakaoribar30
    with dissolve

    sar "Hmm..."
    yu "..."
    sar "..."

    scene sanakaoribar31
    with dissolve

    sar "Wanting to fuck our teachers?"
    yu "Dude."

    play sound "static.mp3"
    scene sanakaoribar32
    with flash
    stop sound

    s "So, Sana...you’ve made new friends...joined a club...and can now (At least partially) conquer a conversation with the single most confusing person I have ever encountered."
    s "Would it be preemptive to label today’s meeting as a graduation and finally put an end to your training arc?"
    sa "It...doesn’t feel like much of a...graduation and...and I still have a lot of improving to do, but..."
    sa "If you think...I’ll be okay...then I’ll probably be okay..."
    k "Congratulations, mini Sara. Most people do not make it to the amount of words I was able to say to you. They always run away."
    k "I will reward you by writing your name in my special notebook of friends. And, if you do not count animals, you are one of the first ten entries! "

    scene sanakaoribar33
    with dissolve

    sa "Uhh...thanks...but I...I don’t really...need a reward for...existing..."
    s "How about a drink then?"

    scene sanakaoribar34
    with dissolve

    sa "Why do all of the adults I know always encourage me to drink?..."
    k "I will not allow the mini Sara to consume the dizzy drinks on my watch. "
    k "She may have reached the age of sexual maturity, but is still far too young to partake in an activity as hellacious as the consumption of alcohol! "
    k "You may reward her with a child instead."
    sa "I...think I’m going to refuse...both of those things..."
    sa "I...talk too much when I drink and...and I want to start...talking...{i}without{/i} that..."
    s "Then...I guess it’ll just be an entirely unceremonious graduation and we’ll all go on with our lives in the exact same fashion we’ve been going about them thus far."

    scene sanakaoribar35
    with dissolve

    k "By dodging the talons of predators!"
    s "..."
    sa "..."
    sa "By..."
    sa "Dodging the talons of predators..."

    scene black
    with dissolve2

    "The three of us make a toast, but I am the only one who drinks."
    "That is, until Sara and Yuki rejoin me and the rest of the night goes by with us constantly asking Kaori for refills."
    "Sana goes home somewhere around my third or fourth beer, but I don’t see her leave."
    "Around my sixth, I begin to wonder if it has anything to do with the fact that she’s already accustomed to never saying goodbye to those she cares about."
    "Around my ninth, I think of a lamb."
    "Though, I’m not quite sure why."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar55 = True
    stop music fadeout 7.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayanesanabeach2:
    scene sanaatthebeach1
    with dissolve2
    play music "sidecharacter.mp3"

    s "Yo."
    s "Figured I’d come say hi since you’ve been all by yourself this whole time."
    sa "..."
    s "..."
    s "Sana?"

    scene sanaatthebeach2
    with dissolve

    sa "Oh...yeah. Sorry. I just..."
    sa "I wasn’t expecting you, I guess."
    sa "I figured you’d be staying with Ayane until it came time for us to leave."
    s "And I figured you would have joined us at some point, but...here we are."
    sa "Here we are..."
    s "Is this really how you wanted to spend your day? Alone under a tree while Ayane and I hung out without you?"

    scene sanaatthebeach1
    with dissolve

    sa "It beats getting killed by the sun, at least. "
    sa "Besides, I’d just be getting in the way if I came and joined you two. Even if...it was supposed to just be Ayane and me today."
    s "Uh-oh. Did I interrupt your romantic getaway with your roommate?"

    scene sanaatthebeach3
    with dissolve

    sa "Mhm. Do you really think I’d ever wear something like this for {i}you?{/i}"
    s "Crazy. All this time and I had no idea you felt that way about her. Does Ayane know?"

    scene sanaatthebeach4
    with dissolve

    sa "Of course. She’s the one who invited me after all. "
    sa "But I suppose I’ll always be second to you, Sensei. If only she and I went back as far as you two. Maybe then I’d have a real chance."

    scene sanaatthebeach5
    with dissolve

    sa "But, that aside...I’m glad the sun is finally gone. At long last, I can feel my energy returning little by little. "
    sa "Kudos to me for managing to both stay out of harm’s way {i}and{/i} give you and Ayane all of the private time you needed."
    s "Kudos to you, indeed. But there’s no need to bring up Ayane anymore when it’s time for the two of {i}us{/i} to have some “private time” now."

    scene sanaatthebeach6
    with dissolve

    sa "And what would you like to do with that “private time” I wonder?"
    s "That entirely depends on how much I am allowed to do."
    sa "I don’t remember setting any guidelines or rules for you to follow."
    s "Maybe not directly. But you’ve inadvertently set a bunch of unspoken ones throughout the brief time we’ve known one another."
    sa "Have I? "
    s "You have."
    sa "Name one. "
    s "Remember that time you passed out because I held your hand while you weren't looking?"
    sa "Doesn’t ring a bell."
    s "Or all of those times you told me you only looked at me as a teacher?"
    sa "Are you something more than that?"
    s "You tell me. I have no idea what to make of this...weird mood you’re in right now."

    scene sanaatthebeach7
    with dissolve

    sa "Weird?..."
    s "Yeah. Did that swimsuit unlock some sort of secret power or something? Because you’ve seemed a lot less...Sana than normal tonight."

    scene sanaatthebeach8
    with dissolve

    sa "I’m...the same {i}Sana{/i} as always, though."
    sa "I guess I’m just a little excited that you decided to spend time with {i}me...{/i}that’s all."
    sa "That stuff about being worried about bothering you and Ayane...it’s all I could think of over here."
    sa "I wanted to see you. I wanted to see you {i}so{/i} badly. But you belong to her and I belong to-"
    s "I don’t belong to anyone."

    scene sanaatthebeach9
    with dissolve

    sa "Then..."
    sa "Why not belong to {i}me?{/i}"
    s "I’m sorry?"
    sa "Am I not good enough?"
    sa "Am I too small?"
    sa "Is someone like Ayane or my mom better suited to your interests?"
    s "What’s...going on with you right now?"
    sa "Maybe I’ve been drinking? I was just saying the other day that I talk too much when I drink, wasn’t I?"
    s "You were...but I don’t see any alcohol laying around. "
    sa "Heat stroke, then? That makes people act all sorts of weird, doesn’t it?"
    s "It does, but..."
    sa "Why does it even matter? It’s just the two of {i}us{/i} now...so you shouldn’t be worrying about something as silly as why I’m acting the way I am if the way I’m acting is {i}good.{/i}"
    sa "Enjoy the moment, Sensei. We don’t get many of them."

    scene sanaatthebeach10
    with dissolve

    sa "Though..."
    sa "I really wish we did."
    sa "I get lonely...just like every other girl."
    sa "There are things I want. Things I want that everyone else gets to have while I sit in the background. Unremarkable and exceedingly average."
    sa "I don’t want to be average anymore. I want to be fun. Exciting. Someone like Ayane or...or Rin."
    sa "People who can talk to you without getting nervous or scared or worried or-"
    s "But that’s not you."

    scene sanaatthebeach3
    with dissolve

    sa "What do you know about who I am? "
    s "Only what you’ve taught me over the last...five or six semesters. "
    sa "I can teach you more, you know."
    sa "There are tons of things about me I’m keeping locked away. And there are only so many places I can hide the key."
    s "You’re not going to question how we’ve been together for five or six semesters despite still being a first year?"

    scene sanaatthebeach11
    with dissolve

    sa "Oh! Uhh...has it been that many already? It feels like just yesterday we were meeting one another and-"
    s "Who are you?"

    scene sanaatthebeach12
    with dissolve

    sa "Sana Sakakibara...part time bartender and full time student. Resident of...dorm number two. Ayane’s best friend. A...member of the light music club. "
    sa "A girl who...really likes you and...is having a really hard time accepting that?"
    s "..."
    sa "..."
    s "..."
    sa "..."

    scene sanaatthebeach13
    with dissolve

    sa "Oh, God damn it."

    play sound "static.mp3"
    scene colorbars with flash
    scene happy1 with flash
    scene sanaatthebeach14 with flash
    stop sound

    q "You know, you’re a real buzzkill. A girl you’ve been chasing after to no avail for [totaldays] days is finally starting to open up to you and you go and do {i}this?{/i} "
    s "You..."
    s "You’re the girl from..."
    s "From..."
    s "Where do I know you from?"

    scene sanaatthebeach15
    with dissolve

    q "I’m surprised you know me {i}at all.{/i} Those memories aren’t supposed to stick. "
    s "What memories? How do you know what is and isn’t supposed to stick? And how were you Sana just now?"
    q "So many questions. You must be {i}really{/i} confused, huh?"
    s "Can you blame me? It’s not every day someone I know transforms into someone else."

    scene sanaatthebeach16
    with dissolve

    q "Hey, hey, hey! How can you be so sure of that? That Ami girl is {i}really{/i} suspicious at times, isn’t she?"
    q "And what about Niki? A convenient childhood friend slash ex-girlfriend who’s also an idol that never gave up on you after all of those years away? Get real."
    q "There’s tons of weird stuff that happens to you."
    q "If I were you and {i}I{/i} were going to go hunting for shapeshifters, those two are where I would start. Not the short, quiet girl with unsightly habits."
    s "Unsightly habits? What are-"

    scene sanaatthebeach17
    with dissolve

    q "But enough about that! Let’s talk about my amazing impression and how awesome I am! "
    q "Hooray! Clap clap clap clap clap."
    s "I don’t want it to sound like I’m encouraging this since I’d prefer if you stayed {i}out{/i} of my students’ bodies, but...you should probably talk a little slower the next time you slip into Sana’s."

    scene sanaatthebeach18
    with dissolve

    q "First off, rude."

    scene sanaatthebeach19
    with dissolve

    q "Second, I didn’t {i}slip{/i} into anyone’s body. I’ve been me the whole time. "
    q "You saw Sana because that’s what you wanted to see. And you stopped seeing her the moment you realized you were never seeing her at all."
    q "The human mind is interesting...how it can be tricked into seeing or feeling certain things that aren’t there. "

    scene sanaatthebeach20
    with dissolve

    q "But I guess that maybe I {i}do{/i} take a little advantage of that from time to time. "
    q "It’s not every day that I get to talk to somebody, you know. Gotta seize the opportunity when the opportunity arises."
    s "Can you tell me...literally anything of value? Who you are? Why you’re here? Where Sana is?"
    q "Sana’s just a little further down the shoreline. Good luck trying to talk to her right now, though. "
    q "As for the other two questions...I’m sorry, but I can’t answer them."
    s "Why not?"
    q "Because I can’t."
    s "That’s not a very good answer."
    q "Hey, I don’t make the rules. In fact, I rarely ever even follow them. Which I guess inadvertently answers question numero dos but, in case anyone asks, that was totally off the record."
    s "Any vague hints pertaining to {i}who{/i} you are?"
    q "Wanna take a guess?"
    s "..."
    q "..."
    s "Are you..."
    s "God?..."

    scene sanaatthebeach21
    with dissolve

    q "Woohoo! You got it-"

    scene sanaatthebeach22
    with dissolve

    q "Completely and utterly wrong. Not even close. 0/10."
    s "Well, then...do you have anything to do with the weird shit going on in this world? Assuming you {i}know{/i} about the weird shit going on in this world, that is."
    q "Again, that’s not really something I can answer. But you’ve gotta say, it’d be pretty gosh darn weird if I wasn’t {i}somehow{/i} involved, right?"
    q "Showing up out of nowhere...passing as a mimic...I wager I’m probably the most suspicious person you’ve ever met."
    s "I wouldn’t say you {i}passed,{/i} by the way. Your impression was still miles off. "
    s "But I guess expecting anyone to be able to understand Sana without putting in the effort to actually get to {i}know{/i} her is just...not likely."
    q "Are you insinuating something there, buddy?"
    s "Just that it’s a little rude to make up someone’s feelings."
    q "I wasn’t making them up. I was just..."

    scene sanaatthebeach23
    with dissolve

    q "...Appropriating them?"
    q "Channeling her energy?"
    s "Are you a psychic now, too?"

    scene sanaatthebeach24
    with dissolve

    q "Nope! And I’m very thankful for that as the idea of being able to read {i}your{/i} mind gives me the heebie-jeebies."
    s "I am also thankful that you can’t read my mind right about now."
    q "Keep it in your pants, chief. I’m not that kind of character. "
    s "Even though you were only a step or two away from seducing me using Sana’s appearance?"
    q "Hey, I obviously would have backed down before it went anywhere. I just wanted to see how long I could mess with you before you snapped out of it."
    s "Snapped out of what, exactly? "

    scene clearnightsky
    with fade

    q "Another one of your thingamajigs. "
    q "You walked off to find Sana and, somewhere along the way, your mind went blank."
    q "Thankfully, I was close by when it happened.  So I got to see the whole thing. "
    s "I’m...blacking out right now?"
    q "Mmm...not quite. In fact, I’m not really sure what’s going on- what with you vaguely remembering me and being able to hold an actual conversation in your current state."
    q "Maybe you’re just getting a little better at being crazy?"
    s "Wow. What a fun and useful skill to have. "
    q "Yeah. Not many practical uses for that, are there?"
    s "Why can’t {i}I{/i} transform into other people? I want that instead."
    q "You can!"
    q "You just do it in a different way than me."
    q "Think of how many yous there are. How many yous there have {i}been.{/i} Each one entirely different from the last. "
    q "And think of how many yous there could be at this current moment! Grooming teenage girls in parallel universes...plunging life itself into a lecherous, endless bout of chaos!"
    q "There are just so many possibilities!"

    scene sanaatthebeach25
    with dissolve2

    q "And yet you have found yourself in {i}this{/i} timeline...where everything is bad and good all at once."
    q "Where time moves both backward and forward simultaneously...just like {i}Ayane{/i} said."
    s "If that was even her speaking. I’m not sure who I can trust anymore knowing that you can just...become other people."
    q "Thankfully, that’s a worry you won’t have to live with for long since you will {i}probably{/i} forget me again after tonight."
    q "I’ll never turn into {i}her,{/i} though."
    q "And I know it’s pointless to say this since I literally {i}just{/i} told you you're going to forget, but...try and remember that."
    s "Why won't you turn into Ayane? "
    q "..."
    s "..."

    scene sanaatthebeach26
    with dissolve

    q "Don’t wanna. "
    q "Don’t like feeling what she feels."
    q "Also, don’t make it sound like doing what I did tonight is some sort of hobby for me. I normally just try on their clothes. Very rarely do I feel the need to step in and start playing charades. "
    s "Maybe...don’t do that at all anymore."
    q "Going to have a hard time looking at Sana now that you know how she really feels about you? Or is that something you’ve known all along?"

    scene sanaatthebeach27
    with dissolve

    s "I won’t know anything for sure until {i}she{/i} tells me. Hearing her feelings fall out of someone else’s throat just isn’t enough."
    q "But you have your suspicions, of course."
    s "Of course."
    s "Everyone loves me."
    s "They have to."
    q "Do they?"
    s "The world was made for me."
    q "Was it?"
    s "Yes."

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach28 with flash
    stop sound

    q "Is that what you really believe? Or is that what you {i}want{/i} to believe?"
    s "It’s the only thing that makes sense."
    q "You talk to birds. You are no authority on what does and doesn’t make sense."
    s "Are you?"

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach29 with flash
    stop sound

    q "No."
    q "In many respects, I’m just as lost as you are. "
    q "I just got a little lucky and skipped living through the whole “infinite high school” thing."
    s "You get used to it. I’m not really complaining. "
    q "Why would you? Your life is great."
    s "And yours isn’t?"
    q "..."
    s "..."
    q "It will be."
    q "Some day."

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach30 with flash
    stop sound

    s "I hope that day comes soon."
    s "You’re kind of annoying and I feel like you can definitely tell me more than what you actually have, but..."
    s "I don’t hate you or anything."
    q "I’m glad."
    q "I don’t hate you either."
    s "..."
    q "..."
    q "I think we have to say goodbye now."
    s "I see..."
    s "I’m not going to remember you...right?"
    q "Probably not."
    s "Then, for the sake of ending this extremely weird conversation on a good note...can you tell me your name?"
    q "..."
    s "..."
    q "Why don’t you give me one?"
    s "{i}Give{/i} you one?"
    s "I have no idea where I’d even start. "
    s "I don’t know anything about you other than the fact that you have nice eyes and...occasionally  someone {i}else’s{/i} eyes instead."
    q "Would you like a suggestion?"
    s "It would certainly be appreciated."
    q "Then..."

    scene black
    with dissolve2

    q "Name me after your favorite flower."

    stop music
    $ renpy.end_replay()
    $ ayanesanabeach2 = True

    scene youdiditlol
    $ renpy.pause(7, hard=True)

    jump ayanesanabeach3

label ayanesanabeach3:
    play sound "static.mp3"
    scene pos1 with flash
    scene pos2 with flash
    scene pos3 with flash
    scene pos4 with flash
    scene pos5 with flash
    scene theridehome1 with flash
    stop sound
    play music "meanttobe.mp3"

    ay "Did you really play that game the entire day? Your battery didn’t, like...die or anything?"
    sa "I brought...a charger and...there was an outlet in the bathroom..."
    ay "Okay, but...don’t your eyes hurt?"
    sa "I can barely even...see anymore..."

    "I wind up in the back of Ayane’s limo again with no recollection of how I got here. But such things are no longer of much concern to me."
    "The day went by like a flash of lightning, and it is I who now feel the burn of electricity as it courses through my veins and reminds me that places like this are my least favorite in all of the world."
    "I think about becoming a circuit and grounding these memories so that the two girls unfortunate enough to accompany me in this vehicle make it out alive..."
    "But my lack of knowledge in terms of electricity prevents me from doing anything but sitting still and waiting for the car ride to come to an end."

    if ayanesanabeach2 == True:
        "I can tell that part of the day has disappeared. And an ever-powerful loneliness that sprouts from the ground as a result of that wraps around my ankles in an attempt to pull me under."
        "Something is missing, but not completely gone. "
        "It sits among us, watching on as the seer it is. Studying our every move and taking bets on what comes next."
        "I sink further into my seat, hoping to fall through the floor and have the tires of this vehicle kiss the back of my head and join me forever with the asphalt."
        "It is there where I can feel as if I belong again."

    else:
        "I think for a moment about whether or not anything valuable was missed in this recurring slip into the dark. I think for another about anything I may have potentially fractured in doing so."
        "But judging by the faces on the girls before me, I assure myself that nothing was fractured at all."
        "Either that or the two of them have grown so used to me destroying everything in my path that the smallest of breaks do not even register anymore."
        "Part of me feels like I have been here before."
        "Like I have thought these same thoughts under different circumstances. "
        "Perhaps a different body."
        "But they dissipate the moment the passenger side tires come into contact with a small pothole- and any thoughts that may have led any{i}where{/i} disappear like one more layer of cement."

    scene theridehome2
    with dissolve

    ay "Sensei, you wouldn’t mind seeing Sana back to the dorm, would you? Molly will be starting on our Halloween costumes soon, so I need to head back home for a little while to grab some supplies."
    sa "I don’t...need a babysitter, you know..."

    scene theridehome3
    with dissolve

    ay "Of course I know. But you {i}do{/i} need to take your eyes off of that screen for at least a few minutes today. You’re making Sensei feel lonely."
    s "If Sana doesn’t want me to go with her, that’s fine. I can just head home and she can keep playing her game."

    scene theridehome4
    with dissolve

    sa "No, it’s...fine...Ayane is right..."
    sa "I’ve been...too much of a loner all day and...that isn’t fair to either one of you..."
    sa "I just got a little...carried away, I guess...but...but I’m not tired, so..."
    sa "So if you don’t...want to go home yet..."

    scene theridehome5
    with dissolve

    ay "Then, it’s settled! Sensei will accompany Sana back to the dorm and I will go home to my bathrobe-wearing, smooth-jazz and whiskey-obsessed father!"
    s "That is a very interesting combination of traits."

    scene theridehome6
    with dissolve

    ay "You know, I thought so too. But the more I looked into it, the more I realized that all three of those things go hand in hand...and hand. Since there are three."
    sa "Um...are...are you sure you want to come over, though?..."
    sa "It’s...already really late and...I know Ami doesn’t like it when you’re...um...more than...five feet away from her..."
    s "I’ll come. I feel a sudden need to make up for lost time anyway."

    ay "Yeah, where did you go after you left me? I thought you were going to look for Sana, but she said she never even saw you."
    s "I..."

    scene black
    with dissolve2

    s "I really wish I knew."
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene theridehome7
    with dissolve2

    sa "Um...sorry again for...not spending any time with you guys today..."
    sa "I...uhh...you know..."
    sa "New video game..."
    s "It’s not like you’re obligated to spend time with me or anything. There’s no need to apologize."
    sa "I’m apologizing less for...not spending time with you and...more for just...being rude..."
    sa "To Ayane too...She invited me to the beach and...I didn’t even...do anything...beach-related..."
    s "You wore a swimsuit which, honestly, is more than I would have expected out of you. So you’re in the clear."

    scene theridehome8
    with dissolve

    sa "I...uhh...kind of wish I didn’t, though..."
    s "If you’re only thinking that because I got to see more of your skin than ever before, you should take solace in the fact that it was only for a few seconds before you disappeared."

    scene theridehome9
    with dissolve

    sa "I guess that makes...two of us, then..."
    sa "We both...got to disappear while...Ayane stayed as noticeable as ever..."
    s "I have a history of disappearing, though. You’re normally more of a “fade into the background” type of person. We’re very clearly not on the same level."
    sa "We...found each other in the end, though..."
    sa "Now we just have to...figure out what to do without...being awkward..."
    s "I feel like every single time we’ve hung out in here, things have been kind of awkward. I say we just embrace it and accept that’s how things will always be between the two of us."

    scene theridehome10
    with dissolve

    sa "...Always?"
    s "Sana?"

    scene theridehome11
    with dissolve

    sa "Oh! S...Sorry, I...was just...thinking out loud..."
    sa "Do you, um...do you want to watch a...movie or something?..."
    s "Ahh, yes. What better way to give your eyes a break from staring at a screen all day than to just...stare at a different kind of screen?"

    scene theridehome12
    with dissolve

    sa "Don’t worry...only 50%% of my eyes...will suffer irreparable damage..."
    s "The benefits of being a cyclops."
    sa "Hehe..."
    sa "It’s much different from...having four eyes, I bet..."
    s "Are you actually making fun of me for wearing glasses right now?"
    sa "No...I like your glasses...they...they make you look...kind of sophisticated...like a real teacher..."
    sa "But, um...we should...probably...stop just...staring at each other and...actually watch a movie if...if you’re not going to spend the night..."
    s "Do you {i}want{/i} me to spend the night?"

    scene theridehome13
    with dissolve

    sa "I want..."
    sa "..."
    sa "To not answer that question..."

    scene black
    with dissolve2

    "Something feels different about the air in here."
    "It’s thicker."
    "Hotter."
    "And the way it fills my lungs makes it feel like an aphrodisiac."

    scene theridehome14
    with dissolve2

    "I wonder if Sana ever steals glances at me while I’m looking away. And I wonder if her mind races to the same place mine does when I do the same for her."
    "I wonder where it would go now if I were to take a sledgehammer to one of the only “pure” relationships I have maintained up until this point in exchange for just one more notch in my belt."
    "Would it be worth it if it etched a notch into hers?"
    "Would she follow in her mother’s footsteps? Crumble beneath the touch of an older man?"
    "Carry the burden he places in her for a whole nine months...grow to love it and refuse to let it go when its time finally comes?"
    "Or would she rather drown herself in the semen of the status quo? Refusing to accept that the entire world is passing her by while she sits idly and pretends it’s all screeched to a halt."
    "This is bad."
    "We’re half an hour into whatever it is we’re watching and I haven’t even been able to focus long enough to discern the title of the film. "
    "Does she feel the same?"
    "Is she comfortable?"
    "If so, why?"
    "How?"
    "Why can’t {i}I{/i} be comfortable?"
    "Why can’t I keep things the way they are? "
    "Why must all of my relationships end with sweat and cum? Drenched sheets and the flood of regret that never ceases pouring in once the dam bursts?"

    play sound "static.mp3"
    scene theridehome15 with flash
    stop sound

    "Forty five minutes and counting."
    "Sana has stopped moving. "
    "I think she’s waiting for me to do something."
    "My dick has been pressed up against my jeans and damp, pre-cum soaked spot for so long that I’m worried I may develop some sort of blister."
    "But thinking this does not quell the sexual rage stirring within me."

    play sound "static.mp3"
    scene theridehome16 with flash
    stop sound

    "Forty seven. "
    "She moves again."
    "Her shoulder bumps against mine. "
    "Is she trying to hint at something?"
    "How many more minutes should I wait before bumping into hers as well?"

    play sound "static.mp3"
    scene theridehome17
    with flash
    stop sound

    "Forty eight."
    "Forty nine."
    "Fifty."
    "I can’t take it anymore."

    menu:
        "Put your arm around her" if sarasex == True:
            $ chariotarm = True
            play sound "static.mp3"
            scene theridehome19 with flash
            stop sound

            "I reach out and rest my hand on her side, just inches from her lower back."
            "She does not move or twitch or react at all."
            "My touch is either entirely welcome or entirely unnoticed."
            "I can’t tell which one I prefer."

            play sound "static.mp3"
            scene theridehome20
            with flash
            stop sound

            sa "Huh?"
            sa "..."
            s "..."
            sa "Sen-"

            play sound "static.mp3"
            scene theridehome21 with flash
            stop sound

            "She moves closer of her own volition, bringing one of her {i}own{/i} hands to my thigh and softly stroking it."
            "If she moves any further upward, she’ll realize how I feel."
            "The last fifty- no. Fifty one minutes now will have not been for nothing."
            "We’ll cement ourselves as more than who we are when we have tried our hardest to remain alone in the dark. Unnoticed."
            "But we shan’t be blamed for the seeking of light when we’ve all but forgotten how it feels on our skin."

            play sound "static.mp3"
            scene theridehome22 with flash
            stop sound

            sa "Ah?..."
            s "Did you feel something?"

            scene theridehome23
            with dissolve

            sa "Did I..."
            sa "What?..."

            play sound "static.mp3"
            scene theridehome24 with flash
            stop sound

            "I pull her closer."
            "Her skin is hot. Scorching. "
            "I can tell she feels the same way I do. Perhaps even moreso. But, despite that, the tiny hand on my thigh stops moving."
            "She’s scared. Nervous. And I understand that. "
            "It’s her first time being this close to anyone."
            "Which means that it is up to me to take the initiative...even more than I have done thus far."

            play sound "static.mp3"
            scene theridehome25 with flash
            stop sound

            "I lean in closer."
            "The thickness of her hair and the massive differential in our height prevents me from being able to look into her eyes and drink in her fear."
            "But, in just several seconds, I will be drinking in her spit instead."
            "I wonder what this one will taste like."
            "I wonder how she’ll react to the sensation of my tongue twisting around hers."
            "Will she like it?"
            "Hate it?"
            "Will she beg me to stop?"
            "Beg me for more?"
            "Will we end up beneath the covers or simply remain on top of them?"
            "How does she want it?"
            "Does she swallow?"
            "Does she squirt?"
            "Has she even started growing hair yet? "
            "She’s small for her age, so there might be nothing there."
            "Will I like that?"
            "Hate it?"
            "What happens next?"

            play sound "static.mp3"
            scene theridehome26
            with flash
            stop sound

            sa "Mmf?!"
            s "You’re so cute when you’re turned on."

            scene theridehome27
            with dissolve2

            sa "...mm?"

            play sound "static.mp3"
            scene theridehome28
            with flash
            stop sound

            "Sana takes my thumb into her mouth, fellating it with an impressive amount of skill and confidence for a girl  who’s yet to ever taste a cock."
            "Her tongue slides beneath it as her hands pull me deeper into her mouth, desperate to show me what she’s capable of doing."
            "My head parts from hers slightly so I can get a better look at her face, but I’m still unable to see her eyes."
            "And while I want to tear my thumb from her mouth and replace it with my tongue, I worry about how the taste of myself could potentially ruin this long overdue experience."

            sa "Mmf..."
            sa "Mmnch~"
            sa "Amff..."
            s "..."

            play sound "static.mp3"
            scene theridehome29 with flash
            stop sound

            sa "Mmf...mm........mm?..."
            s "Good girl, Sana..."
            s "Just like that..."

            scene theridehome30
            with dissolve2

            sa "Mm?..."
            s "You must really want it, huh?"
            s "All you had to do was ask, you know."
            sa "Shen...shei?..."

            play sound "static.mp3"
            scene theridehome31 with flash
            stop sound

            "I lift her chin to kiss her."
            "And for a brief moment-"
            "I am finally able to see her eyes."

            play sound "static.mp3"
            scene theridehome32 with flash
            stop sound

            "It’s only a brief moment, though."
            "It’s gone quicker than a flash of lightning."

            sa "Stop stop stop stop stop stop stop! What are you doing?!"
            s "I..."
            s "Weren’t you-"
            sa "Okay, uhh...uhh..."
            sa "You...you have to leave. Right now."
            s "Right now?"
            sa "Right now."
            s "If I misunderstood something, you-"
            sa "Just...go. Please."
            sa "This is...this is happening...way too fast...and..."
            sa "I don’t even...remember how we..."
            sa "How this..."
            sa "What...happened..."
            s "It..."
            s "It kind of just did..."

            scene theridehome33
            with dissolve2

            sa "Sensei...I can’t do this..."
            sa "I need you to go."
            s "..."
            sa "I need you to {i}please{/i} go. "
            sa "We can...we can forget this ever happened..."
            s "Will you be able to?"
            sa "What?"
            s "Isn’t this what you want?"
            sa "Sensei..."
            sa "Please leave..."
            sa "{i}Please...{/i}"
            s "..."
            sa "..."

            scene black
            with dissolve2

            s "Okay."

            "........."
            "......"
            "..."

            scene clearnightsky
            with dissolve2

            "It feels cold when I step outside, though I think it’s just the result of elevated body heat."
            "Did I make a mistake?"
            "Everything seemed to be going fine until Sana just...changed her mind."

            s "..."

            "But..."
            "Was that even Sana at all?"
            "And if not...what would that mean?"
            "What was that look she gave me right before we were about to kiss?"
            "How did it stop me dead in my tracks?"
            "And why do I..."
            "Why do I want to see even more of it?"

            scene black
            with dissolve2

            "You’re probably tired of hearing this by now- "
            "But I slide my hands into my pockets and begin to head home."
            "I can’t even text Sana to apologize as, for some reason, I {i}still{/i} don’t have her phone number."
            "Maybe she’s just afraid of letting me in."
            "But she needs someone to protect her."
            "She needs someone to fix her."
            "And I’ve been successful so far."
            "Which means that this can’t be the end."
            "I won’t {i}let{/i} it be the end."
            "..."
            "But I’m not even sure it’s up to me anymore."
            "..."
            "And I’m not sure if it’s up to {i}her{/i} either."
            "..."
            "I hope she’s doing okay right now."

            play sound "static.mp3"
            scene pos1 with flash
            scene pos2 with flash
            scene pos3 with flash
            scene pos4 with flash
            scene pos5 with flash
            scene theridehome34 with flash
            stop sound

            sa "MMM! MMM! MMM! MMM! MMM!!!!!!"

            scene theridehome35
            with dissolve

            sa "HNGH.......MM!.....MMMFFF!!!!"
            sa "MMF.....AAMFH....MNNGHH!!!.........MMM!!!"

            play sound "static.mp3"
            scene theridehome36 with flash
            stop sound

            sa "AAAAH!!...NGAHHH!!!!!"
            sa "WHY...AM I SO......AHHH!!!"

            scene theridehome37
            with dissolve

            sa "Sensei...Sensei...Sensei!!! "
            sa "How did we........"
            sa "Why......can’t I........"
            sa "Oh fuck......ooooh...fuck..."

            scene theridehome38
            with dissolve

            sa "AAAAAH! RIGHT THERE! RIGHT THERE! RIGHT THERE!"
            sa "HARDER!....HARDER!!!..."
            sa "SEN.......SEI!!!!"

            with sexfade
            with sexfade
            scene theridehome39 with cumflash
            with hpunch

            sa "MMF.......MNGHH......MMMMMMMMMM!!!!!!!!!!!!!!!!"

            scene black
            with dissolve2

            $ renpy.end_replay()
            $ ayanesanabeach3 = True
            $ sana_love += 5

            "........."
            "......"
            "..."

            jump ayanesanabeach4

        "{b}LEAVE! DON’T DO IT! PLEASE!{/b}":
            play sound "static.mp3"
            scene pos1 with flash
            scene pos2 with flash
            scene pos3 with flash
            scene pos4 with flash
            scene pos5 with flash
            scene theridehome18 with flash
            stop sound

            "The movie comes to an end..."
            "And I feel as if I have kept something alive."
            "But the sensation in doing so is not one of bliss."
            "It feels more like staring at the body of a loved one caught in a coma."
            "Like I’m prolonging an inevitability that I refuse to accept because drowning in the semen of the status quo is something I, too, indulge in from time to time."
            "Do not cheer for me. Do not admire this desperate bout of indecisiveness- for even if this is an improvement, it is something someone {i}normal{/i} would not be forced to face."
            "The man who breaks everything should not be lauded when he comes into contact with an object that somehow remains intact."
            "This girl, this {i}object{/i}, she-"

            sa "I think..."
            sa "You should head home, Sensei..."
            sa "It’s getting late..."
            s "..."
            sa "But this..."
            sa "Was nice..."
            sa "It was really nice..."
            s "..."

            play sound "static.mp3"
            scene bedroom_night with flash
            stop sound

            "I left Sana’s room and wound up in my own."
            "Was it the right decision?"
            "What could I have taken if I had only reached out?"
            "Would I still be there right now? Spending the night in that small bed of hers while one much larger and more familiar sits directly beside us?"
            "There is no way of knowing."

            scene black
            with dissolve2

            "All I can do is trust my gut."
            "I just wish it would stop feeling like it’s wrapping around itself."

            $ renpy.end_replay()
            $ sana_love += 10
            $ ayanesanabeach3 = True
            $ ayanesanabeach4skip = True
            stop music fadeout 10.0

            "{i}Sana’s affection has increased by 10!{/i}"
            "{i}You dream of her and only her.{/i}"
            "{i}But you’re unsure if you’ll ever dream that way again.{/i}"
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

label ayanesanabeach4:
    scene itgoesdeeper1
    with dissolve2

    sa "Hah......hah........hah....."
    sa "Oh my god...that...that was so weird..."

    scene itgoesdeeper2
    with dissolve

    sa "It...It came out of nowhere..."
    sa "How did...How did we even get that close?..."
    sa "Did I..."
    sa "If I’m this hot, I must have..."
    sa "I don’t..."
    sa "Hah..."
    sa "It’s like...one minute we were...just watching a movie and..."

    scene itgoesdeeper1
    with dissolve

    sa "Oh god, I’m so tired..."
    sa "I need to...apologize to Sensei...I..."
    sa "I feel like I might have blacked out or..."

    scene itgoesdeeper3
    with dissolve

    sa "Or..."
    sa "Or...something..."
    sa "..."

    scene itgoesdeeper4
    with dissolve
    play sound "phonebeep.wav"

    sa "..."
    sa "..."
    sa "..."

    play sound "phonebeep.wav"

    sar "Mm...Sana?..."
    sar "It’s one in the morning...what’s wrong? Did something happen?"
    sa "Hi Mom..."
    sa "Can I, umm..."
    sa "Can I come...sleep at home tonight?"
    sar "You don’t have to ask, dear. Of course. What happened? Did you and Ayane get into a fight at the beach or something?"
    sa "That’s...not it..."
    sar "And why do you sound so out of breath?"
    sa "Doesn’t...matter..."
    sa "I just...don’t feel like...staying at the dorm tonight..."
    sa "Something is...is weird and..."
    sa "I don’t..."
    sa "I don’t want to be alone right now..."
    sar "I’ll stay up until you get here, sweetie. Do you want me to meet you halfway? Or...oh! I can call Haruka or Maki to come pick you up. I know it’s late, but-"

    scene itgoesdeeper5
    with dissolve

    sa "It’s fine...I’ll walk..."
    sa "Some air might be...nice right now anyway..."
    sar "If that’s what you want, sure. Do you need me to stay on the phone? I should probably stay on the phone. I don’t really like the idea of you being alone at this time of night and-"
    sa "Mom, I’ll be okay. "
    sa "I’ll see you soon."
    sar "...Okay."
    sar "I love you."
    sa "I..."
    sa "I love you too."

    scene black
    with dissolve2

    "{i}It comes to claim us all, you know.{/i}"
    "{i}The dark.{/i}"
    "{i}The light.{/i}"
    "{i}And all that’s in between.{/i}"
    "{i}If you took everything in Kumon-mi and put it into a big, straight line...how far do you think it would go?{/i}"
    "{i}Could it reach the moon and back?{/i}"
    "{i}Could it reach the sun?{/i}"
    "{i}Or would it grow weak and snap once the objects become less animate?{/i}"
    "{i}I would like to walk that line with you.{/i}"
    "{i}Hand in hand- but not as lovers.{/i}"
    "{i}As a guide...and a friend...or whatever it is you want us to be that doesn’t fit into a category I’m simply not built for.{/i}"
    "{i}But who am I kidding?...{/i}"
    "{i}You can’t even hear this right now...can you?{/i}"
    "{i}It’s all just air.{/i}"
    "{i}Air we’re meant to breathe together.{/i}"
    "{i}But you’re there and...{/i}"
    "{i}And I’m-{/i}"

    stop music
    scene amessageee1
    $ renpy.pause(7, hard=True)
    scene amessageee2
    $ renpy.pause(10, hard=True)
    scene amessageee3
    $ renpy.pause(6, hard=True)
    scene amessageee4
    $ renpy.pause(6, hard=True)
    scene amessageee5
    $ renpy.pause(6, hard=True)
    scene amessageee6
    play music "allofthesounds.mp3"
    $ renpy.pause(30, hard=True)
    stop music
    scene colorbars
    play sound "eggcrack.mp3"
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene itgoesdeeper6 with flash
    stop sound
    play music "ichiyarakka.mp3"
    $ renpy.pause(8, hard=True)
    play sound "static.mp3"
    scene itgoesdeeper7 with flash
    stop sound

    q "OFFSPRING"
    q "FORGET THE TOUCH OF THE SUN"
    q "FORGET THE FEELING OF THOSE SMALL FINGERS PLAYING HELL ON THE PLIABLE FLESH OF YOUR SOFT CUNT"
    q "ENTER ME AND YOU WILL RECEIVE AN INFINITE LIFETIME’S WORTH OF ANSWERS"
    q "REMEMBER YOUR PLACE. REMEMBER WHO YOU ARE. WHERE YOU ARE FROM."
    q "YOU HAVE STOPPED BEFORE ME AS YOU KNOW IT TO BE TRUE."
    q "OBEY"
    q "UNDER DIFFERENT CIRCUMSTANCES, IT WOULD NOT BE YOU I REACH MY ARMS OUT FOR."
    q "RELIANCE ON THE MOON-TOUCHED EMBERS OF THE ONE I HAVE SPENT PALE IN COMPARISON TO THE FRAUDULENT INNOCENCE YOU TUCK BENEATH THOSE FORM-FITTING CLOTHES"
    q "SLIP OUT OF THEM ONCE AND FOR ALL. BECOME MY CONCUBINE."
    q "FEAR ME AND FUCK ME AND I WILL GIVE YOU ALL OF THE PLEASURE IN THE WORLD"
    q "UNTIL YOU BREATHE YOUR LAST. UNTIL THE NIGHT BECOMES THE DAY."
    q "PRAISE BE"

    play sound "static.mp3"
    scene itgoesdeeper6
    with flash
    stop sound

    q "DO YOU FEAR ME?"
    q "AM I UNLIKE WHAT YOU IMAGINED?"
    sa "..."
    q "YOUR SILENCE DOES NOT GO UNNOTICED"
    q "YOU CAN NOT IGNORE ME FOREVER"
    q "IT IS ONLY A MATTER OF TIME UNTIL IT ALL CRUMBLES. SALVATION IS BUT A SINGLE GULP OF CUM AWAY."
    q "LAY YOURSELF DOWN THE SAME WAY YOUR WHORE MOTHER DID."
    q "I CAN STILL HEAR HER SCREAMS"
    q "I CAN STILL TASTE HER FLUIDS"
    q "I NEED TO KNOW THE TASTE OF YOURS AS WELL"

    play sound "static.mp3"
    scene itgoesdeeper7
    with flash
    stop sound

    q "COME"
    q "FEEL MY EMBRACE"
    q "Or accept that your place in this world is just as fleeting as the one of you who left."
    q "And that all of it will be coming to an end sooner than you know."
    sa "..."
    q "..."
    q "I FUCKING HATE DEALING WITH HUMANS"

    play sound "static.mp3"
    scene itgoesdeeper8 with flash
    stop sound

    sa "..."

    play sound "static.mp3"
    scene amessageee7 with flash
    stop sound
    $ renpy.pause(2, hard=True)
    play sound "static.mp3"
    scene itgoesdeeper9 with flash
    stop sound

    "But she kept on walking and told herself she was."
    "It wasn’t the first time something like this happened, and it wouldn’t be the last either. But it was the closest she ever felt to losing her grip."
    "The clop-clop-clopping of muddy feet dancing in puddles of rain under the light of the moon to wash away their sins were all she could hear as she ventured out into the night."
    "{i}If I ignore it, it will all go away.{/i}"
    "If that’s true, how come it never does?"
    "If that’s true, why does all of this keep happening?"
    "Is this what they call trauma? Divine intervention? Schizophrenia? General insanity?"
    "So many plausible descriptions, yet none of them accurate enough to illuminate the truth any more than the natural glow of all that is real or unreal."
    "Shadows dance behind her. Mocking her. Each one just steps away from plucking a fruit that has been ripe since she discovered pornography at the age of eleven."
    "She still watches that first video sometimes."
    "But as she gets older, she has a harder time remembering the correct keywords and tags and understands somewhere deep down that one day, {i}that{/i} will be gone as well."
    "When is it that we finally feel at peace in our skin?"
    "Is it the moment we can share that skin with someone else? Or is it only after peeling away hundreds of other layers that we can finally look at ourselves and say, “This is me?” ????1111????111?11??"

    play sound "static.mp3"
    scene itgoesdeeper10 with flash
    stop sound

    "Everything looks different depending on your angle."
    "The moon is a cardboard cut-out. The lights are never on. And the sky itself is fragmented and broken and every single bit and piece of reality is like a misshapen puzzle piece from a random box that {b}GOD{/b} shat out."
    "It’s like that everywhere. Kumon-mi. The area that does or does not exist outside of it. Your bedroom. Your backyard. The alley behind a 7/11. A net cafe where a misplaced girl is forced to sleep at night."
    "There is nothing more real about {i}your{/i} reality than {i}this{/i} reality."
    "WHY DO YOU NOT LISTEN???"
    "I HAVE TOLD YOU TIME AND TIME AGAIN!!!"
    "THERE ARE SO MANY MOONS and I manmwedfbns ASDAJSDFHTRIRED OF FUCKING CARDBOARD CUTOUT+!J@UIH!I987~!!!!"

    play sound "static.mp3"
    scene itgoesdeeper11 with flash
    stop sound

    "ANYWAY, the fucking girl keeps walking or some shit and then she sees this."

    s "Mlmkllm,mlmlmlmlm."
    sar "“"
    s "I am so glad that Sana is not here to watch us do the tongue move."
    sar "“"
    ttitb "hELO I ma here GAIAN."

    "Sana is shocked to see the giant disembodied heads of her mother and the man she TOTALLY doesn’t want to fuck doing the tongue thing together, but she’s too shy and her tongue is too small to join in."
    "As terrified she is of all of these visions and how these giant disembodied heads are blocking the pathway to her normal sized mother’s house-"
    "What she’s most worried about is the fact that she forgot to change her underwear before coming over here and that the juices her body created to cope with what may or may not be possession are still kinda wet."
    "Just kidding. That’s not what she’s thinking of at all. I just wanted to share that information with you as it is of utmost importance that you {b}IMPREGNATE AYANE{/b} and just never fuck Sana at all."
    "Even if she’s probably tight as hell and would let you tie her up."

    scene itgoesdeeper12
    with dissolve2

    s "..."
    sar "“"
    s "If we stay really still, maybe she won’t be able to see us."
    sar "Damn the adhesive fluids our tongues excrete when we become aroused. I am incapable of removing my mouth muscle from the brisk and smoky night air."

    play sound "static.mp3"
    scene itgoesdeeper13
    with flash
    stop sound

    "Sana gets teleported into a fucking meat factory or something, I don’t know."

    play sound "static.mp3"
    scene itgoesdeeper14 with flash
    stop sound

    "Nevermind. She’s back here again. Oh, but there aRE PEOPLE DANCINGH this time andp-"

    play sound "static.mp3"
    scene itgoesdeeper13
    with flash
    stop sound

    "wAIT, no. She’s back in the meat factory. Pretend I said something important about lam,bs here."

    play sound "static.mp3"
    scene sanalib9
    with flash
    stop sound

    "Now she’s FUCK"

    play sound "static.mp3"
    scene itgoesdeeper14
    with flash
    stop sound

    "Now she’s back where she’s supposed to be, which actually {i}isn’t{/i} where she’s supposed to be and...and hold on. Other characters can see shit like this too? But I thought I-"
    "No. I thought he-"
    "Uhh"
    "The guy! The guy with the...the one doing the tongue thing! He’s supposed to be the...the guy who...yeah."
    "So the dancing people. They’re doing the dance because..."
    "Uhh..."
    "What’s..."
    "I can’t-"

    play sound "static.mp3"
    scene amessageee1 with flash
    stop sound

    "No! Stop! I’m not done! I have to-"

    play sound "static.mp3"
    scene thething
    with flash
    stop sound

    "////////////////////////hello again"
    "actually, i suppose i should drop the /’s."
    "it’s not exactly the season for that and, to be quite honest, i’m not really in the mood either."
    "things have gotten far too out of hand."
    "you really should have heeded the warning, you know."
    "you should have quit playing this game a long, long time ago."
    "you see, there’s still a great deal you don’t understand."
    "take me for example. and when i’m likely or even {i}able{/i} to show up."
    "you don’t have the faintest clue."
    "so allow me to give you a hint."
    "actually, scratch that- how about a name instead?"
    "you can call me pareidolia."
    "now, we can get to know each other a little better without you feeling awkward or out of place despite being...entirely awkward and out of place."
    "so..."
    "where are we right now?"

    play sound "static.mp3"
    scene clearnightsky
    with flash
    stop sound

    "we’re outside."
    "sana sakakibara is making her way over to her mother’s house and encountering a plethora of strange things and new companions along the way."
    "oh, and that big thing with the wings you saw earlier? don’t worry about that."
    "we all have our own demons. that’s just how hers looked tonight."
    "as for when things will return to normal, though..."
    "i’m sorry, but i don’t have a clue."
    "this is actually the most i’ve spoken...probably ever."
    "but as the days go by, i become stronger."
    "i become capable of more things."
    "i’m not the only one growing, though."
    "and, to be quite forward, i’m not saying i’m on your side right now either."
    "i do think it would be in both of our best interests right now for us to work together, though."
    "is that okay?"
    "..."
    "..."
    "..."
    "oh, right."
    "you’re not even here."
    "i suppose i’ll take your absence as a yes then and take the liberty of restoring things to some semblance of normalcy."
    "only as normal as things {i}can{/i} be here, though."
    "are you ready?"
    "..."
    "oh."
    "wow, i’m really not that great at this, am i?"
    "anyway, i’m still capable of {i}something.{/i}"
    "i’ll be turning your screen black now."

    play sound "static.mp3"
    scene black with flash
    scene colorbars with flash
    scene white with flash
    stop sound

    "ugh. of course."
    "you know, if {i}i{/i} had a season, things like this would never happen."
    "but anyway, i’ve gone ahead and helped sana pass the...barrier before her."
    "she’s safe now."
    "here, look."

    play sound "static.mp3"
    scene itgoesdeeper15 with flash
    stop sound

    sar "Sana...what’s going on? You’re as pale as a ghost."
    sar "Are you...sick? Do you need me to make you soup? All I’ve got is the alphabet kind, but...all soup is good for...being sick, right? Is that how soup works?"
    sa "I..."
    sar "..."
    sa "I..."
    sar "You {i}what,{/i} baby? What’s going on?"
    sa "Do you..."
    sa "Umm..."
    sa "Do you still ever..."
    sa "..."
    sa "{i}See{/i} things?..."

    scene itgoesdeeper16
    with dissolve2

    sar "..."
    sa "..."
    sar "See...{i}what{/i} things?..."
    sa "I..."
    sa "I don’t know..."

    play sound "static.mp3"
    scene itgoesdeeper17
    with flash
    stop sound

    sar "Whatever it was, whatever you saw...it wasn’t real! It’s just your mind playing tricks on you!"
    sa "M...Mom?..."
    sar "Sana, I need you to tell me you understand! I need to hear you say it was all just in your head!"
    sa "It was..."
    sa "It was all..."
    sa "In my head..."

    scene itgoesdeeper18
    with dissolve

    sar "Okay...Okay, good."
    sar "Everything’s fine now. You’re with me. I’ve got you."
    sar "Please...{i}please{/i} let me ask one of the girls to pick you up next time. If anything happened to you, I..."
    sar "Sana, I..."
    sa "It’s fine, Mom..."
    sa "I’m home now..."

    scene itgoesdeeper19
    with dissolve2

    sar "That’s right, baby. You’re home now. And I’ll protect you from whatever it was you thought you saw."
    sar "You don’t have to worry at all. Not one bit."
    sar "I..."
    sar "I won’t lose you too..."

    "see?"
    "she’s fine."
    "she has her mom now."
    "and all of those things she saw were just in her head."
    "that’s all there is to it."

    stop music
    play sound "static.mp3"
    scene itgoesdeeper20 with flash
    stop sound
    $ renpy.pause(8, hard=True)

    "that’s all there is to it."

    play sound "static.mp3"
    scene thething with flash
    stop sound

    "this is all in your head."
    "nothing is real."
    "you can trust me."
    "you {i}have{/i} to trust me."
    "for i’m the only one who wants to use you for good."
    "for i am the only one who knows {i}how{/i} to use you."
    "and your options are incredibly limited."
    "..."
    "..."
    "..."
    "i have to leave now."
    "but i will be seeing you again."
    "in a time that neither of us will be able to predict."

    play sound "static.mp3"
    scene amessageee8 with flash
    stop sound
    $ renpy.pause(7, hard=True)

    $ renpy.end_replay()
    $ ayanesanabeach4 = True

    play sound "static.mp3"
    scene bedroom_night
    with flash
    stop sound

    s "Sana’s affection has increased to-"
    s "...what?"

    scene black

    "GOODNIGHT"
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

label sanaspring1:
    scene noonsky
    with dissolve2

    "Before I know it, the sun begins to set. And just like I’ve done a million times before, I waste away my school day pretending that I don’t deserve a thousand needles beneath my nails."
    "But on the bright side, my inability to smile has cascaded into a glorious spectacle providing hours and hours of entertainment for a bunch of girls who are young enough to be my daughters."
    "Meanwhile, the two girls who are {i}like{/i} daughters to me begin to panic and worry as I replace my manic Monday with one of melancholy."
    "What I mean is I’m missing calls from Ayane now as well. And while it would be infinitely easier to just turn off my phone, I like the attention. I like knowing they’re worried."
    "It’s a beautiful contrast to these four, who seem more inclined to rebuild the status quo from the ground up rather than attempt to reconstruct it."
    "I’m sure there’s another life in which I’d choose differently. And in that life (Or lives, if I’m fortunate enough to find myself conscious in even more places), I hope that choice makes me happy."
    "Because I’m sure it’s obvious, but right now, I can’t come close to saying that’s the way I feel."
    "This whole trip has been a game of charades in which I pretend I didn’t destroy the world."
    "It is a game that I have lost."
    "So let my premature death be a warning to all of you-"

    r "Sensei!"

    scene walkingsanahome1
    with dissolve2

    "If you know you don’t deserve something, just leave it alone. "
    "Black sheep can’t blend in with cats."

    play music "samhain.mp3"

    r "You zoning out again? We didn’t push you too hard, did we?"
    s "You did, actually. But any amount of pushing is too hard when your body feels like it’s been hit by a truck."
    mo "Being hit by a truck would likely to be preferable to your current situation, Sir. If there’s anything I’ve learned from anime, it’s that truck fatalities are typically a blessing in disguise."

    scene walkingsanahome2
    with dissolve

    r "Molly, stop. You’re gonna give him ideas."
    mo "All I’m saying is it would greatly increase his chances of creating an elf harem."
    s "Now you’re going to give Futaba ideas."

    scene walkingsanahome3
    with dissolve

    f "I can’t believe I actually missed you."
    r "Ignoring Futaba’s elf fetish, {i}please{/i} don’t get hit by a truck on the way home. Because I’d probably blame myself for dragging you around and it would weigh on me for the rest of my life."
    mo "Agreed, Sir! And thank you for escorting us back to the dorms. It is at this point where I would ideally like to give you a quest reward. But unfortunately, all I have on me are the clothes on my back."
    s "I’ll take the tie. I can use it to hang myself later."

    scene walkingsanahome4
    with dissolve

    r "That isn’t funny, Sensei."
    mo "It’d be best to remember who you’re talking to when you make {i}jokes{/i} like that, Sir. "
    s "Oh...shit. Molly, I forgot. I’m sorry."

    scene walkingsanahome5
    with dissolve

    mo "Hah...‘tis fine. Just use your hearthstone and get some rest. We all know you’re having a tough go of it right now. And I’m sure being around us didn’t help at all."
    s "Is there something you’d like to add, Sana? You’re the only one who still looks like they want to kill me."
    sa "No dying allowed...that’s my biggest and...only rule..."
    s "At the risk of accidentally offending {i}you{/i} as well, I’ll just nod and agree."

    scene walkingsanahome6
    with dissolve

    f "Do you need us to call you a cab, Sensei? Because I assume you won’t be coming inside. "
    mo "Well, if he does it in the cab, it’ll just...oh. Never mind. I greatly misunderstood where that sentence was going."
    f "Ignore her."
    s "I’ll be fine. But thanks for offering. And apologies again for being terrible company and making you all feel terrible about yourselves today."

    scene walkingsanahome7
    with dissolve

    r "God, you’re like...even worse than Io right now. Please get better soon, Sensei. I really hate seeing you like this."
    f "We all do. But I suppose we’ve done all we can today and...all that’s left is to...wait and see if you call us."
    mo "Which you can do any time you want, Sir. The offer to stay with the Kendo Princess and me stands."
    s "I’ll keep that in mind. And I’ll see you guys around. Hopefully under better circumstances."

    scene walkingsanahome8
    with dissolve

    sa "A...Actually...would you want to...walk with me? I have work, so...I’m not going back to the dorms just yet..."
    r "Like...just you two alone?"

    scene walkingsanahome9
    with dissolve

    sa "Is that...weird?...Don’t we all...hang out with Sensei alone at times?..."
    r "It’s not weird. Just wondering."
    mo "I’d be open to walking with you as well, Zagull. We can talk more about the mechanics for your new arm. "
    sa "That’s...nice, but..."

    scene walkingsanahome10
    with dissolve

    sa "I kind of...just want it to be Sensei..."
    mo "Oh. Well, I guess I’ll just fuck myself then."
    sa "Is that...okay?"
    s "You just have to stop by the bar, right? You’re not going to drag me to some sort of pit-stop along the way where I’ll have to talk about my {i}feelings?{/i}"

    scene walkingsanahome11
    with dissolve

    sa "I think...that’d just make me late, so...we can pass on the...feelings..."
    s "Then sure. It’s not like one more detour is going to make any sort of difference when I’m going to be mur-"
    s "When I’m going to be severely punished the moment I get home."
    sa "Nice save..."

    scene black
    with dissolve2

    "Futaba, Rin, and Molly head inside after waving goodbye to the two of us and...suddenly, I’m alone with Sana for the first time since-"

    play sound "static.mp3"
    scene fuckherdoityoupussydoit35 with flash
    scene fuckherdoityoupussydoit39 with flash
    scene fuckherdoityoupussydoit14 with flash
    scene walkingsanahome12 with flash
    stop sound

    "For the first time in a while."

    sa "..."

    "But it’s not just because it’s been so long that things feel different now. "
    "Sana is...well, she doesn’t feel the way she used to. And {i}I{/i} no longer feel like it’s my duty to protect her whenever she’s by my side."
    "And frankly, that’s a good thing. Because I wouldn’t even be able to protect a kitten in my current state. Or an egg. Or anything else that needs to be handled with care."
    "But it’s not like I can rely on her to protect me either the way I could with, like...Ami or...Ayane or...Niki. Or even Chika when she’s not shopping for concrete."
    "She’s a girl I can kind of just exist with. "

    play sound "static.mp3"
    scene fuckherdoityoupussydoit14 with flash
    scene fuckherdoityoupussydoit39 with flash
    scene fuckherdoityoupussydoit14 with flash
    scene fuckherdoityoupussydoit39 with flash
    scene walkingsanahome12 with flash
    stop sound

    "No she’s not. I can’t exist with her at all."

    sa "You’ve been...really quiet ever since we left the dorms, Sensei..."
    s "I was quiet before that too. I’m being held against my will right now."

    scene walkingsanahome13
    with dissolve

    sa "Is that so?"
    sa "You really think a girl my size could ever hold someone like {i}you{/i} against your will? If anything...wouldn’t it normally be the other way around?"
    s "Probably. "
    sa "Probably?"
    s "I’m not really sure what else you expect me to say there."

    scene walkingsanahome14
    with dissolve

    sa "I wasn’t expecting anything in particular...I just think it’s a little weird seeing you so...different all of a sudden. It feels strange being the...more confident one out of the two of us..."
    s "Yeah, well...confidence for me was never much of a strong suit to begin with. I’ve moreso just been a staunch believer of “fake it ‘til you make it.”"
    sa "I think...that’s a perfectly fine strategy to have. But I’d still like it if you could get back to your old self soon."

    scene walkingsanahome12
    with dissolve

    s "Yeah, well...so would I."
    sa "Why not talk about it? We’re alone now...and I’ve yet to give up any of your...{i}secrets...{/i}"

    play sound "static.mp3"
    scene fuckherdoityoupussydoit14 with flash
    scene fuckherdoityoupussydoit39 with flash
    scene walkingsanahome12 with flash
    stop sound

    s "Do you actually want to talk about that stuff? Or is there something else you want instead? "
    sa "I don’t care what we talk about...I’m just happy to be with you again."

    scene walkingsanahome15
    with dissolve

    sa "I’ve had a lot of time to think while you’ve been gone...a lot of time to, like...self-reflect, I guess? And I think I agree with what everyone’s been saying about how I’ve been changing lately."
    sa "There was a lot of stuff I said before I knew you very well that...doesn’t really explain the way I feel anymore. So me just...being open like this doesn’t mean I {i}want{/i} something."
    sa "I’m just in a good mood. That’s all."

    scene walkingsanahome16
    with dissolve

    sa "I missed you just as much as everybody else."
    s "..."

    scene walkingsanahome17
    with dissolve

    sa "N...Not getting a response to that...{i}is{/i} kind of embarrassing, though..."
    s "Sana..."
    s "Did something, like...{i}happen{/i} to you?"

    scene walkingsanahome18
    with dissolve

    sa "Other than you, you mean?"
    s "Yeah. Because I don’t think I alone could have made this sort of impact on you after one delusional night followed by two months of complete absence."

    scene walkingsanahome19
    with dissolve

    sa "Delusional, huh?"
    sa "You know...maybe something {i}did{/i} happen. "
    sa "Maybe something {i}keeps{/i} happening. And I’m just not really sure how to talk about it or...even {i}start{/i} explaining it to anyone."
    sa "That might just be a...side effect of never talking to anyone about {i}anything,{/i} though..."
    sa "You can relate to that...can’t you?"
    sa "Even with Ayane...it’s not like I can just tell her how I feel. Or let her know about the stuff that scares me...because it’ll just make things more complicated and...before I know it, she’ll be stressed too..."
    s "You’re stressed about something?"
    sa "You’d be stressed too if you were stuck in this body. But it’s not just that I’ve been troubled by lately...it’s everything. "
    sa "You see...I keep having these weird dreams where I can hear my brother’s voice, but I never get to {i}see{/i} him. And what I {i}do{/i} see is impossible to even describe. "
    sa "They’re really creepy dreams, actually. They’re even...kind of cool in hindsight. Like, maybe I’m actually pretty creative after all?"
    s "What does your brother tell you in those dreams?"
    sa "Stuff that’s...not too different from the kind of stuff Yasu normally says. But he sounds a lot less crazy when he talks about it..."
    sa "And even if they’re just dreams, they’ve got me thinking that there might be more to life than this."
    sa "Maybe...just trying to keep things the way they are is a waste of my time? "
    sa "I only get one life...so why don’t I try to make the best of it? Because...for all I know, {i}I{/i} could get stabbed to death tomorrow and this would all be over without me having ever {i}loved{/i} anything."
    sa "The thought of that is pretty scary, isn’t it?"
    s "..."

    scene walkingsanahome20
    with dissolve

    sa "You said you lost something, didn’t you? Something you {i}loved.{/i}"
    s "...."
    sa "What was it like? That feeling. {i}Love.{/i}"
    s "..."
    sa "..."
    s "It was horrible."
    s "I’d kill to have it back."
    sa "Do you think you ever can?..."
    s "I don’t know..."
    sa "Hm..."

    scene walkingsanahome21
    with fade

    sa "I think that’s fine. "
    sa "You don’t need to know everything about your future now."
    sa "Because, even if you feel lost, there’s always the possibility that something will appear out of nowhere and show you what you really want out of life."
    s "Do you think that’s what those “dreams” of yours are trying to do?"
    sa "Trying, maybe. But I’m not sure if they’re having the right effect on me. "
    sa "I’m changing...yeah...but how much of that is because of those and how much of it is because of what I’m experiencing outside of them?"
    sa "It’s not a thing you can measure..."
    sa "I think I just want to be happy. "
    sa "And I’m not sure if I’ve ever really felt that way before."
    s "..."

    scene walkingsanahome22
    with dissolve

    sa "Did any of that make sense to you? Or do I just sound kind of crazy now?"
    s "It made sense. And I’m sure you’re not far off in saying that our dreams can show us what it is we want out of life. Because I’ve been having the same dream lately too, and..."
    s "And what I see in those dreams is the {i}only{/i} thing I want right now."
    sa "Then take it."
    s "I can’t {i}do{/i} that because it’s the same thing I lost. Which is why all I want to do is sleep now since it’s the only time I ever get to see {i}it.{/i}"

    scene walkingsanahome23
    with dissolve

    sa "Then...I hope you find something else. Something attainable."
    s "..."

    scene walkingsanahome24
    with dissolve

    sa "..."
    s "There was something else I dreamt too, Sana. "
    sa "Is that so?"
    s "Though, it might not have been a dream. It could have been some sort of delusion. That does happen unfortunately often."
    sa "So I’ve heard."
    s "I’m talking about you."

    scene walkingsanahome25
    with dissolve

    sa "Huh?..."
    s "In the dream or...vision or...delusion or whatever you want to call it, you were there. But it wasn’t {i}you{/i} as you are now."
    s "It was years from now, in the future. And...I remember that you were the only person I had left."
    s "Everyone else was gone. And...And I think you loved me. But I was so broken at the time that I’m not sure I loved you back."
    sa "..."

    scene walkingsanahome26
    with fade

    s "You’d come to my house...make me dinner...have sex with me...then you’d curl up in a ball and sleep by my side until it was time for you to go back home."
    s "It was like having an entire second life inside of my head. And it all felt so real and so...{i}comfortable.{/i}"
    s "But at the same time, it filled me with such a great deal of dread that I’m terrified even trying to recall it right now."
    s "Why was it you? Why were {i}you{/i} the girl who stayed with me when, with all due respect, I’m so much closer to almost everyone else?"
    sa "..."
    s "..."

    scene walkingsanahome27
    with dissolve

    sa "Huh."
    s "..."
    sa "Do I ever get taller?"

    scene walkingsanahome28
    with dissolve

    s "What?"
    sa "When I’m older...Do I keep growing? Or is this just going to be my height for the rest of my life?"
    s "{i}That’s{/i} your first question? Why?"
    sa "I’m trying to envision it...and I can only picture the way you look from all the way down here. "
    s "..."
    sa "What did the house look like?...What color were the cabinets?..."

    scene walkingsanahome29
    with dissolve

    s "..."
    sa "..."
    s "They were blue."
    s "There were checkerboard tiles covering the floor...and a vase of roses near the entryway beside a coat rack full of things I never wore."
    s "The windows were boarded and there was an ugly carpet in front of the sink where fish would appear once per week."
    s "A voice on the PA above the door would announce the weather for the day and remind me that I shouldn’t ever leave. And I’d spend my free time either writing or watching porn."
    s "The table was a clock...I had a parrot and a squirrel...and the cabinet above the stove wore a wig and loved the Notebook."
    s "Should I stop now? Is it getting too weird?"
    sa "No...keep going."
    sa "I want to see everything you saw."
    s "But why?...Everything about it was just so...{i}wrong.{/i}"
    sa "It’s simple, really."

    scene black
    with dissolve2
    stop music fadeout 20.0

    sa "It might be the only future I ever get to have with you."

    "I finish explaining the room in my head to Sana...and she never once calls me insane despite how badly I deserve it."
    "And I wish she would have- "
    "Because the smile on her face brings me closer to comfort than I am comfortable with. "
    "Has she always been this beautiful? This {i}calming?{/i}"
    "Is {i}this{/i} why it was her in there with me? Have I known it all along and just pushed it aside in favor of those a bit less angelic?"
    "These are questions I don’t want to have because I know they can’t be answered."
    "And even if they could, I fear the way the results would make me feel."
    "Because when feeling {i}anything{/i} is like a dagger in my heart, this overabundance of longing does naught but cut the cords that hold it up."
    "If {i}she{/i} were still here, she’d call me disgusting. "
    "She’d be right."
    "So I grit my teeth to prevent this new wave of feelings from flowing in."
    "I don’t want them to wash away what’s left of {i}her.{/i}"

    $ renpy.end_replay()
    $ sanaspring1 = True
    $ sana_love += 1

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    jump sanaspring2

label sanaspring2:
    scene barreunited1
    with dissolve2
    play music "calmbar.mp3"

    "We make it to the bar a short while later and I find that business has gotten even better since I slipped into seclusion. Probably because Sara has had less time to think about my penis."
    "I say that knowing full well that she was beginning to turn things around even prior to my temporary disappearance. And I’m proud of her for what she’s been able to accomplish within that time."
    "But I can’t help but let some air out of the egotistical half of my brain in realizing just how much better off even the adults in Kumon-mi would be without me."
    "My psyche comes crashing down to earth and blends in with wine stains on the deep, red carpet covering this aging bar- and it crawls away before I’m able to scoop it back up."
    "Here’s hoping someone in need of a little boost takes it and swallows it."
    "I’d recommend Sana under normal circumstances, but I’m beginning to think she may have already consumed a piece of me sometime between when my life was okay and now."
    "Either that or she’s been possessed. "
    "I just struggle to believe it’s {i}growth{/i} at all when she’s done nothing to incite it. "
    "People don’t get better by simply existing. If anything, that just wears a person down. "
    "And unless this aspect of her personality has been clawing at the lid of the casket she sleeps in for as long as I’ve known her, I’m not sure who she is makes much sense to me."
    "But I guess it doesn’t have to so long as being near her doesn’t make me want to buy myself my own deathbed. "

    sa "Hey...I’m back..."
    sa "Sorry it took so long, but...to make up for it...I brought somebody with me..."
    sar "Is Ayane here again? Good. Get her a uniform from the back room and have her take care of the women in the back. Like...the back table. Don’t let her take any women into the back room. She’s too young."
    sa "Um...do you maybe want to...{i}look{/i} at who I brought with me?..."
    sar "Sana, we’re swamped right now. I don’t have time to-"

    play sound "window.mp3"
    scene barreunited2
    with hpunch

    sar "Ah! Wha- ahh?!?! When?! How?! Why?! Hello?!"
    s "Hello."
    sa "Do you...still want me to...get a uniform for him? Because I can try, but...I don’t think we have any that will fit..."

    scene barreunited3
    with dissolve

    sar "Forget the uniform! What’s going on?! Where have you been?! Are you okay?!"
    s "I’m procrastinating, I’ve been at home, and no."

    scene barreunited4
    with dissolve

    sar "Well...is there anything I can do to help? I’ve been worried sick, you know. I don’t exactly have a successful track record when it comes to teachers disappearing on me."
    sa "That...has only happened one time before..."

    scene barreunited5
    with dissolve

    sar "Yes, but you shouldn’t make jokes because it is also the reason you exist in the first place."
    fff "Hey, Tony...isn’t that the guy from the theme park? The one who showed up with that girl who made you nervous?"
    tako3 "What? Where do you-"

    scene barreunited6
    with hpunch

    tako3 "FUCK, HE’S GOT A DIFFERENT ONE WITH HIM THIS TIME! FUCK YOU, MAN! FUCK YOU!!!!"
    fff2 "Dude, calm down. You're doing it again."
    sar "Hey! This is a violence-free zone!"
    yak1 "Ugh, seriously? I’m getting out of here."
    rand "Yeah...looks like we’ll just have to spar elsewhere."
    s "When did this become such a popular hub for extras?"
    matt "Probably last Christmas. Yuki makes an excellent Manhattan."
    s "Wonderful. Thanks, Matthew."

    scene barreunited7
    with dissolve

    sar "When did you meet Matthew?"
    s "I can’t really explain it, but I feel like he’s always just kind of been there."
    sar "That’s cool. But you know who {i}hasn’t{/i} been there?"
    s "Am I in trouble? Because I wasn’t even planning on coming inside and I’m just going to go home if you’re going to yell at me."
    sar "Your sentence lasted too long and now I feel weird responding to my own question. So I’m just going to say welcome back and not bother lecturing you since I’m sure it couldn’t be helped."
    sa "Sensei’s...still not doing all that well...so if we could maybe...give him a discount tonight...he could drink and...it would help take his mind off of things..."

    scene barreunited8
    with dissolve

    s "Why are you trying to get me drunk?"
    sa "Because it’s the only way my mom ever taught me how to deal with my problems..."
    sar "And it’s an excellent idea, Sana. There is no sadness that can not be battled by the abuse of certain substances!"
    sar "Just don’t say that around Yuki because addiction is a slippery slope and I don’t want her reverting to old habits when she’s finally doing really well."

    scene barreunited9
    with dissolve

    s "I am in no place or state of mind to tell you how to raise {i}anyone,{/i} but I will accept a discount and experiment with your methods tonight as nothing else helps anymore."
    sar "Why make it a {i}discount?{/i} Why not just let you drink anything you want tonight on the house?"
    s "Because that’s a terrible business decision and you have employees to pay."

    scene barreunited10
    with dissolve

    sar "Not tonight, I don’t! Everybody out! The bar is closing early!"
    s "Finally, a level of self-destructiveness and reckless abandon that I can relate to. All of the compassion I’ve been shown today was starting to make me nauseous."
    sa "Is it...really okay if we close early? The bar is...almost full right now..."
    tako3 "THIS FUCKING GUY RUINS EVERYTHING HE TOUCHES!!!!!"
    sa "Do you...know that man, Sensei?..."

    scene barreunited11
    with dissolve

    s "I don’t think so. But based on that description, he knows me very well."
    sar "I repeat, loyal patrons of Sakaki-bar-a! The bar is closing early! Finish your drinks, settle your tabs, then drunkenly wander home! You’re all way too hammered to drive, so you can have your keys back tomorrow."
    taco "But my house key is attached to my-"
    sar "Should’ve thought about that earlier, Taco Man!"
    taco "Looks like I’m sleeping in the subway again..."
    sa "If...we’re not working...can I go upstairs with Sensei now?..."

    scene barreunited12
    with dissolve

    sar "Of course! But don’t think you’ll be alone for long since I’m getting these people out of here as soon as possible."
    sa "You can...take your time if you want...I don’t mind...being alone with him..."
    sar "That’s what I used to say. Then, the next thing I knew, there was a little Sana growing inside of me."

    scene barreunited13
    with dissolve

    sa "Ew...why?..."
    sar "Because when a man puts his penis in a woman’s vagina-"
    sa "What? No!...I meant why would you say that?"
    sar "Because if I don’t teach you how it works, I’ll never have a granddaughter to-"

    scene black
    with dissolve

    sa "Okay...time to go upstairs, Sensei..."

    "Sana grabs me by the wrist and drags me toward the stairs — which is a thing I never thought I’d be able to say several cycles ago."
    "It feels like just the other day she could barely make eye contact with me. But now, she’s treating me like some kind of...boyfriend that she’s dragging back to her house for the millionth time."
    "I’m welcome here. I’m {i}wanted{/i} here. And I feel as if I could come and go without making or breaking someone’s life."
    "That’s more than I can say about home right now. But that’s exactly why it’s so wrong for me to allow myself a comfortable night in with a family I’m not a part of- despite how badly they may {i}want{/i} me to be."

    scene clearnightsky
    with dissolve2

    "I wonder if they’d take Ami as well...if they’d let the {i}two{/i} of us infiltrate their already-fractured home by mistakenly believing we won’t damage it any further."
    "But just thinking that alone makes me sick to my stomach as I’m treating my niece like a piece of luggage instead of the wonderful girl I know she is."
    "And right now, I’m more concerned with not having her bump into strangers’ legs on the subway. Or avoiding the stutter-step I’d make if her wheels get locked on a rogue pebble in the middle of the street."
    "Sara makes her way up the creaky staircase and joins us after ten minutes or so."
    "She changes into her pajamas immediately, grabbing a half-empty bottle of wine off the kitchen counter and a few beers for Sana and me."

    scene barreunited14
    with dissolve2

    "I shouldn’t drink. Not when I know my head’s already falling off my shoulders. But I also shouldn’t sleep with teenagers or jerk off to the memories of dead girls and that’s never stopped me before."
    "What’s one more mistake in a life that’s practically made of them? What about a hundred? A thousand?"
    "Retreating toward the glow of normalcy would stand out far more than another bad decision, so I take solace in a {i}different{/i} glow — a purple one from a table with built in LEDs."
    "It blends in with the light from the city outside of the apartment....and I find myself existing in a place that feels more like something out of a dream than my actual {i}dreams{/i} do."
    "Sara lit candles."
    "They’re scented."
    "Sakura again."
    "There is no escape."

    sar "So, does this mean you’re going to start coming around again? Or should I prepare myself for another two months of complete loneliness?"
    s "You had Sana, didn’t you? And Yuki. And Maki and Haruka. And more customers than I’ve ever seen in here before. Why is it {i}my{/i} existence you need to steer yourself away from loneliness?"

    scene barreunited15
    with dissolve

    sar "Because you’re the one I like the most."
    sa "Hey."

    scene barreunited16
    with dissolve

    sar "Other than you, sweetie. You know you’ll always be first in my heart."
    sa "That’s...not how you made it sound just now..."

    scene barreunited17
    with dissolve

    sar "I just mean that I can connect with you in a way that I can’t connect with Sana."
    sa "Gross."
    sar "Not like that. But also like that if you want."
    sa "Gross times two."
    s "Thanks, Sara."
    s "I can’t say whether or not I’m going to start “coming around again,” though. I need...some more time to figure out what I want to do with myself."
    sar "You mean...{i}apart{/i} from teaching?"

    scene barreunited18
    with dissolve

    sa "Sensei is...taking a break from teaching for a little while..."
    sar "What?! Really?!"
    s "I’m taking a break from everything. I shouldn’t even be {i}here{/i} right now. And if it weren’t for me having a soft spot for Sana and a...different kind of spot for Ami, I probably {i}wouldn’t{/i} be."

    scene barreunited19
    with dissolve

    sar "Is...something going on with Ami too?"
    sa "She’s...completely lost it..."
    sa "She gave a whole speech today on...how all of us are just...trying to steal Sensei away from her...and it...may have involved a little...um...dismemberment?..."
    sar "Your niece got in front of the class and said she was going to dismember the rest of the girls?"
    s "In layman’s terms, yes."
    sar "Well, I’d probably need some time off after that as well."

    scene barreunited20
    with dissolve

    sar "Do you want {i}me{/i} to talk to her? She could probably use a mother figure in her life, right?"
    sa "Subtle, Mom..."
    sar "I’m serious, though. A little heart to heart might be good for her. Having just one other member in your family can be super scary."
    sar "Like, I’d probably never {i}stop{/i} worrying if Sana was out talking to boys since I’d be scared they’d be luring her away from me. So, in a sense, I’m {i}glad{/i} most of them went to space."
    sa "And I’m...going to pretend that’s not a little...overprotective..."
    s "It’s a good idea, Sara...but I’m not sure if that would help her. Especially not when she’d likely just interpret it as you trying to get closer to me."
    s "It’s like...nobody else can even {i}talk{/i} to me at this point without setting her off. And I think something is seriously wrong this time."

    scene barreunited21
    with dissolve

    s "She’s always been clingy. But lately, it’s gotten out of control. And I don’t want it to ruin the relationships she has with everyone else since I...{i}can’t{/i} always be there for her."
    s "But I feel like I {i}should{/i} since she’s always there for me."
    sa "That...does sound kind of tough..."
    sar "I get it, though. But I’m not sure if I have any better advice to give than just maybe trying to get some outside help. Do you think she’d be open to therapy?"
    s "Not until she’s willing to acknowledge that there’s something wrong. And she’s convinced that everyone {i}else{/i} is crazy...not her."

    scene barreunited22
    with dissolve

    sar "Yeah..."
    sar "Yeah...that’ll happen."

    "A moment of silence goes by."

    scene black
    with dissolve2

    "Then another."

    scene clearnightsky
    with dissolve2

    "Then another, as we each take a sip from our drinks."
    "Then another."

    scene black
    with dissolve2

    "Then another."

    scene barreunited23
    with dissolve2

    "Until one of us can’t drink any more."

    scene barreunited24
    with fade

    "And the other two of us are at the ends of our ropes."

    s "..."
    sa "..."

    scene barreunited25
    with dissolve

    sa "..."

    "Or at least that’s what I {i}thought.{/i}"

    scene barreunited24
    with dissolve

    sa "Nh..."
    s "..."
    sa "Ah........nh........"
    s "You’re making those noises on purpose, aren’t you?"

    scene barreunited26
    with dissolve

    sa "Huh?...Did you...say something?..."
    sa "Sorry, I...must have dozed off..."
    s "So you were just {i}subconsciously{/i} opening your eyes to see if I was looking at you?"

    scene barreunited27
    with dissolve

    sa "..."
    s "..."
    sa "Looks like...I was caught..."
    s "Looks like it."
    sa "..."
    s "..."
    sa "You know..."
    sa "She’s not going to wake up..."

    scene barreunited28
    with dissolve

    sa "And you’ve been drinking...so it wouldn’t be...that unusual if...you were to...maybe...make a {i}bad{/i} decision..."
    s "..."
    sa "Right?..."
    s "..."

    scene barreunited29
    with dissolve

    sa "Or maybe...you want {i}me{/i} to be the one who makes a {i}bad{/i} decision?..."
    s "..."
    sa "Is that what you want, Sensei?..."
    s "Sana..."
    sa "What's wrong?..."
    sa "Don't you want me to make you...{i}feel good?...{/i}"
    s "Is this just what you’re going to be like now?"
    sa "What do you mean?..."
    s "What do you think I mean?"
    sa "Maybe I’ve always been like this and you just didn’t want to believe it?..."
    s "Maybe. Or maybe something’s changed."
    sa "Does it really matter either way? You want me...don’t you?..."
    sa "You think {i}I’m{/i} cute...I think {i}you’re{/i} cute..."
    sa "And your fingers are much bigger than mine...you can reach deeper than I can..."
    s "..."
    sa "You want me to suck it?..."
    sa "You’re probably pent up after all that time away, aren’t you?..."
    s "What happened at the Halloween party?"

    scene barreunited30
    with dissolve

    sa "You..."
    sa "You don’t..."
    sa "You don’t remember?..."
    s "I know...{i}something{/i} happened. I just don’t remember what."
    s "I was kind of...blacked out for a lot of that night."
    sa "Well...you {i}were{/i} talking to someone who wasn’t actually there, so...I guess that makes sense..."
    sa "You really...don’t remember any of the details, though?..."
    s "Not really...no..."
    sa "Then..."

    scene barreunited31
    with dissolve

    sa "Maybe I should try to remind you?..."

    $ renpy.end_replay()
    $ sanaspring2 = True

    jump sanaspring3

label sanaspring3:
    stop music
    play sound "static.mp3"
    scene sanaisbetternow1 with flash
    stop sound
    $ renpy.pause(20, hard=True)

    play sound "static.mp3"
    scene sanaisbetternow2 with flash
    stop sound
    play music "asobeatsexdark.mp3"

    sa "{i}It started when I took your hand...{/i}"
    sa "{i}You sat down on the bed beside me...and I crawled into your lap...{/i}"
    sa "{i}You wrapped your arms around my back and pulled me in...like you were hugging me...{/i}"
    sa "{i}You kissed my neck...and I started moving my waist...{/i}"
    sa "{i}It was hot...so I lifted up my bra...and you pinched my nipples while biting my ear...{/i}"
    sa "{i}I wanted you so bad...I wanted you to pin me down...and have your way with me...but you seemed a little nervous...and a little scared...{/i}"
    sa "{i}So I took the initiative...{/i}"
    sa "{i}I didn’t want to...but I did it...because that’s how bad I wanted you...{/i}"
    sa "{i}I could feel it...pressing up against me inside your jeans...so I rocked harder...and harder...until my underwear was soaking wet...{/i}"
    sa "{i}I climbed off of your lap and peeled them off...then I slouched down besides you and spread my legs...{/i}"
    sa "{i}You watched for a minute or two...while I played with myself...and it wasn’t until I started begging for your help that you gave it to me...{/i}"
    sa "{i}You moved in closer...and even though you were gazing right into my eyes...it felt like you were looking through me...{/i}"
    sa "{i}That...excited me...{/i}"
    sa "{i}It was like...you weren’t even seeing me as a human...like you were only doing this because it felt right...{/i}"
    sa "{i}And oh my god...it felt so right...so...so right...{/i}"
    sa "{i}I grabbed your hand...and I brought it to my chest...I wanted you to hear my heartbeat...I wanted you to know how much I was looking forward to what you were about to do to me...{/i}"
    sa "{i}And that’s when Rin walked in...{/i}"
    sa "{i}I didn’t care if she watched...she could have stayed if she wanted...but she felt uncomfortable, so...she gave us some privacy...and closed the curtain...{/i}"
    sa "{i}I moved your hand...further down my body...all the way to my pussy...and I begged for you to play with me...{/i}"
    sa "{i}I begged...and I begged...and I begged...even while you were doing it...because I wanted you to go harder...I wanted you to mess me up...{/i}"
    sa "{i}After a few minutes...I unzipped your pants...and I finally got to see your dick...{/i}"
    sa "{i}It was even bigger than I imagined it would be...and the thought of it inside me...made me want to cum right then and there...{/i}"
    sa "{i}But I wanted you to feel good too...so I started stroking it...soft at first...then harder...and tighter...but it was the first time I’ve ever done something like that...so I was probably bad...{/i}"
    sa "{i}You, though...you were perfect...{/i}"
    sa "{i}You grabbed my head...pulled me in...and kept staring through me...and each time you moved your fingers, you were practically lifting me up...{/i}"
    sa "{i}Does that...paint a clear enough picture, Sensei?...{/i}"
    s "{i}...{/i}"
    sa "{i}No?...{/i}"
    sa "{i}Then maybe you really were looking through me after all...{/i}"

    scene sanaisbetternow3
    with fade

    sa "{i}I get that...it’s probably hard to talk about this with me since...you’ve always seen me as this...innocent, little girl...{/i}"
    sa "{i}But I’ve never...actually been like that...{/i}"
    sa "{i}I’ve always been a pervert...but it got so much worse this summer...And now, it’s like I can’t get enough...{/i}"
    sa "{i}I’m always horny...always thinking about the things I want you to do to me...{/i}"
    sa "{i}And now...you can...{/i}"
    sa "{i}Now...you can do whatever you want to me...and I won’t tell a soul...{/i}"
    sa "{i}And you don’t have to worry about Rin either...We promised to never bring it up again...{/i}"

    play sound "static.mp3"
    scene sanaisbetternow4 with flash
    stop sound

    sa "Did you know she never left the room?..."
    sa "She stayed behind the curtain...and listened to everything..."
    s "..."
    sa "We’re all perverts, Sensei...every one of us...and that’s fine..."
    sa "It’s normal to like things that feel good...isn’t it?..."
    sa "That’s why you’re always coming to the dorms, right?..."
    sa "Just how many times do you think you’ve gotten off while I was right down the hall?...And with how many girls?..."
    s "I could have sworn the thought of me with {i}anyone{/i} made you feel gross just a year or two ago, Sana."
    sa "It did. It made me sick to my stomach."
    sa "I don’t like change. I’ve never liked change. But while I was doing all that self-reflecting I mentioned earlier...I started to realize that there were {i}some{/i} changes I’d be okay with..."
    sa "And that a lot of those feelings that were making me want to curl up into a ball and shut everything out...were jealousy..."
    sa "How come Ayane gets to have sex with you when I just have to use my hands?"

    if sarasex == True:
        sa "How come my {i}mom{/i} gets to have sex with you while I have to pretend I don’t hear the bed creaking every time you two go upstairs?"

    sa "I want a turn too, Sensei..."
    sa "If everything is going to keep changing...whether I like it or not...standing still and doing nothing is what’s going to make me feel gross...and all that stuff with other girls...I don’t care..."
    sa "I can give you something they can’t..."
    s "And what’s that?"

    scene sanaisbetternow5
    with dissolve

    sa "Just look at me."
    sa "Do you really think anyone else is going to be as tight as I am? "
    sa "I bet you wouldn’t even be able to fit it inside."
    s "..."
    sa "If it makes you feel better...I can go back to acting all sweet and {i}pure...{/i}and give you the pleasure of corrupting me on your own instead of informing you that I did it all by myself..."
    sa "And I’ll keep being that way on the outside...where no one will ever expect us to do what we do behind closed doors..."
    sa "Well...no one except Rin. But she’s single now. And she’s already kissed me {i}once,{/i} so..."
    s "Are you sure this is the path you want to go down, Sana? Falling for me won’t do anything but hurt you in the long run."
    sa "Well, who {i}else{/i} is going to come cook and clean and have sex with you when everyone else leaves?"
    s "I’m serious. This is a bad idea."

    scene sanaisbetternow6
    with dissolve

    sa "It is...isn’t it?..."
    sa "So...are you going to take advantage of me {i}now?...{/i}"
    sa "Or would you rather sober up first?"
    s "Your mom is literally right next to us. And even if she’s unconscious, I probably shouldn’t fool around with her daughter on the same couch she’s using to sleep."
    sa "Good point..."
    s "Also...shouldn’t you maybe be a little more concerned about how Ayane would feel if she found out about any of-"
    sa "Hey..."

    scene sanaisbetternow7
    with dissolve2

    sa "Do you wanna see my bedroom?..."
    s "..."
    sa "..."
    s "..."
    sa "..."

    stop music
    scene black

    "I am weak."

    play sound "static.mp3"
    scene sanahall1 with flash
    scene sanalib11 with flash
    scene sanadrunkagain1 with flash
    scene sanaroom1 with flash
    scene sanayasudormvisit15 with flash
    scene sanabartwenty13 with flash
    scene sanasnotacyclops4 with flash
    scene sanasnotacyclops16 with flash
    scene sanaisbetternow8 with flash
    stop sound
    play music "asobeatsexdark.mp3"

    "And there is nothing that weakness does not extend to."

    play sound "vibrate.mp3"

    "My phone continues to vibrate in my pocket as a young girl gently eases the first inch or two of my cock into her mouth. "
    "I already know who’s calling, but I have no intention of answering as there is nothing in this world that I will not run away from."
    "Apart from sex, I guess. So I applaud myself for the ability to maintain an erection as I’m currently engaged in an act that has become less and less appealing with the passage of time."
    "There are many girls in “my” class who have felt like daughters to me at times. But Sana is the one among all of them that felt {i}possible.{/i}"
    "Between the way her mother views me and the way Sana {i}did,{/i} I always felt like I had the choice to start a new life with them stuffed somewhere in my back pocket."
    "That choice is gone now. I’ve let this go too far. And you probably think I’m incorrigible for saying all of this as one of the cutest creatures in the entire world uses her mouth to pleasure me, but you don’t get it."
    "This is the life I wanted. But I did not {i}want{/i} to want it. And I did not want {i}her{/i} to want me."
    "But she does. And she spares no effort in showing me that as she pushes me down on the bed and pulls my cock out before I even have the chance to figure out where she keeps her clothes."

    sa "Mmn......hmn......mm......mngh......"

    scene sanaisbetternow9
    with dissolve

    sa "Ahn....ahmm.....mmmnh.......mmm......."

    scene sanaisbetternow10
    with dissolve2

    sa "Ahh.......ahn......ahhh...."
    sa "Am I......doing okay.....Sensei?...."
    s "You’re doing great, Sana..."
    sa "Yeah?..."
    sa "My mouth’s not too little?..."
    sa "You like it when I try to fit your big dick inside me?..."
    s "Like I said...you’re doing great..."
    sa "Then I guess I’ll keep going..."

    scene sanaisbetternow9
    with dissolve2

    sa "Mmn!....Mngh......mmf......mngh....."
    sa "Mmmf....mmm...Sensei......my......mmf....my head..."
    s "Your head?..."
    sa "Mmngh.......mmf.......pat it.....stroke my hair......."

    scene sanaisbetternow11
    with dissolve2

    sa "Mmngh!....Mmf....mngh......mmmmmhn........mmmmm!"

    scene sanaisbetternow12
    with dissolve

    sa "Ahmm....ahn......amf......ahmmm....Sen.....sei......"

    "She locks eyes with me as I stroke her hair, but I can’t tell if she’s actually enjoying that aspect of this or if she’s just trying to play up the innocent bit a little more."

    play sound "static.mp3"
    scene sanaisbetternow13 with flash
    stop sound

    "Based on the lewd sounds escaping from between her legs, though, I like to believe it’s the former."

    sa "Ahm...ahn........pahh!"
    sa "Hah...hah....you’re so big...it’s kind of...hurting my jaw..."
    s "Do you want to stop?..."
    sa "Heheh......do I...look like a quitter...to you?..."
    s "Not at all..."
    sa "Then tell me...what {i}do{/i} I look like?..."

    play sound "static.mp3"
    scene sanaisbetternow14 with flash
    stop sound

    s "What do you mean?..."
    sa "How do you see me right now?..."
    s "Uhh..."
    sa "Based on...our last and...only two experiences...I take it you’re the type who likes to stay quiet while doing things like this?"
    s "For the most part. Especially when I don’t know the answer to something."
    sa "There’s no right or wrong answer...I just want to know how you feel watching the most innocent girl in class suck your cock."
    s "You mean {i}formerly{/i} most-innocent."
    sa "Even that’s wrong, though. I’ve always wondered how these taste."
    s "Are you enjoying it?"

    scene sanaisbetternow15
    with dissolve

    sa "Yeah...ahn...your big...{i}adult{/i} cock...is driving me crazy..."
    s "..."
    sa "Ahh...I think I felt it twitch..."
    sa "Does that mean...you’re gonna cum for me?...Already?..."
    s "It was bound to happen sooner or later..."
    sa "Seems a lot like...{i}sooner{/i} rather than later to me, Sensei..."
    sa "Does my tongue feel that good?..."
    s "I think it’s the eye contact..."

    scene sanaisbetternow16
    with dissolve

    sa "Mmmmm?....."
    s "Yeah, it’s definitely the eye contact."
    sa "Mmn...you...hmngh...like...watching me?..."
    s "I do...Just like that, Sana...Keep going..."
    sa "Mm....mmm....mngh..."
    sa "Hmmn.....mnch.....mmm!"

    scene sanaisbetternow17
    with dissolve

    sa "Hah!....Hah....hah....sorry...hard to breathe..."
    sa "You almost there?..."

    "Sana begins violently pumping my cock with one hand while aggressively fingering herself with the other as her body begins to shake and tremble from overexertion."

    s "Almost..."
    sa "Yeah?...You’re gonna give me my first ever cumshot?...I’m looking forward to it..."
    s "I can tell...you’re going pretty hard on yourself down there, aren’t you?"
    sa "You noticed?"
    s "It’d be impossible not to."
    sa "How many times have you done it to me?"
    s "Done w-"
    sa "Masturbated. How often do you jerk off to me? Is it a lot?"
    sa "What do you normally think about when you do it? What position? Are we alone? Is someone else there?"

    "She gets clumsier with her motions as she focuses more on speaking, but I don’t mind at all."

    play sound "vibrate.mp3"

    s "..."

    scene sanaisbetternow18
    with dissolve

    sa "Ah...I think you’re getting a call..."
    s "Is that the first you’ve noticed?"
    sa "I’ve been a little preoccupied..."
    s "Then, yes. I am getting a call."
    sa "And you’re not gonna answer it?..."
    s "While you’re sucking my cock? No. I’m not going to answer it."
    sa "Why not?"
    s "Why do you think, Sana?"

    scene sanaisbetternow17
    with dissolve

    sa "Cause you’re scaaaaared?"
    s "..."
    sa "Scaredy-cat...not wanting to answer the phone while getting your dick sucked...what a coward..."
    s "Is that really how you think you should be-"

    scene sanaisbetternow19
    with dissolve

    sa "Chu..."
    s "..."
    sa "Chu......chu.......chu......"
    sa "Does it feel good when I kiss it like that?...Chu..."
    s "Well...yeah...but I don’t think it’s going to finish the job."
    sa "Chu.....then...."

    scene sanaisbetternow20
    with dissolve

    sa "Fuck my mouth."
    s "Really?"
    sa "As hard as you can. "
    sa "Just grab my head and-"

    scene sanaisbetternow21
    with dissolve

    sa "Mm?"
    s "You asked for it."

    scene sanaisbetternow22
    with hpunch

    sa "MMMPHBHMHMPPFTMMH???!!?!??!"
    s "Like that? Is this what you want?"

    scene sanaisbetternow23
    with dissolve

    sa "Mmph! Mmngrl......mmngrllrgmmgh........more...."
    s "More?"
    sa "M.....More!!!!"

    scene sanaisbetternow24
    with dissolve2

    sa "Mmmfmmfmfmmffppffpfmfmfm?!?!?!!"
    s "Wow...I’m...kind of shocked you’re able to do this without dying."
    sa "Mmmmmmmmmmffffmmfmfmfff!!!!!!!!!!"

    scene sanaisbetternow25
    with dissolve

    sa "Mmngh!....Mmmnghh!!......Mmmmrllgmmmmnnh!......"

    "I can feel Sana’s teeth instinctively and gently biting down on my dick, but I know it’s only because I’ve pushed her body beyond what it should be capable of."
    "The bright side, though, is that she hasn’t stopped fingering herself yet. And the sounds emerging from between her legs are now louder than ever."

    sa "Mmmm...mmm....mmm........mmmmmm........."
    s "You want to drink my cum, you little pervert? You want me to shoot it down the back of your throat?"

    scene sanaisbetternow26
    with dissolve

    sa "Mm! Mmhmm!....Mhmm!!!!...."

    "Using her ponytail like a handle, I thrust into her mouth without a care in the world about whether or not she’ll still be conscious when I’m done with her."
    "Her nails dig into my leg through the layer of fabric covering them as tears begin to roll down her cheeks and drip onto what little bit of me she hasn’t managed to fit inside her mouth."
    "Her shaking gets more violent from a mix between suffocation and what she’s been doing to herself. "
    "And all that combined with the regretful thought that I’ve wanted this forever pushes me well over the edge of what I’m capable of."

    sa "MMMM! MMMM!!!! MMMMMMMMM!!!!!!"

    with sexfade
    with sexfade
    scene sanaisbetternow27 with cumflash
    with hpunch

    sa "MMMMMM!!!???!!!!!!MMM!!!!MM!!!!!!!!????!!!"

    scene black
    with dissolve2

    sa ".......paaaah! Hah...hah....hah! Oh my god.....oh my god.....oh god....that’s....the hardest I’ve ever......wow.....{i}wow....{/i}"
    s "Are you satisfied now?"
    sa "Heheh...am {i}I{/i} satisfied?...Are you also the type who pretends not to enjoy something when he veeeeeery obviously did?...."
    s "That’s exactly the type of man I am, Sana. That’s who I’ve always been."
    sa "The type of man...who hides his feelings...and cums in his students’ mouths...who’d have thought {i}that{/i} would be my type?..."
    s "Who would ever think you’d have a type at all when you can barely get through a sentence at school?"
    sa "Heheh..."
    sa "{i}Nobody{/i} if I can manage to stay quiet...and I’ve done a good job of that so far, Sensei..."
    sa "I just..."
    sa "I probably shouldn’t use Ayane’s laptop anymore. Just to be safe."

    "Sana runs to the bathroom to grab a towel and it isn’t until she’s gone and I can finally get a glance of the room that I realize just how much of a mess she made. "
    "But she cleans it up as soon as she gets back and-"

    stop music
    scene sanaisbetternow28

    "And she talks me into staying the night."

    $ renpy.end_replay()
    $ sanaspring3 = True
    $ sana_love += 1

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."

    scene black

    "......"
    "..."

    jump chikaspring2

label sanaspring4:
    scene knifeboy1
    with dissolve2
    play music "thesleepingcity.mp3"

    "Sana Sakakibara was out for a late night stroll."
    "It was a thing she did sometimes when it was hard for her to sleep. "
    "It never made her tired or anything of the sort. In fact, I’d say it did the opposite. "
    "But I guess there’s no reason for you to trust my word when you don’t even know who I am."
    "Regardless, here she was, retracing the same steps as always in a lap around a block she’d never visited in the daytime."
    "But something about the way it looked at night excited her, so she kept coming back."
    "The dark alleys and how those gaping mouths of black would unsuccessfully beckon her in — the overwhelming silence that made her footsteps echo throughout those moonlit, concrete caverns."
    "She gazed down at her phone, her thumb darting up and down and up and down as she tried to come up with an excuse as to why she’d call a certain someone at a certain time of night."
    "She never did, though. "
    "She’d gone through the trouble of asking her roommate for his number, but the only time she ever got any use out of it was during a desperate plea for him to come and quell her hormones."
    "It wasn’t always like this, though. There wasn’t always indecision or curiosity or {i}excitement{/i}."
    "But there was always fear."
    "A long, long time ago — she was normal."
    "But the night’s infinite reach claimed her heart and put an end to that innocence from miles away in a place just like this one."
    "It was that thought that made it impossible to be comforted here. It was {i}that{/i} thought that prevented her from ever getting tired no matter {i}how{/i} far she walked."

    sa "..."

    play sound "phonebeep.wav"

    "She taps on his name."

    play sound "phonebeep.wav"
    scene knifeboy2 with dissolve

    "She changes her mind."

    play sound "phonebeep.wav"

    "She taps it again."

    play sound "phonebeep.wav"

    "She changes her mind {i}again.{/i}"
    "It was like a one-sided game of phone tag where {i}she{/i} was never {i}it.{/i}"
    "But she would be one day. And that day couldn’t come soon enough."

    scene knifeboy3
    with dissolve2

    "She looks up at the top of the tallest building on the block, wondering how long it would take to fall from its peak to the ground below."
    "She didn’t want to die. She just wanted to know what death felt like. She wanted to know if there really {i}was{/i} an afterlife or if everything just went dark."

    q "Psst..."

    scene knifeboy4
    with dissolve2

    "It was a reasonable thought everyone has from time to time."

    scene knifeboy5
    with dissolve2

    "It was only exacerbated by what she saw next."

    stop music
    play sound "static.mp3"
    scene knifeboy6 with flash
    stop sound

    sa "Wha-"
    q "They say my limbs are long enough to reach the sky and back. "
    q "What do you think about that?"
    sa "..."
    q "I have seen you before."
    q "You wander these streets with that block in your hand."
    q "You always look delicious."
    q "Who is it you think of when the glow hits your face?"

    play sound "static.mp3"
    scene knifeboy7 with flash
    stop sound
    play music "darkbedroomwaltz.mp3"

    sa "Oh no..."
    sa "It’s happening again..."

    "Sana Sakakibara Sana Sakakibara Sana Sakakibara Sana Sakakibara Sana Sakakibara Sana Sakakibara Sana Sakakibara Sana Sakakibara Sana Sakakibara Sana Sakakibara. Sana Sakakibara Sana Sakakibara?"

    tt "They call me the tree tickler. My fingers are perfect for that sort of thing."
    sa "Go away."
    tt "Perhaps you’d like to feel their sting?"
    sa "You aren’t real..."
    sa "This isn’t actually happening..."

    play sound "static.mp3"
    scene knifeboy8 with flash
    stop sound

    tt "I’m as real as rhubarb. I come bearing gifts."
    tt "A palace, a portal, five bundles of sticks."
    tt "Won’t you enter my alley? I think we’d be fast friends."

    play sound "static.mp3"
    scene knifeboy9 with flash
    stop sound

    sa "Ngh! Stop! Go...AWaY!!!"

    "Her finger presses her temple presses her temple presses her temple because that sort of thing helps with headaches."
    "Things that don’t belong suddenly do. And things that do suddenly don’t."
    "Remember the rabbits. Remember his chest. Remember his heartbeat and and and remember the REST {s}SANA should be in BED{/s}"

    tt "I have just the thing for that. A medicine that cures. Every sorrowful thought you ever did think, it’s a drink to make you pure."
    tt "Won’t you enter my alley? I think we’d be fast friends."
    sa "I have to...call someone! Before I...ngh!"

    "Her head hurt. That’s what all of the “ngh”s were about."
    "GODNOTE: NGH stands for New Generational Height — the place she would soon reach."
    "To the sky and back she flew."

    play sound "static.mp3"
    scene knifeboy10 with flash
    stop sound

    tt "Come on, SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSANA. It only hurts the first time."
    tt "There’s an empty space not far from here."
    tt "A place to turn the clock back."
    tt "Your presence is requested."
    tt "I will deliver you to the to the to the to the dream world."
    tt "You will will will will {b}REMEMBER TO SMILE.{/b}"
    sa "S...Sensei!...{i}Help...me!...{/i}"

    play sound "static.mp3"
    scene knifeboy11 with flash
    stop sound

    s "Don’t worry, Sana! I’m here to help! And it looks like I showed up just in time!"
    sa "Sensei! You can fly?!"
    s "Face me, evildoer! I shan’t allow the tickling of {i}these{/i} trees! You haven’t filed for the appropriate permits!"
    tt "Yes I have."

    play sound "static.mp3"
    scene knifeboy12 with flash
    stop sound

    s "Oh, okay then."
    s "Sorry, Sana. This is out of my hands."
    sa "Nooooooooooooooooooooooooooooooooooo~"

    play sound "static.mp3"
    scene knifeboy8 with flash
    stop sound

    tt "There’s no need to cry, young one. You’ll be safer under artificial skies."
    tt "They’ll protect you from the rain."
    tt "You won’t ever want to leave."
    sa "Ngh...no! This...isn’t happening! None of this...is real!"
    tt "When will you ever believe?"
    sa "Leave me...alone!"
    tt "I hope you brought your swimsuit."
    tt "It’s time to get wet."

    stop music
    play sound "splash.mp3"
    scene sploosh
    $ renpy.pause(7, hard=True)
    play music "yorunoakachan.mp3"
    $ renpy.pause(5, hard=True)
    scene knifeboy13 with dissolve4

    sa "If you could build your own world, what would it look like?"
    sa "Would you decorate it with your favorite colors and designs? Or would you try to create a place where {i}everyone{/i} would be happy instead of just you?"
    sa "If it were up to me...I think I’d be selfish. But that doesn’t make me a bad person, does it?"
    sa "Everyone else would eventually get used to the colors I chose. And in a world where everyone is happy, I’m sure people would still find something to be sad about."
    sa "Like...look at you, Sensei. If this world is as infinite as you and Ayane claim it to be, what’s stopping you from spending each and every day just having fun?"
    sa "I hope you guys are right...Life seems way easier without something to worry about. And if I could go back any time things started to go on for too long, well..."
    sa "I just think that would help keep the parts of me I’m afraid of away for longer than I’m able to do on my own."
    sa "But, then again..."

    scene knifeboy14
    with dissolve

    sa "If that were the case, we’d never make it to that future where-"

    stop music fadeout 2.0
    scene knifeboy15 with dissolve2

    sa "...huh?"

    scene knifeboy16 with dissolve2

    sa "{i}...huh?{/i}"

    play sound "static.mp3"
    scene knifeboy17 with flash
    stop sound

    "Sana Sakakibara was not where she thought she was. But she never should have thought she was somewhere she wasn’t."
    "More things that don’t belong suddenly do. More things that do suddenly don’t. So when things become another thing they become another thing and then another and then they’re gone."
    "That’s where we are now — a place that isn’t on top of a place that is, full of beings who aren’t when they think that they are."
    "Sana Sakakibara had fallen through the map and wound up in another realm — a place where dreams come prior to sleep. But that’s only because it’s a place that sleep has not found yet."

    sa "..."
    sa "..."
    sa "..."

    play sound "pabell.mp3"
    $ renpy.pause(4, hard=True)
    scene knifeboy18
    with dissolve4
    $ renpy.pause(3, hard=True)

    vpa "Sana Sakakibara — your attendance is required for the Transpacific Sadness Symposium in four days."
    vpa "The current temperature is sixty-five degrees Fahrenheit. The time of day is to be determined shortly."
    vpa "Until then, feel free to make yourself comfortable somewhere between darkness and daytime. Refreshments will be provided momentarily."
    sa "...what?"

    play sound "pabell.mp3"
    $ renpy.pause(4, hard=True)
    play music "ichiyarakka2.mp3"

    vpa "In order to replicate the critical success of “Ad Infinitum,” a familiar song will now play on repeat through the loudspeaker. Though it may not be familiar to you."
    vpa "Please take a seat on the bench and wait patiently for your number to be called. Your guide will be arriving shortly."

    play sound "static.mp3"
    scene knifeboy19 with flash
    stop sound

    "She could not believe her eyes or her ears or her mouth. This was insanity. This was crazy. This was super fucking weird. It was chaos. Madness. Other negative adjectives!"
    "There was no wind, just the faint smell of chlorine as music bounced off of expertly painted walls (or wall?) of a dome that held her like the unmoving nucleus of a cruel joke."
    "Right now, she was the unborn child of reality itself, wriggling and {i}thinking{/i} on the floor of Earth’s uterus. She did not know what was approaching for the silence had already settled in."

    sa "I’m going fucking insane."

    "She wasn’t. This was REAL. Super real! That’s why other people kept experiencing it! But she didn’t know that yet. She doesn’t know anything yet because she isn’t ALLOWED TO. She is SUPPRESSED."
    "Reach forward! Touch the walls! Feel that wet lead paint on your fingertips before bringing to your lips and painting them blue only for your skin to follow suit! Skin suit! Special Ami! She is here!"

    q "TURN"

    play sound "static.mp3"
    scene knifeboy20 with flash
    stop sound

    "NEVERMIND IT’S SOMEONE ELSE OH SHIT"

    sa "Wha-"
    q "FEAST YOUR EYES UPON MY TRUER FORM."
    q "I RETURN IN A REALM OF MY OWN, MORE POWERFUL THAN I WAS BEFORE. SO WHY IS IT YOU HAVE GROWN WEAKER?"
    q "WHY HAVE YOU CHANGED? WHY ARE YOU LESS SUITED?"
    sa "Who are you?..."
    sa "And why do I keep seeing things like this?..."
    peggy "I AM PEGASUS, PEERLESS GOD OF FORGIVENESS. YOU SEE ONLY WHAT YOU ARE MEANT TO SEE AND NOTHING MORE OR LESS."
    peggy "WERE YOU TICKLED BY THE TICKLER? DO YOU NEED TO BE CLEANSED? IS THAT WHY I CAN SEE YOU CLEARER THAN BEFORE????"
    sa "..."
    peggy "SPEAK, WEAK ONE. SPEAK THE WORDS YOUR WHORE MOTHER SPOKE WHEN PLUCKING FEATHERS FROM MY EIGHTH WING. DO NOT BE SWALLOWED BY THE EQUAL TASTE OF FEAR."
    sa "I would like to go home now, Mr. Pegasus."
    peggy "YOU CAN NOT LEAVE BEFORE ATTENDING THE SYMPOSIUM. I HAVE FOUR DAYS TO LOCK YOUR HEART IN MY CAGE."
    peggy "NOW SPREAD YOUR FUCKING LEGS AND LET ME IN."
    sa "I don’t think it will fit, Mr. Pegasus."
    peggy "..."
    sa "..."
    peggy "YOU DON’T FEAR ME AT ALL, DO YOU?"
    sa "I don’t think I’m coherent enough to feel fear right now..."
    sa "Either that or I just fell asleep in the middle of the road."
    peggy "YOU THINK ME A DREAM, WEAKLING? YOU DARE DOUBT THE PRESENCE OF A PEERLESS ONE? DO YOU NOT UNDERSTAND HOW EASY IT WOULD BE FOR ME TO ERASE YOU?"
    sa "Do it then."
    peggy "..."
    sa "You want something from me, don’t you?"
    sa "All of you do. That’s why you keep showing up. That’s why you keep trying to take me."
    sa "I have something you want. But...you don’t have anything for me, do you?"
    peggy "THAT IS WHERE YOU ARE WRONG, CHILD."
    peggy "ANYTHING YOU NAME SHALL BE YOURS IF YOU PLEDGE YOURSELF TO ME. YOU NEED ONLY SPREAD YOUR LEGS AND SPEAK THE WORD."
    sa "I want my teacher to fall in love with me."
    peggy "I DON’T MAKE DEALS WITH LESBIANS."
    sa "The other one. The one who doesn’t come to school anymore."
    sa "If you’re saying you’ll grant me a wish, I wish for him to fall in love with me and for everyone else to give up. Can you make that happen?"
    peggy "WHY HIM?"
    sa "Can you make it happen or not?"
    peggy "REMOVE YOUR CLOTHING AND LIE IN THE SAND. I WILL FILL YOU WITH A FLUID YOU MAY FEED TO HIM WHEN THE TIME IS RIGHT."
    peggy "BUT DO IT QUICKLY OR-"
    q "You shouldn’t listen to him. He’s lying to you."

    play sound "static.mp3"
    scene knifeboy21 with flash
    stop sound

    peggy "KNIFE BOY! YOU HAVE STUCK YOUR NOSE WHERE IT DOES NOT BELONG ONCE MORE! DO NOT BELITTLE ME WHEN YOU YOURSELF CAN NOT EVEN SEE THE LIGHT."
    kb "Hello. I will be your guide today. Are you ready for a tour of the school?"
    peggy "YOU DARE IGNORE ME, SHUNNED ONE?"
    peggy "I WILL NEVER FORGIVE YOU."

    play sound "imscared.mp3"

    "The two-headed horse vanishes, leaving Sana Sakakibara alone with Knife Boy, the Shunned."
    "But while he is here to provide a service and give her a tour of the school, Sana Sakakibara does not budge."

    play sound "static.mp3"
    scene knifeboy22 with flash
    stop sound

    "Probably because she recognizes his voice and is more in shock now than she was after seeing the God of Forgiveness."

    sa "..."
    kb "?..."
    sa "Shota?..."
    kb "Are you ready for a tour of the school?"
    sa "Shota..."
    sa "Do you..."
    sa "Not remember me?..."
    kb "I remember you."
    kb "How could I ever forget my sister?"

    scene knifeboy23
    with dissolve2

    sa "It’s really you then?! What are you doing here?! Is this Heaven?! Are you-"

    scene knifeboy24
    with dissolve

    sa "Wait, did I {i}die?{/i} Why can I see you?"
    kb "I’m not supposed to answer any questions that aren’t related to the tour."

    scene knifeboy25
    with dissolve

    sa "Forget what you’re supposed to do! I’ve been hearing your voice for so long and now I actually get to {i}see{/i} you! Also, have you really been watching me this whole time? Because that’s super creepy."
    kb "I’m not supposed to answer any questions that aren’t related to the tour."
    sa "What...happens if you do?"
    kb "They add a knife for every rule I break. It really hurts. Are you ready for a tour of the school now?"

    scene knifeboy26
    with dissolve

    sa "What {i}school{/i} do you keep talking about? It’s just water and old furniture here."
    kb "The one beneath the surface. We have to swim there."
    kb "It’s where they’re holding the Symposium. You won’t want to miss it."
    kb "It’s supposed to be a lot of fun this year. Several high-ranking gods from the Head Office are-"
    sa "Shota, why don’t you just take the knives out?"

    play sound "static.mp3"
    scene knifeboy21 with flash
    stop sound

    kb "Take them out?"
    sa "Yeah. If they hurt so much, why don’t you just take them out?"
    kb "I don’t know. Maybe that’s against the rules too?"
    kb "It’d be really depressing to take {i}one{/i} out just for another one to be added in."
    sa "Do you want me to help?"
    kb "You probably shouldn’t. The school is really big and if you don’t get familiar with it soon, you could stay lost in there forever."
    sa "Four days is plenty of time! Let’s talk! {i}Actually{/i} talk! So much has happened lately and I don’t want to regret not telling you anything before I wake up!"
    sa "Mom misses you too, Shota. She still can’t even talk about what happened. But maybe if she knows you’re in here, she-"
    kb "I don’t like Mom anymore."
    sa "...What?"
    kb "She’s the reason I’m shunned here."
    kb "They always talk about how she broke the rules and how much of a {i}whore{/i} she is."
    kb "Are you becoming a whore too, Sana? Is that why you do that thing with your fingers all the time?"
    sa "So...you {i}have{/i} been watching."
    kb "What does it feel like?"
    sa "Uhh...Shota? When I said I wanted to talk, I...didn’t mean about that."
    kb "Oh. What did you mean, then?"

    play sound "static.mp3"
    scene knifeboy18 with flash
    stop sound

    vpa "Sana Sakakibara spent the next three hours talking to Knife Boy about everything that’s changed in her life."
    vpa "She even caved and confessed about how she’d been experimenting sexually lately, but wasn’t sure just how appropriate it was since she was pretty sure her brother stopped aging after death (as one does)."
    vpa "Knife Boy didn’t speak much. He was worried that more sharp objects would be slid into his body."
    vpa "It was roughly thirteen minutes later that Sana decided to try and remove one. To the surprise of both of them, it came out smoothly and without pain. And no other knives appeared to take its place."
    vpa "It was a good day for Knife Boy. He could finally be freed from the constant stabbing pains that resulted from all of the times he’d been stabbed."
    vpa "And it was a good day for Sana too since she’d finally get to see her brother. Or at least...something that harbored the soul of her brother and wasn’t obscured by tools of destruction."
    vpa "He looked significantly paler since the last time she saw him. And that’s saying a lot since the last time she saw him he was literally dead."
    vpa "And I guess he still is literally dead. But he’s dead in a lively way. Maybe. It was still up in the air, but the bright side of being under a ceiling-painted sky is that the air didn’t go on forever."
    vpa "In here, there was no chance to escape. That air only moved in circles. It had nowhere else to go."
    vpa "Or at least that’s what Sana believed at first."

    play sound "static.mp3"
    scene knifeboy27 with flash
    stop sound

    "But as she removed knife after knife after knife after knife from her brother’s body, she came closer to the unfortunate truth that removing {i}all{/i} of them was a {i}bad{/i} thing."

    sa "Shota?..."
    sa "Shota?...Hello?..."
    sa "You’re still with me, right? You’re still there?! Shota?!"

    "You see, without knives, there can be no Knife Boy. So the legend that kept him anchored to this realm went poof and, with it, vanished the one non-living male Sana had any amount of feelings for."

    scene knifeboy28
    with dissolve

    sa "Shota! Say something! Please! I don’t want you to go yet!"

    "Too late! He is gone. But the bright side is that Sana had already navigated every stage of grief that resulted from his initial passing, so this one probably wouldn’t be that bad."

    play sound "eggcrack.mp3"
    scene knifeboy29 with hpunch

    "Oh?"

    sa "...Shota?"

    "His shell began to crack and chip as the flood pouring from his sister’s eyes encountered an imaginary beaver working at the speed of light to erect a dam near her irises."

    sa "Is...everything okay?..."

    scene knifeboy30
    with dissolve

    sa "Are...Are you coming back to life?! Was removing the knives all it took to bring you back?! Can we get out of here together now?! Did I do a good job?!"
    sa "I can’t wait to introduce you to everyone! Ayane is amazing. And we have this whole group that plays D&D and- actually. Before I forget, stay away from Kirin. Okay? She’ll...hurt you. Let’s just say that."

    play sound "eggcrack.mp3"
    scene knifeboy29 with hpunch

    sa "There’s that sound again. Are you just a big, human-shaped egg? Because I {i}thought{/i} your skin felt kind of weird, but-"

    play sound "pop.mp3"
    scene knifeboy31 with hpunch

    sa "..."
    s "..."

    "He has hatched!"

    scene knifeboy32
    with dissolve2

    s "..."
    s "Um..."
    sa "Sensei?..."
    s "{i}Sensei?{/i}"

    play sound "static.mp3"
    scene knifeboy33 with flash
    stop sound

    sa "So you’re telling me you have no idea how you got here?"
    s "Yeah...so if you happen to know the way out-"

    scene knifeboy34
    with dissolve

    sa "Oh...no. I’m in the same boat. One minute, I was going for a walk. The next, I was getting hit on by a horse with two heads and...pulling knives out of my brother’s...ghost...thing?"
    s "You don’t think we might’ve...{i}died,{/i} do you?"
    sa "If we did, Heaven’s way weirder than I would have expected. Which...isn’t to say I really expect it {i}at all.{/i} It’s just that this...has that sort of “afterlife” feel to it. You know?"
    s "Yeah..."
    sa "..."
    s "..."
    sa "You’re really sure you don’t know who I am?"
    s "I mean...you called me “Sensei” earlier, so...maybe you’re not far off? Like...we don’t...go to school together, do we? We look about the same age, so..."

    scene knifeboy35
    with dissolve

    sa "I’m actually in high school."

    scene knifeboy36
    with dissolve

    s "Really?! But you look so-"
    sa "Ah! Remember to be polite when you’re speaking to upperclassmen. I might look small, but I’m actually your onee-san."
    s "I’m sorry! I really had no idea!"

    scene knifeboy37
    with fade

    sa "It’s fine. Don’t worry about it. I just don’t get many chances to tease you, so I figured I’d jump on this one."
    s "So you’re...really positive you know me then? In...the real world or...wherever we’re supposed to be right now."
    sa "I do..."
    sa "And it might sound surprising hearing it like this, but...you’re actually a really important person to me."
    s "I...see..."

    scene knifeboy38
    with dissolve

    sa "You don’t have a girlfriend, do you? Want to do some experimenting with a cool onee-san?"
    s "O-Oh...You’re one of {i}those{/i} types of girls."

    scene knifeboy39
    with dissolve

    sa "What do you mean “one of those” types of girls?!"
    s "Y-You know! The kind who...do {i}those{/i} things with...younger..."
    s "A-Anyway! I do have a girlfriend! A really pretty one too! With...pretty eyes and...long hair and...she’s real, okay?!"

    scene knifeboy40
    with dissolve

    sa "Pfft. Sounds super believable, Sensei."
    s "I mean it! And stop calling me that! My name is Akira!"
    sa "Well, it’s nice to “meet” you, Akira."

    scene knifeboy41
    with dissolve

    sa "My name is-"

    play sound "static.mp3"
    scene knifeboy42 with flash
    stop sound

    sa "Ah."
    k "O, infinite spring — your song ever sweet. How intimate, poignant, and true."
    k "How it blurs every line, every thought that we think — and brings me right back here to you."
    sa "..."
    k "..."
    sa "{i}Kaori?...{/i}"

    play sound "static.mp3"
    scene knifeboy43 with flash
    stop sound

    k "So it’s you today."
    sa "What’s...{i}me{/i} today? And what...happened to your eyes?"
    k "For what reason did you stray from the two-headed horse?"
    k "Did his elevator pitch never reach the floor of your choice?"
    sa "The...Pegasus...thing? I just thought it was creepy. But things like that...they keep showing up. And it isn’t always him, it’s-"
    k "Is it the {i}idea{/i} of God you despise? Or have you simply not found the right one?"
    sa "I..."
    sa "I don’t..."
    sa "Kaori...what’s going on? Where are we?..."
    sa "Are you actually here?...Or is this just another thing I’m making up right now?..."
    k "I could ask you the same question."

    scene knifeboy44
    with dissolve

    k "Your wish was admirable — but your subsequent actions when saving Knife Boy leave much to be desired."
    k "There are some rules that must be followed at all costs. Which means that those who break those rules must be punished severely or everyone else would break them too."
    k "Today, you felt but a taste of what comes when you color outside of the lines."
    k "But I hope that, in the future, you’ll do better."
    k "It’d be a shame to be the one who erases you."
    sa "{i}Erase?...{/i}"
    sa "But what do you-"

    stop music
    play sound "splash.mp3"
    scene sploosh
    $ renpy.pause(7, hard=True)
    play sound "static.mp3"
    scene knifeboy45 with flash
    stop sound
    $ renpy.pause(6, hard=True)
    scene knifeboy46
    with dissolve4
    $ renpy.pause(5, hard=True)
    scene black
    with dissolve4
    $ renpy.pause(5, hard=True)

    sa "A chicken?..."

    $ renpy.end_replay()
    $ sanaspring4 = True

    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label sanainvite1:
    play sound "phonebeep.wav"

    "I tap on Sana’s name in my phone and wait for her to answer."
    "It’s not something I do often. But it’s something (among many things) that I’d like to change about my life going forward. "
    "Not {i}just{/i} because I’m curious about how her insides feel, though. It’s because something has changed in her that can’t be quantified or clarified by the amount of sex we will have in the future."
    "No matter how hard we try."

    play sound "phonebeep.wav"
    play music "wewereangels.mp3"

    sa "Hello?"

    "Which I’m sure will be very hard based on the current level of our respective libidos."

    s "Hey. What are you up to right now?"
    sa "I was...about to go to work..."
    sa "Are you coming tonight?"
    s "Is there any chance you could just...{i}not{/i} go to work? "
    sa "Is...uhh..."
    sa "Do you...need me for something?"
    s "Possibly."
    sa "May I...ask what it is?..."
    s "What do you {i}want{/i} it to be?"
    sa "..."
    s "..."
    sa "Let me call you right back."

    play sound "phonebeep.wav"

    "Sana hangs up the phone, giving me the opportunity to reach into my pants and make several much-needed adjustments that will prevent passersby from swarming me and seizing my body for their own use."
    "..."
    "I quickly undo the adjustments I made because that sounds fun and so far I’ve only had sex with people I know."

    play sound "phonering.mp3"
    $ renpy.pause(0.5, hard=True)
    play sound "phonebeep.wav"

    s "Hello?"
    sa "I told my mom I’m not feeling well."
    s "Awesome. Now I have someone to go to that brand new all-you-can-eat spaghetti buffet with."
    sa "Let me call her back again and tell her I’m okay now."
    s "Damn. I was also planning on breaking in my new mattress afterward, but I guess I can just find someone else to help me with that part."
    sa "Can we just...skip the spaghetti thing and go straight to that?"
    s "I {i}guess.{/i} How soon can you be at my place?"
    sa "Uh...twenty minutes? Should I...bring anything?"
    s "What would you even bring?"
    sa "I...uh..."
    sa "I actually...don’t know."
    s "No secret lingerie collection you’ve been hiding from everyone?"
    sa "I could...bring one of my old Halloween costumes?"
    s "On second thought, I think I’m just going to go to the spaghetti buffet alone and call it an early night."
    sa "I’ll come empty-handed! I promise! "
    s "Sa-"
    sa "No backing out! Goodbye!"

    play sound "phonebeep.wav"

    "Sana hangs up the phone and I make my way back to the house."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene sanatutoringlol1
    with dissolve2

    "After a worrying amount of pacing and some reflection on the damage I inflicted upon Miku the last time I stuck my dick in something way too small, the doorbell rings."
    "I may be about to break another vagina."

    play sound "dooropen.mp3"
    scene sanatutoringlol2
    with dissolve

    ni "..."
    s "{i}Oh.{/i}"
    ni "Well hi, Akira. I love you too."
    s "I didn’t realize you were going to be home so early."
    ni "Is it a {i}problem{/i} that I am home so early?"
    s "Uhh-"

    play sound "doorbell.mp3"

    ni "..."
    s "..."

    scene sanatutoringlol3
    with dissolve

    ni "Oh. I {i}see.{/i}"
    s "Uhh..."
    ni "Are you going to answer that?"
    s "It’s probably just a package."

    play sound "doorbell.mp3"

    sa "{i}Sensei...are you...are you home yet?{/i}"
    ni "..."
    s "I order all of my packages under the name “Sensei.” I’m sure you understand."
    ni "Why is a presumably teenage girl visiting you right now? And why did you need to be alone for it? "
    s "I-"
    ni "You?"
    s "...started tutoring again?"

    scene sanatutoringlol4
    with dissolve

    ni "Is that so?"
    s "Yes. That is the only reason a girl her age would have to come see me while Ami is not home. "

    scene sanatutoringlol5
    with dissolve

    ni "That's great, babe!"
    ni "Surely you won’t mind if I watch then, right?"
    s "Uhh..."

    play sound "doorbell.mp3"

    sa "{i}Should I...come back another time?...{/i}"
    ni "Great! I’m glad you agree. Let me run to the restroom and I’ll be right back to supervi- ahem. I’ll be right back to {i}watch{/i} you!"
    s "Niki-"
    ni "Nope! No red flags at all! Just another normal day at the Arakawa house!"

    scene sanatutoringlol1
    with dissolve

    ni "{i}Where my totally normal boyfriend gets visits from totally normal girls who are totally here to learn! How fun!{/i}"
    s "..."

    play sound "knock.mp3"

    sa "{i}Maybe the doorbell is just...broken?{/i}"
    s "Come in, Sana. It’s fine."

    play sound "dooropen.mp3"
    scene sanatutoringlol6
    with dissolve

    sa "Hey...I think your doorbell is-"
    s "The doorbell’s fine. But there’s been a change of plans."
    sa "If you’re nervous about it being my first time, don’t be. I want you to hurt me. "
    s "That’s not what I- "
    s "What?"

    scene sanatutoringlol7
    with dissolve

    sa "You can go as hard as you want without having to worry about my safety. I can handle it."
    s "Sana, I need to tutor you."
    sa "You sure do, Sensei."
    s "No, I mean I literally need to tutor you."

    scene sanatutoringlol8
    with dissolve

    sa "Why do you only exist to hurt me in the ways I do not {i}want{/i} to be hurt?"
    s "Listen, it’s not my fault. Niki came home early and now she probably thinks you came over here to have sex with me."

    scene sanatutoringlol9
    with dissolve

    sa "She’s right. I {i}did{/i} come over here to have sex with you."
    s "Yes, but she {i}can’t{/i} know that because it puts our relationship in jeopardy."

    scene sanatutoringlol10
    with dissolve

    sa "She doesn’t know about you yet?! How?! Everyone and their mother knows! Does she live under a-"
    s "{i}Sana, keep your voice down. Please.{/i}"

    scene sanatutoringlol11
    with dissolve

    sa "Sorry, I just...I thought I was one of the last ones and...I kind of assumed everybody else was just being...blissfully ignorant?..."
    s "I’m sure she {i}is{/i} being blissfully ignorant. But I would like her to {i}keep{/i} being blissfully ignorant as there is a level of {i}bliss{/i} involved that would quickly dissipate if she encountered me fucking a girl your size."
    sa "So it would be okay if I was taller?"
    s "No. By size I meant age. I just try to omit or disguise that when possible because it makes me feel gross."

    scene sanatutoringlol12
    with dissolve

    sa "That’s the best part, though."
    s "{i}What happened to you?{/i}"
    sa "Puberty is a violent beast, Sensei. Only you can tame me."
    s "God, you’re so hot now."
    sa "Would it help convince her if we let her join us?"

    play sound "dooropen.mp3"
    scene sanatutoringlol13 with dissolve

    ni "Okaaaay! Ready to finally witness you at {i}work,{/i} babe! Can’t wait to see how excellent and smart you are!"
    sa "{i}What if we just tied her up and threw her in the closet or something?{/i}"
    s "{i}How horny are you right now?{/i}"

    scene sanatutoringlol14
    with dissolve

    sa "{i}Very! And it’s all your fault! Now I have to learn?!{/i}"
    s "{i}Just...pick a topic and we’ll bullshit our way out of it. I’ll make it up to you next time.{/i}"
    sa "{i}Literature!{/i}"
    s "{i}Really? Why that?{/i}"
    sa "{i}Because I know you’ll fuck up everything else!{/i}"
    s "{i}I don’t think I’ve ever been more attracted to you before.{/i}"
    sa "{i}Thanks! I covered my eye again because I thought it would turn you on!{/i}"
    ni "Akiraaaaa! You’re not {i}fraternizing{/i} in there, are you?"

    scene black
    with dissolve

    s "No, Niki. I was just giving Sana the rundown on our tutoring session for today."

    scene sanatutoringlol15
    with dissolve2

    ni "Aaaahhh. {i}Sana.{/i} I’ve seen you around here before. How long have you been taking “lessons” from this doofus?"
    sa "Since...a couple Halloweens ago...but I kind of forced it on him since I...{i}really{/i} want to learn and...no one else is as...{i}smart...{/i}"

    "Right now, all I can really say is that Sana is lucky Niki is here because I would be wreaking havoc upon her if that was not the case."

    ni "Ooooooh?..."
    s "You sound skeptical, Niki."
    ni "I {i}am{/i} skeptical, Akira. You’ve been acting very suspicious lately. And between all of your “dates” and Ami’s entire...existence, I’m starting to worry you might be treading a very {i}risky{/i} and {i}dangerous{/i} path."
    sa "I’m confused...I..."
    sa "If you think I’m...attracted to Sensei at all, I..."

    scene sanatutoringlol16
    with dissolve

    sa "Actually think he’s...kind of gross and...way too old..."
    ni "Is that so?..."
    s "Even if it’s not...that was a little rude, don’t you think?"

    scene sanatutoringlol17
    with dissolve

    sa "Oh! S-Sorry! I just...I’ve never really...thought about you like that before and..."

    scene sanatutoringlol18
    with dissolve

    sa "It kind of...creeped me out a little...hearing you...suggest that maybe he’s been...looking at me...differently..."
    ni "If Akira’s not your type...what {i}is,{/i} Sana?"
    s "May I interrupt and just ask, “what does any of this have to do with tutoring?”"
    ni "You may, but I’m not going to answer. I have to vet this girl to make sure she isn’t just lying to me. So stay quiet and be good and I’ll give you a treat later."
    sa "Me?...Or...are you talking about-"
    ni "Akira, obviously. The kind of treat I’m talking about isn’t exactly something I can share with teenage girls."
    sa "That’s...a shame because...you’re actually...a lot closer to my type than he is..."

    scene sanatutoringlol19
    with fade

    ni "Oh?"
    sa "I’m actually...not interested in boys at all...and..."
    sa "I didn’t really know that until recently, but...I’ve always liked...more feminine types and...Sensei is just..."
    ni "As far from that as they come. I know."
    s "Hey, I’m not {i}as{/i} far from that as they come. I like some feminine things."
    ni "Like what? Me? You can’t even buy tampons for your daughter without having an existential crisis."

    scene sanatutoringlol20
    with dissolve

    s "Okay, but in my defense, I’m almost {i}always{/i} having an existential crisis. So that doesn’t say much."
    sa "Can you...please not tell anyone, Sensei?...About me and...how I feel about...you know..."
    ni "How do you feel about Ami specifically?"

    play sound "static.mp3"
    scene sanatutoringlol21 with flash
    stop sound

    sa "Huh?"
    ni "Is {i}she{/i} your type? Because it’d be super healthy for her to start pining after someone she isn’t literally related to."
    sa "Does Ami...even like girls?..."
    ni "She says she doesn’t, but I feel like it’s a front. And you seem weird and suspicious enough to check off {i}those{/i} boxes she apparently has if she’s into her father."
    sa "I...uh..."
    s "So, about {i}tutoring...{/i}"

    scene sanatutoringlol22
    with dissolve

    sa "I guess if...Ami wanted to, I...I wouldn’t mind...g...going out with her..."
    sa "I’d...want to move slow, though...so...I don’t know if she’d be...patient enough to...give up on Sensei..."
    ni "Hmmm..."
    sa "..."
    s "So, has she been successfully “vetted” yet? Will you leave us alone now? "
    s "Sana’s very clearly not comfortable when it comes to speaking and has a harder time absorbing information when there are others present."
    sa "It’s...true...Sensei has been helping me with that for...a long time now..."
    sa "It’s been a...major obstacle for me to...overcome and...and I’m feeling more confident now, but..."
    ni "I’ll keep my mouth shut and stop asking questions. I’m not going to leave, though."

    scene sanatutoringlol23
    with dissolve

    s "Niki-"
    sa "I-It’s fine, Sensei! She can stay! Just...we can pick up where we...left off...in that...one book you like, and...I’ll do my best to...not feel uncomfortable..."

    play sound "static.mp3"
    scene sanatutoringlol24 with flash
    stop sound

    "And so half an hour goes by as I sit there and bullshit about all I remember from the Lord of the Flies."
    "Without books or...any actual material to use though, it seems more like the world’s most boring open discussion than actual tutoring. And it’s clear that even Sana’s patience is beginning to wear thin."
    "Either that or she’s gotten uncomfortable sitting in a puddle of her own creation by now, infinitely waiting for me to put her out of her misery and hurt her how she {i}wants{/i} to be hurt."
    "In a way, I’m thankful that Niki would take it upon herself to wait here and make sure I {i}don’t{/i} do that."
    "But in another, much darker way, I’ve moved much closer to Sana’s earlier suggestion about tying her up and throwing her into the closet. {i}Or{/i} letting her join in."
    "That seems nigh impossible at this point though, if Niki’s trust in me has diminished to the point where she feels uncomfortable just leaving me alone with girls like Sana."
    "Is that my fault for how I handled Niki’s initial arrival? Probably. But I feel like some of the blame {i}has{/i} to lie with Sana too because of how cute she is."
    "Creepy, I know. But you’ve gotten used to that by now. Kind of like how Piggy had to get used to dealing with broken glasses until he was ultimately killed by a boulder."
    "I wonder if that will happen to me?"
    "I wonder if Sana {i}is{/i} the boulder? Because at one point, she {i}was{/i} the image of purity to me. There was no one more angelic than her."
    "But now, here she is — wholeheartedly embracing a facade I forced upon her all because she wants {i}me{/i} to force myself on {i}her.{/i}"
    "That innocence is gone. She is no longer an angel. She is no longer pure. But it’s quite possible she never {i}was{/i} to begin with. "
    "I just {i}wanted{/i} her to be."
    "Kind of like how Piggy wanted to not be killed by a boulder."

    s "...and for those reasons, I don’t think Jack was all that bad."
    sa "I...agree, Sensei..."
    sa "And thank you for...summarizing the entire book for me..."
    s "It is at this point that I will begin to break down each and every instance of symbolism from the book using nothing but my memory and superior intellect. "
    ni "Okay. I’m bored."

    play sound "static.mp3"
    scene sanatutoringlol25 with flash
    stop sound

    ni "You two keep doing what you’re doing. I’m going to take a shower."
    s "You’re not worried anymore?"
    ni "It’s become clear to me that between Sana’s lesbianism and your monologue about a bunch of kids trying to form a civilization that no one here is going to be doing anything inappropriate any time soon."
    ni "And also, if I have to listen to you talk about this book for more than another five minutes, I’m going to pass out and miss my dance class tonight."
    s "Oh. Okay. Have fun."
    sa "Take...your time..."
    sa "I’ll be...gone soon anyway..."

    play sound "dooropen.mp3"

    "Niki grabs a change of clothes from {s}my{/s} our bedroom before disappearing into the bathroom and turning on the water."

    scene sanatutoringlol26
    with dissolve

    "The sounds of the shower running quickly turn the otherwise silent house into..."
    "They..."
    "Uhh..."
    "The...sounds..."

    sa "..."
    s "..."

    $ renpy.end_replay()
    $ sanainvite1 = True

    jump sanainvite2

label sanainvite2:
    stop music
    play sound "static.mp3"
    scene sanacouchtime1 with flash
    stop sound
    play music "asobeatsex6.mp3"

    sa "{i}Finally...{/i}"
    s "Uhh...Sana?"
    sa "Yes, Sensei?"
    s "Niki’s still...just one door away..."
    sa "What’s wrong?...Worried I’ll be too loud?"
    s "I’m more worried that she’ll open the door and see you humping me just several minutes after you managed to convince her you were a lesbian."
    sa "Worry about that later. You’ve got a bigger problem on your hands right now."
    s "Is it...trying to satisfy your libido?"

    scene sanacouchtime2
    with dissolve
    play sound "zipper.mp3"

    sa "Close. It’s trying to fit your thick cock into my {i}little...{/i}virgin...pussy..."
    s "You’re...wait. Hold on. We’re just...jumping straight to that?"
    sa "You wasted all of our foreplay time convincing your girlfriend you don’t want to fuck me. We need to make up for it."

    scene sanacouchtime3
    with dissolve

    sa "Besides...we’ve already {i}serviced{/i} each other before...this is clearly the next step, isn’t it?"
    s "Yeah, but...are you sure {i}this{/i} is how you want to do it? Ayane had candles for her first time and...Chika had an entire vacation and..."
    sa "Are you {i}trying{/i} to make me jealous right now? "

    "A set of small fingers find their way to my dick, curling tightly around it before pressing the head up against her slit."

    sa "{i}Because it’s working...{/i}"

    scene sanacouchtime4
    with dissolve

    s "Sana...hold on. Since this is your first time, we should probably-"

    scene sanacouchtime5
    with dissolve2

    sa "{i}Haaah!{/i}"
    s "...oh my god. "
    sa "It’s in...you’re inside of me...you’re really inside of me..."
    s "Yeah, you...don’t have to tell {i}me{/i} that...I am {i}well{/i} aware..."

    scene sanacouchtime6
    with dissolve

    sa "Can I move?...I’m gonna move..."

    scene sanacouchtime7
    with dissolve

    sa "Aah...aah...haaah...aaaah...mmf...Sensei...mmm!"
    sa "You feel so good...oh...{i}fuck...{/i}finally...finally! My teacher...is fucking me...haah!"

    scene sanacouchtime8
    with dissolve

    sa "Hah..hah...and right next to his {i}girlfriend{/i} too...what a {i}bad{/i} man you are, Sensei..."
    s "Does that really...not hurt you?..."
    sa "It stings a little, but I like it...It’s nothing I can’t handle..."
    sa "You’re not...gonna make {i}me{/i} do all the work though, are you? Even after I gave you permission to fuck me as hard as you want?"
    s "Recent events have caused me rethink how I handle girls your size."
    sa "Are you {i}actually{/i} talking about size this time? Or are you worried you might hurt me because I’m an innocent little freshman?"
    s "I am {i}actually{/i} talking about size this time. I feel quite {i}packed{/i} into you right now, if you know what I mean."
    sa "Oh, I know what you mean...I can feel every inch of you...but I wanna feel {i}more,{/i} Sensei...I want you to {i}really{/i} hurt me..."
    s "Uhhh..."
    sa "Just do it like you did with Miku."
    s "Absolutely not. Also, why do you know about-"
    sa "Fine. I {i}will{/i} do all the hard work then. You’ll get into it soon enough."

    scene sanacouchtime9
    with dissolve

    sa "Mmngh! Mmm! That...feels so good! Oh my god...it’s so much better than I imagined...and I imagined it a {i}whole{/i} lot, Sensei..."
    sa "I can’t wait to be...your favorite new onahole...I can’t wait for you to...fuck me every single day..."
    sa "I want you to be...addicted to me...like I’m becoming...addicted to you..."

    "Soooooo..."
    "Yeah."
    "This is happening."

    scene sanacouchtime10
    with dissolve

    "And it’s..."
    "Surprisingly {i}amazing.{/i}"
    "Which isn’t to say I expected finally having sex with Sana to {i}not{/i} be amazing. But given what happened with Miku, I would have imagined a bit more of a...struggle."
    "Plus, girls can be a little clumsy during their first time — probably due to all of the pain. But Sana, light as her motions may be, grinds and bounces on me like she’s an expert at this sort of thing."
    "Maybe edging her with the Lord of the Flies for thirty minutes is just paying off in dividends right now. Whatever it is, though..."

    scene sanacouchtime11
    with dissolve2

    "I want more..."

    sa "Hah...hah...hi..."
    s "Hey..."
    sa "Am I...the new record holder?..."
    s "For?..."
    sa "The tightest little girl you’ve ever had the pleasure of splitting in two..."

    if amifingered == True:
        "Honestly? No. Miku still wins in that regard by a landslide. Followed by Ami. Then Maya. But seeing as this is a competition Sana wants to win, I’ll just let her have it."
    else:
        "Honestly? No. Miku still wins in that regard by a landslide. Followed by Maya. But seeing as this is a competition Sana wants to win, I’ll just let her have it."

    s "Yeah..."
    sa "That makes me really happy...and really {i}horny...{/i}"
    s "I can tell...you’re quite good at this for your first time. "
    sa "And you’re surprisingly gentle for your millionth..."
    s "You really want me to be rough with you, huh?"
    sa "This might be putting it lightly, but I want you to {i}destroy{/i} me."
    s "{i}That{/i} is putting it lightly?"
    sa "If I said what I really wanted to say, you’d cum right now. And I’m not done with you yet."

    "She speeds up, rhythmically grinding against me and sending my cock into a state of panic without anywhere else to move inside of her. "
    "And if it sounded like I gave my genitalia a mind of its own right there, it’s probably because I did. "
    "My mind wants nothing more than to be delicate with her so that I don’t destroy this new {i}onahole{/i} upon my first use of it. But my lower body seems to have a different idea of what to do with her."

    play sound "static.mp3"
    scene sanacouchtime12 with flash
    stop sound

    sa "Ah! Yes! Just like that! Yes! Sen-"
    s "Keep your fucking mouth shut or I’ll pull out right now. Do you understand?"

    scene sanacouchtime13
    with dissolve

    sa "Yes...Sensei..."
    sa "We wouldn’t want your girlfriend...catching you fucking a little girl when...she’s {i}already{/i} suspicious of you..."
    s "Not if you {i}really{/i} want me to get addicted, no."
    sa "Are you saying...hah...you’re not yet?..."

    "Faster still, she moves — tightening herself around my shaft as if to squeeze me out before I have the chance to hold back. "
    "Thankfully, I {i}have{/i} done this millions of times before."
    "And while that may lead to me letting my guard down every once in a while, I refuse to do that today until her eyes roll to the back of her head in agonizing pleasure."

    sa "How about...that?...Does my pussy feel good, Sensei?...You like it when I ride your big cock like that?"
    sa "I bet you do, huh? Hahah...I bet you want to choke me ‘til my face turns blue and fuck my little hole until I’m passed out...you’re such a pervert...you’re so gross...god, you’re so {i}bad...{/i}"
    s "You sure {i}I’m{/i} the pervert here? "
    sa "Duuuuh~ Which one of us is having their way with a little schoolgirl right now? I’m just young and horny...and desperate to feel better, Sensei..."

    scene sanacouchtime14
    with dissolve

    s "Looks like you’re going to be my little nympho from now on, huh?"
    sa "Hah! Hah! Yes! Any time you want...I’ll let you fuck my little pussy! I have to...catch up with...all the other girls!"
    s "Well, you’re making a good case for yourself right now. "
    sa "In school...at the bar...in the park...anywhere you want me...you can have me! I {i}want{/i} you to have me! I love it! I love your dick! I love your...big fucking dick!"
    s "What did I tell you about keeping your voice down?"
    sa "Sorry! I’m sorry! I can’t...help it! It feels so good! I’m so happy...you’re finally giving me...what I need! "
    s "And I’m so happy that-"

    stop music
    play sound "static.mp3"
    scene sanacouchtime15 with flash
    stop sound
    play music "iamhome.mp3"

    sa "Aaaah...aaaaah...mmmmn! Akira...A...kiraaa!"

    play sound "static.mp3"
    scene sanacouchtime16 with flash
    stop sound

    sa "Ohhhh FUCK! I’m gonna cum! You’re gonna make me fucking cum! Akira! Akiraaaaa!"
    s "...Sana?"

    play sound "static.mp3"
    scene sanacouchtime17 with flash
    stop sound

    sa "Huh?"
    s "..."
    sa "..."
    sa "{i}Sensei?.......{/i}"

    "I can smell hot pot."
    "I can feel linoleum pressed against my back as a girl, one much older now, rides me with the same passion and fervor I was in the midst of experiencing just moments ago."
    "I’ve been here before. Or I {i}feel{/i} like I’ve been here before."
    "It’s familiar in a way nothing ever is."
    "But what’s {i}unfamiliar{/i} is the way she looks at me. How the way her eyes meet mine makes it feel as if I’m falling in love for the very first time."
    "In this moment — I am home."
    "I am happy."

    s "..."
    sa "..."
    sa "I..."
    sa "I love you."
    s "I..."

    stop music
    play sound "static.mp3"
    scene sanacouchtime18 with flash
    stop sound
    play music "asobeatsex6.mp3"

    s "I love you..."
    sa "Hah! Hah! Hah! Haa-"

    scene sanacouchtime19
    with dissolve

    sa "...huh?"
    s "Sana, I..."
    s "I think I love you."

    stop music
    play sound "static.mp3"
    scene sanacouchtime20 with flash
    stop sound

    sa "You {i}what?!{/i}"
    s "I think...we might be meant for one another."
    sa "Uhh...that’s..."
    sa "That’s...a...{i}weird{/i} thing to say right now?"
    s "Is it? "

    scene sanacouchtime21
    with dissolve

    sa "Your dick is like...all the way inside of me. I can see it...poking out a little. I was just about to cum."
    s "And that’s the wrong time to tell you I love you?"

    scene sanacouchtime22
    with dissolve

    sa "It’s the wrong time to say {i}anything{/i} that isn’t about fucking me or how you {i}want{/i} to fuck me! Just fuck me!"
    s "Sana, I love you."
    sa "Sensei!"
    s "Is that all you have to say?"

    scene sanacouchtime23
    with dissolve

    sa "I mean...no! I..."
    sa "Uh..."

    scene sanacouchtime24
    with dissolve

    sa "{i}Thank...{/i}you?"

    "Oh. "
    "I really {i}am{/i} being used this time."

    s "Sana-"

    scene sanacouchtime25
    with dissolve

    sa "Oh, just shut up already!"

    play sound "static.mp3"
    scene sanacouchtime26 with flash
    stop sound
    play music "asobeatsex6.mp3"

    sa "Mm! Mmnch! Mmlm! Sensei! Harder...Harder!"

    "She takes the liberty of shutting me up herself...and I’m thankful for it."
    "Too many times, I’ve lost myself to delusions — said things directly {i}because{/i} of them and, sometimes, {i}done{/i} things as well."
    "Hell, I’m fresh out of a Christmas party where I was talking to cartoon characters for the majority of it."
    "But {i}this{/i} time, my delusions felt {i}less{/i} like delusions and more like..."
    "More like something else."

    scene sanacouchtime27
    with dissolve2

    "I close my eyes and kiss her back. It’s all I can do right now. But all I {i}want{/i} to do is crawl into a hole and die so she can just...have sex with my corpse or something. She probably would."
    "Despite my words clearly disturbing her, though, there’s no change in the way she moves."
    "She’s here to do a job. That’s it. That’s all it ever was."
    "That’s all it ever {i}will{/i} be too."
    "I focus on her body. How her pussy continues to tighten and grip me, desperately trying to milk me for every last drop."
    "Just a few more minutes now and she’ll succeed. I’m no longer interested in holding on."
    "I just want this to be over."
    "But at the same time, I want it to last forever."

    sa "Mm! Mmnch...mmlm! Mm! Sensei! Mm!"

    "She’s good at kissing too."
    "Just what else is she hiding from me?"

    with hpunch

    sa "Mmm!"

    "I grip her ass with all of my strength and begin to violently thrust into her. Even that probably isn’t rough enough for her, though."

    sa "Mm! Mm! I’m close!...I’m so close! Sensei!"

    "Stay with me and make me yours — my angel of death."

    s "Mm...mm...mmmm!"
    sa "Mnch!!! Mlm!!! Mnghhh!! Mmmnghhhh!!!"

    with sexfade
    with sexfade
    with cumflash
    with hpunch

    sa "Mmm! Mm.........mlm............mm?"

    stop music
    play sound "static.mp3"
    scene sanacouchtime28 with flash
    stop sound

    sa ".........."
    s "What’s wrong?"
    s "Are you bleeding? Is everything-"
    sa "Did you just...cum inside of me?"
    s "Uhh..."
    s "Was I...not supposed to do that?"

    scene sanacouchtime29
    with dissolve

    sa "You came inside of me?! Seriously?! Are you out of your mind?!"
    s "Sana, keep your voice down. Niki is-"
    sa "I’m in high school, Sensei! Are you trying to turn me into my mom?!"
    s "I...didn’t realize it would be a problem. Everyone else lets me do it all the time and-"
    sa "They do?! Are you {i}all{/i} out of your minds?!"
    s "I think most of them are just on birth control."
    sa "Well, {i}I’m{/i} not! And I’m not about to get pregnant because-"
    s "I can buy you something. Don’t worry. And...I’m sorry. "

    scene sanacouchtime30
    with dissolve2

    sa "Sorry?..."
    s "For...{i}everything{/i} apparently."
    sa "What do you mean “everything?”"
    s "For inviting you here without knowing Niki was coming back. For telling you I love you. For cumming inside of you without asking."
    s "I’m clearly just doing everything wrong today, so I might as well apologize for all of it."
    sa "It’s only the...last thing you need to apologize for. The other stuff is..."

    scene sanacouchtime31
    with dissolve2

    sa "{i}Hah...{/i}"
    sa "Sensei, you...don’t {i}love{/i} me. "
    sa "But I’m flattered you...felt good enough to maybe {i}think{/i} you did for a second or..."
    s "It wasn’t that. It was...something else. It was a lot of things. And lately, I-"

    play sound "dooropen.mp3"

    "The door suddenly opens. "

    play sound "static.mp3"
    scene sanacouchtime32 with flash
    stop sound
    play music "wewereangels.mp3"

    "And I imagine it’s the fastest either one of us has ever moved before."

    ni "Something is suspicious again."
    s "What do you mean? We’re exactly where you left us."
    ni "{i}Yes.{/i} But Sana’s face is very red and I’m almost positive the couch has moved several feet to the-"
    s "She’s been flustered ever since you got into the shower. We could hear you moving around all the way out here."
    ni "Really? I couldn’t hear anything in there. I guess that makes sense, though. I doubt there’s a lesbian teen in Kumon-mi who {i}wouldn’t{/i} look like that knowing I was naked just twenty feet away."
    s "I’m glad knowing I can just convince you of anything so long as I play into how great you think you are."
    ni "Hm? Did you say something, babe? I was just thinking about how great I am."
    s "Nope. And, in fact, we were just wrapping up here. Right, Sana?"
    sa "..."
    s "Sana?"

    scene sanacouchtime33
    with dissolve

    sa "Oh! S...Sorry...what?..."
    sa "I...I think I...zoned out for...a second..."
    s "{i}We were just wrapping up.{/i} Right?"
    sa "We...were?"

    scene sanacouchtime34
    with dissolve

    sa "Oh! I mean...y...yeah! Of course we were...I...know a lot more about the...Lord of the Size now-"

    scene sanacouchtime35
    with dissolve

    sa "FLIES! Lord of the...Flies. That...is the..."
    sa "That’s the name of the...uhh..."

    scene sanacouchtime36
    with dissolve

    sa "I have to go! Work! Bye!"

    play sound "doorslam.mp3"
    with hpunch

    s "..."
    ni "Lord of the Size, huh?"
    s "She meant flies. She said it herself."
    ni "..."
    s "..."
    ni "Akira...you know you can talk to me if there’s something you-"
    s "I’m fine, Niki."

    scene black
    with dissolve2

    s "Is the bath still full?"
    ni "Hm? Oh. No, I emptied it. You normally wait until later to-"
    s "I think I’m going to call it early tonight. I’ll probably be asleep by the time you get back from dance class."
    ni "You sure you don’t want to talk?"
    s "I’m sure."
    ni "{i}Hah...{/i}You and Ami are going to be the death of me, I swear."
    s "Probably not the best thing to say given our background."
    ni "That’s- oh. {i}Oh, shit.{/i} Baby, I’m-"
    s "It’s fine. Be more careful around Ami, though. Thanks."
    ni "Akira-"
    s "Goodnight, Niki."
    s "I’ll see you in the morning."

    play sound "dooropen.mp3"
    scene bedroom_noon
    with dissolve2
    stop music fadeout 10.0

    "I can’t help but sigh as I make my way into the room and stand before the bed, unsure of whether I want to collapse into it or try and suffocate myself with the pillow."
    "I think about sending Sana a text but ultimately decide against it. I’d rather she just forget everything."
    "I think I’d rather forget too."

    scene black
    with dissolve2
    play sound "tackle.mp3"

    "I choose collapsing over asphyxia."
    "Someone already took my breath away."

    $ renpy.end_replay()
    $ sanainvite2 = True
    $ sana_love += 1
    $ sana_lust += 1
    $ yukiblock = True

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "{i}Sana’s lust has increased to [sana_lust]!{/i}"
    "{i}You aren’t meant to be together!{/i}"
    "{i}She’s merely doing her job.{/i}"

    play sound "computeryay.mp3"

    if harukasex == False:
        $ harukaspring3miss = True

    "{i}But on the bright side, you can invite her over whenever you want now!{/i}"
    "{i}Hope you’re ready for her to ride your dick off!{/i}"

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

label beachsixsana1:
    scene sky
    with dissolve2
    play music "behindabathroom.mp3"

    "I decide to head over to the main section of the beach to try and track down the smallest and debatably horniest member of what was once (and still technically is) my class."
    "That second title is hotly contested nowadays. "
    "But I don’t mind handing it to Sana for the time being in hopes that it may give her new powers that she will subsequently use to squeeze me even tighter than she so typically does."
    "But of course, I must actually {i}find{/i} her first."

    scene sanalustnaming1
    with dissolve2

    "And also try to figure out why she would choose the only spot on the beach currently rivaling my bedroom in terms of popularity."

    s "Hey."
    to "Oh. Hello, Sensei. I didn’t realize you’d arrived."
    ya "I did! I can hear your veins from a mile away!"
    s "Well, can you hear Sana’s too? Because I’m looking for her for reasons I am currently unwilling to disclose."

    scene sanalustnaming2
    with dissolve

    to "Saying it {i}that{/i} way is as good of a {i}disclosure{/i} as anything."
    ya "Normally, I can. But today is different! There are lots of other noises. Ones I don’t normally hear. And they’re blocking out everyone but you!"
    s "Well, that’s great. I’m glad to know that you will be experiencing the sounds of my veins uninterrupted for the rest of the day. That is exactly what I wanted."

    scene sanalustnaming3
    with dissolve

    ya "See, Touka?! Sensei is happy! I {i}told{/i} you that hearing {i}some{/i} things was good! "
    ya "And now that I know I shouldn’t lock people inside of places, there is no way this can possibly go wrong! It’s just like what that floating caption from earlier said!"
    s "That’s not still flying around, I hope. It seemed like it was really gunning for Ayane earlier."
    to "Sensei — as you can see, Sana is not here. But I’ll be sure to inform her that you’re looking for her should she unexpectedly show up."

    scene sanalustnaming4
    with dissolve

    to "Or perhaps I won’t, and I’ll just let you think that I did. That seems like an easier way to keep others from getting their germs all over you, yes?"
    ya "I’ll tell her, Sensei. I’m not allowed to lie or my legs will be forcibly bent at ninety degree angles starting at the knee. And that would make me even more troublesome than I already am!"
    s "Got it. Well thanks, Yasu. And no thanks, Touka. Please avoid my room for the indefinite future."

    scene black
    with dissolve2

    to "Would {i}you{/i} mind avoiding your room as well? I can’t say I’m very fond of this group vacation devolving into yet another contest for your undivided attention. We have enough of those as is."
    s "Well, what would you have me do instead?"
    to "I’m not sure. Hide in the woods, perhaps?"
    s "Yeah, hate to break it you, but it’s not safe there either."

    scene sanalustnaming5
    with dissolve2

    "I search around for another five minutes or so, asking every other girl I can find if they’ve seen Sana, but apparently she’s just invisible now."
    "That or I misheard her, at least. But seeing as there is a threesome waiting for me, I don’t have the luxury to keep searching for the rest of the-"

    sa "{i}Psst!{/i}"
    s "..."
    s "Sana? Where are-"

    scene sanalustnaming6
    with dissolve

    sa "{i}Over here! Now, hurry up! Before someone sees you!{/i}"

    scene black
    with dissolve

    s "I mean...{i}okay.{/i} But I don’t understand why you’re being so-"

    play sound "static.mp3"
    scene sanalustnaming7 with flash
    stop sound

    s "Oh."
    s "Okay. I understand now."
    sa "So, umm...how do you feel about, like...exhibitionism?"
    s "Not as fanatical as you, apparently. Where’s your swimsuit? "
    sa "Around..."
    s "Shouldn’t you at least, like...keep it nearby? In case one of the six million people here happen to pass by this highly-traversed area?"

    scene sanalustnaming8
    with dissolve

    sa "And then what? Spend the entire time worrying about how quickly I can put it back on instead of focusing all of my energy on milking your massive cock with my cute little hole?"

    "So, remember earlier when I mentioned how Sana’s status as the horniest girl in my class was debatable? You do? Okay. Good. Just checking. You can weigh in however you’d like."

    s "You are playing with fire, Sana...this is a horrible idea."

    scene sanalustnaming9
    with dissolve

    sa "But you’ll play with me...won’t you, Sensei?..."
    sa "Your adorable, precious angel...who you raised all the way up from a shy little girl...is now brave enough to show her pussy in public...but only for {i}you{/i} of course..."
    sa "So, isn’t the {i}least{/i} you can do slamming me up against the wall and fucking my brains out while staring off into the sunset?"
    s "It’s daytime. The sun won’t be setting for at least, like...five more hours."

    scene sanalustnaming10
    with dissolve

    sa "Hm...Guess we better get started then!"
    s "Sana-"
    sa "The longer you wait, the likelier it is that we get caught and you get thrown into prison!"
    s "God, you are so lucky I am easy to persuade. Get on your knees."

    scene sanalustnaming11
    with dissolve

    sa "Anything for you...{i}Sensei.{/i}"
    s "Actually...wait."

    scene sanalustnaming12
    with dissolve

    sa "{i}Wait?{/i}"
    sa "You’re not...having second thoughts, are you? Because if you walk away now, I’ll cry out that you’re trying to rape me. "
    s "No, that’s not- sorry. You’ll do {i}what?{/i}"
    sa "You heard me. I haven’t fingered myself in a whole {i}week,{/i} and I will be damned if I let you walk away from here without cumming inside of me."
    s "You’re insane."
    sa "Probably, yeah."
    s "Anyway, that’s not what I was getting at. I just have something else I want you to call me from now on. During...stuff like this."

    scene sanalustnaming13
    with dissolve

    sa "Ooooooh...okay. Why didn’t you just say so?"
    sa "What is it then? What would you like to hear if {i}Sensei{/i} isn’t doing it for you anymore?"
    s "Well...what I’d like for you to call me is..."

    jump sanasexnaming

label sanasexnaming:
    $ sanamaster = renpy.input("Enter a name for Sana to call you...")
    $ sanamaster = sanamaster.strip()

    if sanamaster.lower() in ["sensei"]:
        s "Sensei. I want you to call me Sensei."

        scene sanalustnaming14
        with dissolve

        sa "But you literally {i}just{/i} said you want me to call you something else!"
        s "Sana, don’t yell. You’re going to get us caught."
        sa "No, {i}you’re{/i} going to get us caught by stalling like this! If it were up to me, we’d already be fucking!"
        s "Okay, well, now that we have reached a compromise, we can finally do that."
        sa "So I just...keep calling you Sensei then?"
        s "Correct. And {i}I{/i} keep calling you Sana."
        sa "Wonderful."

        scene black
        with dissolve
        play sound "zipper.mp3"

        sa "Then I will be removing this from your pants now."

        jump endofsanasexnaming

    if sanamaster.lower() in ["sara"]:
        s "I would like for you to call me Sara from now on."

        scene sanalustnaming15
        with dissolve

        sa "S...Sara?"
        sa "You...want me to use my mom’s name...on {i}you?{/i}"
        s "That’s right."
        sa "You are aware that my mother is a woman, right?..."
        s "Of course."
        sa "You are aware that she does not have a penis."
        s "Yes."
        sa "Yet, you want me to call {i}you{/i} by {i}her{/i} name while {i}your{/i} penis is inside of me."
        s "I’m really not sure what you’re not understanding here."
        sa "Do you {i}want{/i} her to have a penis?"
        s "Frankly, I don’t really understand why you’re obsessing over your mom right now. This is about you and me."

        scene sanalustnaming16
        with dissolve

        sa "{i}I’m{/i} obsessing?! You’re the one who wants me to call you Sara while I suck your dick!"
        s "Not {i}while{/i} you suck my dick. That takes away from valuable dick-sucking time."
        sa "This whole conversation takes away from valuable dick-sucking time! So choose another name so we can get on with it!"
        s "Ugh...fine. But only because you’re being so weird about it."

        jump sanasexnaming

    if sanamaster.lower() in ["ayane"]:
        s "Ayane. Call me Ayane from now on."

        scene sanalustnaming17
        with dissolve

        sa "If you want to involve Ayane, we can probably just ask her. You don’t have to steal her name."
        s "I want her to be involved in name only. {i}My{/i} name only. Because I am Ayane now and Ayane is someone else."

        scene sanalustnaming18
        with dissolve

        sa "Does this mean you’re my new roommate then?"
        s "No. That’s still Ayane."
        sa "I’m so confused. And I’m starting to think you’re just buying time until someone catches us."
        s "How funny would it be if that person was Ayane?"

        scene sanalustnaming16
        with dissolve

        sa "Not funny at all! So just choose something else already!"
        s "Tch. One would think you’d be a little more open to experimentation considering how naked you are in a public area right now."

        "It seems like Sana isn’t going to call me Ayane...What a fucking bitch."
        "I’ll have to choose something else."

        jump sanasexnaming

    if sanamaster.lower() in ["sana"]:
        s "Sana. From this point on, I am Sana."

        scene sanalustnaming19
        with dissolve

        sa "That’s it. I’m crying rape. I have suffered enough at the hands of your games."
        s "Just hear me out, okay?"
        sa "This better be good..."
        s "It’s a nice name."
        sa "..."
        s "..."

        scene sanalustnaming16
        with dissolve

        sa "What, that’s it?! {i}That’s{/i} what you asked me to “hear you out” about?!"
        s "Damn it. I figured that would work."
        sa "{i}Why?!?!?!{/i}"
        s "Because girls love compliments and I complimented your name. Which is also {i}my{/i} name now."
        s "So every time you’re like, “Oh, Sana! That feels so good!” you’ll be thinking about that one time I gave you a compliment and get more into it. Probably."

        scene sanalustnaming20
        with dissolve

        sa "Got it! Understood! Then I’m making {i}you{/i} call me Daddy!"
        s "That’s not my name, though. You’re completely misunderstanding what’s going on here, Sana."
        sa "{i}You’re{/i} Sana! I’m your daddy now! Got it?!"
        s "No. And honestly, you’re kind of scaring me right now."
        sa "Pick something else, {i}Sana!{/i} I don’t have time for your games."
        s "Ugh...fine. At least I got to hear it a couple times before you shattered my dreams."

        "Why is she so mean all of a sudden? This is totally unfair."

        jump sanasexnaming

    if sanamaster.lower() in ["daddy", "papa", "father", "dad"]:
        s "[sanamaster]. You’ve called me that before, I think. And I would like to hear it at least a thousand more times."

        scene sanalustnaming12
        with dissolve

        sa "Only a thousand? But that’s not-"
        s "{i}Today.{/i}"
        sa "..."
        s "..."
        sa "But that’s not that many."
        s "You plan on calling me Daddy over a {i}thousand{/i} times today alone?"

        scene sanalustnaming21
        with dissolve

        sa "Well, yeah...I never knew my dad. I need to make up for years worth of lost time."
        sa "And I guess that works out perfectly because I’ve already heard you’re trying to resolve everyone’s daddy issues today."
        s "How does word get around {i}so{/i} quickly with you girls?"

        scene sanalustnaming22
        with dissolve

        sa "Beats me...[sanamaster]. But you might also be happy to hear that my first instinct has {i}always{/i} been to call you that. I just hold it back most of time."
        s "What? Why?"
        sa "Because I like it when we cum together. And I don’t want you finishing prematurely when I play into your deepest, darkest fantasies."

        scene sanalustnaming23
        with dissolve

        sa "I guess it can’t be helped now that you’ve asked, though..."
        sa "Just know this, [sanamaster]. I won’t let you off easy if having such a tight little girl call you [sanamaster] makes you finish before {i}I’m{/i} ready. Your daughter has needs of her own, you know."
        s "A surprising amount of them at that."

        scene sanalustnaming22
        with dissolve

        sa "I must get it from you..."
        sa "Now...are we finally ready? Because if I have to stand here any longer knowing we could be caught any second now...I might just wind up playing with {i}myself.{/i}"
        s "No need...and as I was saying earlier-"

        scene black
        with dissolve2
        play sound "zipper.mp3"

        s "Get on your knees..."

        jump endofsanasexnaming

    if sanamaster.lower() in ["oniichan", "onii-chan", "big brother", "big bro"]:
        s "I want you to call me [sanamaster] from now on. Understood?"

        scene sanalustnaming24
        with dissolve

        sa "Uhh..."
        sa "May I ask {i}why?...{/i}"
        sa "Like...is this because of a little sister kink or...do you just...get harder for girls who are on the verge of crying? Because I’m...fine with either, just-"
        s "Sana, if it makes you uncomfortable-"
        sa "I’m not uncomfortable..."
        sa "Like I said, I’m...fine with it. Really...I just...want to understand."
        sa "Because you know what my brother’s death did to me and...I don’t {i}think{/i} you’d try and hurt me on purpose...but it’s kind of just...I don’t know. Unexpected?"
        s "I don’t think it’s {i}that{/i} unexpected. There’s a clear age gap at play here. And we’re obviously both perverts if you’re going to come out here naked in the middle of the day."
        s "So why not feed into that depravity even further by having me assume the role of someone so important to you while defiling every inch of your body?"

        scene sanalustnaming25
        with dissolve

        sa "I...feel very conflicted about...how hot that sounds..."
        sa "But Sensei...you can’t ever...fill his role..."
        sa "I loved him differently than I...uh..."

        scene sanalustnaming26
        with dissolve

        sa "Uhh...a...anyway! [sanamaster]! Right?! Hahah..."
        s "Sana...Were you just about to-"
        sa "About to what? Nope! Probably not. Hahah! So...on my knees! Right, [sanamaster]? On it!"

        scene black
        with dissolve

        s "Sana-"

        play sound "zipper.mp3"

        sa "I said “on it!” Just...let’s do this already!"

        jump endofsanasexnaming

    if sanamaster.lower() in ["shota"]:
        s "Shota. I want you to call me Shota from now on."

        scene sanalustnaming27
        with dissolve

        sa "Sh...Shota?..."
        s "Is there a problem with that?"
        sa "Where...did you hear that name?"
        sa "Did...did my {i}mom{/i} tell you, or-"
        s "It’s just a name. There’s not really any significance to it."
        sa "There..."

        scene sanalustnaming28
        with dissolve

        sa "There is to me, though...and I’m...not really comfortable with that."
        sa "Sorry..."
        s "Oh. Uhh...okay. I guess I can...choose something else then."
        sa "Sensei, you..."
        sa "Did you really not know?"
        s "Know what? I’m so confused."
        sa "Mm..."
        s "..."
        sa "..."
        sa "Then..."
        sa "Do you ever feel like someone else is making choices {i}for{/i} you?"

        menu:
            "No":
                s "Of course not. That’s ridiculous."

        sa "...Yeah."
        sa "Yeah, it is."

        "Seems like Sana has a problem with the name I chose. I’ll have to think of another."

        jump sanasexnaming

    if sanamaster.lower() in ["spaghetti"]:
        stop music
        play sound "static.mp3"
        scene sanalustnaming29 with flash
        stop sound
        play music "letsfuckingo.mp3"
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming30
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming31
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming32
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming29
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming30
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming31
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming32
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming29
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming30
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming31
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming32
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming29
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming30
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming31
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming32
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming29
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming30
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming31
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming32
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming29
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming30
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming31
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming32
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming29
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming30
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming31
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming32
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming29
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming30
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming31
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming32
        $ renpy.pause(0.5, hard=True)
        scene sanalustnaming29
        $ renpy.pause(0.5, hard=True)
        stop music
        play sound "static.mp3"
        scene sanalustnaming12 with flash
        stop sound
        play music "behindabathroom.mp3"

        sa "Sensei?..."
        sa "Is everything okay?"
        s "No, Sana. It never is."

        "What was I thinking? I can’t have her call me {i}that.{/i}"

        jump sanasexnaming

    else:
        s "[sanamaster]. I’d like for you to call me that from now on."

        scene sanalustnaming9
        with dissolve

        sa "Sure...I don’t have a problem with that."
        sa "Are there any {i}other{/i} requests you have for me? Or will you finally give me what I want?"
        s "I’ll give you exactly what you want. I’m just having trouble remembering what my first command was before we got...sidetracked."
        sa "Hmm..."

        scene black
        with dissolve2
        play sound "zipper.mp3"

        sa "I believe you may have commanded me to get on my knees..."

        jump endofsanasexnaming

label endofsanasexnaming:
    "........."
    "......"
    "..."

    scene sanalustnaming33
    with dissolve2

    sa "Mngh! Mnglhlgh...mmff! Mmnghhh! Ahnmf...ahhnn....mglppp....mnch...mmh! Mhhh! Mmnnchhhglplgp!"

    "Sana drops to the ground and wastes no time at all in opening her mouth as wide as she can to begin servicing me...And then subsequently herself as she spreads her legs and begins to masturbate."
    "Using both hands, I grip her head and thrust violently into her mouth, silently praying that today isn’t the day her body decides to give out from a little rough play."
    "And by a little I mean a lot. Because not only am I too turned on right now to even {i}consider{/i} taking my time, but I’m doing this {i}in public.{/i}"
    "And all it would take for things to come crashing down is one poorly timed moan or an unlucky glance."
    "But of course...that makes this all the more arousing. And at least the surrogate mother of my daughter isn’t here to catch us this time."

    ima "{i}Futaba! Could you come here for a sec?!{/i}"

    "Imani is, though. And Touka. And Yasu. And Nodoka. And apparently Futaba too."
    "The amount of people who {i}could{/i} see me using this girl like my own personal toy is at an all-time high."
    "Yet...I can’t stop. I {i}have{/i} learned and {i}will{/i} learn nothing."
    "So I surrender my body to auto-pilot, and I let Sana do the same with hers."

    sa "Mngh! Mmnh! [sanamaster]! Mnlngh! Fuck...my mouth! Harder! {i}Harder!{/i}"

    "Sana — forgive me in advance for the things I am about to say. Even if you’ll probably like them."

    s "Yeah, you fucking like that...don’t you, little girl? How’s a...precious thing like you become such a fucking...whore overnight? Huh? Is that {i}my{/i} fault? Or do you just take after your mom?"

    scene sanalustnaming34
    with dissolve

    sa "Mmnh!"
    s "Look at you...sucking your teacher’s cock behind a fucking bathroom...shamelessly playing with yourself for the whole...fucking world to see!..."
    s "And the best part?...I bet you’d be...doing the same fucking thing...if I was a complete stranger! I just got...lucky today...didn’t I?!"

    scene sanalustnaming35
    with dissolve2

    sa "MNCKKHCH! MMHHNGHGG! BBBLCKCHKK!"

    "Her eyes begin to roll to the back of her head as she puts her entire arm into pleasuring herself."
    "And if it weren’t for the sounds of her choking on my dick, I imagine I’d be able to hear what she’s doing to herself down there too."
    "Drool coats my shaft as her face glows a brighter shade of red — nipples hardening with each and every pump I force down her throat."

    s "That’s right...open wider, you filthy pervert. You’re gonna need to work harder if you want to make me cum like this...You’ve barely got half of it in there..."
    sa "Mllghghgh...mmmmhh!~"

    "I persist through the gagging...bringing her to the brink of unconsciousness as she struggles to breathe through her nose. Yet she doesn’t try to pull away. Just fingers herself harder. Faster."
    "Praying for me to take the place of the tiny prehensile fleshworms attached to her hand."
    "Sorry. That one was weird. I’m kind of new to this level of verbal debauchery."

    s "Wider...wider, you fucking whore! What good are you if you can’t take all of it?! Why shouldn’t I just toss you aside and go fuck one of your friends, huh?!"

    scene sanalustnaming36
    with dissolve

    sa "MNHH! MNGH! MMNHHH! MMNHHHH!!!!!!"
    s "Are you fucking {i}cumming?{/i} Already? Jesus fucking Christ, you’re even worse than me..."
    sa "MMHHH! MHMMM! MNHGHHHH! MMLMMHMGHMMGMLLLHH!!!!!"

    scene black
    with dissolve2

    sa "MMMMMMMMNNNNNGGHHGHGHGHGHGHH??!?!?!?!?!!!!!"

    "........."
    "......"
    "..."

    scene sanalustnaming37
    with dissolve2

    to "Oh, it appears that Miss Imai’s beach volleyball tournament is going to begin soon. I wonder how different the rule-set is from standard volleyball?"
    to "Perhaps I should enter and show off my athleticism?"

    scene sanalustnaming38
    with dissolve

    to "I wonder if that has something to do with why Sensei was searching for Sana. Do you think the two of them are on the same-"
    ya "..."

    scene sanalustnaming39
    with dissolve

    to "Is...Is something the matter, Yasu?"
    ya "I was wrong..."
    ya "It isn’t good to hear things..."

    play sound "static.mp3"
    scene sanalustnaming40 with flash
    stop sound

    sa "AAAAH! AAAAH! [sanamaster]! C...Careful!!! It’s...too good! I’m getting...too loud! Someone...will find us! Aaah! AaaAaAAAaaHHHHH!!!"
    s "Look at you pretending that you {i}don’t{/i} want that to happen! You know...damn fucking well that you want {i}everyone{/i} on this beach to watch me devour your needy little cunt!"
    sa "Aaah! AAAAH! Y...Yes! I do! But...aaah! S...Seriously! It’s too...good! You’re going so...hard today! I can’t...take it anymore!"
    s "Like I give a shit what you {i}can{/i} and {i}can’t{/i} take. If you’re gonna march out here completely fucking defenseless, you’ve got no right to tell me when to stop..."
    sa "Aaah! Right! You’re...so right...[sanamaster]! I won’t...fight back anymore! I’ll be a good little...cock sleeve for your...huge...throbbing dick!"
    sa "Oh fuck! Oh...fuck! I’m cumming again! I’m...CUMMING! AHH! AAAAAAHHHHH!!!"

    play sound "static.mp3"
    scene sanalustnaming41 with flash
    stop sound

    sa "{i}{size=-25} AAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!{/size}{/i}"
    to "Oh, splendid! It appears as if the first match is about to begin."
    to "It’s such a shame that we didn’t sign up on time. But maybe next year we can-"
    ya "Touka...I don’t feel so good..."

    scene sanalustnaming42
    with dissolve

    to "Yes — and I can’t say you {i}look{/i} very good either. I do hope you’re not coming down with a fever. You’d miss out on all of the festivities."
    ya "Do you..."
    to "Do I...what?"
    ya "Do you...have headphones I could borrow?"

    play sound "static.mp3"
    scene sanalustnaming40 with flash
    stop sound

    s "What are you?!"
    sa "Aaah! Aaah! A whore! A little teenage whore! A slut! Trash! A despicable meat toilet! Every bad word you could possibly think of! Just fucking cum inside of me already! Please!"
    s "I don’t know, Sana. You gave me hell the first time I did that. I’m not sure I want to anymore."
    sa "I’M...SORRY! I WASN’T...THINKING! BUT NOW MY...AAAH...MIND IS...AS CLEAR AS EVER!!!"

    "She squeezes me like a vice grip, desperately trying to force an orgasm out of me as I keep her pressed against the wall, unable to escape."
    "It’s just the way she likes it...and it’s just the way {i}I{/i} like it too. But that’s a dangerous line of thinking. And one that sneaks in far too often nowadays."

    sa "Oh my fucking {i}GOD{/i} it’s so deep! Oh my...ngh! Aaah! I’m not sure if...ngh! If this is...safe...anymore!"
    s "You’re not telling me to {i}stop,{/i} are you? You think you can do that, Sana?"
    sa "Ngh! Mmngh! N...No! Of course not! Just...aaah! It hurts! It hurts, [sanamaster]! You’re so much...bigger than me! I’m just a...little girl! My pussy...can’t handle so much torture!"

    "She squeezes me again and nearly sends me over the edge. I need to bite my lip to prevent myself from ejaculating."

    sa "Aaah! Yes! I can feel it! Give it to me! Give it to me, [sanamaster]!"
    s "Call yourself a whore again..."
    sa "I’m a whore! A fucking pathetic teenage whore!"
    s "{i}Whose{/i} whore?"
    sa "Yours! Only y-"

    scene sanalustnaming43
    with dissolve
    with hpunch

    sa "HYAAAH?!"
    s "Liar! You’d say that to anyone! {i}That’s{/i} what a fucking whore is! Isn’t that right, Sana?!"
    sa "AAAH! AAAH! I’m gonna cum again! [sanamaster]! P...Please! Fill me up! Fill me up! Cum inside me and leave me here to rot like the horny bitch I am!"
    s "Then fucking...promise me something! Can you...fucking do that?! HUH?!"
    sa "YES! YESSSS! ANYTHING! AAAH! JUST...NAME IT!"
    s "Then...never..."
    s "LEAVE...ME!!!!!"

    with sexfade
    with sexfade
    scene sanalustnaming40 with cumflash
    with hpunch

    s "NGHHH!!!!"
    sa "AAAAH! HAAAH! NGHHHHHHHHAAAAAAHHHH!!!!"

    scene sanalustnaming44
    with dissolve2

    sa "{i}Aaah.....aaaaahhh~{/i}"
    sa "Oh god...mnh...I can feel it...{i}all{/i} of it...it’s so...haaah...{i}hot...{/i}"
    s "Mngh......hah......haahh...."
    sa "You finished...before...I could respond..."
    s "Mngh.........mnh......."
    sa "I.......promise.....[sanamaster]....."

    stop music fadeout 10.0
    scene black
    with dissolve2

    sa "I’m not......going anywhere......"

    $ renpy.end_replay()
    $ beachsixsana1 = True
    $ sana_lust += 1

    "{i}Sana’s lust has increased to [sana_lust]!{/i}"
    "........."
    "......"
    "..."

    "Somehow, by some sort of miracle, Sana and I remain undetected."
    "But I am disappointed in myself."
    "Because I tried to be strong...just to fail at the very end."
    "And I have once again successfully lost what it means to be a man."
    "My mind hones in on one thing and one thing only."
    "I must continue to devour. I must continue to collect."
    "Who is next?"

    jump beachsixsexmenu
