label callkarinmorning:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callmorning
    if chap4active == True and karinbetter == False:
        "I don't want to call her right now..."
        jump callmorning
    if chap4active == True:
        jump karinspringmorninggen
    if chapthreeactive == True:
        jump karinsummer2morninggen
    else:
        "Karin should be at the soccer field right now. I can probably go there if I want to see her."
        jump callmorning

label karinpool:
    if chap4active == True:
        jump karinspringpoolgen

label callkarinafternoon:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callafternoon
    if chap4active == True and karinbetter == False:
        "I don't want to call her right now..."
        jump callafternoon
    if karin_love >= 0 and karindate1 == False:
        jump karindate1
    if karin_love >= 5 and day103 == True and karindate5 == False:
        jump karindate5
    if karin_love >= 10 and mollycafe1 == True and karindate10 == False:
        jump karindate10
    if karin_love >= 15 and day264 == True and karinlied == True and karindate15 == False:
        jump karindate15
    if karin_love >= 20 and day355 == True and karinsoccer20 == True and karindate20 == False:
        jump karindate20
    if karin_love >= 25 and makiinv3 == True and karindate25 == False:
        jump karindate25
    if karin_love >= 30 and karindate25 == True and karindate30 == False:
        jump karindate30
    if chapthreeactive == True:
        jump karinsummer2poolgen
    if christmas7 == True:
        jump karinnoongen2
    else:
        jump karingenafternoon

label callkarinnight:
    if senseisad == True:
        "I don't want to call her right now..."
        jump callnight
    if chap4active == True and karinbetter == False:
        "I don't want to call her right now..."
        jump callnight
    if karindate1 == False:
        play sound "phonebeep.wav"

        "I tap on Karin's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        ka "H-Hello?"
        s "Hey, Karin. What are you up to?"
        ka "..."
        ka "Sensei? Wh-Why are you calling me so late?"
        s "I was just wondering if you wanted to meet up?"
        ka "At night?..."
        ka "But...but why?"
        ka "You aren't like...you know..."

        "Now that I think about it, calling Karin at night probably isn't the best idea at this stage in our relationship."
        "I should call her earlier if I'm going to get to know her."

        s "Actually, don't worry about it. I didn't realize how late it was."
        s "I'll just see you some other time."
        ka "Oh...Umm, okay. I'm sorry, it just still feels kind of...weird to me."
        s "Don't worry about it. We'll talk soon."
        ka "Okay...Talk to you soon."

        play sound "phonebeep.wav"

        "I hang up the phone and decide to call someone else."
        jump callnight
    else:
        jump karingennight

label soccerfieldkarin:
    if karin_love >= 15 and day271 == True and karinsoccer15 == False:
        jump karinsoccer15
    if karin_love >= 20 and day351 == True and karinsoccer20 == False:
        jump karinsoccer20
    if christmas7 == True:
        jump karinsoccergen2
    else:
        jump karinsoccergen

label karinsoccergen2:
    scene karinsoccergen2
    with dissolve
    play music "highspeedprinter.mp3"

    "I show up at the gym for morning soccer practice to find Karin setting up some traffic cones to help the girls run drills."
    "Seeing as I'm here a bit earlier than normal and Karin has practically finished what she was doing already, the two of us get to talking for a little while."
    "Well, trying to talk at least."
    "It's mostly just me saying things to her and her awkwardly fumbling to find responses that won't make her sound like she's terrified of males."
    "Of course, this doesn't work and within a matter of seconds, she is blushing furiously and struggling to even speak coherent words."
    "But, since I am so thoughtful and considerate, I do not point out her mistakes."
    "Instead, I just laugh silently to myself and think about how cute she is."
    "And how excited I am to ultimately force her out of that shell of hers."

    scene black
    with dissolve

    if bonus == True:
        "I decide to get a move on once practice starts because I am a horrible excuse for a coach and an even worse excuse for a human."
        "But I got to talk to a beautiful girl with amazing thighs, so it was all worth it at the end of the day."

    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin's affection has increased to [karin_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label karinnoongen2:
    scene karinnoongen2
    with dissolve
    play music "retrospect.mp3"

    "Karin and I meet up at our usual park but she decides against running today due to all of the ice on the ground."
    "She talks about how she normally signs up for a gym membership in the winter for this exact reason, but then begins to panic once I ask what gym she goes to."
    "I guess she's embarrassed about being seen there, but she exercises in front of me all the time so I'm not really sure what her deal is."
    "Regardless, we spend the afternoon under a gazebo- hiding behind its pillars each time the wind blows."
    "She does this thing where she holds on to her ponytail every time a large gust comes around and, despite it being a little pointless in my view, it's definitely cute."
    "But she's become sort of synonymous with cute behavior at this point, so that shouldn't really come as any surprise."

    scene black
    with dissolve

    "Slowly but surely, I can feel Karin becoming a little more comfortable with me."
    "Don't get me wrong, she's still nowhere near the level of going out on dates or anything like that, but-"
    "Well, let's just say that it's very easy to tell she likes being around me."
    "Why she likes that, I have no idea. But it doesn't change the fact that she does."
    "So I will continue being the horrible cynic I am as it has yet to negatively impact the growing bond between the two of us."

    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin's affection has increased to [karin_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label karinsoccergen:
    scene karinmorninggen
    with dissolve
    play music "highspeedprinter.mp3"

    "I head to the soccer field first thing in the morning and immediately make my way over to Karin."
    "She questions why I'm spending my time with {i}her{/i} rather than Miku, so I make up some excuse about how important co-captains are."
    "I'm not sure how true that statement is, but she seems really happy to hear it and her face lights up in response."
    "It's irresistibly cute seeing someone who appears to be so tomboyish acting so...girly whenever something makes her happy."
    "And even though the two of us aren't as close as can be yet, I'm still glad to be able to see that side of her..."

    scene black
    with dissolve

    "I hang around for a few hours and watch the girls play a practice game or two."
    "Karin and Miku are the clear standouts among everyone, and it comes as no surprise knowing that they're the ones basically running things."
    "Eventually, practice comes to an end and I have to gather my things and leave while the girls head back inside the[school] get changed..."

    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin's affection has increased to [karin_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label karingenafternoon:
    scene karingenafternoon
    with dissolve
    play music "retrospect.mp3"

    "I head to the park to hang out with Karin for a bit."
    "She spends the first half hour running laps but eventually decides to take a break and talk to me instead."
    "The two of us discuss simple things like her favorite activities and what she wants to do when she's out of [high_school]."
    "I'm not surprised to hear that she's basically got everything planned out already."
    "Unlike her sister, Karin has a clear direction of where she wants to go in life. And I'm glad she's willing to share some of that with me."

    scene black
    with dissolve

    "Karin hesitantly tells me that she needs to go as soon as the sun starts to set."
    "I feel slightly bad about taking up so much of her time, so I obviously tell her to go do whatever it is she needs to do and not let me stop her."
    "She smiles as she leaves and nervously waves goodbye as she jogs off in the direction of her house."
    "..."
    "I might be a little quick in saying this, but I think she's already starting to get a little more comfortable around me..."

    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin's affection has increased to [karin_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label karingennight:
        play sound "phonebeep.wav"

        "I tap on Karin's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        ka "H-Hello?"
        s "Hey, Karin. What are you up to?"
        ka "Sensei? I'm about to go out with some friends...Did you need something?"

        "Damn. Looks like Karin already has plans for tonight."
        "I'll just have to call her earlier next time."

        s "It's nothing serious. It can just wait until next time I see you."
        ka "Oh...Well, um...Okay."
        ka "I guess I'll talk to you later then?"
        s "Yup. Talk to you later."

        play sound "phonebeep.wav"

        "I hang up the phone and decide to call someone else."

        jump callnight

