label osakodojo:
    if osako_love >= 1 and osakodojo1 == False:
        jump osakodojo1
    if secondbeach18 == True and christmastwo20 == False:
        scene dojo
        with fade
        play music "sakuya4.mp3"

        "I head over to the dojo, but Osako isn't there."
        "I wind up wasting the afternoon in hopes that she'll show up."

        scene black
        with dissolve

        "........."
        "......"
        "..."

        jump saturdaynight
    if day > 5 and beachfive16 == True and karinspring4 == False:
        jump karinspring4
    if chap4active == True:
        jump osakospringdojogen
    if chapthreeactive == True:
        jump osakosummer2dojogen
    else:
        jump osakodojogen

label callosakomorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I tap on Osako's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callmorning

label osakodive:
    if chap4active == True:
        jump osakospringdivegen
    else:
        jump osakospringdivegen

label callosakoafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    else:
        play sound "phonebeep.wav"

        "I tap on Osako's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callafternoon

label callosakonight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    else:
        play sound "phonebeep.wav"

        "I tap on Osako's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."
        jump callnight

label osakodojogen:
    scene osakodojogen
    with fade
    play music "sakuya4.mp3"

    "I make my way over to the dojo to practice karate with Osako."
    "Just kidding."
    "I actually came here to slack off and closely monitor all of the girls actually trying to learn a martial art in hopes of catching a glimpse of a wardrobe malfunction or two."
    "As you may be able to tell, Osako does not like that part of me very much."
    "In fact, she dislikes it {i}so{/i} much that she proceeds to make a laughing stock of me in front of everyone by body slamming me onto the floormat and sitting on me for a full twenty minutes."
    "I have no idea how someone so light can have so much power- and I am also afraid to ask as I fear it would just lead to me being hit again."

    scene black
    with dissolve

    "Osako ultimately decides to spare my life and allows me to sit through the rest of the class without physically abusing me again."
    "That is, until she catches me staring at {i}her{/i} and then decides that my punishment is nowhere near complete."
    "And, in other news, I really don't understand why I keep coming here."

    $ osako_love += 1
    stop music fadeout 5.0

    "{i}Osako's affection has increased to [osako_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label osakodate1:
    if bonus == True:
        "Osako, who must now distract herself from the idea of being tied up and teased by her girlfriend later tonight, exits the apartment by my side and leads me down the stairs."
    else:
        "Osako, who must now distract herself from the thought of her girlfriend doing the Fortnite dance, exits the apartment by my side and leads me down the stairs."

    "Just like she said, it’s not a far walk as I can already make out the light of the convenience store from around the corner."
    "........."
    "......"
    "..."

    scene osakoconvenience1
    with dissolve2

    os "So..."
    os "Can’t really say I expected to find myself out with you of all people on my anniversary."
    s "Hey, you’re the one who invited me. I was more than willing to go home."
    os "I know, I know."
    os "It’s just..."

    scene osakoconvenience2
    with dissolve

    os "It’s the first time Wakana’s ever gone out of her way to contact anyone who isn’t me, I think."
    os "Normally she’s just all like-"

    scene osakoconvenience3
    with dissolve

    os "Why would I expel the energy necessary to call someone when I have absolutely nothing to gain from doing so?"
    s "Wakana would say {i}that?{/i} No way."
    s "That’s impossible."

    scene osakoconvenience4
    with dissolve

    os "It was just a little weird, you know? "
    os "Like, I’m glad that she finally has a friend and whatnot, but it’s just..uncharted territory, I guess."
    s "We’re not particularly close or anything, if that’s what you’re worried about."
    s "I normally wait until a person’s significant other is in space before I think about making a move on them."
    s "And even then it’s a sort of case by case basis."
    os "Is that supposed to make me feel more comfortable about this?"
    s "If you’re uncomfortable as it stands, isn’t that on you in the first place?"

    scene osakoconvenience5
    with dissolve

    os "Of course it is. It’s just..."
    os "I’m totally in love with Wakana and, despite her tendency to repeat the same thing over and over and over, she’s always been a little unpredictable."
    os "Like she doesn’t completely understand how other peoples’ feelings work. Myself included."
    os "But she tries for me, at least. And I love that about her just like I love everything else."

    scene osakoconvenience6
    with dissolve

    os "Shit, what am I even saying right now? You don’t want to hear about this."
    s "I don’t...{i}not{/i} want to hear about it either."
    s "You said you had something to talk to me about, so I figured through context clues that it would just be you ranting about how much you love goth girls for a few minutes or something."

    scene osakoconvenience7
    with dissolve

    os "Not just {i}any{/i} goth girls, dick. Wakana specifically. "
    os "Frankly, I’m still surprised she even settled for me in the first place considering that my style is essentially the polar opposite of hers."
    s "You’re both cute in your own ways."

    scene osakoconvenience8
    with dissolve

    os "Stop calling me cute or I’ll break your kneecaps."
    s "I’m sorry."
    s "Can I still call your girlfriend cute, though? Or is that off limits too?"
    os "You can call her whatever you want so long as you don’t try to make any actual moves on her."
    s "You’re not afraid she’d actually go along with it, are you? Because she clearly likes you a lot if she’s going to ask people for help just to try and cook something for you."

    scene osakoconvenience9
    with dissolve

    os "I like to think that too."
    os "But...I don’t know."
    os "Even though we tell each other we love one another all the time, she still feels weirdly distant on occasion."
    os "And, it’s probably self-explanatory due to the whole karate thing, but I have a tendency to be a little...defensive, I guess."
    os "Not just with myself but with anything I want to protect."
    os "And I swore back in college that I’d protect her for the rest of my life, even if she didn’t want me to."
    s "So, if she never accepted your confession, you’d just...stalk her every hour of every day and defend her from anyone who tried to get close?"
    os "Yeah...probably...I don’t know."
    s "Well, that’s not creepy at all."

    scene osakoconvenience10
    with dissolve

    os "I can’t help it, okay?! "
    os "Wakana’s not like a normal person! She’s like a...scared little puppy that you need to be really gentle and careful with if you ever want her to warm up to you!"
    s "I mean, I never had to do that."

    scene osakoconvenience11
    with dissolve

    os "That’s...exactly why I feel so weird about all of this."
    os "And a big part of why I wanted to talk to you."
    os "For some reason, Wakana warmed up to you almost right away."
    os "Way quicker than she did with me and the two of us are in an actual relationship now."
    os "So I can’t help but overthink that since it’s just...a brand new thing I’ve never had to deal with."
    s "I’m not going to steal your girlfriend, Osako."

    "Probably."
    "Especially since I’d likely die the second I tried anything."

    os "It’s not just the actual act of you “stealing” her. It’s a...fear I have that maybe she’ll realize that she wants something else."
    os "And that we’ll revert to being friends or something if she starts thinking that things aren’t as good as they could be with a different person."
    s "I’m going to be honest, you were the last person I thought I’d have to coach some self-esteem back into."
    os "I’m going to be honest too and say that you’re the last person I thought I’d ever have to talk to about this."
    os "Just being strong physically doesn’t make me strong as a person, you know. I’m actually annoyingly sensitive when it comes to stuff like this."
    os "Wakana’s the tough one. But I think a lot of that is just because she doesn’t really see the world the same way most other people do."
    s "..."
    os "..."

    "We’ve already made it to the convenience store, but have yet to set foot inside and disturb the employees with our decently personal conversation."
    "A conversation I had a feeling was going to be inevitable from the moment I got Wakana’s phone number."
    "I’m not entirely used to engaging in relationships with people whose significant others are not {i}missing{/i}, so at least I can be glad this is happening now rather than later."
    "Preferably, I’d like if it wouldn’t happen at all."
    "But not even my life can be as convenient as that."

    s "I have a question for you."

    scene osakoconvenience8
    with dissolve

    os "You do? About Wakana?"
    s "More or less."
    s "My question is...if you really do care about her, shouldn’t you {i}want{/i} her to figure out whether what she truly wants is you or not?"

    scene osakoconvenience12
    with dissolve

    os "I do. But that doesn’t mean I’m not going to worry about it as well."
    os "She’s everything to me. And the thought of that changing is just..."
    s "Let me clarify that I don’t think you need to worry about that. "
    s "I haven’t known Wakana for long, but the things she said about you today made me realize that she’s so into you that she wouldn’t even consider romance with someone else."
    os "Consideration doesn’t really have anything to do with it."
    os "Wakana’s not as...calculated as she might make it seem. She’s actually pretty neurotic and impulsive at times. "
    os "She can think one thing but then do something else. And things like that aren’t always easy to suppress, which is why I’ve always kept a close eye on her."

    scene osakoconvenience13
    with dissolve

    os "Well...I kept a close eye on her even before I knew that because...holy shit, she’s so hot. "
    os "But yeah. "
    os "I guess I just think everything right now is a little too good to be true."
    os "And that one day she’ll snap out of what’s been such a happy dream for me and move onto bigger and better things."

    scene osakoconvenience14
    with dissolve

    os "I don't know."
    os "Sorry for springing this on you out of nowhere. I’m just really afraid of losing her and...I guess I wanted you to know that?"
    s "Why are you wording that like a question?"

    if bonus == True:
        os "Probably because I still don’t understand {i}why{/i} I wanted you to know that when you’re already fucking Ayane."
    else:
        os "Probably because I still don’t understand {i}why{/i} I wanted you to know that when you’re already Ayane's hug partner."

    s "..."
    os "..."
    s "I’m-"
    os "You totally are."
    s "You don’t-"
    os "Don’t even try to deny it. It’s so obvious."
    s "..."
    os "..."

    scene osakoconvenience15
    with dissolve

    if bonus == True:
        "Damnit, Ayane."
        "Why must your love for me be so powerful?"
    else:
        "I do really love her hugs."

    os "I’m also a little mad that you got to see Wakana in an apron. I wanted that to just be a {i}me{/i} thing."
    s "She looked surprisingly...homely for a woman who would likely have trouble microwaving instant ramen."
    os "And on that note, we should probably head inside so we’re not out here looking like we actually enjoy each other’s company."

    scene osakoconvenience16
    with dissolve

    s "Wait...are {i}both{/i} of you tsundere?"
    os "Hm? Wakana, maybe a little bit. "
    os "But you’d absolutely know if I had any feelings for you. I make very little effort to actually hide them."
    s "This hurts me. "

    scene osakoconvenience17
    with dissolve

    if bonus == True:
        os "Well, sorry to hurt ya even more, but that weird banana shaped muscle you’re already sharing with Ayane would be a no-go for me in the first place."
    else:
        os "Well, sorry to hurt ya even more, but I'm not into guys in the first place."

    s "So it’s not just me, it’s men in general."
    s "That somehow makes me feel a little bit better."
    os "It’s also kinda you. "
    os "You’re fine to talk to...but even if I did like dudes, you're too much of a wimp."
    s "..."
    os "..."
    s "Okay, time to shop."

    scene black
    with dissolve

    "Osako and I enter the convenience store and I can immediately tell just how often she does this."
    "She moves through the narrow aisles with surgical precision, placing ingredients neatly into a basket that she grabbed just beyond the store’s automatic doors. "
    "There’s little to no conversation on the inside, which I imagine is due to the fact that we last left off on the...sheer concept of penises."
    "But, at the same time, I feel like Osako has already said everything she wanted to say in the first place."
    "She’s madly in love with Wakana Watabe. This much is entirely irrefutable."
    "In fact, even if the two of them wound up breaking up, I can see Osako sitting quietly on a porch somewhere, growing old and withering away while thoughts of Wakana still dance around in her head."
    "I wonder if I’ll ever be able to feel that way about anyone."
    "And then I think about all of the people who feel that way about me."
    "It ruins my night."
    "........."
    "......"
    "..."

    scene osakoconvenience18
    with dissolve

    os "Okay! Now we’re ready to make actual soup that isn’t filled with Jell-O."
    s "Oh, am I coming back with you?"
    os "Nope! By “we” I meant Wakana and I."
    s "Wakana and {i}me{/i}."
    os "Fuck off. Only Wakana can correct {i}I{/i}."
    s "Now you’re just fucking with me on purpose."
    os "Damn right me am."

    scene osakoconvenience19
    with dissolve

    os "Thank you, though."
    os "Not just for hearing me out, but for being a friend to the girl I love more than anything else in the world."
    os "And remember...if you {i}do{/i} try anything, I know of seven different pressure points on your body that could kill you instantaneously."
    s "There is no way that’s true. "
    os "Play your cards right and you’ll never have the displeasure of finding out!"
    s "It’s terrifying how you can smile like that while threatening to kill me."
    os "If it’s to protect my cute little fallen angel, I can do anything."

    if bonus == True:
        s "You mean anything except feeling totally comfortable with her associating with someone of the opposite sex because you’re afraid she’ll suddenly discover how awesome she thinks penises are."
    else:
        s "You mean anything except feeling totally comfortable with her associating with someone of the opposite sex."

    scene osakoconvenience20
    with dissolve

    os "Okay, now you’re just being an asshole."
    s "I’m always an asshole. You just don’t have enough experience with me to realize that."
    os "I have even more experience with you than Wakana does. I’ve been giving you karate lessons for like...I don’t even know how long now."
    s "Correction- you’ve been {i}trying{/i} to give me karate lessons. "
    s "You have yet to succeed."

    scene osakoconvenience19
    with dissolve

    os "Oh yeah? Looks like I might have to try a little harder next time, then."
    os "Hope you’re ready to feel sore all over for the next year."
    s "What are you going to do to me?"
    os "Hm. Maybe reveal one of those seven pressure points?"
    s "If I delete Wakana’s number from my phone, will you allow me to keep my life?"

    scene osakoconvenience21
    with dissolve

    os "You don’t have to stop talking to her or anything, dude."
    os "Just...keep in mind that she’s everything to me. And that without her I’d be absolutely nothing."
    s "Sounds good. "

    if bonus == True:
        s "Anyway, enjoy getting tied up and edged tonight."
    else:
        s "Anyway, enjoy combing your girlfriend's hair and doing a whole bunch of other cute feminine things I only kind of want to be included in."

    scene osakoconvenience22
    with dissolve

    os "I will, thank you very much!"

    if bonus == True:
        os "And I hope {i}you{/i} enjoy sexting one of your students!"
        s "I don’t really do that. I much prefer actual physical-"
    else:
        s "Do you think that maybe someday I could...also drop by and-"

    os "Die!"

    if bonus == True:
        os "I mean...bye!"
        os "Go away!"
    else:
        s "I'm sorry...I just wanted to feel included once..."
        s "I am very uncomfortable with who I am as a person."

    scene black
    with dissolve

    if bonus == True:
        "Osako storms off in the opposite direction with a shopping bag pressed firmly between a set of fingers that will likely wind up inside a coworker of mine tonight."
        "I contemplate whether or not this “sexting” thing is truly worth it-"
        "But then realize that I have a perfectly good lesbian fantasy to continue playing out in my head as soon as I get home."
    else:
        "Osako leaves and I cry for a few hours."
        "I am so sad."

    $ renpy.end_replay()
    $ osako_love += 1
    $ osakodate1 = True
    stop music fadeout 5.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label osakodojo1:
    scene osakokicksyourass1
    with dissolve2
    play music "rapid.mp3"

    "So, it appears that today is the day I die."
    "I knew that visiting Osako at the dojo would be a bad idea after her parting words to me the night of her anniversary were that she was going to activate one of my apparently fatal pressure points."
    "But, of course, I’ve always been bad when it comes to warnings. "
    "And even worse when it comes to staying away from cute girls."
    "And now, apparently girls who don’t even like men to begin with."
    "So yeah, no idea how I wound up in this mess if not for taking too many directions from my penis."

    s "I’ll give you one last chance to step down, Osako. "
    s "I am bigger than you. That must be good for something."

    scene osakokicksyourass2
    with dissolve

    os "Is this why you never want to actually practice? Because you’re scared?"
    os "Or are you just feeling a little vulnerable because Ayane isn’t here to protect you today?"

    scene osakokicksyourass1
    with dissolve

    s "I don’t need Ayane’s protection. I’m just saying that any rational person would look at this matchup and assume that {i}I{/i} am going to win."

    scene osakokicksyourass2
    with dissolve

    os "I’ll admit that you’re in surprisingly good shape for someone who despises any amount of physical activity."
    s "That’s not true. I love-"
    os "Don’t say it."
    s "Damn it."
    os "Listen, dude. You can talk all the smack you want, but if you think for a second that I am not going to knock you on your ass, you are sorely mistaken."
    s "In that case, is it too late to back out?"

    scene osakokicksyourass3
    with dissolve

    os "Yup. The least you can do in exchange for taking up a spot on the roster is letting me kick your ass once or twice every few months."
    s "No worries, I’ll just quit the dojo instead then. Thanks for all of your hard work up until now."
    os "You can’t quit. Your story with Ayane hasn’t finished yet. "
    os "Aren’t you guys trying to like, take back Kumon-mi or something?"
    s "Why do you know about that? And why can I hear the background music for it right now?"
    s "You’re not...part of the Amamiya army, are you?"

    scene osakokicksyourass4
    with dissolve

    os "The what?"

    "She must be a spy."
    "Or, even worse...an assassin sent by Ayane to take me down and reclaim the land that her family is owed or...something."

    scene osakokicksyourass5
    with dissolve

    s "Pretend you’re not a part of this all you like. I know that you’re with {i}them{/i}."
    os "Wait, are you actually into that whole roleplaying thing after all?"
    os "This whole time I thought you were just playing along to make Ayane happy."
    s "That’s precisely what I {i}wanted{/i} you to think."

    scene osakokicksyourass6
    with hpunch

    s "Because that means you’ve let your guard down!"

    scene osakokicksyourass4
    with dissolve

    os "..."
    s "..."
    os "Do you..."
    os "Do you expect me to also become a part of this now?"

    scene osakokicksyourass1
    with dissolve

    s "I expect you..."

    scene osakokicksyourass6
    with hpunch

    s "To die!"

    scene black
    with dissolve

    "I gather every last bit of energy in my body and charge at Osako with an ultimate attack."
    "One that’s sure to-"

    s "Wait...impossible!"

    play sound "static.mp3"
    scene osakokicksyourass7 with flash
    stop sound

    os "You know, I was going to say something like “Try and hit me if you can,” but you just went right ahead and attacked me without even getting the signal."
    os "You’re pretty ballsy for a complete wuss, huh?"
    s "Let go of my hand."
    os "And then what? Let you attack me?"
    s "You interrupted my strongest move."

    scene osakokicksyourass8
    with dissolve

    os "If {i}this{/i} is your strongest attack, you really should start paying a little more attention to my lessons."
    os "There’s a lot I can teach you if you actually open up your mind, you know."
    os "For example, do you want to know how I was able to predict the exact motion of your fist before it even reached its halfway point?"
    s "Is it because I’m a complete novice?"
    os "That’s definitely part of it!"
    os "In fact, for the sake of today’s exercise, we can even say that’s {i}all{/i} of it."
    os "While competitive karate does exist and is pretty fucking awesome, it doesn’t take away from the fact that it’s still an art of self defense at its core."
    os "If someone attacks you on the street, it’s probably safe to assume that they aren’t a trained fighter who knows how to counter things like this."
    os "So as long as you’re able to predict their actions before they make them, you have the upper hand."
    s "Cool. Can I have my hand back now? I want to try hitting you again."
    os "No. Because now it’s {i}my{/i} turn to hit you."
    os "But since I’m so nice, I’ll let you know how I’m going to attack and {i}where{/i} so you can try and block it."
    s "As if I’d fall for that. You’ll just attack whatever place you tell me {i}not{/i} to protect."
    s "I know your games, assassin. "
    os "No, no. Really. I mean it."
    os "I’m going to push back on your fist and then attack you from above with a kick."
    s "What? But how are you going to attack me from above when-"

    scene osakokicksyourass9
    with dissolve

    os "HA!"
    s "Wait, what?"

    scene osakokicksyourass10
    with hpunch

    "Osako connects with the side of my neck and I can instantly feel my body beginning to go limp."

    s "Was that..."

    scene osakokicksyourass11
    with dissolve

    os "One of seven ways I know how to kill you in one blow."
    os "Tell me how the ground tastes, would you?"
    s "I..."

    scene black
    with dissolve
    play sound "thump.mp3"

    "I hit the ground without even getting a chance to reach out and break my fall with my hands."
    "My body is no longer capable of moving."
    "I really am going to die today, aren’t I?"

    scene osakokicksyourass12
    with dissolve2

    s "Ngh..."
    s "Even though you told me...exactly where I’d be attacked...I couldn’t do anything about it..."

    scene osakokicksyourass13
    with dissolve

    os "Couldn’t? Or {i}didn’t{/i}?"

    if bonus == True:
        os "Because it seemed like you were too busy admiring how flexible I am to block where I told you to block."
        s "So many...possible positions..."
    else:
        os "Because it seemed like you were too busy thinking about hugs or something to block where I told you to block."
        s "They are just so warm"

    scene osakokicksyourass14
    with dissolve

    os "Hah...really, man. All you need to do is just listen to me and you can {i}actually{/i} become better at this. "
    os "I’m trying to actually help you out with your technique right now, and I can’t do that if you’re down there on the floor."
    s "It doesn’t look like you’re helping me."
    os "I told you what to do and you didn’t do it. Don’t go blaming me for your inadequacy or disinterest."
    os "Now get back up and fight me like a real man or I’ll have to show you where your other six pressure points are."
    s "I...don’t think I can move my body."

    scene osakokicksyourass13
    with dissolve

    os "Sure you can. I didn’t kick you {i}that{/i} hard. "
    s "No...I really-"

    scene osakokicksyourass15
    with dissolve

    s "Ngh-"
    os "Blah blah blah. I’m a weak little bitch who can’t even take one kick from a girl."
    s "Just...put me out of my misery already..."
    os "Are you Wakana now?"
    s "If I say yes...can we make out?..."

    scene osakokicksyourass16
    with hpunch

    s "Ngh!"
    os "You think I’d ever kiss someone as weak as you?"
    s "There is no way...Wakana is stronger than I am..."

    if bonus == True:
        os "True. But Wakana is a beautiful woman and you’re just some perverted lowlife. "
    else:
        os "True. But Wakana is a beautiful woman and you’re just the huggy boy. "

    s "Why is your...foot stronger than my entire body?"
    os "Hm? "
    os "Oh. I used to kickbox before starting karate, so I’ve always considered anything involving legwork my speciality."
    os "How else would I have been able to sink my heel into one of your pressure points without even trying?"
    s "Can I...have my head back now?..."
    os "That depends. Are you going to try and kiss me?"
    s "Not if it means experiencing this level of pain again."
    os "Then sure."
    os "I’ll even go get you a drink as a personal thank you for actually making an effort today."
    os "Even if that effort was entirely worthless."
    s "You are...much scarier than I thought you were..."

    scene black
    with dissolve2

    "Osako removes her foot from my head and I can slowly but surely feel the world begin to solidify beneath me."
    "My legs, which had been as gelatinous as the soup I made with Wakana nights before, stop wobbling and, before long, I’m able to get them to stand upright again."
    "I take another minute or so to fully regain consciousness and manage to open my eyes once I see Osako coming my way with a bottle of water."

    scene osakokicksyourass17
    with dissolve

    os "Uhh...why did you flinch? I’m just bringing you a drink."
    s "I think it was a reflex."
    s "This might just be how I have to act around you from now on."
    os "Oh, stop. I used that same kick on Ayane and she got up in like fifteen seconds."

    if bonus == True:
        "Yes but she also cried the first time I put my penis inside of her, so I know deep down that I’m stronger."

    scene black
    with dissolve2
    stop music fadeout 13.0

    "I take the bottle of water from Osako and quickly rehydrate myself."
    "Not because I want to continue training, but because if I don’t, I’ll likely pass out and be stomped on once more."
    "And while there are plenty of people out there who I am sure would love such a thing...I am very much not one of them."
    "Osako follows me to the side of the room and leans up against the wall beside me, sparing my life for at least another several minutes."
    "Or at least that’s what I {i}would{/i} think..."
    "If she wasn’t an Amamiya family assassin."

    scene osakokicksyourass18
    with dissolve

    s "..."
    os "..."
    s "..."
    os "..."
    os "What?"

    scene osakokicksyourass19
    with dissolve
    play music "sakuya4.mp3"

    s "Hah..."
    s "Nothing."
    s "I can see now why Touka’s family wanted to hire you personally."
    os "That’s not something you could possibly know after like, one tenth of a sparring match."
    os "If I was actually trying, you really would be dead right now."
    os "Like, that’s not even a joke."

    scene osakokicksyourass20
    with dissolve

    s "Why subject yourself to {i}this{/i} then?"
    s "Everyone here has little to no experience at all. Don’t you ever get bored having to teach people that are so...below you?"
    os "Don’t you?"
    os "Wakana says you’re pretty smart."
    os "You even recognized that Lord Byron poem I memorized for her when I confessed. "
    s "First off, Wakana specifically made a point of how recognizing things like that doesn’t make you smart."
    s "And secondly, that is adorable."

    scene osakokicksyourass21
    with dissolve

    os "Isn’t it?"
    os "A lot of people are surprised to hear that I’m actually into a lot of gothic stuff as well and that I’m not just dating Wakana because of that whole “opposites attract” thing."
    os "Like yeah, that applies to our personalities and styles, but we share a ton of the same interests and-"

    scene osakokicksyourass22
    with dissolve

    os "And now I’m going to start ranting about her again because I love her so much."
    s "..."
    os "..."
    s "You never answered the question."

    scene osakokicksyourass23
    with dissolve

    os "Was there a question? I zoned out when we started talking about Wakana."
    s "I asked you why you bothered teaching here since you’re so much better than everyone."

    scene osakokicksyourass24
    with dissolve

    os "Ahh, right. Right."
    os "I don’t know, really. "
    os "There aren’t enough advanced martial artists in Kumon-mi for me to make a living off of instructing them, so I guess I just followed where the money was."
    os "It’s not like this was my first choice or anything. I had much bigger plans. "
    os "Just...can’t really do anything about them anymore."
    s "What kind of plans are you talking about?"

    scene osakokicksyourass25
    with dissolve

    os "Competitions...getting better myself instead of helping others get better."
    os "Always wanted to try doing something on a national level because I’m definitely good enough."
    os "But now that no one’s allowed to leave Kumon-mi, that path just...isn’t possible anymore."
    os "And it doesn’t seem like it’s going to be opening back up anytime soon, so..."

    scene osakokicksyourass26
    with dissolve

    os "..."
    os "So I’ll very likely be a little too old to compete whenever it {i}does{/i}."
    s "Even if it’s a few years, I doubt it would matter-"
    os "It matters."
    os "The most important resource for pretty much all athletes is our age."
    os "Every year counts. And when your “prime” is limited to such a small window of your life, everything you do winds up getting centered around that."
    os "Then, once it’s gone, it’s all downhill and you’ve just gotta...figure out other shit to do."
    os "So even if it is only a few years, each one of those years will matter."

    scene osakokicksyourass27
    with dissolve

    os "Or {i}would{/i} matter...since chances are that’s not happening and that I’ll be stuck teaching beginners until I can’t move my body anymore."
    s "..."
    os "..."

    "I wonder if it’s okay to provide someone false hope even when you know things aren’t going to work out for them?"
    "Obviously, Osako has no idea that time is being reset every few months and that she’ll likely remain in the same limbo her significant other is caught up in-"
    "But I wonder if it’s okay to pretend that’s not the case."
    "To throw a few scripted words of false sincerity at her in hopes that she’s naive enough to eat them up."
    "I guess it’s worth a shot, right?"

    s "I wouldn’t give up just yet."
    s "For all we know, the city could open back up tomorrow and you could board the first flight to...wherever they do karate stuff."

    scene osakokicksyourass28
    with dissolve

    os "Yeah..."
    os "Maybe that will happen."
    os "Or maybe it won’t."
    os "I shouldn’t dwell on it either way."
    os "If things do make a turn for the better, that’s definitely the path I’ll wind up walking."
    os "But for now...I’m happy just walking beside my girlfriend and supporting her."
    s "..."
    os "..."
    s "Are you about to start talking about Wakana again?"
    os "God, she’s so fucking cute. I can’t stand it."

    scene black
    with dissolve2

    "It’s rather unfortunate that I’ll never get to see Osako kicking someone to death on live television."
    "But it {i}is{/i} fortunate that I’ll get to spend more time with her."
    "An unlimited amount of it, too."
    "Who would have thought that someone who’s been {i}this{/i} close to me ever since I arrived in Kumon-mi would suddenly become an actual character in {i}my{/i} story?"
    "And I in hers. "
    "We all have our own dreams...goals...desires..."
    "And most of them will float forever, unfulfilled."
    "But some of us are fortunate enough to learn this beforehand."
    "To create new goals that we can accomplish within shorter amounts of time."
    "And use that manipulation of the laws of the universe to survive or grow."
    "Then, sooner or later-"
    "We’ll have everything we’ve ever wanted."
    "The fortunate ones, I mean."
    "Everyone else?"
    "Well-"
    "Maybe they’ll be rewritten into someone with a little better luck?"

    $ renpy.end_replay()
    $ osako_love += 1
    $ osakodojo1 = True
    stop music fadeout 5.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label osakodate15:
    scene osakokaraoke1
    with fade
    play music "maidcafe.mp3"

    os "..."
    s "..."
    os "..."
    s "..."
    s "You are not the maid I asked for {i}or{/i} wanted."
    os "Tough shit, because I’m the maid you got. You think I’m any happier about this than you are?"
    s "You should be, as I’m pretty sure that’s what you’re being paid for."
    os "Bite me."
    s "Here is my first command. I demand a shorter maid whose name starts with the letter “U” and ends with “ta-chan.”"

    scene osakokaraoke2
    with dissolve

    u "I’m sorry, Master! But little ole’ U-to the-ta-chan’s totally booked up at the moment! Can’t you do her a big favor and settle for Osako-chan just this once?"
    u "So long as she’s wearing that uniform, you don’t have to worry about her putting you in an ankle lock or whatever the heck it is they do in karate."
    s "Is that true, Osako? Am I safe here?"
    os "Depends on how many of my buttons you manage to push."
    s "Which ones am I {i}allowed{/i} to push?"
    os "Not whichever one you’re trying to push right now."
    u "Jeez. Get a room, why don’t ya?"

    scene osakokaraoke1
    with dissolve

    "I wind up at the maid cafe- a place I probably wouldn’t have bothered coming to if I had known I was going to be partially ignored by my favorite employee."
    "Please don’t tell Ami I said that."
    "Anyway, due to word finally starting to get around about this place and the increase of business brought on by summer, I have found myself in the company of another employee who, while good, is no Uta-chan."
    "Thankfully, I don’t think I’ll have to deal with her for very long as the cafe should be closing in about thirty minutes or so."
    "Which is just enough time for me to test this maid’s abilities and see how much she has grown now that she has accepted this as a second near full-time job."
    "Even if it’s a job I’m pretty sure she’s only keeping to satisfy some sort of sexual desire."

    s "You know, I haven’t heard you call me “Master” today. Do I need to file a formal complaint?"
    os "Do I need to formally file my foot in your ass?"

    "She fails the maid test almost immediately."

    s "Can you at least do the thing?"
    os "What thing?"
    s "The thing Uta-chan does to make sure my food tastes delicious."
    os "The flavor beam?"
    s "Yeah. Not to be confused with the death beam- another move I have recently learned that she has."

    scene osakokaraoke3
    with dissolve

    os "Bzzzzzt. "
    os "Your food tastes better now."
    s "You don’t even have a cool rhyme to go along with it?"

    scene osakokaraoke4
    with dissolve

    os "Man, I brought you your damn omelet. Do you really have to spend the rest of your time here trying to get a rise out of me?"
    s "I know it might seem like that’s my goal here, but what I’m {i}really{/i} trying to do is help you. You know, like how you help me with karate."
    os "You have made a total of two or three attempts out of what feels like thousands to actually learn anything inside of the dojo."
    s "And you’ve made how many attempts here?"

    scene osakokaraoke5
    with dissolve

    os "I make plenty of attempts with the other guests. There’s just something about the idea of acting that way to you that makes me throw up in my mouth a little."
    s "If you’re a decent maid when it comes to everyone else, how come I’m the only one you’re serving right now while Uta-chan is busy with literally every other table?"
    os "Just because I’m okay doesn’t mean I can compete with somebody who’s not only way younger, but way more experienced when it comes to this sort of thing."
    os "If I was still a teenager, I guarantee you I’d have more than one table right now. But unfortunately,  life has gone on for me and I must now deal with customers like you who only want cutesy girls."
    s "You’re cute in your own way."

    scene osakokaraoke6
    with dissolve

    os "Oh yeah? And what way is that?"
    s "The way that if I ignore your face and only look at your body, I can pretend that you’re still just as young as Uta."
    os "You need professional help."
    s "What I need is a better maid."

    scene osakokaraoke7
    with dissolve

    u "Are you two in love yet? Or is Osako-chan still a full fledged lesbian?"
    os "Still a lesbian, but thanks for checking. Especially since everyone knows that’s the sort of thing that can just change whenever I want it to."
    s "If Uta-chan can train herself to stop being sexually attracted to sea creatures, I believe that anything is possible."

    scene osakokaraoke8
    with dissolve

    os "To...what?"
    u "So anyway! Ignoring what Sensei just said, do you want to actually come to karaoke after work today?"
    u "You made the mistake of telling me Miss Watabe is feeling under the weather earlier, so you have no excuse to back out on me this time!"
    os "Is caring for my ailing girlfriend not good enough of an excuse?"
    u "Not when there are songs that need to be sung, it’s not! My grandpa that I used to care for would agree with me if he could but, unfortunately, he-"
    os "Yup. He’s dead. You don’t have to remind me every shift, you know."
    s "I wouldn’t bother inviting Osako. She’s made it clear that she’s already past the prime of her life and can’t really do what young people do anymore."

    scene osakokaraoke9
    with dissolve

    os "I’m still younger than you, you know! Stop making it sound like I’m on my death bed just because I mentioned being pretty and perkier during my high school years!"
    u "Do you want to come too, Sensei? The more the merrier! Plus, having a chaperone might prevent the two of us from winding up on the floor again!"

    scene osakokaraoke10
    with dissolve

    os "You’re so much better than him. Why would you ever put yourself in a situation where he can tackle you to the ground?"
    u "What if I’m the one who tackled him?"
    os "That-"

    scene osakokaraoke11
    with dissolve

    os "Actually, that tracks. I’ve seen firsthand how weak this guy is. I think Uta could probably take you down on a good day."
    os "I don’t really understand why she {i}would{/i} when she’s like four leagues ahead of you, though."
    s "Uta-chan, I don’t want Osako-chan to come to karaoke with us. She’s really killing the vibe right now."
    os "If you’re trying to sound young, it’s not working."
    s "You’re one to talk, being so far out of your prime and all."
    u "Master, you’re going to have to speak a little louder if you want grandma Osako to hear you. Her ears ain’t what they used to be."

    scene osakokaraoke12
    with dissolve

    os "Screw it! You want me to come?! Fine! I’ll show both of you I‘m still young at heart! And when I’m done with that, I’ll work on stealing some of your regular customers!"
    os "Just because I’m not your age anymore doesn’t mean I’m invalid! There’s still demand for people like me! "
    s "Maybe at the local retirement home. "

    scene osakokaraoke13
    with dissolve

    os "Again, I am {i}younger{/i} than you!"
    u "Yeah, but Sensei passes the vibe check. And the only kinda vibe Osako-chan knows is the one she uses on Miss Watabe."

    scene osakokaraoke14
    with dissolve

    os "That’s it! Osako-chan, special move! Double-fisted death beam!"
    u "Osako-chan, no! You’re still not ready! You could hurt yourself!"
    s "Those aren’t even fists."
    os "Shut up, shut up, shut up! Just die already!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Uta and I manage to survive the double-fisted death beam (With no actual fists involved) and make it through the rest of the shift without issue."
    "And, being dead set on proving that she is not a “grandma” like Uta suggested, Osako remains true to her word and joins the two of us for a trip to the karaoke bar once the maid cafe closes."
    "Upon arrival, Uta books us a room and, before Osako and I are even able to sit down, she has already booted up the machine and begun singing her first song..."
    "........."
    "......"
    "..."

    play music "utasings.mp3"
    scene osakokaraoke15
    with dissolve2

    os "I barely know any of these songs."
    s "Nothing from back when you were young?"
    os "You mean less than ten years ago? Not sure."
    os "I might recognize some of them if I got to listen to them first but, based on titles alone, I don’t really recognize any of these."
    s "Not a music person?"
    os "Not really. All my free time in high school went toward karate. And all my free time in college went toward Wakana- who isn’t much of a music person either."
    os "We never really did stuff like this. That was more of a...popular girl sort of thing."
    s "Neither one of you strike me as the “popular” type, so that makes sense."

    scene osakokaraoke16
    with dissolve

    os "Yeah...well you don’t seem like you were all that popular either, smartass."
    os "Guess you’re right, though. I was never {i}unpopular{/i} or anything. I actually had a good amount of friends in high school, but they were all, like...club friends. Not people I spent any free time with."
    os "College was totally different. As soon as I started seeing Wakana, I barely even {i}talked{/i} to anyone else anymore. But I never really cared about that since I had her."

    scene osakokaraoke17
    with dissolve

    os "Probably goes without saying, but she was always a bit of an outcast. You can’t really look the way she does and expect {i}not{/i} to be."
    os "But one of my favorite things about her is...that never really seemed to be an issue for her."
    os "She did what she wanted and didn’t care about what anyone else had to say about it."
    os "I still love watching her do that today. And I love how...non-judgemental she is when anyone else wants to do their own thing as well."
    s "She judges {i}me{/i} all the time."
    os "You’re a grown man hanging out with teenage girls. She’d be a bad person if she {i}didn’t{/i} judge you for that."
    os "But if you randomly took up some niche hobby like...painting models or articulating animal skeletons, I doubt she’d think you’re weird for it."
    os "Actually, she’d probably like the skeleton one. That seems like a very {i}Wakana{/i} thing."
    s "Do you ever worry that you might be basing too much of your current self on her?"

    scene osakokaraoke18
    with dissolve

    os "What do you mean?"
    s "It just sounds kind of like you stopped existing as {i}Osako{/i} once you met her. Now you’re just {i}Wakana’s{/i} Osako. "
    os "That’s not true. I still have plenty of interests that I don’t share with Wakana."
    os "At the same time, though, why would being {i}Wakana’s{/i} Osako rather than just {i}Osako{/i} be a problem if that’s what makes me happy?"
    s "It’s not at the moment. But if something ever happened to her, what would that mean for you? "
    s "Aren’t you afraid of the possibility of losing the one thing that makes you {i}you?{/i}"
    os "Of course. It’s my greatest fear of all. "
    os "But fear is something that is meant to be confronted, not avoided."
    os "I’m not going to change who I am based on “what ifs” when the person I am today, codependent or not, is the happiest version of myself I’ve ever been."

    scene osakokaraoke19
    with dissolve

    os "All this...stereotypical “fun stuff” that other people do has just never really been a factor for either one of us. So it’s not like we’re even missing out on anything."
    os "In a way, the fact that she's always been so focused on living for {i}herself{/i} has helped me validate the way I've always felt in the back of my mind."
    os "It was always a little weird to me that I never felt regret or remorse for spending time on my training when others would ask me to come hang out with them."
    os "It’s like...I {i}wanted{/i} to feel bad since I knew I was letting people down...But I didn’t really have the {i}time{/i} to feel bad since it would just distract me."
    s "How is that any different from how you feel now? What changed?"
    os "What changed is I don’t {i}want{/i} to feel bad anymore."
    os "If somebody gets bogged down by me not coming along with them, that’s on them- not me."
    os "Parents...friends...family..."
    os "We worry so much about what everyone around us thinks that we often forget to think for ourselves. Life is so much better once you learn to just...leave all that behind."
    s "If that’s true, how come you get so offended every time we make fun of you for not being young anymore?"

    scene osakokaraoke20
    with dissolve

    os "Because I know you’re wrong and that I could blindfold myself and {i}still{/i} kick both of your asses at the same time."
    s "That’s even more worrying since I know there must be at least five blindfolds inside of your apartment."
    os "One for every weekday."
    u "Aaaand done! Your turn to show off your pipes, Osako. I know that following the great Uta-chan is no easy task, but I’m sure that if you try your best, you-"

    scene osakokaraoke21
    with dissolve

    os "Yeah, yeah, yeah. Just shut up and listen, Uta."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Osako finally finds a song she recognizes and takes the mic from our self-proclaimed MC’s hands."
    "Before I can blink my eyes, their places are swapped. But instead of my gaze landing on the girl it almost always lands on, it gets caught on a nail hanging off of the main stage."
    "And it cuts me deeper than the ones I routinely walk on."
    "........."
    "......"
    "..."

    scene osakokaraoke22
    with dissolve2
    play music "hallelujah.mp3"

    u "Osako, what the heck? This song isn’t fun at all."
    os "Shut up. It’s the only song I recognized the name of and I don’t care if you like it or not."
    u "It’s not that I don’t {i}like{/i} it. It’s just that...well, you know! It seems like something my grandma would sing if she wasn’t knockin’ boots with my grandpa up in Heaven."
    s "Just let her sing, Uta. Your songs are always too energetic for me anyway."
    u "Ugh! What’s a girl gotta do to get some excitement up in here?!"

    "Osako takes a deep breath..."
    "And then slowly opens her mouth..."

    scene osakokaraoke23
    with hpunch

    os "I'VE HEEEEEARD THERE WAAAAAS A SECRET CHORD!!!! "
    os "THAT DAAAAAAVID PLAYED AND IT PLEEEEEASED THE LORD!"
    os "BUT YOOOOUUUU DON’T REAAAAALY CARE FOR MUSIC...DO YOU?!?!?!?!"

    scene osakokaraoke24
    with fade

    os "IT GOOOOOOES LIKE THIS...THE FOURTH...THE FIFTH!!! "
    os "THE MINOR FALLS, THE MAJOR LIFTS!!!!!!!"
    os "AND DAA DA DAAA DA DAAA DA HAAAAALLELUUUUUJAH!!!!"
    u "..."
    s "..."
    u "I’ve gotta go return some video tapes."
    s "I’ll come with you."

    scene black
    with dissolve2

    os "HAAAAALLELLUUUUJAH! HAAAAAALLLELUUUU- Wait, where are you guys going? I thought Uta was singing again after this?"
    u "Sensei, split up! She can’t catch both of us!"
    os "Wha-"
    os "Get back here! I haven’t even finished yet!"

    $ renpy.end_replay()
    $ osakodate15 = True
    $ osako_love += 1
    $ uta_love += 1
    stop music fadeout 10.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label osakodate20:
    scene osakopornshop1
    with dissolve2
    play music "notabluearchivesong.mp3"

    "I decide to swing by the porn shop to see how Maki’s doing, but the smile on her face tells me all I need to know- which means that I am now going to focus on Osako instead."
    "I don’t know how these opportunities to embarrass her keep falling into my lap, but I’m glad they are considering that the chances of {i}her{/i} ever falling into my lap are essentially zero."
    "If I can’t have her, I can at least make her question her existence on this planet- a common strategy employed by many others like me...Albeit with typically less consistent and successful track records."
    "I sigh to myself as my win rate ticks down from 100%% and take my place behind her which, again, is a thing I will never be able to do in the way I want."
    "She’s a lesbian- just in case you aren’t quite picking up what I’m putting down here."

    maki "See this baby right here? This is the DildoSaber- fresh out of the factory and ready to pierce through the heart (Or vagina) of the one you love."
    maki "And if blue isn’t your color, never fear! This thing has a grand total of {i}seven{/i} color settings. And if what I’ve heard is correct, the glow is so bright you can even see it {i}inside{/i} of your partner if the lights are off!"
    os "Is that even safe?"
    maki "It wouldn’t be on the market if it wasn’t. "
    maki "Plus, if for some reason its handleability isn’t already a strong enough selling point, it also has several vibration settings you can access from the official DildoSaber app. "
    os "Wow...They’re really starting to get creative with stuff like this, aren’t they?"
    os "I don’t know. It seems fun...but I’m not really sure if it fits our style. We’re not really {i}app{/i} people."
    os "Do you have anything more, uhh...you know-"

    scene osakopornshop2
    with dissolve

    maki "Dark and somber? "
    maki "Something that would strike fear into the heart of anyone {i}unready{/i} for the games you lovebirds play? "
    os "Hahah...so you...remember..."
    maki "I never forget a customer, Osako Osaka. "
    os "I don’t really know how I feel about that."
    maki "Besides, if I had a dollar for every time I’ve had to pretend to not recognize your partner at school meetings, I’d have enough to afford...maybe a tenth of an official DildoSaber."
    os "Either that thing is damn expensive or you’ve only seen Wakana a handful of times outside of this building."

    scene osakopornshop1
    with dissolve

    maki "It happens every now and then. But with how-"

    scene osakopornshop3
    with dissolve

    maki "Oh! I’m sorry. I was so absorbed in the official DildoSaber that I didn’t even see you there. "
    maki "I’ll be with you right after I finish with this customer."

    scene osakopornshop4
    with dissolve

    os "No, it’s totally fine. She can go ahead of-"
    s "..."

    scene osakopornshop5
    with dissolve

    os "Oh, fuck."
    s "Hey, Osako. Crazy meeting you here."
    maki "Acquainted already?"

    scene osakopornshop6
    with dissolve

    os "I have never seen this man before."
    s "She’s lying. We’re actually best friends. She even shares her girlfriend with me sometimes."
    os "This store wouldn’t happen to be hiring a security guard would it? I feel suddenly compelled to kick the shit out of the nearest pervert."
    s "Run, Maki. Run while you still can. "
    maki "I’m not worried. You see, the official DildoSaber is so heavy-duty that you can also use it as a weapon if you’re ever in a pinch!"
    maki "And with its collapsible...dildo part, it makes the perfect sex toy {i}and{/i} self-defense weapon! Perfect for stuffing into both your bag {i}and{/i} your partner!"
    s "Osako, I’m no lesbian, but this DildoSaber sounds pretty intense and I think you’d be a fool not to buy it."

    scene osakopornshop7
    with hpunch

    os "I don’t want the fucking DildoSaber!"
    maki "Ah-"
    s "Now look what you’ve done. You’ve hurt Maki’s feelings."
    maki "You can make it up to me by purchasing the official DildoSaber for the low, low price of-"

    scene osakopornshop8
    with hpunch

    os "Mm!"
    maki "Wait. I suddenly remembered I have to...go over there!"
    maki "Please {i}come{/i} find me when you’re ready to check out."

    scene osakopornshop9
    with dissolve

    "Sensing that her life must be in danger, Maki scurries off- retreating into the back room and, if her dialogue tonight has been any indication of where her personal interests lie, probably testing out the DildoSaber."

    os "Is nothing sacred anymore? "
    s "If you were seeking sanctuary in this house of unholiness, I have very bad news for you."

    scene osakopornshop10
    with dissolve

    os "Why are you even here? "
    s "The same reason you’re here. Because I’m a sex positive adult looking for a good time."
    s "Also, I’m friends with Maki and wanted to check in on her."
    os "Then check in on her instead of talking to me. I didn’t ask for this."
    s "Right now, I think some alone time with that new toy is what Maki needs most."

    scene osakopornshop11
    with dissolve

    os "I think she needs a lot more than that based on what I’ve heard from Wakana about her husband. "
    s "You’re right. We should go cheer her up physically. But I get to go first."

    scene osakopornshop12
    with dissolve

    os "That seemed low and insensitive even by your standards."
    s "I tend to let it all hang loose in here. That’s what Maki would want after all."

    scene osakopornshop13
    with dissolve

    os "Yeah...I’ve been avoiding coming here lately for that exact reason. I thought she’d need more time to grieve, but...it looks to me like she’s at least somewhat okay now. "
    os "I guess she could always be acting, though."
    s "Having to {i}avoid{/i} this place makes it sound as if you might have some sort of addiction, new best friend."

    scene osakopornshop14
    with dissolve

    os "Stop calling me that. And also, stop trying to probe me for information about my sex life. I’m not going to tell you anything."
    s "If you’re not going to tell me anything, can I at least ask you an extremely generalized, lesbian-based question that I've always been curious about?"
    os "Is it going to be sexist, insensitive, or the result of blatant obliviousness?"
    s "I just want to know why lesbians still like penis shaped toys but not actual men."
    os "So yes. It is going to be all three of the things I just said."
    s "You can not blame man for his curiosity."
    s "You are free to not have sex with him, though."

    scene osakopornshop15
    with dissolve

    os "Well, thanks so much for your {i}permission.{/i} I really-"
    s "Makoto."

    scene osakopornshop16
    with dissolve

    mak "In the flesh."
    s "What are you doing down here? I didn’t think you were ready to-"
    mak "I’m getting a drink. We’re out of bottled water upstairs."
    mak "Also, please stop pestering the customers. If you’re looking for a quick release, check the aisle in the back left. New TENGAs, 30%% off. Woohoo."
    maki "Makoto! Makoto!"

    scene osakopornshop17
    with dissolve

    maki "Look! They came! Heh. Came. And they’re even cooler than I thought!"
    mak "Can you stop waving that thing around? You look like a maniac."
    maki "But it’s got an accelerometer in it that gives it that cool {i}whoosh{/i} noise like you hear in the movies!"
    mak "You know what? Maybe I’ll just die of thirst. "
    maki "Noooo, come on! Pick one up! We’ll have an official DildoSaber fight!"
    s "So, Osako- would you rather stay here and listen to this? Or come talk to me outside about this secret addiction of yours?"

    scene osakopornshop18
    with dissolve

    os "It’s not an {i}addiction.{/i} I just..."
    s "Just what?"
    os "Just don’t want to talk to {i}you{/i} about it. It makes me uncomfortable."
    s "What difference is talking to me about something like this than someone like Maki? As the owner of a penis, I probably know just as much as she does."
    s "If anything, I feel like it should be easier to talk to me since you have literally zero sexual attraction toward me and have likely fantasized {i}at least{/i} once about the owner of this porn shop."

    scene osakopornshop19
    with dissolve

    maki "Everyone does, Osako. I’ve accepted it. It’s nothing to be ashamed about."
    mak "Yeah, that’s it. I’m gonna go die now."

    scene osakopornshop20
    with dissolve

    maki "Wait! No! I’ve already lost one!"

    scene osakopornshop21
    with dissolve

    maki "Makoto! Come back! I’ll give you a discount on your first official DildoSaber!"
    mak "I don’t want a DildoSaber! I want you to pick up more water from the grocery store! The tap water tastes weird!"
    os "Hah..."
    os "I guess...you’re kind of right about the whole sexual attraction thing. I just don’t want you getting weird about this when it seems like “getting weird” is all you’re really good for."
    s "That might be {i}something{/i} I’m good for, sure. But I know when to stop. Kind of. "
    s "And if you heard my inner monologue, you’d know that I’ve already acknowledged the fact that we’re never going to bang like three or four times tonight alone."
    os "Three or four? Isn’t that a little too often?"
    s "Probably, but it’s far less than it would be for everyone else. "
    s "If you don’t want to talk, that’s totally cool and I am happy to just embarrass and annoy you for the rest of the night."
    s "I just figured there might be something you want to get off your chest if you’ve been literally and intentionally {i}avoiding{/i} this place."
    os "Even if there is, what would you do? What sort of relevant sex advice am I going to get from a heterosexual male?"
    s "Hey, we both like women, don’t we? We might have more in common than you think."

    scene osakopornshop22
    with dissolve

    os "..."
    s "..."
    os "Can you promise to not repeat any of this to Wakana?"
    s "Sure."
    os "And to not be a fucking perverted creep about it if I actually tell you anything?"
    s "That one sounds harder but, again, sure."
    os "And no more sexist, insensitive, blatantly oblivious questions?"
    s "I will literally just stand there if I have to. Like Maki, I really just want you to find what you’re looking for."
    s "I doubt I can find it for you but, at the very least, I can walk by your side so you seem less suspicious and don’t feel pressured to just walk away empty-handed."
    os "..."
    s "..."
    os "God, I hate having no one else to talk to sometimes. "
    os "Fine. Come on. But I’m breaking your arm the second you get weird."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene osakopornshop23
    with dissolve2

    "Osako and I step outside to avoid the constant pressure to buy a certain sci-fi themed sex toy that even {i}I{/i} was relatively impressed by and press our backs against the wall."
    "It’s quiet enough around here that we {i}should{/i} be keeping our voices down, but the lack of any noticeable person outside means we may not {i}have{/i} to."
    "I guess that’s up to Osako, though. It’s not as if I’m about to come clean about {i}my{/i} sex life to her when confirming anything at all could prove to be...problematic, if nothing else."
    "She has her suspicions, of course. She’s seen the way I am with Ayane. "
    "But I think it would be a whole new story if..."
    "No."
    "This is supposed to be about her."
    "Not me."

    os "So..."
    os "Telling you any of this is just as much of an invasion of Wakana’s privacy as it is mine, so I really {i}will{/i} kill you if any of it gets out."
    s "I don’t want to die any time soon, so knowing that gives me one more reason to keep my lips sealed."
    os "So, uhh...Wakana and I..."
    os "Well...we’ve got a...certain dynamic when it comes to sex."
    os "One that {i}I{/i} love, mind you...that I don’t really have any issues with at all."
    os "But I always feel like I’m not...doing enough for her. Which makes me feel like I...I don’t know, {i}can’t{/i} do enough for her."
    os "And any time I try to...take the initiative and change the way things work, she just pulls out an Uno reverse card on me and, before I know it, {i}she’s{/i} winning again."
    os "Or I guess...{i}losing,{/i} by most people’s standards...But why would someone always want to {i}lose{/i} when {i}winning{/i} feels so much better?"
    s "I know a metaphor when I hear one."
    os "I just want her to {i}win{/i} sometimes too, you know? It feels...unfair. But she’s never shown any sign of wanting that dynamic to change or being unsatisfied and..."
    os "I don’t know, man. You know I’ve got some...dependence issues...and confidence issues...and other shit like that. It’s probably just those things going to work again."
    os "I just can’t help but feel like I’m doing something wrong...Can’t help but feel like I’ve gotta try and shake things up in some way."

    scene osakopornshop24
    with dissolve

    s "Lucky for you, a brand new product just hit the shelves that's sure to light up even the darkest of sex lives."
    os "Don’t you fucking turn on me, man. I swear."
    s "I figured a joke might be better than any obsolete, heterosexual advice I might have."

    scene osakopornshop25
    with dissolve

    os "Just give me normal advice. Human to human. Tell me I’m overthinking this and...manufacturing problems when none really exist."
    s "Have-"
    os "And before you go asking me if I’ve talked to Wakana about it, I have. But she insisted it’s no issue at all."
    s "Then it’s no issue at all."
    os "You really believe that?"
    s "Doesn’t matter what I believe. What matters is that you trust her and she’s already told you how it is."
    s "If she’s lying, you’ve got much bigger problems on your hands than which one of you cums more frequently."

    scene osakopornshop26
    with dissolve

    os "Okay. Guess my metaphor is dead."
    s "I came out here to listen tonight- not to speak in riddles and pretend to understand what you’re going through."
    s "If you’ve got some issues with your sex life, even if those issues {i}aren’t{/i} issues according to the person you {i}think{/i} has issues...the only person you can work it out with is them."
    s "And again, not a lesbian, but I’m pretty sure there isn’t a single sex toy out there that is going to just magically quell all of the worries you’re burdened with at the moment."
    os "Nothing other than the official DildoSaber, you mean."

    scene osakopornshop27
    with dissolve

    s "You know, the fact that you decided to talk to me at all instead of just outright purchasing something we already know to be a solution is really bizarre."
    os "Believe it or not, there’s a limit to how much torture I can endure. And that seemed a little too large for my tastes."
    os "Not really the shape I like either. I prefer them more...{i}authentic.{/i}"
    s "Is my question from earlier really that insensitive? Because I seriously don’t understand how the lesbian brain works and why penises are suddenly cool once they’re not attached to a man anymore."
    os "That’s the forbidden question, dude. Asking it is never going to get you the answer you’re looking for."
    os "Fact is, even if I’m not physically attracted to men, they’ve got an appendage that gets the job done. I’m sure there are just as many gay dudes with onaholes tucked away in their nightstands. "

    scene osakopornshop28
    with dissolve

    s "If it feels good...it feels good, I guess."
    s "I doubt there’s a limit to the amount of torture you can endure, though. If there is anything I have learned through our brief time together, it’s that you are submissive as all hell."
    s "Or, as Imani put it at the bar recently, you “radiate bottom energy.”"
    os "Takes one to know one. I’ll be damned if she doesn’t radiate that same energy right back."
    s "What kind of energy do I have?"

    scene osakopornshop29
    with dissolve

    os "You?"
    os "Negative."
    s "That’s it. We’re not friends anymore."

    scene osakopornshop30
    with dissolve

    maki "Ah! There you guys are."
    maki "What’s going on out here? Thinking of going halfsies on an official DildoSaber? Act now and I’ll throw in a full set of anal beads for no cost at all."
    s "Is that more up your alley, Osako?"
    os "Only if Wakana wants it to be."
    s "Imani was right. Even {i}I{/i} can feel the bottom energy and I have only known about its existence for a few days."
    maki "Energies aside, I think I found something you might actually be interested in, Osako. But it’d probably be best if I showed you {i}alone.{/i} Without Sensei."
    s "What crazy lesbian toy am I not allowed to know the existence of?"
    os "You coming onto me, Maki?"
    maki "You? When I’ve got a box full of DildoSabers? The Bugatti of sex toys? Don’t make me laugh."

    scene black
    with dissolve2

    os "Alright, alright. Let’s see what you’ve got."
    s "Am I really not allowed to see this?"
    maki "Sensei, if you saw this, it would change everything you know about women. It’s best to leave this to us."
    s "What does that even mean?"
    os "It means it’s time for {i}you{/i} to take your little victory and head home. Can’t believe I’ve been actually opening up to you lately. The Hell is going on with me?"
    s "Y-"
    os "And don’t say I’m falling in love with you. You were surprisingly bearable tonight, which is weird given the place we ran into one another."
    os "{i}Wouldn’t want to ruin it now.{/i}"

    "Osako and Maki head back inside to take a look at...whatever sort of device would forever change my opinion about women."
    "I have no idea what that means, so I’m just going to assume it’s actually a mech and that they are planning to take over the world."
    "And while that might not be true, it’s an option that will prevent me from jerking off to the fantasy of sleeping with her {i}regardless{/i} of her preferences."
    "I’ve been surprisingly bearable tonight."
    "I wouldn’t want to ruin it now."

    $ renpy.end_replay()
    $ osakodate20 = True
    $ osako_love += 1
    stop music fadeout 7.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label osakospring1:
    scene osakobeatsyoass1
    with dissolve4
    play music "goodmorning.mp3"

    "I wake up again. A terrible start to the day."
    "Hello, world."

    s "..."

    "No reply. As expected."
    "I grab a half-emptied water bottle from the nightstand and pour its contents down my throat."
    "Millions of bacterial organisms that snuck into the bottle overnight are consumed in the process."
    "Goodbye, new friends."
    "Please enjoy the warm embrace of my intestines."
    "And please thank them on your way down as I have lost the motivation required to do it myself."
    "Ami doesn’t make me breakfast anymore. "
    "There’s no sweet-smelling aroma sneaking in through the crack underneath my door, and there’s no light that finds its way into the room as I’ve been pulling the curtains closed a little bit tighter than I used to."
    "Every once in a while, I have to clean things up around here."
    "I’m not very good at it yet. I’m not even sure where Ami keeps most of the supplies."
    "I don’t know the right way to remove stains from the carpet or which cleaning fluid is best used on the bathroom tiles. And if it weren’t for expiration dates, I’d probably be eating rotten food as well."
    "It’s fine, though."
    "Ami manages to bathe without the help of a sponge, so she’s already better than I was in that regard. "
    "But she has a hard time looking at me now."
    "She feels guilty. "
    "She keeps looking at my hand in the very short bursts of time in which she’s not zoned out and staring at the ceiling."
    "It’s fine, though."
    "I’m sure she just needs some time. So I’ll keep doing my best to get stains out of the carpet and soap residue off of the bathroom tiles while taking careful note of all the expiration dates."
    "Ami doesn’t ever smile anymore."
    "It’s fine, though."
    "She just takes after me."

    play sound "phonering.mp3"

    s "..."

    "I glance over at my phone to see a call from an unknown number."

    stop sound
    play sound "phonebeep.wav"

    "Which is exactly why I decide to answer it."

    s "Hello?"
    os "Uhh...hey."
    s "...Osako?"
    os "Yeah. S...Surprise!"
    s "Did...something happen? You never call me. I didn’t even know you had my number."
    os "Yeah. I kind of stole it out of Wakana’s phone while she was in the shower this morning. "
    s "...Why?"
    os "To...check in on you, I guess. I haven’t seen you in months. But I heard from Wakana you actually showed up to school the other day?"
    s "Yeah. Just long enough to send everything spiraling into chaos, though."
    os "So, how long did that take? Five minutes?"
    s "Give or take a few, yeah. "
    os "Well, at least no one died. And things haven’t been all that exciting in the real world, so you can take some solace in that, I guess."
    os "Ayane’s been doing great in case you were wondering. She’s showing up at the dojo pretty regularly again. "
    os "And, as expected, she’s a solid student when you’re not there to distract her."
    s "That’s good. But usually, when people call to “check in,” they try to {i}avoid{/i} saying things that make the person they’re checking in on feel worse about themselves."
    os "Bullshit. We might not be all that close, but I know for sure something like {i}that{/i} wouldn’t get to you. Especially when you already know it’s true."
    s "There are a lot of things I know to be true, but it doesn’t mean any of them make me feel {i}good.{/i}"
    os "Did your coma kill off the part of your brain that had a sense of humor? Do you want me to apologize?"
    s "No. I’m just being an asshole because I’m not entirely sure how I’m supposed to talk to you after you stole my number out of your girlfriend’s phone."
    s "Does this mean you’re in love with me now?"
    os "I don’t know. Do you have a vagina?"
    s "Not that I’m aware of. "
    os "Then it’s probably safe to assume I’m not in love with you. "
    s "Why {i}steal{/i} it, though? Why not just {i}ask{/i} Wakana for my number if you really wanted to check in on me? I’m sure she wouldn’t mind."
    os "Because I don’t want her to know about this."
    s "Ahh...so you really {i}are{/i} in love with me then."
    os "Yup. You got me. But confessing over the phone is so lame and, being the old-fashioned, heterosexual woman I am, I’d like to tell you how I really feel in person if that’s okay."
    s "You’re asking me to hang out? {i}Behind{/i} Wakana’s back? As in, she can’t know about it?"
    os "Yup."
    s "This isn’t about soup, is it? Because I’ve already been through that with her before and I was not able to help in any capacity."
    os "I can make my own fucking soup. Now, drag your sorry ass out of bed and come talk to me at the dojo. "
    os "There’s no class today, so I can promise it’ll be just the two of us."
    s "That will come in handy considering all of the heterosexual sex we’re going to have together."
    os "Yeah. Can’t wait. Penis rules. When can you meet?"
    s "Give me a couple hours. I have to make my niece breakfast and do a few things around the house."
    os "You know how to cook?"
    s "No."
    os "Oh."
    os "Well, good luck then. Give me a call whenever you’re free. I don’t have anything going on today."
    s "Yeah...sounds good."

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "I hang up the phone and stare at the ceiling for a few more minutes, wondering what Osako could possibly want to see {i}me{/i} for. "
    "But I don’t wonder for long as I need to make sure Ami has everything she needs before I leave the house."
    "I make my way into her room and sit by her bedside for a moment."
    "She’s still asleep. That’s almost all she does now. But I find comfort in the fact that she might be happier when she’s dreaming as that’s how it always was for me."
    "I focus on her chest, watching her lungs expand and contract while thanking {i}something{/i} out there that hers still function. "
    "But as I get up off the floor and leave the room, I’m stricken with a depressing realization."
    "It’s the fact that I can leave at all."
    "It’s the fact that I don’t have to worry about anyone breaking in to save {i}her{/i} when {i}she{/i} had to deal with that on an almost constant basis."
    "I deserved rescue far less than she does."
    "I deserve nothing at all."
    "Yet I continue to reap the few benefits there are to existing while she gets spaghetti for the fifth day in a row because it’s all I’ve figured out how to cook. "
    "It’s fine, though."

    s "..."

    "She looks cute with short hair."

    scene sky
    with dissolve2

    "I lock the door behind me and leave a note on the table that Ami probably won’t read."
    "But it’s there if she needs it."
    "Now, all that’s left to do is figure out why Osako wants to talk to me in person."

    play sound "static.mp3"
    scene osakobeatsyoass2 with flash
    stop sound

    os "HA!"

    "I quickly discover that she just wants to kill me."

    s "Ngh!"

    scene osakobeatsyoass3 with hpunch

    os "HAAAA!"
    s "Keh!"

    scene osakobeatsyoass4 with hpunch

    os "HAAAAAAAA!"
    s "e "

    play sound "static.mp3"
    scene osakobeatsyoass5 with flash
    stop sound

    os "Okay! I feel better now."

    "If I had known this was coming at the time of my departure, I would have noted something about my death in my letter to Ami. "
    "Somewhat regretfully, I will die by the hand of a lesbian."
    "Or...foot, I guess would be more accurate."
    "Either way, it’s kind of beautiful that I, a man who has taken advantage of so many unassuming women, will be put out of my misery by a woman with no interest in men whatsoever."

    scene black
    with dissolve2

    "Goodbye, world."
    "..."
    "Again, no response."

    scene theend
    with dissolve2
    $ renpy.pause(2, hard=True)

    os "Oh, come on. Stop acting dead. If I wanted to kill you, I would have just done it."

    scene osakobeatsyoass6
    with dissolve2

    s "Go on then. Finish the job."
    os "Wow. You really {i}are{/i} down in the dumps, aren’t you? You didn’t even {i}try{/i} fighting back today."
    s "You’d think that might cause you to go a little easier on me..."
    s "I’m glad you didn’t, though. I both deserve {i}and{/i} needed this. "
    os "Then why not stand back up and let me kick you some more? You’re actually pretty good as a punching bag."
    s "Sure. Just as soon as I regain control of my limbs."
    os "Wow. You might be even more of a masochist than me. "

    scene black
    with dissolve2

    s "It really does feel like that sometimes..."
    os "Come on. I’ll help you up."

    "Osako rolls me onto my back and slaps my face a few times, which I don’t think is an official karate move, before grabbing my shoulders and pulling me upward."

    scene osakobeatsyoass7
    with dissolve

    "She props me up using her hands for a few moments until I’m able to prevent myself from falling over."
    "Meanwhile, I begin to count down the minutes until I’m killed by cranial internal bleeding."

    os "What’s {i}that{/i} look for? I basically just saved your life."
    s "Yeah, that’s why I’m mad."

    scene osakobeatsyoass8
    with dissolve

    os "Oh? So it’s {i}okay{/i} for me to kill you? I thought you were joking when you told me to finish the job."

    scene osakobeatsyoass9
    with dissolve

    s "I both was and wasn’t. If you haven’t noticed, I’m kind of going through a lot of shit right now."

    scene osakobeatsyoass10
    with dissolve

    s "Thanks for at least making me {i}feel{/i} alive, though. I’ve been so numb to everything lately that this is, depressingly, the most fun I’ve had since October."
    s "And by “fun” I essentially just mean “something I don’t inherently despise.”"
    os "Uhh...can I have my foot back?"
    s "No. This is for my protection and yours."

    scene osakobeatsyoass11
    with dissolve

    os "How does this protect me in literally any way whatsoever?"
    s "It protects you from being jailed for manslaughter."
    os "You know what? Fair."
    os "Are you really that messed up, though? Because I get that...unexpected tragedy can put us out of commission for a while, but it’s been {i}months,{/i} man. What’s going on?"
    s "Well, first off, it’s only been months for {i}you.{/i} I was unconscious for the vast majority of that time. And I wouldn’t have come here if I’d known you were going to make me talk about it."
    os "Okay. Then we {i}won’t{/i} talk about it. I don’t need to know any of the specifics. But like, half the reason I called you here was to try and whip you back into shape."

    scene osakobeatsyoass12
    with dissolve

    s "And the other half?"
    os "...Heterosexual sex?"

    scene osakobeatsyoass13
    with dissolve

    s "Hah...Wakana again?"
    os "We’ll get to that later! Let’s talk about {i}you{/i} now. But...in a way that doesn’t trigger your sudden interest in pain and death and stuff."
    s "Just go back to kicking me. There’s no way I can do that."
    os "Not with that attitude, there’s not. And maybe I’m jumping the gun here, but if you ever {i}want{/i} to feel any better, moping around like this isn’t going to do you any good."
    s "Who says I want to feel better?"

    scene osakobeatsyoass14
    with dissolve

    os "Well...who in their right mind {i}wants{/i} to feel like shit? What do you gain from that?"
    s "I don’t know...retribution?"
    os "{i}Retribution?{/i} Are you some kind of character in one of Shakespeare’s plays all of a sudden?"

    scene osakobeatsyoass15
    with dissolve

    s "I guess Romeo and I do have our similarities."
    os "Listen, I’m not going to sit here and pretend that you’re a good guy when you do some {i}very{/i} questionable things with your students on an almost routine basis."
    os "And you know...maybe you {i}do{/i} deserve to be punished for that. Hell, I’ll be the first to admit that the reason I went so hard on you today was to get some of my {i}own{/i} anger out."
    s "You don’t say."
    os "But it feels {i}worse{/i} now that I know you {i}wanted{/i} it. Like, punishment’s only punishment if the person being punished hates it. I get very little joy from {i}putting you out of your misery.{/i}"
    s "Then I’m sorry you did not adequately enjoy beating the shit out of me."
    os "Stop whining for a second and listen to me, man."

    scene osakobeatsyoass16
    with dissolve

    os "How do you think everyone feels when they see you like this?"
    s "They barely see me at all anymore. "
    os "Then how do you think they feel {i}knowing{/i} you’re like this?"
    os "Warranted or not, there are a lot of people who really care about you. And I’m not saying you need to hurry up and “get over it” for all of their sakes as I know that’s straight up impossible."
    os "But feeling sorry for yourself all day every day is just going to make it even harder to get out of bed than it already is. And sooner or later, you’re even going to run out of shitty ways to internally insult yourself."
    os "Trust me on this. Feeling sorry for myself is probably my number one hobby after kicking stuff."

    scene osakobeatsyoass17
    with dissolve

    s "But that’s where we’re different. You feel sorry for yourself because you’re insecure. I {i}don’t{/i} feel sorry for myself at all. I {i}hate{/i} myself. And pretending I {i}don’t{/i} makes me feel even worse."
    s "So what am I supposed to do? Just act like everything’s okay so no one else worries while I continue to decay from the inside out? Mope around and try to stop it, just to make everyone else sick?"
    os "Is being a better person just...not an option? "
    s "I was {i}trying.{/i}"
    s "And just when I felt like I was finally starting to {i}do{/i} better, I was punished for it. "
    s "Now, the only thing that {i}really{/i} mattered to me is gone and the only lesson I learned is to always do what I’m told or everything will fall apart."
    s "At least you’re free, Osako. And I’m here just struggling to comprehend how I’m supposed to feel human when I’m constantly reduced to a pawn in some...divine game of chess."
    os "Man, now I don’t even {i}want{/i} to kick you. That’s depressing as hell."
    s "Tell me about it."
    os "Who was it that punished you, exactly? Your...niece? Yourself? What did that mean?"
    s "Let’s just say it was a voice in the back of my head and call it a day."
    os "How are we gonna call it a day there? That’s like, the most vague bit of information you’ve given me so far. "
    os "As long as you’re being honest about it, I mean. But why would you even lie to {i}me{/i} in the first place? "
    s "The thing is, it’s hard to say if I’m being honest at all. I don’t really know. "
    s "Weird shit just...kind of happens to me sometimes. Chunks of the day disappear. My body acts on its own. I hear things. And some of the dreams I have are just..."
    s "It’s hard. "
    os "Do you want me to kick you again?"

    scene osakobeatsyoass18
    with dissolve

    s "I think that’d be great, actually."
    os "Then I think you’re going to have to release your grip on my foot."
    s "Will it immediately spring back up and knock me out? Or are we standing back up first? I just want to know when I should brace myself."
    os "We can stand back up first."

    scene black
    with dissolve

    s "Fine. Then-"

    play sound "thump.mp3"

    s "Ngh!"
    os "Oh, shit. That was harder than I thought it would be. Are you okay?"
    s "M..."
    s "More weight..."
    os "Okay, maybe we should finish up for the day."

    $ renpy.end_replay()
    $ osakospring1 = True

    jump osakospring2

