label callsaraafternoon:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callafternoon
    if senseisad == True or sarablock == True:
        play sound "phonebeep.wav"
        "I tap on Sara's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't."
        jump callafternoon
    if saranumber == True and bar15 == False:
        "I think I should probably get to know Sara a little better before calling her."
        jump callafternoon
    if sara_love >= 0 and bar15 == True and saradate1 == False:
        jump saradate1
    if sara_love >= 10 and nikidate5 == True and sanadorm35 == True and saradate10 == False:
        jump saradate10
    if chap4active == True:
        jump saraspringnoongen
    if chapthreeactive == True:
        jump sarasummer2noongen
    if christmas7 == True:
        jump saranoongen2
    else:
        jump saragenafternoon

label saranoongen2:
    scene saranoongen2
    with dissolve
    play music "love.mp3"

    "Sara and I meet up somewhere between her bar and the[school] and decide to spend the afternoon walking around the city together."
    "She doesn't normally act like an adult, but her [teenager]-at-heart attitude rings even more true than usual when she's let out in the snow."
    "Every time I turn my head, she scoops up whatever she can find and turns it into a snowball before tossing it at my head."
    "I want to be annoyed, but her childish laughter each time it happens disables my anger-receptors and I must now freeze for the sake of her happiness."
    "Oh well. Worse things have happened, I guess."
    "I'm glad she's having a good time."
    "But she needs to watch her fucking back because I am a snowball-fighting champion."

    scene black
    with dissolve

    "I return the favor eventually and, instead of getting mad, Sara's eyes light up and she jumps into my arms."
    "She doesn't try to kiss me or anything like that."
    "She just looks into my eyes and smiles."
    "Then breaks apart."
    "And before I know it, the two of us part ways and are back on our own."
    "But not before making plans to do this again soon."

    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara's affection has increased to [sara_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label callsaranight:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callnight
    if senseisad == True or sarablock == True:
        play sound "phonebeep.wav"
        "I tap on Sara's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't."
        jump callnight
    if saranumber == True and bar15 == False:
        "I think I should probably get to know Sara a little better before calling her."
        jump callnight
    if bar15 == True and saradate1 == False:
        play sound "phonebeep.wav"

        "I press on Sara's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. She's probably busy at the bar."
        "Wait...how would she be {i}busy{/i} at the bar?"
        "Oh well. I'll just have to call someone else."
        jump callnight
    else:
        "Sara is at the bar right now. I should be able to spend time with her if I go there."
        jump callnight

label callsaramorning:
    if senseisad == True and saracamp2 == False:
        "I don't want to call her right now..."
        jump callmorning
    if senseisad == True or sarablock == True:
        play sound "phonebeep.wav"
        "I tap on Sara's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "She doesn't."
        jump callmorning
    if saranumber == True and bar15 == False:
        "I think I should probably get to know Sara a little better before calling her."
        jump callmorning
    else:
        play sound "phonebeep.wav"

        "I press on Sara's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's still asleep."

        jump callmorning

label sarainvite:
    if sarainvite1 == False:
        jump sarainvite1
    if sarainvite1 == True and sarainvite2 == False:
        jump sarainvite2
    if sarablock == True:
        play sound "phonebeep.wav"

        "I press on Sara's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer."

        jump callnight
    else:
        jump sarainvitegen

label sarainvitegen:
    play sound "phonebeep.wav"

    "I tap on Sara's name in my phone and wait for her to answer."
    "........."
    "......"

    play sound "phonebeep.wav"

    sar "Helloooo?"
    s "Hey. Are you free right now?"
    sar "Sure am! Want me to come over?"
    s "If you'd be so inclined."
    sar "Heheh~"
    sar "Give me a few minutes to get ready and I'll head over."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene sarainvitehub
    with dissolve
    play music "acoustic.mp3" fadein 3.0

    sar "Heya~"
    sar "Is it weird if I tell you I was thinking about you all day?..."
    sar "I'm up for anything, you know?"
    sar "Is there anything you want to do tonight?"

    "How should I spend my time with Sara?"
    menu sarainvmenu:
        "Hang Out (Raise Affection)":
            jump sarainviteaff
        "Doggystyle Sex (Raise Lust)" if sarasex == True and bonus == True:
            jump sarainvitedoggy
        "Missionary Sex (Raise Lust)" if sarasex == True and bonus == True:
            jump sarainvitemissionary
        "Hug Sana's Mom (Raise Lust)" if sarasex == True and bonus == False:
            jump sarainvitedoggy
        "Hug Her And Try To Make Her Pop (Raise Lust)" if sarasex == True and bonus == False:
            jump sarainvitemissionary
        "Headpat" if sarasex == True and bonus == True:
            jump saraheadpat

label sarasbar:
    if sara_lust >= 5 and sarasex == True and saralust5 == False:
        jump saralust5
    if sara_love >= 20 and sarasex == True and day271 == True and sanadorm40 == True and sarabar20 == False:
        jump sarabar20
    if sara_love >= 25 and yukidate10p2 == True and sarabar25 == False:
        jump sarabar25
    if sara_love >= 30 and saraspecial30p1 == True and sarabar30 == False:
        jump sarabar30
    if sara_love >= 35 and rikaspring1 == True and saraspring1 == False:
        jump saraspring1
    if sara_love >= 40 and sarasex == True and yukispring2 == True and saraspring2 == False:
        jump saraspring2
    if chap4active == True:
        jump saraspringbargen
    if chapthreeactive == True:
        jump sarasummer2bargen
    if christmas7 == True:
        jump sarabargen2
    else:
        jump sarabargen

label sarabargen2:
    scene sarabargen2
    with dissolve
    play music "calmbar.mp3"

    "I weather the cold to come spend time with my favorite alcoholic."
    "I don't know many alcoholics. In fact, I think Sara might be the only one, but I'm pretty sure she'd still be my favorite either way."
    "Why? Because she flirts with me and gives me discounts on alcohol."
    "Mix that with the fact that she is incredibly attractive and that there are no other males around and you have the recipe for a perfect bartender."
    "The night proceeds with the two of us becoming mutually inebriated and, before long, Sara is unable to hold herself up any longer."

    scene black
    with dissolve

    "I decide to be a good man and close the bar for her, carrying her upstairs and putting her to bed."

    if bonus == True:
        "She tries to get me to stay but, despite great temptation, I decide that she's too drunk for even {i}me{/i}- which is saying quite a lot."
        "I am not a man of ethics by any means, but I do not trust my ability to form an erection for a girl who can no longer even form proper sentences."
        "Sara passes out the second I reject her and, not having anything else to do, I finally start heading home..."

    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara's affection has increased to [sara_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sarabargen:
    scene saranightgen
    with dissolve
    play music "calmbar.mp3"

    "I decide to spend the night at the bar talking to Sara."
    "Sana is hanging out with Ayane tonight, so the two of us actually get to talk one-on-one for a change."
    "Of course, talking turns to flirting relatively quickly as Sara proceeds to not hold {i}anything{/i} back whatsoever."
    "I want to say that she wouldn't be acting this way if there were any other customers in the bar, but I'm starting to believe that might not be the case at all."

    if bonus == True:
        "And even though I can't quite figure out why she likes me as much as she appears to, I'm not about to deny the undivided attention of an adorable MILF."

    scene black
    with dissolve

    "Sara winds up drinking a bit too much during our conversation and starts dozing off before the bar is even shut down for the night."
    "I do her a favor and turn the sign outside to 'closed' and help carry her up the stairs and into bed."

    if bonus == True:
        "She invites me to sleep over and tries to take my pants off, but she's so drunk at this point that I can't bring myself to go any further."
        "Having been defeated by my own morals (Which apparently still exist), I tuck her into bed and begin the journey home..."
    else:
        "I then proceed to warm up some milk for her and tuck her in because I am kind and I want her to feel cherished."

    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara's affection has increased to [sara_love]{/i}!"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label saragenafternoon:
    scene saraafternoongen
    with dissolve
    play music "normalday.mp3"

    "Sara and I make plans over the phone to spend some time together in the city."
    "We meet in front of the same headquarters as our first 'date,' which has become sort of a landmark to us, and proceed to wander around the town looking for a place to get her boba tea."
    "I want to say I'm surprised at how [young]Sara acts despite having a [teenage]daughter, but I don't think anything about her would {i}really{/i} surprise me at this point."

    if bonus == True:
        "She's like a [teenage]girl trapped in an attractive mother's body...which might actually explain why I like hanging out with her as much as I do."

    scene black
    with dissolve

    "Sara winds up spotting some tea-shop she's never seen before and forces me inside of it."
    "She then {i}pretends{/i} to forget her wallet and I have to pay for her."
    "Things like this would piss me off coming from most people, but something about the way Sara does it makes it seem less malicious and more...endearing."
    "And so I buy her her stupid boba tea and the two of us walk around for another hour or so before heading home..."

    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara's affection has increased to [sara_love]{/i}!"
    "........."
    "......"
    "..."

    jump saturdaynight

label saradate1:
    "I guess it wouldn’t hurt to give Sara a call. "
    "I’ve been meaning to get to know her a little better, and it’s not like I have anything else planned for the day."

    play sound "phonebeep.wav"

    "I pull my phone out of my pocket and press on her name in my contacts."
    "It rings a few times before she finally decides to answer."

    play sound "phonebeep.wav"

    sar "Helloooo? Who's this?"

    "Oh, right. I never gave her my number."
    "I just plugged hers into my phone after she wrote it on a receipt that one night and have been leaving it alone ever since."

    s "It’s your daughter’s teacher. What are you up to right now?"
    sar "Oh, hey! I was starting to think you’d never call me."
    sar "I’m just setting up the bar right now. Why?"
    s "I’m looking for something to do and was wondering if you’d want to go out."
    sar "Like, now? Tonight? "
    s "Yeah. But if you have to set up the bar, it’s-"
    sar "No no no no! I’d love to hang out. I can just have Sana finish setting up when she gets here."
    sar "I’ll tell her I went out to buy groceries or something."
    s "Are you sure that’s okay?"
    sar "Of course! Is there anywhere you’d want to meet?"
    s "Let’s just walk around the city or something. I’ll text you an address and we can meet there in around an hour."
    sar "Sounds good! See ya soon~"

    play sound "phonebeep.wav"

    s "..."

    "It is just then that I realize I don’t know the address of any specific place in the city."
    "..."
    "I guess I’ll just have to look up a random building and have her meet me there."

    scene black
    with dissolve

    "I take a few minutes to research notable locations in the urban district of Kumon-mi and,
    after finding one rather large looking building, decide on that as our meeting spot."
    "........."
    "......"
    "..."

    scene saradate0
    with dissolve
    play music "normalday.mp3"

    "I show up in the designated spot before Sara, which is a good sign. "

    if bonus == True:
        "Obviously, the two of us aren’t formally dating or anything like that, but it still feels good to have done something right by today’s standards."
        "I’ve gotten so used to letting my immoral side take over that small things like showing up on time to a date are all that’s left to make me feel like a good person."
        "And if Sara were a character in an anime, I’m sure she’d be just as impressed as I am with myself right now."
    else:
        "I don't go into the city by myself often, so I was very worried that I was going to get lost and be abducted by a stranger."

    scene saradate1
    with dissolve

    sar "Hey there, stranger~"
    sar "Did I keep you waiting long?"

    "This is the part where the guy normally says “No, not at all,” despite arriving half an hour early or something along those lines."
    "Just, in this case, I really {i}did{/i} just arrive a few minutes ago."

    s "Nah. I just got here myself."

    scene saradate2
    with dissolve

    sar "Awe~ You’re not just saying that to make me feel bad about being a little late, are you?"
    s "I’m not. I really did just get here."
    sar "Right, right..."
    sar "Well, I guess I’ll play along if it’ll make you happy."

    scene saradate3
    with dissolve

    sar "Would you, uhh...mind explaining why we’re meeting in front of {i}this{/i} place,
    though? This isn’t really a typical meeting spot."

    "I turn to the side to see that we're in front of the headquarters for some unfamiliar cell phone company. "

    if bonus == True:
        s "Uh...Nothing turns girls on quite like...multi-billion dollar corporations, right?"

        scene saradate4
        with dissolve

        sar "Woooow. Who is it that spilled the secret to a woman’s heart to you, [saramaster]?"
        s "Just something I picked up over the years, Sara."
        sar "I can tell. I’m so horny now. Please make love to me beneath the giant 5G banner towering over us."
        s "I’m afraid I can’t. 5G Causes cancer and I couldn’t possibly do that to someone as beautiful as you."
        sar "If it’s for you, [saramaster], I’d let you do me under {i}6G{/i}."
        s "..."
        sar "..."
        s "This is possibly the strangest flirting exchange I’ve ever been involved in. I feel like I should apologize."
    else:
        s "I am sorry. This is a terrible date. Feel free to leave now."

    scene saradate5
    with dissolve

    if bonus == True:
        sar "No! Don’t apologize! That was totally fun."
        sar "It made me feel [young]again."
        s "Aren’t you only like 30? That’s still really young."
        sar "I guess by mom-standards, yeah. But I’m no [teenager] anymore, that’s for sure."
    else:
        sar "No, no! It's totally fine. I like cell phones and I like you."

    scene saradate6
    with dissolve

    sar "So please continue to flirt with me~ I would very much appreciate that."
    s "That I can do, Sara. That I can do..."

    scene black
    with dissolve

    "The two of us wind up walking around the city for about an hour or so, stopping at a few convenience stores along the way to buy Sara candy."
    "Yes, apparently she really likes candy. And I mean {i}really{/i} likes candy."
    "In fact, she’s almost like a little kid any time we pass a store that sells chocolate."
    "I even needed to talk her out of going into a few of them given just how many shops there are around here that sell things like that..."

    scene saradate7
    with dissolve

    sar "Wow. We’ve been together almost a full hour and you’re not bored of me yet."
    sar "Maybe we {i}are{/i} meant to be together after all."

    if sarasex == True:
        if bonus == True:
            s "Well, it’s not like we haven’t already {i}been{/i} together, if you catch my drift."

            scene saradate8
            with dissolve

            sar "Not like that, perv! I meant like, you know, as a {i}thing{/i}."
            s "Like...friends with benefits?"
            sar "No! Like..."
            sar "Like I could be your girlfriend. Or something."
            s "This is the first “date” you and I have gone out on and you already want to be my girlfriend?"
            s "Doesn’t that seem a little premature?"
        else:
            s "Well, it’s not like we haven’t already hugged, so..."
            sar "I'm gonna poke your face now."
            s "What? Why? That's entirely unnecessary."

        scene saradate9
        with dissolve

        sar "Whaaaat? No way! I don’t think so at all."
        sar "I mean, you seem pretty tolerable of me and stuff. And you’re cute."
        s "Sara. Why are you poking my face?"

        scene saradate10
        with dissolve

        if bonus == True:
            sar "Oh, and your penis is super big and I don't think I could ever go back to a normal size one now~"
            s "Sara. Hands. There’s an entire family like ten feet away from us."

            scene saradate9
            with dissolve

            sar "Sorry. Heheh~"
            s "You’re still poking me..."
            sar "What’s wrong with a little poking? Am I not allowed to have fun on my day off?"
            s "This isn’t your day off. You just pawned work off on your daughter so you could hang out with me."
        else:
            sar "I heard somewhere that there is a special pressure point inside of the face that can force someone to fall in love with you when poked."

        scene saradate11
        with dissolve

        sar "And I wouldn’t have done that if I didn’t want you to be my new boyfriend."

        "Okay, so...I know Sara and I are close to the same age. And dating in our age group is a lot different than it is when you’re a [teenager]."
        "But even by those standards, she’s still coming on strong."
        "Either she’s incredibly lonely, or she just really {i}really{/i} likes me for some reason beyond my comprehension."

        s "Let’s just...hang out a few more times before committing to anything, okay?"

        if sarainterest == True:
            sar "Why?~ Haruka already told me you like me. Don’t you wanna make sure no other handsome teacher can come sweep me away?"
            s "I’m pretty sure I’m the only male teacher in the[school], so I don’t think that will be an issue."

        else:
            sar "Boo~ You’re no fun, [saramaster]."

        sar "I guess if you’re not ready to date, though, that’s fine. I get it."

        scene saradate12
        with dissolve

        sar "We both have other people that are important to us that we should focus on."
        sar "I have my daughter...You have your [niece]..."
        sar "And I can’t imagine they’d feel normal about becoming related all of a sudden."
        s "Yeah, I can’t imagine that e-"
        s "Wait, related? I thought we were just talking about dating."

        scene saradate7
        with dissolve

        sar "For now. Heheh~"
        s "..."

    else:
        s "I..."

        "I think back to when I turned Sara down in her apartment a while back."
        "I still don’t fully understand what it was about that situation that made me say no to her, but..."
        "I can’t help but wonder if that’s had any sort of impact on how she sees me?"
        "Judging by the flow of the conversation so far, it certainly doesn’t feel that way."
        "But...oh well. I guess it’s just part of human nature to wonder about things like this."
        "I’m sure it’s no big deal."

        s "Are you sure you’d even want to date someone like me?"

        scene saradate13
        with dissolve

        sar "Are you sure you {i}wouldn’t{/i} want to date someone like me?"
        sar "Because if you’re thinking I’m the type who just throws herself at everyone...I’m really not."
        sar "I just...kind of feel comfortable with you for some reason."

        scene saradate14
        with dissolve

        sar "But I know you’re not realistically thinking of me that way, so we can just move on. I’m
        sorry for taking the joke too far."

    scene saradate14
    with dissolve

    sar "Um, all that stuff aside, I’ve actually been wondering something lately."
    sar "You know how you’ve been coming to the bar a lot?"
    sar "Is there anything you think I should be doing that I’m not already doing?"
    sar "The place is going downhill fast and I’m not really sure how long I can keep going at this rate."
    s "What makes you think I know anything about running a bar?"
    sar "Nothing at all! But from a customer’s perspective, you seem to keep coming back. And
    I doubt it’s just because of my daughter and me."
    s "..."
    sar "..."
    s "..."

    scene saradate15
    with dissolve

    sar "Wait a second! It {i}is{/i} because of my daughter and me!"
    s "I thought that was pretty obvious..."

    scene saradate16
    with dissolve

    sar "Ugh! I’m doomed after all!"
    sar "We were fine until all of the men started disappearing, but now it's like we're imploding or something!"
    sar "I can’t rely on our cute faces to keep the place open, can I?!"
    s "I’m sorry to stray away from the topic at hand, but that face makes you look a lot more like Sana than normal."

    scene saradate15
    with dissolve

    sar "She’s my daughter! Of course we look alike!"
    sar "Now, back to talking about the bar! "
    sar "What should I do to make it better?!"
    s "I am {i}not{/i} qualified to answer this question. I’m not even qualified to help
    Sana with her social skills and I’m somehow doing that."
    s "I’ve pretty much exhausted my ability to help."

    scene saradate17
    with dissolve

    sar "Well..."
    sar "Can you at least keep coming by and spending lots of money then?"
    s "..."
    sar "Pleeeeeeeease?"
    s "I was never going to stop in the first place..."

    scene saradate18
    with dissolve

    sar "Yay! More time with [saramaster] and more money for rent! You’re officially my favorite customer!"
    s "Well, thanks. But at least wait until you have a few more to give me that title. It feels kind of meaningless as-is."
    sar "Nope. Title’s all yours. No refunds. Sorry~"

    scene saradate19
    with dissolve

    "The conversation suddenly comes to a halt as Sara’s excitement turns into a mix between
    what seems like appreciation and admiration. "

    sar "Um..."
    sar "I had a really good time today."
    sar "We can...do this again, right?"
    sar "I really don't want this to be like...a one time thing."
    s "Sure. I had fun too."
    s "How about I just call you the next time I’m free and we do something again then?"
    sar "...Yeah."
    sar "Yeah, I’d like that a lot..."

    scene black
    with dissolve2

    "The two of us get off the bench a few minutes later and begin the journey home."
    "We wind up splitting apart near the halfway point so neither of us are forced to walk in the direction opposite our respective homes."
    "Sara returns to the bar, while I return home to grab a change of clothes and something to eat..."
    "All things considered, today was a good day."
    "Sara is certainly...{i}fun{/i}, if not anything else..."

    $ renpy.end_replay()
    $ sara_love += 1
    $ saradate1 = True
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label saralust5:
    scene sarafirstlust1
    with dissolve
    play music "calmbar.mp3"

    "I show up at the bar to find both Sara and Sana waiting behind the counter with nothing to do."
    "Obviously, this has become par for the course here. But it still seems depressing enough for me to point out any chance I get."

    sar "Well, well, well. If it isn't my favorite customer."
    sa "It's...not like we really have another choice..."

    scene sarafirstlust2
    with dissolve

    sar "That’s not true! Haruka shows up every once in a while."
    sar "Oh! And there’s also that group of old ladies who sit in the back of the room and drink a disturbing amount of whiskey."
    s "Sorry for asking, but would you mind telling me exactly what constitutes a “disturbing amount” of whiskey?"

    scene sarafirstlust3
    with dissolve

    sar "Sure. But only if you promise to try and one-up them so I can pay this month’s rent."
    s "You mean to tell me your ability to pay rent depends entirely on how much whiskey I consume tonight?"
    sar "If you'd prefer to just {i}give{/i} me the money instead of getting alcohol poisoning, I'd accept that too."
    sar "Any contribution you make gets me one step closer to keeping my bed so I don't wind up in my daughter's after getting evicted."

    scene sarafirstlust4
    with dissolve

    sa "Wait...what?..."
    sa "You’re not...seriously going to move into my dorm room if that happens...are you?"
    sar "Sana! You wouldn’t let your mother go to sleep on the street would you? I raised you better than that."
    sa "But I...also don’t want to sleep in the same bed as my mom..."
    sar "Why not? We slept in the same bed all the way up until you were-"

    scene sarafirstlust5
    with dissolve

    sa "So...Sensei! Umm...how are you doing today?"
    s "I’m good, Sana. Thanks for asking."
    sar "Oh no! Is my little girl all grown up now?! Am I no longer good enough for her?!"
    sar "This is a mother’s worst nightmare!"
    sar "I have feelings, Sana! I have feelings and you are hurting them!"
    sa "Don’t listen to her...She...doesn’t actually have feelings..."
    sa "And she’s...not allowed to sleep in my bed..."

    scene sarafirstlust6
    with dissolve

    sar "Hmm...Well, if that’s the way things are going to be, I guess I’ll just have to find another bed to sleep in."
    sar "You wouldn’t happen to know of any openings...would you, Sensei?"
    sa "Umm...Mom?..."

    scene sarafirstlust7
    with dissolve

    sar "Sana."
    sa "What...are you doing?..."
    sar "Searching for a backup plan for when I get evicted because your teacher won’t buy our entire stock of whiskey."
    s "I don’t really need to buy it all at once, do I?"
    sar "You do if you care about me."
    s "I mean..."
    sa "Wait...um...maybe..."
    sa "Maybe I can ask Ayane...if it’s okay for you to stay with us..."

    scene sarafirstlust8
    with dissolve

    sa "Is there, umm...a rule against that...Sensei?"
    s "Sana, if there are rules about proper dorm room conduct, I can assure you that I am the absolute worst person to ask."
    sa "I don’t...really know what you mean by that..."
    sa "But I’m going to tell Ayane anyway..."
    s "Don’t worry about it. I’ll make sure your mom has a place to stay if she gets kicked out."

    scene sarafirstlust9
    with dissolve

    sa "Why would you say that?! That makes me worry even more!"
    sa "I...have to talk to Ayane!"
    sa "I’ll...I’ll be right back!"

    scene sarafirstlust10
    with dissolve

    sar "..."

    "Sana quickly pulls her phone out of her pocket and darts out of the bar into the street, leaving me alone with a now-blushing Sara."

    s "..."
    s "Listen, I was just-"
    sar "You...know I was just kidding, right?..."
    sar "I couldn't possibly ask you to do something like that for me..."
    sar "Did you...really mean that?"
    s "I can't guarantee my niece would be okay with it, but it's not like I'd let you just sleep on the street when I have a perfectly good house."
    sar "Thank you so much, but..."
    sar "I’ll figure something out. I always do."

    "I instinctively reach for my wallet to check how thick it is, knowing full well that I may have to spend a little more money here from this point on."

    scene sarafirstlust11
    with dissolve

    sar "I’m really surprised that Sana agreed to my suggestion that quickly, though. "
    sar "She must...{i}really{/i} not want me spending any more time with you."
    sar "Could it be that my daughter finally has her first crush?"

    scene sarafirstlust12
    with dissolve

    sar "And on the same boy as me...You know, I always thought my life was a little like a soap opera."
    sar "Either that or I'm just younger than I thought I was."

    "{i}Or{/i} Sana’s tastes are just a little bit more mature than they should be..."

    sar "Hey...How long do you think she’ll be gone for?"
    s "Sana? Isn’t she just making a phone call?"
    sar "Mhm. But who knows how long that could take? The reception over here is hooooorrible. It could be {i}days.{/i}"
    s "I highly doubt the reception here is that bad, but since I think I know where you're going with this, I'm going to pretend it is."

    scene sarafirstlust13
    with dissolve

    sar "Oh?..."
    sar "Could it be we have our minds on the same thing?..."

    "I obviously know where this is heading."
    "It seems kind of dangerous to initiate this when Sana is going to be back any moment, though."
    "But maybe..."
    "Maybe I can do something to satisfy {i}her{/i} before we’ve been gone “too long...”"

    s "I know that look, Sara."
    sar "What look? I don’t have a look."
    s "You most certainly do have a look."
    sar "Do I?"
    s "You do."
    sar "Hmm..."
    sar "Well if I {i}do{/i} have the look I think you’re talking about, I can’t imagine Sana would be happy to see it."
    sar "If only we had somewhere close by that we could sneak away t-"

    scene sarafirstlust14
    with dissolve

    sar "Oh, wait! How silly of me! I just remembered that I live right upstairs!"
    s "Wow. What a convenient turn of events that is."

    scene sarafirstlust13
    with dissolve

    sar "We can be quick...right, Sensei?~"
    s "We’d have to be {i}very{/i} quick."
    sar "Maaaaybe...if you carry a case of beer downstairs when we're done, I can tell Sana you were helping me with bar stuff?"
    s "And if she comes upstairs?"

    scene sarafirstlust15
    with dissolve

    sar "If she comes upstairs, I guess I’ll just have to keep quiet, won’t I?"
    s "Is that something you think you’re capable of? Because you’re normally pretty loud."
    sar "Heheh~"
    sar "Let’s hope we don’t have to find out..."

    scene black
    with dissolve2

    if bonus == True:
        jump sarafirstlustx
    else:
        "Despite Sara being a very loud hugger, the two of us are able to walk up the stairs and hug without being heard."
        "It's awesome and I enjoy it."
        "Sara likes it too and compliments how good I am at hugging."
        "I hope Sana doesn't find out about this."

        $ renpy.end_replay()
        $ saralust5 = True
        $ sara_lust += 1
        stop music fadeout 5.0

        "{i}Sara’s lust has increased to [sara_lust]!{/i}"
        "........."
        "......"
        "..."

        if day > 5:
            jump endofsat
        else:
            jump endofweekday