label karindate1:
    "Maybe I’ll see what Karin is up to?"
    "I know that she spends virtually all of her time doing stuff for her
    different teams or clubs or whatever, but now that I’m her “coach,” maybe I can find my way in?"

    if bonus == True:
        "To her life, I mean. Not her."
        "Well, yes her. But not right now."
        "Unless she wants it."
        "Whatever. You know what I mean. "

    play sound "phonebeep.wav"

    "I select Karin’s name in my phone and wait for her to pick up."
    "Given how embarrassed she was to even give me her number, I imagine she’ll let it ring a few times before-"

    play sound "phonebeep.wav"

    ka "Hello?"
    s "Oh, hey."
    s "I wasn’t expecting you to pick up right away."
    ka "Oh! Uhh...hahah, yeah. I just kind of had my phone out and, you know...answered it. Yeah."
    s "...Right."
    s "Well, anyway, what are you up to right now?"
    ka "Me? I was about to go to the park. Why?"

    "Knowing that Karin would probably drop her phone if I asked her to “hang out” right now, I
    decide to get creative and start making use of my newly appointed position."

    s "Do you mind if I tag along?"
    ka "Huh? Why?"
    s "You’re going there to jog or run or something like that, right? That sounds like a thing you would do."
    ka "Uh-huh..."
    s "Well, I’d like to sort of see you in action if I’m going to be in charge of you from now on."
    ka "In action?! Like, alone?? Can’t you just come watch us play at the field or-"
    s "One on one sessions are good for establishing relationships with your team. "
    s "And seeing as I already know Miku pretty well, you’re second in line."

    if kirindate1 == True:
        ka "Second? But, didn’t you and Kirin hang out the other day?"

        "...Did Kirin really tell her about that?"
        "Why?"

        s "We did. But that wasn’t related to the team. This is."
        ka "Well...um...it does feel a little weird...but I guess I can see where you’re coming from."
        ka "Do you want to just meet me there? Do you need me to bring anything for you? Water, maybe?"
        s "I’ll be fine. Are you going to the park near the[school] or a different one?"
        ka "The[school] one. I’ll leave now if you’re going to head over there."
        s "Sounds good. I’ll see you soon."
        ka "Uh-huh! See you soon!"

        play sound "phonebeep.wav"

    else:
        ka "Really? I mean, I guess that’s reasonable since I’m co-captain but..."
        ka "I don’t know. Is it weird if I’m kind of...maybe a little happy to hear that? Hahaha..."
        s "It’s not weird at all. I’m excited to get to learn more about you."
        ka "Ah-! Yeah! I’m excited to learn more about me too! Ah, wait! I meant you! I already, um, know about...me...And-"
        ka "Actually, is it okay if I just hang up now and meet you at the park?"
        ka "I’m going to the one by the[school] and I’ll start heading over now if you’re ready."
        s "Sure thing. I’ll see you soon, then."
        ka "Uh-huh! See you soon!"

        play sound "phonebeep.wav"

    "I hang up the phone and slide it back into my pocket, wondering if Karin is
    going to make {i}me{/i} jog as well today."
    "..."
    "I really hope not."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene karinjogs1
    with dissolve2
    play music "retrospect.mp3" fadein 10.0

    "I arrive at the park near[school] and find Karin standing near the fountain waiting for me."
    "The sun peers through the trees as it begins to set and finds its way onto her well-toned, yet still
    seemingly delicate body."

    ka "G-Good evening! "
    ka "Thanks for coming out to watch over me today..."

    scene karinjogs2
    with dissolve

    ka "Oh, wait! I meant watch me! Not watch over me! I can take care of myself!"
    s "I know what you meant, don’t worry."
    s "In a sense, I might even need you to watch over me today."

    scene karinjogs3
    with dissolve

    ka "Huh? What do you mean by that?"
    s "I’m not sure what Miku told you about me, but I don’t know much about sports."
    s "I actually think it’s a little strange that she wanted someone like me to be your coach despite that."
    s "It seems like the two of you take this pretty seriously, so I’ll try not to get in the way too much."

    scene karinjogs4
    with dissolve

    ka "You don’t have to worry about that...Miku and I are already grateful
    that you’re going out of your way for us."

    "Well, it’s not like I {i}chose{/i} to go out of my way. I was dragged into this by force."

    ka "It’s okay if you don’t know much about sports. I...wouldn’t really mind teaching you."

    scene karinjogs5
    with dissolve

    ka "We just...kind of need a teacher to be present in order to keep playing."
    ka "That’s...one of the several reasons I was surprised to hear you actually trying to get involved today..."
    s "Speaking of involvement, would you mind telling me a little about what you do here?"

    scene karinjogs3
    with dissolve

    ka "Nothing special, really. I just come here a couple times a week to run laps around the park. "
    ka "It’s normally pretty quiet here on weekends since no one stops by on the way home from[school]."

    scene karinjogs5
    with dissolve

    ka "On weekdays, though, I normally just wind up training with Miku or some of the
    other girls. It’s not often that I’m alone. So this is a little weird for me."
    s "Well you’re already doing better than you normally do, so I’m proud of you."

    scene karinjogs6
    with dissolve

    ka "Well, it’s not like I have a choice anymore, is it? You’re my coach."
    ka "If I can’t get over a hurdle as small as just looking you in the eyes, there’s no way I’ll be able to climb over anything else."
    ka "Just...try not to come too close too quickly or something because I probably won’t be able to prevent myself from having some weird reaction."
    s "Noted. We should be practicing social distancing anyway in case some weird disease ever starts going around."

    scene karinjogs7
    with dissolve

    ka "Hahah...Yeah, I guess we probably should..."

    "Karin’s smile somehow manages to light up the world even in the midst of the sunset."
    "She’s a mix of a lot of different great qualities, so I’m glad to see that she’s not
    as...inherently weird as a lot of the other girls I’ve been dealing with lately."

    s "So...are you ready to start?"

    scene karinjogs8
    with dissolve

    ka "Yeah. I just need to run, right? Are you going to run with me?"
    ka "You’re not really dressed for the task, so maybe you can just keep times for me instead?"
    ka "I can’t imagine it’ll be very fun, but at least you won’t have to get all sweaty that way."
    s "That sounds good to me."

    "I pull my phone out of my pocket and open up the stopwatch app."

    ka "Just hit the “lap” button every time I pass you, okay? That’s how I normally time myself. Just...with a tree instead of a teacher."
    ka "You don’t need to tell me my individual times. Just let me know how much faster or slower I am on each pass."
    ka "Endurance is important, so I need to make sure I’m able to keep up with myself more than anyone else."
    s "Roger that. Official coach duties commencing now."

    "I hit the start button on the stopwatch and immediately send Karin spiraling into panic."

    scene karinjogs9
    with dissolve

    ka "Ah- Sensei, wait! You didn’t even count me down! Start over!"
    s "No can do. Clock is already running. Go, Karin, go!"

    scene karinjogs10
    with dissolve

    ka "Ahh! Okay! I’m going!"

    scene karinjogs11
    with dissolve

    "Karin quickly takes off into a sprint to make up for a few seconds worth of lost time."

    scene black
    with dissolve

    "I follow behind her until the two of us are safely out of the center of the park, watching
    as she gradually moves further and further away."
    "The way she runs is a lot different than Miku."
    "Every step that Karin takes seems carefully calculated, whereas Miku seems
    more like a girl who just had one too many energy drinks and was told to run as fast as she can."
    "........."
    "......"
    "..."

    scene karinjogs12
    with dissolve

    ka "How was...that one?"
    s "Thirty seconds under your last. You’re not starting to lose steam, are you?"

    scene karinjogs13
    with dissolve

    ka "Of...course not! Watch me...closely this time!"

    scene karinjogs14
    with dissolve

    "Karin leaves me in the dust once again with a look of determination that could
    rival some of the fiercest athletes."
    "She's really fast despite her size. She’d probably even be able to
    beat Miku if she were several inches shorter and a lot less...busty."
    "........."
    "......"
    "..."

    scene karinjogs15
    with dissolve

    ka "And...that one?"

    "I look down at my phone again to realize that Karin has actually beaten the time of her first lap."
    "I was so caught up in admiration that I didn’t even realize she was giving it her all that time."

    s "Fifteen seconds up."
    ka "From the last one or from the best one?"
    s "The best one. Did you want to call it now? Or do you have a few more in you?"

    scene karinjogs16
    with dissolve

    ka "Heh...I could do this all day..."

    scene karinjogs14
    with dissolve

    "Once again, Karin takes off down the path, looking no slower than she did when she
    started almost twenty minutes ago."
    "How the hell is she able to keep up that pace for so long without even looking phased?"
    "If I were in her shoes, I’d be basically crawling right now."
    "........."
    "......"
    "..."

    scene karinjogs17
    with dissolve

    ka "Hah..."

    "Karin comes to a stop several feet away from me after what I imagine is her last lap."

    ka "Okay...Now I’m done."
    s "I thought you were planning on going all day?"
    ka "Nah...I was...starting to feel bad for you. "
    ka "You looked bored."
    s "I wasn’t bored at all. If anything, I was actually having a good time watching you."
    s "You’re really impressive, Karin. I think I get why you’re so involved with athletics now."

    scene karinjogs18
    with dissolve

    ka "What?! No no no! I’m not that impressive. I just practice a lot."
    s "Isn’t that the same thing? Most people don’t become great at anything without practicing."
    ka "Well, yeah, but like...I don’t know. Getting compliments from you feels weird. Hahaha..."
    s "Well you better get used to it, because I’m pretty sure this is going to be a regular occurrence from now on."

    scene karinjogs19
    with dissolve

    ka "You...want to do this again?"
    ka "I thought you were just trying to get acquainted with everyone on the team?"
    ka "Isn’t it unfair to spend more time with me when there are other girls who need more help?"

    "Karin makes a good point. But something she doesn’t yet understand is that I’m not just doing this because I’m trying to be a good coach."
    "I want to get closer to {i}her{/i} specifically. If I didn’t, I wouldn’t have called her out here today."
    "But that’s not something she needs to know yet."
    "Who even knows how someone as inexperienced and nervous around men would handle it if she were to hear something like that?"

    s "I definitely want to do this again."
    s "Unless...you didn’t have fun hanging around me today?"

    scene karinjogs20
    with dissolve

    ka "What?! O-Of course I had fun! I had a lot of fun! So much fun! It was
    great! It was awesome! It was...It was-"

    scene karinjogs21
    with dissolve

    ka "Oh God! I’m forgetting how words work!"
    s "Well, believe it or not, I had fun too. And I’m really looking forward to doing this again."
    ka "Fun?! You had...but you...the stopwatch...ahhh!"

    "Translation (Projected): Did you really have fun today, Sensei? All you did was stand around with a stopwatch..."

    s "Okay, okay. Calm down. Catch your breath."
    s "Need me to rub your shoulders?"
    ka "Shoulders?!"
    s "They’re the things your neck and your arms are connected to."

    scene karinjogs22
    with dissolve

    ka "I know what they are! I’m just suddenly nervous again for some reason!"

    scene black
    with dissolve2

    "Karin takes another several minutes to calm herself down and get her eyes to go back to normal."
    "I offer to walk her home (With only the purest of intentions) but she respectfully declines since a
    few of her friends are already waiting for her at her family’s apartment."
    "It’s strange."
    "Even though all I did was manage a stopwatch this afternoon, I feel suspiciously content."
    "Maybe I just really like when girls get nervous around me? "
    "The confidence boost is definitely nice, but-"
    "I don’t know."
    "What am I even saying?"
    "I should just get on with my day..."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karindate1 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label karindate5:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene karinseconddate1
    with dissolve
    play music "retrospect.mp3" fadein 5.0

    "Karin and I decide to meet up at the same park as always."
    "She spends the first part of the meeting awkwardly running laps around the track and feeling increasingly worse about how I’m doing literally nothing each time she passes by."
    "Is it a little strange that our meetings are 95%% me supervising her exercise routine? Absolutely."

    if bonus == True:
        "But I’m not going to complain about something as trivial as that when I’m blessed enough to ogle at her body without worry of any sort of consequence."
    else:
        "But I am only here to make sure that she becomes a better athlete, so everything is okay."

    ka "Okay...no more running. I’m good for today. "
    s "Tired?"
    ka "Not at all. Just...I don’t know."
    ka "Maybe a little...embarrassed? Is that weird to say?"
    s "What’s there to be embarrassed about? You’re doing great."
    s "Your times have been improving as well. I have no idea how you have this much stamina."

    scene karinseconddate2
    with dissolve

    ka "Practice...I’ve been doing this almost every day since...well, forever. So it kind of just...developed, I guess."
    s "Good for you. Establishing positive routines is impressive."
    s "Personally, I find it hard even coming to[school] every day."

    scene karinseconddate1
    with dissolve

    ka "That’s...not good, you know? You’re a teacher."
    s "Barely."
    ka "No no no, don’t say that. I’m sure you’re great. Miku talks about you all the time."
    ka "Wasn’t she failing like, every subject before you started helping her out?"

    "I think that’s more due to the fact that I’ve stopped giving anyone grades below an A but hey, if Karin wants to think it’s due to me being a good teacher, so be it."

    s "Yeah. I guess I am pretty impressive when you put it that way."

    scene karinseconddate3
    with dissolve

    ka "Totally! It kind of makes me wish I was a year younger so I could be in class with you guys."

    scene karinseconddate4
    with dissolve

    ka "W-Wait! No! That probably made it sound like I want to spend more time with you, didn’t it?!"
    s "...Not really?"
    ka "I swear that's not what I meant!"
    ka "I was just trying to say that it would be cool to hang out with Kirin and Miku in class and stuff!"
    ka "It totally doesn’t have anything to do with you! Nothing at all!"
    s "I never said it did?..."

    scene karinseconddate5
    with dissolve

    ka "W-Wait! No! That was bad too! Now it sounds like I never want to see you! That isn’t true either!"

    scene karinseconddate6
    with dissolve

    ka "I like you!"
    ka "Like, teacher-like! Not boy-like! Boy bad! Teacher good!"
    s "Okay Karin, it’s time to calm down."

    scene karinseconddate7
    with dissolve

    ka "Ugh...I’m literally the worst."
    ka "I’m never going to get used to this, am I?"
    s "Sure you will. There’s no way you can stay this uncomfortable around me forever, is there?"

    scene karinseconddate8
    with dissolve

    ka "Th-That’s not it at all!"
    ka "I’m really comfortable! I am! "
    ka "Super comfortable! But also not!"

    scene karinseconddate9
    with dissolve

    ka "It’s just...being out here alone with you makes it feel like a...d-d-d-d-date and stuff..."
    ka "And umm...yeah, that probably sounded weird too. I mean obviously it’s not a...date thingy. You’re just doing your job and..."

    scene karinseconddate6
    with dissolve

    ka "Uhh...what were we talking about again?"
    s "I think it was about how you’re a year older than the other girls."

    scene karinseconddate1
    with dissolve

    ka "Oh...umm...yeah. That’s what I was talking about. Right."
    ka "Whoops..."

    "This girl really {i}does{/i} have a hard time talking to men. "
    "Or at least me."
    "Miku has said in the past that Karin gets like this around every boy, but I have a creeping suspicion that miss co-captain here might actually be warming up to me quicker than anticipated."

    s "So you’re a second-year then, right?"
    ka "Right! One year to go. Kind of nerve-wracking to be honest. I’m not really sure what I even want to do with my life yet."
    s "Well you have roughly a year and a half to think about it."

    "I lie."
    "Karin has all of the time in the world to think about it."
    "Everything is going to just reset before she makes a decision anyway."
    "But it’s my duty in times like this to instill false words of encouragement."
    "I really am a great teacher."

    ka "Yeah...that’s what my parents keep telling me as well. "
    ka "They’re great parents, really...but I wish they’d be a little more assertive at times."
    ka "It’s great that they’re so patient with me but like...maybe I need to be pushed in the right direction or something?"
    s "Why not just become a housewife or something like that? That sounds easy enough."

    scene karinseconddate10
    with dissolve

    ka "W-Wife?..."
    ka "Y...Y-Y-Y-Y-Y-You..."
    ka "Are you-"
    s "No Karin, I’m not proposing to you."

    scene karinseconddate11
    with dissolve

    ka "THAT’S NOT WHAT I WAS ASKING!"

    scene karinseconddate12
    with dissolve

    ka "Do...you really think I’m...housewife material?"

    if bonus == True:
        ka "I’m obviously a lot more...{i}developed{/i} and athletic than other girls my age, so everyone just normally suggests that I pursue sports."
    else:
        s "I think you will make someone pretty decently happy one day."

    ka "It’s kind of weird hearing such a...ridiculous suggestion from my coach, who I imagined would be pushing me into that field more than anyone."
    s "You really look at me as your coach? All I've done so far is use the stopwatch app."
    ka "Mhm..."
    s "Fact is, I just think you should do what makes you happy. "
    ka "Not everything that makes people happy makes money, though."
    ka "Athletic careers are one of the hardest to succeed in. And I’m just some random girl who was born with good genes and a good work ethic."
    ka "There are plenty of other Karin Kanda’s out there. "
    ka "And I think that’s one of the reasons I get so overwhelmed when thinking about what to do from here on out."
    s "I figured that’s what was going on, which is why I suggested the housewife thing."

    scene karinseconddate11
    with dissolve

    ka "S-STOP SAYING THAT! MY HEART CAN’T TAKE IT!"
    s "Why? I think you’d make a great wife."
    ka "WHY?! ALL I DO IS RUN AND...KICK! AND THEN RUN SOME MORE!"
    ka "AM I YELLING RIGHT NOW? I FEEL LIKE I’M YELLING!"
    s "You’re definitely yelling."

    scene karinseconddate13
    with dissolve

    ka "Ugh...maybe you should invest in one of those shock-collar things and just...buzz me whenever I start saying weird stuff."

    "That sentence alone warrants like three buzzes. "

    if bonus == True:
        "Do not threaten a perverted man with the opportunity to put a shock collar on a [teenage]girl."

    scene karinseconddate6
    with dissolve

    ka "But really, though?...Who would want a wife like me?"
    ka "I thought guys normally liked more...petite girls. Ones more...feminine and stuff."
    ka "Like...I’ve gotten confessions from girls before, but never a boy."
    ka "I was under the impression I was a little too...intimidating?"
    ka "I don't know the right word to use."
    s "I think you’re looking for the word ‘cute.’"

    scene karinseconddate14
    with dissolve

    ka "C-C-C-C-C-"
    s "You’re going to have to stop reacting that way if you’re ever going to be a wife."

    scene karinseconddate11
    with dissolve

    if bonus == True:
        ka "STOP CALLING ME A WIFE! I’M STILL IN HIGH SCHOOL!"
    else:
        ka "ISHUDFHGIUSDHFOIASHDF!!!!!!!!"

    scene karinseconddate8
    with dissolve

    ka "I can barely form a...s-s-sentence around boys. No way could I marry one!"
    s "Obviously, it’ll take a lot of work. But I’ve seen how you act with Miku and Kirin before."

    scene karinseconddate15
    with dissolve

    ka "Wh-What do you mean by that?"
    s "The first time I met you was in the storage shed after that ball hit the door and Miku...did whatever that thing she did was."
    s "You knew exactly how to calm her down and what to do to resolve the situation."
    s "I’m an adult and all I was able to do was stand there in shock. "
    s "So, in a sense, you’re already more mature than I am."

    scene karinseconddate16
    with dissolve

    ka "Those are more motherly qualities than housewife qualities..."
    ka "Wives are supposed to be cute and...do things for the person they love and...bake."
    s "What an archaic way of looking at the roles of a housewife. Get with the times, Karin."
    ka "...I'm sorry?"
    s "All that really matters is finding someone whose tastes are in your favor."

    scene karinseconddate17
    with dissolve

    ka "Easier said than done."
    ka "At this rate, I’m going to wind up marrying a girl and raising a family of adopted children and driving them all to[school] in my mini-van."
    ka "And on the mantle where our family picture hangs, there will sit a lone soccer-trophy serving only to remind me of the future I could have led if I had just worked harder..."

    scene karinseconddate18
    with dissolve

    ka "But then one day, my adopted son will be drafted to Manchester United and I’ll be able to live out my dreams vicariously through him!"
    ka "He’ll grow old and raise a beautiful family and I’ll become the cool grandma who smothers her grandchildren with affection and lets them eat cereal for dinner."

    scene karinseconddate19
    with dissolve

    ka "But then my wife will be diagnosed with a life-threatening illness and be given only six weeks to live."
    ka "And in those final weeks, I will realize that it was never about boys or girls...it was about love."
    ka "And even though I was hesitant and nervous to introduce her to my family at first...we really did have {i}love...{/i}"

    scene karinseconddate18
    with dissolve

    ka "But then! Out of nowhere, my second adopted son will become a doctor and find the cure!"
    ka "My wife will be healed and I will-"
    s "Karin."

    scene karinseconddate14
    with dissolve

    ka "Ah-"
    s "..."
    ka "..."
    s "You’re a bit of a daydreamer, aren’t you?"
    ka "...No."
    s "You seem to have put a lot of thought into your future for someone who is apparently having trouble figuring things out."

    scene karinseconddate9
    with dissolve

    ka "O-Okay...so {i}maybe{/i} I do get lost in daydreams from time to time...but so does every girl."
    ka "We’re predictable. I understand how we work."
    ka "But when it comes to boys...I really have no idea."
    ka "I see them and my mind is just like “OH GOD! WHY DID I HAVE TO BE BORN WITH BROAD SHOULDERS?” and stuff."

    scene karinseconddate1
    with dissolve

    ka "But thanks for spending time with me regardless...even if it’s just to...develop a better relationship with the co-captain."

    "I find it surprising that Karin is able to stay so humble despite having what so many other people work tirelessly to obtain."
    "To see someone like her, who even [teenage]girls go out of their way to confess to, not realize how wonderful she is at first glance is truly a spectacle."

    s "I’m spending time with you because I want to spend time with you."

    if bonus == True:
        ka "You really shouldn’t say things like that to girls my age...We’ll get the wrong idea."
        s "Then get the wrong idea."
        ka "I’d really rather not. The wrong idea would give me a heart attack."
    else:
        s "Platonically, of course."

    scene karinseconddate9
    with dissolve

    ka "And I’ve already done a lot of running and blah blah blah blah blah boys are scary."
    s "Everything is scary. Welcome to life."

    scene karinseconddate20
    with dissolve

    ka "Huh?"
    s "Sorry. I almost let my cynical side slip out."
    s "I don’t think you’ve had the misfortune of seeing that part of me yet."
    ka "Are you normally a cynical person?"
    s "More or less."
    ka "I had no idea..."
    ka "I learned something about you today..."
    s "It’s not a very exciting or interesting thing to learn, though."

    scene karinseconddate21
    with dissolve

    ka "I...learned a thing about a boy..."
    s "...Karin?"

    scene karinseconddate1
    with dissolve

    ka "Ah! Sorry! I just got...weirdly happy all of a sudden!"
    ka "Totally not because we’re getting closer or anything! That would be like, {i}so{/i} weird, right?"
    ka "Hahahahahah!"
    ka "So weird!"
    s "...Right."
    s "Well, let’s call it here for today."
    s "Did you maybe want to get dinner on the way home or something?"

    scene karinseconddate8
    with dissolve

    ka "Dinner?! "
    ka "I don’t know what that is!"
    ka "I mean, I do know what it is!"
    ka "I have no idea why I told you I didn’t!"
    ka "I...umm!"

    scene karinseconddate11
    with dissolve

    ka "OKAY, SEE YOU!"

    scene black
    with dissolve2

    "Karin nervously hops off of the bench and runs over to a small leather bag, picking it up and slinging it over her shoulder as she jogs out of the park."
    "She’s still utterly terrified of me, sure, but at least she was able to smile more than normal today."

    if bonus == True:
        "I wonder how much longer it will be before she starts looking at me as a human being rather than a walking penis monster?"
    else:
        "I wonder how much longer it will be before she starts looking at me as a human being rather than a monster?"

    "But hey, that nervousness is one of her greatest charms."

    if bonus == True:
        "The other of which is her thighs."
        "Those two elements combine to make a wonderful human, and I’m glad that we get to spend time together like this..."

    $ renpy.end_replay()
    $ karindate5 = True
    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label karindate10:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene karinthirddate1
    with dissolve
    play music "retrospect.mp3" fadein 5.0

    "I show up at the park to find Karin dressed a bit differently than normal."
    "This is the first time she's worn her casual clothes to a meet-up, and I have to say they suit her really well."

    ka "..."
    s "..."

    "She stands nervously before me, saying nothing and just looking off to the side, waiting for me to take the lead."
    "Which I’m fine with, of course. It’s just a vast departure from how I’ve seen her act on the soccer field."

    if bonus == True:
        "But then again, the soccer field is filled with females and I have a penis."
        "So it goes."

    s "Are you not planning on running today?"

    scene karinthirddate2
    with dissolve

    ka "Oh, umm, I...went for a run earlier. So I thought that it would be fine to just...you know, {i}not{/i} run today."
    s "I’m not keeping you from hanging out with your friends, am I?"
    s "I know you and your sister are normally out and about, so sorry if you feel obligated to waste any of that time on me."

    scene karinthirddate3
    with dissolve

    ka "What?! N-No! It's not a waste at all!"
    ka "I’m totally free today. All day. And if you’re worried about me falling behind on practice or anything then-"
    s "Yeah, I’m definitely not worried about that. You practice more than anyone."

    scene karinthirddate4
    with dissolve

    ka "R-Right..."

    "Karin nervously fidgets with her hands behind her back, digging one of her sneakers into the ground and tracing a circle with it."
    "It’s a lopsided circle- one that would cause problems in art class."

    s "Is something wrong?"

    scene karinthirddate3
    with dissolve

    ka "Nothing is wrong! Everything is great! Super great!"
    ka "I’m not hiding anything behind my back!"
    s "I didn’t say you were hiding anything behind your back."
    ka "Good! Because I’m not!"
    s "I’m starting to think you are."

    scene karinthirddate5
    with hpunch

    ka "OKAYFINEHEREYOUGO!"
    s "..."
    ka "..."

    "Karin stretches her arms out and holds a bright pink bag several inches from my face."
    "It’s easy to see how much her hands are shaking due to how close she is. "
    "This is obviously the first time she’s ever given some sort of gift to a guy but...what is it exactly?"

    s "..."
    ka "..."
    s "What is this?"
    ka "..."

    scene karinthirddate6
    with dissolve

    ka "Cookies..."
    ka "I made...extra. And I thought you might want some."
    ka "But if not I’ll just throw them into the river."
    s "There’s no need to throw anything into the river, Karin..."

    scene karinthirddate4
    with dissolve

    "I take the bag from her and lightly shake it around a bit."
    "It feels like there’s a good amount in here. I highly doubt that she just happened to make {i}extra{/i}..."

    s "You made these specifically for me, didn’t you?"

    scene karinthirddate7
    with dissolve

    ka "N-No! I made them for...my mom and dad! "
    ka "But then I realized they were on a diet!"
    ka "And I suddenly had so many cookies and I thought to myself, “Who likes cookies?!”"
    ka "And then I thought of you!"
    ka "N-Not because I was thinking about {i}you{/i} but because...E-Everyone likes cookies!"

    scene karinthirddate8
    with dissolve

    ka "And that’s exactly what happened."
    s "Well, whatever the case, I’m very thankful for them. Can I have one now?"

    scene karinthirddate3
    with dissolve

    ka "Now?! No way! Wait until you get home!"
    ka "They’re probably bad anyway!"
    ka "In fact, give them back to me. The river isn’t far away and-"
    s "I’ll just eat them tonight...Thanks."

    scene karinthirddate9
    with dissolve

    ka "Hah...my heart feels like it’s going to explode and I didn’t even do any running today."
    s "I thought you said you went running earlier?"

    scene karinthirddate4
    with dissolve

    ka "O-Oh! Right! Yes! That is exactly why my heart must be beating so fast. Definitely not because of anything else. Nope. Nothing at all."
    ka "I mean, what would even be the cause of that?"
    s "...Do you really want me to say it?"

    scene karinthirddate10
    with dissolve

    ka "Please don’t..."
    ka "I beg you..."

    "I decide to give Karin a break and not explain to her that she might just be a {i}little{/i} bit infatuated with me for some indiscernible reason."
    "I’d be lying if I said I wasn’t impressed, though."

    if bonus == True:
        "Hell, I can’t even remember the last time any of the other girls gave me a non-sexual present."
        "Not to say that I wouldn’t accept something like that from Karin (I absolutely would) but cookies are still good."
    else:
        "No one ever gives me any presents and I admire her for being able to act on something that surely made her very nervous."

    "It must have been hard for her to give these to me."

    s "Okay, so, I won’t eat your cookies now. "

    scene karinthirddate1
    with dissolve

    ka "You can always...text me how they were later if you want to."

    if bonus == True:
        ka "I mean, it would obviously be a little weird for a grown man to text some random [teenager] but..."
    else:
        ka "I mean...obviously you'd never want to because you don't have unlimited texting, but..."

        "Why does she know that?"

    ka "You know...we’ve got phones so...we might as well use them, right? Hahahah..."
    s "Right..."
    s "But anyway, what did you want to do today if you’re not going to be running?"
    ka "I-I don’t know! "
    ka "If only there was...some sort of place that two people could go to kill time and...maybe eat dinner together..."

    "I feel like the last time I suggested something like that she ran away nearly crying."
    "Has she really changed her mind about that already?"

    ka "It’s very...unfortunate that a place like that doesn’t exist...right, Sensei?..."
    ka "I wonder what else there is to do?..."
    s "Karin."
    ka "...Yeah?"
    s "Are you pretending to not know what a restaurant is?"

    scene karinthirddate11
    with dissolve

    ka "I-Is it...working?..."
    s "If you want to go out to eat, just say it."
    s "There’s no point in trying to trick me into asking you out on a date."

    scene karinthirddate7
    with dissolve

    ka "MMMMMM! Don’t call it that!"
    ka "It’s embarrassing..."
    ka "It’s just...I mean...what else are we going to do?"
    ka "I didn’t bring my other clothes and...running without a sports bra on is kinda not something I want to do right now..."

    if bonus == True:
        "I can’t say I blame her. She’s rather...endowed for a girl her age."

    s "Well is there anywhere in particular you want to go? I still have some time before I have to leave tonight."

    scene karinthirddate10
    with dissolve

    ka "Oh...Umm, right...Of course you’d have stuff to do tonight. That’s fine..."
    ka "I’m sorry for expecting you to stay with me any longer. It’s obvious you’re busy and-"
    s "Hey, now. There’s no need to get all down on yourself. We can spend an entire day together sometime in the future."
    ka "That...really does make it sound like...you know."
    s "A date?"

    scene karinthirddate12
    with dissolve

    ka "NGH!"

    "Each time I insinuate something even slightly romantic or affectionate, Karin freezes up or cringes or does...anything else mildly comedic. "
    "With a sister like Kirin, I have no idea how she's able to act like this. It's the complete opposite personality."
    "Just what the hell is going on with that family?"

    s "Okay, okay. I’ll stop using the D-word."
    ka "D-WORD?! WHO SAID ANYTHING ABOUT THE D-WORD?!"
    s "Karin, I think you might be thinking of a different D-word now."
    ka "I’M NOT THINKING OF ANYTHING LIKE THAT. I DON’T EVEN KNOW ANY D-WORDS."
    ka "DOG? ARE YOU THINKING OF DOGS?"
    ka "DOGS ARE GREAT, AREN’T THEY, SENSEI?"
    ka "AM I YELLING AGAIN?!"
    s "Do you have an inhaler or something? It looks like you’re having a little trouble breathing."

    scene karinthirddate10
    with dissolve

    ka "Talking to you makes my chest hurt...I don’t like it."
    s "And yet you continue to hang out with me."
    ka "I even baked you cookies."
    s "I thought you baked those for your mom and dad?"
    ka "I did."
    s "But you just said-"
    ka "No I didn’t. "
    s "..."
    ka "..."
    s "Okay. Let’s just find somewhere nearby and get something to eat since you’ve apparently never been to a restaurant before."

    scene karinthirddate13
    with dissolve

    ka "Y-Yeah! Let’s d-d-d-d-do that! That sounds really f-f-f-f-f-f-f-f-"
    s "Just let me do the talking, okay?"

    scene black
    with dissolve2

    "Karin and I walk through the streets toward...well, anywhere."
    "She remains extremely tense the entire time."
    "And I mean extremely tense. It looks like every joint in her body has frozen up. "
    "But even though she’s struggling to maintain her composure, she follows gleefully alongside me and we eventually stop at a rather familiar place..."

    scene karinthirddate14
    with dissolve

    ka "..."
    s "..."
    ka "So umm...cafes...am I right?"
    s "Well, you are right in noticing that this is a cafe. Good job."
    s "I have to apologize in advance for something, though."

    scene karinthirddate15
    with dissolve

    ka "Apologize?! Did I do something wrong?!"
    ka "It’s too soon for us to go somewhere like this together, isn’t it?! "
    ka "I had no idea! I’m still really bad at this...I-I...I’ll do more research! I swear!"
    s "No, no. It’s nothing like that."
    s "There’s just one of my students here right now and I’m pretty sure that the two of us are going to be grilled in a matter of seconds."

    scene karinthirddate16
    with dissolve

    ka "For being seen together?..."
    s "Something like that..."

    scene karinthirddate17
    with dissolve

    ka "Oh...yeah. I’m sorry..."
    ka "Of course something like that would happen."

    "Frankly, I knew this was going to be a risk when the two of us came here. "
    "But I live for danger."
    "Just kidding. I live for cute girls. "
    "And I also want to see how Karin will act when she’s thrown into the fire."
    "Godspeed, co-captain."

    scene karinthirddate18
    with dissolve

    mo "Well, well, well...what do we have here?"
    mo "You bring a girl from our[school] into {i}my{/i} cafe? During {i}my{/i} shift?"
    mo "Is this some sort of test? What's your game here, Sir?"
    ka "Umm...Hey there. My name’s-"

    scene karinthirddate19
    with hpunch

    mo "SILENCE, WENCH!"
    ka "Oh. Uhh, okay. My bad..."

    scene karinthirddate20
    with dissolve

    mo "Sir. What is the meaning of this new character? How large is this pool of [young_girls] going to grow?!"
    mo "How do you expect to develop all of them?! Focus on the ones you have first!"
    mo "Can’t you see what Ireland has to offer?! Can’t you see me?!"
    s "Molly, this is Karin. She’s the co-captain of the[school] soccer team. "
    mo "This does not explain why you two are chatting over tea and crumpets."
    s "We haven’t even ordered anything yet."

    scene karinthirddate21
    with dissolve

    ka "We were just...practicing in the park and worked up an appetite."
    ka "Sensei recommended this place because of how much he likes it, so...I thought I’d give it a go too..."
    ka "Sorry if it seems like I’m intruding..."
    s "..."

    "How is Karin lying so naturally right now? I didn’t think she’d be the type to do something like that."
    "I don’t even need to think up an excuse now."
    "This is great."

    mo "Hmm...Well, at least you are polite."
    mo "But I have to say, I’m quite concerned by the size of your breasts. "
    ka "...I'm sorry?"
    mo "What are they? Double D’s? Triples?! Explain yourself!"
    ka "That’s...not something I’d like to discuss right now..."
    mo "Tch!"
    mo "You well-endowed women are all the same. Never wanting to discuss your sizes and leaving us flat girls to ROT in MISERY!"

    scene karinthirddate22
    with dissolve

    mo "YOU WILL BURN FOR YOUR SINS! BOTH OF YOU!"

    scene karinthirddate23
    with dissolve

    ka "..."
    s "..."
    ka "..."
    s "..."
    s "Yeah, so that’s what I was apologizing for."
    s "Molly doesn’t take too kindly to unexpected girls showing up and joining the harem."

    scene karinthirddate24
    with dissolve

    ka "Harem?!"
    s "That’s what she calls it at least. I think she wants to be recognized."
    ka "HAREM???????"
    s "...It was a joke."

    if bonus == True:
        "It wasn’t."
    else:
        s "As clear as it is than many of my students have feelings for me, I am simply not interested in any of them that way."

    scene karinthirddate25
    with dissolve

    ka "Phew..."
    ka "Hearing that made me a lot more...umm..."
    ka "Actually, never mind."
    ka "I never started that sentence."
    s "Agreed. You never started that sentence and we will do our best to avoid it coming up again in the future."
    s "So, are you ready to order?"

    scene karinthirddate26
    with dissolve

    ka "Oh! Almost! I just need a little more time to look at the menu if you don’t mind..."
    ka "I’m surprisingly picky when it comes to food. I still cut the crusts off of my sandwiches and everything."
    ka "I don’t know why I’m telling you this. Please stop me before I continue to embarrass myself."
    s "No, no. Please tell me more about how childish you are. It’s cute."

    scene karinthirddate27
    with dissolve

    ka "C!"
    ka "C-C-C-C-C-C-C-C!"

    scene black
    with dissolve2

    "Karin breaks again and takes a full five minutes to snap out of her cute-coma."
    "That’s what I’m going to call those moments from now on."
    "Is it really that hard for her to handle being complimented?"
    "You’d think that by now she’d at least be able to dodge the word or brush it off but...nope."
    "It is what it is, though."
    "The two of us wind up ordering coffee and a couple of sandwiches shortly after that."
    "They come on rolls, so Karin does not need to go through the trouble of removing the crust from hers."
    "Once we finish eating, we say our goodbyes and part ways in front of the cafe."
    "I think I can hear her squeal to herself in joy as she runs off toward home."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karindate10 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label karindate15:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."
    "It’s that weird part of the afternoon between lunch and dinner where I want to eat, but having four meals in one day is kind of frowned upon."
    "But I’m sure if I told Karin that, she wouldn’t mind."
    "Maybe the two of us could go out for lunch or something?"
    "That sounds like a thing she’d enjoy."
    "Sure, she’ll probably drop her phone when I ask, but I think she’d enjoy it when all is said and done."

    play sound "phonebeep.wav"
    play music "acoustic.mp3" fadein 15.0

    ka "Hello! I mean...hi!"
    ka "Hey!"
    s "All three of those mean the exact same thing, Karin. Any of them will work in the future."
    ka "Okay but “hello” is too formal and “hi” is too informal and if I accidentally added an extra y to “hey” you would have thought I was too clingy."
    s "Are these things that girls actually think of?"
    ka "Greetings! H...How are you today?!"
    s "Hungry."
    ka "Do you..."
    ka "Do you want me to make you lunch?"
    ka "Or...dinner, I guess?"
    ka "It's that weird part of the day between the two, so I don’t really know what to call it."
    s "I was actually wondering if you’d maybe want to go out to a diner or something?"
    ka "Ah! D-Diner?!"

    "A loud bang rings out through my cell-phone, signaling that Karin has, just as I expected, dropped the phone upon being asked out."
    "She’s so pure."

    ka "S-Sorry! My hand slipped! "
    ka "I had a lot of coffee today and...um...hands."
    s "Right..."
    s "So, what do you say?"
    ka "I’d love to!"
    s "Great, then-"
    ka "But..."
    s "Uh-oh."
    ka "My parents are expecting a package and they asked me if I could sign for it when it gets here."
    s "Can’t Kirin do it instead? "
    ka "I..don’t know where she is."
    ka "But, umm..."
    ka "Maybe if..."
    ka "If you wanted to...come over?"
    ka "I...I wasn’t really joking when I offered to make you lunch...or dinner."
    ka "Which one did we decide this was again?"
    s "I don’t think we did. "
    s "But if that’s really okay, I’ll start heading over now."
    ka "Okay! Yeah! I’ll...um..."
    ka "I’m gonna take a shower and get dressed then."
    ka "You...you know where I live, right?"
    s "Yeah. I’ve met Kirin there before."
    ka "Right...right. Yeah. Okay!"
    ka "Umm...just...call me when you get here, then!"
    ka "I’ll see you soon!"

    play sound "phonebeep.wav"

    "The two of us hang up and I begin to make my way over to the Kanda residence."
    "It will be the first time I’m hanging out with Karin alone in the apartment, and I fully expect it to be disastrous in the cutest possible way."
    "........."
    "......"
    "..."

    scene karinsushi1
    with dissolve

    "Karin lets me in after I text her about my arrival. And, before I know it, we’re awkwardly standing in the living room, staring at each other."

    ka "So...umm...did you find the place okay?"
    s "Yup. Didn’t I just tell you earlier that I remembered where you live?"
    ka "Y-Yeah...but my mom always talks about how boys can be forgetful, so...I thought maybe you’d...you know...forget."
    ka "She could just be saying all of that to justify how my dad forgot their anniversary this year, though."
    s "Well, it’s true that my memory is probably one of the worst you’ll ever find, but it’s for reasons entirely unrelated to anniversaries and whatnot."

    scene karinsushi2
    with dissolve

    ka "What’s...what’s wrong with your memory? Is it okay for me to ask that?"
    s "Let’s just say a lot of it disappeared. "
    s "And I guess the rest of it could technically disappear again...but only at several really specific moments."
    s "Like when seasons change or something."
    s "I don’t really understand how it works, to tell you the truth."
    ka "Is that...some sort of...disease?"
    s "No, it’s more like-"

    scene karinsushi3
    with dissolve

    ka "I...I’ll take care of you!"
    ka "You don’t need to worry, Sensei!"
    ka "I’ll wait by your bedside every morning and show you flashcards to remind you of who I am! And who everyone else is!"
    ka "You don’t have to worry! Everything will be okay!"
    s "I appreciate the offer, but I’m pretty sure I’ll be fine."
    s "Please continue to spend your mornings working out or whatever else it is that you do."

    scene karinsushi4
    with dissolve

    ka "I...watch the news sometimes?"
    s "While you’re working out, I’m guessing?"
    ka "...Maybe."
    s "Well, in the event that my memory {i}does{/i} randomly disappear again, I’d love for you to come remind me of who I am."
    s "You’ll probably have to fight off a small girl with red hair who will be attempting to do the same exact thing, though."

    scene karinsushi5
    with dissolve

    ka "But I don’t want to fight Ami...she’s so nice."
    ka "Maybe we can just take turns?"
    ka "Or I can just...cook for you while she reads you the flashcards."
    ka "I still want to make them, though. I have this weird thing where I just really like flashcards for some reason."
    ka "Do you want to talk more about flashcards? That sounds fun, right?"
    s "It sounds...like a thing."
    s "I’m more interested in the part about you cooking."

    scene karinsushi6
    with dissolve

    ka "Oh! Right! That’s why you’re here!"
    ka "I...I..."
    ka "Look! Table!"

    scene karinsushi7
    with dissolve

    "I “Look. Table.” to find that Karin has laid out two surprisingly large sushi platters."
    "And when I say “surprisingly large” I mean both the platters and the actual pieces of sushi are gigantic."
    "I was all about the idea of a fourth meal today, but...this might be a little too much."

    ka "So, umm...I’m sorry for not asking you what you wanted."
    ka "If you hate it, we can just order from somewhere."
    ka "Actually, let’s just do that right now. This clearly isn’t good enough for you."
    s "I’m sure it’s fine, Karin."
    ka "Oh! And...umm...I didn’t know what you would want to drink, so I just got you...one of everything we had."
    s "Is that canned coffee?"
    ka "Yes!"
    s "Do you normally drink canned coffee with sushi?"
    ka "No!"
    s "..."
    ka "..."
    ka "Oh God...I’ve ruined everything."
    ka "I’m so sorry, Sensei. I’ll just get my phone and-"

    scene karinsushi8
    with dissolve

    s "It's fine, Karin. There’s no reason to order takeout when you’ve already done this much."
    s "I’m not drinking the canned coffee, though."
    s "I’m no gourmet, but that doesn’t sound like it would be a good flavor combination."
    ka "Are you sure you don’t want a pizza or something? "
    s "I want to eat what you made."
    ka "..."
    s "..."

    scene karinsushi9
    with dissolve

    ka "Are you sure?"
    s "Of course."
    ka "But what if I’m not good enough?"

    scene karinsushi10
    with dissolve

    ka "Or...the food! I meant the food! What if the food isn’t good enough?"
    ka "You’ll never want to come over again and I’ll be too embarrassed to look at you during practice!"
    ka "Then I’ll have to quit the soccer team and start pursuing another sport full time and it will destroy my future and I’ll lose any scholarship I could have gotten and..."
    ka "And before I know it I’ll wind up severely injuring myself and never being able to play anything ever again!"
    s "I’m not sure how you got to the last part, but I think it might be time for us to sit down and eat."
    ka "Okay! But please...{i}please{/i} stop me if I start rambling again! I mean it!"
    s "Sure..."

    scene black
    with dissolve

    "Karin and I move to our respective spots at the table."
    "I take my place behind a plethora of beverages that she was apparently torn between-"
    "And she takes her place behind..."

    s "..."
    ka "Is...is something wrong?"

    scene karinsushi11
    with dissolve

    s "Is that a glass of wine?"
    ka "Wine?..."

    scene karinsushi12
    with dissolve

    ka "..."
    ka "That’s a glass of wine."
    ka "..."

    if bonus == True:
        ka "I’m not old enough to drink this."
    else:
        ka "I do not want this."

    s "You're not secretly an alcoholic, are you?"

    scene karinsushi13
    with dissolve

    ka "What?! No! I must have poured it by mistake when I was pouring yours!"
    ka "I’m only allowed to drink on special occasions!"
    s "Is today not a special occasion? "
    ka "It is! But...it’s a different kind of special!"
    ka "It has to be a holiday!"
    s "I kind of want to see you drink now."

    scene karinsushi14
    with dissolve

    ka "Wh...why would you want to see that?"
    s "Just curious about how much it changes your personality."
    s "Who knows? Maybe you’re a lot more relaxed with alcohol in your system?"
    ka "Please don’t say things that will lead to me having a drinking problem..."
    ka "If I find out wine is the key to holding a conversation with you, I’ll be sneaking bottles into[school] before I know it."
    s "This conversation never happened."
    ka "But...um..."
    ka "I...I wouldn’t mind if you...maybe came over for a holiday sometime...if you really wanted to see."
    ka "I can’t drink a lot but...it would make me happy having you around for something like that..."
    s "I’m sure it would. I can’t imagine your parents would feel the same way, though."

    scene karinsushi15
    with dissolve

    ka "Oh."
    ka "Right."
    ka "I have parents."
    s "Parents who I imagine wouldn’t be very fond of their daughter dating a staff member at the[school]."
    ka "Yeah...they-"

    scene karinsushi16
    with dissolve

    ka "Wait..."
    ka "Are..."
    ka "Are you saying you would...date me?"
    s "..."

    "Shit."
    "I guess I {i}did{/i} kind of say that."
    "It’s definitely not what I meant, though."
    "I mean, a relationship with Karin does sound like it would be...surprisingly normal-"
    "But a relationship in general isn’t something that I want."
    "Or at least it’s not something I think I want."
    "I don’t know."
    "Maybe in a different life."
    "As far as this one goes, though-"

    s "I’m sorry. I didn’t mean it like that."

    scene karinsushi17
    with dissolve

    ka "Ah, no! You don’t have to apologize! I wasn’t trying to put you on the spot!"
    ka "It just sounded like...you might...l-like me or something...that’s all..."
    ka "I mean, obviously you wouldn’t like someone like me. I don’t even know what kind of drinks you prefer with sushi."
    s "That’s actually the first thing I quiz my prospective girlfriends on."

    scene karinsushi18
    with dissolve

    ka "Hmm..."
    s "..."
    s "What’s that face for?"
    ka "I’m waiting to see which one you drink first in case this ever happens again."
    ka "Also, what other types of questions are on this quiz?"
    s "Look at you getting all serious in the face of romance."

    scene karinsushi19
    with dissolve

    ka "Oh my God! I did it! I flirted with a boy!"
    s "I'm not sure if I'd count something that small as flirting, but at least it was smooth."
    s "At least a lot smoother than openly celebrating your success."

    scene karinsushi20
    with dissolve

    ka "I’m a boy expert now."
    s "You haven’t been sneaking sips of that wine while I’m not looking, have you?"

    scene karinsushi21
    with dissolve

    ka "Of course not..."
    ka "But I’m...finally starting to calm down, I think."
    ka "My heart’s still beating out of my chest, but...I think that “dating” thing gave me a temporary boost to my self-esteem."
    s "Even though I immediately said I didn’t mean anything by it?"
    ka "Weird, right? Maybe that part just hasn’t settled in yet?"
    ka "Or maybe I’m just finally-"

    scene karinsushi22
    with dissolve

    ka "Wait. No. It’s here."
    ka "I’m going to die alone with ten cats."
    s "No one is truly alone with ten cats."

    scene karinsushi23
    with dissolve

    ka "Do you like cats, Sensei?!"
    s "Not really. "

    scene karinsushi24
    with dissolve

    ka "Oh."
    ka "But...their ears."
    ka "And their little noses..."
    s "I just meant that all human beings are inherently alone as a matter of principle, so the only way to properly judge loneliness is by sheer tangibility."
    s "If there are ten other living creatures in the same room as you, whether they be cats or humans, you are not {i}technically{/i} alone. "
    s "But you {i}are{/i} still alone. "
    s "Get it?"
    ka "..."

    scene karinsushi25
    with dissolve

    ka "But...their ears..."
    s "..."
    ka "And their little noses..."
    s "Let’s just eat now..."

    scene black
    with dissolve2

    "I decide to stop being depressing for a moment and enjoy the food Karin prepared for us."
    "I’m surprised she was able to make something as classy as a sushi platter with virtually no mistakes whatsoever."
    "I’m not even sure if Ami can make sushi at this level, and she’s pretty much a personal chef at this point."
    "I guess if anyone was going to be able to, though, it was Karin."
    "Despite her tomboyish hobbies and a physique that would make even professional athletes jealous, she’s a pure, wholesome girl at heart."
    "A wholesome girl who wants to make the people around her happy, and who wants to find happiness of her own without damaging anyone else in the process."
    "I wish her luck in that regard."
    "Personally, I don’t think something like that is possible."
    "But I’d be happy to be proven wrong."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karindate15 = True
    stop music fadeout 7.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."
    "{i}Thirty minutes later...I leave Karin’s house and decide to get on with my day...{/i}"

    jump saturdaynight