label osakospring2:
    scene sky
    with dissolve2

    "Osako helps me back up and, after taking a moment or two to remember who I am, {i}where{/i} I am, and the reason I came here, we exit the dojo and begin to head to-"

    s "Osako, where are we going?"
    os "I’m kidnapping you."
    s "Why? No one’s going to want to buy a washed-up creep in his early 30s off of you."
    os "I’m sure Ayane would pay. Maybe even that other girl who was thinking about buying the dojo way back when. I don’t know. I’ll find out later."

    "Okay, so I guess I’m being kidnapped."
    "If I had known this was coming at the time of my departure, I would have noted something about my disappearance in my letter to- "
    "Actually, haven’t I already crossed this line of thinking once today?"

    s "I think you might have given me brain damage."
    os "Is that a good thing or a bad thing? Because you seem a little less miserable than you were a few minutes ago. Maybe I kicked the sadness out of you?"
    s "Maybe. Let me think about it for a second."

    stop music
    play sound "static.mp3"
    scene circle with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene sky with flash
    stop sound
    play music "ame.mp3"

    s "Nope. I’m still overflowing with pain. And now I {i}also{/i} have to worry about the living conditions in whatever warehouse you’re going to stash my body in until you can find a buyer. So thanks."
    os "Damn. I’ll have to kick you a little bit harder next time."
    s "Where are we going? For real. Because I have to get back home soon."
    os "Isn’t your niece in high school? Why can’t she go a few hours without parental supervision?"
    s "Because her hair is short now."
    os "What? So is mine and I look after myself all the time."
    s "It’s complicated. Just tell me where-"
    os "Food. I think I owe you a meal after almost killing you. Plus, being so much stronger than you really worked up an appetite on my end. "
    s "I think you’re taking more pleasure in my misery than you’re supposed to. Everyone else has been very sensitive and understanding and you’re too busy leveraging your strength to even care."
    os "Yeah. I guess I just hate you, then. Where do you want to eat?"
    s "Next to someone who won’t hurt me."
    os "How about here? Here looks good."

    scene osakodiner1
    with dissolve2

    "Osako drags me into an American style diner that is so authentic I can barely make out any of the menu items as they’re all in English. "

    s "Why here? Why would you say this looks good?"
    os "Because you would have just cried for the next ten minutes instead of deliberating. Plus, I’m used to Wakana never knowing where to eat and have decided to just start picking the first thing I see."
    os "It’s a strategy that’s yet to let me down. But I’m anticipating an end to that streak today as it seems like you’re out to ruin everything you come across."

    scene osakodiner2
    with dissolve

    s "I’m not {i}out{/i} to do that. It’s just a side effect of my existence."
    os "Well, whatever it is, cut it out. Because you had your turn to complain and now its mine. "
    s "I think I deserve more time to complain as I don’t get to do it very often and you do it virtually every time Wakana looks at you the wrong way."

    scene osakodiner3
    with dissolve

    os "And more recently, when she doesn’t look at me at all!"
    s "You seem unusually...jubilant for someone who is about to spill their heart out."

    scene osakodiner4
    with dissolve

    os "I kind of have to be. If we both spend the whole afternoon moaning, the wait staff will-"
    s "Think we’re having heterosexual sex?"
    os "I was going to say “kick us out.” But yours is way worse and I’d like to avoid anyone thinking that at any and all costs."
    s "I like having a lesbian friend who says degrading things to me. This is the most fun I’ve had since the last time I told you this was the most fun I’ve had roughly thirty minutes ago."
    os "You really are a masochist, huh?"
    s "A verbal one, I guess. I’d get soft if you slapped me."
    os "Are you saying it’s hard right now?"

    scene osakodiner5
    with dissolve

    s "Hard to be alive."
    os "..."
    os "Okay. Well, I’m gonna go grab a table. "

    scene osakodiner6
    with dissolve

    s "And I’m going to stand here until my feet fuse with the tiles and my legs need to be amputated in order to get me to leave."
    emp "Please don’t do that, sir. We’re understaffed as it is."
    s "I’m sorry, but this is the fate that I’ve chosen for myself."

    scene osakodiner7
    with dissolve

    os "Okay. Come on, Grandpa. Let’s get you into your chair."
    s "Why does everything have to hurt so much?"

    scene black
    with dissolve2

    os "Forgive him. He’s {i}very{/i} old. He just looks young because he...eats well."
    s "Help. She abuses me when no one is around and won’t listen to my problems."
    emp "God, I need a new job..."

    "........."
    "......"
    "..."

    scene osakodiner8
    with dissolve2

    "We grab a seat near the window instead of one at the bar as I’d rather be dyed gold by the setting sun than painted black by the intangible arms of the words I will soon spit out."
    "Osako orders a hamburg steak. I order nothing."
    "She doesn’t like that, so she orders a pork cutlet set and then slides it over to me once it arrives several minutes later."
    "I’ve been trying to avoid good food as Ami doesn’t get to have any and it seems wrong for me to partake in one of the pleasures of life while she can not."
    "I’m sure everything would just taste grey to her right now anyway, though."
    "I hope she recovers soon. And not just because it will free up some more time in my schedule and my mind."
    "But because I love her."
    "I really do love her."
    "And it’s my fault she’s like this."

    os "Are you really gonna sit there and frown for the entire meal? I bought you food. Eat it."
    s "Can we just get the sad part out of the way first? Because I really don’t want to take a bite out of this if you’re going to get all self-loathing a few seconds in and cause me to stop."
    os "Oh, shut up. I {i}am{/i} going to complain, but it’s actually not about {i}me{/i} this time. I’m perfectly normal and perfectly fine."
    s "Well, way to rub it in."
    os "There’s no winning with you when you’re like this, is there?"
    s "Probably not, no."

    scene osakodiner9
    with dissolve

    os "Pfft. I see now why Wakana likes you so much."
    os "You’re actually really similar in a lot of ways. And I’d wager she’s even more stubborn than you are."
    s "You’d probably lose, then. Because at least Wakana was willing to change some of what she was doing to appease you. "

    scene osakodiner10
    with dissolve

    os "Change what she was doing to appease me? But what did-"

    scene osakodiner11
    with dissolve

    os "Oh! You’re probably talking about the medication, aren’t you? Yeah. She’s gotten a lot more responsible after I talked to her about that stuff."
    os "But I feel like that’s less “being stubborn” and more “Hey, I probably shouldn’t die right now.” Regardless of her catch phrase, of course."
    s "Well, there’s {i}one{/i} thing to cross off the similarity list because I definitely-"
    os "If you talk about how you want to die one more time today, I am going to take these chopsticks and insert them into your eyes. Then, I am going to eat your eyes. Then, you won’t have eyes anymore."
    os "Is that really the path you want to go down? One without eyes?"
    s "It would definitely make not giving into temptation easier."

    scene osakodiner12
    with dissolve

    os "God, it’s like talking to a big, ugly wall."
    s "You’re only saying that because you’re scared of penises."
    os "Well {i}sorry{/i} for not being attracted to your weird, fleshy sex-tumor with the capability of shooting out liquid babies."
    s "Apology accepted. Enjoy your equally fleshy meat-pocket that {i}real{/i} babies crawl out of."

    scene osakodiner13
    with dissolve

    os "Never call it a meat-pocket again."
    s "I’m sorry. But on the bright side, I think that’s the closest I’ve come to making a joke since coming out of my coma."
    os "You call that a joke?"
    s "Somewhat reluctantly, yes."
    os "..."
    s "So, you were comparing me to the woman you have sex with?"

    scene osakodiner12
    with dissolve

    os "Somewhat reluctantly, yes."

    scene osakodiner14
    with dissolve

    os "You see..."
    os "Apart from the fact that you’re both stubborn teachers with...fatalistic tendencies and other assorted mental issues, you’re both kind of...caught up on the same thing right now."
    s "I have a very hard time believing that Wakana is going through something even remotely similar to what I’m going through as the only thing she loves is sitting directly in front of me."
    os "No, I mean..."
    os "She’s caught up on {i}you.{/i}"
    s "...What?"

    scene osakodiner15
    with dissolve

    os "Ever since you went into that coma thing, she’s been...obsessively looking into what could have caused it."
    os "She’s scoured like, every single poem your niece has ever written. To the point where even {i}I’ve{/i} memorized a few of them. And she’s starting to sound like some kind of...conspiracy theorist."
    s "..."

    scene osakodiner16
    with dissolve

    os "And, you know...I thought you coming {i}out{/i} of that would have put an end to it. And I’d get my normal- well...normal-{i}ish{/i} girlfriend back once you were {i}alive{/i} again. But that’s not the case at all."
    os "Almost nothing’s changed. She’s still spending almost every night trying to put things together and...it’s getting to the point where I’m not sure how to handle it."
    os "Just walking away and leaving her to it isn’t cutting it, obviously. But you know me. I’m not assertive when it comes to her. And when I {i}try{/i} to be, she just makes me feel like I don’t {i}get{/i} it."
    s "And what do you want {i}me{/i} to do about this?"

    scene osakodiner17
    with dissolve

    os "I don’t know. Would it kill you to maybe, like...talk to her? Or tell her that things are okay so she doesn’t spend the next decade trying to fix the same thing you are?"
    s "I {i}have.{/i}"
    os "What do you mean you have? When? She told me she hadn’t seen you apart from the one day at school."
    s "{i}Before{/i} I disappeared. "
    s "She’s been poking her nose somewhere it doesn’t belong for a while now. And I told her how uncomfortable it made me, which led to her apologizing shortly after."
    s "But I was under the impression she dropped it by now. {i}Not{/i} that she planned on dragging Ami into it as well. "

    scene osakodiner18
    with dissolve

    os "Fuck..."
    s "Yeah. Sorry to disappoint you."
    os "No, it’s not that. You didn’t do anything wrong. She can...be like this sometimes. "
    os "Wakana might seem straight-laced and “by the book” when it comes to school and whatnot. But when there’s something she can’t understand, she throws herself at it. Hard. And recklessly. "
    os "But most of the time, she’s able to figure it out."

    scene osakodiner17
    with dissolve

    os "But not this time."
    os "Like, she’s gone as far as theorizing that Ami might have {i}known{/i} this was going to happen. Or that she {i}wanted{/i} it to. But, like...why? Don’t you guys have a {i}good{/i} relationship?"
    s "I think “codependent” is the best word for our relationship. "
    os "Is it? Because that’s not exactly a {i}good{/i} word for any relationship."
    s "Maybe not for most people, but it works for us."
    s "She lost her parents at a very young age and I’ve been her guardian ever since. But I was a wreck back then, so it was more like {i}her{/i} taking care of {i}me.{/i}"
    s "Which is why it’s so important that I keep an eye on her now since I’m finally getting a chance to be there as more than I actually am."
    s "If you want to know why I haven’t just ended it already and why I keep half-jokingly asking {i}you{/i} to do it, it’s because of that. It’s because of {i}her.{/i}"
    s "If I’m gone, she’ll have no one. "

    scene osakodiner19
    with dissolve

    s "For the first time ever...I feel like I have a purpose."
    s "It’s just unfortunate that purpose showed up at the same time the rest of my world broke apart. "
    s "Ami’s the ledge I’m hanging onto now. And yeah, I could let go. That’d be way easier than pulling myself up, after all."
    s "But I’d fall knowing that she’d jump in after me. And {i}that{/i} is what I’m most afraid of."
    s "She doesn’t deserve to suffer over the choices I’ve made. She’s worked hard and deserves a good life."
    s "She’s just broken."
    s "And if Wakana is going to keep going through her poetry and invading her privacy by dissecting her most personal feelings-"
    os "Sorry to interrupt, but...is that really what they are?"
    s "What?"
    os "Personal feelings."

    scene osakodiner20
    with dissolve

    os "Do you know for sure that’s what she’s writing about?"
    s "I mean...what else would it be? That’s what I taught her to-"

    play sound "static.mp3"
    scene osakodiner20 with flash
    stop sound

    s "That’s..."
    s "But when did I-"
    os "Well, like...without beating around the bush, what if she’s just taking after her mom? And doing what {i}she{/i} did?"

    stop music
    play sound "static.mp3"
    scene osakodiner21 with flash
    stop sound

    os "{i}The Girl Who Cannot Breathe{/i} or whatever. That’s her, right? Because I’ve heard basically everything she’s ever written now thanks to Wakana and-"
    s "Don’t talk about her."

    scene osakodiner22
    with dissolve

    os "But-"
    s "{i}No one{/i} can do what she did."
    s "{i}No one{/i} will ever see anything the way she did."
    os "I’m just trying to say that-"
    s "If Ami is mimicking anyone, it’s {i}me.{/i} And I’m done talking about this. So either drop it, or finish your lunch alone. Pick one."
    os "..."
    s "..."

    scene osakodiner23
    with dissolve2

    os "What did she do to you, man?"

    scene osakodiner24
    with dissolve

    s "I have to get home. Ami’s waiting."
    os "You’re the “Boy,” right?! The one she always wrote about?! That was you! Wasn’t it?!"
    s "..."

    scene osakodiner25
    with dissolve

    os "She can’t hurt you anymore..."
    os "It’s over."

    scene black

    s "No it’s not."

    $ renpy.end_replay()
    $ osakospring2 = True
    $ osako_love += 10
    $ osakonumber = True

    "{i}Osako’s affection has increased by 10! But maybe it's just pity!{/i}"
    "{i}When you get home, you check on your niece. She’s still asleep.{/i}"

    play sound "vibrate.mp3"

    "{i}Your phone vibrates again. It’s a number you’ve yet to save and an apology you will not read.{/i}"

    play sound "computeryay.mp3"

    "{i}As you fight against your inhibitions and punch the name “Osako Osaka” into your contacts, you remember what she said at the diner.{/i}"
    "{i}About how she can’t hurt you anymore.{/i}"
    "{i}And you know it’s not true.{/i}"
    "{i}Because when you climb into bed that night, she’s right there beside you — making circles on your chest with her index fingernail.{/i}"
    "{i}And while you can’t feel anything, you remember the sharp sting of when she bit it too short one night and drew blood while making these same exact circles.{/i}"
    "{i}They seemed so much bigger back then.{/i}"
    "{i}You imagine they would fit around your ankle.{/i}"

    play sound "winner.mp3"

    "{i}Akira Arakawa’s [[DEPRESSION] has worsened!{/i}"
    "{i}He has learned [[GREATER FACADE]!{/i}"

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