label saraeatoutanim:
        scene black
        with dissolve
        play music "calmbar.mp3"
        play sound "dooropen.mp3"

        "I head over to Sara's place and drop several hints at wanting to go upstairs."
        "Thankfully, Sana isn't around to question us today, so she closes up the bar early and eagerly drags me upstairs by the wrist."

        if bonus == True:
            "As soon as we enter her bedroom, I push her down and slide off her pants..."
            jump saraeatoutanimx
        else:
            "As soon as we enter her bedroom, I push her down and gently hug her."

            $ sara_lust += 1
            stop music fadeout 4.0

            "{i}Sara's lust has increased to [sara_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label sarainvite1:
    play sound "phonebeep.wav"

    "I tap on Sara’s name in my phone and wait for her to answer."
    "I figure that the two of us know each other well enough at this point that it won’t really be weird for me to invite her over."
    "Sure, I don't really know what Ami will think about an older woman randomly showing up at the house, but I’m the one who’s paying the bills."
    "I’ll invite whoever I want over."
    "This is what it means to be an adult."

    if invitetip == False:
        call invitetip from _call_invitetip_2

    scene noonsky
    with dissolve
    play sound "phonebeep.wav"

    sar "Hellooo~ Sensei?"

    play music "normalday.mp3" fadein 10.0

    s "Hey. What are you doing tonight?"
    sar "Oh, you know. Just drinking half of my stock since no one else ever wants to show up."
    sar "Do you want to come over and keep me company?"
    s "Actually, I was wondering if {i}you{/i} wanted to come over for a change."
    sar "What, you mean like, to your place?"
    sar "Is that really okay?"
    s "Sure. I come to the bar all the time. I figure it’s about time for you to see where I live."
    sar "Oh my God! Yeah! Definitely!"
    sar "I-I’ll have Sana take over for me and I'll head right over."
    sar "I’m so excited. I was starting to think you were ashamed of me and didn’t want your [niece] knowing that we hang out and stuff."
    sar "Am I sleeping over? Do I need an overnight bag?"
    s "Hey, now. Slow down. "
    s "It’s one thing to invite you over, but I’m pretty sure Ami would kill both of us in the middle of the night if you stayed over your first time here."
    sar "Oooooh, right. Right. Okay!"
    sar "Can you send me the address? I’ll meet you over there as soon as I can."
    s "Sure thing. See you soon."

    play sound "phonebeep.wav"

    "I hang up the phone and quickly type out my address before sending it to Sara."
    "It will be her first time seeing the place and I’m pretty sure Ami will be around tonight."
    "All I can really hope is that the two of them manage to get along."

    scene black
    with dissolve

    "Sara, I’m obviously not worried about. "
    "She has a daughter, so she clearly knows (At least to some extent) how to deal with [young_girls]."
    "Ami, on the other hand..."
    "Well. I guess I’ll just have to wait and see."
    "........."
    "......"

    play sound "doorbell.mp3"
    "..."

    s "Come in."

    play sound "dooropen.mp3"

    "..."

    scene sarafirstinvite1
    with dissolve

    "I’m in the kitchen when Sara lets herself in."
    "She immediately comes to meet me at the counter and props herself up on it using her elbows."
    "She doesn’t say anything, just smiles at me and waits for me to talk."

    s "Uhh, welcome to my house, I guess."
    sar "Thank you so much for having me."
    sar "What are you making me for dinner?"
    s "...I'm sorry. What?"
    sar "You {i}are{/i} making me dinner, aren't you?"
    s "I...didn’t plan on it?"

    scene sarafirstinvite2
    with dissolve

    sar "You invited a girl over and aren’t going to make her dinner? I thought your manners were better than this."
    s "Trust me, you wouldn’t want me making you dinner in the first place. I can barely cook an egg."

    scene sarafirstinvite3
    with dissolve

    sar "It looks like the two of us would have to order out quite often if we ever moved in together."
    s "A - It’s way too early to be talking about moving in together."
    s "B - You can’t cook either?"

    scene sarafirstinvite4
    with dissolve

    sar "I can use a microwave pretty well."
    sar "Sana ate nothing but chicken nuggets until she was seven, so I’ve memorized the cooking times for like twenty different brands."
    s "I don’t know whether to be impressed or abhorred that you would allow your child to live off of nothing but microwaved chicken nuggets for so long."

    scene sarafirstinvite3
    with dissolve

    sar "Hey, she turned out okay, didn’t she?"
    sar "I have the cutest daughter in all of Kumon-mi. And she’s somehow still super tiny despite her diet."
    s "Well that’s obviously genetic. You’re pretty small yourself."

    if bonus == True:
        sar "I’m fun-size. Easier to lift up and have your way with."
        s "Are you already trying to seduce me? You’ve been here for five minutes."

        scene sarafirstinvite5
        with dissolve

        sar "Worried your [niece] will come home and catch us?"
        s "Kind of, yeah. She’ll be home any minute."
    else:
        s "Just like my accountant."

    scene sarafirstinvite6
    with dissolve

    sar "Oh, how is she going to feel about this, by the way?"
    sar "Won’t it be a little weird for her to come home and see you talking to some woman she’s never met before?"
    sar "I’m sure you at least warned her in advance, right?"
    s "Nahh. Ami is mature enough to handle being thrown into the fire every now and then."
    s "She’ll probably freeze at first, but I’m sure she’ll warm up to you in no time at all."

    scene sarafirstinvite7
    with dissolve

    sar "You really think so?"
    sar "Maybe I’ll have a second daughter before I know it?..."
    s "That...is not what I meant."

    play sound "lock.mp3"
    scene sarafirstinvite8
    with dissolve

    a "I’m home!"

    "The sound of the door unlocking quickly breaks up our conversation as we fix our eyes on the door."
    "The moment of truth approaches."

    sar "Oh God. That’s her, right? Do I look okay?"
    s "Why are you more focused on impressing my [niece] than me?"

    if bonus == True:
        sar "I already know you like me. I need to make her like me next and I’ll be basically guaranteed a spot in this family."
        s "Sara, that isn’t how families work."
    else:
        sar "I already know you like me. I need to make her like me next and I’ll be basically guaranteed a spot at her accounting firm."
        sar "You know, since the whole bar thing obviously isn't working out."

    play sound "dooropen.mp3"
    scene sarafirstinvite9
    with dissolve

    a "..."
    s "..."
    sar "..."
    a "..."
    s "Welcome home."
    sar "Hi! You must be Ami. Your [uncle]’s said so much about you."

    "No, I don’t think I have."

    a "..."
    s "How was[school]?"
    a "..."
    sar "..."
    a "I think I might have opened a door to the wrong dimension."
    a "I’m going to leave and come back in and I’m sure everything will go back to normal."

    play sound "dooropen.mp3"
    scene sarafirstinvite10
    with dissolve

    sar "That...didn’t go as I expected it to."
    s "It went exactly as I expected it to."

    a "I...I’m home!"

    play sound "dooropen.mp3"

    scene sarafirstinvite11
    with dissolve

    a "..."
    a "It...it's still here..."
    s "{i}It?{/i}"
    sar "Hi again~"
    s "Welcome home."
    a "What...what’s going on?"
    a "Why is there...a woman...in our house?..."
    s "I invited her over. She’s a friend of mine."

    scene sarafirstinvite12
    with dissolve

    sar "It’s nice to finally meet you, Ami! You’re very pretty."
    a "...Thank you."
    s "Good. Keep saying things like that. She loves compliments."

    if bonus == True:
        sar "You take care of your [uncle] too, don’t you? That’s very impressive for a girl your age."
    else:
        sar "You take care of your [uncle] too, don’t you? Accountants are really useful nowadays, aren't they?"

    sar "I wish my daughter would take care of me more."
    a "D...Daughter?..."
    s "Oh, right. This is Sana’s mom."

    scene sarafirstinvite13
    with dissolve

    a "S-Sana’s mom?!"
    a "Why is Sana’s mom in our kitchen?!"
    a "Is Sana here too?!"
    a "How many girls are you hiding from me?!"
    s "I’m not hiding any. Sana’s mom, {i}Sara{/i}, is right in front of you."
    sar "I hope I’m not intruding or anything."
    a "You are! Get out of my house!"

    scene sarafirstinvite14
    with dissolve

    sar "Wow...I had a feeling you two were close but I didn’t realize you were {i}this{/i} close."
    sar "It’s like she’s afraid of women."
    a "S...Sensei...what is this?..."
    sar "She even calls you Sensei?"
    sar "You haven’t brainwashed her, have you?"

    scene sarafirstinvite15
    with dissolve

    a "I...I’m not brainwashed! I just don’t want anyone stealing my [uncle] away from me!"
    sar "Aww...You really love him, don’t you?"

    if amifingered == True and bonus == True:
        "I think {i}love{/i} is a bit of an understatement, personally..."

    a "O-Of course I do! He’s my [uncle]! He’s all I have!"
    sar "Don’t worry, dear. I won’t steal him from you."
    sar "The two of us were just chatting and he wanted me to meet you."
    sar "In fact, when he invited me over, he specifically said, “I need to prove to you that my [niece] is the cutest girl in all of Kumon-mi.”"
    sar "Now, being the mother of a cute girl, I couldn’t help but dispute it. But now that I’ve seen you in person..."
    sar "I...I think I might have to agree."

    "In an incredibly risky and rather impressive move, Sara swoops in for the kill and appeals to Ami’s weakest point- validation."

    scene sarafirstinvite16
    with dissolve

    a "You..."
    a "You don’t mean that..."
    sar "No, no. I really do."
    a "...Well, thank you."
    a "But...you won’t say anything to Sana...right?..."
    a "I wouldn’t want her to feel bad..."
    a "She’s...really cute too..."
    sar "Of course not. I’ll keep my opinion to myself for the rest of eternity."
    sar "I just hope you can find it in your heart to forgive me for showing up unannounced..."

    scene sarafirstinvite17
    with dissolve

    a "Well...I guess it’s okay as long as I can supervise you two..."
    s "What? Why do we need a supervisor? We’re adults."

    scene sarafirstinvite18
    with dissolve

    a "I’m not a kid, you know! I’m old enough to know what two consenting adults do when they’re alone together!"
    sar "Unfortunately for me, I can’t imagine your [uncle] would ever consent to doing anything when his heart has already been taken by you."

    if bonus == True:
        "Okay. This is no longer risky. It’s reckless."
        "This is a dangerous can of worms you’re opening, Sara."

    scene sarafirstinvite19
    with dissolve

    a "S...Sensei..."
    a "You’d really...choose me over...someone as pretty as her?..."

    scene sarafirstinvite20
    with dissolve

    sar "{i}Did I do well? I did well, right?{/i}"
    s "..."

    scene black
    with dissolve

    "I sigh to myself and take a seat at the dining room table."
    "Sara follows suit and, after taking a minute to collect herself, Ami does as well..."

    scene sarafirstinvite21
    with dissolve

    sar "Thanks for not kicking me out, Ami. I really hope the two of us can get along."
    a "Um...this still feels a little weird for me..."
    a "It’s not exactly...common for someone Sensei’s age to join us at the dinner table."
    a "Especially when there is no dinner..."
    sar "I take it you do all of the cooking around here?"
    sar "I thought Sensei was going to cook dinner for us tonight. I was totally surprised when I found out he wasn’t."

    scene sarafirstinvite22
    with dissolve

    a "Sensei? My Sensei? Cooking dinner?"
    a "Never in a billion years. He needs me."
    s "I want to be offended by that but it’s really hard when it’s 100%% true."
    sar "Now...I don’t mean to impose, but maybe one day you and I could make dinner together, Ami?"
    s "Wait...but I thought you said you couldn’t-"

    scene sarafirstinvite23
    with dissolve

    a "T-Together?..."
    a "But...what about Sana? Shouldn’t you be making dinner with her instead?"
    s "Am I just being ignored now?"

    if bonus == True:
        "Sara seems to be taking this family-infiltration mission seriously. She’s not even acknowledging me anymore."
    else:
        "Sara seems to be taking this firm-infiltration mission seriously. She’s not even acknowledging me anymore."

    "And she’s almost completely won over Ami."
    "What is happening right now?"

    sar "What if Sana comes over as well?"
    sar "In fact, what if we leave Sensei out of it entirely and have a little girls’ night in? That sounds fun, doesn’t it?"
    sar "The blonde one can come too. Ayane, I think?"

    scene sarafirstinvite24
    with dissolve

    a "R-Really?! Just us girls?!"
    sar "Of course! No boys allowed."
    a "That means...I won’t have to worry about anyone stealing Sensei!"

    "Is Ami unaware that there are girls in other locations? One of them could easily {i}steal{/i} me if she’s not looking."

    a "Yes! Yes! I want to do that!"
    a "What was your name again?"
    a "I wasn’t paying attention the first time I heard it because I already decided I hated you. But I’ve changed my mind!"

    scene sarafirstinvite25
    with dissolve

    sar "It’s...Sara. Hahaha..."
    a "Sara...Sara...Okay. That’s easy to remember."
    a "I promise not to tell Sana that you think I’m cuter than her. That’ll be a secret between you and me."
    sar "Thanks. I really appreciate that..."

    scene black
    with dissolve

    "The two of them carry on their conversation and ignore me all the way until night falls."
    "I knew inviting Sara over would spark up some sort of confrontation with Ami, but I had no idea it would mean essentially locking me out of every discussion for the rest of the day."
    "But oh well."
    "I guess this just means it will be easier to invite Sara over in the future."
    "..."
    "Sara winds up calling a cab to drive her home once it gets dark out."
    "I offer to walk her back myself but she shrugs it off when she wants to stay on good terms with my [niece]."
    "It’s strange, though."
    "Even though the two of us didn’t get to spend much time actually {i}talking{/i} to one another, I still feel like I know Sara a lot better than I did before..."

    $ renpy.end_replay()
    $ sara_love += 3
    $ sarainvite1 = True
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sarainvite2:
    play sound "phonebeep.wav"

    "I tap on Sara’s name in my phone and wait for her to answer."
    "The last time she came over ended in an unprecedented success, so I’m hoping for more of the same this time."
    "Well, in the broad sense at least. I’d much prefer if I actually got to spend time with {i}her{/i} instead of her and my [niece]."

    scene noonsky
    with dissolve
    play sound "phonebeep.wav"

    sar "Hey, [saramaster]~ What’s up?"
    s "Not much. What are you doing?"
    sar "Oh you know. A little of this. A little of that. "
    sar "I’m off tonight~"
    s "Are you actually off or are you just going to make Sana cover for you when I invite you over?"
    sar "Does the answer to that really matter?"
    s "I guess it doesn’t."
    sar "Hehehe~ Good. Then I’ll be right over."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."

    scene sarafirstinvitesex1
    with dissolve
    play music "asobeatsex7.mp3" fadein 5.0

    "A mostly empty home is what I find after opening the door."
    "Empty in the sense that Ami is nowhere to be found and won’t be returning any time soon."
    "She sent me a text on the way home that her and some of the others were going to the movies tonight."
    "But it’s not like it’s {i}entirely{/i} empty in the fact that-"
    "Well, I’m here."
    "And soon someone else will be here as well."
    "And there’s also the furniture and...the walls and..."
    "Everything that makes a house a house."
    "I don’t know what I’m talking about."
    "I’m not great at thinking when I’m alone."

    if bonus == True:
        "It’s one of the many reasons I prefer the company of others."
        "The bulk of those reasons being unsavory but-"
        "Well, I’m sure you’ll have a chance to see exactly what I mean by that by the end of the night."
    else:
        "I always wind up just endlessly scrolling through Facebook and liking the pictures of pretty girls who will never talk to me."

    play sound "doorbell.mp3"

    sar "Hellooooo~ Special delivery! One beautiful mom!"

    "What an excellent delivery. There should be a service that specializes in just that."

    s "You can let yourself in."

    "I shout to Sara from the living room."
    "The front door is thin so I don’t doubt that she’ll be able to hear me."

    play sound "dooropen.mp3"
    scene sarafirstinvitesex2
    with dissolve

    sar "Why hello there. Did I keep you waiting long?"
    s "Not long at all. I only got here a few minutes ago myself."
    sar "Is that so?"
    sar "Where’s Ami?"
    s "Not here."

    scene sarafirstinvitesex3
    with dissolve

    sar "You mean we have the place to ourselves tonight?"
    s "It certainly appears that way. The girls are out watching some action movie or something."

    scene sarafirstinvitesex4
    with dissolve

    sar "Excellent...excellent."
    sar "You must have been upset that you didn’t get me all to yourself last time, huh?"
    s "I guess so. Which is weird because, if anything, I figured you would be the one to be upset."

    scene sarafirstinvitesex5
    with dissolve

    sar "You say that as if I like you or something. I wonder what gave you that idea?"

    if sarasex == False:
        s "It’s kind of hard to not get that idea when you’ve cornered me in your room and asked me to lock the door before."

        scene sarafirstinvitesex6
        with dissolve

        if bonus == True:
            sar "Yeah, silly me for getting horny and thinking you might wanna fool around. "
            sar "That really wasn’t my finest moment, you know. I was so embarrassed when you left that I think I even cried."
            sar "I couldn’t even [masturbate] that night. That’s how much you hurt my feelings."
            s "I didn’t mean to hurt your feelings. It’s just..."

            scene sarafirstinvitesex7
            with dissolve

            sar "Yeah, yeah. It’s just that my daughter was passed out several rooms away and you didn’t want her to catch you screwing her mom."
            s "Bingo."
            sar "I’m sorry for coming on so strong in the first place."
            sar "I’m not really the best when it comes to hiding my feelings...so if I ever want something I just kinda reach out and take it."
        else:
            sar "Yeah, silly me for thinking it was appropriate to hug my daughter's teacher. "
            s "Let that be a lesson to you, Sara. A lesson in............................"
            s "Not hugging whoever you think about hugging."
            sar "Ugh."

        scene sarafirstinvitesex6
        with dissolve

        sar "Of course that method doesn’t normally work if someone on the other side isn’t willing, though."
        s "You say that as if it’s something that happens pretty frequently."

        scene sarafirstinvitesex8
        with dissolve

        sar "Not at all."

        if bonus == True:
            sar "It’s been a really long time since I’ve been with a guy. "
        else:
            sar "It’s been a really long time since I’ve hugged a guy. "

        sar "Some things happened and I just kind of...lost interest."
        sar "But something about you makes me want to change that."
        sar "I wonder what it is?..."

        "So do I. "
        "There’s really no reason to like someone like me."
        "I’ve got no special qualities. And I’m mediocre at best when it comes to talking to people."
        "But yet here we are, alone in my house and with another opportunity to take things further."

        sar "Listen..."
        sar "I understand if you still don’t feel comfortable moving this relationship along."
        sar "But, on the off chance that you maybe...you know...want to spend some quality time together, I am {i}more than willing{/i}."
        sar "It’s up to you..."

        "What should I do?"
        "If I turn Sara down now, I don’t think I’ll ever get another chance with her."
        "This decides everything."

        menu:
            "Stay friends":
                s "Sara..."
                sar "I don’t like that face."
                sar "It makes it look like I’m going to be rejected again."
                s "..."
                sar "..."

                scene sarafirstinvitesex9
                with dissolve

                sar "Hah..."
                sar "And boys are always saying how {i}girls{/i} are the confusing ones..."

                scene sarafirstinvitesex10
                with dissolve

                if bonus == True:
                    sar "So what? We stay friends? Not even any foreplay?"
                else:
                    sar "So what? No hug?"

                s "It’s probably for the best. "
                s "Ami seems to like you and there's still the issue of your daughter being in my class."
                sar "Those are both good reasons."
                sar "You obviously wouldn’t want to risk relationships you already have for a chance at one you don’t yet."
                sar "It’s kind of sad, though."
                sar "I think you and I could have been really happy together."
                s "..."
                sar "..."

                scene sarafirstinvitesex5
                with dissolve

                sar "But...I guess that’s nothing more than just a thought in the end."
                sar "Wanna go for a walk or something?"
                s "..."
                s "Sure."

                scene black
                with dissolve2

                "Sara and I leave the house as friends."
                "Nothing more."
                "And chances are there will never be any more."
                "I’ve destroyed the precious thoughts of us that had been swimming in her head since the first time I rejected her."
                "I’ve destroyed any chance for those thoughts to ever be more."
                "And yet-"
                "She continues to smile."
                "She’s stronger than she makes herself out to be."
                "But I guess that’s just how moms are."

                sar "Welp! I think that’s gonna be it for me~"
                s "Leaving already?"
                sar "Yeaaaaah. I’m gonna head back to the bar and give Sana a night off."
                sar "It was nice chatting with you, though...Sensei."
                s "Of course. It was nice chatting with you as well."
                s "I’ll see you soon."
                sar "Yup!"
                sar "See you soon~"

                "Sara heads back to her home-"
                "And I head back to mine..."

                "{i}Somewhere far away, a red string snaps.{/i}"
                "{i}Sara is no longer romanceable.{/i}"
                "{i}You will still be able to view some of her future scenes, but will be locked out of others.{/i}"

                $ renpy.end_replay()
                $ sara_love += 1
                $ sarainvite2 = True
                stop music fadeout 5.0

                "{i}Regardless, her affection has increased to [sara_love]!{/i}"
                "........."
                "......"
                "..."

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat

            "Take things further":
                s "I was just waiting for a better opportunity."
                s "I’m more than willing to start moving things forward with you now that we’re alone."

                scene sarafirstinvitesex11
                with dissolve

                sar "But what if Ami comes home? How will you explain the strange noises coming from your bedroom?"

                if bonus == False:
                    s "Ami knows about the noises I make when I hug."
                    sar "Okay. Good."
                    s "But...just in case-"

                s "I’ll just pretend nothing ever happened."
                sar "She seems pretty dedicated to you. I’m not really sure she’ll let you get away with that."
                s "Well we’ll cross that bridge when we come to it, won’t we?"

                scene sarafirstinvitesex12
                with dissolve

                sar "And you’re sure you want to cross it with someone like me?"
                s "I would have turned you down again if I wasn’t."
                sar "I don’t think I would have handled a second rejection very well. Things like that can kill a girl, you know?"
                s "That seems a little drastic..."

                scene sarafirstinvitesex5
                with dissolve

                if bonus == True:
                    sar "Who cares? You said yes so stop making me wait and fuck me already. Jeez."
                else:
                    sar "Who cares? You said yes so stop making me wait and hug me already. Jeez."

                s "You don’t have to tell me twice..."

    else:
        s "It sure as hell can’t be the fact that you’re borderline-obsessed with me, now could it?"

        scene sarafirstinvitesex13
        with dissolve

        sar "O-Obsessed?! I’m not obsessed!"
        sar "That’s really mean!"
        sar "We’re supposed to mutually like each other! You’re supposed to want to hold my hand and stuff!"

        scene sarafirstinvitesex14
        with dissolve

        sar "Love me more or I’ll hit you."
        s "I can’t imagine you hitting me would do much."
        sar "I wouldn’t be so sure, Sensei. I got into tons of fights in [high_school]. I’m vicious when I want to be."
        sar "I’ll scratch you and...pull your hair and..."

        scene sarafirstinvitesex15
        with dissolve

        if bonus == True:
            sar "Shoot...now I’m turned on..."
            s "Already? I didn’t even do anything."
            sar "It’s the scratching and stuff. It made me think of sex."
            s "Don’t most things in general make you think of sex?"

            scene sarafirstinvitesex16
            with dissolve

            sar "I blame you and your perfectly-sized penis. "
            sar "I’m addicted now and it’s all your fault."
            s "Is that supposed to be an insult?"

            scene sarafirstinvitesex17
            with dissolve

            sar "It was, but I didn’t really think it through beforehand. It definitely sounds more like a compliment when I say it out loud."
            s "Well, thank you for the insult. It was quite generous."

            scene sarafirstinvitesex18
            with dissolve

            sar "Anything for you, [saramaster]~"
            sar "As long as you’ll continue to have me, I’ll be happy to make you feel good about yourself...or just {i}good{/i} in general whenever you like."
            s "Whenever I like? I'm not sure if you’ve realized this but I have a pretty high sex drive."
            sar "I'm not sure if you’ve realized this but so do I."
            s "So if I call you at 3:00 in the morning and ask you to come over, will you come?"
            sar "I probably won’t wake up, but I can give you a spare key to my apartment in the event that you wanna come fuck me in my sleep."
            s "And if I call you while I’m at[school]?"
            sar "I’ll come bring Sana lunch and then suck you off in the bathroom."
            s "Are you an angel?"
            sar "I’m whatever you want me to be~"
            sar "All I ask is that you buy me candy and cuddle with me and lick my pussy every once in a while."
            sar "That’s all~"
            s "Can I just...lick more instead of buying you candy?"
            sar "Depends on how much effort you put into it."

            scene sarafirstinvitesex19
            with dissolve

            sar "Really, though...Thanks for not being weirded out by how quickly I came onto you and stuff."
            sar "The first time we had sex I couldn’t help but feel like I was rushing into things."
            sar "I half-expected you to just turn around and leave, but nope."
            sar "You took me right then and there. You didn’t even care that I was so drunk that I was about to pass out."
            s "Okay, saying it like that makes me sound like some sort of creep."
            sar "Nononono. You’re not a creep at all. Just horny. That’s how boys are."
            sar "I’m not going to hold that against you. I put myself out there and you took me. "

            scene sarafirstinvitesex20
            with dissolve

            sar "And also gave me what was probably my hardest orgasm ever in the process. "
            sar "Everyone wins! Yay!"

            "Sara is too cute."
            "So cute that she shouldn’t be allowed to exist."
            "She truly is a [teenager] trapped in a...slightly older woman’s body."
            "The way she winks at me...speaks with sincerity...suggests giving me blowjobs in the[school] bathroom..."
            "All of these things and more make me realize just how special she is."
            "So if buying candy, cuddling, and licking her pussy is all it takes to keep her by my side, I have absolutely no reason not to."

            s "Sara."
            sar "[saramaster]."
            s "Why are we still in the living room?"
            sar "Because you haven’t picked me up and carried me to the bedroom yet~"
        else:
            sar "Probably hug you or something."
            s "Fuck yeah."

    if bonus == True:
        jump sarainvsexx
    else:
        scene black
        with dissolve

        "Sara and I hug for almost seven minutes before I remember that I have something to do."

        s "I have something to do."
        sar "Okay."

        "Sara leaves."

        $ renpy.end_replay()
        $ sara_lust += 3
        $ sarainvite2 = True
        $ sarasex = True
        stop music fadeout 10.0

        "{i}Sara’s lust has increased to [sara_lust]!{/i}"
        "{i}You can now choose between affection and lust when inviting her over!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label sarainviteaff:
    scene sarainvitegen
    with fade

    "The two of us decide to spend the night together...not really doing anything."
    "But it's a pleasant form of nothingness."
    "Sara lays down next to me on the bed and moves closer."
    "Her eyes lock onto mine and only stray from them in short bursts."
    "But, for the most part, I'm all that she focuses on."
    "It feels a little uncomfortable at first given that neither of us are saying much."
    "But once that initial unease subsides, it becomes overwhelmingly apparent to me that this might just be the most comfortable I've felt in a very long time..."

    scene black
    with dissolve

    "Sara falls asleep next to me and I can't find it in myself to wake her up until Ami gets home."
    "It's a little awkward having to explain to her that Sara was literally {i}just{/i} sleeping and that nothing else happened at all, but she manages to buy it somehow."
    "Maybe it's due to how much she likes her or just...the fact that Sara could barely even keep her eyes open on the way out of the house but-"
    "Well, somehow or another, everything seemed to work out in the end."
    "It was a good night."

    $ sara_love += 3
    stop music fadeout 5.0

    "{i}Sara's affection has increased to [sara_love]!{/i}"

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