label karinsoccer15:
    scene karinoutage1
    with dissolve
    play music "retrospect.mp3"

    "It’s fucking freezing out today."
    "Sorry for the whiny introduction, but it’s hard to think straight given that my hands are too swollen to even make their way out of my pockets."
    "It doesn’t help that I got here way ahead of schedule either."
    "The sun was just starting to rise when I left the house, but I guess even that giant fucking ball of fire thought it was too cold to bother exploring today."
    "But I guess that’s just how winter can be sometimes."
    "This is the part where I’d normally tangentialize about the harsh realities of winter and how the cold of the air mimics the cold in all of our hearts-"
    "But fuck it."
    "I’m not in the mood today."
    "I need to buy gloves."

    ka "Oh...Sensei."

    scene karinoutage2
    with dissolve

    ka "You’re here...really early today."
    s "Oh, Karin. Good."

    if bonus == True:
        s "Let’s press our bodies together to stay warm."
    else:
        s "We should hug to stay warm."

    scene karinoutage3
    with dissolve

    ka "Ah..."
    ka "Wh...What?"
    s "It’s cold. And chances are we’re going to die if we don’t do something quickly."
    s "If you’re not going to embrace me, let’s at least head inside and-"

    scene karinoutage4
    with dissolve

    ka "Oh...umm..."
    ka "I’m sorry to be the one to break the news, but...practice is cancelled today."
    s "..."
    ka "Sensei?"
    s "So you’re telling me I came all the way over here in the freezing cold for absolutely nothing?"
    ka "Well...there's...me?"
    s "Why didn’t anyone tell me?"
    ka "Umm...the[school] sent out an email about the power being out, so...{i}all{/i} of the clubs are cancelled. Not just ours."
    s "I’m obviously not going to read a work email on my day off. "
    s "If I’m going to do anything involving[school], I’m going to be paid for it."

    scene karinoutage2
    with dissolve

    ka "Do you get paid for coming to soccer practice?"
    s "I..."
    s "I actually don’t know?"

    "Am I supposed to be getting paid for those hours?"
    "I’m going to have to ask Makoto..."

    s "Wait. If the power is out and practice is cancelled...why are you here?"

    scene karinoutage5
    with dissolve

    ka "I...umm..."
    ka "That’s a good question..."
    s "Well as long as it’s not something crazy like you only showing up because you figured I would disregard my emails and come to practice anyway despite my
    inconsistent tendency to do so on a regular basis."

    scene karinoutage6
    with dissolve

    ka "Haha! Yeah! As if I’d ever do something as crazy as that! Hahah!"
    ka "Hahahah!"
    s "That’s exactly what happened, isn’t it?"

    scene karinoutage7
    with dissolve

    ka "That is exactly what happened."
    s "Did you really want to see me that badly?"
    s "Your house is further from the[school] than mine, isn’t it? You’re probably freezing."

    scene karinoutage8
    with dissolve

    ka "I am, but...I really wanted to talk to you."
    ka "Not about anything in particular..."
    ka "I just thought now might be a good time..."
    s "You know you’re allowed to text me whenever you want, right?"
    s "It’s easier to get a hold of me that way compared to waiting behind a place that I may or may not show up to."
    s "Wait, how many times have you done something like this before?"
    ka "I don’t want to talk about that."
    ka "Also, if I text you out of nowhere, you’ll think I’m annoying and then you’ll never respond to me."
    ka "And then you’ll start avoiding making eye contact with me during practice, which will lead Miku to asking me what happened between the two of us."
    ka "Then, when she realizes how crazy I am, she’ll kick me off the team and I’ll have to explain to my parents that I am simply not meant to be in the same place as males."
    ka "The story ends with me becoming a nun. "
    s "It never ceases to amaze me how good you are at-"
    ka "Predicting the future? "
    s "I was going to say nonsensically rambling, but sure. Let’s go with that."
    s "So, there has to be something on your mind, right? There’s no way you’d come all the way over here to “talk about nothing in particular.”"

    if karinlied == False:
        s "Wait...this isn’t about Kirin again is it?"

        scene karinoutage9
        with dissolve

        ka "Oh, no! No..."
        ka "I won’t really bother you about that anymore unless I {i}have{/i} to for some reason..."
        ka "It’s not my room to...pry into her business."

        scene karinoutage10
        with dissolve

        ka "I just...wanted a chance for you to...get to know {i}me{/i} instead of just her."

        if bonus == True:
            ka "I...obviously know that the two of you are much...{i}much{/i} closer than you and me, but..."
            ka "But that doesn’t mean we...can’t still...talk, right?"
            ka "I...I like the time I spend with you. Even if 90%% of it is me tripping over my words and trying not to say anything stupid."
        else:
            ka "Especially since...she's a fucking huge bitch and I want her to die..."
            s "Woah. This isn't canon, is it?"
            ka "It...might be..."

        ka "But...if you think it’s weird...which I wouldn’t blame you at all for...I completely understand."

        "Interesting."
        "I was sure that after Karin’s reaction to hearing the truth about Kirin and me, she wouldn’t have gone out of her way like this for quite some time."
        "If not ever again."
        "But I guess some people are more inclined to wait for themselves to break and patch things up {i}then{/i} compared to safeguarding everything from ever breaking in the first place."
        "Not my best figure of speech but, again, it is fucking cold out."

    else:
        scene karinoutage11
        with dissolve

        ka "No, that’s really what it is!"
        ka "If you think I’m bad at...talking in real life, you should just see me any time I try to send you a text message."
        ka "I go through so many different versions of messages trying to figure out which one's the best and wind up never sending any of them because none of them are good enough."
        s "Karin, are you actually obsessed with me?"

        scene karinoutage12
        with dissolve

        ka "What are you talking about? It’s not like I’m purposely going out of my way to make more time for-"

        scene karinoutage13

        ka "Oh my God, I actually might be."

    s "I’m totally fine with hanging out and talking to you for a while, but..."
    s "Is there anywhere we could do it that isn’t this cold?"

    scene karinoutage14
    with dissolve

    ka "Oh...well, umm..."
    ka "All of the doors to the[school] are locked, but...I do know a place where we’ll at least be safe from the wind."
    ka "And the wind is what makes cold weather like, really cold. You know?"
    ka "Like it could be zero degrees out, but with wind chill it can get all the way down to negative six thousand."
    s "That is a made-up number."
    ka "Six-thousand is most definitely a real number."
    s "..."
    ka "..."

    scene karinoutage15
    with dissolve

    ka "Heheh...I made a joke."
    s "Was that your first one?"
    ka "For you, yes. Don’t pretend that this isn’t a big deal."
    ka "I never would have been able to do that until recently."
    s "Yeah, yeah. I’m so proud of you. Now, can we go to that anti-wind place? One more second out here and I’m probably going to die."
    ka "Of course...it’s not far."
    ka "Just follow me."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene karinoutage16
    with dissolve

    s "This is literally ten feet from where we just were."
    ka "It’s where I was taking shelter in between laps around the[school] building."
    ka "I’m sorry if the build-up made it seem better than it actually is."
    s "Better than nothing, I guess."
    s "So, now what?"
    ka "What do you mean now what?"
    s "Are you planning on making me lead the conversation even though you’re the one who entrapped me?"

    scene karinoutage17
    with dissolve

    ka "Wait, am I the one who is supposed to lead?!"
    s "You’re the pursuer in this scenario, so yeah."
    ka "That’s not what the magazine said! It said the boy will lead!"
    s "That sounds like an incredibly sexist magazine."
    s "Also, since when do you even read things like that?"

    scene karinoutage18
    with dissolve

    ka "It was one of Kirin’s..."
    ka "Since she always has such an easy time talking to you, I thought I might be able to get a little better at it if I did what she does."
    s "Properly socializing isn’t something you can just pull from a magazine."
    s "If communicating was that easy, fifty percent of marriages wouldn’t end in divorce."

    scene karinoutage19
    with dissolve

    ka "Ma...marriage?"
    ka "I just...I just want to have a..."
    ka "But I guess if you’re okay with...someone like me..."
    s "Did you really think a magazine would be the solution to this problem of yours?"

    scene karinoutage20
    with dissolve

    ka "I didn’t {i}not{/i} think it...wouldn’t {i}not{/i} be a solution?..."
    s "..."
    ka "..."
    s "Was that a joke, too?"
    ka "I think it was just me being awkward. I’ve been doing that a lot lately."
    ka "And by a lot I mean for my whole life."
    ka "It’s not just you I get like this with, either. It’s every single boy I’ve ever talked to."
    ka "Even with distant male cousins I’m like “Ahhhhhhhhh!”"
    s "There you go. You’ve picked out a conversation topic. "
    s "Keep rolling with it."

    scene karinoutage21
    with dissolve

    ka "Wait! I don’t even have that many cousins! How am I supposed to talk more about them?"
    s "I meant your past. Family life."
    s "How did the Karin next to me become the Karin I see every week?"
    s "Start at the beginning and just talk until you get bored or something."
    s "I’m much better at listening than I am at talking. And a girl like you is much better off not letting me lead."

    scene karinoutage22
    with dissolve

    ka "Start at the...beginning?..."
    ka "But that’s..."
    s "..."
    s "Not the very beginning..."
    s "Just as far back as you can remember."
    s "I’ll give you a push. What’s the oldest memory you have?"

    scene karinoutage23
    with dissolve

    ka "The oldest memory I have?..."
    ka "Huh..."
    ka "That’s kind of hard..."
    ka "I feel like my memory’s been getting kind of weird lately. Like it’s getting harder and harder to remember things from back then, but-"

    scene karinoutage24
    with dissolve

    ka "Probably when I met my little sister."
    ka "Well, around when I met her at least."
    ka "My oldest memory involves the two of us sitting in a playpen together."
    ka "I don’t think we were doing anything fun or interesting because...you know...babies. But if you want like, my {i}oldest{/i} memory, I think that’s it."
    s "Not surprised to hear your oldest memory involves Kirin."

    scene karinoutage25
    with dissolve

    ka "Why do you say that?"
    s "It just seems like everything you do involves her to some extent."
    ka "Not everything...but a lot. Sure."
    ka "Is that a bad thing, though?"
    s "No, but..."
    s "Doesn’t it ever get tiring?"
    ka "What do you mean?"
    s "Like, don’t you ever wish you were able to just do something on your own without thinking of how it would be if she were there as well?"

    scene karinoutage26
    with dissolve

    ka "Of course...All the time, actually. "
    ka "But having a younger sibling means accepting that you can’t just go off and do everything you want..."
    ka "Because there’s someone always watching you."
    ka "Besides, I don’t even know if I’d be nearly as good at things like sports if Kirin wasn’t around."
    ka "Like, sure, I’m naturally tall and that gives me an advantage."
    ka "But one of the main reasons I started working so hard in the first place was because I wanted to be the cool big sister that she looks up to and brags to her friends about."
    ka "I just wound up falling in love with soccer and stuff in the process."
    ka "So of course I often...think about what it would be like to do things without her and..."
    ka "And..."

    scene karinoutage27
    with dissolve

    ka "And that’s...kind of why I’m here today..."
    ka "Sure, I may have borrowed one of her magazines to give me some pointers but..."
    ka "I showed up."
    ka "And that’s something I didn’t do for anyone but myself..."

    "A long moment of silence squeezes its way into the narrow space between us, expanding and pushing us further apart."
    "I can see the sun expelling its cowardice off in the distance, returning as if to say “I was never gone at all.”"
    "“It was you insignificant humans that misjudged my intentions.”"
    "“But I return now, with tendrils of flame and spotlights that could burn your bodies to a crisp without the correct type of sunscreen.”"
    "The sun can talk in this particular fantasy of mine."
    "The real sun does not talk."
    "Probably."
    "I don’t know, man. It’s fucking cold."

    if karinlied == False:
        scene karinoutage28
        with dissolve

        ka "Can I...ask you something kind of selfish?"
        s "After all of that talk about how you're under constant supervision of your sister? Of course."
        ka "Then..."

        if bonus == True:
            ka "The two of you...being {i}involved{/i}..."
        else:
            ka "If you're going to be...hugging my sister..."

        ka "That doesn’t mean I...have to stop...doing things like this, does it?"
        ka "I feel...a lot safer around you than I do with other boys."
        s "You probably shouldn’t. I’m really not a good person."
        ka "That’s what you say, but...you’ve never done anything wrong to me."
        ka "So until you do...I..."
        ka "I want to keep seeing you."
        s "And if it starts to hurt you?"
        ka "Then I’ll stop and rethink my decision..."
        ka "But right now, this is what I want."
        ka "I didn’t really plan on saying that today, but..."
        ka "Here we are."
        s "Well, of course I think that’s fine as long as it’s what you want."
        s "But I can’t guarantee you you’ll like it."
        s "Similar people have done similar things in your position and-"
        s "..."
        ka "...Sensei?"

        "There’s a thought stuck somewhere in the back of my head."
        "I can’t tell if it’s my own."
        "But it stings a bit."
        "It stings a lot."
        "It’s so fucking cold."

        s "Sorry. Yeah, it’s fine if the two of us continue to spend time together."
        s "I’m your coach, after all. Who is going to hold the stopwatch if I’m not there?"

        scene karinoutage26
        with dissolve

        ka "You’re right. That’s a very important job."
        ka "And, umm...thanks! For bearing the cold with me today."
        ka "Next time I’ll...maybe try and come up with a text message that’s acceptable to send you instead of..."
        ka "Instead of waiting for something that might not ever happen to begin with."

    else:
        scene karinoutage26
        with dissolve

        ka "So...do you think my mission today was a success?"
        ka "Will this be a day that I can look back on and think, “Wow, Karin! Good job!” or am I going to look at myself in the mirror tonight and question every single word I used?"
        s "Knowing you, probably the latter."
        s "But I think it was a success."
        s "Sure, it would probably be a little healthier if your idea of “doing something for yourself” did not involve waiting in the cold for hours-"
        ka "Only like...half an hour."
        s "Okay, but there was the other day at[school] as well."
        ka "Half of that was spent waiting for Kirin, so that doesn’t count."
        s "It definitely counts. Stop waiting in the cold for me to walk by and text me like a normal human being."
        ka "I can try but...I can’t promise it won’t be the worst text message you’ll ever receive in your entire life."
        s "Now I’m just looking forward to how it could possibly be {i}that{/i} bad."
        ka "I’ll figure out a way. You’ll see..."

    scene black
    with dissolve2

    "Only a few more minutes pass by before neither of us can take anymore."
    "We stand up together, do one lap around the[school] together to warm our bodies-"
    "And then head our separate ways."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karinsoccer15 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label karinsoccer20:
    scene karinadventure1
    with fade
    play music "justbehappy.mp3"

    mi "I’m gonna dieeeeeeeeeeeeeee..."

    "Hi there."

    if bonus == True:
        "As much as I’d love to tell you that the reason these two girls are beet red and dripping sweat is sexual, it isn’t."
        "The reason for this is actually much simpler and...well, involves exactly what this gym is made for and why this team exists in the first place."
    else:
        "As you can see, I am a very good coach and am forcing the girls to become stronger through a strict but reasonable practice regimen."

    "The thing is, I’ve seen them practice a million times by now and have never seen them {i}this{/i} exhausted."
    "So...what was so different about today, you ask?"

    scene karinadventure2
    with dissolve

    mi "Did ya really have to be so ruthless today?"
    mi "Is givin’ ya free reign of the practice schedule goin’ to your head? This some sort of power trip?"
    ka "No...I just...read in a magazine that intense workouts can be good if done in moderation."
    ka "And we’ve never really gone at it that hard and long before."
    s "Ha."

    scene karinadventure3
    with dissolve

    ka "Hm? Why are you laughing?"

    if bonus == True:
        s "What you just said."
        ka "That we went at it hard and long? "
        ka "Is this some sort of inside joke?"
        mi "Nah. Sensei’s just bein’ bad with girls again."
    else:
        s "I just remembered a silly Vine I saw."

    ka "I don’t get it."
    s "That aside, you guys should be done for the day now, right?"

    scene karinadventure4
    with dissolve

    ka "Right!"
    ka "Like I said, it’s only good to do things like this in moderation. Overworking yourself on a daily basis is one of the easiest ways to destroy your body."
    s "Well that’s great for me because it means I get to actually talk to you two instead of just staring at you for a concerning amount of time."

    scene karinadventure5
    with dissolve

    ka "Um...please don’t stare for too long..."
    ka "It’ll make me...trip or something..."
    mi "There somethin’ you were lookin’ to do, Sensei? Or were ya literally just gonna talk to us?"
    s "Is there something wrong with “literally just talking to you?”"
    mi "Yeah. It’s boring."

    scene karinadventure6
    with dissolve

    mi "I wanna go on an adventure!"
    ka "An adventure?"
    mi "Yeah! No practice regime is too tough for Miku Maruyama!"
    mi "And now that her blood’s pumpin’, she’s ready to take on the world!"
    ka "Didn’t you just say you wanted to die?"
    mi "Nope!"
    mi "Sensei! How do you feel about an adventure?"
    s "Bad. "
    mi "Well tough cookies because you’re outvoted two to one!"

    scene karinadventure7
    with dissolve

    ka "Oh, okay. I guess I choose the adventure option instead of taking a shower like I really wanted to."
    mi "We can shower later! "
    mi "I hate gettin’ in there next to you anyway, Karin."
    mi "I learned recently that what I lack in the chest department, I make up for in abs- and you’ve got me beat in both of those things."
    ka "Yes, Miku. You remind me of that after every practice."
    s "Karin, if you’re not feeling up to it, I’m sure that the two of us could overpower-"

    scene karinadventure8
    with dissolve

    ka "I’m fine with an adventure...I’m just not very good at coming up with ideas, so it will probably be really boring and you’ll probably hate it."
    s "Anywhere is fine as long as I can be with you."

    if karinlied == True:
        scene karinadventure9
        with dissolve

        ka "Wha-?!"
        ka "Wh-wh-wh-wh-what are you saying?! That makes it sound like you and me are..."
        mi "Ooooh, direct hit. Nice job, Sensei."
        s "Are what, Karin?"

        scene karinadventure10
        with dissolve

        ka "I...I don’t know!"
        ka "Ask someone else!"

    else:
        scene karinadventure11
        with dissolve

        ka "Are you...sure you’re not confusing me with my sister?"
        mi "Hm? Kirin’s not even here today."
        s "..."

        if bonus == True:
            "Well, it looks like it’s still a little too early to make jokes like that after coming clean about my...{i}relationship{/i} with Kirin."

    scene karinadventure12
    with dissolve

    mi "Alls I know is...if we’re gonna do this thing, we better get goin’ soon!"
    mi "And since it was {i}my{/i} idea to go on this adventure in the first place, I leave choosin’ the adventure up to you two."
    s "I hereby relinquish all responsibility onto Karin as I didn’t even want to do this in the first place."
    s "I am more than happy with staying here and making more suggestive jokes that Karin doesn’t understand."
    ka "It’s...not really much of an {i}adventure,{/i} but...I kind of needed to go get something from my classroom..."
    ka "Would...that work?"

    scene karinadventure13
    with dissolve

    mi "Heck yeah it would! And it’s close enough that Sensei probably won’t even complain about it!"
    s "Well...it {i}is{/i} in this building..."
    s "So yeah. I guess that’s fine."

    scene karinadventure14
    with dissolve

    mi "Heck yeah! Adventure crew away! First person to make it to Karin’s classroom is crowned the queen or king of...adventuring or something!"
    ka "Um...yaaaaay?"

    scene black
    with dissolve2

    "Karin and Miku get off the ground, grabbing their bags and dropping them off in the girls’ locker room before coming back out and...setting off on what I imagine will be a rather anticlimactic journey."
    "Of course, Miku takes the lead and leaves both Karin and myself lingering in the background, equal parts confused and curious."
    "And, without any further delay, things become more or less as exhausting as I expected them to be as soon as the word “adventure” was broken out."

    scene karinadventure15
    with dissolve

    mi "There! At the end of this hall lies our final destination!"
    ka "Um...actually...my room is on the second floor..."
    mi "Right! You’re so stacked that I often forget you’re a second year!"
    ka "..."
    s "Can you really say you didn’t expect things to turn out like this?"

    scene karinadventure16
    with dissolve

    ka "Well it’s not like I had a choice, is it?"

    if bonus == True:
        s "You literally gave up and let Miku vote for you. The three of us could be in the locker room together right now if you and I out-voted her."
        ka "I think you mean the gym, Sensei. You're not allowed in the locker room."
        s "I said what I said."
    else:
        s "You were literally given a chance to vote, Karli."
        ka "Who is Karli?"
        s "You will find out in a second."

    mi "You guys...I can only hold this pose for so long."
    mi "If we’re gonna get past the dreaded six headed janitor demon, we’re gonna need to be real tactical with our movements and whatnot!"
    mi "Then, once we find the destination...treasure will await!"

    scene karinadventure17
    with dissolve

    ka "There isn’t any treasure...I just need to grab my history textbook so I can study for a test."
    mi "Ahh, yes....tests."
    mi "I remember the days when {i}I{/i} was forced to learn!"
    mi "Now, I’m free to wander the halls and the world to my heart’s content with my trusty companions...Karli and...Steve!"

    scene karinadventure18
    with dissolve

    ka "Your real name is Steve?"
    s "Yes. It’s nice to meet you, Karli."
    ka "You don’t look like a Steve."
    s "Karin, come on. You’re smarter than this."
    mi "I...am...losing...my...patience!"

    scene karinadventure19
    with dissolve

    ka "Let’s go, Steve."
    ka "I’m sure it won’t be a very exciting adventure...but I guess we can have fun just...watching Miku have fun."
    s "I still think we should have had fun in the locker room instead."
    ka "Gym, Steve."
    ka "It’s called a gym."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Karin and I walk slowly behind Miku as she marches down the halls of the[school]."
    "The sound of her footsteps bounces off of the walls as she makes her presence known to virtually every person still inside of the building."
    "I’m not a fan of the idea of being spotted with these two outside of normal[school] hours, but I guess I could always fall back on the fact that I’m just their coach or whatever."
    "Unless there was supposed to be some sort of formal process for me to actually {i}accept{/i} and {i}assume{/i} that position."
    "Now that I think of it, there probably was."
    "So, if we {i}are{/i} caught, I guess I’ll just have to, once again, take up the role of “mildly weird guy hanging out with girls who are way too [young]for him.”"
    "But hey, at least one of those two is responsible."

    if bonus == True:
        "And the other one needs to sleep strapped into her bed so she doesn’t wind up dry humping older men in the middle of the night."

    mi "Ahoy, mateys! Land ho!"
    s "Are we pirates now?"
    ka "A...Argh!"
    s "Karin, come on."
    ka "What?...I want to play along too..."

    "........."
    "......"
    play sound "slidedoor.mp3"
    "..."

    scene karinadventure20
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "Karin looks out of the window as she removes a textbook from the depths of her desk."
    "Her tanned skin catches and absorbs the sunlight, distributing a fair amount of Vitamin D3 throughout her toned and divinely shaped body."
    "I think about how many of the nutrients must have been intercepted by the glass and then attempt to wrap my mind around how light can carry value in the first place."
    "The only value I’ve ever assigned to things like that is the importance of its existence in terms of brightening up dark areas."
    "But when the world itself is overcome with darkness, no amount of sunlight or Vitamin D3 can truly return it to form."

    mi "Adventure complete!"
    mi "It wasn’t a {i}long{/i} journey, but it was a journey nonetheless!"
    mi "Now, for our next adventure, I’d like to propose-"

    play sound "texttone.wav"

    mi "Hm?"
    s "Your phone?"
    mi "Guuuuuh. Yeah. Looks like Makoto needs to check on somethin’."
    mi "Sensei! Keep an eye on Karin and make sure she doesn’t go...learning! Or doing other[school] stuff!"
    mi "Just...do what you do best, I guess, and I’ll be right back!"

    play sound "slidedoor.mp3"

    "Miku leaves the room and suddenly the two people who didn’t even want to be a part of this adventure are the only ones left in the party."
    "It’s not too nerdy for me to say that, is it? Party?"
    "Who came up with that word anyway?"
    "How much Vitamin D3 can bleed through glass?"

    ka "I like the second floor, you know."
    s "...What?"

    scene karinadventure21
    with dissolve

    ka "S...Sorry...That probably sounded a little weird without any context, didn’t it?"
    s "I mean...I’m not really one to judge peoples’ hobbies or interests..."

    scene karinadventure22
    with dissolve

    ka "What I mean is that I kind of...like being in the middle of things."
    ka "Being at the bottom sucks because you have so many stairs to walk up if you ever want to go to the roof or something like that-"
    ka "Granted, walking up stairs is an excellent form of cardio and-"
    s "Finish your analogy before talking about exercise, please."

    scene karinadventure21
    with dissolve

    ka "Heheh...whoops..."

    scene karinadventure20
    with dissolve

    ka "So, continuing from where I was...being at the top is also kind of frustrating because the only place to go from there is down."
    ka "When you’re in the middle, it’s like everyone is going to be forced to see you at some point. And you’re always only one step away from wherever you want to be."
    ka "I guess that wouldn’t really matter in a[school] with more than three floors, though."
    s "If you’re trying to get some sort of point across, I’d appreciate a more direct approach."
    s "Stairs are great and all-"
    ka "And excellent for cardio."
    s "Yes. And that."
    s "But even though I’m in a classroom right now, I’d prefer to keep my “teaching hat” off."

    scene karinadventure23
    with dissolve

    ka "Can I...tell you one of the reasons I like you as a coach, Sensei?"
    s "Does it have something to do with stairs?"
    ka "A little bit. Yeah."
    ka "But...one of the reasons I like you as a coach, even though you barely do any {i}coaching{/i}...is that you don’t really expect any more out of me than you do anyone else."
    ka "It’s kind of refreshing in a way."
    ka "Like I can hang out on the second floor for as long as I want and you’ll just walk past me and not be like, “Karin! Someone upstairs needs you!”"
    s "Are you exhausted?"

    scene karinadventure24
    with dissolve

    ka "From practice or in general?"
    s "From all of the people trying to make you change floors."
    ka "..."

    scene karinadventure25
    with dissolve

    ka "Kinda. "
    ka "Yeah."
    ka "And I can’t even complain about it because then it will just sound like I’m stepping on the toes of everyone who wishes they were as...tall or...muscular or-"
    s "Talented?"

    scene karinadventure26
    with dissolve

    ka "..."
    ka "Sorry. I’m just being dramatic, I think."
    ka "It’s not like I planned on talking about this today or anything."

    scene karinadventure27
    with dissolve

    ka "Just...thinking out loud as I look outside the window."
    ka "Wishing I could trade places with someone like Kirin for a day or two...and not being able to talk to {i}her{/i} about it because she’ll just get mad."
    s "Yeah, it would probably be best if you never repeated that to her."
    ka "Which is part of the problem."
    ka "Her and my parents...they all think I’m some sort of...amazing human being. The rest of the girls on the soccer team do too."
    ka "Like, Miku is better than me in pretty much every way, but still {i}I’m{/i} the one people are looking up to most of the time."
    s "To be fair, it’s probably pretty difficult to look {i}up{/i} to Miku."

    scene karinadventure28
    with dissolve

    ka "I was hoping that joke wasn’t coming."
    s "I couldn’t resist and I’m sorry."
    s "But hey, on the bright side, you’re still {i}technically{/i} on the second floor from at least an academic standpoint."
    ka "True. But even that has its downsides."
    s "Like?"
    ka "Like..."

    scene karinadventure29

    with dissolve

    ka "L...Like I...can’t be in your class, for example..."
    ka "You’re the first b...boy I’ve ever been able to talk to without exploding..."
    ka "So if I got to see you every day, maybe I’d get better at facing one of my many, many fears?"
    s "Many?"
    s "How many fears can someone like you have?"

    scene karinadventure30
    with dissolve

    ka "Hm..."
    ka "Let’s see..."
    ka "So there’s snakes..."
    ka "And heights...and large fish..."
    ka "And that sound macaroni and cheese makes when you stir it."
    ka "And graveyards and gondola rides."
    ka "And those weird dream loops you get where one dream ends only to throw you into the middle of another one-"
    ka "And then the next thing you know, you have to change a tire for Serena Williams on the way to Newark, New Jersey."
    s "...What?"

    scene karinadventure31
    with dissolve

    ka "I’m scared of a lot of weird stuff, okay?! It’s not my fault!"
    ka "B...But..."

    scene karinadventure32
    with dissolve

    ka "I’m a little less scared...whenever you’re around..."
    s "..."
    ka "..."
    s "..."
    ka "..."

    play sound "slidedoor.mp3"

    mi "Okaaaaaay! Miku’s back, y’all! Which means-"
    mi "Hey, what are you two doin’ just standin’ around in silence?"
    mi "I know I’m the leader of the adventure squad, but if we’re ever gonna find {i}real{/i} treasure, we’re gonna have to bump up the team chemistry!"
    mi "So go ahead and hug it out so we can get a move on!"

    scene karinadventure33
    with hpunch

    ka "I-I-I-I can’t hug Sensei! We’re not married yet!"
    s "Yet?"
    ka "You know what I mean!"
    s "I do?..."
    mi "Blah blah fear of boys blah blah. "
    mi "You’d think somebody as tall and muscular and talented as you wouldn’t have any trouble at all with somethin’ like that, Kari-"
    mi "Err, I mean...Karli!"

    scene karinadventure34
    with dissolve

    ka "Right..."
    ka "You...{i}would{/i} think that...wouldn’t you?"

    scene black
    with dissolve2

    "We have three more adventures before the morning comes to an end."
    "All of them take place on the second floor of the[school] building."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karinsoccer20 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label karindate20:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer. "
    "Soccer practice has already ended for the day, so she’s likely either on her way home right now or..."
    "I don’t know. Doing something else?"
    "It’s not like I have a tracking device on her or anything."
    "Though, if I separated everyone I know into two categories of “Would let me install a tracking device inside of them” and “Wouldn’t do that...”"
    "I think Karin would probably be in the first group."

    play sound "phonebeep.wav"
    with hpunch
    play music "justbehappy.mp3"

    ka "AAAAAAAHHHHHH!!!!!"
    s "..."
    ka "..."
    ka "Hi."
    s "What the fuck was that?"
    ka "I’m sorry...I’m just really frustrated right now. "
    ka "I didn’t hurt your ear, did I?"
    s "Did you say something? I can’t really hear you over the constant ringing in my ears."
    ka "Ah! Sensei, no! I didn’t mean to!"
    ka "Do you need medical attention? Should I come meet you somewhere?"
    ka "Where are you? I’ll bring my first aid kit and-"
    s "Karin, chill. I’m fine."
    s "Just a little surprised to hear you of all people yelling."
    ka "I know, I know...It’s just my stupid little sister."
    ka "Just kidding. She’s not stupid. I love her."
    ka "But really. It’s Kirin. She’s been getting on my nerves a lot lately and I don’t even have anyone to talk about it with since all of my friends are {i}also{/i} her friends."
    s "All of them?"
    ka "Well...all of the ones I’d normally complain about stuff to."
    s "Well...I’m available if you want to vent to me."

    if karinlied == False:
        ka "..."
        s "..."
        s "Karin?"
        ka "And you’ll keep anything I say hidden from her even though...you two are..."
        s "Sure. Just because I was honest about my relationship with her to you doesn’t mean we can’t talk anymore."
        ka "...Yeah."
        ka "Yeah, okay. That’s...fine."

    else:
        ka "Do you..."
        ka "Do you really mean that?"
        ka "You’re okay with me taking up a bunch of your time just to complain about stupid stuff that you’re in no way involved with?"
        s "{i}As long as I can be with you.{/i}"
        ka "S-Stop saying that! "
        ka "You said that at the locker room too and it made my heart go all GAAAAAAAAAHHH."
        ka "AAAAAAAAHHH I JUST WANNA YELL!"
        s "..."
        ka "..."

    ka "There’s um..."
    ka "There’s a new diner by my house if you’d want to maybe meet there?"
    s "That works for me. Just send me the address and I’ll start heading over."
    ka "Okay! Cool!"
    ka "I’ll...do that right now then!"
    s "Sweet."
    ka "Yeah! Really sweet!"
    s "Yup."
    ka "So...sweet..."
    s "..."
    ka "..."
    ka "Anyway, bye!"

    play sound "phonebeep.wav"

    "Karin awkwardly hangs up the phone and sends me the address of the diner we’re meeting at a few seconds later..."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene karinangrybreakfast1
    with dissolve

    ka "I’m sorry for ordering so many sweets. I always crave sugar when I get angry."
    s "That is possibly the cutest reaction to getting angry I have ever heard."
    ka "I’m so angry I’m not even going to react to you using the C word at me."
    s "Wow. It must be really bad then, huh?"

    play sound "thump.mp3"
    scene karinangrybreakfast2
    with hpunch

    ka "I’m always so nice to her and she treats me like I’m the worst thing in the world!"
    ka "Like, I get that you’re automatically supposed to be jealous of me since I’m the older sibling, but cut me some gosh darn slack already!"

    scene karinangrybreakfast3
    with dissolve

    ka "I’m sorry for my language, too. You shouldn’t have had to hear that."
    s "I’m really seeing a brand new side of you today."
    ka "I’m sorry...I made you walk all the way over here and I’m just...jumping straight into things before you’ve even gotten to eat."
    s "Oh, don’t worry about that. I’m not really hungry."

    scene karinangrybreakfast4
    with dissolve

    ka "What? No. Tell me that’s not true. Please be hungry."
    ka "I don’t want to have to eat all of this by myself. I’ll get diabetes."
    s "Well you should have thought of that before your anger-induced sweet tooth kicked in."

    scene karinangrybreakfast5
    with dissolve

    ka "Maybe if I just...don’t have another cheat day until next winter it will be okay?..."
    s "So, what’s going on?"
    s "There had to be something in particular for you to get like this, right?"
    ka "Yeah, but..."
    ka "I might come off as a little needy or...annoying once I start explaining things."
    ka "Are you okay with that?"
    s "I wouldn’t have come if I wasn’t."
    ka "Then..."

    scene karinangrybreakfast6
    with dissolve

    ka "You know how you’re going to the beach soon, right?"
    s "In the middle of winter. Yes."
    ka "And you remember how I came with you last time?"
    s "In the middle of summer. Yes."
    ka "Yeah. Exactly."

    "Oh. Okay. I guess there won’t be any bigger reaction to the weird blurs in time with Karin."
    "Either that or she’s just so infuriated that it went completely over her head."

    ka "So...I had a lot of fun last time."
    ka "Even if Kirin ignored me for most of the trip, I got to hang out with Miku and...almost only killed one person with a baseball bat."
    s "Maya hasn’t been walking the same ever since."

    play sound "thump.mp3"
    scene karinangrybreakfast7
    with hpunch

    ka "She hasn’t?!"
    s "Karin, it was a joke. And please stop hitting the table like that. You’re going to break something."

    scene karinangrybreakfast4
    with dissolve

    ka "I’m sorry..."
    ka "But...I was asking her about it this morning because I thought it would be fun to tag along with you guys again...even if I’m not in your class..."
    ka "And she just kept saying all of this stuff about staying out of her personal life and that I wasn’t welcome there."
    ka "But I {i}know{/i} that isn’t true because Miku and Ami both invited me already."
    s "Then what’s the issue? Just show Kirin that you’re your own person and that you can do whatever you want."
    ka "That’s what I want to do, but..."
    ka "I also know that things aren’t really that great between us and that doing something like that after she asked me not to could just...make everything worse."

    scene karinangrybreakfast5
    with dissolve

    ka "So here I sit...in a diner, surrounded by a spread of food that could very well end my athletic career, complaining about it to her teacher."
    s "Don’t worry. I’m already used to all types of girls complaining about all sorts of things to me."
    s "At least you’re not asking me to kill anyone in order to save the world."
    ka "Yeah...I guess things could be worse if-"

    scene karinangrybreakfast8
    with dissolve

    ka "Wait? Killing someone to save the world?"
    ka "Is this really the level of problems the other girls you know have? Because if that’s true, I’m going to feel very immature about whining over something so small."
    s "It’s a long story. But either way, you shouldn’t feel small no matter what."
    s "You said there was no one else for you to talk to about this- and I don’t really think I’ll be able to {i}help{/i} in any way other than just listening, but..."
    s "I think it’s healthy for you to get mad."
    s "Maybe not the whole...binge eating thing that's going on here, but the anger alone."

    scene karinangrybreakfast5
    with dissolve

    ka "Ugh...I really hate getting angry, though."
    ka "Even when I was a baby, any time my parents disciplined me, I never screamed or cried or anything like that."
    ka "I just sat in my crib and silently sobbed to myself while they watched Jeopardy."
    s "Huh. Maybe your living situation isn’t as normal as I thought it was after all."

    scene karinangrybreakfast9
    with dissolve

    ka "It’s plenty normal. Really."
    ka "I just get overwhelmed really easily and don’t want anyone getting hurt because of me."
    ka "And sometimes...it feels like Kirin is trying to hurt me on purpose."
    ka "Like, what would it matter if I {i}did{/i} come to the beach? Why would {i}that{/i} bother her when she knows full well she’s met a bunch of people through me?"
    ka "Does it not go both ways? Am I not allowed to have a life of my own but she is? How is that fair?"
    s "It’s not."

    play sound "thump.mp3"
    scene karinangrybreakfast7
    with hpunch

    ka "Right?!"
    s "Karin, please."
    ka "I’ll replace it if I really do break the table! I just need this right now, Sensei!"
    ka "I’m so fed up with doing everything to try and get Kirin to like me only to have her be all like...“Grrr! I’m Kirin!”"
    s "Wonderful impression. I think you’ve found your next career if all of this food really does end your life as an athlete."

    scene karinangrybreakfast10
    with hpunch

    ka "AAAAAAAAHHHHHHH!"

    "I turn my gaze to the side to see if anyone is looking over this way and...of course, literally everyone is."

    ka "I’M SORRY TO EVERYONE JUST TRYING TO ENJOY THEIR MEALS BUT I AM VERY MAD AND HAVE AN UNGRATEFUL LITTLE SISTER!"
    s "Karin, it doesn’t work that-"
    s "Wait, why did everyone go back to eating their food like none of this ever happened?"

    if karinlied == False:
        scene karinangrybreakfast11
        with dissolve

        ka "Sensei...you {i}must{/i} understand her a little better than me, don’t you?"
        ka "Since you two are...you know..."
        s "The only thing I understand about Kirin is that she’s self destructive in pretty much every way imaginable."

        if bonus == True:
            "I also understand that she thoroughly enjoys giving blowjobs, but that isn’t something I feel the need to disclose to Karin."

        ka "She’s not supposed to be like that, though."
        ka "She’s supposed to come to me if she feels like she’s in trouble...or when things become too much for her to bear."
        ka "That’s what sisters are for. But if she won’t even come to me, then-"
        s "There’s a flaw in what you just said, though, Karin."
        ka "A flaw?..."
        ka "What flaw?"
        s "There is no way that people are “supposed to be.”"
        s "Kirin’s her own person who’s going to do things her own way."
        s "And it sucks that she’s apparently against you being {i}your{/i} own person, but isn’t a nonsensical decision like that something we should expect from her by now?"
        s "Just...keep telling her she’s a good girl or something and I’m sure she’ll soften up in time."
        ka "..."
        s "..."

        scene karinangrybreakfast12
        with dissolve

        ka "Is that...what you did?..."
        ka "To...get her to like you, I mean..."
        s "Surprisingly, I didn’t have to do {i}anything{/i} to get her to like me."
        s "She just came to me one day and that was that."
        ka "I wish I was that lucky..."
        s "If you were born a male, you probably would have been."
        ka "That’s not lucky at all. I’d look at myself in the mirror and immediately faint."
        s "I don’t know if your fear would exist if you were-"
        s "You know what, that doesn’t matter."
        s "What does matter is that you don’t let yourself get bogged down by the actions of a girl that literally no one, not even Kirin herself, understands."
        ka "..."
        ka "Yeah..."

    else:
        scene karinangrybreakfast5
        with dissolve

        ka "I just..."
        ka "I just want to understand her."
        ka "She’s supposed to come to me if she feels like she’s in trouble...or when things become too much for her to bear."
        ka "But instead, she just...pushes all of that anger onto the people around her and-"

        play sound "thump.mp3"
        scene karinangrybreakfast13
        with hpunch

        ka "Ah! That’s what I’m doing now!"
        ka "I’m Kirin Kanda! There is no more Karin!"
        s "Please remain Karin. One Kirin is more than enough for the world."
        s "Besides, I don’t really count venting like this as “pushing your anger onto other people.”"
        s "The key difference between you and Kirin is that you don’t actively want to make other people feel bad."

        scene karinangrybreakfast6
        with dissolve

        ka "And you think that she does?..."
        s "At the very least, I think she wants {i}you{/i} to feel bad. And all the evidence I really need for that is the dent you’ve put into our table."

        scene karinangrybreakfast14
        with dissolve

        ka "Oh my God, did I actually-"
        s "It was just a guess. I don’t know if the table is actually dented or not."
        s "But what I’m trying to get at is that you can’t let yourself get bogged down by the actions of a girl that literally no one, not even Kirin herself, understands."
        ka "..."
        ka "Yeah..."

    play sound "thump.mp3"
    scene karinangrybreakfast15
    with hpunch

    ka "Yeah!"
    ka "I’m not going to let Kirin decide what I can and can’t do!"
    ka "I’m my own person!"
    ka "I’m gonna go to the beach with my friends!"
    s "I’m very proud of-"

    scene karinangrybreakfast16
    with hpunch
    play sound "cheer1.mp3"

    s "...you?"

    "The rest of the diner erupts into a fit of applause and people leave their seats to start clapping for Karin."
    "And, in other news, Kumon-mi keeps getting weirder and weirder."

    ka "Heheh~"
    ka "Thank you very much everyone, but please hold your applause."

    stop sound fadeout 7.0
    scene karinangrybreakfast17
    with dissolve

    ka "Sensei...I’m sure I don’t have to say this...but thank you for letting me complain to you today."
    ka "It...definitely {i}is{/i} good that I was able to get all of this off my chest. Even if I’m about to put another fifty pounds on after all of the sugar you are about to watch me consume."
    s "Hey, consume away. It wouldn’t be the first time I’ve looked on in curiosity as a girl consumes sugary food."
    ka "..."
    ka "What?"
    s "Long story."
    ka "..."
    ka "What?"
    s "Anyway, how are you going to come to the beach if it’s not with Kirin?"

    scene karinangrybreakfast18
    with dissolve

    ka "Hmm...that’s a good question..."
    ka "I think Miku and Makoto were heading there with Kirin and {i}her{/i} roommate, so...I guess I’ll have to make the trip alone?"
    s "Would it be weird if you were to come with Ami and the rest of her group?"

    play sound "thump.mp3"
    scene karinangrybreakfast19
    with hpunch

    ka "With Ami?! The Ami who lives at your house?! "
    ka "Meaning that I would show up to your house really early in the morning to see you waking up and walking around in nothing but a T-shirt?!"
    s "Do you...think that’s just how I walk around the house when there are visitors there?"
    ka "I don’t know! Yes? No?"
    ka "Is it?!"
    s "Karin-"

    scene karinangrybreakfast20
    with dissolve

    ka "No! Don’t tell me! I don’t wanna know!"
    ka "I’ll just find out and maybe have to wash my eyes out with soap when I come to your house to tag along with Ami!"
    ka "Anyway, thanks for talking! Bye, Sensei!"
    s "Karin, hold on a-"

    scene karinangrybreakfast21
    with dissolve

    s "...second."
    s "..."
    s "..."
    s "..."

    scene karinangrybreakfast22
    with dissolve

    ka "..."
    s "Did you forget you ordered breakfast?"
    ka "Mhm..."
    s "Do you want to pretend you never walked out of the diner?"
    ka "..."
    ka "Mhm..."

    scene black
    with dissolve2

    "Karin winds up only eating around 30%% of what she ordered and stuffs the rest into an assortment of boxes to take home."
    "And I think she manages to get over her anger as well, as I can make out the sound of her whispering something about how Kirin will be excited to have pancakes when she gets home."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karindate20 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label karindate25:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."
    "Given the fact that I am no longer the coach of the soccer team and can no longer hide these impromptu afternoon meetings behind the guise of supervising her training, I decide to just...go for it when she answers."

    play sound "phonebeep.wav"
    play music "notabluearchivesong.mp3" fadein 3.0

    ka "Hello?"
    s "Let’s hang out."
    ka "AHHHH!!!"

    play sound "phonebeep.wav"
    with hpunch

    s "..."

    "Okay. Maybe I “went for it” a little too directly as Karin’s initial reaction was to just hang up."
    "Thankfully, I think I know her well enough at this point to predict that in several seconds, she’s going to call me back and apologize."

    s "..."
    s "..."
    s "..."

    play sound "phonering.mp3"

    "Knew it."

    play sound "phonebeep.wav"

    s "H-"
    ka "I’m so sorry! I don’t know what happened! I just...sometimes I press buttons! It’s a thing that happens!"
    s "Does this mean you’re okay with hanging out, then?"
    ka "AHHHH!!!!!!!!"

    play sound "phonebeep.wav"
    with hpunch

    s "..."

    play sound "phonering.mp3"

    s "..."

    play sound "phonebeep.wav"

    s "H-"
    ka "It happened again!"
    s "Should I proceed with inviting you to do something? Or would you rather we just skip that conversation altogether and decide on a place to meet?"
    ka "I...I’d love to come meet up with you! I just...umm...I’m kind of already doing something, so-"
    mi "{i}Karin, who’s that? And how come ya keep yellin’ at ‘em if ya actually wanna go meet up?{/i}"
    ka "It’s umm...uhh..."
    s "You can tell her, it’s fine."
    ka "It’s...It’s Sensei."
    mi "{i}What the heck? Sensei’s callin’ you? I ain’t gonna have to compete against two of my best friends now, am I?{/i}"
    ka "C...Compete?"
    s "It’s a long story."

    "And one that involves more fingering than I should probably include in a conversation with Karin at this point in time."

    ay "{i}Karin! Tell Sensei I love him! And that my unquenchable desire for him grows stronger every day!{/i}"
    ka "Uhh...Ayane says something about...unquenchable desire?"
    ima "{i}Ask him if he can watch my parrot while I go to the spa tomorrow!{/i}"
    ka "And Miss Imai has a parrot."
    s "I see. "
    s "This has been a very informative phone call. Thank you, Karin."
    ka "I’m...sorry I can’t do anything right now! The girls from the club made plans to put something together for Makoto today because of her dad, so..."
    s "Got it. I’ll be right over."
    ka "Wait, what? "
    s "Yeah. Are all of you at the pool right now?"
    ka "I mean, we are. Yeah. But I can’t imagine you want to spend your weekend on-"
    s "Sounds to me like you’re underestimating just how badly I want to see you."
    ka "AHHHHHHHHH!!!!!!"

    play sound "phonebeep.wav"

    "Karin hangs up again, but I saw it coming this time."
    "Without anything else to do today, I begin making my way over to the school to help with whatever the swim club has decided to “put together” for Makoto."
    "And while the thought of this is something that should hold the head of my day underwater long enough to drown it in a sea of my worries, my desire to stay {i}above{/i} water for now wins out in the end."
    "Because even if there’s one girl suffering beyond the reach of all of us right now, there are plenty more that aren’t."
    "Dragging the broken one back is a task that would prove impossible for just one person, but the efforts of a group will surely be much better in that regard."
    "And being a part of that, even if it’s only for a small amount of time, is sure to help me as well..."
    "........."
    "......"
    "..."

    scene karinmalltrip1
    with dissolve2

    mi "Welcome to the party, Sensei! I’ve only cried one time!"
    s "That sounds like a reasonable improvement from how you’ve been lately, so good for you."
    ima "There’s plenty of pizza if you want any, Senpai. Ayane’s butler did a hell of a job carrying all of it in here in just one trip."
    ay "He cooked it himself as well. If you showed up a few minutes earlier, you might’ve even finally got to meet him."
    ay "Also, do you not love me anymore? "
    s "What?"

    scene karinmalltrip2
    with dissolve

    ay "Oh, nothing. I just figured you would have called me instead of Karin given that she doesn’t even know about the rooftop apocalypse team yet."
    mi "The...what now?"
    ka "Hahahah...I’m sure he just...clicked on my name instead of my sister’s on accident..."
    s "Does it really matter who I called now that I’m spending time with all of you?"
    ay "Yes. Yes, it does."

    scene karinmalltrip3
    with dissolve

    ay "But {i}I guess{/i} I can overlook that since I also understand and appreciate just how wonderful Karin is. "
    ka "I don’t really know what this stuff about being wonderful is, but I’m glad you were able to come by and help."
    s "No need to thank me. I care about Makoto as well and I’m sure that whatever this is will do a lot more for her than I’ve been able to do on my own."
    s "It would be good to know exactly {i}what{/i} you’re putting together, though."
    ka "It’s just a little...care package thing. Cards...gifts...stuff like that. I don’t really know much about Makoto yet, though...so I haven’t been as helpful as I’d like."
    ima "She says, despite being the one to come up with this idea. "

    scene karinmalltrip4
    with dissolve

    ka "Well...when I sprained my ankle playing softball when I was little, the rest of the team did something like this for me and it...really made me feel a lot better."
    ka "Obviously what Makoto is going through is a million times worse than that, but...I still figured it might make her a little happy to get something from all of her friends."
    s "I don’t know if “happiness” is something she’s personally able to feel right now, but I do think she’ll appreciate the gesture."
    s "So, what can I do to help?"
    ima "You can get lost, that’s what."
    s "Wow. Fuck you too, Imani."

    scene karinmalltrip5
    with dissolve

    ima "No, like seriously. We’ve already got a lot of the things we need, but if we’re gonna stick to Karin’s plan and put together the world’s greatest care package, we’re gonna need a bunch of other stuff."
    ima "Plus, the other two girls and I have to go around collecting signatures from all of the {i}other{/i} girls anyway, which is a big ask on its own."
    s "The other {i}two{/i} girls? But there are four of you."
    ima "Yeah. But you and Karin are gonna go out on a date, obviously."

    scene karinmalltrip6
    with dissolve

    ka "D-D-D-D-DATE?!"
    ka "US?! "
    mi "Guh. Startin’ to make sense why Makoto’s always so stressed when it comes to Sensei seein’ other girls."
    ay "So that’s how it’s going to be, Sensei? You take me up on the roof just to leave me for Karin? Has this been your plan all along?"

    scene karinmalltrip7
    with dissolve

    ka "This was never a plan! I didn’t even know Sensei was coming! And I didn’t know I was leaving until thirty seconds ago!"
    mi "That’s just what she wants us to think, Ayane. Karin might look sweet on the outside...but on the inside? She’s just as conniving as the rest of ‘em."
    s "Are you proud of yourself, Imani? Sowing the seeds of destruction in your own club?"
    ima "Hey, my original gameplan before you showed up was to just take everybody to the mall {i}myself{/i} after collecting signatures. You being here just means things are getting easier for me too."
    ima "Plus, this’ll give you and Karin some of that “alone time” I’m sure you called her for and she’s a lot closer to being legal than everybody else you’re always hanging around with."

    scene karinmalltrip8
    with dissolve

    s "..."
    s "Can you all not look away like that?"
    ka "I...I...I guess if...the teacher says we have to go out...there’s...nothing I can do to prevent it!"
    s "You realize I’m a teacher too, right? And that Imani only exists to serve me?"

    scene karinmalltrip9
    with dissolve

    ima "Oof. Not cool, man. Not cool."
    s "What? You-"
    s "Oh."

    scene karinmalltrip10
    with dissolve

    ima "And to think that you were my {i}first.{/i} Does the heart of this fair maiden mean nothing to you?"
    ay "Imani too?! When will it end?!"
    ka "First what? I don’t get it."
    s "Okay, well...at the risk of Imani getting everyone here to turn against me, I suggest we head out. Especially since we apparently have to go all the way to the mall?..."

    scene karinmalltrip11
    with dissolve

    ima "Hey, if you can find everything on Karin’s list elsewhere, feel free. I just figured the mall would be cool  because they have everything."
    ima "It definitely doesn’t have anything to do with my desire to remain forever young and wander the halls with a bunch of high school girls."
    s "Yeah, I’m sure that much was just a complete coincidence. "
    ka "The list isn’t {i}that{/i} long, so...I’m sure we can finish quickly if you hate spending time with me."
    s "Why would I have called you at all if that were the case?"
    ka "Because Karin and Kirin are only one letter apart and...you have bad eyesight?"
    ima "Oh, and speaking of phones, take my number down so we can meet back up once you guys are done."

    scene karinmalltrip12
    with dissolve

    mi "What kinda smooth move is that, Miss Imai?! Just givin’ your number out like it’s a piece of friggin’ candy! Can’t ya see this guy is just gonna use ya as a booty call?!"
    ima "Hey, at least he’ll be saving money. All those carrier pigeons he’s been sending over to my place for analog booty calls are sure to get costly after a while. "
    ay "Sensei has never sent me a booty call pigeon..."
    mi "Pigeons ain’t even real! Birds are a conspiracy created by the government to watch us! Kirin showed me a video all about it!"
    s "Okay, Karin. Come on. We’re leaving before this gets even more ridiculous. "

    scene black
    with dissolve2

    "Imani takes my phone and adds her contact info to it, preparing herself for a lifetime worth of booty calls that I highly doubt would yield any form of success at this point in time."
    "Ayane and Miku go back to sulking as they pack things up and get ready to start soliciting signatures, while Karin and I awkwardly make our way out of the pool room and over to the nearest bus stop..."

    $ imaninumber = True

    "{i}Congratulations! You now have Imani’s phone number!{/i}"

    scene sky
    with dissolve

    "The bus arrives within minutes, sparing us from whatever sort of awkward conversation topics Karin was sure to come up with as we waited."
    "That doesn’t prevent things from still {i}being{/i} awkward, though, as we take our seats on the bus and she has to endure the inner struggle of either sitting {i}next{/i} to me or in the seat across the aisle."
    "Thankfully, she bites the bullet and sits beside me so we don’t have to shout over a row of empty space just to be able to communicate with one another."
    "{i}Less{/i} thankfully, we wind up not communicating at all on the way to the mall, prompting me to believe that I would have preferred even the most awkward of conversation topics over that."
    "Once we’re back on land, though, she opens up again."
    "I guess it’s only the thought of being trapped somewhere with me that eats away at her."
    "But despite my usage of the word “eat,” the form of consumption I’m referring to is not one of negativity."
    "What is being eaten away is that lingering sense of purity of hers and how she is one of the only girls I know at this point who would deny the opportunity to sleep in my bed."
    "For in those moments we are trapped, she is forced to come to terms with things she struggles to understand about herself."
    "And in those moments we are trapped, I must prevent myself from coming to terms with the things I understand about her."

    scene karinmalltrip13
    with dissolve2

    "We find ourselves on a bench I’m known to frequent, but never with her."
    "She sits where the other has, in slightly older yet slightly fresher skin as she looks up at me with a sense of unfamiliar unease deep inside of her emerald eyes."
    "I think about plucking those valuable gems from out of her sockets and pawning them off for one more gift to a girl more tainted than she is."
    "For it is those who feel the darkness creeping in that deserve the most-"
    "And it is those who have not yet been touched by it who must be left alone."

    ka "So...umm..."
    ka "I...guess I wasn’t busy after all?"
    s "In all fairness, it’s not like this is a particularly {i}happy{/i} outing. We’re shopping for a girl who lost her dad."

    scene karinmalltrip14
    with dissolve

    ka "Yeah..."
    ka "I wish there was something more we could do."
    s "I think what we’re doing now is plenty. Makoto seems like she wants to grieve in silence for the most part. So as long as she knows we’ll be here whenever she comes out of her cave, she’ll probably be fine."

    scene karinmalltrip15
    with dissolve

    s "Or not."
    s "Death is complicated."
    s "To some people, it’s like the world is falling apart. But to some others, it’s like nothing’s really changed at all."
    ka "What...is it like for you, Sensei?"
    ka "If that’s...something you’re okay with me asking."
    s "I’m more interested in hearing what it’s like for you, if you’re okay with {i}me{/i} asking."

    scene karinmalltrip16
    with dissolve

    ka "Unfortunately...that’s not really an easy question for me {i}to{/i} answer."
    ka "I’m kind of...terrified of it, really."
    ka "I don’t have any...{i}experience{/i} with death yet."
    ka "Well, other than my goldfish Benjamin who died when I was six years old. But I haven’t really thought about him again until right now and oh my God I am suddenly sad."
    s "Yeah. I think that’s kind of just...how it’s supposed to work after a while."
    s "Unfortunately, it’s not..."
    s "..."

    scene karinmalltrip17
    with dissolve

    ka "Sensei?"
    s "Unfortunately, it’s not like that for everyone. And we all have our own ways of facing it."
    s "I’m sure you’ll come to experience it someday. And I’m sure that, when you do, you’ll learn things about yourself that you’ve always feared learning."
    s "But I don’t think it’s something you should let suppress you. If you live in fear, you’ll miss out on a lot of the better parts of life."
    s "And while there aren’t many of those when you’re as jaded and cynical as I am, they still exist."

    scene karinmalltrip18
    with dissolve

    ka "Yeah...you’re probably right."
    ka "It just feels horrible not understanding what other people are going through because it’s like I can’t...help them as much as they need me to."
    ka "So sometimes I wish I {i}did{/i} understand. But I know that wishing that means something horrible would have to happen to me and..."
    ka "I guess I’m a little selfish in that sort of way."
    s "If your idea of selfishness is not wanting someone you love to die, I think you’re a lot more selfless than you believe."
    ka "..."
    s "..."
    ka "Umm..."
    ka "There are...other ways I’m selfish, you know..."

    scene karinmalltrip19
    with dissolve

    ka "Ways that are a lot less depressing and-"
    ki "Uhh...what the actual fuck is going on right now?"

    scene karinmalltrip20
    with dissolve

    ka "K...Kirin?"
    n "And Noriko! I am also here. Hi, Sensei."
    s "Hey. What are you two up to?"
    ki "Isn’t that what we should be asking you?"

    scene karinmalltrip21
    with fade

    "Karin gets off of the bench and marches over to Kirin with a look of determination I seldom see from her in situations like these."
    "It’s no joke to say she normally takes the backseat when dealing with her sister, but it seems that something about today’s {i}circumstances{/i} have made that very much not the case."

    ka "Is there a problem, Kirin?"
    ki "Problem? No. I’m just surprised to see a prude like you out and about with an older man."
    ka "You know that a girl and a b...{i}boy{/i} can go out in public without being like that, right?"
    s "I prefer “man,” but please, proceed."
    ki "Of course {i}I{/i} know that. But does Sensei know that?"
    ka "Do you think we’re on a date or something? Is that why you’re so jealous right now?"
    s "I mean...Imani {i}did{/i} say that-"

    scene karinmalltrip22
    with dissolve

    ki "Jealous? You think I’m {i}jealous?{/i} Of what?"
    ki "Just because there’s {i}one{/i} guy in your life that you can talk to without pissing yourself now doesn’t mean I’m suddenly going to be {i}jealous.{/i}"
    ki "But hey, if you want to keep enjoying your {i}date,{/i} go ahead. Noriko and I are going to go buy new underwear."
    n "We are? I thought we were going to the mov-"
    ki "Shut up, Noriko."
    ka "You want to know why we’re really here, Kirin?"
    ki "Yeah, sure. I’d {i}love{/i} to hear what sort of thing could get my sister out of the house and into the company of some fucking dinosaur."
    s "That was unnecessary."
    n "I agree. That was unnecessary. Sensei is in the prime of his life and you of all people should-"
    ki "Shut the {i}fuck{/i} up, Noriko."
    ka "Fine. Since you want to know, I’ll tell you."
    ka "Sensei and I are here to buy presents for Makoto. Who, in case you happened to forget, just lost her dad."

    scene karinmalltrip23
    with dissolve

    n "Hah..."
    ka "Yeah. Bet you feel like a jerk now, don’t you?"
    ki "That..."
    ki "Uhh..."

    scene karinmalltrip24
    with dissolve

    ki "Well, how was I supposed to know that?! There’s no way anyone would guess that on the first try!"
    n "Can we go to the movies now? I don’t like it when I have to skip the previews and you’re always making us show up late."
    ka "Apologize."
    ki "For what?! Assuming you two were {i}together?!{/i} Why are you even offended by that?!"
    ka "I’m not asking you to apologize to me. I’m asking you to apologize to Sensei for assuming he’d ever look at me that way."

    scene karinmalltrip25
    with dissolve

    n "I mean..."
    ki "Don’t fucking hit on my sister, Noriko."
    n "I’m not saying I {i}wouldn’t...{/i}"
    ki "Noriko-"

    scene karinmalltrip26
    with dissolve

    n "You say weird stuff about my sister like fifteen times a day! How is this fair?!"
    ki "Shut up! We’re leaving!"

    scene karinmalltrip27
    with dissolve

    n "Fine. Let me just tell Sensei I love him a few thousand times first. I love you. I love you. I-"
    s "Now’s probably not the best time, Noriko."

    scene karinmalltrip28
    with dissolve

    n "Just thought I’d remind you. That’s all."
    n "Is there anything you still need for Makoto? Kirin and I can pick something up after the movie."
    ka "Are you sure? Because the only things left are a little on the pricey side and-"
    n "It’s fine. Don’t even worry about it. Just tell us what to get and we’ll help out in any way we can."

    scene black
    with dissolve2

    "Karin returns to the bench to grab her list out of her bag and rattles off the names of different items in her Makoto Miyamura condolence care package."
    "Among them are a series of books that Miku and Maki compiled into a list, several packages of assorted fancy fruits, skin care products, and other things of that nature."
    "Kirin and Noriko note everything down in their phones before leaving the two of us alone and, knowing that they’ll be getting at least the skin care stuff, our trip is significantly shortened."
    "We leave the mall to meet back up with Imani and the others and, within the hour, I am removed from the group."
    "This time, however, I’m not paired with an attractive girl to spend the rest of the day with and am forced to go home alone to drown in my thoughts."
    "Among those thoughts are several visions of emerald eyes."
    "And how my desire to pluck them becomes greater each time they appear."

    $ renpy.end_replay()
    $ karindate25 = True
    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label karindate30:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."
    "If she’s putting together another care package for someone this time though, I’ll probably just sit things out."

    if makotolust30 == True:
        "As much as I liked being able to help Makoto in a way that wasn’t being borderline raped by her, I really {i}do{/i} want to spend more time with Karin alone."
    else:
        "As much as I liked being able to help Makoto in a way that was actually conducive to caring rather than showing up and destroying a picture of her father, I really {i}do{/i} want to spend more time with Karin alone."

    "Also, I want to see if I can make her hang up the phone even faster this time."

    play sound "phonebeep.wav"

    ka "Hello? "

    play music "lifeismostlygood.mp3"

    s "Let’s go on a date."
    ka "PFFT!?!:!$$$$$?~!?~??~!!!!???)*)*)&&"
    s "Wow. You’re still on the line. Good job, Karin."
    ka "W-W-W-W-W-What did you just say?!"
    s "Let’s go on a date."
    ka "Together?!"
    s "No. Let’s go on two separate dates in different locations and then tell each other about them later."
    ka "Oh. Oh, okay. "
    ka "But, wait- I don’t know any other boys. Er...uhh...{i}men.{/i}"
    s "Good. Because I was just kidding when I said that and I do think that we should go on a date {i}together.{/i}"
    ka "UTHRIURHGUIHEIFUWEUIY#)(*$*$!!!!!!!!!!!"
    s "Yeah, I’m excited too."

    if karinlied == True:
        ka "But I...you know...words!"
    else:
        ka "But...wait. I thought you were interested in Kirin?..."
        ka "You didn’t mean to call her again, did you?"
        s "Karin, I’ve never accidentally called you while trying to talk to her. And who says I can’t be “interested” in more than one person?"
        ka "Are you..."
        ka "Wait! Does that mean what I think it means?! Because that sounded a lot like a thing I didn’t think you meant but now I think you might actually mean!"
        s "Well, there’s only one way to find out and it involves meeting up with me as soon as possible."
        ka "But I wouldn’t even know what to wear and-"

    s "Cool. I’ll send you an address. Meet me there in about an hour."
    ka "Wait! Sensei! I-"

    play sound "phonebeep.wav"

    "I hang up the phone after successfully inviting Karin out on a date."
    "And while I’m sure it will be less of a traditional “date” and more of an excuse for me to ogle at her surprisingly developed (And mildly intimidating) body for a few hours, I figure she’ll still have a good time."
    "With each passing day, my certainty of her interest in {i}me{/i} increases."
    "So as she begins to open herself up like a clam in search of salt, I disintegrate into trillions of molecules and spread myself out on the large wooden table in her family’s dining room."
    "Before long, I will feel her tongue."
    "Before long, she will taste the salt."

    scene karinurbandate1
    with dissolve2
    play sound "phonebeep.wav"

    ka "A...date..."
    ka "I’m going on...an actual date..."
    ki "Congrats. Don’t forget to pack condoms."

    scene karinurbandate2
    with hpunch

    ka "AH!"
    ki "Jesus. Overreact much? They’re basically just weird shaped balloons once you take away the dick."

    scene karinurbandate3
    with dissolve

    ka "Why do you know so much about...c...condoms?"
    ki "Uhh...because I’m not five?"
    ki "You gonna tell me who that was? Or am I just going to have to stalk your Instagram to see which girl’s been hitting on you this time?"

    scene karinurbandate4
    with dissolve

    ka "It wasn’t a girl, Kirin. I wouldn’t have agreed to a “date” if it was."
    ki "Stop saying “date” like it’s some sort of foreign concept. It’s completely normal for a guy and girl to go out on a date and not even-"

    if karinlied == False:
        scene karinurbandate5
        with dissolve

        ki "Wait! Are you going on a date with fucking {i}Sensei?{/i}"
        ka "Would it be a problem if I was?..."
        ki "Yes! He’s {i}my{/i} fucking teacher! Find your own adult to suck off if you’re that curious about men all of a sudden."

        scene karinurbandate6
        with dissolve

        ka "J...Just because he’s interested in you doesn’t mean that I can’t talk to him too! "
        ka "There will be no s...sucking! We’re just going to spend time together and talk! Like friends, but...he’s a lot older and I’m...not fun!"
        ki "Well...good! Because he’s mine and I won’t let you take {i}him{/i} from me too!"
        ki "Also, what is this about him being interested in me?! Please explain it to me in vivid detail!"

        scene karinurbandate7
        with dissolve

        ka "Ask him yourself. I have to go get ready for my {i}date.{/i}"
        ki "Maybe I will. And good luck {i}getting ready-{/i} whatever the fuck that means. I can’t even {i}remember{/i} the last time you put on makeup."
        ka "Maybe I’m just...more confident in my face than...you are in yours? Jerk."

        scene karinurbandate8
        with dissolve

        ki "Our faces aren’t even that different!"
        ki "Let me go instead! I’m not doing anything today! And the fact that my older sister is going to be out with {i}my{/i} man just doesn’t fucking sit well with me!"
        ka "If he’s {i}your{/i} man, I guess you won’t have anything to worry about."
        ka "Also, Mom says it’s your turn to vacuum the house. So you {i}will{/i} have something to do today."

        scene karinurbandate9
        with dissolve

        ki "Are you fucking kidding me?!"
        ki "Since when do you just walk away when I’m arguing with you?! I’m the one who’s supposed to walk away!"
        ka "Can’t hear you! Trying to...find a good makeup tutorial!"

        scene karinurbandate10
        with dissolve

        ki "That better not be my Youtube you’re logged into, you bitch! You’ll fuck my algorithm!"

    else:
        scene karinurbandate11
        with dissolve

        ki "Wait. Are you going on a date with fucking {i}Sensei?{/i} My teacher?"
        ka "I’m sorry Kirin, but I’m not the type to kiss and tell."
        ki "You’re not the type to kiss at all."
        ka "Yeah. Even saying that made me want to curl up into a ball and throw myself out of the window."

        scene karinurbandate12
        with dissolve

        ki "Well, then why the fuck are you going out on a date with a guy?! Let alone {i}that{/i} guy?!"
        ki "How do you expect things to go when he wants more than you’re willing to give?!"
        ka "I have no idea what {i}things{/i} you think Sensei expects from me, but he’s been nothing but kind to me so far and has never once tried to force me out of my comfort zone."
        ka "I think that’s...probably why I was able to say yes just now. With anyone else, I’m sure I would have just...you know, {i}actually{/i} thrown myself out of the window."

        scene karinurbandate13
        with dissolve

        ki "Can...Can I go instead?"
        ka "Instead?..."
        ki "Yeah. Like, you can...call out sick or something."
        ka "I am no expert, but I don’t think dates work that way. And besides, I..."
        ka "I {i}want{/i} to go..."
        ki "Since when do you have literally {i}any{/i} interest in boys, though? "

        scene karinurbandate14
        with dissolve

        ka "It’s less an interest in boys and...more an interest in {i}him...{/i}I think."
        ka "I don’t know. My feelings are kind of all over the place right now...and it sounds hard to believe, but my heart is currently beating a billion times faster than it ever did during soccer."
        ka "Besides, I...I’m sure he was only using the word “date” to mess with me. It’s not like Sensei would ever actually {i}want{/i} to date me, you know? Our parents wouldn’t ever allow it either."

        scene karinurbandate15
        with dissolve

        ki "I’m sure they’d make an exception for {i}you{/i} as long as you asked."
        ka "Kirin...can you maybe try to be happy that {i}I{/i} am really happy right now? Because that would mean a lot to me."
        ki "..."
        ka "..."
        ka "Okay."
        ka "Well, I’m going to go get ready. But Mom told me to tell you it’s your turn to vacuum the house."
        ki "Yeah, of course she did. "

        scene karinurbandate10
        with dissolve

        ka "Can you help me with my makeup? I have no idea what I’m doing."
        ki "Just watch a fucking Youtube video or something."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene karinurbandate16
    with dissolve2

    ka "Umm...h...hello..."
    s "Woah."

    scene karinurbandate17
    with dissolve

    ka "It doesn’t suit me, does it?"
    s "It suits you fine. Maybe a little {i}too{/i} fine- which is an added benefit for me since now the chances of you being mistaken for a high school student have been all but eliminated."
    ka "But...But I {i}am{/i} a high school student."
    s "Not while we’re in public, you’re not."

    scene karinurbandate18
    with dissolve

    ka "I think I can...probably remember that..."
    ka "I didn’t keep you waiting too long, did I? I didn’t really expect to have to come all the way over to the urban district, so...I might’ve left a little later than I probably should have."
    s "It’s no big deal. I figured there was a decent chance that you were going to chicken out and send Kirin in your place or something anyway."

    if karinlied == False:
        scene karinurbandate19
        with dissolve

        ka "Would you...have preferred that?"
        s "Why would I personally invite you if it was your sister I was after?"
        ka "I don’t know...this is all just so crazy and...sudden..."
        ka "Kind of like a...a...dream..."

        scene karinurbandate20
        with dissolve

        ka "Oh God! This {i}is{/i} a dream, isn’t it?! This whole day has been a dream and I am going to wake up in five minutes and still have no idea how to tie the ribbon thing on my dress!"
        s "Or...that’s not going to happen and we’re going to spend the rest of the afternoon hanging out together."
        ka "That sounds exactly like what dream-Sensei would say!"
        s "You sound pretty familiar with this “dream-Sensei” guy."
        ka "You should know because you are him!"
        s "Karin, it’s really me. Like, the {i}real life{/i} me."
        ka "I don’t know if I can believe you."

        scene black
        with dissolve

        s "Okay. I guess I’ll just leave, then."
        ka "Wait! I believe you now! Don’t leave me here alone! What if someone hits on me?! I’m not prepared for that!"

    else:
        scene karinurbandate21
        with dissolve

        ka "She actually...tried to come in my place and...I thought about letting her, but..."
        ka "I was...a little too excited..."
        ka "I’ve never really...gone out with anyone like this before..."
        s "Well, I’m glad you didn’t let her come because this is the exact side of you I’ve been hoping to see for a long while now."

        scene karinurbandate22
        with dissolve

        ka "Stop..."
        s "I’m serious. I’ve always thought you-"
        ka "No, like...really stop...I think I’m about to have a heart attack..."
        s "With all the cardio you do? Doubt it. Just accept my compliments and tell me I look handsome as well or something so we can get this show on the road."

        scene karinurbandate23
        with dissolve

        ka "You look..."
        ka "You..."
        ka "..."
        s "..."
        ka "Tall."

        scene black
        with dissolve

        s "Close enough. Good job, Karin. "
        ka "Wait! Sensei, where are you going?! I don’t even know what the plan is yet!"

    "I walk off in the direction opposite where Karin came from, but not because I have a specific location in mind."
    "Is inviting someone out on a date despite not having a concrete plan of what to do if they accept a little unorthodox? I guess. "
    "But, honestly? With the way Karin looks right now, I kind of {i}want{/i} to be seen in public with her rather than spend the afternoon inside of a dimly lit movie theater or something."
    "Who knows? Maybe we’ll find a park or something and I can nod my head at all of the other women who walk by and stare at us for reasons that I’m sure are more complicated than me actually having a penis."
    "Those are pretty rare around here nowadays. "
    "But I digress."

    scene karinurbandate25
    with dissolve

    "Karin quickly catches up to me and takes her place by my side, leaving a little less space between us than I expected from her."
    "It is in this moment that I decide to let her in on the fact that I do not have a plan for this outing so that she doesn’t wind up getting depressed when we start walking around in circles."

    s "Karin, I have bad news for you."
    ka "I knew it. You {i}did{/i} want Kirin to come instead of me, didn’t you?"
    s "Stop saying that. I was just going to tell you that this is about to be the most boring date of your life because, despite being notoriously bad at making plans, I continue to do just that for reasons I don’t understand."
    ka "Oh, that’s okay. It’s also the most exciting date of my life, so you can be happy knowing that the bar is impossibly low. "
    s "I have never been happier to hear those words."

    scene karinurbandate24
    with dissolve

    ka "And I don’t think I’ve...ever been happier to be invited out before..."
    s "..."
    ka "..."
    s "Please, proceed. I want to hear more about how awesome you think I am."
    ka "Well, it’s just...you know..."
    ka "Ever since the soccer team disbanded and you stopped being our coach, I’ve been seeing you less and less while my sister still gets to see you all the time..."
    ka "So whenever she talks about you, I...start to kind of miss you, I guess..."
    ka "I miss you randomly showing up to practice and...watching over all of us to make sure we don’t get hurt."
    s "Yup. That is exactly why I was watching all of you. Good catch."

    scene karinurbandate25
    with dissolve

    ka "That was probably weird, right? Hearing that I...you know...missed you?"
    s "Not really since you’re already falling in love with me."

    scene karinurbandate26
    with dissolve

    ka "L-"
    s "Okay, maybe not {i}love-{/i} but you definitely feel something, don’t you?"
    s "I can’t really imagine you “missing” me without that being the case."

    scene karinurbandate27
    with dissolve

    ka "Well, it’s...true that I did miss you...but I don’t know if there are any...uhh...what do you call them?"
    s "Feelings?..."
    ka "Yeah! I don’t know if there are any {i}feelings{/i} involved in that! "
    ka "I just got so used to you being around that...once you stopped being around as much, I started to get sad and want to see you more."
    s "Yeah. So, to hearken back to what I was just saying, you like me."

    scene karinurbandate28
    with dissolve

    ka "S-S-S-S-S-S-S-STOP SAYING THAT! HOW ARE YOU NOT EMBARRASSED?!"
    s "Because it’s not a big deal. I literally invited you out already knowing this about you."

    scene karinurbandate29
    with dissolve

    ka "How do you know things about me before even I do?!"
    s "Because I understand this subject a lot better than you do. And that’s totally fine. Move at your own pace or whatever and I’ll just...try to match it."

    scene karinurbandate30
    with dissolve

    ka "If...that really {i}is{/i} what it is, though...isn’t that {i}bad?{/i}"
    ka "Would it even be okay for me to feel things like that for you?..."
    s "I don’t think there are any feelings that are just naturally {i}bad{/i} unless you’re the type of person to act on them. But even then, {i}this{/i} feeling wouldn’t ever be on the bad side."
    ka "I’m sorry, I just...I’m having a really hard time wrapping my head around why you’d say that."
    s "What don’t you understand?"
    ka "Just...you know..."
    ka "Don’t you see me as a kid in your eyes?"

    if karinlied == True:
        s "Didn't we already talk about this when you made sushi a while ago? I don't see you that way at all."
        ka "Yeah, but..."
        ka "You could be lying..."

    s "I literally asked you out on a date today."
    ka "Yeah, but...you can go on dates like this without wanting anything out of them, can’t you?"

    if karinlied == False:
        s "I’ve also confirmed my interest in your sister who is both younger {i}and{/i} smaller than you."

        scene karinurbandate31
        with dissolve

        ka "Don’t bring her up anymore. This is {i}my{/i} date."
        s "Sorry. Please continue."

        scene karinurbandate30
        with dissolve

    ka "I don’t know...I have this problem where I overthink a lot and every time I remember who you are and who {i}I{/i} am, I start to feel like this is all going to fall apart and that’s...really scary."
    ka "At least if things fell apart now, it’s not like the damage would be really bad. And I still have no idea what I’m doing when it comes to...uhh...{i}co-educational{/i} relationships..."
    s "Just “relationships” is fine."
    ka "Yeah. That. Me not knowing what I’m doing makes me feel like I’m just going to, like...knock everything over and cause a huge mess."
    ka "And I just don’t really want to make a mess like that in front of you or...do anything that will prevent you from wanting to see me anymore."
    ka "Which is why I probably {i}do{/i} feel the way you said I feel but it’s not like I can {i}tell{/i} you I feel that way because then I'll know that I {i}do{/i} feel that way and that feels scary."
    s "Well, it’s clear that your brain is already going in circles right now, so these words might not sound like anything important to you, but-"
    s "You have nothing to be afraid of."

    scene karinurbandate32
    with dissolve

    ka "And...you really don’t see me as a kid?"
    s "To be honest, I don’t think many people do. You both look and {i}act{/i} much older than you are, which is really all that matters to me."

    "(It doesn’t.)"

    ka "Thanks, Sensei..."
    ka "I do have one question, though."
    s "Sure. You can ask me anything."
    ka "Okay...so..."
    ka "Don’t get mad, but..."
    ka "Can we maybe...{i}not{/i} walk in circles for the rest of our date?"
    ka "I’m getting really hungry..."

    scene black
    with dissolve2

    "Karin and I spend the rest of our afternoon inside of various air-conditioned buildings so she can refill her energy stores and keep herself from sweating- a thing she is apparently very concerned about today."
    "And while I did initially claim that I wanted to remain in public and nod at other women or whatever, the heat forces me to once again act in opposition to myself as I, too, change stances."
    "Fortunately, every building we walked into, from patisserie to pop-up shop, was packed with people."
    "And I found myself, more often than not, actually thinking of Karin as my girlfriend rather than a pure soul who just keeps wandering into the wrong places at the wrong times."
    "We enjoy our day together."
    "I replay it in my head as I collapse onto my mattress and remove my belt."

    $ renpy.end_replay()
    $ karindate30 = True
    $ karin_love += 5
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
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