label osakospring3:
    scene black
    with dissolve2

    "{i}Back at school, where you’re not because you’re a sensitive little bitch boy who can’t get over how he banged a teenager into oblivion...{/i}"

    scene osakodesk1
    with dissolve2
    play music "phantomthief.mp3"

    ima "So...how is this supposed to work again? Classes aren’t competing against each other, they’re competing against...{i}themselves?{/i}"
    w "No. Only {i}your{/i} class is competing against itself. The rest of the classes are competing against each other- the way athletics festivals {i}typically{/i} work."

    scene osakodesk2
    with dissolve

    ima "And...{i}why{/i} are we being singled out, exactly? Are the rest of you just too scared to go up against us since we’re obviously superior in every way?"
    w "I think it’s moreso the fact that the girls of class A refuse to venture outside of the tiny, predatorial bubble formed by your predecessor. "
    w "They’ve made a name for themselves as the outcasts of the first year. And frankly, it’s miraculous they haven’t been collectively expelled on account of how much noise they make on a daily basis."
    ima "I don’t know, Wakana. Sounds to me like the rest of you are scared."

    scene osakodesk3
    with fade

    w "We sure are. Good day."
    ima "Oh, hell nah. You wait one damn minute, Miss Watabe."
    w "I’m surprised you even remember my surname."
    ima "My roster’s imbalanced right now. I heard from Senpai that Ami’s not coming back to school any time soon, so I’ve only got 19 girls for sports day. Is one team just supposed to compete with a handicap?"
    w "Of course not."

    scene osakodesk4
    with dissolve

    w "You’ll have to kill one."
    ima "Man, for real? I barely avoided my last murder charge. You’re seriously going to make me go through that again?"
    w "Look Imani, I don’t know what you want me to tell you. None of the other classes want to participate with the girls of 1-A. "
    w "And considering I have my hands full planning out the rest of the event, it would be a big help if you could figure out what to do with your class {i}without{/i} my help."
    w "Now, is that everything? Because I’m very busy right now."

    scene osakodesk5
    with fade

    ima "Fine, yeah. I’ll figure it out on my own, I guess. The girls have been itching to do another one of those Dorm Wars things anyway. Maybe I can just combine that with this and keep everybody happy that way?"
    w "Wonderful idea so long as you can find out a way to do it without anyone indecently exposing themselves while an adult man watches from the shadows."

    scene osakodesk6
    with dissolve

    ima "So it’s cool if a few of them watch as long as they’re out in the open? "
    w "Imani."
    ima "What? It ain’t like we get paid well, yo. Can’t blame me for thinking up ways to monetize this."
    w "Leave. Now."

    scene osakodesk7
    with dissolve

    ima "Did you move your couch?"
    w "That’s it. I’m calling HR."

    play sound "doorslam.mp3"
    scene osakodesk8 with hpunch

    ima "{i}Bye, Wakana! Sorry I had to leave on such short notice!{/i}"

    scene osakodesk9
    with fade

    w "{i}Hah...{/i}"

    scene osakodesk10
    with dissolve

    w "Apologies, my sweet. That lasted longer than I thought it would."

    scene osakodesk11
    with fade

    os "You don’t think she knew I was down here, do you? Should I be nervous? Are we going to get caught?"
    w "Don’t be silly. Imani wouldn’t- oh. I get it."
    w "Yes, you should be nervous. There is a high likelihood that the two of us will be caught. Oh, how suspenseful it is to be engaged in a sexual act at this very moment."

    scene osakodesk12
    with dissolve

    os "Mm~"
    os "Wakana...I love the way you taste..."
    w "And I love the way you use your tongue to stimulate my clitoris."

    scene osakodesk13
    with dissolve

    os "You’re not enjoying this at all, are you?"
    w "What? Of course I am. Can you not tell by how wet I am?"
    os "I can’t tell if you’re wet {i}at all{/i} or if it’s just my saliva. I’ve been down here for like thirty minutes."
    w "My, has it been that long already? Would you like to switch places, my dear? I believe I could get away with locking the door for a short while now that our lovable {i}pest{/i} has gone back to work."
    os "Are you even {i}close{/i} to finishing right now? "
    w "The more you talk, the further away I move. So either shut your mouth and take your pants off or {i}open{/i} it and proceed with more clitoral stimulation."

    scene osakodesk14
    with fade

    os "You know you can tell me if you’re not enjoying it, right? I don’t want you pretending you are just to humor me."
    w "Osako, what’s gotten into you? This is hardly the time to evoke such nonsensical ideas. "
    w "If I wasn’t enjoying it, I’d simply close my legs and crush your skull. I’m just worried it might send you spiraling into a level of ecstasy I’d never again be able to replicate."
    os "Do you want me to do it softer? Faster? Should I get something from the toy box? Tell me what to do. I don’t mind. I {i}want{/i} you to do that. "
    w "Do you? Because I commanded you to stop talking and your response to that was to start spilling your insecurities all over my crotch."
    os "I just want you to cum, babe. That’s it. I want you to go crazy for me."

    scene osakodesk15
    with dissolve

    w "{i}Hah...{/i}Osako. You know that {i}going crazy{/i} isn’t in my repertoire. My body can’t handle it."
    os "But your body handles handling {i}my{/i} body just fine. Why does it only become an issue when I touch {i}you?{/i}"
    w "I’m not sure, my love. I’m likely just too immersed in pleasuring you to notice the pain most of the time."
    os "Do you want to change positions then? Will laying down help? What can I do?"

    scene osakodesk16
    with dissolve

    w "You can stop worrying and lick my pussy any way you like. "
    os "That just makes it sound like I’m doing it for {i}myself,{/i} though. "
    w "Osako...I don’t know what you want me to tell you right now. You’re not doing anything wrong. It’s just harder for me to {i}finish{/i} than it is for others on account of my injuries. "
    os "When was the last time you even came? Be honest."

    scene osakodesk17
    with dissolve

    w "Was it not the last time we had sex? "
    os "No. Or the time before that. Or the time before {i}that.{i} "
    os "And any further back I don’t remember since you had your nose buried so far up Ami’s notebook that you may as well have been eating {i}her{/i} out."

    scene osakodesk18
    with dissolve

    w "I can not begin to express how uncomfortable that sentence just made me feel. "
    os "Yeah, well...it seems like nothing I do can make you {i}comfortable,{/i} so we might as well just stop for today."
    w "What? But-"

    scene black
    with dissolve

    w "Osako, what do you think you’re doing?"
    os "Moving the...couch back since you’re too weak to do it yourself."
    w "You don’t...{i}ugh.{/i} "
    w "Why today?..."

    scene osakodesk19
    with dissolve2

    os "Why today {i}what?{/i}"
    w "Kitten, why do you think I invited you here today? While I’m working?"
    os "I don’t know. Is there any other furniture you need moved around?"
    w "Osako, no. It’s because I {i}know{/i} I’ve been neglectful lately and I was hoping to do something special for you to try and make up for that. And you {i}love{/i} sex in somewhat public places."
    w "It wasn’t my intention for you to take my...inadequacy as a partner this deeply to heart as I can promise you this is not an issue with anything {i}you’re{/i} doing. This is {i}my{/i} fault."
    os "Well, blaming yourself isn’t going to make me feel better either."
    w "Then what {i}is?{/i} What can I do? "
    os "Cum."
    w "What, {i}now?{/i}"
    os "..."

    scene osakodesk20
    with dissolve

    w "Ah...ahh.....ah!"
    os "Wakana."

    scene osakodesk21
    with dissolve

    w "Oh, come on. That was funny."
    os "..."
    w "You’re not amused, are you?"
    os "I’m not amused."

    scene osakodesk22
    with dissolve

    w "Look. I’m sorry, okay? I wish it was easier for me to reach climax as well. But given what I’ve been through, I’m lucky I can even {i}walk.{/i}"
    w "Orgasms just...they’re rare. But just because I don’t always {i}finish{/i} doesn’t mean I’m not enjoying what we do. It still feels {i}good.{/i} I still like {i}doing it.{/i}"
    os "You like doing things to {i}me,{/i} though. I rarely even get the chance to do stuff to you and any time I {i}try{/i} it just makes me feel like a loser."
    w "I’m...sorry again. And I’m sure I sound like a broken record, but it’s just hard for me sometimes. "
    os "I bet it’d be easier if I had a dick."
    w "We have like ten of them you can strap on at any moment, my love."
    os "No, I mean like..."
    os "Like what if you’re not actually as into girls as you think you are?"
    w "Excuse me? What is that supposed to mean?"

    scene osakodesk23
    with dissolve

    os "Like...what if the reason you never finish is because you’re more attracted to men? What if you don’t like me the way you {i}think{/i} you like me?"
    w "Well, first off, I don’t just {i}like{/i} you. I love you. And I’ve made a vow to stay by your side for as long as you’ll have me. "
    w "And, as far as this {i}doubting my attraction to women{/i} thing goes, I’m not sure {i}where{/i} that comes from, but I want it to stop. That was one of the most ridiculous things you’ve ever said to me."
    w "Frankly, I’m kind of offended."
    os "I just..."

    scene osakodesk24
    with dissolve

    os "You’ve never tried it before, Wakana! "
    os "Like...what if you’re doomed to a life of unreachable climaxes because you’re more sexually compatible with men than you are with me?!"
    w "You’ve never fucked a man either, Osako. Does this mean {i}I{/i} get to start accusing {i}you{/i} of depriving yourself of a more ideal future the next time you don’t cum in five minutes?"
    os "No, because {i}I’m{/i} not sexually attracted to men and {i}you{/i} are! Also, I pretty much always cum in five minutes! I am very weak to sexual contact!"
    w "And I am very aware of that. I’m just saying that you sound ridiculous right now. I don’t need to have experienced sex with a man to know that {i}you’re{/i} the one I want to be with."
    os "Well..."

    scene osakodesk25
    with dissolve

    os "Well...I..."
    w "You {i}what?{/i} You’ve already offended me by even suggesting this. You might as well just get it {i}all{/i} off your chest while we’re here."
    os "I..."

    scene osakodesk26
    with dissolve

    os "I think you have to try it at least once!"
    w "..."

    scene osakodesk27
    with dissolve

    w "What are you suggesting to me right now?..."
    os "I just...I don’t want you to go the rest of your life never knowing whether or not {i}I’m{/i} actually the right person. "
    w "What is it you want me to {i}try,{/i} Osako? Say it out loud."
    os "I can’t."
    w "But you have no problem asking me to do it regardless?"

    scene osakodesk28
    with dissolve

    os "I don’t {i}want{/i} you to do it! It took me forever to even work up the courage to suggest this! "
    w "{i}Courage?{/i}"
    w "You think you’re acting {i}courageous{/i} right now? By assuming I’ve just decided to {i}settle{/i} for a woman? By acting like you know what’s better for me than {i}I{/i} do?"

    scene osakodesk29
    with dissolve

    os "Wakana, I just want you to be happy..."
    w "Osako, I think you should leave for the day. I have work to do."

    scene osakodesk30
    with dissolve

    os "Okay...I’m sorry. "
    os "I didn’t mean to make it sound like...like however it must have sounded to you..."
    w "It {i}sounded{/i} like you were content with just...giving me away to someone else. And frankly, that’s not something I ever expected to hear out of you."
    os "Wakana..."
    w "I need time to think about this. "
    w "Please leave."

    scene black
    with dissolve2
    stop music fadeout 10.0

    os "Are you still coming home tonight?..."
    os "Can we talk more later?..."
    w "Oh, you don’t have to worry about that. I’m sure we’ll be having a {i}very{/i} lengthy and uncomfortable discussion about this topic soon since you’ve been apparently sitting on it {i}forever.{/i}"

    play sound "dooropen.mp3"

    os "{i}I’m sorry...I’m really sorry...{/i}"
    w "..."
    w "I’ll call you after work."

    "{i}The couple’s mutual affection has decreased by 5!{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ osakospring3 = True

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