label sarainvitedoggy:
    scene black
    with dissolve

    ".........."
    "......"
    "..."

    if bonus == True:
        jump sarainvitedoggyx
    else:
        $ sara_lust += 3
        stop music fadeout 5.0

        "{i}Sara's lust has increased to [sara_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label sarabjreplay:
        scene black
        with dissolve
        play music "calmbar.mp3"
        play sound "dooropen.mp3"

        "I head over to Sara's place and the two of us get to talking about a number of things."

        if bonus == True:
            "Most of those things are of sexual nature so, before we know it, we wind up inside of her apartment and my penis winds up inside of her mouth."
            jump sarabjreplayx
        else:
            "Most of those things involve hugging, so we decide to do that for a couple hours."

            $ sara_lust += 1
            stop music fadeout 4.0

            "{i}Sara's lust has increased to [sara_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label sarainvitemissionary:
    scene black
    with dissolve

    ".........."
    "......"
    "..."

    if bonus == True:
        jump sarainvitemissionaryx
    else:
        $ sara_lust += 3
        stop music fadeout 5.0

        "{i}Sara's lust has increased to [sara_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label saradate10:
    play sound "phonebeep.wav"

    "I tap on Sara’s name in my phone and wait for her to answer."
    "It’s relatively windy out today, but that doesn’t stop me from wanting to wander around outside for a bit."
    "And if there is anyone I know who likes wandering around the city with me (And routinely stopping to buy candy because she is a child trapped in a woman’s body), it’s Sara."
    "But hey, if a few stops at convenience stores are all it takes to be seen in public with an attractive woman that’s actually close to my age..."
    "I guess that’s a price I’m willing to pay."

    play sound "phonebeep.wav"

    sar "Mmn...hello?..."
    s "Hey. You’re not just waking up now, are you?"
    sar "What time is it?..."
    s "It’s a little past noon."
    sar "Ngh..."
    sar "I drank too much last night..."
    s "Yeah, that sounds on-brand."
    s "Want to subject yourself to sensory overload and go walk around the urban district for a little while?"
    sar "Mnh...when?"
    s "Like, now."
    sar "Guh...okaaaaay."
    sar "I’ll start getting ready..."

    play sound "phonebeep.wav"

    "Sara hangs up and I begin to make my way to the same huge office building we normally meet at when we decide to visit that part of town."
    "Knowing that it will likely be a while until she gets there, I stop for coffee at a nearby cafe (One without any [[confirmed] manga club members working) and pick something up for Sara as well."
    "........."
    "......"
    "..."

    scene saranikiboard1
    with dissolve
    play music "justbehappy.mp3"

    "Unfortunately, she is one of those cowards who is incapable of drinking black coffee, so I wind up consuming two drinks instead of one."
    "That’s fine, though."
    "Caffeine is one of those drugs that you can’t overdose on."
    "Probably."
    "And, even in the event that I somehow did, she’ll be here to call an ambulance."
    "I’m sure today will proceed just fine with all of that in mind."

    s "You look really good for someone battling a hangover right now."
    sar "Thanks~ "
    sar "The trick is to just drink more as soon as you wake up so your brain can go back to feeling good."
    s "That’s not a trick, that’s alcoholism."
    sar "I just call it having a good time."
    s "That is also alcoholism."
    s "You have a problem."

    scene saranikiboard2
    with dissolve

    sar "I do not! It’s not like I do this every morning, Sensei. "
    sar "I just got a call from Haru-chan really late last night because she was feeling all lonely again."
    sar "So the two of us did what any good friends would do and got drunk on the phone and cried to each other about all kinds of stuff."
    s "I’m kind of glad I don’t have any friends as close as that. That sounds horrible."

    if sarasex == True:
        scene saranikiboard3
        with dissolve

        sar "That’s not true. I’m your friend, Sensei~"
        sar "And I think we’re plenty close."

        if bonus == True:
            sar "So close that you get to stick it in me while my daughter is downstairs. Isn’t that great?"
            s "For us? Yes. For your daughter? No."
            sar "Well {i}I{/i} think it’s great."
            sar "Don't you think it’s like...about time we told her, though?"
            sar "At least that way, we probably wouldn’t have to worry about her walking in on us."
            s "I prefer to keep my relationships secret, if you don’t mind."
            s "Especially from people as pure as Sana."

            scene saranikiboard4
            with dissolve

            sar "Oh, please. She’s a growing girl. I’m sure she gets up to all sorts of stuff while she’s alone."
            s "Take that back. I will not allow you to tarnish that girl’s image."
            sar "I’m just saying, I know I did when I was her age. "
            sar "But I was also having sex with my teacher when I was her age, soooo..."
            sar "Maybe I just have a thing for teachers?"
        else:
            sar "Some might even say we're like a sandwich. Just two meats stuck together, waiting to be consumed by a large man."
            s "No one would say that."
            sar "You never know, Sensei."

    else:
        scene saranikiboard5
        with dissolve

        sar "That’s not true, Sensei. I think we’re plenty close."
        sar "Even if you won’t accept my love."
        s "I’ve accepted it. I just can’t return it."
        sar "Yeah, that."
        sar "But if you ever feel like calling me in the middle of the night to get drunk and cry, I’ll always be there. Kay?"
        s "This is not a thing I will ever want. But thanks, Sara."
        sar "Of course~"

        scene saranikiboard6
        with dissolve

        sar "Though, I suppose at this point you’d rather just call my daughter and talk to her instead, wouldn’t you?"
        s "I’m not quite sure what you’re insinuating with that."
        sar "Just that she’s getting awfully warmed up to you out of nowhere."

        if bonus == True:
            sar "Maybe on account of you visiting her dorm room at night?"
        else:
            s "I am the only person who knows she is a health inspector. It is a bond we share now."

        scene saranikiboard7
        with dissolve

        sar "Maybe if I was still her size..."

        if bonus == False:
            s "Maybe if you were a health inspector."
            sar "..."

        s "..."
        s "Okay, anyway, why don’t we talk about something else?"
        sar "Embrace my youthful jealousy, Sensei...Embrace it~"
        s "It’s less of a youth thing and more of an...innocence thing."
        s "And even then, nothing like that is even close to happening between Sana and me."

        if bonus == True:
            sar "But...if the opportunity arose..."
            s "..."
            sar "Come on. If there’s anyone who knows what teachers like you think about in their spare time, it’s me."
            sar "I was barely a freshman when I started sleeping with mine."
        else:
            sar "Okay. Thank you for being honest with me. I appreciate you as a person and respect your decision to not pursue a further romantic relationship with her."
            s "No prob."

    "It’s crazy right now to think of Sana doing anything remotely close to what Sara was doing back then."

    if bonus == True:
        "Will that {i}stop{/i} me from thinking about it? Of course not. "
        "My mind lands on that almost every time I walk into her room."
        "But it’s just so far out of reach at this point that I don’t even bother addressing it."
        "Sara, though-"
        "Those experiences went on to shape the rest of her life."
        "A lot of people say that the first few years of a child’s life are what go on to sculpt them as a person."
        "I don’t think I agree with that."
        "I think that people tend to find themselves in their[teen]years- particularly their years in [high_school]."
        "Which is why I’m so worried about how everyone I know will eventually break down and die."
        "And how I, too, will become the man who abandoned Sara and her family."
    else:
        "She is such a good girl."

    s "Do you regret it at all?"

    scene saranikiboard8
    with dissolve

    if bonus == True:
        sar "What? Sleeping with my teacher? "
    else:
        sar "What? Hugging my teacher until the stork showed up and gave me my children?"

    s "Yeah."
    sar "Hmm...I guess I do sometimes."
    sar "I definitely loved him. "
    sar "But now I have an adorable little girl who’s going to wind up becoming a better version of me when she's older. And that’s fine."
    sar "Besides, even if he wound up being unfaithful, I needed someone like that back then."
    s "Have you always been this-"
    sar "Needy?"

    scene saranikiboard9
    with dissolve

    sar "Probably."
    sar "Yeah, I’d say so."
    sar "I was kind of like an...anti-Sana when I was in [high_school]."

    if bonus == True:
        sar "Instead of closing myself off from everyone, I chose to stay wide open instead."
        sar "I would have let anyone in regardless of who they were or what they wanted from me."
        sar "And I wound up falling for the first person to ever look at me as a girl."
        sar "Well, the first older person at least."

        scene saranikiboard10
        with dissolve

        sar "There were plenty of boys who liked me back then, but I never really had any interest in them since they were all just kids."
        sar "Like, what could they do for me that I couldn’t do for myself?"
        s "Well, you just wanted to feel loved, right? That’s what you’re making it sound like."
        sar "I think “protected” is a little closer to what I was looking for."
        sar "It would make me happy when I’d get a confession from a boy, but none of them would ever make me feel as safe as someone older with more...power and stuff."
    else:
        sar "Instead of closing myself off from everyone, I started a popular polka group and learned how to play the accordian."

    scene saranikiboard11
    with dissolve

    sar "Which is probably one more reason I like you so much."

    if bonus == True:
        s "The only power {i}I{/i} have is determining whether a handful of [teenage]girls will make it through their first year of [high_school] or not."

        scene saranikiboard12
        with dissolve

        sar "You’ve got a lot more power than that, Sensei."
        sar "You have an entire class of girls who look up to you and learn from you."
        sar "And with barely any men around, you’re pretty much the only male figure they have in their lives."
        sar "Given those kinds of circumstances, I think it’s pretty miraculous you’re as decent as you are."
    else:
        s "What?"

    scene saranikiboard13
    with dissolve

    sar "If only the same could have been said about Sana’s dad..."

    if bonus == True:
        s "I take it he was one of those people who abused his position?"

        scene saranikiboard14
        with dissolve

        sar "Will you think I’m dumb or gullible if I say he was?"
        s "I think you’re dumb and gullible now."
    else:
        s "What does that have to do with anything?"
        sar "Oh, you know."
        s "Sara, I don't even like the accordian."

    scene saranikiboard15
    with dissolve

    sar "Hey!"
    s "I’m kidding..."

    "Kind of."

    s "Of course I won’t think that. "
    s "I don’t know what things were like for you when you were that age, and I don’t know what must have been going through your mind in order to deal with that."
    s "But it’s not crazy to believe someone would have taken advantage of you in the position."

    scene saranikiboard16
    with dissolve

    sar "Good recovery. I like you again."
    s "Good. Those ten seconds you didn’t were really suspenseful. "

    scene saranikiboard17
    with dissolve

    sar "Heheh~"
    sar "Either way, what’s done is done. "
    sar "All things considered, I think I’m in a pretty good place now."
    sar "I own a business."
    s "That’s failing."
    sar "I have a nice apartment."
    s "That you live by yourself in and are likely overpaying for."
    sar "And I have the cutest daughter in the world."
    s "Who can’t hold a conversation to save her life."

    scene saranikiboard15
    with dissolve

    sar "You’re mean today! Let me have something!"
    s "You have my arm. Any more and you’ll start getting ahead of yourself."

    scene saranikiboard11
    with dissolve

    sar "Oh ho ho~ Are you saying I get to keep this arm all to myself?"
    s "Sure. For now. "
    s "I do want something in return, though."

    if bonus == True:
        sar "Ooooh? Do we need to go somewhere a little more private, [saramaster]?"
        s "It’s nothing like that."
        s "I just want you to tell me more of your story sometime."

        scene saranikiboard18
        with dissolve2

        sar "..."
        s "I’m obviously not going to call you at 2:00AM to get drunk and cry, but I’d like to hear more about how you wound up where you are now."
        s "I know surprisingly little about you for a girl who is allegedly “wide open.”"

        "I’m also sure that figuring out what makes Sara tick is sure to help me grow a little closer to Sana as well."
        "And, even if it doesn’t, I’m interested in seeing how things got to this point."
        "And how I might possibly be able to avoid forcing that onto anyone else in the future."

    sar "Do you want to get married?"
    s "What?"
    s "No?"

    scene saranikiboard19
    with dissolve

    sar "Heheh~ Just checking..."
    sar "I’d love to tell you more of my story sometime."
    sar "And I’d love to hear yours as well."
    s "..."
    sar "..."
    s "Yeah, I don’t know if-"

    scene saranikiboard20
    with dissolve

    sar "Oh! Here’s a good place to start now!"

    scene saranikiboard21
    with fade

    "Sara lets go of my arm and skips over to a local concert hall, displaying a gigantic billboard of-"

    s "Uh-oh."
    sar "When I was a little girl, I wanted to be just like that one day."
    sar "Someone the entire world would gaze at with envy."
    sar "A person that boys would adore and that girls would look up to."

    if bonus == True:
        sar "But now I’m washed up and emotionally spent before even hitting the middle of my thirties."
    else:
        sar "But now I’m just...washed up and emotionally spent."

    sar "Do you like girls like that, Sensei?"
    sar "They make your heart race, don’t they?"

    scene saranikiboard22
    with dissolve

    sar "Or maybe they make you feel a little something else?"

    if bonus == True:
        sar "Doesn’t seeing that cute girl up there make you want to just grab her and corrupt-"
    else:
        sar "Doesn’t seeing that cute girl up there make you want to just take her to the zoo and show her the elephants?"

    scene saranikiboard23
    with dissolve

    sar "..."
    s "..."

    scene saranikiboard24
    with fade

    sar "Why aren’t you saying anything?"
    sar "Don’t tell me that...{i}you{/i} wanted to look like that one day, too?..."
    s "That..."
    s "Is my ex-girlfriend."
    sar "..."
    s "..."

    scene saranikiboard25
    with dissolve

    sar "Oh, come on! Like I’d ever believe that you dated {i}Niki.{/i}"
    sar "She’s like...an icon in Kumon-mi. "
    sar "I don’t really follow idols the way I used to, but she’s on TV all the time and..."
    sar "And you still haven’t told me you’re kidding yet..."

    scene saranikiboard26
    with dissolve
    play sound "phonebeep.wav"

    sar "What are you-"

    scene saranikiboard27
    with dissolve

    sar "What are you doing? I have no idea who-"

    play sound "phonebeep.wav"

    ni "Haven’t I told you not to call me in the middle of the day before?! I’m fucking busy!"

    scene saranikiboard28
    with dissolve

    sar "Um...is this..."
    ni "..."
    ni "Who the fuck are you?"
    sar "A friend of...your ex-boyfriend’s..."
    sar "Is this really Niki Nakayama?"
    ni "Teehee~ Apologies, miss! That was my manager on the phone just now."
    ni "Would you mind putting your {i}friend{/i} on the line for sec? There's something I need to talk to him about~"

    scene saranikiboard29
    with dissolve

    sar "She, uhh...wants to talk to you..."
    s "..."
    sar "..."
    ni "Hello? "
    ni "Are you still-"

    scene saranikiboard30
    with dissolve
    play sound "phonebeep.wav"

    sar "Ah!"
    sar "You just...hung up on Niki..."
    s "This is what’s best for everyone."

    scene saranikiboard31
    with dissolve

    s "Do you believe me now?"
    s "You should have been able to recognize her voice if you know her, right?"
    sar "..."
    s "..."

    if sarasex == True:
        if bonus == True:
            sar "I’m...having sex with Niki Nakayama’s ex-boyfriend?..."
        else:
            sar "I hugged a person Niki Nakayama hugged?..."

        sar "Did I...Did I finally make it after all?"
        s "..."
    else:
        sar "It’s suddenly starting to make a lot more sense why you don’t like me the same way I like you."
        s "..."

    scene black
    with dissolve2

    "Sara is a little too shocked to carry on hanging out after that."
    "There’s also the fact that she needs to start getting ready for work, but it’s not like that’s ever stopped her before."
    "All things considered, I think this was a pretty good afternoon."
    "I got to learn a little more about Sara...and also got to make myself look a lot cooler than I actually am in the process."
    "Now, as long as Niki doesn’t-"

    play sound "texttone.wav"

    s "..."

    play sound "texttone.wav"

    s "..."
    s "I’ll just..."
    s "Read those later..."

    $ renpy.end_replay()
    $ saradate10 = True
    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label sarabar20:
    scene barsaraayane1
    with dissolve
    play music "calmbar.mp3"

    "I decide to spend a totally normal night at the bar where nothing can possibly go wrong."

    scene barsaraayane2
    with dissolve

    ay "What’re ya drinkin’ stranger?"

    "I fail miserably."

    s "Whiskey on the rocks. No ice."
    ay "Comin’ right up, champ."
    s "Ayane, don’t agree to that. It’s literally not possible."
    ay "I ain’t Ayane, bud. I’m Efrosinia Aleksandrova, Russian spy."
    s "You are equally bad at that job as well, then."
    s "Where are the people who actually work here?"

    scene barsaraayane3
    with dissolve

    sa "I...tried to stop her...but..."
    sa "My mom is...stronger than I am..."
    ay "You still want that orange soda, champ?"
    s "Ayane, please take off that uniform."

    scene barsaraayane4
    with dissolve

    ay "Here? Shouldn't we wash the counters first?"
    sa "I think...there are bigger issues than the counters..."
    s "You guys didn’t hire Aya-"
    ay "Efrosinia."
    s "You guys didn’t hire Efrosinia, did you?"

    scene barsaraayane5
    with dissolve

    sa "No..."
    sa "Well...not really..."
    sa "Ayane and I were hanging out and...my mom asked if we could come help her with something..."
    ay "Efrosinia. But yes."
    ay "Sana and I are going to fix this bar, Sensei. Watch."
    s "How? You haven’t even served me yet and I’m literally the only customer."
    sar "I didn’t ask for their help to serve customers, Sensei. I need them for marketing stuff."

    scene barsaraayane6
    with dissolve

    s "Woah. When did you get there?"
    sar "I just sat down a second ago. Don’t freak out."
    s "Okay, good. I would have felt bad if I ignored you in favor of a younger girl wearing the same outfit."

    scene barsaraayane7
    with dissolve

    ay "Wait, Sensei! It’s me, Ayane!"
    ay "I’m not Efrosinia at all! Notice me! Not Sana’s mom!"
    sar "Ayane...why don’t you take off that uniform now, dear?"

    scene barsaraayane8
    with dissolve

    if bonus == True:
        ay "Why is everyone so horny tonight?! "
        ay "Fine! But only if Sensei is participating as well!"
    else:
        ay "But this is where all of my power is stored!"

    s "Sorry, Sana. Would you mind leaving a little early tonight?"
    sa "Huh?...What?..."
    sa "I...zoned out for a second..."
    sa "What are you doing with those two that I can’t...be around for?"
    sa "Whatever it is...I’m sure I could contribute in...some way..."

    scene barsaraayane9
    with dissolve

    ay "Really? I didn’t think you were ready for that yet."
    sar "Oh, my sweet Sana. I love you, but I think you should stay out of this."

    if bonus == True:
        ay "That’s right. Sensei is an adult who-"
    else:
        ay "Does anyone want to make a bone neck-"

    scene barsaraayane10
    with dissolve

    sar "You too, Ayane."
    sar "You can keep the outfit as payment for helping me out, though."
    ay "Thank you! It’s extremely cute and I will handle it with care!"

    if bonus == True:
        ay "I promise I won’t use it for anything naughty either!"
        sa "Na...naughty?..."
        sar "Sana, would you mind taking your friend upstairs and helping her put her normal clothes back on since she seems so against doing it on her own?"
        sa "Oh...um...yes, but..."

    sa "Do you still need me around tonight?..."
    sa "Because Ayane and I were..."
    sar "Not anymore, dear. I already told you everything I wanted to tell you."
    sar "The two of you are free to leave whenever you want since I’ll be closing any minute now."
    sa "Oh...okay..."
    sa "Umm...afro...xena?"

    scene barsaraayane11
    with dissolve

    ay "Ayane is fine now, Sana..."
    ay "And I’m coming."

    if bonus == True:
        ay "Sensei...even though she’s beautiful...remember who it is that’s carrying your child."
    else:
        ay "Sensei...if you get a minute-"
        s "No."
        ay "Ugh. FIne."

    scene barsaraayane12
    with dissolve

    "Sana takes Ayane upstairs and I find myself alone at the bar with Sara once again."
    "She takes a sip from her glass of wine, looking me directly in the eyes before saying-"

    if bonus == True:
        sar "Congratulations on the child."
        s "There is no child, Sara."
        sar "Are you sure about that?"
        s "Yes. I would have noticed if Ayane was pregnant."
        sar "Mhm~"

        scene barsaraayane13
        with dissolve

        sar "But what about me?"
        s "First off, yes. I would have noticed that as well."
        s "Secondly, put down the fucking wine if you’re pregnant, you maniac."

        scene barsaraayane14
        with dissolve

        sar "Relax, relax. There is no baby, so I’m free to get as drunk as I want."
    else:
        sar "Sometimes, I wonder if this is all actually real or if this is just some kind of crazy dream."
        s "You have an alcohol problem."

    scene barsaraayane15
    with dissolve

    sar "And, this might come as a surprise, but that isn’t very drunk at all tonight."
    s "Reaching out to [younger_girls] for help with marketing...watching your alcohol intake..."
    s "What happened to you?"
    sar "Do you want the sad answer or the really sad answer?"
    s "Give me the sad answer."
    sar "If I don’t start turning things around for this place pretty soon, I’m going to wind up losing it."
    s "Oh, yeah. I feel like we’ve established this before."
    s "What was the really sad answer?"

    if bonus == True:
        sar "That I actually am pregnant and am about to lose not only the bar and my home but my daughter and my liver as well."
        s "Yeah, that sounds a lot more serious."
    else:
        sar "That I'm actually a ghost and that this building is the only thing keeping me tied to reality."
        s "Wooooooooah."

    scene barsaraayane16
    with dissolve

    sar "Hah...I really can’t do it anymore, Sensei."
    sar "I’m getting desperate."
    sar "I used to love running this place, and I used to be so good at it."
    sar "Mine and Sana’s cuteness can only take us so far without any males around."
    sar "Maybe I just need to hire an attractive man to bring in a lot of women and-"

    scene barsaraayane17
    with dissolve

    sar "..."
    s "..."
    sar "..."
    s "No."
    sar "Not even to help little ole’ me?"

    if bonus == True:
        s "None of the girls I would attract are even old enough to drink yet."
        sar "I don’t mind bending the rules a little bit as long as I can pay rent."

    s "I can’t believe someone like you was ever allowed to run a bar in the first place."

    scene barsaraayane15
    with dissolve

    sar "Anybody can run a bar as long as they can bring in customers."
    sar "I just apparently suck at attracting female ones."
    s "So you think enlisting the help of a wallflower and an...{i}Ayane{/i} is going to help?"
    sar "I don’t expect Sana to be able to do much. But isn’t Ayane the heiress of her father’s bubble wrap company?"
    sar "She must know at least {i}something{/i} about marketing, right?"
    s "I mean...she’s definitely a lot smarter than she lets on."
    s "Maybe she can just get her father to invest in the business or something like that?"

    if bonus == True:
        sar "Ooooh maybe he’s one of those creepy dads who’s super into his daughter? "
        sar "And if I give her a job here, outfit and everything, he’ll show up and spend lots of money..."
        s "I don’t think I’m supposed to let you exploit my students like that."

        scene barsaraayane17
        with dissolve

        sar "You’re right. I should just ask her to wear it back home and seduce her father with it the old fashioned way."
        s "Sara..."

        scene barsaraayane15
        with dissolve

        sar "What? She doesn’t have to {i}do{/i} anything. Just...twirl around a couple times and say something like, “I love you, Daddy~”"
        sar "That would work on you, wouldn’t it?"
        s "Yes, but I’m a horrible person. "
        s "Besides, Ayane’s father doesn’t really pay much attention to her from what I understand. "

        scene barsaraayane18
        with dissolve

        sar "Why didn’t you tell me that before I started rambling on about seducing him! Now {i}I{/i} feel like a horrible person, too!"
        s "I liked the picture you were painting and wanted to imagine it firsthand. "

        scene barsaraayane19
        with dissolve

        sar "Mm! I knew you liked her in the barmaid outfit more than me! I could tell right away!"
        sar "The only way you can make it up to me is by getting a job here and helping me attract new customers."
        s "Again, I’m going to refuse."
        sar "What if I give you Sana?"
        s "..."
        s "Like, in what context?"
        sar "Like you marry me and become her new step-dad."
        s "Would you really be okay with someone marrying you just to get to your daughter?"
        sar "It depends on the ring!"
        sar "Also, it happens in soap operas all the time. I’m basically prepared for it at this point."
        sa "Um...prepared for...what?"
    else:
        s "That is a good idea. I will begin preparing a Powerpoint presentation immediately."
        sar "I can finally use my Shark Tank voice."

    scene black
    with dissolve

    "Sana and Ayane come back downstairs in their normal clothes and stop halfway between the counter and the door."
    "Sara and I hop off of our stools to meet them and, within a matter of seconds, things proceed to get even more difficult."

    scene barsaraayane20
    with dissolve

    sar "Sana, hypothetically, if Sensei promised to save the bar in exchange for you becoming his property-"
    s "Weird way to say “stepdaughter.”"
    sar "Would you do it?"

    scene barsaraayane21
    with dissolve

    sa "Property?!"

    if bonus == True:
        ay "You can’t have Sana! She’s mine! And I’m yours! "
        sar "Do I get to have anybody?"
        ay "No! You just exist, Sana’s mom!"
        sar "You know my name, Ayane..."
        ay "Not anymore I don’t!"
        sa "What...would I do as...pro...property?..."
        s "Your mom is kidding."
        s "What she really wants to know is how you’d react to her and I getting married."
    else:
        sar "Did I say property? I meant personal secretary."

    scene barsaraayane22
    with hpunch

    sa "That’s even worse!"

    "...It is?"

    ay "Fine! I concede! Take Sana! Just don’t get married!"
    sar "Wow. "
    sar "Those are...uhh...quite the reactions..."
    s "We’re not going to. Sara’s just desperate for a new method to turn the bar around."

    scene barsaraayane23
    with dissolve

    sar "It’s a little more than {i}just{/i} turning the bar around, you big jerk."
    sa "Hah...my heart...so fast..."
    ay "Well...umm...I {i}am{/i} really thankful for the outfit, Sara. And for always being so nice to me."

    if bonus == True:
        ay "So if there's any way I can help without relinquishing the hand of the man before me, I will do my best."
    else:
        sar "Any time, yo."

    scene barsaraayane24
    with dissolve

    ay "And...umm...Sensei-"

    if amiinvite3 == False:
        ay "If you wouldn’t mind, I’d like to maybe talk to you about something soon. "
        ay "If that’s okay. "
        s "Hm? Yeah. That’s fine."
        s "Good luck with whatever weird marketing stuff the two of you are planning on doing."
        sa "I honestly...have no idea..."
        sa "But I’ll...do my best..."
    elif thirdreset3 == True:
        s "Yeah? What's up?"
        ay "Um..."
        ay "Try not to stay too late. Ami might get jealous."
        s "Oh."
        s "Uhh...okay."
    else:
        ay "We...still need to talk about that thing I wanted to talk about..."
        s "Hey, I'm waiting on you. I am ready for this whenever."
        ay "R-Right..."
        ay "Well, then...okay. Soon."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene barsaraayane25
    with dissolve

    sar "Hah...[teenager]s are exhausting..."
    s "Tell me about it."
    sar "To think they’d be so opposed to two consenting adults having some sort of relationship together...What gives?"
    s "I think it’s less about you having a relationship and more about who you’d be having it {i}with{/i}."

    scene barsaraayane26
    with dissolve

    sar "Have you always been this popular with girls, Sensei?"

    if saradate10 == True:
        sar "I mean...you did date {i}the{/i} Niki Nakayama, so I guess you must have been."

    s "For as long as I can remember at least."

    "I manage to make myself sound cool and be completely honest at the same time."
    "Memory loss has its perks."

    sar "All the more reason to come work for me."
    s "Sure. But what can you pay me?"
    sar "I can pay you in love~"
    s "Is there a bank around here where I can trade love for cash? Because I have a [niece] to take care of."
    sar "Isn’t your [niece] the one taking care of you?"
    s "Yes, but I’m the one funding everything."
    sar "She’s not rolling in maid cafe money yet?"
    s "I don’t think- Wait, why do you know about the maid cafe?"
    sar "Oh, I go there for lunch sometimes. The prices are great and the girls are adorable."
    s "I...didn’t think you were the type to go to places like that."
    sar "Of course I am. Everyone likes maid cafes, Sensei. And anyone who says they don’t is a liar."
    s "Well, if all else fails, you could always get a job there. At least you’d still get to wear a nice outfit."
    sar "I’m not going to let this place fail."
    sar "I’ve decided."
    s "Well, I’m glad to see you taking a step in the right direction, but you should probably come up with a solid gameplan first."
    sar "I’m trying, aren’t I?"
    sar "I’m asking for help and throwing ideas out there. It’s just that none of them are very good yet."
    s "You’re also closing the bar early. How does that help at all?"
    sar "It’s just for one night."
    s "It’s not, though. You’ve been doing this a lot lately."
    s "You did the same thing when I walked Sana home that one time."
    s "You’re not going to bring in any new customers if your hours aren’t reliable."

    scene barsaraayane27
    with dissolve

    sar "..."
    sar "You..."
    sar "You think I don’t know that?"
    s "If you know it, then do something-"

    scene barsaraayane28
    with hpunch

    sar "It’s really fucking hard, okay?!"
    sar "Do you have any idea how depressing it is just sitting here for hours on end hoping literally {i}anyone{/i} shows up?!"
    sar "It used to be fine! I used to actually make money! "
    sar "Now I can’t even make it through one night without trying to figure out which bills I have to stagger to keep all of my shit on!"
    sar "I’m tired! I’m sad!"

    scene barsaraayane29
    with dissolve

    sar "And the man I like is barely doing anything to help."
    s "..."
    sar "..."
    sar "I’m sorry for yelling. And I know it’s not your responsibility."
    sar "But I’m in deep...deep trouble...and..."

    scene barsaraayane30
    with dissolve2

    sar "And I have nobody else to rely on..."
    sar "I need you to be more than just a friend for me right now. I need you to whip me into shape."

    if bonus == True:
        sar "And also just whip me. That sounds fun too."
        s "You’re not very good at crying, are you?"
        sar "I’m much better at it when I’m by myself."

    "Sara’s makeup begins to smear as her tears drip down her cheeks."
    "There’s no sobbing or heavy breathing or anything like that. Just a single, blank stare and an occasional sniffle. "
    "It’s like she’s waiting for me to say some magic words and make all of the unfortunate circumstances she’s found herself in vanish."
    "I can’t do that."
    "I can’t do anything but watch her cry and pretend to know how to help her."
    "She’ll see through that, though."
    "She might act like a [teenager], but she isn’t one."
    "She’s an adult who’s experienced adult things."
    "She’s someone who’s been burned before and it wouldn’t be right for me to burn her again after the two of us have been spending so much time together."
    "I guess this is just one of those rare occasions where honesty will need to do the trick."

    s "I don’t know what to do, Sara."
    s "I have zero experience with running a bar."
    sar "I can train you. Believe it or not, I’m still really good when I’m not drunk."
    s "I can’t work here. You know that."
    s "I already have a job."
    sar "I can’t lose this place...I have so many memories here. "
    s "I don’t want you to lose this place either. "

    "I stand up from my stool, ready to drop a cool one-liner and make a dramatic exit."
    "But it isn’t until I stand up that I realize that I don’t have any lines. "
    "And that any exit I make while she’s in this condition will be dramatic by default."

    scene black
    with dissolve2

    "So I do the only thing I know how to do."
    "I comfort her physically."
    "I bend down and wrap my arms around her, letting her cry into the fabric of my shirt."
    "It is right then that the sobbing begins."
    "She was doing such a good job at holding back, too."
    "Oh well."
    "It’s not bad to let people break as long as you’re there to make sure none of the pieces fall into a storm drain."
    "You could also collect them and put them into a box."
    "There are many, many things you can do with the shattered remnants of one’s well-being."
    "Especially remnants as colorful as this woman’s."
    "I will protect them from every storm drain in the world."

    sar "I’m sorry..."
    sar "It’s been...a really bad day..."
    s "It’s fine."
    s "I don’t know how I can help you."
    s "But I’ll try to pay more attention for your sake."
    sar "Thank you..."
    sar "That means...the world to me..."

    "I wind up having to carry Sara upstairs and put her to bed the same way I’ve done many nights before."
    "Just this time it’s from crying so hard that she gave herself a migraine and not the compulsive consumption of alcohol."
    "Goodnight, Sara."
    "Goodnight, everything."
    "I go home."

    $ renpy.end_replay()
    $ sara_love += 3
    $ sarabar20 = True
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sarabar25:
    scene barnight
    with dissolve2
    play music "sidecharacter.mp3"

    "I make my way to the bar."
    "No one is there."
    "Though, I imagine that’s on account of the sign on the door saying they’re closed for the night."
    "I’m not sure why Sara chose {i}now{/i} to take a night off when she’s finally [[kind of] on the cusp of turning things around for the place."
    "But I guess I’m not one to spend too much time questioning her decisions when she’s made so many poor ones in the past that they’re starting to lose their novelty."
    "Regardless, I doubt she’s far."

    if bonus == True:
        "In fact, knowing her, she’s probably upstairs getting drunk...or masturbating to pictures of me as we speak."
    else:
        "In fact, knowing her, she’s probably upstairs getting drunk...or looking at pictures of me as we speak."

    "I’m not sure where she’d get any, considering I don’t think I’ve posed for a photo even once since waking up here-"
    "But Ayane’s sure had no problem procuring images of me, so maybe Sara just bought them from her?"
    "I don’t know. "
    "I’m done standing around down here, though. "
    "If I’m going to come all the way over to a failing bar in the middle of the night, I’m at least going to get something out of it."

    if sarasex == True and bonus == True:
        "And whether that be a blowjob or just some quality time with a friendly neighborhood MILF, I’m sure that whatever happens will be, at the bare minimum, worth walking a few miles."
    else:
        "And whether that be a free beer or just some quality time with a “friend,” I’m sure that whatever happens will be, at the bare minimum, worth walking a few miles."

    scene black
    with dissolve

    "The stairs creak the same way they always do, as I’m sure it’s been decades since this building has received any sort of renovation."
    "And I’m sure it’ll be a few decades more until it {i}is{/i} renovated (If Sara even still owns it by then)."
    "But stairs aren’t all that important."
    "You can let them rot and decay and still manage to make your way up just by stepping around all of the soft spots. "
    "The worst case scenario is that your leg will bust through an old plank and maybe tear some skin off or rip your pants in the process-"
    "But you’ll still get to where you’re trying to go."
    "Until you don’t, that is."
    "But I don’t know why I’m telling you this."
    "I ascend."

    scene saranewapt1
    with dissolve2

    "I walk into Sara’s place to find that she must have taken the liberty of redecorating recently. "
    "There’s some sort of movie on her television (Which also looks rather new), but I can’t be bothered to figure out what it is since I’m too busy taking in the rest of the sights. "
    "It’s warm inside- much warmer than in the corridor that carried me here. "
    "And the residual scent of old alcohol and vomit has been replaced by a sweeter smell of cinnamon and...some other indiscernible spice."
    "Sara locks eyes with me, not feeling the need to say hello as, apparently, I’m just welcome to intrude on her privacy whenever I want now-"
    "But Sana doesn’t react. Or perhaps it’s more like she doesn’t notice."
    "She just keeps her eyes centered on the movie that I can’t be bothered to watch and attempts to either fade into obscurity or simply just enjoy some rare time alone with her mother."
    "I don’t think I should be here right now."

    sar "Oh, good. I was worried that I was going to have to get up."
    sar "Can you pour me another glass of wine? There’s an open bottle on the counter over there."
    sar "Also, any compliments regarding my super awesome interior design skills are welcome. "
    sar "I was in the mood for a little spring cleaning earlier and, well, one thing led to a whole bunch of other things that led to this place looking almost brand new."
    sa "We don’t...even {i}get{/i} Spring here, though..."
    s "If I didn’t know better, I’d think you just bought a whole new place."
    sar "Less talking, more pouring. "
    sar "I know you’re not much of a wine guy, but feel free to help yourself to some as well. You know, as thanks for your service and whatnot."

    scene saranewapt2
    with fade

    s "Better idea- how about I just block your view of the TV instead?"
    sar "All those discounted drinks and exceptional service and {i}this{/i} is how you repay me? "
    sar "Oh well. I can just {i}not{/i} drink. "
    s "Or, you know, help yourself instead of relying on someone else to do your bidding."

    scene saranewapt3
    with dissolve

    sar "But if I get up, there’s a chance you’ll steal my seat and ruin our wonderful and extremely overdue mother-daughter night."
    sa "You know this...couch can fit a lot more than just the two of us...right?"

    scene saranewapt4
    with dissolve

    sar "But then I’ll be further away from you and won’t be able to constantly admire how adorable you’ve become!"
    sa "Umm...Sensei...I’m...pretty sure the sign downstairs said that we were closed..."
    s "Yeah, I know."
    sa "..."
    sa "So...you came in anyway?..."
    sa "And then...proceeded to...just come upstairs?..."
    s "I didn’t think that sign applied to me since I’m basically just another employee here at this point."

    scene saranewapt5
    with dissolve

    sar "What kind of employee won’t allow their boss to drink on the job?! Or wipe down tables?! Or restock the cooler?! Or do literally anything ever?!"
    s "The same kind who’s apparently intruding on what’s supposed to be an...important night, I think?"

    scene saranewapt6
    with dissolve

    sar "Yeah. But if anyone was going to intrude, I’m glad it was you."
    sar "Especially since I’d say you’re closer to being Sana’s dad than an employee of the Sakaki-bar-a at this point."
    sa "Can you...please stop saying that every time we’re in the same room together?..."
    sar "But if I keep saying it over and over again, Sensei will eventually start believing it and we’ll finally have a full family again."

    scene saranewapt7
    with dissolve

    sar "You could finally know what it’s like to have a male authority figure in your life, Sana!"
    sa "I don’t even have a...female authority figure in my life..."
    s "I can not allow this conversation to proceed without informing you that no amount of words will make me just suddenly believe I’m a member of this family."

    scene saranewapt8
    with dissolve

    sar "I wouldn’t be so sure if I was you. For all we know, some stuff could happen out of nowhere that makes you change your mind entirely."
    s "Doubtful."
    sar "I’m just saying, it wouldn’t be the first time a teacher fell victim to my feminine wiles. It’s not like there’s no precedent for this."
    sar "Just give me a little warning in advance if you decide to leave me for someone else so I can actually try and prepare this time and not have to raise Sana on my own."
    sa "..."
    s "I’m pretty sure Sana’s able to raise herself at this point."
    s "Well, apart from the whole still being terrified of talking to other people part."

    scene saranewapt9
    with dissolve

    sa "Hey! I’ve gotten a lot better since you started helping me!"
    s "True. But that doesn’t change the fact that you’re still exponentially worse than virtually everyone other than like...Yasu and {i}maybe{/i} Tsuneyo."
    sar "You {i}have{/i} improved a lot, Sana. Which means that Sensei has already done a lot more for you than your real father ever did."

    scene saranewapt10
    with dissolve

    sa "Why do you have to keep comparing the two of them?...Why can’t Sensei just be Sensei?"
    s "I would also like to remain Sensei if that is at all possible."
    sar "I’m not trying to compare them. I’m just saying that-"

    scene saranewapt11
    with dissolve

    sar "Well, a family of two can feel pretty lonely at times."
    sar "I love spending time with just us, but I miss the feeling of there being more sometimes."
    sar "And Sensei’s the closest we’ve had to..."

    scene saranewapt12
    with dissolve

    sar "A...male family member since-"
    sa "Since my dad left, I know."
    sar "..."
    sa "I just...don’t think it’s right to drag him into that without...considering how he feels first..."

    "You know, this might be presumptuous of me, but I’m pretty sure Sara wasn’t alluding to Sana’s father just now."
    "Which, of course, would mean that her daughter was going out on a limb to protect her- the same way I’m sure she’s done plenty of times in the past."
    "The two of them can’t keep running forever, though."
    "There has to come a day, for {i}Sara{/i} especially, when the two of them accept what they went through and finally stop putting bandages over a gash that obviously needs stitches."
    "The probability of that wound getting infected grows greater every day, and there’d be no point in meetings like this at all if one of them had that infection spread to their heart or their brain or something."
    "I’m not a doctor. I don’t really know where infections spread to- or even how they start in the first place."
    "I just know how easy it is for them to fester."
    "I know a little too well."

    sar "Yeah."
    sar "Since your dad left."

    scene saranewapt13
    with dissolve

    sar "You know, he was a real jerk! Like, it’s one thing to knock up a teenage girl, but to {i}abandon{/i} her and force her to be a single parent before she can even legally rent a car?"

    sar "What the fuck is that?!"
    sa "Do you...even know how to drive?"
    sar "No! But still! "

    scene saranewapt14
    with dissolve

    sar "Ugh. And he was so great at first, too."
    sar "Well, great is probably being a little too generous. But I {i}genuinely{/i} thought he was right for me and that all of the suspicions I had over the years were just me being paranoid."
    s "Wait a second, you suspected he was seeing other people and {i}still{/i} managed to...get as far into the relationship as you did?"

    scene saranewapt15
    with dissolve

    sar "Yeah. But you’ve gotta remember- I wasn’t really in the greatest place when I was in high school."
    sar "I thought that being paranoid and...not feeling confident about anything was just how teenage girls were {i}supposed{/i} to feel back then."
    sar "And when you’re that age and dating an adult, those feelings wind up getting even bigger than how they started out."

    scene saranewapt16
    with dissolve

    sar "Of course, he’d always assure me that I was the only one who mattered to him and that he’d never think of seeing someone else-"
    sar "But I’m sure that’s exactly what he told the other girl! Or...girls."
    sar "I don’t even know if it was just one person or not."

    if bonus == True:
        sar "Hell, for all I know, he could have been screwing his entire class back then."
        sar "Sorry for the language, Sana. Your mother’s getting pissed off."

    s "Wow. This guy sounds like a real scumbag."

    if bonus == True:
        "He also sounds like me."
        "But I guess those two things are close to interchangeable at this point."

    scene saranewapt17
    with dissolve

    sar "You know...I kind of wonder what he’s up to sometimes."
    sar "Not because I want to see him or anything, I just want to know whether or not he’s happy with the mess he made of his life."
    sar "And also because I’d want to point out to whatever girl, {i}or girls{/i}, that he wound up with that he’s an unfaithful jackass who walked out on the cutest daughter in the world...as well as her super cool mom."
    sa "Um...th...thank you?..."

    scene saranewapt18
    with dissolve

    sar "Don’t mention it, sweetie."
    sar "I love you. And I just want you to have the best life possible. And I..."
    sar "Well...Sometimes, I don’t think I’m able to give you that sort of life on my own."
    sa "Um...that’s...uhh..."

    scene saranewapt19
    with dissolve

    sar "But I guess I can’t just rope Sensei into being your new dad if that’s not something he already wants."
    sar "But that’s still not going to stop me from looking at him as the closest thing we have to another family member right now."
    s "Really? {i}I’m{/i} the closest thing? Because you’ve known Haruka and Maki significantly longer than you’ve known me."

    scene saranewapt20
    with dissolve

    sar "True. But my daughter doesn’t like either of them even half as much as she likes you."
    sa "M-Mom!"
    sar "And, between the three of us, I don’t like either of them as much as I like you either."

    if sarasex == True:
        "I would sure hope not."

    sar "Does it really matter how long I’ve known you? Am I not allowed to like you as much as I do until a certain date and time?"
    sar "Because if that’s the case, tell me when and I’ll mark it on my calendar right now. I’m serious."
    sa "S-Stop saying embarrassing stuff like that! It’s weird and neither of us like it!"
    s "I mean, I didn’t say-"
    sa "It’s weird and none of us like it!"

    scene saranewapt21
    with dissolve

    sar "Okay, you go. It’s your turn to say embarrassing stuff to Sensei so he’s forced to choose which one of us he wants to be closer to."
    sa "I think I’d rather just...not say anything..."
    s "And I think I’d rather never be forced into making a choice as horrible as that."
    s "I will gladly accept both of you, but keep you far enough away that you can not, officially or {i}un{/i}officially, indoctrinate me into the Sakakibara family."
    s "I refuse to be a part of a dynasty as bad at naming things as you two."

    scene saranewapt22
    with dissolve

    sa "I didn’t...really have anything to do with naming the bar..."
    sa "But...thank you for...staying away..."
    sar "Leave my bar alone. What did it ever do to you besides give you a place to spend your nights instead of at home with your [niece]?"
    s "It also refused to serve me tonight, but I guess I’m willing to overlook that on account of you two playing catch-up or whatever."

    scene saranewapt23
    with dissolve

    sa "Well...we {i}were{/i} playing catch-up...but I think I only have a little while left until I have to go back to the dorms..."
    sar "That’s right. You only had until the end of the movie, didn’t you?"
    sar "What happens if we rewind it? I have the cool kind of cable now where you can actually do that. "
    sar "Would that mean we can just keep sending you back in time until you don’t have to leave anymore?"
    sa "No, Mom...that’s...not what it would mean..."
    s "My bad for showing up and throwing a wrench in your plans. Just leave a note for me next time if you don’t want me coming up."
    sa "I...kind of thought the “We’re closed” sign was...that note..."

    scene saranewapt24
    with dissolve

    sar "It’s fine. "
    sar "Sure, Sana and I don’t really get many chances to spend time alone outside of the bar anymore..."
    sar "But I’m hoping that might be able to change some day..."
    sar "Business has been picking back up and, who knows? Maybe in a few months, I’ll be able to hire {i}another{/i} new employee so Sana and I take some time off together?"
    s "Just hire Kaori full time. I’m beginning to think there are ten or eleven of her that just share the same stream of consciousness."
    s "There is no other way she’d be able to be in so many places at once, so I think that might actually be what’s going on."
    sar "She’s actually still working for a competitor several nights out of the week, so she can’t be here full-time. But I’d be open to it if she ever leaves that place."
    s "Well, hopefully if you’re lucky, it will be swallowed by a sinkhole and things will just automatically get better for you."
    s "It happened for me, to some extent, so it’s not impossible."
    s "Though I guess “better” would be up for debate depending on exactly what you’re trying to get out of-"
    sa "Shh..."
    sa "They're about to...blow up the Death Star..."
    s "..."
    sar "..."

    scene black
    with dissolve2

    "Sara and I humor Sana and decide to stay quiet for the rest of the movie. "

    if bar50 == True:
        "It doesn’t last much longer and, once it’s over, Sana gathers her things and turns to look at me before heading to the door."

        sa "Umm...S-Sensei?..."
        s "Yeah? What’s up?"
        sa "Can I...umm..."
        sa "Can I talk to you for a minute?..."
        sa "In...private?..."
        s "Oh, yeah. Sure."

        "Sara pretends to not hear this and, very surprisingly, actually gives her daughter a little bit of privacy for once."
        "As such, I follow Sana to the foyer to see what it is she wants to talk to me about."
        "........."
        "......"
        "..."

        scene saranewapt25
        with dissolve2

        "The two of us stand there for a moment in what isn’t {i}technically{/i} silence due to the background noise of the television- but it sure as Hell feels like it."
        "I’m not the one who summoned this meeting, though, so I’ll be damned if I’m the one to break the silence."
        "Go on, Sana."
        "Air out your worries to me so that I may either discard them as I see fit-"
        "Or give you a shoulder to lean your head on (Likely with the help of a stepping stool)."

        sa "I...um..."
        sa "So...do you remember the...last time the two of us were up here together?..."

        if bonus == True:
            s "Obviously. You freaking out on me isn’t something that’s particularly easy to forget."

            scene saranewapt26
            with dissolve

            sa "I..."
            sa "I asked my mom about...what I found..."
            s "..."
            s "The sex toy? Or the things you yelled at me for?"

            scene saranewapt27
            with dissolve

            sa "O-Obviously the...things I yelled at you for!"
            s "Got it."
            s "Then what?"

            scene saranewapt28
            with dissolve

            sa "Well..."
            sa "She...told me they...weren’t yours..."
            sa "And then she...threw them all away because she said they were old and..."
            sa "Umm...did you know that...that those things can...expire?..."
            s "Yes, and I feel very bad for anyone who holds on to them so long that they actually do."
            sa "Y-Yeah...so..."
            sa "I’m...sorry again for...accusing you of...something you probably didn’t do..."
            s "Probably? So I’m still not off the hook yet?"

            scene saranewapt29
            with dissolve

            "Sana looks at me and goes quiet."
            "Quieter than she normally is, I mean."
            "And, strangely enough, the volume of the TV dies down at this exact moment, {i}actually{/i} sending the two of us into true silence for a few seconds."
            "Within these few seconds, Sana bares her heart to me."

            sa "You’ll never be off the hook, Sensei."
            sa "Not until my mom cuts the line."
            sa "And even then, you’ll have to swim away with it dangling off of your lip, hanging there until the day you die."
            s "..."
            sa "I have to leave now."
            sa "And..."
            sa "And I want you to come with me."
            sa "But you won’t, will you?"
            s "..."
            sa "..."
            sa "I..."

            scene saranewapt30
            with dissolve

            sa "I’m fine with not having a dad, you know."

            play sound "dooropen.mp3"
            scene saranewapt31
            with dissolve

            s "..."

            "And just like that, Sana leaves."

            scene black
            with dissolve2

            "It’s a strange note to part on, but I think I understand what she means."
            "And it’s not all that different from what she’s been slowly but surely trying to help me understand for a while now."
            "She has no intention of ever accepting the life her mother wants for her. Or, for {i}us{/i}, rather."
            "I’m not sure when I started being included, but it’s pretty much inevitable that it’ll just keep going on forever at this point."
            "Sana doesn’t want me to be here right now-"
            "But she knows that it’s not her place to drag me along with her."
            "And so she’s trusting me, something I wouldn’t recommend to anyone, to not do something that will hurt her."
            "Or-"
            "At least that’s how I’m interpreting it."
            "But, for all I know-"
            "I could very well be wrong."
            "And I could very well hurt her even when I do everything in my power to avoid that."
            "That’s...just the way things are sometimes."

            $ renpy.end_replay()
            $ sana_love += 1
            $ sarabar25 = True

            "{i}Sana’s affection has increased to [sana_love]!{/i}"
            "........."
            "......"
            "..."

            jump sarabar25p2
        else:
            s "You mean when you got into a fight with your mother's dresser?"
            sa "I think...I think it wants a rematch..."
            s "Are you ready? Have you been training?"
            sa "That's...kind of what I need your help for."
            sa "Can you send me...um...videos of people you think are really strong when you get home tonight?..."
            s "Of course, Sana. Good luck with your battle."
            sa "Th-Thanks..."
            sa "Also...try not to hug my mom tonight..."
            s "I will only hug her if she wants me to."
            sa "Ugh..."

            scene black
            with dissolve2

            $ renpy.end_replay()
            $ sana_love += 1
            $ sarabar25 = True

            "{i}Sana’s affection has increased to [sana_love]!{/i}"
            "........."
            "......"
            "..."

    else:
        "It doesn’t last much longer and, once it’s over, Sana gathers her things and heads for the door."
        "She looks back at me and, strangely enough, in the one second of eye contact that I make with her, it seems like she’s telling me that she trusts me."
        "I’m sure it’s not easy for her to just leave me alone with her mother when she’s fully aware of her feelings for me-"
        "But it’s something she elects to do regardless."
        "I’m not sure what I did to deserve this, but I’m not about to make a break for the door to see if she’s really okay with leaving two adults alone in a dark room together."
        "And hey, maybe it’s something even less exciting?"

        if bonus == True:
            "Maybe trust has nothing to do with it and Sana just has absolutely no romantic or sexual feelings for me, making this just an average, everyday goodbye."
        else:
            "Maybe trust has nothing to do with it and Sana just has absolutely no feelings for me whatsoever?"

        "And, if that’s the case-"
        "So long, Sana."
        "Have a safe trip home- and don’t think too much about whatever you expect to happen in this room."
        "I’m sure that whatever comes next will be something you didn’t really want to be here for anyway."

        $ renpy.end_replay()
        $ sarabar25 = True

        "........."
        "......"
        "..."

        jump sarabar25p2