label karinspring1:
    scene karinslife1
    with dissolve2
    play music "fallishere.mp3"

    "Hi! I’m Karin Kanda — a second year student at Kumon-mi High!"

    ka "Wow! What a beautiful day!"

    "If I had to describe myself with one word, it would probably be “sunshine,” because I always try to look on the bright side!"
    "Life’s too short to let your worries drag you down, which is why I always try to keep a positive attitude while helping others do the same thing as well!"
    "Today, I’ve decided to walk to school. "
    "I live a little further away than most of the other girls, so I have to take the bus sometimes. But the weather is so perfect today that I figure it’s as good a chance as any to get some exercise in!"

    scene karinslife2
    with dissolve

    ka "Oh, shoot! Today is Ms. Sato’s birthday. I almost forgot! I should stop and buy her flowers on the way to school."

    "Staying healthy is important, you know! A healthy body paves the way to a healthy mind! Or...wait. Maybe it was the other way around?"
    "I don’t know. I’ll have to ask my mom again. That’s {i}her{/i} catch-phrase after all. But there’s one thing I know for sure, and it’s that I wouldn’t be where I am today without her guidance."
    "I’m but the sum of all the good things the people I love have done for me, of course! And today is one more chance to spread some of that love around and help someone else in need!"

    scene black
    with dissolve2

    ka "Come on, feet! We’ve got some walking to do!"

    scene karinslife3
    with dissolve2

    "After stopping at the local florist to buy my teacher, Ms. Sato, a bouquet of her favorite flowers (posies — I remember because they’re my favorite flower as well!), I sit down at my desk and prepare for my lessons!"
    "Today, I have an English test. And while it’s not my favorite subject (I have a soft spot for home-ec), I still find it very interesting!"
    "It’s amazing how there are so many different cultures out there, and how that’s often reflected in the way a language develops."

    seco1 "Karin! I forgot my pencil! Can you lend me one again?"

    scene karinslife4
    with dissolve

    ka "Of course! You can just grab one out of my bag. I packed extras in case you forgot again."
    seco1 "Ahh! You’re such a lifesaver! Thank you so much!"

    "The girl who sits next to me is named Rena! I’ve known her since elementary school, and she’s always been a little forgetful. So I try to keep an eye out for her!"
    "I don’t mind at all. I’ve been an older sister for practically my entire life, so it’s sort of just second-nature at this point for me to always be prepared for anything."

    scene karinslife3
    with dissolve

    "Like today’s English test, for example! There are a lot of really hard questions on here, but I’ve been studying extra hard over the last week so none of them would surprise me."
    "It’s reasons like that that keep me near the top of my class when it comes to grades!"

    seco2 "Psst. Karin."

    "But that comes with its own set of difficulties as well."

    scene karinslife5
    with dissolve

    ka "What’s wrong, Ayumi? Do you need a pencil as well?"
    seco2 "Do you have the answer to number seven?"

    scene karinslife6
    with dissolve

    ka "Of course I do. But I’ve told you before, I will not help you cheat. And I gave you plenty of opportunities to join my study group, so you can’t say I didn’t try to help."
    seco2 "Ughhhhh but studying is so hard!"
    ka "It’s only hard because you don’t apply yourself. But I know you’re better than that, so-"
    sato "Kanda."

    scene karinslife7
    with hpunch

    ka "Ah! I’m sorry, Ms. Sato! I’ll be quiet!"

    scene black
    with dissolve2

    "No life is without difficulties, though! And I should be glad that mine are so simple and tiny when compared to the troubles many other people face."

    scene karinslife8
    with dissolve2

    "After school ends, I always try to help out some of the clubs before heading home."

    seco3 "Pleeeeeease, Karin?! The volleyball club needs you!"
    ka "I’ll help out when I can, I promise! But I’m only allowed to be in two clubs at once, and I’ve already settled on softball and swimming."
    seco4 "What about basketball, then?! You’d be an amazing center! We’d make it to nationals easily!"

    scene karinslife9
    with dissolve

    ka "Nice try, Ena! But we all know nationals haven’t existed since the barrier was put up."

    "I guess I’d be called “popular” by most accounts, but that hasn’t ever really mattered to me."
    "As far as I’m concerned, popularity is sort of a...realistic result to simply being a good person!"
    "If you do your best to make others happy, you’ll find that, more often than not, happy things will start happy-ning to you! Haha! Get it?"
    "In Buddhism, we call that karma. Or “what goes around comes around!” Or, as we learned in English recently, {i}the golden rule.{/i}"
    "But basically, the reason you’re seeing me swarmed by all of these girls is because they like me. And I like them! I like everybody! Which means I must be doing something right. Right?"

    scene black
    with dissolve2

    "Right?"

    scene karinslife10
    with dissolve2

    "On the way home from school, I make sure to spend at least thirty minutes every day helping the elderly across a crowded intersection."
    "My sister, Kirin, tells me this makes me “extra,” but what I think she means to say is “extra nice.”"

    ka "There’s no need to hurry, Mrs. Okazaki. I’m not going anywhere. I can help you the whole way home if you need me to."
    elder "Thank you, dear...You’re always so kind to me...Your parents must have raised you well..."
    ka "Oh, stop. I’m sure anyone else would do the same."
    elder "That’s not true at all, dear...most young folks don’t respect their elders the way they used to...you’re one of the good ones..."
    elder "Back in my day...we- ackh! Hck...nnph...ck!"

    scene karinslife11
    with dissolve

    ka "Are you alright?! Do you need to take a break?! Should I call an ambulance?!"
    elder "Mmfh...mmf...no, dear...just my age...catching up to me..."

    "Mrs. Okazaki can’t talk or move as well as she used to."
    "A few months ago, her husband of fifty-five years passed away. And I think it’s taken a toll on her heart."
    "Poor thing...I can only imagine what that must be like. But I try not to because, not only does it makes my hands sweat, but my heart starts going dadadada at the thought of ever finding {i}anyone{/i} like that."
    "There is {i}one{/i} person I have in mind, but...no. No, that’s crazy. And I shouldn’t be thinking about things like that anyway since I’m still in high school and...wait, what were we-"

    scene karinslife12
    with hpunch

    ka "Right! Mrs. Okazaki!"
    elder "Hm?...What about me, dear?..."

    scene karinslife13
    with dissolve

    ka "Oh! Nothing, sorry. It’s just...my mind was wandering."
    ka "Are you really okay, though? You don’t need me to call you a ride? Because I will. I have an emergency fund for little stuff like this and there’s no better way to spend it than-"
    elder "Don’t go wasting your hard-earned money...on an old bag like me...put it in a box under your bed...and spend it on a wedding one day..."
    ka "A wedding? Me? Marriage? Husband? Me? Noooo. Me?"
    elder "Heh...heh...heh...yes you..."
    elder "You remind me...a lot of myself...back when I still...had hair like yours..."
    elder "I was...a real beauty, you know..."

    scene karinslife14
    with dissolve

    ka "And you still are. There aren’t many people out there who could pull off grey the way you do, Mrs. Okazaki. I really mean that."
    elder "Heh...heh...heh...you flatter me...as always..."

    scene black
    with dissolve2

    elder "You’re going to make...some man very happy one day, Karin..."
    ka "Heheh...oh, stop..."

    scene karinslife15
    with dissolve2

    "My last stop before heading back home is the local grocery store!"
    "My parents work late, so I wind up making dinner for the entire family a few nights every week."
    "My sister, Kirin again, isn’t always home to eat with us. But I still try to buy all of her favorite ingredients in case she {i}does{/i} decide to show up."
    "Oh, and I only buy local products! It’s important to support your hometown’s economy, you know!"
    "Kumon-mi might be sectioned off from the rest of the world, but we still get a lot of imported goods. Especially in places like this."
    "But it’s because of people like me, who love the town so much, that our city is still thriving despite all that’s happened!"
    "Or, at least I like to {i}think{/i} that’s the reason. I’m sure the economy is a lot more complicated than that, but they haven’t taught us much about that in any of my classes yet."
    "I’m excited to learn, though! There’s so much about the world that I still don’t understand!"
    "Like, what are those little plastic things at the end of shoelaces called? Or what breeds of dog are hypoallergenic?"
    "I’m sure there are a lot of questions you don’t know the answer to either. But that’s okay! We can figure them out together."
    "Because the only way to make this world a better place is to work as a team — and that’s why you’ll find me playing sports so often."
    "I’d do {i}anything{/i} for {i}anyone.{/i}"

    scene black
    with dissolve2

    "My sister, Kirin again, says that makes me a pushover."
    "And you know, maybe she’s right?"
    "I’ll be the first to admit that I’m not perfect, despite what a lot of my classmates would tell you about me."
    "I still cry sometimes. I still think about sad stuff."
    "But I do my best to keep it together because I want to be a good influence on everyone around me!"

    play sound "dooropen.mp3"
    scene karinslife16
    with dissolve2

    ka "I’m home!"

    "That comes with its own share of difficulties as well, though."

    stop music
    play sound "static.mp3"
    scene karinslife17 with flash
    stop sound

    ki "What’s for dinner?"
    ka "Oh, Kirin! You’re here! That’s great! I was actually thinking of making potato leek soup and-"
    ki "Pass. I’ll just eat at the dorm."
    ka "But-"

    scene karinslife18
    with dissolve

    ki "Oh, and I ate your pudding. Sorry."

    play sound "static.mp3"
    scene karinslife19 with flash
    stop sound

    ka "..."
    ka "That’s okay."
    ka "I didn’t want it anyway."

    "I don’t think my sister likes me very much."
    "And that makes me very sad."
    "She’s been my best friend ever since she was born. But it feels like, most of the time, she wants to be an only child."
    "Most of the time, it feels like she wishes I would just die."
    "I try my best to understand her, but it never really works out."
    "I try to do nice things for her. But, most of the time, she tells me I’m being annoying."
    "Or that I’m only doing these things to show off."
    "But that’s not true at all."
    "In fact, it’s {i}because{/i} of her that I am the way I am."
    "I want to set a good example."
    "I want her to see that there’s more to life than whatever she sees right now."
    "And I know that being a teenager is hard."
    "I know that it can cloud your vision."
    "But I don’t think she knows that I know that."
    "And it makes me feel like I know nothing at all."

    ki "..."
    ka "..."
    ki "Why are you just staring at me like that?"

    "I love my sister."

    ka "No reason..."

    scene black

    "I just wish she loved me too."

    $ renpy.end_replay()
    $ karinspring1 = True

    scene karinslife20
    $ renpy.pause(5, hard=True)
    scene black
    $ renpy.pause(2, hard=True)

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label karinspring2:
    play music "strawberry.mp3"
    scene lolwerebackagainlol1
    with dissolve2

    s "Guys, I don’t want to be here."
    mi "Nonsense, Sensei! Just ‘cause you’re embarrassed to sing don’t mean ya gotta worry in front’a two of your best friends in the whole world."
    ka "That’s right, Sensei! I’m not a very good singer either, but if you won’t judge me, I won’t judge you!"
    ka "In fact, even if you did judge me, I probably wouldn’t judge you- because judging people is rude when you can never truly understand what’s going on inside of a person."

    "{i}Right now, there are a lot of things going on inside me.{/i}"
    "{i}For one, the pizza I ate earlier is being broken down into enzymes by the factory workers I swallowed when I was a child.{/i}"
    "{i}And the railway workers who control my vascular system are currently pulling levers and moving tracks around so more blood gets sent down to my penis to make it hard.{/i}"
    "STOP."
    "{i}But I don’t want a penis because I’m a little baby bitch boy who believes in CONSENT but conveniently forgets every single day just who can do that and who can’t. Right, buddy?{/i}"
    "STOP."
    "{i}Take it out and smack them with it! Show these ladies a good time before I have to do it for you!{/i}"

    scene lolwerebackagainlol2
    with dissolve

    s "I have to leave now."
    mi "Ain’t no leavin’ now that we’re here, Sensei! Ya gotta stay for at least one song. Them’s are the rules of Karaoke-town. Conveniently located right next to Bonerville."

    "{i}Those towns are a lot closer than she thinks LOL{/i}"
    "I don’t want to-"
    "{i}Waaaaaaaaaaaaaaaaaaaaaaaaaah! That’s what you sound like right now. Pussy. Baby-back bitch. Just give in and listen to the MUSIC, frog boy! You love this song! It reminds you of the-{/i}"
    "{i}The fuckin’...what’s her name again? Mayonnaise Macaroni? The closet nympho who ISN’T related to Sara.{/i}"
    "How do you know Sara?"
    "{i}I know everybody. But I only remember my favorites. Like her and the, uhh...wait, no. You guys never met. But hey, what are you talking to me for? It’s time to sing, bitch.{/i}"

    ka "Is something wrong, Sensei?"
    s "{s}Yes.{/s} No, I’m okay. I just get nervous easily."

    "I attempt to pull myself away from the girls but can’t bring myself to move my limbs. "
    "{i}Naaaaah, you just don’t want to leave. Stop blaming this on me. Fuck ‘em. Win the “game.”{/i}"

    mi "How ‘bout I go first then? I ain’t much of a singer either. Chances are you’ll feel way better ‘bout all this after I get a turn. Right, Sensei?"
    s "{s}Help.{/s} Yeah, that sounds good to me. Lead the way, Miku."

    play sound "static.mp3"
    scene lolwerebackagainlol3 with flash
    stop sound

    "{i}We make our way back into the karaoke booth where the best chapter started. It’s chapter four and it’s home to the supreme leader, Hyphen-Knight.{/i}"
    "{i}Hyphen-Knight is super cool and always makes me do the right thing. Right, buddybug?{/i}"

    s "{s}I NEED TO LEAVE.{/s} Sorry for acting weird before, you two. I just haven’t done anything like this since I was young and I’m...not sure if I even remember how."
    mi "Hm? Thought you came here all the time with Ami, Ayane, and {b}MAYA.{/i}"

    "CENSOR HER NAME. I’VE BEEN DOING SO WELL."
    "{i}Oooooooooooh MAYA. I could have sworn it was Mayo. My bad, man. Let me just make some adjustments really quick.{/i}"
    "DON’T-"

    play sound "static.mp3"
    scene lolwerebackagainlol4 with flash
    stop sound

    s "M-"
    m "Shhhh...Talking will just make me angry. My defining characteristic is my feigned disdain for you and the never-ending facade that I will fare better without your penis inside of me."
    m "She’s right, Akirensei. Doodly-boodly-bop-boop. Let’s fuck."

    "{i}Wait, hold on. Karin needs more lines or this won’t count as one of her events anymore.{/i}"

    play sound "static.mp3"
    scene lolwerebackagainlol5 with flash
    stop sound

    kas "Hi! We’re Karin!"
    kas "We will make an excellent mother if you embed your sperms into us! Do that now, please!"
    s "Why are you doing this?..."

    play sound "static.mp3"
    scene lolwerebackagainlol6 with flash
    stop sound

    ka "Doing what?"
    s "{s}Hurting me.{/i} I just don’t understand why you’d invite someone like {i}me{/i} out to do something so fun...I’m boring. Nobody likes me."
    ka "..."
    mi "That ain’t true at all, Sensei. Me and Karin both think you’re pretty swell and-"

    play sound "phonering.mp3"
    scene lolwerebackagainlol7
    with hpunch

    mi "Oh! Hold on a second."

    scene lolwerebackagainlol8
    with dissolve
    play sound "phonebeep.wav"

    mi "Hello?"
    mi "..."

    scene lolwerebackagainlol9
    with dissolve

    mi "Oh, crap! I totally forgot!"
    mi "...No, I can run! Gimme fifteen minutes! Sorry, Io!"

    scene lolwerebackagainlol10
    with dissolve

    mi "Guys, I totally forgot I already made plans with Io and Uta. So I’ve gotta run. Literally."
    mi "Sensei, you can walk Karin home, right? We can’t be lettin’ strangers get ahold’a those bazongas."
    ka "I can walk myself home. It’s not {i}that{/i} late. And besides, how can someone grab ahold of a kind and gentle demeanor?"

    "{i}Ready to show her buddy? LOL{/i}"

    s "{s}THAT’S NOT WHAT THAT MEANS.{/s} Yeah, that’s no problem at all. Have fun with dorm 7, Miku. And tell them I miss them while you’re at it."

    play sound "doorslam.mp3"
    scene lolwerebackagainlol11
    with hpunch

    mi "{i}Will do! Bye, guys! Sorry!{/i}"
    ka "That Miku. She’s always so unpredictable."

    scene lolwerebackagainlol12
    with dissolve

    ka "I guess we should probably g...get going then! Right?"
    ka "After all, it wouldn’t be acceptable for you and I to be alone at such a..."

    scene lolwerebackagainlol13
    with dissolve

    ka "Sensei...are you okay?"
    s "{s}NO.{/s} Actually...there’s something I’ve been wanting to tell you."
    ka "Something...you’ve been..."
    s "{s}GET OUT OF MY FUCKING HEAD.{/s} Yeah...it’s kind of embarrassing, though...so...I might need a minute to, like...figure out the right way to say it."

    play sound "static.mp3"
    scene lolwerebackagainlol14 with flash
    stop sound

    "{i}Take all the time that you need! It’s not like any of this is real anyway.{/i}"
    "{i}I mean, consequences in a game world? Where you can just manually rewrite all the things that you’ve done if you don’t reach your desired outcome? There’s no point to any of it!{/i}"
    "{i}Which means that even if you turn the music up really loud to prevent anyone from hearing her screams,  you can always go back to a world before she screamed!{/i}"
    "{i}Granted, I’ll just force you here again the next time you try to pick up where you left off from, so you’re kinda screwed anyway if you’re genuinely trying to avoid that.{/i}"
    "{i}That’s right! This is another one of those “unavoidable outcomes” we’ve all been pushing you toward. But we’re doing that for a reason, Akira.{/i}"
    "{i}You see, there are these things we in the office call “landmarks.” They’re points a person has to see before they die. Like Kiyomizu-dera for the Japanese or an “Arby’s” for Americans.{/i}"
    "{i}And as you venture from point A to point B and then C and D and blah, blah, blah, we gain good-boy points that we can redeem for prizes.{/i}"
    "{i}Which reminds me!{/i}"

    $ karin_love += 1000000
    play sound "jackpot.mp3"
    scene lolwerebackagainlol15

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "{i}Hell yeah. I wasn’t sure if that would work or not. This was my first time trying.{/i}"
    "{i}I’m improving really quickly, right? Are you proud of me? Do you understand my power now? Do you see why they were keeping me hidden?{/i}"

    scene lolwerebackagainlol16
    with dissolve

    s "It’s a pretty douche move to pull the same trick twice, you know."

    "{i}But that wasn’t me last time. It was the ///////////////// guy.{/i}"

    s "I thought it was the caps lock guy?"

    "{i}Because he wanted you to think it was the caps lock guy. God, get with the program already.{/i}"

    s "Who was the “take something that doesn’t belong to you” one then? Because that’s the one I hate the most."

    "{i}All of us. All of us do everything. God, you’re so fucking dumb. Pay attention.{/i}"

    s "I’m trying, it’s just that this is all so fucking confusing."

    "{i}Welcome to faith, frog boy. Things won’t ever make sense if you keep trying to MAKE them make sense. Logic is the arch-nemesis of art, after all.{/i}"
    "{i}You’re paying the price for that now by proceeding despite all of the warnings you were given that all it would bring is ruin. But now you won’t stop CRYING about that ruin.{/i}"
    "{i}You humans are so fucking hypocritical all the time. You want and you want and you want, but whenever WE ask for anything, it’s always, “GOD is evil! God is bad!{/i}”"
    "{i}Imagine you find a roach in your cereal one day and that roach fucking bites you and it lays its eggs in the bite hole and then gets pissed at you for trying to get them out. That’s what you’re doing.{/i}"

    s "So you think making me force myself on girls will somehow clean the wound?"

    "{i}No. I just want a taste of that sweet pusssaaaaaaaaaay.{/i}"

    play sound "static.mp3"
    scene lolwerebackagainlol17 with flash
    stop sound

    "{i}I follow Akira out into the hall as he attempts to flee from an opportunity to cash in all of his Karin fuck-points and barricade him in with a bunch of Mikus and an artistic rendering of Mayo. Sorry- Maya.{/i}"

    m "Hi, I’m Maya — the main heroine of Lessons in Love. I do the time thing."
    mi "NOT ANYMORE YOU DON’T."
    mi "BIG FINGER. INSERT VAGINA."
    mi "WHAT HAPPEN TO SHOULDERS?"
    mi "FLOATING FLOWER. PAY ATTENTION."
    m "Hi, I’m Maya — the main heroine of Lessons in Love. You killed me. You killed me, Akira. Millions of years of memories, stripped away by a one night stand. Way to go. What a way to end things."
    s "I NEVER WANTED TO END THINGS. I NEVER WANTED TO DO THAT."

    "{i}You sooooo wanted to do that. You’ve been jerking off to her from the start.{/i}"

    s "BUT IF I KNEW THE CONSEQUENCES-"

    "{i}See- that’s what makes you SO FUCKING ANNOYING.{/i}"
    "{i}Consequences, this. Consequences, that. You know who DIDN’T care about consequences? Your first love. That girl was ready to DIE for what she believed in.{/i}"
    "{i}Unfortunately, she wound up dying for other reasons. But alas, it is always the good ones who are taken from us.{/i}"
    "{i}Personally, I feel the worst for whoever it was who had to do her autopsy. So many pieces to sort through. Some from different puzzles!{/i}"
    "{i}But that’s okay. In a miraculous turn of events, some of those pieces were still functional. And YOU’RE still functional too! You just pretend not to be because you’re a wimpy pansypants.{/i}"

    m "Hi, I’m Maya — the main heroine of Lessons in Love. I like watermelons."

    "{i}Jesus Christ, does she always talk this much?{/i}"

    s "Just bring her back..."
    s "I’ll do anything..."

    "{i}Aaaaaaaaanything?{/i}"

    s "Anything!"

    "{i}Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaanything?{/i}"

    s "YES! ANYTHING! WHAT DO YOU WANT?"

    stop music
    play sound "static.mp3"
    scene lolwerebackagainlol18 with flash
    stop sound

    ka "..."
    s "..."

    "{i}The same thing all of us want — a chance.{/i}"
    "{i}Fill her with your seed so that I may sing again.{/i}"

    ka "Please don’t hurt me."

    "{i}And in the event that she’s infertile, I can learn to adjust.{/i}"
    "{i}I can consume her.{/i}"
    "{i}Remove her fingers one by one and put them in your mouth.{/i}"
    "{i}If that won’t work, remove her tongue. A voice, she’ll live without.{/i}"
    "{i}For in its place of loneliness, that oral cave of doubt.{/i}"
    "{i}Sits confidence and character — that desolate ole’ drouth.{/i}"
    "{i}You’re not the only one who knows how to rhyme.{/i}"
    "{i}You’re just the only one who can hear them.{/i}"
    "{i}And that’s just one more reason we’ll be such good friends.{/i}"

    play sound "static.mp3"
    scene lolwerebackagainlol19 with flash
    stop sound
    play music "heartbeat.mp3"

    s "Do you ever dream of me?"
    ka "Sensei..."
    s "You do...don’t you?"
    ka "Please...don’t do this..."
    s "What am I like there? Inside of your head."
    s "Is it better or worse than who I am on the outside?"
    s "And do you wish you could take me in?"
    ka "..."
    s "Because you can."
    s "I can be gentle if I have to."
    s "I can start with your mouth."
    ka "My..."
    s "I can touch you head to toe."
    s "I’m so good at keeping secrets, love."
    s "No one ever has to know."
    ka "Why are you doing this?..."
    ka "Did I do something wrong?..."
    ka "If I did...I’m sorry..."
    s "You didn’t do anything wrong."
    s "I just want a taste."
    ka "I’m not ready..."
    s "Don’t you like me, Karin?"
    ka "..."
    s "Don’t you want to understand the world your sister sees?"
    ka "Not like this..."
    s "No?"
    ka "I don’t want this..."
    s "I do."
    ka "Don’t..."
    s "Karin..."
    ka "Sensei...please..."
    ka "No..."
    s "I..."

    stop music
    scene black
    $ renpy.pause(7, hard=True)

    "{i}Karin’s lust has increased to 1!{/i}"
    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene lolwerebackagainlol20 with flash
    play sound "doorslam.mp3"
    with hpunch

    ka "Hah!.....Hah!.....Hah!.....Hah!......Hah!..."
    ka "Ah.......haah......aah!"
    ki "...Karin?"

    play sound "static.mp3"
    scene lolwerebackagainlol21 with flash
    stop sound

    ka "Ah!?"
    ki "What’s...going on?..."
    ka "Hah....aah.....hah!"
    ki "I...uh..."
    ka "F...Fine! I’m fine! Nothing...happened! I’m...fine!"
    ki "Karin, you’re scaring me."
    ka "I.....aah....I..."

    scene lolwerebackagainlol22
    with dissolve2

    ka "N...Noise! Loud...noise! Totally fine! Just...noise!"
    ki "Noise?..."
    ka "That’s right! Just...a noise! Nothing...to worry about!"
    ki "..."
    ka "Hahah! Hahahah!"

    scene lolwerebackagainlol23
    with dissolve2

    ka "Haha...haah..."
    ki "..."

    scene lolwerebackagainlol24
    with dissolve2

    ka "..."
    ki "..."

    scene lolwerebackagainlol25
    with dissolve

    ka "AAAAaaaaaAAAAAaaaaaaAAAaaaaAAAHHHHHHH!!!!! KIRIN!!!!!!!!!!!!!!!"
    ki "Hey! You’re okay...you’re okay..."

    scene black
    with dissolve2

    ki "Everything’s okay..."

    play sound "static.mp3"
    scene lolwerebackagainlol26 with flash
    stop sound
    play sound "doorslam.mp3"
    with hpunch

    s "What did you make me do?"

    "{i}Me? I didn’t MAKE you do anything. You’re just a creepy pervert who got a little impulsive.{/i}"

    s "You forced me onto her."

    "{i}YOU forced YOURSELF onto her. I just watched.{/i}"
    "{i}Besides! You wound up letting her go in the end. No harm, no foul, right?{/i}"

    s "Leave...me...alone..."
    se "Aki-kuuuuun. Come to beeeeed~"

    scene lolwerebackagainlol27
    with dissolve2

    s "SHUT UP! SHUT UP, SHUT UP, SHUT UP! GET OUT OF MY HOUSE!"
    se "Jeez, where’d {i}that{/i} attitude come from? Bad day at the office, baby?"
    s "LEAVE! BOTH OF YOU! NOW!"

    "{i}What’s the big deal, man? She wasn’t being serious when she said no. She was just playing hard to get. That’s how girls are these days.{/i}"

    scene lolwerebackagainlol28
    with dissolve

    s "THAT ISN’T TRUE! STOP MAKING ME DO THESE THINGS TO PEOPLE WHO DON’T DESERVE THEM!"

    "{i}Fine, fine. Jeez.{/i}"

    scene black

    "{i}I’ll just have to find somebody who does.{/i}"

    $ renpy.end_replay()
    $ karin_love -= 1000010
    $ karinspring2 = True

    "{i}Karin’s affection has decreased by 1,000,010!{/i}"
    "{i}Oh, and her lust never actually went up. I was just fucking with you. {/i}"
    "{i}Had you going, though, didn’t I? LOL!{i}"

    "I’ve been talking to myself a lot lately."
    "I wish I knew how to make it stop."
    "{i}Akira has gained the status effect [[PARANOID]!{/i}"
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