label osakospring4:
    scene osakonewhair1
    with dissolve2

    "What I {i}can{/i} do, though, is finally talk to Osako about her cool new haircut."

    s "And now it’s time for the main event."
    os "You leaving and me preparing for my next class?"
    s "You don’t have another class. It’s all in your head."
    os "There are a lot of things in my head right now, but I can assure you that my schedule is not one of-"

    scene osakonewhair2
    with dissolve

    os "Wha-"
    s "I’m sorry. I’ve been just overcome by an immense need to ruffle your hair up."
    os "Right. But, just to remind you, I probably could have been an Olympian if I applied myself. So you invading my personal space is-"
    s "Your hair is so soft now."

    scene osakonewhair3
    with dissolve

    os "What do you mean “now?!” I’ve never let you touch me before! And I’m not about to start just because of your “immense needs!”"

    scene osakonewhair4
    with dissolve

    s "Sorry. I’ve gotten it out of my system. I’m just not used to you looking so cute."
    os "Yeah, well...it was just time for a change. But not the kind of change that makes it okay for you to lay your gross fingers all over me. "
    s "They’re not gross."
    os "How many girls have they been inside now?"
    s "Not enough. Also, you like girls."
    os "Yeah, but the ones {i}I{/i} like are a little older. So if you do that again, I’m just going to break your entire arm off."
    s "Fair enough. But I would now like to press you about why you felt the need for a “change” as it coincides with a thing that’s been on my mind a lot lately."
    os "Don’t you have better things to do with your time than worrying about a pair of local lesbians?"
    s "There’s saving the world, but that’s just really hard."

    scene osakonewhair5
    with dissolve

    os "You’re seriously still worried about us?"
    s "Yes. And even more so now that you’ve changed your hairstyle. That’s a breakup move. "

    scene osakonewhair6
    with fade

    os "It’s not {i}always{/i} a breakup move, you know. Sometimes, a girl just...wants to change up her look."
    s "Is that what’s happening this time?"

    scene osakonewhair7
    with dissolve

    os "Kind of, yeah."
    s "So you two are still together?"
    os "Kind of, yeah."
    s "Being “kind of” together doesn’t really bode well for the future, Osako."

    scene osakonewhair8
    with dissolve

    os "Yeah, you think I don’t fucking know that?"
    os "Sometimes, it feels like the only reason we’re still together {i}at all{/i} is because it would be too inconvenient to break up. "
    os "But dwelling on it any longer isn’t going to do me any good. So I figured- hey. What signifies a fresh start better than a...fresh hairstyle?"
    s "We could always have another foursome. That seemed to work pretty well at reigniting your chemistry last time."

    scene osakonewhair9
    with dissolve

    os "Almost {i}too{/i} well. But I’m going to throw myself into blissful ignorance and just assume that was a coincidence."
    s "So are you two just...on a break now or something?"

    scene osakonewhair10
    with dissolve

    os "No...it’s not like that."
    os "We’re still together. We’re still living in the same house and sleeping in the same bed, but...there are some things that have to change if we’re going to get back to the way we were."
    os "And, as you may have guessed, they’re mostly on my end. So I’m just trying to...focus on myself for now. Put myself in a better head-space."
    s "Why would I guess that {i}you’re{/i} the problem when Wakana’s got the downer mindset of Edgar Allan Poe and the medicinal tendencies of Heath Ledger?"
    os "Because {i}I’m{/i} the one with less self-confidence than a rabbit being chased by a fox. "
    s "Wakana is many things, but I’m not sure a “fox” is one of them. At least not in the...animal sort of way."

    scene osakonewhair11
    with dissolve

    os "Please refrain from subtly voicing your attraction to my girlfriend even {i}if{/i} we’re in a bit of a tight spot right now."
    s "It’s not just Wakana. I’d also like to be in a tight spot with {i}you{/i} if you know what I’m saying."

    scene osakonewhair12
    with dissolve

    os "All {i}I{/i} know is that I’m suddenly nauseous."

    scene osakonewhair13
    with dissolve

    os "And also that...this has been in the works for a long time. You’ve known from the start that I’m pretty much always kind of...worried when it comes to my relationship with Wakana."
    os "And I guess that...has just finally weighed on her a little too much with some of the things I’ve been saying to her."

    scene osakonewhair14
    with dissolve

    os "So I’ve started working on Osako 2.0 — the new, confident and cool model who will be able to give her partner tons of love and tons of orgasms."
    s "I see. "
    s "So the time has finally come for the apprentice to teach his master. What you want to do with your hands is-"

    scene osakonewhair15
    with dissolve

    os "I don’t need your help with sexual stuff, Akira! That comes down to...finding the right medication or...something. "
    s "You don’t sound very confident about that, Osako."

    scene osakonewhair16
    with dissolve

    os "I KNOW! ARE YOU NOT PAYING ATTENTION?! THAT’S LIKE THE ROOT CAUSE OF ALL OF MY PROBLEMS!"

    scene osakonewhair17
    with dissolve

    os "Regaining my confidence is just one step on the way to a new me — one whose existence doesn’t entirely revolve around her partner."
    os "I’m going to live how {i}I{/i} want to live, and Wakana is going to see that I’m not just...some robot who was put here to want to fuck her."
    os "And if I have to sideline love for a little while in order to do that, fine. She’s made it clear that she’s not going anywhere if I’m going to actively try and change. So that’s what this is."
    s "So I have {i}her{/i} to thank for your cool, new haircut. Got it."
    os "In a roundabout way, I guess so. But with new hair comes new...other stuff. And from this point on, the Osako Osaka you know is going to be better and more likable."
    s "Awesome. So what’s the next step now that you’ve cut your hair?"

    scene osakonewhair18
    with dissolve

    os "I have no fucking clue. All I do apart from letting Wakana put stuff inside me is work. I think I need to...find a hobby or something. What do {i}you{/i} do for fun, Akira? "
    s "I-"
    os "Besides Ayane and Imani and whoever else you subject to your gross man-hands."
    s "Oh."
    os "Is there even anything else? Or is that literally all you do?"
    s "I mean..."
    s "I guess there’s porn?"

    scene osakonewhair19
    with dissolve

    os "Your hobby is porn?"
    s "The heart wants what the heart wants, Osako."
    os "I think you’re confusing your heart with that weird, fleshy growth between your legs."
    s "Yeah...I do that a lot, actually."
    os "So, do you have any idea of other things I can do that {i}don’t{/i} involve making porn a major part of my life and free time?"
    s "No, not really. Let’s get really into porn together."
    os "I think I’d rather just break up with Wakana at that point. "
    s "You’ll cave. I know you."
    os "No, you know the {i}old{/i} me. The new me doesn’t do stuff like that."
    s "Yes she does."
    os "No she doesn’t."
    s "Yes she does."
    os "No...she doesn’t."

    stop music
    play sound "static.mp3"
    scene osakonewhair20 with flash
    stop sound
    play music "citylife.mp3"

    os "I fucking hate you, Akira. "
    s "Called it. This is great, though. Because now we can start a porn club."
    maki "I already have one! It’s called “Maki Miyamura’s MILF of the Month Membership — where mammaries become memories.”"

    "I meet up with Osako later that night after her shift at the maid cafe. "
    "And while she verbally disapproved of this affair becoming her next hobby (many times), it’s the only thread we have in common and the only way I can see myself {i}helping.{/i}"
    "I just hope she doesn’t feel weird about watching porn next to a heterosexual male that she will never want to have sex with as a tried and true lesbian woman."

    os "You know, as a tried and true lesbian woman, I’ve gotta say — it feels kind of weird watching  porn next to a heterosexual male that I will never want to have sex with."
    maki "Yay! That sentence implies it’s possible you’ll want to have sex with me one day. And while many others might be disturbed by that, I actually find it rather flattering."
    s "Be careful, Maki. Osako is “kind of” in a relationship right now and you don’t want to step on her toes."

    scene osakonewhair21
    with dissolve

    maki "Kind of? Are you and Watabe-sensei still having trouble? Did the Official Dildo Saber not fix everything? Because it says on the box that it’s supposed to."
    s "Oh, right. You already know each other because Osako is a freak."
    os "Some jobs just require certain tools and not all of us have them built into our bodies. But no, we’re fine. Ish. That’s not why I’m here, though."
    maki "So you {i}are{/i} going to join the MILF of the Month club?"
    os "I...don’t think so. I’m not really a MILF girl. "
    maki "Not {i}yet{/i} you’re not. But only because the film we’re watching today hasn’t had a chance to convert you yet."

    scene osakonewhair22
    with dissolve

    maki "Behold! The star of September — Reiko Kobayakawa! At only 41 years of age, she’s already starred in hundreds of films! "
    maki "Born in Tokyo and {i}coming{/i} in at 165cm, her three sizes are 35/24/35! Making her not {i}just{/i} an excellent role model for young women everywhere, but wonderfully proportionate!"
    os "Did you...memorize all of that for the sake of your club? Or..."
    maki "No. I memorized it for the sake of my {i}heart.{/i}"

    scene osakonewhair23
    with fade

    os "I see..."

    "I tear myself away from September’s MILF of the Month and watch Osako as she...watches her. Which is weird. I know. But seeing her in a context like this is...kind of interesting to me."
    "Like, maybe the two of us really {i}can{/i} become porn buddies? And-"

    os "Please stop staring at me while a MILF is being audibly railed right in front of you."
    s "I’m sorry. I was just thinking of how nice this is."

    scene osakonewhair24
    with dissolve

    os "{i}Why?{/i}"
    s "Well, it’s just that everyone else I know wants to sleep with me. But with you, I can kick back and relax and enjoy my hobbies without having to worry about that."
    os "Surely it’s not {i}everyone.{/i} Like, you’re not banging Maki, are you?"

    scene osakonewhair25
    with fade

    if makisex == True:
        maki "Not {i}currently.{/i} We can. I’d just have to charge you the live performance fee. And also ask you to vacate the couch since the floor is kind of sticky in here."

    else:
        maki "He would be if I had anything to do with it. But breaching parent-teacher norms with me seems to be out of the question at this point in time for our friend here."

    os "Oooookay. Then I guess maybe I {i}might{/i} be the only person you can do this with. But that doesn’t mean I {i}want{/i} to."
    s "But you’re here, aren’t you?"
    os "Yeah — but that’s only because I’m trying to find a new hobby, remember?"

    scene osakonewhair24
    with fade

    os "Chances are, I’ll be trying out a bunch of new stuff in the near future. And getting this one out of the way early will at least get you off my back for a little while."
    s "“Trying a bunch of new stuff” you say?"
    os "Are you actually even attracted to me? Or are you just being non-stop flirty today because you know nothing’s going to come of it?"
    s "Probably both. It’s fun being able to test how smooth I am on someone who isn’t going to cave."
    os "Wow. I’m starting to think you might be more in-need of new interests than me and {i}your{/i} relationship isn’t teetering on the edge of destruction right now."
    maki "If you’re looking for a new hobby, how about fishing?"

    scene osakonewhair26
    with fade

    os "Fishing?"
    s "This again?"
    maki "It’s what my husband used to do when he was looking to clear his head. And based on that “teetering on the edge of destruction” comment, it sounds like that might help."
    maki "Porn is great and all. Like, don’t get me wrong — it’s my favorite thing in the world. But I can see how it wouldn’t be...beneficial during times like this."
    maki "Even if I don’t really grasp what the specific issue is."
    s "Osako’s trying to be more confident and independent so her entire existence stops revolving around her significant other."
    maki "Oh. Well, maybe fishing’s {i}not{/i} the best bet then. Maybe you should become a race car driver."

    scene osakonewhair27
    with fade

    os "You two are pretty terrible at this, aren’t you?"
    s "Hey, {i}we’re{/i} not the ones who can’t figure out what to do with our lives."
    os "You’re absolutely someone who can’t figure out what to do with his life."
    s "Okay, yeah. But Maki’s not. She was born to sell sex to people. And {i}we{/i} were born to buy it."
    os "Can you please stop lumping me in with you just because I followed you to a porn shop I was probably going to come to this week anyway?"
    s "I can, yeah. But I want you to know that this is how I’m trying to connect with you because I {i}do{/i} want you to become more confident in yourself."
    s "You’re too...strong and loyal to be all miserable like this. And I want your relationship to succeed just as badly as you do."
    os "Yeah, but you only want it to succeed because you think it increases your chances of having a threesome with us one day and that is very much not the case."
    s "That’s not true, Osako. Seriously."

    scene osakonewhair28
    with dissolve

    os "So you’d {i}reject{/i} such an invitation if it ever actually happened?"
    s "I mean...no. But it’s not like I have an ulterior motive here. "
    s "I want you to get better because I want you to be happy. And I just think it would be cool if you two could go back to being happy {i}together{/i} rather than confused and...distant."

    scene osakonewhair29
    with dissolve

    os "You...do?"
    s "Obviously, yes. I’ve been trying to tell you that this whole time."
    os "Sorry, I just...don’t really get why you’re being so nice to {i}me{/i} when Wakana’s the one you’re close with. You and I are kinda just, like...{i}there.{/i}"
    s "Yeah, but we don’t {i}have{/i} to be. We {i}can{/i} be closer. I {i}want{/i} to be closer. "

    scene osakonewhair30
    with dissolve

    os "Is this about the haircut again? Because you never got like this with me until-"
    s "{i}No.{/i} It’s about me being in the same boat as you. Just instead of it being a relationship that’s teetering on the edge, it’s everything about me."

    scene osakonewhair31
    with fade

    s "I’m not happy. And I want to change too. So being around someone who {i}also{/i} wants to do that is..."

    scene osakonewhair32
    with dissolve

    s "Wait, where did Maki go?"
    maki "{i}Refilling the lotions! It seemed like you two were about to have a moment and I didn’t want to get in the way!{/i}"
    s "Well, that’s...nice."
    os "Akira, I..."
    os "I don’t really know what to say. I’ve never really thought of you on...{i}that{/i} level before."

    scene osakonewhair33
    with dissolve

    s "And I’m not saying you should now. I get that we’re not close, and that it’s hard to just...open up to people you’re not really comfortable with."
    s "But I know you care about me on {i}some{/i} level because of what you said in the diner. And I’m the type of person who can’t help but immediately latch onto any amount of affection from anyone."

    scene osakonewhair34
    with dissolve

    s "And how you kicked the living shit out of me just before we went there."
    s "I obviously can’t do that to you, so...I guess this is my equivalent. "
    os "..."
    s "But I’m clearly not good at connecting with people verbally, so..."
    os "No, dude...I appreciate it. "
    os "You’re just so fucking...odd that I can’t normally figure out when and...{i}if{/i} you’re being serious."
    os "You’d think that after dealing with Wakana for so long that I’d be able to get a grasp of that easier, but...I guess it’s a little harder when you don’t also want to screw the person in question."
    s "That’s fair. I’d probably feel the same way in your position."
    os "You really want to be closer to me?"

    scene osakonewhair35
    with dissolve

    s "If you’re okay with that, yeah."
    os "And you’re fine with me not wanting to screw you?"
    s "I am, yeah."
    os "And you’re not going to try and screw my girlfriend?"
    s "Do you want to just make a checklist for me to go over when I get home later? Because it seems like that might be best right now."

    scene osakonewhair36
    with dissolve

    os "No...it’s fine."
    os "Let’s...hang out more. Maybe we {i}can{/i} find something to do together that...isn’t sitting around and watching porn. "
    s "Are you sure it can’t be that? Because the MILF of the Month club does sound really fun. "

    scene osakonewhair37
    with dissolve

    os "You know, that Kobayakawa girl really {i}is{/i} hot. So if they’re all like this and it’s only once a month..."
    s "You think you’d ever hook up with a girl that age?"
    os "I don’t know. I’ve only been with Wakana before. But, like...isn’t that girl even younger than Rika?"
    s "You think you’d ever hook up with Rika? "
    os "She has a better shot than you do, at least."

    scene black
    with dissolve2
    stop music fadeout 12.0

    s "I want to be offended by that, but Rika’s extremely attractive and I understand completely."
    os "I’m gonna tell her you said that the next time we’re at the bar."
    s "You don’t have to. I’ll do it myself. Just not while Imani’s around. She gets jealous easily. "
    os "True. You two have sex yet?"
    s "Nah, we’re waiting until the next time all four of us are together."
    os "Okay. But if you make eye contact with me again while that’s happening, I swear to God that we’re never hanging out again."
    s "I just wanted to make sure you were doing everything correctly."
    os "Hey, remember earlier when I said I fucking hate you?"

    "Maki comes back into the room a few minutes later and the three of us finish watching the MILF of the Month have sex with...{i}many{/i} different men."
    "And despite that “film” dragging on for way longer than it had any right to, I think it’s safe to say we all had a good time."
    "And I think it’s safe to say that I’m on the cusp of having another close friend."
    "So maybe Osako can be what I {i}wanted{/i} Imani to be — someone I can spend time with and just..."
    "That’s it."
    "That’s all I need sometimes."
    "We go our separate ways."
    "But she falls asleep holding someone who sees her, and I fall asleep holding myself."

    $ renpy.end_replay()
    $ osako_love += 5
    $ osakospring4 = True

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
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