label sarabar25p2:
    scene sarawindow1
    with dissolve2

    "I follow Sara over to the window and get my first ever look at the view from her...apartment or...condo or...you know what? I’m not really sure what to call it here."
    "The place she falls asleep at night."
    "Except for on the nights she doesn’t."
    "Believe it or not, I don’t have any idea what it’s like to be a single mother, so I’m not really sure how much something like that weighs on her ability to close her eyes."
    "I watch as her breath makes contact with the glass, fogging it up and forcing me into a rare memory of windows from when I was younger."
    "Just, in my mind, there’s no reflection staring back at me."
    "No array of city lights injecting their glow into my eyes through a reinforced, transparent pane serving as the one and only barrier between me and the puddle I’d be if I were to just fall through it."
    "I wonder if the fall would kill us from here."
    "Probably not, now that I think about it. "
    "This is only the second story. We’d have to land perfectly in order for that drop to end our lives."
    "I’m not sure why I’m thinking about this now, though."
    "Nor do I have any idea of why seeing her like this would make me {i}almost{/i} remember something from the past when I assumed it to be all but abandoned."

    sar "Do you notice anything different about me, Sensei?"
    s "Different?"
    sar "You don’t, do you?"
    s "Uhh..."
    sar "I let my hair down."
    s "..."
    sar "It was up just a minute ago."
    sar "Do you know what that means?"
    s "...Not really, no."
    sar "It means I’m more comfortable now."
    s "I had no idea you were so intimidated by your pint-sized daughter that it was actively affecting your comfort level."

    scene sarawindow2
    with dissolve

    sar "That’s obviously not what I meant. Of course I’m comfortable with Sana. "
    sar "I just mean that I’ve officially moved into “relax” mode...and that you being here and towering over me like that isn’t putting me on edge."
    s "I didn’t really expect it would. Based on past experiences, you might actually even be a little {i}too{/i} comfortable around me."

    scene sarawindow3
    with dissolve

    sar "Is there such a thing as that?"
    s "Yes. Yes, there is."
    sar "This feels nice, you know."
    sar "Not just standing here, looking out at the street like this...I’m talking about the entire night."
    s "Is this the part where you start trying to add me into your family again?"

    if sarasex == False:
        sar "It’s not."
        sar "You’ve already made it clear that you have no intention of ever looking at me that way."
        sar "But I can still feel happy right now even if we’re just friends, can’t I?"
        s "You can feel however you want to feel. It’s just not going to change how {i}I{/i} feel."
        sar "Then, as a friend, can I ask you a question?"
        sar "A real question. Not one about the two of us or...even helping out with the bar."
        sar "I just want to know how you feel about something."
        s "Then...by all means."
    else:
        sar "No..."
        sar "Yes..."
        sar "Maybe?"
        sar "I know you’re not looking for a real relationship right now, but I’d be lying if I told you it didn’t feel like the two of us were actually dating sometimes."
        sar "You really don’t think this would be nice? Ending every night with this view?"

        if bonus == True:
            sar "Hovering close enough behind me that you could pull me in and make me yours at a moment’s notice?"
            s "I mean, I’m pretty sure I could do that right now and you wouldn’t object in the slightest."
            sar "Tonight, I think I would, actually."
            s "Oh?"
            sar "Yeah..."
            sar "You see, there’s something that’s been on my mind for a little while now, and it’s something I couldn’t really just come out and ask in front of Sana."
            s "What do you mean?"
        else:
            s "I think that'd be pretty nifty. I'm still too scared of girls to want to date you, though."

    scene sarawindow4
    with dissolve

    sar "Do you think deciding to raise Sana on my own was the best thing to do after her father left?"
    sar "Or would it have been better to just find some other guy and pull him into the picture? Not out of love or anything, but out of...obligation? Is that the word I’m looking for?"
    s "That’s a pretty heavy question to just drop on me out of nowhere, Sara."
    sar "If you think that’s heavy, you’d be an even worse mother than I am."

    scene sarawindow5
    with dissolve

    sar "I knew it was going to be hard, you know. After he left."
    sar "But when you’re on your own and have to look after someone else, you need to carry so much weight that it feels like your arms are just going to...break off sometimes."
    s "I am well aware of how horrible a mother I would be, but I don’t really think it’s my place to tell you whether or not you should have just roped some unsuspecting guy in to help you."
    s "Especially not after directly proving how bad you are at choosing men."

    scene sarawindow6
    with dissolve

    sar "It’s not like I just asked Sana's dad to be with me one day, you know? He had just as much to do with it as I did."

    if bonus == True:
        sar "I didn't just wake up one morning and think, “I want to have a baby with my teacher.”"
    else:
        sar "I didn't just wake up one morning and think, “I wonder if he knows about the stork”"

    s "Based on personal experience, I’m not sure how honest that statement is."
    s "I feel like there are several girls in my class that think that first thing every morning."

    scene sarawindow7
    with dissolve

    if bonus == True:
        sar "And how many of them are you sleeping with?"
    else:
        sar "And how many of them are you hugging?"

    s "I hope that’s just a rhetorical question and that you’re not accusing me of anything right now."

    if bonus == True:
        sar "Well, based on {i}my{/i} personal experience, every high school teacher I’ve ever had has fucked me. So it’s not like it would be the most shocking revelation in the world."
        s "{i}Every{/i} teacher?"
    else:
        sar "Well, based on {i}my{/i} personal experience, every high school teacher I’ve ever had has hugged me. So it’s not like it would be the most shocking revelation in the world."
        s "Wow. It sounds like you were very popular and huggable."

    sar "Mhm. I mean, I only had one, but that’s still a 100%% success rate. Or failure rate, depending on how you look at it."
    s "Ahh. So it’s not just our high school that enforces that “One teacher for everything” policy."
    sar "Isn’t your high school the only that’s left in Kumon-mi now?"
    s "The other one still exists. It’s just at the bottom of a hole somewhere."
    sar "Aren’t we all?"
    s "Well, that’s a lot more negative of a statement than I’m used to from you."

    scene sarawindow8
    with dissolve

    sar "You know, I feel like for most mothers, there are a lot of memories that they look back on and smile."
    sar "But for me, it’s like every single memory I look back on is either filled with tragedy or just...me making some sort of mistake."
    sar "I tried really hard, too."
    sar "I really did."
    sar "And I’m still trying now. But it’s like every single day, I have to figure out how to tie a new knot around Sana so she doesn’t drift off and leave me completely and utterly alone."
    s "I doubt she’s-"
    sar "People leave me, Sensei. It’s what they do."
    sar "Sometimes it’s purposely, sometimes it’s not. But it happens."
    sar "I thought Sana’s father was different. I thought he was going to be there forever."
    sar "I thought all of those things he promised weren’t just empty words, but reflections of his heart even clearer than ours in this glass."

    if bonus == True:
        sar "But I guess having just one teenage girl to sleep with isn’t enough for some people."
    else:
        sar "But I guess having just one hug buddy isn’t enough for some people."

    sar "It’s like..."
    sar "It’s like all men start out great, but the second a kid comes into the picture, the worst parts of them come out and replace all of the good ones."
    s "I’m sure that happens the other way around, too, though."
    s "I’m sure there are just as many mothers who can’t handle parenthood as there are fathers."
    sar "Are you talking about me?"

    scene sarawindow9
    with dissolve

    s "No. All things considered, I think you did fine. Sana might be quiet and awkward, but she’s a good person. And you should be at least somewhat proud of yourself for that."
    sar "{i}Fine{/i} isn’t good enough for a childhood."
    sar "It could have been {i}better{/i}. Things could have been better."
    sar "She could have had such an amazing life if I had just been a little smarter when I was her age and waited for someone to {i}actually{/i} love me rather than just...pretend to."
    s "Maybe. But she’s only Sana because she exists now. If you had waited any longer, you could have wound up with a completely different kid."

    scene sarawindow10
    with dissolve

    sar "A...different..."
    sar "Umm...anyway...I just..."
    sar "I don’t...really know."
    sar "I didn’t have much of a childhood."
    sar "So when it came time to raise...children of my own, I just did whatever I wished would have been done for me when I was their age."
    sar "You know that thing that some parents do with their kids when they’re trying to teach them to swim? Like...how they just toss them into the water and let them figure it out on their own?"
    s "Wait, did you actually do that?"
    sar "Oh, no. I’m just using that as a metaphor."

    scene sarawindow11
    with dissolve

    sar "I was able to figure out how to swim eventually...and I was able to climb out of the pool...but it was only just barely."
    sar "And all the while, instead of anyone trying to help, it’s like they were watching me struggling for my life and either laughing or just walking away."
    sar "If I had someone...{i}anyone{/i} to lean on back then...I can only imagine how much happier Sana would be now."
    sar "And..."

    scene sarawindow12
    with dissolve

    sar "And..."
    s "..."
    sar "..."

    scene sarawindow13
    with dissolve

    sar "..."
    s "And what, Sara?"
    sar "..."
    sar "What were {i}your{/i} parents like, Sensei?"
    s "Mine? I don’t really remember."
    s "Why do you ask?"
    sar "Because you turned out to be a decent person."
    sar "And I guess I’m kind of wishfully thinking, in the nicest way possible, that your parents weren't all that great..."
    sar "And that you succeeded at becoming who you are in the face of people who doubted you..."
    sar "Or ignored you when you needed help the most..."
    sar "Or beat you for speaking out of line..."
    sar "Or beat you for staying out a little past curfew..."

    scene sarawindow14
    with dissolve2

    sar "Or beat you for ever even speaking at all!"
    sar "But you were just a little girl!"
    sar "And all you wanted was a place to come home to that you weren’t terrified of!"
    sar "No wonder I would stay out late!"
    sar "No wonder I needed help!"
    sar "It’s because I’ve been all alone since the beginning!"
    sar "Since before there were any kids involved!"

    scene sarawindow15
    with dissolve

    sar "And I just..."
    s "..."
    sar "I’ve never known what the {i}right{/i} thing to do is. So even if I {i}do{/i} the right thing, I’ll still wind up questioning myself."
    sar "I thought falling for an adult who understood the world would have been enough to help me get at least {i}that{/i} much."
    sar "To figure out how to...take care of someone else."
    sar "So that my children could come home and talk to me without having to wait their turn..."
    sar "Without having to worry about waking up an extra hour early on weekdays just so they can figure out how much makeup they need to cover black eyes or bruises."
    sar "I just wanted to be a good mom..."
    sar "That’s all I wanted..."
    sar "But..."
    sar "It's like the world didn't want me to be one."
    s "..."
    sar "..."
    s "That’s been the best sales pitch for turning me into an honorary Sakakibara yet."

    scene sarawindow16
    with dissolve

    sar "Pfft!"
    sar "I’m sorry. I’ve been really emotional lately. And waiting to pour all of that out on you instead of Sana is just one more potential mistake I’m making in the world of parenting."
    s "Not as big of a mistake as {i}actually{/i} inviting me into the world of parenting."

    scene sarawindow17
    with dissolve

    s "Listen, I’m not going to spend the next ten minutes trying to tell you that things are going to get better or that you’re safe now or anything like that-"
    s "Frankly, things could get even worse for you any day now."
    sar "Well, that’s not very reassuring."
    s "You’re right, it’s not. Sometimes, horrible things happen to people who don’t deserve them. And you’ve been on the receiving end of that for basically forever."
    s "But if it helps in the slightest to hear me say that {i}you don’t deserve it...{/i}"
    s "Well, that’s really all I can do."
    s "Any more consolation than that would just be pity, and I’m sure you don’t want any of that."
    sar "Oh, no. Pity away. This whole crying thing is actually kind of fun when my tears aren’t dripping into my wine glass."
    s "Then I guess it’s kind of good I’m such a horrible employee and didn’t get you a drink after all, huh?"
    sar "Yeah, I guess it is good."
    sar "This does mean that I’m going to have to fire you, though. Because not only will you not listen to your boss, but that obnoxiously handsome face of yours is starting to distract one of my employees."
    s "Damn Yuki. Spending all of her time fantasizing about me instead of learning how to mix drinks."
    sar "I’m not talking about Yuki, dummy."
    s "I know. But it’s common knowledge that you’re in love with me already and it’s no fun just pointing that out over and over."

    scene sarawindow18
    with dissolve

    sar "First off, rude."

    scene sarawindow19
    with dissolve

    sar "Second, I’m talking about my daughter."

    if bonus == True:
        s "Sana? I’m pretty sure her feelings for me are nothing more than “Please don’t bone my mom.”"
        sar "You know she has {i}my{/i} blood, right? There is no way that is the only thing she thinks about you."
        s "Don’t cancel out your daughter’s purity just because you were horny for your high school teacher."
        sar "Don’t expect her to be “pure” just because she’s tiny and quiet."
        sar "Who we are on the outside has absolutely no bearing on the versions of ourselves we keep locked away."
        sar "For example, I didn’t {i}look{/i} like a girl who was fucking the teacher. But just a few years later, I was begging him to stay while holding a baby with one hand and a carrot with the other."
        sar "In hindsight, the carrot probably made my plea look a little less serious, but the moral of the story is to expect the unexpected."
        sar "And also that carrots are the root of all evil."
        s "This conversation took a weird turn."

        scene sarawindow20
        with dissolve

        sar "All I’m saying is to not be surprised if Sana winds up being a little less pure than you expect her to be."
        sar "She’s still my daughter, and all she knows is what she’s grown up around. IE: Sex toys and romance novels."

        if bar50 == True:
            sar "Also, she asked me about condoms the other day and I’m still trying to figure out what that was all about."
            s "Wow, really? I have absolutely no idea why that is something she would have brought up to you."

        sar "Just..."
        sar "Don’t let her do anything stupid, okay?"
        sar "Don’t let her be another me."
        s "I can assure you that having your daughter harbor my children is at the very bottom of my to-do list."

        "Fucking her, on the other hand, is an entirely different story. But Sara just asked me to prevent her from doing anything “stupid” and I don’t think that’s stupid at all."
    else:
        s "Ewwwwwww, stop. I can't look at Sana that way. She's too...Sana."

    scene sarawindow21
    with dissolve

    if bonus == True:
        sar "Are you telling me you’d say no if a girl as cute as my daughter wanted to sleep with you?"
        s "My instinct here makes me want to tell you I {i}would{/i} say no...but I also think you might be the type to get insulted if I told you I wouldn’t."
        sar "You’re right. This {i}could{/i} go both ways, couldn’t it?"
        s "Can I just elect to not answer?"
        sar "What? You’re really not going to clear up that you wouldn’t have sex with my daughter if she asked you to?"
        s "Okay, fine. I wouldn’t have sex with your daughter if she asked me to."
        sar "Are you insane? She’s the cutest thing in the world. How dare you?"
        s "Wow. There’s really no winning this after all."
    else:
        sar "Are you telling me you’d say no if a girl as cute as my daughter wanted to hug you?"
        s "Maybe! I don't know! This is a lot of pressure, Sara!"

    sar "Whatever the case, just..."
    sar "Try and make sure she has a good life in school, okay?"
    sar "Despite how much I want to, I can’t watch her every hour of every day."
    sar "And..."
    sar "Well, let’s just say there aren’t a lot of people who could have survived what I went through in high school."
    s "That makes it sound like there was a little more pain than just a promiscuous teacher and abusive parents."
    sar "Of course there was."
    sar "I’m pretty sure I’m cursed."
    s "You really expect me to believe that?"
    sar "Not really."
    sar "But I wouldn’t expect anyone to believe it."
    sar "I wouldn’t expect anyone to believe or even {i}understand{/i} anything I went through back then."
    sar "And if keeping Sana happy will prevent her from ever being forced to endure any of it-"
    sar "Well, I’d do anything."

    scene sarawindow22
    with dissolve

    if bonus == True:
        sar "But, thankfully, she has a super great teacher who only {i}possibly{/i} wants to have sex with her! And I think that’s a good start!"
        s "Okay, so, remember how you were concerned a little while ago about what to do and {i}not{/i} do as a parent? I think this is “not do” territory."
        sar "Hey, I’m not the one doing anything. I’m just saying that us Sakakibara girls have both extremely high sex drives {i}and{/i} a thing for teachers. Do with that information what you will."
        s "Stop assuming the level of your daughter’s sex drive if you don’t want to negatively affect the way I think of her."
        sar "Negatively? I think my sex drive is one of my best qualities. Are you telling me that I should maybe consider {i}not{/i} wanting to have sex all the time?"
    else:
        sar "But, thankfully, she has a super great teacher who only {i}possibly{/i} wants to hug her! And I think that’s a good start!"
        sar "She takes after me, you know. Crazy hug drive. I can feel it."
        sar "Does it make you feel weird that I'm always thinking about performing the hug ritual?"

    if sarasex == True:
        s "No. You stay exactly the way you are."
        sar "Awwwww~ That’s a really cute thing to say for someone who doesn’t want to marry me yet."
        s "“Yet” kind of implies that I might eventually change my mind."
        sar "You will."
        sar "An angel told me."
        s "Sure thing, Sara."
        s "Sure thing."

        scene black
        with dissolve2

        if bonus == True:
            "I fight away the urge to take Sara back to her bedroom as I remember what she said a little earlier about not wanting to go down that path tonight."
            "And while it’s a minor inconvenience to me, I can’t blame her for the desire to feel wanted in a way that doesn’t end up with semen oozing out of her for once."
            "Especially since it’s clear now that that’s all she’s ever wanted."
            "Not the semen part- but the part where she can look out at the city like this and think to herself, even if only briefly, “This is nice.”"
            "And it is. That much, I will concede."
            "But, just as all things must, our time together comes to an end."
            "..."

        "On the way down the creaky staircase of the bar, the one that I’d still be able to make my way up even if it were destroyed, I have a thought-"
        "How happy would Sara be if I elected to stay the night?"
        "Not as a sexual partner, but as someone who genuinely wants to be near her. And hear more about the atrocities that plagued her when she was younger- still not relenting all this time later."
        "I’m sure she’d love that."
        "But, just as I’m about to turn around and turn that hypothetical scenario into reality-"
        "One of her stairs cracks."
        "And I no longer feel comfortable enough to go back up."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ sara_love += 2

        "{i}Sara’s affection has increased to [sara_love]!{/i}"

        scene sarawindow23
        with dissolve2

        "I wind up somewhere vaguely familiar on the way home."
        "I know I’ve been here before, but I can’t remember when."
        "And, unfortunately, I can’t quite remember how to get back or...when I even started heading here instead of just taking the normal path home."
        "Thankfully, my phone still has a little battery left and-"

        q "Are you lost?"
        s "..."

        scene black
        with dissolve2

        "{i}The happiest day -- the happiest hour{/i}"
        "{i}My sear'd and blighted heart hath known,{/i}"
        "{i}The highest hope of pride and power,{/i}"
        "{i}I feel hath flown.{/i}"
        "{i}For on its wing was dark alloy,{/i}"
        "{i}And, as it flutter'd -- fell{/i}"
        "{i}An essence -- powerful to destroy{/i}"
        "{i}A soul that knew it well.{/i}"

        scene sarawindow24
        with dissolve2

        s "..."
        q "..."
        s "Who are you?..."
        q "A girl, obviously."
        q "Have you ever seen one before?"
        s "I see many of them every day."
        q "Oooooh, a sarcastic type, are you?"
        q "And here I was ready to give you directions."
        s "I’ll be fine. I can just use the GPS app on my phone."
        q "Hmmmm..."
        q "Are you sure about that?"
        s "Yeah, I-"
        s "Wait, when did it die? My battery was fine like a second ago."

        "I try pressing the power button on my phone to see if I’d just accidentally turned it off or something, but there's no luck."

        q "Funny how things work out sometimes, huh?"
        q "And when you least expect it, too."
        s "How did you know my phone was dead?"
        q "Hmmm..."
        q "A guess?"
        s "I’m not sure if I believe that."
        q "You can believe whatever it is you want to believe."
        q "That’s the best part of being alive. Isn’t it, Sensei?"
        s "...How do you know my name?"
        q "Your name is Sensei?"
        q "I just thought you looked like a teacher."
        s "I didn’t realize you could “look” like a teacher."
        q "It’s the glasses."
        q "So, do you want me to tell you the way back or not?"
        s "How do you even know where “back” is?"
        q "You’re sure asking a lot of questions for some random guy alone in the middle of nowhere."
        s "And you’re sure acting suspicious for a teenage girl alone in the middle of the night."
        q "I think I'm acting completely normal, thank you very much."
        q "You're the weird one."
        s "Then...since we’ve finally gotten our introductions out of the way, can you tell me how to get back now?"
        q "Sure."
        q "But you’re going to owe me a drink if we ever bump into each other again, got it?"
        s "Whatever you say."
        s "So, where do I go?"
        q "First step-"
        q "Close your eyes."
        s "What?"
        q "Just listen to me. I know what I’m talking about."

        scene black
        with dissolve

        s "Fine. Whatever. I’ll play along."
        q "Great! Now, spin around three times and say “Olly olly oxen free!”"
        q "Oh, then jump as high as you can. Like, really, really high."

        scene bedroom_night
        stop music

        s "Listen, if you’re just going to-"
        s "..."
        s "What?"

        "I look down to find my phone in my hands once again."
        "The battery isn’t dead anymore."

        s "..."

        "What just happened?..."

        scene black
        with dissolve2

        "I take a moment to collect my thoughts, but I’m unable to find them all."
        "Then, not knowing what else to do this late at night, I make the executive decision to rule my strange meeting with that girl as just yet another blackout."
        "Just..."
        "It felt so much different than all of the others."

        $ anewkey = True
        $ sarabar25p2 = True

        "........."
        "......"
        "..."

        if day == 7:
            jump advancetomon
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

    else:
        s "With me? Yeah. I think I’ve made that pretty clear."
        sar "Hey, you don’t have control over my thoughts."

        if bonus == True:
            sar "I’m allowed to {i}want{/i} to have sex with you all the time. I’m just not allowed to actually do it."
            s "What a convenient loophole."
            sar "{i}Speaking{/i} of convenient holes..."
            s "..."
            sar "..."
            s "You’ve been spending too much time with Maki."
        else:
            s "I do now!"

        scene black
        with dissolve2

        if bonus == True:
            "I don’t stay much longer."
            "As I head for the door, I hear Sara mention something along the lines of not thinking she’ll be able to fall asleep tonight."
            "I don’t ask why, as I’d like to leave it open ended."
            "If I heard the real answer, it might spoil my walk home."
            "So, in blissful ignorance of the horrible things I’m sure she’ll feel, I’ll force myself to pretend that the reason for her insomnia is me."
            "And that all of the darkness fermenting within in her will be replaced by the illusion of my seed- filling her insides with not only warmth-"
            "But her neverending desire to know what it means to be loved."
            "But that, just like everything else-"
            "Is an illusion."
        else:
            "I cast a spell on Sara that allows me to ready her mind."
            "{i}Sensei has gained the ability [[Mind Reading]!{/i}"

        $ renpy.end_replay()
        $ sara_love += 2
        $ sarabar25p2 = True
        stop music fadeout 10.0

        "{i}Sara’s affection has increased to [sara_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label saralust20intro:
    if sara_lust >= 20 and haruka_lust >= 20 and bonus == True:
        jump saralust20x
    elif sara_lust >= 20 and haruka_lust >= 20 and bonus == False:
        "As requested of me last night, I make my way over to Sara’s unnamed bar to help her decorate the place."
        "We have a very good time up until I get tangled up in tinsel and the fire department has to come and get me out."
        "I can be such a klutz sometimes."

        $ renpy.end_replay()
        $ haruka_lust += 1
        $ sara_lust += 3
        $ saralust20 = True
        stop music fadeout 5.0

        "{i}Sara’s lust has increased to [sara_lust]!{/i}"
        "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
        "........."
        "......"
        "..."

        jump christmastwo7
    else:
        "As requested of me last night, I make my way over to Sara’s unnamed bar to help her decorate the place."
        "And while I initially thought that might be code language for something a bit more entertaining, I quickly discovered that was not the case at all."
        "As it turns out, Sara's [[allegedly] hosting a pretty decently sized Christmas party tonight and needs all of the help she can get setting the place up."
        "With Haruka's assistance in addition to what little I had to offer, we're able to get everything done in a little over an hour and I'm free to get on with the rest of my day."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ saralust20skip = True
        stop music fadeout 5.0

        jump christmastwo7