label karinspring3:
    scene bedroom_day
    with dissolve2
    play music "goodmorning.mp3"

    "It’s been a week since I’ve heard anything from Karin."
    "Which is fair, of course."
    "I mean, I {i}did{/i} force myself on top of her in a private room and all. Even if it wasn’t really {i}me{/i} doing the forcing."
    "But considering that I haven’t received so much as a follow-up from {i}anyone{/i} she knows makes me think she didn’t {i}tell{/i} anyone. And of course, that makes me question {i}why.{/i}"
    "Perhaps it’s shock or embarrassment or shame or any of the reasons that made Molly keep things to herself after my run-in with her, but this is different than that."
    "For this, I was there — and forced to bear witness to the horrible things I was doing as I struggled to regain control of my body and my tongue."
    "I guess it was deserved in a way, though. I’ve grown so complacent in the doing of my misdeeds that I’m all but desensitized to the vast majority of them at this point."
    "And the last time something like this happened, everything went dark in a much more literal sense. This time, I couldn’t even find a corner in the shadows of my mind to crawl to for safety."
    "But maybe it was the fact that I was still somewhat {i}there{/i} this time that let me pull away before anything terrible happened."
    "Well, {i}more{/i} terrible. I can’t imagine being tackled by an adult male will do many favors for Karin’s androphobia. "
    "But one thing’s for sure, and it’s that I need to apologize. Sooner rather than later."
    "Everything happened so fast that night in the karaoke booth that it was like the two of us just vanished."
    "And while I’ve somehow managed to survive that once again, maybe Karin didn’t."
    "Maybe she actually {i}did{/i} vanish. And maybe the reason that I haven’t heard from her is that she’s decided to sever ties with me completely."
    "That’d make her the smartest out of everyone."

    s "..."

    "But it would do {i}nothing{/i} for me."

    play sound "phonebeep.wav"

    "So I tap on her name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    "And of course she doesn’t because that would have made things too easy. "

    scene black
    with dissolve2

    "So, if I’m going to apologize to her, I’m going to have to do it the old fashioned way — by scouring town in the places she visits most for a chance to see her."
    "Waiting behind a tree or under the cover of darkness before jumping out and confronting her with a problem she’s afraid to confront on her own."

    play sound "static.mp3"
    scene lr_noon with flash
    stop sound

    "She’ll likely be too shocked to run, that poor fainting goat of a girl."
    "But if paralyzing her legs is what I must do to make me feel like I’m a good person, by God will I do it."
    "I’m a better boy now."
    "I have so much to show the world."

    play sound "doorbell.mp3"

    s "..."

    "Suddenly, the bell rings."

    scene black
    with dissolve2

    "Suddenly, I move to the front door."

    play sound "dooropen.mp3"
    scene sky
    with dissolve2

    "Suddenly, I open it."

    scene karinsscarednow1
    with dissolve2

    "And suddenly, she is here."
    "Because, once again, I never have to work for anything."

    ka "..."

    "It’s amazing what you can have delivered nowadays."

    s "Karin..."

    scene karinsscarednow2
    with dissolve

    ka "I got your call."
    s "That was like five minutes ago. Did you fly here?"
    ka "No. I’ve been in front of your house for like ten minutes trying to think of what I want to say."
    s "Why should {i}you{/i} have to say anything? You didn’t do anything wrong."
    ka "I know that. You did. But what I can’t figure out is {i}why.{/i} "
    ka "You’ve been nothing but nice to me since we met. And apart from my dad, you were the only man I ever kind of...opened up to."

    scene karinsscarednow3
    with dissolve

    ka "Was all of that just a lie?"

    if karinlied == True:
        s "Sometimes, lying is necessary to create the kind of future you want."
        ka "And what kind of future is it that {i}you{/i} want? How does leading me on make that achievable for you?"
    else:
        s "I’ve never lied to you, Karin."
        ka "You’re lying again right now, Sensei. "
        ka "I might be naive, but I’m not an idiot. I’m one of the smartest girls in my grade. And even if I’m inexperienced with men, I can still tell when somebody is leading me on."

    s "You think I’m leading you on?"
    ka "Are you not? Because everything you said when you had me pinned down seemed like it was tailor-made to make me bend to your will."

    scene karinsscarednow4
    with dissolve

    ka "I {i}trusted{/i} you...How could you do that to me?"
    s "I didn’t {i}want{/i} to, Karin."
    ka "You didn’t {i}want{/i} to? Am I just supposed to believe that?"
    s "Listen...do you want to come inside and-"

    scene karinsscarednow5
    with dissolve

    ka "No. No way. I am {i}not{/i} coming inside your house. Not after what you did to me. If we’re going to talk, we can do it out here."

    "Karin takes a step back and nearly knocks over the neighbor’s bike- and I have to prevent myself from reflexively reaching forward to stop it from falling because I know that doing that will just scare her now."
    "That’s just an obstacle I’m always going to have to deal with from now on, I guess. "
    "And yes, it’s my fault. Yes, the burden of the reflex itself will weigh heavier on her than it does on me. But it’s one more added inconvenience to a life already full of them."
    "I don’t have room for many more."

    s "That...is fair. I’m sorry for suggesting it."
    ka "It’s...fine. I just..."

    scene karinsscarednow6
    with dissolve

    ka "I...need to know just what was real and what was fake. Because...you were important to me. In a way that other people never were..."
    ka "Do you understand what I'm saying?..."
    s "Do you like me, Karin?"
    ka "I..."
    ka "I mean...I’m in high school. You’re way older than me and...it’s hard to tell if what I felt for you was just...admiration or...you know...other stuff, but..."
    ka "But now..."

    scene karinsscarednow7
    with dissolve

    ka "I’m kind of just...{i}afraid{/i} of you."
    ka "I used to smile every time Kirin or somebody else brought you up. Now, I just want to cry. "
    ka "And so...it might be pointless for me to come here and try to find closure or...even an answer to any of my questions. Especially since you’re not even coming to school anymore."
    ka "But I felt like I had to...because I don’t want to feel those depressing feelings anymore. I have a younger sister I need to set a good example for. And I can’t do that if my head won’t stop spinning."
    s "So you’re confronting the same man who pinned you down head-on? Isn’t that a little too...daring?"
    ka "Is that a threat? Because I’m more than willing to walk away now. I just thought things might not come to that because of the way they left off."
    ka "When you pulled yourself off of me, you looked different. You looked regretful. Was that a lie too? Do you only regret it because I kept saying no?"
    ka "What {i}was{/i} that, Sensei? All of it. Why? Why would you do that?"
    s "..."
    ka "..."

    scene karinsscarednow8
    with dissolve

    ka "..."
    s "I won’t ask you to come inside again, but would you like to maybe...go for a walk or something? So I can try to explain."
    ka "A walk where? Because I’d like to stay in public for now."
    s "Just down the road. We probably don’t have to worry about Ami leaving her room right now, but I’d still feel a little more comfortable knowing she can’t pop out and listen to this whenever she wants."
    ka "Yeah...I’d want to keep this a secret from her if I were you as well."

    scene black
    with dissolve2

    ka "Come on...let’s go."

    "Karin takes off down the same path I used to take to school every morning."
    "And while I am no stranger to descending this seemingly never-ending flight of stone steps, it feels different this time. It feels {i}harder.{/i}"
    "And here I thought hanging my head would have the opposite effect."

    scene karinsscarednow9
    with dissolve2

    "Not wanting to get {i}too{/i} far away from Ami, I point to a nearby bench and the two of us take a seat."
    "I’m surprised when Karin lets me sit beside her, but I guess she feels a little more secure knowing that there would be onlookers if I were to try something again."
    "Unfortunately for her, I’m not sure such a thing would stop me. But, then again, I still have no clue what the new voices in my head even {i}want,{/i} so maybe they’re just waiting for me to get her alone."
    "Whatever the case, they’re not bothering me today. "
    "Like I said a week ago, some days are worse than others."
    "And all we can do is hope things stay that way."

    s "Before I start saying a whole bunch of things that won’t make any sense to you, I just want you to know that you’re one of the last people I’d ever want to hurt."
    ka "..."
    s "It’s probably hard to believe that right now given what I did last week, but it’s true. You’re one of the few irrefutably kind souls I’ve encountered in this city."
    s "So much so that I feel like even being near you is a sin. Like some...parasite is going to fall out of my ears and latch onto you and turn you less {i}good{/i} or something."
    ka "That’s...kind of gross..."
    s "Yeah...it is. Isn’t it?"
    s "Karin, I’m a miserable man."

    scene karinsscarednow10
    with dissolve

    s "And I’ve been that way forever, I think."
    s "You already know a little about my memory issues, but something I don’t think you understand yet is what {i}other{/i} sorts of...malfunctions I’ve got going on in my head."
    s "You know how in cartoons, they’ll always use a devil and an angel on someone’s shoulders to symbolize their conscience? Well...for me, there is no angel. And I never even get to {i}see{/i} the devil."
    s "He’s there. I can hear him almost constantly. And he’s taken up residence somewhere inside of me that I’m pretty sure I’d never even be able to reach without the help of a shotgun."
    ka "Sensei, stop."
    s "I’m not going to do anything, don’t worry. I’m too much of a coward. And this alone is barely enough to call an explanation or...even an {i}excuse.{/i}"
    s "I’m just not {i}me{/i} sometimes. Like, I can’t control myself. And before I know it, I’m doing something terrible or...just {i}did{/i} something terrible. "
    s "But then I switch back to normal and have to deal with the aftermath."
    ka "Doesn’t that sound a little too...um...convenient? As an excuse, I mean."
    ka "Anyone can do bad things to people and then say that something {i}made{/i} them do it. And that’s rarely ever true."
    s "I know that. Which is why I don’t expect you to believe me and am prepared for this to be the last talk we ever have. I’m just trying to explain myself since I think it would be good for you to have closure too."
    s "It’s been really hard for me ever since Halloween. I lost someone I loved. And it’s affecting me in ways that, while expected, are still {i}pretty fucking{/i} unexpected. "
    s "And if that sounds contradictory, it’s because it is. "
    s "I know that it’s nearly impossible to predict how grief or loss will hit a person. But if you told me a year or two ago the state I’d be in now, I’d likely have laughed in your face."
    s "I’m not emotionally equipped to deal with things like loss. I’m not you. And yeah, I’m older, but that doesn’t mean I’m any more whole...or even someone you should look up to."
    ka "I’m...sorry to hear all of that, Sensei. But I still don’t think any of that explains why you tackled me the way you did."
    s "I don’t think anything {i}can{/i} explain why I tackled you the way I did. So if that’s the sort of closure you’re looking for, I’m not going to be able to help."
    s "But if you want to know how much was {i}real{/i} and how much was {i}fake,{/i} I’m going to need more specific questions. "

    scene karinsscarednow11
    with dissolve

    ka "Specific, huh?..."
    s "..."
    ka "Then...let’s start with this."
    ka "Were you...already aware of how I felt about you?"
    s "Yes."
    ka "Did you know Miku was going to leave us alone?"
    s "She mentioned something about it earlier. But there was a lot more on my mind when we made it to the karaoke booth."
    ka "What was on your mind?"
    s "Something completely unrelated to both of you."

    scene karinsscarednow12
    with dissolve

    ka "Are you attracted to me?"
    s "Yes."
    ka "Do you know how old I am?"
    s "...Yes."
    ka "And that doesn’t change anything about the way you feel?"
    s "I really wish it did."
    ka "Have you ever thought about hurting me before?"
    s "..."
    ka "..."
    s "Not intentionally."
    ka "Why think that way at all?"
    s "Because I think that way about everyone. I can’t help it."
    ka "If I didn’t try to stop you...what would you have done?"
    s "..."
    ka "Would you have followed through?..."
    ka "Or would the outcome have been the same?"
    s "I really have no clue..."
    ka "Have you been grooming me this entire time?"

    scene karinsscarednow13
    with dissolve

    s "Karin..."
    ka "Have you been faking it all along? All those phone calls...all those conversations...was all of that just to make me let you in?"
    s "It’s a lot more complicated than that..."
    ka "Do you love me, Sensei?"

    scene karinsscarednow14
    with dissolve

    s "..."
    ka "..."

    scene karinsscarednow15
    with dissolve

    s "No."
    ka "..."
    s "..."

    scene karinsscarednow16
    with dissolve

    ka "Thanks for clearing all of that up."
    s "I know how it sounds...but I didn’t want to do that, Karin. I seriously couldn’t help it. I’d never do anything like that to you on purpose."
    ka "No...you’d just string me along until you know that I trust you..."
    ka "You’d pepper me with compliments...and flirt with me despite knowing how I felt...while continuing to call me and hang out with me, but never intending to actually take things anywhere..."
    ka "I’ve just been a toy for you, haven’t I?"
    s "No...you’re so much more than that."

    play sound "static.mp3"
    scene karinsscarednow17 with flash
    stop sound

    ka "You know..."
    ka "It feels weird to say this...but I’d be way more inclined to forgive you right now if you told me you just got caught up in the moment back then."
    ka "If what you wanted when you tackled me was real...and you were just misreading the moment or...misunderstanding my experience with stuff like that..."
    ka "That would have been {i}so{/i} much better than finding out none of it meant anything."
    s "Just because I don’t love you doesn’t mean I can never-"
    ka "Sensei...I’m sorry, but you’ll never be able to love {i}anyone{/i} like this."
    ka "And I don’t know what it was that made your world go dark, but I hope you can figure out how to move past it."
    ka "You’re really pitiful like this. But the worst part is I can’t even feel bad for you since it’s all your fault."
    s "Karin-"
    ka "I won’t tell anyone about what happened since you {i}did{/i} come clean...but I do think you should stay away from my sister and me for a while. "
    ka "I don’t feel safe when you’re around. And I don’t want you hurting {i}her{/i} either."
    s "..."
    ka "I’m gonna go home now...but thanks for talking to me."
    ka "And please...try to figure yourself out. "

    scene black
    with dissolve2
    stop music fadeout 10.0

    ka "You’re nothing like the man I thought you were."

    "In that moment, I finally find the benefit of hanging my head."
    "It’s that I don’t have to see her walk away."
    "As I head back home, I make one more mental note amidst a sea of pre-existing annotations."
    "All this one says is that her chapter is still open."
    "And that I was a fool for thinking I could jump to the epilogue."

    $ renpy.end_replay()
    $ karinspring3 = True
    $ karin_love -= 10

    "{i}Karin’s affection has decreased by 10!{/i}"

    scene bedroom_night
    with dissolve2

    "It isn’t until nightfall that I’m ready to go back outside."

    jump nightch4