label osakospring5:
    scene nightsky
    with dissolve2
    play music "fallishere.mp3"

    "And so the moment for me to decide how I’ll be spending my night has once again reared its ugly head — casting aside choice after choice when they {i}all{/i} lead to the same place in the end."
    "Me. A girl. Some place where we can rest our bodies. Probably a leash if Chika is involved. Probably some light arguing if it’s Makoto. But no matter {i}who{/i} it is, I know what I’ll be doing tonight."
    "And there is no one who can stop me."

    play sound "phonering.mp3"
    $ renpy.pause(1, hard=True)
    play sound "phonebeep.wav"

    s "Hello?"
    os "{i}Hey. We’re hanging out tonight.{/i}"
    s "This is the biggest plot twist I have ever experienced."
    os "{i}What is? Me calling you? I’ve done that before.{/i}"
    s "Never right after I speak to myself about how I’m going to wind up having sex with whatever girl I see tonight."
    os "{i}Please don’t.{/i}"
    s "{i}Too late now, Osako. You’ve toyed with fate and must pay the price.{/i}"
    os "{i}Wow. I completely understand why you’re so popular with girls now. Who can compete with pickup lines like that?{/i}"
    s "Osako, I’m so miserable."
    os "{i}Wow. I completely understand why you’re so popular with girls now. Who can compete with emotional stability like that?{/i}"
    s "You are one of the last people I want to hear about “emotional stability” from. And I know a lot of emotionally unstable people, Osako. {i}A lot.{/i}"
    os "{i}Cool. So when are we meeting?{/i}"
    s "I don’t know. What are we doing?"
    os "{i}Something I’m pretty sure no straight guy has ever done before.{/i}"
    s "You?"
    os "{i}Yeah. Come have sex with me. I’ll send you the address now.{/i}"

    play sound "phonebeep.wav"

    "I tap on my- wait, no. My phone beeps. I look at it. "

    s "..."
    s "You want me to go all the way to the urban district?"
    os "{i}Yup. That’s where I am going to have sex with you. I can’t wait.{/i}"

    scene black
    with dissolve2

    s "Ugh. You’re lucky I’m such a good friend."
    os "{i}No, I’m lucky you’re such a perverted pushover. See you soon!{/i}"

    play sound "phonebeep.wav"

    "Osako hangs up the phone and I begin to make my way to the nearest subway station."

    scene osakowitch1
    with dissolve2

    "Then, after a brief ride along a line that was surprisingly busy for this time of night, I manage to catch up with her."

    s "Guess who’s ready to fuck a lesbian."
    os "Me. Pretty much all the time. "
    os "You’re gonna have to find another one, though. I changed my mind right after I hung up on you."
    s "Not even the girls who like girls can be trusted. Where am I supposed to find another lesbian at this time of night?"

    scene osakowitch2
    with dissolve

    os "Right over there. Where we’re going."
    s "Oh god. Are you taking me to a gay bar? Do you have any idea how torturous that will be for a chronic heterosexual like me?"
    os "Nope. Gayer."
    s "{i}Than a gay bar?{/i}"

    scene osakowitch3
    with dissolve

    os "I said what I said and I stand by it."
    s "Osako...what are we doing?"

    scene osakowitch4
    with dissolve

    os "So! Remember that time I talked to you about needing new hobbies? And then you dragged me to a porn shop to join the MILF of the Month Club?"
    s "I remember how much you loved it, yeah. Why continue the search when we’ve already found the perfect thing for you?"
    os "Because there are a bunch of {i}other{/i} things I want to try too! And it’s {i}my{/i} turn to subject {i}you{/i} to something you’re likely going to hate.  Which is why we’re taking a class on witchcraft tonight."
    s "We are not. I don’t do things like that."
    os "We sure are. And yes you do."
    s "I do not. "
    os "Yes you do."
    s "I...do...{i}not.{/i}"
    os "Sure you do! You love it."
    s "No means no and that is final."

    play sound "static.mp3"
    scene osakowitch5 with flash
    stop sound

    s "I fucking hate you, Osako."

    "{i}Somehow,{/i} Osako manages to drag me into a community college in the urban district that hosts a variety of silly and meaningless classes that I highly doubt anyone ever takes seriously."

    ins "Now, before we begin, I just want to remind everyone that witchcraft is {i}far{/i} more serious and powerful than you might initially believe. But {i}only{/i} in the hands {i}and minds{/i} of those who trust it."

    "I stand corrected and sad."

    ins "Today, we’ll be learning about different types of spells that crystals can be used for, how to properly place them on altars and grids, and then a little bit of dowsing and energy healing for fun at the end!"

    scene osakowitch6
    with dissolve

    s "Okay. So maybe I {i}was{/i} a little out of line with the MILF thing. But this is just {i}low.{/i}"
    os "Oh, come on! It’ll be fun. Especially near the end when we get to all the dowsing and energy healing."
    s "I don’t know what either of those two things mean, Osako."
    os "Me either! But that’s what makes it fun! Maybe."

    scene osakowitch7
    with dissolve

    ins "Excuse me! First and foremost, {i}love{/i} the top. But second, would you and your hubby mind quieting down a {i}teensy-weensy{/i} bit so I can proceed? Thankies!"
    os "Yes. This man is my husband. And I will now demonstrate the power of women by making him shut up."

    scene osakowitch8
    with dissolve

    s "Slay, queen."
    os "Never say that again. Do you understand?"
    s "I’m sorry."
    os "I need to hear that you understand. I will not risk hearing this a second time. Acknowledge these words, beard."
    s "I think your crystal is making you mean. It must be misaligning your chakras or something. That’s a thing, right?"
    os "Never say that again either. In fact, just stay quiet for the rest of class. {i}Thankies.{/i}"

    scene osakowitch9
    with dissolve

    s "Since when do you even like this stuff? Witchcraft seems like more of a Wakana thing, doesn’t it?"
    os "I don’t like this stuff. I know nothing about it. And while it definitely {i}is{/i} more of a Wakana thing, that doesn’t mean {i}I{/i} wouldn’t enjoy it."
    os "Besides, every lesbian needs to attempt witchcraft at least once or they revoke our license and we start liking men."

    scene osakowitch10
    with dissolve

    s "So you’ve forced me to attend the funeral for the only chance I’d ever have with you. Reiko Kobayakawa would {i}not{/i} be proud right now."
    os "Yeah. But on the bright side, look at all of these {i}other{/i} lesbians you can take home to not have sex with."
    s "Can we just skip to the dowsing part now? My pride is so lost at this point that I’m probably going to {i}need{/i} the assistance of magic to unearth it."

    play sound "slidedoor.mp3"

    os "Akira, there is no amount of dowsing that could help you recover what has never existed in the first place."
    s "That’s where the magic comes in."
    n "Woah! Sensei?"

    scene osakowitch11
    with fade

    s "Oh, Noriko and Kirin are here too."
    s "That makes sense."
    n "What are you doing here? And who’s your super hot friend?"
    s "Miss Watabe’s girlfriend. Sort of."

    scene osakowitch12
    with dissolve

    n "Wait, really?! I remember you looking kinda different! I suddenly don’t know who to be more jealous of between you and your partner."
    os "Uhh...thank you?"
    s "Are you actually into this stuff, Noriko?"

    scene osakowitch13
    with dissolve

    n "I’m not {i}not{/i} into it! I think this stuff can be kind of fun so long as you don’t buy too much into it. I’m just here because Kirin wanted to learn how to make a love potion and I wanted to be supportive."
    ki "I do not! I just thought it would be funny! That love potion thing wasn’t serious at all!"

    scene osakowitch14
    with dissolve

    n "Ooooooh. {i}Riiiiiiight.{/i} Gotcha."
    ki "Don’t make your dismissal so obviously fake either! Be a better friend and support me in my efforts to...steal your future husband or whatever!"
    n "I’m doing the best I can, Kirin. I-"

    ins "{i}Ahem!{/i} Hi, new girls! Welcome to the class! Buuuuut, if it’s not a problem, could you also keep it down a tad? I already warned your friends, but this is {i}not{/i} the kind of class you can just {i}talk{/i} through."

    scene osakowitch15
    with dissolve

    n "{i}Gotcha.{/i} We’ll be good. We both love crystals. And sage. And dowsing."
    ins "Ah! Well, you’re in luck then! First, though...are you sure you’re in the right place? Because this class is for adults only and-"
    n "Oh, I signed up beforehand. Stacy Fakename. Eighteen. And this is my cousin, Joanna."

    scene black
    with dissolve

    ins "Oh, great! I see both of you right here. Now, where were we?"
    ins "Ah, right! The identification of crystals is far more complex than merely memorizing their names and colors. Each one possesses certain qualities that-"

    play sound "static.mp3"
    scene osakowitch16 with flash
    stop sound

    n "Hey, you guys don’t mind if we join you, right? The last time Kirin and I came to one of these things, women kept trying to hit on us."
    s "You’ll have to ask Osako. This is her thing. I’m just being dragged along for the very painful ride."
    ki "Osako’s your name? Can I call you that? Or should I be more formal?"
    os "It’s only one letter off from my family name, so it doesn’t make much of a difference either way."

    scene osakowitch17
    with dissolve

    ki "Cool! Osako it is then. I just didn’t want to be rude."
    os "Well...thanks. Are you always this polite?"
    s "I think she just wants to fuck you."
    n "Yeah, I was thinking the same thing."

    scene osakowitch18
    with dissolve

    ki "Hahah! You guys are so funny!"
    os "She didn’t deny it."
    n "She rarely ever does. It’s cool that you’re into this stuff though, Osako! Maybe you can give Kirin and I some tips on potioncraft?"

    scene osakowitch19
    with dissolve

    os "Oh, no. I’m not {i}into it{/i} or anything. This is Witchcraft 101. I’m just...trying out a bunch of new hobbies and dragging who I can only assume is your teacher along with me to make him suffer."
    s "We’re good friends. It just doesn’t look like it."
    n "A little self-searching, then? Fun! Kirin’s doing the same thing right now."
    ki "Maybe the two of us can find new hobbies...{i}in each other.{/i}"

    scene osakowitch20
    with dissolve

    os "What does that even mean?"
    ki "What do you {i}want{/i} it to mean?"
    os "..."
    ki "..."
    s "So is that love potion for {i}me?{/i} Or-"

    scene osakowitch21
    with dissolve

    ki "There is no potion, damn it! It was a joke!"
    os "Another one for the harem, huh?"
    s "You’ll fall for me too once they revoke your lesbian license. Which they may very well do at this rate since none of us have been paying attention to the class at all."
    os "I think I’ve got a little while left until they come for me. They normally wait until you hit thirty to start knocking on your door."

    scene osakowitch22
    with dissolve

    n "I’m assuming you’re the same age as Wakana, then?"
    os "Uh...yeah. But...you call {i}her{/i} by her first name too? She hates when students do that."
    n "I’m an exception. Wakana and I are great friends. {i}She{/i} was actually my teacher before Akira-sensei was."
    os "And you call...{i}him{/i} by his first name?"
    n "Of course. He’s my Onii-chan."

    scene osakowitch23
    with dissolve

    os "You’re related?"
    n "Only when my clothes are on! Once they’re off, I’m whatever he {i}wants{/i} me to be! Which is totally fine since {i}I’m{/i} Stacy Fakename! Eighteen."

    scene osakowitch24
    with dissolve

    os "This harem thing really never ends, does it?"
    s "{i}Now{/i} do you see how hard my life is?"
    os "The education system has failed us in so many ways, hasn’t it?"
    n "You joke, but I imagine {i}you’d{/i} be pretty popular with the girls in our school too, Osako."

    scene osakowitch25
    with dissolve

    os "Me? No way. I don’t buy that at all."
    ki "I guess she does kind of have that same sort of...{i}Otoha{/i} thing going on for her, doesn’t she? Cool and princely aura, but still kind of feminine as a whole."
    os "Wakana, I’d understand. {i}She’s{/i} cool. And super hot. But {i}I’m{/i} just, like...Girl C."
    ki "Girl C?"
    os "Yeah. You know. Like...a background character. There’s nothing about me that really stands out."
    n "I mean...Wakana does have her own sort of...mini...harem...cult...thing. But I don’t think you’re “Girl C” at all, Osako."
    os "You have known me for ninety seconds."
    n "Yeah! Which was more than enough to make Kirin want to bang you."
    os "And I’ve only known {i}her{/i} for ninety seconds, but I feel like that isn’t saying much."

    scene osakowitch26
    with dissolve

    ki "I’m hormonal, okay?! I’d cum from a fucking {i}hug{/i} at this point in my life!"
    n "Isn’t she just the cutest?"
    s "Don’t compliment her too much or she might cum from {i}that{/i} too."

    scene osakowitch27
    with dissolve

    ki "Aaaah! Fuck you guys! I’m going to the bathroom!"
    n "Bye Kirin! Don’t cum!"
    os "So is just...{i}everyone{/i} in your school unhinged?"
    s "Pretty much everyone except that Otoha girl that you were compared to a second ago, yeah."

    scene osakowitch28
    with dissolve

    os "Great. So she’s Girl B and I’m Girl C. No harems here. Not like I’d know what to do with one anyway when I’ve only ever had eyes for one person."
    n "Really? I figured you’d have been really popular in school, Osako. Otoha definitely was at Kumon-mi Academy. It wasn’t until she was among all the misfits that she started fading into obscurity."

    scene osakowitch29
    with dissolve

    os "I mean, like...I had {i}friends.{/i} But I was active in sports clubs and stuff and...I don’t know. I wasn’t {i}that{/i} type of popular."
    os "Hell, I didn’t even really start {i}thinking{/i} about romance and stuff until college. Before that, {i}Girl C{/i} would have been a compliment."
    n "You’ve just gotta wait for a spinoff then!"

    scene osakowitch30
    with dissolve

    os "Hm?"
    n "It’s not unheard of for side characters to get spinoffs where {i}they{/i} get to be the star! And that’s what you’re trying to figure out now by taking classes you’re not totally interested in, right?"
    os "Uhh...I mean...I don’t know if I’d say I’m trying to become the {i}main{/i} character. But feeling a little more like...someone who doesn’t solely exist for someone else would be nice."
    n "Well, you’ve picked the right person to accompany you on your journey then."

    scene osakowitch31
    with dissolve

    os "{i}This guy?{/i} You’re kidding."
    s "Would the two of you think less of me if I mentioned how that kind of hurt?"
    os "See what I mean? You’re talking about Wakana, right? How {i}she’s{/i} along for the journey? Because I’ve been trying to keep her out of it. I’m-"
    n "No, I’m talking about Sensei."
    n "As weird as it is, he manages to bring out the best in people way more often than you’d think."
    s "No, I just think everyone else looks way better by comparison."
    os "What he said."
    n "Well, {i}both{/i} of you have self-esteem issues then."

    scene osakowitch32
    with dissolve

    s "Well, she’s got us there."
    os "..."
    s "..."
    os "Why are you holding my hand?"
    s "Because I’m in love with you."

    scene osakowitch33
    with dissolve

    os "What’s your name again? Stacy?"
    n "Or Noriko. Either one works."
    os "Strong name."
    n "I’m a strong girl."
    n "And the man behind you is the one who helped turn me into that."
    os "Something tells me you’d have turned out just fine with {i}or{/i} without him."
    n "Maybe. Maybe not. And maybe your whole self-discovery thing won’t really be influenced by him either."
    n "But I can tell from just these ninety...probably a hundred-twenty seconds now, that {i}both{/i} of you can help each other."

    scene osakowitch34
    with dissolve

    os "Well, I hope so. Because we both clearly need it."
    s "Misery is contagious. All we’re going to do is kill each other."

    scene osakowitch35
    with dissolve

    s "..."
    os "..."
    s "I changed my mind. I love you again."
    os "Learn how to love me without touching me."

    scene black
    with dissolve2

    n "Anyways! I’ll be right back. I’m gonna go make sure Kirin didn’t fall into the toilet and-"
    ins "Actually, don’t bother! Because all three of you are now being ejected from the class for disturbing everyone else and ruining meditation time!"
    os "Noooo, but we didn’t even get to the dowsing yet! That was supposed to be the fun part!"
    ins "Witchcraft isn’t about {i}fun!{/i} It’s about explaining and manipulating the unknown! Which is something you’d know if you paid attention for more than five seconds!"
    os "Yeah, well maybe it’s just really fucking boring! Come on, Akira. Let’s get drunk and have heterosexual sex with each other. Which is a thing we definitely do!"
    s "Are my dreams coming true or do we just need to keep deceiving them for reasons I don’t understand?"
    os "Confuse the lesbians! Scatter!"

    "Osako pulls me out of the classroom so quickly that I’m pretty sure she dislocates my shoulder."

    stop music fadeout 20.0
    $ renpy.end_replay()
    $ osakospring5 = True
    $ osako_love += 1

    jump osakospring6