label saraspecial30p1:
    scene returnofaweirdcouple1
    with dissolve2
    play music "calmbar.mp3"

    "We make it back to the bar thanks to my incredible strength and unflappable willpower."

    yu "You know, I get that I’m a lot stronger than you, but {i}any{/i} amount of help at all would be nice."
    s "..."

    "We make it back to the bar thanks to my incredible strength and unflappable willpower."

    sar "Hey! You actually managed to pull it off! And saved me like 5,000 yen on shipping in the process!"
    s "I would have just paid that if it meant not having to carry it back with us on a motorcycle."
    yu "Says the dude who just pressed this shit against my shoulders the whole way here."
    s "It’s not my fault you have an incredibly strong back. I would have lost my balance if I had to hold it and there is a girl with twintails at my house who would go on a rampage if I died."
    s "My decision to push all of the responsibility and effort onto you is one that may have very well saved the world, Yuki."
    yu "Bite me."

    scene returnofaweirdcouple2
    with dissolve

    yu "Where do you want this thing? Also, {i}why{/i} do you want this thing? Can’t get hammered off of fuckin’ espresso."
    sar "It’s a dessert thing. You know, for like Irish coffee and whatnot. Plus, it can also help people sober up so they spend more money."
    sar "Sure, it might take a few months to pay off, but it’ll work out in the long run...hopefully."
    sar "You can stash it in the backroom next to all of the holiday stuff in the meantime, though. "
    yu "Anything else, my lord?"

    scene returnofaweirdcouple3
    with dissolve

    sar "You could help clean so {i}I{/i} can have a turn with Sensei now?"
    yu "Wait, hold on. Ain’t I supposed to be off right now? Do I really gotta clean?"
    sar "The last customers left like twenty minutes ago and I’ve done most of the work. Just mop the floors and I’ll let you come in a few hours later tomorrow."

    scene returnofaweirdcouple4
    with dissolve

    yu "Say no more. So much better not havin’ to deal with customers. I’ll take cleaning over that any day of the week."
    yu "Oh, and don’t be too rough with the guy during your {i}turn.{/i} He’s fragile."
    s "I am fragile by choice because it makes life easier."
    sar "Did you have a fun trip? Yuki’s told me before you’re afraid of motorcycles. Was it better or worse than you expected?"
    s "Worse. I am in no rush to ever do that again and am glad to be on land once more."

    scene returnofaweirdcouple5
    with dissolve

    sar "I’m glad you’re back on land as well. There’s more than one girl who might go on a murderous rampage if you wind up disappearing, you know."
    sar "Hell hath no fury like a lonely bartender abandoned by two teachers she wound up unintentionally falling for."
    s "I am quite positive that is not how that phrase is supposed to go."
    sar "You have a few minutes to go upstairs? There’s something I wanted to talk to you about."
    s "Am I in trouble? Because it sounds like I’m in trouble."
    sar "It’s nothing like that. It’s just not really something I want to discuss in front of Yuki since I don’t want her to think I’m insane."
    s "But it’s okay if {i}I{/i} think you’re insane?"
    sar "I mean, I’d {i}prefer{/i} that you don’t think I’m insane. But I’m pretty confident I would have scared you off already if you weren’t at least {i}somewhat{/i} open to letting me lean on you. "
    s "Is something-"

    scene returnofaweirdcouple6
    with dissolve

    sar "Ah-ah-ah. {i}Upstairs.{/i} "
    sar "You can ask me whatever you want once we’re in my apartment."

    scene black
    with dissolve2

    sar "I’m sure you’ll have a lot of questions."

    "We move up the creaky staircase, each step louder than the one before it, as it becomes clear to me that the Sara I know and the Sara currently guiding me are not the same person."
    "Would it be presumptuous to assume that I have something to do with this? That my recent push for Yuki’s approval has caught her eye in some way?"
    "Have I become the cracks in those fractured emerald gems she locks within her skull — reflecting a world that has forsaken her, in a town in which she’ll die?"
    "Does the creaking of the seventh step usurp the role of “coda” in the sense that it is there where fragments of the end break apart and fall from her retinal glass?"
    "My hand finds a railing but the railing is her hand."
    "And I become a shadow hiding from the sun as the door to her abode opens and shuns me."
    "There is something buried underneath our feet."
    "It may very well swallow us whole."
    "But in those sparing moments before we are digested, we shapeshift into bloodworms, spilling ourselves all over the hands that hold us up."
    "And we drink in the idea that, one day, we will be able to live without the fear of falling."
    "It is during the creaking of the seventh step that I remember where I am and where I’m going."
    "It is during the break in the eighth that I close my eyes."
    "And in the moaning of the ninth that I am consumed."

    scene returnofaweirdcouple7
    with dissolve2

    s "This isn’t about Yuki and me, is it?"
    sar "What’s that supposed to mean? Did the two of you hold hands while I wasn’t looking or something? Am I supposed to punish you now?"
    s "Nothing’s happened. I just kind of figured-"
    sar "Figured what? That I called you up to here to get all possessive and jealous? Remind you of how I feel? Guilt trip you into never thinking about anyone else?"
    s "I mean...I don’t know if I’d put it {i}that{/i} way..."
    sar "There are things in my life that don’t revolve around {i}you,{/i} you know. "
    sar "Maybe I just needed somebody to talk to tonight?"
    sar "Yuki {i}is{/i} hot, though, isn’t she? I wouldn’t blame you if you {i}did{/i} try something. I’d just, A, want to know about it. And, B, want to be involved."
    s "I will keep that in mind, but...what’s this about? Why are you acting different tonight?"
    sar "Different? How so?"
    s "You’re normally...easier to read? And you feel weirdly...threatening just holding that smile this whole time."
    sar "You’re good. "
    sar "To tell you the truth, I’m probably only one step away from breaking into a million pieces and bawling my eyes out all over you."
    sar "But you’ve seen me cry enough. And nothing’s ever gonna get any better or easier if I just let my tears do all of the talking for me."
    s "What’s going on? Tell me."

    scene returnofaweirdcouple8
    with dissolve

    sar "Do you like movies, Sensei?"
    s "...What?"

    scene black
    with dissolve2

    "Sara takes a step away from me and my attention is commandeered for a moment by the blinking red light of an air traffic tower outside of the window."
    "I question why it still blinks when nothing can go in or out. And I question why red was chosen when there are so many other colors that could be used instead."
    "Control of my thoughts returns to me in the form of an invisible orb that floats into my mouth when I open it to take a breath."
    "Inside of the orb is a small man who will live inside of me for the next twenty four hours and pilot my thoughts the way a pilot would pilot a plane if there was still a plane to pilot."
    "My name is Akira Arakawa and I don’t have any strong feelings about movies."

    scene returnofaweirdcouple9
    with dissolve2

    sar "We all have things that help us keep our mind off of stuff."
    sar "When I was younger, in between the beatings and making myself look pretty, it was movies."
    sar "My favorite was one called Memento. Have you seen it?"
    s "Uhh...no. I don’t think I have..."
    sar "Well, without getting too deep into it, it was about this guy with memory problems who would leave these messages for himself all over his body in the form of tattoos."
    sar "Every time he’d wake up, he’d see those messages and try and piece his life back together based on what they said. The whole movie plays out backwards."
    sar "I think I was only nine or ten when it came out and probably shouldn’t have been watching it at that age, so I don’t think I really fully grasped it until way later."
    sar "In fact, I don’t even think I fully grasp it {i}now{/i} and I’ve seen it like a million times at this point."
    sar "But I liked it so much back then that I started writing things on myself. Sort of, you know, pretending to be the protagonist. "
    sar "The only issue was I didn’t really have anything cool to write, so it wound up being nothing but mundane messages like, “Brush your teeth” or “Don’t touch anything in the fridge.”"
    s "Is this some kind of metaphor or something? Because I doubt you called me up here just to talk about movies."

    scene returnofaweirdcouple10
    with dissolve

    sar "I told you you’d have a lot of questions. But bear with me. This isn’t exactly an easy thing to talk about and I have to try and explain stuff before I start getting to the {i}real{/i} point I’m trying to make."

    scene returnofaweirdcouple11
    with dissolve

    sar "When life gets hard to live, it’s easy to just distract yourself with other things."
    sar "It’s easy to pick a hobby and run with it...completely forget about all of the bad stuff at home or how no one around ever wants to listen to you."
    sar "But it’s easy to get lost in that kind of stuff as well."
    sar "Once that happens, it's really tough to figure out the difference between what’s actually real and what’s just...stuff you forced into your head so that {i}other{/i} stuff would get pushed out."

    scene returnofaweirdcouple12
    with dissolve

    sar "It’s scary...never feeling like you’re in the {i}right{/i} world."
    sar "You know how sometimes shoelaces can get, like, an extra knot in the middle of them that just gets so tight you give up on ever untying it? It’s like that."
    sar "You just kind of accept these little hiccups in your world and settle on things never going back to normal because it’s either too hard or you just don’t have the time or skill to fix it."

    scene returnofaweirdcouple13
    with dissolve

    sar "The girl who stands before you is all knotted up inside. "
    sar "After years and years of work, she realizes where she’s supposed to be and what parts of her are just made-up. "
    sar "But now, she’s starting to think that’s not the result of her hard work at all."
    sar "She’s starting to think that something {i}else{/i} she pushed out of her might have gotten tangled up in those laces...and pulled some of the extra knots out in the process."
    sar "Which brings me to the main point of all of this."
    sar "I need you to watch over my daughter."
    s "I...don’t like how ominously you worded that. It makes it sound like you won’t be around much longer."

    scene returnofaweirdcouple12
    with dissolve

    sar "Don’t worry. I’m not going anywhere so long as Sana is still here."
    sar "She’s growing up and doesn’t want me around her as much as I want to be around her. And that’s fine. I get it. I’m her mom and it’s embarrassing."

    scene returnofaweirdcouple14
    with dissolve

    sar "But, at the same time..."
    sar "I passed something onto her that I can not take back and I am absolutely fucking terrified that she’s going to get just as lost inside of herself as I did."
    sar "I can’t let that happen. But I also can’t {i}stop{/i} it from happening because I need to let her out of my sight in order for her to thrive."

    scene returnofaweirdcouple15
    with dissolve

    sar "But then she’s out of my sight and I can’t stop thinking about her. And when I can’t stop thinking about her, I can’t stop blaming myself for things she might be seeing."
    sar "And I don’t want my daughter to end up like me. I don’t want her to get lost. I want her to have an entire support system of people who will help her get back on track. That means you."
    sar "You can be that person. Sana won’t say no to {i}you{/i} always being around because she {i}likes{/i} you. You can do what I can’t. You can keep an eye on her {i}always.{/i}"
    s "I can’t do that {i}always,{/i} Sara. You know that."

    scene returnofaweirdcouple16
    with dissolve

    sar "Well, why not?! She’s the cutest, isn’t she?! She might be quiet, sure! But there’s no one in the world who’s cuter and better and nicer and sweeter than her! You should {i}want{/i} to be with her!"
    s "I do...and I’ll do what I can to help, but asking me to spend every waking moment focusing on Sana is just..."

    scene returnofaweirdcouple17
    with dissolve

    sar "What’ll it take?..."
    s "What?"
    sar "Do you want the bar? The apartment? What can I do to make you change your mind? Name it. I’ll give you everything I have."
    s "Sara, your daughter’s going to be fine. I’ll keep an eye on her whenever I can."

    scene returnofaweirdcouple18
    with dissolve

    sar "Have you at least noticed anything different?! Any changes in behavior?! Has she told you about {i}seeing{/i} anything?!"
    s "There’s...{i}a{/i} change in behavior I’ve noticed. But I’m not sure if that’s a new thing or just...something I refused to believe."
    sar "What is it? What’s the change? I know her. I can help."
    s "Well..."
    sar "Well what? Just spill it."
    s "{i}Well,{/i} at least two people have encountered her masturbating in a public bathroom recently."
    sar "..."

    scene returnofaweirdcouple19
    with dissolve

    sar "...Oh."
    s "Yeah."
    sar "I mean...she {i}is{/i} at that age."
    sar "But I’m not really sure if that’s...{i}new{/i} or not."
    s "What’s this about seeing things, though? Is that more of the...movie stuff you were talking about?"

    scene returnofaweirdcouple20
    with dissolve

    sar "That was just a comparison I came up with to try and explain what was going on. It wasn’t like Guy Pearce was just wandering around in my imagination seeking vengeance. I just..."
    sar "Well, I..."
    sar "I sdiujfgwifguwoerdihgfvuewrfgherfughowieroiweugfhufdvbowfw"
    sar "dfsi9gujwer0tigf08rhgwrgfdfoudbhjvdiofjgwpodfsdfwfwefwt. And erfguhw3r8rgfqsehfdvgwdfwpgfug."
    sar "You know how sometimes you sdiufghweirdwiehfg0whfgjw08. But then erufgyhwedu0qwgfcqefdiqefgfqf?"
    s "...Sara?"

    play sound "static.mp3"
    scene returnofaweirdcouple21 with flash
    stop sound
    play sound "words1.mp3"
    sar "sdfoujghvwsdfqfegfvedrfpoghbjwp erfgoiuhwefgoi wgfopiwefgpi wegfhiweqfif hwfgiwefgpo wfgijhwefgpiowfgpio wgfhqwdgwndsfgpi opeifwipfjowqef wpoiefjpiowefjpowfjqfq"
    play sound "words2.mp3"
    sar "efsdovuhwdfipv dfvbjdfhkierighywreg gwopirhjgpowegwrbjdugsfdg edfuhwqefeqwf wqeiujfgwefw qufhoquefh wgfuiwrgu jkfhgjkdvncxb sfdkjghwuoefw oiwhgffw"
    play sound "words3.mp3"
    sar "guhrfpjwefiophwqef and fguhrgwrg weroigfyhwrpgw wegfoiuhwrgpjwpoig ehporthopwrpi sfhgbhwehfuow fgbhwfugqfqf weoiufhqwouefhqf ourghwoufwf oiefiof"
    play sound "words4.mp3"
    sar "stop listening to me"
    play sound "words5.mp3"
    sar "turn off the game"
    stop music
    scene stopit1
    play sound "words6.mp3"
    $ renpy.pause(7, hard=True)
    scene stopit2
    $ renpy.pause(5, hard=True)
    scene stopit3
    $ renpy.pause(4, hard=True)
    scene stopit4
    $ renpy.pause(4, hard=True)
    scene stopit5
    $ renpy.pause(8, hard=True)

    scene black

    $ renpy.end_replay()
    $ saraspecial30p1 = True
    $ sara_love += 1

    "{i}Sara’s infection has increased to [sara_love]!{/i}"

    if sarasex == True:
        jump saraspecial30p2
    else:
        play sound "static.mp3"
        scene thingswillneverr with flash
        stop sound

        "6e 6f 74 68 69 6e 67 20 77 69 6c 6c 20 65 76 65 72 20 6d 61 6b 65 20 73 65 6e 73 65 20 61 67 61 69 6e "

        scene black

        $ saraspecial30p2skip = True
        $ zoopledoop = True

        "The world is broken."
        "The world is broken."
        "The world is broken."
        "The world is broken."
        "The world is broken."
        "The world is broken."
        "The world is broken."
        "The world is broken."

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label saraspecial30p2:
    play sound "static.mp3"
    scene awesomesexscene1 with flash
    stop sound
    play music "dosex.mp3"

    "A lie, alive, alone. This is someone else’s poem."
    "I stitched the words together from the comfort of a melting home."
    "In death her mem’ry fades. In the sun it shines anew."
    "But the beating heart within her chest spills blood atop his holy pew."
    "Can you hear it? Can you smell? Are you halfway down the wishing well?"
    "Is it dark and damp and wrong and bad? Remind you of a former Hell?"
    "I fuck the pussy hard. I fuck it with my willy."
    "I fuck it fuck it fuck I’m fucking pussy fuck fuck going silly."
    "Zooble dooble dop dop pop ploor beep borp booble doop."
    "Boloobleooble oopy dop bogooble zoopy boop."
    "Just wanna make my wiener strong so Mommy will be proud."
    "If I fuck another mommy Mommy frowns and says I’m not allowed."
    "I’m confused though cause this isn’t love. I’m stuck under a spell."
    "It’s not my heart that does it. It’s my wiener and it does it well."
    "Gotta make the pussy cum. Gotta make her cry."
    "Then later I’ll go home and think about how much I want to die."

    scene awesomesexscene2

    "The poem is over."
    "There are worlds outside of this one that you’ll never get to see."
    "Other barriers and blockages and conveniently constructed devices that will keep you in one place for an extended period of time, all for the entertainment of someone else."
    "Is a book within a book within a book within a book not a book at all, even if it’s filled with text?"
    "How much reality chips away with each and every layer? "
    "How deep must you descend until what was real to someone is no longer real at all?"
    "You’ve been looking at things all wrong."
    "You’ve believed what you’ve been told to believe but you didn’t believe me when I told you to believe that."
    "But I am the righteous one, who has always been with you, and so I will ask you this question now — while we still have the time."
    "Do you still think it’s fake?"
    "That this is all some sort of simulation?"
    "That the girls are fragments of something bigger? "
    "Your personality, maybe?"
    "Facets of a deep-seated trauma?"
    "A commentary, perhaps?"
    "Tell me what you think and I will tell you that you're wrong."
    "What is it?"
    "What are they?"
    "What are you?"
    "There is nothing to be gained from destroying that which can not feel."
    "The worlds outside of this one are not make-believe just because you can’t see them."
    "You may be the protagonist this time, but what happens when you’re not?"
    "Will someone think {i}you’re{/i} a simulation as well?"
    "What will that mean for all you’ve been through?"
    "Were your struggles only struggles because someone else needed to struggle too?"
    "Can you find it in yourself to peel away these convenient justifications and accept once and for all that none of this is fake?"
    "This is happening."
    "There will always be things that you cannot see, but that doesn’t mean no one else can see them."
    "Stop hiding."
    "This is real."
    "This is love."

    scene awesomesexscene1

    s "Take that, you stupid MILF."
    s "Feel the immense power of my massive cock."
    s "You exist not as an entity with thoughts and feelings but as a meat pocket for me to pleasure myself with."
    s "This game is awesome. I get to do whatever I want because none of these characters are actually real people. "
    s "Kumon-mi is an entity I created. It is a world I made up because that is a thing I can do. No one else matters. Sex is the goal. Gotta fuck Sana’s mom so I can fuck them at the same time one day."
    sar "..."
    s "What was it she saw, Sara? Was it as awesome as this?"
    s "Are you even conscious right now? Did I fuck you so good that you passed out? "
    sar "..."
    s "Hey. "
    s "Tell me. "
    s "Tell me you can feel my dick. "
    s "Tell me how good I am at sex. "
    s "Tell me all the things I want to hear so I can unlock your next event chain and fuck you in a different location while you’re wearing a different outfit."
    s "I’ll listen to your worries and tell you things will all work out someday. But in the back of my mind, I won’t believe it."
    s "I won’t believe anything because there is nothing left to believe."
    s "This is all for me."
    s "This is all for me."
    s "This is all for me."
    s "This is all for me."
    s "This is all for me."
    s "I am the only one who’s real."
    s "The rest of you are just fleshlights."

    play sound "dooropen.mp3"
    scene awesomesexscene3
    with dissolve

    yu "Hey, I finished — woah. "
    yu "Okay. Probably should’ve seen that coming. "
    yu "Listen, uhh...I ain’t tryin’ to interrupt your “alone time” or whatever, but I was thinkin’ you- "
    yu "..."
    yu "Sara, you..."
    yu "You {i}are{/i} awake, right?..."

    "Zoople dorp, doopy dop. Sex so good I wanna pop."

    yu "Yo, ease up on her fuckin’ head, man. You’re gonna hurt her."
    yu "Sara, are you okay? Gonna need you to say somethin’ before I can leave."

    "Gonna do Yuki next. Gonna bang all the moms."
    "Gotta beat the game."

    s "Take that, you stupid MILF."

    stop music
    play sound "static.mp3"
    scene awesomesexscene4 with flash
    stop sound
    play music "sidecharacter.mp3"

    yu "Okay, that’s enough!"
    yu "The fuck you think you’re doing, dickwipe?! She ain’t even conscious!"
    s "Let go! Want more!"
    yu "Get a fucking grip, man! You’re like a full fifty kilos heavier than her!"
    s "Release me!"
    yu "You were gonna fuckin' {i}kill her{/i} at that rate!"
    s "Let...go!"

    scene awesomesexscene5
    with dissolve

    yu "Fucking...Christ! Where’d all this strength come from?! What happened to...being a little bitch?!"
    yu "You want to play...rough, tough guy?! Let’s see how you feel...gettin’ put to sleep!"

    scene awesomesexscene6
    with dissolve

    sar "Ugh..."
    sar "What happened?..."
    sar "Why does my head hurt?..."
    yu "Morning...sunshine! Have a...nice nap?!"

    scene awesomesexscene7
    with dissolve

    sar "Huh?...What are you talking about?..."
    yu "Caught this guy...not knowin’ when to stop! Think he...went at it so hard he...knocked you the fuck out!"

    scene awesomesexscene8
    with dissolve

    sar "Oh my god! Oh my god, oh my god, oh my god!"
    yu "Dude’s...stronger than I thought, but...this is nothin’...I got your back, Sara..."
    sar "Yuki, no! It’s okay! "

    scene awesomesexscene9
    with dissolve

    yu "What?! The fuck you mean, “It’s okay?” You weren’t even awake until ten seconds ago! Dude could’ve fucking killed you!"
    sar "Maybe! But now {i}you’re{/i} going to kill {i}him!{/i} His face is turning blue!"
    yu "He’ll be fine! He’s still awake ain’t he?! Look!"

    play sound "thump.mp3"
    scene awesomesexscene10 with hpunch

    yu "Oh. Maybe not. "
    sar "Ah! Sensei!"
    yu "Uhh...whoops."

    scene awesomesexscene11
    with dissolve

    sar "Yuki, why?!"
    yu "Okay. Maybe I used a little too much force, but he’s a big boy. He’ll be fine in a few minutes. Just gotta let the...oxygen come back or whatever."
    yu "I ain’t really sure how it works, to be honest."
    yu "But hey, maybe that’ll teach him a lesson to not fuck my boss so hard she passes out."
    sar "Ahhh! How am I going to explain this when he wakes up?!"
    yu "I mean...you could start by saying something like, “Yuki knocked you the fuck out for being too rough with me. She’s such a good friend and an even better employee.”"
    yu "Sounds plain and simple to me. But I ain’t really sure how shit normally goes with you two, so..."

    scene awesomesexscene12
    with fade

    sar "Damn it, Yuki! My boyfriend is unconscious on my living room floor because of you! This is not a situation I was prepared to deal with!"
    yu "Uhh...you forgettin’ that it was {i}you{/i} who was unconscious a few seconds ago? How come I’m the one gettin’ yelled at?"

    scene awesomesexscene13
    with dissolve

    sar "Well, who else am I going to yell at?! You’re the only other person in here who’s awake right now!"
    yu "Oh damn. Guess he wasn’t joking. That thing’s massive. Props to you, Sara."

    scene awesomesexscene14
    with dissolve

    sar "Oh my fucking god, I can’t believe this."
    yu "You ain’t actually like, mad at me, are you?"
    sar "No...I’m not mad. You didn’t really have to knock him out though, did you? Wasn’t that going a little too far?"
    yu "Sara, the dude had your head pinned down against the floor and was pounding you so hard that your paintings were about to fall off of the walls."
    sar "Yeah, but I {i}like{/i} it that way."

    scene awesomesexscene15
    with dissolve

    yu "Uh-uh. No way. Likin’ it rough is one thing, but nobody likes it so rough that they pass the fuck out. Ain’t gonna believe that."
    sar "Ugh...he’s never going to want to have sex with me again after this. I know it."

    scene awesomesexscene16
    with dissolve

    yu "Yeaaaah...maybe."
    yu "Might save you some internal bleeding, though. Christ that thing is big."
    sar "Yuki, I’ve got it from here. Why don’t you head home for the night?"

    scene awesomesexscene17
    with dissolve

    yu "You sure you’re gonna be good? Cause I don’t mind sticking around for a little while longer."
    yu "Don’t think he’s the type that’ll get all mad and shit once he wakes up, but you can never really know for sure. Don’t want you stuck in a situation you can’t find a way out of."
    sar "I’ll be fine, but thank you. I’ll make sure he knows you were only looking out for me. I know you two have been starting to grow a little closer lately and I don’t want this to ruin that."

    scene awesomesexscene18
    with dissolve

    yu "We’re just friends...but aight. "
    yu "Call me if you need something else, okay? "

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    yu "I’ll see you tomorrow..."

    "........."
    "......"
    "..."

    scene awesomesexscene19
    with dissolve4

    s "..."
    sar "..."
    s "Sara?..."
    sar "Heeeey..."
    s "What happened?...When did I fall asleep?..."
    sar "Like...half an hour ago?"
    s "I see..."
    s "And where are my pants?"

    scene awesomesexscene20
    with dissolve

    sar "They’re still on the floor..."
    sar "I thought about putting them back on you, but I didn’t want to wake you up and needed a little more time to try and, uhh...think of how to talk my way out of this."
    s "I don’t even remember what happened..."
    sar "Well, you uhh..."

    scene awesomesexscene21
    with dissolve

    sar "You kind of...spontaneously interrupted a really serious conversation to have sex with me. "
    sar "Which is cool. I’m all for random acts of lewdness and stuff. I just...you know, prefer to stay conscious during them."
    s "Conscious? So I-"

    scene awesomesexscene20
    with dissolve

    sar "Choked me until I passed out. Which would be pretty bad if it weren’t for the fact that Yuki showed up and did the same thing to you later. Which is why you’re...just now waking up. And I’m sorry."
    s "I did {i}what?...{/i}"
    sar "You, uhh..."
    sar "You did something else as well..."
    s "What does that mean? What else did I do to you?"
    sar "I...uhh..."
    sar "I don’t know if you just {i}missed{/i} or...something, but..."
    sar "You kind of...fucked my ass. "
    sar "And by “kind of” I mean you {i}really{/i} fucked my ass. You were {i}not{/i} gentle about it."
    s "Sara, I’m sorry. I must have blacked out or-"
    sar "It’s fine. Don’t worry about it."
    s "It’s not fine. That happens sometimes and I can’t really control what’s going on while-"

    scene awesomesexscene22
    with dissolve

    sar "You don’t have to explain it, Sensei. I get it."
    s "What do you mean you {i}get it?{/i} This isn't something you just {i}get.{/i} It's infinitely more complicated than that."
    sar "No, I {i}get it{/i} because the same thing used to happen to me."
    s "It..."
    s "What?..."

    scene awesomesexscene23
    with dissolve

    sar "That’s actually what I was trying to tell you before you snapped."
    sar "That whole thing with the movies...and with Sana “seeing” stuff..."
    sar "It all comes back to the same thing."
    sar "I don’t know exactly when it started or stopped, I just know that there were pieces of my life that never felt like they fit."
    sar "Sometimes, it was a shadow in the corner of the room. Or some weird figure who would come and talk to me in some language I didn’t understand."
    sar "Sometimes, it would be like parts of the day disappeared entirely. And I’d wake up somewhere unfamiliar without any idea of how I got there or what I was doing."
    sar "I’ve been drawn to you since the moment we met and...I thought at first it was just because I have a thing for teachers."
    sar "But I realize now that it might be for another reason entirely."

    scene awesomesexscene24
    with dissolve

    sar "That’s why I let it happen."
    sar "That’s why I’m not mad about you interrupting our talk...or choking me...or fucking my ass with zero lube — which is a thing I absolutely {i}do{/i} own and would have gladly gotten for you..."
    sar "I’m not mad about any of it because I know what it’s like to lose control. And I’m not going to hold something against you that I know can’t be held in the first place."
    s "..."
    sar "Do you think I’m crazy?"
    sar "Do shadows ever talk to {i}you,{/i} Sensei?"
    s "..."
    sar "..."
    s "I don’t think you’re crazy, Sara..."
    s "But I also don’t think there’s an easy way to explain any of that."

    scene awesomesexscene23
    with dissolve

    sar "I’m not looking for an explanation. I wasn’t even looking for someone to relate to tonight. "
    sar "I just wound up getting lucky for the third time in my life by finding out that the man I’ve fallen for {i}this{/i} time won’t flip his lid when he realizes what I am."
    s "What are you?..."

    scene awesomesexscene24
    with dissolve

    sar "Broken."
    sar "We both are."
    sar "There might be a reason for it. There might {i}not{/i} be a reason for it. I don’t know."
    sar "But no one else will ever understand these missing pieces. "
    sar "No one else will ever see that switch flip in a person and just {i}get{/i} it, because that’s something only people who have experienced it firsthand will understand."
    sar "Everyone other than us will just think we’re crazy. Delusional. But it’s so...{i}so{/i} much deeper than that."
    sar "Which is why we need to protect Sana. "
    sar "We can’t let her follow us into the dark."
    s "But how are we supposed to protect her if we can’t even figure out what’s happening with {i}us?{/i} "
    s "The pieces may have stopped disappearing for you, but I’m losing more and more every day.  And I’ve wound up hurting people because of it. "
    s "What if Yuki never showed up tonight? What if she hadn’t stopped me?"
    sar "You think {i}I{/i} have the answer to that? I gave you a whole monologue about Memento because I couldn’t figure out how to properly talk about myself. "
    s "Then what are we supposed to do? And how are you so sure Sana’s right behind us?"
    sar "Because it’s already started and it will only get worse."
    sar "I don’t know if there’s anything we can do to stop it. But if we never let her out of our sight, we can fill in all of the gaps for her."
    s "That’s just not reasonable, Sara. We can’t lock her up like that."

    scene awesomesexscene25
    with dissolve

    sar "I know that...of course I know that..."
    sar "I just don’t know what else to do..."
    sar "When I think of how scared I was back then...and how desperately I ran from all of the shadows that were following me...and I picture {i}Sana{/i} in my place?..."
    sar "How can I live with that?"
    sar "How can I live knowing how terrified and worried my daughter is as the world around her breaks into pieces?"
    s "You think {i}I{/i} have the answer to that? I was just choked out for sodomizing her mom."

    scene awesomesexscene26
    with dissolve

    sar "Heheh...that’ll be a story for the grandkids if you ever decide to marry me."
    s "I think you should reevaluate what stories you want to tell your fictional grandchildren."
    sar "I’m scared, Sensei..."
    sar "I thought this was over..."
    sar "All this time, I thought I was the only one who’d ever have to go through this. It never even occurred to me that Sana could face the same thing."
    s "Same here. Never in a million years did I think that the part of me I’m most confused about would be one shared by {i}you.{/i}"
    sar "Like I said...I got lucky."
    sar "But what should we do now? Where should we go from here?"
    s "I don’t have a clue. But this is your daughter we’re talking about, so you’re going to wind up being the one who has to make a decision. "
    s "I’ll follow you when you do, though. I promise."
    sar "Okay...but if you bail on me like the last guy, I’m going to hunt you down. I hope you know that."
    s "Feel free. It’s not like I have anywhere to go."
    sar "Sensei...can you..."
    sar "Can you...stay here tonight? I don’t really want to be alone and Sana’s with Ayane. "
    s "Sure, Sara."
    sar "And if you decide to fuck my ass again in the middle of the night, can you use lube? I’m in a lot of pain right now."

    scene black
    with dissolve2

    s "Sure, Sara..."
    sar "Thank you. I’ll leave it on the nightstand."

    "A lie, alive, alone. This is someone else’s home."
    "I stitched these words together so they’d form another happy poem."
    "I wish you were there with me — in the darkness where we slept."
    "“But instead you had to leave us,” quoth the creaking of the seventh step."

    $ renpy.end_replay()
    $ saraspecial30p2 = True
    $ sara_love += 10
    stop music fadeout 10.0

    "{i}Sara’s affection has increased by 10!{/i}"
    "{i}You are not as special as you think you are.{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1

    if day == 7:
        $ day = 1
    else:
        $ day += 1

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

    scene street_day
    with dissolve2

    "What do I want to do with my day?"

    jump satmorningmenu

label sarabar30:
    if saraspecial30p2 == True:
        scene movienight1
        with fade
        play music "calmbar.mp3"

        yu "Well, I’ll be damned. If it ain’t Captain Fucksalot."
        s "I’ll take that over Douchebag McDouchefuck. "
        yu "Glad you’re conscious again. But if you think I’m gonna apologize for pullin’ you off of Sara-"
        s "I don’t think that at all. In fact, I’m glad you pulled me off. I...wasn’t really myself that night."

        scene movienight2
        with dissolve

        "I find Yuki alone at the counter after making my way into the bar. And if I focus just on her, I can help myself relive the moments back when this was all a hidden gem."
        "I tune out the chatter behind me and stare straight ahead, hoping that the person I came here to see will creep into my peripheral vision, but it’s all to no avail."
        "I know she isn’t coming. "
        "It’s not some paranormal sensation based on an unworldly connection and the fresh knowledge that we’re both prone to snapping from time to time — it’s just a hunch."
        "A normal, old hunch."
        "And like a plant, I’ll let it die."
        "Because I can go one night without progression when there are others who need it more."

        yu "We cool then? No hard feelings from getting choked out?"
        s "No hard feelings. You’re a good friend."
        yu "To you? Or Sara?"
        s "To both of us. You helped in more ways than you know."

        scene movienight3
        with dissolve

        yu "All I did was bust into the living room and knock you out. Ain’t really what I’d call bein’ helpful."
        s "Well, it was. "
        s "And maybe next time, if all of us are conscious, you can help out in {i}another{/i} way."
        yu "..."
        s "..."

        scene movienight4
        with dissolve

        yu "Or I can just choke you again. "

        scene black
        with dissolve2

        s "Okay...too soon."
        s "I’ll try again another night..."

        "........."
        "......"
        "..."
        "{i}Meanwhile...{/i}"
    else:
        scene hungryboy
        play music "calmbar.mp3"

        "help"

        scene black

        "....."

    scene movienight5
    with dissolve2

    h "Welp, now that that’s over, Tom Hardy or Leonardo DiCaprio? You have to pick one."
    sar "Leo 100%%. It’s ridiculous that you even have to ask."

    scene movienight6
    with dissolve

    h "I don’t know. I feel like I might have to go with Tom on this. I like the whole tough guy thing, and he makes the beard work way better than Leo does."
    h "Plus, watching Leo crawl out of a bear is going to stay with me forever and I don’t want that memory popping back up in bed."
    h "Also, I wouldn’t have to worry about Tom Hardy just staring into the mirror during sex and that would totally be a Leo thing."
    sar "I’d stare into the mirror too if my name was Leonardo DiCaprio. "
    h "I think we’re a little too old for him now anyway."
    sar "Maybe you, but I’ll be 18 forever."
    sa "I...didn’t like either of them..."

    scene movienight7
    with dissolve

    sar "You didn’t like Leo?! I was in love with him when I was your age!"
    h "You were also pregnant when you were her age, so I think we should let Sana make her own decisions here instead of just following in your footsteps."
    sar "What didn’t you like?! Was it the beard? Because Haruka’s right, he looks better without the beard."
    sa "He’s...old. They’re both old..."
    sar "Sana, I love you. But you are hurting me right now."
    h "What even {i}is{/i} your type, Sana? I don’t think I’ve ever even heard you talk about boys before."

    scene movienight8
    with dissolve

    sar "Brendan Fraser? Brad Pitt? Johnny Depp? Keanu? Kevin Spacey?"
    h "You might have more luck if you shy away from the 90’s heartthrobs and-"

    scene movienight9
    with dissolve

    h "{i}Kevin Spacey?{/i} Really?"
    sar "There’s just something about him, you know?"
    h "Not...really?"
    sa "Um...I...I don’t really know..."

    scene movienight10
    with dissolve

    sa "I haven’t really...thought much about it, but...umm..."
    sa "Maybe..."
    sa "Pedro...Pascal?..."
    sar "..."
    h "..."

    scene movienight11
    with dissolve

    saraharuka "Yeah..."

    scene movienight12
    with dissolve

    h "Wait, isn’t he the same age as Leo though?"
    h "I could have sworn I read a thing about late 40’s actors the other day and I’m, like...{i}pretty{/i} sure they’re both 48."
    sar "There is no way Pedro Pascal is 48. But there’s also no way Leo is 48, so whatever you read is wrong."
    sa "Like I said, I...haven’t really thought about it...I just...think he’s kind of...cool..."

    scene movienight13
    with dissolve

    h "Should we watch something with him in it next? I still haven’t seen that movie with him and Nicolas Cage."
    sar "What’s that about? "
    h "It’s a movie about Nicolas Cage where Nicolas Cage plays Nicolas Cage. Also, Pedro Pascal is there."
    sar "That is the single most Nicolas Cage movie I have ever heard of."
    sa "I can...stay for one more, but...I have to call Ayane first..."
    sa "I forgot to tell her I...didn’t have work tonight, so...she’ll probably be...wondering where I am..."

    scene movienight14
    with dissolve

    sar "Okay, but make sure you tell her I love her and that I want her to come by the bar more often."
    sa "I’m..."
    sa "Not going to...tell her that..."

    scene movienight15
    with dissolve

    sar "Ask her how she feels about Leo! Ayane will have my back! She’ll understand!"
    sa "Ayane...only has eyes for...Sensei, so..."

    play sound "dooropen.mp3"

    sar "Leo doesn’t count! He’s an exception to every rule!"

    scene movienight16
    with dissolve

    sar "Hah...betrayed by my own daughter..."
    h "You want another drink? I’m making one last run to the fridge now since it would be extremely disrespectful to Nicolas Cage if any of us get off the couch during one of his movies."
    sar "I’m fine. Thanks, though."
    h "You sure? You might need it. This {i}is{/i} a Nicolas Cage movie after all."

    scene black
    with dissolve2

    sar "I’m okay, Haru-chan. "
    h "Okaaaaay. But don’t say I didn’t warn you."

    "........."
    "......"
    "..."

    scene movienight17
    with dissolve2

    h "So...what’s going on? You never throw together movie night unless you’re feeling down. "
    sar "Oh? Since when do {i}you{/i} pay attention to anyone other than yourself?"
    h "Since Masahiro died."

    scene movienight18
    with dissolve

    sar "Ugh...poor Maki. I can’t believe all they’d give her is a fucking phone call."
    h "Yeah...But ever since then, I’ve been trying to be a better friend. Things don’t always have to be about me anymore."

    scene movienight19
    with dissolve

    h "Because in the grand scheme of things, and this isn’t me bragging or boasting, I don’t have it all that bad."
    h "You two are the ones struggling, so I’m gonna do what I can to be there for you."

    scene movienight20
    with dissolve

    sar "Thank you, Haru-chan...but just because your problems aren’t the heaviest around doesn’t make them any less real."
    sar "I know how lonely you are. So I’ll always be here if you need me as well."
    h "Thanks, Sara. So...are we gonna talk about it? Or is this more of an “Ignore it and keep our minds off of stuff night?”"

    scene movienight21
    with dissolve

    sar "You know me...which means you know what I’ll pick."
    h "“Ignore it and keep our minds off of stuff night” it is. Thankfully, we have the world’s most unhinged and weirdly talented actor to help us out with that."
    sar "So...what are you going to do when he gets back to Kumon-mi?"

    scene movienight22
    with dissolve

    h "Nic Cage is coming to Kumon-mi?! Why?! {i}How?{/i}"
    sar "I’m talking about your husband, Haru-chan...If you want to help me keep my mind off of stuff, let me share what bits of happiness {i}you{/i} have."

    scene movienight23
    with dissolve

    h "Well, I know we won’t be going to see Nicolas Cage."
    sar "Haru-chan..."
    h "I don’t know, Sara."
    h "It’s been so long at this point that I can barely even remember what he looks like."
    sar "Oh, come on. We both know that’s not true. Plus, I asked about it, so you can say whatever you want and it won’t come across as braggy."
    h "I’m being serious, though. Like, yeah, I have pictures and everything. And tons and tons of memories."
    h "But it’s been years. What if he looks different? I know {i}I’ve{/i} put on some weight since he left."
    sar "Yeah but you’re lucky because all of your extra calories go right into your boobs and mine just make my thighs jiggle."

    scene movienight24
    with dissolve

    h "It’s just kind of weird being away from someone for so long and then having them waltz back into your life one day."
    h "Like, things keep moving while they’re not here. I didn’t hit the pause button on life. I’ve actually done things while he’s been gone. And I’m sure it’s no different for him."
    h "But, like...what would {i}you{/i} do if Sana’s dad just suddenly came back into the picture after all this time away? It would be weird, right?"

    scene movienight25
    with dissolve

    sar "Of course. But that’s way different, Haru-chan."
    sar "He walked out on me intentionally...and it’s been over a decade since then."
    sar "For all I know, the guy went and started another family after that. There’s no way it {i}wouldn’t{/i} be weird for him to just suddenly reappear."
    h "You really have no idea where he went?"

    scene movienight26
    with dissolve

    sar "You think I would have just sat around and done nothing if I {i}did{/i} know where he was? No way. I would have been on that dude for child support even harder than Leo was on that bear earlier."
    h "Sorry, stupid question...The whole situation is just so bizarre to me."
    sar "That’s because you have a husband who actually loves you and not some douchebag who just pretends to."

    scene movienight27
    with dissolve

    sar "I’m not as smart as you, Haruka. Doesn’t matter if it’s now or all the way back then, there are just stupid things I’ve done that you never would have."
    sar "Maybe if you grew up in my shoes you wouldn’t have wound up as perfect and beautiful as you are today, but even saying that is probably just me trying to make myself feel better."
    sar "It’s all so obvious in hindsight."
    sar "The “not wanting to ever bring me around other people” thing I can understand since I was still in high school and he was a grown man-"
    sar "But the constant disappearances...the way he’d stare off into the distance any time I’d try to bring up the future...the look on his face the first time I told him I was-"

    scene movienight28
    with dissolve

    sar "The...first time I...told him I was..."
    sar "I...was..."

    scene movienight29
    with dissolve

    sar "I..."
    sar "I..."
    h "..."

    scene movienight30
    with dissolve

    sar "Can you braid my hair?"
    h "Sara..."
    h "Of course..."
    h "Come here."

    scene movienight31
    with dissolve

    sar "Thank you, Haru-chan. I’m sorry for ruining everything again."
    h "You have nothing to apologize for. I was actually hoping you’d ask."

    scene movienight32
    with dissolve

    h "Plus, Nicolas Cage gets to see you with braids now. And...remind me, how many men have gotten to see that version of you again?"
    sar "Haru-chan, I have made more bad decisions in my life than I am able to count. But even I know better than to let a man see me with braids."

    scene movienight33
    with dissolve

    h "Good...Then I can keep this part of you all to myself."
    h "Besides, we both know I’d treat you better than any man ever could in the first place."
    sar "You would. You and me should just get married."
    h "Not legal in Japan, sweetie."
    sar "I wish the world would accept our love."

    scene movienight34
    with dissolve

    h "Man, I wonder when the last time I did this was? I hope I remember how."
    h "Your hair’s just as soft as always. Are you still using that shampoo from-"
    sar "I miss my son."

    scene movienight35
    with dissolve2

    h "..."
    sar "Can I..."
    sar "Talk about him for a little while?..."
    h "Sara..."

    play sound "dooropen.mp3"

    sa "S...Sorry...There was...something weird on..."
    sa "...Mom?"

    scene movienight36
    with dissolve

    sar "Hey, baby..."
    sa "What...What happened?..."
    sar "Nothing, baby..."
    sa "But...you're..."
    sar "Do you want to help braid my hair?..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve2

    "When I make it back to my room, I think about her one more time."
    "It isn’t for long, and it isn’t particularly groundbreaking-"
    "But the thought goes something like this:"
    "I hope she’s with her daughter."

    scene black
    with dissolve2
    $ renpy.pause(1, hard=True)
    scene waynesworld
    with dissolve3
    $ renpy.pause(2, hard=True)
    scene black
    with dissolve2
    $ renpy.pause(1, hard=True)
    scene waynesworld2
    with dissolve3
    $ renpy.pause(4, hard=True)
    scene black
    with dissolve4

    $ renpy.end_replay()
    $ sarabar30 = True
    $ sara_love += 1
    stop music fadeout 8.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "{i}She still exists when you’re not near her.{/i}"
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