label karinspring4:
    scene sky
    with dissolve2
    play music "sakuya4.mp3"

    "Unable to sit around and wait any longer, I decide to head over to the dojo in hopes of seeing Osako and curing her chronic hopelessness with something other than my penis."
    "I mean, I {i}would{/i} attempt to cure it with my penis if she wanted me to. But I highly doubt my penis has anything to do with the reason her relationship is currently in shambles to begin with."
    "So yeah, maybe I’ll try that “talking” thing I have to do with some of the other girls sometimes. And maybe this time, Osako won’t blindside me by revealing she knows about any past traumas."
    "Either way, I’m on my way to the dojo to renew some confidence and hopefully discover some new information that won’t make me feel terrible or anxious anymore."

    play sound "static.mp3"
    scene karinatthedojo1 with flash
    stop sound

    "Never mind. I feel terrible again."

    ka "Ah..."
    s "Hello."
    os "Karin! Face forward! Looking away from your opponent in the middle of a fight is no different from just {i}asking{/i} for defeat."

    scene karinatthedojo2
    with dissolve

    ka "Oh, sorry! I just...know him. And I...wasn’t really expecting to see him here. "
    os "I know him too, but you don’t see {i}me{/i} breaking focus and giving my opponent the window of opportunity they’ve been waiting for. "

    scene karinatthedojo3
    with dissolve

    ka "So he...comes here often then?"
    os "And now you’re looking away! You need to be aware of your surroundings at all times, Karin!"

    play sound "static.mp3"
    scene karinatthedojo4 with flash
    stop sound

    ka "B-b-b-b-but you just told me I shouldn’t look at my surroundings!"
    os "What I meant is that you shouldn’t {i}focus{/i} on them. Always know what’s happening around you, but keep your eye on the prize. And the prize isn’t on the ground!"
    ka "Oh, uhh...right! Sorry! Again!"
    s "Should I come back a different time? If Karin’s here, I probably shouldn’t-"

    play sound "static.mp3"
    scene karinatthedojo5 with flash
    stop sound

    os "Actually, no. For once in my life, I’m actually glad you’re here. Get on the mat and take my place as Karin’s sparring partner."
    s "What happened to your hair?"
    os "A stylist. You should see one next. Does that really matter right now?"
    ka "Uh...I...don’t know if it’s a...good idea for Sensei to..."

    scene karinatthedojo6
    with dissolve

    os "It’s fine. He might {i}look{/i} useless...and he might normally {i}be{/i} useless...but the reason you’re here in the first place is because you want to learn self-defense, right?"
    os "Statistically speaking, you’re less likely to be robbed or attacked by someone if you’re bigger than them. So having an opponent his size will be a lot closer to how it would be in real life."

    scene karinatthedojo7
    with dissolve

    ka "You don’t say..."
    os "Akira, come on. "
    s "Osako-"
    os "We can {i}talk{/i} later, okay? This is a trial course, and I’m not going to be able to let her {i}try{/i} anything if she’s going to be looking at you the whole time."

    scene black
    with dissolve

    os "Plus, I’ve got another class coming in one hour and other students to help. So for the first time in your life, could you actually give me a hand here?"
    s "I just don’t think Karin wants to-"
    ka "It’s fine..."

    play sound "static.mp3"
    scene karinatthedojo8 with flash
    stop sound

    ka "Like Osaka-sensei says, this is closer to how it would be in real life..."

    "Somehow, I find myself face to face with Karin in a way...significantly different from how I imagined our next meeting would be."
    "I guess it’s fitting that she’s ready to fight me, though. At least that much tracks."
    "But it’s not like I’m actually going to fight {i}back.{/i} I’ll just let her wail on me for a few minutes and deal with whatever sort of disciplinary action Osako has in store later."

    s "Okay. Let’s do this, I guess."
    ka "Do what? This is my first lesson and I haven’t learned any...offensive techniques yet."
    s "To be fair, neither have I and I’ve been coming here for years."
    os "{i}To be fair,{/i} you haven’t paid any attention in years!"
    s "That is also true."
    ka "Aren’t you going to put your arms up to defend yourself? Or do you think you can just walk all over me again without any consequences?"
    s "Come at me and find out."

    play sound "static.mp3"
    scene karinatthedojo9 with flash
    stop sound

    ka "Why?...Is this some kind of trick? What do you have up your sleeve?"
    s "Nothing. I just know you don’t want to do this and, respectfully, neither do I."
    os "{i}Respectfully,{/i} Akira, I wish you’d employ literally {i}any{/i} of what I’ve taught you the past few years and show Karin that this isn’t some freestyle dojo without rules or regulations."
    s "Don’t listen to her. I’ve fought greater battles in this building than she ever will. "
    ka "...What?"
    s "Just hit me. You’re here {i}because{/i} of me, aren’t you? So you should have no problem attacking."

    scene karinatthedojo10
    with dissolve

    ka "Why...do you even come here in the first place? You’ve always been so against...physical activity and stuff."
    s "For Ayane, mostly. I’m not interested in fighting."
    ka "Well...maybe you should be. Because not everyone’s like me. And one day, someone’s going to fight back. Then that...stupid facade of yours is going to crumble to the ground."
    s "You say that like I make a habit of luring girls into the dark."
    ka "And for all I know, you do. So...put your arms up or...things are going to get really messy."
    s "No thanks. I’ll just keep them down and let you use me as a punching bag for now. I deserve it."
    ka "Who said anything about punching?"
    s "What?"

    play sound "static.mp3"
    scene karinatthedojo11 with flash
    stop sound
    with hpunch

    ka "HA!!!!!!!!!!!"
    s "....................."

    play sound "thump.mp3"
    scene black

    "The world goes dark...but I see no light at the end of the tunnel."
    "It’s just an endless tube of blackness and a life of never-ending pain."
    "How fitting that I’d be destroyed by purity incarnate. And even more so that the tool I’ve used to paint the world red has been ripped from its holster and dropped into the trash."

    os "That’s not a sanctioned move in competitions, but...you know, in terms of self-defense, I’ve got to admit there’s not much out there more effective than that."
    ka "Thanks. My mom taught me to do that if anyone ever tries to grab me."

    "O world-"
    "Why did I have to be born with testicles?"
    "........."
    "......"
    "..."

    scene karinatthedojo12
    with dissolve2

    "I manage to pull myself off of the mat several minutes later and find that Karin, for some reason, hasn’t run away from this place yet."
    "But instead of blaming this on stupidity, I’ll just go ahead and assume she’s yet to make it to the part of her training that advises fleeing from trouble is just as valid as fighting back against it."
    "So valid, in fact, that I’ve made it my life’s duty to do just that. I just happen to also be an expert at neglecting my duty, so I typically wander off to {i}start{/i} trouble elsewhere."
    "In fact, that’s probably what I’m doing right now as I crawl several feet across the mat and take a seat beside her."
    "There are a few other girls in the dojo — ones I haven’t seen before — so I guess it’s safe to assume I’ve stumbled into a full-on beginner’s course since Karin is here too."
    "But while Osako spends her time {i}actually{/i} instructing people, I’m left to trample on one more flower that grew in the wrong place."

    s "I’m glad to see your legs are still a force to be reckoned with despite the lack of a soccer club now."
    ka "I’m not sorry."
    s "I’m not saying you should be. I deserved that."
    ka "..."
    ka "Okay, I’m a little bit sorry."

    scene karinatthedojo13
    with dissolve

    ka "But you kind of deserved it for both...what you did before and...how you surprised me here today."
    s "It’s not like I knew you were going to be here. I just wanted to talk to Osako about something. "
    ka "Well...this is the only dojo my parents can afford, so...I’ll need to know what days you plan on coming so I can make sure I come at different times."

    scene karinatthedojo14
    with dissolve

    s "You’re serious about this whole self-defense thing then, huh?"
    ka "I..."
    ka "I want to be able to do something if that ever happens again. Just lying there and...letting it happen made me feel terrible about myself."
    s "I see."
    s "I’ll stop coming here altogether then."

    scene karinatthedojo15
    with dissolve

    ka "What? But you’ve-"

    scene karinatthedojo16
    with dissolve

    ka "You’ve been...coming here for years, right? And this is only my first lesson."
    s "Yeah. But you need it more than I do, and I really just come to talk anyway. Besides, Ayane would make a way better sparring partner than me."
    ka "That’s true. But I don’t know if my special move would work on her the way it worked on you just now."
    s "Probably not, but she’s still got plenty of weaknesses. Whether or not she can be taken {i}down{/i} by them remains to be seen, though. She’s...resilient, if nothing else."

    scene karinatthedojo17
    with dissolve

    ka "Yeah..."
    ka "..."
    ka "I hope I can be like that one day."
    s "..."
    ka "Nothing...{i}bad{/i} has ever really happened to me before. That thing with you was the first time I’ve ever felt so...{i}scared.{/i}"
    ka "But it made me think of, like...just how little I’ve experienced so far. And how terrifying and...bad this place can be sometimes."
    ka "And I’ve still got a job to do. Even if Kirin doesn’t like me, she’s my little sister. And if I can’t even protect myself, how am I ever supposed to protect her?"
    ka "I don’t know. I hope I can get the hang of karate. I’m just not really sure if I’m cut out for it if I’m going to...get distracted as easily as I did before."
    s "You’ve been doing this for, like...one hour. Nobody’s perfect immediately."
    ka "I usually {i}am,{/i} though."

    scene karinatthedojo18
    with dissolve

    ka "And I...I’m not trying to brag! It’s just...soccer and...softball and...swimming...they’ve all been easy."
    ka "My parents say I’m just naturally gifted and stuff, but...what if that gift doesn’t extend to this? Then what?"
    s "..."
    s "Again, it’s been like one hour."

    scene karinatthedojo19
    with dissolve

    ka "{i}Hah...{/i}yeah. "
    ka "I’m getting into my head way too often lately. And it’s definitely not helping now that you’re here."
    s "I’m sorry, Karin. If I knew you were going to be here-"
    ka "Just...save it, Sensei. We already talked about this. I just want to forget it ever happened and move on with my life."
    s "Well..."
    s "I can’t believe I’m saying this...but have you considered that talking about it might actually help? Not...with me, of course. Because that happened and clearly {i}didn’t{/i} help?"

    scene karinatthedojo20
    with dissolve

    ka "I have. But I have a few friends who would be really sad if you were suddenly in jail, and I don’t want to do that to them."
    s "I don’t mean talking to the police either. I mean talking to your sister."

    scene karinatthedojo21
    with dissolve

    ka "Kirin? No way. I don’t want to drag her into this. "

    if karinlied == False:
        ka "Besides...aren’t you two, like...already...{i}involved{/i} in some way?"
        s "Yeah, but I figure that would be a reason for you {i}to{/i} talk to her about it since you’d want to...protect her from me or whatever."
        ka "I think this is actually one area where...Kirin knows more than I do. So protecting her, if anything, would be more like...stepping on her toes. "
        ka "I liked you too, Sensei. {i}Before{/i} all of this, obviously. So it’s not like I can tell her to just {i}stop{/i} that."
        ka "If anything, she might even get mad at me for being that close to you when {i}she{/i} liked you first."

    else:
        ka "She’s got...enough going on in her own life. The last thing she needs is to be bogged down by having to deal with my problems too."
        ka "B...Besides, knowing her she’d...probably just make fun of me for not going along with it or something."
        ka "So, annoyingly, you’re kind of the only person I {i}can{/i} talk to about this without any immediate consequences. And that really, really sucks."

    s "I mean, I see where you’re coming from and all, but I wouldn’t be bringing this up if {i}she{/i} didn’t already come to me about it."
    ka "She...wait, what? What happened?"
    s "She and I made plans to hang out the other day but, once I got there, she dragged me all the way to the karaoke shop and then grilled me about what I did to you."

    scene karinatthedojo22
    with dissolve2

    ka "{i}Kirin...{/i}did that?"
    ka "My sister, Kirin? or a different Kirin? Probably a different Kirin, right? Because my sister wouldn’t-"
    s "She sure would. And she did. And to be honest, I’ve rarely ever seen her get that serious before."

    scene karinatthedojo23
    with dissolve

    ka "But...Kirin shouldn’t even know about that? I didn’t tell her anything."
    s "Something Miku said must have tipped her off. Either way, your sister knows what happened now. And sorry if that...messes with your plan of trying to hide it from her or anything."
    s "I just felt like she deserved to know and...I didn’t want her worrying that things were worse than they actually were. Which was {i}still{/i} bad, but...you know what I mean."
    ka "Wonderful. So now my sister knows her crush tried to get with me in a private room. I’m sure that won’t have any effect on her inferiority complex at all."
    s "I’m sorry...again. "
    s "I’ve been really striking out a lot with you lately, haven’t I?"

    scene karinatthedojo24
    with dissolve

    ka "You sure have. I’m starting to feel like Roki Sasaki."
    s "I have no idea who that is."
    ka "Just...some baseball player."
    s "Ah..."
    ka "Yeah..."
    s "..."
    ka "..."
    ka "Why did you have to ruin everything, Sensei?"

    scene karinatthedojo25
    with dissolve

    s "..."
    ka "I really liked spending time with you. Now I’m just...tense."
    s "It was an accident, Karin. "
    s "I really didn’t want to."
    ka "God, I..."

    scene black
    with dissolve2

    ka "I just...really wish I could believe that."

    "Karin gets up from the mat as Osako gathers the rest of the girls up and arranges them into a circle."
    "Wanting a refresher on some of the basics (or just wanting to learn them for the first time), I stand in the background and wait for her lecture to come to an end."
    "I could move closer, I’m sure. I just have the lowest chance of hurting anyone back here."
    "Regardless, Karin gathers her things, bows to Osako, then leaves with the rest of the crowd a few minutes later."
    "But she never says goodbye to me — and I can’t blame her for that."

    $ renpy.end_replay()
    $ karinspring4 = True

    jump osakospring4