label osakospring6:
    scene osakosarabar1
    with dissolve2

    "That’s okay, though. Because we decide to head over to Sara’s place so I can drink away the pain — a method I’m sure Sara herself would endorse if she weren’t too busy taking inventory at the moment."
    "It feels a little weird being alone here with Osako when I found out along the way that the rest of our normal group is hanging out at our normal bar tonight."
    "I guess it’s harder for her to try and be herself when there’s a magnet inside of her too though. She’d just drift back to Wakana if given the opportunity."
    "And I imagine Wakana knows this as well since she seems to support this little outing if what my new partner in witchcraft is saying is true."

    play music "calmbar.mp3"

    "But hey, it’s not like we {i}need{/i} to be with them in the first place. We can make our own decisions. And it’s way easier to {i}talk{/i} without Rika getting riled up about trivia or Imani trying to fuck me in the bathroom."
    "The only question is what {i}will{/i} we talk about now that our moment for exploration has come and gone?"
    "Do we sit here and pretend that it was a success? That she’s closer to comfortable with herself now?"
    "Or do we treat it like it is — one more failure in a list that I’m sure will be full of them before she can find what makes her happy."

    os "So, that was a total failure."

    "Okay. Good. At least she isn’t indecisive enough to not decide for me."

    s "For what it’s worth, you never struck me as a witchcraft person anyway. Just the type who fucks them."

    scene osakosarabar2
    with dissolve

    os "At least I know where to go girlfriend hunting if Wakana ever {i}does{/i} break up with me."
    s "She would have done that already if you two weren’t meant to be together."

    scene osakosarabar3
    with dissolve

    os "Oh, shut it. Nobody is {i}meant{/i} to be with anyone. The two of us can fail just as easy as anybody else. Probably {i}easier{/i} now that you and I are off on our own while they get drunk and talk about us."
    s "What do you think they’re saying?"
    os "I don’t know. Hasn’t really crossed my mind."
    s "You expect me to believe that a girl who is chronically worried about her place in this world just {i}hasn’t{/i} put any thought into what her significant other is saying about her behind her back?"

    scene osakosarabar4
    with dissolve

    os "Maybe I’ve just been having so much fun with {i}you{/i} that it’s distracting me from all the worrying?"
    s "You’re dying inside, aren’t you?"

    scene osakosarabar5
    with dissolve

    os "Hah! It probably seems that way if I’ve resorted to taking night classes, huh?"

    scene osakosarabar6
    with dissolve

    os "And, you know...maybe it’s true to a certain extent. I mean...it’s {i}obviously{/i} true to a certain extent."
    os "But for the first time in my life, it isn’t really about Wakana. Or love. Or...security or stability or any of that other stuff I’ve been getting buried by since college. It’s about {i}me.{/i} And that’s...great."
    os "I kind of like this feeling. Failure. Trying things out and then looking back on them and thinking it was funny I ever expected it to work in the first place. That’s not a thing I’ve ever felt before."

    scene osakosarabar7
    with fade

    os "It’s like what I was saying to your {i}little sister{/i} earlier. I had plenty of friends when I was younger. I did really well in all of my clubs."
    os "And, while my family is nowhere near as wealthy as Wakana’s, they’ve always been supportive of me. So if I ever {i}did{/i} fail at anything, which I can’t really remember, I’m sure they would have helped me through it."
    s "Sorry, are you just bragging now?"

    scene osakosarabar8
    with dissolve

    os "Maybe a little. Why? Does that strike a nerve as someone who fails at everything all the time?"
    s "..."

    scene osakosarabar9
    with dissolve

    os "You know I’m just kidding, right?"
    s "Yeah...I know. I just wish I was able to handle it as well as you do."
    s "Maybe once you get used to failing at everything, though, you’ll start feeling a little differently about it."
    os "Akira."
    os "You’re not a failure."
    s "..."
    os "You’re really not."
    s "Osako-"

    scene osakosarabar10
    with dissolve

    os "I talked to Imani the other day."
    s "Okay. But being good at sex isn’t enough to make me not a-"
    os "Not about that, idiot. Though, it definitely did come up and I definitely {i}do{/i} know way too much about your penis now."
    s "It was only a matter of time..."
    os "I’m talking about that thing {i}you two{/i} talked about."
    s "..."

    scene osakosarabar11
    with dissolve

    os "You do know that...walking away from something because it’s what’s best for {i}you{/i} doesn’t make you a failure, right?"
    s "It does when it’s your responsibility. You’d think the same thing about yourself if you had to leave the dojo."
    os "If I had to choose between my own personal happiness and the dojo, I’d choose myself every time. I’m not going to suffer just because it’s “the right thing to do.” And you shouldn’t either."
    s "I’m assuming Wakana doesn’t know yet?"
    os "What makes you think that?"
    s "The fact that she hasn’t come for my head."

    scene osakosarabar12
    with dissolve

    os "Pfft."
    os "Yeah, okay. Fair."

    scene osakosarabar13
    with dissolve

    os "Do you really think she’d get mad at you over something like that, though? If she {i}knew{/i} it was something you needed to do to feel human again?"
    s "The word “again” implies that I have ever felt human at all."
    os "Haven’t you?"
    s "..."
    os "Those practice fights with Ayane...those nights at the dive bar, kicking all of our asses at trivia with Rika..."

    scene osakosarabar14
    with dissolve

    os "That time we went down on our partners together?! Surely you must have felt human in {i}those{/i} moments, right?"

    scene osakosarabar15
    with fade

    s "..."
    os "Do you need another drink? I’ll buy the next one."
    s "No, I..."
    s "..."
    s "This is kind of hard for me."
    os "Akira, I know you're attracted to me. But it just {i}isn’t{/i} going to happen."
    s "Not that. This...bonding thing. Having to open up to someone without envisioning what choices and words will lead to sex the quickest."
    os "You don’t {i}have{/i} to open up. We can just drink."
    s "I kind of {i}want{/i} to, though. I just don’t know how."
    os "Then...is that really how you look at everyone? Is {i}every{/i} conversation just a means of getting a girl’s pants off?"
    s "Maybe not all of them...but enough for it to be unhealthy."
    s "Especially when you remember who I’m talking {i}to.{/i}"
    os "..."
    s "{i}Any{/i} amount is unhealthy when you take that into consideration. So walking away from school wouldn’t just be what’s best for me, it’d be what’s best for {i}everyone.{/i}"
    s "Despite all that, though...I still can’t bring myself to do it."
    s "Why?"
    os "Akira..."

    scene osakosarabar16
    with fade

    os "Are you {i}sure{/i} you want to admit this to me? Because I’m not {i}saying{/i} you’re about to admit anything...but I do know what you’re implying. And I want to stop you before you say something you’ll regret."
    s "I don’t know, Osako."
    s "I have no idea."

    scene osakosarabar17
    with dissolve

    os "{i}Hah...{/i}"
    os "I can’t even pretend to understand what you’re going through right now. And that sucks. It really does."
    os "Like...I want to help, but...what can someone even {i}do{/i} to help with a problem like that?"
    s "At least you see it as a problem. That’s more than most are able to offer up."
    os "Sure. But, like you said a second ago, {i}most{/i} of the people you’re dealing with aren’t...{i}smart{/i} enough yet to make their own decisions."
    os "No one our age knows. Wakana doesn’t know. Imani doesn’t know. Rika doesn’t know. So now {i}I{/i} have to be the one who knows. And {i}I{/i} don’t know what to do about it."
    s "I’m sorry I’ve burdened you with the knowledge of who I really am, Osako."
    os "You should be..."

    scene osakosarabar18
    with dissolve

    os "Why’d you have to go and make me care about you?..."
    os "Life was so much easier when you were just some asshole-ish creepy guy flirting with the rich girl at my karate class. I wasn’t ever supposed to {i}care.{/i}"
    s "So why do you?..."
    s "What was it about the way I act...how I constantly annoy you and flirt with you despite you hating it and...how I unintentionally make your girlfriend ignore you for {i}my{/i} sake that made you {i}like{/i} me? I don’t get it."
    os "And you think I do?"
    os "Until recently, I was fine with you just being a step or two above an acquaintance. But..."
    os "You seem different when it’s just {i}us.{/i} Better. Real."

    scene osakosarabar19
    with dissolve

    os "The flirting and shit doesn’t bother me. I fuck with you too. It’s just...frustrating doing all this stuff to try and “find myself” beside someone who’s decided it’s okay to just stay lost."
    os "It makes me feel like you’re only helping at all because it gives you one more excuse to not do the same yourself. And that pisses me off..."
    os "I pity you, Akira. I pity the type of mind that can see what needs to be done to enact the changes you need and just...not even make an attempt to do the same."
    s "Getting a new hobby won’t stop me from preying on teenagers, Osako."

    scene osakosarabar20
    with dissolve

    os "And there it is..."
    os "I’m both proud of you and hate you for admitting that at the same time."
    s "Because {i}you{/i} have to deal with it now too?"
    os "Yeah."
    os "Do I side with my morals and do what’s right? Do I ruin a friend’s life and, by extension, ruin a bunch of other lives in the process? It’s not exactly an easy choice."
    s "You wouldn’t be ruining anything — just making a handful of people very upset for a sizable amount of time."

    scene osakosarabar21
    with dissolve

    os "But then a girl would lose her father a {i}second{/i} time. My partner would lose her best friend. My {i}other{/i} friend would lose the man she’s rapidly falling for."

    scene osakosarabar22
    with dissolve

    os "But, worst of all, {i}I’d{/i} lose my witchcraft buddy!"

    scene osakosarabar23
    with fade

    s "I’m surprised you can still make jokes after hearing what I just confessed to."
    os "I had a thousand red flags to soften the blow. I’d just hoped it would never be something that became so {i}real.{/i}"
    s "But if {i}you{/i} figured it out so easily, what’s stopping Wakana and Imani from doing the same?"
    os "Easy. They like you more, so they’re giving you every benefit of every doubt that has ever existed."
    s "And how do you think they’d feel if they found out?"
    os "Crushed. Both of them. Then {i}they’d{/i} probably feel like failures too for looking straight past all of the signs you posted around them pointing directly {i}to{/i} this."
    s "I really am just fucking up {i}everything{/i} then, huh?"
    os "You sure are. Way to ruin the night, asshole."
    s "I bet you feel better about yourself now though, right?"

    scene osakosarabar24
    with fade

    os "Yeah. I feel {i}really{/i} great buying drinks for a predator. You got me there."
    s "Anyway...I think I {i}am{/i} going to quit."

    scene osakosarabar25
    with dissolve

    os "..."
    s "Everything just...makes more sense that way. And yeah, it’d make {i}more{/i} sense if I stopped seeking the girls out entirely, but..."
    os "They’re important to you...and that’s okay. It’s everything else you’re doing that’s not."
    s "Yeah..."
    s "Thank you for not using your karate to chop me in half."

    scene osakosarabar26
    with dissolve

    os "Don’t mention it. Feel any better after getting that off your chest? Do {i}you{/i} want to choose the next night class?"
    s "No. I just want to not hate myself for a minute. That would be enough."
    os "Guess we’ll just have to keep looking then. Maybe we’ll find something we can {i}both{/i} enjoy?"
    s "Well, I’ve always wanted to try banging Wakana-"
    os "Actually, maybe I {i}will{/i} chop you in half? It’ll cut down some of the calories I gained from drinking tonight {i}and{/i} the world will be a safer place. The pros really do outweigh the cons here."
    s "I have never agreed with anyone so much."
    sa "Um...uh...Sensei?..."

    scene osakosarabar27
    with fade

    s "Oh. Hey, Sana. I didn’t realize you were working tonight."
    sa "Yuki is...not here again and...actually, that doesn’t matter right now..."
    sa "Can we talk?..."
    s "About what?"
    sa "Just...something you said the other day..."
    sa "I...I realize I..."

    scene osakosarabar28
    with dissolve

    sa "Uhh...I realized my...reaction...wasn’t really...uhh..."
    s "Don’t worry about it. I was just being dumb."

    scene osakosarabar29
    with dissolve

    sa "Just...being...dumb?..."
    s "Yeah. It’s nothing you need to be worried about."
    s "Can you grab us two more beers, though? I’m going to need them."
    sa "Why?"

    scene osakosarabar30
    with dissolve

    s "To...drink?"
    sa "..."
    s "...Sana?"

    scene osakosarabar31
    with dissolve

    sa "It’s nothing."

    scene black
    with dissolve2

    sa "I’ll be right back with your order..."

    "........."
    "......"
    "..."

    scene nightsky
    with dissolve2

    "Osako and I talk for another hour or so before we decide to head out."
    "Things get less serious, thankfully. Though, I probably shouldn’t be {i}too{/i} thankful when it was me who made things serious in the first place."
    "Am I glad that I essentially admitted to her what I’ve been doing? Nope. In fact, I feel ten times worse."
    "But..."
    "I think I get what she was saying about failure feeling good now, though."
    "And I think the fact that I feel this shameful at all is indicative of something bigger."
    "..."
    "I really like being with her."

    play sound "static.mp3"
    scene osakosarabar32 with flash
    stop sound

    "But all good things must come to an end. And for tomorrow to ever begin, we must first bid farewell to today."
    "Perhaps what comes when the sun shines again won’t make me feel like I’ve lived in the dark all these years."
    "I just know that, whatever happens next, I must feel like a failure to ever know what it means to succeed."
    "I hope she finds her happiness first — for she is far more deserving than a cretin like me."

    os "Are you gonna be okay?"
    s "Yeah...I just need to get my head straight."
    os "No. I mean are you going to be okay walking home? You don’t need me to be your bodyguard?"
    s "Oh. Come to think of it, I {i}would{/i} feel a little more comfortable if you were to just stay in my room with me tonight. Fight off any demons that come to claim me. You might have to sign an NDA, though."
    os "Meh. I think I’ll just let you be claimed by the demons. It was nice knowing you, though."
    s "Yeah. Nice knowing you too, Osako."
    s "Guess I’ll just...see you when I see you then."
    os "I’ll send you the class list. I’m serious about letting you choose the next one."
    s "Osako-"
    os "This doesn’t have to just be for me anymore. We can figure shit out together."
    os "And if you ever need to talk, you know where I live."
    s "Wakana is going to be so jealous of how close we’re getting."

    scene osakosarabar33
    with dissolve

    os "Maybe she’ll finally know how I felt then!"
    s "What?"

    scene black
    with dissolve2

    os "Night, Akira! Don’t do anything stupid! Like...seriously! You do some really stupid shit!"
    s "Goodnight, Osako. Have fun banging my future girlfriend."

    "I don’t get a snarky response this time."

    stop music
    play sound "static.mp3"
    scene osakosarabar34 with flash
    stop sound

    "Just more indecision and the unwelcome recollection of {i}another{/i} strange night when I turn around to head home."

    k "{i}Nao-chan! Grabbing more than three wiggleworms at once will confuse the Frog Boy! You must move slowly! Only one at a time!{/i}"
    na "{i}!!!!!!!!!!!{/i}"

    "I took her first time and have barely looked at her since."
    "But was it really {i}her{/i} at all?"

    k "{i}Ah! The hot bean water! I forgot to empty its mesh-bed! Wait right there, Nao-chan! I will return in seventeen seconds!{/i}"

    "Why hasn’t she come to see me?"
    "Is she scared?"
    "She doesn’t sound scared."
    "She doesn’t sound any different at all."

    scene black
    with dissolve2
    play sound "footsteps.mp3"

    "She probably doesn’t even realize what happened."

    k "{i}Nao-chan, is something not right? What has drawn your attention so late in the night?{/i}"
    na "{i}...{/i}"
    s "..."

    "I’m gone before I hear Kaori say anything else."
    "One more word and I would have kicked down the door."

    $ renpy.end_replay()
    $ osakospring6 = True
    $ osako_love += 1

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