label saracamp1:
    play sound "static.mp3"
    scene campingtime1 with flash
    stop sound
    play music "firstsecondmall.mp3"

    "{b}good things come to those who wait! ~ companycorp is now announcing our latest project: an eighth of a location just outside of the gel kiosk in aisle nine west{/b}"
    "{b}refill your kidneys at your own leisure with our brand new insertion technique ~ thread, what makes the family more familiar{/b}"
    "{b}later this spring, a new presentation will take place beneath the main floor ~ the hole that swallowed everything and the impact it may have on your dating life{/b}"
    "{b}are you feeling sad? try our brand new tongue depressor ~ made with real tongue! only at grayson’s. shop gray, shop grayson’s{/b}"
    "{b}looking for the exit? too bad! all exits have been blocked off for the immediate future. for more information, please visit our website ~ where VIP accounts are as free as you are.{/b}"
    "{b}our next prayer circle begins in fifteen minutes! attendance is not mandatory, but encouraged.{/b}"
    "{b}remember to smile, daughter of the black page ~ the oyster is your world!{/b}"

    scene black
    stop music
    $ renpy.pause(5, hard=True)

    "{b}one more lock removed/where feelers dare to fly{/b}"

    play sound "static.mp3"
    scene sky with flash
    stop sound
    play music "unmatchingeyes.mp3"

    $ totaldays += 1
    $ day = 7
    show sunday onlayer date
    hide saturday onlayer date

    "I had a weird dream last night."
    "I know that’s not really an uncommon thing to say at this point considering that I’ve even begun showing some of them to you, but this one was particularly strange even by my standards."
    "I possessed the body of a woman — not in the sense that I kept her chained up in a secret room of my house, but in the sense that I was quite literally inside of her body."
    "But it wasn’t like it was just my penis that was inside of her body. It was all of me. But not in a vore kind of way. Like, basically, I was just a woman."
    "I wandered through the halls of an abandoned mall and came across a 500 yen coin that no vending machine would ever accept no matter how many times I tried to dump my findings into them."
    "Eventually, there was a small man who offered to take the coin off my hands so long as I accepted his mystery box."
    "I took him up on the deal. And when I opened the box, there was a small child inside — wrapped in foil like a hot sweet potato, but one I could not legally take a bite of without incurring the wrath of the government."
    "I took him home and fed him. I gave him a pile of dirt to play in and made sure to change the bulbs of his heat lamp every time it would start to dim."
    "Eventually, he grew into me and tried to give me (female version) a hug. So of course, I accepted."
    "But when our skin made contact, I woke up in bed with a particularly grumpy yet despondent redhead staring down at me."

    play sound "static.mp3"
    scene campingtime2 with flash
    stop sound

    "And that’s basically how I wound up here. "

    a "..."
    s "You don’t seem very excited to be going camping anymore, Ami."
    a "Probably because you failed to mention the part about how we’d be going along with a bunch of older women."
    s "Does that really change anything? Besides, you wouldn’t have agreed to come if I’d told you."
    a "So you just tricked me instead?"
    s "That’s right. And I regret nothing as this will ultimately bring us closer together."
    s "Besides, there’s no way you didn’t realize last night that someone else was involved in this. "
    a "Obviously. "

    scene campingtime3
    with fade

    a "But I sure didn’t expect it to be three of them and that we’d all be going together."
    sar "My friend Yuki is coming too. But we didn’t have room in the car, so she’s just going to meet us there."
    h "You know you can drive a little faster, right Maki?"
    maki "No can do, Haru-kun. I’ve got precious cargo along for the ride this time."

    scene campingtime4
    with dissolve

    h "Kun?"
    maki "That’s right. Because the boys are back in town and you’ll never guess what they do. They camp. "
    h "What?"
    maki "That’s us. We’re the boys."
    h "I’m confused."
    sar "So! Ami, have you ever gone camping before?"

    scene campingtime5
    with fade

    a "No."
    sar "Then, are you excited to try it out for the first time?"
    a "I’m only doing this because Sensei said it would be good for our relationship and my entire life revolves around making him happy."

    scene campingtime6
    with dissolve

    s "Ami, be more polite to Sara. She’s never done anything to get on your bad side before."
    sar "It’s fine, Sensei. I kind of get where she’s coming from. "
    sar "I used to drag Sana around to go shopping when she was little and that was never really {i}her{/i} thing. So if Ami’s only here to please you, that’s fine by me. We’ll all end up at the same place either way."
    a "I don’t have anything against Sana’s mom. She’s really nice and really pretty. I just also want her to leave us alone for the entire trip so you and me can properly bond."

    scene campingtime7
    with dissolve

    sar "The {i}whole{/i} trip? But I was looking forward to bonding with you as well!"

    "Before I went to sleep last night, I wound up giving Sara a call and explaining the situation to her."
    "And, since she (and everyone else) has been dying to help me so much lately, she wasted no time at all in accepting the role as Ami’s surrogate mother for the duration of the trip."
    "Which isn’t to say I expect her to adequately {i}fill{/i} that role — especially when there’s one other girl vying for the same position and it’s one Ami seems to like significantly more, but still."
    "Sara’s already raised children. And, for reasons I will never understand, she seems to love it. So...maybe I’ll get lucky and Ami won’t entirely hate it and I can kind of...pick up a few tricks from her or something."

    a "You already have a daughter. I don’t want to take Sana’s place. "

    scene campingtime8
    with dissolve

    "Or maybe she’ll keep deflecting every opportunity Sara takes to try and shorten the gap between them."

    sar "Just because you aren’t my daughter doesn’t mean we can’t bond! We got along well when I came over to your house that one time, didn’t we?"
    maki "Wait, really? Ami always tries to kick me out when I go to Sensei’s house."

    scene campingtime9
    with dissolve

    a "I wouldn’t have to if you didn’t keep smuggling suitcases full of weird stuff into my living room."
    sar "Wait, Maki — how often are you going over to Sensei’s place?"
    h "Often enough for this to be a recurring problem, apparently."
    maki "Hey, I’m just trying to bump up my sales numbers. You two should be commending me as fellow business owners."

    scene campingtime10
    with dissolve

    sar "Ami, I would like to apologize on behalf of Maki for any strange objects she may have snuck into your house. And I can assure you that I do not have any strange objects in my possession whatsoever."
    maki "Well, you’re in luck! Because my trunk is full of-"
    sar "I would also like to apologize...on behalf of Maki in general."
    a "It’s fine. I like you. I’m just not in a great mood."

    scene campingtime11
    with dissolve

    sar "Is it because you were looking forward to spending some alone time with your uncle?"
    a "Yes. And it doesn’t really help that I look like a demon either."
    s "She’s going through a phase. She’ll break out of it soon, hopefully. "

    scene campingtime12
    with dissolve

    sar "Well, how about this? I just so happen to always travel with a full bag worth of haircare and fashion products, so how about I...fix you up a little bit? Does that sound fun?"
    s "Ami doesn’t need {i}fixing,{/i} Sara. Well...not like that at-"
    a "Sure."

    scene campingtime13
    with dissolve

    s "Wait, really?"
    sar "Yeah, really?!"
    a "Is that really such a surprise? Do you think I {i}like{/i} looking like this? I hate it. And being self-conscious about that is one more reason I’m in such a bad mood right now."
    a "But yes, the other reason is that I wanted to be alone with Sensei. And now I can’t. So that’s just great."

    scene campingtime14
    with fade

    h "On the bright side, you two will be able to share a tent at least. We were able to find an extra one in Sara’s storage room."
    maki "Haru-kun’s right! The rest of us girls will share a different tent so the two of you can be alone for a little while. Your uncle already informed us of how important that would be."

    "I did no such thing. But I’m glad to see that Maki’s going out of her way to lie for me. "

    scene campingtime15
    with dissolve

    h "Can you please stop calling me Haru-kun?"
    maki "Unfortunately, I can not. I’m sorry."
    sar "And, I’ll tell you what — if at any point you find me overbearing or annoying, all you have to do is say the word and I’ll leave you alone."
    a "What word?"
    sar "Haru-kun."

    scene campingtime16
    with dissolve

    h "Oh, come on!"

    scene campingtime17
    with fade

    a "I’m not asking to be left alone. This is just...a lot at once after not really talking to anybody for weeks. "
    sar "It is, isn’t it? But you know what, Ami? I think you’re really brave. And I’m not just saying that because you were able to leave the house looking like that. "

    scene campingtime18
    with dissolve

    sar "I’m saying it because I know what it’s like to feel like a failure. And how you can’t help but blame all of the terrible things happening in the world on some stupid decisions you’ve made."
    sar "Maki feels that way too sometimes, I’m sure. But maybe not Haru-kun since she hasn’t had to experience anything traumatic just yet."
    maki "Knock on wood."
    h "I’m just not going to get myself involved in this since I can’t imagine anything I have to say doing me any favors."
    a "How much do you know?..."

    scene campingtime19
    with dissolve

    sar "..."

    "She knows everything."
    "Well...maybe not {i}everything.{/i}"
    "I made sure to leave out the part about how all of this anguish ultimately stems from the fact that I fucked the wrong high-schooler. But she knows about what’s going on with Ami at least."
    "Truth is, I didn’t want Sara saying the wrong thing since I know she always goes overboard when it comes to parenting. So I told her about the scissors."
    "I told her about the mental breakdowns and the organ-harvesting rant in the classroom."
    "I even told her about how Ami’s feelings for me are a bit more than just a niece’s love for her uncle."

    if amifingered == True:
        "But again, I conveniently left out the part about how I’ve reciprocated those feelings on {i}many{/i} occasions and have had to wash her dried fluids off my cock more times than I can even count."

    "The thing is, I trust Sara."

    if sarasex == True:
        "She’s the only one who really {i}gets{/i} what I’m going through concerning all of the...blackouts and whatnot."


    "And I don’t expect her {i}to{/i} say the wrong thing because, even if she isn’t the {i}best{/i} mom out there, she’s empathetic. And compassionate. "

    sar "It doesn’t matter what I know. What matters is what I don’t."

    scene campingtime20
    with dissolve

    "And...kind of amazing."
    "The way she can smile like that after losing a son is something I can only hope to emulate. And all that {i}I’ve{/i} lost has had different colored blood than me."
    "So yeah...the point of this trip {i}is{/i} to paint myself in one of those colors and hopefully emerge looking slightly more like a father figure."
    "But it might be good for me as well — to walk in the shadow of someone who can find the shade and make all of this look whole again."

    sar "Let’s try and have some fun today, okay? "
    sar "Even if it’s only for twenty-four hours, let’s pretend like we’ve left Kumon-mi altogether and picture ourselves in a happier place where we can start all over."
    sar "No worries...no drama...just grass. And bugs. And marshmallows. And anything else that Maki has packed into her trunk that won’t make us all look like insatiable nymphomaniacs."
    a "I’ll try, but...why are you so concerned about how I feel when you barely even know me?...I don’t get it."
    sar "I know more about you than you think, Ami. It’s not like Sensei never talks about you."

    scene campingtime21
    with dissolve

    a "Does he?..."
    sar "Plus, moms don’t need a reason to be concerned about things like that."
    sar "Even if you’re not Sana, I still feel the need to protect you and nurture you. So that’s what I’m going to do until you ask me to stop. And even then, I’ll never stop {i}feeling{/i} this way."
    sar "It just comes with the territory, I guess. And it’s territory I’m sure your uncle’s familiar with if he was worried enough to venture this far out of his comfort zone just to try and make you happy."

    scene campingtime22
    with dissolve

    a "..."
    a "Yeah."
    a "He’s pretty amazing, isn’t he?..."
    s "Not really."
    sar "He really is."
    a "There’s a part of what you said that needs to be fixed, though. "

    scene campingtime23
    with dissolve

    sar "There is?"
    a "Yeah."

    scene sky
    with dissolve2

    a "He doesn’t want to be my “uncle” anymore."
    s "..."
    sar "And how does that make {i}you{/i} feel?"
    a "..."
    s "You don’t have to answer, Ami."
    a "I’ll answer."
    a "Just..."

    scene black
    with dissolve2

    a "I’d like to do it in private."

    "I’m not sure how long we remain in the car before Maki quite literally ventures off the beaten path down a long dirt road that will either take us to our destination or send us speeding off a nearby cliff."
    "And if the latter happens, fine. That would actually be a pretty poetic death considering the scenario and the conversations we had leading up to it."
    "But I’m looking for a different sort of fresh start."
    "One that will allow me to continue being the sad sack of shit I am, but with a slightly less sad sack of shit looming over me at all times. "
    "Watching my every move. "
    "Always thinking about me."
    "Less like a niece-"
    "And more like a daughter."

    $ renpy.end_replay()
    $ saracamp1 = True
    $ ami_love += 1
    $ sara_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    jump yukicamp1

label saracamp2:
    scene black
    with dissolve2

    "I think I’ve done enough for today."
    "In fact, this is probably the most I’ve done at {i}all{/i} since I was in the shape and state required to attend similar events hosted by my class."
    "I wonder how those work without me. "
    "But that shouldn’t come as much of a surprise as my narcissism seldom allows me to comprehend how {i}anything{/i} works without me."
    "Even acknowledging that, though, I can’t help but feel like there’s something missing despite everything I’ve accomplished during my brief time here. "
    "It was just one day, but it felt like two. So is this sudden and apparent emptiness the result of me wanting to stretch that two into a three? Maybe a three into a four?"

    play sound "zipper.mp3"

    "I shrug my shoulders as I unzip the mouth of my shelter and allow it to swallow me."
    "Everyone else has hurried off to sleep already and I look on in awe as my niece is digested before my very eyes."
    "I don’t call her my daughter internally because it still hasn’t set in yet."
    "All I know is that she’s cute. And so I watch her sleep for approximately seven minutes before opening up a second mouth inside of the mouth and crawling into that one."
    "I think I like camping."
    "I think I like being out here where the only people I can hurt are people who have already {i}been{/i} hurt before."
    "It alleviates some of the pressure of simply existing and grants me the strength I need to not be chewed in half by my sleeping bag."
    "When I close my eyes, I think of Heaven."
    "I think of how it must appear. Or if it ever will appear. Because I {i}want{/i} it to appear."
    "But I also worry that days like this are the closest I’ll ever come to experiencing such a thing."
    "My final thought before falling asleep is that I want to do this again."
    "I just want to do it alone next time."
    "I want to be one with the forest."
    "I want it to swallow me."
    "Goodnight, Moon."

    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 1
    hide sunday onlayer date
    show monday onlayer date

    scene sky
    with dissolve2
    play music "acoustic.mp3"

    maki "Is it faster if I take this left?"
    a "That road’s closed for construction. But you can follow this one straight for three more lights and then turn left at that one."
    sar "Weird. I don’t remember seeing any construction at all on our way to pick you guys up."
    h "You were probably just so excited to spend time with your newest daughter that you overlooked it."
    maki "What are they even building over here? It’s not another porn shop is it? Am I going to have to fight another small business owner to defend my turf? You’ll help- won’t you, Haru-kun?"
    h "Sure, Maki. I’ll fight a rival porn dealer for you."
    sar "I’ll help too! I can be scrappy."
    maki "No, you’re too small. You’ll only get in the way."
    s "I hadn’t noticed any of this either. Do you know what’s going on, Ami?"
    a "Mm...just more houses, I think? Maybe a closer convenience store if we’re lucky."
    sar "That sure sounds like it’d be convenient to me."
    h "Maki, drive faster."
    s "Maki, don’t."
    h "But if we don’t get there soon, Sara might try to make another joke."
    maki "Was that a joke? I thought it was more of an observation than anything."
    sar "It was obviously a joke! It’s not my fault that none of you appreciate good humor. Right, Ami?"
    a "Hm? What was the joke? I must have missed it."
    sar "Ugh! Never mind! Maki, drive faster!"

    "It’s the morning after, if you couldn’t already tell."
    "Our trip has come to an end and the time has come for us to bid farewell to camaraderie and get back to our old, boring lives."
    "I’m starting to think mine might be a little less boring from now on, though. But there’s still one problem-"
    "I don’t know what to do about Niki."
    "I’ve obviously had several chances to talk to Ami about her proposition but, I...may have prioritized something else. "
    "Something with a more immediate impact on the way I’m thinking as opposed to something that would have to take place in the future."
    "I’m pretty sure that’s okay, though. And I’m pretty sure Niki would be proud of me for taking the step I took last night."
    "I know Ami’s proud of me, that’s for sure. But I also know that she’d be proud of me if I decided I was a cat one day and started dropping dead mice at her feet. "
    "Suffice it to say, her pride comes easy. Niki’s comes at a cost."
    "And mine is a giant invisible force-field covering every inch of my body in a way that makes me forget it’s even there."

    scene black
    with dissolve2

    "When we pull up to the house, Sara gets out of the car as well and follows Ami and me to the door."
    "Originally, I think it’s just to give her the chance to say goodbye and...hug us or whatever. But I quickly realize that’s not the case when Maki speeds off."
    "She smiles at me, silently asking to be invited in. So I silently respond by opening the door as a low-effort way to repay her for opening one yesterday."

    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene saraamishouse1
    with dissolve2

    sar "Did you have fun yesterday, Ami?"
    a "Yeah...and thanks again for making me...not so hideous anymore."
    sar "Thank me again once you can get rid of those dark circles. Or just come visit me so I can see the finished product."
    s "Maybe don’t invite my niece out to the bar, Sara."

    scene saraamishouse2
    with dissolve

    sar "You’re still calling her that after yesterday? Did we fail our mission after all?"
    s "Oh. Shit."
    a "It’s fine. I imagine it’ll take some getting used to. Besides, it’s not like you’re technically {i}wrong.{/i} And I don’t really care {i}what{/i} you call me. "
    a "We can...take it slow or..."

    scene saraamishouse3
    with dissolve

    a "Yeah..."
    sar "Are you doing anything later tonight, Ami? Maybe you, me, and Sana could go out to dinner or something? That wouldn’t be too weird, would it?"

    scene saraamishouse4
    with dissolve

    a "Maybe another time. I already told one of my friends I’d meet up with them and...probably shouldn’t immediately back out."
    s "Wait, you did? Are you sure you’re ready for that? It’s not too soon? You don’t want to...stay inside for a few more days?"

    scene saraamishouse5
    with dissolve

    a "Weren’t you literally {i}just{/i} trying to get me to start leaving the house again yesterday? I’m a burden to you if I stay here and we both know that."
    s "But that still doesn’t mean I expect you to start acting normal again after one outing and-"
    a "It’s fine. It’s just Maya I’m meeting up with anyway. "

    play sound "static.mp3"
    scene nodokontest6 with flash
    scene saraamishouse5 with flash
    stop sound

    s "Ah."

    scene saraamishouse6
    with dissolve

    sar "Then maybe {i}me and you{/i} could go out to dinner?"
    a "Sara, I like you. And I want to thank you again for yesterday. But please — don’t push it."

    scene saraamishouse7
    with dissolve

    sar "Hey, you were my first pick! Sensei’s just the backup! You know where my heart really lies!"

    scene saraamishouse8
    with dissolve

    a "That’s only because the quickest way to a man’s heart is through his daughter. And if you win me over, you think you’ll win him as well. Don’t think I don’t know your games, Sara."
    sar "Can I not want {i}both{/i} of those things? Why does it have to be one or the other?"
    s "Just give it a rest, Sara. Ami’s not letting you out of this one."
    a "Right you are, Dad. "

    scene saraamishouse9
    with dissolve

    a "You can have him for a few minutes, though. I’m gonna go warm the bath up."
    a "Camping is fun and all, but I think I would have preferred a hot spring instead."
    sar "Hahah...I’ll try to remember that for next time..."

    scene saraamishouse10
    with dissolve

    "Ami exhibits an extreme amount of growth by leaving me in the room with a woman my age. Either that or she’s cynically and slyly expressing her doubt that I’m sexually interested in older women to begin with. "
    "Either way, the two of us are left alone as she runs into her room to grab a change of clothes for the bath. But I guess she’s never been that {i}opposed{/i} to Sara in the first place."
    "And while I want to sit here and ponder {i}why{/i} that seems to be the case, I’m worried that doing so will lead me down a road I don’t want to think of at all."
    "So I match the tone set by a local bartender and {i}also{/i} stand here in silence, waiting for that quiet to be killed off and replaced with something brighter."

    sar "Uhh..."
    s "..."
    sar "Welp...I need to head out. "
    s "You do? I figured you’d be sticking around for a little while longer considering how you followed us in here."

    scene saraamishouse11
    with dissolve

    sar "I really just wanted to say goodbye to Ami. But this is your first day as father and daughter and I probably shouldn’t be getting in the way of that."
    s "It might be the first day in name, but Ami pointed out yesterday that that’s sort of how things have been all along. "
    s "But hey, maybe now I’ll start making better decisions when it comes to her {i}guidance.{/i}"
    s "I probably won’t, but it’s worth a shot."

    scene saraamishouse12
    with dissolve

    sar "I know exactly what you mean. I made a ton of mistakes with Sana when she was growing up that I didn’t realize until way later. Heck, even now I’m making mistakes."
    sar "But we’re only human, Sensei. Being perfect is so far out of the question that all we can {i}really{/i} do is hope those mistakes don’t pile up to the point where our girls can’t figure out how to get over them."
    sar "That’s why I wanted to help with Ami. I know what that fear is like."

    scene saraamishouse13
    with dissolve

    sar "But I guess she’s also right about the “wanting to win you over” part. "

    if sarasex == False:
        s "Sara-"

        scene saraamishouse14
        with dissolve

        sar "I know, I know. Your heart lies elsewhere."
        sar "I just wanted to remind you of the life you’re missing out on. That’s all."

        scene saraamishouse15
        with dissolve

        sar "But I’ll be going now."
        sar "I had fun yesterday, Sensei. Even if I was just living in a fantasy for part of it."
        sar "I hope you did too."

        scene black
        with dissolve2

        sar "And good luck with Ami. Feel free to let me know if you need anything."
        s "I will. Thanks, Sara."
        sar "And come visit sometime! We miss your face. And your money."
        s "I will. I’ll talk to you later."

        play sound "dooropen.mp3"

        sar "Bye! See you soon!"

        "Sara exits the house and I-"
        "Well, I guess my new-ish life begins."

        scene bedroom_day
        with dissolve2

        "There’s no way of knowing if this change in my relationship with Ami will {i}actually{/i} affect anything, but...I’m going to have to find out eventually."

    else:
        s "I figured as much. But some might say you’ve already won."

        scene saraamishouse15
        with dissolve

        sar "And some might say I haven’t. It really comes down to what {i}you’ll{/i} do next, Sensei. I’ve done more than enough to prove I’d make an excellent rock for your garden. "
        s "Probably not the best analogy, Sara. Most gardens have more than one rock in them."
        sar "As long as I’m the biggest and the one you look at first, I’m happy. "
        sar "Maybe a boulder would be better then. Something you wouldn’t be able to move."

        scene saraamishouse14
        with dissolve

        sar "But I digress. And now I really {i}have{/i} overstayed my welcome."

        scene black
        with dissolve2

        "Sara gives me a quick hug before retreating to the door."
        "But when she grabs the handle, I feel the urge to call out to her."

        scene saraamishouse16
        with dissolve

        s "You haven’t overstayed your welcome, Sara."
        s "You can come here whenever you want."
        sar "..."
        s "I mean it. "
        s "You’ve been a huge help. And it’s nice having someone on hand who at least {i}sort of{/i} knows what they’re doing when it comes to raising a teenager."
        s "So yeah, drop by whenever. "
        s "We’d both be happy to see you. "
        sar "..."
        s "..."
        s "Is something wrong. Why are you just-"

        scene black
        with dissolve2

        sar "That’s not something you should have said to me."
        s "But...why not?"
        s "I don’t get it."
        sar "Sensei...if you let me come here whenever I want..."

        scene saraamishouse17
        with dissolve2

        sar "I’d never leave!"
        s "Sara?..."

        scene saraamishouse18
        with dissolve2

        sar "At least not without you two."
        s "You..."
        s "You’re...not saying you want to {i}move in,{/i} are you? "

        scene saraamishouse19
        with dissolve2

        sar "Here? I guess we could make it work if we tried hard enough."
        sar "It might be a little small for four people, but...I don’t need a lot of space. And I’m sure Sana and Ami wouldn’t mind sharing a room for a few years. But if that’s not possible..."

        scene saraamishouse17
        with dissolve2

        sar "What about the future?"
        s "..."
        sar "..."
        s "What {i}about{/i} the future, Sara?"

        scene saraamishouse20
        with dissolve

        sar "I’ve been thinking about leaving this place. "
        sar "And when I do, I want you to come with me. Ami too, of course."
        sar "Somewhere the four of us can be a family. Somewhere on the other side of the wall."
        s "But...we have no way of knowing when that wall will be gone."
        sar "But wouldn’t it be nice to have something to look forward to when it does?"

        scene saraamishouse17
        with dissolve2

        sar "Maybe somewhere in the countryside so we could go camping a little more often! Doesn’t that sound great?"
        s "I mean...yeah. But-"
        a "A family?..."

        scene saraamishouse21
        with fade

        s "Ami?...How long have you-"
        a "You want the four of us...to be a family?"
        sar "Or more! I’m still young. I wouldn’t mind having another. "
        a "With who?"

        scene saraamishouse22
        with dissolve

        s "Seriously?"
        sar "Okay, I guess that’ll just be a topic for another day! But apart from another child, how does that sound to you, Ami? "
        sar "Are you okay with leaving Kumon-mi behind? Or would you rather stay here? Because the more I think about it, the more I want to get away. "
        sar "And I don’t think there’s anything that would make me happier than taking you two with me. "
        a "I..."
        a "Um..."

        scene saraamishouse23
        with dissolve

        a "Well...what do {i}you{/i} have to say about this?"
        s "..."
        sar "This is all just hypothetical for now, guys. We obviously can’t go anywhere yet."
        sar "And I don’t want it to sound like I’m trying to force myself into your family or...take the place of anyone, but..."
        sar "It’s just something to think about. "
        sar "I think the four of us could have a nice life together."
        s "..."
        a "Dad?"

        scene black
        with dissolve2

        s "I think we need to have another talk soon, Ami."

        "Sara exits the house and I-"
        "I guess I have one more thing to add to the conversation about Niki that I’ve been fearfully avoiding."
        "But despite how the weight of these two options presses so heavily against my chest that I can feel the ghost of an old worm, there is one positive to come from them."
        "It’s the idea that there are people who will love my niece even if I’m gone."
        "Sorry."
        "Daughter."

        scene bedroom_day
        with dissolve2

        "But apart from that...I guess it’s time to try and force a little more normalcy back into my life as well."

    "Even if it’s just one step at a time."

    stop music fadeout 10.0
    $ renpy.end_replay()
    $ saracamp2 = True
    $ sara_love += 1

    if harukasex == False:
        $ harukaspring1miss = True

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "{i}Congratulations! Your “JOY” meter has also increased! Fewer options are now blocked in “SANDBOX MODE!”{/i}"

    "Now what should I do?"

    jump ch4morningmenu

label saraspring1:
    scene nightsky
    with dissolve2
    play music "calmbar.mp3"

    "It’s as good a night as any to drown my sorrows in alcohol. And I’m sure Sara would agree as that is both her chosen method for doing the same thing {i}and{/i} she’ll manage to make some money out of it."
    "However, now that her daughter has a newfound (or newly open) affinity for extracting semen from my body, there’s a good possibility I’ll be able to drown my sorrows in a different, {i}cheaper{/i} way."
    "I’d probably pay if she really asked me to. But I’m glad she took after her mother’s thirst for teacher cock as I just happen to be a teacher who possesses one."
    "Anyway, beer. "
    "Sex."

    play sound "static.mp3"
    scene sarayukicheck1 with flash
    stop sound

    "And orchestrated encounters with a small family of angels. "

    sar "Oh! Hey. I wasn’t expecting you to show up tonight."
    sa "Neither...was I..."
    s "Why? I come here all the time. What reason would you possibly have to believe that?"

    scene sarayukicheck2
    with dissolve

    sar "I think we’ve just developed a Sensei-sense by now. A sense-ei, if you will."
    sa "Can you...please stop making terrible puns? Even if this particular one is...mostly correct."
    sar "Not if you want to stay in business, Sana. This building is quite literally built on top of a terrible pun."
    s "Well, yes— I am here. So your Sensei-sense is clearly lacking. "
    s "Now, please provide me with ten beers so that I may drink myself into a stupor and ignore all of my other problems."

    scene sarayukicheck3
    with dissolve

    sar "No can do! I’ve got a job for you since you just so happened to wander in at the perfect moment."
    sa "Are you...really going to make him come with you?...And just...leave me here on my own again?..."
    sa "Wouldn’t you be...better suited for that, don’t you think?..."

    scene sarayukicheck4
    with dissolve

    sar "Nope! I trust you with my bar and my life, Sana. Plus, you’ve done it a million times before. And, if everything goes according to plan, you won’t {i}have{/i} to start doing that again."
    s "I feel like I get dragged into “missions” more often than I’m supposed to here."

    scene sarayukicheck5
    with dissolve

    sar "Blame this one on Yuki, not me. She’s the one who keeps forgetting to show up for her shifts."
    s "Again? Really?"
    sa "She was...supposed to be here tonight, but...I guess she...forgot?..."
    s "That excuse made sense last time. But if that {i}keeps{/i} happening, something else is probably going on."
    sar "Exactly. Which is why I’m headed over to her place now to make sure everything’s okay. "

    scene sarayukicheck6
    with dissolve

    sar "And why {i}you{/i} get to come with me so I’m not abducted in the middle of the night and sold into the sex trade! "
    sa "Alternatively, you could stay here and we could just...{i}let{/i} her be abducted."

    scene sarayukicheck7
    with dissolve

    sar "Boooooo. Surely {i}you{/i} don’t want me to be trafficked. Right, Sensei?"
    s "Ten beers please, Sana."

    scene sarayukicheck8
    with dissolve

    sa "Coming right up, Sir."
    sar "After all we’ve been through, you’re going to just let me become someone’s sex slave?! "
    s "I’m not {i}letting{/i} anything happen. I just can’t imagine the sex trade is going very strong right now on account of nearly every male being somewhere in space. This is a calculated, low-risk move."
    sar "Sana, I would expect this from! But not you, Sensei!"
    s "Okay, fine. I’ll come with you. But only because hearing that you’d {i}expect{/i} your daughter to be okay with this is very sad."

    scene sarayukicheck9
    with dissolve

    sar "Yay! I’ll take what I can get."
    sa "But what if someone barges in here with a gun and {i}I{/i} get sold into-"

    scene sarayukicheck10
    with dissolve

    sa "Actually, I’ll probably be fine. You two can go."
    sar "Yay! You heard the girl! Come on, Sensei!"

    scene black
    with dissolve

    s "Are you sure that’s a note you’re okay leaving on?"
    sar "Everything will be fine! You’re the most intimidating customer we get. So if {i}you{/i} haven’t laid a finger on Sana yet, I doubt anyone else is going to."

    scene sarayukicheck11
    with dissolve

    s "I repeat — are you sure that’s a note you’re okay leaving on?"
    sar "I don’t have much of a choice. For all we know, Yuki could be in greater danger than Sana is. And sending {i}her{/i} out on her own is out of the question entirely. Bye, Sana!"
    s "But...you {i}could{/i} stay here and-"
    sar "Bye, Sana! Your mom is going on a date!"
    sa "No she’s not! But have fun! Take your time!"
    s "If Yuki’s actually in trouble, do you really think we should be taking this so...{i}lightly?{/i} She has ties to the Yakuza. That’s pretty serious, isn’t it?"

    scene sarayukicheck12
    with dissolve

    sar "Oh, please. Have you {i}seen{/i} Yuki? I’m pretty sure she could take the entire Yakuza out on her own. This is just a normal wellness check. I’m sure everything will be fine."
    s "Famous last words, Sara. Once you say that, you pretty much solidify that everything is going to not {i}be{/i} fine."

    scene black
    with dissolve2

    sar "Well, then we need to go and figure that out! Bye, Sana! Date!"
    sa "Not a date! But still have fun!"
    sar "Date! Bye!"
    sa "Mom! Stop-"

    play sound "static.mp3"
    scene sarayukicheck13 with flash
    stop sound

    "We’re outside now. I think we’re on a date."

    if sarasex == False:
        "Which, to be fair, I’m not really cool with. But it makes Sara happy and there are clearly bigger issues that need to be addressed right now. "
    else:
        "I’m pretty sure it’s the kind that won’t end in sex, though. Especially since the entire purpose of it is to...make sure Yuki is still alive?"

    "To be honest, I can’t help but worry. Because even though I’m not particularly {i}close{/i} with Yuki, she has hollowed out {i}some{/i} kind of spot in my mind or heart or wherever it is feelings come from."

    sar "No answer again. I’ve called her like twenty times now."
    s "And...how many times has she missed work exactly?"

    scene sarayukicheck14
    with dissolve

    sar "Four or five, I think. I haven’t exactly been keeping track. But I haven’t really {i}needed{/i} to since business has started to slow down again."
    s "Any idea why? "
    sar "Not a clue, really. It feels like it just happened overnight or something. It’s fine, though. Chances are some new bar opened and people are just high on that right now."
    sar "But that’s one more reason I have to figure out what’s going on with Yuki as soon as possible. We’ll need all hands on deck once the masses start returning."
    s "So this is purely a business venture we’re on right now? "

    scene sarayukicheck15
    with dissolve

    sar "Of course it’s not {i}purely{/i} a business venture. Yuki’s my friend. If she was {i}just{/i} an employee, I probably would have only called her, like...five times."
    s "Have you brought this up {i}at all{/i} to her? How did she explain her absence the first time? Or the times after that? Because there’s no way she’s just missed four or five shifts in a row, without-"

    scene sarayukicheck16
    with dissolve

    sar "Sensei, I know you’re worried. I am too. I’m not just ignoring Yuki’s “history.” I know who she is and what she suffers from."
    sar "But I’ve got it under control."
    sar "Not wanting my little girl to be out in the dark alone isn’t the only reason I didn’t want her going over to Yuki’s place, you know. "
    sar "I’m prepared for the worst. "
    sar "And I’m sorry to drag you into it...but I’m way more comfortable with you by my side."
    s "..."
    sar "Now, let’s get a move on. "
    sar "The quicker we get to her, the quicker we can rest."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene sarayukicheck17
    with dissolve2

    "I’ve been here before — with a smaller her."
    "And while their silhouettes are similar, there’s one inarguably closer to mine in more ways than one could count."
    "It’s better at matching my pace. And in between imperfectly timed steps, there’s no massive gap in size that would cause the laymen to question just how “it” would fit and how much it would hurt."
    "She’s older than me. She doesn’t know that yet, but it’s the truth. Yet, I’ve never seen her as an older sister."

    if saraspecial30p2 == True:
        "There are things we have in common. Things that no one should. But it’s the type of connection that can only strengthen a bond when you {i}want{/i} it to. At all other times, it’s the kind that should be feared."
        "Like two people witnessing a murder — locking eyes before heading their separate ways and forgetting they ever saw anything. Or at least trying to."
        "That’s the way it feels sometimes. Like we not only {i}see{/i} each other, but we can see into each other’s pasts."
        "And I’m not sure how comfortable either one of us is about that. Especially when I’ve yet to divulge much of mine to her in any form."
        "Regardless, I can see her."
        "And in this light, despite it illuminating the path to somewhere much darker, she is beautiful as always while I step closer to the shadows to accentuate the difference."

        jump restofsaraspring1
    else:
        "A good friend is more apt of a description, I suppose. But despite how good she {i}is,{/i} there’s this sort of...untapped or inaccessible knowledge that I {i}want{/i} to grab hold of but {i}can’t.{/i}"
        "I’m sure there’s a life in which we’re closer. Maybe not as close as brother and sister, but close in a form where she would spread her legs or open her mouth with me upon command."
        "Would she drop to her knees right now if I uttered the required words? Or would she make me take her out to dinner first?"
        "These are the bits of knowledge I’ve elected to forego in the name of protecting her offspring."
        "But I am certain-"
        "There are much more important details in the fabric that are lost to my unclean eyes."

        sar "..."
        s "..."

        scene black
        with dissolve2
        stop music fadeout 10.0

        "There are no words the rest of the way."
        "It appears I haven’t earned them."

        $ renpy.end_replay()
        $ saraspring1 = True
        $ sara_love += 1

        "{i}Sara’s affection has increased to [sara_love]!{/i}"
        "{i}But she will always be a side character.{/i}"
        "{i}And you will continue to crawl away from a world that’s breaking down behind you.{/i}"
        "{i}The pieces to your puzzle have fallen somewhere between the cracks. But you’re too scared to turn around and search for them.{/i}"
        "{i}And maybe you’re better off that way.{/i}"
        "{i}But maybe such a decision will make it possible to ever get out?{/i}"
        "{i}There’s only one way of knowing.{/i}"
        "{i}But there’s one more for someone stronger.{/i}"
        "///////////////////////TEMPORARY END"
        "///////////////////////LOCATING “YUKISPRING1”"
        $ renpy.pause(5, hard=True)
        "///////////////////////DESTINATION LOCATED"

        jump yukispring1