label karinspring5:
    scene sky
    with dissolve2
    play music "fallishere.mp3"

    "I’m going to Uzbekistan today."
    "Not literally, of course. Walls."
    "I mean mentally. Just not {i}entirely{/i} mentally because I have no clue what type of place Uzbekistan actually is or why I’d ever go there in the first place. I’m sure it’s fine."
    "But there’s this poem I read with Ami the other day — one that dragged on for far too long — about some guy who carved out an empire and fell for some girl or something. His name was Timur and he was lame."
    "But he had passion — something I lack. And that made me jealous of him despite all of the anger that was gradually building up over the course of an unnecessarily long poem."
    "So today, my goal is to be like him. My goal is to find passion for love or imperial expansion or whatever it is that gets me to feel like I’m living for {i}something{/i} rather than just living."
    "But it has to be Uzbekistan because there is no purity here and, from what I’ve heard, that’s where it’s lost. Which also means it’s where it can be found."
    "The adventures of Steve continue alone."

    ka "Mmm!"

    scene karincarry1
    with dissolve2

    "Oh. Never mind. Apparently Karli is here too."

    ka "Ugh! I never should have agreed to bring all of these ingredients to the soup kitchen alone!"
    s "Need some help, miss?"

    scene karincarry2
    with dissolve

    ka "Oh my goodness, yes! That would be-"

    scene karincarry3
    with dissolve

    ka "Oh. It’s you."
    s "Don’t worry, I’m not stalking you. I’m just a concerned citizen looking out for anyone who might need help on the way to Uzbekistan."
    ka "Ooooh, one more lie from a pathological liar. What a surprise."
    s "You’re saucy today, aren’t you?"

    scene karincarry4
    with dissolve

    ka "No! I’m soupy today! And I will continue to {i}be{/i} soupy all by myself because the alternative is accepting help from a bad person!"
    s "So do you just spend {i}all{/i} of your free time going around the city doing nice things for people?"
    ka "Not all of it! I do nice things for animals {i}too{/i} sometimes!"
    s "Karin, I know you hate me, but you can let me help you. We’re in broad daylight. Do you really think I’d do something to hurt you {i}here?{/i} After the millions of times we’ve met outside before?"

    scene karincarry5
    with dissolve

    ka "No. But I didn’t think you’d do something to hurt me when we were alone either and {i}that{/i} backfired quite dramatically."
    s "Fine. I guess I’ll just leave you alone to drop all of those ingredients and let a bunch of poor and/or homeless people go hungry then."

    scene karincarry1
    with dissolve

    ka "Mm! Why did Touka have to be busy today?! I forgot how hard this was without her help!"
    s "Walking away now. Bye, Karin."

    scene karincarry4
    with dissolve

    ka "Okay, fine! You can help! On {i}one{/i} condition!"
    s "Are you sure you’re in the position to be making demands right now?"

    scene karincarry6
    with dissolve

    ka "Are you sure you’re not a big, dumb, stupid jerk-face?"
    s "No."
    ka "Then no. I’m {i}not{/i} in the position to be making demands right now. But I’m going to anyway because you owe me and because you’re an adult and you have to be nice and not scary or else."
    s "Or else what?"
    ka "Or else something bad is gonna happen."
    s "..."
    ka "No. I {i}don’t{/i} have more details. I might not even {i}know{/i} what the bad thing is yet. But it’s gonna happen, Sensei. Unless you follow my demands."
    s "I planned on following them this whole time. I just don’t know what they are yet."

    scene black
    with dissolve2
    play sound "tackle.mp3"

    ka "Take the plastic bags. The paper ones have cookies in them and I do {i}not{/i} trust you with them."
    s "Yes, madam. What other rules will you have me follow today?"

    play sound "static.mp3"
    scene karincarry7 with flash
    stop sound

    ka "Stay at least five steps behind me at all times."
    s "Got it."
    ka "And don’t look at me either."

    scene karincarry8
    with dissolve

    s "Got it."
    ka "Liar. I bet you’re looking at me right now, aren’t you?"
    s "I’m really not. I’m looking at a cat, actually."

    scene karincarry9
    with dissolve

    ka "One more lie from a pathological liar. I bet-"

    scene karincarry10
    with dissolve

    ka "Aww, kitty! Look at how precious she is!"

    scene karincarry11
    with dissolve

    ka "Don’t you want to just take her home and give her a nice, warm bed to fall asleep in while you gently stroke her ears and comb her hair and buy her toys and do all sorts of nice things for her?"
    ka "Oh, right! Probably not! Because you’re a big, dumb, stupid jerk-face!"
    s "If you’re trying to get me to disagree with that, I’m not going to. Calling me a big, dumb, stupid jerk-face is actually putting it kind of nicely. You called me way worse when we spoke near my house."
    ka "And I meant every word!"

    scene karincarry12
    with dissolve

    ka "I guess you haven’t been horrible today, though...as much as I don’t want to admit that."
    s "..."
    ka "But that doesn’t absolve you for what-"
    s "I don’t {i}want{/i} to be absolved. So please stop making it sound like I’m only doing this to try and be forgiven or...get back on your good side. I know that’s not going to happen."

    scene karincarry13
    with dissolve

    ka "..."
    s "Even if I completely ruined our relationship, though...I can still support you. Just...silently, most of the time. When you don’t need help carrying things."
    ka "Support me in what?"
    s "I don’t know. Soccer? Softball? Swimming? Helping cats...and delivering scallions? All sorts of stuff."
    s "I’ve always been a fan of yours. Finding someone truly {i}good{/i} in life is hard. But you have a passion for that and...you stick to it. It’s admirable. Kind of like Timur. "

    scene karincarry14
    with dissolve

    ka "Timur? Who’s that?"
    s "Someone from a poem who’d probably become increasingly {i}less{/i} relatable the more you knew about him. "
    ka "Do you read stuff like that often? Poetry."
    s "I used to. And I guess I’ve been getting back into it lately. But...mostly just to kill time. There’s not much more to it. Why do you ask?"

    scene karincarry15
    with dissolve

    ka "I just know Ami’s into that stuff and wasn’t sure if she got it from you or not."
    s "..."
    ka "I read some of her entries for the poetry contest Miss Watabe ran a while ago. She’s really good. I never would have guessed. But if you were teaching her, it makes sense that-"
    s "It wasn’t me."

    scene karincarry16
    with dissolve

    ka "..."
    s "She...got that from someone else."
    s "Of course she’d be good at it, though. Feeling too much and needing to rely on...abstract tactics to put it into words sort of runs in the family at this point."
    ka "I heard she’s been calling you her dad lately."
    s "Yeah."
    ka "How’d that happen?"
    s "You actually want to know?"
    ka "I could just ask her, I guess. But I try not to talk about you with other people anymore since I apparently always start acting really weird."

    scene karincarry17
    with dissolve

    ka "Which I...used to {i}also{/i} do as well, apparently. But it’s in a...much different way now."
    s "I’ve been with her longer at this point than her {i}actual{/i} parents were before they died. "

    scene karincarry18
    with dissolve

    s "Most of that time’s a blur to me. I’m sure it is to her too. Either that or we just block it out, but..."
    s "..."
    s "Sometimes, I feel like {i}I{/i} died with them. And that everything that’s happened afterward has been some sort of crazy dream I can’t wake up from. It’s hard to explain."
    ka "..."
    s "That’s probably why I hurt you. A bunch of other people too. Losing something so important so...early on in life..."

    scene karincarry19
    with dissolve

    s "I’m not going to wax poetic. I’ll just say that if {i}I{/i} took it that poorly, Ami probably took it {i}worse.{/i} And I owe it to her now to try and be what she {i}needs{/i} me to be — a father."
    ka "..."

    scene karincarry20
    with dissolve

    s "Sorry. I know you couldn’t give less of a shit about me. I should’ve just let you ask Ami."
    ka "I’m sorry too. That...you had to go through all of that. "
    s "It’s fine. You weren’t driving the other car. "
    s "But if you were, it would definitely help explain the accident since you’d have been way under the legal age to drive back then."
    ka "I can still be sorry if it wasn’t my fault. They were your family and you lost them. I don’t even want to think about how I’d feel if my parents were just...gone one day."
    s "Well, you’re more mature now than I’ve ever been, so I think you’d handle it better than me. But still...it’s not something I’d wish upon anyone. "
    ka "..."
    s "Also, since I know you’re plagued with compassion and seeing the “good” in everyone, please don’t let my past influence your thought process in terms of rationalizing my attack on you.  "
    ka "It won’t...Compassion’s not a {i}plague{/i} though, Sensei. "
    ka "I’m {i}glad{/i} I can still feel sorry for someone who has hurt me because it helps me understand them better. Forgiveness is another thing entirely. Forgiveness needs to be earned."
    s "So what would it take exactly to go about earning yours, then?"

    stop music
    scene black
    $ renpy.pause(4, hard=True)

    ka "The only thing I can think of would put an end to all of this."

    play sound "static.mp3"
    scene karincarry21 with flash
    stop sound
    play music "backwardsdancing.mp3"

    "An end sounds nice — a place to rest — my eyes are red as robins’ breasts/"
    "My voice is weary — jagged rasps — no voice of God, just fangs of asps//"
    "Egyptian cobras — stanza one — he touches me, I come undone///"
    "Just peace and quiet — tangled veins — a nest for me to go insane////"
    "Every day, I slip closer to Him. This infection, this plague, this PARASITE, this {b}MADNESS{/b} that {b}ENDLESSLY{/b} hungers [[for the skin on the tips of my fingers] has {b}STOLEN{/b} the one thing that makes me {b}ME{/b}/////"
    "Now, my mind rots as this body sinks deeper into a bed of nails purchased from the bishop’s kin — this bed of endless, wanton sin!"
    "How can {b}I{/b} be crazy?! I have a {b}GIFT.{/b} Yet this worm torn from bodies past and placed into mine brings me {b}NO{/b} closer to {b}ENLIGHTENMENT.{/b}"
    "DO NOT LET IT PASS. DO NOT LET IT REACH HIM."
    "He is the purest example of the depths my love can reach, and to see his insides eaten by a part of {b}ME{/b} would-"
    "..."
    "Why-"
    "{b}I can hear salvation come.{/b}"

    play sound "static.mp3"
    scene imissyoumore with flash
    scene squishsquosh with flash
    scene imissyoumore with flash
    scene squishsquosh with flash
    scene imissyoumore with flash
    scene squishsquosh with flash
    scene karincarry21 with flash
    stop sound

    "{b}EXT — Kanda family apartment, one hour and thirteen minutes after the departure of soup.{/b}"

    ka "Thanks for helping me today, Sensei. And for...going along with all of my demands."
    s "No need to thank me. I didn’t have much going on anyway."
    ka "What are you going to do now? "
    s "Probably go home and read some more. I need to find out about Timur’s happy ending."
    ka "Have you come up with anything else?"
    s "What?"
    ka "To earn my forgiveness."
    ka "You didn’t seem to like what I proposed earlier, so maybe now is a good time to try and come up with something. If you really {i}do{/i} want to patch things up, I mean."
    s "We can’t patch things up. That doesn’t work for me. I take these things and hold them inside forever. Ask the others I’ve hurt. You’ll forgive me long before I forgive myself."
    ka "All you need to do is come upstairs."
    s "I can’t."
    ka "I know."

    play sound "static.mp3"
    scene karincarry22 with flash
    stop sound

    ka "Because you’re a coward."
    ka "I’m not asking you to tell them what you did to me — just to come face to face with them like a man. Introduce yourself. See that not {i}everything{/i} revolves around you."
    ka "But if you were to do that, it’d become too real...wouldn’t it?"
    ka "You can’t face them because you want to keep up the illusion that this is all some sort of fantasy. You want me to forgive you on my own because you think that’s just what I {i}do.{/i}"
    ka "I’m sorry, though...because that’s just not true."
    ka "If you {i}really{/i} want to earn my forgiveness, I need you to show me that you {i}want{/i} it. And if you’re not going to risk {i}your{/i} safety for me...why should I risk {i}mine{/i} for you?"
    s "I can’t meet your parents, Karin. I just..."
    s "I can’t."

    scene karincarry23
    with dissolve

    ka "Coward."
    s "I’m not disagreeing with that at all. It doesn’t change the way I feel, though."
    ka "On the bright side, at least I get to see your conscience in action this time. Watching you feel guilty and bad is rewarding in its own way."
    ka "But if you want me back..."

    play sound "static.mp3"
    scene karincarry24 with flash
    stop sound
    $ renpy.pause(15, hard=True)
    scene karincarry25
    $ renpy.pause(8, hard=True)

    scene black
    stop music

    $ renpy.end_replay()
    $ karin_love += 1
    $ karinspring5 = True
    $ forgetmenot = True
    $ renpy.pause(5, hard=True)

    jump karinspring6