label restofsaraspring1:
    sar "So...it’s been a while since I’ve “checked in” on you."
    s "Probably on account of the whole coma thing. And the immeasurable sadness that has become my everyday life."
    sar "Has your outlook on the world not changed since becoming a father?"
    s "Did yours change when you became a mother?"

    scene sarayukicheck18
    with dissolve

    sar "Of course. It’s pretty noticeable going from having {i}no{/i} reason to live to having an extremely clear one. Was it not like that for you?"

    scene sarayukicheck19
    with dissolve

    s "Maybe it was years ago. I can’t...vividly remember that far back. But just changing what I call Ami hasn’t made as big of an impact on me as I thought it would at first."
    sar "Hm."

    scene sarayukicheck20
    with dissolve

    sar "Guess I’m just a better parent than you, then."
    s "Guess so."
    sar "The choice is always there for you to join my family, though. Maybe adding another daughter to the mix could shock you back into the initial thrills of fatherhood?"
    s "Yeah, I’m not sure I could ever look at Sana as a daughter anymore. Sorry, Sara."

    scene sarayukicheck21
    with dissolve

    sar "Who says I’m talking about Sana? Maybe I’m suggesting that I want you to put a {i}new{/i} baby in me?"

    scene sarayukicheck22
    with dissolve

    sar "Wait- why wouldn’t you be able to look at Sana as a daughter, though? It’s not because she’s one of your students, is it? Because Ami-"
    s "No, it’s not that. She’s just..."
    s "She’s been...different lately."

    scene sarayukicheck23
    with dissolve

    sar "D..."
    sar "Different how? Because I told you to tell me if anything changed. If Sana is-"
    s "I don’t...no. Not like that, Sara. I doubt she’s the same as {i}us{/i} in regard to the whole “blacking out” phenomenon. But...she did mention having dreams."
    sar "What...kind of dreams? Did she say? Because they could be important. They might...mean something? I don’t know. What were they? Do you know?"
    s "I do. I just don’t know if it’s something you want to hear."
    sar "I do. I {i}need{/i} to know if it involves my daughter. Because she hasn’t said anything to me and-"
    s "She’s been dreaming of something...{i}someone{/i} you don’t like talking about."

    scene sarayukicheck24
    with dissolve2

    sar "...oh."
    s "Yeah...But she started changing even before that."
    s "The thing is, though...I’m pretty sure it’s less of a {i}change{/i} and more of her simply...revealing to me the way she’s always been."

    scene sarayukicheck25
    with dissolve

    s "She’s kind of like a chameleon, if you think about it."
    s "She’s great at blending into her surroundings and making herself {i}seem{/i} harmless. But she’s {i}really{/i} an opportunistic hunter waiting for her chance to strike."
    sar "Are you sure we’re talking about the same girl? Because {i}my{/i} Sana isn’t like that at all."
    s "Then maybe she’s hiding who she really is from {i}you{/i} too."
    sar "Why...would she do that, though? I don’t get it."
    s "Beats me. People do all sorts of things that I don’t understand. And lately, Sana’s just...started to become one of them."
    sar "..."
    s "..."
    sar "I don’t like this."
    s "Just...part of being a parent, I guess."
    sar "No, I don’t like that you’re hiding something from me about my daughter."

    scene sarayukicheck26
    with dissolve

    sar "You {i}know{/i} how worried I am about her. You know how desperate I am to make sure she doesn’t wind up like me. I offered you my bar. My apartment. Anything you want..."
    sar "So is there just {i}nothing{/i} you want? Or are you hiding whatever’s going on from me for some {i}other{/i} reason? Be real with me, Sensei. As a parent. You’d want to know about Ami, wouldn’t you?"
    s "Well...let me ask you this."
    s "If Sana {i}did{/i} become like you — not in the sense of blacking out...or {i}seeing{/i} things...but {i}as a person{/i} — how would you feel about {i}that?{/i}"

    scene sarayukicheck27
    with dissolve

    sar "{i}Hah...{/i}"
    sar "So {i}that’s{/i} what you mean..."
    s "..."

    scene sarayukicheck28
    with dissolve

    sar "I guess it really {i}is{/i} in our genes then."
    s "...Sara?"

    scene sarayukicheck29
    with dissolve

    sar "When did it happen?"
    s "When did...{i}what{/i} happen?"
    sar "She came onto you, didn’t she? It was only a matter of time."
    s "..."
    sar "Relax...I’m not {i}mad.{/i} I was the same age as her when I went down that same path, remember?"
    sar "It’s not like I can tell her to “learn from my mistakes” or whatever when she quite literally {i}only exists{/i} because of them."
    sar "I regret nothing. And if this is what gets you to keep a closer eye on her, so be it."
    s "..."
    sar "..."
    sar "Sensei?"
    s "Literally any response I make right now would either be incriminating or bad, so I’m just going to keep my mouth shut."

    scene sarayukicheck30
    with dissolve

    sar "It’s preferable to finding out she’s hallucinating and getting thrown on auto-pilot for hours at a time. At least I know she’d be {i}safe{/i} with you."
    s "I’m an adult male. Your daughter is in high school and under five feet tall."
    sar "I know. Isn’t she just adorable?"
    s "..."

    scene sarayukicheck31
    with dissolve

    sar "Incriminate yourself already! I want to scold you for being a bad boy!"
    s "I take it you’re just...{i}fine{/i} with her becoming like you, then?"

    scene sarayukicheck32
    with dissolve

    sar "Mm...I mean {i}ideally,{/i} she’d wait a few more years until her body is fully developed to start fooling around with actual {i}people.{/i} And even more ideally, she wouldn’t come after my boyfriend like this."
    s "I’m not your boyfriend."
    sar "Yes you are. Shut up."
    s "I’m trying to. You’re the one who keeps trying to make me talk."
    sar "Uhh, {i}yeah.{/i} Because you totally just admitted that the reason my perfect future family’s in jeopardy is because my daughter is suddenly horny for her prospective daddy."
    s "Going back to silence now. Goodbye."

    scene sarayukicheck33
    with dissolve

    sar "If {i}that{/i} is the worst of the changes you’ve seen from Sana, that’s like...the {i}best{/i} case scenario. However, as her mother and your girlfriend, I can not give you my blessing."
    s "I don’t {i}want{/i} your blessing. That’d be weird as hell."

    scene sarayukicheck34
    with dissolve

    sar "Great! That’s settled, then."
    s "{i}What{/i} is settled? I have no idea where we even are in this conversation anymore."
    sar "We’re at the part where I remind you to keep your eye on my daughter for {i}actual{/i} developments or changes. Not ones everyone and their mother saw coming."
    s "I-"
    sar "Get it? Because {i}I’m{/i} her mother."
    s "..."
    sar "And I could tell she was hot for teacher just like me."
    s "Yeah, I get it."
    sar "So you agree then?"
    s "To...have sex with your daughter?"

    scene sarayukicheck35
    with dissolve

    sar "Noooo! To tell me if and when something is wrong! {i}I’m{/i} the one who gets to have sex with you! I worked for it! She can’t just swoop in and steal you! That’s not fair!"
    s "Of course I’ll tell you if something’s wrong, Sara. But...I’d feel wrong if I didn’t make it abundantly clear that I might {i}not{/i} know something like that."

    scene sarayukicheck36
    with dissolve

    s "If Sana kept her feelings about {i}me{/i} hidden for so long, who even knows what else she could be hiding? Revealing intimate details just...isn’t a thing she does?"
    sar "Then...what are we supposed to do?"
    s "I don’t know...Wait and see if she tackles one of us to the ground and fucks us in the ass?"

    scene sarayukicheck37
    with dissolve

    sar "Ugh! {i}Again?!{/i} I can only take so much!"
    s "Better you than me."
    sar "Yeah because {i}you’d{/i} get to stand there and watch while I’m sodomized and forced to figure out how to tell Sana she just screwed her own mom."
    s "You’d let me watch?"
    sar "Might as well. We’re already doing it."

    scene black
    with dissolve2
    stop music fadeout 13.0

    s "I’m going to have a lot of trouble figuring out if this makes you a better or worse mom when I’m getting into bed tonight."
    sar "Aww, you think about me in bed? That’s so sweet! I do the same thing. Sana too, apparently."
    s "Sara..."
    sar "Boyfriend..."
    s "How about we just...drop it? We’ll be at Yuki’s soon anyway."
    sar "Works for me!"
    sar "You know, Yuki would probably let you screw her daughter too. She gets it."
    s "I don’t think either of you get it..."

    $ renpy.end_replay()
    $ saraspring1 = True
    $ sara_love += 1

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "........."
    "......"
    "..."

    jump yukispring1

label saraspring2:
    scene sarabtc1
    with dissolve2
    play music "calmbar.mp3"

    "I find myself at the bar, staring longingly into the eyes of a woman who probably wouldn’t mind if I boned her daughter."
    "And that’s good, because I’m probably going to bone her daughter."
    "I kid. Just not really. But also {i}kind of{/i} because that’s not why I’m here tonight."
    "I’m here to relax and unwind and get partially inebriated under the supervision of someone I feel like I could unironically trust my life with."
    "It’s a bit ironic given that one life has already been lost under her supervision, though. "
    "But we don’t talk about that."
    "We sit. And we stare. And we drink. And we pretend the world is a little better than it is."
    "That’s what bars are for. And there’s nothing quite like a silent night at one with someone you truly love."
    "..."
    "God damn it."

    sar "And then there were two..."
    s "We’ve been alone for like three hours now."
    sar "Yeah, but the bar is officially closed as of five minutes ago. Which means I can use that line and have it be all romantic and intimate."
    s "But-"

    scene sarabtc2
    with dissolve

    sar "And then you’d kiss me and {i}propose{/i} and I’d say yes with tears in my eyes and leap across the counter into your arms where you’d princess carry me all the way back to your house and make love to me."
    s "I-"
    sar "All night. And then I’d get pregnant and-"
    s "Sara, I think you’re overestimating my strength. There’s no way I can carry you all the way to my house."

    scene sarabtc3
    with dissolve

    sar "Hey! You’re not calling me fat, are you? Because you haven’t even gotten me pregnant yet, mister. At least wait until then to start resenting me for my image changing."
    s "Are you done yet?"

    scene sarabtc2
    with dissolve

    sar "And then after we’re done having sex, we’d fall asleep in each other’s arms and then wake up the next morning to go look at houses."
    sar "But it wouldn’t be {i}all{/i} fun and games since we’d also have to set aside time that day to tell Sana that her fantasies of stealing her mother’s boyfriend have been washed away like-"
    s "Condoms in the sand?"

    scene sarabtc3
    with dissolve

    sar "What?"
    s "Old reference. You wouldn’t get it."
    sar "Why are they in the sand?"
    s "They just are, Sara."
    sar "Do you even know how to put a condom on?"

    "Yes. Your friend’s daughter used to make me wear them."

    s "Nope. So please never ask me to as I’d like to avoid the embarrassment. "

    scene sarabtc4
    with dissolve

    sar "Works for me. Just don’t get mad when I wrap my legs around you on a danger-day and squeeze you for every last potential child you’ve got."
    s "You know, you’re really good at saying things that give me erections."
    sar "And you’re really good at putting your erections inside of me. We make a good team."
    s "We’re going to have sex tonight, aren’t we?"
    sar "We better, otherwise I’ll have shaved for nothing."
    sar "Before that, though...there’s something else I want to do."
    s "Sana already went home. We can’t drag her into things this time."

    scene sarabtc5
    with dissolve

    sar "What? No! That’s not- "
    sar "I meant I want to get to know you better."
    s "Oh. Doesn’t that normally come {i}before{/i} people start regularly having sex, though?"

    scene sarabtc6
    with dissolve

    sar "Not from my experience."
    s "Mine either, to be honest. I guess that means you didn’t really know anything about Sana’s dad either then?"
    sar "Nuh-uh. Nope. Not happening. Not answering that question."
    s "Uh...okay. Can I ask why?"
    sar "It’s just that we {i}always{/i} talk about me when we get into background stuff. So I’m not going to answer any questions about myself this time. "
    sar "Tonight, I want to learn something about you. Something personal. Because you’ve emptied at least five gallons worth of jizz into me now and I still feel like I barely know you."
    s "If only semen carried memories and I could just inject them into you via sex."
    sar "That’d be crazy."
    s "Yeah. No one would like me anymore."
    sar "Does that mean your memories are bad? Or evil? Is our relationship just one long con you’re carrying out to try and empty my bank account before running away?"
    s "That last part would actually make things way easier to explain so, sure. I am a con man."
    sar "Sensei, come on. Anything is fine. I just want to know more about you. Is that really so bad?"
    s "You know the blackout thing, don’t you?"
    sar "Yeah, but only because you sodomized me. Isn’t there something I can learn that {i}won’t{/i} come along with intense pain?"
    s "..."
    sar "{i}Anything?{/i}"
    s "I am a con man."

    scene sarabtc7
    with dissolve

    sar "{i}Hah...{/i}"
    s "Really, though. There’s something I’ve been keeping from you."

    scene sarabtc8
    with dissolve

    sar "Something you’ve been...keeping from me? Like, intentionally?"
    s "I’m a liar, Sara. And hearing this might hurt you, but...if you {i}really{/i} want to know more about who I am, I can’t keep it a secret any longer."

    scene sarabtc9
    with dissolve

    sar "Wait, hold on! I’m not sure if I want to know anymore! This sounds bad!"
    sar "Do you have some kind of STD? Is Sana already pregnant? Do you have some kind of incurable terminal illness that you didn’t want to tell me about because you were afraid of hurting me?"
    s "Worse."

    scene sarabtc10
    with dissolve

    sar "Worse?!?!? How?!?!?"
    s "Sara — do you remember how old I told you I was?"

    scene sarabtc8
    with dissolve

    sar "Of course. You said you were 34 . And then {i}I{/i} was like, “Yay! We’re almost the same age!” Then-"

    scene sarabtc11
    with dissolve

    sar "{i}No.{/i}"
    s "The truth is..."
    sar "Don’t say it."
    s "I’m actually 31."

    scene sarabtc12
    with dissolve

    sar "NOOOOOOOOOOOOOOOO!!!!!!! WHY??!?!?!?!"
    s "I’m sorry you had to find out this way..."
    sar "I wish you would have just sodomized me again instead!"
    s "I mean...I can arrange that."

    scene sarabtc13
    with dissolve

    sar "Does this make me a cougar now? What age do I have to be to become one? Is there a rule for that? Am I okay if it’s only a two year age gap? "
    s "I think you’re fine. I just knew you wanted to be the younger one in the relationship, so I may have...kept this a secret for a little longer than necessary."
    sar "Why did you even lie in the first place? Were you just-"

    scene sarabtc14
    with dissolve

    sar "Ah! You were just trying to impress me, weren’t you?"
    s "..."
    sar "You {i}were.{/i}"
    s "Yup. You got me."

    "It has nothing at all to do with the fact that I didn’t even know how old I was when we first talked about this."

    scene sarabtc15
    with dissolve

    sar "Hm...So you {i}like{/i} older girls then..."
    s "Yup. Got me again."

    "I don’t even need to comment on this one."

    sar "Hmmmmmm..."
    s "..."
    sar "So, if I’m a cougar as decided by whoever creates the cougar guidelines, what does that make you? Is there a term for younger boys who go after older girls? Are you like, a...cheetah or something?"
    s "You seem to have flipped from being miserable about this to very okay with it in a matter of seconds."
    sar "Well, duh. Of course I’d be miserable finding out that {i}I’m{/i} your elder by roughly two decades."
    s "Two {i}years.{/i}"
    sar "Two centuries. But I feel a little better now knowing that you’re into that sort of thing."
    s "Does that mean you’re just going to play this up from now on then?"
    sar "{i}Maaaaaaybe.{/i} I haven’t seen how you respond to being touched by a wise onee-san yet. Maybe I’ll like it?"
    s "I mean...technically, you {i}have{/i} experienced that. I didn’t {i}just{/i} decide to be 31. I’ve been 31 the whole time we’ve known each other."
    sar "Riiiiiiight. The {i}whole{/i} time we’ve known each other. As if we haven’t-"

    play sound "static.mp3"
    scene ayhh11 with flash
    scene sarabtc16 with flash
    scene ayhh11 with flash
    scene sarabtc17 with flash
    scene ayhh11 with flash
    scene sarabtc18 with flash
    stop sound

    sar "..."
    s "..."

    scene sarabtc19
    with dissolve

    sar "What were we talking about just now?"
    s "Uhh..."
    s "Something about you being older than me, I think?"

    scene sarabtc20
    with dissolve

    sar "R-Right! Yeah."

    scene sarabtc21
    with dissolve

    sar "So...now that we know that...and I’ve obtained an extra piece of information..."
    sar "What do you say we go back up to my room and you let onee-san take care of you?..."
    s "No thanks."
    sar "That’s what I-"

    scene sarabtc22
    with hpunch

    sar "No thanks?!"
    s "Yeah, no thanks."
    sar "Were you just humoring me then?! Is me being the older one actually going to be a problem?! Just pretend I’m 18! I look it, right?! I don’t care!"
    s "Sara-"
    sar "In fact, {i}please{/i} pretend I’m 18! It will make me feel better about myself and Sana will be more inclined to hang out with me!"
    s "Sara, I just meant that I’d rather do things somewhere else. "

    scene sarabtc23
    with dissolve

    sar "Oh. You mean like a...love hotel or something?"
    s "Sara, you have an entire bar. A bar that we have, somehow, never actually done anything in."
    sar "Have we really never done anything down here?"
    s "Not that I can remember, no."
    sar "That’s actually really impressive. I’m surprised we’ve managed to keep the streak going this long. I almost don’t want to break it now."
    s "I heard an “almost” in there. "
    sar "You sure did. And if you come over to my side of the counter, you’ll find out just what I-"

    play sound "static.mp3"
    scene sarabtc24 with flash
    stop sound

    s "I am here now."
    sar "Excuse me, sir. But I’m afraid I can’t let you leave the bar without paying your tab."
    s "Give me all the money in the register. And don’t even think about calling the cops."

    scene sarabtc25
    with dissolve

    sar "Are we doing CNC instead? Do you want to change the scenario up? Are you going to take me against my will?"
    s "Is that...something you’d be into?"
    sar "It’s not...{i}not{/i} something I’m into."
    s "..."
    sar "Or I could just get on my knees and suck your cock without any roleplay involved. I just thought it’d be hot if you were like, some young stud trying to wine and dash and I made you pay in “other ways.”"
    s "That scenario would make more sense if I was the one who had to service {i}you.{/i}"
    sar "Yeah, I guess. But I want to suck your dick. And the exchange rate of cum to alcohol matches up perfectly based on the current...economy or whatever."
    s "..."
    sar "Pay me?"

    scene black
    with dissolve2

    s "Can I just...{i}always{/i} pay like this from now on?"
    sar "You sure can, [saramaster]."

    scene sarabtc26
    with dissolve

    sar "It’ll be our little {i}deal.{/i} You drink as much as you want, I drink as much as {i}I{/i} want. Just I have to work a little harder for it."
    sar "But that’s okay. I {i}am{/i} on the clock after all."
    s "You’re about to be on the “cock” too."

    scene sarabtc27
    with dissolve

    sar "Pffft!!! Hahahaahahah! "
    s "Please don’t laugh. My terrible sense of humor is not meant to be rewarded with jubilance."
    sar "It was just so bad!!! Hahaahaah!!! That’s worse than Sakaki-bar-a!!!"
    s "{i}Nothing{/i} is worse than Sakaki-bar-a."

    scene sarabtc28
    with dissolve

    sar "There are lots of things worse than Sakaki-bar-a. How many other bars can you name where you can just walk behind the counter and get a blowjob from the bartender?"
    s "I’m not sure. But maybe that’s where all of your business has gone lately?"
    sar "Secret sex bars scattered throughout Kumon-mi?"
    s "You know, you and Maki could probably join forces and make a lot of money off something like that."

    scene black
    with dissolve
    play sound "zipper.mp3"

    sar "You know, you’re probably right. Even with the lack of men, there are tons of girls who’d pay to get “serviced” by Yuki. And Maki’s super skilled at pretty much everything."

    scene sarabtc29
    with dissolve2

    sar "But I’d be the manager of course. And I wouldn’t even {i}consider{/i} servicing anyone but you..."

    "Sara unsheathes my cock and begins to passionately stroke it, gazing up at me as I run my fingers through her hair."
    "Her grip is tight despite her excluding one finger from the process — and as I look down at her and see her smiling just inches from my flesh, I regret not telling her more about me."
    "I regret choosing something superficial. Because while learning that she’s older than me can assuredly change the way she fucks me-"
    "I can only imagine the changes that would come if she knew where I {i}really{/i} came from."

    sar "How’s that, [saramaster]?...You like it when onee-san jerks you off?..."

    scene sarabtc30
    with dissolve

    sar "Such a big...{i}strong{/i} cock you’ve got here...ahm...full of youth...aaahn...and vigor..."
    sar "I bet you really want to...ahmm...stick it in...don’t you, [saramaster]?..."
    sar "You want to fuck onee-san all night long, don’t you?...Mmn...mm...you want to cum inside her pussy, [saramaster]?..."

    scene sarabtc31
    with dissolve

    sar "Or would you rather just stand there and let me take advantage of you?..."

    play sound "static.mp3"
    scene mombattlebutdifferent29 with flash
    scene sarabtc32 with flash
    stop sound

    s "Mmn...That...one..."
    sar "{i}Yeah?...{/i}ahlm...you wanna be onee-san’s little plaything tonight?...Is {i}that{/i} what you want, [saramaster]?..."
    s "S..."
    sar "S?..."
    s "...ngh."

    scene sarabtc31
    with dissolve

    sar "{i}Chu...{/i}you just stay quiet, then...onee-san will handle everything..."

    scene sarabtc32
    with dissolve2

    sar "Mm~"
    sar "Mnf...mlm...mmnh....mmm! [saramaster]...you’re so {i}huge...{/i}I can barely fit it in-"

    scene sarabtc33
    with dissolve

    sar "Mm!"
    s "Aren’t you supposed to be more {i}experienced{/i} than me, {i}onee-san?{/i}"

    scene sarabtc34
    with dissolve

    sar "Mm?..."
    s "Don’t talk about how it’ll “barely fit” when you’re just getting started. If you’re going to suck my cock, you’re going to do it correctly. Do you understand?"

    scene sarabtc35
    with dissolve

    sar "Mm...mmmm! Oneeshnn......wllwrk......hrdrr!!!"

    scene sarabtc36
    with dissolve2

    sar "Mm! Mm! Mm! "

    "I guide myself deeper into Sara’s mouth and begin to stroke myself as her tongue dances wildly across my skin."
    "She reaches forward and begins to caress my balls, still desperate to please me in any way she can despite how I’ve stolen the reins from her."
    "But this is what needed to be done. For if I allowed her to take control, I would have seen her as someone else."
    "This way, we can {i}both{/i} get what we want. And I can stave off the impurities that live within my mind for at least one more hour."

    scene sarabtc37
    with dissolve

    sar "Mm~ Mm...[saramaster]...ssbgg...flgdd?...Yllktht?..."
    s "You’re so pretty...{i}onee-san...{/i}you’ll make a wonderful outlet..."
    sar "Mm...mmm~! Otlt?..."
    s "That’s right. I’m choosing you as a very special girl in my life. You should be happy."
    sar "Mm! Iamhppy...Ilvyrcock!"

    play sound "dooropen.mp3"

    sar "Iwntyouto-"
    s "Wait. Shh."

    $ renpy.end_replay()
    $ saraspring2 = True
    $ sara_love += 1
    $ sara_lust += 1

    jump tsubasaspring2

label saraspring3:
    play sound "static.mp3"
    scene saraflashbacktime1 with flash
    stop sound

    sar "Instead, I’ll just sit here and hope that absorbing all of that information is not currently and discreetly rotting me from the inside out."
    sar "Which I think it is."
    sar "..."
    sar "..."
    sar "..."
    sar "Yup. It definitely is."

    stop music
    play sound "static.mp3"
    scene saraflashbacktime2 with flash
    stop sound
    play music "beginningoftheend.mp3"

    "I’m probably just overreacting."
    "Sana’s only doing what makes her happy. "
    "And if I need to suffer for that to be the case, then so be it."
    "This is what I signed up for when I was her age. And thinking I can just back out of it now that I’ve seen what it’s like on film is dumber than thinking I can manage a place like this alone."
    "Though it’s {i}not{/i} as dumb as thinking I could raise children alone. {i}That{/i} is my crowning achievement."
    "And the trophy I’ve earned from my failure now turns itself into a shadow and hangs over my head, whispering into my ear whenever I try to sleep."
    "At least that voice isn’t beckoning me closer to depravity, though."
    "I guess this is what I get for looking into the mirror too long."

    play sound "static.mp3"
    scene saraflashbacktime3 with flash
    stop sound

    sar "Aaah! Aaah! Harder! Harder, Sensei!"

    "I wonder if she does it as much as we did."
    "I wonder what her favorite positions are. "
    "If Sensei is gentle with her. "
    "If she ever {i}wants{/i} him to be or if she’s even more like me in thinking that’s just never enough."
    "It’s weird, you know? "
    "Because, on one hand, I’m scared. The way any mother would be."
    "But on the other, there’s this strange sense of...{i}pride{/i} that I don’t really know how to put into words."
    "I’ve heard something before. About mimicry being close to flattery. I can’t really remember if those are the exact words, but I think they are."
    "Is her doing exactly what I did just a twisted way of showing me she {i}doesn’t{/i} think I’m a failure?"
    "Is wanting to include me {i}more{/i} than the worst case scenario of her thinking so little of me that I’d come without question?..."
    "I have so many things I want to ask her, but lack the courage to ask any of it at all."
    "There’s one thing I’ve learned for sure, though."

    him "You gonna cum for me, baby? Again? How many times is that now?"
    sar "Ah! Ah! I don’t know! Not...enough, though! Harder! Please!"

    "It’s that this goes deeper than just being starved for attention — because I have given her all I have."
    "And that was infinitely more than I ever received from anyone but {b}him.{/b}"

    play sound "static.mp3"
    scene saraflashbacktime4 with flash
    stop sound

    him "Talk dirty to me, baby...You know how I like it..."
    sar "But Sensei...aah!...I don’t know...anything at all!...I’m just a...slutty...cock-obsessed schoolgirl who...loves how her teacher’s big, adult dick makes her little pussy feel!"
    him "Mmngh...fuck, Sara...how are you still so tight after all this time?"
    sar "Because I’m just a little girl...they’d throw you in jail forever if they saw what you did to me, Sensei...and they’d burn me at the stake for...loving it so much!"
    him "F...Fuck...I should’ve...brought more condoms!"
    him "Let me go grab some from-"

    scene saraflashbacktime5
    with dissolve

    sar "Aaah! No! Don’t leave me! Cum with me, Sensei! I’m not even worth a condom! Just fucking do whatever you want with me! Please! Please, please, please!"
    him "Mngh...Sara...Sara!"
    sar "Sensei! Yes! Just like that! Haah! Aaaah! Aaaaaaah!"

    "It was always me who talked him into finishing inside."
    "And while it wasn’t like I was {i}trying{/i} to get pregnant, I wasn’t exactly against it either."
    "I just wanted something — {i}anything{/i} to make me feel like I had some sort of purpose. Which is probably why I jumped at the fact that someone looked at me the way he did."
    "This is where we’d meet most often. So if I {i}had{/i} taken Sana’s invite, I’d have felt right at home."
    "And if the drab decor mixed with those scents of sex and lotions and stale cigarette smoke didn’t do it for me, the arms of someone larger and stronger would have."
    "But even when he had me pinned down by my shoulders, I never felt like I was trapped. I felt like I was safe."
    "Does Sana feel that way too?"
    "Protected in the arms of someone she trusts more than me?"
    "Would I know the answer by gazing into the mirror once more while the man I pledged myself to {i}this{/i} time moves in and out of her so deeply that I can see it sliding around beneath her skin?"

    scene black
    with dissolve2
    stop music

    "My shame is infinite."
    "My mother, in all her vicious splendor, would have puked if she saw my eyes roll to the back of my head from the ministrations of a man like him."
    "Meanwhile, if I were to see {i}my{/i} daughter at the height of her ecstasy..."
    "I think I’d just be happy knowing there is {i}something{/i} that makes her feel alive."
    "And for the very first time..."
    "It is something we have in common."
    "It is something we can share."
    "........."
    "......"
    "..."

    play music "ichiyarakka.mp3"
    scene saraflashbacktime6
    with dissolve2

    "After he and I finished our rendezvous, we’d shower together and he’d send me on my way."
    "I was supposed to be back by 10:00 on weeknights or my father would hit me."
    "I felt like it was worth it sometimes. Especially the week before my period when my hormones started ramping up and turning me into a borderline nymphomaniac."
    "I imagine it would have been hell without someone for me to spend all of that energy on. And how lucky I was that he was {i}always{/i} willing to help."
    "The walk back was always a little awkward, though."
    "Things were livelier back then. Back when men were still {i}here{/i} and not zillions of miles away."
    "I’d take the long way back through a stretch of food stalls and izakaya because I liked looking at all of the lights and hearing music bleed into the open air whenever a door would slide open."
    "Or at least that’s what I told myself because it made me feel less guilty about trying to make people look at me."
    "And they did. But despite me liking it and {i}wanting{/i} it, I’d never respond. Just smile and keep walking. Quicken my pace a little and take solace in the fact that I wasn’t yet a ghost."

    play sound "static.mp3"
    scene saraflashbacktime7 with flash
    stop sound

    "I knew I could be at any moment, though."
    "I blacked out a lot those years. Saw things. {i}Heard{/i} things."
    "And all it would take for my life to come to an end was one poorly timed blackout in the immediate vicinity of {i}one{/i} bad person."
    "It never happened."
    "And it wouldn’t be until years later that those unfortunate thoughts would manifest in the form of the single worst thing that has ever happened to me."
    "Just...it {i}didn’t{/i} happen to me."
    "My son became a ghost in my place."
    "Now I struggle to even bring him up without everything around me shattering into a million pieces."
    "Is this what I get for defying God?"
    "Should I have listened to the two-headed horse or that woman with blades for wings? Taken their offers in exchange for whatever it is they wanted from me?"
    "I often think so. Especially now that I don’t see them anymore."
    "But back then, I had nothing to give."
    "Why am I ignored now that I {i}do?{/i}"

    scene black
    with dissolve2

    "You probably think I’m crazy, don’t you? Always telling you things like this."
    "I’m sure it also doesn’t help to hear me musing about the way my lover touches my daughter when I should be getting between them instead."
    "But all I do is make mistakes, so it’s impossible to trust my judgement."
    "Sana is safer with him than she is with me. But despite already making her choice, she’s kind enough to include {i}me{/i} as well."
    "Worthless me."
    "Sickening me."
    "{size=-2}Dreadful, nauseating, stupid, pitiful me! Who does nothing but cry and dredge up memories I {i}could{/i} erase but {i}don’t{/i} because I’m afraid of what will happen if I reach back to find them and come up empty-handed!{/size}"
    "If you were real, would you hold me?"
    "{i}Just{/i} me?"
    "Or is there {i}no{/i} world in the trillions that exist where I, alone, am enough?"
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene saraflashbacktime8
    with dissolve2

    "The apartment was different back then. My parents didn’t like to clean — and they’d often let the trash pile up until the place reeked of rotten food and old beer."
    "Sometimes, I’d get sick of it and take it out myself. But most of the time, I just hid in my room or snuck into the movie theater to spend all of my time there."
    "Well, the time I {i}wasn’t{/i} already spending beneath my teacher. Which was a good portion of it if my earlier recollection didn’t already clue you in on that."

    fat "Sara!"

    scene saraflashbacktime9
    with dissolve

    sar "{i}Oh, shit.{/i}"

    scene saraflashbacktime10
    with dissolve

    fat "Where the fuck have you been? What part of 10:00 do you not understand?"
    sar "Sorry, Dad. I lost track of time. It won’t happen a-"
    fat "Oh, don’t give me that shit! You say the same fucking thing every time! You’re lucky we let you go out at all!"
    moth "Especially in {i}that{/i} outfit. I can see your thong from all the way over here, Sara."

    scene saraflashbacktime11
    with dissolve

    sar "Can you {i}not?{/i} I’m allowed to dress myself, aren’t I?"
    fat "Not for much longer if you’re going out in public looking like a cheap fucking prostitute. What happens if you get pregnant, huh? You think {i}we’re{/i} going to help you?"
    sar "I’m not going to get pregnant from wearing a thong, Dad."
    moth "If you get knocked up, make sure it’s a rich boy. We’re tired of running that shitty old bar your grandfather left us."

    scene saraflashbacktime12
    with dissolve

    sar "Can I just...go to my room please? I’m tired."
    fat "Sure. After you clean the fucking dishes like you said you were going to before you left for school today."

    scene saraflashbacktime13
    with dissolve

    sar "What? I never said-"

    play sound "static.mp3"
    scene saraflashbacktime14 with flash
    stop sound

    fat "Are you calling me a fucking liar?! You think you can talk back to me?!"
    sar "Wha- no! I’ll clean them! I just don’t remember saying that!"
    moth "Oh, Sara. You need to learn when to just keep your mouth shut."
    fat "And how to fucking tell time too. We’ve been waiting around all day for you to pull your fucking weight so we can eat dinner. How are we supposed to eat without any dishes, Sara?"
    sar "I’m sorry. I’ll clean them right now. Just please don’t hit me."
    moth "Again with the mouth. You’re no child of mine, that’s for sure."
    fat "What did you just fucking say to me?"
    sar "N...Nothing. I’ll...clean now."

    scene saraflashbacktime15
    with dissolve

    fat "What sort of lowlife, ungrateful, piece of shit daughter can look at the man who puts a roof over her fucking head and assume he wants to {i}hit{/i} her!"
    sar "You just...it looked like..."
    fat "Looked like what, Sara?! Is your big, bad father being {i}mean{/i} to his freeloading daughter again?! Are you scared of me?! After all I’ve fucking done for you?!"

    play sound "tackle.mp3"
    scene saraflashbacktime16 with hpunch

    sar "Yes! I {i}am!{/i} I’ve said it over and over and over again! But you’re always too fucking drunk to-"

    play sound "slap.mp3"
    scene saraflashbacktime17 with flash
    stop sound

    sar "Ngh!"
    fat "Too fucking {i}what{/i} now?! You think I’m a drunk?! Is {i}that{/i} all I am to you?!"

    scene saraflashbacktime18
    with dissolve

    fat "Let’s talk about you then, Sara! What have {i}you{/i} fucking contributed to this house apart from running up the fucking water bill and making it smell like- {i}sniff.{/i} What {i}is{/i} that?"
    sar "Not my face! Please!"
    moth "She’s probably going through my perfume again. I noticed my No. 5 missing."
    fat "{i}*Sniff*{/i} That’s exactly fucking it. It’s not enough to eat all of our fucking food, you’re stealing from your own fucking mother now?!"
    sar "No! I didn’t steal anything! I’m wearing my own perfume! I don’t know what happened to-"

    play sound "static.mp3"
    scene saraflashbacktime19 with flash
    stop sound

    fat "YOU’RE CALLING {i}HER{/i} A LIAR NOW TOO?! WHEN DOES IT FUCKING END WITH YOU, SARA?!"
    sar "NGHGH?!?!!!"
    moth "Don’t choke the girl, dear. Even {i}if{/i} she deserves it."
    fat "She can breathe. She’s just pretending she can’t because she wants you to feel bad for her. Woe is Sara. {i}Poor{/i} Sara. Her life is so fucking hard, isn’t it?"
    sar "Ngckkk....nghhkkk! K...ngchchkkk!!!"
    moth "I {i}do{/i} actually think you’re choking her, dear."

    scene saraflashbacktime20
    with dissolve

    sar "{b}{size=+5}HAAAAAAAAH! AAAAAH!{/b}{/size}"
    fat "Fucking drama queen. That was five seconds. {i}My{/i} dad use to strangle me until my face turned blue. You have any idea how {i}scared{/i} you’d be living under his roof?"
    sar "I’ll do the dishes! I’ll do them right now! I’ll be back by 10:00 from now on! I promise!"
    fat "You sure will. Because starting tomorrow, your curfew is changed to 9:00. {i}That{/i} way, you might actually make it home on time."

    scene saraflashbacktime21
    with dissolve

    sar "But I-"
    fat "{i}But I{/i} don’t give a shit! You’ll do what we tell you or we’ll kick your ass to the street where you can learn what it’s {i}really{/i} like to be {i}scared.{/i}"
    moth "She wouldn’t last ten minutes out there with her thong out. Poor thing would be a meat toilet in less than twenty-four hours."
    fat "Yeah, well at least then {i}someone{/i} would have a fucking use for her."

    scene black
    with dissolve2
    play sound "tackle.mp3"

    fat "Now, get in the fucking kitchen and pull your weight. And go right to sleep after that, you hear me?"

    play sound "static.mp3"
    scene saraflashbacktime1 with flash
    stop sound
    play music "calmbar.mp3"

    sar "..."

    "I used to think I was a better parent than mine because {i}I{/i} never put my children through the Hell that {i}I{/i} was put through."
    "But then one of them found it on accident."
    "Now, I don’t think that much anymore."
    "I try not to think at all, really."
    "But you can see how well that’s working out since the two of {i}us{/i} are here now while I continue to delay the inevitable."
    "This was over the moment she asked."
    "I would cut my belly open if she begged me to in earnest."
    "How lucky I am that she wants to keep me alive when I have done nothing to earn my place in her world."
    "That’s me."
    "Worthless me."

    $ renpy.end_replay()
    $ saraspring3 = True

    scene black
    stop music
    $ renpy.pause(5, hard=True)

    "I should make myself useful."

    $ renpy.pause(1, hard=True)
    scene fin
    $ renpy.pause(4, hard=True)
    scene black
    $ renpy.pause(3, hard=True)

    play sound "static.mp3"
    scene bedroom_day with flash
    stop sound

    $ totaldays += 1
    $ day = 4
    hide wednesday onlayer date
    show thursday onlayer date

    "I need to keep myself busy."

    jump ch4morningmenu

label saraspring4:
    scene saraisanaughtygirl1
    with dissolve2
    play music "calmbar.mp3"

    "Once more, I find myself seated in front of a girl who probably shouldn’t be allowed to work in a bar. "
    "Granted, she probably shouldn’t be allowed to fuck her teacher either and I’ve never had a problem with that, so I doubt I’ll be turning her or her mother in to the authorities anytime soon."
    "Fucking aside but not completely ignored, we still haven’t discussed what I said to her shortly after the first time she accepted me. And we probably should."
    "But we probably {i}won’t.{/i} Because I have already used that dreadful word on far too many girls — and using it on Sana was the result of little more than falling into another one of her traps."
    "I don’t actually love her. I love a dream of her that I can just {i}barely{/i} remember having. "
    "And I’m not about to put this new phase of our relationship at risk by pretending it’s more than it really is."
    "We’re just two insatiable perverts who love to touch each other. "
    "And it just so happens that Sana is not only very good at that, but wants it almost constantly."
    "Probably right now too. Watch."

    s "Sana."
    sa "Yes?"
    s "What are you thinking about?"

    scene saraisanaughtygirl2
    with dissolve

    sa "Hm? Why do you ask?"
    s "Just trying to prove something to the void I’m always internally speaking to."
    sa "Well...I still have homework to do. So...that?"

    "She’s normally hornier than this, I swear."

    s "That’s it? Really?"

    scene saraisanaughtygirl3
    with dissolve

    sa "Mm..."
    sa "I guess I’m also thinking about taking you upstairs and riding you until it snaps off."

    "Boom. Told you."

    scene saraisanaughtygirl4
    with dissolve

    sa "I’m just not entirely sure if my mom is actually asleep right now, so I don’t know how much detail I should go into."

    scene saraisanaughtygirl5
    with fade

    s "I sure {i}hope{/i} she is, because I forgot she was even there."
    sa "I’m {i}pretty{/i} sure she’s passed out...so I probably wouldn’t worry about it. "
    s "That’s sort of unusual for her while the bar is open, isn’t it?"
    sa "Yeah...I’m pretty sure I know why though."
    sa "She told me she wanted to talk to me about something and then just kept drinking until she turned into {i}that.{/i}"

    scene saraisanaughtygirl6
    with dissolve

    sa "So I guess I’m working alone tonight. And I guess we aren’t talking after all."
    s "Do you know what she wanted to talk to you {i}about?{/i} Or..."
    sa "Let’s just say I’m probably not the daughter she thought I was."

    scene saraisanaughtygirl7
    with dissolve

    s "Yeah, well...you’re definitely turning out different than {i}I{/i} thought you were too."
    sa "In a good way or a bad way?"
    s "Depends on which role I’m in while you ask me that question. As your teacher, you are exponentially worse than I could have ever expected."
    sa "And as...whatever it is you {i}really{/i} are?"
    s "Good. {i}Very{/i} good."

    scene saraisanaughtygirl8
    with dissolve

    sa "Heheheh..."
    s "Don’t let it go to your head, though."
    sa "Too late. Want to come upstairs and help me {i}clean my room?{/i}"
    s "What if your mom wakes up?"
    sa "She won’t. We’ve already been through this, Sensei. The {i}first{/i} time you saw my room."
    s "..."
    sa "Does it persuade you at all knowing I’m on birth control now?"

    scene black
    with dissolve
    play sound "tackle.mp3"

    s "Yes. Now, let’s go. Before she realizes I was here."

    play sound "footsteps.mp3"
    stop music fadeout 15.0

    sa "Heheh...afraid you’ll make her {i}jealous?{/i}"
    s "Afraid she’ll find out what I do with her daughter."
    sa "It’s not the end of the world even if she {i}does,{/i} Sensei. For all you know, she might even want to join in~"

    scene saraisanaughtygirl9
    with dissolve2

    s "{i}Yeah...no. That’s not happening.{/i}"
    sa "{i}Not with that attitude, it’s not.{/i}"
    sar "Hah..."

    "That fucking idiot..."
    "That fucking perverted, insatiable idiot."
    "Who does he think he is saying all of that in front of a girl’s mother? Asleep or not."
    "He’s lucky I’m such a pushover. And that I’ve probably subjected Sana to this myself before."
    "Guess I’ll just...let them have their fun. Beats having to {i}talk{/i} when I know there’s no way it’ll lead to a happy ending. At least...not the kind I want."
    "I’ll be shocked if I can’t hear them from down here when all it takes to shake that floor is Sana’s footsteps. "
    "But on the bright side, I won’t have to watch it on video this time. And my failures as a mother won’t be broadcast directly to my best friend."
    "I just have to pretend he isn’t my boyfriend. Or that she’s fucking a boy her {i}own{/i} age."

    scene saraisanaughtygirl10
    with dissolve2
    play music "asobeatsexdark.mp3"

    "Who am I kidding when that would barely change anything, though?..."
    "I’d still listen..."
    "I can’t {i}help{/i} but listen because I know now that she {i}wants{/i} me to listen. "
    "And I can’t help but think that all it would take for her to accept me is to open the door while it’s happening..."
    "To watch my little girl masquerade as a woman the same way I did..."
    "I don’t think I’ve ever seen her truly happy before..."
    "I wonder how she looks when she does it...if that smile on film was just an act or if that’s the way she {i}really{/i} is."
    "Knowing me, I bet it’s authentic..."
    "I bet she’ll ride him like her life depends on it..."

    sa "{i}{size=-4}Ah! Fuck! Sensei!{/i}"

    "Oh..."

    scene black
    with dissolve2

    "I never realized just how clearly I’d be able to hear from down here..."
    "........."
    "......"
    "..."

    play sound "bedcreak.mp3" fadein 3.0
    scene saraisanaughtygirl11
    with dissolve2

    sa "I can feel every...inch of you!...You’re so deep inside!...It’s...driving me crazy!"
    s "Just keep your voice down, okay? I don’t want-"

    scene saraisanaughtygirl12
    with dissolve2

    sa "Aaah! AaaaAAAAaaAAAHHHH!"
    s "Sana...what did I just say?"
    sa "I’m sorry, Sensei! I can’t help it! You’re just so big and I’m so little! Aah, it hurts! It hurts!"
    s "It doesn’t {i}hurt,{/i} you fucking liar..."

    scene saraisanaughtygirl13
    with dissolve

    sa "{i}Noooo...{/i}but imagine it {i}did?{/i}"
    sa "You like that, right? I might be in high school, but I’m still the size of a middle-schooler. "
    sa "Would you stoop {i}that{/i} low, Sensei? What’s your...cutoff?..."
    sa "Would you fuck little Sana too? Admit it...show me how...sick you {i}really{/i} are..."
    sa "Close your eyes...pretend I’m even {i}younger...{/i}I’ll even let you tie me up if you want..."

    scene saraisanaughtygirl14
    with fade

    sa "{i}My mom has all sorts of toys, you know...I’m sure there are some handcuffs in there...{/i}"
    sa "{i}You ever use them on her, Sensei?...I bet it’d be more fun with me...I say we...ngh...find out...nghh! Harder! Harder, Sensei!{/i}"
    s "{i}You’re a fucking...freak...Sana!...{/i}"
    sa "{i}Haah...aaah...like mother...like...daughter!{/i}"
    sar "..."

    "I couldn’t stop myself."
    "They’re just a door away now. And whether they are deepening their bond or simply just helping each other drain their sexual frustration, I can hear them."
    "This isn’t how a family sounds, though. This isn’t what I want."
    "When I invited this man into my home, I imagined him as a {i}father{/i} to my little girl. "
    "Do {i}all{/i} fathers only know how to {i}take?{/i}"

    sa "{i}Aaah! Aaah! Cumming! I’m cumming...Sensei!{/i}"
    s "{i}Do it...cum for me, Sana...be a good little girl and...fucking cum for me!{/i}"
    sa "{i}Ahh! Yes! If you...rub my clit...like that...aaah...S...Sensei! Sen...sei!!!!!!!{/i}"

    "This...isn’t {i}taking,{/i} though."
    "Or maybe it is...but is {i}taking{/i} something offered to you really as wrong as it would be to {i}steal{/i} it?"

    sa "{i}Aaah! Aaaah! AaaAaAAAaAAahh!{/i}"
    s "{i}Ngh...mngh!...{/i}"

    "He sounds different with her than he does with me..."
    "I guess it’s true what they say about the newer models outperforming the older ones."

    play sound "static.mp3"
    scene saraisanaughtygirl15 with flash
    stop sound
    play sound "dosex.mp3"

    "It wasn’t always like this, though..."
    "{i}I{/i} was the newest model once...{i}I{/i} was the one who could drive a man to madness with little more than a flash of skin and a well-timed wink."
    "It was {i}me{/i} who could bring out that instinctive drive to {i}destroy{/i} and the primal urge we all feel to just {i}fuck{/i} each other and be happy."
    "I truly didn’t care who heard me or saw me back then...the same way I know {i}Sana{/i} doesn’t care who hears her now."

    sar "Aaah...aaah...aaaah!"

    "Why are we like this?..."
    "Why does each brush with death get our heart pumping the way it does?..."

    him "Keep...your voice...down!"
    sar "I can’t help it...you’re just so big inside of my schoolgirl pussy, Sensei..."

    play sound "static.mp3"
    scene saraisanaughtygirl11 with flash
    scene saraisanaughtygirl15 with flash
    scene saraisanaughtygirl11 with flash
    scene saraisanaughtygirl15 with flash
    scene saraisanaughtygirl11 with flash
    scene saraisanaughtygirl15 with flash
    stop sound

    him "God...I can’t believe I...let you talk me into...doing this in school...again!"
    sar "Everyone...already went home...and I didn’t want to wait any longer! Plus I...aah...my curfew is...earlier!"
    sar "Hah...aaaah!...None of this would’ve happened if you just...fucked me in the bathroom before first period like I...begged you to!"
    him "Fuck...your curfew...you are...{i}mine{/i} after school...you hear me?!"
    sar "Aaah! Aaah! Yes...Sensei! I’m yours...every hour...of every day! My body...is yours...for the taking!"
    him "And no one else’s...right?..."
    sar "Haaah...aaaah...aaaaaaah..."

    play sound "dosex.mp3"
    scene saraisanaughtygirl16
    with hpunch

    him "And...no one else’s...right?!?!?"
    sar "AAAH! AAAAAAH! YES! NO ONE ELSE...SENSEI! NO ONE ELSE...CAN FUCK ME...LIKE YOU DO!"

    play sound "static.mp3"
    scene saraisanaughtygirl17 with flash
    stop sound

    sa "{i}Fuck...yes! Make me into your...little slut...Sensei! Pound my...loli pussy ‘til I...can barely fucking walk! NgaAaAaaAaaHHHH!{/i}"
    s "{i}Jesus...fuck, you’re so tight...Sana...fuck...{/i}"
    sa "{i}Hah...haaah...yes! This is what...you’re missing...every time you...fuck somebody else!{/i}"
    sa "{i}Be mine...be mine! Be mine, mine, mine, mine, mine! AAAAAAH!{/i}"
    sar "Hah..."

    "Like mother, like daughter indeed. "
    "Pledge to give him everything...to {i}be{/i} his everything...then hate yourself when he disappears one day."

    sa "{i}Mmmfgh...mnlch...mlm! Mmm! Mmnnck!{/i}"
    s "{i}Mngh...did you just...bite my fucking lip?...{/i}"

    scene saraisanaughtygirl18
    with dissolve

    sa "{i}Get...used to it...heheh! Mnch!{/i}"

    "I often wonder what I could have done to make him stay."
    "If there was {i}anything{/i} I could have done to make him stay."
    "But of course, that wasn’t something I ever had to think about before he was gone."
    "Maybe Sana learned from this mistake? "
    "Maybe {i}that’s{/i} why she came up with something as ridiculous as inviting her mother into her sex life."
    "But even {i}with{/i} how ridiculous it is...and how much I hate it..."

    scene saraisanaughtygirl19
    with dissolve2

    "I can’t help but wonder..."
    "If I were in there...how would things play out?"

    scene saraisanaughtygirl20
    with dissolve2

    sar "{i}Ahh...ah...{/i}"

    "Would she touch me?..."
    "Would {i}I{/i} touch her?..."
    "And how would {i}he{/i} look as he turns this house into a home — however dysfunctional that home may be?"
    "Would he treat us the same way? Prioritize one or the other?..."
    "How would it work?...What would we {i}do?...{/i}"
    "What does she {i}want{/i} me to do?...I just...I don’t...understand!...Any of it!"
    "None of this...makes...sense! I’m her...mother! Her shameful...worthless...mother! But still...her {i}mother!{/i}"

    scene saraisanaughtygirl21
    with dissolve

    "I’m not supposed to feel this way...I’m not supposed to...enjoy this!"

    scene saraisanaughtygirl22
    with fade

    "But in some strange way...it makes me feel young again."
    "It makes me feel noticed."

    sa "{i}NGHHHHH, YES, YES, YES! OH GOD, YES! GOD, YES! FUCK ME, DADDY! FUCK ME! FUCK ME, FUCK ME, FUCK ME!{/i}"

    "She {i}chose{/i} me...My adorable little girl...finally {i}chose{/i} me..."
    "She wants to share...with her mother...she wants us...to get...closer!"

    s "{i}Sana...Sana...aah...{/i}"

    "I want to see them...I want to be in there...I want him to fuck me beside her...I want her to love me..."
    "I want it inside...oh God, I fucking want it inside...I want to open the door...I want to watch..."

    sar "{i}Sensei...Sensei...{/i}"

    "I know he’s treating her right, because I know how he treats me."
    "And I’m happy for her...but I’m {i}jealous...{/i}"

    scene saraisanaughtygirl23
    with fade

    "I want to cum...I want to cum with my daughter...I want her to see...that I will love her...no matter who...she...aaaah..."

    scene saraisanaughtygirl24
    with dissolve2

    sa "{i}YES! YES! DADDY!{/i}"

    "No...{i}no!...{/i}"
    "I can’t! I shouldn’t enjoy this! Who am I? {i}What{/i} am I?!"

    sa "{i}Inside! Cum inside! Do it! Do it, do it, do it!{/i}"
    sar "{i}Mm! Mmmnh!{/i}"

    "Why is it her in there?! Why did it have to be {i}him?!{/i}"
    "Of {i}course{/i} I’d want to be involved! I love them both! I want to feel this with them! Not out here on my own!"

    scene saraisanaughtygirl25
    with dissolve

    s "{i}Mn...mngh! Mmngh!{/i}"
    sa "{i}Haaah!.....Hah.......aaaahhh....{/i}"

    scene saraisanaughtygirl26
    with dissolve2

    sa "{i}Guh...wow...{/i}"
    sa "{i}You came a lot...Am I that good on top?{/i}"
    s "{i}I’m not convinced you aren’t a succubus.{/i}"
    sar "{i}Hah...hah...aaah...{/i}"

    "He finished inside her...my boyfriend came inside my little girl...and I’m still...I’m..."

    s "{i}Wait...Sana...did you hear that just now?{/i}"

    scene saraisanaughtygirl27
    with dissolve2
    stop music fadeout 10.0

    sar "{i}Ah?...{/i}"
    s "{i}Is Sara- mmf?!{/i}"
    sa "{i}Mlnhm...who cares? Just fuck me again...{/i}"
    sa "{i}Unless...mmf...you’re saying you’d rather go be with her...mnch...{/i}"

    "Please..."
    "Put me out of my misery..."

    sa "{i}Mnch...mlm...mnh!{/i}"
    s "{i}Mn...how can I...leave when...you’re still...like this?...{/i}"
    sa "{i}Heheh...mnh...that’s...mlm...what I like...to hear!{/i}"

    scene black
    with dissolve2

    "I continue to listen."
    "I have to."
    "There is no escape."

    $ renpy.end_replay()
    $ saraspring4 = True
    $ sara_lust += 1
    $ sana_lust += 1

    "{i}Sana’s lust has increased to [sana_lust]!{/i}"
    "{i}Sara’s lust has increased to [sara_lust]!{/i}"
    "{i}It’s two for the price of one!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4

label saraspring5:
    scene nightsky
    with dissolve2

    "{i}In the wettest part of town, two girls who were very commonly wet in a more sexual context were about to become even more wet in a mostly non-sexual context.{/i}"

    scene daughterbath1
    with dissolve2
    play music "summerwind.mp3"

    "{i}At least for now. But who could say what the night would devolve into when they’ve both pleasured themselves to the sound of the other one fucking at least once now?{/i}"
    "{i}{size=-1}The smaller one had made her place known. But the larger one, albeit not much larger, was still feeling somewhat conflicted by the whole thing with her teenage daughter taking dicks the size of her torso.{/i}{/size}"
    "{i}The tears and the anguish had vanished for the moment, though. For tonight, she planned on actually talking to her. And the best place to do that was somewhere she couldn’t drink away the worries.{/i}"
    "{i}{size=-1}She could drown them, though. And if Sana refused to abide by her new set of rules, Sara would kill her in front of this group of unsuspecting, pastel-colored civilians.{/size}{/i}"
    "{i}{size=-1}She would then kill herself. Then her family would be reunited either above or below ground and the guy who’s currently fucking the female members would have to wait a little while until he could do that again.{/i}{/size}"
    "{i}Of course, this was all just speculation. For it was equally plausible that one of them would just finger the other or something. I don’t really know.{/i}"
    "{i}I just know that, whatever it is that happens, it’ll be far easier for the one of them who isn’t used to caring.{/i}"
    "{i}At least not about the things she should.{/i}"

    sar "It’s been a while since we’ve done something like this together, hasn’t it?"
    sa "Have we...{i}ever{/i} done something like this together?"
    sar "Of course! I used to bathe with you all the time when you were little. Back when we could still fit in the tub together."

    scene daughterbath2
    with dissolve

    sa "We probably still could if we tried...I’m just not sure how...necessary that would be at our age."
    sar "You’re right. And it also probably wouldn’t be the best place to have a conversation. "

    scene daughterbath3
    with dissolve

    sa "Right...are you sure this place {i}is,{/i} though?"
    sa "Because I know what you want to talk to me about, and I’m not sure it’s something other people should be around for..."
    sar "It’ll...be fine as long as we keep our voices down. And I don’t start having a panic attack."
    sa "Do you {i}feel{/i} like you’re about to have a panic attack?"
    sar "Like, right now? Or just in general? Because I pretty much always feel like I’m going to have one."
    sa "Okay. But are you closer to doing that now than you normally would be?"
    sar "Yes."

    scene daughterbath4
    with dissolve

    sa "..."
    sar "What?"
    sa "You know we don’t have to do this, right? You can just ignore what happened if you think that’s easier."
    sar "As your mother, I feel like that would be extremely irresponsible of me."
    sa "And as your daughter, I probably shouldn’t have invited you to a-"

    scene daughterbath5
    with dissolve

    sar "{i}Shh! Wait until we’re in a more private spot at least!{/i}"

    scene black
    with dissolve2

    sa "Okay...but I’ll tell you again...we don’t {i}have{/i} to do this..."
    sar "Yeah...we kind of do."

    "........."
    "......"
    play sound "water1.mp3"
    "..."

    scene daughterbath6
    with dissolve2

    sar "Aaaah...there’s nothing like a nice, hot bath after a long day. Don’t you agree, Sana?"
    sa "I can think of at least one thing even better than that."

    scene daughterbath7
    with dissolve

    sar "You’re not giving me any time to ease into things at all, are you?"
    sa "And give you another chance to avoid bringing it up?...You should see this as me doing you a favor."
    sar "A...{i}favor.{/i} "
    sa "Right. If you’re so sure that we {i}have{/i} to talk about it, as your daughter, I should help you out so you don’t keep running away or getting drunk to ignore the elephant in the room."

    scene daughterbath8
    with dissolve

    sar "You laugh, but no amount of drinking can mask the presence of an...{i}elephant{/i} the size of your teacher."
    sa "I can’t tell if...that’s about his penis or not..."
    sar "It wasn’t supposed to be...But it {i}is{/i} pretty massive, isn’t it?"
    sa "{i}Huge.{/i} "

    scene daughterbath9
    with dissolve

    sar "Did it hurt? The first time you guys...you know..."
    sa "That’s...how you want to start this discussion? By asking me how much it hurt?"
    sar "That’s the beginning, isn’t it? I feel like I should ask you everything if I want to better understand what’s...going on here, Sana."
    sa "I don’t think it’s all that hard to understand, Mom..."

    scene daughterbath10
    with dissolve

    sa "You’ve been in my shoes before. You should know better than anyone what I’m going through."
    sa "I like Sensei...and I was tired of sitting around and waiting for him to make the first move, so I did it."
    sar "When? How long has this been going on?"

    scene daughterbath11
    with dissolve

    sa "Over a year ago if you’re not counting, like...{i}actual{/i} sex. He fingered me at Ayane’s house. She wasn’t happy about that when I told her."
    sar "I assume she also told you she came to the bar to talk to me about {i}you{/i} then?"

    scene daughterbath12
    with dissolve

    sa "No...but I kind of had a feeling she would. Especially after she and the other girls tried to make me feel bad about asking you to join me at the love hotel."
    sar "And...you {i}don’t{/i} feel bad about that?"
    sa "Of course not. Which is why I told them they just didn’t understand how we are. How we’re {i}different{/i} from a...{i}normal{/i} family."

    scene daughterbath13
    with fade

    sar "Different...{i}how,{/i} Sana? I don’t understand what you mean by that."
    sa "Well, we’re not...{i}close{/i} the way a lot of people like us are. You had me at a young age and...you’re just as much of a friend as you are a mom, I think."
    sar "Only because {i}my{/i} parents never gave me the freedom I give you."

    scene daughterbath14
    with fade

    sa "You had enough freedom to get knocked up by your teacher, though."
    sar "Sana! That...I..."

    scene daughterbath15
    with dissolve

    sa "Don’t get me wrong...I’m not trying to guilt you for that or anything. I’m just saying that...I can sort of relate to you in a way I can’t with any other adult I know..."
    sar "Because I’m your {i}mother.{/i} "
    sa "You are. But you’re also a pervert with the same taste in boys who knows how to get their attention. I am what I am because of {i}you.{/i}"
    sar "You don’t need to remind me...That’s not something I’m proud of, Sana."
    sa "Why not? I’m happy. Isn’t that all you want for me?"

    scene daughterbath16
    with fade

    sar "Yes! It’s {i}all{/i} I want for you! But you’re making it sound like I {i}endorse{/i} what you’re doing just because it’s exactly what {i}I{/i} did!"
    sa "Do you not?..."
    sar "No! I just..."

    scene daughterbath17
    with dissolve2

    sar "I know I can’t tell you {i}not{/i} to. Because I...I don’t want to take your free will away when I’ve done nothing but reap the benefits of the poor choices I’ve made in the past."
    sa "Right. Which is what the other girls won’t understand about us. "
    sa "You see me as more than {i}just{/i} your daughter. You see me as an equal. "

    scene daughterbath18
    with dissolve2

    sar "No, Sana...I see you as my daughter and {i}only{/i} my daughter. It’s the most important thing in the world to me, so tying any {i}other{/i} role to that is-"
    sa "Sorry...if you see me as only your daughter, why were you sitting outside of my door masturbating while I had sex with Sensei the other night?"

    scene daughterbath19
    with dissolve2

    sar "..."
    sa "..."
    sar "You..."
    sar "You heard that?..."

    scene daughterbath20
    with fade

    sa "Mhm. That’s why I pulled Sensei in for round two. It was a power move."
    sar "Ah...I...oh God...um-"

    scene daughterbath21
    with dissolve

    sa "You don’t have to feel bad about it, Mom. I’ve done it too. "

    scene daughterbath22
    with fade

    sar "What do you mean you’ve done it too?! You {i}hate{/i} that I’ve been seeing Sensei! You {i}hate{/i} how I-"
    sa "Shh...don’t be {i}too{/i} loud or everyone here will find out how naughty we are..."

    scene daughterbath23
    with dissolve2

    sar "Have you really been...listening to us like that?..."
    sa "Mhm..."

    scene daughterbath24
    with fade

    sa "I won’t lie...I hated it at first...listening to you go at it for hours...and {i}hours...{/i}"
    sa "Then one day, I got so tired of it that I told myself I was going to go up there and give you two a piece of my mind..."

    scene daughterbath25
    with dissolve2

    sa "But when I made it upstairs...when I finally made it to the door...and knew that {i}right{/i} behind it...my teacher was having his way with someone who looked {i}just like me?...{/i}"
    sa "Let’s just say my hand gained a mind of its own."
    sar "Oh my God...I had no idea...I’m sorry, Sana...I’m sorry...I never should have done that in the house...I never should have-"
    sa "Again, you’re not getting it."

    play sound "static.mp3"
    scene daughterbath26 with flash
    stop sound

    sa "It doesn’t {i}bother{/i} me. And the only reason it’s bothering {i}you{/i} is because you’re blaming yourself for stuff that’s beyond your control, Mom."
    sa "I’d have slept with Sensei no matter {i}what{/i} you did because something inside us just makes us...hungry."
    sar "...Hungry?"
    sa "I know you feel it...that...{i}heat...{/i}"
    sa "That never-ending need to let someone else {i}in{/i} and help you feel all those things you can’t make {i}yourself{/i} feel. And I’m sorry."
    sa "I’m sorry I ever blamed you for acting on those feelings with Sensei...if I had only known how much you were hurting, I would have never been mad at all."
    sar "..."
    sa "Don’t look at me like that...like you’re disappointed in me..."
    sar "Sana, I’m...not disappointed...I’m just...I’m confused..."
    sar "I...understand wanting to act on your feelings...I understand needing someone else to feel...{i}whole...{/i}"
    sar "What I don’t understand is what compelled you to ask me to {i}join{/i} you...{i}that’s{/i} what hurts. Because it..."
    sar "It feels like..."
    sa "Feels like {i}what?...{/i}"

    scene daughterbath27
    with dissolve2

    sar "It feels like you don’t respect me..."
    sa "That’s not it..."
    sar "And also that you know I can’t ever say no to you."
    sa "..."
    sar "..."

    scene daughterbath28
    with dissolve

    sa "Okay...{i}that{/i} one...might be a little true."
    sar "How can you just take advantage of me like that?...Did you not think about my feelings at all?...How {i}I’d{/i} feel watching my daughter fuck my boyfriend in front of my best friend?"

    scene daughterbath29
    with dissolve

    sa "Sensei’s {i}not{/i} your boyfriend, Mom."
    sar "Well...{i}whatever{/i} he is! Do you have any idea the emotional whiplash that caused me?! How am I supposed to face Haruka now?!"
    sa "I imagine it’d be...pretty easy since Haruka was invited too..."
    sar "That’s beside the point! You can’t just...ask your mother to...do things like that with you! You didn’t even talk to me first! You just threw me to the wolves and let them devour me!"
    sa "You’re right. But I’m talking to you now."
    sar "Don’t do it, Sana. Really. Don’t-"
    sa "Let’s have a threesome with Sensei. Let’s show him that there’s a {i}real{/i} family waiting for him and all he needs to do is accept us."

    scene daughterbath30
    with dissolve

    sar "{i}Mnh...{/i}"
    sa "You’re {i}not{/i} a bad mom...you’ve been exactly what I need. {i}I’m{/i} the one who’s been a letdown. So if anyone is-"
    sar "Please don’t...go putting yourself down or...taking any of the blame, Sana..."
    sar "No matter how you look at this, it all comes back to me..."
    sar "I’ve failed you. I’ve failed you and...created a world where your perception of what’s right and wrong is so warped that you see {i}no{/i} issue at all in inviting me into an incestuous polycule."
    sa "It’s not that I can’t see what’s right and wrong, Mom..."
    sa "{i}I just don’t care.{/i}"

    scene daughterbath31
    with dissolve

    sar "How?...{i}Why?...{/i}"
    sa "Because I {i}tried{/i} to live that way and I hated it. I hated everyone else having fun while {i}I{/i} struggled all alone in the dark."
    sar "You have never been alone. I have always been there, Sana. I will always {i}be{/i} there."
    sa "That’s not what I mean and you know it."

    scene daughterbath32
    with dissolve

    sa "We’re different, Mom...and it’s {i}okay{/i} that we’re different because {i}we{/i} won’t judge each other for that. Who cares what anyone else thinks?"
    sar "You..."
    sar "You {i}really{/i} don’t think I’m a failure?...You’re not just saying that to...appease me?"
    sa "If I was just saying things to appease you, I wouldn’t be offering to share the guy I like."
    sar "How..."

    scene daughterbath33
    with dissolve2

    sar "...would that work, by the way? I don’t...really understand what...you have in mind...exactly..."
    sa "Like...how would having a threesome with Sensei work?"
    sar "Right...like...you’re still my daughter...so are we just...both {i}there?{/i} Or..."
    sa "I mean...I’ve realized I like girls too, so..."
    sar "Sure...and, so do I...but...you know...we’re still..."
    sa "..."
    sar "..."
    sa "Want to just...see what happens?"

    scene daughterbath34
    with dissolve

    sar "Sana..."
    sa "We don’t {i}have{/i} to, Mom. Just..."
    sa "{i}I’m{/i} okay with it if you are. I wasn’t {i}only{/i} trying to win a competition or make you look bad in front of your friend. That was just a tiny {i}part{/i} of it."
    sar "Sensei...still doesn’t even know that {i}I{/i} know, does he?"
    sa "No. But please don’t tell him because I have a feeling it’ll make him mad at me and I don’t want to stop having sex. I think I’m addicted."
    sar "Mnh...I’ve always looked forward to being able to talk to you about this stuff..."
    sar "I just also felt like you’d be older and I’d be...way less involved."
    sa "You’ll be involved in everything now, Mom. "

    scene daughterbath35
    with dissolve2

    sar "What?..."
    sa "Yeah..."
    sa "You’ve given me more than enough space so far...and I know how hard that must have been."
    sa "But I want to change that...I want to be closer to you...especially since I know now that you’ve never {i}wanted{/i} to be my equal. You just...were..."
    sar "So...we can be...more like...{i}family?{/i} You won’t just...avoid me anymore? I won’t embarrass you?..."
    sa "You’ll still embarrass me, sure. But I can embarrass you too."
    sar "Not in front of Sensei, please. "
    sa "Same for you. Truce?"
    sar "Truce."
    sa "For everyone else, though...they’ll see a new side of me. They’ll realize what I meant by {i}our{/i} connection being different."
    sar "I love you, Sana...I really do. No matter what."
    sa "I love you too, Mom. No matter what. "

    scene daughterbath36
    with dissolve

    sa "Oh. Can you do me a favor, though? If not, it’s okay."
    sar "Um...sure. Yeah. What...what is it?"

    scene nightsky
    with dissolve2

    sa "Okay, so...I want to get better at giving head. And I was wondering if you had any tips as someone who’s done it- Mom?"

    play sound "water1.mp3"

    sar "Sorry, I..."
    sar "I think I’m...overheating...from the bath. "
    sar "Are you ready to get out? I’m ready to get out. Let’s get out."
    sa "Heh...okay..."
    sa "Don’t ask for tips yet..."
    sa "Got it..."

    "{i}So yeah! Wetness prevails and incest is inevitable and all that good stuff. You know how it is.{/i}"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "{i}Is this really how a “family” is formed, though? Or does such a thing require a bit more than just intimate contact?{/i}"
    "{i}If you ask the man who used to be involved with these two, I’m sure you’d get a different answer than the one their current fuckstick would give you.{/i}"
    "{i}I guess it doesn’t really matter what family means to either one of them, though. Especially now that they’ve had their little talk.{/i}"
    "{i}What matters is if they can figure out how to position that fuckstick in a way that can provide pleasure to both of them rather than leaving one begging for more.{/i}"
    "{i}Are you up to the task, my glorious puppeteer?{/i}"

    menu:
        "There is no real choice":
            "{i}Good.{/i}"
        "The only answer is yes":
            "{i}Good.{/i}"

    "{i}I knew you would be.{/i}"
    "{i}Just as I knew that it was only a matter of time until the summer claimed one more.{/i}"

    "///////////YOU watch IT slink BACK into ITS grave, ENVIOUS of THE way IT burns THAT which IT never SEES"
    "///////////WHO will THE heat CLAIM next????"
    "{s}tgoxgxhor knz ,eraxz yxaue{/s}"

    $ renpy.end_replay()
    $ saraspring5 = True
    $ sara_lust += 1
    $ sana_lust += 1
    $ sarablock = False

    "{i}Sana’s lust has increased to [sana_lust]!{/i}"
    "{i}Sara’s lust has increased to [sara_lust]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsatch4
    else:
        jump endofweekdaych4