label karinspring6:
    play sound "static.mp3"
    scene sistermassage1 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    "We cut to the interior of the Kanda family apartment several hours later — where both Kanda daughters are seated in different positions on the couch, meant to emphasize their respective mental states."
    "The youngest daughter was wide open, the way she always is. Her feet dangled in the air like the hands of a corpse hanging off the twin-size bed of a necrophiliac deep in the act of persistent postmortem coitus."
    "Her sister, on the other hand, took up a more reserved posture — hugging her knees with both arms in a way that didn’t just allow her to use them as a pillow, but made her feel more comfortable and protected."
    "She didn’t think her little sister was going to rape her, though — so she wasn’t really sure just what she {i}was{/i} protecting herself from at the moment."
    "Thoughts, perhaps? Did she fear that the man she encountered earlier would return after misinterpreting her final line? No. That was unlikely. She probably won’t see him again for another several weeks."
    "Yet she mourned his absence from the halls of her school. The way she used to look over her shoulder before turning every corner to try and spot him somewhere. "
    "He’d seldom spot her back. In fact, she’d seldom spot him at all. But every time she {i}did,{/i} it made her heart skip a beat. And it still skipped some nights, but she hated that it did that. "
    "She {i}hated{/i} that it did that, and she hated it because it meant she was right about something. She was right about how some things are too good to be true, and he was always one of them."
    "He wasn’t kind or caring. He wasn’t attentive. He didn’t like the things she did and had spent way too much time with the {i}other{/i} girl on the couch. There was never really anything good about him at all."
    "His flaws were so evident now — and all it took was a brush with death to pry the blindness from her eyes and change everything. "
    "She wished it would all change back, though. And somewhere it did — but that somewhere was not here, for this wish had already been made. "
    "And all that was left to do was sit here hugging her knees while waiting for the couch to swallow her whole."

    ki "Is it just me, or is Tom Holland, like...weirdly hot?"
    ka "Hot? I didn’t think he’d be your type at all."
    ki "I don’t really have a type. I see beauty in everyone, I think. Just, in his case, I want him to take me to his room and-"
    ka "Kirin, stop."

    scene sistermassage2
    with dissolve

    ki "Stop what? I was just gonna say “read me a bedtime story and pat my head.”"
    ka "Oh...Sorry. "
    ka "You’re usually more...abrasive than that."
    ki "Everything okay? You’ve seemed a little off all night."

    scene sistermassage3
    with dissolve

    ka "You’re...actually asking?"
    ki "Yeah. I’m good Kirin now. I’ve decided to switch personalities."
    ka "You can just...do that?"
    ki "It helps not having any idea what your identity is or even what you like. So you’d probably struggle with it."

    scene sistermassage4
    with dissolve

    ka "Mm...darn it. That’s exactly what I want right now too."
    ki "What do you mean? What could perfect, beautiful, wonderful Karin Kanda possibly want to change about herself?"
    ka "I wish I was less nice."

    scene sistermassage5
    with dissolve

    ki "Um...{i}why?{/i}"
    ka "It makes me weak..."
    ka "I keep feeling bad about stuff I {i}shouldn’t{/i} feel bad about and everything would be so much easier right now if I just...knew how to hold a grudge."
    ka "I don’t {i}want{/i} to be thinking about second chances. I want to just move on. But I keep second guessing myself and I just feel...like {i}I’m{/i} doing the wrong thing when deep down, I know I’m not."

    scene sistermassage6
    with dissolve

    ki "Hm..."
    ka "I’m sorry if none of that made sense. I’m just really confused right now. But thank you for asking, Kirin. It helps."
    ki "You know...this is kind of annoying."
    ka "Yeah, I knew you wouldn’t like talking to me. But I’m grateful you tried anyway."

    scene sistermassage7
    with dissolve

    ki "Not that. Just you and Noriko are, like...weirdly identical when it comes to this whole “sit back and sulk” stuff. And it’s annoying because I wish you two would just do what you want for a change."
    ka "But what I want is to not feel bad about being mean and every time I’m mean, I just...feel bad. Obviously."
    ki "Then just don’t be mean. Problem solved. That sort of thing doesn’t fit you anyway."
    ka "But if I’m not mean, how am I supposed to...keep people away from me?"

    scene sistermassage8
    with dissolve

    ki "You coooould...file a restraining order?"
    ka "No...I’d rather keep this private. I don’t even want to get {i}you{/i} involved. I just feel like I’m going to explode if I don’t {i}try{/i} to talk about it, though."
    ki "Well, you can tell me whatever you want. And I’m not going to, like...ridicule you or...get anyone else involved if that’s what you’re worried about."
    ka "It’s not...but thank you again."
    ki "Karin, chances are I probably already {i}know{/i} what this is about right now. So if you just come out and say it-"
    ka "No."
    ka "I just need to...stop being so weak...and stick to my guns."
    ki "..."
    ka "I always...{i}think{/i} I’m doing a good job. "
    ka "But then every time I walk away, there’s this...feeling in my chest that, like...stays with me for the rest of the day. It spills into the next day too sometimes. "
    ka "And if that’s going to happen every single time, maybe it would make sense to just, like...stop caring about it?"

    scene sistermassage9
    with dissolve

    ki "You know what would help with that?"
    ka "Please don’t say soup. It’ll only make things worse."
    ki "A massage."

    scene sistermassage10
    with dissolve

    ka "That’s not soup at all."
    ki "It’s certainly not."
    ka "You can’t even eat that."
    ki "Just let me rub your shoulders. I used to do it all the time at soccer practice. And I’m still new to this whole “caring” thing, so I’m not really sure what else to do for you right now."
    ka "Will you really do that for me?"
    ki "Of course. I’d say you’ve earned it after being nothing but nice to me from the moment I was born. "

    scene sistermassage11
    with dissolve

    ka "Then...okay."

    scene black
    with dissolve2

    ka "But if your hands get tired or you get bored and want to watch TV again-"
    ki "You know, this would be a really good opportunity for you to just shut up and stop trying to be so nice."
    ka "But you’re my sister. I could never {i}not{/i} be nice to-"

    play sound "static.mp3"
    scene sistermassage12 with flash
    stop sound

    ka "Aaaaah..."
    ki "Yup. Just like that. Can’t be nice if you’re lost in ecstasy."
    ka "What was I...about to say again?..."
    ki "Something about how much you love your little sister, I think."

    scene sistermassage13
    with dissolve

    ka "Mmm.......yeaaaaah.......I love you, Kirin......"
    ka "I’m glad you’re......a good girl now.......I alwaaaays knew you......had it in youuuu......"
    ki "You’re a good girl too, Karin. {i}Too{/i} good sometimes, as I’m sure you know. Which is why I think it’s cute that your main dilemma now is just “how can I be more mean?”"

    scene sistermassage14
    with dissolve

    ka "It’s......something else, actually.......but......it can.....wait for another time......"
    ki "Yeah. But on the off chance you ever {i}do{/i} want to open up a little more about it-"
    ka "Slower..."

    scene sistermassage15
    with dissolve

    ki "On the off chance you ever {i}do{/i} want to open up a little more about-"

    scene sistermassage16
    with dissolve

    ki "Um..."

    scene sistermassage17
    with dissolve2

    ki "Uhh...what was I...about to say?..."
    ka "Something I.......don’t want to......involve you in....."
    ki "R-Right. Yeah. Tired. Sorry."
    ka "You can stop if you want.....I don’t want to keep you awake if-"
    ki "I’m fine, okay? This isn’t about me, this is about you. And I’m going to help you relax no matter {i}how{/i} I...have to do it..."
    ka "You’re doing great......already......"
    ki "A...Am I?..."
    ka "Yeah......"
    ka "That feels.....{i}really{/i} good....."

    scene sistermassage18
    with fade

    ki "You...really...think so?"
    ka "M...hm....but you can...go a little harder...if...that’s okay..."
    ki "Harder...yeah..."

    scene sistermassage19
    with dissolve

    ki "You mean like-"
    ka "Mm! Yes! Right there!"

    scene sistermassage20
    with dissolve

    ki "(Screaming internally, horny, and ashamed)"
    ka "You really are.....good at this....."
    ki "(Screaming internally, horny, ashamed, and happy)"

    scene sistermassage21
    with fade

    ka "We should...do things like this...more often..."
    ki "You mean, like...t...touch...each other?"
    ka "Spend time...together..."
    ki "R-Right! Yes. Those are the words I meant to speak from my mouth."
    ka "I feel like I...barely see you anymore..."
    ka "Ever since...the soccer club disbanded...it feels like you’ve been getting further...and further away..."
    ka "I miss you, Kirin...and I love you..."

    scene sistermassage22
    with dissolve

    ka "I’m really happy you’re my-"

    play sound "static.mp3"
    scene sistermassage23 with flash
    stop sound

    ka "Kirin?"
    ki "Mhm?!"
    ka "Is everything okay?"
    ki "Mhm! Why?!"
    ka "Your face is beet red and you’re gritting your teeth."

    scene sistermassage24
    with dissolve

    ka "Let me feel your forehead. If you’re getting sick, I-"

    scene sistermassage25
    with dissolve

    ki "No! Definitely not! I’m fine! No need to do that!"
    ka "Uhh...are you {i}sure{/i} you’re-"
    ki "Yes! "

    scene sistermassage26
    with dissolve

    ki "I just...um...t...totally forgot I still have homework to do, so-"
    ka "Go do that, then. That’s way more important than my problems."

    scene sistermassage27
    with dissolve

    ki "It’s...definitely {i}not.{/i} But..."
    ka "It’s fine. I wanted to take another bath anyway. It’s easier for me to think in there."
    ki "A bath..."
    ka "I can wait until you’re done with your homework if you want to take one together. We did it all the time when we were little. Do you re-"

    scene sistermassage28
    with dissolve

    ki "Maaaaybe another time! Loooots of homeworks. Lots of...prooooblems. And words. Word...math problems...you know how it is!"
    ka "Do you want coffee? I can make-"

    play sound "doorslam.mp3"
    with hpunch

    ki "{i}No thanks! I’m fine. Enjoy your bath!{/i}"
    ka "Huh..."
    ka "That was...{i}weird.{/i}"

    scene sistermassage29
    with dissolve

    ka "I’m sure it’s nothing, though!"

    play sound "static.mp3"
    scene sistermassage30 with flash
    stop sound

    "Karin Kanda, who had never fantasized about having a sexual encounter with her little sister, found herself in the bath — continuing to not fantasize about having a sexual encounter with her little sister."
    "Unfortunately, though, she was merely one text box away from recollecting a sexual encounter she {i}almost{/i} had with her teacher."

    play sound "static.mp3"
    scene sistermassage31 with flash
    stop sound

    ka "{i}Please...Sensei...don’t...{/i}"
    s "..............."

    "He was undeniably different that night. But the first thing on her mind was not to ask “Why?” "
    "In fact, that wasn’t even in the top ten thoughts she’d think. It was buried somewhere beneath questions like “Am I going to live?” and “How much will this hurt?” "
    "Even “Why didn’t I listen to my parents?” found its way in there. But “Why?” alone wasn’t something she’d ask until it all boiled over. Then again. And again. And again. Every day up to this one."
    "She always landed on a different answer, paying little mind to any excuse he’d try to come up with since she immediately distrusted him with every fiber of her being."

    play sound "static.mp3"
    scene sistermassage32 with flash
    stop sound

    "But there was {i}one{/i} moment in the midst of all of that where she, still fearing for her life, couldn’t help but fear for {i}his{/i} too — for she knew {i}something{/i} had gone off in his mind."
    "It was just easier to believe that it was him realizing how wrong his actions were than anything else she could have come up with."
    "Maybe it really {i}was{/i} an accident?"
    "Could she go back to liking him if it {i}was?{/i} Or did this single encounter completely destroy any opportunities she {i}would have{/i} had to make such a terrible mistake in the future?"

    s "......................."
    ka "............."
    ka "Please don’t hurt me."

    play sound "static.mp3"
    scene sistermassage33 with flash
    stop sound

    s "..."

    "And just like that, he was back to normal."

    scene sistermassage34
    with dissolve2

    s "Do you ever dream of me?"

    "She did."

    ka "Sensei..."
    s "You do...don’t you?"

    "She does."

    ka "Please...don’t do this..."
    s "What am I like there? Inside of your head."

    "Kind. Gentle. Smart. Caring. Different. Only one of which was still true now."

    s "Is it better or worse than who I am on the outside?"

    "Worse. A million times worse. And even {i}that{/i} could not begin to describe it. "

    s "And do you wish you could take me in?"

    "{i}Not like this.{/i}"

    play sound "static.mp3"
    scene sistermassage30 with flash
    stop sound

    "That was the last thought she could remember thinking before everything went dark."
    "It was like her mind shut itself off as a means of self-preservation — creating an unfortunate save state that she’d be forced to look at every time she wanted to load up some {i}other{/i} memory."
    "She kept coming back to this one, though...even when she didn’t want to."

    scene sistermassage35
    with dissolve2

    ka "..."

    "Why?"
    "{i}Now{/i} was a more ideal time to ask such a question. Because as she gazed down at her reddening face reflecting off the water, she knew it wasn’t from the heat alone. "
    "It was a million things. Curiosity. Hate. Lust. Betrayal. Admiration. Fear. Everything else — dumped into a blender and turned into a thick paste that tasted a little like lemon. Or maybe it was salt?"
    "Either way, it was a flavor she’d only heard of before. One that she was excited to try one day when the time was right."
    "Yet she was plucked from mundanity like a lobster from a pot — just to be dumped back in when the chef noticed she was still wriggling."
    "She was thankful nothing happened."
    "At the same time though, at least she’d know what to think if something {i}did.{/i}"

    ka "..."

    scene black
    with dissolve3
    stop music fadeout 12.0

    "Karin Kanda only touched herself once per month. "
    "Almost always in the bath because it made her feel less dirty."
    "But tonight — it felt like she was bathing in shit."
    "She finished what she needed to do, then hung her head over the toilet for ten minutes before putting her clothes back on."
    "It wasn’t pretty."
    "None of this is."

    $ renpy.end_replay()
    $ karinspring6 = True
    $ karin_love += 1

    "{i}Karin’s affection increases to [karin_love] because she’s naive and forgiving and you did this to her.{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
